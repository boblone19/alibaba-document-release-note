---
title: "OpenTrek AgentRuntime Product Introduction 20260629"
product_version: "V3.18.6"
pdf_pages: 16
source_pdf: "ca65dd93b14c62de_Alibaba Cloud Apsara Stack V3.18.6 OpenTrek AgentRuntime Product Introduction 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/Agent%20Runtime/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20OpenTrek%20AgentRuntime%20Product%20Introduction%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# OpenTrek AgentRuntime Product Introduction 20260629

## Table of Contents

- 1 What is AgentRuntime agent runtime service
- 2 Product details
- 3 Benefits
- 4 Functions and features
- 5 Common scenarios
- 6 Terms
- 7 Limits

untime service

## 1 What is AgentRuntime agent runtime service

**agent runtime service**

**AgentRuntime Platform** is a Platform-as-a-Service (PaaS) platform designed for enterprise-
grade AI Agent applications and deployed within the customer's private cloud environment. The platform focuses on solving core challenges across the entire lifecycle ofAgents in production environments, from code debugging, deployment to O&M. It provides unified

**Agent runtime management, tool (Tool/MCP) lifecycle management, fine-grained**

**elastic scheduling of underlying heterogeneous resources, and multi-level security**

**isolation**.
AgentRuntime supports runtimes for mainstream languages such as Python, Node.js, and Java. It provides standardized deployment, version management, canary release, and elastic instance scheduling for Agent applications. The platform includes two built-in sandbox services: Code Interpreter and Browser Use, supporting secure, isolated code execution (including file I/O and session management) and browser automation tasks (such as web browsing, data scraping, and form filling), respectively. The platform provides unified governance for tool invocation. It is compatible with the MCP protocol and supports one-click tool onboarding, custom publishing, and centralized credential management. The platform centrally manages access credentials for Agents, sandboxes, large models, and tools through security mechanisms. It can integrate with the enterprise credential center or AI Gateway. Observability covers tracing analysis and runtime metrics. You can visually monitor the duration and status of each step in Agent execution.

## 2 Product details

AgentRuntime agent runtime service is an all-in-one infrastructure platform for enterprisegrade Agent applications. The platform provides full lifecycle management capabilities, from debugging and deployment to monitoring and upgrades. It includes a unified execution environment that supports Python, Node.js, Java, and other language runtimes. It integrates secure sandboxing (Code Interpreter, Browser Use), model access and governance, tool invocation, credential management, and observability features. This topic describes the working principles and core features of AgentRuntime.

**Working principle**

AgentRuntime uses a layered architecture composed of the Agent runtime, Sandbox platform, Model Management Center, Tool Management Center, Credential Management Center, and Observability module.

**Core runtime layer**

The Agent runtime provides a standardized execution environment for various Agent applications. It supports both no-code and pro-code development modes. It also implements version management, canary release, and elastic instance scheduling.

**Secure execution layer**

The Sandbox platform provides an isolated execution environment based on the container service runD sandbox. Code Interpreter supports secure execution of Python/Node.js/Java code and file session management. Browser Use provides web automation capabilities based on VNC+Playwright.

**Model management layer**

The platform supports registration and management of model services through AI Gateway proxy.

**Tool management layer**

The Tool Management Center supports the MCP protocol, and enables the integration of preset tools and custom tools.

**Credential management layer**

The Credential Management Center centrally manages API key credentials and injects them securely at runtime.

**Observability layer**

The Observability module uses OpenTelemetry to provide end-to-end tracing from requests from entry points to models, tools, and external dependencies. Also, it supports real-time monitoring of Agent execution duration and status via Metrics.

**Deployment**

Each module exposes its capabilities through standard HTTP APIs (compatible with the OpenAI Chat Completions protocol) and multi-language SDKs (Python/Node.js). It supports integration with mainstream frameworks such as LangChain and AgentScope.

**Core features**

**Unified execution environment**: Provides Agent applications with a standardized, stable,
and efficient runtime environment. It aligns with public cloud functionality to ensure a consistent development and runtime experience.
**Full lifecycle management**: Supports the complete process management of Agent
applications, from debugging and deployment to monitoring and upgrades.
**Multi-language runtimes**: Includes built-in runtimes for Python 3.0+, Node.js, and Java,
and enables enterprises to build Agents using their existing technology stacks.
**Secure sandbox capabilities**: Provides two types of sandbox capabilities: Code
Interpreter (for code execution and session management) and Browser Use (for web browsing, data scraping, and form filling). Both are built on MicroVMs to deliver multi-level isolation.
**Model access**: Supports access to third-party models, open-source hosted models, and
vector models. It integrates AI Gateway to provide model proxy, load balancing, timeout control, content security, and token throttling.
**Tool management**: Supports the MCP protocol, and provides a tool marketplace, enabling
the integration of preset tools and publishing of custom tools.
**Credential management**: Centrally manages API key credential types required by
Agents, Sandboxes, LLMs, and tool invocations.
**Observability capability**: Supports visualized Trace call chains and real-time Metrics
monitoring, displaying execution duration, status, and error information.
**Multi-mode development**: Supports two development methods: no-code (for business
users) and high-code (coding in Python/Node.js/Java). AgentRuntime provides a unified execution environment, full lifecycle management, multilanguage runtime, secure sandbox, model management, tool management, credential management, and observability capabilities, empowering enterprises to operate Agent applications based on their own technology stacks.

## 3 Benefits

AgentRuntime agent runtime service is an all-in-one infrastructure platform for enterprisegrade Agentic applications. It provides a unified execution environment, full lifecycle management, multi-language runtime support, security sandbox services, model management, tool ecosystem integration, centralized credential management, and observability capabilities. The platform supports both no-code and pro-code development modes, adapts to languages such as Python, Node.js, and Java, remains compatible with mainstream Agent frameworks, and integrates model and tool services through the AI Gateway. This topic introduces the core product benefits of AgentRuntime.

**Enterprise-grade capabilities with standardized delivery**

The platform inherits EDAS's technical practices in application hosting and governance, offering an application-centric management model. It supports auto scaling based on CPU/memory usage and business metrics, and includes built-in traffic governance for canary releases and traffic splitting. Developers focus on business concepts such as applications, versions, and configurations, without needing to operate underlying Kubernetes resources.

**Unified agent execution and lifecycle management**

The platform provides a standardized execution environment for all types of Agent applications, supporting the complete lifecycle management from debugging and deployment to monitoring and upgrades. It includes built-in runtimes for Python 3.0+, Node.js, and Java, aligning with existing enterprise technology stacks. The sandbox environment supports Code Interpreter and Browser Use, fulfilling requirements for code execution and web automation.

**On-demand auto scaling and multi-level security isolation**

The platform supports request-driven auto-scaling: Instances scale to zero when idle and start rapidly upon request arrival. It offers container-level, sandbox-level, request-level, and session-level isolation mechanisms. The credential management module centrally controls access credentials for Agents, sandboxes, large models, and external tools, supporting dynamic injection and one-click disabling. Security policies bind predefined levels to underlying resources and scheduling policies automatically.

**Integrated management of models and tools**

Through the enterprise AI Gateway, the platform integrates mainstream models such as Qwen and DeepSeek, supporting multi-model load balancing and failover, along with content moderation and token-based throttling. The tool management module supports the MCP protocol, providing standardized interfaces for tool definition, registration, and invocation. Third-party tools can be integrated via the AI Gateway, enabling unified access to both model services and tool capabilities.

**Production-ready observability and operability**

The platform supports trace-based visualization of Agent decision paths, displaying the full chain from frontend requests, gateways, Agents, models, to tool invocation. It provides metric-based monitoring of latency and status, allowing real-time tracking of execution status and response time for each step. The platform also offers version management, canary release, endpoint configuration, and auto-scaling policy settings, meeting enterprise requirementss for continuous evolution and stable operation.

## 4 Functions and features

AgentRuntime is an enterprise-grade AI Agent runtime platform. It provides a unified execution environment, full lifecycle management, multi-language runtime support, security sandboxes, elastic resource scheduling, multi-level isolation, observability, tool and model integration, and credential management.

**Runtime management**

| Feature | Description |
|---|---|
| Unified execution environment | The system provides a standardized execution environment, supporting the operation of various Agent applications. |
| Full lifecycle management | The system supports the debugging, deployment, monitoring, and upgrading of Agent applications. |
| Python/Node.js/Java runtime | The system supports Python, Node.js, and Java runtimes. |

**Sandbox capabilities**

| Feature | Description |
|---|---|
| Code Interpreter | The system provides a secure, isolated environment that supports the execution of dynamically generated code, file I/O, and session management. |
| Browser Use | The system supports automated browser tasks such as web browsing, data scraping, and form filling. |
| All-in-One sandbox | The system integrates capabilities such as code execution, browser interaction, and file system access into a single sandbox instance. |
| File system | The system provides an isolated, read/write virtual file system for the sandbox. It supports creating, reading, modifying, and deleting files. |
| Operation capability (Computer/Mobile Use) | The system supports simulating graphical user interface (GUI) operations on desktop or mobile devices. |

**Elastic scheduling**

| Feature | Description |
|---|---|
| Second-level cold start and on-demand scaling | The system supports scaling Agent instances down to zero. It starts an instance when a request arrives. |
| Sleep and resume (coming soon) | Before scaling down an instance, the system takes a snapshot of its runtime status (such as memory and session information) and persists it. The system loads the snapshot when resuming the instance. |
| Session affinity assurance | The system routes consecutive requests from the same user to the same Agent instance. |
| High-concurrency elastic scale-out | The system automatically increases the number of instances based on predefined policies. |
| Business-aware scheduling API | The system provides an API that allows business code to actively request or release computing resources. |

**Security isolation**

| Feature | Description |
|---|---|
| Multi-level security isolation | The system supports request-level, instance- level, and session-level isolation. |
| Multi-tenant isolation assurance | The system provides tenant isolation mechanisms from the network, computing, and storage dimensions. |
| Physical/cluster isolation | The system supports deploying Agents with different security levels or belonging to different business units in completely independent physical clusters to achieve the highest level of security isolation. |
| Node isolation | Through scheduling policies, the system confines high-risk Agents to a dedicated “sandbox node pool,” ensuring physical isolation from other regular workloads at the compute node level. |

| Kernel-level isolation (strong sandbox) (coming soon) | The platform seamlessly integrates strong security sandbox capabilities such as ACK's runD. For high-risk tasks like executing untrusted code, the system runs them within an independent kernel based on hardware virtualization. This effectively prevents container escape by malicious code and protects the host and other applications. |
|---|---|
| TLS 1.2+ transmission encryption | The system encrypts all network communications using TLS version 1.2 or higher. |
| Storage isolation and mount | The system supports securely mounting external storage (such as Object Storage Service or local disks) to the sandbox. |

**Observability**

| Feature | Description |
|---|---|
| End-to-end trace | The system traces calls from the frontend request, through the gateway and Agent, to the model, tools, and external dependencies. |
| AI application monitoring (requires integration with AI observability products) | The system supports monitoring via Prometheus or ARMS, analyzing model performance, token consumption, and GPU utilization. |
| Log and evaluation | The system centrally stores logs and supports retrieval and SQL analysis. It also evaluates model call logs for quality, security, and intent. |

**Tool and model management**

| Feature | Description |
|---|---|
| MCP | The system supports Model Context Protocol (MCP) mode. |
| Tool governance and version management | The system manages the lifecycle, version control, and permission governance of tools. |
| Integration with mainstream models | The system integrates mainstream large language models such as Qwen and DeepSeek. |

| Load balancing and degradation across multiple models | The integrated AI Gateway distributes requests across multiple model instances. The system fails over to a backup model if the primary model fails. |
|---|---|
| Content security and token throttling | The integrated AI Gateway audits the input and output of models for content security. The system limits token consumption according to defined policies. |
| Unified tool definition and invocation | The system provides standardized protocols for defining, registering, versioning, and invoking tools. |

**Credential management**

| Feature | Description |
|---|---|
| Support multiple credential types | The system supports the API Key credential type. |
| Inject credentials dynamically | The system works with the AgentRuntime to inject credentials securely at runtime. |
| Enable or disable control | The system enables you to enable or disable credentials with one click. |

## 5 Common scenarios

AgentRuntime agent runtime service provides a unified execution environment, full lifecycle management, security sandbox, and multi-language runtime support to meet the foundational deployment and operations requirements of enterprise-grade Agent applications. This topic describes the scenarios for using AgentRuntime.

**Scenario 1: Full lifecycle management of enterprise AI**

**applications**

The AgentRuntime platform supports the complete lifecycle management of Agent applications, from debugging and deployment to monitoring and upgrades. Enterprises can develop Agent applications in languages such as Python, Node.js, and Java, and manage them centrally through the platform. The platform integrates observability capabilities, including tracing analysis, log correlation, and LLM call token consumption metrics. This scenario applies to internal enterprise AI application teams that require standardized deployment processes, simplified operational complexity, and improved development efficiency.

**Scenario 2: MCP tool hosting and runtime environment**

**optimization**

The AgentRuntime platform provides a standardized hosted runtime environment for MCP (Model Control Protocol) tools. In scenarios such as Alibaba Cloud Model Studio, traditional solutions deploy multiple MCPs on a single ECS virtual machine, leading to dependency conflicts, insufficient security isolation, lack of resource elasticity, and poor stability. The AgentRuntime platform resolves dependency issues through containerized deployment—each MCP is packaged as an independent container image containing all required environments and dependencies. It enhances security through multi-level isolation mechanisms (container and sandbox isolation). It achieves efficient resource utilization through on-demand auto scaling, allowing instances to scale down to zero when no requests exist. It ensures fault isolation so that a failure in one MCP does not affect other services. This scenario applies to enterprise platforms that need to host multiple third-party or open-source tools, especially those with high security and stability requirements.

**Scenario 3: Deployment of security-sensitive Agent**

**applications**

To mitigate security risks associated with executing untrusted code, AgentRuntime provides multi-dimensional security isolation mechanisms. The platform supports multiple modes, including physical or cluster isolation, node isolation, kernel-level isolation (strong sandbox, coming soon), and request- or session-level isolation. Administrators can predefine resources and policies corresponding to different security levels; developers simply select the appropriate security level to automatically apply the respective isolation measures. The platform integrates strong security sandbox capabilities such as ACK-provided runD (coming soon) to ensure high-risk tasks run in hardware-virtualized environments and prevent container escape. This scenario applies to industries with strict data security requirements, such as finance and government, where Agent applications must handle protected data or execute external code.

**Scenario 4: Automated tasks and data processing**

The AgentRuntime platform supports code execution and data processing capabilities. It provides a securely isolated Code Interpreter environment for executing dynamically generated code, supporting file I/O and session management. It also enables browser automation via VNC + Playwright to perform tasks such as web browsing, data scraping, and form filling. Additionally, it supports desktop application automation through GUI-based interaction with local applications. This scenario applies to enterprise applications requiring automated data collection, processing, and analysis, such as public opinion monitoring, market research, and business process automation.

**Scenario 5: Cross-departmental sharing of models and tools**

The AgentRuntime platform supports cross-departmental and cross-project sharing of models and tools. The credential management module centrally stores LLM access keys and tool API credentials, assigning usage permissions by project or role. The Tool Hub supports custom tool publishing and internal sharing, facilitating the accumulation of enterprise-grade capability assets. Multiple sandbox environments can be independently configured with dependencies and images to accommodate varying technology stacks across teams. The development mode supports a smooth transition from low-code rapid validation to pro-code engineering implementation. This scenario applies to large enterprise groups where headquarters centrally build Agent infrastructure, and subsidiaries or business units develop dedicated Agent applications on the same platform to achieve capability reuse and standardization.

## 6 Terms

This topic describes the basic concepts of AgentRuntime agent runtime service. AgentRuntime **platform** The PaaS platform deployed in an Apsara Stack environment provides unified runtime management for agents, full lifecycle management for tools, heterogeneous resource scheduling, and multi-level security isolation.

**Agent runtime**

The agent runtime provides a standardized containerized execution environment. It supports runtime environments such as Python, Node.js, and Java, and offers full lifecycle management capabilities.

**Security sandbox**

The security sandbox provides two types: Code Interpreter and Browser Use. It supports operations such as code execution, file I/O, and web automation, and features process-level and kernel-level isolation.

**Model management**

The system integrates mainstream models such as Qwen and DeepSeek. It provides capabilities such as load balancing across multiple models, degradation, and token throttling.

**Tool management**

The system provides standardized tool definition, registration, and calling protocols and supports the MCP protocol.

**Credential management**

The system centrally manages API key credentials required for accessing agents, sandboxes, and large models.

**Observability**

The system supports trace tracking for agent execution chains and metrics monitoring for duration and status at each step.

**Development mode**

The system supports both no-code and pro-code modes, and enables business personnel to build agents through a visual interface.

**Multi-tenant security isolation**

The system implements isolation at the request, instance, and session levels to ensure operational security in multi-tenant environments.

**Persistent storage**

The system supports mounting OSS and local disks to meet data persistence requirements during agent runtime.

**Unified API and SDK**

The system provides HTTP APIs compatible with the OpenAI Chat Completions protocol and SDKs for multiple programming languages.

## 7 Limits

Do not exceed the specified limits when you use AgentRuntime agent runtime service. Exceeding these limits may cause exceptions in your program.

| Category | Limitation description |
|---|---|
| Cluster | Deploy the management cluster and workload clusters separately (at least two Kubernetes clusters). Each cluster requires a minimum configuration of 16 cores and 32 GB of memory. The management console must be able to access the Kubernetes API Server of the workload clusters. The AI Gateway in the workload clusters must have an externally accessible IP address (via a LoadBalancer-type Service). In exclusive mode, a large number of concurrent sessions increases pressure on cluster resources. Plan your cluster capacity according to your business scale. |
| Sandbox | The first startup of a sandbox may take longer due to image pull and pod scheduling. We recommend that you perform image warm-up in advance. |
| Credential | User experience for certain operations may be affected in a self-signed certificate environment. |
| Storage | Prepare the OSS bucket and image repository in advance and ensure sufficient storage quota. OSS is optional, but you must configure it if you want to use zero- code agents, sandbox state persistence, or deployment acceleration features. |
