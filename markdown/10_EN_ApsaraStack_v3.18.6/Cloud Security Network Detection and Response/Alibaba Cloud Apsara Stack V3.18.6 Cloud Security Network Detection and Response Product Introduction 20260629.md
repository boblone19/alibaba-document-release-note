---
title: "Cloud Security Network Detection and Response Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 18
source_pdf: "9e538a99b81cb453_Alibaba Cloud Apsara Stack V3.18.6 Cloud Security Network Detection and Response Product Introductio"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Security%20Network%20Detection%20and%20Response%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Cloud Security Network Detection and Response Product Introduction 20260629

## Table of Contents

- 1 What is NDR?
- 2 Benefits
- 3 Architecture
- 4 Functions and features
- 5 Use scenarios
- 6 Terms

?

## 1 What is NDR?

Network Detection and Response (NDR) uses a variety of threat detection engines and threat intelligence to detect network attacks at the Internet and internal network perimeters and takes appropriate measures to defend against attacks.

**Overview**

NDR is a service that can analyze big data in real time within microseconds. It is the first line of defense against attacks. NDR performs in-depth packet analysis on mirrored traffic of data centers to detect various attacks and abnormal behaviors in real time. In addition, NDR accurately identifies network threats based on custom thresholds and can work together with other security systems. NDR is dedicated to detecting and responding to attacks in network traffic before, during, and after events. Before events, NDR provides preventive measures such as port antiscanning and threat intelligence. During events, NDR provides detection and blocking capabilities such as intrusion detection system (IDS), web IDS, behavior analysis, and oneclick blocking. After events, NDR provides tracing capabilities such as protocol log collection for all traffic and malicious packet retention. In addition, NDR can be used with Security Orchestration, Automation and Response (SOAR) to perform detection and response orchestration. This implements automated operations on all traffic.

## 2 Benefits

Apsara Stack Security is a leading service in the cloud security industry and has received various certifications from relevant authorities. Apsara Stack Security safeguards Apsara Stack environments with advanced security systems and security technologies.

**Leading service in the cloud security industry**

The Apsara Stack Security team accumulated rich security experience by protecting all internal business systems of Alibaba Group from 2005. After the service was released in 2011, Apsara Stack Security became a leading service that provides comprehensive protection to ensure cloud security. Apsara Stack Security has protected more than 40% of websites in China. It mitigates more than 50% of DDoS attacks and blocks up to 3.6 billion times of attacks every day. It has patched more than 6.13 million vulnerabilities over the previous year.

**Mature systems and advanced technologies**

Apsara Stack Security is developed based on ten years of experience in the cloud security industry. After a decade of experience in providing security services for the internal business systems of Alibaba Group, Alibaba Cloud has obtained considerable security research achievements, security data, and security operations methods, and has built a professional cloud security team. Apsara Stack Security is developed based on the rich experience of the security team to help enterprises build sophisticated systems that can enhance the security of cloud computing platforms. This service can protect the cloud platforms, cloud networks, and cloud business systems of Apsara Stack tenants.

**Comparison with traditional security services**

| Feature | Traditional security service | Apsara Stack Security |
|---|---|---|
| Industry-leading security capabilities that surpass other Internet enterprises | A traditional security service provider only has limited products and features and cannot provide a comprehensive security protection system. | Alibaba Group accumulated a large number of intelligence sources based on years of attack prevention experience. This enables Apsara Stack Security to detect common Internet attacks such as zero- day exploits, and provide comprehensive security capabilities. |
| Prompt risk forecasting | Traditional security services cannot forecast risks because they are not tested in a wide array of security monitoring scenarios. | Apsara Stack Security can detect and quickly respond to critical vulnerabilities and security events to prevent security issues. |

| Big data modeling and analysis | Traditional security services cannot detect threats by verifying their signatures. The traditional log analysis feature can only be used to collect data and generate reports. You cannot use this feature to perform data modeling or analysis. | Apsara Stack Security implements big data modeling and analysis to detect threats in networks and display security data. More than 30 algorithmic models are used to analyze historical data, network data, and server data. This way, Apsara Stack Security provides insights into the security of business systems. |
|---|---|---|
| Scalability and hardware and software decoupling | Traditional security services are developed based on existing hardware devices. These security services require virtual hosts that are created on virtualization platforms. | Hardware and software decoupling: All modules are developed based on the cloud computing architecture and the generalist x86 architecture for hardware. Therefore, the modules do not require specific hardware. Scalability: You can scale out the number of hardware devices to improve performance without the need to change the network architecture. |
| Comprehensive protection system that supports unified detection and emergency response | Traditional security services add devices to enhance security capabilities. The devices can collect only device logs and status data, and display the data on the management platform. The devices cannot collaborate to provide additional features. | Apsara Stack Security provides comprehensive Internet protection to ensure the security of networks, servers, applications, data, and user identities. The security modules automatically interact with each other to respond to security issues and share intelligence. |
| Compatibility with all data center environments and decoupling from specific cloud platforms | Most traditional security services are provided as hardware appliances. Due to this reason, the services are incompatible with the cloud platforms that adopt the Software Defined Network (SDN) technology. | Apsara Stack Security is developed based on interactions between servers and the operating system, and performs data analysis to detect threats at the data ingress and egress of networks. This ensures that Apsara Stack Security is compatible with all data center environments and avoids the complex network topology in data centers. |

## 3 Architecture

NDR detects and analyzes inbound and outbound traffic on a packet-by-packet basis through traffic mirroring.

**Product network architecture**

**Department A**

**Department B**

**Internet**

**Data Center Network**

|   | Traffic Distribution Switch |
|---|---|

NGFW

**Router/vSwitch**

**Traffic security**

NGFW

**Optical splitter**

**ISW-side Cloud Firewall**

Traction

**Anti-DDoS**

|   | Optical splitter |   |
|---|---|---|

**ISW**

**ISW**

**CSW-side Cloud**

Re-

**Firewall**

injection

**DSW**

**DSW**

**CSW**

**CSW**

**LSW**

**LSW**

**ASW**

**ASW**

**ASW**

**ASW**

**ASW**

**ASW**

| XGW | SLB |
|---|---|

**Apsara**

**OPS**

**RDS**

**ECS**

**Data**

**WAF**

**State /SOC**

**Data**

**NCs**

**NCs**

**Encryption**

**Security**

**Stack**

**Service**

**Security -**

**Center**

NDR is deployed in bypass mode, which is transparent to your business systems. NDR requires network devices such as optical splitters and network Test Access Points (TAPs) to mirror traffic over uplink ports of Inter-connection Switches (ISWs), Customer Switches (CSWs), and LVS Switches (LSWs) to the NDR cluster.

**Terms**

| Term | Description |
|---|---|
| NDR | NDR is a service that detects and analyzes network traffic. |
| optical splitter | An optical splitter or an optical fiber splitter is a passive device. Only light beams are input to the device. An optical splitter consists of entrance slits, exit slits, mirrors, and dispersive elements, and is used to separate the required resonance line. The key component of an optical splitter is the dispersive element. Gratings are used as dispersive elements for commercial use. |
| Traffic Distribution Switch | A traffic distribution switch is a network TAP that is used to replicate, aggregate, and filter data. Protocol conversion is performed to convert 10GE POS data into GE LAN data, and the data is sent in load balancing mode based on specific algorithms. This ensures that all data packets from the same session or IP address are sent over the same port. Note NDR has two types of network TAPs: commercial network TAP and network TAP developed by Apsara Stack. The network TAP developed by Apsara Stack is a TSW used to replicate and distribute traffic, but it is unable to filter traffic. Commercial network TAPs are provided by vendors such as Accelink, EmbedWay, and Hengguang. |

| ISW | An Inter-Connect Switch (ISW) provides access to the networks of Internet service providers (ISPs) or the backbone networks of enterprises. |
|---|---|
| DSW | A Distribution Switch (DSW) is a core switch that is used to connect all Access Switches (ASWs). |
| ASW | An Access Switch (ASW) provides access to Elastic Compute Service (ECS) instances and uses an uplink to connect to a DSW. |
| CSW | A Customer Switch (CSW) provides access to your internal backbone networks, including access to virtual private clouds (VPCs) by using leased lines, and performs route distribution and exchange between the internal network and the Internet. A CSW can encapsulate Virtual Extensible LAN (VXLAN) packets sent from leased lines to Extendable Gateways (XGWs). |
| LSW | An Integrated Access Switch (LSW) functions as gateways to provide access to various cloud services, such as VPC and Server Load Balancer (SLB). Each cloud service server, such as the XGW, SLB, or OPS server, is connected to two LSWs. These servers exchange routing information by using Open Shortest Path First (OSPF). The two LSWs exchange routing information with each other by using Internal Border Gateway Protocol (IBGP). The LSWs exchange routing information with DSWs and CSWs by using External Border Gateway Protocol (eBGP). |

## 4 Functions and features

This topic describes the features of Network Detection and Response (NDR).

| Level-1 feature | Level-2 feature | Level-3 feature | Description |
|---|---|---|---|
| Traffic detectio n | Deploy ment mode | Bypass mode | The network threat detection and response system can be deployed in bypass mode to analyze data transfer from cloud networks to the Internet on the Inter-connection Switch (ISW) side, from cloud networks to enterprise internal networks on the Customer Switch (CSW) side, and on Elastic Network Interfaces (ENIs) of Elastic Compute Service (ECS) instances (mirrored VPC traffic). |
|   | Network perform ance | Throughput and detection capacity | It can process traffic of up to 20 GB for a single cluster and process traffic of up to 10 GB for threat detection. |
|   |   | DDoS attack detection | DoS attacks that target web, MySQL, FTP, Samba, OpenLDAP, and Redis services. |
|   |   | SQL injection detection | Detects SQL injection attacks to protect business systems against common SQL injection attacks, including blind SQL injection. |
|   |   | Webshell detection | Detects webshell attacks, such as attacks from China Chopper and malicious file uploads. |
|   |   | Ransomware detection | Detects ransomware such as Buran, Clop, Yatron, SamSam, and Bad Rabbit. |
|   |   | Reverse shell detection | Detects reverse shells that may exist in Linux and Windows. |
|   |   | Abnormal connection detection | Detects abnormal connections established by using DNS tunneling or PowerShell. |
|   |   | Scan attack detection | Detects scan attacks launched by using scanners such as Acunetix Web Vulnerability Scanner (AWVS), Masscan, Nessus, Nmap, Burp Suite, Zed Attack, AppScan, Web Vulnerability Scanner (WVS), TangScan, and eEye. |
|   |   | Mining detection | Detects malicious mining behavior performed on hosts by miners such as XMRig and Decred Miner. |

| Threat detectio n | Threat detectio n |   |   |
|---|---|---|---|
|   |   | Sensitive data leakage detection | Detects leakage of data in services, such as WordPress, Microsoft SharePoint, Oracle Application Server, Apache, Web-CMS, NGINX, Oracle databases, MySQL, and Elasticsearch. |
|   |   | Brute-force attack detection | Detects brute-force attacks. |
|   |   | Trojan detection | Detects more than 100 types of trojans, such as FireEye, BlackRAT, SoreFang, AZORult, and Rifdoor, and remote access and control by using a webshell. |
|   |   | Whitelist policy | Allows you to configure and manage a whitelist for threat detection. No thread detection alerts are generated for attacks that hit the whitelist. |
|   |   | Directory traversal detection | Detests web attacks, such as directory traversal attacks, path traversal attacks, arbitrary file upload attacks, server- side request forgery (SSRF) attacks, and cross-site request forgery (CSRF) attacks. |
|   |   | Buffer overflow detection | Detects common buffer overflow attacks. |
|   |   | Network threat handling | Supports asynchronous export of threat detection events and logs of blocked traffic. Displays export tasks on the download task management page. Allows you to download exported events and logs and delete export tasks. |
|   |   | Worm detection | Detects worm attacks to prevent downloading and spreading of worms in communication networks. |
|   |   | Cross-site scripting detection | Detects cross-site scripting attacks. |
|   |   | Remote code execution detection | Detects remote code execution attacks and remote command execution attacks. |
|   |   | Remote code execution vulnerability detection | Detects remote code execution attacks launched by exploiting vulnerabilities in Microsoft SharePoint, Microsoft Dynamics 365, Oracle WebLogic Server, Apache, and Content Management System (CMS) applications. |
|   | t Version: 2 |   |   |

|   |   | Remote file inclusion detection | Detects remote file inclusion (RFI) and local file inclusion (LFI) attacks. |
|---|---|---|---|
|   | Logs of blocked traffic | Top rankings | Displays the top five source IP addresses and top five destination IP addresses of attacks in the logs of blocked traffic, and changes in the number of alerts over time. |
|   |   | Logs of blocked traffic | Generates logs for traffic that hits protection rules. The logs record the source and destination IP addresses of the traffic, the number of times of attacks, the ID of the protection policy, and the name of the matching protection rule. Allows you to modify the actions specified in a protection rule. |
| Attacker profiles | Attacker profiles | Attack process | Allows you to view the details of the attack process and download the payload and PCAP files that contain the attack details. |
|   |   | Attacker behavior | Analyzes and displays the basic information, threat intelligence, attack methods, targets, and attack processes. |
| Log search | Log search | Search conditions | Allows you to search log content by using a combination of time range, organization, and log type or entering a logical expression. |
|   |   | Log export tasks | Allows you to manage log export tasks and asynchronously export logs. |
|   |   | Log conversion | Provides tools to help you convert log fields in specific formats. |
|   |   | Log field export | Allows you to export all log fields or only the specified fields. You can also export log details to PCAP files. |
|   |   | Search template | Allows you to select the fields to display in logs, add field search conditions, and save search conditions as a template, which improves the efficiency of log search. |
|   |   | Traffic log search | Allows users to view traffic logs and logs of security events generated within the previous 1 hour, 4 hours, 8 hours, 24 hours, 7 days, and 30 days. |

| Policy manage ment | Policy manage ment | Intrusion detection rules | Provides more than 4,300 predefined network intrusion detection rules, and allows you to enable or disable specific detection rules. You can also create custom detection rules by configuring the rule name, engine, attack type, severity level, CVE, target application, rule mode, direction, rule content, rule description, and remarks. |
|---|---|---|---|
|   |   | IP address pool for internal assets | Identifies IP addresses used by internal assets in order to determine the direction of network traffic. |
|   |   | Address book management | Supports IP address book management. You can manage multiple IP addresses at a time and reference address books in protection policies. |
|   |   | HTTP custom policies | Supports application layer protection policies. You can configure monitoring and block rules based on the fields of HTTP requests and set the validity period of protection policies. |
|   |   | Web application detection configuration | Provides more than 1,200 predefined rules for detecting various types of web attacks, such as webshell uploads, SQL injection, XSS, code execution, carriage return line feed (CRLF) injection, and LFI. Allows you to configure, enable, and disable web attack detection rules. |
|   |   | Spoofing rules for port scanning | Allows you to configure spoofing rules for port scanning. You can add IP addresses and ports that you want to protect in a spoofing rule to decoy attackers. |
|   |   | Network layer policies | Supports Layer 4 protection policies. You can configure traffic monitoring and block rules based on source IP addresses, destination IP addresses, and ports. |
| Behavio r analysis | Behavio r analysis | DNS behavior analysis | Detects domain names that are generated by using domain generation algorithms (DGAs) and domain names that are used to launch DNS tunneling attacks, triggers alerts for abnormal DNS requests, and allows you to asynchronously export the corresponding information. You can specify the time range, the number of requests, and the total length of a domain name. You can collect statistics on the number and trend of domain names. |
|   |   | Encrypted traffic analysis | Identifies SSL-encrypted traffic based on the signatures of packets, detects malware communication, and then generates alerts. You can asynchronously export the corresponding information. |
| Packet capture | Packet capture | Packet capture | Allows users that assume the global organization security administrator role to create packet capture tasks to capture TCP, UDP, and ICMP packets. |

| Traffic analysis | Internet border | Internet border traffic statistics | Collects statistics about inbound and outbound traffic from the Internet border to ECS instances within the previous 1 hour, 24 hours, and 7 days, including the number of inbound and outbound active IP addresses, number of application types, average traffic volume, and peak traffic volume. |
|---|---|---|---|
|   |   | Internet border traffic sorting | Allows you to sort active IP addresses that have accessed the Internet border by traffic volume, number of IP addresses, number of application types, and number of sessions. |
|   |   | Internet border access details | Allows you to view the network access details of each IP address, network traffic trends of different IP addresses, associated ECS instances, and historical network sessions. You can view the statistics generated within the previous 1 hour, 24 hours, and 7 days. |
|   |   | Blocking of access to the Internet border | Allows you to block suspicious network access with a few clicks by restricting requests that are sent from or to suspicious IP addresses. |
|   | Internal network border | Internal network border access details | Allows you to view the network access details of each IP address, network traffic trends of different IP addresses, associated ECS instances, and historical network sessions. You can view the statistics generated within the previous 1 hour, 24 hours, and 7 days. |
|   |   | Internal network border traffic statistics | Collects statistics about inbound and outbound traffic sent from the networks of data centers to ECS instances within the previous 1 hour, 24 hours, and 7 days, including the number of inbound and outbound active IP addresses, number of application types, average traffic volume, and peak traffic volume. |
|   |   | Internal network border traffic sorting | Allows you to sort active IP addresses that have accessed ECS instances from data centers by traffic volume, number of IP addresses, number of application types, and number of sessions. |
| Traffic trends | Traffic trends | Inbound session traffic trends | Displays the top five IP addresses with the highest volume of traffic that flows from the Internet or data centers to ECS instances and the distribution of application types. Displays the ranking of ECS instances based on the volume of traffic that flows to them. You can view the statistics generated within the previous 1 hour, 24 hours, and 7 days. |

|   |   | Outbound session traffic trends | Displays the top five IP addresses with the highest volume of traffic that flows from ECS instances to external networks and the distribution of application types. Displays the ranking of ECS instances based on the volume of traffic that flows from them to external networks. You can view the statistics generated within the previous 1 hour, 24 hours, and 7 days. |
|---|---|---|---|
|   |   | Total traffic trends | Displays the trend of total traffic. You can view the trend of network bandwidth and the trend of network packets within the previous 1 hour, 24 hours, and 7 days. |

os

## 5 Use scenarios

Network Detection and Response (NDR) provides flexible and scalable network security solutions for users of different scales and from various sectors, such as industry, agriculture, transportation, public service, finance, and education.

**Apsara Stack for public services**

Apsara Stack for public services allows users from the public service sector to build a centralized service platform for public services in the Apsara Stack environment. This way, the users can work on intelligent platforms and provide intelligent services for the public. The work efficiency of the users is greatly improved, and the public receives better services. Users can deploy Anti-DDoS and Web Application Firewall (WAF) in the cloud to establish the first and outermost-level line of defense, and use Apsara Stack Security to ensure the operational security, data security, and O&M security of public service systems. Apsara Stack Security can also provide security services to help build an organizational structure for security management, optimize management policies, and foster an awareness of security operations.

**Apsara Stack for finance**

Apsara Stack for finance can help users build an in-depth security protection system. Users can deploy NDR, Anti-DDoS, and Cloud Firewall at the data egress of Apsara Stack to perform in-depth detection and protection against attacks at the network layer, deploy WAF to filter out malicious traffic at the application layer, and deploy the Server Guard agent on hosts to ensure terminal security. Apsara Stack Security collects network-wide security logs to perform centralized big data modeling and analysis and eliminate security silos. Users can deploy security protection systems in the cloud based on the x86 architecture, eliminating the need for traditional security hardware.

## 6 Terms

This topic describes terms related to Network Detection and Response (NDR).

**optical splitter**

An optical splitter or an optical fiber splitter is a passive device. Only light beams are input to the device. An optical splitter consists of entrance slits, exit slits, mirrors, and dispersive elements, and is used to separate the required resonance line. The key component of an optical splitter is the dispersive element. Gratings are used as dispersive elements for commercial use.

**traffic distribution switch**

A traffic distribution switch is a network TAP that is used to replicate, aggregate, and filter data. Protocol conversion is performed to convert 10GE POS data into GE LAN data, and the data is sent in load balancing mode based on specific algorithms. This ensures that all data packets from the same session or IP address are sent over the same port.

**IDS detection**

An Intrusion Detection System (IDS) is a network security device used to monitor network transmission in real time. When anomalies are detected, the system triggers alerts or proactively takes security measures.

**web IDS**

Web IDS is a subset of intrusion detection systems, specifically designed for detecting intrusions targeting web applications, such as SQL injection and cross-site scripting (XSS) attacks.

**DDoS attack**

An attacker combines multiple computers by using the client-server model to form an attack platform and initiates a large number of valid requests to one or more targets from this platform to cause network failures. DDoS attacks are much stronger than common denial of service (DoS) attacks.

**SQL injection**

An attacker makes the server run malicious SQL commands by inserting these commands in web tables or by inserting malicious strings in URL requests.

**traffic scrubbing**

The traffic scrubbing service monitors the inbound traffic of a data center in real time to identify unusual traffic that may be from DDoS attacks and other attacks. This service scrubs the unusual traffic without affecting businesses.

**brute-force attack**

Brute-force attacks work by iterating through all possible combinations that can make up a password.

**webshell**

A webshell is a script written in languages such as Active Server Pages (ASP) and Hypertext Preprocessor (PHP). Attackers can run a webshell on a web server to perform high-risk operations. This enables attackers to obtain sensitive information or control the server through server penetration or privilege escalation.

**SOAR**

Security Orchestration, Automation and Response (SOAR) is a security management service provided by Apsara Stack Security. You can use SOAR to automate and process security event operations to improve security response efficiency.

**ISW**

An Inter-Connect Switch (ISW) provides access to the networks of Internet service providers (ISPs) or the backbone networks of enterprises.

**DSW**

A Distribution Switch (DSW) is a core switch that is used to connect all Access Switches (ASWs).

**ASW**

An Access Switch (ASW) provides access to Elastic Compute Service (ECS) instances and uses an uplink to connect to a DSW.

**CSW**

A Customer Switch (CSW) provides access to your internal backbone networks, including access to virtual private clouds (VPCs) by using leased lines, and performs route distribution and exchange between the internal network and the Internet. A CSW can encapsulate Virtual Extensible LAN (VXLAN) packets sent from leased lines to Extendable Gateways (XGWs).

**LSW**

An Integrated Access Switch (LSW) functions as gateways to provide access to various cloud services, such as VPC and Server Load Balancer (SLB). Each cloud service server, such as the XGW, SLB, or OPS server, is connected to two LSWs. These servers exchange routing information by using Open Shortest Path First (OSPF). The two LSWs exchange routing information with each other by using Internal Border Gateway Protocol (IBGP). The LSWs exchange routing information with DSWs and CSWs by using External Border Gateway Protocol (EBGP).
