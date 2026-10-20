---
title: "OpenTrek Dev Product Introduction 20260630"
product_version: "V3.18.6"
pdf_pages: 32
source_pdf: "4bfc02cff8409685_Alibaba Cloud Apsara Stack V3.18.6 OpenTrek Dev Product Introduction 20260630.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/OpenTrek%20Dev/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20OpenTrek%20Dev%20Product%20Introduction%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# OpenTrek Dev Product Introduction 20260630

## Table of Contents

- 1 Product details
- 2 Product value
- 3 Use cases
- 4 Features

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

## 4 Features

Model Studio dedicated edition features

| Primary feature | Seconda ry feature | Tertiary feature | Description |
|---|---|---|---|
|   | Agent manage ment | Custom agent creation | Create an agent from scratch by providing a name, description, and creation method. After initialization, you'll be taken to the version configuration page for further setup. |
|   |   | Create agent from template | Quickly create an agent from a template using a guided interface and prompt engineering. |
|   |   | Edit agent | Edit an existing agent's name, description, avatar, and other details to update its configuration. |
|   |   | Delete agent | Permanently remove unneeded agents to free up system resources and organize the agent list. |
|   |   | Search agent | Quickly locate a specific agent by searching for its name. |
|   |   | Export agent | Export an agent file by providing the import key for the target environment. Agent dependencies, such as model services, knowledge bases, memory content, MCP services, and sub-agents, are not exported. You cannot export an agent using an import key from the same environment. |
|   |   | Import agent | Select an exported agent file to import. You can only import an agent if it was exported using an import key generated for the current environment. This feature is intended for importing agent files between different environments. |
|   |   | Get import key | Generates an import key to validate agent exports from other environments. The key is valid for 72 hours. |
|   |   | Custom version creation | Create a new agent version. After specifying a version name and creation method, you will be directed to the workflow page to develop the version from scratch. |
|   |   | Create version from template | Quickly build an agent version from a template using a guided interface and prompts. |

|   | Version manage ment |   |   |
|---|---|---|---|
|   |   | Upgrade template form to workflow | Duplicates the current version and opens the copy on the workflow canvas to enable more advanced business processes. |
|   |   | Clone version within agent | Clones an agent version's configuration to create an identical new version, allowing modifications without affecting the original. |
|   |   | Clone version to another workspace | Clones an existing agent version's configuration to a specified workspace. Dependencies such as model services, knowledge bases, memory content, MCP services, and sub- agents are not cloned. |
|   |   | Traffic allocation settings | Set traffic allocation quotas for a specified agent version. Supports traffic splitting by session ID and request ID to ensure the version receives sufficient resources. When an agent has only one version, allocating traffic to it also sets it as the output version. |
|   |   | Export agent version | Export selected agent versions, with multi-select support. Dependencies such as model services, knowledge bases, memory content, and sub-agents are not exported. You cannot export a version using an import key from the same environment. |
|   |   | Import agent version | Select an exported agent version file to import. You can only import a version if it was exported using an import key generated for the current environment. This feature is intended for importing agent versions between different environments. |
|   |   | Version status managemen t | Manage the lifecycle of agent versions, including viewing details, publishing, and taking versions offline. |
|   |   | Publish version | Publish a version in development to a live state, making it available for external calls. The platform performs completeness and validity checks before publishing. |
|   |   | Effect tracking | Query task details and log records for each agent service request. Supports filtering by version, session ID, and request ID. |
|   |   | Metric monitoring | Monitor 11 business and performance metrics at both the agent and version levels: request concurrency, concurrency ratio, concurrency trend, success rate, average request latency, average time to first token, maximum request latency, maximum time to first token, memory consumption, input tokens, and output tokens. |

|   |   | Start node | Defines the starting point of the agent workflow. Customize input parameters and map them to the agent's standard input to set initial conditions for subsequent tasks. |
|---|---|---|---|
|   |   | Iterator | Paired with an Aggregator, distributes a collection of data serially or in parallel, enabling iteration over a list of data. |
|   |   | Aggregator | Paired with an Iterator, aggregates data distributed serially or in parallel from an iteration. |
|   |   | Large Language Model (LLM) node | Configures a Large Language Model (LLM) to perform specific inference tasks. Supports model selection, parameter settings, input/output configuration, and prompt-based content generation. |
|   |   | Multimodal understandi ng LLM node | Configures a multimodal understanding Large Language Model (LLM) to perform specific inference tasks. Supports model selection, parameter settings, input/output configuration, and prompt-based content generation. |
|   |   | Text reranking model node | Reranks text using a specified model. Supports model selection, parameter settings, and input/output configuration. |
|   |   | Image-text reranking model node | Reranks image-text pairs using a specified model. Supports model selection, parameter settings, and input/output configuration. |
|   |   | Tool node | Calls a registered tool. You can configure its input parameters to perform a specific function. |
|   |   | Document retrieval | Retrieves from authorized document knowledge bases. Supports configuration of retrieval parameters, input, and output. |
|   |   | Image-text retrieval | Retrieves from authorized image-text knowledge bases. Supports configuration of retrieval parameters, input, and output. |
|   |   | Data table retrieval | Retrieves from authorized data table knowledge bases. Supports configuration of retrieval parameters, input, and output. |
|   |   | SQL executor | Executes SQL tasks on an authorized database registered with the platform. Supports input and output configuration. |

| Agent develop ment | Design workflo w |   |   |
|---|---|---|---|
|   |   | Content merge | Merges outputs from multiple preceding nodes. Supports streaming output for merged results and defining rules and structures for combining results. |
|   |   | Intermediate output | Outputs partial information from preceding nodes before the final result is generated. |
|   |   | Write to short-term memory | Allows you to select variables defined in short-term memory and perform operations such as overwriting, appending, or clearing their values. |
|   |   | Agent node | Allows you to select another configured agent version as a callable node within the current workflow. The session between the main agent and sub-agent remains relatively stable. |
|   |   | Script node | Allows you to write custom scripts to complete tasks. Supports defining input and output parameters that conform to a preset structure. |
|   |   | Selector node | Implements conditional branching logic in the workflow, choosing different execution paths based on the values of input parameters. |
|   |   | Result rendering node | Combines and renders the agent's output information, including text, attachment content, and custom structured data. |
|   |   | Validation | Validates the agent's configuration, ensuring all nodes are configured correctly and connections are logical to guarantee normal operation. |
|   |   | Autosave | Automatically saves configuration changes to ensure operational continuity and data safety. |
|   |   | Manual save | Provides an option to manually save the configuration, allowing users to save the agent's current state at a specific moment. |
|   |   | Function capabilities | Provides a built-in library of 30 functions, enabling developers to further parse and process data or read specific information, such as getting the value of a specific key in an object, parsing items from a list, or reading historical dialogue records. |

|   | Debuggi ng | Text input debugging | Allows developers to input text to simulate user-agent interactions to test and adjust the agent's response and processing logic. |
|---|---|---|---|
|   |   | Attachment input debugging | Allows you to upload attachments to test the agent's ability to handle different attachment types and ensure it can correctly parse and use the contained data. |
|   |   | Additional information debugging | Provides an interface for inputting additional information to simulate interactions in complex scenarios and test how the agent uses this information for decision-making. |
|   |   | JSON input debugging | Allows data input in JSON format to help developers test the agent's ability to parse and respond to structured data. Suitable for API debugging. |
|   |   | Clear session | Enables developers to clear all content from the current session and reset its state, allowing them to start a fresh interaction test and ensure session independence. |
|   |   | Run mode debugging | In Run mode, the agent automatically executes the entire task chain and provides an answer. This mode is suitable for quickly validating the agent's automated execution flow and efficiency. |
|   |   | Debug mode debugging | Debug mode allows manual triggering of each task's execution for fine-grained troubleshooting. This mode is suitable for debugging and optimizing complex logic. |
|   |   | Intermediate task view | Displays all intermediate tasks and sub-step results during the agent's execution to help developers understand each step and the logic of the entire interaction process. |
|   |   | View logs | Allows you to view the agent's debug logs, including error messages and execution status, to facilitate analysis and troubleshooting. |
|   |   | Insert and view thought process | Allows developers to insert and view the agent's thought process, including decision logic and reasoning steps, to evaluate and optimize the agent's decision-making quality. |
|   |   | Short-term memory: Conversatio n history toggle | Enable or disable the conversation history. If disabled, the agent cannot reference past dialogue from the session. |

|   | v Product In |   |   |
|---|---|---|---|
|   | Memory |   |   |
|   |   | Short-term memory: Conversatio n turn limit | Define the number of conversation turns to retain and the handling method when the limit is exceeded. Options include truncating or summarizing the history. |
|   |   | Short-term memory: Conversatio n summary settings | Select a model and set a prompt for summarizing conversation history to improve summary quality. |
|   |   | Short-term memory: Key entities toggle | Toggle the extraction of key entities, which are valuable pieces of information from the conversation history saved separately to avoid being lost in a long context. |
|   |   | Short-term memory: Key entity settings | Set the name, description, and type for up to 10 entities. The system extracts entities based on these settings. |
|   |   | Short-term memory: Key entity extraction settings | Select a model and set a prompt for key entity extraction to improve its effectiveness. |
|   |   | Short-term memory: Custom variables | Set custom variables. Their content can be written using the "Custom Memory" node in the agent settings. |
|   |   | Long-term memory: Create memory partition from Q&A template | Create a long-term memory partition from a Q&A template, saving important conversation content to the memory store to improve agent response quality. Supports selecting models for memory generation and vectorization. |
|   |   | Long-term memory: Create memory partition from user profile template | Create a long-term memory partition from a user profile template, saving user profile information from conversations to memory. Supports selecting models for memory generation and vectorization. User profile tags can be maintained manually. |

|   |   | Long-term memory: Custom memory partition creation | Create a memory partition through workflow orchestration. Configuration parameters include: Memory storage structure: Choose from key-value pairs, multiple texts, or text. Memory generation strategy: Choose between workflow orchestration or manual maintenance. Memory organization strategy: Set a retention policy, such as permanent or time-based cleanup. Memory retrieval strategy: Set the retrieval method to search and recall content by memory title or content. Vectorization model: Configure the vectorization model for the memory partition's retrieval strategy. |
|---|---|---|---|
|   |   | Long-term memory: Edit memory content | Edit specific memory entries within a partition to update their content for new business scenarios or requirements. |
|   |   | Long-term memory: Delete memory content | Remove individual memory entries that are outdated or incorrect to improve the quality of the memory store. |
|   |   | Long-term memory: Edit memory partition | Edit an existing memory partition to update its name, description, generation strategy, organization strategy, retrieval strategy, and other information. |
|   |   | Long-term memory: Delete memory partition | Delete an existing memory partition to adapt to the agent's evolving needs. |
|   |   | Long-term memory: Debug memory partition | Debug the content of a memory partition by entering a query to test its recall effectiveness. |
|   | Templat e list | Template list | View agent template names, IDs, descriptions, and other information, and access template details from this page. |
|   |   | Template details | View template usage instructions, configuration requirements, APIs, capability dependencies, and other information. You can also create an agent from this page. |
|   |   | Use template | Create an agent directly from a template's detail page. You can choose to create a new agent or add a new version to an existing agent. |

|   | Agent templat e - AutoDoc | Create agent from AutoDoc template | Create an agent instance from the AutoDoc template. You can choose to create a new agent or add a version to an existing one, and customize the name and description. |
|---|---|---|---|
|   |   | Edit AutoDoc template agent | Edit the name and description of agent instances created from the AutoDoc template. |
|   |   | Configure AutoDoc template agent | Associate a single, specified document knowledge base. |
|   |   |   | Configure parameters for various stages, including standard Q&A, knowledge rewriting, multi-turn rewriting, vector retrieval, text retrieval, result reranking, and summarization. |
|   |   |   | Standard Q&A library: Set up a standard Q&A library based on a long-term memory partition. Supports adding, editing, deleting, and viewing standard Q&A content. |
|   |   |   | Knowledge lexicon: Set up a knowledge lexicon based on a long-term memory partition. Supports adding, editing, deleting, and viewing terms and their definitions. |
|   |   | Delete AutoDoc template agent | Delete agent instances created from this template. |
|   |   | Create agent from AutoBI template | Create an agent instance from the AutoBI template. You can choose to create a new agent or add a version to an existing one, and customize the name and description. |

| Agent template s |   |   |   |
|---|---|---|---|
|   |   | Configure AutoBI template agent | Parameter settings: Associate knowledge base: Search for and bind data table knowledge bases. Knowledge rewriting: Use the default configuration or customize the LLM and its parameters (such as prompt and temperature) for knowledge rewriting. Multi-turn rewriting: Use the default configuration or customize the LLM and its parameters (such as prompt and temperature) for multi-turn rewriting. Recall configuration: Configure recall information for table columns, values, and SQL samples. Use the default configuration or set the recall count and threshold. Generate SQL: Configure the SQL generation scheme. Select NL2SQL and configure the runtime parameters (such as prompt and temperature) of the LLM used for SQL generation. Summarization: Configure response summaries by refining and summarizing SQL execution results. Use the default configuration or customize the LLM and its parameters (such as prompt and temperature) for summarization. Chart generation: Generate chart data structures from SQL execution results for application rendering. Customize the LLM and its parameters (such as prompt and temperature) for generating chart data structures. |
|   | Agent templat e - AutoBI |   |   |
|   |   | Delete AutoBI instance | Delete agent instances created from this template. |
|   |   | Data query | Handles database queries using natural language and commands. When you describe the query requirement, the system automatically parses it and generates the corresponding SQL query statement. |
|   |   | Data analysis | Analyzes the user's data query intent and the query results. It then analyzes these results in the context of the query to extract key information, perform data analysis, and generate an analytical summary. |
|   |   | Create agent from AutoVideo template | Create an agent instance from the AutoVideo template. You can choose to create a new agent or add a version to an existing one, and customize the name and description. |

|   | v Product In |   |   |
|---|---|---|---|
|   | Agent templat e - AutoVid eo |   |   |
|   |   | Edit AutoVideo template agent | Edit the name and description of agent instances created from the AutoVideo template. |
|   |   | Configure AutoVideo template agent | Associate a single, specified image-text knowledge base. |
|   |   |   | Configure parameters for various stages, including standard Q&A, knowledge rewriting, multi-turn rewriting, vector retrieval, text retrieval, result reranking, and summarization. |
|   |   |   | Standard Q&A library: Set up a standard Q&A library based on a long-term memory partition. Supports adding, editing, deleting, and viewing standard Q&A content. |
|   |   |   | Knowledge lexicon: Set up a knowledge lexicon based on a long-term memory partition. Supports adding, editing, deleting, and viewing terms and their definitions. |
|   |   | Delete AutoVideo template agent | Delete agent instances created from this template. |
|   |   | General image understandi ng | Generates basic content descriptions for up to four images within the same conversation. |
|   |   | Image understandi ng with image-text knowledge base | Generates descriptions for single images based on recall, reranking, and generation configurations, along with the configured image-text knowledge base. |
|   |   | Image conversation | Supports conversations about a single image for a limited number of turns within a single dialogue when recall configuration is disabled. |
|   |   | Video conversation | Supports conversations about a single video (under 20 MB) for a limited number of turns within a single dialogue when recall configuration is disabled. |
|   |   | General video understandi ng | Generates basic content descriptions for videos up to 20 MB in size. |

|   |   | Specific chart type understandi ng | Supports content understanding for three types of clearly presented chart images: line charts, bar charts, and pie charts. |
|---|---|---|---|
|   |   | Text-to- image retrieval | Retrieves images from the knowledge base using a text query, based on AutoVideo's recall and reranking configurations. |
|   |   | Image-to- image retrieval | Retrieves images from the knowledge base using an image query, based on AutoVideo's recall and reranking configurations. |
| My tools | Tool list | Edit tool | Edit registered tools. This allows you to modify and update tool information, such as configuration details and request parameters. |
|   |   | Delete tool | Remove tools that are no longer needed, freeing up system resources and helping to maintain a clean and efficient platform. |
|   |   | Query tool | Lets you quickly find registered tools by keyword, which improves the efficiency of locating specific tools and speeds up development and maintenance. |
|   |   | Upgrade to MCP | Registered API-type tools can be upgraded to an MCP service with one click. Supports adding the upgraded tool to an existing MCP tool or creating a new MCP. |
|   |   | MCP service details | Displays the details of an MCP service, showing the tools it contains. You can switch views to see tool descriptions, request parameters, and response parameters. |
|   | API tool registrat ion | Register tool | Register external service APIs. By providing the tool's name, description, address, and request method, you can define the API tool's basic properties and call parameters for quick integration. |
|   |   | Streaming API support | Integrate and use streaming APIs. Configure API tools to support streaming output, which allows the interface to continuously return data. |
|   |   | Asynchronou s invocation support | Enable asynchronous invocation for long-running request tasks. Asynchronous tool calls are supported after completing the integration according to platform instructions. |

|   | MCP service registrat ion | Register MCP tool in SSE mode | Register an MCP tool in SSE mode by providing a name and description, then following the service configuration instructions and verifying service connectivity. |
|---|---|---|---|
|   |   | Register MCP tool in STDIO mode | Select a virtual machine, develop and upload a code package according to the scaffold requirements, and deploy the service on the virtual machine. |
|   | Tool debuggi ng | API tool debugging | Debug registered API tools to ensure their connectivity and the correctness of their responses. Simulate requests and observe the tool's response data to adjust parameters and optimize performance. |
|   |   | MCP service debugging | Supports selecting a specific tool within an MCP service for debugging via form or JSON input. For MCP tools registered in SSE mode that require authentication, you can provide an authentication key during debugging. |
| Platform | Platform tool list | Query tool list | Search for platform tools by name or type to quickly find a specific tool. |
|   |   | Tool details | View the details of a platform tool, including usage instructions, parameter descriptions, and resource dependencies, to understand its applicable scenarios. |
| tools |   |   |   |
|   | Platform built-in API tool | Quark Search | Integrates with the Quark Search API. It is built-in by default. To use it, enter your Quark authentication information and pay the related fees. |
| Shared tools | Shared tool list | Query shared tool list | Search for platform tools by name or type to quickly find a specific tool. |
|   |   | Query tool details | View the details page of a tool to see its usage information. |
|   | Debug shared tool | API tool debugging | Debug API tools to ensure their connectivity and the correctness of their responses. Simulate requests and observe the tool's response data to adjust parameters and optimize performance. |
|   |   | MCP service debugging | Supports selecting a specific tool within an MCP service for debugging via form or JSON input. For MCP tools registered in SSE mode that require authentication, an authentication key can be provided during debugging. |

| Prompt template s | My templat es | Create prompt template | Create prompt templates using Custom, CRISPE, and Few- shot frameworks. You can configure prompt tags for easy calling and searching of templates. |
|---|---|---|---|
|   |   | Query template | Query templates by tags and specified content to quickly find the desired prompt template. |
|   |   | Template list | Displays all created prompt templates. The list shows template names and debug status for easy management. |
|   |   | Edit template | Change the name, tags, framework, and instruction content of a prompt template. The template content can be adjusted based on its usage scenario. |
|   |   | Debug template | Debug a prompt template by inputting variable values to verify its usability. Supports selecting a model service for debugging. |
|   |   | Delete template | Delete prompt templates that are no longer needed to keep your workspace organized. |
|   | Platform templat es | Platform template list | Provides built-in platform prompt templates. Supports template debugging and can be selected directly when building agents. |
|   |   | Query platform template | Quickly finds built-in platform prompt templates by querying by template category tags and prompt content. |
| Prompt optimiza tion | Optimiz ation task list | Query task list | Query prompt optimization tasks by prompt name to quickly find a specific task and get its details and optimization status. |
|   |   | Task details | View the details of a prompt optimization task. Multiple optimization solutions are provided, and results can be saved to "My Templates" to be used when building agents. |
|   |   | Terminate task | Terminate a prompt optimization task that is in progress, which interrupts the optimization process. |
|   |   | Delete task | Delete prompt optimization tasks to clean up the task workspace for easier searching. |
|   | Initiate optimiza tion task | Create new prompt optimization task | Select a model to optimize the instruction based on the input prompt description, thereby improving prompt quality. |

| Agent evaluati on | Evaluati on set manage ment | Evaluation set version managemen t | Supports adding, downloading, disabling, enabling, and deleting evaluation set versions, as well as viewing their log information. |
|---|---|---|---|
|   | Evaluati on task | Evaluation task managemen t | After an evaluation task is created, you can view its details, which include basic information and task instance information. Supports manually starting, rerunning, or deleting the task. |
|   |   | View evaluation results | For completed evaluation tasks, you can view the evaluation report. The report displays performance information and sample analysis results to help you assess the agent's effectiveness. |
|   | Knowled ge base list | View knowledge base | Find a knowledge base by its name, ID, or type, and view its name, description, configuration parameters, and status. |
|   |   | Edit knowledge base information | Edit the name, description, and retrieval strategy of an existing knowledge base. |
|   |   | Content managemen t | View a knowledge base's original files, task details, parsing status, and parsing results. Supports deleting tasks and downloading source files, parsed results, and chunking results to manage the content. |
|   |   | Enable/Disa ble knowledge base | An enabled knowledge base can be called by an agent. Disabling a knowledge base restricts its use. |
|   |   | Delete knowledge base | Delete obsolete knowledge bases to free up system resources. |
|   | Custom knowled ge base creation | Custom creation | Create a knowledge base with more flexibility and configure it for specific use cases: Configure the content structure and its fields. The retrieval strategy can be configured with vector index and Elasticsearch index parameters. |
|   |   | Build index for custom knowledge base | Build an index for a custom knowledge base to improve the accuracy of knowledge recall. Configuration includes content structure, index content, storage information, model selection, and fields for retrieval and recall. Supports adding and configuring index nodes in the workflow. |

|   | Docume nt knowled ge base creation | Create from document template | Select a document knowledge base template and enter a name and description to quickly create a document knowledge base. |
|---|---|---|---|
|   |   | Advanced settings: Vector model switching | Switch the text vectorization model on the advanced settings page. This can only be done when creating a new knowledge base; the model cannot be changed after creation. |
|   |   | Advanced settings: Parsing strategy | Set parsing strategies on the advanced settings page. Different strategies enable features like document text extraction, layout analysis, image OCR, table parsing, formula parsing, and image parsing. |
|   | Image- text knowled ge base creation | Create from image-text template | Select an image-text knowledge base template and enter a name and description to quickly create a knowledge base. |
|   |   | Advanced settings: Vectorizatio n | Set the image-text vectorization model and vectorization trigger conditions. The model cannot be changed after the knowledge base is created. |
|   |   | Advanced settings: Image-text parsing | Enable or disable smart parsing, and set the image-text parsing model and related prompts. |
|   | Data table knowled ge base creation | Create from data table template | Create a data table knowledge base from a template. By configuring the data source, you can import information from a database into the knowledge base to enable quick data calls. |
|   | Custom knowled ge base details | View knowledge base details | View the knowledge base name, description, ID, and creation method. |
|   |   | Query knowledge base content | Search for tasks by content keyword or status. Supports queries based on the content structure table. |
|   |   | Import to knowledge base | Batch add content to the knowledge base by using a template or via the API. |

| Knowled ge base |   |   |   |
|---|---|---|---|
|   |   | Delete task | Delete obsolete tasks to clean up the knowledge base content. |
|   |   | Retry task | Reprocess ingested content. |
|   |   | Refresh content list | Refresh the page status. Automatically refreshes every 30 seconds. |
|   | Docume nt knowled ge base details | View knowledge base details | Displays the knowledge base name, description, code, and creation method. |
|   |   | Original files: Query | Query original files by file code, filename, format, and status. |
|   |   | Original files: Import file | Import files via document upload or API synchronization. |
|   |   | Original files: Delete | Delete a file, along with its corresponding parsed results, chunking results, and vector data. Supports batch deletion. |
|   |   | Original files: Parsing details | View the file parsing results to inspect chunking and parsing status. Supports editing the parsed results. |
|   |   | Original files: Reparse | Reparse a file. Supports batch reparsing. |
|   |   | Original files: Download source file | Download the source file to your local machine. |
|   |   | Original files: Download parsed results | Download the parsed result file. |
|   |   | Original files: Refresh | Refresh the page status. Automatically refreshes every 30 seconds. |
|   |   | Content details: Query | Search for content by keyword, chunk code, and status. |

|   |   | Content details: Batch import | Batch import content via template import or API synchronization. |
|---|---|---|---|
|   |   | Content details: Delete | Delete parsed content. Supports batch deletion. |
|   |   | Content details: Re- vectorize | Re-vectorize specified content. This operation is not supported if the content is already in the vector store. |
|   |   | Content details: Refresh | Refresh the page status. Automatically refreshes every 30 seconds. |
|   | Image- text knowled | Display knowledge base details | Displays the knowledge base name, description, code, and creation method. |
|   |   | Query | Query by file code, filename, and status. |
|   |   | Import file | Import files via file upload, template import, or API synchronization. |
|   |   | Parse | Manually edit image content, descriptions, and tags for recall when the agent accesses the knowledge base. |
|   | ge base details | Smart parse | Initiate smart parsing, which overwrites existing content. Supports batch smart parsing. |
|   |   | Delete file | Delete obsolete images. Supports batch deletion. |
|   |   | Re-vectorize | Re-initiate vectorization for an image. Supports batch re- vectorization. |
|   |   | Refresh | Refresh the page status. Automatically refreshes every 30 seconds. |
|   | Data table knowled ge base details | Display knowledge base details | Displays the knowledge base name, description, code, and creation method. |
|   |   | Edit knowledge base | Register a data table and edit the knowledge base details based on the registered table. |

|   | Shared knowled ge base | View shared knowledge base | On the Shared Knowledge Base page, view a list of knowledge bases shared from other workspaces to the current one, and view their details. |
|---|---|---|---|
|   |   | Share knowledge base | Share a specific knowledge base from the current workspace to other authorized workspaces. |
| Data manage ment | Dataset manage ment | Dataset creation and settings | View a list of datasets, filtering by keyword and tag. Datasets feature a three-level tagging system and support custom design and management of dataset tags. |
|   |   |   | Create and manage datasets for multiple data modalities, including documents, text, images, audio, video, and tables. Dataset files can be managed in a hierarchical path structure. |
|   |   |   | Supports hosting multiple file types: Image: .png, .jpg, .jpeg, .bmp, .gif, .webp, .svg, .ico, .tiff, .eps, .psd, .raw, .heic, .jxr Audio: .wav, .mp3, .aac, .flac, .alac, .ogg, .wma, .aiff, .dsd, .midi, .dts, .amr, .opus, .m4a Video: .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm, .mpeg, .3gp, .vob, .ts, .asf, .rm Document: pdf, txt, doc, docx, md, epub, caj, wps, xls, xlsx, ppt, pptx, html, htm, rtf, odt, ods, xml, tex, mobi, fb2, fb2z, azw Tabular: .csv, .json, .jsonl, .parquet |
|   |   | Data view | Datasets can contain multiple subsets with flexible data formats. Users can custom-configure the mapping between subsets and file data, and enable or disable automatic updates for subset data. |
|   |   | Data files | Supports batch uploading of data files as individual files or in folders, with download and delete operations available. Batch uploads have a limit on the number of files. Different file types can be uploaded in the same batch. |
|   |   | Dataset permissions | Includes data permission management. Workspace administrators and dataset creators have full permissions, while regular users have read-only access. |
|   | Integrat ed develop ment | Command- line interface (CLI) | Provides a command-line interface (CLI) for batch uploading and downloading of data files. |
| 6 |   | > Document Version: 2026063 |   |

|   |   | OpenAPI | Provides an OpenAPI for dataset operations such as dataset creation, data file upload, and subset creation configuration. |
|---|---|---|---|
|   | Task templat es | View templates and create tasks | Provides data processing templates. Supports filtering, searching, and viewing template details, including detailed descriptions and dataflow diagrams. You can also create tasks from templates. |
|   | Processi ng tasks | Task managemen t | Create data processing tasks for batch processing of datasets. |
|   |   |   | Tasks can be in either a draft or a published state and include management functions such as configuration, publishing, decommissioning, and cloning. |
|   |   | Run task | Flexibly configure the computing resource specifications and parallelism required for task execution. |
|   |   | Task configuratio n | Templates are categorized as cleaning, parsing, enhancement, balancing, and end-to-end. Supports creating pipeline tasks where a single task can combine both CPU- and GPU-based operators. Processing results can be saved as a new subset. |
|   | Task operatio ns and mainten ance | View task instances | Provides task instance O&M functions. Supports viewing task instance execution status, input and output dataset information, and logs. |
|   |   | Cancel and rerun task instances | Task instance O&M supports cancel and rerun operations. |
|   | Integrat ed develop ment | Command- line interface (CLI) | Provides a command-line interface (CLI) for creating and executing tasks. |
|   |   | OpenAPI | Provides an OpenAPI for CRUD (Create, Read, Update, Delete) and view operations on tasks and instances. |
|   |   | Document - Basic PDF parsing to generate knowledge snippets | Parses uploaded PDF documents, directly extracts native content and generates a semantic data structure. Scanned content and images are not supported. The parsed results are split into knowledge snippets and can be imported into a knowledge base. |

|   | End-to- end templat es |   |   |
|---|---|---|---|
|   |   | Document - Deep PDF parsing to generate knowledge snippets | Parses uploaded PDF documents with layout analysis capabilities. Supports parsing tables, formulas, and URL hyperlinks, and generates a semantic structure tree. The parsed results are split into knowledge snippets and can be imported into a knowledge base. |
|   |   | Document - Basic Excel parsing to generate knowledge snippets | Parses uploaded Excel documents (such as .xls, .xlsx) without parsing images, performs chunking, and generates knowledge snippets. The results are saved as a dataset, and the split snippets can be saved as a JSONL file in the platform's unified format. |
|   |   | Document - Basic Word parsing to generate knowledge snippets | Parses uploaded Word documents without parsing images and generates a semantic structure tree. The parsed results are split into knowledge snippets and can be imported into a knowledge base. |
|   |   | Document - Deep Word parsing to generate knowledge snippets | Parses uploaded Word documents, including support for parsing images within the document, and generates a semantic structure tree. The parsed results are split into knowledge snippets and can be imported into a knowledge base. |
|   |   | Document - Plain text parsing to generate knowledge snippets | Splits uploaded plain text documents (supports .txt, .json, .jsonl, .md) into knowledge snippets that can be imported into a knowledge base. |
|   |   | Document: Deep PDF parsing | Parses uploaded PDF documents. Word documents are automatically converted to PDF and then parsed. The results are saved as a corresponding JSONL file for the document. |
| Data processi ng |   |   |   |
|   |   | Document: Basic PDF parsing | Parses uploaded PDF documents, directly extracts native content (scanned content and images are not supported), generates a semantic data structure, and saves the results as a dataset. |
|   |   | Document: Basic Word parsing | Parses uploaded Word documents without parsing images. The results are saved as a corresponding JSONL file for the document. |

|   | Data parsing templat es |   |   |
|---|---|---|---|
|   |   | Document: Deep Word parsing | Parses uploaded Word documents, including support for parsing images within the document. The results can be saved as a corresponding JSONL file. |
|   |   | Video: Smart parsing of segments and keyframes | Splits a video into multiple segments, returns the boundary time points and a keyframe for each segment (but not the video segments themselves), and provides a summary description for each segment and keyframe. Supports various video file formats. |
|   |   | Video: Video slicing | Based on video parsing results, slices a long video into segments and generates a corpus dataset according to the platform's text-to-video data protocol. |
|   |   | Video: Video frame extraction | Based on video parsing results, extracts frames from a long video to generate images (in JPG format) and creates a corpus dataset according to the platform's text-to-image training data protocol. |
|   | Data cleaning templat es | Text: Data cleaning | Cleans specified columns in a text dataset, including encoding conversion, content filtering, sensitive information handling, and deduplication. Operators can be combined as needed to generate high-quality text data suitable for LLM training. |
|   |   | Video: Data cleaning | Performs operations such as aspect ratio filtering, duration filtering, and resolution filtering on a video dataset to filter out suitable samples. |
|   |   | Image: Data cleaning | Performs operations such as deduplication, shape filtering, size filtering, clarity filtering, and aspect ratio filtering on an image dataset to filter out suitable samples. |
|   | Data augmen tation | Text: SFT Q&A pair augmentatio n | For a set of text question-and-answer (Q&A) pairs, this extracts up to 10 seed Q&A pairs and generates up to 2,000 new Q&A samples based on their content and format features. |
|   |   | Text: Text Q&A pair extraction | Extracts Q&A pairs from text snippets. The results are saved as a JSONL file and a data subset. |
|   |   | Image: Pre- annotation template for descriptions and Q&A pairs | Batch generates two types of data about images: descriptions and Q&A pairs. This data is stored in the pre tag _ column as pre-annotated content. Users can specify the prompt and the questions the model needs to answer. |

|   | Data balancin g | Text: Random undersampli ng | Addresses multi-class data imbalance by randomly sampling the majority classes to match the sample count of the smallest class, thus achieving data balance. This operator is mainly used in classification tasks, especially when class distribution is severely imbalanced. |
|---|---|---|---|
|   |   | Text: Random oversamplin g | Addresses multi-class data imbalance by randomly duplicating samples from minority classes to match the sample count of the largest class, thus achieving data balance. This operator is mainly used in classification tasks, especially when class distribution is severely imbalanced. |
|   |   | Text: Cluster- based undersampli ng | This template implements an undersampling function based on K-means clustering to address class imbalance. By applying K-means clustering to each class, it reduces the number of majority class samples to match the number of minority class samples, generating a dataset with a balanced class distribution. |
|   |   | Text: Augmentatio n-based oversamplin g | This template is mainly used to address class imbalance in multi-class classification tasks. It uses text data augmentation techniques to oversample minority classes by generating new samples to balance the number of samples across all classes. |
|   | System settings: Default scenario models | Default scenario service list | View the default service configurations for platform scenarios to enable global control. |
|   |   | Default scenario service settings | For scenarios in agents, memory, and knowledge bases that use models, you can customize the default model selection. Users can also switch models on the respective scenario interfaces. |
|   | System settings: System paramet ers | System parameter list | View and manage system parameters. Supports querying by parameter name and code. |
|   |   | System parameter configuratio n | Set various parameters for the agent center, which will take effect globally. Supports batch configuration by uploading a file. |

|   | System settings: Request traffic control | Request traffic control list | View and manage request quotas and maximum concurrent tasks for different workspaces, agents, and versions. |
|---|---|---|---|
|   |   | Request traffic control method | You can choose to control traffic by the number of concurrent requests or by the number of parallel processing requests. |
|   |   | Edit version traffic | Modify existing version traffic control settings to adjust traffic guarantees based on agent usage. |
| System manage ment |   | Delete version traffic | For agents that no longer require version traffic control, you can delete the configuration. |
|   | System settings: Virtual machine manage ment | Query virtual machine managemen t | Filter virtual machines by name, code, and available workspace. |
|   |   | Virtual machine list | View virtual machine details and status. Supports refreshing the connection status of a specific virtual machine from the list. |
|   |   | View virtual machine services | View the list of services deployed on this virtual machine. |
|   |   | Register virtual machine | Select an available workspace for the virtual machine. A connectivity test must be passed before the registration can be submitted. |
|   |   | Edit virtual machine | Modify virtual machine registration information, including the service name and available workspace. |
|   |   | Delete virtual machine | Delete a virtual machine that is no longer in use, along with all services deployed on it. |
|   | Model integrati on | Integrate model | Integrate models deployed on the platform or registered from third parties. Integrated models can be allocated to workspaces. |
|   |   | Model list | Lets you view and filter integrated models. You can also perform operations such as enabling, disabling, and editing them. |
|   | Version: 20 |   |   |

|   | v Product In |   |   |
|---|---|---|---|
|   |   | Debug model | Debug an integrated model to confirm its service connectivity. |
|   | Workspa ce manage ment | Workspace list | View a list of workspaces that you belong to. |
|   |   | Create workspace | Administrators can create new workspaces. |
|   |   | Workspace member managemen t | Workspace administrators can add and remove members and assign administrator roles. |
