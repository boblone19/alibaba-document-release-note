---
title: "Alibaba Cloud Apsara Stack V3.18.3 Log Service Operations and Maintenance Guide 20241029"
product_version: "V3.18.3"
doc_version: "20241029"
pdf_pages: 20
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Log Service Operations and Maintenance Guide 20241029.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%97%A5%E5%BF%97%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Log%20Service%20Operations%20and%20Maintenance%20Guide%2020241029.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Log Service Operations and Maintenance Guide 20241029

## Table of Contents

- 1 O&M methods
  - 2.1 Use the service terminal to view logs on machines
  - 2.2 Use the CLI to maintain Log Service
  - 2.3 Use CDS-Intelligent O&M to query logs

## 1 O&M methods

This topic describes the two O&M methods of Log Service. Log Service is deployed, managed, and maintained by using the Apsara Infrastructure Management console. Log Service supports the following O&M methods: Terminal: In the Apsara Infrastructure Management console, you can use the terminal service to log on to the machine where Log Service resides and view logs. Command-line interface (CLI): Log Service provides the CLI to meet the requirements for automated configurations. You can use the CLI to manage projects, Logstores, machine groups, consumer groups, and Logtail configurations. You can also use the CLI to query logs.

**Terminal**

1. Log on to the Apsara Uni-manager Operations Console.
2. Log on to the Apsara Infrastructure Management console.
In the top navigation bar of the Apsara Uni-manager Operations Console, click **Products**. Then, choose **Base/Platforms > Apsara Infrastructure Management**.
3. Go to the Project O&M page.
i. In the left-side navigation pane, click **Project & Cluster O&M**. ii. On the **Project O&M** page, enter `sls` in the **Project | Cluster** field. The `CdsSlsHybridCluster***` in the search results is the cluster where Log Service resides. iii. Click **Status Details** in the **Actions** column.
4. On the **Product Details** page, select a component and click **Terminal** in the Actions
column. In this example, the sls-backend-server.ServiceTest component is used.
5. Log on to the machine by using the terminal service and go to the related directory to view
logs. Log Service CLI provides the following features: Supports most RESTful API operations of Log Service. For example, you can use the CLI to manage projects, Logstores, machine groups, consumer groups, and Logtail configurations. Allows you to manage logs across multiple accounts and regions. Allows you to query and pull logs. Allows you to migrate data from Elasticsearch to Log Service. Supports flexible time configurations. Allows you to replicate logs across regions at a high speed, reindex historical logs, and ship logs to data warehouses.
1. Download and install the Log Service CLI.
For more information, see Log Service CLI.
2. Obtain a project name, an endpoint, and an AccessKey pair.
For more information, see the related topics in **Log Service Developer Guide**.
3. Use Log Service CLI to query logs and maintain Log Service.
For more information, see Log Service CLI.

## 2 O&M

### 2.1 Use the service terminal to view logs on machines

**view logs on machines**

In the Apsara Infrastructure Management console, you can use the terminal service to log on to the machine where Log Service resides and view logs.

**DBPostHandler#**

Startup log: /cloud/app/sls-backendserver/DBPostHandler#/db_post_handler/current/log/start.log Service log: none

**DBPreHandler#**

Startup log: /cloud/app/sls-backendserver/DBPreHandler#/db_pre_handler/current/log/start.log Service log: none

**InitSlsCluster#**

Startup log: /cloud/app/sls-backendserver/InitSlsCluster#/init_sls_cluster/current/log/start.log Service log: none

**ServiceTest#**

Startup log: /cloud/app/sls-backendserver/ServiceTest#/service_test_monitor/current/log/service_monitor.log Service log: none

**SlsAppProcessMonitor#**

Startup logs: /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_common_worker_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_config_service_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_etl_framework_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_loghub_master_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_presto_worker_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_query_master_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_quota_server_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_replay_worker_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_shennong_worker_monitor/current/log/start.log Service log: none

**SlsCommonWorkerDecider#**

Startup log: /cloud/app/sls-backendserver/SlsCommonWorkerDecider#/sls_common_worker_decider/current/log/start.log Service log: none

**SlsConfigManager#**

Startup log: /cloud/app/sls-backendserver/SlsConfigManager#/sls_config_manager/current/log/start.log Service log: none

**SlsConfigServiceDecider#**

Startup log: /cloud/app/sls-backendserver/SlsConfigServiceDecider#/sls_config_service_decider/current/log/start.log Service log: none

**SlsDeployFuxiless#**

Startup log: /cloud/app/sls-backendserver/SlsDeployFuxiless#/sls_deploy_fuxiless/current/log/start.log Service log: none

**SlsEtlFrameworkDecider#**

Startup log: /cloud/app/sls-backendserver/SlsEtlFrameworkDecider#/sls_etl_framework_decider/current/log/start.log Service log: none

**SlsImportOdpsScheduler#**

Startup log: /cloud/app/sls-backendserver/SlsImportOdpsScheduler#/sls_import_odps_scheduler/current/log/start.log Service log: none

**SlsLoghubMasterDecider#**

Startup log: /cloud/app/sls-backendserver/SlsLoghubMasterDecider#/sls_loghub_master_decider/current/log/start.log Service log: none

**SlsPrometheus#**

Startup log: /cloud/app/sls-backendserver/SlsPrometheus#/sls_prometheus/current/log/start.log Service log: none

**SlsQueryMasterDecider#**

Startup log: /cloud/app/sls-backendserver/SlsQueryMasterDecider#/sls_query_master_decider/current/log/start.log Service log: none

**SlsQuotaServerDecider#**

Startup log: /cloud/app/sls-backendserver/SlsQuotaServerDecider#/sls_quota_server_decider/current/log/start.log Service log: none

**SlsReplayWorkerDecider#**

Startup log: /cloud/app/sls-backendserver/SlsReplayWorkerDecider#/sls_replay_worker_decider/current/log/start.log Service log: none

**SlsReplayWorkerDecider#**

Startup log: /cloud/app/sls-backendserver/SlsReplayWorkerDecider#/sls_replay_worker_decider/current/log/start.log Service log: none

**SlsShennongWorkerDecider#**

Startup log: /cloud/app/sls-backendserver/SlsShennongWorkerDecider#/sls_shennong_worker_decider/current/log/start.log Service log: none

**ToolService#**

Startup logs: /cloud/app/sls-backendserver/ToolService#/init_diamond/current/log/diamond_publish_content.LOG /cloud/app/sls-backend-server/ToolService#/init_diamond/current/log/start.log /cloud/app/sls-backend-server/ToolService#/init_odps/current/log/start.log /cloud/app/sls-backend-server/ToolService#/init_pop/current/log/start.log /cloud/app/sls-backend-server/ToolService#/jdk_uploader/current/log/start.log Service log: none

### 2.2 Use the CLI to maintain Log Service

**Service**

Log Service provides the command-line interface (CLI) to meet the requirements for automated configurations in Log Service. You can use the CLI to manage projects, Logstores, machine groups, consumer groups, and Logtail configurations. You can also use the CLI to query logs. Log Service CLI provides the following features: Supports most RESTful API operations of Log Service. For example, you can use the CLI to manage projects, Logstores, machine groups, consumer groups, and Logtail configurations. Allows you to manage logs across multiple accounts and regions. Allows you to query and pull logs. Allows you to migrate data from Elasticsearch to Log Service. Supports flexible time configurations. Allows you to replicate logs across regions at a high speed, reindex historical logs, and ship logs to data warehouses.
1. Download and install the Log Service CLI.
For more information, see Log Service CLI.
2. Obtain a project name, an endpoint, and an AccessKey pair.
For more information, see the related topics in **Log Service Developer Guide**.
3. Use Log Service CLI to query logs and maintain Log Service.
For more information, see Log Service CLI.

### 2.3 Use CDS-Intelligent O&M to query logs

**query logs**

The system centrally stores and indexes logs of key services. You can query logs within a specified time range by service type, project, and storage service.

**Background information**

Logs are not permanently stored. The system automatically clears logs on a regular basis. The log retention period varies based on the cloud service. The log retention period is determined by the amount of logs and the severity of the logs. The maximum log retention period of Alibaba Cloud services does not exceed 30 days.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
3. In the left-side navigation pane, choose **CDS-Intelligent Maintenance > Log Search**.
4. On the **Log Search** page, configure the Type, Project, Storage, and Select Date parameters
and specify a search condition.

| and an analytic statement in the |   |
|---|---|
| * \| SELECT status, count(*) AS PV GROUP |   |

A search condition consists of a search statement and an analytic statement in the `Search`

| statement\|Analytic statement |   |
|---|---|
|   | . The search statem |

statement|Analytic statement format. Example: * | SELECT status, count(*) AS PV GROUP `BY status` . The search statement and the analytic statement are separated by a vertical bar (|). The search statement uses proprietary syntax of Simple Log Service. A search statement can be executed alone. However, an analytic statement must be executed together with a search statement. You can use the log analysis feature to analyze the data in search results. You can also use the feature to analyze all data in a Logstore. For more information, see "Simple Log Service > Query and analysis" in **CDS User Guide**.

| Statement | Description |
|---|---|
| Search statement | A search statement specifies one or more search conditions, and then returns the logs that meet the specified conditions. A search statement can be a keyword, a numeric value, a numeric value range, a space character, or an asterisk (*). If you specify a space or an asterisk (*) as the search statement, no conditions are specified and all logs are returned. |
| Analytic statement | An analytic statement is used to aggregate or analyze all log data or the log data that meets the specified search conditions in a Logstore. |

5. Click **Query**.
The system displays the log data that meets the conditions.

**Note**

Different types of logs have different formats. The actual log formats prevail.

**Supported logs**

The following table describes the **Simple Log Service** Logstores whose detailed logs you can query. The logs are generated after Simple Log Service initializes each service.

|   |   | Logstore |   | config name _ |   | log path |   | server role |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   | action trail _ |   | None |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ | sls-backend- |   |
|   |   |   |   |   | e | sMetaServiceRole/Act |   |   |   |
|   |   |   |   |   |   |   |   | server.SlsMetaServ |   |
|   |   |   | _ |   |   |   |   |   |   |
|   |   |   |   |   |   | ionTrailOplog.LOG |   |   |   |
|   |   | alert-metering |   |   |   | /apsara/sls/sls Et _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Et _ |   |   |
|   |   |   |   |   |   | lFrameworkPartitionR |   |   |   |
|   |   |   |   |   |   |   |   | sls-backend- server.SlsEtlFramewor |   |
|   |   |   | etering | None | e |   |   | s |   |
|   |   |   |   |   |   | ole/alert metering.L _ |   | k |   |
|   |   |   |   |   |   | OG |   |   |   |
|   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   | oot/sys/DispatchWork |   |   |   |
|   |   |   |   | dispatch worker log _ _ | atch worker log |   |   |   |   |
|   |   |   |   |   |   | er/*dispatch worker. _ |   |   |   |
|   |   |   |   |   |   | LOG |   |   |   |
|   |   | dispatch worker log _ _ |   |   |   |   |   |   |   |
|   |   |   |   | dispatch worker log f |   | /apsara/sls/sls Di _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Di _ |   |   |
|   |   |   |   |   | atch worker log f | spatchWorkerPartitio |   |   |   |
|   |   |   |   | _ _ _ uxiless | _ _ _ |   |   |   |   |
|   |   |   |   |   |   | nRole/*dispatch work _ |   |   |   |
|   |   |   |   |   |   | er.LOG |   |   |   |
|   |   |   |   | etl framework log fuxi |   | /apsara/sls/sls Et _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Et _ |   |   |
|   |   |   |   |   | framework log fuxi | lFrameworkPartitionR |   |   |   |
|   |   |   |   | _ _ _ less | _ _ |   |   |   |   |
|   |   |   |   |   |   | ole/etl worker.LOG _ |   |   |   |
|   |   | etl framework log _ _ |   |   |   |   |   |   |   |
|   |   |   |   | etl framework log |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   | framework log | oot/sys/EtlFramework |   |   |   |
|   |   |   |   | _ _ | _ |   |   |   |   |
|   |   |   |   |   |   | /etl worker.LOG _ |   |   |   |
|   |   | etl golang worker log _ _ _ |   | etl golang worker log _ _ _ |   | /apsara/tubo/TempRoo t/sys/EtlFramework/etl golang worker.LOG _ _ |   | sls-backend- server.SlsEtlFramewor k# |   |
|   |   |   |   | etl golang worker log _ _ _ fuxiless _ |   | /apsara/sls/sls EtlFram _ eworkPartitionRole/etl _ golang worker.LOG _ |   |   |   |

|   |   |   |   | oss shipper metering |   | /apsara/sls/sls Sh _ |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | /apsara/sls/sls Sh _ |   |   |
|   |   |   |   |   | shipper metering | ennongReplayWorkerRo |   |   |   |
|   |   |   |   | _ _ _ log fuxiless _ | _ _ _ |   |   |   |   |
|   |   |   |   |   |   | le/oss shipper meter _ _ |   |   |   |
|   |   |   |   |   |   | ing.LOG |   |   |   |
|   |   |   |   | odps shipper meterin |   | /apsara/sls/import |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/import |   |   |
|   |   |   |   |   | s shipper meterin | odps/scheduler/odps _ |   |   |   |
|   |   |   |   | _ _ g log _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | shipper metering.lo _ _ |   |   |   |
|   |   |   |   |   |   | g |   |   |   |
|   |   | etl metering _ |   |   |   |   |   |   |   |
|   |   |   |   | export metering log |   | /usr/local/export/ |   |   |   |
|   |   |   |   |   |   |   | /usr/local/export/ | server.SlsShennongWo |   |
|   |   |   |   |   | ort metering log | export * metering.lo _ _ |   |   |   |
|   |   |   |   | _ _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | g |   |   |   |
|   |   |   |   | python etl metering _ _ |   | /usr/local/python- etl/metering.log |   |   |   |
|   |   |   |   | oss shipper metering |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   | shipper metering | oot/sys/ShennongRepl |   |   |   |
|   |   |   |   | _ _ _ log | _ _ _ |   |   |   |   |
|   |   |   |   |   |   | ayWorker/oss shipper _ |   |   |   |
|   |   |   |   |   |   | metering.LOG _ |   |   |   |
|   |   | export service log _ _ |   | redis op log |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   | is op log | sExportServiceRole/r |   |   |   |
|   |   |   |   | _ _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | edis worker.log _ |   |   |   |
|   |   |   |   | export service worker |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   | ort service worker | sExportServiceRole/e |   |   |   |
|   |   |   |   |   |   |   |   | sls-backend- server.SlsExportServic |   |
|   |   |   | service log _ _ | _ _ log _ | _ _ |   |   | serv |   |
|   |   |   |   |   |   | xport service worker _ _ |   | e# |   |
|   |   |   |   |   |   | .log |   |   |   |
|   |   |   |   | export service log |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   | ort service log | sExportServiceRole/E |   |   |   |
|   |   |   |   | _ _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | xportService.LOG |   |   |   |
|   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   | oot/sys/FcTriggerWor |   |   |   |
|   |   |   |   |   |   |   |   | None |   |
|   |   |   |   | fc trigger log _ _ | rigger log |   |   |   |   |
|   |   |   |   |   |   | ker/fc trigger.log _ |   |   |   |
|   |   | fc trigger log _ _ |   |   |   |   |   |   |   |
|   |   |   |   | fc trigger log fuxiless |   | /apsara/sls/sls Fc _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Fc _ |   |   |
|   |   |   |   |   | rigger log fuxiless | TriggerWorkerRole/fc |   |   |   |
|   |   |   |   |   |   |   |   | None |   |
|   |   |   |   | _ _ _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | trigger.log _ |   |   |   |

|   |   | /usr/local/python- |   |
|---|---|---|---|
| hon etl metering _ _ | etl/metering.log |   |   |

|   | forwarder-grpc |   |   |   |   |   | /cloud/app/sls- |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | /cloud/app/sls- |   |   |
|   |   |   |   |   |   |   | backend- |   |   |   |
|   |   |   |   |   |   |   | server/SlsForwarderP |   |   |   |
|   |   | orwarder-grpc |   |   |   |   |   |   |   |   |
|   |   |   |   | forwarder-grpc |   |   | rometheus#/sls forwa _ |   | None |   |
|   |   |   |   |   |   |   | rder prometheus/curr _ |   |   |   |
|   |   |   |   |   |   |   | ent/forwarder- |   |   |   |
|   |   |   |   |   |   |   | grpc.json |   |   |   |
|   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |
|   |   |   |   |   |   |   | sls-backend- |   |   |   |
|   |   |   |   |   |   |   | server/SlsForwarderK |   |   |   |
|   |   |   |   |   |   |   | afka#/sls forwarder _ _ |   |   |   |
|   |   |   |   |   |   |   | kafka/current/sls fo _ |   |   |   |
|   |   |   |   |   |   |   | rwarder kafka releas _ _ |   |   |   |
|   |   |   |   |   |   |   | e 64/kafka/logs/erro _ |   |   |   |
|   |   |   |   | forwarder-kafka-error |   |   | r.log |   |   |   |
|   | forwarder-kafka |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |
|   |   |   |   |   |   |   | sls-backend- |   |   |   |
|   |   |   |   |   |   |   | server/SlsForwarderK |   |   |   |
|   |   |   |   | forwarder-kafka- |   |   | afka#/sls forwarder _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   | None |   |
|   |   |   |   | access |   |   | kafka/current/sls fo _ |   |   |   |
|   |   |   |   |   |   |   | rwarder kafka releas _ _ |   |   |   |
|   |   |   |   |   |   |   | e 64/kafka/logs/acce _ |   |   |   |
|   |   |   |   |   |   |   | ss.log |   |   |   |
|   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |
|   |   |   |   |   |   |   | sls-backend- |   |   |   |
|   |   |   |   |   |   |   | server/SlsForwarderS |   |   |   |
|   |   |   |   |   |   |   |   |   | sls-backend- |   |
|   |   |   |   |   |   |   | yslog#/sls forwarder _ |   |   |   |
|   | forwarder-syslog |   |   | forwarder-syslog |   |   |   |   | server.SlsForwarderSy |   |
|   |   |   |   |   |   |   | syslog/current/sls _ _ |   | slog# |   |
|   |   |   |   |   |   |   | forwarder syslog rel _ _ |   |   |   |
|   |   |   |   |   |   |   | ease 64/syslog- _ |   |   |   |
|   |   |   |   |   |   |   | forwarder.json |   |   |   |
|   | kms sql log _ _ |   |   | kms sql log _ _ |   |   | /apsara/tubo/TempRoo t/sys/SlsKmsWrapperS ervice/kms sql.LOG _ |   | sls-backend- server.SlsKmsWrapper Service# |   |
|   | 2 |   |   | > Doc |   |   |   |   | ument Version: 2024102 |   |

|   |   | og Service |   |   |   |   |   |   | ions and Maintenance Gu de·O&M |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   | kms sql log fuxiless _ _ _ |   | /apsara/sls/sls KmsWr _ apperServiceWorker/k ms sql.LOG _ |   |   |   |
|   |   |   |   |   | kms worker log fuxile |   | /apsara/sls/sls Km _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/sls Km _ |   |   |
|   |   |   |   |   |   | s worker log fuxile | sWrapperServiceWorke |   |   |   |
|   |   |   |   |   | _ _ _ ss | _ _ _ |   |   |   |   |
|   |   |   |   |   |   |   | r/sls kms wrapper se _ _ _ |   |   |   |
|   |   |   |   |   |   |   | rvice worker.LOG _ |   |   |   |
|   |   | kms worker log _ _ |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/tubo/TempR | Service# |   |
|   |   |   |   |   |   |   | oot/sys/SlsKmsWrappe |   |   |   |
|   |   |   |   |   | kms worker log |   |   |   |   |   |
|   |   |   |   |   |   |   | rService/sls kms wra _ _ |   |   |   |
|   |   |   |   |   | _ _ |   |   |   |   |   |
|   |   |   |   |   |   |   | pper service worker. _ _ |   |   |   |
|   |   |   |   |   |   |   | LOG |   |   |   |
|   |   | logtail alarm _ |   |   | None |   | None |   | sls-backend- server.SlsLogtail# |   |
|   |   | logtail status profile _ _ |   |   | None |   | None |   |   |   |
|   |   | logtail suicide profile _ _ |   |   | None |   | None |   |   |   |
|   |   | metering |   |   | metering |   | /apsara/sls/meteri ng.log |   | sls-backend- server.SlsMeteringServ ice# |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   |   |   | sMirrorsls-backend- |   |   |   |
|   |   |   |   |   |   |   | server.SlsMirrorServ |   |   |   |
|   |   |   |   |   |   |   | ice#ServiceRole/mirr |   |   |   |
|   |   |   |   |   |   |   | or service worker.LO _ _ |   |   |   |
|   |   | mirror service |   |   | mirror service |   |   |   |   |   |
|   |   | _ |   |   | _ |   | G |   |   |   |
|   |   | nginx error log _ _ |   |   | nginx error log _ _ |   | /apsara/sls/nginx/ logs/error.log |   | sls-backend- server.Nginx# |   |
|   |   | offline scheduler log _ _ |   |   | offline scheduler log |   | /apsara/sls/import |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/import |   |   |
|   |   |   |   |   |   | ne scheduler log | odps/scheduler/impo _ |   |   |   |
|   |   |   | _ _ |   | _ _ | _ _ |   |   |   |   |
|   |   |   |   |   |   |   | rt odps*.log _ |   |   |   |

|   |   | /apsara/sls/meteri | sls-ba serve |
|---|---|---|---|
| ering | ng.log |   |   |

|   |   | /apsara/sls/nginx/ | sls-backend- |
|---|---|---|---|
| nx error log _ _ | logs/error.log |   |   |

|   | pk-query |   | pk-query |   | /apsara/tubo/TempR |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   | query | oot/sys/ShennongWork |   |   |   |
|   |   |   |   |   | er/pk query.LOG _ |   |   |   |
|   |   |   | pk-query fuxiless |   | /apsara/sls/sls Sh _ |   |   |   |
|   |   |   |   |   |   | /apsara/sls/sls Sh _ | rker# |   |
|   |   |   |   | query fuxiless | ennongWorkerRole/pk _ |   |   |   |
|   |   |   | _ | _ |   |   |   |   |
|   |   |   |   |   | query.LOG |   |   |   |
|   | presto gc log _ _ |   | presto gc log |   | /apsara/presto/pre |   |   |   |
|   |   |   |   |   |   | /apsara/presto/pre |   |   |
|   |   |   |   | sto gc log | sto data/var/log/gc. _ |   |   |   |
|   |   | _ _ | _ _ | _ _ |   |   |   |   |
|   |   |   |   |   | log* |   |   |   |
|   | presto http _ |   | presto http |   | /apsara/presto/pre |   |   |   |
|   |   |   |   |   |   | /apsara/presto/pre |   |   |
|   |   |   |   | sto http | sto data/var/log/htt _ |   |   |   |
|   |   | _ | _ | _ |   |   |   |   |
|   |   |   |   |   | p-request.log |   |   |   |
|   | presto metering _ |   | presto metering |   | /apsara/presto/pre |   |   |   |
|   |   |   |   |   |   | /apsara/presto/pre |   |   |
|   |   |   |   | sto metering | sto data/var/log/met _ |   |   |   |
|   |   | _ | _ | _ |   |   |   |   |
|   |   |   |   |   | ering.log |   |   |   |
|   | presto monitor _ |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   | oot/sys/PrestoWorker |   |   |   |
|   |   | monitor _ | presto monitor _ | sto monitor |   |   |   |   |
|   |   |   |   |   | /presto monitor.LOG _ |   |   |   |
|   | presto server _ |   | presto server |   | /apsara/presto/pre |   |   |   |
|   |   |   |   |   |   | /apsara/presto/pre | r# |   |
|   |   |   |   | sto server | sto data/var/log/ser _ |   |   |   |
|   |   |   | _ | _ |   |   |   |   |
|   |   |   |   |   | ver.log |   |   |   |
|   |   |   | presto server fuxiless |   | /apsara/sls/presto |   |   |   |
|   |   |   |   |   |   | /apsara/sls/presto |   |   |
|   |   |   |   | sto server fuxiless | /presto data/var/log _ |   |   |   |
|   |   |   | _ _ | _ _ |   |   |   |   |
|   |   |   |   |   | /server.log |   |   |   |
|   | presto sql server _ _ |   | presto sql server _ _ |   | /apsara/presto/sls sql _ _ server.LOG |   |   |   |
|   | presto worker _ |   | presto worker _ |   | /apsara/tubo/TempRoo t/sys/PrestoWorker/pre sto worker.LOG _ |   |   |   |
|   |   |   | presto worker fuxiless _ _ |   | /apsara/sls/sls Presto _ WorkerRole/presto wo _ rker.LOG |   |   |   |

|   | prometheus-backend- |   |   |   |   |   | /cloud/app/sls- |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | /cloud/app/sls- |   |   |
|   |   |   |   |   |   |   | backend- |   |   |   |
|   |   |   |   |   |   |   | server/SlsPrometheus |   |   |   |
|   |   | prometheus-backend- |   | prometheus-backend- |   |   |   |   |   |   |
|   |   |   |   |   |   |   | #/sls prometheus/cur _ |   |   |   |
|   | log | og |   | log |   |   |   |   |   |   |
|   |   |   |   |   |   |   | rent/aos sls prometh _ _ |   |   |   |
|   |   |   |   |   |   |   | eus release 64/sls p _ _ _ |   |   |   |
|   |   |   |   |   |   |   | rometheus.LOG* |   |   |   |
|   | prometheus-log |   |   |   |   |   | /cloud/app/sls- |   |   |   |
|   |   |   |   |   |   |   |   | /cloud/app/sls- |   |   |
|   |   |   |   |   |   |   | backend- |   |   |   |
|   |   |   |   |   |   |   | server/SlsPrometheus |   |   |   |
|   |   | prometheus-log |   | prometheus-log |   |   |   |   |   |   |
|   |   |   |   |   |   |   | #/sls prometheus/cur _ |   |   |   |
|   |   |   |   |   |   |   | rent/prometheus*.LOG |   |   |   |
|   | query master log _ _ |   |   | query master log |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   | ry master log |   | oot/sys/QueryMaster/ |   |   |   |
|   |   |   |   | _ _ | _ _ |   |   |   |   |   |
|   |   |   |   |   |   |   | query master.LOG* _ |   |   |   |
|   |   |   |   | query master log fuxil _ _ _ |   |   | /apsara/sls/sls Qu _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/sls Qu _ | # |   |
|   |   |   |   |   | ry master log fuxil _ _ _ |   | eryMasterRole/query _ |   |   |   |
|   |   |   |   | ess |   |   |   |   |   |   |
|   |   |   |   |   |   |   | master.LOG* |   |   |   |
|   | replication status _ |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   |   |   | sMirrorServiceRole/m |   |   |   |
|   |   |   |   |   |   |   |   |   | sls-backend- server.SlsMirrorService |   |
|   |   |   | tion status _ | replication status _ | lication status |   |   |   | server |   |
|   |   |   |   |   |   |   | irror service schedu _ _ |   | # |   |
|   |   |   |   |   |   |   | le.LOG |   |   |   |
|   | scmc access log _ _ |   |   | scmc access log |   |   | /apsara/sls/nginx/ |   | sls-backend- server.SlsScmc# |   |
|   |   |   |   |   |   |   |   | /apsara/sls/nginx/ |   |   |
|   |   |   |   |   | c access log |   | logs/scmc access.log _ |   |   |   |
|   |   |   | _ | _ _ | _ _ |   |   |   |   |   |
|   | scmc err log _ _ |   |   | scmc err log _ _ |   |   | /apsara/sls/nginx/ logs/scmc err log _ _ |   |   |   |
|   | scmc op log _ _ |   |   | scmc op log _ _ |   |   | /apsara/sls/nginx/ logs/scmc op log _ _ |   |   |   |
|   | shennong log profile _ _ |   |   | None |   |   | None |   | sls-backend- server.SlsShennongWo rker# |   |

|   |   | /apsara/sls/nginx/ | sls-backend- server.SlsScmc# |
|---|---|---|---|
| c err log _ _ | logs/scmc err log _ _ |   |   |

|   |   | /apsara/sls/nginx/ |   |
|---|---|---|---|
| c op log _ _ | logs/scmc op log _ _ |   |   |

|   |   |   | sls configservice log _ _ |   |   |   | sls configservice log |   |   | /apsara/sls Config _ |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | /apsara/sls Config _ |   |   |
|   |   |   |   |   |   |   |   | configservice log |   | ServiceRole/sls conf _ |   |   |   |
|   |   |   |   |   |   |   | _ _ | _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ig service.LOG _ |   |   |   |
|   |   |   |   |   |   |   | sls configservice log f |   |   | /apsara/sls/sls Co _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /apsara/sls/sls Co _ |   |   |
|   |   |   |   |   |   |   |   | configservice log f |   | nfigServiceRole/sls _ |   |   |   |
|   |   |   |   |   |   |   | _ _ _ uxiless | _ _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | config service.LOG _ |   |   |   |
|   |   |   |   |   |   |   | sls configservice quer |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /apsara/tubo/TempR | e# |   |
|   |   |   |   |   |   |   |   | configservice quer |   | oot/sys/*ConfigServi |   |   |   |
|   |   |   |   |   |   |   | _ _ y log _ | _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ce/config service qu _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ery.LOG |   |   |   |
|   |   |   | sls configservice quer _ _ y log _ |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | sls configservice quer |   |   | /apsara/sls/sls Co _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /apsara/sls/sls Co _ |   |   |
|   |   |   |   |   |   |   |   | configservice quer |   | nfigServiceRole/conf |   |   |   |
|   |   |   |   |   |   |   | _ _ y log fuxiless _ _ | _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ig service query.LOG _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /apsara/cloud/app/ |   |   |
|   |   |   |   |   |   |   |   |   |   | sls-backend- |   |   |   |
|   |   |   |   |   |   |   |   |   |   | server/SlsConsole#/s |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ls console/current/s _ |   |   |   |
|   |   |   | sls console error log |   |   |   | sls console error log |   |   | ls console/logs/erro _ |   |   |   |
|   |   |   | _ _ _ |   |   |   | _ _ _ |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | r.log |   |   |   |
|   |   |   | sls console info log _ _ _ |   |   |   |   |   |   | /cloud/app/sls- |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /cloud/app/sls- |   |   |
|   |   |   |   |   |   |   |   |   |   | backend- |   |   |   |
|   |   |   |   |   |   |   |   |   |   | server/SlsConsole#/s |   |   |   |
|   |   |   |   | ls console info log _ _ _ |   |   | sls console info log |   |   |   |   |   |   |
|   |   |   |   |   |   |   | _ _ _ |   |   | ls console/current/s _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ls console/logs/info _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | .log |   |   |   |
|   |   |   | sls consumergroup lo _ _ g |   |   |   | sls consumergroup lo _ _ |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   |   |   | consumergroup lo _ |   | oot/sys/QuotaServer/ |   |   |   |
|   |   |   |   |   |   |   | g |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | monitor.LOG |   |   |   |
|   |   |   |   |   |   |   | sls consumergroup lo _ _ |   |   | /apsara/sls/sls Qu _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | /apsara/sls/sls Qu _ | server.SlsQuotaServer # |   |
|   |   |   |   |   |   |   |   | consumergroup lo _ |   | otaServerRole/monito |   |   |   |
|   |   |   |   |   |   |   | g fuxiless _ | uxiless |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | r.LOG |   |   |   |

|   |   | sls etl20 coordinator l _ _ _ og |   | sls etl20 coordinator l _ _ _ |   | /apsara/sls/sls Sl _ |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ | sls-backend- |   |
|   |   |   |   |   | etl20 coordinator l _ _ | sEtl20CoordinatorRol |   |   |   |
|   |   |   |   |   |   |   |   | server.SlsEtl20C |   |
|   |   |   |   | og |   |   |   |   |   |
|   |   |   |   |   |   | e/SlsEtl20.LOG* |   |   |   |
|   |   | sls etl20 job checker _ _ _ _ log |   | sls etl20 job checker _ _ _ _ log |   | /apsara/sls/sls SlsEtl20 _ JobCheckerRole/SlsEtl2 0.LOG* |   | sls-backend- server.SlsEtl20JobChec kerRole# |   |
|   |   | sls etl20 sts proxy lo _ _ _ _ g |   | sls etl20 sts proxy lo _ _ _ _ |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ | sls-backend- |   |
|   |   |   |   |   | etl20 sts proxy lo _ _ _ | sEtl20StsProxyRole/S |   |   |   |
|   |   |   |   |   |   |   |   | server.SlsEtl2 |   |
|   |   |   |   | g |   |   |   |   |   |
|   |   |   |   |   |   | lsEtl20.LOG* |   |   |   |
|   |   | sls etl20 worker grou _ _ _ pb log _ |   | sls etl20 worker grou _ _ _ |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ | sls-backend- |   |
|   |   |   |   |   | etl20 worker grou _ _ | sEtl20WorkerGroupBRo |   |   |   |
|   |   |   |   |   |   |   |   | server.SlsEtl20Wo |   |
|   |   |   |   | pb log _ | log |   |   |   |   |
|   |   |   |   |   |   | le/SlsEtl20.LOG* |   |   |   |
|   |   | sls etl20 worker log _ _ _ |   | sls etl20 worker log |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sl _ | sls-backend- |   |
|   |   |   |   |   | etl20 worker log | sEtl20WorkerRole/Sls |   |   |   |
|   |   |   |   |   |   |   |   | server.SlsE |   |
|   |   |   | _ _ | _ _ _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | Etl20.LOG* |   |   |   |
|   |   | sls fastcgi log _ _ |   | sls fastcgi log |   | /apsara/sls/fcgi a _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/fcgi a _ | sls-backend- |   |
|   |   |   |   |   | fastcgi log | gent/FastcgiAgent*.L |   | s |   |
|   |   |   |   |   |   |   |   | s |   |
|   |   |   | _ | _ _ | _ |   |   |   |   |
|   |   |   |   |   |   | OG |   |   |   |
|   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   | oot/sys/ShennongWork |   |   |   |
|   |   |   |   | sls index status log _ _ _ |   |   |   |   |   |
|   |   |   |   |   |   | er/project index siz _ _ |   |   |   |
|   |   |   |   |   |   | e.LOG |   |   |   |
|   |   | sls index status log _ _ _ |   |   |   |   |   |   |   |
|   |   |   |   | sls index status log f |   | /apsara/sls/sls Sh _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Sh _ |   |   |
|   |   |   |   |   | index status log f | ennongWorkerRole/pro |   |   |   |
|   |   |   |   | _ _ _ _ uxiless | _ _ _ |   |   |   |   |
|   |   |   |   |   |   | ject index size.LOG _ _ |   |   |   |
|   |   |   |   | sls loghub shard statu |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   | loghub shard statu | oot/sys/LoghubMaster |   |   |   |
|   |   |   |   | _ _ _ s log _ | _ _ |   |   |   |   |
|   |   |   |   |   |   | /loghub master meta. _ _ |   |   |   |
|   |   |   |   |   |   | LOG |   |   |   |
|   |   | sls loghub shard statu _ _ _ s log _ |   |   |   |   |   |   |   |
|   |   |   |   | sls loghub shard statu _ _ _ |   | /apsara/sls/sls Lo _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/sls/sls Lo _ |   |   |
|   |   |   |   |   | loghub shard statu _ _ | ghubMasterRole/loghu |   |   |   |
|   |   |   |   | s log fuxiless _ _ | g fuxiless |   |   |   |   |
|   |   |   |   |   |   | b master meta.LOG _ _ |   |   |   |

|   |   |   |   |   |   |   |   |   |   |   | sls-backend- |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/tubo/TempR | server.SlsLoghubMast |   |
|   |   |   |   |   |   |   |   |   | oot/sys/LoghubMaster |   | er# |   |
|   |   |   |   |   |   | sls loghubmaster log _ _ | loghubmaster log |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | /sls loghub master.L _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   | OG |   |   |   |
|   | sls loghubmaster log _ _ |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | sls loghubmaster log _ _ _ |   |   | /apsara/sls/sls Lo _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/sls/sls Lo _ |   |   |
|   |   |   |   |   |   |   | loghubmaster log _ _ |   | ghubMasterRole/sls l _ |   |   |   |
|   |   |   |   |   |   | fuxiless | less |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | oghub master.LOG _ |   |   |   |
|   | sls meta service _ _ |   |   |   |   | sls meta service |   |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   |   |   | meta service |   | sMetaServiceRole/Met |   |   |   |
|   |   |   | _ |   |   | _ _ | _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | aService.LOG |   |   |   |
|   | sls meta service oplo _ _ _ g |   |   |   |   | sls meta service oplo _ _ _ |   |   | /apsara/sls/sls Sl _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/sls/sls Sl _ |   |   |
|   |   |   |   |   |   |   | meta service oplo _ _ |   | sMetaServiceRole/Met |   |   |   |
|   |   |   |   |   |   | g |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | aServiceOplog.LOG |   |   |   |
|   | sls metering service l _ _ _ og |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   |   |   |   | oot/sys/SlsMeteringS |   |   |   |
|   |   |   |   |   |   | sls metering service l _ _ _ og | metering service l |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ervice/stdout.out |   |   |   |
|   |   |   |   |   |   |   |   |   | /cloud/log/sls- |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /cloud/log/sls- | ice# |   |
|   |   |   |   |   |   |   |   |   | backend- |   |   |   |
|   |   |   |   |   |   | sls metering service l |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | server/SlsMeteringSe |   |   |   |
|   |   |   |   |   |   | _ _ _ |   |   |   |   |   |   |
|   |   |   |   |   |   | og fuxiless _ |   |   | rvice#/sls metering _ _ |   |   |   |
|   |   |   |   |   |   |   |   |   | service app/tianji/s _ |   |   |   |
|   |   |   |   |   |   |   |   |   | tdout |   |   |   |
|   | sls monitor log _ _ |   |   |   |   | sls monitor log _ _ |   |   | /apsara/sls/fcgi a _ gent/monitor *.LOG _ |   | sls-backend- server.SlsFastcgi# |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/sls/fcgi a _ |   |   |
|   |   |   |   |   |   |   | monitor log _ |   | gent/monitor *.LOG _ |   |   |   |
|   | sls operation agg log _ _ _ |   |   |   |   | sls operation agg log |   |   | /apsara/sls/fcgi a _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/sls/fcgi a _ |   |   |
|   |   |   |   |   |   |   | operation agg log |   | gent/metering *.LOG _ |   |   |   |
|   |   |   |   | _ _ |   | _ _ _ | _ _ |   |   |   |   |   |
|   | sls operation log _ _ |   |   |   |   | sls operation log |   |   | /apsara/sls/fcgi a _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   | /apsara/sls/fcgi a _ |   |   |
|   |   |   |   |   |   |   | operation log |   | gent/ols operation*. _ |   |   |   |
|   |   |   | _ |   |   | _ _ | _ |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | LOG |   |   |   |

| sls portal access log _ _ _ |   | sls portal access log _ _ _ |   | /apsara/sls/web/lo gs/access.log |   | sls-backend- server.SlsWeb# |   |
|---|---|---|---|---|---|---|---|
| sls portal api audit _ _ _ |   | sls portal api audit _ _ _ |   | /apsara/sls/web/lo gs/apidetail.log |   |   |   |
| sls portal http req _ _ _ |   | sls portal http req _ _ _ |   | /apsara/sls/web/lo gs/httpclient.log |   |   |   |
| sls portal normal _ _ |   | sls portal normal _ _ |   | /apsara/sls/web/lo gs/normal.log |   |   |   |
| sls portal sys info _ _ _ |   | sls portal sys info _ _ _ |   | /apsara/sls/web/lo gs/sysinfo.log |   |   |   |
| sls quotaserver log _ _ |   | sls quotaserver log |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   | quotaserver log | oot/sys/QuotaServer/ |   |   |   |
|   |   | _ _ | _ |   |   |   |   |
|   |   |   |   | quota server.LOG _ |   |   |   |
|   |   | sls quotaserver log fu _ _ _ |   | /apsara/sls/sls Qu _ |   |   |   |
|   |   |   |   |   | /apsara/sls/sls Qu _ |   |   |
|   |   |   | quotaserver log fu _ _ | otaServerRole/quota _ |   |   |   |
|   |   | xiless | ss |   |   |   |   |
|   |   |   |   | server.LOG |   |   |   |
| sls quotausage log _ _ |   | sls quotausage log |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   | /apsara/tubo/TempR | # |   |
|   |   |   | quotausage log | oot/sys/QuotaServer/ |   |   |   |
|   |   | _ _ | _ |   |   |   |   |
|   |   |   |   | charge.LOG |   |   |   |
|   |   | sls quotausage log fu _ _ _ |   | /apsara/sls/sls Qu _ |   |   |   |
|   |   |   |   |   | /apsara/sls/sls Qu _ |   |   |
|   |   |   | quotausage log fu _ _ | otaServerRole/charge |   |   |   |
|   |   | xiless | ss |   |   |   |   |
|   |   |   |   | .LOG |   |   |   |
| sls replayworker log _ _ |   | sls replayworker log _ _ |   | /apsara/tubo/TempRoo t/sys/ShennongReplay Worker/shennong repl _ ay worker.LOG _ |   | sls-backend- server.SlsReplayWorke r# |   |
|   |   | sls replayworker log f _ _ _ uxiless |   | /apsara/sls/sls Shenno _ ngReplayWorkerRole/s hennong replay worke _ _ r.LOG |   |   |   |

|   |   | /apsara/sls/web/lo |   |
|---|---|---|---|
| portal access log _ _ | gs/access.log |   |   |

|   |   | /apsara/sls/web/lo |   |
|---|---|---|---|
| portal api audit _ _ | gs/apidetail.log |   |   |

|   |   | /apsara/sls/web/lo | sls-backend- |
|---|---|---|---|
| portal http req _ _ | gs/httpclient.log |   |   |

|   |   | /apsara/sls/web/lo |   |
|---|---|---|---|
| portal normal _ | gs/normal.log |   |   |

|   |   | /apsara/sls/web/lo |   |
|---|---|---|---|
| portal sys info _ _ | gs/sysinfo.log |   |   |

|   |   | sls service error log _ _ _ |   |   |   |   | /alidata/www/logs/ |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | /alidata/www/logs/ |   |   |
|   |   |   |   |   |   |   | java/sls- |   |   |   |
|   |   |   |   | g | sls service error log _ _ _ | service error log |   |   |   |   |
|   |   |   |   |   |   |   | service/applog/error |   |   |   |
|   |   |   |   |   |   |   | .log |   |   |   |
|   |   | sls service info log _ _ _ |   |   |   |   | /alidata/www/logs/ |   |   |   |
|   |   |   |   |   |   |   |   | /alidata/www/logs/ |   |   |
|   |   |   |   |   |   |   | java/sls- |   |   |   |
|   |   |   |   |   | sls service info log _ _ _ | service info log |   |   |   |   |
|   |   |   |   |   |   |   | service/applog/info. |   |   |   |
|   |   |   |   |   |   |   | log |   |   |   |
|   |   |   |   |   | sls shennongworker lo |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   | shennongworker lo | oot/sys/ShennongWork |   |   |   |
|   |   |   |   |   | _ _ g | _ |   |   |   |   |
|   |   |   |   |   |   |   | er/shennong worker.L _ |   |   |   |
|   |   | sls shennongworker lo |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | OG |   |   |   |
|   |   | _ _ g |   |   |   |   |   |   |   |   |
|   |   |   |   |   | sls shennongworker lo _ _ |   | /apsara/sls/sls Sh _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/sls Sh _ |   |   |
|   |   |   |   |   |   | shennongworker lo _ | ennongWorkerRole/she |   |   |   |
|   |   |   |   |   | g fuxiless _ | uxiless |   |   |   |   |
|   |   |   |   |   |   |   | nnong worker.LOG _ |   |   |   |
|   |   | trace log _ |   |   | trace log |   | /apsara/shennong a _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/shennong a _ |   |   |
|   |   |   |   |   |   | e log | gent/tracer/index wo _ |   |   |   |
|   |   |   |   |   |   |   |   |   | sls-backend- server.SlsShenn |   |
|   |   |   |   |   | _ | _ |   |   |   |   |
|   |   |   |   |   |   |   | rker trace.LOG _ |   |   |   |
|   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/tubo/TempR |   |   |
|   |   |   |   |   |   |   | oot/sys/ShennongWork |   |   |   |
|   |   |   |   |   | worker input log _ _ | ker input log |   |   |   |   |
|   |   |   |   |   |   |   | er/shennong worker i _ _ |   |   |   |
|   |   |   |   |   |   |   | nput.LOG |   |   |   |
|   |   | worker input log _ _ |   |   |   |   |   |   |   |   |
|   |   |   |   |   | worker input log fuxil |   | /apsara/sls/sls Sh _ |   |   |   |
|   |   |   |   |   |   |   |   | /apsara/sls/sls Sh _ |   |   |
|   |   |   |   |   |   | ker input log fuxil | ennongWorkerRole/she |   |   |   |
|   |   |   |   |   | _ _ _ ess | _ _ _ |   |   |   |   |
|   |   |   |   |   |   |   | nnong worker input.L _ _ |   |   |   |
|   |   |   |   |   |   |   | OG |   |   |   |
