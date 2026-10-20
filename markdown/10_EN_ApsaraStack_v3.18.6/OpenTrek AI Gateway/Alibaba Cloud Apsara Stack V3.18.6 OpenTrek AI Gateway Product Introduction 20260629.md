---
title: "OpenTrek AI Gateway Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 23
source_pdf: "a9ad6be615fc34ff_Alibaba Cloud Apsara Stack V3.18.6 OpenTrek AI Gateway Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/AI%20%E7%BD%91%E5%85%B3/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20OpenTrek%20AI%20Gateway%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# OpenTrek AI Gateway Product Introduction 20260629

## Table of Contents

- 1 What is AI Gateway
- 2 Product details
- 3 Product value
- 4 Features
- 5 Use cases
- 6 Usage limits
- 7 Key concepts

## 1 What is AI Gateway

An AI Gateway is a core tool that connects AI applications to large language model (LLM) services. It addresses key challenges in model integration, management, security, and stability. As enterprises adopt large models, they encounter challenges with traditional service invocation methods. These challenges include incompatible APIs from multiple vendors, complex resource management, data breach risks, and poor service stability. An AI Gateway provides a standardized entry point with unified administration capabilities, enabling efficient and secure service invocation for large models. Its core features include the following: Unified invocation method: Integrates commercial models, such as those from Alibaba Cloud Model Studio and OpenAI, with self-built models, such as Llama3.x. The gateway is compatible with the OpenAI API standard and uses policies to switch between model services flexibly. These policies allocate requests based on the model name or a specified ratio. AI invocation observability: Monitors key metrics in real time, such as queries per second (QPS), token consumption, and response time. It uses logging and tracing features to provide greater transparency into service calls. Security protection: Ensures data compliance and protects sensitive information through features such as API key rotation, consumer authentication (JWT/API Key), and Content Moderation. Intelligent administration: Includes built-in mechanisms for rate limiting, caching, and multi-level service degradation (fallback). These features optimize resource allocation and improve the success rate of service calls.

## 2 Product details

This topic describes AI Gateway, the challenges that enterprises face in AI scenarios, and the core capabilities of AI Gateway.

**Product overview**

Artificial intelligence (AI) plays an essential role in modern business innovation. The rise of large language models (LLMs) has expanded the use of AI. A variety of commercial and selfbuilt models are driving business growth in different fields. However, enterprises face challenges in AI adoption, including integration, stability, security, and management complexity. To address these challenges, AI Gateway acts as a bridge between enterprise AI applications and LLM services. It significantly improves integration efficiency and the governance of model services.

**Challenges in enterprise AI scenarios**

Large language models are widely used in enterprise AI scenarios. The three typical calling scenarios are as follows:
1. **Developers directly use LLM services:** Developers connect directly to LLM APIs from
different providers to meet business requirements.
2. **AI applications call LLM services:** Internal enterprise AI applications call LLM services to
handle complex tasks.
3. **AI applications call regular applications (as tools):** AI applications call the API
operations of regular applications to extend their features. In practice, enterprises often need to choose and switch between multiple models. If a model needs to be replaced due to poor stability or performance, enterprises want to switch to another model quickly. They also want to perform grayscale testing on new models to evaluate their effectiveness. Unlike personal applications, enterprises face the following four major challenges when they adopt AI technology:
1. **High cost of integration and switching between different LLM services**: Different
model providers have different standards and access methods for their LLM API operations. This makes it difficult for applications to switch smoothly between providers or use models from different providers simultaneously.
2. **Difficulty in managing internal users of LLM services** : LLM API operations are a
shared and scarce resource within an enterprise. Misuse by some callers can lead to issues such as rate limiting. Different models also have significant cost differences. Enterprises need to ensure that high-cost models are used for high-value business scenarios. However, achieving fine-grained permission management and resource control for users is difficult. It is also hard to apply different models and policies for different business scenarios.
3. **High data security and compliance risks** : LLM services are typically offered as Software
as a Service (SaaS) due to hardware and other limitations. When an enterprise calls an LLM service API operation, its internal data is at risk of being exposed. In addition, data compliance is a critical issue when calling LLM services, especially open source or external ones.
4. **Poor stability of LLM services**: LLM services are limited by hardware. Their API operation
rate limiting thresholds are low, and their stability is lower than that of general API services. The response time (RT) and success rate of the API operations are unstable, which affects the overall availability of AI applications.

**AI Gateway scenario example**

An enterprise plans to build AI applications to improve business efficiency and explore new opportunities. The enterprise purchases LLM services such as Alibaba Cloud Model Studio and Azure OpenAI. It also deploys a self-built open source model (llama3.x) on FC. To allow various internal AI applications to use these LLM services efficiently and securely, the enterprise configures AI Gateway. It integrates administration capabilities into the gateway to provide a unified access point for all AI applications. The following figure shows this process. The gateway administrator assigns a consumer identity to each AI application, which is authenticated by an API key. When an application sends a request to AI Gateway, the gateway automatically routes the request to the model services of Model Studio and Azure based on the `model` parameter. If a model service is unavailable due to rate limiting or other reasons, the gateway automatically falls back to the self-built open source model. To ensure data security and compliance, all AI requests must pass a Content Moderation review. The gateway intercepts non-compliant requests. The administrator enables rate limiting and caching to prevent any single application from overwhelming the model services with too many requests. The administrator also continuously monitors the AI API dashboard to view model call status and make adjustments.

**Core capabilities of AI Gateway**

AI Gateway provides a complete solution to expose and manage AI applications as APIs. This means:
1. All calls to LLM services pass through AI Gateway. This resolves issues related to model
stability, authorization, security, compliance, observability, and administration at the gateway layer.
2. All API calls exposed by AI applications pass through AI Gateway. This addresses
requirements for protocol access, authentication, authorization, rate limiting, and degradation at the gateway layer. To address these challenges, AI Gateway provides the following core capabilities:

**Unified calling method**

AI Gateway can quickly integrate various types of LLM services, including commercial and self-built ones. It exposes a unified API that is compatible with OpenAI. AI Gateway supports more than a dozen domestic and international LLM providers, including Model Studio and OpenAI, along with self-built LLM services such as ollama. AI Gateway provides the AIAPI type, which is an API optimized for AI scenarios. AIAPI offers three ways to integrate LLM services: Single model service: You can specify a single LLM service. This supports pass-through model names, or you can specify a model name. When a model name is specified, the model name passed in the user request is ignored. Multiple model services (by model name): You can specify one or more LLM services and configure model name matching rules for each. For example, you can configure a rule to call the OpenAI LLM service if the model name matches the `gpt-*` pattern, and call the Model Studio LLM service if the model name matches the `qwen-*` pattern. Multiple model services (by proportion): You can specify one or more LLM services and set a model name and request percentage for each. This pattern is ideal for grayscale testing of new models.

**Observability for AI calls**

AI Gateway integrates observability features for AI calls, including Metrics, Logging, and Tracing. Unlike general API observability, AI observability supports statistics for AI calls based on a token dimension. It supports observability dimensions such as API, model, and consumer. Logs of AI requests and responses are also recorded for subsequent tracking and auditing. The key metrics for AI observability are as follows: Queries Per Second (QPS): The number of AI requests and responses per second. This is broken down into QPS for AI requests, QPS for streaming responses, and QPS for nonstreaming responses. Request success rate: The success rate of AI requests. Statistics can be collected per second, every 15 seconds, or per minute. Token consumption/s: The number of tokens consumed per second. This is broken down into input tokens, output tokens, and total tokens. Average request response time (RT): The average response time (in ms) of AI requests over a specified period, such as a second, 15 seconds, or a minute. This is broken down into non-streaming RT, streaming RT (the total time for a streaming response), and streaming first-packet RT (the time to the first packet of a streaming response). Cache hits: Statistics on the number of cache hits and misses over a specified period. Rate limiting statistics: Statistics on the number of rate-limited requests and normal requests over a specified period. Token statistics by model: Statistics on token consumption for different models over a specified period. Token statistics by consumer: Statistics on token consumption for different consumers over a specified period. Threat statistics: Statistics on threats detected by Content Moderation, categorized by dimensions such as threat type and consumer.

**Built-in security protection**

AI Gateway provides three core security capabilities: Unified management and rotation of API keys: Store the API keys for LLM services at the gateway layer to shield them from callers. You can also configure multiple API keys for automatic rotation. Unified authorization: Use the built-in consumer authorization feature to grant separate permissions to different callers. It supports authorization methods such as JWT and API keys. You can also observe call status and configure rate limiting by consumer. Content moderation: Deep integration with Alibaba Cloud Content Moderation lets you review and protect the content of AI requests and responses. You can configure review policies and sensitive words as needed. This helps ensure the compliance of request content and prevents the leakage of sensitive enterprise information.

**Governance and acceleration for AI calls**

AI Gateway provides a unified administration center for enterprise AI applications. It uses features such as rate limiting, caching, and fallback to effectively improve the success rate of model calls. These features include the following: Token-based rate limiting: AI Gateway has a built-in token rate limiting policy. This policy can limit the number of tokens consumed per unit of time based on request features, such as headers. Automatic rotation of multiple API keys: AI Gateway supports configuring multiple API keys for a model service. When processing AI requests, the keys are automatically rotated to prevent an issue with one key from affecting all requests. AI cache: AI Gateway integrates an AI cache policy. This policy can cache responses to recurring requests to improve response efficiency and reduce LLM service costs. Model service fallback: AI Gateway supports falling back to a backup model when a model service is unavailable. It also supports multi-level fallback, which can effectively improve the success rate of AI requests. In summary, AI Gateway is a key tool for enterprises to improve the efficiency of their AI applications. By simplifying integration, unifying administration, strengthening security, and accelerating responses, AI Gateway helps enterprises make their AI innovation process more efficient, secure, and controllable.

## 3 Product value

AI Gateway provides stability, extensibility, and ease of use for AI services. It features a highconcurrency architecture, zero-downtime configuration updates that take effect in milliseconds, and a comprehensive ecosystem of Wasm hot plugins. The gateway also supports the Server-Sent Events (SSE) streaming protocol and resource optimization.

**Enterprise-grade reliability**

**A solid foundation for high-concurrency scenarios**

AI Gateway is built on Alibaba's years of experience in gateway technology. Its highconcurrency architecture can handle hundreds of thousands of requests per second. This provides the stability required for large-scale distributed systems and AI services.

**Intelligent, zero-downtime configuration updates**

Completely solve the traffic jitter problem caused by traditional Nginx Reload. The configuration change takes effect in milliseconds and has no business awareness. It is specially optimized for long-connection scenarios (such as AI services) to ensure service continuity.

**Flexible extensibility**

**A comprehensive plugin ecosystem for all scenarios**

The official plugin library includes core features for AI inference, traffic management, and security protection. It meets the needs of more than 90% of business scenarios, allowing you to respond quickly to complex business challenges.

**Innovative Wasm hot plugin architecture**

Plugins are isolated in a Wasm sandbox. This supports development in multiple languages, such as Rust, Go, and Python. You can upgrade plugin versions independently. This enables hitless hot updates for gateway logic and reduces maintenance complexity.

**Out-of-the-box security and usability**

**Standardized console and GUI-based configuration**

Provides the product standard console, which supports one-click activation of functions such as white screen operation and content security protection to reduce the O & M threshold.

**Simplified deployment and automation capabilities**

It is compatible with Ingress and Gateway API standards, integrates with Let's Encrypt to automatically issue and renew free certificates, and does not require a K8s environment. It can be quickly deployed with a single Docker command, offering an industry-leading developer experience.

**Efficient stream processing engine**

**End-to-end streaming protocol support**

Native support for streaming protocols such as SSE(Server-Sent Events) allows the WASM plug-in to customize the logic for processing streaming packets and flexibly adapt to scenarios such as AI streaming inference and real-time data push.
**Resource Optimization and Performance Breakthrough** In high-bandwidth and high-
throughput scenarios, such as AI model services, stream processing significantly reduces memory usage, improves resource utilization, and lower infrastructure costs.

## 4 Features

This topic describes the features of AI Gateway. AI Gateway connects enterprise AI applications with large language model services, providing the following features:

**Instance management**

| Feature | Description |
|---|---|
| Instance lifecycle management | Manage the complete lifecycle of AI Gateway instances, including creation, startup, shutdown, deletion, upgrades, and scaling. |
| Auto scaling | Automatically scales gateway instances based on business workloads to handle traffic peaks and troughs. |
| Instance engine parameters | Supports configuring engine parameters for an instance. |

**Model API management**

| Feature | Description |
|---|---|
| Multi-scenario AI capability access | Supports mainstream AI tasks such as text generation, image generation, video generation, speech synthesis, embedding, and rerank. It provides standardized API wrappers that unify heterogeneous model services. |
| Multi-protocol compatibility | Provides built-in support for mainstream protocols, including OpenAI, Anthropic, Model Studio, Doubao, ComfyUI, and vLLM. You can also customize HTTP/WebSocket protocols to seamlessly integrate with various large language models and AI services. |
| Intelligent model routing | Dynamically routes traffic to multiple backend model services based on the model name in the request (using glob pattern matching) or a preset weight ratio. This supports canary releases, A/B testing, and load balancing. |
| Consumer authentication and authorization | Performs authentication and access control for callers based on API keys. Only authorized consumers can access model APIs, ensuring secure service isolation. |
| Online debugging and usage guide | Provides a visual debugging panel that supports streaming output, parameter adjustments, and context memory. It also automatically generates sample code for API calls, simplifying developer onboarding. |

| Policy configuration | Header modification policy: Dynamically adds, overwrites, or removes HTTP headers before forwarding a request to the backend or returning a response to the client. This supports identity propagation, protocol adaptation, and security hardening for non-intrusive traffic governance. Timeout policy: Configures a maximum response wait time for model APIs. If a timeout occurs, the system automatically returns a 504 error, preventing slow backend calls from causing cascading failures and ensuring service-level agreement (SLA) stability. AI token rate limiting policy: Limits the total token consumption of API calls based on a preset token quota (such as daily, hourly, or per minute). This ensures fair resource allocation and prevents resource abuse. API RPS rate limiting policy: Restricts the maximum number of requests per unit of time (second, minute, hour, or day) to prevent high-frequency calls from overwhelming the API and protect backend large language model services. AI content moderation policy: Performs real-time content moderation on both user input and model output. It supports multi-level risk interception and detection in streaming responses to ensure AI services meet compliance and security requirements. |
|---|---|

**Route management**

| Feature | Description |
|---|---|
| Create LLM API and add endpoints | Create an LLM API associated with one or more large language model services. It is compatible with the OpenAI protocol and includes three default routes: a text completion endpoint, a conversational AI endpoint, and an embedding endpoint. |
| Pre-built policies and plugins | Includes four pre-built plugins: content moderation, rate limiting, caching, and web search. Note You must configure the input parameters for these plugins before use. |
| Consumer authentication | Supports authentication using an API key to verify the identity and permissions of API consumers. |
| API debugging | Provides usage examples to simplify the debugging and testing of API services. |
| Route list | Allows you to view the list of routes configured for the current API. |

| Policy configuration | Header modification policy: Dynamically adds, overwrites, or removes HTTP headers before forwarding a request to the backend or returning a response to the client. This supports identity propagation, protocol adaptation, and security hardening for non-intrusive traffic governance. Timeout policy: Configures a maximum response wait time for a route request. If a timeout occurs, the system automatically returns a 504 error, preventing slow backend calls from causing system-wide failures and ensuring service SLA and stability. Rewrite policy: Dynamically modifies the path and host of the original request before it is forwarded to a backend service. It supports exact or prefix-level path rewriting to meet complex architectural needs such as multi-environment routing, version migration, and microservice adaptation, ensuring traffic is accurately delivered to the target service endpoint. Fallback policy: Automatically switches requests to a predefined lightweight fallback service when a backend large language model service times out or returns a specified error code (such as 5xx or 4xx). This ensures basic system availability and prevents a single point of failure from causing a complete service outage. |
|---|---|

**MCP service management**

| Feature | Description |
|---|---|
| Tool management | Provides toolchain management for MCP services, including configuration tools, monitoring tools, and debugging tools, to support end-to-end service lifecycle management. |
| OpenAPI to MCP conversion | Automatically converts standard OpenAPI definitions into the MCP service specification, enabling rapid migration and adaptation of API definitions, authentication, and routing rules. |
| DB to MCP conversion | Provides automated migration from databases, such as MySQL and PostgreSQL, to MCP services, including data model conversion, SQL logic adaptation, and performance optimization. |
| Direct MCP routing | Implements direct routing based on the MCP protocol, optimizing request routing across data centers and cloud environments to reduce intermediate-layer forwarding latency. |

| Policy configuration | Header modification policy: Dynamically adds, overwrites, or removes HTTP headers before forwarding a request to the backend or returning a response to the client. This supports identity propagation, protocol adaptation, and security hardening for non-intrusive traffic governance. Timeout policy: Configures a maximum response wait time for an MCP request. If a timeout occurs, the system automatically returns a 504 error, preventing slow backend calls from causing system-wide failures and ensuring service SLA and stability. Rewrite policy: Dynamically modifies the path and host of the original request before it is forwarded to a backend service. It supports exact or prefix-level path rewriting to meet complex architectural needs such as multi-environment routing, version migration, and microservice adaptation, ensuring traffic is accurately delivered to the target service endpoint. |
|---|---|

**Service and source management**

| Feature | Description |
|---|---|
| Service management | Supports creating, viewing, editing, and deleting services. |
| Sources | Supports various source types, including AI services, DNS domains, fixed addresses, and Kubernetes (K8s) services. |

**Domain management**

| Feature | Description |
|---|---|
| Domain operations | Allows you to add or remove custom domains for the API gateway, enabling API access through your domain. |

**Certificate management**

| Feature | Description |
|---|---|
| Certificate operations | Allows you to update the SSL/TLS certificate or protocol configurations for a domain to ensure secure communication. You can configure encryption algorithms and cipher suites used for HTTPS transport to enhance security. |

**Consumer management**

| Feature | Description |
|---|---|
| Consumer lifecycle | Supports registering, deactivating, and deleting API callers or users, and assigning access permissions to them. |
| Consumer authorization | Supports assigning access permissions to consumers for Model APIs, MCP services, and routes. You can control which Model APIs, MCP services, and routes a consumer can call. |

**Multi-model support**

| Feature | Description |
|---|---|
| Multi-model support | Provides unified access and policy adaptation for mainstream AI models, such as large language models and image generation models. It enables model-level resource scheduling, access control, and performance monitoring. |

**API debugging**

| Feature | Description |
|---|---|
| API debugging | Provides an online API testing feature to validate API availability and correctness, streamlining the development and debugging process. |

**Plugin management**

| Feature | Description |   |   |
|---|---|---|---|
| Multi-level plugin scope | Configure plugins on various domain objects—such as instances, routes, services, domains, or MCP Servers—or combinations of these. This provides precise, multi-level control for complex governance needs. |   |   |
| Combined plugin binding | Allows the same plugin to be bound to multiple domain objects simultaneously (for example, a route and a consumer). The plugin is triggered only when a request matches all binding conditions, enabling high-precision policy enforcement. |   |   |
| Dedicated AI plugin ecosystem | Provides a set of plugins designed for large model scenarios, including ai-proxy (protocol proxy), ai-token-ratelimit (token rate limiting), ai-security-guard (content security), ai-rag (retrieval augmentation), and ai-prompt- decorator (prompt enhancement), which are deeply integrated with the AI application lifecycle. |   |   |
|   |   | ai-prompt- |   |

|   |   | ai-rag |
|---|---|---|
|   | decorator |   |

| Authentication and security plugins | Provides built-in authentication methods (such as key- auth , jwt-auth , oauth , and opa ) and security protection plugins (such as waf , ip-restriction , bot- detect , and cors ) to ensure trusted caller identities and enforce access compliance. |   |   |   |
|---|---|---|---|---|
| Traffic governance plugins | Supports plugins such as key-rate-limit , cluster-key- rate-limit , and traffic-tag to enable fine-grained traffic scheduling and resource isolation. |   |   |   |
|   |   | cluster-key- |   |   |
| Request/response transformation plugins | Use plugins such as transformer , custom-response , de- graphql , and ai-json-resp to dynamically modify request structures, protocol formats, or response content, enabling features like protocol conversion, field masking, and result standardization. |   |   |   |
|   |   |   | de- |   |
| Observability plugin | Integrates with the geo-ip plugin to enhance the observability of AI services. |   |   |   |
| Multiple instances of the same plugin type | Allows you to configure multiple plugins of the same type (for example, multiple rate limiting rules) on a single domain object, such as a route. The plugins are executed based on priority or a combination of conditions to meet the requirements of complex, layered business policies. |   |   |   |

|   | auth |
|---|---|

| bot- |   |
|---|---|

|   | detect |
|---|---|

|   | key-rate-limit |
|---|---|
| traffic-tag |   |

| plugins | rate-limit |
|---|---|

|   | transformer |
|---|---|
| ai-json-resp |   |

|   | graphql |
|---|---|

**Observability analysis**

| Feature | Description |
|---|---|
| Monitoring and metrics | Monitor real-time performance metrics, health status, and request volume for the API gateway. |
| Log management | Deliver access logs, error logs, and other information from the API gateway to a specified storage or analysis service. |
| API-level monitoring | View performance metrics and access statistics for specific REST APIs and their endpoints. |

## 5 Use cases

This article outlines the core use cases of the AI gateway.

**Unified access for large models**

For applications that use large language models (LLMs), the AI gateway serves as a unified proxy for mainstream and self-hosted large model services. It offers an OpenAI-compatible access method and provides governance capabilities like secondary API key issuance, rate limiting, security protection, and observability.
**High availability:** Maintains service continuity with features such as grayscale release for
multiple models, failover between models, token quota management, and traffic control.
**High security:** Provides content security detection for large models and supports route-
based and consumer authentication for fine-grained access control, security, and policy management for all API calls.
**Reduced model hallucination:** Reduces model hallucination with features like live web
search, automatic search result integration, and user intent recognition.
**Enterprise-grade observability:** Enables OpenTelemetry observability capabilities
across the application, gateway, and backend LLM services for end-to-end tracing. It uses a TraceId to correlate logs, request parameters, and other information across the entire request path.

**Unified management and access for MCP Server**

**Unified management and access for MCP Server:** The AI gateway provides proxying,
security authentication, and centralized governance capabilities for MCP Server, including unified observability and rate limiting.
**API-to-MCP:** Directly converts REST APIs into MCP Server instances, eliminating the need
to build and maintain them manually.
**Protocol offloading:** Reduces upgrade costs with seamless support for the latest official
MCP protocol. For example, it converts Server-Sent Events (SSE) to streaming HTTP responses, allowing stateless applications to process streams without implementing SSE handlers.
**MCP marketplace:** Provides an officially maintained MCP marketplace that ensures the
availability, ease of use, and security of MCP Server implementations.

## 6 Usage limits

AI Gateway has operational limits to ensure the stability and responsiveness of your gateway instance. Follow the recommendations in the table below.

| Item | Limit | Description |
|---|---|---|
| Number of routes/services | 5,000 | Exceeding this limit increases the latency of configuration updates from the control plane (xDS pushes). To prevent this, segment your services across multiple gateway instances or namespaces. |
| Concurrent connections per node | 50,000 (connection-level) | The Envoy core supports high concurrency. However, in AI scenarios, SSE streaming responses often maintain persistent connections. The actual limit depends on the node's memory. For example, a 4 GB node can typically handle around 5,000 active AI requests. |
| Request body size | 32 MB | The default is 4 MB but can be adjusted. Processing large request bodies consumes the gateway's buffer memory. In high-concurrency scenarios, monitor the gateway's memory usage closely to prevent OOM. |
| File transfer | Not recommended | The gateway is primarily designed for signaling traffic. For large files, such as images or audio/video segments, we recommend uploading them directly to OSS. The gateway should then only pass through the file URL or forward minimal metadata. |
| Request timeout | 300 seconds | We recommend increasing the timeout period for time- consuming tasks like large model inference, especially for reasoning-intensive models. To prevent a buildup of zombie connections, pair this with an effective idle connection cleanup policy. |

| Wasm plugin memory | 128 MB (per virtual machine) | Plugins such as AI Proxy run within a Wasm sandbox. Be mindful of this memory limit when processing large context or performing frequent regular expression filtering to avoid OOM. |
|---|---|---|
| Number of certificates | 1,000 | This is the recommended maximum number of certificates to mount on a single gateway instance via SNI. An excessive number of certificates reduces memory lookup efficiency during the TLS handshake. |

## 7 Key concepts

This document defines the core terms of AI Gateway to help you understand its design principles and operate it effectively.

**Gateway instance**

| A | gateway instance |
|---|---|
| K8s |   |

|   |   |   |   | private cloud |
|---|---|---|---|---|
| rmance | Envoy |   | core, it features a c |   |
| data plane |   |   | gateway instance |   |
|   |   | . A |   |   |

physical boundary for AI traffic ingress, protocol conversion, and security governance. Each instance has its own network egress, policy configurations, and resource quotas, making it the fundamental unit for multi-tenant isolation and granular service management.

**Route**

A `route` defines the mapping rules between request patterns and backend targets. The gateway forwards traffic by matching incoming requests against criteria such as `domain` `name` , path, HTTP method, headers, or specific AI model identifiers. The traffic is then directed to upstream services according to preset policies like weighted distribution or conditional filtering. For AI applications, a `route` also ensures reliable connections for streaming responses and long-lived protocols such as WebSocket Secure (WSS).

**Service**

A `service` is a logical abstraction of a backend business capability or model provider. It represents a group of workloads that can process requests, including containerized services within a `Kubernetes` cluster, traditional microservice instances, or even external

| service discovery |   | , the |
|---|---|---|
| d performs dynamic |   |   |

APIs from large model providers like `Qwen` and OpenAI. Using `service discovery` , the gateway monitors the health of these workloads in real time and performs dynamic `load`

```
balancing .
```

**Domain name**

A `domain name` is the public entry point for clients accessing AI services. Beyond traffic matching, it is a key component for `TLS offloading` and certificate management. Using Server Name Indication (SNI), a single `gateway instance` can securely host multiple domain names, enabling physical isolation of business entry points and brand customization.

**Plugin/policy**

A `plugin/policy` is a cross-cutting extensibility layer based on the `WebAssembly (Wasm)` architecture. The gateway uses plugins to implement advanced features like AI Proxy (protocol normalization), token-level `rate limiting` , content security auditing, and `authentication` . Plugins support dynamic hot-reloading, allowing for flexible expansion of the gateway's governance capabilities without interrupting business connections.

**Consumer**

A `consumer` represents the identity of an API caller. It represents an independent entity, such as an application, a third-party developer, or an internal department, for auditing and billing purposes. By enabling `authentication` on a `route` and associating it with `consumer` s, you can apply governance policies at the identity level instead of just the API level. This enables features like personalized quota management and usage tracking for different users.

**MCP**

In the context of AI, `MCP` (Model Context Protocol) is a standardized tool invocation protocol initiated by companies like Anthropic. It simplifies the integration between large language models (acting as agents) and external data sources or services, such as databases, email clients, or other APIs. Within the `Higress` architecture, `MCP` can also refer to Mesh Configuration Protocol. The McpBridge component uses this protocol to connect to various `service discovery` sources, such as `Nacos` or `K8s` , and synchronize service configurations across different environments.
