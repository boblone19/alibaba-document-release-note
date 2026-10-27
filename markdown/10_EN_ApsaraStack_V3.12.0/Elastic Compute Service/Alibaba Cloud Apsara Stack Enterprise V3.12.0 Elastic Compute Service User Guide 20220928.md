---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic Compute Service User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 123
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic Compute Service User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%BC%B9%E6%80%A7%E8%AE%A1%E7%AE%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Elastic%20Compute%20Service%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic Compute Service User Guide 20220928

## Table of Contents

- 1 What is ECS?
  - 1.1 Overview
  - 1.2 Instance types
  - 1.3 Instance lifecycle
- 2 Instructions
  - 2.1 Restrictions
  - 2.2 Suggestions
  - 2.3 Limits
  - 2.4 Notice for Windows users
  - 2.5 Notice for Linux users
  - 2.6 Notice on defense against DDoS attacks
- 3 Quick start
  - 3.1 Overview
  - 3.2 Log on to the ECS console
  - 3.3 Create a security group
  - 3.4 Create an instance
  - 3.5 Connect to an instance
    - 3.5.1 Instance connecting overview
    - 3.5.2 Connect to a Linux instance by using SSH commands in Linux or Mac OS X
    - 3.5.3 Connect to a Linux-based instance by using remote connection tools in Windows
    - 3.5.4 Connect to a Windows instance by using RDP
    - 3.5.5 Connect to an ECS instance by using the VNC
- 4 Instances
  - 4.1 Create an instance
  - 4.2 Connect to an instance
    - 4.2.1 Instance connecting overview
    - 4.2.2 Connect to a Linux-based instance by using SSH commands in Linux or Mac OS X
    - 4.2.3 Connect to a Linux-based instance by using remote connection tools in Windows
    - 4.2.4 Connect to a Windows instance by using RDC
    - 4.2.5 Install the certificate for VNC in Windows
    - 4.2.6 Connect to an ECS instance by using the VNC
  - 4.3 View instances
  - 4.4 Modify an instance
  - 4.5 Stop an instance
  - 4.6 Start an instance
  - 4.7 Restart an instance
  - 4.8 Delete an instance
  - 4.9 Change the instance type of an instance
  - 4.10 Change an instance logon password
  - 4.11 Change the VNC password
  - 4.12 Add an ECS instance to a security group
  - 4.13 Customize instance data
  - 4.14 Modify a private IP address
  - 4.15 Install the CUDA and GPU drivers for a Linux instance
  - 4.16 Install the CUDA and GPU drivers for a Windows instance
- 5 Disks
  - 5.1 Create a disk
  - 5.2 View disks
  - 5.3 Roll back a disk
  - 5.4 Modify the disk properties
  - 5.5 Modify the disk description
  - 5.6 Attach a disk
  - 5.7 Partition and format disks
    - 5.7.1 Format a data disk for a Linux instance
    - 5.7.2 Format a data disk of a Windows instance
  - 5.8 Expand a disk
  - 5.9 Reinitialize a disk
  - 5.10 Detach a data disk
  - 5.11 Release a data disk
- 6 Images
  - 6.1 Create a custom image
  - 6.2 View images
  - 6.3 View instances related to an image
  - 6.4 Modify the description of a custom image
  - 6.5 Share custom images
  - 6.6 Import custom images
    - 6.6.1 Limits on importing custom images
    - 6.6.2 Convert the image file format
    - 6.6.3 Import a custom image
  - 6.7 Export a custom image
  - 6.8 Delete a custom image
- 7 Snapshots
  - 7.1 Create a snapshot
  - 7.2 View snapshots
  - 7.3 Delete a snapshot
- 8 Automatic snapshot policies
  - 8.1 Create an automatic snapshot policy
  - 8.2 View automatic snapshot policies
  - 8.3 Modify an automatic snapshot policy
  - 8.4 Configure an automatic snapshot policy
  - 8.5 Configure an automatic snapshot policy for multiple disks
  - 8.6 Delete an automatic snapshot policy
- 9 Security groups
  - 9.1 Create a security group
  - 9.2 View security groups
  - 9.3 Modify a security group
  - 9.4 Add a security group rule
  - 9.5 Clone a security group rule
  - 9.6 Modify a security group rule
  - 9.7 Export security group rules
  - 9.8 Import security group rules
  - 9.9 Add an instance
  - 9.10 Remove instances from a security group
  - 9.11 Delete a security group
- 10 Elastic Network Interfaces
  - 10.1 Create an ENI
  - 10.2 View ENIs
  - 10.3 Modify a secondary ENI
  - 10.4 Bind a secondary ENI to an instance
  - 10.5 Unbind a secondary ENI from an instance
  - 10.6 Delete a secondary ENI
- 11 Deployment sets
  - 11.1 Create a deployment set
  - 11.2 View deployment sets
  - 11.3 Modify a deployment set
  - 11.4 Delete a deployment set
- 12 Install FTP software
  - 12.1 Overview
  - 12.2 Install and configure vsftp in CentOS
  - 12.3 Install vsftp in Ubuntu or Debian
  - 12.4 Build an FTP site in Windows Server 2008
  - 12.5 Build an FTP site in Windows Server 2012

## 1 What is ECS?

### 1.1 Overview

Elastic Compute Service (ECS) is a type of computing service that features elastic processingcapabilities. Compared with physical servers, ECS can be more efficientlymanaged and is more user-friendly. You can create instances, resize disks, and add or release any number of ECS instances at any time based on your business needs. An ECS instance is a virtual computing environment that contains the most basic components of computers such as the CPU, memory, and storage. Users perform operations on ECS instances. Instances are core components of ECS, and operations can be performed on instances by using the ECS console. Other resources such as block storage, images, and snapshots can only be used after they are integrated into ECS instances. For more information, see ECS components. ECS components

### 1.2 Instance types

An ECS instance is the smallest unit that can provide compute capabilities and services for your business. The compute capabilities of instances vary by instance type. An ECS instance type defines the basic properties of ECS instances, such as CPU, clock speed, and memory. In addition to the instance type, you must also configure the Block Storage devices, image, and network type when you create an ECS instance. The following table describes instance families and lists the instance types of each instance family.

| Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
|---|---|---|---|---|---|---|---|---|
| n4 | ecs.n4.sm all | 1 | 2.0 | N/A | 0.5 | 50 | 1 | 1 |
|   | ecs.n4.lar ge | 2 | 4.0 | N/A | 0.5 | 100 | 1 | 1 |
|   | ecs.n4.xla rge | 4 | 8.0 | N/A | 0.8 | 150 | 1 | 2 |
|   | ecs.n4.2xl arge | 8 | 16.0 | N/A | 1.2 | 300 | 1 | 2 |
|   | ecs.n4.4xl arge | 16 | 32.0 | N/A | 2.5 | 400 | 1 | 2 |
|   | ecs.n4.8xl arge | 32 | 64.0 | N/A | 5.0 | 500 | 1 | 2 |
| mn4 | ecs.mn4.s mall | 1 | 4.0 | N/A | 0.5 | 50 | 1 | 1 |
|   | ecs.mn4.l arge | 2 | 8.0 | N/A | 0.5 | 100 | 1 | 1 |
|   | ecs.mn4.x large | 4 | 16.0 | N/A | 0.8 | 150 | 1 | 2 |
|   | ecs.mn4. 2xlarge | 8 | 32.0 | N/A | 1.2 | 300 | 1 | 3 |
|   | ecs.mn4. 4xlarge | 16 | 64.0 | N/A | 2.5 | 400 | 1 | 8 |
|   | ecs.mn4. 8xlarge | 32 | 128.0 | N/A | 5.0 | 500 | 2 | 8 |
| xn4 | ecs.xn4.s mall | 1 | 1.0 | N/A | 0.5 | 50 | 1 | 1 |
|   | ecs.e4.sm all | 1 | 8.0 | N/A | 0.5 | 50 | 1 | 1 |
|   | ecs.e4.lar ge | 2 | 16.0 | N/A | 0.5 | 100 | 1 | 1 |
|   | ecs.e4.xla rge | 4 | 32.0 | N/A | 0.8 | 150 | 1 | 2 |

| lastic Comput | e Service User Guide·What is ECS |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| e4 Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
|   | ecs.e4.2xl arge | 8 | 64.0 | N/A | 1.2 | 300 | 1 | 3 |
|   | ecs.e4.4xl arge | 16 | 128.0 | N/A | 2.5 | 400 | 1 | 8 |
| sn1ne | ecs.sn1ne .large | 2 | 4.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.sn1ne .xlarge | 4 | 8.0 | N/A | 1.5 | 500 | 2 | 3 |
|   | ecs.sn1ne .2xlarge | 8 | 16.0 | N/A | 2.0 | 1,000 | 4 | 4 |
|   | ecs.sn1ne .3xlarge | 12 | 24.0 | N/A | 2.5 | 1,300 | 4 | 6 |
|   | ecs.sn1ne .4xlarge | 16 | 32.0 | N/A | 3.0 | 1,600 | 4 | 8 |
|   | ecs.sn1ne .6xlarge | 24 | 48.0 | N/A | 4.5 | 2,000 | 6 | 4 |
|   | ecs.sn1ne .8xlarge | 32 | 64.0 | N/A | 6.0 | 2,500 | 8 | 8 |
| g6 | ecs.g6.lar ge | 2 | 8.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.g6.xla rge | 4 | 16.0 | N/A | 1.5 | 500 | 4 | 3 |
|   | ecs.g6.2xl arge | 8 | 32.0 | N/A | 2.5 | 800 | 8 | 4 |
|   | ecs.g6.3xl arge | 12 | 48.0 | N/A | 4.0 | 900 | 8 | 6 |
|   | ecs.g6.4xl arge | 16 | 64.0 | N/A | 5.0 | 1,000 | 8 | 8 |
|   | ecs.g6.6xl arge | 24 | 96.0 | N/A | 7.5 | 1,500 | 12 | 8 |
|   | ecs.g6.8xl arge | 32 | 128.0 | N/A | 10.0 | 2,000 | 16 | 8 |
| Document V | ersion: 20220928 1 |   |   |   |   |   |   |   |

|   | at is ECS? Elastic Compute Servic |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
|   | ecs.g5.lar ge | 2 | 8.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.g5.xla rge | 4 | 16.0 | N/A | 1.5 | 500 | 2 | 3 |
| g5 |   |   |   |   |   |   |   |   |
|   | ecs.g5.2xl arge | 8 | 32.0 | N/A | 2.5 | 800 | 2 | 4 |
|   | ecs.g5.3xl arge | 12 | 48.0 | N/A | 4.0 | 900 | 4 | 6 |
|   | ecs.g5.4xl arge | 16 | 64.0 | N/A | 5.0 | 1,000 | 4 | 8 |
|   | ecs.g5.6xl arge | 24 | 96.0 | N/A | 7.5 | 1,500 | 6 | 8 |
|   | ecs.g5.8xl arge | 32 | 128.0 | N/A | 10.0 | 2,000 | 8 | 8 |
|   | ecs.g5.16 xlarge | 64 | 256.0 | N/A | 20.0 | 4,000 | 16 | 8 |
| sn2ne | ecs.sn2ne .large | 2 | 8.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.sn2ne .xlarge | 4 | 16.0 | N/A | 1.5 | 500 | 2 | 3 |
|   | ecs.sn2ne .2xlarge | 8 | 32.0 | N/A | 2.0 | 1,000 | 4 | 4 |
|   | ecs.sn2ne .3xlarge | 12 | 48.0 | N/A | 2.5 | 1,300 | 4 | 6 |
|   | ecs.sn2ne .4xlarge | 16 | 64.0 | N/A | 3.0 | 1,600 | 4 | 8 |
|   | ecs.sn2ne .6xlarge | 24 | 96.0 | N/A | 4.5 | 2,000 | 6 | 4 |
|   | ecs.sn2ne .8xlarge | 32 | 128.0 | N/A | 6.0 | 2,500 | 8 | 8 |
|   | ecs.sn2ne .14xlarge | 56 | 224.0 | N/A | 10.0 | 4,500 | 14 | 8 |
| 2 | > Document Version: 2022092 |   |   |   |   |   |   |   |

|   | e Service User Guide·What is ECS |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
|   | ecs.r6.lar ge | 2 | 16.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.r6.xla rge | 4 | 32.0 | N/A | 1.5 | 500 | 4 | 3 |
|   | ecs.r6.2xl arge | 8 | 64.0 | N/A | 2.5 | 800 | 8 | 4 |
| r6 |   |   |   |   |   |   |   |   |
|   | ecs.r6.3xl arge | 12 | 96.0 | N/A | 4.0 | 900 | 8 | 6 |
|   | ecs.r6.4xl arge | 16 | 128.0 | N/A | 5.0 | 1,000 | 8 | 8 |
|   | ecs.r6.6xl arge | 24 | 192.0 | N/A | 7.5 | 1,500 | 12 | 8 |
|   | ecs.r6.8xl arge | 32 | 256.0 | N/A | 10.0 | 2,000 | 16 | 8 |
| r5 | ecs.r5.lar ge | 2 | 16.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.r5.xla rge | 4 | 32.0 | N/A | 1.5 | 500 | 2 | 3 |
|   | ecs.r5.2xl arge | 8 | 64.0 | N/A | 2.5 | 800 | 2 | 4 |
|   | ecs.r5.3xl arge | 12 | 96.0 | N/A | 4.0 | 900 | 4 | 6 |
|   | ecs.r5.4xl arge | 16 | 128.0 | N/A | 5.0 | 1,000 | 4 | 8 |
|   | ecs.r5.6xl arge | 24 | 192.0 | N/A | 7.5 | 1,500 | 6 | 8 |
|   | ecs.r5.8xl arge | 32 | 256.0 | N/A | 10.0 | 2,000 | 8 | 8 |
|   | ecs.r5.16x large | 64 | 512.0 | N/A | 20.0 | 4,000 | 16 | 8 |
|   | ecs.se1ne .large | 2 | 16.0 | N/A | 1.0 | 300 | 2 | 2 |

| ser Guide·Wh |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   | at is ECS? Elastic Compute Servic |   |   |   |   |   |   |   |
| Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
| se1ne | ecs.se1ne .xlarge | 4 | 32.0 | N/A | 1.5 | 500 | 2 | 3 |
|   | ecs.se1ne .2xlarge | 8 | 64.0 | N/A | 2.0 | 1,000 | 4 | 4 |
|   | ecs.se1ne .3xlarge | 12 | 96.0 | N/A | 2.5 | 1,300 | 4 | 6 |
|   | ecs.se1ne .4xlarge | 16 | 128.0 | N/A | 3.0 | 1,600 | 4 | 8 |
|   | ecs.se1ne .6xlarge | 24 | 192.0 | N/A | 4.5 | 2,000 | 6 | 4 |
|   | ecs.se1ne .8xlarge | 32 | 256.0 | N/A | 6.0 | 2,500 | 8 | 8 |
|   | ecs.se1ne .14xlarge | 56 | 480.0 | N/A | 10.0 | 4,500 | 14 | 8 |
| se1 | ecs.se1.la rge | 2 | 16.0 | N/A | 0.5 | 100 | 1 | 2 |
|   | ecs.se1.xl arge | 4 | 32.0 | N/A | 0.8 | 200 | 1 | 3 |
|   | ecs.se1.2 xlarge | 8 | 64.0 | N/A | 1.5 | 400 | 1 | 4 |
|   | ecs.se1.4 xlarge | 16 | 128.0 | N/A | 3.0 | 500 | 2 | 8 |
|   | ecs.se1.8 xlarge | 32 | 256.0 | N/A | 6.0 | 800 | 3 | 8 |
|   | ecs.se1.1 4xlarge | 56 | 480.0 | N/A | 10.0 | 1,200 | 4 | 8 |
| ebmg5s | ecs.ebmg 5s.24xlar ge | 96 | 384.0 | N/A | 30.0 | 4,500 | 8 | 32 |
| ebmg5 | ecs.ebmg 5.24xlarg e | 96 | 384.0 | N/A | 10.0 | 4,000 | 8 | 32 |
|   | ecs.i2.xlar ge | 4 | 32.0 | 1 × 894 | 1.0 | 500 | 2 | 3 |

| lastic Comput | e Service |   |   |   |   |   | User Guid | e·What is ECS |
|---|---|---|---|---|---|---|---|---|
| Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
| i2 | ecs.i2.2xl arge | 8 | 64.0 | 1 × 1,788 | 2.0 | 1,000 | 2 | 4 |
|   | ecs.i2.4xl arge | 16 | 128.0 | 2 × 1,788 | 3.0 | 1,500 | 4 | 8 |
|   | ecs.i2.8xl arge | 32 | 256.0 | 4 × 1,788 | 6.0 | 2,000 | 8 | 8 |
|   | ecs.i2.16x large | 64 | 512.0 | 8 × 1,788 | 10.0 | 4,000 | 16 | 8 |
| d1 | ecs.d1.2xl arge | 8 | 32.0 | 4 × 5,500 | 3.0 | 300 | 1 | 4 |
|   | ecs.d1.3xl arge | 12 | 48.0 | 6 × 5,500 | 4.0 | 400 | 1 | 6 |
|   | ecs.d1.4xl arge | 16 | 64.0 | 8 × 5,500 | 6.0 | 600 | 2 | 8 |
|   | ecs.d1.6xl arge | 24 | 96.0 | 12 × 5,500 | 8.0 | 800 | 2 | 8 |
|   | ecs.d1- c8d3.8xla rge | 32 | 128.0 | 12 × 5,500 | 10.0 | 1,000 | 4 | 8 |
|   | ecs.d1.8xl arge | 32 | 128.0 | 16 × 5,500 | 10.0 | 1,000 | 4 | 8 |
|   | ecs.d1- c14d3.14 xlarge | 56 | 160.0 | 12 × 5,500 | 17.0 | 1,800 | 6 | 8 |
|   | ecs.d1.14 xlarge | 56 | 224.0 | 28 × 5,500 | 17.0 | 1,800 | 6 | 8 |
|   | ecs.d2- zyy- d0.4xlarg e | 16 | 64.0 | N/A | 3.0 | 300 | 2 | 8 |
|   | ecs.d2- zyy- d0.6xlarg e | 24 | 96.0 | N/A | 4.0 | 400 | 2 | 8 |

|   | at is ECS? Elastic Compute Servic |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Instance family | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
| d2 | ecs.d2- zyy.4xlar ge | 16 | 64.0 | 6 × 7,500 | 3.0 | 300 | 4 | 8 |
|   | ecs.d2- zyy.6xlar ge | 24 | 96.0 | 12 × 7,500 | 4.0 | 400 | 4 | 8 |
|   | ecs.d2- zyy.7xlar ge | 56 | 224.0 | 12 × 7,300 | 17.0 | 1,800 | 6 | 8 |
|   | ecs.d2- zyy.8xlar ge | 32 | 160.0 | 12 × 7,300 | 17.0 | 1,800 | 6 | 8 |
|   | ecs.d2- zyy.22xlar ge | 88 | 352.0 | 12 × 7,300 | 17.0 | 1,800 | 6 | 8 |
|   | ecs.d2- zyy- m40.8xlar ge | 32 | 128.0 | 12 × 7,500 | 6.0 | 600 | 4 | 8 |
|   | ecs.d2- gab.4xlar ge | 16 | 64.0 | 6 × 1,150 | 3.0 | 300 | 4 | 8 |
|   | ecs.d2- gab.8xlar ge | 32 | 128.0 | 12 × 1,150 | 6.0 | 600 | 4 | 8 |
| sccg5ib | ecs.sccg5 ib.24xlarg e | 96 | 384.0 | N/A | 10.0 | 4,500 | 8 | 32 |
| scch5ib | ecs.scch5i b.16xlarg e | 64 | 192.0 | N/A | 10.0 | 4,500 | 8 | 32 |
|   | ecs.c6.lar ge | 2 | 4.0 | N/A | 1.0 | 300 | 2 | 2 |
|   | ecs.c6.xla rge | 4 | 8.0 | N/A | 1.5 | 500 | 4 | 3 |
|   | ecs.c6.2xl arge | 8 | 16.0 | N/A | 2.5 | 800 | 8 | 4 |

| lastic Comput |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   | e Service |   |   |   |   |   | User Guid | e·What is ECS |
| Instance family c6 | Instance type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (including one primary ENI) |
|   | ecs.c6.3xl arge | 12 | 24.0 | N/A | 4.0 | 900 | 8 | 6 |
|   | ecs.c6.4xl arge | 16 | 32.0 | N/A | 5.0 | 1,000 | 8 | 8 |
|   | ecs.c6.6xl arge | 24 | 48.0 | N/A | 7.5 | 1,500 | 12 | 8 |
|   | ecs.c6.8xl arge | 32 | 64.0 | N/A | 10.0 | 2,000 | 16 | 8 |
| sn1 | ecs.sn1.m edium | 2 | 4.0 | N/A | 0.5 | 100 | 1 | 2 |
|   | ecs.sn1.la rge | 4 | 8.0 | N/A | 0.8 | 200 | 1 | 3 |
|   | ecs.sn1.xl arge | 8 | 16.0 | N/A | 1.5 | 400 | 1 | 4 |
|   | ecs.sn1.3 xlarge | 16 | 32.0 | N/A | 3.0 | 500 | 2 | 8 |
|   | ecs.sn1.7 xlarge | 32 | 64.0 | N/A | 6.0 | 800 | 3 | 8 |
| sn2 | ecs.sn2.m edium | 2 | 8.0 | N/A | 0.5 | 100 | 1 | 2 |
|   | ecs.sn2.la rge | 4 | 16.0 | N/A | 0.8 | 200 | 1 | 3 |
|   | ecs.sn2.xl arge | 8 | 32.0 | N/A | 1.5 | 400 | 1 | 4 |
|   | ecs.sn2.3 xlarge | 16 | 64.0 | N/A | 3.0 | 500 | 2 | 8 |
|   | ecs.sn2.7 xlarge | 32 | 128.0 | N/A | 6.0 | 800 | 3 | 8 |
|   | ecs.sn2.1 4xlarge | 56 | 224.0 | N/A | 10.0 | 1,200 | 4 | 8 |

The following table describes FPGA-accelerated instance families.

| Instanc e family | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | FPGA |
|---|---|---|---|---|---|---|---|---|---|
| f 1 | ecs.f1- c8f1.2x large | 8 | 60.0 | N/A | 3.0 | 400 | 4 | 2 | Intel ARRIA 10 GX 1150 |
|   | ecs.f1- c8f1.4x large | 16 | 120.0 | N/A | 5.0 | 1,000 | 4 | 2 | 2 × Intel ARRIA 10 GX 1150 |
|   | ecs.f1- c28f1.7 xlarge | 28 | 112.0 | N/A | 5.0 | 2,000 | 8 | 2 | Intel ARRIA 10 GX 1150 |
|   | ecs.f1- c28f1.1 4xlarge | 56 | 224.0 | N/A | 10.0 | 2,000 | 14 | 2 | 2 × Intel ARRIA 10 GX 1150 |
| f 3 | ecs.f3- c16f1.4 xlarge | 16 | 64.0 | N/A | 5.0 | 1,000 | 4 | 8 | 1 × Xilinx VU9P |
|   | ecs.f3- c16f1.8 xlarge | 32 | 128.0 | N/A | 10.0 | 2,000 | 8 | 8 | 2 × Xilinx VU9P |
|   | ecs.f3- c16f1.1 6xlarge | 64 | 256.0 | N/A | 20.0 | 2,000 | 16 | 8 | 4 × Xilinx VU9P |

The following table describes GPU-accelerated instance families.

| Instanc e family | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | GPU |
|---|---|---|---|---|---|---|---|---|---|
|   | ecs.gn 5- c4g1.xl arge | 4 | 30.0 | 440 | 3.0 | 300 | 1 | 3 | 1 × NVIDIA P100 |

| lastic Com |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   | pute Service User Guide·What is ECS |   |   |   |   |   |   |   |   |
| Instanc e family | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | GPU |
| gn5 | ecs.gn 5- c8g1.2 xlarge | 8 | 60.0 | 440 | 3.0 | 400 | 1 | 4 | 1 × NVIDIA P100 |
|   | ecs.gn 5- c4g1.2 xlarge | 8 | 60.0 | 880 | 5.0 | 1,000 | 2 | 4 | 2 × NVIDIA P100 |
|   | ecs.gn 5- c8g1.4 xlarge | 16 | 120.0 | 880 | 5.0 | 1,000 | 4 | 8 | 2 × NVIDIA P100 |
|   | ecs.gn 5- c28g1. 7xlarge | 28 | 112.0 | 440 | 5.0 | 1,000 | 8 | 8 | 1 × NVIDIA P100 |
|   | ecs.gn 5- c8g1.8 xlarge | 32 | 240.0 | 1760 | 10.0 | 2,000 | 8 | 8 | 4 × NVIDIA P100 |
|   | ecs.gn 5- c28g1. 14xlarg e | 56 | 224.0 | 880 | 10.0 | 2,000 | 14 | 8 | 2 × NVIDIA P100 |
|   | ecs.gn 5- c8g1.1 4xlarge | 54 | 480.0 | 3520 | 25.0 | 4,000 | 14 | 8 | 8 × NVIDIA P100 |
|   | ecs.gn 4- c4g1.xl arge | 4 | 30.0 | N/A | 3.0 | 300 | 1 | 3 | 1 × NVIDIA M40 |
|   | ecs.gn 4- c8g1.2 xlarge | 8 | 30.0 | N/A | 3.0 | 400 | 1 | 4 | 1 × NVIDIA M40 |
|   | ecs.gn 4.8xlar ge | 32 | 48.0 | N/A | 6.0 | 800 | 3 | 8 | 1 × NVIDIA M40 |

|   | What is ECS | ? |   |   |   |   | El | astic Comp | ute Servic |
|---|---|---|---|---|---|---|---|---|---|
|   | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | GPU |
| Instanc gen4 family |   |   |   |   |   |   |   |   |   |
|   | ecs.gn 4- c4g1.2 xlarge | 8 | 60.0 | N/A | 5.0 | 500 | 1 | 4 | 2 × NVIDIA M40 |
|   | ecs.gn 4- c8g1.4 xlarge | 16 | 60.0 | N/A | 5.0 | 500 | 1 | 8 | 2 × NVIDIA M40 |
|   | ecs.gn 4.14xla rge | 56 | 96.0 | N/A | 10.0 | 1,200 | 4 | 8 | 2 × NVIDIA M40 |
| ga1 | ecs.ga 1.xlarg e | 4 | 10.0 | 1 × 87 | 1.0 | 200 | 1 | 3 | 0.25 × AMD S7150 |
|   | ecs.ga 1.2xlar ge | 8 | 20.0 | 1 × 175 | 1.5 | 300 | 1 | 4 | 0.5 × AMD S7150 |
|   | ecs.ga 1.4xlar ge | 16 | 40.0 | 1 × 350 | 3.0 | 500 | 2 | 8 | 1 × AMD S7150 |
|   | ecs.ga 1.8xlar ge | 32 | 80.0 | 1 × 700 | 6.0 | 800 | 3 | 8 | 2 × AMD S7150 |
|   | ecs.ga 1.14xla rge | 56 | 160.0 | 1 × 1,400 | 10.0 | 1,200 | 4 | 8 | 4 × AMD S7150 |
|   | ecs.gn 5i- c2g1.la rge | 2 | 8.0 | N/A | 1.0 | 100 | 2 | 2 | 1 × NVIDIA P4 |
|   | ecs.gn 5i- c4g1.xl arge | 4 | 16.0 | N/A | 1.5 | 200 | 2 | 3 | 1 × NVIDIA P4 |
|   | ecs.gn 5i- c8g1.2 xlarge | 8 | 32.0 | N/A | 2.0 | 400 | 4 | 4 | 1 × NVIDIA P4 |

|   | pute Servic | e |   |   |   |   | U | ser Guide· | What is ECS |
|---|---|---|---|---|---|---|---|---|---|
| Instanc e | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | GPU |
| family gn5i |   |   |   |   |   |   |   |   |   |
|   | ecs.gn 5i- c16g1. 4xlarge | 16 | 64.0 | N/A | 3.0 | 800 | 4 | 8 | 1 × NVIDIA P4 |
|   | ecs.gn 5i- c16g1. 8xlarge | 32 | 128.0 | N/A | 6.0 | 1,200 | 8 | 8 | 2 × NVIDIA P4 |
|   | ecs.gn 5i- c24g1. 12xlarg e | 48 | 192.0 | N/A | 10.0 | 2,000 | 8 | 8 | 2 × NVIDIA P4 |
|   | ecs.gn 5i- c28g1. 14xlarg e | 56 | 224.0 | N/A | 10.0 | 2,000 | 14 | 8 | 2 × NVIDIA P4 |
| gn5e | ecs.gn 5e- c11g1. 3xlarge | 10 | 58.0 | N/A | 2.0 | 150 | 1 | 6 | 1 × NVIDIA P4 |
|   | ecs.gn 5e- c11g1. 5xlarge | 22 | 116.0 | N/A | 4.0 | 300 | 1 | 8 | 2 × NVIDIA P4 |
|   | ecs.gn 5e- c11g1. 11xlarg e | 44 | 232.0 | N/A | 6.0 | 600 | 2 | 8 | 4 × NVIDIA P4 |
|   | ecs.gn 5e- c11g1. 22xlarg e | 88 | 464.0 | N/A | 10.0 | 1,200 | 4 | 8 | 8 × NVIDIA P4 |
|   | ecs.gn 6i- c10g1. 2xlarge | 10 | 42.0 | N/A | 5.0 | 800 | 2 | 4 | 1 × T4 |

| User Guide· | What is ECS | ? |   |   |   |   | El | astic Comp | ute Servic |
|---|---|---|---|---|---|---|---|---|---|
| Instanc e family | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | GPU |
| gn6i | ecs.gn 6i- c10g1. 5xlarge | 20 | 84.0 | N/A | 8.0 | 1,000 | 4 | 6 | 2 × T4 |
|   | ecs.gn 6i- c10g1. 10xlarg e | 40 | 168.0 | N/A | 15.0 | 2,000 | 8 | 8 | 4 × T4 |
|   | ecs.gn 6i- c10g1. 20xlarg e | 80 | 336.0 | N/A | 30.0 | 4,000 | 16 | 8 | 8 × T4 |
|   | ecs.gn 6i- c14g1. 3xlarge | 14 | 56.0 | N/A | 5.0 | 1,000 | 4 | 6 | 1 × T4 |
|   | ecs.gn 6i- c14g1. 7xlarge | 28 | 112.0 | N/A | 10.0 | 2,000 | 8 | 8 | 2 × T4 |
|   | ecs.gn 6i- c14g1. 14xlarg e | 56 | 224.0 | N/A | 20.0 | 4,000 | 12 | 8 | 4 × T4 |
|   | ecs.gn 6i- c20g1. 5xlarge | 20 | 80.0 | N/A | 10.0 | 1,500 | 4 | 6 | 1 × T4 |
|   | ecs.gn 6i- c20g1. 10xlarg e | 40 | 160.0 | N/A | 20.0 | 3,000 | 8 | 8 | 2 × T4 |
|   | ecs.gn 6v- c8g1.2 xlarge | 8 | 32.0 | N/A | 2.5 | 800 | 4 | 4 | 1 × NVIDIA V100 |

| lastic Com | pute Servic | e |   |   |   |   | U | ser Guide· | What is ECS |
|---|---|---|---|---|---|---|---|---|---|
| Instanc e family gn6v | Instanc e type | vCPUs | Memor y (GiB) | Local storag e (GiB) | Bandwi dth (Gbit/s ) | Packet forwar ding rate (Kpps) | NIC queues | ENIs (includi ng one primar y ENI) | GPU |
|   | ecs.gn 6v- c8g1.8 xlarge | 32 | 128.0 | N/A | 10.0 | 2,000 | 8 | 8 | 4 × NVIDIA V100 |
|   | ecs.gn 6v- c8g1.1 6xlarge | 64 | 256.0 | N/A | 20.0 | 2,500 | 16 | 8 | 8 × NVIDIA V100 |
| sccgn 6p | ecs.scc gn6p.2 4xlarge | 96 | 768.0 | N/A | 30.0 | 4,500 | 8 | 32 | 8 × NVIDIA V100 |

The following table describes shared instance families that support IPv6.

| Instance family | Instance type | vCPUs | Memo ry (GiB) | Local storag e (GiB) | Band width (Gbit/ s) | Packet forwa rding rate (Kpps) | IPv6 suppo rt | NIC queue s | ENIs (includin g one primary ENI) |
|---|---|---|---|---|---|---|---|---|---|
| n4v2 | ecs.n4v2 .small | 1 | 2.0 | N/A | 0.5 | 50 | Yes | 1 | 1 |
|   | ecs.n4v2 .large | 2 | 4.0 | N/A | 0.5 | 100 | Yes | 1 | 1 |
|   | ecs.n4v2 .xlarge | 4 | 8.0 | N/A | 0.8 | 150 | Yes | 1 | 2 |
|   | ecs.n4v2 .2xlarge | 8 | 16.0 | N/A | 1.2 | 300 | Yes | 1 | 2 |
|   | ecs.n4v2 .4xlarge | 16 | 32.0 | N/A | 2.5 | 400 | Yes | 1 | 2 |
|   | ecs.n4v2 .8xlarge | 32 | 64.0 | N/A | 5.0 | 500 | Yes | 1 | 2 |
|   | ecs.mn4 v2.small | 1 | 4.0 | N/A | 0.5 | 50 | Yes | 1 | 1 |
|   | ecs.mn4 v2.large | 2 | 8.0 | N/A | 0.5 | 100 | Yes | 1 | 1 |

|   | hat is ECS? Elastic Compute Servic |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| User Guide·W |   |   |   |   |   |   |   |   |   |
| Instance family | Instance type | vCPUs | Memo ry (GiB) | Local storag e (GiB) | Band width (Gbit/ s) | Packet forwa rding rate (Kpps) | IPv6 suppo rt | NIC queue s | ENIs (includin g one primary ENI) |
| mn4v2 | ecs.mn4 v2.xlarg e | 4 | 16.0 | N/A | 0.8 | 150 | Yes | 1 | 2 |
|   | ecs.mn4 v2.2xlar ge | 8 | 32.0 | N/A | 1.2 | 300 | Yes | 1 | 2 |
|   | ecs.mn4 v2.4xlar ge | 16 | 64.0 | N/A | 2.5 | 400 | Yes | 1 | 2 |
|   | ecs.mn4 v2.8xlar ge | 32 | 128.0 | N/A | 5.0 | 500 | Yes | 2 | 8 |
| xn4v2 | ecs.xn4v 2.small | 1 | 1.0 | N/A | 0.5 | 50 | Yes | 1 | 1 |
| e4v2 | ecs.e4v2 .small | 1 | 8.0 | N/A | 0.5 | 50 | Yes | 1 | 1 |
|   | ecs.e4v2 .large | 2 | 16.0 | N/A | 0.5 | 100 | Yes | 1 | 1 |
|   | ecs.e4v2 .xlarge | 4 | 32.0 | N/A | 0.8 | 150 | Yes | 1 | 2 |
|   | ecs.e4v2 .2xlarge | 8 | 64.0 | N/A | 1.2 | 300 | Yes | 1 | 3 |
|   | ecs.e4v2 .4xlarge | 16 | 128.0 | N/A | 2.5 | 400 | Yes | 1 | 8 |

The following table describes burstable instance families.

| Insta nce famil y | Insta nce type | vCPU s | Mem ory (GiB) | Basel ine CPU com putin g perf orma nce | CPU credi ts per hour | Max CPU credi t bala nce | Local stora ge (GiB) | Band widt h (Gbit /s) | Pack et forw ardin g rate (Kpp s) | NIC queu es | ENIs (inclu ding one prim ary ENI) |
|---|---|---|---|---|---|---|---|---|---|---|---|

| Insta nce famil y | Insta nce type | vCPU s | Mem ory (GiB) | Basel ine CPU com putin g perf orma nce | CPU credi ts per hour | Max CPU credi t bala nce | Local stora ge (GiB) | Band widt h (Gbit /s) | Pack et forw ardin g rate (Kpp s) | NIC queu es | ENIs (inclu ding one prim ary ENI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | ecs.t 5- lc2m 1.nan o | 1 | 0.5 | 20% | 12 | 288 | N/A | 0.1 | 40 | 1 | 1 |
|   | ecs.t 5- lc1m 1.sm all | 1 | 1.0 | 20% | 12 | 288 | N/A | 0.2 | 60 | 1 | 1 |
|   | ecs.t 5- lc1m 2.sm all | 1 | 2.0 | 20% | 12 | 288 | N/A | 0.2 | 60 | 1 | 1 |
|   | ecs.t 5- lc1m 2.lar ge | 2 | 4.0 | 20% | 24 | 576 | N/A | 0.4 | 100 | 1 | 1 |
|   | ecs.t 5- lc1m 4.lar ge | 2 | 8.0 | 20% | 24 | 576 | N/A | 0.4 | 100 | 1 | 1 |
|   | ecs.t 5- c1m1 .larg e | 2 | 2.0 | 25% | 30 | 720 | N/A | 0.5 | 100 | 1 | 1 |
|   | ecs.t 5- c1m2 .larg e | 2 | 4.0 | 25% | 30 | 720 | N/A | 0.5 | 100 | 1 | 1 |

|   | e·What is ECS? Elastic Compute Servic |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Insta nce famil y | Insta nce type | vCPU s | Mem ory (GiB) | Basel ine CPU com putin g perf orma nce | CPU credi ts per hour | Max CPU credi t bala nce | Local stora ge (GiB) | Band widt h (Gbit /s) | Pack et forw ardin g rate (Kpp s) | NIC queu es | ENIs (inclu ding one prim ary ENI) |
| t 5 | ecs.t 5- c1m4 .larg e | 2 | 8.0 | 25% | 30 | 720 | N/A | 0.5 | 100 | 1 | 1 |
|   | ecs.t 5- c1m1 .xlar ge | 4 | 4.0 | 25% | 60 | 1,440 | N/A | 0.8 | 200 | 1 | 2 |
|   | ecs.t 5- c1m2 .xlar ge | 4 | 8.0 | 25% | 60 | 1,440 | N/A | 0.8 | 200 | 1 | 2 |
|   | ecs.t 5- c1m4 .xlar ge | 4 | 16.0 | 25% | 60 | 1,440 | N/A | 0.8 | 200 | 1 | 2 |
|   | ecs.t 5- c1m1 .2xlar ge | 8 | 8.0 | 25% | 120 | 2,880 | N/A | 1.2 | 400 | 1 | 2 |
|   | ecs.t 5- c1m2 .2xlar ge | 8 | 16.0 | 25% | 120 | 2,880 | N/A | 1.2 | 400 | 1 | 2 |
|   | ecs.t 5- c1m4 .2xlar ge | 8 | 32.0 | 25% | 120 | 2,880 | N/A | 1.2 | 400 | 1 | 2 |

|   | mpute Service User Guide·What is ECS |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Insta nce famil y | Insta nce type | vCPU s | Mem ory (GiB) | Basel ine CPU com putin g perf orma nce | CPU credi ts per hour | Max CPU credi t bala nce | Local stora ge (GiB) | Band widt h (Gbit /s) | Pack et forw ardin g rate (Kpp s) | NIC queu es | ENIs (inclu ding one prim ary ENI) |
|   | ecs.t 5- c1m1 .4xlar ge | 16 | 16.0 | 25% | 240 | 5,760 | N/A | 1.2 | 600 | 1 | 2 |
|   | ecs.t 5- c1m2 .4xlar ge | 16 | 32.0 | 25% | 240 | 5,760 | N/A | 1.2 | 600 | 1 | 2 |

The following table describes the ecs.anyshare custom instance type.

| Instance family | vCPUs (x) | Memory (GiB) | Bandwidt h (Gbit/s) | Packet forwardin g rate (Kpps) | NIC queues | ENIs (including one primary ENI) | Disk bandwidt h (Gbit/s) |
|---|---|---|---|---|---|---|---|
| Cust om inst ance t ype ecs.anys hare | 0 < x <=2 | 1 to 16 | 0.5 | 100 | 1 | 2 | 0.5 |
|   | 2 < x <=4 | 2 to 32 | 0.8 | 100 + (x - 2)/0.2 | 1 | 2 | 0.8 |
|   | 4 < x <=8 | 4 to 64 | 0.8 + (x - 5)/4 | 200 + (x - 4)/0.2 | 1 | 3 | 0.8 + (x - 5)/4 |
|   | 8 < x <=12 | 8 to 96 | 1.5 + (x - 8)/8 | 400 + (x - 8)/0.8 | 2 | 3 | 1.5 + (x - 8)/4 |
|   | 12 < x <=16 | 12 to 128 | 2 + (x - 12)/4 | 450 + (x - 12)/0.8 | 3 | 4 | 1 |
|   | 16 < x <=24 | 16 to 196 | 3 + (x - 16)/8 | 500 + (x - 16)/0.8 | 3 | 5 | 1 + (x - 16)/8 |
|   | 24 < x <=32 | 24 to 256 | 4 + (x - 24)/8 | 600 + (x - 24)/0.4 | 4 | 6 | 2 + (x - 24)/8 |
|   | x > 32 | 32 to 352 | min(5 + (x - 32)/8, 10) | min(800 + (x- 32)/0.8, 1200) | 4 | 8 | min(3 + (x - 32)/8, 8) |

The following instance types are applicable only in environments that are upgraded from Apsara Stack V2 to V3.

| Instance family | Instance type | vCPUs | Memory (GiB) |
|---|---|---|---|
| n1 | ecs.n1.tiny | 1 | 1.0 |
|   | ecs.n1.small | 1 | 2.0 |
|   | ecs.n1.medium | 2 | 4.0 |
|   | ecs.n1.large | 4 | 8.0 |
|   | ecs.n1.xlarge | 8 | 16.0 |
|   | ecs.n1.3xlarge | 16 | 32.0 |
|   | ecs.n1.7xlarge | 32 | 64.0 |
| n2 | ecs.n2.small | 1 | 4.0 |
|   | ecs.n2.medium | 2 | 8.0 |
|   | ecs.n2.large | 4 | 16.0 |
|   | ecs.n2.xlarge | 8 | 32.0 |
|   | ecs.n2.3xlarge | 16 | 64.0 |
|   | ecs.n2.7xlarge | 32 | 128.0 |
| e3 | ecs.e3.small | 1 | 8.0 |
|   | ecs.e3.medium | 2 | 16.0 |
|   | ecs.e3.large | 4 | 32.0 |
|   | ecs.e3.xlarge | 8 | 64.0 |
|   | ecs.e3.3xlarge | 16 | 128.0 |
| c1 | ecs.c1.small | 8 | 8.0 |
|   | ecs.c1.large | 8 | 16.0 |
| c2 | ecs.c2.medium | 16 | 16.0 |
|   | ecs.c2.large | 16 | 32.0 |
|   | ecs.c2.xlarge | 16 | 64.0 |
| m1 | ecs.m1.medium | 4 | 16.0 |
|   | ecs.m1.xlarge | 8 | 32.0 |

| lastic Compute Service |   |   |   |
|---|---|---|---|
|   |   |   | User Guide·What is ECS |
| Instance family | Instance type | vCPUs | Memory (GiB) |
| m2 | ecs.m2.medium | 4 | 32.0 |
| s1 | ecs.s1.small | 1 | 2.0 |
|   | ecs.s1.medium | 1 | 4.0 |
|   | ecs.s1.large | 1 | 8.0 |
| s2 | ecs.s2.small | 2 | 2.0 |
|   | ecs.s2.large | 2 | 4.0 |
|   | ecs.s2.xlarge | 2 | 8.0 |
|   | ecs.s2.2xlarge | 2 | 16.0 |
| s3 | ecs.s3.medium | 4 | 4.0 |
|   | ecs.s3.large | 4 | 8.0 |
| t 1 | ecs.t1.small | 1 | 1.0 |

### 1.3 Instance lifecycle

The lifecycle of an ECS instance begins when the instance is created and ends when the instance is released. This topic describes the instance states in the ECS console, state attributes, and corresponding instance states in API responses. The following table describes the states that an ECS instances may go through during its lifecycle. Instance states

| State | State attribute | Description | State in an API response |
|---|---|---|---|
| Instance being created | Intermediate | The instance is being created and waiting to be started. If an instance remains in the Instance being created state for an extended period of time, an exception has occurred. | Pending |
| Starting | Intermediate | When you start or restart an instance by using the ECS console or calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Starting state for an extended period of time, an exception has occurred. | Starting |

| State | State attribute | Description | State in an API response |
|---|---|---|---|
| Running | Stable | While an instance is in the Running state, the instance can function normally and can accommodate your business needs. | Running |
| Stopping | Intermediate | When you stop an instance by using the ECS console or calling an API operation, the instance enters this state before it enters the Stopped state. If an instance remains in the Stopping state for an extended period of time, an exception has occurred. | Stopping |
| Stopped | Stable | An instance enters this state when it is stopped. An instance in the Stopped state cannot provide external services. | Stopped |
| Reinitializing | Intermediate | When you re-initialize the system disk or a data disk of an instance by using the ECS console or calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Reinitializing state for an extended period of time, an exception has occurred. | Stopped |
| Changing system disk | Intermediate | When you replace the system disk of an instance by using the ECS console or calling an API operation, the instance enters the Changing system disk state before it enters the Running state. If an instance remains in the Changing system disk state for an extended period of time, an exception has occurred. | Stopped |

describes the relationships between instance states in the ECS console and instance states in API responses. The following figure shows the transitions between instance states in API responses. Transitions between instance states in API responses

## 2 Instructions

### 2.1 Restrictions

Learn about restrictions before performing operations on ECS instances. Do not upgrade the kernel or operating system version of an ECS instance. Do not start SELinux for Linux systems except CentOS and RedHat. Do not detach PVDriver. Do not arbitrarily modify the MAC address of the network interface.

### 2.2 Suggestions

Consider the following suggestions to make more efficient use of ECS: ECS instances with 4 GiB or higher memory must use a 64-bit operating system. 32-bit operating systems have a maximum of 4 GiB of memory addressing. A 32-bit Windows operating system supports a maximum of 4 CPU cores. To ensure service continuity and avoid failover-induced service unavailability, we recommend that you configure service applications to boot automatically at system startup.

### 2.3 Limits

Before using ECS instances, you must be familiar with the limits of instance families. General limits Windows operating systems support a maximum of 64 vCPUs in instance specifications. ECS instances do not support the installation of virtualization software and secondary virtualization. Sound card applications are not supported. Only GPU instances support virtual sound cards. External hardware devices, such as hardware dongles, USB flash drives, external hard disks, and bank U keys, cannot be directly connected to ECS instances. ECS does not support multicast protocols. If multicasting services are required, we recommend that you use unicast instead. Instance family ga1 To create a ga1 instance, you must use one of the following images pre-installed with drivers: Ubuntu 16.04 with an AMD GPU driver pre-installed Windows Server 2016 English version with an AMD GPU driver pre-installed Windows Server 2008 R2 English version with an AMD GPU driver pre-installed Note: A ga1 instance uses an optimized driver provided by Alibaba Cloud and AMD. The driver is installed in images provided by Alibaba Cloud and is currently unavailable for download. If the GPU driver malfunctions due to improper removal of related components, you need to replace the system disk to restore GPU related functions. Not e This operation causes data loss. If the driver malfunctions because an improper image is selected, you need to replace the system disk to reselect an image with an AMD GPU driver pre-installed. For Windows Server 2008 or earlier, you cannot connect to the VNC after the GPU driver takes effect. The VNC is irresponsive with a black screen or stuck at the splash screen. You can use other methods such as Remote Desktop Protocol (RDP) to access the system. RDP does not support DirectX, OpenGL, or other related applications. You need to install the VNC and a client, or use other supported protocols such as PCOIP and XenDesktop HDX 3D. Instance families gn4, gn5i, and gn5 Bandwidth: If you use an image of Windows Server 2008 R2 for a gn4 instance, you cannot use the Connect to VNC function in the ECS console to connect to the instance after the installed GPU driver takes effect. You need to set the bandwidth to a non-zero value or attach an Elastic IP address to the created instance. Image: If an NVIDIA GPU driver is not required, you can select any image, and then Install the CUDA and GPU drivers for a Linux instance or Install the CUDA and GPU drivers for a Windows instance.

### 2.4 Notice for Windows users

Before using Windows-based ECS instances, you must consider the following points: Data loss may occur if a local disk is used as the data disk of an instance. We recommend that you use a cloud disk to create your instance if you are not sure about the reliability of the data architecture. Do not close the built-in shutdownmon.exe process. Otherwise, the server may require a longer time to restart. Do not rename, delete, or disable Administrator accounts or it may affect the use of the server. We do not recommend that you use virtual memory. When you modify your computer name, you must synchronize the following key values in the registry. Otherwise, the computer name cannot be modified, causing failure when installing certain third-party programs. The following key values must be modified in the registry:

```
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ActiveComputerName HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
```

### 2.5 Notice for Linux users

Before using Linux-based ECS instances, you must consider the following points: Do not modify content of the default /etc/issue files under a Linux instance. Otherwise, the custom image created from the instance cannot be recognized, and instances created based on the image cannot start as expected. Do not arbitrarily modify the permissions of each directory in the partition where the root directory is located, especially permissions of /etc, /sbin, /bin, /boot, /dev, /usr, and /lib directories. Improper modification of permissions can cause errors. Do not rename, delete, or disable Linux root accounts. Do not compile or perform any other operations on the Linux kernel. We do not recommend the use of Swap for partitioning. Do not enable the NetWorkManager service. This service conflicts with the internal network service of the system, causing network errors.

### 2.6 Notice on defense against DDoS attacks

attacks You need to purchase Anti-DDoS Pro to defend against DDoS attacks. For more information, see Apsara Stack Security Product Introduction.

## 3 Quick start

### 3.1 Overview

This topic describes how to quickly create and connect to an ECS instance. Perform the following procedure: A security group is a virtual firewall used to control traffic to and from ECS instances. Each ECS instance must be added to at least one security group. Before creating an instance, you must select a security group to control traffic to and from the instance. An ECS instance is a virtual machine that contains basic computing components such as CPU, memory, operating system, network, and disks. After a security group is created, you can select an instance type based on your business requirements. For more information, see Instance types. Select a remote connection method based on the network configuration and operating system of the ECS instance and your local operating system. After you log on to the instance, you can perform other operations on it, such as installing applications.

### 3.2 Log on to the ECS console

This topic describes how to log on to the ECS console. Prerequisites Before logging on to the ASCM console, make sure that you have obtained the IP address or domain name of the ASCM console from the deployment personnel. The URL used to access the ASCM console is in the following format: https://[IP address or domain name of the ASCM console]. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL used to access the ASCM console. Press the Enter key.
2. Enter your username and password.
Obtain the username and password for logging on to the console from the operations administrator. Not e When you log on to the ASCM console for the first time, you must change the password of your username as prompted. Due to security concerns, your password must meet the minimum complexity requirements: The password must be 8 to 20 characters in length and must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).
3. Click Login to go to the ASCM console homepage.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.

### 3.3 Create a security group

Security groups are an important means for network security isolation. They are used to set network access control for one or more ECS instances. Prerequisites A Virtual Private Cloud (VPC) has been created. For more information, see VPC User Guide . Context Instances that belong to the same account and are in the same region and in the same security group can communicate with each other over the internal network. If instances that belong to the same account in the same region are in different security groups, you can implement internal network communication by authorizing mutual access between two security groups. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click New Securit y Group.
5. Configure the parameters of the security group.

| Type | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | The organization to which the security group belongs. Make sure that the security group and the VPC belong to the same organization. |
|   | Resource Set | Yes | The resource set to which the security group belongs. Make sure that the security group and the VPC belong to the same resource set. |
|   | Region | Yes | The region to which the security group belongs. Make sure that the security group and the VPC belong to the same region. |
|   | Zone | Yes | The ID of the zone where the security group resides. |

|   |   |   | Elastic Compute Servic |
|---|---|---|---|
| Type | Parameter | Required | Description |
|   | VPC | Yes | The VPC to which the security group belongs. |
|   | Security Group Name | No | The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). It cannot start with http:// or https://. |
| Basic Settings |   |   |   |
|   | Description | No | The description of the security group. We recommend that you provide an informational description to simplify future management operations. The name must be 2 to 256 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), and commas (,). It cannot start with http:// or https://. |

6. Click Submit .

### 3.4 Create an instance

An ECS instance is a virtual machine that contains the basic computing components of a server, such as CPU, memory, operating system, network, and disks. Prerequisites A VPC and a VSwitch are created. For more information, see Create a VPC and Create a VSwitch in Apsara Stack VPC User Guide. If you want to assign an IPv6 address to the instance that you want to create, make sure that the VPC and VSwitch are associated with IPv6 CIDR blocks. For more information, see Enable an IPv6 CIDR b lock for a VPC and Enable an IPv6 CIDR block for a VSwitch in Apsara Stack VPC User Guide. A security group is available. If no security group is available, create a security group. For more information, see Create a security group. Context Some limits apply when you create GPU-accelerated instances. For more information, see Limits. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. Click Creat e Inst ance.
4. Configure parameters listed in the following tables to create an instance.
i. Configure the basic settings of the instance.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select an organization in which to create the instance. |
| Resource Set | Yes | Select a resource set in which to create the instance. |

ii. Select a region and zone for the instance.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | Select a region in which to create the instance. |
| Zone | Yes | Select a zone in which to create the instance. Zones are the physical zones with separate power supplies and networks in the same region. The internal networks of zones are interconnected, and faults in one zone are isolated from the other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |

iii. Configure the network of the instance.

| Parameter | Required | Description |
|---|---|---|
| Network Type | Yes | Select the type of the network in which to create the instance. VPC is available. |
| VPC | Yes | Select a VPC in which to create the instance. |
| VSwitch | Yes | Select a VSwitch to be connected to the instance. |
| Private IP | No | Specify a private IP address for the instance. The private IP address must be within the CIDR block of the VSwitch. If you do not specify a private IP address, the system will automatically allocate a private IP address to the instance. |

iv. (Optional)Specify whether to assign an IPv6 address to the instance. v. Select a security group in which to create the instance. vi. Select an instance family and instance type for the instance.

| Parameter | Required | Description |
|---|---|---|
| Instance Family | Yes | Select an instance family for the instance. After you select an instance family, you must select an instance type. |
| Instance Type | Yes | Select an instance type. Windows Server images require specific CPU and memory combinations. For more information, see Limits in ECS Product Introduction. |

vii. Configure the image to be used by the instance.

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image and Cust om Image. |

| Parameter | Required | Description |
|---|---|---|
| Public Image | Subject to the image type | Select a public image for the instance. Public images provided by Alibaba Cloud are licensed, secure, and stable. Public images include Windows Server images and major Linux images. This parameter must be specified when you set Image Type to Public Image. When you use an image that supports DHCPv6 to create an instance, an IPv6 address is automatically assigned to the instance. The created instance can use this IPv6 address to communicate over the internal network. When you use an image that does not support DHCPv6 to create an instance, you must manually assign an IPv6 address to the instance. The following images support DHCPv6: Linux images: CentOS 7.6 IPv6 64-bit CentOS 6.10 64-bit SUSE Linux Enterprise Server 12 SP4 64-bit Windows Server images Not e To use an IPv6 address to communicate over the Internet, you must also enable public bandwidth for the IPv6 address. For more information, see Enable Internet bandwidth for an IPv6 address in A psara Stack VPC User Guide. |
| Custom Image | Subject to the image type | Select a custom image for the instance. Custom images are created from instances or snapshots, or imported from your local device. This parameter must be specified when you set Image Type to Cust om Image. |

viii. Configure the storage settings for the instance.

| Parameter | Required | Description |
|---|---|---|
| System Disk | Yes | Specify the disk category and capacity of the system disk. Valid disk categories: Ult ra Disk and SSD Disk. The system disk size must range from 20 GiB to 500 GiB. |
| Data Disk | No | You can click Data Disk to add data disks. Specify the disk category and capacity of each data disk. Valid disk categories: Ult ra Disk and SSD Disk. A maximum of 16 data disks can be added to an instance. The maximum capacity of each data disk is 32 TiB. You can select or clear Release wit h Inst ance and Encrypt for each data disk. To encrypt a data disk, set Encrypt ion Algorit hm to AES256 or SM4 and set Encrypt ion Key to a key created in Key Management Service (KMS). You can also add data disks after the instance is created. For more information, see Create a disk. |

ix. Configure the logon password settings for the instance.

| Parameter | Required | Description |   |
|---|---|---|---|
| Set Password | Yes | Specify when to set the password. Valid values: Now and Lat er. If Later is selected, you can use the password reset feature to set a password at a later time. For more information, see Change the logon password of an instance. Not e The password is used to log on to the instance, not to the VNC. |   |
| Logon Password | No | Set the password to be used to log on to the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / _ |   |
|   |   |   | ( ) ` ~ ! @ # $ % ^ & |
|   |   | * - + = \| { } [ ] : ; ' < > , . ? / _ |   |
| Confirm Password | No | Re-enter the password. |   |

x. (Optional)Select a deployment set in which to create the instance. xi. (Optional)Enter a name for the instance. The name must be 2 to 128 characters in length and start with a letter. It can contain periods (.), underscores (_), colons (:), and hyphens (-). If you do not specify a name, the system will assign an instance name at random. xii. (Optional)In the User Data field, enter the user data to be automatically run upon instance startup. Windows supports Batch and PowerShell scripts. Before you perform Base64 encoding, make sure that the content to be encoded includes `[bat]` or `[powershell]` as the first line. Linux supports shell scripts. xiii. Enter the number of instances that you want to create. The number must be an integer ranging from 1 to 100.
5. Click Submit .
Result The instance appears in the instance list. When the instance is being created, it is in the Preparing state. After the instance is created, it enters the Running state.

### 3.5 Connect to an instance

#### 3.5.1 Instance connecting overview

After an instance is created, you can connect to the instance to perform operations such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that have public IP addresses. For more information about the procedure, see the following topics: Connect to a Linux-based instance by using SSH commands in Linux or Mac OS X Connect to a Linux-based instance by using remote connection tools in Windows Connect to a Windows-based instance by using RDP Use the VNC feature in the ECS console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator, and that of a Linux instance is root.

#### 3.5.2 Connect to a Linux instance by using SSH commands in Linux or Mac OS X

commands in Linux or Mac OS X This topic describes how to use SSH commands to connect to a Linux instance. Prerequisites The instance and the security group are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

| Rule direction | Authorizati on policy | Protocol type | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Accept | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

Procedure
1. Enter the following command and press the Enter key.

```
ssh root@instance IP
```

2. Enter the instance password of the root user and press the Enter key.

#### 3.5.3 Connect to a Linux-based instance by using remote connection tools in Windows

remote connection tools in Windows This topic describes how to connect to an instance by using the PuTTY tool. Prerequisites Remote connection tools are designed with similar logics. In this example, PuTTY is used to connect to an instance. Download PuTTY at the following URL: .
1. Download and install PuTTY for Windows.
2. Start the PuTTY client and complete the following settings:
Host Name (or IP Address): Enter the EIP of the instance to be connected. Port: Select the default port 22. Connection Type: Select SSH. Saved Session: Enter the name of the session. Click Save. After the settings are saved, PuTTY remembers the name and IP address of the instance. This eliminates the need to enter them every time you connect to the instance.
3. Click Open to connect to the instance.
When you connect to the instance for the first time, PuTTY displays security alerts. Click Yes to proceed.
4. Enter the username root and press Enter.
5. Enter the password for the instance and press Enter.
If a message similar to the following one appears, a connection to the instance is established.

```
Welcome to aliyun Elastic Compute Server!
```

#### 3.5.4 Connect to a Windows instance by using RDP

RDP This topic describes how to connect to a Windows instance by using Remote Desktop Protocol (RDP). Prerequisites The instance and the security group are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the RDP port.

| Rule direction | Authorizati on policy | Protocol type | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Accept | TCP | 3389/3389 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

CredSSP-related security updates are installed on the operating system of the instance.
1. Activate the Remote Desktop Connection feature by using any of the following methods:
Click St art , enter mstsc in the search box, and click mst sc in the search result. Press Windows Key + R. In the Run dialog box that appears, enter mstsc and click OK.
2. In the Remot e Deskt op Connect ion dialog box, enter the EIP of the instance and click Show
Opt ions.
3. Enter the username.
The default username is administrator.
4. (Optional)If you do not want to enter the password upon subsequent logons, select Allow me t o
save credent ials.
5. Click Connect .
6. In the Windows Securit y dialog box that appears, enter the password for the account and click
OK. Result After you log on to the instance, the Windows desktop appears. If authentication errors occur or the required function is not supported, install security updates.
1. Connect to an ECS instance by using the VNC before proceeding.
2. Choose St art > Cont rol Panel.
3. Click Syst em and Securit y.
4. Click Check f or updat es in the Windows Updat es pane.
5. If updates are available, click Inst all updat es.
6. Restart the instance.

#### 3.5.5 Connect to an ECS instance by using the VNC

VNC You can access your instance by using the VNC in the ECS console when other SSH clients such as PuTTy, Xshell, and SecureCRT do not work properly. Prerequisites The instance is in the Running state. The root certificate is imported to your web browser. For more information, see Install a certificate. If you log on to an instance for the first time after the instance is created, make sure that you set a new VNC password. For more information, see Change the VNC password. Context The VNC password is used to log on to the VNC of the ECS console, and the instance password is used to log on to an instance. You can use the VNC to connect to an instance to solve issues shown in the following table.

| Scenario | Resolution |
|---|---|
| The instance startup is slowly due to self-check upon startup. | Check the progress of the self check. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear, which consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance, and click Remot e Connect ion in the Act ions column.
5. Enter the VNC password, and then click OK.
After the connection is successful, the logon page is displayed, as shown in the following figure.
6. Enter the username and password.
For Linux instances: Enter the username root and the logon password. Not e Passwords in Linux are not displayed as you type. Press the Enter key after you enter the password. For Windows instances: To use key combinations such as Ctrl + Alt + Delete, click the corresponding key combination in the upper-right corner of the VNC page. Enter the username and password as prompted, and click the Log In icon .

## 4 Instances

### 4.1 Create an instance

An ECS instance is a virtual machine that contains the basic computing components of a server, such as CPU, memory, operating system, network, and disks. Prerequisites A VPC and a VSwitch are created. For more information, see Create a VPC and Create a VSwitch in Apsara Stack VPC User Guide. If you want to assign an IPv6 address to the instance that you want to create, make sure that the VPC and VSwitch are associated with IPv6 CIDR blocks. For more information, see Enable an IPv6 CIDR b lock for a VPC and Enable an IPv6 CIDR block for a VSwitch in Apsara Stack VPC User Guide. A security group is available. If no security group is available, create a security group. For more information, see Create a security group. Context Some limits apply when you create GPU-accelerated instances. For more information, see Limits. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. Click Creat e Inst ance.
4. Configure parameters listed in the following tables to create an instance.
i. Configure the basic settings of the instance.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select an organization in which to create the instance. |
| Resource Set | Yes | Select a resource set in which to create the instance. |

ii. Select a region and zone for the instance.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | Select a region in which to create the instance. |
| Zone | Yes | Select a zone in which to create the instance. Zones are the physical zones with separate power supplies and networks in the same region. The internal networks of zones are interconnected, and faults in one zone are isolated from the other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |

iii. Configure the network of the instance.

| Parameter | Required | Description |
|---|---|---|
| Network Type | Yes | Select the type of the network in which to create the instance. VPC is available. |
| VPC | Yes | Select a VPC in which to create the instance. |
| VSwitch | Yes | Select a VSwitch to be connected to the instance. |
| Private IP | No | Specify a private IP address for the instance. The private IP address must be within the CIDR block of the VSwitch. If you do not specify a private IP address, the system will automatically allocate a private IP address to the instance. |

iv. (Optional)Specify whether to assign an IPv6 address to the instance. v. Select a security group in which to create the instance. vi. Select an instance family and instance type for the instance.

| Parameter | Required | Description |
|---|---|---|
| Instance Family | Yes | Select an instance family for the instance. After you select an instance family, you must select an instance type. |
| Instance Type | Yes | Select an instance type. Windows Server images require specific CPU and memory combinations. For more information, see Limits in ECS Product Introduction. |

vii. Configure the image to be used by the instance.

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image and Cust om Image. |
| Public Image | Subject to the image type | Select a public image for the instance. Public images provided by Alibaba Cloud are licensed, secure, and stable. Public images include Windows Server images and major Linux images. This parameter must be specified when you set Image Type to Public Image. When you use an image that supports DHCPv6 to create an instance, an IPv6 address is automatically assigned to the instance. The created instance can use this IPv6 address to communicate over the internal network. When you use an image that does not support DHCPv6 to create an instance, you must manually assign an IPv6 address to the instance. The following images support DHCPv6: Linux images: CentOS 7.6 IPv6 64-bit CentOS 6.10 64-bit SUSE Linux Enterprise Server 12 SP4 64-bit Windows Server images Not e To use an IPv6 address to communicate over the Internet, you must also enable public bandwidth for the IPv6 address. For more information, see Enable Internet bandwidth for an IPv6 address in A psara Stack VPC User Guide. |
| Custom Image | Subject to the image type | Select a custom image for the instance. Custom images are created from instances or snapshots, or imported from your local device. This parameter must be specified when you set Image Type to Cust om Image. |

viii. Configure the storage settings for the instance.

| Parameter | Required | Description |
|---|---|---|
| System Disk | Yes | Specify the disk category and capacity of the system disk. Valid disk categories: Ult ra Disk and SSD Disk. The system disk size must range from 20 GiB to 500 GiB. |
| Data Disk | No | You can click Data Disk to add data disks. Specify the disk category and capacity of each data disk. Valid disk categories: Ult ra Disk and SSD Disk. A maximum of 16 data disks can be added to an instance. The maximum capacity of each data disk is 32 TiB. You can select or clear Release wit h Inst ance and Encrypt for each data disk. To encrypt a data disk, set Encrypt ion Algorit hm to AES256 or SM4 and set Encrypt ion Key to a key created in Key Management Service (KMS). You can also add data disks after the instance is created. For more information, see Create a disk. |

ix. Configure the logon password settings for the instance.

| Parameter | Required | Description |   |
|---|---|---|---|
| Set Password | Yes | Specify when to set the password. Valid values: Now and Lat er. If Later is selected, you can use the password reset feature to set a password at a later time. For more information, see Change the logon password of an instance. Not e The password is used to log on to the instance, not to the VNC. |   |
| Logon Password | No | Set the password to be used to log on to the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / _ |   |
|   |   |   | ( ) ` ~ ! @ # $ % ^ & |
|   |   | * - + = \| { } [ ] : ; ' < > , . ? / _ |   |
| Confirm Password | No | Re-enter the password. |   |

x. (Optional)Select a deployment set in which to create the instance. xi. (Optional)Enter a name for the instance. The name must be 2 to 128 characters in length and start with a letter. It can contain periods (.), underscores (_), colons (:), and hyphens (-). If you do not specify a name, the system will assign an instance name at random. xii. (Optional)In the User Data field, enter the user data to be automatically run upon instance startup. Windows supports Batch and PowerShell scripts. Before you perform Base64 encoding, make sure that the content to be encoded includes `[bat]` or `[powershell]` as the first line. Linux supports shell scripts. xiii. Enter the number of instances that you want to create. The number must be an integer ranging from 1 to 100.
5. Click Submit .
Result The instance appears in the instance list. When the instance is being created, it is in the Preparing state. After the instance is created, it enters the Running state.

### 4.2 Connect to an instance

#### 4.2.1 Instance connecting overview

After an instance is created, you can connect to the instance to perform operations such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that have public IP addresses. For more information about the procedure, see the following topics: Connect to a Linux-based instance by using SSH commands in Linux or Mac OS X Connect to a Linux-based instance by using remote connection tools in Windows Connect to a Windows-based instance by using RDP Use the VNC feature in the ECS console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator, and that of a Linux instance is root.

#### 4.2.2 Connect to a Linux-based instance by using SSH commands in Linux or Mac OS X

SSH commands in Linux or Mac OS X This topic describes how to use SSH commands to connect to a Linux-based instance. Prerequisites Create a security group and an instance. Procedure
1. Enter the following command: `ssh root@instance IP` .
2. Enter the password for the root user to log on to the instance.

#### 4.2.3 Connect to a Linux-based instance by using remote connection tools in Windows

remote connection tools in Windows This topic describes how to connect to an instance by using the PuTTY tool. Prerequisites Remote connection tools are designed with similar logics. In this example, PuTTY is used to connect to an instance. Download PuTTY at the following URL: . Procedure
1. Download and install PuTTY for Windows.
2. Start the PuTTY client and complete the following settings:
Host Name (or IP Address): Enter the EIP of the instance to be connected. Port: Select the default port 22. Connection Type: Select SSH. Saved Session: Enter the name of the session. Click Save. After the settings are saved, PuTTY remembers the name and IP address of the instance. This eliminates the need to enter them every time you connect to the instance.
3. Click Open to connect to the instance.
When you connect to the instance for the first time, PuTTY displays security alerts. Click Yes to proceed.
4. Enter the username root and press Enter.
5. Enter the password for the instance and press Enter.
If a message similar to the following one appears, a connection to the instance is established.

```
Welcome to aliyun Elastic Compute Server!
```

#### 4.2.4 Connect to a Windows instance by using RDC

RDC This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC). Prerequisites A security group and a Windows instance are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

| Rule direction | Action | Protocol | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 addresses | 0.0.0.0/0 |

Procedure
1. Use one of the following methods to enable RDC:
Click St art , enter mstsc in the search box, and click mst sc in the search result. Press the Windows logo key+R. In the Run dialog box that appears, enter mstsc and click OK.
2. In the Remot e Deskt op Connect ion dialog box, enter the Elastic IP address of the instance and
click Show Opt ions.
3. Enter the username.
The default username is administrator.
4. (Optional)If you do not want to enter the password upon subsequent logons, select Allow me t o
save credent ials.
5. Click Connect .
6. In the Windows Securit y dialog box that appears, enter the password corresponding to the
username you entered and click OK. Result If the Windows desktop appears, a connection to the Windows instance is established. If an error message is returned indicating that an authentication error has occurred and the function requested is not supported, install CredSSP updates and try again. Follow these steps to install the updates:
1. Connect to an ECS instance by using the VNC.
2. Choose St art > Cont rol Panel.
3. Click Syst em and Securit y.
4. Click Check f or updat es in the Windows Updat es section.
5. If updates are available, click Inst all updat es.
6. Restart the instance.

#### 4.2.5 Install the certificate for VNC in Windows

Before you log on to VNC, you must export the relative certificate from the site such as the Apsara Stack Cloud Management (ASCM) console and install the certificate in your local browser. Context The VNC feature is provided by the VNC proxy service. The VNC proxy service uses the relative certificate different from that of Apsara Infrastructure Management Framework. The certificate of the VNC proxy service must be manually imported. Procedure
1. Export the certificate from the ASCM console.
i. Log on to the ASCM console. Press the F12 key or Fn+F12 to view and select the certificate. For example, in the Chrome browser, press the F12 key to open Chrome DevTools. ii. In the Cert if icat e dialog box, click the Cert if icat e Pat h tab, select the root certificate, and then click View Cert if icat e. iii. In the Cert if icat e dialog box, click the Det ails tab, and click Copy t o File. iv. In the Cert if icat e Export Wizard dialog box, click Next . v. Select DER encoded binary X.509 (.CER) as the format and then click Next . vi. Click Browse, select where to store the certificate, enter a file name, and then click Save. vii. Click Next . viii. Click Finish. ix. Click OK.
2. Install the certificate in your local browser.
i. Double-click the certificate. ii. In the Cert if icat e dialog box, click Inst all Cert if icat e. iii. In the Cert if icat e Import Wizard dialog box, click Next . iv. Select Place all cert if icat es in t he f ollowing st ore and click Browse. v. In the Select Cert if icat e St ore dialog box, select T rust ed Root Cert if icat e Aut horit y and then click OK. vi. In the Cert if icat e Import Wizard dialog box, click Next . vii. Click Finish. viii. If a security warning message is displayed, click Yes.
3. Restart your browser and log on to the ASCM console.
If no security warning message is displayed in the left part of the address bar, the certificate is installed.

#### 4.2.6 Connect to an ECS instance by using the VNC

VNC You can access your instance by using the VNC in the ECS console when other SSH clients such as PuTTy, Xshell, and SecureCRT do not work properly. Prerequisites The instance is in the Running state. The root certificate is imported to your web browser. For more information, see Install a certificate. If you log on to an instance for the first time after the instance is created, make sure that you set a new VNC password. For more information, see Change the VNC password. Context The VNC password is used to log on to the VNC of the ECS console, and the instance password is used to log on to an instance. You can use the VNC to connect to an instance to solve issues shown in the following table.

| Scenario | Resolution |
|---|---|
| The instance startup is slowly due to self-check upon startup. | Check the progress of the self check. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear, which consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance, and click Remot e Connect ion in the Act ions column.
5. Enter the VNC password, and then click OK.
After the connection is successful, the logon page is displayed, as shown in the following figure.
6. Enter the username and password.
For Linux instances: Enter the username root and the logon password. Not e Passwords in Linux are not displayed as you type. Press the Enter key after you enter the password. For Windows instances: To use key combinations such as Ctrl + Alt + Delete, click the corresponding key combination in the upper-right corner of the VNC page. Enter the username and password as prompted, and click the Log In icon .

### 4.3 View instances

You can view the list of created instances and the details of individual instances. The details of an instance include basic configurations, disks, snapshots, security groups, and elastic network interfaces (ENIs). Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created instances that match the specified criteria are displayed.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Instance Name | Enter an instance name to search for the instance. |
| Instance ID | Enter an instance ID to search for the instance. |
| IP Address | Enter the IP address of an instance to search for the instance. |
| VPC ID | Enter a VPC ID to search for the instances that belong to the VPC. |

| c Compute Service | User Guide·Instance |
|---|---|

| Filter option | Description |
|---|---|
| Image ID | Enter an image ID to search for the instances that use the image. |
| Status | Select an instance status to search for the instances in that status. Valid values: Running St opped St art ing St opping |
| Security Group ID | Enter a security group ID to search for the instances that belong to the security group. |
| Operating System | Enter the name of operating system to search for the instances that use the operating system. |

5. Use one of the following methods to go to the Instance Details page of an instance:
In the Inst ance ID/Name column, click the instance ID. Click Manage in the Act ions column corresponding to the instance. In the Act ions column corresponding to the instance, choose More > Show Det ails.

### 4.4 Modify an instance

You can modify the name, description, and custom data of an existing instance. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and choose More > Modif y from the Act ions column.
5. Modify the name, description, and custom data for the instance.
The name must be 2 to 128 characters in length. The description must be 2 to 256 characters in length. The custom data must be 2 to 999 characters in length.
6. Click OK.

### 4.5 Stop an instance

You can stop an instance that is not in use. Stopping an instance will interrupt the services that are running on it. Exercise caution when you stop an instance. Prerequisites The instance is in the Running state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to stop the instance:
To stop a single instance, find the instance and choose More > Inst ance St at us > St op in the Act ions column. To stop one or more instances at a time, select the instances and click St op in the lower-left corner of the Instances page.
5. In the message that appears, click OK.
Result In the St at us column, the instance state changes from Running to St opping. After the instance is stopped, its state changes to St opped.

### 4.6 Start an instance

You can start a stopped instance. Prerequisites The instance is in the St opped state. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to start the instance:
To start a single instance, find the instance and choose More > Inst ance St at us > St art in the Act ions column. To start one or more instances at a time, select the instances and click St art in the lower-left corner of the Instances page.
5. In the message that appears, click OK.
Result In the St at us column, the instance state changes from St opped to St art ing. After the instance is started, its state changes to Running.

### 4.7 Restart an instance

You must restart an instance after you change its logon password or install system updates. Restarting an instance will stop the instance and interrupt the services that are running on it for a period of time. Exercise caution when you restart an instance. Prerequisites The instance is in the Running state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to restart the instance:
To restart a single instance, find the instance and choose More > Inst ance St at us > Rest art in the Act ions column. To restart one or more instances at a time, select the instances and click Rest art in the lowerleft corner of the Instances page.
5. In the Restart Instance dialog box, select a restart mode.
Rest art : restarts the instance normally. Force Rest art : forces the instance to restart. This may result in loss of unsaved data.
6. Click OK.

### 4.8 Delete an instance

You can delete an instance that is no longer needed to release its resources. Deleted instances cannot be recovered. We recommend that you back up data before you delete an instance. If a data disk is released along with the instance, the data on the disk cannot be recovered. Prerequisites The instance is in the St opped state. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select the instance and click Delet e in the lower-left corner of the Instances page.
5. In the message that appears, click OK.

### 4.9 Change the instance type of an instance

instance You can change the instance type of an instance to suit your business needs. This eliminates the need to create a new instance. Prerequisites The instance is in the St opped state. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and click Upgrade/Downgrade in the Act ions column.
5. On the Change Specifications page that appears, select a new instance type and click Submit .
The instance types available for selection are displayed on the Change Specifications page.
6. Restart the instance by using the console or calling an API operation for the new instance type to
take effect. For more information, see Start an instance or StartInstance in ECS Developer Guide.

### 4.10 Change an instance logon password

password If you did not set a logon password when creating an instance or forgot the password, you can reset the password. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and select one of the following methods to access the instance details page.
In the Inst ance ID/Name column, click the instance ID. Click Manage in the Act ions column. In the Act ions column, choose More > Show Det ails. Click Change Password. Enter and confirm the new password, and then click OK. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ' ~ ! @ # $ % ^ & * - _ + = | { } [ ] : ; ' <

```
> , . ? /
```

Restart the instance in the console or by calling an API operation to make the new password take effect. For more information, see Restart an instance or the RebootInstance section in ECS Developer Guide.

### 4.11 Change the VNC password

If you log on to the VNC for the first time or forget the VNC password, you can reset the password. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and select one of the following methods to access the instance details page.
In the Inst ance ID/Name column, click the instance ID. Click Manage in the Act ions column. In the Act ions column, choose More > Show Det ails. Click Change VNC Password. Enter and confirm the new password, and click OK. The password must be 6 characters in length and can contain digits and uppercase and lowercase letters. It does not support special characters. Restart the instance in the console or by calling an API operation to make the new password take effect. For more information, see Restart an instance or the RebootInstance section in ECS Developer Guide.

### 4.12 Add an ECS instance to a security group

security group You can add a created instance to a security group and use security group rules to control network access to the instance. Context A security group acts as a virtual firewall and is used to provide security isolation. A security group controls access to ECS instances. Instances that belong to the same account and are in the same region and in the same security group can communicate with each other over the internal network. If instances that belong to the same account in the same region are in different security groups, you can implement internal network communication by authorizing mutual access between two security groups. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group and click Manage Inst ances in the Act ions column.
5. Click Add Inst ance.
6. Select the instance and click OK.
An instance can be added to five security groups. After an instance is added, the security group rules automatically apply to the instance.

### 4.13 Customize instance data

ECS allows you to run the instance customization script upon startup and import data into instances. Context The instance data customization feature is applicable to both Windows and Linux instances. It allows you to: Run the instance customization script upon startup. Import data into instances. Usage instructions Limit s The instance data customization feature can only be used when an instance meets all the following requirements: Network type: VPC Image: a system image or a custom image that is inherited from the system image Operating system: one type included in Supported operating systems

| Windows | Linux |
|---|---|
| Windows Server 2016 64-bit Windows Server 2012 64-bit Windows Server 2008 64-bit | CentOS Ubuntu SUSE Linux Enterprise OpenSUSE Debian Aliyun Linux |

When you configure instance data customization scripts, you must enter custom data based on the type of operating system and script. Not e Only English characters are allowed. If your data is Base64 encoded, select Ent er Base64 Encoded Inf ormat ion. Not e The size of the customization script cannot exceed 16 KB before the data is Base64 encoded. For Linux instances, the script format must meet the requirements described in Types of Linux instance customization scripts. For Windows instances, the script can only start with `[bat]` or `[powershell]` . After starting an instance, run a command to view the following information: Execution result of the instance customization script Data imported to instances Console: You can modify the custom instance data in the console. Whether the modified instance customization script needs to be re-executed depends on the script type. For example, if the `bootc` `md` script in Cloud Config is modified for Linux instances, the script is automatically executed each time instances are restarted. OpenAPI: You can also use OpenAPI to customize instance data. For more information, see Creat eInst ance and Modif yInst anceAt t ribut e in ECS Developer Guide . Linux instance data customization scripts Linux instance data customization scripts provided by Alibaba Cloud are designed based on the cloudinit architecture. They are used to automatically configure parameters of Linux instances. Customization script types are compatible with the cloud-init. Description of Linux instance data customization scripts Linux instance customization scripts are executed after instances are started and before `/etc/init` is executed. Linux instance customization scripts can only be executed with root permissions by default. Types of Linux instance customization scripts User-Dat a Script Description: A script, such as shell script, is used to customize data. Format: The first line must include #! , such as #! /bin/sh . Limit: The script size (including the first line) cannot exceed 16 KB before the data is Base64 encoded. Frequency: The script is executed only when instances are started for the first time. Example:

```
#! /bin/sh
echo "Hello World. The time is now $(date -R)!" | tee /root/output10.txt
```

Cloud Conf ig Dat a Description: Predefined data is used to configure services, such as specifying yum sources or importing SSH keys. Format: The first line must be `#cloud-config` . Limit: The script size (including the first line) cannot exceed 16 KB before the data is Base64 encoded. Frequency: The script execution frequency varies with the specific service. Example:

```
#cloud-config
apt: primary:
- arches: [default]
uri: http://us.archive.ubuntu.com/ubuntu/
```

Include Description: The configuration content can be saved in a text file and imported into cloud-init as a URL. Format: The first line must be `#include` . Limit: The script size (including the first line) cannot exceed 16 KB before the data is Base64 encoded. Frequency: The script execution frequency depends on the script type in the text file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/cloudconfig
```

GZIP f ormat Description: Cloud-ini limits the size of customization scripts to 16 KB. You can compress and import the script file into the customization script if the file size exceeds 16 KB. Format: The .gz file is imported into the customization script as a URL in `#include` . Frequency: The script execution frequency depends on the script content contained in the GZIP file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/config.gz
```

View the custom data of a Linux instance Run the following command in the instance:

```bash
curl http://100.100.100.200/latest/user-data
```

Windows instance customization scripts Windows instance customization scripts independently developed by Alibaba Cloud can be used to initialize Windows instances. There are two types of Windows instance customization scripts: Batch processing program: starts with `[bat]` and serves as the first line. The script size must be smaller than 16 KB before the data is Base64 encoded. PowerShell script: starts with `[powershell]` and serves as the first line. The script size must be smaller than 16 KB before the data is Base64 encoded. View the custom data of a Windows instance Run the following PowerShell command in the instance:

```
Invoke-RestMethod http://100.100.100.200/latest/user-data/
```

### 4.14 Modify a private IP address

Each instance is assigned a private NIC and bound with a private IP address. You can modify the private IP address of the instance. The private IP address you use must be within the CIDR block of the VSwitch to which the instance belongs and cannot be used by another instance. Prerequisites The instance is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and choose More > Change Privat e IP Address from the Act ions column.
5. Enter a new private IP address and click OK.
The private IP address you can use must be within the CIDR block of the VSwitch to which the instance belongs and cannot be used by another instance or for a specific purpose. For example, if the CIDR block of the VSwitch is 192.168.1.0/24, you can use an IP address in the range of 192.168.1.1 to 192.168.1.254. The first address 192.168.1.0 identifies the subnet itself, and the last address 192.168.1.255 identifies the broadcast address. Both addresses are reserved and cannot be used.

### 4.15 Install the CUDA and GPU drivers for a Linux instance

for a Linux instance You must install a GPU driver on GPU instances to use the GPU. If the image you use does not contain a pre-installed GPU driver, you must manually install the CUDA and GPU drivers for the instance. Prerequisites If your instance cannot connect to the Internet, the installation file cannot be downloaded. You can install an FTP client on the instance to transfer the installation file to the instance. Context When installing NVIDIA drivers, you must install the kernel package that contains the kernel header file before you install the CUDA and GPU drivers on the instance. Procedure
1. Install the kernel package.
i. Run the uname -r command to view the current kernel version. A similar output is displayed: CentOS: `3.10.0-862.14.4.el7.x86_64` Ubuntu: `4.4.0-117-generic` ii. Copy the kernel package of the corresponding version to the instance and install the package. CentOS: Copy the RPM package of the `kernel-devel` component and run the rpm -ivh 3.10.0-862.14.4.el7.x86_64.rpm command to install the package. 3.10.0-862.14.4.el7.x86 _64.rpm is used as an example. Replace it with the actual package name. Ubuntu: Copy the DEB package of the `linux-headers` component and run the dpkg -i 4.4.0-117-generic.deb command to install the package. 4.4.0-117-generic.deb is used as an example. Replace it with the actual package name.
2. Download the CUDA Toolkit.
i. Access the official CUDA download page. Choose the version based on the GPU application requirements for CUDA. This example uses CUDA Toolkit 9.2. Download the CUDA Toolkit ii. Choose a platform based on your operating system. Select Inst aller T ype to runf ile (local) and click Download. NVIDIA drivers are already included in the CUDA Toolkit. Download the drivers
3. Copy the downloaded cuda_9.2.148_396.37_linux.run file to the instance. cuda_9.2.148_396.37_lin
ux.run is used as an example. Replace it with the actual file name.
4. Run the sudo sh ./cuda_9.2.148_396.37_linux.run --silent --verbose --driver --t oolkit --
samples command to install the CUDA driver. cuda_9.2.148_396.37_linux.run is used as an example. Replace it with the actual file name. The installation takes about 10 to 20 minutes. When `Driver: Installed` is displayed, the installation is successful. View the CUDA installation result
5. Run the nvidia-smi command to view the GPU driver status.
If the output displays the details of the GPU driver, the driver is running properly. View the GPU driver status What's next If you want to run the OpenGL program, you must first purchase the licenses and install the GRID drivers. For information about the installation procedure, see the official NVIDIA documentation.

### 4.16 Install the CUDA and GPU drivers for a Windows instance

for a Windows instance You must install a GPU driver on GPU instances to use the GPU. If the image you use does not contain a pre-installed GPU driver, you must manually install the CUDA and GPU drivers for the instance. Prerequisites If your instance cannot connect to the Internet, the installation file cannot be downloaded. You can install an FTP client on the instance to transfer the installation file to the instance. To compile CUDA programs, first install a Windows compiling environment, such as Visual Studio 2015. If you do not need to compile CUDA programs, ignore it.
1. Download the CUDA Toolkit.
i. Access the official CUDA download page. Choose the version based on the GPU application requirements for CUDA. This example uses CUDA Toolkit 9.2. ii. Choose a platform based on your operating system. Set Inst aller T ype to exe (local) and click Download. NVIDIA drivers are already included in the CUDA Toolkit.
2. Copy the downloaded cuda_9.2.148_windows.exe file to the instance. cuda_9.2.148_windows.exe
is used as an example. Replace it with the actual file name.
3. Double-click cuda_9.2.148_windows.exe and follow the installation wizard to install the CUDA
driver. cuda_9.2.148_windows.exe is used as an example. Replace it with the actual file name. The installation takes about 10 to 20 minutes. When `Installed: - Nsight Monitor and HUD Launc` `her` is displayed, the driver is installed.
4. Press Win + R and enter devmgmt .msc.
The NVIDIA device is displayed in Display Adapt er.
5. Press Win + R, enter cmd, and run the "C:\Program Files\NVIDIA Corporat ion\NVSMI\nvidia-
smi" command. If the output displays the details of the GPU driver, the driver is running properly. What's next If you want to run the OpenGL and DirectX programs, you must first purchase the licenses and install the GRID drivers. For information about the installation procedure, see the official NVIDIA documentation.

## 5 Disks

### 5.1 Create a disk

You can create an independent data disk and attach it to an ECS instance to increase the storage space of the instance. This topic describes how to create an empty data disk. You cannot create independent system disks. Context We recommend that you plan the number and size of data disks before you create them. The following limits apply to data disks: A maximum of 16 data disks can be attached to an instance. Disks and Shared Block Storage devices share this quota. Each Shared Block Storage device can be attached to up to four ECS instances at the same time. Each ultra disk, shared ultra disk, standard SSD, or shared SSD can have a maximum capacity of 32 TiB. Disks cannot be combined in ECS. They are independent of each other. You cannot combine multiple disks into one by formatting them. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across multiple disks, because a snapshot can only back up data of a single disk. If you create a logical volume across several disks, data discrepancies will occur when you restore these disks. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. Click Creat e Disk.
4. Configure parameters listed in the following table to create a disk.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | Select an organization in which to create the disk. |
|   | Resource Set | Yes | Select a resource set in which to create the disk. |
|   | Region | Yes | Select a region in which to create the disk. |
|   | Zone | Yes | Select a zone in which to create the disk. |

|   | Elastic Compute Servic |   |   |
|---|---|---|---|
| Section | Parameter | Required | Description |
|   | Name | Yes | Enter a name for the disk. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |
| Basic Settings |   |   |   |
|   | Specifications | Yes | Select a disk category and specify the disk size. Valid disk categories: SSD Disk Ult ra Disk Shared SSD: shared SSD Shared Ult ra Disk: shared ultra disk The disk size must range from 20 GiB to 32768 GiB. |
|   | Encrypt | No | Specify whether to encrypt the disk. |
|   | Encryption Algorithm | No | Select an encryption algorithm. This parameter is required when you set Encrypt to Yes. Valid values: AES256: AES256 encryption algorithm. SM4: Chinese encryption algorithm SM4. |

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Encryption Key | No | Select an encryption key. This parameter is required when you set Encrypt to Yes. Not e If no key is available, create a key in KMS. |
|   | Use Snapshot | No | Specify whether to create the disk from a snapshot. If you select Yes, you must specify a snapshot. The size of the created disk depends on the size of the specified snapshot. If the disk size that you specify is greater than the snapshot size, the disk will be created with the size you specified. If the disk size that you specify is smaller than the snapshot size, the disk will be created with the snapshot size. |

5. Click Submit .
Result The created disk is displayed in the disk list and in the Pending state. What's next After the disk is created, you must attach the disk to an instance and partition and format the disk. For more information, see the following topics:

### 5.2 View disks

You can view the list of created disks and the details of individual disks.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created disks that match the specified criteria are displayed.
4. Select a filter option from the drop-down list, enter the relevant information in the search box, and
click search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Disk Name | Enter a disk name to search for the disk. |
| Disk ID | Enter a disk ID to search for the disk. |
| Instance ID | Enter an instance ID to search for the disks that are attached to the instance. |
| Disk Status | Select a disk status to search for disks in that status. Valid values: Running Pending At t aching Det aching Creat ing Delet ing Delet ed Not e Deleted disks are no longer displayed in the disk list. Init ializing All St at uses |
| Disk Properties | Select a disk type to search for disks of that type. Valid values: All Syst em Disk Dat a Disk |
| Policy ID | Enter the ID of an automatic snapshot policy to search for the disks that use the policy. |

| Filter option | Description |
|---|---|
| Encryption Key ID | Enter the ID of an encryption key to search for the disks that are encrypted with the key. |

5. In the Disk ID/Name column, click a disk ID to go to the Disk Details page of the disk.
The properties and mount information of the disk are displayed on the Disk Details page.

### 5.3 Roll back a disk

If you have created snapshots for a disk, you can use a snapshot to roll back the disk to the state it was when the snapshot was taken. Rolling back a disk is irreversible. Once the disk is rolled back, the disk data before the rollback time cannot be restored. Exercise caution when you perform this operation. Prerequisites Snapshots have been created for the disk. The disk is not released. The instance where the target disk resides must be in the St opped state. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filtering option from the drop-down list, enter the relevant information in the search bar,
and click Search. You can select multiple filtering options to narrow down the search results.

| Filtering option | Description |
|---|---|
| Snapshot Name | Enter a snapshot name to search for the snapshot. |
| Snapshot ID | Enter a snapshot ID to search for the snapshot. |
| Instance ID | Enter an instance ID to search for the snapshots related to the instance. |
| Disk ID | Enter a disk ID to search for the snapshots related to the disk. |
| Snapshot Type | Select a snapshot type to search for the snapshots of that type. Options include: All User Snapshot s: manual snapshots. Aut omat ic snapshot s: automatic snapshots. |

| Filtering option | Description |
|---|---|
| Creation Time | Enter a creation time to search for the snapshots that were created at that time. |

5. Find the snapshot and click Rest ore in the Act ions column.
6. Click OK.

### 5.4 Modify the disk properties

You can modify the properties of a created disk, such as changing the settings of the Release Disk with Instance and Release Automatic Snapshots with Disk options. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk and choose More > Modif y Disk Propert ies from the Act ions column.
5. Modify the release mode.
Release Disk wit h Inst ance: When this option is selected, the disk is released together when the instance it is attached to is deleted. When this option is not selected, the disk changes to the Pending state when the instance it is attached to is deleted. Release Aut omat ic Snapshot s wit h Disk: When this option is selected, the automatic snapshots created for the disk is released together when the disk is deleted. When this option is not selected, the automatic snapshots are retained.
6. Click OK.

### 5.5 Modify the disk description

You can modify the name and description of a created disk. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk and choose More > Modif y Disk Descript ion from the Act ions column.
5. Modifies the name and description of the disk.
The name must be 2 to 128 characters in length and start with a letter. It can contain periods (.), underscores (_), colons (:), and hyphens (-). The description must be 2 to 256 characters in length and cannot start with http:// and https://.
6. Click OK.

### 5.6 Attach a disk

You can attach a disk that is created separately to an ECS instance as a data disk. The disk and the instance must be in the same region and the same zone. Prerequisites The disk is in the Pending state. Context You do not need to attach data disks that are created at the same time as an instance. A disk can only be attached to an instance that is in the same zone and region as the disk. You can attach a disk to a single ECS instance at a time. A Shared Block Storage device can be attached to a maximum of four ECS instances at the same time. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk and choose More > At t ach from the Act ions column.
5. Specify the destination instance and configure the release mode as needed.
If you select Release Disk wit h Inst ance, the disk is released together when the instance it is attached to is deleted. If you do not select Release Disk wit h Inst ance, the disk changes to the Pending state when the instance it is attached to is deleted.
6. Click OK.

### 5.7 Partition and format disks

#### 5.7.1 Format a data disk for a Linux instance

Data disks created separately are not partitioned or formatted. This topic describes how to partition and format a data disk of a Linux instance. Prerequisites The disk has been attached to the instance. Procedure
1. Connect to the instance.
2. Run the f disk -l command to view all data disks attached to the ECS instance.
If /dev/vdb is not displayed in the command output, the ECS instance does not have a data disk. Check whether the data disk is attached to the instance.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00000000
```

3. Create partitions for the data disk.
i. Run the f disk /dev/sdb command. ii. Enter n to create a new partition. iii. Enter p to set the partition as the primary partition. iv. Enter a partition number and press the Enter key. In this example, 1 is entered to create Partition 1. v. Enter the number of the first available sector. This example uses the default value. This is done by pressing the Enter key. You can also enter a value from 1 to 41610 and press the Enter key. vi. Enter the number of the last sector. This example uses the default value. This is done by pressing the Enter key. You can also enter a value from 1 to 11748 and press the Enter key. vii. (Optional)Optional. To create multiple partitions, repeat steps b through f until all four primary partitions are created. viii. Run the wq command to start partitioning.

```
[root@iZ********eZ ~]# fdisk /dev/vdb Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel Building a new DOS disklabel with disk identifier 0x01ac58fe. Changes will remain in memory only, until you decide to write them. After that, of course, the previous content won't be recoverable. Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite) WARNING: DOS-compatible mode is deprecated. It's strongly recommended to
         switch off the mode (command 'c') and change display units to
         sectors (command 'u').
Command (m for help): n Command action
   e   extended
   p   primary partition (1-4)
```

`p`

```
Partition number (1-4): 1 First cylinder (1-41610, default 1): Using default value 1 Last cylinder, +cylinders or +size{K,M,G} (1-41610, default 41610): Using default value 41610 Command (m for help): wq The partition table has been altered!
```

4. Run the f disk -l command to view the partitions.
If /dev/vdb1 is displayed in the command output, new partition vdb1 is created.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x01ac58fe Device Boot Start End Blocks Id System /dev/vdb1 1 41610 20971408+ 83 Linux
```

5. Format the new partition. In this example, the new partition is formatted as ext3 after you run the
mkf s.ext 3 /dev/vdb1 command. The time required for formatting depends on the disk size. You can also format the new partition to another file system. For example, you can run the mkf s.ext 4 /dev/vdb1 command to format the partition as ext4. Compared with ext2, ext3 only adds the log function. Compared with ext3, ext4 improves on some important data structures. ext4 provides better performance and reliability, and more functions.

```
[root@iZ********leZ ~]# mkfs.ext3 /dev/vdb1 mke2fs 1.41.12 (17-May-2010) Filesystem label= OS type: Linux Block size=4096 (log=2) Fragment size=4096 (log=2) Stride=0 blocks, Stripe width=0 blocks 1310720 inodes, 5242852 blocks 262142 blocks (5.00%) reserved for the super user First data block=0 Maximum filesystem blocks=4294967296 160 block groups 32768 blocks per group, 32768 fragments per group 8192 inodes per group Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
    4096000
Writing inode tables: done Creating journal (32768 blocks): done Writing superblocks and filesystem accounting information: done This filesystem will be automatically checked every 25 mounts or 180 days, whichever comes first. Use tune2fs -c or -i to override.
```

6. Run the `echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab` command to write the
information of the new partition to the /etc/fstab file. You can run the `cat /etc/fstab` command to view the new partition information. Ubuntu 12.04 does not support barriers. To write the information of the new partition into the /etc/fstab file, you must run the `echo '/dev/vdb1 /mnt ext3 barrier=0 0 0' >> /etc/fstab` command. In this example, the partition information is added to the ext3 file system. You can also modify the ext3 parameter to add the partition information to another type of file system. To attach the data disk to a specific folder, for example, to store web pages, modify the /mnt part of the preceding command.

```
[root@iZ********eZ ~]# echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab [root@iZbp19cdhgdj0aw5r2izleZ ~]# cat /etc/fstab
```

`#`

```bash
# /etc/fstab
# Created by anaconda on Thu Aug 14 21:16:42 2014
```

`#`

```bash
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
```

`#`

```
UUID=94e4e384-0ace-437f-bc96-057dd64f**** / ext4 defaults,barrier=0 1 1 tmpfs /dev/shm tmpfs defaults 0 0 devpts /dev/pts devpts gid=5,mode=620 0 0 sysfs /sys sysfs defaults 0 0 proc /proc proc defaults 0 0 /dev/vdb1 /mnt ext3 defaults 0 0
```

7. Mount the new partitions. Run the mount -a command to mount all the partitions listed in /etc/fs
tab and run the df -h command to view the result. If the following information is displayed, the new partitions are mounted and available for use.

```
[root@iZ********eZ ~]# mount -a [root@iZ********eZ ~]# df -h Filesystem Size Used Avail Use% Mounted on /dev/vda1 40G 5.6G 32G 15% / tmpfs 499M 0 499M 0% /dev/shm /dev/vdb1 20G 173M 19G 1% /mnt
```

#### 5.7.2 Format a data disk of a Windows instance

Data disks created separately are not partitioned or formatted. This topic describes how to partition and format a data disk of a Windows instance. This example uses Windows Server 2008. Prerequisites The disk has been attached to an instance. Procedure
1. In the lower-left corner of the screen, click the Server Manager icon.
2. In the left-side navigation pane of the Server Manager window, choose St orage > Disk
Management .
3. Right-click an empty partition and select New Simple Volume from the shortcut menu.
If the disk status is Of f line, change it to Online.
4. Click Next .
5. Set the size of the simple volume, which is the partition size. Then click Next .
The default value is the maximum value of the disk space. You can specify the partition size as needed.
6. Specify the drive letter and then click Next .
7. Specify the formatting options and then click Next .
We recommend that you format the partition with the default settings provided by the wizard.
8. When the wizard prompts that the partition has been completed, click Finish to close the wizard.

### 5.8 Expand a disk

You can expand system or data disks online. After a disk is expanded, you do not need to restart the instance to which the disk is attached for the new disk capacity to take effect. Prerequisites To avoid data loss, we recommend that you create a snapshot to back up disk data before you expand a disk. For more information, see Create a snapshot. No snapshot is being created for the disk to be expanded. The disk or the instance to which the disk is attached meets the following requirements: If the disk is a system disk, the instance is in the Running state. If the disk is a data disk, one of the following requirements is met: The disk is in the Pending state. If the disk is attached to an instance, the instance is in the Running state. If the disk is a Shared Block Storage device, it is in the Pending state. Context The following limits apply when you expand a disk.

| Limit | Description |
|---|---|
| Disk category | Ultra disks and standard SSDs can be expanded. Shared SSDs and shared ultra disks can be expanded. |
| Operating system | The system disks of Windows Server 2003 instances cannot be expanded. |
| Partitioning mode | You cannot expand a data disk that uses the MBR partitioning scheme to more than 2 TiB. To expand this kind of disk to more than 2 TiB, we recommend that you create and attach a new data disk with the desired size. Use the GPT partitioning scheme to partition the new data disk and then copy data from the original data disk to the new data disk. |
| File system | For Windows instances, you can expand only disks that use NTFS file systems. |
| Maximum capacity | Ultra disk and standard SSD: 32,768 GiB Shared SSD and shared ultra disk: 32,768 GiB |
| Operations | When you expand disks, only the capacity of the disks is expanded. The sizes of partitions and file systems do not change. You must manually re-allocate storage space on a disk after the disk is expanded. You cannot shrink an expanded disk by any means, such as by rolling it back. |

Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. Find the target disk and choose More > Expand Disk in the Act ions column.
4. In the Expand Disk dialog box that appears, specify a new capacity for the disk.
The new capacity must be greater than the current capacity.
5. Click OK.
Result When you expand disks, only the capacity of the disks is expanded. The sizes of partitions and file systems do not change. You must manually re-allocate storage space on a disk after the disk is expanded.

### 5.9 Reinitialize a disk

You can reinitialize a disk to restore it to its initial state. Prerequisites The disk is in the Running state. The instance is in the St opped state. After a disk is reinitialized, its data is lost and cannot be recovered. Exercise caution when you perform this operation. We recommend that you back up the data of the disk or create snapshots before you reinitialize the disk. For more information, see Create a snapshot. Context The result of disk reinitialization depends on the disk type and how the disk is created. System disk: The disk is restored to the initial state of the image used by the disk. If the original image is deleted, the disk cannot be reinitialized. Data disk: If the disk is empty when created, the disk is restored to an empty disk. If the disk is created from a snapshot, the disk is restored to a disk with only the data of the source snapshot. If the disk is created from a snapshot and the snapshot is deleted, the disk cannot be reinitialized. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk and click Reinit ialize in the Act ions column.
5. Perform the following operations based on the disk type.
For a system disk, enter and confirm a new logon password, select the Start Instance After Reinitializing Disk option as needed, and then click OK. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ' ~ ! @ # $ % ^ & * - _ + = | { } [ ] : ; ' <

```
> , . ? /
```

For a data disk, click OK. Result When the disk is being reinitialized, the disk enters the Init ializing state. After the reinitialization, it changes to the Running state.

### 5.10 Detach a data disk

You can detach a data disk, not a system disk. Prerequisites For a Windows instance, you must bring the data disk offline in Disk Management. Not e To guarantee data integrity, we recommend that you stop read/write operations on the data disk when you detach the disk. Otherwise, data may be lost. For a Linux instance, you must connect to the instance and unmount the partitions on the disk. Not e If you have configured the /etc/fstab file to automatically mount the disk partitions upon instance startup, you must delete the mounting information from the /etc/fstab file before you detach the disk. Otherwise, you cannot connect to the instance after the instance is restarted. The data disk to be detached is in the Running state. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk and choose More > Det ach from the Act ions column.
5. Click OK.

### 5.11 Release a data disk

You can release a data disk that is no longer needed. The released data disk cannot be recovered. Exercise caution when you release a data disk. Prerequisites The data disk is in the Pending state. If the data disk is attached to an instance, detach the disk from the instance first. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk and choose More > Release from the Act ions column.
5. Click OK.

## 6 Images

### 6.1 Create a custom image

You can create a custom image and use it to create identical instances or replace the system disks of existing instances. This allows you to have multiple instances with the same operating system and data environment. Create a custom image from a snapshot You can create a custom image from a system disk snapshot to fully load the operating system and data environment of the snapshot to the image. Before you perform this operation, make sure that a snapshot of system disks is used. You cannot create a custom image from snapshots of data disks.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the snapshot and click Creat e Cust om Image in the Act ions column.
5. Enter the name and description of the image, and then click OK.
The name must be 2 to 128 characters in length and can contain periods (.), underscores (_), hyphens (-), and colons (:). It cannot start with a special character or digit. The description must be 2 to 256 characters in length and cannot start with http:// and https://. Create a custom image from an instance You can create a custom image from an instance to completely replicate the data of all disks of the instance, including the system disk and data disks. Not e To avoid data security risks, delete sensitive data before you create a custom image. When you create a custom image from an instance, a snapshot is generated for each disk in the instance, and all the snapshots constitute a complete custom image.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and choose More > Creat e Cust om Image from the Act ions column.
5. Enter the name and description of the custom image, and then click OK.
The name must be 2 to 128 characters in length and can contain periods (.), underscores (_), hyphens (-), and colons (:). It cannot start with a special character or digit. The description must be 2 to 256 characters in length and cannot start with http:// and https://.

### 6.2 View images

You can view the list of created images.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created images that match the specified criteria are displayed.
4. Select the tab based on the type of images you want to view.
You can select the Cust om Images or Public Images tab.
5. Select a filtering option from the drop-down list, enter the relevant information in the search bar,
and click Search. You can select multiple filtering options to narrow down the search results.

| Filtering option | Description |
|---|---|
| Image Name | Enter an image name to search for the image. |
| Image ID | Enter an image ID to search for the image. |
| Snapshot ID | Enter a snapshot ID to search for the images associated with the snapshot. This option is not available for public images. |

### 6.3 View instances related to an image

image You can view the instances that use the specified image. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a tab based on the type of the image.
You can select the Cust om Images or Public Images tab.
5. Find the target image and click Relat ed Inst ances in the Act ions column.
Result The Instances page appears, showing the instances that use the image. You can perform operations on these instances, such as updating the image.

### 6.4 Modify the description of a custom image

custom image You can modify the description of a created custom image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target custom image and click Modif y Descript ion in the Act ions column.
5. In the dialog box that appears, modify the image description in the Basic Settings field.
The description must be 2 to 256 characters in length and cannot start with http:// or https://.
6. Click OK.

### 6.5 Share custom images

You can share a custom image that you create to organizations that you manage to create multiple identical ECS instances in a short time. Context Only custom images can be shared. Shared images are not counted towards the image quota assigned to the organization. The organization can use the shared image to create instances or replace system disks of existing instances. You can delete shared images. After a shared image is deleted, the image is no longer visible to the organization to which the image was shared. The system disk of instances created from the shared image can no longer be reinitialized. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the image and click Share Image in the Act ions column.
5. Select the organization to which you want to share the image and click OK.
An image can be shared only to the organizations that the image owner manages.

### 6.6 Import custom images

#### 6.6.1 Limits on importing custom images

This topic describes the limits on importing images. You must understand the limits to ensure image availability and improve import efficiency. The following limits apply when you import custom images: Limits on importing custom images in Linux Limits on importing custom images in Windows Limits on importing custom images in Linux When you import custom images in Linux, note the following limits: Multiple network interfaces are not supported. IPv6 addresses are not supported. The password must be 8 to 30 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The firewall is disabled, and port 22 is opened. The Linux system disk size ranges from 40 GiB to 500 GiB. DHCP must be enabled in the image. SELinux is disabled. The Kernel-based Virtual Machine (KVM) driver must be installed. We recommend that you install cloud-init to configure the hostname and NTP and yum sources. Limits

| Item | Standard operating system image | Non-standard operating system image |
|---|---|---|
| Description | The supported standard 32-bit and 64-bit operating systems include: CentOS Ubuntu SUSE openSUSE Red Hat Debian CoreOS Aliyun Linux Not e Support for standard operating systems may be subject to version changes. You can access the ECS console to check the latest supported operating systems. | Non-standard operating systems include: Operating systems that are not supported by Alibaba Cloud. Standard operating systems that do not meet the requirements of critical system configuration files, basic system environments, and applications. If you want to use non-standard operating system images, you must select Others Linux when importing images. If you import non-standard operating system images, Alibaba Cloud does perform any processing on the instances created from these images. After you create an instance, you must connect to the instance by clicking Connect to VPN in the ECS console. You can then configure the IP address, route, and password for the instance. |

| Item | Standard operating system image | Non-standard operating system image |
|---|---|---|
| Critical system configuration files | Do not modify /etc/issue* . Otherwise, the version of the operating system cannot be identified, which leads to system creation failure. Do not modify /boot/grub/men u.lst . Otherwise, the system may fail to start. Do not modify /etc/fstab . Otherwise, partitions cannot be loaded, which leads to system startup failure. Do not modify /etc/shadow to read-only. Otherwise, the password file cannot be modified, which leads to system creation failure. Do not modify /etc/selinux/c onfig to enable SELinux. Otherwise, the system may fail to start. | Requirements for standard operating system images are not met. |
| Requirements for the basic system environment | Do not adjust the system disk partitions. Only disks with a single root partition are supported. Make sure that the system disk has sufficient storage space. Do not modify critical system files, such as /sbin , /bin , and /lib* . Before importing an image, confirm the integrity of the file system. Only ext3 and ext4 file systems are supported. |   |
| Applications | Do not install qemu-ga on a custom image. Otherwise, some of the services that Alibaba Cloud needs may be unavailable. |   |

| /boot/grub/men |   |
|---|---|

|   | u.lst |
|---|---|

| /etc/selinux/c |   |
|---|---|

|   | onfig |
|---|---|

|   | /sbin |
|---|---|
| /lib* |   |

| User Guide·Images |   |   |
|---|---|---|
| Item | Standard operating system image | Non-standard operating system image |
| Image file formats | Only images in the RAW, VHD, or qcow2 format can be imported. If you want to import images in other formats, use a tool to convert the format before importing the image. We recommend that you import images in the VHD format, which has a smaller transmission footprint. |   |
| Image file size | We recommend that you configure the disk size for importing images based on the virtual disk size (not the image file size). The disk size for importing images must be at least 40 GiB. |   |

Limits on importing custom images in Windows When you import custom images in Windows, note the following limits: The password must be 8 to 30 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Imported Windows images do not provide the Windows activation service. The firewall must be disabled. Otherwise, remote logon is unavailable. Port 3389 must be opened. The Windows system disk size ranges from 40 GiB to 500 GiB. Limits

| Item | Description |
|---|---|

| Item | Description |
|---|---|
| Operating system versions | Alibaba Cloud supports importing the following versions of 32- bit and 64-bit operating system images: Microsoft Windows Server 2016 Microsoft Windows Server 2012, including: Microsoft Windows Server 2012 R2 (Standard Edition) Microsoft Windows Server 2012 (Standard Edition and Datacenter Edition) Microsoft Windows Server 2008, including: Microsoft Windows Server 2008 R2 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2008 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2003, including: Microsoft Windows Server 2003 R2 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2003 (Standard Edition, Datacenter Edition, and Enterprise Edition) or later, including Service Pack 1 (SP1) Microsoft Windows 7, including: Microsoft Windows 7 (Professional Edition) Microsoft Windows 7 (Enterprise Edition) Not e Support for standard operating systems may be subject to version changes. You can access the ECS console to check the latest supported operating systems. |
| Requirements for the basic system environment | Multi-partition system disks are supported. Make sure that the system disk has sufficient storage space. Do not modify critical system files. Before importing an image, confirm the integrity of the file system. The NTFS file system with the MBR partition type is supported. |
| Applications | Do not install qemu-ga on an imported image. If it is installed, some of the services that Alibaba Cloud needs may be unavailable. |

| Item | Description |
|---|---|
| Image file formats | RAW VHD qcow2 We recommend that you configure the system disk size for importing images based on the virtual disk size (not the image file size). The system disk size for importing images must range from 40 GiB to 500 GiB. Not e We recommend that you import images in the VHD format, which has a smaller transmission footprint. |

#### 6.6.2 Convert the image file format

You can only import image files in the RAW, VHD, and qcow2 formats to ECS. If you want to import images in other formats, you must convert the image into a supported format. This topic describes how to convert the image format in Windows and Linux. Context You can use the qemu-img tool to convert an image from VMDK, VDI, VHDX, qcow1, or QED to RAW, VHD, or qcow2, or implement conversion between RAW, VHD, and qcow2. Not e We recommend that you use the qcow2 format if your application environment supports this format. Windows
1. Download qemu.
Visit QEMU Binaries for Windows (64 bit) to download the qemu tool. Select a qemu version based on your operating system.
2. Install qemu.
The installation path in this example is C:\Program Files\qemu.
3. Configure the environment variables for qemu.
i. Choose St art > Comput er, right-click Computer, and choose Propert ies from the shortcut menu. ii. In the left-side navigation pane, click Advanced Syst em Set t ings. iii. In the Syst em Propert ies dialog box that appears, click the Advanced tab and then click Environment Variables. iv. In the Environment Variables dialog box that appears, find the Pat h variable from the Syst em variables section. If the Pat h variable exists, click Edit . If the Pat h variable does not exist, click New. v. Add a system variable value. In the Edit System Variable dialog box that appears, add C:\Program Files\qemu to the Variable value field, separate different variable values with semicolons (;), and then click OK. In the New System Variable dialog box that appears, enter Path in the Variable name field, enter C:\Program Files\qemu in the Variable value field, and then click OK.
4. Open Command Prompt in Windows and run the `qemu-img --help` command. If a successful
response is displayed, the tool is installed.
5. In the Command Prompt window, run the `cd [Directory of the source image file]` command
to switch to a new file directory, for example, cd D:\ConvertImage .
6. In the Command Prompt window, run the `qemu-img convert -f raw -O qcow2 centos.raw centos.`
`qcow2` command to convert the image file format. The parameters are described as follows: The `-f` parameter is followed by the source image format. The `-O` parameter (case-sensitive) is followed by the destination image format, source file name, and destination file name. After the conversion is complete, the destination file appears in the directory of the source image file. Linux
1. Install the qemu-img tool.
For Ubuntu, run the `apt install qemu-img` command. For CentOS, run the `yum install qemu-img` command. Run the `qemu-img convert -f raw -O qcow2 centos.raw centos.qcow2` command to convert the image file format. The parameters are described as follows: The `-f` parameter is followed by the source image format. The `-O` parameter (case-sensitive) is followed by the destination image format, source file name, and destination file name.

#### 6.6.3 Import a custom image

After you upload a local image to an OSS bucket, you can import the image to the ECS environment as a custom image. Prerequisites An image that meets the limits and requirements for image import has been made. The image must be in the RAW, VHD, or qcow2 format. For more information, see Limits on importing custom images and Convert the image file format. You have been authorized to import images. For more information, see the RAM authorization section in ASCM Console User Guide. A local image has been uploaded to a bucket by using the OSS console or calling an OSS API operation. For more information, see the Upload objects section in OSS User Guide or the PutObject s ection in OSS Developer Guide. Not e Make sure that the bucket is in the same region as the custom image you want to create. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Import Image.
5. Configure the parameters of the image.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | The region of the custom image to be imported. |
| Organization | Yes | The organization to which the custom image belongs. |
| Resource Set | Yes | The resource set of the custom image. |
| OSS Bucket Name | Yes | The name of the OSS bucket where the image to be imported resides. |
| OSS Object Name | Yes | The endpoint of the OSS object where the image is stored. For information about how to obtain the endpoint of an OSS object, see the Obtain object URLs section in OSS User Guide. |
| Image Name | Yes | The name of the custom image. The name must be 2 to 128 characters in length. It must start with a letter and can contain letters, periods (.), underscores ( ), and hyphens (-). _ |
| Operating System | Yes | Linux and Windows are available. |
| System Disk | Yes | The size of the system disk of the ECS instance. Unit: GiB. |
| System Architecture | Yes | x86 64 and i386 are available. _ |

| Parameter | Required | Description |
|---|---|---|
| Platform | Yes | Linux: Cent OS Ubunt u SUSE OpenSUSE Debian CoreOS Aliyun Ot hers Linux Cust omized Linux Windows: Windows Server 2003 Windows Server 2008 Windows Server 2012 |
| Image Format | Yes | The format of the custom image. RAW, VHD, and qcow2 are available. |
| Description | No | The description of the custom image. |

6. Click OK.
Result You can go to the Images page to view the progress of custom image creation. For more information, see View images. When 100% is displayed in the Progress column of the Images page, the image is created.

### 6.7 Export a custom image

You can export a custom image to an OSS bucket and then download it to your local device. Prerequisites OSS is activated and an OSS bucket is created. For more information, see the "Create buckets" section in OSS User Guide. You are authorized to export images. For more information, see the "RAM" chapter in ASCM Console User Guide. Context You can export custom images to the RAW, VHD, or qcow2 format. After a custom image is exported to an OSS bucket, you can download the image to your local device. For more information, see the "Obtain object URLs" section in OSS User Guide.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target custom image and click Export Image in the Act ions column.
5. Select a bucket for OssBucket . Enter a prefix in the OSS Pref ix field. Then click OK.
The OSS Pref ix field is optional. The prefix must be 1 to 30 characters in length and can contain digits and letters.

### 6.8 Delete a custom image

You can delete a custom image that is no longer needed. However, public images cannot be deleted. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select one of the following methods to delete custom images.
To delete one image, find the image and click Delet e Image in the Act ions column. To delete multiple images, select images and click Delet e at the bottom of the image list.
5. Click OK.

## 7 Snapshots

### 7.1 Create a snapshot

You can manually create a snapshot for a disk to back up disk data. Prerequisites The instance to which the disk is attached is in the Running or St opped state. The disk is in the Running state. Context You can create up to 64 snapshots for each disk. Snapshots can be used in the following scenarios: Restore a disk from one of its snapshots. Create a custom image from a system disk snapshot. For more information, see Create a custom image from a snapshot. Data disk snapshots cannot be used to create custom images. Create a new data disk from a data disk snapshot. To create a data disk from a snapshot, set Use Snapshot to Yes and specify a snapshot on the Create Disk page. For more information, see Create a disk. When you re-initialize a data disk created from a snapshot, the disk is restored to the status of the snapshot. Note the following considerations when you create a snapshot: For each disk, the first snapshot is a full snapshot and subsequent snapshots are incremental snapshots. It takes an extended period of time to create the first snapshot. It takes a short period of time to create an incremental snapshot. The amount of taken time depends on the volume of data that has been changed since the last snapshot. The more data that has been changed, the more time it takes. Avoid creating snapshots during peak hours. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target disk and click Creat e Snapshot in the Act ions column.
5. Enter a snapshot name and description and then click OK.
Not e The names of manual snapshots cannot start with auto because auto is a prefix reserved for automatic snapshots. You can go to the Snapshots page to check the progress of snapshot creation. For more information, see View snapshots. When 100% is displayed in the Progress column, the snapshot is created.

### 7.2 View snapshots

You can view the list of created snapshots. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created snapshots that match the specified criteria are displayed.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Snapshot Name | Enter a snapshot name to search for the snapshot. |
| Snapshot ID | Enter a snapshot ID to search for the snapshot. |
| Instance ID | Enter an instance ID to search for the snapshots related to the instance. |
| Disk ID | Enter a disk ID to search for the snapshots related to the disk. |
| Snapshot Type | Select a snapshot type to search for the snapshots of that type. Valid values: All User Snapshot s: manual snapshots Aut omat ic Snapshot s: automatic snapshots |
| Creation Time | Enter a time to search for the snapshots that were created at that time. |

### 7.3 Delete a snapshot

You can delete a snapshot that is no longer needed. After the snapshot is deleted, it cannot be recovered. You cannot delete system disk snapshots that have been used to create custom images. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete the snapshot:
To delete a single snapshot, find the snapshot and click Delet e in the Act ions column. To delete one or more snapshots at a time, select the snapshots and click Delet e in the lowerleft corner of the Snapshots page.
5. In the message that appears, click OK.
cies

## 8 Automatic snapshot policies

### 8.1 Create an automatic snapshot policy

policy Automatic snapshot policies can apply to both system disks and data disks and can be used to create periodical snapshots for the disks. Using automatic snapshot policies can improve data availability and operation error tolerance. Context Automatic snapshot policies can effectively eliminate the following risks associated with manual snapshot creation: When applications such as personal websites or databases deployed on an ECS instance encounter attacks or system vulnerabilities, you may not be able to manually create snapshots. In this case, you can use the latest automatic snapshot to roll back the affected disks to restore your data and reduce losses. You can also specify an automatic snapshot policy to create snapshots before regular system maintenance tasks. This eliminates the need to manually create snapshots and ensures that snapshots are always created before maintenance. You can create up to 64 snapshots for each disk. If the maximum number of snapshots for a disk is reached when a new snapshot is being created, the system deletes the oldest automatic snapshot. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot
Policies.
3. Click Creat e Policy.
4. Configure the properties of the automatic snapshot policy.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | The ID of the region to which the automatic snapshot policy applies. |
| Organization | Yes | The organization to which the automatic snapshot policy applies. |
| Policy Name | Yes | The name of the automatic snapshot policy. The name must be 2 to 128 characters in length and cannot start with a special character or digit. It can contain periods (.), underscores ( ), hyphens (-), and _ colons (:). |

cies

| Parameter | Required | Description |
|---|---|---|
| Creation Time | Yes | The time when a snapshot is automatically created. You can select any hour from 00:00 to 23:00. Not e The default time zone for the snapshot policy is UTC+8. You can change the time zone based on your business requirements. The creation of an automatic snapshot is canceled if the scheduled time for creating the snapshot is reached but the previous automatic snapshot is still being created. This may occur if the disk stores a large volume of data. For example, you can specify a policy for the system to create automatic snapshots at the following points in time: 00:00, 01:00, and 02:00. When the system starts creating a snapshot at 00:00, it takes 70 minutes for the system to complete the snapshot task. Therefore, the system does not create another snapshot at 01:00. Instead, after the system completes the snapshot task at 01:10, the system creates the next snapshot at 02:00. |
| Frequency | Yes | The day when a snapshot is created. You can select multiple values. The day ranges from Monday to Sunday. |
| Retention Policy | No | The retention policy of the automatic snapshot. The default value of the retention time is 30 days. You can configure the following parameters: Keep f or: Specify the number of days during which the snapshots can be retained. Valid values: 1 to 65536. Always keep t he snapshot s unt il t he number of snapshot s reaches t he upper limit : Select this option to retain the snapshots until the maximum number of snapshots is reached. |

5. Click OK.
What's next After the automatic snapshot policy is created, you need to apply it to a disk to automatically create snapshots for the disk. For more information, see Configure an automatic snapshot policy for multiple disks. cies

### 8.2 View automatic snapshot policies

You can view the list of automatic snapshot policies. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot
Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created automatic snapshot policies that match the specified criteria are displayed.
4. View the list of automatic snapshot policies.

### 8.3 Modify an automatic snapshot policy

policy You can modify the properties of an automatic snapshot policy, such as the name, creation time, frequency, and retention policy. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot
Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy and click Modif y Policy in the Act ions column.
5. Modify the properties of the policy.
Changes made to the retention duration do not take effect on existing snapshots, but take effect only on newly created snapshots.
6. Click OK.

### 8.4 Configure an automatic snapshot policy

policy After you apply an automatic snapshot policy to a disk, snapshots will be created automatically for the disk based on the policy settings. You can cancel an applied automatic snapshot policy at any time. Context We recommend that you configure the automatic snapshot policy to create automatic snapshots during off-peak hours. You can also manually create a snapshot for the disk that already has an automatic snapshot policy applied. When an automatic snapshot is being created, you must wait until the snapshot is complete before you can create a manual snapshot. The automatic snapshot is named in the following format: auto_yyyyMMdd_1, such as auto_20140418_1. cies
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk and click Conf igure Aut omat ic Snapshot Policy in the Act ions column.
5. Select a procedure based on the operation you want to perform on the policy.
To apply an automatic snapshot policy, turn on Aut omat ic Snapshot Policy, select a policy, and then click OK. To cancel an automatic snapshot policy, turn off Aut omat ic Snapshot Policy and click OK.

### 8.5 Configure an automatic snapshot policy for multiple disks

policy for multiple disks After you apply an automatic snapshot policy to a disk, snapshots will be created automatically for the disk based on the policy settings. You can cancel an applied automatic snapshot policy at any time. Context We recommend that you configure the automatic snapshot policy to create automatic snapshots during off-peak hours. You can also manually create a snapshot for the disk that already has an automatic snapshot policy applied. When an automatic snapshot is being created, you must wait until the snapshot is complete before you can create a manual snapshot. The automatic snapshot is named in the following format: auto_yyyyMMdd_1, such as auto_20140418_1. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot
Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy and click Apply Policy in the Act ions column.
5. Select a tab based on the operation you want to perform on the disks.
To apply the automatic snapshot policy, click the Disks Wit hout Policy Applied tab, select one or more disks, and click Apply Policy at the bottom of the disk list. To cancel the automatic snapshot policy, click the Disks Wit h Policy Applied tab, select one or more disks, and click Disable Aut omat ic Snapshot Policy at the bottom of the disk list.

### 8.6 Delete an automatic snapshot policy

policy You can delete an automatic snapshot policy that is no longer needed. After you delete the automatic snapshot policy, the policy is automatically canceled for disks that have it applied.
1. Log on to the ECS console.
cies
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot
Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy and click Delet e Policy in the Act ions column.
5. In the message that appears, click OK.

## 9 Security groups

### 9.1 Create a security group

Security groups are an important means for network security isolation. They are used to set network access control for one or more ECS instances. Prerequisites A Virtual Private Cloud (VPC) has been created. For more information, see VPC User Guide . Context Instances that belong to the same account and are in the same region and in the same security group can communicate with each other over the internal network. If instances that belong to the same account in the same region are in different security groups, you can implement internal network communication by authorizing mutual access between two security groups. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click New Securit y Group.
5. Configure the parameters of the security group.

| Type | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | The organization to which the security group belongs. Make sure that the security group and the VPC belong to the same organization. |
|   | Resource Set | Yes | The resource set to which the security group belongs. Make sure that the security group and the VPC belong to the same resource set. |
|   | Region | Yes | The region to which the security group belongs. Make sure that the security group and the VPC belong to the same region. |
| ument Version: 20220928 | 10 |   |   |

|   | Elastic Compute Servic |   |   |
|---|---|---|---|
| Type | Parameter | Required | Description |
|   | Zone | Yes | The ID of the zone where the security group resides. |
|   | VPC | Yes | The VPC to which the security group belongs. |
|   | Security Group Name | No | The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). It cannot start with http:// or https://. |
| Basic Settings |   |   |   |
|   | Description | No | The description of the security group. We recommend that you provide an informational description to simplify future management operations. The name must be 2 to 256 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), and commas (,). It cannot start with http:// or https://. |

6. Click Submit .

### 9.2 View security groups

You can view the list of security groups that you create. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created security groups that match the specified criteria are displayed.
4. Select a filtering option from the drop-down list, enter the relevant information in the search bar,
and click Search. You can select multiple filtering options to narrow down the search results.

| Filtering option | Description |
|---|---|
| Security Group ID | Enter a security group ID to search for the security group. |
| Security Group Name | Enter a security group name to search for the security group. |
| VPC ID | Enter a VPC ID to search for the security groups that belong to the VPC. |

### 9.3 Modify a security group

You can modify the name and description of a created security group. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group and click Modif y in the Act ions column.
5. Modify the name and description of the security group.
6. Click OK.

### 9.4 Add a security group rule

You can use security group rules to control access to and from the ECS instances in a security group over the Internet and the internal network. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. Click Creat e Rule.
6. Configure parameters listed in the following table to create a security group rule.

| Parameter | Required | Description |
|---|---|---|
| ENI Type | Yes | Valid value: Int ernal Net work ENI. In VPCs, you cannot find public NICs in ECS instances and can add only internal security group rules. However, the added security group rules apply to both the Internet and internal network. |

| Parameter | Required | Description |
|---|---|---|
| Direction | Yes | Out bound: access from the ECS instances in the current security group to other ECS instances on the internal network or resources on the Internet. Inbound: access from other ECS instances on the internal network or resources on the Internet to the ECS instances in the current security group. |
| Action | Yes | Allow: allows access requests on the specified port or ports. Deny: discards data packets and returns no messages. If two security group rules are different only in the Action parameter, the Deny rule takes effect while the Allow rule is ignored. |
| Protocol | Yes | All: all protocols. This value can be used in total trust scenarios. T CP: can be used to allow or deny traffic on one or several successive ports. UDP: can be used to allow or deny traffic on one or several successive ports. ICMP: can be used when the ping command is used to test the status of the network connection between instances. ICMPv6: can be used when the ping6 command is used to test the status of the network connection between instances. GRE: can be used for VPN. |
| Port Range | Yes | The port range depends on the protocol type. When you set Protocol to All, -1/-1 is displayed, indicating all ports. You cannot specify a port range in this case. When you set Protocol to T CP, you can use the <start port number>/<end port number> format to specify a port range. Valid port numbers: 1 to 65535. Set the start port number and end port number to the same value to specify a single port. For example, use 22/22 to specify port 22. When you set Protocol to UDP, you can use the <start port number>/<end port number> format to specify a port range. Valid port numbers: 1 to 65535. Set the start port number and end port number to the same value to specify a single port. For example, use 3389/3389 to specify port 3389. When you set Protocol to ICMP, -1/-1 is displayed, indicating all ports. You cannot specify a port range in this case. When you set Protocol to ICMPv6, -1/-1 is displayed, indicating all ports. You cannot specify a port range in this case. When you set Protocol to GRE, -1/-1 is displayed, indicating all ports. You cannot specify a port range in this case. |

| Parameter | Required | Description |
|---|---|---|
| Priority | Yes | The priority of the rule. Valid values: 1 to 100. The default value is 1, indicating the highest priority. |
| Authorization Type | Yes | IPv4 Addresses: IPv4 addresses or IPv4 CIDR blocks. IPv6 Addresses: IPv6 addresses or IPv6 CIDR blocks. Securit y Groups: another security group. This authorization type takes effect only on the internal network. |
| Authorization Object | Yes | Authorization objects depend on the authorization type. When you set Authorization Type to IPv4 Addresses: Enter an IPv4 address or IPv4 CIDR block. Example: 12.1.1.1 or 13.1 .1.1/25. You can enter up to 10 authorization objects at a time. Separate multiple objects with commas (,). If you specify 0.0.0.0/0, all IPv4 addresses will be allowed or denied based on the Action parameter. Exercise caution when you specify 0.0.0.0/0. When you set Authorization Type to IPv6 Addresses: Enter an IPv6 address or IPv6 CIDR block. Example: 2001:0db8::14 28:**** or 2001:0db8::1428:****/128. You can enter up to 10 authorization objects at a time. Separate multiple objects with commas (,). If you specify ::/0, all IPv6 addresses will be allowed or denied based on the Action parameter. Exercise caution when you specify ::/0. When you set Authorization Type to Securit y Groups, select a security group ID. If the current security group is of the VPC type, the selected security group must be in the same VPC as the current security group. |
| Description | No | The description of the security group rule. We recommend that you provide an informational description to simplify future management operations. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

7. Click OK.

### 9.5 Clone a security group rule

You can clone a security group rule to quickly create a similar rule. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Find the target security group rule and click Clone in the Act ions column.
7. In the Clone Securit y Group Rule dialog box, modify the attributes of the security group rule.
For more information about the attributes of security group rules, see Add a security group rule.
8. Click OK.

### 9.6 Modify a security group rule

You can modify improper rules in a security group to ensure the security of ECS instances in the security group. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Find the target security group rule and click Modif y in the Act ions column.
7. In the Modif y Securit y Group Rule dialog box, modify the attributes of the security group rule.
For more information about the attributes of security group rules, see Add a security group rule.
8. Click OK.

### 9.7 Export security group rules

You can export security group rules of a security group to a local device for backup. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Click Export in the upper-right corner to download and save the rules to a local device.

### 9.8 Import security group rules

You can import a local backup file of security group rules into a security group to quickly create or restore security group rules.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Click Import in the upper-right corner.
7. In the Import Rule dialog box, click Choose File.
8. Select the target local backup file of security group rules and click Open. Then, click OK.
The local backup file must be in the CSV format. You can download a template file from the Import Rule dialog box.

### 9.9 Add an instance

You can add an existing instance to a security group in the same region. After the instance is added, the security group rules of the security group automatically apply to the instance. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group and click Manage Inst ances in the Act ions column.
5. Click Add Inst ance.
6. Select an instance and click OK.

### 9.10 Remove instances from a security group

security group You can remove instances from a security group, but each of the instances must always belong to at least one security group. Prerequisites The instances to be removed are added to two or more security groups. Context After an ECS instance is removed from a security group, the instance will be isolated from the other ECS instances in the security group. We recommend that you perform a full test in advance to ensure that services can run properly after you remove the instance. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Manage Inst ances in the Act ions column.
5. On the Instances page that appears, select one or more instances and click Remove in the lower-
left corner.
6. Click OK.

### 9.11 Delete a security group

You can delete a security group that is no longer needed. Prerequisites No instances exist in the security group. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete the security group:
To delete a single security group, find the security group and click Delet e in the Act ions column. To delete one or more security groups at a time, select the security groups and click Delet e in the lower-left corner of the Security Groups page.
5. In the message that appears, click OK.
es

## 10 Elastic Network Interfaces

### 10.1 Create an ENI

You can bind elastic network interfaces (ENIs) to instances to create high-availability clusters and implement fine-grained network management. You can also unbind an ENI from an instance and then bind the ENI to another instance to implement a low-cost failover solution. Prerequisites A virtual private cloud (VPC) and a VSwitch are created. For more information, see Create a VPC and Create a VSwitch in Apsara Stack VPC User Guide . A security group is available in the VPC. If no security group is available in the VPC, create a security group. For more information, see Create a security group. Context ENIs are classified into primary and secondary ENIs. A primary ENI is created by default when an instance is created in a VPC. This primary ENI has the same lifecycle as the instance and cannot be unbound from the instance. ENIs created separately are secondary ENIs. You can bind secondary ENIs to or unbind them from instances. This topic describes how to create a secondary ENI. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e ENI.
5. Configure parameters listed in the following table to create an ENI.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | The organization in which to create the ENI. |
|   | Resource Set | Yes | The resource set in which to create the ENI. |
|   | Region | Yes | The region in which to create the ENI. |
|   | Zone | Yes | The zone in which to create the ENI. |

|   | rfac Elastic Compute Servic |   |   |
|---|---|---|---|
| Section | Parameter | Required | Description |
|   | VPC | Yes | The VPC in which to create the ENI. The secondary ENI can be bound only to an instance in the same VPC. Not e After the ENI is created, you cannot change its VPC. |
| Basic Settings |   |   |   |
|   | VSwitch | Yes | The VSwitch to be associated with the ENI. The secondary ENI can be bound only to an instance in the same VPC. Select a VSwitch that is in the same zone as the instance to which the ENI will be bound. The VSwitch of the ENI can be different from that of the instance. Not e After an ENI is created, you cannot change its VSwitch. |
|   | Security Group | Yes | The security group in which to create the ENI within the specified VPC. The rules of the security group automatically apply to the ENI. |

es es

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | ENI Name | Yes | The name of the ENI. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |
|   | Description | No | The description of the ENI. We recommend that you provide an informational description to simplify future management operations. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |
|   | Primary Private IP | No | The primary private IPv4 address of the ENI. The IPv4 address must be within the CIDR block of the specified VSwitch. If you do not specify a primary private IP address, the system automatically assigns a private IP address to the ENI. |

6. Click Submit .
Result The created ENI is displayed on the ENIs page and is in the Available state.

### 10.2 View ENIs

es You can view the list of created ENIs.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created ENIs that match the specified criteria are displayed.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| ENI Name | Enter an ENI name to search for the ENI. |
| ENI ID | Enter an ENI ID to search for the ENI. |
| VSwitch ID | Enter a VSwitch ID to search for the ENIs that are associated with the VSwitch. |
| Security Group ID | Enter a security group ID to search for the ENIs that belong to the security group. |
| Instance ID | Enter an instance ID to search for the ENIs that are bound to the instance. |

### 10.3 Modify a secondary ENI

You can modify the attributes of a secondary elastic network interface (ENI), including the name, security group, and description. Prerequisites The secondary ENI is in the Available state. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI and click Modif y in the Act ions column.
5. In the Modify ENI dialog box that appears, modify the name, security group, and description of the
ENI.
6. Click OK.

### 10.4 Bind a secondary ENI to an instance

instance es You can bind a secondary elastic network interface (ENI) to an instance. After the ENI is bound to the instance, the instance can process the traffic on the ENI. Prerequisites The secondary ENI is in the Available state. The instance to which you want to bind the secondary ENI is in the Running or St opped state. The instance and the secondary ENI belong to the same VPC. The VSwitch with which the secondary ENI is associated is in the same zone as the VSwitch to which the instance is connected. An ENI can be bound only to an instance in the same zone. The VSwitches of the ENI and of the instance can be different but must be in the same zone. Context The following limits apply when you bind an ENI to an instance: You can manually bind only secondary ENIs. Primary ENIs share the same lifecycle as instances and cannot be manually bound. An ENI can only be bound to a single ECS instance. However, an ECS instance can be bound with multiple ENIs. The maximum number of ENIs that can be bound to an instance depends on the instance type. For more information about the number of ENIs that can be bound to an instance of each instance type, see Instance families in ECS Product Introduction . Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target secondary ENI and click Bind in the Act ions column.
5. In the Bind dialog box that appears, select an instance and click OK.
Result In the St at us/Creat ion T ime column, the status of the secondary ENI changes to Bound.

### 10.5 Unbind a secondary ENI from an instance

instance You can unbind a secondary elastic network interface (ENI) from an instance. After the secondary ENI is unbound from the instance, the instance no longer processes the traffic on the ENI. Prerequisites The secondary ENI is in the Bound state. The instance is in the Running or St opped state. Context Only secondary ENIs can be unbound. Primary ENIs share the same lifecycle as instances and cannot be unbound. es
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI and click Unbind in the Act ions column.
5. Click OK.
Result In the St at us/Creat ion T ime column, the status of the secondary ENI changes to Available.

### 10.6 Delete a secondary ENI

You can delete a secondary elastic network interface (ENI) that is no longer needed. Prerequisites The secondary ENI is in the Available state. Context You can delete only secondary ENIs. Primary ENIs share the same lifecycle as instances and cannot be deleted. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI and click Delet e in the Act ions column.
5. Click OK.

## 11 Deployment sets

### 11.1 Create a deployment set

You can use a deployment set to distribute or aggregate instances involved in your business. You can select hosts, racks, or network switches to improve service availability or network performance based on your needs. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. Click Creat e Deployment Set .
4. Configure the parameters of the deployment set.

| Category | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | The organization to which the deployment set belongs. |
|   | Resource Set | Yes | The resource set to which the deployment set belongs. |
|   | Region | Yes | The region where the deployment set is located. |
|   | Zone | Yes | The zone where the deployment set is located. |
|   | Deployment Domain | Yes | This parameter setting determines the Deployment Target options. Valid values: Def ault : When Default is selected, the deployment target options are Host, Rack, and Network Switch. Swit ch: When Switch is selected, the deployment target options are Host and Rack. |
|   | Deployment Target | Yes | The basic unit that can be scheduled when you deploy instances. Host : Instances are distributed or aggregated at the host level. Rack: Instances are distributed or aggregated at the rack level. VSwit ch: Instances are distributed or aggregated at the VSwitch level. |

|   | t sets Elastic Compute Servic |   |   |
|---|---|---|---|
| Category | Parameter | Required | Description |
| Basic Settings | Deployment Policy | Yes | The dispersion policies are used to improve service availability to avoid business impact when a host, rack, or switch fails. The aggregation policies are used to improve network performance to minimize the access latency between instances. Options are: Loose Dispersion St rict Dispersion Loose Aggregat ion St rict Aggregat ion |
|   | Deployment Set Name | No | The name of the deployment set. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain digits, periods (.), underscores ( ), hyphens (-), colons (:), and _ commas (,). |
|   | Description | No | The description of the deployment set. We recommend that you provide an informational description to simplify future management operations. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |

5. Click Submit .

### 11.2 View deployment sets

You can view the list of created deployment sets. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
The created deployment sets that match the specified criteria are displayed.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
then click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Deployment Set Name | Enter a deployment set name to search for the deployment set. |

| c Compute Service | User Guide·Deployment set |
|---|---|

| Filter option | Description |
|---|---|
| Deployment Set ID | Enter a deployment set ID to search for the deployment set. |
| Resource Set | Enter a resource set name to search for the deployment sets that belong to the resource set. |

### 11.3 Modify a deployment set

You can modify the name and description of a deployment set. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the deployment set and click Modif y in the Act ions column.
5. In the Change Deployment Set dialog box, change the name of the deployment set.
6. Click OK.

### 11.4 Delete a deployment set

You can delete a deployment set that is no longer needed. Prerequisites No instances exist in the deployment set. Procedure
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the deployment set and click Delet e in the Act ions column.
5. Click OK.

## 12 Install FTP software

### 12.1 Overview

File Transfer Protocol (FTP) transfers files between a client and a server by establishing two TCP connections. One is the command link for transferring commands between a client and a server. The other is the data link used to upload or download data. Before uploading files to an instance, you must build an FTP site for the instance.

### 12.2 Install and configure vsftp in CentOS

CentOS This topic describes how to install and configure vsftp in CentOS to transfer files. Procedure
1. Install vsftp.

```bash
yum install vsftpd -y
```

2. Add an FTP account and a directory.
i. Check the location of the nologin file, which is usually under the /usr/sbin or /sbin directory. ii. Create an FTP account. Run the following commands to create the /alidata/www/wwwroot directory and specify this directory as the home directory of the account pwftp. You can also customize the account name and directory.

```
mkdir -p /alidata/www/wwwroot useradd -d /alidata/www/wwwroot -s /sbin/nologin pwftp
```

iii. Modify the account password.

```
passwd pwftp
```

iv. Modify the permissions on the specified directory.

```
chown -R pwftp.pwftp /alidata/www/wwwroot
```

3. Configure vsftp.
i. Open the vsftp configuration file.

```
vi /etc/vsftpd/vsftpd.conf
```

ii. Change the value of anonymous_enable from `YES` to `NO` . iii. Delete the comment delimiter ( `#` ) from the following configuration lines:

```
local_enable=YES
        write_enable=YES
        chroot_local_user=YES
```

iv. Press the Esc key to exit the edit mode, and enter `:wq` to save the modifications and exit.
4. Modify the shell configuration.
i. Open the shell configuration file.

```
vi /etc/shells
```

ii. If the file does not contain /usr/sbin/nologin or /sbin/nologin, add it to the file.
5. Start vsftp and perform a logon test.
i. Start vsftp.

```
service vsftpd start
```

ii. Use the account pwftp to perform an FTP logon test. This example uses the directory /alidata/www/wwwroot.

### 12.3 Install vsftp in Ubuntu or Debian

This topic describes how to install and configure vsftp in an instance running Ubuntu or Debian to transfer files. Procedure
1. Update the software source.

```
apt-get update
```

2. Install vsftp.

```
apt-get install vsftpd -y
```

3. Add an FTP account and a directory.
i. Check the location of the nologin file, which is typically under the /usr/sbinor /sbin directory. ii. Create an FTP account. Run the following commands to create the /alidata/www/wwwroot directory and specify this directory as the home directory of the account pwftp. You can also customize the account name and directory.

```
mkdir -p /alidata/www/wwwroot useradd -d /alidata/www/wwwroot -s /sbin/nologin pwftp
```

iii. Modify the account password.

```
passwd pwftp
```

iv. Modify the permissions on the specified directory.

```
chown -R pwftp.pwftp /alidata/www/wwwroot
```

4. Configure vsftp.
i. Open the vsftp configuration file.

```
vi /etc/vsftpd.conf
```

ii. Change the value of anonymous_enable from `YES` to `NO` . iii. Delete the comment delimiter ( `#` ) from the following configuration lines:

```
local_enable=YES
        write_enable=YES
        chroot_local_user=YES
        chroot_list_enable=YES
        chroot_list_file=/etc/vsftpd.chroot_list
```

iv. Press the Esc key to exit the edit mode, and enter `:wq` to save the modifications and exit. v. Open the /etc/vsftpd.chroot_list file and add the FTP account name to the file. Save the modifications and exit. You can follow steps a to d to open and save the file.
5. Modify shell configurations.
i. Open the shell configuration file.

```
vi /etc/shells
```

ii. If the file does not contain /usr/sbin/nologin or /sbin/nologin, add it to the file.
6. Start vsftp and perform a logon test.
i. Start vsftp.

```
service vsftpd restart
```

ii. Use the account pwftp to perform an FTP logon test. This example uses the directory /alidata/www/wwwroot.

### 12.4 Build an FTP site in Windows Server 2008

Server 2008 This topic describes how to build an FTP site on an instance running Windows Server 2008. Prerequisites You have added the Web Server (IIS) role and installed FTP on an instance. Procedure
1. Connect to an instance.
2. Choose St art > Adminst rat ive T ools > Int ernet Inf ormat ion Services (IIS) Manager.
3. Right-click the server name and select Add FT P Sit e from the shortcut menu.
4. Enter an FTP site name and a physical path, and then click Next .
5. Set IP Address to All Unassigned and SSL to No SSL, and then click Next .
6. Set Aut hent icat ion to Basic, Aut horizat ion to All Users, and Permissions to Read and Writ e,
and click Finish. Result Then you can use the administrator account and password to upload and download files through FTP. Make sure that the following conditions are met: The port for the FTP site is not in use by other applications, and Windows firewall is not blocking the port. The security group of the instance contains a security group rule that allows inbound access to the FTP port.

### 12.5 Build an FTP site in Windows Server 2012

Server 2012 This topic describes how to build an FTP site on an instance running Windows Server 2012. Prerequisites You have added the Web Server (IIS) role and installed FTP on an instance. Procedure
1. Connect to an instance.
2. Click the Server Manager icon.
3. In the left-side navigation pane, click IIS.
4. In the Server area, right-click the server name and select Int ernet Inf ormat ion Services (IIS)
Manager from the shortcut menu.
5. Right-click the server name and select Add FT P Sit e from the shortcut menu.
6. Enter an FTP site name and a physical path, and then click Next .
7. Set IP Address to All Unassigned and SSL to No SSL, and then click Next .
8. Set Aut hent icat ion to Basic, Aut horizat ion to All Users, and Permissions to Read and Writ e,
and click Finish. Result Then you can use the administrator account and password to upload and download files through FTP. Make sure that the following conditions are met: The port for the FTP site is not in use by other applications, and Windows firewall is not blocking the port. The security group of the instance contains a security group rule that allows inbound access to the FTP port.
