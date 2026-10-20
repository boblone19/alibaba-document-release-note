---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 14
source_pdf: "730a9e021c787afd_Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Product Introduction 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/API%20%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20API%20Gateway%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Product Introduction 20260828

## Table of Contents

- 1 API Gateway
  - 1.1 Product details
  - 1.2 Product value
  - 1.3 Features
  - 1.4 Scenarios
  - 1.5 Instance specifications
  - 1.6 Usage limits
  - 1.7 Key concepts

## 1 API Gateway

API Gateway is a core component of modern application architectures. It unifies the management of API and AI requests and coordinates interactions between systems. It builds a stable, highly extensible, enterprise-grade service platform by hosting standardized interfaces, integrating services, and exposing capabilities.

**Products and capabilities**

Alibaba Cloud API Gateway offers two products: Cloud-native API Gateway and AI Gateway. Cloud-native API Gateway is a high-performance, highly extensible gateway that deeply integrates API management, traffic shaping, and microservice administration. AI Gateway is designed for AI scenarios. It acts as a unified proxy for large model APIs and MCP Servers, and provides extensive integration and administration capabilities.

**Solutions and advantages**

**Built on open source, better than open source**

It uses Spring Cloud Gateway to build an access layer gateway and an API management platform. Based on extensive implementation experience, it significantly enhances the gateway's traffic management capabilities for complex production scenarios.

**High system architecture compatibility**

It connects to service registries, such as Nacos, Eureka, and K8s, in a microservices model to monitor backend services and enable fast publishing. It also transforms protocols, such as WebService, gRPC, and Dubbo. This unifies the management and publishing of services that use different protocols, providing a solution for system integration.

**Open ecosystem**

It provides an Open Platform that uses unified management and authorization to expose its capabilities to external partners. This helps you build ecosystems with your partners.

### 1.1 Product details

This topic describes the key features of API Gateway.

**Features**

| Feature module | Description | Related documents |
|---|---|---|
| Instance management | Lets you manage the instance lifecycle, configure engine parameters, and enable auto scaling for instances based on workload. | API Gateway User Guide > Instance management |
| Service exposure | Supports route grouping, route management, plugin management, and signature management. | API Gateway User Guide > Service exposure |

| Service invocation | Authentication and authorization: Provides client authentication and API authorization. Client authentication supports Basic, JSON Web Token (JWT), and other methods. API debugging: Supports online API testing. | API Gateway User Guide > Service invocation |
|---|---|---|
| Source management | Lets you discover and import backend services from sources such as Nacos, Eureka, a microservices namespace, and a database. | API Gateway User Guide > Source management |
| Policy management | Supports lifecycle management for various policies. | API Gateway User Guide > Policy management |
| Gateway cascading | Enables multiple gateways to work together. It connects routes and services across gateways, allowing users of one gateway to invoke services managed by another. | API Gateway User Guide > Gateway cascading |
| Observability and analysis | Supports gateway instance monitoring, log search, log delivery, distributed tracing, and API monitoring. | API Gateway User Guide > Gateway Logs |

### 1.2 Product value

API Gateway is a lightweight and easy-to-use service that delivers high performance, stability, and reliability. It provides open, cross-protocol interconnection and one-stop service management.

**High performance, stability, and reliability**

API Gateway is designed to reliably support large-scale requests. It is built on the same high availability (HA), high-performance, and distributed cluster technologies that are used within Alibaba.

**Lightweight and easy to use**

API Gateway enables the efficient digital delivery of business capabilities and supports rapid changes. You can publish APIs and change configurations with flexibility and ease. You can call APIs simply and conveniently. You can easily scale out processing capacity as needed.

**Open, cross-protocol interconnection**

API Gateway enables interoperability by simplifying application calls, connecting new and legacy systems, and facilitating communication between enterprise organizations. It securely interconnects services across different systems and protocols and integrates with existing enterprise systems and account systems. It transforms complex parameter structures and supports publishing and consuming service APIs for various common protocols.

**Microservice integration**

API Gateway integrates with various microservice backend applications, such as Spring Cloud, Dubbo, and HSF.

**One-stop service management**

API Gateway provides centralized control for exposing capabilities across platforms, systems, and organizations, which enables unified management, organization, and interaction. It provides complete API lifecycle management, a Service Catalog, service authorization, and user management. It supports role-based service publishers, consumers, and administrators, and provides flexible permission management.

**Highly adapted for AI scenarios**

AI Gateway features a high-concurrency architecture, millisecond-level zero-downtime configuration updates, WebAssembly (WASM) hot plugins, and a comprehensive plugin ecosystem. It supports the Server-Sent Events (SSE) streaming protocol and includes resource optimization features to ensure the stability, extensibility, and ease of use of AI services. Enterprise-grade reliability: Built on a solid foundation for high-concurrency scenarios, it enables zero-downtime intelligent configuration updates. Flexible extensibility: It offers a comprehensive plugin ecosystem with an innovative hot plugin architecture that uses a WASM sandbox. Out-of-the-box security and usability: A standardized console and GUI-based configuration provide a high degree of automation for simplified deployments. Efficient stream processing engine: It supports end-to-end streaming protocols to improve resource utilization, reduce infrastructure costs, and achieve performance breakthroughs. For more information, see **AI Gateway Product Introduction > Product Value**.

### 1.3 Features

This topic describes the features of API Gateway.

**Instance management**

| Feature | Description |
|---|---|
| Instance lifecycle management | Manages the full lifecycle of gateway instances, including creation, startup, shutdown, deletion, upgrades, and scaling. |
| Auto scaling | Automatically adjusts the number of gateway instances based on business workload to handle traffic fluctuations. |

**Source management**

| Feature | Description |
|---|---|
| Nacos | Lets you discover and import backend services from Nacos. |

| EDAS microservice namespace | Lets you discover and import backend services from an EDAS microservice namespace. |
|---|---|
| Eureka | Lets you discover and import backend services from Eureka. |
| Database | Lets you discover and import backend services from a database. |

**Service publishing**

| Feature | Description |
|---|---|
| Route group | Lets you logically group related routes to apply policies, distribute traffic, or implement complex routing scenarios such as a canary release. |
| Route management | Lets you add, modify, delete, publish, and unpublish gateway routes. |
| Plugin management | Supports a plugin marketplace and global plugins. |
| Signature management | Supports signature authentication using Hash-based Message Authentication Code (HMAC) algorithms, including SHA-1, SHA-256, and SM3. |

**Consumer management**

| Feature | Description |
|---|---|
| Consumer lifecycle | Lets you register, deactivate, and delete API consumers, and assign them access permissions. |
| Consumer authorization | Lets you assign API access permissions to consumers and control which APIs they can call. |

**API debugging**

| Feature | Description |
|---|---|
| API debugging | Provides an online testing tool to verify API availability and correctness, simplifying development and debugging. |

**Policy management**

| Feature | Description |
|---|---|
| Authentication policy | Includes authentication methods such as JSON Web Token (JWT), Basic, API key, and custom authentication to secure your applications. |
| Rate limiting policy | Limits the request rate to prevent traffic spikes from overwhelming your backend services, ensuring efficient and stable operation. |
| Timeout policy | Sets a maximum timeout for requests forwarded by the gateway. |
| Circuit breaker policy | Prevents calls to backend services at the gateway level to protect your applications from cascading failures. |
| Mock policy | Lets you define filtering rules and return mock responses during runtime. This helps you meet specific data parsing needs and simulate data objects that are difficult to construct or obtain. |
| Signature policy | Generates signatures for requests that pass through the gateway. |
| CORS policy | Lets documents or scripts from one domain request resources from another domain through the gateway. |
| Caching policy | Caches responses to avoid redundant requests to backend services for the same resource. |
| IP allowlist/blocklist policy | Restricts requests based on their source IP address to enhance the security of your backend services. |
| Request tracing policy | Adds a request tracing header to requests passing through the gateway to enable end-to-end request tracing. |
| ACL policy | Controls which authorized consumers can access a service. |

**Cascading management**

| Feature | Description |
|---|---|
| Cascading gateway | In complex, multi-environment scenarios, this feature automatically syncs services from a source gateway to a cascaded gateway. This makes the services accessible to consumers in other environments and automates cross-environment publishing. |

| Cascading link | In a cascading setup, you define the relationships between gateway instances and ensure network reachability. The platform then automatically synchronizes route information, credentials, signatures, and some governance policies. This allows consumers in other environments to call the services under a unified governance strategy. |
|---|---|

**Domain name management**

| Feature | Description |
|---|---|
| Domain operations | Lets you add or remove custom domain names for the API Gateway, enabling API access through these domains. |
| Protocols and certificates | Lets you update Secure Sockets Layer (SSL)/Transport Layer Security (TLS) certificates or protocol configurations for a domain to ensure secure communication. You can configure encryption algorithms and cipher suites for HTTPS transport to optimize security. |

**Observability and analysis**

| Feature | Description |
|---|---|
| Monitoring and metrics | Provides real-time visibility into monitoring data for the API Gateway, such as performance metrics, health status, and request volume. |
| Log management | Lets you deliver API Gateway logs, such as access logs and error logs, to specified storage or analytics services. |
| Distributed tracing | Lets you enable distributed tracing to analyze the entire flow of a request through your system. |
| API-level monitoring | Lets you view performance metrics and access statistics for specific REST APIs and their operations. |

### 1.4 Scenarios

This topic describes the core scenarios for API Gateway.

**Exposing services and managing traffic**

**Service exposure and traffic management:** The gateway is compatible with the K8s
Ingress standard. It supports multiple backend services, such as microservices and functions. It also supports multiple service discovery methods, such as K8s and Nacos. The gateway provides high integration, ease of use, simple extensibility, and hot updates. Traffic management for containers and microservices: The gateway acts as the access layer for container services. It is compatible with the K8s Ingress standard and provides finegrained routing and API management. It supports one-click import of K8s Services or Nacosregistered services. Requests connect directly to pod IPs. The gateway also supports core annotation extensions for Nginx Ingress and provides service administration capabilities, such as traffic throttling, prefetch, and grayscale releases. Multi-active disaster recovery: As a unified access layer for multiple clusters, the gateway enables features such as multi-active disaster recovery. It supports multiple service sources, such as ACK, MSE Nacos, FC, DNS domain names, and fixed IP addresses. The gateway enables precise routing based on ratios or request content and supports health checks and service fallback.

**API full lifecycle management**

**API full lifecycle management:** The gateway provides full lifecycle management for APIs,
including design, development, publishing, and unpublishing. It also supports multienvironment management. This helps teams manage and publish APIs more efficiently and securely, which promotes rapid business iteration and innovation. Standardized development and improved efficiency: With API full lifecycle management, developers can use the API-first pattern for parallel development between the frontend and backend. This enables rapid system iteration. Fine-grained API management: Fine-grained API management prevents uncontrolled exposure in scenarios such as opening APIs to partners or integrating internal and external systems for collaboration. Multi-environment management: Multi-environment management keeps development, testing, pre-production, and production environments separate. This prevents development and testing activities from affecting the production environment. It also simplifies testing and validation at different stages.

### 1.5 Instance specifications

This topic describes the instance specifications that API Gateway supports to help you select the appropriate one for your business.

**Specification types**

The API Gateway instance specification types are as follows:

| Specifications | Container CPU (cores) | Container memory (GB) | Container storage (GB) | TPS |
|---|---|---|---|---|
| mini | 1 | 2 | 100 | 1000 |
| small | 2 | 4 | 100 | 2000 |
| standard | 4 | 8 | 100 | 4000 |
| large | 8 | 16 | 100 | 8000 |

### 1.6 Usage limits

API Gateway enforces several usage limits to ensure stable operation. Exceeding these limits can cause system errors.

| Metric | Limit | Description |
|---|---|---|
| Number of APIs/routes | 10,000 | Exceeding this limit can cause forwarding errors and requires a capacity assessment. |
| Concurrency | 1,000 | Exceeding 1,000 concurrent requests on a single node requires an evaluation of your backend service's response time (RT) and request concurrency to prevent gateway OOM errors. |
| Request body size | 4 MB | You can adjust this limit, but exceeding it under high concurrency can cause gateway OOM errors. Always consider the gateway's capacity during configuration. |
| File transfer | Not recommended | File transfers, like large request bodies, are a primary cause of gateway OOM errors. We recommend using a dedicated file service and passing only the file URL through the gateway. |
| Timeout | 10 seconds | You can adjust the request timeout, but exceeding the default value increases the risk of gateway OOM errors. |

### 1.7 Key concepts

This topic defines the key terms in API Gateway.

**Gateway instance**

A gateway instance is a deployed unit of API Gateway that schedules and processes traffic. We recommend deploying one gateway instance per ACK cluster. You can also use a namespace to run multiple, isolated instances within the same cluster. Each instance consists of two main components: a data plane that directly handles business traffic and a control plane that manages the configuration.

**Route**

A route defines rules that map requests to services. Using request attributes such as the domain name, path, or header, the gateway routes traffic proportionally or conditionally to different backend services or even to different clusters.

**Service**

A service is a logical abstraction of a backend application. It represents a set of workloads that can process requests, such as a model-serving application, a REST API, or a database.

**Domain name**

A domain name is the public-facing entry point for clients to access backend services. It is also the starting point for the gateway's traffic matching and policy enforcement.

**Plugin/policy**

API Gateway provides a plugin marketplace with built-in extensions for features like authentication and authorization, traffic management, and security. These plugins let you flexibly extend the capabilities of your gateway.

**Consumer**

A consumer represents an entity that calls your APIs. In API Gateway, you use consumers to enable authentication for routes.
