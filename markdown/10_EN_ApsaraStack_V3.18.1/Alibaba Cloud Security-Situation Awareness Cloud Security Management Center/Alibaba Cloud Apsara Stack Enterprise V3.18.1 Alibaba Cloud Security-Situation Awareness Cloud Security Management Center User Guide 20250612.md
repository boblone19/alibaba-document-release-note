---
title: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20250612"
product_version: "V3.18.1"
doc_version: "20250612"
pdf_pages: 71
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3.18.1%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%80%81%E5%8A%BF%E6%84%9F%E7%9F%A5/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.18.1%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20User%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20250612

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 Security Operations Center (SOC)
  - 3.1 Threat monitoring
  - 3.2 Use the Operations Center module
  - 3.3 Use the Risk Analysis module
    - 3.3.1 View threat events
    - 3.3.2 View threat investigation results
    - 3.3.3 View vulnerability analysis results
    - 3.3.4 View cloud service check data
    - 3.3.5 View attack surface assessment results
    - 3.3.6 View traffic analysis results
  - 3.4 Use the Tasks module
  - 3.5 Asset Management
    - 3.5.1 View tenant assets
    - 3.5.2 View platform assets
  - 3.6 Use the Logs module
    - 3.6.1 View the information on the Overview page
    - 3.6.2 Query log details
    - 3.6.3 Query raw logs
    - 3.6.4 View platform logs
    - 3.6.5 View tenant logs
    - 3.6.6 Log configurations
      - 3.6.6.1 Manage log sources
      - 3.6.6.2 Configure a log parsing template
      - 3.6.6.3 Configure log forwarding
  - 3.7 Use the Reports module
  - 3.8 Use the Rules module
    - 3.8.1 Create an analysis rule
    - 3.8.2 Alert rules
    - 3.8.3 Create a blocking rule
  - 3.9 Use the Operations module
    - 3.9.1 Configure the log storage policy
    - 3.9.2 Add custom IP addresses and modify the SOC location configuration
    - 3.9.3 Manage organization authorization
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

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. We recommend that you use Google Chrome.
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

## 3 Security Operations Center (SOC)

**(SOC)**

### 3.1 Threat monitoring

Security administrators can use the threat monitoring feature to understand the overall security of a network. This topic describes how to use the threat monitoring feature.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, **Threat Monitoring**.
4. In the upper-right corner of the **Threat Monitoring** page, select values from the drop-
down lists to view the required network security information. You can select **All Platform and Organizations**, **All Organizations**, **Platform**, or
**Organization** from the drop-down list on the left.
You can select **Today**, **Last 24 Hours**, **Last 7 Days**, or **Last 30 Days** from the dropdown list on the right.
5. View the overall network security information within a specified time range.

| Section | Description |
|---|---|
| Global Security Situation | This section displays the statistics on security risks from the perspective of global security management. The following list describes the modules in this section: Total Organizations: displays the number of organizations in the current cloud environment. If you select Platform or Organization from the drop- down list on the left, the total number of organizations is 1. Risk Index: displays the statistics on global risk indicators based on threat events and at-risk assets within an organization. Trend of Risk Indexes: displays the trend of risk indicators within a specified time range. The trends of risk indicators within the current day and last day are calculated by hour. The trends of risk indicators within the last 7 days and last 30 days are calculated by day. Organization Risks: displays the statistics on top 5 at-risk organizations, assets of top 5 at-risk organizations, and threat events of top 5 at-risk organizations. Asset Information: displays the total number of assets, the asset protection rate, and the proportions of high-risk, medium-risk, low-risk, and risk-free assets. Threat Events: displays the total number of threat events and the number of threat events at each risk level. The information about external risk sources and attack sources is displayed on maps. The world map and China map are supported. |

| Asset Risk Situation | The following list describes the statistics on the asset risk situation from the perspective of asset risk management: Asset Distribution by Risk Level: displays the distribution of assets at the following levels: high, medium, low, and risk-free. Trend of Asset Risks: displays the trend in the number of at-risk assets. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Top 5 Security Vulnerability Risks: displays the top 5 asset vulnerabilities. Top 5 Security Baseline Risks: displays the top 5 asset baseline risks. Top 5 At-risk Assets: displays the top 5 at-risk assets, including the risk indicators, threat events, network attacks, suspicious behaviors, security vulnerabilities, and security baselines of the assets. |
|---|---|
| Threat Situation | The following list describes the statistics on the threat event situation from the perspective of threat event management: Threat Event Distribution by Level: displays the distribution and statistics of threat events at the following severity levels: emergency, serious, suspicious, moderate, and information. Trend of Threat Events: displays the trend in the number of threat events. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Threat Event Distribution by Type: displays the distribution and statistics of threat events in the following types: exception, malware, unauthorized privilege escalation, vulnerability exploitation, and risk connection. ATT&CK Attack Behavior: displays the statistics on ATT&CK involved in threat events. Top 10 Threat Events: displays the number of times that the top 10 threat events are detected. Threat Event Distribution by Attack Chain: displays the attack phases involved in threat events and the number of times that the threat events are detected. Attack phases include payload delivery, vulnerability exploitation, webshell insertion, command control, scan extension, privilege escalation, and target attack. |

### 3.2 Use the Operations Center module

**module**

The Operations Center module provides the security alert data of security services provided by Apsara Stack Security. The Operations Center page provides the Network Risk View and Host Risk View tabs. Security administrators can use the module to obtain information about network attacks and defenses. This helps improve network security. This topic describes how to view data in the Operations Center module.

**View data in the network risk view**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. On the **Network Risk View** tab, view the following data.

| Section | Description |
|---|---|
| Statistics window selection (marked 1 in the preceding figure) | In this section, you can specify the types of data that you want to view on the Operations Center page. You can perform the following operations: Select statistics windows: Click Select Statistics Window and select the types of data that you want to view. By default, the following options are selected: Alert data, Distribution of Alert Handling Methods, ECS Instance Protection, Risk Level, Distribution of Alerting Data Sources, Distribution of Alert Types, Top 10 Attacking IP Addresses, Top 10 Attacked IP Addresses, Top 5 Attacked Websites, and List display area. Save view: Click the icon to save the current view. Manually refresh data: Click the icon to manually refresh the data in the current view. Enable automatic refresh: Turn on . The system automatically refreshes the data in the current view every 5 minutes. Export data: Click the icon to export the data in the current view. |
| Search condition (marked 2 in the preceding figure) | In this section, you can specify search conditions to query data. You can specify search conditions such as the time range, data source, query scope, alert type, risk level, attack source, alerting asset, alert source IP address, alert destination IP address, and alert name based on your business requirements. |
| Search result (marked 3 in the preceding figure) | In this section, Security Operations Center (SOC) displays the search results that meet the specified data types and search conditions. |

| List (marked 4 in the preceding figure) | In this section, SOC displays the details of threats in a list based on the data types and search conditions that you specify. The details include the occurrence time, attack source, alert name, alert type, risk level, and data source. You can also perform the following operations to manage the details of threats: Configure the data display mode. Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the data that has the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. Click Details in the Actions column of an alert to go to theD etails panel to view the details of the alert. Click the icon to refresh the data in the list. Click the icon to configure the items that you want to view in the list. By default, all items are selected and displayed in the list. |
|---|---|

**View data in the host risk view**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. On the **Host Risk View** tab, view the following data.

| Section | Description |
|---|---|
| Statistics window selection (marked 1 in the preceding figure) | In this section, you can specify the types of data that you want to view on the Operations Center page. You can perform the following operations: Select statistics windows: Click Select Statistics Window and select the types of data that you want to view. By default, the following options are selected: Alert data, ECS Instance Protection, Risk Level, Distribution of Alert Types, Top 10 Attacked IP Addresses, and List display area. Save view: Click the icon to save the current view. Manually refresh data: Click the icon to manually refresh the data in the current view. Enable automatic refresh: Turn on . The system automatically refreshes the data in the current view every 5 minutes. Export data: Click the icon to export the data in the current view. |
| Search condition (marked 2 in the preceding figure) | In this section, you can specify search conditions to query data. You can specify search conditions such as the time range, handling status, data source, query scope, alert type, risk level, attack source, alerting asset, alert source IP address, alert destination IP address, and alert name based on your business requirements. The data source is fixed as Sever Guard. |
| Search result (marked 3 in the preceding figure) | In this section, SOC displays the search results that meet the specified data types and search conditions. |

| List (marked 4 in the preceding figure) | In this section, SOC displays the details of threats in a list based on the data types and search conditions that you specify. The details include the occurrence time, attack source IP address, alert name, alert type, risk level, and data source. You can also perform the following operations to manage the details of threats: Configure the data display mode. Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the data that has the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. Click Details in the Actions column of an alert to go to theD etails panel to view the details of the alert. Click the icon to refresh the data in the list. Click the icon to configure the items that you want to view in the list. By default, all items are selected and displayed in the list. |
|---|---|

**Create a custom view**

By default, the Operations Center page provides the Network Risk View and Host Risk View tabs. You can also create a custom view.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. In the upper-right corner of the **Operations Center** page, click **Select Statistics**
**Window**, select the types of data to be displayed in the custom view, and then click the
icon.
5. In the **Save current view** dialog box, enter a view name and click **Save**.
The view name can be up to 16 characters in length.

### 3.3 Use the Risk Analysis module

#### 3.3.1 View threat events

This topic describes how to view threat events. Security administrators can obtain threat details based on these events and ensure network security.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Threat Events**.
4. On the **Threat Events** page, view the details of the threat events.

| Section | Description | Supported operation |
|---|---|---|
| Search condition (marked 1 in the preceding figure) | In this section, you can specify search conditions for threat events. You can specify the query time, scope, threat level, threat type, attack phase, and threat name to search for threat events. | Select values from drop-down lists or enter keywords, and click the icon. If you do not specify search conditions, all threat events are automatically displayed. |
| Search result (marked 2 in the preceding figure) | The search result section displays the information about threat events that meet the specified search conditions. | Click the name of a threat event or click Details in the Actions column of a threat event. On the details page of the threat event, view the information on the Threat Details and Evidence Details tabs. |

On the **Threat Details** tab, view the values of the following parameters: **Start Time**, **Last**
**Detected At**, **Analytic Rules**, **Network Protocol**, **Threat Intelligence**, **Source**
**Information**, **Target Details**, and **Key Information**.
Click the rule ID next to **Analytic Rules** to view more information about the rule that detects the threat. Click **Generate Response Event** to generate a case for the current threat event on the
**Case Management** page of the **Security Orchestration, Automation, and**
**Response (SOAR)** console. This helps monitor and handle this threat event.
On the **Evidence Details** tab, view the raw logs of the threat event.

#### 3.3.2 View threat investigation results

The threat investigation feature allows you to perform comprehensive threat investigations based on IP addresses, asset names, and asset IDs. This topic describes how to use the threat investigation feature.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Threat Investigation**.
4. On the **Threat Investigation** page, select a time range, enter the IP address, name, or ID
of the asset whose threat information you want to query, and then click the icon. For assets whose threat information is frequently queried, you can create shortcuts for the assets by performing the following steps: Click **Add Shortcut**. In the dialog box that appears, configure the **Type** and **Content** parameters. This way, you can view the threat investigation results of these assets in a quicker manner. After you create a shortcut, you can click the corresponding icon to view the threat investigation results of an asset. image
5. On the page that appears, view the risk items.
The modules displayed vary based on the asset. The modules displayed on the console shall prevail. The following list describes the common modules: Asset Details: displays the network topology and asset fingerprints of the asset. The asset fingerprints include ports, software, processes, accounts, middleware, and startup items. Suspicious Process: displays statistics on the suspicious processes in the asset in the form of charts and tables. The statistics include the total number of suspicious processes, suspicious process distribution by level, suspicious process distribution by type, and the top five suspicious processes. Network Attack: displays statistics on the network attacks on the asset in the form of charts and tables. The statistics include the total number of network attacks, distribution of network attack data sources, distribution of network attack types, and the top five network attacks. Vulnerabilities: displays statistics on the vulnerabilities in the asset and the failed baseline check items for the asset in the form of lists. Attack Surface: displays the attack paths of attacks that the asset has suffered.

#### 3.3.3 View vulnerability analysis results

This topic describes how to view vulnerability analysis results on the platform side and the tenant side. Security administrators can use the results to troubleshoot issues.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Vulnerability Analytics**.
4. On the **Platform** or **Tenant** tab of the page that appears, view the vulnerabilities and
baselines.

**Vulnerabilities**

On the Vulnerabilities tab, you can view the following information: vulnerability name, vulnerability type, vulnerability level, CVE ID, affected assets, priority, the time when the risk was detected, and the organization in which the risk exists. You can specify search conditions to search for vulnerabilities.

> **Note:** If you do not specify search conditions, all vulnerabilities are displayed by default.

| Search condition | Description |
|---|---|
| Scope | The organization whose risks you want to query. Note This search condition is available only on the Tenant tab. |
| Time range | The time range to query. Valid values: Today, Last 24 Hours, Last 7 Days, Last 30 Days, and Custom. |
| Vulnerability type | The type of the vulnerabilities. Valid values: All, Linux Software, Windows System, Web CMS, and Application (Urgent Vulnerability Included). |
| Vulnerability level | The severity of the vulnerabilities. Valid values: All, High, Medium, and Low. |
| Priority | The priority of the vulnerabilities. Valid values: All, High, Medium, and Low. |
| Vulnerability name | The keyword that is used to search for vulnerabilities. The keyword can be a vulnerability name or a Common Vulnerabilities and Exposure (CVE) ID. Fuzzy match is supported. |

All search results are displayed in the vulnerability list. You can perform the following operations based on your business requirements: Click the icon to refresh the vulnerability list. Click the icon to export the vulnerability list. Click the name of a vulnerability or click **Details** in the **Actions** column of a vulnerability to view the vulnerability details and affected assets. In the **Scanned**
**Asset** section of the vulnerability details panel, click **Details** in the Actions column of
an asset to view the asset details.

**Baselines**

On the Baselines tab, you can view the following information: baseline name, risk type, risk level, affected asset, the time when the risk was last detected, and the organization in which the risk exists. You can specify search conditions to search for baselines.

> **Note:** If you do not specify search conditions, all baselines are displayed by default.

| Search condition | Description |
|---|---|
| Scope | The organization whose risks you want to query. Note This search condition is available only on the Tenant tab. |
| Time range | The time range to query. Valid values: Today, Last 24 Hours, Last 7 Days, Last 30 Days, and Custom. |
| Risk type | The risk type of the baselines. Valid values: hierarchy protection Unauthorized Access Internationally Agreed Best Practices for Security Custom baseline Best security practices Weak password Container security Data Security Access Control Monitoring Alarms Disaster Recovery Backup Log Audit Authentication Security Network Configuration |
| Risk level | The severity of the baselines. Valid values: All, High, Medium, and Low. |
| Baseline name | The name of the baseline. |

All search results are displayed in the baseline list. You can perform the following operations based on your business requirements: Click the icon to refresh the baseline list. Click the icon to export the baseline list. Click the name of a baseline or click **Details** in the **Actions** column of a baseline to view the baseline details, including the baseline description and affected cloud service instances.

#### 3.3.4 View cloud service check data

You can use built-in security baselines to check and manage the security compliance of Apsara Stack services. This topic describes how to perform a cloud service check and view check data.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis** > **Cloud Service Check**.
4. In the upper-right corner of the **Cloud Service Check** page, click **Select Organization or**
**Resource Set**. Select one or more organizations that you want to check and click **OK**.
5. On the **Cloud Service Check** page, view information about the baselines of cloud services.
The information includes baseline risk items, affected assets, enabled baseline check items, disabled baseline check items, and the time when the check was last performed.
6. Perform a cloud service check.
Manual check Click **Check now**. The system starts a full check on the configurations of all services to detect risks and affected assets. During the check, you can click **View** to view the check progress in the **Check Item Detection** dialog box.

> **Note:** Do not perform other operations until the check is complete.

Automatic check Click **Check Settings** to configure a check policy. The following table describes the required parameters.

| Parameter | Description |
|---|---|
| Check Cycle | The days of the week on which you want to run an automatic check. Valid values range from Monday to Sunday. You can select multiple days of the week. |
| Checked At | The time range during which you want to run an automatic check. Valid values: 24:00 - 06:00, 06:00 - 12:00, 12:00 - 18:00, and 18:00 - 24:00. You can select only one time range. |
| Select Resource Set | The resource sets that you want to check. |

| Baseline Check Item | The baselines that you want to use. |
|---|---|

After you configure the check policy, Security Operations Center (SOC) automatically performs a check based on all specified baselines within the specified time range.
7. View check data.
In the baseline list of the Cloud Service Check page, view the values in the Cloud Product Baseline, Baseline Type, Risk Level, Affected assets, Last Checked At, and Status columns. Find a baseline and click its name or click **Details** in the **Actions** column. In the panel that appears, view data on the Baseline Check Details and Cloud Service Instances tabs. If an organization or instance is riskless, you can select and add the organization or instance to the whitelist. Find a baseline and click **Verify** in the **Actions** column, or select multiple baselines and click **Verify** below the baseline list to verify the baselines. During the verification, you can click **View** in the Actions column of the baseline to view the verification progress. You can click **Cancel Verification** in the Actions column of the baseline to cancel the verification.

#### 3.3.5 View attack surface assessment results

This topic describes how to view attack surface assessment results.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis**＞**Attack Surface Assessment**.
4. In the upper-right corner of the **Attack Surface Assessment** page, select the organization
or platform that you want to view.
5. On the **Attack Surface Assessment** page, view the statistics of exposed attack surfaces.
**Shadow IP addresses Within Last 30 Days** : A shadow IP address outside the cloud is
an IP address of an asset that can communicate with the cloud platform but is not managed by the cloud platform. The asset can be unauthorized software, an unapproved hardware device, a cloud service, or a third-party application. This type of asset is not managed by the cloud platform and may cause unknown risks or threats. Attackers can use a shadow IP address to attack assets in the cloud.
**Vulnerable Security Group**: A vulnerable security group is a security group that allows
inbound traffic from IP addresses in a loose manner. To implement the principle of least privilege, we recommend that you delete security group rules that allow inbound traffic from unnecessary IP addresses. An unnecessary IP address refers to an IP address that is not required in your workloads. This helps reduce exposure at the network layer.
**Exposed Asset**: An exposed asset is an Elastic Compute Service (ECS) instance that is
accessible from outside the cloud platform and is under a known attack path.
**At-risk Account**: An at-risk account is an account that uses a weak password and can
be used to log on to assets in the cloud from outside the cloud. If the account is leaked, attackers can intrude assets in the cloud with ease.
**Risk Level of Attack Surface** : The risk level of the attack surface for the specified
organization or platform is determined after a comprehensive evaluation is performed. The risk level can be Low, Medium, High, and Critical.
6. View the details of each risk on the corresponding tab.
**Attack Surface**: On this tab, the statistics on attack paths and core assets affected by
the attack paths are displayed. You can click **Panorama View** to view the network topology of all attack paths. You can also click **View Attack Path** in the Actions column of an attack path to view the network topology of the attack path.
**Shadow IP Address Outside Cloud**: On this tab, shadow IP addresses outside the cloud
are displayed in a list. You can click an IP address to view the details of the IP address, including the geographical location, cloud-connected assets, the time when the IP address was first detected, the time when the IP address was last detected, inbound cloud-connected assets, destination IP address, and inbound traffic.
**Vulnerable Security Group**: On this tab, vulnerable security groups are displayed in a
list. You can click **Details** in the Details column of a security group to view more details of the security group.
**Exposed Asset**: On this tab, the ECS instances that can be directly accessed from
outside the cloud are displayed in a list. You can click the name of an instance to view the basic information about the asset and the security vulnerabilities that the asset suffers.
**At-risk Account**: On this tab, risky accounts are displayed in a list.

#### 3.3.6 View traffic analysis results

This topic describes how to view the analysis information about traffic, including organization traffic, application traffic, source IP traffic, and destination IP traffic.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Traffic Analysis**.
4. On the **Traffic Analysis** page, select the widgets that you want to view and specify search
conditions to view the global traffic information.

| Section | Description |
|---|---|

| Widget selection (marked 1 in the following figure) | In this section, you can specify the types of data that you want to view. You can also perform the following operations: View raw logs: Click View Raw Log to go to the Log Query page and view the details of raw logs. Select statistics windows: Select the types of data that you want to view from the Select Statistics Window drop-down list. By default, the following options are selected: Organization Traffic, Application Traffic, Traffic of Source IP Address, Traffic of Destination IP Address, Source Port Traffic, Destination Port Traffic, Access Destination Traffic, and Access Source Traffic. Select a data range: Valid values: TOP 5, TOP 10, and TOP 20. Select the view to be displayed. Save the view: Click the icon to save the current view. Export data: Click the icon to export the data in the current view. |
|---|---|
| Search condition (marked 2 in the preceding figure) | In this section, you can specify search conditions to search for traffic analysis data. You can specify search conditions based on your business requirements. You can specify the time range, query scope, application, source IP address, destination IP address, source port, and destination port. |
| Search result (marked 3 in the preceding figure) | In this section, Security Operations Center (SOC) displays the search results that meet the specified search conditions. |

### 3.4 Use the Tasks module

On the Tasks page, you can analyze and handle global security risks in a streamlined process. This facilitates security operations and management and helps accumulate experience in handling risks. This topic describes how to manage tasks on the Tasks page.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, click **Tasks**.
4. On the Tasks page, view the overall information about tasks.
Total Tasks: the total number of tasks in Security Operations Center (SOC). The number is counted from the time when SOC starts to run until the current point in time. Tasks Pending Handling, Tasks Being Handled, and Handled Tasks: the number of tasks that are pending, the number of tasks that are being handled, and the number of tasks that are handled. The numbers are counted from the time when SOC starts to run until the current point in time. Task Completion Rate and On-time Task Completion Rate: the proportion of tasks that are completed to all tasks and the proportion of tasks that are completed on time to all tasks. The proportions are measured from the time when SOC starts to run until the current point in time. Handling Solutions: the number of handling solutions that are published from the time when SOC starts to run until the current point in time. The solutions include solutions that are manually created and solutions that are synchronized from handling records. Create solutions Click **Handling Solutions**. On the page that appears, click **Create Solution**. In the panel that appears, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Solution Name | Enter the name of the handling solution. The name must be 0 to 200 characters in length. |
| Organization | Select the organization to which the handling solution is delivered. Valid values: Platform and All Organizations Platform All Organizations Organization. If you select this option, you must also select one or more organizations from the Organization drop-down list. |
| Solution Type | Select the type of the handling solution. Valid values: Threat Event Security alert Vulnerabilities Baselines Asset Risks Security Inspection |
| Problem Description | Enter the problem description of the handling solution. The description must be 0 to 1,024 characters in length. |
| Solution | Specify the handling solution. The value must be 0 to 2,048 characters in length. |
| Handled By | Select a contact from the contact drop-down list or enter a custom contact, which must be 0 to 8 characters in length. |

Synchronize solutions from handling records: For more information, see the Handle a task section of this topic. If a solution is manually created, it enters the **Published** state after creation. You can directly reference the solution. If a solution is synchronized from handling records, it is in the **Pending Approval** state after synchronization. You must approve the solution before you can reference the solution. After the solution is referenced, you can disable the solution. You can also **delete** or **modify** a solution.
5. Click **Create Task**, configure the parameters, and then click **OK**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Name | Enter the name of the task. The name must be 0 to 128 characters in length. |
| Delivering Organization | Select the organization to which the task is delivered. Valid values: Platform and All Organizations Platform All Organizations Organization. If you select this option, you must select one or more organizations from the Organization drop-down list. |
| Task Type | Select the type of the task. Valid values: Threat Event: You can click Select Risk Record to select one or more threat events within your data permission scope. Security alert: You can click Select Risk Record to select one or more security alerts within your data permission scope. Vulnerabilities: You can click Select Risk Record to select one or more vulnerabilities within your data permission scope. Baselines: You can click Select Risk Record to select one or more baselines within your data permission scope. Asset Risks: You can click Select Risk Record to select one or more assets within your data permission scope. Security Inspection |
| Priority | Select the priority of the task. Valid values: Urgent, High, Medium, and Low. |
| Problem Description | Enter the problem description of the task. The description must be 0 to 1,024 characters in length. |
| Handling Suggestion | Enter handling suggestions for the task. The value must be 0 to 1,024 characters in length. You can select Referenced Solution and select one or more handling solutions from the drop-down list. |

| Handling Deadline | Specify the deadline for the task. If the task is not completed before the deadline, the handling status of the task changes to Timed Out. |
|---|---|
| Handled By | Select a contact from the contact drop-down list or enter a custom contact, which must be 0 to 8 characters in length. |
| Notification Method | Valid values: DingTalk and Mail. |

After the task is created, you can view the task in the task list. You can also handle all tasks. Search for a task Specify filter conditions to search for a task. You can specify the following filter conditions: Scope, Task Type, Priority, Task Status, Processing status, Task Name, and Handled By. Handle a task i. Find the task and click the task name or **Handling Details** in the **Actions** column. ii. On the Task Details page, turn on Received. Start to Handle. iii. Handle the task based on suggestions provided in the **Handling Suggestion** section and record the handling process in the **Handling Records** field. The value must be 0 to 2,048 characters in length.

> **Note:** When you enter a record, you can select **Synchronize to Handling** **Solutions**. If you encounter the same task later, you can directly reference the handling solution as the handling suggestion.
> If you select Synchronize to Handling Solutions for a handling record, the handling record becomes a handling solution and enters the **Pending** **Approval** state. Before you can reference the handling solution, you must go to the **Handling Solutions** page and approve the solution. You can also disable the solution.

After a task is handled, the task status changes from **In processing** to **Completed**, and you cannot modify the task.

### 3.5 Asset Management

#### 3.5.1 View tenant assets

You can view the assets of tenants on the Tenant Assets page. The assets include Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, Object Storage Service (OSS) buckets, Server Load Balancer (SLB) instances, and elastic IP addresses (EIPs). This topic describes how to view the assets of tenants. You can also specify search conditions in the search box to search for an asset.

> **Note:** If you do not specify search conditions, all assets are automatically displayed.

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Assets > Tenant Assets**.
4. In the upper-right corner of the **Tenant Assets** page, select one or more organizations that
you want to view from the **Scope** drop-down list. Then, you can view the tenant asset overview.
5. Click the **ECS**, **ApsaraDB RDS**, **OSS**, **SLB**, **EIP**, **Active Internet IP Aaddresses**, **Tunnel**,
and **Server Outside Cloud** tabs to view the assets of the tenant. You can specify filter conditions to search for servers, assets, or instances.

> **Note:** If you do not specify search conditions, all servers, assets, or instances are automatically displayed.

Configure asset importance tags and business types. Click a server or instance name to view the following details.

**ECS**

| Tab | Description |
|---|---|

| Asset Information | Basic information: You can view the asset information in the Basic Information and Disk Information sections. Network Information: You can view the asset information in the VPC, SLB, NAT Gateway, and EIP sections. You can also click Network Link View to view the network connections and Internet access paths to ECS instances. This can help you troubleshoot network issues, reduce exposure risks, and trace threats. You can zoom in, zoom out, and download the view. You can also drag the elements in the view. You can click Network Information List to return to the network information list. Security policy: You can view the information in the Secure login settings and Security Group Information sections. |
|---|---|
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack Configuration Management DataBase (CMDB). Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Fingerprints | You can view fingerprint information on the Port, Software, Process, Account, Planned tasks, Middleware, and Startup Item tabs. |
| Asset Risks | Risk Level You can view the risk assessment data of the asset, including the asset risk index, network attack risks, suspicious process risks, vulnerability risks, and security baseline risks. You can view the distribution of network attacks, suspicious behavior, vulnerabilities, and baselines by risk level. You can also view the trend of network attacks within the last seven days. You can view the following information: top 5 network attack risks, top 5 suspicious process risks, top 5 security vulnerability risks, and top 5 security baseline risks. Network Attacks: You can view and handle network attacks on the asset. Suspicious Processes: You can view and handle the suspicious behavior that affects the asset. Vulnerabilities: You can view the details of vulnerabilities in the asset and fix the vulnerabilities based on the provided suggestions. Baselines: You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |

**ApsaraDB RDS**

| Tab | Description |
|---|---|
| Asset Information | Basic information: You can view the basic information about the ApsaraDB RDS instance in the Basic Information section. Network Information: You can view the tunnel information about the ApsaraDB RDS instance in the Tunnel section. Security policy: You can view the whitelist of the ApsaraDB RDS instance in the Whitelist information section. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | You can view the baseline risks in the asset and handle the risks based on the provided suggestions. |

**OSS**

| Tab | Description |
|---|---|
| Asset Information | You can view the basic information about the OSS bucket. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |

| Asset Risks | You can view the baseline risks in the OSS bucket and handle the risks based on the provided suggestions. |
|---|---|

**SLB, EIP, and Active Internet IP Addresses**

| Tab | Description |
|---|---|
| Asset Information | Basic information: You can view the basic information about the asset. Associate ECS Asset: You can view the information about the ECS instances that are associated with the asset. You can click a server name to view the details of the associated ECS instance. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | Network Attacks: You can view and handle network attacks on the asset. Suspicious Processes: You can view and handle the suspicious behavior that affects the asset. Vulnerabilities: You can view the details of vulnerabilities in the asset and fix the vulnerabilities based on the provided suggestions. Baselines: You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. |

**Tunnel**

| Tab | Description |
|---|---|

| Asset Information | Basic information: You can view the basic information about the asset in the Basic Information section. Network Information: You can view the tunnel information about the asset in the Tunnel section. Security policy: You can view the whitelist of the asset in the Whitelist information section. |
|---|---|
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. |

**Servers Outside Cloud**

| Tab | Description |
|---|---|
| Asset Information | Basic information: You can view the basic information and network information about the asset. Security policy: You can view the security logon settings. |
| Asset Fingerprints | You can view fingerprint information on the Port, Software, Process, Account, Planned tasks, Middleware, and Startup Item tabs. |

| Asset Risks | Risk Level You can view the risk assessment data of the asset, including the asset risk index, network attack risks, suspicious process risks, vulnerability risks, and security baseline risks. You can view the distribution of network attacks, suspicious behavior, vulnerabilities, and baselines by risk level. You can also view the trend of network attacks within the last seven days. You can view the following information: top 5 network attack risks, top 5 suspicious process risks, top 5 security vulnerability risks, and top 5 security baseline risks. Suspicious Processes: You can view and handle the suspicious behavior that affects the asset. Vulnerabilities: You can view the details of vulnerabilities in the asset and fix the vulnerabilities based on the provided suggestions. Baselines: You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |
|---|---|

Click the icon to refresh the asset list. Click the icon to export the asset information. Click the icon to configure the items that you want to view in the asset list.

#### 3.5.2 View platform assets

This topic describes how to view the protection information about physical machines on which platform assets are deployed. Security administrators can identify issues and obtain handling suggestions based on the information.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Assets > Platform Assets**.
4. On the **Platform Assets** page, view asset information.

> **Note:** By default, all assets are displayed.

You can view the total number of assets, the numbers of offline assets, high-risk assets, medium-risk assets, and low-risk assets, and the risk indicators of at-risk assets. In the asset list, view the information in the following columns: Server Name/IP, Server UUID, Organization, Risk Index, Operating System, Suspicious Processes, and Agent State. You can configure the Importance and Business Type parameters for an asset.
5. Click the name of an asset to view information on the Basic information, Associate ECS
Asset, Risk Level, and Suspicious Processes tabs. Risk Level You can view information in the Asset Risk Index, Suspicious Process Risk, Suspicious Process Distribution by Risk Level, Trend of Suspicious Processes in Last 7 Days, and Top 5 Suspicious Process Risks sections. You can also click the icon to download a snapshot of the page. Suspicious Processes If a large number of alerts are displayed, you can configure the following search conditions to search for a specific alert: start time, end time, data source, alert type, risk level, and handling status. To handle an alert, click the alert name. In the panel that appears, view the affected assets, the time when the alert occurred, and the time when the alert ended. You can also view the details of the alert and the handling suggestion in the **Related Exceptions** section.

### 3.6 Use the Logs module

#### 3.6.1 View the information on the Overview page

**page**

The Overview page displays the overall statistics on all logs that are collected by Security Operations Center (SOC) in a visualized manner. On the Overview page, you can pre-define and customize widgets to display logs. This topic describes how to view the logs that are displayed in the widgets on the Overview page.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Overview**.
4. On the **Overview** page, specify a time range, the query scope, and the widgets that you
want to view. Valid values for the time range: **Today**, **Last 24 Hours**, **Last 7 Days**, **Last 30 Days**, and **Custom**.

**Valid values for the default widget:**

**Total Logs**: displays the total number of collected log entries and the comparison
statistics on the total numbers of collected log entries between the current and previous time ranges.
**Distribution of Log Organizations** : displays the proportions of logs collected on the
platform side and tenant side. This option is available only to global organization security administrators.
**Trend of Logs**: displays the trend in the number of collected log entries. The log
entries are collected on an hourly basis within a time range of five days or less. The log entries are collected on a daily basis within a time range of more than five days.
**Log Statistics by Severity**: displays the total numbers of collected logs by severity
level. Supported severities include: Information, Suspicious, Moderate, Serious, and Urgent.
**Log Distribution by Log Source** : displays the proportions of collected logs by log
source. Supported log sources include, but are not limited to: Server Guard, Container Security Service (CSS), and Cloud Firewall.
**Log Distribution by Log Source System Type** : displays the proportions of collected
logs by log source system type. System types for log sources include security, data, host, and network.
**Log Distribution by Type** : displays the proportions of collected logs by type. Log
types include network logs, operation logs, threat logs, application logs, and system logs.
**Log Trend by Type**: displays the trend in proportions of collected logs by type. On the
Log Query page, you can set the query result as followed logs and select Save As Independent Window. Then, you can view the followed logs in a widget on the Overview page.
5. On the **Overview** page, manage the widgets of the logs.
Move a widget In the widget that you want to manage, click the icon and drag the widget to a specific position. In the upper-right corner of the **Overview** page, click the icon. Close a widget In the widget that you want to manage, move the pointer over the icon and click **Close**
**View**. In the upper-right corner of the **Overview** page, click the
icon. Export snapshots on the page In the upper-right corner of the **Overview** page, click the icon. Customize a widget View a statement In the **test** widget, move the pointer over the icon and click **View Statement**. Edit a widget a. In the **test** widget, move the pointer over the icon and click **Edit View**. b. In the **Customize Chart** section of the **Edit View** dialog box, configure the Chart Type, Chart Size, Chart Title, Statistics Field, X-axis Field, and Y-Axis Field parameters. c. Click **Generate Preview** to view the custom widget. After you confirm the configurations, click **Save to Log Overview**. Close a widget In the **test** widget, move the pointer over the icon and click **Close View**. In the upper-right corner of the **Overview** page, click the icon. Remove a widget from default widgets In the **test** widget, move the pointer over the icon and click **Remove from Default**. In the upper-right corner of the **Overview** page, click the icon.
6. In the lower part of the **Overview** page, view the application logs of Server Guard.
Click **Details** in the **data** column of a log to view the log details.

#### 3.6.2 Query log details

This topic describes how to query log details.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Query**.
4. Search for logs by specifying the following filter conditions: time range, scope, system type,
log source, log type, log subtype, log field, and query statement. The following list describes the query results: Log distribution histogram: displays the distribution of the queried logs by time. Table Mode: displays the logs of the specified log fields in a table and the log analysis result. List Mode: displays the logs of the specified log fields in a list and the log analysis result. Chart: displays the log analysis result and allows you to customize the chart type, chart size, chart title, and statistical field of a log.

**Related operations**

Follow Logs: Click **Follow Logs** and enter a name in the **Followed Log Name** field. After the configuration is complete, you can select a log entry from the **Default data** dropdown list to view the log entry. In this case, you can modify the log settings and click the icon to save the latest log settings. Log Dictionary: Specify whether to enable the log dictionary feature,. A log dictionary records the log field information, including the name, type, and description of each type of log.

#### 3.6.3 Query raw logs

Security Operations Center (SOC) allows you to query raw logs. Raw logs contain the information that is required for debugging. Security administrators can use these raw logs to troubleshoot system failures. This topic describes how to query raw logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Query**.
4. On the **Log Query** page, specify the **time**, **organization**, **system type**, **log source**, **log**
**type**, and **query syntax**. Then, click **Search**.
The number of queried logs within the specified time range is displayed in a bar chart. The log details are displayed in a list. The following list describes the supported query syntax:

**Full-text match**

Example 1: 12.XX.XX.12. Example 2: www.bai*.c?m.

**Field-based query**

Example 1:

```
src_ip: 12.XX.XX.12 AND hostname:abc?o*al OR filesize:>100
```

Example 2:

```
12.XX.XX.12 AND appName:yundun-soc
```

**SQL-like query**

Example 1:

```
select * from mytable where src_ip = '12.XX.XX.12' order by gmt_create desc
```

Example 2:

```
select src_ip, count(*) as cnt, max(filesize) as filesize from mytable group by src _ip limit 10
```

Example 3:

```
select count(*) as cnt from mytable where hostname like '%abc%'
```

> **Important:** When you perform field-based queries, specify the logical operators AND, OR, and NOT in upper-case letters.
> When you enter an SQL statement to query logs, set the name of the table name to **mytable**.
> When you enter an SQL statement to query logs, user-defined functions (UDFs) and nested queries are not supported.
> When you enter an SQL statement to query logs, the DISTINCT operations are not supported.
> When you enter an SQL statement to query logs, you can use the count(*) as cnt function to rename the queried log fields cnt. You cannot use the src_ip as ip function to rename the queried IP addresses.
> When you enter an SQL statement to query logs, only fields of the string type can be aggregated.
> If a query times out when you use a wildcard character to query logs, you can narrow down the query scope and try again.

5. In the log list, select the fields that you want to query and view the logs about the fields.
You can also expand a display field to view the top 5 values of the field.

#### 3.6.4 View platform logs

Platform logs record information about Apsara Stack Security. Security administrators can use these logs to troubleshoot issues that occur on Apsara Stack Security. This topic describes how to view platform logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Platform Log**.
4. On the **Platform Log** page, specify the log source, time range, and query content based on
your business requirements. The following list describes the supported query syntax:

**Full-text match**

Example 1:

```
12.XX.XX.12
```

Example 2:

```
www.bai*.c?m
```

**Field-based query**

Example 1:

```
src_ip: 12.XX.XX.12 AND hostname:abc?o*al OR filesize:>100
```

Example 2:

```
12.XX.XX.12 AND appName:yundun-soc
```

The system displays logs of Apsara Stack Security in a column chart based on the specified search conditions. You can view the numbers of logs at different points in time within the specified time range. You can also view the log details in the log list. To configure the fields that you want to display in the log list, click the icon. To export the log list, click the icon.
5. Optional. Click **Save as Analysis Rule**. On the **Create Rule** page, the **Log Scope** and
**Search Condition** parameters are automatically configured based on the previous
parameter settings. Configure the **Threat Name** parameter and click **OK**. For more information about parameter settings, see Create an analysis rule. After a rule is created, you can view the rule whose type is **Custom Association Rule** on the **Analytic Rules** page.

#### 3.6.5 View tenant logs

Tenant logs record information about tenants. Security administrators can use these logs to troubleshoot issues that occur on the tenant side. This topic describes how to view tenant logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Tenant Log**.
4. On the **Tenant Log** page, specify the scope, log source, and time range based on your
business requirements. The following list describes the supported query syntax:

**Full-text match**

Example 1:

```
12.XX.XX.12
```

Example 2:

```
www.bai*.c?m
```

**Field-based query**

Example 1:

```
src_ip: 12.XX.XX.12 AND hostname:abc?o*al OR filesize:>100
```

Example 2:

```
12.XX.XX.12 AND appName:yundun-soc
```

The system displays **tenant logs** in a column chart based on the query conditions that you specify. You can view the numbers of logs at different points in time within the specified time range. You can also view the details of the queried logs in the log list. To configure the fields that you want to display in the log list, click the icon. To view the details of a log, click **Details** in the data column of the log. To export the log list, click the icon.

#### 3.6.6 Log configurations

##### 3.6.6.1 Manage log sources

You can manage log sources of the Third-party Network Element or Terminal type on the Log Sources tab as a security administrator. This topic describes how to manage the log sources that are connected to Security Operations Center (SOC).
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Configurations**.
4. On the **Log Sources** tab, click **New log source**. In the panel that appears, configure the
parameters and click **OK**. The following table describes the parameters.

**Third-party Network Element**

| Parameter | Description |
|---|---|
| Log Source | Select Third-party Network Element. |
| Name | Specify the name of the log source. The name must be 0 to 30 characters in length. |
| Access System Type | Select the type of the source system in the log source that is connected to SOC. Valid values: Host, Storage, Application, Network, Data, Security, and Others. |
| Reliability Level | Enter the reliability level of the log data that is obtained from the log source. This value is used as the weight value in log analysis and affects the analysis result. Valid values: 0 to 100. Unit: %. |

| Data Protocol | Select the protocol over which the log data is delivered to SOC. Valid values: Syslog. If you select this option, you must configure the following parameters: IP Address: Enter the IP address of the log source. Host Name: Enter the hostname of the log source. Protocol: Select the network protocol of the log source. Valid values: UDP TCP SLS. If you select this option, you must configure the following parameters: Log Project accessKey Log Store secretKey Endpoint |
|---|---|
| Log Parsing | Select a log parsing template. You can click Create Log Parsing Template to create a log parsing template. You can also select an existing log parsing template. For more information, see Configure a log parsing template. |
| Storage Period | Specify the data storage period. Valid values: 0 to 185. Unit: days. |
| Permission Scope | Specify the level of users who can manage the log source. Valid values: Platform Tenant If you want to view threat-related alerts in SOC, select Display Alerts in Operations Center. |
| Description | Enter a description for the log source. |

**Terminal**

| Parame ter | Description |
|---|---|

| Log Source | Select Terminal Note If you want to collect logs of a host, Simple Log Service is required and Logtail must be installed on the host. Make sure that Logtail is installed and configured on the host. |
|---|---|
| Name | Specify the name of the log source. The name must be 0 to 30 characters in length. |
| Access System Type | Select the type of the source system in the log source that is connected to SOC. Valid values: Host, Storage, Application, Network, Data, Security, and Others. |
| Reliabil ity Level | Enter the reliability level of the log data that is obtained from the log source. This value is used as the weight value in log analysis and affects the analysis result. Valid values: 0 to 100. Unit: %. |
| Networ k Type | Select the network type of the log source. Valid values: Classic Network VPC |
| Host ID | Use the default value IP Address. |
| Host Name | Enter the hostname and IP address of the log source. You can add multiple hostnames and IP addresses. |
| Collect Logs | Specify the log data that you want to collect. Valid values: Windows Event Logs and Linux Logs Custom If you select this option, you must configure the following parameters: Operating system: Select Windows or Linux. Log Directory: Specify the directory of the log file. Example: /var/log/http/ . Directory Depth: Specify the maximum depth of the log file directory for monitoring. Valid values: 0 to 1000. A value of 0 specifies that only the specified log file directory is monitored. Log Files: Enter the name of the log file. Example: access*.log . Collection and Filtering: Specify a filter method, which can be based on specified directories or files. |

| Log Parsing | Select a log parsing template. You can click Create Log Parsing Template to create a log parsing template. You can also select an existing log parsing template. For more information, see Configure a log parsing template. |
|---|---|
| Storage Period | Specify the data storage period. Valid values: 0 to 185. Unit: days. |
| Permiss ion Scope | Specify the level of users who can manage the log source. If you set the Permission Scope parameter to Tenant and select a specific tenant from the drop-down list, the aliuid log field is automatically specified when a Terminal log source is connected to SOC. This also facilitates operations in hybrid clouds. Valid values: Platform Tenant If you want to view threat-related alerts in SOC, select Display Alerts in Operations Center. |
| Descrip tion | Enter a description for the log source. |

After the log source is created, the log source appears in the log source list. You can configure filter conditions such as **System Type**, **Data Source**, **Data Protocol**, and
**Status** to view and manage log sources.
You can view the following information about a log source: IP, data source, access system type, data protocol, log parsing template, log storage and total logs, status, online status, and enabling status.

> **Note:** If no data is collected from a log source within 24 hours, the icon in the **Online** **Status** column is displayed in **orange**. In this case, you need to check the log source.
> If no data is collected from a log source within 120 hours, the icon in the **Online Status** column is displayed in **red**. In this case, you need to check the log source.

SOC records the most recent 10 logs that are unidentified for a log source and allows you to view these logs. If a log does not match a parsing rule or uses a timestamp that is in an invalid format, the log is unidentified. You can perform the following steps to process unidentified logs for a log source: a. Find the log source and click **View Unrecognized Logs** in the **Actions** column. b. In the **Edit** panel, process unidentified logs. If **No Matched Parsing Rules** is displayed in the Why Not Recognized column, click
**Create Log Parsing Template** and configure the parameters.
a. In the **Rule Information** step, configure the **Rule Name** and **Log Type** parameters and click **Next**. b. In the **Log Parsing** step, configure the **Log Sample**, **Log Identifier**, and **Parsing**
**Method** parameters, and click **Next**. Then, complete the **Log Standardization**
step. If a different value is displayed in the Why Not Recognized column, click **Edit Log**
**Parsing Rule** to modify the existing rules based on the value, or click **Create Rule**
to create a parsing rule for the log source. You can **modify** or **delete** a log source based on your business requirements.

##### 3.6.6.2 Configure a log parsing template

Security Operations Center (SOC) provides the log parsing feature. Security administrators can configure log parsing templates based on their business requirements to manage logs in an efficient manner. This topic describes how to configure a log parsing template.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Configurations**.
4. On the **Log Parsing** tab, click **Create Log Parsing Template**.
5. In the **Create Log Parsing Template** wizard, configure the **Template Name** and **Scope**
parameters. Then, click **Next**. The values of the **Template Name** and **Scope** parameters can be up to 200 characters in length.
6. Click **Create Rule** to create a rule that is associated with the log parsing template.
Configure the rule information. Configure the **Rule Name** and **Log Type** parameters. Then, click **Next**. The value of the **Rule Name** parameter can be up to 15 characters in length. Valid values of the Log Type parameter: **System Log**, **Operation Log**, **Network Log**,
**Threat Log**, **Application Log**, and **Other**.
Specify a log parsing method. Configure the **Log Sample**, **Log Identifier**, and **Parsing Method** parameters. Then, click **Parse**. After the parsing is complete, click **Next**. Click **Add** to specify multiple parsing methods. Valid values of the Parsing Method parameter: json jsonCut jsonArray jsonArrayCut grok keyvalue Specify field mappings to format logs. Specify field mappings to format logs and click **Confirm**. If you want to create multiple rules, repeat the preceding steps.
7. After all rules are created, click **Confirmation**.
The log parsing template that you created is displayed in the log parsing list. You can modify or delete the template based on your business requirements.

##### 3.6.6.3 Configure log forwarding

Security Operations Center (SOC) provides the log forwarding feature. Security administrators can forward logs based on their business requirements and view logs in a timely manner. You can specify multiple log sources for a log forwarding task. You can also forward logs that belong to specified organizations. This topic describes how to configure a log forwarding task.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Configurations**.
4. On the **Log Forwarding** tab, click **Create Forwarding Task**. In the panel that appears,
configure the following parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Task name | The name of the forwarding task. The name must be 0 to 64 characters in length. |
| Data Protocol | The protocol based on which logs are forwarded. The value is fixed as Syslog. |
| IP:Port | The IP address, port number, and protocol of the server to which logs are forwarded. The protocol supports User Datagram Protocol (UDP) and Transmission Control Protocol (TCP). |
| Organization | The organization to which the logs are forwarded. Valid values: Platform and All Organizations Platform All Organizations Organization. If you select this option, you must select one or more organizations from the Organization drop-down list. |

| Select Log Source | Select one or more types of log sources in theL og Source section and click the icon to move the selected log sources to theS elected Log Sources section. |
|---|---|
| Forwarding Status | Turn on or turn off the switch to enable or disable the log forwarding feature. |

To create multiple log forwarding tasks, repeat the preceding steps. After you create a log forwarding task, you can view and manage the log forwarding task in the log forwarding task list. You can filter log forwarding tasks by scope or task name. You can turn on or turn off the switches in the Status column to enable or disable log forwarding. You can modify or delete a log forwarding task.

### 3.7 Use the Reports module

This topic describes how to create a report task. After you create a report task, the system sends reports to the specified email addresses at specified intervals.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Reports**.
4. On the Reports page, click **Create Report**.
5. In the **Create Report** panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Report Name | The name of the report task. We recommend that you enter information such as the report purpose for easier identification and management. The name must be 1 to 16 characters in length. |
| Task Type | The type of the task. Valid values: Daily Report, Weekly Report, and Monthly Report. |
| Organization | The platform or organizations to which the report task is related. |
| Email Box | The email address of the report recipient. If you enter more than one email address, separate the email addresses with commas (,). |

6. Click **OK**.

**Result**

In the report task list, you can download, edit, and delete the newly created report tasks.

### 3.8 Use the Rules module

#### 3.8.1 Create an analysis rule

You can use analysis rules to perform comprehensive association-based analysis on a large number of logs. You can also trace the attack paths of multi-phase attacks based on the detected high risks. This way, security administrators can obtain helpful risk information in an efficient and quick manner and the efficiency of security operations is improved. This topic describes how to create an analysis rule. Security Operations Center (SOC) provides built-in rules based on common business requirements. You can only view the details of the built-in rules but cannot modify the rules. If the built-in rules cannot meet your business requirements, you can perform the following steps to create a rule:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Rules > Analytic Rules**.
4. On the **Analytic Rules** page, click **Create Rule**. In the Create Rule wizard, configure the
following parameters.

| Parameter | Description |
|---|---|
| Threat Name | The name for a threat. |
| Threat Level | The level for the threat. Valid values: Information Suspicious Moderate Serious Urgent |

| Threat Type | The threat type. You can select multiple types for a threat. Valid values: Network Scanning Vulnerability Exploitation Malware Network Attack Suspicious Network Connection Privilege Escalation Suspicious Processes |
|---|---|
| ATT&CK ID | The IDs of one or more attacks that are involved in the Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) stages. |
| Rule Type | The type for the rule that you want to create. If you select Association-based Analysis Rule, you must configure the following parameters: Time Series: the time condition for the rule that you want to create. Valid values: Periodicity: The rule is used to detect the threats that occur within the same period of time. Chronological Order: The rule is used to detect the threats that occur in sequence. Associated Object: the object on which the rule is used to detect threats. The value is fixed as Same Asset. Trigger Condition: the trigger condition. You can configure the following parameters to specify the trigger condition: Association Type: specifies whether the associated condition is a required condition. Log Scope: the log sources, log types, log subtypes, and log levels. Source IP and Destination IP. Keyword: If you specify multiple keywords, separate them with semicolons (;). Time Period: Valid values: 0 to 1440. Unit: minutes. Log Quantity: the number of logs. Attack Phase: Valid values: Payload Delivery, Vulnerability Exploitation, Backdoor Installation, Command and Control, Scanning, Privilege Escalation and Action on Objectives. If you select Search-based Analysis Rule, you must configure the following parameters: Log Scope: the platform or organizations to which you want to apply the rule. Search Condition: the search conditions for the rule. Time Period: the time period of a rule. |

| Execution Period | The interval at which the rule is executed. Default value: 5. Unit: minutes. |
|---|---|
| Description | The description of the threat. The description can be 0 to 256 characters in length. |
| Handling Suggestion | The handling suggestion. The suggestion can be 0 to 256 characters in length. |

5. **Optional.** If you want to verify the created rule, click **Quick Verify**.
6. Click **OK**.
The created rule is displayed in the rule list. You can click **Edit** or **Delete** in the Actions column of a custom rule to modify or delete the rule based on your business requirements.

#### 3.8.2 Alert rules

> You can create alert rules to obtain threat events, alerts, baseline risks, vulnerabilities, and configuration risks in cloud services in a timely manner. You can also send real-time alerts to alert contacts by DingTalk or email. The security alerts are provided in Security Operations Center (SOC). This topic describes how to create an alert rule.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Rules** > **Alert Rule**.
4. On the **Alert Rules** page, click Create Rule.
5. In the **Create Alert Rule** panel, configure the parameters and click **OK**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Rule Name | Enter the name of the alert rule. The name must be 0 to 64 characters in length. You can use the name to search for the rule. |
| Rule Description | Enter the description of the alert rule. The description must be 0 to 128 characters in length. |

| Rule Scope | Select the application scope of the alert rule. Valid values:P latform and All Organizations, Platform, All Organizations, and Select Organization. Note If you are a platform security administrator, the default value Platform is displayed. If you are an organization security administrator, you need to select specific organizations. |
|---|---|
| Alert Condition | Select a value for Rule Type, which supports Threat Event, Alert, Vulnerability, and Baseline. Then, configure an alert condition based on the value. Threat Event: If you select this option, you must configure the Threat Event Name, Threat Event Severity, Threat Event Type, Attacker IP Address, Attacked IP Address, Scanned Asset, and Threat Behavior parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. Alert: If you select this option, you must configure the Alert Name, Alert Severity, Alert Type, Attack IP Address, Attack IP Address, and Scanned Asset parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. Vulnerability: If you select this option, you must configure the Vulnerability Name, Vulnerability Severity, Vulnerability Type, CVE ID, Scanned Asset, and Affected Asset parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. Baseline: If you select this option, you must configure the Baseline Name, Baseline Severity, Baseline Type, Scanned Asset, and Affected Asset parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. |
| Notification Recipient | Select the contacts to which you want to send alerts. You can select only the contacts that are added in System Configurations ＞ Alert Settings. |
| Notification Method | Select the notification method that you want to use to send alerts. Valid values: DingTalk and Email. |
| Alerting Interval | Specify the interval at which you want to send alerts. You can specify a value that ranges from 0 to 1,440 minutes or a value that ranges from 0 to 168 hours. |

After the alert rule is created, the contacts that are specified in the alert rule receive alerts when threats are detected.

#### 3.8.3 Create a blocking rule

This topic describes how to block requests for a specific IP address with a few clicks.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Rules > Block Rules**.
4. On the **Block Rules** page, click **Add**.
5. In the **Add** dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| IP Protocol | Specify the type of the IP address that you want to block. Valid values: IPv4 and IPv6. |
| Source IP Address | Enter the source IP address that you want to block. |
| Destination IP Address | Enter the destination IP address that you want to block. |
| Destination Port | Enter the destination port that is used with the specified destination IP address. |
| Blocking Duration | Select a time range during which you want to block requests. Valid values: 1 Day, 7 Days, and 30 Days. |
| Type | Select the blocking mode. Valid values: Whitelist and Blacklist. |
| Description | Enter the reason for blocking. |

6. Click **OK**.
The created blocking rule is displayed in the rule list. You can **query** or **delete** the rule based on your business requirements.

### 3.9 Use the Operations module

#### 3.9.1 Configure the log storage policy

Security Operations Center (SOC) allows you to create a custom log storage policy based on your business requirements. This topic describes how to configure a log storage policy.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose**Operations > Storage Management**.
4. On the **Storage Management** page, click **Modify**. After you modify the configurations,
click **Modify**. SOC provides default values for the log storage policy. If the default values do not meet your business requirements, you can specify other values for the log storage policy.

**Unified Log Analysis and Storage**

| Parameter | Description |
|---|---|

| Used Storage Space | The storage space that is used. |
|---|---|
| Maximum Storage Duration | The maximum storage duration that can be configured for a log source. Default value: 185. Valid values: 185 to 1098. Unit: days. |

**Built-in Storage**

| Parameter | Description |
|---|---|
| Maximum Storage Duration | The maximum storage duration that can be configured for a log source. Default value: 7. Valid values: 0 to 30. Unit: days. |
| Data Cleansing Notification | If you turn on the switch, you are notified when the number of data entries in a single security monitoring table exceeds 1 million and automatic data deletion is triggered. When the preceding scenario occurs, you are notified only once. |
| Notification Recipient | The recipient who receives notifications when the number of data entries in a single security monitoring table exceeds 1 million and automatic data deletion is triggered. |
| Notification Method | The notification methods by which the recipient receives notifications when the number of data entries in a single security monitoring table exceeds 1 million and automatic data deletion is triggered. Valid values: DingTalk and Email. |

#### 3.9.2 Add custom IP addresses and modify the SOC location configuration

**the SOC location configuration**

This topic describes how to add custom IP addresses and modify the location configuration of Security Operations Center (SOC). You can configure custom internal IP addresses based on your networking plan. After you configure the internal IP addresses, IP addresses from the public address library do not match the addresses outside China.

**Add IP addresses**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Operations > IP Address Library**.
4. Click **Add**.
If you want to add multiple IP addresses and locations at a time, click **Batch Upload (.txt)** to import multiple IP addresses and locations by using a template.
5. In the **New** dialog box, configure the IP and Geographic Location parameters.
6. Click **OK**.
The added IP address is displayed in the IP address list. You can perform the following operations based on your business requirements: Modify the IP address Find the IP address that you want to manage and click **Modify**. In the **Modify** dialog box, modify the Geographic Location parameter. Delete the IP address Find the IP address that you want to manage and click **Delete**. In the **Delete** message, click **OK**.

**Modify the location configuration of SOC**

The Global Security Situation feature of SOC uses the geographical location that is configured for SOC. You can perform the following steps to modify the location configuration of SOC.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Operations > IP Address Library**.
4. In the upper-right corner of the **IP Address Library** page, click **Security Operations**
**Center Location Configuration**.
5. In the **Security Operations Center Location Configuration** dialog box, configure the
**Country**, **Province**, and **City** parameters and click **OK**.

#### 3.9.3 Manage organization authorization

This topic describes how to enable global organization service-linked role authorization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Operations > Organization Authorization**.
4. Turn on the switch next to **Global Organization SLR Authorization**. In the message that
appears, click **OK**. If Global Organization SLR Authorization is enabled, Security Operations Center (SOC) is automatically assigned the service-linked roles of all organizations, including organizations that are created in subsequent operations. SOC automatically collects information about the cloud assets and security data of all organizations. The global organization security administrator has the operations and management permissions on the cloud platform and cloud assets and security data of organizations. If Global Organization SLR Authorization is disabled, SOC is not assigned the servicelinked roles of the organizations. You must assign the service-linked role of at least one organization to SOC as an organization security administrator. Otherwise, the features of SOC are unavailable. After the service-linked role of the organization is assigned to SOC, SOC automatically collects information about the cloud assets and security data of the organization. The global organization security administrator has the operations and management permissions on the cloud platform and the organization.

**Important**

> Organization service-linked role authorization has a higher priority than global organization service-linked role authorization. If the number of organizations for which global organization service-linked role authorization is enabled is different from the total number of organizations, you must modify the service-linked role authorization for the organizations.

rity configurations

## 4 Apsara Stack Security configurations

**configurations**

### 4.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. We recommend that you use Google Chrome.
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

rity configurations

### 4.2 System monitoring

On the Monitoring Overview tab, you can monitor cloud services to identify abnormal services at the earliest opportunity. This facilitates service O&M. This topic describes how to view the monitoring data.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **System Monitoring**.
4. On the System Monitoring page, view the monitoring overview and monitoring data of cloud
services. On the **Monitoring Overview** tab, you can view the following information. Monitoring overview: You can view the total numbers of monitored services, abnormal services, metrics, and exceptions. Cloud service monitoring data: You can view the information about cloud services, such as the number of metrics, the number of exceptions, and the service status. You can view the monitoring data of each cloud service on the corresponding cloud service tab. Cloud services that can be monitored include Server Guard, Basic Service, Automated Orchestration, Platform for Connecting to Third-party Services, Data Encryption Service, Threat Intelligence, Intelligent Analysis Platform, Updates, Trusted Computing, NDR, Security Operations Center, Key Management Service, Password service platform, Key Management Service(Base Edition), and Container safety. rity configurations Monitored data includes data of all services that are connected to Alibaba Cloud services. In this topic, Server Guard is used as an example. Click the **Server Guard** tab to view all services that are required to run Server Guard. You can search for a service by service name or status in the search box above the service list. In the service card section, you can view the service status, CPU utilization, memory usage, loads, TCP connections, processes, and NGINX queries per second (QPS). You can click a service card to view the monitoring details of the service.

| Metric | Description |
|---|---|
| Basic Monitoring | You can configure the monitoring time and monitoring view. The monitoring time supports 3 Hours, 6 Hours, 12 Hours, 1 Day, 2 Days, and Custom. You can click the icon to manually update the monitoring data. You can also turn on Auto Refresh to automatically update the monitoring data. The monitoring view supports Cluster View and Single- server View. |
| Middleware |   |
| Health Check | You can check the health status of all hosts in an application based on check methods such as TCP- and HTTP-based health checks. |

### 4.3 Rules

#### 4.3.1 Create and manage IPS rules

Cloud Firewall provides built-in intrusion prevention system (IPS) rules. You can create custom IPS rules based on your business requirements and network environment to monitor the operations of Cloud Firewall. This topic describes how to create and manage custom IPS rules.
1. Log on to the Apsara Uni-manager Management Console.
rity configurations
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

rity configurations

| Description | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |
|---|---|

After you create a custom IPS rule, you can perform the following operations on the rule: View the details of the rule You can filter rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details. Enable the rule Find the rule that you want to enable and turn on the switch in the **Enable or not** column to change the status of the rule from **Disable** to **Enable**. Disable the rule If a rule does not meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Enable or not** column to change the status of the rule from **Enable** to **Disable**.

#### 4.3.2 Manage Anti-DDoS Service rules

On the Anti-DDoS Service rules page, you can modify threshold settings for traffic scrubbing and redirection based on your business requirements. This topic describes how to modify threshold settings for traffic scrubbing and redirection.
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
ii. In the **Modify Threshold** dialog box, specify custom thresholds and click **OK**. rity configurations iii. **Optional.** Click **Automatic DDoS Traffic Redirection and Scrubbing**. In the **Enable**
**Automatic Redirection** message, click **OK**.

> **Note:** By default, **Automatic DDoS Traffic Redirection and Scrubbing** is turned off.

If you turn on Automatic DDoS Traffic Redirection and Scrubbing, traffic scrubbing events are triggered based on custom thresholds. The traffic of attacked IP addresses is automatically forwarded to an Anti-DDoS cluster for scrubbing. If you turn off Automatic DDoS Traffic Redirection and Scrubbing, alert events are triggered based on custom thresholds. You can start or end traffic scrubbing in the Anti-DDoS Service console based on your business requirements.

#### 4.3.3 Manage Server Guard rules

You can view vulnerabilities, baselines, and server exceptions on the Server Guard Rules tab. This topic describes how to view the information about Server Guard rules.
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

rity configurations

| Baselines (marked 2 in the preceding figure) | On the Baselines tab, you can view the baseline types and check the items that are used. To search for a baseline, you can select a baseline type from the Baseline Type drop-down list, select a severity from the Risk Level drop-down list, and enter a check item category or name in the search box. In the baseline list, you can view the following information about a baseline: Baseline Type, Check Item Category, Check Item Name, Risk Level, Updated At, and Status. |
|---|---|
| Server Exceptions (marked 2 in the preceding figure) | On the Server Exceptions tab, you can view the following information: Rule Alert Types and Webshell & Malicious Processes. To search for an exception on a server, you can select a rule category from the Rule Category drop-down list, select a severity level from the Risk Level drop-down list, and then enter a rule subcategory name in the search box. In the server exception list, you can view the following information: Rule Subcategory, Rule Category, Risk Level, Updated At, Source, and Status. |

#### 4.3.4 Create and manage WAF rules

You can create custom Web Application Firewall (WAF) rules based on your business requirements and network environment to monitor the operations of WAF. This topic describes how to create and manage WAF rules.

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

rity configurations

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
rity configurations
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
update packages. rity configurations b. Click Import Upgrade Package and drag the downloaded update packages to the dotted box. You can also click the icon to upload the update packages.

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

Batch update: On the **Feature Library Upgrade** tab, click **One-click upgrade**. Update a service in Apsara Stack Security: Find the service that you want to update on the **Feature Library Upgrade** tab and click **Upgrade now** in the **Operation** column. After the update is complete, the status of the service is **Upgrade successful**. rity configurations If the update fails, you can click **Upgrade Records** in the **Operation** column to find the versions of the feature libraries that failed to be updated and click **Retry** in the Operation column. If the update is successful, you can perform the following operations: On the **Feature Library Upgrade** tab, find the service and click **Version Details** in the **Operation** column to view the versions of the updated rule libraries. You can click **Restart Upgrade** to update a rule library in a feature library. In the **Feature Library Upgrade Records**panel, find the feature library that you want to view and click **Details** in the **Operation** column to view the details of the feature library update package. You can find a rule library and click **Restart**
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

rity configurations

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
rity configurations download and click **Download** in the **Operation** column. After the update packages are downloaded, upload the update packages to Apsara Stack Security Center. In Apsara Stack Security Center, perform update-related operations to complete the update.

### 4.6 Global configuration

#### 4.6.1 Configure host security rules

You can configure global brute-force attack detection rules to prevent hosts from being cracked by brute-force attacks and prevent unusual batch logons and suspicious account logons. This topic describes how to configure host security rules.

**Important**

If you modify global brute-force attack detection rules, all host assets, including tenantside hosts and platform-side physical servers, are affected. The modification also affects the attack analysis results of Threat Detection Service (TDS). Proceed with caution.
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

rity configurations

#### 4.6.2 Configure a whitelist

If a normal request is considered an attack by the attack blocking feature of Threat Detection Service (TDS) or the unusual logon detection feature of Server Guard, you can add the source IP address of the request to a whitelist to avoid false positives. This topic describes how to configure a global whitelist for unusual logons and brute-force attacks.

> **Note:** Make sure that only trusted IP addresses are included in the whitelist.

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
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
rity configurations
4. On the **Global Settings** tab, turn on or off the switch in the Actions column to enable or
disable the attack blocking feature. After you disable the attack blocking feature, Server Guard generates alerts for web attacks but does not block them.

#### 4.6.4 Add a Server Guard account

After you add a Server Guard account, you can use the account to configure and manage Server Guard and Web Application Firewall (WAF) resources. This topic describes how to add a Server Guard account.
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
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Cloud Firewall Monitoring**.
4. In the **System Inspection** section, click **One-click Inspection**.
After the inspection is complete, you can perform the following operations: rity configurations Click **Details** in the **Actions** column of **Internet Firewall (ICFW)**, **VPC Firewall**
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

also click the rity configurations b. In the**Connectivity Check**section, click**Add**. Configure the parameters and click **OK**.

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

1. Log on to the Apsara Uni-manager Management Console.
rity configurations
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Apsara Stack Account** tab, modify the information about your Apsara Stack
tenant account. i. Find your Apsara Stack tenant account and click **Revised** in the **Operation** column. ii. In the **Change Account** dialog box, modify Apsara Stack Account, Access Key, and Access Secret, and click **OK**. After the modification, you can click Details in the **Operation** column to view the details of the Apsara Stack tenant account.

#### 4.8.2 Manage Alibaba Cloud accounts

After you add an Alibaba Cloud account to Apsara Stack Security Center, you can manage the Anti-DDoS Pro, Anti-DDoS Premium, and Web Application Firewall (WAF) instances that belong to the Alibaba Cloud account in Apsara Stack Security Center. This way, you can use features in a hybrid cloud. This topic describes how to add an Alibaba Cloud account to Apsara Stack Security Center. To use features in a hybrid cloud, you can add an Alibaba Cloud account to Apsara Stack Security Center.
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
