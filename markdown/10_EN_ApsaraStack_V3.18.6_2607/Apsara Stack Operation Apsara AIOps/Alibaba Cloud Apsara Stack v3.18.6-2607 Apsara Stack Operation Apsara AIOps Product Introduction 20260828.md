---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 11
source_pdf: "84fb617d9efe4be0_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps Product Introduction 202"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20Stack%20Operation%20Apsara%20AIOps%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps Product Introduction 20260828

## Table of Contents

- 1 Intelligent O&M Assistant
- 2 Product details
- 3 Product value
- 4 Use cases
- 5 Functions and features

## 1 Intelligent O&M Assistant

This chapter introduces the Intelligent O&M Assistant. The Intelligent O&M Assistant is the entry point for intelligent Operations and Maintenance (O&M) upgrades on the Apsara Stack platform. It provides platform O&M engineers with capabilities such as O&M Q&A, environment information queries, content matching and recommendation, predictive optimization suggestions, inference, analysis, summarization, and code and visualization generation. The assistant also serves as a foundation for customer-facing intelligent O&M. It provides out-of-the-box capabilities that integrate the platform's Toolbox, knowledge base, and MCP Server to facilitate the engineering and deployment of O&M agents on-premises.

## 2 Product details

frontend comprises intelligent Q&A and a suite of O&M agents, while O&M LLM management

**Frontend**

**Intelligent Q&A**

Intelligent Q&A provides the following capabilities: Answers questions about Operations Console operations. Searches for cloud product knowledge. Searches for standard change plans. Queries environment information. Provides consultations on O&M services.

**O&M agents**

The following agents are available: Information Query Assistant: This is a cloud platform-based O&M information query agent. Based on user input, it leverages the Natural Language to API (NL2API) capability of the Large Language Model (LLM) to query the corresponding Configuration Item (CI) information from the Configuration Management Database (CMDB) and displays the results. Network Operations Assistant: This assistant analyzes IP addresses, instance identifiers, and alert information in user requests in real time. It automatically associates network asset topologies, identifies resource binding relationships, and performs health checks and traffic path diagnosis on Server Load Balancer (SLB) instances. Furthermore, it parses alert semantics, conducts root cause analysis based on historical events and performance metrics, and provides precise remediation recommendations to improve the efficiency of locating network exceptions and enhance system security on the cloud platform. Expert Consultation Assistant: This assistant draws on the O&M experience of expert service teams and focuses on troubleshooting common cloud platform issues. You can query solutions and best practices, as well as consult on O&M services. Report Assistant: This assistant helps you query existing reports and cards. It also allows you to create reports based on the statistics and trends of capacity data, usage data, asset data, and alert events to enable data-driven O&M decision-making. Alert Assistant: This assistant provides intelligent analysis and diagnosis services for alert and event data in cloud platform environments. It retrieves and processes alert events in real time, and analyzes their distribution, trends, correlations, and historical comparisons. By combining with cloud product performance metrics and assisted diagnostics, it helps users quickly locate exceptions and potential risks, provides precise remediation recommendations, and improves cloud platform O&M efficiency and security. Change Assistant: This assistant recommends change plans suitable for users' scenarios. The coverage includes standard changes such as hardware repair, product scaling, hotfix upgrades, and resource cleanup. Diagnostic Expert: This assistant performs root cause analysis based on product blueprints and fault scenarios. It combines user input (such as health status, alert events, and problem symptoms) with topology dependencies, product logs, and alert events to provide diagnostic recommendations. Inspection Assistant: This assistant inspects cloud products, components, hardware, and cloud platforms for operational risks. Script Assistant: This assistant allows you to generate efficient scripts with one click for general O&M commands, Tongque inspection scripts, common cloud product Command- Line Interface (CLI) commands, Ark commands, and Tianji operations to improve O&M automation.

**O&M LLM management and control - AIOps**

**Application management**

You can centrally create, configure, and manage Q&A and workflow-orchestrated intelligent applications, enabling unified lifecycle management of AI applications.

**MCP management**

You can view the built-in Model Context Protocol (MCP) servers on the platform for easy integration with your applications.

**Knowledge base**

The system provides a built-in knowledge base that contains O&M knowledge for the cloud platform, including official product documentation, monitoring and alert data, FAQs, standard changes, upgrade plans, and delivery plans. You can also manage custom knowledge bases by creating them in the backend and uploading custom O&M documents.

**Corpus system**

Corpus tasks: The corpus system provides a unified entry for managing corpus tasks and supports the full workflow of receiving, annotating, and reviewing tasks. You can view task details and perform operations from either a personal or global perspective.

**System settings**

Model management: This feature displays built-in models and allows the configuration of external inference services, enabling unified management and flexible scaling of model services.

## 3 Product value

This topic explains the value of Apsara Cloud Intelligence. Apsara Cloud Intelligence delivers a one-stop, intelligent operations and maintenance (O&M) solution by deeply integrating a proprietary large model trained for Apsara Stack with platform O&M scenarios. This helps O&M teams increase efficiency, lower incident rates, and build industry influence through industry collaboration and award recognition.

**O&M efficiency**

Enhanced intelligent O&M capabilities: Apsara Cloud Intelligence is built on a knowledge base from a decade of Apsara Stack O&M experience. This foundation includes millions of daily O&M issues, over 100,000 high-quality documents, and the expertise of more than 2,000 Apsara Stack specialists, covering professional domains such as CLI solutions, FAQs, delivery plans, and standard change procedures. The platform uses the large model's advanced understanding and reasoning capabilities in the O&M domain to significantly reduce issue response time and cut ticket resolution time by 37%. Rich ecosystem of O&M agents: Apsara Cloud Intelligence provides a comprehensive set of O&M agents, such as an alert assistant, an intelligent diagnosis assistant, a platform inspection assistant, and tools for O&M information query, script generation, and intelligent reporting. These agents enable an intelligent transformation of the entire O&M lifecycle. As a result, it reduces repetitive queries for on-site teams by 70%, doubles diagnostic efficiency, and shortens script development time from hours to minutes. This approach reduces overall O&M costs by 40%, with AI automating tasks that would otherwise require 30% of manual effort. Unified intelligent O&M platform: Apsara Cloud Intelligence integrates out-of-the-box capabilities, including the platform toolbox, knowledge base, and MCP Server. It serves as the foundation for an enterprise's intelligent O&M, shifting the paradigm from reactive responses to proactive prevention. AI-driven insights enable precise decision-making for specific O&M scenarios, reducing problem identification time in general O&M domains by 90% and lowering labor costs by 40%, while also raising system availability to an industryleading standard.

**Industry influence**

Award submissions: Organizations can use the backend capabilities of Apsara Cloud Intelligence to consolidate and build upon their private operations and maintenance knowledge. By integrating with their existing OA and O&M systems, they can create diverse application scenarios for the large model. This allows them to compete for relevant industry awards and recognition, such as an 'Intelligent O&M Technology Innovation Award' or an 'Industry Development Award' in sectors like finance, securities, or energy. Industry collaboration: By partnering with industry organizations, such as the China Academy of Information and Communications Technology (CAICT), renowned universities, or financial technology institutions, organizations can engage in joint research and projects to collectively advance industry standards and best practices for large models in operations and maintenance. These collaborations enhance their brand awareness and influence.

## 4 Use cases

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

## 5 Functions and features

This topic describes the typical functions and features of Apsara AIOPS.

**Frontend**

| Module | Description |
|---|---|
| Intelligent Q&A | The system answers questions about general O&M knowledge, cloud product knowledge, standard change plans, and the monitoring and alert knowledge base. You can also select a text that refers to an O&M object in the current environment to run real-time interactive queries. |
| Information query assistant | The natural language-based query feature understands user intent and returns accurate results, such as server information and associations. |
| Diagnostic assistant | This assistant analyzes cloud product logs, monitoring data, and blueprint topologies to provide intelligent root cause analysis. The system supports both standard diagnosis and deep diagnosis. |
| Script assistant | This assistant allows you to generate efficient scripts with one click for general O&M commands, Tongque inspection scripts, common cloud product Command-Line Interface (CLI) commands, Ark commands, and Tianji operations to improve O&M automation. |
| Report assistant | This assistant helps you query existing reports and cards. It also allows you to create reports based on the statistics and trends of capacity data, usage data, asset data, and alert events to enable data-driven O&M decision- making. |
| Alert assistant | This assistant provides intelligent analysis and diagnosis services for alert data in the coud platform environment. The assistant retrieves and processes the latest alert information in real time, analyzes alert distribution, trends, correlations, and historical comparisons, helps you identify abnormal fluctuations and potential risks, and provides targeted handling suggestions to ensure efficient and secure cloud platform O&M. |

**O&M LLM management and control - AIOps**

| Module | Description |
|---|---|
| Application management | You can edit built-in applications, including their basic information, knowledge base scope, and model parameters. You can also create AI applications, debug and publish them, and view detailed information such as debug records, application logs, and monitoring data. |
| MCP management | You can view the built-in Model Context Protocol (MCP) servers on the platform for easy integration with your applications. |

| Knowledge base | The system provides a built-in knowledge base that contains O&M knowledge for the cloud platform, including official product documentation, monitoring and alert data, FAQs, standard changes, upgrade plans, and delivery plans. You can also manage custom knowledge bases by creating them in the backend and uploading custom O&M documents. |
|---|---|
| Corpus system | The corpus system provides a unified entry for managing corpus tasks and supports the full workflow of receiving, annotating, and reviewing tasks. You can view task details and perform operations from either a personal or global perspective. |
| System settings | The model management feature displays built-in models and allows the configuration of external inference services, enabling unified management and flexible scaling of model services. |
