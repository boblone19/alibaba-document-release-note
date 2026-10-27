---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition User Guide 20250613"
product_version: "V3.18.3"
doc_version: "20250613"
pdf_pages: 139
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition User Guide 20250613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%AE%89%E9%AA%91%E5%A3%AB/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Server%20Guard%20Advanced%20Edition%20User%20Guide%2020250613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition User Guide 20250613

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 Server Guard
  - 3.1 View the security overview of servers
  - 3.2 Assets
    - 3.2.1 Manage assets
    - 3.2.2 Use the server fingerprints feature
  - 3.3 Threat protection
    - 3.3.1 Vulnerability management
      - 3.3.1.1 Scan for vulnerabilities and view vulnerability statistics
      - 3.3.1.2 Manage Linux software vulnerabilities
      - 3.3.1.3 Manage Windows system vulnerabilities
      - 3.3.1.4 Manage Web-CMS vulnerabilities
      - 3.3.1.5 Manage application vulnerabilities
      - 3.3.1.6 Configure vulnerability management policies
    - 3.3.2 Baseline check
      - 3.3.2.1 Baseline check overview
      - 3.3.2.2 Manage baseline check policies
      - 3.3.2.3 View baseline check results and handle baseline risks
    - 3.3.3 Risk exposure detection
    - 3.3.4 Application protection
  - 3.4 Intrusion prevention
    - 3.4.1 Use the antivirus feature
    - 3.4.2 Web tamper proofing
    - 3.4.3 Application whitelist
    - 3.4.4 Attack analysis
    - 3.4.5 Security alert
      - 3.4.5.1 Overview
      - 3.4.5.2 View and handle alerts
      - 3.4.5.3 View exceptions related to an alert
      - 3.4.5.4 Quarantine
      - 3.4.5.5 Configure alerts
    - 3.4.6 SDK for malicious file detection
    - 3.4.7 Use the core file monitoring feature
  - 3.5 Log retrieval
    - 3.5.1 Log retrieval overview
    - 3.5.2 Query logs
    - 3.5.3 Supported log sources and fields
    - 3.5.4 Logical operators
  - 3.6 Server settings
    - 3.6.1 Install the Server Guard agent
    - 3.6.2 Manage protection modes
    - 3.6.3 Configure defense rules
- 4 System configuration
  - 4.1 Log on to the Apsara Uni-manager Management Console
  - 4.2 Rules
    - 4.2.1 Manage Anti-DDoS Service rules
    - 4.2.2 Manage Server Guard rules
    - 4.2.3 Create and manage WAF rules
    - 4.2.4 Create and manage IPS rules
  - 4.3 Configure alert settings
  - 4.4 Global configuration
    - 4.4.1 Configure the attack blocking feature
  - 4.5 Cloud Firewall monitoring
  - 4.6 Account management
    - 4.6.1 Manage Apsara Stack tenant accounts
    - 4.6.2 Manage Alibaba Cloud accounts

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

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ %
> **Forget password**
> If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging on to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For information about how to enable MFA and bind an MFA device, see Manage MFA.

## 3 Server Guard

### 3.1 View the security overview of servers

**servers**

This topic describes how to view the details of server security on the Security Overview page in the Server Guard console. This helps security administrators obtain the security status of servers in the cloud. This topic describes how to view the security status of servers.

**Security Overview**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Security Overview**.
4. Click the **Security Overview** tab to view the security overview and security trend
dashboard. 安全总览 This tab displays the numbers of security vulnerabilities and security events on servers. For security vulnerabilities, you can view **Unhandled Vulnerabilities** and **Baseline Risks**. For security events, you can view **Unhandled Alerts**, **Precision Defense (Last 15**
**Days)**, and **File Tampering Attempts Prevented in Last 15 Days** .
**Server Risks**: This section displays the number of unhandled vulnerabilities, the number
of baseline risks, and the distribution of risk levels.
**Asset Protection**: This section displays the number of protected servers and the
number of offline servers.
**Recent Important Security Risks and Intrusions**: This section displays the recent
risks and events on your servers. You can click a risk or an event to view the details.
**Operating System Distribution**: This section displays your servers by operating
system.

**Security Dashboard**

This tab displays data such as assets, vulnerabilities, baselines, and alerts. You can configure the custom content of a dashboard based on your business requirements.

**Important**

> In multi-level organization mode, the security dashboard can be accessed only when you have the required permissions and specify the view as all resource sets in the level-1 organization.

**Configure the custom content of a dashboard**

1. On the **Security Dashboard** tab, click **Direct access**.
访问
2. In the upper-right corner the SAS page, click the
icon.
3. After you complete the following configurations, click **Save**.
On the **Select Statistics** tab, select the type of data that you want to display in real time on the dashboard. You can select **All** or a data type. On the **Configurations** tab, configure the **Title** and **Title Decoration** parameters.

**Create a custom scenario-specific dashboard**

You can create custom scenario-specific dashboards based on your business requirements.
1. On the **Security Dashboard** tab, click **Direct access**.
访问
2. In the upper-right corner the SAS page, click the
icon.
3. Click **Create**, complete the following configurations, and then click **Save**.
On the **Select Statistics** tab, select the type of data that you want to display in real time on the dashboard. You can select **All** or a data type. On the **Configurations** tab, configure the **Title** and **Title Decoration** parameters. If you want to display a dashboard, find the dashboard on the **Scenarios** page and click
**Enable Now**.

> **Note:** The number of dashboards that you can create is unlimited.

**Introduction to the dashboard**

**Vulnerability**

The **Vulnerability** section displays the total number of vulnerabilities in your assets, a doughnut chart that shows the proportions of vulnerabilities of different priorities, the number of vulnerabilities of each priority, and a chart that shows the vulnerability information in the last seven days. The **Vulnerability** section displays the following information:
**Total**: the total number of vulnerabilities in your assets.
**Urgent**: the number of vulnerabilities that must be fixed at the earliest opportunity. The
status icon is a red dot.
**Moderate**: the number of vulnerabilities that can be fixed at a later point in time. The
status icon is an orange dot.
**Low**: the number of vulnerabilities that cannot be fixed. The status icon is a gray dot.
A chart that shows the number of vulnerabilities of each priority in the last seven days.

**Assets**

The **Assets** section displays the statistics about detected assets. The **Assets** section displays the following information:
**Total**: the total number of assets.
**Compromised**: the number of servers with unhandled high-risk alerts. The status icon is a
red dot.
**At-risk**: the number of servers with vulnerabilities, baseline risks, or medium- or low-risk
alerts. The status icon is an orange dot.
**Safe**: the number of servers without vulnerabilities, baseline risks, or alerts. The status icon
is a green dot.
**Unknown**: the number of low-risk vulnerabilities that can be exploited over the Internet in
your servers. The status icon is a gray dot. A list that displays the top five high-risk assets and the corresponding status.

**Baseline Check**

The **Baseline Check** section displays the total number of baseline risks in your assets, the number of check items at each risk level, and a chart that shows the check items at each risk level in the last seven days. Real-time data is displayed. The **Baseline Check** section displays the following information:
**Total**: the total number of at-risk check items in your assets.
**High**: the number of high-risk check items. The status icon is a red dot. We recommend
that you troubleshoot and handle the risks at the earliest opportunity.
**Medium**: the number of medium-risk check items. The status icon is an orange dot.
**Low**: the number of low-risk check items. The status icon is a gray dot.
A chart that shows the check items at each risk level in the last seven days.

**Security Trend**

The **Security Trend** section displays the trend chart of security scores in the last seven days, 15 days, or 30 days. Real-time data is displayed.

**Alert**

The **Alert** section displays the information about the top 5 unhandled high-risk alerts in the last 24 hours, including the alert time, alert name, and the affected servers.

**Attack Source Top5**

The **Attack Source Top5** section displays the top 5 attacker IP addresses and the number of attacks from the top 5 IP addresses on your server in the last 24 hours.

**Cloud Platform Best Practices**

The **Cloud Platform Best Practices** section displays the information about the check items that are detected by the configuration assessment feature in real time. The Cloud Platform Best Practices section displays the following information:
**Check Item**: the check items that are supported by the configuration assessment feature.
**Risk Level**: the risk level of a check item. The following items describe the relationship
between colors and risk levels. Red: indicates a high level of risk. Orange: indicates a medium level of risk. Gray: indicates a low level of risk. Green: indicates a normal state.
**Affected**: the number of affected assets.

**Most Vulnerable Assets**

The **Most Vulnerable Assets** section displays the top 5 vulnerable assets in the last 24 hours.

### 3.2 Assets

#### 3.2.1 Manage assets

After you add servers to Server Guard, you can manually synchronize the information about the most recent servers, view server information, and manage servers by group. This topic describes how to manage servers.

**Synchronize the information about the most recent servers**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Assets** > **Asset Management**.
4. On the **Assets** page, click **Synchronize Assets**.
Server Guard obtains the information about the most recent servers and updates the server list.

> **Note:** The system takes 1 minute to update the information. Wait until the information is updated.

**View the server information**

On the **Assets** page, view the server information. View the information about servers that match one or more filter conditions. You can configure filter conditions above the server list to search for a server. The filter conditions include **Instance Name**, **Internet IP**, and **Private IP Address**. You can configure one or more filter conditions. Find a server that you want to manage and view the security status of the server in the
**Risk Status** column.
Find a server whose details you want to view and click **Fix** in the **Details** column. On the details page of the server, view the details of the server.

| Tab | Description |
|---|---|
| Basic Information | Risk Status: displays risks such as vulnerabilities and alerts. Details: displays the basic information about the server, such as the server ID, region, group, and operating system. You can click Group to change the group to which the server belongs. Cloud Disk Snapshot: displays disk snapshots. Vulnerability Check: displays the types of vulnerabilities that can be detected. You can find a vulnerability type and click the icon to enable or disable the detection of vulnerabilities of the type for the server. Asset Investigation: displays server fingerprints. Logon Security Settings: displays the approved logon locations, approved IP addresses, approved time ranges, and approved accounts. You can manage alerts for the server. Approved Logon Location: Click Manage to specify approved logon locations. Common Login IPs: Click Manage to specify approved IP addresses. Common Login Time: Click Manage to specify approved logon time ranges. Common Login Accounts: Click Manage to specify approved logon accounts. |
| Vulnerabilities | This tab displays the vulnerabilities that are detected on the server. |
| Alerts | This tab displays the alerts that are generated for the server. |
| Internet Exposures | This tab displays information about servers that are exposed on the Internet. |
| Baseline Risks | This tab displays the baseline check results of the server. |
| Asset Fingerprints | This tab displays the fingerprints of the server. You can view the historical change records such as add, remove, or modify in the previous 1 week, 1 month, 3 months, or 1 year. |

View the information about servers in a category. Server Guard allows you to manage servers by category. The categories include **Security Risks** and **Asset Attributes**. In the server list, you can perform the following operations.

| Operation | Procedure |
|---|---|
| Classify servers | i. Select the required servers and choose Asset Classification > Group below the server list. ii. In the Group dialog box, select a group and click OK. |
| Send commands to servers | i. Select the required servers and click Order Issuance below the server list. ii. In the Order Issuance dialog box, select required items and click OK. |
| Export information | Select the server whose information you want to export and click the information that you want to export below the server list. You can export basic asset information, weak password information, asset vulnerability information, baseline risk information, baseline check information, and client logs. |
| Enable protection | i. Select the required servers and choose More Operations > Enable Protection below the server list. ii. In the message that appears, click OK. |
| Remove servers from Server Guard | Select the required servers and choose More Operations > Remove Assets below the server list. |
| Disable protection | i. Select the required servers and choose More Operations > Disable Protection below the server list. ii. In the message that appears, click OK. Note After you disable protection for a server, all detection and protection capabilities cannot be used, including fingerprint collection, vulnerability management, baseline checks, antivirus, web tamper proofing, and application whitelist. The heartbeat of the Server Guard agent is not affected. |

**Add multi-cloud servers**

Server Guard allows you to protect and manage third-party cloud servers and servers in data centers. The following procedure describes how to add a multi-cloud or data center provider.
1. In the left-side **Asset Management by Classification** section of the **Assets** page, click
**Providers**.
2. On the page that appears, click **Create Provider**. In the dialog box that appears, configure
the Provider Name **parameter.** If the provider does not define regions, retain the default region created by the system to manage data center information. After the provider is added, you can perform the following operations in the **Actions** column: **Edit**, **Delete**, and **Add Region**.

**Manage server groups and tags**

In the left-side navigation tree of the **Assets** page, manage server groups and tags. Manage server groups: You can add servers to server groups in advance. This way, when you use the features of Server Guard, you can select servers on which you want the features to take effect by server group. The features include web tamper proofing, baseline check, and vulnerability scan. In the left-side navigation tree, click **Server Groups** below **Asset Management by**
**Classification**. On the page that appears, you can manage server groups.
Create a server group: Click**Add Group**. In the dialog box that appears, enter a group name in the **Group name**field, select the servers that you want to add to the group, and then click**OK**. Modify a server group: Find the server group that you want to modify and click**Manage** in the**Actions**column. Delete a server group: Find the server group that you want to delete and click**Delete** in the**Actions**column. Manage server tags: You can add **tags** to servers to identify their special attributes. This allows you to search for servers that have the same attributes. In the left-side navigation tree, manage server tags in the **Tag** section. Create a tag: Click **Manage**. In the Add Tag dialog box, enter a tag name, select the servers to which you want to add the tag, and then click **OK**. Delete a tag: Find the tag that you want to delete and click the icon. In the **Note** message, click**OK**.

#### 3.2.2 Use the server fingerprints feature

This topic describes how to view the information about the listening port on a server, the software version, the process, the account, the scheduled task, and middleware.

**View server fingerprints**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Assets** > **Server Fingerprints**.
4. On the **Server Fingerprints** page, view the server fingerprints.
On the **Overview** tab, view the server fingerprints.

**Port**

> **Note:** You can view information about listening ports to perform the following checks: check for servers that monitor a specific port and check for ports that is monitored by a specific server.

On the **Port** tab, view the **Port**, **Protocol**, and Server Information parameters. You can search for a port by port number, server process name, server name, or server IP address. In the server information list, you can view the **process**, **IP address**, and **most**
**recent scan time** of a server.

**Manage software versions**

> **Note:** You can view information about software versions to perform the following checks and operation: check for software assets that are installed without authorization, check for outdated versions of software assets, and identify affected assets if vulnerabilities are detected.

On the **Software** tab, view all the **software assets** that are in use and the **numbers of**
**servers** that use the software assets.
You can use software name and another search condition, such as version, installation directory, server name, or server IP address, to search for specific software. If you use version as the second search condition, digits or letters that are separated by a delimiter in a component of a version number can contain up to five characters in length, and a version number can contain up to five components. If a version number contains more than five components, only the five components from the left are used. The following list describes the supported search conditions: The value **6.2.1**. The value is used to search for packages whose versions are 6.2.1. A value **greater than 6.2.1**. The value is used to search for packages whose versions are later than 6.2.1. A value **smaller than 6.2.1**. The value is used to search for packages whose versions are earlier than 6.2.1. A value **greater than 6.2.1 and smaller than 6.2.5** . The value is used to search for packages whose versions are later than 6.2.1 and earlier than 6.2.5. Click software to view the details, such as the software versions and the servers that use the software. You can click the icon in the upper-right corner to download a software version table to your computer for subsequent asset check.

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

On the **Server Fingerprints** page, click the **Middleware** tab. On the tab that appears, view the number of middleware fingerprints of all tasks. You can use middleware name or type and another search condition, such as server IP address, port, or version, to search for specific middleware. If you use version as the second search condition, digits or letters that are separated by a delimiter in a component of a version number can contain up to five characters in length, and a version number can contain up to five components. If a version number contains more than five components, only the five components from the left are used. The following list describes the supported search conditions: The value **6.2.1**. The value is used to search for packages whose versions are 6.2.1. A value **greater than 6.2.1**. The value is used to search for packages whose versions are later than 6.2.1. A value **smaller than 6.2.1**. The value is used to search for packages whose versions are earlier than 6.2.1. A value **greater than 6.2.1 and smaller than 6.2.5** . The value is used to search for packages whose versions are later than 6.2.1 and earlier than 6.2.5. Click a middleware name to view the middleware details such as the assets, version, and installation path.

**Manage startup items**

On the **Server Fingerprints** tab, click the **Startup Items** tab to view the startup items and the number of fingerprints.

**Configure the fingerprint collection frequency for servers and**

**record retention settings**

**Important**

In multi-level organization mode, only an account that has level-1 organization permissions or global organization permissions can modify the fingerprint collection

> frequency for servers and the record retention settings.

1. In the upper-right corner of the **Server Fingerprints** page, click **Settings**.
2. On the **Collection Cycle Settings** tab of the **Settings** dialog box, configure the
fingerprint collection frequency.
3. On the **Record Retention Settings** tab of the **Settings** dialog box, specify a value for
**Account Change Periods**.

### 3.3 Threat protection

#### 3.3.1 Vulnerability management

##### 3.3.1.1 Scan for vulnerabilities and view vulnerability statistics

**vulnerability statistics**

This topic describes how to scan for vulnerabilities and view vulnerability scan results and fixing statistics.

**Perform vulnerability scan**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Vulnerabilities** page, manually perform a vulnerability scan or run an automatic
periodic scan task on your servers. Manually perform a vulnerability scan: If you want to immediately check whether vulnerabilities exist in your servers, you can use the quick scan feature to scan your servers for vulnerabilities. Before you perform quick scan, perform the following steps to check whether the required servers exist in the system: Click **Settings** in the upper-right corner of the
**Vulnerabilities** page. In the **Settings** panel, click **Manage** to the right of a vulnerability
type. a. On the **Vulnerabilities** page, click **Scan Now**. b. In the **One-click detection** dialog box, select the type of vulnerabilities that you want to scan for and click **OK**. After a scan task is created, wait for 15 minutes before you can stop the scan task.

**Note**

If you did not specify the servers on which the vulnerability scan task runs, the scan task runs on all assets that are protected by Server Guard and is complete within 30 minutes. You can refresh the page to view the most recent scan results. Run an automatic periodic scan task. You can configure a scan cycle for an automatic periodic scan task. Then, Security Center runs the automatic periodic scan tasks to scan for vulnerabilities on your servers on a regular basis. For more information, see the **Configure vulnerability management po**
**licies** topic in **Vulnerabilities**.

**View vulnerability scan results**

In the upper part of the **Vulnerabilities** page, you can view the overall information about vulnerabilities.

| Parameter | Description |
|---|---|
| High-priority Vulnerability (CVE) | Click the number below High-priority Vulnerability (CVE) to go to the High- priority Vulnerability (CVE) panel. In this panel, you can view security bulletins for all types of vulnerabilities with the high priority. For more information about how to fix vulnerabilities, see the topics in Vulnerability management. |
| Vul Servers | Click the number below Vul Servers to go to the Server(s) tab of the Assets |
| Fixing | Click the number below Fixing to go to the Fixing panel. In this panel, you can view the list of vulnerabilities that are being fixed and the fixing progress. |
| Fixed Today | Click the number below Fixed Today to go to the Fixed Today panel. In this panel, you can view the list of the vulnerabilities that are fixed on the current day and the fixing details. |
| Total Fixed | Click the number below Total Fixed to go to the Total Fixed panel. In this panel, you can view information about the assets affected by vulnerabilities that are fixed. |

| Disclosed Vulnerabilities | Click the number below Disclosed Vulnerabilities to go to the Detectable Vulnerabilities panel. In this panel, you can view the list of and details about the vulnerabilities that can be detected by Security Center. The details include CVE IDs, vulnerability names, vulnerability detection methods, and vulnerability disclosure time. In this panel, you can also enter a CVE ID or a vulnerability name above the vulnerability list to search for a vulnerability. This way, you can check whether the vulnerability can be detected by Server Guard. You can click the CVE ID of a vulnerability to view details about the vulnerability in the Alibaba Cloud vulnerability library. |
|---|---|
| Detection Time of Latest Vul | View the time when the system was last scanned for vulnerabilities. |

##### 3.3.1.2 Manage Linux software vulnerabilities

This topic describes how to manage Linux software vulnerabilities.

**Background information**

Apsara Stack Security automatically scans software that is installed on your servers to detect the vulnerabilities in the Common Vulnerabilities and Exposures (CVE) list. Apsara Stack Security also sends you alert notifications about the detected vulnerabilities. In addition, Apsara Stack Security provides commands that you can use to fix vulnerabilities and allows you to verify vulnerability fixes.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.

**Note**

You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Linux Software** tab, view the detected Linux software vulnerabilities.

> **Note:** You can search for specific vulnerabilities by using the search and filter features.

5. Click a vulnerability. In the panel that appears, you can view the details of the vulnerability
and the assets that are affected by the vulnerability.

> **Note:** You can find affected assets by using the search and filter features.

**Details**: This tab displays the basic information about the vulnerability, including the CVE
ID, vulnerability impact score, and the security bulletin. You can click the **CVE ID** to view more information about the vulnerability.
**Pending vulnerability**: This tab displays the servers that are affected by the
vulnerability.
6. Fix a vulnerability based on the impact.
Table 1 Actions to fix vulnerabilities

| Action | Description |
|---|---|
| Fix | Use fixing commands: Run the commands that are automatically generated on the server to fix the vulnerability. Quick fix: Directly fix the vulnerability in the Server Guard console. |
| Restarted and Verified | If a vulnerability fix takes effect only after a server reboot, reboot the server after the status of the vulnerability changes to Handled (To Be Restarted). After you reboot the server, click Restarted and Verified. The vulnerability is fixed. |
| Ignore | If you select this action to ignore a vulnerability, the system no longer reports alerts for the vulnerability. |
| Verify | Click Verify to verify the vulnerability fix. If you do not manually verify a fix, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.3 Manage Windows system vulnerabilities

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

| Operation | Procedure |
|---|---|
| Fix | Select this action to fix the vulnerability. The system caches an official Windows patch in the cloud. Your server can automatically download the patch for updates. |
| Ignored. | If you select this action to ignore a vulnerability, the system no longer reports alerts for the vulnerability. |
| Verify | Click Verify to verify the vulnerability fix. |
| Restarted and Verified | If a vulnerability fix takes effect only after a server reboot, reboot the server after the status of the vulnerability changes to Handled (To Be Restarted). After you reboot the server, click Restarted and Verified. The vulnerability is fixed. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.4 Manage Web-CMS vulnerabilities

This topic describes how to manage Web-CMS vulnerabilities.

**Background information**

The Web-CMS vulnerability detection feature obtains information about the latest vulnerabilities and provides patches in the cloud. This helps you detect and fix vulnerabilities.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.

**Note**

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
|---|---|
| Verify | Click Verify to verify the vulnerability fix. If you do not manually verify the fix of a vulnerability, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |
| Roll Back | For vulnerabilities that have been fixed, click Roll Back to restore the web files that have been replaced. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.5 Manage application vulnerabilities

This topic describes how to manage application vulnerabilities, including urgent vulnerabilities.

**Background information**

Apsara Stack Security automatically detects vulnerabilities on servers, such as the unauthorized Redis access vulnerability and Struts S2-052 vulnerability, and generates vulnerability alerts. After you fix a vulnerability, you can also check whether the fix is successful.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.

**Note**

You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Application(Urgent Vulnerability Included)** tab, view all vulnerabilities.
You can search for a specific vulnerability by using the search and filter features.
5. Click the name of a vulnerability. In the panel that appears, view the details in the following
sections: **Details**, **Suggestions**, and **Pending Vulnerabilities**. You can find affected assets by using the search and filter features.
6. Handle the vulnerability based on its impact. The following table describes the actions that
are used to fix vulnerabilities. Follow the instructions to manually fix the vulnerabilities on the Application(Urgent Vulnerability Included) tab. Table 1 Actions to fix vulnerabilities

| Action | Description |
|---|---|
| Ignore | If you select this action to ignore a vulnerability, the system no longer reports alerts for the vulnerability. |
| Verify | Click Verify to verify the vulnerability fix. If you do not manually verify a fix, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.6 Configure vulnerability management policies

**policies**

You can enable or disable automatic detection for different types of vulnerabilities and enable vulnerability detection for specific servers. You can also specify a time duration during which invalid vulnerabilities are retained and configure a vulnerability whitelist.

**Background information**

A vulnerability whitelist allows you to exclude vulnerabilities from the detection list. You can add multiple vulnerabilities in the vulnerability list to the whitelist. The system does not detect vulnerabilities that are added to the whitelist. You can manage the vulnerability whitelist on the vulnerability settings panel.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. In the upper-right corner, click **Settings** to configure vulnerability management policies.
Configure policies in non-multi-level organization mode

| Item | Description |
|---|---|
| Whether to enable detection for vulnerabilities. | Find a vulnerability type and enable or disable detection for vulnerabilities of this type. |
| Effective Asset Range | Click Manage next to a vulnerability type and specify the servers on which vulnerabilities of this type are detected. |
| Retain Invalid Vulnerabilities For | Select a period of time during which invalid vulnerabilities are retained. Valid values: 7 days, 30 days, and 90 days. Note If you do not handle a detected vulnerability, the system determines that the alert for the vulnerability is invalid. The system deletes the vulnerability after the specified period of time ends. |
| Scan cycle | Select the scan cycle for vulnerabilities. Default value: 00:00 to 06:00 every day. The configuration of the scan cycle applies only to the detection of Linux software vulnerabilities, Windows system vulnerabilities, and application vulnerabilities. If you enable the detection of Web-CMS vulnerabilities, the system scans for this type of vulnerabilities once a day. If you modify the scan cycle, the historical cycle tasks that are not run are deleted. Full scan tasks are created based on the new scan cycle. If the scan cycle is changed to 18:00 to 24:00 every day at 17:00, scan tasks are run immediately based on the new scan cycle from the current day. If the scan cycle is changed to 18:00 to 24:00 every day at 19: 00, a complete scan window does not exist on the current day, and scan tasks are run based on the new scan cycle from the next day. |

| Vulnerability Scan Level | Select the vulnerability severities for detection. Valid values: High: Vulnerabilities of this severity must be fixed at the earliest opportunity. Medium: Vulnerabilities of this severity can be fixed later. Low: Vulnerabilities of this severity are less urgent, and can be fixed later. |
|---|---|
| Vulnerability Whitelist Settings | Click Create Rule to configure a vulnerability whitelist for the specified servers. Server Guard does not detect the vulnerabilities that you add to the whitelist. |

Configure policies in multi-level organization mode In multi-level organization mode, your operations take effect only on the resource sets on which you have permissions in the current organization.

| Number | Description |
|---|---|
| 1 | Find a vulnerability type and enable or disable detection for vulnerabilities of this type. You can click Details to configure vulnerability detection for the child organizations within the current organization. The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. |
| 2 | Click Manage next to a vulnerability type and specify the resource sets and servers on which vulnerabilities of this type are detected. |

| 3 | Select a period of time during which invalid vulnerabilities are retained. Valid values: 7 days, 30 days, and 90 days. If Non-unified Value is displayed, the resource sets on which you have permissions have different configurations. You can configure the resource sets to ensure that the configurations are the same. Note If you do not handle a detected vulnerability, the system determines that the alert for the vulnerability is invalid. The system deletes the vulnerability after the specified period of time ends. |
|---|---|
| 4 | Select the vulnerability severities for detection. Valid values: High: Vulnerabilities of this severity must be fixed at the earliest opportunity. Medium: Vulnerabilities of this severity can be fixed later. Low: Vulnerabilities of this severity are less urgent, and can be fixed later. If the icon is displayed, specific resource sets are selected. You can clear the items to configure the resource sets in a centralized manner. |
| 5 | Click Create Rule to configure a vulnerability whitelist for the specified servers. Server Guard does not detect the vulnerabilities that you add to the whitelist. |

#### 3.3.2 Baseline check

##### 3.3.2.1 Baseline check overview

The baseline check feature automatically checks the security configurations on servers and provides detailed check results and suggestions for baseline reinforcement.

**Overview**

After you enable the baseline check feature, Apsara Stack Security automatically checks for risks related to the operating systems, accounts, databases, passwords, and security compliance configurations of your servers, and provides reinforcement suggestions. For more information, see Baseline check items. By default, a full baseline check is automatically performed from 00:00 to 06:00 every day. You can create and manage baseline check policies. When you create or modify a policy, you can specify the baselines, interval, and time period, and select the servers to which you want to apply this policy.

**Usage notes**

By default, the following baselines are disabled. To check these baselines, make sure that these baselines do not affect your business and select them when you configure a custom policy. Baselines related to weak passwords for specific applications such as MySQL, PostgreSQL, and SQL Server

> **Note:** If these baselines are enabled, the system attempts to log on to servers with weak passwords. The logon attempts consume server resources and generate a large number of logon failure records.

Baselines related to classified protection of cybersecurity Internationally agreed best practices for security

**Baselines**

| Category | Baseline |
|---|---|
| Unauthorized access | ActiveMQ unauthorized access high exploit vulnerability risk CouchDB unauthorized access high exploit risk Docker unauthorized access high vulnerability risk Elasticsearch unauthorized access high exploit vulnerability risk Hadoop unauthorized access high exploit vulnerability risk Jboss unauthorized access high exploit vulnerability risk Jenkins unauthorized access high exploit vulnerability risk Kubernetes-Apiserver unauthorized access to high-risk risks LDAP unauthorized access high exploit vulnerability risk (Windows) OpenLDAP unauthorized access vulnerability baseline (Linux) Memcached unauthorized access high exploit vulnerability risk Mongodb unauthorized access high exploit vulnerability risk Postgresql unauthorized access to high-risk risk baseline RabbitMQ unauthorized access high exploit vulnerability risk Redis unauthorized access high exploit vulnerability risk rsync unauthorized access high exploit vulnerability risk ZooKeeper unauthorized access high exploit vulnerability risk |

|   | MLPS compliance | MLPS Level 3 Compliance Baseline for Alibaba Cloud Linux 3 MLPS Level 2 Compliance Baseline for Alibaba Cloud Linux 2 MLPS Level 3 Compliance Baseline for Alibaba Cloud Linux 2 MLPS Level 3 Compliance Baseline for Anolis 8 MLPS Level 3 Compliance Baseline for Bind MLPS Level 2 Compliance Baseline for CentOS Linux 6 MLPS Level 3 Compliance Baseline for CentOS Linux 6 MLPS Level 2 Compliance Baseline for CentOS Linux 7 MLPS Level 3 Compliance Baseline for CentOS Linux 7 MLPS Level 3 Compliance Baseline for CentOS Linux 8 MLPS Level 2 Compliance Baseline for Debian Linux 8 MLPS Level 3 Compliance Baseline for Debian Linux 8/9/10 MLPS Level 3 Compliance Baseline for IIS MLPS Level 3 Compliance Baseline for Informix MLPS Level 3 Compliance Baseline for JBoss 6/7 MLPS Level 3 Compliance Baseline for Kylin MLPS Level 3 Compliance Baseline for MongoDB MLPS Level 3 Compliance Baseline for SQL Server MLPS Level 3 Compliance Baseline for MySQL MLPS Level 3 Compliance Baseline for Nginx MLPS Level 3 Compliance Baseline for Oracle MLPS Level 3 Compliance Baseline for PostgreSQL MLPS Level 3 Compliance Baseline for Red Hat Linux 6 MLPS Level 2 Compliance Baseline for Red Hat Linux 7 MLPS Level 3 Compliance Baseline for Red Hat Linux 7 MLPS Level 3 Compliance Baseline for Redis MLPS Level 3 Compliance Baseline for SUSE 10 MLPS Level 3 Compliance Baseline for SUSE 12 MLPS Level 3 Compliance Baseline for SUSE 15 MLPS Level 3 Compliance Baseline for SUSE 11 MLPS Level 3 Compliance Baseline for Ubuntu 14 |   |
|---|---|---|---|

|   | MLPS Level 2 Compliance Baseline for Ubuntu 16/18 MLPS Level 3 Compliance Baseline for Ubuntu 16/18/20 MLPS Level 3 Compliance Baseline for UOS MLPS Level 3 Compliance Baseline for Websphere Application Server MLPS Level 3 Compliance Baseline for WebLogic MLPS Level 2 Compliance Baseline for Windows 2008 R2 MLPS Level 3 Compliance Baseline for Windows 2008 R2 MLPS Level 2 Compliance Baseline for Windows 2012 R2 MLPS Level 3 Compliance Baseline for Windows 2012 R2 MLPS Level 2 Compliance Baseline for Windows Server 2016/2019 MLPS Level 3 Compliance Baseline for Windows Server 2016/2019 |
|---|---|
|   | Alibaba Cloud Standard - Alibaba Cloud Linux 2/3 Benchmark Alibaba Cloud Standard - Anolis 7/8 Security Baseline Check Alibaba Cloud Standard - Apache Security Baseline Check Alibaba Cloud Standard - CentOS Linux 6 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check Alibaba cloud standard - CouchDB security baseline check Alibaba Cloud Standard-SQL Server Security Baseline Check (2008 or Later) Alibaba Cloud Standard - Debian Linux 8/9/10/11/12 Security Baseline |
|   | Alibaba Cloud Standard-Docker Host Security Baseline Check Alibaba Cloud Standard - ElasticSearch Security Baseline Check Alibaba Cloud Standard - Hadoop Security Baseline Check Alibaba Cloud Standard - IIS 8 Security Baseline Check Alibaba Cloud Standard - Influxdb Security Baseline Check |

| Best security practices | Alibaba Cloud Standard -Jboss6/7 Security Baseline Alibaba Cloud Standard - Kylin Security Baseline Check Alibaba Cloud Standard - Memcached Security Baseline Check Alibaba Cloud Standard - Activemq Security Baseline Alibaba Cloud Standard - Jenkins Security Baseline Check Alibaba Cloud Standard - RabbitMQ Security Baseline Alibaba Cloud Standard - MongoDB Security Baseline Check (Version 3.x ) Alibaba Cloud Standard - Mysql Security Baseline Check |
|---|---|
|   | Alibaba Cloud Standard - Nginx Security Baseline Check Alibaba Cloud Standard - Oracle Security Baseline Check Alibaba Cloud Standard-PostgreSql Security Initialization Check Alibaba Cloud Standard - Red Hat Enterprise Linux 6 Security Baseline Check Alibaba Cloud Standard - Red Hat Enterprise Linux 7/8 Security Baseline Check Alibaba Cloud Standard - Redis Security Baseline Check Alibaba Cloud Standard - Rocky Linux 8/9 Security Baseline Check Alibaba Cloud Standard - Windows SMB Security Baseline Check Alibaba Cloud Standard - SUSE Linux 15 Security Baseline Check Alibaba Cloud Standard - Apache Tomcat Security Baseline(on windows) Alibaba Cloud Standard - Ubuntu Security Baseline Alibaba Cloud Standard - Uos Security Baseline Check Alibaba Cloud Standard - Windows Server 2008 R2 Security Baseline Check Alibaba Cloud Standard - Windows 2012 R2 Security Baseline Alibaba Cloud Standard - Windows 2016/2019 Security Baseline Alibaba Cloud Standard-Apache Tomcat Security Baseline |

| Internationally agreed best practices for security | Alibaba Cloud Linux 2/3 Internationally Agreed Best Practices for Security CentOS Linux 6 LTS Internationally Agreed Best Practices for Security CentOS Linux 7 LTS Internationally Agreed Best Practices for Security CentOS Linux 8 LTS Internationally Agreed Best Practices for Security Debian Linux 8/9/10 Internationally Agreed Best Practices for Security Ubuntu 14 LTS Internationally Agreed Best Practices for Security Ubuntu 16/18/20 LTS Internationally Agreed Best Practices for Security Windows Server 2008 R2 Internationally Agreed Best Practices for Security Windows Server 2012 R2 Internationally Agreed Best Practices for Security Windows Server 2016/2019 R2 Internationally Agreed Best Practices for Security |
|---|---|

| Weak password | MongoDB Weak Password baseline(support version 2. X) Ftp login weak password baseline Jboss6/7 login weak password baseline Jenkins login weak password baseline Linux system login weak password baseline MongoDB Weak Password baseline SQL Server DB login weak password baseline Mysql database login weak password check (version 8.x is not supported) Mysql DB login weak password baseline(Windows version) Openldap login weak password baseline OpenVPN weak password detection in Linux system Oracle login weak password detection PostgreSQL DB login weak password baseline pptpd login weak password baseline Proftpd login weak password baseline RabbitMQ login weak password baseline Redis DB login weak password baseline rsync login weak password baseline svn login weak password baseline Apache Tomcat Console weak password baseline VncServer weak password check Weblogic 12c login weak password detection Windows system login weak password baseline Activemq login weak password baseline |
|---|---|

##### 3.3.2.2 Manage baseline check policies

This topic describes how to create, modify, and delete baseline check policies and how to specify baseline check levels.

**Background information**

By default, the baseline check feature uses **default baseline check policies** to check the baseline risks of assets. You can also create custom baseline check policies based on your business requirements. For example, you can create a custom baseline check policy to check the compliance based on Multi-Level Protection Scheme (MLPS) level 2 in China.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Baseline Check**.
4. In the upper-right corner of the Baseline Check page, click **Manage Policy**. In the **Manage**
**Policy** panel, manage baseline check policies.

> **Important:** In multi-level organization mode, your operations take effect only on the resource sets on which you have permissions in the current organization.
> In multi-level organization mode, the resource sets on which you have permissions have different configurations if **Nonunified Value** is displayed. You can configure the resource sets to ensure that the configurations are the same.

Create a standard baseline check policy: Click **Create Standard Policy**. In the panel that appears, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Enter a policy name. |
| Check Cycle | Specify an interval for the baseline check task. Valid values: 1 day, Every 3 Day, Every 7 Day, and Every 30 Day. |
| Detection time | Select a time range for the baseline check task. Valid values: 00:00 to 6:00, 06:00 to 12:00, 12:00 to 18:00, and 18:00 to 24:00. |
| Check Items | Select the baselines that you want to check. The default policy includes the following types of baselines: unauthorized access, MLPS compliance, best security practices, internationally agreed best practices for security, and weak password. |

| Servers | Select the server groups to which you want to apply the baseline check policy. In multi-level organization mode, you must select the resource set on which you have permissions in the current organization. Note By default, newly purchased servers are classified into the Default > Asset Group. To apply the policy to new servers, select Default. |
|---|---|

Create a custom baseline check policy: Click **Create Custom Policy**. In the panel that appears, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Enter a policy name. |
| Check Cycle | Specify an interval for the baseline check task. Valid values: 1 day, Every 3 Day, Every 7 Day, and Every 30 Day. |
| Detection time | Select a time range for the baseline check task. Valid values: 00:00 to 6:00, 06:00 to 12:00, 12:00 to 18:00, and 18:00 to 24:00. |
| Check Items | Select the baselines that you want to check. |
| Servers | Select the server groups to which you want to apply the baseline check policy. In multi-level organization mode, you must select one or more resource sets on which you have permissions in the current organization. Note By default, newly purchased servers are classified into the Default > Asset Group. To apply the policy to new servers, select Default. |

Modify a baseline check policy. In the policy list, find the policy that you want to modify and click **Edit** in the **Actions** column.

> **Note:** You cannot modify the baselines of the default policy. You can only modify the server groups to which the default policy is applied.

Modify multiple policies at a time (supported only in multi-level organization mode): If you create multiple policies that have the same name and the same type under different resource sets, click **Centrally Edit** below the policy list to modify the policies at a time.

> **Note:** If the resource sets have different configurations after you modify the policies as an administrator, the system displays a message instructing you to change the configurations to ensure that all resource sets have the same configurations.

Delete a baseline check policy: In the policy list, find the policy that you want to delete and click **Delete** in the **Actions** column.

> **Important:** You cannot restore a policy after you delete the policy. You cannot delete the default policy.

Specify the baseline check levels: In the **Baseline Check Level** section, specify the baseline check levels. Valid values: High, Medium, and Low. In multi-level organization mode, the icon for a level indicates that the level is specified in specific resource sets. You can clear the selected items to configure baseline check levels in a centralized manner.

> Create custom weak password rules: Server Guard provides default weak password rules based on the Alibaba Cloud threat intelligence. You can also use a template to upload custom weak password rules. Make sure that the size of the file that you upload does not exceed 5 KB.

In the **Custom Weak Password Rules** section, click **Import File** to upload an onpremises file of weak password rules.

> To export the uploaded file, right-click the name of the file to save the file or click the name of the file to save the file on the preview page.

##### 3.3.2.3 View baseline check results and handle baseline risks

**baseline risks**

Apsara Stack Security Center provides details of baseline check results and suggestions on how to manage failed check items. This topic describes how to view baseline check results and manage failed check items in Apsara Stack Security Center. The check results include affected assets, checked items, and suggestions.

**View the summary of baseline check results**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Baseline Check**.
4. In the upper part of the **Baseline Check** page, view the summary of baseline check
results. You can filter data by baseline check policy. You can select a baseline check policy from the **Select Policy** drop-down list to view the following information:
**Checked Servers**: The number of servers on which the baseline check runs. These
servers are specified in the selected baseline check policy.
**Check Items**: The number of **check items** specified in the selected baseline check
policy.
**Last Pass Rate**: The pass rate of the last baseline check.
If the number below **Last Pass Rate** is green, the pass rate of the checked servers is high. If the number is red, a large number of failed check items were detected on the checked servers. We recommend that you view the details of the check result and manage the failed check items.
5. Select **All** from the **Select Policy** drop-down list.
The **Baseline Check** page displays the details of all baselines, such as **Baseline**, **Checked**
**Items**, **Failed Items/Affected Servers**, **Category**, and **Last Checked At**.

> **Note:** You can also select a baseline check policy from the **Select Policy** drop-down list to view the baselines that are specified in the policy.

**View the details of a baseline**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Baseline Check**.
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
|---|---|

**View the exposure details of assets**

**Exposed assets**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Risk Exposure Detection**.
4. On the **Asset Exposure** tab of the **Risk Exposure Detection** page, view the information
about exposed assets. Filter assets: Filter assets by vulnerability, asset group, or port. View the exposure details of an asset: Find the asset whose details you want to view and click **Exposure Details** in the **Actions** column. In the panel that appears, you can view the communication link topology between the asset and the Internet, and the details of the links. Export data of exposed assets: Click the icon in the upper-right corner of the exposed asset list to export and save the details of the exposed assets to your computer. The exported file is an Excel file.

**Exposed applications**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Risk Exposure Detection**.
4. On the **Application exposure** tab of the **Risk Exposure Detection** page, view the
information about exposed applications. Filter applications: Filter applications by specifying whether vulnerabilities exist or entering the service version or middleware version, or the service name or middleware name. View the exposure details of an application: Find the application whose details you want to view and click **Exposure Details** in the **Actions** column. In the panel that appears, you can view the exposure details of the application. Export data of an exposed application: Click the icon in the upper-right corner of the list of exposed applications to export and save the details of the exposed applications to your computer. The exported file is an Excel file.

#### 3.3.4 Application protection

The application protection feature is developed based on the runtime application selfprotection (RASP) technology. This feature can detect attacks and provide protection during application runtime. To use the application protection feature, you do not need to change the application code. You need to only install the application protection agent on the servers that you want to protect. The feature can protect your applications against attacks that are launched by exploiting most unknown vulnerabilities.

**Step 1: Add applications for protection**

Before you can use the application protection feature, you must add an application and then enable the application protection feature for the server or container in which the application is deployed.

**Add an application**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Application Protection**.
4. On the **Configuration** tab of the **Application Protection** page, click **Create**
**Application**. In the New application dialog box, enter the name and description of the
application that you want to add, and click **OK**. After you add an application, the default policy takes effect on the application. The default protection mode is Monitor. You can click **Protection strategy** in the **Operation** column to view information about the default policy.
5. In the **Prompt** message, click **Cancel**.
You can also click **OK** to add the application. For more information, see Enable the application security feature for a server and Enable the application security feature for a container.
6. **Optional**. If you do not want to use the default policy, perform the following steps to modify
the protection policy: i. In the application list of the **Configuration** tab, find the application whose protection policy you want to modify and click **Protection strategy** in the **Operation** column. ii. In the **Protection strategy** panel, modify the policy and click **OK**.

| Parameter | Description |
|---|---|
| Protection Mode | The protection mode for the application. Valid values: Monitor: monitors your application to detect attacks. The running of the application is not affected. If an attack is detected, an alert is generated. For this alert, Processing method is Monitor. Block: monitors and blocks attacks, and monitors high-risk operations that are performed on the application. If an attack is blocked, an alert is generated. For this alert, Processing method is Block. Disable: disables the application protection feature for the application. Attacks are not monitored or blocked. |
| Detection timeout | The maximum timeout period for attack detection. Valid values: 1 to 60000. Unit: milliseconds. Default value: 300. After the specified period elapses, the original business logic continues regardless of whether the detection logic is incomplete. We recommend that you use the default value. |
| SOURCE IP judgment method | The method that is used to obtain source IP addresses. If you select Default, the system obtains source IP addresses based on the values of standard request headers that record source IP addresses. Standard request headers that record source IP addresses include X-Real-IP, True-Client-IP, and X-Forwarded-For. If you select Taken from the value that defines the header, the system preferentially obtains source IP addresses based on the values of custom headers. If the system cannot obtain source IP addresses based on the values of custom headers, the value Default takes effect. |
| Detection type | The types of attacks that you want to detect. We recommend that you retain the default settings. To retain the default settings, click Select All. For more information about the different types of attacks, see Attack types. |

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
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Application Protection**.
4. On the **Alert** tab of the **Application Protection** page, view the information about alert
events. On the **Alert** tab, the doughnut charts display the behavior of applications after the application protection feature is enabled for the applications and the statistics about attacks on the applications. The list in the lower part of the page displays the details of each attack. The details include the type, URL, behavior data, and handling method of an attack. View statistics about application behavior The **Application Behavior Statistics** section displays the application behavior that is monitored by the application protection feature and the behavior types. The behavior types include normal behavior and attacks. View attack statistics The **Attack Statistics** section displays the attacks that are detected by the application protection feature and the types of attacks. View attack details The list in the lower part of the Application protection page displays the details of each attack. You can view the time, type, URL, behavior data, and handling method of each attack in the list. You can also view the details of an attack. To view the details of an attack, find the attack and click **View** in the **Operation** column. In the **Details** panel, view the details, including vulnerability details, request details, and server details.

**Configure a whitelist rule**

You can configure a whitelist rule to allow requests from specific IP addresses. If requests match a whitelist rule that you specify, Server Guard does not block or generate alerts on the requests.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Prevention** > **Application Protection**.
4. On the **Whitelist** tab of the **Application Protection** page, click **Configure a whitelist**.
In the **Configure a whitelist** panel, perform the following steps to configure a whitelist rule and select applications to which you want the rule to take effect. i. In the **Rule Name** field, enter a name for the rule. ii. In the **Resource Set** drop-down list, select a resource set. In multi-level organization mode, all resource sets that belong to the current organization are displayed. iii. In the **Source IP Address** section, enter the source IP addresses that you want to add to the whitelist. You can enter up to 100 IP addresses or CIDR blocks.

> **Important:** If you enter 0.0.0.0/0, Server Guard allows requests from all IP addresses. Proceed with caution.

iv. In the **Request Path** section, configure the path that is used to match requests from the IP addresses in the whitelist. You can select one of the following match methods for the path:
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

v. In the **Detection type** section, select the detection type and click **Next**. vi. Select the applications for which you want the whitelist rule to take effect and click **OK**. After the configuration is complete, the whitelist rule takes effect on all online application instances of the selected applications.

**Attack types**

The following table describes the types of attacks that the application protection feature can detect and the solutions to defend against each type of attack.

| Attack Type | Description | Protection suggestion |
|---|---|---|
| JNI injection | Java Native Interface (JNI) injection is a common method to bypass the RASP technology. After an attacker obtains the permissions to execute code, the attacker can use JNI functions to call external malicious dynamic-link libraries. This way, the attacker can bypass the security protection at the Java layer and conceal specific malicious behavior. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |

| SQL injection | An SQL injection attack inserts SQL statements into the query strings of web requests or web forms and induces the server to execute the SQL statements. An attacker can obtain the data on websites on which security vulnerabilities exist by inserting SQL statements into web forms. | SQL injection is caused by concatenating SQL statements. Precompile input parameters or use whitelists and blacklists to limit concatenated parameters. |
|---|---|---|
| XXE | XXE injection is short for XML external entity injection. If an XML file references an external entity, an attacker can construct malicious content to cause arbitrary file reads, command execution, and internal network attacks. | Check whether your application needs to load external entities when it parses XML files. If not, disable external entities in the XML parsing configurations. |
| Malicious DNS query | An attacker can use multiple methods to exploit malicious Domain Name System (DNS) queries. An attacker is likely to use the DNS protocol to bring sensitive information out of internal networks. The attacker may also use the DNS protocol to check whether an internal network system has vulnerabilities such as Server-Side Request Forgery (SSRF) and Java Naming and Directory Interface (JNDI) injection. | Malicious DNS queries are caused by server requests for user-controlled parameters. Check parameter settings and configure whitelists. |
| Malicious reflection call | The self-protection module of RASP prohibits attackers from using reflection to modify RASP data during runtime. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| SSRF | SSRF is a web vulnerability that allows an attacker to attack the internal system of a website by inducing a server-side application to initiate HTTP requests. | SSRF is caused by server requests for input parameters. Check parameter settings and configure whitelists. |

| Malicious file read and write | Java provides the RandomAccessFile class for file read and write operations. If you use this class to read and write files but do not restrict the file path or file content, an attacker may read sensitive system files or upload trojan files. | Check whether you can read and upload files as expected. If an exception occurs, check the function code and configure blacklists. |
|---|---|---|
| Malicious file upload | For the file upload feature provided by a website, if the types of files are not restricted, an attacker may obtain higher permissions on the server by uploading trojan files. This causes serious harm. | Restrict the types of files that can be uploaded and prohibit uploading files with execute permissions, such as Jakarta Server Pages (JSP) files. |
| Command injection | A command execution vulnerability allows an attacker to execute arbitrary system commands on a server. | In most cases, remote command execution is caused by webshells or the risky code of a server. Check the location in which commands are executed. If command execution is caused by webshells, delete the webshells in time. If commands are executed to implement normal features on a server, configure whitelists to limit the commands that can be executed. |
| Directory traversal | The directories of a website may be browsed arbitrarily due to the configuration defects of the website. This results in the disclosure of privacy information. An attacker can use the disclosed information to attack the website. | Check whether directory traversal operations are normal. If an exception occurs, check the function code and configure blacklists to restrict related commands, such as "./" and "../". |
| In-memory webshell injection | In-memory webshells are an emerging trojan horse technique. An attacker can inject trojans into memory by using technical approaches that help effectively bypass the detection of Web Application Firewall (WAF) and host defense. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| Arbitrary file read | For the file download and read feature provided by a website, if files are read and downloaded by using an absolute path or a directory traversal character and file paths are not restricted, an attacker can exploit this vulnerability to obtain sensitive information and attack the server. | Check whether you can read files as expected. If an exception occurs, check the function code and configure blacklists to restrict input parameters, such as "./" and "../". |

| Weak database password | If a database password is weak, an attacker can initiate brute-force attacks to obtain the password. Then, the attacker can steal data from the database and obtain system permissions. | Use a more complex password. |
|---|---|---|
| Thread injection | Thread injection is a common method to bypass the RASP technology. If an attacker obtains the permissions to execute code, the attacker can create a thread to cause RASP to lose the context of the runtime environment. In this case, the defense capability of RASP is compromised. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| Malicious Attach API | The Attach API is a Java technology that can be used to dynamically modify the bytecode of running applications. An attacker can use the technology to inject agent-type in- memory webshells. This method is highly deceptive. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| JNDI injection | If an application initiates a JNDI query but the query URL is controlled by an attacker, the attacker can induce the server on which the application runs to query malicious links and load malicious classes. This results in arbitrary code execution on the server. | If this vulnerability is caused by third-party components, you must upgrade the components at the earliest opportunity. If this vulnerability is caused by self- written code for JNDI queries, you must restrict the query URLs to prohibit queries over vulnerable protocols. |
| Usage of insecure protocols | If the URL that a server accesses is user-controllable and the URL protocol is not restricted on your application, an attacker can read sensitive files on the server over vulnerable protocols such as File and NetDoc. | Restrict URL protocols. |
| Deserialization attack | Java deserialization is a process of restoring a sequence of bytes into a Java object. If the Java object contains code that can cause high risks, an attacker can control the member variables of the Java object to initiate attacks during the deserialization process. | Upgrade the components on which vulnerabilities are detected at the earliest opportunity. If no official versions of the components that have vulnerabilities fixed are released, temporarily disable the deserialization. |

| Arbitrary file deletion | For the file deletion feature provided by a website, if files are read and downloaded by using an absolute path or a directory traversal character and file paths are not restricted, an attacker can exploit this vulnerability to obtain sensitive information and attack the server. | Check whether you can delete files as expected. If an exception occurs, check the function code and configure blacklists to restrict input parameters, such as "./" and "../". |
|---|---|---|
| Expression injection | Expressions provide a wide range of features, such as data query and processing during runtime. Multiple expressions also provide features that require advanced permissions such as function calls. If the features are not restricted, attackers can modify the content of expressions and execute arbitrary code. | Strictly restrict the content of expressions and disable Java function calls. If this vulnerability is caused by third-party components, you must upgrade the components at the earliest opportunity. |
| Engine injection | Java provides various third-party JavaScript engines such as Rhino and Nashorn, and template engines such as Apache Velocity and FreeMarker. In most cases, the engines provide features that require advanced permissions such as function calls. If the features are not restricted, attackers can modify the content that is executed by the engines and execute arbitrary code. | Strictly restrict the content imported to the engines and disable Java function calls. If this vulnerability is caused by third-party components, you must upgrade the components at the earliest opportunity. |
| Malicious beans binding | Some Java frameworks support bean property binding when applications are running. If the types of bean properties that can be bound are not restricted, attackers can modify the values of sensitive bean properties to disrupt the running of applications or even execute arbitrary code. | Restrict the types of bean properties that can be bound to prevent the values of bean properties such as class and class loaders from being changed. If this vulnerability is caused by third- party components, you must upgrade the components at the earliest opportunity. |
| Malicious class loading | Zero-day vulnerabilities and web shells depend on the loading of malicious classes. If malicious classes are loaded, attackers can initialize malicious classes, obtain the permissions to execute code, and perform malicious operations. | If malicious classes are loaded by using web shells, delete the web shells at the earliest opportunity. If malicious classes are loaded due to framework vulnerabilities, upgrade the frameworks at the earliest opportunity. |

| JSTL file inclusion | The JavaServer Pages Standard Tag Library (JSTL) is a set of JavaServer Pages (JSP) tags, which encapsulates the common core features of JSP applications. If a user-controllable parameter is directly concatenated in JSTL without any restrictions on the parameter, attackers can construct a special script that causes arbitrary file reads and SSRF attacks. | We recommend that you do not directly concatenate user-controllable parameters in JSTL. If you need to do this, you must exercise strict whitelist control on the content of the parameters. |
|---|---|---|

### 3.4 Intrusion prevention

#### 3.4.1 Use the antivirus feature

Server Guard provides the antivirus feature. This feature allows you to customize settings for virus and webshell detection.

**Virus detection and removal**

**Configure virus detection**

The antivirus feature can automatically quarantine common network viruses, such as common trojans, ransomware, mining programs, and DDoS trojans. Apsara Stack Security experts check and verify all the automatically quarantined viruses to ensure a minimum false positive rate. If the automatic virus blocking feature is disabled, Server Guard generates alerts when viruses are detected. You must manually manage detected viruses in the Server Guard console. We recommend that you enable the virus blocking feature to improve the security of your servers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Virus Defense**.
4. In the upper-right corner of the **Anti-virus** tab, click **Scan Settings**.
5. In the **Scan Settings** panel, configure the **Scan Cycle**, **Scan mode**, and **Scan Scope**
parameters, and click **OK**. In multi-level organization mode, you can search for the assets that you want to scan by resource set.

**Scan for viruses**

1. On the **Anti-virus** tab, click **Scan** or **Rescan**.
2. In the panel that appears, configure the **Scan mode** and **Scan Scope** parameters and
click **OK**.

| Paramete r | Description |
|---|---|
| Scan mode | Select a scan mode. Valid values: Quick Scan: In this mode, Server Guard automatically scans items such as active processes, startup items, and sensitive directories and files for risks. Custom Directory Scan: In this mode, you can specify the file directories that you want to scan. Enter the file directory that you want to scan. Separate multiple directories with line feeds. A single scan supports up to 30,000 files. If more than 30,000 files are included in the specified directories, the excess files are not scanned. |
| Scan Scope | Select the assets that you want to scan. You can select assets based on the following types: All Assets: If you select this option, all assets are scanned. By asset: If you select this option, you can select servers based on your business requirements. By group: If you select this option, you can select asset groups. Then, Server Guard scans all assets in the asset groups. If new assets are added to the asset groups, the assets are automatically scanned by Server Guard. |

**Handle alerts**

> **Important:** Virus removal may cause service interruptions. Before you perform deep cleanup, we recommend that you manually back up snapshots of your system to prevent unnecessary losses.

1. On the **Anti-virus** tab, click **Process**.
2. Click **Process**, select the required servers, and then click **Batch handled**. Alternatively,
find a server and click **Handle** in the **Actions** column.
3. In the **Alert Process** dialog box, select one of the following handling methods, select **I Am**
**Aware of Risks of Virus Removal**, and then click **Process Now**.
**Deep cleanup**: After the Server Guard experts conduct tests and analysis on persistent
viruses, the experts develop the Deep cleanup method based on the test and analysis results to detect and remove the viruses.
**Whitelist**: If you select this method, Server Guard no longer generates alerts for the
detected viruses. Proceed with caution.
**Ignore**: If you select this method, the status of the alert changes to Ignored. Server
Guard still generates this alert in subsequent detection.
**Handled manually**: This alert reports a suspicious exception. We recommend that you
troubleshoot the exception based on the handling suggestions. After you troubleshoot the exception, click Process Now. The alert status changes to Handled.

#### 3.4.2 Web tamper proofing

The web tamper proofing feature can monitor website directories and files on your server in real time. The feature can also restore tampered files or directories by using backups if a website is tampered with. This prevents the website from being inserted with illegal information and ensures that the website runs as expected. This topic describes how to use the web tamper proofing feature.

**Prerequisites**

The Server Guard agent is installed on the server for which you want to enable the web tamper proofing feature. For more information, see Install the Server Guard agent.

**Background information**

To make illegal profits or launch business attacks, attackers exploit vulnerabilities in websites to tamper with the websites. For example, attackers insert hidden links to the websites. Tampering with web pages affects normal user access and may cause serious economic loss, damage to brand reputation, and political risks. The Server Guard agent automatically collects information about the processes related to the files in the protected directories of protected servers. The agent identifies suspicious processes and abnormal file changes in real time and generates alerts for or intercepts the processes that cause abnormal file changes.

**Limits**

A quota of 1 on web tamper proofing can be consumed to protect one server. You can enable the web tamper proofing feature for a server only once. You can add up to 10 directories on each server for protection. If the operating system and kernel version of your server are **supported by the whitelist**
**feature**, take note of the following items. For more information, see **Supported versions**
**of operating systems and kernels**.
Use the whitelist feature: If Server Guard generates an alert for or blocks a process that causes abnormal file changes but the process is required by your workloads, you can add the process to the process whitelist. Then, Server Guard no longer blocks or generates alerts for the process. When you add directories for protection, take note of the following items: The maximum length of the full path to each specified file or directory is 1,000 characters. If you add a process path of a Network File System (NFS) server for protection, Server Guard cannot protect the files in the path from NFS client-based attacks that attempt to modify the files. If the operating system and kernel version of your server are **not supported by the**
**whitelist feature**, take note of the following items. For more information, see **Supported**
**versions of operating systems and kernels**.
The whitelist feature is not supported. The web tamper proofing feature still blocks a process even if you add the process to the process whitelist. When you add directories for protection, take note of the following items: The maximum size of each specified directory is 20 GB. The maximum number of folders in each specified directory is 20,000. The maximum number of folder levels in each specified directory is 20. The maximum size of each specified file is 20 GB. You cannot set Prevention Mode to Alert Mode. The paths to the NFS cannot be protected. Alerts may not be generated. Details of alerts do not include information about process paths. Table 1. Supported versions of operating systems and kernels

| Supported operating system | Supported operating system version | Supported kernel version |
|---|---|---|
| Windows (32-bit or 64-bit) | Windows Server 2008, Windows Server 2012, Windows Server 2016, and Windows Server 2019. | All versions |
|   |   | 2.6.32 series 2.6.32-754.35.1.el6.x86 64 _ 2.6.32-754.33.1.el6.x86 64 _ 2.6.32-754.31.1.el6.x86 64 _ 2.6.32-754.30.2.el6.x86 64 _ 2.6.32-754.29.2.el6.x86 64 _ 2.6.32-754.29.1.el6.x86 64 _ 2.6.32-754.28.1.el6.x86 64 _ 2.6.32-754.27.1.el6.x86 64 _ 2.6.32-754.25.1.el6.x86 64 _ 2.6.32-754.24.3.el6.x86 64 _ 2.6.32-754.23.1.el6.x86 64 _ 2.6.32-754.22.1.el6.x86 64 _ 2.6.32-754.18.2.el6.x86 64 _ 2.6.32-754.17.1.el6.x86 64 _ 2.6.32-754.15.3.el6.x86 64 _ 2.6.32-754.14.2.el6.x86 64 _ 2.6.32-754.12.1.el6.x86 64 _ 2.6.32-754.11.1.el6.x86 64 _ 2.6.32-754.10.1.el6.x86 64 _ 2.6.32-754.9.1.el6.x86 64 _ 2.6.32-754.6.3.el6.x86 64 _ |

|   |   | 2.6.32-754.3.5.el6.x86 64 _ 2.6.32-754.2.1.el6.x86 64 _ 2.6.32-754.el6.x86 64 _ 2.6.32-696.30.1.el6.x86 64 _ 2.6.32-696.28.1.el6.x86 64 _ 2.6.32-696.23.1.el6.x86 64 _ 2.6.32-696.20.1.el6.x86 64 _ 2.6.32-696.18.7.el6.x86 64 _ 2.6.32-696.16.1.el6.x86 64 _ 2.6.32-696.13.2.el6.x86 64 _ 2.6.32-696.10.2.el6.x86 64 _ 2.6.32-696.10.1.el6.x86 64 _ 2.6.32-696.6.3.el6.x86 64 _ |
|---|---|---|
|   |   | 2.6.32-696.3.2.el6.x86 64 _ 2.6.32-696.3.1.el6.x86 64 _ 2.6.32-696.1.1.el6.x86 64 _ 2.6.32-696.el6.x86 64 _ 2.6.32-642.15.1.el6.x86 64 _ 2.6.32-642.13.1.el6.x86 64 _ 2.6.32-642.11.1.el6.x86 64 _ 2.6.32-642.13.1.el6.centos.plus.x86 64 _ 2.6.32-642.11.1.el6.centos.plus.x86 64 _ 2.6.32-642.6.2.el6.centos.plus.x86 64 _ 2.6.32-642.6.2.el6.x86 64 _ 2.6.32-642.6.1.el6.x86 64 _ 2.6.32-642.4.2.el6.x86 64 _ 2.6.32-642.3.1.el6.x86 64 _ 2.6.32-642.1.1.el6.x86 64 _ 2.6.32-642.el6.x86 64 _ 2.6.32-573.22.1.el6.x86 64 _ 2.6.32-573.18.1.el6.x86 64 _ 2.6.32-573.12.1.el6.x86 64 _ 2.6.32-573.26.1.el6.x86 64 _ 2.6.32-573.3.1.el6.x86 64 _ 2.6.32-573.7.1.el6.x86 64 _ 2.6.32-573.8.1.el6.x86 64 _ 2.6.32-573.el6.x86 64 _ 2.6.32-504.30.3.el6.x86 64 _ 2.6.32-504.23.4.el6.x86 64 _ 2.6.32-504.16.2.el6.x86 64 _ 2.6.32-504.12.2.el6.x86 64 _ 2.6.32-504.8.1.el6.x86 64 _ |

|   |   | 2.6.32-504.3.3.el6.x86 64 _ 2.6.32-504.1.3.el6.x86 64 _ 2.6.32-504.el6.x86 64 _ 2.6.32-431.29.2.el6.x86 64 _ 2.6.32-431.23.3.el6.x86 64 _ 2.6.32-431.20.3.el6.x86 64 _ 2.6.32-431.17.1.el6.x86 64 _ 2.6.32-431.el6.x86 64 _ 2.6.32-358.18.1.el6.x86 64 _ 2.6.32-358.6.2.el6.x86 64 _ 2.6.32-358.el6.x86 64 _ 2.6.32-279.el6.x86 64 _ 2.6.32-220.13.1.el6.x86 64 _ 2.6.32-220.el6.x86 64 _ 3.10.x series 3.10.107-1.el6.elrepo.x86 64 _ 3.10.0-1160.108.1.el7.x86 64 _ 3.10.0-1160.105.1.el7.x86 64 _ 3.10.0-1160.102.1.el7.x86 64 _ 3.10.0-1160.99.1.el7.x86 64 _ 3.10.0-1160.95.1.el7.x86 64 _ 3.10.0-1160.92.1.el7.x86 64 _ 3.10.0-1160.90.1.el7.x86 64 _ 3.10.0-1160.88.1.el7.x86 64 _ 3.10.0-1160.83.1.el7.x86 64 _ 3.10.0-1160.81.1.el7.x86 64 _ 3.10.0-1160.80.1.el7.x86 64 _ 3.10.0-1160.76.1.el7.x86 64 _ 3.10.0-1160.71.1.el7.x86 64 _ 3.10.0-1160.66.1.el7.x86 64 _ 3.10.0-1160.62.1.el7.x86 64 _ 3.10.0-1160.59.1.el7.x86 64 _ 3.10.0-1160.53.1.el7.x86 64 _ 3.10.0-1160.49.1.el7.x86 64 _ 3.10.0-1160.45.1.el7.x86 64 _ 3.10.0-1160.42.2.el7.x86 64 _ 3.10.0-1160.41.1.el7.x86 64 _ 3.10.0-1160.36.2.el7.x86 64 _ 3.10.0-1160.31.1.el7.x86 64 _ 3.10.0-1160.25.1.el7.x86 64 _ 3.10.0-1160.24.1.el7.x86 64 _ 3.10.0-1160.21.1.el7.x86 64 _ |
|---|---|---|

|   |   | 3.10.0-1160.15.2.el7.x86 64 _ 3.10.0-1160.11.1.el7.x86 64 _ 3.10.0-1160.6.1.el7.x86 64 _ 3.10.0-1160.2.2.el7.x86 64 _ 3.10.0-1160.2.1.el7.x86 64 _ 3.10.0-1160.el7.x86 64 _ 3.10.0-1127.19.1.el7.x86 64 _ 3.10.0-1127.18.2.el7.x86 64 _ 3.10.0-1127.13.1.el7.x86 64 _ 3.10.0-1127.10.1.el7.x86 64 _ 3.10.0-1127.8.2.el7.x86 64 _ 3.10.0-1127.el7.x86 64 _ 3.10.0-1062.18.1.el7.x86 64 _ 3.10.0-1062.12.1.el7.x86 64 _ 3.10.0-1062.9.1.el7.x86 64 _ 3.10.0-1062.7.1.el7.x86 64 _ 3.10.0-1062.4.3.el7.x86 64 _ 3.10.0-1062.4.2.el7.x86 64 _ 3.10.0-1062.4.1.el7.x86 64 _ 3.10.0-1062.1.2.el7.x86 64 _ 3.10.0-1062.1.1.el7.x86 64 _ 3.10.0-1062.el7.x86 64 _ 3.10.0-957.27.2.el7.x86 64 _ 3.10.0-957.21.3.el7.x86 64 _ 3.10.0-957.12.2.el7.x86 64 _ 3.10.0-957.12.2.el7.x86 64 _ 3.10.0-957.12.1.el7.x86 64 _ 3.10.0-957.10.1.el7.x86 64 _ 3.10.0-957.5.1.el7.x86 64 _ 3.10.0-957.1.3.el7.x86 64 _ 3.10.0-957.el7.x86 64 _ 3.10.0-862.14.4.el7.x86 64 _ 3.10.0-862.11.6.el7.x86 64 _ 3.10.0-862.9.1.el7.x86 64 _ 3.10.0-862.6.3.el7.x86 64 _ 3.10.0-862.3.3.el7.x86 64 _ 3.10.0-862.3.2.el7.x86 64 _ 3.10.0-862.2.3.el7.x86 64 _ 3.10.0-862.el7.x86 64 _ 3.10.0-693.21.1.el7.x86 64 _ 3.10.0-693.17.1.el7.x86 64 _ 3.10.0-693.11.6.el7.x86 64 _ |
|---|---|---|

|   |   | 3.10.0-693.11.1.el7.x86 64 _ 3.10.0-693.5.2.el7.x86 64 _ 3.10.0-693.2.2.el7.x86 64 _ 3.10.0-693.el7.x86 64 _ 3.10.0-514.26.2.el7.x86 64 _ 3.10.0-514.26.1.el7.x86 64 _ 3.10.0-514.21.2.el7.x86 64 _ 3.10.0-514.21.1.el7.x86 64 _ 3.10.0-514.16.1.el7.x86 64 _ 3.10.0-514.10.2.el7.x86 64 _ 3.10.0-514.6.2.el7.x86 64 _ 3.10.0-514.6.1.el7.x86 64 _ 3.10.0-514.2.2.el7.x86 64 _ 3.10.0-514.el7.x86 64 _ 3.10.0-327.36.3.el7.x86 64 _ 3.10.0-327.36.2.el7.x86 64 _ 3.10.0-327.36.1.el7.x86 64 _ 3.10.0-327.28.3.el7.x86 64 _ 3.10.0-327.28.2.el7.x86 64 _ 3.10.0-327.22.2.el7.x86 64 _ 3.10.0-327.18.2.el7.x86 64 _ 3.10.0-327.13.1.el7.x86 64 _ 3.10.0-327.10.1.el7.x86 64 _ 3.10.0-327.el7.x86 64 _ 3.10.0-229.el7.x86 64 _ 3.10.0-123.9.3.el7.x86 64 _ 4.4.x series 4.4.248-1.el7.elrepo.x86 64 _ 4.4.240-1.el7.elrepo.x86 64 _ 4.4.231-1.el7.elrepo.x86 64 _ 4.4.228-2.el7.elrepo.x86 64 _ 4.4.225-1.el7.elrepo.x86 64 _ 4.4.223-1.el7.elrepo.x86 64 _ 4.4.219-1.el7.elrepo.x86 64 _ 4.4.217-1.el7.elrepo.x86 64 _ 4.4.216-1.el7.elrepo.x86 64 _ 4.4.202-1.el7.elrepo.x86 64 _ 4.4.196-1.el7.elrepo.x86 64 _ 4.4.175-1.el7.elrepo.x86 64 _ 4.4.169-1.el7.elrepo.x86 64 _ 4.4.71-1.el7.elrepo.x86 64 _ 4.9.x - 4.14.x series |
|---|---|---|

| CentOS (64-bit) | Unlimited. However, only limited kernel versions are supported. | 4.14.1-1.el7.elrepo.x86 64 _ 4.13.3-1.el7.elrepo.x86 64 _ 4.13.2-1.el7.elrepo.x86 64 _ 4.11.8-1.el7.elrepo.x86 64 _ 4.9.220-37.el7.x86 64 _ 4.9.215-36.el7.x86 64 _ 4.18.x series 4.18.10-1.el7.elrepo.x86 64 _ 4.18.8-1.el7.elrepo.x86 64 _ 4.18.0-529.el8.x86 64 _ 4.18.0-521.el8.x86 64 _ 4.18.0-513.11.1.el8 9.x86 64 _ _ 4.18.0-513.9.1.el8 9.x86 64 _ _ 4.18.0-513.el8.x86 64 _ 4.18.0-512.el8.x86 64 _ 4.18.0-500.el8.x86 64 _ 4.18.0-497.el8.x86 64 _ 4.18.0-496.el8.x86 64 _ 4.18.0-490.el8.x86 64 _ 4.18.0-485.el8.x86 64 _ 4.18.0-477.27.2.el8 8.x86 64 _ _ 4.18.0-477.27.1.el8 8.x86 64 _ _ 4.18.0-477.21.1.el8 8.x86 64 _ _ 4.18.0-477.15.1.el8 8.x86 64 _ _ 4.18.0-477.13.1.el8 8.x86 64 _ _ 4.18.0-477.10.1.el8 8.x86 64 _ _ 4.18.0-448.el8.x86 64 _ 4.18.0-425.19.2.el8 7.x86 64 _ _ 4.18.0-425.13.1.el8 7.x86 64 _ _ 4.18.0-425.10.1.el8 7.x86 64 _ _ 4.18.0-425.3.1.el8.x86 64 _ 4.18.0-408.el8.x86 64 _ 4.18.0-394.el8.x86 64 _ 4.18.0-383.el8.x86 64 _ 4.18.0-373.el8.x86 64 _ 4.18.0-372.32.1.el8 6.x86 64 _ _ 4.18.0-372.26.1.el8 6.x86 64 _ _ 4.18.0-372.16.1.el8 6.0.1.x86 64 _ _ 4.18.0-372.19.1.el8 6.x86 64 _ _ 4.18.0-372.9.1.el8.x86 64 _ 4.18.0-365.el8.x86 64 _ 4.18.0-358.el8.x86 64 _ |
|---|---|---|

|   |   | 4.18.0-348.20.1.el8 5.x86 64 _ _ 4.18.0-348.12.2.el8 5.x86 64 _ _ 4.18.0-348.7.1.el8 5.x86 64 _ _ 4.18.0-348.2.1.el8 5.x86 64 _ _ 4.18.0-348.el8.x86 64 _ 4.18.0-305.25.1.el8 4.x86 64 _ _ 4.18.0-305.19.1.el8 4.x86 64 _ _ 4.18.0-305.17.1.el8 4.x86 64 _ _ 4.18.0-305.12.1.el8 4.x86 64 _ _ 4.18.0-305.10.2.el8 4.x86 64 _ _ 4.18.0-305.7.1.el8 4.x86 64 _ _ 4.18.0-305.3.1.el8.x86 64 _ 4.18.0-240.22.1.el8 3.x86 64 _ _ 4.18.0-240.15.1.el8 3.x86 64 _ _ 4.18.0-240.10.1.el8 3.x86 64 _ _ 4.18.0-240.1.1.el8 3.x86 64 _ _ 4.18.0-193.28.1.el8 2.x86 64 _ _ 4.18.0-193.19.1.el8 2.x86 64 _ _ 4.18.0-193.14.2.el8 2.x86 64 _ _ 4.18.0-193.6.3.el8 2.x86 64 _ _ 4.18.0-193.1.2.el8 2.x86 64 _ _ 4.18.0-193.el8.x86 64 _ 4.18.0-147.8.1.el8 1.x86 64 _ _ 4.18.0-147.5.1.el8 1.x86 64 _ _ 4.18.0-147.3.1.el8 1.x86 64 _ _ 4.18.0-80.11.2.el8 0.x86 64 _ _ 4.19.x - 4.20.x series 4.20.13-1.el7.elrepo.x86 64 _ 4.19.118-2.el7.centos.x86 64 _ 4.19.113-300.el7.x86 64 _ 4.19.104-300.el7.x86 64 _ 4.19.110-300.el7.x86 64 _ 4.19.94-300.el7.x86 64 _ 4.19.12-1.el7.elrepo.x86 64 _ 4.19.1-1.el7.elrepo.x86 64 _ 5.3.x - 5.8.x series 5.8.8-1.el7.elrepo.x86 64 _ 5.6.5-1.el7.elrepo.x86 64 _ 5.5.7-1.el7.elrepo.x86 64 _ 5.5.5-1.el7.elrepo.x86 64 _ 5.5.1-1.el7.elrepo.x86 64 _ 5.4.268-1.el8.elrepo.x86 64 _ |
|---|---|---|

|   |   | 5.4.268-1.el7.elrepo.x86 64 _ 5.4.265-1.el7.elrepo.x86 64 _ 5.4.264-1.el7.elrepo.x86 64 _ 5.4.262-1.el8.elrepo.x86 64 _ 5.4.259-1.el7.elrepo.x86 64 _ 5.4.258-1.el7.elrepo.x86 64 _ 5.4.257-1.el7.elrepo.x86 64 _ 5.4.256-1.el7.elrepo.x86 64 _ 5.4.255-1.el7.elrepo.x86 64 _ 5.4.254-1.el7.elrepo.x86 64 _ 5.4.253-1.el8.elrepo.x86 64 _ 5.4.249-1.el7.elrepo.x86 64 _ 5.4.247-1.el7.elrepo.x86 64 _ 5.4.246-1.el7.elrepo.x86 64 _ 5.4.245-1.el7.elrepo.x86 64 _ 5.4.243-1.el7.elrepo.x86 64 _ 5.4.242-1.el7.elrepo.x86 64 _ 5.4.240-1.el7.elrepo.x86 64 _ 5.4.231-1.el7.elrepo.x86 64 _ 5.4.230-1.el7.elrepo.x86 64 _ 5.4.228-1.el7.elrepo.x86 64 _ 5.4.225-200.el7.x86 64 _ 5.4.225-1.el7.elrepo.x86 64 _ 5.4.223-1.el7.elrepo.x86 64 _ 5.4.221-1.el7.elrepo.x86 64 _ 5.4.210-1.el7.elrepo.x86 64 _ 5.4.209-1.el7.elrepo.x86 64 _ 5.4.208-1.el7.elrepo.x86 64 _ 5.4.207-1.el7.elrepo.x86 64 _ 5.4.204-1.el7.elrepo.x86 64 _ 5.4.201-1.el7.elrepo.x86 64 _ 5.4.195-1.el7.elrepo.x86 64 _ 5.4.194-1.el7.elrepo.x86 64 _ 5.4.188-1.el7.elrepo.x86 64 _ 5.4.181-1.el7.elrepo.x86 64 _ 5.4.179-1.el7.elrepo.x86 64 _ 5.4.173-1.el7.elrepo.x86 64 _ 5.4.172-1.el7.elrepo.x86 64 _ 5.4.170-1.el7.elrepo.x86 64 _ 5.4.168-1.el7.elrepo.x86 64 _ 5.4.165-1.el7.elrepo.x86 64 _ 5.4.157-1.el7.elrepo.x86 64 _ |
|---|---|---|

|   |   | 5.4.155-200.el7.x86 64 _ 5.4.155-1.el7.elrepo.x86 64 _ 5.4.150-1.el7.elrepo.x86 64 _ 5.4.148-1.el7.elrepo.x86 64 _ 5.4.144-1.el7.elrepo.x86 64 _ 5.4.143-1.el7.elrepo.x86 64 _ 5.4.132-1.el7.elrepo.x86 64 _ 5.4.131-1.el7.elrepo.x86 64 _ 5.4.129-1.el7.elrepo.x86 64 _ 5.4.119-19.0009.28 5.4.119-19-0009.11 5.4.119-19-0009.1 5.4.109-1.el7.elrepo.x86 64 _ 5.4.91-1.el7.elrepo.x86 64 _ 5.4.86-1.el7.elrepo.x86 64 _ 5.4.42-200.el7.x86 64 _ 5.4.8-1.el7.elrepo.x86 64 _ 5.3.8-1.el7.elrepo.x86 64 _ 5.3.7-1.el7.elrepo.x86 64 _ 5.3.6-1.el7.elrepo.x86 64 _ 5.3.0-1.el7.elrepo.x86 64 _ 5.10.x - 5.13.x series 5.13.2-1.el7.elrepo.x86 64 _ 5.12.12-1.el7.elrepo.x86 64 _ 5.12.3-1.el7.elrepo.x86 64 _ 5.11.8-1.el7.elrepo.x86 64 _ 5.11.6-1.el7.elrepo.x86 64 _ 5.11.1-1.el7.elrepo.x86 64 _ 5.10.9-1.el7.elrepo.x86 64 _ 5.14.0 series 5.14.0-412.el9.x86 64 _ 5.14.0-407.el9.x86 64 _ 5.14.0-391.el9.x86 64 _ 5.14.0-386.el9.x86 64 _ 5.14.0-383.el9.x86 64 _ 5.14.0-366.el9.x86 64 _ 5.14.0-362.18.1.el9 3.x86 64 _ _ 5.14.0-362.13.1.el9 3.x86 64 _ _ 5.14.0-362.8.1.el9 3.x86 64 _ _ 5.14.0-361.el9.x86 64 _ 5.14.0-350.el9.x86 64 _ 5.14.0-333.el9.x86 64 _ |
|---|---|---|

|   |   | 5.14.0-325.el9.x86 64 _ 5.14.0-312.el9.x86 64 _ 5.14.0-307.el9.x86 64 _ 5.14.0-299.el9.x86 64 _ 5.14.0-289.el9.x86 64 _ 5.14.0-285.el9.x86 64 _ 5.14.0-284.30.1.el9 2.x86 64 _ _ 5.14.0-284.25.1.el9 2.x86 64 _ _ 5.14.0-284.18.1.el9 2.x86 64 _ _ 5.14.0-284.11.1.el9 2.x86 64 _ _ 5.14.0-267.el9.x86 64 _ 5.14.0-252.el9.x86 64 _ 5.14.0-229.el9.x86 64 _ 5.14.0-226.el9.x86 64 _ 5.14.0-210.el9.x86 64 _ 5.14.0-205.el9.x86 64 _ 5.14.0-197.el9.x86 64 _ 5.14.0-191.el9.x86 64 _ 5.14.0-177.el9.x86 64 _ 5.14.0-162.23.1.el9 1.x86 64 _ _ 5.14.0-162.18.1.el9 1.x86 64 _ _ 5.14.0-162.12.1.el9 1.x86 64 _ _ 5.14.0-162.6.1.el9 1.x86 64 _ _ 5.14.0-160.el9.x86 64 _ 5.14.0-148.el9.x86 64 _ 5.14.0-134.el9.x86 64 _ 5.14.0-119.el9.x86 64 _ 5.14.0-70.30.1.el9 0.x86 64 _ _ 5.14.0-70.17.1.el9 0.x86 64 _ _ 5.15.x - 5.19.x series 5.19.12-1.el7.elrepo.x86 64 _ 5.19.1-1.el7.elrepo.x86 64 _ 5.19.0-1.el7.elrepo.x86 64 _ 5.18.7-1.el7.elrepo.x86 64 _ 5.18.6-1.el7.elrepo.x86 64 _ 5.18.4-1.el7.elrepo.x86 64 _ 5.18.0-1.el7.elrepo.x86 64 _ 5.17.6-1.el7.elrepo.x86 64 _ 5.17.1-1.el7.elrepo.x86 64 _ 5.17.0-1.el7.elrepo.x86 64 _ 5.16.12-1.el7.elrepo.x86 64 _ 5.15.102-1.el7.x86 64 _ |
|---|---|---|

|   |   | 5.15.11-1.el7.elrepo.x86 64 _ 5.15.6-1.el7.elrepo.x86 64 _ 5.15.5-1.el7.elrepo.x86 64 _ 5.15.2-1.el7.elrepo.x86 64 _ 6.x.x series 6.6.4-1.el8.elrepo.x86 64 _ 6.6.1-1.el7.elrepo.x86 64 _ 6.4.12-1.el7.elrepo.x86 64 _ 6.4.11-1.el7.elrepo.x86 64 _ 6.4.10-1.el7.elrepo.x86 64 _ 6.4.8-1.el7.elrepo.x86 64 _ 6.4.7-1.el7.elrepo.x86 64 _ 6.4.3-1.el7.elrepo.x86 64 _ 6.4.2-1.el7.elrepo.x86 64 _ 6.4.1-1.el7.elrepo.x86 64 _ 6.4.0-1.el7.elrepo.x86 64 _ 6.3.9-1.el7.elrepo.x86 64 _ 6.3.8-1.el7.elrepo.x86 64 _ 6.3.7-1.el7.elrepo.x86 64 _ 6.3.6-1.el7.elrepo.x86 64 _ 6.3.5-1.el7.elrepo.x86 64 _ 6.3.4-1.el7.elrepo.x86 64 _ 6.3.3-1.el7.elrepo.x86 64 _ 6.3.2-1.el7.elrepo.x86 64 _ 6.3.1-1.el7.elrepo.x86 64 _ 6.3.0-1.el7.elrepo.x86 64 _ 6.2.12-1.el8.elrepo.x86 64 _ 6.2.12-1.el7.elrepo.x86 64 _ 6.2.11-1.el7.elrepo.x86 64 _ 6.2.10-1.el7.elrepo.x86 64 _ 6.2.9-1.el7.elrepo.x86 64 _ 6.2.8-1.el7.elrepo.x86 64 _ 6.2.7-1.el7.elrepo.x86 64 _ 6.2.6-1.el7.elrepo.x86 64 _ 6.2.2-1.el7.elrepo.x86 64 _ 6.2.1-1.el7.elrepo.x86 64 _ 6.1.0-1.el7.elrepo.x86 64 _ 6.0.10-1.el7.elrepo.x86 64 _ 6.0.6-1.el9.elrepo.x86 64 _ 6.0.1-1.el7.elrepo.x86 64 _ |
|---|---|---|

|   |   | 3.x.x series 3.19.0-80-generic 3.19.0-25-generic 3.13.0-170-generic 3.13.0-169-generic 3.13.0-164-generic 3.13.0-153-generic 3.13.0-145-generic 3.13.0-144-generic 3.13.0-135-generic 3.13.0-92-generic 3.13.0-86-generic 3.13.0-65-generic 3.13.0-32-generic 3.13.0-30-generic 3.2.0-126-generic 3.2.0-67-generic 4.4.0 series 4.4.0-210-generic 4.4.0-208-generic 4.4.0-206-generic 4.4.0-203-generic 4.4.0-201-generic 4.4.0-200-generic 4.4.0-198-generic 4.4.0-197-generic 4.4.0-194-generic 4.4.0-193-generic 4.4.0-190-generic 4.4.0-189-generic 4.4.0-187-generic 4.4.0-186-generic 4.4.0-185-generic 4.4.0-184-generic 4.4.0-179-generic 4.4.0-178-generic 4.4.0-177-generic 4.4.0-176-generic 4.4.0-174-generic 4.4.0-173-generic 4.4.0-171-generic |
|---|---|---|

|   |   | 4.4.0-170-generic 4.4.0-169-generic 4.4.0-166-generic 4.4.0-165-generic 4.4.0-164-generic 4.4.0-161-generic 4.4.0-159-generic 4.4.0-157-generic 4.4.0-154-generic 4.4.0-151-generic 4.4.0-150-generic 4.4.0-148-generic 4.4.0-146-generic 4.4.0-145-generic 4.4.0-143-generic 4.4.0-142-generic 4.4.0-141-generic 4.4.0-140-generic 4.4.0-139-generic 4.4.0-138-generic 4.4.0-137-generic 4.4.0-135-generic 4.4.0-131-generic 4.4.0-130-generic 4.4.0-128-generic 4.4.0-127-generic 4.4.0-124-generic 4.4.0-122-generic 4.4.0-119-generic 4.4.0-117-generic 4.4.0-116-generic 4.4.0-112-generic 4.4.0-109-generic |
|---|---|---|
|   |   | 4.4.0-105-generic 4.4.0-104-generic 4.4.0-101-generic 4.4.0-98-generic 4.4.0-97-generic 4.4.0-96-generic 4.4.0-93-generic 4.4.0-87-generic 4.4.0-85-generic |

|   |   | 4.4.0-81-generic 4.4.0-79-generic 4.4.0-63-generic 4.4.0-62-generic 4.4.0-57-generic 4.4.0-53-generic 4.15.0 series 4.15.0-1098-gcp 4.15.0-1047-gcp 4.15.0-213-generic 4.15.0-212-generic 4.15.0-211-generic 4.15.0-210-generic 4.15.0-209-generic 4.15.0-208-generic 4.15.0-206-generic 4.15.0-204-generic 4.15.0-202-generic 4.15.0-201-generic 4.15.0-200-generic 4.15.0-197-generic 4.15.0-196-generic 4.15.0-194-generic 4.15.0-193-generic 4.15.0-192-generic 4.15.0-191-generic 4.15.0-190-generic 4.15.0-189-generic 4.15.0-188-generic 4.15.0-187-generic 4.15.0-184-generic 4.15.0-181-generic 4.15.0-180-generic 4.15.0-177-generic 4.15.0-176-generic 4.15.0-175-generic 4.15.0-173-generic 4.15.0-171-generic 4.15.0-170-generic 4.15.0-169-generic 4.15.0-167-generic 4.15.0-166-generic |
|---|---|---|

| Ubuntu (64-bit) | Unlimited. However, only limited kernel versions are supported. | 4.15.0-161-generic 4.15.0-163-generic 4.15.0-162-generic 4.15.0-159-generic 4.15.0-158-generic 4.15.0-156-generic 4.15.0-154-generic 4.15.0-153-generic 4.15.0-151-generic 4.15.0-147-generic 4.15.0-145-generic 4.15.0-144-generic 4.15.0-143-generic 4.15.0-141-generic 4.15.0-142-generic 4.15.0-140-generic 4.15.0-139-generic 4.15.0-137-generic 4.15.0-136-generic 4.15.0-135-generic 4.15.0-134-generic 4.15.0-132-generic 4.15.0-130-generic 4.15.0-129-generic 4.15.0-128-generic 4.15.0-124-generic 4.15.0-122-generic 4.15.0-121-generic 4.15.0-117-generic 4.15.0-118-generic 4.15.0-112-generic 4.15.0-111-generic 4.15.0-109-generic 4.15.0-108-generic 4.15.0-106-generic 4.15.0-101-generic 4.15.0-99-generic 4.15.0-96-generic 4.15.0-91-generic 4.15.0-88-generic 4.15.0-76-generic 4.15.0-74-generic |
|---|---|---|

|   |   | 4.15.0-72-generic 4.15.0-70-generic 4.15.0-66-generic 4.15.0-65-generic 4.15.0-64-generic 4.15.0-62-generic 4.15.0-58-generic 4.15.0-54-generic 4.15.0-55-generic 4.15.0-52-generic 4.15.0-51-generic 4.15.0-48-generic 4.15.0-47-generic 4.15.0-46-generic 4.15.0-45-generic 4.15.0-43-generic 4.15.0-42-generic 4.15.0-29-generic 4.15.0-23-generic 4.15.0-15-generic 4.15.0-13-generic 4.18.0 series 4.18.0-21-generic 4.18.0-15-generic 5.3.0 series 5.3.0-40-generic 5.4.0 series 5.4.0-173-generic 5.4.0-172-generic 5.4.0-171-generic 5.4.0-170-generic 5.4.0-169-generic 5.4.0-167-generic 5.4.0-166-generic 5.4.0-165-generic 5.4.0-164-generic 5.4.0-163-generic 5.4.0-162-generic 5.4.0-159-generic 5.4.0-156-generic 5.4.0-155-generic 5.4.0-154-generic |
|---|---|---|

|   |   | 5.4.0-153-generic 5.4.0-152-generic 5.4.0-151-generic 5.4.0-150-generic 5.4.0-149-generic 5.4.0-148-generic 5.4.0-147-generic 5.4.0-146-generic 5.4.0-144-generic 5.4.0-139-generic 5.4.0-137-generic 5.4.0-136-generic 5.4.0-135-generic 5.4.0-132-generic 5.4.0-131-generic 5.4.0-128-generic 5.4.0-126-generic 5.4.0-125-generic 5.4.0-124-generic 5.4.0-123-generic 5.4.0-122-generic 5.4.0-121-generic 5.4.0-120-generic 5.4.0-117-generic 5.4.0-113-generic 5.4.0-110-generic 5.4.0-109-generic 5.4.0-108-generic 5.4.0-107-generic 5.4.0-106-generic 5.4.0-105-generic 5.4.0-104-generic 5.4.0-102-generic 5.4.0-100-generic 5.4.0-99-generic 5.4.0-97-generic 5.4.0-96-generic 5.4.0-94-generic 5.4.0-92-generic 5.4.0-91-generic 5.4.0-90-generic 5.4.0-89-generic |
|---|---|---|

|   |   | 5.4.0-88-generic 5.4.0-86-generic 5.4.0-84-generic 5.4.0-83-generic 5.4.0-81-generic 5.4.0-80-generic 5.4.0-77-generic 5.4.0-75-generic 5.4.0-74-generic 5.4.0-73-generic 5.4.0-72-generic 5.4.0-70-generic 5.4.0-67-generic 5.4.0-66-generic 5.4.0-65-generic 5.4.0-62-generic 5.4.0-60-generic 5.4.0-59-generic 5.4.0-58-generic 5.4.0-54-generic 5.4.0-53-generic 5.4.0-52-generic 5.4.0-48-generic 5.4.0-47-generic 5.4.0-45-generic 5.4.0-42-generic 5.4.0-40-generic 5.4.0-31-generic 5.15.0 series 5.15.0-94-generic 5.15.0-92-generic 5.15.0-91-generic 5.15.0-89-generic 5.15.0-88-generic 5.15.0-87-generic 5.15.0-86-generic 5.15.0-84-generic 5.15.0-83-generic 5.15.0-82-generic 5.15.0-79-generic 5.15.0-78-generic 5.15.0-76-generic |
|---|---|---|

|   |   | 5.15.0-75-generic 5.15.0-73-generic 5.15.0-72-generic 5.15.0-71-generic 5.15.0-70-generic 5.15.0-69-generic 5.15.0-67-generic 5.15.0-60-generic 5.15.0-58-generic 5.15.0-56-generic 5.15.0-53-generic 5.15.0-52-generic 5.15.0-46-generic 5.15.0-43-generic 5.15.0-41-generic 5.15.0-40-generic 6.2.0 series 6.2.0-1018-gcp |
|---|---|---|
|   |   | 4.9.0 series 4.9.0-19-amd64 4.9.0-18-amd64 4.9.0-17-amd64 4.9.0-16-amd64 4.9.0-15-amd64 4.9.0-14-amd64 4.9.0-13-amd64 4.9.0-12-amd64 4.9.0-11-amd64 4.9.0-9-amd64 4.9.0-8-amd64 4.9.0-4-amd64 4.19.0 series 4.19.0-25-amd64 4.19.0-24-amd64 4.19.0-23-amd64 4.19.0-22-amd64 4.19.0-21-amd64 4.19.0-20-amd64 4.19.0-18-amd64 4.19.0-16-amd64 4.19.0-17-amd64 |

| Debian | Unlimited. However, only limited kernel versions are supported. | 4.19.0-13-amd64 4.19.0-12-amd64 4.19.0-10-amd64 4.19.0-9-amd64 4.19.0-8-amd64 4.19.0-6-amd64 5.10.0 series 5.10.0-27-amd64 5.10.0-26-amd64 5.10.0-25-amd64 5.10.0-24-amd64 5.10.0-23-amd64 5.10.0-22-amd64 5.10.0-21-amd64 |
|---|---|---|
|   |   | 5.10.0-20-amd64 5.10.0-19-amd64 5.10.0-18-amd64 5.10.0-17-amd64 5.10.0-16-amd64 5.10.0-15-amd64 5.10.0-14-amd64 5.10.0-11-amd64 5.10.0-10-amd64 5.10.0-9-amd64 5.10.0-8-amd64 6.1.0 series 6.1.0-18-amd64 6.1.0-17-amd64 6.1.0-16-amd64 6.1.0-13-amd64 6.1.0-12-amd64 6.1.0-11-amd64 6.1.0-10-amd64 |
|   |   | 3.10.0 series 3.10.0-1160.88.1.0.1.an7.x86 64 _ 3.10.0-1160.83.1.0.1.an7.x86 64 _ 3.10.0-1160.81.1.0.1.an7.x86 64 _ 3.10.0-1160.80.1.0.1.an7.x86 64 _ 3.10.0-1160.76.1.0.1.an7.x86 64 _ 3.10.0-1160.71.1.0.1.an7.x86 64 _ |

| erver Guard Advanc er Guide·Server Gu | ed Edition U ard | Alibaba Cloud Security-Server G ard Advanced Editio |
|---|---|---|
| Anolis OS (64-bit) | Unlimited. However, only limited kernel versions are supported. | 3.10.0-1160.66.1.0.1.an7.x86 64 _ 3.10.0-1160.62.1.0.1.an7.x86 64 _ 3.10.0-1160.59.1.0.1.an7.x86 64 _ 3.10.0-1062.an7.x86 64 _ 3.10.0-1160.an7.x86 64 _ 4.18.0 series 4.18.0-477.36.1.0.1.an8.x86 64 _ 4.18.0-477.27.1.0.1.an8.x86 64 _ 4.18.0-477.21.1.0.1.an8.x86 64 _ 4.18.0-477.13.1.0.1.an8.x86 64 _ 4.18.0-425.19.2.0.1.an8.x86 64 _ 4.18.0-425.13.1.0.1.an8.x86 64 _ 4.18.0-372.32.1.an8 6.x86 64 _ _ 4.18.0-372.26.1.an8 6.x86 64 _ _ 4.18.0-372.19.1.an8 6.x86 64 _ _ 4.18.0-372.16.1.an8 6.x86 64 _ _ 4.18.0-372.9.1.an8.x86 64 _ 4.18.0-348.23.1.an8 5.x86 64 _ _ 4.18.0-348.20.1.an8 5.x86 64 _ _ 4.18.0-348.12.2.an8.x86 64 _ 4.18.0-348.2.1.an8 4.x86 64 _ _ 4.18.0-305.an8.x86 64 _ 4.19.91 series 4.19.91-27.7.an7.x86 64 _ 4.19.91-27.4.an8.x86 64 _ 4.19.91-27.1.an7.x86 64 _ 4.19.91-27.an7.x86 64 _ 4.19.91-26.6.an8.x86 64 _ 4.19.91-26.6.an7.x86 64 _ 4.19.91-26.5.an8.x86 64 _ 4.19.91-26.5.an7.x86 64 _ 4.19.91-26.4.an8.x86 64 _ 4.19.91-26.4.an7.x86 64 _ 4.19.91-26.1.an8.x86 64 _ 4.19.91-26.an8.x86 64 _ 4.19.91-26.an7.x86 64 _ 4.19.91-25.8.an8.x86 64 _ 4.19.91-25.7.an8.x86 64 _ 4.19.91-25.7.an7.x86 64 _ 4.19.91-25.2.an7.x86 64 _ 4.19.91-24.8.an8.x86 64 _ |

|   |   | 5.10.134 series 5.10.134-16.1.an8.x86 64 _ 5.10.134-15.2.an8.x86 64 _ 5.10.134-15.an8.x86 64 _ 5.10.134-14.1.an8.x86 64 _ 5.10.134-14.an8.x86 64 _ 5.10.134-13.1.an8.x86 64 _ 5.10.134-13.an8.x86 64 _ |
|---|---|---|
| RHEL | Unlimited. However, only limited kernel versions are supported. | 2.6.32 series 2.6.32-754.35.1.el6.x86 64 _ 2.6.32-754.17.1.el6.x86 64 _ 2.6.32-754.9.1.el6.x86 64 _ 2.6.32-754.el6.x86 64 _ 2.6.32-696.el6.x86 64 _ 2.6.32-573.el6.x86 64 _ 2.6.32-431.el6.x86 64 _ 2.6.32-358.el6.x86 64 _ 2.6.32-279.el6.x86 64 _ 2.6.32-220.el6.x86 64 _ 3.10.0 series 3.10.0-1160.108.1.el7.x86 64 _ 3.10.0-1160.102.1.el7.x86 64 _ 3.10.0-1160.99.1.el7.x86 64 _ 3.10.0-1160.95.1.el7.x86 64 _ 3.10.0-1160.92.1.el7.x86 64 _ 3.10.0-1160.90.1.el7.x86 64 _ 3.10.0-1160.88.1.el7.x86 64 _ 3.10.0-1160.83.1.el7.x86 64 _ 3.10.0-1160.81.1.el7.x86 64 _ 3.10.0-1160.80.1.el7.x86 64 _ 3.10.0-1160.76.1.el7.x86 64 _ 3.10.0-1160.71.1.el7.x86 64 _ 3.10.0-1160.59.1.el7.x86 64 _ 3.10.0-1160.45.1.el7.x86 64 _ 3.10.0-1160.42.2.el7.x86 64 _ 3.10.0-1160.21.1.el7.x86 64 _ 3.10.0-1160.11.1.el7.x86 64 _ 3.10.0-1160.2.1.el7.x86 64 _ 3.10.0-1160.el7.x86 64 _ |
|   |   | 3.10.0-1127.el7.x86 64 _ 3.10.0-1062.el7.x86 64 _ |

|   |   | 3.10.0-957.el7.x86 64 _ 3.10.0-862.el7.x86 64 _ 3.10.0-693.2.2.el7.x86 64 _ 4.18.0 series 4.18.0-513.11.1.el8 9.x86 64 _ _ 4.18.0-477.21.1.el8 8.x86 64 _ _ 4.18.0-477.15.1.el8 8.x86 64 _ _ 4.18.0-477.13.1.el8 8.x86 64 _ _ 4.18.0-477.10.1.el8 8.x86 64 _ _ 4.18.0-425.19.2.el8 7.x86 64 _ _ 4.18.0-372.19.1.el8 6.x86 64 _ _ 4.18.0-372.9.1.el8.x86 64 _ 4.18.0-348.12.2.el8 5.x86 64 _ _ 4.18.0-348.2.1.el8 5.x86 64 _ _ 4.18.0-305.3.1.el8 4.x86 64 _ _ 4.18.0-80.el8.x86 64 _ 5.14.0 series 5.14.0-284.11.1.el9 2.x86 64 _ _ |
|---|---|---|
|   |   | 3.10.0 series 3.10.0-1160.al7.1.x86 64 _ 3.10.0-1127.19.1.al7.1.x86 64 _ 3.10.0-1127.al7.1.x86 64 _ 3.10.0-1062.12.1.al7.1.x86 64 _ |
|   |   | 3.10.0-1062.4.1.al7.1.x86 64 _ 3.10.0-514.2.3.al7.x86 64 _ 4.4.x series 4.4.95-3.al7.x86 64 _ 4.4.95-2.al7.x86 64 _ 4.4.95-1.al7.x86 64 _ 4.4.24-2.al7.x86 64 _ 4.19.x series 4.19.91-27.7.al7.x86 64 _ 4.19.91-27.6.al7.x86 64 _ 4.19.91-27.5.al7.x86 64 _ 4.19.91-27.4.al7.x86 64 _ 4.19.91-27.3.al7.x86 64 _ 4.19.91-27.2.al7.x86 64 _ 4.19.91-27.1.al7.x86 64 _ 4.19.91-27.al7.x86 64 _ 4.19.91-26.6.al7.x86 64 _ |

|   |   | 4.19.91-26.5.al7.x86 64 _ 4.19.91-26.4.al7.x86 64 _ 4.19.91-26.3.al7.x86 64 _ 4.19.91-26.2.al7.x86 64 _ 4.19.91-26.1.al7.x86 64 _ 4.19.91-26.al7.x86 64 _ 4.19.91-25.8.al7.x86 64 _ 4.19.91-25.7.al7.x86 64 _ 4.19.91-25.6.al7.x86 64 _ 4.19.91-25.3.al7.x86 64 _ 4.19.91-25.1.al7.x86 64 _ 4.19.91-25.al7.x86 64 _ 4.19.91-24.1.al7.x86 64 _ 4.19.91-24.al7.x86 64 _ |
|---|---|---|
| Alibaba Cloud Linux (64-bit) | Unlimited. However, only limited kernel versions are supported. | 4.19.91-23.1.al7.x86 64 _ 4.19.91-23.al7.x86 64 _ 4.19.91-22.2.al7.x86 64 _ 4.19.91-22.1.al7.x86 64 _ 4.19.91-22.fc.1.al7.x86 64 _ 4.19.91-22.al7.x86 64 _ 4.19.91-21.2.al7.x86 64 _ 4.19.91-21.al7.x86 64 _ 4.19.91-19.2.al7.x86 64 _ 4.19.91-19.1.al7.x86 64 _ 4.19.91-18.al7.x86 64 _ 4.19.91-007.ali4000.alios7.x86 64 _ 4.19.81-17.2.al7.x86 64 _ 4.19.81-17.1.al7.x86 64 _ 4.19.81-17.al7.x86 64 _ 4.19.57-15.1.al7.x86 64 _ 4.19.43-13.2.al7.x86 64 _ 4.19.36-12.al7.x86 64 _ 4.19.34-11.al7.x86 64 _ 4.19.24-9.al7.x86 64 _ 4.19.24-7.14.al7.x86 64 _ 4.19.24-7.al7.x86 64 _ 5.10.x series 5.10.134-16.1.al8.x86 64 _ 5.10.134-16.al8.x86 64 _ 5.10.134-15.2.al8.x86 64 _ 5.10.134-15.1.al8.x86 64 _ 5.10.134-15.al8.x86 64 _ |

|   |   | 5.10.134-14.1.al8.x86 64 _ 5.10.134-14.al8.x86 64 _ 5.10.134-13.1.al8.x86 64 _ 5.10.134-13.al8.x86 64 _ 5.10.134-12.2.al8.x86 64 _ 5.10.134-12.1.al8.x86 64 _ 5.10.134-12.al8.x86 64 _ 5.10.112-11.2.al8.x86 64 _ 5.10.112-11.1.al8.x86 64 _ 5.10.112-11.al8.x86 64 _ 5.10.84-10.4.al8.x86 64 _ 5.10.84-10.3.al8.x86 64 _ 5.10.84-10.2.al8.x86 64 _ 5.10.60-9.al8.x86 64 _ 5.10.23-6.al8.x86 64 _ 5.10.23-6.1.al8.x86 64 _ 5.10.23-5.al8.x86 64 _ |
|---|---|---|
| Oracle Linux | Unlimited. However, only limited kernel versions are supported. | 4.14.35 series 4.14.35-2047.505.4.3.el7uek.x86 64 _ 5.4.17 series 5.4.17-2136.311.6.1.el8uek.x86 64 _ 5.4.17-2136.302.7.2.2.el8uek.x86 64 _ 5.4.17-2136.310.7.1.el8uek.x86 64 _ |

**Step 1: Enable web tamper proofing for servers**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Tamper Proofing**.
4. The first time you use web tamper proofing, click **Add Servers for Protection** on the
**Tamper Proofing** page.
If this is not the first time that you use web tamper proofing, click the **Management** tab on the **Tamper Proofing** page and click **Add Server**.
5. In the **Add Servers for Protection** panel, select a server type and the server that you
want to protect. Supported server types are Windows and Linux. If you have multiple organizations, select the required resource set and specify servers.
6. Click **Next**. In the **Add Directory** step, configure the parameters.
By default, the **Whitelist Mode** is used. In whitelist mode, you must specify the directories and formats of files that you want to protect. You can click **Blacklist Mode** to switch to the blacklist mode. In blacklist mode, you must specify the directory that you want to protect, and the subdirectories, formats of files, and files that **do not require protection** in the protected directory.

**Whitelist Mode**

In whitelist mode, Server Guard intercepts or generates an alert for modifications to the files of the specified formats in the protected directory.

| Parameter | Description |
|---|---|
| Protected Directory | The server directory that you want to protect. After you specify a directory, Server Guard determines whether to intercept modifications to the name, content, or attribute of the files in the directory based on the process whitelist and prevention mode that you specify. Enter a value in the /The name of the directory/ format. Example: /tmp/ . Note Servers that run Linux or Windows operating systems use different path formats. Enter a valid directory path based on the type of your operating system. |
| Protected File Formats | The formats of the files that you want to protect. You can select formats from the drop-down list. You can also enter formats that are not displayed in the drop-down list. Note All formats of files can be added for protection. |

| Prevention Mode | Interception Mode: Server Guard intercepts suspicious processes and abnormal file changes. This ensures the security of websites and files on your server. Alert Mode: Server Guard identifies suspicious processes and abnormal file changes and generates alerts. Important If the operating system or kernel version of your server is not supported by the whitelist feature, Server Guard does not generate alerts. In this case, if you set Prevention Mode to Alert Mode, Server Guard intercepts suspicious processes. For more information, see Supported versions of operating systems and kernels. |   |
|---|---|---|
| Local Backup Directory | The directory in which backup files of the protected directories are stored. By default, Server Guard uses /usr/local/aegis/bak as the backup directory for Linux servers and C:\Program Files (x86)\Alibaba\Aegis\bak as the backup directory for Windows servers. You can change the default backup directories. Important If the operating system or kernel version of your server iss upporte d by the whitelist feature, you do not need to configure the Local Backup Directory parameter. |   |

|   | (x86)\Alibaba\Aegis\bak |
|---|---|

**Sample configuration**

If you specify `/tmp/` for **Protected Directory**, xml for **Protected File Formats**, and
**Interception Mode** for **Prevention Mode**, Server Guard intercepts the modifications to
the XML files in the tmp directory.

**Blacklist Mode**

In blacklist mode, Server Guard does not intercept or generate alerts for modifications to the specified subdirectories, files of the specified formats, or specified files in the protected directory. Server Guard intercepts and generates an alert for modifications to other subdirectories and files in the protected directory. For more information about how to configure the **Protected Directory**, **Prevention**
**Mode**, and **Local Backup Directory** parameters, see the **Whitelist Mode** section in
this topic.

| Parameter | Description |
|---|---|
| Excluded Sub- Directories | Enter the subdirectories that do not require web tamper proofing. Enter a value in the Subdirectory name/ format. Example: dir1/dir0/ . Click Add Sub-Directory to add another subdirectory. Server Guard does not protect files in the excluded subdirectories. |

| Excluded File Formats | The formats of the files that do not require protection. Server Guard does not protect files in the excluded formats. |
|---|---|
| Excluded Files | The files that do not require protection. Enter a value in the Subdirectory name/File name format. Example: dir2/file3 . Click Add File to add another file. |

> **Important:** The **Excluded Sub-Directories**, **Excluded File Formats**, and **Excluded Files** parameters are evaluated by using a logical **OR**.

**Sample configuration**

| ry, | dir1/dir0/ |
|---|---|
| dir2/file3 |   |

If you specify `/tmp/` for **Protected Directory**, `dir1/dir0/` for **Excluded Sub-**
**Directories**, txt for **Excluded File Formats**, `dir2/file3` for **Excluded Files**, and
**Interception Mode** for **Prevention Mode**, the files in the `dir1` subdirectory below
`dir0` in the tmp directory, TXT files in the tmp directory, or the `file3` file in the `dir2` subdirectory in the tmp directory can be modified. The modifications to other subdirectories and files in the tmp directory are intercepted by Server Guard.
7. Optional. On the **Management** tab of the **Tamper Proofing** page, find the server that you
specify in the Add Servers for Protection panel and click **Add Directory** in the **Actions** column to add another directory for protection. You can click the icon next to the server name to view the list of protected directories on the server. You can find a protected directory and click **Modify** in the Actions column to modify the parameter configurations.
8. On the **Management** tab of the **Tamper Proofing** page, find the server that you specify
in the Add Servers for Protection panel and click the icon in the **Protection** column to enable the web tamper proofing feature for the server. The first time you enable this feature for a server, the status in the **Status** column of the server changes to **Initializing**, and a progress bar appears. Wait until the feature is enabled. After this feature is enabled, the status of the server changes to **Running**. The following table describes the statuses that are available in the Status column.

| Status | Description | Suggestion |
|---|---|---|
| Initializing | Web tamper proofing is being initialized. | The first time you enable the web tamper proofing feature for a server, the status is Initializing. Wait until the feature is enabled. |
| Running | Web tamper proofing is enabled and runs as expected. | None. |

| Exception | An error occurred when web tamper proofing is enabled. | Move the pointer over Exception, view the causes, and then click Retry. |
|---|---|---|
| Not Initialized | The switch in the Protection column is turned off. | Turn on the switch in the Protection column. |

**Step 2: View the server status**

On the **Protection** tab of the **Tamper Proofing** page, view the details of the protection status. The overview statistics on web tamper proofing, and the statistics on the top 5 protected files and top 5 blocked processes in the last 15 days Details of alerts triggered by web tamper proofing The alert list displays all alerts that are generated for abnormal file changes on your server regardless of whether the alerts are generated in **Interception Mode** or **Alert Mode**. You can view the details of an alert, including the severity level, alert name, affected assets, file path, process name, and protection status. The severity level is **Medium**. List of **Handled** alerts By default, alerts that are generated in Interception Mode are displayed, and the **status** of the alerts is **Defended**. This indicates that the web tamper proofing feature detects abnormal file changes and then intercepts the processes that modify files. List of **Unhandled** alerts Alerts that are generated in **Alert Mode** are displayed, and the default **status** of the alerts is **Unhandled**. This indicates that the web tamper proofing feature generates alerts for suspicious processes and abnormal file changes. If an intercepted process that modifies files or the process that modifies files and then triggers an alert is required by your workloads, you can add the process to the whitelist to allow the process. After you add a process for which an alert is generated to the whitelist, the status of the alert changes to **Added to Whitelist**, and the alert is added to the
**Handled** alert list. For more information, see **Add a process to the whitelist** .

> **Important:** If an alert is reported more than 100 times, we recommend that you handle the alert at the earliest opportunity.

**Add a process to the whitelist**

If you confirm that the process that modifies the protected files on your server is normal and want the process to modify the files, you can add the process to the whitelist.

> **Important:** You can add a process to the process whitelist only if the operating system and kernel versions of your server are supported by the whitelist feature. For more information, see **Supported versions of operating systems and kernels** .
> Attackers may exploit the processes in the whitelist to compromise your server. We recommend that you add only trusted processes to the whitelist.

On the **Protection** tab of the **Tamper Proofing** page, add a normal process to the whitelist.

**Add a process for which an alert is generated to the whitelist**

1. In the **Unhandled** alert list, find a process that you want to add to the whitelist and click
**Handle** in the **Actions** column.
2. In the dialog box that appears, set the **Process Method** parameter to **Add To Whitelist**
and click **Process Now**. A process may run on multiple servers or run in multiple directories on the same server. If you want to add the process to the whitelist, select **Process servers with the same**
**process at the same time**.
You can also find alerts generated for processes that modify files in the **Handled** alert list and add an alert whose status is **Defended** to the whitelist. You can view process paths to check whether a process is normal.

**Add multiple processes for which alerts are generated to the**

**whitelist at the same time**

1. In the alert event list on the Protection tab, find and select the processes that you want to
add to the whitelist.
2. Click **Add Process to Whitelist** below the list. In the message that appears, click **OK**.

**Specify processes in the process whitelist**

1. Click the number below **Whitelist** to go to the **Process Management** panel.
2. Click **Enter the Whitelist**. Then, configure the **Process Path** and **Server Name/IP**
parameters to add a process to the process whitelist.

**View the processes in the whitelist or remove processes from**

**the whitelist**

1. Click the number below **Whitelist** to go to the **Process Management** panel. In the
Process Management panel, you can view the information about all suspicious processes that are added to the whitelist. The information includes the server on which the processes run, the paths to the processes, and the numbers of times that the processes modify files.
2. In the Process Management panel, find the suspicious process that you want to remove and
click **Remove from Whitelist** in the **Actions** column. You can also select multiple suspicious processes and click **Remove from Whitelist** below the list to remove the processes from the whitelist at a time.

#### 3.4.3 Application whitelist

The application whitelist feature prevents unauthorized programs from running on your servers and provides a trusted running environment for your servers. This topic describes how to use the application whitelist feature.

**Create an application whitelist policy**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Policies** tab of the **Application Whitelist** page, click **Create Policy**.
5. In the**Create Application Whitelist** panel, configure an application whitelist policy and
click **Create**.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |
| Policy Mode | The mode of the policy. Valid values: Alert Mode and Observation Mode. Note In observation mode, no alerts are generated. After the observation ends, the observation mode is automatically changed to the alert mode. |
| Observation End Time | If you set the Policy Mode parameter to Observation Mode, you must configure this parameter. |

| Policy Content | The content of the policy. You can configure the following items: Process Collection Tasks: Click Settings. In the Select Process Collection Task panel, select tasks and click OK. Custom Process Group: Click Settings. In the Select Custom Process Group panel, select process groups and click OK. Process base white Library: the default item that refers to the basic whitelist of Apsara Stack system images and the basic whitelist of YUM repositories. |
|---|---|
| Select an asset | The assets on which you want the policy to take effect. |

In the application whitelist policy list, you can perform the following operations: Modify a policy: Find the policy that you want to modify and click **Edit** in the **Actions** column. Enable or disable a policy: Select the policy that you want to enable or disable and click
**Enable all or Disable all** below the policy list.
Delete a policy: Select the policy that you want to delete and click **Delete** below the policy list.

**View the servers on which the application whitelist policy takes**

**effect**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Application Whitelist**page, click the **Servers**tab and view the servers on which
the policy takes effect. You can filter servers by policy status, policy mode, and asset status. You can also filter servers by server group and protection status. In the server list, you can perform the following operations: View the policy details of a server: Find the server that you want to view and click
**Details**in the**Actions**column.
Enable or disable the policy for a server: Select the server for which you want to enable or disable the policy and click**Enable Policy or Disable Policy** below the server list. Remove the policy: Select the server from which you want to remove the policy and choose**More Operations**>**Detach Policy**below the server list.

**Create a collection task**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Application Whitelist** page, click the **Knowledge Bases** tab and then click the
**Process Collection** tab.
5. On the**Process Collection**tab, click**Create Collection Task**.
6. In the**Create Process Collection Task**panel, configure Task Name, Observation End
Time, and Scan Assets, and click**OK**. You can re-scan assets and view task details in the collection task list.

**Create a custom process group**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.
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

##### 3.4.5.2 View and handle alerts

This topic describes how to view and handle alerts that are generated by Server Guard.

**Background information**

After Apsara Stack Security generates an alert, the information about the alert is displayed. If the alert is not handled, the alert is displayed in the **Unhandled Alerts** list on the **Security**
**Alerts** page. After the alert is handled, the status of the alert changes from **Unhandled**
**Alerts** to **Handled**.

> **Note:** Apsara Stack Security retains the records of **Unhandled Alerts** and **Handled** on the **Security Alerts** page. By default, the records of **Unhandled Alerts** are displayed.

**Platform**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

**View the details of an alert**

1. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
2. On the Security Alerts page, view or search for all alerts and the details of the alerts.

**Handle alerts**

1. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
2. On the **Security Alerts** page, find the alert that you want to handle and click **Handle** in
the **Actions** column. In the dialog box that appears, configure Process Method and click
**Process Now**.

> **Note:** If the alert is related to multiple exceptions, the details panel of the alert appears after you click **Handle**. You can separately handle the exceptions in the panel.

**Ignore**: If you ignore the alert, the status of the alert changes to **Handled**. Server Guard
no longer generates this alert.
**Add To Whitelist**: If the alert is a false positive, you can add the alert to the whitelist.
Then, the status of the alert changes to **Handled**. Server Guard no longer generates this alert. In the **Handled** alert list, you can click **Cancel whitelist** to remove the alert from the whitelist.

> **Note:** A false positive indicates that Server Guard generated an alert on a normal process. A common false positive includes alerts that are generated for a **suspicious process** **that sends TCP packets**. The false positive notifies you that suspicious scans on other devices are detected on your servers.

**Handled manually**: This alert reports a suspicious exception. We recommend that you
troubleshoot the exception based on the handling suggestions. After you troubleshoot the exception, click Process Now. Then, the alert status changes to Handled.
**Batch unhandled**: This method allows you to handle multiple alerts at a time. Before
you handle multiple alerts at a time, we recommend that you view the details of the alerts.
3. **Optional.** If you confirm that one or more alerts can be ignored or are false positives,
select the alerts and click **Ignore Once** or **Whitelist** on the **Security Alerts** page.

**Export alerts**

1. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
2. On the **Security Alerts** page, click the
icon above the alert list to export alerts. After the alert list is exported, the **Done** message appears in the upper-right corner of the Security Alerts page.
3. In the **Done** notification of the **Alerts** page, click **Download**.
The alert list is downloaded to your computer.

**Download archived data**

Server Guard automatically enables alert event archiving and saves archived data for 185 days. You can download archived data.

**Important**

In multi-level organization mode, only an account that has level-1 organization permissions or global organization permissions can download archived data.
1. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
2. In the upper-right corner of the page, click **Archive data**.
3. In the dialog box that appears, find the data that you want to download and click
**Download**.

##### 3.4.5.3 View exceptions related to an alert

Server Guard supports automatic analysis of exceptions related to an alert. You can click the name of an alert in the alert list to view and manage all exceptions that are related to the alert. You can also view the results of automatic attack tracing to analyze and handle the exceptions.

**Background information**

Security Center automatically associates alerts with exceptions in real time to detect potential threats. Exceptions related to an alert are listed in chronological order. This allows you to analyze and handle the exceptions to improve the emergency response mechanism of your system. An automatically correlated alert is identified by the icon.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the Security Alerts page, click the name of the required alert in the **Event** column. The
alert details panel appears.
5. In the alert details panel, view the alert details and related exceptions of the alert. Then,
handle the exceptions. View the details about an alert View the assets that are affected by an alert, the first time and last time when the alert was triggered, and the details about the related exceptions. View affected assets Move the pointer over the name of an **affected asset** to view the details about the asset. View and manage **related exceptions** In the **Related Exceptions** section, view the details about all the exceptions that are related to the alert. You can also view suggestions on how to handle the exceptions. Click **Note** to the right of an exception to add a note for the exception. Click the icon to the right of a note to delete the note.

##### 3.4.5.4 Quarantine

Sever Guard can quarantine malicious files. Quarantined files are listed in the Quarantine panel of the Security Alerts page. The system automatically deletes a quarantined file 30 days after the file is quarantined. You can restore a quarantined file with a few clicks before the file is deleted. This topic describes how to view and restore quarantined files.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the **Security Alerts** page, click **Quarantine** in the upper-right corner.
In the **Quarantine** panel, you can perform the following operations: View information about quarantined files. The information includes server IP addresses, paths that store the files, file status, and modification time. Click **Restore** in the **Actions** column to remove a file. The file is displayed in the alert list again.

##### 3.4.5.5 Configure alerts

This topic describes how to configure alerts. You can specify approved logon locations and web directories to scan. You can also configure advanced logon settings.

**Background information**

Server Guard supports advanced logon settings. You can configure fine-grained logon detection rules. For example, you can specify approved logon IP addresses, approved logon time ranges, and approved logon accounts to block unauthorized access to your assets.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. In the upper-right corner of the page that appears, click **Settings**.
If you have multiple organizations, select the required organization and resource set. Then, configure parameters on different tabs.

**Add an approved logon location**

a. In the **Approved Logon Location** section, click **Manage** on the right side. b. Select the logon location that you want to add and select the servers for which you want to allow logons from the location. c. Click **OK**. Server Guard allows you to **modify** or **remove** approved logon locations. To change the servers that allow logons from an approved logon location, find the location and click **Edit** in the Actions column. To remove an approved logon location, find the location and click **Delete**.

**Configure advanced logon settings**

> **Note:** When you configure advanced logon settings, you can specify the IP addresses, accounts, and time ranges that are allowed for logons to your assets. After the advanced logon settings are configured, Server Guard sends you alerts if your assets receive logon requests that are outside the logon settings. The procedure to configure advanced logon settings is similar to the procedure to configure **approved** **logon locations**. You can follow the preceding procedure to **create**, **modify**, and **delete** advanced logon settings.

Turn on or turn off the switch to the right of **Unapproved IP Address Alert**. If you turn on the switch and your assets receive logon requests from unapproved IP addresses, alerts are triggered. Turn on or turn off the switch to the right of **Unapproved Logon Time Alert**. If you turn on the switch and your assets receive logon requests in unapproved time ranges, alerts are triggered. Turn on or turn off the switch to the right of **Unapproved Account Logon Alert**. If you turn on the switch and your assets receive logon requests from unapproved accounts, alerts are triggered.

**Add web directories to scan**

Server Guard automatically scans web directories of data assets in your servers and runs dynamic and static scan tasks. You can also manually add custom web directories. a. In the **Add Scan Targets** section, click **Manage** on the right side. b. Specify a valid web directory and select the servers on which the web directory is scanned.

> **Note:** To ensure the scan performance and efficiency, we recommend that you do not specify a root directory.

c. Click **OK**.

**Modify a whitelist rule**

**Organization-level Whitelist Rule**: You can modify or delete the whitelist rules of
your assets. Find an asset and click **Edit** in the **Actions** column to modify the whitelist rule of the asset. Find an asset and click **Delete** in the **Actions** column to delete the whitelist rule of the asset.
**Global Whitelist Rule**: The whitelist rules are configured by Apsara Stack Security
and cannot be modified.

#### 3.4.6 SDK for malicious file detection

You can use SDK for malicious file detection to detect common viruses such as ransomware and mining programs in Object Storage Service (OSS) objects to prevent the spread and execution of malicious files. This topic describes how to use SDK for malicious file detection.

**Supported virus types**

The following table describes the types of viruses that can be detected.

| Virus type | Virus name |
|---|---|
| Backdoor | Reverse shell |
| DDoS | DDoS trojan |
| Downloader | Trojan downloader |
| Engtest | Engine test program |
| Hacktool | Attacker tool |
| Trojan | High-risk program |
| Malbaseware | Tainted basic software |
| MalScript | Malicious script |
| Malware | Malicious program |
| Miner | Mining program |
| Proxytool | Proxy |

| RansomWare | Ransomware |
|---|---|
| RiskWare | Riskware |
| Rootkit | Rootkit |
| Stealer | Tool that is used to steal information |
| Scanner | Scanner |
| Suspicious | Suspicious program |
| Virus | Infectious virus |
| WebShell | Webshell |
| Worm | Worm |

**OSS file detection**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Defense** > **SDK for Malicious File Detection** .
4. Click the **OSS Object Check** tab, select a detection method and start detection. The
following table describes the supported detection methods. If your bucket is not displayed in the list on the **OSS File Check** tab, you can click
**Synchronize Buckets** to obtain the latest list of buckets.

| Detection method | Description | Procedure |
|---|---|---|

| Manual full detection | Check all objects in one or more buckets. | i. On the OSS Object Check tab, find a bucket and click Check in the Actions column, or select multiple buckets and click Batch Check below the bucket list. ii. In the Check panel, configure the Object Check Type parameter and click OK. |
|---|---|---|
| Manual incremental detection | Check only newly added objects in a bucket that has been checked. | i. On the OSS Object Check tab, find the required bucket and click Incremental Check in the Actions column. ii. In the Incremental Check panel, configure the Object Check Type parameter and click OK. |
| Automatic detection | Enable periodic automatic detection for specified buckets based on configured scan policies. We recommend that you take note of the following items before you configure a scan policy: A bucket can be specified only in one policy. Automatic detection is enabled only for newly added objects in OSS. | i. On the OSS Object Check tab, click Configure Policy. ii. In the Configure Policy panel, click the icon to enable automatic detection. iii. Configure the Check Cycle, Object Check Time, Object Check Type, and Effective Bucket parameters, and click OK. |

**View detection results**

View the overall information about at-risk OSS objects In the statistics section of the **At-risk File Overview** tab, you can view the following information: the total number of OSS objects that are checked, the number of objects at each risk level, and the remaining quota. The risk levels are high, medium, and low. View the details of at-risk files In the list of at-risk files of the At-risk File Overview tab, find the file whose details you want to view and click **Details** in the **Actions** column. In the details panel, view details of the file, such as Object Details and Event Description.

> **Note:** If risks are detected in a file, the file may be embedded with viruses such as malicious scripts and DDoS trojans. We recommend that you handle the file at the earliest opportunity based on the suggestions provided in the Event Description section.

View the statistics on OSS object detection In the statistics section of the **OSS File Check** tab, you can view the following information: the number of buckets in which malicious objects are detected, the number of objects at each risk level, and the total number of buckets. The risk levels are high, medium, and low. View the detection results of a bucket In the bucket list of the **OSS Object Check** tab, find the bucket whose detection results you want to view and click **Details** in the **Actions** column. On the Object Check Details page, you can view the information about the bucket in the Basic Information and At-risk Object Details sections.

#### 3.4.7 Use the core file monitoring feature

The core file monitoring feature monitors access to core files on servers in real time. The feature can monitor file operations such as access, modify, delete, and rename operations in real time and generate alerts when suspicious operations are detected. You can use the feature to check whether your core files are stolen or tampered with. This topic describes how to use the core file monitoring feature to monitor access to core files on servers.

**Important**

In multi-level organization mode, pay attention to the following items: Only an account that has level-1 organization permissions or global organization permissions can create, modify, or delete a rule.

> You can view the status of hosts within the permission scope by resource set.

**Limits**

The servers must run a kernel Linux version that is supported by the AliWebGuard file. For more information, see Website tamper-proofing.

**Step 1: Create a rule**

**Rule validation logic**

Before the core file monitoring feature works, you must create rules to specify the monitoring scope of server files. We recommend that you understand the rule validation logic before you create a rule. During the monitoring of access to files on a server, Server Guard generates an alert or allows a request only if the request matches **all** the following items in the rule that you specify: Process path File path File operation Server Guard preferentially matches requests against the rules in which the Handling Method parameter is set to Release. This type of rule is referred to as an allow rule. If a request does not match an allow rule, Server Guard matches the request against the rules in which the Handling Method parameter is set to Alert. This type of rule is referred to as an alert rule.

**Configuration suggestions and examples**

We recommend that you configure monitoring rules for core system files and important configuration files. Before you create a rule, you must determine the files to monitor and the scope of processes that are allowed to access the files. For core business files, you must configure an alert rule for all processes and multiple allow rules for allowed processes. This helps ensure that all access operations on the files are monitored and unnecessary alerts are not generated.

> **Important:** If you do not configure an alert rule for all processes, you cannot monitor the access operations performed by processes that are beyond the scope of the specified process path. All out-of-scope processes can bypass the monitoring of Server Guard.
> When you configure an allow rule, we recommend that you do not use a wildcard character to specify a process path. If you use a wildcard character to specify a process path, attackers can exploit the allow rule to access your server files after bypassing the monitoring of Server Guard.

For example, the path of the core files that you want to monitor is /etc/sysctl.conf, and the allowed process is systemd. To monitor the file path /etc/sysctl.conf, you must configure two rules. Rule 1: Set the Handling Method parameter to Alert, set the Process Path parameter to an asterisk ( `*` ), set the File Path parameter to `/etc/sysctl.conf` , and select all options for the File operation parameter. The asterisk (*) specifies all processes. Rule 2: Set the Handling Method parameter to Release, set the Process Path parameter to `/usr/lib/systemd/systemd` , set the File Path parameter to `/etc/sysctl.conf` , and select all options for the File operation parameter. If you want to monitor core files on multiple servers, you can specify the file paths on all servers in an alert rule and set the Process Path parameter to an asterisk (*). Then, configure multiple allow rules for different process paths that you want to allow on different servers.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. On the **Defense > Core File Monitoring** page, click the **Monitoring Rule** tab.
4. Click **New Rule**. In the New rule panel, configure the parameters and click **Determine**.

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the scaling rule. |

| Handling Method | Select an action for Server Guard to perform when the rule is hit. Valid values: Alert: Server Guard generates an alert and records an event. Release: Server Guard allows the request. Server Guard does not generate an alert or record an event. |
|---|---|
| Alert Severity | Select the severity for the alert that is generated when the rule is hit. |
| Rule status | Specify whether to enable the rule after the rule is created. You can enable a maximum of 100 rules. |
| Process path | Enter the path of the processes to monitor. You can use a wildcard character to specify a process path. For example, if you want to monitor the process path /usr/conf, you can enter */conf. You can also use an asterisk (*) to specify all processes. You can enter a process path that is 1 to 128 characters in length. You must separate multiple paths with line feeds. You can specify a maximum of 20 process paths in each rule. |
| File Path | Enter the path of the files to monitor. You can use a wildcard character to specify a file path. For example, if you want to monitor the file path /etc/nginx/nginx.conf, you can enter /etc/nginx/*. You can also use /* to specify all file paths. You can enter a file path that is 1 to 128 characters in length. You must separate multiple paths with line feeds. You can specify a maximum of 20 file paths in each rule. |
| File operation | Select the file operations that you want to monitor. |
| Rule Scope | Select the servers to which you want to apply the rule. In multi-level organization mode, you can filter servers by resource set when you select the By asset value. |

If you want to modify, delete, enable, or disable the rule after you create the rule, we recommend that you find the entry point in the Status or Actions column of the rule. The first time you enable a rule for a server, it requires up to 5 minutes for the rule to take effect. If you modify a rule, it requires up to 1 minute for the rule to take effect. After the rule takes effect, existing alerts and recorded events are not affected.

**Step 2: View and handle alerts**

1. On the **Core File Monitoring** page, click the **Alert Events** tab. Then, you can view the
alerts that are generated by Server Guard on file access.
2. Find the alert that you want to view and click **Details** in the Actions column to view the
details of file access.

|   | Note If a Python script is used to access a file, Server Guard cannot obtain detailed CLI information. If a Shell built-in command is used to access a file, Server Guard cannot obtain detailed CLI information. For example, if the command is echo "new content" >> /etc/nginx/nginx.conf , ["-bash"] is displayed as the collected CLI information on the alert details page. This is because the command is a Shell built-in command, which appends content to the nginx.conf file. Server Guard collects CLI information after Shell parsing and displays the collected CLI information in JSON arrays on the alert details page. The command that is displayed may be different from the original user-specified command. Example 1: A user-specified command is mkdir "1 2" , which is equivalent to the mkdir 1\ 2 command. Both the commands create a directory named 1 2. After Shell parsing, the user-specified command becomes mkdir and 1 2 , and the display result on the alert details page is ["mkdir", "1 2"] . Example 2: A user-specified command is rm -rf * . After Shell parsing, * is replaced by all files and subdirectories in the specified directory. In this example, Server Guard collects and displays the following CLI information: rm , -rf , and the list of all files and subdirectories in the current directory. |
|---|---|
|   | /etc/nginx/nginx.conf |

|   | 1 2 |
|---|---|
| ["mkdir", "1 2"] |   |

3. Check whether an abnormal event is recorded based on the details of file access.
The follow-up solution varies based on your check results. If an abnormal event is recorded, we recommend that you manually block the related processes and quarantine the related files after you confirm that your business is affected. If the event records normal file access, you can add the alert to the whitelist to handle the alert. If the event is considered not affecting your files and you do not need to add the alert to the whitelist, you can ignore the alert.
4. After you examine and handle the alert, find the alert and click **Handle** in the Actions
column. Then, select a handling method and click **OK**. Whitelist: After you add the alert to the whitelist, Server Guard automatically generates a whitelist rule that allows the behavior detected by the alert. If you select this option, you must configure the Whitelist Rule Name, Process Path, File Path, File operation, and Rule Scope parameters. Then, click **OK**. Ignore: If you ignore the alert, the status of the alert changes to Ignored. If the same alert is detected later, Server Guard generates a new alert. Handle manually: If you have handled the abnormal event, you can select this option.

**FAQ**

**What are the differences between web tamper proofing and**

**core file monitoring?**

Web tamper proofing is a different feature that Server Guard provides to protect files. Web tamper proofing and core file monitoring differ in the following items.

| Item | Website tamper-proofing | Core file monitoring |
|---|---|---|
| Scenario | You need to protect assets such as websites that are vulnerable to attacks and sensitive to file tampering. | You need to monitor access operations on core files to prevent content theft. You need to monitor the changes on important files to avoid file tampering. The changes include modify, delete, and rename operations. |
| Protection scope | The feature can protect most Linux and Windows servers. | The feature can protect most Linux servers. |
| Capability | The feature supports identification of abnormal file changes. The feature can also block the related processes or generate alerts. | The feature supports monitoring of abnormal access to files, including read, modify, and delete operations. The feature can also generate alerts. |

For more information about web tamper proofing, see Use the feature of web tamper proofing.

**If I enable both web tamper proofing and core file monitoring,**

**which feature preferentially takes effect?**

If web tamper proofing and core file monitoring are both enabled for a server, web tamper proofing preferentially takes effect. If Server Guard cannot match a request against the rules of web tamper proofing, Server Guard matches the request against the rules of core file monitoring. The process whitelist rules of web tamper proofing take effect only when the web tamper proofing feature works. The allow rules of core file monitoring take effect only when the core file monitoring feature works.

### 3.5 Log retrieval

#### 3.5.1 Log retrieval overview

Server Guard provides the log retrieval feature. You can use the feature to manage logs that are scattered in various systems of Apsara Stack in a centralized manner. This way, you can easily identify the causes of issues that occur on your servers. The log retrieval feature allows you to store logs for 180 days and query logs that are generated within 30 days.

**Features**

The log retrieval feature provides the following benefits:
**End-to-end log retrieval platform**: allows you to retrieve logs of various Apsara Stack
services over a unified interface and trace issues in an efficient manner.
**Log service-related software as a service (SaaS)**: allows you to query logs on all
servers in Apsara Stack without the need to install or deploy specific software. TB-level data retrieval: allows you to obtain full-text search results within several seconds. You can also add up to 50 Boolean expressions in a search condition. Support for various log sources. Log delivery: allows you to deliver security logs to Simple Log Service for further analysis. Advanced search: allows you to query and analyze logs on a server. The advanced search feature can be used only after you activate Simple Log Service.

**Scenarios**

You can use the log retrieval feature to meet the following requirements:
**Security event analysis**: When a security event is detected on a server, you can retrieve
the logs to identify the cause of the issue and assess the extent of the damage and affected assets.
**Operation audit**: You can audit the operation logs on a server to identify high-risk
operations and critical issues in a precise manner.

**Retrievable log types**

Table 1 Log sources

| Log source | Description |
|---|---|
| Logon history | Logs of successful system logons |
| Process snapshots | Logs of processes on a server at a specific point in time |
| Port listening snapshots | Logs of listening ports on a server at a specific point in time |
| Account snapshots | Logs of account-based logons on a server at a specific point in time |
| Process startups | Logs of process startups on a server |
| Network connections | Logs of outbound connections that are initiated from hosts |

#### 3.5.2 Query logs

This topic describes how to search for and view physical server logs.

**Quick search**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Log Retrieval**.
4. On the **Quick Search** tab, configure search conditions.

| Search condition | Description |
|---|---|
| Select a log source | The log source that you want to query. For more information, see Supported log sources and fields. |
| Select a field | The field that is recorded for the log source. For more information, see Supported log sources and fields. |
| Keywords | The keyword of the field. |
| Logical operator | Equal to or contained in the prefix. |
| + | You can click the plus sign to add expressions for a log source. |
| Time Range | The time range in which you want to query logs. |

5. Click **Search** and view the search result.
**Reset**: Click **Reset** to remove existing search conditions.
**Save Search**: Click **Save Search** to save a search condition, which can be used for
subsequent log searches.

> **Important:** The Save Search button is displayed only when at least one result is returned based on the search conditions.

**Saved Search Conditions**: Click **Saved Search Conditions** to select and use a search
condition that you saved.

**Advanced search**

**Important**

> The advanced search feature can be used only after you activate Simple Log Service. To activate Simple Log Service, contact the administrator.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Log Retrieval**.
4. On the **Advanced Search** tab, follow the on-screen instructions to search for logs.

#### 3.5.3 Supported log sources and fields

This topic describes the log sources and fields that are supported by the log retrieval feature. The log retrieval feature allows you to query the following types of log sources. You can click a log source link to view the fields that are supported.

| Log source | Description |
|---|---|
| Logon history | Logs of successful system logons |
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
| IP | string | The IP address. |
| pid | string | The ID of the process. |
| groupname | string | The user group. |
| ppid | string | The ID of the parent process. |
| uid | string | The ID of the user. |
| username | string | The username. |
| filename | string | The name of the process file. |

| pfilename | string | The name of the parent process file. |
|---|---|---|
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
|---|---|---|
| home dir _ | string | The home directory. |
| warn time _ | string | The time at which a password expiration notification is sent. |
| groups | string | The group to which the user belongs. |
| login ip _ | string | The IP address of the last logon. |
| last chg _ | string | The time at which the password was last changed. |
| shell | string | The Linux shell command. |
| domain | string | The domain in Windows. |
| tty | string | The terminal of the logon. |
| account expire _ | string | The time at which the account expires. |
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
| md5 | string | The MD5 hash value of the process file. If the size of the process file exceeds 1 MB, the system does not calculate the MD5 hash value of the process file. |

**Network connection logs**

The following table describes the fields that are supported in network connection logs.

| Field | Type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address. |
| src ip _ | string | The source IP address. |

| src port _ | string | The source port. |
|---|---|---|
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

#### 3.6.1 Install the Server Guard agent

If you want to monitor the security of assets in Server Guard, you must install the Security Center agent on your server. This topic describes how to install the Security Center agent by using Server Guard settings.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Setting** > **Settings**.
4. Click the **Agent** tab.
5. **Optional.** Click the **Client to be installed** tab to view the number of servers on which the
agent is not installed and the information about the servers. You can specify the operating system type, server IP address, or server name to search for a server.
6. Click the **Client Installation Guide** tab to install the Security Center agent.
CLI Installation

**Deploy Hosts in Apsara Stack**

a. On the **CLI Installation** tab, find the operating system of your server and click **Copy** on the right.

> **Note:** If you do not find the required installation command for the operating system of your server, click **Create Installation Command**, configure the **Organization**, **Resource Set**, and **Client Type** parameters, and then click OK. Then, click **Copy** on the right.

b. Run the command on your server. c. Click the **Installation Verification** tab to verify the command based on the operating system of the server.

**Deploy Hosts Outside Apsara Stack**

> **Important:** Before you install the Server Guard agent, make sure that you have a sufficient quota, and the domain name of the server is resolved to Server Guard. You can click **View Domain Name Resolution** or **View Quota** to view the required information.

a. Click **Manage Service Provider**. On the **Assets** page, click the **Server(s)** tab. b. On the tab that appears, click **Create Provider**, configure the **Provider Name** parameter, and then click **OK**. c. Go to the **Agent Installation** page. On the **Agent Installation Guide** tab, click **CLI**
**Installation**.
d. In the **Deploy Hosts Outside Apsara Stack** section, find the newly added service provider and click Create Installation Command. In the dialog box that appears, configure the **Client Type**, **Effective Duration**, **Region**, **Data Center**, and **Asset**
**Group** parameters.
In multi-organization mode, you must select the required **organization** and
**resource set**.
e. After the configuration is complete, click **Copy** and run the command on your server. f. Click the **Installation Verification** tab to verify the command based on the operating system of the server.

**Image Installation**

> **Important:** Before you install the Server Guard agent, make sure that your you have a sufficient quota, and the domain name of the server is resolved to Server Guard. You can click **View Domain Name Resolution** or **View Quota** to view the required information.

a. On the **Image Installation** tab, install the agent as prompted. b. Click the **Installation Verification** tab and copy the required command on this tab based on the operating system of the server to verify the installation result.

#### 3.6.2 Manage protection modes

This topic describes how to manage protection features and protection modes for each server to improve the efficiency and security of servers.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Setting** > **Settings**.
4. On the **Protection Capability Settings** tab of the **Settings** tab, configure the following
protection capabilities. In multi-level organization mode, servers can be filtered by resource set.

| Prote ction capab ility | Description | Operation |
|---|---|---|
| Proacti ve defens e | Malicious Host Behavior Prevention: The proactive defense feature can identify threats to processes, intelligently determine risk levels, and block high-level risks such as viruses, trojans, ransomware, mining programs, and DDoS trojans in real time. Anti-ransomware (Bait Capture): In this section, the anti-ransomware feature creates decoy data based on ransomware behavior patterns. The decoy data is not affected during normal process operations. If ransomware attempts to tamper with the decoy data, the anti- ransomware feature detects and immediately intercepts the tampering operation. The feature is supported only for Windows servers. Risk Monitoring on Data Restoration: In this section, Server Guard uses snapshots to restore cloud disk files that are encrypted by ransomware. If assets on which regular backup is not performed are attacked by ransomware, data restoration may be affected. If you want to modify the automatic snapshot policy, go to the Elastic Compute Service (ECS) console. If you want to view vulnerable assets, click Details to the right of Risk assets. Malicious Behavior Prevention: This feature blocks known malicious network behavior to improve the security of your assets. The feature is supported only for container firewalls. | Enable protection capabilities: Find the protection capability that you want to enable and click the icon next to the capability. Configure the protection scope: Find the protection capability that you want to manage and click Manage next to the protection scope. In the dialog box that appears, select the asset group and assets and then click Ok. |

| Websh ell detecti on and remov al | Server Guard scans the web directories of your servers for webshells. | Configure the protection scope: Find the protection capability that you want to manage and click Manage next to the protection scope. In the dialog box that appears, select the asset group and assets and then click Ok. |
|---|---|---|

5. On the **Protection mode management** tab, manage prevention modes.
In multi-level organization mode, servers can be filtered by resource set.

| Protection mode | Description | Operation |
|---|---|---|
| Prevention Mode Manageme nt | Basic Prevention Mode: This mode is suitable for scenarios in which basic protection is required. In this mode, the Server Guard agent consumes 50 MB of memory and less than 2% of one CPU core, and the agent automatically downgrades the security features that consume a large number of resources. However, threats may not be detected at the earliest opportunity. We recommend that you enable Advanced Prevention Mode. | N/A |
|   | Advanced Prevention Mode: This mode is suitable for scenarios in which critical workloads need to be protected. In this mode, the Server Guard agent can identify more types of suspicious intrusions and potential threats by using the big data analytics engine, machine learning engine, and deep learning engine. | Manage protected servers: In the Advanced Prevention Mode section, click Manage. In the Advanced Prevention Mode panel, select the servers that you want to protect and click OK. |

|   | Safeguard Mode For Major Activities: This mode is suitable for major event protection. In this mode, all protection rules and security engines are enabled to generate alerts for all suspicious intrusions and potential threats. | Manage protected servers: In the Safeguard Mode For Major Activities section, click Manage. In the Safeguard Mode For Major Activities panel, select the servers that you want to protect and click OK. Specify the maximum CPU utilization: In the Safeguard Mode For Major Activities section, select an option from the CPU Threshold drop-down list. Valid values: 5%, 10%, 20, 30%, 40%, 50%, and 60%. |
|---|---|---|
|   | After you enable the self-protection mode, the system automatically blocks activities that attempt to uninstall the Server Guard agent. This ensures the stability of the Server Guard agent. Note We recommend that you run important services in an operating system that supports the self- protection mode. This helps prevent the Server Guard agent from being uninstalled. If the Server Guard agent is uninstalled, the server is not protected, which can cause security risks. The system requires 30 minutes to disable the self-protection mode. | Manage protected servers: In the Self-protection Management section, click Manage. In the dialog box that appears, select the servers that you want to protect and click OK. Enable the self-protection mode: Click the icon to enable the self-protection mode. |
| Self- protection Manageme nt |   |   |

#### 3.6.3 Configure defense rules

The host-specific rule configuration feature allows you to manage defense and detection rules that are configured for your servers. You can create defense rules based on your business requirements to improve the security of your system.

**Scenarios**

Malicious behavior defense supports system defense rules and custom defense rules. The following table describes the scenarios for which the two types of rules are suitable.

| Rule type | Scenario |
|---|---|

| System defense rule | Common attacks are automatically blocked. You can disable a system defense rule or change the servers on which a system defense rule takes effect. |
|---|---|
| Custom defense rule | If you want to allow or block specific behavior, you can createc ustom defense rules based on your business scenarios. |

The high-risk command audit feature allows you to create custom audit rules.

**Malicious behavior defense**

**Manage system defense rules**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Settings** > **Rule Settings**.
4. On the **Defense Rules** tab of the **Malicious Behavior Defense** tab, search for and
manage a system defense rule. Search for a system defense rule Method 1: On the **Defense Rules** tab, enter the name of the system defense rule in the search box. Method 2: On the **Defense Rules** tab, select a value in the **Attack Phase** section to filter system defense rules. Manage a system defense rule Enable or disable a system defense rule: If a system defense rule is not suitable for your business scenario and affects the security score of your assets, you can disable the rule. a. Select one or more system defense rules based on your business requirements. b. In the lower-left corner of the system defense rule list, click **Enable** or **Disabled**. Manage servers on which a system defense rule takes effect

> **Note:** After you remove a server from a system defense rule, Server Guard no longer detects or reports risks on the server based on the rule.

a. Find a system defense rule and click**Management host** in the **Actions** column. b. In the **Management host** panel, add servers to the rule or remove servers from the rule. Then, click **OK**.

**Manage custom defense rules**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Settings** > **Rule Settings**.
4. On the **Custom Defense Rule** tab of the **Malicious Behavior Defense** tab, click **New**
**rule**.
5. In the **New rule** panel, configure the **Rule Type** parameter, the required parameters, and
the **Action** parameter based on your business requirements. Then, click **Next**. The required parameters vary based on the value of the Rule Type parameter. If you want to add specific behavior to the whitelist, make sure that the Rule Type parameter for the defense rule uses one of the following values:

> **Note:** You can add only the behavior of the Process hash type to the blacklist.

Process hash Command Line Process Network File Read and Write Operation on Registry Dynamic-link Library Loading File Renaming
6. In the server list of the **New rule** panel, select the servers on which you want the rule to
take effect and click **Finish**. By default, a newly created custom defense rule is enabled. You can modify the rule and manage the servers on which the rule takes effect.

**Audit of high-risk commands**

**Create and enable a custom audit rule**

**Important**

In multi-level organization mode, only an account that has permissions on the level-1 organization can create, modify, and delete rules.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.

**Note**

In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Settings** > **Rule Settings**.
4. On the **Audit of High-risk Commands** tab, click **New rule**.
5. In the **New rule** panel, configure the parameters and click **Next**.

| Paramet er | Description |
|---|---|
| Rule Name | The name of the rule. |
| Rule descriptio n | The description of the rule. |
| OS Type | The OS type. Valid values: Linux and Windows. |
| Process Path | The path to the process to which you want to apply the rule. The value of this parameter must be 5 to 100 characters in length. Wildcards are supported. If you use wildcards, the value must include the name of a specific process or subdirectory. Examples: /usr/bin/bash , */bash , /root/abc , c://cmd.exe , /cmd.exe , and C:/Windows/System32/cmd.exe . |

|   | */bash |
|---|---|
| C:/Windows/System32/cmd.exe |   |

| Command Line | The command line that you want to match by using the rule. The value of this parameter must be 1 to 100 characters in length. We recommend that you use wildcards. If you use wildcards, the value must include characters. Examples: *C:\Users\Administrator* , *id* , and *python* . You can also use regular expressions to match high-risk commands. Enter a command line and click Test on the right. In the dialog box that appears,t he Matching Mode field displays the command line. Enter a command that you want to test against the specified command line and click Test. If the test is successful, the dialog box is automatically closed. |
|---|---|
| Threat Level | The severity level of the command that hits the rule. Valid values:C ritical, Warning, and Notice. |

6. Select the assets to which the rule applies and click **OK**.
If you want to apply the rule to subsequently added servers, select **Apply to Newly Added**
**Servers**.
7. After you create the rule, find the rule in the rule list and click the
icon in the **Switch** column to enable the rule. The rule can be in one of the following states: Running: The rule is in effect. Disabled: The rule does not take effect. Silent Running: If the upper limit for the Triggers parameter within the specified period of time is exceeded, the rule enters the Silent Running state, and no alerts are generated. The rule does not take effect until the next cycle. To modify the Triggers parameter, log on to the Apsara Uni-manager Management Console and go to the Global Settings module of Server Guard.

**View audit alerts**

1. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
2. In the upper part of the alert list, select **Command Line Audit** as the alert type to view the
alerts named **Suspicious Command Lines** and the alert details.

## 4 System configuration

### 4.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ %
> **Forget password**
> If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging on to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For information about how to enable MFA and bind an MFA device, see Manage MFA.

### 4.2 Rules

#### 4.2.1 Manage Anti-DDoS Service rules

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
ii. In the **Modify Threshold** dialog box, specify custom thresholds and click **OK**. iii. **Optional.** Click **Automatic DDoS Traffic Redirection and Scrubbing**. In the **Enable**
**Automatic Redirection** message, click **OK**.

> **Note:** By default, **Automatic DDoS Traffic Redirection and Scrubbing** is turned off.

If you turn on Automatic DDoS Traffic Redirection and Scrubbing, traffic scrubbing events are triggered based on custom thresholds. The traffic of attacked IP addresses is automatically forwarded to an Anti-DDoS cluster for scrubbing. If you turn off Automatic DDoS Traffic Redirection and Scrubbing, alert events are triggered based on custom thresholds. You can start or end traffic scrubbing in the Anti-DDoS Service console based on your business requirements.

#### 4.2.2 Manage Server Guard rules

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
| Baselines (marked 2 in the preceding figure) | On the Baselines tab, you can view the baseline types and check the items that are used. To search for a baseline, you can select a baseline type from the Baseline Type drop-down list, select a severity from the Risk Level drop-down list, and enter a check item category or name in the search box. In the baseline list, you can view the following information about a baseline: Baseline Type, Check Item Category, Check Item Name, Risk Level, Updated At, and Status. |

| Server Exceptions (marked 2 in the preceding figure) | On the Server Exceptions tab, you can view the following information: Rule Alert Types and Webshell & Malicious Processes. To search for an exception on a server, you can select a rule category from the Rule Category drop-down list, select a severity level from the Risk Level drop-down list, and then enter a rule subcategory name in the search box. In the server exception list, you can view the following information: Rule Subcategory, Rule Category, Risk Level, Updated At, Source, and Status. |
|---|---|

#### 4.2.3 Create and manage WAF rules

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
| Severity | The level of the severity. Valid values: No Threat, Low, Moderate, and Important. |
| Match Condition | The match condition of the rule. Each match condition consists of am atch field, a logical operator, and a match value. |

| Logging | Specifies whether to record logs. Valid values: Perform Logging When Match Condition Is Met and Do not Perform Logging When Match Condition Is Met. |
|---|---|
| Attack Type | The type of attacks that you want the rule to detect. You can select only one option. |
| Blocking Status Code | The status code that is returned. You can select only one option. |
| Expire At | The expiration time of the rule. If you do not specify an expiration time, the rule never expires. |

After you create a rule, you can perform the following operations on the rule: Configure search conditions to filter WAF rules. Find the rule and click **Modify** in the **Actions** column to modify the information about the rule.

#### 4.2.4 Create and manage IPS rules

Cloud Firewall provides built-in intrusion prevention system (IPS) rules. You can create custom IPS rules based on your business requirements and network environment to monitor the operations of Cloud Firewall. This topic describes how to create and manage custom IPS rules.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
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
|---|---|
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability that you want to list in the IPS rule. Note CVE provides a list of public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Application | The name of the attacked application. |
| Rule Mode | The mode of the IPS rule. Valid values: Packet and Traffic. |
| Direction | The direction of traffic that you want to monitor by using the IPS rule. Valid values: Inbound and Outbound, Inbound, and Outbound. |
| Rule Content | The content of the IPS rule. You must specify the content by using the Snort syntax. Note To prevent negative impact on your business, make sure that you enter valid content for the rule. |
| Rule Description | The description of the IPS rule. We recommend that you enter information such as the purpose or impact of the rule. |
| Description | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |

After you create a custom IPS rule, you can perform the following operations on the rule: View the details of the rule You can filter rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details. Enable the rule Find the rule that you want to enable and turn on the switch in the **Enable or not** column to change the status of the rule from **Disable** to **Enable**. Disable the rule If a rule does not meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Enable or not** column to change the status of the rule from **Enable** to **Disable**.

### 4.3 Configure alert settings

On the Alert Settings page, you can configure alert contacts and alert rules. When monitoring data meets the conditions of an alert rule, the system automatically sends an alert to specified alert contacts by email and DingTalk message. This topic describes how to configure alert contacts and alert rules.

**Configure alert contacts**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. On the **Alert Settings** tab, click **Create Contact**. In the dialog box that appears, configure
the Contact Name, DingTalk Chatbot Token, and Email parameters, and click **Determine**. You can view the added contact in the contact list. You can **modify** a contact or **delete** multiple contacts at a time.

**Configure alert rules**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. Click the **AEGIS** tab, configure alert rules, and then click **Save**.

| Alert type | Alert subtype | Alert level | Notificati on method | Frequenc y |
|---|---|---|---|---|
| Vulnerability | Linux software vulnerability Windows system vulnerability Web-CMS vulnerability Application vulnerability Urgent vulnerability | Low Medium High |   |   |
| Baseline risk | High-risk exploit MLPS compliance Best security practices Weak password | Low Medium High |   |   |

|   |   |   |   | 5 minutes |
|---|---|---|---|---|
| Asset exposure | Vulnerability Non-vulnerability | All levels |   |   |
| Intrusion alert | Suspicious process Webshell Unusual logon Exception Threat intelligence Malicious process Unusual network connection Abnormal account Application intrusion event Cloud threat detection Precision defense Malicious script Persistent webshell Application threat detection | Low Medium High |   |   |
|   |   |   | Email DingTal k messag e | 10 minutes 30 minutes 1 hour 1 day 1 week |
| Application whitelist event | Unauthorized process start | All levels |   |   |
| Tampering | File modification File addition File deletion | All levels |   |   |

### 4.4 Global configuration

#### 4.4.1 Configure the attack blocking feature

The attack blocking feature protects your servers from web attacks. This topic describes how to configure the attack blocking feature.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
4. On the **Global Settings** tab, turn on or off the switch in the Actions column to enable or
disable the attack blocking feature. After you disable the attack blocking feature, Server Guard generates alerts for web attacks but does not block them.

### 4.5 Cloud Firewall monitoring

You can use the Cloud Firewall monitoring feature to monitor the status of Cloud Firewall, detect abnormal traffic, and handle abnormal events at the earliest opportunity. This topic describes how to perform system inspection and service monitoring.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Cloud Firewall Monitoring**.
4. In the **System Inspection** section, click **One-click Inspection**.
After the inspection is complete, you can perform the following operations: Click **Details** in the **Actions** column of **Internet Firewall (ICFW)**, **VPC Firewall**
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

After the configuration is complete, you can view the automatic check frequency for the CIDR block and the self-check result of each cluster in the **Service Check Status** and **Interface Status** sections.

**Note**

In each section, you can select a check frequency from the**automatic check** drop-down list to specify an automatic check frequency for the CIDR block. You can

> icon to manually refresh the check frequency for the CIDR block.

also click the b. In the**Connectivity Check**section, click**Add**. Configure the parameters and click **OK**.

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

### 4.6 Account management

#### 4.6.1 Manage Apsara Stack tenant accounts

This topic describes how to view and modify the information about your Apsara Stack tenant account.

> **Important:** All assets in Apsara Stack Security are bound to your Apsara Stack tenant account. You can modify the account information. Proceed with caution.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Apsara Stack Account** tab, modify the information about your Apsara Stack
tenant account. i. Find your Apsara Stack tenant account and click **Revised** in the **Operation** column. ii. In the **Change Account** dialog box, modify Apsara Stack Account, Access Key, and Access Secret, and click **OK**. After the modification, you can click Details in the **Operation** column to view the details of the Apsara Stack tenant account.

#### 4.6.2 Manage Alibaba Cloud accounts

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
