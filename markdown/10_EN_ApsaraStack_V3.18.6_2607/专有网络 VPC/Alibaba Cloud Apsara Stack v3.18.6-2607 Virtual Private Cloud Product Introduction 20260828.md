---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 17
source_pdf: "fef33325b7998aad_Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%B8%93%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Virtual%20Private%20Cloud%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud Product Introduction 20260828

## Table of Contents

- 1 Virtual private cloud
  - 1.1 Features
  - 1.2 Benefits
  - 1.3 Features
  - 1.4 Use scenarios

## 1 Virtual private cloud

A virtual private cloud (VPC) is a private network in the cloud. A VPC provides network services for resources in the cloud. Different VPCs are logically isolated from each other. You have full control over your VPC. For example, you can specify CIDR blocks, and configure route tables and gateways for your VPC. In your VPCs, you can use Alibaba Cloud resources, such as Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, and Server Load Balancer (SLB) instances.

### 1.1 Features

Virtual private clouds (VPCs) are private networks deployed on Apsara Stack. VPCs are logically isolated from each other. You can manage your VPCs and Apsara Stack resources in your VPCs.

**VPCs**

Each VPC consists of one private CIDR block, at least one vRouter, and at least one vSwitch. When you create a VPC and a vSwitch, you must specify the private IP address range for the VPC in CIDR notation. You can use the standard private CIDR blocks listed in the following table and their subsets as the private CIDR blocks for your VPCs.

| CIDR block | Number of available private IP addresses (excluding IP addresses reserved by the system) |
|---|---|
| 192.168.0.0/16 | 65,532 |
| 172.16.0.0/16 | 65,532 |

A vRouter is the hub of a VPC. As a core component, it connects the vSwitches in a VPC and serves as a gateway between a VPC and other networks. After you create a VPC, the system automatically creates a vRouter. Each vRouter is associated with a route table. A vSwitch is a basic network component that connects different cloud resources in a VPC. After you create a VPC, you can create vSwitches to create one or more subnets for the VPC. vSwitches in the same VPC can communicate with each other. You can deploy your applications in vSwitches that belong to different zones to improve service availability.

**Custom route tables and routes**

After you create a VPC, the system creates a system route table to manage routes of the VPC. By default, vSwitches in the VPC use this route table. You cannot create or delete the system route table of a VPC. However, you can create a custom route table and associate it with a vSwitch to manage your network in a more flexible way. You can add custom routes to the system route table and custom route tables to route traffic to specified next hops. The route table uses the longest prefix match algorithm for traffic routing. If multiple routes match the destination IP address, the route with the longest subnet mask prevails and is used to determine the next hop. This ensures that the traffic is routed to the most precise destination.

**High-availability virtual IP addresses (HAVIPs)**

HAVIPs are private IP addresses that can be created and released as independent resources. You can use HAVIPs with high-availability software such as Keepalived to provide active/standby services. This improves the availability of your services. Each Elastic Compute Service (ECS) instance is assigned a private IP address as the primary IP address. You can associate HAVIPs with an ECS instance to increase the number of private IP addresses available for the ECS instance.

**Network access control lists (ACLs)**

Network ACLs allow you to implement access control for a VPC. You can create network ACL rules and associate a network ACL with a vSwitch. This allows you to control inbound and outbound traffic of ECS instances that are associated with the vSwitch.

**Various connection methods**

Apsara Stack provides multiple connection methods. You can connect a VPC to the Internet, a data center, or another VPC. Connect a VPC to the Internet You can connect a VPC to the Internet by associating elastic IP addresses (EIPs) with resources in the VPC or configuring NAT gateways. This way, resources in the VPC can communicate with the Internet. Connect a VPC to another VPC You can establish high-performance and secure connections between VPCs by creating a pair of router interfaces. Connect a VPC to a data center You can connect a VPC to a data center through Express Connect circuits. This allows you to smoothly migrate on-premises applications to the cloud.

### 1.2 Benefits

This topic describes the benefits of virtual private clouds (VPCs). VPCs are secure, reliable, flexible, easy to use, and scalable.

**Security and reliability**

Each VPC is identified by a unique tunnel ID, which corresponds to a virtual network. Different VPCs are isolated by tunnel IDs: Similar to a traditional network, you can create vSwitches and vRouters to divide a VPC into multiple subnets. Elastic Compute Service (ECS) instances in the same subnet use the same vSwitch to communicate with each other, while ECS instances in different subnets use vRouters to communicate with each other. VPCs are completely isolated from each other. Cloud resources in different VPCs can communicate with each other by using elastic IP addresses (EIPs) or NAT IP addresses. The IP packets of an ECS instance are encapsulated by using the tunneling technology. Therefore, information at the data link layer (the MAC address) of the ECS instance is not transferred to the physical network. This way, ECS instances in different VPCs are isolated at Layer 2. ECS instances in a VPC use security groups and firewalls to control inbound and outbound traffic at Layer 3.

**Flexible management**

You can use security group rules and access control lists (ACLs) to manage inbound and outbound traffic to cloud resources in a VPC in a flexible manner.

**Ease of use**

You can easily create and manage VPCs in the VPC console. When you create a VPC, the system automatically creates a vRouter and a route table for the VPC.

**High scalability**

You can create different subnets in a VPC to deploy different services. Additionally, you can connect a VPC to a data center or another VPC to extend the network architecture.

### 1.3 Features

This topic describes the features of Alibaba Cloud Virtual Private Cloud (VPC). A VPC provides an isolated, customizable virtual network environment that lets you flexibly manage and securely isolate your network resources. VPC supports a wide range of networking capabilities, including network segmentation, Elastic IP addresses (EIPs), subnetting, and gateway configuration. These features help ensure high availability for your backend services and secure network communications.

**VPC**

| Feature |   | Description |
|---|---|---|
| VPC management | Modify a VPC | Modify the name and description of a VPC. |
|   | Create a VPC | Create a VPC. |
|   | Delete a VPC | Delete a VPC. |
|   | View a VPC | Find and view VPCs by using filters. |
| Multi-account VPC sharing | Share a VPC | Share a VPC with other accounts in your resource set, organization, or subordinate organizations. |
| VPC instance management | Tags | Add custom tags to VPC instances. |
|   | Enable IPv6 for a VPC | Enable IPv6 for a VPC. |
|   | Modify VPC attributes | Modify the name and description of a VPC. |
|   | Create a VPC | Create a VPC. |
|   | Delete a VPC | Delete a VPC. |
|   | Query VPC information | Query information about a VPC. |

| ECS services | VPC network management for ECS instances | VPC provides network connectivity for each ECS instance. |
|---|---|---|
|   |   | Provides networking services for ECS elastic network interfaces. |
|   |   | Supports rate limiting for ECS instances. |
|   |   | Provides network proxy services for ECS instances. |
|   |   | Supports ECS proxy, migration, access control, O&M, monitoring, and after-sales tools. |
| VPC traffic mirroring | Supported instance types for VPC traffic mirroring | Supports Shenlong MOC 2.0 instances. |
|   |   | Supports general-purpose instance types. |
|   | Basic configuration | Modify a traffic mirror session. |
|   |   | Stop a traffic mirror session. |
|   |   | Create a traffic mirror session. |
|   |   | Delete a traffic mirror session. |
|   |   | View a traffic mirror session. |
|   | Filter conditions | Filter both ingress and egress traffic. |
|   |   | Filter based on the 5-tuple. |
|   | Mirror session | Copies network traffic from a source to a destination based on filter conditions. |
|   | Mirror source | An elastic network interface (ENI) from which traffic is copied. |
|   | Mirror destination | An elastic network interface (ENI) or an internal- facing Server Load Balancer (SLB) instance that receives the mirrored traffic. |

|   | Hardware and software ecosystem | Supports Shenlong MOC 2.0. |
|---|---|---|
|   |   | Supports general-purpose instance types. |
|   |   | Supports Intel processors. |
|   |   | Supports Hygon processors. |
|   |   | Supports ARM (Kunpeng) processors. |
| vSwitch instance management | vSwitch subnet mask | The IPv4 subnet mask length for a vSwitch ranges from /16 to /29. |
|   | Modify vSwitch attributes | Modify the attributes of a vSwitch. |
|   | Create a vSwitch | Create a vSwitch in a VPC. |
|   | Delete a vSwitch | Delete a vSwitch from a VPC. |
|   | Query the vSwitch list | Query a list of vSwitches. |
| Route table management | Delete a custom route | Delete a route entry from a vRouter. |
|   | Delete a custom IPv4 route | Delete an IPv4 route entry from a vRouter. |
|   | Subnet route | Associate a custom route table with a vSwitch to forward its traffic based on the routes in the table. |
|   | Subnet route 2.0 |   |
|   | Create a custom route | Add a custom route entry to a vRouter. |
|   | Create a custom IPv4 route | Add a custom route entry to a vRouter. The next hop can be set to an elastic network interface, a router interface (RI) for a VPC or VBR, an ECS instance, a VPN Gateway, a NAT Gateway, or an HAVIP. |
|   | Query the route table list | Query the route entries in a vRouter. |

|   | Custom IPv4 routes with active/standby router interfaces | Add a custom route entry to a vRouter where the next hop is configured with active/standby router interfaces (VBR). |
|---|---|---|
|   | Custom IPv4 routes with load-balanced router interfaces | Add a custom route entry to a vRouter where the next hop is configured with multiple load- balancing router interfaces (VBR). |
|   | Custom route table | In addition to the default system route table, you can create custom route tables. Add custom route entries with next hops such as ECS instances, various gateways, or VBRs. |
| HAVIP | High availability with active/standby ECS instances | Bind to ECS instances to create a high- availability active/standby pair. |
|   | Modify HAVIP attributes | Modify the attributes of an HAVIP. |
|   | Create an HAVIP | Create an HAVIP instance. |
|   | Delete an HAVIP | Delete an HAVIP instance. |
|   | High availability with active/standby elastic network interfaces | Bind to elastic network interfaces to create a high-availability active/standby pair. |
|   | Query an HAVIP | Query the attributes and status of an HAVIP. |
| IPv6 Gateway egress-only rules | Restricts access to allow only outbound internet connections while preventing inbound connections initiated from the internet. | Allows resources in the VPC to make outbound IPv6 connections to the internet, while blocking unsolicited inbound connections. |
| IPv6 Gateway management | Modify an IPv6 Gateway | Modify an IPv6 Gateway. |
|   | Create an IPv6 Gateway | Create an IPv6 Gateway. |
|   | Delete an IPv6 Gateway | Delete an IPv6 Gateway. |
|   | View a NAT bandwidth plan | View a NAT bandwidth plan. |

| irtual Private Cloud | Product Introduction·Virtual priv te clou |   |
|---|---|---|
| NAT bandwidth plan management |   |   |
|   | Modify NAT bandwidth plan name and description | Modify the properties of a bandwidth plan. |
|   | Modify NAT bandwidth plan bandwidth | Modify a bandwidth plan. |
|   | Delete a NAT bandwidth plan | Delete a bandwidth plan. |
|   | Remove public IP from NAT bandwidth plan | Remove a public IP address from a bandwidth plan. |
|   | Add public IP to NAT bandwidth plan | Add a public IP address to a bandwidth plan. |
| NAT Gateway | DNAT | Maps a public IP address and port to a private IP address and port, allowing inbound internet traffic to reach servers within the VPC. |
|   | SNAT | Maps private IP addresses to a public IP address, allowing servers within the VPC to access the internet. |
| NAT Gateway management | Tags | Add custom tags to NAT Gateway instances. |
|   | Modify a NAT Gateway | Modify gateway properties, such as the name. |
|   | Create a NAT Gateway | Create a NAT Gateway. |
|   | Delete a NAT Gateway | Delete and release a gateway. |
| Manage DNAT table | Use the same EIP for SNAT and DNAT | Use a single EIP for both SNAT and DNAT entries. |
|   | Modify a DNAT entry | Modify a DNAT entry. You can change the frontend and backend port information and the backend ECS instance. |
|   | Create a DNAT entry | Create a DNAT entry. |
|   | Delete a DNAT entry | Deletes a DNAT entry, which removes its port forwarding rule. |

| Manage SNAT table | Modify an SNAT entry | Modify the associated EIP and rule granularity of an SNAT entry. |
|---|---|---|
|   | Create SNAT entry (ECS granularity) | Create an SNAT forwarding rule that applies to a specific ECS instance. |
|   | Create SNAT entry (vSwitch granularity) | Create an SNAT forwarding rule that applies to a specific vSwitch. |
|   | Delete an SNAT entry | Deletes an SNAT entry, which removes its outbound address translation rule. |
| EIP | Tags | Add custom tags to EIP instances. |
|   | Modify EIP attributes | Modify EIP attributes. |
|   | Query the EIP list | Query a list of EIPs. |
|   | Traffic metering | Meter EIP traffic and export the data to Operations Management Service (OMS). |
|   | Modify EIP bandwidth | Modify the bandwidth of an EIP. |
|   | Support for multiple ISP lines | Allocate EIPs from various Internet Service Provider (ISP) lines. |
|   | Allocate with specified bandwidth | Allocate an EIP with a specified bandwidth. |
|   | Allocate an EIP | Allocate an EIP address. |
|   | Associate an EIP | Associate an EIP with a cloud service instance, an HAVIP instance, or an elastic network interface in the same region. |
|   | Unassociate an EIP | Unassociate an EIP address from its bound instance. |
|   | Release an EIP | Release an EIP that is no longer needed. |
|   | Associate an EIP with an elastic network interface (ENI) | Associate an EIP with a single elastic network interface. |
| 2 | > Document Version: 2026082 |   |

|   | Associate multiple EIPs with an ENI | Associate multiple EIPs with a single elastic network interface. |
|---|---|---|
| Virtualized gateway | Containerization | XGW runs on Docker. |
|   | Multi-data center | XGW on Docker supports intra-city disaster recovery. |
|   |   | XGW on Docker supports multiple regions. |
| Network ACL | vSwitch-level access control with network ACLs (IPv4) | Create a network ACL, configure ingress and egress rules, and associate it with a vSwitch to control inbound and outbound IPv4 traffic. |
|   | Import or export ACL rules | ASCM VPC ACL supports cloning and the import/export of ACL rules. |
| Router instance management | Modify router attributes | Modify router attributes. |
|   | Query router instance information | Query router instance information. |
|   | Intra-region VPC connectivity | Use Express Connect to establish private connections between VPCs in the same region. This is supported for both same-account and cross-account scenarios. |
| Express Connect Note This service is provided by Express Connect. |   |   |
|   | Cross-region VPC connectivity | Use Express Connect to establish private connections between VPCs in different regions. This is supported for both same-account and cross-account scenarios. |
|   | Enable a router interface | Enable an inactive router interface to allow data transmission. |
|   | Disable a router interface | Disable an active router interface to stop data transmission. |
|   | Edit a peer interface | Edit the configuration of the peer router interface. |
|   | Edit a local interface | Edit the configuration of the local router interface. |
| > Document Version: 2 | 0260828 1 |   |

|   | Configure a route | Configure routes for the router interface. |
|---|---|---|
| Multi-AZ and multi- region | VPC multi-region 2.0 | Available for Apsara Stack deployments on physical machines. |
|   | Three-AZ support | Available for physical machine deployments. |
|   | Support for Intel | Supports Intel processors. |
|   | Support for Hygon | Supports Hygon processors. |
| Hardware and software ecosystem | Support for Kunpeng | Supports Kunpeng processors. |
|   | Phytium | Available for physical machine deployments. |
|   | Sunway | Available for physical machine deployments. |
|   | Support for V8 | Available for physical machine deployments. |
|   | Support for 8U | Available for physical machine deployments. |
| Network interface cards (NICs) | Support for dual-port CX6 NICs | Available for physical machine deployments. |
|   | Support for X710 NICs on Hygon | Available for physical machine deployments. |
|   | XGW on Docker with dual- port CX6 NICs | For virtualized gateways. |
|   | 100 Gbit/s network access for VPC | For physical machine gateways. |
| Architectural enhancements | FRR support on XGW | Fast Reroute (FRR) ensures rapid data flow recovery during network failures. |
| vSwitch | vSwitch creation linked to VPC CIDR blocks | vSwitch creation can be linked to multiple IPv4 CIDR blocks in the VPC. |
|   | vSwitch creation linked to VPC CIDR blocks | vSwitch creation can be linked to multiple IPv6 CIDR blocks in the VPC. |

**Monitoring and alarms**

| Feature |   | Description |
|---|---|---|
| Alarms | VPC alarms | Set alarms for VPC resources and events. |
| Monitoring | NOE operations and monitoring | Provides NOE, a backend operations tool for querying VPC resources. |
|   | AVS monitoring | Integrate AVS with CloudMonitor to monitor tenant networks. |
|   |   | Integrate AVS with the Tianji monitoring platform to monitor networks. |
|   | NAT monitoring | Monitor inbound and outbound bandwidth, and bandwidth utilization for your NAT Gateway. |

### 1.4 Use scenarios

Virtual private clouds (VPCs) are virtual networks that are isolated from each other. VPCs support flexible configurations to meet the requirements of different scenarios.

**Deploy applications in a safe manner**

You can deploy applications in a VPC to provide services to external networks. To control access to the applications over the Internet, you can create security group rules and configure whitelists. You can also isolate application servers from databases to implement access control. For example, you can deploy web servers in a subnet that can access the Internet, and deploy databases in another subnet that cannot access the Internet.

**Deploy applications that require access to the Internet**

You can deploy applications that require access to the Internet in a subnet of a VPC and use an Internet NAT gateway to route network traffic. You can configure SNAT entries to allow instances in the subnet to access the Internet without the need to expose the private IP addresses. In addition, you can change the elastic IP addresses (EIPs) specified in the SNAT entries to prevent attacks from the Internet.

**Implement cross-zone disaster recovery**

You can create one or more vSwitches to create one or more subnets for the VPC. vSwitches within the same VPC can communicate with each other. To implement cross-zone disaster recovery, you can deploy resources across vSwitches in different zones.

**Isolate business systems**

VPCs are logically isolated from each other. You can use multiple VPCs to isolate business systems in different environments such as production and test environments. To allow business systems deployed in two VPCs to communicate with each other, you can create a peering connection between the VPCs.

**Build a hybrid cloud**

To expand your on-premises network, you can establish a dedicated connection between a VPC and your data center. This allows you to seamlessly migrate the applications in your data center to the cloud. You do not need to change the access method for the applications.
