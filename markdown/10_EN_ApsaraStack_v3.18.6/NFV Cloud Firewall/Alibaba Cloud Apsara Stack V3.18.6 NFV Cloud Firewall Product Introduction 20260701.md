---
title: "NFV Cloud Firewall Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 14
source_pdf: "12e9a0cb843cdcda_Alibaba Cloud Apsara Stack V3.18.6 NFV Cloud Firewall Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-NFV%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20NFV%20Cloud%20Firewall%20Product%20Introduction%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# NFV Cloud Firewall Product Introduction 20260701

## Table of Contents

- 1 What is NFV Cloud Firewall?
- 2 Benefits
- 3 Service architecture
- 4 Functions and features
- 5 Scenarios

Firewall?

## 1 What is NFV Cloud Firewall?

**Firewall?**

**Introduction to NFV Cloud Firewall**

NFV Cloud Firewall is a cloud computing service developed based on the network functions virtualization (NFV) technology to protect assets in virtual network environments in the cloud. NFV Cloud Firewall is embedded with a stable operating system (OS) that is exclusively defined for network firewalls. NFV Cloud Firewall is typically implemented as software and directly deployed on a cloud platform. It provides end-to-end threat defense capabilities from Layer 2 to Layer 7 and integrates various security features such as firewalls, Network Address Translation (NAT), quality of service (QoS), fine-grained access control for applications, intrusion prevention, antivirus, attack protection, URL filtering, and data protection. These features help you address various security challenges in a cloud environment and ensure the network security of cloud platforms, applications, data, and users.

**Values**

More and more enterprises migrate their businesses to the cloud as digital transformation develops. However, the migration of businesses to the cloud also brings security threats to the cloud. While users enjoy the convenience brought by cloud resources, the security of business assets in the cloud may face more severe challenges than traditional environments. NFV Cloud Firewall provides all-in-one security features to comprehensively protect your business assets in the cloud from Layer 2 to Layer 7.

| Compared with traditional hardware firewalls, NFV Cloud Firewall is designed for cloud |   |
|---|---|
| environments. It can be fully integrated with cloud platforms to maximize the advantages of |   |
| cloud-native technologies, such as rapid deployment, flexible scaling, and rapid migration. |   |
| Such advantages help you better align business scenarios with business development, and |   |
| build a green, secure cloud computing environment that provides power services. |   |

## 2 Benefits

**Fully adaptable software firewall**

In a cloud computing environment, computing, storage, and data resources run on virtual machines on servers. NFV Cloud Firewall supports both high security and quick and ﬂexible deployment on virtual machines. This provides powerful perimeter protection capabilities for virtual networks and applications. Virtual ﬁrewalls (vFWs) of NFV Cloud Firewall are deployed as virtual machines (VMs) to overcome the limitations of physical ﬁrewalls. In addition, vFWs can be deployed closer to VMs in a cloud computing environment to enable security protection for east-west traffic.

**Professional next-generation firewall features**

NFV Cloud Firewall provides a wide array of network security features to defend against network attacks. It helps enterprises enhance network security for branch oﬃces and network isolation in multi-tenant cloud environments. NFV Cloud Firewall provides ﬁne-grained application control, multi-dimensional application risk analysis and ﬁltering, and ﬂexible access control, including policy-based blocking, session throttling, application traﬃc redirection, and intelligent traﬃc management. NFV Cloud Firewall also supports intrusion prevention, virus ﬁltering, attack protection, network address translation (NAT), and other features to protect your businesses against network attacks, identify applications, and enhance access control. In addition, NFV Cloud Firewall supports high availability (HA) networking. You can conﬁgure and throttle sessions to implement redundant deployment that supports high reliability and business continuity.

**Cloud-native features adapted to cloud computing**

In a cloud computing environment, the cloud platform provides a variety of technical solutions to improve the stability, scalability, and performance of the system. These technical solutions are closely related to the cloud computing environment and show strong cloudnative characteristics. Adopting these technical solutions to solve speciﬁc problems makes NFV Cloud Firewall more adaptable to the cloud environment. NFV Cloud Firewall is deeply integrated with the cloud computing platform. The cloud platform monitors the status of devices. When the performance is insuﬃcient, virtual devices or resources are automatically scaled out to ensure system performance for your business.

## 3 Service architecture

NFV Cloud Firewall is deployed in primary and secondary clusters, and uses high availability (HA) heartbeat detection and a quick failover mechanism to ensure business continuity and fault recovery.

**How it works**

| NFV Cloud Firewall is deployed in a network-enhanced exclusive Elastic Compute Service |   |   |
|---|---|---|
| (ECS) cluster in active-standby mode, and supports the native traffic redirection technology of |   |   |
| Alibaba Cloud. To enable traffic redirection, deploy an endpoint interface in the virtual private |   |   |
| cloud (VPC) that requires NFV Cloud Firewall protection. After you configure a redirection |   |   |
| policy for the VPC, a traffic redirection route is automatically generated in the VPC to forward |   |   |
| traffic to NFV Cloud Firewall for scrubbing. You can redirect traffic between VPCs or between a |   |   |
| VPC and a data center to NFV Cloud Firewall for protection. |   |   |

**Single-zone HA architecture**

**Single-zone**

**HA Architecture**

**VPC N**

**VPC 2**

**VPC 1**

10.16.68.0/24 10.16.64.0/24

**......**

ONSPe-2 ONSPe-N ONSPe-1

**·**

**·**

**Bond ENI**

**VLAN 2**

**VLAN 1**

**VLAN N**

**ECMP**

**ECMP**

**Relay**

**Network**

**·**

**Element**

**·**

**Slave ENI**

**Slave ENI**

**VPC**

**·**

**Member ENI**

**·**

Eth0.1 Eth0.2 Eth0.n

**HA**

**Trunk ENI**

**Trunk ENI**

**·**

**vFW supports the**

**A/S cluster type**

**ENI-Business Port**

**ENI-Business Port**

**VFW01 (M)**

**vFW01 (S)**

**·**

vport-1 vport-2 vport-3

**InspectionAVS**

vport-1 vport-2 vport-3

**InspectionAVS**

**ARP**

**ARP**

**NC01**

**NC02**

**AZ**

**HA for deployment in an exclusive cluster (single zone)**

High performance: NFV Cloud Firewall is deployed in a network-enhanced exclusive ECS cluster. The CPU thread cores are exclusive to NFV Cloud Firewall. This ensures stable and predictable computing performance and processing capability of NFV Cloud Firewall. High reliability: The primary and secondary devices in the virtual ﬁrewalls (vFWs) of NFV Cloud Firewall are respectively deployed in two diﬀerent network-enhanced clusters. If a physical server fails, traﬃc is switched to the other server based on the HA mechanism of NFV Cloud Firewall to ensure service continuity.

**Optimal protection path in the cloud-based on vFWs**

Optimal protection path for traﬃc within the cloud: Based on the NFV Cloud Firewall protection solution, the protected east-west direction of VPCs remains within the cloud. All data is forwarded through cloud networks. This cloud-native security protection model provides the most efficient and secure traffic protection path.

**HA of the NFV Cloud Firewall cluster**

HA of the NFV Cloud Firewall cluster based on primary/secondary deployment NFV Cloud Firewall supports HA heartbeat probes. You can configure two devices in the NFV Cloud Firewall cluster to implement HA. Only one device functions as the primary device in the NFV Cloud Firewall cluster. When the primary device is active, it forwards packets while passing all its network and configuration information and current session information to the secondary device. If the primary device fails, the secondary device takes over to forward packets. NFV cluster heartbeat probe mechanism (split-brain prevention) Within the same cluster, NFV Cloud Firewall sends heartbeat packets over the heartbeat connection. You can configure a heartbeat packet interval and alert threshold to detect the status between NFV Cloud Firewall clusters. The default interval is 0.5 seconds. If an NFV Cloud Firewall cluster fails three consecutive heartbeat probes, the NFV Cloud Firewall cluster is declared unhealthy. In this case, the healthy NFV Cloud Firewall cluster proactively takes over network traffic.

**Failover based on Express Connect**

If all NFV Cloud Firewall clusters fail, you can use **Express Connect** to implement quick service failover by bypassing the NFV Cloud Firewall clusters. This mechanism ensures quick service recovery.

**Terms**

| Term | Description |
|---|---|
| Trunking | The network interface controller (NIC) relay mode, which aggregates multiple ENIs into a single trunk NIC to enhance the instance-side network connectivity and increase the ENI density per instance. |
| Trunk ENI | In relay mode, the NIC responsible for aggregation is exposed as a NIC device within the guest OS, and all member ENIs are aggregated into the trunk ENI. |
| Member ENI | In relay mode, the NIC exposed to the user data plane functions as a VLAN sub-interface within the guest OS, and all member ENIs are aggregated into the trunk ENI. |
| Bond ENI | After multiple physical ENIs from different ECS instances are aggregated into a single logical ENI that is externally exposed, the ENI is called a bond ENI. A bond ENI supports Equal Cost Multi-Path (ECMP) and health checks, which are not supported by regular ENIs. |

| Slave ENI | The multiple physical ENIs are called slave ENIs, which are similar to bond and slave interfaces in network terminology. A slave ENI can be trunked to a trunk ENI. |
|---|---|

**Cross-zone High-availability architecture**

**Cross-zone HA Architecture**

| vSwitch1: 10.16.64.0/25 ECS1 ONSPe-1 HA VFW01 VFW01' (M) (S) NC01 NC02 ONSPe-2 ECS2 vSwitch2: 10.16.68.0/25 AZ1 |   | 24 vSwitch1: 10.16. ECS3 ONSPe-1 t VPC HA VFW02 VFW02' (M) (S) NC03 NC04 24 ONSPe-2 ECS4 vSwitch2: 10.16 AZ |   |   |   |
|---|---|---|---|---|---|
|   | VPC 1: 10.16.64.0/ VPC1 route table vSwitch2: 10.16.68.0/26→ONSPe-1 vSwitch2: 10.16.68.64/26→ONSPe-1 vSwitch2: 10.16.68.0/25→ONSPe-1 | 24 vSwitch1: 10 ECS3 ONSPe-1 |   |   |   |
|   | Network Elemen | t VPC HA VFW02 VFW02' (M) (S) |   |   |   |
|   |   |   |   | NC03 | NC04 |
|   | VPC2: 10.16.68.0/ VPC1 route table vSwitch1: 10.16.64.0/26→ONSPe-2 vSwitch1: 10.16.64.64/26→ONSPe-2 | 24 ONSPe-2 ECS4 vSwitch2: 10 |   |   |   |
|   | vSwitch1: 10.16.64.0/25→ONSPe-2 |   |   |   |   |

|   | VFW01' (S) |
|---|---|

| VFW02 (M) |   | VFW02' (S) |
|---|---|---|

| NC01 | NC02 |
|---|---|

Business Traffic Fault Isolation Cross-zone Fault isolation

**HA for deployment in an exclusive cluster (across zones)**

The cross-zone HA architecture is the same as that of the single-zone HA architecture. The cross-zone HA architecture is mainly used to ensure failover between the primary and secondary NFV Cloud Firewall clusters. In this architecture, if the NFV Cloud Firewall cluster or NC cluster fails, east-west traffic across VPCs is redirected to the NFV Cloud Firewall cluster in the other zone based on the configured routes. This mechanism enhances security for multi-zone deployment and enables HA between clusters.

## 4 Functions and features

This topic describes the functions and features of NFV Cloud Firewall.

**Fully parallel, high performance security OS**

NFV Cloud Firewall adopts a multi-CPU and multi-core processing architecture to maximize the capacity of CPUs and cores. The dedicated algorithm developed for NFV Cloud Firewall can implement all security features on each CPU and evenly divide the session load to all cores, which maximizes the parallel processing capacity of the cores and enables parallel detection that requires packet parsing only once. After a packet is parsed, each security module detects the packet in parallel. This feature eﬀectively ensures comprehensive security performance when multiple threat protection features are enabled. NFV Cloud Firewall can maintain fast, eﬃcient, and stable operation even when all security features are enabled at the application layer. NFV Cloud Firewall provides you with industry-leading security performance, which advances in various aspects, such as high throughput, low latency, and high concurrency.

**Various policy tuning methods**

NFV Cloud Firewall provides a wide array of security policy tuning methods, including policy redundancy detection, policy hit analysis, and policy auditing. Policy redundancy detection can quickly check the relationship between security policies in a virtual ﬁrewall (vFW) cluster for redundancy. By working with the policy hit analysis feature, the system can identify frequently used policies and idle policies. The two features can be used together to ﬂexibly aggregate or delete redundant policies. You can combine policy redundancy detection with policy auditing to manage the lifecycle of policies in a ﬁne-grained manner. When temporary policies are configured or modified, the change time and changes are recorded. Then, you can select any two versions in the policy lifecycle to compare the conﬁgurations. By working with policy hit analysis, the system can easily identify frequently used historical policies. You can combine the advantages of these features to quickly sort out your policies even in a complex network topology.

**Fine-grained, multi-dimensional application management**

Security protection is implemented based on the comprehensive awareness of the network and business environment. NFV Cloud Firewall uses in-depth network traﬃc detection and analysis technologies to accurately identify applications, users, content, and geographic locations in multiple dimensions, which provides you with advanced and ﬂexible security control features. NFV Cloud Firewall also supports network visualization and provides various security services, such as access control based on user protocols and application protocols, URL filtering, application bandwidth management, and intelligent link load balancing.
**Accurate application identification and flexible application control** : NFV Cloud
Firewall supports in-depth application identification, which can accurately identify thousands of network applications based on protocol characteristics, behavior characteristics, and association analysis, including more than 600 types of mobile applications and more than 300 types of cloud applications. NFV Cloud Firewall provides you with multi-dimensional visualization information, including application categories, application risk levels, application technologies, and application feature distribution to help you detect application security risks at the earliest opportunity. In addition, NFV Cloud Firewall supports flexible and easy-to-use application security control, including policybased control, session throttling, traffic control, application traffic redirection, and time limiting.
**Access control based on geographic locations**: NFV Cloud Firewall can accurately
identify the geographic locations of attack source and destination IP addresses. This allows you to implement location-based access control to efficiently block attacks and ensure communication security.
**Data transmission security**: Based on in-depth data inspection technologies, NFV Cloud
Firewall controls the transmission of data and files from multiple dimensions, such as data type, protocol type, file name, file size, and keyword. This prevents critical, sensitive, and confidential data and files from being leaked to the Internet and meets the data transmission security requirements of enterprises.
**Internet access control**: NFV Cloud Firewall supports the URL filtering feature, which can
effectively control visits to your website and prevent business risks caused by visits to malicious websites. URL filtering helps you control and block access to web pages based on multiple dimensions, such as a single URL, URL category, and URL keyword category. It also provides built-in URL categories and URL keyword categories. You can also customize URL categories or URL keyword categories to meet different URL filtering requirements.
**File transfer control**: NFV Cloud Firewall supports in-depth file inspection based on file
types, file sizes, and file names to control and secure file transfer for enterprises. In addition, you can also specify keywords and page types to effectively control outbound data transmission. This prevents employees from posting inappropriate comments on the Internet that can damage your brand image.

**ALG technology**

| NFV Cloud Firewall supports multi-protocol application layer gateway (ALG) capabilities, |   |
|---|---|
| including FTP, HTTP, MS RPC, PPTP, Q.931, RAS, RSH, RTSP, SIP, TFTP, DNS, XDMCP, and |   |
| _ H.323. Based on strict security policies, the ALG technology is used to ensure business |   |
| communication of multi-channel applications and monitor and filter traffic based on security |   |
| policies. |   |

**End-to-end threat detection and security protection**

NFV Cloud Firewall implements defense capabilities based on in-depth application detection, protocol detection, and attack principle analysis. It can eﬀectively detect and ﬁlter out attacks such as HTTP ﬂood attacks, DoS attacks, Trojans, worms, vulnerabilities, and escapes. Such capabilities provide you with end-to-end protection from Layer 2 to Layer 7. NFV Cloud Firewall provides the following key features:
**Network layer protection**: NFV Cloud Firewall provides protection against common
mainstream network attacks, including various flood attacks, such as SYN flood attacks, ICMP flood attacks, UDP flood attacks, and DNS query flood attacks. NFV Cloud Firewall also provides protection against various scanning or spoofing attacks, such as IP address spoofing, address resolution protocol (ARP) spoofing, IP address scanning, and port scanning. In addition, NFV Cloud Firewall provides protection against various malformed packet attacks, such as Ping of Death (PoD) attacks, Teardrop attacks, IP fragmentation, abuse of IP options, abuse of TCP options, Lang attacks, and ICMP flood attacks. DDoS attacks such as Smurf and Fraggle attacks can also be mitigated.
**Application layer protection**: NFV Cloud Firewall provides protection against complex
application attacks based on in-depth application identification. It supports protection against attacks of common applications and protocols, such as HTTP, FTP, SMTP, IMAP, POP3, TELNET, TCP, UDP, DNS, RPC, FINGER, MSSQL, ORACLE, NNTP, DHCP, LDAP, VOIP, NETBIOS, and TFTP. NFV Cloud Firewall regularly updates the attack signature library. Security experts actively respond to new attacks and vulnerabilities.
**Antivirus**: NFV Cloud Firewall provides quick, high-performance, and low-latency virus
filtering. After you enable the antivirus feature, NFV Cloud Firewall can detect various viruses, such as worms, Trojans, malware, and malicious websites, and handle the detected viruses based on configurations. The antivirus feature can scan viruses of the following protocols: FTP, HTTP, SMTP, SMB, POP3, IMAP4, and SMB. The types of files that can be scanned include archive files, compressed files of the GZIP, BZIP2, TAR, ZIP, and RAR formats, PE files, HTML files, MAIL files, RIFF files, ELF files, PDF files, Microsoft Office files, and RAW files. You can also select the Others option to perform scanning on files other than the preceding file types, such as GIF, BMP, PNG, JPEG, FWS, CWS, RTF, MPEG, OGG, MP3, WMA, WMV, ASF, and RM files.
**Perimeter traffic filtering**: NFV Cloud Firewall filters traffic based on the IP whitelist and
blacklist, and blocks requests that match the IP blacklist to filter out requests from malicious IP addresses. You can manually add or import IP addresses to the IP blacklist, or configure the system to automatically update the IP blacklist based on the FTP or TFTP server.
**Web protection**: This feature provides protection against web attacks. It can effectively
identify and defend against web threats, such as SQL injection, cross-site scripting (XSS), HTTP flood, sensitive directory scan, external links, hotlink, and iframe issues.

**iQoS**

The intelligent quality of service (iQoS) feature enhanced by NFV Cloud Firewall is based on application identification and user identification, and implements traffic control based on applications and users through fine-grained traffic classification and two-layer eight-level QoS pipeline nesting technology. This feature can control traffic from different dimensions, such as IP address and application. Two-layer traffic control allows you to control both users and applications. It supports traffic control based on the enterprise organizational structure and easy-to-configure traffic control policies for fine-grained traffic classification and control. You can use this feature to effectively protect key services, improve network bandwidth utilization, reduce bandwidth costs, and improve user experience. iQoS provides the following key capabilities:
**Two-layer, eight-level traffic control**: The iQoS technology of NFV Cloud Firewall
supports traffic control at two layers. Each layer of traffic control supports four levels of nesting. This enables two layers and eight levels of flexible network application control.
**Fine-grained traffic classification**: The iQoS technology of NFV Cloud Firewall supports
fine-grained traffic classification and control based on pipelines. All traffic that goes through your device must enter the pipeline based on the preset match conditions. You can specify one or more match conditions in a QoS rule to classify network traffic, such as the source security zone, source interface, source address entry, destination security zone, destination interface, destination address entry, service, service group, application, and application group.
**Differentiated services code point (DSCP)** : The iQoS technology enhanced by NFV
Cloud Firewall enables DSCP features based on priorities from 0 to 7.
**Flexible bandwidth adjustment**: NFV Cloud Firewall provides an advanced flexible
bandwidth adjustment mechanism. If the pipeline of each level has remaining bandwidth, the bandwidth can be scheduled to sub-pipelines to maximize the bandwidth utilization.
**Peer suppression**: NFV Cloud Firewall enables peer suppression by using the iQoS
technology. Peer suppression reduces the packet rate of the peer and improves the bandwidth utilization of the local host.

## 5 Scenarios

| If your business is deployed in multiple virtual private clouds (VPCs) and cross-VPC |   |   |
|---|---|---|
| communication is enabled, or if your VPCs need to communicate with data centers off the |   |   |
| cloud, you can deploy NFV Cloud Firewall to implement security protection. |   |   |

**Unified security control for group customers**

**Scenario**

Group customers use Group Cloud to integrate the IT systems and data resources of their subsidiaries, branch offices, or departments.

**Requirements**

The customer needs to implement cross-organization and cross-region security policy management in a unified manner to ensure the security and compliance of communications between branch offices. In addition, the customer requires centralized O&M and auditing.

**Solution**

Deploy NFV Cloud Firewall to protect network traffic between VPCs of the group. NFV Cloud Firewall supports cross-organization permission control and policy assignment. The VFW Cloud Firewall configuration and O&M operations are managed by the headquarters.

**Cloud security for the financial industry**

**Scenario**

An industry-leading financial institution intends to build a financial industry cloud that serves its partner enterprises in the ecosystem to implement resource integration and data collaboration.

**Requirements**

The customer requires security isolation for core business systems to prevent external and internal data leaks and meet security compliance requirements of the financial industry.

**Solution**

Use NFV Cloud Firewall to build an enterprise-class network perimeter protection system that supports access control and in-depth traffic inspection from Layer 2 to layer7. This protection system is expected to implement fine-grained access control on internal and external traffic and threat blocking.

**Gov Cloud platform security and compliance**

**Scenario**

To meet policy and regulation compliance requirements, the public sector, state-owned enterprises, and industry regulators set a course for building regional gov clouds and stateowned clouds.

**Requirements**

As network security requirements become stricter, isolation, auditing, and action tracking are required by multi-tenant environments for data security.

**Solution**

Deploy NFV Cloud Firewall as the security hub of the cloud platform to provide policy-based traffic filtering, log auditing, and security event response services to meetcompliance requirements.

**Security service delivery for Gov and industry clouds of ISPs**

**Scenario**

The three major Internet service providers (ISPs) in each province or city have built local private clouds to serve the local public service sector and enterprise customers to promote business transformation and revenue.

**Requirements**

The public service sector and enterprise customers require flexible, scalable security services that are also cost-effective.

**Solution**

NFV Cloud Firewall provides standardized and replicable security services that support ondemand provisioning, automatic scaling, and automated O&M and auditing. This helps the ISPs improve the service delivery efficiency.
