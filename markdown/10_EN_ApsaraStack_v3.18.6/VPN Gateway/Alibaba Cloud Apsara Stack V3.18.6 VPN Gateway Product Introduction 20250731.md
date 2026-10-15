---
title: "VPN Gateway Product Introduction 20250731"
product_version: "V3.18.6"
pdf_pages: 7
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 VPN Gateway Product Introduction 20250731.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/VPN%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20VPN%20Gateway%20Product%20Introduction%2020250731.pdf"
converter: line-classifier (PyMuPDF)
---

# VPN Gateway Product Introduction 20250731

y

## VPN Gateway

VPN Gateway is an Internet-based service that securely and reliably connects enterprise data centers, office networks, and Internet clients to virtual private clouds (VPCs) through encrypted tunnels.

### Features

VPN Gateway allows you to establish secure and reliable network connections between data centers, office networks, Internet clients, and virtual private clouds (VPCs) by using IPsec-VPN and SSL-VPN.

**IPsec-VPN**

IPsec-VPN is a route-based network connection technology that provides flexible traffic routing methods and allows you to configure and maintain VPN policies with ease. You can use IPsec-VPN to establish connections between data centers, office networks, and VPCs. You can also use IPsec-VPN to establish connections between VPCs in different regions.

**SSL-VPN**

SSL-VPN is a network connection technology based on OpenVPN. After you deploy the required resources, you need to only load an SSL client certificate to an Internet client and initiate a connection to a VPC.

### Benefits

VPN gateways are easy to configure and allow you to establish secure and stable connections in an efficient manner. Compared with Express Connect, VPN Gateway allows you to establish connections in a faster and more cost-effective manner.

**Security**

VPN Gateway uses the IPsec protocol or certificates in data transmission to ensure data security.

**Stability**

VPN Gateway adopts the hot-standby architecture to implement failover within a few seconds, session persistence, and zero service downtime.

**Ease-of-use**

A VPN gateway is ready-to-use and its configurations immediately take effect. You can deploy VPN gateways in a fast manner.

**Cost-effectiveness**

The encrypted and Internet-based connections provided by VPN Gateway are more costeffective than Express Connect circuits.

### Scenarios

You can use VPN Gateway to build hybrid cloud networks, connect cloud resources, and enable telecommuting.

**Build a hybrid cloud network**

| Feature |  | Description |
|---|---|---|
| IPsec-VPN configuration | Manage IPsec-VPN connections | Modify IPsec-VPN connections. |
|  |  | Create IPsec-VPN connections. |
|  |  | Delete IPsec-VPN connections. |
| SSL-VPN configuration | Manage SSL clients | Download SSL client certificates. |
|  |  | Create SSL client certificates. |
|  |  | Delete SSL client certificates. |
|  | Manage SSL servers | Modify SSL servers. |
|  |  | Create SSL servers. |
|  |  | Delete SSL servers. |
|  | Create VPN gateways | Modify VPN gateways. |
|  |  | Create VPN gateways. |
|  |  | View VPN gateways. |

y You can use IPsec-VPN to establish encrypted connections between data centers and virtual private clouds (VPCs) to build a hybrid cloud network.

**Connect cloud resources**

You can use IPsec-VPN to establish encrypted connections between VPCs are that deployed in the same region or different regions. This enables the resources in different VPCs to communicate with each other.

**Enable telecommuting**

You can use SSL-VPN to connect Internet clients to VPCs through encrypted channels. This way, the clients can connect to VPCs in a secure manner anytime. This is an ideal feature for telecommuting scenarios.

### Features

| Instance management |  |  |
|---|---|---|
|  | Customer gateway | Modify customer gateways. |
|  |  | Create customer gateways. |
|  |  | Delete customer gateways. |
|  |  | View customer gateways. |
| O&M capabilities | Monitoring capabilities | Support for IPsec-VPN monitoring. |
|  |  | Support for SSL-VPN monitoring. |
|  |  | Support for VPN Gateway monitoring. |
| Multi-data center deployment | Multi-Region | VPN supports multiple regions. |
|  | Zone-disaster recovery support | VPN Gateway supports zone-disaster recovery. |
| Encryption algorithm | Encryption algorithm | aes, aes192, aes256, eds, 3des. |
|  | Authentication algorithm | sha1, MD5. |
