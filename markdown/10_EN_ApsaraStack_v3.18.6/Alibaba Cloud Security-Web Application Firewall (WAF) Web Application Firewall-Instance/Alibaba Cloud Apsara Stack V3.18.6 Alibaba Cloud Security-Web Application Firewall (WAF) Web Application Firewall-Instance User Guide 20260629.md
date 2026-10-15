---
title: "Alibaba Cloud Security-Web Application Firewall (WAF) Web Application Firewall-Instance User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 54
source_pdf: "bbb612f7cc54680b_Alibaba Cloud Apsara Stack V3.18.6 Alibaba Cloud Security-Web Application Firewall (WAF) Web Applica"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99-%E4%BC%81%E4%B8%9A%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20Web%20Application%20Firewall-Instance%20User%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Security-Web Application Firewall (WAF) Web Application Firewall-Instance User Guide 20260629

## Table of Contents

- 1 Usage notes
- 2 Getting Started
  - 2.1 Log on to the Apsara Uni-manager Management Console
  - 2.2 User roles and permissions
  - 2.3 Log on to the Apsara Uni-manager Operations Console
  - 2.4 Getting started
- 3 Create an instance
- 4 Statistics information
  - 4.1 Protection overview
  - 4.2 Access status monitoring
  - 4.3 Export protection reports
  - 4.4 Attack statistics
  - 4.5 Traffic trends
- 5 Protection logs
  - 5.1 Attack detection logs
  - 5.2 HTTP flood protection logs
  - 5.3 System operation logs
  - 5.4 Access logs
  - 5.5 Log download management
  - 5.6 Query logs by IP address
- 6 Protection configurations
  - 6.1 Protected website management
    - 6.1.1 Manage websites
    - 6.1.2 Manage VIPs
  - 6.2 Protection policies
  - 6.3 Global custom rules
  - 6.4 Custom rules
  - 6.5 Tamper-proofing rules
  - 6.6 HTTP flood protection
    - 6.6.1 HTTP flood protection rules
    - 6.6.2 HTTP flood whitelist
  - 6.7 Threat intelligence
  - 6.8 Certificate management
  - 6.9 Data masking
- 7 System settings
  - 7.1 Online backup
  - 7.2 Instance system settings
- 8 System information
  - 8.1 Node status
    - 8.1.1 Loads
    - 8.1.2 Network information
    - 8.1.3 Detection status
    - 8.1.4 Forwarding status
    - 8.1.5 Disk status
    - 8.1.6 Historical data query
  - 8.2 System firmware information

## 1 Usage notes

Before you log on to Apsara Stack Security Center, make sure that your computer meets the configuration requirements. For more information, see the **Configuration requirements** table of this topic. Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 2 Getting Started

### 2.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from a deployment engineer. A web browser is available. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your
browser and press the Enter key.
2. Enter your username and password.
You can obtain the username and password that are used to log on to the Apsara Unimanager Management Console from the operations administrator. The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. The password must be 8 to 20 characters in length and contain at least two of the following character types: Letters Digits Special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your logon scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Re-enter the username and password as described in Step 2 and click **Log On**. c. Enter the six-digit MFA verification code and click **Authenticate**. Scenario 2: You log on to the Apsara Uni-manager Management Console after MFA is enabled and an MFA device is bound. Enter a six-digit MFA verification code and click **Authenticate**. For more information about how to enable MFA and bind an MFA device, see the
**Manage MFA** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 User roles and permissions

The user roles provided by Web Application Firewall (WAF) have the permissions to use independent WAF. This topic describes the user roles. All roles are default user roles. You cannot create custom roles. Before you log on to the WAF
  - Instance console, make sure that your account is assigned the required roles.
Default tenant-side user roles

| Role name | Description |
|---|---|
| Organization security administrator | Uses Security Operations Center (SOC) to manage the security of hosts, applications, and networks for an organization. This role also has the permissions to manage security services related to Elastic Compute Service (ECS). |
| Global organization security administrator | Uses SOC to conduct security management for Apsara Stack and all tenants, and manages security services related to ECS. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create**
**users** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.3 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .

### 2.4 Getting started

This topic helps you get started with the features of Web Application Firewall (WAF) - Instance. WAF uses intelligent semantic analysis algorithms to identify web attacks. WAF also uses a learning model to enhance its analysis capabilities and meet your daily security protection requirements without relying on traditional rule libraries. The following content describes the procedure for using WAF:
1. Create a WAF instance. For more information, see Create an instance.
2. Create custom WAF protection rules.
WAF provides default protection policies. You can also configure custom protection policies based on your business requirements. For more information about how to configure protection policies, see Protection policies. For more information about how to create custom rules, see Custom rules. For more information about how to configure HTTP flood protection rules, see HTTP flood protection.
3. Add websites that you want WAF to protect.
WAF can protect Internet websites and virtual private cloud (VPC) websites. For more information, see Manage websites.
4. View WAF protection results.
For more information about how to view the overall protection information, see Protection overview. For more information about how to view web attack detection logs, see Attack detection logs. For more information about how to view HTTP flood protection logs, see HTTP flood protection logs.

## 3 Create an instance

This topic describes how to create a Web Application Firewall (WAF) instance.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a **region** and click **Access with Authorized Role**.
3. On the Web Application Firewall page, click **Create Instance**. In the panel that appears,
configure the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Organization | The organization to which the instance belongs. |
| Resource Set | The resource set to which the instance belongs. |
| Available Zones | The zone of the instance. |
| Instance Name | The instance name. |
| Detection Engine Specifications | The specifications of the detection engine. Valid values:S hared ECS and Dedicated ECS. |
| Detection Engine Version | When Detection Engine Specifications is set to Shared ECS, you can select Basic Edition or Premium Edition. When Detection Engine Specifications is set to Dedicated ECS, you can select Basic Edition, Premium Edition, or Enterprise Edition. |
| CPU | When Detection Engine Specifications is set to Shared ECS, this parameter is set to X86 by default and cannot be changed. When Detection Engine Specifications is set to Dedicated ECS, you can select X86 or ARM. |

| Detection Engine Resources | The detection engine resources. The value of this parameter varies based on the edition and specifications of the detection engine. When Detection Engine Specifications is set to Shared ECS: The basic edition provides 8 cores and 16 GB of memory. The premium edition provides 16 cores and 32 GB of memory. When Detection Engine Specifications is set to Dedicated ECS: The basic edition provides 2 cores and 4 GB of memory. The premium edition provides 4 cores and 8 GB of memory. The enterprise edition provides 24 cores and 48 GB of memory. |
|---|---|
| Estimated QPS | This parameter indicates the maximum number of HTTP requests that can be processed by the instance per second. The value varies depending on the Detection Engine Specifications (Shared ECS or Dedicated ECS ), Detection Engine Version (Basic Edition, Premium Edition, or Enterprise Edition), and Available Zones parameters. You can increase the number of detection engines to improve the QPS. Formula: EstimatedQPS = Numberofzones × QPSofthecorrespondingenginespe cificationsandedition × Numberofenginesinasinglezone(thedefaultva lueis2) Example: When two zones, Shared ECS, and Basic Edition are specified and the number of detection engines in a single zone is 3, the estimated QPS is 6,000 (2 × 1,000 × 3). QPS values of different detection engine specifications and editions: When Detection Engine Specifications is set to Shared ECS: The basic edition provides 1,000 HTTP QPS. The premium edition provides 4000 HTTP QPS. When Detection Engine Specifications is set to Dedicated ECS: The basic edition provides 1,000 HTTP QPS. Each instance can protect up to two virtual private clouds (VPCs). The premium edition provides 2,500 HTTP QPS. Each instance can protect up to six VPCs. The enterprise edition provides 20,000 HTTP QPS. Each instance can protect up to 46 VPCs. |
| Number of Detection Engines | The number of detection engines in a single zone. Valid values: 2 to 16. |

| Protocol Version | Specify the IP protocol stack supported by the Web Application Firewall (WAF) instance. IPv4: Only IPv4 traffic is protected. You cannot upgrade an IPv4 WAF instance to a dual-stack WAF instance. Dual Stack: Both IPv4 traffic and IPv6 traffic are protected. The IPv6 capability of a dual-stack WAF instance can only be used to connect to an Application Load Balancer (ALB) instance. |
|---|---|
| VPC Protection Mode | When Detection Engine Specifications is set to Dedicated ECS, you can select Single VPC Protection or Multiple VPC Protection. If you select Multiple VPC Protection, you can click Add a VPC below the parameter to add VPCs. |
| VPC 1 | Select a VPC to be protected by WAF. |
| vSwitch1-1 | Select a zone in the VPC. |

**What to do next**

After you create an instance, you can perform the following operations in the instance list: View the information about the instance In the instance list on the Web Application Firewall page, you can view the information of the WAF instance that you created, including the instance name, access entry, VPC, number of detection nodes, QPS, and whether an update is available. You can view the WAF QPS quota in the upper-right corner of the page.

**Important**

When the **Update Available** column of a WAF instance displays **Available**, and you directly perform the update, data errors may occur. We recommend that you upgrade the instance before you perform subsequent operations. To upgrade the WAF instance, log in to the Apsara Uni-manager Operations Console and choose **Cloud Services > WAF Instance Management > WAF Instance**
**Management** in the **Cloud Shield Operations Center**. For more information, see
**Web Application Firewall - Instance O&M Guide > Instance management**.
Specify the columns that you want to view in the instance list In the upper-right corner of the Web Application Firewall page, click the icon. In the dialog box that appears, select the columns that you want to display in the instance list. VPC management You can manage VPCs only when you set the **VPC Protection Mode** to **Multiple VPC**
**Protection**. Click **VPC Management** in the **Operation** column of a WAF instance to add
or remove VPCs. Scale out or scale in the instance On the Web Application Firewall page, find the instance that you want to manage and click
**Scale Up** or **Scale Down** in the **Operation** column. In the panel that appears, modify the
Number of Detection Engines parameter and click OK. The Number of Detection Engines parameter specifies the number of detection engines in a single zone. Valid values of this parameter: 2 to 16. Release the instance On the Web Application Firewall page, find the instance that you want to release and click
**Release** in the **Operation** column. In the dialog box that appears, enter **Confirm Release**
and click **OK**.

**Warning**

After the instance is released, it cannot be restored. Before you release the WAF instance, make sure that no services are protected by the WAF instance and that the corresponding instance data has been deleted. Go to the instance details page On the Web Application Firewall page, find the instance that you want to view and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column. On the page that appears, view information about the instance in the Statistics, Detection Logs, Configure Protection, System Settings, and System Info modules. In Apsara Stack versions earlier than v3.18.6 sp-2512, after you add a site, you must manually modify the Elastic Compute Service (ECS) security group of the WAF instance to allow detection node traffic. Otherwise, the back-to-origin request may fail. In Apsara Stack v3.18.6 sp-2512 and later, no manual configuration is required because the security group automatically allows detection node traffic. on

## 4 Statistics information

### 4.1 Protection overview

The Overview page displays information including attack statistics, the geographical distribution of attackers, the total number of requests, and the number of blocked requests. You can also view information about the attacks. Then, you can configure protection rules to protect your web services. This topic describes how to view the Web Application Firewall (WAF) protection overview.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Statistics** > **Overview**.
4. On the **Overview** page, view data on the **Last 24 Hours** and **Last 30 Days** tabs.
Requests: displays the total number of requests. Attacks: displays the total number of attacks. Blocked Requests: displays the total number of blocked requests. Geographical Distribution of Attack Sources: displays the distribution of attackers on the map of China or the map of the world. Initiate AttacksIP appears most frequently: displays the top five IP addresses from which the highest number of attacks are initiated in a bar chart. The x-axis shows the number of requests. The y-axis shows the IP addresses. Type-based Attack Distribution: displays the distribution of the top five attack types and the number of attacks of each type in a bar chart. Most Attacked Sites: displays the top five websites that are most attacked and the number of attacks on each website.

### 4.2 Access status monitoring

Web Application Firewall (WAF) monitors access to web services. Security administrators can analyze the service access information to detect vulnerabilities and improve the security of the web services. This topic describes how to view access information of web services.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Overview > Access Status Monitoring**.
4. On the **Access Status Monitoring** page, view the access information.
You can specify the following filter conditions to view specific access information: on
**IP** or **SESSION**
**All**, **Site**, or **URL**
**Requests Within 30 Seconds** or **Average Response Time**
Only real-time access monitoring information of the top 100 web services that are most frequently accessed is displayed.

### 4.3 Export protection reports

Web Application Firewall (WAF) can automatically export protection reports. You can also manually export protection reports. This topic describes how to export protection reports.

**Export a protection report**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Statistics > Export**.
4. On the Export page, export protection reports.
All protection reports are displayed on the **Protection Reports** tab regardless of whether the protection reports are manually exported or automatically exported. Manually export a protection report On the **Protection Reports** tab, click **Generate Report**. Configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Report Name | The name of the protection report. |
| Report Type | The type of the protection report to export. Valid values:D aily Report and Customize. |
| Statistical Period | The time range within which statistics are collected for the protection report. Select a time range based on the value of the Report Type parameter. |
| Statistical Scope | The scope of sites whose statistics are collected for the protection report. Valid values: All Sites and Specify Statistical Site. |

on

| Root Path | Note This parameter is required only if you set the Statistical Scope parameter to Specify Statistical Site. Enter the root path of the sites. Valid values: http://: The sites use only HTTP. https://: The sites use only HTTPS. http(s)://: The sites use both HTTP and HTTPS. |
|---|---|

Automatically export a protection report On the **Scheduled Reports** tab, click **Add Scheduled Report**. Configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Report Name | The name of the protection report. |
| Report Type | The type of the protection report. Valid values: Daily Report and Weekly Report. |
| Statistical Scope | The scope of sites whose statistics are collected for the protection report. Valid values: All Sites and Specify Statistical Site. |
| Root Path | Note This parameter is required only if you set the Statistical Scope parameter to Specify Statistical Site. Enter the root path of the sites. Valid values: http://: The sites use only HTTP. https://: The sites use only HTTPS. http(s)://: The sites use both HTTP and HTTPS. |

**Manage protection reports**

On the **Protection Reports** tab, you can view and manage protection reports. Filter protection reports Click **Filter**, specify filter conditions, and then click **Ok**. The logical relationship among multiple filter conditions is AND. Only protection reports that match all filter conditions are displayed. View report details on Find the protection report whose details you want to view and click the icon in the
**Actions** column.
Download protection reports Select the protection reports that you want to download and choose **More > Download**
**Selected Reports**.
Delete protection reports Select the protection reports that you want to delete and choose **More > Delete Selected**
**Reports**.

### 4.4 Attack statistics

You can view attack statistics to obtain information about attacks launched against your website and perform operations to handle the source IP addresses of the attacks. This topic describes how to enable and view attack statistics.

**Attack statistics**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Statistics** > **Attack Statistics**.
4. On the **Attack Statistics** page, click **Configure Statistics**.
5. In the **Configure Statistics** panel, click the
icon and click **Ok**. After you complete the preceding configuration, the attack statistics feature is enabled. If your website is attacked, you can view the top 100 source IP addresses that initiate attacks most frequently and the information of the targets on the **Attack Source Tracking** and
**Attack Target Analysis** tabs. You can find the attack whose details you want to view and
click the icon in the **Actions** column. Then, you can perform operations on the attack on the **Attack Detection Logs** page. For more information, see View attack detection logs.

### 4.5 Traffic trends

The Traffic Trend Chart page displays the traffic trends of your website. You can specify the time range within which statistics are generated. This topic describes how to view the traffic trends of a website.

**View the traffic trend chart**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Statistics** > **Traffic Trend Chart**.
4. On the **Traffic Trend Chart** page, click the
icon to the right of **Information Overview**. on
5. In the **Edit** panel, select the website whose traffic trends you want to view from the
**Website** drop-down list, specify **Attack Time**, and then click **Query**.
After you complete the preceding configurations, you can view the trends of your website traffic that is generated within the specified time range.

## 5 Protection logs

### 5.1 Attack detection logs

You can use attack detection logs to analyze attacks on your web services. You can update your protection policies and custom rules and fix web service vulnerabilities based on the analysis results. This helps enhance the security of your web services. This topic describes how to view attack detection logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Detection Logs > Attack Detection Logs**.
On the Attack Detection Logs page, you can view attack detection logs. You can also perform the following operations based on your business requirements: Filter logs Click **Filter**. In the panel that appears, specify filter conditions and click **Ok**. Multiple filter conditions are evaluated by using the logical AND operator. The system returns logs only if all conditions are met. Download logs a. Select one or more logs that you want to download, move the pointer over **More** in the upper-right corner of the page, and then select **Download Selected Logs(.json)** or
**Download Selected Logs(.csv)**. In the Alert message, click **Ok**.
b. In the left-side navigation pane, choose **Detection Logs > Log Download**
**Management**. On the Log Download Management page, find the download task that
you created and click the icon in the **Actions** column. Switch between log display modes Move the pointer over the icon and select **List** or **Detailed View** as the display mode of logs.

### 5.2 HTTP flood protection logs

You can use HTTP flood protection logs to analyze the HTTP flood attacks on your web services. You can update your HTTP flood protection rules and HTTP flood whitelist and fix web service vulnerabilities based on the analysis results. This helps enhance the security of your web services. This topic describes how to view HTTP flood protection logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Detection Logs > HTTP Flood Protection Logs**.
On the HTTP Flood Protection Logs page, you can view HTTP flood protection logs. You can also perform the following operations based on your business requirements: Filter logs Click **Filter**. In the panel that appears, specify filter conditions and click **Ok**. Multiple filter conditions are evaluated by using the logical AND operator. The system returns logs only if all conditions are met. Add an HTTP flood attack to the blacklist Find the HTTP flood attack that you want to add to the blacklist and click the icon in the **Actions** column to create a blacklist rule. In the **Add to Blacklist** panel, enter a name for the blacklist rule and click **OK**.

### 5.3 System operation logs

This topic describes how to view system operation logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Detection Logs > System Operations Logs**.
On the System Operations Logs page, you can view system operation logs. You can also perform the following operations based on your business requirements: Filter logs Click **Filter**. In the panel that appears, specify filter conditions and click **Ok**. Multiple filter conditions are evaluated by using the logical AND operator. The system returns logs only if all conditions are met. Download logs a. Select one or more logs that you want to download, move the pointer over **More**, and then select **Download Selected Logs (.json)** or Download Selected Logs (.csv). In the Alert message, click **Ok**. b. In the left-side navigation pane, choose **Detection Logs > Log Download**
**Management**. On the Log Download Management page, find the download task that
you created and click the icon in the **Actions** column.

### 5.4 Access logs

This topic describes how to view access logs.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Detection Logs > Access Logs**.
On the Access Logs page, you can view access logs. You can also perform the following operations based on your business requirements: Filter logs Click **Filter**. In the panel that appears, specify filter conditions and click **Ok**. Multiple filter conditions are evaluated by using the logical AND operator. The system returns logs only if all conditions are met. Download logs a. Select one or more logs that you want to download, move the pointer over **More**, and then select **Download Selected Logs(.json)** or **Download Selected Logs(.csv)**. In the Alert message, click **Ok**. b. In the left-side navigation pane, choose **Detection Logs > Log Download**
**Management**. On the Log Download Management page, find the download task that
you created and click the icon in the **Actions** column.

### 5.5 Log download management

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Detection Logs > Log Download Management**.
On the Log Download Management page, you can perform the following operations: Download logs Select one or more logs that you want to download and click the icon. Delete logs Select one or more logs that you want to delete and choose **More > Delete Selected**
**Tasks**.

### 5.6 Query logs by IP address

If you want to check whether an IP address hits a rule that you configure in your Web Application Firewall (WAF) instance, you must query data from multiple sources. This topic describes how to automatically identify rules that are hit by an IP address.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Detection Logs > Querying With IP**.
4. On the **Querying With IP** page, select a log type from the **Log Type** drop-down list and
enter the IP address that you want to query in the IP search box.
5. Find the query result that you want to view and click the
icon in the **Actions** column to view the details.

## 6 Protection configurations

### 6.1 Protected website management

**management**

#### 6.1.1 Manage websites

This topic describes how to add an Internet website to Web Application Firewall (WAF).
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Protection Site**
**Management**.
4. On the **Site Management** tab, click **Add Site**.
5. In the **Configure Listening Information** step of the **Add Protected Site** panel,
configure the parameters that are described in the following table and click **Next**. Configure the Internet website that you want WAF to protect. WAF can protect HTTP and HTTPS websites.

| Parameter | Description |
|---|---|
| Protected Site Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You can use an asterisk (*) as a wildcard. If you specify multiple domain names, separate them with commas (,). If you enter IPv6 addresses, you must use brackets ([]) to enclose each IPv6 address. |
| Description | The description of the website. |

| Port Settings | The port on which WAF listens. If the website can be accessed over multiple ports, click Add Group of Ports to add the ports. If the website can be accessed only over HTTP, you can skip the certificate configuration and directly proceed to site management. If the website can be accessed over HTTPS, you need to specifyS SL Configuration Mode after you select Enable SSL. SSL Configuration Mode: Specify the SSL encryption and decryption mode. Use WAF SSL configuration: WAF completes SSL decryption and processes HTTPS traffic. If you select this option, you need to upload an SSL certificate and bind the certificate file to WAF so that WAF can decrypt HTTPS traffic, process the traffic, and then encrypt the traffic. Use ALB SSL configuration: Application Load Balancer (ALB) completes SSL decryption. WAF only processes the decrypted HTTP traffic. If you select this option, you need to first configure the certificate required by the current website. Then, select the ALB certificate to ensure that HTTPS traffic can be decrypted. Note When HTTPS is enabled and performance must be ensured, we recommend that you configure a certificate and enable TLS offloading on the ALB side. This enables WAF to focus on security detection, which balances security and performance. If the website can be accessed over HTTP/2, select Enabled HTTP2. This option is available only when you select Enable SSL. |
|---|---|
| Certificate Config | The certificate type of the website. By default, SSL Certificate is selected. |
| Certificate Settings | The SSL certificate of the website. Valid values: Upload Certificate or Select Existing Certificate. Upload Certificate: If the SSL certificate of the website is not uploaded to WAF, select this option. By default, the SSL certificate and the private key file are separately uploaded. If you select Include Private Key in Certificate File, upload only one file that contains the SSL certificate and the private key. Select Existing Certificate: If the SSL certificate of the website is uploaded to WAF, select this option. Then, select the required SSL certificate from the drop-down list. You can enter a keyword to search for the certificate. |
| Certificate Name | The name of the SSL certificate. |

| SSL Cert File | The SSL certificate and private key file. By default, the SSL certificate and the private key file are separately uploaded. If you select Include Private Key in Certificate File to the right of Certificate Name, upload only one file that contains the SSL certificate and the private key. |
|---|---|
| Certificate Password | The password of the SSL certificate. |
| Mutual Authentication | Specifies whether to enable mutual authentication. If you click the icon to enable mutual authentication, configure the following parameters: CA Certificate Settings: the certificate authority (CA) certificate. Valid values: Upload Certificate or Select Existing Certificate. Upload Certificate: If the CA certificate of the website is not uploaded to WAF, select this option. Configure the CA Certificate Name and CA Certificate File parameters. Select Existing Certificate: If the CA certificate of the website is uploaded to WAF, select this option. Then, select the required CA certificate from the drop-down list. You can enter a keyword to search for the certificate. Detection Depth: the detection depth of mutual authentication. Client Detection: the verification of the client certificate. Valid values: ON, OFF, OPTIONAL, and Optional (no ca). _ If the client certificate is provided, select OPTIONAL. If the client certificate is issued by a non-trusted CA, select Optional (no ca). _ |

6. In the **Configure VPC** step of the **Add Protected Site** panel, configure the parameters
that are described in the following table and click **Next**.

| Parameter | Description |
|---|---|
| Protected VPC | The VPC to which the website that you want WAF to protect belongs. |
| Access Method | The access mode. This parameter specifies the load balancing service to be used to distribute traffic. SLB Access: A Classic Load Balancer (CLB) instance is used to distribute Layer 4 traffic to WAF. This option is suitable for most scenarios. ALB Access: An ALB instance is used to distribute Layer 7 traffic to WAF. IPv6 traffic can be distributed from end to end. If you set SSL Configuration Mode to Use ALB SSL configuration in Configure Listening Information, only ALB Access is supported by default. |

| VPC SLB Virtual IP/VPC ALB Virtual IP | Select an SLB or ALB virtual IP address (VIP) from the drop-down list. |
|---|---|

7. In the **Configure Response Method** step of the **Add Protected Site** panel, configure the
parameters that are described in the following table and click **Next**.

| Response mode | Parameter | Description |
|---|---|---|
| Forward to Backend Servers | Load Balancing Algorithm | The algorithm that is used for load balancing. Valid values: Weighted Round-robin, Source IP Address Hash, and Least Connections. |
|   | Backend Server Address | The backend server to which traffic is forwarded after passing through WAF. To add more forwarding addresses, click Add Forwarding Address. Back-to-origin routing over IPv6 supports only ALB instance IPv6 addresses. It does not support Elastic Compute Service (ECS) instance IPv6 addresses. |
|   | X-Forwarded-For | The pass-through mode of the source IP address. The X-Forwarded-For (XFF) header is used to identify the actual source IP address of an HTTP client. The header is used for traffic forwarding services, such as the HTTP proxy and load balancing. Valid values: Append IP Address of Previous Hop to the X- Forwarded-For Field Overwrite Original Value of the X-Forwarded- For Field with IP Address of Previous Hop Remain Unchanged |
| Redirect | Response Status Code | The HTTP status code that is returned when WAF redirects inbound traffic to a specific address. Valid values: 301, 302, 307, and 308. 301: The requested page is permanently redirected to another URL. 302: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 307: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 308: The requested page is permanently redirected to another URL. |
|   | Redirection Address | The destination URL to which requests are redirected. |

| Specify Response Content | Response Status Code | The HTTP status code that is returned when WAF returns the specified content. Valid values: 200, 400, 401, 402, 404, 405, 500, 503, and 504. |
|---|---|---|
|   | Response | The content that you want to be returned. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

8. In the **Protection Policy** step of the **Add Protected Site** panel, configure the parameters
that are described in the following table and click **Next**. Then, go to the **OK** step.

**Important**

You can configure a protection policy only if you set the **Configure Response Method** parameter to **Forward to Backend Servers**.

| Parameter | Description |
|---|---|
| Protection Policy | The protection policy of WAF. By default, Default Policy Set is selected. Valid values: Not Use Protection Policy Default protection policies Default Policy Set Strict Protection Observation Mode Financial Institution Internet Enterprise Custom protection policies For more information about protection policies, see Protection policies. |
| User Identification | The user identification mode. Note If you enable HTTP flood protection for the protected website and set the Target Type parameter to SESSION when you configure the HTTP flood protection rule, you must set the User Identification parameter to Identify by WAF. |

After you add websites to WAF, you can perform the following operations in the protected website list: View protected websites You can view the information about the protected websites that you added to WAF, such as the status, website name, port, domain name, and downstream node. Specify the items that you want to view in the protected website list Click the icon to the right of **Actions**, select the items that you want to display in the protected website list, and then click Ok. Filter protected websites In the upper-right corner of the page, click **Filter**. In the panel that appears, filter protected websites by Name, Server Names, Policy Group, Anti Tamper Status, Create Time, or Last Update Time. Enable, disable, export, or delete protected websites Select the protected websites that you want to manage and choose **More > Enable**
**Selected Sites**, **Disable Selected Sites**, **Export Selected Sites(.csv)**, or **Delete**
**Selected Sites**.
Modify the basic information about a protected website Find the protected website whose basic information you want to modify and click the icon in the **Actions** column. On the **Basic Information** tab, click the icon to the right of each parameter to modify the corresponding information. The parameters include **Site**
**Name**, **Listening Port**, **Domain Name**, **Description**, and **Virtual IP Address**.
Modify the request processing mode of a protected website Find the protected website whose request processing mode you want to modify and click the icon in the **Actions** column. On the **Request Processing Method** tab, click the icon to the right of each parameter to modify the corresponding information. The parameters include **Configure Response Method**, **Scheduling Algorithm**, **X-**
**Forwarded-For**, **Backend Server Health Check**, **Access Log Record**, **Backend**
**Server Address**, **HTTP Header**, **Back-to-origin IP Address**, and **SSE Configuration**.
View and modify protection settings Find the protected website whose protection settings you want to modify and click the icon in the **Actions** column. On the **Protection Mode** tab, view and modify the protection settings. View the details of the protection policies that you configured, such as Decoding Method, Attack Detection Module, Blocking Method, HTTP Response Processing, HTTP Request Body Detection, and Detection Timeout Period. Click the icon to the right of **Default Policy Set** and modify the protection policy settings. For more information about protection policies, see Protection policies. Custom Rules: You can create custom rules. For more information, see Custom rules. Rule Source: You can select **Use Existing Rule** or **Add Rule**. Method Used to Obtain Source IP Addresses: You can specify the method used to obtain the IP addresses of origin servers. The IP addresses of origin servers can be obtained from sockets, the X-Forwarded-For header, or the HTTP header. User Identification: Click the icon. In the panel that appears, set the User Identification parameter to **Disable**, **Identify by WAF**, or **Obtain User ID from**
**Requests**, and click Ok.

#### 6.1.2 Manage VIPs

You can add a virtual IP address (VIP), a VIP in a virtual private cloud (VPC), or an elastic IP address (EIP) to instance-based Web Application Firewall (WAF). The VIP that you add to WAF can be used as the downstream node of a VPC-connected website that you add to WAF. This topic describes how to add a VIP in a VPC to WAF and how to manage the VIP.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Protection Site**
**Management**.
4. On the **Virtual IP Address Management** tab, add a VIP, a VIP in a VPC, or an EIP to WAF.
Add a VIP in a VPC to WAF. a. On the **VPC SLB Virtual IP** or **VPC ALB Virtual IP** tab, click **Add Virtual IP Address** and configure parameters in the panel that appears. b. In the **Add Virtual IP Address** panel, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Access Method | The load balancing service used to distribute traffic to WAF. SLB Access: A Classic Load Balancer (CLB) instance is used to distribute Layer 4 traffic to WAF. This option is suitable for most scenarios. ALB Access: An Application Load Balancer (ALB) instance is used to distribute Layer 7 traffic to WAF. The ALB instance can distribute IPv6 traffic from end to end. |
| Network Type | The access mode of the VIP. This parameter is available only when ALB Access is selected. Intranet: Traffic is transmitted only within a VPC. This access mode is suitable for internal system communication. Internet: Requests from the Internet are received and transmitted. This access mode is suitable for external services. |

| Virtual IP Address | Specify a traffic destination and how the VIP is created. Add Virtual IP Address: The system automatically generates a VIP and the corresponding SLB instance. Create Specified Virtual IP Address: The system generates a VIP as required and creates the corresponding SLB instance. |
|---|---|
| Availability Zones | Select the zone to which the VIP belongs from the drop-down list. |
| Protected VPC | Select a VPC to receive traffic and protect. |
| Switch | Select the vSwitch to which the VIP belongs. |
| Protocol Version | Select the IP protocol of the VIP to ensure compatibility with application traffic. This parameter is required only when ALB Access is selected. IPv4: supports only IPv4 traffic. Dual Stack: supports both IPv4 and IPv6 traffic. Important Make sure that the WAF instance is of the dual-stack type. Otherwise, IPv6 traffic cannot be inspected. You need to configure and view the IPv6 gateway in the ALB console. |
| Description | Enter the purpose of the VIP or add a description for subsequent O&M management or reference. |
| VPC SLB Virtual IP/VPC ALB Virtual IP | Enter the VIP of the SLB instance to be created. This parameter is available only when Virtual IP Address is set to Create Specified Virtual IP Address. Make sure that the specified IP address is not occupied and is the same as the CIDR block of the destination VPC. |
| Operational Mode | The mode in which the VIP runs. Active-Active: Traffic is distributed from the VIP to multiple WAF detection engines in all data centers. Compared with the active- standby mode, the active-active mode improves the availability of WAF. Active-Standby: Traffic is distributed from the VIP to multiple WAF detection engines in the specified data center. If the VIP and WAF detection engines reside in the same data center, using the active- standby mode can avoid data transmission across data centers and reduce the network latency. |

Add an EIP.

**Important**

After you enable EIPs in **System Settings > Instance System Settings**, you can manage EIPs. a. In the left-side navigation pane, click **EIP management**. On the page that appears, click **Add EIP**. b. In the **Add EIP** panel, configure the EIP and related information and click **OK**.

| Parameter | Description |
|---|---|
| EIP ID | Enter the ID of the EIP and click Query. |
| EIP | After you click Query, the EIP is displayed. |
| Protected VPC | Select a VPC to protect from the drop-down list. Make sure that traffic destined for the EIP is routed to the destination VPC. |
| VPC SLB Virtual IP | Select the VPC SLB VIP that you have created from the drop-down list to associate it with the EIP. After Internet traffic reaches the VIP, the traffic is distributed to the VIP and then load balanced by the SLB instance. |
| Back-to-source SLB instance | Select an SLB instance from the drop-down list as the load balancer for origin routing. The SLB instance is used to distribute legitimate traffic from WAF to backend servers. |

After you complete the configuration, you can perform the following operations: On the **VPC SLB Virtual IP** and **VPC ALB Virtual IP** pages:
**View**: Click the
icon to the left of a VPC to view VIPs. You can also click the icon in the **Actions** column of a VIP to view the details of the VIP. We recommend that the **specifications** of the CLB or ALB instance be higher than the overall performance of the WAF instance. If not, find the CLB or ALB instance in the SLB console and modify the specifications.
**Delete**: Click the
icon to the left of a VPC to view VIPs. You can also click the icon the **Actions** column of a VIP and click **Ok** in the message that appears to delete the VIP. On the **EIP management** page:
**View**: You can view the configurations of an EIP or click the
icon in the **Actions** column to view the details of the EIP. Click the icon next to the **Back-to-source SLB**
**instance** to modify the SLB instance for origin routing.
**Enable bypass**: On the **EIP Details** page, click **Enable bypass** and enter an EIP to
enable the bypass mode.

**Important**

The bypass mode takes effect on the inbound and outbound traffic of all websites that are associated with the EIP. In bypass mode, the EIP is connected to the specified tenant SLB instance and traffic is not inspected by WAF.

### 6.2 Protection policies

Web Application Firewall (WAF) provides default protection policies. You can also configure custom protection policies based on your business requirements. This topic describes how to configure protection policies of WAF.

**Background information**

By default, you can configure five types of protection policies.

| Protection policy | Scenario | Description |
|---|---|---|
| Default policy set | Scenarios that do not have high security requirements | Blocks high-risk attacks but does not detect server responses or bot requests. |
| Strict protection policy | Scenarios that have high security requirements | Blocks all attacks. |
| Policy for Internet enterprises | Internet website services | Blocks high-risk attacks but does not detect Active Server Pages (ASP) code injections or module injections. |
| Policy for financial institutions | Financial website services | Allows and records command injections, blocks high-risk attacks, but does not detect ASP code injections or module injections. |
| Policy in observation mode | Scenarios in which attacks only need to be recorded | Allows and records all requests. |

You can perform the following steps to configure protection policies based on your business requirements:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Protection Policies**.
4. In the upper-right corner of the Protection Policies page, click **Add Protection Policy**. In
the panel that appears, configure the **Name** parameter and click **OK**.
5. Find the new protection policy and click the
icon in the **Actions** column to view the details of the policy. The following table describes the sections on the policy details page.

| Section | Description |
|---|---|
| Decoding Method | The algorithms that you want to use to decode requests. |
| Attack Detection Module | The types of attacks that you want to detect and the risk levels of the attacks that you want to block. |
| Blocking Method | The HTTP status code and image that you want WAF to return when WAF blocks an attack. |
| HTTP Response Processing | The HTTP response detection settings. Configure the HTTP Response Processing and Maximum Body Length parameters. |
| HTTP Request Body Detection | The HTTP request body detection settings. Configure the HTTP Request Body Detection parameter. |
| Detection Timeout Period | The timeout settings. Turn on or off Enable Timeout Detection and configure the Detection Timeout Period parameter. |
| Request Body Size Check | The size of a file that is exempt from detection. |

For example, perform the following steps to configure detection modules in the **Attack**
**Detection Module** section:
i. In the **Attack Detection Module** section, find the module that you want to configure and click the **Edit** icon. In this example, **SQL Injection Detection Module** is used. ii. In the **SQL Injection Detection Module** panel, configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Enabled | Specifies whether to enable the detection module. |
| Blocking Threshold | The attack blocking threshold. Valid values: NotBlock, Only BlockHigh, BlockModerate and High Risks, and BlockAll. |
| Logging Threshold | The logging threshold. Valid values: NotLog, Only LogHigh, LogModerate and High Risks, and LogAll. |
| Detect Non-Injected SQL | Specifies whether to detect non-injection SQL attacks. |

iii. Click **Ok**.
6. **Optional.** Delete protection policies.
Select the protection policies that you want to delete and choose **More** > **Delete Selected**
**Protection Policies**. In the message that appears, click **Ok**.
The default protection policy cannot be deleted.

### 6.3 Global custom rules

Global custom rules take effect on all Web Application Firewall (WAF) instances. This topic describes how to view WAF rules.

**Create a global custom rule**

You can create global custom rules in Cloud Shield Operations Center. Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose **Product Operation >**
**Security O&M > Cloud Shield Operations Center**. In the left-side navigation pane,
choose **Cloud Services > WAF Instance Management > Rules**. Then, you can add global custom rules on the page that appears. For more information, see **Web Application**
**Firewall - Instance O&M Guide > Rule management**.

**View global custom rules**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection** > **Global Custom Rules**.
4. On the Global Custom Rules page, view information about global custom rules.
The list displays the **Status**, **Rule ID**, **Description**, **Expire At**, **Created At**, and **Last**
**Modified At** fields of global custom rules.
View the details of a global custom rule Find the rule that you want to view and click the icon in the **Actions** column to view the details of the global custom rule. View logs Find the rule whose logs you want to view and click the icon in the **Actions** column. The Attack Detection Logs page is displayed. On this page, you can view the logs. Filter global custom rules In the upper-right corner of the Global Custom Rules page, click **Filter**. In the panel that appears, filter global custom rules by rule ID, description, last modification time, creation time, or expiration time. To add a filter condition, click **Add Filter Item**.

### 6.4 Custom rules

You can create custom rules to meet different requirements for intrusion protection and filter out specific requests. This topic describes how to create a custom rule for Web Application Firewall (WAF).

**Create a custom rule**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Custom Rules**.
4. Click **Add Rule**. In the panel that appears, configure the parameters that are described in
the following table and click **OK**.

**Important**

We recommend that you use the Monitor mode for a newly created custom rule and monitor the results of the rule for a period of time. If no false positives are generated, use the Block mode for the rule.

| Parameter | Description |
|---|---|

| Mode |   | The action you want WAF to perform on requests that match the rule. Valid values: Block, Allow, Monitor, and Control by Using Detection Module. Block: blocks requests that match the rule. Allow: allows requests that match the rule. Monitor: records and allows requests that match the rule. Control by Using Detection Module |
|---|---|---|
| Description |   | The description of the rule. We recommend that you specify the purpose of the rule. |
| Risk Level |   | The risk level. Valid values: No Threat, Low, Moderate, and High. Note This parameter is required only if you set the Mode parameter to Block, Allow, or Monitor. |
| Match Condition |   | The match conditions of the rule. Click Add Match Condition to specify more than one condition. The logical relationship among multiple conditions is AND. The rule takes effect only when all conditions are met. Note If you want to match multiple user IP addresses at the same time, select regular expression match or equal to. If you select equal to, separate multiple IP addresses with commas (,). Examples: [User IP] [equal to] [0.0.0.0,127.0.0.1] [User IP] [regular expression match] [0.0.0.0\|127.0.0.1] |
| Action |   | Specify the detection module to be enabled or disabled. The configuration is available only in Control by Using Detection Module mode. |
| Scope of Usage |   | The websites on which the rule takes effect. You cannot enter a website name that contains the wildcard character (*). |
|   | Logging | Specify whether to record logs when the rule is matched. The default value is Log When Match Condition Is Met. After you set the Logging parameter to Log When Match Condition Is Met, all block events are recorded in the intrusion detection log. |

| baba Cloud Security- ion Firewall (WAF) | Web Application Firewall-Instan Web Appli e User Guide·Protection configu ation |   |
|---|---|---|
| Advanced |   |   |
|   | Attack Type | The type of attack that you want to block. |
|   | Blocking Status Code | The status code that you want the website to return when a request is blocked. |
|   | Expire At | The expiration time of the rule. |
|   | Punishme nt Mechanis m | The Punishment Mechanism parameter is available only in Block mode. No Punishment: Requests that match the rule are blocked. No other actions are performed. IP Block: The source IP addresses of the requests that match the rule are added to the blacklist. Access from these IP addresses is denied within the punishment duration. Session Block: Session identifiers, such as session IDs in cookies, are extracted from the requests that match the rule to block user sessions. All requests from the blocked sessions are denied within the punishment duration. After you complete the configuration, the system automatically creates an HTTP flood protection rule to block IP addresses or sessions. You cannot modify or delete the HTTP flood protection rule. You can only enable or disable the rule. |
|   | Punishme nt Duration | In Block mode, you can specify the Punishment Duration parameter, which takes effect only when IP Block or Session Block is selected. This parameter takes effect only on IP addresses and sessions that are newly added to the blacklist. Existing entries in the blacklist are not affected by punishment duration changes. For example, a session will be blocked for 1 hour. Even if you change the punishment duration to 5 minutes, the session will still be blocked for 1 hour based on the original setting. |

**Important**

After you configure the parameters, click **OK**. If the system determines that the rule may be used to `deny all requests` and the Mode parameter is not set to Monitor, the system displays a message to prompt you to set the **Mode** parameter to **Monitor** and create a custom rule again.
5. Optional. You can also create custom rules offline and click **Import Rules** to import the
rules at a time. The logical relationship among multiple custom rules is **OR**. If two custom rules use the same match conditions but trigger different actions on requests that meet the match conditions, WAF performs the action that is specified in the rule whose **ID number** is smaller.

**Manage custom rules**

You can view and manage custom rules in the custom rule list. View custom rules In the custom rule list, view the custom rules that you created. Query logs Find the rule whose logs you want to view and click the icon in the **Actions** column. Modify a custom rule Find the rule that you want to modify and click the icon in the **Actions** column. In the panel that appears, modify the configurations of the rule. Filter custom rules In the upper-right corner of the Custom Rules page, click **Filter**. In the panel that appears, filter custom rules by ID, Comment, Last Update Time, Create Time, or Expire Time. What to do next Select the rules that you want to enable, disable, export, or delete, move the pointer over
**More** in the upper-right corner of the page, and then select **Enable Selected Rules**,
**Disable Selected Rules**, **Export Selected Rules**, or **Delete Selected Rules**.

### 6.5 Tamper-proofing rules

You can configure tamper-proofing rules to protect web page data from being tampered with. This topic describes how to configure a tamper-proofing rule.

**Create a tamper-proofing rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Settings > Instance System Settings**.
On the Instance System Settings page, set the **Anti Tamper** parameter to **On** to enable the tamper-proofing feature. By default, the tamper-proofing feature is disabled. After you set the **Anti Tamper** parameter to **On**, the Anti Tamper Rule module is displayed in the left-side navigation pane of the console.
4. In the left-side navigation pane, choose **Configure Protection > Anti Tamper Rule**.
5. On the Anti Tamper Rule page, click **Add Rule**. In the **Add Anti Tamper Rule** panel,
configure the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Status | The status of the tamper-proofing rule. Valid values: Enable and Disable. |

| Description | The description of the rule. We recommend that you enter the protection purpose of the rule. |
|---|---|
| Protocol | The protocol type. Valid values: http and https. |
| Domain Name | The domain name for which the rule takes effect. If the server is bound to a domain name, you must enter the domain name. |
| Match Condition | The match condition of the rule. Valid values: File Path and Regular Expression. The page path starts with a forward slash (/) and ends with html, shtml, txt, js, css, jpg, or png. The value can be up to 128 characters in length. |
| Scope of Usage | The websites for which the rule takes effect. |

**Manage tamper-proofing rules**

You can view and manage tamper-proofing rules in the tamper-proofing rule list. View tamper-proofing rules In the tamper-proofing rule list, view the information about tamper-proofing rules. Modify a tamper-proofing rule Find the rule that you want to modify and click the icon in the **Actions** column. Filter tamper-proofing rules In the upper-right corner of the Anti Tamper Rule page, click **Filter**. In the panel that appears, filter tamper-proofing rules by ID, Comment, Last Update Time, or Create Time. Enable, disable, or delete tamper-proofing rules Select the tamper-proofing rules that you want to manage, move the pointer over **More**, and then select **Enable Selected Rules**, **Disable Selected Rules**, or **Delete Selected**
**Rules** to enable, disable, or delete the rules.

### 6.6 HTTP flood protection

#### 6.6.1 HTTP flood protection rules

An HTTP flood attack is a type of DDoS attack that targets the application layer. Attackers use proxy servers or zombies to overwhelm targeted web servers by sending a large number of HTTP requests. You can configure HTTP flood protection rules to prevent HTTP flood attacks. This topic describes how to configure an HTTP flood protection rule.

**Create an HTTP flood protection rule**

1. Log in to the Apsara Uni-manager Management Console
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > HTTP Flood**
**Protection**.
4. On the HTTP Flood Protection page, click **Add Rule**. In the **Add HTTP Flood Protection**
**Rules** panel, configure the parameters that are described in the following table and click
**OK**.

| Parameter | Description |
|---|---|
| Rule Mode | The action you want WAF to perform on requests that trigger the HTTP flood protection rule. Valid values: Blocking Mode: limits requests that match the rule. Monitoring Mode: records but does not limit requests that match the rule. |
| Rule Type | The type of the HTTP flood protection rule. Valid values: Restrict Users Based on Policy and Restrict Known Users. Restrict Users Based on Policy: limits requests that meet all match conditions in the HTTP flood protection rule. You can specify the following match conditions: Trigger Condition, Statistical Objects, Action, Throttling Period, and Statistical Scope. The Statistical Scope parameter is in the Advanced section. Restrict Known Users: limits requests that are initiated from specific IP addresses or in specific sessions based on the HTTP flood protection rule. To limit known users, you must configure an IP address or session list and a limit mode. After you configure the list, the HTTP flood protection rule limits requests based on the list. |
| Rule Name | The name of the HTTP flood protection rule. |
| Target Type | The type of source from which requests are limited. Valid values: IP and SESSION. Note If you set the Target Type parameter to SESSION, you can apply the HTTP flood protection rule only to a site for which the User Identification parameter is set to Identify by WAF. For more information, see Site management. |
| Trigger Condition | The trigger condition of the HTTP flood protection rule. This parameter is required if you set the Rule Type parameter to Restrict Users Based on Policy. |

| Statistical Objects | The URL addresses that are protected based on the HTTP flood protection rule. This parameter is required if you set the Rule Type parameter to Restrict Users Based on Policy. Valid values: IP Addresses with Specified Prefix Specified IP Address All IP Addresses |
|---|---|
| Restricted IP List or Restricted SESSION List | The list of limited IP addresses or sessions. If you set the Rule Type parameter to Restrict Known Users, you must enter the IP addresses or sessions from which you want to limit requests based on the value of the Target Type parameter. You can enter only one IP address or session in each line. |
| Action | The mode in which the HTTP flood protection rule limits requests. Valid values: Block: The rule blocks specific sources from accessing the specified URLs. Throttle: The rule limits the frequency at which specific sources access the specified URLs. |
| Restricted URL Address | The URLs that are protected based on the HTTP flood protection rule. This parameter is required if you set the Rule Type parameter to Restrict Known Users. Valid values: IP Addresses with Specified Prefix Specified IP Address All IP Addresses |
| Throttling Period | The period during which the specified action takes effect. |
| Statistical Scope | The range of requests to limit. This parameter is available in the Advanced section and is required if you set the Rule Type parameter to Restrict Users Based on Policy. All Access Data: If you select this option, all requests that are forwarded to WAF and match the access frequency condition are limited. This compromises system performance. Top N Access Data: If you select this option, only top 100 requests that match the access frequency condition are limited. You can select this option to minimize the impact on system performance when there are more than 100 requests need to be limited. |

#### 6.6.2 HTTP flood whitelist

If a request source is trusted, you can add this request source to the HTTP flood whitelist to allow all requests from this source. This topic describes how to configure the HTTP flood whitelist.

**Add a request source to the HTTP flood whitelist**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > HTTP Flood**
**Protection**.
4. On the **Whitelist** tab, click **Add User to Whitelist**. In the panel that appears, configure
the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Type | The type of the request source. Valid values:I P and SESSION. |
| IP or SESSION | The IP addresses or sessions to be added to the whitelist based on the value of the Type parameter. You can enter multiple IP addresses or sessions at a time. Make sure you enter one IP address or session in each line. |
| Description | The description of the whitelist. |

**Manage the HTTP flood whitelist**

Search for a request source in the whitelist In the upper-right corner of the page, click **Filter**. In the Filter Item panel, specify a filter condition to search for a specific request source. You can click **Add Filter Item** to specify multiple filter conditions. Remove a request source from the whitelist On the Whitelist tab, select the request source that you want to delete and choose **More** >
**Delete Selected Items**.

### 6.7 Threat intelligence

The threat intelligence module can receive threat intelligence feeds from the Internet. This helps enterprises observe suspicious requests from the Internet and develop protection policies to defend against attacks. This topic describes how to view the threat intelligence of assets.

**View threat intelligence**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Threat Intelligence**.
4. On the **Threat Intelligence** page, if **Threat Intelligence** is disabled, you can enable it in
**System SettingsInstance System Settings**.
5. You can view threat intelligence within different time periods based on **Intelligence**
**Synchronization Status**.

### 6.8 Certificate management

After you upload a certificate on the Certificates page, you can select the certificate when you add a website to Web Application Firewall (WAF) on the Protection Site Management page. This topic describes how to upload a certificate. When you add an HTTPS website for protection on the **Protection Site Management** page, you must select the certificate to which the domain name of the HTTPS website is bound.

**Upload a certificate**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Certificates**.
4. On the **Certificates** page, upload a certificate.
i. On the **SSL Certificate** tab, click Upload SSL Certificate. On the **CA Certificates** tab, click Upload Certificate. ii. In the **Add File** panel, configure the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Certificate Name | The name of the certificate. Important If the certificate is an SSL certificate and the certificate and the private key are in the same file, select Include Private Key in Certificate File. |
| File | The certificate and private key file. SSL certificate a. Drag the certificate and its private key file to the fields. If you select Include Private Key in Certificate File when you configure the Certificate Name parameter, you do not need to upload the private key file. b. Configure the Certificate Password parameter. Important This parameter is required only if you do not select Include Private Key in Certificate File. Certificate authority (CA) certificate Drag the certificate to the field. |
| Certificate Password | The password of the SSL certificate. |

### 6.9 Data masking

Web Application Firewall (WAF) allows you to configure data masking policies to mask sensitive data before the sensitive data is displayed. The sensitive data includes ID card numbers, dates of birth, bank card numbers, and passwords.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **Configure Protection > Data Privacy**.
4. In the **Log Data Privacy** section of the Data Privacy page, click the
icon to the right of
**Disable**. In the panel that appears, turn on **Log Privacy**.
5. Configure the **Built-in** and **Customized** parameters based on your business requirements.

## 7 System settings

### 7.1 Online backup

This topic describes how to create an online backup.

**Create an online backup**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Settings > Online Backup**.
4. On the Online Backup page, click **Create Backup**. In the **Add Backups** panel, configure
the Description parameter and click OK. You can back up information such as protected websites and related protection policies, online backup rules, and certificates.

**Manage online backups**

You can view and manage online backups in the online backup list. Select the online backups that you want to manage, move the pointer over **More**, and then select **Download Selected Backups** or **Delete Selected Backups** to download or delete the backups.

### 7.2 Instance system settings

Instance-based Web Application Firewall (WAF) allows you to configure global system settings to enable or disable the global protection engine, specify an internal-facing Server Load Balancer (SLB) instance as the downstream service, and configure shared virtual IP addresses. This topic describes how to configure global system settings.
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall - Instance-Based**. On the **Web Application Firewall** page, select
a region from the **Region** drop-down list and click **Access with Authorized Role**. Find the instance that you want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Settings > Instance System Settings**.
4. On the **Instance System Settings** page, configure the parameters that are described in
the following table.

| Parameter | Description | Operation |
|---|---|---|

| Global WAF Protection Engine | Specifies whether to enable global protection engine. The engine determines the status of intrusion prevention configurations at the platform management side and the service group management side. If you disable the engine, WAF allows all traffic and does not perform intrusion detection or traffic processing. | Click the icon to the right of this parameter. In the panel that appears, turn on or off the switch and click Ok. |
|---|---|---|
| Threat Intelligence | Specify whether to enable threat intelligence. | Click the icon to the right of this parameter. In the panel that appears, turn on or off the switch and click Ok. |
| Expiration Reminder for SSL Certificate | The expiration reminder for SSL certificates. | Click the icon to the right of this parameter. In the panel that appears, change the time and click Ok. |
| Maximum Number Of Journal Downloads | The maximum number of logs that can be downloaded. | Click the icon to the right of this parameter. In the panel that appears, specify the maximum number of logs that can be downloaded. Then, click Ok. |
| Anti Tamper | Specifies whether web pages can be locked. When a locked page receives a request, a cached version of the page is returned. This helps prevent web page tampering. | Click the icon to the right of this parameter. In the panel that appears, turn on or off the switch and click Ok. |
| EIP | Specify whether elastic IP addresses (EIPs) can be added to WAF. | Click the icon to the right of this parameter. In the panel that appears, turn on or off the switch and click Ok. |
| Status code for domainless configuration | The status code returned when no domain name is matched. | Click the icon to the right of this parameter. In the panel that appears, specify the status code to return when no domain name is matched. |

| Upper limit of listening ports | The maximum number of listener ports. | Click the icon to the right of this parameter. In the panel that appears, specify the maximum number of listening ports. |
|---|---|---|

## 8 System information

### 8.1 Node status

#### 8.1.1 Loads

This topic describes how to view the loads on Web Application Firewall (WAF) nodes. The loads include CPU utilization and memory usage. You can identify faults based on the loads and check whether a scale-out is required.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Usage** tab, view the loads on WAF nodes.
In the Usage section, you can view the CPU utilization and memory usage of WAF nodes. In the CPU Utilization and Memory Usage sections, you can view the changes in CPU utilization and memory usage over a specific period of time.

#### 8.1.2 Network information

This topic describes how to view the network information about Web Application Firewall (WAF) nodes. The information includes the network I/O, traffic detection statistics, and traffic forwarding statistics.

**Node network information**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Node Status** page, click the **Network Status** tab.
5. View the network I/O of WAF nodes.

#### 8.1.3 Detection status

This topic describes how to view the number of requests detected by Web Application Firewall (WAF) nodes per second and the average detection time of the WAF nodes.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Detection Status** tab, view the detection status of WAF nodes.
In the Detection Status section, you can view the number of requests detected by WAF nodes per second and the average detection time of the WAF nodes. In the Requests Detected per Second section and the Average Detection Time section, you can view the changes over a specific period of time.

#### 8.1.4 Forwarding status

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Forwarding Status** tab, view the forwarding status of Web Application Firewall
(WAF) nodes. In the Forwarding Status section, you can view the number of new connections per second, the number of concurrent connections, and the average processing latency of WAF nodes. In the New Connections per Second, Concurrent Connections, and Average Latency of Request Processing sections, you can view the changes over a specific period of time.

#### 8.1.5 Disk status

This topic describes how to view the disk information about Web Application Firewall (WAF) nodes. You can identify faults based on the disk information and check whether a scale-out is required.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. Click the **Disk Status** tab to view the disk information about WAF nodes.
In the Disk Status section, you can view the disk I/O and disk usage of WAF nodes. In the
**Disk Read I/O** and **Disk Write I/O** sections, you can view the changes in disk reads and
writes over a specific period of time.

#### 8.1.6 Historical data query

This topic describes how to query the historical data of Web Application Firewall (WAF) nodes.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. Click the **Historical Data Query** tab to view historical data of the target WAF node.
Click the icon to the right of **Information Overview**. In the **Edit** panel, configure the
**Node** and **Attack Time** parameters and click **Query**.
5. In the **Historical System Performance Data** section, view the CPU utilization, memory
usage, and disk usage of the node. In the **Historical Traffic Monitoring Data** section, view the following node information: the network read I/O, network write I/O, number of new connections per second, and number of requests detected per second.

### 8.2 System firmware information

This topic describes how to query the system firmware information of Web Application Firewall (WAF).
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > Application Security > Web Application**
**Firewall - Instance**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**. Find the instance that you
want to manage and click its name in the **WAF Instance Name** column or **Console Entry** in the Access Entry column.
3. In the left-side navigation pane, choose **System Info > System Firmware Information**.
4. On the **System Firmware Information** page, view the information in the Current
Firmware Version section, including **Instance Name** and **Attack Detection Engine**.
