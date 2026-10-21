---
title: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Network Detection and Response User Guide 20241024"
product_version: "V3.18.3"
doc_version: "20241024"
pdf_pages: 20
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Network Detection and Response User Guide 20241024.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Cloud%20Security%20Network%20Detection%20and%20Response%20User%20Guide%2020241024.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Network Detection and Response User Guide 20241024

## Table of Contents

- 1 Log on to the Apsara Infrastructure Management console
- 2 Use the traffic analysis feature
- 3 Use the Threat Detection module
  - 3.1 View threat detection results
  - 3.2 View logs of blocked traffic
- 4 Search for logs
- 5 Use the Policy Configuration module
  - 5.1 Configure network-layer policies
  - 5.2 Configure application-layer policies
  - 5.3 Configure protection policies for port scanning and spoofing
  - 5.4 Create and manage address books

Infrastructure Management cons ole

## 1 Log on to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.
Infrastructure Management cons ole

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Platforms > Apsara Infrastructure Management Framework**.
s feature

## 2 Use the traffic analysis feature

**feature**

The Network Detection and Response (NDR) console allows you to analyze the traffic of the Apsara Stack base. You can use traffic information to identify unusual Internet traffic and block malicious access. This topic describes how to view the traffic at the Internet border and block IP addresses with a few clicks.

**Prerequisites**

**NDR** is purchased and deployed at the egress (ISW) of Apsara Stack. NDR audits, analyzes,
and manages both inbound and outbound traffic at the Internet border.

**Procedure**

1. Log on to the NDR console.
2. In the left-side navigation pane, click **Traffic Analysis**. On the Traffic Analysis page, view
the information about the traffic at the Internet border and block malicious IP addresses. i. Specify the conditions to filter traffic.

| Condition | Description |
|---|---|
| 1 | Specify the traffic direction. Valid values: Inbound and Outbound. Inbound: The traffic flows from the Internet to the internal network. Outbound: The traffic flows from the internal network to the Internet. |
| 2 | Specify whether you want to view the traffic by IP address or by application. Valid values: By IP and By Application. |
| 3 | Specify the time range. Valid values: Last 1 Hour, Last 24 Hours, and Last 7 Days. |

s feature ii. View the details about the traffic at the Internet border.

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

| Parameter | Description |
|---|---|
| Type | Specify the blocking type and the IP address type. Valid values for the blocking type: Whitelist: If you select Whitelist, you must set the Destination IP parameter. Blacklist: If you select Blacklist, you must set the Source IP parameter. Source IP is the source IP address in the traffic list. Valid values for the IP address type: IPv4 and IPv6. |
| Source IP | Specify the source IP address that you want to block. If the traffic direction is set to Inbound, the system obtains source IP addresses from network sessions. |
| Destination IP | Specify the destination IP address that you want to block. If the traffic direction is set to Outbound, the system obtains destination IP addresses from network sessions. You cannot change the destination IP addresses that the system obtains from network sessions. |

s feature

| Destination Port | Specify the destination port that is used with the specified destination IP address. |
|---|---|
| Block Duration | Specify the blocking duration. Valid values: 1 Day, 7 Days, and 30 Days. |
| Reason | Specify the blocking description. The value can be up to 100 characters in length. |

4. On the **Traffic Analysis** page, click **View Blocked IPs** in the upper-right corner to view
the list of blocked IP addresses. tion module

## 3 Use the Threat Detection module

**module**

### 3.1 View threat detection results

This topic describes how to view threat detection results.
1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Threat Detection**. On the **Threat Detection** tab,
specify the search conditions and click **Query**. You can view the following information about detected threats.

| Category | Description |
|---|---|
| Alert Type Chart | The alert type chart displays the number of attacks by alert type. |
| Source IP \| Destination IP Top 5 | The bar chart in the Source IP \| Destination IP Top 5 section displays the top five IP addresses that initiate the most attacks and the numbers of the attacks, and the top five IP addresses that receive the most attacks and the numbers of the attacks. |
| Alert Trend Chart | The alert trend chart displays the number of attacks within a specified time range. |

tion module

| Attack list | The attack list displays the attack details. You can perform the following operations in the attack list: To select the columns that you want to display, clickC ustomize Column Display. To handle an attack, click Handle in the Actions column. You can use one of the following handling methods: Block, Threat Detection Whitelist, and Ignore. Block: blocks IP addresses from which attacks are initiated by using network-layer access control policies. You can set the validity period of the handling method to One Day, One Week, One Month, Custom, or Permanent. Ignore: ignores an alert. If the same attack is initiated again, a new alert is generated. Threat Detection Whitelist: adds an IP address to the whitelist. After the IP address is added to the whitelist, no alerts are generated for the attacks from the IP address or on the IP address. You can click Whitelist above the attack list to view the added IP address. You can also remove or add an IP address in the Whitelist Management dialog box. Each state that is displayed in the Protection Status column in the attack list corresponds to the selected handling method. By default, Unhandled is displayed. After a handling method is selected, a state that corresponds to the selected handling method is displayed. If you select Block, Blocked is displayed in the Protection Status column. If you select Threat Detection Whitelist, Added to Whitelist is displayed. If you select Ignore, Ignored is displayed. To add a custom label to an attack, click Label in the Actions column. Click Details in the Actions column to view Basic Information, Rule Details, and Original Alert List. Click Export All Records to export the attack list. |
|---|---|

### 3.2 View logs of blocked traffic

Logs of blocked traffic record the traffic that matches a blocking policy. This topic describes how to view logs of blocked traffic.
1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Threat Detection**. On the **Blocking Log** tab, specify
the search conditions and click **Query**.
3. View the following logs of blocked traffic.
封禁日志查看

| Category | Description |
|---|---|
| Source IP\|Destination IP TOP 5 (marked 1 in the preceding figure) | The bar chart in the Source IP\|Destination IP TOP 5 section displays the top five IP addresses that initiate the most attacks and the numbers of the attacks, and the top five IP addresses that receive the most attacks and the numbers of the attacks. |

tion module

| RST Packet Statistics (Global) (marked 2 in the preceding figure) | The line chart in the RST Packet Statistics (Global) section displays the number of reset (RST) packets at different points in time. |
|---|---|
| Protection Statistics (Count) (marked 3 in the preceding figure) | The column chart in the Protection Statistics (Count) section displays the number of protection sessions at a specific time. |
| List of logs of blocked traffic (marked 4 in the preceding figure) | You can view the details of logs of blocked traffic or manage logs of blocked traffic. You can perform the following operations in the log list: Export logs of blocked traffic: Click Export All Records above the log list. Configure protection actions for blocked traffic: Find a log of blocked traffic that you want to manage and click Block, Add to Whitelist, or Monitor in the Actions column. Note If the Source parameter is set to Port spoofing, the traffic is blocked by default and you cannot modify the protection action. If you want to allow an IP address, go to the Policy Configurations page and create a network-layer policy to allow the IP address. Block: When the system detects traffic that matches a blocking policy, the system generates an alert and blocks the detected traffic. Monitor: When the system detects traffic that matches a blocking policy, the system generates an alert but does not block the detected traffic. Add to Whitelist: After you add an IP address to the whitelist, the system does not block the traffic of the IP address any more. Configure a protection action for multiple traffic objects: Select multiple logs of blocked traffic and click Add to Whitelist (Batch Operation), Block (Batch Operation), or Monitor (Batch Operation). |

## 4 Search for logs

This topic describes how to search for and view logs.
1. Log on to the Network Detection and Response (NDR) console.
2. In the left-side navigation pane, click **Log Queries**.
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
View log details: Click **Details** in the Actions column to view the details of a log. View field details: Click **Help Information** in the upper-right corner of the Log Retrieval page to view the details of a field. Decode fields: Click **Decoding Gadget** in the upper-right corner of the Log Retrieval page to convert fields that are encoded in a specific format into another format. View the percentage of a field: Click the **ellipse icon** next to a field in the lower-left corner of the Log Retrieval page to view the percentage of the field. To hide the data, click the ellipse icon again. View field descriptions: Move the pointer over a field to view the description of the field.

## 5 Use the Policy Configuration module

**Configuration module**

### 5.1 Configure network-layer policies

**policies**

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
| Rules | The method to configure rules for the policy. If you set Policy Type to Source IP Only or Destination IP Only, you must use one of the following methods to add IP addresses. If you select Manual Input, you must enter multiple CIDR blocks. Separate multiple CIDR blocks with commas (,). You can enter up to 100 CIDR blocks, and the CIDR blocks must be unique. If you select Import File, you must upload a .csv file. If you select Address Book, you must select a created address book. If you set Policy Type to Source IP, Destination IP/Port, you must enter an IP address and a port in the following format: Source IP address\|Source port-Destination IP address\|Destination port. |

| Whether to Enable | Specifies whether to enable the policy. |
|---|---|
| Protection Action | The action for the policy. Valid values: Allow, Monitor, and Block. |
| Effective Duration | The validity period of the policy. Valid values: Permanent, One Day, One Week, One Month, and Custom. |

> **Note:** To import multiple policies at a time, you can perform the following operations: Choose **Import Policy** > **Download Template**, enter the content of the network-layer policy template, and then choose **Import Policy** > **Incremental Import**. Then, click **Select** **File**, import the network-layer policy template, and click **OK**.

**Manage network-layer policies**

1. On the **Network Layer Policy** tab, search for and view network-layer policies based on the
policy action, direction, creation time, and expiration time. You can also enter the rule name, rule description, rule ID, and UUID in the search box to search for and view networklayer policies.
2. To manage the queried policies, perform the following operations:
Enable or disable a policy: Find the policy that you want to enable or disable and click the or icon in the **Whether to Enable** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled. Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. You can edit only disabled policies. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. You can delete only disabled policies. Enable a policy: In the upper-right corner of the policy list, click the icon for **Network**
**Policy Switch**.
Manage multiple network-layer policies at a time: Choose **Batch Delete**, **Batch Enable**,
**Batch Disable**, or **Batch Export** from the Batch Operation drop-down list.
Export all network-layer policies: In the lower-left corner of the policy list, click **Full**
**Export**.

### 5.2 Configure application-layer policies

**policies**

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
on information such as the action, status, direction, matching field content, creation time, and expiration time.
2. Perform the following operations on the policies that are returned:
Enable or disable a policy: Find the policy that you want to enable or disable and click the or icon in the **State** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled. Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. Delete, enable, disable, or export multiple application-layer policies at a time: Select multiple application-layer policies and choose **Batch Delete**, **Batch Enable**, **Batch**
**Disable**, or **Batch Export** from the Batch Operation drop-down list.

### 5.3 Configure protection policies for port scanning and spoofing

**for port scanning and spoofing**

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

**Manage protection policies for port scanning and spoofing**

1. On the **Port Scan Spoofing Policy** tab, search for and view policies by address type. You
can also enter the protection address, rule ID, or protection port in the search box to search for policies.
2. Perform the following operations on the policies that are returned:
Edit a policy: Find the policy that you want to edit and click **Edit** in the **Actions** column. Delete a policy: Find the policy that you want to delete and click **Delete** in the **Actions** column. Delete multiple policies at a time: Select multiple policies and click **Batch Delete**. Enable or disable a policy: Find the policy that you want to enable or disable and turn on or turn off the switch in the **Status** column. The icon indicates that the policy is enabled. The icon indicates that the policy is disabled.

### 5.4 Create and manage address books

**books**

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
| IP Address | If you set the Address Type parameter to Manual Input, enter 32-bit IP addresses. Specify only IPv4 addresses or only IPv6 addresses in an address book. An address book cannot contain both IPv4 addresses and IPv6 addresses. |
| Address Book Description | The description of the address book. |

**Manage address books**

1. On the **Address Book Management** tab, specify an address book name, address book
description, or IP address to search for and view address books.
2. Perform the following operations on the address books that are returned:
Search for an address book: Specify an address book name, address book description, or IP address above the address book list to search for an address book. Modify an address book: Find the address book that you want to modify and click **Edit** in the **Actions** column. Delete an address book: Find the address book that you want to delete and click **Delete** in the **Actions** column. Delete multiple address books at a time: Select the address books that you want to delete and click **Batch Delete**.
