---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Elastic Compute Service Introduction to Instance Families and Instance Types"
product_version: "V3.16.2"
doc_version: "20230419"
pdf_pages: 36
source_pdf: "0e2e86306258647e_Alibaba Cloud Apsara Stack Enterprise v3.16.2 Elastic Compute Service Introduction to Instance Famil"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.16.2/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Elastic%20Compute%20Service%20Introduction%20to%20Instance%20Families%20and%20Instance%20Types%2020230419.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Elastic Compute Service Introduction to Instance Families and Instance Types

## Table of Contents

- 1 Instance families and instance types
- 2 Intel-based instance families
  - 2.1 Shared instance families
  - 2.2 Dedicated instance families
  - 2.3 ECS Bare Metal Instance families
  - 2.4 Heterogeneous computing and heterogeneous ECS Bare Metal Instance families
  - 2.5 SCC instance families
  - 2.6 Instance families equipped with local HDDs
  - 2.7 Burstable instance families
- 3 Hygon-based instance families
  - 3.1 Shared instance families
  - 3.2 Dedicated instance families
  - 3.3 Heterogeneous computing instance families
  - 3.4 Instance families equipped with local HDDs
- 4 Kunpeng-based instance families
  - 4.1 Shared instance families
  - 4.2 Dedicated instance families
  - 4.3 Instance families equipped with local HDDs
- 5 Feiteng-based instance families
  - 5.1 Shared instance families
  - 5.2 Dedicated instance families

lies and instance types

## 1 Instance families and instance types

**types**

Alibaba Cloud Elastic Compute Service (ECS) instances are categorized into different instance families based on the business and use scenarios for which they are suited. ECS instance families include shared instance families, dedicated instance families, ECS Bare Metal Instance families, instance families equipped with local HDDs, instance families equipped with local SSDs, heterogeneous computing instance families, and Super Computing Cluster (SCC) instance families. Each instance family consists of one or more instance types that share similar attributes.

**Instance families**

The following table describes the instance families and their use scenarios.

| Instance family | Use scenario |
|---|---|
| Shared instance families | Shared instance families are suitable for business scenarios where performance requirements are not high, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and integrated application services. |
| Dedicated instance families | Dedicated instance families are suitable for business scenarios that require high performance, such as web frontend servers, data analysis, batch processing, video encoding, high-performance scientific and engineering applications, and scenarios where large volumes of packets are received and transmitted. |
| ECS Bare Metal Instance families | ECS Bare Metal Instance families provide robust compute, storage, and network configurations for business scenarios that require dedicated resources, security isolation, and high performance, such as containers, databases, core business of enterprises, and big data computing. |
| Instance families equipped with local HDDs | Instance families equipped with local HDDs are suitable for business scenarios such as mass storage and offline computing that have high requirements for big data computing, storage, and analysis and can meet the high requirements of distributed computing services such as Hadoop in terms of storage performance, storage capacity, and internal bandwidth. |
| Instance families equipped with local SSDs | Instance families equipped with local SSDs are suitable for I/O-intensive applications that require high performance and low latency, such as NoSQL databases (including Cassandra and MongoDB), MPP data warehouses, distributed file systems, and search scenarios that use solutions such as Elasticsearch. |

lies and instance types

| Instance family | Use scenario |
|---|---|
| Heterogeneous computing instance families | Heterogeneous computing instance families use various accelerators including NVIDIA T4 GPUs, NVIDIA V100 GPUs, and FPGAs, and are suitable for business scenarios such as artificial intelligence (AI) inference, computer vision, speech recognition, speech synthesis, machine translation, recommendation systems, real-time rendering, deep learning, and scientific computing applications. |
| SCC instance families | SCC instance families provide computing cluster services with ultimate computing performance and parallel efficiency by using the high-speed InfiniBand network on top of ECS Bare Metal Instance families. SCC instance families are suitable for scenarios such as high-performance computing, AI, machine learning, scientific and engineering computing, data analysis, and audio and video processing. |
| Burstable instance families | Burstable instance families provide a baseline level of CPU performance with the ability to burst above the baseline by spending CPU credits. They are suitable for business scenarios where performance requirements are not high, such as web applications and small and medium-sized websites. |

**Instance types**

An instance family can be categorized into multiple instance types based on their vCPU and memory specifications. ECS instance types define the basic attributes of instances, such as the number of vCPUs, memory size, network capabilities, and storage capabilities. Network capabilities include the network bandwidth, packet forwarding rate, maximum number of elastic network interfaces (ENIs) per instance, and maximum number of IP addresses per ENI. Storage capabilities include the maximum disk bandwidth, maximum disk IOPS, and maximum number of attached disks per instance. The network and storage performance of instances within the same instance family depend on their computing capacities. The larger computing capacity the instances have, the higher network and storage performance the instances can deliver. lies and instance types The following figure shows the naming conventions of ECS instance types. Each instance type name consists of the following parts: Service name: Each instance type name starts with ecs., which indicates ECS. Instance family name: Examples: s6-k and g6x-k10. In s6-k, s indicates the shared instance family, 6 indicates the sixth generation, and k indicates Kernel-based Virtual Machine (KVM) virtualization. In g6x-k10, g indicates the dedicated instance family, 6 indicates the sixth generation, x indicates the use of 128 logical cores, and k10 indicates the use of KVM and 10 Gbit/s networks. CPU-to-memory ratio: For example, c1m2 indicates a CPU-to-memory ratio of 1:2, such as a configuration of 2 vCPUs and 4 GiB of memory, or 4 vCPUs and 8 GiB of memory. Number of vCPUs: For example, large indicates 2 vCPUs per instance, xlarge indicates 4 vCPUs per instance, 2xlarge indicates 8 vCPUs per instance, and 3xlarge indicates 12 vCPUs per instance. The following section describes the columns of the tables in the topics about Intel-, Hygon-, Kunpeng-, and Feiteng-based instance families. Instance family: the name of the instance family. Processor: the model of the processor supported and recommended for the instance family. For example, Intel V6 represents Intel Cascade Lake processors. Virtualization: the virtualization technology used by the instance family, including KVM, firstgeneration SHENLONG architecture, second-generation SHENLONG architecture, and thirdgeneration SHENLONG architecture. lies and instance types Physical machine vCPUs: the number of hyperthreads on an X86-based host or the number of logic cores on an ARM-based host. This number is represented by the number of vCPUs. In the same network environment, the network capability of a single vCPU varies on physical machines that have different numbers of vCPUs. The number of vCPUs is specified for the most recent non-shared instance types to provide a better quality of service (QoS). Unlimited indicates that the number of vCPUs is not specified. Network: the network configurations of a host. On the same physical machine, the network capability of a single vCPU varies based on network configurations. Network configurations are specified for the most recent non-shared instance types to provide a better QoS. 10 G indicates that the instance family is used in a 2 × 10 Gbit/s network, and 25 G indicates that the instance family is used in a 2 × 25 Gbit/s network. Unlimited indicates that network configurations are not specified. Description: the characteristics of the instance family, such as the number of vCPUs, computeto-memory ratios, GPUs, and attached disks. Remarks: indicates whether the instance family is suitable for new customers. Not recommended indicates that the instance family is not recommended for new customers.

**Resource allocation**

Resources are allocated differently to ECS instances of different types. For all KVM-based instances, CPU and memory resources must be reserved for virtualization. For example, 8 vCPUs and 32 GiB of memory, 10 vCPUs and 40 GiB of memory, or 10 vCPUs and 48 GiB of memory must be reserved to handle network virtualization, storage virtualization, and system control tasks. For all instances that use SHENLONG architecture, no CPU or memory resources need to be reserved for the server. SHENLONG architecture integrates software and hardware and offloads network virtualization, storage virtualization, and system control to a dedicated chip system to achieve zero resource overheads and prevent the performance of virtual machines from fluctuating when demand outstrips resource supplies at the underlying layer. Resources of the memory and local disks in hosts cannot be overprovisioned. CPU resources of hosts that host shared and burstable instances can be overprovisioned. We recommend that you keep the overprovisioning ratio below 4. CPU resources of hosts that host other instances cannot be overprovisioned.

## 2 Intel-based instance families

### 2.1 Shared instance families

Shared instance families are suitable for business scenarios where performance requirements are not high, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and integrated application services. This topic describes the attributes, specifications, and virtualization technologies of shared instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.s6-k | Intel V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.s6-m | Intel V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.s7-k | Intel V7 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |

| ecs.anysh are | Intel | KVM | Unlimited | Unlimit ed | Allows you to create, modify, and delete custom instance types in the Apsara Uni-manager Operations Console. Custom instance types are all shared instance types and support only Intel processors. | Not recom mende d |
|---|---|---|---|---|---|---|
| ecs.s6 | Intel V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, and 8. CPU-to-memory ratios: 1:1, 1:2, 1:4, and 1:8. | Not recom mende d |
| ecs.xn4 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | Provides only the ecs.xn4.small instance type with 1 vCPU and 1 GiB of memory. | Not recom mende d |
| ecs.n4 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, 8, 16, and 32. CPU-to-memory ratio: 1:2. | Not recom mende d |
| ecs.mn4 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, 8, 16, and 32. CPU-to-memory ratio: 1:4. | Not recom mende d |
| ecs.e4 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, 8, and 16. CPU-to-memory ratio: 1:8. | Not recom mende d |

| ecs.xn4v2 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | Provides the ecs.xn4.small instance type with 1 vCPU and 1 GiB of memory. Supports IPv6 addresses. | Not recom mende d |
|---|---|---|---|---|---|---|
| ecs.n4v2 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, 8, 16, and 32. CPU-to-memory ratio: 1:2. Supports IPv6 addresses. | Not recom mende d |
| ecs.mn4v 2 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, 8, 16, and 32. CPU-to-memory ratio: 1:4. Supports IPv6 addresses. | Not recom mende d |
| ecs.e4v2 | Intel V4/V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 1, 2, 4, 8, and 16. CPU-to-memory ratio: 1:8. Supports IPv6 addresses. | Not recom mende d |

### 2.2 Dedicated instance families

Dedicated instance families are suitable for business scenarios that require high performance, such as scenarios where large volumes of packets are received and transmitted, web frontend servers, data analysis, batch processing, video encoding, and high-performance scientific and engineering applications. This topic describes the attributes, specifications, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|

| ecs.g7x- se-x25 | Intel V7 | Third- generatio n SHENLON G architect ure | 128 | 25 G | Supports Shared Block Storage. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g7x- x25 | Intel V7 | Third- generatio n SHENLON G architect ure | 128 | 25 G | None. | Recom mende d |
| ecs.g7s- k10 | Intel V7 | KVM | 64 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 54. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.g7s- k25 | Intel V7 | KVM | 64 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 54. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.g7m- k10 | Intel V7 | KVM | 96 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 86. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |

| ecs.g7m- k25 | Intel V7 | KVM | 96 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 86. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g7x- k10 | Intel V7 | KVM | 128 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.g7x- k25 | Intel V7 | KVM | 128 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 118. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.g7v- k10 | Intel V7 | KVM | 192 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.g7v- k25 | Intel V7 | KVM | 192 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |

| ecs.g6s- m10 | Intel V6 | Second- generatio n SHENLON G architect ure | 64 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Not recom mende d |
|---|---|---|---|---|---|---|
| ecs.g6s- m25 | Intel V6 | Second- generatio n SHENLON G architect ure | 64 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Not recom mende d |
| ecs.g6m- m10 | Intel V6 | Second- generatio n SHENLON G architect ure | 96 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Not recom mende d |
| ecs.g6m- m25 | Intel V6 | Second- generatio n SHENLON G architect ure | 96 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Not recom mende d |
| ecs.g6s- k10 | Intel V6 | KVM | 64 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |

| ecs.g6s- k25 | Intel V6 | KVM | 64 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g6m- k10 | Intel V6 | KVM | 96 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 88. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.g6m- k25 | Intel V6 | KVM | 96 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 88. CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |
| ecs.c6 | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 52, 64, and 104. CPU-to-memory ratio: 1:2. | Recom mende d |
| ecs.g6 | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 52, 64, and 104. CPU-to-memory ratio: 1:4. | Recom mende d |
| ecs.r6 | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 52, 64, and 104. CPU-to-memory ratio: 1:8. | Recom mende d |

| ecs.re6 | Intel V6 | Second- generatio n SHENLON G architect ure | 208 | Unlimit ed | Offers 3 TB of memory and a CPU-to-memory ratio of 1:15. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.sn1 | Intel V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 16, 32, and 56. CPU-to-memory ratio: 1:2. | Not recom mende d |
| ecs.sn2 | Intel V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 16, 32, and 56. CPU-to-memory ratio: 1:4. | Not recom mende d |
| ecs.se1 | Intel V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 16, 32, and 56. CPU-to-memory ratio: 1:8. | Not recom mende d |
| ecs.sn1ne | Intel V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, and 88. CPU-to-memory ratio: 1:2. Supports IPv6 addresses. | Not recom mende d |
| ecs.sn2ne | Intel V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 56, and 88. CPU-to-memory ratio: 1:4. Supports IPv6 addresses. | Not recom mende d |

| ecs.se1ne | Intel V5/V6 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 56, and 88. CPU-to-memory ratio: 1:8. Supports IPv6 addresses. | Not recom mende d |
|---|---|---|---|---|---|---|
| ecs.c5 | Intel V5 | Second- generatio n SHENLON G architect ure | 104 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 64, 86, and 88. CPU-to-memory ratio: 1:2. | Not recom mende d |
| ecs.g5 | Intel V5 | Second- generatio n SHENLON G architect ure | 104 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 64, 86, and 88. CPU-to-memory ratio: 1:4. | Not recom mende d |
| ecs.r5 | Intel V5 | Second- generatio n SHENLON G architect ure | 104 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 64, 86, and 88. CPU-to-memory ratio: 1:8. | Not recom mende d |
| ecs.re5 | Intel V5 | KVM | 192 | Unlimit ed | Offers 3 TB of memory and a CPU-to-memory ratio: 1:16. | Not recom mende d |

### 2.3 ECS Bare Metal Instance families

Elastic Compute Service (ECS) Bare Metal Instance families provide robust compute, storage, and network configurations for business scenarios that require dedicated resources, security isolation, and high performance, such as containers, databases, core business of enterprises, and big data computing. This topic describes the attributes, specifications, and virtualization technologies of ECS Bare Metal Instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.ebmg 7s-se- x25-c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 64 | 25 G | Provides the ecs.ebmg7s-se-x25- c1m8.16xlarge instance type with 64 vCPUs and 512 GiB of memory. Supports Shared Block Storage and allows you to enable NUMA mode. | Recom mende d |
| ecs.ebmg 7m-se- x25-c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 96 | 25 G | Provides the ecs.ebmg7m-se-x25- c1m8.24xlarge instance type with 96 vCPUs and 768 GiB of memory. Supports Shared Block Storage and allows you to enable NUMA mode. | Recom mende d |
| ecs.ebmg 7x-se- x25-c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 128 | 25 G | Provides the ecs.ebmg7x-se-x25- c1m8.32xlarge instance type with 128 vCPUs and 1,024 GiB of memory. Supports Shared Block Storage and allows you to enable NUMA mode. | Recom mende d |

| ecs.ebmg 7s-se- numaoff- x25-c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 64 | 25 G | Provides the ecs.ebmg7s-se- numaoff-x25- c1m8.16xlarge instance type with 64 vCPUs and 512 GiB of memory. Supports Shared Block Storage and allows you to disable NUMA mode. | Not recom mende d |
|---|---|---|---|---|---|---|
| ecs.ebmg 7m-se- numaoff- x25-c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 96 | 25 G | Provides the ecs.ebmg7m-se- numaoff-x25- c1m8.24xlarge instance type with 96 vCPUs and 768 GiB of memory. Supports Shared Block Storage and allows you to disable NUMA mode. | Not recom mende d |
| ecs.ebmg 7x-se- numaoff- x25-c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 128 | 25 G | Provides the ecs.ebmg7x-se- numaoff-x25- c1m8.32xlarge instance type with 128 vCPUs and 1,024 GiB of memory. Supports Shared Block Storage and allows you to disable NUMA mode. | Not recom mende d |
| ecs.ebmg 7s-x25- c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 64 | 25 G | Provides the ecs.ebmg7s-x25- c1m8.16xlarge instance type with 64 vCPUs and 512 GiB of memory and allows you to enable NUMA mode. | Recom mende d |

| ecs.ebmg 7m-x25- c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 96 | 25 G | Provides the ecs.ebmg7m-x25- c1m8.24xlarge instance type with 96 vCPUs and 768 GiB of memory and allows you to enable NUMA mode. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.ebmg 7x-x25- c1m8 | Intel V7 | Third- generatio n SHENLON G architect ure | 128 | 25 G | Provides the ecs.ebmg7x-x25- c1m8.32xlarge instance type with 128 vCPUs and 1,024 GiB of memory and allows you to enable NUMA mode. | Recom mende d |
| ecs.ebmg 6s-m10- c1m4 | Intel V6 | Second- generatio n SHENLON G architect ure | 64 | 10 G | Provides the ecs.ebmg6s-m10- c1m4.16xlarge instance type with 64 vCPUs and 256 GiB of memory. | Recom mende d |
| ecs.ebmg 6s-m25- c1m4 | Intel V6 | Second- generatio n SHENLON G architect ure | 64 | 25 G | Provides the ecs.ebmg6s-m25- c1m4.16xlarge instance type with 64 vCPUs and 256 GiB of memory. | Recom mende d |
| ecs.ebmg 6s-m10- c1m24 | Intel V6 | Second- generatio n SHENLON G architect ure | 64 | 10 G | Provides the ecs.ebmg6s-m10- c1m24.16xlarge instance type with 64 vCPUs and 1,536 GiB of memory. | Recom mende d |
| ecs.ebmg 6s-m25- c1m24 | Intel V6 | Second- generatio n SHENLON G architect ure | 64 | 25 G | Provides the ecs.ebmg6s-m25- c1m24.16xlarge instance type with 64 vCPUs and 1,536 GiB of memory. | Recom mende d |

| ecs.ebmg 6m-m10- c1m4 | Intel V6 | Second- generatio n SHENLON G architect ure | 96 | 10 G | Provides the ecs.ebmg6m-m10- c1m4.24xlarge instance type with 96 vCPUs and 384 GiB of memory. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.ebmg 6m-m25- c1m4 | Intel V6 | Second- generatio n SHENLON G architect ure | 96 | 10 G | Provides the ecs.ebmg6m-m25- c1m4.24xlarge with 96 vCPUs and 384 GiB of memory. | Recom mende d |
| ecs.ebmr e6-3t | Intel V6 | Second- generatio n SHENLON G architect ure | 208 | 25 G | Provides the ecs.ebmre6-3t.52xlarge with 208 vCPUs and 3,072 GiB of memory. | Recom mende d |
| ecs.ebmc 6 | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | Provides the ecs.ebmc6.26xlarge instance type with 104 vCPUs and 192 GiB of memory. | Recom mende d |
| ecs.ebmg 6 | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | Provides the ecs.ebmg6.26xlarge instance type with 104 vCPUs and 384 GiB of memory. | Recom mende d |
| ecs.ebmr 6 | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | Provides the ecs.ebmr6.26xlarge instance type with 104 vCPUs and 768 GiB of memory. | Recom mende d |

| ecs.ebmr e6p | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | 25 G | Uses 1,536 GiB of Intel Optane persistent memory (AEP). | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.ebmg 5 | Intel V5 | First- generatio n SHENLON G architect ure | 96 | 10 G | Provides the ecs.ebmg5.24xlarge instance type with 96 vCPUs and 384 GiB of memory. | Not recom mende d |
| ecs.ebmg 5s | Intel V5 | Second- generatio n SHENLON G architect ure | 96 | 25 G | Provides the ecs.ebmg5s.24xlarge instance type with 96 vCPUs and 384 GiB of memory. | Not recom mende d |

### 2.4 Heterogeneous computing and heterogeneous ECS Bare Metal Instance families

**heterogeneous ECS Bare Metal Instance**

**families**

Heterogeneous computing instance families and heterogeneous ECS Bare Metal Instance families use various accelerators including NVIDIA T4 GPUs, NVIDIA V100 GPUs, and FPGAs, and are suitable for business scenarios such as AI inference, computer vision, speech recognition, speech synthesis, machine translation, recommendation systems, real-time rendering, deep learning, and scientific computing applications. This topic describes the attributes, specifications, and virtualization technologies of heterogeneous computing instance families and heterogeneous ECS Bare Metal Instance families.

| Instance family | Processor | Virtualiza tion | vCPUs of physical server | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.gn6i | Intel V5 and V6 | KVM | Unlimited | Unlimit ed | Uses one to eight NVIDIA T4 GPUs and offers a CPU-to- memory ratio of 1:4 | Recom mende d |

| ecs.gn6v | Intel V5 and V6 | KVM | Unlimited | Unlimit ed | Uses one to eight NVIDIA V100 GPUs and offers a CPU-to- memory ratio of 1:4 | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.vgn6i | Intel V5 and V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | Uses vGPUs Supports the 1/4 and 1/2 compute capacity of NVIDIA Tesla T4 GPUs | Recom mende d |
| ecs.ebmg n6i | Intel V5 and V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | ECS Bare Metal Instance family that uses four NVIDIA T4 GPUs | Recom mende d |
| ecs.ebmg n6i-2 | Intel V5 and V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | ECS Bare Metal Instance family that uses two NVIDIA T4 GPUs | Recom mende d |
| ecs.ebmg n6i-8 | Intel V5 and V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | ECS Bare Metal Instance family that uses eight NVIDIA T4 GPUs | Recom mende d |
| ecs.ebmg n6e-2 | Intel V6 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | ECS Bare Metal Instance family that uses two NVIDIA V100 GPUs | Recom mende d |

| ecs.gn3 | Intel V4 | KVM | Unlimited | Unlimit ed | Uses one to two NVIDIA K2 GPUs | Not recom mende d |
|---|---|---|---|---|---|---|
| ecs.gn4 | Intel V4 | KVM | Unlimited | Unlimit ed | Uses one to two NVIDIA M40 GPUs | Not recom mende d |
| ecs.gn5 | Intel V4 | KVM | Unlimited | Unlimit ed | Uses one to eight NVIDIA P100 GPUs | Not recom mende d |
| ecs.gn5e | Intel V5 | KVM | Unlimited | Unlimit ed | Uses one to eight NVIDIA P4 GPUs and offers a CPU-to- memory ratio of 1:6 | Not recom mende d |
| ecs.gn5i | Intel V4 | KVM | Unlimited | Unlimit ed | Uses one to eight NVIDIA P4 GPUs and offers a CPU-to- memory ratio of 1:4 | Not recom mende d |
| ecs.gn5t | Intel V4 | KVM | Unlimited | Unlimit ed | Uses two to eight NVIDIA 1080Ti GPUs and offers a CPU-to- memory ratio of 1:4 | Not recom mende d |

### 2.5 SCC instance families

Super Computing Cluster (SCC) instance families provide computing cluster services with ultimate computing performance and parallel efficiency by using the high-speed InfiniBand network on top of Elastic Compute Service (ECS) Bare Metal Instance families. SCC instance families are suitable for scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analysis, and audio and video processing. This topic describes the attributes, specifications, and virtualization technologies of SCC instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|

| ecs.sccgn 6e | Intel V6 | Second- generatio n SHENLON G architect ure | 104 | Unlimit ed | Uses eight NVIDIA V100 GPUs and a 100 Gbit/s InfiniBand network. | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.sccgn 6p | Intel V5/V6 | Second- generatio n SHENLON G architect ure | 96 | Unlimit ed | Uses eight NVIDIA V100 GPUs and a 100 Gbit/s InfiniBand network. | Recom mende d |
| ecs.scch5 | Intel V5 | Second- generatio n SHENLON G architect ure | 64 | Unlimit ed | Uses processors with high clock speeds that deliver a base frequency of 3.1 GHz and an all-core turbo frequency of 3.5 GHz. | Not recom mende d |
| ecs.sccg5i b | Intel V5 | First- generatio n SHENLON G architect ure | 96 | 10 G | Uses a 100 Gbit/s InfiniBand network. | Not recom mende d |

### 2.6 Instance families equipped with local HDDs

**local HDDs**

Instance families equipped with local HDDs are suitable for business scenarios such as mass storage and offline computing that have high requirements for big data computing, storage, and analysis and can meet the high requirements of distributed computing services such as Hadoop in terms of storage performance, storage capacity, and internal bandwidth. This topic describes the attributes, specifications, and virtualization technologies of instance families equipped with local HDDs.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|

| ecs.d7s- k10-8t | Intel V7 | KVM | 64 | 10 G | Uses twelve 8-TB SATA HDDs | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.d7s- k25-8t | Intel V7 | KVM | 64 | 25 G | Uses twelve 8-TB SATA HDDs. | Recom mende d |
| ecs.d7m- k10-8t | Intel V7 | KVM | 96 | 10 G | Uses twelve 8-TB SATA HDDs. | Recom mende d |
| ecs.d7m- k25-8t | Intel V7 | KVM | 96 | 25 G | Uses twelve 8-TB SATA HDDs. | Recom mende d |
| ecs.d7x- k10-12t | Intel V7 | KVM | 128 | 10 G | Uses twelve 12-TB SATA HDDs. | Recom mende d |
| ecs.d7x- k25-12t | Intel V7 | KVM | 128 | 25 G | Uses twelve 12-TB SATA HDDs. | Recom mende d |
| ecs.d2- zyy | Intel V5/V6 | KVM | Unlimited | Unlimit ed | Uses twelve 8-TB SATA HDDs. | Recom mende d |

### 2.7 Burstable instance families

Burstable instance families provide baseline CPU performance and are burstable but limited by accrued CPU credits. They are suitable for business scenarios that do not require high performance of virtual machines, such as web applications and small and medium-sized websites. This topic describes the attributes, specifications, and virtualization technologies of burstable instance families.

| Instance family | Processo r | Virtualiz ation | vCPUs of physical server | Network | Description | Remarks |
|---|---|---|---|---|---|---|

| ecs.t5 | Intel V5 and V6 | KVM | Unlimited | Unlimite d | Provides baseline CPU performance and is burstable but limited by accrued CPU credits. | Not recomme nded. Shared instance families are recomme nded. |
|---|---|---|---|---|---|---|

instance families

## 3 Hygon-based instance families

### 3.1 Shared instance families

Shared instance families are suitable for business scenarios that do not require high performance of virtual machines, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and integrated application services. This topic describes the attributes, specifications, and virtualization technologies of shared instance families.

| Instance family | Processor | Virtualiza tion | vCPUs of physical server | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.s6- hg-k | Hygon 2 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64 | Recom mende d |
| ecs.ghg-s | Hygon 1 and Hygon 2 | KVM | Unlimited | Unlimit ed | CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Not recom mende d |

### 3.2 Dedicated instance families

Dedicated instance families are suitable for business scenarios that require high performance, such as scenarios where large volumes of packets are received and transmitted, web frontend servers, data analysis, batch processing, video encoding, and high-performance scientific and engineering applications. This topic describes the attributes, specifications, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.g6s- hg-k10 | Hygon 2 | KVM | 64 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8. | Recom mende d |

instance families

| ecs.g6s- hg-k25 | Hygon 2 | KVM | 64 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g6x- hg-k10 | Hygon 2 | KVM | 128 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 120 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g6x- hg-k25 | Hygon 2 | KVM | 128 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 120 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.ghg | Hygon 1 and Hygon 2 | KVM | Unlimited | Unlimit ed | CPU-to-memory ratio: 1:4 | Not recom mende d |

### 3.3 Heterogeneous computing instance families

**families**

Heterogeneous computing instance families use various accelerators including NVIDIA T4 GPUs, NVIDIA V100 GPUs, and FPGAs, and are suitable for business scenarios such as AI inference, computer vision, speech recognition, speech synthesis, machine translation, recommendation systems, real-time rendering, deep learning, and scientific computing applications. This topic describes the attributes, specifications, and virtualization technologies of heterogeneous computing instance families.

| Instance family | Processor | Virtualiza tion | vCPUs of physical server | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|

instance families

| ecs.gn6ih | Hygon 2 | KVM | 128 vCPUs | Unlimit ed | Uses eight NVIDIA T4 GPUs and offers a CPU- to-memory ratio of 1:4 | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.gn6hv | Hygon 1 | KVM | 128 vCPUs | Unlimit ed | Uses one to two NVIDIA V100 GPUs and offers a CPU-to-memory ratio of 1:4 | Recom mende d |

### 3.4 Instance families equipped with local HDDs

**local HDDs**

Instance families equipped with local HDDs are suitable for business scenarios that have high requirements for big data computing, storage, and analysis, such as mass storage and offline computing scenarios, and can also meet the high requirements of distributed computing services such as Hadoop in terms of storage performance, storage capacity, and internal bandwidth. This topic describes the attributes, specifications, and virtualization technologies of instance families equipped with local HDDs.

| Instance family | Processor | Virtualiza tion | vCPUs of physical server | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.dhg | Hygon 1 and Hygon 2 | KVM | Unlimited | Unlimit ed | Uses twelve 8-TB SATA HDDs | Recom mende d |

ed instance families

## 4 Kunpeng-based instance families

**families**

### 4.1 Shared instance families

Shared instance families are suitable for business scenarios that do not require high performance of virtual machines, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and integrated application services. This topic describes the attributes, specifications, and virtualization technologies of shared instance families.

| Instance family | Processor | Virtualiz ation | vCPUs of physical server | Networ k | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.s5- kp-k | Kunpeng9 20 | KVM | Unlimited | Unlimit ed | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.gkp-s | Kunpeng9 20 | KVM | Unlimited | Unlimit ed | CPU-to-memory ratio: 1:4 | Not recom mende d |

### 4.2 Dedicated instance families

Dedicated instance families are suitable for business scenarios that require high performance, such as scenarios where large volumes of packets are received and transmitted, web frontend servers, data analysis, batch processing, video encoding, and high-performance scientific and engineering applications. This topic describes the attributes, specifications, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|

ed instance families

| ecs.g5s- kp-k10 | Kunpeng9 20 | KVM | 64 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g5s- kp-k25 | Kunpeng9 20 | KVM | 64 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g5m- kp-k10 | Kunpeng9 20 | KVM | 96 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 88 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g5m- kp-k25 | Kunpeng9 20 | KVM | 96 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, and 88 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g5x- kp-k10 | Kunpeng9 20 | KVM | 128 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 120 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g5x- kp-k25 | Kunpeng9 20 | KVM | 128 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 120 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |

ed instance families

| ecs.g5m- kp-m10 | Kunpeng9 20 | Second- generatio n SHENLON G architect ure | 96 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g5m- kp-m25 | Kunpeng9 20 | Second- generatio n SHENLON G architect ure | 96 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, and 96 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.gkp | Kunpeng9 20 | KVM | Unlimited | Unlimit ed | CPU-to-memory ratio: 1:4 | Not recom mende d |
| ecs.gkp-m | Kunpeng9 20 | Second- generatio n SHENLON G architect ure | Unlimited | Unlimit ed | CPU-to-memory ratio: 1:4 | Not recom mende d |

### 4.3 Instance families equipped with local HDDs

**local HDDs**

Instance families equipped with local HDDs are suitable for business scenarios that have high requirements for big data computing, storage, and analysis, such as mass storage and offline computing scenarios, and can also meet the high requirements of distributed computing services such as Hadoop in terms of storage performance, storage capacity, and internal bandwidth. This topic describes the attributes, specifications, and virtualization technologies of instance families equipped with local HDDs.

| Document V | ersion: 20230419 |   |   |   |   | 3 |
|---|---|---|---|---|---|---|

ed instance families

| Instance family | Processor | Virtual ization | vCPUs of physical server | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|
| ecs.dkp | Kunpeng920 | KVM | Unlimited | Unlimit ed | Uses twelve 8-TB SATA HDDs | Recom mende d |

d instance families

## 5 Feiteng-based instance families

### 5.1 Shared instance families

Shared instance families are suitable for business scenarios that do not require high performance of virtual machines, such as small and medium-sized websites and web applications, development environments, servers, code repositories, microservices, testing and staging environments, lightweight databases, lightweight enterprise applications, and integrated application services. This topic describes the attributes, specifications, and virtualization technologies of shared instance families.

| Instance family | Processor | Virtual ization | vCPUs of physical server | Netwo rk | Description | Remarks |
|---|---|---|---|---|---|---|
| ecs.s5- ft-k | FT-2000+ | KVM | Unlimited | Unlimi ted | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recomme nded |
| ecs.s6- ft-k | FT-S2500 | KVM | Unlimited | Unlimi ted | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, and 64 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recomme nded |

### 5.2 Dedicated instance families

Dedicated instance families are suitable for business scenarios that require high performance, such as scenarios where large volumes of packets are received and transmitted, web frontend servers, data analysis, batch processing, video encoding, and high-performance scientific and engineering applications. This topic describes the attributes, specifications, and virtualization technologies of dedicated instance families.

| Instance family | Processor | Virtualiza tion | Physical machine vCPUs | Netwo rk | Description | Remar ks |
|---|---|---|---|---|---|---|

d instance families

| ecs.g5s- ft-k10 | FT-2000+ | KVM | 64 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
|---|---|---|---|---|---|---|
| ecs.g5s- ft-k25 | FT-2000+ | KVM | 64 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, and 56 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g6x- ft-k10 | FT-S2500 | KVM | 128 | 10 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 120 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.g6x- ft-k25 | FT-S2500 | KVM | 128 | 25 G | vCPUs: 2, 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, and 120 CPU-to-memory ratios: 1:1, 1:2, 1:3, 1:4, 1:6, and 1:8 | Recom mende d |
| ecs.gft | FT-2000+ | KVM | Unlimited | Unlimit ed | CPU-to-memory ratio: 1:4 | Not recom mende d |
