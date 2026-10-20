---
title: "Apsara Stack DNS Product Introduction 20250924"
product_version: "V3.18.6"
pdf_pages: 16
source_pdf: "475fa25ac7ae48ee_Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack DNS Product Introduction 20250924.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E8%A7%A3%E6%9E%90DNS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20DNS%20Product%20Introduction%2020250924.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Apsara Stack DNS Product Introduction 20250924

## Table of Contents

- 1 Apsara Stack DNS
  - 1.1 Overview
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features

## 1 Apsara Stack DNS

### 1.1 Overview

Apsara Stack DNS is a service that is encapsulated based on the DNS protocol and runs on Apsara Stack to resolve domain names over internal networks, such as virtual private clouds (VPCs), networks of self-managed data centers, and the classic network. You can configure rules and policies to map domain names to IP addresses. Apsara Stack DNS then distributes the DNS requests from clients to cloud resources, self-managed business applications, business systems on your internal networks, or the service resources of Internet service providers (ISPs).

| Category | Feature | Supported |
|---|---|---|
| Global domain names in Apsara Stack | Global basic DNS resolution | Yes |
|   | Global load balancing (weight) | Yes |
|   | Global domain name forwarding | Yes |
|   | Global default forwarding | Yes |
|   | Internet recursive resolution | Yes |
| Global line | Scheduling domain management | Yes |
| Private domain names for VPCs | Tenant-specific basic DNS resolution | Yes |
|   | Tenant-specific load balancing (weight) | Yes |
|   | VPC association and disassociation | Yes |
|   | Tenant-specific domain name forwarding | Yes |
|   | Tenant-specific default forwarding | Yes |
| Private lines | Scheduling domain management | Yes |
| Global scheduling | Scheduling instance management (multi- cloud) | Yes |
| > Document Version: 2025 | 0924 |   |

| roduct Introduction·Apsar DNS | a Stac Apsara Stack DN |   |
|---|---|---|
|   | Address pool management (multi-cloud) | Yes |
| Cross-cloud shared domain names | Global basic DNS resolution (multi-cloud) | Yes |
| ISP line | ISP line management (multi-cloud) | Yes |
| Node management | Synchronization cluster management (multi- cloud) | Yes |
| Log management | Log management (multi-cloud) | Yes |

**DNS**

DNS is a distributed database used for TCP/IP applications. It translates domain names into IP addresses and selects paths for emails.

**Domain name resolution**

Domain name resolution maps domain names to IP addresses by using DNS. It includes both authoritative resolution and recursive resolution.

**Recursive resolution**

Recursive resolution queries domain names cached on the local DNS server or sends a request to the authoritative DNS system to obtain the corresponding IP addresses. You can use recursive resolution to resolve Internet domain names.

**DNS forwarding**

DNS forwarding uses two DNS servers to provide DNS resolution services. The local DNS server is used to configure and manage the domain name resolution data. The other DNS server is used to resolve domain names.

**Default forwarding**

If DNS queries for authoritative domain names are not resolved by the local DNS server, they are forwarded to another DNS server for resolution.

### 1.2 Benefits

Apsara Stack DNS is a key network service that controls data traffic for Apsara Stack. This service resolves domain names, balances and schedules server loads, and connects Apsara Stack with self-managed data centers. Apsara Stack DNS provides a complete suite of solutions to deploy a cloud environment, achieve high availability and disaster recovery for data centers, and balance server loads to secure your IT services. You can perform the following operations by using Apsara Stack DNS in enterprise intranets: Access other Elastic Compute Service (ECS) instances deployed in the current virtual private cloud (VPC). Access other cloud service instances on Apsara Stack. Access the custom business systems of your enterprise. Access services over the Internet. Use the global server load balancing (GSLB) feature to implement multi-active solutions and disaster recovery, such as local active-active disaster recovery, active zoneredundancy, remote active-active disaster recovery, active geo-redundancy, and geodisaster recovery. Connect to Apsara Stack DNS with your own DNS servers over a leased line.

**Enterprise domain name management**

Apsara Stack DNS provides management and resolution services for your enterprise domain names. It supports the following operations: Perform forward and reverse DNS lookups for domain names of cloud service instances, such as ECS instances. Perform forward and reverse DNS lookups for your internal domain names. Add, modify, and delete DNS records of the following types: A, AAAA, CNAME, MX, PTR, TXT, SRV, NAPTR, CAA, and NS. Add multiple A, AAAA, and PTR records for a hostname of a domain name. The system returns all record values by default through random round-robin to achieve load balancing. Add multiple A, AAAA, and CNAME records for a hostname of a domain name. The system returns a record value based on the weights configured for the record values of these records to achieve load balancing.

**Flexible integration with data centers**

Apsara Stack DNS can forward enterprise domain names and provide the following services for you to flexibly build your network and cascade Apsara Stack DNS servers with the DNS servers that you create: Global default forwarding Query forwarding for specific domain names

**Internet access from enterprise servers**

Apsara Stack DNS supports recursive resolution for Internet domain names, which allows your servers to access the Internet.

**Tenant isolation**

Apsara Stack DNS allows you to manage private zones in VPCs, resolve internal domain names, and isolate DNS records and resolution based on tenants. You can use Apsara Stack DNS to isolate data by VPC without the need to build your own DNS system. This helps reduce server and O&M costs. This feature is available only in Apsara Stack DNS Standard Edition.

**GTM-based management**

Global Traffic Manager (GTM) achieves nearby access to application services and load balancing in high-concurrency scenarios. GTM can implement traffic switchover based on health check results. This allows you to build active zone-redundancy and geo-disaster recovery services in a flexible and efficient manner. GSLB provides the following features in enterprise intranets: Allows you to add multiple records for a hostname of a domain name. The system returns a record value based on the weights configured for the record values of these records to achieve load balancing. Supports scheduling line management. You can customize lines and their priorities to allow clients to access the nearest nodes and implement intelligent traffic scheduling based on geographical locations and application groups. This accelerates access to applications. Synchronizes DNS configuration data among multiple clusters for which GTM is activated. This feature is supported in multi-cloud scenarios. Supports address pool management. You can manage your applications in a centralized manner by application service cluster. Supports custom global scheduling domains. You can manage and code global scheduling instances in a centralized manner based on your naming conventions.

**Unified management platform**

You can access DNS and any other cloud services on the Apsara Uni-manager Management Console with one account. This provides the following benefits: Apsara Stack DNS supports web operations for data and service management, which facilitates your use of the DNS service. Apsara Stack DNS is deployed on clusters. You can add more clusters based on your needs. You can deploy Apsara Stack DNS in multiple zones. Apsara Stack DNS supports local active-active and zone-disaster recovery. Apsara Stack DNS is deployed in anycast mode, which delivers high availability and disaster recovery.

**API operations**

Apsara Stack DNS provides API operations so that you can integrate it with other systems.

### 1.3 Scenarios

Apsara Stack DNS is a key network service that controls data traffic for Apsara Stack. This service resolves domain names, balances and schedules server loads, and connects Apsara Stack with self-managed data centers and Alibaba Cloud. Apsara Stack DNS provides a complete suite of solutions to deploy a cloud environment, achieve high availability and disaster recovery for data centers, and balance server loads to secure your IT services.

**Basic DNS resolution**

**Access cloud resource instances in a VPC**

You can use Apsara Stack DNS to access ApsaraDB RDS, Server Load Balancer (SLB), and Object Storage Service (OSS) instances from the Elastic Compute Service (ECS) instances or Docker instances in a virtual private cloud (VPC).

**Access ECS instances or Docker instances by using hostnames**

**in a VPC**

You can create hostnames for the ECS instances or Docker instances in a VPC based on the rules that you define, and access and manage these instances by using the hostnames.

**Access the domain names of internal services in a VPC**

You can develop your own Platform as a Service (PaaS) or Software as a Service (SaaS) services on Apsara Stack and expose these services internally through domain names. Services can be deployed in multiple data centers or regions. Tenants can access the deployed services by using domain names in the relevant VPC.

**Schedule the requests to internal services on Apsara Stack by**

**using the round-robin algorithm**

You can use Apsara Stack DNS to access a deployed SaaS service and evenly distribute requests to different nodes in a VPC.

**Access Internet services from a VPC or the classic network**

You can use Apsara Stack DNS to access Internet services from a VPC or the classic network.

**Establish connections between Apsara Stack and other**

**networks**

You can use Apsara Stack DNS to connect your internal network, a public cloud network, or other external networks to Apsara Stack to implement DNS resolution.

**Tenant isolation**

**Isolate tenant resources on Apsara Stack**

You can use Apsara Stack DNS to isolate tenant resources on Apsara Stack. The internal DNS records and the default forwarding configurations of each tenant are isolated from those of other tenants. Tenants can configure their own private DNS records to complete service addressing and scheduling.

**Establish connections among global resources on Apsara Stack**

If you want to allow all tenants to share global resources and configurations on Apsara Stack, system administrators can configure global DNS records and settings to complete service addressing and scheduling.

**Perform VPC-based intelligent scheduling on Apsara Stack**

You can use Apsara Stack DNS to provide different resolution results for different VPCs of a tenant based on the same hostname.

**Global scheduling**

You can develop your own PaaS or SaaS services on Apsara Stack and expose these services internally through domain names. Services can be deployed in multiple data centers or regions.

**Schedule the traffic loads of internal network services on**

**Apsara Stack based on weights**

You can use Apsara Stack DNS to access a deployed PaaS or SaaS service from within or outside the cloud and distribute requests to different nodes in backend service clusters based on the weights of these nodes.

**Schedule the traffic loads of internal network services on**

**Apsara Stack based on the geographical locations of request**

**sources or the application groups to which request sources**

**belong**

You can use Apsara Stack DNS to access a deployed PaaS or SaaS service from within or outside the cloud and distribute requests to different nodes based on the geographical locations or application groups of the request sources.

**Enterprise disaster recovery**

You can develop your own PaaS or SaaS services on Apsara Stack and expose these services internally through domain names. Services can be deployed in multiple data centers or regions.

**Schedule the traffic loads of internal network services on**

**Apsara Stack to achieve disaster recovery**

You can use Apsara Stack DNS to access a deployed PaaS or SaaS service from within or outside the cloud and switch the access traffic of internal services from backend service cluster A (primary data center) to backend service cluster B (secondary data center) in a disaster recovery scenario.

### 1.4 Features

Apsara Stack DNS provides the DNS resolution and Global Server Load Balancer (GSLB) services in VPCs, networks of self-managed data centers, and the classic network.

**Global Traffic Manager (GTM)**

| Feature |   | Description |
|---|---|---|
| Address pool | Health check | The health check for address pools using protocols such as TCP, UDP, HTTP, HTTPS, and ICMP is supported. |
|   | Address pool management | You can add, modify, comment, and delete address pools at a time. You can also perform fuzzy search based on keywords to manage application service clusters. |
|   | Address Type | The supported addresses can be IPv4 addresses, IPv6 addresses, or domain names. This meets the configuration requirements of common application services. |
|   | Load Balancing Policy | The system supports the following load balancing policies for DNS records, each of which can contain multiple IP addresses: round- robin (ALLRR) and WRR. These load balancing policies can help distribute global traffic to different applications. |

| Data synchronization management | GTM data synchronization | Real-time synchronization of scheduling configuration data, such as scheduling instances, address pools, IP address configurations, and scheduling domains, among multiple GTM nodes. The cluster can work normally when less than half of the nodes fail. |
|---|---|---|
|   | GTM cluster management | You can merge multiple GTM clusters to form a large GTM cluster |
|   | Rebuild a GTM cluster | Clusters can be rebuilt in single-data center or multi-data center failure scenarios to ensure business continuity. |
|   | Merge GTM Control Domain | You can merge multiple GTM clusters to form a large GTM cluster |
|   | Emergency group | Clusters can be rebuilt in single-data center or multi-data center failure scenarios to ensure business continuity. |
| Scheduling domains | Scheduling domain management | You can add, modify, comment, and delete scheduling domains at a time. You can also perform fuzzy search based on keywords to customize private scheduling domains. |
| Scheduling instances | CNAME Settings | Each scheduling instance supports a custom CNAME access domain name to resolve configuration records. |
|   | Address pool switchover | You can configure primary and secondary address pools for scheduling instances to achieve automatic switchover between the primary and secondary address pools based on their health check results. |
|   | IP address-based Access Policy | You can configure multiple access policy for each scheduling instance. Separate access policy can be configured for different lines (corresponding to the DNS request source) to implement intelligent traffic scheduling. |
|   | Scheduling instance management | You can add, modify, comment, and delete scheduling instances at a time. You can also perform fuzzy query based on keywords to manage scheduling instances. |

| Resolution line management | IP address line configuration | Lines can be created based on client IP addresses and more than one route can be configured for each source CIDR block. In addition, priorities can be configured for routes that belong to the same source CIDR block. |
|---|---|---|

**Management and resolution of authoritative domain names**

| Feature |   | Note |
|---|---|---|
| Internal DNS resolution management | Authoritative domain name management | Apsara Stack DNS allows you to add, modify, remove, or batch delete authoritative domain names or add remarks. Fuzzy match based on keywords is also supported. This allows users to customize a DNS resolution service for each VPC to implement VPC-level tenant isolation. |
|   | DNS record management | Apsara Stack DNS allows you to add, modify, remove, and batch delete DNS records of the following types: A, AAAA, CNAME, NS, MX, TXT, SRV, PTR, NAPTR, CAA, and SOA. Fuzzy search is supported by keyword. |
|   | Load balancing policy | Each of the following types of DNS records can contain multiple IP addresses: A, AAAA, and CNAME. The system supports the following load balancing policies for DNS records, each of which can contain multiple IP addresses: round- robin (ALLRR) and WRR. These load balancing policies can help distribute global traffic to different applications. |
| PrivateZone (DNS Standard Edition only) | Custom DNS authoritative DNS resolution service for VPC | Users can associate DNS query forwarding rules with VPCs or disassociate DNS query forwarding rules from VPCs. Users can also query associations between authoritative domain names and VPCs. |
|   | Authoritative domain name management | You can add, modify, remove, or batch delete authoritative domain names or add remarks. Fuzzy match based on keywords is also supported. This allows users to customize a DNS resolution service for each VPC to implement VPC-level tenant isolation. |
|   | DNS record management | Apsara Stack DNS allows you to add, modify, and delete DNS records of the following types: A, AAAA, CNAME, NS, MX, TXT, SRV, PTR, NAPTR, CAA, and SOA. Fuzzy search is supported by keyword. |

|   | Load Balancing Policy (Among Addresses) | Each of the following types of DNS records can contain multiple IP addresses: A, AAAA, and CNAME. The system supports the following load balancing policies for DNS records, each of which can contain multiple IP addresses: round- robin (ALLRR) and WRR. These load balancing policies can help distribute global traffic to different applications. |
|---|---|---|

**Forwarding and recursion configuration management and**

**resolution**

| Feature |   | Note |
|---|---|---|
| Global internal network forwarding configuration | Domain name forwarding configuration management | You can add, modify, comment, remove, and delete forwarding configurations based on domain names. You can also perform fuzzy search based on keywords to perform undifferentiated global forwarding DNS resolution services over all VPCs and classic network. |
|   | Default forwarding mode | Apsara Stack DNS can forward requests with or without recursion. In non-recursive forwarding mode, only the specified DNS server is used to resolve domain names. If the resolution fails or times out, a message is returned to the DNS client to indicate that the current request fails. In the mode of forwarding with recursion, the specified DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used. |
|   | Default forwarding configuration management | You can enable, modify, and disable the default forwarding configuration. This way, you can forward the DNS resolution over all VPCs and classic network. |
|   | VPC-based custom DNS forwarding service | Users can associate DNS query forwarding rules with VPCs or disassociate DNS query forwarding rules from VPCs. Users can also query associations between authoritative domain names and VPCs. |
|   | Domain name forwarding configuration management | You can add, modify, remove, or batch delete authoritative domain names or add remarks. Fuzzy match based on keywords is also supported. This allows users to customize a DNS resolution service for each VPC to implement VPC-level tenant isolation. |

| Tenant forwarding configurations |   |   |
|---|---|---|
|   | Forwarding mode | Public DNS can forward requests with or without recursion. In non-recursive forwarding mode, only the specified DNS server is used to resolve domain names. If the resolution fails or times out, a message is returned to the DNS client to indicate that the current request fails. In the mode of forwarding with recursion, the specified DNS server is preferentially used to resolve domain names. If the resolution fails, the local DNS server is used. |
|   | Default forwarding configuration management | You can add, modify, remove, or batch delete authoritative domain names or add remarks. Fuzzy match based on keywords is also supported. This allows users to customize a DNS resolution service for each VPC to implement VPC-level tenant isolation. |

**Characteristics**

| Feature |   | Description |
|---|---|---|
| Low latency | Low-latency DNS services | Apsara Stack DNS supports Anycast IP addresses and provides seamless data center service switchover in disaster recovery scenarios. |
| Hybrid cloud | System cascade | Supports interconnection with external DNS systems and interconnection between hybrid clouds through domain name forwarding. |
| Quick update | The time when data delivery takes effect. | The changes for domain names take effect within 5 seconds. The effective time for changes in domain names within a VPC is not affected by TTL. |
| Access Control | Traffic throttling for individual requests | The throttling for DNS requests is supported for VPCs. By default, the Throttling Threshold is set to 50,000 QPS for a single VPC and 3,000QPS for a single source IP address in a single VPC. |
| High availability | High-availability resolution service | Apsara Stack DNS supports Anycast IP addresses and provides seamless data center service switchover in disaster recovery scenarios. |
|   | Multi-region Architecture 2.0 | DNS supports the multi-region 2.0 solution. |

**O&M and monitoring**

| Feature |   | Note |
|---|---|---|
| O&M logs | DNS Logs | Supports DNS resolution logs to facilitate DNS tracing and troubleshooting. |
| Statistical monitoring | QPS Statistics | QPS(Query Per Second) statistics are supported to measure the performance of the DNS resolution service. |
|   | Success Rate | Supports statistics on the success rate of DNS resolution to determine the quality of DNS resolution in the current network. When the resolution success rate decreases, a large number of domain names fail to be accessed and administrator intervention is required. |
|   | Average Resolution Latency | The average DNS resolution latency is supported. If the resolution latency is high, a large number of external domain names are accessed. In this case, a random domain name attack may occur and administrator intervention is required. |

**Other features**

| Feature |   | Description |
|---|---|---|
| OpenAPI | API service capabilities | Apsara Stack DNS provides API operations so that you can integrate it with other systems. |
| Resolution line management | IP address line configuration | Lines can be created based on client IP addresses and more than one route can be configured for each source CIDR block. In addition, priorities can be configured for routes that belong to the same source CIDR block. The lines can be used by global domain names on Apasara Stack, private domain names of VPCs, and GTM instances to implement line-based intelligent resolution. |

| Global recursive resolution service | Recursive resolution service configuration | The recursive resolution service can be enabled and disabled on demand. You can enable this service to resolve public domain names for servers and terminals deployed in VPCs or classic networks. This allows these servers or terminals to access the Internet. |
|---|---|---|
| Cache | Support for cache management | Supports cache management. |
| Support for the xfer protocol | Resolve the original primary domain name of a website. | Forwarding mode: has high requirements on network connectivity. |
| Multi-IDC Deployment | Three-zone disaster recovery is supported. | Support physical machine-based deployment. |
