# Apsara Stack — What changed in the English V3.18.6 2607 document set

**Delta of `V3.18.6_2607` vs `V3.18.6` on the international documentation portal, derived line-by-line from the converted English Markdown corpus.**

| | |
|---|---|
| Manuals in V3.18.6_2607 | 265 |
| Documented pages | 38,512 |
| Document dates | 2026-07-31 → 2026-09-11 |
| Products covered | 54 |
| Manuals paired to an earlier V3.18.6 edition | 162 (every pair has a strictly later document date; none regressed) |
| Manuals with no earlier edition (new here) | 103 |
| V3.18.6 manuals not re-published in this set | 125 |
| Sentences added in the new edition (informative only) | 1,160 |
| Sentences no longer present (informative only) | 833 |
| Informative sentences before cancelling re-typeset pairs | 1,256 added, 929 removed (after cancellation: the two rows above) |
| Limit/quota rows added or changed | 43 |
| Manuals carrying their own release-notes section | 13 |

**How to read this.** §2 ranks the largest changes. §3 quotes the release-notes sections that product teams wrote into the manuals themselves. §4 is the detail: for every manual with material evidence it shows what text appeared, what text disappeared, which sections were added, removed or renamed, and which limits changed — each line attributed to the section it sits in. §5 lists manuals that exist only in the new set, §6 the ones that were not refreshed. §7 states the method and its limits. Nothing here is inferred from product knowledge: every claim is a diff of two PDFs.

---

## 1. Scope: the portal now carries two parallel V3.18.6 sets

The download page exposes **V3.18.6** and **V3.18.6 2607** (value `V3.18.6_2607`) as two selectable entries. They are not two spellings of one set: the 2607 objects live at a different storage path (`国际版文档/3816 2607/pdf 3/<product>/`, the folder name is mangled upstream) and none of their identifiers collide with the older set. In practice `V3.18.6_2607` is a service-pack refresh that re-published 162 manuals with a later document date, added 103 manuals, and left 125 V3.18.6 manuals untouched — so for ~1/3 of the English corpus the *older* document is still the current one.

## 2. Biggest changes in this refresh

| product | manual | pages | doc date | net lines | sections ± | limits |
|---|---|---|---|---|---|---|
| MaxCompute | Developer Guide | 316 → 552 (+236) | 20260629 → 20260826 | +39 / -40 | +324 / -18 | 8 |
| ApsaraDB for MongoDB | Operations and Maintenance | 90 → 315 (+225) | 20260629 → 20260828 | +54 / -0 | +40 / -0 | 0 |
| ApsaraDB for POLARDB PolarDB for P | Operations and Maintenance | 117 → 341 (+224) | 20260630 → 20260831 | +82 / -0 | +83 / -0 | 0 |
| ApsaraDB for POLARDB PolarDB-X 2.0 | Operations and Maintenance | 87 → 312 (+225) | 20260629 → 20260828 | +54 / -0 | +40 / -0 | 0 |
| ApsaraDB for POLARDB PolarDB for M | Operations and Maintenance | 192 → 329 (+137) | 20260630 → 20260828 | +36 / -11 | +21 / -7 | 0 |
| ApsaraDB for RDS | Operations and Maintenance | 196 → 332 (+136) | 20260629 → 20260831 | +62 / -9 | +61 / -4 | 0 |
| Database Backup | Developer Guide | 12 → 114 (+102) | 20250529 → 20260828 | +0 / -1 | +41 / -21 | 0 |
| Data Transmission Service | Developer Guide | 480 → 572 (+92) | 20260313 → 20260901 | +2 / -4 | +1 / -2 | 0 |
| Message Queue for Apache Kafka | User Guide | 160 → 241 (+81) | 20260629 → 20260828 | +1 / -1 | +36 / -0 | 0 |
| Cloud Defined Storage | User Guide | 963 → 1032 (+69) | 20260629 → 20260908 | +160 / -61 | +7 / -85 | 8 |
| Cloud Defined Storage | Operations and Maintenance | 327 → 390 (+63) | 20260630 → 20260901 | +44 / -10 | +40 / -6 | 0 |
| CloudMonitor | Developer Guide | 552 → 616 (+64) | 20260629 → 20260902 | +9 / -1 | +14 / -87 | 0 |
| Container Service for Kubernetes | User Guide | 734 → 779 (+45) | 20260629 → 20260902 | +65 / -68 | +25 / -8 | 2 |
| CloudMonitor | User Guide | 405 → 435 (+30) | 20260629 → 20260901 | +16 / -12 | +27 / -16 | 0 |


**Three observations that fall out of the diff**

- The in-document service-pack label **v3.18.6sp-2607** appears in 12 new editions and 0 baseline editions of the same manuals — that is how the portal's `V3.18.6 2607` entry names itself inside the PDFs.
- Database O&M manuals account for the largest page growth, and most of it is one new chapter: 6 O&M manuals gained a **Console release notes** section (ApsaraDB for MongoDB, ApsaraDB for POLARDB Polar, ApsaraDB for RDS, Data Transmission Service …).
- Biggest page growth: MaxCompute Developer Guid 316→552 pp, ApsaraDB for MongoDB Operations and 90→315 pp, ApsaraDB for POLARDB Pol Operations and 87→312 pp, ApsaraDB for POLARDB Pol Operations and 117→341 pp, ApsaraDB for POLARDB Pol Operations and 192→329 pp.
- Largest restructure: **Elastic Compute Service** User Guide dropped 247 section titles while its page count moved +6 — the chapters were re-organised, not deleted with the content.

## 3. What the product teams wrote themselves

13 manuals in this set carry their own release-notes / what's-new section. Those are quoted verbatim below (truncated where long) — they are the only statements in this note written by the vendor rather than derived by diffing.

**console release notes** — same wording in 5 manuals: ApsaraDB for MongoDB (Operations and Maintenance Guide); ApsaraDB for POLARDB PolarDB for MySQL (Primary_Secondar; ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Sec; ApsaraDB for POLARDB PolarDB-X 2.0 (Operations and Maint; ApsaraDB for RDS (Operations and Maintenance Guide)

> This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases. **v3.18.6sp-2607**

**kernel release notes** — same wording in 1 manual: ApsaraDB for POLARDB PolarDB-X 2.0 (User Guide)

> This topic describes the kernel release notes for PolarDB HTAP. For a detailed list of updates, see the **cloud-native distributed database PolarDB-X** **2.0** section in the **Hotfix release notes**. **Release date: 2026-07-30** v3.18.6r-paas-drds-hotfeature-SP007 provides a kernel upgrade for PolarDB-X 2.0 Enterprise Edition (Distributed): v3.18.6r-paas-drds-hotfeature-SP007 provides a kernel upgrade for PolarDB-X 2.0 Standard Edition (Centralized):

**console release notes** — same wording in 1 manual: ApsaraDB for RDS ApsaraDB RDS for PolarDB (User Guide)

> This topic describes the new features and important updates for RDS PolarDB. **v3.18.6sp-2607** eSQL (Compatible with Oracle)?

**console release notes** — same wording in 1 manual: ApsaraDB for RDS ApsaraDB RDS for PostgreSQL (User Guide

> This topic describes new features and important updates for the RDS PostgreSQL console. **v3.18.6sp-2607**

**release notes for kubernetes 1.34** — same wording in 1 manual: Container Service for Kubernetes (User Guide)

> Container Service for Kubernetes (ACK) strictly complies with the Certified Kubernetes Conformance Program. This topic describes the updates in Kubernetes 1.34, including update notes, major changes, and feature updates. **Component versions** The following table describes the core component versions that are supported by ACK clusters that run Kubernetes 1.34. **Major changes** In Kubernetes 1.34, if you select Terway as the network plug-in and select DataPath V2 when you create an ACK cluster, the kube-proxy container no longer runs on nodes on which Terway is installed.

**release notes for kubernetes 1.32** — same wording in 1 manual: Container Service for Kubernetes (User Guide)

> Container Service for Kubernetes (ACK) is a certified Kubernetes offering. This topic describes the main changes in ACK for Kubernetes versions 1.32 and 1.31, including upgrade notes, major changes, new features, deprecated features and APIs, and feature gates. **Release notes for Kubernetes 1.32** **Component versions** The following table lists the core component versions for ACK clusters. **Feature changes** Starting from version 1.32, when you create an ACK cluster using the CreateCluster API operation, the default proxy mode for kube-proxy is IPVS instead of iptables.

**release notes for kubernetes 1.30** — same wording in 1 manual: Container Service for Kubernetes (User Guide)

> Container Service for Kubernetes (ACK) strictly abides by the terms of the Certified Kubernetes Conformance Program. This topic describes the updates in Kubernetes 1.30, including update notes, major changes, new features, deprecated features and APIs, and feature gates. **Component versions** The following key component versions are supported by ACK clusters that run Kubernetes 1.30. **Update notes** **Features** CVE-2024-10220 vulnerabilities are fixed in 1.30.7-aliyun.1. **Kubernetes 1.29** A sleep mode is added for the PreStop hook.

**console release notes** — same wording in 1 manual: Data Management (User Guide)

> This topic describes the new features and important updates for Data Management (DMS). **v3.18.6sp-2607** **v3.18.6sp-2605**

**console release notes** — same wording in 1 manual: Data Transmission Service (Operations and Maintenance Gu

> This topic describes the new features and important updates for the DTS console. **v3.18.6sp-2607**

**release notes** — same wording in 1 manual: Data Transmission Service (User Guide)

> This topic describes the new features and important updates of Data Transmission Service (DTS). **v3.18.6sp-2607** **v3.18.6sp-2605** nsole

**release notes** — same wording in 1 manual: IDaaS (Developer Guide)

> **Update date: October 23, 2025** Release description: The first time Identity as a Service (IDaaS) released on Apsara Stack. All API operations of IDaaS are available. 1. List of operations by function **1.1. Instances** **1.2. Applications** **1.3. Accounts** **1.4. Organizations** **1.5. Account groups** **1.6 Identity providers (IdPs)** **1.7. Password policies** **1.8. Synchronization** **1.9. Brands** **1.10 Network endpoints** **1.11 Network zones** **1.12.

## 4. Change detail per manual

*52 manuals with material evidence are expanded; 110 further manuals changed only cosmetically (re-flow, page numbering, boilerplate) and are tabled at the end of this section.*

### Alibaba Cloud Message Queue — Product Introduction

`27 pages / 20260629` → `27 pages / 20260828` (+0 pages, 9 → 9 sections, 37,823 → 37,454 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Message Queue Product Introduction 20260828.md`

**Limits and quotas that changed**
- new · *limits* · The length of a topic name | 64 characters | The topic name cannot exceed this length limit. Otherwise, you will be unable to send or subscribe.
- new · *limits* · The size of a message | A normal message or an ordered message: 4 MB A transactional message, a scheduled message, or a delayed message: 64 KB Note Message attributes are …
- new · *limits* · The rate of transactions per second (TPS) for sending and receiving messages on a single Message Queue for Apache RocketMQ instance | For a cluster that consists of two p …


### API Gateway — Developer Guide

`613 pages / 20260629` → `367 pages / 20260828` (-246 pages, 315 → 160 sections, 699,736 → 451,282 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway Developer Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `API call - Service management` — You must also specify Modify service nodes API description Modify the node configuration of a service individually.

**Text no longer present**
- `Common API call methods` — The system automatically identifies the gateway type (API Gateway or AI Gateway) based on the instance ID and executes the corresponding processing logic.
- `Common API call methods` — Some API Gateway and AI Gateway operations share the same path but behave differently.
- `API Gateway` — This document provides an overview of the OpenAPI interface system for API Gateway (SCG, Spring Cloud Gateway).

**Sections added** (1 total): `API call - Policy configuration`
**Sections dropped** (17 total): `API call - Policy configuration management`; `AI Gateway`; `API call - Plugin management`; `API call - Built-In Plug-In management`; `API Call - Model API Management`; `API call - MCP management` …

### API Gateway — User Guide

`196 pages / 20260629` → `196 pages / 20260828` (+0 pages, 82 → 82 sections, 304,331 → 305,106 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 API Gateway User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Route groups` — In the Associate Domain Name section, you can click Add to associate a domain name with the route group.
- `Signature management` — After you configure a signature plan for a route, the signature plan can be used for API request signature calculation.
- `Signature management` — After you disable API request signing for a route, the signatures of requests that match the route are no longer verified until you enable this feature for the route again.
- `Source routes` — To distinguish from regular routes, the API gateway_cascade:true header match rule is added for both the source route and cascade route.
- `Source consumers` — After you stop authorization, you can click Open Authorization in the Operation column of the source consumer to allow the source consumer to access the APIs again.
- `IP blacklist and whitelist policy` — Deny policies have a higher priority than allow policies.
- `Domain name management` — The domain name management module allows you to add different domain names and associate a route with domain names.


### Application Real-time Monitoring Service — Product Introduction

`14 pages / 20260629` → `14 pages / 20260828` (+0 pages, 8 → 8 sections, 10,396 → 10,486 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Product Introduction 20260828.md`

**Limits and quotas that changed**
- new · *limits* · Maximum nodes per application (by default, TLog outputs data from three physical machines) | 500
- new · *limits* · Trace retention period | 7 days. A longer retention period requires separate evaluation.
- new · *limits* · Metric retention period | 7 days. A longer retention period requires separate evaluation.
- new · *limits* · Supported JDK versions | 1.6 1.7 1.8
- new · *limits* · Maximum number of unique SQL patterns per user | 1,000


### Application Real-time Monitoring Service — User Guide

`153 pages / 20260629` → `153 pages / 20260828` (+0 pages, 99 → 96 sections, 258,466 → 260,898 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `FAQ about application` — By default, all agents that are downloaded after August 20, 2019 support the feature.
- `API calls` — The parameter details table provides the detailed information about the parameters of the selected API operation.
- `Arthas diagnostics` — You can add custom observations in the Add a custom observation item section.
- `Connect LLM applications to` — By default, uWSGI loads your application when the master process starts.
- `Create an alert rule` — To add more alert rules, click the plus sign on the right of the first alert rule.
- `ARMS SDKs` — If you cannot obtain the dependency from the pom.xml file, directly download armssdk-1.7.3.jar.

**Text no longer present**
- `API call snapshots` — The Interface Snapshot tab displays all the API operations that are called in the application within the specified time period.
- `API calls` — On the SQL Analysis and NoSql Analysis tabs, you can view the SQL and NoSQL requests that are initiated within the code of the selected API operation in the left-side pane.
- `API calls` — The Exception Analysis tab displays the Java exceptions that are thrown from the code of the selected API operation in the left-side pane.

**Sections dropped** (3 total): `Manually install the ARMS agent for a Java application`; `Install the ARMS agent for a Java application deployed in Do …`; `Java components and frameworks supported by ARMS`

### Apsara Stack DNS Apsara Stack DNS (Within Cloud) — User Guide

`66 pages / 20260310` → `68 pages / 20260828` (+2 pages, 55 → 55 sections, 95,280 → 102,921 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Stack DNS Apsara Stack DNS (Within Cloud) User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Add and manage DNS records` — In the Add DNS Record dialog box that appears, configure the parameters described in the following table and then click OK.
- `Add and manage forwarding domain` — On the Global Forwarding Domain Names tab, click Add Domain Name.
- `Add and manage forwarding domain` — In the Add Description dialog box, enter a description in the Description text box and click OK.
- `Enable default forwarding` — Configure global default forwarding rules based on the following information.
- `Add and manage tenant internal domain` — In the Add Tenant Internal Domain Name dialog box, configure the parameters described in the following table and click OK. Organization: Select an organization.
- `Associate a domain name with a VPC` — Simply configuring domain name resolution data does not take effect by default.
- `Disassociate a domain name from a VPC` — The VPC from which you disassociate the domain name is no longer displayed on the VPCs page.

**Text no longer present**
- `Add and manage forwarding domain` — In the Add Global Forwarding Domain Name dialog box, configure the domain name based on the following information, and then click OK.
- `Add and manage forwarding domain` — You can modify, add remarks to, and delete user-defined domain names.
- `Global default forwarding configuration` — You can enable or disable default forwarding in the Apsara Uni-manager Management Console.

**Sections added** (9 total): `Enable default forwarding`; `Enable global recursive resolution`; `Manage cached records`; `Associate a domain name with a VPC`; `Disassociate a domain name from a VPC`; `Associate a tenant default forwarding`; `Disassociate a tenant default forwarding`; `Perform health checks` …
**Sections dropped** (8 total): `Global default forwarding configuration`; `Global default recursive configuration`; `Cache management`; `Associate VPC`; `Dissociate a VPC`; `Detach a VPC` …

### Apsara Stack Resilience ASR for Geo-disaster — Developer Guide

`360 pages / 20260701` → `199 pages / 20260902` (-161 pages, 47 → 72 sections, 444,603 → 244,251 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Geo-disaster Developer Guide 20260902.md`

**Text new in this edition** (first lines by section)
- `Obtain AccessKey pair` — Otherwise, the API operation call may fail. Obtain a personal AccessKey pair** 1.
- `Obtain AccessKey pair` — We recommend that you use personal AccessKey pairs to call API operations.
- `Obtain an endpoint` — Find the icon in the Resource Application Result resource named asrdr-api and click the column.
- `ListDrGroups` — This API queries a paginated list of disaster recovery relationships under the current account and allows you to filter the results by name, status, primary and secondary regions, and other …
- `GetProtectGroup` — This API obtains the details of a protection group in the ASRDR service and returns extended data such as synchronization groups, status details, and failover tasks on demand.
- `CreateSyncGroup` — Make sure that you configure valid cloud instance regions and product instance information before you call this API.

**Sections added** (47 total): `Obtain an endpoint`; `Legacy API (deprecated)`; `API overview`; `Initialization operations`; `InitUser`; `CreateBackupCloud`; `CreateMainCloud`; `DescribeBackupCloud` …
**Sections dropped** (29 total): `Obtain the information and`; `Cloud instance management`; `ListSupportProducts`; `DescribeCloudInstance`; `DescribeCloudCredentials`; `SaveCloudCredentials` …

### Apsara Stack Resilience ASR for Geo-disaster — Operations and Maintenance Guide

`96 pages / 20260701` → `113 pages / 20260828` (+17 pages, 73 → 113 sections, 126,799 → 142,092 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Geo-disaster Operations and Maintenance Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `How do I add databases and tables to` — To filter out the database in the ASR-DR console whose version is earlier than V3.15.0, perform the following steps:
- `Replace the JAR package` — If an error occurs, you can replace the original JAR package with a new JAR package after the bugs are fixed in code.
- `Replace the JAR package` — In this case, you can delete the slf4j-log4j12 JAR package from the BOOT-INF/lib/ directory and compress data to generate a new JAR package.
- `How do I add databases and tables to` — Therefore, if you add databases and tables to ApsaraDB RDS instances, you must manually modify related data of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) and DTS.
- `How do I add databases and tables to` — Manually add a database to the secondary ApsaraDB RDS instance and create table schemas.
- `How do I add databases and tables to` — Manually add a database to the primary ApsaraDB RDS instance and create table schemas.
- `How do I add databases and tables to` — You must grant the synchronization account the read and write permissions on the new database in the primary and secondary ApsaraDB RDS instances.

**Text no longer present**
- `O&M architecture` — Product Configuration Upgrade, Cluster Deployment, Product Version, Product Baseline, DNS Resources, VIP Resources, Database Resources, Conditions of the Network Between Data Centers, and BG …
- `inspect_db_resource` — If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.
- `drei_product` — Contact Alibaba Cloud technical support to obtain the rebuild files and decompress them.

**Sections added** (98 total): `Purpose`; `Requirements`; `Usage notes`; `Component architecture`; `Server roles`; `Common O&M operations`; `Log in to the ASR-DR`; `ASR-DR O&M` …
**Sections dropped** (54 total): `Introduction`; `Roles`; `ASR O&M operations`; `Getting started`; `Log on to the ASR console`; `View platform monitoring metrics` …
**Sections renamed**: `O&M architecture` → `Architecture`; `View ASR logs` → `View ASR-DR logs`; `Appendixes` → `Appendix`

### Apsara Stack Resilience ASR for Geo-disaster — User Guide

`204 pages / 20260701` → `218 pages / 20260901` (+14 pages, 123 → 128 sections, 316,296 → 333,933 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Geo-disaster User Guide 20260901.md`

**Text new in this edition** (first lines by section)
- `View a protection entity` — You can view the RPO of only the protection groups whose instance type is OSS or CDS-OSS.
- `Change the group of a protected entity` — The new protection group must have the same production region organization, disaster recovery region organization, and synchronization direction as the current protection group.
- `Delete a protection group` — Delete protection groups that you no longer need.
- `Manage cloud product information` — O&M console of ASR for Geo-disa ster Recovery Related operations After you add a cloud, you can also perform the following operations.
- `Perform a site failover` — This operation does not support hybrid disaster recovery.

**Text no longer present**
- `Manage protection groups` — You can also add instances to the protection group, view the details of the protection group, and enable reprotection for the protection group.
- `Private domain name resolution (DNS)` — Click Add Entity in the Actions column of the target protection group.

**Sections added** (8 total): `View the health status of a protection`; `Configure disaster recovery for PolarDB-`; `Delete a protection group`; `Data verification`; `Manage verification tasks`; `Manage validation clusters`; `Manage scoring items for`; `Manage fault injection tasks`
**Sections dropped** (4 total): `Protection Groups`; `Manage protection group topologies`; `Manage a plan`; `1. Log on to the ASR for Geo-disaster Recovery console`
**Sections renamed**: `Manage topology applications` → `Manage topology application bindings`; `Manage business disaster recovery plans` → `Manage business disaster recovery`; `Execute a business disaster recovery` → `Execute a business disaster recovery dri …`; `Create a disaster recovery unit` → `Create a disaster recovery unit namespac …`

### Apsara Stack Resilience ASR for Zone-disaster Recovery — User Guide

`122 pages / 20260701` → `126 pages / 20260901` (+4 pages, 96 → 100 sections, 152,246 → 159,032 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Zone-disaster Recovery User Guide 20260901.md`

**Text new in this edition** (first lines by section)
- `Arbitration configuration` — For example, tenant Domain Name System (DNS) in the 3AZ scenario does not support arbitration.
- `Create a protection group` — You can add databases, middleware, and Elastic Compute Service (ECS) instances that run application services for the same business to a single protection group (as an HDR protection group) t …
- `Create a protection group` — Select the Product type from the drop-down list, select the corresponding Instance ID/Name to add to the protection group, verify that you have added all required products and instances, and …
- `License authorization` — Contact your account manager to renew your license. Feature restrictions after license expiration** When a trial license expires or the authorization quota is insufficient, the ASR platform …
- `License authorization` — An insufficient Advanced Edition license quota does not restrict access to Advanced Edition features.
- `Arbitration configuration` — Middleware, OTSInner, DNSProduct, Tongque, MemberK8s, ARMS, Prometheus, and PolarDB-X 2.0 5.
- `Create a protection group` — ApsaraDB RDS, ApsaraDB for Redis, ApsaraDB for MongoDB, PolarDB-X 1.0, PolarDB-X 2.0, Object Storage Service (OSS), Elastic Compute Service (ECS), Realtime Compute for Apache Flink with deco …

**Text no longer present**
- `Create a protection group` — In a protection group, you can add various instances that belong to the same business application, such as databases, middleware, and Elastic Compute Service (ECS) instances, and treat them …
- `Create a protection group` — In the Protected Instance step, configure the Product and Instance ID/Name parameters to select the instances that you want to add to the protection group, confirm that the required instance …
- `Create a protection group` — ApsaraDB RDS, Tair (Redis OSS-compatible), ApsaraDB for MongoDB, PolarDB-X 1.0, PolarDB-X 2.0, Object Storage Service (OSS), ECS, Realtime Compute for Apache Flink, and Elasticsearch.

**Sections added** (5 total): `Product O&M`; `Database O&M`; `Zone alignment`; `Arbitration configuration`; `License authorization`
**Sections dropped** (1 total): `Configure arbitration`

### Apsara Uni-manager — User Guide

`1380 pages / 20260701` → `1398 pages / 20260902` (+18 pages, 755 → 770 sections, 1,676,146 → 1,692,486 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Uni-manager User Guide 20260902.md`

**Text new in this edition** (first lines by section)
- `Preset roles and their permissions` — The permission list describes the permissions of the roles to perform management operations in the Apsara Uni-manager Management Console and the permissions to call API operations.
- `Portal homepage` — In the Quick Entry section, you can add shortcuts based on your business requirements.
- `Create a user` — The default policy does not restrict the login time or login IP address.
- `Create a user` — When you bind a resource set, the system navigates to the user details page and opens the Add to Resource Set dialog box.
- `RAM policies` — However, to ensure consistency, we recommend that you follow the standard capitalization of the product code and API operation names.
- `Manage custom roles` — For example, if you set oss:ListBuckets,ecs:Describe*,rds:Describe* in Allow, the role has the permission to list all Object Storage Service (OSS) buckets, call all ECS APIs starting with De …
- `Manage custom roles` — Click Add Permissions below the list, and then click OK.
  *… 77 further added lines in this manual*

**Text no longer present**
- `Configure a quota template` — An operations administrator can configure quota templates in the root organization and all level-1 organizations.
- `Preset roles and their permissions` — Management permissions include both console operation permissions on the Apsara Uni- Manager Management Console and API-level permissions for programmatic access.
- `Home` — This card displays the usage of each quota item of cloud services.
  *… 39 further removed lines*

**Sections added** (50 total): `Familiarize yourself with the`; `Portal homepage`; `View the system user list and details`; `AccessKey log`; `Service resources`; `Create or modify a logical inventory`; `AI service tokens`; `Set quotas` …
**Sections dropped** (19 total): `Get familiar with the interface`; `Home`; `View system users`; `View and export AccessKey pair logs`; `Configure logical inventories`; `Modify application form configuration` …
**Sections renamed**: `Configure inventory change` → `Configure physical inventory change`; `View application` → `View application forms`; `Approval application form` → `Approve an application form`; `Cloud services supported by multi-cloud` → `Cloud services supported by multi-`

### ApsaraDB for MongoDB — Operations and Maintenance Guide

`90 pages / 20260629` → `315 pages / 20260828` (+225 pages, 81 → 133 sections, 164,765 → 563,047 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for MongoDB Operations and Maintenance Guide 20260828.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases. **v3.18.6sp-2607**

**Text new in this edition** (first lines by section)
- `Overview of the instance details page` — The system records 10 types of logs that cover all operations and changes to your instance, including general logs, high availability (HA) logs, API logs, and management logs.
- `Modify the storage capacity` — If you want to shrink the storage capacity, make sure that the new storage capacity is not smaller than the current storage usage of the instance plus 20 GiB.
- `Console release notes` — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases.
- `Overview of the ApsaraDB` — Check the Overview of abnormal data module for new instance exceptions.
- `Overview of the instance details page` — Why are multi-line SQL statements not supported?** Only single-line SQL statements are supported, and SQL statements cannot contain line breaks.
- `Overview of the instance details page` — Verify that the data volume of logs under the filter conditions does not exceed the limit.
- `View instance information` — These child instances are grouped and displayed by instance type.
  *… 14 further added lines in this manual*

**Sections added** (40 total): `Console release notes`; `Overview of the ApsaraDB`; `Instance management`; `Overview of the instance details page`; `View instance information`; `Instance O&M operations`; `Scheduled migration management`; `Batch operation management` …

### ApsaraDB for POLARDB PolarDB for MySQL (Primary_Secondary Edition) — Operations and Maintenance Guide

`192 pages / 20260630` → `329 pages / 20260828` (+137 pages, 132 → 146 sections, 362,040 → 586,281 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB for MySQL (Primary_Secondary Edition) Operations and Maintenance Guide 20260828.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases. **v3.18.6sp-2607**

**Text new in this edition** (first lines by section)
- `Console release notes` — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases.
- `Overview of the ApsaraDB` — Check the Overview of abnormal data module for new instance exceptions.
- `Overview of the instance details page` — Why are multi-line SQL statements not supported?** Only single-line SQL statements are supported, and SQL statements cannot contain line breaks.
- `Scheduled migration management` — Select candidate instances, configure parameters such as the destination location, migration window, and VIP switching mode for each instance, and apply default configurations to all instanc …
- `Scheduled migration management` — Delete migration plans that you no longer need.
- `Scheduled migration management` — After you add candidate instances to the list of selected instances, configure migration parameters for each instance.
- `Scheduled migration management` — Return to the migration plan list and confirm that the new plan appears in the list with the status Wait or Running.

**Text no longer present**
- `Overview of the homepage of` — Check whether new instance exceptions are identified in the Overview of abnormal data section.
- `Overview of the instance details page` — The Physical Topology tab is displayed only for MySQL instances that do not use the new architecture.
- `Intelligent host diagnostics` — By default, the system allows you to view only the data collected within the previous seven days (based on the collection time in file metadata).

**Sections added** (21 total): `Console release notes`; `Overview of the ApsaraDB`; `Scheduled migration management`; `Batch operation management`; `Instance dashboard`; `Cluster instance list`; `Cluster instance list overview`; `Basic information of cluster instances` …
**Sections dropped** (7 total): `Overview of the homepage of`; `Intelligent O&M`; `Intelligent host diagnostics`; `Information collection`; `Automated script management`; `Host software package management` …

### ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) — Operations and Maintenance Guide

`117 pages / 20260630` → `341 pages / 20260831` (+224 pages, 110 → 210 sections, 211,032 → 609,127 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) Operations and Maintenance Guide 20260831.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases. **v3.18.6sp-2607**

**Text new in this edition** (first lines by section)
- `Overview of the instance details page` — The system records 10 types of logs that cover all operations and changes to your instance, including general logs, high availability (HA) logs, API logs, and management logs.
- `Modify the storage capacity` — If you want to shrink the storage capacity, make sure that the new storage capacity is not smaller than the current storage usage of the instance plus 20 GiB.
- `Automated script management` — The details page displays the current version number of the script, such as V1.0.4.
- `Console release notes` — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases.
- `Overview of the ApsaraDB` — Check the Overview of abnormal data module for new instance exceptions.
- `Overview of the instance details page` — Why are multi-line SQL statements not supported?** Only single-line SQL statements are supported, and SQL statements cannot contain line breaks.
- `Overview of the instance details page` — Verify that the data volume of logs under the filter conditions does not exceed the limit.
  *… 42 further added lines in this manual*

**Sections added** (83 total): `Console release notes`; `Overview of the ApsaraDB`; `Instance management`; `Overview of the instance details page`; `View instance information`; `Instance O&M operations`; `Scheduled migration management`; `Batch operation management` …

### ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) — User Guide

`371 pages / 20260630` → `373 pages / 20260831` (+2 pages, 126 → 127 sections, 751,576 → 754,203 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) User Guide 20260831.md`

**Text new in this edition** (first lines by section)
- `hypopg (hypothetical` — The result shows that version 1.3.1 of the hypopg extension is installed.
- `pg_search (BM25 index)` — For queries with non-text filtering conditions, such as rating>1 , add the corresponding columns to the BM25 index to enable predicate pushdown and significantly improve query performance.
- `Upgrade a minor engine` — If this button does not appear, the kernel is already the latest version.
- `Modify the values of` — If the new parameter settings take effect only after you restart the instance, the system prompts you to restart the instance.
- `Change the network type of` — If you retain the classic network endpoint, add the VPC endpoint to the ECS instances before the classic network endpoint expires.
- `Create an alert rule` — The minimum alert detection frequency is once per minute.
- `imgsmlr (similar images)` — The extension also provides a function to create a Operators Both the pattern and signature types support the <-> operator for Euclidean distance.

**Text no longer present**
- `Migrate data from a PolarDB for` — ApsaraDB for POLARDB You need to pay attention to the following changes when you upgrade the engine version from PostgreSQL 14 to PostgreSQL 16.
- `Primary/secondary switchover` — The secondary instance serves only as a backup and does not allow external access.
- `Manage tags` — ApsaraDB for POLARDB If you have a large number of instances, you can create multiple tags and add the tags to the instances.

**Sections added** (1 total): `Launch templates`
**Sections renamed**: `Primary/secondary switchover` → `Primary/standby switchover`

### ApsaraDB for POLARDB PolarDB-X 2.0 — Operations and Maintenance Guide

`87 pages / 20260629` → `312 pages / 20260828` (+225 pages, 71 → 123 sections, 160,163 → 558,588 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB-X 2.0 Operations and Maintenance Guide 20260828.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases. **v3.18.6sp-2607**

**Text new in this edition** (first lines by section)
- `Overview of the instance details page` — The system records 10 types of logs that cover all operations and changes to your instance, including general logs, high availability (HA) logs, API logs, and management logs.
- `Modify the storage capacity` — If you want to shrink the storage capacity, make sure that the new storage capacity is not smaller than the current storage usage of the instance plus 20 GiB.
- `Console release notes` — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases.
- `Overview of the ApsaraDB` — Check the Overview of abnormal data module for new instance exceptions.
- `Overview of the instance details page` — Why are multi-line SQL statements not supported?** Only single-line SQL statements are supported, and SQL statements cannot contain line breaks.
- `Overview of the instance details page` — Verify that the data volume of logs under the filter conditions does not exceed the limit.
- `View instance information` — These child instances are grouped and displayed by instance type.
  *… 14 further added lines in this manual*

**Sections added** (40 total): `Console release notes`; `Overview of the ApsaraDB`; `Instance management`; `Overview of the instance details page`; `View instance information`; `Instance O&M operations`; `Scheduled migration management`; `Batch operation management` …

### ApsaraDB for POLARDB PolarDB-X 2.0 — User Guide

`198 pages / 20260629` → `201 pages / 20260828` (+3 pages, 83 → 87 sections, 313,289 → 315,788 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB-X 2.0 User Guide 20260828.md`

**Release notes written in the manual itself**
- *Kernel release notes* — This topic describes the kernel release notes for PolarDB HTAP. For a detailed list of updates, see the **cloud-native distributed database PolarDB-X** **2.0** section in the **Hotfix release notes**. **Release date: 2026-07-30** v3.18.6r-paas-drds-hotfeature-SP007 provides a kernel upgrade for PolarDB-X 2.0 Enterprise Edition (Distributed): v3.18.6r-paas-drds-hotfeature-SP007 provides a kernel upgrade for PolarDB-X 2.0 Standard Edition (Centralized):

**Text new in this edition** (first lines by section)
- `Create an instance` — Click to switch the instance list view between Default and Compact modes.
- `Create an instance` — In the upper-left corner, click Create New Instance.
- `Upgrade the kernel version` — You can manually upgrade the kernel version of your PolarDB for HTAP instances.
- `Upgrade the kernel version` — Although the console automatically checks for new versions when you log on, it does not apply upgrades automatically.
- `Upgrade the kernel version` — After you upgrade the kernel version, you cannot downgrade it.
- `Upgrade the kernel version` — In the Configuration Information section, click Upgrade Kernel Version.
- `Upgrade the kernel version` — In the dialog box that appears, select a Target Version (optional), set the Upgrade Time, Canary Batches, and Canary Interval (Hours), and then click OK.

**Text no longer present**
- `Primary instance` — The specifications include basic information such as the code of the instance type, the number of CPU cores, and memory capacity.
- `Overview` — ApsaraDB for POLARDB Note In the default mode, the DBA account is the privileged account.
- `Slow query logs` — ApsaraDB for POLARDB Note Instances of Enterprise Edition (Distributed) allow you to view the details of slow query logs by compute node (CN) and data node (DN).

**Sections added** (6 total): `Kernel release notes`; `Release an instance and`; `Upgrade the kernel version`; `PolarDB AI`; `Intelligent Assistant`; `Appendix`
**Sections dropped** (2 total): `Release a PolarDB-X instance`; `AI capabilities`
**Sections renamed**: `Enable and disable the three-role mode` → `Enable and disable the three-role`; `Manage the accounts for the three-role` → `Manage the accounts for the three-`; `Deadlock analysis` → `Lock analysis`

### ApsaraDB for RDS — Operations and Maintenance Guide

`196 pages / 20260629` → `332 pages / 20260831` (+136 pages, 126 → 188 sections, 363,307 → 587,135 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS Operations and Maintenance Guide 20260831.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases. **v3.18.6sp-2607**

**Text new in this edition** (first lines by section)
- `Automated script management` — The details page displays the current version number of the script, such as V1.0.4.
- `Console release notes` — This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases.
- `Overview of the ApsaraDB` — Check the Overview of abnormal data module for new instance exceptions.
- `Overview of the instance details page` — Why are multi-line SQL statements not supported?** Only single-line SQL statements are supported, and SQL statements cannot contain line breaks.
- `Scheduled migration management` — Select candidate instances, configure parameters such as the destination location, migration window, and VIP switching mode for each instance, and apply default configurations to all instanc …
- `Scheduled migration management` — Delete migration plans that you no longer need.
- `Scheduled migration management` — After you add candidate instances to the list of selected instances, configure migration parameters for each instance.
  *… 22 further added lines in this manual*

**Text no longer present**
- `Overview of the homepage of` — Check whether new instance exceptions are identified in the Overview of abnormal data section.
- `Overview of the instance details page` — The Physical Topology tab is displayed only for MySQL instances that do not use the new architecture.
- `Automated script management` — We recommend that you submit a ticket to Apsara Stack technical support for risk assessment and assistance.

**Sections added** (61 total): `Console release notes`; `Overview of the ApsaraDB`; `Scheduled migration management`; `Batch operation management`; `Instance dashboard`; `Cluster instance list`; `Cluster instance list overview`; `Basic information of cluster instances` …
**Sections dropped** (4 total): `Overview of the homepage of`; `Information collection`; `Host software package management`; `Software package`

### ApsaraDB for RDS ApsaraDB RDS for MySQL — User Guide

`181 pages / 20260629` → `168 pages / 20260831` (-13 pages, 89 → 90 sections, 301,736 → 291,103 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260831.md`

**Deprecations / removals stated in the text**
- (Create a read-only instance) Account creation, deletion, authorization, and password changes are not supported.
- (Delete a database) You can delete databases that are no longer used in the ApsaraDB RDS console.
- (Configure transaction splitting) ApsaraDB for RDS ApsaraDB RDS for MySQL User G Note When you no longer need transaction splitting, you can click Disable to the right of Transaction Splitting.
- (SQL Audit) If you no longer require the SQL audit feature, you can disable the feature to reduce costs.

**Text new in this edition** (first lines by section)
- `Configure an IP address whitelist for an` — After you add any new IP address to the default group, the system automatically removes the default deny rule 127.0.0.1 .
- `Log on to the ApsaraDB` — For security purposes, your password must meet the minimum complexity requirements.
- `Create a read-only instance` — Account creation, deletion, authorization, and password changes are not supported.
- `Reset the password of a` — In the dialog box that appears, enter and confirm the new password, and then click OK.
- `Configure a dedicated proxy` — During high-traffic events like sales promotions, you can dynamically add or remove read-only instances without changing your application's connection configuration.
- `Configure a dedicated proxy` — If you re-enable the service, the system assigns a new proxy endpoint.
- `Configure a connection pool` — The connection pooling feature does not support IP-specific permissions for an account.

**Text no longer present**
- `Update the minor engine` — ApsaraDB RDS for MySQL User G ApsaraDB for RDS Manually update the minor version 1.
- `Product Material Optimization` — ApsaraDB for RDS ApsaraDB RDS for MySQL User G Smart Image Generation API -- detailed field schema for the 7 atomic capabilities.
- `Configure transaction splitting` — When transaction splitting is enabled and the default isolation level READ COMMITTED is used, the ApsaraDB RDS instance starts a transaction only for write requests when autocommit is disabl …

**Sections added** (13 total): `Console feature release`; `Reset the password of a`; `Smart Matting`; `Configure a connection pool`; `Set the consistency level`; `View monitoring data`; `Use the SQL audit feature`; `Database recovery` …
**Sections dropped** (12 total): `Package Audit`; `Delete a database`; `Change the endpoint and port number of an instance`; `Configure short-lived`; `Configure transaction splitting`; `View resources and engine` …
**Sections renamed**: `Log in to the ApsaraDB RDS` → `Log on to the ApsaraDB`; `Use the Upload Binlogs` → `Upload binlogs`

### ApsaraDB for RDS ApsaraDB RDS for PolarDB — User Guide

`159 pages / 20260629` → `164 pages / 20260827` (+5 pages, 67 → 71 sections, 251,381 → 259,324 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for PolarDB User Guide 20260827.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic describes the new features and important updates for RDS PolarDB. **v3.18.6sp-2607** eSQL (Compatible with Oracle)?

**Text new in this edition** (first lines by section)
- `Create an instance` — For details, see the Quota Management chapter of the Unified Cloud Management Platform User Guide.
- `RDS PolarDB JDBC` — Select the version based on the Java Development Kit (JDK) version that is used by your application.
- `RDS PolarDB JDBC` — For Configure the JDBC driver Before you use the JDBC driver in your Java application, add the path of the JDBC driver to CLASSPATH .

**Text no longer present**
- `Configure SSL encryption` — ApsaraDB RDS for PolarDB User ApsaraDB for RDS Note When the JKS file is used in Java, you must modify the default JDK security configurations in JDK 7 and JDK 8.
- `Configure an IP address` — Add an ECS security group for the PolarDB instance to ApsaraDB for RDS ApsaraDB RDS for PolarDB User allow ECS instances in the group to connect to the PolarDB instance.
- `RDS PolarDB JDBC` — Select the version based on the Java Configure the JDBC driver Before you use the JDBC driver in your Java application, add the path of the JDBC driver to CLASSPATH .

**Sections added** (7 total): `Console release notes`; `Change VSwitch`; `Diagnostics`; `Session management`; `Lock analysis`; `Space analysis`; `Slow SQL`
**Sections dropped** (3 total): `Session Manager`; `Storage analysis`; `Slow query logs`

### ApsaraDB for RDS ApsaraDB RDS for PostgreSQL — User Guide

`159 pages / 20260629` → `164 pages / 20260831` (+5 pages, 75 → 76 sections, 251,944 → 260,394 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20260831.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic describes new features and important updates for the RDS PostgreSQL console. **v3.18.6sp-2607**

**Deprecations / removals stated in the text**
- (Limits on ApsaraDB RDS for) DB RDS instances that run Postgr eSQL 9.4 and PostgreSQL 10 are no longer available for purchase i n Apsara Stack V3.18 4.[Announcement] ApsaraDB RDS instances that run PostgreSQL 9.4 and Po …
- (Limits on ApsaraDB RDS for) ApsaraDB RDS for PostgreSQL Us ApsaraDB for RDS 3.[Announcement] ApsaraDB RDS instances that run PostgreSQL 9.4 and PostgreSQL 10 are no longer available for purchase in Apsara Stack V3.18 A …

**Text new in this edition** (first lines by section)
- `Limits on ApsaraDB RDS for` — DB RDS instances that run Postgr eSQL 9.4 and PostgreSQL 10 are no longer available for purchase i n Apsara Stack V3.18 4.[Announcement] ApsaraDB RDS instances that run PostgreSQL 9.4 and Po …
- `Configure an IP address` — The IP address whitelist labeled default contains only the default IP address 0.0.0.0/0, which allows all entities to access your ApsaraDB RDS instance.
- `Change the VPC and vSwitch` — The ApsaraDB RDS for PostgreSQL 10.0 instances that use local SSDs do not support this feature.
- `Change the network type of` — If you retain the classic network endpoint, add the VPC endpoint to the ECS instances before the classic network endpoint expires.
- `Real-time monitoring` — Some database engines (MongoDB and Redis) do not support the report download feature.
- `View slow query logs` — The instances of some database types do not support the SQL optimization feature.
- `View slow query logs` — This highlight persists after you close the optimization window and automatically shifts to the new record when you optimize another slow SQL statement.

**Text no longer present**
- `Limits on ApsaraDB RDS for` — ApsaraDB RDS for PostgreSQL Us ApsaraDB for RDS 3.[Announcement] ApsaraDB RDS instances that run PostgreSQL 9.4 and PostgreSQL 10 are no longer available for purchase in Apsara Stack V3.18 A …
- `Connect to an ApsaraDB RDS` — ApsaraDB for RDS ApsaraDB RDS for PostgreSQL Us Important The postgres database is the default system database.
- `Connect to an ApsaraDB RDS` — ApsaraDB RDS for PostgreSQL Us ApsaraDB for RDS Important The postgres database is the default system database.

**Sections added** (7 total): `Console release notes`; `Accounts`; `Databases`; `Networks, VPCs, and`; `Monitoring`; `Diagnostics`; `View slow query logs`
**Sections dropped** (5 total): `Manage accounts`; `Database management`; `Monitoring and alerts`; `Restore data of an ApsaraDB RDS for PostgreSQL instance`; `Slow query logs`

### Auto Scaling — User Guide

`74 pages / 20260312` → `75 pages / 20260828` (+1 pages, 74 → 74 sections, 129,343 → 132,037 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Auto Scaling User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Rollback of failed instances in` — In this case, you can use other methods to add ECS instances and ensure that the scaling group meets your business requirements.
- `Rollback of failed instances in` — Automatically add ECS instances When you create ECS instances by calling API operations, Auto Scaling uses the Alibaba Cloud Resource Access Management (RAM) service.
- `Rollback of failed instances in` — For example, since the quota for ECS instances that can be attached to the SLB backend server group has been reached, the request to add five ECS instances results in only two being created, …
- `Rollback of failed instances in` — Manually add ECS instances When you manually add existing instances, Auto Scaling automatically removes the rolledback ECS instances from the scaling group but does not release these ECS ins …
- `Quick Start overview` — Create scaling groups A scaling group defines properties such as the maximum and minimum number of instances it can contain and the scale-in policy.
- `Expected number of instances` — Manually execute a scaling rule and add instances at the same time Scenario:** Expected number of instances:
- `View the instance list` — The weight that Auto Scaling sets when it adds the instance to the vServer group.

**Text no longer present**
- `Expected number of instances` — Manually execute a scaling rule and add instances at the same time Scenario:** The add1 scaling rule specifies to create one ECS instance.

**Sections added** (3 total): `Usage limits`; `View the instance list`; `View scaling activity details`
**Sections dropped** (3 total): `Limits`; `Query instances`; `View the details of a scaling`
**Sections renamed**: `Roll back ECS instances` → `Rollback of failed instances in`

### Cloud Defined Storage — Operations and Maintenance Guide

`327 pages / 20260630` → `390 pages / 20260901` (+63 pages, 253 → 293 sections, 648,185 → 767,385 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Operations and Maintenance Guide 20260901.md`

**Text new in this edition** (first lines by section)
- `Proactive disk replacement` — This feature is not supported for Table Store clusters, EBS1.0 clusters, or OSS1.0 clusters.
- `Before you begin` — To perform such operations, contact Alibaba Cloud technical support first.
- `Configure a cluster sales policy` — If the oversubscription ratio is too high and concurrent writes cause the used capacity to approach the physical storage limit, the system triggers storage capacity throttling.
- `Configure a cluster sales policy` — In the Sales Configuration section, enter a new value for Oversold Ratio.
- `Configure a cluster sales policy` — The cluster will then automatically schedule new cloud disks.
- `Intelligent O&M configuration` — If the default O&M robot configuration does not meet your business needs, you can update it.
- `Manage user information` — In the Update User dialog box, change the value for Instance Quota.
  *… 4 further added lines in this manual*

**Text no longer present**
- `Maintain corrupted disks` — Tablestore clusters, Cloud Parallel File Storage (CPFS) clusters, Elastic Block Storage (EBS)-1.0 clusters, and Object Storage Service (OSS)-1.0 clusters do not support the disk maintenance …
- `Before you begin` — CDS Ops does not support managing Pangu clusters in managed OSS clusters.
- `Before you begin` — Contact Alibaba Cloud technical support to perform them.

**Sections added** (40 total): `Manage cloud disks`; `Intelligent O&M configuration`; `Manage Tablestore clusters`; `Tablestore cluster overview`; `OTS Chiji platform`; `Log in to the OTS Chiji console`; `User data`; `Manage user information` …
**Sections dropped** (6 total): `Manage disks`; `Create hot migration jobs to migrate`; `Configurations`; `Initiate a CDS Cluster Scale Up`; `Maintain corrupted disks`; `Actively replace a hard disk`

### Cloud Defined Storage — User Guide

`963 pages / 20260629` → `1032 pages / 20260908` (+69 pages, 165 → 51 sections, 3,145,729 → 3,451,015 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage User Guide 20260908.md`

**Deprecations / removals stated in the text**
- (Buckets) Delete a bucket** In the Object Storage Service (OSS) console, you can delete buckets that you no longer need.
- (Buckets) Back-to-origin is not supported for objects with original image protection enabled.
- (Buckets) Delete a single previous version Find the version that you no longer use and click Delete in the Operation column.

**Limits and quotas that changed**
- new · *limitations* · Number of instances per Alibaba Cloud account | 1,024 | To increase this limit, contact Alibaba Cloud technical support.
- new · *limitations* · Number of tables per instance | 1,024 | To increase this limit, contact Alibaba Cloud technical support.
- new · *limitations* · Instance name length | 3 to 16 bytes | The name must consist of lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and hyphens (-). It must start with a lett …
- new · *limitations* · Table name length | 1 to 255 bytes | The name must consist of lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and underscores (). It must start with a let …
- new · *limitations* · Column name length | 1 to 255 bytes | The name must consist of lowercase letters (a-z), uppercase letters (A-Z), digits (0-9), and underscores (). It must start with a le …
- new · *limitations* · Number of columns in a primary key | 1 to 4 | N/A

**Text new in this edition** (first lines by section)
- `What is Object Storage Service (OSS)` — After you enable TLS version settings, you can select either TLS 1.2 or 1.3.
- `What is Object Storage Service (OSS)` — Downgrading the TLS version (for example, from TLS 1.3 to TLS 1.2) or disabling TLS version settings may introduce security risks.
- `Disks` — Enable the multi-attach feature for disks that support NVMe 3.4.5.1.
- `Disks` — You can then attach the disk to up to 16 ECS instances that support the NVMe protocol within the same zone, allowing multiple ECS instances to concurrently read and write data on the same hi …
- `Data collection` — Linux Windows Effective time By default, after you add, delete, or modify the user_defined_id file, the new configuration takes effect within 1 minute.
- `Data collection` — If you set the startup parameter based on the Collection Rate Greater Than 40 MB/s column in the table, the collection performance approaches the limit.
- `Data transformation` — Several additional directives not defined in the C (1989 version) standard are included for convenience.
  *… 120 further added lines in this manual*

**Text no longer present**
- `2.1.1.2.2. ACL` — ItemLimitNotesObject key lengthMaximum 1,023 bytesThis includes the full path with all directory prefixesObjects per bucketUnlimitedNo hard limit on the number of objectsDirectory depthNo ha …
- `2.1.1.3.8. TLS` — Cloud Defined Storage If you disable TLS version management, TLS 1.2 and TLS 1.3 are supported by default.
- `2.1.1.3.8. TLS` — Downgrading the TLS version, such as changing the TLS version from TLS 1.3 to TLS 1.2, or disabling TLS version management may cause security and compliance issues.
  *… 36 further removed lines*

**Sections added** (7 total): `Block storage`; `Tablestore`; `Terms`; `Limitations`; `Secondary index`; `Search Index`; `Data monitoring`
**Sections dropped** (85 total): `2.1.1.1.2. ACL`; `2.1.1.3.5. Access permissions and account authorization`; `2.1.1.3.8. TLS`; `2.1.1.4.1. IMG`; `2.10.5.7.1. Permissions required by a gateway to operate OSS …`; `3.4.5. Enable the multi-attach feature for disks that suppor …` …

### CloudMonitor — Developer Guide

`552 pages / 20260629` → `616 pages / 20260902` (+64 pages, 197 → 123 sections, 678,646 → 746,968 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 CloudMonitor Developer Guide 20260902.md`

**Text new in this edition** (first lines by section)
- `CreateDashboardFolder` — The default API rate limit is 10,000 requests per second, and the default user rate limit is 50 requests per second.
- `DescribeCloudProductResourceTypes` — Queries the list of resource types that cloud products support.
- `DescribeConsoleViews` — This API is intended only for querying CMS console view configurations.
- `DescribeConsoleViews` — Its behavior and parameters are subject to change at any time without backward compatibility guarantees.This API queries the view configuration information of the CMS console.
- `DescribeConsoleViews` — External users and third-party applications must not call this API.
- `DescribeConsoleViews` — The API behavior and parameters may change at any time, and backward compatibility is not guaranteed.
- `PutResourceMetricRule` — After you modify a rule, the new configuration takes effect in the next monitoring period.

**Text no longer present**
- `DescribeSiteMonitorQuota` — CloudMonitor Queries the quotas and version of site monitoring.

**Sections added** (14 total): `DescribeMetricTopList`; `DescribeCloudProductResourceTypes`; `Console view configuration`; `DescribeConsoleViews`; `BatchDeleteCustomMetricMeta`; `CreateCustomMetricMeta`; `DescribeMetricPromQLRange`; `DescribeDynamicThresholdBound` …
**Sections dropped** (87 total): `DeleteAlertFilterConfigBatch`; `ModifyAlertFilterConfig`; `DescribeAlertFilterConfig`; `DeleteNotificationRules`; `ModifyNotificationRule`; `CreateAlertFilterConfig` …

### CloudMonitor — User Guide

`405 pages / 20260629` → `435 pages / 20260901` (+30 pages, 138 → 149 sections, 558,330 → 608,008 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 CloudMonitor User Guide 20260901.md`

**Text new in this edition** (first lines by section)
- `Kubernetes container` — Support Prometheus Monitoring 2.0, offering detailed monitoring for core components, nodes, applications, networks, GPUs, and Big Data/AI.
- `Kubernetes container` — The list includes columns such as Instance ID/Name, Organization/Resource Group, Region, Instance Status, Prometheus Monitoring 2.0, CPU Utilization, Memory Utilization, Cluster ID, Cluster …
- `Custom dashboards` — API Gateway Alibaba Cloud DNS Message Queue Elasticsearch on K8s OSS SLB ECS ApsaraDB for Redis (Cluster Edition) ApsaraDB for Redis (Standard Edition/Read/Write Splitting Edition) ApsaraDB …
- `Availability probe` — Use candidate ECS instances with an Agent version no lower than 4.0.0.1 for DNS probing.
- `Monitoring assistant` — On the Memory tab, click New, set the title and content, and enter the information that you want the system to remember.
- `UModel exploration` — You can switch between the two views, and the system displays the graph view by default.
- `Entity topology exploration` — Display Configure whether to display entity tags, group tags, and thumbnails, and whether to allow dragging entities.

**Text no longer present**
- `Kubernetes container monitoring` — For instances that support Prometheus monitoring 2.0, click the instance name to go to the Kubernetes container monitoring page.
- `Kubernetes container` — Support Prometheus monitoring 2.0, providing detailed monitoring for core components, nodes, applications, networks, GPUs, and big data/AI workloads.
- `Kubernetes container` — The Kubernetes container monitoring page displays a list of Kubernetes clusters with columns for Instance ID/Name, Organization/Resource Set, Region, Instance Status, Prometheus monitoring 2 …

**Sections added** (27 total): `Monitoring assistant`; `Intelligent exploratory`; `UModel exploration`; `Entity topology exploration`; `ECS`; `BMCP (Node)`; `BMCP (Bare metal-intelligent computing`; `Bare Metal Management Service (BMS)` …
**Sections dropped** (16 total): `Elastic Compute Service`; `BMCP (Container-based AI Compute`; `BMCP (Bare metal compute platform)`; `Bare Metal Service (BMS)`; `PolarDB High-availability Edition`; `PolarDB for MySQL HTAP Edition` …
**Sections renamed**: `CloudMonitor metrics` → `Cloud Monitor metrics`; `ApsaraDB for RDS: New connection` → `ApsaraDB RDS: New connectivity`; `AnalyticDB for PostgreSQL (new` → `AnalyticDB for PostgreSQL (New Link)`; `Cloud-native multi-model database` → `Cloud-native Multimode Database`

### Container Registry — User Guide

`110 pages / 20260629` → `118 pages / 20260902` (+8 pages, 82 → 85 sections, 208,728 → 236,245 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Container Registry User Guide 20260902.md`

**Text new in this edition** (first lines by section)
- `Configure quotas` — After you select a zone on the Resource Pool Configuration page, the Synchronously Modify Quotas in Other Zones option appears in the Configure Quota dialog box.
- `Create a namespace` — In the Quota Overview area on the right, you can view the current configuration.
- `Create a namespace` — You can set the default repository type to public, so that automatically created repositories are public by default.
- `Modify image accessibility` — If the Automatically Create Repository feature is disabled, you must enable the Automatically Create Repository feature before you can set the Default Repository Type parameter.
- `Add a chart whitelist` — Turn on the Chart ACL access control switch, and then click Add chart whitelist.
- `Add a chart whitelist` — In the Add chart whitelist dialog box, set entry and description, and then click OK.
- `Create a namespace` — In the Quota Overview section on the right, you can view the current configuration.

**Text no longer present**
- `Replicate images between` — In the Select Destination Repository for Replication dialog box, select Same Account for the Synchronization Scenario parameter, specify the region, destination instance name, namespace, ima …
- `Replicate images between` — In the Select Destination Repository for Replication dialog box, select a value for Image Tag to be Copied, specify the region, product type, destination instance name, namespace, image repo …
- `Replicate images between` — In the Select Destination Repository for Replication dialog box, select Same Account for the Synchronization Scenario parameter, specify the region, product type, destination instance name, …

**Sections added** (6 total): `Create a synchronization source`; `Add a chart whitelist`; `Create a repository`; `Delete a repository`; `Synchronize instances in the`; `Synchronize instances within the`
**Sections dropped** (2 total): `Create a role and grant permissions to the`; `Replicate images between`

### Container Service for Kubernetes — Product Introduction

`23 pages / 20251202` → `24 pages / 20260828` (+1 pages, 9 → 9 sections, 30,535 → 30,004 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Product Introduction 20260828.md`

**Limits and quotas that changed**
- new · *limits* · Cluster | By default, you can create a maximum of 50 clusters across all regions. Each cluster can contain a maximum of 100 nodes. To increase these quotas, submit a tick …
- new · *limits* · ECS instance | Cluster creation, scale-out, and auto-scaling operations are subject to the quota and inventory of underlying products, such as Elastic Compute Service (EC …

**Text no longer present**
- `Scenarios` — Ecosystem support Supports mainstream deep learning frameworks, such as TensorFlow, Caffe, MXNet, and Pytorch, and offers optimized features of these frameworks.

**Sections added** (1 total): `Functions and features`

### Container Service for Kubernetes — User Guide

`734 pages / 20260629` → `779 pages / 20260902` (+45 pages, 234 → 252 sections, 1,570,883 → 1,663,279 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes User Guide 20260902.md`

**Release notes written in the manual itself**
- *Release notes for Kubernetes 1.34* — Container Service for Kubernetes (ACK) strictly complies with the Certified Kubernetes Conformance Program. This topic describes the updates in Kubernetes 1.34, including update notes, major changes, and feature updates. **Component versions** The following table describes the core component versions that are supported by ACK clusters that run Kubernetes 1.34.
- *Release notes for Kubernetes 1.32* — Container Service for Kubernetes (ACK) is a certified Kubernetes offering. This topic describes the main changes in ACK for Kubernetes versions 1.32 and 1.31, including upgrade notes, major changes, new features, deprecated features and APIs, and feature gates. **Release notes for Kubernetes 1.32** **Component versions** The following table lists the core component versions for ACK clusters.

**Deprecations / removals stated in the text**
- (Kubernetes 1.28 release notes) You can no longer specify the --container-runtime-endpoint and --image-service-endpoint flags in kubelet commands.
- (Delete a cluster) You can delete clusters that you no longer need in the Container Service for Kubernetes (ACK) console.
- (Upgrade a node pool) If you no longer need these files, manually delete the Docker directory from the data disk after you switch the container runtime.
- (Update a node pool) If you no longer need the data in the Docker directory, you can manually delete the directory.

**Limits and quotas that changed**
- new · *limits* · Elastic Compute Service (ECS) instance | When you create clusters, expand clusters, or perform auto scaling for clusters, you may fail to create nodes due to ECS instance …
- new · *set bandwidth limits for pods* · k8s.aliyun.com/egress-bandwidth | :

**Text new in this edition** (first lines by section)
- `MLPS Security Hardening` — MLPS Security Hardening Important By default, ACK creates the ack_admin, ack_audit, and ack_security regular users in Alibaba Cloud Linux for which MLPS Security Hardening is enabled to ensu …
- `ack-koordinator` — K8s APIServer Koordinator Protocol Extensions Manager (CRD, extend-res) Koordlet Kubelet Node-level Resource QoS for Containers Data Fine- Reporting grained Scheduling LS LS BE BE Pod Pod Po …
- `Create an Ingress with the console` — In this example, the service weights for both the old and new versions are set to 50, which means each service receives 50% of the traffic.
- `Upgrade a node pool` — These snapshots are retained for 30 days by default, but you can delete them earlier.
- `Manage agent network access with TrafficPolicy` — Allow traffic on a specific TCP port** The following policy allows the agent to access the destination server only through TCP port 80.
- `Manage agent network access with TrafficPolicy` — Allow DNS traffic on port 53** DNS queries primarily use UDP, but some large responses fall back to TCP.
- `Release notes for Kubernetes 1.30` — Consequently, when the resources structure of the container API changes, for example, when the claims field is added, the resource structure of the PVC API also changes.
  *… 25 further added lines in this manual*

**Text no longer present**
- `Use the policy administration feature in the` — By default, the table on the page displays the 100 most recent alert logs for blocked operations or warnings from the last 7 days.
- `ack-koordinator` — K8s APIServer Protocol Extensions (CRD, extend-res) Koordlet Node-level Data Reporting Fine- LS Pod LS Pod BE Pod BE Pod Versioning In ack-koordinator v1.1.1-ack.1 and later, the version num …
- `Compatibility of NGINX Ingress annotations` — The APIG document claims "51 supported annotations", and its statistical caliber contains "partially compatible" annotations (such as server-alias, auth-tls-secret, etc.), and includes denyl …
  *… 43 further removed lines*

**Sections added** (25 total): `Delete a cluster`; `Maintain a cluster`; `Edit a node pool`; `Upgrade a node pool`; `Use dynamic NAS volumes`; `Container security: policy rule library`; `Policy management in the ACK console`; `Configure resource quotas and limits` …
**Sections dropped** (8 total): `Modify a node pool`; `Update a node pool`; `Mount a dynamically provisioned NAS volume`; `Predefined security policies of ACK`; `Use the policy administration feature in the`; `Set resource quotas and limits` …
**Sections renamed**: `Delete a Kubernetes cluster` → `Create a Kubernetes cluster`; `Descheduling` → `Rescheduling`; `Create and manage hybrid cloud node pool …` → `Create and manage hybrid node pools`; `Create an Ingress in the ACK console` → `Create an Ingress with the console`

### Data Management — Developer Guide

`443 pages / 20260313` → `447 pages / 20260831` (+4 pages, 204 → 204 sections, 536,201 → 540,308 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Data Management Developer Guide 20260831.md`

**Text new in this edition** (first lines by section)
- `GetOpLog` — Users with the administrator or security administrator role can call this API.
- `CreateFreeLockCorrectOrder` — Only instances in the security collaboration control mode can call this API.
- `CreateTask` — Currently, only the Single-instance SQL Assignment, Script, and ECS Remote Command task nodes support output variables, and their configuration methods differ.
- `GetDBTopology` — Call the GetDBTopology API to retrieve the topology information of a logical database and its corresponding physical database shards.
- `Getting started` — Java Development Kit (JDK) 1.8 or later is installed before you can use Apsara Stack SDK for Java.

**Text no longer present**
- `Handle errors` — Data Management Important If you use a specific error struct, you must add the error package github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors by using the following code:
- `UpdateTaskFlowOwner` — The new owner of the task flow must belong to the same tenant as the previous owner.

**Sections added** (1 total): `API overview`
**Sections dropped** (1 total): `List of operations by function`

### Data Management — User Guide

`239 pages / 20260629` → `242 pages / 20260831` (+3 pages, 133 → 134 sections, 478,325 → 474,226 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Data Management User Guide 20260831.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic describes the new features and important updates for Data Management (DMS). **v3.18.6sp-2607** **v3.18.6sp-2605**

**Text new in this edition** (first lines by section)
- `Control modes` — The instances that are managed in Stable Change mode consume the billing quota of the instances that are managed in Security Collaboration mode.
- `Manage instances` — Only the database instances that are managed in Security Collaboration mode support this operation.
- `Manage databases` — The database instances that are managed in Flexible Management mode do not support this operation.
- `Perform SQL reviews` — After you modify the SQL statements, click Confirm to allow the system to review the SQL statements again.
- `Create an iteration template` — You can select multiple ticket states that allow the iteration to advance to the next stage based on your requirements.
- `Data archiving` — To clean up the archived data from the source table, create a new standard data change ticket.
- `Data archiving` — Create a new lock-free data change ticket to optimize the source tablespace.

**Text no longer present**
- `Control modes` — Data Management Note The instances that are managed in Stable Change mode consume the billing quota of the instances that are managed in Security Collaboration mode.
- `Create an iteration template` — Data Management Data Management Note You can select multiple ticket states that allow the iteration to advance to the next stage based on your requirements.

**Sections added** (3 total): `Console release notes`; `Supported database types and`; `Data archiving`
**Sections dropped** (2 total): `Features that are supported`; `Archive data`

### Data Transmission Service — Developer Guide

`480 pages / 20260313` → `572 pages / 20260901` (+92 pages, 161 → 160 sections, 661,207 → 762,050 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Data Transmission Service Developer Guide 20260901.md`

**Text new in this edition** (first lines by section)
- `Configure HTTPS requests` — Python Set a global default protocol The following sample code shows how to specify a global default protocol:
- `MigrationReserved` — Get started with SDK for Java Get started with SDK for Phython Get started with SDK for Go Related API operations ConfigureMigrationJob ConfigureSynchronizationJob Definition of the Migratio …

**Text no longer present**
- `Configure HTTPS requests` — Data Transmission Service Set a global default protocol The following sample code shows how to specify a global default protocol:
- `Request structure` — Data Transmission Service Protocols You can send API requests over HTTP or HTTPS.
- `MigrationReserved` — Get started with SDK for Java Get started with SDK for Phython Get started with SDK for Go Data Transmission Service Related API operations Definition of the MigrationReserved parameter The …

**Sections added** (1 total): `Query the details of a DTS task`
**Sections dropped** (2 total): `Install the core package of Apsara Stack SDK for Go`; `DescribeDtsJobDetail`

### Data Transmission Service — Operations and Maintenance Guide

`32 pages / 20260629` → `33 pages / 20260826` (+1 pages, 27 → 27 sections, 40,902 → 41,711 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Data Transmission Service Operations and Maintenance Guide 20260826.md`

**Release notes written in the manual itself**
- *Console release notes* — This topic describes the new features and important updates for the DTS console. **v3.18.6sp-2607**

**Text no longer present**
- `Manage DTS resources` — View resource information By default, the information about all DTS resources is displayed.

**Sections added** (1 total): `Console release notes`
**Sections dropped** (1 total): `View DTS resources`

### Data Transmission Service — User Guide

`680 pages / 20260629` → `695 pages / 20260831` (+15 pages, 161 → 160 sections, 1,319,083 → 1,328,708 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Data Transmission Service User Guide 20260831.md`

**Release notes written in the manual itself**
- *Release notes* — This topic describes the new features and important updates of Data Transmission Service (DTS). **v3.18.6sp-2607** **v3.18.6sp-2605** nsole

**Text new in this edition** (first lines by section)
- `Migrate data from a self-managed SQL` — DTS does not support SQL Server clusters or SQL Server Always On availability groups (AOAGs).
- `Migrate data from a self-managed Db2` — If your self-managed Db2 for LUW database uses a whitelist, add the DTS server IP addresses from the dialog box to the whitelist.
- `Configure ETL in a migration task` — Built on code generation technology, which adds minimal overhead to the migration process.
- `Synchronize data from an ApsaraDB RDS` — You can also use DataWorks to add full data merging nodes before you perform further computing and analysis.
- `Synchronize data from RDS MySQL to` — Because the old appended column rule was selected during the task configuration, DTS adds the dts_ prefix to these business fields.
- `Configure ETL in a synchronization task` — For example, for the script script:e_set( new_column , dt_now()) , you must add the new_column column to the target table.
- `Configure ETL in a synchronization task` — When the __OPERATION__ is INSERT, UPDATE, or DELETE, add a new column named "dts_sync_time" and set its value to the log commit time (__COMMIT_TIMESTAMP__).

**Text no longer present**
- `Migrate data from a self-managed SQL` — Data Transmission Service Prerequisites The version of the self-managed SQL Server database is 2005, 2008, 2008 R2, 2012, 2014, 2016, or 2017.
- `Migrate data from an ApsaraDB RDS for` — Data Transmission Service Data Transmission Service SQL operations that support incremental data migration Data Transmission Service Procedure 1.
- `Migrate data between PolarDB for MySQL` — Data Transmission Service SQL operations that support incremental data migration Data Transmission Service Procedure 1.

**Sections added** (11 total): `Release notes`; `Migrate data from a MySQL database`; `Migrate data from a self-managed MySQL`; `Migrate data from a PostgreSQL`; `Migrate data from an Oracle database`; `Migrate data between self-managed Oracle`; `Migrate data from a self-managed Db2`; `Synchronize data between ApsaraDB RDS` …
**Sections dropped** (10 total): `Supported databases, initial`; `instances`; `instance to an AnalyticDB for MySQL V3.0`; `instance to a DataHub project`; `instance to a self-managed Kafka cluster`; `Configure two-way data` …
**Sections renamed**: `Configure ETL in a data migration task` → `Configure ETL in a migration task`; `Configure ETL in a data synchronization` → `Configure ETL in a synchronization task`

### Database Backup — Developer Guide

`12 pages / 20250529` → `114 pages / 20260828` (+102 pages, 23 → 43 sections, 10,378 → 130,099 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Database Backup Developer Guide 20260828.md`

**Text no longer present**
- `Configure the objects to` — The database instance that you want to restore has the existing object DB1.table1 and a new object DB1xxx.table1xxx.

**Sections added** (41 total): `API reference`; `List of operations by function`; `Backup schedule`; `CreateBackupPlan`; `ConfigureBackupPlan`; `DescribeBackupPlanList`; `StartBackupPlan`; `StopBackupPlan` …
**Sections dropped** (21 total): `What is DBS?`; `Technical advantages`; `Feature matrix`; `MySQL`; `PPAS`; `Redis` …

### DataHub — User Guide

`167 pages / 20260629` → `167 pages / 20260825` (+0 pages, 68 → 55 sections, 236,245 → 239,490 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 DataHub User Guide 20260825.md`

**Limits and quotas that changed**
- new · *limits* · Active shards | (0,256] | Each topic can contain up to 256 active shards.
- new · *limits* · Total number of shards | (0,512] | You can create up to 512 shards in each topic.
- new · *limits* · Http BodySize | Up to 4 MB | The size of an HTTP request body cannot exceed 4 MB.
- new · *limits* · String size | Up to 1 MB | The size of a string cannot exceed 1 MB.
- new · *limits* · Waiting time for ShardMerge or ShardSplit | 5s | You cannot perform the ShardMerge or ShardSplit operation on a shard within 5 seconds after the shard is created.
- new · *limits* · QPS | Up to 5,000 | The write QPS limit of a shard is 5,000. Multiple write queries in one batch are considered one query.

**Text new in this edition** (first lines by section)
- `Overview` — Restart the Manager process after you add the path of the shared library to the **Q:
- `OGG Adapters` — This command creates several new Copy the definition file generated on the source to the dirdef directory.
- `OGG Adapters` — Generate definition file Note** This step is not required for OGG versions 12.2.x and later.

**Text no longer present**
- `Synchronize data to` — Use a MaxCompute SDK Use odpscmd Start odpscmd and run the setproject odps.security.ip.whitelist.services=DataHub; command to add DataHub to the service whitelist of MaxCompute.
- `Note` — The DataHub Output and Input plugins for Logstash are open source under the Apache License 2.0.


### DataWorks — User Guide

`1590 pages / 20260629` → `1600 pages / 20260831` (+10 pages, 662 → 654 sections, 2,738,354 → 2,804,701 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 DataWorks User Guide 20260831.md`

**Deprecations / removals stated in the text**
- (Configure HybridDB for MySQL Reader) Data types that are not listed in the preceding table are not supported.
- (Configure PostgreSQL Writer) Except for the field types listed above, other types are not supported.
- (ODPS Script node) The DDL statements used to return data, such as DESC and SHOW statements, are not supported.
- (ODPS Script node) DDL statements that display results on the screen, such as desc and show , are not supported.

**Text new in this edition** (first lines by section)
- `PyODPS 2 nodes` — PyODPS 2 nodes allow you to execute MaxCompute SQL statements to query data and obtain query results.
- `PyODPS 3 node` — DataWorks provides PyODPS 3 nodes, which allow you to directly write Python code for MaxCompute jobs in order to periodically schedule MaxCompute jobs.
- `Isolate data sources` — Only workspaces in standard mode support the data source isolation feature.
- `Configure HybridDB for MySQL Reader` — Data types that are not listed in the preceding table are not supported.
- `Configure PostgreSQL Writer` — Except for the field types listed above, other types are not supported.
- `Configure a full and incremental` — Support for synchronizing data changes generated by DML operations varies based on the destination type.
- `Configure a real-time synchronization` — Configure source tables** The minimum unit for synchronizing data from tables in sharded databases is a logical table.

**Text no longer present**
- `Static column splitting` — You can use commas (,) as the delimiter to split the following data to four new columns, that is, 1111, 2222, 3333, and 4444.
- `PyODPS 2 node` — PyODPS 2 nodes support ODPS SQL queries and allow you to read the execution results.
- `PyODPS 3 node` — This means that instance.open_reader uses the Result API, which can retrieve a maximum of 10,000 records.
  *… 16 further removed lines*

**Sections added** (4 total): `Configure GoldenDB Reader`; `Lock stealing`; `SQL snippet nodes`; `PyODPS 2 nodes`
**Sections dropped** (4 total): `Configure a real-time full-database synchronization task`; `SQL component node`; `Manually correct sensitive data identification results`; `Request processing policies for Data`
**Sections renamed**: `ODPS SQL node` → `ODPS SQL nodes`; `ODPS Spark node` → `ODPS Spark nodes`; `Spark SQL node` → `Spark SQL nodes`; `CDH Spark node` → `CDH Spark nodes`

### Elastic Compute Service — Developer Guide

`836 pages / 20260312` → `465 pages / 20260902` (-371 pages, 221 → 189 sections, 1,420,314 → 1,326,306 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Elastic Compute Service Developer Guide 20260902.md`

**Text new in this edition** (first lines by section)
- `ModifyPrefixList` — For example, if you add an entry with the CIDR block 10.0.0.0/8, you cannot also delete an entry with the CIDR block 10.0.0.0/8.
- `Common parameters` — Common request parameters You can obtain the values of the Product and Version parameters in the Apsara Uni-manager Management Console.
- `RunInstances` — Usage notes Preparations You can select an instance type based on the performance data of instance types.
- `CreateImage` — API description When you call this API, note the following points:
- `CreateImage` — After you successfully call the API, the system creates a snapshot for each cloud disk of the instance.
- `CreateImage` — The system sequentially allocates device names for the data disks from /dev/xvdb to /dev/xvdz by default, and the device names must be unique.
- `ModifyPrefixList` — Do not specify duplicate CIDR blocks when you add or delete entries.

**Text no longer present**
- `Getting started` — We recommend that you use the core library version 4.5.17 or later, and use the SDK version 4.23.2.
- `Install ECS SDK for Java` — We recommend that you use the core library version 4.5.17 or later and use ECS SDK for Java 4.23.2.
- `Log on to the API Tool console` — You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Sections added** (7 total): `Prefix lists`; `CreatePrefixList`; `DescribePrefixLists`; `ModifyPrefixList`; `DescribePrefixListAttributes`; `DescribePrefixListAssociations`; `DeletePrefixList`
**Sections dropped** (28 total): `Preparations`; `Log on to the API Tool console`; `Obtain API information`; `Obtain an AccessKey pair`; `Obtain an STS AccessKey 3-`; `Obtain the values of common` …

### Elastic Compute Service — User Guide

`511 pages / 20260629` → `517 pages / 20260828` (+6 pages, 321 → 124 sections, 909,074 → 914,264 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Elastic Compute Service User Guide 20260828.md`

**Deprecations / removals stated in the text**
- (Connect to a Windows instance from a) Elastic Compute Service If an error message is returned indicating that an authentication error occurs and the function requested is not supported, install CredSSP updates and try again.

**Limits and quotas that changed**
- new · *limits* · Maximum number of system disks per instance | 1 | No

**Text new in this edition** (first lines by section)
- `Create an instance` — Configure the region, instance type, image, storage, and other parameters for the instance.
- `Create an instance` — The quota headroom displays the CPU, GPU, and memory quotas for the current region, organization, and resource set.
- `Create an instance` — The quota headroom displays the disk quotas and the quotas for different cloud disk types in the current region, organization, and resource set.
- `View instance details` — This item lists the allocated CPU quotas for resource sets and subordinate organizations under the current organization, as well as the used CPU quotas for the current organization and its s …
- `View instance details` — This item lists the allocated GPU quotas for resource sets and subordinate organizations under the current organization, as well as the used GPU quotas for the current organization and its s …
- `View instance details` — This item lists the allocated memory quotas for resource sets and subordinate organizations under the current organization, as well as the used memory quotas for the current organization and …
- `View instance details` — In the Customize Columns dialog box, select the instance information to display (for example, add Created By), and then click Save.

**Text no longer present**
- `Enable the multi-attach feature` — After the multi-attach feature is enabled for a premium performance disk, we recommend that you use cluster file systems such as Oracle Cluster File System version 2 (OCFS2), Global File Sys …
- `Install cloud-init` — Compared with Alibaba Cloud cloud-init 19.1.21, Alibaba Cloud cloud-init 23.2.2 provides the following improvements and new features:
- `Limits` — Windows does not support instance types with less than 2 GiB of memory.
  *… 153 further removed lines*

**Sections added** (2 total): `Stop one or more instances`; `View instance details`
**Sections dropped** (247 total): `Connect to a Linux instance by using SSH commands in Linux o …`; `Connect to a Linux instance by using a remote connection too …`; `Connect to a Windows instance from a Windows computer by usi …`; `Instances`; `Use Workbench to connect to a Linux instance over SSH`; `Use Workbench to connect to a Windows instance over RDP` …

### Elasticsearch — Operations and Maintenance Guide

`127 pages / 20260629` → `126 pages / 20260828` (-1 pages, 57 → 57 sections, 213,903 → 211,401 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Elasticsearch Operations and Maintenance Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Log in to the Elasticsearch` — Do not use the default elasticsearch-cluster instance, which is created in the elasticsearch namespace during deployment, for production workloads.
- `Security settings` — After you create a new cluster, you must configure a whitelist first.
- `Security settings` — It has the kibana_system role, which includes only the minimum permissions required for Kibana to initialize and does not allow it to read user data.
- `Security settings` — This role includes only the minimum permissions required for management and cannot be used to read user data.
- `Security settings` — Modify whitelist Important Currently, only Alibaba Cloud Elasticsearch instances support whitelist modification.
- `Security settings` — For information on the minimum effective subnet, consult your delivery or on-site security teams.
- `Security settings` — To add underlying network segments to existing instances in batches, contact Alibaba Cloud technical support for assistance.

**Text no longer present**
- `Log in to the Elasticsearch` — Do not use the default elasticsearch-cluster cluster created during deployment in the elasticsearch namespace to host production workloads.
- `Security settings` — After a successful modification, a success message appears and the port number updates to the new value.
- `Security settings` — Modify whitelist Important Currently, only Elasticsearch instances support whitelist modification.

**Sections added** (2 total): `Elasticsearch metrics on a`; `Blank screen and access issues`
**Sections dropped** (2 total): `Use custom dashboards to`; `GUI exceptions`

### IDaaS — Developer Guide

`555 pages / 20260629` → `555 pages / 20260831` (+0 pages, 236 → 235 sections, 806,746 → 827,442 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 IDaaS Developer Guide 20260831.md`

**Release notes written in the manual itself**
- *Release notes* — **Update date: October 23, 2025** Release description: The first time Identity as a Service (IDaaS) released on Apsara Stack. All API operations of IDaaS are available. 1. List of operations by function **1.1. Instances** **1.2. Applications** **1.3. Accounts** **1.4. Organizations** **1.5. Account groups** **1.6 Identity providers (IdPs)** **1.7. Password policies** **1.8. Synchronization** **1.9.

**Sections dropped** (1 total): `API operations related to account group management`

### MaxCompute — Developer Guide

`316 pages / 20260629` → `552 pages / 20260826` (+236 pages, 191 → 528 sections, 702,816 → 816,976 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Developer Guide 20260826.md`

**Deprecations / removals stated in the text**
- (Usage limits) Language features from Java versions later than Java 8 are not supported.
- (Implementation principles and features) Function calls without return values are not supported because UDT always appears in expressions, and function calls without return values cannot be embedded in expressions.
- (Materialized view operations) QL QL Window functions, User-defined table-valued functions (UDTFs), and non-deterministic functions, such as user-defined scalar functions (UDFs) and user-defined aggregate functions (UDAFs …
- (3.6.2.28.4. RPAD) For the types that are not supported by MaxCompute, this function ignores the data.

**Limits and quotas that changed**
- new · *limits of maxcompute sql* · Table name length | 128 bytes | Size | A table or column name can contain only letters, digits, and underscores ( ). It must start with a _ letter.
- new · *limits of maxcompute sql* · Comment length | 1,024 bytes | Size | A comment is a valid string that cannot exceed 1,024 bytes in length.
- new · *limits of maxcompute sql* · Column definitions in a table | 1,200 | Quantit y | A table can contain a maximum of 1,200 column definitions.
- new · *limits of maxcompute sql* · Partitions in a table | 60,000 | Quantit y | A table can contain a maximum of 60,000 partitions.
- new · *limits of maxcompute sql* · Partition levels of a table | 6 | Quantit y | A table can contain a maximum of six levels of partitions.
- new · *limits of maxcompute sql* · Destination INSERT objects | 256 | Quantit y | In a MULTI-INSERT operation, you can insert data into a maximum of 256 tables at a time.

**Text new in this edition** (first lines by section)
- `Python 3 UDF` — To enable Python 3 when you execute SQL statements, add the following command:
- `Usage limits` — Language features from Java versions later than Java 8 are not supported.
- `Implementation principles and features` — However, UDT does not support Java-style type conversion, such as (Object)1 .
- `SDK for Python` — Similar to the open method built in Python, file resources also support various opening modes.
- `SQL built-in functions` — The support for implicit type conversions of parameters differs for each MaxCompute SQL built-in function.
- `GROUPING and GROUPING_ID` — By default, the columns that are not used in the GROUP BY clause are filled with NULL.
- `WIDTH_BUCKET` — This parameter specifies the minimum value of the acceptable range for the bucket..

**Text no longer present**
- `3.6.2.2. CHR` — The default value 1 indicates the position where a substring matches pattern in the search for the first time.
- `Python 3 UDF` — To enable Python 3 for a job, add the following command before the required SQL statement and execute them together:
- `Implementation principles and feature descript` — For example, the compiler can determine that the value returned by java.util.Arrays.asList(new java.math.BigInteger('1')) is of the java.util.List<java.math.BigInteger> type based on the par …
  *… 15 further removed lines*

**Sections added** (324 total): `Log on to the Apsara Uni-manager`; `Obtain the AccessKey pair of an Alibaba`; `Explicit conversions of data types`; `Implicit type conversion and its application`; `SQL built-in functions`; `CASE WHEN`; `Conversions between the STRING and`; `Create a table` …
**Sections dropped** (18 total): `1.2.2.1. Log on to the Apsara Uni-manager Management Console`; `1.2.2.2. Obtain the AccessKey pair of an organization`; `1.2.2.3. Obtain the AccessKey pair of an Alibaba Cloud accou …`; `3.1.4.5. Conversions between the STRING and DATETIME types`; `3.4.1.12. Forcibly delete data from a table or partition`; `3.5.2.6.2.4. Call the scripts of other programming languages` …
**Sections renamed**: `Partitioned table` → `Partitioned tables`; `3.4.1.8. Modify the value of LastDataMod …` → `Modify the value of LastDataModifiedTime`; `Implementation principles and feature de …` → `Implementation principles and features`; `Common MaxCompute SQL errors and` → `Common MaxCompute SQL`

### MaxCompute — Operations and Maintenance Guide

`174 pages / 20251205` → `160 pages / 20260827` (-14 pages, 104 → 108 sections, 271,494 → 272,499 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute Operations and Maintenance Guide 20260827.md`

**Text new in this edition** (first lines by section)
- `Query and allocate resources` — For example, MinCPU=500 indicates that the quota group can allocate at least 5 (500/100) cores.
- `Query and allocate resources` — MaxCPU=2000 indicates that the quota group can allocate at most 20 (2000/100) cores.
- `Enable and disable SQL acceleration` — For example, you can set this parameter to default:2,12- 23:4 to increase the resource quota in peak hours.
- `Manage service configurations` — If you add xstream_max_worker_num=3 at the end of the configuration file, three workers are launched when you start XStream.
- `Query and allocate resources` — The quota group is allocated 50 CPU cores and all allocated CPU cores are used.
- `Usage notes` — To obtain full capability support within a VPC, you must enable the odpsPPV2Enable feature and set odpsPPV2Enable to true when you plan data in Deployment Planner.
- `odpscmd commands` — By default, the access_id, access_key, end_point, log_view, and tunnel_point parameters are you can view the MaxCompute version.
  *… 9 further added lines in this manual*

**Text no longer present**
- `Query and allocate resources` — In the scenario of the second figure, the 9243 quota group is allocated 50 CPU cores and all allocated CPU cores are used.
- `Manage service configurations` — If you add xstream_max_worker_num=3 at the end of the configuration file, three workers are running when you start XStream.
- `Before you start` — During the MaxCompute O&M process, the default account is admin.
  *… 13 further removed lines*

**Sections added** (28 total): `MaxCompute job workflow`; `Usage notes`; `What is LogView?`; `Work with LogView`; `Routine inspections`; `Dashboard`; `Resource library`; `Business O&M features and entry point` …
**Sections dropped** (20 total): `Concepts and architecture`; `Before you start`; `Preliminary knowledge of LogView`; `LogView usage examples`; `Perform routine inspections`; `Business O&M features and page` …
**Sections renamed**: `Control server roles` → `Control service roles`; `Start AdminConsole` → `Start Admin Console`

### MaxCompute — User Guide

`633 pages / 20260629` → `631 pages / 20260825` (-2 pages, 342 → 339 sections, 982,785 → 1,018,963 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 MaxCompute User Guide 20260825.md`

**Text new in this edition** (first lines by section)
- `Terms` — Basic data types ommon commands ommon commands If you want to use new data types introduced in the MaxCompute V2.0 data type edition, you must add one of the following configurations to enab …
- `Terms` — If you use DataFrame to enable the MaxCompute V2.0 data type edition and want the settings to globally take effect, add the configuration options.sql.use_odps2_extension = ommon commands Tru …
- `UploadSession` — The writer then becomes unusable, and you must open a new writer to resume the upload.
- `Use PyODPS in DataWorks` — For example, use the run_security_query method to call GRANT or REVOKE statements, and use the run_xflow or execute_xflow method to call API commands.
- `SQL` — For example, you must use the run_security_query method to execute GRANT or REVOKE statements, and use the run_xflow or execute_xflow method to call API operations.
- `XFlow and models` — By default, the execution results of the create_online_model method, the not returned until all operations are complete.
- `Column operations` — To perform an exclusive check, set String operations The DataFrame API provides several operations for Sequence or scalar objects of the string type.

**Text no longer present**
- `Terms` — If you want to use new data types introduced in the MaxCompute V2.0 data type edition, you preceding table can contain NULL values.
- `Column operations` — Although the DataFrame API does not support chained comparisons, such as 3 <= String operations The DataFrame API provides several operations for Sequence or scalar objects of the string typ …
- `Use LogView V2.0 to view job` — LogView V2.0 provides a newly designed UI, increases the loading speed, and delivers the following new features:

**Sections added** (3 total): `ACL-based access control`; `Run jobs in local mode`; `Compatibility with Hadoop MapReduce`
**Sections dropped** (5 total): `Job running in local mode`; `Compatible SDK versions`; `Use a PyODPS node to read data from a partitioned table`; `Use a PyODPS node to query data based on specific criteria`; `ACL authorization`

### Message Queue for Apache Kafka — Product Introduction

`17 pages / 20260629` → `17 pages / 20260828` (+0 pages, 9 → 9 sections, 26,410 → 26,143 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Message Queue for Apache Kafka Product Introduction 20260828.md`

**Limits and quotas that changed**
- new · *limitations* · Maximum message size | 10 MB


### Message Queue for Apache Kafka — User Guide

`160 pages / 20260629` → `241 pages / 20260828` (+81 pages, 115 → 151 sections, 235,079 → 342,332 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Message Queue for Apache Kafka User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `http-sink-connector` — Click Add Endpoint Configuration to configure multiple endpoints.

**Text no longer present**
- `Transform configuration` — Message Queue for Apache Kafka Configure converters Note You can click Add converter to add at most 10 converters.

**Sections added** (36 total): `clickhouse-sink-connector`; `github-source-connector`; `hbase-sink-connector`; `lindorm-search-sink-connector`; `lindorm-tsdb-sink-connector`; `lindorm-vector-sink-connector`; `lindorm-widetable-sink-connector`; `mariadb-sink-connector` …

### OpenTrek AgentRuntime — Product Introduction

`16 pages / 20260629` → `16 pages / 20260828` (+0 pages, 8 → 8 sections, 23,736 → 23,360 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek AgentRuntime Product Introduction 20260828.md`

**Limits and quotas that changed**
- new · *limits* · Cluster | Deploy the management cluster and workload clusters separately (at least two Kubernetes clusters). Each cluster requires a minimum configuration of 16 cores and …

**Text new in this edition** (first lines by section)
- `Terms` — These sandboxes support operations such as code execution, file I/O, and web automation, and feature process-level and kernel-level isolation.


### OpenTrek AI Gateway — Product Introduction

`23 pages / 20260629` → `23 pages / 20260828` (+0 pages, 8 → 8 sections, 34,738 → 35,118 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek AI Gateway Product Introduction 20260828.md`

**Limits and quotas that changed**
- new · *usage limits* · Number of routes/services | 5,000 | Exceeding this limit increases the latency of configuration updates from the control plane (xDS pushes). To prevent this, segment your …
- new · *usage limits* · Concurrent connections per node | 50,000 (connection-level) | The Envoy core supports high concurrency. However, in AI scenarios, SSE streaming responses often maintain p …
- new · *usage limits* · Request body size | 32 MB | The default is 4 MB but can be adjusted. Processing large request bodies consumes the gateway's buffer memory. In high-concurrency scenarios, …
- new · *usage limits* · Request timeout | 300 seconds | We recommend increasing the timeout period for time- consuming tasks like large model inference, especially for reasoning-intensive models …


### OpenTrek AI Gateway — User Guide

`358 pages / 20260629` → `370 pages / 20260828` (+12 pages, 110 → 112 sections, 484,304 → 510,958 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 OpenTrek AI Gateway User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Manage quota rules` — The system automatically resets the quota at the start of the corresponding cycle (00:00) based on the selected time zone.
- `Create a quota rule` — Create a gateway instance and make sure that the instance version is 2.1.13.
- `Configure model API policies` — Rate limiting policies support the following rate limiting scopes (time windows), paired with rate limiting units:
- `Manage consumers` — In the Reset Credential dialog box, enable Custom Credential, enter a new credential, and click Reset.
- `Manage consumers` — On the Model API subtab, click Authorization, select one or more model APIs, and then click Confirm.
- `Manage consumers` — On the Model API subtab, click Delete in the Operation column and then click Confirm.
- `AI proxy` — If the name is not in this table, the corresponding protocol does not support the parameter, or the raw mode is not set, the configuration does not take effect.

**Text no longer present**
- `External authentication` — By default, the plugin uses whitelist mode with an Whitelist mode de OpenTrek Blacklist mode Configuration examples When endpoint_mode is envoy Example 1 Configuration for the ext-auth plugi …
- `Route management` — OpenTrek de Note By default, the system retains context across multiple calls.
- `Authorization management` — On the Model API tab, click Authorization, select one or more model APIs from the Model API drop-down list, and then click Determine.

**Sections added** (6 total): `Manage consumers`; `Token quota`; `Create a quota rule`; `Manage quota rules`; `Practice tutorial`; `Access the AI Gateway over`
**Sections dropped** (4 total): `View consumer details`; `Authorization management`; `Modify a consumer`; `Delete consumers`

### Operation Orchestration Service — Product Introduction

`9 pages / 20250728` → `8 pages / 20260828` (-1 pages, 5 → 5 sections, 7,919 → 6,971 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Operation Orchestration Service Product Introduction 20260828.md`

**Text new in this edition** (first lines by section)
- `Product details` — Templates support both YAML and JSON formats and come in two types:
- `Benefits` — All actions, including operations within OOS and tasks that interact with other cloud services, support both authentication and auditing.
- `Use cases` — The process starts with a source image, applies updates step-by-step, and creates a new image for testing and production.
- `Use cases` — This approach provides version control and traceability for your images, which helps prevent environment drift caused by manual changes.
- `Use cases` — You can create a template that runs daily to keep your test environment pristine and prevent previous test data from affecting new results.

**Text no longer present**
- `Scenarios` — You can generate a new image from a source image, and use the new image for testing and production.

**Sections added** (2 total): `Product details`; `Use cases`
**Sections dropped** (2 total): `Service details`; `Scenarios`

### Server Load Balancer — User Guide

`126 pages / 20260629` → `130 pages / 20260828` (+4 pages, 67 → 67 sections, 234,245 → 237,714 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Add backend servers and their` — You can add the primary and secondary ENIs of ECS instances only for highperformance SLB instances.
- `Add backend servers and their` — You can add ECS instances and their associated primary and secondary ENIs to the default server group, a vServer group, or a primary/secondary server group.
- `Create and manage CLB instances` — Before modifying the IP address, you must disable release protection for the instance and ensure that the new IP address is not already allocated.
- `Add a TCP listener` — Add backend servers In the Backend Servers step, add backend servers to process requests received by the SLB instance and click Next**.
- `Add an HTTP listener` — Add backend servers On the Backend Servers wizard page, add backend servers to process requests forwarded by SLB and click Next**.
- `Add an HTTPS listener` — Add backend servers On the Backend Servers wizard page, add backend servers to process requests received by the SLB instance and click Next**.
- `Add and manage additional domain` — The domain name of the certificate must be the same as the additional domain name that you add.

**Text no longer present**
- `Certificate overview` — Server Load Balancer You can add up to 600 certificates with each account.
- `What is SLB?` — After you add ECS instances that are deployed in the same region to an SLB instance, SLB uses virtual IP addresses (VIPs) to virtualize the ECS instances into backend servers in a highperfor …
- `Preparations` — Before you use SLB, you must create ECS instances that function as backend servers, deploy applications on the ECS instances, and then add the ECS instances to your SLB instance to process c …

**Sections renamed**: `Create and manage SLB instances` → `Create and manage CLB instances`

### Virtual Private Cloud — User Guide

`163 pages / 20260629` → `161 pages / 20260828` (-2 pages, 80 → 80 sections, 298,760 → 298,328 characters). Evidence file: `Alibaba Cloud Apsara Stack v3.18.6-2607 Virtual Private Cloud User Guide 20260828.md`

**Text new in this edition** (first lines by section)
- `Overview` — If you create a custom route table and associate the custom route table with a vSwitch for which IPv6 CIDR block is enabled, you must add a custom route whose destination CIDR block is ::/0 …
- `VPC overview` — By default, IPv4 and IPv6 addresses are used only for communication within VPCs.
- `Create and manage VPCs` — After you delete the item, the AI diagnosis tool re-evaluates your resources and generates new suggestions.
- `Scenarios` — Outbound rules Network ACLs for SLB If the ECS instance in the vSwitch acts as the backend server of an SLB instance, you must add the following network ACL rules.
- `View monitoring data` — By default, the system displays monitoring data collected within the previous hour.
- `View monitoring data` — By default, the system displays the monitoring data within the last hour.
- `Overview` — The routes whose destination CIDR blocks are 100.64.0.0/10 and 192.168.0.0/24 are system routes.

**Text no longer present**
- `VPC overview` — Virtual Private Cloud By default, IPv4 and IPv6 addresses are used only for communication within VPCs.
- `Create and manage network` — Virtual Private Cloud On the Network ACLs page, you can add tags to network ACLs for management.
- `Scenarios` — Inbound rules and Outbound rules describe a network ACL example for VPCs that support IPv4 addresses only.

**Sections added** (1 total): `VPC topology`

<details><summary>Manuals with cosmetic-only differences</summary>

| product | manual | pages | doc date |
|---|---|---|---|
| Alibaba Cloud Message Queue | Developer Guide | 386 → 386 | 20260108 → 20260828 |
| Alibaba Cloud Message Queue | Operations and Maintenan | 58 → 63 | 20260629 → 20260831 |
| Alibaba Cloud Message Queue | User Guide | 373 → 379 | 20260629 → 20260828 |
| Alibaba Cloud Security-Web Applicati | Developer Guide | 218 → 214 | 20251212 → 20260828 |
| Alibaba Cloud Security-Web Applicati | Operations and Maintenan | 32 → 32 | 20260629 → 20260828 |
| Alibaba Cloud Security-Web Applicati | Product Introduction | 14 → 13 | 20260629 → 20260831 |
| Alibaba Cloud Security-Web Applicati | User Guide | 60 → 60 | 20260629 → 20260902 |
| Alibaba Cloud Security-Web Applicati | Operations and Maintenan | 10 → 10 | 20260629 → 20260828 |
| Alibaba Cloud Security-Web Applicati | Product Introduction | 12 → 12 | 20260629 → 20260831 |
| API Gateway | Operations and Maintenan | 11 → 11 | 20260629 → 20260828 |
| API Gateway | Product Introduction | 14 → 14 | 20260629 → 20260828 |
| Application Real-time Monitoring Ser | Developer Guide | 110 → 110 | 20250619 → 20260828 |
| Application Real-time Monitoring Ser | Operations and Maintenan | 31 → 31 | 20251205 → 20260828 |
| Apsara Big Data Manager | Operations and Maintenan | 8 → 8 | 20260629 → 20260825 |
| Apsara Big Data Manager | Product Introduction | 12 → 12 | 20251027 → 20260825 |
| Apsara Big Data Manager | User Guide | 50 → 50 | 20260629 → 20260825 |
| Apsara Stack DNS | Developer Guide | 239 → 239 | 20250627 → 20260828 |
| Apsara Stack DNS | Operations and Maintenan | 19 → 19 | 20260310 → 20260828 |
| Apsara Stack DNS | Product Introduction | 16 → 16 | 20250924 → 20260828 |
| Apsara Stack DNS Apsara Stack DNS (M | User Guide | 19 → 19 | 20251103 → 20260828 |
| Apsara Stack Resilience | Product Introduction | 29 → 29 | 20260701 → 20260901 |
| Apsara Stack Resilience ASR for Zone | Developer Guide | 118 → 118 | 20260701 → 20260828 |
| Apsara Stack Resilience ASR for Zone | Operations and Maintenan | 100 → 96 | 20260701 → 20260828 |
| Apsara Uni-manager | Developer Guide | 1123 → 1134 | 20260630 → 20260901 |
| Apsara Uni-manager | Operations and Maintenan | 74 → 74 | 20260629 → 20260828 |
| Apsara Uni-manager | Product Introduction | 22 → 22 | 20260629 → 20260901 |
| ApsaraDB for MongoDB | Developer Guide | 223 → 224 | 20260629 → 20260831 |
| ApsaraDB for MongoDB | Product Introduction | 13 → 13 | 20260629 → 20260828 |
| ApsaraDB for MongoDB | User Guide | 163 → 162 | 20260630 → 20260831 |
| ApsaraDB for POLARDB | Product Introduction | 29 → 29 | 20260629 → 20260901 |
| ApsaraDB for POLARDB PolarDB for MyS | Developer Guide | 126 → 142 | 20260630 → 20260831 |
| ApsaraDB for POLARDB PolarDB for Pos | Developer Guide | 158 → 158 | 20260630 → 20260831 |
| ApsaraDB for POLARDB PolarDB-X 2.0 | Developer Guide | 179 → 179 | 20260629 → 20260831 |
| ApsaraDB for RDS | Developer Guide | 397 → 399 | 20260313 → 20260827 |
| ApsaraDB for RDS | Product Introduction | 38 → 38 | 20260629 → 20260831 |
| Auto Scaling | Developer Guide | 420 → 419 | 20250619 → 20260828 |
| Auto Scaling | Operations and Maintenan | 9 → 8 | 20250619 → 20260828 |
| Auto Scaling | Product Introduction | 9 → 9 | 20250728 → 20260828 |
| Cloud Defined Storage | Product Introduction | 37 → 46 | 20260629 → 20260831 |
| cloud gateway | Developer Guide | 71 → 71 | 20250924 → 20260828 |
| cloud gateway | Operations and Maintenan | 132 → 131 | 20260310 → 20260901 |
| cloud gateway | Product Introduction | 15 → 14 | 20260310 → 20260828 |
| cloud gateway | User Guide | 26 → 26 | 20260310 → 20260828 |
| Cloud Security Firewall | Developer Guide | 114 → 114 | 20251212 → 20260828 |
| Cloud Security Firewall | Operations and Maintenan | 8 → 8 | 20260629 → 20260828 |
| Cloud Security Firewall | Product Introduction | 9 → 9 | 20251030 → 20260828 |
| Cloud Security Firewall | User Guide | 53 → 51 | 20251030 → 20260911 |
| Cloud Security Network Detection and | Developer Guide | 457 → 457 | 20260702 → 20260828 |
| Cloud Security Network Detection and | Operations and Maintenan | 19 → 19 | 20260317 → 20260828 |
| Cloud Security Network Detection and | Product Introduction | 18 → 18 | 20260629 → 20260828 |
| Cloud Security Network Detection and | User Guide | 33 → 33 | 20260629 → 20260828 |
| CloudMonitor | Product Introduction | 18 → 19 | 20260629 → 20260901 |
| Container Registry | Developer Guide | 148 → 147 | 20251202 → 20260828 |
| Container Registry | Operations and Maintenan | 8 → 8 | 20260629 → 20260828 |
| Container Registry | Product Introduction | 12 → 13 | 20260629 → 20260828 |
| Container Service for Kubernetes | Developer Guide | 186 → 185 | 20251202 → 20260828 |
| Container Service for Kubernetes | Operations and Maintenan | 26 → 26 | 20260629 → 20260828 |
| Container Service for Kubernetes Dis | Product Introduction | 12 → 12 | 20260629 → 20260828 |
| Container Service for Kubernetes Dis | User Guide | 22 → 22 | 20260629 → 20260828 |
| Data Management | Product Introduction | 20 → 20 | 20250730 → 20260831 |
| Data Transmission Service | Product Introduction | 20 → 20 | 20251205 → 20260831 |
| Database Backup | Operations and Maintenan | 14 → 14 | 20250626 → 20260828 |
| DataHub | Developer Guide | 128 → 128 | 20260311 → 20260825 |
| DataHub | Operations and Maintenan | 95 → 96 | 20260629 → 20260825 |
| DataHub | Product Introduction | 9 → 9 | 20260306 → 20260825 |
| DataWorks | Developer Guide | 1018 → 1018 | 20260629 → 20260831 |
| DataWorks | Operations and Maintenan | 137 → 139 | 20251204 → 20260825 |
| DataWorks | Product Introduction | 36 → 36 | 20260629 → 20260825 |
| Elastic Compute Service | Introduction to Instance | 57 → 57 | 20260629 → 20260828 |
| Elastic Compute Service | Operations and Maintenan | 210 → 210 | 20260629 → 20260828 |
| Elastic Compute Service | Product Introduction | 31 → 31 | 20260312 → 20260828 |
| Elasticsearch | Developer Guide | 177 → 177 | 20260629 → 20260825 |
| Elasticsearch | Product Introduction | 15 → 15 | 20260629 → 20260825 |
| Elasticsearch | User Guide | 186 → 185 | 20260629 → 20260825 |
| Express Connect | Developer Guide | 151 → 151 | 20251028 → 20260828 |
| Express Connect | Operations and Maintenan | 46 → 46 | 20260310 → 20260828 |
| Express Connect | Product Introduction | 8 → 10 | 20260310 → 20260828 |
| Express Connect | User Guide | 50 → 50 | 20260629 → 20260828 |
| IDaaS | Operations and Maintenan | 20 → 20 | 20260629 → 20260901 |
| IDaaS | Product Introduction | 11 → 11 | 20251216 → 20260831 |
| IDaaS | User Guide | 250 → 250 | 20260630 → 20260831 |
| MaxCompute | Product Introduction | 24 → 24 | 20260629 → 20260825 |
| Message Queue for Apache Kafka | Developer Guide | 125 → 125 | 20251203 → 20260828 |
| Message Queue for Apache Kafka | Operations and Maintenan | 44 → 44 | 20260629 → 20260831 |
| OpenTrek AgentRuntime | User Guide | 73 → 73 | 20260629 → 20260828 |
| Operation Orchestration Service | Developer Guide | 64 → 64 | 20250925 → 20260828 |
| Operation Orchestration Service | Operations and Maintenan | 14 → 37 | 20250925 → 20260828 |
| Operation Orchestration Service | User Guide | 56 → 59 | 20250627 → 20260828 |
| Resource Orchestration Service | Developer Guide | 172 → 172 | 20260312 → 20260828 |
| Resource Orchestration Service | Operations and Maintenan | 7 → 7 | 20250619 → 20260828 |
| Resource Orchestration Service | Product Introduction | 7 → 7 | 20250729 → 20260828 |
| Resource Orchestration Service | User Guide | 476 → 457 | 20260312 → 20260828 |
| Server Load Balancer | Developer Guide | 326 → 326 | 20251028 → 20260828 |
| Server Load Balancer | Operations and Maintenan | 41 → 41 | 20260629 → 20260828 |
| Server Load Balancer | Product Introduction | 21 → 21 | 20260629 → 20260828 |
| Tracing Analysis | Developer Guide | 20 → 20 | 20260313 → 20260828 |
| Tracing Analysis | Operations and Maintenan | 22 → 22 | 20260313 → 20260828 |
| Tracing Analysis | Product Introduction | 8 → 8 | 20260313 → 20260828 |
| Tracing Analysis | User Guide | 84 → 84 | 20260313 → 20260828 |
| TransitRouter | Developer Guide | 258 → 258 | 20250924 → 20260828 |
| TransitRouter | Operations and Maintenan | 12 → 12 | 20251120 → 20260828 |
| TransitRouter | Product Introduction | 9 → 9 | 20260326 → 20260828 |
| TransitRouter | User Guide | 60 → 59 | 20260629 → 20260901 |
| Virtual Private Cloud | Developer Guide | 517 → 517 | 20260629 → 20260828 |
| Virtual Private Cloud | Operations and Maintenan | 116 → 126 | 20260629 → 20260828 |
| Virtual Private Cloud | Product Introduction | 17 → 17 | 20260310 → 20260828 |
| VPN Gateway | Developer Guide | 173 → 173 | 20250619 → 20260828 |
| VPN Gateway | Operations and Maintenan | 9 → 9 | 20260629 → 20260828 |
| VPN Gateway | Product Introduction | 7 → 7 | 20250731 → 20260828 |
| VPN Gateway | User Guide | 56 → 56 | 20260629 → 20260828 |

</details>
## 5. Manuals that appear only in V3.18.6_2607

103 of the 265 manuals have no same-name, same-document-type counterpart in the older English set. They are not all 'new products': the release also renamed catalogue labels wholesale (the folder `云盾` became `云安全中心（专有云）`, products gained sub-edition suffixes), and folder names therefore cannot be used as a pairing key. Each manual below is matched against the *previous English product names* (V3.18.6 and V3.16.2) and classified by how close the closest name is.

- **Back in English (4)** — product name exists in the V3.16.2 English set but was absent from V3.18.6, so this release restores English coverage for it: ApsaraDB for Redis (Operations and Maintenance Guide, 315 pp), ApsaraDB for Redis (User Guide, 185 pp), ApsaraDB for Redis (Developer Guide, 126 pp), ApsaraDB for Redis (Product Introduction, 17 pp).
- **New English title with no close predecessor (4)**: Time Series and Spatial-Temporal Databas … (Developer Guide, 427 pp), Time Series and Spatial-Temporal Databas … (User Guide, 49 pp), Time Series and Spatial-Temporal Databas … (Operations and Maintenance Guide, 27 pp), Time Series and Spatial-Temporal Databas … (Product Introduction, 11 pp).
- **Relabelled / split by edition / new document type (95)** — listed in the table with the closest earlier English name and its similarity score; treat these as catalogue restructuring until a human confirms, not as new products.

| product (V3.18.6_2607) | manual | pages | doc date | closest earlier English name (score, set) |
|---|---|---|---|---|
| Alibaba Cloud Message Queue RocketMQ v5.0 | Developer Guide | 186 | 20260828 | Alibaba Cloud Message Queue (0.814, V3.16.2) |
| Alibaba Cloud Message Queue RocketMQ v5.0 | Product Introduction | 25 | 20260828 | Alibaba Cloud Message Queue (0.814, V3.16.2) |
| Alibaba Cloud Message Queue RocketMQ v5.0 | User Guide | 178 | 20260831 | Alibaba Cloud Message Queue (0.814, V3.16.2) |
| Alibaba Cloud Security-Server Guard Advanced Edition C … | Developer Guide | 189 | 20260828 | Server Guard Advanced Edition (0.542, V3.18.6) |
| Alibaba Cloud Security-Server Guard Advanced Edition C … | Operations and Maintenance | 50 | 20260828 | Server Guard Advanced Edition (0.542, V3.18.6) |
| Alibaba Cloud Security-Server Guard Advanced Edition C … | Product Introduction | 28 | 20260828 | Server Guard Advanced Edition (0.542, V3.18.6) |
| Alibaba Cloud Security-Server Guard Advanced Edition C … | User Guide | 71 | 20260828 | Server Guard Advanced Edition (0.542, V3.18.6) |
| Alibaba Cloud Security-Server Guard Advanced Edition S … | Developer Guide | 225 | 20260828 | Server Guard Advanced Edition (0.531, V3.18.6) |
| Alibaba Cloud Security-Server Guard Advanced Edition S … | Product Introduction | 41 | 20260828 | Server Guard Advanced Edition (0.531, V3.18.6) |
| Alibaba Cloud Security-Server Guard Advanced Edition S … | User Guide | 318 | 20260828 | Server Guard Advanced Edition (0.531, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | Developer Guide | 262 | 20260828 | Cloud Security Management Center (0.604, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | Operations and Maintenance | 13 | 20260828 | Cloud Security Management Center (0.604, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | Product Introduction | 26 | 20260828 | Cloud Security Management Center (0.604, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | User Guide | 69 | 20260828 | Cloud Security Management Center (0.604, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | Operations and Maintenance | 15 | 20260828 | Alibaba Cloud Security-Web Application Firew … (0.583, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | Product Introduction | 12 | 20260828 | Alibaba Cloud Security-Web Application Firew … (0.583, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Cloud Secur … | User Guide | 47 | 20260828 | Alibaba Cloud Security-Web Application Firew … (0.583, V3.18.6) |
| Alibaba Cloud Security-Situation Awareness Security Or … | User Guide | 49 | 20260828 | Security Orchestration Automation and Respon … (0.708, V3.18.6) |
| AnalyticDB for MySQL AnalyticDB for PostgreSQL | Developer Guide | 90 | 20260828 | AnalyticDB for PostgreSQL (0.719, V3.18.6) |
| AnalyticDB for MySQL AnalyticDB for PostgreSQL | Operations and Maintenance | 315 | 20260828 | AnalyticDB for PostgreSQL (0.719, V3.18.6) |
| AnalyticDB for MySQL AnalyticDB for PostgreSQL | User Guide | 259 | 20260828 | AnalyticDB for PostgreSQL (0.719, V3.18.6) |
| Application Operation Platform Application Hybrid Mark … | Operations and Maintenance | 13 | 20260831 | Application Hybrid Marketplace (0.667, V3.18.6) |
| Application Operation Platform Application Hybrid Mark … | Product Introduction | 8 | 20260831 | Application Hybrid Marketplace (0.667, V3.18.6) |
| Application Operation Platform Application Hybrid Mark … | User Guide | 31 | 20260831 | Application Hybrid Marketplace (0.667, V3.18.6) |
| Apsara File Storage NAS | Developer Guide | 129 | 20260827 | File Storage NAS (0.824, V3.18.6) |
| Apsara File Storage NAS | Operations and Maintenance | 14 | 20260827 | File Storage NAS (0.824, V3.18.6) |
| Apsara File Storage NAS | Product Introduction | 8 | 20260827 | File Storage NAS (0.824, V3.18.6) |
| Apsara File Storage NAS | User Guide | 68 | 20260827 | File Storage NAS (0.824, V3.18.6) |
| Apsara Stack Data Center as a service | Developer Guide | 139 | 20260828 | Apsara Stack DNS (0.622, V3.18.6) |
| Apsara Stack Data Center as a service | Operations and Maintenance | 41 | 20260828 | Apsara Stack DNS (0.622, V3.18.6) |
| Apsara Stack Data Center as a service | Product Introduction | 11 | 20260828 | Apsara Stack DNS (0.622, V3.18.6) |
| Apsara Stack Data Center as a service | User Guide | 60 | 20260828 | Apsara Stack DNS (0.622, V3.18.6) |
| Apsara Stack Operation Apsara AIOps | Operations and Maintenance | 29 | 20260902 | Apsara Stack DNS Apsara Stack DNS (Within Cl … (0.6, V3.18.6) |
| Apsara Stack Operation Apsara AIOps | Product Introduction | 11 | 20260828 | Apsara Stack DNS Apsara Stack DNS (Within Cl … (0.6, V3.18.6) |
| Apsara Stack Operation Apsara AIOps | User Guide | 21 | 20260828 | Apsara Stack DNS Apsara Stack DNS (Within Cl … (0.6, V3.18.6) |
| Apsara Uni-manager Apsara Copilot | Developer Guide | 57 | 20260828 | Apsara Uni-manager (0.711, V3.18.6) |
| Apsara Uni-manager Apsara Copilot | Product Introduction | 9 | 20260828 | Apsara Uni-manager (0.711, V3.18.6) |
| Apsara Uni-manager Apsara Copilot | User Guide | 71 | 20260901 | Apsara Uni-manager (0.711, V3.18.6) |
| ApsaraDB for Redis | Developer Guide | 126 | 20260828 | ApsaraDB for Redis (1.0, V3.16.2) |
| ApsaraDB for Redis | Operations and Maintenance | 315 | 20260831 | ApsaraDB for Redis (1.0, V3.16.2) |
| ApsaraDB for Redis | Product Introduction | 17 | 20260828 | ApsaraDB for Redis (1.0, V3.16.2) |
| ApsaraDB for Redis | User Guide | 185 | 20260831 | ApsaraDB for Redis (1.0, V3.16.2) |
| Bastionhost Bastionhost | Product Introduction | 17 | 20260902 | Operation Orchestration Service (0.549, V3.18.6) |
| Bastionhost Tenant-side Bastionhost | Operations and Maintenance | 33 | 20260901 | Tenant-side Bastionhost (0.792, V3.18.6) |
| Bastionhost Tenant-side Bastionhost | User Guide | 149 | 20260901 | Tenant-side Bastionhost (0.792, V3.18.6) |
| Cloud Defined Storage ApsaraStack Parallel File System | Developer Guide | 58 | 20260827 | ApsaraStack Parallel File System (0.753, V3.18.6) |
| Cloud Defined Storage ApsaraStack Parallel File System | Operations and Maintenance | 18 | 20260902 | ApsaraStack Parallel File System (0.753, V3.18.6) |
| Cloud Defined Storage ApsaraStack Parallel File System | Product Introduction | 11 | 20260831 | ApsaraStack Parallel File System (0.753, V3.18.6) |
| Cloud Defined Storage ApsaraStack Parallel File System | User Guide | 20 | 20260902 | ApsaraStack Parallel File System (0.753, V3.18.6) |
| Cloud Defined Storage Cloud Parallel File Storage | Operations and Maintenance | 22 | 20260827 | Cloud Parallel File Storage (0.716, V3.18.6) |
| Cloud Defined Storage Cloud Parallel File Storage | Product Introduction | 10 | 20260827 | Cloud Parallel File Storage (0.716, V3.18.6) |
| Cloud Defined Storage Cloud Parallel File Storage | User Guide | 16 | 20260827 | Cloud Parallel File Storage (0.716, V3.18.6) |
| Cloud Defined Storage Elastic File System NAS | Developer Guide | 164 | 20260831 | Elastic File System NAS (0.678, V3.18.6) |
| Cloud Defined Storage Elastic File System NAS | Operations and Maintenance | 35 | 20260903 | Elastic File System NAS (0.678, V3.18.6) |
| Cloud Defined Storage Elastic File System NAS | Product Introduction | 12 | 20260831 | Elastic File System NAS (0.678, V3.18.6) |
| Cloud Defined Storage Elastic File System NAS | User Guide | 50 | 20260902 | Elastic File System NAS (0.678, V3.18.6) |
| Cloud Security Firewall NFV Cloud Firewall | Developer Guide | 178 | 20260828 | Cloud Security Firewall (0.724, V3.18.6) |
| Cloud Security Firewall NFV Cloud Firewall | Product Introduction | 14 | 20260828 | Cloud Security Firewall (0.724, V3.18.6) |
| Cloud Security Firewall NFV Cloud Firewall | User Guide | 205 | 20260828 | Cloud Security Firewall (0.724, V3.18.6) |
| Database Audit Database Security Audit | Developer Guide | 98 | 20260831 | Database Security Audit (0.764, V3.18.6) |
| Database Audit Database Security Audit | Operations and Maintenance | 29 | 20260831 | Database Security Audit (0.764, V3.18.6) |
| Database Audit Database Security Audit | Product Introduction | 14 | 20260831 | Database Security Audit (0.764, V3.18.6) |
| Database Audit Database Security Audit | User Guide | 121 | 20260831 | Database Security Audit (0.764, V3.18.6) |
| Database Audit Static Data Masking and Watermarking | Operations and Maintenance | 22 | 20260831 | Static Data Masking and Watermarking (0.831, V3.18.6) |
| Database Audit Static Data Masking and Watermarking | Product Introduction | 16 | 20260831 | Static Data Masking and Watermarking (0.831, V3.18.6) |
| Database Audit Static Data Masking and Watermarking | User Guide | 150 | 20260831 | Static Data Masking and Watermarking (0.831, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Ente … | Developer Guide | 201 | 20260828 | Enterprise Distributed Application Service (0.645, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Ente … | Operations and Maintenance | 71 | 20260828 | Enterprise Distributed Application Service (0.645, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Ente … | Product Introduction | 16 | 20260828 | Enterprise Distributed Application Service (0.645, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Ente … | User Guide | 1118 | 20260828 | Enterprise Distributed Application Service (0.645, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Sche … | Developer Guide | 102 | 20260828 | Enterprise Distributed Application Service (0.83, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Sche … | Operations and Maintenance | 13 | 20260828 | Enterprise Distributed Application Service (0.83, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Sche … | Product Introduction | 10 | 20260828 | Enterprise Distributed Application Service (0.83, V3.18.6) |
| Enterprise Distributed Application Service (EDAS) Sche … | User Guide | 139 | 20260828 | Enterprise Distributed Application Service (0.83, V3.18.6) |
| Key Management Service Key Management Service | Developer Guide | 127 | 20260831 | Key Management Service (0.667, V3.18.6) |
| Key Management Service Key Management Service | Operations and Maintenance | 25 | 20260831 | Key Management Service (0.667, V3.18.6) |
| Key Management Service Key Management Service | Product Introduction | 9 | 20260831 | Key Management Service (0.667, V3.18.6) |
| Key Management Service Key Management Service | User Guide | 51 | 20260831 | Key Management Service (0.667, V3.18.6) |
| Machine Learning Platform for AI Bare Metal Computing … | Developer Guide | 355 | 20260731 | Bare Metal Computing Platform (0.65, V3.18.6) |
| Machine Learning Platform for AI Bare Metal Computing … | Operations and Maintenance | 73 | 20260731 | Bare Metal Computing Platform (0.65, V3.18.6) |
| Machine Learning Platform for AI Bare Metal Computing … | Product Introduction | 13 | 20260731 | Bare Metal Computing Platform (0.65, V3.18.6) |
| Machine Learning Platform for AI Bare Metal Computing … | User Guide | 149 | 20260731 | Bare Metal Computing Platform (0.65, V3.18.6) |
| OpenTrek OpenTrek AI Studio | Operations and Maintenance | 26 | 20260901 | OpenTrek AI Studio (0.8, V3.18.6) |
| OpenTrek OpenTrek AI Studio | Product Introduction | 15 | 20260831 | OpenTrek AI Studio (0.8, V3.18.6) |
| OpenTrek OpenTrek Dev | Developer Guide | 279 | 20260901 | OpenTrek Dev (0.733, V3.18.6) |
| OpenTrek OpenTrek Dev | Operations and Maintenance | 82 | 20260902 | OpenTrek Dev (0.733, V3.18.6) |
| OpenTrek OpenTrek Dev | Product Introduction | 35 | 20260901 | OpenTrek Dev (0.733, V3.18.6) |
| OpenTrek OpenTrek-Ops | Product Introduction | 16 | 20260902 | OpenTrek-Ops (0.733, V3.18.6) |
| OpenTrek OpenTrek-Ops | User Guide | 68 | 20260902 | OpenTrek-Ops (0.733, V3.18.6) |
| Prometheus Service | Developer Guide | 24 | 20260828 | Log Service (0.593, V3.16.2) |
| Prometheus Service | Operations and Maintenance | 13 | 20260828 | Log Service (0.593, V3.16.2) |
| Prometheus Service | Product Introduction | 16 | 20260828 | Log Service (0.593, V3.16.2) |
| Prometheus Service | User Guide | 80 | 20260828 | Log Service (0.593, V3.16.2) |
| Realtime Compute Realtime Compute for Apache Flink (Co … | Developer Guide | 452 | 20260828 | Realtime Compute for Apache Flink (Compute-S … (0.889, V3.18.6) |
| Realtime Compute Realtime Compute for Apache Flink (Co … | Operations and Maintenance | 56 | 20260825 | Realtime Compute for Apache Flink (Compute-S … (0.889, V3.18.6) |
| Realtime Compute Realtime Compute for Apache Flink (Co … | Product Introduction | 13 | 20260825 | Realtime Compute for Apache Flink (Compute-S … (0.889, V3.18.6) |
| Realtime Compute Realtime Compute for Apache Flink (Co … | User Guide | 105 | 20260831 | Realtime Compute for Apache Flink (Compute-S … (0.889, V3.18.6) |
| Server Load Balancer Application Load Balancer | Product Introduction | 20 | 20260828 | Application Load Balancer (0.719, V3.18.6) |
| Server Load Balancer Application Load Balancer | User Guide | 137 | 20260828 | Application Load Balancer (0.719, V3.18.6) |
| Time Series and Spatial-Temporal Database | Developer Guide | 427 | 20260827 | — none — |
| Time Series and Spatial-Temporal Database | Operations and Maintenance | 27 | 20260827 | — none — |
| Time Series and Spatial-Temporal Database | Product Introduction | 11 | 20260827 | — none — |
| Time Series and Spatial-Temporal Database | User Guide | 49 | 20260827 | — none — |

## 6. V3.18.6 manuals not carried into this set

125 manuals exist in the older `V3.18.6` set with no counterpart in `V3.18.6_2607`. Their text was **not** superseded inside this refresh, so the older file remains the current English reference for them (they are still in the local corpus, nothing was deleted).

| product | manual | pages | doc date |
|---|---|---|---|
| Alibaba Cloud Security-Web Application Firewall (WAF) Web … | Developer Guide | 196 | 20260629 |
| Alibaba Cloud Security-Web Application Firewall (WAF) Web … | User Guide | 54 | 20260629 |
| AnalyticDB for PostgreSQL | Developer Guide | 90 | 20260630 |
| AnalyticDB for PostgreSQL | Operations and Maintenance | 91 | 20260630 |
| AnalyticDB for PostgreSQL | User Guide | 258 | 20260630 |
| Application Hybrid Marketplace | Operations and Maintenance | 13 | 20260630 |
| Application Hybrid Marketplace | Product Introduction | 8 | 20260630 |
| Application Hybrid Marketplace | User Guide | 31 | 20260630 |
| Application Load Balancer | Product Introduction | 20 | 20260701 |
| Application Load Balancer | User Guide | 136 | 20260701 |
| Apsara AIOps | Operations and Maintenance | 22 | 20260701 |
| Apsara AIOps | Product Introduction | 11 | 20260701 |
| Apsara AIOps | User Guide | 21 | 20260701 |
| Apsara Copilot | Developer Guide | 57 | 20260701 |
| Apsara Copilot | Product Introduction | 9 | 20260701 |
| Apsara Copilot | User Guide | 61 | 20260701 |
| Apsara Stack Resilience ASR for Backup and Recovery | Developer Guide | 279 | 20260701 |
| Apsara Stack Resilience ASR for Backup and Recovery | Operations and Maintenance | 141 | 20260701 |
| Apsara Stack Resilience ASR for Backup and Recovery | User Guide | 299 | 20260701 |
| Apsara Stack Resilience Cloud Platform Backup | User Guide | 13 | 20260701 |
| Apsara Stack Resilience Cloud Platform Backup and O&M Guid … | 20260701 | 12 | 20260701 |
| Apsara Stack Security Security Administrator Guide | 20250529 | 38 | 20250529 |
| Apsara Uni-manager Operations Console | Developer Guide | 580 | 20260703 |
| Apsara Uni-manager Operations Console | Operations and Maintenance | 25 | 20260703 |
| Apsara Uni-manager Operations Console | Product Introduction | 19 | 20260703 |
| Apsara Uni-manager Operations Console | User Guide | 710 | 20260703 |
| Apsara Uni-manager Operations Console Platform Operation a … | Operations Guide | 1253 | 20260703 |
| ApsaraStack Parallel File System | Developer Guide | 59 | 20260701 |
| ApsaraStack Parallel File System | Operations and Maintenance | 18 | 20260701 |
| ApsaraStack Parallel File System | Product Introduction | 11 | 20260701 |
| ApsaraStack Parallel File System | User Guide | 14 | 20260701 |
| Bare Metal Computing Platform | Developer Guide | 158 | 20251205 |
| Bare Metal Computing Platform | Operations and Maintenance | 60 | 20260630 |
| Bare Metal Computing Platform | Product Introduction | 13 | 20250930 |
| Bare Metal Computing Platform | User Guide | 121 | 20260630 |
| BareMetal Mangement Service | Operations and Maintenance | 41 | 20260630 |
| BareMetal Mangement Service | User Guide | 60 | 20260630 |
| BareMetal Mangement Service | Developer Guide | 139 | 20251205 |
| BareMetal Mangement Service | Product Introduction | 11 | 20251205 |
| Cloud Defined Storage | Developer Guide | 2021 | 20260629 |
| cloud migration hub | Product Introduction | 12 | 20260303 |
| cloud migration hub | User Guide | 133 | 20251217 |
| Cloud Parallel File Storage | Developer Guide | 38 | 20260701 |
| Cloud Parallel File Storage | Operations and Maintenance | 22 | 20260701 |
| Cloud Parallel File Storage | Product Introduction | 10 | 20260701 |
| Cloud Parallel File Storage | User Guide | 19 | 20260701 |
| Cloud Security Management Center | Developer Guide | 262 | 20260701 |
| Cloud Security Management Center | Operations and Maintenance | 13 | 20260701 |
| Cloud Security Management Center | Product Introduction | 26 | 20260701 |
| Cloud Security Management Center | User Guide | 56 | 20260701 |
| Cloud Security Scanner | Developer Guide | 233 | 20260701 |
| Cloud Security Scanner | Operations and Maintenance | 15 | 20260701 |
| Cloud Security Scanner | Product Introduction | 12 | 20260701 |
| Cloud Security Scanner | User Guide | 47 | 20260701 |
| Cloud-native Gateway | Product Introduction | 12 | 20260630 |
| Cloud-native Gateway | User Guide | 188 | 20260630 |
| Container Security Service | Developer Guide | 189 | 20260701 |
| Container Security Service | Operations and Maintenance | 50 | 20260701 |
| Container Security Service | Product Introduction | 28 | 20260701 |
| Container Security Service | User Guide | 69 | 20260701 |
| Database Backup | User Guide | 52 | 20250529 |
| Database Security Audit | Developer Guide | 98 | 20260701 |
| Database Security Audit | Operations and Maintenance | 29 | 20260701 |
| Database Security Audit | Product Introduction | 14 | 20260701 |
| Database Security Audit | User Guide | 121 | 20260701 |
| Elastic File System NAS | Developer Guide | 145 | 20260701 |
| Elastic File System NAS | Operations and Maintenance | 35 | 20260701 |
| Elastic File System NAS | Product Introduction | 11 | 20260701 |
| Elastic File System NAS | User Guide | 42 | 20260701 |
| Enterprise Distributed Application Service | Developer Guide | 201 | 20260701 |
| Enterprise Distributed Application Service | Operations and Maintenance | 71 | 20260701 |
| Enterprise Distributed Application Service | Product Introduction | 16 | 20260701 |
| Enterprise Distributed Application Service | User Guide | 1118 | 20260701 |
| File Storage NAS | Developer Guide | 129 | 20260701 |
| File Storage NAS | Operations and Maintenance | 14 | 20260701 |
| File Storage NAS | Product Introduction | 8 | 20260701 |
| File Storage NAS | User Guide | 68 | 20260701 |
| Key Management Service | Developer Guide | 127 | 20260701 |
| Key Management Service | Operations and Maintenance | 25 | 20260701 |
| Key Management Service | Product Introduction | 9 | 20260701 |
| Key Management Service | User Guide | 44 | 20260701 |
| Lindorm | Developer Guide | 426 | 20250825 |
| Lindorm | Operations and Maintenance | 27 | 20260630 |
| Lindorm | Product Introduction | 11 | 20250930 |
| Lindorm | User Guide | 49 | 20260630 |
| Managed Service for Prometheus | Developer Guide | 24 | 20260422 |
| Managed Service for Prometheus | Operations and Maintenance | 13 | 20260422 |
| Managed Service for Prometheus | Product Introduction | 16 | 20260703 |
| Managed Service for Prometheus | User Guide | 80 | 20260703 |
| NFV Cloud Firewall | Developer Guide | 178 | 20260701 |
| NFV Cloud Firewall | Product Introduction | 14 | 20260701 |
| NFV Cloud Firewall | User Guide | 205 | 20260701 |
| OpenTrek AI Studio | Operations and Maintenance | 25 | 20260630 |
| OpenTrek AI Studio | Product Introduction | 12 | 20260630 |
| OpenTrek Dev | Developer Guide | 279 | 20260630 |
| OpenTrek Dev | Operations and Maintenance | 76 | 20260630 |
| OpenTrek Dev | Product Introduction | 32 | 20260630 |
| OpenTrek-Ops | Product Introduction | 14 | 20260630 |
| OpenTrek-Ops | User Guide | 39 | 20260630 |
| Realtime Compute for Apache Flink (Compute-Storage Separat … | Developer Guide | 370 | 20260701 |
| Realtime Compute for Apache Flink (Compute-Storage Separat … | Operations and Maintenance | 56 | 20260701 |
| Realtime Compute for Apache Flink (Compute-Storage Separat … | Product Introduction | 13 | 20260701 |
| Realtime Compute for Apache Flink (Compute-Storage Separat … | User Guide | 524 | 20260701 |
| SchedulerX 2.0 | Developer Guide | 102 | 20260701 |
| SchedulerX 2.0 | Operations and Maintenance | 13 | 20260701 |
| SchedulerX 2.0 | Product Introduction | 10 | 20260701 |
| SchedulerX 2.0 | User Guide | 139 | 20260701 |
| Security Orchestration Automation and Response (SOAR) | Developer Guide | 46 | 20260701 |
| Security Orchestration Automation and Response (SOAR) | Operations and Maintenance | 10 | 20260701 |
| Security Orchestration Automation and Response (SOAR) | Product Introduction | 19 | 20260701 |
| Security Orchestration Automation and Response (SOAR) | User Guide | 49 | 20260701 |
| Server Guard Advanced Edition | Developer Guide | 225 | 20260701 |
| Server Guard Advanced Edition | Operations and Maintenance | 12 | 20260701 |
| Server Guard Advanced Edition | Product Introduction | 41 | 20260701 |
| Server Guard Advanced Edition | User Guide | 318 | 20260701 |
| Static Data Masking and Watermarking | Operations and Maintenance | 22 | 20260701 |
| Static Data Masking and Watermarking | Product Introduction | 16 | 20260701 |
| Static Data Masking and Watermarking | User Guide | 151 | 20260701 |
| Tair（Redis OSS-compatible） | Developer Guide | 126 | 20260630 |
| Tair（Redis OSS-compatible） | Operations and Maintenance | 89 | 20260630 |
| Tair（Redis OSS-compatible） | Product Introduction | 17 | 20260630 |
| Tair（Redis OSS-compatible） | User Guide | 172 | 20260630 |
| Tenant-side Bastionhost | Product Introduction | 17 | 20260701 |
| Tenant-side Bastionhost | Operations and Maintenance | 33 | 20260701 |
| Tenant-side Bastionhost | User Guide | 149 | 20260701 |

## 7. Method, and what it cannot tell you

1. Both editions were downloaded as official PDFs, converted to text-only Markdown with the same line classifier, and every page hash-verified; PDFs are not kept locally by design.
2. Manuals are paired by **exact** product name + document type after normalisation. No fuzzy pairing: at 0.90 similarity *ApsaraDB for RDS* matched *ApsaraDB for Redis*, which would have manufactured `changes`. Unmatched names are listed in Sections 4/5 instead of being guessed.
3. Textual deltas are **sentence-level, not line-level**: PDF re-flow moves line breaks between editions, so lines are re-joined per section and split on punctuation before comparison. Three gates then run: (i) headings, tables, fenced code, log samples and regex fragments are dropped; (ii) template text recurring in ≥ 8% of the paired corpus is dropped; (iii) only *informative* sentences are counted — those carrying a version/number/quota or a support/add/deprecate/change verb, with self-describing UI narration ("This topic describes…", "On the X page, click…") excluded. Gates (i)–(iii) leave 1,256 added / 929 removed informative sentences; re-typing cancellation then reduces that to 1,160 / 833 — which are the figures quoted in §1. Counting raw *lines* instead of sentences inflates the delta by an order of magnitude, because PDF line breaks move between editions.
3b. Quoted lines are verbatim extracts from the converted Markdown. The PDF extraction occasionally duplicates a short token or reorders a cell ("QL QL Window functions", "start with a _ letter"); those are extraction artifacts of our converter, not typographical errors in the manual, and they do not affect the substance of the quoted sentence.
4. Section counting normalises numbered headings (`2.1.1.2.3. Limits_1578278510` → `limits`), so a re-number is not counted as add + drop. Renames are reported when the normalised titles are ≥ 0.85 similar.
5. What this cannot show: why a change was made; whether removed text reflects a dropped feature or an editorial decision; and anything for the 103 unpaired manuals, which have no baseline in this set. Limits rows are only compared where both editions carry the same row key.
6. Full machine-readable evidence (all added/removed lines per manual, with section attribution): `.scratch/rn2607_pairs.json` in the session workspace.

## 8. Where the files are

| path | contents |
|---|---|
| `markdown/10_EN_ApsaraStack_V3.18.6_2607/` | the 265 manuals behind this note |
| `markdown/10_EN_ApsaraStack_v3.18.6/` | the older 287-manual English set used as baseline |
| `文档缓存索引.csv` | 901 rows; `id / versionStamp / pages / markdown / markdownSha256` |
| `markdown_全量_901册.zip` | whole corpus, one zip |

