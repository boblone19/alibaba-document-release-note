---
title: "VPN网关 产品简介"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 7
source_pdf: "01_产品简介_product-introduction-manual-refactoring.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/vpn/zh/product-introduction-manual-refactoring.pdf"
converter: line-classifier (PyMuPDF)
---

# VPN网关 产品简介

## VPN网关

VPN网关是一款基于互联网的网络连接服务，通过建立加密通道的方式实现企业本地数据中心、企业办公网络和互联网客户端与阿里云专有网络VPC（Virtual Private Cloud）之间安全可靠的私网互联。

### 产品详情

VPN网关通过IPsec-VPN和SSL-VPN两种方式在企业本地数据中心、企业办公网络、互联网客户端与阿里云专有网络VPC（Virtual Private Cloud）之间建立安全可靠的网络连接。

**IPsec-VPN**

IPsec-VPN是一种基于路由的网络连接技术，提供灵活的流量路由方式，便于配置和维护VPN策略。 IPsec-VPN支持在企业本地数据中心、企业办公网络与VPC之间建立网络连接，也支持在不同地域的VPC之间建立网络连接。

**SSL-VPN**

SSL-VPN是一种基于OpenVPN架构的网络连接技术。部署后，仅需要在互联网客户端中加载证书并发起连接，互联网客户端便可与VPC之间建立网络连接。

### 产品价值

VPN网关配置简单，可以快速建立安全、稳定的网络连接，相比于使用物理专线建立网络连接的方式，使用

**安全**

使用IPsec协议或者证书对传输数据进行加密，保证数据安全可信。

**稳定**

底层采用双机热备架构，故障时实现秒级切换，保证会话不中断，业务不受影响。

**简单**

开通即用，配置实时生效，实现快速部署。

**低成本**

基于互联网建立加密通道，相比使用物理专线成本更低。

### 应用场景

**构建混合云网络**

IPsec-VPN可以在企业本地数据中心和VPC之间建立加密通信通道，实现云下云上网络的连接，构建混合云网络。

**云上资源互通**

IPsec-VPN可以在同地域或者不同地域的VPC之间建立加密通信通道，实现相互隔离的VPC之间的资源互通。

**远程办公**

SSL-VPN可以在互联网客户端和云上VPC之间建立加密通信通道，互联网客户端通过互联网可以随时随地安全地连接VPC，满足远程办公的需要。

### 功能特性

| 功能 |  | 说明 |
|---|---|---|
| IPsec-VPN配置 | 管理IPSec连接 | 修改IPsec连接。 |
|  |  | 创建IPsec连接。 |
|  |  | 删除IPsec连接。 |
| SSL-VPN配置 | 管理SSL客户端 | 下载SSL客户端证书。 |
|  |  | 创建SSL客户端证书。 |
|  |  | 删除SSL客户端证书。 |
|  | 管理SSL服务端 | 修改SSL服务端。 |
|  |  | 创建SSL服务端。 |
|  |  | 删除SSL服务端。 |
| 实例管理 | 创建VPN网关 | 修改VPN网关。 |
|  |  | 创建VPN网关。 |
|  |  | 查看VPN网关。 |
|  | 用户网关 | 修改用户网关。 |
|  |  | 创建用户网关。 |
|  |  | 删除用户网关。 |
|  |  | 查看用户网关。 |

| 运维能力 | 监控能力 | 支持IPSEC-VPN监控。 |
|---|---|---|
|  |  | 支持SSL-VPN监控。 |
|  |  | 支持VPN网关监控。 |
| 多机房 | 多Region | VPN支持多Region。 |
|  | 支持同城容灾 | VPN网关支持同城容灾。 |
| 加密算法 | 加密算法 | aes、aes192、aes256、eds、3des。 |
|  | 认证算法 | sha1、MD5。 |
