---
title: "Apsara Stack Resilience Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 29
source_pdf: "9f0847033542205a_Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack Resilience Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20Resilience%20Product%20Introduction%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Apsara Stack Resilience Product Introduction 20260701

## Table of Contents

- 1 Apsara Stack Resilience
  - 1.1 Product details
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features
    - 1.4.1 ASR for zone-disaster recovery
    - 1.4.2 ASR-DR: geo-disaster recovery platform
    - 1.4.3 ASR for backup and recovery

## 1 Apsara Stack Resilience

As industries become increasingly digitized, the stability and security of IT infrastructure are more crucial for enterprises. With the evolution of Classified Protection of Cybersecurity 2.0 and the rapid growth of new infrastructure, cloud disaster recovery has emerged as a future trend**.** To ensure business continuity and data security, Apsara Stack provides multiple disaster recovery solutions such as Apsara Stack Resilience for Geo-disaster Recovery, Apsara Stack Resilience for Zone-disaster Recovery, and Apsara Stack Resilience for Backup and Recovery (ASR-BR). Combinations of these solutions are also supported. These disaster recovery solutions are designed and developed based on Alibaba Cloud computing capabilities and international disaster recovery standards. Apsara Stack Resilience ASR (Apsara Stack Resilience) is a graphical switchover tool provided by Alibaba Cloud that enables rapid disaster recovery switchover during disasters, minimizing the Recovery Time Objective (RTO). Apsara Stack Resilience offers one-click disaster recovery management from an application system perspective for all scenarios, making it an ideal choice for ensuring business continuity and data security for enterprises.

### 1.1 Product details

Apsara Stack Resilience(ASR) is dedicated to full-stack cloud backup and recovery and is used to ensure data security and business continuity for enterprises. Apsara Stack Resilience provides the following disaster recovery solutions: ASR for Zone-disaster Recovery, ASR for Geo-disaster Recovery, and ASR for Backup and Recovery. You can combine these solutions to fit your business scenarios. For example, the three data centers across two regions architecture combines ASR for Zone-disaster Recovery and ASR for Geo-disaster Recovery. It aims to quickly implement switchover and recovery in multiple scenarios.

**ASR for Zone-disaster Recovery**

ASR for Zone-disaster Recovery consists of a primary data center and a secondary data center. The secondary data center is in the same region as the primary center, but in different zones. This deployment method is used to combat local disasters with a small impact. ASR for Zone-disaster Recovery is adopted on all core cloud products such as networking, cloud computing, databases, storage, middleware, and big data products. This can be used in cross-zone deployment for high availability. In the event of a disaster, business can be quickly switched over to the secondary zone. The endpoint of the cloud product remains unchanged. ASR for Zone-disaster Recovery can be used in two data centers and three data centers. On the foundation of the two data centers-based mode, a third data center can be added and the databases are deployed in a distributed manner. The architecture of ASR for Zone-disaster Recovery with two data centers: Architecture of three data centers-based zone-disaster recovery: ASR for Zone-disaster Recovery is mainly used for monitoring, drills, protection group disaster recovery, data center-level fault recovery, and single-product fault recovery. Cloud product monitoring: checks the status of synchronization tasks between data centers, business status of each data center, and synchronization latency on a regular basis, and monitors disaster recovery in both data centers in real time on the dashboard. Disaster recovery drills: allows you to customize hot switchover for cloud products to meet your requirements of routine disaster recovery drills. Data center-level fault recovery: handles data center-level faults, such as power outages in the primary and secondary data centers, network outages in the primary and secondary data centers, and split-brain scenarios. Single-product fault recovery: helps the cloud product recover from faults and ensures business continuity when the high-reliability feature becomes unavailable. Compared with other solutions, ASR for Zone-disaster Recovery has the following advantages: It is cost-effective to access applications because ASR for Zone-disaster Recovery is oriented to cloud-native applications and no business transformation is required for application migration to the cloud. Full-stack disaster recovery provides integrated disaster recovery architecture to cover Apsara Uni-manager and cloud products. The three data centers-based mode of ASR for Zone-disaster Recovery supports 0 synchronization latency for ApsaraDB RDS for MySQL, ApsaraDB for OceanBase, PolarDB-X 2.0, Elasticsearch and MongoDB. Hybrid cloud

**ASR for Geo-disaster Recovery**

ASR for Zone-disaster Recovery consists of a primary data center and a secondary data center. The secondary data center is in a different region from the primary data center to cope with possible disasters at the primary data center. After you create a protection group, you can establish a hot backup channel between the resources of the primary and secondary sites. Changes to the resources at the primary site are asynchronously replicated to the corresponding resources at the secondary site in hot backup mode. If the primary data center fails, applications or services are failed over to the secondary data center by using a failover plan. After the primary data center is recovered, business is failed back to the primary cloud by using a failback plan. This way, business continuity is ensured. ASR for Geo-disaster Recovery includes the cross-cloud mode and cross-region mode, and supports application dual-active capability. The following figures show architectures of the two modes. Cross-cloud mode Cross-region mode ASR for Geo-disaster Recovery offers the following main features: DR drills, system management, and DR Dashboard. DR drills: include DR for Business and Global DR. You can set protection groups, drill plans, and recovery plans. You can also associate plans and then start the associated plans in batches based on execution sequence number. Plans can be divided into switchover, switchback, failover, and failback. System management: includes user management, primary cloud instance configuration, secondary cloud instance configuration, log management, capacity management, selfdisaster recovery, and historical messages. DR dashboard: displays metrics such as the RTO duration, synchronization latency satisfaction of both the drill plan and recovery plan, the numbers of successful and failed drill plans and recovery plans within a specified time period, and the overall progress of the switchover and switchback processes. ASR for Geo-disaster Recovery is an application-based protection group disaster recovery mode and has the following advantages: Multiple disaster recovery scenarios are supported, such as many-to-one, primary/secondary, and cross-region. It is from the intuitive business perspective and supports the following features: disaster recovery drills for protection groups, protection groups switchover, and backward protection. Switchover of a cloud is not required if a single service is faulty.

**ASR for Backup and Recovery**

One or more secondary data centers are created to back up data of the primary site. ASR for Backup and Recovery provides the cloud-native backup capability and is required in MLPScompliant projects. ASR for Backup and Recovery uses the unified backup management platform and supports virtual machine backup (including cloud disk), storage backup (excluding cloud disk), VMware backup, database backup, big data backup, and local backup of cloud platform metadata. ASR for Backup and Recovery supports the following services: ApsaraDB RDS, OSS, ECS, Apsara File Storage NAS, PolarDB-X 1.0, VMware virtual machine, and MaxCompute. Single-region backup architecture Cross-region backup architecture ASR for Backup and Recovery offers the following main features: backup, migration, and recovery. Backup: includes cross-region backup and local backup. You can create database backup vaults and create and delete storage backup vaults. All backup vaults are stored in OSS. Recovery: includes routine recovery, cloud rebuilding recovery, recovery on cloud of VMware VMs, and local recovery of VMware VMs. Migration: Migration plans are created to migrate data from on-premises VMware VMs to ECS instances. ASR for Backup and Recovery has the following advantages: A unified backup management platform is provided and can be used to back up databases, storage services, and MaxCompute. Physical backup is used for databases. The performance of the primary cloud instance is not affected because the backup time is very short.

**Three data centers across two regions disaster recovery**

Three data centers across two regions disaster recovery combines zone-disaster recovery and geo-disaster recovery. This solution is used to combat regional natural disasters and prevent regional failures. Two regions include the local and remote regions. Three data centers include the local primary data center, the local secondary data center, and the remote secondary data center. This solution provides active-active zone-disaster recovery. Data is synchronously replicated between two data centers. Data is asynchronously replicated between data centers in different regions that are in the active-standby mode. This mode has low business intrusion and can be quickly set up. It provides financial-grade reliability and unified disaster recovery management for full-stack cloud services. Architecture of three data centers across two regions disaster recovery Compared with traditional disaster recovery, the three data centers across two regions mode has the following advantages: The combination of zone-disaster recovery and geo-disaster recovery achieves lower RPO and RTO. This mode can be used to address regional failures and meet the high MLPS requirements in the finance industry.

**Hybrid disaster recovery**

Hybrid disaster recovery refers to disaster recovery between Apsara Stack and public cloud. In this document, it specifically refers to hybrid disaster recovery between Apsara Stack and Alibaba Cloud public cloud. Hybrid Disaster Recovery for Apsara Stack is an efficient, secure, and cost-effective disaster recovery service specifically designed for hybrid cloud scenarios. On the disaster recovery management platform, you can create protection groups for your cloud product instances to achieve data synchronization between Apsara Stack instances and public cloud instances. It also provides orchestration-enabled drill and fault emergency response capabilities to ensure the consistency of business data. Architecture of hybrid disaster recovery: Hybrid disaster recovery offers the following advantages: It takes Apsara Stack as the primary data center and public cloud as the backup resource pool to reduce the high cost of building and maintaining a second data center. It also enables on-demand scaling when demand increases. If Apsara Stack fails and becomes unavailable, disaster recovery can be implemented through the public cloud disaster recovery management platform.

### 1.2 Benefits

Unlike the disaster recovery that covers only ECS instances, Apsara Stack Resilience (ASR) provides multiple disaster recovery solutions such as ASR for Zone-disaster Recovery, ASR for Geo-disaster Recovery, and ASR for Backup and Recovery. A combination of these solutions is also supported. These make ASR an ideal choice for enterprises to ensure business continuity and data security.

**ASR for Zone-disaster Recovery**

**Application-specific disaster recovery solutions**

You can select appropriate cloud-based disaster recovery solutions based on application features. It is cost-effective to access applications because ASR for Zone-disaster Recovery is oriented toward cloud-native applications and no cloud migration is required. It can cover all distributed applications. For applications that use traditional architectures, you can create protection groups to migrate them to the cloud without the need for business transformation.

**Strong data consistency**

The three data centers-based mode of ASR for Zone-disaster Recovery supports 0 synchronization latency for ApsaraDB RDS for MySQL, ApsaraDB for OceanBase, PolarDB-X 2.0, Elasticsearch and MongoDB.

**Full-stack disaster recovery**

ASR for Zone-disaster Recovery delivers full-stack disaster recovery schemes that cover base, cloud products, and Apsara Uni-manager. It can be used in cross-zone deployment for high availability. In the event of a disaster, business can be quickly switched over to the secondary zone. The endpoint of the cloud product remains unchanged.

**Full disaster recovery scenarios**

ASR for Zone-disaster Recovery covers all disaster recovery scenarios. It allows you to customize hot switchover for cloud products to meet your routine disaster recovery drill requirements. It also supports data center-level fault recovery and single-product fault recovery.

**ASR for Geo-disaster Recovery**

**Intuitive business perspective**

ASR for Geo-disaster Recovery is a business-based protection group disaster recovery. It supports the following features in an intuitive and visualized manner: disaster recovery drills for protection groups, push-button switchover of protection groups, and backward protection. Switchover of a cloud is not required if a single service is faulty.

**Abundant disaster recovery scenarios**

Support diversified scenarios such as cross-cloud disaster recovery, cross-Region disaster recovery, multi-to-one disaster recovery, application dual-active disaster recovery, and hybrid cloud disaster recovery.

**Efficient disaster recovery drills**

Support flexible and custom disaster recovery drill plans and custom cloud product switchover policies. The drill plans are executed in a standardized process. You do not need to manually write drill scripts. The drill results are visualized.

**Controlled disaster recovery management**

Support multitenancy. Disaster recovery resources are isolated by organization to ensure data security. Each service can be switched independently to avoid mutual interference.

**ASR for Backup and Recovery**

**Backup of multiple services**

ASR for Backup and Recovery provides the cloud-native backup capability and supports the following services: ApsaraDB RDS, Object Storage Service (OSS), Elastic Compute Service (ECS) instances and files, Apsara File Storage NAS, PolarDB-X 1.0, VMware virtual machine, and MaxCompute.

**High backup efficiency for databases**

Physical backup is used for databases. The backup time is very short. All backup jobs can complete in time.

**Multiple backup scenarios**

You can create backup plans as a tenant. ASR-BR supports periodic backup, manual backup, and cloud rebuilding recovery of the business data for cloud services.

**Automated plug-in installation and connections**

The Tunnel mechanism is used to implement automatic one-way connections between VPC and storage network. Cloud Assistant is used to install the proxy plug-in and no manual installation is required.

**High security**

The integration of the management page of ASR for Backup and Recovery with the cloud platform ensures that the account permission system is consistent. Security is enhanced because the cloud security mechanism is also integrated.

### 1.3 Scenarios

Selection of disaster recovery solutions is determined by a variety of factors, such as investment, acceptable RTO and RPO, and disaster types. The following table describes the scenarios of different disaster recovery solutions.

| Disaster recovery solution | Scenario | Industry |
|---|---|---|
| Two data centers-based mode of ASR for Zone-disaster Recovery | High business continuity is required. Strong data consistency is not required. The two data centers have independent power supplies, independent networks, and optical fiber length of no more than 50 kilometers in between. | Industries such as finance, healthcare, government, energy, and transportation |
| Three data centers-based mode of ASR for Zone-disaster Recovery | High business continuity is required. Strong data consistency is required to ensure synchronization latency of 0 for instances in the same region. Note The following products are supported: ApsaraDB RDS for MySQL, PolarDB-X 2.0Elastic Compute Service (ECS), Elastic Block Storage (EBS), Server Load Balancer (SLB), Virtual Private Cloud (VPC) and ApsaraDB for MongoDB. The three data centers have independent power supplies, independent networks, and optical fiber length of no more than 50 kilometers in between. | Finance |

| ASR for Geo- disaster Recovery | High business continuity is required. Strong data consistency is not required. The capability to cope with regional failures is required. Distance between regions is more than 100 km. Application primary-secondary disaster recovery and application dual-active disaster recovery are supported. | Industries such as government, energy, transportation, and healthcare |
|---|---|---|
| ASR for Backup and Recovery | Need to meet security requirements for core business data. Virtual machine backup (including cloud disks), storage backup (excluding cloud disks), VMware backup and recovery, database backup, big data backup, and cloud platform metadata backup are required. Note The following products are supported: ApsaraDB RDS, Object Storage Service (OSS), ECS instances and files, Apsara File Storage NAS (NAS), PolarDB-X 1.0, PolarDB-X 2.0, VMware, and MaxCompute. | All industries, especially those with classified protection requirements. |
| Three data centers across two regions mode | A solution is needed to combat regional natural disasters. A solution is needed to prevent regional faults. Near 0 synchronization latency for business- critical data is required. The budget is adequate. | Finance |
| Hybird cloud disaster recovery | For customers with disaster recovery requirements, it provides a cost-effective hybrid cloud disaster recovery solution. In scenarios where business modules are deployed in both public cloud and Apsara Stack, it prevents service disruptions caused by failures in either public cloud or Apsara Stack. | All industries, especially those concurrently utilizing both Apsara Stack and public cloud. |

### 1.4 Features

This topic describes the features of ASR for Zone-disaster Recovery, ASR for Geo-disaster Recovery, and ASR for Backup and Recovery.

#### 1.4.1 ASR for zone-disaster recovery

This topic describes the features of the Zone-Disaster Recovery Management Platform available in the Apsara Uni-manager Operations Console and the Apsara Uni-manager Management Console.

**Features in the Apsara Uni-manager Operation Console**

| View | Feature |   | Description |
|---|---|---|---|
|   | Overview |   | Displays the overall disaster recovery capabilities. It lets you understand the disaster recovery capabilities of your platform more intuitively and quickly. You can view the status of the secondary data center and the network traffic between data centers, predict the duration and results of forced switchovers, and view the usage records of the platform. |
|   | Platform Monitoring | Product Monitoring | Displays the overall product states, the service states in the primary data center, the service states in the secondary data center, disaster recovery capabilities, primary data center location, and update time. Before services are switched over or back, you can check whether the states of the services are normal. If abnormalities exist, you can switch over or back the services after the abnormalities are resolved. |
|   |   | Synchronization Monitoring | Displays Data Synchronization Latency Compliance Rate, Instances with Successful Synchronization, Instances with Synchronization Exceptions, and the Synchronization Latency for products. |
|   |   | Dashboard monitoring | Displays business continuity, including statistics on the number of disaster recovery products, overview of selected products, and product details. |
|   | Disaster Recovery Drills | Drill Plan | You can run online drills to switch over products from the primary data center to the secondary data center when no power or network outages occur. Online drills are implemented to ensure data consistency between the primary and secondary data centers. Custom drills and predefined drills are supported: Custom drills: You can select multiple products to create and run drill plans based on your requirements. Predefined drills: You can select a product drill plan predefined on ASR for Zone-disaster Recovery or select the overall drill plan that includes all products. |
|   |   | Drill History | Displays the history and results of predefined drills and custom drills. |

| Normal view |   |   |   |
|---|---|---|---|
|   | Disaster Recovery | Switchover | Scenario-based fault recovery is supported to reduce the RTO of disaster recovery. Online services can be quickly restored by switching services to the secondary data center. Disaster recovery scenarios include recovery from power failures, island faults, split-brain, and single- product faults. You can perform one-click switch operations. |
|   |   | Returning to the platform | Platform failback, the reverse of platform failover, returns services to their original state after recovery from a fault scenario, such as a power failure, an island fault, or a single product fault. You can perform a failback with a few clicks. |

|   |   | Fault Simulation | Fault simulation is a testing and verification technique used to evaluate the recovery capabilities of a cloud platform in the event of failures or disasters. Fault simulation involves manually introducing faults to simulate potential system failures and observe and analyze the disaster recovery process of the cloud platform. Feature Description Security risks may arise when faults are injected into a data center. You Operatio are not allowed to inject faults unless n you are authorized. You must apply approval for an authentication code before you inject faults into a data center. To ensure the accuracy of disaster Environ recovery drill results, you must ment check whether the environment Check works as expected before you inject faults. If the environment does not work as expected, do not perform further operations. Start You can manually inject fault types injection similar to (but not) real disasters in the data center. Data After the fault simulation is Center completed, you can manually Recover recover the faulty data center to y ensure normal business. |
|---|---|---|---|
|   |   | Recovery History | Displays the recovery history, which records the time for various recovery and failover operations, execution results, logs, and failover duration. |
|   | Monitoring center | Environment check | Quickly get information about disaster recovery product versions, product baselines, DNS resources, VIP resources, and database resources. Use the environment check to verify if all items meet the disaster recovery requirements. |
|   | ersion: 2026 |   |   |

| Feature | Description |
|---|---|
| Operatio n approval | Security risks may arise when faults are injected into a data center. You are not allowed to inject faults unless you are authorized. You must apply for an authentication code before you inject faults into a data center. |
| Environ ment Check | To ensure the accuracy of disaster recovery drill results, you must check whether the environment works as expected before you inject faults. If the environment does not work as expected, do not perform further operations. |
| Start injection | You can manually inject fault types similar to (but not) real disasters in the data center. |
| Data Center Recover y | After the fault simulation is completed, you can manually recover the faulty data center to ensure normal business. |

| roduct Introd Resilience | uction·Apsara |   |   |
|---|---|---|---|
| O&M view |   |   |   |
|   |   | Product check | Automatically checks the status of SLB, DNS, and the MiniRDS metadatabase before and after a disaster recovery switchover. |
|   | Configurat ion center | Alert Management | The zone-disaster recovery management platform provides preset alert rules. You can modify existing alert levels as needed. An alert is generated when an abnormal metric is detected and the conditions of an alert rule are met. |
|   |   | Leased Line Management | After you configure the Data Center Interconnect (DCI) information, the network traffic between devices in different data centers is displayed on the Overview page. This gives you a clear view of the data transmission between devices in different data centers. |
|   |   | Arbitration management | In a standard three-data-center deployment, the arbitration service detects real data center-level failures. If a failure occurs, the service determines if the conditions for an arbitrated switchover are met. If so, it initiates a switchover to move products and the underlying platform to a healthy data center. |
|   |   | Theme settings | Set the theme color, logo, and platform name for the monitoring dashboard or the drill dashboard. |
|   | Security center | Escape logon management | The escape logon switch is controllable. To ensure account security, change your logon password regularly. |
|   |   | Data backup | You can back up data such as user accounts and alert rules that are configured in the ASR for Zone-disaster Recovery console to an Object Storage Service (OSS) bucket. You can restore the data to the ASR for Zone- disaster Recovery console as required with a few clicks. |

**Features in the Apsara Uni-manager Management Console**

| Feature | Description |
|---|---|

| Protection Groups | You can create a protection group for resources used by an application. You can add ECS instances, ApsaraDB RDS instances, OSS buckets, or AnalyticDB clusters in an application to a protection group. After these resources are added to the protection group, you can fail them over as a group. You can view protection group information such as the name, product list, description, creator, and creation time. |
|---|---|

#### 1.4.2 ASR-DR: geo-disaster recovery platform

**platform**

This topic describes features of the ASR-DR: geo-disaster recovery platform available on the Apsara Uni-manager Operations Console and the Apsara Uni-manager Management Console.

**Features on the Apsara Uni-manager Operations Console**

| Feature |   |   | Description |   |   |
|---|---|---|---|---|---|
| Homepage |   |   | You can view Authorization usage statistics, Node task load statistics, Total number of abnormal synchronization entities, Unassigned task statistics, Bandwidth Usage, and Dedicated Line traffic usage. |   |   |
| Disaster Recovery Monitoring | Cloud Platform Monitoring |   | You can monitor the disaster recovery status of cloud products. This includes metrics such as service availability, domain name resolution, and network access. This ensures that the cloud platform can quickly switch to another region in case of a failure, thereby ensuring business continuity. |   |   |
|   | Protection Group Status Monitoring |   | You can monitor the number of synchronization entities, synchronization status, and maximum synchronization latency for protection groups. You can also monitor the synchronization status, synchronization latency, and status of primary and secondary instances for cloud products. |   |   |
| Products | DNS |   | You can add a DNS forwarding configuration to resolve the Server unreachable: |   |   |
|   |   |   |   | Server unreachable: |   |
|   |   |   | java.net.unknownHostException |   | issue. |

| General | VPC Management | You can delete or view registration information for existing Virtual Private Clouds (VPCs) . You can register new VPC information for cloud instances that lack it. You can validate VPC registration information if a VPC authorization error occurs or a VPC-type instance fails to be accessed. You can view the VPC authorization information for the current cloud instance. You can authorize a cloud instance if it is not authorized. |
|---|---|---|
|   | Node Management | You can view node information and unassigned tasks in the ASR-DR cluster. You can click Details to view tasks that are running on the current node. |
|   | Disaster Recovery Interconnection Management | You can add disaster recovery interconnections between specified regions. |
|   | Disaster recovery Gateway Management | In cross-cloud scenarios, configure the peer gateway information. This establishes a disaster recovery relationship and connects the networks at both ends. |
|   | Parameter Management | You can dynamically configure parameters for ASR-DR products. |
|   | Cloud Information Management | You can configure the disaster recovery cloud and production cloud on the Apsara Uni-manager Operations Console. Then, you can use ASR-DR: Geo- Disaster Recovery Platform on the Apsara Uni-manager Management Console. After you add a production cloud instance, configure the supported disaster recovery products and their addresses. ASR for Geo-disaster Recovery can then perform disaster recovery for resource instances in the production cloud. |
|   | Capacity Management | You can view the resource usage of protection groups and synchronization entities. |
|   | Large-screen Map Configuration | You can configure disaster recovery regions for the large-screen map. After configuration, the geo-disaster recovery data for these regions will be displayed on the large screen. |
| 2 | > Document Version: 2026070 |   |

|   | Data Upgrade | You can upgrade all data for protection groups and disaster recovery plans. |
|---|---|---|
| Disaster recovery O&M | Synchronization Entity Management | You can view protection group lists and details. You can also delete protection groups and protected entities that are no longer needed. You can view the task execution list, step details, and single-step execution logs for the current synchronization entity. You can retry or skip a single step. |
|   | Site Disaster Recovery Drill | You can simulate a scenario where all site devices fail and all services must be switched over. Execute pre- created and attached disaster recovery plans. During the data center switchover, these disaster recovery plans will be executed in batches. |
|   | Site Disaster Recovery | For a real scenario where all site devices fail and all services must be switched over, you can execute pre- created and attached disaster recovery plans. During the data center switchover, these disaster recovery plans will be executed in batches. |
|   | Plan Execution History | You can view plan steps, progress, associated protection groups, and execution history of a site disaster recovery plan. |
| Independent Disaster Recovery |   | You can create independent disaster recovery and perform failovers and switchover drills. You can view details of independent disaster recovery. You can also unbind and delete configurations. Note Independent disaster recovery needs to be configured only in cross-cloud disaster recovery scenarios and does not need to be configured in cross-region scenarios. |

**Features on the Apsara Uni-manager Management Console**

| Feature | Description |
|---|---|
| Overview | The system presents a business disaster recovery overview using charts and figures. You can view real- time disaster recovery metrics and check the status of disaster recovery protection groups to streamline DR management and enhance business continuity. |

| Instance List |   | You can create instances to be protected separately at the production and disaster recovery sites. The number and specifications of these instances must match exactly between the two sites within a protection group. |
|---|---|---|
| Business Disaster Recovery | Protection Group | You can create, modify, and delete protection groups. You can add synchronization entities from various cloud products to a protection group. You can switch over or fail back a protection group. You can view protection group details. You can perform the following operations on a protection group: start, stop, and reprotect. Topology diagrams allow you to view disaster recovery relationships, data flow direction, and latency between primary and standby data centers and entities. |
|   | Business Disaster Recovery Plan | A business disaster recovery plan organizes resource switchover or inspection operations within a protection group into a series of sequentially ordered tasks. You can create drill switchover plans, drill failback plans, failover plans, and failback plans. You can configure drill metrics. Based on the collected metrics, the system evalutes drill results and provides targeted suggestions for any non- compliant items. |
|   | Disaster Recovery Unit Namespace | You can create a disaster recovery unit namespace and bind it to a protection group. This ensures that only the synchronization entities within the specified namespace are switched over during a switchover. A disaster recovery unit namespace cannot be bound to multiple protection groups. A synchronization entity cannot be used by multiple disaster recovery unit namespaces. |
| Alert Management | Alert Rules | You can create, stop, modify, delete, and view alert rules. |
|   | Alert Records | You can view and export reported alert information to stay promptly informed of any anomalies. |
|   | Synchronization Latency Alert Configuration | You can configure synchronization latency alert thresholds for various cloud products. ASR-DR calculates synchronization latencyfor each product based on these thresholds and displays the results on the homepage and the disaster recovery dashboard. |

| System Management | Cloud Instance Management | You can create, modify, and delete cloud instances. The system manages cloud instances by level-1 organization. Any authorized user within a level-1 organization or its sub-organizations can configure cloud instances for their organization. Configured cloud instances will then be visible to all members within that organization. |
|---|---|---|
|   | Disaster Recovery Relationship Management | You must create disaster recovery relationships between instances before performing disaster recovery operations. Only paired regions support disaster recovery operations. |
|   | Log Management | You can view all operation logs on the ASR-DR: Geo- Disaster Recovery Platform, including creation, deletion, and execution records of protection groups, plans, and instances. |
|   | Hybrid Cloud Disaster Recovery Management | The system supports hybrid disaster recovery between Apsara Stack and Alibaba Cloud Public Cloud. |
| Large-Screen Monitoring |   | You can get an overview of the disaster recovery system with charts and figures. Based on the type of disaster recovery plan task, the geo-disaster recovery dashboard operates in either Normal or Switch Status mode. |

#### 1.4.3 ASR for backup and recovery

This topic describes the features of ASR for Backup and Recovery on the Apsara Uni-manager Management Console.

| Feature | Description |
|---|---|
| Overview | The system displays real-time backup status, backup and restoration statistics, resource statistics, backup status, and system alerts to help you quickly grasp the overall backup landscape. |

| User Guidance | You can access either the homepage or the product documentation page. You can view the workflow for using ASR for Backup and Recovery as an operations administrator or organization administrator. You can view benefits, preparations, and steps for backing up data to Alibaba Cloud Public Cloud. You can view recommended scenarios and key concepts for backup. |
|---|---|
| Instance List | You can view instances and their details across various cloud products. You can view backup records, log backup status, and backup and restoration events for instances. |
| Backup Repository | A backup repository is a logical storage space planned on a storage pool. It is equivalent to an Object Storage Service (OSS) bucket and is used to store business data backups. You can create repositories for database, storage, deduplication- based storage, and Tablestore products. Isolation between different types of data warehouses is also supported. Repositories can be stored locally, remotely, or on Alibaba Cloud Public Cloud. You can create image repositories based on backup repositories to back up cloud product business data to the backup repositories, then synchronize data to the image repositories. You can view, modify, and delete backup repositories. |
| Backup Plan | When you create a backup plan, the system automatically lists resource instances and displays their backup protection status. You can filter backup plans by instance ID or instance name. You can view, start, stop, and modify a backup plan. You can view log backups, backup events, and backup statistics. |
| Backup Record | You can view backup records. The system displays details such as instance name, instance type, record status, start time, duration, task progress, storage capacity, and backup mode. You can filter backup records by instance ID, start time, or record status. |

| Data Restoration |   | You can perform cloud reconstruction recovery (disaster recovery) to restore data when the production cloud experiences catastrophic failures and requires reconstruction. You can perform routine restoration for daily scenarios such as accidental data deletion or tampering in the production cloud. A single recovery plan supports multiple products and multiple instances. You can perform orchestrated restoration by customizing the recovery sequence and setting instance priorities. You can associate recovery policies with recovery plans to enable automatic execution. |
|---|---|---|
| Archive Management |   | You can configure permissions for third-party platforms to obtain device information from them. You can create, edit, and authorize tape libraries and media sets. You can create archive plans to archive RDS or OSS instances in tape libraries. You can create recovery tasks to restore RDS or OSS instances archived in tape libraries. |
| System Management | Storage Pool Group Management | Operations administrators can manage backup storage pools. A storage pool is a cluster that stores backup data. You can create multiple storage pools. You can manage both local and remote storage pools. |
|   | Self-backup Management | You can back up metadata for the hybrid cloud backup service. |
|   | Disaster Recovery | You can create disaster recovery tasks. Note You can use this feature in the following scenarios: You need to restore data backed up to a remote storage pool across clouds to a standby Alibaba Cloud Apsara Stack. The production cloud fails or encounters a disaster, requiring data restoration. |
|   | vCenter Management | You can create vCenters to operate and manage virtual machines. |

|   | Authorization Management | You can view authorization details, including authorization type, total authorizations, authorization usage, and remaining quota. Operations administrators can set quotas for each organization to ensure fair allocation of resources and prevent any single organization from consuming excessive capacity at the expense of others. By default, no quota limits are applied. |
|---|---|---|
|   | Alert List | You can view alert information. You can delete alert records. |
|   | Flow Control Configuration | Operations administrators can customize traffic thresholds for cloud products and VMware across different time periods. Note Throttling configurations for different time periods and storage pools operate independently. |
| O&M Management |   |   |
|   | Engine Monitoring | Operations administrators can view traffic, CPU, memory, and load monitoring data. |
|   | Resource Statistics | You can view information such as Used Space and Backup Plans from two dimensions: Vault Resources and Organization Resources. Note Operations administrators can view resource statistics for all organizations. Organization administrators can view resource statistics only for their own organization. |
|   | Log Management | You can view logs of all operations in the system, including creation, deletion, and execution of backup plans and backup and restoration. |
|   | Parameter Configuration | Operations administrators can centrally configure parameters for product backup and restoration, as well as expired fragment cleanup for HBR-Backend and HBR-Storage. Note HBR-Backend expired fragment cleanup: applies only to storage repositories, PolarDB Cluster Edition storage repositories, Tablestore repositories, and container storage repositories. HBR-Storage expired fragment cleanup: applies only to deduplicated storage repositories. |
| 8 | > Document Version: 2026070 |   |

|   | Event Management | You can view all event records and logs. You can filter events by event type, event status, start time, or end time. |
|---|---|---|
