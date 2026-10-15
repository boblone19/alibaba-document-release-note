---
title: "Apsara AIOps User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 21
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Apsara AIOps User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%BB%B4%E5%B0%8F%E6%99%BA/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20AIOps%20User%20Guide%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Apsara AIOps User Guide 20260701

## Log on to Apsara AIOps

This topic describes how to log on to and use Apsara AIOps.

**Prerequisites**

The endpoint, username, and password of the Apsara Uni-manager O&M console are obtained from the deployment personnel or administrator. The endpoint of the Apsara Uni-manager Operations console is in the format of region-id .ops.console. intranet-domain-id. The Chrome browser (recommended) is available.

**Procedure**

1. Open the browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations console and press
the Enter key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.

**Note**

Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password must be 10 to 20 characters in length.
4. Click **Agree and Log On**.
5. You can use one of the following methods to enter Apsara AIOps:
Method 1: In the top navigation bar, choose **Platform Operation > Management and**
**Control Service O&M > AIOps**.
Method 2: Click the floating ball on the page to enter Apsara AIOps.

## Intelligent dialogue

This article introduces the use of intelligent dialogue, which supports users to ask questions related to cloud products on the platform in natural language, consult information from AI, and conduct intelligent dialogue with AI.

**Procedure**

1. Log on to Apsara AIOps.
2. In the **Apsara AIOps** dialog box, enter a question and click
.

**Note**

Move the left mouse button to the content on the console page and click the AI search displayed to automatically trigger the Q&A capability for the selected content. New conversation: Click the top of the dialog box to open a new conversation. Historical Conversations: Click at the top of the dialog box to view historical conversations within the last seven days. Window Full Screen: Click above the dialog box to display the dialog box in full screen. After full screen, you can switch the operation intelligence in the left navigation bar.

| Question Scenario | Question Method |
|---|---|
| Service Consulting | How do I troubleshoot the failure of a Tianji component to the final state? What are the concepts of product, feature, and cluster in Apsara Infrastructure Cloud? How do I configure user permissions in the ASO console? How to use ossutil What is the architecture of ECS? |

| > Document Version: 202607 | 01 |
|---|---|

Close the dialog box: Click at the top of the dialog box to close the Apsara AIOps dialog box. Switch smart body: Click in the upper left corner of the dialog box to switch to the operation smart body.
3. After Apsara AIOps returns the Q&A content, you can perform the following operations:
: Approved. A Like indicates approval. : I don't agree with it. A little step indicates that I don't approve of the answer. : Copy. You can copy the content of the response. : regenerates an answer. You can regenerate an answer. At the same time, relevant operations or introductions are generated according to the questions asked, and multi-round conversations are supported during the Q&A process.

**Question Method Description**

| Alert handling | What are the P1 alerts in the current system? Analysis of alarms in the current system Help me analyze EcsGrandcanalHumanProcessing alerts |
|---|---|
| Routine inspection | What are the risks of current cloud platform inspection? What are the risks of infrastructure inspection? What are the serious inspection results? What are the risks of ECS inspection |
| O&M changes | Hotfix Upgrade Solution for V3 Enterprise Edition Temporary cleanup solution for memory fragments of ECS physical machines in Apsara Stack V3 rdsperf configuration automatic cleanup for minirds instances SLB-LVS machines go up and down How to undownload a product cluster in the Apsara Infrastructure Management Framework console |

| O&M agent | Description |
|---|---|
| Information query assistant | Is a cloud-based operation and maintenance information query intelligence, according to the user input information, through the large model NL2API capabilities, from the CMDB query corresponding CI information, and show it. |
| Network O&M Assistant | Analyzes IP addresses, instance identifiers, or alert information in user requests in real time, automatically correlates network asset topologies, identifies resource bindings, diagnoses health check and traffic paths for SLB instances, analyzes alert semantics, and analyzes root causes based on historical events and performance metrics. Finally, provides suggestions for precise handling to improve the efficiency of locating network exceptions on the cloud platform and system security. |
| Expert Advisory Assistant | Based on the O&M experience accumulated by the expert service team, it focuses on troubleshooting, locating, and solving common problems of the cloud platform, and supports solution query, best practices, and O&M consulting services. |
| Report Assistant | You can query existing reports and cards. You can also create new reports based on statistics and trend dimensions such as capacity data, usage data, asset data, and alert events. This allows you to make data-driven O&M decisions. |

## Operations Agent

This article describes the operations related to the O&M agent.

**Procedure**

1. Log on to Apsara AIOps.
2. In the **Apsara AIOps** dialog box, click
Switch to O&M Intelligence. You can also click and switch to the operations intelligence in the left navigation bar of the fullscreen interface.
3. The following features are supported under the operations intelligence.

| Alert Assistant | It is committed to providing intelligent analysis and diagnosis services for alarm and event data in the cloud platform environment. By obtaining and handling alert events in real time, analyzing their distribution, trends, correlations, and historical comparisons, and combining cloud product performance indicators and auxiliary diagnosis methods, users can quickly locate anomalies and potential risks, provide accurate response suggestions, and improve the efficiency and security of cloud platform operation and maintenance. |
|---|---|
| Change Assistant | You can recommend a suitable change plan based on the user's requirement scenario description. The scope covers standard changes such as hardware maintenance, product expansion, Hotx upgrade, and water level cleaning. |
| Diagnostic Assistant | Based on product blueprints and fault scenarios, you can analyze root causes based on user inputs, such as health status, alarm events, and problem phenomena, and topology dependencies, product logs, and alarm events to provide diagnosis suggestions. |
| Inspection Assistant | Checks whether the operations of cloud products, components, hardware, and cloud platforms are at risk. |
| Script Assistant | Supports common O&M commands, inspection scripts, black-screen commands, Ark commands, and Apsara Infrastructure Management Framework operations. You can generate efficient scripts with one click to improve O&M automation. |

4. Select the target intelligence, enter the question to ask, and click
. To create a conversation, click or **Create Conversation** at the top of the dialog box. Historical Conversations: Click or **Historical Conversations** at the top of the dialog box to view historical conversations within the last seven days. Window Full Screen: Click above the dialog box to display the dialog box in full screen. After full screen, you can switch the operation intelligence in the left navigation bar. Exit Full Screen: In the Full Screen dialog box, click above the dialog box to exit full screen. Close dialog: Click at the top of the dialog box to close the O&M Intelligence dialog box. Switch smart body: Click in the upper left corner of the dialog box to switch to the operation smart body.
5. After the O&M agent returns the answer, the following operations are supported.
: Approved. A Like indicates approval. : I don't agree with it. A little step indicates that I don't approve of the answer. : Copy. You can copy the content of the response. : regenerates an answer. You can regenerate an answer. At the same time, relevant operations or introductions are generated according to the questions asked, and multi-round conversations are supported during the Q&A process.

### Information query assistant

This topic describes the use case of the information query assistant.

**Introduction**

Supports natural language-based CMDB queries on the cloud platform, which can understand user intentions and accurately return results such as server information, network configurations, application topologies, and association relationships. Supports fuzzy query, multi-condition combination query, and context understanding.

**Usage Guide**

**Input Specifications**

The following types of information can be queried:
1. **Pangu storage** (such as bad disks and disk details)
: disk-xxx disk information, bad disk status of xxx host, and overall bad disk status
2. **ECS instance** (query by IP address, ID, or hostname)
, for example, the information of the ECS instance whose IP address is xx.xx.xx.xx, and the detailed configuration of the instance ID xxx ECS
3. **Physical host /machine** (such as the home cluster and hardware information)
, for example, the cluster to which host xxx belongs and the details of the physical machine whose IP address is the xx.xx.xx.xx.
4. **Resource query** (such as EIP, SLB, RDS, DNS, etc.)
For example, which ECS instance is bound to EIP xxx and SLB instance xxx details
5. **Product and cluster topologies** (such as dependencies or dependencies between products,
clusters, services, and service roles) Example: What services are available in the xx cluster and what services are dependent on the service role DockerDaemon#

| Scenarios | Result Description |
|---|---|
| General query | Key Information: displays the key results of the information query. More related information: displays information to query more related information. |
| Menu query | Menu query results Menu Path: displays the specific path of the menu query. Link: You can click Menu Links to go to the corresponding menu page. |

| Scenarios | Problem example |
|---|---|
| General query | Query xx machine information List information about two physical machines Query the operating system version of the physical machine whose IP address is xx.xx.xx.xx Which cluster does host xx belong to? Query the IP address of machine xx What are the images whose operating system is CentOS 64? _ What is the status of bad disks of xx machines in the current environment? Information about ECS instances whose IP addresses are xx.xx.xx.xx |
| Menu query | Menu entry for O&M big model management |

6. **Function entry** (such as the "Operation Orchestration" menu link)
: Operation Orchestration function entry, menu: Resource Management

**Note**

When you ask a question, if you can, include the resource identifier (such as the IP address, ID, and name), the target type (such as ECS, cluster, and service role), or your query intent (such as feature query and dependency query). This significantly improves the query accuracy.

**Results interpretation**

**Sample question list**

**FAQ**

1. . Basic ability**

**Q: What can this assistant do for me?**

**A:** this assistant is a natural language based cloud platform CMDB query expert. You can ask
questions directly in spoken language, which can help you query server information, network configuration, application topology and resource association. Supports fuzzy search and multicondition combination queries, and understands the context.

**Q: What types of resources can I query?**

**A:** supports the following five types of resource queries:
**Pangu Storage**: such as bad disk detection and disk details (for example, disk-xxx disk
information).
**ECS Instance**: You can query detailed configurations by IP address, ID, or hostname.
**Physical Host /Server**: queries the cluster, hardware information, and operating system
version.
**Other Resources**: the binding relationships and details of EIPs, Server Load Balancer (SLB)
instances, ApsaraDB RDS instances, and DNS.
**Product and Cluster Topology** : You can query the dependencies among products, clusters,
services, and service roles.
**Feature Entry**: You can directly find the path of the O&M menu and provide a redirect link. For
example, you can enter the O&M feature in Operation Orchestration Service (OO).
2. . Use skills**

**Q: How can I get the most accurate results?**

**A:** to improve accuracy, we recommend that you include at least one of the following three
elements when asking questions:
1. **Resource ID**: the specific IP address, instance ID, hostname, or disk number.
2. **Destination Type**: specifies whether you want to query ECS instances, clusters, server roles, or
physical machines.
3. **Query Intent**: indicates whether you want to query configurations, dependencies, or feature
menus. Good example: Details of an ECS with an IP address of 192.168.1.1 Fuzzy example: look up that machine

**Q: Is complex combination query supported? Like checking multiple conditions at the**

**same time?**

**A:** support. You can perform a query based on multiple conditions.
Example: Query the machines whose host name is xxx and currently have bad disks. Example: List all service roles that depend on DockerDaemon in the xx cluster.
3. . Interpretation of Results**

**What do query results usually contain?**

**A:** The varies based on the query type. The results are as follows:
**General resource query**:
**Key Information**: displays the core data that you care about, such as the IP address,
configuration, and status.
**More information**: Provides additional extended information associated with the resource.
**Menu /Feature Query**:
**Menu Path**: displays the hierarchical path of the feature.
**Shortcut Links**: provides links that can be clicked to go to the corresponding O&M page with
one click.

**Q: Why are there sometimes no results?**

**A:** may be caused by:
**Scope Limit**: You can query only the existing configuration items (CIs) in the CMDB of the
platform. If the resources are not entered or beyond the management scope, the results cannot be returned.
**Unclear**: If the issue is too vague or lacks key identifiers, such as IP addresses and IDs, intent
recognition may fail. We recommend that you add specific information and try again.

| Scenarios | Problem example |
|---|---|
| Assets | Please help me generate the statistical report of the physical server of the cloud platform by product dimension. Please help me generate the overall asset statistics of the platform and the server resource usage report in the dimension of computing /storage /network products. |

4. . Security and Restrictions**

**Q: Can this assistant help me fix faults or perform operations?**

**A:** can't. This assistant only provides information query and navigation capabilities. It can tell you
"which machine has a bad disk" or "where the bad disk is", but it cannot provide specific repair suggestions, nor can it directly perform O&M operations such as restart and disk replacement.

**Q: How do I ensure the data security of queries?**

**A:** The query scope of Assistant is strictly limited to the CMDB authorization scope of the platform.
It only displays the visible configuration information within your permissions, and does not disclose sensitive data or unauthorized access.

### Report Assistant

This topic describes how to use Report Assistant.

**Introduction**

Supports multi-source data integration, unified aggregation of platform-side assets, capacity, performance and other scattered data, to build a global data view; provides multi-dimensional statistics and trend analysis capabilities, covering asset statistics, capacity /water level distribution, alarm /event statistics and change trends and other core report types, support by asset, product, alarm source and other dimensions, flexible selection of time range, it also displays key indicators such as the total amount, average value, and utilization rate of data. It supports real-time display of CPU, memory, disk usage and capacity data of physical machines and product clusters, and combines historical trend analysis to realize comprehensive visualization of running status.

**Usage Guide**

**Input Specifications**

The following report generation ranges are supported:
1. Assets, including the total number and category statistics of assets, product-dimension server
statistics, and server list.
2. Capacity, including multi-product capacity statistics, single-product capacity statistics, single-
product capacity trends, multi-server capacity statistics, and single-server capacity trends.
3. Water level, including multi-product water level statistics, single-product water level trend, multi-
server water level statistics, and single-server water level trend.
4. Alerts, including alert statistics and alert trends.
5. Events, including event statistics and event trends.

**Results interpretation**

According to the range of questions, generate relevant statistical charts or tables. After you confirm the content, click **Confirm Intent to Create Now** to create a report.

**Sample question list**

| Capacity | Please help me generate the capacity trend report of ECS and EBS in the past week. Please help me query the statistical report of cloud product inventory capacity. |
|---|---|
| Water level | Please help me generate a report with water level statistics for all products Please help me generate the water level trend report of ECS |
| Alert | Please help me generate the alert statistics report of the platform and be able to make statistics by product dimension. Please help me generate the alert statistics of the platform and the trend report of alerts in the past 7 days. |
| Events | Please help me generate the event statistics report of the platform. Please help me generate the event statistics of the platform and the trend report of the event in the past 7 days. |
| Integrated | Please help me generate ECS O&M reports, including alerts, water levels, capacity, assets, and events. Please help me generate the capacity and water level data report for computing cloud products. |

| Metric | Meaning | Data Source | Update Frequency |
|---|---|---|---|
| Capacity | How many resources are available (total amount, allocated amount, remaining amount, allocation rate (such as CPU cores and memory GB)) | capacity management system | Daily 00:00 Snapshot |
| Water Level | How much is currently used-real-time /average usage (e. g. CPU usage %, memory usage %) | TianjiMon monitoring system | Real-time collection (daily average value for trend chart) |

**FAQ**

1. . Basic usage classes**

**Q: Where can I view a generated report after I save it?**

Log on to the ASO **A:**. In the top navigation bar, click **Platform Operations > Report Center >**
**List of Reports**.
2. . Data and dimension classes**

**Q: What exactly do the "capacity" and "water level" refer to in the report? Easy to**

**confuse how to do?**

**A:** Distinguish with one sentence

**Q: Where does the model, SN, IP, and other fields displayed in the server list come from?**

**Is it accurate?**

**A:** are all from the CMDB (Configuration Management Database), which is strongly consistent with
the asset ledger. If you find that the information is inconsistent, submit a ticket for feedback.

**Q: Why do some services, such as ApsaraDB RDS, have only CPU /memory capacity and**

**no disk capacity?**

**A:** Capacity models vary based on cloud services. Computing and storage products such as ECS and
CDS support multi-dimensional capacity (vCPU, memory, and disk), while database products such as RDS only manage CPU and memory capacity (disk capacity is independently managed by the underlying storage system and is not yet connected). It will be gradually expanded by product evolution.
3. . Fault and Support Class**

**Q: The generated report card loads slowly or displays "Data loading…", What could be**

**the reason?**

**A:** Please check the in sequence:
1. Check whether you can access other pages of the ASO platform.
2. Check the time range: whether the description of the long cycle (such as nearly 1 year + full
product)? It is recommended to try the last 7 days.
3. Check whether the filter condition describes too many dimensions.
4. If the exception persists, take a screenshot, ask the question, and submit a ticket for feedback.

### Alert Assistant

This topic describes the use cases of Alert Assistant.

**Introduction**

Supports word interaction and natural language dialogue to implement intelligent interpretation of cloud platform alerts, automatically identify alert phenomena, affect the business scope and related resources, and combine knowledge base and diagnostic engines to recommend handling plans to improve the alarm handling efficiency from hour-level to minute-level and reduce the impact on customer business.

**Usage Guide**

**Input Specifications**

The following alert /event questions are supported:
1. Query information based on dimensions such as alert name, list, distribution, level, and status.
2. Query information based on dimensions such as event name, list, distribution, level, and status.
3. Analysis, handling, and suggestions for a single alert.
4. Analysis, handling, and suggestions for a single event.

**Results interpretation**

**Alerts /event list**: displays the list of alerts and events. You can click **Batch Disable Alerts** to
disable alerts in multiple sessions.
**Alert /Event Analysis Report**: displays the analysis reports of alerts and events, including
anomaly detection, impact analysis, and handling suggestions based on real data.
**Recommended Actions**: You can select alert or event-related actions.
Click **Blueprint Diagnosis**. The **Product Diagnosis** page appears. Click **Monitoring Query**. The **Cloud Service Monitoring** page appears. Recommended Alert Item Handling Guide: displays the handling scheme of a specific alert item, including the alert description, alert attributes, associated rules, applicable version, alert cause, alert impact, and troubleshooting scheme.

**Sample question list**

| Scenarios | Problem example |
|---|---|
| General | The list of alerts in the current system. event list in the current system Alert distribution in the current system Event distribution in the current system P1 alarm in current system |
| Single Alert /Event | Help me analyze EcsGrandcanalHumanProcessing alerts |

### Inspection Assistant

This topic describes how to use the inspection assistant.

**Introduction**

Obtains inspection results of the cloud platform based on natural language conversations, generates inspection reports, and recommends solutions for inspection exceptions.

**Usage Guide**

**Input Specifications**

You can obtain multi-dimensional inspection results such as infrastructure, cloud platforms, cloud products, and production security. The following example shows a conversation: In the Cloud Platform Inspection section, click **Cloud Platform Inspection** in the upper part of the Q&A dialog box. You can select an inspection task to obtain the risk list. In the Cloud Service Inspection section, click **Cloud Service Inspection** in the upper part of the Q&A dialog box. You can select a cloud service to obtain the risk list. resource usage inspection Infrastructure Inspection

**Results interpretation**

According to the inspection questions raised, the reply content: Cloud platform inspection results: displays the inspection results and distribution of cloud platforms, the execution status of inspection tasks, and the risk trends of historical inspections (in the last 14 days). Result of a single inspection task: displays the critical or warning risks identified by the inspection task and the recommended solutions.

**More details**

If the current inspection result does not meet expectations, you can view all inspection results: Click Export Inspection Result to download the current inspection result details and analyze each case. Click Full Inspection Result. You are redirected to the **Inspection Result Details** tab of the
**Tongque > Inspection Center > Routine Inspection** page to view the full inspection results
of the cloud platform. Click Export Report. On the page that appears, you can view and export the full inspection report.

**Tongque > Report Center > Service Report**

| Scenarios | Problem example |
|---|---|
| Script | Help me generate a script for deploying applications to ECS Write an inspection script to inspect the health status of key components and services provided by Pangu after the upgrade. |
| Command | How to use snapctl info to query base information How to use commands to check the status of an RDS instance |

Click Re-inspect. You are redirected to the **Inspection Tasks** tab of the **Inspection Center >**
**Inspection Center > Routine Inspection** page. You can trigger each inspection task as
needed.

**Sample question list**

What are the risks of current cloud platform inspection? What are the risks of infrastructure inspection? What are the risks of resource usage inspection? What are the risks of kernel inspection? What are the serious inspection risks? What are the risks of ECS inspection

### Script Assistant

This topic describes the use cases of Script Assistant.

**Introduction**

In addition to general O&M commands, such as Linux, Python, and Bat commands, the built-in cloud platform O&M scenario-specific script knowledge base allows you to automatically generate executable scripts based on natural language input. This improves O&M script writing efficiency and accuracy. Supports common O&M commands, inspection scripts, black-screen commands, Ark commands, and Apsara Infrastructure Management Framework operations. You can generate efficient scripts with one click to improve O&M automation.

**Usage Guide**

**Input Specifications**

The following range of script questions are supported: Provide scripts for related operations Query of black-screen commands

**Results interpretation**

Script: displays the feature description and details of the related script. Command: displays related commands, optional parameter description, and command usage examples.

**Sample question list**

### Diagnostic Assistant

This topic describes the use cases of the diagnostic assistant.

| Scenarios | Problem example |
|---|---|
| Cloud Platform | What are the exceptions to the current cloud platform? The number of hardware exceptions on the cloud platform and the scope of products affected. |
| Product | ECS product diagnosis OSS product diagnosis |
| Alert | Analysis of ECS product alerts What is the cause of the alert that the EBS cluster is overloaded? |
| Logs | Whether the operational logs of RDS in the last day are abnormal Query the latest 1000-line logs of ASO and analyze whether exceptions are found. |

**Introduction**

You can use multi-dimensional data such as cloud service logs, monitoring metrics, and blueprint topologies to troubleshoot issues and perform intelligent root cause analysis (RCA). Supports two modes: General Diagnosis and Deep Diagnosis. A structured diagnosis report is generated, including problem summary, impact troubleshooting, root cause analysis, and handling suggestions.

**Usage Guide**

**Input Specifications**

The following questions are supported: Cloud product basics consulting Log /Command Parsing abnormal influence surface analysis Exception troubleshooting guidelines In the Final State Diagnostics section, click **Final State Diagnostics** in the upper part of the Q&A dialog box. You can select a product to diagnose and analyze whether the product does not reach the final state.

**Results interpretation**

Cloud product diagnosis list: displays a list of all abnormal products on the current cloud platform. Find the product that you want to diagnose and click **Diagnose**in the Actions column. Product Diagnosis: displays detailed product diagnosis results, including problem summary, diagnosis details, root cause analysis, and handling suggestions. Click **Comprehensive**
**Diagnosis**. You are redirected to the**Tongque > Diagnosis Center > Product Diagnosis**
page to view the multi-dimensional diagnostic details of the product. Alert Diagnosis: displays detailed alert diagnosis results, including alert description, diagnosis details, root cause analysis, and handling suggestions. Log diagnosis: quickly analyzes the log entry for exceptions.

**Sample question list**
