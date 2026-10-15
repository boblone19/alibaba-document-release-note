---
title: "cloud gateway Product Introduction 20260310"
product_version: "V3.18.6"
pdf_pages: 15
source_pdf: "7551840bd7202cb6_Alibaba Cloud Apsara Stack V3.18.6 cloud gateway Product Introduction 20260310.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%8E%A5%E5%85%A5%E7%BD%91%E5%85%B3%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20cloud%20gateway%20Product%20Introduction%2020260310.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# cloud gateway Product Introduction 20260310

## Table of Contents

- 1 Cloud Gateway
- 2 Service description
- 3 Benefits
- 4 Functions and features

way

## 1 Cloud Gateway

Cloud Gateway (CGW) is designed to provide scenario-specific network services to help you efficiently build hybrid clouds and migrate workloads to the clouds. CGW is an ideal service for migrating your infrastructure from a public or private cloud to a hybrid cloud. cription

## 2 Service description

Cloud Gateway (CGW) provides scenario-specific network access services to help enterprises efficiently build hybrid clouds and migrate workloads to clouds.

**ONSP**

**Capabilities**

Allows you to create and delete service clusters. Allows you to manage resources. Allows you to route network traffic from VPCs to service clusters.

**Supported services**

Load balancing: allows you to configure load balancing services of ecosystem partners, such as F5 load balancers, Sangfor Technologies load balancers, and Radware load balancers, for VPCs. Virtual firewalls: allows you to protect traffic between VPCs and traffic between a data center and a VPC and enable address translation. Hillstone firewalls are supported. Network performance monitoring (NPM): allows you to collect and analyze network traffic by using third-party services, such as DeepFlow provided by Yunshan Networks and Network Performance Management (NPM) provided by Netis.

## 3 Benefits

Cloud Gateway (CGW) provides you with comprehensive, efficient, secure, easy-to-use, and visual network services.

**ONSP**

ONSP allows you to connect to, deploy, and manage network elements from ecological partners. Automatic deployment: Virtual network elements from ecological partners can be automatically deployed by using standard procedures and models. High reliability: Virtual network elements can be deployed in active/standby clusters, which support automatic switchover for network traffic. Centralized management: Virtual network elements can be deployed in an exclusive VPC. You can centrally manage the virtual network elements at a low cost.

## 4 Functions and features

Cloud Gateway (CGW) provides scenario-specific networking services to help enterprises efficiently build hybrid clouds and migrate workloads to clouds. This topic describes the functions and features of CGW.

**Hybrid cloud network - Platform**

| Feature |   | Description |
|---|---|---|
| Cloud service interconnection | Dynamic DNS | Supports DNS forwarding, automated issuance of A records, and an management interface in hybrid cloud scenarios, improving the efficiency of hybrid cloud networking. |
|   | Dynamic VIPs | Provides network access to cloud services, configurations of virtual IP addresses (VIPs) and DNS, and mutual access between cloud services in multiple clouds, data centers, and Apsara Stack. Supports dynamic VIPs. Both dynamic and static VIPs are recorded in Apsara Infrastructure Management. This allows the system to flexibly use VIPs to provide external services. |
|   | Cross-cloud access | Generates detailed access matrix requirements for cloud instances based on predefined access matrix metadata and rules. This provides accurate input for cloud service interconnection and helps improve the efficiency of hybrid cloud networking. |
| Hybrid cloud resources | IP address pools | Collects and displays information about IP address pools on Apsara Stack. |
|   | Physical topology | Dynamically collects interconnection information of network devices within a single data center on Apsara Stack, and statically adds interconnection information between devices across data centers or between internal devices in customer data centers. |
|   | Network element management | Allows you to manage network devices on Apsara Stack and those in customer data centers (with limited support). |

| North-south security protection policies | Security protection policies (north-south) | Maintains north-south security protection policies for cloud platforms, including system- generated default policies and manually added policies. You can also use the hardware firewalls deployed by the "default border security" policy to issue and manage security protection policies. |
|---|---|---|
|   | NAT management | Allows you to manage the network address translation (NAT) capabilities of cloud platforms for outbound access from the classic network to environments outside Apsara Stack, and supports address pool management and NAT policy management. |
|   | Boundary firewall management | Allows you to manage hardware firewalls deployed by the "default border security" policy, and supports password-free logon redirection to the native management interface of the firewalls. |

**Network open platform**

| Feature |   | Description |
|---|---|---|
| Basic features | Network element lifecycle management | Provides network functions virtualization (NFV)- based network service lifecycle management capabilities for ecosystem partners based on Open Network Service Platform (ONSP) in hybrid cloud scenarios. |
|   | Traffic redirection management | Enables east-west traffic, as well as part of north-south traffic, to be redirected by ONSP to third-party network elements for processing. |
| O&M monitoring capabilities | Monitoring by CloudMonitor | Integrates with CloudMonitor to report abnormal status alerts of asynchronous tasks and network elements to CloudMonitor. |
|   | Monitoring by TianjiMon | Integrates with TianjiMon to report alerts of ONSP to TianjiMon. |
|   | Network element sharing | Allows network element administrators to share network elements with other tenants. |
|   | Multi-tenancy | Supports multiple tenants, each managing their own network elements. |

| roduct Introduction·Fu d features |   |   |
|---|---|---|
| Advanced features |   |   |
|   | ECS specification filtering | Supports Elastic Compute Service (ECS) specification filtering. |
|   | Dynamic refresh of virtual private cloud (VPC) IDs and vSwitch names | Supports dynamic refresh of VPC IDs and vSwitch names. |
|   | Bypass with a few clicks | Supports bypass with a few clicks. |
|   | Multi-VPC security protection | Supports security protection across multiple VPCs. |
| Domestically innovative architectures | Intel | Supports Intel chip architecture. |
|   | Hygon | Supports Hygon chip architecture. |
|   | Kunpeng | Supports Kunpeng chip architecture. |
|   | Phytium | Supports Phytium chip architecture. |

**Bare metal network**

| Feature |   | Description |
|---|---|---|
| Basic features | Service reliability | Supports attachment of bare metal instances to the backend of internal-facing Server Load Balancer (SLB) instances that can be accessed from a VPC. |
|   | Bare metal service deployment and operations | Allows customers to access bare metal instances from office networks or legacy data centers by using leased lines (the VPC to be connected to by using a leased line must be the same as that in which the required bare metal instance resides). Allows customers to log on to bare metal instances by using ECS. (the ECS instance to use and the bare metal instance to log on to must reside in the same VPC). |
|   | Connection of bare metal instances to VPCs | Supports applications for and release of bare metal instances in VPCs, communication between bare metal instances in the same VPC and different vSwitches, communication between bare metal instances and ECS instances in the same VPC, and communication between bare metal instances in different VPCs. |

|   | Access from bare metal instances to cloud services | Supports access from bare metal instances to OPS-DNS, Network Time Protocol (NTP) serves, ApsaraDB RDS instances, Object Storage Service (OSS), and File Storage NAS (NAS). |
|---|---|---|
|   | Access from bare metal instances to the Internet | Supports access from bare metal instances to the Internet by using SNAT entries of NAT gateways. |
|   | Public access to bare metal instances | Supports attachment of bare metal instances to the backend of Internet-facing SLB instances, and supports public access to bare metal instances by using DNAT entries of NAT gateways to map specified bare metal IP addresses. |
| Authorization management | License-based authorization management | Supports the management of a group of hybrid switches (HSWs) for each license and allows access for up to 48 NIC bare metal instances with two network interface controllers (NICs). |
| Bare metal port types | 10 GE optical port | Supports 10 GE servers, which require port aggregation based on Link Aggregation Control Protocol (LACP). |
|   | 25 GE optical port | Supports 10 GE or 25 GE servers, which require port aggregation based on LACP. |
| Deployment modes | Zone-disaster recovery with dual data centers |   |
|   | Multi-region deployment (unit-based deployment) |   |
| De-stacking | Supports de-stacking architecture on HSWs managed by bare metal instances. |   |

**Topology visualization for cloud networking services**

| Feature |   | Description |
|---|---|---|
|   | VPC topology |   |
|   | Subnet information within a VPC | Displays information about ECS instances within a subnet. |

| roduct Introduction·Fu d features |   |   |
|---|---|---|
| Display of a specified VPC topology |   |   |
|   | NAT gateway information | Displays NAT gateway information within a VPC. |
|   | Express Connect information within a VPC | Displays VPC peering connection information. |
|   | Obtaining VPC topology information by calling API operations | Allows you to obtain information about a VPC topology by calling API operations. |
| Display of areas outside a VPC | VPC peering | Displays the quantity and supports redirection. |
|   | VBR uplink | Displays the quantity and supports redirection. |
|   | NAT gateways | Displays the quantity and supports redirection. |
|   | Internet-facing SLB instances | Displays the quantity of Internet-facing SLB instances to which ECS instances that reside in the current VPC are attached. |
|   | EIPs | Displays the quantity of EIPs with which ECS instances that reside in the current VPC are associated. |
|   | VPN gateways | Displays the quantity of VPN gateways associated with the current VPC. |
|   | IPv6 gateways | Displays the quantity of IPv6 gateways of the current VPC. |
| Display of VPCs | Visualization of VPC topologies and selection of VPCs |   |
| Display of routers | Route table IDs | Displays route table IDs. |
|   | Route table names | Displays route table names. |
|   | Router IDs | Displays router IDs. |
| Display of all routers | All routers | Displays all routers in a list. |

| Display of vSwitches | vSwitch IDs | Displays vSwitch IDs. |
|---|---|---|
|   | vSwitch names | Displays vSwitch names. |
|   | Zones of vSwitches | Displays the zones of vSwitches. |
|   | IPv4 CIDR blocks of vSwitches | Displays the IPv4 CIDR blocks of vSwitches. |
|   | IPv6 CIDR blocks of vSwitches | Displays the IPv6 CIDR blocks of vSwitches. |
| Display of cloud resources under vSwitches. | ECS instances | Displays the quantity and supports redirection. |
|   | ApsaraDB RDS instances | Displays the quantity and supports redirection. |
|   | Internal-facing SLB instances | Displays the quantity and supports redirection. |
|   | All vSwitches | Displays all vSwitches in a list. |

**Traffic visualization for hybrid cloud network**

| Feature |   | Description |
|---|---|---|
| Traffic analysis | Traffic trends | Supports traffic ranking and displays the top N applications. |
|   | Traffic analysis | Displays type distributions of the top N applications, the number of application types, average traffic size, and total traffic size. |
|   | Supported data sources | Supports vSwitch port mirroring, which indicates traffic mirroring in both ingress and egress directions of vSwitch ports. |
| Traffic scheduling | Emergency scheduled traffic shifting for zone- disaster recovery | Allows you to lower the traffic priority of low- priority, high-bandwidth applications to ensure bandwidth for high-priority applications (Apsara Stack V3.17 supports only ODPS). |
|   | Analyzer adding | Allows you to add a traffic analyzer. |

| roduct Introduction·Fu d features | nctions a cloud gatewa |   |
|---|---|---|
| Analyzer management |   |   |
|   | Analyzer modification | Allows you to modify a traffic analyzer. |
|   | Analyzer removal | Allows you to remove a traffic analyzer. |
|   | Analyzer viewing | Allows you to view a traffic analyzer. |
|   | Analysis port adding | Allows you to add an analysis port for an analyzer. |
|   | Analysis port modification | Allows you to modify an analysis port for an analyzer. |
|   | Analysis port removal | Allows you to remove an analysis port from an analyzer. |
|   | Analysis port viewing | Allows you to view an analysis port of an analyzer. |
| Rule management | Rule creation | Allows you to create a traffic analysis rule. |
|   | Rule modification | Allows you to modify a traffic analysis rule. |
|   | Rule deletion | Allows you to delete a traffic analysis rule. |
|   | Rule viewing | Allows you to view a traffic analysis rule. |
| Scenario management | Scenario creation | Allows you to create a traffic analysis scenario. |
|   | Scenario modification | Allows you to modify a traffic analysis scenario. |
|   | Scenario deletion | Allows you to delete a traffic analysis scenario. |
|   | Scenario viewing | Allows you to view a traffic analysis scenario. |
| Multi-data center deployment | Multi-zone deployment for traffic visualization |   |
| Network assets | Network asset analysis for traffic visualization |   |

| Security integration | Integration with Galaxy Security Gateway for traffic visualization | Supports data export to third-party platforms. |
|---|---|---|
