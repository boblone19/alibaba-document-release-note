---
title: "Alibaba Cloud Security-Web Application Firewall (WAF) Web Application Firewall-Instance Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 12
source_pdf: "c51fd246c1160f44_Alibaba Cloud Apsara Stack V3.18.6 Alibaba Cloud Security-Web Application Firewall (WAF) Web Applica"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-Web%E5%BA%94%E7%94%A8%E9%98%B2%E7%81%AB%E5%A2%99-%E4%BC%81%E4%B8%9A%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Alibaba%20Cloud%20Security-Web%20Application%20Firewall%20%28WAF%29%20Web%20Application%20Firewall-Instance%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Security-Web Application Firewall (WAF) Web Application Firewall-Instance Product Introduction 20260629

## Table of Contents

- 1 What is WAF - Instance?
- 2 Functions and features
- 3 Service architecture
- 4 Common scenarios

AF - Instance?

## 1 What is WAF - Instance?

Web Application Firewall (WAF) - Instance is a new WAF architecture that is derived from the original physical machine architecture. WAF - Instance is deployed with Elastic Compute Service (ECS) resources and can implement quick auto scaling based on the existing ECS resources to meet the requirements of different customers. Both WAF - Instance and WAF defend against common attacks defined by Open Web Application Security Project (OWASP), including SQL injections, cross-site scripting (XSS) attacks, common web server plug-in vulnerabilities, trojan uploads, and unauthorized access to core resources. Both WAF - Instance and WAF filter out numerous malicious access attempts to prevent data leaks of website assets and ensure website security and availability. Apsara Stack WAF reconstructs its capabilities based on algorithm innovation. It releases the intelligent semantic analysis engine to identify web attacks. This is equivalent to building an intelligent brain into WAF and allows WAF to independently identify attack behavior. WAF also uses learning models to continuously enhance the analysis capabilities of the brain. This way, WAF can meet the daily protection requirements of users without relying on traditional rule libraries. WAF - Instance provides the following core features:

**Intelligent detection of attack behavior**

WAF - Instance provides an intelligent detection engine to detect all OWASP attacks without relying on traditional rule libraries. The engine can intelligently identify and analyze HTTP and HTTPS traffic to detect and block security threats.

**Web access control**

WAF - Instance supports flexible access control through a built-in access control engine, which collects statistics on client access behavior by IP address and session. Users can configure throttling policies by domain name or URL, and IP address blacklist and whitelist policies to manage access from specific sources.

## 2 Functions and features

Web Application Firewall (WAF) protects web applications from attacks and ensures secure access for mobile and PC users over the Internet.

| Categor y | Feature | Description |
|---|---|---|
| Statistics | Overview | You can view the following protection statistics information for the previous 24 hours and previous 30 days: The geographical distribution of attackers in China and worldwide The total number of requests processed by WAF The total number of attacks The total number of blocked requests The IP addresses from which the most attacks are initiated in terms of requests, attacks, and blocked requests Top five attack types Top five attacked websites |
|   | Access Status Monitoring | You can view real-time information about top 100 requests. You can filter data from the following dimensions: IP address, session, website address, URL, number of requests within 30 seconds, and average response time. The data is updated at 5-second intervals. |
|   | Export | You can export daily, weekly, or scheduled reports for all or specific websites. A report contains the following fields: Trend of Requests, Most Accessed Websites, Most Accessed IP Addresses, Trend of Total Web Attacks, Type-based Attack Distribution, Distribution of Attack IP Addresses in China, Distribution of Attack IP Addresses Worldwide, and Trend of Total Blocked Requests. |
|   | Attack Statistics | You can view attack detection statistics, including top 100 attack sources, the number of times of attacks, and the time when the attacks are launched. |
|   | Traffic Trend Chart | You can view the trends of queries per second (QPS) by website. |
|   | HTTP Flood Protection Logs | You can view HTTP flood protection logs. The logs record request URLs, names of matched rules, and time when the requests match the rules. You can filter logs by specifying one or more conditions, including event generation time and rule name. |

| Detection Logs |   |   |
|---|---|---|
|   | Attack Detection Logs | You can view and filter attack detection logs. In the log list, you can view the information about attack detection logs, including the Processing Result, Attacked Address, Attack Type, Attack IP Address, and Attack Time parameters. You can also view the details of each log. The details include the attack risk level, decoding method, attack payload after decoding, and each field in an HTTP request. If a blocked request is identified as a false positive, you can click Eliminate False Positive to create a whitelist rule. You can filter logs by specifying one or more conditions, including attack types, source IP addresses, and event generation time. You can also select logs to create a download task, and then go to the Log Download Management page to download JSON or CSV logs to your computer. |
|   | Log Download Management | You can manage asynchronous download tasks for attack detection logs. |
|   | System Operations Logs | You can view system operations logs, including usernames, operations, and IP addresses. |
|   | Querying With IP | You can specify an IP address to query the rules that are matched by the IP address, such as the type of rules that are matched (HTTP flood attacks or attack detection logs) and the attack details. |
|   | Access Logs | You can view access logs, including access addresses, source and destination IP addresses, request methods, and response codes. |
|   | HTTP Flood Protection | You can set access frequency control rules for domain names and URLs. This limits the access frequency of IP addresses or sessions that match the rules, or blocks access from these IP addresses or sessions. You can also configure an HTTP flood protection whitelist. Requests from IP addresses or sessions in the whitelist are not matched against HTTP flood protection rules. |
|   | Threat Intelligence | WAF integrates threat intelligence that is collected from the Internet. This helps enterprises monitor suspicious requests from the Internet and develop protection policies to defend against attacks. |
|   | Global Custom Rules | You can view rules added by the global administrator. |

|   | Protection Policies | WAF supports multiple decoding methods, including URL decoding, JSON parsing, Base64 decoding, hexadecimal conversion, backslash unescape, XML parsing, Hypertext Preprocessor (PHP) deserialization, and UTF-7 decoding. WAF supports detection of SQL injections, cross-site scripting (XSS) attacks, intelligence, cross-site request forgery (CSRF), server-side request forgery (SSRF), PHP deserialization, Java deserialization, Active Server Pages (ASP) code injections, file inclusion attacks, file upload attacks, PHP code injections, command injections, web crawlers, and server responses. WAF provides the following built-in protection policies: Default Policy Set Observation Mode Strict Protection Financial Institution Internet Enterprise WAF allows you to configure custom decoding algorithms in the policies, separately enable or disable attack detection modules, and configure the detection granularity. You can specify custom status codes to return for blocked requests. You can enable HTTP response detection and configure the length of a response body in detection rules. You can configure the length of a request body in detection rules. You can enable or disable detection timeout settings. |
|---|---|---|
| Configure Protectio n |   |   |
|   | Custom Rules | You can add, delete, enable, and disable custom rules. You can specify the following actions for custom rules: Allow, Block, Monitor, and Control by Using Detection Module. The Control by Using Detection Module action allows you to enable specific protection modules to implement fine-grained access control. You can configure match conditions in a custom rule based on the following fields or their combinations: URI, GET Parameter, Decoded Path, Host, Full Cookie, POST Parameter, Full Body, HTTP Status Code, Response Content, and User IP. If you set the Match Condition parameter to User IP, you can configure a match condition based on source regions. You can specify attack types and custom status codes for blocked requests. You can also specify a validity period for a custom rule. |
|   | Certificates | You can manage SSL certificates for websites, including uploading certificates and private keys. |
|   | Anti Tamper Rule | The web page tamper-proofing feature is supported. You can configure tamper-proofing rules to prevent specific web pages from being tampered with or accidentally modified. WAF caches static web page resources, such as HTML, SHTML, TXT, JS, CSS, JPG, and PNG files, and directly returns cached pages to prevent tampering. WAF periodically detects web page tampering and generates alerts when tampering is detected. |

|   | Protection Site Management | You can add Internet websites and virtual private cloud (VPC) websites to WAF for protection. WAF supports traffic forwarding over HTTP and HTTPS on non- standard ports to the domain names and IP addresses of origin servers. You can select Forward to Backend Servers, Redirect, or Specify Response Content for WAF to forward back-to-origin requests. If you set the Configure Response Method parameter to Forward to Backend Servers, you can select Weighted Round-robin, Least Connections, or Source IP Address Hash as the load balancing algorithm. You can select Redirect to Specific Instance to allow WAF to forward back-to-origin requests directly to Server Load Balancer (SLB) or Elastic Compute Service (ECS) instances that reside in VPCs. In this case, you do not need to associate public IP addresses with the instances. This prevents attackers from obtaining the actual IP addresses of the instances to bypass WAF. You can configure the health check paths of web servers. You can also configure response codes and response timeout periods. You can enable the recording of website access logs to record request headers, request bodies, response headers, and payloads. WAF provides the following built-in protection policies: Default Policy Set, Observation Mode, Strict Protection, Financial Institution, and Internet Enterprise. WAF supports monitoring of origin servers. If the health check of an origin server fails, WAF prompts the failure. You can configure custom values for the X-Forwarded-For header field in HTTP requests for matching. You can add custom header fields to HTTP responses. |
|---|---|---|
| System Settings | Online Backup | You can back up information such as protected websites and related protection policies, custom rules, and certificates. |
|   | Instance System Settings | You can configure WAF parameters, including Global WAF Protection Engine, Anti Tamper, Upper limit of listening ports, and Maximum Number Of Journal Downloads. |

| System Info | Node Status | Usage: displays the CPU utilization and memory usage of WAF nodes. Network Status: displays the read and write throughput of WAF nodes. Detection Status: displays the queries per second (QPS) and average detection time of WAF nodes. Forwarding Status: displays the number of new connections per second and the average processing latency of WAF nodes. Disk Status: displays the disk usage and total disk size of WAF nodes. Historical Data Query: allows you to query the historical system performance data of WAF nodes, including the CPU utilization, memory usage, disk usage, and historical traffic monitoring data. |
|---|---|---|
|   | System Firmware Information | You can view WAF node names and versions of attack detection engines of the current instance. |

chitecture

## 3 Service architecture

Apsara Stack Web Application Firewall (WAF) receives web access traffic and performs protocol parsing and in-depth decoding on the traffic. Then, WAF calls the semantic analysis and access control engines to analyze traffic and determines whether to allow or block traffic based on the preset policies. Core Components Statistical Website Policy Log Management Management Management Report Core Components Access Control Rule Detection Semantic Analysis Data Collection Layer Traffic Parsing In-depth Decoding Web Application Traffic (HTTP/HTTPS) Traditionally, attacks are identified by matching rules that use regular expressions. However, the rules cannot cover all attack payloads that are based on programming languages. As a result, WAF cannot provide protection as expected. Apsara Stack WAF adopts the intelligent semantic analysis algorithm to analyze web requests and responses to identify threats and attacks. The algorithm processes data through four stages: lexical analysis, syntax analysis, semantic analysis, and threat model matching. Semantic Threat Lexical Syntax A l i A l i A l i Mdl WAF provides built-in syntax compilers for common programming languages. WAF performs in-depth decoding on HTTP and HTTPS payloads, matches the required compiler based on the type of the identified programming language, and then matches the threat model to obtain a threat level. Next, WAF either allows or blocks the related access requests. Threat detection based on intelligent semantic analysis outperforms rule-based threat detection in terms of detection accuracy and false positive rates. scenarios

## 4 Common scenarios

Web Application Firewall (WAF) provides comprehensive web protection for various types of websites, including government, finance, insurance, e-commerce, Online to Offline (O2O), Internet Plus, and gaming websites. Examples: Use WAF to prevent sensitive data leaks and improve data security. For example, you can prevent databases from data download or leaks caused by injection attacks and prevent unauthorized URL access and unauthorized access. For financial customers, use WAF to protect business systems in real time, such as portal websites, online business centers, and online customer service. This helps customers meet the technical evaluation requirements of Multi-Level Protection Scheme (MLPS) 2.0 and regulatory requirements. For e-commerce customers, use WAF to identify web attacks and ensure website availability. Use the HTTP flood protection feature of WAF to protect against abnormal access behavior during major events, such as promotion abuse. During critical periods, use the Strict Protection policy in WAF to enhance system security or create custom rules to proactively defend against zero-day vulnerabilities.
