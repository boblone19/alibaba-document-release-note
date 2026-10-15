---
title: "Elastic File System NAS Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 11
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Elastic File System NAS Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%98%BF%E9%87%8C%E4%BA%91%E5%BC%B9%E6%80%A7%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20EFS-NAS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elastic%20File%20System%20NAS%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Elastic File System NAS Product Introduction 20260701

Elastic File System NAS Product I

## Product details

Alibaba Cloud Elastic File Storage NAS (EFS-NAS) is a file storage service for compute nodes, such as Alibaba Cloud Elastic Compute Service (ECS) instances, E-HPC, and container services. It is a distributed file system that provides shared access, elastic scaling, high reliability, and high performance.

**Instance types**

EFS-NAS supports capacity-optimized and compute-optimized instance types to meet different business scenarios. Capacity-based instance Based on hybrid servers with both Solid-State Drives (SSDs) and Hard Disk Drives (HDDs). Provides a large-capacity, cost-effective solution for shared file storage. Suitable for cost-sensitive scenarios such as records management, data archiving, and video surveillance playback. Performance-oriented instance Based on all-flash servers with SSDs. Provides high-throughput, low-latency file access. Suitable for performance-sensitive scenarios such as high-performance computing (HPC), media editing, and database file storage. File system mounting: You can mount a file system to multiple clients. Elastic scale-out: You can scale out file systems online to dynamically adjust capacity as your business grows. Mount targets: You can create mount targets for sharing through the Network File System (NFS) or Server Message Block (SMB) protocol. Quota management: You can set capacity quotas for organizations to achieve efficient resource allocation, cost control, and performance optimization. Single namespace capacity: The system allows a maximum capacity of 5 PiB for unified management of massive data. Maximum scale of a single cluster: The system supports up to 2,000 disks and scale-out as needed. Three-server initial deployment: You can start with a small-scale deployment and scale out smoothly as your business grows. Flexible storage pool deployment: The system supports dedicated resources and flexible planning for the underlying file storage cluster, reducing the initial investment in hardware.

**Protocol support and multi-protocol interoperability**

NFS v3.0 and NFS v4.0 protocols are supported. SMB 2.1 and SMB 3.0 protocols are supported. Multi-protocol interoperability: You can access the same directory or file using both the NFS and SMB protocols. This meets file sharing needs across different operating systems and application scenarios. Elastic File System NAS Product I

**Data security and permission management**

Triplicate protection: Data is stored in multiple replicas for redundancy. This ensures high availability (HA) and data security. Erasure coding (EC) protection: The system supports multiple data protection policies, including 2+1, 4+2, 8+3, 4+2:1, and 8+2:1 modes, to improve storage efficiency and reliability. ACL: The system supports Windows Access Control Lists (ACLs) and Linux POSIX ACLs for file access control. Security group control: You can set read and write access policies based on client IP addresses.

**Auditing and compliance**

You can query operation logs through ActionTrail to meet enterprise auditing and compliance requirements.

**Product advantages**

Balanced performance and capacity: The system delivers high-performance, low-latency storage while maintaining massive capacity and cost efficiency. Multi-protocol interoperability and hybrid access: The same data source can be directly accessed by different systems, improving cross-platform collaboration efficiency. Flexible and elastic deployment: Online scale-out and resource pooling management adapt to evolving business lifecycles. HA and data security: The combination of triplication and EC ensures HA and optimizes storage utilization. Fine-grained security and auditing: Multi-level ACLs, security group policies, and access auditing meet the security and compliance requirements of enterprises, government agencies, and financial institutions. Elastic File System NAS Product I

## Product value

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

The management console and APIs support real-time monitoring of capacity, performance, and health status. They also provide automatic alerts and scale-out. This improves O&M efficiency and control. Elastic File System NAS Product I

## Scenarios

Network Attached Storage (NAS) is widely used in the government, enterprise, finance, and manufacturing sectors. EFS-NAS provides easy file sharing, flexible scaling, and robust security. Its core benefits include centralized management, flexible scale-out, fast retrieval, security protection, and cross-regional collaboration. These features address common challenges associated with traditional storage, such as limited capacity, performance issues, and difficulties with management and compliance.

**Government and enterprise sectors**

E-government and business file management: Centrally store and manage official documents, approval files, and image files. This enables efficient file sharing and collaboration across departments and regions. Public safety and law enforcement forensics: Store high-definition (HD) video surveillance footage, data from law enforcement recorders, and audit logs. This supports fast retrieval and long-term archiving to meet regulatory and classified protection requirements. E-prosecution for judicial authorities: Integrate with business systems to ensure real-time synchronization of case files and evidence across multiple nodes. This improves case handling efficiency and traceability.

**Finance industry**

File and image archive management: Centrally store customer images, scanned contracts, and counter receipts. This allows for fast retrieval and disaster recovery to meet compliance requirements. Business reporting and file sharing: Provides a unified file access platform for branch offices to improve internal data distribution and collaboration efficiency. Active-active/high availability (HA) business support: The high availability and replication features of the NAS file system support dual-center operations for electronic imaging and compliance record-keeping systems. This ensures business continuity.

**Manufacturing industry**

Industrial design and R&D data management: Centrally manage large files, such as computer-aided design (CAD) drawings, process documents, and test videos. NAS supports metadata tags and full-text search to speed up design iterations. Production process and quality traceability: Store process parameters, device logs, and inspection images from production lines. This enables fast queries based on criteria such as batch or time to support quality management. Cross-plant collaboration and supply chain sharing: Securely share production materials and order files among multiple factories and suppliers. This enables real-time collaboration and ensures version consistency.

| Feature | Description |
|---|---|
| File system type | Capacity-based: Provides storage-optimized instances based on hybrid flash servers with both SSDs and HDDs. These instances are suitable for cost-sensitive and less latency-sensitive file sharing services, such as database backups, log storage, Windows user directories, and Linux home directories. Performance-oriented: Provides compute-optimized instances based on all-flash servers with SSDs. These instances are suitable for latency-sensitive file sharing services that require fast responses, such as Linux/Windows enterprise applications, container PersistentVolumes (PVs), web content management, and gene computing. |
| File system capacity | A single file system supports a maximum capacity of 5 PiB. |
| Protocol interoperability | Supports NFS v3.0, NFS v4.0, NFS v4.1, SMB 2.1, and SMB 3.0 protocols. You can select the protocol version to mount the file system based on the application scenario. The same folder or file can be accessed using both NFS and SMB protocols. This meets file sharing requirements across different operating systems and application scenarios. |
| Quota management | Supports setting capacity quotas for organizations. This helps with resource allocation, cost control, and performance optimization. |
| Mount target | Supports creating mount targets for shares that use the NFS or SMB protocol. |
| Mount | Supports mounting a file system to multiple compute nodes using a mount target. |
| Elastic scale-out | Supports online scale-out. You can dynamically adjust the capacity as your business grows. |

| Feature | Description |
|---|---|

Elastic File System NAS Product I

## Features

This topic describes the features of EFS-NAS.

**Reliability and data security**

| Triplicate | Each data block (Chunk) is copied into three identical replicas. These replicas are stored on different nodes in the cluster based on a specific policy. This ensures that if a node fails, data can still be recovered from other nodes. This feature provides high data reliability and protects user data. |
|---|---|
| Erasure coding (EC) | EC technology divides data into n data blocks and m parity blocks, which form an n+m EC group. These blocks are stored on different servers. If m or fewer blocks are lost, the lost blocks can be recovered using the EC algorithm. The supported EC patterns are 2+1, 4+2, 8+3, 4+2:1, and 8+2:1. |
| NFS access control | NFS shares support configuring permissions, such as read/write and read-only, and rules, such as root squash and all squash, based on client IP addresses or CIDR blocks. |
| User/Group | For SMB protocol shares, you can manage permissions by user or group. You can assign different permission levels, such as read/write, read-only, or full control, to different users or groups to ensure data access security. |
| Audit log | Supports querying operation logs through ActionTrail to meet enterprise audit and compliance requirements. |
| Snapshot | Use snapshots to periodically back up business data on your file system. This protects against data loss caused by accidental operations, attacks, or viruses. You can set a policy to delete snapshots when they expire. Custom expiration policies and permanent retention are supported. A single file system supports up to 2,048 snapshots. The recommended number of snapshots to retain is 128. A maximum of 8,192 snapshots can be created across all file systems. |
| Recycle bin | Enable the recycle bin to prevent business disruptions or permanent data loss from accidental file deletion. When enabled, deleted files and folders are temporarily stored in the recycle bin. You can set a retention policy. Files are permanently deleted after the retention period ends. You can recover files during the retention period. |
| QoS configuration | To prevent a file system from using too many system resources, O&M engineers can configure Quality of Service (QoS) policies through a graphical user interface. These policies limit the maximum bandwidth and operations per second (OPS) for file system reads and writes. |

Elastic File System NAS Product I

**Deployment**

| Feature | Description |
|---|---|
| Initial size | Requires a minimum of three nodes. |
| Maximum size of a single cluster | 2,000 disks. |
| Storage pool | The underlying file storage cluster supports exclusive use. This provides flexibility in deployment planning and reduces the number of devices required for initial setup. |

Elastic File System NAS Product I
