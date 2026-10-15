---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 69
source_pdf: "cf584d602acc5f9e_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Ma"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center User Guide 20260828

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 云安全管理中心（SOC）
  - 3.1 Threat monitoring
  - 3.2 View data in the operations center
  - 3.3 Use the Risk Analysis module
    - 3.3.1 View threat events
    - 3.3.2 Use the threat investigation feature
    - 3.3.3 View attack surface assessment results
    - 3.3.4 View cloud service check data
    - 3.3.5 View vulnerability analysis results
    - 3.3.6 View traffic analysis results
  - 3.4 威胁情报
    - 3.4.1 Threat intelligence overview
    - 3.4.2 Query threat intelligence
  - 3.5 资产管理
    - 3.5.1 View tenant assets
  - 3.6 Use the Logs module
    - 3.6.1 View the information on the Overview page
    - 3.6.2 Log query
      - 3.6.2.1 Query log details
      - 3.6.2.2 Query raw logs
    - 3.6.3 View tenant logs
    - 3.6.4 Logging configurations
  - 3.7 Create and manage a task
  - 3.8 Report management
    - 3.8.1 Reports
    - 3.8.2 Report tasks
    - 3.8.3 Report templates
  - 3.9 Use the Rules module
    - 3.9.1 Create and manage an analysis rule
    - 3.9.2 Create a response policy
  - 3.10 Use the Operations module
    - 3.10.1 Manage organization authorization

## 1 Usage notes

Before you log on to Apsara Stack Security Center, you must verify that your computer meets the configuration requirements. For more information about the configuration requirements, see . Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 2 Quick start

### 2.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. All roles available in Apsara Stack Security are default roles. You cannot create custom roles. Before you log in to Apsara Stack Security, make sure that your account is assigned the required role. For more information, see the Default roles in Apsara Stack Security section of this topic. Table 1: Default roles in Apsara Stack Security

| Role name | Description |
|---|---|
| Organization security administrator | This role has the permissions to manage security services for an organization, such as Security Operations Center (SOC), and services for server security, application security, and network security. |
| Global organization security administrator | This role has the permissions to use SOC to manage security for all tenants. |
| Global organization security auditor | This role has the permissions to use SOC to check the security status of all organizations. |
| Custom role | This role has the permissions to customize the operations management permissions of all organizations, the current organization, subordinate organizations of the current organization, and resource sets. This role has the read and write permissions on service feature menus and can configure custom service feature menus. Note The current custom permissions of all organizations do not include the permissions on the Apsara Uni-manager Management Console. The permissions of a custom role are different from the data permissions of the global organization security administrator. |

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

**Note**

When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable**
**MFA** topic in **Apsara Uni-manager Operations Console User Guide** .

## 3 云安全管理中心（SOC）

### 3.1 Threat monitoring

Security administrators can use the threat monitoring feature to understand the overall security of a network. This topic describes how to use the threat monitoring feature.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Situation Monitoring**.
4. In the upper-right corner of the **Situation Monitoring** page, select values from the
**Organization** and time statistics drop-down lists to filter network security information.
You can select **All Organizations** or **Organization** from the **Organization** drop-down list. You can select **Today**, **Last 24 Hours**, **Last 7 Days**, or **Last 30 Days** from the dropdown list on the right.
5. View the overall network security information within a specified time range.

| Section | Description |
|---|---|
| Global Security Situation | This section displays the statistics on security risks from the perspective of global security management. This section includes the following modules: Total Organizations: displays the total number of organizations within the specified organization scope. Risk Index: displays the statistics on global risk indexes based on threat events and risky assets within an organization. Trend of Risk Indexes: displays the trend of risk indexes within the specified period of time. The trends of risk indexes within the current day and last day are calculated by hour. The trends of risk indexes within the last 7 days and last 30 days are calculated by day. Organization Risks: displays the statistics on the top 5 risky organizations, assets of the top 5 risky organizations, and threat events of the top 5 risky organizations. Asset Information: displays the total number of assets, asset protection rate, and proportions of high-risk, medium-risk, low-risk, and risk-free assets. Threat Events: displays the total number of threat events and the number of threat events at each risk level. The information about external risk sources and attack sources is displayed on maps. The world map and China map are supported. |

| Asset Risk Situation | This section displays the statistics on the asset risk situation from the perspective of asset risk management. This section includes the following modules: Asset Distribution by Risk Level: displays the distribution and statistics on high-risk, medium-risk, low-risk, and risk-free assets. Trend of Asset Risks: displays the trend in the number of risky assets. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Top 5 Security Vulnerability Risks: displays the top 5 asset security vulnerabilities. Top 5 Security Baseline Risks: displays the top 5 asset security baseline risks. Top 5 At-risk Assets: displays the top 5 risky assets, including the risk indexes, threat events, cyberattacks, abnormal behavior, security vulnerabilities, and security baseline risks of the assets. |
|---|---|
| Threat Situation | This section displays the statistics on the threat situation from the perspective of threat event management. This section includes the following modules: Threat Event Distribution by Level: displays the distribution and statistics on threat events at the urgent, serious, suspicious, moderate, and information levels. Trend of Threat Events: displays the trend in the number of threat events. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Threat Event Distribution by Type: displays the distribution and statistics of threat events of the network attack, suspicious process, malware, unauthorized privilege escalation, vulnerability exploitation, and risk connection types. ATT&CK Attack Behavior: displays the statistics on Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) behavior involved in threat events. Top 10 Threat Events: displays the number of times that the top 10 threat events are detected. Threat Event Distribution by Attack Chain: displays the attack phases involved in threat events and the number of times that the threat events are detected. Attack phases include payload delivery, vulnerability exploitation, webshell insertion, command control, scan extension, privilege escalation, and target attacks. |

| Handling and Response Posture Note If you want to view data in the Handling and Response Posture section, you must have permissions on Security Orchestration and Automation Response (SOAR). | This section displays the statistics on the handling and response posture from the perspective of handling and response management. This section includes the following modules: Total SOAR Handled Entities: displays the total number of entities handled by SOAR. Automatic Response Quantity: displays the number of automatic responses. Total Handling Tasks: displays the total number of tasks. Playbook Executions: displays the number of playbook executions. Enabled Playbooks/Total Playbooks: displays the number of enabled playbooks and the total number of playbooks. Trend of SOAR Handled Entities: displays the trend in the number of entities handled by SOAR. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Latest SOAR Handled Entities: displays the top 5 entities handled by SOAR. Top 5 Organizations with Highest Handling Task Completion Rate: displays the top 5 organizations that have the highest task completion rate and displays the task completion rate and on-time task completion rate for each organization. Automatic Response Distribution by Type: displays the trends in the number of automatic responses by type. The trends within the current day and last day are calculated by hour. The trends within thel ast 7 days and last 30 days are calculated by day. Playbook Running Trend: displays the playbook execution trend. The trends within the current day and last day are calculated by hour. The trends within the last 7 days and last 30 days are calculated by day. Top 5 Executed Playbook: displays the top 5 executed playbooks. |
|---|---|

### 3.2 View data in the operations center

**center**

The operations center displays the security and alert data of security services provided by Apsara Stack Security. Security administrators can view the information about cyberattacks and defenses on the Network Risk View, Host Risk View, and Data Security View tabs of the operations center. This helps improve network security. This topic describes how to view data in the operations center.

**View data in the network risk view**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. On the **Network Risk View** tab, view the following data.

| Section | Description |
|---|---|
| Widget selection (marked 1 in the following figure) | In this section, you can specify the types of data that you want to view. You can also perform the following operations: Select widgets: Select the widgets that you want to view from theS elect Statistics Window drop-down list. By default, the following widgets are selected: Alert Data, Distribution of Alert Handling Methods, ECS Instance Protection, Risk Level, Distribution of Alerting Data Sources, Distribution of Alert Types, Top 10 Attacking IP Addresses, Top 10 Attacked IP Addresses, Top 5 Attacked Websites, and List display area. Save the current view: Click the icon. Manually update statistics: Click the icon to manually update the statistics in the current view. Enable auto update: Turn on . The system automatically updates the statistics in the current view every 5 minutes. Export statistics: Click the icon to export the statistics in the current view. |
| Search condition (marked 2 in the following figure) | In this section, you can specify filter conditions to filter data. You can specify the following filter conditions: time range, data source, organization (all organizations or a specific organization), alert category, alert type, risk level, attack source, and asset. |
| Search result (marked 3 in the following figure) | Widgets that match the specified filter conditions are displayed accordingly. |

| List (marked 4 in the following figure) | In this section, details about user data alerts that match the specified filter conditions are displayed in the list, including the time when the attack occurred, attack source, alert name, alert category, alert type, and AI analysis. Click AI Analysis to view the suggestions generated by AI. You can perform the following operations to manage the details of alerts: Set the granularity of alert statistics: Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the alerts that have the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. View data details: Find the alert that you want to view and clickD etails in the Actions column. In the Details panel, view the details of the alert. Update the statistics in the list: Click the icon to manually update the statistics in the list. Customize the columns displayed in the list: Click the icon and select the columns you want to view. By default, all columns are selected. Deliver a task: Find the alert that you want to manage, clickM ore in the Actions column, and then select Deliver Handling Task. In the Create Task panel, configure the parameters and click OK. Note If alerts are aggregated, click the icon next to an alert to expand the alert list. Create a response policy: Find the alert that you want to manage, clickM ore in the Actions column, and then select Create Response Policy. In the Create Policy panel, configure the parameters and click OK. |
|---|---|

**View data in the host risk view**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. On the **Host Risk View** tab, view the following data.

| Section | Description |
|---|---|

| Widget selection (marked 1 in the following figure) | In this section, you can specify the types of data that you want to view. You can also perform the following operations: Select widgets: Select the widgets that you want to view from theS elect Statistics Window drop-down list. By default, the following widgets are selected: Alert Data, ECS Instance Protection, Risk Level, Distribution of Alert Types, Top 10 Attacked IP Addresses, and List display area. Save the current view: Click the icon. Manually update statistics: Click the icon to manually update the statistics in the current view. Enable auto update: Turn on . The system automatically updates the statistics in the current view every 5 minutes. Export statistics: Click the icon to export the statistics in the current view. |
|---|---|
| Search condition (marked 2 in the following figure) | In this section, you can specify filter conditions to filter data. You can specify the following filter conditions: time range, handling status, data source (Server Guard and Container Security Service), organization (all organizations or a specific organization), alert category, alert type, risk level, and attack source. |
| Search result (marked 3 in the following figure) | Widgets that match the specified filter conditions are displayed accordingly. |

| List (marked 4 in the following figure) | In this section, details about alerts that match the specified filter conditions are displayed in the list, including the time when the attack occurred, attack source, alert name, alert category, alert type, and AI analysis. Click AI Analysis to view the suggestions generated by AI. You can also perform the following operations to manage the details of alerts: Set the granularity of alert statistics: Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the alerts that have the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. View data details: Find the alert that you want to view and clickD etails in the Actions column. In the details panel, view the details of the alert. Update the statistics in the list: Click the icon to manually update the statistics in the list. Customize the columns displayed in the list: Click the icon and select the columns you want to view. By default, all columns are selected. Deliver a task: Find the alert that you want to manage, clickM ore in the Actions column, and then select Deliver Handling Task. In the Create Task panel, configure the parameters and click OK. Note If the alerts are aggregated, click the icon next to an alert to expand the alert list. Create a response policy: Find the alert that you want to manage, clickM ore in the Actions column, and then select Create Response Policy. In the Create Policy panel, configure the parameters and click OK. Handle one or more alerts: You can handle one or more alerts that occurred on a host. Find the alert that you want to handle and click Handle in the Actions column. In the dialog box that appears, select Quarantine, Add to Whitelist, Ignore, or Manually Handled in the Handling Method section. You can also select Handle the same type of alerts at a time in the Batch Handle section, which is optional. Then, click Handle Now. |
|---|---|

**View data in the data security view**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. On the **Data Security View** tab, view the following data.

| Section | Description |
|---|---|
| Widget selection (marked 1 in the following figure) | In this section, you can specify the types of data that you want to view. You can also perform the following operations: Select widgets: Select the widgets that you want to view from theS elect Statistics Window drop-down list. By default, the following widgets are selected: Alert Data, Risk Level, Distribution of Alert Types, Top 10 Source IP Addresses in Sensitive Data Access, Top 10 Most Accessed Sensitive Instances, and List display area. Save the current view: Click the icon. Manually update statistics: Click the icon to manually update the statistics in the current view. Enable auto update: Turn on . The system automatically updates the statistics in the current view every 5 minutes. Export statistics: Click the icon to export the statistics in the current view. |
| Search condition setting (marked 2 in the following figure) | In this section, you can specify filter conditions to filter data. You can specify the following filter conditions: time range, data source (SDDP), organization (all organizations or a specific organization), alert category, and alert type. |
| Search result (marked 3 in the following figure) | Widgets that match the specified filter conditions are displayed accordingly. |

| List (marked 4 in the following figure) | In this section, details about Sensitive Data Discovery and Protection (SDDP) user asset alerts that match the specified filter conditions are displayed in the list, including the time when the attack occurred, attack source, alert name, alert category, alert type, and AI analysis. Click AI Analysis to view the suggestions generated by AI. You can also perform the following operations to manage the details of alerts: Set the granularity of alert statistics: Above the list, click Details. The system displays the details of all attacked IP addresses in chronological order. Above the list, click Aggregate. The system aggregates the alerts that have the same attacked IP address, attacker IP address, and alert type every 10 minutes. You can click the + icon to view the details. View the details of an alert: Click Details in the Actions column of an alert to open the Details panel and view the details of the alert. Update the statistics in the list: Click the icon to manually update the statistics in the list. Customize the columns displayed in the list: Click the icon and select the columns you want to view. By default, all columns are selected. Deliver a task: Find the alert that you want to manage, clickM ore in the Actions column, and then select Deliver Handling Task. In the Create Task panel, configure the parameters and click OK. Note If the alerts are aggregated, click the icon next to an alert to expand the alert list. Create a response policy: Find the alert that you want to manage, clickM ore in the Actions column, and then select Create Response Policy. In the Create Policy panel, configure the parameters and click OK. |
|---|---|

**Create a custom risk view**

By default, the Operations Center page provides the Network Risk View, Host Risk View, and Data Security View tabs. To create a custom risk view, perform the following steps:
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Operations Center**.
4. In the upper-right corner of the **Operations Center** page, click **Select Statistics**
**Window**, select widgets for the custom risk view to be created, and then click the
icon.
5. In the **Save current view** dialog box, enter a view name and click **Save**.
The view name must up to 16 characters in length.

**Create a custom alert dashboard**

In the upper-right corner of the Operations Center page, click **Create Alert Dashboard**. On the page that appears, configure the basic information of the dashboard, such as the name and organization.

| Parameter | Description |
|---|---|
| Dashboard Name | The name of the dashboard. The name can be up to 32 characters in length, and can contain letters, digits, and commonly used special characters. |
| Time Range | You can select Today, Last 24 Hours, Last 7 Days, or Last 30 Days, or Custom. |
| Organization | You can select All, Platform, All Organizations, or Organization. |
| Select Statistics Window | Specify a combination of widgets that you want to view. You can specify the types of data to be displayed and the source of data in the corresponding dimension. |

After the dashboard is created, the filter conditions supported by the dashboard are displayed in the data filtering section. You can delete the dashboard if you no longer need it.

**Specify the alert handling time**

In the upper-right corner of the Operations Center page, click **Handling Time Configuration** to go to the **Alert Handling Time Configuration** page and configure the following parameters.

| Parameter | Description |
|---|---|
| Handling Type | You can customize the handling time for alerts of different types or risk levels. You can set the unit of the handling time to minutes, hours, or days. The value must be a positive integer, and the system will automatically verify the value that you have entered. |
| Alert Category |   |

After you complete the configuration, the system automatically checks whether an alert is handled within the specified handling time. You can view the ratio of alerts that are handled promptly in the alert data view. Timely Alert Handling Rate: The system determines whether an alert is handled within the specified time based on the time when the alert was triggered, the specified alert handling time, and the time when the alert was handled. Alerts matching the corresponding condition are considered alerts that have been handled promptly. Ratio of alerts that are handled promptly = (Number of alerts that are handled promptly/Total number of alerts) × 100%. Two decimal places are reserved.

### 3.3 Use the Risk Analysis module

#### 3.3.1 View threat events

Threat events refer to indicator of compromise (IOC) threat events generated by Security Operations Center (SOC) after comprehensive association analysis of raw logs and alerts based on predefined or custom security analysis models. This topic describes how to view threat events. Security administrators can obtain threat details based on these events to ensure network security.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center (SOC)**. On the **Security Operations Center (SOC)** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Threat Events**.
4. On the **Threat Events** page, view the details of threat events.

| Section | Description | Operation |
|---|---|---|
| Search condition | In this section, you can specify search conditions to search for threat events. You can specify the following search conditions: time range, Organization, Data Scope, Threat Level, Threat Type, Attack Phase, Handling Status, Hit Intelligence, and attack source or destination IP address. | Select options from drop-down lists or enter keywords, and click Search. If you do not specify search conditions, all threat events are displayed by default. Note After you set the Organization parameter to Organization, you can select one or more organizations from the Organization drop- down list. You can select one or more options from the Threat Level, Threat Type, and Attack Phase drop-down lists. |

| Search result | This section displays the information about threat events that meet the specified search conditions. | Find the threat event that you want to manage and move the pointer over a value in the Attacked IP Address or Attacker IP Address column to view the corresponding server. Click the icon to update the threat event list. Click the icon to export the threat event list. Deliver a task: Find the threat event that you want to manage, click More in the Actions column, and then select Deliver Handling Task. In the Create Task panel, configure the parameters and click OK. Create a response policy: Find the threat event that you want to manage, click More in the Actions column, and then select Create Response Policy. In the Create Policy panel, configure the parameters and click OK. View threat tracing details: Find a threat event that has a tracing diagram generated and click the icon to the right of the threat name. On the Threat Tracing tab, view the threat tracing details. Click the or icon to zoom out or in the threat tracing diagram. |
|---|---|---|

5. Click the name of a threat event or click **Details** in the Actions column to go to the details
page of the threat event. Choose **Handle > Deliver Handling Task** to go to the **Create Task** page, configure the parameters, and click **OK**. Choose **Handle > Create Response Policy** to go to the **Create Response Policy** page, configure the parameters, and click **OK**. Choose **Handle > Create Case** to create a case. You can view the case on the **Handle**
**> Case Management** page.
6. Click the name of a threat event or click **Details** in the Actions column. On the details page,
view the information on the **Threat Details** and **Evidence Details** tabs. On the **Threat Details** tab, view the following information: **Start Time**, **Last Detected**
**At**, **Analytic Rules**, **Network Protocol**, **Threat Intelligence**, **Source Information**,
**Target Details**, and **Key Information**.
Click the rule ID next to **Analytic Rule** to view more information about the rule that detects the threat. Click **Generate Case** to generate a case for the current threat event on the **Security**
**Events** page of the Security Orchestration and Automation Response (SOAR) console.
This helps monitor and handle the threat event. On the **Evidence Details** tab, view the raw logs of the threat event. Click **Details** next to a raw log to view the details of the raw log, including alert information. The content that matches an association analysis rule is highlighted.

#### 3.3.2 Use the threat investigation feature

The threat investigation feature allows you to perform comprehensive threat investigations based on IP addresses, asset names, and asset IDs. This topic describes how to use the threat investigation feature.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Threat Investigation**.
4. On the **Threat Investigation** page, select a time range, specify the asset information,
such as the IP address or name of the asset, and then click the icon. i. After you select **Asset Fingerprints**, you can select the **Account**, **Port**, or **AI**
**Component** query condition to query the fingerprints of matching assets. The query
result shows the basic information of the assets. You can click View Details or go to the asset details page. ii. The attacker profile module can automatically generate an attacker profile corresponding to an attacker IP address based on statistics such as alerts and threat intelligence. The profile shows the number of victims, the attack timeline, and the number of attacks. iii. If an asset is frequently queried, you can create a shortcut for the asset by performing the following steps: Click **Add Shortcut**. In the Add Shortcut dialog box, configure the
**Type** and **Content** parameters and click OK. This way, you can quickly view the threat
investigation results of the asset. After a shortcut is created, you can click the corresponding icon to view the threat investigation results of an asset.
5. On the page that appears, view the risk items.
The modules displayed vary based on assets. The modules displayed on the console shall prevail. Regular modules: Asset Details: displays the network topology and fingerprints of the asset. The asset fingerprints include ports, software, processes, accounts, middleware, and startup items. Suspicious Process: displays statistics on the abnormal behavior in the asset in the form of charts and tables. The statistics include the total amount of abnormal behavior, abnormal behavior distribution by level, abnormal behavior distribution by type, and top 5 abnormal behavior. Network Attack: displays statistics on the cyberattacks on the asset in the form of charts and tables. The statistics include the total number of cyberattacks, distribution of cyberattack data sources, distribution of cyberattack types, and top 5 cyberattacks. Vulnerabilities: displays statistics on the vulnerabilities in the asset and the failed baseline check items for the asset in the form of lists. Attack Surface: displays the path of the attacks that are launched against the asset.

#### 3.3.3 View attack surface assessment results

This topic describes how to view attack surface assessment results.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis** > **Attack Surface Assessment**.
4. In the upper-right corner of the **Attack Surface Assessment** page, select the organization
that you want to view.
5. On the **Attack Surface Assessment** page, view the statistics on exposed attack surfaces.
**Shadow IP addresses Within Last 30 Days** : A shadow IP address outside the cloud is
an IP address of an asset that can communicate with the cloud platform but is not managed by the cloud platform. The asset can be unauthorized software, an unapproved hardware device, a cloud service, or a third-party application. This asset is not managed by the cloud platform and may cause unknown risks or threats. Attackers can use a shadow IP address to attack assets in the cloud.
**Vulnerable Security Group**: A vulnerable security group is a security group that allows
inbound traffic from IP addresses in a loose manner. To implement the principle of least privilege, we recommend that you delete security group rules that allow inbound traffic from unnecessary IP addresses. An unnecessary IP address refers to an IP address that is not required in your workloads. This helps reduce exposure at the network layer.
**Exposed Assets**: An exposed asset is an Elastic Compute Service (ECS) instance that is
accessible from outside the cloud platform and exposed in a known attack path.
**At-risk Accounts**: A risky account is an account that uses a weak password and can be
used to log in to assets in the cloud from outside the cloud. If the account is leaked, attackers can intrude assets in the cloud with ease.
**Risk Level of Attack Surface** : The risk level of the attack surface for the specified
organization is determined after a comprehensive evaluation is performed. The risk level can be Low, Medium, High, and Critical.
6. View the details of each risk on the corresponding tab.
**Attack Surface**: This tab displays the statistics on attack paths and core assets affected
by the attack paths. You can view the following information about an attack path: **Path**
**Name**, **Path Risk Score**, **Affected Core Assets**, and **Assets in Path**.
You can perform the following operations: Click the icon. On the **Attack Path Configuration** page, configure **Risk Score for**
**Attack Path Filtering**.
Click **Panorama View** to view the network topologies of all attack paths. Find the attack path that you want to manage and click its name or **View Attack Path** in the Actions column to view the network topology of the attack path.

**Note**

You can click **2D Mode** or **3D Mode** in the upper-right corner of the **Attack Surface**
**Assessment** page or attack path page to switch the view.
**Shadow IP Address Outside Cloud**: This tab displays the list of **shadow IP addresses**
**outside the cloud**. You can perform the following operations:
Click an IP address to view its details, including the **geographical location**, **cloud-**
**connected assets**, **handling status**, **time when the IP address was first/last**
**detected**, **inbound cloud-connected assets**, **destination IP address**, and
**inbound traffic**.
**Vulnerable Security Group**: This tab displays the list of vulnerable security groups. You
can click the name of a security group or click **Details** in the Actions column of a security group to view its details, including **VPC ID**, **Security Group Type**, **Organization**,
**Resource Set**, **Description**, and **Instances Within Security Group**.
**Exposed Assets**: This tab displays the list of ECS instances that can be directly accessed
from outside the cloud platform. You can click the name of an asset to view its basic information, such as the importance, organization, and virtual private cloud (VPC) of the asset. You can also view security risks such as vulnerabilities, security baselines, and accounts.
**At-risk Accounts**: This tab displays the list of risky accounts. Find the asset that you
want to view and click its name. On the details page of the asset, view **Basic**
**Information**, **Business Information**, and **Asset Fingerprints**.

#### 3.3.4 View cloud service check data

You can use built-in security baselines to check and manage the security compliance of Apsara Stack services. This topic describes how to perform a cloud service check and view check data.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis** > **Cloud Service Check**.
4. In the upper-right corner of the **Cloud Service Check** page, click **Select Organization or**
**Resource Set**. Select one or more organizations that you want to check and click **OK**.
5. Specify search conditions to search for baselines.

**Note**

If you do not specify search conditions, all baselines of cloud services are displayed by default.

| Search condition | Description |
|---|---|
| Baseline Type | The type of the baseline. Valid values: Security Protection, Identity Authentication, Access Control, Network Configuration, Data Security, Disaster Recovery Backup, Log Audit, and Monitoring Alarms. |
| Risk Level | The risk level of the baseline. Valid values: High, Medium, and Low. |
| Baseline name | Enter the name of a baseline in the search box and click the icon to search for the baseline. |

6. On the **Cloud Service Check** page, view information about the baselines of cloud services.
The information includes baseline risk items, affected assets, enabled baseline check items, disabled baseline check items, and the time when the check was last performed.
7. Perform a cloud service check.
Manual check Click **Check Now**. The system starts a full check on the configurations of all services to detect risks and affected assets. During the check, you can click **View** to view the check progress in the **Check Item Detection** dialog box.

**Note**

Do not perform other operations until the check is complete. Automatic check Click **Check Settings** to configure a check policy. The following table describes the required parameters.

| Parameter | Description |
|---|---|
| Check Cycle | The days of the week on which you want to run an automatic check. Valid values: Monday to Sunday. You can select multiple days of the week. |
| Checked At | The time range during which you want to run an automatic check. Valid values: 24:00 - 06:00, 06:00 - 12:00, 12:00 - 18:00, and 18:00 - 24:00. You can select only one time range. |

| Baseline Check Item | The baselines that you want to use. |
|---|---|
| Select Resource Set | The resource sets that you want to check. |

After you configure the check policy, Security Operations Center (SOC) automatically performs a check based on all specified baselines within the specified time range.
8. View check data.
In the baseline list, view the following information about baselines: Cloud Product Baseline, Baseline Category, Baseline Type, Risk Level, Affected assets, Last Checked At, and Status. Find a baseline and click its name or click **Details** in the **Actions** column. In the panel that appears, view data on the Baseline Check Details and Cloud Service Instances tabs. If an organization or instance is riskless, you can select and add the organization or instance to the whitelist. Find a baseline and click **Verify** in the **Actions** column, or select one or more baselines and click **Verify** below the baseline list to verify that the detected baseline risks are fixed. During the verification, you can click **View** in the Actions column of the baseline to view the verification progress. You can click **Cancel Verification** in the Actions column of the baseline to cancel the verification.

#### 3.3.5 View vulnerability analysis results

This topic describes how to view vulnerability analysis results on the tenant side. Security administrators can use the results to troubleshoot issues.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center (SOC)**. On the **Security Operations Center** page, select a region
from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Risk Analysis > Vulnerability Analytics**.

**Vulnerabilities**

You can specify search conditions to search for vulnerabilities.

**Note**

If you do not specify search conditions, all vulnerabilities are displayed by default.

| Query condition | Description |
|---|---|
| Organization | The organization whose risks you want to query. |

| Time range | Specify the time range of the data that you want to query. You can select Today, Last 24 Hours, Last 7 Days, Last 30 Days, or Custom from the time range drop-down list. |
|---|---|
| Vulnerability Distribution | The vulnerability data that you want to query. You can select Host, Host & Container, or All. |
| Vulnerability Type | The type of the vulnerabilities that you want to query. Valid values: All, Web-CMS, Linux Software, Windows System, and Application(Urgent Vulnerability Included). |
| Vulnerability Level | The severity of the vulnerabilities. Valid values: All, High, Medium, and Low. |
| Data Source | The source from which you want to query vulnerability data. Valid values: Server Guard and Container Security Service, and MoreSec. |
| Vulnerability name or Common Vulnerabilities and Exposures (CVE) ID | Enter a keyword of a vulnerability name or CVE ID in the search box to search for vulnerabilities. Fuzzy search is supported. |

All search results are displayed in the vulnerability list. You can perform the following operations based on your business requirements: Click the icon to refresh the vulnerability list. Click the icon to export the vulnerability list. Find the vulnerability that you want to view and click its name or **Details** in the **Actions** column to view the vulnerability details and affected assets. The vulnerability details page displays information such as vulnerability fix suggestions and vulnerability announcements based on the vulnerability type. The Affected Assets page displays information about the assets affected by the vulnerability. You can click **Details** in the Actions column of the asset to go to the Asset Management page. You can also fix and handle asset vulnerabilities and record the entire lifecycle of asset vulnerabilities in real time.

**Note**

You can view the result of the asset type and vulnerability fixes on the
**Affected Asset** tab.
If the asset type has container labels, you can click Details to go to the container asset details page. If the asset type has only ECS labels, you can go to the ECS asset details page. Deliver a task: Find the vulnerability that you want to manage, click **More** in the **Actions** column, and then select **Deliver Handling Task**. In the **Create Task** panel, configure the parameters and click **OK**. Create a response policy: Find the vulnerability that you want to manage, click **More** in the Actions column, and then select **Create Response Policy**. In the **Create Policy** panel, configure the parameters and click **OK**. Add vulnerabilities to the whitelist: Select one or more vulnerabilities and click **Add to**
**Whitelist**. In the **Prompt** dialog box, enter remarks and click **OK**.
Click**Details**in the Actions column to view the vulnerability details and affected assets. On the Affected Assets tab, you can click **Verify** or **Ignore**. Fix multiple vulnerabilities at a time: Select one or more vulnerabilities and click **Batch**
**Fix** below the vulnerability list. You can also click **Repair** in the Actions column of a
vulnerability. In the **Batch Fix** dialog box, select **I have understood the risk of repair**
**failure.** and click **Fix Now**.

**Baselines**

You can specify search conditions to search for baselines.

**Note**

If you do not specify search conditions, all baselines are displayed by default.

| Query condition | Description |
|---|---|
| Scope | The organization whose risks you want to query. |
| Time range | Specify the time range of the data that you want to query. You can select Today, Last 24 Hours, Last 7 Days, Last 30 Days, or Custom from the time range drop-down list. |
| Data source | The data source of the baselines that you want to query. Valid values: All Server Guard Cloud Service Check |

| Risk Type | The risk type of the baselines. Valid values: hierarchy protection Unauthorized Access Internationally Agreed Best Practices for Security Custom baseline Best security practices Weak password Container security Data Security Access Control Monitoring Alarms Disaster Recovery Backup Log Audit Authentication Security NetworkConfiguration |
|---|---|
| Risk Level | The severity of the baselines. Valid values: All, High, Medium, and Low. |
| Baseline Name | The name of the baseline. |

All search results are displayed in the baseline list. You can perform the following operations based on your business requirements: Click the icon to refresh the baseline list. Click the icon to export the baseline list. Click the name of a baseline or click **Details** in the **Actions** column of a baseline to view the baseline details, including **Affected Assets**, **Resource Set**, and **Organization**. Click the name of an affected asset to go to the **Tenant Assets** page. On the Tenant Assets page, you can view information about the affected asset. Deliver a task: Find the baseline that you want to manage, click **More** in the **Actions** column, and then select **Deliver Handling Task**. In the **Create Task**panel, configure the parameters and click **OK**. Create a response policy: Find the baseline that you want to manage, click **More** in the Actions column, and then select **Create Response Policy**. In the **Create Policy** panel, configure the parameters and click **OK**.

**Note**

We recommend that you handle the risks based on the risk description provided by SOC.

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

### 3.4 威胁情报

#### 3.4.1 Threat intelligence overview

You can view the overall situation and statistics of threats to your assets on the Threat Intelligence Overview page. This topic describes how to view the threat intelligence of assets.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Threat Intelligence > Threat Intelligence**
**Overview**.
4. On the **Threat Intelligence Overview** page, view the statistics and events of threats that
are detected on your assets by the threat intelligence feature.

| Section | Description |
|---|---|
| Total Threat Indicators | This section displays the numbers of the following types of threats and the month-over-month changes in the numbers: malicious IP addresses, domain names, and files. |
| Trend of Threat Indicators | This section displays the trends of threats within the specified period of time. |

| Threat Intelligence Call Summary | This section displays the query statistics on threat intelligence in the following parts: Threat Indicators: the number of API operation calls. Threat IoC Query Type: the numbers of queries for IP addresses, domain names, and files. API Query Source Distribution: the proportions of query sources. Threat Intelligence Query Statistics: the trends of threats within the specified period of time. |
|---|---|
| Threat Intelligence Tag Distribution | This section displays the following statistics on the tags that are added to threat intelligence: The numbers of tags at the high, medium, and low severity levels. Top 10 Hit Intelligence Tags: displays the top 10 tags that occur most frequently in the Threat Tag column and the number of occurrences of each tag in the Hits column. You can click a number in the Hits column to view the details, including threats and alerts in the Hit IoC Information and Related Information sections. |

5. In the upper-right corner of the Threat Intelligence Overview page, enter an IP address,
domain name, or MD5 hash value in the search box and click the icon. Then, you are redirected to the details page. On this page, you can view the following information: **Threat Level**, **Basic Information**, **Threat Details**, and **Threat Overview**. For more information, see Query threat intelligence.

#### 3.4.2 Query threat intelligence

You can use the threat intelligence feature to query the threat intelligence of an IP address. This feature helps you identify suspicious or malicious IP addresses at the earliest opportunity. This topic describes how to query threat intelligence.

**Prerequisites**

The **service configuration** feature is enabled. For more information, see Manage the threat intelligence module.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Threat Intelligence** > **Intelligence Query**.
4. On the page that appears, perform the following operations:
View the threat intelligence in assets.

| Section | Description |
|---|---|

| Top 10 Active Malicious IP Addresses | You can view the top 10 active malicious IP addresses and their tags. Click a malicious IP address. On the page that appears, you can view the following information about the malicious IP address: Threat Level: View the threat level of the suspicious or malicious IP address. The threat levels are Normal, Suspicious, and High Risk. If the threat level of an IP address is High Risk, we recommend that you handle the IP address at the earliest opportunity. Basic Information: View the basic information about the suspicious or malicious IP address. The basic information includes the data center server, autonomous system number (ASN), country, city, number of associated domain names, activity level, and tags that are added to the IP address. Threat Details: View the threat tag list of a malicious IP address. The list displays information such as the intelligence source, first detection time, last activity time, and threat tag. Threat Overview: View the risk analysis of malicious IP addresses based on historical threat indicators and events. |
|---|---|
| Top 10 Active Malicious Domain Names | You can view the top 10 active malicious domain names and their tags. Click a malicious domain name. On the page that appears, view the following information about the malicious domain name: Threat Level: View the threat level of the suspicious or malicious domain name. The threat levels are Normal, Suspicious, and High Risk. If the threat level of a malicious domain name is High Risk, we recommend that you handle the domain name at the earliest opportunity. Summary of Domain Name Report: View the basic information about a suspicious or malicious domain name. The basic information includes the domain name tag, number of historical IP addresses, number of malicious IP addresses, malicious URL of the domain name, subdomain of the domain name, number of malicious subdomain names, sample of malicious communication with the domain name, registration time, and expiration time. Domain Name Details: View the values of the WHOlS Details and WHOIS Value parameters of the malicious domain name. Threat Overview: View the risk analysis of malicious domain names based on historical threat indicators and events. Threat Details: View the threat tag list of malicious domain names. The list displays information such as the intelligence source, first detection time, last active time, and threat tag. |

| Top 10 File MD5 Hash Values | View the top 10 files and their tags. Click the MD5 hash value of a file. On the page that appears, view the following information about the file: Threat Level: View the threat levels of the suspicious or malicious file. The threat levels include Normal, Suspicious, and High. If the threat level of a file is High Risk, we recommend that you handle the file at the earliest opportunity. File Report Summary: You can view the basic information about the suspicious or malicious file. The basic information includes the file tag, file name, runtime environment, and time when the malicious file is first detected. Static Threat Analysis: You can view the results of checks that are performed by multiple engines on the file. |
|---|---|

On the search page, enter an IP address, domain name, or file MD5 hash value in the search box. On the details page, you can view the details of malicious IP addresses, malicious domain names, and malicious files.

### 3.5 资产管理

#### 3.5.1 View tenant assets

You can view the assets of tenants on the Tenant Assets page. The assets include Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, Object Storage Service (OSS) buckets, Server Load Balancer (SLB) instances, and elastic IP addresses (EIPs). This topic describes how to view the assets of tenants. You can also specify a search condition in a search box to search for an asset.

**Note**

If you do not specify a search condition, all assets are automatically displayed.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Assets > Tenant Assets**.
4. In the upper-right corner of the **Tenant Assets** page, select a time range from the
**Created At** drop-down list and select an organization from the **Organization** drop-down
list. You can select Today, Last 24 Hours, Last 7 Days, or Last 30 Days from the **Created At** drop-down list to view asset information within the selected time period. You can also specify a custom time range to view asset information. Click the icon to refresh the asset data.
5. Click the following tabs to view tenant assets: **ECS**, **ApsaraDB RDS**, **OSS**, **AI Asset**, **SLB**,
**EIP**, **Active Internet IP Addresses**, **Tunnel**, **Server Outside Cloud**, and **Container**.
You can specify search conditions to search for servers, assets, or instances.

**Note**

If you do not specify search conditions, all servers, assets, or instances are automatically displayed. Configure asset importance tags and business types. Click a server or instance name to view the following details.

**Container**

| Tab | Description |
|---|---|
| Asset Information | Basic Information: You can view the basic information about the container asset. |
| Asset Risks | Risk Level You can view the risk assessment data of the asset, including asset risk indexes, suspicious process risks, and vulnerability risks. You can view the severity distribution of suspicious processes, vulnerabilities, and their trends within the last seven days. You can view the top 5 suspicious processes and vulnerabilities. Suspicious Processes: You can view and handle the suspicious behavior that affects the asset. Vulnerabilities: You can view the details of security vulnerabilities in container assets. You can also run management tasks and create response policies. |

**ECS**

| Tab | Description |
|---|---|

| Asset Information | Basic Information: You can view asset information in the Basic Information and Disk Information sections. Network Information: You can view the virtual private cloud (VPC), SLB instance, NAT gateway, and EIP of the asset. You can also click Network Link View to view the network connections and Internet access paths to ECS instances. This helps you troubleshoot network issues, reduce exposure risks, and trace threats. You can zoom in, zoom out, and download the view. You can also drag the elements in the view. You can click Network Information List to return to the network information list. Security Policy: You can view the security login settings and security group information. Associated Container Assets: You can view the basic information, risk indexes, suspicious processes, and vulnerabilities of the associated container assets. |
|---|---|
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack configuration management database (CMDB). Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Fingerprints | You can view fingerprint information on the AI Component, Port, Software, Process, Account, Planned Tasks, Middleware, and Startup Item tabs. |

| Asset Risks | Risk Level You can view the risk assessment data of the asset, including asset risk indexes, cyberattack risks, abnormal behavior risks, security vulnerability risks, and security baseline risks. You can view the distribution of cyberattacks, suspicious processes, security vulnerabilities, and security baselines by risk severity. You can also view the trend of cyberattacks within the last seven days. You can view the following information: top 5 cyberattack risks, top 5 suspicious process risks, top 5 security vulnerability risks, and top 5 security baseline risks. Network Attacks: You can view and handle cyberattacks on the asset. Suspicious Processes: You can view and handle the suspicious processes that affect the asset. Vulnerabilities: You can view the details of security vulnerabilities in the asset and fix the security vulnerabilities based on the provided suggestions. Fix a security vulnerability: On the ECS tab of the Tenant Assets page, find the ECS instance that you want to manage, and click the name of the ECS instance to go to the Basic Information tab of the Asset Information tab or click the number in the Vulnerabilities column to go to the Vulnerabilities tab of the Asset Risks tab. On the Vulnerabilities tab, find the vulnerability that you want to fix and click Repair in the Actions column. In the Batch Fix dialog box, select I have understood the risk of repair failure. and click Fix Now. Baselines: You can view the details of the security baseline risks in the asset and handle the security baseline risks based on the provided suggestions. Handle a security baseline risk: On the ECS tab of the Tenant Assets page, find the ECS instance that you want to manage, and click the name of the ECS instance to go to the Basic Information tab of the Asset Information tab or click the number in the Baselines column to go to the Baselines tab of the Asset Risks tab. On the Baselines tab, find the security baseline risk that you want to handle and click an option in the Actions column to perform the corresponding operation. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |
|---|---|

| Asset Behaviors | Process Behavior On the Process Behavior tab, you can view the statistics information in the Process Behavior Distribution and Top 5 Process Behaviors sections. This helps you understand the behavior characteristics and distribution of each process in the system. You can select Today, Last 24 Hours, Last 7 Days, Last 30 Days, or Custom as a time range. The default time range is Last 30 Days. In the Process Tree section, you can view the process location based on PIDs, usernames, or process names, along with a process tree view that provides association analysis and traceability for related scenarios. In the Process Behavior section, you can view the process behavior and its details. You can click a process behavior name to view the timeline of the process. Click Details next to a process to view the details of the process. Configuration Behavior On the Configuration Behavior tab, you can view the statistics information in the Configuration Behavior Analysis and Top 5 Configuration Behavior sections. This helps you understand the distribution of configurations in the system. You can filter data by time or by behavior name. You can select Today, Last 24 Hours, Last 7 Days, Last 30 Days, or Custom as a time range. The default time range is Last 30 Days. In the configuration behavior list section, the list is displayed in a timeline format, showing all critical behavior detected within the statistical period, sorted by the time of occurrence. Click Query Instance Details to view the details of raw logs. Behavior Baseline The status and baseline learning cycle of the suspicious behavior model associated with the asset are displayed on cards. Click Re-learn to clear all learning data and exception configurations of the assets associated with the model, and then restart the learning baseline. Before the new learning cycle ends, the model suspends detection for anomalies on the corresponding assets. This results in a "detection vacuum". |
|---|---|

**AI Asset**

| Tab | Description |
|---|---|
| Asset Information | Basic Information: You can view the asset information in the Basic Information and Disk Information sections. Security Policy: You can view the security login settings and security group information. |

| Asset Fingerprints | You can view fingerprint information on the AI Component, Port, Software, Process, Account, Planned Tasks, Middleware, and Startup Item tabs. |
|---|---|
| Asset Risks | Risk Level You can view the risk assessment data of the asset, including asset risk indexes, cyberattack risks, abnormal behavior risks, security vulnerability risks, and security baseline risks. You can view the distribution of cyberattacks, abnormal behavior, security vulnerabilities, and security baselines by risk level. You can also view the trend of cyberattacks within the last seven days. You can view the following information: top 5 cyberattack risks, top 5 abnormal behavior risks, top 5 security vulnerability risks, and top 5 security baseline risks. Suspicious Processes: You can view and handle the suspicious processes that affect the asset. Vulnerabilities: You can view the details of security vulnerabilities in the asset and fix the security vulnerabilities based on the provided suggestions. Fix a security vulnerability: On the ECS tab of the Tenant Assets page, find the ECS instance that you want to manage, and click the name of the ECS instance to go to the Basic Information tab of the Asset Information tab or click the number in the Vulnerabilities column to go to the Vulnerabilities tab of the Asset Risks tab. On the Vulnerabilities tab, find the vulnerability that you want to fix and click Repair in the Actions column. In the Batch Fix dialog box, select I have understood the risk of repair failure. and click Fix Now. Baselines: You can view the details of the security baseline risks in the asset and handle the security baseline risks based on the provided suggestions. Handle a security baseline risk: On the ECS tab of the Tenant Assets page, find the ECS instance that you want to manage, and click the name of the ECS instance to go to the Basic Information tab of the Asset Information tab or click the number in the Baselines column to go to the Baselines tab of the Asset Risks tab. On the Baselines tab, find the security baseline risk that you want to handle and click an option in the Actions column to perform the corresponding operation. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |

**ApsaraDB RDS**

| Tab | Description |
|---|---|
| Asset Information | Basic Information: You can view the basic information about the ApsaraDB RDS instance in the Basic Information section. Network Information: You can view the tunnel information about the ApsaraDB RDS instance in the Tunnel section. Security Policy: You can view the whitelist of the ApsaraDB RDS instance in the Whitelist Information section. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | You can view the details of the security baseline risks in the asset and handle the security baseline risks based on the provided suggestions. |

**OSS**

| Tab | Description |
|---|---|
| Asset Information | You can view the basic information about the OSS bucket. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | You can view the details of the security baseline risks in the OSS bucket and handle the security baseline risks based on the provided suggestions. |

**SLB, EIP, and Active Internet IP Addresses**

| Tab | Description |
|---|---|
| Asset Information | Basic Information: You can view the basic information about the asset in the Basic Information section. Associate ECS Asset: You can view the information about the ECS instances that are associated with the asset. You can click the name of an associated ECS instance to view its details. |
| Business Information | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
| Asset Risks | Network Attacks: You can view and handle cyberattacks on the asset. Suspicious Processes: You can view and handle the abnormal behavior that affects the asset. Vulnerabilities: You can view the details of security vulnerabilities in the asset and fix the security vulnerabilities based on the provided suggestions. Baselines: You can view the details of the security baseline risks in the asset and handle the security baseline risks based on the provided suggestions. |

**Tunnel**

| Tab | Description |
|---|---|
| Asset Informatio n | Basic Information: You can view the basic information about the asset in the Basic Information section. Network Information: You can view the tunnel information about the asset in the Tunnel section. Security Policy: You can view the whitelist of the asset in the Whitelist Information section. |

| Business Informatio n | Application: You can view the information about the application to which the asset belongs in the Apsara Stack CMDB. Application System: You can view the information about the application system to which the asset belongs in the Apsara Stack CMDB. Service: You can view the information about the service to which the asset belongs in the Apsara Stack CMDB. |
|---|---|
| Asset Risks | You can view the details of the security baseline risks in the asset and handle the security baseline risks based on the provided suggestions. |

**Server Outside Cloud**

| Tab | Description |
|---|---|
| Asset Informatio n | Basic Information: You can view the basic information and network information about the asset. Security Policy: You can view the security login settings. |
| Asset Fingerprin ts | You can view fingerprint information on the AI Component, Port, Software, Process, Account, Planned Tasks, Middleware, and Startup Item tabs. |

| Asset Risks | Risk Level You can view the risk assessment data of the asset, including asset risk indexes, cyberattack risks, abnormal behavior risks, security vulnerability risks, and security baseline risks. You can view the distribution of cyberattacks, abnormal behavior, security vulnerabilities, and security baselines by risk level. You can also view the trend of cyberattacks within the last seven days. You can view the following information: top 5 cyberattack risks, top 5 abnormal behavior risks, top 5 security vulnerability risks, and top 5 security baseline risks. Suspicious Processes: You can view and handle the abnormal behavior that affects the asset. Vulnerabilities: You can view the details of security vulnerabilities in the asset and fix the security vulnerabilities based on the provided suggestions. Fix a vulnerability: On the Server Outside Cloud tab of the Tenant Assets page, find the server that you want to manage, and click the name of the server to go to the Risk Level tab of the Asset Risks tab or click the number in the Vulnerabilities column to go to the Vulnerabilities tab of the Asset Risks tab. On the Vulnerabilities tab, find the vulnerability that you want to fix and click Repair in the Actions column. In the Batch Fix dialog box, select I have understood the risk of repair failure. and click Fix Now. Baselines: You can view the details of the security baseline risks in the asset and handle the security baseline risks based on the provided suggestions. Handle a security baseline risk: On the Server Outside Cloud tab of the Tenant Assets page, find the server that you want to manage, and click the name of the server to go to the Risk Level tab of the Asset Risks tab or click the number in the Baselines column to go to the Baselines tab of the Asset Risks tab. On the Baselines tab, find the security baseline risk that you want to handle and click an option in the Actions column to perform the corresponding operation. Exposure on Internet: You can check whether the asset is exposed on the Internet and implement the required measures. |
|---|---|
| Asset Behaviors | On the Process Behavior tab, you can view the statistics information in the Process Behavior Distribution and Top 5 Process Behaviors sections. This helps you understand the behavior characteristics and distribution of each process in the system. You can select Today, Last 24 Hours, Last 7 Days, Last 30 Days, or Custom as a time range. The default time range is Last 30 Days. In the Process Tree section, you can view the process location based on PIDs, usernames, or process names, along with a process tree view that provides association analysis and traceability for related scenarios. In the Process Behavior section, you can view the process behavior and its details. You can click a process behavior name to view the timeline of the process. Click Details next to a process to view the details of the process. Behavior Baseline The status and baseline learning cycle of the suspicious behavior model associated with the asset are displayed on cards. Click Re-learn to clear all learning data and exception configurations of the assets associated with the model, and then restart the learning baseline. Before the new learning cycle ends, the model suspends detection for anomalies on the corresponding assets. This results in a "detection vacuum". |

Click the icon to refresh the asset list. Click the icon to export the asset information. Click the icon to configure the items that you want to view in the asset list.

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

#### 3.6.2 Log query

##### 3.6.2.1 Query log details

This topic describes how to query log details.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Search**.
4. You can search logs by specifying the following search conditions: time range, organization
(all organizations or a specific organization), system type, log source, log type, log subtype, log field, and query statement. The log query module can transform the natural language you input into Simple Log Service Processing Language (SPL) statements. Click the icon, enter query information, and then click the icon to generate an executable SPL statement. You can also modify the SPL statement. Descriptions of the query results: Log distribution histogram: displays the distribution of the queried logs by time. After you click a bar in the histogram, the system automatically adds the start time and end time of the bar as query conditions. Table Mode: displays the logs of the specified log fields in a table and the log analysis result. List Mode: displays the logs of the specified log fields in a list and the log analysis result. Chart: displays the log analysis result and allows you to customize the chart type, chart size, chart title, and statistical field of a log.

**What to do next**

Configure the current log query results as followed logs: Click **Follow Logs**. In the Follow Logs dialog box, configure the **Followed Log Name** parameter, select Save As Independent Window, and then click OK. After the configuration is complete, you can query the followed logs in a widget of the
**Overview** page.
Save the current view: Click the icon in the upper-right corner of the Log Search page. In the Create Filter Condition dialog box, enter the query condition name of the current view and click OK. After the current view is saved, you can select the query condition name of the current view from the **Default Data** drop-down list in the upper-right corner of the Log Search page to perform a quick query. Delete the current view: Click the icon in the upper-right corner of the Log Search page to delete the saved view query conditions. The **Default Data** view cannot be deleted. Enable auto update: Turn on . Then, the system automatically updates the log query information every 5 minutes. View log dictionaries: Click **Log Dictionary** to view the information about different types of logs, including the field name, type, and description. On the **Log Search** page, click **Save as Analysis Rule** after you specify log query conditions. Then, you are redirected to the **Create Rule** page. On the **Create Rule** page, the system automatically sets **Log Scope** and **Search Condition** to the log source and query conditions that you have specified.

##### 3.6.2.2 Query raw logs

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

**Important**

When you perform field-based queries, specify the logical operators AND, OR, and NOT in upper-case letters. When you enter an SQL statement to query logs, set the name of the table name to **mytable**. When you enter an SQL statement to query logs, user-defined functions (UDFs) and nested queries are not supported. When you enter an SQL statement to query logs, the DISTINCT operations are not supported. When you enter an SQL statement to query logs, you can use the count(*) as cnt function to rename the queried log fields cnt. You cannot use the src_ip as ip function to rename the queried IP addresses. When you enter an SQL statement to query logs, only fields of the string type can be aggregated. If a query times out when you use a wildcard character to query logs, you can narrow down the query scope and try again.
5. In the log list, select the fields that you want to query and view the logs about the fields.
You can also expand a display field to view the top 5 values of the field.

#### 3.6.3 View tenant logs

Tenant logs record information about tenants. Security administrators can use these logs to troubleshoot issues that occur on the tenant side. This topic describes how to view tenant logs.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Tenant Logs**.
4. On the **Tenant Logs** page, specify the scope, log source, and time range based on your
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
5. On the **Tenant Logs** page, set the log query conditions and click **Save as Analysis Rule**
to go to the **Create Rule** page. On the **Create Rule** page, the system automatically sets
**Log Scope** and **Search Condition** to the log source and query conditions that you have
specified.

#### 3.6.4 Logging configurations

Security Operations Center (SOC) provides the log forwarding feature. Security administrators can forward logs based on their business requirements and view logs at the earliest opportunity. You can specify multiple log sources for a log forwarding task. You can also forward logs that belong to specified organizations. This topic describes how to configure a log forwarding task.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center (SOC)**. On the **Security Operations Center** page, select a region
from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Logs > Log Configurations**.
4. On the **Log Forwarding** tab, click **Create Forwarding Task**. In the panel that appears,
configure the following parameters and click **OK**.

**Note**

You can set the Data Protocol parameter to Syslog or Kafka.

**Syslog**

| Parameter | Description |
|---|---|
| Task Name | The name of the forwarding task. The name must be 0 to 64 characters in length. |
| IP:Port | The IP address, port number, and protocol that are used for log forwarding. Supported protocols include UDP and TCP. |
| Test Connectivity | Test whether network communication is established. |
| Data Scope | The organization to which the task is delivered. |
| Select Log Source | Select one or more types of log sources in theL og Source section and click the icon to add the selected log sources to theS elected Log Sources section. |
| Forwarding Field | Supported log forwarding fields: Standardized Field Original Field Standardized Field and Original Field |
| Forwarding Status | Turn on or turn off the switch to enable or disable the log forwarding feature. |

**Kafka**

| Parameter | Description |
|---|---|

| Task Name | The name of the forwarding task. The name must be 0 to 64 characters in length. |
|---|---|
| Service Address | The IP address and port number that are used for log forwarding. |
| Topics | The list of Kafka topics. Separate multiple Kafka topics with commas (,). |
| Authentication | Specifies whether a Kafka cluster requires authentication. If the Kafka cluster requires authentication, click the icon to turn on the switch and configure the following parameters. Protocol type: Select SASL PLAINTEXT from the drop-down list. _ SASL Authentication: Select PLAIN, SCRAM-SHA-256, or SCRAM-SHA- 512 from the drop-down list. Username/Password: Enter the username and password that are used to access the Kafka cluster. |
| Test Connectivity | Test whether network communication is established. |
| Data Scope | The organization to which the task is delivered. |
| Select Log Source | Select one or more types of log sources in theL og Source section and click the icon to add the selected log sources to theS elected Log Sources section. |
| Forwarding Field | Supported log forwarding fields: Standardized Field Original Field Standardized Field and Original Field |
| Forwarding Status | Turn on or turn off the switch to enable or disable the log forwarding feature. |

To create multiple log forwarding tasks, repeat the preceding steps. After you create a log forwarding task, you can view and manage the log forwarding task in the log forwarding task list. You can filter log forwarding tasks by data scope or **task name**. You can **turn on** or **turn off** the switches in the Status column to enable or disable log forwarding. You can **modify** or **delete** a log forwarding task. For a single log forwarding task, you can view the forwarding information about the task, including the log source, log type, total number of log entries that are sent, and the amount of data sent in the last 24 hours.

### 3.7 Create and manage a task

On the Tasks page, you can analyze and handle global security risks in a streamlined process. This facilitates security operations and management and helps accumulate experience in handling risks. This topic describes how to create and manage a task.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Handle > Tasks**.
4. On the Tasks page, view the overall information about tasks.
Total Tasks: the total number of tasks in Security Operations Center (SOC). The number is counted from the time when SOC starts to run until the current point in time. Tasks Pending Handling, Tasks Being Handled, and Handled Tasks: the number of tasks that are pending, the number of tasks that are being handled, and the number of tasks that are handled. The numbers are counted from the time when SOC starts to run until the current point in time. Task Completion Rate and On-time Task Completion Rate: the proportion of tasks that are completed to all tasks and the proportion of tasks that are completed on time to all tasks. The proportions are measured from the time when SOC starts to run until the current point in time. Handling Solutions: the number of handling solutions that are manually created from the time when SOC starts to run until the current point in time. The handling solutions include solutions that are manually created and are synchronized from handling records. Manually create a handling solution On the Tasks page, click **Handling Solutions**. On the Handling Solutions page, click
**Create Solution**. In the Create Solution panel, configure the parameters that are
described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Solution Name | The name of the handling solution. The name must be 1 to 200 characters in length. |
| Sharing Scope | The organization to which the handling solution is delivered. You can select one or more organizations from the drop-down list. |
| Solution Type | The type of the handling solution. Valid values: Threat Event Security alert Vulnerabilities Baselines Asset Risks Security Inspection Playbook Review |
| Problem Description | Describe the issue to address. This parameter supports rich text. You can enter text, format the text, and insert multimedia elements such as images or code blocks. |
| Solution | The handling solution. This parameter supports rich text. You can enter text, format the text, and insert multimedia elements such as images or code blocks. |
| Handled By | Select contacts from the drop-down list. |

Synchronize the solution from a handling record. For more information, see the Handle a task section of this topic. A manually created handling solution is in the **Published** state. You can directly reference the handling solution. A solution synchronized from a handling record is in the
**Pending Approval** state. Before you reference a solution synchronized from a handling
record, you must **approve** or **disable** the solution in SOC of the Apsara Uni-manager Operations Console. You can **delete** or **modify** a handling solution.
5. On the Tasks page, click **Create Task**. In the Create Task panel, configure the parameters
that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|

| Task Name | The name of the task. The name must be 0 to 128 characters in length. |
|---|---|
| Task Type | The type of the task. Valid values: Threat Event: You can click Select Risk Record to select a threat event within your data permission scope. Security alert: You can click Select Risk Record to select an alert within your data permission scope. Vulnerabilities: You can click Select Risk Record to select a vulnerability within your data permission scope. Baselines: You can click Select Risk Record to select a baseline within your data permission scope. Asset Risks: You can click Select Risk Record to select an asset within your data permission scope. Security Inspection: You can customize risk information and issue descriptions. |
| Delivering Organization | The organization to which the task is delivered. |
| Reference Risk Information | Specify whether to reference risk information. If you choose to reference risk information, the risk information is automatically filled in the Problem Description and Handling Suggestion fields. |
| Priority | The priority of the task. Valid values: Urgent, High, Medium, and Low. |
| Problem Description | Describe the issue to address. This parameter supports rich text. You can enter text, format the text, and insert multimedia elements such as images or code blocks. |
| Handling Suggestion | The handling suggestions. This parameter supports rich text. You can enter text, format the text, and insert multimedia elements such as images or code blocks. You can select Referenced Solution and select an existing solution from the knowledge base of handling solutions. |
| Handling Deadline | The deadline for the task. If the task is not completed before the deadline, the handling status of the task changes to Timed Out. |
| Handled By | Select contacts from the drop-down list. You can expand a multi-level organization to select contacts. |
| Notification Method | The notification method of the task. Valid values: DingTalk and Mail. |

The created task is displayed in the task list. On the Tasks page, you can handle all tasks. Search for a task Specify filter conditions to search for a task. You can specify the following filter conditions:
**Delivering Organization**, Task Type, Priority, Task Status, Handling Status, Task Name,
and Handled By. Handle a task i. Find the task that you want to manage and click the task name or **Handling Details** in the **Actions** column. ii. On the task details page, turn on **Received. Start to Handle**. In the message that appears, click OK. iii. Handle the task based on suggestions provided in the **Handling Suggestion** section and record the handling process in the **Handling Records** field. The handling record must be 0 to 2,048 characters in length.

**Note**

After you enter and save a record, you can select **Synchronize to Handling**
**Solutions**. If you encounter the same task later, you can directly reference the
handling solution as the handling suggestion. A handling record that is synchronized to the knowledge base of handling solutions becomes a handling solution and enters the **Pending Approval** state. In the **knowledge base of handling solutions** of SOC, set the
**Solution Status** filter condition to **Pending Approval**, find the solution, and
choose **More > Approve** or **More > Disable** in the **Actions** column. After a task is handled, the status of the task changes from **Handling** to **Completed**. In this case, you can no longer modify the task.

### 3.8 Report management

#### 3.8.1 Reports

The reports in the Security Operations Center (SOC) console displays the overall report statistics collected by SOC in a visualized manner. On the Reports page.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center (SOC)**. On the **Security Operations Center** page, select a region
from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Reports > Reports**.
4. The **Reports** tab displays statistics on reports, including the total number of reports,
number of daily reports, number of weekly reports, number of monthly reports, and number of custom periodic reports. You can also view the latest report generation time.
5. You can manage generated reports in a list. You can set the organization, data range, time
range, and task type to search for and filter the details by task name or report name. You can **download**, **preview**, and **delete** reports.

#### 3.8.2 Report tasks

This topic describes how to create a report task in Security Operations Center (SOC). Report tasks in SOC are displayed in a list.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Reports > Report Tasks**.
4. On the **Report Tasks** tab, click **Create Report Task**, configure the following parameters,
and then click **OK**.

| Parameter |   | Description |
|---|---|---|
| Task Name |   | The name of the report task. The name can be 0 to 128 characters in length. |
| Organization |   | The organization to which the report task belongs. |
| Task Description |   | The description of the report task. The description can be 0 to 1,024 characters in length. |

| Task Type | One-time Task | Report Statistical Period: Specify the time when the report task collects statistics. Report Name: Specify the name of the report. The name can be 0 to 128 characters in length. Data Scope: Select an organization from the drop- down list. Report Templates: Select a report template from the drop-down list. You can create a report template. Report Format: Word HTML Report Language: Select Simplified Chinese, Traditional Chinese, or English from the drop-down list. Storage Period: Specify the retention period of the report task. The default is 180 days. Specify whether to enable the report task. Specify whether to turn on Sending. Report Sending Time: After you enable this feature, you can customize the time period within which reports are sent. Recipients: Select an organization and contacts to receive the report. Notification Method: Select a method to send reports. Valid values: DingTalk and Email. |
|---|---|---|

|   | Periodic Task | Select Daily Report, Weekly Report, Monthly Report, or Custom from the drop-down list. Report Name: Specify the name of the report. The name can be 0 to 128 characters in length. Data Scope: Select an organization from the drop- down list. The remaining settings are the same as those of a one- time task. |
|---|---|---|

Click **Edit** in the Actions column of a report task to modify the report task. For example, you can modify the report name, data scope, report template, report format, storage period, and task status. Choose **More** > **View All** in the Actions column of a report task to view all reports in the task. You can also **download**, **preview**, **delete**, or **send** reports. Click **Download Latest** in the Actions column of a report task to download the report task information in the **HTML** format.

#### 3.8.3 Report templates

This topic describes how to create a Security Operations Center (SOC) report template and configure a custom report template.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center (SOC)**. On the **Security Operations Center (SOC)** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Reports > Report Templates**.
4. On the **Report Templates** tab, click **Create Report Template**, configure the following
parameters, and click **OK**.

| Parameter | Description |
|---|---|
| Template Name | The name of the template. The name can be 0 to 128 characters in length. |
| Template Description | The description of the template. The description can be 0 to 256 characters in length. |

| Organization | Select an organization from the drop-down list. |
|---|---|
| Security Risk Overview Analysis of Network Attack Details Analysis of Suspicious Process Details Analysis of Vulnerability Details Analysis of Baseline Details Analysis of Threat Event Details | The built-in security risk analysis templates. |

Click **Copy** in the Actions column of a report template to synchronize its content. Click **Delete** in the Actions column of a report template to delete it. Click **Edit** in the Actions column of a report template to modify its content.

### 3.9 Use the Rules module

#### 3.9.1 Create and manage an analysis rule

You can perform comprehensive association analysis on a large number of logs based on the analysis logic of an analysis rule to detect threats and risks and trace attack paths of multiphase attacks. This way, security administrators can obtain helpful risk information in an efficient and quick manner, thus improving the efficiency of security operations. This topic describes how to create and manage an analysis rule.

**Create a rule**

Security Operations Center (SOC) provides predefined rules based on regular business requirements. The predefined rules can only be viewed but cannot be modified. If the predefined rules cannot meet your business requirements, you can perform the following operations to create a rule:
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Global Platform Security >**
**Security Operations Center (SOC)**. On the **Security Operations Center (SOC)** page,
select a region from the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Policies > Analytic Rules**.
4. On the **Analytic Rules** page, click **Create Rule**. On the Create Rule page, configure the
parameters that are described in the following table.

| Parameter |   | Description |
|---|---|---|
|   | Organization | The organization to which the analysis rule belongs. |
|   | Data Scope | Specify the data scope. |

| baba Cloud Security-Situ areness |   |   |
|---|---|---|
| Basic Information |   |   |
|   | Threat Name | The name of the threat. |
|   | Threat Level | The level of the threat. Valid values: Information Suspicious Moderate Serious Urgent |
|   | Threat Type | The type of the threat. You can select one or more threat types. Valid values: Network Scanning Vulnerability Exploitation Malware Network Attack Suspicious Network Connection Suspicious Processes Unauthorized Privilege Escalation |
|   | ATT&CK ID | The IDs of one or more attacks that are involved in the Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) stages. |
|   | Description | The description of the threat. The description must be 0 to 256 characters in length. |
|   | Handling Suggestion | The suggestion on how to handle the threat. The suggestion must be 0 to 256 characters in length. |
|   |   | Time Series: Specify how the rule detects threats based on the occurrence time of the threats. Valid values: Same-period Unordered Match: The rule is used to detect the threats that occur within the same period of time. Cross-period Sequential Match: The rule is used to detect the threats that occur in sequence. Same-period Sequential Match: The rule is used to detect the threats that occur in sequence within the same period of time. |

|   |   | Associated Object: Specify the object on which the rule takes effect. Select Same Asset. By default, this option is selected. |
|---|---|---|
|   |   | Associate Analysis Condition: Specify the conditions to trigger the rule. Note On the right side of the Associate Analysis Condition section, you can click Add or Delete to add or delete a condition. You can also click Up or Down to move a condition. Association Type: Specify whether the conditions are required. If yes, select Necessary Condition. Log Scope: Specify the log scope, including the system types, log sources, log types, log subtypes, and log levels. Analysis Condition1: Separate multiple keywords with semicolons (;). Click Add on the right side to add an analysis condition. Aggregation Field: Security Operations Center (SOC) aggregates logs within the aggregation cycle based on the fields that you selected. Valid values: Standardized Field and Log Original Field. Associate Threat Intelligence: Specify whether to match threat intelligence. After you select Associate Threat Intelligence, select Source IP Address, Destination IP Address, Domain Name, and File MD5 Hash Value from the drop-down list. You can select multiple options. Log Threshold: Set the number of logs. |
| Rule Configuration | Rule Type: Select Association-based Analysis Rule. |   |
|   | Rule Type: Select Search-based Analysis Rule. | Log Scope: Specify the log scope, including the system types, log sources, log types, and log subtypes. |
|   |   | Search Condition: Specify the search condition of the rule. |
|   | Attack Phase | Valid values: Payload Delivery, Vulnerability Exploitation, Backdoor Installation, Command and Control, Scanning, Privilege Escalation, and Action on Objectives. |
|   | Time Range | You can set the unit to Minutes, Hours, or Days. The maximum is 365 days. |
|   | > Document Version: 2026082 |   |

|   | Execution Period | The interval at which the rule is executed. Default value: 5 minutes. You can set the unit to Minutes, Hours, or Days. The maximum is 365 days. |
|---|---|---|

5. **Optional.** If you want to verify the created rule, click **Quick Verify**.
6. Click **OK**.
The created rule is displayed in the rule list. You can modify or delete a custom rule based on your business requirements. To modify or delete a custom rule, find the rule that you want to manage and click **Edit** or **Delete** in the Actions column to modify or delete the rule.

**Manage a rule**

1. In the left-side navigation pane, choose **Policies > Analytic Rules**.
2. On the Analytic Rules page, find the rule that you want to view and view the following
information about the rule: rule ID, threat name, threat level, threat type, organization, data scope, ATT&CK ID, rule type, and rule status. You can also perform the following operations to manage a rule:

**Change the status of a rule**

On the Analytic Rules page, find the rule that you want to manage and click the switch icon in the **Status** column to enable or disable the rule.

**Modify or delete a rule**

On the Analytic Rules page, find the rule that you want to manage and click **Edit** or
**Delete** in the **Actions** column to modify or delete the rule.

**Copy a rule**

On the Analytic Rules page, find the rule that you want to manage and click **Copy** in the
**Actions** column. In the **Copy Rule** dialog box, select an organization from the
**Organization** drop-down list and click **OK**. This operation is applicable to specific rules.

**Note**

If one or more predefined rules are disabled, **the system prompts you to**

**confirm whether to enable them.**

The copied custom rules can be modified and deleted. The copied predefined rules can only be deleted.

#### 3.9.2 Create a response policy

You can create a response policy to handle threat events and security alerts (security alerts on the Operations Center page) in a timely manner, and monitor risk information related to threat events, security alerts (security alerts on the Operations Center page), security baselines, and security vulnerabilities. Real-time alert notifications are sent to specified contacts via DingTalk or email. This topic describes how to create a response policy.
1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > Security Operations Center**. On the **Security**
**Operations Center** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose Policies > Response Policies.
4. On the **Response Policy** page, click **Create Policy**.
5. In the **Create Policy** panel, configure the parameters that are described in the following
table and click **OK**. i. Basic Information The basic information about the policy.

| Parameter | Description |
|---|---|
| Organization | The organization to which the response policy belongs. |
| Policy Name | The name of the policy. |
| Policy Description | The description of the policy. |
| Policy Type | The type of the policy. Valid values: Threat Event Alert Vulnerability Baseline Important The policy settings vary depending on the policy type that you select. |

ii. Policy Settings Specify the trigger conditions of the response policy. The settings vary depending on the policy type that you select. a. Threat Event

| Parameter | Description |
|---|---|
| Data Scope | The impact scope of the policy. You need to select an organization. |
| Policy Cycle | The interval at which the response policy is matched and triggered. |
| Threat Event Name | The name of the threat that triggers the policy. |
| Threat Event Severity | The severity level of the threat. By default, all severity levels are selected. Valid values: Information, Suspicious, Moderate, Critical, and Urgent. You can select one or more severity levels. |
| Threat Event Type | The type of the threat. By default, all threat types are selected. Valid values: Network Scanning, Vulnerability Exploitation, Malware, Network Attack, and others. You can select one or more threat types. |
| Attacker IP Address | The source IP address that launches the threat. You can specify at most 10 IP addresses or CIDR blocks (/24) and separate them with commas (,). |
| Attacked IP Address | The IP address targeted by the threat. You can specify at most 10 IP addresses or CIDR blocks (/24) and separate them with commas (,). |
| Scanned Asset | The assets to which the response policy is applied. Default value: All Assets. Valid values: All Assets, Public IP Address/Mask, Private IP Address/Mask, Public IP Address, and Private IP Address. |
| Threat Behavior | The number of occurrences of the threat to trigger the response policy. |

b. Alert

| Parameter | Description |
|---|---|
| Data Scope | The impact scope of the policy. You need to select an organization. |
| Policy Cycle | The interval at which the response policy is matched and triggered. |
| Alert Name | The name of the alert that triggers the policy. |
| Alert Severity | The severity level of the alert. By default, all severity levels are selected. Valid values: Information, Suspicious, Moderate, Critical, and Urgent. You can select one or more severity levels. |
| Alert Type | The type of the alert. By default, all alert types are selected. Valid values: Unusual Logon, Malicious Script, Webshell, Suspicious Process, and others. You can select one or more alert types. |
| Attacker IP Address | The source IP address that triggers the alert. You can specify at most 10 IP addresses or CIDR blocks (/24) and separate them with commas (,). |
| Attacked IP Address | The targeted IP address. You can specify at most 10 IP addresses or CIDR blocks (/24) and separate them with commas (,). |
| Scanned Asset | The assets to which the response policy is applied. Default value: All Assets Valid values: All Assets, Instance Type, Instance Name, VPC, Public IP Address/Mask, Private IP Address/Mask, Public IP Address, and Private IP Address. |

c. Vulnerability

| Parameter | Description |
|---|---|

| Data Scope | The impact scope of the policy. You need to select an organization. |
|---|---|
| Policy Cycle | The interval at which the response policy is matched and triggered. |
| Vulnerability Name | The name of the vulnerability that triggers the policy. |
| Vulnerability Severity | The severity level of the vulnerability. By default, all severity levels are selected. Valid values: Low Risk, Medium Risk, and High Risk. You can select one or more severity levels. |
| Vulnerability Type | The type of the vulnerability. By default, all vulnerability types are selected. Valid values: Linux Software, Windows System, Web CMS, and Application(Urgent Vulnerability Included). You can select one or more vulnerability types. |
| CVE ID | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability. |
| Scanned Asset | The assets to which the response policy is applied. Default value: All Assets. Valid values: All Assets, Instance Type, Instance Name, VPC, Public IP Address/Mask, Private IP Address/Mask, Public IP Address, and Private IP Address. |
| Priority Score | The priority of the vulnerability. Valid values: 0 to 10. |
| Affected Assets | The number of affected assets to trigger the response policy. |

d. Baseline

| Parameter | Description |
|---|---|
| Data Scope | The impact scope of the policy. You need to select an organization. |
| Policy Cycle | The interval at which the response policy is matched and triggered. |
| Baseline Name | The name of the baseline that triggers the policy. |
| Baseline Severity | The severity level of the baseline. By default, all severity levels are selected. Valid values: Low Risk, Medium Risk, and High Risk. You can select one or more severity levels. |
| Baseline Type | The type of the baseline. By default, all baseline types are selected. valid values: hierarchy protection, Unauthorized Access, Internationally Agreed Best Practices for Security, Custom baseline, Best security practices, Weak password, and others. You can select one or more baseline types. |
| Scanned Asset | The assets to which the response policy is applied. Default value: All Assets. Valid values: All Assets, Instance Type, Instance Name, VPC, Public IP Address/Mask, Private IP Address/Mask, Public IP Address, and Private IP Address. |
| Affected Assets | The number of affected assets to trigger the response policy. |

iii. Response Settings By default, you can set **Response Method** only to **Notifications**. After you select this option, you need to specify the contacts and notification method. When the response policy is triggered, a notification is automatically sent to the specified contacts.

**Note**

The **Interactive Handling** option is available only on the SOC side and in Enterprise Cloud Operations mode.This option is unavailable to tenants in the Apsara Unimanager Management Console.

| Parameter | Description |
|---|---|
| Allowed Notifications | If a threat matches the response policy, the system sends only the specified number of notifications. |
| Notification Recipient | Select the contact to which notifications are sent in the corresponding organization. You can select multiple contacts. |
| Notification Method | The notification method. Valid values: DingTalk and Email. |

**Manage response policies**

1. In the left-side navigation pane, choose **Policies** > **Response Policies**.
2. On the Response Policies page, you can perform the following operations on the desired
policy: Click **Edit** or **Delete** in the **Actions** column of the policy to modify or delete the policy. Turn on or off the switch in the **Status** column of the policy to enable or disable the policy.

### 3.10 Use the Operations module

#### 3.10.1 Manage organization authorization

This topic describes how to enable global organization service-linked role authorization.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Global Platform Security > Security**
**Operations Center**. On the **Security Operations Center** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Operations > Organization Authorization**.
4. Turn on the switch next to **Global Organization SLR Authorization**. In the message that
appears, click **OK**. If Global Organization SLR Authorization is enabled, Security Operations Center (SOC) is automatically assigned the service-linked roles of all organizations, including organizations that are created in subsequent operations. SOC automatically collects information about the cloud assets and security data of all organizations. The global organization security administrator has the operations and management permissions on the cloud platform and cloud assets and security data of organizations. If Global Organization SLR Authorization is disabled, SOC is not assigned the servicelinked roles of the organizations. You must assign the service-linked role of at least one organization to SOC as an organization security administrator. Otherwise, the features of SOC are unavailable. After the service-linked role of the organization is assigned to SOC, SOC automatically collects information about the cloud assets and security data of the organization. The global organization security administrator has the operations and management permissions on the cloud platform and the organization.

**Important**

Organization service-linked role authorization has a higher priority than global organization service-linked role authorization. If the number of organizations for which global organization service-linked role authorization is enabled is different from the total number of organizations, you must modify the service-linked role authorization for the organizations.
