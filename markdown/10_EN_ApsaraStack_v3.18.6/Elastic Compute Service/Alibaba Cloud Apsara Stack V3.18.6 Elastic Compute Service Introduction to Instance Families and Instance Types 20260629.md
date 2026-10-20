---
title: "Elastic Compute Service Introduction to Instance Families and Instance Types"
product_version: "V3.18.6"
doc_version: "20260629"
pdf_pages: 57
source_pdf: "2d3c695b236540a2_Alibaba Cloud Apsara Stack V3.18.6 Elastic Compute Service Introduction to Instance Families and Ins"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8ECS%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elastic%20Compute%20Service%20Introduction%20to%20Instance%20Families%20and%20Instance%20Types%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Elastic Compute Service Introduction to Instance Families and Instance Types

## Table of Contents

- 1 Instance families and instance types
- 2 Intel-based instance families
  - 2.1 Shared
  - 2.2 Dedicated
  - 2.3 ECS Bare Metal Instance families
  - 2.4 Heterogeneous computing and heterogeneous bare metal
  - 2.5 Super Computing Cluster (SCC)
  - 2.6 Local HDD
  - 2.7 Burstable instance families
  - 2.8 Network-enhanced
  - 2.9 Storage-enhanced instance families
  - 2.10 Trusted computing
  - 2.11 Local SSD
- 3 Yitian instance family
  - 3.1 Shared
  - 3.2 Dedicated instances
- 4 Hygon-based instance families
  - 4.1 Shared
  - 4.2 Dedicated
  - 4.3 Heterogeneous computing
  - 4.4 Local HDD
  - 4.5 Local SSD
  - 4.6 Super Computing Cluster
  - 4.7 Network-enhanced
  - 4.8 Storage-enhanced
- 5 Kunpeng-based instance families
  - 5.1 Shared
  - 5.2 Dedicated
  - 5.3 Local HDD
  - 5.4 Network-enhanced
- 6 Feiteng-based instance families
  - 6.1 Shared
  - 6.2 Dedicated

milies and instance types

## 1 Instance families and instance types

**instance types**

Alibaba Cloud Elastic Compute Service (ECS) instances are categorized into different instance families based on the business and use scenarios for which they are suitable. ECS instance families include shared instance families, dedicated instance families, ECS Bare Metal Instance families, instance families equipped with local HDDs, instance families equipped with local SSDs, heterogeneous computing instance families, and Super Computing Cluster (SCC) instance families. Each instance family consists of one or more instance types that share similar attributes.

**Instance families**

The following table describes the instance families and their use scenarios.

| Instance family | Application Scenario |
|---|---|
| Shared instance families | Shared instance families are suitable for business scenarios in which performance requirements are not high, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and integrated application services. |
| Dedicated instance families | Dedicated instance families are suitable for business scenarios that require high performance, such as web frontend servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios in which large volumes of packets are received and transmitted. |
| ECS Bare Metal Instance families | ECS Bare Metal Instance families provide robust computing, storage, and network configurations for business scenarios that require dedicated resources, security isolation, and high performance, such as containers, databases, core business of enterprises, and big data computing. |
| Local HDD | Instance families equipped with local HDDs are suitable for business scenarios that have high requirements for big data computing, storage, and analysis, such as mass storage and offline computing. These instance families can meet the high requirements of distributed computing services, such as Hadoop, for storage performance, storage capacity, and internal bandwidth. |
| Instance families equipped with local SSDs | Instance families equipped with local SSDs are suitable for I/O-intensive applications that require high performance and low latency, such as NoSQL databases (including Cassandra and MongoDB), MPP data warehouses, distributed file systems, and search scenarios that use solutions such as Elasticsearch. |
| Heterogeneous computing instance families | Heterogeneous computing instance families use various accelerators, such as NVIDIA T4 GPUs, NVIDIA V100 GPUs, and FPGAs, and are suitable for business scenarios such as AI inference, computer vision, speech recognition, speech synthesis, machine translation, recommendation systems, real-time rendering, deep learning, and scientific computing applications. |

milies and instance types

| Supercomputing Cluster | SCC instance families provide computing cluster services with ultimate computing performance and parallel efficiency using high-speed InfiniBand networks on top of ECS bare metal instances. SCC instance families are suitable for scenarios such as high-performance computing, AI, machine learning, scientific and engineering computing, data analysis, and audio and video processing. |
|---|---|
| Burstable | Burstable instance families provide baseline CPU performance with the ability to burst above the baseline by spending CPU credits. These instance families are suitable for business scenarios in which performance requirements are not high, such as web applications and small and medium-sized websites. |
| Network- enhanced instance families | Network-enhanced instance families are optimized for network-intensive scenarios. The network metrics of network-enhanced instance families are significantly higher than the network metrics of general-purpose instance families of the same generation. This ensures that network-enhanced instance families can meet the requirements of various scenarios. Network-enhanced instance families are especially suitable for scenarios that require higher network performance than general-purpose instance families. |
| Storage- enhanced instance families | Compared with instance families of the same generation, storage-enhanced instance families optimize capabilities related to Elastic Block Storage (EBS), such as disk bandwidth and IOPS. Storage-enhanced instance families are more suitable for storage-intensive scenarios. |
| Trusted computing | Trusted computing instances use UEFI secure firmware, virtual Trusted Platform Modules (vTPM/vTCM), and remote attestation services to measure and verify instance boot integrity. This ensures that the instances are secure and trusted. |

**Instance types**

An instance family can be categorized into multiple instance types based on the vCPU and memory specifications. ECS instance types define the basic attributes of instances, such as the number of vCPUs, memory size, network capabilities, and storage capabilities. Network capabilities include the network bandwidth, packet forwarding rate, maximum number of elastic network interfaces (ENIs) per instance, and maximum number of IP addresses per ENI. Storage capabilities include the maximum disk bandwidth, maximum disk IOPS, and maximum number of disks per instance. The network and storage performance of instances within the same instance family vary based on the computing capacity of the instances. The larger computing capacity an instance has, the higher network and storage performance the instance can deliver. The following figure shows the naming conventions of ECS instance types. milies and instance types Each instance type name consists of the following parts: Service name: Each instance type name starts with ecs., which indicates ECS. Instance family name: Examples: s6-k and g6x-k10. In s6-k, s indicates the shared instance family, 6 indicates the sixth generation, and k indicates Kernel-based Virtual Machine (KVM) virtualization. In g6x-k10, g indicates the dedicated instance family, 6 indicates the sixth generation, x indicates the use of 128 logical cores, and k10 indicates the use of KVM and 10 Gbit/s networks. CPU-to-memory ratio: For example, c1m2 indicates a CPU-to-memory ratio of 1:2, such as a configuration of 2 vCPUs and 4 GiB of memory, or 4 vCPUs and 8 GiB of memory. Number of vCPUs: For example, large indicates 2 vCPUs per instance, xlarge indicates 4 vCPUs per instance, 2xlarge indicates 8 vCPUs per instance, and 3xlarge indicates 12 vCPUs per instance. The following section describes the columns of the tables in the topics about Intel-, Hygon-, Kunpeng-, and Feiteng-based instance families. Instance family: the name of the instance family. Processor: the model of the processor that is supported and recommended for the instance family. For example, Intel V6 refers to Intel Cascade Lake processors. Virtualization: the virtualization technology used by the instance family, such as KVM, and the first-generation, second-generation, and third-generation SHENLONG architectures. Host threads: The number of hyper-threads (X86 architecture) or logical cores (ARM architecture) on the host, represented in vCPUs. In the same network environment, the network capability of a single vCPU differs if the physical machines have different numbers of vCPUs. The latest non-shared instance families make this distinction to provide better Quality of Service (QoS). The value 'Unlimited' indicates that the number of host vCPUs is not differentiated. Network: the network configurations of a host. On the same physical machine, the network capability of a single vCPU varies based on network configurations. Network configurations are specified for the most recent non-shared instance types to provide better QoS. 10 G indicates that the instance family is used in a 2 × 10 Gbit/s network, and 25 G indicates that the instance family is used in a 2 × 25 Gbit/s network. Unlimited indicates that network configurations are not specified. milies and instance types Description: the characteristics of the instance family, such as the number of vCPUs, compute-to-memory ratios, GPUs, and disks.

**Resource allocation**

Resources are allocated differently to ECS instances of different types. For all KVM-based instances, CPU and memory resources must be reserved for virtualization. For example, 8 vCPUs and 32 GiB of memory, 10 vCPUs and 40 GiB of memory, or 10 vCPUs and 48 GiB of memory must be reserved to handle network virtualization, storage virtualization, and system control tasks. For all instances that use the SHENLONG architecture, no CPU or memory resources need to be reserved on the server side. The SHENLONG architecture integrates software and hardware and offloads network virtualization, storage virtualization, and system control to dedicated chips. This provides zero resource overheads and prevents the performance of virtual machines from fluctuating when demand outstrips the resource supplies at the underlying layer. Memory resources and local disk resources of hosts cannot be overprovisioned. CPU resources of hosts that host shared and burstable instances can be overprovisioned. We recommend that you keep the overprovisioning ratio below four. CPU resources of hosts that host other instances cannot be overprovisioned.

**Limits on custom instance specifications**

Specific specifications have limits in usage. The following specifications do not support custom settings: CPU credits Non-Uniform Memory Access (NUMA) ON option Bare metal instance specifications vGPUs Super Computing Cluster (SCC) instance specifications

## 2 Intel-based instance families

**families**

### 2.1 Shared

Shared instances suit business scenarios that do not require high virtual machine performance, such as small and medium-sized websites and web applications, development environments, build servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and general application services. This topic describes the specific attributes, specification sizes, and virtualization technologies of shared instance families.

| Instance family | Processo r | Virtualization | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.s9-k | Intel V9 | KVM | 96 vCPU, 128 vCPU, 192 vCPU, 256 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.s8-k | Intel V8 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.s6-k | Intel V6 | KVM | 64 vCPU, 72 vCPU, 80 vCPU, 96 vCPU, 104 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.s6-m | Intel V6 | Second- generation Shenlong architecture | 64 vCPU, 96 vCPU, 104 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |

| ecs.s7-k | Intel V7 | KVM | 64 vCPU, 80 vCPU, 96 vCPU, 104 vCPU, 128 vCPU, 144 vCPU, 152 vCPU, 192 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
|---|---|---|---|---|---|
| ecs.anysh are | Intel | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU, 104 vCPU, 128 vCPU | 10 G, 25 G | You can create, modify, and delete custom instance specifications in the Apsara Uni-manager Operations Console. All custom instance specifications are shared instances and support only Intel processors. |
| ecs.xn4 | Intel V4/V5/V6 | KVM | 32 vCPU, 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Supports only ecs.xn4.small with 1 vCPU and 1 GiB memory. |
| ecs.n4 | Intel V4/V5/V6 | KVM | 32 vCPU, 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Specification sizes (vCPU): 1, 2, 4, 8, 16, 32 Compute-to-memory ratio: 1:2 |
| ecs.mn4 | Intel V4/V5/V6 | KVM | 32 vCPU, 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Specification sizes (vCPU): 1, 2, 4, 8, 16, 32 Compute-to-memory ratio: 1:4 |
| ecs.e4 | Intel V4/V5/V6 | KVM | 32 vCPU, 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Specification sizes (vCPU): 1, 2, 4, 8, 16 Compute-to-memory ratio: 1:8 |

| ecs.xn4v2 | Intel V4/V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | ecs.xn4.small with 1 vCPU and 1 GiB memory. Supports IPv6 addresses. |
|---|---|---|---|---|---|
| ecs.n4v2 | Intel V4/V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Specification sizes (vCPU): 1, 2, 4, 8, 16, 32 Compute-to-memory ratio: 1:2 Supports IPv6 addresses. |
| ecs.mn4v 2 | Intel V4/V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Specification sizes (vCPU): 1, 2, 4, 8, 16, 32 Compute-to-memory ratio: 1:4 Supports IPv6 addresses. |
| ecs.e4v2 | Intel V4/V5/V6 | KVM | 40 vCPU, 48 vCPU, 64 vCPU, 56 vCPU, 80 vCPU, 96 vCPU | 10 G, 25 G | Specification sizes (vCPU): 1, 2, 4, 8, 16 Compute-to-memory ratio: 1:8 Supports IPv6 addresses. |

### 2.2 Dedicated

Dedicated instance families suit business scenarios that require high virtual machine performance, such as high packet forwarding rate scenarios, web frontend servers, data analysis, batch computing, video encoding, and high-performance scientific and engineering applications. This topic describes specific attributes, specification sizes, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualization | Host threads | Networ k | Description |
|---|---|---|---|---|---|

| ecs.g9m- k10 | Intel V9 | Kernel-based Virtual Machine (KVM) | 96 vCPU | 10 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 86 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
|---|---|---|---|---|---|
| ecs.g9m- k25 | Intel V9 | KVM | 96 vCPU | 25 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 86 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.g9x- k10 | Intel V9 | KVM | 128 vCPU | 10 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.g9x- k25 | Intel V9 | KVM | 128 vCPU | 25 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.g9v- k10 | Intel V9 | KVM | 192 vCPU | 10 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 128, 160, and 178 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |

| ecs.g9v- k25 | Intel V9 | KVM | 192 vCPU | 25 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 128, 160, and 178 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
|---|---|---|---|---|---|
| ecs.g9h- k10 | Intel V9 | KVM | 256 vCPU | 10 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 128, 160, 192, 224, and 242 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.g9h- k25 | Intel V9 | KVM | 256 vCPU | 25 G | Supports ENI Trunking Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 128, 160, 192, 224, and 242 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.g8x- k25 | Intel V8 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.g8x- k10 | Intel V8 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |

| ecs.g8s- k10 | Intel V8 | Kernel-based Virtual Machine (KVM) | 64 vCPU | 10 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
|---|---|---|---|---|---|
| ecs.g8s- k25 | Intel V8 | KVM | 64 vCPU | 25 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g8m- k10 | Intel V8 | KVM | 96 vCPU | 10 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g8m- k25 | Intel V8 | KVM | 96 vCPU | 25 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g7x- x25 | Intel V7 | Third- generation SHENLONG architecture | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 48, 64, and 128. |
| ecs.g7s- k10 | Intel V7 | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, and 54. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g7s- k25 | Intel V7 | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, and 54. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g7m- k10 | Intel V7 | KVM | 96 vCPU | 10 GB | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 86. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |

| ecs.g7m- k25 | Intel V7 | KVM | 96 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 86. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
|---|---|---|---|---|---|
| ecs.g7x- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g7x- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g7v- k10 | Intel V7 | KVM | 192 vCPU | 10 GB | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g7v- k25 | Intel V7 | KVM | 192 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g6s- m10 | Intel V6 | Second- generation SHENLONG architecture | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |

| ecs.g6s- m25 | Intel V6 | Second- generation SHENLONG architecture | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
|---|---|---|---|---|---|
| ecs.g6m- m10 | Intel V6 | Second- generation SHENLONG architecture | 96 vCPU | 10 GB | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g6m- m25 | Intel V6 | Second- generation SHENLONG architecture | 96 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g6s- k10 | Intel V6 | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g6s- k25 | Intel V6 | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.g6m- k10 | Intel V6 | KVM | 96 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 88. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |

| ecs.g6m- k25 | Intel V6 | KVM | 96 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 88. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
|---|---|---|---|---|---|
| ecs.c6 | Intel V6 | Second- generation SHENLONG architecture | 104 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 52, 64, and 104. Compute-to-memory ratio: 1:2. |
| ecs.g6 | Intel V6 | Second- generation SHENLONG architecture | 104 vCPU | 25 GB | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 52, 64, and 104. Compute-to-memory ratio: 1:4. |
| ecs.r6 | Intel V6 | Second- generation SHENLONG architecture | 104 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 52, 64, and 104. Compute-to-memory ratio: 1:8 |
| ecs.re6 | Intel V6 | Second- generation SHENLONG architecture | 208 vCPU | 10 G and 25 G | Offers memory of 3 TB and a compute-to- memory ratio of 1:15. |
| ecs.sn1 | Intel V5/V6 | KVM | 48 vCPU, 64 vCPU, and 96 vCPU | 10 G and 25 G | Specification sizes (vCPU): 2, 4, 8, 16, 32, and 56. Compute-to-memory ratio: 1:2. |
| ecs.sn2 | Intel V5/V6 | KVM | 48 vCPU, 64 vCPU, and 96 vCPU | 10 G and 25 G | Specification sizes (vCPU): 2, 4, 8, 16, 32, and 56. Compute-to-memory ratio: 1:4. |

| ecs.se1 | Intel V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, and 96 vCPU | 10 G and 25 G | Specification sizes (vCPU): 2, 4, 8, 16, 32, and 56. Compute-to-memory ratio: 1:8. |
|---|---|---|---|---|---|
| ecs.sn1ne | Intel V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, and 96 vCPU | 10 G and 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, and 88. Compute-to-memory ratio: 1:2. Supports IPv6 addresses. |
| ecs.sn2ne | Intel V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, and 96 vCPU | 10 G and 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 56, and 88. Compute-to-memory ratio: 1:4. Supports IPv6 addresses. |
| ecs.se1ne | Intel V5/V6 | KVM | 40 vCPU, 48 vCPU, 56 vCPU, 64 vCPU, 80 vCPU, and 96 vCPU | 10 G and 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 56, and 88. Compute-to-memory ratio: 1:8 Supports IPv6 addresses. |
| ecs.c5 | Intel V5 | Second- generation SHENLONG architecture | 104 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 64, 86, and 88. Compute-to-memory ratio: 1:2. |
| ecs.g5 | Intel V5 | Second- generation SHENLONG architecture | 104 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 64, 86, and 88. Compute-to-memory ratio: 1:4. |
| ecs.r5 | Intel V5 | Second- generation SHENLONG architecture | 104 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 64, 86, and 88. Compute-to-memory ratio: 1:8 |

### 2.3 ECS Bare Metal Instance families

**families**

Elastic Compute Service (ECS) Bare Metal Instance families provide robust compute, storage, and network configurations for business scenarios that require dedicated resources, security isolation, and high performance, such as containers, databases, core business of enterprises, and big data computing. This topic describes the attributes, specifications, and virtualization technologies of ECS Bare Metal Instance families.

| Instance family | Processor | Virtualizat ion | Physical machine threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.ebmg7 s-se-x25- c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 64 vCPUs | 25 G | Provides the ecs.ebmg7s- se-x25-c1m8.16xlarge instance type with 64 vCPUs and 512 GiB of memory. Supports Shared Block Storage and lets you enable Non-Uniform Memory Access (NUMA) mode. |
| ecs.ebmg7 m-se-x25- c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 96 vCPUs | 25 G | Provides the ecs.ebmg7m- se-x25-c1m8.24xlarge instance type with 96 vCPUs and 768 GiB of memory. Supports Shared Block Storage and lets you enable NUMA mode. |
| ecs.ebmg7 x-se-x25- c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPUs | 25 G | Provides the ecs.ebmg7x- se-x25-c1m8.32xlarge instance type with 128 vCPUs and 1,024 GiB of memory. Supports Shared Block Storage and lets you enable NUMA mode. |
| ecs.ebmg7 s-se- numaoff- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 64 vCPUs | 25 G | Provides the ecs.ebmg7s- se-numaoff-x25- c1m8.16xlarge instance type with 64 vCPUs and 512 GiB of memory. Supports Shared Block Storage and lets you disable NUMA mode. |

| ecs.ebmg7 m-se- numaoff- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 96 vCPUs | 25 G | Provides the ecs.ebmg7m- se-numaoff-x25- c1m8.24xlarge instance type with 96 vCPUs and 768 GiB of memory. Supports Shared Block Storage and lets you disable NUMA mode. |
|---|---|---|---|---|---|
| ecs.ebmg7 x-se- numaoff- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPUs | 25 G | Provides the ecs.ebmg7x- se-numaoff-x25- c1m8.32xlarge instance type with 128 vCPUs and 1,024 GiB of memory. Supports Shared Block Storage and lets you disable NUMA mode. |
| ecs.ebmg7 s-x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 64 vCPUs | 25 G | Provides the ecs.ebmg7s-x25- c1m8.16xlarge instance type with 64 vCPUs and 512 GiB of memory and lets you enable NUMA mode. CPU-to-memory ratio: 1:8. |
| ecs.ebmg7 m-x25- c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 96 vCPUs | 25 G | Provides the ecs.ebmg7m- x25-c1m8.24xlarge instance type with 96 vCPUs and 768 GiB of memory and lets you enable NUMA mode. |
| ecs.ebmg7 x-x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPUs | 25 G | Provides the ecs.ebmg7x-x25- c1m8.32xlarge instance type with 128 vCPUs and 1,024 GiB of memory and lets you enable NUMA mode. CPU-to-memory ratio: 1:8. |
| ecs.ebmg7 x-1nvme- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPUs | 25 G | ecs.ebmg7x-1nvme-x25- c1m8.32xlarge: 128 vCPUs and 1024 GiB of memory. |

| ecs.ebmg7 x-12nvme- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPUs | 25 G | ecs.ebmg7x-1nvme-x25- c1m8.32xlarge, 128 vCPUs, 1024 GiB |
|---|---|---|---|---|---|
| ecs.ebmg6 s-m10- c1m4 | Intel V6 | Second- generation SHENLONG architectur e | 64 vCPUs | 10 G | Provides the ecs.ebmg6s- m10-c1m4.16xlarge instance type with 64 vCPUs and 256 GiB of memory. |
| ecs.ebmg6 s-m25- c1m4 | Intel V6 | Second- generation SHENLONG architectur e | 64 vCPUs | 25 G | Provides the ecs.ebmg6s- m25-c1m4.16xlarge instance type with 64 vCPUs and 256 GiB of memory. |
| ecs.ebmg6 s-m10- c1m24 | Intel V6 | Second- generation SHENLONG architectur e | 64 vCPUs | 10 G | Provides the ecs.ebmg6s- m10-c1m24.16xlarge instance type with 64 vCPUs and 1,536 GiB of memory. |
| ecs.ebmg6 s-m25- c1m24 | Intel V6 | Second- generation SHENLONG architectur e | 64 vCPUs | 25 G | Provides the ecs.ebmg6s- m25-c1m24.16xlarge instance type with 64 vCPUs and 1,536 GiB of memory. |
| ecs.ebmg6 m-m10- c1m4 | Intel V6 | Second- generation SHENLONG architectur e | 96 vCPUs | 10 G | Provides the ecs.ebmg6m- m10-c1m4.24xlarge instance type with 96 vCPUs and 384 GiB of memory. |
| ecs.ebmg6 m-m25- c1m4 | Intel V6 | Second- generation SHENLONG architectur e | 96 vCPUs | 10 G | Provides the ecs.ebmg6m- m25-c1m4.24xlarge instance type with 96 vCPUs and 384 GiB of memory. |
| ecs.ebmre6 -3t | Intel V6 | Second- generation SHENLONG architectur e | 208 vCPUs | 25 G | Provides the ecs.ebmre6- 3t.52xlarge instance type with 208 vCPUs and 3,072 GiB of memory. |

| ecs.ebmc6 | Intel V6 | Second- generation SHENLONG architectur e | 104 vCPUs | 25 G | Provides the ecs.ebmc6.26xlarge instance type with 104 vCPUs and 192 GiB of memory. |
|---|---|---|---|---|---|
| ecs.ebmg6 | Intel V6 | Second- generation SHENLONG architectur e | 104 vCPUs | 25 G | Provides the ecs.ebmg6.26xlarge instance type with 104 vCPUs and 384 GiB of memory. |
| ecs.ebmr6 | Intel V6 | Second- generation SHENLONG architectur e | 104 vCPUs | 25 G | Provides the ecs.ebmr6.26xlarge instance type with 104 vCPUs and 768 GiB of memory. |
| ecs.ebmre6 p | Intel V6 | Second- generation SHENLONG architectur e | 104 vCPUs | 25 G | Uses 1,536 GiB of Intel Optane persistent memory (AEP). |
| ecs.ebmg5 | Intel V5 | First- generation SHENLONG architectur e | 96 vCPUs | 10 G | Provides the ecs.ebmg5.24xlarge instance type with 96 vCPUs and 384 GiB of memory. |
| ecs.ebmg5 s | Intel V5 | Second- generation SHENLONG architectur e | 96 vCPUs | 25 G | Provides the ecs.ebmg5s.24xlarge instance type with 96 vCPUs and 384 GiB of memory. |

### 2.4 Heterogeneous computing and heterogeneous bare metal

**heterogeneous bare metal**

Heterogeneous computing and heterogeneous bare metal instances work with various accelerators, such as NVIDIA T4, NVIDIA V100, Cambricon MLU 370 S4, Hygon DCU Z100, and FPGA. These instances apply to business scenarios such as AI inference, computer vision, speech recognition and synthesis, machine translation, recommendation systems, real-time rendering, deep learning, and scientific computing. This topic describes specific attributes, specification sizes, and virtualization technologies of heterogeneous computing and heterogeneous bare metal instance families.

| Instance family | Processo r | Virtualization | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.gn8ix- k25 | Intel V8 | KVM | 128 vCPU | 25 G | Equipped with eight NVIDIA L20 GPUs. |
| ecs.gn7fm -k10 | Intel V7 | KVM | 96 vCPU | 10 G | Equipped with four NVIDIA A16 GPUs. |
| ecs.gn7fm -k25 | Intel V7 | KVM | 96 vCPU | 25 G | Equipped with four NVIDIA A16 GPUs. |
| ecs.gn7km -k10 | Intel V7 | KVM | 96 vCPU | 10 G | Equipped with four NVIDIA A2 GPUs. |
| ecs.gn7km -k25 | Intel V7 | KVM | 96 vCPU | 25 G | Equipped with four NVIDIA A2 GPUs. |
| ecs.gn7kx- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with eight NVIDIA A2 GPUs. |
| ecs.gn7kx- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with eight NVIDIA A2 GPUs. |
| ecs.gn7im -k10 | Intel V7 | KVM | 96 vCPU | 10 G | Equipped with two NVIDIA A10 GPUs. |
| ecs.gn7im -k25 | Intel V7 | KVM | 96 vCPU | 25 G | Equipped with two NVIDIA A10 GPUs. |
| ecs.gn7fx- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with eight NVIDIA A16 GPUs. |
| ecs.gn7fx- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with eight NVIDIA A16 GPUs. |
| ecs.gh6v m-k10 | Intel V7 | KVM | 96 vCPU | 10 G | Equipped with two Hygon DCU Z100 accelerators. |
| ecs.gh6v m-k25 | Intel V7 | KVM | 96 vCPU | 25 G | Equipped with two Hygon DCU Z100 accelerators. |

| ecs.gh6vx- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with eight Hygon DCU Z100 accelerators. |
|---|---|---|---|---|---|
| ecs.gh6vx- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with eight Hygon DCU Z100 accelerators. |
| ecs.gc6im- k10 | Intel V7 | KVM | 96 vCPU | 10 G | Equipped with two Cambricon MLU 370 S4 accelerators. |
| ecs.gc6im- k25 | Intel V7 | KVM | 96 vCPU | 25 G | Equipped with two Cambricon MLU 370 S4 accelerators. |
| ecs.gc6ix- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with eight Cambricon MLU 370 S4 accelerators. |
| ecs.gc6ix- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with eight Cambricon MLU 370 S4 accelerators. |
| ecs.gc6em -k10 | Intel V7 | KVM | 96 vCPU | 10 G | Equipped with two Cambricon MLU 370 X8 accelerators. |
| ecs.gc6em -k25 | Intel V7 | KVM | 96 vCPU | 25 G | Equipped with two Cambricon MLU 370 X8 accelerators. |
| ecs.gc6ex- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with eight Cambricon MLU 370 X8 accelerators. |
| ecs.gc6ex- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with eight Cambricon MLU 370 X8 accelerators. |
| ecs.gn7ix- x25 | Intel V7 | Third- generation Shenlong architecture | 128 vCPU | 25 G | Equipped with four NVIDIA A10 GPUs. |
| ecs.ebmg n7ix-x25- c1m8 | Intel V7 | Third- generation Shenlong architecture | 128 vCPU | 25 G | Equipped with four NVIDIA A10 GPUs. |

| lastic Compu | te Service |   |   | Introd and I | uction to Instance Families nstance Types ·Intel-based nstance familie |
|---|---|---|---|---|---|

| ecs.vgn7ix -x25 | Intel V7 | Third- generation Shenlong architecture | 128 vCPU | 25 G | Equipped with four NVIDIA A10 GPUs. Supports fractional vGPUs. Suports one-half, one-third, one-fourth, or one-sixth allocation of an NVIDIA A10 GPU. |
|---|---|---|---|---|---|
| ecs.vgn6ix -k25-slice2 | Intel V7 | KVM | 128 vCPU | 25 G | Supports fractional vGPUs. Supports one-half allocation of an NVIDIA Tesla T4 GPU. |
| ecs.vgn6ix -k10-slice2 | Intel V7 | KVM | 128 vCPU | 10 G | Supports fractional vGPUs. Supports one-half allocation of an NVIDIA Tesla T4 GPU. |
| ecs.vgn6i m-k25- slice4 | Intel V7 | KVM | 96 vCPU | 25 G | Supports fractional vGPUs. Supports one-fourth allocation of an NVIDIA Tesla T4 GPU. |
| ecs.vgn6i m-k10- slice4 | Intel V7 | KVM | 96 vCPU | 10 G | Supports fractional vGPUs. Supports one-fourth allocation of an NVIDIA Tesla T4 GPU. |
| ecs.gn7ix- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with four or eight NVIDIA A10 GPUs. |
| ecs.gn7ix- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with four NVIDIA A10 GPUs. |
| ecs.gn6ix- k25 | Intel V7 | KVM | 128 vCPU | 25 G | Equipped with four NVIDIA Tesla T4 GPUs. |
| ecs.gn6ix- k10 | Intel V7 | KVM | 128 vCPU | 10 G | Equipped with four NVIDIA Tesla T4 GPUs. |

| ecs.gn6i | Intel V5/V6 | KVM | 48 vCPU, 64 vCPU, 80 vCPU, or 96 vCPU | 10 G or 25 G | Equipped with one to eight NVIDIA T4 GPUs. The computing-to- memory ratio is approximately 1:4. |
|---|---|---|---|---|---|
| ecs.gn6v | Intel V5/V6 | KVM | 96 vCPU | 10 G or 25 G | Equipped with one to eight NVIDIA V100 GPUs. The computing-to- memory ratio is approximately 1:4. |
| ecs.vgn6i | Intel V5/V6 | Second- generation Shenlong architecture | 96 vCPU or 104 vCPU | 10 G or 25 G | Supports fractional vGPUs. Supports one-fourth or one-half allocation of an NVIDIA Tesla T4 GPU. |
| ecs.ebmg n6i | Intel V5/V6 | Second- generation Shenlong architecture | 96 vCPU or 104 vCPU | 10 G or 25 G | Equipped with four NVIDIA T4 GPUs. ECS Bare Metal |
| ecs.ebmg n6i-2 | Intel V5/V6 | Second- generation Shenlong architecture | 96 vCPU or 104 vCPU | 10 G or 25 G | Equipped with two NVIDIA T4 GPUs. ECS Bare Metal |
| ecs.ebmg n6i-8 | Intel V5/V6 | Second- generation Shenlong architecture | 96 vCPU | 10 G or 25 G | Equipped with eight NVIDIA T4 GPUs. ECS Bare Metal |
| ecs.ebmg n6e-2 | Intel V6 | Second- generation Shenlong architecture | 104 vCPU | 10 G or 25 G | Equipped with two NVIDIA V100 GPUs. ECS Bare Metal |
| ecs.gn3 | Intel V4 | KVM | 56 vCPU | 10 G or 25 G | Equipped with one to two NVIDIA K2 GPUs. |
| ecs.gn4 | Intel V4 | KVM | 56 vCPU | 10 G or 25 G | Equipped with one to two NVIDIA M40 GPUs. |
| ecs.gn5 | Intel V4 | KVM | 64 vCPU | 10 G or 25 G | Equipped with one to eight NVIDIA P100 GPUs. |

| ecs.gn5e | Intel V5 | KVM | 96 vCPU | 10 G or 25 G | Equipped with one to eight NVIDIA P4 GPUs. The computing-to- memory ratio is 1:6. |
|---|---|---|---|---|---|
| ecs.gn5i | Intel V4 | KVM | 56 vCPU or 64 vCPU | 10 G or 25 G | Equipped with one to two NVIDIA P4 GPUs. The computing-to- memory ratio is 1:4. |
| ecs.gn5t | Intel V4 | KVM | 64 vCPU | 10 G or 25 G | Equipped with two to eight NVIDIA 1080Ti GPUs. The computing-to- memory ratio is approximately 1:4. |

### 2.5 Super Computing Cluster (SCC)

**(SCC)**

Super Computing Cluster (SCC) instance families provide computing cluster services with ultimate computing performance and parallel efficiency using high-speed InfiniBand networks on top of Elastic Compute Service (ECS) bare metal instances. SCC instance families are suitable for scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analytics, and audio and video processing. This topic describes the attributes, specifications, and virtualization technologies of SCC instance families.

> **Note:** SCCs are dedicated to HPC scenarios. To use SCCs, the hyper-threading feature must be disabled. However, the instance type is still calculated based on hyper-threading being enabled. Therefore, the number of CPU cores displayed in the operating system (GuestOS) is half of the defined instance type.

| Instance family | Processor | Virtualizat ion | Physical machine vCPUs | Networ k | Description |
|---|---|---|---|---|---|
| ecs.sccg7- ib | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | Uses an InfiniBand high- performance network. |

| ecs.sccc7- ib | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | Uses an InfiniBand high- performance network. |
|---|---|---|---|---|---|
| ecs.sccr7-ib | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | Uses an InfiniBand high- performance network. |
| ecs.sccg7x- roce-x25- c1m2 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | Supports Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE) network interface controllers (NICs). |
| ecs.sccg7x- roce-x25- c1m4 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | Supports RoCE NICs. |
| ecs.sccg7x- roce-x25- c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | Supports RoCE NICs. |
| ecs.sccgn6 e | Intel V6 | Second- generation SHENLONG architectur e | 104 vCPU | 10 or 25 GB | Uses eight NVIDIA V100 GPUs and a 100 GB InfiniBand network. |
| ecs.sccgn6 p | Intel V5/V6 | Second- generation SHENLONG architectur e | 96 vCPU | 10 or 25 GB | Uses eight NVIDIA V100 GPUs and a 100 GB InfiniBand network. |
| ecs.scch5 | Intel V5 | Second- generation SHENLONG architectur e | 64 vCPU | 10 or 25 GB | Uses processors with high clock speeds that deliver a base frequency of 3.1 GHz and an all-core turbo frequency of 3.5 GHz. |

| ecs.sccg5ib | Intel V5 | First- generation SHENLONG architectur e | 96 vCPU | 10 GB | Uses a 100 GB InfiniBand network. |
|---|---|---|---|---|---|

### 2.6 Local HDD

Local HDD instances suit business scenarios that require big data computing and storage analysis, such as massive data storage and offline computing. These instances meet the requirements of distributed computing workloads represented by Hadoop for instance storage performance, storage capacity, and internal bandwidth. This topic describes specific attributes, specification sizes, and virtualization technologies of local HDD instance families.

| Instance family | Processo r | Virtualization | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.d7s- 12x8t-k25 | Intel V7 | KVM | 64 vCPU | 25 G | The host is equipped with twelve 8 TB SATA HDDs. |
| ecs.d7x- 12x12t- k25 | Intel V7 | KVM | 128 vCPU | 25 G | The host is equipped with twelve 12 TB SATA HDDs. |
| ecs.d7x- 12x12t- k10 | Intel V7 | KVM | 128 vCPU | 10 G | The host is equipped with twelve 12 TB SATA HDDs. |
| ecs.d7s- 12x8t-k10 | Intel V7 | KVM | 64 vCPU | 10 G | The host is equipped with twelve 8 TB SATA HDDs. |
| ecs.d7s- 10x16t- k25 | Intel V7 | KVM | 64 vCPU | 25 G | The host is equipped with ten 16 TB SATA HDDs. |
| ecs.d7s- 10x16t- k10 | Intel V7 | KVM | 64 vCPU | 10 G | The host is equipped with ten 16 TB SATA HDDs. |
| ecs.d7m- 12x8t-k25 | Intel V7 | KVM | 96 vCPU | 25 G | The host is equipped with twelve 8 TB SATA HDDs. |
| ecs.d7m- 12x8t-k10 | Intel V7 | KVM | 96 vCPU | 10 G | The host is equipped with twelve 8 TB SATA HDDs. |

| ecs.d7s- k10-8t | Intel V7 | KVM | 64 vCPU | 10 G | The host is equipped with twelve 8 TB SATA HDDs. |
|---|---|---|---|---|---|
| ecs.d7s- k25-8t | Intel V7 | KVM | 64 vCPU | 25 G | The host is equipped with twelve 8 TB SATA HDDs. |
| ecs.d7m- k10-8t | Intel V7 | KVM | 96 vCPU | 10 G | The host is equipped with twelve 8 TB SATA HDDs. |
| ecs.d7m- k25-8t | Intel V7 | KVM | 96 vCPU | 25 G | The host is equipped with twelve 8 TB SATA HDDs. |
| ecs.d7x- k10-12t | Intel V7 | KVM | 128 vCPU | 10 G | The host is equipped with twelve 12 TB SATA HDDs. |
| ecs.d7x- k25-12t | Intel V7 | KVM | 128 vCPU | 25 G | The host is equipped with twelve 12 TB SATA HDDs. |
| ecs.d6m- 24x2t-k10 | Intel V6 | KVM | 80 vCPU | 10 G | The host is equipped with twenty-four 2 TB SATA HDDs. |
| ecs.d5m- 24x1t-k10 | Intel V5 | KVM | 80 vCPU | 10 G | The host is equipped with twenty-four 1 TB SATA HDDs. |
| ecs.d4s- 16x1t-k10 | Intel V4 | KVM | 56 vCPU | 10 G | The host is equipped with sixteen 1 TB SATA HDDs. |
| ecs.d2-zyy | Intel V5/V6 | KVM | 40 vCPU, 48 vCPU, 64 vCPU, 80 vCPU, 96 vCPU, 104 vCPU | 10 G, 25 G | The host is equipped with twelve 8 TB SATA HDDs. |

### 2.7 Burstable instance families

Burstable instance families provide baseline CPU performance with the ability to burst above the baseline by spending CPU credits. These instance types are suitable for business scenarios that do not require high performance of virtual machines, such as web applications and small and medium-sized websites. This topic describes the attributes, specifications, and virtualization technologies of burstable instance families.

| Instance family | Processor | Virtualizat ion | Physical machine vCPUs | Netwo rk | Description |
|---|---|---|---|---|---|
| ecs.t5 | Intel V5/V6 | KVM | 40 vCPU, 48 vCPU, 64 vCPU, 80 vCPU, 96 vCPU, 104 vCPU | 10 Gbps, 25 Gbps | Provides baseline CPU performance with the ability to burst above the baseline by spending CPU credits. |

### 2.8 Network-enhanced

Network-enhanced instance families are optimized for network-intensive scenarios. The network metrics of network-enhanced instance families are significantly higher than those of general-purpose instance families of the same generation. This ensures that networkenhanced instance families can meet the requirements of various scenarios. Networkenhanced instance families are especially suitable for scenarios that require higher network performance than general-purpose instance families. This topic describes the attributes, specifications, and virtualization technologies of network-enhanced instance families.

| Instance family | Processor | Virtualiza tion | Physical Machine Thread Count | Network | Family Description |
|---|---|---|---|---|---|
| ecs.ne9x- k25 | Intel V9 | KVM | 128 vCPU | 25 G | Instance sizes (vCPUs): 2, 4, 8, 16, 32, 64, and 72 CPU-to-memory ratios: 1:2, 1:4, 1:6, and 1:8 |
| ecs.ne9m- k25 | Intel V9 | KVM | 96 vCPU | 25 G | Instance sizes (vCPUs): 2, 4, 8, 16, 32, 64, and 72 CPU-to-memory ratios: 1:2, 1:4, 1:6, and 1:8 |
| ecs.ne8m- k25 | Intel V8 | KVM | 96 vCPUs | 25 G | Instance sizes (vCPUs): 2, 4, 8, 16, 32, 64, and 72 CPU-to-memory ratios: 1:2, 1:4, 1:6, and 1:8 |

| ecs.ne7x- k10 | Intel V7 | KVM | 128 vCPUs | 10 G | Instance sizes (vCPUs): 2, 4, 8, 16, 32, 64, 72, 96, and 104 CPU-to-memory ratios: 1:2, 1:4, 1:6, and 1:8 |
|---|---|---|---|---|---|
| ecs.ne7m- k25 | Intel V7 | KVM | 96 vCPUs | 25 G | Instance sizes (vCPUs): 8, 12, 16, 24, 32, 40, 48, 56, 64, and 72 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |
| ecs.ne7m- k10 | Intel V7 | KVM | 96 vCPUs | 10 G | Instance sizes (vCPUs): 8, 12, 16, 24, 32, 40, 48, 56, 64, and 72 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 |

### 2.9 Storage-enhanced instance families

**families**

Storage-enhanced instance families are optimized for storage-intensive scenarios and provide optimized Elastic Block Storage (EBS)-related capabilities, such as disk bandwidth and disk IOPS. This topic describes the attributes, specifications, and virtualization technologies of storage-enhanced instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Network | Description |
|---|---|---|---|---|---|
| ecs.g7x-se- k25 | Intel V7 | KVM | 128 vCPUs | 25 Gbps | Supports Shared Block Storage |
| ecs.g7x-se- x25 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPUs | 25 Gbps | Supports Shared Block Storage |

| ecs.g7x-se- x25 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | vCPUs: 2, 4, 8, 12, 16, 24, 32, 48, 64, and 128. |
|---|---|---|---|---|---|
| ecs.ebmg7 s-se- numaoff- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 64 vCPU | 25 GB | CPU-to-memory ratio: 1:8. Supports Shared Block Storage and lets you disable NUMA mode. |
| ecs.g7s-se- x25 | Intel V7 | Third- generation SHENLONG architectur e | 64 vCPU | 25 GB | CPU-to-memory ratio: 1:8. |
| ecs.ebmg7 x-se- numaoff- x25-c1m8 | Intel V7 | Third- generation SHENLONG architectur e | 128 vCPU | 25 GB | CPU-to-memory ratio: 1:8. Supports Shared Block Storage and lets you disable NUMA mode. |

### 2.10 Trusted computing

Trusted computing instances use UEFI secure firmware, virtual Trusted Platform Modules (vTPM/vTCM), and remote attestation services to measure boot processes and verify integrity. This process ensures that your instances are secure and trustworthy. This topic describes the properties, instance sizes, and virtualization technologies of trusted computing instance families.

| Family | Processo r | Virtualiz ation | Physical server threads | Network | Family description |
|---|---|---|---|---|---|
| ecs.g7x- vtpm-k25 | Intel V7 | KVM | 128vCPU | 25 G | Supports ENI Trunking Compute-to-memory ratio: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |

### 2.11 Local SSD

Local SSD instances are I/O-intensive local disk storage instances which suit business scenarios that demand extremely high storage I/O performance and have a high-availability architecture at the application layer, such as NoSQL non-relational databases, MPP data warehouses, and distributed file systems.

| Instance family | Processor | Virtualizati on | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.i7m- 12x4t- k25 | Intel V7 | KVM | 96 vCPU | 25 G | The host is equipped with 12 NVMe SSDs, each with 3840 GB capacity. |
| ecs.i7m- 4x4t-k25 | Intel V7 | KVM | 96 vCPU | 25 G | The host is equipped with 4 NVMe SSDs, each with 3840 GB capacity. |
| ecs.i7x- 12x4t- k25 | Intel V7 | KVM | 128 vCPU | 25 G | The host is equipped with 12 NVMe SSDs, each with 3840 GB capacity. |
| ecs.i7x- 12x4t- k10 | Intel V7 | KVM | 128 vCPU | 10 G | The host is equipped with 12 NVMe SSDs, each with 3840 GB capacity. |
| ecs.i6m- k25-4x4t | Intel V6 | KVM | 96 vCPU | 25 G | The host is equipped with 4 NVMe SSDs, each with 3840 GB capacity. |
| ecs.i6m- k10-4x4t | Intel V6 | KVM | 96 vCPU | 10 G | The host is equipped with 4 NVMe SSDs, each with 3840 GB capacity. |

ce family

## 3 Yitian instance family

### 3.1 Shared

Shared instances suit business scenarios that do not require high virtual machine performance, such as small to medium-sized websites and web applications, developer environments, build servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and general application services. This topic describes the properties, specification sizes, and virtualization technologies of shared instance families.

| Instance family | Processo r | Virtualization | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.s8-yt- k | Yitian 710 | KVM | 128 vCPU | 10 Gbps, 25 Gbps | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.s8- numaon- yt-k | Yitian 710 | KVM | 128 vCPU | 10 Gbps, 25 Gbps | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 Supports NUMA ON confifiguration. |

### 3.2 Dedicated instances

Dedicated instances suit business scenarios that require high virtual machine performance, such as high packet forwarding rate scenarios, web frontend servers, data analysis, batch computing, video encoding, and high-performance scientific and engineering applications. This topic describes specific attributes, specification sizes, and virtualization technologies of dedicated instance families.

| Instance family | Processo r | Virtualizatio n | Host threads | Networ k | Description |
|---|---|---|---|---|---|

ce family

| ecs.g8x- yt-k10 | Yitian 710 | KVM | 128 vCPUs | 10 G | Specification sizes (vCPUs): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 118 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
|---|---|---|---|---|---|
| ecs.g8x- yt-k25 | Yitian 710 | KVM | 128 vCPUs | 25 GB | Specification sizes (vCPUs): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 118 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 Supports NUMA. |
| ecs.g8x- numaon- yt-k10 | Yitian 710 | KVM | 128 vCPUs | 10 GB | Specification sizes (vCPUs): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 80, 96 Compute-to-memory ratio: 1:4 Supports NUMA. |
| ecs.g8x- numaon- yt-k25 | Yitian 710 | KVM | 128 vCPUs | 25 G | Specification sizes (vCPUs): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 80, 96 Compute-to-memory ratio: 1:4 Supports NUMA. |

d instance families

## 4 Hygon-based instance families

**families**

### 4.1 Shared

Shared instances suit business scenarios that do not require high virtual machine performance, such as small and medium-sized websites and web applications, development environments, build servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and general application services. This topic describes the specific attributes, specification sizes, and virtualization technologies of shared instance families.

| Insta nce famil y | Proce ssor | Virtualiz ation | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.s8 -hg-k | Hygon 4 | KVM | 256 vCPU | 25 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 |
| ecs.s8 - numa on-hg- k | Hygon 4 | KVM | 256 vCPU | 10 G, 25 G | Supports NUMA ON configuration Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 |
| ecs.s7 -hg-k | Hygon 3 | KVM | 128 vCPU | 10 G, 25 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 |
| ecs.s6 -hg-k | Hygon 2 | KVM | 64 vCPU, 128 vCPU | 10 G, 25 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 |
| ecs.gh g-s | Hygon 1 | Shenlong Generatio n 2 | 128 vCPU | 10 G, 25 G | Compute-to-memory ratio: 1:4 Specification sizes (vCPU): 2, 4, 8, 12, 16, 32, 64, 96, 128 |

### 4.2 Dedicated

d instance families Dedicated instances suit business scenarios that require high virtual machine performance, such as high packet forwarding rate scenarios, frontend web servers, data analysis, batch computing, video encoding, and high-performance scientific and engineering applications. This topic describes the specific attributes, specification sizes, and virtualization technologies of dedicated instance families.

| Instance family | Processo r | Virtualizatio n | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.g8h- vtpm- 2numa- hg-k10 | Hygon 4 | KVM | 256 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128, 192. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. Supports the vTPM feature. |
| ecs.g8h- vtpm- 2numa- hg-k25 | Hygon 4 | KVM | 256 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128, 192. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. Supports the vTPM feature. |
| ecs.g8m- 2numa- hg-k10 | Hygon 4 | KVM | 96 vCPU | 10 G | Supports NUMA ON configuration. Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 64. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8m- 2numa- hg-k25 | Hygon 4 | KVM | 96 vCPU | 25 G | Supports NUMA ON configuration. Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 64. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |

d instance families

| ecs.g8x- 2numa- hg-k10 | Hygon 4 | KVM | 128 vCPU | 10 G | Supports NUMA ON configuration. Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g8x- 2numa- hg-k25 | Hygon 4 | KVM | 128 vCPU | 25 G | Supports NUMA ON configuration. Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8v- 2numa- hg-k10 | Hygon 4 | KVM | 192 vCPU | 10 G | Supports NUMA ON configuration. Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8v- 2numa- hg-k25 | Hygon 4 | KVM | 192 vCPU | 25 G | Supports NUMA ON configuration. Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |

d instance families

| ecs.g8h- 2numa- hg-k10 | Hygon 4 | KVM | 256 vCPU | 10 G | Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128, 192. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g8h- 2numa- hg-k25 | Hygon 4 | KVM | 256 vCPU | 25 G | Supports ENI Trunking. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128, 192. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8h- hg-k25 | Hygon 4 | KVM | 256 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 128, 160, 192, 224, 242. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7m- hg-k10 | Hygon 3 | KVM | 96 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 86. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7m- hg-k25 | Hygon 3 | KVM | 96 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 86. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |

d instance families

| ecs.g7x- numaoff- hg-x25 | Hygon 3 | Third- generation Shenlong architecture | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g7x- numaon- hg-x25 | Hygon 3 | Third- generation Shenlong architecture | 128 vCPU | 25 G | Supports NUMA ON configuration. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 68, 128. Compute-to-memory ratios: 1:8. |
| ecs.g7x- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7x- numaon- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 48, 64. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7x- numaon- hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 48, 64. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7x- hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 118. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7s- numaon- hg-k25 | Hygon 3 | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |

d instance families

| ecs.g7s- numaon- hg-k10 | Hygon 3 | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g7s- hg-k25 | Hygon 3 | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 54. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g7s- hg-k10 | Hygon 3 | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 54. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g6s- hg-k10 | Hygon 2 | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g6s- hg-k25 | Hygon 2 | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g6x- hg-k10 | Hygon 2 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |

d instance families

| ecs.g6x- hg-k25 | Hygon 2 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.ghg | Hygon 1/2 | Second- generation Shenlong | 128 vCPU | 10 G, 25 G | Compute-to-memory ratio: 1:4. |

### 4.3 Heterogeneous computing

Hygon heterogeneous computing instances work with various accelerators, such as Hygon 1 and Hygon 3. These instances suit business scenarios including AI inference, computer vision, speech recognition and synthesis, machine translation, recommendation systems, real-time rendering, deep learning, and scientific computing. This topic describes the specific attributes, instance sizes, and virtualization technologies of the heterogeneous computing instance family.

| Instance family | Processo r | Virtualizatio n | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.gh8vv -2numa- hg-k10 | Hygon 4 | KVM | 192 vCPU | 10 G | Equipped with 8 Hygon DCU BW150 units. |
| ecs.gh8vv -2numa- hg-k25 | Hygon 4 | KVM | 192 vCPU | 25 G | Equipped with 8 Hygon DCU BW150 units. |
| ecs.gn7kx -hg-k10 | Hygon 2 | KVM | 128 vCPU | 10 G | Equipped with 2 NVIDIA A2 units. |
| ecs.gn7kx -hg-k25 | Hygon 2 | KVM | 128 vCPU | 25 G | Equipped with 2 NVIDIA A2 units. |
| ecs.gb7eh -2numa- hg-k10 | Hygon 4 | KVM | 256 vCPU | 10 G | Equipped with 8 Kunlun P800 units. |
| ecs.gb7eh -2numa- hg-k25 | Hygon 4 | KVM | 256 vCPU | 25 G | Equipped with 8 Kunlun P800 units. |

d instance families

| ecs.gn6ix- hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 4 NVIDIA T4 units. |
|---|---|---|---|---|---|
| ecs.gn6ix- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 4 NVIDIA T4 units. |
| ecs.gh7vh -2numa- hg-k25 | Hygon 4 | KVM | 256 vCPU | 25 G | Equipped with 8 Hygon DCU K100 AI units. |
| ecs.gh7vh -2numa- hg-k10 | Hygon 4 | KVM | 256 vCPU | 10 G | Equipped with 8 Hygon DCU K100 AI units. |
| ecs.gn7ix- hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 4 NVIDIA A10 units. |
| ecs.gn7ix- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 4 NVIDIA A10 units. |
| ecs.gh7ex -hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 8 Hygon DCU K100 units. |
| ecs.gh7ex -hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 8 Hygon DCU K100 units. |
| ecs.gc6ex -hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 2 Cambricon MLU 370 X8 units or 8 Cambricon MLU 370 X8 units. |
| ecs.gc6ex -hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 2 Cambricon MLU 370 X8 units or 8 Cambricon MLU 370 X8 units. |
| ecs.ge7ix- hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 8 Enflame I20 units. |
| ecs.ge7ix- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 8 Enflame I20 units. |
| ecs.ge7vx -hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 8 Enflame T20 units. |

d instance families

| ecs.ge7vx -hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 8 Enflame T20 units. |
|---|---|---|---|---|---|
| ecs.gt6ex- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 8 ILUVATAR BI-V150 units. |
| ecs.gt6ex- hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 8 ILUVATAR BI-V150 units. |
| ecs.gh7vx -hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 8 Hygon DCU K100-AI units. |
| ecs.gh7vx -hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 8 Hygon DCU K100-AI units. |
| ecs.gh6vx -hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Equipped with 2 or 8 Hygon DCU Z100L units. |
| ecs.gh6vx -hg-k10 | Hygon 3 | KVM | 128 vCPU | 10 G | Equipped with 2 or 8 Hygon DCU Z100L units. |
| ecs.gn6hv | Hygon 1 | KVM | 128 vCPU | 10 G, 25 G | Equipped with 1 to 2 NVIDIA V100 units. The computing-to- memory ratio is approximately 1:4. |

### 4.4 Local HDD

Local HDD instances are suitable for business scenarios such as mass storage and offline computing that have high requirements for big data computing, storage, and analysis and can meet the high requirements of distributed computing services such as Hadoop in terms of storage performance, storage capacity, and internal bandwidth. This topic describes the attributes, specifications, and virtualization technologies of instance families equipped with local HDDs.

| Instance family | Processor | Virtualization | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.dhg | Hygon 1/2 | KVM | 64 vCPU, 128 vCPU | 10 G, 25 G | Uses twelve 8-TB SATA HDDs. |

### 4.5 Local SSD

d instance families Local SSD instances are suitable for I/O-intensive applications that require high performance and low latency, such as NoSQL databases (including Cassandra and MongoDB), MPP data warehouses, distributed file systems, and search scenarios that use solutions such as Elasticsearch. This topic describes the attributes, specifications, and virtualization technologies of instance families equipped with local SSDs.

| Instance family | Processor | Virtualizat ion | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.i7x- 4x4t-hg- k10 | Hygon 3 | KVM | 128 vCPUs | 10 GB | An instance is equipped with four Non-Volatile Memory Express (NVMe) SSDs of 3,840 GB. |
| ecs.i7x- 4x4t-hg- k25 | Hygon 3 | KVM | 128 vCPUs | 25 GB | An instance is equipped with four NVMe SSDs of 3,840 GB. |

### 4.6 Super Computing Cluster

Super Computing Cluster (SCC) instance families provide computing cluster services with ultimate computing performance and parallel efficiency using high-speed InfiniBand networks on top of Elastic Compute Service (ECS) bare metal instances. SCC instance families are suitable for scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analytics, and audio and video processing. This topic describes the attributes, specifications, and virtualization technologies of SCC instance families.

> **Note:** SCCs are dedicated to HPC scenarios. To use SCCs, the hyper-threading feature must be disabled. However, the instance type is still calculated based on hyper-threading being enabled. Therefore, the number of CPU cores displayed in the operating system (GuestOS) is half of the defined instance type.

| Instance family | Processor | Virtualizat ion | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.sccg7x- roce-hg- x25-c1m4 | Hygon 3 | Third- generation SHENLONG architectur e | 128 vCPU | 25 G | Supports Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE) network interface controllers (NICs). |

### 4.7 Network-enhanced

d instance families Network-enhanced instance families are optimized for network-intensive scenarios. The network metrics of network-enhanced instance families are significantly higher than those of general-purpose instance families of the same generation. This ensures that networkenhanced instance families can meet the requirements of various scenarios. Networkenhanced instance families are especially suitable for scenarios that require higher network performance than general-purpose instance families. This topic describes the attributes, specifications, and virtualization technologies of network-enhanced instance families.

| Instance family | Processor | Virtualiza tion | Host threads | Network | Instance Family Description |
|---|---|---|---|---|---|
| ecs.ne8x- hg-k25 | Hygon 4 | KVM | 128 vCPU | 25 GB | Supports ENI trunking. Specification sizes (vCPU): 2, 4, 8, 16, 32, 64, and 72. Compute-to-memory ratios: 1:2, 1:4, 1:6, and 1:8. |
| ecs.ne8m- hg-k25 | Hygon 4 | KVM | 96 vCPU | 25 GB | Specification sizes (vCPU): 2, 4, 8, 16, 32, 64, and 72. Compute-to-memory ratios: 1:2, 1:4, 1:6, and 1:8. |
| ecs.ne7x- hg-k25 | Hygon 3 | KVM | 128 vCPU | 25 GB | Specification sizes (vCPU): 2, 4, 8, 16, 32, 64, 72, 96, and 104. Compute-to-memory ratios: 1:2, 1:4, 1:6, and 1:8. |

### 4.8 Storage-enhanced

Storage-enhanced instances optimize EBS-related capabilities, such as cloud disk bandwidth and cloud disk IOPS, and suit storage-intensive application scenarios. This article describes specific attributes, specification sizes, and virtualization technologiesof storage-enhanced instance families.

| Instance family | Processo r | Virtualizatio n | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.g8x-se- 2numa-hg- k25 | Hygon 4 | KVM | 128 vCPU | 25 G | Supports shared block storage. |

d instance families

| ecs.g7x-se- numaoff-hg- x25 | Hygon 3 | Third- generation Shenlong architecture | 128 vCPU | 25 G | Supports shared block storage. Specification sizes (vCPU): 16, 32, 128. Compute-to- memory ratio: 1:8. |
|---|---|---|---|---|---|
| ecs.g7x-se- 2numa-hg- k25 | Hygon 3 | KVM | 128 vCPU | 25 G | Supports shared block storage. |

sed instance families

## 5 Kunpeng-based instance families

**families**

### 5.1 Shared

Shared instance families suits business scenarios that do not require high virtual machine performance, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and general application services. This topic describes the attributes, specification sizes, and virtualization technologies of shared instance families.

| Instance family | Processo r | Virtualization | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.s8- numaon- kp-k | Kunpeng9 20 | KVM | 128 vCPUs, 160 vCPUs, 256 vCPUs | 10 G, 25 G | Supports NUMA ON configuration. Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.s5-kp- k | Kunpeng9 20 | KVM | 64 vCPUs, 96 vCPUs, 128 vCPUs | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. |
| ecs.gkp-s | Kunpeng9 20 | KVM | / | 10 G, 25 G | CPU-to-memory ratio: 1:4. |

### 5.2 Dedicated

Dedicated instances suit business scenarios that require high virtual machine performance, such as high packet forwarding rate scenarios, frontend servers, data analysis, batch computing, video encoding, and high-performance scientific and engineering applications. This topic describes the specific attributes, specification sizes, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualizatio n | Host threads | Networ k | Description |
|---|---|---|---|---|---|

sed instance families

| ecs.g8v- 2numa- kp-k25 | Kunpeng920 | KVM | 192 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g8v- 2numa- kp-k10 | Kunpeng920 | KVM | 192 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8h- 2numa- kp-k25 | Kunpeng920 | KVM | 256 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128, 192. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8h- 2numa- kp-k10 | Kunpeng920 | KVM | 256 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128, 192. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8x- 2numa- kp-k25 | Kunpeng920 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g8x- 2numa- kp-k10 | Kunpeng920 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128. Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8. |

sed instance families

| ecs.g5h- kp-k10 | Kunpeng920 | KVM | 256 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g5h- kp-k25 | Kunpeng920 | KVM | 256 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g5s- kp-k10 | Kunpeng920 | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g5s- kp-k25 | Kunpeng920 | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g5m- kp-k10 | Kunpeng920 | KVM | 96 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g5m- kp-k25 | Kunpeng920 | KVM | 96 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |

sed instance families

| ecs.g5x- kp-k10 | Kunpeng920 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
|---|---|---|---|---|---|
| ecs.g5x- kp-k25 | Kunpeng920 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g5m- kp-m10 | Kunpeng920 | Second- generation Shenlong architecture | 96 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.g5m- kp-m25 | Kunpeng920 | Second- generation Shenlong architecture | 96 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96. Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8. |
| ecs.gkp | Kunpeng920 | KVM | 96 vCPU | 10 G, 25 G | Compute-to-memory ratio: 1:4. |
| ecs.gkp- m | Kunpeng920 | Second- generation Shenlong architecture | / | 10 G, 25 G | Compute-to-memory ratio: 1:4. |

### 5.3 Local HDD

Instance families equipped with local HDDs are suitable for business scenarios such as mass storage and offline computing that have high requirements for big data computing, storage, and analysis and can meet the high requirements of distributed computing services such as Hadoop in terms of storage performance, storage capacity, and internal bandwidth. This topic describes the attributes, specifications, and virtualization technologies of instance families equipped with local HDDs. sed instance families

| Instance family | Processor | Virtual ization | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.dkp | Kunpeng920 | KVM | 64 vCPU, 96 vCPU | 10 Gbps, 25 Gbps | Equipped with twelve 8- TB SATA HDDs. |

### 5.4 Network-enhanced

Network-enhanced instances are optimized for network-intensive application scenarios. All network metrics improve significantly and exceed those of general-purpose instance families from the same generation, meeting vertical scenario requirements. This instance type is especially suitable for scenarios that require higher network performance than generalpurpose instances. This topic describes specific attributes, specification sizes, and virtualization technologies of network-enhanced instance families.

| Instance family | Process or | Virtuali zation | Host threads | Networ k | Description |
|---|---|---|---|---|---|
| ecs.ne5x-kp-k25 | Kunpeng 920 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 16, 32, 64, 72 Compute-to-memory ratios: 1:2, 1:4, 1:6, 1:8 |
| ecs.ne5m-kp- k25 | Kunpeng 920 | KVM | 96 vCPU | 25 G | Specification sizes (vCPU): 8, 12, 16, 24, 32, 40, 48, 56, 64, 72 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.ne5m-kp- k10 | Kunpeng 920 | KVM | 96 vCPU | 10 G | Specification sizes (vCPU): 8, 12, 16, 24, 32, 40, 48, 56, 64, 72 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |

ed instance families

## 6 Feiteng-based instance families

**families**

### 6.1 Shared

Shared instances suit business scenarios that do not require high virtual machine performance, such as small and medium-sized websites and web applications, development environments, build servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and general application services. This topic describes specific attributes, specification sizes, and virtualization technologies of shared instance families.

| Instance family | Processor | Virtualizatio n | Host threads | Network | Description |
|---|---|---|---|---|---|
| ecs.s7- 2numa-ft- k | FT-5000C-E | KVM | 160 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.s5-ft- k | FT-2000+ | KVM | 64 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.s6-ft- k | FT-S2500 | KVM | 128 vCPU | 10 G, 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |

### 6.2 Dedicated

Dedicated instances suit business scenarios that require high virtual machine performance, such as high packet forwarding rate scenarios, web frontend servers, data analysis, batch computing, video encoding, and high-performance scientific and engineering applications. This topic describes specific attributes, specification sizes, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualizatio n | Host threads | Network | Description |
|---|---|---|---|---|---|

ed instance families

| ecs.g7x- 2numa-ft- k10 | FT-5000C-E | KVM | 160 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128 Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8 |
|---|---|---|---|---|---|
| ecs.g7x- 2numa-ft- k25 | FT-5000C-E | KVM | 160 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 96, 128 Compute-to-memory ratios: 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.g7x- 8numa-ft- k10 | FT-5000C | KVM | 128 vCPU | 10 G | Supports ENI Trunking. Compute-to-memory ratios: 1:4, 2:7, 4:15, 8:30, 16:60, 24:90, 32:120, 48:180, 64:240, 96:360 |
| ecs.g6x- numaon- ft-k10 | FT-S2500 | KVM | 128 vCPU | 10 G | Supports NUMA ON configuration. |
| ecs.g6x- numaon- ft-k25 | FT-S2500 | KVM | 128 vCPU | 25 G | Supports NUMA ON configuration. |
| ecs.g5s-ft- k10 | FT-2000+ | KVM | 64 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.g5s-ft- k25 | FT-2000+ | KVM | 64 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |

ed instance families

| ecs.g6x-ft- k10 | FT-S2500 | KVM | 128 vCPU | 10 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
|---|---|---|---|---|---|
| ecs.g6x-ft- k25 | FT-S2500 | KVM | 128 vCPU | 25 G | Specification sizes (vCPU): 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120 Compute-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, 1:8 |
| ecs.gft | FT-2000+ | KVM | 64 vCPU | 10 G, 25 G | Compute-to-memory ratio: 1:4 |
