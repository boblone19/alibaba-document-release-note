# Alibaba Cloud Apsara Stack V3.18.6 — What changed in the English document set since V3.16.2

**Delta of `V3.18.6` vs `V3.16.2` on the international documentation portal, derived line-by-line from the converted English Markdown corpus.**

| | |
|---|---|
| Manuals in the V3.18.6 English set | 287 |
| Documented pages (V3.18.6) | 42,932 |
| Document dates in the V3.18.6 set | 2025-05-29 → 2026-07-03 |
| Products covered (V3.18.6) | 89 |
| Baseline available for comparison — the V3.16.2 English set | 53 manuals dated 2022-06-28 → 2025-11-06; User / Developer / Instance-Families guides only, no Product Introduction or O&M volumes |
| Manuals paired to a V3.16.2 counterpart | 32 (every pair has a strictly later document date: 32/32) |
| V3.18.6 manuals with no V3.16.2 counterpart (delta not computable) | 255 (§5) |
| V3.16.2 manuals not re-published in the V3.18.6 set | 21 (§6) |
| Sentences added in the new editions (informative only) | 1,902 |
| Sentences no longer present (informative only) | 1,436 |
| Informative sentences before cancelling re-typeset pairs | 1,999 added, 1,533 removed (after cancellation: the two rows above) |
| Limit/quota rows added or changed | 13 |
| Paired manuals carrying their own release-notes section | 3 |

**How to read this.** §2 ranks the largest changes and states what the diff itself shows. §3 quotes the release-notes sections that product teams wrote into the manuals themselves. §4 is the detail: for every manual with material evidence it shows what text appeared, what text disappeared, which sections were added, removed or renamed, and which limits changed — each line attributed to the section it sits in. §5 lists the manuals that have no comparable baseline (with the closest earlier English name, because the V3.16.2 English set is far smaller than V3.18.6), §6 the baseline manuals that were not re-published. §7 states the method and its limits. Nothing here is inferred from product knowledge: every claim is a diff of two PDFs, and absence of a diff is **not** evidence that a product is unchanged.

---

## 1. Scope: two document sets, different catalogue generations

The download page exposes **V3.18.6** and **V3.16.2** as two selectable English sets. They are not two editions of the same catalogue: the V3.16.2 baseline holds 53 manuals dated 2022-06-28 → 2025-11-06 and only three document types (28× User Guide, 24× Developer Guide, 1× Introduction to Instance Families and Instance Types), while the V3.18.6 set holds 287 manuals dated 2025-05-29 → 2026-07-03 across 8 document types (adding Product Introduction, Operations Guide and Operations & Maintenance Guide volumes that the baseline never published in English). Only 32 manuals can therefore be diffed at all; the other 255 are listed in §5 with the closest earlier English name instead of a fabricated comparison.

The corpus was also rebranded between the two sets: the string **“Apsara Stack Enterprise”** appears in 48 of 53 baseline manuals but only 41 of 287 V3.18.6 manuals (`Apsara Stack Enterprise v3.16.2` → `Apsara Stack V3.18.6` in the title blocks). Sentences whose only difference is this rename still count as changed text below — they are real textual deltas, and no attempt was made to suppress them.

## 2. Biggest changes between the two sets

| product | manual | pages | doc date | net lines | sections ± | limits |
|---|---|---|---|---|---|---|
| Cloud Defined Storage | Developer Guide | 783 → 2021 (+1238) | 20241114 → 20260629 | +169 / -128 | +612 / -3 | 0 |
| DataWorks | User Guide | 995 → 1590 (+595) | 20220916 → 20260629 | +282 / -237 | +342 / -231 | 0 |
| Apsara Uni-manager Operations Cons | Developer Guide | 65 → 580 (+515) | 20251106 → 20260703 | +39 / -4 | +110 / -5 | 0 |
| Container Service for Kubernetes | User Guide | 320 → 734 (+414) | 20220916 → 20260629 | +376 / -81 | +137 / -46 | 0 |
| API Gateway | Developer Guide | 196 → 613 (+417) | 20220915 → 20260629 | +30 / -54 | +159 / -94 | 0 |
| CloudMonitor | Developer Guide | 174 → 552 (+378) | 20250312 → 20260629 | +1 / -2 | +181 / -5 | 2 |
| Apsara Uni-manager Operations Cons | User Guide | 419 → 710 (+291) | 20251106 → 20260703 | +145 / -129 | +274 / -407 | 0 |
| MaxCompute | Developer Guide | 34 → 316 (+282) | 20220726 → 20260629 | +85 / -4 | +144 / -2 | 3 |
| Cloud Defined Storage | User Guide | 691 → 963 (+272) | 20240703 → 20260629 | +209 / -99 | +91 / -145 | 8 |
| Alibaba Cloud Message Queue | Developer Guide | 113 → 386 (+273) | 20220815 → 20260108 | +23 / -21 | +176 / -51 | 0 |
| Data Transmission Service | Developer Guide | 223 → 480 (+257) | 20220913 → 20260313 | +17 / -13 | +137 / -2 | 0 |
| CloudMonitor | User Guide | 205 → 405 (+200) | 20250421 → 20260629 | +38 / -20 | +98 / -12 | 0 |
| AnalyticDB for PostgreSQL | User Guide | 85 → 258 (+173) | 20220915 → 20260630 | +21 / -9 | +47 / -4 | 0 |
| Auto Scaling | Developer Guide | 249 → 420 (+171) | 20220916 → 20250619 | +13 / -25 | +60 / -12 | 0 |

**Four observations that fall out of the diff**

- The largest documented growth is concentrated in a few products: Cloud Defined Storage Developer Guide 783→2021 pp (+169 sentences), DataWorks User Guide 995→1590 pp (+282 sentences), Apsara Uni-manager Operations … Developer Guide 65→580 pp (+39 sentences), API Gateway Developer Guide 196→613 pp (+30 sentences), Container Service for Kubernet … User Guide 320→734 pp (+376 sentences).
- 3 of the 32 paired manuals carry 5 release-notes / what's-new sections of their own (§3 quotes them verbatim); outside these, everything in this note was derived by diffing, not stated by the vendor.
- 8 of the 32 paired manuals contain explicit deprecation / removal wording ("no longer supported", "deprecated" …); they are quoted per manual in §4.
- Largest restructure: **MaxCompute** User Guide dropped 570 section titles — the section titles were re-organised while the page count also moved -148, so content was removed along with the restructure.

## 3. What the product teams wrote themselves

3 paired manuals in this set carry their own release-notes / what's-new section. Those are quoted verbatim below (truncated where long) — they are the only statements in this note written by the vendor rather than derived by diffing.

**release notes for apsara** — same wording in 1 manual: Apsara Uni-manager Operations Console (Developer Guide)

> **Uni-manager Operations** **Console SDK** This topic describes the release notes for the Apsara Uni-manager Operations Console SDK of Apsara Stack V3.18.6, including API releases, modifications, and known issues. **SDK version hisstory**

**version change management** — same wording in 1 manual: Apsara Uni-manager Operations Console (User Guide)

> This page displays all version change tasks that you can view. You can view the details and phases of a specific change task and perform operations on it. **Prerequisites** This page is hidden by default. If needed, you can edit it for display under **Menu** **Management**. **Procedure** 1. Log in to the Apsara Uni-manager Operations Console. 2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Version** **Management**. 3. In the left-side navigation pane, choose **Version Task**. 4. Click **Create a Change Task**. 5.

**release notes for kubernetes 1.34** — same wording in 1 manual: Container Service for Kubernetes (User Guide)

> Container Service for Kubernetes (ACK) strictly complies with the Certified Kubernetes Conformance Program. This topic describes the updates in Kubernetes 1.34, including update notes, major changes, and feature updates. **Component versions** The following table describes the core component versions that are supported by ACK clusters that run Kubernetes 1.34. Container Service for Kubernetes **Major changes** In Kubernetes 1.34, if you select Terway as the network plug-in and select DataPath V2 when you create an ACK cluster, the kube-proxy container no longer runs on nodes on which Terway

**release notes for kubernetes 1.32** — same wording in 1 manual: Container Service for Kubernetes (User Guide)

> Container Service for Kubernetes Container Service for Kubernetes (ACK) is a certified Kubernetes offering. This topic describes the main changes in ACK for Kubernetes versions 1.32 and 1.31, including upgrade notes, major changes, new features, deprecated features and APIs, and feature gates. **Component versions** The following table lists the core component versions for ACK clusters. **Feature changes** Starting from version 1.32, when you create an ACK cluster using the CreateCluster API operation, the default proxy mode for kube-proxy is IPVS instead of iptables.

**release notes for kubernetes 1.30** — same wording in 1 manual: Container Service for Kubernetes (User Guide)

> Container Service for Kubernetes (ACK) strictly abides by the terms of the Certified Kubernetes Conformance Program. This topic describes the updates in Kubernetes 1.30, including update notes, major changes, new features, deprecated features and APIs, and feature gates. **Component versions** The following key component versions are supported by ACK clusters that run Kubernetes 1.30. Container Service for Kubernetes **Update notes** **Features** CVE-2024-10220 vulnerabilities are fixed in 1.30.7-aliyun.1. **Kubernetes 1.29** A sleep mode is added for the PreStop hook.

## 4. Change detail per manual

*31 manuals with material evidence are expanded; 1 further manual changed only cosmetically (re-flow, page numbering, boilerplate) and is tabled at the end of this section.*

### Alibaba Cloud Message Queue — Developer Guide

`113 pages / 20220815` → `386 pages / 20260108` (+273 pages, 196 → 320 sections, 143,271 → 409,295 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Alibaba Cloud Message Queue Developer Guide 20260108.md`

**Text new in this edition** (first lines by section)
- `SDK for Java` — Click the button, choose Middleware > Message Queue (MQ), and set Version to 2018-02-05.
- `Obtain API information and its` — For detailed instructions on using an API operation, refer to the developer guide for the specific cloud product.
- `Obtain API information and its` — From the Version drop-down list, select the target API version.
- `Obtain API information and its` — The page displays a list of all API operations for the current version.
- `Obtain common header` — You can use the API debugging feature in the Apsara Uni-manager Management Console to obtain the ID.
- `Obtain common header` — In the top navigation bar, click Products and choose Developer Tools > API and Tools > Developer Portal.
- `Overview` — You can download this SDK from the platform to directly call Apsara Stack API operations.

**Text no longer present**
- `Usage notes on development` — Select the Apsara Stack version from the drop-down list.
- `Call an API operation` — You can use the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway to call API operations in Apsara Stack.
- `Call an API operation` — Context You can use the POP gateway or the ASAPI gateway to call API operations in Apsara Stack.

**Sections added** (176 total): `Prerequisites`; `Obtain API information and its`; `Obtain common header`; `Obtain STS access credentials`; `Calling private cloud APIs`; `SDK for Java`; `RocketMQ_API`; `QueryCommonGenRedirectUrl` …
**Sections dropped** (51 total): `Getting started`; `Usage notes on development`; `Call an API operation`; `Log on to the API Tool console`; `View the information about API`; `Obtain the values of common` …
**Sections renamed**: `Transport protocol and character encodin …` → `Transport protocol and character`; `ONSClientException construction by using` → `ONSClientException construction by`

### Alibaba Cloud Message Queue — User Guide

`330 pages / 20250725` → `373 pages / 20260629` (+43 pages, 166 → 184 sections, 690,225 → 750,166 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Alibaba Cloud Message Queue User Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Configure logging` — ApsaraMQ for RocketMQ SDK for Java versions earlier than 1.7.8.Final ApsaraMQ for RocketMQ SDK for Java versions earlier than 1.7.8.Final support only Log4j and Logback.
- `Message accumulation in Java` — Alibaba Cloud Message Queue Note ApsaraMQ for RocketMQ can support 1 billion accumulated messages without compromising the performance.
- `Product updates` — To optimize user experience and help new users get started, the procedure for applying for resources has been simplified.
- `Overview` — If a new application needs to access ApsaraMQ for RocketMQ, you must create the following ApsaraMQ for RocketMQ resources for the application:
- `Overview` — You can add, delete, modify, and query the preceding resources in the ApsaraMQ for RocketMQ console or by calling API operations.
- `Query a message trace` — The following versions of SDKs support the message tracing feature:
- `View the operation logs of an` — If you extend the retention period by modifying the logging configurations, the log data before the new retention period is not backfilled.

**Text no longer present**
- `Updates` — To optimize user experience and help new users get started, the resource application process has been simplified.
- `Transactional messages` — The producer sends a new ACK to the Message Queue for Apache RocketMQ broker based on the final status of the local transaction.
- `Resource management overview` — If a new application needs to access Message Queue for Apache RocketMQ, you must create the following Message Queue for Apache RocketMQ resources for the application:

**Sections added** (25 total): `（该章标题在源 PDF 内即为缺字文本，无法还原）`; `Product updates`; `Use the TCP client SDK for Java to send and subscribe to nor …`; `Use the HTTP client SDK for Java to send and subscribe to no …`; `Log on to the console`; `Network management`; `View endpoint information`; `Associate an ApsaraMQ for RocketMQ` …
**Sections dropped** (11 total): `Message Queue for Apache`; `Updates`; `Log on to the Message Queue`; `Resource management overview`; `Query results`; `Dead-letter queues` …
**Sections renamed**: `Query message traces` → `Query a message trace`; `Status in message traces` → `States in message traces`

### AnalyticDB for PostgreSQL — User Guide

`85 pages / 20220915` → `258 pages / 20260630` (+173 pages, 47 → 94 sections, 140,102 → 414,717 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 AnalyticDB for PostgreSQL User Guide 20260630.md`

**Text new in this edition** (first lines by section)
- `Create a vector index` — AnalyticDB for PostgreSQL User G Supported vector operators AnalyticDB for PostgreSQL User G Important Only AnalyticDB for PostgreSQL instances of V6.6.1.0 or later support the following vec …
- `Perform vector search` — AnalyticDB for PostgreSQL User G Note Only AnalyticDB for PostgreSQL instances of V6.3.10.18 or later support approximate index search based on the inner product distance or cosine similarit …
- `Use pgvector-compatible` — AnalyticDB for PostgreSQL vector databases are built based on PostgreSQL 9.4 and do not support the USING heap syntax when tables are created.
- `View performance metrics` — PolarDB for MySQL V2.0 provides rich performance metrics and second-level monitoring frequency, which allow you to easily track the status of clusters and address operational challenges.
- `Label` — Find the instance to which you want to add tags and click the icon in the Tags column.
- `Vector analysis` — Vector analysis is widely used in various fields such as Alibaba Group data mid-end, e-commerce, new retail, Alibaba Cloud City Brain, and Tongyi Qianwen Q&A service.
- `Vector analysis` — Two-way retrieval based on vector search and full-text search AnalyticDB for PostgreSQL vector databases support vector indexes and full-text indexes, and can use vector search and full-text …

**Text no longer present**
- `Import data from or export data to OSS in` — Fault-tolerance parameters When the default values are used for the preceding parameters, a timeout occurs if the transmission rate is lower than 1 Kbit/s for 15 consecutive seconds.
- `Configure a whitelist` — After you clear the default whitelist, it contains only 127.0.0.1.
- `Obtain client tools` — Graphical client tools AnalyticDB for PostgreSQL users can directly use client tools that support Greenplum, such as SQL Workbench, Navicat Premium, and Navicat for PostgreSQL.

**Sections added** (47 total): `Instance specifications`; `Reset the password of an`; `Update the minor engine`; `Label`; `Set instance parameters`; `Manage users and`; `Add a field to a column-`; `Vector analysis` …
**Sections dropped** (4 total): `Reset the password of an account`; `Update the minor engine version`; `Manage users and permissions`; `Add a field to a column-oriented`
**Sections renamed**: `Import data from or export data to OSS i …` → `Import data from or export data to`; `Use the COPY statement to import data` → `Use the COPY statement to import`; `Principles and scenarios of row` → `Principles and scenarios of`

### API Gateway — Developer Guide

`196 pages / 20220915` → `613 pages / 20260629` (+417 pages, 116 → 315 sections, 288,524 → 699,736 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 API Gateway Developer Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Get common header` — Click the button, choose Cloud Platform > Unified Cloud Management Platform, and set Version to 2019-05-10.
- `Obtain API information and` — For instructions on how to use a specific API, see the developer guide for the corresponding cloud product.
- `Obtain API information and` — From the Version drop-down list, select the target API version.
- `Obtain an AccessKey` — If you use an individual account AccessKey, you must add the following restrictive parameters to the header.
- `Get common header` — You can use the online API debugging feature in the Apsara Uni-manager Management Console to quickly obtain the organization ID.
- `Get common header` — You can use the online API debugging feature in the Apsara Uni-manager Management Console to quickly obtain the resource group ID.
- `Obtain user and role` — In the permission list, select API Gateway with Read- Only and Read and write permissions, and then click Next.

**Text no longer present**
- `View information about API operations` — Before you use SDKs, obtain service names, API operation names, and API operation versions.
- `View information about API operations` — Context The API operations on the API Directory page are only for reference.
- `View information about API operations` — Then, you can view the service name, API operation name, and API operation version.
  *… 29 further removed lines*

**Sections added** (159 total): `Obtain API information and`; `Get common header`; `Obtain user and role`; `Obtain the region ID and`; `Calling Apsara Stack APIs`; `Java version`; `Common API call methods`; `API call - Cluster management` …
**Sections dropped** (94 total): `Overview`; `List of operations by function`; `ASAPI Developer Guide`; `Log on to the API Tool console`; `View information about API operations`; `Obtain common header parameters` …
**Sections renamed**: `Obtain an AccessKey pair` → `Obtain an AccessKey`; `Obtain an STS AccessKey pair` → `Obtain an STS AccessKey`; `ModifyApiGroup` → `ModifyGroup`; `CreateApiGroup` → `CreateGroup`

### API Gateway — User Guide

`120 pages / 20220727` → `196 pages / 20260629` (+76 pages, 71 → 82 sections, 170,230 → 304,331 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 API Gateway User Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Import management` — API Gateway supports smooth migration of API definitions, group configurations, and authorization rules from the original API Gateway 1.0 to shared API Gateway instances.
- `API KEY authentication` — API Gateway authentication policies support API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway application, and CSB authentication.
- `BASIC authentication` — API Gateway authentication policies support various authentication methods, such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication.
- `OAuth 2.0 authentication` — API Gateway supports several authentication policies, such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication.
- `Custom authentication` — API Gateway supports several authentication policy methods, such as API key, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication.
- `API Gateway application authentication` — API Gateway supports authentication policies such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway application, and CSB authentication.
- `CSB authentication` — API Gateway authentication policies support several authentication methods, such as API KEY, BASIC, JWT, OAuth 2.0, custom authentication, API Gateway applications, and CSB authentication.
  *… 36 further added lines in this manual*

**Text no longer present**
- `Error code mapping plug-in` — For example, clients support only HTTP status code 200 and want to map HTTP status code 429 that is returned by API Gateway to HTTP status code 200.
- `Configure an account for global` — To configure a global administrator account, you must add the PrimaryKey value of the Level-1 department to which the global administrator account belongs to the desired API Gateway database …
- `Cross-user VPC authorization` — Starting from Apsara Stack V3.8.1, API Gateway provides two internal APIs that allow VPC owners to authorize their VPCs to other users.
  *… 95 further removed lines*

**Sections added** (73 total): `Product introduction`; `Log on to the O&M console`; `Getting started`; `Use routes to access EDAS`; `Use routes to access`; `Instance management`; `Instance list`; `Configure security group rules` …
**Sections dropped** (64 total): `Quick start`; `Create an API with HTTP as the`; `Call an API`; `Manage applications`; `Create an app`; `View app details` …
**Sections renamed**: `JWT authentication plug-in` → `JWT authentication`

### Apsara Uni-manager Operations Console — Developer Guide

`65 pages / 20251106` → `580 pages / 20260703` (+515 pages, 38 → 157 sections, 80,492 → 697,180 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Apsara Uni-manager Operations Console Developer Guide 20260703.md`

**Release notes written in the manual itself**
- *Release notes for Apsara* — **Uni-manager Operations** **Console SDK** This topic describes the release notes for the Apsara Uni-manager Operations Console SDK of Apsara Stack V3.18.6, including API releases, modifications, and known issues.

**Text new in this edition** (first lines by section)
- `Install Apsara Uni-manager Operations Console ` — We recommend that you use the SDK for Java core library 4.6.0 or later, Gson 2.9.1 or later, and the latest version of Apsara Uni-manager Operations Console SDK for Java.
- `Install Apsara Uni-manager Operations Console ` — We recommend that you use the SDK for Python core library 2.11.5 or later, and use the latest version of Apsara Unimanager Operations Console SDK for Python.
- `Permissions required to call` — Currently, API calls support identity verification using an AccessKey.
- `Obtain the service domain` — You can view the intranet and Internet domain names in the Apsara Stack API calls section.
- `Initiate an API request` — Make sure that the account has the permissions to call the API operation.
- `Initiate an API request` — SDKManager is an Ingress gateway that receives all API requests sent from the Apsara Unimanager Operations Console.
- `Initiate an API request` — If Apsara Uni-manager Operations Console SDK for Java includes API operations that belong to multiple services, the API requests may have identical class names.

**Text no longer present**
- `Getting started` — We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.14.0.2.
- `Install SDK for Java` — We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.16.2.0.
- `Initiate a request` — SdkManager receives all O&M requests sent from API gateways.

**Sections added** (110 total): `Release notes for Apsara`; `Unrecommended and`; `Permissions required to call`; `Test network connectivity`; `Confirm the QPS limits of API`; `Install Apsara Uni-manager Operations Console SDK for Java`; `Install Apsara Uni-manager Operations`; `Use Apsara Uni-manager` …
**Sections dropped** (5 total): `Install SDK for Java`; `Configure authentication credentials`; `Handle errors`; `GetAlertList`; `Resource management`
**Sections renamed**: `Initiate a request` → `Initiate an API request`

### Apsara Uni-manager Operations Console — User Guide

`419 pages / 20251106` → `710 pages / 20260703` (+291 pages, 531 → 346 sections, 725,280 → 979,934 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Apsara Uni-manager Operations Console User Guide 20260703.md`

**Release notes written in the manual itself**
- *Version change management* — This page displays all version change tasks that you can view. You can view the details and phases of a specific change task and perform operations on it. **Prerequisites** This page is hidden by default. If needed, you can edit it for display under **Menu** **Management**. **Procedure** 1. Log in to the Apsara Uni-manager Operations Console. 2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Version** **Management**. 3.

**Deprecations / removals stated in the text**
- (Delete an alert blocking rule) You can delete an alert blocking rule that you no longer need.
- (Modify a resource tag) You can delete resource tags that are no longer needed.
- (Delete software) To save storage space, you can delete software that is no longer needed after O&M jobs are executed.
- (Delete a log cleanup rule) You can delete log cleanup rules that are no longer needed.

**Text new in this edition** (first lines by section)
- `Rule management` — Every day at precisely 02:00:00, the system conducts a cleanup of previous execution plans and creates new plans based on the current settings of your log cleanup rules.
- `Rule management` — When setting the upper limit of disk space usage in a rule, make sure the range falls between 0% and 100%, and note that the digit preceding the percent sign (%) must be an integer.
- `User management` — In the Add dialog box, select the user that you created in Step 4 and click OK.
- `Operation platform` — In a single-region scenario, the Operation Platform page displays the following content by default for regular users.
- `Overview` — By default, the system creates system administrators, security administrators, security auditors, and role administrators during initialization.
- `Configure login settings` — In the Add Policy dialog box, configure the parameters described in the following table and click OK.
- `User management` — In the Add Department dialog box, enter a new department name and click OK.
  *… 105 further added lines in this manual*

**Text no longer present**
- `Delete a log cleanup rule` — At 02:00 every day, the system cleans up existing execution plans and generates new execution plans based on the current cleanup rules.
- `Slow I/O analysis` — By default, the system shows the slow I/O list, top ten NCs, cluster statistics, top 5 cluster statistics, and reasons in the last 24 hours.
- `Donghuangzhong configuration` — Host allow port configuration By default, the host network only allows port 22 for networks outside the cloud platform.
  *… 104 further removed lines*

**Sections added** (274 total): `Top navigation bar`; `User information`; `Operation platform`; `Getting Started`; `System administrator`; `Security administrator`; `Configure login settings`; `Security auditor` …
**Sections dropped** (407 total): `Apsara Uni-manager`; `Homepage`; `View the alert list`; `View the details of an alert`; `Change the states of alerts`; `Alert contacts` …
**Sections renamed**: `Operation log audit` → `Operation log auditing`; `Monitoring rule management` → `Monitoring management`; `View the monitoring information of an` → `View the monitoring information of cloud`; `Inspection report` → `Inspection records`

### ApsaraDB for MongoDB — Developer Guide

`221 pages / 20220913` → `223 pages / 20260629` (+2 pages, 121 → 121 sections, 281,634 → 298,408 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for MongoDB Developer Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Procedure for API calls` — By default, Apsara Stack Enterprise Edition V3.16.0 and later versions use the point of presence (POP) gateway to deliver the same user experience as in the Alibaba Cloud public cloud.
- `Apsara Stack documentation` — Click the Enterprise, Agility&XStack, or All-in-one tab based on the Apsara Stack version that you use.
- `Obtain common header` — This topic also explains the response parameters that are returned after you call API operations.
- `Obtain common header` — In the left-side navigation pane, click Replica Set Instances or Sharded Cluster Instances based on the instance type.
- `SDK for Java` — SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.
- `SDK for Go` — By default, certificate authority (CA) certificates on the operating systems are used.
- `SDK for Python` — SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.Proceed with caution.

**Text no longer present**
- `Getting started` — In this example, the ApsaraDB for MongoDB SDK uses version 3.6.3.
- `Install ApsaraDB for MongoDB SDK for Java` — We recommend that you use version 4.5.17 or later for the core library of Apsara Stack SDK for Java.
- `Install ApsaraDB for MongoDB SDK for Java` — In this example, ApsaraDB for MongoDB SDK for Java uses version 3.6.3.
  *… 2 further removed lines*

**Sections added** (13 total): `Procedure for API calls`; `Obtain the information and`; `Obtain common header`; `Troubleshooting`; `Install the core package of SDK for Go`; `Use POP to make API calls`; `SDK for Java`; `SDK for Go` …
**Sections dropped** (17 total): `Usage notes on development`; `Process of API calls`; `Log on to the API Tool console`; `View the API-related information`; `Obtain the values of common`; `Obtain the endpoint of ApsaraDB` …
**Sections renamed**: `IP whitelists and security groups` → `IP whitelists and security`

### ApsaraDB for MongoDB — User Guide

`89 pages / 20220727` → `163 pages / 20260630` (+74 pages, 65 → 102 sections, 122,052 → 240,624 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for MongoDB User Guide 20260630.md`

**Text new in this edition** (first lines by section)
- `View performance metrics` — PolarDB for MySQL V2.0 provides rich performance metrics and second-level monitoring frequency, which allow you to easily track the status of clusters and address operational challenges.
- `Add a mongos node` — In the Mongos List section of the page that appears, click Add Mongos.
- `Add a mongos node` — In the MongoDB sharded cluster add node panel, click Add a new item, and configure the Specifications and Quantity parameters.
- `Add a shard node` — The time required to add shard nodes does not depend on the number of shard nodes that are being added.
- `Upgrade the MongoDB version` — You cannot downgrade the MongoDB version of an instance after you upgrade it.
- `Upgrade the MongoDB version` — In the upper-right corner of the Specification Information section of the page that appears, click Upgrade Database and select the version to which you want to upgrade the instance.
- `Enable the audit log feature` — If you enable the audit log feature for an instance for the first time, the admin and slow operation types are selected by default.

**Text no longer present**
- `Configure TDE for an ApsaraDB` — Before you enable TDE, you can create a MongoDB 4.0 or 4.2 instance to test the compatibility between your application and the database version.
- `Configure a whitelist` — Context The system creates a default whitelist for each instance.
- `Restore data to the current ApsaraDB for` — If you have upgraded the database version, you cannot use the backup files of the earlier database version to restore data.

**Sections added** (40 total): `Instance types`; `Replica set instance types`; `Sharded cluster instance`; `Use the mongo shell to connect to an ApsaraDB for MongoDB in …`; `View the details of an`; `Add a mongos node`; `Add a shard node`; `Change the configurations of one or` …
**Sections dropped** (8 total): `Overview of replica set instance connections`; `View the details of an ApsaraDB`; `Change the name of an instance`; `Configure a primary/secondary switchover`; `Restore backup data to a new ApsaraDB`; `Audit logs` …
**Sections renamed**: `Introduction to connection strings and U …` → `Introduction to connection strings and`; `Configure a primary/secondary failover` → `Configure a primary/secondary`; `Create a dual-zone replica set` → `Create a dual-zone replica`

### Auto Scaling — Developer Guide

`249 pages / 20220916` → `420 pages / 20250619` (+171 pages, 89 → 137 sections, 366,677 → 645,543 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Auto Scaling Developer Guide 20250619.md`

**Text new in this edition** (first lines by section)
- `Process of API calls` — To ensure that Apsara Stack provides the same experience as Alibaba Cloud Public Cloud, API operations in Apsara Stack Enterprise V3.16.0 and later are called by using the POP gateway by def …
- `Process of API calls` — Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway.
- `View the information about` — In the left-side navigation pane, click API fold.
- `Obtain Auto Scaling SDKs` — You can go to the SDK Center to select the SDK version that meets your business requirements.
- `Common parameters` — You cannot configure the x-acsinstanceid header to call API operations to create instances and query instances.
- `AttachVServerGroups` — For information about the vServer group quota, see Limits of Auto Scaling User Guide.
- `CreateEciScalingConfiguration` — Auto Scaling preferentially creates elastic container instances by using the lowest-priced instance type.

**Text no longer present**
- `Obtain Auto Scaling SDKs` — For example, to use Auto Scaling SDK for Java, you must download aliyun-java-sdk-ess and aliyun- Auto Scaling SDKs encapsulate the API that was released on August 28, 2014.
- `Make API calls` — You can use the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway to call ASAPI operations.
- `Make API calls` — Obtain the AccessKey credentials that are required for the API call.

**Sections added** (60 total): `Process of API calls`; `Use Auto Scaling SDK for Java to`; `Use CommonRequest to call API`; `Call examples of Auto`; `Use Auto Scaling SDK for`; `DescribeScalingActivityDetail`; `AttachDBInstances`; `DetachDBInstances` …
**Sections dropped** (12 total): `Usage notes on development`; `Make API calls`; `Obtain the endpoint of Auto`; `Use Auto Scaling SDK for Java to initiate`; `Use CommonRequest to call API operations`; `Call examples of Auto Scaling` …
**Sections renamed**: `View the information about API` → `View the information about`; `Obtain an STS AccessKey 3-tuple` → `Obtain an STS AccessKey 3-`

### Auto Scaling — User Guide

`57 pages / 20220727` → `74 pages / 20260312` (+17 pages, 62 → 74 sections, 92,764 → 129,343 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Auto Scaling User Guide 20260312.md`

**Text new in this edition** (first lines by section)
- `Expected number of instances` — If you do not enable the Expected Number of Instances feature for a scaling group, Auto Scaling rejects new scaling requests when the scaling group has an ongoing scaling activity.
- `Expected number of instances` — Manually execute a scaling rule and add instances at the same time Scenario:** The add1 scaling rule specifies to create one ECS instance.
- `Expected number of instances` — Manually execute the add1 scaling rule and add an existing ECS instance at the same time.
- `Edit scaling groups` — For example, the new scaling configuration appears in the Scaling Group Configuration column.
- `Resolve scaling activity` — If the exception persists after you complete the DIY troubleshooting, submit a ticket to ask for technical support.
- `Create a scaling rule` — For information about the scaling rule quota, see the Limits topic in the Notes chapter of Auto Scaling Use r Guide.

**Text no longer present**
- `Precautions` — Scaling rules ESS uses scaling rules to scale ECS instances in a scaling group based on the minimum and maximum numbers of ECS instances specified for the scaling group.
- `Overview` — Create a scaling configuration Configure the parameters for the scaling configuration, such as Instance Type and Image.
- `Create a scaling group` — When you create a scaling group, you can specify the minimum and maximum numbers of ECS instances that are allowed in the scaling group.

**Sections added** (16 total): `Remove unhealthy ECS`; `Roll back ECS instances`; `Instance lifecycle`; `Quick Start overview`; `Expected number of instances`; `Edit scaling groups`; `Scaling activities`; `View the details of a scaling` …
**Sections dropped** (6 total): `Remove unhealthy ECS instances`; `Instance rollback after a failed`; `Instance lifecycle management`; `Overview`; `Modify a scaling group`; `Put an instance into the Standby`
**Sections renamed**: `Create an event-triggered task` → `Create an event-triggered`; `Modify an event-triggered task` → `Modify an event-triggered`; `Disable an event-triggered task` → `Disable an event-triggered`; `Enable an event-triggered task` → `Enable an event-triggered`

### Cloud Defined Storage — Developer Guide

`783 pages / 20241114` → `2021 pages / 20260629` (+1238 pages, 30 → 896 sections, 2,333,816 → 3,058,424 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Cloud Defined Storage Developer Guide 20260629.md`

**Deprecations / removals stated in the text**
- (Error responses) Error codes Cloud Defined Storage Cloud Defined Storage Cloud Defined Storage Operations not supported by OSS If an operation not supported by OSS is performed to access a resource, OSS retu …

**Text new in this edition** (first lines by section)
- `Installation` — The version of OSS SDK for Python in this topic is compatible with Python 2.6, 2.7, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 or later version.
- `Quick Start` — We recommend SDK core library version 4.5.17 or later, ECS Java SDK version 4.23.2, and EBS Java SDK version 1.0.3.
- `Quick Start` — When using the disk and snapshot features, set the API version to 2014-05-26 and the product name to Ecs.
- `Quick Start` — When using the asynchronous replication and replication pair-consistent group features, set the API version to 2021-07-30 and the product name to ebs.
- `Getting started` — To use the cloud disk and snapshot features, set the API version to 2014-05-26 and the product name to Ecs.
- `Getting started` — To use the asynchronous replication and replication pair-consistent group features, set the API version to 2021-07-30 and the product name to ebs.
- `Getting started` — When you use disk or snapshot features, set the API version to 2014-05-26 and the product name to Ecs.
  *… 129 further added lines in this manual*

**Text no longer present**
- `ASAPI Developer Guide` — ASAPI SDK for Java version 1.0.6.7-RELEASE supports Apsara Stack Agility v3.6 and later, Apsara Stack Enterprise v3.14.0 and later, Apsara Stack Enterprise v3.13.0 SP002+, and Apsara Stack E …
- `ASAPI Developer Guide` — ASAPI SDK for Python version 2.4.7.1-RELEASE supports Apsara Stack Agility v3.6 and later, Apsara Stack Enterprise v3.14.0 and later, Apsara Stack Enterprise v3.13.0 SP002+, and Apsara Stack …
- `ASAPI Developer Guide` — ASAPI SDK for Java version 1.0.2.5-RELEASE supports Apsara Stack Enterprise v3.12.0, Apsara Stack Enterprise v3.13.0, and Apsara Stack Agility v3.5.
  *… 103 further removed lines*

**Sections added** (612 total): `Introduction to the OSS API`; `Access control`; `User Signature Authentication`; `Add signatures to the Authorization`; `FAQ`; `Generate a signed URL`; `Temporary access authorization`; `Bucket ACL` …
**Sections dropped** (3 total): `ASAPI Developer Guide`; `NAS`; `Call examples for SDK for Python`

### Cloud Defined Storage — User Guide

`691 pages / 20240703` → `963 pages / 20260629` (+272 pages, 196 → 165 sections, 1,669,115 → 3,145,729 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Cloud Defined Storage User Guide 20260629.md`

**Deprecations / removals stated in the text**
- (2.1.1.1.2. ACL) You can also delete exported historical inventory lists that you no longer need.
- (Buckets) Delete a single previous version Find the version that you no longer use and click Delete in the Operation column.
- (Delete objects) You can delete uploaded objects in the OSS console when they are no longer needed.

**Limits and quotas that changed**
- new · *4.2.9.4.2. limits on data import from elastics …* · Size of a single data record | The maximum size of a single data record is 3 MB. If the size of a single data record exceeds the maximum size, the data record is discarde …
- new · *4.2.9.4.2. limits on data import from elastics …* · Number of data import configurations | The maximum number of data import configurations that can be created in a single project is 100, regardless of configuration types. …
- new · *4.2.9.4.2. limits on data import from elastics …* · Bandwidth | When a data import job reads data from an Alibaba Cloud Elasticsearch cluster over a virtual private cloud (VPC), the default maximum network bandwidth that i …
- new · *4.2.9.4.2. limits on data import from elastics …* · Number of concurrent jobs | A data import job pulls Elasticsearch data in Scroll mode. In this mode, the total number of shards that are used for concurrent jobs cannot e …
- new · *4.2.9.4.2. limits on data import from elastics …* · Number of shards in a Logstore | The write performance of Simple Log Service varies based on the number of shards in a Logstore. A single shard supports a maximum data wr …
- new · *4.2.9.4.2. limits on data import from elastics …* · Network | If you use an Alibaba Cloud Elasticsearch cluster in a VPC or use a self-managed Elasticsearch cluster on an Elastic Compute Service (ECS) instance, you can rea …

**Text new in this edition** (first lines by section)
- `4.3.1.1.3. Logtail configuration files and rec` — Microsoft Windows Server 2008 Microsoft Windows Server 2012 Microsoft Windows Server 2016 Microsoft Windows Server 2019 Microsoft Windows 7 Microsoft Windows 10 Microsoft Windows Server Vers …
- `4.3.2.2. Logtail and LoongCollector compatibil` — Alibaba Cloud Linux 3.2 ARM Anolis OS 8.2 ARM or later CentOS 8.4 ARM Debian 11.2 and 12.2 ARM Ubuntu 20.04, 22.04, and 24.04 ARM The minimum required CPU architecture is ARMv8.2-A.
- `4.11.2. Use custom policies to grant permissio` — Allow access requests from specific IP addresses The following project policy is used to allow access requests for the exampleproject project from only 192.168.0.0/16 and 172.16.0.1:
- `2.1.1.2.2. ACL` — ItemLimitNotesObject key lengthMaximum 1,023 bytesThis includes the full path with all directory prefixesObjects per bucketUnlimitedNo hard limit on the number of objectsDirectory depthNo ha …
- `2.1.1.3.8. TLS` — Cloud Defined Storage If you disable TLS version management, TLS 1.2 and TLS 1.3 are supported by default.
- `2.1.1.3.8. TLS` — Downgrading the TLS version, such as changing the TLS version from TLS 1.3 to TLS 1.2, or disabling TLS version management may cause security and compliance issues.
- `What is Log Service?` — Log Service provides more than 200 built-in functions, more than 400 regular expressions, and flexible user-defined functions that allow you to filter, split, convert, enrich, and replicate …
  *… 169 further added lines in this manual*

**Text no longer present**
- `Mount an SMB file system` — Double-click Internet Protocol Version 4 (TCP/IPv4) to open the Internet Protocol Version 4 (TCP/IPv4) Properties dialog box, and then click Advanced.
- `Configure hotlink protection for a bucket` — If you add www.example.com to the Referer whitelist, requests sent from URLs that start with www.example.com, such as www.example.com/123 and www.example.com.cn are allowed.
- `Usage notes` — File gateways only support file and directory names that are encoded in UTF-8.
  *… 74 further removed lines*

**Sections added** (91 total): `CDS`; `What is Object Storage Service (OSS)`; `2.1.1.1.2. ACL`; `2.1.1.3.5. Access permissions and account authorization`; `2.1.1.3.8. TLS`; `2.1.1.4.1. IMG`; `Notes`; `Common tools` …
**Sections dropped** (145 total): `Cloud Defined Storage`; `Features`; `Usage notes`; `Log on to the OSS console`; `Create a bucket`; `Upload objects` …
**Sections renamed**: `Search for and view an automatic snapsho …` → `3.6.2. Search for and view an automatic …`; `Activate a replication pair-consistent g …` → `3.8.1. Create and activate a replication …`; `Associate Log Service with external data` → `4.4.14. Associate Log Service with exter …`; `Use open source Flink to consume log dat …` → `4.7.6. Use open source Apache Flink to c …`

### CloudMonitor — Developer Guide

`174 pages / 20250312` → `552 pages / 20260629` (+378 pages, 20 → 197 sections, 248,133 → 678,646 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 CloudMonitor Developer Guide 20260629.md`

**Limits and quotas that changed**
- new · *maxcompute quota groups* · (ECS) system load Load1 | Count/s | SystemLoad1 | userId and instanceId | The system load in the last minute.
- new · *maxcompute quota groups* · (ECS) system load Load5 | Count/s | SystemLoad5 | userId and instanceId | The system load in the last 5 minutes.

**Text new in this edition** (first lines by section)
- `DescribeSiteMonitorQuota` — CloudMonitor Queries the quotas and version of site monitoring.

**Text no longer present**
- `Common parameters` — To obtain the values of the Product and Version parameters in the Apsara Uni-manager Management Console, perform the following steps:
- `Common parameters` — If you do not specify the request headers when you call an API operation, the root organization and root resource set are used by default.

**Sections added** (181 total): `Preparations`; `Obtain the endpoint`; `Monitoring data on time series`; `DescribeMetricData`; `DescribeMetricTop`; `Custom monitoring`; `PutCustomMetric`; `DescribeCustomMetricList` …
**Sections dropped** (5 total): `CloudMonitor API`; `Common parameters`; `Metrics for Apsara Stack`; `Cloud Products`; `Threshold-triggered alert rules`

### CloudMonitor — User Guide

`205 pages / 20250421` → `405 pages / 20260629` (+200 pages, 48 → 138 sections, 305,046 → 558,330 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 CloudMonitor User Guide 20260629.md`

**Deprecations / removals stated in the text**
- (Custom dashboards) After you specify a dashboard as the default dashboard, the previous default dashboard is no longer the default, and the details page of the default dashboard is automatically displayed when …

**Text new in this edition** (first lines by section)
- `Kubernetes container monitoring` — For instances that support Prometheus monitoring 2.0, click the instance name to go to the Kubernetes container monitoring page.
- `Kubernetes container` — Support Prometheus monitoring 2.0, providing detailed monitoring for core components, nodes, applications, networks, GPUs, and big data/AI workloads.
- `Kubernetes container` — The Kubernetes container monitoring page displays a list of Kubernetes clusters with columns for Instance ID/Name, Organization/Resource Set, Region, Instance Status, Prometheus monitoring 2 …
- `Kubernetes container` — For an instance that does not support Prometheus monitoring 2.0, click its Instance ID/Name to view the cluster details page.
- `Holographic View` — By default, the system displays the Global View for All Spaces over the Last 6 Hours.
- `Alert list` — In the timeline section, add events such as Alert Triggered, Alert Investigation, root cause analysis, Alert Closed, and Alert Response.
- `Alert list` — In the Add Timeline Event panel, configure Select Node, Time, and Description.

**Text no longer present**
- `Custom dashboards` — Click the downward arrow next to the icon in the upper-right corner of the New Board page and select a refresh interval for the dashboard from the drop-down list.
- `Custom dashboards` — Click Set the dashboard in the upper-right corner of the New Board page.
- `Custom dashboards` — In the Copy dashboard dialog box, enter a new dashboard name and select the folder to which you want to copy the dashboard.

**Sections added** (98 total): `Alert center`; `Alert overview`; `Alert list`; `Notification policy`; `Blocking policies`; `Process monitoring`; `View host monitoring details`; `Cloud product monitoring` …
**Sections dropped** (12 total): `CloudMonitor`; `Monitor processes`; `Metrics`; `View the monitoring data`; `View alert rules`; `Use the initiative alerting` …
**Sections renamed**: `Cloud service monitoring` → `Cloud resource monitoring`

### Container Service for Kubernetes — Developer Guide

`98 pages / 20220915` → `186 pages / 20251202` (+88 pages, 17 → 90 sections, 230,762 → 271,003 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Container Service for Kubernetes Developer Guide 20251202.md`

**Text new in this edition** (first lines by section)
- `Use CommonRequest` — The following sample RPC call contains the service (ACK), API operation (CreateCluster), and version (2015-12-15) information.
- `Use CommonRequest` — Container Service for Kubernetes The following sample RPC call contains the service (ACK), API operation (CreateCluster), and version (2015-12-15) information.
- `View the information about an` — In the Version drop-down list, select the required API version.
- `View the information about an` — Below the API list, you can view all API interfaces for the current version.
- `Use CommonRequest` — SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.
- `Use CommonRequest` — Container Service for Kubernetes Container Service for Kubernetes Configure a proxy You can configure the HTTP_PROXY and HTTPS_PROXY environment variables when you call API operations.
- `Use CommonRequest` — By default, certificate authority (CA) certificates on the operating systems are used.

**Text no longer present**
- `Getting started` — Usage notes on development documentation This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).
- `Getting started` — Make API calls You can use the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway to call Apsara Stack API operations.
- `Getting started` — Obtain the AccessKey pair that is required for the API call.

**Sections added** (76 total): `Log on to OpenAPI Explorer`; `View the information about an`; `Obtain an AccessKey pair`; `Obtain an STS AccessKey pair`; `Obtain the values of common header`; `Obtain the information and the`; `Obtain the Container Service SDK`; `Examples of using Container` …
**Sections dropped** (7 total): `Getting started`; `Examples of using Container Service SDK for Java`; `Examples of using Container Service SDK for Python`; `Examples of using Container Service SDK for Go`; `Container Service API invocation`; `Use the ASAPI gateway to call API operations` …

### Container Service for Kubernetes — User Guide

`320 pages / 20220916` → `734 pages / 20260629` (+414 pages, 137 → 234 sections, 519,091 → 1,570,883 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Container Service for Kubernetes User Guide 20260629.md`

**Release notes written in the manual itself**
- *Release notes for Kubernetes 1.34* — Container Service for Kubernetes (ACK) strictly complies with the Certified Kubernetes Conformance Program. This topic describes the updates in Kubernetes 1.34, including update notes, major changes, and feature updates. **Component versions** The following table describes the core component versions that are supported by ACK clusters that run Kubernetes 1.34.
- *Release notes for Kubernetes 1.32* — Container Service for Kubernetes Container Service for Kubernetes (ACK) is a certified Kubernetes offering. This topic describes the main changes in ACK for Kubernetes versions 1.32 and 1.31, including upgrade notes, major changes, new features, deprecated features and APIs, and feature gates. **Component versions** The following table lists the core component versions for ACK clusters.

**Deprecations / removals stated in the text**
- (Release notes for Kubernetes 1.34) In Kubernetes 1.34, the kubelet server no longer supports the TLS_RSA_WITH_AES_256_GCM_SHA384 and TLS_RSA_WITH_AES_128_GCM_SHA256 Transport Layer Security (TLS) cipher suites.
- (Release notes for Kubernetes 1.32) Starting from version 1.32, kube-apiserver no longer supports the TLS_RSA_WITH_AES_256_GCM_SHA384 and TLS_RSA_WITH_AES_128_GCM_SHA256 TLS cipher suites.
- (Release notes for Kubernetes 1.32) Starting from version 1.32, when you enable the RAM Roles for Service Accounts (RRSA) feature, the -- api-audiences parameter of kube-apiserver is no longer modified and retains its previous …
- (Kubernetes 1.26 release notes) Before you update your cluster to Kubernetes 1.26, check whether the controller or application that needs to interact with the deprecated beta APIs is updated to use the recommended API vers …

**Text new in this edition** (first lines by section)
- `Configure RAM role authorization for ack-ai-` — In the left-side navigation pane, select 2015-05-01 from the Version drop-down list, enter CreatePolicy in the search box, and then find and click CreatePolicy.
- `Configure RAM role authorization for ack-ai-` — In the left-side navigation pane, select 2015-05-01 from the Version drop-down list, enter AttachPolicyToRole in the search box, and then find and click AttachPolicyToRole.
- `CPU Burst` — Alibaba Cloud Linux 2 provides the CPU Burst feature in kernel version 4.19.91-22.al7.
- `Release notes for Kubernetes 1.34` — This capability was available in Kubernetes 1.31, and has been enhanced in Kubernetes 1.34 with Snapshottable API server cache, allowing the cache to serve the latest data and historical ver …
- `Release notes for Kubernetes 1.30` — We recommend that you use flowcontrol.apiserver.k8s.io/v1 API (available in Kubernetes 1.29 and later versions) or flowcontrol.apiserver.k8s.io/v1beta3 API (available in Kubernetes 1.26 and …
- `Kubernetes 1.26 release notes` — Therefore, Kubernetes 1.26 does not support containerd 1.5 or earlier.
- `Kubernetes 1.26 release notes` — The feature gate is removed from the kubelet in Kubernetes 1.24 and removed from the API server in Kubernetes 1.26.
  *… 336 further added lines in this manual*

**Text no longer present**
- `Update the Kubernetes version of a cluster` — If the deprecated API versions are used in a cluster whose Kubernetes version is earlier than 1.18, you must replace these API versions with new API versions before you update the Kubernetes …
- `Ingress configurations` — Currently, only Ingress controllers of 0.12.0-5 and later versions support traffic splitting.
- `Create an Ingress in the console` — Only Ingress controllers of 0.12.0-5 and later versions support traffic splitting.
  *… 56 further removed lines*

**Sections added** (137 total): `Product Announcements`; `ACK release notes`; `Lifecycle of ACK clusters`; `Release notes for Kubernetes 1.34`; `Kubernetes 1.28 release notes`; `ACK support for Kubernetes 1.22`; `Container Service support for Kubernetes 1.20`; `1.2. [CVE] CVE vulnerability fixes` …
**Sections dropped** (46 total): `Announcements`; `Container Service support for`; `in NVIDIA GPU drivers`; `Procedure`; `Log on to the Container Service`; `Create a Kubernetes cluster` …
**Sections renamed**: `Vulnerability fixed: CVE-2021-` → `Vulnerability fixed: CVE-2021-1056 in NV …`; `Schedule an application pod to a specifi …` → `Schedule an application pod to a specifi …`; `Use kritis-validation-hook to` → `kritis-validation-hook`; `Create an Ingress in the console` → `Create an Ingress in the ACK console`

### Data Management — User Guide

`226 pages / 20220916` → `239 pages / 20260629` (+13 pages, 125 → 133 sections, 413,754 → 478,325 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Data Management User Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Control modes` — Data Management Note The instances that are managed in Stable Change mode consume the billing quota of the instances that are managed in Security Collaboration mode.
- `Global search` — Data Management (DMS) provides the global search feature to allow you to quickly find the desired instances, databases, and tables managed by DMS or the features of DMS.
- `Import data` — By default, you can execute only the INSERT and REPLACE statements to import data to database instances that are managed in Security Collaboration mode.
- `Manage projects` — To add available iteration templates to the project, select the iteration templates that you want to add in the All Iteration Templates section and click the icon.
- `Create an iteration template` — Data Management Data Management Note You can select multiple ticket states that allow the iteration to advance to the next stage based on your requirements.
- `Orchestrate tasks` — In the Add Transaction Market dialog box, configure the Transaction Market Name and Description parameters.
- `Run a script by using SSH after you` — In the Add Machine Cluster dialog box, configure the Cluster Name, Primary Machine, and Secondary Machine parameters.

**Text no longer present**
- `Control modes` — The instances that are managed in Stable Change mode consume the billing quota of the instances that are managed in Security Collaboration mode.
- `Manage schema versions` — Save new schema versions New schema versions are saved when the following operations are performed in DMS:
- `Schema design` — Context When you create projects, process new business requirements, or optimize business operations, you may need to change schemas.

**Sections added** (23 total): `Global search`; `Enable metadata access`; `Manage data in a single`; `Use the schema design feature to`; `Create shadow tables for`; `Import data`; `Create an iteration template`; `Run a script by using SSH after you` …
**Sections dropped** (14 total): `Experience the new version of the DMS`; `Enable metadata access control`; `Single database query`; `Synchronize shadow tables`; `Manage iteration templates`; `Batch processing` …
**Sections renamed**: `Register database instances with` → `Register a database instance`; `Customize the layout and style of the DM …` → `Customize the layout and style of the`; `Super SQL mode` → `Use the super SQL mode`; `Repair table consistency` → `Repair table inconsistency`

### Data Transmission Service — Developer Guide

`223 pages / 20220913` → `480 pages / 20260313` (+257 pages, 11 → 161 sections, 533,800 → 661,207 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Data Transmission Service Developer Guide 20260313.md`

**Text new in this edition** (first lines by section)
- `Quick start` — We recommend that you use SDK core library version 4.5.17 or later and SDK version 5.1.25.
- `Obtain an AccessKey pair` — You can use one type of access credential for authentication when you make an API request.
- `Obtain an AccessKey pair` — We recommend that you use the AccessKey pairs of personal accounts to call API operations in Apsara Stack services and perform operations in the Apsara Uni-manager Management Console.
- `Obtain common header` — This topic also describes the return values of specific parameters after you call API operations.
- `Install Apsara Stack SDK for Java` — To use the DTS SDK for Java, install the core library of Apsara Stack SDK for Java and DTS SDK for Java, and add the following dependencies to the pom.xml file:
- `Use CommonRequest to call API` — You can call the newly released API operations of an Apsara Stack service without the need to update the SDK for the service.
- `Use CommonRequest to call API` — You can obtain the values of these parameters from the API references.

**Text no longer present**
- `Common parameters` — Sample responses Data Transmission Service (DTS) API uses standard HTTP status codes to indicate whether the call is successful.
- `Common parameters` — If you cannot identify the cause of the error, you can contact the Alibaba Cloud and provide the returned HostId and RequestId for technical support.
- `DTS API (new)` — Related API operations ConfigureDtsJob ConfigureSubscription DescribeDtsJobDetail DescribeDtsJobs The value of the Reserve parameter is a JSON string.

**Sections added** (137 total): `Preparations`; `Log on to OpenAPI Explorer`; `Obtain the information and`; `Obtain an AccessKey pair`; `Obtain access credentials`; `Obtain common header`; `Obtain the endpoint of DTS`; `Use the SDK for Java` …
**Sections dropped** (2 total): `Use the ASAPI gateway to call API operations`; `Use the ASAPI gateway to make API calls`

### DataWorks — User Guide

`995 pages / 20220916` → `1590 pages / 20260629` (+595 pages, 481 → 662 sections, 1,706,114 → 2,738,354 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 DataWorks User Guide 20260629.md`

**Deprecations / removals stated in the text**
- (Add an SAP HANA data source) Other SAP HANA versions have not been tested and are not supported by default.
- (Configure ClickHouse Reader) Other data types in the open source ClickHouse official data type collection are not supported.
- (Configure RestAPI Reader) Scheduling parameters are not supported for a batch synchronization task that uses RestAPI Reader.

**Text new in this edition** (first lines by section)
- `Configure a real-time full-database` — The default values of the Shards and Replica Shards parameters are 1.
- `PyODPS 2 node` — PyODPS 2 nodes support ODPS SQL queries and allow you to read the execution results.
- `PyODPS 3 node` — This means that instance.open_reader uses the Result API, which can retrieve a maximum of 10,000 records.
- `Usage overview` — By default, the metrics whose fluctuating values are greater than 0 are displayed.
- `What is DataWorks?` — This version improves the data development system by supporting dual-project development, isolating development and production environments, enforcing development standards, and reducing cod …
- `Create a workspace` — After the workspace is created, you can refresh the workspace list to view the new workspace.
- `Create a synchronization node` — You can add data sources, create destination tables, configure synchronization nodes, and commit synchronization nodes to migrate and synchronize data in an efficient and stable manner.
  *… 242 further added lines in this manual*

**Text no longer present**
- `View the summary information about API` — View rankings Top 10 API Operations with Highest Error Rate Yesterday section In this section, you can view the top 10 APIs with the highest call error rate in the past 24 hours.
- `Configure HDFS Writer` — HDFS Writer can be used in the environment where Hive 1.1.1 and Hadoop 2.7.1 (JDK version:
- `Create an API in the codeless UI` — If the API may return more than 2,000 records, we recommend that you select Paginat ion.
  *… 212 further removed lines*

**Sections added** (342 total): `What is DataWorks?`; `Prerequisites`; `Log on to DataWorks console`; `Create an exclusive resource`; `Create a workspace`; `Create tables and upload data`; `Overview of the DataWorks`; `Manage workspace members and roles` …
**Sections dropped** (231 total): `Create a synchronization`; `Create tables and import data`; `Upload and reference an authentication`; `Data source isolation`; `Sync data monitoring`; `Manage connection permissions` …
**Sections renamed**: `Manage users` → `Manage clusters`; `Configure AnalyticDB for MySQL 2.0 Write …` → `Configure an AnalyticDB for MySQL V2.0`; `Configure an HBase data source` → `Configure a DataHub data source`; `Configure a HybridDB for MySQL` → `Configure a HybridDB for MySQL data`

### Elastic Compute Service — Developer Guide

`855 pages / 20220916` → `836 pages / 20260312` (-19 pages, 220 → 221 sections, 1,332,550 → 1,420,314 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Elastic Compute Service Developer Guide 20260312.md`

**Text new in this edition** (first lines by section)
- `Obtain API information` — To call API operations by using an SDK, you must obtain information that includes the service name, API operation name, and API version.
- `Obtain API information` — Elastic Compute Service Background information The information on the API directory page of the Apsara Uni-manager Management Console is for reference only.
- `Obtain API information` — In the API list, you can view the names of all API operations in the current API version.
- `Obtain API information` — If multiple API versions exist, you can select a required API version from the Version drop-down list.
- `RAM authorization` — Resources involved in ECS API operations describes the resources involved in each ECS API operation.
- `Common parameters` — Common request parameters Elastic Compute Service You can obtain the values of the Product and Version parameters in the Apsara Uni-manager Management Console.
- `CreateInstance` — Elastic Compute Service If the instance type supports user data, you can specify UserData .

**Text no longer present**
- `ModifyInstanceSpec` — After you change the instance type or the network bandwidth of an instance, you cannot initiate another change for this instance within 5 minutes.
- `Obtain API information` — To call API operations by using an SDK, you must first obtain information about the service name, API operation name, and API version.
- `Obtain API information` — Context The information on the API Directory page of the Apsara Uni-manager Management Console is for reference only.
  *… 14 further removed lines*

**Sections added** (13 total): `Use CommonRequest to call API`; `StartInstances`; `RebootInstances`; `DeleteInstances`; `ModifyInstanceMetadataOptions`; `DescribeInstanceAttribute`; `DescribeDeploymentSetSupportedInstanceTypeFamily`; `ModifyDiskSpec` …
**Sections dropped** (12 total): `Obtain the endpoint of ECS`; `Use CommonRequest to call API operations`; `ImportKeyPair`; `DescribeDiskMonitorData`; `DescribeInstanceMonitorData`; `JoinResourceGroup` …
**Sections renamed**: `Obtain an STS AccessKey 3-tuple` → `Obtain an STS AccessKey 3-`

### MaxCompute — Developer Guide

`34 pages / 20220726` → `316 pages / 20260629` (+282 pages, 32 → 191 sections, 43,124 → 702,816 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 MaxCompute Developer Guide 20260629.md`

**Limits and quotas that changed**
- new · *limits of maxcompute sql statements* · Partitions that can be queried | 10,000 | Quantity | | A maximum of 10,000 partitions can be queried. |
- new · *limits of maxcompute sql statements* · SQL execution plans | 1 MB | Size | | The size of the execution plan generated by MaxCompute SQL cannot exceed 1 MB. Otherwise, FAILED: ODPS- |
- new · *limits of maxcompute sql statements* · \0 or \00 | Ending character

**Text new in this edition** (first lines by section)
- `UPDATE and DELETE` — To handle this issue, we recommend that you use the MaxCompute client whose version must be 0.35.0.
- `3.6.2.2. CHR` — The default value 1 indicates the position where a substring matches pattern in the search for the first time.
- `Python 3 UDF` — To enable Python 3 for a job, add the following command before the required SQL statement and execute them together:
- `Implementation principles and feature descript` — For example, the compiler can determine that the value returned by java.util.Arrays.asList(new java.math.BigInteger('1')) is of the java.util.List<java.math.BigInteger> type based on the par …
- `Java SDK` — This document introduces the MaxCompute Java SDK packages and links to the complete API reference.
- `Java SDK` — Complete API reference for MaxCompute Use Maven to manage the SDK version.
- `Volume2` — Before you manage external volumes by using the SDK for Java, you need to add the following dependency:
  *… 45 further added lines in this manual*

**Text no longer present**
- `SDK for Java` — For example, to specify the version of odps-sdk-core that you want to use, add the following Maven dependency:
- `Obtain the AccessKey pair of an Alibaba Cloud` — AccessKey pairs allow you to access Apsara Stack resources with full permissions for your account.
- `SDK for Python` — DataFrame PyODPS provides a pandas-like API called PyODPS DataFrame.

**Sections added** (144 total): `Obtain an endpoint`; `Volume2`; `MaxCompute SQL`; `Scenarios`; `Reserved words`; `Partitioned table`; `Type conversion`; `3.1.4.5. Conversions between the STRING and DATETIME types` …
**Sections dropped** (2 total): `SDK for Java`; `View the endpoint`
**Sections renamed**: `Log on to the Apsara Uni-manager Managem …` → `1.2.2.1. Log on to the Apsara Uni-manage …`; `Obtain the AccessKey pair of an Alibaba …` → `1.2.2.3. Obtain the AccessKey pair of an …`

### MaxCompute — User Guide

`781 pages / 20220830` → `633 pages / 20260629` (-148 pages, 908 → 342 sections, 1,478,863 → 982,785 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 MaxCompute User Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Instance operations` — For example, you can configure show p -all -limit 100 to enable the system to return information about 100 instances executed in the current project.
- `Terms` — If you want to use new data types introduced in the MaxCompute V2.0 data type edition, you preceding table can contain NULL values.
- `Terms` — For some operations or built-in functions that use new data types for parameters and return values, if the MaxCompute V2.0 data type edition is disabled, these operations or built-in functio …
- `Use PyODPS in DataWorks` — This means that instance.open_reader uses the Result interface by default, which has a limit and can retrieve a maximum of 10,000 data records.
- `Sequence` — DataFrame does not support the TIMESTAMP and STRUCT types that are introduced in MaxCompute V2.0.
- `Column operations` — Although the DataFrame API does not support chained comparisons, such as 3 <= String operations The DataFrame API provides several operations for Sequence or scalar objects of the string typ …
- `Use UDFs and the third-party Python` — Therefore, we recommend that you make sure your code runs normally before you write production code by using MapReduce API in Python 3.
  *… 76 further added lines in this manual*

**Text no longer present**
- `Backup and restoration` — After you run the restore table table_name PARTITION(pt='1') PARTITION(pt='2') to LSN '102'; command, the pt1 partition is restored to the version that corresponds to LSN 102 and the pt2 par …
- `Instance operations` — For example, you can use show p -all -limit 100 to return information about 100 instances executed in the current project.
- `Terms` — Basic data types mon commands If you want to use the new data types in MaxCompute V2.0, you must first add one of the following flags to values.
  *… 173 further removed lines*

**Sections added** (103 total): `Log on to the Apsara Uni-`; `Create a task account`; `Add and remove users`; `Create roles and grant`; `Basic concepts and`; `Examples of uploading and`; `FAQ related to data upload and`; `Multi-engine support` …
**Sections dropped** (570 total): `Log on to the Apsara Uni-manager`; `Create an Apsara Stack tenant`; `Add and delete a user`; `Create and authorize a role`; `Write and run a Graph job`; `Use Logview to view job running` …
**Sections renamed**: `Configure the MaxCompute client` → `Configure the MaxCompute`; `UDF example` → `UDF examples`; `Selection of tools to migrate data to` → `Selection of tools to migrate`; `Java sandbox limits` → `Java sandbox limitations`

### Resource Orchestration Service — Developer Guide

`189 pages / 20220915` → `172 pages / 20260312` (-17 pages, 77 → 76 sections, 289,601 → 276,827 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Resource Orchestration Service Developer Guide 20260312.md`

**Text new in this edition** (first lines by section)
- `SDK for Java` — In this example, the Resource Orchestration Service (ROS) service, the ListStacks operation, and the 2019-09-10 version are used.
- `Call an API operation` — Resource Orchestration Service Apsara Stack allows you to call API operations by using the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway.
- `Obtain the information and` — In the API operation list, view all API operations of the current version.
- `Preparations` — You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID.
- `SDK for Java` — To view the recommended SDK version and sample code, perform the following operations:
- `SDK for Java` — In the top navigation bar of the page that appears, choose API Integration > SDK Sample Code.
- `SDK for Java` — The SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues.

**Text no longer present**
- `Call an API operation` — Apsara Stack allows you to call API operations by using the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway.
- `View the information about API` — View and remember the service name, API operation name, and API version.
- `Obtain the values of common` — Response parameters The following table describes the response parameters that are returned by default when you call operations to query the instances of cloud services.

**Sections added** (9 total): `Go to OpenAPI Explorer`; `Obtain the information and`; `Install the core package of SDK for Go`; `Use CommonRequest to call API`; `Use POP to make API calls`; `SDK for Java`; `SDK for Go`; `SDK for Python` …
**Sections dropped** (13 total): `Log on to the API Tool console`; `View the information about API`; `Obtain the endpoint of ROS`; `Get started with ROS SDK for Java`; `Get started with ROS SDK for Go`; `Install Go SDK` …
**Sections renamed**: `Obtain an STS AccessKey 3-tuple` → `Obtain an STS AccessKey 3-`

### Resource Orchestration Service — User Guide

`545 pages / 20220713` → `476 pages / 20260312` (-69 pages, 103 → 110 sections, 734,932 → 702,556 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Resource Orchestration Service User Guide 20260312.md`

**Text no longer present**
- `Update a stack` — In the Conf irm step, confirm the template and stack configurations, and click Updat e St ack.
- `ALIYUN::ROS::WaitConditionHandle` — Therefore, you must rsion command to query the version number.

**Sections added** (8 total): `View a stack`; `Modify a template`; `Configure sharing settings`; `View operation logs`; `Redis`; `ALIYUN::REDIS::Instance`; `PAI`; `ALIYUN::PAI::Service`
**Sections dropped** (1 total): `Edit a template`

### Server Load Balancer — Developer Guide

`283 pages / 20220915` → `326 pages / 20251028` (+43 pages, 123 → 135 sections, 449,892 → 517,971 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Server Load Balancer Developer Guide 20251028.md`

**Text new in this edition** (first lines by section)
- `Procedure for API calls` — To ensure that Apsara Stack provides the same experience as Alibaba Cloud public cloud, API operations in Apsara Stack Enterprise V3.16.0 and later are called through the POP gateway by defa …
- `Procedure for API calls` — Apsara Stack allows you to call API operations through the point of presence (POP) gateway.
- `Procedure for API calls` — Server Load Balancer Note When you call an API operation, add the organization ID and resource set ID to the header parameters to specify the organization and resource set to which the resou …
- `Obtain API information and its` — From the Version drop-down list, select the API version.
- `Obtain API information and its` — Select the corresponding API operation and obtain the POP endpoint information of the cloud service under the parameter name.
- `Preparations` — From the Version drop-down list, select the API version that you want to use.
- `Preparations` — Select the corresponding API operation and obtain the POP Endpoint information under the parameter name.

**Text no longer present**
- `Obtain the SLB SDK` — For example, to use SLB SDK for Java, you must download aliyun-java-sdk-sl and The SLB SDK encapsulates the API released on May 15, 2014.
- `Call an API operation` — To ensure that Apsara Stack provides the same user experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterpr …
- `Call an API operation` — Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway.

**Sections added** (21 total): `Procedure for API calls`; `Log on to OpenAPI Explorer`; `Obtain API information and its`; `SDK for Java`; `SDK for Go`; `Python version`; `Use SLB SDK for Go to`; `Access method` …
**Sections dropped** (9 total): `Call an API operation`; `Log on to the API Tool console`; `View information about an API`; `Obtain the endpoint of the SLB`; `Use SLB SDK for Go to make`; `Make API requests` …
**Sections renamed**: `Use ASAPI to make API calls` → `Use POP to make API calls`; `Call examples for SDK for Java` → `Call examples for SDK for`; `Primary/secondary server groups` → `Primary/secondary server`

### Server Load Balancer — User Guide

`64 pages / 20220913` → `126 pages / 20260629` (+62 pages, 51 → 67 sections, 111,459 → 234,245 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Server Load Balancer User Guide 20260629.md`

**Deprecations / removals stated in the text**
- (Release an SLB instance) You can release SLB instances that are no longer needed to reduce costs.
- (Overview) Not ice Internal-facing SLB instances of the classic network type are no longer available for purchase.
- (Overview) Not ice Shared-performance SLB instances are no longer available for purchase.

**Text new in this edition** (first lines by section)
- `Enable Proxy Protocol to` — NGINX Plus R16 and later and open source NGINX 1.13.11 and later support Proxy Protocol V2.
- `Certificate overview` — Server Load Balancer You can add up to 600 certificates with each account.
- `Preparations` — Before you use SLB, you must create ECS instances that function as backend servers, deploy applications on the ECS instances, and then add the ECS instances to your SLB instance to process c …
- `Configure an SLB instance` — You can set bandwidth caps to limit the service capabilities of applications.
- `Configure an SLB instance` — In the Backend Servers step, perform the following steps to add backend servers.
- `Configure an SLB instance` — Set the Server Group Type parameter to Default Server Group.
- `Configure an SLB instance` — On the Default Server Group tab, specify the backend ports that are used by backend ECS instances to receive requests.
  *… 21 further added lines in this manual*

**Text no longer present**
- `What is SLB?` — Benefits High availability SLB is designed with full redundancy to eliminate single points of failure and support zone-disaster recovery.
- `Preparations` — Select an instance type Shared-resource SLB instances share resources with each other.
- `Preparations` — Add backend servers Before you use the SLB service, you must create ECS instances, deploy applications on the ECS instances, and then associate the ECS instances with your SLB instance to pr …
  *… 11 further removed lines*

**Sections added** (29 total): `Enable Proxy Protocol to`; `Instance management`; `Instance overview`; `Create and manage SLB instances`; `Configure and manage listeners`; `Domain name extensions`; `SLB additional domain names`; `Add and manage additional domain` …
**Sections dropped** (12 total): `Start and stop an SLB instance`; `Enable access control`; `Disable access control`; `Add backend servers to the default server`; `Add on-premises servers to the default`; `Add ECS instances to a vServer group` …

### Virtual Private Cloud — Developer Guide

`498 pages / 20220916` → `517 pages / 20260629` (+19 pages, 235 → 211 sections, 853,576 → 749,386 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Virtual Private Cloud Developer Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Obtain VPC SDK` — For example, to use VPC SDK for Java, you must download aliyun-java-sdk-vpc and VPC SDK encapsulates the API released on April 28, 2016.
- `Procedure for API calls` — Virtual Private Cloud Apsara Stack allows you to call API operations by using the point of presence (POP) gateway.
- `Procedure for API calls` — Obtain the AccessKey credentials that are required when you call an API operation.
- `Use CommonRequest to call API` — You must obtain the value of the Action parameter and specify an API operation in For example, if you want to call the DescribeVpcs operation, you must use request.setSysAction("DescribeVpcs …
- `Call Python SDK` — After installing the Alibaba Cloud Python SDK, you can write code to use the Alibaba Cloud Python SDK to access the POP gateway of Apsara Stack and call API operations of the Apsara Uni-mana …
- `Call Python SDK` — When you call a specific API, configure the parameters based on their positions specified in the development documentation.
- `Call Go SDK` — After installing the Alibaba Cloud Go SDK, you can write code to access the POP Gateway of Alibaba Cloud and call API operations of the Apsara Uni-manager Management Console.

**Text no longer present**
- `Call API operations` — Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway.
- `Call API operations` — Obtain the AccessKey pair that is required for the API call.
- `View the information about API` — Context The API operations on the API Directory page are only for reference.

**Sections added** (31 total): `Procedure for API calls`; `Log in to OpenAPI Explorer`; `Use CommonRequest to call API`; `Call Python SDK`; `Call Go SDK`; `List of operations by function`; `Sign an API request`; `ListVpcIpv6Isps` …
**Sections dropped** (56 total): `Call API operations`; `Log on to the API Tool console`; `Call examples for SDK for Java`; `Use CommonRequest to call API operations`; `Call examples for SDK for Python`; `Overview` …
**Sections renamed**: `View the information about API` → `View the information about`; `Obtain an STS AccessKey 3-tuple` → `Obtain an STS AccessKey 3-`; `Obtain the values of common headers` → `Obtain the values of common`; `Call examples for SDK for Go` → `Call examples for SDK for`

### Virtual Private Cloud — User Guide

`69 pages / 20220719` → `163 pages / 20260629` (+94 pages, 51 → 80 sections, 109,973 → 298,760 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 Virtual Private Cloud User Guide 20260629.md`

**Deprecations / removals stated in the text**
- (Create a VPC with an IPv6) Configure security group rules** Communication between services that are assigned IPv4 addresses and services that are assigned IPv6 addresses is not supported.
- (Manage associated resources) After the network ACL is disassociated from the vSwitch, the network ACL no longer controls traffic of the ECS instances connected to the vSwitch.
- (Overview of EIP) You can also disassociate and release an EIP that you no longer need.
- (Disassociate an EIP from a) After the EIP is disassociated from the cloud resource, the cloud resource can no longer access the Internet by using the EIP.

**Text new in this edition** (first lines by section)
- `Overview` — The VPC Organization Quota Usage section shows the VPC quota consumption over the past 7, 15, or 30 days.
- `Overview` — The EIP Organization Quota Usage section displays the EIP quota consumption for the last 7, 15, or 30 days.
- `VPCs` — Apsara Stack allows you to perform the following operations in the VPC console and by calling API operations:
- `VPCs` — Apsara Stack allows you to query, create, modify, and delete vSwitches in the VPC console and by calling API operations.
- `VPCs` — You can add custom routes to the system route table and custom route tables to route traffic to specific next hops.
- `Create a VPC with an IPv6` — By default, IPv6 addresses are used only for communication within private networks.
- `Create a VPC with an IPv6` — Purchase IPv6 Internet bandwidth** By default, IPv6 addresses are used only for communication within private networks.
  *… 7 further added lines in this manual*

**Text no longer present**
- `Overview` — Add the following route entry to VPC1 Add the following route entry to VPC2 Connect two VPCs through a VPN gateway The following figure shows that VPC1 (172.16.0.0/12) is connected to VPC2 ( …
- `Create an IPv6 VPC` — Purchase an IPv6 public bandwidth plan By default, IPv6 addresses can be used for communication only within private networks.
- `Overview` — By default, IPv4 and IPv6 addresses provided for VPCs support only communication over private networks.
  *… 5 further removed lines*

**Sections added** (50 total): `Plan networks`; `Plan a VPC`; `Create a VPC with an IPv6`; `Add subnet routes to a route`; `Configure a NAT gateway`; `Configure an EIP`; `Enable IPv6 for a VPC`; `Enable IPv6 for a vSwitch` …
**Sections dropped** (29 total): `Design networks`; `Create an IPv6 VPC`; `VPCs and VSwitches`; `VPC management`; `Create a VPC`; `Delete a secondary IPv4 CIDR block` …
**Sections renamed**: `Create a VPC with an IPv4 CIDR` → `Create a VPC with an IPv4`; `Add a secondary IPv4 CIDR block` → `Manage secondary IPv4 CIDR blocks`; `Disassociate HAVIPs from` → `Disassociate an EIP from a`; `Associate HAVIPs with backend` → `Associate HAVIPs with backend cloud`

### VPN Gateway — Developer Guide

`103 pages / 20220913` → `173 pages / 20250619` (+70 pages, 33 → 91 sections, 257,486 → 255,980 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 VPN Gateway Developer Guide 20250619.md`

**Text new in this edition** (first lines by section)
- `Call an API operation` — To ensure that Apsara Stack provides the same experience as Alibaba Cloud Public Cloud, API operations in Apsara Stack Enterprise V3.16.0 and later are called by using the POP gateway by def …
- `View the information about` — View and record the service name, API operation name, and API version of the API operation that you want to call.
- `Obtain the endpoint of VPN` — To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.
- `Use CommonRequest to call API` — SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.
- `Use CommonRequest to call API` — SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.Proceed with caution.
- `Use CommonRequest to call API` — By default, certificate authority (CA) certificates on the operating systems are used.

**Text no longer present**
- `Call an API operation` — Apsara Stack allows you to call API operations by using the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway.
- `Call an API operation` — To ensure that Apsara Stack provi Not e You can still use the ASAPI gateway to call API operations.
- `Obtain API information` — To call API operations by using an SDK, you must first obtain information about the service name, API operation name, and API version.

**Sections added** (54 total): `Usage notes on development`; `Log on to OpenAPI Explorer`; `View the information about`; `Obtain the values of common`; `Obtain the endpoint of VPN`; `Install VPC SDK for Java`; `Configure authentication credentials`; `Configure connection requests` …
**Sections dropped** (9 total): `Usage notes on development documentation`; `Log on to the API Tool console`; `Obtain API information`; `Obtain the values of common header parameters`; `Obtain the endpoint of VPN Gateway`; `Call examples for SDK for Java` …
**Sections renamed**: `Obtain an STS AccessKey 3-tuple` → `Obtain an STS AccessKey 3-`; `Call examples for SDK for Go` → `Call examples for SDK for`

### VPN Gateway — User Guide

`39 pages / 20220913` → `56 pages / 20260629` (+17 pages, 39 → 28 sections, 57,695 → 84,155 characters). Evidence file: `Alibaba Cloud Apsara Stack V3.18.6 VPN Gateway User Guide 20260629.md`

**Text new in this edition** (first lines by section)
- `Overview of IPsec-VPN connections` — All gateway devices that support the two protocols can connect to VPN gateways on Apsara Stack.
- `Connect a data center to a VPC` — In the Add Route Entry dialog box, configure the following parameters and click OK.
- `Manage destination-based routes` — In the Edit route entry dialog box, select a new weight and click OK.
- `Manage tags` — In the Edit Tags dialog box, configure the following parameters, click Add to add multiple tags, and then click OK.
- `Manage tags` — In the Batch Add Tags dialog box, click Add, configure the Tag Key and Tag Value parameters, and then click OK.
- `Manage tags` — After you add tags to VPN gateways, you can efficiently filter VPN gateways by tag.

**Text no longer present**
- `What is VPN Gateway?` — All on-premises gateway devices that support these two protocols can connect to VPN gateways on Alibaba Cloud.
- `IPsec-VPN overview` — All gateway devices that support the two protocols can connect to VPN gateways on Alibaba Cloud.
- `IPsec-VPN overview` — You must make sure that the security group rules applied to the Elastic Compute Service (ECS) instances in the VPC allow gateway devices in the data center to access cloud resources.

**Sections added** (13 total): `Log on to the VPC console`; `Getting started`; `Overview of IPsec-VPN connections`; `Overview of SSL-VPN`; `Create and manage a VPN`; `Customer gateways`; `Create and manage a`; `Create and manage IPsec-VPN` …
**Sections dropped** (25 total): `Log on to the VPN Gateway`; `IPsec-VPN overview`; `SSL-VPN overview`; `Manage a VPN Gateway`; `Create a VPN gateway`; `Modify a VPN gateway` …
**Sections renamed**: `Manage a destination-based route` → `Manage destination-based routes`

<details><summary>Manuals with cosmetic-only differences</summary>

| product | manual | pages | doc date |
|---|---|---|---|
| Elastic Compute Service | Introduction to Instance | 36 → 57 | 20230419 → 20260629 |

</details>
## 5. Manuals that have no V3.16.2 counterpart (delta not computable)

255 of the 287 V3.18.6 manuals have no same-name, same-document-type counterpart in the 53-manual V3.16.2 English set. The baseline published only User, Developer and Instance-Families guides, so most Product Introduction, Operations and O&M volumes enter this list **by construction**, together with every product documented in English for the first time. Each manual below is matched against the *previous English product names* and classified by how close the closest name is — treat near-matches as catalogue restructuring or renames to verify, not as confirmed new products.

- **Product already in the baseline, manual type is new (38)** — e.g. DataWorks (Developer Guide), Data Transmission Service (User Guide), Elastic Compute Service (User Guide), Data Management (Developer Guide), Cloud Defined Storage (Operations and Maintenance Guide), Elastic Compute Service (Operations and Maintenance Guide); full list in the table.
- **Closest earlier name ≥ 0.5 similarity (136)** — the closest *string* match, shown per row with its score. The score is a search hint only, **not** evidence of a rename: string similarity also pairs unrelated products (ApsaraDB for RDS scores 0.933 against ApsaraDB for Redis). Verify before treating any row here as renamed / split by sub-edition.
- **No close predecessor (81)** — first English appearance of the product: Realtime Compute for Apache Flink (Compu … (User Guide, 524 pp), Cloud Security Network Detection and Res … (Developer Guide, 457 pp), Lindorm (Developer Guide, 426 pp), ApsaraDB for POLARDB PolarDB for Postgre … (User Guide, 371 pp), Realtime Compute for Apache Flink (Compu … (Developer Guide, 370 pp), Apsara Stack Resilience ASR for Geo-disa … (Developer Guide, 360 pp), OpenTrek Dev (Developer Guide, 279 pp), Alibaba Cloud Security-Web Application F … (Developer Guide, 218 pp), Apsara Stack Resilience ASR for Geo-disa … (User Guide, 204 pp), Alibaba Cloud Security-Web Application F … (Developer Guide, 196 pp), ApsaraDB for POLARDB PolarDB for MySQL ( … (Operations and Maintenance Guide, 192 pp), Tair（Redis OSS-compatible） (User Guide, 172 pp); full list in the table.

| product (V3.18.6) | manual | pages | doc date | closest earlier English name (string score) |
|---|---|---|---|---|
| Alibaba Cloud Message Queue | Operations and Maintenance | 58 | 20260629 | Alibaba Cloud Message Queue (1.0) |
| Alibaba Cloud Message Queue | Product Introduction | 27 | 20260629 | Alibaba Cloud Message Queue (1.0) |
| Alibaba Cloud Security-Web Application Firewall (WAF) | Developer Guide | 218 | 20251212 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) | Operations and Maintenance | 32 | 20260629 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) | Product Introduction | 14 | 20260629 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) | User Guide | 60 | 20260629 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) … | Developer Guide | 196 | 20260629 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) … | Operations and Maintenance | 10 | 20260629 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) … | Product Introduction | 12 | 20260629 | — none — |
| Alibaba Cloud Security-Web Application Firewall (WAF) … | User Guide | 54 | 20260629 | — none — |
| AnalyticDB for PostgreSQL | Developer Guide | 90 | 20260630 | AnalyticDB for PostgreSQL (1.0) |
| AnalyticDB for PostgreSQL | Operations and Maintenance | 91 | 20260630 | AnalyticDB for PostgreSQL (1.0) |
| API Gateway | Operations and Maintenance | 11 | 20260629 | API Gateway (1.0) |
| API Gateway | Product Introduction | 14 | 20260629 | API Gateway (1.0) |
| Application Hybrid Marketplace | Operations and Maintenance | 13 | 20260630 | — none — |
| Application Hybrid Marketplace | Product Introduction | 8 | 20260630 | — none — |
| Application Hybrid Marketplace | User Guide | 31 | 20260630 | — none — |
| Application Load Balancer | Product Introduction | 20 | 20260701 | Server Load Balancer (0.585) |
| Application Load Balancer | User Guide | 136 | 20260701 | Server Load Balancer (0.585) |
| Application Real-time Monitoring Service | Developer Guide | 110 | 20250619 | — none — |
| Application Real-time Monitoring Service | Operations and Maintenance | 31 | 20251205 | — none — |
| Application Real-time Monitoring Service | Product Introduction | 14 | 20260629 | — none — |
| Application Real-time Monitoring Service | User Guide | 153 | 20260629 | — none — |
| Apsara AIOps | Operations and Maintenance | 22 | 20260701 | ApsaraDB for Redis (0.593) |
| Apsara AIOps | Product Introduction | 11 | 20260701 | ApsaraDB for Redis (0.593) |
| Apsara AIOps | User Guide | 21 | 20260701 | ApsaraDB for Redis (0.593) |
| Apsara Big Data Manager | Operations and Maintenance | 8 | 20260629 | Data Management (0.588) |
| Apsara Big Data Manager | Product Introduction | 12 | 20251027 | Data Management (0.588) |
| Apsara Big Data Manager | User Guide | 50 | 20260629 | Data Management (0.588) |
| Apsara Copilot | Developer Guide | 57 | 20260701 | Apsara Stack Security (0.562) |
| Apsara Copilot | Product Introduction | 9 | 20260701 | Apsara Stack Security (0.562) |
| Apsara Copilot | User Guide | 61 | 20260701 | Apsara Stack Security (0.562) |
| Apsara Stack DNS | Developer Guide | 239 | 20250627 | Apsara Stack Security (0.727) |
| Apsara Stack DNS | Operations and Maintenance | 19 | 20260310 | Apsara Stack Security (0.727) |
| Apsara Stack DNS | Product Introduction | 16 | 20250924 | Apsara Stack Security (0.727) |
| Apsara Stack DNS (Multicloud Integration) | User Guide | 19 | 20251103 | Apsara Stack Security (0.519) |
| Apsara Stack DNS (Within Cloud) | User Guide | 66 | 20260310 | Apsara Stack Security (0.636) |
| Apsara Stack Resilience | Product Introduction | 29 | 20260701 | Apsara Stack Security (0.65) |
| Apsara Stack Resilience ASR for Zone-disaster Recovery | Developer Guide | 118 | 20260701 | — none — |
| Apsara Stack Resilience ASR for Backup and Recovery | Developer Guide | 279 | 20260701 | Apsara Stack Security (0.508) |
| Apsara Stack Resilience ASR for Backup and Recovery | Operations and Maintenance | 141 | 20260701 | Apsara Stack Security (0.508) |
| Apsara Stack Resilience ASR for Backup and Recovery | User Guide | 299 | 20260701 | Apsara Stack Security (0.508) |
| Apsara Stack Resilience ASR for Geo-disaster | Developer Guide | 360 | 20260701 | — none — |
| Apsara Stack Resilience ASR for Geo-disaster | Operations and Maintenance | 96 | 20260701 | — none — |
| Apsara Stack Resilience ASR for Geo-disaster | User Guide | 204 | 20260701 | — none — |
| Apsara Stack Resilience ASR for Zone-disaster Recovery | Operations and Maintenance | 100 | 20260701 | — none — |
| Apsara Stack Resilience ASR for Zone-disaster Recovery | User Guide | 122 | 20260701 | — none — |
| Apsara Stack Resilience Cloud Platform Backup | User Guide | 13 | 20260701 | Apsara Stack Security (0.542) |
| Apsara Stack Resilience Cloud Platform Backup and O&M … | — | 12 | 20260701 | — none — |
| Apsara Stack Security Security Administrator Guide | — | 38 | 20250529 | Apsara Stack Security (0.594) |
| Apsara Uni-manager | Developer Guide | 1123 | 20260630 | Apsara Uni-manager Management Console (0.653) |
| Apsara Uni-manager | Operations and Maintenance | 74 | 20260629 | Apsara Uni-manager Management Console (0.653) |
| Apsara Uni-manager | Product Introduction | 22 | 20260629 | Apsara Uni-manager Management Console (0.653) |
| Apsara Uni-manager | User Guide | 1380 | 20260701 | Apsara Uni-manager Management Console (0.653) |
| Apsara Uni-manager Operations Console | Operations and Maintenance | 25 | 20260703 | Apsara Uni-manager Operations Console (1.0) |
| Apsara Uni-manager Operations Console | Product Introduction | 19 | 20260703 | Apsara Uni-manager Operations Console (1.0) |
| Apsara Uni-manager Operations Console Platform Operati … | Operations Guide | 1253 | 20260703 | Apsara Uni-manager Operations Console (0.68) |
| ApsaraDB for MongoDB | Operations and Maintenance | 90 | 20260629 | ApsaraDB for MongoDB (1.0) |
| ApsaraDB for MongoDB | Product Introduction | 13 | 20260629 | ApsaraDB for MongoDB (1.0) |
| ApsaraDB for POLARDB | Product Introduction | 29 | 20260629 | ApsaraDB for MongoDB (0.778) |
| ApsaraDB for POLARDB PolarDB for MySQL (Primary_Second … | Developer Guide | 126 | 20260630 | — none — |
| ApsaraDB for POLARDB PolarDB for MySQL (Primary_Second … | Operations and Maintenance | 192 | 20260630 | — none — |
| ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_S … | Developer Guide | 158 | 20260630 | — none — |
| ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_S … | Operations and Maintenance | 117 | 20260630 | — none — |
| ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_S … | User Guide | 371 | 20260630 | — none — |
| ApsaraDB for POLARDB PolarDB-X 2.0 | Developer Guide | 179 | 20260629 | ApsaraDB for MongoDB (0.609) |
| ApsaraDB for POLARDB PolarDB-X 2.0 | Operations and Maintenance | 87 | 20260629 | ApsaraDB for MongoDB (0.609) |
| ApsaraDB for POLARDB PolarDB-X 2.0 | User Guide | 198 | 20260629 | ApsaraDB for MongoDB (0.609) |
| ApsaraDB for RDS | Developer Guide | 397 | 20260313 | ApsaraDB for Redis (0.933) |
| ApsaraDB for RDS | Operations and Maintenance | 196 | 20260629 | ApsaraDB for Redis (0.933) |
| ApsaraDB for RDS | Product Introduction | 38 | 20260629 | ApsaraDB for Redis (0.933) |
| ApsaraDB for RDS ApsaraDB RDS for MySQL | User Guide | 181 | 20260629 | ApsaraDB RDS for SQL Server (0.607) |
| ApsaraDB for RDS ApsaraDB RDS for PolarDB | User Guide | 159 | 20260629 | ApsaraDB RDS for SQL Server (0.552) |
| ApsaraDB for RDS ApsaraDB RDS for PostgreSQL | User Guide | 159 | 20260629 | AnalyticDB for PostgreSQL (0.557) |
| ApsaraStack Parallel File System | Developer Guide | 59 | 20260701 | Apsara Stack Security (0.583) |
| ApsaraStack Parallel File System | Operations and Maintenance | 18 | 20260701 | Apsara Stack Security (0.583) |
| ApsaraStack Parallel File System | Product Introduction | 11 | 20260701 | Apsara Stack Security (0.583) |
| ApsaraStack Parallel File System | User Guide | 14 | 20260701 | Apsara Stack Security (0.583) |
| Auto Scaling | Operations and Maintenance | 9 | 20250619 | Auto Scaling (1.0) |
| Auto Scaling | Product Introduction | 9 | 20250728 | Auto Scaling (1.0) |
| Bare Metal Computing Platform | Developer Guide | 158 | 20251205 | — none — |
| Bare Metal Computing Platform | Operations and Maintenance | 60 | 20260630 | — none — |
| Bare Metal Computing Platform | Product Introduction | 13 | 20250930 | — none — |
| Bare Metal Computing Platform | User Guide | 121 | 20260630 | — none — |
| BareMetal Mangement Service | Operations and Maintenance | 41 | 20260630 | Data Management (0.615) |
| BareMetal Mangement Service | User Guide | 60 | 20260630 | Data Management (0.615) |
| BareMetal Mangement Service | Developer Guide | 139 | 20251205 | Data Management (0.615) |
| BareMetal Mangement Service | Product Introduction | 11 | 20251205 | Data Management (0.615) |
| Cloud Defined Storage | Operations and Maintenance | 327 | 20260630 | Cloud Defined Storage (1.0) |
| Cloud Defined Storage | Product Introduction | 37 | 20260629 | Cloud Defined Storage (1.0) |
| cloud gateway | Developer Guide | 71 | 20250924 | API Gateway (0.636) |
| cloud gateway | Operations and Maintenance | 132 | 20260310 | API Gateway (0.636) |
| cloud gateway | Product Introduction | 15 | 20260310 | API Gateway (0.636) |
| cloud gateway | User Guide | 26 | 20260310 | API Gateway (0.636) |
| cloud migration hub | Product Introduction | 12 | 20260303 | CloudMonitor (0.552) |
| cloud migration hub | User Guide | 133 | 20251217 | CloudMonitor (0.552) |
| Cloud Parallel File Storage | Developer Guide | 38 | 20260701 | Cloud Defined Storage (0.744) |
| Cloud Parallel File Storage | Operations and Maintenance | 22 | 20260701 | Cloud Defined Storage (0.744) |
| Cloud Parallel File Storage | Product Introduction | 10 | 20260701 | Cloud Defined Storage (0.744) |
| Cloud Parallel File Storage | User Guide | 19 | 20260701 | Cloud Defined Storage (0.744) |
| Cloud Security Firewall | Developer Guide | 114 | 20251212 | Cloud Defined Storage (0.5) |
| Cloud Security Firewall | Operations and Maintenance | 8 | 20260629 | Cloud Defined Storage (0.5) |
| Cloud Security Firewall | Product Introduction | 9 | 20251030 | Cloud Defined Storage (0.5) |
| Cloud Security Firewall | User Guide | 53 | 20251030 | Cloud Defined Storage (0.5) |
| Cloud Security Management Center | Developer Guide | 262 | 20260701 | Data Management (0.558) |
| Cloud Security Management Center | Operations and Maintenance | 13 | 20260701 | Data Management (0.558) |
| Cloud Security Management Center | Product Introduction | 26 | 20260701 | Data Management (0.558) |
| Cloud Security Management Center | User Guide | 56 | 20260701 | Data Management (0.558) |
| Cloud Security Network Detection and Response | Developer Guide | 457 | 20260702 | — none — |
| Cloud Security Network Detection and Response | Operations and Maintenance | 19 | 20260317 | — none — |
| Cloud Security Network Detection and Response | Product Introduction | 18 | 20260629 | — none — |
| Cloud Security Network Detection and Response | User Guide | 33 | 20260629 | — none — |
| Cloud Security Scanner | Developer Guide | 233 | 20260701 | Cloud Defined Storage (0.513) |
| Cloud Security Scanner | Operations and Maintenance | 15 | 20260701 | Cloud Defined Storage (0.513) |
| Cloud Security Scanner | Product Introduction | 12 | 20260701 | Cloud Defined Storage (0.513) |
| Cloud Security Scanner | User Guide | 47 | 20260701 | Cloud Defined Storage (0.513) |
| Cloud-native Gateway | Product Introduction | 12 | 20260630 | NAT Gateway (0.714) |
| Cloud-native Gateway | User Guide | 188 | 20260630 | NAT Gateway (0.714) |
| CloudMonitor | Product Introduction | 18 | 20260629 | CloudMonitor (1.0) |
| Container Registry | Developer Guide | 148 | 20251202 | Container Service for Kubernetes (0.522) |
| Container Registry | Operations and Maintenance | 8 | 20260629 | Container Service for Kubernetes (0.522) |
| Container Registry | Product Introduction | 12 | 20260629 | Container Service for Kubernetes (0.522) |
| Container Registry | User Guide | 110 | 20260629 | Container Service for Kubernetes (0.522) |
| Container Security Service | Developer Guide | 189 | 20260701 | Container Service for Kubernetes (0.604) |
| Container Security Service | Operations and Maintenance | 50 | 20260701 | Container Service for Kubernetes (0.604) |
| Container Security Service | Product Introduction | 28 | 20260701 | Container Service for Kubernetes (0.604) |
| Container Security Service | User Guide | 69 | 20260701 | Container Service for Kubernetes (0.604) |
| Container Service for Kubernetes | Operations and Maintenance | 26 | 20260629 | Container Service for Kubernetes (1.0) |
| Container Service for Kubernetes | Product Introduction | 23 | 20251202 | Container Service for Kubernetes (1.0) |
| Container Service for Kubernetes Distributed Cloud Con … | Product Introduction | 12 | 20260629 | Container Service for Kubernetes (0.598) |
| Container Service for Kubernetes Distributed Cloud Con … | User Guide | 22 | 20260629 | Container Service for Kubernetes (0.598) |
| Data Management | Developer Guide | 443 | 20260313 | Data Management (1.0) |
| Data Management | Product Introduction | 20 | 20250730 | Data Management (1.0) |
| Data Transmission Service | Operations and Maintenance | 32 | 20260629 | Data Transmission Service (1.0) |
| Data Transmission Service | Product Introduction | 20 | 20251205 | Data Transmission Service (1.0) |
| Data Transmission Service | User Guide | 680 | 20260629 | Data Transmission Service (1.0) |
| Database Backup | Developer Guide | 12 | 20250529 | — none — |
| Database Backup | Operations and Maintenance | 14 | 20250626 | — none — |
| Database Backup | User Guide | 52 | 20250529 | — none — |
| Database Security Audit | Developer Guide | 98 | 20260701 | Apsara Stack Security (0.55) |
| Database Security Audit | Operations and Maintenance | 29 | 20260701 | Apsara Stack Security (0.55) |
| Database Security Audit | Product Introduction | 14 | 20260701 | Apsara Stack Security (0.55) |
| Database Security Audit | User Guide | 121 | 20260701 | Apsara Stack Security (0.55) |
| DataHub | Developer Guide | 128 | 20260311 | DataWorks (0.5) |
| DataHub | Operations and Maintenance | 95 | 20260629 | DataWorks (0.5) |
| DataHub | Product Introduction | 9 | 20260306 | DataWorks (0.5) |
| DataHub | User Guide | 167 | 20260629 | DataWorks (0.5) |
| DataWorks | Developer Guide | 1018 | 20260629 | DataWorks (1.0) |
| DataWorks | Operations and Maintenance | 137 | 20251204 | DataWorks (1.0) |
| DataWorks | Product Introduction | 36 | 20260629 | DataWorks (1.0) |
| Elastic Compute Service | Operations and Maintenance | 210 | 20260629 | Elastic Compute Service (1.0) |
| Elastic Compute Service | Product Introduction | 31 | 20260312 | Elastic Compute Service (1.0) |
| Elastic Compute Service | User Guide | 511 | 20260629 | Elastic Compute Service (1.0) |
| Elastic File System NAS | Developer Guide | 145 | 20260701 | Elastic IP Address (0.611) |
| Elastic File System NAS | Operations and Maintenance | 35 | 20260701 | Elastic IP Address (0.611) |
| Elastic File System NAS | Product Introduction | 11 | 20260701 | Elastic IP Address (0.611) |
| Elastic File System NAS | User Guide | 42 | 20260701 | Elastic IP Address (0.611) |
| Elasticsearch | Developer Guide | 177 | 20260629 | Elastic Compute Service (0.647) |
| Elasticsearch | Operations and Maintenance | 127 | 20260629 | Elastic Compute Service (0.647) |
| Elasticsearch | Product Introduction | 15 | 20260629 | Elastic Compute Service (0.647) |
| Elasticsearch | User Guide | 186 | 20260629 | Elastic Compute Service (0.647) |
| Enterprise Distributed Application Service | Developer Guide | 201 | 20260701 | Resource Orchestration Service (0.567) |
| Enterprise Distributed Application Service | Operations and Maintenance | 71 | 20260701 | Resource Orchestration Service (0.567) |
| Enterprise Distributed Application Service | Product Introduction | 16 | 20260701 | Resource Orchestration Service (0.567) |
| Enterprise Distributed Application Service | User Guide | 1118 | 20260701 | Resource Orchestration Service (0.567) |
| Express Connect | Developer Guide | 151 | 20251028 | — none — |
| Express Connect | Operations and Maintenance | 46 | 20260310 | — none — |
| Express Connect | Product Introduction | 8 | 20260310 | — none — |
| Express Connect | User Guide | 50 | 20260629 | — none — |
| File Storage NAS | Developer Guide | 129 | 20260701 | Cloud Defined Storage (0.606) |
| File Storage NAS | Operations and Maintenance | 14 | 20260701 | Cloud Defined Storage (0.606) |
| File Storage NAS | Product Introduction | 8 | 20260701 | Cloud Defined Storage (0.606) |
| File Storage NAS | User Guide | 68 | 20260701 | Cloud Defined Storage (0.606) |
| IDaaS | Developer Guide | 555 | 20260629 | DataWorks (0.571) |
| IDaaS | Operations and Maintenance | 20 | 20260629 | DataWorks (0.571) |
| IDaaS | Product Introduction | 11 | 20251216 | DataWorks (0.571) |
| IDaaS | User Guide | 250 | 20260630 | DataWorks (0.571) |
| Key Management Service | Developer Guide | 127 | 20260701 | Data Management (0.588) |
| Key Management Service | Operations and Maintenance | 25 | 20260701 | Data Management (0.588) |
| Key Management Service | Product Introduction | 9 | 20260701 | Data Management (0.588) |
| Key Management Service | User Guide | 44 | 20260701 | Data Management (0.588) |
| Lindorm | Developer Guide | 426 | 20250825 | — none — |
| Lindorm | Operations and Maintenance | 27 | 20260630 | — none — |
| Lindorm | Product Introduction | 11 | 20250930 | — none — |
| Lindorm | User Guide | 49 | 20260630 | — none — |
| Managed Service for Prometheus | Developer Guide | 24 | 20260422 | Container Service for Kubernetes (0.643) |
| Managed Service for Prometheus | Operations and Maintenance | 13 | 20260422 | Container Service for Kubernetes (0.643) |
| Managed Service for Prometheus | Product Introduction | 16 | 20260703 | Container Service for Kubernetes (0.643) |
| Managed Service for Prometheus | User Guide | 80 | 20260703 | Container Service for Kubernetes (0.643) |
| MaxCompute | Operations and Maintenance | 174 | 20251205 | MaxCompute (1.0) |
| MaxCompute | Product Introduction | 24 | 20260629 | MaxCompute (1.0) |
| Message Queue for Apache Kafka | Developer Guide | 125 | 20251203 | — none — |
| Message Queue for Apache Kafka | Operations and Maintenance | 44 | 20260629 | — none — |
| Message Queue for Apache Kafka | Product Introduction | 17 | 20260629 | — none — |
| Message Queue for Apache Kafka | User Guide | 160 | 20260629 | — none — |
| NFV Cloud Firewall | Developer Guide | 178 | 20260701 | Cloud Defined Storage (0.514) |
| NFV Cloud Firewall | Product Introduction | 14 | 20260701 | Cloud Defined Storage (0.514) |
| NFV Cloud Firewall | User Guide | 205 | 20260701 | Cloud Defined Storage (0.514) |
| OpenTrek AgentRuntime | Product Introduction | 16 | 20260629 | — none — |
| OpenTrek AgentRuntime | User Guide | 73 | 20260629 | — none — |
| OpenTrek AI Gateway | Product Introduction | 23 | 20260629 | API Gateway (0.667) |
| OpenTrek AI Gateway | User Guide | 358 | 20260629 | API Gateway (0.667) |
| OpenTrek AI Studio | Operations and Maintenance | 25 | 20260630 | — none — |
| OpenTrek AI Studio | Product Introduction | 12 | 20260630 | — none — |
| OpenTrek Dev | Developer Guide | 279 | 20260630 | — none — |
| OpenTrek Dev | Operations and Maintenance | 76 | 20260630 | — none — |
| OpenTrek Dev | Product Introduction | 32 | 20260630 | — none — |
| OpenTrek-Ops | Product Introduction | 14 | 20260630 | — none — |
| OpenTrek-Ops | User Guide | 39 | 20260630 | — none — |
| Operation Orchestration Service | Developer Guide | 64 | 20250925 | Resource Orchestration Service (0.772) |
| Operation Orchestration Service | Operations and Maintenance | 14 | 20250925 | Resource Orchestration Service (0.772) |
| Operation Orchestration Service | Product Introduction | 9 | 20250728 | Resource Orchestration Service (0.772) |
| Operation Orchestration Service | User Guide | 56 | 20250627 | Resource Orchestration Service (0.772) |
| Realtime Compute for Apache Flink (Compute-Storage Sep … | Developer Guide | 370 | 20260701 | — none — |
| Realtime Compute for Apache Flink (Compute-Storage Sep … | Operations and Maintenance | 56 | 20260701 | — none — |
| Realtime Compute for Apache Flink (Compute-Storage Sep … | Product Introduction | 13 | 20260701 | — none — |
| Realtime Compute for Apache Flink (Compute-Storage Sep … | User Guide | 524 | 20260701 | — none — |
| Resource Orchestration Service | Operations and Maintenance | 7 | 20250619 | Resource Orchestration Service (1.0) |
| Resource Orchestration Service | Product Introduction | 7 | 20250729 | Resource Orchestration Service (1.0) |
| SchedulerX 2.0 | Developer Guide | 102 | 20260701 | — none — |
| SchedulerX 2.0 | Operations and Maintenance | 13 | 20260701 | — none — |
| SchedulerX 2.0 | Product Introduction | 10 | 20260701 | — none — |
| SchedulerX 2.0 | User Guide | 139 | 20260701 | — none — |
| Security Orchestration Automation and Response (SOAR) | Developer Guide | 46 | 20260701 | Resource Orchestration Service (0.514) |
| Security Orchestration Automation and Response (SOAR) | Operations and Maintenance | 10 | 20260701 | Resource Orchestration Service (0.514) |
| Security Orchestration Automation and Response (SOAR) | Product Introduction | 19 | 20260701 | Resource Orchestration Service (0.514) |
| Security Orchestration Automation and Response (SOAR) | User Guide | 49 | 20260701 | Resource Orchestration Service (0.514) |
| Server Guard Advanced Edition | Developer Guide | 225 | 20260701 | Server Load Balancer (0.545) |
| Server Guard Advanced Edition | Operations and Maintenance | 12 | 20260701 | Server Load Balancer (0.545) |
| Server Guard Advanced Edition | Product Introduction | 41 | 20260701 | Server Load Balancer (0.545) |
| Server Guard Advanced Edition | User Guide | 318 | 20260701 | Server Load Balancer (0.545) |
| Server Load Balancer | Operations and Maintenance | 41 | 20260629 | Server Load Balancer (1.0) |
| Server Load Balancer | Product Introduction | 21 | 20260629 | Server Load Balancer (1.0) |
| Static Data Masking and Watermarking | Operations and Maintenance | 22 | 20260701 | — none — |
| Static Data Masking and Watermarking | Product Introduction | 16 | 20260701 | — none — |
| Static Data Masking and Watermarking | User Guide | 151 | 20260701 | — none — |
| Tair（Redis OSS-compatible） | Developer Guide | 126 | 20260630 | — none — |
| Tair（Redis OSS-compatible） | Operations and Maintenance | 89 | 20260630 | — none — |
| Tair（Redis OSS-compatible） | Product Introduction | 17 | 20260630 | — none — |
| Tair（Redis OSS-compatible） | User Guide | 172 | 20260630 | — none — |
| Tenant-side Bastionhost | Product Introduction | 17 | 20260701 | — none — |
| Tenant-side Bastionhost | Operations and Maintenance | 33 | 20260701 | — none — |
| Tenant-side Bastionhost | User Guide | 149 | 20260701 | — none — |
| Tracing Analysis | Developer Guide | 20 | 20260313 | — none — |
| Tracing Analysis | Operations and Maintenance | 22 | 20260313 | — none — |
| Tracing Analysis | Product Introduction | 8 | 20260313 | — none — |
| Tracing Analysis | User Guide | 84 | 20260313 | — none — |
| TransitRouter | Developer Guide | 258 | 20250924 | Data Transmission Service (0.5) |
| TransitRouter | Operations and Maintenance | 12 | 20251120 | Data Transmission Service (0.5) |
| TransitRouter | Product Introduction | 9 | 20260326 | Data Transmission Service (0.5) |
| TransitRouter | User Guide | 60 | 20260629 | Data Transmission Service (0.5) |
| Virtual Private Cloud | Operations and Maintenance | 116 | 20260629 | Virtual Private Cloud (1.0) |
| Virtual Private Cloud | Product Introduction | 17 | 20260310 | Virtual Private Cloud (1.0) |
| VPN Gateway | Operations and Maintenance | 9 | 20260629 | VPN Gateway (1.0) |
| VPN Gateway | Product Introduction | 7 | 20250731 | VPN Gateway (1.0) |

## 6. V3.16.2 manuals not carried into the V3.18.6 set

21 manuals exist in the V3.16.2 English baseline with no same-name, same-type counterpart in V3.18.6. Their text was not superseded inside the new set by an object this note could pair — some product lines are presented under new names in the V3.18.6 catalogue (the closest-name column in §5 flags the candidates), the rest simply have no English edition in the new set. The baseline files remain in the local corpus, nothing was deleted.

| product (V3.16.2) | manual | pages | doc date |
|---|---|---|---|
| Alibaba Cloud DNS (Within Cloud) | User Guide | 49 | 20250612 |
| Apsara Stack Security | Developer Guide | 779 | 20220913 |
| Apsara Stack Security | User Guide | 321 | 20220916 |
| Apsara Uni-manager Management Console | Developer Guide | 607 | 20251106 |
| Apsara Uni-manager Management Console | User Guide | 167 | 20251106 |
| ApsaraDB for Redis | Developer Guide | 114 | 20220915 |
| ApsaraDB for Redis | User Guide | 132 | 20220913 |
| ApsaraDB RDS for SQL Server | User Guide | 56 | 20251105 |
| Elastic IP Address | Developer Guide | 116 | 20220830 |
| Elastic IP Address | User Guide | 20 | 20220816 |
| Log Service | Developer Guide | 207 | 20220915 |
| Log Service | User Guide | 605 | 20220915 |
| NAT Gateway | Developer Guide | 72 | 20220902 |
| NAT Gateway | User Guide | 28 | 20220707 |
| Object Storage Service | User Guide | 61 | 20240702 |
| Realtime Compute | Developer Guide | 406 | 20220915 |
| Realtime Compute | User Guide | 43 | 20220628 |
| Server Migration Center | Developer Guide | 53 | 20240305 |
| Server Migration Center | User Guide | 37 | 20240305 |
| Tablestore | Developer Guide | 189 | 20220905 |
| Tablestore | User Guide | 33 | 20220905 |

## 7. Method, and what it cannot tell you

1. Both sets were downloaded as official PDFs, converted to text-only Markdown with the same line classifier, and every page hash-verified; PDFs are not kept locally by design.
2. Manuals are paired by **exact** product name + document type after normalisation. No fuzzy pairing: at 0.90 similarity *ApsaraDB for RDS* would match *ApsaraDB for Redis*, which would manufacture `changes`. Unmatched names are listed in Sections 5/6 instead of being guessed.
3. Textual deltas are **sentence-level, not line-level**: PDF re-flow moves line breaks between editions, so lines are re-joined per section and split on punctuation before comparison. Three gates then run: (i) headings, tables, fenced code, log samples and regex fragments are dropped; (ii) template text recurring in ≥ 8% of the paired corpus (floor of 6 manuals — with only 32 pairs this filter is weaker than in the V3.18.6→2607 note) is dropped; (iii) only *informative* sentences are counted — those carrying a version/number/quota or a support/add/deprecate/change verb, with self-describing UI narration ("This topic describes…", "On the X page, click…") excluded. Gates (i)–(iii) leave 1,999 added / 1,533 removed informative sentences; re-typing cancellation then reduces that to 1,902 / 1,436 — the figures quoted in §1.
3b. Per-pair document dates range from a few months to almost four years apart (part of the baseline dates back to 2022), so deltas include re-branding and re-typing of long-lived text; the re-typing cancellation above removes same-sentence rewrites (token Jaccard ≥ 0.82) from both sides. The known brand rename (“Apsara Stack Enterprise” → “Apsara Stack”) was deliberately **not** suppressed — sentences that changed only by brand still appear as added/removed lines.
3c. Quoted lines are verbatim extracts from the converted Markdown. The PDF extraction occasionally duplicates a short token or reorders a cell; those are extraction artifacts of our converter, not typographical errors in the manual, and they do not affect the substance of the quoted sentence.
4. Section counting normalises numbered headings (`2.1.1.2.3. Limits_1578278510` → `limits`), so a re-number is not counted as add + drop. Renames are reported when the normalised titles are ≥ 0.85 similar.
5. What this cannot show: why a change was made; whether removed text reflects a dropped feature or an editorial decision; anything about the manuals with no baseline (§5 — listed with closest names, never summarised as new or unchanged); and limits rows where the two editions do not share the row key.
6. Full machine-readable evidence (all added/removed sentences per manual, with section attribution): `.scratch/rn3162_pairs.json` in the session workspace. Regenerate with `python3 工具/rn3162_pairs.py && python3 工具/build_note_3162.py`.

## 8. Where the files are

| path | contents |
|---|---|
| `markdown/10_EN_ApsaraStack_v3.18.6/` | the 287-manual English set this note describes |
| `markdown/10_EN_ApsaraStack_V3.16.2/` | the 53-manual 2024–2025 English baseline |
| `文档缓存索引.csv` | 901 rows; `id / versionStamp / pages / markdown / markdownSha256` |
| `markdown_全量_901册.zip` | whole corpus, one zip |

