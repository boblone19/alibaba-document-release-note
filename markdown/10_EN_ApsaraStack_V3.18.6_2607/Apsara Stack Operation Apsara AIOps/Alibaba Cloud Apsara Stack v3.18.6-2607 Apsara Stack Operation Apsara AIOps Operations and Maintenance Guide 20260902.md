---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps Operations and Maintenance Guide 20260902"
product_version: "V3.18.6_2607"
doc_version: "20260902"
pdf_pages: 29
source_pdf: "d26e6798bf4e3495_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps Operations and Maintenan"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20Stack%20Operation%20Apsara%20AIOps%20Operations%20and%20Maintenance%20Guide%2020260902.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps Operations and Maintenance Guide 20260902

## Table of Contents

- 1 Log in to AIBase Management Console
- 2 Application management
- 3 MCP management
- 4 Knowledge base
- 5 Corpus system
  - 5.1 Corpus tasks
- 6 System Settings
  - 6.1 Model management
- 7 Common faults and solutions
- 8 High-risk operations

Management Console

## 1 Log in to AIBase Management Console

**Management Console**

This topic describes how to log in to the AIBase Management Console.

**Prerequisites**

You have obtained the endpoint, username, and password of the Apsara Uni-manager Operations Console from the deployment engineer or administrator. The endpoint of the Apsara Uni-manager Operations Console follows the regionid.ops.console.intranet-domain-id format. The Google Chrome browser (recommended) is available.

**Procedure**

1. Open a browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console and
press Enter.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter the correct username and password.
Management Console

> **Note:** Obtain the username and password for logging in to the Apsara Uni-manager Operations Console from the deployment engineer or administrator.
> If you enter an incorrect password for three consecutive times, the system enables image Completely Automated Public Turing Test to tell Computers and Humans Apart (CAPTCHA) verification. After five consecutive incorrect attempts, the account will be locked. Contact the administrator to unlock it.
> When you log in to the Apsara Uni-manager Operations Console for the first time, you must change the password of the login account. Follow the prompts to complete the password change.
> To improve security, the password must:
> contain uppercase and lowercase letters.
> contain digits (0 to 9).
> contain special characters, such as exclamation marks (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).
> be 10 to 20 characters in length.

4. Click **Log In**.

> **Note:** If a privacy policy has been configured, click **Agree to Privacy Policy and Log In** .

5. In the top navigation bar, choose **Platform Operation > Management and Control**
**Service O&M > AIBase Management Console**.
agement

## 2 Application management

You can centrally create, configure, and manage Q&A and process-orchestrated intelligent applications, enabling unified control over the entire lifecycle of AI applications.

**Create an application**

## 1 Log in to AIBase Management Console.

2. In the left-side navigation pane, select **Application Management**.
3. Click **Create an application**.
4. Configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Application Code | Enter the application code. |
| Application Name | Enter an application name. |
| Application Type | Select an application type. Dialogue type Process Orchestration |
| Platform | Select the platform to which the application belongs. ASCM ASO |
| Product | Select the product to which the application belongs. |
| Application Description | Enter a description for the application, including its scenario and purpose. |
| Application Introduction | Enter an introduction for the application. The content appears on the agent homepage. |

agement

**View applications**

1. On the **Application Management** page, you can view all applications.
2. You can display applications by **All**, **Built-in**, or **User-created**, and filter applications by a
combination of **Application Name**, **Platform**, and **Product** to find the target application.
3. Each application card displays basic information, including the **application name**, source,
**status**, **application type**, **platform**, **creator**, and **creation time**.
agement

**Application details**

1. On the **Application Management** page, click the name of the target application to go to
the application details page.
2. In the upper-right corner of the application details page, you can perform the following
operations.

| Application type | Action |
|---|---|
| Process orchestration | Graph operation > Import task flow: Import a workflow. Graph operation > Export task flow: Export a workflow. Save: Update the application node information and save the changes. Verification: Update the application node information and validate the workflow. Debugging: Update the application node information and debug the content. You can also copy or export the debug responses, and view the logs. Publish: Update the application node information and publish the application. Note Built-in applications do not support operations such as Import task flow, Save, Verification, and Publish. |
| Dialogue type | Save: Update the application content and save the changes. Publish: Update the application content and publish the application. |
| a2a |   |

agement
3. On the **Application debugging** tab, you can configure the following application content.

| Application type | Description |
|---|---|
| Process orchestration | Orchestrate the task flow of the application on the right-side canvas. Start: The start node is the starting point of the entire workflow and marks the launch of the workflow. Required node: LLM: Perform natural language processing and generation tasks. Use large language models (LLMs) for text generation, question answering, dialogue, reasoning, or other natural language-related tasks. Reply: Generate output, typically to send messages or results to users or external systems. Generate and send responses such as intermediate output, final results, status updates, or notifications to provide feedback to callers or other systems. Context: Knowledge base: Access and process information or data stored in a knowledge base. A knowledge base is a structured storage mechanism that saves and organizes various types of information, such as documents, images, and diagnostic data, to make the information easy to find and use. Perform information retrieval to find and extract relevant information from the knowledge base, such as answering user queries or locating documents and data records. Plug-in: Tool: Call external tools, services, or APIs. Perform specific functions such as data processing, calling external services or interfaces, and file operations to enable the workflow to integrate multiple functions and services. MCP: The Model Context Protocol (MCP) node adds an MCP service that already exists in MCP management. Application: The application node references and uses an existing application as part of the workflow. Reuse existing workflows or modules to ensure code or logic consistency, reduce redundant work, and improve efficiency. Manual intervention: Pause the workflow execution to allow user confirmation or supplementary input from the user. HTTP: Send customized HTTP requests to a specified network address to achieve seamless integration with various external services. Logic: Conditional judgment: Select branches based on specific conditions or logic. Problem understanding: Intent recognition: Identify user intents and execute subsequent workflow nodes based on different user intents. Conversion: Variable assignment: Assign variables within the workflow to global variables for temporary storage and continuous reference in subsequent conversations. |

agement

|   | Variable aggregation: Collect and process multiple variables or data points. Integrate data sources to perform data summarization, calculation, or conversion for subsequent steps. The variable aggregation node does not combine variables. By default, it takes the last non-empty variable from multi-branch nodes. Execute: Loop: Provide a local workflow that executes loop steps on an array- type variable from a preceding workflow until all results are output. End: The end node is the endpoint of the entire workflow and marks the termination of the workflow. |
|---|---|
| Dialogue type | Prompt words: Enter prompt content. By adjusting the prompt content, you can guide the chat direction of the large model. The prompt is fixed at the beginning of the context. You can use variables: [data] carries known information from the knowledge base; [question] is the question raised by the user. Model service: Click to configure the Model and Surprise value (temperature). The value range of surprise value is a floating-point number in the range (0, 1]. A higher value makes the output more random, while a lower value makes the output more deterministic. Knowledge base: Add knowledge base documents as context. Click Add to add knowledge base documents. Click Create a knowledge base in the upper-right corner to go to the knowledge base page. For more information, see Knowledge base. Click to delete added knowledge base documents. MCP: Click Add to add an MCP service. You can search by name. Click to delete added MCPs. Debug preview: Debug dialogue-type applications and predict the accuracy of the application. You can also Copy or Export Answers for debug responses, and view Logs. |
| a2a |   |

4. On the **Debug Records** tab, view the debug records of the application.
The debug record list includes the **First Conversation Message** and **Conversation**
**Creation Time**.
Click **View details** in the **Operation** column of the target debug record to view the conversation details.
5. On the **Data Dashboard** tab, view the monitoring statistics of the application within the
target time range.
**Total number of users** and the trend chart within the time range.
**Number of questions** and the trend chart within the time range.
**Total tokens** and the trend chart within the time range.
6. On the **Release Management** tab, view the terminal management and release records of
the application. agement Under **Terminal Management**, you can go to the terminal interface or copy the terminal interface link. Under **Release record**, view the release record list, including the **version number**,
**version alias**, **version description**, and **release time**.

**Related operations**

**Edit an application**

1. On the **Application Management** page, click
**> Edit** for the target application.

> **Note:** The platform does not support editing built-in applications.

2. In the pop-up dialog box, modify the application information and click **OK**.

**Delete an application**

1. On the **Application Management** page, click
**> Delete** for the target application.

> **Note:** The platform does not support deleting built-in applications.
> This operation is irreversible. Proceed with caution.

2. In the pop-up dialog box, click **OK**.
nt

## 3 MCP management

View the built-in MCP servers on the platform for use in your applications.

**Procedure**

1. Log in to the AIBase Management Console.
2. In the left-side navigation pane, choose **MCP Management**.
3. View all built-in MCP servers on the platform, including the name, **Platform**, **Version**, and
**Description**.
You can filter MCP servers by name and **Platform** to find the target server.
4. Click the name to go to the MCP details page and view the **Basic description** and **Tool**
**List**.
nt

## 4 Knowledge base

You can create, view, and delete custom knowledge bases, and view documents in preset knowledge bases.

**Prerequisites**

You have configured an embedding model.

**Folders**

Before creating a knowledge base, you can perform the following operations on folders.

**Create a folder**

2. In the left-side navigation pane, select **Knowledge Base**.
3. On the **User-created** tab, click **Create a folder**.
4. Enter a **folder name** and click **OK**.

**Edit a folder**

1. Click the
icon next to the target folder.
2. In the dialog box that appears, modify the **folder name** and click **OK**.

**Delete a folder**

1. Click the
icon next to the target folder.
2. In the pop-up dialog box, click **Delete**.

> **Note:** After you delete a folder, the system moves all knowledge bases in the folder to the default folder. Proceed with caution.

**Create a knowledge base**

1. Log in to AIOps Management Console.
2. In the left-side navigation pane, select **Knowledge Base**.
3. Click **Create a knowledge base**, or click the
icon next to the target folder.
4. Configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter a name for the knowledge base. |
| Description | Enter a description for the knowledge base. |
| Embedding model | Select an embedding model. |
| Folder | Select the folder to which the new knowledge base belongs. |

**View knowledge bases**

1. On the **Knowledge Base** page, you can view all **user-created** and **built-in** knowledge
bases.
2. You can search for knowledge bases by name. The knowledge base information includes
the name, **description**, **creator**, and **creation time**.

**Knowledge base details**

**Add a document**

1. On the **Knowledge Base** page, click the name of the target knowledge base to go to the
knowledge base details page.
2. Click **Add document**.
3. In the **Upload file** step, click or drag a file into the dashed box to upload it, and then click
**Next** after the upload completes.

> **Note:** The system supports file types such as doc, docx, pdf, txt, md, html, xls, xlsx, and csv.

4. In the **Segmentation & Cleaning** step, select and configure the document segmentation
parameters. Intelligent segmentation: This is the optimal segmentation method for general documents. The system splits the document by segmentation marker first. If a segment exceeds the maximum segment length, the system splits it by the maximum segment length and appends the segment overlap length. Parent-child segmentation: This method uses a two-level parent-child structure to balance retrieval accuracy and context information. Parent blocks provide context, and child blocks enable precise retrieval.
5. Click **Segment preview** to check whether the document segmentation meets your
expectations, and then click **Next**.
6. In the **Data processing** step, wait until the **Processing status** of the file changes to **Data**
**processing successful**, and then click **Confirm**.

**View knowledge base details**

1. On the **Knowledge Base** page, click the name of the target knowledge base to go to the
knowledge base details page.
2. View the document list in the knowledge base, which includes the document **name**, **data**
**size**, **processing status**, **segmentation method**, and **upload time**. You can also search
for a target document by file name.

**Segmentation configuration**

1. On the knowledge base details page, click **Config** in the **Operation** column of the target
document.
2. In the **Segmentation & Cleaning** step, select and configure the document segmentation
parameters.
3. Click **Segmentat preview** to check whether the document segmentation meets your
expectations, and then click **Next**.
4. In the **Data processing** step, wait until the **Processing status** of the file changes to **Data**
**processing successful**, and then click **Confirm**.

**Delete a document**

1. On the knowledge base details page, click **Delete** in the **Operation** column of the target
document.
2. In the pop-up dialog box, click **OK**.

**Download a document**

1. On the knowledge base details page, select the target document.
2. Click **Download** at the bottom of the list to download the document to your local device for
viewing.

**Edit a knowledge base**

> **Note:** You cannot edit built-in knowledge bases on the platform.

1. Click
**> Edit** in the **Operation** column of the target knowledge base.
2. Modify the parameters in the pop-up dialog box, and then click **OK**.

**Share a knowledge base**

> **Note:** This feature takes effect only in multi-region deployments.
> You cannot share built-in knowledge bases on the platform.
> You can share knowledge bases only from the primary region to unit regions. Sharing from unit regions to the primary region is not supported.

1. Click
**> Share** in the **Operation** column of the target knowledge base.
2. Sharing a knowledge base takes a long time. When the knowledge base displays **Sharing**,
the sharing succeeds.
3. Switch to the unit region and obtain the shared knowledge base on the **Shared from**
**Primary** tab.

**Delete a knowledge base**

> **Note:** You cannot delete built-in knowledge bases on the platform.
> This operation is irreversible. Proceed with caution.

1. Click
**> Delete** in the **Operation** column of the target knowledge base.
2. In the pop-up dialog box, click **Delete**.

## 5 Corpus system

### 5.1 Corpus tasks

The centralized management portal for corpus tasks provides end-to-end support for reception, annotation, and review. You can view task details from a personal or global perspective and perform related operations.

**Task types**

Waited: Corpus tasks that require processing by the current logged-in user. Launched: Corpus tasks initiated by the current logged-in user. Handled: Corpus tasks that the current logged-in user has processed. Related: Corpus tasks related to the current logged-in user. All: All corpus tasks.

**Add corpus**

2. In the left-side navigation pane, select **Corpus System > Corpus Task**.
3. Click **Create Corpus**.
4. Configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Product | Select the product to which the corpus belongs. |
| Question or Title | Enter a question or title related to the corpus. |
| Similar Questions | Click Add Item and enter similar questions. If you enter multiple similar questions, you can drag the icon before a question to adjust its position. Click the icon to delete a question. |
| Corpus Content | Enter the content related to the corpus. |

5. After the corpus is created, its **status** changes to **To be Received**. For information about
the reception operation, see Receive corpus.

**Receive corpus**

1. In the corpus list, find the target corpus task in the **To be Received** status.
2. Click **Receive** in the **Operation** column of the target corpus task.
3. Configure the **annotator** in the pop-up dialog box.

> **Note:** **Receive** indicates that the corpus has passed preliminary screening and is confirmed as content that the current system needs to refine. After reception, the corpus flows to annotators for labeling.

4. Click **OK**. The corpus **status** then changes to **To be Annotated**. For information about the
annotation operation, see Annotate corpus.

**Annotate corpus**

1. In the corpus list, find the target corpus task in the **To be Annotated** status.
2. Click **Annotation** in the **Operation** column of the target corpus task.
3. Configure the following parameters in the pop-up dialog box.

| Parameter | Description |
|---|---|

| Correctness Marking | Select an annotation result for the corpus. Accurate Partial Error Completely Wrong Note If the annotation result is Accurate, the corpus flows directly to the reviewer for approval. If the result is Partial Error or Completely Wrong, the corpus flows to the reviser for content modification. |
|---|---|
| Product | Select the product to which the corpus belongs. |
| Reviewer | This parameter takes effect only when you set Correctness Marking to Accurate. Select a corpus reviewer. |
| Reviser | This parameter takes effect only when you set Correctness Marking to Partial Error or Completely Wrong. Select a corpus reviser. |

4. Click **OK**. The corpus **status** then changes to **To be Reviewed** or **To be Revised**. For
information about related operations, see Review corpus or Revise corpus.

**Revise corpus**

1. In the corpus list, find the target corpus task in the **To be Revised** status.
2. Click **Revise** in the **Operation** column of the target corpus task.
3. On the corpus details page, modify the following corpus content.
Question or Title Similar Questions Corpus Content
4. Then, click **Complete revision**.
5. Configure the following parameters in the pop-up dialog box.

| Parameter | Description |
|---|---|
| Product | Select the product to which the corpus belongs. |
| Reference | Click Add Item and enter the reference materials for the revised corpus. |

| Revision Remarks | Select the revision feedback for the corpus. Improved Content Don't know how to modify Product Original Document Error |
|---|---|
| Reviewer | Select a corpus reviewer. |

6. Click **OK**. The corpus **Status** then changes to **To be Reviewed**. For information about the
review operation, see Review corpus.

**Review corpus**

1. In the corpus list, find the target corpus task in the **To be Reviewed** status.
2. Click **Review** in the **Operation** column of the target corpus task.
3. Confirm the **Review Result** in the pop-up dialog box.

**Pass**

**Reject** and enter the **Review comments**.
4. Then, click **OK**.
The status of approved corpus changes to **Published**. The **Status** of rejected corpus changes to **To be Revised**. For information about the revision operation, see Revise corpus.

**Related operations**

**Feedback details**

> **Note:** This feature takes effect after you receive thumbs-down feedback from users.

1. Click **Feedback Details** in the **Operation** column of the target corpus task.
2. In the pop-up panel, view the corpus task preview, including **Original Corpus**, **Feedback**
**Information**, and **Reference Materials**.

**History**

1. Click **History** in the **Operation** column of the target corpus task.
2. In the pop-up panel, view the history of the corpus, including the workflow, time, and
operators associated with the corpus.
3. Select a history record on the left side to view the **Question or Title**, **Similar Questions**,
and **Corpus Content** for the corresponding workflow on the right side.

**Archive corpus**

1. Select the target corpus task.
2. Click **Archive** below the corpus list.
3. In the pop-up dialog box, click **OK**.

> **Note:** You cannot perform operations on the corpus after archiving it.

## 6 System Settings

### 6.1 Model management

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

## 7 Common faults and solutions

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

## 8 High-risk operations

This topic describes the high-risk operations of Apsara AIOps to help users better estimate and avoid related operational risks.

| High-risk operations | Impact | Recovery plan |
|---|---|---|
| Delete entire intelligences | All the data of the smart body will be deleted. | Unrecoverable |
| Delete entire knowledge base | All knowledge base data will be deleted | Unrecoverable |
