---
title: "Cloud Security Firewall Product Introduction 20251030"
product_version: "V3.18.6"
pdf_pages: 9
source_pdf: "b4fc0b1a37dd4d32_Alibaba Cloud Apsara Stack V3.18.6 Cloud Security Firewall Product Introduction 20251030.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-%E4%BA%91%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Security%20Firewall%20Product%20Introduction%2020251030.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Cloud Security Firewall Product Introduction 20251030

## Table of Contents

- 1 Features
- 2 Benefits
- 3 Scenarios

## 1 Features

| Function module | Features | Description |
|---|---|---|
| Internet Cloud Firewall (ISW) | Internet access control | Supports Internet firewall, including inbound and outbound access control with parameters such as source, destination type, destination, protocol type, port type, port, application, and action. |
|   | On-demand traffic steering policy | Supports searching target assets by asset type, region, instance ID, and IP address to enable firewall traffic steering policies on demand, including Internet firewall, virtual private cloud (VPC) firewall, and IDC-VPC firewall. |
|   | Intrusion prevention | Supports configurable threat DPI engine operation modes: monitor mode or Block Mode. Supports configuration of bidirectional IP whitelists for both inbound and outbound traffic. Supports custom Basic Policies for intrusion prevention. Supports Virtual Patches feature with one-click enablement. Supports protection against network event types including the following: abnormal connections, command execution, brute-force attacks, scanning, information leakage, DoS attacks, overflow attacks, Web attacks, trojans and backdoors, viruses and trojans, worms, mining behavior, reverse shell, and abnormal links. |
|   | Event logs | Supports searching event logs by source IP address, destination IP address, event type, action taken, and time dimension. |
|   | Traffic logs | Supports searching traffic logs by multiple dimensions. |
|   | VPC-VPC access control | Supports virtual private cloud (VPC) firewalls: detects and controls communication traffic between two VPCs, including source, destination type, protocol type, port type, application, action, and more. |
|   | ECS-ECS access control | Supports internal firewalls: controls inbound and outbound traffic between ECS instances, including source, destination, protocol type, port range, action, and more. |
|   | IDC-VPC access control | Supports IDC-VPC firewall: includes source, destination type, protocol type, port type, application, action, and more. |

|   | On-demand traffic steering policy | Supports searching target assets by asset type, region, instance ID, and IP address to enable firewall traffic steering policies on demand, including Internet firewall, virtual private cloud (VPC) firewall, and IDC-VPC firewall. |
|---|---|---|
| VPC Cloud Firewall (CSW) |   |   |
|   | Intrusion prevention | Supports configurable threat DPI engine operation modes: monitor mode or Block Mode. Supports configuration of bidirectional IP whitelists for both inbound and outbound traffic. Supports custom Basic Policies for intrusion prevention. Supports Virtual Patches feature with one-click enablement. Supports protection against network event types including the following: abnormal connections, command execution, brute-force attacks, scanning, information leakage, DoS attacks, overflow attacks, Web attacks, trojans and backdoors, viruses and trojans, worms, mining behavior, reverse shell, and abnormal links. |
|   | Event logs | Supports searching event logs by source IP address, destination IP address, event type, action taken, and time dimension. |
|   | Traffic logs | Supports searching traffic logs by multiple dimensions. |

## 2 Benefits

Apsara Stack Security is a leading service in the cloud security industry and has received various certifications from relevant authorities. It fully protects the security of the Apsara Stack environment through advanced security systems and technologies.

**Leading service in the cloud security industry**

The Apsara Stack Security team has accumulated extensive security experience by protecting all internal business systems of Alibaba Group since 2005. After Alibaba Cloud Security was released in 2011, the service became an industry leader providing comprehensive protection to ensure cloud security.

**Mature systems and advanced technologies**

Apsara Stack Security is developed based on over ten years of protection experience. Through protecting Alibaba Group's internal business systems for more than a decade, Alibaba Group has obtained numerous security research achievements, security data, and security operations methods, while building a professional cloud security team. Apsara Stack Security leverages this rich experience to help enterprises build sophisticated systems that enhance security for cloud computing platforms. This service protects the cloud platform, cloud network environments, and cloud business systems of Apsara Stack users.

**Comparison with traditional security services**

| Benefit | Traditional security service | Apsara Stack Security |
|---|---|---|
| Comprehensive security capabilities among Internet enterprises | A traditional security service provider offers only limited services and features, and cannot provide a comprehensive security protection system. | Alibaba Group has accumulated extensive intelligence sources based on years of attack prevention experience. As a result, the service can detect common Internet attacks including zero-day exploits, and provide comprehensive security capabilities. |
| Early risk detection | Traditional security services cannot detect risks because they lack experience in monitoring a wide array of services. | Apsara Stack Security can detect and quickly respond to critical vulnerabilities and security events to prevent security issues. |
| Big data modeling and analysis | Traditional security services cannot detect threats by scanning signatures. The traditional log analysis feature can only collect data and report analysis results. You cannot use this feature to perform data modeling or analysis. | Apsara Stack Security implements big data modeling and analysis to detect threats in the entire network and display the security data. More than 30 algorithmic models are used to analyze historical data, network data, and server data. This way, Apsara Stack Security provides additional insights into the security of the system. |

| Scalability and decoupling from hardware | Traditional security services are developed based on existing hardware devices. These security services require virtual hosts that are created on virtualization platforms. | Hardware and software decoupling: All modules are developed based on the cloud computing architecture and the common x86 architecture for hardware. As a result, the modules do not require specific hardware. Scalability: You can scale out hardware devices to increase performance without the need to change the network architecture. |
|---|---|---|
| Comprehensive protection system that supports unified detection and response | Traditional security services add devices to improve security capabilities. The devices can collect only device logs and status data, and display the data on the management platform. You cannot integrate the devices to use additional features. | Apsara Stack Security provides comprehensive Internet protection to ensure the security of networks, servers, applications, data, and user identities. The security modules automatically interact with each other to respond to security issues and share intelligence. |
| Compatibility with all data center environments and decoupling from specific cloud platforms | Most traditional security services are provided as hardware appliances. Due to this reason, the services are incompatible with the cloud platforms that adopt Software Defined Network (SDN) technology. | Based on the interactions between servers and the operating system, Apsara Stack Security performs data analysis to detect threats at the network perimeter. This ensures that Apsara Stack Security is compatible with all data center environments and addresses the complex network topology in data centers. |

## 3 Scenarios

Apsara Stack Security provides flexible and scalable security solutions for users of different scales across various sectors, including industry, agriculture, transportation, public service, finance, and education.

**Apsara Stack for classified protection compliance**

Apsara Stack helps you deploy security modules provided by Apsara Stack Security on your computing platforms to implement in-depth defense. These modules include server security, network security, application security, data security, O&M audit, and centralized management components. This enables real-time detection of security risks on platforms and services. It also helps meet the requirements of Multi-Level Protection Scheme (MLPS) 2.0 level 3 and MLPS 2.0 level 4. Additionally, Apsara Stack provides on-premises security operations and MLPS compliance consultation to help ensure business security and stability while meeting MLPS 2.0 level 3 and MLPS 2.0 level 4 requirements.

**Apsara Stack for public services**

Apsara Stack for public services enables users in the public service sector to build a centralized service platform in the Apsara Stack environment. This allows users to work on intelligent platforms and provide intelligent convenience services to the public. User work efficiency is significantly improved, resulting in better public services. You can deploy Anti- DDoS Service and Web Application Firewall (WAF) on the cloud to establish the first and outermost line of defense, while using Apsara Stack Security to ensure operational security, data security, and O&M security of public service systems. Apsara Stack Security also provides security services to help build organizational structures for security management, improve management policies, and foster security operations awareness.

**Apsara Stack for Finance**

Apsara Stack for finance helps users build an in-depth security protection system. You can deploy Network Detection and Response, Anti-DDoS Service, and Cloud Firewall at the Apsara Stack egress to perform in-depth detection and protection against network layer attacks. You can deploy WAF to filter application layer attacks and install the Server Guard agent on hosts to ensure terminal security. Apsara Stack Security collects network-wide security logs for centralized big data modeling and analysis, eliminating security silos. Users can deploy security protection systems on the cloud based on the x86 architecture, eliminating the need for traditional security hardware.
