---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Elastic File System NAS Product Introduction 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 12
source_pdf: "e24be106bfa0cb1d_Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Elastic File System NAS Product Introd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/CDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Defined%20Storage%20Elastic%20File%20System%20NAS%20Product%20Introduction%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Elastic File System NAS Product Introduction 20260831

## Table of Contents

- 1 Product details
- 2 Product value
- 3 Scenarios
- 4 Functions and features

## 1 Product details

Alibaba Cloud Elastic File Storage NAS (EFA-NAS) is a file storage service for compute nodes such as Elastic Compute Service (ECS) instances, Elastic High Performance Computing (E- HPC), and container services. It is a shared, scalable, highly reliable, and high-performance distributed file system.

**Service types**

EFS-NAS supports two instance types, capacity and performance, to meet different business scenarios. Capacity instances Run on servers with a mix of Solid-State Drives (SSDs) and Hard Disk Drives (HDDs). Provide a large-capacity, cost-optimized shared file storage solution. Suitable for cost-sensitive scenarios such as archive management, data archiving, and video surveillance playback. Performance instances Run on all-flash SSD servers. Provide high-throughput, low-latency file access. Suitable for performance-sensitive scenarios such as high-performance computing (HPC), media editing, and database file storage.

**Core features**

File system mounting: Multiple clients can mount the file system. Elastic scaling: You can scale out the file system online and dynamically adjust the capacity as your business grows. Mount points: You can generate mount points through Network File System (NFS) or Server Message Block (SMB) protocol shares. Quota management: You can set capacity quotas by organization to achieve rational resource allocation, cost control, and performance optimization. Unique namespace capacity: A single namespace supports up to 5 PiB of capacity for unified management of mass data. Maximum cluster scale: A single cluster supports up to 2,000 disks and scales out horizontally on demand. Minimum three-node deployment: You can start with three nodes to meet the needs of small-scale business and smooth scaling. Flexible storage pool deployment: You can dedicate and flexibly plan resources at the underlying layer of the storage cluster to reduce initial equipment investment.

**Service features**

**Protocol support and multi-protocol interoperability**

The system supports the NFS v3.0, NFS v4.0, and NFS v4.1 protocols. The system supports the SMB 2.1 and SMB 3.0 protocols. Multi-protocol interoperability: You can access the same directory or file through multiple protocols such as NFS and SMB to meet file sharing requirements across operating systems and various application scenarios. The system supports IPv4/IPv6 dual-stack networks, and clients can access the file system through IPv4 or IPv6 addresses.

**Data security and permission management**

Triplicate protection: The system stores data in multiple replicas to ensure high availability and data security. Erasure coding protection: The system supports multiple data protection schemas, including 2+1, 4+2, 8+3, 4+2:1, and 8+2:1, to improve storage efficiency and reliability. Access control list (ACL) access control: The system supports Windows ACL and Linux POSIX ACL file access control. Security group control: You can set read/write access RAM policies based on client IP addresses.

**Audit and compliance**

You can query operation logs through audit trail to meet enterprise audit and compliance requirements.

**Benefits**

Performance and capacity: The service meets both high-performance, low-latency requirements and mass low-cost storage needs. Multi-protocol interoperability and cross-platform access: Different systems can directly access the same data source to improve multi-platform collaboration efficiency. Flexible and elastic deployment: Online scaling and resource pooling adapt to different business lifecycles. High availability and data security: The combination of triplicate storage and erasure coding ensures high reliability and optimizes storage utilization. Fine-grained security and audit: Multi-level ACL permissions, security group policies, and access audits meet the security, compliance, and regulatory requirements of industries such as government and finance.

## 2 Product value

**High availability and data reliability**

Multiple replicas and an erasure coding data redundancy mechanism ensure service availability during hardware failures and prevent data loss.

**Shared consistency and high-concurrency performance**

Multiple compute instances can access the same data source simultaneously. File locks and transaction mechanisms ensure strong consistency. Optimized I/O scheduling and a distributed architecture maintain stable throughput and low latency during high-concurrency access.

**Protocol and ecosystem interoperability**

Support for standard protocols, such as NFS v3, NFS v4.0, SMB 2.1, and SMB 3.0, ensures compatibility with major Linux and Windows systems. This allows for seamless integration with existing business systems and reduces migration costs.

**Multiple access methods**

You can access resources securely within the cloud through a VPC, or connect on-premises data centers to the cloud using leased lines and VPNs. This provides low-latency, cross-region access to support hybrid cloud and multi-data center deployments.

**Security and compliance**

The product provides fine-grained access control, encryption for data in transit and at rest, and access auditing. These features ensure end-to-end data security and help you meet industry and regulatory requirements.

**Easy O&M and visual management**

The management console and APIs support real-time monitoring of capacity, performance, and health status. They also provide automatic alerts and scale-out. This improves O&M efficiency and control.

## 3 Scenarios

Network Attached Storage (NAS) is widely used in the government, enterprise, finance, and manufacturing sectors. EFS-NAS provides easy file sharing, flexible scaling, and robust security. Its core benefits include centralized management, flexible scale-out, fast retrieval, security protection, and cross-regional collaboration. These features address common challenges associated with traditional storage, such as limited capacity, performance issues, and difficulties with management and compliance.

**Government and enterprise sectors**

E-government and business file management: Centrally store and manage official documents, approval files, and image files. This enables efficient file sharing and collaboration across departments and regions. Public safety and law enforcement forensics: Store high-definition (HD) video surveillance footage, data from law enforcement recorders, and audit logs. This supports fast retrieval and long-term archiving to meet regulatory and classified protection requirements. E-prosecution for judicial authorities: Integrate with business systems to ensure real-time synchronization of case files and evidence across multiple nodes. This improves case handling efficiency and traceability.

**Finance industry**

File and image archive management: Centrally store customer images, scanned contracts, and counter receipts. This allows for fast retrieval and disaster recovery to meet compliance requirements. Business reporting and file sharing: Provides a unified file access platform for branch offices to improve internal data distribution and collaboration efficiency. Active-active/high availability (HA) business support: The high availability and replication features of the NAS file system support dual-center operations for electronic imaging and compliance record-keeping systems. This ensures business continuity.

**Manufacturing industry**

Industrial design and R&D data management: Centrally manage large files, such as computer-aided design (CAD) drawings, process documents, and test videos. NAS supports metadata tags and full-text search to speed up design iterations. Production process and quality traceability: Store process parameters, device logs, and inspection images from production lines. This enables fast queries based on criteria such as batch or time to support quality management. Cross-plant collaboration and supply chain sharing: Securely share production materials and order files among multiple factories and suppliers. This enables real-time collaboration and ensures version consistency.

## 4 Functions and features

This topic describes the functions and features of EFS-NAS.

**Basic features**

| Feature | Description |
|---|---|
| File system type | Capacity: Hybrid flash servers based on Solid State Drives (SSDs) and Hard Disk Drives (HDDs) provide capacity-type instances. These instances apply to cost-sensitive file sharing workloads that do not require low-latency responses, such as database backup, log storage, Windows user directories, and Linux home directories. Performance: All-flash servers based on SSDs provide performance- type instances. These instances apply to latency-sensitive file sharing workloads that require high response speeds, such as Linux and Windows enterprise applications, container Persistent Volumes (PVs), web content management, and genomic computing. |
| File system capacity | A single file system supports a maximum capacity of 5 PiB. |
| Protocol interoperability | The system supports NFS v3.0, NFS v4.0, NFS v4.1, SMB 2.1, and SMB 3.0 protocols. You can select the protocol version for mounting the file system based on your application scenario. Multiple protocols such as Network File System (NFS) and Server Message Block (SMB) can access the same directory or file, meeting file sharing requirements across operating systems and various application scenarios. |
| Quota management | The system supports capacity quotas by organization to enable rational resource allocation, cost control, and performance optimization. You can set directory quotas, user quotas, and user group quotas for specified directories. Each quota type supports both capacity and file count dimensions, and the system enforces fine-grained storage resource control through three levels: hard quotas, soft quotas, and advisory quotas. |
| Mount point | You can generate mount points through NFS or SMB protocol shares. |
| IPv4/IPv6 dual-stack | The system supports IPv4 and IPv6 dual-stack network access. When creating an NFS or SMB share, you can select the IPv4 or IPv6 protocol version. Clients can mount and access the file system through IPv4 and IPv6 addresses. A single file system supports simultaneous creation of IPv4 and IPv6 mount points. |
| Mount | You can mount the file system to multiple clients through mount points. The console enables batch mounting or unmounting of NFS shares to multiple Elastic Compute Service (ECS) instances, and the system automatically executes mount commands through the ECS Cloud Assistant. |

| Elastic scaling | You can scale out the capacity online and dynamically adjust it as your business grows. |
|---|---|

**Reliability and data security**

| Feature | Description |
|---|---|
| Three replicas | The system replicates each chunk into three identical replicas and distributes these replicas across different nodes in the cluster based on a defined strategy. This approach ensures that data remains recoverable from other nodes even if a node fails, providing high data reliability and protecting user data security. |
| Erasure coding (EC) | Erasure coding divides data into n data chunks and m parity chunks to form an n+m EC group. These chunks reside on different servers. When any number of chunks up to m are lost, the EC algorithm recovers the lost chunks. The system supports 2+1, 4+2, 8+3, 4+2:1, and 8+2:1 EC schemas. |
| NFS access control | NFS shares support read/write and read-only permissions based on client IP addresses or CIDR blocks, as well as rules such as root squashing and all squashing. |
| User/user group | SMB protocol shares support permission management by user or user group. You can assign different permission levels such as read/write, read-only, and full control to different users or user groups to ensure data access security. |
| Audit log | You can query operation logs through the audit trail feature to meet enterprise audit and compliance requirements. |

| Snapshot | Snapshots enable periodic backup of file system business data to mitigate the risk of data loss caused by accidental operations, attacks, or viruses. Snapshots include two types: normal snapshots and scheduled snapshots, which address different data protection requirements. Normal snapshot: Users manually create this type of snapshots for instant backup before critical operations such as system upgrades, configuration changes, and data migration. Scheduled snapshot: The system automatically generates this type of snapshots on a periodic basis according to a scheduled snapshot policy. Scheduled snapshots apply to daily backup of critical directories in production environments, meetting long-term protection requirements such as data compliance retention, accidental deletion prevention, and automated O&M. You can also configure an expiration deletion policy for snapshots, supporting custom expiration policies or permanent retention. A single file system supports a maximum of 2,048 snapshots. We recommend that you retain 128 snapshots. All file systems combined support a maximum of 8,192 snapshots. |
|---|---|
| WORM | Write Once Read Many (WORM) is a feature that protects file data security. After you enable a WORM policy, the system enforces strict access control on files within the specified protection period to ensure that data cannot be modified after it is written. This effectively prevents accidental operations, malicious deletion, and ransomware attacks. |
| Recycle bin | To prevent business disruption or permanent data loss caused by accidental file deletion, you can enable the recycle bin feature. After enabling this feature, the system temporarily stores deleted files or directories in the recycle bin. You can configure a retention policy so that the system permanently deletes recovered files after the specified retention period expires. Users can restore these files during the retention period. |
| QoS configuration | To prevent a file system from consuming excessive system resources, O&M personnel can configure QoS policies for the file system through the graphical interface to limit the maximum read/write bandwidth and maximum IOPS of the file system. |
| Batch freeze, restore, and deletion | The console supports batch freeze and batch restore operations on multiple file systems for batch lifecycle management. A file system in the frozen status suspends all read and write access and does not support scale-out or deletion operations. You must restore the file system before deleting it. The system supports both single and batch deletion of file systems. You cannot delete a file system in the frozen status. |

**Deployment**

| Feature | Description |
|---|---|

| Initial scale | A minimum of three nodes are required. |
|---|---|
| Maximum cluster scale | 2,000 disks. |
| Storage pool | The file storage cluster infrastructure supports dedicated storage pools. This enables flexible planning and deployment and reduces the initial device investment. |
| Multi-region | The system supports multi-region deployment and unit-region deployment to meet different business deployment requirements. |
