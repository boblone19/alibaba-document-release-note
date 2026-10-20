---
title: "Server Load Balancer Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 21
source_pdf: "42c1c347d7c96445_Alibaba Cloud Apsara Stack V3.18.6 Server Load Balancer Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Server%20Load%20Balancer%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Server Load Balancer Product Introduction 20260629

## Table of Contents

- 1 What is SLB?
  - 1.1 Service details
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features

## 1 What is SLB?

This topic provides an overview of Server Load Balancer (SLB). SLB distributes inbound network traffic across multiple Elastic Compute Service (ECS) instances that function as backend servers based on forwarding rules. You can use SLB to improve the responsiveness and availability of your applications.

**Overview**

After you attach ECS instances that are deployed in the same region to an SLB instance, SLB uses virtual IP addresses (VIPs) to virtualize these ECS instances into backend servers in a high-performance server pool that ensures high availability. Client requests are distributed to the ECS instances based on forwarding rules. SLB checks the health status of the ECS instances and automatically removes unhealthy ones from the server pool to eliminate single points of failure (SPOFs). This enhances the resilience of your applications.

**Components**

SLB consists of three components: SLB instances An SLB instance is a running SLB service entity that receives traffic and distributes traffic to backend servers. To get started with SLB, you must create an SLB instance, configure at least one listener for the SLB instance, and attach at least two ECS instances to the SLB instance. Listeners A listener checks client requests and forwards them to backend servers. It also performs health checks on backend servers. Backend servers ECS instances are used as backend servers to receive distributed requests. You can add ECS instances one by one to the server pool, or use vServer groups or primary/secondary server groups to add and manage multiple ECS instances at a time.

**Benefits**

High availability SLB is designed with full redundancy that prevents SPOFs and supports zone-disaster recovery. SLB can be scaled based on application loads and can provide continuous services during traffic fluctuations. High scalability You can increase or decrease the number of backend servers to adjust the load balancing capability of your applications. High cost efficiency SLB can save 60% of load balancing costs compared with traditional hardware solutions. Outstanding security You can integrate SLB with Apsara Stack Security to defend your applications against DDoS attacks of up to 5 Gbit/s. High concurrency An SLB cluster supports hundreds of millions of concurrent connections. A single SLB instance supports tens of millions of concurrent connections.

### 1.1 Service details

The Server Load Balancer (SLB) service consists of SLB instances, listeners, and backend servers.

**SLB instances**

An SLB instance is a running entity of the SLB service that receives and distributes traffic to backend servers. To get started with SLB, you must create an SLB instance and add at least one listener and two Elastic Compute Service (ECS) instances to the SLB instance. SLB allows you to list, query, create, update, and delete SLB instances. You can also add ECS instances to and remove ECS instances from SLB instances.

**Listeners**

A listener is used to check client requests and forward the requests to one or more backend servers. TCP, UDP, HTTP, and HTTPS listeners are supported. Listeners can perform health checks on backend servers and automatically isolate unhealthy backend servers.

**Backend servers**

Backend servers are ECS instances that are added to an SLB instance to receive requests. You can add individual ECS instances to the default server group of an SLB instance. You can also add multiple ECS instances to vServer groups or primary/secondary server groups.

### 1.2 Benefits

Server Load Balancer provides high availability, scalability, low cost, security, and high concurrency. This topic describes the high availability benefits of Server Load Balancer for single SLB instances, multiple SLB instances, and backend ECS instances.

**High availability**

Server Load Balancer uses a fully redundant design with no single point of failure and supports Multi-zone Disaster Recovery. It scales out elastically based on your application's payload. This ensures that services remain available during traffic fluctuations.

| Object | Description of high availability benefits |
|---|---|
| Server Load Balancer | SLB instances are deployed in a cluster to enable session synchronization. This eliminates single points of failure, improves redundancy, and ensures service stability. Layer 4 load balancing is implemented using Linux Virtual Server (LVS) with keepalived. Layer 7 load balancing is implemented using Tengine. Tengine is a web server project that is based on Nginx and optimized for high-traffic websites. Requests from the Internet reach the LVS cluster through Equal-Cost Multipath Routing (ECMP). Each LVS server in the cluster uses multicast messages to synchronize sessions with other LVS servers in the same cluster. This ensures session synchronization across all servers in the LVS cluster. The LVS cluster also performs health checks on the Tengine cluster. Server Load Balancer removes abnormal devices from the Tengine cluster to ensure the availability of Layer 7 load balancing. |
| Single SLB instance | Alibaba Cloud lets you create multi-zone deployments in a region to achieve high availability for a single SLB instance. If the primary zone fails or becomes unavailable, Server Load Balancer can switch to the secondary zone and resume service in about 30 seconds. When the primary zone recovers, Server Load Balancer automatically switches back to the primary zone. |
| High availability of multiple SLB instances | If you have extremely high availability requirements, the built-in availability mechanisms of a single SLB instance might not be sufficient. For example, if an SLB instance becomes unavailable due to a network attack or a configuration error, a zone-level failover is not triggered. This is because the issue is not a zone-wide fault. In this case, you can create multiple SLB instances and use Alibaba Cloud DNS to schedule traffic. You can also use a global load balancing solution to implement cross-region disaster recovery and backup. |
| High availability of backend ECS instances | Server Load Balancer uses health checks to determine the availability of backend ECS instances. The health check mechanism improves the overall availability of your frontend application. It prevents abnormal backend ECS instances from affecting your service. After you enable health checks, if a backend ECS instance becomes unhealthy, Server Load Balancer automatically forwards new requests to other healthy ECS instances. When the unhealthy instance recovers, Server Load Balancer automatically restores it to the service. For more information about health checks, see Health check overview in the User Guide. |

**Scalability**

You can add or remove backend servers at any time to scale your application's service capacity as needed.

**Low cost**

Server Load Balancer costs less than traditional hardware load balancers. This protects your investment.

**High concurrency**

A cluster can support tens of millions of concurrent connections. A single instance can support millions of concurrent connections.

### 1.3 Scenarios

Server Load Balancer (SLB) is suitable for scenarios where you want to handle large volumes of traffic, scale applications, eliminate single points of failure (SPOFs), and implement crosszone or cross-region disaster recovery.

**Handle large volumes of traffic**

SLB instances route traffic to Elastic Compute Service (ECS) instances that act as backend servers based on listening rules. This allows you to avoid overloaded servers that may negatively affect user experience. The session persistence feature can be used to forward all requests from a client to the same backend ECS instance to improve access efficiency.

**Scale applications**

SLB can be used as traffic ingress points for both web servers and application servers. This allows you to scale the service capability of your applications by adding or removing backend ECS instances in response to business requirements.

**Eliminate SPOFs**

SLB instances act as the single point of contact for clients. You can add multiple ECS instances to an SLB instance. When an ECS instance malfunctions, SLB automatically isolates the ECS instance and distributes inbound requests to other healthy ECS instances. This ensures that your applications continue to run as expected.

**Implement zone-disaster recovery (multi-zone disaster**

**recovery)**

To provide more stable and reliable load balancing services, SLB supports cross-zone deployment in most regions. You can deploy an SLB instance across multiple zones within the same region to improve disaster tolerance and ensure the reliability of your applications. When the primary zone fails or has no healthy ECS instances, the SLB instance automatically fails over services to the secondary zone. This process is completed within 30 seconds. When the primary zone recovers, the SLB instance automatically switches services back to the primary zone. You can plan the deployment of backend servers based on your business needs. We recommend that you add at least one backend server in each zone to maximize the load balancing capabilities of SLB. ECS instances that reside in different zones can be added to an SLB instance. Under normal circumstances, the SLB instance evenly distributes inbound traffic to ECS instances in the primary zone (Zone A) and to those in the secondary zone (Zone B). If Zone A fails, the SLB instance distributes inbound traffic only to ECS instances in Zone B. This deployment mode is tolerant to zone-level failures at the expense of latency. However, you can deploy core services across zones to make up for this.

**Implement cross-region disaster recovery**

You can deploy SLB instances in different regions and add the ECS instances of different zones within each of these regions to the SLB instance in the same region. You can use Alibaba Cloud DNS to resolve domain names to the service addresses of SLB instances in different regions for global load balancing. When a region becomes unavailable, you can temporarily stop DNS resolution in the region without affecting traffic to your applications.

### 1.4 Features

This topic describes the features of Alibaba Cloud Server Load Balancer (SLB). SLB supports Layer 4 and Layer 7 load balancing. It provides health checks, session persistence, and domain forwarding to ensure high availability for backend services.

**SLB Instances**

| Feature |   | Description |
|---|---|---|
| SLB instance management | Modify instance properties | You can edit the name and description of an SLB instance. |
|   | Create an instance | You can create an SLB instance and specify a scheduling algorithm. |
|   | Delete an instance | You can delete an existing SLB instance. |
|   | Start or stop an instance | You can start or stop a specified SLB instance. |
|   | View instance details | You can view the detailed configuration of a specified SLB instance. |
|   | SLB configuration details | You can import or export SLB configuration details. |
|   | Medium I slb.s2.small | Maximum connections: 50,000 New connections per second (CPS): 5,000 Queries per second (QPS): 5,000 |
|   | Small I slb.s1.small | Maximum connections: 5,000 New connections per second (CPS): 3,000 Queries per second (QPS): 1,000 |
|   | Large I slb.s3.small | Maximum connections: 200,000 New connections per second (CPS): 50,000 Queries per second (QPS): 30,000 |

| SLB instance types |   |   |
|---|---|---|
|   | Large II slb.s3.medium | Maximum connections: 500,000 New connections per second (CPS): 20,000 Queries per second (QPS): 20,000 |
|   | Super large I slb.s3.large | Maximum connections: 1,000,000 New connections per second (CPS): 100,000 Queries per second (QPS): 50,000 |
|   | Medium II slb.s2.medium | Maximum connections: 100,000 New connections per second (CPS): 10,000 Queries per second (QPS): 10,000 |
|   | slb.i40g.large | Maximum connections: 5,020,000 New connections per second (CPS): 500,000 Queries per second (QPS): 100,000 |
|   | slb.i20g.large | Maximum connections: 5,020,000 New connections per second (CPS): 500,000 Queries per second (QPS): 100,000 |
| IPv6 | 6to4 support | 6to4 is supported. |
|   | 6to6 support | Supports IPv6-to-IPv6 translation. |
|   | Multi-zone Disaster Recovery for IPv6 | SLB supports Multi-zone Disaster Recovery for IPv6. |
|   | SLB supports attaching to the classic IPv6 network over the public network. | SLB supports attaching classic IPv6 networks to the public network. |

**Listeners**

| Feature |   | Description |
|---|---|---|
| Listener | Create a listener | You can create a Layer 4 or Layer 7 listener and configure health checks to ensure the availability of backend servers. |
|   | Delete a listener | You can delete a specified listener from the load balancer. This action stops the port from receiving and distributing requests. |
|   | Start or stop a listener | You can start or stop a listener to control whether it receives and distributes requests. |
|   | Edit a listener | You can modify the configuration of an existing listener, such as its port, protocol, or advanced settings. |
|   | Session persistence | SLB uses cookies to maintain session persistence. This ensures that requests from the same user session are routed to the same backend server. |
|   | Health check | SLB automatically monitors the health status of backend servers and forwards requests only to healthy servers. HTTP health check: Confirms the server status using HTTP requests. TCP health check: Confirms the server status using TCP handshakes. |
|   | Listener support | You can configure the listener protocol. HTTP: You can set the listener port and protocol type as required. HTTPS: You can set the listener port and protocol type as required. |

| Layer 7 listeners |   |   |
|---|---|---|
|   | Application protocol support | SLB supports multiple protocols, such as HTTP 1.0/1.1/2.0 and WebSocket(S). |
|   | Support for gzip compression | Gzip compresses data during transmission to reduce bandwidth usage and improve efficiency. |
|   | Support for HTTP redirection | You can configure automatic redirection from HTTP to HTTPS. This configuration ensures data security and maintains compatibility for users who access services using legacy links. |
|   | IPv6 access to backend servers | Supports the IPv6 protocol. |
|   | Layer 7 content-based load balancing | You can configure domain name or URL forwarding rules to route requests to different backend servers. |
|   | Certificate management | SLB provides certificate hosting and offloading to help reduce certificate licensing costs. |
|   | Forwarding rule | Layer 7 load balancing supports domain name or URL forwarding rules. These rules route requests from different domain names or URLs to different ECS instances. |
|   | Scheduling algorithm | SLB supports multiple load balancing scheduling algorithms to optimize traffic distribution. Round Robin (RR): Distributes requests to backend servers in sequence. Weighted Round Robin (WRR): Distributes requests based on the configured weights of backend servers. |

| Layer 4 listeners | Session persistence | SLB maintains session persistence based on the source IP address. This ensures that requests from the same client are routed to the same backend server during a session. |
|---|---|---|
|   | Health check | SLB automatically monitors the health status of backend servers and forwards requests only to healthy servers. HTTP health check: Confirms the server status using HTTP requests. TCP health check: Confirms the server status using TCP handshakes. |
|   | Listener support | You can configure the listener protocol. TCP: You can set the listener port and protocol type as required. UDP: You can set the listener port and protocol type as required. |
|   | IPv6 access to backend servers | Supports the IPv6 protocol. |
|   | Scheduling algorithm | SLB supports multiple load balancing scheduling algorithms to optimize traffic distribution. Round Robin (RR): Distributes requests to backend servers in sequence. Weighted Round Robin (WRR): Distributes requests based on the configured weights of backend servers. Consistent Hashing (CH): Uses a hash algorithm that is based on the source IP address. This ensures that requests from a specific client are always assigned to the same backend server. |

| Forwarding rule | Configure a forwarding rule | Layer 7 load balancing supports domain name or URL forwarding rules. These rules route requests from different domain names or URLs to different ECS instances. |
|---|---|---|
|   | Graceful connection termination for SLB Layer 4 | SLB Layer 4 supports graceful connection termination. If you remove a backend server or if a health check fails, existing connections continue to operate for a specified period. |
|   |   | The graceful termination period can be set to a maximum of 900 seconds. |
| Session persistence | Source IP address and cookie- based session persistence | SLB supports session persistence based on the source IP address and cookies. |
|   | Long-lived connections remain active during hot migration of applications | SLB supports long-lived connections that remain active during hot migration of backend applications. |

**Backend Servers**

| Feature |   | Description |
|---|---|---|
| Backend servers | Modify the weight of an ECS instance | Modify the weight of an added ECS instance. Higher-weighted ECS instances receive more requests. Set weights based on the service capacity of each ECS instance. |
|   | Add a backend server | Add an ECS instance to handle connection requests forwarded from the frontend. |
|   | Remove an ECS instance | Remove an ECS instance from the SLB instance. |
|   | Backend servers support descriptions | Backend servers support descriptions. |

| Default server group | Add a backend server | Add an ECS instance to handle connection requests forwarded from the frontend. |
|---|---|---|
|   | View the default server group | View the status and port configuration of ECS instances in the server group. |
|   | Edit a backend server | Modify the weight of an added ECS instance. Higher-weighted ECS instances receive more requests. Set weights based on the service capacity of each ECS instance. |
|   | Remove a backend server | Remove an ECS instance from the SLB instance. |
| vServer group | Create a vServer group | Create a server group. A server group is a collection of ECS instances. By associating different listeners with different server groups, SLB can route different requests to different ECS instances. |
|   | View a vServer group | View the status and port configuration of ECS instances in the server group. |
|   | Edit a vServer group | Rename the server group. Modify the weights of ECS instances in the group. Add new ECS instances or remove existing ones. |
|   | Delete a vServer group | Delete a specified server group. Remove associated ECS instances from the SLB instance. |
|   | SLB vServer group | vServer groups display associated listener information. |

| Primary/secondary server group | Create a primary/secondary server group | A primary/secondary server group contains one primary server and one secondary server. When the primary server is healthy, traffic is routed to it. When the primary server fails, traffic switches to the secondary server group. |
|---|---|---|
|   | Delete a primary/secondary server group | Delete a specified primary/secondary server group. |
|   | Support for primary/secondary server groups and primary/secondary IPAM pools | Customize the number of real servers (RS) behind the primary and secondary servers in a primary/secondary server group. |

**Access Control**

| Feature |   | Description |
|---|---|---|
| Access control | Create and manage policy groups | Specify which IP addresses can access the SLB service by configuring listener-level access control policy groups. |
|   | Modify the access control quota limit | Provide a page to increase the access control quota limit. |

**Certificate Management**

| Feature |   | Description |
|---|---|---|
| Certificate | Upload a certificate | Store certificates in the SLB certificate management system instead of deploying them directly to backend ECS servers. Private keys uploaded to the certificate management system are encrypted at rest. |
| Chinese cryptographic algorithm | Support for Chinese cryptographic algorithms | When clients encrypt messages using Chinese cryptographic algorithms (client support required), SLB can decrypt the encrypted messages. |

**Monitoring and Alerting**

| Feature |   | Description |
|---|---|---|
| Monitoring | Multi-dimensional monitoring and comparison | Supports multi-dimensional monitoring. |
|   | Monitor connections between SLB and backend RS | Monitor connections between SLB and backend real servers (RS). |
|   | Operation log | View instance operation logs. |
|   | Fine-grained monitoring | The SLS Pub component requires Simple Log Service, and SLB offers fine-grained monitoring. |
| Alerting | Provide alerting | Provide alerting. |

**Security**

| Feature |   | Description |
|---|---|---|
| Security | Access control list (ACL) | Supports access control lists (ACLs). |
|   | SLB supports blacklists and whitelists | SLB access control uses blacklists to block malicious IP addresses from accessing SLB services. |
|   | SLB whitelist limit | Number of entries allowed in an SLB whitelist. |
|   | Set a listener whitelist | Add a whitelist to specify which IP addresses can access the SLB service. |

**Network Interconnection**

| Feature | Description |
|---|---|

| Network interconnection | Frontend networking capability | Attach an Elastic IP Address (EIP) to an SLB instance. This allows a virtual private cloud (VPC) SLB instance to accept traffic from the Internet. |
|---|---|---|
|   | Backend networking capability | Attach a load balancer directly to an Elastic Network Interface (ENI) for flexible network configuration. |
|   |   | Configure multiple secondary IP addresses on an ENI and use them as backend servers for SLB. |
|   |   | Connect to on-premises IDCs using leased lines. Connect to on-premises IDCs using the Internet. |
|   |   | Attach ECS instances across multiple zones to improve system availability and disaster recovery capability. |

**Cluster Scalability**

| Feature |   | Description |
|---|---|---|
| Cluster scalability | Multi-zone Disaster Recovery in multi-cluster mode | In multi-cluster mode, SLB supports Multi-zone Disaster Recovery. If the primary cluster fails, traffic is switched to the secondary cluster. |
|   | Multi-cluster deployment for physical SLB servers | You can create SLB instances in a specified cluster. |
|   |   | Supports tenant-based multi- cluster isolation. |
|   | Horizontal scaling within a cluster | SLB supports horizontal scaling within a cluster. |
|   |   | You can scale out to the maximum number of supported nodes. |

**High Availability and High Performance**

| Feature |   | Description |
|---|---|---|
| High availability | Cross-zone disaster recovery | Virtual IP address (VIP) cross- zone disaster recovery. |
|   | Support for multiple regions | Supports multiple regions. |
| High performance | SLB supports 100 Gbps network architecture | Physical servers support 100 Gbps network architecture. |
|   | SLB supports 100 Gbps network architecture | Virtualized gateways support 100 Gbps network architecture. |
| Multiple data centers | SLB supports Multi-region 2.0 | Business Foundation System (BFS) unitization: physical servers. |
|   | SLB supports 3-AZ deployment | Supports physical server deployment. |
| Real server (RS) hot migration | SLB maintains long-lived TCP connections during hot migration of clients or backend real servers (RS) | Long-lived TCP connections remain active during hot migration of cloud hosts. This improves infrastructure stability and application decoupling. For ECS acting as clients or RS, TCP connections remain active during hot migration. LVS must support inner-layer RSS (for 40 Gbps hardware). |

**Hardware Compatibility and Product Forms**

| Feature |   | Description |
|---|---|---|
|   | Intel | Supports physical server deployment. |
|   | Hygon | Supports physical server deployment. |
|   | Kunpeng | Supports physical server deployment. |
|   | Phytium | Supports physical server deployment. |

| Domestic Software and Hardware Ecosystem |   |   |
|---|---|---|
|   | Support for V8 | Supports physical server deployment. |
|   | Support for 8U | Supports physical server deployment. |
|   | Intel support for virtualized gateway SLB | Virtualization gateways are supported. |
|   | Hygon support for virtualized gateway SLB | Supports virtualization gateways. |
|   | V8 support for virtualized gateway SLB | It supports virtualization gateway. |
|   | 8U support for virtualized gateway SLB | Support for virtualization gateways. |
| Network Interface Controller (NIC) | ConnectX-5 NICs | Supported for physical server deployments. |
|   | Dual-port ConnectX-6 NICs | Supported for physical server deployments. |
|   | ConnectX-5 NICs for virtualized SLB | Supported for virtualized gateways. |
|   | Dual-port ConnectX-6 NICs for virtualized SLB | Supported for virtualized gateways. |
|   | LVS on Docker | Supports containerized deployment. |
|   | Multi-zone Disaster Recovery for LVS on Docker | Supports Multi-zone Disaster Recovery. |
|   | Proxy on NFV | Supports Network Functions Virtualization (NFV) on ECS deployment. |
|   | Multi-zone Disaster Recovery for Proxy on NFV | Supports Multi-zone Disaster Recovery. |

| Virtualized gateway |   |   |
|---|---|---|
|   | KeyServer on NFV | Supports NFV on ECS deployment. |
|   | Multi-zone Disaster Recovery for KeyServer on NFV | Supports Multi-zone Disaster Recovery. |
|   | Chinese cryptographic algorithm support for SLB on NFV | Supports Chinese cryptographic algorithms. |
|   | The Virtualized Gateway SLB supports attaching to on-premises IDCs. | The virtualized gateway SLB supports Layer 4 attachment to on- premises Internet Data Centers (IDCs). |
|   | Support for multi- region architecture | SLB supports a unitized architecture for multi-region deployments. |
