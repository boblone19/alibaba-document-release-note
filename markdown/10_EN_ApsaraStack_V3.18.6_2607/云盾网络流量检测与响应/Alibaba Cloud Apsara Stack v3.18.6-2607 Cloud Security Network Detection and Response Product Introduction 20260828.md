---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 18
source_pdf: "9db737535b45d61c_Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Product Introd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E7%9B%BE%E7%BD%91%E7%BB%9C%E6%B5%81%E9%87%8F%E6%A3%80%E6%B5%8B%E4%B8%8E%E5%93%8D%E5%BA%94/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Security%20Network%20Detection%20and%20Response%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Security Network Detection and Response Product Introduction 20260828

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

This topic describes the functions and features of NDR.

| Level-1 feature | Level-2 feature | Level-3 feature | Feature description |
|---|---|---|---|
| Traffic detectio n | Deploy ment Mode | Out-of-band deployment | The network threat detection and response system supports out-of-band deployment. You can perform security analysis on traffic from the cloud network to the Internet (ISW side), from the cloud network to the enterprise intranet (CSW side), and on ECS ENI traffic in the cloud network (VPC traffic mirroring). |
|   | Network perform ance | Throughput and detection performance | A single cluster processes up to 20 Gbit/s of traffic and handles up to 10 Gbit/s of threat detection traffic. |
|   |   | DDoS attack detection | The system detects DoS attacks, including Denial-of- Service Attack behaviors that target services such as Web, MySQL, FTP, Samba, OpenLDAP, and Redis. |
|   |   | SQL injection detection | The system detects SQL injection attacks and protects against common SQL injection attacks and blind SQL injection attacks. |
|   |   | Webshell detection | The system detects Webshell upload attacks and identifies tools such as China Chopper and malicious file uploads. |
|   |   | Ransomware behavior detection | The system detects ransomware behaviors and supports detection of ransomware families such as Buran, Clop, Yatron, Samsam, and Bad Rabbit. |
|   |   | Reverse shell behavior detection | The system detects Reverse Shell behaviors in Linux and Windows operating systems. |
|   |   | Abnormal connection detection | The system detects abnormal connection behaviors such as DNS tunneling and PowerShell-based connections. |
|   |   | Malicious scan detection | The system detects malicious scanning behaviors from scanners such as AWVS, Acunetix, Masscan, Nessus, Nmap, Burp Suite, Zed Attack Proxy, AppScan, WVS, TangScan, and eEye. |
|   |   | Mining behavior detection | The system detects Mining behaviors and identifies host mining software such as DecredMiner and XMRig that consume host resources. |

| Threat detectio n | Threat detectio n |   |   |
|---|---|---|---|
|   |   | Sensitive data leakage detection | The system detects data leakage attacks that target services such as WordPress, Microsoft SharePoint, Oracle Application Server, Apache, WebCMS, Nginx, Oracle DB, MySQL, and Elasticsearch. |
|   |   | Brute-force cracking detection | The system detects brute-force cracking attacks. |
|   |   | Trojan behavior detection | The system detects Trojan behaviors, including communication behaviors of hundreds of Back Door programs such as FireEye, BlackRAT, SoreFang, Azorult, and Rifdoor, as well as Webshell remote control communication behaviors. |
|   |   | Whitelist policy | The system supports configuration and management of threat detection whitelists. Traffic that matches a whitelist entry no longer generates threat detection alerts. |
|   |   | Directory traversal detection | The system detects Web Attack types such as Directory Traversal, path traversal, arbitrary file upload, arbitrary file read, SSRF, and CSRF. |
|   |   | Buffer overflow detection | The system detects common Buffer Overflow attack behaviors. |
|   |   | Network threat response | The system supports asynchronous export of threat detection events and block logs. You can view export tasks in the download task management section, and download the exported content or delete export tasks. |
|   |   | Worm behavior detection | The system detects worm behaviors and prevents worms from downloading, spreading, and communicating across the network. |
|   |   | Cross-site scripting detection | The system detects Cross-Site Scripting (XSS) attack behaviors. |
|   |   | Remote code execution detection | The system detects remote code execution and Remote Command Execution attack behaviors. |
|   |   | Remote code execution vulnerability detection | The system detects remote code execution vulnerability exploitation behaviors that target applications such as Microsoft SharePoint, Dynamics 365, Oracle WebLogic Server, Apache, and CMS. |
|   | t Version: 2 |   |   |

|   |   | Remote file inclusion detection | The system detects remote file inclusion and Local File Inclusion attack behaviors. |
|---|---|---|---|
|   | Block logs | Top block information | The system provides statistics on the top 5 source IP addresses and destination IP addresses in block logs, along with a Trend Chart of alert count changes. |
|   |   | Block logs | Traffic that matches a protection policy generates a block log. You can view the source, destination, attack count, matched policy ID, and matched rule name in the block log, and modify the protection action of the policy. |
| Attacker profile | Attacker profile | Attack process | You can view attack process details and download attack payload and PCAP files. |
|   |   | Attacker behavior | The system provides a unified analysis and display of attacker basic information, threat intelligence, attack techniques, attack targets, and attack processes from the attacker perspective. |
| Log Retrieva l | Log Retrieva l | Search criteria | You can search and query logs by using combined conditions and logical expressions based on time range, organization, and log type. |
|   |   | Log export tasks | The system supports log export task management and allows asynchronous log export. |
|   |   | Log conversion | The system provides a utility to convert log fields in special formats. |
|   |   | Log export fields | You can export all log fields or select specific fields for export, and export log details as PCAP files. |
|   |   | Search templates | You can select the fields to display in logs, add search criteria to any field, and save the search criteria as a Template for subsequent filtering. |
|   |   | Traffic log retrieval | You can view traffic logs and Security Event logs for the past 1 hour, 4 hours, 8 hours, 24 hours, 7 days, or 30 days. |
|   |   | Intrusion detection rules | The system provides more than 4,300 Preset network intrusion attack detection rules and supports configuration management of detection rules. You can enable or disable individual rules and create Custom Rule with attributes such as rule name, rule engine, attack type, severity, CVE, attack application, rule mode, direction, rule content, rule description, and remarks. |

| loud Secur and Respo | ity Network nse |   |   |
|---|---|---|---|
| Policy manage ment | Policy manage ment |   |   |
|   |   | Internal IP Address Pool | The system supports Internal IP address identification and configuration for Network Traffic direction determination. |
|   |   | Address book management | The system supports IP address book management. You can manage IP addresses in batches and reference address books in protection policies. |
|   |   | HTTP Custom Policy | The system supports Application Layer protection policies. You can configure observation and blocking policies based on HTTP packet field content and set the effective time for policies. |
|   |   | Web application detection configuration | The system provides more than 1,200 Preset Web intrusion attack detection rules, including detection of Webshell upload, SQL injection, Cross-Site Scripting (XSS), Code Execution, CRLF, Local File Inclusion, and other attack behaviors. You can manage Web application detection rules and enable or disable them. |
|   |   | Port Scan deception policy | The system supports Port Scan deception policies. You can add IP addresses and ports that require protection to deceive malicious port scanning behaviors. |
|   |   | Network layer policy | The system supports Layer 4 protection policies. You can configure traffic observation and blocking policies based on Source IP addresses, destination IP addresses, and ports. |
| Behavio r analysis | Behavio r analysis | Outbound connection analysis | The system monitors unauthorized or abnormal outbound connections initiated by cloud hosts. It identifies potential risks by using views such as protocol distribution, high- frequency IP addresses, and time trends, and supports Whitelist filtering and log export. |
|   |   | DNS behavior analysis | The system detects DGA domains and DNS Tunnel activities, identifies suspicious DNS requests, and generates alerts. You can export results asynchronously, customize the detection time range, request count, and total domain name length, and view statistics on the number and trends of suspicious domains. |
|   |   | Encrypted traffic analysis | The system detects SSL Encryption traffic characteristics, identifies malware communication behaviors in encrypted traffic, and generates alerts. You can export alert content asynchronously. |

| Network packet capture | Network packet capture | Network packet capture | Users with the Global Organization Security Administrator role can create network packet capture tasks to capture TCP, UDP, and ICMP packets. |
|---|---|---|---|
| Traffic analysis | Internet boundar y | Internet boundary traffic statistics | The system records Inbound and Outbound Network Traffic between the Internet boundary and cloud hosts, including the number of active IP addresses, the number of application types, the average traffic volume, and the peak traffic volume. You can view statistics for the past 1 hour, 24 hours, or 7 days. |
|   |   | Internet boundary traffic ranking | The system ranks active IP addresses at the Internet boundary by Network Traffic volume, number of accessed IP addresses, number of application types, and number of sessions. |
|   |   | Internet boundary access record details | You can view network access record details for each IP address, including the Network Traffic Trend Chart, associated ECS assets, and historical network session records. You can view statistics for the past 1 hour, 24 hours, or 7 days. |
|   |   | One-click blocking at the Internet boundary | You can block suspicious network access behaviors with one click to prevent suspicious IP addresses from sending or receiving network traffic. |
|   | Intranet boundar y | Intranet boundary access record details | You can view network access record details for each IP address, including the Network Traffic Trend Chart, associated ECS assets, and historical network session records. You can view statistics for the past 1 hour, 24 hours, or 7 days. |
|   |   | Intranet boundary traffic statistics | The system records Inbound and Outbound Network Traffic between the IDC network and cloud hosts, including the number of active IP addresses, the number of application types, the average traffic volume, and the peak traffic volume. You can view statistics for the past 1 hour, 24 hours, or 7 days. |
|   |   | Intranet boundary traffic ranking | The system ranks active IP addresses from the IDC network to cloud hosts by Network Traffic volume, number of accessed IP addresses, number of application types, and number of sessions. |

| Traffic trends | Traffic trends | Inbound session traffic trends | The system ranks the top 5 sources of traffic to cloud hosts from the Internet and IDC IP addresses by Network Traffic volume and displays the distribution of application types. You can also view the ranking of cloud hosts by network access traffic volume and view statistics for the past 1 hour, 24 hours, or 7 days. |
|---|---|---|---|
|   |   | Outbound session traffic trends | The system ranks the top 5 destinations of traffic from cloud hosts to external networks by Network Traffic volume and displays the distribution of application types. You can also view the ranking of cloud hosts by outbound network access traffic volume and view statistics for the past 1 hour, 24 hours, or 7 days. |
|   |   | Total traffic trends | The system tracks overall Network Traffic trends. You can view the Network Bandwidth and packet count trends for the past 1 hour, 24 hours, or 7 days. |

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
