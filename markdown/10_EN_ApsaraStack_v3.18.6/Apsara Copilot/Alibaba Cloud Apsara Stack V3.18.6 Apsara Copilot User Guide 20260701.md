---
title: "Apsara Copilot User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 61
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara Copilot User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%A3%9E%E5%A4%A9%E5%8A%A9%E7%90%86/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Copilot%20User%20Guide%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara Copilot User Guide 20260701

## Apsara Copilot homepage

The homepage displays the full capabilities of Apsara Copilot to help you deeply understand the product's value and usage, and provide clear guidance.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. Click
in the top navigation bar or floating menu to enter Apsara Copilot.
3. Click
above the **Apsara Copilot** dialog box, or click **Assistant Introduction** inside the dialog box.
4. Go to the Apsara Copilot homepage to view its positioning, features, highlights, and
benefits.

**Note**

**Experience now**: Click **Experience now** to open the Apsara Copilot dialog box.
**Official documents**: Click **Official documents** to go to the Apsara Copilot help
documentation.

## Access control of Apsara

**Copilot**

This topic describes how to implement the access control of Apsara Copilot by configuring custom roles with different permissions.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Permissions** > **Role Permissions**.
4. Click **Create Custom Role**.
5. Configure the basic information, management permissions, application permissions, menu
permissions, and custom permissions for the role. For more information about the configurations, see the "Manage custom roles" topic in User Guide of the Apsara Uni-manager Management Console. In the **Application Permissions** step, search for and find Apsara Stack Assistant and select the permissions that you want to grant to the role based on your business requirements.
6. After the role is created, assign the role to users.

| Parameter |  | Description |
|---|---|---|
|  | Enable on Platform | Specifies whether to display Apsara Copilot in the console. If you turn on the switch, Apsara Copilot is displayed in the floating menu and top navigation bar. : does not display Apsara Copilot. : displays Apsara Copilot. |

## Configurations of Apsara

**Copilot**

### Configure custom settings

This topic describes how to enable, disable, and configure the custom settings of Apsara Copilot.

**Prerequisites**

You are an operations administrator.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, choose **Apsara Copilot** > **Custom Settings**.
4. On the **Custom Settings** page, configure the parameters based on your business
requirements. To restore Apsara Copilot to the default settings, click **Restore Default**
**Settings** in the lower part of the page. The configurations take effect the next time you log
in to the console.

| Display Control |  |  |
|---|---|---|
|  | Intranet Search | Specifies whether to display the switch for enabling internal network-based search in the Apsara Copilot pane. : does not display the switch. : displays the switch. If you turn on the switch, you must also configure the information about a local knowledge base. Note This feature allows users to determine whether to use internal network-based search in the Apsara Copilot pane. Knowledge Source: The value is fixed to Model Studio Dedicated Edition. URL: the API of the knowledge center of Model Studio, which can be used to retrieve relevant files in the specified workspace and knowledge base. APP KEY: the AppKey that is in effect. _ Workspace Code: the code of the workspace to which the knowledge base belongs in workspace management. Knowledge Base Code: the code of the knowledge base in knowledge services. |
| AI Assistant Settings | Specify a language for the AI assistant. | You can select Simplified Chinese, English, or Traditional Chinese. |
|  | Assistant Name | We recommend that you enter a name that does not exceed 40 characters in length. The default name is Apsara Copilot. |
|  | Greetings | The greetings used by Apsara Copilot. |
|  | Recommende d Questions on Home Page | The recommended questions to be displayed on the homepage of Apsara Copilot. You can click Add Question to add more questions or click the icon in the row of a question to remove the question. |
|  | Disclaimer | The legal disclaimer used by Apsara Copilot. Default legal disclaimer: This content is AI-generated and may not be completely accurate. Use it as a reference only. |
|  | Official Alternative Answer | The alternative answer used by Apsara Copilot. |

|  | Entry Icon | The display icon of Apsara Copilot. We recommend that you use an image whose aspect ratio is 1:1, such as 100 × 100 pixels in the GIF, PNG, JPG, or JPEG format. |
|---|---|---|
|  | Welcome Page Icon | The logo to be displayed on the welcome page of Apsara Copilot. We recommend that you use an image whose aspect ratio is 1:1, such as 100 × 100 pixels in the GIF, PNG, JPG, or JPEG format. |
|  | Conversation Icon | The avatar used by Apsara Copilot during conversations. We recommend that you use an image whose aspect ratio is 1:1, such as 100 × 100 pixels in the GIF, PNG, JPG, or JPEG format. |
|  | Answer Style | The style of the answer. Valid values: Expert Mode, Simple Mode, and Service Mode. Expert Mode: rigorous, clear structure, and standardized terminology. It is suitable for technical support engineers to implement in-depth Q&A, architecture design, and best practices. Simple Mode: concise, high information density, and no redundant expression. It is suitable for scenarios such as quick response, operation guidance, and troubleshooting. Service Mode: patient, friendly, and positive. It is suitable for improving employee satisfaction and service reliability. |
| Preferred Style |  |  |

### Accuracy evaluation

The system provides the accuracy evaluation feature that allows you to evaluate the accuracy of Apsara Copilot. By configuring evaluation cases, evaluation datasets, and evaluation tasks, you can initiate automated accuracy evaluation and export a detailed evaluation report.

#### Evaluation case management

##### Create an evaluation case

This topic describes how to create an evaluation case.

**Prerequisites**

| Parameter | Description |
|---|---|
| Use Case Type | The type of the evaluation case. Set the value to rag. |
| Product | The cloud service to which the evaluation case belongs. |
| Question | The question of the evaluation case. |
| Answer | The answer to the question of the evaluation case. |

You are an operations administrator.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, choose **Apsara Copilot** > **Accuracy Evaluation**.
4. Click the **Evaluation Case Management** card.
5. On the **Evaluation Case Management** page, click **Add Use Case**.
6. In the **Add Evaluation Case** dialog box, configure the parameters.
7. Click **Add Use Case**.

##### Manage an evaluation case

| Operation | Description |
|---|---|
| View the evaluation case | Find the evaluation case and click View in the Actions column. In the Evaluation Case Details panel, you can view the evaluation case details, including the associated evaluation datasets. Note The evaluation case code can be copied with one click. To do so, move the pointer over the code and click the icon. An associated evaluation dataset can be disassociated from the current evaluation case. To do so, find the evaluation dataset in the list and click Disassociate in the Actions column. |
| Delete the evaluation case | i. Find the evaluation case and click Delete in the Actions. ii. In the message that appears, click OK. |

This topic describes how to manage an evaluation case after it is created. You can view and delete the evaluation case.

**Prerequisites**

You are an operations administrator. An evaluation case is created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, choose **Apsara Copilot** > **Accuracy Evaluation**.
4. Click the **Evaluation Case Management** card.
5. Manage the created evaluation case as needed.

#### Evaluation dataset management

##### Create an evaluation dataset

This topic describes how to create an evaluation set.

**Prerequisites**

You are an operations administrator by default. You have created evaluation cases.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.

| Configuration item | Description |
|---|---|
| Evaluation Dataset Type | Select the type of the evaluation set. The current version supports rag type only. |

3. In the left-side navigation pane, select **Apsara Copilot** > **Accuracy Evaluation**.
4. Click the **Evaluation Dataset Management** card.
5. On the **Evaluation Dataset Management** page, click **Create Evaluation Dataset**.
6. In the **Create Evaluation Dataset** dialog box, configure the evaluation dataset
information.

| Evaluation Dataset Name | Set a name for the evaluation set. |
|---|---|
| Evaluation Scenario | Select an evaluation scenario. The system supports Test Q&A and User Q&A. |
| Description | Optional. Enter a description for the evaluation set. |
| Select Evaluation Cases | i. Click Create Evaluation Dataset From Evaluation Cases. ii. Select cases. You can filter cases by User Case Code, Question, Product, and Reference Answer. After you set the filter conditions, click Search to apply the filters. iii. Click OK. You can also click Add All to add all cases to the evaluation dataset. |

| Operation | Description |
|---|---|
| View the evaluation dataset | Find the evaluation dataset and click View in the Actions column. On the Evaluation Dataset Use Case Management page, you can manage the evaluation cases in the dataset. |
| Modify the evaluation dataset | i. Find the evaluation dataset and click Modify in the Actions column. ii. In the Modify Evaluation Dataset panel, modify the Evaluation Dataset Name and Description parameters. iii. Click OK. |

7. Click **Create Evaluation Dataset**.

##### Manage an evaluation dataset

This topic describes how to manage an evaluation dataset after it is created. You can view, modify, and delete the evaluation dataset.

**Prerequisites**

You are an operations administrator. An evaluation dataset is created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, choose **Apsara Copilot** > **Accuracy Evaluation**.
4. Click the **Evaluation Dataset Management** card.
5. Manage the created evaluation dataset as needed.

| Delete the evaluation dataset | i. Find the evaluation dataset and click Delete in the Actions column. ii. In the message that appears, click OK. |
|---|---|

| Configuration item | Description |
|---|---|
| Task Name | Enter a name for the evaluation task. |
| Evaluation Task Type | Select an evaluation task type. The current version supports rag type only. |
| Evaluation Dataset | Select an evaluation set from the drop-down list. |
| Evaluation Type | Select Manual or Automatic. |
| Evaluator | When you select Manual for Evaluation Type, specify one or more evaluators. You can specify up to three evaluators. All specified evaluators must complete the evaluation. If any evaluator selects Completely Wrong as the evaluation result, the evaluation fails. |

#### Evaluation task management

##### Create an evaluation task

This topic describes how to create an evaluation task.

**Prerequisites**

You are an operations administrator by default. You have created an evaluation dataset.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Accuracy Evaluation**.
4. Click the **Evaluation Task Management** card.
5. On the **Evaluation Task Management** page, click **Create Evaluation Task**.
6. In the **Create Evaluation Task** dialog box, configure the evaluation task information.

| Evaluation Method | When you select Automatic for Evaluation Type, select an evaluation method. Select Ground Truth or No Ground Truth. |
|---|---|

**Manual evaluation task**

**Automatic evaluation task**

7. Click **Create Evaluation Task**.

**Note**

After you create an evaluation task, the system does not automatically start the task. You must click **Start Evaluation** in the **Actions** column to start the evaluation task.

##### Manage an evaluation task

This topic describes how to manage an evaluation task.

**Prerequisites**

You are an operations administrator by default. You have created an evaluation task.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the navigation pane on the left, choose **Apsara Copilot** > **Accuracy Assessment**.
4. Click the **Evaluation Task Management** card.
5. View the list of evaluation tasks. You can use the **Task ID**, **Evaluation Dataset**,
**Evaluation Type**, and **Status** filters to quickly find a specific task.

| Operation | Description |
|---|---|
| Perform manual evaluation | i. In the Actions column of the evaluation task, click Manual Evaluation. Note You can perform manual evaluation only on tasks whose Evaluation Type is Manual and whose status is Pending Manual Evaluation or In Progress. ii. On the Manual Evaluation page, click Evaluate in the Actions column for a use case. Note Click View in the Actions column to view the details of the evaluation results. |

6. Manage the created evaluation task as needed.

|  | iii. In the Evaluation Result Details panel, review the information to be evaluated. Then, in the Manual Evaluation section, set the Evaluation Result and Remarks. Note For Evaluation Result, you can select Completely Accurate, Partially Accurate, Completely Incorrect, or Not Evaluated. If you select Completely Incorrect, the evaluation fails. You must then select a reason from the Reason for Failure drop-down list below. Options include Unclear Question, Incomplete Reference Answer, Incomplete Content, Duplicate Use Case, or Other. |
|---|---|
| View the evaluation results | i. In the Actions column of the evaluation task, click View Results. Note You can view the results only when the task status is iv. Click Submit. If there are multiple use cases, you can click Completed. Submit and Switch to Next after you finish evaluating the current use case. ii. On the Evaluation Results page, view the evaluation results for the use cases. iii. Click View in the Actions column for a use case to expand its result details. |

| View the report | i. In the Actions column of the evaluation task, click the icon and select View Report. Note You can view the report only when the task status is Completed. ii. On the Evaluation Report page for the task, view the detailed evaluation and analysis report. |
|---|---|
| Delete the evaluation task | i. In the Actions column, click and select Delete. ii. In the message that appears, click OK. |
| Perform a re-evaluation | i. If the evaluation task fails, click Re-evaluate in the Actions column. ii. In the message that appears, click OK. |

| Configuration item | Description |
|---|---|
| Accuracy Rate Trend Analysis | Displays accuracy rate analysis as a line chart. You can switch betweenD ay Dimension or Month Dimension. |
| Question Classification Statistics | Displays question classification statistics as a column chart. You can switch between Day Dimension or Month Dimension. |

#### Accuracy rate analysis

View the accuracy status of Apsara Copilot.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Accuracy Evaluation**.
4. Click the **Accuracy Rate Analysis** card.
5. On the **Accuracy Rate Analysis** page, view **Accuracy Rate Trend Analysis**, **Question**
**Classification Statistics**, and **Data Details**.

| Data Details | Enter the start date and end date for your query to view detailed data within the specified time range. You can switch between Day Dimension or Month Dimension Click View Report in the Actions column of a detail entry to go to the evaluation report details page. Click above the list to download the detailed data to your local device. |
|---|---|

### Model configuration

Manage and configure your AI models, including large language models, embedding models, and rerank models.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Model Configurations**.
4. In the **Large Language Model (LLM)**/**Embedding Model**/**Rerank Model** section, click
**Add Model**.
5. In the **Add Model Configuration** dialog box, configure the model.

| Configuration item | Description |
|---|---|
| Model Name | Enter the display name of the model. |
| Model Code | Enter the code of the model, representing the unique ID of the model. |
| API Key | Enter the API key of the model. |
| Request URL | Enter the API request URL of the model. |
| Model Provider | Select a model provider. Options: Model Studio Dedicated Edition, Alibaba Cloud Model Studio, aibase, and openai. |
| Set as Default Model | Specify whether to set the model as the default model. |

6. Click **Save**.
7. Perform other related operations.

| Operation | Description |
|---|---|
| Edit the model | i. In the model card section, click Edit in the upper-right corner. ii. In the Edit Model Configuration dialog box, update the model configuration. Note You cannot modify the model name or model code. iii. Click Save. |
| Delete the model | i. In the model card section, click Delete in the upper-right corner. ii. Click OK. |
| Change the default model | In the model card section, click Set as Default Model at the bottom to change the default model based on business requirements. |

| Configuration item | Description |
|---|---|
| Knowledge Base Type | Select the type of knowledge base. The system supports Vector Knowledge Base and Graph Knowledge Base. Vector Knowledge Base: a production-grade vector database based on Milvus. Graph Knowledge Base: a knowledge base implementation based on LightRAG. |

### Knowledge base management

#### Create a knowledge base

Create vector and graph knowledge bases on the Knowledge Base Management page.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click **Create Knowledge Base**.
5. In the **Create Knowledge Base** dialog box, configure the knowledge base.

| Knowledge Base Name | Enter a name for the knowledge base. |
|---|---|
| Embedding Model | Select the embedding model used to convert text into vectors. Different models have different vector dimensions and semantic precision. You cannot change this setting after creation. |
| Default Chunking Policy | Select a document chunking policy. General: general chunking, suitable for most scenarios. QA: question-answer chunking, suitable for FAQ documents. Structure: structured chunking, suitable for long structured content. Custom: custom delimiter-based chunking, suitable for documents with fixed formats such as laws and regulations. |
| Chunk Size | Set this parameter when you select General, Structure, or Custom as the document chunking policy. Set the number of units contained in each independent segment (chunk) when splitting the original long text. |
| Chunk Overlap | Set this parameter when you select General, Structure, or Custom as the document chunking policy. Set the length of repeated content between two adjacent text chunks. In other words, the end of the previous chunk overlaps with the beginning of the next chunk. |
| Separator | Set this parameter when you select Custom as the document chunking policy. Define a series of priority rules to guide the system to split long text into appropriately sized chunks while preserving semantic integrity. Note The system supports escape characters such as \n (line break), \t (tab), and \r (carriage return). Separate multiple delimiters with commas (for example, \n,\t). Leave this field blank to disable pre-segmentation. |
| Description | Enter a task description for the knowledge base. The more detailed the description, the easier it is to retrieve the knowledge base accurately. |

6. Click **OK**.

#### Edit a knowledge base

You can modify the configuration when updates are available for a knowledge base.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click
in the upper-right corner of the target knowledge base card, and select **Modify**
**Knowledge Base**.
5. In the **Modify Knowledge Base** dialog box, update the knowledge base configuration. For
more information about configuration items, see Create a knowledge base.
6. Click **OK**.

#### Configure the chunking policy

Adjusting chunking parameters controls how the system splits text, which affects retrieval quality and document loading efficiency.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click
in the upper-right corner of the target knowledge base card and select **Configure**
**Chunking Policy**.
5. In the **Chunking Policy** dialog box, adjust the chunking policy for the knowledge base. For
detailed descriptions of chunking policies, see Create a knowledge base.

**Note**

The preset policies align with the followingRAGFlow chunking policies: General, QA, Book, and Laws. If you leave this parameter blank, the system uses the default policy of the knowledge base.
6. Click **OK**.

#### Delete a knowledge base

Delete any knowledge base you no longer need.

**Prerequisites**

The operater is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click
in the upper-right corner of the target knowledge base card and select **Delete**.
5. In the **Delete Knowledge Base** dialog box, enter the knowledge base name to confirm the
operation.
6. Click **OK**.

#### Import a file

Import files into a knowledge base.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of a knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, click **Import File**.
6. In the **Import File** dialog box, select or drag a file into the dashed box to upload it.

**Note**

Supported file types include txt, md, doc, docx, pdf, pptx, csv, xlsx, and html.
7. Click **OK**.

#### View file details

The file details page displays file preview and chunks information.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of a knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, click the file name to view its details.

#### Ingest files

After importing files, you can ingest them.

**Prerequisites**

The operator is an operations administrator by default. The file status is **Parsed**.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.

| Operation | Description |
|---|---|
| Ingest a single file | Click Ingest in the Actions column corresponding to the file. |
| Ingest multiple files at a time | i. Select multiple files that you want to ingest. ii. Click Batch Ingest below the file list. iii. In the Batch Ingest Chunking Policy dialog box, confirm or modify the chunking policy. iv. Click OK. |

2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of a knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, ingest files.
6. (Optional) Perform other related operations.
After ingesting a file, the file status changes to **Indexed**. You can download the file. If file ingestion fails, the file status changes to **Index Error**. You can retry the operation.

#### Delete an file

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of a knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, click **Delete** in the **Actions** column.
6. Click **OK**.

#### View the knowledge graph

View the generated knowledge graph in a graph-type knowledge base.

**Prerequisites**

The operator is an operations administrator by default. The knowledge base is of graph type.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of the knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, click
in the upper-right corner of the list.
6. On the **Knowledge Graph** tab, view the generated knowledge graph. If no knowledge
graph exists, click **Generate Now**.

**Note**

The knowledge graph displays nodes and their relationships. Enter a node name in the drop-down list at the top to search for and view the specific node. Click a node in the graph to display its description, network metrics, tags, and associations. Control the knowledge graph view. Click in the upper-right corner of the knowledge graph to zoom in. Click in the upper-right corner of the knowledge graph to zoom out. Click in the upper-right corner of the knowledge graph to enter fullscreen mode. Click in the upper-right corner of the knowledge graph to restore the default view.

#### View the mind map

View the generated mind map.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, select **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of a knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, click
in the upper-right corner of the list.
6. On the **Mind Map** tab, view the generated mind map.

**Note**

Click **Regenerate** above the mind map to regenerate the mind map. Enter a node name above the mind map to search by node. Control the display of the mind map. Enter a percentage in the upper-right corner of the mind map to adjust the display scale. Click in the upper-right corner of the mind map to zoom in. Click in the upper-right corner of the mind map to zoom out. Click in the upper-right corner of the mind map to enter full-screen mode. Click in the upper-right corner of the mind map to restore the default view.

#### Retrieval configuration and retrieval

**testing**

The Retrieve Testing tab supports retrieval configuration and retrieval testing.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.
3. In the left-side navigation pane, choose **Apsara Copilot** > **Knowledge Base**
**Management**.
4. Click the name of a knowledge base to go to its details page.
5. On the **Knowledge Base Details** page, click
in the upper-right corner of the list.
6. Configure retieval settings.
i. Click **Retrieval Configurations**. ii. In the **Retrieval Configurations** dialog box, set **Query Mode (query_mode)**,
**Retieved Entity Relationships (top_k)**, **Retrieval Chunks (chunk_top_k)**, and
**Enable Reranking (enable_rerank)**.

**Note**

Query mode supports **hybrid** or **mix**. iii. Click **OK**.
7. Perform retrieval testing. Enter search content in the text box and click **Search**.

**Note**

Query Mode: The right side displays the currently configured query mode. Advanced Keywords: advanced keywords extracted from the search content. Basic Keywords: basic keywords extracted from the search content. The section below displays the retrieved information.

### AI-assisted cloud resource

**management**

You can use custom configurations to better manage your cloud resources.

#### AI-assisted creation

Configure personalized scenarios for AI-assisted creation of cloud services.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Configurations**.

| Configuration item | Description |
|---|---|
| Cloud Service | Select a cloud service for AI-assisted creation. Currently, the system supports only Elastic Compute Service (ECS) Instance and Virtual Private Cloud (VPC). |
| Custom Scenario | Configure custom scenarios as needed for use during assisted resource creation. Add a scenario: Click Add Scenario to customize a scenario. You can select Enumeration Scenario, Scenario Description, or None. Delete a scenario: Click next to the scenario. Adjust the scenario order: Drag in front of a scenario to adjust its display order. Restore the preset scenario: Click Restore Preset Scenario, and the system automatically loads the default layout and scenario configurations. |

3. In the left-side navigation pane, select **Apsara Copilot** > **Auxiliary Cloud Resource**
**Management**.
4. Click the **AI-assisted Creation** tab.
5. Complete the AI-assisted creation configuration.
6. Click **Save**.

**Result display**

After you configure assisted creation for a cloud service, Apsara Copilot intelligently plans and assists users in creating resources based on personalized scenarios.

| Configuration item | Description |
|---|---|
| Change Service Configurations | Select the cloud product to upgrade or downgrade. Currently, only Elastic Computing Service (ECS) and Server Load Balancer (SLB) are supported. |
| Rule Template | Select a rule template. If the predefined templates do not meet your needs, customize a rule template. |
| Rule Description | Displays the details of the selected rule template. |

#### AI-assisted configuration change

You can configure rules for the AI-assisted configuration change of cloud products. These rules are used to analyze and provide recommendations when you upgrade or downgrade a cloud product.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, select **Configurations**.
3. In the navigation pane on the left, select **Apsara Copilot** > **Auxiliary Cloud Resource**
**Management**.
4. Click the **AI-assisted Configuration Change** tab.
5. Configure the settings for assisted Upgrade/Downgrade.

| Configuration item | Description |
|---|---|
| Rule Name | Enter a name for the rule. The name must be unique. |
| Monitoring metrics | Displays the monitoring metrics supported by the current cloud product. These metrics are used for monitoring analysis and in the rule description. |
| Rule Description | Create an analysis rule for the cloud resource. This rule is used for assisted resource upgrade/downgrade. You can enter a description in Generate rules with AI and then insert the generated result. |

6. Click **Apply**.

**Customize a rule template**

1. On the **AI-assisted Configuration Change** tab, click **Manage Rules** to the right of **Rule**
**Template**.
2. On the **Manage Rules** panel, click
.
3. Configure the rule.

| Operation | Description |
|---|---|
| Edit a rule template | i. On the Manage Rules panel, select a rule and click Modify. Note Predefined rule templates cannot be edited. ii. Update the rule name and description. iii. Click Save. |
| Delete a rule template | On the Manage Rules panel, select a rule and click Delete. Note Predefined rule templates cannot be deleted. |

4. Click **Save**.
5. You can perform other operations on rule templates.

**Results**

After configuring the AI-assisted configuration change for a cloud product, Apsara Assistant uses the applied rules to provide recommendations during an upgrade or downgrade.

## Application of Apsara

**Copilot**

### Apsara Copilot chats

Apsara Copilot allows users to ask the platform questions about cloud services in natural language, consult AI for information, and engage in intelligent chats with AI.

**Prerequisites**

The user, as an operations administrator, has enabled the display of the AI assistant in the Apsara Uni-manager Management Console under **Configurations** > **Apsara Copilot** >
**Custom Settings**.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. Click
in the top navigation bar or floating menu to enter Apsara Copilot.
3. In the **Apsara Copilot** dialog box, enter your question and click
.

| Scenario | Description |
|---|---|
| Knowledge Q&A | Provides accurate answers and guidance for usage-related questions regarding cloud service recommendations, feature operations, limitations, and best practices. |
| Resource Search | Precisely locates target resources, provides detailed information, and enables viewing of associated resources. |

| Resource Operation | Supports operations such as creating, modifying, and deleting cloud resources to simplify your resource management process. |
|---|---|
| Bill Analysis | Analyzes your cloud resource usage costs, generates detailed expense reports, and provides optimization suggestions to reduce overall spending. |
| Resource Analysis | Tracks cloud resource usage, including utilization and performance metrics, to help you fully understand resource status and optimize resource allocation. |
| Code Generation | Automatically generates code samples in multiple programming languages for OpenAPI and Terraform based on your requirements, improving development efficiency and code quality. |

**Note**

Apsara Copilot supports multiple models. You can switch between different models when asking questions. If the selected model supports deep thinking, you can enable or disable deep thinking mode. Enter "/" in the input box to add a slot, then select the corresponding slot value based on the slot type. Click in the input box to expand the command center. The command center provides a complete list of common Apsara Copilot command examples for quick instruction sending. Enter keywords in the input box under the command center to quickly find related command questions. View recommended questions by command type and trigger them with one click. Click in the input box to choose whether to enable MCP and intranet search. After enabling MCP and selecting connected cloud services, you can invoke MCP services of those cloud services. The intranet search option appears here only when you have enabled its display in the custom settings of Apsara Copilot.
4. After Apsara Copilot responds, you can perform the following operations.
: Like — indicates approval of the response. : Dislike — indicates disapproval of the response. : Copy — copies the response content. : Export response — exports the generated response.

| Related operation | Description |
|---|---|
| New chat | Click above the dialog box to start a new chat. |
| Chat history | Click above the dialog box to view chat history. |
| Full screen | Click above the dialog box to display the Apsara Copilot dialog box in full screen. |
| Settings | Click above the dialog box to select whether to enable word selection. When enabled, left-click to highlight content on the console page, then click Consult Apsara Copilot to automatically trigger Q&A for the selected content. |
| Homepage | Click above the dialog box or click Assistant Introduction in the dialog box to go to the Apsara Copilot homepage. |
| Close | Click above the dialog box to close the Apsara Copilot dialog box. |
| Help documentation | Click Documentation in the dialog box to view Apsara Copilot help documentation. |

**Related operations**

### Perform text-selection Q&A

After you enable text-selection Q&A and select text on a console page, you can trigger Apsara Copilot to answer questions about the selected content.

**Prerequisites**

Text-selection Q&A is enabled for Apsara Copilot.

**Note**

To enable the feature, click the icon in the upper-right corner of the Apsara Copilot pane and turn on Enable Word Selection.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. Click and drag to select text on a console page and select Consult Apsara Copilot to send
the selected text to Apsara Copilot.
3. Apsara Copilot automatically searches for answers.

### AI-based intelligent analysis

Apsara Copilot provides intelligent data querying and data insights capabilities for AI-based intelligent analysis scenarios. For detailed operations of AI-based intelligent analysis, see the **Data analysis** > **Custom**
**analysis** > **Intelligent analysis** section in Apsara Uni-manager Management Console User
Guide.

### AI-based bill analysis

Billing data is complex and voluminous. Users struggle to identify underlying trends or potential issues from raw numbers. Apsara Copilot provides AI-based bill analysis capabilities that deliver multi-dimensional insights into billing data. This helps platform users understand resource usage and cost patterns more quickly and efficiently, enabling them to control expenses effectively. Simultaneously, it offers intelligent analytics for platform operators— including anomaly detection in bill fluctuations and trend forecasting—to ensure billing accuracy and optimize operational strategies for revenue growth. For detailed operations of AI-based bill analysis by product, see the **Bill management** > **AI-**
**based bill analysis by product** section in Apsara Uni-manager Management Console User
Guide.

**AI-based bill Aanalysis by organization**

For detailed operations of AI-based bill Aanalysis by organization, see the **Bill management**
> **AI-based bill analysis by organization** section in Apsara Uni-manager Management
Console User Guide. AI-based bill analysis by bill detail supports AI parsing of daily and hourly billing details. For detailed operations, see the **Bill management** > **AI-based bill analysis by bill detail** section in Apsara Uni-manager Management Console User Guide.

**Daily Details**

**Hourly Details**

### AI billing rule analysis

Apsara Copilot provides AI analysis for billing rule scenarios. For detailed operations of AI billing rule analysis, see the **Pricing** > **AI billing rule analysis** section in Apsara Uni-manager Management Console User Guide.

| Item | Description |
|---|---|
| AI Assistant Core Metrics | Displays core data for the AI assistant, including Comprehensive Score, Daily Active Users, and Total Conversations. Note Comprehensive score is a composite metric that measures the overall service quality of Apsara Copilot. The system calculates this score based on three dimensions: user satisfaction, performance response, and request success rate. This score reflects the quality of service and user experience during actual usage. |
| AI Assistant Feature Usage | Displays usage data for scenario-based features such as Intelligent Q&A, Knowledge Coverage, Intelligent Analysis, AI-assisted Operations, Code Generation, and MPC Calls. |
| AI Assistant Performance Response | Displays core performance data for the AI assistant, including TTFT (Time To First Token) and Average Generation Speed. |
| AI Assistant Resource Consumption | Displays resource consumption data for the AI assistant, including Consumed Tokens and Model Inference Latency. |
| AI Assistant License Usage | Displays license usage for the AI assistant, including Standard Agent, Resource Management Agent, Operations Management Agent, and Data Insight Agent. |

## Apsara Copilot operations

**analytics**

Apsara Copilot provides an operations analytics dashboard to help customers better monitor its usage and evaluate business effects.

**Prerequisites**

The operator is an operations administrator by default.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, select **Home**.
3. Click the **AI + Operation** tab to view metric data for **last week** and **last month**.

## View operation logs

This topic describes how to view the operation logs of Apsara Copilot.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Operation Audit** > **Operation Log**.
4. On the **Operation Log** page, configure filter conditions such as Organization, Product Type,
Resource Type, Event Type, Resource ID, Source IP, Event ID, and Start/End Time, and then click **Search**.

**Note**

Select **Apsara Uni-manager** from the Product Type drop-down list and **Apsara**
**Copilot** from the Resource Type drop-down list.
5. View the displayed operation logs.
6. Find the operation log whose details you want to view and click **View** in the **Details**
column. dix

## Appendix

### Log in to the Apsara Uni-

**manager Management Console**

This topic describes how to log in to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

**Note**

You can click the current language in the upper-right corner to switch to another language.
2. Enter your username and password.
dix

**Note**

Obtain the username and password from an operations administrator. If you log in to the Apsara Uni-manager Management Console for the first time, you must follow the on-screen instructions to change the password of your account. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is the first time that you log in to the Apsara Uni-manager Management**

**Console after MFA is forcefully enabled by the administrator.**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For information about how to enable MFA and bind an MFA device, see Manage MFA.

**What to do next**

**Forget password**

1. If you forget the login password, click **Forgot Password** below the Password field.
2. On the Forgot Password page, configure the **Account Name** and **Email Address**
parameters, specify the verification code, and then click **Confirm**. dix

**Note**

You can use the username of your account and the email address that was used to create the account. The system sends a link for resetting the password to the email address that you specify.
