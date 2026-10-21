---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Product Introduction 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 8
source_pdf: "add512e9fa9dffcf_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Product Introduction 20260827.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20NAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20File%20Storage%20NAS%20Product%20Introduction%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Product Introduction 20260827

## Table of Contents

- 1 File Storage NAS
  - 1.1 Product Details
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features

## 1 File Storage NAS

File Storage NAS (NAS) is a file storage service for compute nodes, such as Elastic Compute Service (ECS) instances and container services. NAS is a distributed file system that provides high performance, high reliability, scalability, and shared access. After you create a NAS file system and a mount target, you can mount the file system on compute nodes, such as ECS instances and container services, using the standard Network File System (NFS) and Server Message Block (SMB) protocols. You can also access the file system using standard Portable Operating System Interface (POSIX)-based APIs. Multiple compute nodes can simultaneously mount the same file system to share files and directories. NAS file systems support hybrid deployments of Hygon and Intel servers within a cluster.

### 1.1 Product Details

File Storage NAS (NAS) provides scalable file systems and allows simultaneous access to a NAS file system from multiple Elastic Compute Service (ECS) instances. The storage capacity of a NAS file system automatically scales up or down when users create or delete files. NAS provides shared data sources for workloads and applications that run on multiple ECS instances or servers.

**File system management**

A file system is where files are stored. A file system can be mounted on a compute node using a mount target. The data and metadata in the file system are stored in the traditional directory tree structure. A file system supports simultaneous access from hundreds of compute nodes for data sharing and highly concurrent read and write operations. You can use the NAS console to manage the file systems in your account. You can create, delete, scale out, and query the details of a file system. The details page of a file system displays the basic information about the file system, such as the ID, region, and storage capacity.

**Mount target management**

A mount target is an access endpoint for a file system instance in a virtual private cloud (VPC) or classic network. Each mount target has a domain name. To mount a NAS file system to a compute node or ECS instance, you must specify the domain name of the mount target. You can use the NAS console to view the mount targets of a file system and modify their status and permission groups.

**Permission group**

The permission group mechanism is a whitelist mechanism provided by NAS. You can add rules to a permission group of a NAS file system. You can allow users from specific IP addresses or CIDR blocks to access the NAS file system using different permissions. Each mount target must be associated with a permission group.

**Unified namespace**

A unified namespace creates a virtual root directory where each file system is a first-level subdirectory. This provides a consistent experience when you manage multiple file systems and saves maintenance time. You can use the NAS console to create unified namespaces and mount targets. You can also add, remove, and modify file systems in a unified namespace and view its details. Unified namespaces also support cross-domain orchestration. This feature maps file systems to the local directory tree of the client. After orchestration, you can specify a root directory to generate an automatic mount script. This enables cross-domain use of the file system.

**Lifecycle management**

Lifecycle management helps you manage hot and cold data separation in NAS. You can configure a lifecycle policy to automatically archive infrequently accessed files to the highcapacity Object Storage Service (OSS). Data archived to OSS can still be accessed in the same way.

**Permission control and ACL-based isolation**

You can configure directory-level access control lists (ACLs) for a NAS file system. You can configure ACLs for files or directories. This lets you perform directory-level fine-grained access control. You can use the ACL feature of NAS to grant users and groups different access permissions on directories and files. This helps implement access isolation.

**Audit logs**

NAS supports the audit log feature. Logs record operations that are performed on file systems in real time. You can use the logs to analyze and troubleshoot issues.

### 1.2 Benefits

File Storage NAS offers several advantages over traditional storage, including shared access, high reliability, elastic scaling, ease of use, and support for hybrid deployment.

**Parallel shared access**

A file system can be mounted on multiple compute nodes to provide shared access. This reduces data replication and synchronization costs.

**High reliability**

NAS uses the Pangu distributed system to store data in triplicate, ensuring high data reliability and data protection.

**Scalability**

NAS lets you respond to business changes in a timely manner. You can scale the storage capacity of a file system as needed.

**Ease of use**

NAS supports the Network File System (NFS) 3.0, NFS 4.0, Server Message Block (SMB) 2.1, and SMB 3.0 protocols. You can access file systems by calling Portable Operating System Interface (POSIX)-based APIs, regardless of the type of the compute nodes on which the file systems reside. The SMB protocols are suitable for Windows Elastic Compute Service (ECS) instances. The NFS protocols are suitable for Linux ECS instances.

**Support for hybrid deployment**

NAS file systems can be deployed in a hybrid manner on Hygon servers and Intel servers in a cluster.

### 1.3 Scenarios

File Storage NAS (NAS) is used for several purposes, such as providing shared storage and high availability with Server Load Balancer (SLB), enabling file sharing within an enterprise, and performing data backup.

**Shared storage and high availability for SLB**

For example, your SLB instance is connected to multiple Elastic Compute Service (ECS) instances. You can store the data of applications on these ECS instances in a shared NAS file system. This data sharing method ensures the high availability of the SLB instance.

**File sharing within an enterprise**

For example, the employees of an enterprise need to access the same datasets. An administrator can create a NAS file system and configure different file or directory permissions for users or user groups.

**Data backup**

For example, you want to migrate your data from a data center to the cloud for backup. You want to use a standard interface to access the cloud storage service. You can back up your data in a NAS file system.

### 1.4 Features

**Basic features**

| Feature | Description |
|---|---|
| File system management | Manage file systems from the console. Create, delete, and scale out file systems, and query their details. |
| Mount target management | A mount target is an access point for a file system instance in a virtual private cloud (VPC) or classic network. Each mount target has a domain name. To mount a NAS file system to a compute node or an ECS instance, specify the domain name of the mount target. |
| Protocol support | Supports the NFSv3/NFSv4 and SMB 2.1/SMB 3.0 protocols. Choose the protocol version for mounting a file system as needed. |
| Permission groups | In File Storage NAS, a permission group acts as a whitelist. Add rules to a permission group to allow specified IP addresses or network segments to access a file system. You can also grant different levels of access permissions to different IP addresses or network segments. |
| Quota management | Quota management provides directory-level control over storage resources. Set directory quotas and user quotas to monitor and limit file system usage. Directory quota: Tracks the storage capacity and number of files used by all users in a specified directory. User quota: Tracks or limits usage for specific users. User quotas can be for tracking or for enforcement. Tracking: Tracks file system usage for user reference. Enforcement: Prohibits write operations after the quota is exceeded. Quota management applies only to NFS file systems. For a single file system, you can set quotas for up to 500 directories. The maximum directory depth is 8 layers. |

| Unified namespace | A unified namespace creates a virtual root directory where each file system acts as a first-level subdirectory. This provides a consistent user experience when you manage multiple file systems, similar to managing a single file system, which saves maintenance time. You can also create unified namespaces and mount targets in different domains. The cross-domain orchestration feature maps these to a client's local directory tree to enable cross-domain access to file systems. |
|---|---|
| Lifecycle management | Manage the lifecycle of NFS file systems. Configure lifecycle management policies to dump cold data from a file system to Object Storage Service (OSS) for data layering. Add lifecycle policies based on your business needs to optimize file storage management. You can also view and modify lifecycle policies and query the usage of general- purpose and Infrequent Access storage from the NAS console. |

**Reliability and availability**

| Feature | Description |
|---|---|
| Triplicate protection | Based on a distributed system with triplicate replication, each block of data is copied three times. These replicas are stored on different nodes in the cluster based on a specific policy. This design ensures that if a node fails, data can be recovered from other nodes. This provides high data reliability and protects your data. |
| Permission management | NAS file systems that use the NFS protocol support directory-level access control lists (ACLs). Use NFSv4 ACLs and POSIX ACLs to configure permissions for files or directories. This provides granular, directory-level permission management. A system administrator can set specific permissions for different users and groups on various files and directories to enforce access isolation. |

**Scalability**

| Feature | Description |
|---|---|
| Elastic scale-out | File Storage NAS is highly scalable. The performance of a cluster scales linearly as you add more nodes. A single NAS cluster can support hundreds of data nodes and scale to tens of petabytes. |

**Deployment notes**

A NAS cluster deployment requires a minimum of 6 nodes.
