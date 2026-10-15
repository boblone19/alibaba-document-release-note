---
title: "Alibaba Cloud Security-Web Application Firewall (WAF) Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 14
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Alibaba Cloud Security-Web Application Firewall (WAF) Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99-%E4%BC%81%E4%B8%9A%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20Product%20Introduction%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# Alibaba Cloud Security-Web Application Firewall (WAF) Product Introduction 20260629

Alibaba Cloud Security-Web Appli cation Firewall (WAF) ?

## What is WAF?

Web Application Firewall (WAF) defends against common attacks defined by Open Web Application Security Project (OWASP), including SQL injections, cross-site scripting (XSS) attacks, common web server plug-in vulnerabilities, trojan uploads, and unauthorized access to core resources. WAF filters out numerous malicious access attempts to prevent data leaks of website assets and ensure website security and availability. Apsara Stack WAF rebuilds its capabilities based on algorithm innovation. It releases the intelligent semantic analysis engine to identify web attacks. This is equivalent to building an intelligent brain into WAF and allows WAF to separately identify attack behavior. WAF also uses learning models to continuously enhance the analysis capabilities of the brain. This way, WAF can meet the daily protection requirements of users without relying on traditional rule libraries. The following core features are supported:

**Intelligent detection of attack behaviors**

WAF provides an intelligent detection engine to detect all OWASP attacks without relying on traditional rule libraries. The engine can intelligently identify and analyze HTTP and HTTPS traffic to detect and block security threats.

**Web access control**

WAF supports flexible access control through a built-in access control engine, which collects statistics on client access behavior by IP address and session. Users can configure throttling policies by domain name or URL, and IP address blacklist and whitelist to manage access from specific sources.

| Category | Module | Feature | Description |
|---|---|---|---|
| System Manageme nt | System Info | Back-to-origin IP Addresses | You can view the back-to-origin IP addresses for physical machines that are deployed in the classic network. You can view the back-to-origin IP addresses for Server Load Balancer (SLB) instances that are deployed in a virtual private cloud (VPC). |
|  |  | System Firmware Information | You can view system firmware versions and attack detection engines. |
|  |  | Node Status | Usage: displays the CPU utilization and memory usage. Network Status: displays the read and write throughput. Detection Status: displays the QPS and average detection time. Forwarding Status: displays the number of new connections per second and the average processing latency. Disk Status: displays the disk usage and total disk size. |
|  | System Settings | Global System Settings | Note This feature is visible only to global organization security administrators. They can modify global system settings, including whether to enable the WAF protection engine, whether to allow an internal-facing SLB instance to be specified as the downstream node of a website, whether to enable website tamper-proofing, whether to enable the EIP mode, and the maximum number of logs that can be downloaded. |
|  |  | Other System Configurations | You can configure Secure Sockets Layer (SSL) certificate-related settings. |

Alibaba Cloud Security-Web Appli cation Firewall (WAF)

## Functions and features

Web Application Firewall (WAF) protects web applications from malicious attacks and ensures secure access for mobile and PC users over the Internet.

|  |  | Alert Settings | In the Add Alert Service panel, you can set the Security parameter to Website Management, Security Policy Management, ACL Management, Attack Detection Log, Access Log, or ACL Rule Execution Log. WAF sends logs over the syslog protocol. You can configure service and system- related alert thresholds. |
|---|---|---|---|
|  |  | Online Backup | You can back up protected websites and associated protection policies, custom rules, certificates, and other information. |
| Monitoring and O&M | Statistics | Attack Statistics | You can view attack detection statistics, including the numbers and attack times related to top 100 attack sources and destinations. |
|  |  | Traffic Trend Chart | You can query the trends of queries per second (QPS) traffic by website. |
|  |  | Access Status Monitoring | You can view real-time information about top 100 access requests. You can filter data from the following dimensions: IP address, session, website address, URL, number of requests within 30 seconds, and average response time. The data is refreshed at 5-second intervals. |
|  |  | Overview | You can view the following protection statistics for the previous 24 hours and previous 30 days: The geographical distribution of attackers in China and worldwide The total number of requests processed by WAF, total number of attacks, and total number of blocked requests The IP addresses from which the most attacks are initiated in terms of requests, attacks, and blocked requests Top 5 attack types Top 5 attacked websites |
|  |  | Export | You can export daily, weekly, and scheduled reports for all or specific websites. A report includes Trend of Requests, Most Accessed Websites, Most Accessed IP Addresses, Trend of Total Web Attacks, Type-based Attack Distribution, Distribution of Attack IP Addresses in China, Distribution of Attack IP Addresses Worldwide, and Trend of Total Blocked Requests. |

Alibaba Cloud Security-Web Appli cation Firewall (WAF)

|  | Protection Log | HTTP Flood Protection Logs | You can view HTTP flood protection logs. The logs include request URLs, names of matched rules, and match time. You can filter logs by specifying one or more conditions, including event generation time and rule names. |
|---|---|---|---|
|  |  | Attack Detection Logs | You can view and filter attack detection logs. In the log list, you can view the information about attack detection logs, including the Processing Result, Attacked Address, Attack Type, Attack IP Address, and Attack Time parameters. You can also view details of each log. The details include the attack risk level, decoding method, attack payload after decoding, and each field in an HTTP request. If a blocked request is identified as a false positive, you can click Eliminate False Positive to create a whitelist rule. You can filter logs by specifying one or more conditions, including attack types, source IP addresses, and event generation time. You can also select logs to create a download task, and then go to the Log Download Management page to download JSON or CSV logs to your computer. |
|  |  | Log Download Management | You can manage asynchronous download tasks for attack detection logs. |
|  |  | System Operations Logs | You can view system operations logs, which include usernames, operations, IP addresses, and other information. |
|  |  | Querying With IP | You can specify an IP address to query the rules that are matched by the IP address, such as the type of rules that are matched (HTTP flood attacks or attack detection logs) and the attack details. |
|  |  | Access logs | You can view access logs, which include access addresses, source and destination IP addresses, request methods, response codes, and other information. |

Alibaba Cloud Security-Web Appli cation Firewall (WAF)

|  |  | HTTP Flood Protection | You can configure access control rules for domain names and URLs to restrict the access frequency of IP addresses or sessions that meet the specified conditions or block them. You can also restrict the access frequency of specific IP addresses or sessions or block them. WAF supports the whitelist feature for the HTTP flood protection module. Protection rules of this module are not applicable to IP addresses or sessions in a whitelist. |
|---|---|---|---|
|  |  | Global Custom Rules | You can view rules created by the global administrator. |
|  |  | Threat Intelligence | WAF integrates threat intelligence that is collected from the Internet. This helps enterprises monitor suspicious requests from the Internet, and develop targeted protection policies to defend against attacks. |
|  |  | Protection Policies | WAF supports multiple decoding methods, including URL decoding, JSON parsing, Base64 decoding, hexadecimal conversion, backslash unescape, XML parsing, PHP deserialization, and UTF-7 decoding. WAF supports the detection of SQL injections, cross-site scripting (XSS) attacks, intelligence, cross-site request forgery (CSRF), server-side request forgery (SSRF), PHP deserialization, Java deserialization, Active Server Pages (ASP) code injections, file inclusion attacks, file upload attacks, PHP code injections, command injections, web crawlers, and server responses. WAF provides five built-in protection policies: Default Policy Set, Observation Mode, Strict Protection, Financial Institution, and Internet Enterprise. WAF allows you to configure custom decoding algorithms in the policies, separately enable or disable attack detection modules, and configure the detection granularity. You can specify custom status codes to return for blocked requests, enable HTTP response detection and configure the length of a response body in detection rules, configure the length of a request body in detection rules, and enable or disable detection timeout settings. |

Alibaba Cloud Security-Web Appli cation Firewall (WAF)

| Security Protection | Configure Protection |  |  |
|---|---|---|---|
|  |  | Custom Rules | You can add, delete, enable, and disable custom rules. You can specify the following actions for a custom rule: Allow, Block, Monitor, and Control by Using Detection Module, which allows you to enable specific protection modules to implement finer- grained access control. You can configure match conditions in a custom rule based on the following fields or their combinations: URI, GET Parameter, Decoded Path, Host, Full Cookie, POST Parameter, Full Body, HTTP Status Code, Response Content, and User IP. If you select User IP, you can configure a match condition based on source regions. You can specify attack types and custom status codes for blocked requests. You can also specify a validity period for a custom rule. You can search for custom rules by domain name. |
|  |  | Certificates | You can manage SSL certificates for websites, including uploading certificates and private keys. |

Alibaba Cloud Security-Web Appli cation Firewall (WAF)

|  |  | Protection Site Management | You can add, remove, modify, enable, or disable a website for protection. You can add Internet-accessible websites and VPC-accessible websites. WAF can provide web services by using the elastic IP address (EIP) associated with an SLB instance. In this case, you can quickly bypass WAF by modifying the EIP association settings. You can manage the EIP on the Virtual IP Address Management tab of the Protection Site Management page. By default, WAF provides five shared virtual IP addresses (VIPs). WAF also allows tenants to create exclusive VIPs and custom VIPs. WAF supports traffic forwarding over HTTP and HTTPS on non-standard ports to the domain names and IP addresses of origin servers. You can configure exclusive VIPs, custom VIPs, and multiple VIPs for a single domain name. You can select Forward to Backend Servers, Redirect, or Specify Response Content for WAF to forward back-to-origin requests. If you select Forward to Backend Servers, you can select Weighted Round-robin, Least Connections, or Source IP Address Hash as the load balancing algorithm. You can select Redirect to Specific Instance to allow WAF to forward back-to-origin requests directly to SLB or Elastic Compute Service (ECS) instances in VPCs. In this case, you do not need to associate public IP addresses with the instances. This prevents attackers from obtaining the actual IP addresses of the instances to bypass WAF. You can configure the health check paths of web servers. You can also configure response codes and response timeout periods. You can enable the recording of website access logs to record request headers, request bodies, response headers, and payloads. WAF provides the following built-in protection policies: Default Policy Set, Observation Mode, Strict Protection, Financial Institution, and Internet Enterprise. WAF supports monitoring of origin servers. If the health check of an origin server fails, WAF prompts the failure. You can configure custom values for the X- Forwarded-For header field in HTTP requests for matching. You can add custom header fields to HTTP responses. Canary release settings are supported. You can add domain names or websites by configuring canary release settings, and then enable the block or observe mode. |
|---|---|---|---|

Alibaba Cloud Security-Web Appli cation Firewall (WAF)

|  |  | Anti Tamper Rule | You can configure protection rules of the website tamper-proofing module to prevent specific web pages from being tampered with or accidentally modified. WAF caches static web page resources, such as HTML, SHTML, TXT, JS, CSS, JPG, and PNG files, and directly returns cached pages to prevent tampering. WAF periodically detects web page tampering and generates alerts when tampering is detected. |
|---|---|---|---|

Alibaba Cloud Security-Web Appli cation Firewall (WAF) Alibaba Cloud Security-Web Appli cation Firewall (WAF)

## Architecture

Web Application Firewall (WAF) receives web access traffic and performs protocol parsing and in-depth decoding on the traffic. Then, WAF calls the semantic analysis, access control, and threat intelligence modules to analyze traffic and determines whether to allow or block traffic based on the predefined policies.

**Core**

**Components**

Statistical Website Management Policy Management Log Management Report

**Core**

**Components**

Access Control Rule Detection Semantic Analysis

**Data Collection**

**Layer**

Traffic Parsing In-depth Decoding

**Web Application**

**Traffic**

(HTTP/HTTPS) Traditionally, attacks are identified by matching rules that use regular expressions. However, the rules cannot cover all attack payloads that are based on programming languages. As a result, WAF cannot provide protection as expected. WAF adopts the intelligent semantic analysis algorithm to analyze web requests and responses to identify threats and attacks. The algorithm processes data through four stages: lexical analysis, syntax analysis, semantic analysis, and threat model matching. Semantic Threat Model Lexical Analysis Syntax Analysis Analysis Matching WAF provides built-in syntax compilers for common programming languages. WAF performs in-depth decoding on HTTP and HTTPS payloads, matches the required compiler based on the type of the identified programming language, and then matches the threat model to obtain a threat level. Next, WAF either allows or blocks the related access requests. Threat detection based on intelligent semantic analysis outperforms rule-based threat detection in terms of detection accuracy and false positive rates. Alibaba Cloud Security-Web Appli os cation Firewall (WAF)

## Use scenarios

Web Application Firewall (WAF) provides comprehensive web protection features for various types of websites, including public service, finance, insurance, e-commerce, Online to Offline (O2O), Internet Plus, and gaming websites. WAF can be used to prevent sensitive data leaks and improve data security. For example, you can prevent databases from data download or leaks caused by injection attacks and prevent unauthorized URL access and authorization bypass. For financial customers, WAF can be used to protect business systems in real time, such as portal websites, online business centers, and online customer service. For e-commerce customers, WAF can be used to identify web attacks and ensure website availability. The HTTP flood protection feature of WAF can be used to protect against abnormal access behavior during major events, such as promotion abuse. During critical periods, the Strict Protection policy in WAF can be used to enhance system security or create custom rules to proactively defend against zero-day vulnerabilities.
