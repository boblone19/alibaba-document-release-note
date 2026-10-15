---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 TransitRouter Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 TransitRouter Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%BD%AC%E5%8F%91%E8%B7%AF%E7%94%B1%E5%99%A8/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20TransitRouter%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 TransitRouter Product Introduction 20260828

## Transit router

TransitRouter (TR) is an enterprise-grade networking solution that enables you to quickly build high-speed, high-quality, and stable connections between virtual private clouds (VPCs) in the same region, along with between multiple VPCs and data centers.

### Product details

Transit Router (TR) supports establishing private network communication channels between virtual private clouds (VPCs) in the same region and between VPCs and data centers. TR also provides rich network interconnection and routing management capabilities, such as forwarding association, route learning, custom route tables, and routing policies. These capabilities allow enterprises to customize network connectivity and help them build flexible, reliable, and large-scale enterprise interconnection networks.

**Network instance connections**

Transit Router supports connections to Virtual Private Cloud (VPC) instances and Virtual Border Router (VBR) instances. VPC instances in the same region can communicate with each other after they are connected to a transit router instance. After a transit router instance is connected to a VBR instance, the data center associated with the VBR instance can communicate with VPC instances connected to the transit router.

**Routing**

Transit Router supports various routing management features, such as forwarding association, route learning, custom route tables, custom route entries, and routing policies. These features help enterprises customize network connectivity.

**Custom route tables**

After a transit router is connected to a network instance, it stores the routes of the network instance in a route table. The transit router forwards traffic from the network instance by querying the route entries in the route table. Each transit router has a default route table and supports the creation of custom route tables. The default route table and custom route tables are isolated from each other, which allows you to implement access isolation.

**Forwarding association**

The forwarding association feature controls traffic forwarding for network instances. After a forwarding association is established between a network instance connection and a transit router route table, the transit router forwards traffic from the network instance by querying the route entries in the route table.

**Route learning**

The route learning feature controls route advertisement for network instances. After a route learning relationship is established between a network instance connection and a transit router route table, the routes of the network instance are allowed to be advertised to the transit router route table.

**Custom route entries**

Route tables of transit routers support custom route entries. You can add custom route entries to a transit router route table to help control traffic forwarding for network instances.

**Routing policies**

A routing policy controls route advertisement for the route table of a transit router. A routing policy can determine whether to advertise routes in a transit router route table to network instances. It can also modify the properties of routes in a transit router route table.

**Multicast**

Transit Router supports multicast traffic forwarding by default. After VPC instances in the same region are connected to a transit router instance, you can establish a multicast network between the VPC instances. You can create a Connect connection under a transit router to connect to a data center. VPC instances under the transit router and the on-premises data center can transmit multicast traffic through the Connect connection to enable multicast network communication between cloud and on-premises environments.

**Health check**

VBRs can connect data centers to Alibaba Cloud through Express Connect circuits. After a VBR instance is connected to a transit router instance, you can use the health check feature to detect the connectivity of the Express Connect circuit.

### Benefits

Transit routers are easy to configure and quickly establish secure, flexible, high-speed, highquality, and stable communication channels between VPCs in the same region and between multiple VPCs and on-premises data centers. This helps enterprises build large-scale enterprise-class interconnection networks.

**Large-scale network interconnection**

Transit routers quickly connect multiple VPC-connected instances and on-premises networks in the same region to enable resource communication. A transit router in the same region supports VPC peering for up to 300 VPCs, meeting enterprise network expansion needs.

**Low latency and high speed**

Transit routers provide low-latency and high-speed network transmission capabilities. The maximum transmission rate between resources in the same region can reach the port forwarding rate of network devices.

**High reliability and high quality**

Transit routers provide primary and secondary nodes that automatically switch between each other to ensure uninterrupted service. Multiple sets of high-quality transmission links exist between any two nodes in the network. When underlying links are interrupted, the network automatically converges without affecting your services.

### Scenarios

Transit Router is used for scenarios such as connecting VPCs in the same region, connecting on-premises and cloud networks in the same region, and enabling multicast network communication.

**Connect VPCs in the same region**

After VPC-connected instances in the same region are connected to a transit router, they can communicate with each other.

**Connect on-premises data centers and VPCs**

When an on-premises data center is connected to a transit router through a VBR instance, it can communicate with VPC-connected instances that are connected to the same transit router in the same region.

**Cloud multicast networks**

After VPC-connected instances in the same region are connected to a transit router, they can communicate with each other through multicast networks via the transit router.

**Connect on-premises and cloud multicast networks**

On-premises data centers can connect directly to a transit router through Connect connections, enabling multicast network communication with VPC instances under the transit router through these Connect connections.

### Functions and features

| Operation |   | Description |
|---|---|---|
| Virtual private cloud (VPC) connections | Connect transit routers to VPCs | You can connect transit routers to VPCs. |
| Virtual border router (VBR) connections | Connect transit routers to VBRs | You can connect transit routers to VBRs. |
| Route tables of transit routers | Create or delete route tables | Multiple route tables may exist on one transit router to implement traffic control of different network partitions. |
|   | Associated route tables | Associated route tables are used to implement routing and forwarding for the network communication between transit routers and other network instances. |
|   | Route learning | You can specify the network instances from which transit routers automatically learns routes. |
|   | Support for static routes | Route tables of transit routers can be configured with static routes. |
|   | Support for routing policies | The route tables of transit routers can control the sending and receiving rules of routes based on routing policies. |

| Multicast management | Create or delete multicast groups | Multiple multicast groups can be created on one transit router, and each multicast group has one multicast IP address. |
|---|---|---|
|   | Add or delete multicast sources | You can manage multicast sources in a multicast group. |
|   | Add or remove multicast members | You can manage multicast members in a multicast group. |
| Multicast | Cloud multicast | Multicast sources and members are in the cloud. |
|   | On-premises and cloud multicast | The multicast sources or multicast members are not in the cloud. |
|   | One network interface card (NIC) works as both a multicast source and a multicast member | The same NIC works as both a multicast source and a multicast member. |
| O&M and Monitoring | Traffic monitoring service connected to VPCs | The traffic between transit routers and VPCs is monitored. |
|   | Traffic monitoring service connected to VRBs | The traffic between transit routers and VBRs is monitored. |
|   | Service-level monitoring of transit routers | Transit routers are connected to CloudMonitor to implement tenant monitoring and management. |
|   | Cluster-level monitoring of transit routers | Transit routers are connected to TianjiMon to implement platform monitoring and management. |
|   | Region-level monitoring of transit routers | Transit routers are connected to TianjiMon to implement platform-side region monitoring and management. |

| Health checks | Cloud Enterprise Network (CEN) instances | You can select CEN instances on which health check is performed. |
|---|---|---|
|   | VBRs | You can select VBRs on which health check is performed. |
|   | Detection IP addresses for health checks | You can specify the source and destination IP addresses. |
|   | Probe interval and probe packets | You can specify the probe interval and the number of probe packets. |
| Multiple clusters | Support for multiple clusters | Transit routers support multi- cluster deployment solutions. |
| Topology display | Display of resource topologies | The basic information about the topologies of cloud services associated with transit routers can be displayed. |
| Quota management | Quota management for transit routers | You can perform quota management on transit routers. |
| Security Protection | Shared security policies for multiple VPCs | Security policies are shared among multiple VPCs. |
| Disaster recovery | Support for zone-disaster recovery | Transit routers support zone- disaster recovery. |
| domestic software and hardware ecology | Support for Intel chip architecture | Transit routers support Intel chip architecture. |
|   | Support for Hygon chip architecture | Transit routers support Hygon chip architecture. |
