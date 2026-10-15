---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) User Guide 20260902"
product_version: "V3.18.6_2607"
doc_version: "20260902"
pdf_pages: 60
source_pdf: "ff89d5f97889223a_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) User G"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20User%20Guide%2020260902.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Web Application Firewall (WAF) User Guide 20260902

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
  - 2.3 Quick start
- 3 Detection overview
  - 3.1 View protection overview
  - 3.2 View access information
  - 3.3 Export protection report
  - 3.4 View attack detection statistics
  - 3.5 View traffic trends
- 4 Protection logs
  - 4.1 View attack detection logs
  - 4.2 View HTTP flood protection logs
  - 4.3 View system operation logs
  - 4.4 View access logs
  - 4.5 IP query
  - 4.6 Log download management
- 5 Protection configuration
  - 5.1 Protection site management
    - 5.1.1 Internet websites
    - 5.1.2 VPC websites
    - 5.1.3 Manage virtual IP addresses
  - 5.2 Configure protection policies
  - 5.3 Global custom rules
  - 5.4 Create a custom rule
  - 5.5 Anti-tampering rules
  - 5.6 HTTP flood protection
    - 5.6.1 Configure an HTTP flood protection rule
    - 5.6.2 Configure the HTTP flood whitelist
  - 5.7 Threat intelligence
  - 5.8 Upload a certificate
  - 5.9 Data masking
  - 5.10 Use your computer to verify the access configurations
  - 5.11 Modify DNS settings
- 6 System management
  - 6.1 Configure alert settings
    - 6.1.1 Configure alerts
    - 6.1.2 Configure alert thresholds
  - 6.2 Online backup
  - 6.3 Other system settings
  - 6.4 Global system settings
- 7 System information
  - 7.1 Node status
    - 7.1.1 View the loads on nodes
    - 7.1.2 View the network information of nodes
    - 7.1.3 View the node detection status
    - 7.1.4 View the node forwarding status
    - 7.1.5 View the disk information of nodes
    - 7.1.6 Historical node data query
  - 7.2 Back-to-origin IP addresses
  - 7.3 System firmware information

## 1 Usage notes

Before you log on to Apsara Stack Security Center, you must verify that your computer meets the configuration requirements. For more information about the configuration requirements, see . Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 2 Quick start

### 2.1 User roles and permissions

Web Application Firewall (WAF) provides tenant-side user roles and platform-side user roles. Tenant-side user roles have the permissions to use independent WAF. Platform-side user roles have the permissions to use WAF that protects the Apsara Stack platform. This topic describes the user roles. All roles are default user roles. You cannot create custom roles. Before you log on to tenantside WAF or platform-side WAF, make sure that your account is assigned the required roles. Table 1. Tenant-side user roles

| Role name | Description |
|---|---|
| System administrator of Apsara Stack Security Center | Manages and configures system settings for Apsara Stack Security Center. The system administrator has permissions to manage Apsara Stack accounts, synchronize data, configure alerts, and configure global settings. |
| Security administrator of Apsara Stack Security Center | Monitors the security status across Apsara Stack and configures security policies for each functional module of Apsara Stack Security. The security administrator has permissions on all features that are related to Threat Detection, Network Security, Application Security, Server Security, Physical Server Security, and Asset Management. Note The permissions to use WAF must be separately granted. |
| Department security administrator | Monitors the security status of cloud resources in a specific department and configures security policies for each functional module of Apsara Stack Security for the department. The department security administrator has permissions on all features that are related to Threat Detection, Network Security, Application Security, Server Security, Physical Server Security, and Asset Management. The department security administrator can specify alert notification methods and alert contacts in the department. Note The permissions to use WAF must be separately granted. |
| Auditor of Apsara Stack Security Center | Conducts security audits across Apsara Stack. The auditor can view audit events and raw logs, configure audit policies, and access all features that are related to Security Audit. |

Table 2. Platform-side user roles

| Role name | Description |
|---|---|

| Platform security configuration administrator | Configures platform-side WAF. |
|---|---|

If you do not have an account that is assigned the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create a**
**user** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

You need to obtain the endpoint of the Apsara Uni-manager Management Console from the deployment personnel. A browser is available. We recommend using Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter. You can click the current language in the upper-right corner to switch to another language. The Authorized Login button is displayed only when a global IdP is configured in third-party authentication. You can customize the name of the Authorized Login button based on your requirements.
2. Enter your username and password.
Obtain the username and password for the Apsara Uni-manager Management Console from the operations administrator. The first time you log on to the Apsara Uni-manager Management Console, you must change your account password as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Account Logon**.
4. If your account has multi-factor authentication (MFA) enabled, perform the corresponding
operations in the following scenarios:

**First logon after the administrator enforces MFA**

a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Re-enter your account and password as described in Step 2, and click **Account Login**. c. Enter the 6-digit MFA code and click **Authenticate**.

**You have enabled and bound MFA**

Enter the 6-digit MFA code and click **Authenticate**. For more information about how to bind and enable MFA, see Manage multi-factor authentication.

**Related operations**

**Forgot password**

1. If you forget your logon password, click **Forget Password** below the password input box.
2. On the Forgot Password page, enter your **Account Name**, **Email Address**, and verification
code, and then click **Confirm**. You can use the username of your account and the email address that was used to create the account. A password reset link will be sent to your email. You can enter a new password after accessing the link.

### 2.3 Quick start

This topic helps you get started with the features of Web Application Firewall (WAF). WAF uses intelligent semantic analysis algorithms to identify web attacks. WAF also uses a learning model to enhance its analysis capabilities and meet your daily security protection requirements without relying on traditional rule libraries. The following content describes the procedure for using WAF:
1. Customize WAF protection rules.
WAF provides default protection policies. You can also customize policies that suit your business requirements. For more information about how to configure protection policies, see Configure protection policies. For more information about how to configure custom rules, see Create a custom rule. For more information about how to configure HTTP flood protection rules, see Configure an HTTP flood protection rule.
2. Add websites that you want to protect.
WAF can protect Internet websites and virtual private cloud (VPC) websites. For more information about how to add an Internet website to WAF for protection, see Add an Internet website for protection. For more information about how to add a VPC website to WAF for protection, see Add a VPC website for protection.
3. Configure Domain Name System (DNS) resolution.
For more information about how to change the DNS-resolved source IP address for a website to a virtual IP address assigned by WAF, see Modify DNS resolution settings.
4. View WAF protection results.
For more information about how to view the protection overview, see View protection overview. For more information about how to view the service access information, see View Web service access information. For more information about how to view the detection logs for web attacks, see View attack detection logs. For more information about how to view the detection logs for HTTP flood attacks, see View HTTP flood protection logs.

## 3 Detection overview

### 3.1 View protection overview

The Detection Overview page displays information including attack statistics, the geographical distribution of attackers, the total number of requests, and the number of blocked requests. You can also view information about the attacks. Then, you can configure protection rules to protect your web services. This topic describes how to view the Web Application Firewall (WAF) protection overview.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the
**Application Security** section, click **Web Application Firewall**. On the **Web Application**
**Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Statistic** > **Detection Overview**.
4. On the **Detection Overview** page, view data on the **Statistics within Last 24 Hours**
and **Statistics within Last 30 Days** tabs. Total Requests: displays the total number of requests. Attack Times: displays the total number of attacks. Blocked Requests: displays the total number of blocked requests. Attacker Geographical Distribution: displays the distribution of attackers on the map of China or the map of the world. Initiate Attack IP appears most frequently: displays the top 5 IP addresses from which the highest number of attacks are initiated in a bar chart. The x-axis shows the number of requests. The y-axis shows the IP addresses. Distribution of Attack Types: displays the distribution of the top 5 attack types and the number of attacks of each type in a bar chart. Most Attacked Websites: displays the top 5 websites that are most attacked and the number of attacks on each website.

### 3.2 View access information

Web Application Firewall (WAF) monitors access to web services. Security administrators can analyze the service access information to detect vulnerabilities and improve the security of the web services. This topic describes how to view access information about web services.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Statistic > Access Status Monitor**.
4. On the **Access Status Monitor** page, view access information.
You can specify the following filter conditions to view specific access information:
**IP** or **SESSION**
**All**, **Site**, or **URL**
**Requests within 30 Seconds** or **Average Response Time**
Only real-time access monitoring information about the top 100 web services that are most accessed is displayed.

### 3.3 Export protection report

Web Application Firewall (WAF) supports manual and automatic export of protection reports. This topic describes how to export protection reports.

**Export protection report**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose**Statistics > Export**.
4. On the **Export** page, export protection reports.
All protection reports are displayed on the **Protection Reports** tab regardless of whether the protection reports are manually exported or automatically exported. Manually export a protection report On the **Protection Reports** tab, click **Generate Report**. Configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Report Name | The name of the protection report. |
| Report Type | The type of the protection report to export. Valid values:D aily Report and Customize. |
| Statistical Period | The time range within which statistics are collected for the protection report. Select a time range based on the value of the Report Type parameter. |
| Statistical Scope | The scope of websites whose statistics are collected for the protection report. Valid values: All Sites and Specify Statistical Site. |

| Root Path | Note This parameter is required only if you set the Statistical Scope parameter to Specify Statistical Site. Enter the root path of the websites. Valid values: http://: The websites use only HTTP. https://: The websites use only HTTPS. http(s)://: The websites use both HTTP and HTTPS. |
|---|---|

Automatically export a protection report On the **Scheduled Reports** tab, click **Add Scheduled Report**. Configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Report Name | The name of the protection report. |
| Report Type | The type of the protection report. Valid values: Daily Report and Weekly Report. |
| Statistical Scope | The scope of websites whose statistics are collected for the protection report. Valid values: All Sites and Specify Statistical Site. |
| Root Path | Note This parameter is required only if you set the Statistical Scope parameter to Specify Statistical Site. Enter the root path of the websites. Valid values: http://: The websites use only HTTP. https://: The websites use only HTTPS. http(s)://: The websites use both HTTP and HTTPS. |

**Manage protection reports**

On the **Protection Reports** tab, you can view and manage the protection reports. Filter protection reports Click **Filter**, specify filter conditions, and then click **OK**. If you specify multiple filter conditions, WAF uses the AND operator to combine the filter conditions. The system returns reports that match the conditions. View report details Find the protection report whose details you want to view and click the icon in the
**Actions** column.
Download protection reports Select the protection reports that you want to download and choose **More > Download**
**Selected Reports**.
Delete protection reports Select the protection reports that you want to delete and choose **More > Delete Selected**
**Reports**.

### 3.4 View attack detection statistics

**statistics**

Attack detection statistics allow you to obtain information about attacks on your website and perform operations on the source IP addresses of the attacks. This topic describes how to enable and view attack detection statistics.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Statistic** > **Attack Detection Statistics**.
4. On the **Attack Detection Statistics** page, click **Statistical Configuration**.
5. In the **Statistical Configuration** panel, click the
icon and click **OK**. After you complete the preceding configurations, the attack detection statistics feature is enabled. If your website is attacked, you can view the top 100 source IP addresses from which the highest number of attacks are initiated and information about the targets of attacks on the **Attack Detection Traceability** and **Attack Target Analysis** tabs. You can also find the attack whose details you want to view and click the icon in the **Actions** column. Then, you can perform operations on the attack on the **Attack Detection Logs** page. For more information, see View attack detection logs.

### 3.5 View traffic trends

The Traffic Trend Graph page displays the traffic trends of your website. You can specify the time range from which the statistics are generated. This topic describes how to view the traffic trends of a website.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Statistic** > **Traffic Trend Graph**.
4. On the **Traffic Trend Graph** page, click the
icon to the right of **Query Information**.
5. In the **Edit query information** panel, select the website whose traffic trends you want to
view from the **Website** drop-down list, specify the **time range**, and then click **Query**. After you complete the preceding configurations, you can view the trends of your website traffic that is generated within the specified time range.

## 4 Protection logs

### 4.1 View attack detection logs

Attack detection logs allow you to analyze the attacks on your web services. You can update your protection policies and custom rules and fix web service vulnerabilities based on the analysis results to improve the security of your web services. This topic describes how to view attack detection logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > Attack Detection Logs**.
On the Attack Detection Logs page, you can view attack detection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**. If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions. Export logs a. Select the logs that you want to export and select **Download selected log(.json)** or
**Download selected log(.csv)** from the **More** drop-down list. In the Alert message,
click **OK**. b. In the left-side navigation pane, choose **Detection Logs > Downloading Log**
**Management**. Find the download task that you created and click the
icon in the
**Actions** column to download the logs.
Switch between display modes In the upper-right corner of the Attack Detection Logs page, click the icon and select
**List** or **Detailed View** to specify the display mode for the logs.

### 4.2 View HTTP flood protection logs

**logs**

HTTP flood protection logs allow you to analyze the HTTP flood attacks on your web services. You can update your HTTP flood protection rules and HTTP flood attack whitelist and fix web service vulnerabilities based on the analysis results to improve the security of your web services. This topic describes how to view HTTP flood protection logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > HTTP Flood Detection Logs**.
On the HTTP Flood Detection Logs page, you can view HTTP flood protection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**. If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions. Add an HTTP flood attack to the blacklist Find the HTTP flood attack that you want to add to the blacklist and click the icon in the
**Actions** column to create a blacklist rule. In the **Add to Blacklist** panel, enter a name
for the blacklist rule and click **OK**.

### 4.3 View system operation logs

This topic describes how to view system operation logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > System Operation Log**.
On the Attack Detection Logs page, you can view attack detection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**. If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions. Export logs a. Select the logs that you want to export and select **Download selected log(.json)** or
**Download selected log(.csv)** from the **More** drop-down list. In the Alert message,
click **OK**. b. In the left-side navigation pane, choose **Detection Logs > Downloading Log**
**Management**. Find the download task that you created and click the
icon in the
**Actions** column to download the logs.
Switch between display modes In the upper-right corner of the Attack Detection Logs page, click the icon and select
**List** or **Detailed View** to specify the display mode for the logs.

### 4.4 View access logs

This topic describes how to view access logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > Access Log**.
On the Attack Detection Logs page, you can view attack detection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**. If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions. Export logs a. Select the logs that you want to export and select **Download selected log(.json)** or
**Download selected log(.csv)** from the **More** drop-down list. In the Alert message,
click **OK**. b. In the left-side navigation pane, choose **Detection Logs > Downloading Log**
**Management**. Find the download task that you created and click the
icon in the
**Actions** column to download the logs.
Switch between display modes In the upper-right corner of the Attack Detection Logs page, click the icon and select
**List** or **Detailed View** to specify the display mode for the logs.

### 4.5 IP query

The ip query feature lets you quickly search for a specific IP address. It automatically analyzes the rule type triggered by the IP, such as a cc attack or an attack detection log, and provides attack details. This helps you troubleshoot issues efficiently without time-consuming manual searches across multiple sources.
1. Log on to the Apsara Uni-manager console.
2. In the upper-right corner of the console, click **Security**, and choose **Application Security**
**> > Web Application Firewall**. On the **Web Application Firewall** authorization page,
select a **region** and click **Role-based Authorization**.
3. In the left-side navigation pane, choose **Protection Log > > IP Query**.
4. On the **IP Query** page, select a **Log Type** and enter the desired IP address in the search
box.
5. Click the
icon in the **Actions** column for the target IP address to view details.

### 4.6 Log download management

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a **region** and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > Log Download Management**.
You can perform the following operations in the log download management list: Download logs Select one or more complete logs and click the icon. Delete logs Select one or more complete logs and choose **More > Delete Selected Tasks**.

## 5 Protection configuration

### 5.1 Protection site management

#### 5.1.1 Internet websites

Tenant-side Web Application Firewall (WAF) can protect Internet websites and virtual private cloud (VPC) websites. This topic describes how to add an Internet website to WAF.

**Background information**

For information about how to add an Internet website to WAF, refer to this topic. For information about how to add a VPC website to WAF, see Add a VPC website to WAF for protection.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a **region** and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Configure Protection > Protection Site**
**Management**.
4. On the **Internet Sites** tab, click **Add Site**.
5. In the **Configure Listening Information** step of the **Add Protected Site** panel,
configure the parameters that are described in the following table and click **Next**. Configure the Internet website that you want WAF to protect. WAF can protect HTTP and HTTPS websites.

| Parameter | Description |
|---|---|
| Protected Site Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You can use asterisks (*) as wildcards. If you specify multiple domain names, separate them with commas (,). |
| Description | The description of the website. |

| Port Settings | The port on which WAF listens. If the website can be accessed over multiple ports, click Add Group of Ports to add the ports. If the website can be accessed only over HTTP, you can skip the configuration of the certificate and configure the Virtual IP Address parameter. If the website can be accessed over HTTPS, select Enable SSL and configure the parameters. If the website can be accessed over HTTP/2, select Enable HTTP2. Note This option is available only when you select Enable SSL. |
|---|---|
| Certificate Config | The certificate type of the website. By default, SSL Certificate is selected. |
| Certificate Settings | The SSL certificate of the website. Valid values: Upload Certificate or Select Existing Certificate. Upload Certificate: If the SSL certificate of the website is not uploaded to WAF, select this option. By default, the SSL certificate and the private key file are separately uploaded. If you select Include Private Key in Certificate File, upload only one file that contains the SSL certificate and the private key. Select Existing Certificate: If the SSL certificate of the website is uploaded to WAF, select this option. Then, select the required SSL certificate from the drop-down list. You can enter a keyword to search for the certificate. |
| Certificate Name | The name of the SSL certificate. |
| SSL Cert File | The SSL certificate and private key file. By default, the SSL certificate and the private key file are separately uploaded. If you select Include Private Key in Certificate File to the right of Certificate Name, upload only one file that contains the SSL certificate and the private key. |
| Certificate Password | The password of the SSL certificate. |

| Mutual Authenticatio n | Click the icon to enable mutual authentication and configure the parameters. CA Certificate Settings: the certificate authority (CA) certificate. You can select Upload Certificate or Select Existing Certificate. Upload a New Certificate: If the CA certificate of the website is not uploaded to WAF, select this option. Configure the CA Certificate Name and CA Certificate File parameters. Select Existing Certificate: If the CA certificate of the website is uploaded to WAF, select this option. Then, select the required CA certificate from the drop-down list. You can enter a keyword to search for the certificate. Detection Depth: the detection depth of mutual authentication. Client Detection: the verification of the client certificate. Valid values: ON, OFF, OPTIONAL, and Optional (no ca). _ If the client certificate is provided, select OPTIONAL. If the client certificate is issued by a non-trusted CA, select Optional (no ca). _ |
|---|---|
| Virtual IP Address | Select whether the downstream virtual IP address is an existing virtual IP address or a new one to be created. Valid values: Select Existing Virtual IP Address Add Virtual IP Address Create Specified Virtual IP Address |
| Virtual IP Address | The virtual IP address. Important By default, you can select up to eight virtual IP addresses. Configure this parameter only if you select Select Existing Virtual IP Address from the Virtual IP Address drop-down list. |
| Type of Virtual IP Address | The type of the virtual IP address. Valid values: Public IP Address of Classic Network Internal IP Address of Classic Network Important This parameter is required only if you select Add Virtual IP Address or Create Specified Virtual IP Address from the Virtual IP Address drop- down list. |

| Protocol of Virtual IP Address | The version of the virtual IP address. Valid values: ipv4 ipv6 Important This parameter is required only if you select Add Virtual IP Address or Create Specified Virtual IP Address from the Virtual IP Address drop- down list. |
|---|---|
| Specify Data Center | Specifies whether the specified virtual IP address is used by the specified data center. Valid values: Yes No Important This parameter is required only if you select Create Specified Virtual IP Address from the Virtual IP Address drop-down list. |
| Custom IP Address | The custom virtual IP address. Important This parameter is required only if you select Create Specified Virtual IP Address from the Virtual IP Address drop-down list and select No from the Specify Data Center drop-down list. |
| Data Center Name | The name of the data center that uses the virtual IP address. Important This parameter is required only if you select Create Specified Virtual IP Address from the Virtual IP Address drop-down list and select Yes from the Specify Data Center drop-down list. |
| Operational Mode | The running mode. Valid values: Active-Active Active-Standby Important This parameter is required only if you select Create Specified Virtual IP Address from the Virtual IP Address drop-down list and select Yes from the Specify Data Center drop-down list. |

6. In the **Configure Response Method** step of the **Add Protected Site** panel, configure the
parameters that are described in the following table and click **Next**.

| Configure Response Method | Parameter | Description |
|---|---|---|
| Forward to Backend Servers | Load Balancing Algorithm | The algorithm that is used for load balancing. Valid values: Weighted Round-robin, Source IP Address Hash, and Least Connections. |
|   | Backend Server Address | The address of the origin server to which WAF forwards traffic. Valid values: Back-to-origin Address and Redirect to Specific Instance. Back-to-origin Address: Enter the address of the origin server. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorithm. Redirect to Specific Instance: Enter the address of a specific Elastic Compute Service (ECS) or Server Load Balancer (SLB) instance. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorithm. |
|   | X-Forwarded- For | The pass-through mode of the source IP address. The X-Forwarded-For (XFF) header is used to identify the actual source IP address of an HTTP client. The header is used for traffic forwarding services, such as the HTTP proxy and load balancing. Valid values: Append IP Address of Previous Hop to the X- Forwarded-For Field Overwrite Original Value of the X-Forwarded-For field with IP Address of Previous Hop Remain Unchanged |
| Redirect | Response Status Code | The HTTP status code that is returned when WAF redirects inbound traffic to a specific address. Valid values: 301, 302, 307, and 308. 301: The requested page is permanently redirected to another URL. 302: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 307: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 308: The requested page is permanently redirected to another URL. |
|   | Redirection Address | The destination URL to which requests are redirected. |

| Specify Response Content | Response Status Code | The HTTP status code that WAF returns when WAF returns the specified content. Valid values: 200, 400, 401, 402, 404, 405, 500, 503, and 504. |
|---|---|---|
|   | Response | The content that you want to be returned. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

7. In the **Protection Policy** step of the **Add Protected Site** panel, configure the parameters
that are described in the following table and click **Next**. Then, go to the **OK** step.

**Important**

You can configure a protection policy only if you set the **Configure Response Method** parameter to **Forward to Backend Servers**.

| Paramet er | Description |
|---|---|
| Protectio n Policy | Select a WAF protection policy. By default, Default Policy Set is selected. Valid values: Not Use Protection Policy Default protection policies Default Policy Set Strict Protection Internet Enterprise Financial Institution Observation Mode Custom protection policies For more information about protection policies, see Protection policies. |
| User Identific ation | The user identification mode. Valid values: Disable Identify by WAF Obtain User ID from Requests Note If you enable HTTP flood protection for the protected website and set theT arget Type parameter to SESSION when you configure the HTTP flood protection rule, you must set the User Identification parameter to Identify by WAF. |

After you add Internet websites to WAF, you can perform the following operations in the protected website list: View protected websites You can view the information about the protected websites that you added to WAF, such as the status, website name, port, domain name, and downstream node. Specify the items that you want to view in the protected website list Click the icon to the right of **Actions**, select the items that you want to display in the protected website list, and then click Ok. Filter protected websites In the upper-right corner of the page, click **Filter**. In the panel that appears, filter protected websites by Name, Server Names, Policy Group, Anti Tamper Status, Create Time, or Last Update Time. More operations Select the protected websites that you want to manage and choose **More > Enable**
**Selected Sites**, **Disable Selected Sites**, **Export Selected Sites(.csv)**, or **Delete**
**Selected Sites**.
Modify the basic information about a protected website Find the protected website whose basic information you want to modify and click the icon in the **Actions** column. On the **Basic Information** tab, click the icon to the right of each parameter to modify the corresponding information. You can modify the following parameters: Site Name, Listening Port, Domain Name, Description, and Virtual IP Address. Modify the request processing mode of a protected website Find the protected website whose request processing mode you want to modify and click the icon in the **Actions** column. On the **Request Processing Method** tab, click the icon to the right of each parameter to modify the corresponding information. You can modify the following information about the website on the Request Processing Method tab: Configure Response Method, Scheduling Algorithm, X-Forwarded-For, Backend Server Health Check, Access Log Record, Backend Server Address, HTTP Header, Back-toorigin IP Address, and SSE Configuration. View and modify protection settings Protection Policy: View the details of the protection policies that you configured, such as Decoding Method, Attack Detection Module, Blocking Method, HTTP Response Processing, HTTP Request Body Detection, and Detection Timeout Period. Click the icon to the right of **Default Policy Set** and modify the protection policy settings. For more information about protection policies, see Protection policies. Custom Rules: You can create custom rules. For more information, see Custom rules. Anti Tamper Rule: You can add website tamper-proofing rules. For more information, see Configure a website tamper-proofing rule. Method Used to Obtain Source IP Addresses: You can specify the method used to obtain the IP addresses of origin servers. The IP addresses of origin servers can be obtained from sockets, the X-Forwarded-For header, and the HTTP header. User Identification: Click the icon. In the panel that appears, modify the User Identification parameter and click Ok. Valid values of the User Identification parameter: **Disable**, **Identify by WAF**, and **Obtain User ID from Requests**.

#### 5.1.2 VPC websites

Web Application Firewall (WAF) can protect Internet websites and virtual private cloud (VPC) websites. This topic describes how to add a VPC website to WAF for protection.

**Overview**

For information about how to add an Internet website to WAF, see Add an Internet website to WAF for protection. For information about how to add a VPC website to WAF, see this topic.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a **region** and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **Configure Protection > Protection Site**
**Management**.
4. On the **Protection Site Management** page, click the **VPC Websites** tab.
5. On the **VPC Websites** tab, click **Add Site**.
6. In the **Configure Listening Information** step of the **Add Protected Site** panel,
configure the parameters that are described in the following table and click **Next**. WAF can protect HTTP and HTTPS websites.

| Paramet er | Description |
|---|---|
| Protecte d Site Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You can use an asterisk (*) as a wildcard character. If you specify multiple domain names, separate them with commas (,). |
| Descript ion | The description of the website. |

| Port Settings | The port on which WAF listens. If the website can be accessed over multiple ports, click Add Group of Ports to add the ports. If the website can be accessed only over HTTP, clickN ext. For more information, see Step 7 of this topic. If the website can be accessed over HTTPS, select Enable SSL and configure the parameters. If the website can be accessed over HTTP/2, select Enable HTTP2. Note This option is available only when you select Enable SSL. |
|---|---|
| Certifica te Config | The certificate type of the website. SSL Certificate is selected by default. |
| Certifica te Settings | The SSL certificate of the website. You can select Upload Certificate or Select Existing Certificate. Upload Certificate: If the SSL certificate of the website has not been uploaded to WAF, select this option. By default, the SSL certificate and the private key file are separately uploaded. If you select Include Private Key in Certificate File, upload only one file that contains the SSL certificate and the private key. Select Existing Certificate: If the SSL certificate of the website is uploaded to WAF, select this option. Then, select the required SSL certificate from the drop-down list. You can enter a keyword to search for the certificate. |
| Certifica te Name | The name of the SSL certificate. |
| SSL Cert File | The SSL certificate and the private key. By default, the SSL certificate and the private key are separately uploaded. If you select Include Private Key in Certificate File to the right of Certificate Name, upload only one file that contains the SSL certificate and the private key. |
| Certifica te Passwor d | The password of the SSL certificate. |

| Mutual Authenti cation | Specifies whether to enable mutual authentication. If you click the icon to enable mutual authentication, configure the following parameters: CA Certificate Settings: the certificate authority (CA) certificate. Valid values: Upload Certificate or Select Existing Certificate. Upload Certificate: If the CA certificate of the website is not uploaded to WAF, select this option. Configure the CA Certificate Name and CA Certificate File parameters. Select Existing Certificate: If the CA certificate of the website is uploaded to WAF, select this option. Then, select the required CA certificate from the drop- down list. You can enter a keyword to search for the certificate. Detection Depth: the detection depth of mutual authentication. Client Detection: the verification of the client certificate. Valid values: ON, OFF, OPTIONAL, and Optional (no ca). _ If the client certificate is provided, select OPTIONAL. If the client certificate is issued by a non-trusted CA, select Optional (no ca). _ |
|---|---|

7. In the **Configure VPC** step, configure the parameters and click **Next**. The following table
describes the parameters.

| Paramet er | Description |
|---|---|
| Protecte d VPC | The VPC to which the website that you want WAF to protect belongs. |
| Virtual IP Address | Valid values: Select Existing Virtual IP Address SLB Add Virtual IP Address Create Specified Virtual IP Address EIP Important You can select SLB only if you choose System Settings > Global System Settings in the left-side navigation pane and enable Use Internal-facing SLB Instance as Downstream. The SLB option is available only if you enable Use Internal-facing SLB Instance as Downstream. |
| Switch | The vSwitch that is associated with the website. Important This parameter is required only if you select Add Virtual IP Address or Create Specified Virtual IP Address from the Virtual IP Address drop-down list. |

| SLB | The Server Load Balancer (SLB) instance that is associated with the website. Important This parameter is required only if you select SLB from the Virtual IP Address drop- down list. |
|---|---|
| Virtual IP Address of VPC | If you set the Virtual IP Address parameter to Select Existing Virtual IP Address, select an existing virtual IP address (VIP) from the Virtual IP Address of VPC drop-down list. Important By default, up to eight VIPs can be selected. If you set the Virtual IP Address parameter to Add Virtual IP Address, click Generate Virtual IP Address next to Virtual IP Address of VPC to generate a VIP. If you set the Virtual IP Address parameter to Create Specified Virtual IP Address, enter a VIP in the Virtual IP Address of VPC field. |
| Specify Data Center | Select whether to specify a data center for the website. Important This parameter is required only if you select Create Specified Virtual IP Address from the Virtual IP Address drop-down list. |
| EIP | The EIP that is associated with the website. Important This parameter is required only if you select EIP from the Virtual IP Address drop- down list. |

8. In the Configure Response Method step, configure the parameters, and click **Next**. The
following table describes the parameters.

| Configure Response Method | Parameter | Description |
|---|---|---|
|   | Load Balancing Algorithm | The algorithm that is used for load balancing. Valid values: Weighted Round-robin, Source IP Address Hash, and Least Connections. |
|   | Backend Server Address | The backend server to which traffic is forwarded after passing through WAF. |

| baba Cloud Securit ion Firewall (WAF) |   |   |
|---|---|---|
| Forward to Backend Servers |   |   |
|   | X- Forwarded- For | The pass-through mode of the source IP address. The X-Forwarded-For (XFF) header is used to identify the actual source IP address of an HTTP client. The header is used for traffic forwarding services, such as the HTTP proxy and load balancing. Valid values: Append IP Address of Previous Hop to the X- Forwarded-For Field Overwrite Original Value of the X-Forwarded-For Field with IP Address of Previous Hop Remain Unchanged |
| Redirect | Response Status Code | The HTTP status code that WAF returns when WAF redirects inbound traffic to a specified address. Valid values: 301, 302, 307, and 308. 301: The requested page is permanently moved to another URL. 302: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 307: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 308: The requested page is permanently redirected to another URL. |
|   | Redirection Address | The destination URL to which requests are redirected. |
| Specify Response Content | Response Status Code | The HTTP status code that is returned when WAF returns the specified content. Valid values: 200, 400, 401, 402, 404, 405, 500, 503, and 504. |
|   | Response | The content that you want to be returned. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

9. In the Protection Policy step, configure the parameters and click Next. Then, go to the **OK**
step. The following table describes the parameters.

| Paramet er | Description |
|---|---|

| Protectio n Policy | The protection policy of WAF. By default, Default Policy Set is selected. Valid values: Not Use Protection Policy Default protection policies Default Policy Set Strict Protection Internet Enterprise Financial Institution Observation Mode Custom protection policies For more information about protection policies, see Protection policies. |
|---|---|
| User Identifica tion | The user identification mode. Valid values: Disable Identify by WAF Obtain User ID from Requests Note If you enable HTTP flood protection for the protected website and set theT arget Type parameter to SESSION when you configure the HTTP flood protection rule, you must set the User Identification parameter to Identify by WAF. |

After you add websites to WAF, you can perform the following operations in the protected website list: View protected websites You can view the information about the protected websites that you added to WAF, such as the status, VPC, website name, port, domain name, and virtual IP address. Specify the items that you want to view in the protected website list Click the icon to the right of **Actions**, select the items that you want to display in the protected website list, and then click Ok. Filter protected websites In the upper-right corner of the page, click **Filter**. In the panel that appears, filter protected websites by Name, Server Names, Policy Group, Anti Tamper Status, Create Time, or Last Update Time. More operations Select the protected websites that you want to manage and choose **More > Enable**
**Selected Sites**, **Disable Selected Sites**, **Export Selected Sites(.csv)**, or **Delete**
**Selected Sites**.
Modify the basic information about protected websites Find the protected website whose basic information you want to modify and click the icon in the **Actions** column. On the **Basic Information** tab, click the icon to the right of each parameter to modify the corresponding information. You can modify the following information about the website on the Basic Information tab: website name, website status, listening port, domain name, website description, and virtual IP address. Modify the request processing mode of protected websites Find the protected website whose request processing mode you want to modify and click the icon in the **Actions** column. On the **Request Processing Method** tab, click the icon to the right of each parameter to modify the corresponding information. You can modify the following information about the website on the Request Processing Method tab: Configure Response Method, Scheduling Algorithm, X-Forwarded-For, Backend Server Health Check, Access Log Record, Backend Server Address, HTTP Header, Back-toorigin IP Address, and SSE Configuration. View and modify protection methods Protection Policies: View the details of the protection policies that you configured, such as Decoding Method, Attack Detection Module, Blocking Method, HTTP Response Processing, HTTP Request Body Detection, and Detection Timeout Period. Click the icon to the right of **Default Policy Set** and modify the protection policy settings. For more information about protection policies, see Protection policies. Custom Rules: You can create custom rules. For more information, see Custom rules. Anti Tamper Rule: You can add website tamper-proofing rules. For more information, see Configure a website tamper-proofing rule. Method Used to Obtain Source IP Addresses: You can specify the method used to obtain the IP addresses of origin servers. The IP addresses of origin servers can be obtained from sockets, the X-Forwarded-For header, or the HTTP header. User Identification: Click the icon. In the panel that appears, modify the User Identification parameter and click Ok. Valid values of the User Identification parameter: **Disable**, **Identify by WAF**, and **Obtain User ID from Requests**.

#### 5.1.3 Manage virtual IP addresses

You can add a virtual IP address, a virtual IP address in a virtual private cloud (VPC), or an elastic IP address (EIP) to Web Application Firewall (WAF). The object that you add to WAF can be used as the downstream node of a VPC website that you add to WAF. This topic describes how to add a virtual IP address, a virtual IP address in a VPC, or an EIP to WAF and how to manage the objects.
2. In the upper-right corner of the console, click **Security**. In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Configure Protection > Protection Site**
**Management**.
4. On the **Virtual IP Addresses Management** tab, add a virtual IP address, VPC virtual IP
address, or EIP. Add a virtual IP address to WAF. a. In the left-side navigation tree, click **Virtual IP Address**. On the page that appears, click **Add Virtual IP Address**. b. In the **Add Virtual IP Address** panel, configure the parameters and click **OK**. If you set the **Virtual IP Address** parameter to **Add Virtual IP Address**, configure the **Type of Virtual IP Address** , **Description**, and **Protocol of Virtual IP**
**Address** parameters.
If you set the **Virtual IP Address** parameter to **Create Specified Virtual IP**
**Address**, configure the **Type of Virtual IP Address** , **Description**, **Specify Data**
**Center**, and **Custom IP Address** parameters.
Add a virtual IP address in a VPC to WAF. a. In the left-side navigation tree, click **Virtual IP Address of VPC**. On the page that appears, click **Add Virtual IP Address**. b. In the **Add Virtual IP Address** panel, configure the parameters and click **OK**. If you set the **Virtual IP Address** parameter to **Add Virtual IP Address**, configure the **Protected VPC**, **Switch**, and **Description** parameters. If you set the **Virtual IP Address** parameter to **Create Specified Virtual IP**
**Address**, configure the **Protected VPC**, **Switch**, **Description**, and **Virtual IP**
**Address of VPC** parameters.
In the left-side navigation tree, click **EIP Management**. On the page that appears, click
**Add EIP**. In the **Add EIP** panel, configure the **EIP ID**, **EIP**, **Protected VPC**, **VPC Virtual**
**IP**, and **Back to Source SLB instance** parameters and click **OK**.
After you add a virtual IP address, a virtual IP address in a VPC, or an EIP to WAF, you can perform the following operations: On the **Virtual IP Address**, **Virtual IP Address of VPC**, or **EIP Management** tab, view the added objects. You can also click the icon in the **Actions** column to view the object details. On the **EIP Details** page, modify the value of the **Back to Source SLB Instance** parameter to change the back-to-origin SLB instance. In the upper-right corner of the EIP Details page, click **Enable bypass** and enter an EIP to enable the bypass feature.

### 5.2 Configure protection policies

This topic describes how to configure Web Application Firewall (WAF) protection policies.

**Background information**

WAF provides a default protection policy. You can also customize protection policies to suit your business requirements.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the
**Application Security** section, click **Web Application Firewall**.
3. In the left-side navigation pane, choose **Protection Configuration > Website**
**Protection Policies**.
4. Click **Add a protection policy**. In the panel that appears, configure **Policy name** and
click **Confirm**.
5. In the **Actions** column of the new protection policy, click the
icon to view details.

| Parameter | Description |
|---|---|
| Decode | Select algorithms that you want to use to decode the requests. |
| Attack Detection Modules | Specify the types of attacks that you want to detect and the risk levels of attacks that you want to block. |
| Block Options | Specify the HTTP status code and image that you want WAF to return when it blocks an attack. |
| HTTP Response Detection | Configure Enable HTTP response processing and Response Detection Max Body Size. |
| HTTP Request Detection | Configure Response Detection Max Body Size. |
| Detection Timeout | Configure Enable Detection Timeout and Timeout Threshold. |

For example, perform the following steps to configure modules in the **Attack Detection**
**Modules** section:
i. Move the pointer over a specific module in the **Attack Detection Modules** section. In this example, move the pointer over **SQL Injection Detection Module** and click the
**modify** icon.
ii. In the **SQL Injection Detection Module** panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Enabled | Specify whether to enable the detection module. |
| Blocking Threshold | Valid values: NotForbid, Only ForbidHigh Risk, ForbidMedium or High Risk, and Forbid All. |
| Record Threshold | Valid values: Notrecord, Only recordHigh Risk, recordMedium or High Risk, and record All. |
| Detect Non-Injected SQL | Specify whether to enable detection for NoSQL injection vulnerabilities. |

iii. Click **OK**.
6. Manage protection policies.
To delete a protection policy, select the protection policy. Then, in the upper-right corner, choose **More > Delete Selected Protection Policies**. In the message that appears, click
**OK**.
You cannot delete the default protection policy.

### 5.3 Global custom rules

**Create a global custom rule**

You need to create global custom rules in the system configurations. For more information, see **Rules** > **Create and manage WAF rules** in Apsara Stack Security configurations.

**View a global custom rule**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the console, click **Security**. Then, choose **Application**
**Security > Web Application Firewall**. On the **Web Application Firewall** page, select a
**region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Configure Protection** > **Global Custom Rules**.
4. On the Global Custom Rules page, view information about global custom rules.
The list displays the **Status**, **Rule ID**, **Description**, **Expire At**, **Created At**, and **Last**
**Modified At** parameters of global custom rules.
View the details of a global custom rule Find the rule that you want to view and click the icon in the **Actions** column to view the details of the global custom rule. View logs Find the rule whose logs you want to view and click the icon in the **Actions** column. The Attack Detection Logs page is displayed. On this page, you can view the logs. Filter global custom rules In the upper-right corner of the Global Custom Rules page, click **Filter**. In the panel that appears, filter global custom rules by rule ID, description, last modification time, creation time, or expiration time. To add a filter condition, click **Add Filter Item**.

### 5.4 Create a custom rule

You can create custom rules to meet different requirements for intrusion protection and filter out specific requests. This topic describes how to create a custom rule for Web Application Firewall (WAF).

**Create a custom rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration > Customized Rules**
4. Click **Add Rule** or **Add Intelligence Rule** based on the type of rule that you want to
create. In the panel that appears, configure the parameters and click **Confirm**. The following table describes the parameters. Create Rule

| Parameter | Description |
|---|---|
| Type | The action that you want WAF to perform on requests that match the rule. Valid values: Block, Allow, Monitor, and Detection module control. Block: blocks requests that match the rule. Allow: allows requests that match the rule. Monitor: records and allows requests that match the rule. Detection module control |
| Comment | The description of the rule. We recommend that you enter the protection purpose of the rule. |

| Risk Level | The risk level. Valid values: No Threat, Low Risk, Medium Risk, and High Risk. Note This parameter is required only if you set the Type parameter to Block, Allow, or Monitor. |
|---|---|
| Matching Pattern | The match conditions of the rule. You can click Add Pattern to specify multiple match conditions. A request matches the rule only if the request meets all match conditions. |
| Action | You can select Enabled or Disabled from the drop-down list to enable or disable the rule. |
| Apply to Websites | The websites for which you want the rule to take effect. You cannot enter a website name that contains the asterisk (*) wildcard character. |
| Log Recording Option | Specifies whether to record a log when the rule is triggered. The default value is Enable Log Recording. After you set the Log Recording Option parameter to Enable Log Recording, all interception events are recorded in the intrusion detection logs. |
| Attack Type | The type of attack that you want to defend against. |
| Block Status Code | The status code that you want the website to return when a request is blocked. |
| Expiration Time | The expiration time of the rule. |

Add Intelligence Rule

| Parameter | Description |
|---|---|
| Type | The action that you want WAF to perform on requests that match the rule. Valid values: Monitor and Block. Monitor: records and allows requests that match the rule. Block: blocks requests that match the rule. |
| Comment | The description of the rule. We recommend that you enter the protection purpose of the rule. |
| Risk Level | The risk level. Valid values: No threat, Low Risk, Medium Risk, and High Risk. |

| Matching Pattern | The match conditions of the rule. Click Add Pattern to specify multiple conditions. A request matches the rule only if the request meets all match conditions. |
|---|---|
| Apply to Websites | The websites for which you want the rule to take effect. |
| Log Recording Option | Specifies whether to record a log when the rule is triggered. The default value is Enable Log Recording. After you set the Log Recording Option parameter to Enable Log Recording, all interception events are recorded in the intrusion detection logs. |
| Attack Type | The type of attack that you want to defend against. |
| Block Status Code | The status code that you want the website to return when a request is blocked. |
| Expiration Time | The expiration time of the rule. |

5. (Optional) You can also create custom rules offline and click **Import Rules** to import the
rules at the same time. The logical relation between multiple custom rules is **OR**. If two custom rules use the same match conditions but trigger different actions on requests that meet the match conditions, WAF performs the action that is specified in the rule whose ID number is smaller on the requests.

**Manage custom rules**

You can view and manage custom rules in the custom rule list. View custom rules In the custom rule list, view the custom rules that you created. View logs Find the rule whose logs you want to view and click the icon in the Actions column. Modify custom rules Find the rule that you want to modify and click the icon in the **Actions** column. In the panel that appears, modify the configurations of the rule. Filter custom rules In the upper-right corner of the Customized Rules page, click **Filter**. In the Filter Item panel, specify filter conditions to filter custom rules by ID, comment, most recent modification time, creation time, or expiration time. Enable, disable, export, or delete custom rules Select the rules that you want to manage and select **Enable Selected Rules**, **Disable**
**Selected Rules**, **Export Selected Rules**, or **Delete Selected Rules** from the **More**
drop-down list to enable, disable, export, or delete the rules.

### 5.5 Anti-tampering rules

You can configure anti-tampering rules to protect content on your origin server from malicious tampering.

**Prerequisites**

The anti-tampering rule feature is disabled by default. Ensure that you have set the **Anti-**
**tampering** switch to **On** in **Aegis Operation Center > Cloud Product Management >**
**Physical Machine WAF O&M > Global System Settings**. The anti-tampering rule feature
appears in the left navigation bar only after it is enabled. For detailed instructions, see the **Physical Machine WAF Aegis O&M > Global System**
**Settings** chapter in the Web Application Firewall **Operation Guide (for Tenants) -**
**Physical Machine**.

**Add an anti-tampering rule**

1. Log on to the Apsara Uni-manager Operation Console.
2. In the upper-right corner of the console, click **Security** and then choose **Application**
**Security > Web Application Firewall**. On the **Web Application Firewall** authorization
page, select a **region** and click **role-based access**.
3. In the left-side navigation pane, choose **Protection Settings > anti-tampering rules**.
4. Click **Add Rule**. In the **Add Anti-tampering Rule** panel, configure the parameters and
click **OK**.

| Paramet er | Description |
|---|---|
| Status | The status of the rule. Valid values: Enable and Disable. |
| Descript ion | A description for the rule. |
| Protocol | The protocol to which the rule applies. Valid values:h ttp and https. |
| Domain name | The domain name to which the rule applies. This field is required if your backend server restricts access by domain name. |
| Match conditio n | The match condition type can be File Path or Regular Expression. The file path must start with a forward slash (/), end with a file extension (for example, .html or .jpg), and be no longer than 128 characters. |
| Scope | The site on which the rule takes effect. |

**Manage anti-tampering rules**

You can view and manage your anti-tampering rules in the rule list. View a rule The list of anti-tampering rules displays details for each rule, including the protected path, creation time, and last modified time. Edit a rule To modify a rule, click the icon in the **Actions** column. Filter rules Click **Filter** in the upper-right corner of the page to filter rules by ID, description, last modified time, or creation time. More operations Select multiple anti-tampering rules, click **More Operations**, and then select **Enable**
**Selected Rules**, **Disable Selected Rules**, or **Delete Selected Rules**.

### 5.6 HTTP flood protection

#### 5.6.1 Configure an HTTP flood protection rule

An HTTP flood attack is a type of DDoS attack that targets the application layer. Attackers use proxy servers or zombies to overwhelm targeted web servers by sending a large number of HTTP requests. You can configure HTTP flood protection rules to prevent HTTP flood attacks. This topic describes how to configure an HTTP flood protection rule.

**Create an HTTP flood protection rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration** > **HTTP Flood**
**Detection**.
4. Click **Add Rule**. In the **Add HTTP Flood Detection Rules** panel, configure the parameters
and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Rule Mode | The action that you want WAF to perform on requests that trigger the HTTP flood protection rule. Blocking Mode: limits the requests. Observe: records but does not limit the requests. |

| Rule Types | The type of the HTTP flood protection rule. Valid values: Restrict Users by Policy and Restrict Known Users. Restrict Users by Policy: limits requests that meet all match conditions in the HTTP flood protection rule. You can configure the following match conditions: Restriction Trigger Threshold, Restricted URL Address, Restriction Mode, Restriction Time, and Statistical Range of Visits. The Statistical Range of Visits parameter is in the Advanced section. Restrict Known Users: limits requests that are initiated from specific IP addresses or in specific sessions based on the HTTP flood protection rule. To restrict known users, you must configure the IP address or session list and the limit mode. After you configure the list, the HTTP flood protection rule limits requests based on the list. |
|---|---|
| Rule Name | The name of the HTTP flood protection rule. |
| Target Type | The type of source for limited requests. Valid values:I P and SESSION. Note If you set Target Type to SESSION, you can apply the HTTP protection rule only to a website whose User Identification is set to WAF User System. For more information, see Add an Internet website to WAF for protection. |
| Restriction Trigger Threshold | If you set Rule Types to Restrict Users by Policy, you must configure the triggering conditions for the HTTP flood protection rule. |
| Restricted URL Address | If you set Rule Types to Restrict Users by Policy, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Prefix URL Record all IP addresses |
| Restricted IP List or Restricted SESSION List | If you set Rule Types to Restrict Known Users, you must enter the IP addresses or sessions from which you want to limit requests based on the value of Target Type. You can enter only one IP address or session in each line. |

| Restricted URL Address | If you set Rule Types to Restrict Known Users, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Prefix URL Restrict user access to all addresses |
|---|---|
| Restriction Mode | The mode in which the HTTP flood protection rule limits requests. Valid values: Forbidden: The rule blocks specific sources from accessing the specified URL address. Frequency control: The rule limits the frequency at which specific sources access the specified URL address. |
| Restriction Time | The time at which the action that is specified in the HTTP flood protection rule takes effect. |
| Statistical Range of Visits | If you set Rule Type to Restrict Users by Policy, you can specify the range of data records to limit requests in the Advanced section. Statistics Full Access Data: If you select this option, the frequency of requests is limited when the requests are forwarded to WAF and meet the HTTP flood protection rule, regardless of which data records are accessed by requests. This decreases system performance. Statistics TOP Access Data: If you select this option, the frequency of requests is limited when the requests meet the preceding conditions and access the top 100 data records. This option helps reduce the decrease in system performance. You can select this option when the number of accessed data records is greater than 100. Take note that the top 100 data records are measured based on real-time monitoring. |

**Manage HTTP flood protection rules**

You can view and manage HTTP flood protection rules in the HTTP flood protection rule list. View HTTP flood protection rules In the HTTP flood protection rule list, you can view the protection policies, binding situations, creation time, and most recent modification time. Modify HTTP flood protection rules Find the HTTP flood protection rule that you want to modify and click the icon in the
**Actions** column.
Filter HTTP flood protection rules In the upper-right corner of the page, click **Filter** to filter HTTP flood protection rules by ID, name, target type, or creation time. Enable, disable, or delete HTTP flood protection rules Select the HTTP flood protection rules that you want to manage and select **Enable**
**Selected Rules**, **Disable Selected Rules**, or **Delete Selected Rules** from the **More**
drop-down list.

#### 5.6.2 Configure the HTTP flood whitelist

If a request source is trusted, you can add this request source to the HTTP flood whitelist to allow all requests from this source. This topic describes how to configure the HTTP flood whitelist.

**Add a request source to the HTTP flood whitelist**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration** > **HTTP Flood**
**Detection**.
4. On the **HTTP Flood Detection Whitelist** tab, click **Add Whitelist Item**. In the Add An
unrestricted user panel, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Type | The type of request source. Valid values: IP and SESSION. |
| IP or SESSION | Specify the IP addresses or sessions based on the value of the Type parameter. You can enter only one IP address or session in each line. |
| Comment | The description of the whitelist. |

**Manage the HTTP flood whitelist**

Search for a request source in the whitelist In the upper-right corner of the page, click **Filter**. In the Filter Item panel, specify a filter condition to search for specific request sources. You can click **Add Filter Item** to specify multiple filter conditions. Remove a request source Select the request source that you want to delete and choose **More** > **Delete Selected**
**Items**.

### 5.7 Threat intelligence

**View threat intelligence**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the console, click **Security**. Then, choose **Application**
**Security > Web Application Firewall**. On the **Web Application Firewall** page, select a
**region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Configure Protection > Threat Intelligence**.
4. On the **Threat Intelligence** page, you can view threat intelligence details within different
time periods based on **Intelligence Synchronization Status**.

### 5.8 Upload a certificate

After you upload a certificate on the Certificate Management page, you can select the certificate when you add a website to Web Application Firewall (WAF) on the Protection Site Management page. This topic describes how to upload a certificate. When you add an HTTPS website for protection on the **Protection Site Management** page, you must select the certificate to which the domain name of the HTTPS website is bound.

**Upload a certificate**

2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration** > **Certificate**
**Management**.
4. On the **Certificate Management** page, upload a certificate.
i. Click the **SSL Certificate** tab. In the upper-right corner of the page, click Upload Certificate. ii. In the **Add File** panel, configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | Enter the certificate name. Important If the certificate and the private key are in the same file, select Include private key in certificate file. |
| File | Upload the certificate and private key. SSL Certificate a. Drag the certificate and its private key file to the fields. If you select Include private key in certificate file when you configure the Name parameter, you do not need to upload the private key file. b. Configure the SSL Certificate Password parameter. Important This parameter is required only if you do not select Include private key in certificate file. CA Certificate Drag the certificate to the field. |

**Manage certificates**

You can manage certificates on the **SSL Certificate** tab. View a certificate In the certificate list, you can view the certificate name, usage, domain name, or validity period. View information about a certificate Find the certificate whose information you want to view and click the icon in the **Actions** column. On the **Certificate Details** page, you can view the certificate name, upload time, issuer, serial number, validity period, domain name, and site information. Replace a certificate Find the certificate that you want to replace and click the icon in the **Actions** column. In the **Edit File** panel, replace the certificate with another certificate. Delete a certificate For example, if you want to delete an SSL certificate, select the SSL certificate and choose
**More** > **Delete selected certificate**. In the message that appears, click **OK**.

### 5.9 Data masking

You can configure data masking policies to mask sensitive data in logs, such as national ID numbers, birth dates, bank card numbers, passwords, and other user-defined sensitive data.

**Important**

The log data masking feature for a physical WAF is only supported on x86 architectures, not on ARM, due to hardware limitations.
1. Log on to the Apsara Uni-manager console.
2. In the upper-right corner of the console, click **Security** and choose **Application Security**
**> Web Application Firewall**. On the **Web Application Firewall** authorization page,
select a **Region** and click **Authorize by Role**.
3. In the left-side navigation pane, choose **Protection Configuration > Data**
**Desensitization**.
4. On the **Log Data Desensitization** page, click
to the right of **Disabled**. In the **Edit**
**Log Desensitization** dialog box, turn on the **Log Desensitization** switch
.
5. Configure the **Built-in Parameters** and **Custom Parameters** as needed.

### 5.10 Use your computer to verify the access configurations

**the access configurations**

This topic describes how to use your computer to verify the access configurations of your website.

**Background information**

Before you use Web Application Firewall (WAF) to scrub traffic that is destined for a website, we recommend that you use your computer to verify the access configurations of the website. After you add the virtual IP address and domain name of a website to the hosts file on your computer, the request to access the domain name from your browser first passes through WAF.

**Procedure**

1. Add the virtual IP address and domain name to the hosts file on your computer.
If your computer runs Windows 7, the hosts file is stored in the following path: C:\Windows\System32\drivers\etc\hosts. i. Open the hosts file by using a text editor, such as Notepad. ii. Add the following content to the end of the file: `<The virtual IP address that is`

```
assigned by WAF><Protected domain name> .
```

The IP address that precedes the domain name is the virtual IP address that is assigned by WAF.
2. Ping the protected domain name.
The returned IP address must be the virtual IP address that is assigned by WAF in the hosts file. If the returned IP address is still the IP address of the origin server, refresh the onpremises Domain Name System (DNS) cache.
3. Enter the domain name in the address bar of your browser and press the Enter key.
If the access configurations are correct, you can visit the website.
4. Verify the protection capability of WAF.
Simulate a web attack and check whether WAF blocks the attack. For example, add /?alert(xss) to the URL. If you try to visit www.example.com/? `alert(xss)` , WAF is expected to block the attack.

### 5.11 Modify DNS settings

Before you can modify your Domain Name System (DNS) settings, you must make sure that the access configurations of your website are correct. After you modify the DNS settings, the traffic that is destined for your website can be redirected to Web Application Firewall (WAF). This topic describes how to modify the DNS settings to add your website to WAF. The domain name of a protected website may not be resolved by a DNS provider. For example, a website may use a Server Load Balancer (SLB) instance to connect to the Internet. In this case, you can change the back-to-origin IP address of the SLB instance to the virtual IP address that WAF assigns to your website.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration > Protection Site**
**Management**.
4. Find the website whose DNS settings you want to modify and click the
icon in the
**Actions** column.
5. On the **Basic Information** tab, record the virtual IP address that is assigned to the
website.
6. Log on to the console of the DNS provider and find the DNS settings for the domain name of
the website. Then, change the IP address in the A record to the virtual IP address that is assigned to the website. We recommend that you set the time-to-live (TTL) to 600 seconds in DNS settings. If you specify a higher value for the TTL, the period of time that is required to synchronize and update DNS records is longer.

## 6 System management

### 6.1 Configure alert settings

#### 6.1.1 Configure alerts

After you add a syslog server to Web Application Firewall (WAF), WAF alert logs can be pushed to the syslog server over the syslog protocol. This topic describes how to add a syslog server to WAF.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings** > **Syslog Configuration**.
4. On the **Alarm Service Configuration** tab, click **Add alarm service**.
5. In the **Add Alarm Service** panel, configure the parameters and click **Confirm**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Syslog Server | The IP address and port number of the syslog server. |
| RFC | The Request for Comments (RFC) document that defines the syslog protocol. Valid values: RFC3164 and RFC5424. |
| Protocol | The transmission protocol. Valid values: TCP and UDP. |
| Comment | The description of the syslog server. This information facilitates identification and management. |
| General | The type of alert. Valid values: System Management and System Monitor and Alarm. |
| Security | The module whose alert logs are sent to the syslog server. Valid values: Website Management, Security Policy Management, ACL Management, Attack Detection Log, Access Log, and ACL Rule Execution Log. |

6. Find the new syslog server and click the
icon in the **Actions** column to test whether alerts are sent. If a message appears, indicating that the alert test is successful, the syslog server is added to WAF. If an error message appears, WAF cannot connect to the syslog server. You can troubleshoot the error based on the error message and click the icon to retest whether alerts are sent.

#### 6.1.2 Configure alert thresholds

This topic describes how to configure alert thresholds.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings > Alert Settings**.
4. On the **Alert Threshold Configurations** tab, click the
icon to the right of the threshold that you want to modify.
5. In the panel that appears, specify the threshold.

| Threshold | Description |
|---|---|
| Queries per Second | If the number of queries per second exceeds the threshold, alerts are triggered. If the threshold is set to 0, no alerts are triggered. |
| New Connections | If a large number of new connections exist, no alerts are triggered. |

| High CPU Utilization | If the CPU utilization exceeds the threshold for a specific period of time, alerts are triggered. |
|---|---|
| High Memory Usage | If the memory usage exceeds the threshold for a specific period of time, alerts are triggered. |
| High Disk Usage | If the disk usage exceeds the threshold, alerts are triggered. |

6. Click **Ok**.

### 6.2 Online backup

This topic describes how to create an online backup.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a region from the
**Region** drop-down list and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings > Online Backup**.
4. On the Online Backup page, click **Create Backup**. In the **Add Backups** panel, configure
the Description parameter and click **OK**. You can back up information such as protected websites and related protection policies, online backup rules, and certificates.

**Manage online backups**

You can view and manage online backups in the online backup list. Select the online backups that you want to manage, move the pointer over **More**, and then select **Download Selected Backups** or **Delete Selected Backups** to download or delete the backups.

### 6.3 Other system settings

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the console, click **Security**. Then, choose **Application**
**Security > Web Application Firewall**. On the **Web Application Firewall** page, select a
**region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings > Other System**
**Configurations**.
4. On the **Other System Configurations** page, click the
icon next to the configuration item. In the **Edit Expiration Reminder for SSL Certificate** panel, specify the warning days before the certificate expiration, and then click **OK**. You can only set the value to a number from 1 to 180.

### 6.4 Global system settings

You can configure global system settings to enable or disable the Web Application Firewall (WAF) global protection engine, specify an internal-facing Server Load Balancer (SLB) instance as the downstream service, and configure shared virtual IP addresses. This topic describes how to configure global system settings.

**Important**

The **Global System Settings** feature has been migrated to **Cloud Shield Operations**
**Center > Cloud Services > WAF Management**. For more information, see the

**Physical server-based WAF O&M in Cloud Shield Operations Center > Global**

**system settings** topic in the WAF **O&M Guide (Tenant-side)-Physical servers**.

## 7 System information

### 7.1 Node status

#### 7.1.1 View the loads on nodes

This topic describes how to view the loads on Web Application Firewall (WAF) nodes. The loads include CPU utilization and memory usage. You can identify faults based on the loads and check whether a scale-out or a scale-up activity is required.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the
**Application Security** section, click **Web Application Firewall**. On the **Web Application**
**Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Payload Status** tab, you can view the loads on WAF nodes.
In the Payload Status section, you can view the CPU utilization and memory usage of WAF nodes. In the **CPU usage** and **Memory usage** sections, you can view the changes in CPU utilization and memory usage over a specific period of time.

#### 7.1.2 View the network information of nodes

This topic describes how to view the network information of Web Application Firewall (WAF) nodes. The information includes the network I/O, traffic detection statistics, and traffic forwarding statistics.

**Network information**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the
**Application Security** section, click **Web Application Firewall**. On the **Web Application**
**Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Node Status** page, click the **Node Network Status** tab.
5. View the network I/O of WAF nodes.

**Traffic detection statistics**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Node Status** page, click the **Detection Status** tab.
5. View the traffic detection statistics of WAF nodes.

**Traffic forwarding statistics**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Node Status** page, click the **Forward Status** tab.
5. View the traffic forwarding statistics of WAF nodes.

#### 7.1.3 View the node detection status

This topic describes how to view the queries per second (QPS) and the average detection time consumed by WAF nodes.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a **region** and click
**Access with Authorized Role**.
3. In the left-side navigation pane of the **Web Application Firewall** page, choose **System**
**Info > Node Status**.
4. On the **Detection Status** tab, you can view the detection status of each WAF node.
This page displays the QPS and the average detection time consumed by each node. Charts are displayed in the lower part of the page to show the changes over a period of time.

#### 7.1.4 View the node forwarding status

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the console, click **Security**. Then, choose **Application**
**Security > Web Application Firewall**. On the **Web Application Firewall** page, select a
**region** and click **Access with Authorized Role**.
3. In the left-side navigation pane of the **Web Application Firewall**, choose **System Info >**
**Node Status**.
4. On the **Forwarding Status** tab, you can view the forwarding status of each WAF node.
On this page, you can view the number of new connections per second, the number of concurrent connections, and the average processing latency for each node. The changes over a period of time are also displayed in the charts in the lower part of the page.

#### 7.1.5 View the disk information of nodes

This topic describes how to view the disk information of Web Application Firewall (WAF) nodes. You can identify faults based on the information and check whether a scale-out or a scale-up activity is required.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the
**Application Security** section, click **Web Application Firewall**. On the **Web Application**
**Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info** > **Node Status**.
4. Click the Disk Status tab to view the disk information of WAF nodes.
In the Disk Status section, you can view the disk I/O and disk usage of WAF nodes. In the
**Read** and **Write** sections, you can view the changes in disk reads and writes over a
specific period of time.

#### 7.1.6 Historical node data query

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar of the console, click **Security**. Then, choose **Application**
**Security > Web Application Firewall**. On the **Web Application Firewall** page, select a
**region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. Click the **Historical Data Query** tab to view historical data of the target WAF node.
Click the icon next to the **Information Overview**. In the **Edit** panel, specify **Node** and
**Attack Time**, and then click **Query**.
5. In the **Historical System Performance Data** section, you can view the CPU usage,
memory usage, and disk usage. In the **Historical Traffic Monitoring Data** section, you can view the network read I/O, network write I/O, number of new connections per second, and number of detection requests per second.

### 7.2 Back-to-origin IP addresses

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a **region** and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Back-to-origin IP Addresses**.
4. On the **Back-to-origin IP Addresses** page, you can view **Back-to-origin IP Addresses**
**of Physical Servers in Classic Network** and **Back-to-origin IP Addresses of SLB**
**Instances in VPC**.

### 7.3 System firmware information

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. Then, choose **Application Security > Web**
**Application Firewall**. On the **Web Application Firewall** page, select a **region** and click
**Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > System Firmware Information**.
4. On the **System Firmware Information** page, you can view the current firmware version
information, which includes **Instance Name** and **Attack Detection Engine**.
