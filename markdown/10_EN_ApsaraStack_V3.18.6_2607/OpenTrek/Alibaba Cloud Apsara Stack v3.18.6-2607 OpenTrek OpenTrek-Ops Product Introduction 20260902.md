---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek-Ops Product Introduction 20260902"
product_version: "V3.18.6_2607"
doc_version: "20260902"
pdf_pages: 16
source_pdf: "9423369a148302fa_Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek-Ops  Product Introduction 20260902.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/OpenTrek/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20OpenTrek%20OpenTrek-Ops%20%20Product%20Introduction%2020260902.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek-Ops Product Introduction 20260902

## Table of Contents

- 1 Product Details
- 2 Benefits
- 3 Common scenarios
- 4 Functions and features
- 5 Terms

## 1 Product Details

The agent operations and maintenance platform (OpenTrek Agent Operations Platform, referred to as OpenTrek-Ops) is an enterprise-level multi-intelligent body operation and management platform based on the xClaw paradigm, providing a "cloud and Agent" integrated operation and maintenance product solution based on "hosted, observable, evolvable". Provide full life cycle management for AI intelligence, and provide "cloud + Agent" supervision and control integrated operation and maintenance for business, ensuring the safe, controllable and large-scale landing of enterprise AI productivity, and enabling enterprise intelligence to use the cloud.

## 2 Benefits

OpenTrek-Ops delivers a suite of key advantages, including out-of-the-box deployment, secure and controllable operations, full-stack observability, transparent costs, and projectbased management.

**Out-of-the-box deployment**

OpenTrek-Ops runs on the Apsara Stack Intelligent Computing foundation and supports oneclick provisioning for single agents and agent teams. It includes standard configurations for production environments and uses standardized templates to run agents and xClaw with production-grade elasticity. This eliminates manual setup of the underlying environment and enables business deployment within minutes. Native integration with AI observability, AI PaaS, and AI IaaS ensures stability and resource utilization in high-concurrency O&M scenarios.

**Secure and controllable operations**

OpenTrek-Ops establishes an end-to-end security audit system. It uses graphical security rule configuration and real-time interception of sensitive operations to ensure that all O&M operations are traceable and auditable, meeting the strict compliance requirements of the financial and government sectors. OpenTrek-Ops provides global security posture awareness and displays interception trends, risk level distributions, and rule hit rankings. Additionally, the integrated File Guard module enforces fine-grained control over agent file operations. At the architectural level, agents run in ACK secure sandbox containers. OpenTrek-Ops uses compute isolation technology to further strengthen operational security. This forms a defense-in-depth closed loop from policy configuration and real-time monitoring to underlying infrastructure isolation.

**Full-stack observability**

The monitoring system covers multiple dimensions, including business metrics, application performance, large model calls, tool calls, session messages, and security audits. It enables panoramic observability across the entire stack: business, agent or xClaw, agent infrastructure, cloud platform, and infrastructure. The system records both operational logs and conversation logs, enabling end-to-end dual-log tracing. It also integrates data insight capabilities (including agent analysis, project analysis, and intelligent metering analysis) and the UModel data pipeline, further enhancing multi-dimensional observability.

**Transparent costs**

OpenTrek-Ops builds an end-to-end transparent AI financial asset operation system. Powered by a precise metering engine, it displays token consumption and model usage distribution. You can perform deep drill-down analysis across four dimensions: model, project, agent, and user. This enables multi-level cost accounting from macro overviews to micro-level details, fully meeting the refined management requirements of project-based operations.

**Project-based management**

OpenTrek-Ops upgrades Agent Teams to Project Management. This feature allows you to centrally manage multi-agent collaborative projects tailored to specific business scenarios. Featuring both statistical and project card views, the platform supports project-level creation, orchestration, monitoring, and batch operations. This empowers enterprises to efficiently organize and manage AI agent resources by project.

**Efficient O&M**

OpenTrek-Ops delivers full lifecycle management for agents and supports one-click deployment and batch O&M for agents. Batch O&M includes batch starting, stopping, decommissioning, restarting, and scaling of agents, as well as batch synchronizing, disabling, and deleting of skills. Leveraging ACK secure sandbox containerization, OpenTrek-Ops ensures operational stability and resource utilization in high-concurrency scenarios. This significantly reduces infrastructure setup and maintenance costs, helping enterprises rapidly build production-grade agent clusters.

## 3 Common scenarios

OpenTrek-Ops is dedicated to the "Cloud + Agent" unified O&M scenarios for optimal AI utilization. It provides AI agents with full lifecycle management and business operations with integrated monitoring, management, and control, empowering enterprises to effectively manage and maintain their cloud-based agents.

**Lifecycle management for agents**

**Core capabilities**

The platform delivers management capabilities across the three agent states: creation, deployment, and runtime, achieving true application lifecycle management. Key features include one-click provisioning, batch O&M, and auto-scaling. The V1.1.1 release introduces support for pro-code agents (Hermes type), enabling source code publishing and secure agent execution within ACK sandboxes. Additionally, the upgraded Project Management module (formerly Agent Team) allows you to centrally manage multi-agent collaborative projects tailored to specific business scenarios.

**Scenarios**

Deploy and manage enterprise AI agents at scale. Create and operate multi-agent collaborative O&M teams (Agent Teams). Centrally host and govern agents in hybrid cloud environments. Develop, deploy, and manage pro-code agents from source. Orchestrate multi-agent collaboration for projects and perform end-to-end trace topology analysis.

**Customer benefits**

Centered on agents as the primary entry point, OpenTrek-Ops bridges agent O&M with cloud platform O&M to deliver full lifecycle management. This provides you with a low-cost, highly stable, and efficient AI agent O&M experience.

**Integrated cloud and agent O&M for business monitoring,**

**management, and control**

**Core capabilities**

From a business perspective, OpenTrek-Ops delivers integrated cloud and agent O&M for monitoring, management, and control across businesses, agent or xClaw, agent infrastructure, cloud platform resources, and hardware infrastructure. This ensures stable business operations. OpenTrek-Ops provides core capabilities such as panoramic observability, security auditing, and cost analysis. The V1.1.1 release adds data insights capabilities (including agent analysis, project analysis, and intelligent metering analysis), UModel data integration, Overview, and File Guard. These features further enhance integrated O&M capabilities.

**Scenarios**

Secure and controllable large-scale deployment of enterprise AI productivity Agent O&M and governance under strict compliance requirements, such as those in financial and government sectors Data-driven analysis of agent efficiency and operational optimization

**Customer benefits**

Centered on agents as the primary entry point, OpenTrek-Ops bridges agent O&M with cloud platform O&M for business monitoring, management, and control. This enables rapid fault discovery, precise isolation, and swift recovery, ensuring continuous and stable business operations.

## 4 Functions and features

OpenTrek-Ops includes six core modules: Operations Overview, Operation Center, Security Center, Operations Analysis, System Settings, and AI Assistant. These modules provide core product features such as agent lifecycle management, project management, capability and plugin management, infrastructure management, security settings and audit logs, cost analysis, and conversational AI O&M assistant.

**Operations overview**

| Feature | Description |
|---|---|
| Operations overview | This module displays core metrics such as the total number of agents, online agents, daily tasks, and task success rate to help you quickly understand the overall operational status of the agent platform. |
| AI assistant | The conversational AI O&M assistant supports natural language interactions to help users quickly complete O&M queries, fault diagnostics, and daily operations. It provides intelligent Q&A capabilities based on the platform knowledge base, helping O&M personnel quickly obtain operation guides and solutions. |

**AI assistant**

| Feature | Description |
|---|---|
| Conversational interactions | The conversational AI O&M assistant supports natural language interactions to help users quickly complete O&M queries, fault diagnostics, and daily operations. It provides intelligent Q&A capabilities based on the platform knowledge base, helping O&M personnel quickly obtain operation guides and solutions. |
| Scheduled tasks | Create and manage periodic inspections, automated analysis, and scheduled tasks, and view their execution history and running status. |
| Knowledge base | Create knowledge bases to maintain SOPs, manuals, cases, and product documents for agent retrieval. |

**Operation center**

**Agent list:**

| Feature | Description |
|---|---|

| Agent list | Display the running status and basic information of all agent instances, including xClaw, workflow, and pro-code types. Viewing all agents, agents created by you, and favorite agents. |
|---|---|
| Filter and search | Filter agents by conditions such as status, type, all creators, and all projects. |
| Agent management | Provide two core capabilities: agent discovery and agent hosting. Support xClaw, workflow, and pro-code agent types, and enable both automatic discovery and manual hosting of agents. Edit, update, restart, scale, start, stop, and delete agents. Add skills and channels to agents, and perform version rollbacks. |

**Project management:**

| Feature | Description |
|---|---|
| Project statistics | Display statistics such as the total number of projects, activated projects, projects with agents, and idle projects. |
| Project management | Create and edit projects, and bind agents to projects. Support batch O&M, agent O&M, skill O&M, and configuration updates for projects, and provide full lifecycle management including adding skills, plugins, and MCP services to projects. |

**Capabilities and plugins:**

| Feature | Description |
|---|---|
| Skill management | Centrally manage the creation, configuration, and O&M of agent skills. Enable and disable skills, and manage skill versions and rollbacks. |
| MCP management | Add, edit, start, stop, and manage MCP servers. Support manual configuration, JSON import, and AI gateway synchronization. |
| Plugin management | Support uploading plugins. After you upload a plugin, the system automatically parses and registers it. View plugin details and delete plugins. Update plugin versions and manageplugin statuses. |

**Change history:**

| Feature | Description |
|---|---|
| Change statistics | View the number of total, successful, failed, and running operations. |
| Operation records | Record the history of O&M operations such as agent configuration changes, skill updates, MCP management, and security policy adjustments. View operation details, target objects, start time, and end time. |

**Infrastructure:**

| Feature | Description |
|---|---|
| AI gateway | Import gateways. Synchronize, edit, delete, and view details of gateways. |
| Model service | Manage model services for agents, and integrate and configure multiple models such as Qwen3.5-plus. |
| Data storage | View detailed information about infrastructure instances. |
| Kubernetes cluster | Create self-managed Kubernetes clusters. Edit and delete clusters. |
| Agent platform | Manage agents from the Alibaba Cloud Model Studio low-code platform and the Dify platform. |

**Security center**

**Security settings:**

| Feature | Description |
|---|---|
| Security overview | The security overview dashboard displays the global security posture, risk statistics, and key security metrics. |
| Tool guard | Enable or disable the global tool guard feature, add custom security rules, and manage the activation status and details of these rules. |
| File guard | The new file guard capability performs security checks and applies access control to files that agents access to prevent sensitive file leakage. |

**Audit logs:**

| Feature | Description |
|---|---|
| Audit logs | Obtain the list of audit logs related to security rules, filter logs by the newly added All Projects scope, and view audit records across projects. |
| Log details | View audit log details. |

**Session analysis**

| Feature | Description |
|---|---|
| Filter | Filter sessions by session ID, agent, and time range. |
| Data statistics | Collect statistics on sessions within a specified time range and view trace aggregation analysis and session details. |

**UModel exploration**

| Feature | Description |
|---|---|
| Data statistics | This visual exploration tool supports model governance and data asset management scenarios. It uniformly presents model entities and their relationships in the system, allows you to view the details of each node. You can classify entities by type and domain. |
| Data display | Display data in graphic and table views. |

**Operations analysis**

**Cost analysis:**

| Feature | Description |
|---|---|
| Data statistics | The system calculates the total number of tokens, number of calls, token trends, and total token usage distributed by model within a specified time range. |
| Multi-dimensional analysis | View token consumption data across multiple dimensions, including model, project, agent, and user, to gain a comprehensive understanding of resource usage. |

**System settings**

| Feature | Description |
|---|---|
| Tenant management | Add and manage tenants. |
| Configuration management | Manage global platform configurations, supporting channel management, system configuration, and data subscription. |

## 5 Terms

| Concept | Description |
|---|---|
| Agent | An agent is an autonomous execution entity powered by large language models. The agent can understand natural language instructions, autonomously plan task steps, invoke external tools, and complete end-to- end business workflows. |
| Agent team | Deprecated since V1.1.1. We recommend that you use project-based management. An agent team was a collaborative working group that consisted of multiple agents, designed to facilitate division of labor, collaboration, and member management for complex tasks. |
| Model Context Protocol (MCP) | The MCP is an open protocol that enables standardized interactions between agents, external data sources, and tools. The MCP provides agents with a unified API for context access. |
| Skill | A skill is a predefined capability unit that an agent can invoke. It encapsulates specific operational logic and parameter specifications, enabling the agent to execute domain-specific tasks. |
| Agent infrastructure | Agent infrastructure is the underlying platform that supports the running, scheduling, and management of agents. It provides core capabilities such as model integration, tool registration, and session management. |
| Security settings | Security settings are a collection of security control rules governing agent execution. These settings include permission control, operation approval, and data access restrictions. Security settings ensure that agents execute tasks within the compliance scope. |
| Audit logs | Audit logs record all agent activities, including task execution, tool invocations, and data access. They are essential for security auditing, troubleshooting, and compliance tracking. |
| Cost analysis | Cost analysis provides token consumption statistics and model invocation analysis capabilities during agent execution. This feature helps administrators monitor resource utilization and optimize costs. |
| Pro-code agent | A pro-code agent is an advanced agent defined programmatically via the Agent Definition Language (ADL). It supports complex business logic orchestration and custom workflows, making it ideal for scenarios that require fine-grained control. |
| Project | A project is a business-oriented organizational unit designed to manage agents, allocate resources, and perform statistical analysis. It facilitates isolation and collaboration across multiple business lines. |

| Capabilities and plugins | Introduced in V1.1.1, this unified management concept integrates Skills and the Model Context Protocol (MCP) into a single interface. It provides a one- stop experience for capability registration, discovery, and invocation. |
|---|---|
| Agent Definition Language (ADL) memory | ADL memory is a memory persistence mechanism within the ADL. It enables agents to maintain context states across sessions, facilitating long-term memory and personalized interaction. |
| Security sandbox | A security sandbox is an isolated runtime environment for agents. It provides file protection and tool protection capabilities, ensuring that agents securely execute operations in a restricted environment and preventing unauthorized access. |
