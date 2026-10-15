---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 14
source_pdf: "159ad28459af55a0_Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3CGW/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20cloud%20gateway%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 cloud gateway Product Introduction 20260828

## Table of Contents

- 1 Cloud Gateway
- 2 Product Details
- 3 Product Value
- 4 Features

way

## 1 Cloud Gateway

Cloud Gateway (CGW) is designed to provide scenario-specific network services to help you efficiently build hybrid clouds and migrate workloads to the clouds. CGW is an ideal service for migrating your infrastructure from a public or private cloud to a hybrid cloud. ails

## 2 Product Details

The Cloud Access Gateway provides network services for specific scenarios. It helps customers quickly migrate to the cloud and flexibly build hybrid clouds. This service meets the diverse requirements that arise as cloud infrastructure evolves from private or public clouds to hybrid clouds.

**Open Network Service Platform**

This platform provides lifecycle management for third-party virtual network services, such as Server Load Balancer, firewall, and network performance management, based on network functions virtualization (NFV). The platform follows ETSI standards to standardize onboarding, ensure high availability (HA), enable rapid scaling, and support efficient O&M. It delivers virtual network and security services from Alibaba Cloud's ecosystem partners. Key features include the following: Initializes virtual network service sets. Manages virtual network service clusters. Manages network traffic steering policies. Monitors virtual network element health and isolates faults.

**Computing Power Platform Networking**

This feature diagnoses nodes in the Computing Power Network (CPN). It performs performance analysis, performance monitoring, network device management, and network monitoring. This provides O&M teams with the data required to help administrators better understand and manage network performance and faults.

**Intelligent Computing Server Access to VPC**

Intelligent computing servers connect to a VPC through the computing power platform access gateway, which is a dedicated CHSW device. This connection enables unified management of intelligent computing server resources. The system supports features such as instance management, operation history, bare metal networking, and O&M configuration. These features are used to perform daily O&M tasks for the computing power platform access gateway. ue

## 3 Product Value

The Cloud Access Gateway delivers comprehensive, efficient, secure, easy-to-use, and visual network services for Apsara Stack customers.

**Open Network Service Platform**

Provides an open network service platform that enables standard access, rapid deployment, and efficient operations and maintenance (O&M) support for ecosystem network elements. Automated Deployment: Supports automated deployment of ecosystem partner virtual network devices through standardization and modeling. High Reliability: Supports active/standby high availability cluster models for virtual network devices, with automatic traffic switching during failover. Centralized Management: Deploys partner virtual network devices centrally in an independent VPC to achieve centralized management and reduce deployment costs.

**Computing Power Platform Network**

Provides network access capabilities for intelligent computing scenarios, delivering high performance, simplified O&M, flexible access, strong compatibility, and security. High Performance: Supports RoCEv2-based RDMA networks, physical dual-plane and virtual multi-plane architectures, and multi-track deployment solutions. Easy O&M: Supports over 20 one-click inspection items on the host side, along with performance analysis and testing tools covering communication libraries, bandwidth, and latency. Comprehensive monitoring and alerting coverage on both host and network sides simplifies network operations and maintenance. Flexible Access: Supports dual-uplink access for computing nodes and storage nodes to the storage network, and single-uplink or dual-uplink access for computing nodes to the computing network. Supports current mainstream GPU network interface controller (NIC) access methods. Compatibility: Switches are compatible with H3C and Ruijie. GPUs support NVIDIA GPUs, Hygon DCUs, and Ascend NPUs. Security: Supports ACL-based tenant isolation and secure isolation for multi-tenant traffic.

**Intelligent Computing Server Access to VPC**

Enables intelligent computing server access to a virtual private cloud (VPC). Compatibility: Requires no modifications to intelligent computing servers. Supports connecting intelligent computing servers to the VPC network through a forward gateway. Enables reuse of existing servers to protect your investment. Unified Management: Integrates with Alibaba Cloud VPC products to connect ECS and intelligent computing servers and provide unified resource management. Ease of Use: Integrates with intelligent computing server management to enable unified management and on-demand allocation of intelligent computing server resources. Automatically configures tenant networks for intelligent computing servers when resources are allocated. Security: Supports multi-tenant isolation for intelligent computing server networks. Intelligent computing server networks are isolated from the underlying cloud platform network.

## 4 Features

Cloud Access Gateway provides network connectivity services for various scenarios to help enterprises quickly migrate to the cloud and flexibly build hybrid clouds.

**Hybrid Cloud Networking – Platform Side**

| Feature |   | Description |
|---|---|---|
| Cloud Service Connectivity | Dynamic DNS | Automates DNS forwarding and A record configuration for hybrid cloud scenarios. Includes a management page to improve efficiency when connecting hybrid cloud networks. |
|   | Dynamic VIP | Provides network access capabilities for Alibaba Cloud services and VIP or DNS configuration. Enables service interconnection across multicloud, IDC, and Apsara Stack environments. Supports dynamic VIP creation and synchronizes changes with static VIP resources created in Tianji. Offers flexible external service exposure. |
|   | Cross-Cloud Access | Generates specific access matrices for cloud instances using predefined metadata and rules. Provides accurate input for cloud service connectivity and improves hybrid cloud network connectivity efficiency. |
| Hybrid Cloud Resources | IP Address Pool | Collects and displays IP address pool information from Apsara Stack. |
|   | Physical Topology | Dynamically collects network device interconnection data within a single Apsara Stack data center. Lets you manually add cross- data-center interconnections and internal device interconnections in customer IDCs. |
|   | Network Element Management | Manages network devices in Apsara Stack and customer IDCs (limited support). |
|   | Mitigation Policies (North- South) | Maintains north-south security policies for the cloud platform. Includes system-default policies and custom policies. Integrates with hardware firewalls deployed through “Border Default Security” to push and manage security policies. |

| North-South Security Policies |   |   |
|---|---|---|
|   | NAT Management | Manages NAT capabilities for outbound traffic from the classic network to external networks. Supports IP address pool management and NAT policy management. |
|   | Border Wall Management | Manages hardware firewalls deployed through “Border Default Security”. Supports passwordless login to the firewall’s native management interface. |

**Network Open Platform**

| Feature |   | Description |
|---|---|---|
| Core Features | Network Element Lifecycle Management | ONSP builds an open hybrid cloud networking platform. It delivers network function virtualization (NFV)-based lifecycle management for network services to ecosystem partners. |
|   | Traffic Steering | Using ONSP, steer east-west traffic and some north-south traffic to third-party network elements for processing. |
| O&M Monitoring Capabilities | CMS Monitoring | Integrates with CloudMonitor Service (CMS) to report asynchronous tasks and network element anomaly alerts to CMS. |
|   | Tianjimon Monitoring | Integrates with Tianjimon to report ONSP platform anomaly alerts to Tianjimon. |
| Advanced Features | Network Element Sharing | Allows network element administrators to share network elements with other tenants. |
|   | Multi-Tenant Support | Supports multiple tenants managing their own network elements independently. |
|   | ECS Instance Type Filtering | Filters ECS instance types. |
|   | Dynamic Refresh of VPC ID and vSwitch Name | Refreshes VPC IDs and vSwitch names dynamically. |
|   | One-Click Bypass | Enables one-click bypass. |
| > Document Version: 2 | 0260828 |   |

|   | Multi-VPC Security Protection | Protects multiple VPCs. |
|---|---|---|
| Domestic Software | Intel | Supports Intel processors. |
|   | Hygon | Supports Hygon processors. |
| and Hardware Ecosystem |   |   |
|   | Kunpeng | Supports Kunpeng processors. |
|   | Phytium | Supports Phytium processors. |

**Bare Metal Networking**

| Feature |   | Description |
|---|---|---|
| Core Features | Service Reliability | You can attach bare metal servers as backend servers to Server Load Balancer (SLB) instances in a VPC. |
|   | Deployment and Maintenance of Bare Metal Services | You can access bare metal servers from your office or an existing IDC over a leased line. The VPC connected to your leased line must be the same as the VPC where the bare metal server resides. You can also log on to bare metal servers using ECS instances. The ECS instance and the bare metal server must be in the same VPC. |
|   | Bare Metal Server Access to VPC | You can provision and release bare metal servers in a VPC. This feature enables communication between bare metal servers in different vSwitches within the same VPC, between bare metal servers and ECS instances in the same VPC, and between bare metal servers in different VPCs. |
|   | Bare Metal Server Access to Cloud Services | You can access cloud services such as ops-dns, NTP servers, ApsaraDB RDS, OSS, and NAS from bare metal servers. |
|   | Bare Metal Server Access to the Internet | You can use the Source Network Address Translation (SNAT) feature of NAT Gateway to connect bare metal servers to the Internet. |

|   | Internet Access to Bare Metal Servers | You can attach bare metal servers as backend servers to Internet-facing SLB instances. You can also use the Destination Network Address Translation (DNAT) feature of NAT Gateway to map public IP addresses to the IP addresses of bare metal servers. |
|---|---|---|
| License Management | This feature supports license-based authorization. | Each license lets you manage one group of HSW switches and up to 48 dual-NIC bare metal servers. |
| Bare Metal Server Port Types | 10-Gigabit Optical Port | This port is for 10-Gigabit servers and requires Link Aggregation Control Protocol (LACP) port aggregation support. |
|   | 25-Gigabit Optical Port | This port is for 10-Gigabit or 25-Gigabit servers and requires LACP port aggregation support. |
|   | Multi-Zone Disaster Recovery Across Data Centers |   |
| Deployment Models |   |   |
|   | Multi-Region Deployment (Cell-Based Deployment) |   |
| Stacking Removal | HSW bare machine managed switches support an unstacked architecture. |   |

**Alibaba Cloud Networking Service Topology Visualization**

| Feature |   | Description |
|---|---|---|
| Display Specified VPC Network Topology | Display Specified VPC Network Topology |   |
|   | Display Subnet Information in VPC | Displays ECS information in subnets. |
|   | Display NAT Gateway Information in VPC | Displays NAT Gateway information in the VPC. |
|   | Display Express Connect Information in VPC | Displays VPC peering connection information. |
| > Document Version: 2 | 0260828 1 |   |

|   | Retrieve VPC Network Topology Information Using Open API | Retrieve VPC network topology information using Open API. |
|---|---|---|
|   | VPC Peering | Displays count and supports navigation. |
| Display External Network Areas for VPC |   |   |
|   | Attach a virtual border router (VBR) | Displays count and supports navigation. |
|   | NAT Gateway | Displays count and supports navigation. |
|   | Internet-Facing SLB | Displays count. Backends are ECS instances in this VPC. |
|   | Elastic IP Address | Displays count. EIPs are bound to ECS instances in this VPC. |
|   | VPN Gateway | Displays count. Shows VPN Gateways associated with this VPC. |
|   | IPv6 Gateway | Displays count. Shows IPv6 Gateways for this VPC. |
| Display VPC Private Networks | Displays VPC topology. Lets you select different VPC networks. |   |
| Display Routers | Route Table ID | Displays route table IDs. |
|   | Route Table Name | Displays route table names. |
|   | Router ID | Displays router IDs. |
| Display Full Router List | Displays all routers. | Lists all routers vertically. |
| Display vSwitches | vSwitch ID | Displays vSwitch IDs. |
|   | vSwitch Name | Displays vSwitch names. |
|   | Zone for vSwitch | Displays the zone where the vSwitch resides. |

| loud gateway |   |   |
|---|---|---|
|   | IPv4 CIDR Block for vSwitch | Displays the IPv4 CIDR block for the vSwitch. |
|   | IPv6 CIDR Block for vSwitch | Displays the IPv6 CIDR block for the vSwitch. |
| Display Cloud Resources Under vSwitches | Elastic Compute Service (ECS) | Displays count and supports navigation. |
|   | ApsaraDB RDS | Displays count and supports navigation. |
|   | Internal SLB | Displays count and supports navigation. |
|   | Display All vSwitches | Lists all vSwitches vertically. |

**Hybrid Cloud Network Traffic Visualization**

| Feature |   | Description |
|---|---|---|
| Traffic Analysis | Traffic Trend | Shows top-N traffic rankings. |
|   | Traffic Analysis | Supports statistics on Top-N application type distribution, traffic number of application types, mean traffic volume, and total traffic volume. |
|   | Supported Data Sources | Supports switch port mirroring. Mirrors traffic in both inbound and outbound directions on switch ports. |
| Traffic Rerouting | Multi-zone disaster recovery supports emergency traffic rerouting | Lowers traffic priority for low-priority applications consuming large bandwidth. Ensures bandwidth for high-priority applications. (Version 317 supports only ODPS.) |
|   | Add Analyzer | Add a NIS Traffic Analyzer device. |
|   | Edit Analyzer | Edit a NIS Traffic Analyzer device. |
|   | Delete Analyzer | Delete a NIS Traffic Analyzer device. |

| Analyzer Management |   |   |
|---|---|---|
|   | View Analyzer | You can view NIS Traffic Analyzer devices. |
|   | Add Analyzer Port | Add analysis port information for an analyzer. |
|   | Edit Analyzer Port | Edit analysis port information for an analyzer. |
|   | Delete Analyzer Port | Delete an analyzer’s analysis port. |
|   | View Analyzer Port | View an analyzer’s analysis port. |
| Rule Management | Add Rule | Add a traffic analysis rule. |
|   | Edit Rule | Edit a traffic analysis rule. |
|   | Delete Rule | Delete a traffic analysis rule. |
|   | View Rule | View a traffic analysis rule. |
| Scenario Management | Add Scenario | Add a traffic analysis scenario. |
|   | Edit Scenario | Edit a traffic analysis scenario. |
|   | Delete Scenario | Delete a traffic analysis scenario. |
|   | View Scenario | View a traffic analysis scenario. |
| Multi-Data Center Support | Traffic visualization supports multi-AZ deployment. |   |
| Network Asset | Traffic visualization supports network asset analysis. |   |
| Security Integration | Traffic visualization supports Galaxy Gateway. | Exports data to third parties. |
