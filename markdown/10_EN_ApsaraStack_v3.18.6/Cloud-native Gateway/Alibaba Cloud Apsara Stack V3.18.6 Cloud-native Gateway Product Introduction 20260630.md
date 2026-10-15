---
title: "Cloud-native Gateway Product Introduction 20260630"
product_version: "V3.18.6"
pdf_pages: 12
source_pdf: "580b084ad5fb777d_Alibaba Cloud Apsara Stack V3.18.6 Cloud-native Gateway Product Introduction 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E5%8E%9F%E7%94%9F%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud-native%20Gateway%20Product%20Introduction%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Cloud-native Gateway Product Introduction 20260630

## Table of Contents

- 1 What is AI Gateway
- 2 Product details
- 3 Product value
- 4 Features
- 5 Scenarios

## 1 What is AI Gateway

An AI Gateway is a core tool that connects AI applications to large language model (LLM) services. It addresses key challenges in model integration, management, security, and stability. As enterprises adopt large models, they encounter challenges with traditional service invocation methods. These challenges include incompatible APIs from multiple vendors, complex resource management, data breach risks, and poor service stability. An AI Gateway provides a standardized entry point with unified administration capabilities, enabling efficient and secure service invocation for large models. Its core features include the following: Unified invocation method: Integrates commercial models, such as those from Alibaba Cloud Model Studio and OpenAI, with self-built models, such as Llama3.x. The gateway is compatible with the OpenAI API standard and uses policies to switch between model services flexibly. These policies allocate requests based on the model name or a specified ratio. AI invocation observability: Monitors key metrics in real time, such as queries per second (QPS), token consumption, and response time. It uses logging and tracing features to provide greater transparency into service calls. Security protection: Ensures data compliance and protects sensitive information through features such as API key rotation, consumer authentication (JWT/API Key), and Content Moderation. Intelligent administration: Includes built-in mechanisms for rate limiting, caching, and multi-level service degradation (fallback). These features optimize resource allocation and improve the success rate of service calls.

## 2 Product details

Cloud Native Gateway is a high-performance, secure API gateway that acts as a traffic proxy for Kubernetes Ingress and the Gateway API. It provides service exposure, traffic management, application ingress, and integration. The gateway offers high performance, robust reliability, multi-layer security, and high scalability.

**Why choose Cloud Native Gateway**

| Feature | Description |
|---|---|
| Open-source enhancement | It is fully compatible with open-source community products and seamlessly integrates with Kubernetes. It offers enhanced capabilities in performance, observability, and ease of use. |
| Fully-managed service | This fully-managed service lets you focus on business development instead of cluster deployment and operations. This ensures a professional, elastic, and reliable service. |
| High availability | It solves common availability issues in open-source middleware by offering comprehensive monitoring and O&M for each instance. |
| Embrace cloud-native | Its containerized components include a Kubernetes Ingress Controller and are deeply integrated with Container Service. |
| Visualization | It provides a visual interface to view, manage, and control APIs. |

For more information, see Features and Product Value.

**Key concepts**

The core function of Cloud Native Gateway is to provide HTTP APIs.

**HTTP API**

HTTP APIs are interfaces centered around routes. They are ideal for scenarios like Kubernetes Ingress, microservice architectures, and AI (using Server-Sent Events), enabling you to quickly expose services to external traffic. In a Kubernetes cluster, an Ingress manages externally accessible resources for cluster Services and provides Layer 7 load balancing. The Cloud Native Gateway Ingress offers more powerful traffic management than a standard API gateway. It is compatible with Nginx Ingress and more than 50 Nginx Ingress annotations, covering over 90% of Nginx Ingress use cases. It supports canary releases for multiple service versions, flexible service governance, and comprehensive security, to meet the traffic management demands of large-scale, cloud-native distributed applications. If fine-grained API-level management is not required between business systems, you can configure a route to direct specific requests to a backend service. A route path is typically less granular than an API endpoint, such as /user/*. This allows you to quickly configure access paths and enable interaction between systems. HTTP APIs are designed for development and operations teams. They use routes to provide a flexible way to split business logic, orchestrate service interactions, and simplify the communication logic between different systems.

**Main features**

| Function module | Description |
|---|---|
| Instance management | Supports instance lifecycle management, engine parameter configuration, and auto scaling based on business load. |
| API management | Provides full lifecycle management for service interfaces, including creation, editing, maintenance, debugging, and decommissioning. |
| Service exposure | Supports route management, plugin management, and domain management. |
| Service invocation | Authentication and Authorization: Authenticates client identities and authorizes API access. Supports multiple client authentication methods, including Basic and JWT. API debugging: Supports online API testing. |
| Source management | Supports discovering and importing backend services from Nacos. |
| Plugin and policy management | Supports the configuration of various plugins and policies. |

## 3 Product value

Cloud Native Gateway seamlessly integrates with cloud products such as container services and microservices. It provides a secure and efficient, cloud-native traffic gateway that enables rapid external access to your cloud resources and accelerates your enterprise's digital transformation.

**Low cost**

Cloud Native Gateway consolidates the functions of a traffic gateway (such as `K8s Ingress`

|   | Nginx |
|---|---|
| gateway |   |

and `Nginx` ), a microservice gateway (such as `Spring Cloud Gateway` and `Zuul` `gateway` ), and a security gateway. This consolidation reduces resource overhead by 50%, shortens request time, and lowers O&M complexity.

**High integration**

Integrates seamlessly with container and microservice ecosystems to support service discovery methods such as `K8s` and `Nacos` . Integrates with logging and monitoring services. Simplifies certificate management by integrating with your existing certificate infrastructure.

**Boost productivity**

As a managed PaaS product, it provides a suite of productivity tools for every stage of the API lifecycle. These tools improve API management and O&M efficiency while lowering routine maintenance costs.

**High performance and high availability**

Distributed deployment enables large-scale access with low-latency processing. Evolved from an internal Alibaba product, the gateway is battle-tested at a massive scale. During the 2020 Double 11 event, it handled hundreds of thousands of requests per second. The gateway is now used by various Alibaba businesses, including Alipay, DingTalk, Taobao, Tmall, Youku, Fliggy, and Koubei.

## 4 Features

Cloud-native Gateway provides full lifecycle management for instances, smart routing, a plugin marketplace, and microservice integration. It includes built-in security plugins for JWT and APIKEY authentication. The gateway also uses IP address whitelists, request tracing, and HTTPS encryption to ensure high availability and security. This topic describes the features of Cloud-native Gateway.

**Instance management**

| Feature | Description |
|---|---|
| Instance lifecycle management | Full lifecycle management of gateway instances, including creation, startup, shutdown, deletion, and upgrades. |
| Instance engine parameters | Set parameters for the instance engine. |

**Routing management**

| Feature | Description |
|---|---|
| Routing management | Add and delete gateway routes. You can perform editing and debugging operations. |

**Consumer management**

| Feature | Description |
|---|---|
| Consumer lifecycle management | Create, edit, and delete consumers, and assign them access permissions. |
| Consumer authorization | Grant consumers authorization for specific routes. |

**Plugin management**

| Category | Description | Example plugins |
|---|---|---|
| Authentication | Identity authentication and authorization. | key-auth, jwt-auth, oidc |
| Security | Security protection and access control. | bot-detect, waf, cors |
| Traffic | Traffic management and control. | request-block, ip-restriction |

| Transformatio n | Request and response data processing. | transformer, custom-response |
|---|---|---|
| Observability | Monitoring and logs. | log-request-response |

**Domain name management**

| Feature | Description |
|---|---|
| Domain name operations | Add or delete custom domain names for the API gateway to enable API access through your domain. |
| Protocols and certificates | Update SSL/TLS certificates or protocol configurations for a domain name to ensure secure communication. Configure encryption algorithms and suites for HTTPS to optimize security. |

**Observation and analysis**

| Feature | Description |
|---|---|
| Monitoring and metrics | View real-time monitoring data for the API gateway, such as performance metrics, health status, and request volume. |
| Log management | Deliver API gateway logs, such as access logs and error logs, to specified storage or analysis services. |
| Tracing analysis | Enable distributed tracing to analyze the flow of requests throughout your system. |
| API-level monitoring | View performance metrics and access statistics for specific REST APIs and their operations. |

## 5 Scenarios

This topic describes the core application scenarios of the cloud-native gateway.

**AI scenarios**

**Large model service proxy**

Higress provides the `ai-proxy` plug-in for AI service proxying. It supports multiple large language model (LLM) providers, such as OpenAI, Azure OpenAI, Moonshot, and Qwen. Core features include protocol conversion, model mapping, and context management.

**AI load balancing**

The `ai-load-balancer` plug-in offers specialized load balancing policies for LLMs, including global least requests and prefix cache matching algorithms.

**Security protection scenarios**

**Identity authentication**

Multiple authentication plug-ins are available, such as `basic-auth` , `key-auth` , `jwt-` `auth` , and `oidc` , for identity verification in various scenarios.

**Traffic protection**

You can use plug-ins such as `request-block` , `key-rate-limit` , and `ip-restriction` to implement request blocking, rate limiting, and IP-based access control.

**Access control**

Plug-ins such as `bot-detect` , `waf` , and `cors` provide bot detection, Web Application Firewall (WAF), and cross-origin resource sharing (CORS) capabilities for enhanced security protection.

**Traffic management scenarios**

**Request transformation**

You can use plug-ins such as `transformer` , `custom-response` , and `geo-ip` to transform request and response data, generate custom responses, and handle geolocation information.

**Routing control**

Routing-related plug-ins such as `rewrite` and `header-control` support URL rewriting and request header manipulation.

**Release management scenarios**

**Frontend canary release**

The `frontend-gray` plug-in enables canary releases for frontend users. It supports business A/B testing and ensures release stability through canary matching, monitoring, and rollback policies. You can configure canary rules based on multiple dimensions, such as user ID and user tags.

**Observability scenarios**

**Monitoring integration**

You can integrate with Prometheus and Grafana to monitor gateway metrics and visualize them in dashboards.

**Statistics and tracing**

You can use statistics and tracing plug-ins to obtain comprehensive request monitoring and Tracing Analysis capabilities.
