---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 50
source_pdf: "70068a962312c0bc_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Contain"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83%EF%BC%88%E5%AE%89%E9%AA%91%E5%A3%AB%EF%BC%89%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Container%20Security%20Service%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Server Guard Advanced Edition Container Security Service Operations and Maintenance Guide 20260828

## Table of Contents

- 1 O&M documentation
  - 1.1 Introduction
    - 1.1.1 Deployment architecture
    - 1.1.2 Core modules
      - 1.1.2.1 Asset Management
      - 1.1.2.2 Container Firewall
      - 1.1.2.3 Mirror Scan
      - 1.1.2.4 Cluster defense
  - 1.2 High availability
  - 1.3 Disaster recovery and backup
  - 1.4 Monitor objects and send alert notifications
  - 1.5 Capacity Planning
  - 1.7 Hot upgrade
  - 1.8 AliNet (06_21) Linux Driver OS / Kernel List

## 1 O&M documentation

### 1.1 Introduction

Container Security Service (CSS) is a centralized management and operations platform for immutable infrastructure to ensure cloud native container security. CSS uses the automatic mode to resolve security issues that occur when containers are constantly integrated, delivered, deployed, and run. CSS uses a cloud-native architecture of Server Guard to provide multiple features such as cloud asset management, baseline check, proactive defense, security hardening, and security status visualization. CSS can efficiently detect and block risks such as container escapes, viruses, attacks, encryption ransomware, and vulnerability exploits. CSS protects runtime nodes, containers, and images in and outside the cloud, and helps you meet regulatory compliance requirements. The feature of container image scan detects high-risk and medium-risk system vulnerabilities, application vulnerabilities, malicious samples, configuration risks, and sensitive data in images. The feature provides suggestions on how to handle these issues and supports end-to-end image risk management. The container firewall feature is provided by CSS to ensure the security of container environments. If attackers exploit vulnerabilities or malicious images to intrude into clusters, the container firewall feature generates alerts or blocks attacks.

#### 1.1.1 Deployment architecture

**Deployment architecture**

**V3.18.1 and earlier**

YundunConsole YundunBaseService AegislmageAnalyzer Lateral foundation capacity Dipper Compute engine Aegisbiz AegisSuspicious SasFileserver

**SasCluster**

Core Capabilities AegisContainerNetwork SasContainerService AegisVirusScan MiniRDS

**Server**

**Side**

AegisVulnerability AegisHealthCheck AegisDetect OSS Detection /Defense Capability SLS YaraSlave AegisMaster AegisCloudavbd MetaQ/Diamond Aegiserver Aegisupdate AegisCloudavira AegisPrivate CloudEngine Tair/SchedulerX Detection Client Management engine

**Middleware**

**BasicThinCluster**

AliYunDun AliYunDunUpdate AliNet sas-jenkins-plugin sas-image-scanner

**Customer**

**household**

**end**

ECS or external host ECS or off-cloud host (ACK or user-created (Jenkins node)

**V3.18.2- V3.18.6(2512 universal)**

YundunConsole YundunBaseService Lateral foundation capacity AegisPrivateCloudEegine Dipper Detection engine Compute engine

**yundun-basic**

MiniRDS Aegisbiz AegisContainerNetwork SasContainerDefense SasContainerService OSS Core Competence SLS AegisHealthCheck AegisVirusScan AegisImageAnalyzer AegisSuspicious MetaQ/Diamond

**Server**

**Side**

AegisVulnerability AegisDetect BanffAegisWeb AegisMatcher Detection /Defense Capability Tair/SchedulerX

**Middleware**

AegisMaster Aegiserver Aegisupdate Client Management

**yundun-css(ageis)**

**Paas Shared Node Pool**

AliYunDun AliYunDunUpdate AliNet sas-jenkins-plugin sas-image-scanner

**Customer**

**household**

**end**

ECS or off-cloud host (ACK or user-created Kubernetes node) ECS or external host (Jenkins node)

**V3.19- V3.18.6(2512limit)**

YundunConsole YundunBaseService Lateral foundation capacity Dipper AegisPrivate CloudEegine Detection engine Compute Engine

**yundun-basic**

MiniRDS Aegis SasContainer SasContainer OSS AegisContainer biz Network Service Defense Core Competence SLS Aegis Aegis Aegis Aegis HealthCheck VirusScan Suspicious ImageAnalyzer MetaQ/Diamond

**Service**

**service**

**end**

Aegis Aegis Banff Vulnerability Matcher AegisWeb Detection and Defense Capabilities Tair/SchedulerX

**Middleware**

AegisMaster Aegis Aegis server update Client Management

**yundun-css(ageis)**

**Paas Shared Node Pool**

AliYunDun AliYunDun AliNet sas-jenkinssas-image-scanner

**Client**

Update plugin

**Side**

ECS Instance or Server Outside Cloud ECS Instance or Server Outside Cloud (ACKorSelf-managedKubernetesNode) (JenkinsNode)

**Versions later than V3.18.6(2512limit)**

YundunConsole YundunBaseService

**Lateral foundation**

**capacity**

Dipper AegisPrivate CloudEegine

**Detection engine**

**Compute Engine**

**yundun-basic**

MiniRDS SasContainer SasContainer Aegisbiz AegisContainer OSS Network Service Defense

**Core Competence**

SLS AegisSuspicious AegisHealthCheck AegisVirusScan AegisImage Analyzer MetaQ/Diamond

**Service**

**service**

**end**

AegisMatcher AegisVulnerability BanffAegisWeb

**Detection /Defense**

Tair/SchedulerX

**Capability**

**Middleware**

Aegisupdate AegisMaster Aegiserver

**Client Management**

**yundun-css(ageis)**

**Paas Shared Node Pool**

deamonsetsas-image- AliYunDun AliYunDun AliNet sas-jenkins-

**Customer**

Update docker plugin scanner

**household**

**end**

ECS or off-cloud host ECS or external host (ACK or user-created (Jenkinsnode) Container security, reuse Server Guard detection capabilities, including the server and client two modules. Server: manages container clusters and image assets on and off the cloud, and provides core capabilities such as detection and defense. Client side: reports the running status of container clusters and nodes in real time, and provides running detection and network blocking capabilities.

**Server side**

The server side consists of the following types of modules: Lateral basic capabilities: the common capabilities of Apsara Stack Security services, which can be used in consoles or by calling API operations. Core capabilities: asset management, alerting, and file collection. Detection and defense: detection of and defense against vulnerabilities and baseline risks, and protection of files, networks, and processes. Detection engines: the commercial virus detection engines, a self-developed virus detection engine, and a big data computing engine. Client management: manages client connections, updates the status of container clusters, and delivers configuration rules. The following table describes modules of the server side.

| Module | Responsibilities |
|---|---|
| YundunConsole | The console provides a unified management interface for security administrators. |
| YundunBaseService | API Gateway, which opens host security capabilities to third- party developers. |
| AegisSuspicious | Intrusion alert events and application whitelists. |
| Aegisbiz | Manage the assets of container clusters and images inside and outside the cloud. |
| SasFileserver | This module corresponds to the file collection feature. |
| AegisContainerNetwork (AegisMetaData) | This module corresponds to the network visualization and container firewall features. |
| SasContainerService (NewSas) | This module corresponds to the image plug-in scan feature. |
| SasContainerDefence (NewSas) | This module corresponds to the active defense for containers feature. |
| AegisHealthCheck | This module corresponds to the baseline check feature. |
| AegisVirusScan | File detection. |
| AegisDetect | In the old version of file detection, only file whitelist management is retained. All other processes are migrated to AegisVirusScan. |
| AegisDefence | Tamper-proof. |
| AegisVulnerability | Vulnerability detection. |
| AegisPrivateCloudEngine | The GLE engine is a virus detection engine developed by Alibaba. |
| AegisMaster | Client configuration and plug-in management. |

| Aegiserver | Client connection management, configuration delivery, and message forwarding. |
|---|---|
| Aegisupdate | Files such as customer order upgrades, rules /scripts /patches are pulled. |
| YaraSlave | Yara binary detection engine, a commercial virus detection engine. |
| AegisCloudavira | Red umbrella binary engine, commercial virus detection engine. |
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
| AliNet | The container process that is used to implement the container firewall feature. |

**Note**

Operating systems supported by the Server Guard agent Operating systems supported by AliNet

#### 1.1.2 Core modules

##### 1.1.2.1 Asset Management

The Container Security Asset Center allows you to view the security protection status of managed assets, such as container clusters and images.

**Supported asset types**

Cloud assets: Container Service for Kubernetes (ACK) and Container Registry (Container Registry) Assets outside the cloud: self-built kubernetes,quay image repository, harbor image repository, and Jenkins image

**Core Process**

**Asset synchronization**

Obtain ACK and ACR data by using OpenAPI. Access user-created Kubernetes: V3.18.6-2512 the-limit version and earlier to obtain the data of user-created Kubernetes and user-created image warehouses through directional access. In versions later than V3.18.6-2512-limit, you can run the YAML command on the master node of the self-managed cluster and obtain the cluster information by using the client. The container cluster asset updates the container status in real time based on the container change messages reported by the client.

**V3.18.6-2512-limit version and earlier core process**

Self-built image warehouse
1. Use the webhook to
notify you of changes to the image asset. Synchronize assets
1. Synchronize assets
outside the cloud through reverse access Synchronize assets in the cloud user-created Kubernetes apis user-created image Asset changes repository apis

**Aegisbiz**

3. Broadcast container
asset change information
1. Call OpenAPI to
synchronize ACK assets

**Service**

2. Forward container

**Service**

change information

**End**

Listen for container ACK control

**Aegiserver**

change ACK control messages and send Other applications
1. The client reports
container change information. AliYunDun AliYunDun

**Customer**

**Household**

**End**

ACR node user-created Kubernetes cluster node Interface Access metaq notification

**V3.18.6 -2512-limit later version core process**

|   | Self-built image |   |
|---|---|---|
| 1. Use the webhook to not | ify yowu aorfe chhoanugsees to th | e image asset. |

Synchronize assets

| 1. | Configure access to a m | anaged image cluster |
|---|---|---|

outside the cloud Synchronize assets in the cloud image managed set group access information Asset changes

**Aegisbiz**

| 1. Call OpenAPI to synchron | ize ACK assets |
|---|---|

**Service**

| 3. Broadcast container asset change info | r2m. Faotirown | ard container change informatio | n |
|---|---|---|---|

**Service**

**End**

Listen for ACK control container change

**Aegiserver**

messages and send ACK control Other applications
2. Run the YAML of the man
1. The client reports container change information.
AliYunDun AliYunDun

**Customer**

**Household**

**End**

ACR node user-created Kubernetes cluster node Interface Access metaq notification

**Access process for external assets**

Through reverse access, the container security server can access the user VPC network from the control area to request the mirror warehouse api and Kubernetes apiServer. In IDC scenarios, off-cloud assets may be integrated into container security management by using the grid connection method. image repository K8S apiServer image repository api api

| Grid c | onn | ection |
|---|---|---|

ECS ECS ECS User VPC User VPC

|   | Reverse access |
|---|---|
|   | Download an image through reverse access |
| Obtain the manifest Download layer AegisImageA |   |

Obtain information about Kubernetes clusters and image assets through reverse access Synchronize assets outside the cloud Control area

**Core process of container network topology**

The network logs of containers are marked as in and out traffic. Combined with the network link logs, after dipper processing, the east-west traffic between containers, the public network, and the north-south traffic between containers are retained and presented in the topology diagram. east-west traffic: the in and out log time intervals are within a specific range, and the quintet (source ip, source port, destination ip, destination port) of the two logs exactly match. north-south traffic: the time interval between in and out logs is within a specific range, and either the source ip address or the destination ip address can be traced to the public ip address Match interval: The exact match time is 60 seconds, and the service mode time is 10 seconds. Consume matched network logs Obtain container asset information

**Service**

**Service**

Assembled topology

**End**

AegisContainerNetwork Aegisbiz sls Network logs after matching Pairing Network Log

| Networ | k logs after matchin |
|---|---|

Dipper Report in and out network logs

| Pairing network log ECS |   |   | Pairing network log unication Off-cloud |
|---|---|---|---|
|   | Network comm | Network comm | unication |

**Customer**

**Household**

**End**

hosts

##### 1.1.2.2 Container Firewall

Container Firewall is a firewall service provided by Container Security for container environments and is a core feature of Container Security run time protection. Combined with container network visualization, configure reasonable isolation rules. When hackers exploit vulnerabilities or malicious images to invade a container cluster, the container firewall will alert or intercept abnormal behaviors, which can control risks within a small range and prevent the entire container environment from being invaded.

**Network object description**

compared with hosts, containers and pods have a short lifetime and drift between different nodes. you cannot configure rules based on fixed ip addresses and ports. therefore, you need to define additional network objects for firewall isolation rules. The user's isolation rules are to be configured on the IP,DNS, or pod,namespace, image, and label of the container. The IP address, DNS address, and isolation rules between images and tags must be matched in real time when the container instance is started.

| Object Type | Property Name | Description | Remarks |
|---|---|---|---|
|   | Namespace | The namespace that is defined in the cluster. | Tag: kubernetes.io/metadata.name: <namespace> |

| libaba Cloud Se rd Advanced Ed |   |   |   |
|---|---|---|---|
| Container |   |   |   |
|   | Application Name | Tags defined within each application (app) | The essence is a custom label app: <application name>. ack is marked with app: by default. , self-built Kubernetes need to define the label, otherwise, the corresponding application will not be selected when defining the network object. |
|   | Image | Image Name |   |
|   | Label | Custom tags |   |
| IP | IP | Separate multiple IP addresses or CIDR blocks with commas (,). You can specify up to 50 IP addresses or CIDR blocks. |   |
| DNS domain name | DNS domain name | The configured domain names are resolved to IP addresses (up to 500) through DNS, and these IP addresses are RAM. |   |

**Core Process**

AliYunDun AliYunDun Container Container start events start events and and container container metadata metadata notifications notifications AliNet Business AliNet Business Container A Container B Deliver the initiate tcp, Source Issue Issue Final syn destination container container container syn, and message container blocking outreach blocking after kernel instance instance information rules requests rules filtering information AliSecNetFilter AliSecNetFilter The payload syn that carries message the active carrying container active information container information Network
1. configure firewall rules: the configuration and blocking functions of the container firewall
completely depend on the alinet plug-in. the status of the alinet plug-in is verified before the container firewall function is enabled. if the alinet plug-in is not installed or the heartbeat of the alinet plug-in is abnormal, the container firewall function cannot be enabled.
2. Issue firewall rules: The aliNet plug-in records the container status and metadata of the
current node, and accepts firewall rules issued by the server.
3. Allows, alerts, and blocks network traffic: The aliNet neutron plug-in aliSecNetFilter enables,
alerts, and blocks traffic that hits rules based on the recorded container metadata and firewall rules.

##### 1.1.2.3 Mirror Scan

The image security scan feature can detect high and high risk system vulnerability, application vulnerabilities, malicious samples, and configuration risks in images.

**Supported scan image types**

In-cloud image type: defaultACR, Enterprise Edition ACR Image types outside the cloud: quay,harbor, and images built by jenkins

**Support for scanning risky content**

**Vulnerabilities**: system vulnerability (cve) and application vulnerabilities (sca)

**Baseline:**

Identity Authentication Make sure that no duplicate usernames or UIDs exist Make sure that no account has the same password hash Make sure that no account with an empty password exists in the system Ensure that a strong password hashing algorithm is used Ensure root is the only account with UID 0 Make sure that no duplicate user groups or GIDs exist Unauthorized access CouchDB unauthorized access configuration risk Risk of unauthorized access to Elasticsearch PostgreSQL unauthorized access configuration risk Jenkins unauthorized access configuration risk Risk of unauthorized access to Hadoop Weak password Tomcat weak password configuration Configure weak passwords for ApsaraDB for Redis rsync weak password configuration svn weak password configuration Service configuration Make sure that the openssh service is not installed
**Malicious samples:** webshells, binary files, such as trojans, ransomware, mining viruses,
and backdoor programs

**Scan process**

**Image scan for periodic tasks**

You can use the image scan settings to scan images from a specified image repository within a specified period.

| Generate a 1. Issue scan task periodic task Update scan progress Update image security information Aegisbiz Obtain 2. Query the manifest Each stage reports the image scan progress Download 3. Download the i Vulnerability the 6. Query image securityr iunlfeosrmation image layer 4. Concurrent execution of groovy parsing scripts Report vulnerability 5. List ofObtain a list of To perform a Obtain a list information software pascokftawgaeres packages baseline scan of files Groovy parsing script Aegis execution Vulnerability Aegis ImageAnalyzer 5. Trigger file detection Record baseline check results 5. Report baseline check results Aegis HealthCheck Determine whether the file is ready Record alarm Push Engine information scI am va ug le n ec rv ae b a iln itd ies Aegis Suspicious Aaegis VirusScan | the image manifest. Image repository mage layer 5. Upload the file to OSS. OSS Detection engine |
|---|---|

| 2. Query | 2. Query | the image manifest. |
|---|---|---|
| nload the i |   | mage laye |

|   |   | Vulnerability ge securityr iunlfeosrmation |
|---|---|---|
| 6. Q | uery ima | Vulnerability ge securityr iunlfeosrmatio |

**Webhook Image Scan**

acr images and user-created image repositions can use webhooks to report image changes, create a single-cycle image scan task, and immediately run tasks to scan images.

**Image scan of Jenkins plug-ins**

OpenApi requests

| Http req | uest |
|---|---|

SasImagerPlugin
1. Download the
SasImageScanner image JenKins

**docker images**

2. Load the
SasImageScanner image
3. Start the image
scan container. Save the image to your local computer Decompress the Update scan tar image
4. Image
task status preprocessing
5. Download
the

| Obtai dete | n the groovy ction script |   |
|---|---|---|
|   |   | cript |

groovy script upload files Obtain a list Obtain a list of To perform a to oss software packages baseline scan of files
6. Concurrent execution of
groovy parsing scripts Client

|   | temporary upload oss url |
|---|---|

SasImageScanner container Server Query Obtain the groovy temporary scripts upload url. Update scan Aegisbiz progress
7. Report script
OSS filtering results Filtering results of distributed images SasContainerService
8. Report File
8. Report package
8. Report baseline
Filtering List filtering list check results Lifecycle tasks Vulnerability Determine whether rules Record baseline the file is ready check results Update scan Report vulnerability Push Engine progress information Aegis HealthCheck Update image security information Aegisbiz AegisVulnerability AegisVirusScan
9. Query image
security information Engine detection result Record alarm information Image cve and sca vulnerabilities AegisSuspicious Detection engine

##### 1.1.2.4 Cluster defense

**Container file defense**

This feature is a basic service of container protection. The cluster must be connected to container security, and the operating system and kernel version must be supported. You can create file defense rules to implement fine-grained file-level protection by specifying the paths to be protected, the types of files to be included or excluded, the actions to be executed (alerts or block), and the whitelist process. The following figure shows the flowchart of container file defense: Container tamper-proofing architecture Process whitelist Rule application Alert management Rule management Directory management management management POP Internal VPC cloud sas-container-defense aegis-suspicious Rule delivery / Alert reporting plug-in installation Internal cloud aegis-master aegis-server Rule delivery / Alert reporting plug-in installation aegis-client

**Active defense for containers**

This feature detects security risks during container startup or run time from multiple perspectives: image security, run time security, and runtime environment security. By configuring corresponding rules, you can block the running of risky images, stop untrusted processes, and block container escapes to improve the security level of the overall container runtime environment. This topic describes how to configure risky image blocking, non-image program defense, and container escape protection rules.

| Rule Type | Rule description | Remarks |
|---|---|---|

| Block risky images | After you create a risky image blocking rule, Container Security checks the security of the image when you create resources from the image in the specified cluster. If the image that matches the risky image blocking rule is enabled, Container Security checks the security of the image. This ensures that the image that is started in the cluster meets your security requirements. | Only some cluster types of Container Service for Kubernetes (Container Service for Kubernetes) are supported. |
|---|---|---|
| Non- image program defense | After you create a protection rule for non- image programs, Container Security can detect and block the startup of programs outside the image. This helps you defend against known or unknown attack modes. | AliYunDun ≥ aegis 12 13, and _ _ AliHips ≥ 00 43. _ Make sure that the container image name cannot exceed 287 characters in length. The full path length of the running program in the container cannot exceed 1023 characters. The namespace of the cluster cannot exceed 287 characters in length. |
| Container anti- escape | The container anti-escape feature can detect high-risk behaviors from multiple dimensions, such as processes, files, and system calls. It establishes a barrier between containers and hosts to effectively prevent escaping behaviors and ensure container runtime security. This feature blocks attacks from attackers that exploit container vulnerabilities to host servers. This helps improve server system security. | The server where the cluster resides is connected to Container Service. |

**Block risky images**

Create a rule yundun-css-main ACK

| Ru | le issue |
|---|---|

SASMaliciouslm Create a pod Rules age policy

| Verification of im | ages |
|---|---|

Image scan results

| Obtain rules b | y cluster ID |
|---|---|

Query rules There is a risk

| im (bl | match the rule age execution behavior ock, alert, and release) |
|---|---|

Match Policy Management to Component Rule (gatewatkeeper) Alert /Release Interception Yes No Create a pod Create a pod Generating End Alerts suspicious

**Non-mirror program defense flowchart**

**Flow chart of container anti-escape**

Deploy hazardous containers
6. .** Dangerous container
deployment Client aegis-suspicious Alihips

|   | aegis-server d |
|---|---|
| 7. Alert record reporting | d |

5. .** Rule push
Aliyundun
8. .** T_MSG_PLUGIN
_EVENT_ALIHIPS
1. .** T_MSG_PLUGIN
3. .** T_MSG_CLIENT)
_HEARTS RULE_PUSH aegis-server
2. .** Assemble the rules

**Container Signature**

Container signatures enable trusted signatures on container images to ensure that only approved container images are allowed to be deployed. This prevents unauthorized images from being started and fundamentally helps you improve asset security. This feature is based on the asymmetric encryption algorithm. You must use KMSto create a key of the RSA_2048 typeand use the SIGN/VERIFY key. This feature integrates the signature verification capability with ACK clusters by configuring the**attestor**and**security policy**for containers. After the policy is enabled, only images with valid signatures can be deployed in the specified namespace. Images that are not signed or fail to be verified will be blocked. The flowchart is as follows: Signature verification Container for container startup security in ack cluster Sign the attestor for the

| Query the ce | rtiSfieecr |
|---|---|

Prover Security policy namespace of the cluster ack cluster
1. Query ACK clusters
2. Check whether the cluster
plug-in is installed.

**Notes for container signing:**

1. You need to install the component kritis-validation-hook to create an ACK
cluster
2. Check that the key signed by ACK and the certifier of Security Center use the
Query kms key interface, Query the security policies same key user-generated certifier of a Security Center
3. Check whether the delivered policy and the namespace delivered to the ack
for image signing are correct. kms acr only acr of the select an acr image

**Menu CMK creation type:**

to create a container. enterprise RSA_2048 edition has the image
**Key purpose:** the key of
SIGN/VERIFY signing feature.

### 1.2 High availability

**High-availability server side**

**Note**

High availability is delivered by using stateless applications. The server side of Container Security Service (CSS) consists of stateless applications and implements load balancing based on virtual IP addresses (VIPs) and Dubbo to ensure service availability. The server side is stateless. If you have at least two physical machines, service availability is ensured when one physical machine runs as expected. Data is stored in middleware such as Diamond and MetaQ or cloud services such as MiniRDS, Simple Log Service, Object Storage Service (OSS), and Tair. The middleware and cloud services provide high data storage availability. CSS provides API operations that can be called over HTTPS and implements load balancing based on domain names and VIPs to ensure service availability. Service calls in CSS depend on the Dubbo microservices framework. Software-based load balancing of Dubbo ensures service availability.

| Third-party Application User Server Guard Ag VIP DNS |   |
|---|---|
| Aegisbiz Aegisbiz SasContainerService SasContainerService Dubbo SasContainerNetwork SasContainerNetwork AegislmageAnalyzer AegislmageAnalyzer ...... ...... Physical Machine Physical Machine |   |
| MiniRDS OSS Tair MetaQ Cloud Storage Middleware Base Resource |   |

|   | VIP |   |
|---|---|---|

### 1.3 Disaster recovery and backup

**Zone-disaster recovery**

**Note**

Zone-disaster recovery is delivered by using the active-active mode. The zone-disaster recovery architecture of Container Security Service (CSS) follows the rules of the active-active mode. In this architecture, disaster recovery is ensured by cloud storage services or middleware.

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

**Note**

Geo-disaster recovery is delivered based on independent regions. The multi-region architecture of CSS follows the rules of independent regions. General regions do not depend on the central region, and data is completely isolated from services.

### 1.4 Monitor objects and send alert notifications

**notifications**

**System metrics**

System monitoring of Container Security Service (CSS) is connected to the TianjiMon console.

**Important**

Note: The alerting feature is not enabled for versions earlier than Apsara Stack V3.17.1. This section describes the monitoring metrics of applications.

**aegisbiz**

| Metric name (TianjiMon) | Monitored object | Metric description | Alert Threshold | Alert Descriptio n |
|---|---|---|---|---|
| aegisbiz cpu container host _ _ _ | CPU Utilization (Single Machine) | CPU Usage | util avg > _ 95 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisbiz cpu container serv _ _ _ errole | CPU utilization (service role) |   |   |   |
| aegisbiz cpu container clust _ _ _ er | CPU Utilization (Cluster) |   |   |   |
| aegisbiz memo container ho _ _ _ st | Memory (standalone) | Maximum and average memory usage | util avg > _ 90 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisbiz memo container se _ _ _ rverrole | Memory (service role) |   |   |   |
| aegisbiz memo container cl _ _ _ uster | Memory (Cluster) |   |   |   |
| aegisbiz load container host _ _ _ | Load (single machine) | Maximum and average CPU load (load1,load5,load15) | load1 av _ g > 1 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisbiz load container serv _ _ _ errole | Load (service role) |   |   |   |
| aegisbiz load container clus _ _ _ ter | Load (Cluster) |   |   |   |
| aegisbiz tcp conns containe _ _ _ r host _ | tcp connections (standalone) | Maximum and average tcp connections | No | No |
| aegisbiz tcp conns containe _ _ _ r serverrole _ | tcp connections (server role) |   |   |   |
| aegisbiz tcp conns containe _ _ _ r cluster _ | tcp connections (cluster) |   |   |   |
| aegisbiz ntp container host _ _ _ | NTP (standalone) | NTP | No | No |
| aegisbiz ntp container serve _ _ _ rrole | NTP (service role) |   |   |   |
| 0 |   | > Do | cument Versi | on: 2026082 |

|   |   | Contai tions a | ner Security nd Maintena M d | Service Oper nce Guide·O ocumentatio |
|---|---|---|---|---|
| aegisbiz ntp container clust _ _ _ er | NTP (cluster) |   |   |   |
| aegisbiz process count cont _ _ _ ainer host _ | Number of processes (on a single machine) | Maximum and average number of processes | process n _ umber m _ ax > 100 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisbiz process count cont _ _ _ ainer cluster _ | Number of processes (service roles) |   |   |   |
| aegisbiz process count cont _ _ _ ainer host _ | Number of processes (cluster) |   |   |   |
| aegisbiz nginx container ho _ _ _ st | NGINX QPS (standalone) | The QPS of NGINX requests. | No | No |
| aegisbiz nginx container ser _ _ _ verrole | Nginx QPS (service role) |   |   |   |
| aegisbiz nginx container clu _ _ _ ster | Nginx QPS (cluster) |   |   |   |
| aegisbiz health container ho _ _ _ st | health check (stand-alone) | Whether the application is started normally | health > 0 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisbiz health container se _ _ _ rverrole | health check (service role) |   |   |   |
| aegisbiz health container cl _ _ _ uster | health check (Cluster) |   |   |   |

**aegis-metadata application**

| Monitoring metric (TianjiMon metric name) | Monitoring name | Monitoring description | Alert Threshold | Alert Descriptio n |
|---|---|---|---|---|

| aegismetadata cpu containe _ _ r host _ | CPU Utilization (Single Machine) | CPU Usage | util avg > _ 95 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
|---|---|---|---|---|
| aegismetadata cpu containe _ _ r serverrole _ | CPU utilization (service role) |   |   |   |
| aegismetadata cpu containe _ _ r cluster _ | CPU Utilization (Cluster) |   |   |   |
| aegismetadata memo contai _ _ ner host _ | Memory (standalone) | Maximum and average memory usage | util avg > _ 90 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegismetadata memo contai _ _ ner serverrole _ | Memory (service role) |   |   |   |
| aegismetadata memo contai _ _ ner cluster _ | Memory (Cluster) |   |   |   |
| aegismetadata load contain _ _ er host _ | Load (single machine) | Maximum and average CPU load (load1,load5,load15) | load1 av _ g > 1 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegismetadata load contain _ _ er serverrole _ | Load (service role) |   |   |   |
| aegismetadata load contain _ _ er cluster _ | Load (Cluster) |   |   |   |
| aegismetadata tcp conns co _ _ _ ntainer host _ | tcp connections (standalone) | Maximum and average tcp connections | No | No |
| aegismetadata tcp conns co _ _ _ ntainer serverrole _ | tcp connections (server role) |   |   |   |
| aegismetadata tcp conns co _ _ _ ntainer cluster _ | tcp connections (cluster) |   |   |   |
| aegismetadata ntp containe _ _ r host _ | NTP (standalone) | NTP | No | No |
| aegismetadata ntp containe _ _ r serverrole _ | NTP (service role) |   |   |   |
| 2 |   | > Do | cument Versi | on: 2026082 |

|   |   | tions a | nd Maintena M d | nce Guide·O ocumentatio |
|---|---|---|---|---|
| aegismetadata ntp containe _ _ r cluster _ | NTP (cluster) |   |   |   |
| aegismetadata process coun _ _ t container host _ _ | Number of processes (on a single machine) | Maximum and average number of processes | process n _ umber m _ ax > 100 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegismetadata process coun _ _ t container cluster _ _ | Number of processes (service roles) |   |   |   |
| aegismetadata process coun _ _ t container host _ _ | Number of processes (cluster) |   |   |   |
| aegismetadata nginx contai _ _ ner host _ | NGINX QPS (standalone) | The QPS of NGINX requests. | No | No |
| aegismetadata nginx contai _ _ ner serverrole _ | Nginx QPS (service role) |   |   |   |
| aegismetadata nginx contai _ _ ner cluster _ | Nginx QPS (cluster) |   |   |   |
| aegismetadata health contai _ _ ner host _ | health check (stand-alone) | Whether the application is started normally | health > 0 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegismetadata health contai _ _ ner serverrole _ | health check (service role) |   |   |   |
| aegismetadata health contai _ _ ner cluster _ | health check (Cluster) |   |   |   |

**aegisContainerNetWork application**

| Monitoring metric (TianjiMon metric name) | Monitoring name | Monitoring description | Alert Threshold |
|---|---|---|---|
| tjmon aegismetadata memo conta _ _ _ iner host _ | Memory (standalone) | CPU Usage | util avg > _ 90 |
| tjmon aegismetadata load contain _ _ _ er host _ | Load (single machine) | Maximum and average CPU load (load1,load5,load15) | load1 avg > _ 2 |

| tjmon aegismetadata process cou _ _ _ nt container host _ _ | Number of processes (on a single machine) | Maximum number of processes | process nu _ mber max> _ 100 |
|---|---|---|---|
| tjmon aegismetadata health conta _ _ _ iner host _ | health check (stand- alone) | Whether the application is started normally | health>0 |
| tjmon aegismetadata exception al _ _ _ arm | Abnormal Alert (Single Machine) | Error Alert Reporting | level=="ER ROR" |
| tjmon aegiscontainer oom host _ _ _ | Memory overflow alarm (standalone) | Memory overflow alarm | oom status _ _ sum>0 |

**aegis-image-analyzer application**

| Monitoring metric (TianjiMon metric name) | Monitoring name | Monitoring description | Alert Threshold | Alert Descriptio n |
|---|---|---|---|---|
| aegisimageanalyzer cpu con _ _ tainer host _ | CPU Utilization (Single Machine) | CPU Usage | util avg > _ 95 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisimageanalyzer cpu con _ _ tainer serverrole _ | CPU utilization (service role) |   |   |   |
| aegisimageanalyzer cpu con _ _ tainer cluster _ | CPU Utilization (Cluster) |   |   |   |
| aegisimageanalyzer memo c _ _ ontainer host _ | Memory (standalone) | Maximum and average memory usage | util avg > _ 90 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisimageanalyzer memo c _ _ ontainer serverrole _ | Memory (service role) |   |   |   |
| aegisimageanalyzer memo c _ _ ontainer cluster _ | Memory (Cluster) |   |   |   |

| aegisimageanalyzer load co _ _ ntainer host _ | Load (single machine) | Maximum and average CPU load (load1,load5,load15) | load1 av _ g > 1 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
|---|---|---|---|---|
| aegisimageanalyzer load co _ _ ntainer serverrole _ | Load (service role) |   |   |   |
| aegisimageanalyzer load co _ _ ntainer cluster _ | Load (Cluster) |   |   |   |
| aegisimageanalyzer tcp con _ _ ns container host _ _ | tcp connections (standalone) | Maximum and average tcp connections | No | No |
| aegisimageanalyzer tcp con _ _ ns container serverrole _ _ | tcp connections (server role) |   |   |   |
| aegisimageanalyzer tcp con _ _ ns container cluster _ _ | tcp connections (cluster) |   |   |   |
| aegisimageanalyzer ntp con _ _ tainer host _ | NTP (standalone) | NTP | No | No |
| aegisimageanalyzer ntp con _ _ tainer serverrole _ | NTP (service role) |   |   |   |
| aegisimageanalyzer ntp con _ _ tainer cluster _ | NTP (cluster) |   |   |   |
| aegisimageanalyzer process _ count container host _ _ _ | Number of processes (on a single machine) | Maximum and average number of processes | process n _ umber m _ ax > 100 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisimageanalyzer process _ count container cluster _ _ _ | Number of processes (service roles) |   |   |   |
| aegisimageanalyzer process _ count container host _ _ _ | Number of processes (cluster) |   |   |   |
| aegisimageanalyzer nginx c _ _ ontainer host _ | NGINX QPS (standalone) | The QPS of NGINX requests. | No | No |
| aegisimageanalyzer nginx c _ _ ontainer serverrole _ | Nginx QPS (service role) |   |   |   |
| > Document Version: 20260828 |   |   |   | 3 |

|   |   | Alibab | a Cloud Secu ard Adv | rity-Server G anced Editio |
|---|---|---|---|---|
| aegisimageanalyzer nginx c _ _ ontainer cluster _ | Nginx QPS (cluster) |   |   |   |
| aegisimageanalyzer health c _ _ ontainer host _ | health check (stand-alone) | Whether the application is started normally | health > 0 | Consecuti ve times: 3 times Silence duration: 300s Detection interval: 60s |
| aegisimageanalyzer health c _ _ ontainer serverrole _ | health check (service role) |   |   |   |
| aegisimageanalyzer health c _ _ ontainer cluster _ | health check (Cluster) |   |   |   |

**Note**

For more information about the system monitoring of reusable Server Guard applications, see Server Guard Operations Guide.

**Business metrics**

System monitoring of CSS is implemented based on TianjiMon. The following table describes the metrics.

| Modules | Metric name | Description |
|---|---|---|
| Container asset | Node Quantity | Statistics on the number of nodes in all dimensions of a container cluster |
|   | Number of applications | Statistics on the number of applications in all dimensions of a container cluster |
|   | Number of pods | Statistics on the number of pods in all dimensions of a container cluster |
|   | Number of containers | Statistics on the number of containers in all dimensions of a container cluster |
|   | Number of images | Statistics on the number of images in all dimensions |
|   | Number of image scan tasks | Number of image scan tasks that are created |
|   | Number of image scan layers | Number of image layers that are scanned |

| libaba Cloud Security-Ser rd Advanced Edition |   |   |
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

### 1.5 Capacity Planning

Container security is calculated based on the number of CPU cores of the NC in the zone. For each additional 12000 container cores, two physical machines must be added to the BasicThinCluster (the ratio of NC to ECS is 1:6,500 NC to 3000 ECS, and the average specification of each ECS is 4 cores). The maximum specification of the Server Guard can only support up to 192000 cores. If the upper limit is exceeded, contact R&D for intervention.

**Resource Specifications**

| Server Guard specifications | BasicThinCluster | SasCluster | Calculation formula (the expected number of CPU cores of the entire cloud machine) |
|---|---|---|---|
| small | 2 | 2 | Total core number of containers in the cluster < 12000 |
| standard | 2~4 | 2~4 | Total core number of containers in the cluster < 24000 |
| large | 4~8 | 4~8 | Total core number of containers in the cluster < 48000 |
| xlarge | 8~16 | 8~16 | Total core number of containers in the cluster < 96000 |
| 2xlarge | 16~32 | 16~32 | Total core number of containers in the cluster < 192000 |

**MiniRDS resource specifications**

x86 Database Specifications

| Speci ficati on | small |   | standard |   | large |   | xlarge |   | 2xlarge |   |
|---|---|---|---|---|---|---|---|---|---|---|
| Data base insta nce nam e | Data base insta nce type | Disk spac e (Unit : GB) | Data base insta nce type | Disk spac e (Unit : GB) | Data base insta nce type | Disk spac e (Unit : GB) | Data base insta nce type | Disk spac e (Unit : GB) | Data base insta nce type | Disk spac e (Unit : GB) |
| aegis erver | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |

| healt hche ck | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
|---|---|---|---|---|---|---|---|---|---|---|
| defe nder | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| aegis vul | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| mord or | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| aegis biz | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
| aegis asset s | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| aegis dete ct | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 |
| aegis mast er | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| suspi cious | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |

| banff web | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 |
|---|---|---|---|---|---|---|---|---|---|---|
| aegis virus scan | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 | rds.m ys2.2 xlarg e | 500 |
| sasfil eserv er | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 |
| aegis meta data | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
| basel ine | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.2 xlarg e | 500 |
| news as | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 |
| aegis matc her | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.la rge | 50 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| aegis defe nce | rds.m ys2.st andar d | 50 | rds.m ys2.st andar d | 50 | rds.m ys2.la rge | 100 | rds.m ys2.xl arge | 200 | rds.m ys2.xl arge | 200 |
| mag piebr idge db | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |
| yund unap i | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |

| yund unlu ban | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |
|---|---|---|---|---|---|---|---|---|---|---|
| data sync | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.st andar d | - | rds.m ys2.la rge | - | rds.m ys2.la rge | - |

Arm /sw database specifications

| Database instance name | small | standard | large | xlarge | 2xlarge |
|---|---|---|---|---|---|
| aegiserve r | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
| healthch eck | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| defender | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisvul | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| mordor | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisbiz | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
| aegisasse ts | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| aegisdete ct | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismas ter | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| suspiciou s | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |

| banffweb | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
|---|---|---|---|---|---|
| aegisviru sscan | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s3.l arge | rds.mysql.c1.l arge | rds.mysql.c1.la rge |
| sasfileser ver | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismet adata | rds.mysql.s1.s mall | rds.mysql.s2.la rge | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
| baseline | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.c1.la rge |
| newsas | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s2.l arge | rds.mysql.s3.la rge |
| aegismat cher | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| aegisdefe nce | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s2.l arge | rds.mysql.s3.l arge | rds.mysql.s3.la rge |
| magpiebr idgedb | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| yunduna pi | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| yundunlu ban | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |
| datasync | rds.mysql.s1.s mall | rds.mysql.s1.s mall | rds.mysql.s1. small | rds.mysql.s2.l arge | rds.mysql.s2.la rge |

**Oss/Sls-inner resource capacity planning**

| Specific ations | Total core number of containers in a cluster | OSS Capacity (GB) | sls-Inner Total Disk Used (GB) |
|---|---|---|---|
|   | Formula | 2 GB per machine | 0.1 GB per machine |

| small | 12000 | 7000 | 350 |
|---|---|---|---|
| standar d | 24000 | 14000 | 700 |
| large | 48000 | 28000 | 1400 |
| xlarge | 96000 | 56000 | 2800 |
| 2xlarge | 192000 | 112000 | 5600 |

**Tair resource capacity planning**

| Speci ficati ons | Total core num ber of cont ainer s in a clust er | Required Allocation Quota for Each Tair Namespace (MB) |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   | nam espa ce | 92 | 381 | 499 | 663 | 106 | 690 | 478 | 692 | Total (Unit : MB) |
| small | 1200 0 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| stan dard | 2400 0 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| large | 4800 0 | 512 | 512 | 512 | 256 | 256 | 256 | 256 | 256 | 2816 |
| xlarg e | 9600 0 | 1024 | 1024 | 1024 | 512 | 512 | 512 | 512 | 512 | 5632 |
| 2xlar ge | 1920 00 | Contact R&D for confirmation |   |   |   |   |   |   |   |   |

**MetaQ resource capacity planning**

| Specific ations | Total core numbe r of contai ners in a cluster | Metaq Capacity Planning (Unit: 10,000) |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   | Process messag es | Networ k Messag es | File Messag es | Process write file messag es | Plug-in heartbe at messag es | Other | Total (Unit: 10,000) |
|   | Formula : (Messa ges /Hour /Machin e) | 240 | 20 | 5 | 15 | 60 | 140 | 0.058 |
| small | 12000 | 84 | 7 | 1.75 | 5.25 | 21 | 49 | 203 |
| standa rd | 24000 | 168 | 14 | 3.5 | 10.5 | 42 | 98 | 406 |
| large | 48000 | 336 | 28 | 7 | 21 | 84 | 196 | 812 |
| xlarge | 96000 | 672 | 56 | 14 | 42 | 168 | 392 | 1624 |
| 2xlarg e | 192000 | 1344 | 112 | 28 | 84 | 336 | 784 | 3248 |

### 1.6 XC

**Difference between Apsara Stack and controllable capabilities**

The difference between Apsara Stack and controllable capabilities is caused by different platforms. Apsara Stack x86 and Hygon x86 have the same capabilities. The capabilities of Phytium ARM and Kunpeng ARM differ from Apsara Stack by less than 30%, and plans are in place to align them in the future. The capabilities of ShenWei differ from Apsara Stack x86 by less than 50%, and no plans exist to align them in the future.

**Differences in container security capabilities**

| Feature | x86 | AR M | Sh en We i | Description |
|---|---|---|---|---|
| Overvie w | 100 % | 100 % | 100 % | This feature displays assets, vulnerabilities, exceptions, configuration defects, and events that require attention. |
| Containe r manage ment | 100 % | 100 % | 100 % | This feature provides information about the security status of containers. You can view the security status, groups, virtual private clouds (VPCs) of servers. You can also view the numbers of all servers, at-risk servers, unprotected servers, inactive servers, and new servers. You can click the name of a server to view the server details, including vulnerabilities, alerts, baseline check results, and asset fingerprint investigation. |
| Image scan and CI/CD scan | 100 % | 90 % | 80 % | The vulnerability detection feature detects Linux software vulnerabilities and application vulnerabilities. The feature provides details of vulnerabilities. You can use the quick scan feature. The baseline check feature automatically checks for risks related to the operating systems, accounts, databases, passwords, and security compliance configurations of your servers, and provides reinforcement suggestions. The malicious sample detection feature detects and removes virus and webshell. The system automatically detects and removes common trojan viruses, ransomware, mining viruses, and DDoS trojans. Important Capability differences Specific independent and controllable operating systems are not supported and must be adapted by using rule packages. Avira and Bitdefender detection engines are not supported by ARM. Only Graph Learning Engine (GLE) is supported. ShenWei does not support an engine. |
| Containe r firewall | 100 % | 0% | 0% | The container firewall feature is provided by Container Security Service (CSS) to ensure the security of container environments. If attackers exploit vulnerabilities or malicious images to intrude into clusters, the container firewall feature generates alerts or blocks attacks. Important Differences in capabilities: ARM and ShenWei do not support AliNet. No alerts are generated, and abnormal behavior is not blocked if you use ARM or ShenWei. |

| Containe r runtime protectio n | 100 % | 80 % | 50 % | This feature displays the information about alerts for affected cluster nodes in a centralized manner, including the number of servers on which alerts are generated, the total number of unhandled alerts, and alerts that require urgent handling. The alert types include abnormal process behavior, webshell, unusual logon, malicious process (cloud detection and removal), sensitive file tampering, abnormal network connection, persistent webshell, and web application threat detection. Important Differences in capabilities: Avira and Bitdefender detection engines are not supported by ARM. Only GLE is supported. ShenWei does not support an engine. |
|---|---|---|---|---|
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
|---|---|
| Heterogeneous multi-region deployment ((x86 and ARM)) Hardware heterogeneity at the central/unit data center level | Yes |

### 1.7 Hot upgrade

Container Security Service (CSS) supports hot upgrade by default. No additional O&M operations are required.

### 1.8 AliNet (06_21) Linux Driver OS / Kernel List

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
|   | 3.13.0-32-generic 3.13.0-86-generic 4.4.0-62-generic 4.4.0-63-generic 4.4.0-93-generic 4.4.0-96-generic 4.4.0-104-generic 4.4.0-117-generic 4.4.0-124-generic 4.4.0-142-generic 4.4.0-146-generic 4.4.0-151-generic 4.4.0-170-generic 4.4.0-174-generic 4.4.0-179-generic 4.4.0-184-generic | Exact match is supported. Example: 3.13.0-32-generic. |

|   | 4.4.0-185-generic 4.4.0-210-generic 4.15.0-13-generic 4.15.0-23-generic 4.15.0-42-generic 4.15.0-45-generic 4.15.0-52-generic |   |
|---|---|---|
| Ubuntu | 4.15.0-54-generic 4.15.0-72-generic 4.15.0-96-generic 4.15.0-106-generic 4.15.0-109-generic 4.15.0-111-generic 4.15.0-118-generic 4.15.0-124-generic 4.15.0-128-generic 4.15.0-144-generic 4.15.0-147-generic 4.15.0-158-generic 4.15.0-166-generic 4.15.0-169-generic 4.15.0-170-generic 4.15.0-1047-gcp 5.3.0-40-generic 5.4.0-31-generic 5.4.0-42-generic 5.4.0-47-generic 5.4.0-58-generic 5.4.0-73-generic 5.4.0-77-generic 5.4.0-86-generic 5.4.0-91-generic 5.4.0-92-generic 5.4.0-94-generic 5.4.0-100-generic 5.4.0-102-generic 5.4.0-106-generic |   |

| AliYunLinux | 3.10.0-1160.al7.1.x86 64 _ 4.4.95-1.al7.x86 64 _ 4.4.95-3.al7.x86 64 _ 4.19.24-7.al7.x86 64 _ 4.19.24-7.14.al7.x86 64 _ 4.19.81-17.al7.x86 64 _ 4.19.81-17.2.al7.x86 64 _ 4.19.91-19.1.al7.x86 64 _ 4.19.91-21.2.al7.x86 64 _ 4.19.91-21.al7.x86 64 _ 4.19.91-22.2.al7.x86 64 _ 4.19.91-22.al7.x86 64 _ 4.19.91-23.al7.x86 64 _ 4.19.91-24.1.al7.x86 64 _ 4.19.91-25.1.al7.x86 64 _ 4.19.91-25.3.al7.x86 64 _ 4.19.91-25.6.al7.x86 64 _ 4.19.91-25.7.al7.x86 64 _ 5.10.23-5.al8.x86 64 _ 5.10.60-9.al8.x86 64 _ 5.10.84-10.2.al8.x86 64 _ 5.10.84-10.3.al8.x86 64 _ | Exact match is supported. |
|---|---|---|
| Anolis | 3.10.0-1160.an7.x86 64 _ 3.10.0-1062.an7.x86 64 _ 3.10.0- 1160.59.1.0.1.an7.x86 64 _ 4.19.91-25.2.an7.x86 64 _ 4.19.91-25.7.an7.x86 64 _ 4.18.0-348.2.1.an8 4.x86 64 _ _ 4.18.0-348.12.2.an8.x86 64 _ |   |
