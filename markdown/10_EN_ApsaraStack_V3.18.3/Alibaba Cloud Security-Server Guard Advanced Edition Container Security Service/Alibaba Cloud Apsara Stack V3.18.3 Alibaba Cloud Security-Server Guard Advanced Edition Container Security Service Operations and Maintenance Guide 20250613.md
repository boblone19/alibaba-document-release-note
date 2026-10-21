---
title: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Operations and Maintenance Guide 20250613"
product_version: "V3.18.3"
doc_version: "20250613"
pdf_pages: 27
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Operations and Maintenance Guide 20250613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Container%20Security%20Service%20Operations%20and%20Maintenance%20Guide%2020250613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Operations and Maintenance Guide 20250613

## Table of Contents

- 1 O&M documentation
  - 1.1 Introduction
  - 1.2 High availability
  - 1.3 Disaster recovery and backup
  - 1.4 Monitoring and alerting
  - 1.6 Hot upgrade
  - 1.7 AliNet (06_21) Linux Driver OS / Kernel List

## 1 O&M documentation

### 1.1 Introduction

Container Security Service (CSS) is a centralized management and operations platform for immutable infrastructure to ensure cloud native container security. CSS uses the automatic mode to resolve security issues that occur when containers are constantly integrated, delivered, deployed, and run. CSS uses a cloud-native architecture of Server Guard to provide multiple features such as cloud asset management, baseline check, proactive defense, security hardening, and security status visualization. CSS can efficiently detect and block risks such as container escapes, viruses, attacks, encryption ransomware, and vulnerability exploits. CSS protects runtime nodes, containers, and images in and outside the cloud, and helps you meet regulatory compliance requirements. The feature of container image scan detects high-risk and medium-risk system vulnerabilities, application vulnerabilities, malicious samples, configuration risks, and sensitive data in images. The feature provides suggestions on how to handle these issues and supports end-to-end image risk management. The container firewall feature is provided by CSS to ensure the security of container environments. If attackers exploit vulnerabilities or malicious images to intrude into clusters, the container firewall feature generates alerts or blocks attacks.

**Architecture**

YundunConsole YundunBaseService AegislmageAnalyzer Lateral Basic Capabilities Dipper Compute Engine Aegisbiz AegisSuspicious SasFileserver

**SasCluster**

Core Capabilities AegisContainerNetwork SasContainerService AegisVirusScan MiniRDS

**Server**

**Side**

AegisVulnerability AegisHealthCheck AegisDetect OSS Detection and Defense Capabilities SLS YaraSlave AegisMaster AegisCloudavbd MetaQ/Diamond Aegiserver Aegisupdate AegisPrivateCloudEngine AegisCloudavira Tair/SchedulerX Client Management Detection Engine

**Middleware**

**BasicThinCluster**

AliYunDun AliYunDunUpdate AliNet sas-jenkins-plugin sas-image-scanner

**Client**

**Side**

ECS Instance or Server Outside Cloud (ACK or Self-managed Kubernetes Node) ECS Instance or Server Outside Clo CSS uses the detection capability of Server Guard at both the server side and client side. Server side: manages the security of container clusters and image assets in and outside the cloud, and provides core capabilities such as detection and defense capabilities. Client side: reports the running status of container clusters and nodes in real time, and provides running detection and network blocking capabilities.

**Server side**

The server side consists of the following types of modules: Lateral basic capabilities: the common capabilities of Apsara Stack Security services, which can be used in consoles or by calling API operations. Core capabilities: asset management, alerting, and file collection. Detection and defense: detection of and defense against vulnerabilities and baseline risks, and protection of files, networks, and processes. Detection engines: the commercial virus detection engines, a self-developed virus detection engine, and a big data computing engine. Client management: manages client connections, updates the status of container clusters, and delivers configuration rules. The following table describes modules of the server side.

| Module | Description |
|---|---|
| YundunConsole | This module corresponds to the CSS console. Security administrators can perform centralized management in the console. |
| YundunBaseService | This module allows third-party developers to call API operations to use the security feature. |
| AegisSuspicious | This module is used to manage alerts, intrusions, and application whitelists. |
| Aegisbiz | This module is used to manage the clusters and image assets in and outside the cloud. |
| SasFileserver | This module corresponds to the file collection feature. |
| AegisContainerNetwork (AegisMetaData) | This module corresponds to the network visualization and container firewall features. |
| SasContainerService (NewSas) | This module corresponds to the image plug-in scan feature. |
| AegisHealthCheck | This module corresponds to the baseline check feature. |
| AegisVirusScan | This module corresponds to the file check feature. |
| AegisDetect | This module corresponds to the file whitelist feature. This module previously corresponds to the file check feature, which is migrated to the AegisVirusScan module. |

| AegisVulnerability | This module corresponds to the vulnerability detection feature. |
|---|---|
| AegisPrivateCloudEngine | This module corresponds to the self-developed Graph Learning Engine (GLE) of Alibaba Cloud for virus detection. |
| AegisMaster | This module is used to configure the Server Guard agent and manage plug-ins. |
| Aegiserver | This module is used to manage the connections of the Server Guard agent, deliver configurations, and forward messages. |
| Aegisupdate | This module is used to upgrade the Server Guard agent and obtain rules, scripts, and patches. |
| YaraSlave | This module corresponds to the Yara engine used to check binary files, which is a commercial virus detection engine. |
| AegisCloudavira | This module corresponds to the Avira engine used to check binary files, which is a commercial virus detection engine. |
| AegisCloudavbd | This module corresponds to the Bitdefender engine used to check binary files, which is a commercial virus detection engine. |
| AegisImageAnalyzer | This module corresponds to the image scan feature. |
| Dipper | This module corresponds to the big data compute engine that is used to detect intrusions. |

**Client side**

The following table describes the server processes that correspond to the modules of the client side.

| Process name | Description |
|---|---|
| SasJenkinsPlugin | The Jenkins plug-in used for image scans, which pulls up the SasImageScanner container. |
| SasImageScanner | The container process that is used to implement the image scan feature. |
| AliYunDun | A core process that is used to establish connections with Server Guard. |

| AliYunDunUpdate | A core process that is used to periodically check whether the Server Guard agent needs to be updated. |
|---|---|
| AliNet | The container process that is used to implement the container firewall feature. |

**Note**

Operating systems supported by the Server Guard agent Operating systems supported by AliNet

### 1.2 High availability

**High-availability server side**

> **Note:** High availability is delivered by using stateless applications.

The server side of Container Security Service (CSS) consists of stateless applications and implements load balancing based on virtual IP addresses (VIPs) and Dubbo to ensure service availability. The server side is stateless. If you have at least two physical machines, service availability is ensured when one physical machine runs as expected. Data is stored in middleware such as Diamond and MetaQ or cloud services such as MiniRDS, Simple Log Service, Object Storage Service (OSS), and Tair. The middleware and cloud services provide high data storage availability. CSS provides API operations that can be called over HTTPS and implements load balancing based on domain names and VIPs to ensure service availability. Service calls in CSS depend on the Dubbo microservices framework. Software-based load balancing of Dubbo ensures service availability.

| Third-party Application User Server Guard Ag VIP DNS |   |
|---|---|
| Aegisbiz Aegisbiz SasContainerService SasContainerService Dubbo SasContainerNetwork SasContainerNetwork AegislmageAnalyzer AegislmageAnalyzer ...... ...... Physical Machine Physical Machine |   |
| MiniRDS OSS Tair MetaQ Cloud Storage Middleware Base Resource |   |

|   | VIP |   |
|---|---|---|

### 1.3 Disaster recovery and backup

**Zone-disaster recovery**

> **Note:** Zone-disaster recovery is delivered by using the active-active mode.

The zone-disaster recovery architecture of Container Security Service (CSS) follows the rules of the active-active mode. In this architecture, disaster recovery is ensured by cloud storage services or middleware.

| Data Ingress Data Ingress Primary/Secondary Primary/Secondary Network VIP VIP Netwo SasContainerService Aegisbiz SasContainerService Aegisbiz Active-active Server Serve Guard Guar AegisimageAnalyzer ...... AegisimageAnalyzer ...... MiniRDS MiniRDS Primary/Secondary Cloud OSS OSS Cloud Storage Storage OSS OSS Tair MetaQ Tair MetaQ Active-active Middleware Middlew Diamond Dubbo Diamond Dubbo Primary Data Center Secondary Data Center |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| Network VIP SasContainerService Aegisbiz Server Guard AegisimageAnalyzer ...... MiniRDS Cloud OSS Storage OSS Tair MetaQ Middleware Diamond Dubbo Primary Data Center |   |   |   |   |   |   |   | ary/Secondary |   |   |
|   |   |   |   |   |   |   | Prim | ary/Secon | dary |   |
|   | Network VIP |   |   |   |   |   | Prim | ary/Secondary VIP Netw |   |   |
|   | SasContainerService Aegisbiz Server Guard AegisimageAnalyzer ...... |   |   |   |   |   | Acti | SasContainerService Aegisbiz ve-active Serv Gua AegisimageAnalyzer ...... |   |   |
|   |   | MiniRDS Cloud OSS Storage OSS |   |   |   |   | Prim | MiniRDS ary/Secondary OSS Clo Stor OSS |   |   |
|   | Tair MetaQ Middleware Diamond Dubbo |   |   |   |   |   | Acti | Tair MetaQ ve-active Middle Diamond Dubbo |   |   |

| rk | VIP |   |
|---|---|---|

|   | VIP |   |
|---|---|---|

The following table describes the disaster recovery solution in each component.

| Component | Solution |
|---|---|
| Container security | The active-active deployment strategy depends on middleware and Object Storage Service (OSS) to ensure data consistency. |
| DNS | Anycast VIPs are used to isolate traffic between the primary and secondary data centers. |
| VIP | BGP routing is used to implement primary/secondary switchover. |
| MiniRDS | Secondary databases synchronize data from the primary databases based on binary logs. |
| SLS | Data synchronization is implemented based on backups in OSS. |
| OSS | Data synchronization between the primary and secondary data centers is supported. |
| Middleware | The active-active deployment strategy depends on MiniRDS to ensure data consistency. |

**Geo-disaster recovery**

> **Note:** Geo-disaster recovery is delivered based on independent regions.

The multi-region architecture of CSS follows the rules of independent regions. General regions do not depend on the central region, and data is completely isolated from services.

### 1.4 Monitoring and alerting

**System metrics**

System monitoring of Container Security Service (CSS) is connected to the TianjiMon console.

**Important**

> **Note:** The alerting feature is not enabled for versions earlier than Apsara Stack V3.17.1. This section describes the monitoring metrics of applications.


**aegisbiz**

| Metric name (TianjiMon) | Monitored object | Metric description | Alert threshold | Alert descriptio n |
|---|---|---|---|---|

| aegisbiz cpu container host _ _ _ | CPU utilization (Single machine) | CPU utilization. | util avg > _ 95 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
|---|---|---|---|---|
| aegisbiz cpu container serv _ _ _ errole | CPU utilization (Server role) |   |   |   |
| aegisbiz cpu container clust _ _ _ er | CPU utilization (Cluster) |   |   |   |
| aegisbiz memo container ho _ _ _ st | Memory usage (Single machine) | Maximum and average memory usage. | util avg > _ 90 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegisbiz memo container se _ _ _ rverrole | Memory usage (Server role) |   |   |   |
| aegisbiz memo container cl _ _ _ uster | Memory usage (Cluster) |   |   |   |
| aegisbiz load container host _ _ _ | Load (Single machine) | Maximum and average CPU loads (Load 1, Load 5, and Load 15). | load1 av _ g > 1 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegisbiz load container serv _ _ _ errole | Load (Server role) |   |   |   |
| aegisbiz load container clus _ _ _ ter | Load (Cluster) |   |   |   |
| aegisbiz tcp conns containe _ _ _ r host _ | Number of TCP connections (Single machine) |   |   |   |

|   |   | Contai tions a | ner Security nd Maintena M d | Service Oper nce Guide·O ocumentatio |
|---|---|---|---|---|
|   |   | Maximum and average number of TCP connections. | None | None. |
| aegisbiz tcp conns containe _ _ _ r serverrole _ | Number of TCP connections (Server role) |   |   |   |
| aegisbiz tcp conns containe _ _ _ r cluster _ | Number of TCP connections (Cluster) |   |   |   |
| aegisbiz ntp container host _ _ _ | NTP (Single machine) | NTP. | None | None. |
| aegisbiz ntp container serve _ _ _ rrole | NTP (Server role) |   |   |   |
| aegisbiz ntp container clust _ _ _ er | NTP (Cluster) |   |   |   |
| aegisbiz process count cont _ _ _ ainer host _ | The number of processes (Single machine) | Maximum and average number of processes. | process n _ umber m _ ax > 100 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegisbiz process count cont _ _ _ ainer cluster _ | The number of processes (Server role) |   |   |   |
| aegisbiz process count cont _ _ _ ainer host _ | The number of processes (Cluster) |   |   |   |
| aegisbiz nginx container ho _ _ _ st | NGINX QPS (Single machine) | Queries per second (QPS) processed by NGINX. | None | None. |
| aegisbiz nginx container ser _ _ _ verrole | NGINX QPS (Server role) |   |   |   |
| aegisbiz nginx container clu _ _ _ ster | NGINX QPS (Cluster) |   |   |   |

| aegisbiz health container ho _ _ _ st | Health check (Single machine) | Application starts as expected. | health > 0 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
|---|---|---|---|---|
| aegisbiz health container se _ _ _ rverrole | Health check (Server role) |   |   |   |
| aegisbiz health container cl _ _ _ uster | Health check (Cluster) |   |   |   |

**aegis-metadata**

| Metric name (TianjiMon) | Monitored object | Metric description | Alert threshold | Alert descriptio n |
|---|---|---|---|---|
| aegismetadata cpu containe _ _ r host _ | CPU utilization (Single machine) | CPU utilization. | util avg > _ 95 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegismetadata cpu containe _ _ r serverrole _ | CPU utilization (Server role) |   |   |   |
| aegismetadata cpu containe _ _ r cluster _ | CPU utilization (Cluster) |   |   |   |
| aegismetadata memo contai _ _ ner host _ | Memory usage (Single machine) | Maximum and average memory usage. | util avg > _ 90 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegismetadata memo contai _ _ ner serverrole _ | Memory usage (Server role) |   |   |   |
| aegismetadata memo contai _ _ ner cluster _ | Memory usage (Cluster) |   |   |   |

| aegismetadata load contain _ _ er host _ | Load (Single machine) | Maximum and average CPU loads (Load 1, Load 5, and Load 15). | load1 av _ g > 1 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
|---|---|---|---|---|
| aegismetadata load contain _ _ er serverrole _ | Load (Server role) |   |   |   |
| aegismetadata load contain _ _ er cluster _ | Load (Cluster) |   |   |   |
| aegismetadata tcp conns co _ _ _ ntainer host _ | The number of TCP connections (Single machine) | Maximum and average TCP connections. | None | None. |
| aegismetadata tcp conns co _ _ _ ntainer serverrole _ | The number of TCP connections (Server role) |   |   |   |
| aegismetadata tcp conns co _ _ _ ntainer cluster _ | The number of TCP connections (Cluster) |   |   |   |
| aegismetadata ntp containe _ _ r host _ | NTP (Single machine) | NTP. | None | None. |
| aegismetadata ntp containe _ _ r serverrole _ | NTP (Server role) |   |   |   |
| aegismetadata ntp containe _ _ r cluster _ | NTP (Cluster) |   |   |   |

| aegismetadata process coun _ _ t container host _ _ | The number of processes (Single machine) | Maximum and average number of processes. | process n _ umber m _ ax > 100 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
|---|---|---|---|---|
| aegismetadata process coun _ _ t container cluster _ _ | The number of processes (Server role) |   |   |   |
| aegismetadata process coun _ _ t container host _ _ | The number of processes (Cluster) |   |   |   |
| aegismetadata nginx contai _ _ ner host _ | NGINX QPS (Single machine) | The number of QPS processed by NGINX. | None | None. |
| aegismetadata nginx contai _ _ ner serverrole _ | NGINX QPS (Server role) |   |   |   |
| aegismetadata nginx contai _ _ ner cluster _ | NGINX QPS (Cluster) |   |   |   |
| aegismetadata health contai _ _ ner host _ | Health check (Single machine) | Application starts as expected. | health > 0 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegismetadata health contai _ _ ner serverrole _ | Health check (Server role) |   |   |   |
| aegismetadata health contai _ _ ner cluster _ | Health check (Cluster) |   |   |   |

**aegis-image-analyzer**

| Metric name (TianjiMon) | Monitored object | Metric description | Alert threshold | Alert descriptio n |
|---|---|---|---|---|

| aegisimageanalyzer cpu con _ _ tainer host _ | CPU utilization (Single machine) | CPU utilization. | util avg > _ 95 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
|---|---|---|---|---|
| aegisimageanalyzer cpu con _ _ tainer serverrole _ | CPU utilization (Server role) |   |   |   |
| aegisimageanalyzer cpu con _ _ tainer cluster _ | CPU utilization (Cluster) |   |   |   |
| aegisimageanalyzer memo c _ _ ontainer host _ | Memory usage (Single machine) | Maximum and average memory usage. | util avg > _ 90 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegisimageanalyzer memo c _ _ ontainer serverrole _ | Memory usage (Server role) |   |   |   |
| aegisimageanalyzer memo c _ _ ontainer cluster _ | Memory usage (Cluster) |   |   |   |
| aegisimageanalyzer load co _ _ ntainer host _ | Load (Single machine) | Maximum and average CPU loads (Load 1, Load 5, and Load 15). | load1 av _ g > 1 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegisimageanalyzer load co _ _ ntainer serverrole _ | Load (Server role) |   |   |   |
| aegisimageanalyzer load co _ _ ntainer cluster _ | Load (Cluster) |   |   |   |
| aegisimageanalyzer tcp con _ _ ns container host _ _ | The number of TCP connections (Single machine) | Maximum and average number of TCP connections. | None | None. |
| aegisimageanalyzer tcp con _ _ ns container serverrole _ _ | The number of TCP connections (Server role) |   |   |   |
| > Document Version: 20250613 |   |   |   | 1 |

|   |   | Alibab | a Cloud Secu ard Adv | rity-Server G anced Editio |
|---|---|---|---|---|
| aegisimageanalyzer tcp con _ _ ns container cluster _ _ | The number of TCP connections (Cluster) |   |   |   |
| aegisimageanalyzer ntp con _ _ tainer host _ | NTP (Single machine) | NTP. | None | None. |
| aegisimageanalyzer ntp con _ _ tainer serverrole _ | NTP (Server role) |   |   |   |
| aegisimageanalyzer ntp con _ _ tainer cluster _ | NTP (Cluster) |   |   |   |
| aegisimageanalyzer process _ count container host _ _ _ | The number of processes (Single machine) | The maximum and average number of processes. | process n _ umber m _ ax > 100 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
| aegisimageanalyzer process _ count container cluster _ _ _ | The number of processes (Server role) |   |   |   |
| aegisimageanalyzer process _ count container host _ _ _ | The number of processes (Cluster) |   |   |   |
| aegisimageanalyzer nginx c _ _ ontainer host _ | NGINX QPS (Single machine) | The number of QPS processed by NGINX. | None | None. |
| aegisimageanalyzer nginx c _ _ ontainer serverrole _ | NGINX QPS (Server role) |   |   |   |
| aegisimageanalyzer nginx c _ _ ontainer cluster _ | NGINX QPS (Cluster) |   |   |   |

| aegisimageanalyzer health c _ _ ontainer host _ | Health check (Single machine) | Application starts as expected. | health > 0 | The number of consecuti ve alerts is 3. The silence duration is 300 seconds. The probe interval is 60 seconds. |
|---|---|---|---|---|
| aegisimageanalyzer health c _ _ ontainer serverrole _ | Health check (Server role) |   |   |   |
| aegisimageanalyzer health c _ _ ontainer cluster _ | Health check (Cluster) |   |   |   |

**Note**

System monitoring of Server Guard is reused. For more information, see https://aliyuque.antfin.com/aegisgroup/scxr0h/du1is5#LSZ9W.

**Business metrics**

System monitoring of CSS is implemented based on TianjiMon. The following table describes the metrics.

| Module | Metric name | Description |
|---|---|---|
| Container management | Number of nodes | Statistics on the number of nodes in all dimensions of a container cluster |
|   | Number of applications | Statistics on the number of applications in all dimensions of a container cluster |
|   | Number of pods | Statistics on the number of pods in all dimensions of a container cluster |
|   | Number of containers | Statistics on the number of containers in all dimensions of a container cluster |
|   | Number of images | Statistics on the number of images in all dimensions |
|   | Number of image scan tasks | Number of image scan tasks that are created |
|   | Number of image scan layers | Number of image layers that are scanned |

| ontainer Security Service ions and Maintenance Gui M documentation |   |   |
|---|---|---|
| Image scan |   |   |
|   | Number of image scan results | Monitoring of the number of image scan results |
|   | Duration of image pre- analysis | Time consumed for image scan pre-analysis in each dimension |
|   | Duration of image analysis | Time consumed for image scan analysis in each dimension |
|   | Duration of image analysis for manifests | Time consumed for image scan analysis of manifests in each dimension |
| CICD | Number of times that Jenkins rules are pulled | Number of times that Groovy rules are pulled during image scans in Jenkins |
|   | Duration of rull pulling in Jenkins | Time consumed for pulling Groovy rules during image scans in Jenkins |
|   | Number of times that Jenkins scan results are reported | Number of times that Jenkins scans images and reports results |
|   | Duration of reporting Jenkins scan results | Time consumed for reporting scan results after image scans in Jenkins are complete |
| Container firewall | Number of container network logs that are consumed | Number of messages that are consumed by Dipper for container network visualization |
|   | Time consumed for processing container network logs | Time consumed by Dipper for container network visualization |
|   | Number of blocks by using the container firewall feature | Numbers alerts and blocks by using the container firewall feature |
| Container runtime protection | Number of container Linux vulnerabilities | Number of container Linux vulnerabilities |
|   | Number of container application vulnerabilities | Number of container application vulnerabilities |
|   | Number of container alerts | Number of container alerts |

### 1.5 XC

**Difference between Apsara Stack and controllable capabilities**

The difference between Apsara Stack and controllable capabilities is caused by different platforms. Apsara Stack x86 and Hygon x86 have the same capabilities. The capabilities of Phytium ARM and Kunpeng ARM differ from Apsara Stack by less than 30%, and plans are in place to align them in the future. The capabilities of ShenWei differ from Apsara Stack x86 by less than 50%, and no plans exist to align them in the future.

**Differences in container security capabilities**

| Feature | x86 | AR M | Sh en We i | Description |
|---|---|---|---|---|
| Overvie w | 100 % | 100 % | 100 % | This feature displays assets, vulnerabilities, exceptions, configuration defects, and events that require attention. |
| Containe r manage ment | 100 % | 100 % | 100 % | This feature provides information about the security status of containers. You can view the security status, groups, virtual private clouds (VPCs) of servers. You can also view the numbers of all servers, at-risk servers, unprotected servers, inactive servers, and new servers. You can click the name of a server to view the server details, including vulnerabilities, alerts, baseline check results, and asset fingerprint investigation. |

| Image scan and CI/CD scan | 100 % | 90 % | 80 % | The vulnerability detection feature detects Linux software vulnerabilities and application vulnerabilities. The feature provides details of vulnerabilities. You can use the quick scan feature. The baseline check feature automatically checks for risks related to the operating systems, accounts, databases, passwords, and security compliance configurations of your servers, and provides reinforcement suggestions. The malicious sample detection feature detects and removes virus and webshell. The system automatically detects and removes common trojan viruses, ransomware, mining viruses, and DDoS trojans. Important Capability differences Specific independent and controllable operating systems are not supported and must be adapted by using rule packages. Avira and Bitdefender detection engines are not supported by ARM. Only Graph Learning Engine (GLE) is supported. ShenWei does not support an engine. |
|---|---|---|---|---|
| Containe r firewall | 100 % | 0% | 0% | The container firewall feature is provided by Container Security Service (CSS) to ensure the security of container environments. If attackers exploit vulnerabilities or malicious images to intrude into clusters, the container firewall feature generates alerts or blocks attacks. Important Differences in capabilities: ARM and ShenWei do not support AliNet. No alerts are generated, and abnormal behavior is not blocked if you use ARM or ShenWei. |
| Containe r runtime protectio n | 100 % | 80 % | 50 % | This feature displays the information about alerts for affected cluster nodes in a centralized manner, including the number of servers on which alerts are generated, the total number of unhandled alerts, and alerts that require urgent handling. The alert types include abnormal process behavior, webshell, unusual logon, malicious process (cloud detection and removal), sensitive file tampering, abnormal network connection, persistent webshell, and web application threat detection. Important Differences in capabilities: Avira and Bitdefender detection engines are not supported by ARM. Only GLE is supported. ShenWei does not support an engine. |
| Log query | 100 % | 100 % | 100 % | This feature allows you to query logs for logon, brute-force attacks, process snapshots, network connections, listening port snapshots, account snapshots, and process startup. |

**Adaptation information of modules**

| Module | x86 (Apsara Stack and Hygon) | ARM (Phytium and Kunpeng) | ShenWei |
|---|---|---|---|
| Client | 100% | 50% (AliNet is not supported.) | 50% (AliNet is not supported.) |
| Server | 100% | 100% | 100% |
| Frontend | 100% | 100% | 100% |
| Compute engine | 100% | 100% | 100% |
| Detectio n engine | 100% | 50% (Avira and Bitdefender engines are not supported.) | 0% (No detection engine is supported.) |

**Multi-chip architecture in one cloud**

Multi-chip architecture in one cloud is commonly suitable for two scenarios: heterogeneous zone-disaster recovery (hardware heterogeneity at the data center level for primary and backup data centers) and heterogeneous multi-region deployment (hardware heterogeneity at the central/unit data center level). The following table describes the scenarios that are supported with CSS.

| Scenario | Supported |
|---|---|
| Heterogeneous zone-disaster recovery (x86 and ARM) Hardware heterogeneity at the data center level for primary and backup data centers | Yes (Specific capabilities do not take effect in the ARM data center, such as proactive defense and self-protection.) |
| Heterogeneous multi-region deployment ((x86 and ARM)) Hardware heterogeneity at the central/unit data center level | Yes |

### 1.6 Hot upgrade

Container Security Service (CSS) supports hot upgrade by default. No additional O&M operations are required.

### 1.7 AliNet (06_21) Linux Driver OS / Kernel List

**/ Kernel List**

**Supported system versions**

| Linux major version | Linux minor version |
|---|---|
| CentOS6 | 6.5, 6.6, 6.7, 6.8, 6.9, 6.10 |
| CentOS7 | 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9 |
| CentOS8 | 8 |
| Ubuntu14 | 14.04 |
| Ubuntu16 | 16.04 |
| Ubuntu18 | 18.04 |
| Ubuntu20 | 20.04 |
| AliYunLinux | 2.1903, 17.01, 3 |
| ANOLIS | 7.9,8.4 |

**Kernel versions**

| Linux | Kernel version | Remarks |
|---|---|---|

| CentOS | 2.6.32 3.10.0 4.18.0 4.19.104 5.4.8 5.4.42 | For kernel versions that start with 3.10.0-123, special match is supported. For kernel versions that start with 4.18.0, exact match is supported. ( 4.18.0-147.5.1.el8 1.x86 64 _ _ 4.18.0-193.14.2.el8 2.x86 64 _ _ 4.18.0-193.28.1.el8 2.x86 64 _ _ 4.18.0-240.15.1.el8 3.x86 64 _ _ 4.18.0-240.22.1.el8 3.x86 64 _ _ 4.18.0-305.3.1.el8.x86 64 _ 4.18.0-305.10.2.el8 4.x86 64 _ _ 4.18.0-305.19.1.el8 4.x86 64 _ _ 4.18.0-348.2.1.el8 5.x86 64 _ _ 4.18.0-348.7.1.el8 5.x86 64 _ _ 4.18.0-358.el8.x86 64 _ 4.18.0-365.el8.x86 64 _ 4.19.104-300.el7.x86 64 _ 5.4.8-1.el7.elrepo.x86 64 _ 5.4.42-200.el7.x86 64) _ |
|---|---|---|
|   | 3.13.0-32-generic 3.13.0-86-generic 4.4.0-62-generic 4.4.0-63-generic 4.4.0-93-generic 4.4.0-96-generic 4.4.0-104-generic 4.4.0-117-generic 4.4.0-124-generic 4.4.0-142-generic 4.4.0-146-generic 4.4.0-151-generic 4.4.0-170-generic 4.4.0-174-generic 4.4.0-179-generic 4.4.0-184-generic 4.4.0-185-generic 4.4.0-210-generic 4.15.0-13-generic 4.15.0-23-generic | Exact match is supported. Example: 3.13.0-32-generic. |

| Ubuntu | 4.15.0-42-generic 4.15.0-45-generic 4.15.0-52-generic 4.15.0-54-generic 4.15.0-72-generic 4.15.0-96-generic 4.15.0-106-generic 4.15.0-109-generic 4.15.0-111-generic 4.15.0-118-generic 4.15.0-124-generic |   |
|---|---|---|
|   | 4.15.0-128-generic 4.15.0-144-generic 4.15.0-147-generic 4.15.0-158-generic 4.15.0-166-generic 4.15.0-169-generic 4.15.0-170-generic 4.15.0-1047-gcp 5.3.0-40-generic 5.4.0-31-generic 5.4.0-42-generic 5.4.0-47-generic 5.4.0-58-generic 5.4.0-73-generic 5.4.0-77-generic 5.4.0-86-generic 5.4.0-91-generic 5.4.0-92-generic 5.4.0-94-generic 5.4.0-100-generic 5.4.0-102-generic 5.4.0-106-generic |   |

| AliYunLinux | 3.10.0-1160.al7.1.x86 64 _ 4.4.95-1.al7.x86 64 _ 4.4.95-3.al7.x86 64 _ 4.19.24-7.al7.x86 64 _ 4.19.24-7.14.al7.x86 64 _ 4.19.81-17.al7.x86 64 _ 4.19.81-17.2.al7.x86 64 _ 4.19.91-19.1.al7.x86 64 _ 4.19.91-21.2.al7.x86 64 _ 4.19.91-21.al7.x86 64 _ 4.19.91-22.2.al7.x86 64 _ 4.19.91-22.al7.x86 64 _ 4.19.91-23.al7.x86 64 _ 4.19.91-24.1.al7.x86 64 _ 4.19.91-25.1.al7.x86 64 _ 4.19.91-25.3.al7.x86 64 _ 4.19.91-25.6.al7.x86 64 _ 4.19.91-25.7.al7.x86 64 _ 5.10.23-5.al8.x86 64 _ 5.10.60-9.al8.x86 64 _ 5.10.84-10.2.al8.x86 64 _ 5.10.84-10.3.al8.x86 64 _ | Exact match is supported. |
|---|---|---|
| Anolis | 3.10.0-1160.an7.x86 64 _ 3.10.0-1062.an7.x86 64 _ 3.10.0- 1160.59.1.0.1.an7.x86 64 _ 4.19.91-25.2.an7.x86 64 _ 4.19.91-25.7.an7.x86 64 _ 4.18.0-348.2.1.an8 4.x86 64 _ _ 4.18.0-348.12.2.an8.x86 64 _ |   |
