---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Scanner User Guide 20250612"
product_version: "V3.18.3"
doc_version: "20250612"
pdf_pages: 16
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Scanner User Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F-%E9%BB%98%E5%AE%89/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Scanner%20User%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Scanner User Guide 20250612

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
  - 2.3 Quick start
- 3 Apsara Stack Security configurations
  - 3.1 Log on to the Apsara Uni-manager Management Console
  - 3.2 Rules
    - 3.2.1 Create and manage IPS rules
    - 3.2.2 Manage Anti-DDoS Service rules
    - 3.2.3 Manage Server Guard rules
    - 3.2.4 Create and manage WAF rules
  - 3.3 Global configuration
    - 3.3.1 Configure the attack blocking feature
  - 3.4 Account management
    - 3.4.1 Manage Apsara Stack tenant accounts
    - 3.4.2 Manage Alibaba Cloud accounts

## 1 Usage notes

Before you log on to Apsara Stack Security Center, you must verify that your computer meets the configuration requirements. For more information about the configuration requirements, see . Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

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

### 2.3 Quick start

This topic describes how to get started with the vulnerability scan feature. The following procedure shows how to use the vulnerability scan feature:
1. Configure the following detection items and the required cycles based on your environment
requirements: Overall Monitoring: Configure detection features and the monitoring cycle of each detection feature. For more information, see Configure overall monitoring. Basic Monitoring: Configure Weak Password Vulnerability Monitoring, Operation Security Vulnerability Monitoring, CMS Application Vulnerability Monitoring, and Baseline Monitoring. For more information, see Configure basic monitoring. Web Monitoring: Configure the monitoring cycle and the types of web vulnerabilities that you want to monitor. For more information, see Configure web monitoring. Whitelist: Add the assets that do not require detection to the whitelist. For more information, see Configure a whitelist.
2. Import assets that require vulnerability scans.
Import internal assets: Configure a scan engine to import your internal assets in virtual private clouds (VPCs). For more information, see Configure a scan engine for internal assets. Import Internet assets: Import your Internet assets. For more information, see Import assets.

> **Note:** The number of imported assets cannot exceed the specified upper limit.

3. View and confirm the results of vulnerability scans.
View the overall information to obtain the results of vulnerability scans. For more information, see View the information on the Overview page. View and confirm vulnerability risks. For more information, see Manage vulnerabilities. View and confirm host compliance risks. For more information, see Manage host compliance risks.
4. Generate vulnerability scan reports.
Generate reports to audit the vulnerabilities and baseline risks on assets on a regular basis. For more information, see Create a report.

## 3 Apsara Stack Security configurations

**configurations**

### 3.1 Log on to the Apsara Uni-manager Management Console

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

### 3.2 Rules

#### 3.2.1 Create and manage IPS rules

Cloud Firewall provides built-in intrusion prevention system (IPS) rules. You can create custom IPS rules based on your business requirements and network environment to monitor the operations of Cloud Firewall. This topic describes how to create and manage custom IPS rules.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
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
|---|---|
| Rule Description | The description of the IPS rule. We recommend that you enter information such as the purpose or impact of the rule. |
| Description | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |

After you create a custom IPS rule, you can perform the following operations on the rule: View the details of the rule You can filter rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details. Enable the rule Find the rule that you want to enable and turn on the switch in the **Enable or not** column to change the status of the rule from **Disable** to **Enable**. Disable the rule If a rule does not meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Enable or not** column to change the status of the rule from **Enable** to **Disable**.

#### 3.2.2 Manage Anti-DDoS Service rules

On the Anti-DDoS Service rules page, you can modify threshold settings for traffic scrubbing and redirection based on your business requirements. This topic describes how to modify threshold settings for traffic scrubbing and redirection.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
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

#### 3.2.3 Manage Server Guard rules

You can view vulnerabilities, baselines, and server exceptions on the Server Guard Rules tab. This topic describes how to view the information about Server Guard rules.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Server Guard Rules** tab, view the information about Server Guard rules.

| Item | Description |
|---|---|
| Overview (marked 1 in the preceding figure) | You can view the following information: Total Vulnerability Detection Rules, Total Baseline Check Items, Total Host Exception Detection Rules, and Engines. |

| Vulnerabilities (marked 2 in the preceding figure) | On the Vulnerabilities tab, you can view all detected vulnerabilities and the total number of detected vulnerabilities. To search for a vulnerability, you can select a vulnerability type from the Vulnerability Type drop-down list and enter a Common Vulnerabilities and Exposures (CVE) ID or operating system (OS) name in the search box. In the vulnerability list, you can view the following information about a detected vulnerability: Vulnerability Name, CVE ID, Vulnerability Type, OS, Updated At, and Status. |
|---|---|
| Baselines (marked 2 in the preceding figure) | On the Baselines tab, you can view the baseline types and check the items that are used. To search for a baseline, you can select a baseline type from the Baseline Type drop-down list, select a severity from the Risk Level drop-down list, and enter a check item category or name in the search box. In the baseline list, you can view the following information about a baseline: Baseline Type, Check Item Category, Check Item Name, Risk Level, Updated At, and Status. |
| Server Exceptions (marked 2 in the preceding figure) | On the Server Exceptions tab, you can view the following information: Rule Alert Types and Webshell & Malicious Processes. To search for an exception on a server, you can select a rule category from the Rule Category drop-down list, select a severity level from the Risk Level drop-down list, and then enter a rule subcategory name in the search box. In the server exception list, you can view the following information: Rule Subcategory, Rule Category, Risk Level, Updated At, Source, and Status. |

#### 3.2.4 Create and manage WAF rules

You can create custom Web Application Firewall (WAF) rules based on your business requirements and network environment to monitor the operations of WAF. This topic describes how to create and manage WAF rules.

> **Important:** WAF rules are global custom rules that take effect on all tenants. Proceed with caution.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **WAF Rules** tab, click **Create Rule**. Configure the parameters and click **OK**.

| Parameter | Description |
|---|---|

| Mode | The handling action and status of the rule. You can set the handling action to Block, Allow, Monitor, or Detection Module Control. You can set the status to Enable or Disable. |
|---|---|
| Description | The description of the rule. |
| Severity | The level of the severity. Valid values: No Threat, Low, Moderate, and Important. |
| Match Condition | The match condition of the rule. Each match condition consists of am atch field, a logical operator, and a match value. |
| Logging | Specifies whether to record logs. Valid values: Perform Logging When Match Condition Is Met and Do not Perform Logging When Match Condition Is Met. |
| Attack Type | The type of attacks that you want the rule to detect. You can select only one value. |
| Blocking Status Code | The status code that is returned. You can select only one value. |
| Expire At | The expiration time of the rule. If you do not specify an expiration time, the rule never expires. |

After you create a rule, you can perform the following operations on the rule: Filter the WAF rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details.

### 3.3 Global configuration

#### 3.3.1 Configure the attack blocking feature

The attack blocking feature protects your servers from web attacks. This topic describes how to configure the attack blocking feature.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
3. In the left-side navigation pane, click **Global Settings**.
4. On the **Global Settings** tab, turn on or off the switch in the Actions column to enable or
disable the attack blocking feature. After you disable the attack blocking feature, Server Guard generates alerts for web attacks but does not block them.

### 3.4 Account management

#### 3.4.1 Manage Apsara Stack tenant accounts

This topic describes how to view and modify the information about your Apsara Stack tenant account.

> **Important:** All assets in Apsara Stack Security are bound to your Apsara Stack tenant account. You can modify the account information. Proceed with caution.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
3. In the left-side navigation pane, click **Accounts**.
4. On the **Apsara Stack Account** tab, modify the information about your Apsara Stack
tenant account. i. Find your Apsara Stack tenant account and click **Revised** in the **Operation** column. ii. In the **Change Account** dialog box, modify Apsara Stack Account, Access Key, and Access Secret, and click **OK**. After the modification, you can click Details in the **Operation** column to view the details of the Apsara Stack tenant account.

#### 3.4.2 Manage Alibaba Cloud accounts

After you add an Alibaba Cloud account to Apsara Stack Security Center, you can manage the Anti-DDoS Pro, Anti-DDoS Premium, and Web Application Firewall (WAF) instances that belong to the Alibaba Cloud account in Apsara Stack Security Center. This way, you can use features in a hybrid cloud. This topic describes how to add an Alibaba Cloud account to Apsara Stack Security Center. To use features in a hybrid cloud, you can add an Alibaba Cloud account to Apsara Stack Security Center.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
3. In the left-side navigation pane, click **Accounts**.
4. On the **Alibaba Cloud Account** tab, click **Add**.
i.

| Parameter | Description |
|---|---|
| Access Key | The AccessKey ID of the Alibaba Cloud account that you want to add. |
| Access Secret | The AccessKey secret of the Alibaba Cloud account. |
| Alibaba Cloud Service | The Alibaba Cloud services that you want to use. Valid values:A nti- DDoS Pro and Anti-DDoS Premium IP and Web Application Protection. You can select one value or both. |

After the Alibaba Cloud account is added, you can view the account in the account list. You can **modify** or **remove** the account.
