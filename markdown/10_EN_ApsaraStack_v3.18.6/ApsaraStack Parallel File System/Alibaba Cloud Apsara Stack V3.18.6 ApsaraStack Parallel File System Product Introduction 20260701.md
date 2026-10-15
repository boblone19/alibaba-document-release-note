---
title: "ApsaraStack Parallel File System Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 11
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 ApsaraStack Parallel File System Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%AB%98%E6%80%A7%E8%83%BD%E5%B9%B6%E8%A1%8C%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8APFS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraStack%20Parallel%20File%20System%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# ApsaraStack Parallel File System Product Introduction 20260701

ApsaraStack Parallel File System

## Product overview

ApsaraStack Parallel File System (APFS) is a high-performance parallel file system for Apsara Stack. It delivers the high performance required for large-scale parallel training in intelligent computing scenarios and provides intelligent data management, reliable security, flexible deployment, and resource scalability. APFS is suitable for scenarios such as AIGC, autonomous driving, electronic design automation (EDA) simulation, and computer graphics (CG) rendering. The following figure shows the service architecture.

**Application protocol**

APFS is a high-performance parallel file storage service. For pre-training and full-parameter fine-tuning scenarios, it provides a high-performance file system that is compliant with the Portable Operating System Interface (POSIX) standard for training on multiple multi-GPU servers. This allows data and applications to run on the distributed file system without modification.

**Data processing**

The distributed storage architecture provides sub-millisecond data access and a read/write throughput of tens of GB/s. Storage clusters support security isolation based on performance, capacity, and data to provide multitenancy. Seamless data flow with OSS streamlines business processes, such as training and inference.

**Underlying hardware**

Storage clusters support Intel and Hygon hardware. Client clusters support Intel, Hygon, and Kunpeng hardware. ApsaraStack Parallel File System

## Benefits

**Ultra-High Performance**

Both APFS clusters and single file systems support TB-level throughput capacity. Enterprise-grade NVMe SSD media. Data access links use RDMA high-speed networks. Fully parallel I/O access model. Compute nodes and all storage servers within the APFS storage cluster can establish connections in parallel and read data simultaneously. Distributed metadata. Metadata is chunked based on the directory tree structure and distributed to multiple service nodes, which provide services simultaneously.

**Scalability**

Online seamless storage capacity expansion. Performance scales elastically with capacity. It supports online expansion of storage nodes, which is transparent to applications. It also supports online hot upgrades of backend storage service systems and the dynamic addition and removal of disks without service interruption. Distributed metadata. A single file system handles 10 billion files. With a fully symmetric architecture for data and metadata, POSIX clients can access all service nodes in parallel. Throughput and IOPS grow linearly with capacity, reaching up to TB-level throughput and millions of IOPS. This meets the high-performance access requirements for large and massive small files in artificial intelligence, HPC, and machine learning.

**Cost-Effectiveness**

Data is stored using EC erasure coding. It supports 4D+2P specifications. ApsaraStack Parallel File System

## Common scenarios

**AIGC**

APFS works with Object Storage Service (OSS) and File Storage NAS to form a complete solution. It provides persistent storage for model training that requires millions of image assets and for AI art files created by users. APFS delivers up to 100 Gbps of throughput, accelerating data read and write performance during training. This speeds up model training and inference, shortens time-to-market for new services, and reduces wait times for AI art generation.

**Autonomous driving**

In autonomous driving, APFS’s ultra-high performance improves GPU computing resource utilization. Its cloud-based scalability and instant availability reduce operations management costs. APFS enables seamless integration between on-premises and cloud environments and supports the full data lifecycle — upload, compute, distribution, and archiving. It lowers data storage cost and supports dataflow with OSS, meeting both elastic compute needs and data storage cost optimization goals.

**HPC storage**

APFS integrates with ACK and Serverless Container Service to build fast, low-cost, and highprecision container environments for genomic computing. It serves as shared storage for genomic data analysis and stores raw sequencing data, assembled data, and intermediate results. It meets genomics users’ requirements for low latency and high IOPS, reduces data copying and transfer, and syncs computation results to Object Storage Service (OSS). APFS integrates with OSS to provide mass storage capacity. Using lifecycle management, APFS archives cold data to Archive Storage to lower storage cost.

| Feature | Description |
|---|---|
| File system management | You can create, view, and delete file systems on the APFS console. APFS provides standard open APIs for these operations. |
| Multi-tenancy | APFS allows you to manage file systems and mount targets for multi-level organizations and resource sets. |
| Quota management | APFS allows you to manage quotas based on organizations and resource sets. You can manage the capacity usage of various organizations and resource sets. |
| Usage statistics | You can collect statistics on the used capacity of an APFS file system. You can view capacity information, such as physical capacity usage, physical capacity usage trend, and logical capacity usage, on the APFS console. |
| Supported protocols | Network protocols: The RDMA over Converged Ethernet (RoCE) and 100G Ethernet protocols are supported. Storage protocols: The Portable Operating System Interface (POSIX) standard is supported. You can run your data and application software on APFS without the need to modify them. |
| Hardware compatibility | Intel and Hygon hardware can be used for storage clusters. Intel, Hygon, and Kunpeng hardware can be used for client clusters. |
| Client mount | APFS supports batch mount and automatic mount of clients. |

| Feature | Description |
|---|---|

ApsaraStack Parallel File System

## Features

This topic describes the features of ApsaraStack Parallel File System (APFS).

**Reliability and availability**

| Erasure coding (EC) of data | APFS splits raw data into multiple data fragments and generates a specific number of parity fragments through calculation. These data fragments and parity fragments together form an EC group and are distributed across different storage nodes. When some of the data fragments or parity fragments are lost, APFS can recover the lost data from other fragments. EC involves two concepts: data fragments (n) and parity fragments (m): Data fragments (n): APFS divides data into n data fragments. Parity fragments (m): APFS calculates m parity fragments from n data fragments. The combination of n data fragments and m parity fragments forms an EC group. These fragments reside on different servers. APFS can recover any lost fragments by using the EC algorithm as long as the number of lost fragments is less than or equal to m. APFS supports the 4+2 EC scheme. That is, the configuration of four data fragments and two parity fragments is supported. |
|---|---|
| System redundancy | The key components of the entire APFS are fully redundant to eliminate single points of failure (SPOFs). The data is not lost if a single storage node fails. Because the failure of a single node is transparent to applications, and access to applications is not affected. |
| Fault tolerance and stability | APFS automatically reconstructs and rebalances data after a disk or node failure. The impact of data reconstruction and recovery on system performance does not exceed 10%. |
| Online upgradeS | APFS supports hot upgrades of storage systems. You can add disks to or remove disks from an APFS file system while the file system is providing services. |

| Feature | Description |
|---|---|
| Minimum number of servers in a cluster | 6 |
| Step size per scale-out | 6 |
| Maximum number of servers in a cluster | 126 |
| Maximum capacity of a single file system | 25 PiB |
| High-performance client | APFS supports parallel data read and write I/O operations on high- performance computing (HPC) Linux clients. |

ApsaraStack Parallel File System

**Performance and scalability**

| Scale-out | You can perform online scale-out of APFS file systems and clusters. |
|---|---|

| Feature | Description |
|---|---|
| Data flow | APFS enables efficient data flow between APFS and Object Storage Service (OSS). It provides two core capabilities: data backup and data import. These features help you manage data lifecycles, optimize costs, and rapidly import data for HPC scenarios. Data backup: You can configure a backup plan to automatically back up data from APFS to OSS on a regular schedule. This feature applies to the following scenarios: Data backup and disaster recovery. Synchronize data replicas from APFS to OSS to establish a cross-storage backup strategy, thereby enhancing data security. Storage cost optimization. Identify infrequently accessed data and migrate it to OSS to reduce overall storage costs and implement tiered data management. Import data. Create an import job to efficiently move data from OSS back to APFS. This feature applies to the following scenarios: Migrate offline data to the cloud. Leverage OSS's support for multiple data import methods to transfer data from on-premises environments or other sources into APFS, improving data transfer efficiency. Accelerate AI and big data training. Batch import massive volumes of historical data stored in OSS to the high-performance APFS. This delivers low-latency, high-throughput data access for I/O-intensive scenarios such as AI model training and HPC. |

| Feature | Description |
|---|---|
| Metric monitoring | APFS allows you to perform multi-dimensional performance monitoring for storage clusters. Through a graphical interface on the APFS console, you can view monitoring metrics for an APFS file system, such as total, used, and remaining capacity, capacity utilization, read/write bandwidth, and read/write IOPS. On the cluster node page of the O&M console, you can view metric data such as total, used, and remaining capacity, as well as the read and write bandwidth of individual nodes. On the cluster monitoring page, you can view metric data such as read bandwidth, write bandwidth, read IOPS, write IOPS, and latency of the cluster. |

ApsaraStack Parallel File System

**Data management**

**Monitoring and O&M**

| Alerts | You can configure alert rules and view alert information for file systems by using the console. |
|---|---|

ApsaraStack Parallel File System
