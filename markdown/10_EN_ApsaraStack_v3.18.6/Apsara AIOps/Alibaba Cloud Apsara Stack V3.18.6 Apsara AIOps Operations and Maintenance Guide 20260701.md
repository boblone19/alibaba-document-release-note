---
title: "Apsara AIOps Operations and Maintenance Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 22
source_pdf: "8eb32685fdfd3230_Alibaba Cloud Apsara Stack V3.18.6 Apsara AIOps Operations and Maintenance Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%BB%B4%E5%B0%8F%E6%99%BA/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20AIOps%20Operations%20and%20Maintenance%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Apsara AIOps Operations and Maintenance Guide 20260701

## Table of Contents

- 1 Logon to AIOps Management Console
- 2 Application management
- 3 MCP Management
- 4 Knowledge base
- 5 System Settings
  - 5.1 Model management
- 6 Common faults and solutions
- 7 High-risk operations

Management Console

## 1 Logon to AIOps Management Console

**Management Console**

This topic describes how to log on to the AIOps Management Console.

**Prerequisites**

The endpoint, username, and password of the Apsara Uni-manager O&M console are obtained from the deployment personnel or administrator. The endpoint of the Apsara Uni-manager Operations console is in the format of region-id .ops.console. intranet-domain-id. The Chrome browser (recommended) is available.

**Procedure**

1. Open the browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations console and
press the Enter key. Management Console

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, make sure that your password meets the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password must be 10 to 20 characters in length.

4. Click **Agree and Log On**.
5. In the top navigation bar, choose**Platform Operation > Management and Control**
**Service O&M > AIOps Management Console**.

## 2 Application management

Centrally create, configure, and manage Q&A and process orchestration intelligent applications to implement unified control over the entire lifecycle of AI applications.

**Create an application**

1. Log on to the AIOps Management Console.
2. In the left-side navigation pane, click **Application Management**.
3. Click **Create Application**.
4. Set the following parameters and click **OK**.

| Parameters | Parameter description |
|---|---|
| Application Code | Enter the application code. |
| Application Name | Enter an application name. |
| Application type | Select an application type. dialogue type Process orchestration |
| Application Description | Enter the description of the application, such as the application scenario and purpose. |
| Application introduction | Enter an introduction to the application, which is displayed on the smartphone homepage. |

**View applications**

1. On the **Applications** page, you can view all applications.
2. You can specify **All**, **Built-in**, or **User-created**. You can also search by name.
3. The application card displays the basic information of the application, including
**Application Name**, Application Source, **Status**, **Application Type**, **Created By**, and
**Created At**.

**Application Details**

1. On the **Application Management** page, click the name of the application that you want to
manage. The Application Details page appears.
2. You can perform the following operations in the upper-right corner of the Application
Details page.

| Application Type | Operation |
|---|---|

| Process orchestration | Figure Operations > Import Task Flow: allows you to import task flows. Figure Operations > Export Task Flow: allows you to export task flows. Save: After you update the information about the application node, you can save it. Verification: The process is verified after the application node information is updated. Debug: You can debug the application after you update the node information. You can also copy, export, and view logs of the debugging response. Publish: After you update the node information, the node is published. |
|---|---|
| dialogue type | Save: Save the updated application. Publish: The application is published after it is updated. |
| a2a |   |

3. On the **Application Debugging** tab, you can configure the following application settings.

| Application Type | Description |
|---|---|
|   | The task flow of the application is orchestrated on the canvas on the right. Start: The start node is the starting point of the entire process and marks the start of the process. Required nodes: LLM: Used for Natural Language Processing and generation tasks. Leverage large language models for text generation, question answering, dialogue, reasoning, or other natural language-related tasks. Reply: Used to produce output, usually to send messages or results to users or external systems. Generates and sends responses, such as in-process output, final result output, status updates, or notifications. The processing results can be fed back to the caller or other systems. Context: knowledge base: Used to access and process information or data stored in the knowledge base. A knowledge base is a structured storage mechanism for holding and organizing various types of information (such as documents, images, and diagnostic data) so that it is easy to find and use. Information retrieval is performed to find and extract relevant information from knowledge base, such as answering a user's query and finding documents or data records. Plug-ins: Code execution: used to execute custom code or scripts in a process. Handle complex logic or specific tasks, and implement flexible feature extensions through programming, such as data computing and business rule judgment. |

| Process orchestration | Tool: used to call external tools, services, or APIs. Performs specific functions, such as data processing, invoking external services or interfaces, and file operations, enabling processes to integrate multiple functions and services. MCP: The MCP node is used to add an MCP service that already exists in the MCP management. Application: The application node is used to reference and use an application that has been built as part of a process. Reuse built processes or modules to ensure the consistency of code or logic, reduce repetitive work, and improve efficiency. Manual intervention: used to pause during process execution to implement user confirmation or user information supplement input. Http: used to send customized HTTP requests to specified network addresses to implement seamless integration with various external services. Logic: |
|---|---|
|   | Conditional Judgment: used to select branches based on specific conditions or logic. Problem understanding: Intent recognition: used to recognize user intents and implement subsequent process nodes based on different user intents. Conversion: Variable assignment: assigns variables in the workflow to global variables for temporary storage and can be continuously referenced in subsequent conversations. Variable aggregation: used to aggregate and process multiple variables or data points. Integrate data sources and perform data aggregation, calculation, or conversion for subsequent processing and use. Variable aggregation nodes are not variable combinations. By default, the last variable of the multi-branch node variable is not empty. Execution: Loop: Used to provide a local process to execute a loop step on a pre-process array type variable until all results are output. End: The end node is the end point of the entire process and marks the stop of the process. |

| dialogue type | Prompt: Enter the content of the prompt. You can adjust the content of the prompt to guide the chat direction of the model. The prompt is fixed at the beginning of the context. Variables can be used:[data] is the information known in the carrying knowledge base;[question] is the question asked by the user. Model Service: Click Model and Surprise Value. The value of Surprise Value is a floating-point number (0,1]. A higher value will make the output more random, while a smaller value will make the output more certain. knowledge base: Supports adding knowledge base documents as contexts. Click Add to add a knowledge base document. Click Create knowledge base in the upper-right corner to go to the knowledge base page. For more information, see knowledge base. Click to delete the added knowledge base document. MCP: Click Add to add an MCP. You can search for an MCP by name. Click to delete the added MCP. Debugging preview: supports debugging of dialog-based applications and predicts the accuracy of applications. You can also copy, export, and view logs of the debugging response. |
|---|---|
| a2a |   |

4. On the **Debugging Records** tab, view the debugging records of the application.
The debugging record list includes **the first session information** and **session**
**creation time**.
Find the debugging record that you want to view and click **View Details** in the **Actions** column.
5. On the **Release Management** tab, you can view the release records of the application and
manage terminals. On the **Terminal Management** page, you can go to the terminal page or copy the link of the terminal page. On the **Release Records** tab, you can view the release records, including **Version**,
**Version Alias**, **Version Description**, and **Release Time**.

**Related operations**

**Edit an application**

1. On the **Application Management** page, find the application that you want to manage and
click
**> Edit** in the Actions column.

> **Note:** Platform built-in applications do not support editing.

2. In the dialog box that appears, modify the application information and click **OK**.

**Delete an application**

1. On the **Application Management** page, find the application that you want to delete and
click
**> Delete** in the Actions column.

> **Note:** The built-in applications of the platform cannot be deleted.
> This operation is irreversible, please operate with caution!

2. In the message that appears, click **OK**.
nt

## 3 MCP Management

The built-in MCP Server can be viewed for applications.

**Procedure**

1. Log on to the Big Model Management · AIOps console.
2. In the left-side navigation pane, click **MCP Management**.
3. You can view all built-in MCP servers, including the name, **version**, and **description**. You
can also search by name.
4. Click the name of the MCP instance to go to the MCP details page. You can obtain the **Basic**
**Description** and **Tools**.

## 4 Knowledge base

You can create, view, and delete user-created knowledge base and view documents in preset knowledge base.

**Folder**

Before you create a knowledge base, you can perform the following operations on the folder:

**Create a folder**

1. Log on to the AIOps Management Console.
2. In the left-side navigation pane, click **knowledge base**.
3. On the **User-created** tab, click **Create Folder**.
4. Enter a name in the **Folder Name** field and click **OK**.

**Edit a folder**

1. Click the
icon corresponding to the target folder.
2. In the dialog box that appears, modify the **Folder Name** and click **OK**.

**Delete a folder**

1. Click the
icon corresponding to the target folder.
2. In the dialog box that appears, click **Delete**.

> **Note:** After you delete a folder, all knowledge base in the folder are moved to the default folder. Exercise caution when you delete the folder.

**Create knowledge base**

1. Log on to the AIOps Management Console.
2. In the left-side navigation pane, click **knowledge base**.
3. Click **Create knowledge base** or click the
icon in the Actions column.
4. Set the following parameters and click **OK**.

| Parameters | Parameter description |
|---|---|
| Name | Enter the knowledge base name. |
| Description | Enter a description for the knowledge base. |
| Embedding model | Select an embedding model. |
| Folder | Select the folder to which the new knowledge base belongs. |

**View knowledge base**

1. On the **knowledge base** page, you can view all **user-created** or **built-in** knowledge base.
2. The knowledge base allows you to search by name. The knowledge base information
includes the name, **description**, **creator**, and **creation time**.

**knowledge base Details**

**View knowledge base details**

1. On the **knowledge base** page, click the name of the target knowledge base to go to the
knowledge base details page.
2. You can view the documents in the knowledge base, including the document **name**, **data**
**size**, **processing status**, **segmentation method**, and **upload time**. You can also search
for a document by file name.

**Add a document**

1. On the **knowledge base** page, click the name of the target knowledge base to go to the
knowledge base details page.
2. Click **Add Document**.
3. In the **Upload File** step, click or drag the file to upload it to the dotted box. After the file is
uploaded, click **Next**.

> **Note:** Support doc,docx,pdf,txt,md,html,xls,xlsx,csv and other types of files.

4. In the **Segment&Cleansing** step, select and configure the document segmentation
parameters. Intelligent segmentation: the optimal segmentation method for common documents. The document is segmented based on the segment identifier. If the maximum segment length is exceeded, the document is processed based on the maximum segment length and the overlapping length of the segments. Parent-child segmentation: A two-layer parent-child segmentation structure is used to balance retrieval accuracy and context information. The parent block is used to provide context, and the child block is used for precise retrieval.
5. Click **Preview** to check whether the document is segmented as expected. Then, click **Next**.
6. In the **Data Processing** step, wait until the **Processing Status** of the file is **Data**
**Processable** and click **OK**.

**Segmentation Configuration**

1. On the knowledge base details page, find the target document and click **Segment**
**Configuration** in the **Actions** column.
2. In the **Segment&Cleansing** step, select and configure the document segmentation
parameters.
3. Click **Preview** to check whether the document is segmented as expected. Then, click **Next**.
4. In the **Data Processing** step, wait until the **Processing Status** of the file is **Data**
**Processed** and click **OK**.

**Delete a document**

1. On the knowledge base details page, find the document that you want to delete and click
**Delete** in the **Actions** column.
2. In the message that appears, click **OK**.

**Download a document**

1. On the knowledge base details page, select the target document.
2. Click **Download** below the list to download the document to your computer for viewing.

**Edit knowledge base**

1. Click
**> Edit** in the Actions column corresponding to the target knowledge base.

> **Note:** Platform built-in knowledge base do not support editing.

2. In the dialog box that appears, modify the parameters and click **OK**.

**Delete knowledge base**

> **Note:** Platform built-in knowledge base cannot be deleted.
> Deleted can not be withdrawn, please operate with caution!

1. Click
**> Delete** in the Actions column corresponding to the target knowledge base.
2. In the dialog box that appears, click **Delete**.

## 5 System Settings

### 5.1 Model management

Supports displaying built-in models and configuring external inference services to implement unified management and flexible expansion of model services.

**Model Type**

LLM: the inference model. The default inference model is used by the application. This default inference model is also used by the Q&A result generation and further questioning. Embedding: the default embedding model of the knowledge base, which is used to import and retrieve knowledge base. Switching models will cause the existing data vectors to not match and may cause the retrieval to fail. Do not change them at will. Rerank: The reordering model reorders the knowledge base-based documents and the semantic matching of user questions to optimize the original sorting results.

**Procedure**

1. Log on to the AIOps Management Console.
2. In the left-side navigation pane, choose **System Settings > Model Management**.
3. In the **Model List** section, you can view the **Built-in Model Services**, including the model
type, number, and name.

> **Note:** **Built-in Model Service** does not allow you to add, edit, or delete models.

4. In the lower part of the page, you can view and configure the external inference service.
Add model a. Click **Add Model**. b. Set the following parameters and click **OK**.

| Parameters | Parameter description |
|---|---|
| Model Type | Select the type of the new model. LLM Embedding Rerank |
| Model | Enter a model name. |
| API Key | Enter an API Key. |
| API endpoint URL | Enter the API endpoint URL. |

| Model name in the APl endpoint | Enter the model name from the API endpoint. |
|---|---|
| Vector dimension | This field takes effect only when you set Model Type to Embedding. The dimension of the input vector. |

API-KEY settings a. Click **API-KEY Settings**. b. In the dialog box that appears, configure the **API Key** and click **OK**. Edit Model a. Click **Edit** in the Actions column corresponding to the target model. b. In the dialog box that appears, modify the model parameters and click **OK**.

> **Note:** You cannot change the **Model Type**.

Delete a model a. Click **Delete** in the Actions column corresponding to the target model. b. In the message that appears, click **OK**.

> **Note:** Deleted can not be withdrawn, please operate with caution!

5. In the upper-right corner of the page, click **System Model Settings**.
6. Configure the default models of built-in applications and user-created applications. You can
configure the **Inference Model**, **Embedding Model**, and **Rerank Model** parameters. Then, click **OK**. and solutions

## 6 Common faults and solutions

**solutions**

**Intent recognition error, a solution to troubleshoot the**

**problem, the results were sent to the operation and**

**maintenance information query intelligent body, resulting in**

**the query can not be found.**

A: The current use of LLM-based intent recognition, a combination of user questions, context, and the intelligent body's own description of itself, allowing LLM to determine which intelligent body the user's demands should be given. However, the scheme of LLM intent recognition cannot cover all cases, and there will be overlapping responsibilities between intelligences, resulting in unstable LLM answers, so there will be some boundary cases that fail to be dispatched.

**MCP-dependent smart body call failed: tool not found or not**

**authorized?**

The tool cannot be found: The current MCP is divided into two types: system built-in (such as obtaining the current time) and ASO OPS API. The OPS API is implemented and registered as the OPS API by all business parties and is released with ASO. If the AIOPS and ASO release versions do not match, an error will be reported that the tool cannot be found. No permission: when the smart body calls MCP Tool, it uses ak/sk when the user logs in to ASO. if the user role does not have permission to some required OPS API, there will be permission problems.

**Reply: Sorry, this question cannot be answered. I focus on the**

**cloud platform O&M field. Please feel free to ask relevant**

**questions at any time.**

A: Insufficient knowledge base data. There are always some questions and answers that are beyond the system's capabilities. The interaction with this part should be that Yunwei Xiaozhi informs the user of his own capabilities and guides the user to ask questions about knowledge within his own capabilities. At the same time, according to user demands, expand the knowledge base. On-site or users can also upload private domain knowledge expansion knowledge base. ons

## 7 High-risk operations

This topic describes the high-risk operations of Apsara AIOps to help users better estimate and avoid related operational risks.

| High-risk operations | Impact | Recovery plan |
|---|---|---|
| Delete entire intelligences | All the data of the smart body will be deleted. | Unrecoverable |
| Delete entire knowledge base | All knowledge base data will be deleted | Unrecoverable |
