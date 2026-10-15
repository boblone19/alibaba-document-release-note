---
title: "cloud migration hub Product Introduction 20260303"
product_version: "V3.18.6"
pdf_pages: 12
source_pdf: "d63faea2b44a8113_Alibaba Cloud Apsara Stack V3.18.6 cloud migration hub Product Introduction 20260303.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E8%BF%81%E7%A7%BB%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20cloud%20migration%20hub%20Product%20Introduction%2020260303.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# cloud migration hub Product Introduction 20260303

## Table of Contents

- 1 What is Alibaba Cloud Migration Center (AMC)?
- 2 Product value
- 3 Scenarios
- 4 Features

aba Cloud Migration Center (AMC )?

## 1 What is Alibaba Cloud Migration Center (AMC)?

**Migration Center (AMC)?**

Alibaba Cloud Migration Center (AMC) leverages extensive cloud migration experience to help you migrate systems to the cloud or between clouds, addressing diverse migration needs. As a core engine for enterprise digital transformation, AMC provides an end-to-end, intelligent cloud migration system built on four pillars: centralized management, comprehensive product coverage, best practices, and application-centric services. This system helps enterprises achieve efficient, secure, and low-cost cloud migration.
1. Centralized management: A single platform for end-to-end cloud migration
End-to-end coverage: AMC covers the entire migration process, from survey and planning to preparation, testing, execution, and validation. You can perform all migration operations on a single platform. Automated operations: AMC collects configuration information and runtime status from migration sources. Based on migration conditions, such as network bandwidth, it automatically designs task execution strategies, differentiated adaptation solutions, and data validation methods. This process requires no manual intervention. You can bypass complex configurations and complete the migration with just a few clicks. Process visualization: AMC provides an end-to-end tracking dashboard that displays migration progress and resource status in real time. It collects key metrics during migration, such as network transmission success rate, migration bandwidth utilization, and source resource workload. The system automatically triggers alerts if anomalies are detected.
2. Comprehensive product coverage: Unified management for various resource types
Servers: Supports the migration of on-premises servers and virtual machines (VMs) to the cloud, along with cross-cloud VM migration. VMware: Supports agentless migration of on-premises VMware clusters to the cloud. Operating systems: Supports upgrades for End-of-Life (EOL) systems or refactoring to compliant operating systems. Storage: Supports NAS migration to the cloud and OSS cross-cloud migration. Databases: Supports MySQL database migration to the cloud and cross-cloud migration.
3. Best Practices: Meeting enterprise demands for data security, business stability, and
migration efficiency Business continuity priority: Data migration is performed while ensuring the migration source operates under a secure workload. AMC monitors the runtime status of migration sources in real time during the migration. It automatically triggers circuit breakers if abnormal business risks are detected. Resource utilization: AMC maximizes overall migration efficiency by executing migration tasks in batches, adaptively adjusting synchronization rates, and performing data validation during off-peak hours. This approach fully utilizes resources such as migration network bandwidth, traffic, and CPU. Compatibility and extensibility: The platform includes built-in adaptation rules for crossversion migration. It scans for differences and performs automatic adaptation. The migrated system is brought online only after thorough testing and validation. If required, AMC supports version upgrades, instance type enhancements, and application cluster scaling during the migration. aba Cloud Migration Center (AMC )? Data consistency and integrity: By default, AMC uses secure transmission protocols for all resources to ensure data transmission integrity at the network layer. It supports integrity validation during data synchronization to improve validation efficiency. The platform performs layered data validation, from global to local, with recursive checks at each layer to quickly identify problematic data.
4. Application-centric services: Managing migration from a business perspective
Application migration plan: You can combine all resources for an application into a single migration plan. AMC then executes the resource migration actions from the bottom up, based on the application's architectural dependencies. Application-level resource mapping: You can build mapping relationships between source and cloud resources at the application level. AMC visually displays the application architecture topology, which simplifies the management of the entire application migration lifecycle. Application-level business cutover: You can orchestrate business cutover actions. AMC monitors the runtime status of both source and cloud resources and detects the progress of data synchronization and cutover actions in real time. The unified platform enables multiple teams to collaborate. It supports real-time information synchronization for multiple roles, such as business, technical, and O&M, to reduce communication costs. e

## 2 Product value

This document describes the value and features of Cloud Migration Center.

**Centralized management**

It covers the end-to-end migration lifecycle—assessment, planning, preparation, testing, execution, and validation—all in one platform. It requires no manual intervention and eliminates complex configuration. You can start a migration with a single click. It provides an end-to-end tracking dashboard that shows real-time migration progress and resource status. It captures key metrics during migration to visualize the entire process.

**Support for mainstream products**

You can migrate on-premises servers or virtual machines to the cloud. You can also migrate virtual machines across clouds. You can migrate on-premises VMware clusters to the cloud without installing agents. You can upgrade end-of-life (EOL) systems or rebuild operating systems to meet compliance requirements. You can migrate NAS to the cloud and migrate OSS across clouds. You can migrate MySQL databases to the cloud and across clouds.

**Built on best practices**

You can maximize overall migration efficiency by running migration tasks in batches, automatically adjusting sync rates, and scheduling data validation during off-peak hours. This ensures full utilization of migration network bandwidth, traffic capacity, and CPU resources. You can perform data migration under secure workload conditions at the migration source. You can monitor the source’s runtime status in real time. It automatically halts migration if abnormal business risks are detected. All resources use secure transmission protocols by default. This ensures data integrity at the network layer.

**Services for applications**

You can group all resources belonging to an application into a migration plan. You can migrate resources from the bottom up, following the application’s architectural dependencies. You can map source resources to cloud resources by application. You can visualize the application architecture topology. You can manage the full lifecycle of application migration to the cloud. You can orchestrate cutover actions for business migration. You can monitor the runtime status of both source and cloud resources. It detects real-time progress of data synchronization and cutover actions. It enables cross-team collaboration through a unified platform.

## 3 Scenarios

Cloud Migration Hub provides a variety of features to help customers migrate to the cloud efficiently. It significantly reduces migration risks and workload, making it suitable for a wide range of cloud migration scenarios.

**Server migration**

Migrate on-premises servers to the cloud: You can use Cloud Migration Hub to migrate servers from an on-premises data center to Alibaba Cloud. This lets you fully leverage the cloud's high availability, security, and elasticity. Migrate on-premises virtual machines to the cloud: Cloud Migration Hub supports migrating on-premises virtual machines, such as VMware, Virtual Box, XEN, KVM, and Hyper-V, to Apsara Stack. Cross-cloud virtual machine migration: Cloud Migration Hub supports the smooth migration of Elastic Compute Service instances from other cloud providers to Apsara Stack. This ensures data security and business continuity. It also helps businesses benefit from Alibaba Cloud's competitive products, services, and pricing.

**Migrate on-premises VMware clusters to the cloud**

No agent installation is required. The migration client runs outside the virtual machine. It does not consume virtual machine resources. High migration efficiency: You can perform batch migrations without installing an agent on each virtual machine. This saves time and labor costs. No business security concerns: No operations are performed within the virtual machine's operating system. This eliminates business security concerns.

**Operating system replacement**

You can replace Linux distributions that are no longer officially maintained, such as CentOS 7 and CentOS 8, with newer operating system versions. This provides a longer maintenance lifecycle and technical support. If your current operating system does not meet business or compliance requirements, or to change the system architecture, you can replace the operating system to improve system reliability and performance.

**Storage migration**

OSS to OSS migration: You can migrate data between Alibaba Cloud Object Storage Service (OSS) buckets. This is ideal for large-scale object storage. Under standard conditions, data remains synchronized and consistent. The migration is stable and does not cause interruptions. This helps you manage data in a unified way. NAS to OSS migration: You can efficiently migrate large volumes of files from on-premises or cloud-based Network Attached Storage (NAS) to Alibaba Cloud OSS. Under standard conditions, file data remains synchronized and consistent. The migration is stable and does not cause interruptions. This meets long-term storage requirements. NAS to NAS migration: You can efficiently migrate files from on-premises or cloud-based NAS to Alibaba Cloud NAS. This is ideal for large-scale file storage. Under standard conditions, file data remains synchronized and consistent. The migration is stable and does not cause interruptions. This allows for the integration and optimization of file storage on the cloud.

**Database migration**

Migrate on-premises databases to the cloud: Cloud Migration Hub supports the smooth migration of on-premises MySQL databases to Apsara Stack. This lets you benefit from elastic scaling, a high availability (HA) architecture, and fully managed O&M. You do not need to build your own data center or perform manual maintenance. This significantly reduces costs and improves reliability. Cross-cloud database migration: Cloud Migration Hub supports database migration between Apsara Stack environments. It uses strategies such as data consistency verification and dynamic speed adjustment. This ensures data security and maintains business continuity without noticeable interruptions. It easily handles requirements such as cross-region disaster recovery, resource consolidation, and architecture upgrades. Database migration for domestic technology initiatives: To meet the demand for replacing foreign technology with domestic alternatives, Cloud Migration Hub supports migrating MySQL databases to PolarDB for MySQL. This satisfies domestic compliance and performance requirements.

## 4 Features

This topic describes the features of Apsara Migration Center (AMC) in the Apsara Uni-manager Management Console.

| Feature |   |   | Description |
|---|---|---|---|
| Guidance Center |   |   | This feature provides a one-stop guide for AMC and covers applicable scenarios, supported operating systems, standardized migration procedures, and basic environment preparation requirements, which helps users quickly understand and initiate cloud migration tasks. |
| Dashboard |   |   | This feature provides a visual overview of the overall cloud migration progress. It displays the completion status of migration plans, operational status of various tasks, and the number of completed tasks. This helps users monitor the migration progress in real time. |
| Resource Migration |   |   | This feature provides end-to-end resource migration management and execution capabilities and supports a full lifecycle migration process from assessment and survey to result verification. Based on automated workflow orchestration and visual monitoring, this feature enables efficient cloud migration across multiple scenarios, including servers, VMware, operating systems, storage, and databases, thereby reducing migration complexity and improving overall efficiency. |
|   |   | Migration Sources | Server migration allows you to migrate one or more migration sources to Apsara Stack. Migration sources include physical servers, virtual machines (VMs), cloud instances from other cloud platforms, or other types of servers. Import the information about a migration source by using the CLI Import the information about a migration source by using the Server Migration Center (SMC) console Import the information about a migration source by using the SMC client Import the information about a migration source by configuring the Server Migration Connector without agents |

|   |   | Migration Tasks | Create a server migration task AMC allows you to migrate data from servers in self-managed data centers, on-premises VMs, or third-party cloud servers to Apsara Stack. Supported VMs include VMware, VirtualBox, Xen, KVM, and Hyper-V. Third-party cloud servers include servers on Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), Tencent Cloud, UCloud, China Telecom e-Cloud, and QingCloud. Create an agentless migration task for a VMware VM AMC provides the non-intrusive migration technology to help you migrate VMware VMs to Apsara Stack without the need to install agents. This improves the efficiency of business migration to Apsara Stack and eliminates your concerns about business security and business performance during the migration process. Create an OS replacement task You can seamlessly migrate the operating systems of ECS instances from CentOS 7/8 and Anolis OS 7/8 to Alibaba Cloud Linux V3 64bit for longer maintenance periods and enhanced technical support. You can upgrade Alibaba Cloud Linux 2 to Alibaba Cloud Linux 3. |
|---|---|---|---|
| Advanced Services | Server Migration |   |   |

|   | Cross-platform Application Scanning | This feature automates the analysis of software packages and source code and supports mainstream programming languages and Chinese-made processor architectures. It assesses migratability, identifies compatibility issues, and provides migration recommendations, helping users efficiently accomplish the migration tasks of heterogeneous platforms. Software package evaluation Checks the shared object (SO) dependency libraries and executable files that are included in user software packages (such as RPM, TAR, ZIP, and GZIP files) and assesses the migratability of these SO dependency libraries and executable files. Checks the SO dependency libraries and binary files included in user JAR packages and assesses the migratability of the JAR packages. Source code scanning Checks the source code written in C/C++, Java, Python, Go, and Rust, and provides guidance on how to migrate the source files. Checks the user build project files and provides guidance on how to migrate these files. Checks the link libraries used in the user's software build project files and provides migratability information. Supports compatibility scanning for Chinese- made processors such as Kunpeng, Hygon, and ShenWei. |
|---|---|---|
|   | JVM Parameter Tuning | This feature intelligently generates, optimizes, migrates, and queries JVM parameters. It supports multiple versions and architectures to improve the efficiency and stability of Java application migration. Parameter Generation: provides a visual interface to integrate commonly used JVM parameters and automatically generate accurate JVM parameter strings. Parameter Optimization: provides optimization suggestions based on the existing parameters and environment information. Parameter Migration: allows you to migrate the native JVM parameters to the destination version and environment, and automatically recommends modification solutions. Parameter Query: allows you to query one or more JVM parameters and displays their associated module, parameter type, value type, and detailed descriptions. |
