---
title: "Alibaba Cloud Apsara Stack V3.18.2 Cloud Security Network Detection and Response User Guide 20240606 (1)"
product_version: "V3.18.2"
doc_version: "20240606"
pdf_pages: 61
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Cloud Security Network Detection and Response User Guide 20240606 (1).pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E7%BD%91%E7%BB%9C%E7%9B%91%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Cloud%20Security%20Network%20Detection%20and%20Response%20User%20Guide%2020240606%20%281%29.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Cloud Security Network Detection and Response User Guide 20240606 (1)

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 Network Detection and Response
  - 3.1 Change the organization to view the menu items
  - 3.2 View traffic trends
  - 3.3 View traffic statistics
    - 3.3.1 View traffic at the Internet border
    - 3.3.2 View traffic at the internal network border
  - 3.4 Create packet capture tasks
  - 3.5 Search for logs
  - 3.6 View an attacker profile
  - 3.7 Use the Threat Detection module
    - 3.7.1 View threat detection results
    - 3.7.2 View logs of blocked traffic
  - 3.8 Use the Behavior Analysis module
    - 3.8.1 View DNS behavior analysis results
    - 3.8.2 View encrypted traffic analysis results
  - 3.9 Policy configuration
    - 3.9.1 Configure network-layer policies
    - 3.9.2 Configure application-layer policies
    - 3.9.3 Configure spoofing policies for port scanning
    - 3.9.4 Manage address books
    - 3.9.5 Configure an IDS rule
    - 3.9.6 Manage internal CIDR blocks for traffic monitoring
- 4 Apsara Stack Security configurations
  - 4.1 Log on to the Apsara Uni-manager Management Console
  - 4.2 System monitoring
  - 4.3 Rules
    - 4.3.1 Create and manage IPS rules
    - 4.3.2 Manage Anti-DDoS Service rules
    - 4.3.3 Manage Server Guard rules
    - 4.3.4 Create and manage WAF rules
  - 4.4 Configure alert settings
  - 4.5 Updates
    - 4.5.1 Upgrade center overview
    - 4.5.2 Update feature libraries or the version of Apsara Stack Security
    - 4.5.3 Download update packages
  - 4.6 Global configuration
    - 4.6.1 Configure the attack blocking feature
    - 4.6.2 Add a Server Guard account
  - 4.7 Cloud Firewall monitoring
  - 4.8 Account management
    - 4.8.1 Manage Apsara Stack tenant accounts
    - 4.8.2 Manage Alibaba Cloud accounts
- 5 文档标题缺失，请补全后重新导出
  - 5.1 Log on to the NDR console
  - 5.2 Use the traffic analysis feature
  - 5.3 Use the Threat Detection module
    - 5.3.1 View threat detection results
    - 5.3.2 View logs of blocked traffic
  - 5.4 Search for logs
  - 5.5 Use the Policy Configuration module
    - 5.5.1 Configure network-layer policies
    - 5.5.2 Configure application-layer policies
    - 5.5.3 Configure protection policies for port scanning and spoofing
    - 5.5.4 Create and manage address books

## 1 Usage notes

Before you log on to Apsara Stack Security Center, make sure that your computer meets the configuration requirements. For more information, see the Configuration requirements table of this topic. Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 2 Quick start

### 2.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. All roles in Apsara Stack Security Center are provided by default. You cannot create custom roles. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. For more information, see Default roles in Apsara Stack Security. Table 1. Default roles in Apsara Stack Security

| Role name | Description |
|---|---|
| System administrator of Apsara Stack Security Center | Manages and configures system settings for Apsara Stack Security Center. The system administrator has permissions to manage Apsara Stack accounts, synchronize data, configure alerts, and configure global settings. |
| Security administrator of Apsara Stack Security Center | Monitors the security status across Apsara Stack and configures security policies for each functional module of Apsara Stack Security. The security administrator has permissions on all features under Threat Detection, Network Security, Application Security, Server Security, Physical Server Security, and Asset Management. Note The permissions on Web Application Firewall (WAF) must be separately granted. |
| Department security administrator | Monitors the security status of cloud resources in a specific department and configures security policies for each functional module of Apsara Stack Security for this department. The department security administrator has permissions on all features under Threat Detection, Network Security, Application Security, Server Security, Physical Server Security, and Asset Management. In addition, the department security administrator can specify alert notification methods and alert contacts in the department. Note The permissions on WAF must be separately assigned. |
| Auditor of Apsara Stack Security Center | Conducts security audits across Apsara Stack. The auditor can view audit events and raw logs, configure audit policies, and access all features under Security Audit. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create a**
**user** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

## 3 Network Detection and Response

**Response**

### 3.1 Change the organization to view the menu items

**view the menu items**

The Network Detection and Response (NDR) console displays the full or partial menu based on the organization level. This topic describes how to change the organization to view the full menu. The menu display varies based on the organization and resource set that you select in the top navigation bar of the NDR console. For most organizations and resource sets, the system displays only the Log Retrieval and Threat Detection pages. Security administrator: views the full menu of the NDR console, such as the Traffic Trends, Traffic Analytics, Packet Capture, Log Retrieval, Attacker Profile, Threat Detection, Behavior Analysis, and Policy Configurations pages. Level-1 organization or lower: views the Log Retrieval and Threat Detection pages. If a level-1 or lower organization needs to view the full menu, change the organization to the security administrator level, which is the root level.

**Procedure**

1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, choose **Security >****Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. If you are using a level-1 or lower organization, click the
icon in the top navigation bar to change the organization to the security administrator level (root level) to view the full menu.

### 3.2 View traffic trends

The security administrator can analyze traffic trends and obtain the traffic rate, peaks, and troughs. The security administrator can also view the top five IP addresses that have the largest amount of traffic and identify malicious IP addresses. This topic describes how to view network traffic trends and statistics about inbound and outbound traffic.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. On the **Traffic Trends** page, select **Last 1 Hour**, **Last 24 Hours**, or **Last 7 Days** to query
traffic trends within a specific time range.
4. View network traffic information.
Network traffic trends You can view the network traffic trends in the time range that you selected. The network traffic trends include the trends of inbound traffic and outbound traffic. Inbound traffic and outbound traffic are measured in bit/s. Inbound traffic You can view information about Inbound Sessions, Inbound Applications, and Destination IPs with Most Requests. Outbound traffic You can view information about Outbound Sessions, Outbound Applications, and Source IPs with Most Requests.

### 3.3 View traffic statistics

#### 3.3.1 View traffic at the Internet border

Network Detection Response allows you to view traffic at the Internet border. You can use traffic information to identify abnormal Internet traffic. This topic describes how to view traffic at the Internet border.

**Prerequisites**

The **Network Traffic Monitoring System** module is purchased and deployed at the egress (ISW) of Apsara Stack. This module audits, analyzes, and manages both inbound and outbound traffic at Internet borders.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane,click **Internet Boundary Traffic Analysis**.
4. On the **Internet Boundary Traffic Analysis** page, view traffic at the Internet border and
block malicious traffic. i. Specify filter conditions.

| Position | Description |
|---|---|
| ① | Specify the traffic direction. Valid values: Inbound and Outbound. Inbound: The traffic flows from the Internet to the internal network. Outbound: The traffic flows from the internal network to the Internet. |
| ② | Specify whether you want to view the traffic by IP address or by application. Valid values: By IP and By Application. |
| ③ | Specify the time range. Valid values: Last 1 Hour, Last 24 Hours, and Last 7 Days. |

ii. View the details of the traffic at the Internet border.

**Traffic Statistics**

In the **Visits to IP** or **Visits from IP** section, you can view **Source IPs**, **Destination**
**IPs**, **Applications**, and **Traffic Risk**.
On the right side of the **Visits to IP** or **Visits from IP** section, you can view
**Average Traffic**, **Peak Traffic**, and traffic trends in a chart.

**Traffic List**

In the **Traffic List** section, you can sort IP addresses by traffic volume, number of destination IPs, number of applications, and number of sessions. View traffic information. If you specified **Inbound** for the traffic direction, you can view abnormal traffic on the **By Source IP** or **By Destination IP** tab of the Traffic List section. If you specified **Outbound** for the traffic direction, you can view abnormal traffic in the Traffic List section. Find the IP address whose traffic statistics you want to view and click **Details** in the
**Actions** column to view the traffic trends, basic information, and sessions of the IP
address.

#### 3.3.2 View traffic at the internal network border

**border**

Network Detection Response allows you to view traffic at the internal network border. You can use traffic information to identify suspicious traffic from the internal network. This topic describes how to view traffic at the internal network border.

**Prerequisites**

**q**

The **Network Traffic Monitoring System** module is purchased and deployed at the ingress (CSW) of Apsara Stack. This module audits, analyzes, and manages both inbound and outbound traffic routed over leased lines between on-premises data centers and virtual private clouds (VPCs).

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane,click **Intranet Boundary Traffic Analysis**.
4. On the **Intranet Boundary Traffic Analysis** page, view traffic at the internal network
border. i. Specify filter conditions.

| Position | Description |
|---|---|
| ① | Select a VPC name from the drop-down list. |
| ② | Specify the traffic direction. Valid values: Inbound and Outbound. Inbound: The traffic flows from the Internet to the internal network. Outbound: The traffic flows from the internal network to the Internet. |
| ③ | Specify whether you want to view the traffic by IP or by application. Valid values: By IP and By Application. |
| ④ | Specify the time range. Valid values: Last 1 Hour, Last 24 Hours, and Last 7 Days. |

ii. View the details of the traffic at the internal network border.

**Traffic Statistics**

In the **Visits to IP** or **Visits from IP** section, you can view **Source IPs**, **Destination**
**IPs**, **Applications**, and **Traffic Risk**.
On the right side of the **Visits to IP** or **Visits from IP** section, you can view
**Average Traffic**, **Peak Traffic**, and traffic trends in a chart.

**Traffic List**

In the **Traffic List** section, you can sort IP addresses by traffic volume, number of visited destination IPs, number of applications, and number of sessions. View traffic information. If you specified **Inbound** for the traffic direction, you can view abnormal traffic on the **By Source IP** or **By Destination IP** tab of the Traffic List section. If you specified **Outbound** for the traffic direction, you can view abnormal traffic in the Traffic List section. Find the IP address whose traffic statistics you want to view and click **Details** in the
**Actions** column to view the traffic trends, basic information, and sessions of the IP
address.

### 3.4 Create packet capture tasks

You can enable the packet capture feature to capture network data packets for specific IP addresses and ports and analyze the packets. This way, you can locate network faults, analyze attacks, and identify security risks to network communications. This topic describes how to create a packet capture task.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Packet Capture**.
4. Click **Create Packet Capture Task**.
5. In the **Create Packet Capture Task** panel, configure the parameters and click **Ok**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Task Name | The name of the packet capture task. We recommend that you enter an informative name, such as a name that indicates the purpose of the task. Note The value must contain 2 to 64 characters. |

| Maximum Bytes | The maximum number of bytes that can be captured in a packet. If the number of bytes in a packet exceeds the value of this parameter, the excess bytes are discarded. Note Maximum value: 10485760. Unit: bytes. |
|---|---|
| Duration (s) | The maximum duration of the packet capture task. Unit: seconds. Note Valid values: integers that are no greater than 300. |
| Protocol | The protocol of packets. Valid values: All TCP UDP ICMP |
| IP Address Type | The IP version of packets. Valid values: IPV4 and IPV6. |
| Direction | The direction of packets. Valid values: Bidirectional, In, and Out. |
| IP | The IP address of packets. |
| Port | The port of packets. Note Valid values: an integer from 1 to 65535, or 0. The value 0 indicates all ports. |

**What to do next**

On the **Packet Capture** page, you can view the created packet capture task and the task status. You can also download the details about the task or delete the task. To download the details or delete the task, find the task and click **Download** or **Delete** in the **Actions** column.

### 3.5 Search for logs

This topic describes how to search for logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security >****Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Log Retrieval**.
4. On the **Log Retrieval** page, specify search conditions. The following table describes the
conditions.

| Search condition | Description |
|---|---|
| Today | The time range to query. Valid values: Last Hour, Last 4 Hours, Today, Last 7 Days, Last 14 Days, Last 30 Days, and Custom. |
| All Departments | The department to which the logs belong. |
| Log Type | The type of logs that you want to search for. Valid values:S ecurity Event Log, Full Traffic Log, and Behavior Analysis Log. Default value: Security Event Log / ndr attack log. _ _ |
| Search Template | The template for log search. You can save search conditions as a template. |
| Enter the content | The content of the logs. You must use a query syntax that is similar to Lucene to specify the content. |

5. Click the
icon to view the search results.
**Clear**: If you no longer want to use the specified search conditions, you can click **Clear** to
clear the conditions.
**Save**: If you want to reuse the specified search conditions, you can click **Save** to save
the conditions as a template. In the dialog box that appears, specify a name for the template. The system displays logs in a column chart based on the specified search conditions. You can view the numbers of logs at different points in time within a specific time range. In the lower part of the Log Retrieval page, you can view the details of the returned logs. You can also click the parameters in the log list to add the parameters to search conditions. Select the fields that you want to display in the log list: Select the fields in the lower-left section of the Log Retrieval page. Export all fields of the returned logs: Click **Export All Fields** on the **Log Retrieval** page to export all fields of the returned logs. All fields of the returned logs are displayed in the lower-left section of the **Log Retrieval** page. The fields are divided into **Displayed**
**Fields** and **Optional Fields**.
Export the selected fields of the returned logs: Click **Export Selected Fields** on the **Log**
**Retrieval** page to export the selected fields of the returned logs. You can click
**Download Task Management** in the upper-right corner of the Log Retrieval page to
view export results. View log details: Click **Details** in the Actions column to view the details of a log. View field details: Click **Help Information** in the upper-right corner of the Log Retrieval page to view the details of a field. Decode fields: Click **Decoding Gadget** in the upper-right corner of the Log Retrieval page to convert fields that are encoded in a specific format into another format. The following encoding methods are supported: **Unicode encoding**, **UTF-8 encoding**,**URL**
**encoding**,**Hex encoding**, and **Base64 encoding**.
View the percentage of a field: Click the **Ellipse** icon next to a field in the lower-left section of the Log Retrieval page to view the percentage of the field. To hide the data, click the Ellipse icon again. View field descriptions: Move the pointer over a field in the lower-left section of the Log Retrieval page to view the description of the field.

### 3.6 View an attacker profile

The attacker profile feature analyzes and displays the basic information, threat intelligence, attack methods, attack targets, and attack processes of attacks that are initiated from an IP address in a centralized manner. This topic describes how to view an attacker profile.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security >****Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Attacker Profile**.
4. On the **Attacker Profile** page, specify search conditions. The following table describes the
search conditions.

| Search condition | Description |
|---|---|
| Last Hour | The time range to query. Valid values: Last Hour, Last 4 Hours, Last 8 Hours, Today, Last 7 Days, Last 14 Days, Last 30 Days, and Custom. |
| All Departments | The department to which the logs belong. Only a global organization security administrator can view the logs of all tenants. An organization security administrator can view only the logs of the tenant to which the department belongs. |
| Attack Result | The result of the attacks. Valid values: Attempt, Success, and Failure. |
| Threat Level | The severity of the attacks. Valid values: Low Risk, Medium Risk, and High Risk. |
| Please enter the attacker IP | The IP address from which the attacks are initiated. |

5. In the **List** section, view the search results.
6. Click a tab in the **List** section to view information about the attacks that are initiated from
the IP address. Click the **Basic Information** tab to view the basic information about the attacks. Click
**Attack Evidence Message Download** in the upper-right corner of the **Basic**
**Information** tab to download attack evidence messages. You can click **Download Task**
**Management** in the upper-right corner of the Attacker Profile page to view download
results. Click the **Attack Method** tab to view the attack details, including the attack events, attack results, destination IP addresses, target Elastic Compute Service (ECS) instances, departments, IP address types, and listening ports. Click the **Top Destination IPs** tab to view the top five hosts and IP addresses that receive the highest number of attacks. You can also view the number of attack attempts, the number of successful attacks, and the number of attacks by severity. Click the **Attack Process** tab to view the detailed process of the attacks. Click **>** on the
**Attack Process** tab to view the details of the attacks.

### 3.7 Use the Threat Detection module

**module**

#### 3.7.1 View threat detection results

This topic describes how to view threat detection results.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, click **Threat Detection**.
4. On the **Threat Detection** tab, specify search conditions.

| Search condition | Description |
|---|---|
| Time | The time range to query. Valid values: Last Hour, Last 4 Hours, Last 8 Hours, Today, Last 7 Days, Last 14 Days, Last 30 Days, and Custom. |
| Source IP | The IP address from which the attacks are initiated. |
| Threat Level | The severity of the attacks. Valid values: All Selection, Low Risk, Medium Risk, and High Risk. |
| Attack Type | The type of the attacks. Valid values: All Selection, Suspicious Connection, Command Execution, Brute-force Attack, Scan, Other, Information Leak, DoS Attack, Overflow Attack, Web Attack, Trojan Backdoor, Worm, Mining, Reverse Shell, Remote File Inclusion, Webshell Upload, SQL Injection, XSS Attack, Code Execution, CRLF, and Local File Inclusion. |

| Destination IP | The IP address that receives the attacks. |
|---|---|
| HTTP Response Code | The HTTP response code. |
| Rule ID | The rule ID. |
| Attack Result | The result of the attacks. Valid values: All Selection, Attempt, Success, and Failure. |
| Alert Source | The alert source. Valid values: All Selection, IDS, and WEBIDS. |
| Department | The first-level department. |
| Label | The label of the attacks. |
| Protection Status | The protection status. Valid values: All, Unhandled, Blocked, Added to Whitelist, and Ignored. |

5. Click **Query** to view the search results.
If you no longer require the specified search conditions, click **Reset** to clear the search conditions. The system analyzes the attacks that meet the search conditions and displays the analysis results in charts. The pie chart in the **Alert Type Chart** section displays the percentages of different alert types. The bar chart in the **Source IP | Destination IP Top 5** section displays the top five source IP addresses and destination IP addresses of attacks and the number of attacks. The chart in the **Alert Trend Chart** section displays the trend of the number of attacks in a specific time range. The attack list in the lower part of the Threat Detection page displays the details of the attacks. Select the columns that you want to view: Click Customize Column Display above the attack list to select the columns that you want to view in the attack list. View attack details: Click **Details** in the Actions column of an attack to view the details of the attack on the **Basic Information**, **Rule Details**, and **Original Alert List** tabs. Add a tag to an attack: Click **Label** in the Actions column of an attack to add a custom tag to the attack. Select a handling method for an attack: Click **Handle** in the Actions column of an attack to select a handling method for the attack. The following handling methods are supported: **Block**, **Threat Detection Whitelist**, and **Ignore**.
**Block**: blocks the source IP address of the attack and the X-Forwarded-For (XFF)
header by using a network-layer access control policy.

**Block the source IP address**

| Parameter | Description |
|---|---|
| Blocking Type | Select Network Blocking from the Blocking Type drop-down list. Then, you can create an access control policy to block the source IP address of the attack. |
| Source IP | The source IP address of the attack. |
| Destination IP | The IP address of the attacked asset. |
| Destination Port | The destination port of the attack. |
| Effective Duration | The validity period of the handling method. Valid values: One Day, One Week, One Month, Custom, and Permanent. |

**Block the XFF header**

| Parameter | Description |
|---|---|
| Blocking Type | Select XFF Blocking from the Blocking Type drop-down list. Then, you can create an access control policy to block the XFF header. |
| XFF Field | The XFF header. |
| Effective Duration | The validity period of the handling method. Valid values: One Day, One Week, One Month, Custom, and Permanent. |

**Threat Detection Whitelist**:
Add the source IP address of the attack, the attacked asset, the name of the attack, or the attack payload to the whitelist. The source IP address, attacked asset, attack name, and attack payload are evaluated by using the AND operator. No alerts are generated for attacks that match the whitelist rule. You can click **Whitelist** above the attack list to view the source IP address, attacked asset, attack name, and attack payload that are added to the whitelist. In the **Whitelist Management** dialog box, you can remove or add a whitelist rule. Effective Duration: the validity period of the handling method. Valid values: **One**
**Day**, **One Week**, **One Month**, **Custom**, and **Permanent**.
**Ignore**: ignores an alert. If the same attack is initiated again, a new alert is
generated. Each value in the Protection Status column corresponds to the handling method that you selected. By default, Unhandled is displayed. After you select a handling method, the value in the Protection Status column is updated. If you select **Block**, **Blocked** is displayed in the Protection Status column. If you select **Threat Detection Whitelist**,
**Trusted** is displayed. If you select **Ignore**, **Ignored** is displayed.
You can also select multiple attacks and click **Add to Whitelist (Batch Operation)**,
**Block (Batch Operation)**, or **Add Label (Batch Operation)** to handle the attacks.
Export the attack list: Click **Export All Records** above the attack list to export the returned data. You can click **Download Task Management** in the upper-right corner of the Threat Detection page to view export results.

#### 3.7.2 View logs of blocked traffic

Logs of blocked traffic record the traffic that hits a blocking policy. This topic describes how to view the logs of the blocked traffic.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, click **Threat detection**.
4. On the **Threat Detection** page, click **Blocking Log**.
5. On the **Blocking Log** tab, specify search conditions.
6. Click **Query**.
The bar chart in the Source IP | Destination IP Top 5 section displays the top five IP addresses that initiate the most attacks and the numbers of the attacks, and the top five IP addresses that receive the most attacks and the numbers of the attacks. The line chart in the RST Packet Statistics (Global) section displays the number of reset (RST) packets at different points in time. The chart in the **Protection Statistics (Count)** section displays the number of times that attacks are defended against within the specified time range. The log list in the lower part of the **Blocking Log** tab displays the details of the logs for the blocked traffic. You can also click **Export All Records** above the log list to export the logs. In the
**Actions** column of the log list, you can click **Block**, **Add to Whitelist**, and **Monitor** to
configure **Protection Action** for a log. If you select multiple logs, you can configure a protection action for multiple attacks at a time.
**Block**: When the system detects the traffic that hits a blocking policy, the system
generates an alert and blocks the traffic.
**Monitor**: When the system detects the traffic that hits a blocking policy, the system
generates an alert but does not block the traffic.
**Add to Whitelist**: No alerts are generated for the traffic from the IP address that is
added to the whitelist.

### 3.8 Use the Behavior Analysis module

**module**

#### 3.8.1 View DNS behavior analysis results

DNS behavior analysis can analyze the characteristics of suspicious domain names to detect suspicious DNS behaviors. This topic describes how to view DNS behavior analysis results.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security >****Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Behavior Analysis**.
4. On the **DNS Behavior Analysis** tab, specify search conditions.
You can configure the following parameters based on your business requirements: **Created**
**At**, **Department**, **Domain Name**, **Source IP**, and **Exception Type**.
5. Click **Query** to view DNS behavior analysis results in the following sections: **Statistics on**
**DGA Domain Names**, **Statistics on DNS Tunneling-involved Domain Names**, and
**Trends of Suspicious DNS Resolutions**. You can also view the DNS behavior list below
the sections. You can perform the following operations in the DNS behavior list: View the details of a suspicious DNS behavior: Click **Details** in the **Actions** column of a behavior to view the details of the behavior. Add a suspicious DNS behavior to the whitelist: Click **Add to Whitelist** in the **Actions** column of a suspicious behavior to add the behavior to the whitelist. You can also select multiple behaviors and click **Add to Whitelist (Batch Operation)** to add the behaviors to the whitelist at the same time. Export the DNS behavior list: Click **Export All Records** above the DNS behavior list to export the DNS behavior list. You can click **Download Task Management** in the upperright corner of the Behavior Analysis page to view export results. View the whitelist: Click **Whitelist** above the DNS behavior list to view the details of the whitelist. In the **Whitelist** dialog box, you can search for, add, or remove a behavior. Configure a rule to detect DNS tunneling attacks: Click **DNS Tunneling Detection Rule** above the DNS behavior list. In the Configure DNS Tunneling Detection Rule dialog box, configure the Request Scope(Minutes), Requests(Minutes), and DNS Domain Name Length(Character) parameters and click **OK**.

#### 3.8.2 View encrypted traffic analysis results

Encrypted traffic analysis can detect suspicious encrypted traffic by analyzing the characteristics of traffic. This topic describes how to view encrypted traffic analysis results.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane, click **Behavior Analysis**.
4. On the **Encrypted Traffic Analysis** tab, specify search conditions.
You can configure the following parameters based on your business requirements: **Created**
**At**, **Department**, **Source IP**, **Destination IP**, and **Attack Tool Type**.
5. Click **Query** to view encrypted traffic analysis results in the following sections: **Analysis of**
**Encrypted Traffic Types**, **Type Analysis of Attack Tools** , and **Source IP |**
**Destination IP Top 5**. You can also view the encrypted traffic list below the sections.
You can perform the following operations in the encrypted traffic list: View the details of encrypted traffic: Click **Details** in the **Actions** column of a record of encrypted traffic to view the details of the record. Add encrypted traffic to the whitelist: Click **Add to Whitelist** in the **Actions** column of a record of suspicious encrypted traffic to add the encrypted traffic to the whitelist. You can also select multiple records of suspicious encrypted traffic and click **Add to Whitelist**
**(Batch Operation)** below the list to add the traffic to the whitelist at the same time.
Export encrypted traffic list: Click **Export All Records** above the encrypted traffic list to export all records of suspicious encrypted traffic. View the whitelist: Click **Whitelist** above the encrypted traffic list to view the details of the whitelist.

### 3.9 Policy configuration

#### 3.9.1 Configure network-layer policies

This topic describes how to create and view network-layer policies.

**Create network-layer policies**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security >****Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Policy Configurations**.
4. Create network-layer policies.
Create a single network-layer policy On the **Network Layer Policy** tab, click **Create Policy**. In the Create Policy panel, configure parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |
| Policy Description | The description of the policy. |
| Direction | The direction of traffic on which the policy takes effect. |
| Policy Type | The type of the policy. Valid values: Source IP Only, Destination IP Only, and Source IP, Destination IP/Port. |

| Rules | The method to configure rules for the policy. Valid values: Manual Input, Import File, and Address Book. You can configure multiple rules for a policy. Note You can specify IPv4 or IPv6 addresses. You cannot specify both types of IP addresses at the same time. |
|---|---|
| Whether to Enable | Specifies whether to enable the policy. |
| Protection Action | The action for the policy. Valid values: Allow, Monitor, and Block. |
| Effective Duration | The validity period of the policy. Valid values: Permanent, One Day, One Week, One Month, and Custom. |

Import incremental network-layer policies a. On the **Network Layer Policy** tab, select **Download Template** from the **Import**
**Policy** drop-down list.
b. Fill in the network-layer policy template. Then, on the Network Layer Policy tab, select
**Incremental Import** from the Import Policy drop-down list . In the dialog box that
appears, click **Select File**, select the network-layer policy template, and then click **OK**.

**View network-layer policies**

On the **Network Layer Policy** tab, you can filter and view network-layer policies based on information such as the action, traffic direction, rule name, rule description, rule ID, UUID, and expiration time. You can also perform the following operations: Enable or disable a policy: Find the policy that you want to enable or disable and turn on or turn off the switch in the **Whether to Enable** column. indicates that the policy is enabled. indicates that the policy is disabled. Modify a policy: Find the policy that you want to modify and click **Edit** in the **Actions** column. You can modify only disabled policies. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. You can delete only disabled policies. Enable global network-layer policies: Turn on **Global Network Policies** above the policy list. Enable threat intelligence filtering: Turn on **Threat Intelligence Filtering** above the policy list. After threat intelligence filtering is enabled, the system blocks the traffic that matches threat intelligence. Manage multiple network-layer policies at a time: You can **delete**, **enable**, **disable**, or
**export** multiple network-layer policies at a time.
Export all network-layer policies: Click **Full Export** in the lower part below the policy list.

#### 3.9.2 Configure application-layer policies

This topic describes how to create an application-layer policy, view application-layer policies, and view policies for web application detection.

**Create an application-layer policy**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Policy Configurations**.
4. On the **Application Layer Policy** tab, click the **HTTP Custom Policy** tab.
5. Click **Create Policy**. In the Create Policy panel, configure the parameters and click **OK**.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |
| Direction | The direction of traffic on which the policy takes effect. Valid values: Inbound and Outbound. |
| Matching Condition | The matching condition for the policy. A matching condition is the core element of a policy. A policy matches traffic against the conditions and then allows, monitors, or blocks the traffic that meets the conditions. You must configure the Matching Field, Logical Operator, Matching Content, and Case Sensitive or Not parameters to add a matching condition. |
| Protection Action | The action for the policy. Valid values: Allow, Monitor, and Block. |
| Whether to Enable | Specifies whether to enable the policy. |
| Effective Duration | The validity period of the policy. Valid values: Permanent, One Day, One Week, One Month, and Custom. |

**View application-layer policies**

On the **HTTP Custom Policy** tab of the **Application Layer Policy** tab, you can search for and view application-layer policies based on the action, status, direction, matching field content, creation time, and expiration time. You can also perform the following operations: Enable or disable a policy: Find the policy that you want to enable or disable and click the or icon in the **State** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled. Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. Delete multiple application-layer policies at a time: Select multiple application-layer policies and select **Batch Delete** from the Batch Operation drop-down list.

**View policies for web application detection**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Network Security > Network Detection**
**and Response**. On the **Network Detection and Response** page, select a region from
the **Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Policy Configurations**.
4. On the **Application Layer Policy** tab, click the **Web Application Detection**
**Configuration** tab.
5. On the Web Application Detection Configuration tab, configure the **Startup Status** and
**Protection type** parameters to filter and view policies.

> **Note:** You can also use the **advanced search** feature to search for policies for web application detection based on the **rule name**, **rule ID**, and **threat level**.

You can find a policy in the policy list and click the or icon in the **Effective Status** column to enable or disable the policy. The icon indicates that the policy is **enabled**. The icon indicates that the policy is **disabled**.
6. In the upper-right corner of the policy list, click the
or icon for **Web Application**
**Detection**.
WEB应用检测配置 The icon indicates that all policies are **enabled**. The icon indicates that all policies are **disabled**.

#### 3.9.3 Configure spoofing policies for port scanning

**scanning**

A spoofing policy for port scanning lures attackers to launch attacks against ports that do not exist. This way, attacks are exposed. This topic describes how to configure spoofing policies for port scanning.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security** and choose **Network Security > Network**
**Detection Response**. On the authorization page for **Network Detection Response**,
select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, click **Policy Configurations**.
4. On the **Port Scan Spoofing Policy** tab, click **Create Policy**. In the Create Policy panel,
configure parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | The organization to which the policy belongs. Select an organization from all organizations of Network Detection Response (NDR). |
| Address Type | The type of the address that you want to protect. The address consists of an IP address and ports that are configured in a service. You can obtain the address by using the port of the security component. Valid values: WAF, Public SLB, EIP, and Custom. |
| Protection Address | The address that you want to protect. |
| Port Whitelist | The ports in the whitelist. Spoofing policies for port scanning are applied only to the ports that are not added to the whitelist. |
| Protection Mode | The protection mode. Valid values: Monitor and Protect. If you set the Protection Mode parameter to Monitor, NDR generates alerts but does not block attacks. If you set the Protection Mode parameter to Protect, NDR generates alerts and blocks attacks. |

**View spoofing policies for port scanning**

On the **Port Scan Spoofing Policy** tab, you can filter and view spoofing policies for port scanning based on information such as the department, address type, rule name, rule description, rule ID, and UUID. You can also perform the following operations: Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. Delete multiple policies at a time: Select multiple policies and click **Batch Delete**. Enable or disable a policy: Find the policy that you want to enable or disable and click the or icon in the **Status** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled.

#### 3.9.4 Manage address books

An address book is a collection of IP addresses. You can create an address book to improve protection configuration efficiency. This topic describes how to create an address book and query address books in the address book list.

**Create an address book**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane,click **Policy Configuration**.
4. On the **Address Book Management** tab, click **Create IP Address Book**. In the Create
Address Book panel, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Address Book Name | The name of the address book. |
| Address Book Type | The method to add addresses to the address book. Valid values: File Import and Manual Input. |
| Select File | If you set the Address Book Type parameter to File Import, click Select File to import an on-premises file. Note After you import the on-premises file, the IP addresses contained in the file are displayed in the address book list. However, the name of the file is not displayed. |
| IP Address | If you set the Address Book Type parameter to Manual Input, enter 32-bit IP addresses. Specify only IPv4 addresses or only IPv6 addresses in an address book. An address book cannot contain both IPv4 addresses and IPv6 addresses. |
| Address Book Description | The description of the address book. |

**Query address books**

On the **Address Book Management** tab, query address books in the address book list. Search for an address book: Specify an address book name, address book description, or IP address above the address book list to search for an address book. Modify an address book: Click **Edit** in the **Actions** column of an address book. Delete an address book: Click **Delete** in the **Actions** column of an address book. Delete multiple address books at the same time: Select the address books that you want to delete and click **Batch Delete**.

#### 3.9.5 Configure an IDS rule

Network Detection Response provides built-in intrusion detection system (IDS) rules. You can configure custom IDS rules based on your business requirements and network environment. This topic describes how to create and manage IDS rules.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane,click **Policy Configuration**.
4. On the **Intrusion Detection Rule** tab, click **Create Rule**. In the Create Rule panel,
configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Rule Name | The name of the IDS rule. We recommend that you enter a name that can help you identify and manage the IDS rule in an efficient manner. |
| Rules Engine | The rules engine that you want to use. Valid values:B asic Policies and Virtual Patches. |
| Attack Type | The type of the attack that you want to detect by using the IDS rule. |
| Severity | The severity level of the attack. Valid values:L ow, Medium, and High. |
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability to be listed in the rule. Note CVE provides a list of the public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Application | The name of the attacked application. |
| Rule Mode | The mode of the rule. Valid values: Packet and Traffic. |
| Direction | The direction of traffic that you want to monitor by using the IDS rule. Valid values: Inbound and Outbound, Inbound, and Outbound. |

| Rule Content | The content of the IDS rule. Use the Snort syntax to specify the content. Note To prevent a negative impact on your business, make sure that you enter valid content for the IDS rule. |
|---|---|
| Rule Description | The description of the rule. We recommend that you enter information such as the purpose or impact of the rule. |
| Description | The remarks for the rule. We recommend that you enter information such as the purpose or impact of the rule. |

After you create an IDS rule, you can view and manage the rule in the IDS rule list. View the details of an IDS rule You can click the **Filter** icon above the IDS rule list to filter IDS rules. Find the rule whose details you want to view and click **Details** in the **Actions** column. Enable an IDS rule Find the rule that you want to enable and turn on the switch in the **Status** column to change the status of the rule from **Disable** to **Enable**. Disable an IDS rule If a rule cannot meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Status** column to change the status of the rule from **Enable** to **Disable**.

#### 3.9.6 Manage internal CIDR blocks for traffic monitoring

**monitoring**

CIDR blocks are configured for Network Traffic Monitoring System. Security administrators can change the CIDR blocks for traffic monitoring based on business requirements. The settings of CIDR blocks apply only to a data center that is deployed in the region to which the specific CIDR block belongs. This topic describes how to add and manage internal CIDR blocks for traffic monitoring.

> **Note:** Changes to CIDR block settings immediately take effect without the need for intervention of security administrators.
> If you add the same CIDR block on the traffic collection CIDR block setting page and the region setting page, make sure that you select the same region on both pages.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Network Security > Network Detection Response**. On the **Network**
**Detection Response** page, select a region from the **Region** drop-down list and click
**Access with Authorized Role**.
3. In the left-side navigation pane,click **Policy Configuration**.
4. On the **IP Address Pool of Internal Assets** tab, click **Add**.
5. In the **New** dialog box, configure the parameters and click **OK**. The following table
describes the parameters.
**CIDR Block**: Enter a CIDR block for traffic monitoring.

> **Note:** Enter a valid CIDR block. You cannot enter a CIDR block that is already configured for the region.

**Region**: Select the region of the data center.
After you complete the preceding configurations, you can manage the internal CIDR block in the CIDR block list. View the internal CIDR block for traffic monitoring and region information Select a **region**, enter the internal CIDR block that you want to modify or delete, and then click **Search**. Modify the internal CIDR block for traffic monitoring Find the internal CIDR block that you want to modify and click **Edit** in the **Actions** column. Delete the internal CIDR block for traffic monitoring Find the internal CIDR block that you want to delete and click **Delete** in the **Actions** column. configurations

## 4 Apsara Stack Security configurations

**configurations**

### 4.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

### 4.2 System monitoring

configurations On the Monitoring Overview tab, you can monitor cloud services to identify abnormal services at the earliest opportunity. This facilitates service O&M. This topic describes how to view the monitoring data.
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

### 4.4 Configure alert settings

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
configurations
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. Click the **AEGIS** tab, configure alert rules, and then click **Save**.

| Alert type | Alert subtype | Alert level | Notificati on method | Frequenc y |
|---|---|---|---|---|
| Vulnerability | Linux software vulnerability Windows system vulnerability Web-CMS vulnerability Application vulnerability Urgent vulnerability | Low Medium High | Email DingTal k messag e | 5 minutes 10 minutes 30 minutes 1 hour 1 day 1 week |
| Baseline risk | High-risk exploit MLPS compliance Best security practices Weak password | Low Medium High |   |   |
| Asset exposure | Vulnerability Non-vulnerability | All levels |   |   |
| Intrusion alert | Suspicious process Webshell Unusual logon Exception Threat intelligence Malicious process Unusual network connection Abnormal account Application intrusion event Cloud threat detection Precision defense Malicious script Persistent webshell Application threat detection | Low Medium High |   |   |

configurations

| Application whitelist event | Unauthorized process start | All levels |   |   |
|---|---|---|---|---|
| Tampering | File modification File addition File deletion | All levels |   |   |

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

If your Apsara Stack environment is inaccessible over the Internet, you can manually import update packages to update feature libraries or the version of Apsara Stack Security. configurations a. Set Upgrade Package Import to **Offline Manual Import** and click **Generate Upgrade**
**Identifier**. Then, download update packages. For more information, see Download
update packages. b. Click Import Upgrade Package and drag the downloaded update packages to the dotted box. You can also click the icon to upload the update packages.

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

Batch update: On the **Feature Library Upgrade** tab, click **One-click upgrade**. Update a service in Apsara Stack Security: Find the service that you want to update on the **Feature Library Upgrade** tab and click **Upgrade now** in the **Operation** column. configurations After the update is complete, the status of the service is **Upgrade successful**. If the update fails, you can click **Upgrade Records** in the **Operation** column to find the versions of the feature libraries that failed to be updated and click **Retry** in the Operation column. If the update is successful, you can perform the following operations: On the **Feature Library Upgrade** tab, find the service and click **Version Details** in the **Operation** column to view the versions of the updated rule libraries. You can click **Restart Upgrade** to update a rule library in a feature library. In the **Feature Library Upgrade Records**panel, find the feature library that you want to view and click **Details** in the **Operation** column to view the details of the feature library update package. You can find a rule library and click **Restart**
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

1. Log on to the .
2. In the left-side navigation pane, choose **Operation > Upgrade packages**.
3. In the **Upgrade Mode** section on the **Upgrade packages** page, click **Standard Mode**.
4. In the **Identifier of Apsara Stack Security Version** search box, enter the version of
Apsara Stack Security to which you want to update and click **Obtain Rule Package** to obtain update packages.

> **Note:** For more information about how to obtain the version identifier of Apsara Stack Security, click **How to Obtain Upgrade Package** below the search box.
> If you use Apsara Stack Security V3.12, V3.13, or V3.14, you must enter the version identifier of Apsara Stack Security in the Identifier of Apsara Stack Security Version search box to obtain update packages.

5. In the **Download Upgrade Package** section, find the update packages that you want to
download and click **Download** in the **Operation** column. After the update packages are downloaded, upload the update packages to Apsara Stack Security Center. In Apsara Stack Security Center, perform update-related operations to complete the update.

**Advanced mode**

1. Log on to the .
2. In the left-side navigation pane, choose **Operation > Upgrade packages**.
3. In the **Upgrade Mode** section on the **Upgrade packages** page, click **Advanced Mode**.
4. In the **Identifier of Apsara Stack Security Version** section, select Apsara Stack Security
from the drop-down list on the left and select the version of the update package that you want to download from the drop-down list on the right.
5. In the **Download Upgrade Package** section, find the update packages that you want to
configurations download and click **Download** in the **Operation** column. After the update packages are downloaded, upload the update packages to Apsara Stack Security Center. In Apsara Stack Security Center, perform update-related operations to complete the update.

### 4.6 Global configuration

#### 4.6.1 Configure the attack blocking feature

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

#### 4.6.2 Add a Server Guard account

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

configurations

| Organization UID or Primary Key | The UID or primary key of the organization to which the Server Guard account belongs. |
|---|---|

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
After the inspection is complete, you can perform the following operations: Click **Details** in the **Actions** column of **Internet Firewall (ICFW)**, **VPC Firewall**
**(CCFW)**, or **Traffic Monitoring (Beaver)** to view the status of each system.
Click **Inspect Now** in the **Actions** column of **Internet Firewall (ICFW)**, **VPC Firewall**
**(CCFW)**, or **Traffic Monitoring (Beaver)** to perform inspection on each system.
5. In the **Service Monitoring** section, configure the monitoring settings on the **ICFW** or
**CCFW** tab.

**ISW-side Cloud Firewall (ICFW)**

configurations a. In the **Traffic Forwarding Configuration - Service CIDR Block** section, click **Add**, configure the parameters, and then click **OK**.

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

After the Alibaba Cloud account is added, you can view the account in the account list. You can **modify** or **remove** the account. 后重新导出

## 5 文档标题缺失，请补全后重新导出

### 5.1 Log on to the NDR console

The Apsara Stack base contains various IP addresses, such as static server IP addresses, switch IP addresses, and the virtual IP addresses (VIPs) that are dynamically requested for Server Load Balancer (SLB) and XGW gateways. Specific IP addresses must not be exposed to the Internet or the data center networks of users. Otherwise, security risks may occur. You can use Network Detection and Response (NDR) to control access to the IP addresses from the Internet and the data centers. This topic describes how to log on to the NDR console.

**Procedure**

1. 2. 3. 4.
5. In the upper-right corner, click **Security Management** and choose **Network Security** >
**Network Detection and Response**.

### 5.2 Use the traffic analysis feature

**feature**

The Network Detection and Response (NDR) console allows you to analyze the traffic of the Apsara Stack base. You can use traffic information to identify unusual Internet traffic and block malicious access. This topic describes how to view the traffic at the Internet border and block IP addresses with a few clicks.

**Prerequisites**

**NDR** is purchased and deployed at the egress (ISW) of Apsara Stack. NDR audits, analyzes,
and manages both inbound and outbound traffic at the Internet border.

**Procedure**

1. Log on to the NDR console.
2. In the left-side navigation pane, click **Traffic Analysis**. On the Traffic Analysis page, view
the information about the traffic at the Internet border and block malicious IP addresses. 后重新导出 i. Specify the conditions to filter traffic.

| Condition | Description |
|---|---|
| 1 | Specify the traffic direction. Valid values: Inbound and Outbound. Inbound: The traffic flows from the Internet to the internal network. Outbound: The traffic flows from the internal network to the Internet. |
| 2 | Specify whether you want to view the traffic by IP address or by application. Valid values: By IP and By Application. |
| 3 | Specify the time range. Valid values: Last 1 Hour, Last 24 Hours, and Last 7 Days. |

ii. View the details about the traffic at the Internet border.

**Traffic Statistics**

In the **Visits from IP or Visits to IP** section, view **Source IPs**, **Destination IPs**, and **Applications**. On the right side of the Visits from IP or Visits to IP section, view **Average Traffic**,
**Peak Traffic**, and traffic trends in a chart.

**Traffic List**

In the **Traffic List** section, you can sort IP addresses by traffic volume, number of visited source or destination IP addresses, number of applications, and number of sessions. View traffic information. If you specify **Inbound** for the traffic direction, view traffic information on the **By**
**Source IP** or **By Destination IP** tab of the Traffic List section.
If you specify **Outbound** for the traffic direction, view traffic information in the Traffic List section. Find the IP address whose traffic details you want to view and click **Details** in the
**Actions** column to view the traffic trends, basic information, and sessions of the IP
address.
3. In the Traffic List section, find the IP address that you want to manage and click **Block IP**
**Addresses** in the **Actions** column.

> **Note:** Quick blocking is supported only when you specify the **By IP** mode.

后重新导出

| Parameter | Description |
|---|---|
| Type | Specify the blocking type and the IP address type. Valid values for the blocking type: Whitelist: If you select Whitelist, you must set the Destination IP parameter. Blacklist: If you select Blacklist, you must set the Source IP parameter. Source IP is the source IP address in the traffic list. Valid values for the IP address type: IPv4 and IPv6. |
| Source IP | Specify the source IP address that you want to block. If the traffic direction is set to Inbound, the system obtains source IP addresses from network sessions. |
| Destination IP | Specify the destination IP address that you want to block. If the traffic direction is set to Outbound, the system obtains destination IP addresses from network sessions. You cannot change the destination IP addresses that the system obtains from network sessions. |
| Destination Port | Specify the destination port that is used with the specified destination IP address. |
| Block Duration | Specify the blocking duration. Valid values: 1 Day, 7 Days, and 30 Days. |
| Reason | Specify the blocking description. The value can be up to 100 characters in length. |

4. On the **Traffic Analysis** page, click **View Blocked IPs** in the upper-right corner to view
the list of blocked IP addresses.

### 5.3 Use the Threat Detection module

**module**

#### 5.3.1 View threat detection results

This topic describes how to view threat detection results.
1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Threat Detection**. On the **Threat Detection** tab,
specify the search conditions and click **Query**. You can view the following information about detected threats.

| Category | Description |
|---|---|

后重新导出

| Alert Type Chart | The alert type chart displays the number of attacks by alert type. |
|---|---|
| Source IP \| Destination IP Top 5 | The bar chart in the Source IP \| Destination IP Top 5 section displays the top five IP addresses that initiate the most attacks and the numbers of the attacks, and the top five IP addresses that receive the most attacks and the numbers of the attacks. |
| Alert Trend Chart | The alert trend chart displays the number of attacks within a specified time range. |
| Attack list | The attack list displays the attack details. You can perform the following operations in the attack list: To select the columns that you want to display, clickC ustomize Column Display. To handle an attack, click Handle in the Actions column. You can use one of the following handling methods: Block, Threat Detection Whitelist, and Ignore. Block: blocks IP addresses from which attacks are initiated by using network-layer access control policies. You can set the validity period of the handling method to One Day, One Week, One Month, Custom, or Permanent. Ignore: ignores an alert. If the same attack is initiated again, a new alert is generated. Threat Detection Whitelist: adds an IP address to the whitelist. After the IP address is added to the whitelist, no alerts are generated for the attacks from the IP address or on the IP address. You can click Whitelist above the attack list to view the added IP address. You can also remove or add an IP address in the Whitelist Management dialog box. Each state that is displayed in the Protection Status column in the attack list corresponds to the selected handling method. By default, Unhandled is displayed. After a handling method is selected, a state that corresponds to the selected handling method is displayed. If you select Block, Blocked is displayed in the Protection Status column. If you select Threat Detection Whitelist, Added to Whitelist is displayed. If you select Ignore, Ignored is displayed. To add a custom label to an attack, click Label in the Actions column. Click Details in the Actions column to view Basic Information, Rule Details, and Original Alert List. Click Export All Records to export the attack list. |

#### 5.3.2 View logs of blocked traffic

Logs of blocked traffic record the traffic that matches a blocking policy. This topic describes how to view logs of blocked traffic.
1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Threat Detection**. On the **Blocking Log** tab, specify
the search conditions and click **Query**. 后重新导出
3. View the following logs of blocked traffic.
封禁日志查看

| Category | Description |
|---|---|
| Source IP\|Destination IP TOP 5 (marked 1 in the preceding figure) | The bar chart in the Source IP\|Destination IP TOP 5 section displays the top five IP addresses that initiate the most attacks and the numbers of the attacks, and the top five IP addresses that receive the most attacks and the numbers of the attacks. |
| RST Packet Statistics (Global) (marked 2 in the preceding figure) | The line chart in the RST Packet Statistics (Global) section displays the number of reset (RST) packets at different points in time. |
| Protection Statistics (Count) (marked 3 in the preceding figure) | The column chart in the Protection Statistics (Count) section displays the number of protection sessions at a specific time. |
| List of logs of blocked traffic (marked 4 in the preceding figure) | You can view the details of logs of blocked traffic or manage logs of blocked traffic. You can perform the following operations in the log list: Export logs of blocked traffic: Click Export All Records above the log list. Configure protection actions for blocked traffic: Find a log of blocked traffic that you want to manage and click Block, Add to Whitelist, or Monitor in the Actions column. Note If the Source parameter is set to Port spoofing, the traffic is blocked by default and you cannot modify the protection action. If you want to allow an IP address, go to the Policy Configurations page and create a network-layer policy to allow the IP address. Block: When the system detects traffic that matches a blocking policy, the system generates an alert and blocks the detected traffic. Monitor: When the system detects traffic that matches a blocking policy, the system generates an alert but does not block the detected traffic. Add to Whitelist: After you add an IP address to the whitelist, the system does not block the traffic of the IP address any more. Configure a protection action for multiple traffic objects: Select multiple logs of blocked traffic and click Add to Whitelist (Batch Operation), Block (Batch Operation), or Monitor (Batch Operation). |

### 5.4 Search for logs

This topic describes how to search for and view logs.
1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Log Queries**.
后重新导出
3. On the **Log Retrieval** page, specify search conditions. The following table describes the
search conditions.

| Search condition | Description |
|---|---|
| Time | Specify the time range of the logs that you want to search for. Valid values: Last Hour, Last 4 Hours, Last 8 Hours, Today, Last 7 Days, Last 14 Days, Last 30 Days, and Custom. |
| Log Type | Specify the type of the logs that you want to search for. Valid values: Security Event Log, Full Traffic Log, and Behavior Analysis Log. Default value: Security Event Log / ndr attack log. _ _ |
| Search Template | Specify the template for log search. You can save search conditions as a template. |
| Content | Enter the content of the logs. You must use a query syntax that is similar to Lucene to specify the content. |

4. Click the
icon to view the search results.

> **Note:** **Clear**: If you no longer want to use the specified search conditions, you can click **Clear** to clear the conditions.
> **Save**: If you want to reuse the specified search conditions, you can click **Save** to save the conditions as a template. In the Save Template dialog box, specify a name for the template.

The system displays logs in a column chart based on the specified search conditions. You can view the numbers of logs at different points in time within a specific time range. In the lower part of the Log Retrieval page, you can view the details of the returned logs. You can also click the parameters in the log list to add the parameters to search conditions. Select the fields that you want to display in the log list: Select the fields in the lower-left corner of the Log Retrieval page. Export all fields of the returned logs: Click **Export All Fields** on the **Log Retrieval** page to export all fields of the returned logs. All fields of the returned logs are displayed in the lower-left column of the **Log Retrieval** page. The fields are divided into **Displayed**
**Fields** and **Optional Fields**.
Export the selected fields of the returned logs: Click **Export Selected Fields** on the **Log**
**Retrieval** page to export the selected fields of the returned logs.
View log details: Click **Details** in the Actions column to view the details of a log. View field details: Click **Help Information** in the upper-right corner of the Log Retrieval page to view the details of a field. Decode fields: Click **Decoding Gadget** in the upper-right corner of the Log Retrieval page to convert fields that are encoded in a specific format into another format. 后重新导出 View the percentage of a field: Click the **ellipse icon** next to a field in the lower-left corner of the Log Retrieval page to view the percentage of the field. To hide the data, click the ellipse icon again. View field descriptions: Move the pointer over a field to view the description of the field.

### 5.5 Use the Policy Configuration module

**module**

#### 5.5.1 Configure network-layer policies

You can configure network-layer policies based on your business requirements to detect attacks that match the policies. This topic describes how to create and manage network-layer policies.

**Create a network-layer policy**

1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Policy Configurations**.
3. On the **Network Layer Policy** tab, click **Create Policy**. In the Create Policy panel,
configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |
| Policy Description | The description of the policy. |
| Direction | The parameter is set to Inbound. |
| Policy Type | The type of the policy. Valid values: Source IP Only, Destination IP Only, and Source IP, Destination IP/Port. |

后重新导出

| Rules | The method to configure rules for the policy. If you set Policy Type to Source IP Only or Destination IP Only, you must use one of the following methods to add IP addresses. If you select Manual Input, you must enter multiple CIDR blocks. Separate multiple CIDR blocks with commas (,). You can enter up to 100 CIDR blocks, and the CIDR blocks must be unique. If you select Import File, you must upload a .csv file. If you select Address Book, you must select a created address book. If you set Policy Type to Source IP, Destination IP/Port, you must enter an IP address and a port in the following format: Source IP address\|Source port-Destination IP address\|Destination port. |
|---|---|
| Whether to Enable | Specifies whether to enable the policy. |
| Protection Action | The action for the policy. Valid values: Allow, Monitor, and Block. |
| Effective Duration | The validity period of the policy. Valid values: Permanent, One Day, One Week, One Month, and Custom. |

> **Note:** To import multiple policies at a time, you can perform the following operations: Choose **Import Policy** > **Download Template**, enter the content of the network-layer policy template, and then choose **Import Policy** > **Incremental Import**. Then, click **Select** **File**, import the network-layer policy template, and click **OK**.

**Manage network-layer policies**

1. On the **Network Layer Policy** tab, search for and view network-layer policies based on the
policy action, direction, creation time, and expiration time. You can also enter the rule name, rule description, rule ID, and UUID in the search box to search for and view networklayer policies.
2. To manage the queried policies, perform the following operations:
Enable or disable a policy: Find the policy that you want to enable or disable and click the or icon in the **Whether to Enable** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled. Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. You can edit only disabled policies. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. You can delete only disabled policies. 后重新导出 Enable a policy: In the upper-right corner of the policy list, click the icon for **Network**
**Policy Switch**.
Manage multiple network-layer policies at a time: Choose **Batch Delete**, **Batch Enable**,
**Batch Disable**, or **Batch Export** from the Batch Operation drop-down list.
Export all network-layer policies: In the lower-left corner of the policy list, click **Full**
**Export**.

#### 5.5.2 Configure application-layer policies

You can configure application-layer policies based on your business requirements to detect the attacks that match the policies. This topic describes how to create and manage application-layer policies.

**Create an application-layer policy**

1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Policy Configurations**.
3. On the **Application Layer Policy** tab, click **Create Policy**. In the Create Policy panel,
configure the parameters and click **OK**. The following table describes the parameters. 4.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |
| Direction | The direction of traffic on which the policy takes effect. Valid values: Inbound and Outbound. |
| Match Condition | The matching condition for the policy. A matching condition is the core element of a policy. A policy matches traffic against the conditions and then allows, monitors, or blocks the traffic that meets the conditions. You must configure the Matching Field, Logical Operator, Matching Content, and Case Sensitive or Not parameters to add a matching condition. |
| Protection Action | The action for the policy. Valid values: Allow, Monitor, and Block. |
| Whether to Enable | Specifies whether to enable the policy. |
| Effective Duration | The validity period of the policy. Valid values: Permanent, One Day, One Week, One Month, and Custom. |

**Manage application-layer policies**

1. On the **Application Layer Policy** tab, search for and view application-layer policies based
on information such as the action, status, direction, matching field content, creation time, and expiration time. 后重新导出
2. Perform the following operations on the policies that are returned:
Enable or disable a policy: Find the policy that you want to enable or disable and click the or icon in the **State** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled. Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. Delete, enable, disable, or export multiple application-layer policies at a time: Select multiple application-layer policies and choose **Batch Delete**, **Batch Enable**, **Batch**
**Disable**, or **Batch Export** from the Batch Operation drop-down list.

#### 5.5.3 Configure protection policies for port scanning and spoofing

**scanning and spoofing**

You can configure protection policies for port scanning and spoofing to detect the attacks that match the policies. This topic describes how to create and manage protection policies for port scanning and spoofing.

**Create a protection policy for port scanning and spoofing**

1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Policy Configurations**.
3. On the **Port Scan Spoofing Policy** tab, click **Create Policy**. In the Create Policy panel,
configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Address Type | The type of the address that you want to protect. The address consists of an IP address and ports that are configured in a service. You can obtain the address by using the port of the security component. Valid values: WAF, Public SLB, EIP, and Custom. |
| Protection Address | The address that you want to protect. |
| Port Whitelist | The ports in the whitelist. Protection policies for port scanning and spoofing are applied only to the ports that are not added to the whitelist. |
| Protection Mode | The protection action. Valid values: Monitor: If you select this option, the system does not protect against port scanning and spoofing but generates an alert. Protect: If you select this option, the system protects against port scanning and spoofing and generates an alert. |

后重新导出

**Manage protection policies for port scanning and spoofing**

1. On the **Port Scan Spoofing Policy** tab, search for and view policies by address type. You
can also enter the protection address, rule ID, or protection port in the search box to search for policies.
2. Perform the following operations on the policies that are returned:
Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. Delete multiple policies at a time: Select multiple policies and click **Batch Delete**. Enable or disable a policy: Find the policy that you want to enable or disable and turn on or turn off the switch in the **Status** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled.

#### 5.5.4 Create and manage address books

An address book is a collection of IP addresses. You can create an address book to improve protection configuration efficiency. This topic describes how to create and manage address books.

**Create an IP address book**

1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Policy Configurations**.
3. On the **Address Book Management** tab, click **Create IP Address Book**. In the Create
Address Book panel, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Address Book Name | The name of the address book. |
| Address Type | The method to add addresses to the address book. Valid values: File Import and Manual Input. |
| Select Attachments | If you set the Address Type parameter to File Import, click Select File to import an on-premises file. Note After you import the on-premises file, the IP addresses contained in the file are displayed in the address book list. However, the name of the file is not displayed. |

后重新导出

| IP Address | If you set the Address Type parameter to Manual Input, enter 32-bit IP addresses. Specify only IPv4 addresses or only IPv6 addresses in an address book. An address book cannot contain both IPv4 addresses and IPv6 addresses. |
|---|---|
| Address Book Description | The description of the address book. |

**Manage address books**

1. On the **Address Book Management** tab, specify an address book name, address book
description, or IP address to search for and view address books.
2. Perform the following operations on the address books that are returned:
Search for an address book: Specify an address book name, address book description, or IP address above the address book list to search for an address book. Modify an address book: Find the address book that you want to modify and click **Edit** in the **Actions** column. Delete an address book: Find the address book that you want to delete and click **Delete** in the **Actions** column. Delete multiple address books at a time: Select the address books that you want to delete and click **Batch Delete**.
