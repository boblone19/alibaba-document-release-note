---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Web Application Firewall (WAF) User Guide 20241023"
product_version: "V3.18.3"
doc_version: "20241023"
pdf_pages: 62
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Web Application Firewall (WAF) User Guide 20241023.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20User%20Guide%2020241023.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Web Application Firewall (WAF) User Guide 20241023

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
  - 2.3 Quick start
- 3 Detection overview
  - 3.1 View protection overview
  - 3.2 View access information
  - 3.3 Export protection reports
  - 3.4 View attack detection statistics
  - 3.5 View traffic trends
- 4 Protection logs
  - 4.1 View attack detection logs
  - 4.2 View HTTP flood protection logs
  - 4.3 View system operation logs
  - 4.4 View access logs
- 5 Protection configuration
  - 5.1 Tenant-side WAF
    - 5.1.1 Add an Internet website to WAF for protection
    - 5.1.2 Add a VPC website to WAF for protection
    - 5.1.3 Use your computer to verify the access configurations
    - 5.1.4 Modify DNS settings
    - 5.1.5 Upload a certificate
    - 5.1.6 Manage virtual IP addresses
    - 5.1.7 Configure protection policies
    - 5.1.8 Create a custom rule
    - 5.1.9 Configure a website tamper-proofing rule
    - 5.1.10 Configure an HTTP flood protection rule
    - 5.1.11 Configure the HTTP flood whitelist
    - 5.1.12 Configure a log privacy policy
    - 5.1.13 Query logs by IP address
  - 5.2 Platform-side WAF
    - 5.2.1 Add a website to WAF for protection
    - 5.2.2 Configure protection policies
    - 5.2.3 Create a custom rule
    - 5.2.4 Configure an HTTP flood protection rule
- 6 System management
  - 6.1 Configure alerts
  - 6.2 Configure alert thresholds
  - 6.3 Configure global system settings
  - 6.4 View the loads on nodes
  - 6.5 View the network information of nodes
  - 6.6 View the disk information of nodes

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

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters such as the exclamation point (!), at sign (@), number sign (#), dollar sign ($), and percent sign (%).

3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Manage MFA** section in **Apsara Uni-manager** **Management Console User Guide**.

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

> **Note:** Only real-time access monitoring information about the top 100 web services that are most accessed is displayed.

### 3.3 Export protection reports

Web Application Firewall (WAF) supports manual and automatic export of protection reports. This topic describes how to export protection reports.

**Export protection reports**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Statistic > Export Detection Report**.
4. On the **Export Detection Report** page, export protection reports.

> **Note:** All protection reports are displayed on the **Protection report** tab regardless of whether the protection reports are manually exported or automatically exported.

Manually export a protection report On the **Protection report** tab, click **Run a report manually**. Configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Report name | The name of the protection report. |
| Report Type | The type of the protection report. Valid values: Daily Report, Weekly Report, and Customized. |
| Statistical Period | The time range during which statistics are collected for the protection report. The valid values of this parameter vary based the value of the Report Type parameter. |
| Statistical Scope | The scope of websites whose statistics are collected for the protection report. Valid values: All sites and Specify a Statistical Site. |
| Sire- rootRelativePath | Enter the root directory of the website. Valid values: http://: The website uses only HTTP. http(s)://: The website uses both HTTP and HTTPS. |

Automatically export a protection report On the **Scheduled report run task** tab, click **Add a scheduled report run task** . Configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Report name | The name of the protection report. |

| Report Type | The type of the protection report. Valid values: Daily Report and Weekly Report. |
|---|---|
| Statistical Scope | The scope of websites whose statistics are collected for the protection report. Valid values: All sites and Specify a Statistical Site. |
| Sire- rootRelativePath | Enter the root directory of the website. Valid values: http://: The website uses only HTTP. http(s)://: The website uses both HTTP and HTTPS. |

**Manage protection reports**

On the **Protection Report** tab, you can view and manage the protection reports. Filter protection reports Click **Filter**, specify filter conditions, and then click **OK**.

> **Note:** If you specify multiple filter conditions, WAF uses the AND operator to combine the filter conditions. The system returns reports that match the conditions.

View report details Find the protection report whose details you want to view and click the icon in the
**Actions** column.
Download protection reports Select the protection reports that you want to download and choose **More > Download**
**Selected Report**.
Delete protection reports Select the protection reports that you want to delete and choose **More > Delete Selected**
**Report**.

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
On the Attack Detection Logs page, you can view attack detection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**.

> **Note:** If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions.

Export logs a. Select the logs that you want to export and select **Download selected log(.json)** or
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
On the HTTP Flood Detection Logs page, you can view HTTP flood protection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**.

> **Note:** If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions.

Add an HTTP flood attack to the blacklist Find the HTTP flood attack that you want to add to the blacklist and click the icon in the
**Actions** column to create a blacklist rule. In the **Add to Blacklist** panel, enter a name
for the blacklist rule and click **OK**.

### 4.3 View system operation logs

This topic describes how to view system operation logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > System Operation Log**.
On the Attack Detection Logs page, you can view attack detection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**.

> **Note:** If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions.

Export logs a. Select the logs that you want to export and select **Download selected log(.json)** or
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
On the Attack Detection Logs page, you can view attack detection logs and perform the following operations based on your business requirements: Filter logs Click **Filter**, specify filter conditions, and then click **OK**.

> **Note:** If you specify multiple filter conditions, Web Application Firewall (WAF) combines the conditions by using the logical AND operator. The system returns logs that match all conditions.

Export logs a. Select the logs that you want to export and select **Download selected log(.json)** or
**Download selected log(.csv)** from the **More** drop-down list. In the Alert message,
click **OK**. b. In the left-side navigation pane, choose **Detection Logs > Downloading Log**
**Management**. Find the download task that you created and click the
icon in the
**Actions** column to download the logs.
Switch between display modes In the upper-right corner of the Attack Detection Logs page, click the icon and select
**List** or **Detailed View** to specify the display mode for the logs.

## 5 Protection configuration

### 5.1 Tenant-side WAF

#### 5.1.1 Add an Internet website to WAF for protection

**protection**

Tenant-side Web Application Firewall (WAF) can protect Internet websites and virtual private cloud (VPC) websites. This topic describes how to add an Internet website to WAF.

**Background information**

For information about how to add an Internet website to WAF, refer to this topic. For information about how to add a VPC website to WAF, see Add a VPC website to WAF for protection.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration** > **Protection Site**
**Management**.
4. On the **Internet Websites** tab, click **Add a site**.
5. In the **Monitoring Information** step of the **Add Protected Site** panel, configure the
parameters and click Next. The following table describes the parameters. WAF can protect HTTP and HTTPS websites.

| Parameter | Description |
|---|---|
| Protected Website Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You can use an asterisk (*) as a wildcard character. If you specify multiple domain names, separate the domain names with commas (,). |
| Remarks | The description of the website. |

| Port Settings | The port on which WAF listens. If the website can be accessed over multiple ports, click Add a group of ports to add the ports. If the website can be accessed only over HTTP, you can skip the configuration of the certificate and configure the Downstream parameter. If the website can be accessed over HTTPS, select Enable SSL and configure the parameters. If the website can be accessed over HTTP/2, select Enabled HTTP2. This option is available only when you select Enable SSL. |
|---|---|
| Certificate Config | The certificate type of the website. By default, SSL Cert is selected. |
| SSL Cert Setting | The SSL certificate of the website. You can select Upload a New Certificate or Choose an Existing Certificate. Upload a New Certificate: If the SSL certificate of the website is not uploaded to WAF, select this option. By default, the SSL certificate and the private key are separately uploaded. If you select Include private key in certificate file, upload only one file that contains the SSL certificate and the private key. Choose an Existing Certificate: If the SSL certificate of the website is uploaded to WAF, select this option. Then, select the required SSL certificate from the drop-down list. |
| Name | The name of the SSL certificate. |
| SSL Cert File | The SSL certificate and private key. By default, the SSL certificate and the private key are separately uploaded. If you select Include private key in certificate file to the right of Name, upload only one file that contains the SSL certificate and the private key. |
| SSL Certificate Password | The password of the SSL certificate. |

| Two-way authentication | Click the icon to enable mutual authentication and configure the parameters. CA Certificate Settings: the certificate authority (CA) certificate. You can select Upload a New Certificate or Choose an Existing Certificate. Upload a New Certificate: If the CA certificate of the website is not uploaded to WAF, select this option. Configure the CA Certificate Name and CA Certificate File parameters. Choose an Existing Certificate: If the CA certificate is uploaded to WAF, select this option and enter a keyword to search for the CA certificate. Then, select the CA certificate from the drop-down list. Detection Depth: the detection depth. SSL Verify Client: the verification of the client certificate. You can select ON, OFF, OPTIONAL, or OPTIONAL NO CA from the drop-down list. If the client certificate is provided, select OPTIONAL. If the client certificate is issued by a non-trusted CA, select OPTIONAL NO CA. |
|---|---|
| Downstream | The downstream node. Valid values: Select an existing virtual IP Create virtual IP Create specified virtual IP |
| Virtual IP | The virtual IP address. Important By default, you can select up to eight virtual IP addresses. Configure this parameter only if you select Select an existing virtual IP from the Downstream drop-down list. |
| Virtual IP Type | The type of the virtual IP address. Valid values: Internet Virtual IP Intranet Virtual IP Important This parameter is required only if you select Create virtual IP or Create specified virtual IP from the Downstream drop-down list. |

| Virtual IP Version | The version of the virtual IP address. Valid values: ipv4 ipv6 Important This parameter is required only if you select Create virtual IP from the Downstream drop-down list. |
|---|---|
| Whether to specify a computer room | Specifies whether the specified virtual IP address is used by the specified data center. Valid values: Yes No Important Configure this parameter only if you select Create specified virtual IP from the Downstream drop-down list. |
| Custom IP | The custom virtual IP address. Important This parameter is required only if you select Create specified virtual IP from the Downstream drop-down list and select No from the Whether to specify a computer room drop-down list. |
| Name of the computer room | The name of the data center that uses the virtual IP address. Important This parameter is required only if you select Create specified virtual IP from the Downstream drop-down list and select Yes from the Whether to specify a computer room drop-down list. |

6. In the **Request Processing** step of the **Add Protected Site** panel, configure the
parameters and click **Next**. The following table describes the parameters.

| Response mode | Parameter | Description |
|---|---|---|
|   | Load Balancing Algorithm | The algorithm that is used for load balancing. Valid values: Weighted Round Robin, Source Address Hash, and Least Connections Method. |

| er Guide·Protection co |   |   |
|---|---|---|
| Forward to Backend Server |   |   |
|   | Backend Server Address | The address of the origin server to which WAF forwards traffic. Valid values: Fill in the back-to- source address and Return to the back-to-source instance. Fill in the back-to-source address: Enter the address of the origin server. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorithm. Return to the back-to-source instance: Enter the address of a specific Elastic Compute Service (ECS) or SLB instance. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorithm. |
|   | X-Forwarded-For | The pass-through mode of the originating IP address. The X-Forwarded-For (XFF) header is used to identify the originating IP address of an HTTP client. The header is used for traffic forwarding services, such as HTTP proxy and load balancing. Valid values: Add last hop IP address to the end of X- Forwarded-For Use last hop IP address as X-Forward-For Remain Unchanged |
| Redirect | Response Status Code | The HTTP status code that is returned when WAF redirects inbound traffic to a specific address. Valid values: 301, 302, 307, and 308. 301: The requested page is permanently redirected to another URL. 302: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 307: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 308: The requested page is permanently redirected to another URL. |
|   | Redirect address | The destination URL to which requests are redirected. |
| Respond with Specified Content | Response Status Code | The HTTP status code that is returned when WAF returns the specified content. Valid value: 200, 400, 401, 402, 404, 405, 500, 503, and 504. |
|   | Response | The content that you want to be returned. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

7. In the **Protection Policy** step of the Add Protected Site panel, configure the parameters
and click **Next**. Then, go to the **Finish** step.

> **Important:** You can configure a protection rule only if you set the **Request Processing Method** parameter to **Forward to Backend Server**.

| Parameter | Description |
|---|---|
| Protection Policy | Select a WAF protection policy. By default, Default Policy Set is selected. Valid values: Disable Protection Policy Default protection policy Default Policy Set Strict Protection Internet Enterprise Financial Institution Observation Mode Custom protection policy For information about the preceding protection policies, see Configure protection policies. |
| User Identification | Specify whether to enable the user identification feature. Note If you enable HTTP flood protection for the protected website and set the Target Type parameter to SESSION when you configure the HTTP flood protection rule, you must set the User Identification parameter to WAF User System. |

After you add Internet websites to WAF, you can perform the following operations in the protected website list: View added Internet websites You can view information about the Internet websites that you added to WAF, such as the name, port, domain name, and downstream node. Specify the items that you want to view in the protected website list Click the icon to the right of **Actions** and select the items that you want to view in the protected website list. Filter Internet websites In the upper-right corner of the Protection Site Management page, click **Filter** and specify filter conditions, such as the name, domain name, protection policy, status of the website tamper-proofing feature, creation time, and most recent modification time. Enable, disable, export, or delete protected websites Select the protected websites that you want to manage. Select **Enable Selected Sites**,
**Disable Selected Sites**, **Export Selected Sites**, or **Delete Selected Sites** from the
**More** drop-down list.
Modify the basic information about protected websites Find the protected website whose basic information you want to modify and click the icon in the **Actions** column. On the **Basic Information** tab, click the icon to the right of each configuration item to modify the corresponding information. You can modify the following information about the website on the Basic Information tab: name, status, listening port, domain name, remarks, and downstream node. Modify the request processing mode of protected websites Find the protected website whose processing mode you want to modify and click the icon in the **Actions** column. On the **Request Processing** tab, click the icon to the right of each configuration item to modify the corresponding information. You can modify the following information about the website on the Request Processing tab: request processing mode, scheduling algorithm, X-Forwarded-For, status of backend server health check, access log record method, backend server address, HTTP header, and back-to-origin IP address. View and modify protection methods Website Protection Policies View the details of the protection policies that you configured, such as decoding methods, attack detection modules, block options, HTTP response processing, HTTP request body detection, and detection timeout. Click the icon to the right of **Default Policy Set** to modify protection policies. For more information about protection policies, see Configure protection policies. Customize Rules: You can click Add Customized Rule to create custom rules in the Customize Rules section. For more information, see Create a custom rule. Source IP Recording Options: You can specify the method to obtain the IP address of the origin server. The IP address of the origin server can be obtained from the X- Forwarded-For header. BOT Protection Strategy: You can click Add BOT Protection Strategy to create bot management rules in the BOT Protection Strategy section. For more information, see Configure the bot management feature.

#### 5.1.2 Add a VPC website to WAF for protection

**protection**

Web Application Firewall (WAF) can protect Internet websites and virtual private cloud (VPC) websites. This topic describes how to add a VPC website to WAF for protection.

**Background information**

For information about how to add an Internet website to WAF, see Add an Internet website to WAF for protection. For information about how to add a VPC website to WAF, refer to this topic.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**. In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration** > **Protection Site**
**Management**.
4. On the **Protection Site Management** page, click the VPC Websites tab.
5. On the **VPC Websites** tab, click **Add a site**.
6. In the **Monitoring Information** step of the **Add Protected Site** panel, configure the
parameters and click **Next**. The following table describes the parameters. WAF can protect HTTP and HTTPS websites.

| Parameter | Description |
|---|---|
| Protected Website Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You can use an asterisk (*) as a wildcard character. If you specify multiple domain names, separate the domain names with commas (,). |
| Remarks | The description of the website. |
| Port Settings | The port on which WAF listens. If the website can be accessed over multiple ports, click Add a group of ports to add the ports. If the website can be accessed only over HTTP, clickN ext. For more information, see Step 7. If the website can be accessed over HTTPS, select Enable SSL and configure the parameters. If the website can be accessed over HTTP/2, select Enabled HTTP2. This option is available only when you select Enable SSL. |
| Certificate Config | The certificate type of the website. By default, SSL Cert is selected. |

| SSL Cert Setting | The SSL certificate of the website. You can select Upload a New Certificate or Choose an Existing Certificate. Upload a New Certificate: If the SSL certificate of the website is not uploaded to WAF, select this option. By default, the SSL certificate and the private key are separately uploaded. If you select Include private key in certificate file, upload only one file that contains the SSL certificate and the private key. Choose an Existing Certificate: If the SSL certificate of the website is already uploaded to WAF, select this option. Then, select the required SSL certificate from the drop-down list. |
|---|---|
| Name | The name of the SSL certificate. |
| SSL Cert File | The SSL certificate and the private key. By default, the SSL certificate and the private key are separately uploaded. If you select Include private key in certificate file to the right of Name, upload only one file that contains the SSL certificate and the private key. |
| SSL Certificate password | The password of the SSL certificate. |
| Two-way authentication | Click the icon to enable mutual authentication and configure the parameters. CA Certificate Settings: the certificate authority (CA) certificate. You can select Upload a New Certificate or Choose an Existing Certificate. Upload a New Certificate: If the CA certificate of the website is not uploaded to WAF, select this option. Configure the CA Certificate Name and CA Certificate File parameters. Choose an Existing Certificate: If the CA certificate is already uploaded to WAF, select this option and enter a keyword to search for the CA certificate. Then, select the CA certificate from the drop-down list. Detection Depth: the detection depth. SSL Verify Client: the verification of the client certificate. You can select ON, OFF, OPTIONAL, or OPTIONAL NO CA from the drop-down list. If the client certificate is provided, select OPTIONAL. If the client certificate is issued by a non-trusted CA, select OPTIONAL NO CA. |

7. In the **set up VPC** step, configure the parameters and click Next. The following table
describes the parameters.

| Parameter | Description |
|---|---|

| Protected VPC | The VPC to which the website that you want WAF to protect belongs. |
|---|---|
| Downstream | The downstream node. Valid values: Create specified virtual IP Select an existing virtual IP SLB Create virtual IP EIP Important You can select SLB only if you choose System Settings > Global System Settings and turn on Internal-facing SLB instances are used as the downstream. |
| Virtual Switch | The vSwitch that is associated with the website. |
| SLB | The Server Load Balancer (SLB) instance that is associated with the website. |
| Create Virtual IP Method | The method that is used to create a virtual IP address. Valid values: Select an existing virtual IP and Create virtual IP. |
| VPC Virtual IP | If you set the Create Virtual IP Method parameter to Select an existing virtual IP, select an existing virtual IP address from the VPC Virtual IP drop-down list. Important By default, you can select up to eight virtual IP addresses. If you set the Create Virtual IP Method parameter to Create virtual IP, click Click to Create Vip next to VPC Virtual IP to generate a virtual IP address. |

8. In the Request Processing step, configure the parameters and click **Next**. The following
table describes the parameters.

| Response mode | Parameter | Description |
|---|---|---|
|   | Load Balancing Algorithm | The algorithm that is used for load balancing. Valid values: Weighted Round Robin, Source Address Hash, and Least Connections Method. |

| er Guide·Protection co |   |   |
|---|---|---|
| Forward to Backend Server |   |   |
|   | Backend Server Address | The address of the origin server to which WAF forwards inbound traffic. Valid values: Fill in the back-to-source address and Return to the back- to-source instance. Fill in the back-to-source address: Enter the address of the origin server. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorithm. Return to the back-to-source instance: Enter the address of a specific Elastic Compute Service (ECS) or SLB instance. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorithm. |
|   | X-Forwarded-For | The pass-through mode of the originating IP address. The X-Forwarded-For (XFF) header is used to identify the originating IP address of an HTTP client. The header is used for traffic forwarding services, such as HTTP proxy and load balancing. Valid values: Add last hop IP address to the end of X- Forwarded-For Use last hop IP address as X-Forward-For Remain Unchanged |
| Redirect | Response Status Code | The HTTP status code that is returned when WAF redirects inbound traffic to a specific address. Valid values: 301, 302, and 307. 301: The requested page is permanently redirected to another URL. 302: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. 307: The requested page is temporarily redirected to another URL. The requester must continue to use the original URL for subsequent requests. |
|   | Redirect address | The destination URL to which requests are redirected. |
| Respond with Specified Content | Response Status Code | The HTTP status code that is returned when WAF returns the specified content. Valid values: 200, 404, and 503. |
|   | Response | The content that you want to be returned. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

9. In the Protection Policy step, configure the parameters and click Next. Then, go to the
Finish step. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Protection Policy | Select a WAF protection policy. By default, Default Policy Set is selected. Valid values: Disable Protection Policy Default protection policy Default Policy Set Strict Protection Internet Enterprise Financial Institution Observation Mode Custom protection policy For information about the preceding protection policies, see Configure protection policies. |
| User Identification | Specify whether to enable the user identification feature. Note If you enable HTTP flood protection for the protected website and set the Target Type parameter to SESSION when you configure the HTTP flood protection rule, you must set the User Identification parameter to WAF User System. |

After you add VPC websites to WAF, you can perform the following operations in the protected website list: View added VPC websites You can view information about the VPC websites that you added to WAF. The information includes the name, port, domain name, and downstream node. Specify the items that you want to view in the protected website list Click the icon to the right of **Actions** and select the items that you want to view in the protected website list. Filter VPC websites In the upper-right corner of the Protection Site Management page, click **Filter** and specify filter conditions, such as the name, domain name, protection policy, status of the website tamper-proofing feature, creation time, and most recent modification time. Enable, disable, export, or delete protected websites Select the protected websites that you want to manage. Select **Enable Selected Sites**,
**Disable Selected Sites**, **Export Selected Sites**, or **Delete Selected Sites** from the
**More** drop-down list.
Modify the basic information about protected websites Find the protected website whose basic information you want to modify and click the icon in the **Actions** column. On the **Basic Information** tab, click the icon next to each configuration item to modify the corresponding information. You can modify the following information about the website on the Basic Information tab: name, status, listening port, domain name, remarks, and downstream node. Modify the request processing mode of protected websites Find the protected website whose processing mode you want to modify and click the icon in the **Actions** column. On the **Request Processing** tab, click the icon next to each configuration item to modify the corresponding information. You can modify the following information about the website on the Request Processing tab: request processing mode, scheduling algorithm, X-Forwarded-For, status of backend server health check, access log record method, backend server address, HTTP header, and back-to-origin IP address. View and modify protection methods Website Protection Policies You can view the details of the protection policies that you configured, such as the decoding methods, attack detection modules, block options, HTTP response processing, HTTP request body detection, and detection timeout. Click the icon next to **Default Policy Set** to modify protection policies. For more information about protection policies, see Configure protection policies. Customize Rules: You can click Add Customized Rule to add custom rules in the Customize Rules section. For more information, see Create a custom rule. Source IP Recording Options BOT Protection Strategy: You can click Add BOT Protection Strategy to add bot management rules in the BOT Protection Strategy section. For more information, see Configure the bot management feature.

#### 5.1.3 Use your computer to verify the access configurations

**configurations**

This topic describes how to use your computer to verify the access configurations of your website.

**Background information**

Before you use Web Application Firewall (WAF) to scrub traffic that is destined for a website, we recommend that you use your computer to verify the access configurations of the website. After you add the virtual IP address and domain name of a website to the hosts file on your computer, the request to access the domain name from your browser first passes through WAF.

**Procedure**

1. Add the virtual IP address and domain name to the hosts file on your computer.
If your computer runs Windows 7, the hosts file is stored in the following path: C:\Windows\System32\drivers\etc\hosts. i. Open the hosts file by using a text editor, such as Notepad. ii. Add the following content to the end of the file: `<The virtual IP address that is`

```
assigned by WAF><Protected domain name> .
```

> **Note:** The IP address that precedes the domain name is the virtual IP address that is assigned by WAF.

2. Ping the protected domain name.
The returned IP address must be the virtual IP address that is assigned by WAF in the hosts file. If the returned IP address is still the IP address of the origin server, refresh the onpremises Domain Name System (DNS) cache.
3. Enter the domain name in the address bar of your browser and press the Enter key.
If the access configurations are correct, you can visit the website.
4. Verify the protection capability of WAF.
Simulate a web attack and check whether WAF blocks the attack. For example, add /?alert(xss) to the URL. If you try to visit www.example.com/? `alert(xss)` , WAF is expected to block the attack.

#### 5.1.4 Modify DNS settings

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
the website. Then, change the IP address in the A record to the virtual IP address that is assigned to the website.

> **Note:** We recommend that you set the time-to-live (TTL) to 600 seconds in DNS settings. If you specify a higher value for the TTL, the period of time that is required to synchronize and update DNS records is longer.

#### 5.1.5 Upload a certificate

After you upload a certificate on the Certificate Management page, you can select the certificate when you add a website to Web Application Firewall (WAF) on the Protection Site Management page. This topic describes how to upload a certificate.

> **Note:** When you add an HTTPS website for protection on the **Protection Site Management** page, you must select the certificate to which the domain name of the HTTPS website is bound.

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

#### 5.1.6 Manage virtual IP addresses

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

#### 5.1.7 Configure protection policies

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

| er Guide·Protection configurati | Alibaba Cloud Security-Web Appl cation Firewall (WAF |
|---|---|

| HTTP Request Detection | Configure Response Detection Max Body Size. |
|---|---|
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

> **Note:** You cannot delete the default protection policy.

#### 5.1.8 Create a custom rule

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
| Matching Pattern | The match conditions of the rule. You can click Add Pattern to specify multiple match conditions. A request matches the rule only if the request meets all match conditions. |
| Action | You can select Enabled or Disabled from the drop-down list to enable or disable the rule. |
| Apply to Websites | The websites for which you want the rule to take effect. You cannot enter a website name that contains the asterisk (*) wildcard character. |
| Log Recording Option | Specifies whether to record a log when the rule is triggered. The default value is Enable Log Recording. After you set the Log Recording Option parameter to Enable Log Recording, all interception events are recorded in the intrusion detection logs. |

| Attack Type | The type of attack that you want to defend against. |
|---|---|
| Block Status Code | The status code that you want the website to return when a request is blocked. |
| Expiration Time | The expiration time of the rule. |

Add Intelligence Rule

| Parameter | Description |
|---|---|
| Type | The action that you want WAF to perform on requests that match the rule. Valid values: Monitor and Block. Monitor: records and allows requests that match the rule. Block: blocks requests that match the rule. |
| Comment | The description of the rule. We recommend that you enter the protection purpose of the rule. |
| Risk Level | The risk level. Valid values: No threat, Low Risk, Medium Risk, and High Risk. |
| Matching Pattern | The match conditions of the rule. Click Add Pattern to specify multiple conditions. A request matches the rule only if the request meets all match conditions. |
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

#### 5.1.9 Configure a website tamper-proofing rule

**rule**

You can configure website tamper-proofing rules to protect web page data from being tampered with. This topic describes how to configure a website tamper-proofing rule.

**Create a website tamper-proofing rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**. In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings > Global System Settings**.
Set the **Anti Tamper** parameter to **On** to enable the website tamper-proofing feature.

> **Note:** By default, the website tamper-proofing feature is disabled. After you enable the website tamper-proofing feature, the feature is displayed in the left-side navigation pane of the console.

4. In the left-side navigation pane, choose **Protection Configuration > Anti Tamper Rule**.
5. In the upper-right corner of the Anti Tamper Rule, click **Add Rule**. In the **Add Anti Tamper**
**Rule** panel, configure the parameters and click **Confirm**. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Status | The status of the website tamper-proofing rule. You can select Enable or Disable. |
| Comment | The description of the rule. We recommend that you enter the protection purpose of the rule. |
| Protocol | The protocol type. Valid values: http and https. |
| Domain | The domain name for which the rule takes effect. If the server is bound to a domain name, you must enter the domain name. |
| Matching Pattern | The match condition of the rule. The type of the match condition can beP age Path or Regular Expression. The page path starts with a forward slash (/) and ends with html, shtml, txt, js, css, jpg, or png. The value cannot exceed 128 characters in length. |
| Apply to Websites | The websites for which the rule takes effect. |

**Manage website tamper-proofing rules**

You can view and manage website tamper-proofing rules in the website tamper-proofing rule list. View website tamper-proofing rules In the website tamper-proofing rule list, you can view the protected page path, creation time, and most recent modification time of each website tamper-proofing rule. Modify a website tamper-proofing rule Find the website tamper-proofing rule whose configurations you want to modify and click the icon in the **Actions** column. Filter website tamper-proofing rules In the upper-right corner of the Anti Tamper Rule page, click **Filter** and specify filter conditions to filter website tamper-proofing rules by ID, remarks, most recent modification time, or creation time. Disable, export, or delete website tamper-proofing rules Select the website tamper-proofing rules that you want to manage and select **Disable**
**Selected Rules**, **Export Selected Rules**, or **Delete Selected Rules** from the **More**
drop-down list to disable, export, or delete the rules.

#### 5.1.10 Configure an HTTP flood protection rule

**rule**

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
| Rule Name | The name of the HTTP flood protection rule. |
| Target Type | The type of source for limited requests. Valid values:I P and SESSION. Note If you set Target Type to SESSION, you can apply the HTTP protection rule only to a website whose User Identification is set to WAF User System. For more information, see Add an Internet website to WAF for protection. |

| Restriction Trigger Threshold | If you set Rule Types to Restrict Users by Policy, you must configure the triggering conditions for the HTTP flood protection rule. |
|---|---|
| Restricted URL Address | If you set Rule Types to Restrict Users by Policy, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Prefix URL Record all IP addresses |
| Restricted IP List or Restricted SESSION List | If you set Rule Types to Restrict Known Users, you must enter the IP addresses or sessions from which you want to limit requests based on the value of Target Type. You can enter only one IP address or session in each line. |
| Restricted URL Address | If you set Rule Types to Restrict Known Users, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Prefix URL Restrict user access to all addresses |
| Restriction Mode | The mode in which the HTTP flood protection rule limits requests. Valid values: Forbidden: The rule blocks specific sources from accessing the specified URL address. Frequency control: The rule limits the frequency at which specific sources access the specified URL address. |
| Restriction Time | The time at which the action that is specified in the HTTP flood protection rule takes effect. |
| Statistical Range of Visits | If you set Rule Type to Restrict Users by Policy, you can specify the range of data records to limit requests in the Advanced section. Statistics Full Access Data: If you select this option, the frequency of requests is limited when the requests are forwarded to WAF and meet the HTTP flood protection rule, regardless of which data records are accessed by requests. This decreases system performance. Statistics TOP Access Data: If you select this option, the frequency of requests is limited when the requests meet the preceding conditions and access the top 100 data records. This option helps reduce the decrease in system performance. You can select this option when the number of accessed data records is greater than 100. Take note that the top 100 data records are measured based on real-time monitoring. |

**Manage HTTP flood protection rules**

You can view and manage HTTP flood protection rules in the HTTP flood protection rule list. View HTTP flood protection rules In the HTTP flood protection rule list, you can view the protection policies, binding situations, creation time, and most recent modification time. Modify HTTP flood protection rules Find the HTTP flood protection rule that you want to modify and click the icon in the
**Actions** column.
Filter HTTP flood protection rules In the upper-right corner of the page, click **Filter** to filter HTTP flood protection rules by ID, name, target type, or creation time. Enable, disable, or delete HTTP flood protection rules Select the HTTP flood protection rules that you want to manage and select **Enable**
**Selected Rules**, **Disable Selected Rules**, or **Delete Selected Rules** from the **More**
drop-down list.

#### 5.1.11 Configure the HTTP flood whitelist

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

#### 5.1.12 Configure a log privacy policy

Web Application Firewall (WAF) allows you to configure log privacy policies to mask sensitive data before the sensitive data is displayed. The sensitive data includes ID card numbers, birth dates, bank card numbers, and passwords.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Configure Protection > Data Privacy**.
4. On the **Log Data Privacy** page, click the
icon to the right of **Disable**. In the panel that appears, click the icon to enable **Log Privacy**.
5. Configure the **Built-in** and **Customized** parameters based on your business requirements.

#### 5.1.13 Query logs by IP address

If you want to check whether an IP address hits a rule that you configure in your Web Application Firewall (WAF) instance, you must query data from multiple sources, which is inefficient. This topic describes how to automatically identify rules that are hit by an IP address.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**. In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Detection Logs > Querying With IP**.
4. On the **Querying With IP** page, select a log type from the **Log Type** drop-down list and
enter the IP address that you want to query in the IP search box.
5. Find the query result that you want to view and click the
icon in the **Actions** column to view the details.

### 5.2 Platform-side WAF

#### 5.2.1 Add a website to WAF for protection

Compared with tenant-side Web Application Firewall (WAF), platform-side WAF is used to manage the status of intrusion protection configurations at the WAF platform management side and the service group management side. Platform-side WAF performs intrusion detection and request processing on platform-side web traffic. If you want WAF to perform actions on traffic to a specific domain name, you must add the domain name to WAF. This topic describes how to add a domain name to WAF.

**Background information**

The following list describes the default configurations of platform-side WAF: By default, **HTTPS proxy traffic forwarding** and **ingress traffic forwarding** are disabled. If the wildcard character (*) is used as a part of the domain name of a protected website and **Platform Observation Mode** is configured for the website, WAF records requests to the website but does not block the requests. The configurations of the website cannot be modified. If you want to block requests to a specific domain name, you must enable **HTTPS proxy traffic forwarding**, add the HTTPS proxy to WAF, and configure protection policies.

**Prerequisites**

Your account is assigned the **platform security configuration administrator** role. For more information, see User roles and permissions.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, choose
> **User Information**.

3. On the page that appears, click **Switch Role**. In the Switch Role dialog box, select
**Platform Security Configuration Administrator** from the **Switch Role** drop-down list.
4. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
5. In the left-side navigation pane, choose **System Settings** > **Global System Settings** and
enable **https-proxy traffic forwarding**.
6. Obtain the domain name.
i. Log on to Apsara Infrastructure Management. ii. In the left-side navigation pane, choose **O&M Tools** > **Basic Data Management**. iii. On the **Basic Data Management** page, click **Resource Dashboard**. Enter
**https_proxy** in the **Name** search box to obtain the logon information and the values of
`db_host` , `db_user` , `db_password` , `db_password` , and `db_name` . iv. Run the following command on the OPS server and log on to the database:

```
mysql -h{db_host} -u{db_user} -p{db_password} -P{db_port} -D{db_name}
```

v. Run the following command to obtain the domain name of the HTTPS proxy:

```
select * from domain_info\G;
```

7. Add the obtained domain name to WAF.
i. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
ii. In the left-side navigation pane, choose **Protection Configuration** > **Protection Site**
**Management**.
iii. On the **Internet Websites** tab, click **Add a site**. iv. In the **Monitoring Information** step of the **Add Protected Site** panel, configure the parameters and click **Next**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Protected Website Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You cannot use an asterisk (*) as a wildcard. If you specify multiple domain names, separate them with commas (,). |
| Description | The description of the website. |
| Port settings | The port on which WAF listens. If the website can be accessed over multiple ports, click Add a group of ports to add the ports. |

v. In the **Protection Policy** step of the **Add Protected Site** panel, configure the parameters and click **Next**. Then, go to the **Finish** step. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Protection Policy | Select a WAF protection policy. By default, Default Policy Set is selected. Valid values: Disable Protection Policy Default protection policies Default Policy Set Strict Protection Internet Enterprise Internet Enterprise Observation Mode Platform Observation Mode Custom protection policy For information about the preceding protection policies, see Configure protection policies. |
| User Identification | Specify whether to enable the user identification feature. Valid values: Disable, WAF User System, and Extract User ID from Request. Note If you enabled HTTP flood protection for the protected website and set the Target Type parameter to SESSION when you configured the HTTP flood protection rule, you must set the User Identification parameter to WAF User System. If you set the User Identification parameter to Extract User ID from Request, you must configure the User ID Locates in and User ID Parameter parameters. |

After you add a website to WAF, WAF processes attacks that match the protection rule. You can perform the following operations on the protected website list. View protected websites You can view information about the Internet websites that you added to WAF, such as the status, name, port, domain name, and protection policy. Specify the items that you want to view in the protected website list. Click the icon to the right of **Actions** and select the items that you want to view in the protected website list. Filter Internet websites In the upper-right corner of the Protection Site Management page, click **Filter** and specify filter conditions, such as the name, domain name, protection policy, status of the website tamper-proofing feature, creation time, and most recent modification time. Enable, disable, export, or delete protected websites Select the protected websites that you want to manage. Select **Enable Selected Sites**,
**Disable Selected Sites**, **Export Selected Sites**, or **Delete Selected Sites** from the
**More** drop-down list.
Modify basic information about protected websites Find the protected website whose basic information you want to modify and click the icon in the **Actions** column. On the **Basic Information** tab, click the icon to the right of each configuration item to modify the corresponding information. You can modify the following information about the website on the Basic Information tab: name, listening port, domain name, and remarks. Modify the method of recording logs Click the icon in the **Actions** column. On the **Request Processing Method** tab, click the icon to the right of **Access Log Record** to modify the method of recording logs. View and modify protection methods Website Protection Policies: View the details of the protection policies that you configured, such as decoding methods, attack detection modules, block options, HTTP response processing, HTTP request body detection, and detection timeout. Click the icon to the right of Default Policy Set to modify protection policies. For more information about protection policies, see Configure protection policies. Customize Rules: You can click Add Customized Rule to add custom rules in the Customize Rules section. For more information, see Create a custom rule. Source IP Recording Options: You can specify the method to obtain the IP address of the origin server. The IP address of the origin server can be obtained from the X- Forwarded-For header. User Identification: You can specify the method to identify users. For more information, see the description of the User Identification parameter in this topic.

#### 5.2.2 Configure protection policies

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
|---|---|
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

> **Note:** You cannot delete the default protection policy.

#### 5.2.3 Create a custom rule

You can create custom rules to meet different requirements for intrusion protection and filter out specific requests. This topic describes how to create a custom rule for Web Application Firewall (WAF).

**Create a custom rule**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Application Security > Web Application Firewall**. On the **Web**
**Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **Protection Configuration** > **Customized Rules**.
4. In the upper-right corner, click **Add Rule**. In the Add Customized Rules panel, configure the
parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Type | The action that you want WAF to perform on requests that match the rule. Valid values: Block: blocks requests that match the rule. Allow: allows requests that match the rule. Monitor: records and allows requests that match the rule. Detection module control |
| Comment | The description of the rule. We recommend that you enter the protection purpose of the rule. |
| Risk level | The risk level. Valid values: No threat, Low Risk, Medium Risk, and High Risk. Note This parameter is required only if you set the Type parameter to Block, Allow, or Monitor. |
| Matching Pattern | The match conditions of the rule. Click Add Pattern to specify more than one condition. A request matches the rule only if the request matches all match conditions. For example, if you want to block requests from a specific path of an HTTPS proxy that is added to WAF, you can set the Type parameter to Block and add the path to the match conditions. |
| Apply to Websites | The websites for which you want the rule to take effect. You cannot enter a website name that contains the asterisk (*) wildcard character. |

| Log Recording Option | Specifies whether to record a log when the rule is triggered. The default value is Enable Log Recording. After you set the Log Recording Option parameter to Enable Log Recording, all interception events are recorded in the intrusion detection logs. |
|---|---|
| Attack Type | The type of attack that you want to block. |
| Blocking Status Code | The status code that you want the website to return when a request is blocked. |
| Expiration Time | The expiration time of the rule. |

5. (Optional) You can create custom rules offline and click **Import Rules** to import the rules at
the same time.

**Configuration example**

If you want to block all requests from an HTTPS proxy that is added to WAF except requests from a specific path, you can set the protection action of the protection policy for the HTTPS proxy to Block and create a custom rule. This section provides a sample configuration.
**Type**: Set the value to **Allow**.
**Matching Pattern**: Set the match field to **URI**, the logical operator to **contain**, and the
match content to the path.
**Apply to Websites**: Select the HTTPS proxy.

**Manage custom rules**

You can view and manage custom rules in the custom rule list. View custom rules In the custom rule list, view the custom rules that you created. Multiple custom rules are evaluated by using a logical **OR**. If two custom rules use the same match conditions but trigger different actions, such as blocking traffic or allowing traffic, WAF runs the first rule. View logs Find the rule whose logs you want to view and click the icon in the **Actions** column to view log information. Modify a custom rule Find the rule that you want to modify and click the icon in the **Actions** column. In the panel that appears, modify the configurations of the rule. Filter custom rules In the upper-right corner of the Customized Rules page, click **Filter**. In the Filter Item panel, specify filter conditions to filter custom rules by ID, comment, most recent modification time, creation time, or expiration time. Enable, disable, export, or delete custom rules Select the rules that you want to manage and select **Enable Selected Rules**, **Disable**
**Selected Rules**, **Export Selected Rules**, or **Delete Selected Rules** from the **More**
drop-down list to enable, disable, export, or delete the rules.

#### 5.2.4 Configure an HTTP flood protection rule

An HTTP flood attack is a type of DDoS attack that targets the application layer. Attackers use proxy servers or zombies to overwhelm targeted web servers by sending a large number of HTTP requests. This topic describes how to configure an HTTP flood protection rule.

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
| Rule Mode | The action that you want WAF to perform on requests that trigger the HTTP flood protection rule. Valid values: Blocking Mode and Observe. Blocking Mode: limits the requests. Observe: records but does not limit the requests. |

| Rule Types | The type of the HTTP flood protection rule. Valid values: Restrict Users by Policy and Restrict Known Users. Restrict Users by Policy: limits requests that meet all the match conditions in the HTTP flood protection rule. You can specify the following match conditions: Restriction Trigger Threshold, Restricted URL Address, Restriction Mode, Restriction Time, and Statistical Range of Visits. The Statistical Range of Visits parameter is in the Advanced section. Restrict Known Users: limits requests that are initiated from specific IP addresses or in specific sessions based on the HTTP flood protection rule. To restrict known users, you must configure the IP address or session list and the limit mode. After you configure the list, the HTTP flood protection rule limits requests based on the list. |
|---|---|
| Rule Name | The name of the HTTP flood protection rule. |
| Target Type | The type of source for limited requests. Valid values:I P and SESSION. Note If you set Target Type to SESSION, you can apply the HTTP protection rule only to a website whose User Identification is set to WAF User System. For more information, see Add an Internet website to WAF for protection. |
| Restriction Trigger Threshold | If you set Rule Types to Restrict Users by Policy, you must configure the triggering conditions for the HTTP flood protection rule. |
| Restricted URL Address | If you set Rule Types to Restrict Users by Policy, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Prefix URL Record all IP addresses |
| Restricted IP List or Restricted SESSION List | If you set Rule Types to Restrict Known Users, you must enter the IP addresses or sessions from which you want to limit requests based on the value of Target Type. You can enter only one IP address or session in each line. |

| Restricted URL Address | If you set Rule Types to Restrict Known Users, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Prefix URL Restrict user access to all addresses |
|---|---|
| Restriction Mode | The mode in which the HTTP flood protection rule limits requests. Valid values: Forbidden: The rule blocks specific sources from accessing the specified URL address. Frequency control: The rule limits the frequency at which specific sources access the specified URL address. |
| Restriction Time | The time at which the action specified in the HTTP flood protection rule takes effect. |
| Statistical Range of Visits | If you set Rule Type to Restrict Users by Policy, you can specify the range of data records to limit requests in the Advanced section. Statistics Full Access Data: If you select this option, the frequency of requests is limited when the requests are forwarded to WAF and meet the HTTP flood protection rule, regardless of which data records are accessed by requests. This decreases system performance. Statistics TOP Access Data: If you select this option, the frequency of requests is limited when the requests meet the preceding conditions and access the top 100 data records. This option helps reduce the decrease in system performance. You can select this option when the number of accessed data records is greater than 100. Take note that the top 100 data records are measured based on real-time monitoring. |

**Manage HTTP flood protection rules**

You can view and manage HTTP flood protection rules in the HTTP flood protection rule list. View HTTP flood protection rules In the HTTP flood protection rule list, you can view the protection policies, binding situations, creation time, and most recent modification time. Modify HTTP flood protection rules Find the HTTP flood protection rule that you want to modify and click the icon in the
**Actions** column.
Filter HTTP flood protection rules In the upper-right corner of the page, click **Filter** to filter HTTP flood protection rules by ID, name, target type, and creation time. Enable, disable, or delete HTTP flood protection rules Select the HTTP flood protection rules that you want to manage and select **Enable**
**Selected Rules**, **Disable Selected Rules**, or **Delete Selected Rules** from the **More**
drop-down list.

## 6 System management

### 6.1 Configure alerts

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

### 6.2 Configure alert thresholds

This topic describes how to configure alert thresholds.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**.In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings > Syslog Configuration**.
4. On the **Alarm Threshold Configuration** tab, click the
icon to the right of the threshold that you want to modify.
5. In the panel that appears, specify the threshold.

| Threshold | Description |
|---|---|
| Queries per second | If the number of queries per second exceeds the threshold, alerts are sent. If the threshold is set to 0, no alerts are sent. |
| Number of new connections | If a large number of new connections exist, no alerts are sent. |
| CPU utilization | If the CPU utilization exceeds the threshold for a specific period of time, alerts are sent. |
| Memory usage | If the memory usage exceeds the threshold for specific a period of time, alerts are sent. |
| Disk usage | If the disk usage exceeds the threshold, alerts are sent. |

6. Click **OK**.

### 6.3 Configure global system settings

**settings**

You can configure global system settings to enable or disable the Web Application Firewall (WAF) global protection engine, internal-facing SLB instances used as the downstream, and shared virtual IP address. This topic describes how to configure global system settings.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click **Security**. In the **Application Security**
section, click **Web Application Firewall**. On the **Web Application Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Settings** > **Global System Settings**.
4. On the **Global System Settings** page, configure the parameters. The following table
describes the parameters.

| Parameter | Description | Operation |
|---|---|---|
| Global WAF Protection Engine | The global WAF protection engine determines the status of intrusion protection configurations at the WAF platform management side and the service group management side. If you turn off Global WAF Protection Engine, WAF allows all traffic and does not perform intrusion detection or traffic processing. | Click the icon to the right of this parameter. In the panel that appears, turn on or turn off the switch and click OK. |
| Internal-facing SLB instances are used as the downstream | Specifies whether an elastic IP address (EIP) that is associated with a Server Load Balancer (SLB) instance can be added to WAF. |   |
| Shared Virtual IP Address | Specifies whether a shared virtual IP address is supported. |   |
| Display the Logo on report header | Specifies whether the Alibaba Cloud logo is displayed on the security report. |   |
| Anti Tamper | Specifies whether web pages can be locked. When a locked page receives a request, a cached version of the page is returned. This helps prevent web page tampering. |   |

| EIP | Specifies whether an EIP can be added to WAF. |   |
|---|---|---|
| https-proxy traffic forwarding | Specifies whether HTTPS proxy traffic forwarding is supported. |   |
| Ingress traffic forwarding | Specifies whether ingress traffic forwarding is supported. |   |
| Create an Extranet shared VIP | Creates an Extranet shared virtual IP address. | Click Click to create on the right side of this parameter. Note If you click Click to create, five Extranet shared virtual IP addresses are created. Proceed with caution. |
| Monitoring Data Retention Period | The retention period of monitoring data. | Click the icon on the right side of this parameter and specify the retention period of monitoring data. Then, click OK. |
| Dump nginx logs to OSS | Specifies whether NGINX logs can be transferred to Object Storage Service (OSS). | Click the icon on the right side of this parameter. In the Edit Dump nginx logs to OSS panel, click the icon and configure the following parameters: Endpoint, AccessKeyId, AccessKeyId, and OSS Path. Then, click OK. |
| Maximum Number Of Journal Downloads | Specifies the maximum number of logs that can be downloaded. | Click the icon on the right side of this parameter and specify the maximum number of logs that can be downloaded. Then, click OK. |

### 6.4 View the loads on nodes

This topic describes how to view the loads on Web Application Firewall (WAF) nodes. The loads include CPU utilization and memory usage. You can identify faults based on the loads and check whether a scale-out or a scale-up activity is required.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the
**Application Security** section, click **Web Application Firewall**. On the **Web Application**
**Firewall** page, select a **region** and click **Access with Authorized Role**.
3. In the left-side navigation pane, choose **System Info > Node Status**.
4. On the **Payload Status** tab, you can view the loads on WAF nodes.
In the Payload Status section, you can view the CPU utilization and memory usage of WAF nodes. In the **CPU usage** and **Memory usage** sections, you can view the changes in CPU utilization and memory usage over a specific period of time.

### 6.5 View the network information of nodes

**of nodes**

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

### 6.6 View the disk information of nodes

**nodes**

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
