---
title: "Bare Metal Computing Platform Product Introduction 20250930"
product_version: "V3.18.6"
pdf_pages: 13
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Bare Metal Computing Platform Product Introduction 20250930.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%A3%B8%E9%87%91%E5%B1%9E%E7%AE%97%E5%8A%9B%E5%B9%B3%E5%8F%B0BMCP/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Bare%20Metal%20Computing%20Platform%20Product%20Introduction%2020250930.pdf"
converter: line-classifier (PyMuPDF)
---

# Bare Metal Computing Platform Product Introduction 20250930

Bare Metal Computing Platform P ls

## Product details

BareMetal Computing Platform (BMCP) is an AI Infrastructure as a Service (IaaS) platform that provides unified management and provisioning of computing power. It is a large-scale, highperformance computing power management platform built on Apsara Stack. BMCP offers diverse, high-performance computing cluster services, such as bare metal and container clusters. It provides highly scalable, high-performance, and cost-effective infrastructure services for large-scale, distributed AI research and development (R&D) scenarios, such as Natural Language Processing (NLP) and general large models. It offers various computing services, such as bare metal clusters, container clusters, and AI platform services, to meet diverse user requirements. BMCP lets you manage your existing high-performance computing clusters. It uses cloudbased resource management to help you migrate intelligent computing workloads to the cloud. Bare Metal Computing Platform P

## Benefits

The BMCP platform offers the following key features and benefits:
1. High performance: Bare metal servers deliver the full performance of the underlying
hardware without a virtualization layer. This allows compute-intensive and storageintensive applications to execute more efficiently.
2. Dedicated resources: You have exclusive access to physical server resources. This
eliminates the "noisy neighbor" effect and guarantees stable compute and storage performance.
3. Flexible configuration: You can choose the hardware configuration that best fits your
application and select from various processors, memory, storage, and network resources to achieve an optimal balance between performance and cost.
4. Rapid deployment: You can deploy servers much faster than with traditional physical
hardware. This lets you launch projects quickly and shortens your time to market.
5. Security and isolation: Full control over hardware resources provides a high level of security
and isolation. This is ideal for business scenarios with strict security and compliance requirements. The BMCP platform is a future-ready, enterprise-grade solution. It is ideal for scenarios that require large-scale computing power, such as scientific research, intelligent computing, largescale internet services, and finance. The platform provides a powerful and flexible computing environment. Bare Metal Computing Platform P

## Scenarios

BMCP provides two scenarios: general-purpose and resource reuse. To accommodate different IDC environments, BMCP offers maximum compatibility for resource reuse and top performance for general-purpose use.

**General-purpose scenario**

BMCP builds a highly scalable, high-performance, and cost-effective computing cluster service that runs on native RoCE networks and high-performance parallel file storage. It uses ACK container cluster services, which are deeply optimized for AI scenarios, to provide capabilities such as hardware acceleration, scheduling optimization, and network topology awareness. To meet the diverse computing power needs of various industries, BMCP offers a range of instance types, including Intelligent Computing High-Speed Network, Intelligent Computing Basic, Intelligent Computing Management, and High-Performance Computing High-Speed Network. This provides a cost-effective way to build AI applications in the cloud. Large-scale distributed training: This scenario provides deeply optimized intelligent computing services for large-scale, high-performance training with high resource utilization. It is ideal for applications such as graphics and image editing (image generation with Artificial Intelligence-Generated Content (AIGC)), natural language processing (text generation with AIGC), speech, and video. The service ensures efficient and predictable training to accelerate model iteration. AIGC: Provides scenario-based solutions to generate digital content, such as text, images, audio, and video. Autonomous driving: Provides multiple types of computing power, including bare metal, container, and virtualization. It uses various GPU resource scheduling policies, Remote Direct Memory Access (RDMA) networks, and the Cloud Parallel File System (CPFS) to ensure efficient data processing and computing. This supports efficient model training for autonomous driving that uses petabyte-scale data. It also helps with the deep optimization and rapid iteration of end-to-end algorithms for perception, planning, control, and simulation generation. AI for Science: Provides converged AI and high-performance computing (HPC) power. Computing power and storage resources are shared over a unified network. By deploying and scheduling AI and HPC tasks together, it offers a unified, standard computing service for applications such as basic research, new drug development, and engineering simulation. This promotes innovation in new scientific research paradigms.

**Resource reuse scenario**

The resource reuse scenario uses a managed mode to incorporate existing resources. In a customer's existing intelligent computing center IDC, Apsara Stack BMCP connects to computing servers to manage the high-performance computing cluster. This approach centrally manages disparate computing resources to maximize the return on previous investments. Using Alibaba Cloud products such as Container Service and Machine Learning Platform, this mode builds an integrated hardware and software solution. This helps customers migrate their intelligent computing workloads to the cloud and enhances the service capabilities of the entire platform.

| Feature | Description |
|---|---|
| High-network intelligent computing instance types | GPU-accelerated high-network intelligent computing instances based on native RoCE networks and CPFS storage. Supports some NVIDIA A-series and H-series GPUs. Supports various GPUs, such as Hygon, Ascend, APG, Kunlunxin, and Muxi. |
| Managed intelligent computing instance types | GPU-accelerated registered intelligent computing instances that use existing IB/RoCE networks and traditional storage. Supports certain NVIDIA A-series and H-series GPUs. Supports multiple GPUs, such as Hygon and Ascend. |
| Basic intelligent computing instance types | Basic GPU-accelerated ECS Bare Metal instances that support standard networks without high-speed networking or CPFS. Supports various GPUs, such as Hygon and Ascend. |
| Training and inference optimized intelligent computing instance types | Supports CPN high-performance networks. Deeply optimized based on APG hardware to meet the requirements for building and managing computing power clusters for large-scale parallel inference scenarios. |
| Managed high- performance computing instance types | Designed for traditional high-performance computing (HPC) clusters. Uses BMCP for management to achieve cloud-based resource management and supports migrating repurposed HPC clusters to the cloud. |

| Feature | Description |
|---|---|
| Resource overview | Displays information about bare metal computing clusters, including the number of clusters, nodes, and images. Displays information about container computing clusters, including the number of clusters, nodes, and images. |
| Quota Statistics | Displays the number of physical machines and quota information for each GPU, including statistics for computing power, GPU, CPU, and memory quotas. |

Bare Metal Computing Platform P

## Features

This topic describes the features of the Bare Metal Computing Platform (BMCP).

**Instance types**

**Overview**

| Computing Resource Statistics | Provides a top utilization list for bare metal computing clusters. Provides a top utilization list for container computing clusters. |
|---|---|
| Organizatio n Utilization Ranking | Lists the recent Resource Usage Trends (last 7, 15, or 30 days) for the organization and its sub-organizations. You can view usage trends for basic intelligent computing instances, high-network intelligent computing instances, managed intelligent computing instances, and high-network HPC instances. You can also classify the trends by chip. |
| Alert information | Alert information includes: Resource Alerts, Alert Statistics, and Alert Trends. Resource Alerts lists all resource alerts for your account in the selected organization, resource set, and region. Click Handle to go to the Alert History page in Cloud Monitor to view detailed alert information. Alert Statistics lists the total number of alerts, P1 alerts, P2 alerts, and P3 alerts for your account in the selected organization, resource set, and region. Alert Trends lists the recent alert trends (last 7, 15, or 30 days) for your account in the selected organization, resource set, and region. |

| Feature | Description |
|---|---|
| Cluster types | Supports on-demand creation of bare metal and ack computing clusters. Supports the creation of training and inference optimized clusters. These clusters support large EP and PD separation. |
| Cluster management | Supports one-click creation of bare metal and container computing clusters. Provides a console page for creating target clusters. Provides full lifecycle management for bare metal and container computing clusters, including creation, display, startup, scaling, and deletion. |
| Storage mounting | High-network intelligent computing instances support cluster deployment of high- performance file storage clients and file system mounting. |
| Multi-rail scheduling | When creating a bare metal or container cluster, nodes within the same segment are allocated with priority. High-network intelligent computing instances in bare metal computing clusters support multi-rail scheduling. |

| Feature | Description |
|---|---|
| Node management | Supports full lifecycle management of BMCP nodes, including management, startup, restart, and stop operations. |

Bare Metal Computing Platform P

**Cluster management**

**Node management**

| Remote logon | Supports remote logon to bare metal nodes using Workbench. |
|---|---|
| Storage mounting | Managed intelligent computing instances support storage mounting using the iSCSI and NFS protocols. |
| GPU sharing | GPU virtualization includes hardware virtualization and kernel virtualization. Hygon K100-AI and Ascend 910B only support hardware virtualization. Some NVIDIA A-series GPUs support both hardware and kernel virtualization. High-network and basic intelligent computing instances support GPU virtualization. They provide a graphical interface for managing virtualization specifications at the node level. |

| Feature | Description |
|---|---|
| Image center | Provides standard images for AI application scenarios, including training, inference, and base images. It also includes container images optimized for the domestic hardware and software ecosystem. Container image management. High-network and basic intelligent computing instances support the image center feature. |
| Data acceleration | Data acceleration is divided into image acceleration and cache acceleration. Image acceleration: Converts system images or custom images into a special image format. This format enables on-demand loading during image use, providing millisecond-level startup speeds. Cached data: Builds cached datasets on the local disks of GPU nodes. This significantly accelerates data access speeds in data-intensive scenarios, such as AI. High-network and basic intelligent computing instances support the data acceleration feature. |

| Feature | Description |
|---|---|

Bare Metal Computing Platform P

**Application center**

**Network and security**

| Network resource management | VPC management Supports one-click connection of intelligent computing nodes to a VPC for communication with other services within the cloud. Supports the management of tenant VPCs and vSwitch networks. EVPC management Supports creating EVPCs by organization to manage the RDMA networks of intelligent computing nodes. Using EVPCs, you can manage RDMA network segments and subnets for intelligent computing nodes. You can also isolate RDMA networks between different intelligent computing clusters and between tenant organizations. High-network intelligent computing instances support the EVPC management feature. |
|---|---|
| Security groups | Security group management includes features such as creating and deleting security groups, adding and deleting security group rules, and attaching and detaching instances. Configure security groups to act as virtual firewalls for your instances. This lets you control inbound and outbound traffic to improve instance security. |
| Key pairs | Key pair management includes features such as creating and deleting key pairs, and attaching and detaching instances. Attach a key pair to an instance. Then, you can use the private key to log on to the instance. |

| Feature | Description |
|---|---|
| File system management | High-network intelligent computing instances support cluster deployment of high- performance file storage clients and file system mounting. |

| Feature | Description |
|---|---|
| Tag management | Provides tag management for bare metal and container resources. Supports creating custom tags as needed. |
| Metering management | Supports metering at the container, bare metal, and node levels. It provides resource-level metering for GPUs, CPUs, memory, and more. |

| Feature | Description |
|---|---|

Bare Metal Computing Platform P

**Storage management**

**Operational efficiency**

**Image management**

| Bare metal images | Bare metal image management provides features for custom images, such as query, status management, deletion, and export. It also provides features for public images, such as query, status management, and export. You can upload custom images as needed. |
|---|---|

| Feature | Description |
|---|---|
| Model management | Manages and displays the models in the resource pool, covering general-purpose and managed instance families. |

| Feature | Description |
|---|---|
| Cluster monitoring | Supports multiple metrics. Provides infrastructure monitoring, including key metrics such as CPU utilization, memory usage, disk usage, system load, TCP connections, and network bandwidth. Provides basic GPU monitoring, covering key metrics such as GPU temperature, power, utilization, encoder utilization, decoder utilization, and GPU frame buffer utilization. Provides RDMA monitoring for high-network intelligent computing instances. Metrics include send and receive throughput of the RDMA network, number of buffer overflows, number of out-of-order network datagrams, number of local CQE errors, and number of RNR NAK packets from the peer. Supports querying monitoring data based on time dimensions. |
| Event monitoring | Supports event monitoring for bare metal and container computing clusters. You can configure event alerting mechanisms for metrics such as GPU PCIe/driver failures, compute engine anomalies, PCIe link bandwidth degradation, and GPU interconnect failure diagnostics. Configure event alerts with different severity levels, such as critical, warning, and notice. You can create different alert rules to notify specific personnel based on their permissions. Supports viewing historical alert information. |
| Quick diagnostics | Quick diagnostics supports one-click fault inspection for bare metal and container computing clusters. Diagnostic capabilities include container engine anomaly detection, runc process hang detection, GPU failure detection, HBM availability detection, collective communication library availability verification, GPU stress testing, and intra-machine communication tests. For O&M, it supports network diagnostics, including capabilities such as RDMA port speed and bonded port checks. Create inspection tasks with one click and view the diagnostic results. High-network and basic intelligent computing instances support the quick diagnostics feature. |

Bare Metal Computing Platform P

**Model management**

**O&M and monitoring**

| Job topology visualization | Job topology visualization provides an end-to-end view of job communication links across GPUs, network interface cards, servers, and vSwitches. This helps you quickly identify abnormal points. High-network and basic intelligent computing instances support job-based topology visualization. |
|---|---|

Bare Metal Computing Platform P
