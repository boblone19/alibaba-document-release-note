---
title: "Virtual Private Cloud Product Introduction 20260310"
product_version: "V3.18.6"
pdf_pages: 17
source_pdf: "c78f4a878ff13a8c_Alibaba Cloud Apsara Stack V3.18.6 Virtual Private Cloud Product Introduction 20260310.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%B8%93%E6%9C%89%E7%BD%91%E7%BB%9CVPC/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Virtual%20Private%20Cloud%20Product%20Introduction%2020260310.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Virtual Private Cloud Product Introduction 20260310

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

This topic describes the features of virtual private clouds (VPCs). VPCs provide an isolated and customizable virtual environment for flexible management and secure isolation of resources. VPCs support a variety of features, including isolating CIDR blocks, and configuring Elastic IP (EIP), subnets, and gateways to ensure high availability of backend services and communication security.

**VPC**

| Feature |   | Description |
|---|---|---|
| VPC management | Modify VPC | Modify the name and description of a VPC. |
|   | Create VPC | Create a VPC. |
|   | Delete VPC | Delete a VPC. |
|   | Query VPC | Query a VPC using filters. |
| VPC sharing | VPC sharing | Share VPCs in the current resource set, between organization and sub-branches, and in the current organization. |
| VPC instance management | Tags | Custom tags are supported due to the integration of the tag system. |
|   | Enable IPv6 | Enable the IPv6 feature for VPCs |
|   | Modify VPC attributes | Modify the VPC name and description. |
|   | Create VPC | Create a VPC. |
|   | Delete VPC | Delete a VPC. |
|   | Query VPC | Query a VPC. |

| Elastic Compute Service (ECS) | Manage network for ECS instances | Provide network connectivity for ECS instances. |
|---|---|---|
|   |   | Provide ECS network interface controller service. |
|   |   | Support ECS throttling. |
|   |   | Provide ECS proxy network service. |
|   |   | Support ECS proxy, migration, access control, O&M monitoring, and after-sales tools. |
| Traffic mirroring | Supported models | SHENLONG MOC 2.0 |
|   |   | General models |
|   | Basic settings | Modify traffic mirroring. |
|   |   | Stop traffic mirroring. |
|   |   | Create traffic mirror. |
|   |   | Delete traffic mirror. |
|   |   | View traffic mirroring. |
|   | Filters | Outbound and inbound traffic. |
|   |   | 5-tuples. |
|   | Traffic mirror session | Mirror traffic from a source to a destination based on specified filters. |
|   | Traffic mirror source | An ENI from which you want to mirror traffic. |
|   | Traffic mirror destination | An ENI or an internal-facing SLB instance that is used to receive mirrored traffic. |
|   |   | SHENLONG MOC 2.0 |

|   | ITAI |   |
|---|---|---|
|   |   | General models |
|   |   | Intel |
|   |   | Hygon |
|   |   | ARM (Kunpeng) |
| Manage vSwitch | vSwitch mask | The IPv4 mask length of the vSwitch CIDR block must be 16 to 29 bits. |
|   | Modify vSwitch | Modify a vSwitch |
|   | Create vSwitch | Create a vSwitch in the VPC. |
|   | Delete vSwitch | Delete a vSwitch from a VPC. |
|   | Query vSwitch | Query a vSwitch. |
|   | Delete a custom route entry | Delete an existing route entry in the vRouter. |
| Route Table Management |   |   |
|   | Delete a custom IPv4 route entry | Delete an existing route entry in the vRouter. |
|   | Subnet routing | After you associate a custom route table with a vSwitch, traffic in the vSwitch is forwarded based on the custom route table. |
|   | Subnet routing 2.0 |   |
|   | Create a custom route | Set up a new custom route entry in the vRouter. |
|   | New IPv4 custom route | Set a new custom route entry in the vRouter. The next hop can be set to Elastic Network Interface, RI (VPC/VBR), ECS, VPN, NAT, and HAVIP. |
|   | Query the list of route tables | Query entries in a route table. |

|   | IPv4 custom routes support dedicated RI primary/secondary mode | Set a new custom route entry in the vRouter. The next hop can be configured as a primary/secondary RI (VBR) interface. |
|---|---|---|
|   | IPV4 custom routes support dedicated RI load balancing mode | Set a new custom route entry in the vRouter. The next hop can be configured as multiple load sharing RI (VBR) interface. |
|   | Custom route tables | In addition to the system route table, you can create custom route table and entries. The next hop type supports ECS, gateways, and VBRs. |
|   | ECS high reliability | HAVIP can be bound to a primary instance and a secondary ECS instance. |
| High-availability virtual IP address (HAVIP) |   |   |
|   | Modify HAVIP | Modify HAVIP attributes. |
|   | Create HAVIP | Create a new HAVIP. |
|   | Delete HAIVP | Deletes an HAVIP instance. |
|   | ENI high reliability | HAVIP can be bound to a primary ENI and a secondary ENI. |
|   | Query HAIVP | Query HAIVP attributes and status. |
| IPv6 gateway egress-only rules | Allow access from the Internet and reject access from the VPC to the Internet | Only access from the Internet is allowed. Resources in the VPC are not allowed to access the Internet. |
| Manage IPv6 gateway | Modify IPv6 gateway | Modify an IPv6 gateway. |
|   | Create IPv6 gateway | Create an IPv6 gateway. |
|   | Delete IPv6 gateway | Delete an IPv6 gateway. |
|   | View NAT service plans | Query a NAT service plan. |
|   | Modify the name and description of a NAT service plan. | Modify attributes of a service package |

| irtual Private Cloud |   |   |
|---|---|---|
| Manage NAT service plans |   |   |
|   | Modify the bandwidth of a NAT service plan | Modify the bandwidth plan. |
|   | Delete a NAT service plan | Delete a service plan. |
|   | Remove a public IP address from a NAT service plan. | Remove a public IP address from a NAT service plan. |
|   | Add a public IP address to a NAT service plan. | Add a public IP addresses to a NAT service plan. |
| NAT gateway | DNAT | Modify the destination address of IP data packets, generally used in scenarios where the Internet accesses a private server. |
|   | SNAT | Modify the source address of IP packets, generally used in scenarios where a private server accesses the Internet. |
| Basic NAT gateway management | Tags | Custom tags are supported due to the integration of the tag system. |
|   | Modify a NAT gateway | Modify the gateway attributes, including the name. |
|   | Create a NAT gateway | Create a gateway. |
|   | Delete NAT gateway | Delete or release a NAT gateway. |
| Manage a DNAT table | SNAT and DNAT share the same EIP | Specify the same EIP for both SNAT and DNAT entries. |
|   | Modify DNAT Entry | Modify the DNAT rule. You can change the port information and backend ECS instances. |
|   | Create DNAT entry | Create a DNAT rule. |
|   | Delete DNAT entry | The forwarding logic becomes invalid after the DNAT rule is deleted. |
|   | Modify an SNAT entry | Modify the associated EIP and rule granularity of an SNAT rule. |

| roduct Introduction·Vi e cloud | rtual priva Virtual Private Clou |   |
|---|---|---|
| Manage SNAT table |   |   |
|   | Create SNAT entries- Specify ECS | Create SNAT rules for the ECS to match ECS forwarding. |
|   | Create SNAT entries- Specify vSwitch | Create SNAT rules for vSwitches to match vSwitch forwarding. |
|   | Delete an SNAT entry | The forwarding rule becomes invalid after the corresponding SNAT entry is deleted. |
| EIPs | Tags | Custom tags are supported due to the integration of the tag system. |
|   | Modify EIP attributes | Modify EIP attributes. |
|   | Query EIP list | Query the EIP list. |
|   | Metered Traffic | Support traffic metering capabilities based on EIPs. You can export EIP metering data to OMS. |
|   | Modify the bandwidth of an EIP | Change the bandwidth of the EIP. |
|   | Multi-carrier lines | Create an EIP. |
|   | Specified bandwidth creation | Support the creation of a specified bandwidth. |
|   | Apply for an EIP | Apply for an EIP. |
|   | Associate an HAVIP with an EIP | Bind the EIP to a cloud resource, HAVIP, or ENI in the same region. |
|   | Unbind an EIP | Unbind the EIP from the instance. |
|   | Release an EIP | Releases EIPs that are no longer in use. |
|   | Bind an EIP to an ENI | Each EIP can be associated with one ENI. |
|   | Bind multiple EIPs to ENI | Bind multiple EIPs to ENI. |
|   | Containerization | XGW on docker. |
| 2 | > Document Version: 2026031 |   |

| irtual Private Cloud | Product Introduction·Virtual priv te clou |   |
|---|---|---|
| Virtuali gateway |   |   |
|   | Multi-IDC Deployment | Supports zone-disaster recovery. |
|   |   | XGW on docker supports multiple regions. |
| Network ACLs | Support for NACL (IPv4) at vSwitch level | Create NACLs and configure inbound and outbound rules. Bind the NACL to the vSwitch to manage the inbound and outbound IPv4 traffic. |
|   | Import/export ACL rules to files | The VPC ACL feature in ASCM supports cloning ACL and importing/exporting ACL rules. |
| vRouter Management | Modify vRouter attributes | Modify vRouter attributes. |
|   | Query vRouter | Query a vRouter. |
| Express Connect circuit Note Provide service using Express Connect | Local region VPCs | Enable private communication between VPCs by using Express Connect in the same account or across accounts. |
|   | Cross-region VPCs | Enable private communication between VPCs in different regions by using Express Connect in the same account or across accounts. |
|   | Activate vRouter interface | Activate a vRouter interface in the Inactive state. After being activated, the vRouter interface sends data properly. |
|   | Disable a vRouter interface | You can deactivate a vRouter interface in the Active status. No data will pass through the vRouter interface. |
|   | Modify information of the peer interface | Modify the configuration of the peer interface. |
|   | Modify information of the local interface | Modify the configuration of the local interface. |
|   | Configure a route | Configure routes for vRouter interfaces. |
| Multi-IDC Deployment | VPC supports multi-region 2.0 | Physical servers in Business Foundation System. |
| > Document Version: 2 | 0260310 1 |   |

| roduct Introduction·Vi e cloud | rtual priva Virtual Private Clou |   |
|---|---|---|
|   | VPC support 3AZ | Physical server. |
| ITAI | Intel | Intel |
|   | Hygon | Hygon |
|   | Kunpeng | Kunpeng |
|   | Phytium | Physical server. |
|   | ShenWei | Physical server. |
|   | Support V8 | Physical server. |
|   | Support 8U | Physical server. |
| NICs | Support CX6 dual-port network interface controllers (NICs). | Physical server. |
|   | Support X710 10GE NIC on x86 Hygon. | Physical server. |
|   | XGWdocker supports CX6 dual-port network interface controllers (NICs). | Virtuali gateway. |
|   | VPC supports 100G network access | Physical gateway. |
| Architecture Optimization | XGW supports FRR | FRR (Fast Reroute) protocol restores data flow in network failures. |
| vSwitch | Interaction between vSwitch creation and VPC CIDR | Support the interaction between vSwitch creation and IPv4 CIDR block. |
|   | Interaction between vSwitch creation and VPC CIDR | Support the interaction between vSwitch creation and IPv6 CIDR block. |

**Monitoring and alerting**

| Feature |   | Note |
|---|---|---|
| Alerting | VPC alerts | Alerts are supported. |
| Monitoring | NOE monitoring and O&M | NOE is integrated and runs on the backend, allowing data about VPC resources to be queried. |
|   | AVS Monitoring | AVS is connected to CMS tenant network monitoring. |
|   |   | AVS integrates the monitoring system. |
|   | NAT monitoring | NAT supports tenant monitoring of network inbound bandwidth, outbound bandwidth, and bandwidth usage. |

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
