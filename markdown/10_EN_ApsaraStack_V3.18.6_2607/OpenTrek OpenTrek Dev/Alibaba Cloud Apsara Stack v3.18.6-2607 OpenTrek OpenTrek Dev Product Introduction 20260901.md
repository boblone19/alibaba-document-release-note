---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek Dev Product Introduction 20260901"
product_version: "V3.18.6_2607"
doc_version: "20260901"
pdf_pages: 35
source_pdf: "4d5dd09f2686d5a5_Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek Dev Product Introduction 20260901.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/OpenTrek/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20OpenTrek%20OpenTrek%20Dev%20Product%20Introduction%2020260901.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek OpenTrek Dev Product Introduction 20260901

## Table of Contents

- 1 Product details
- 2 Product value
- 3 Use cases
- 4 Functions and features

## 1 Product details

Model Studio-Enterprise Edition is an enterprise-grade development platform for large model agents, providing a one-stop toolchain for domain-specific knowledge processing and management, agent building, and capability evaluation.

**Background**

As large model technology moves into real-world production, enterprises face three core challenges in their intelligent transformation: First, large model application development is difficult to manage across the full lifecycle. In traditional workflows, fragmented toolchains and a lack of evaluation systems reduce development efficiency, while key stages like context engineering and dynamic knowledge system updates lack sufficient tools and proven methodologies. Second, limited multimodal data processing capabilities severely restrict the expansion of application scenarios. Enterprises struggle to effectively convert massive volumes of unstructured data—such as financial reports, blueprints, and audio/video files—into valuable knowledge assets. Finally, agent development faces the dual challenge of limited functional scope and significant security risks. Agents must meet diverse needs, ranging from simple Q&A to complex decision-making, while guaranteeing system stability and data security in enterprise-grade scenarios. Industry research shows that over 70% of enterprises building large model applications are hindered by pain points such as long knowledge base build cycles, limited agent functionality, and poor toolchain integration. These issues directly lengthen AI application development cycles by more than 40%. Model Studio-Enterprise Edition was created to address these critical bottlenecks. The platform focuses on enterprise-grade scenarios, centered on "full lifecycle management" and "foundational capability support." By providing a full-stack platform that covers data processing, application development, and O&M optimization, it streamlines the entire workflow from multimodal knowledge processing to engineering production-ready agents. As the core infrastructure for building AI-native systems, Model Studio-Enterprise Edition not only resolves toolchain fragmentation but also overcomes the limitations of traditional multimodal data processing. It delivers an end-to-end solution—from data parsing to application deployment—that helps enterprises accelerate AI deployment and iteration, moving large models from proof-of-concept to scalable industrial application.

**Product overview**

Model Studio-Enterprise Edition is an enterprise-grade dual platform for large model application development and knowledge processing. It provides a full lifecycle toolchain covering development, debugging, evaluation, observability, and O&M, and integrates core capabilities such as knowledge processing, agent building, and tool ecosystem management. For knowledge processing, the platform uses end-to-end multimodal parsing to manage various data modalities, including documents, images, audio/video, and data tables. It includes built-in deep-parsing templates to accurately process over 10 types of professional content, such as financial reports, academic papers, and policy documents. The platform enables complex table parsing, formula recognition, and image understanding, helping enterprises quickly build a high-quality knowledge base and providing foundational support for AI applications like RAG Q&A. For agent development, the platform provides comprehensive support for a wide range of scenarios: On the one hand, by integrating RAG for knowledge enhancement, custom workflow orchestration, and ReAct reasoning and decision-making mechanisms, developers can flexibly build various types of agents, such as knowledge Q&A, workflow-driven, and autonomous planning agents, meeting a wide range of needs from simple interactions to complex decision-making. On the other hand, the platform offers an open MCP and tool ecosystem that expands agent capabilities while ensuring stability under high concurrency and secure script execution. Additionally, the platform features a fine-grained memory management mechanism. Shortterm memory supports context compression and entity extraction, while long-term memory enables personalized services through user profiles and task maps. Combined with custom generation and retrieval strategies, this allows agents to continuously evolve. With these capabilities, Model Studio-Enterprise Edition provides a one-stop service for knowledge processing, agent development, evaluation, and O&M, establishing it as a core engine driving intelligent transformation across industries.

## 2 Product value

Model Studio Dedicated Edition integrates extensive industry-specific knowledge and data to support a wide range of applications. It addresses questions across multiple domains and provides accurate, comprehensive answers. This platform lets you efficiently manage solutions for all your use cases in one place.

**Efficient multimodal knowledge processing**

Customer value Build a high-quality enterprise knowledge base and rapidly deploy AI applications, such as RAG Q&A. Key capabilities Provides end-to-end knowledge parsing for managing multimodal data, including documents, images, audio, video, and data tables. It features over 20 deep-parsing templates for more than 10 document types, such as financial reports, academic papers, policies, and textbooks. These capabilities let you parse document layouts, complex tables, and formulas, as well as understand images, allowing you to quickly build a multimodal knowledge base using your private data.

**Build agents for any scenario**

Customer value Create various agents for a wide range of scenarios, including knowledge Q&A agents, workflow agents, and autonomous planning agents. Key capabilities Integrates multiple mechanisms, including RAG enhancement, custom workflow orchestration, and the ReAct framework for single-agent reasoning and decision-making. This lets developers switch between operating modes for diverse development needs, from basic Q&A to complex multi-agent systems.

**Open MCP and tool ecosystem**

Customer value Integrate diverse tools efficiently to enhance development flexibility and security. This simplifies the integration process, reduces costs, and accelerates business innovation and response. Key capabilities Supports asynchronous API tool calls and dynamic injection of authentication credentials for various tool types. You can register MCP services in either Server-Sent Events (SSE) or STDIO mode and run them in an isolated security sandbox for flexible and secure deployment. The platform also lets you wrap APIs as MCP services with a single click, ensuring cross-protocol compatibility and reducing integration costs.

**Fine-grained memory management**

Customer value Effectively manage long context for agent tasks using short-term memory, and deliver personalized experiences through long-term memory. This helps your agents improve and become more helpful with each interaction. Key capabilities Short-term memory management includes features like history round setting, long context compression, key entity extraction, and custom memory read and write. Long-term memory supports key Q&A, user profiling, and task mapping. It also lets you define custom memory generation, organization, and recall strategies.

## 3 Use cases

This topic describes how Model Studio can be applied in various industries. Model Studio lets organizations across various industries build powerful AI applications. The following sections highlight several key use cases.

**Public sector**

To simplify complex policy documents for the public, you can build an intelligent interpretation agent. By ingesting historical policy documents into a knowledge base, the agent can use retrieval-augmented generation (RAG) to provide clear explanations. It can also support voice-based queries and trace information back to specific clauses, reducing the workload on government helpdesks and improving efficiency for both citizens and businesses.

**Finance**

Buy-side financial institutions often need to quickly analyze vast amounts of unstructured data, such as financial reports, prospectuses, satellite imagery, and web articles. You can use multimodal capabilities to build a knowledge base that supports multi-source data retrieval. An agent built for investment analysis can then be configured with specific reasoning logic to automatically generate batch analysis reports on a recurring schedule.

**Energy and power**

In power grid management, slow fault responses and inefficient coordination between systems are common challenges. To address this, you can build an intelligent dispatch agent to act as a decision-making hub. By creating a dispatch knowledge base from integrated data sources—including command libraries, equipment ledgers, and historical contingency plans— the agent can identify and route issues, coordinate with power flow and transfer tools, manage contingency plans, and provide smart visualizations to support operators.

**Industrial manufacturing**

You can create an industrial internet of things (IIoT) data hub that consolidates real-time sensor data (such as temperature, pressure, and vibration) with historical production logs (like process parameters, quality inspection records, and energy reports). You can use this data to build a process optimization knowledge base. A process analysis agent can then use this knowledge base to forecast energy consumption, trace the root cause of defects, and intelligently tune process parameters, creating a closed-loop optimization system.

**Healthcare**

Patients often struggle with technical pharmaceutical information, and healthcare providers face a high volume of inquiries. You can build a medication consultation agent to address these issues. By integrating authoritative medical and pharmaceutical data, the agent can help users find drug information, match medications to symptoms, and obtain clear usage guidance. This enhances patient safety and makes accessing medication information more convenient.

**Media and publishing**

You can build an agent that combines retrieval from a local knowledge base with web search capabilities. This automates workflows for sensitive content detection, fact-checking, and style consistency analysis, significantly improving the efficiency of proofreading and editorial review processes.

**Education**

Using a multimodal model, you can build a tool that comprehensively understands both video and audio content from educational lectures. This capability automatically extracts key concepts, organizes them into a structured knowledge system, and generates concise summaries.

## 4 Functions and features

This topic describes the functions and features of Model Studio Exclusive.

| Level 1 feature | Level 2 feature | Level 3 feature | Level 3 feature description |
|---|---|---|---|
|   | Agent managemen t | Create a custom agent | You can create an agent from scratch by specifying the agent name, description, and creation method, and then proceed to the version configuration page for further settings. |
|   |   | Create an agent from a template | You can quickly build an agent based on a template through interface guidance and prompt engineering. |
|   |   | Edit an agent | You can modify the name, description, avatar, and other information of an existing agent to update the agent configuration and description as needed. |
|   |   | Delete an agent | You can permanently remove agents that are no longer needed to release system resources and keep the agent list clean. |
|   |   | Search for an agent | You can quickly search for an agent by name to locate a specific instance among multiple agents. |
|   |   | Export an agent | Enter the import key of the target environment to export the agent file. When you export an agent, the dependent model services, knowledge bases, memory content, Model Context Protocol (MCP) services, and sub-agents are not exported. Keys from the same environment cannot be used for export. |
|   |   | Import an agent | Select an exported agent file to import. You can import only agents that were exported with the current environment key, and only agent files from different environments are eligible for import. |
|   |   | Obtain an import key | The system automatically generates a key for verification when you export an agent to another environment. The key is valid for 72 hours. |

|   | Version managemen t | Create a custom version | You can create a new version of an agent, navigate to the workflow page to develop the agent version from scratch, and specify the version name and creation method. |
|---|---|---|---|
|   |   | Create a version from a template | You can quickly build a version based on a template through interface guidance and prompts. |
|   |   | Upgrade a template form to a workflow | This feature creates a replica of the current version and opens the workflow canvas on the replica, where you can implement more advanced and complex business processes. |
|   |   | Clone a version within the current agent | This feature allows you to clone the configuration of an existing agent version to generate an identical new version, which facilitates modifications without affecting the original version. |
|   |   | Clone a version to another namespace | This feature allows you to clone the configuration of an existing agent version to a specified namespace. The dependent model services, knowledge bases, memory content, MCP services, and sub-agents are not cloned. |
|   |   | Configure traffic switchover for a version | You can set traffic allocation quotas for specified agent versions and split traffic by session ID and request ID to ensure that the specified agent receives sufficient traffic resources. If you set traffic for a single version, that version becomes the output version. |
|   |   | Export an agent version | You can select one or more agent versions to export. When you export an agent version, the dependent model services, knowledge bases, memory content, and sub-agents are not exported. Keys from the same environment cannot be used for export. |
|   |   | Import an agent version | Select an exported agent file to import. You can import only agents that were exported with the current environment key, and only agent files from different environments are eligible for import. |
|   |   | Manage version status | You can manage different versions of an agent, including viewing version details, publishing versions, and unpublishing versions, to maintain the agent lifecycle. |

|   |   | Publish a version | You can publish an agent version in the design phase to make it available for external calls. Before publishing, the platform verifies the completeness and validity of the version. |
|---|---|---|---|
|   |   | Track performance | You can query the task details and log records of each request to the agent service and filter the results by version, session ID, and request ID. |
|   |   | Metric monitoring | The system collects metrics by agent and version dimensions, including Q&A success rate, average Q&A latency, number of Q&A requests, average time to first token, input token consumption, and output token consumption. The system also monitors business and performance metrics for the knowledge bases, tools, and models that a specified agent version calls. |
|   |   | Start node | This node defines the starting point of the agent workflow. You can customize input parameters and map them to the standard input of the agent to set initial conditions for subsequent tasks. |
|   |   | Iterator | This node works with the aggregator to distribute a collection of data in serial or parallel mode, which enables loop processing of the data list. |
|   |   | Aggregator | This node works with the iterator to distribute a collection of data in serial or parallel mode, which enables loop processing of the data list. |
|   |   | LLM node | This node configures a large language model (LLM) to perform specific inference tasks. You can select a model, set model parameters, configure input and output, and use prompts to control the model output. |
|   |   | Multimodal LLM node | This node configures a multimodal LLM to perform specific inference tasks. You can select a model, set model parameters, configure input and output, and use prompts to control the model output. |
|   |   | Text reranking model node | This node works with a text reranking model to perform specific tasks. You can select a model, set model parameters, and configure input and output. |

|   |   | Image-text reranking model node | This node works with an image-text reranking model to perform specific tasks. You can select a model, set model parameters, and configure input and output. |
|---|---|---|---|
|   |   | Tool node | This node calls registered tools. You can configure input parameters and select tools to perform specific functions or services. |
|   |   | Document retrieval | You can select an authorized document knowledge base for retrieval and configure retrieval parameters, input, and output. |
|   |   | Image-text retrieval | You can select an authorized image-text knowledge base for retrieval and configure retrieval parameters, input, and output. |
|   |   | Data table retrieval | You can select an authorized data table knowledge base for retrieval and configure retrieval parameters, input, and output. |
|   | Design a workflow |   |   |
|   |   | SQL executor | You can select a registered and authorized database on the platform to execute SQL tasks and configure input and output. |
|   |   | Content merging | This node merges multiple preceding output results. It supports streaming output of merged results and allows you to define combination rules and structures for multiple results. |
|   |   | Intermediate output | This node outputs partial information before the final result is generated. |
|   |   | Write to short-term memory | You can select variables configured in short- term memory and overwrite, append, or clear the variable values. |
|   |   | Agent node | You can select another configured agent version as a call node in the current workflow. The session between the parent and child agents remains relatively stable. |
|   |   | Script node | You can write custom scripts to complete tasks, define input and output parameters, and conform to the preset parameter structure. |

| Agent develop ment |   |   |   |
|---|---|---|---|
|   |   | Selector node | This node implements conditional branching logic in a workflow and allows you to select different execution paths based on input parameter values. |
|   |   | Result rendering node | This node combines and renders the output of an agent, including text, attachment content, and custom structured data. |
|   |   | Validity check | The system checks the validity of the agent configuration to ensure that all node configurations are correct and connections are valid, which guarantees normal agent operation. |
|   |   | Auto-save | The system automatically saves changes during agent configuration to ensure continuity of user operations and data security. |
|   |   | Manual save | You can manually trigger a save to store the current agent status and configuration at a specific point in time. |
|   |   | Function capabilities | The system provides a built-in function library with 30 functions. Developers can use these functions to further parse and process data or read specific information, such as retrieving the value of a specific key in an object, parsing data items in a list, and reading historical conversation records. |
|   |   | Text input debugging | Developers can enter text to simulate user interactions with the agent to test and adjust the agent response and processing logic for text input. |
|   |   | Attachment input debugging | You can upload attachments to test the ability of the agent to process different types of attachments, ensuring that the agent correctly parses and uses the data in the attachments. |
|   |   | Additional information debugging | The system provides an interface for entering additional information so that developers can simulate interactions in complex scenarios and test how the agent makes decisions based on additional information. |

|   | Debugging |   |   |
|---|---|---|---|
|   |   | JSON input debugging | You can enter data in JSON format to test the ability of the agent to parse and respond to structured data, which is suitable for API debugging. |
|   |   | Clear a session | Developers can clear all content in the current session and reset the session status to start a new interaction test, ensuring session independence. |
|   |   | Run mode debugging | In run mode, the agent automatically executes the full workflow and provides a response, which is suitable for quickly testing the automated execution process and efficiency of the agent. |
|   |   | Debug mode debugging | Debug mode allows you to manually trigger the execution of each task for finer-grained control and troubleshooting, which is suitable for debugging and optimizing complex logic. |
|   |   | Intermediate task inspection | The system displays all intermediate tasks and sub-step results during agent execution to help developers understand each step and logic in the interaction process. |
|   |   | Log viewing | Developers can view agent debugging logs, including error messages and execution status, to facilitate debugging analysis. |
|   |   | Thought process insertion and viewing | Developers can insert and view the thought process of the agent, including decision logic and reasoning steps, to evaluate and optimize the decision quality of the agent. |
|   |   | Short-term memory - conversation record toggle | You can define a toggle for conversation records. When disabled, the system cannot reference historical conversation records in the session. |
|   |   | Short-term memory - conversation record retention rounds | You can define the number of conversation record retention rounds and specify the handling method after exceeding the limit. The system supports truncation or summarization after the defined number of rounds is exceeded. |
|   |   | Short-term memory - conversation record summary settings | You can select a conversation record summary model and a summary prompt to improve the summarization quality. |

|   |   | Short-term memory - important entity toggle | Important entities refer to valuable information extracted from historical conversations and stored separately to prevent loss of critical information due to excessively long context. You can enable or disable this feature with a toggle. |
|---|---|---|---|
|   | Memory |   |   |
|   |   | Short-term memory - important entity settings | You can configure entity names, descriptions, and types. The system extracts entities based on these settings. You can configure up to 10 entities. |
|   |   | Short-term memory - important entity extraction settings | You can select an important entity extraction model and configure an important entity extraction prompt to improve the extraction quality. |
|   |   | Short-term memory - custom variables | You can configure custom variables and write variable content based on the custom memory node in the agent settings. |
|   |   | Long-term memory - create a memory partition with an important Q&A template | You can create a long-term memory partition by using an important Q&A template, select a memory generation model and a vector embedding model, and save important conversation content from sessions to the memory store to improve agent response quality. |
|   |   | Long-term memory - create a memory partition with a user profile template | You can create a long-term memory partition by using a user profile template and save user profile information from sessions to memory. You can select a memory generation model and a vector embedding model, and manually maintain user profile tags. |

|   |   | Long-term memory - create a custom memory partition | You can create a memory partition through workflow orchestration with the following parameter configurations: Memory storage structure: You can select key-value pairs, multi-text, or text. Memory generation strategy: You can select workflow orchestration or manual maintenance. Memory cleanup strategy: You can set the memory retention period and select permanent retention or time-based cleanup. Memory retrieval strategy: You can configure the memory retrieval method and retrieve and recall content by memory title or memory content. Vector embedding model: You can configure the vector embedding model for the memory retrieval strategy of the memory partition. |
|---|---|---|---|
|   |   | Long-term memory - edit memory content | You can edit specific memory entries in a memory partition and update the content to adapt to new business scenarios or requirements. |
|   |   | Long-term memory - delete memory content | You can remove individual memory entries that are no longer applicable or are incorrect to optimize the quality of the memory store. |
|   |   | Long-term memory - edit a memory partition | You can edit an existing memory partition and update its name, description, memory generation strategy, cleanup strategy, and retrieval strategy. |
|   |   | Long-term memory - delete a memory partition | You can delete an existing memory partition to adapt to the evolving requirements of the agent. |
|   |   | Long-term memory - debug a memory partition | You can debug the content in a memory partition by entering a query to verify the recall performance of the memory partition. |
|   |   | Template list | You can view the agent template name, ID, description, and other information, and navigate to the template details page from this page. |

| OpenTrek |   |   |   |
|---|---|---|---|
|   | Template list |   |   |
|   |   | Template details | You can view the template usage instructions, configuration requirements, APIs, capability dependencies, and other information, and initiate agent creation from this page. |
|   |   | Use a template | You can create an agent directly from the template details page based on the template. You can create a new agent or add a version to an existing agent. |
|   | Agent template - AutoDoc | Create an agent based on the AutoDoc template | You can create an agent instance based on the AutoDoc template. You can create a new agent or add a version to an existing agent, and customize the name and description. |
|   |   | Edit an agent based on the AutoDoc template | You can edit the name and description of an agent instance created based on the AutoDoc template. |
|   |   | Configure an agent based on the AutoDoc template | You can associate a single specified document knowledge base. |
|   |   |   | Parameter settings: You can configure parameters for standard Q&A, knowledge rewriting, multi-turn rewriting, vector retrieval, text retrieval, result reranking, and summarization. |
|   |   |   | Standard Q&A library: You can configure a standard Q&A library based on long-term memory partitions and add, edit, delete, or view standard Q&A entries. |
|   |   |   | Knowledge vocabulary: You can configure a knowledge vocabulary based on long-term memory partitions and add, edit, delete, or view standard Q&A entries. |
|   |   | Delete an agent based on the AutoDoc template | You can delete agent instances created based on this template. |
|   |   | Create an agent based on the AutoBI template | You can create an agent instance based on the AutoBI template. You can create a new agent or add a version to an existing agent, and customize the name and description. |

|   | v Product Intro and features |   |   |
|---|---|---|---|
| Agent template s | Agent template - AutoBI |   |   |
|   |   | Configure an agent based on the AutoBI template | Parameter settings: Associate a knowledge base: You can search for and bind a data table knowledge base. Knowledge rewriting: The system provides a default configuration scheme. You can also customize the LLM and parameters for knowledge rewriting, including the prompt and temperature. Multi-turn rewriting: The system provides a default configuration scheme. You can also customize the LLM and parameters for knowledge rewriting, including the prompt and temperature. Recall configuration: You can configure table columns, values, and SQL sample recall information. The system provides a default configuration scheme, and you can configure the recall count and recall threshold. SQL generation: You can configure the SQL generation scheme, select NL2SQL, and configure the runtime parameters of the LLM for SQL generation, including the prompt and temperature. Summarization: You can configure reply summarization to extract and summarize SQL execution results. The system provides a default configuration scheme, and you can also customize the LLM and parameters for summarization, including the prompt and temperature. Chart drawing: The system generates chart data structures from SQL execution results for the application to render corresponding charts. You can also customize the LLM and parameters for generating chart data structures, including the prompt and temperature. |
|   |   | Delete an AutoBI instance | You can delete agent instances created based on this template. |
|   |   | Data query | You can use natural language queries and instructions to handle database query operations. You only need to describe the query requirements, and the system automatically parses the requirements and generates the corresponding SQL query statements. |

|   |   | Data analysis | The system analyzes user input data query intents and query results, analyzes data results based on the question, extracts key information, performs data analysis, and generates an analysis summary. |
|---|---|---|---|
|   | Agent template - AutoVideo | Create an agent based on the AutoVideo template | You can create an agent instance based on the AutoVideo template. You can create a new agent or add a version to an existing agent, and customize the name and description. |
|   |   | Edit an agent based on the AutoVideo template | You can edit the name and description of an agent instance created based on the AutoVideo template. |
|   |   | Configure an agent based on the AutoVideo template | You can associate a single specified image- text knowledge base. |
|   |   |   | Parameter settings: You can configure parameters for standard Q&A, knowledge rewriting, multi-turn rewriting, vector retrieval, text retrieval, result reranking, and summarization. |
|   |   |   | Standard Q&A library: You can configure a standard Q&A library based on long-term memory partitions and add, edit, delete, or view standard Q&A entries. |
|   |   |   | Knowledge vocabulary: You can configure a knowledge vocabulary based on long-term memory partitions and add, edit, delete, or view standard Q&A entries. |
|   |   | Delete an agent based on the AutoVideo template | You can delete agent instances created based on this template. |
|   |   | General image understanding | The system generates basic content descriptions for up to four images within a single conversation. |
|   |   | Image understanding based on an image-text knowledge base | The system generates a description for a single image based on the recall configuration, reranking configuration, generation configuration, and the configured image-text knowledge base. |

|   |   | Image conversation | You can disable the recall configuration and conduct a conversation about a single image within a limited number of turns in a single- round conversation. |
|---|---|---|---|
|   |   | Video conversation | You can disable the recall configuration and conduct a conversation about a single video up to 20 MB in size within a limited number of turns in a single-round conversation. |
|   |   | General video understanding | The system generates basic content descriptions for videos up to 20 MB in size. |
|   |   | Specific chart type understanding | The system understands the content of line charts, bar charts, and pie charts that clearly present information. |
|   |   | Text-based image retrieval | You can retrieve images and text within the knowledge base by using text queries based on the recall and reranking configurations of AutoVideo. |
|   |   | Image-based image retrieval | You can retrieve images and text within the knowledge base by using image queries based on the recall and reranking configurations of AutoVideo. |
|   |   | Edit a tool | The system provides a tool editing feature that allows you to modify and update registered tools, including updating tool configuration information and request parameters. |
|   |   | Delete a tool | You can remove tools that are no longer needed to release system resources, which helps maintain a clean and efficient agent platform. |
|   | Tool list |   |   |
|   |   | Query a tool | The system provides a tool query feature that allows you to quickly find registered tools by keyword, which improves the efficiency of retrieving specific tools from a large number of tools and accelerates the development and maintenance process. |
|   |   | Upgrade to MCP | You can upgrade registered API-type tools to MCP with one click. You can add the upgrade to an existing MCP tool or create a new MCP tool. |

|   |   | Observability | You can view invocation metrics for a specified tool within a specific time range, including the success rate, average latency, and invocation count. |
|---|---|---|---|
|   |   | Tool registration | Agent Factory provides an API tool registration feature that allows you to integrate external service APIs into the agent platform. By entering information such as the tool name, description, address, and request method, you can define the basic attributes and invocation parameters of the API tool to quickly connect to and use third-party services. |
| My tools | API tool registration |   |   |
|   |   | Streaming API support | The system supports the integration and use of streaming APIs. You can configure API tools to support streaming output, which enables the API to continuously return data. |
|   |   | Asynchronous tool invocation support | For tools with long execution times per request, you can enable asynchronous invocation. After completing the integration according to the platform instructions, the system supports asynchronous invocation of the tools. |
|   | MCP service registration | Register an MCP tool in SSE mode | Select SSE mode to register an MCP tool. After entering the name and description, the system provides service configuration instructions and verifies service connectivity. |
|   |   | Register an MCP tool in STDIO mode | You can select a virtual machine, develop and upload a code package as required by the scaffold, and deploy the service on the virtual machine. |
|   | Tool debugging | API tool debugging | This module allows you to debug registered API tools to ensure connectivity and correct return results. You can simulate requests, observe tool response data, adjust parameter configurations, and optimize tool performance. |
|   |   | MCP service debugging | You can select a specific tool from an MCP service and debug it by using form-based or JSON-based input. For MCP tools registered in SSE mode with authentication information, you can enter authentication keys during debugging. |

| Platform tools | Platform tool list | Query the tool list | You can search for platform tools by tool name or tool type to quickly locate a specific tool. |
|---|---|---|---|
|   |   | Tool details | You can view platform tool details on the tool details page, including usage instructions, parameter descriptions, and resource dependencies, to understand the applicable scenarios of the tool. |
|   | Built-in platform API tools | Quark Search | This tool connects to the Quark Search API and is built in by default. To use it, enter the Quark authentication information and pay the associated fees. |
| Shared tools | Shared tool list | Query the shared tool list | You can search for platform tools by tool name or tool type to quickly locate a specific tool. |
|   |   | Query tool details | You can view tool details on the tool details page. |
|   | Shared tool debugging | API tool debugging | This module allows you to debug API tools to ensure connectivity and correct return results. You can simulate requests, observe tool response data, adjust parameter configurations, and optimize tool performance. |
|   |   | MCP service debugging | You can select a specific tool from an MCP service and debug it by using form-based or JSON-based input. For MCP tools registered in SSE mode with authentication information, you can enter authentication keys during debugging. |
|   | My templates | Create a prompt template | You can create prompt templates by using three frameworks: Custom, CRISPE, and Few- shot. You can also configure prompt tags to facilitate prompt template invocation and retrieval. |
|   |   | Template query | You can query templates by template tag and specified input content to quickly locate the required prompt template. |
|   |   | Template list | The system displays all created prompt templates. You can view the template name and debugging status in the list to facilitate template management. |

| Prompt template s |   |   |   |
|---|---|---|---|
|   |   | Edit a template | You can modify the name, tags, framework, and instruction content of a prompt template based on the template usage scenario. |
|   |   | Debug a template | You can debug a prompt template by entering variable values to verify template availability. You can also select a model service for debugging. |
|   |   | Delete a template | You can delete prompt templates that are no longer needed to organize the workspace. |
|   | Platform templates | Platform template list | The platform provides built-in prompt templates. You can debug templates and directly select them when building agents. |
|   |   | Platform template query | You can query built-in platform prompt templates by template category tag and prompt content to quickly locate a template. |
| Prompt optimiza tion | Optimization task list | Quey the task list | You can query instruction optimization tasks by prompt name to quickly locate a specific task and obtain task details and optimization status. |
|   |   | Task details | You can view the details of a prompt instruction optimization task. The system provides multiple optimization schemes, and you can save the optimization results to My Templates for agent building. |
|   |   | Terminate a task | You can terminate a prompt instruction optimization task that is in progress to interrupt the optimization process. |
|   |   | Delete a task | You can delete prompt instruction optimization tasks to organize the task workspace and facilitate task retrieval. |
|   | Initiate an optimization task | Create a prompt instruction optimization task | You can select a model to optimize instructions based on the input prompt description to improve prompt quality. |
|   | Evaluation set managemen t | Evaluation set version management | You can add, download, disable, enable, or delete an evaluation set version. You can also view evaluation set version log information. |

| OpenTrek De n·Functions |   |   |   |
|---|---|---|---|
| Agent evaluatio n |   |   |   |
|   | Evaluation tasks | Evaluation task management | After creating an evaluation task, you can view task details, including basic information and task instance information. You can also manually start, rerun, or delete tasks. |
|   |   | View evaluation results | For completed evaluation tasks, you can view evaluation reports. The evaluation reports display evaluation effectiveness information and sample analysis results to help you assess agent performance. |
|   | Knowledge base list | View a knowledge base | You can search for a knowledge base by knowledge base name, ID, or type, and view the name, description, configuration parameters, and status of a specific knowledge base. |
|   |   | Edit knowledge base information | You can edit the name, description, and retrieval strategy of an existing knowledge base. |
|   |   | Knowledge base content management | You can view the original files, task details, parsing status, and parsing results of a knowledge base. You can also delete tasks in the knowledge base and download the source files, parsing results, and segmentation results to organize knowledge base content. |
|   |   | Enable/disable a knowledge base | An enabled knowledge base can be invoked by agents. You can disable a knowledge base to restrict its invocation. |
|   |   | Delete a knowledge base | You can delete obsolete knowledge bases to release system resources. |
|   |   | Knowledge base metric observability | You can view invocation metrics for a specific knowledge base within a selected time range, including the invocation success rate, average latency, invocation count, and token consumption. |
|   |   | Custom creation | You can create a knowledge base in a more flexible way and configure it based on the knowledge base usage scenario: You can configure the content structure and field information of the knowledge base. You can configure vector index and ES index parameters for the retrieval strategy. |

|   | Create a custom knowledge base |   |   |
|---|---|---|---|
|   |   | Build indexes for custom knowledge bases | You can build indexes for custom knowledge bases to improve the accuracy of knowledge retrieval during invocations. You can configure index content including content structure, indexed content, storage information, model selection, and retrieval and recall fields. The system also supports adding and configuring index nodes in workflows. |
|   | Create a document knowledge base | Create from a document template | You can select a document knowledge base template, enter the knowledge base name and description, and quickly create a document knowledge base. |
|   |   | Advanced settings - Switch the vector embedding model | You can switch the text vectorization model on the advanced settings page. You can switch the model only when creating a knowledge base. After the knowledge base is created, the text vectorization model cannot be modified. |
|   |   | Advanced settings - Parsing strategy | You can configure a parsing strategy on the advanced settings page. Based on different parsing strategies, the system can perform document text extraction, layout analysis, image OCR, table parsing, formula parsing, and image parsing. |
|   | Create an image-text knowledge base | Create from an image- text template | You can select an image-text knowledge base template, enter the knowledge base name and description, and quickly create a document knowledge base. |
|   |   | Advanced settings - Vectorization | You can configure the image-text vectorization model and vectorization trigger conditions. After the knowledge base is created, the image-text vectorization model cannot be modified. |
|   |   | Advanced settings - Image-text parsing | You can enable or disable intelligent parsing and configure the image-text parsing model and related prompts. |
|   | Create a data table knowledge base | Create from a data table template | You can create a data table knowledge base from a data table knowledge base template. By configuring the data source, you can import information from a database into the knowledge base to quickly enable data invocation. |

| Knowled ge base |   |   |   |
|---|---|---|---|
|   | Custom knowledge base details | View knowledge base details | You can view the knowledge base name, description, ID, and creation method. |
|   |   | Query knowledge base content | You can search for tasks by knowledge base content keyword or status. The system supports querying by content structure table. |
|   |   | Import knowledge base content | You can batch add knowledge base content by using template import or API import. |
|   |   | Delete a task | You can delete obsolete tasks to organize knowledge base content. |
|   |   | Retry a task | You can reprocess the content to be imported. |
|   |   | Refresh the content list | The system refreshes the page status automatically every 30 seconds. |
|   | Document knowledge base details | View knowledge base details | The system displays the knowledge base name, description, knowledge base code, and creation method. |
|   |   | Original files - Query | You can query original files by file code, file name, format, or status. |
|   |   | Original files - Import files | You can import files by uploading documents or synchronizing through APIs. |
|   |   | Original files - Delete | You can delete files. The system also deletes the corresponding parsing results, segmentation results, and vector database data. Batch deletion is supported. |
|   |   | Original files - Parsing details | You can view file parsing results, verify segmentation and parsing status, and edit parsing results. |
|   |   | Original files - Re-parse | You can re-parse files. Batch re-parsing is supported. |
|   |   | Original files - Download source files | You can download source files to your local device. |

|   |   | Original files - Download parsing results | You can download parsing result files. |
|---|---|---|---|
|   |   | Original files - Refresh | The system refreshes the page status automatically every 30 seconds. |
|   |   | Content details - Query | You can search for content by keyword, segment code, or status. |
|   |   | Content details - Batch import | You can batch import content by using template import or API synchronization. |
|   |   | Content details - Delete | You can delete parsed content. Batch deletion is supported. |
|   |   | Content details - Re- vectorize | You can re-vectorize specified content. This operation is not supported when the content is in the vector database. |
|   |   | Content details - Refresh | The system refreshes the page status automatically every 30 seconds. |
|   | Image-text knowledge base details | View knowledge base details | The system displays the knowledge base name, description, code, and creation method. |
|   |   | Query | You can query by file code, file name, or status. |
|   |   | Import files | You can import files by uploading files, importing from templates, or synchronizing through APIs. |
|   |   | Parse | You can manually edit image content, image descriptions, and image tags so that agents can retrieve them when accessing the knowledge base. |
|   |   | Intelligent parsing | You can initiate intelligent parsing to overwrite existing content. Batch intelligent parsing is supported. |
|   |   | Delete files | You can delete obsolete images. Batch deletion is supported. |

|   |   | Re-vectorize | You can re-vectorize images. Batch re- vectorization is supported. |
|---|---|---|---|
|   |   | Refresh | The system refreshes the page status automatically every 30 seconds. |
|   | Data table knowledge base details | View knowledge base details | The system displays the knowledge base name, description, code, and creation method. |
|   |   | Edit a knowledge base | You can register data tables and edit knowledge base details based on the registered data tables. |
|   | Shared knowledge bases | View shared knowledge bases | On the shared knowledge base menu page, you can view the list of knowledge bases shared from other namespaces to this namespace and view knowledge base details. |
|   |   | Share knowledge bases | You can select a knowledge base in the current namespace and share it with other namespaces where you have permissions. |
|   | Dataset managemen t | Dataset creation and configuration | You can view the dataset list and filter datasets by keyword or tag. Datasets use a three-level tag system, and you can design and manage custom dataset tags. |
|   |   |   | You can create and manage datasets. The system supports multiple data modalities including documents, text, images, audio, video, and tables. You can organize dataset files by hierarchical paths. |
|   |   |   | The system supports hosting multiple file types: Image: .png, .jpg, .jpeg, .bmp, .gif, .webp, .svg, .ico, .tiff, .eps, .psd, .raw, .heic, .jxr Audio: .wav, .mp3, .aac, .flac, .alac, .ogg, .wma, .aiff, .dsd, .midi, .dts, .amr, .opus, .m4a Video: .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .mpeg, .3gp, .vob, .ts, .asf, .rm Rich text document: pdf, txt, doc, docx, md, epub, caj, wps, xls, xlsx, ppt, pptx, html, htm, rtf, odt, ods, xml, tex, mobi, fb2, fb2z, azw Tabular: .csv, .json, .jsonl, .parquet |

| Data manage ment |   |   |   |
|---|---|---|---|
|   |   | Data view | Datasets support multiple subsets with flexible data formats. You can configure custom mappings between subsets and file data, and enable or disable automatic updates for subset data. |
|   |   | Data files | You can batch upload data files through files and folders, and download or delete files. A maximum file limit applies per batch, and you can upload different file types in the same batch. |
|   |   | Dataset permissions | The system provides data permission management. Namespace administrators and dataset creators have full operation permissions on datasets, while regular users can only browse. |
|   | Integrated developmen t | CLI operation mode | The system provides a CLI operation mode that allows you to batch upload and download data files through the command line. |
|   |   | OpenAPI | The system provides OpenAPIs that support dataset operations such as dataset creation, data file upload, and subset creation and configuration. |
|   | Task templates | View templates and create tasks | The system provides processing templates. You can filter, search, and view template details including detailed descriptions and data flow details. You can also create tasks from templates. |
|   | Processing tasks | Task management | You can create data processing tasks to perform batch data processing on datasets. |
|   |   |   | Tasks distinguish between draft and published states. The system provides task management features including task configuration, publishing, unpublishing, and cloning. |
|   |   | Task execution | You can flexibly configure the compute resource specifications and parallelism required for task execution. |

|   |   | Task configuration | The system categorizes templates into cleaning, parsing, augmentation, balancing, and end-to-end types. You can create pipeline tasks and combine CPU and GPU resource operators within the same task. The system supports saving processing results as new subsets. |
|---|---|---|---|
|   |   | View task instances | The system provides task instance O&M features. You can view task instance execution status, input and output dataset information, and logs. |
|   | Task O&M |   |   |
|   |   | Cancel and rerun task instances | Task instance O&M supports cancel and rerun operations. |
|   | Integrated developmen t | CLI operation mode | The system provides a CLI operation mode that allows you to create and execute tasks through the command line. |
|   |   | OpenAPI | The system provides OpenAPIs that support creating, deleting, configuring, and viewing tasks and instances. |
|   | End-to-end templates | Document - Basic PDF parsing to generate knowledge segments | The system parses user-uploaded PDF documents and directly extracts native PDF content. Scanned content and image content extraction are not supported. The system generates semantic data structures and splits parsing results into knowledge segments that you can import into a knowledge base. |
|   |   | Document - Advanced PDF parsing to generate knowledge segments | The system parses user-uploaded PDF documents with layout analysis capabilities. It supports parsing tables, formulas, and URL hyperlinks, and generates a semantic structure tree. The system splits parsing results into knowledge segments that you can import into a knowledge base. |
|   |   | Document - Basic Excel parsing to generate knowledge segments | The system parses user-uploaded Excel documents such as xls and xlsx files. Image parsing within documents is not supported. The system performs chunk splitting, generates knowledge segments, and saves results as datasets. You can save the split knowledge segment results as JSONL files in a unified platform format. |

| Data processi ng |   |   |   |
|---|---|---|---|
|   |   | Document - Basic Word parsing to generate knowledge segments | The system parses user-uploaded Word documents. Image parsing within documents is not supported. The system generates a semantic structure tree and splits parsing results into knowledge segments that you can import into a knowledge base. |
|   |   | Document - Advanced Word parsing to generate knowledge segments | The system parses user-uploaded Word documents and supports parsing images within documents. The system generates a semantic structure tree and splits parsing results into knowledge segments that you can import into a knowledge base. |
|   |   | Document - Plain text document to generate knowledge segments | The system splits user-uploaded plain text documents into knowledge segments that you can import into a knowledge base. Supported file types include txt, json, jsonl, and md. |
|   | Data parsing templates | Document - Advanced PDF parsing | The system parses user-uploaded PDF documents and automatically converts Word documents to PDF for parsing. The system saves results as JSONL files corresponding to the documents. |
|   |   | Document - Basic PDF parsing | The system parses user-uploaded PDF documents and directly extracts native PDF content. Scanned content and image content extraction are not supported. The system generates semantic data structures and saves parsing results as datasets. |
|   |   | Document - Basic Word parsing | The system parses user-uploaded Word documents. Image parsing within documents is not supported. The system saves results as JSONL files corresponding to the documents. |
|   |   | Document - Advanced Word parsing | The system parses user-uploaded Word documents and supports parsing images within documents. You can save parsing results as corresponding JSONL files. |
|   |   | Video - Intelligent video segment parsing and keyframe extraction | The system splits videos into multiple segments and returns the boundary timestamps and keyframes for each segment without returning the actual video segments. The system generates summary descriptions for segments and keyframes. Multiple video file formats are supported. |

|   |   | Video - Video slicing | Based on video parsing results, the system splits long videos into segments and generates a corpus dataset according to the platform text-to-video data protocol. |
|---|---|---|---|
|   |   | Video - Video frame extraction | Based on video parsing results, the system extracts frames from long videos to generate JPG images and creates a corpus dataset according to the platform text-to-image training data protocol. |
|   | Data cleaning templates | Text - Data cleaning | The system cleans specified columns in text datasets through operations such as encoding conversion, content filtering, sensitive information processing, and deduplication. You can combine operators as needed to generate high-quality text data suitable for LLM training. |
|   |   | Video - Data cleaning | The system filters video datasets by aspect ratio, duration, and resolution to select suitable samples. |
|   |   | Image - Data cleaning | The system cleans image datasets through operations such as deduplication, shape filtering, size filtering, clarity filtering, and aspect ratio filtering to select suitable samples. |
|   | Data augmentatio n | Text - SFT Q&A pair augmentation | For a text Q&A pair sample set, the system extracts seed Q&A pairs (up to 10) and generates new Q&A samples (up to 2,000) based on the content and format features of the seed Q&A pairs. |
|   |   | Text - Text Q&A pair extraction | The system extracts Q&A pairs from text segments and saves the results as JSONL files and data subsets. |
|   |   | Image - Image description and Q&A pair pre-annotation template | The system batch generates image descriptions and Q&A pairs, and stores them in the pre tag column as pre-annotation _ content. You can specify the prompt and the questions that the model needs to answer. |

|   | Data balancing | Text - Data balancing - Random undersampling | This operator resolves multi-class data imbalance. It randomly samples majority class samples in the dataset so that each class has the same number of samples as the smallest class, achieving data balance. This operator applies primarily to classification tasks, especially when class distribution is severely imbalanced. |
|---|---|---|---|
|   |   | Text - Data balancing - Random oversampling | This operator resolves multi-class data imbalance. It randomly duplicates minority class samples in the dataset so that each class has the same number of samples as the largest class, achieving data balance. This operator applies primarily to classification tasks, especially when class distribution is severely imbalanced. |
|   |   | Text - Data balancing - Clustering-based undersampling | This template implements K-means clustering-based undersampling to resolve class imbalance. It performs K-means clustering on each class and reduces majority class samples to match the number of minority class samples, generating a dataset with balanced class distribution. |
|   |   | Text - Data balancing - Data augmentation- based oversampling | This template resolves class imbalance in multi-class classification tasks. It uses text data augmentation techniques to oversample minority class samples and generates new samples to balance the sample count across classes. |
|   | Global resource management |   | Global resource management allows you to add and manage various data resources required by the platform, including infrastructure resources such as object storage and databases. This feature provides unified resource storage and management capabilities for agent services, data centers, and knowledge bases. Only organization administrators or resource set administrators can configure these resources when accessing with administrator roles. |
|   | Global service management |   | The system provides creation, configuration, and O&M management capabilities for agent services and data center resources. Through global service management, you can configure gateway services, storage resources, and database resources for agent applications, and allocate namespaces for services to ensure stable operation of agent services and normal data center services. |

|   | System settings - Scenario default models | Scenario default service list | You can view the default service configuration for platform scenarios and implement global control. |
|---|---|---|---|
|   |   | Scenario default service settings | Agents, memory, and knowledge bases each use models in various scenarios. The model selection provides default options and supports custom configuration. You can switch models in the scenario interface. |
| System manage ment |   |   |   |
|   | System settings - System parameter settings | System parameter settings list | You can view and manage system parameters, and search for system parameters by name or code. |
|   |   | System parameter configuration | You can configure various parameters for the agent center. The settings take effect globally after configuration. You can also batch configure parameters by uploading files. |
|   | System settings - Request traffic control | Request traffic control list | You can view the allocated traffic request counts and maximum parallel task counts for different namespaces, agents, and versions. |
|   |   | Request traffic control methods | You can control traffic by the number of concurrent requests or by the number of parallel processing requests. |
|   |   | Edit version traffic | You can modify the configured version traffic control and adjust traffic guarantees based on agent usage. |
|   |   | Delete version traffic | You can delete the version traffic control configuration for agents that no longer require traffic control. |
|   | System settings - VM managemen t | VM management query | You can filter virtual machines (VMs) by VM name, VM code, or available namespace. |
|   |   | VM list | You can view VM details and status, and refresh the connection status of a specific VM in the list. |
|   |   | View VM services | You can view the list of services deployed on a VM. |
|   |   | Register a VM | You can select the available namespace for a VM. You must complete a connectivity test before submitting and saving the registration. |

|   |   | Edit a VM | You can modify VM registration information, including the service name and available namespace. |
|---|---|---|---|
|   |   | Delete a VM | You can delete VMs that are no longer in use. This also deletes all services in the service list of the VM. |
|   | Model integration | Integrate a model | You can integrate platform-deployed models or third-party registered models, and allocate namespaces for integrated models. |
|   |   | Model list | You can view and filter integrated models, and enable, disable, or edit integrated models. |
|   |   | Model debugging | You can debug integrated models to verify model service connectivity. |
|   | Namespace managemen t | Namespace list | You can view the list of namespaces to which you belong. |
|   |   | Create a namespace | Administrators can create namespaces. |
|   |   | Namespace member management | Namespace administrators can add or remove namespace members and assign regular members as administrators. |
