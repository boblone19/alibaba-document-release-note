---
title: "OpenTrek-Ops User Guide 20260630"
product_version: "V3.18.6"
pdf_pages: 39
source_pdf: "a5de1b840e361908_Alibaba Cloud Apsara Stack V3.18.6 OpenTrek-Ops  User Guide 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/OpenTrek-Ops/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20OpenTrek-Ops%20%20User%20Guide%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# OpenTrek-Ops User Guide 20260630

## Table of Contents

- 1 Overview
- 2 Log in to the OpenTrek-Ops platform
- 3 Operation overview
- 4 Operation Center
  - 4.1 Agent management
  - 4.2 Agent team
  - 4.3 Operation history
- 5 Asset Center
  - 5.1 Skills
  - 5.2 MCP
  - 5.3 Agent Infra
- 6 System Settings
  - 6.1 Organization management
  - 6.2 Platform management
- 7 Multi-tenant management
- 8 AI Assistant
- 9 FAQ

ew

## 1 Overview

This topic describes the features and usage of the OpenTrek-Ops platform. OpenTrek-Ops is a multi-agent operations and governance platform based on the xClaw, providing full lifecycle management capabilities for enterprise-grade AI agents. The platform delivers an all-in-one solution for operations teams by focusing on agent creation, deployment, monitoring, collaboration, and governance.

**Product architecture**

OpenTrek-Ops divides operations management into three layers: agent operations, skill asset operations, and infrastructure operations. The platform accumulates operations experience and collects data across these three layers. It then aggregates the operations data into a unified governance center to perform integrated analysis and comprehensive processing. OpenTrek-Ops provides a unified operations portal and a single operations entry point to deliver a consistent operations experience for users. The platform integrates with various infrastructure services, including LLM Service, Redis, OSS, and PostgreSQL. It also exposes data from the operations system to third-party systems through APIs.

**Scenarios**

OpenTrek-Ops applies to the following scenarios:
**AI operations automation**: The platform automates the execution of operational tasks
through agents to reduce manual operation costs.
**Multi-agent collaboration**: Users build agent teams to enable multi-role collaboration in
complex operations scenarios.
**Skill asset management**: The platform manages, reviews, and distributes agent skills in
a unified manner to enable capability reuse.
**Ops governance**: OpenTrek-Ops comprehensively monitors agent running status, token
consumption, and error rates. You have obtained the access URL, username, and password of the OpenTrek-Ops platform from the administrator. We recommend that you use the Chrome browser.

**User roles**

User roles provide different operation permissions for different users. The system creates the system administrator, tenant administrator, and regular user roles by default during initialization. The permissions are as follows:

| Role | Permission description |
|---|---|
| System administrator | Manages the Ops operations of the platform, including agent management, agent team management, skill management, and tenant management. |
| Tenant administrator | Manages agents and skills within the scope of the affiliated tenant. |
| Regular user | Performs basic operations such as creating agents and using skills. |

| OpenTrek-Ops User Guide·Over w | vi |
|---|---|

to the OpenTrek-Ops platform

## 2 Log in to the OpenTrek-Ops platform

**platform**

**Log in and log out**

This topic describes how users log in to and log out of the OpenTrek-Ops platform.

**Scenarios**

Logging in and logging out are basic operations for using the OpenTrek-Ops platform, applicable to the following scenarios: Ops personnel access the platform daily to perform routine operations. Administrators configure and manage the system. Users securely log out of the system after completing their operations. You have obtained the endpoint, username, and password of the OpenTrek-Ops platform from the administrator. The administrator provides the endpoint of the OpenTrek-Ops platform. We recommend that you use the Chrome browser.
1. Open a browser.
2. In the address bar, enter the endpoint of the OpenTrek-Ops platform and press Enter.
3. Enter the correct username and password.

> **Note:** Obtain the username and password for logging in to the OpenTrek-Ops platform from the administrator.
> If you enter an incorrect password multiple times in a row, the system enables the verification code login feature. If the number of consecutive incorrect attempts reaches the upper limit, the system locks the account. Contact the administrator to unlock the account.
> When you log in to the OpenTrek-Ops platform for the first time, the system may require you to change the initial password. Follow the prompts to change the password. To improve security, the password must meet the following requirements:
> The password must contain uppercase and lowercase English letters.
> The password must contain Arabic numerals (0 to 9).
> The password must contain special characters.
> The password must be 10 to 20 characters in length.

4. Click **Log In**.

**Log out of the system**

1. In the upper-left corner of the page, click the username.
to the OpenTrek-Ops platform
2. In the dialog box, click **Sign Out**.
tion overview

## 3 Operation overview

This topic describes the features and metrics of the Overview page in the OpenTrek-Ops platform.

**Scenarios**

Operation Overview is the homepage dashboard of the platform, applicable to the following scenarios: Perform daily operations inspections to quickly understand the overall health status of the platform. Monitor the running trends of agents and token consumption to evaluate resource usage efficiency. View model performance metrics to analyze the response time and processing capacity of different models. Monitor the infrastructure status to promptly discover and troubleshoot service exceptions. You have logged in to the OpenTrek-Ops platform as a tenant administrator.
1. Log in to the OpenTrek-Ops platform.
After a successful login, the system directs you to the **Overview** page by default.
2. On the **Overview** page, you can view the following core modules:

| Module name | Description |
|---|---|

tion overview

| Team Overview | Displays the statistics on the number of teams and agents. Today's Top 5 Active Teams Displays a list of the top five teams by activity. |
|---|---|
| Weekly Activity Trend | Displays the activity trend over the last seven days. |
| Model Performance | Displays the TTFT P99 and TPOT P99 performance metrics for each model. |
| Cloud Products | Displays the number of instances for API Gateway, Object Storage Service (OSS), PolarDB, and Alibaba Cloud Container Service for Kubernetes (ACK). |
| Token Trend | Displays the time trend of token consumption in a line chart. When you move the pointer over the line chart, the system displays the total token data for the corresponding point in time. |
| Model Token Distribution | Displays the token usage distribution of different models. |
| Infrastructure | Displays the utilization of CPU, memory, and storage. |
| Central dashboard | Displays the running status of infrastructure such as ACK, LLM Service, Redis, OSS, and PG. Blue indicates that the service is normal. Today's Tokens Displays the total token consumption for the current day. Active Teams Today Displays the number of active teams for the current day. Active Agents Today Displays the number of active agents for the current day. Error Rate Displays the error rate metric for current requests. Peak QPS Today Displays the peak QPS for the current day. |

**Next steps**

After obtaining the operation overview information as required, you can use agent management to view and manage the details of agents. tion Center

## 4 Operation Center

### 4.1 Agent management

This topic describes how to manage agents in the OpenTrek-Ops platform. You can create, view, edit, start, stop, scale, and delete agents.

**Scenarios**

Agent management is a core feature of the platform, applicable to the following scenarios: Create new operations agents to automate specific operational tasks. Manage the configuration and running status of existing agents to ensure that the agents run normally. Allocate and manage agent resources for different teams to optimize resource allocation. View agent execution records to analyze agent performance and troubleshoot issues. You have logged in to the OpenTrek-Ops platform. You have the tenant administrator role or a role with agent creation permissions.
1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, select **Ops Center** > **Agent Management**.
On the **Agent Management** page, you can obtain the following information: View the total number of agents. Use the search box to search for a target agent by agent name. Use the **All Creators** drop-down list to filter the agent list by creator. Use the **All Statuses** drop-down list to filter the agent list by status. Use the **All Teams** drop-down list to filter the agent list by team. Click the view switch button to switch between the grid view and the list view. Click the refresh button to refresh the agent list data. View agent cards, which display information such as the agent icon, name, type label, team, creator, and running status.
3. Create an agent.
i. On the **Agent Management** page, click the **Create Agent** button. ii. In the creation form that appears, fill in the following information:

| Module | Parameter | Required | Description |
|---|---|---|---|
|   | Name | Yes | The display name of the agent. We recommend that you use a meaningful name. |

| Trek-Ops User enter |   |   |   |
|---|---|---|---|
| Basic Info |   |   |   |
|   | Type | Yes | Select an agent type. The system supports two types: QwenPaw and OpenCL. |
|   | Team | Yes | The team to which the agent belongs. |
|   | Description | No | The feature description of the agent. |
|   | Edition | Yes | Select the professional or the standard edition. The professional edition provides comprehensive capabilities, including powerful memory services, scaling, and full-stack observability. The standard edition provides limited capabilities. This edition supports basic operations features and does not ensure high availability. |
| Persona | Persona | No | The persona traits. |
|   | Behavior Boundary | No | The behavior boundaries. |
| Skill Configurati on | / | No | Click Add Skill. After you select a skill, click Confirm. Note Before you add a skill, make sure that you created the skill on the Assets > Skills tab. |
| Channel Settings | / | No | Enable DingTalk or DingTalk Hybrid. Note Before you configure channels, make sure that you enabled the channel in System Settings > Channel Management. |

iii. After you fill in the information, click the **Create** button. After creation, the system displays the new agent in the agent list.
4. View agent details.
tion Center On the **Agent Management** page, find and click the card of the target agent to go to the agent details page. On the agent details page, you can view the following information: Basic Info: name, type, description, and creation time. Running status: running or stopped. Configuration information: operation configuration parameters of the agent, such as the overview, persona, skills, MCP, cloud resources, channels, metrics, trace, and topology. Operational logs: historical execution records of the agent. You can view historical tasks and logs.

**Related operations**

| Operation type | Procedure |
|---|---|
| Edit an agent | 1. Find the target agent in the agent list. 2. Click the agent card to go to the agent details page. 3. In the Basic Info section, edit Primary Model as needed. 4. In the lower part of the details page, click theP ersona, Skills, and Channels tabs to edit the related information. |
| Start or stop an agent | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Start or Stop. 3. After you confirm the operation, the system updates the agent status. |
| Restart an agent | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Restart. 3. After you confirm the operation, the system updates the agent status. |
| Delete an agent | Note Before you delete an agent, make sure that the agent is in the stopped status. 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Delete. 3. In the confirmation dialog box that appears, click Delete. 4. After deletion, the system removes the agent from the list. |

tion Center

| Scale an agent | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Scale. 3. In the Adjust Resources dialog box, preview the current configuration information, and then configure the CPU and memory. 4. Click Apply. During the scaling process, the agent status changes to Changing. You can view the scaling task details on theO peration History page. |
|---|---|
| Update an agent | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickM ore, and then select Update to upgrade the agent. Note When the agent image is the latest version, the system dims and disables the Update button. |
| Chat with an agent | 1. Find the target agent in the agent list and click the agent card to go to the details page. 2. In the upper-right corner of the details page, clickC hat to go to the OpenClaw Chat page. Note For more information, see the OpenClaw guide. |

**Next steps**

After creating an agent, you can add the agent to an agent team for collaboration.

### 4.2 Agent team

This topic describes how to manage agent teams in the OpenTrek-Ops platform. You can create teams and manage team members.

**Scenarios**

The agent team feature applies to the following scenarios: Build a multi-role operations team to enable seamless collaboration on complex operational tasks. Manage the team member agents and permissions to ensure effective management of team members. Coordinate task assignment for agents within the team to improve team collaboration efficiency. Form a dedicated operations team for a specific project or business scenario. tion Center You have logged in to the OpenTrek-Ops platform. You obtained the tenant administrator role or a role with the permission to create agent teams.
1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Ops Center** > **Agent Team**.
On the **Agent Team** page, you can obtain the following information: Use the search box to search for a target team by team name. Click the **Create Team** button to create an agent team. View a team card, which displays information such as the team name, the number of members, and the creator. Click a team card to go to the team details page and view the member list.
3. Create a team.
i. On the **Agent Team** page, click the **Create Team** button. tion Center ii. Fill in the following information in the creation form that appears:

| Parameter | Required | Description |
|---|---|---|
| Team Name | Yes | The display name of the team. We recommend that you enter a meaningful name. |
| Description | No | The responsibilities and goals of the team. |
| Organization | Yes | The organization to which the team belongs. |
| K8S Cluster | No | Select a Kubernetes cluster. |
| Model Service | Yes | Select at least one text generation model. |
| Runtime Storage | Yes | This feature is enabled by default. |
| Memory Service | No | This feature is disabled by default. If you enable this feature, select at least one text vectorization model. |
| Team Member Settings | No | Configure the Team Admin and Team Members. Team Admin: This role has full management permissions for the team, including members, resources, and configurations. Team Members: This role can use resources such as agents, skills, and tools under the team. |

iii. Click the **Create Team** button to complete the creation.
4. Manage team members.
i. Add a member: a. Click **Enter** in the lower-right corner of the target team card to go to the details page. b. On the **Agent** tab, click **Create Agent**. You can refer to Agent management to add an agent. c. Click **Create** to complete the addition. ii. Remove a member: a. Find the target agent in the team member list. b. Click the icon in the **Operation** column of the member to complete the operation.
5. Add a skill.
On the team details page, click the **Skills** tab and click **Add Skill**. Select a skill and click
**Confirm** to add the skill to the team.
6. Add an MCP server.
tion Center On the team details page, click the **MCP** tab and click **Add MCP**. Select an MCP service and click **Add to Team** to add the MCP server to the team.
7. Add a cloud resource.
On the team details page, click the **Cloud Resource** tab. On the **Model Services** tab, click
**Add Resource**. Select a model and click **Save** to bind the model to the team.
8. Perform trace analysis.
On the team details page, click the **Trace Analysis** tab to view all trace records under the team. Click a trace ID to view the details.

**Related operations**

**Edit a team**

1. On the **Agent Team** page, select the target team and click **Enter** in the lower-right corner
of the team card.
2. Click **Edit** in the upper-right corner of the page to edit the **Team Name**, **Description**,
**Model Service**, and **Team Members**.
3. Click **Save**.

**Delete a team**

> **Note:** Before you delete a team, make sure that you clean up all agents under the team.

1. On the **Agent Team** page, select the target team and click **Enter** in the lower-right corner
of the team card.
2. Click **Delete** in the upper-right corner of the page, and then click **Confirm Delete**.

> **Warning:** The delete operation is irreversible. Proceed with caution.

**Batch operations**

1. On the **Agent Team** page, select the target team and click **Enter** in the lower-right corner
of the team card.
2. Click **Batch Operations** in the upper-right corner of the page.
Agent operations tion Center a. In the batch operation dialog box, select **Agent Ops**, and then select a specific operation.

| Operation type | Detailed steps |
|---|---|
| Update agent version | a. Select Update Agent Version. b. Select the runtime and version. |
| Resize specification | a. Select Resize Spec. b. Set the target specification. You can select a recommended specification or customize a specification. |
| Restart | Select Restart. |
| Start | Select Start. |
| Stop | Select Stop. |
| Go offline | Select Offline. |

b. Click **Select Agent**. In the **Select Agent** dialog box, select the agents and click
**Confirm Selection**.
c. Select the execution mode. Full Execution The system executes the operation on all agents simultaneously. Batch Execution Set the number of batches. The system executes the operation in batches. d. Click **Confirm**. The interface indicates that the system submitted the batch operation. You can view the batch operation details on the **Operation History** page. Skill operations a. In the batch operation dialog box, select **Skill Ops**. b. Select a specific operation. The system supports batch **Sync Skill**, **Disable Skill**, and
**Remove Skill**.
c. Select the skills to execute. d. Click **Select Agent**. In the **Select Agent** dialog box, select the agents and click
**Confirm Selection**.
e. Select the execution mode. Full Execution The system executes the operation on all agents simultaneously. Batch Execution Set the number of batches. The system executes the operation in batches. tion Center f. Click **Confirm**. The interface indicates that the system submitted the batch operation. You can view the batch operation details on the **Operation History** page. Configuration update a. In the batch operation dialog box, select **Config Update**. b. Select **Update Model**. c. Select the target model. d. Click **Select Agent**. In the **Select Agent** dialog box, select the agents and click
**Confirm Selection**.
e. Select the execution mode. Full Execution The system executes the operation on all agents simultaneously. Batch Execution Set the number of batches. The system executes the operation in batches. f. Click **Confirm**. The interface indicates that the system submitted the batch operation. You can view the batch operation details on the **Operation History** page.

**Next steps**

After creating a team, you can assign skills to the team to enable team collaboration.

### 4.3 Operation history

This topic describes how to view the operation history of agents and teams.

**Scenarios**

After performing Ops operations on agents, such as restart, upgrade, scaling, and skill synchronization, you can view the execution status and results on the Operation History page. You have logged in to the OpenTrek-Ops platform. You have the tenant administrator role or a role with the permission to create agent teams.
1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Ops Center** > **Change History** to go to the
**Operation History** page.
3. On the **Operation History** page, you can view the following information:
Statistics cards: The top of the page displays four statistical metrics: **Total Changes**,
**Success** operations, **Failed/Partial** operations, and **Running** operations.
Operation record list: The system displays all operation records in a table.
4. View operation details.
In the operation record list, click the operation type in the target row to view the detailed history of the operation. tion Center You can view the operation details, start time, end time, target team, target agent, and batch policy.
5. View the agent execution results of batch operations.
For batch operations, you can view the **Batch policy** and the total number of agents in the operation details drawer.
6. Search for and filter operation records.
Use the search box to search for records by operator, operation type, or operation details. Use the filter box to filter records by status, operation type, team name, or agent name.
7. Refresh data.
Click **Refresh** to manually trigger a data refresh.

**Parameter description**

The operation record list contains the following fields:

| Field | Description |
|---|---|
| Change Type | The system displays the icon and Chinese label of the operation type, with different colors for different types. |
| Operator | The name of the user who performed the operation. |
| Target Team | The list of target teams. |
| Target Agent | The list of target agents. |
| Status | The execution status of the operation, including Success, Failed, Running, and Pending. |
| Time | The timestamp when the operation started. |
| Duration | The execution duration of the operation. The system dynamically updates the duration for running operations. |

Center

## 5 Asset Center

### 5.1 Skills

This topic describes how to manage skills in the OpenTrek-Ops platform. The operations include creating, enabling, disabling, and viewing skills.

**Scenarios**

The skill management feature applies to the following scenarios: Manage and publish skills for agents in a unified manner to standardize capabilities. Review the security and compliance of skills to ensure skill quality. Encapsulate common capabilities into skills for multiple agents to reuse, improving development efficiency. Manage the version and lifecycle of skills to achieve continuous iteration and optimization. You have logged in to the OpenTrek-Ops platform. You have the tenant administrator role or a role with the skill creation permission.
1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Asses**>**Skills**.
On the **Skills** page, you can obtain the following information: View the total number of skills, the number of enabled skills, the number of disabled skills, and the total number of installations. Use the search box to search for a target skill by skill name. Use the category filter to filter skills by All, Efficiency Tools, Data Analysis, Content Creation, Development Tools, or Other. Click **Create Skill** to create a new skill. Center View skill cards. which display information such as the skill icon, name, description, version number, update time, and enablement status.
3. Create a skill.

> **Note:** The system provides the following built-in skills: Word/DOCX, PDF, ADL_memory, Excel/XLSX, agent-browser, Skill Builder/Creator, and PowerPoint/PPTX. It also supports custom skill creation.

i. On the **Skills** page, click **Create Skill**. ii. Fill in the following information in the creation form:

| Parameter | Required | Description |
|---|---|---|
| Upload Skill Package | Yes | Upload a prepared skill package. The package must be a .zip file that contains a skill.md file in the root directory. The skill.md file must include the name and description in YAML format. Important The size of a single skill file cannot exceed 10 MB. If the file exceeds this limit, compress the file or split it into multiple skills. |
| Skill Name | No | The system uses the name in the skill.md file by default. You can modify the name. |
| Skill Description | No | The system uses the description in the skill.md file by default. You can modify the description. |
| Tags | No | Select a category for the skill. The system supports Efficiency Tools, Data Analysis, Content Creation, Development Tools, and Other. |

iii. After the system uploads the skill package, click **Create Skill**.
4. Enable or disable a skill.

> **Note:** If you disable a skill, agents that have installed it cannot call it anymore.

i. Find the target skill in the skill list and click the card to go to the skill details page. ii. Click **Enable** or **Disable** in the upper-right corner of the details page. iii. The system updates the status after you confirm the operation.
5. Delete a skill.
Center

> **Note:** You cannot delete system built-in skills.

Find the target skill in the skill list and click the card to go to the skill details page. Click
**Delete**, and then click **Confirm Delete** in the dialog box.
Or click the **Delete** icon in the upper-right corner of the skill card, and then click **Confirm**
**Delete** in the dialog box.
6. Update the version.
i. Click the target skill card in the skill list. ii. Click **Update Version** in the upper-right corner of the skill details page. iii. Upload the new version file in the update version dialog box. The system automatically performs a security scan and completes the update. iv. Click **Start Update**.
7. View skill details.
i. Click the target skill card in the skill list. ii. Go to the skill details page to view the following information: Basic information: the name, category, description, and version. Skill configuration: the detailed configuration parameters of the skill. Usage records: the records of agents calling the skill, version upgrade details, and security information.

**Next steps**

After creating and enabling a skill, you can install and use the skill in an agent.

### 5.2 MCP

This topic describes how to manage Model Context Protocol (MCP) servers in the OpenTrek-

| Ops platform, including adding, editing, enabling, disabling, and deleting MCP servers. | The |   |
|---|---|---|
| platform uses the standardized MCP to connect to and manage various external servers. This |   |   |
| enables seamless integration and collaboration between agents and heterogeneous data |   |   |
| sources, tools, and business systems. |   |   |

**Scenarios**

In the OpenTrek-Ops platform, users manage the full lifecycle of MCP configurations in the asset center. This includes creating, editing, deleting, and managing versions of MCP configurations. This section applies to the following scenarios: Manage MCP servers in a unified manner to integrate agents with external systems. Configure MCP server connection parameters to ensure that agents can access external tools and services. Manage the lifecycle of MCP servers, including creating, editing, enabling, disabling, and deleting servers. The current user has logged in to the OpenTrek-Ops platform. The current user has the permissions to access MCP management in the asset center. Center
1. Log on to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Assets** > **MCP**.
On the **MCP** page, you can obtain the following information: View the numbers of enabled and disabled MCP servers. Use the search box to find target MCP servers. View the MCP list, which includes the name, description, server type, source, status, and number of tools.
3. Add an MCP server.
You can add an MCP server by using manual configuration, JSON import, or AI gateway synchronization.

**Method 1: Manual configuration**

a. On the **MCP** page, click **Add MCP**. b. On the **Manual Config** tab, configure the following parameters: Center

| Parameter | Required | Description |
|---|---|---|
| Server Type | Yes | Select a server type: SSE Streamable HTTP STDIO |
| Server Name | Yes | Enter a server name. |
| Description | No | Optional. Add a description. |

Center

| Server Address | Yes | Enter the server endpoint, such as http://localhost:8080/sse. |
|---|---|---|
| Headers | No | Add headers directly. You can add multiple headers. Click Paste. Paste headers in the Header:Value or Header=Value format with one header per line. Then, click Parse. |
| Environment Variables | No | Add environment variables. |
| Timeout | No | Specify the timeout period for connection, tool list retrieval, and tool invocation. Valid range: 1- 600 seconds. Default: 30 seconds. |

c. Click **Add**. The system sets the status of the added server to **Enabled**.

**Method 2: JSON import**

a. On the **MCP** page, click **Add MCP**. b. In the **Add MCP Server** dialog box, click **JSON Import**. c. Paste the MCP server configuration JSON string into the input box. Center d. Click **Import**. The system sets the status of the imported server to **Enabled**.

**Method 3: Gateway import**

After importing an AI gateway, you can use the **Sync Gateway** operation to automatically import the **MCP configurations** associated with the AI gateway. For more information, see Synchronize a gateway.
4. View MCP details.
In the server list, click a server name to view the basic info, connection config, and tool list of the server: Basic info View the name, description, server type, status, tool count, and last synchronization status of the server. Connection config View the server endpoint URL, timeout, and source. Tool list View detailed tool names and descriptions.
5. Disable or enable an MCP server.
For a server in the **Enabled** status, click the disable icon in the **Actions** column of the target server. For a server in the **Disabled** status, click the enable icon in the **Actions** column of the target server.
6. Edit an MCP server.

> **Note:** You cannot edit servers imported from a gateway.

Click **Edit** in the **Actions** column of the target server. In the **Edit MCP Server** dialog box, modify the **Description**, **Server Address**, **Headers**, **Environment Variables**, and
**Timeout**.
Center
7. Delete an MCP server.
Click **Delete** in the **Actions** column of the target server. In the **Confirm Delete** dialog box, click **Delete**.

> **Important:** This operation is irreversible. Proceed with caution.

### 5.3 Agent Infra

This topic describes the features and configurations of the Agent Infra module in the OpenTrek-Ops platform.

**Scenarios**

The Agent Infra feature applies to the following scenarios: Manage the infrastructure services that the agent depends on to ensure the stability of the agent runtime environment. Monitor the infrastructure status to detect and troubleshoot service faults promptly. Configure the infrastructure connection parameters to optimize service performance and resource utilization. Manage the integration and configuration of underlying services such as LLM Service, Redis, Object Storage Service (OSS), and PostgreSQL. You have logged in to the OpenTrek-Ops platform as a tenant administrator.
1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **Assets**>**Agent Infra**.
On the **Agent Infra** page, you can obtain the following information: View information such as the names and types of model services, Kubernetes clusters, AI gateways, and data storage infrastructure.
3. Model services
Add a model Center a. On the **Model Services** tab, click **Add Model** and configure the following parameters:

| Parameter | Required | Description |
|---|---|---|
| Model ID | Yes | Enter the identifier for model API calls, such as gpt- 4-turbo. |
| Display Name | Yes | Enter the display name of the model, such as GPT-4 Turbo. |
| Provider | Yes | Select a provider. The system currently supports Alibaba Cloud. |
| Protocol | Yes | Select a protocol. |
| Inference Type | Yes | Select Text Generation or Text Embedding. |
| API Key | Yes | Contact Alibaba Cloud technical support to obtain the API key. |
| API Endpoint | Yes | Contact Alibaba Cloud technical support to obtain the API endpoint. |

b. Click **Confirm**. Edit a model

> **Note:** Before you modify the infrastructure configuration, make sure that the modifications do not affect running agent tasks.

a. Click the edit icon in the **Actions** column of the target model. b. Modify the related parameters and click **Save Changes**. Remove a model a. Click the remove icon in the **Actions** column of the target model. b. In the dialog box that appears, click **Delete**.
4. Kubernetes clusters
Import a cluster Center a. On the **K8S Cluster** tab, click **Import Cluster** and configure the following parameters.

| Parameter | Required | Description |
|---|---|---|
| Cluster | Yes | Select the Kubernetes cluster instance to import. |
| Agent Service Endpoint | Yes | This endpoint generates the root domain name for agent links. Configure the wildcard DNS record in the DNS console in advance. |
| Access IP | No | Enter the domain name and port to access the cluster API server. If you leave this parameter empty, the system uses the domain name and port in the default kubeconfig. |
| ingressClassName | Yes | Select the Ingress type for agent domain name routing. |

b. Click **Import**. View details Click the name of the target cluster to view details such as the **Basic Info**, **Cluster Info**,
**Cluster Resources**, and **Master Nodes** of the cluster.
Edit a cluster Click the edit icon in the **Actions** column of the target cluster to modify the **Agent**
**Service Endpoint**, **Access IP**, and **ingressClassName** of the cluster. After you modify
the parameters, click **Save**. Remove a cluster Click the remove icon in the **Actions** column of the target cluster, and then click
**Remove** in the dialog box.
5. AI gateways
Import a gateway a. On the **AI Gateway** tab, click **Import Gateway** and configure the following parameters:

| Parameter | Required | Description |
|---|---|---|
| AI Gateway Name | Yes | Select the gateway instance to import. |
| API Key | Yes | Contact Alibaba Cloud technical support to obtain the API key. |

Center b. Click **Import**.

> **Note:** If you import an ASCM AI gateway, the system automatically imports the **MCP** **configuration** and **AI model configuration** associated with the AI gateway after you click **Import**. You can view the configurations on the **MCP** page and the **Agent** **Infra**>**Model Services** page.

View details Click the name of the target gateway to view details such as the **Basic Information**,
**Access Points**, **model API**, and **MCP** of the gateway.
Edit a gateway Click the edit icon in the **Actions** column of the target gateway. In the **Edit Higress**
**Gateway** dialog box, modify the **API Key** and click **Save**.
Synchronize a gateway Click the synchronize icon in the **Actions** column of the target gateway, and then click
**Sync** to synchronize the MCP and AI models for the gateway.
Remove a gateway Click the remove icon in the **Actions** column of the target gateway, and then click
**Remove** in the dialog box.
6. Data storage
On the **Data Storage** tab, click the instance name to view details such as the **Basic**
**Information** and **Access Endpoints** of the instance.
m Settings

## 6 System Settings

This article describes the functions and configuration methods of the OpenTrek-Ops platform system settings module, including tenant management, cloud platform management, channel management and system configuration four functions.

> **Important:** Please use system administrator login for system setup.

### 6.1 Organization management

This topic describes how to manage tenants in the OpenTrek-Ops platform.

**Scenarios**

The organization/tenant management feature applies to the following scenarios: Isolate resources and manage permissions in multi-tenancy environments to ensure independence among different tenants. Create dedicated tenants for different departments or business units to enable hierarchical management. Manage the tenant lifecycle, including creating, enabling, disabling, and deleting tenants. Configure the connection between tenants and the cloud platform to enable unified resource scheduling. You have log in to the OpenTrek-Ops platform. You have the system administrator permissions.
1. Log in to the OpenTrek-Ops platform.
2. The system displays the **Organization Management** page by default. On this page, you
can view the tenant list, involving the following fields:

| Field | Description |
|---|---|
| Tenant Name | The display name and identifier of the tenant. |

m Settings

| Cloud Platform | Indicates whether the tenant connects to the cloud platform. |
|---|---|
| Associated Organization | The name of the organization associated with the tenant. |
| Administrator | The username of the tenant administrator. |
| Created At | The creation date of the tenant. |
| Actions | You can edit or delete the tenant. |

3. Add a tenant.
i. On the **Organization Management** page, click **Add Tenant**. ii. Enter the following information in the pop-up form:

| Parameter | Required | Description |
|---|---|---|
| Tenant Name | Yes | The display name of the tenant. |
| Tenant Code | Yes | The unique identifier of the tenant. It supports only letters, numbers, and hyphens. |
| Description | No | Enter the description of the tenant. |
| Connect to cloud Platform | Yes | Select Yes or No. |
| Select Organization | Yes | If you select Yes for Connect to Cloud Platform, select an associated organization. You can select any level-2 organization under the same level-1 organization. Cross-level-1 organization selection is not supported. |
| Assign Administrators | Yes | If you select Yes for Connect to Cloud Platform, set tenant administrators. Select one or more users under the selected level-1 organization. |

iii. Click **Confirm Create** to complete the creation.
4. Edit a tenant.
i. Find the target tenant in the tenant list. ii. Click the edit icon in the **Actions** column to modify configuration information such as the tenant name and description. iii. Click **Save changes** to update the tenant. m Settings
5. Delete a tenant.

> **Warning:** Deleting a tenant is a high-risk operation. Proceed with caution. The system cannot recover any data under the tenant after deletion.

i. Find the target tenant in the tenant list. ii. Click the delete icon in the **Actions** column. iii. Click **Confirm Delete** in the confirmation dialog box. The system removes the tenant from the list after a successful deletion.

**Next steps**

Log in as the created tenant administrator to perform initial tenant configuration. This includes registering model services and importing Kubernetes clusters. For more information, see Agent Infra.

> **Note:** When you log in for the first time, the system prompts you to initialize the password. Follow the prompts to set a new password and store it securely.

### 6.2 Platform management

This topic describes how to manage cloud platform configurations in the OpenTrek-Ops platform.

**Scenarios**

The cloud platform management feature applies to the following scenarios: Configure and manage cloud platform resources and notification channels connected to the OpenTrek-Ops platform. Configure the push targets for agent running statuses and for alert messages. Implement unified management and resource scheduling in a multi-cloud platform environment. Enable real-time push notifications for O&M messages to ensure that Ops personnel obtain key information promptly. Configure multiple notification channels, such as DingTalk, email, and SMS, to meet the notification requirements of different scenarios. Manage cloud platform connection information and authentication credentials to ensure the stability of data interoperability. You have logged in to the OpenTrek-Ops platform. You have the system administrator permissions.

**Cloud platform management**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **System Settings** > **Platform**.
m Settings
3. On the **Platform Management** page, click **Cloud Platforms**.
On the cloud platform management page, you can view the list of configured cloud platforms.
4. Add a cloud platform configuration.
i. On the cloud platform management page, click **Add Cloud Platform**. ii. In the form that appears, enter the cloud platform connection information.

| Field | Required | Description |
|---|---|---|
| Platform Name | Yes | The custom name. We recommend that you enter a meaningful name. |
| Platform Code | Yes | The unique identifier of the platform. |
| Cloud Vendor | Yes | The default value is Alibaba Cloud Apsara Stack. |
| Cloud Platform OpenAPI Endpoint | Yes | The ASCM OpenAPI domain name. Contact Alibaba Cloud technical support to obtain the domain name. |
| Access Key (AK) | Yes | a. Log in to the Apsara Uni-Manager Management Console as the admin user. b. Click the icon in the upper-right corner and select Personal Information. c. View the Accesskey (AK) and AccessKey Secret (SK) of the admin user. |
| Secret Key (SK) | Yes |   |
| Enable Network Proxy | No | The system disables the network proxy by default. |

iii. Click **Confirm Create** to complete the creation.
5. Edit a cloud platform configuration.
Click the edit icon in the **Actions** column of the target cloud platform. You can edit the cloud platform name and the cloud platform OpenAPI endpoint. After you complete the update, click **Confirm Update**.
6. Delete a cloud platform configuration.
Click the delete icon in the **Actions** column of the target cloud platform. In the dialog box that appears, click **Confirm Delete**.

> **Warning:** The delete operation is irreversible. The system permanently deletes all configurations under the cloud platform. Proceed with caution.

7. Disable or enable a cloud platform.
m Settings Click the disable or enable icon in the **Actions** column of the target cloud platform to complete the operation.

**Channel management**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **System Settings** > **Platform**.
3. On the **Platform Management** page, click **Channels**.
On the **Channels** page, you can view the list of configured channels.
4. Enable a channel.
Click the switch in the upper-right corner of the target channel card to enable the channel. After you turn on the switch, the status changes to **Enabled**.

**System configuration**

1. Log in to the OpenTrek-Ops platform.
2. In the left-side navigation pane, choose **System Settings** > **Platform**.
3. On the **Platform Management** page, click **System Configuration**. You can modify the
preset configuration item for the skill package size.
4. Click **Edit** in the **Actions** column to modify the configuration value.

> **Note:** The modification takes effect immediately for all tenants. Adjust the value with caution to prevent an oversized skill from affecting the loading performance.

5. Click **Save**.
enant management

## 7 Multi-tenant management

This topic describes how to switch and manage tenants. You have logged in to the OpenTrek-Ops platform as a tenant administrator.
1. Log in to the OpenTrek-Ops platform.
2. Click the current tenant at the bottom of the left-side menu to switch tenants. The system
isolates resources for different tenants to ensure independence.
3. Configure the tenant.
In the tenant switch dialog, click the settings button for the target tenant. Enter the designated administrator in the input box and authorize the user as the Ops administrators of the current tenant.

> **Note:** Ensure that the tenant administrator added the organization of the selected user to the platform.

Click **Confirm Authorization**, and then click **Back** in the upper-right corner of the page. stant

## 8 AI Assistant

You can implement automated operations management with the AI Assistant. This topic describes how to use the AI Assistant.
1. Log in to the OpenTrek-Ops platform.
2. Click the icon in the lower-right corner of the interface to open the AI Assistant.
3. Enter your question in the input box of the AI Assistant and click
. New conversation: Click above the dialog box to start a new conversation. Conversation history: Click above the dialog box to view the conversation history. Full screen: Click above the dialog box to display the dialog box in full screen. Close conversation: Click above the dialog box to close the AI Assistant.

## 9 FAQ

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
