---
title: "Apsara AIOps Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 11
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara AIOps Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%BB%B4%E5%B0%8F%E6%99%BA/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20AIOps%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara AIOps Product Introduction 20260701

Apsara AIOps Product Introductio

## Intelligent O&M Assistant

This chapter introduces the Intelligent O&M Assistant. The Intelligent O&M Assistant is the entry point for intelligent Operations and Maintenance (O&M) upgrades on the Apsara Stack platform. It provides platform O&M engineers with capabilities such as O&M Q&A, environment information queries, content matching and recommendation, predictive optimization suggestions, inference, analysis, summarization, and code and visualization generation. The assistant also serves as a foundation for customer-facing intelligent O&M. It provides out-of-the-box capabilities that integrate the platform's Toolbox, knowledge base, and MCP Server to facilitate the engineering and deployment of O&M agents on-premises. Apsara AIOps Product Introductio

## Product details

The Intelligent O&M Assistant consists of the Frontend and O&M LLM Management and system configuration.

**Frontend**

**Intelligent Q&A**

Key capabilities include: Q&A for console operations. Cloud product knowledge retrieval. Standard change plan retrieval. Environment information queries. O&M service consultation.

**O&M agents**

The following agents are available: Information query assistant: This O&M agent queries information on the cloud platform. It uses natural language input and the NL2API capabilities of a large language model (LLM) to retrieve and display configuration item (CI) information from the CMDB. Network O&M assistant: Analyzes user requests containing IP addresses, instance IDs, or alert data in real time. This agent automatically correlates network asset topology, identifies resource binding relationships, performs health checks and traffic path diagnostics on load balancer instances, and parses alert semantics. It combines this data with historical events and performance metrics to conduct root cause analysis and provide precise remediation recommendations. This improves network anomaly detection and platform security. Expert consultation assistant: Uses the experience of expert O&M teams to help troubleshoot and resolve common cloud platform issues. It supports services such as solution queries, best practices, and O&M consultation. Report assistant: Queries existing reports and dashboards, and creates new reports based on statistical and trend data, including capacity, resource utilization, assets, and alert events. This enables data-driven O&M decision-making. Alert assistant: Analyzes and diagnoses alerts and events on the cloud platform. It processes alert events in real time to analyze their distribution, trends, and correlation with historical data. This analysis, combined with cloud product performance metrics and diagnostic tools, helps identify anomalies and potential risks and provides precise recommendations to improve O&M efficiency and platform security. Change assistant: Recommends suitable change plans based on user-described scenarios. It covers standard changes such as hardware repair, product scaling, Hotx upgrades, and data cleanup. Diagnosis assistant: Performs root cause analysis based on product blueprints and failure scenarios. It provides diagnostic recommendations by combining user input (such as health status, alerts, and symptoms) with topology dependencies, product logs, and other alert data. Inspection assistant: Inspects cloud products, components, hardware, and the cloud platform to identify potential operational risks. Apsara AIOps Product Introductio Script assistant: Supports general O&M commands, Tongque inspection scripts, common command-line interface (CLI) commands for cloud products, Ark commands, and Tianji operations. It generates efficient scripts with a single click to enhance O&M automation.

**Application management**

Centrally create, configure, and manage Q&A-based and workflow-orchestrated intelligent applications. This provides unified, full-lifecycle management for AI applications.

**MCP management**

View the platform's built-in MCP Servers and make them available to applications.

**Knowledge base**

Includes a built-in knowledge base containing O&M knowledge for the cloud platform, including official product documentation, monitoring alerts, FAQs, standard change plans, upgrade guides, and delivery solutions. You can also create and manage your own knowledge bases and upload custom O&M documents.

**System settings**

Display built-in models and configure external inference services. This provides unified management and flexible scaling of model services. Apsara AIOps Product Introductio

## Product value

This topic explains the value of Apsara Cloud Intelligence. Apsara Cloud Intelligence delivers a one-stop, intelligent operations and maintenance (O&M) solution by deeply integrating a proprietary large model trained for Apsara Stack with platform O&M scenarios. This helps O&M teams increase efficiency, lower incident rates, and build industry influence through industry collaboration and award recognition.

**O&M efficiency**

Enhanced intelligent O&M capabilities: Apsara Cloud Intelligence is built on a knowledge base from a decade of Apsara Stack O&M experience. This foundation includes millions of daily O&M issues, over 100,000 high-quality documents, and the expertise of more than 2,000 Apsara Stack specialists, covering professional domains such as CLI solutions, FAQs, delivery plans, and standard change procedures. The platform uses the large model's advanced understanding and reasoning capabilities in the O&M domain to significantly reduce issue response time and cut ticket resolution time by 37%. Rich ecosystem of O&M agents: Apsara Cloud Intelligence provides a comprehensive set of O&M agents, such as an alert assistant, an intelligent diagnosis assistant, a platform inspection assistant, and tools for O&M information query, script generation, and intelligent reporting. These agents enable an intelligent transformation of the entire O&M lifecycle. As a result, it reduces repetitive queries for on-site teams by 70%, doubles diagnostic efficiency, and shortens script development time from hours to minutes. This approach reduces overall O&M costs by 40%, with AI automating tasks that would otherwise require 30% of manual effort. Unified intelligent O&M platform: Apsara Cloud Intelligence integrates out-of-the-box capabilities, including the platform toolbox, knowledge base, and MCP Server. It serves as the foundation for an enterprise's intelligent O&M, shifting the paradigm from reactive responses to proactive prevention. AI-driven insights enable precise decision-making for specific O&M scenarios, reducing problem identification time in general O&M domains by 90% and lowering labor costs by 40%, while also raising system availability to an industryleading standard.

**Industry influence**

Award submissions: Organizations can use the backend capabilities of Apsara Cloud Intelligence to consolidate and build upon their private operations and maintenance knowledge. By integrating with their existing OA and O&M systems, they can create diverse application scenarios for the large model. This allows them to compete for relevant industry awards and recognition, such as an 'Intelligent O&M Technology Innovation Award' or an 'Industry Development Award' in sectors like finance, securities, or energy. Industry collaboration: By partnering with industry organizations, such as the China Academy of Information and Communications Technology (CAICT), renowned universities, or financial technology institutions, organizations can engage in joint research and projects to collectively advance industry standards and best practices for large models in operations and maintenance. These collaborations enhance their brand awareness and influence. Apsara AIOps Product Introductio

## Use cases

This topic introduces the typical use cases of Cloud Intelligence Assistant.

**Intelligent O&M Q&A**

The assistant uses natural language to answer O&M questions about platform alerts, operational tasks, and standard changes. The assistant queries your knowledge base and historical ticket data in real time to provide accurate solutions, reducing the need for manual support.

**Real-time topology query**

The assistant dynamically parses CMDB data to visualize resource dependency chains and help you quickly locate anomalies in your environment.

**Risk prediction and optimization**

The assistant analyzes time series data to predict resource bottlenecks and proactively recommend scaling or configuration optimization plans.

**Intelligent root cause analysis**

The assistant correlates logs, topology, monitoring metrics, and event data to automatically generate a root cause analysis for failures. This can reduce diagnostic time by 80%.

**Automated script generation**

The assistant translates O&M requirements into executable Python/Shell scripts and automatically verifies their security.

**Intelligent dashboards**

The assistant automatically generates analytical dashboards based on O&M data to display information about resources, resource levels, and alerts.

**Enterprise-grade O&M agents**

Cloud Intelligence Assistant provides a standard development platform with built-in capabilities, such as a platform toolkit and the MCP Server, to help you quickly build custom O&M intelligent agents for your enterprise.

| Module | Description |
|---|---|
| Intelligent Q&A | Provides answers to questions about general O&M topics, cloud product information, standard change procedures, and knowledge base (KB) articles for monitoring and alerts. You can also highlight an O&M object in your current environment to query it in real time. |
| Information Query Assistant | Uses natural language processing to understand your queries and accurately retrieve information. For example, you can ask for server details or query dependency relationships. |
| Diagnosis Assistant | Analyzes cloud product logs, monitoring data, and blueprint topologies to provide AI-assisted root cause analysis. It supports two modes: Normal Diagnosis and Deep Diagnosis. |
| Scripting Assistant | Generates efficient scripts with a single click to enhance O&M automation. It supports a wide range of commands, including general O&M commands, TQ inspection scripts, common CLI commands for cloud products, Ark commands, and Apsara operations. |
| Report Assistant | Helps you find existing reports and dashboards. You can also create new reports based on statistics and trends from data sources such as capacity, utilization, assets, and alert events. This enables you to make data-driven O&M decisions. |
| Alert Assistant | The Alert Assistant intelligently analyzes and diagnoses alert data in your cloud environment. It processes the latest alert information in real time to analyze distribution, trends, correlations, and historical patterns. This helps you quickly identify abnormal fluctuations and potential risks, suggests targeted remedies, and improves your cloud O&M efficiency and security. |

| Module | Description |
|---|---|
| Application management | You can edit built-in applications, including their basic information, associated knowledge base, and model parameters. You can also create, debug, and publish a new AI application. You can review detailed information, such as debugging records, application logs, and monitoring data. |

Apsara AIOps Product Introductio

## Features

This topic describes the key features of Intelligent O&M Assistant.

**Frontend**

| Knowledge base | The built-in knowledge base contains O&M information for the cloud platform, such as official product documentation, articles for monitoring and alerts, FAQs, and standard procedures for changes, upgrades, and delivery. You can also create a custom knowledge base by uploading your own O&M documents. |
|---|---|
| Model management | Manage the models for your AI applications. You can add, edit, and delete models. |

Apsara AIOps Product Introductio
