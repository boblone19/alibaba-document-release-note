---
title: "Container Security Service Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 28
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Container Security Service Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Container%20Security%20Service%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Container Security Service Product Introduction 20260701

Container Security Service Produ

## What is CSS?

**Pioneer of cloud security**

Since 2005, the security team of Alibaba Cloud has been responsible for protecting all internal business systems of Alibaba Group. The team has been successfully and consistently defending against global network attacks. Cloud computing technology has been continuously developed and widely used in recent years. This facilitates the shift from using traditional data centers to the cloud computing architecture. In the context of digital transformation in different industries, migrating services and data to the cloud becomes the future of the industry. To protect cloud services, the security team launched Apsara Stack Security in 2011. In 2013, the team officially released the first version of Apsara Stack Security to meet the increasing business requirements of Apsara Stack and ensure the security of Apsara Stack and the industry cloud at the IaaS layer. Since then, Alibaba Cloud has made major technological breakthroughs in implementing fully cloud-native core systems. Based on the cloud-native architecture, enterprises can maximize cloud capabilities and focus on business development. At the same time, developers can also rely on cloud-native technologies and products to improve development efficiency and focus more on the implementation of business logic. This shows that cloud-native technologies are gradually becoming the most effective way to release the value of cloud. As the cornerstone of cloud-native development, container security is undoubtedly the focus of cyber attacks and defense. Based on the security technologies accumulated over the years and the concept of intelligent and automated operations, the Alibaba Cloud security team launched Apsara Stack Security Container Security Service (CSS). This product is intended for Alibaba Cloud users. It covers development environments such as containers, Kubernetes, and microservices and supports the security management of PaaS resources and nodes, CI/CD risk detection, and container runtime protection. It aims to provide high-quality container security assurance services for enterprises and developers.

**Product positioning**

Product name: Apsara Stack Security Container Security Service (CSS). CSS is a unified platform for the security management and operations for Docker and Kubernetes. Through automated security detection of development outputs such as code, development infrastructure, supply chain, and images, CSS can effectively reduce their vulnerability risks, thereby reducing the repetitive work caused by security risks for the development, testing, and operations teams, and reducing the online defense pressure on the security team. In terms of container runtime security, CSS can cover containers and their infrastructure. It supports runtime vulnerability detection and repair, container and infrastructure exception detection, container escape detection, active defense based on files and processes, and threat traceability. This helps effectively defend against zero-day and blind spot exploits. In terms of container asset management, CSS supports asset management from multiple dimensions, including clusters, namespaces, container groups, applications, and images. You can select an appropriate perspective to manage the security of the assets in Kubernetes clusters based on the actual business deployment. In addition, CSS provides a wealth of risk statistics and trend reports to help you quickly and accurately grasp the real-time security status of large-scale container clusters. In terms of security throughout the application lifecycle, CSS aims to help you implement development, security and operations (DevSecOps). By providing an automated and easy-touse security detection method for each phase of the DevOps process, CSS ensures security capabilities for each team and reduces the obstacles to shift left security. CSS makes sure that known security risks can be effectively converged in the early phases of the process, thus reducing the security risks and repair costs of containerized environments and business applications. Container Security Service Produ Code and build: CSS supports security scan of code repositories. Security scans are performed on application code, open source components, base images, supply chains, and infrastructure during the build process based on the scan mechanisms of the security engine. For example, scans are triggered upon update or at the specified time to detect risky plug-ins and middleware, malicious files, and base image vulnerabilities. This reduces security risks during development and improves R&D efficiency. Test: CSS supports gray box testing based on passive Interactive Application Security Testing (IAST). Passive IAST monitors the internal data flow of an application in real time, and is used in combination with the dynamic taint analysis (DTA) technology to dynamically track the propagation process of the marked stain when the program is running. This way, security vulnerabilities in the code can be accurately detected and dynamic security detection is implemented. Release and deploy: The image security scan feature of CSS continuously monitors the security level of images in image repositories to detect issues such as baseline risks, system vulnerabilities, application vulnerabilities, and malicious files. In addition, by using the image trust signature feature, the system can verify whether the image transmitted to the host is a trusted image, thereby strictly controlling the security of the image transmission process between the image repository and the host. Operate and monitor: Server Guard monitors the security of Kubernetes environments, resources, nodes, and containers by installing the agent on all nodes in Kubernetes clusters. It also monitors and analyzes elements such as files, processes, and networks throughout the application lifecycle. The container runtime protection policies and data are based on years of accumulated data, which defend millions of Alibaba Cloud users from up to hundreds of thousands of attacks every day. The security team analyzes more than 10 TB of security data in the Alibaba Cloud public cloud every day to build basic security capabilities, such as malicious IP address library, malicious behavior library, malicious sample library, and vulnerability library.

**Scenarios**

CSS is widely used to build security systems in cloud environments such as the industry cloud, Alibaba Gov Cloud, cloud platforms using chips made by chip companies in China, and co-built cloud. CSS supports security management and operations on cloud containers across sectors, including the public service sector, finance, energy, state-owned enterprises, and national ministries and commissions.

**CI/CD automated security testing**

From code development and submission to the official delivery of applications, every developer encounters security risks introduced in the integrated development environment (IDE), open source code, supply chain, and infrastructure. For example, the open source code may reference middleware with vulnerabilities or images are built by using malicious base images. In an environment that uses CI/CD for high-speed iteration where a large number of submissions are involved, security products must adopt automated and practical detection methods to be effectively integrated into the development process. Based on the principle of secure-by-default, CSS manages software assets such as application code generated during development, referenced open source code, supply chain, images, and infrastructure, and implements real-time automated security checks to ensure that no security risks are introduced in any phase of the CI/CD process. In addition, CSS has little impact on the application iteration speed, which can effectively reduce the repetitive work caused by security risks for the development, testing, and operations teams, thereby improving collaboration efficiency. Container Security Service Produ Integrated Test Automatically perform tests Push

**Developer**

Trigger a Git/Svn Jenkins hook Test Environment Code Repository Push Build a Docker Pull the deployment Compile and package code image environment

**Developer**

Maven build Dockerfile Push Pass the test Pull changes Docker Registry Production Environment

**Microservice-based development scenarios**

In the microservices architecture, the traditional security solution of managing assets based on the operating system is no longer applicable. An accurate presentation of the security status of cloud-native assets requires cloud-native security products that describe threats in an application-oriented manner. CSS makes full use of the advantages of the cloud-native architecture. It can aggregate the data of containers in which applications run and the Alibaba Cloud PaaS, backend as a service (BaaS), and function as a service (FaaS) resources on which they depend, and sort out the security status of applications from the perspective of developers. In the C/S architecture of the traditional security solution, clients are deployed at the operating system layer, failing to fully cover the exception monitoring points in the microservices architecture. CSS integrates endpoint detection and response (EDR) and Runtime Application Self-protection (RASP) to monitor and check the data flow of applications in containers. It can accurately identify vulnerabilities in request traffic and provide professional fixing solutions. It worked well when detecting vulnerabilities during integrated testing and runtime. Cloud Functions (FaaS) </> Application Android </> IOS </> C# </> JavaScript... Cloud APIs (BaaS) Microservice Microservice

**PDS**

**OSS**

**ApsaraMQ**

**Regis**

... API API API API Microservice Microservice Kubernetes Resources (PaaS) Workloader Volumes Network

| Primary feature | Secondary feature | Description |
|---|---|---|
| Container asset management | Container network topology | Visualize publicly exposed ports and network connectivity relationships across clusters. This includes visual security controls for cluster information, cluster risks, image information, mitigation policies, and network connectivity. |
|  | Cluster | View cluster name or ID, cluster type, region, servers, creation time, cluster status, and risk level. |
|  | Namespace | View namespace name, associated cluster, creation time, and risk status. |
|  | Node | View node information, node type, associated cluster, and node status. |
|  | Container | View container ID, alerts, vulnerabilities, pod, server, risk status, and details. |
|  | Pod | View pod name, namespace, number of risky containers versus total containers, pod IP, server, cluster, and risk status. |
|  | Application | View application name, associated cluster, creation time, risk status, and details. |
|  | Runtime image | View risk status and details for the current container runtime and its associated image. |
| Image asset management | Self-managed cluster integration | Integrate self-managed Kubernetes clusters into container asset management and apply container security capabilities. |
|  | Third-party image repository integration | Support up to 20 third-party image repositories (private image repositories). After integration, view imported images in Asset Center > Image Management. |
|  | Basic information | View image registry address or tag, image size, most recent discovery time, risk status, and image fingerprint. |

Container Security Service Produ

## Features

This topic describes the features supported by Container Security and provides their descriptions.

| Image security scanning | Risk information | View image vulnerability information, including system vulnerabilities, application vulnerabilities, baseline risks, and malicious samples. |
|---|---|---|
|  | Application vulnerability | Detect weak passwords in system services and vulnerabilities in both system and application services. |
|  | Weak password baseline | Detect risky accounts such as weak-password accounts, suspicious hidden accounts, cloned accounts, and blank-password accounts. Also check compliance with Linux password policies for MongoDB, SQL Server, MySQL, PostgreSQL, Redis, Rsync, SVN, Linux logon, Windows logon, Apache Tomcat console logon, and FTP logon. |
|  | System vulnerability | Supported operating systems include CentOS 5/6/7, Red Hat 5–9, Debian 6–10, Ubuntu 12.04/14.04/16.04/18.04/20.04/22.04, Oracle Linux 5/6/7/8, Amazon Linux AMI, Amazon Linux 2, SLES 10 SP4, SLES 11 SP1/SP2/SP3/SP4, SLES 12/12 SP1/SP2/SP3/SP4/SP5. Domestic operating systems supported include UnionTech UOS V20, Kylin V10, and Anolis OS 7/8. |
|  | Malicious image sample | Detect and remove ransomware, mining programs, DDoS Trojans, Trojan programs, backdoor programs, malicious programs, important programs, worms, suspicious programs, and self- mutating Trojans. |
|  | Unauthorized access baseline | Perform high-risk exploitation baseline checks on applications vulnerable to unauthorized access. Supported services include CouchDB, Docker, Elasticsearch, Hadoop, Jenkins, Memcached, Apache, Tomcat, and ZooKeeper. Checks cover identity authentication, service configuration, and password leakage. |
|  | CI/CD scanning plugin | Integrate a plugin into your CI/CD tool to trigger image scanning before uploading to a repository. Supported modes: Jenkins Freestyle mode integration. Jenkins Pipeline mode integration. |
| Container file protection | Container file tamper- proofing | Monitor directories or files inside containers in real time. Generate alerts or block malicious tampering attempts to ensure stable container operation. Note You must enable the related plugin using a supported kernel version. v3.18.3-Kunpeng and v3.18.3-Phytium are not supported. |
|  | Risky image blocking | Perform security validation on images. Block or alert on images that match risky image blocking rules. |

Container Security Service Produ

| ontainer Securi t Introduction·F | ty Service Produ eatures |  |
|---|---|---|
| Container proactive defense |  |  |
|  | Non-image program defense | Detect and block programs launched outside of images. Proactively defend against malware intrusions and known or unknown attack patterns. |
|  | Container escape prevention | Detect high-risk behavior across multiple dimensions—such as process, file, and system calls—to identify container escape attacks. These attacks exploit misconfigured containers or vulnerabilities in Docker or the underlying operating system. Block escape attempts to protect container runtime security. This feature blocks attackers from escaping containers to compromise the host server and improves overall server security. Note You must enable the related plugin using a supported kernel version. v3.18.3-Kunpeng and v3.18.3-Phytium are not supported. |
| Container image signing | Container image signing | The container image signing feature signs container images to establish trust. Deploy only container images you explicitly approve. Prevent unsigned images from starting. |
| Container firewall | Container network protection | Create and manage network access control policies between container network objects within the same cluster. Apply network access control between container objects and IP or DNS objects. Display protection status, including risk details list, number of risks in the last 24 hours, number of risks in the last 30 days, number of risks in the last 180 days, number of unprotected clusters versus total clusters, protection status (enabled or disabled), and total rule count. Note You must enable the related plugin using a supported kernel version. v3.18.3-Kunpeng and v3.18.3-Phytium are not supported. |
| Vulnerability management | Linux system vulnerability | Supported distributions include CentOS 5, 6, and 7; Red Hat 5 through 9; Debian 6 through 10; Ubuntu 12.04, 14.04, 16.04, 18.04, 20.04, and 22.04; Oracle Linux 5, 6, 7, and 8; Amazon Linux AMI; Amazon Linux 2; SLES 10 SP4; SLES 11 SP1, SP2, SP3, and SP4; SLES 12, 12 SP1, SP2, SP3, SP4, and SP5; and others. Supported operating systems include CentOS 5/6/7, Red Hat 5–9, Debian 6–10, Ubuntu 12.04/14.04/16.04/18.04/20.04/22.04, Oracle Linux 5/6/7/8, Amazon Linux AMI, Amazon Linux 2, SLES 10 SP4, SLES 11 SP1/SP2/SP3/SP4, SLES 12/12 SP1/SP2/SP3/SP4/SP5. Domestic operating systems supported include UnionTech UOS V20, Kylin V10, and Anolis OS 7/8. |
| 0 | > Document Version: 2026070 |  |

|  | Application vulnerability | Detect weak passwords in system services and vulnerabilities in both system and application services. |
|---|---|---|
| Baseline check | Container baseline check | Scan container configurations for security issues and generate alerts. Use Alibaba Cloud’s best practices for Kubernetes Master and Node nodes to check container baseline configurations. Scanning covers: Alibaba Cloud Standard – Docker security baseline check. Based on Alibaba Cloud’s best practices, this check evaluates Docker security auditing, service configuration, and file permissions to detect and warn about risks. Alibaba Cloud Standard – Kubernetes Master security baseline check. Checks Kubernetes Master node configurations based on Alibaba Cloud’s container security best practices. Alibaba Cloud Standard – Kubernetes Node security baseline check. Checks Kubernetes Node node configurations based on Alibaba Cloud’s container security best practices. |
|  | Threat intelligence detection | Use Alibaba Cloud threat intelligence to identify potential threats in your assets. Threat intelligence correlates, analyzes, and processes threat-related data to detect threats and trigger timely alerts. This improves threat detection efficiency and response speed. Supported intelligence types: Malicious domain names. Malicious IP addresses. Dark web communication IP addresses. Command-and-control communication IP addresses. Miner pool communication IP addresses. Malicious URLs. Malicious download sources. |

Container Security Service Produ

|  | Threat model detection | The threat detection module uses more than 350 threat detection models. It covers over 95% of cloud-based intrusion events. Models are categorized by operating system, analysis target, and attack method to help users quickly understand cloud environment intrusions. Supported alert types: Anomalous process behavior. Anomalous logons. Anomalous activity. Sensitive file tampering. Suspicious network connections. Anomalous accounts. Application intrusion events. Persistent backdoors. Application threat detection. Web shells. Malicious processes (cloud anti-virus scanning). Malicious scripts. |
|---|---|---|
| Intrusion alerting |  |  |
|  | Anti-virus scanning | Supported virus types: Ransomware, mining programs, DDoS Trojans, Trojan programs, backdoor programs, malicious programs, important programs, worms, suspicious programs, and self-mutating Trojans. Immediate scanning: Deploy scanning tasks immediately. Apply policies by asset group. Periodic scanning: Set a scan schedule for selected servers in specified asset groups. |

Container Security Service Produ

|  | Precision defense | Support process behavior blocking, process chain defense, process binary detection, and script execution detection. Block ransomware, mining programs, Trojan programs, worms, malicious programs, backdoor programs, DDoS Trojans, self- mutating Trojans, infection-type viruses, hacking tools, exploit programs, compromised foundational software, and rootkits. Detect scripting languages including bash, Python, Perl, PowerShell, VBScript, batch, JScript, C#, C, and Lua. Detect batch worm-mining scripts. Detect exploit scripts automatically generated by open-source weaponized frameworks such as Cobalt Strike, Empire, Metasploit, and Nishang. Note You must enable the related plugin using a supported kernel version. v3.18.3-Kunpeng and v3.18.3-Phytium are not supported. |
|---|---|---|
|  | Web shell detection | Detect web shells. Automatically block abnormal connections made through known web shells and isolate related files. Clean and isolate web shells in PHP, PHT, JSP, JSpx, ASP, ASA, CER, CDX, HTR, HDX, ASMX, ASHX, ASAX, ASPX, ASCX, and CS files. |
| Log retrieval | Log retrieval | Query logs for process snapshots, network connections, and process launches. |
| Feature settings | Feature settings | Container network topology: Draw network topology diagrams for container clusters. View them in Asset Center. Enabling this feature consumes a small amount of additional CPU resources. Malicious network behavior prevention: Block known malicious network behavior to strengthen security defenses. Container escape prevention: Monitor privilege escalation from inside containers to the host. Detect attempts to access host resources or other containers on the host. Support blocking or alerting. Authorization management: Manage container clusters authorized to use container security protection features. |

Container Security Service Produ

| Private Docker Registry Repository A Repository B S Image V3 Image V4 |  | Aegis Server S Console Analysis & Detection Dipper GLE AV r VUL Scan Baseline Scan Exposure S Code SCA DTA Honeypot Sandbox Monitor & Scan r EDR RASP Honeypot Mon Kubernetes Cloud API Cloud Function |  |  | Code Repository Project-A Project-B n V3.1 V4.1 |
|---|---|---|---|---|---|
|  | can |  | S | ca |  |

|  |  | V3.1 |
|---|---|---|

| nito | r |
|---|---|
| nito | r |

|  |  | Image V3 |
|---|---|---|

| SLB | EIP |
|---|---|

| Redis | MongoD |
|---|---|

| Java | Android |
|---|---|

Container Security Service Produ re

## Service architecture

The security control mode of Apsara Stack Security Container Security Service (CSS) adopts a C/S architecture based on the cloud-native environment, enabling multi-dimensional monitoring at the operating system layer, application layer, and environment layer. At the same time, all resource-intensive security detection capabilities are deployed on the server side, while the client is responsible only for feature collection and risk mitigation, fundamentally reducing CSS resource consumption. You can interact with CSS in browser/server mode and can log in to the CSS console over HTTPS. CSS supports mainstream browsers. In the CSS console, you can query risk data in the cloud in real time and configure security policies to handle security risks based on your business requirements. Monitor Scan Kubernetes ACK ACR SEA ... Alibaba Cloud SLS RDS ApsaraMQ ... Workloader Network Application Volume Cloud API C# PHP Python ... Cloud Function The dotted line in the figure is the The agent is installed on all nodes of the Kubernetes cluster and continuously monitors Kubernetes nodes and containers. The agent communicates with the CSS server over a TCP persistent connection and retrieves required scripts, rules, installation packages, and other files from the server over HTTP. The agent can automatically connect to the CSS server for online upgrades. The scanner is deployed on the server side and continuously monitors user code repositories, Docker configurations, image repository configurations, Kubernetes configurations, Kubernetes resources, cloud service configurations, and image repositories by using the network of Apsara Stack. Scan conditions such as update triggers or scheduled pulls can be set to meet varying levels of user security requirements, making the scan method more tailored to user needs while reducing resource consumption based on configurations.

|  | Aegis |
|---|---|
|  | TIP |

|  |  | Physical Machines |  |
|---|---|---|---|
|  |  | Physical Machines |  |
| Physical Machines | Physical Machines | Physical Machines |  |

Container Security Service Produ re The Runtime Application Self-protection (RASP) plug-in is referenced via runtime parameters during container building and is deployed within the container application, continuously monitoring its internal data flow. It sends monitoring data back to the server over HTTP.

**Deployment**

From Apsara Stack Security V3.18.2, the method of using base resources is updated for CSS. Before the update, Apsara Stack physical machines are deployed in Apsara Infrastructure Management. After the update, the machines are deployed in PaaS environments to share resource pools with cloud services. The following figure shows the service architecture after the update. Apsara Infrastructure Management-based PaaS-based Deployment Deployment Aegis SOC SOAR SOC SOAR TIP HSM ... HSM ... Physical Machines The server side consists of the following types of modules: Lateral basic capabilities: the common capabilities of Apsara Stack Security services, which can be used in consoles or by calling API operations. Core capabilities: asset management, alerting, and file collection. Detection and defense: detection of and defense against vulnerabilities and baseline risks, and protection of files, networks, and processes. Detection engines: the commercial virus detection engines, a self-developed virus detection engine, and a big data computing engine. Client management: manages client connections, updates the status of container clusters, and delivers configuration rules.

| Asset Discovery Asset Identification |  | Code Managemen Build Managemen | t t | Image Storage Image Distribution |  | Container Orchestration Cluster Management |  | Network Visualization Network Isolation |  |  | Service Discovery and Registration Service |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Observation Asset Deployment Image Resource Traffic Inventory Management Security Monitoring Management Association ConCtodaeiner IdentificationS eacunrityd Association Security Security Monitoring |  |  |  |  |  |  |  |  |  |  |  |
| Control Container Security Vulnerability Scan Malicious File Protec Bti aon seline Risk Behavior Detection |  |  |  |  |  |  |  |  |  |  |  |
| Vulnerability Scan |  |  |  |  |  |  |  |  | Behavior Detection |  |  |

Container Security Service Produ re

**App: A**

**App: B**

**App: C**

**App: B**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Aegis**

**Aegis**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**Pod**

**&**

**CSS**

**oneAgent**

**&**

**CSS**

**oneAgent**

**Kubelet/Runtime**

**Kubelet/Runtime**

**Guest OS**

**Host OS**

**Hypervision-ECS**

**Date Center**

**Physical Machines,**

**Network, and**

**Alibaba Cloud Infrastructure**

**Storage**

**Computing, Storage, and**

CSS provides security capabilities to protect Docker, Container Service for Kubernetes (ACK), and Container Registry on the tenant side, servers in data centers, and servers of third-party clouds. The capabilities are divided into the following categories: centralized cloud asset management, CI/CD security, image security, container runtime protection, and microsegmentation. Protection Throughout Container Lifecycle CI/CD Image Service Process Protection File Protection Network Threat Prevention AlibabaCloudSecurityCenter

**Disaster recovery architecture**

**Zone-disaster recoveree**

The zone-disaster recovery architecture of CSS follows the rules of the active-active mode. In this architecture, disaster recovery is ensured by cloud storage or middleware.

|  |  |  |  | Primary/Secondar | y |
|---|---|---|---|---|---|
|  | Network VIP |  |  | Primary/Secondar | Network y VIP |
|  | Aegiserver Aegisbiz Guard Server AegisMaster ... |  |  | Active- | Aegiserver Aegisbiz Guard Server AegisMaster ... |
|  |  |  |  | active |  |
|  |  | MiniRDS Cloud Storage OSS OSS |  | Primary/Secondar | MiniRDS Cloud Storage y OSS OSS |
| Middleware Tair MetaQ Diamond Dubbo |  |  |  | Active- active | Middleware Tair MetaQ Diamond Dubbo |

|  | VIP |  |
|---|---|---|

|  | VIP |  |
|---|---|---|

| Component | Solution |
|---|---|
| Server Guard | The active-active deployment strategy depends on middleware and cloud storage to ensure data consistency. |
| DNS | Anycast virtual IP addresses (VIPs) are used to isolate traffic between the primary and secondary data centers. |
| VIP | Border Gateway Protocol (BGP) routing is used to implement primary/secondary switchover. |

Container Security Service Produ re Data Ingress Data Ingress Primary Data Secondary Data The following table describes the disaster recovery solution in each component.

| MiniRDS | Secondary databases synchronize data from the primary databases based on binary logs. |
|---|---|
| SLS | Data synchronization is implemented based on backups in Object Storage Service (OSS). |
| OSS | Data synchronization between the primary and secondary data centers is supported. |
| Middleware | The active-active deployment strategy depends on MiniRDS to ensure data consistency. |

Container Security Service Produ re

**Geo-disaster recovery**

The multi-region architecture of CSS follows the rules of independent regions. General regions do not depend on the central region, and data is completely isolated from services.

**Support for chips offered by chip companies in China**

**Differences between Apsara Stack and self-managed platforms**

The following list describes the features of CSS that are supported on platforms using chips offered by chip companies in China: Capabilities of CSS are 100% consistent between Apsara Stack using x86 CPUs and selfmanaged platforms using x86 Hygon CPUs. From Apsara Stack V3.18.3, CSS can be deployed on platforms using ARM-based Phytium and Kunpeng CPUs. However, some blocking features that rely on plug-ins, such as container firewall, container file protection, and container active defense, are not supported. Container Security Service Produ

## Features

### Asset center

**Container network topology**

Kubernetes uses different resource isolation solutions based on the actual deployment method. Apsara Stack Security Container Security Service (CSS) provides a variety of container asset security management features and detailed data of each element of Kubernetes from the cluster perspective to meet the usage habits of different users. You can use these features and data based on the actual situation. Internet perspective: information cards from the Internet perspective. Cluster perspective: Kubernetes cluster information cards and drill-down perspectives of nodes, namespaces, and applications.

**Container management**

Kubernetes uses different resource isolation solutions based on the actual deployment method. For example, you can deploy your business in hundreds of thousands of small clusters where one or more business divisions share a cluster, or in one or more large clusters in each zone where business divisions are isolated by namespace. CSS provides a variety of container asset security management features and detailed data of each element of Kubernetes from the cluster perspective to meet the usage habits of different users. You can use these features and data based on the actual situation. Cluster: Kubernetes cluster information cards and drill-down perspectives of nodes, namespaces, and applications. Namespace: the basic namespace information and the distribution of pods at risk. Application: the basic application information and the distribution of containers at risk. Pod: the basic pod information and the distribution of containers at risk. Container: the basic container information, container vulnerability information, and intrusion risk information.

**Image management**

Using risky images causes security risks to the containers created based on them. The asset management feature of CSS provides image-based risk tracing and protection capabilities, with a management scope covering from the image to the whole Kubernetes cluster. Image: the basic image information and the threat information such as system vulnerabilities, application vulnerabilities, baseline risks, and viruses and trojans.

### CI/CD security

**Container image scan**

Container Security Service Produ The container image scan feature can detect and identify high-risk system vulnerabilities, application vulnerabilities, malicious samples, configuration risks, and sensitive data in images. Vulnerabilities may exist in the basic system software, middleware, web applications, and databases that are in your images. The vulnerabilities include mining programs and backdoor programs. Containers that run based on vulnerable images pose threats to your assets. This feature allows you to check whether image vulnerabilities and malicious samples exist in your vulnerable assets, and provides suggestions on vulnerability fixing. This feature provides end-to-end vulnerability management capabilities and allows you to fix image vulnerabilities in a convenient manner. Supported operating systems CentOS 5, 6, and 7 and Red Hat Enterprise Linux (RHEL) 5, 6, and 7 Ubuntu 12.04, 14.04, 16.04, 18.04, and 18.10 Alpine 2.3 to 2.7 and 3.1 to 3.12 Oracle Linux 5, 6, 7, and 8 Amazon Linux AMI and 2 Debian 6, 7, 8, 9, and 10 SUSE Linux Enterprise Server (SLES) 5, 6, 7, 8, and 9, SLES 10 SP4, SLES 11 P3, SLES 12 SP2, and SLES 12 SP5 Fedora Linux 2X and 3X openSUSE 10.0, Leap 15.2, and Leap 42.3 Supported detection capabilities Scan images for system vulnerabilities Scan images for application vulnerabilities Scan images for baseline risks Scan images for malicious samples

### Container Runtime Protection

**Vulnerability Management**

Container Security detects major types of vulnerabilities to help you understand the vulnerabilities and risks in your assets. It supports the detection of Linux software vulnerabilities and application vulnerabilities, including emergency vulnerabilities. For detected vulnerabilities, Container Security provides remediation guidance, validation options, detailed vulnerability information, and one-click scanning.

**Linux Software Vulnerability Detection and Remediation**

Container Security compares the software versions installed on your ECS instances with the official CVE vulnerability database. This allows it to identify vulnerable software, such as SSH, OpenSSL, and MySQL, and send vulnerability alerts that include remediation recommendations.

**Linux software vulnerability**

CentOS 5/6/7, Red Hat 5/6/7 Debian 3.0/3.1/4/5/6/7/8/9/10/11/SID Ubuntu precise (12.04), trusty (14.04), xenial (16.04), bionic (18.04) Oracle Linux 5/6/7/8

| Type | Items |
|---|---|
| Weak credentials for system services | OpenSSH, MySQL, MSSQL, MongoDB, FTP, VSFTP, ProFTPD, Memcache, Redis, Subversion, SMB, SMTP, POP3, IMAP. |
| System service vulnerabilities | OpenSSL, SMB, RSYNC, VNC, pcAnywhere, Redis. |
| Application service vulnerabilities | Tomcat, Apache Struts 2, ActiveMQ, Confluence, CouchDB Query Server, Discuz! Docker, Drupal Drupalgeddon 2, ECShop, Elasticsearch, Weaver OA, Hadoop JavaServer Faces 2, JBoss, Jenkins, Kubernetes, MetInfo, PHP, OpenSSL phpMyAdmin, Actuator unauth RCE, ThinkPHP, WebLogic, WordPress, Zabbix |

Container Security Service Produ Amazon Linux AMI, Amazon Linux 2 SLES 10 SP4, SLES 11 SP1/SP2/SP3/SP4, SLES 12 / 12 SP1/SP2/SP3/SP4/SP5, SLES 15

**Linux Vulnerability Detection and Remediation Workflow**

**Linux Vulnerability Detection Workflow**

i. The client reports a heartbeat and receives scheduled scan tasks based on the configured scan interval. ii. After the client reports the installed package information, vulnerabilities are matched using OVAL rules. Full vulnerability details are added and then filtered through the vulnerability whitelist and operational policies before being stored.

**Linux Vulnerability Remediation Workflow**

i. Manual remediation creates a remediation task that is executed on a schedule. ii. You cannot remediate vulnerabilities in the (kernel).

**Application Vulnerability Detection**

Container Security compares the middleware versions installed on your ECS instances with official middleware vulnerability databases. This allows it to identify vulnerable middleware components and send vulnerability alerts that include remediation recommendations.

**Baseline Checks**

Container Security provides default baseline check items. It scans container assets against security baselines to identify configuration risks and defects, and then provides risk alerts and remediation guidance. The currently supported container baseline templates include the following: Alibaba Cloud Standard – Docker Security Baseline Check CIS Standard – Kubernetes (ACK) Master Node Security Baseline Check CIS Standard – Kubernetes (ACK) Node Security Baseline Check Alibaba Cloud Standard – Kubernetes Master Security Baseline Check Alibaba Cloud Standard – Kubernetes Node Security Baseline Check

| Defense Method | Description |
|---|---|
| Process Behavior Interception | Using heuristic and regex rule libraries from Alibaba Cloud’s machine learning engine, it monitors server processes across dimensions such as network behavior and command-line activity to detect and block risky process behaviors. |
| Process Chain Defense | Analyzes process context to assess risk and blocks common exploit attempts—such as information probing or downloading malicious code through web vulnerabilities. |
| Process Binary Detection | Detects ransomware, mining programs, Trojans, worms, malicious programs, backdoors, DDoS Trojans, self-mutating Trojans, file-infector viruses, hacking tools, exploit kits, compromised system software, and rootkits. |

Container Security Service Produ

**Intrusion Alerts**

Container Security detects security alert events in real time across your assets. It covers alert types such as webpage tamper protection, abnormal processes, web shells, suspicious logins, and malicious processes. Using detection modules such as stream computing engines, GLE, and HIPS, it provides comprehensive threat detection to promptly identify security threats and help you maintain visibility into your security posture. Intrusion event alerts indicate common threats or even Advanced Persistent Threat (APT) attacks detected on your servers. These threats may originate from a malicious IP address that targets your assets or from anomalous activity within compromised assets, such as a host that executes malicious scripts or connects to malicious download sources.

**Anti-Virus Scanning**

Based on the automated analysis of massive virus samples and persistent attack patterns, the Alibaba Cloud security team developed a machine learning-powered anti-virus scanning engine. Container Security uses this engine to scan specified servers for viruses and provides actions such as cleaning, ignoring, whitelisting, or manually handling detected threats. Supported virus types include ransomware, mining programs, DDoS Trojans, Trojan programs, backdoor programs, malicious programs, high-risk programs, worms, suspicious programs, and self-mutating Trojans.

**Warning**

Risk exposure checks require extensive data management for assets, applications, and risks. This feature depends on the Dipper engine. If your environment lacks this engine, you cannot use this feature.

**Precise Defense**

Host-based Intrusion Prevention System (HIPS) uses heuristic behavior rules to intercept risky actions in real time. These actions include viruses, Trojans, malicious programs, suspicious network connections, and web shell connections. HIPS supports both single-step and multi-step defense. It delivers timely and accurate warnings before intrusion behaviors can impact your information systems, building an intelligent defense system that identifies threat actions by their source entities. Kernel-level interception effectively eliminates delays in how Container Security handles viruses.

| Script Execution Detection | Detects scripts written in Bash, Python, Perl, PowerShell, VBS, BAT, JScript, C#, and C. Detects auto-generated exploit scripts from open-source offensive frameworks (Cobalt Strike, Empire, Metasploit, Nishang). Detects batch worm mining scripts. |
|---|---|

Container Security Service Produ

**Web Shell Detection**

Container Security detects web shells and automatically blocks suspicious connections that are initiated through known web shells. It isolates related files and effectively cleans PHP, ASP, and JSP web shells. Web shell detection is powered by the proprietary Alibaba Cloud GLE engine. Refined over seven years on the Alibaba Cloud public cloud, GLE combines static pattern matching, dynamic taint simulation through Abstract Syntax Tree (AST) execution, and heuristic anomaly detection to accurately identify large web shells, small web shells, and one-liner web shells. The Alibaba Cloud security team has publicly run four “Zeus Crowdsourced Testing” campaigns. The GLE engine has been tested by over 600 white hat hackers and achieved a detection rate of over 95% against advanced adversarial examples that were crafted by toptier researchers.

**Warning**

Container Security supports web shell scanning for automatically discovered or manually added web directories, including full-disk scans.

**Threat Model Detection**

By leveraging the big data association analysis capabilities of Dipper, the Container Security threat detection module includes over 350 threat detection models that cover more than 95% of cloud intrusions. The models are categorized by operating system, analysis target, and attack technique to help you quickly understand intrusion events in your cloud environment.
**Supported asset types:** ECS, classic network physical machines, on-premises IDC hosts,
and third-party cloud hosts.
**Alert types (require Dipper):** abnormal process behavior, suspicious logins, anomalous
activity, sensitive file tampering, suspicious network connections, abnormal accounts, application intrusions, persistent backdoors, application threat detection, and container escape.
**Alert types:** web shells, malicious processes (cloud-based scanning), and malicious
scripts.

**Warning**

Threat detection model computation requires the Dipper engine. If your environment lacks this engine, you cannot use this feature.

**Threat Intelligence Detection**

Using Alibaba Cloud Threat Intelligence, Container Security can effectively identify potential threats in your assets. Threat intelligence correlates, analyzes, and processes threat-related data to deliver timely alerts, which improves threat detection efficiency and response speed.

| Category | Description |
|---|---|
| Protection Status | Provides a summary page for container firewall policy activity. |
| Protection Management | Configure protection policies for different source/destination network objects. Supports: Container-to-container. Container objects and IP/DNS objects. IP object, DNS object, and container object. |
| Network Objects | Container objects: Create network objects using attributes such as namespace, application name, and image for easier configuration and management. IP objects: Create network objects using IP addresses. DNS objects: Create network objects using DNS-resolved domain names. |

| Configuration Item | Description |
|---|---|
| Rule Name | Enter a rule name. Use 6–50 characters, starting with a letter or Chinese character. You can include digits, underscores ( ), and _ hyphens (-). |

Container Security Service Produ Supported intelligence types include malicious domain names, malicious IP addresses, darknet communication IP addresses, C2 communication IP addresses, miner pool communication IP addresses, malicious URLs, and malicious download sources.

**Warning**

Threat intelligence detection requires the Dipper engine. If your environment lacks this engine, you cannot use this feature. To use threat intelligence in Container Security, you must purchase the Alibaba Cloud Threat Intelligence Service separately.

**Container Firewall**

Using the access control capabilities from the Alibaba Cloud network plug-in (AliNet), Container Firewall enforces real-time lateral access control between containers based on configured protected objects and policies.

**Container File Defense**

Powered by the proprietary Alibaba Cloud SecWebGuard plug-in, Container File Defense monitors directories and files inside containers in real time. It triggers alerts or blocks tampering attempts to prevent illegal content or malicious code from being injected into your applications and ensures stable container operations.

**Prerequisites**

You must install the Container Security Agent on all servers or nodes in the cluster that you want to protect and ensure that the SecWebGuard plug-in runs properly.

|  | Container Security Service Prod ct Introduction·Feature |
|---|---|

| Rule Configu ration | Protected Directory | Specify the directory to protect. Requirements: Start with /. Specify only one directory. Path length must be under 500 characters. One rule protects one directory. To protect multiple directories, click Operation > Add to create additional rules. A single rule supports up to 10 protected directories. |
|---|---|---|
|  | Process Whitelist | List processes allowed to modify the protected directory. Whitelisted processes won’t trigger alerts or blocking. Requirements: Use container-view process paths only. Each process path must be under 50 characters. Separate multiple processes with semicolons (;). Up to 10 whitelist processes per protected directory. |
|  | Action | Select an action when tampering is detected: Alert: Generate an alert only when the protected directory is modified. Block: Generate an alert and block the responsible process when the protected directory is modified. Note Start with Alert mode. After confirming normal operations don’t trigger false alerts, switch to Block mode to avoid disrupting legitimate processes. If a legitimate process gets blocked, add it to the process whitelist. |

**Container Active Defense**

Container Active Defense proactively identifies security risks across multiple dimensions, including image integrity, runtime behavior, and the runtime environment. By configuring rules, you can block untrusted processes and prevent container escape, which raises your overall container security level.

**Risky Image Blocking**

After you create a **Risky Image Blocking** rule, Container Security validates the images that are used to create resources in the specified cluster. If an image matches the rule, an alert or a blocking action is triggered. This ensures that only compliant images run in your cluster.

**Managing System Rules**

| Configuration Item | Description |
|---|---|
| Rule Name | Enter a rule name. |
| Rule Type | Select a rule type from the drop-down list. Choose a type based on your protection needs. By default, all detection items for the selected type are enabled. Uncheck any items you don’t need. See the console for available rule types and detection items. |

Container Security Service Produ After you create a Risky Image Blocking rule for a cluster, any resource creation that uses an image, such as a pod, triggers a security validation request to Container Security. Container Security then checks the image against the rule for the cluster. If the image matches the rule, Container Security triggers an alert or blocks the operation and logs a security validation alert. All rules in the same cluster take effect. If an image matches multiple rules, multiple alerts are generated with the corresponding actions. If a rule contains multiple conditions, Container Security executes the rule action as soon as a condition is matched, without checking the other conditions. The matching priority within a rule is: whitelist > blacklist > others (malicious samples > unscanned images > baseline violations > vulnerabilities).

**Non-Image Program Defense**

In container environments, base software is embedded in the container image and should not be installed or modified during runtime. Therefore, launching programs from outside the image is considered abnormal behavior and often indicates malware injection. The Non-Image Program Defense feature detects and blocks such activity to secure your container runtime.

**Managing System Rules**

Container Security provides a default system rule for Non-Image Program Defense. If you do not have custom rules, this system rule is enabled by default and generates alerts for non-image program launches across all integrated clusters. You can view this rule on the System Rules tab in the Container Active Defense section of the Container Security console. The system rule uses only the Alert action and never blocks operations. You can enable or disable the rule and adjust the clusters to which it applies. When you add or change clusters, the system rule automatically includes the new clusters. When you first use this feature, you should monitor the system rule alerts for false positives. The system rule does not support whitelists or blocking. To add a whitelist or enable blocking, you must create a custom rule. If you create a custom rule, the system rule is automatically disabled. You cannot re-enable the system rule until you delete all custom rules.

**Container Escape Prevention**

In standard container environments, which exclude secure containers, containers share the host OS kernel. Attackers can exploit container vulnerabilities to escalate privileges and compromise the host or other containers. You can configure Container Escape Prevention rules to block such escapes and secure your runtime environment. This feature supports only clusters that meet both of the following conditions:

**The cluster is an ACK dedicated cluster or a self-managed Kubernetes cluster with**

**the Container Security Agent installed.**

| Defense Action | Select a defense action: Alert: Generate an alert only when a defined risk is detected. Block: Generate an alert and block the associated process or operation when a defined risk is detected. Important Some legitimate workflows might trigger rules. Start with Alert mode, observe thoroughly, then enable Block mode if needed. |
|---|---|
| Whitelist | Click + Add Rule and enter image names to whitelist. Up to 20 entries allowed. Use partial keywords for fuzzy matching. For example, with image address yundun-example-registry.cn-hangzhou.aliyuncs.com/yundun- example/yun-repo:test, these whitelist entries are valid: yun-repo test yun-repo:test repo:test Important Whitelisted images bypass escape behavior checks. Use this feature carefully. |

Container Security Service Produ

**Container Image Signing**

Container Image Signing lets you enable trusted signing of container images. This feature ensures that only your approved images can be deployed, which prevents unauthorized and unsigned images from running and fundamentally improves asset security.

### Log retrieval

**Quick retrieval**

You can query logs for process snapshots, network connectivity, and process startup. This feature supports prefix-based fuzzy match.

**Supported log types:**

Process snapshot: Process runtime information on a host at a point in time. Network connectivity: Logs of outbound connections initiated by a host. Process startup: Information about processes starting on a host.

### Feature Settings

**Feature Overview**

| Feature Module | Description |
|---|---|
| Container Network Topology | Displays communication relationships between services in container clusters. This helps with security analysis and troubleshooting. |
| Malicious Network Behavior Prevention | Blocks known malicious network behaviors. This prevents containers from being used for C2 communication, mining, and other attacks. |
| Container Escape Prevention | Protects against privilege escalation where container permissions are elevated to the host. It supports alerting or blocking. |
| Authorization Management | Manages container clusters that access mitigation capabilities and resource quotas (CPU core count). |

Container Security Service Produ
