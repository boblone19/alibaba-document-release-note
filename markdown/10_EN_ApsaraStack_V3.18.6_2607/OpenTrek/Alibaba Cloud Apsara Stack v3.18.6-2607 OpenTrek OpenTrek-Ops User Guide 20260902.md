---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek-Ops User Guide 20260902"
product_version: "V3.18.6_2607"
doc_version: "20260902"
pdf_pages: 68
source_pdf: "c76bd8003dea53f0_Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek-Ops  User Guide 20260902.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/OpenTrek/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20OpenTrek%20OpenTrek-Ops%20%20User%20Guide%2020260902.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek-Ops User Guide 20260902

## Table of Contents

- 1 Overview
- 2 Log in to the OpenTrek-Ops platform
- 3 Operations overview
- 4 AI assistant
- 5 O&M Center
  - 5.1 Agent list
  - 5.2 Project management
  - 5.3 Capabilities and plugins
- 6 Change history
- 7 Infrastructure
- 8 Security center
  - 8.1 Security settings
  - 8.2 Audit logs
- 9 Session analysis
- 10 UModel exploration
- 11 Operational analysis
  - 11.1 Cost analysis
- 12 System settings
  - 12.1 Tenant management
  - 12.2 Configuration management
- 13 Configure an Ops administrator
- 14 FAQ

ew

## 1 Overview

This topic describes the features and usage of the OpenTrek-Ops platform. OpenTrek-Ops is a multi-agent operations and governance platform based on the xClaw paradigm, providing full lifecycle management for enterprise-grade AI agents. The platform delivers an all-in-one solutions for Ops teams, covering the creation, deployment, monitoring, collaboration, and governance of agents.

**Product architecture**

OpenTrek-Ops divides Ops management into three layers: agent Ops, skill asset Ops, and infrastructure Ops. The platform accumulates Ops experience and collects data across these three layers to aggregate Ops data into a unified governance center, performing integrated analysis and comprehensive processing on the data. OpenTrek-Ops provides a unified Ops portal to deliver a consistent Ops experience for users. The platform integrates with various infrastructure services, including LLM Service, Redis, OSS, and PostgreSQL. It also exposes data from the Ops system to third-party systems through APIs.

**Scenarios**

OpenTrek-Ops applies to the following scenarios:
**Automated intelligent operations**: Automate the execution of operational tasks through
agents to reduce manual operation costs.
**Multi-agent collaboration**: Build agent projects to enable multi-role collaboration in
complex Ops scenarios.
**Skill asset management**: Manage, review, and distribute agent skills in a unified manner
to enable capability reuse.
**Ops governance**: Monitor the running status, token consumption, and error rates of
agents comprehensively.

**Prerequisites**

You have obtained the endpoint, username, and password of the OpenTrek-Ops platform from the administrator. We recommend that you use the Google Chrome browser.

**User roles**

User roles provide different operation permissions for different users. The system creates the OPENTREKOPS application permission for agent Ops by default during initialization. The permissions are as follows:

| Role | Permission description |
|---|---|
| Platform administrator | This role has platform management permissions only. Users with this role can only view and operate features related to platform management. |
| Operations administrator | This role has operations management permissions only. Users with this role can view and operate the pages and features in the Overview, AI Assistant, Ops Center, Asset Center, and Operations Analysis menus. |

ew

| Project administrator | This role has project management permissions only. Users with this role can view and operate the pages and features in the AI Assistant and Ops Center menus. |
|---|---|
| Tenant administrator | This role has tenant management permissions only. Users with this role can only view and operate the pages and features in the Organization Management menu. |
| Tenant operations administrator | This role has tenant operations permissions only. Users with this role can view and operate the pages and features in the Overview, AI Assistant, Ops Center, Asset Center, Security Center, and Operations Analysis menus. Users with this role can create and manage agents, projects, and skills. |

**Navigation structure**

The platform navigation in V1.1.1 adopts a five-group classification layout to help users locate feature modules quickly:

| Navigation group | Included modules |
|---|---|
| Workbench | Overview and AI Assistant |
| Management | Ops Center (Agent List, Project Management, Capabilities and Plugins), Change History, and Infrastructure |
| Security | Security Center (Security Settings and Audit Logs) |
| Analysis | Operation Analysis (Cost Analysis) |
| System | System Settings (Tenant Management and Platform Management) |

to the OpenTrek-Ops platform

## 2 Log in to the OpenTrek-Ops platform

**platform**

**Log in and log out**

This topic describes how users log in to and log out of the OpenTrek-Ops platform.

**Scenarios**

Logging in and logging out are basic operations for using the OpenTrek-Ops platform. These operations apply to the following scenarios: O&M personnel access the platform on a daily basis to perform O&M operations. Administrators perform system configuration and management. Users securely log out of the system after they complete their operations.

**Prerequisites**

You have obtained the endpoint, username, and password of the OpenTrek-Ops platform from the administrator. The administrator provides the endpoint of the OpenTrek-Ops platform. We recommend that you use the Chrome browser.

**Procedure**

1. Open a browser.
2. Enter the endpoint of the OpenTrek-Ops platform in the address bar and press Enter.
3. Enter the correct username and password.

**Note**

Obtain the username and password for logging in to the OpenTrek-Ops platform from the administrator. If you enter an incorrect password multiple times in a row, the system enables the verification code logon feature. If you reach the maximum number of consecutive incorrect attempts, the system locks the account. Contact the administrator to activate the account. When you log in to the OpenTrek-Ops platform for the first time, the system may require you to change the initial password. Follow the prompts to change the password. To improve security, the password must meet the following requirements: The password must contain uppercase and lowercase English letters. The password must contain Arabic numerals (0 to 9). The password must contain special characters. The password must be 10 to 20 characters in length.
4. Click **Log In**.

**Log out of the system**

to the OpenTrek-Ops platform
1. In the lower-left corner of the page, click
on the right side of the current logon user.
2. In the dialog box, click **Sign Out**.
tions overview

## 3 Operations overview

This topic describes the features and metrics on the **Operations Overview** page of the OpenTrek-Ops platform.

**Scenarios**

The **Operations Overview** page is the default dashboard of the platform, ideal for the following scenarios: Perform daily O&M inspections to quickly understand the overall health status of the platform. Monitor agent operation trends and token consumption to evaluate resource usage efficiency. View model performance metrics to analyze the response time and processing capabilities of different models. Monitor infrastructure status to promptly detect and troubleshoot service exceptions.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform as a tenant operations administrator.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
After logging in, the system redirects you to the **Operations Overview** page by default.
2. On the **Operations Overview** page, you can view the following core modules:

| Module | Description |
|---|---|

tions overview

| Project Overview | Displays the statistics on the number of projects and agents. Today's Top 5 Active Projects Displays a list of the top five projects ranked by activity today. |
|---|---|
| Weekly Activity Trend | Displays the activity trend over the last seven days. |
| Model Performance | Displays the TTFT P99 and TPOT P99 performance metrics for each model. |
| Cloud Products | Displays the number of instances for API Gateway, Object Storage Service (OSS), PolarDB, and Kubernetes. |
| Token Trend | Displays the token consumption trend over time in a line chart. When you move the pointer over the line chart, the system displays the total token data for the corresponding point in time. |
| Model Token Distribution | Displays the token usage distribution across different models. |
| Infrastructure | Displays the usage of CPU, memory, and storage. |
| Central dashboard | Displays the running status of infrastructure such as Alibaba Cloud Container Service for Kubernetes (ACK), Large Language Model (LLM) Service, Redis, OSS, and PostgreSQL (PG). Blue indicates that the service is running normally. Today's Tokens Displays the total token consumption for the current day. Active Projects Today Displays the number of active projects for the current day. Active Agents Today Displays the number of active agents for the current day. Error Rate Displays the error rate metric for current requests. Peak QPS Today Displays the peak QPS for the current day. |

**Next steps**

After obtaining the operations overview information as needed, you can view and manage detailed agent information through the agent management feature. stant

## 4 AI assistant

The AI Ops Assistant enables automated O&M management. This topic describes how to use the AI Assistant.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **AI Assistant** to open the AI Ops Assistant.
3. Enter your question in the input box of the AI Assistant and click
. Click a quick question on a card to start a session. Ops Management Support centralized lifecycle management of agents, including creation, configuration, and start/stop operations. You can quickly dispatch and manage various Ops tasks such as deployment, restart, and configuration updates to automate operations. Smart Insights Query operational metrics and cost data of agents, with multi-dimensional analysis and trend prediction on key data such as performance, cost, and traffic, to identify resource waste and inefficient usage scenarios and provide cost reduction and efficiency improvement solutions. Fault Diagnosis Diagnose the token cost, performance latency, resource health, and engine health of agents. The system provides actionable diagnosis and handling suggestions to help you quickly troubleshoot agent exceptions. Create a task: Click **New Task** in the upper-left corner of the page to start a new conversation. Historical task: Search for a historical task in the conversation task record search box to view the historical task records. stant Delete a task: Move the pointer over the target conversation task, click next to the task, and select **Delete** to delete the historical task record. Rename a task: Move the pointer over the target conversation task, click next to the task, select **Rename**, edit the task name, and then click . Pin a task: Move the pointer over the target conversation task, click next to the task, and select **Pin** to pin the task.
4. In the upper-left corner of the **AI Assistant** interface, click **Long-running Tasks**.
i. View long-running tasks. On the **Long-running Tasks** page, you can view the metrics of long-running tasks, including **Total Tasks**, **Running**, **Today's Success Rate**, and **Today**. ii. Create a task. On the **Long-running Tasks** page, click **New Task**, enter a task name, set the scheduled time, select an execution model, describe the task, and then click **Save**. iii. Execute a task manually. On the **Long-running Tasks** page, click **Execute Manually** in the **Actions** column of the target task. The system triggers the task. You can select the task under Scheduled Job on the left side to view the execution details. iv. Edit a scheduled task. On the **Long-running Tasks** page, click **Edit** in the **Actions** column of the target task, modify the task name, scheduled time, execution model, and description, and then click
**Save changes**.
v. Disable or enable a scheduled task. On the **Long-running Tasks** page, click **Disable** or **Enable** in the **Actions** column of the target task to manage the task status. vi. View the details of a scheduled task. On the **Long-running Tasks** page, click **Details** in the **Actions** column of the target task to view the task details. vii. Delete a scheduled task. On the **Long-running Tasks** page, click **Delete** in the **Actions** column of the target task, and then click **Delete** in the dialog box. viii. Filter and search for scheduled tasks. On the **Long-running Tasks** page, you can filter tasks by All, Enabled, or Disabled, and can also search for a task by name or description.
5. In the upper-left corner of the **AI Assistant** interface, click **Operations Knowledge Base**.
i. View the built-in knowledge base. On the **Operations Knowledge Base** page, click **All Knowledge Bases** to view the built-in OpenTrek-Ops product documentation. Click **Details** in the **Actions** column to view specific documents, index status, settings, and other detailed information. stant ii. Create a knowledge base. a. On the **Operations Knowledge Base** page, select the **Created by Me** tab, click
**Create Knowledge Base**, enter a knowledge base name and description, select the
visibility scope, and then click **Create Knowledge Base**. b. Upload a document. Click **Details** in the **Actions** column of the created knowledge base. On the **Document**
**Management** tab, click **Upload Document** to upload a local document.
c. Index status On the **knowledge base** details page, select **Index Status** to view the index details of the knowledge base. d. Retrieval test On the **knowledge base** details page, select **Retrieval Test**, enter a keyword from the document, and click **Search**. The interface displays the retrieval results. e. Settings On the **knowledge base** details page, select **Settings** to view the basic information, personal space quota, and retrieval model of the knowledge base. iii. View the details of a knowledge base. Click **Details** in the **Actions** column of the created knowledge base to view specific documents, index status, settings, and other detailed information. iv. Rebuild the index. Click **Rebuild index** in the **Actions** column of the created knowledge base, and the system rebuilds the indexes of all documents in the knowledge base. The previous version continues to serve requests until the new version is ready. v. Delete a knowledge base. Click **Delete** in the **Actions** column of the created knowledge base. After confirmation, the system also deletes the documents and indexes.

## 5 O&M Center

### 5.1 Agent list

This topic describes how to manage agents in the OpenTrek-Ops platform. You can host, view, edit, start, stop, scale, and delete agents.

**Common scenarios**

Agent management is a core feature of the platform and applies to the following scenarios: Create new Ops agents to automate specific Ops tasks. Manage the configuration and running status of existing agents to ensure that the agents run properly. Allocate and manage agent resources for different projects to optimize resource allocation. View agent execution records to analyze agent performance and troubleshoot issues.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. You have the tenant operations administrator role or a role with agent creation permissions.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Operation Center** > **Agent List** to go to the
**Agent Management** page.
You can view the following information on this page: Use the search box to search for an agent by name. Use the **All Creators** drop-down list to filter the agent list by creator. Use the **All Projects** drop-down list to filter the agent list by project. Click the view switch button to switch between the grid view and the list view. View agents that you created or favorited, and filter them by the **All**, **xClaw**, **Workflow**, or **Pro-Code** type. View agent cards that display information such as the agent icon, name, type label, project, creator, and running status.
3. Host an agent.
On the **Agent Management** page, click **Hosted Agent**. The system supports three types:
**xClaw**, **Workflow**, and **ProCode**.

**xClaw**

The **xClaw** tab is selected by default. Fill in the following information in the form:

| Module | Parameter | Required | Description |
|---|---|---|---|
| Basic Info | Name | Yes | The display name of the agent. We recommend using a meaningful name. |
|   | Description | No | The feature description of the agent. |
|   | Type | Yes | Select the agent type. The system supports three types: QwenPaw, OpenClaw, and Hermes. |
|   | Project | Yes | Select the project to which the agent belongs. |
|   | Version | Yes | Select the professional or standard version. The professional version provides comprehensive capabilities, including powerful memory services, auto scaling, and comprehensive observability. The standard version provides limited capabilities. It supports basic Ops features and does not guarantee high availability. |
| Persona | Persona | No | Describe the persona traits. |
|   | Behavior Boundary | No | Define the behavior boundaries. |
| Skill Configurati on | / | No | Click Add Skill, select a skill, and then click Confirm. Note Before you add a skill, make sure that you have created a skill on the Capabilities and Plug-ins > Skills tab. |

| Plugin Configurati on | / | No | Click Add Plugin, select a plugin, and then click Confirm. Note Before you add a plugin, make sure that you have uploaded a plugin on the Capabilities and Plug-ins > Plugins tab. |
|---|---|---|---|
| Channel Settings | / | No | You can enable DingTalk, WeChat, and WeCom. Note Before you configure channels, make sure that you have enabled channels in System Settings > Configuration Management > Channel Management. |
| Visibility | / | Yes | Control which users can view this agent. Only Me All Project Members Specific Members |

After you fill in the information, click **Create**. After the agent is created, the new agent appears in the agent list.

**Workflow**

Select the **Workflow** tab and fill in the following information in the form:

| Module | Parameter | Require d | Description |
|---|---|---|---|
| Basic Info | Agent Name | Yes | The display name of the workflow application. We recommend using a meaningful name. |
|   | Feature Description | No | Briefly describe the features of the workflow. |
|   | Project | Yes | Select the project to which the agent belongs. |
| Workflow Orchestrati on | DSL Type | Yes | Dify DSL by default. |
|   | Dify Platform | Yes | Select a Dify platform. |
|   | > Document Version: 2026090 |   |   |

| Trek |   |   |   |
|---|---|---|---|
|   | Upload DSL File | Yes | Click to upload or drag and drop a file to the upload area. The system supports the .json, .yaml, and .yml formats. |
| Visibility | / | Yes | Control which users can view this agent. Only Me All Project Members Specific Members |

After you fill in the information, click **Create Agent** to complete the creation. After the agent is created, the new agent appears in the agent list.

**Pro-code**

Select the **ProCode** tab and fill in the following information in the form:

| Module | Parameter | Require d | Description |
|---|---|---|---|
| Basic Info | App Name | Yes | The display name of the pro-code agent. We recommend using a meaningful name. |
|   | Description | No | Briefly describe the application feature. |
|   | Project | Yes | Select the project to which the agent belongs. |
|   | Agent Framework | Yes | Select a built-in agent framework. |
|   | Tech Stack | Yes | Select a runtime. You can select a specific version or Other. |
|   | PUBLISH PLATFORM | Yes | The system supports Self-Managed Platform. Deploy the agent to your own platform. |
|   | RESOURCE CONFIGURATI ON | Yes | Set the number of replicas, CPU, and memory. |

| Deploymen t Configurati |   |   |   |
|---|---|---|---|
|   | IMAGE CONFIGURATI ON | Yes | Image Source The system supports Custom Registry. Image Address Enter the complete image pull address, including the registry, namespace, image name, and tag. Image Pull Policy The system supports Prefer local image, Always pull image, and Use local image only. Image Authentication Select an existing secret or create a new secret. |
| on |   |   |   |
|   | LAUNCH CONFIGURATI ON | No | Enter the launch command and port. |
|   | Health Check | No | Enter the check path, check port, check interval, and timeout period. |
|   | Environment Variables | No | Set environment variables. The system supports Form Mode and JSON Mode. |
| Visibility | / | Yes | Control which users can view this agent. Only Me All Project Members Specific Members |

After you fill in the information, click **Create App** to complete the creation. After the application is created, the new agent appears in the agent list.
4. Discover an agent.

**Note**

Discover and integrate existing agents from Alibaba Cloud Model Studio or Dify. OpenTrek Dev On the **Agent Management** page, click **Discover Agent**. On the **OpenTrek Dev** tab, configure the following parameters:

| Parameter | Description |
|---|---|
| Platform | Select an integrated Alibaba Cloud Model Studio platform. |

| Type | Select the agent to integrate. The system imports all published versions of the agent as independent agents. The system supports two types: Autonomous Agent and Workflow. |
|---|---|
| Select Agent | Search for an agent by name and select it. You can select multiple agents. |
| Project | Select a project. |
| Visibility | Control which users can view this agent. Only Me All Project Members Specific Members |

Click **Import Agent**. The new agent appears in the agent list after the creation succeeds. Dify On the **Agent Management** page, click **Discover Agent**. On the **Dify** tab, configure the following parameters:

| Parameter | Description |
|---|---|
| Platform | Select an integrated Alibaba Cloud Model Studio platform. |
| App Type | Select the agent to integrate. The system imports all published versions of the agent as independent agents. The system supports five types: Workflow, Chatflow, Chat Assistant, Agent, and Text Generation. |
| Select Agent | Search for an agent by name and select it. You can select multiple agents. |
| Project | Select a project. |
| Visibility | Control which users can view this agent. Only Me All Project Members Specific Members |

Click **Import Agent**. The new agent appears in the agent list after the creation succeeds.
5. View the agent details.
On the **Agent Management** page, find the target agent and click the agent card to go to the agent details page. On the agent details page, view the following information: Basic information: The name, type, description, creation time, project, primary model, and more. Running status: Running, Changing, Stopped, or Abnormal. Configuration information: The running configuration parameters of the agent, such as overview, persona, skills and tools, channels, cloud resources, version history, security settings, metrics analysis, trace analysis, and topology.

**Note**

For pro-code agents, you can view the details of instances and scaling, backup and version, metrics analysis, and trace analysis. For workflow agents, you can view the details of overview, channels, and version management. Operational logs: The historical execution records of the agent, including historical tasks and logs.

**Related operations**

| Operation type | Agent type | Procedure |
|---|---|---|
|   |   | 1. Find the target agent in the agent list. 2. Click the agent card to go to the agent details page. 3. In the Basic Info section, edit the Primary Model as needed. 4. Click More > Edit in the upper-right corner of the page to edit the agent name, description, and visibility. 5. In the lower part of the details page, click theP ersona, Skills and Tools, Channels, Cloud Resources, Version History, or Security Settings tab to edit the related information. i. Persona Edit the Identity, Persona, and Behavior Boundaries, and then click Save. |

|   |   | ii. Skills and Tools Skills Add a skill Click Add Skill, select one or more skills, and then click OK. Note Before adding a skill to an agent, you must first add the skill to the project to which the agent belongs. Roll back a skill If an added skill has multiple versions, click the skill name and switch the version in the upper-right corner of the skill details page to roll back the skill version. Delete a skill Click the delete icon next to an added skill to remove the skill. Update the skill status |
|---|---|---|
| Edit an agent | xClaw | Click next to an added skill to enable or disable the skill. Plugins Add a plugin Click Add Plugin, select the target plugin, and then click OK. Delete a plugin Click the delete icon on the plugin card to remove the plugin. MCP Add an MCP server Click Add MCP. In the Add MCP Server dialog box, search for and select the server, and then click Bind to Agent. Delete an MCP server Click the delete icon next to an added MCP server to remove the MCP server. Update the status of an MCP server Click next to an added MCP server to enable or disable the MCP server. iii. Channels Configure the channel information and click Save Configuration. iv. Cloud Resources Click the delete icon next to the target model service to remove the model. The system synchronizes the change to the agent after removal. v. Version History On the Version History tab, click Publish in the Actions column of a historical version to roll back the agent to that version. |

|   |   | vi. Security Settings Global inheritance The agent inherits global rules. You can disable or enable rules in the Actions column. Agent-specific Add a rule Click Add Rule, set the rule ID, select a tool, configure parameters such as the regex pattern and exclusion pattern, and then click Add. After the rule is added, the status changes to Synchronized. For more information, see Security settings. Enable or disable a rule Click in the Actions column of the target rule to enable or disable the rule. |
|---|---|---|
|   | Pro-code | Edit a rule 1. Click the agent card to go to the agent details page. Click in the Actions column of the target rule to edit the 2. On the agent details page, click More in the upper-right corner and agent rule information. select Edit. Delete a rule 3. Edit the agent name, description, and visibility. 4. Click SaCvliec.k in the Actions column of the target rule to delete the rule. |
|   | Workflow | 1. Click the agent card to go to the agent details page. 2. On the agent details page, click More in the upper-right corner and select Edit. 3. Edit the agent name, description, and visibility, and then clickS ave. 4. In the lower part of the details page: i. Click Channels to configure channels such as DingTalk and WeChat. ii. Click Version Management to preview or publish historical versions. |
| Start or stop an agent | xClaw | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Start or Stop. 3. After confirmation, the system updates the agent status. |
|   | Pro-code | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Take Offline or Start. 3. After confirmation, the system updates the agent status. |

| Restart an agent | xClaw/Pro- code | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickR estart. 3. After confirmation, the system updates the agent status. |
|---|---|---|
| Delete an agent | xClaw/Pro- code/Workfl ow | Note Before you delete an agent, make sure that the agent is in the stopped status. 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Delete. 3. In the confirmation dialog box, click Delete. 4. After deletion, the system removes the agent from the list. |
| Scale | xClaw/Pro- code | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Scale. 3. In the Adjust Resources dialog box, preview the current configuration information and then set the CPU and memory. 4. Click Apply. During the scaling process, the agent status changes to Changing. You can view the scaling task details on theC hange History page. |
| Update an agent | xClaw | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Update. The system displays the available versions for upgrade by default. 3. Click Confirm Upgrade to upgrade the agent. Note When the agent image is the latest version, the Update button is unavailable. |
|   | Pro-code | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Update. 3. Update the basic information, deployment configuration, advanced settings, and other details of the agent as needed. 4. Click Confirm Update. |

|   | Workflow | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Update. Re-upload the DSL file. 3. Click Update. |
|---|---|---|
| Unbind an agent | Workflow | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Unbind. 3. After unbinding, the system clears the workflow agent data on this platform. After confirmation, click Confirm Unbind. |
| Favorite an agent | xClaw/Pro- code | Click the favorite icon on the target agent card to add the agent to favorites. You can then view the agent in My Favorites. |
| Chat with an agent | xClaw/Work flow | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the agent details page, clickC hat to go to the interaction page and start a conversation. Note You can view only the conversations that you initiated. |

**Next steps**

After creating an agent, you can add the agent to a project for collaboration.

### 5.2 Project management

This topic describes how to manage projects in the OpenTrek-Ops platform, including creating projects and managing project members.

**Scenarios**

The project management feature applies to the following scenarios: Build a multi-role O&M team to divide and collaborate on complex O&M tasks. Manage team member agents and permissions to ensure effective management of team members. Coordinate task assignment among agents within the team to improve team collaboration efficiency. Form a dedicated O&M team for a specific project or business scenario.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. You have obtained the tenant operations administrator role or a role with project creation permissions.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Operation Center > Project Management** to go
to the **Project Management** page. Obtain the following information on this page: View the number of total, activated and idle projects as well as the number of bound agents. Use the search box to search for a target project by project name. Filter projects by creator. Click **Create Project** to create a new project. View project cards, which display information such as the project name, number of agents, creator, and description. Click a card to go to the project details page and view the agent list.
3. Create a project.
i. On the **Project Management** page, click **Create Project**. ii. In the pop-up creation form, fill in the following information:

| Parameter | Required | Description |
|---|---|---|
| Project Name | Yes | The display name of the team. We recommend that you enter a meaningful name. |
| Description | No | The responsibilities and goals of the project. |
| K8S Cluster | No | Select a Kubernetes cluster. |
| Model Service | Yes | Select at least one text generation model. |
| Runtime Storage | Yes | Enabled by default. |
| Memory Service | No | Disabled by default. When enabled, select at least one text vectorization model. |
| Permission | No | Configure Project Admin and Project Members. Project Admin: This role has full management permissions for the project and can manage members, resources, and configurations. Project Member: This role can use resources such as agents, skills, and tools under the project. |

iii. Click **Create Project** to complete the creation.
4. Add a project member.
i. Click the target project card to go to the details page. ii. On the Agent tab, click **Create Agent**. Refer to Agent list to add an agent. iii. Click **Create** to complete the addition.
5. Add a skill.
On the project details page, select the **Skills** tab, click **Add Skill**, select a skill, and then click **Confirm** to add the skill to the project.
6. Add a plugin.
On the project details page, select the **Plugins** tab, click **Add Plugin**, select a plugin, and then click **Confirm** to add the plugin to the project.
7. Add an MCP server.
On the project details page, select the **MCP** tab, click **Add MCP**, select an MCP server, and then click **Add to Project** to add the MCP server to the project.
8. Manage cloud resources.
Add a cloud resource On the project details page, select the **Cloud Resources** tab. On the **Model Service** tab, click **Add Resource**, select a model, and then click **Save** to bind the model to the project. Delete a cloud resource On the project details page, select the **Cloud Resources** tab. On the **Model Service** tab, click the delete icon in the **Action** column of the target cloud resource to delete the cloud resource.
9. Trace Analysis.
On the project details page, select the **Trace Analysis** tab to view all trace records under the project. Click a trace ID to view the details.

**Related operations**

**Edit a project**

1. On the **Project Management** page, select the target project and click the project card.
2. Click **Edit** in the upper-right corner of the page to edit the **project name**, **description**,
**project admins**, and **project members**.
3. Click **Save**.

**Delete a project**

**Note**

Before you delete a project, make sure that all agents under the project are cleaned up.
1. On the **Project Management** page, select the target project and click the project card.
2. Click **Delete** in the upper-right corner of the page, and then click **Confirm Delete**.

**Warning**

The deletion operation is irreversible. Proceed with caution.

**Batch operations**

1. On the **Project Management** page, select the target project and click the project card.
2. Click **Batch Operations** in the upper-right corner of the page.
Agent Ops Select **Agent Ops** in the batch operation dialog box, and then select a specific operation.

| Operation type | Procedure |
|---|---|

| Update | Select Operation & Scope a. Select Update for the agent Ops operation. b. Select an agent type: xClaw, Workflow, or ProCode. c. Select the agents and click Next. Configure Parameters Select the runtime and version, and then click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |
|---|---|
| Resize Spec | Select Operation & Scope a. Select Resize Spec for the agent Ops operation. b. Select an agent type: xClaw or ProCode. c. Select the agents and click Next. Configure Parameters Select the target specification or a custom specification, and then click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |
| Restart | Select Operation & Scope a. Select Restart for the agent Ops operation. b. Select an agent type: xClaw or ProCode. c. Select the agents and click Next. Configure Parameters No configuration is required. Click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |

| Start | Select Operation & Scope a. Select Start for the agent Ops operation. b. Select an agent type: xClaw or ProCode. c. Select the agents and click Next. Configure Parameters No configuration is required. Click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |
|---|---|
| Stop | Select Operation & Scope a. Select Stop for the agent Ops operation. b. Select an agent type: xClaw or ProCcode. c. Select the agents and click Next. Configure Parameters No configuration is required. Click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |
| Offline | Select Operation & Scope a. Select Offline for the agent Ops operation. b. Select an agent type: xClaw or ProCode. c. Select the agents and click Next. Configure Parameters No configuration is required. Click Next. Execution Method Select an execution policy: Full Executionp or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |

Skill Ops a. **Select Operation & Scope** a. Select **Skill Ops** for the operation. b. For **Skill Ops**, select **Sync Skill, Upgrade Skill, Disable Skill, or Remove Skill.** c. Select the agents and click **Next**. b. **Configure Parameters** Select the skills and click **Next**. c. **Execution Method** Select an execution policy: **Full Execution** or **Batch Execution**, and then click **Next**. d. **Preview** Preview the details and click **Confirm Execution** after verification. Plugin Operations a. **Select Operation & Scope** a. Select **Plugin Operations** for the operation. b. For **Plugin Operations**, select **Batch Install Plugins** or **Batch Uninstall Plugins**. c. Select the agents and click **Next**. b. **Configure Parameters** Select the plugins and click **Next**. c. **Execution Method** Select an execution policy: **Full Execution** or **Batch Execution**, and then click **Next**. d. **Preview** Preview the details and click **Confirm Execution** after verification. Config Update

| Operation type | Procedure |
|---|---|
| Update Model | Select Operation & Scope a. Select Update Model for the operation. b. Select the agents and click Next. Configure Parameters Select the target models and click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |

| Sync MCP | Select Operation & Scope a. Select Sync MCP for the operation. b. Select the agents and click Next. Configure Parameters No configuration is required. Click Next. Execution Method Select an execution policy: Full Execution or Batch Execution, and then click Next. Preview Preview the details and click Confirm Execution after verification. |
|---|---|

**Next steps**

After creating a project, you can assign skills to the project to enable team collaboration.

### 5.3 Capabilities and plugins

This topic describes how to manage skills, MCPs, and plugins in the Apsara Uni-Manager Operations Console, including creating, enabling or disabling, managing versions, and installing and configuring them.

**Prerequisites**

You have logged on to the OpenTrek-Ops platform. You have obtained the role of a tenant operations administrator or a role that has the creation and plugin permissions.

**Skills**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Operation Center** > **Capabilities and Plugins**.
Go to the **Skills** management page, where you can obtain the following information: View the total number of skills, the number of enabled skills, the number of disabled skills, and the total number of installations. Use the search box to search for a target skill by name. Use category filters to filter skills by All, Efficiency Tools, Data Analysis, Content Creation, Development Tools, or Others. Click **Create Skill** to create a new skill. View skill cards that display the skill icon, name, description, version number, update time, and enablement status.
3. Create a skill.

**Note**

The system provides built-in skills. The actual data prevails. i. On the **Skills** management page, click **Create Skill**. ii. Fill in the following information in the creation form:

| Parameter | Required | Description |
|---|---|---|
| Upload skill package | Yes | Upload a prepared skill package. The package must be a .zip file that contains a skill.md file in the root directory. The skill.md file must include the name and description in YAML format. Important A single skill file must not exceed 10 MB in size. If the file exceeds this limit, compress it or split it into multiple skills. |
| Skill name | No | The system uses the name from skill.md by default. You can modify it. |
| Skill description | No | The system uses the description from skill.md by default. You can modify it. |
| Tag category | No | Select the category for the skill. Supported categories include Efficiency Tools, Data Analysis, Content Creation, Development Tools, and Others. |

iii. After the skill package upload completes, click **Create Skill**. The system enables the skill by default after you add it.
4. Enable or disable a skill.

**Note**

After you disable a skill, agents that have installed the skill can no longer call it. i. Find the target skill in the skill list and click the card to go to the skill details page. ii. Click **Enable** or **Disable** in the upper-right corner of the details page. iii. The system updates the status after you confirm the operation.
5. Delete a skill.

**Note**

You cannot delete built-in skills. Find the target skill in the skill list, click the card to go to the skill details page, click **Delete**, and then click **Confirm Delete** in the dialog box.
6. Update the version.
i. Click the target skill card in the skill list. ii. Click **Update Version** in the upper-right corner of the skill details page. iii. Upload the new version file in the update version dialog box. The system automatically performs a security scan and then completes the update. iv. Click **Start Update**.
7. View skill details.
i. Click the target skill card in the skill list. ii. Go to the skill details page to view the following information: Basic information: the name, category, description, version, and origin. Overview: the detailed configuration parameters of the skill. Files: the detailed file directory of the skill. Security: the security risk assessment details of the skill. Version history: the upgrade and evolution details of each version. Installed: the projects that have installed the skill. Click a project to view the associated agents.

**MCP**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Operation Center** > **Capabilities and Plugins**,
and then click the **MCP** tab. Go to the **MCP** page, where you can obtain the following information: View the number of enabled and disabled MCP servers. Use the search box to find a target MCP server. View the MCP list, which includes the name, description, server type, origin, and status.
3. Add an MCP server.
You can add an MCP server by using one of the following methods: manual configuration, JSON import, or AI Gateway automatic synchronization.

**Method 1: Manual configuration**

a. On the **MCP** page, click **Add MCP**. b. On the **Manual Configuration** tab, specify the following parameters:

| Parameter | Required | Description |
|---|---|---|

| Server type | Yes | Select the server type: SSE Streamable HTTP STDIO |
|---|---|---|
| Server name | Yes | Enter the server name. |
| Description | No | Optional. Enter a description. |
| Server endpoint | Yes | Enter the server endpoint, such as http://localhost:8080/sse. |
| Headers | No | Add headers directly. You can add multiple headers. Click Paste, paste headers in the Header:Value or Header=Value format with one header per line, and then click Parse. |
| Environment variables | No | Add environment variables. |
| Timeout period | No | Specify the timeout period for connections, tool list retrieval, and tool calls. The value ranges from 1 to 600 seconds. The default value is 30 seconds. |

c. Click **Add**. The system sets the status of the added server to **Enabled**.

**Method 2: JSON import**

a. On the **MCP** page, click **Add MCP**. b. In the Add MCP Server dialog box, click **JSON Import**. c. Paste the MCP server configuration JSON into the input box. d. Click **Import**. The system sets the status of the imported server to **Enabled**.

**Method 3: Gateway import**

After you import the AI Gateway, you can click **Synchronize Gateway** to allow the system to automatically import the **MCP configurations** associated with the AI Gateway. For more information, see Synchronize a gateway.
4. View MCP server details.
In the server list, click a server name to view the basic information, connection configuration, and tool list of the server: Basic information View the name, description, server type, status, origin, and timeout period of the server. Endpoint information View the endpoint details of the server. Tool list View the detailed tool names and descriptions.
5. Disable or enable an MCP server.
For a server whose status is **Enabled**, click the disable icon in the **Actions** column of the target server . For a server whose status is **Disabled**, click the enable icon in the **Actions** column of the target server .
6. Edit an MCP server.

**Note**

You cannot edit servers that were imported from the gateway. i. Click the edit icon in the Actions column of the target server to edit the **Description**,
**Server Endpoint**, **Headers**, and **Timeout Period** of the MCP server.
ii. Click **Next: Impact Confirmation**. iii. Confirm the impact scope, and then click **Confirm Save and Deploy**.
7. Delete an MCP server.
Click the delete icon in the **Actions** column of the target server , and then click **Delete** in the **Confirm Deletion** dialog box.

**Important**

This operation is irreversible. Proceed with caution.

**Plugin**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Operation Center** > **Capabilities and Plugins**,
and then click the **Plugin** tab. On the **Plugin** page, you can obtain the following information: View the total number of plugins, the number of enabled plugins, and the number of disabled and installed plugins. Use the search box to search for a target plugin by name. View plugin cards that display the plugin icon, name, description, version number, and status.
3. Upload a plugin.
i. On the **Plugin** page, click **Upload Plugin**. ii. In the dialog box, upload the plugin package and enter the plugin name, description, and version. After you upload the plugin package, the system automatically parses and registers the plugin. iii. Click **Upload**. After the upload succeeds, the plugin appears in the plugin list.
4. Manage plugin versions.
Click a target plugin card to go to the plugin details page, click **Update Version**, upload the new plugin package, and then click **Start Update**. The system automatically completes a security scan and then updates the plugin.
5. Install or uninstall a plugin on an agent.
On the agent details page, click the **Skills and Tools** tab, and then click the **Plugin** subtab:
**Install a plugin**: Click **Add Plugin**, select the target plugin, and then click **OK**.
**Uninstall a plugin**: Click the delete icon next to an installed plugin, and then confirm the
uninstallation.
6. Enable or disable a plugin.
In the plugin list, click a target plugin card to go to the plugin details page, and then click
**Disable** or **Enable** to disable or enable the plugin. After you disable a plugin, agents that
have the plugin installed cannot use the plugin features.
7. Delete a plugin.
In the plugin list, click a target plugin card to go to the plugin details page, click **Delete**, and then click **Confirm Deletion** in the dialog box.
```html ```
e history

## 6 Change history

This topic describes how to view the Ops change history of resources such as agents, skills, security rules, and MCPs, including batch changes, single changes, and change management operations.

**Scenarios**

After performing Ops operations such as restart, upgrade, scaling, and skill synchronization, you can view the execution status and results on the Change History page. The system generates a change history record for any operation that affects or modifies the agent runtime environment (POD) and its runtime dependencies, such as cloud resources and Kubernetes resources.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. You have obtained the tenant operations administrator role.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Change History**. On the **Operation History** page,
you can view the following information: Statistics cards: The top of the page displays five metrics: **Total Changes**, **Success**,
**Failed/Partial**, **Running**, and **Pending**.
Change record list: The system displays all change records in a table.
3. View operation details.
In the change record list, click the target change type to view the detailed history of the change. e history You can view detailed information such as **Basic Info**, **Change Target**, and **Execution**
**Logs**.
4. View the agent execution results for batch operations.
For batch operations, click the target change type. In the operation details drawer, you can view the **Execution Strategy** and the total number of agents. e history
5. Search for and filter operation records.
Enter the operator, change type, or change details in the search box to search directly. Use the filter box to filter records by agent, status, change type, or project. Use the **All Agents** drop-down list to filter change records by agent. Use the **All Statuses** drop-down list to filter change records by status. Use the **All Types** drop-down list to filter change records by change type. Use the **All Projects** drop-down list to filter change records by project.
6. Refresh data.
Click **Refresh** to manually refresh the data.

**Parameter description**

e history The operation record list contains the following fields:

| Module | Description |
|---|---|
| Basic Info | Basic information includes: Detailed information such as the operator, start time, end time, duration, and description. |
| Change Target | Detailed information such as the object type, related objects, and target objects. |
| Execution Strategy | Detailed information such as the batch dimension, pause strategy, and total batches of the strategy. |
| Execution Logs | The detailed execution steps of the change. |

ructure

## 7 Infrastructure

This topic describes the features and configurationss of the infrastructure module in the OpenTrek-Ops platform.

**Scenarios**

The infrastructure feature applies to the following scenarios: Manage the infrastructure services that agents depend on to ensure the stability of the agent runtime environment. Monitor the infrastructure status to promptly detect and troubleshoot service faults. Configure the connection parameters of the infrastructure to optimize service performance and resource utilization. Manage the integration and configuration of underlying services such as Large Language Model (LLM) Service, Redis, Object Storage Service (OSS), and PostgreSQL.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform as a tenant operations administrator.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Infrastructure** to go to the **Agent Infra** page.
This page provides the following information: View information such as the name and type of model services, Kubernetes clusters, AI gateways, agent platforms, and data storage infrastructure.
3. AI Gateway
Import a gateway a. On the **AI Gateway** tab, click **Import Gateway** and configure the following parameters:

| Parameter | Required | Description |
|---|---|---|
| AI Gateway Name | Yes | Select the gateway instance to import. |
| API Key | Yes | If required, contact Alibaba Cloud technical support to obtain the API key. |

ructure b. Click **Import**.

**Note**

If you import an ASCM AI gateway, the system automatically imports the **MCP**
**configuration** and **AI model configuration** associated with the AI gateway after
you click **Import**. You can view these configurations on the **MCP** page and the
**Infrastructure** > **Model Services** page.
View details Click the name of the target gateway to view detailed information such as **Basic**
**Information**, **Access Points**, **Model API**, and **MCP**.
Edit a gateway a. Click the edit icon in the **Actions** column of the target gateway, and then edit the
**API Key** in the **Edit AI Gateway** dialog box.
b. Click **Next: Impact Confirmation**. c. Verify the impact, and click **Confirm Update**. Otherwise, click **Back** to re-edit. Synchronize a gateway a. Click the synchronize icon in the **Actions** column of the target gateway, and then click **Synchronize**. b. Confirm the impact of this synchronization, and click **Confirm Sync**. The system pulls the latest model and MCP configurations from the cloud, overwrites the local data, and automatically pushes the configurations to the associated digital employees. Remove a gateway Click the remove icon in the **Actions** column of the target gateway, and then click
**Remove** in the dialog box.
4. Model Services
Add a model ructure a. On the **Model Services** tab, click **Add Model** and configure the following parameters:

| Parameter | Required | Description |
|---|---|---|
| Model ID | Yes | Enter the identifier used for model API calls, such as gpt-4-turbo. |
| Display Name | Yes | Enter the model name to display, such as GPT-4 Turbo. |
| Provider | Yes | Select amodel provider. The system currently supports Alibaba Cloud. |
| Protocol | Yes | Select a protocol. |
| Inference Type | Yes | Select Text Generation or Text Embedding. |
| API Key | Yes | If required, contact the Alibaba Cloud technical support to obtain the API key. |
| API Endpoint | Yes | Contact Alibaba Cloud technical support to obtain the API endpoint. |

b. Click **Confirm**. View model details. On the **Model Services** tab, view information about all models, such as the **Provider**,
**Inference Type**, **Protocol**, **Source**.
Click the name of the target model in the model list to view the **Basic Information**, source, and **Access Endpoint** of the model. Edit a model ructure

**Note**

Before you modify the infrastructure configuration, make sure that the modification does not affect running agent tasks. a. Click the edit icon in the **Actions** column of the target model. b. Edit the relevant parameters and click **Next: Impact Confirmation**. c. Verify the impact, and then click **Confirm & Apply**. Otherwise, click **Back to Edit** to re-edit. Remove a model a. Click the remove icon in the **Actions** column of the target model. b. In the pop-up dialog box click **Delete**.
5. Data Storage
On the **Data Storage** tab, click the name of an instance to view the **Basic Information** and **Access Endpoints** details of the instance.
6. K8S Cluster
Import a cluster ructure a. On the **K8S Cluster** tab, click **Import Cluster** and configure the following parameters.

| Parameter | Required | Description |
|---|---|---|
| Cluster Name | Yes | Enter a custom cluster name. |
| KubeConfig | Yes | Enter the cluster configuration in YAML format. |
| storageClassName | Yes | Select the StorageClass of the cluster for persistent storage. |
| ingressClassName | Yes | Select the Ingress type for agent domain name routing. |
| Wildcard Domain Support | Yes | The default value is Yes. After changing the wildcard DNS settings, you must restart running agents for the change to take effect. |
| Agent Service Endpoint | Yes | This endpoint serves as the root domain name for generating agent links. Configure a wildcard DNS record in the DNS console in advance. |

b. Click **Import**. Edit a cluster Click the edit icon in the **Actions** column of the target cluster to edit parameters such as the **Agent Service Endpoint**, **Access IP**, **ingressClassName**, **storageClassName**, and **KubeConfig**. After editing, click **Save**. Remove a cluster Click the remove icon in the **Actions** column of the target cluster, and then click
**Remove** in the pop-up dialog box.
7. Agent Platform
Add a platform ructure a. On the **Agent Platform** tab, click **Add Platform** and configure the following parameters:

| Parameter | Required | Description |
|---|---|---|
| Name | Yes | Enter a custom name of the platform, such as Alibaba Cloud Model Studio Enterprise Edition. |
| Type | Yes | Valid values: OpenTrek Dev and Dify. |
| AppKey | Yes | a. Log in to the Alibaba Cloud Model Studio console. In the left-side navigation pane, select Integration and Openness > APP KEY to _ obtain the AppKey value. b. The page displays the workspace identifier on the right side of the region section at the top. Note This parameter is required only when you select OpenTrek Dev as the type. |
| Workspace | Yes |   |
| Endpoint | Yes | Enter the endpoint, workspace ID, and admin API Key of Dify. Note This parameter is required only when you select Dify as the type. |
| Workspace ID | Yes |   |
| Admin API Key | Yes |   |
| ApiDomain | Yes | Enter the business gateway URL to converse with agents on the Alibaba Cloud Model Studio platform. Note This parameter is required only when you select OpenTrek Dev as the type. |

b. Click **Confirm**. Edit a platform Click the edit icon in the **Actions** column of the target platform to edit information such as the platform name. If you leave the AppKey field empty, the system retains the original value. After editing, click **Save**. Delete a platform Click the delete icon in the **Actions** column of the target platform, and then click
**Confirm**.
ructure

**Warning**

This operation is irreversible. Proceed with caution. ty center

## 8 Security center

### 8.1 Security settings

This topic describes how to configure security settings in the OpenTrek-Ops platformApsara Uni-Manager Operations Console, including the security overview, tool guardprotection rules, and file guardprotection policies.

**Prerequisites**

You have logged ion to the OpenTrek-Ops platform. You have obtained the system administrator role or a role with security configuration permissions.

**Security overview**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, selectchoose **Security Center > Security**
**SettingsSecurity Center > Security Settings** to go to. The system displays the
**Security Overview** page by default.
3. On the Security **Overview** tabpage, view the following information:
Blocked Today: the number of tool calls that the system blocked on the current day. Active Rules: the number of enabled security rules that are currently enabled. Blocking Trend: a trend chart that shows the number of recent blocksed calls over a recent period. The system displays data for the last 7 days by default. Risk Level Distribution: blocking statistics distributed by CRITICAL, HIGH, MEDIUM, LOW, and INFO levels. Top 5 Triggered Rule Hitss: the top 5 security rules with the highest number of hits.

**Tool guardprotection**

**View rules**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, selectchoose **Security Center > Security Settings**
**Security Center > Security Settings**, and then select **Tool GuardProtection**.
3. In the upper part of the page, you can configure security scanning for tool calls. Dangerous
operations require your explicit approval before execution.The system requires your explicit approval before it executes high-risk operations. Enable: This option eenables all security rules for the tenant. After you enable this option, the system blocks calls to dangeroushigh-risk tools. Disable: This option disables all security rules for the tenant. After you disable this option, the system does not block calls to dangeroushigh-risk tools.
4. In the lower part of the page, you can view the list of **Global Rules** or **Agent Rules** list.
You can also filter target rules by a combination of rule ID, description, level, and agent to find the target rule.

| Category | Parameter | Description |
|---|---|---|

ty center

| Global Rrules | Rule | The ID of the security rule. |
|---|---|---|
|   | SeverityLevel | The severity level of the security rule. CRITICAL: Severemajor HIGH: Hhigh MEDIUM: Mmedium LOW: Llow INFO: Iinformation |
|   | Type | The type of the security rule. Built-in Custom |
|   | Description | The description of the security rule. |
|   | PMatch patterns | The match patterns of the security rule. |
|   | Synchronization Sstatus | The synchronization status of the security rule. |
|   | Actions | You can enable or disable the security rule. |
| Agent Rrules | Rule | The ID of the agent rule. |
|   | SeverityLevel | The severity level of the agent rule. |
|   | Description | The description of the agent rule. |
|   | PMatch patterns | The match patterns of the agent rule. |
|   | Agent | The agent. |
|   | Project | The project to which the agent rule belongs. |
|   | Synchronization Sstatus | The synchronization status of the agent rule. |

5. Click the name of the target rule to go to the rule details page and view its detailed
information about the rule, including basic information, severity levelthreat categories, match patterns, and hit statistics. ty center

**Add a rule**

**Note**

TFor more information about how to add an agent rules, see Agent list.
1. Click **Add Rule**.
2. Configure the following parameters and click **Add**.

| Parameter | Description |
|---|---|
| Alert Rule ID | Enter the ID of the security rule. |
| Tool Llist | Select a tool category. Shell Execution File Read File Write/Edit Code Search Web Access Browser Image View Screen Capture File Transfer All Tools |
| Parameter Llist | After you select a tool category, the system automatically fills inpopulates the parameters. If you leave this field empty, the rule matches all parameters. |

ty center

| Category | Select athe category of the security rule. Command Iinjection Data Exfiltrationtheft Path Directory Traversal Sensitive File Access Network Abuse Credential Exposure Resource Abuse Prompt Injection Code Execution Privilege Escalation Sensitive file accessPrivilege escalation Network abuse AccessKey Pair exposure Resource abuse Prompt injection Code Execution |
|---|---|
| Severity level | Select the severity level of the security rule. CRITICAL: Severecritical HIGH: Hhigh MEDIUM: Mmedium LOW: Llow INFO: Iinformation |
| Regex Ppatterns | Enter the regex pattern forof the security rule. |
| Exclusion Ppatterns | Enter the exclusion pattern forof the security rule. |
| Description | Enter thea description of the security rule. |
| Remediation suggestion | Enter a remediation suggestion for the security rule. |

ty center

**Enable a rule**

1. Click the switch in the **Actions** column of the target security rule.
2. In the pop-up dialog box that appears, click **ConfirmOK**.

**Note**

When eanbledAfter you enable the rule, the rule participates in blocksing tool calls.

**Disable a rule**

1. Click the switch in the **Actions** column of the target security rule.
2. In the pop-up dialog box that appears, click **ConfirmOK**.

**Note**

WhenAfter you disabled the rule, the rule no longer blocks any tool calls. ty center

**File guardprotection**

**Add a path**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Security Center > Security Settings**choose
**Security Center > Security Settings**, and then select **File GuardProtection**.
3. Click **Add Path**, configure the following parameters, and then click **Add**.

| Parameter | Description |
|---|---|
| Path | The path of the configuration file. |
| Rule Ttype | The access control policy for the configuration file path. The following two policy types are available: Extra Grant: Grants access permissions to the specified file path.Additional authorization: grants access permissions to the specified object path. Permanent Deny: Denies access to the specified file path.Permanent block: blocks access to the specified object path. |
| Description | A brief description of the access policy for this path. |

**Edit a path**

1. Click the edit icon in the **Actions** column of the target protection path.
2. Modify the **Path**, **Rule Type**, and **Description** of the protection path.
3. Click **Save**.

**Delete a path**

Click the delete icon in the **Actions** column of the target protection path to delete the path.

**Enable a path**

1. Click the switch in the **Actions** column of the target protection path.
2. In the pop-up dialog box that appears, click **ConfirmOK**.

**Disable a path**

1. Click the switch in the **Actions** column of the target protection path.
2. In the pop-up dialog box that appears, click **ConfirmOK**.
```html ```

### 8.2 Audit logs

The system tracks key operations in real time, focusing on high-risk events and compliance remediation progress.

**Prerequisites**

ty center You have logged in to the OpenTrek-Ops platform. You have the system administrator role or a role with audit log permissions. You have enabled the tool guard feature in **Security Settings**.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Security Center > Audit Logs**.
3. You can filter audit logs by keyword, severity, decision, and project above the list.
4. View the audit log list. The following table describes some parameters.

| Parameter | Description |
|---|---|
| Event ID | The ID of the event. |
| Project | The project to which the agent belongs. |
| Agent | The name of the agent. |
| Tool Name | The tool category of the security rule. |
| Tool Parameters | The tool parameter of the security rule. |
| Rule ID | The ID of the security rule. Click the rule name to view the rule details. |
| Severity | The severity level of the security rule: CRITICAL: Major HIGH: High MEDIUM: Medium LOW: Low INFO: Information |
| Decision | The decision result of the security rule: ALLOW: Allow DENY: Deny TIMEOUT: Timeout |
| Decision By | The decision maker of the security rule: USER: User SYSTEM: System |

ty center

| Time | The time of the audit log. |
|---|---|
| Actions | Click Details to view the audit log details. |

5. Click **Export** in the upper-right corner of the audit log list to download the audit logs to
your local computer. n analysis

## 9 Session analysis

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. You have the system administrator role or a role with session analysis permissions.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Session Analysis**.
3. On the **Session Analysis** page, view the following information:
Search for sessions by session ID. Filter sessions by agent. Query sessions by filtering time or specifying a custom time range.
4. Click a session name or session ID to view details such as the session name, session ID,
start time, entry agent, project, session duration, turns, total tokens, input tokens, output tokens, trace list, and session messages. In the trace list, click a trace ID to view the trace details. el exploration

## 10 UModel exploration

UModel exploration is a visual exploration tool designed for model governance and data asset management scenarios. It provides a unified view of model entities and their associations in the system, transforms scattered and abstract metadata into interactive visual graphs, and helps users quickly understand the system architecture, data asset distribution, and entity dependencies.

**Prerequisites**

You have logged in to the OpenTrek-Ops console. You have the system administrator role or a role with UModel exploration permissions.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **UModel Exploration**.
3. On the **UModel Explorer** page, viewn the following information:
The total number of nodes and connections. The statistics grouped by type or region. The option to switch between the **Graph view** and the **Table view** in the upper-left corner. The zoom and full-screen options for the topology in the lower-left corner.
4. Click any node in the topology, and a dialog box displays the detailed information of the
node in a form or JSON format. tional analysis

## 11 Operational analysis

### 11.1 Cost analysis

This topic describes how to view multi-dimensional statistics of token consumption in the OpenTrek-Ops platform. This feature enables transparent management of computing power costs.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. You have the system administrator role or a role with operations analysis permissions. An agent runs in the OpenTrek-Ops platform and generates token consumption data.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Operations Analysis > Cost Analysis**.
3. Select a target time range in the upper-right corner.
Last 24 hours (default) Last 7 days This month Custom
4. View the following information at the top of the page.

| Section | Description |
|---|---|
| Total Tokens | Displays the total, input, and output token consumption within the target time range. |
| Calls | Displays the number of model calls within the target time range. |
| Token Trend | Displays a trend chart of token consumption within the target time range, including total, input, and output data. Move the pointer over a node to view the data at the corresponding time. |
| Total Tokens by Model | Displays the total number of tokens and the consumption proportion of each model within the target time range. |

tional analysis
5. View detailed data by the following dimensions at the bottom of the page.

| Dimension | Description |
|---|---|
| Model dimension | Collects token consumption data by model. You can filter the data by model name. Click a model name to view the total tokens, input tokens, output tokens, calls, and token trend chart of the model. |
| Project dimension | Collects token consumption data by project. You can filter the data by project name. Click a project name to view the total tokens, input tokens, output tokens, calls, token trend chart, model distribution, and agent distribution of the project. |
| Agent dimension | Collects token consumption data by agent. You can filter the data by project name and agent name. Click an agent name to view the total tokens, input tokens, output tokens, calls, token trend chart, and model distribution of the agent. |
| User dimension | Collects token consumption data by user. You can filter the data by user name. Click a user name to view the total tokens, input tokens, output tokens, calls, token trend chart, model distribution, and agent distribution of the user. |

m settings

## 12 System settings

This section describes the features and configuration methods of the system settings modules in the OpenTrek-Ops platform, including tenant management and platform management.

**Important**

Log in as the system administrator to configure system settings.

### 12.1 Tenant management

This topic describes how to manage tenants in the OpenTrek-Ops platform.

**Scenarios**

The tenant management feature applies to the following scenarios: Isolate resources and manage permissions in multi-tenancy environments to ensure independence among tenants. Create dedicated tenants for different departments or business units to implement hierarchical management. Manage the lifecycle of tenants, including creation, activation, deactivation, and deletion. Configure the connection between tenants and the cloud platform to enable unified resource scheduling.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. You have obtained the system administrator permissions.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **System Settings > Tenant Settings**. On the
**Tenant Management** page, you can view the tenant list, which contains the following
fields:

| Field | Description |
|---|---|
| Tenant Name | The display name and identifier of the tenant. |
| Associated Organization | The name of the organization associated with the tenant. |
| Created At | The creation date of the tenant. |
| Actions | You can edit and delete the tenant. |

3. Add a tenant.
i. On the **Tenant Management** page, click **Add Tenant**. m settings ii. Fill in the following information in the pop-up dialog box:

| Parameter | Required | Description |
|---|---|---|
| Tenant Name | Yes | The display name of the tenant. |
| Tenant Code | Yes | The unique identifier of the tenant. It supports only letters, digits, and hyphens. |
| Description | No | The description of the tenant. |
| Select Organization | Yes | Select the associated organizations. You can select any level-2 organization under the same level-1 organization, but cannot select organizations across different level-1 organizations. |
| Specify Administrator | Yes | The administrator of the tenant. |

iii. Click **Confirm Create** to complete the creation.
4. Edit a tenant.
i. Find the target tenant in the tenant list. ii. Click the edit icon in the **Actions** column to modify the tenant name, description, organization, and other configuration information. iii. Click **Save Changes** to update the tenant.
5. Delete a tenant.

**Warning**

Deleting a tenant is a high-risk operation. Proceed with caution. You cannot recover any data under this tenant after deletion. i. Find the target tenant in the tenant list. ii. Click the delete icon in the **Actions** column. iii. In the confirmation dialog box, click **Confirm Delete**. The system removes the tenant from the list after a successful deletion.

**Next steps**

Log in as the administrator of the newly created tenant to perform initial tenant configuration, including registering model services and importing Kubernetes clusters. For more information, see Infrastructure.

**Note**

When you log in for the first time, the system prompts you to initialize the password. Follow the prompts to set a new password and keep it secure. m settings

### 12.2 Configuration management

This topic describes how to manage channels, system configurations, and data subscriptions in the OpenTrek-Ops platform.

**Scenarios**

The cloud platform management feature applies to the following scenarios: Configure and manage cloud platform resources and notification channels connected to the OpenTrek-Ops platform, and configure the push targets for agent running status and alert messages. Achieve unified management and resource scheduling in a multi-cloud platform environment. Push O&M messages in real time to ensure that O&M personnel receive critical information promptly. Configure multiple notification channels, such as DingTalk and WeChat, to meet notification requirements in different scenarios. Manage cloud platform connection information and authentication credentials to ensure stable data interoperability.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform. The logged-in user has obtained the management permission for the platform.

**Channel management**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **System Settings > Configuration Management**.
3. On the **Configuration** page, select **Channel Management**.
On the **Channel Management** page, view the list of configured channels.
4. Enable a channel.
Click the switch in the upper-right corner of the target channel card to enable the channel. After you turn on the switch, the status changes to **Enabled**.

**System configuration**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **System Settings > Configuration Management**.
3. On the **Configuration** page, select **System Configuration** to modify the preset
configuration items of the system. ProCode Runtime Configuration Click the edit icon in the **Actions** column to modify the available runtimes for the procode agent, and then click **Save**. Skill Package Size Click the edit icon in the **Actions** column to modify the configuration value, and then click **Save**. m settings

**Note**

The modifications take effect immediately for all tenants. Adjust the size with caution and prevent an excessively oversized skill pack from affecting the loading performance. Agent Console Hide Sidebar Click the edit icon in the **Actions** column to modify the configuration value, and then click **Save**. Deployment Features Configuration Click the edit icon in the **Actions** column to modify the global parameters for the platform deployment mode, and then click **Save & Apply**.

**Note**

Modifying the deployment mode configuration triggers a hot update. All changes take effect immediately without restart. AI Assistant Model Config

**Note**

The model configuration affects all intelligent assistant instances. Modifications take effect within the next synchronization cycle. a. Click the edit icon in the **Actions** column. b. Click **Add LLM Config**, configure the parameters, and then click **Save**. Default Cluster Config Click the edit icon in the **Actions** column to enter the cluster configurations. If you enable the default cluster, the system automatically imports this cluster when you create a new tenant. After editing, click **Save**.

**Data subscription**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **System Settings > Configuration Management**.
3. On the **Configuration** page, select **Data Subscription**, click **Add Subscription** to go to
the SLS data configuration page, and then configure the following parameters. The data subscription feature exports platform runtime data to Simple Log Service (SLS) for subsequent data analysis and monitoring.

| Parameter | Description |
|---|---|
| Subscription Name | Enter a custom subscription name. |
| SLS Type | Select Private Cloud SLS. |

m settings

| SLS Project | Log in to the SLS console and view the name of the project to configure. |
|---|---|
| SLS LogStore | Log in to the SLS console, click the project name to go to the details page, and then view the LogStore name. |

4. Click **Create**.
ure an Ops administrator

## 13 Configure an Ops administrator

**administrator**

This topic describes how to configure an Ops administrator.

**Prerequisites**

You have logged in to the OpenTrek-Ops platform as a tenant administrator.

**Procedure**

1. Log in to the OpenTrek-Ops platform.
2. In the lower part of the left-side menu, click
on the right side of the current login account and select **Current Tenant**. You can switch tenants. The system isolates resources for different tenants to ensure independence among tenants.
3. Configure tenant settings.
In the tenant switching dialog box, click the settings button for the target tenant. Enter the specified administrator in the input box and authorize the user as the Ops administrator of the current tenant.

**Note**

Ensure that the tenant administrator has added the organization of the selected user to the platform. Click **Confirm Authorization**, and then click **Back** in the upper-right corner of the page.

## 14 FAQ

**Login issues**

**What can I do if I forget my password?**

A: Contact the system administrator to reset the password.

**What do I do if the page is abnormal after I log on to the console?**

A: Please clear the browser cache and log on again, or try to use Chrome browser.

**Agent-related issues**

**Q: Can I not find the required type when I create the agent?**

A: Contact the administrator to check whether the corresponding Agent type plug-in has been installed.

**Q: Why does the Agent fail to start?**

A: Check whether the configuration of the agent is complete and whether the dependent infrastructure services are running properly.

**Skills Related Questions**

**What can I do if a skill cannot be used by agents after it is created?**

A: Make sure that the skill is enabled and the agent has the skill installed.
