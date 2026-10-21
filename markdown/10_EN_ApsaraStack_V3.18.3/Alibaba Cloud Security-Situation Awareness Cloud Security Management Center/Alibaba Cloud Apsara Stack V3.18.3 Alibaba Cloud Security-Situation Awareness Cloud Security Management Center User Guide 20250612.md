---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20250612"
product_version: "V3.18.3"
doc_version: "20250612"
pdf_pages: 60
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20User%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20250612

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
  - 3.4 Asset Management
    - 3.4.1 View tenant assets
  - 3.5 Use the Logs module
    - 3.5.1 View the information on the Overview page
    - 3.5.2 Query log details
    - 3.5.3 Query raw logs
    - 3.5.4 View platform logs
    - 3.5.5 View tenant logs
    - 3.5.6 Log configurations
      - 3.5.6.1 Manage log sources
      - 3.5.6.2 Configure a log parsing template
      - 3.5.6.3 Configure log forwarding
  - 3.6 Use the Reports module
  - 3.7 Use the Tasks module
  - 3.8 Use the Rules module
    - 3.8.1 Create an analysis rule
    - 3.8.2 Alert rules
  - 3.9 Use the Operations module
    - 3.9.1 Add custom IP addresses and modify the SOC location configuration
    - 3.9.2 Manage organization authorization

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

## 3 Security Operations Center (SOC)

**(SOC)**

### 3.1 Threat monitoring

Security administrators can use the threat monitoring feature to understand the overall security of a network. This topic describes how to use the threat monitoring feature.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Threat Monitoring**.
4. In the upper-right corner of the **Threat Monitoring** page, select values from the drop-
down lists to view the required network security information. You can select **Platform and All Organizations**, **All Organizations**, **Platform**, or
**Organization** from the drop-down list on the left.
You can select **Today**, **Last 24 Hours**, **Last 7 Days**, or **Last 30 Days** from the dropdown list on the right.
5. View the overall network security information within a specified time range.

| Section | Description |
|---|---|
| Global Security Situation | This section displays the statistics on security risks from the perspective of global security management. The following list describes the modules in this section: Total Organizations: displays the total number of organizations within the specified organization scope. Risk Index: displays the statistics on global risk indicators based on threat events and at-risk assets within an organization. Trend of Risk Indexes: displays the trend of risk indicators within a specified time range. The trends of risk indicators within the current day and last day are calculated by hour. The trends of risk indicators within the last 7 days and last 30 days are calculated by day. Organization Risks: displays the statistics on top 5 at-risk organizations, assets of top 5 at-risk organizations, and threat events of top 5 at-risk organizations. Asset Information: displays the total number of assets, the asset protection rate, and the proportions of high-risk, medium-risk, low-risk, and risk-free assets. Threat Events: displays the total number of threat events and the number of threat events at each risk level. The information about external risk sources and attack sources is displayed on maps. The world map and China map are supported. |

| Asset Risk Situation | This section displays the statistics on the asset risk situation from the perspective of asset risk management. The following list describes the modules in this section: Asset Distribution by Risk Level: displays the distribution of assets at the high-risk, medium-risk, low-risk, and risk-free levels. Trend of Asset Risks: displays the trend in the number of at-risk assets. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Top 5 Security Vulnerability Risks: displays the top 5 asset vulnerabilities. Top 5 Security Baseline Risks: displays the top 5 asset baseline risks. Top 5 At-risk Assets: displays the top 5 at-risk assets, including the risk indicators, threat events, network attacks, suspicious behaviors, vulnerabilities, and baseline risks of the assets. |
|---|---|
| Threat Situation | This section displays the statistics on the threat event situation from the perspective of threat event management. The following list describes the modules in this section: Threat Event Distribution by Level: displays the distribution and statistics of threat events at the emergency, serious, suspicious, moderate, and information levels. Trend of Threat Events: displays the trend in the number of threat events. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Threat Event Distribution by Type: displays the distribution and statistics of threat events in the exception, malware, unauthorized privilege escalation, vulnerability exploitation, and risk connection types. ATT&CK Attack Behavior: displays the statistics on ATT&CK involved in threat events. Top 10 Threat Events: displays the number of times that the top 10 threat events are detected. Threat Event Distribution by Attack Chain: displays the attack phases involved in threat events and the number of times that the threat events are detected. Attack phases include payload delivery, vulnerability exploitation, webshell insertion, command control, scan extension, privilege escalation, and target attack. |

| Handling and Response Posture Note If you want to view data in the Handling and Response Posture section, you must have permissions on Security Orchestration Automation Response (SOAR). | This section displays the statistics on the handling and response posture from the perspective of handling and response management. The following list describes the modules in this section: Total SOAR Handled Entities: displays the total number of entities handled by SOAR. Automatic Response Quantity: displays the number of automatic responses. Total Handling Tasks: displays the total number of handling tasks. Playbook Executions: displays the number of playbook executions. Enabled Playbooks/Total Playbooks: displays the number of enabled playbooks and the total number of playbooks. Trend of SOAR Handled Entities: displays the trend in the number of entities handled by SOAR. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Latest SOAR Handled Entities: displays the top 5 entities handled by SOAR. Top 5 Organizations with Highest Handling Task Completion Rate: displays the top 5 organizations that have the highest handling task completion rate and displays the task completion rate and on-time task completion rate for each organization. Automatic Response Distribution by Type: displays the trends in the number of automatic responses by type. The trends within the current day and last day are calculated by hour. The trends within thel ast 7 days and last 30 days are calculated by day. Playbook Running Trend: displays the playbook execution trend. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Top 5 Executed Playbook: displays the top 5 executed playbooks. |
|---|---|

### 3.2 Use the Operations Center module

**module**

The Operations Center module provides alert data in security services provided by Apsara Stack Security. The Operations Center page provides the Network Risk View and Host Risk View tabs. Security administrators can use the module to obtain information about network attacks and defenses. This helps improve network security. This topic describes how to view data in the Operations Center module.

**View data in the network risk view**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. On the **Network Risk View** tab, view the following data.

| Section | Description |
|---|---|
| View setting (marked 1 in the following figure) | In this section, you can specify the types of data that you want to view on the Operations Center page. You can perform the following operations: Select the required data types: Select options from the Select Statistic Window drop-down list. By default, the following options are selected: Alert data, Distribution of Alert Handling Methods, ECS Instance Protection, Risk Level, Distribution of Alerting Data Sources, Distribution of Alert Types, Top 10 Attacking IP Addresses, Top 10 Attacked IP Addresses, Top 5 Attacked Websites, and List display area. Save the view: Click the icon to save the current view. Manually refresh data: Click the icon to manually refresh the data in the current view. Enable automatic refresh: Turn on . The system automatically refreshes the data in the current view every 5 minutes. Export data: Click the icon to export the data in the current view. |
| Search condition setting (marked 2 in the following figure) | In this section, you can specify conditions to search for data. You can specify different search conditions based on your business requirements. For example, you can specify the query time range, data source, query scope, risk level, attack source, source IP address or destination IP address of an alert, the type or name of an alert, or the asset on which an alert is generated as a search condition. |
| Search result display (marked 3 in the following figure) | In this section, Security Operations Center (SOC) displays the search results that meet the specified data types and search conditions. |

| List display (marked 4 in the following figure) | In this section, SOC displays the details of threats in a list based on the data types and search conditions that you specify. The details include the occurrence time, attack source, alert name, alert type, risk level, and data source. You can also perform the following operations to manage the details of threats: Configure the data display mode. Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the alerts that have the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. Click Details in the Actions column of an alert to go to theD etails panel to view the details of the alert. Click the icon to refresh the data in the list. Click the icon to configure the items that you want to view in the list. By default, all items are selected and displayed in the list. Deliver a handling task: Select one or more alerts and click Batch Deliver Handling Tasks. You can also click More in the Actions column of an alert and select Deliver Handling Task. In the Create Task panel, configure parameters and click OK. Note If the alerts are aggregated, click next to an alert to expand the alert list. Create a response policy: Click More in the Actions column of an alert and select Create Response Policy. In the Create Policy panel, configure parameters and click OK. |
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

| View setting (marked 1 in the following figure) | In this section, you can specify the types of data that you want to view on the Operations Center page. You can perform the following operations: Select the required data types: Select options from the Select Statistic Window drop-down list. By default, the following options are selected: Alert data, ECS Instance Protection, Risk Level, Distribution of Alert Types, Top 10 Attacked IP Addresses, and List display area. Save the view: Click the icon to save the current view. Manually refresh data: Click the icon to manually refresh the data in the current view. Enable automatic refresh: Turn on . The system automatically refreshes the data in the current view every 5 minutes. Export data: Click the icon to export the data in the current view. |
|---|---|
| Search condition setting (marked 2 in the following figure) | In this section, you can specify conditions to search for data. You can specify different search conditions based on your business requirements. For example, you can specify the query time range, handling status, data source, query scope, risk level, attack source, source IP address or destination IP address of an alert, the type or name of an alert, or the asset on which an alert is generated as a search condition. The data source is fixed as Sever Guard. |
| Search result display (marked 3 in the following figure) | In this section, SOC displays the search results that meet the specified data types and search conditions. |

| List display (marked 4 in the following figure) | In this section, SOC displays the details of threats in a list based on the data types and search conditions that you specify. The details include the occurrence time, attack source IP address, alert name, alert type, risk level, and data source. You can also perform the following operations to manage the details of threats: Configure the data display mode. Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the alerts that have the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. Click Details in the Actions column of an alert to go to theD etails panel to view the details of the alert. Click the icon to refresh the data in the list. Click the icon to configure the items that you want to view in the list. By default, all items are selected and displayed in the list. Deliver a handling task: Select one or more alerts and click Batch Deliver Handling Tasks. You can also click More in the Actions column of an alert and select Deliver Handling Task. In the Create Task panel, configure parameters and click OK. Note If the alerts are aggregated, click next to an alert to expand the alert list. Create a response policy: Click More in the Actions column of an alert and select Create Response Policy. In the Create Policy panel, configure parameters and click OK. |
|---|---|

**Create a custom risk view**

By default, the Operations Center page provides the Network Risk View and Host Risk View tabs. You can also create a custom risk view.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. In the upper-right corner of the **Operations Center** page, click **Select Statistics**
**Window**, select data types for the custom risk view that you want to create, and then click
the icon.
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
| Search condition (marked 1 in the preceding figure) | In this section, you can specify search conditions for threat events. You can specify the query time range, scope, threat level, threat type, attack phase, threat name, and source or destination IP address to search for threat events. | Select options from drop-down lists or enter keywords in the search box, and click the icon. If you do not specify search conditions, all threat events are automatically displayed. Note If you select Organization from the Scope drop-down list, you can select one or more organizations from the Organization drop-down list. You can select one or more options from the Threat Level, Threat Type, and Attack Phase drop- down lists. |
|   |   | Click the name of a threat event or click Details in the Actions column of a threat event. On the details page of the threat event, view the information on the Threat Details and Evidence Details tabs. Click the icon to refresh the threat event list. Click the icon to export the threat event list. Handle a threat event: Click Handle in the Actions column of a threat event. In the Handle panel, perform the interactive handling operation and view the handling records. Deliver a handling task: Select one or more threat events and click Batch Deliver Handling Tasks. You can also click More in the Actions column of a threat event and select Deliver Handling Task. In the Create Task panel, configure parameters and click OK. |

| Search result (marked 2 in the preceding figure) | In this section, you can view the information about threat events that meet the specified search conditions. | Create a response policy: Click More in the Actions column of a threat event and select Create Response Policy. In the Create Policy panel, configure parameters and click OK. View threat tracing details: Find a threat event for which a tracing diagram is generated, and click the icon next to a threat name to go to the Threat Tracing page. On this page, view the threat tracing details. |
|---|---|---|
|   |   | Click the icon or the icon to zoom in or out the tracing diagram. Click the icon to download the tracing diagram to your computer. Click the icon to configure the Node layout and Node Distance parameters. Click the icon to refresh the tracing diagram. |

On the **Threat Details** tab, view the following parameters: **Start Time**, **Last Detected**
**At**, **Analytic Rules**, **Network Protocol**, **Threat Intelligence**, **Source Information**,
**Destination Information**, and **Key Information**.
Click the rule ID next to **Analytic Rules** to view more information about the rule that detects the threat. Click **Generate Case** to generate a case for the current threat event on the **Case**
**Management** page of the **SOAR** console. This helps monitor and handle this threat
event. On the **Evidence Details** tab, view the raw logs of the threat event. You can click **Details** in the Actions column of a raw log to view the details of the raw log, including alert information. The content that matches an associated analysis rule is highlighted.

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
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center**. On the **Security Operations Center** page, select a region
from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Vulnerability Analytics**.
4. On the **Platform** or **Tenant** tab of the page that appears, view the vulnerabilities and
baselines.

**Platform**

**Vulnerabilities**

On the Vulnerabilities tab, you can view the following information about a vulnerability: Vulnerability Name, Vulnerability Type, Priority Score, CVE ID, Affected Assets, Vulnerability Level, Last Detected At, and Organization. You can specify search conditions to search for vulnerabilities.

> **Note:** If you do not specify search conditions, all vulnerabilities are displayed by default.

| Search condition | Description |
|---|---|
| Time range | The time range of data to query. Valid values: Today, Last 24 Hours, Last 7 Days, Last 30 Days, and Custom. |
| Vulnerability type | The type of the vulnerabilities. Valid values: All, Linux Software, Windows System, Web CMS, and Application (Urgent Vulnerability Included). |
| Vulnerability level | The severity of the vulnerabilities. Valid values: All, High, Medium, and Low. |
| Search by vulnerability name or Common Vulnerabilities and Exposure (CVE) ID | The keyword that is used to search for vulnerabilities. The keyword can be a vulnerability name or a CVE ID. Fuzzy match is supported. |

All search results are displayed in the vulnerability list. You can perform the following operations based on your business requirements: Click the icon to refresh the vulnerability list. Click the icon to export the vulnerability list. Click the name of a vulnerability or click **Details** in the **Actions** column of a vulnerability to view the vulnerability details and affected assets. On the **Vulnerability**
**Details** tab of the vulnerability details panel, click the CVE ID of a vulnerability to view
the details of the vulnerability and the suggestions on how to fix the vulnerability. On the **Scanned Asset** tab, click the name of an affected asset to go to the **Platform**
**Assets** page. On the Platform Assets page, you can view information about the
affected asset. Create a response policy: Click **More** in the Actions column of a vulnerability and select
**Create Response Policy**. In the **Create Policy** panel, configure parameters and click
**OK**.
Deliver a handling task: Select one or more vulnerabilities and click **Batch Deliver**
**Handling Tasks**. You can also click **More** in the Actions column of a vulnerability and
select **Deliver Handling Task**. In the **Create Task** panel, configure parameters and click **OK**. Add vulnerabilities to the whitelist: Select one or more vulnerabilities and click **Add to**
**Whitelist**. In the **Prompt** dialog box, enter remarks and click **OK**.

**Baselines**

On the Baselines tab, you can view the following information about a baseline: Baseline Name, Risk Type, Risk Level, Affected Asset, Last Detected At, and Organization. You can specify search conditions to search for baselines.

> **Note:** If you do not specify search conditions, all baselines are displayed by default.

| Search condition | Description |
|---|---|
| Time range | The time range of data to query. Valid values: Today, Last 24 Hours, Last 7 Days, Last 30 Days, and Custom. |
| Risk type | The risk type of the baselines. Valid values: hierarchy protection Unauthorized Access Internationally Agreed Best Practices for Security Custom baseline Best security practices Weak password Container security Data Security Access Control Monitoring Alarms Disaster Recovery Backup Log Audit Authentication Security Network Configuration |
| Risk level | The severity of the baselines. Valid values: All, High, Medium, and Low. |
| Baseline name | The name of the baseline. |

All search results are displayed in the baseline list. You can perform the following operations based on your business requirements: Click the icon to refresh the baseline list. Click the icon to export the baseline list. Click the name of a baseline or click **Details** in the **Actions** column of a baseline to view the affected assets. Deliver a handling task: Select one or more baselines and click **Batch Deliver**
**Handling Tasks**. You can also click **More** in the Actions column of a baseline and
select **Deliver Handling Task**. In the **Create Task** panel, configure parameters and click **OK**. Create a response policy: Click **More** in the Actions column of a baseline and select
**Create Response Policy**. In the **Create Policy** panel, configure parameters and click
**OK**.

> **Note:** We recommend that you handle the risks based on the risk description provided by Security Operations Center (SOC).

**Tenant**

**Vulnerabilities**

On the Vulnerabilities tab, you can view the following information about a vulnerability: Vulnerability Name, Vulnerability Type, Priority Score, CVE ID, Affected Assets, Vulnerability Level, Last Detected At, and Organization. You can specify search conditions to search for vulnerabilities.

> **Note:** If you do not specify search conditions, all vulnerabilities are displayed by default.

| Search condition | Description |
|---|---|
| Scope | The organization whose risks you want to query. |
| Time range | The time range of data to query. Valid values: Today, Last 24 Hours, Last 7 Days, Last 30 Days, and Custom. |
| Vulnerability type | The type of the vulnerabilities. Valid values: All, Linux Software, Windows System, Web CMS, and Application (Urgent Vulnerability Included). |
| Vulnerability level | The severity of the vulnerabilities. Valid values: All, High, Medium, and Low. |

| Vulnerability name | The keyword that is used to search for vulnerabilities. The keyword can be a vulnerability name or a CVE ID. Fuzzy match is supported. |
|---|---|

All search results are displayed in the vulnerability list. You can perform the following operations based on your business requirements: Click the icon to refresh the vulnerability list. Click the icon to export the vulnerability list. Click the name of a vulnerability or find a vulnerability and choose **More** > **Details** in the **Actions** column to view the vulnerability details and affected assets. On the
**Vulnerability Details** tab of the vulnerability details panel, click the CVE ID of a
vulnerability to view the details of the vulnerability and the suggestions on how to fix the vulnerability. On the **Scanned Asset** tab, click the name of an affected asset to go to the **Tenant Assets** page. On the Tenant Assets page, you can view information about the affected asset.

> **Note:** You can view the result of a vulnerability fix on the **Scanned Asset** tab.

Deliver a handling task: Select one or more vulnerabilities and click **Batch Deliver**
**Handling Tasks**. You can also click **More** in the Actions column of a vulnerability and
select **Deliver Handling Task**. In the **Create Task** panel, configure parameters and click **OK**. Create a response policy: Click **More** in the Actions column of a vulnerability and select
**Create Response Policy**. In the **Create Policy** panel, configure parameters and click
**OK**.
Add vulnerabilities to the whitelist: Select one or more vulnerabilities and click **Add to**
**Whitelist**. In the **Prompt** dialog box, enter remarks and click **OK**.
Fix multiple vulnerabilities at a time: Select one or more vulnerabilities and click **Batch**
**repair** in the lower part of the vulnerability list. You can also click **Repair** in the
Actions column of a vulnerability. In the **Batch repair** dialog box, select **I have**
**understood the risk of repair failure.** and click **Repair now**.

**Baselines**

On the Baselines tab, you can view the following information about a baseline: Baseline Name, Risk Type, Risk Level, Affected Asset, Last Detected At, and Organization. You can specify search conditions to search for baselines.

> **Note:** If you do not specify search conditions, all baselines are displayed by default.

| Search condition | Description |
|---|---|
| Scope | The organization whose risks you want to query. |

| Time range | The time range of data to query. Valid values: Today, Last 24 Hours, Last 7 Days, Last 30 Days, and Custom. |
|---|---|
| Risk type | The risk type of the baselines. Valid values: hierarchy protection Unauthorized Access Internationally Agreed Best Practices for Security Custom baseline Best security practices Weak password Container security Data Security Access Control Monitoring Alarms Disaster Recovery Backup Log Audit Authentication Security Network Configuration |
| Risk level | The severity of the baselines. Valid values: All, High, Medium, and Low. |
| Baseline name | The name of the baseline. |

All search results are displayed in the baseline list. You can perform the following operations based on your business requirements: Click the icon to refresh the baseline list. Click the icon to export the baseline list. Click the name of a baseline or click **Details** in the **Actions** column of a baseline to view the baseline details, including **Affected Asset**, **Resource Set**, and
**Organization**. Click the name of an affected asset to go to the **Tenant Assets** page.
On the Tenant Assets page, you can view information about the affected asset. Deliver a handling task: Select one or more baselines and click **Batch Deliver**
**Handling Tasks**. You can also click **More** in the Actions column of a baseline and
select **Deliver Handling Task**. In the **Create Task** panel, configure parameters and click **OK**. Create a response policy: Click **More** in the Actions column of a baseline and select
**Create Response Policy**. In the **Create Policy** panel, configure parameters and click
**OK**.

> **Note:** We recommend that you handle the risks based on the risk description provided by SOC.

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
5. Specify search conditions to search for baselines.

> **Note:** If you do not specify search conditions, all baselines of cloud services are displayed by default.

| Search condition | Description |
|---|---|
| Baseline application scope | The application scope of the baseline. Valid values: Tenant and Platform. |
| Baseline type | The type of the baseline. Valid values: Security protection, Identity authentication, Access control, Network Configuration, Data Security, Disaster Recovery Backup, Log Audit, and Monitoring alarms. |
| Risk level | The risk level of the baseline. Valid values: High, Medium, and Low. |
| Baseline name | The name of the baseline. You can enter a baseline name in the search box and click the icon to search for the baseline. |

6. On the **Cloud Service Check** page, view information about the baselines of cloud services.
The information includes baseline risk items, affected assets, enabled baseline check items, disabled baseline check items, and the time when the check was last performed.
7. Perform a cloud service check.
Manual check Click **Check Now**. The system starts a full check on the configurations of all services to detect risks and affected assets. During the check, you can click **View** to view the check progress in the **Check Item Detection** dialog box.

> **Note:** Do not perform other operations until the check is complete.

Automatic check Click **Check Settings** to configure a check policy. The following table describes the required parameters.

| Parameter | Description |
|---|---|
| Check Cycle | The days of the week on which you want to run an automatic check. Valid values range from Monday to Sunday. You can select multiple days of the week. |
| Checked At | The time range during which you want to run an automatic check. Valid values: 24:00 - 06:00, 06:00 - 12:00, 12:00 - 18:00, and 18:00 - 24:00. You can select only one time range. |
| Select Resource Set | The resource sets that you want to check. |
| Baseline Check Item | The baselines that you want to use. |

After you configure the check policy, Security Operations Center (SOC) automatically performs a check based on all specified baselines within the specified time range.
8. View check data.
In the baseline list, view the following information about baselines: Cloud Product Baseline, Baseline Category, Baseline Type, Risk Level, Affected assets, Last Checked At, and Status. Find a baseline and click its name or click **Details** in the **Actions** column. In the panel that appears, view data on the Baseline Check Details and Cloud Service Instances tabs. If an organization or instance is riskless, you can select and add the organization or instance to the whitelist. Find a baseline and click **Verify** in the **Actions** column, or select one or more baselines and click **Verify** below the baseline list to verify that the detected baseline risks are fixed. During the verification, you can click **View** in the Actions column of the baseline to view the verification progress. You can click **Cancel Verification** in the Actions column of the baseline to cancel the verification.

#### 3.3.5 View attack surface assessment results

This topic describes how to view attack surface assessment results.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis** > **Attack Surface Assessment**.
4. In the upper-right corner of the **Attack Surface Assessment** page, select the organization
or platform that you want to view.
5. On the **Attack Surface Assessment** page, view the statistics of exposed attack surfaces.
**Shadow IP addresses Within Last 30 Days** : A shadow IP address outside the cloud is
an IP address of an asset that can communicate with the cloud platform but is not managed by the cloud platform. The asset can be unauthorized software, an unapproved hardware device, a cloud service, or a third-party application. This type of asset is not managed by the cloud platform and may cause unknown risks or threats. Attackers can use a shadow IP address to attack assets in the cloud.
**Vulnerable Security Group**: A vulnerable security group is a security group that allows
inbound traffic from IP addresses in a loose manner. To implement the principle of least privilege, we recommend that you delete security group rules that allow inbound traffic from unnecessary IP addresses. An unnecessary IP address refers to an IP address that is not required in your workloads. This helps reduce exposure at the network layer.
**Exposed Asset**: An exposed asset is an Elastic Compute Service (ECS) instance that is
accessible from outside the cloud platform and involved in a known attack path.
**At-risk Account**: An at-risk account is an account that uses a weak password and can
be used to log on to assets in the cloud from outside the cloud. If the account is leaked, attackers can intrude assets in the cloud with ease.
**Risk Level of Attack Surface** : The risk level of the attack surface for the specified
organization or platform is determined after a comprehensive evaluation is performed. The risk level can be Low, Medium, High, and Critical.
6. View the details of each risk on the corresponding tab.
**Attack Surface**: This tab displays the statistics on attack paths and core assets affected
by the attack paths. You can view the following information about an attack path: **Path**
**Name**, **Path Risk Score**, **Affected Core Assets**, and **Assets in Path**.
You can perform the following operations: Click the icon. In the **Attack Path Configuration** dialog box, configure the **Risk**
**Score for Attack Path Filtering** and **Start Time for Attack Path** parameters.
Click **Panorama View** to view the network topologies of all attack paths. Click the name of an attack path or click **View Attack Path** in the Actions column of an attack path to view the network topology of the attack path.

> **Note:** You can click **2D Mode** or **3D Mode** in the details page of an attack path to switch the view mode.

**Shadow IP Address Outside Cloud**: This tab displays **shadow IP addresses outside**
**the cloud** in a list. You can perform the following operations:
Click an IP address to view the details of the IP address, including the **geographical**
**location**, **cloud-connected assets**, **handling status**, **time when the IP address**
**was first detected, time when the IP address was last detected**, **inbound**
**cloud-connected assets**, **destination IP address**, and **inbound traffic**.
Click **Handle** in the **Actions** column of an IP address to perform the **interactive**
**handling operation** and view the **handling records**.
**Interactive Handling**: Click
next to the Handling Entity column, select a **scenario** and select a value from the **Applicable Scope** drop-down list and a value from the
**Action Validity Period** drop-down list to block an entity.
**Handling Records**: Click **Details** in the Actions column of a handling record to view
the details of the handling record.
**Vulnerable Security Group**: This tab displays vulnerable security groups in a list. You
can click the name of a security group or click **Details** in the Details column of a security group to view details of the security group, including**VPC ID**, **Security Group Type**,
**Organization**, **Resource Set**, **Description**, and **Instances Within Security Group**.
**Exposed Asset**: This tab displays the ECS instances that can be directly accessed from
outside the cloud platform in a list. You can click the name of an asset to view the basic information about the asset and the security vulnerabilities that the asset suffers.
**At-risk Account**: This tab displays risky accounts in a list. You can click the name of an
asset to go to the asset details page. On this page, you can view **Basic Information**,
**Business Information**, and **Asset Fingerprints**.

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
| Search condition (marked 2 in the preceding figure) | In this section, you can specify search conditions to search for traffic analysis data. You can specify search conditions based on your business requirements. You can specify the time range, query scope, application, source IP address, destination IP address, source port, and destination port. |
| Search result (marked 3 in the preceding figure) | In this section, Security Operations Center (SOC) displays the search results that meet the specified search conditions. |

### 3.4 Asset Management

#### 3.4.1 View tenant assets

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

| Asset Risks | Risk Level You can view the risk assessment data of the asset, including the asset risk index, network attack risks, suspicious process risks, vulnerability risks, and security baseline risks. You can view the distribution of network attacks, suspicious behavior, vulnerabilities, and baselines by risk level. You can also view the trend of network attacks within the last seven days. You can view the following information: top 5 network attack risks, top 5 suspicious process risks, top 5 security vulnerability risks, and top 5 security baseline risks. Network Attacks: You can view and handle network attacks on the asset. Suspicious Processes: You can view and handle the suspicious behavior that affects the asset. Vulnerabilities: You can view the details of vulnerabilities in the asset and fix the vulnerabilities based on the provided suggestions. Fix a vulnerability: Click a number or a server in the Vulnerabilities column to go to the Vulnerabilities tab of the Asset Risks tab. On the Vulnerabilities tab, find a vulnerability and click Repair in the Actions column. In the Batch repair dialog box, select I have understood the risk of repair failure. and click Repair now. Baselines: You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. Handle a baseline risk: Click a number or a server in the Baselines column to go to the Baselines tab of the Asset Risks tab. On the Baselines tab, find a baseline risk and click Handle in the Actions column. In the Ok message, click OK. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |
|---|---|

**ApsaraDB RDS**

| Tab | Description |
|---|---|
| Asset Information | Basic information: You can view the basic information about the ApsaraDB RDS instance in the Basic Information section. Network Information: You can view the tunnel information about the ApsaraDB RDS instance in the Tunnel section. Security policy: You can view the whitelist of the ApsaraDB RDS instance in the Whitelist information section. |

| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
|---|---|
| Asset Risks | You can view the baseline risks in the asset and handle the risks based on the provided suggestions. |

**OSS**

| Tab | Description |
|---|---|
| Asset Information | You can view the basic information about the OSS bucket. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | You can view the baseline risks in the OSS bucket and handle the risks based on the provided suggestions. |

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

| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
|---|---|
| Asset Risks | You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. |

**Servers Outside Cloud**

| Tab | Description |
|---|---|
| Asset Information | Basic information: You can view the basic information and network information about the asset. Security policy: You can view the security logon settings. |
| Asset Fingerprints | You can view fingerprint information on the Port, Software, Process, Account, Planned tasks, Middleware, and Startup Item tabs. |

| Asset Risks | Risk Level You can view the risk assessment data of the asset, including the asset risk index, network attack risks, suspicious process risks, vulnerability risks, and security baseline risks. You can view the distribution of network attacks, suspicious behavior, vulnerabilities, and baselines by risk level. You can also view the trend of network attacks within the last seven days. You can view the following information: top 5 network attack risks, top 5 suspicious process risks, top 5 security vulnerability risks, and top 5 security baseline risks. Suspicious Processes: You can view and handle the suspicious behavior that affects the asset. Vulnerabilities: You can view the details of vulnerabilities in the asset and fix the vulnerabilities based on the provided suggestions. Fix a vulnerability: Click a number or a server in the Vulnerabilities column to go to the Vulnerabilities tab of the Asset Risks tab. On the Vulnerabilities tab, find a vulnerability and click Repair in the Actions column. In the Batch repair dialog box, select I have understood the risk of repair failure. and click Repair now. Baselines: You can view the baseline risks in the asset and handle the baseline risks based on the provided suggestions. Handle a baseline risk: Click a number or a server in the Baselines column to go to the Baselines tab of the Asset Risks tab. On the Baselines tab, find a baseline risk and click Handle in the Actions column. In the Ok message, click OK. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |
|---|---|

Click the icon to refresh the asset list. Click the icon to export the asset information. Click the icon to configure the items that you want to view in the asset list.

### 3.5 Use the Logs module

#### 3.5.1 View the information on the Overview page

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

#### 3.5.2 Query log details

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

#### 3.5.3 Query raw logs

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

#### 3.5.4 View platform logs

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

#### 3.5.5 View tenant logs

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

#### 3.5.6 Log configurations

##### 3.5.6.1 Manage log sources

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

##### 3.5.6.2 Configure a log parsing template

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

##### 3.5.6.3 Configure log forwarding

Security Operations Center (SOC) provides the log forwarding feature. Security administrators can forward logs based on their business requirements and view logs at the earliest opportunity. You can specify multiple log sources for a log forwarding task. You can also forward logs that belong to specified organizations. This topic describes how to configure a log forwarding task.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Configurations**.
4. On the **Log Forwarding** tab, click **Create Forwarding Task**. In the panel that appears,
configure the following parameters and click **OK**.

> **Note:** You can set the Data Protocol parameter to Syslog or Kafka.

**Syslog**

| Parameter | Description |
|---|---|
| Task Name | The name of the forwarding task. The name must be 0 to 64 characters in length. |
| IP:Port | The IP address, port number, and protocol that are used for log forwarding. The protocol supports User Datagram Protocol (UDP) and Transmission Control Protocol (TCP). |

| Organization | The organization to which the logs are forwarded. Valid values: Platform and All Organizations. Platform. All Organizations. Organization: If you select this option, select one or more organizations from the Organization drop-down list. |
|---|---|
| Select Log Source | Select one or more types of log sources in theL og Source section and click the icon to add the selected log sources to theS elected Log Sources section. |
| Forwarding Status | Turn on or turn off the switch to enable or disable the log forwarding feature. |

**Kafka**

| Parameter | Description |
|---|---|
| Task Name | The name of the forwarding task. The name must be 0 to 64 characters in length. |
| Service Address | The IP address and port number that are used for log forwarding. |
| Topics | The list of Kafka topics. Separate multiple Kafka topics with commas (,). |
| Authentication | Specifies whether a Kafka cluster requires authentication. If the Kafka cluster requires authentication, click the icon to turn on the switch and configure the following parameters. Protocol type: Select SASL PLAINTEXT from the drop-down list. _ SASL Authentication: Select PLAIN, SCRAM-SHA-256, or SCRAM-SHA- 512 from the drop-down list. Username/Password: Enter the username and password that are used to access the Kafka cluster. |
| Organization | The organization to which the logs are forwarded. Valid values: Platform and All Organizations. All Organizations. Platform. Organization: If you select this option, select one or more organizations from the Organization drop-down list. |

| Select Log Source | Select one or more types of log sources in theL og Source section and click the icon to add the selected log sources to theS elected Log Sources section. |
|---|---|
| Forwarding Status | Turn on or turn off the switch to enable or disable the log forwarding feature. |

To create multiple log forwarding tasks, repeat the preceding steps. After you create a log forwarding task, you can view and manage the log forwarding task in the log forwarding task list. You can filter log forwarding tasks by **scope** or **task name**. You can **turn on** or **turn off** the switches in the Status column to enable or disable log forwarding. You can **modify** or **delete** a log forwarding task.

### 3.6 Use the Reports module

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

### 3.7 Use the Tasks module

On the Tasks page, you can analyze and handle global security risks in a streamlined process. This facilitates security operations and management and helps accumulate experience in handling risks. This topic describes how to manage tasks on the Tasks page.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Handle > Tasks**.
4. On the Tasks page, view the overall information about tasks.
Total Tasks: the total number of tasks in Security Operations Center (SOC). The number is counted from the time when SOC starts to run until the current point in time. Tasks Pending Handling, Tasks Being Handled, and Handled Tasks: the number of tasks that are pending, the number of tasks that are being handled, and the number of tasks that are handled. The numbers are counted from the time when SOC starts to run until the current point in time. Task Completion Rate and On-time Task Completion Rate: the proportion of tasks that are completed to all tasks and the proportion of tasks that are completed on time to all tasks. The proportions are measured from the time when SOC starts to run until the current point in time. Handling Solutions: the number of handling solutions that are published from the time when SOC starts to run until the current point in time. The solutions include solutions that are manually created and solutions that are synchronized from handling records. Create solutions Click **Handling Solutions**. On the page that appears, click **Create Solution**. In the panel that appears, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Solution Name | Enter the name of the handling solution. The name must be 0 to 200 characters in length. |
| Organization | Select the organization to which the handling solution is delivered. Valid values: Platform and All Organizations. Platform. All Organizations. Organization: If you select this option, select one or more organizations from the Organization drop-down list. |
| Solution Type | Select the type of the handling solution. Valid values: Threat Event: You can click Select Risk Record to select a threat event within your data permission scope. Security alert: You can click Select Risk Record to select a security alert within your data permission scope. Vulnerabilities: You can click Select Risk Record to select a vulnerability within your data permission scope. Baselines: You can click Select Risk Record to select a security baseline within your data permission scope. Asset Risks: You can click Select Risk Record to select an asset within your data permission scope. Security Inspection |
| Problem Description | Enter the problem description of the handling solution. The description must be 0 to 1,024 characters in length. |
| Solution | Specify the handling solution. The value must be 0 to 2,048 characters in length. |
| Handled By | Select a contact from the contact drop-down list or enter a custom contact, which must be 0 to 8 characters in length. |

Synchronize solutions from handling records: For more information, see Handle a task. A manually created solution is in the **Published** state. You can directly reference the solution. A solution synchronized from handling records is in the **Pending Approved** state. You must **approve** the solution to reference the solution. After you reference the solution, you can **disable** the solution. You can also **delete** or **modify** a solution.
5. Click **Create Task**, configure the parameters, and then click **OK**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Name | Enter the name of the task. The name must be 0 to 128 characters in length. |
| Delivering Organization | Select the organization to which the task is delivered. Valid values: Platform and All Organizations. Platform. All Organizations. Organization: If you select this option, select one or more organizations from the Organization drop-down list. |
| Task Type | Select the type of the task. Valid values: Threat Event: You can click Select Risk Record to select one or more threat events within your data permission scope. Security alert: You can click Select Risk Record to select one or more security alerts within your data permission scope. Vulnerabilities: You can click Select Risk Record to select one or more vulnerabilities within your data permission scope. Baselines: You can click Select Risk Record to select one or more baselines within your data permission scope. Asset Risks: You can click Select Risk Record to select one or more assets within your data permission scope. Security Inspection |
| Priority | Select the priority of the task. Valid values: Urgent, High, Medium, and Low. |
| Problem Description | Enter the problem description of the task. The description must be 0 to 1,024 characters in length. |
| Handling Suggestion | Enter handling suggestions for the task. The value must be 0 to 1,024 characters in length. You can select Referenced Solution and select one or more handling solutions from the drop-down list. |
| Handling Deadline | Specify the deadline for the task. If the task is not completed before the deadline, the handling status of the task changes to Timed Out. |
| Handled By | Select a contact from the contact drop-down list or enter a custom contact, which must be 0 to 8 characters in length. |
| Notification Method | Valid values: DingTalk and Mail. |

After the task is created, you can view the task in the task list. You can also handle all tasks. Search for a task Specify filter conditions to search for a task. You can specify the following filter conditions: Scope, Task Type, Priority, Task Status, Processing status, Task Name, and Handled By. Handle a task i. Find the task and click the task name or **Handling Details** in the **Actions** column. ii. On the Task Details page, turn on Received. Start to Handle. iii. Handle the task based on suggestions provided in the **Handling Suggestion** section and record the handling process in the **Handling Records** field. The value must be 0 to 2,048 characters in length.

> **Note:** When you enter a record, you can select **Synchronize to Handling** **Solutions**. If you encounter the same task later, you can directly reference the handling solution as the handling suggestion.
> A handling record that is synchronized to the knowledge base becomes a handling solution and is in the **Pending Approval** state. Before you can reference the handling solution, you must find the solution on the **Handling** **Solutions** page and click **Approve** or **Disable** in the **Operation** column.

After you handle a task, the task status changes from **In processing** to **Completed**. In this case, you can no longer **edit** the task.

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
|---|---|
| Threat Level | The level for the threat. Valid values: Information Suspicious Moderate Serious Urgent |
| Threat Type | The threat type. You can select multiple types for a threat. Valid values: Network Scanning Vulnerability Exploitation Malware Network Attack Suspicious Network Connection Privilege Escalation Suspicious Processes |
| ATT&CK ID | The IDs of one or more attacks that are involved in the Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) stages. |

| Rule Type | The type for the rule that you want to create. If you select Association-based Analysis Rule, you must configure the following parameters: Time Series: the time condition for the rule that you want to create. Valid values: Periodicity: The rule is used to detect the threats that occur within the same period of time. Chronological Order: The rule is used to detect the threats that occur in sequence. Associated Object: the object on which the rule is used to detect threats. The value is fixed as Same Asset. Trigger Condition: the trigger condition. You can configure the following parameters to specify the trigger condition: Association Type: specifies whether the associated condition is a required condition. Log Scope: the log sources, log types, log subtypes, and log levels. Source IP and Destination IP. Keyword: If you specify multiple keywords, separate them with semicolons (;). Time Period: Valid values: 0 to 1440. Unit: minutes. Log Quantity: the number of logs. Attack Phase: Valid values: Payload Delivery, Vulnerability Exploitation, Backdoor Installation, Command and Control, Scanning, Privilege Escalation and Action on Objectives. If you select Search-based Analysis Rule, you must configure the following parameters: Log Scope: the platform or organizations to which you want to apply the rule. Search Condition: the search conditions for the rule. Time Period: the time period of a rule. |
|---|---|
| Execution Period | The interval at which the rule is executed. Default value: 5. Unit: minutes. |
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

| Alert Condition | Select a value for Rule Type, which supports Threat Event, Alert, Vulnerability, and Baseline. Then, configure an alert condition based on the value. Threat Event: If you select this option, you must configure the Threat Event Name, Threat Event Severity, Threat Event Type, Attacker IP Address, Attacked IP Address, Scanned Asset, and Threat Behavior parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. Alert: If you select this option, you must configure the Alert Name, Alert Severity, Alert Type, Attack IP Address, Attack IP Address, and Scanned Asset parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. Vulnerability: If you select this option, you must configure the Vulnerability Name, Vulnerability Severity, Vulnerability Type, CVE ID, Scanned Asset, and Affected Asset parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. Baseline: If you select this option, you must configure the Baseline Name, Baseline Severity, Baseline Type, Scanned Asset, and Affected Asset parameters. Each of the parameters specifies a match condition, and different match conditions are evaluated by using the AND operator. |
|---|---|
| Notification Recipient | Select the contacts to which you want to send alerts. You can select only the contacts that are added in System Configurations ＞ Alert Settings. |
| Notification Method | Select the notification method that you want to use to send alerts. Valid values: DingTalk and Email. |
| Alerting Interval | Specify the interval at which you want to send alerts. You can specify a value that ranges from 0 to 1,440 minutes or a value that ranges from 0 to 168 hours. |

After the alert rule is created, the contacts that are specified in the alert rule receive alerts when threats are detected.

### 3.9 Use the Operations module

#### 3.9.1 Add custom IP addresses and modify the SOC location configuration

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

> **Note:** After you add the IP address, the default map of SOC changes.
> IP addresses in the Chinese mainland: By default, the map of China is displayed.
> IP addresses outside Chinese mainland: By default, a world map is displayed.
> Affected scopes:
> Threat events on the Threat Monitoring page

Global Security Situation Threat Situation The added IP address is displayed in the IP address list. You can perform the following operations based on your business requirements: Modify the IP address Find the IP address that you want to manage and click **Modify**. In the **Modify** dialog box, modify the Geographic Location parameter. Delete the IP address Find the IP address that you want to manage and click **Delete**. In the **Delete** message, click **OK**.

**Modify the location configuration of SOC**

The global security situation uses the geographical location that is configured for SOC. You can perform the following steps to modify the location configuration of SOC.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Operations > IP Address Library**.
4. In the upper-right corner of the **IP Address Library** page, click **Security Operations**
**Center Location Configuration**.
5. In the **Security Operations Center Location Configuration** dialog box, configure the
**Country**, **Province**, and **City** parameters and click **OK**.

#### 3.9.2 Manage organization authorization

This topic describes how to enable global organization service-linked role authorization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Operations > Organization Authorization**.
4. Turn on the switch next to **Global Organization SLR Authorization**. In the message that
appears, click **OK**. If Global Organization SLR Authorization is enabled, Security Operations Center (SOC) is automatically assigned the service-linked roles of all organizations, including organizations that are created in subsequent operations. SOC automatically collects information about the cloud assets and security data of all organizations. The global organization security administrator has the operations and management permissions on the cloud platform and cloud assets and security data of organizations. If Global Organization SLR Authorization is disabled, SOC is not assigned the servicelinked roles of the organizations. You must assign the service-linked role of at least one organization to SOC as an organization security administrator. Otherwise, the features of SOC are unavailable. After the service-linked role of the organization is assigned to SOC, SOC automatically collects information about the cloud assets and security data of the organization. The global organization security administrator has the operations and management permissions on the cloud platform and the organization.

> **Important:** Organization service-linked role authorization has a higher priority than global organization service-linked role authorization. If the number of organizations for which global organization service-linked role authorization is enabled is different from the total number of organizations, you must modify the service-linked role authorization for the organizations.
