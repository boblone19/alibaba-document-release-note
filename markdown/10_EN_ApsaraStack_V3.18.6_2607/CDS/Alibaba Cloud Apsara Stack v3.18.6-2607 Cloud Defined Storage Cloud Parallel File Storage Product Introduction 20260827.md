---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Cloud Parallel File Storage Product Introduction 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 10
source_pdf: "d5818174c2c07557_Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Cloud Parallel File Storage Product In"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/CDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Defined%20Storage%20Cloud%20Parallel%20File%20Storage%20Product%20Introduction%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Cloud Parallel File Storage Product Introduction 20260827

## Table of Contents

- 1 Product details
- 2 Product value
- 3 Scenarios
- 4 Features

## 1 Product details

Cloud Parallel File Storage (CPFS) is a high-performance parallel file system for Apsara Stack that supports the POSIX protocol. It provides sub-millisecond data access and read/write throughput of tens of GB/s. CPFS is ideal for scenarios such as AIGC, autonomous driving, EDA simulation, and CG rendering.

## 2 Product value

**Ultra-high Performance**

CPFS clusters and single file systems support terabyte-level throughput. Data is stored on enterprise-grade NVMe SSDs and accessed over a high-speed RDMA network. CPFS uses a fully parallel I/O access model. Compute nodes can establish parallel connections with all storage servers in a CPFS storage cluster to read data simultaneously. CPFS uses distributed metadata. Metadata is distributed across multiple service nodes based on the directory tree structure to provide concurrent services.

**Scalability**

CPFS supports online storage capacity scale-out, and performance scales elastically with capacity. CPFS supports online expansion of storage nodes, which is transparent to applications. With no service interruption, you can perform online hot upgrades for backend storage services and dynamically add or remove disks. The distributed metadata architecture allows a single file system to scale to handle 10 billion files. The fully symmetric data and metadata architecture allows POSIX clients to access all service nodes in parallel. Throughput and IOPS scale linearly with capacity to achieve terabyte-level throughput and millions of IOPS. This meets the high-performance access requirements of large files and massive numbers of small files in artificial intelligence (AI), high-performance computing (HPC), and machine learning (ML).

**Cost-effectiveness**

Data is stored using erasure coding (EC) and supports a 4D+2P configuration.

## 3 Scenarios

CPFS is a high-performance file storage service from Alibaba Cloud. It supports end-to-end Remote Direct Memory Access (RDMA) networks for intelligent computing scenarios, such as AI-Generated Content (AIGC) and autonomous driving.

**AIGC**

CPFS combines with Object Storage Service (OSS) and File Storage NAS to form a complete solution. It provides persistent storage for the millions of image assets required for model training and for AI art files. CPFS also delivers throughput of up to hundreds of Gbps. This accelerates data read and write performance during training, provides faster model training and inference speeds, shortens time-to-market for new services, and reduces wait times for AI art generation.

**Autonomous driving**

For autonomous driving, high-performance CPFS storage improves the utilization of GPU computing resources. The scalability and on-demand deployment of CPFS in the cloud reduce operations management costs. It enables seamless integration between cloud and onpremises environments, streamlining the entire data lifecycle of uploading, computing, distributing, and archiving data. This process lowers overall data storage costs. A hybrid cloud deployment of CPFS supports data flow with OSS. This addresses the requirements for both computing elasticity and data storage cost optimization.

**High-performance storage for genomics**

CPFS integrates with Container Service for Kubernetes (ACK), Serverless Kubernetes (ASK), and Genomics Service (AGS) to build a fast, low-cost, and high-precision container environment for genomics. This setup satisfies the requirements for gene sequencing computation and data sharing. CPFS serves as shared storage for genomic data analytics. It stores raw sequencing data, assembled data, and intermediate data. This meets the lowlatency and high input/output operations per second (IOPS) storage requirements of the genomics industry and reduces data copying and transfers. Additionally, computational results from CPFS can be synchronized to Object Storage Service (OSS), which provides massive storage capacity and helps reduce storage costs.

## 4 Features

This topic describes the features of CPFS.

**Basic features**

| Feature | Description |
|---|---|
| File system management | Create, view, and delete file systems in the console. Standard Open APIs are also provided. |
| Multitenancy | Manage file systems and mount targets using multi-level organizations and resource sets. |
| Quota management | Manage quotas based on organizations and resource sets to control capacity usage. |
| Metering | Collect statistics on the used capacity of CPFS file systems. In the console, you can view capacity information such as physical capacity usage, physical capacity usage trends, and logical capacity usage. |
| Protocol support | Network protocols: Supports protocols such as RoCE and 100G Ethernet. Storage protocols: Supports the standard POSIX protocol. Your data and applications can run on the distributed file system without modification. |
| Hardware compatibility | Compatible with mainstream server hosts, hard drive types, and RAID cards. |
| Client mounting | Supports batch and automatic mounting of clients. |

**Reliability and availability**

| Feature | Description |
|---|---|
| Erasure coding (EC) | Erasure Coding (EC) divides raw data into multiple data blocks and generates a specific number of parity blocks through calculation. These data and parity blocks form an EC group distributed across different data nodes. If some data or parity blocks are lost, the lost data can be recovered from the remaining blocks. EC involves two concepts: data blocks (n) and parity blocks (m): Data blocks (n): The data is divided into n segments. Parity blocks (m): These are m blocks calculated from the n data blocks. The data blocks (n) and parity blocks (m) form an EC group, with each block stored on a different server. If m or fewer blocks are lost, the EC algorithm can recover them. CPFS file systems support a 4+2 configuration. |

| System redundancy design | All key system components have a fully redundant design. No part of the system configuration has a single point of failure. The failure of a single data node does not cause data loss. Single-node failures are transparent to applications and do not affect normal read operations. |
|---|---|
| Fault stability | Supports automatic data reconstruction and balancing after a hard drive or node failure. The impact of data reconstruction and recovery on system performance is less than 10%. |
| Online upgrades | The storage system can be upgraded online without service interruption. You can also dynamically add and remove disks. |

**Performance and scalability**

| Feature | Description |
|---|---|
| Minimum initial scale | 6 nodes. |
| Scaling step size | 6 nodes. |
| Maximum cluster scale | 126 nodes. |
| Maximum file system capacity | 1.7 PiB. |
| High-performance client | Supports parallel I/O read and write operations for high-performance computing (HPC) Linux clients. |
| Scale-out | Supports online scale-out for CPFS file systems and clusters. |

**Data management**

| Feature | Description |
|---|---|
| Lifecycle management | Supports data replication between CPFS file systems and Object Storage Service (OSS). |

**Monitoring and O&M**

| Feature | Description |
|---|---|

| Metric monitoring | Monitor the performance of storage clusters across multiple dimensions. In the console's graphical interface, view metrics such as total capacity, remaining capacity, used capacity, usage percentage, read/write bandwidth, and read/write input/output operations per second (IOPS). |
|---|---|
| Alerting | Configure alert rules and view alert information for your file system in the console. Alerts can be sent as notifications through email and DingTalk. |
