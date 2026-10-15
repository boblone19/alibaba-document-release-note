---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 21
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20Stack%20Operation%20Apsara%20AIOps%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack Operation Apsara AIOps User Guide 20260828

o AIOPS

## Log in to AIOPS

This topic describes how to log in to AIOps.

**Prerequisites**

You have obtained the endpoint, username, and password of the Apsara Uni-manager Operations Console from the deployment engineer or administrator. The endpoint of the Apsara Uni-manager Operations Console follows this format: regionid.ops.console.intranet-domain-id. The Google Chrome broswer (recommended) is available.

**Procedure**

1. Open a browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console and
press Enter.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter the correct username and password.
o AIOPS

**Note**

Obtain the username and password for logging in to the Apsara Uni-manager Operations Console from the deployment engineer or administrator. If you enter an incorrect password for three consecutive times, the system enables image Completely Automated Public Turing Test to tell Computers and Humans Apart (CAPTCHA) verification. After five consecutive incorrect attempts, the account will be locked. Contact the administrator to unlock it. When you log in to the Apsara Uni-manager Operations Console for the first time, you must change the password of the login account. Follow the prompts to complete the password change. To improve security, the password must: contain uppercase and lowercase letters. contain digits (0 to 9). contain special characters, including exclamation marks (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). be 10 to 20 characters in length.
4. Click **Log In**.

**Note**

If a privacy policy has been configured, click **Agree to Privacy Policy and Log In** .
5. Access AIOps by using one of the following methods:
Method 1: In the top navigation bar, choose **Platform Operation > Management and**
**Control Service O&M > AIOps**.
Method 2: Click the floating button on the page. ent dialogue

## Intelligent dialogue

This topic describes how to use the Intelligent Dialogue feature. You can ask questions about the platform and cloud products in natural language, consult AI, and have intelligent conversations.

**Procedure**

1. Log in to Apsara AIOps.
2. In the left-side navigation pane, choose **Intelligent Dialogue > Create a session**.
3. Obtain the **Current to-do list**, including tasks of the high priority, medium priority, and low
priority.
4. Click a to-do task to view the corresponding to-do list.
Click **Disposal** for the target to-do task. In the dialog box below, the system automatically selects an agent and generates a question description. Click **Closing Order** for the target to-do task, and then click **OK** in the dialog box that appears to close the order.
5. Enter your question in the chat box, press Shift + Enter to insert a line break, and then click
.

**Note**

Use @ in the chat box to specify an agent to answer your question. To query specific content, highlight it with the left mouse button on the console page, and click the AI Search option that appears to automatically trigger the Q&A capability.
6. After Apsara AIOps returns the answer, perform the following operations:
: Click the like button to indicate that you approve of the answer. : Click the dislike button to indicate that you disapprove of the answer. Select a feedback option in the chat box and click **OK** to submit it. : Copy the answer content. : Request the system to regenerate an answer. ent dialogue : Export the answer content in formats such as Markdown, PDF, DOCX, and WPS. The system also generates relevant operations or descriptions based on your questions, and supports multi-turn conversations throughout the Q&A process.
7. Perform the following operations in the upper-right corner of the page.
Click **Create a Conversation** to start a new conversation. Click **Historical Dialogue** to view conversation records from the past seven days. Click **Current to-do list** to view the tasks to be handled. Click to close the Apsara AIOps chat box.

**How to ask questions**

| Scenario | Questions |
|---|---|
| Service consultation | How do I troubleshoot Tianji components that have not reached the final state? What are the concepts of product, feature, and cluster in Apsara Stack Tianji? How do I configure user permissions in the ASO console? How do I use ossutil? What is the architecture of the ECS cloud service? |
| Alert handling | What P1 alerts are active in the current system? Analyze the alerts in the current system. Help me analyze the EcsGrandcanalHumanProcessing alert. |
| Routine inspection | What risks are identified in the current cloud platform inspection? What risks are identified in the infrastructure inspection? What are the major inspection findings? What risks are identified in the ECS inspection? |
| O&M change | Hotfix upgrade plan for Apsara Stack V3 Enterprise Edition Temporary cleanup plan for ECS physical machine memory fragmentation in the Apsara Stack V3 environment Automatic cleanup of rdsperf configuration for MiniRDS instances Bring SLB-LVS machines online or offline How do I take a product cluster offline in the Tianji console? |

## O&M agent

This topic describes the operations related to O&M Agent.

**Procedure**

1. Log in to Apsara AIOps.
2. In the **Apsara AIOps** chat box, click
to switch to O&M Agent. You can also click and then switch to the O&M Agent from the left-side navigation pane in the full-screen view.
3. View the following features provided by O&M Agent.

| O&M agent | Description |
|---|---|
| Information Query Assistant | This is a cloud platform-based O&M information query agent. Based on user input, it leverages the Natural Language to API (NL2API) capability of the Large Language Model (LLM) to query the corresponding Configuration Item (CI) information from the Configuration Management Database (CMDB) and displays the results. |
| Network Operations Assistant | This assistant analyzes IP addresses, instance identifiers, and alert information in user requests in real time. It automatically associates network asset topologies, identifies resource binding relationships, and performs health checks and traffic path diagnosis on Server Load Balancer (SLB) instances. Furthermore, it parses alert semantics, conducts root cause analysis based on historical events and performance metrics, and provides precise remediation recommendations to improve the efficiency of locating network exceptions and enhance system security on the cloud platform. |
| Expert Consultation Assistant | This assistant draws on the O&M experience of expert service teams and focuses on troubleshooting common cloud platform issues. You can query solutions and best practices, as well as consult on O&M services. |
| Report Assistant | This assistant helps you query existing reports and cards. It also allows you to create reports based on the statistics and trends of capacity data, usage data, asset data, and alert events to enable data-driven O&M decision-making. |

| Alert Assistant | This assistant provides intelligent analysis and diagnosis services for alert and event data in cloud platform environments. It retrieves and processes alert events in real time, and analyzes their distribution, trends, correlations, and historical comparisons. By combining with cloud product performance metrics and assisted diagnostics, it helps users quickly locate exceptions and potential risks, provides precise remediation recommendations, and improves cloud platform O&M efficiency and security. |
|---|---|
| Change Assistant | This assistant recommends change plans suitable for users' scenarios. The coverage includes standard changes such as hardware repair, product scaling, hotfix upgrades, and resource cleanup. |
| Diagnostic Expert | This assistant performs root cause analysis based on product blueprints and fault scenarios. It combines user input (such as health status, alert events, and problem symptoms) with topology dependencies, product logs, and alert events to provide diagnostic recommendations. |
| Inspection Assistant | This assistant inspects cloud products, components, hardware, and cloud platforms for operational risks. |
| Script Assistant | This assistant allows you to generate efficient scripts with one click for general O&M commands, Tongque inspection scripts, common cloud product Command-Line Interface (CLI) commands, Ark commands, and Tianji operations to improve O&M automation. |
| RocketMQ(Tianji)AiAs sistant | This assistant provides comprehensive intelligent monitoring and in-depth diagnosis services for RocketMQ clusters. By deeply integrating cluster topology awareness, real-time Broker status collection, multi-dimensional analysis of key performance metrics (such as TPS, message accumulation, disk usage, and primary/secondary synchronization latency), intelligent parsing of instance configurations, and resource usage statistics, it builds a complete health profile for RocketMQ clusters. The assistant supports automated cluster inspections that cover core dimensions including primary/secondary consistency, permission configurations, NameServer registration status, and message retention policies. Furthermore, it leverages an AI-driven diagnosis engine to accurately identify and locate root causes of potential performance bottlenecks, configuration risks, resource skew, and high availability (HA) risks. This helps O&M personnel quickly focus on key issues amidst massive metrics and complex topologies, significantly improving fault response efficiency and system governance capabilities, and ensuring the high availability, stability, and maintainability of the RocketMQ middleware. |

| RocketMQ(PaaS)AiAss istant | This assistant provides comprehensive intelligent monitoring and in-depth diagnosis services for RocketMQ (PaaS) clusters. By deeply integrating cluster topology awareness, real-time Broker status collection, multi- dimensional analysis of key performance metrics (such as TPS, message accumulation, disk usage, and primary/secondary synchronization latency), intelligent parsing of instance configurations, and resource usage statistics, it builds a complete health profile for RocketMQ (PaaS) clusters. The assistant supports automated cluster inspections that cover core dimensions including primary/secondary consistency, permission configurations, NameServer registration status, and message retention policies. Furthermore, it leverages an AI-driven diagnosis engine to accurately identify and locate root causes of potential performance bottlenecks, configuration risks, resource skew, and high availability (HA) risks. This helps O&M personnel quickly focus on key issues amidst massive metrics and complex topologies, significantly improving fault response efficiency and system governance capabilities, and ensuring the high availability, stability, and maintainability of the RocketMQ (PaaS) middleware. |
|---|---|

4. Select the target agent, enter your question, and click
. New chat: Click or **Create a Conversation** above the chat box to start a new conversation. Conversation history: Click or **Historical Dialogue** above the chat box to view conversation records from the last seven days. Full screen: Click above the chat box to display the chat box in full screen. In fullscreen mode, you can switch to a different O&M agent from the left-side navigation pane. Exit full screen: In full-screen mode, click above the chat box to exit. Close chat: Click above the chat box to close the O&M agent chat box. Switch agent: Click in the upper-left corner of the chat box to switch to O&M Agent.
5. After the O&M agent returns a response, perform the following operations:
: Click the like button to indicate that you approve of the answer. : Click the dislike button to indicate that you disapprove of the answer. Select a feedback option in the chat box and click **OK** to submit it. : Copy the answer content. : Request the system to regenerate an answer. : Export the answer content in formats such as Markdown, PDF, DOCX, and WPS. The system also generates relevant operations or descriptions based on your questions, and supports multi-turn conversations throughout the Q&A process.

### Information query assistant

This topic describes the use case of the information query assistant. Supports natural language-based CMDB queries on the cloud platform, which can understand user intentions and accurately return results such as server information, network configurations, application topologies, and association relationships. Supports fuzzy query, multi-condition combination query, and context understanding. The following types of information can be queried:
1. **Pangu storage** (such as bad disks and disk details)
: disk-xxx disk information, bad disk status of xxx host, and overall bad disk status
2. **ECS instance** (query by IP address, ID, or hostname)
, for example, the information of the ECS instance whose IP address is xx.xx.xx.xx, and the detailed configuration of the instance ID xxx ECS
3. **Physical host /machine** (such as the home cluster and hardware information)
, for example, the cluster to which host xxx belongs and the details of the physical machine whose IP address is the xx.xx.xx.xx.
4. **Resource query** (such as EIP, SLB, RDS, DNS, etc.)
For example, which ECS instance is bound to EIP xxx and SLB instance xxx details
5. **Product and cluster topologies** (such as dependencies or dependencies between
products, clusters, services, and service roles) Example: What services are available in the xx cluster and what services are dependent on the service role DockerDaemon#
6. **Function entry** (such as the "Operation Orchestration" menu link)
: Operation Orchestration function entry, menu: Resource Management

**Note**

When you ask a question, if you can, include the resource identifier (such as the IP address, ID, and name), the target type (such as ECS, cluster, and service role), or your query intent (such as feature query and dependency query). This significantly improves the query accuracy.

| Scenarios | Result Description |
|---|---|
| General query | Key Information: displays the key results of the information query. More related information: displays information to query more related information. |
| Menu query | Menu query results Menu Path: displays the specific path of the menu query. Link: You can click Menu Links to go to the corresponding menu page. |

| Scenarios | Problem example |
|---|---|
| General query | Query xx machine information List information about two physical machines Query the operating system version of the physical machine whose IP address is xx.xx.xx.xx Which cluster does host xx belong to? Query the IP address of machine xx What are the images whose operating system is CentOS 64? _ What is the status of bad disks of xx machines in the current environment? Information about ECS instances whose IP addresses are xx.xx.xx.xx |
| Menu query | Menu entry for O&M big model management |

**FAQ**

1. . Basic ability**

**Q: What can this assistant do for me?**

**A:** this assistant is a natural language based cloud platform CMDB query expert. You can ask
questions directly in spoken language, which can help you query server information, network configuration, application topology and resource association. Supports fuzzy search and multi-condition combination queries, and understands the context.

**Q: What types of resources can I query?**

**A:** supports the following five types of resource queries:
**Pangu Storage**: such as bad disk detection and disk details (for example, disk-xxx disk
information).
**ECS Instance**: You can query detailed configurations by IP address, ID, or hostname.
**Physical Host /Server**: queries the cluster, hardware information, and operating system
version.
**Other Resources**: the binding relationships and details of EIPs, Server Load Balancer (SLB)
instances, ApsaraDB RDS instances, and DNS.
**Product and Cluster Topology** : You can query the dependencies among products,
clusters, services, and service roles.
**Feature Entry**: You can directly find the path of the O&M menu and provide a redirect link.
For example, you can enter the O&M feature in Operation Orchestration Service (OO).
2. . Use skills**

**Q: How can I get the most accurate results?**

**A:** to improve accuracy, we recommend that you include at least one of the following three
elements when asking questions:
1. **Resource ID**: the specific IP address, instance ID, hostname, or disk number.
2. **Destination Type**: specifies whether you want to query ECS instances, clusters, server
roles, or physical machines.
3. **Query Intent**: indicates whether you want to query configurations, dependencies, or
feature menus. Good example: Details of an ECS with an IP address of 192.168.1.1 Fuzzy example: look up that machine

**Q: Is complex combination query supported? Like checking multiple conditions at**

**the same time?**

**A:** support. You can perform a query based on multiple conditions.
Example: Query the machines whose host name is xxx and currently have bad disks. Example: List all service roles that depend on DockerDaemon in the xx cluster.
3. . Interpretation of Results**

**What do query results usually contain?**

**A:** The varies based on the query type. The results are as follows:
**General resource query**:
**Key Information**: displays the core data that you care about, such as the IP address,
configuration, and status.
**More information**: Provides additional extended information associated with the
resource.
**Menu /Feature Query**:
**Menu Path**: displays the hierarchical path of the feature.
**Shortcut Links**: provides links that can be clicked to go to the corresponding O&M page
with one click.

**Q: Why are there sometimes no results?**

**A:** may be caused by:
**Scope Limit**: You can query only the existing configuration items (CIs) in the CMDB of the
platform. If the resources are not entered or beyond the management scope, the results cannot be returned.
**Unclear**: If the issue is too vague or lacks key identifiers, such as IP addresses and IDs,
intent recognition may fail. We recommend that you add specific information and try again.
4. . Security and Restrictions**

**Q: Can this assistant help me fix faults or perform operations?**

**A:** can't. This assistant only provides information query and navigation capabilities. It can tell
you "which machine has a bad disk" or "where the bad disk is", but it cannot provide specific repair suggestions, nor can it directly perform O&M operations such as restart and disk replacement.

**Q: How do I ensure the data security of queries?**

**A:** The query scope of Assistant is strictly limited to the CMDB authorization scope of the
platform. It only displays the visible configuration information within your permissions, and does not disclose sensitive data or unauthorized access.

### Report Assistant

This topic describes how to use Report Assistant. Supports multi-source data integration, unified aggregation of platform-side assets, capacity, performance and other scattered data, to build a global data view; provides multidimensional statistics and trend analysis capabilities, covering asset statistics, capacity /water level distribution, alarm /event statistics and change trends and other core report types, support by asset, product, alarm source and other dimensions, flexible selection of time range, it also displays key indicators such as the total amount, average value, and utilization rate of data. It supports real-time display of CPU, memory, disk usage and capacity data of physical machines and product clusters, and combines historical trend analysis to realize comprehensive visualization of running status. The following report generation ranges are supported:
1. Assets, including the total number and category statistics of assets, product-dimension
server statistics, and server list.
2. Capacity, including multi-product capacity statistics, single-product capacity statistics,
single-product capacity trends, multi-server capacity statistics, and single-server capacity trends.
3. Water level, including multi-product water level statistics, single-product water level trend,
multi-server water level statistics, and single-server water level trend.
4. Alerts, including alert statistics and alert trends.
5. Events, including event statistics and event trends.
According to the range of questions, generate relevant statistical charts or tables. After you confirm the content, click **Confirm Intent to Create Now** to create a report.

| Scenarios | Problem example |
|---|---|
| Assets | Please help me generate the statistical report of the physical server of the cloud platform by product dimension. Please help me generate the overall asset statistics of the platform and the server resource usage report in the dimension of computing /storage /network products. |
| Capacity | Please help me generate the capacity trend report of ECS and EBS in the past week. Please help me query the statistical report of cloud product inventory capacity. |
| Water level | Please help me generate a report with water level statistics for all products Please help me generate the water level trend report of ECS |
| Alert | Please help me generate the alert statistics report of the platform and be able to make statistics by product dimension. Please help me generate the alert statistics of the platform and the trend report of alerts in the past 7 days. |
| Events | Please help me generate the event statistics report of the platform. Please help me generate the event statistics of the platform and the trend report of the event in the past 7 days. |
| Integrated | Please help me generate ECS O&M reports, including alerts, water levels, capacity, assets, and events. Please help me generate the capacity and water level data report for computing cloud products. |

**FAQ**

1. . Basic usage classes**

**Q: Where can I view a generated report after I save it?**

Log on to the ASO **A:**. In the top navigation bar, click **Platform Operations > Report**
**Center > List of Reports**.
2. . Data and dimension classes**

**Q: What exactly do the "capacity" and "water level" refer to in the report? Easy to**

**confuse how to do?**

**A:** Distinguish with one sentence

| Metric | Meaning | Data Source | Update Frequency |
|---|---|---|---|
| Capacity | How many resources are available (total amount, allocated amount, remaining amount, allocation rate (such as CPU cores and memory GB)) | capacity management system | Daily 00:00 Snapshot |
| Water Level | How much is currently used-real-time /average usage (e. g. CPU usage %, memory usage %) | TianjiMon monitoring system | Real-time collection (daily average value for trend chart) |

**Q: Where does the model, SN, IP, and other fields displayed in the server list come**

**from? Is it accurate?**

**A:** are all from the CMDB (Configuration Management Database), which is strongly consistent
with the asset ledger. If you find that the information is inconsistent, submit a ticket for feedback.

**Q: Why do some services, such as ApsaraDB RDS, have only CPU /memory capacity**

**and no disk capacity?**

**A:** Capacity models vary based on cloud services. Computing and storage products such as
ECS and CDS support multi-dimensional capacity (vCPU, memory, and disk), while database products such as RDS only manage CPU and memory capacity (disk capacity is independently managed by the underlying storage system and is not yet connected). It will be gradually expanded by product evolution.
3. . Fault and Support Class**

**Q: The generated report card loads slowly or displays "Data loading…", What could**

**be the reason?**

**A:** Please check the in sequence:
1. Check whether you can access other pages of the ASO platform.
2. Check the time range: whether the description of the long cycle (such as nearly 1 year +
full product)? It is recommended to try the last 7 days.
3. Check whether the filter condition describes too many dimensions.
4. If the exception persists, take a screenshot, ask the question, and submit a ticket for
feedback.

### Alert Assistant

This topic describes the use cases of Alert Assistant. Supports word interaction and natural language dialogue to implement intelligent interpretation of cloud platform alerts, automatically identify alert phenomena, affect the business scope and related resources, and combine knowledge base and diagnostic engines to recommend handling plans to improve the alarm handling efficiency from hour-level to minute-level and reduce the impact on customer business. The following alert /event questions are supported:
1. Query information based on dimensions such as alert name, list, distribution, level, and
status.
2. Query information based on dimensions such as event name, list, distribution, level, and
status.
3. Analysis, handling, and suggestions for a single alert.
4. Analysis, handling, and suggestions for a single event.
**Alerts /event list**: displays the list of alerts and events. You can click **Batch Disable**
**Alerts** to disable alerts in multiple sessions.
**Alert /Event Analysis Report**: displays the analysis reports of alerts and events,
including anomaly detection, impact analysis, and handling suggestions based on real data.
**Recommended Actions**: You can select alert or event-related actions.
Click **Blueprint Diagnosis**. The **Product Diagnosis** page appears. Click **Monitoring Query**. The **Cloud Service Monitoring** page appears. Recommended Alert Item Handling Guide: displays the handling scheme of a specific alert item, including the alert description, alert attributes, associated rules, applicable version, alert cause, alert impact, and troubleshooting scheme.

| Scenarios | Problem example |
|---|---|
| General | The list of alerts in the current system. event list in the current system Alert distribution in the current system Event distribution in the current system P1 alarm in current system |
| Single Alert /Event | Help me analyze EcsGrandcanalHumanProcessing alerts |

### Inspection Assistant

This topic describes how to use the inspection assistant. Obtains inspection results of the cloud platform based on natural language conversations, generates inspection reports, and recommends solutions for inspection exceptions. You can obtain multi-dimensional inspection results such as infrastructure, cloud platforms, cloud products, and production security. The following example shows a conversation: In the Cloud Platform Inspection section, click **Cloud Platform Inspection** in the upper part of the Q&A dialog box. You can select an inspection task to obtain the risk list. In the Cloud Service Inspection section, click **Cloud Service Inspection** in the upper part of the Q&A dialog box. You can select a cloud service to obtain the risk list. resource usage inspection Infrastructure Inspection According to the inspection questions raised, the reply content: Cloud platform inspection results: displays the inspection results and distribution of cloud platforms, the execution status of inspection tasks, and the risk trends of historical inspections (in the last 14 days). Result of a single inspection task: displays the critical or warning risks identified by the inspection task and the recommended solutions.

**More details**

If the current inspection result does not meet expectations, you can view all inspection results: Click Export Inspection Result to download the current inspection result details and analyze each case. Click Full Inspection Result. You are redirected to the **Inspection Result Details** tab of the
**Tongque > Inspection Center > Routine Inspection** page to view the full inspection
results of the cloud platform. Click Export Report. On the page that appears, you can view and export the full inspection report. **Tongque > Report Center > Service Report** Click Re-inspect. You are redirected to the **Inspection Tasks** tab of the **Inspection**
**Center > Inspection Center > Routine Inspection** page. You can trigger each
inspection task as needed. What are the risks of current cloud platform inspection? What are the risks of infrastructure inspection? What are the risks of resource usage inspection? What are the risks of kernel inspection? What are the serious inspection risks? What are the risks of ECS inspection

### Script Assistant

This topic describes the use cases of Script Assistant. In addition to general O&M commands, such as Linux, Python, and Bat commands, the built-in cloud platform O&M scenario-specific script knowledge base allows you to automatically generate executable scripts based on natural language input. This improves O&M script writing efficiency and accuracy. Supports common O&M commands, inspection scripts, blackscreen commands, Ark commands, and Apsara Infrastructure Management Framework operations. You can generate efficient scripts with one click to improve O&M automation. The following range of script questions are supported: Provide scripts for related operations Query of black-screen commands Script: displays the feature description and details of the related script. Command: displays related commands, optional parameter description, and command usage examples.

| Scenarios | Problem example |
|---|---|
| Script | Help me generate a script for deploying applications to ECS Write an inspection script to inspect the health status of key components and services provided by Pangu after the upgrade. |
| Command | How to use snapctl info to query base information How to use commands to check the status of an RDS instance |

### Diagnostic Assistant

This topic describes the use cases of the diagnostic assistant. You can use multi-dimensional data such as cloud service logs, monitoring metrics, and blueprint topologies to troubleshoot issues and perform intelligent root cause analysis (RCA). Supports two modes: General Diagnosis and Deep Diagnosis. A structured diagnosis report is generated, including problem summary, impact troubleshooting, root cause analysis, and handling suggestions. The following questions are supported: Cloud product basics consulting Log /Command Parsing abnormal influence surface analysis Exception troubleshooting guidelines In the Final State Diagnostics section, click **Final State Diagnostics** in the upper part of the Q&A dialog box. You can select a product to diagnose and analyze whether the product does not reach the final state. Cloud product diagnosis list: displays a list of all abnormal products on the current cloud platform. Find the product that you want to diagnose and click **Diagnose**in the Actions column. Product Diagnosis: displays detailed product diagnosis results, including problem summary, diagnosis details, root cause analysis, and handling suggestions. Click **Comprehensive**
**Diagnosis**. You are redirected to the**Tongque > Diagnosis Center > Product**
**Diagnosis** page to view the multi-dimensional diagnostic details of the product.
Alert Diagnosis: displays detailed alert diagnosis results, including alert description, diagnosis details, root cause analysis, and handling suggestions. Log diagnosis: quickly analyzes the log entry for exceptions.

| Scenarios | Problem example |
|---|---|
| Cloud Platform | What are the exceptions to the current cloud platform? The number of hardware exceptions on the cloud platform and the scope of products affected. |
| Product | ECS product diagnosis OSS product diagnosis |
| Alert | Analysis of ECS product alerts What is the cause of the alert that the EBS cluster is overloaded? |
| Logs | Whether the operational logs of RDS in the last day are abnormal Query the latest 1000-line logs of ASO and analyze whether exceptions are found. |
