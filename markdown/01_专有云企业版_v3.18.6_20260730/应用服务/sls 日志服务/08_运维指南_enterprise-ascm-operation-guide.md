---
title: "日志服务 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 23
source_pdf: "08_运维指南_enterprise-ascm-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sls/zh/enterprise-ascm-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 日志服务 运维指南

日志服务

## 运维方式

本文介绍日志服务的运维方式。 日志运维：日志服务依赖飞天基础运维平台进行部署，日志运维也主要通过飞天基础运维平台。日志运维有以下两种方式： Terminal：在飞天基础运维平台上通过机器Terminal快速登录到日志服务所在的机器，直接查看日志。 CLI：为满足越来越多的自动化日志服务配置需求，日志服务提供命令行工具CLI（Command Line Interface）。CLI工具提供管理Project、Logstore、机器组、消费组、Logtail配置、日志查询等操作。 运维大盘：日志服务提供运维大盘，可通过运维大盘对日志服务的Project、云账号等进行统一管理。
1. 登录Apsara Uni-manager运维控制台。
2. 登录飞天基础运维平台。
在Apsara Uni-manager运维控制台的顶部菜单栏，选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 进入产品集群运维。
i. 在左侧导航栏中，单击**产品集群运维**。 ii. 在**产品集群运维**页面，在**产品**|**集群**搜索框输入 `sls` 进行查询。 搜索结果中 `CdsSlsHybridCluster***` 即为日志服务所在集群。 iii. 在**操作**列，单击**集群详情**。
4. 在**集群详情**页面的**服务列表**页签中，单击目标组件（此处以sls-backend-server.ServiceTest#为例）
名称，并单击实例列表**操作**列的**Terminal**。
5. 登录机器Terminal，进入到对应的文件目录查看日志。
日志服务命令行工具CLI的主要功能包括： 支持大部分的日志服务REST接口。例如管理Project、Logstore、机器组、消费组和Logtail配置等。 支持多账号，便于跨地域操作日志。 支持基本查询和拉取日志。 支持Elasticsearch数据迁移。 日志服务支持灵活的时间配置。 支持高速跨域日志复制，历史数据重新索引与数仓投递。
1. 下载并安装日志服务CLI工具。
具体操作，请参见日志服务CLI。
2. 获取日志服务的Project名称、Endpoint和访问密钥（AccessKey）。
具体操作，请参见**《日志服务开发指南》**中的相关章节。
3. 使用日志服务CLI命令查询日志和维护日志服务。
具体操作，请参见日志服务CLI。

**运维大盘**

运维大盘的主要功能包括： Project管理查看全部的SLS Project信息，搜索Project查看该Project的地域、可用区、等信息、状态、资源配额等信息。 设置Project的可用性。 对Project的资源配额，如logstore上限、shard上限等进行设置。 具体操作，请参见Project管理。 账号管理对云账号的可用状态进行设置。 限制某账号可创建的Project数量。 具体操作，请参见账号管理。 日志服务

## 运维与诊断

### 通过机器Terminal查看日志

在飞天基础运维平台上，通过机器Terminal快速登录到日志服务所在的机器，直接查看日志。

**DBPostHandler#**

启动日志：/cloud/app/sls-backendserver/DBPostHandler#/db_post_handler/current/log/start.log 服务日志：无

**DBPreHandler#**

启动日志：/cloud/app/sls-backendserver/DBPreHandler#/db_pre_handler/current/log/start.log 服务日志：无

**InitSlsCluster#**

启动日志：/cloud/app/sls-backend-server/InitSlsCluster#/init_sls_cluster/current/log/start.log 服务日志：无

**ServiceTest#**

启动日志：/cloud/app/sls-backendserver/ServiceTest#/service_test_monitor/current/log/service_monitor.log 服务日志：无

**SlsAppProcessMonitor#**

启动日志： /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_common_worker_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_config_service_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_etl_framework_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_loghub_master_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_presto_worker_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_query_master_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_quota_server_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_replay_worker_monitor/current/log/start.log /cloud/app/sls-backendserver/SlsAppProcessMonitor#/sls_shennong_worker_monitor/current/log/start.log 服务日志：无

**SlsCommonWorkerDecider#**

启动日志：/cloud/app/sls-backend- 日志服务 server/SlsCommonWorkerDecider#/sls_common_worker_decider/current/log/start.log 服务日志：无

**SlsConfigManager#**

启动日志：/cloud/app/sls-backendserver/SlsConfigManager#/sls_config_manager/current/log/start.log 服务日志：无

**SlsConfigServiceDecider#**

启动日志：/cloud/app/sls-backendserver/SlsConfigServiceDecider#/sls_config_service_decider/current/log/start.log 服务日志：无

**SlsDeployFuxiless#**

启动日志：/cloud/app/sls-backendserver/SlsDeployFuxiless#/sls_deploy_fuxiless/current/log/start.log 服务日志：无

**SlsEtlFrameworkDecider#**

启动日志：/cloud/app/sls-backendserver/SlsEtlFrameworkDecider#/sls_etl_framework_decider/current/log/start.log 服务日志：无

**SlsImportOdpsScheduler#**

启动日志：/cloud/app/sls-backendserver/SlsImportOdpsScheduler#/sls_import_odps_scheduler/current/log/start.log 服务日志：无

**SlsLoghubMasterDecider#**

启动日志：/cloud/app/sls-backendserver/SlsLoghubMasterDecider#/sls_loghub_master_decider/current/log/start.log 服务日志：无

**SlsPrometheus#**

启动日志：/cloud/app/sls-backendserver/SlsPrometheus#/sls_prometheus/current/log/start.log 服务日志：无

**SlsQueryMasterDecider#**

启动日志：/cloud/app/sls-backendserver/SlsQueryMasterDecider#/sls_query_master_decider/current/log/start.log 服务日志：无

**SlsQuotaServerDecider#**

启动日志：/cloud/app/sls-backendserver/SlsQuotaServerDecider#/sls_quota_server_decider/current/log/start.log 服务日志：无

**SlsReplayWorkerDecider#**

启动日志：/cloud/app/sls-backend- 日志服务 server/SlsReplayWorkerDecider#/sls_replay_worker_decider/current/log/start.log 服务日志：无

**SlsReplayWorkerDecider#**

启动日志：/cloud/app/sls-backendserver/SlsReplayWorkerDecider#/sls_replay_worker_decider/current/log/start.log 服务日志：无

**SlsShennongWorkerDecider#**

启动日志：/cloud/app/sls-backendserver/SlsShennongWorkerDecider#/sls_shennong_worker_decider/current/log/start.log 服务日志：无

**ToolService#**

启动日志： /cloud/app/sls-backendserver/ToolService#/init_diamond/current/log/diamond_publish_content.LOG /cloud/app/sls-backend-server/ToolService#/init_diamond/current/log/start.log /cloud/app/sls-backend-server/ToolService#/init_odps/current/log/start.log /cloud/app/sls-backend-server/ToolService#/init_pop/current/log/start.log /cloud/app/sls-backend-server/ToolService#/jdk_uploader/current/log/start.log 服务日志：无

### 通过CLI工具维护日志服务

为满足越来越多的自动化日志服务配置需求，日志服务提供命令行工具CLI（Command Line Interface）。CLI工具提供管理Project、Logstore、机器组、消费组、Logtail配置、日志查询等操作。 日志服务命令行工具CLI的主要功能包括： 支持大部分的日志服务REST接口。例如管理Project、Logstore、机器组、消费组和Logtail配置等。 支持多账号，便于跨地域操作日志。 支持基本查询和拉取日志。 支持Elasticsearch数据迁移。 支持灵活的时间配置。 支持高速跨域日志复制，历史数据重新索引与数仓投递。
1. 下载并安装日志服务CLI工具。
具体操作，请参见日志服务CLI。
2. 获取日志服务的Project名称、Endpoint和访问密钥（AccessKey）。
具体操作，请参见**日志服务开发指南**中的**获取****AccessKey**和**获取日志服务的****Endpoint**章节。
3. 使用日志服务CLI命令查询日志和维护日志服务。
具体操作，请参见日志服务CLI。

### 通过CDS-智能运维查询日志

日志服务系统对关键性服务的日志进行了统一存储和索引，您可以根据服务类型、项目、存储服务等维度查询指定时间范围内的日志信息。

**背景信息**

日志并非永久保存，系统会定期自动清理日志。不同服务日志的保存时长不同，日志保存时长由日志数据量以及日志重要程度决定，但是阿里云云产品日志的最长保存时间不超过30天。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏，选择**产品运维** > **存储运维** **> CDS****运维****·CDS-OPS**。
3. 在左侧导航栏，选择**CDS-****智能运维** > **日志查询**。
4. 在**日志查询**页面，选择类型、项目、存储和日期，并配置查询条件。
查询条件由查询语句和分析语句构成，格式为查询语句|分析语句，例如 * | SELECT status, `count(*) AS PV GROUP BY status` 。查询语句和分析语句以竖线（|）分割，查询语句的语法为日志服务专有语法。 查询语句可单独使用，分析语句必须与查询语句一起使用，即分析功能是基于查询结果或全量数据进行的。更多信息，请参见《**CDS****用户指南》**中“日志服务”节点下的“查询与分析”章节。

| 语句类型 | 说明 |
|---|---|
| 查询语句 | 查询语句用于指定日志查询时的过滤规则，返回符合条件的日志。查询语句可以为关键词、数值、数值范围、空格、星号（*）等。 如果为空格或星号（*），表示无过滤条件。 |
| 分析语句 | 分析语句用于对查询结果或全量数据进行计算和统计。 |

5. 单击**查询**。
系统显示符合条件的日志数据。

**说明**

不同类型的日志格式不同，请以实际为准。

**支持查询日志服务哪些类型的日志**

支持查询**日志服务**中以下Logstore的详细日志。这些日志为日志服务自身各服务初始化后生成的日志。

| Logstore |  | config name _ |  | log path |  | server role |
|---|---|---|---|---|---|---|
| action trail _ |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  | /apsara/sls/sls Sl _ |  |
|  |  |  |  | sMetaServiceRole/Act |  |  |
|  |  |  |  |  |  | sls-backend- |
|  | trail | 无 |  |  |  |  |
|  |  |  |  | ionTrailOplog.LOG |  |  |

日志服务

|  |  | alert-metering |  |  |  | /apsara/sls/sls Et _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | /apsara/sls/sls Et _ |  |  |
|  |  |  |  |  |  | lFrameworkPartitionR |  |  |  |
|  |  |  |  |  |  |  |  | sls-backend- server.SlsEtlFramewor |  |
|  |  |  | etering | 无 |  |  |  | s |  |
|  |  |  |  |  |  | ole/alert metering.L _ |  | k |  |
|  |  |  |  |  |  | OG |  |  |  |
|  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | oot/sys/DispatchWork |  |  |  |
|  |  |  |  | dispatch worker log _ _ | atch worker log |  |  |  |  |
|  |  |  |  |  |  | er/*dispatch worker. _ |  |  |  |
|  |  |  |  |  |  | LOG |  |  |  |
|  |  | dispatch worker log _ _ |  |  |  |  |  |  |  |
|  |  |  |  | dispatch worker log f |  | /apsara/sls/sls Di _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Di _ |  |  |
|  |  |  |  |  | atch worker log f | spatchWorkerPartitio |  |  |  |
|  |  |  |  | _ _ _ uxiless | _ _ _ |  |  |  |  |
|  |  |  |  |  |  | nRole/*dispatch work _ |  |  |  |
|  |  |  |  |  |  | er.LOG |  |  |  |
|  |  | etl alert log _ _ |  |  |  | /apsara/sls/sls Et _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Et _ | sls-backend- |  |
|  |  |  |  |  |  | lFrameworkPartitionR |  |  |  |
|  |  |  |  |  |  |  |  | server.SlsEtlFramew k |  |
|  |  |  | rt log _ | etl alert log _ _ | alert log |  |  |  |  |
|  |  |  |  |  |  | ole/etl worker.LOG _ |  |  |  |
|  |  |  |  | etl framework log fuxi |  | /apsara/sls/sls Et _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Et _ |  |  |
|  |  |  |  |  | framework log fuxi | lFrameworkPartitionR |  |  |  |
|  |  |  |  | _ _ _ less | _ _ |  |  |  |  |
|  |  |  |  |  |  | ole/etl worker.LOG _ |  |  |  |
|  |  | etl framework log _ _ |  |  |  |  |  |  |  |
|  |  |  |  | etl framework log |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  | framework log | oot/sys/EtlFramework |  |  |  |
|  |  |  |  | _ _ | _ |  |  |  |  |
|  |  |  |  |  |  | /etl worker.LOG _ |  |  |  |
|  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | oot/sys/EtlFramework |  |  |  |
|  |  |  |  |  |  | /etl golang worker.L _ _ |  |  |  |
|  |  |  |  | etl golang worker log _ _ _ |  | OG |  |  |  |
|  |  | etl golang worker log _ _ _ |  |  |  |  |  |  |  |
|  |  |  |  | etl golang worker log |  | /apsara/sls/sls Et _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Et _ | server.SlsEtlFramewor |  |
|  |  |  |  |  | golang worker log | lFrameworkPartitionR |  |  |  |
|  |  |  |  |  |  |  |  | k# |  |
|  |  |  |  | _ _ _ fuxiless _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | ole/etl golang worke _ _ |  |  |  |
|  |  |  |  |  |  | r.LOG |  |  |  |

日志服务

|  |  |  |  | oss shipper metering |  | /apsara/sls/sls Sh _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | /apsara/sls/sls Sh _ |  |  |
|  |  |  |  |  | shipper metering | ennongReplayWorkerRo |  |  |  |
|  |  |  |  | _ _ _ log fuxiless _ | _ _ _ |  |  |  |  |
|  |  |  |  |  |  | le/oss shipper meter _ _ |  |  |  |
|  |  |  |  |  |  | ing.LOG |  |  |  |
|  |  |  |  | odps shipper meterin |  | /apsara/sls/import |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/import |  |  |
|  |  |  |  |  | s shipper meterin | odps/scheduler/odps _ |  |  |  |
|  |  |  |  | _ _ g log _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | shipper metering.lo _ _ |  |  |  |
|  |  |  |  |  |  | g |  |  |  |
|  |  | etl metering _ |  |  |  |  |  |  |  |
|  |  |  |  | export metering log |  | /usr/local/export/ |  |  |  |
|  |  |  |  |  |  |  | /usr/local/export/ | server.SlsShennongW |  |
|  |  |  |  |  | ort metering log | export * metering.lo _ _ |  |  |  |
|  |  |  |  | _ _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | g |  |  |  |
|  |  |  |  | python etl metering _ _ |  | /usr/local/python- etl/metering.log |  |  |  |
|  |  |  |  | oss shipper metering |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  | shipper metering | oot/sys/ShennongRepl |  |  |  |
|  |  |  |  | _ _ _ log | _ _ _ |  |  |  |  |
|  |  |  |  |  |  | ayWorker/oss shipper _ |  |  |  |
|  |  |  |  |  |  | metering.LOG _ |  |  |  |
|  |  | export-service-metrics |  | redis op log |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  | is op log | sExportServiceRole/r |  |  |  |
|  |  |  |  |  |  |  |  | server.SlsExportS |  |
|  |  |  |  | _ _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | edis worker.log _ |  |  |  |
|  |  | export service log _ _ |  | redis op log |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  | is op log | sExportServiceRole/r |  |  |  |
|  |  |  |  | _ _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | edis worker.log _ |  |  |  |
|  |  |  |  | export service worker |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  | ort service worker | sExportServiceRole/e |  |  |  |
|  |  |  |  |  |  |  |  | sls-backend- server.SlsExportServic |  |
|  |  |  | service log _ _ | _ _ log _ | _ _ |  |  | serv |  |
|  |  |  |  |  |  | xport service worker _ _ |  | e# |  |
|  |  |  |  |  |  | .log |  |  |  |
| 1 |  |  |  |  |  |  |  |  |  |
|  |  |  |  | export service log |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  | ort service log | sExportServiceRole/E |  |  |  |
|  |  |  |  | _ _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | xportService.LOG |  |  |  |
|  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | oot/sys/FcTriggerWor |  |  |  |
|  |  |  |  |  |  |  |  | 无 |  |
|  |  |  |  | fc trigger log _ _ | rigger log |  |  |  |  |
|  |  |  |  |  |  | ker/fc trigger.log _ |  |  |  |
|  |  | fc trigger log _ _ |  |  |  |  |  |  |  |
|  |  | 2 |  |  |  |  |  |  |  |

|  |  | /usr/local/python- |  |
|---|---|---|---|
| hon etl metering _ _ | etl/metering.log |  |  |

|  | 日志服务 |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | fc trigger log fuxiless |  |  | /apsara/sls/sls Fc _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Fc _ |  |  |
|  |  |  |  |  |  | rigger log fuxiless |  | TriggerWorkerRole/fc |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 无 |  |
|  |  |  |  |  | _ _ _ | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | trigger.log _ |  |  |  |
|  | forwarder-grpc |  |  |  |  |  |  | /cloud/app/sls- |  |  |  |
|  |  |  |  |  |  |  |  |  | /cloud/app/sls- |  |  |
|  |  |  |  |  |  |  |  | backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsForwarderP |  |  |  |
|  |  | orwarder-grpc |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | forwarder-grpc |  |  | rometheus#/sls forwa _ |  | 无 |  |
|  |  |  |  |  |  |  |  | rder prometheus/curr _ |  |  |  |
|  |  |  |  |  |  |  |  | ent/forwarder- |  |  |  |
|  |  |  |  |  |  |  |  | grpc.json |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |
|  |  |  |  |  |  |  |  | sls-backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsForwarderK |  |  |  |
|  |  |  |  |  |  |  |  | afka#/sls forwarder _ _ |  |  |  |
|  |  |  |  |  | forwarder-kafka-error |  |  |  |  | 无 |  |
|  |  |  |  |  |  |  |  | kafka/current/sls fo _ |  |  |  |
|  |  |  |  |  |  |  |  | rwarder kafka releas _ _ |  |  |  |
|  |  |  |  |  |  |  |  | e 64/kafka/logs/erro _ |  |  |  |
|  |  |  |  |  |  |  |  | r.log |  |  |  |
|  | forwarder-kafka |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |
|  |  |  |  |  |  |  |  | sls-backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsForwarderK |  |  |  |
|  |  |  |  |  | forwarder-kafka- |  |  | afka#/sls forwarder _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 无 |  |
|  |  |  |  |  | access |  |  | kafka/current/sls fo _ |  |  |  |
|  |  |  |  |  |  |  |  | rwarder kafka releas _ _ |  |  |  |
|  |  |  |  |  |  |  |  | e 64/kafka/logs/acce _ |  |  |  |
|  |  |  |  |  |  |  |  | ss.log |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |
|  |  |  |  |  |  |  |  | sls-backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsForwarderS |  |  |  |
|  |  |  |  |  |  |  |  | yslog#/sls forwarder _ |  | sls-backend- |  |
|  | forwarder-syslog |  |  |  | forwarder-syslog |  |  |  |  | server.SlsForwarderSy |  |
|  |  |  |  |  |  |  |  | syslog/current/sls _ _ |  | slog# |  |
|  |  |  |  |  |  |  |  | forwarder syslog rel _ _ |  |  |  |
|  |  |  |  |  |  |  |  | ease 64/syslog- _ |  |  |  |
|  |  |  |  |  |  |  |  | forwarder.json |  |  |  |
|  | kms sql log _ _ |  |  |  | kms sql log _ _ |  |  | /apsara/tubo/TempRoo t/sys/SlsKmsWrapperS ervice/kms sql.LOG _ |  | sls-backend- server.SlsKmsWrapper Service# |  |
|  |  |  |  |  | kms sql log fuxiless _ _ _ |  |  | /apsara/sls/sls KmsWr _ apperServiceWorker/k ms sql.LOG _ |  |  |  |

日志服务

|  |  |  |  |  | kms worker log fuxile |  | /apsara/sls/sls Km _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | /apsara/sls/sls Km _ |  |  |
|  |  |  |  |  |  | s worker log fuxile | sWrapperServiceWorke |  |  |  |
|  |  |  |  |  | _ _ _ ss | _ _ _ |  |  |  |  |
|  |  |  |  |  |  |  | r/sls kms wrapper se _ _ _ |  |  |  |
|  |  |  |  |  |  |  | rvice worker.LOG _ |  |  |  |
|  |  | kms worker log _ _ |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/tubo/TempR | Service# |  |
|  |  |  |  |  |  |  | oot/sys/SlsKmsWrappe |  |  |  |
|  |  |  |  |  | kms worker log |  |  |  |  |  |
|  |  |  |  |  |  |  | rService/sls kms wra _ _ |  |  |  |
|  |  |  |  |  | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  | pper service worker. _ _ |  |  |  |
|  |  |  |  |  |  |  | LOG |  |  |  |
|  |  | logtail alarm _ |  |  | 无 |  | 无 |  | sls-backend- server.SlsLogtail# |  |
|  |  | logtail status profile _ _ |  |  | 无 |  | 无 |  |  |  |
|  |  | logtail suicide profile _ _ |  |  | 无 |  | 无 |  |  |  |
|  |  | metering |  |  | metering |  | /apsara/sls/meteri ng.log |  | sls-backend- server.SlsMeteringSer vice# |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  |  |  | sMirrorsls-backend- |  |  |  |
|  |  |  |  |  |  |  | server.SlsMirrorServ |  | sls-backend- server.SlsMirrorServic |  |
|  |  | mirror service _ |  | ervice | mirror service |  |  |  | server.SlsMirrorServic |  |
|  |  |  |  |  | _ |  | ice#ServiceRole/mirr |  | e# |  |
|  |  |  |  |  |  |  | or service worker.LO _ _ |  |  |  |
|  |  |  |  |  |  |  | G |  |  |  |
|  |  | nginx error log _ _ |  |  | nginx error log _ _ |  | /apsara/sls/nginx/ logs/error.log |  | sls-backend- server.Nginx# |  |
|  |  | offline scheduler log _ _ |  |  | offline scheduler log |  | /apsara/sls/import |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/import |  |  |
|  |  |  |  |  |  | ne scheduler log | odps/scheduler/impo _ |  |  |  |
|  |  |  |  |  |  |  |  |  | 无 |  |
|  |  |  | _ _ |  | _ _ | _ _ |  |  |  |  |
|  |  |  |  |  |  |  | rt odps*.log _ |  |  |  |
|  |  | pk-query |  |  | pk-query |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | query | oot/sys/ShennongWork |  |  |  |
|  |  |  |  |  |  |  | er/pk query.LOG _ |  |  |  |
|  |  |  |  |  | pk-query fuxiless |  | /apsara/sls/sls Sh _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Sh _ | server.SlsShennongW orker# |  |
|  |  |  |  |  |  | query fuxiless | ennongWorkerRole/pk _ |  |  |  |
|  |  |  |  |  | _ | _ |  |  |  |  |
|  |  |  |  |  |  |  | query.LOG |  |  |  |

|  |  | /apsara/sls/meteri | sls-ba serve |
|---|---|---|---|
| ering | ng.log |  |  |

|  |  | /apsara/sls/nginx/ | sls-backend- |
|---|---|---|---|
| nx error log _ _ | logs/error.log |  |  |

日志服务

|  | presto gc log _ _ |  |  | presto gc log |  |  | /apsara/presto/pre |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | /apsara/presto/pre |  |  |
|  |  |  |  |  | sto gc log |  | sto data/var/log/gc. _ |  |  |  |
|  |  |  | _ _ | _ _ | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  | log* |  |  |  |
|  | presto http _ |  |  | presto http |  |  | /apsara/presto/pre |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/presto/pre |  |  |
|  |  |  |  |  | sto http |  | sto data/var/log/htt _ |  |  |  |
|  |  |  | _ | _ | _ |  |  |  |  |  |
|  |  |  |  |  |  |  | p-request.log |  |  |  |
|  | presto metering _ |  |  | presto metering |  |  | /apsara/presto/pre |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/presto/pre |  |  |
|  |  |  |  |  | sto metering |  | sto data/var/log/met _ |  |  |  |
|  |  |  | _ | _ | _ |  |  |  |  |  |
|  |  |  |  |  |  |  | ering.log |  |  |  |
|  | presto monitor _ |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  |  | oot/sys/PrestoWorker |  |  |  |
|  |  |  | monitor _ | presto monitor _ | sto monitor |  |  |  |  |  |
|  |  |  |  |  |  |  | /presto monitor.LOG _ |  |  |  |
|  | presto server _ |  |  | presto server |  |  | /apsara/presto/pre |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/presto/pre | r# |  |
|  |  |  |  |  | sto server |  | sto data/var/log/ser _ |  |  |  |
|  |  |  |  | _ | _ |  |  |  |  |  |
|  |  |  |  |  |  |  | ver.log |  |  |  |
|  |  |  |  | presto server fuxiless |  |  | /apsara/sls/presto |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/presto |  |  |
|  |  |  |  |  | sto server fuxiless |  | /presto data/var/log _ |  |  |  |
|  |  |  |  | _ _ | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  | /server.log |  |  |  |
|  | presto sql server _ _ |  |  | presto sql server _ _ |  |  | /apsara/presto/sls sql _ _ server.LOG |  |  |  |
|  | presto worker _ |  |  | presto worker _ |  |  | /apsara/tubo/TempRoo t/sys/PrestoWorker/pre sto worker.LOG _ |  |  |  |
|  |  |  |  | presto worker fuxiless _ _ |  |  | /apsara/sls/sls Presto _ WorkerRole/presto wo _ rker.LOG |  |  |  |
|  | prometheus-backend- |  |  |  |  |  | /cloud/app/sls- |  |  |  |
|  |  |  |  |  |  |  |  | /cloud/app/sls- |  |  |
|  |  |  |  |  |  |  | backend- |  |  |  |
|  |  |  |  |  |  |  | server/SlsPrometheus |  |  |  |
|  |  | rometheus-backend- |  | prometheus-backend- |  |  |  |  |  |  |
|  |  |  |  |  |  |  | #/sls prometheus/cur _ |  |  |  |
|  | log | og |  | log |  |  |  |  |  |  |
|  |  |  |  |  |  |  | rent/aos sls prometh _ _ |  |  |  |
|  |  |  |  |  |  |  | eus release 64/sls p _ _ _ |  |  |  |
|  |  |  |  |  |  |  | rometheus.LOG* |  |  |  |

#

|  |  |  |  |  |  |  |  |  |  | 日志服务 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | prometheus-log |  |  |  |  |  |  | /cloud/app/sls- |  |  |  |
|  |  |  |  |  |  |  |  |  | /cloud/app/sls- |  |  |
|  |  |  |  |  |  |  |  | backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsPrometheus |  |  |  |
|  |  | rometheus-log |  |  | prometheus-log |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | #/sls prometheus/cur _ |  |  |  |
|  |  |  |  |  |  |  |  | rent/prometheus*.LOG |  |  |  |
|  | query master log _ _ |  |  |  | query master log |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | ry master log |  | oot/sys/QueryMaster/ |  |  |  |
|  |  |  |  |  | _ _ | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | query master.LOG* _ |  |  |  |
|  |  |  |  |  | query master log fuxil _ _ _ |  |  | /apsara/sls/sls Qu _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Qu _ | # |  |
|  |  |  |  |  |  | ry master log fuxil _ _ _ |  | eryMasterRole/query _ |  |  |  |
|  |  |  |  |  | ess |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | master.LOG* |  |  |  |
|  | query master meterin _ _ g log _ |  |  |  | query master meterin |  |  | /apsara/sls/sls Qu _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Qu _ |  |  |
|  |  |  |  |  |  | ry master meterin |  | eryMasterRole/query _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | sls-backend- server.SlsQueryMaster |  |
|  |  |  | _ |  | _ _ g log _ | _ _ |  |  |  | s |  |
|  |  |  |  |  |  |  |  | master metering *.LO _ _ |  | # |  |
|  |  |  |  |  |  |  |  | G* |  |  |  |
|  | redis sentinel _ |  |  |  | redis sentinel log _ _ |  |  | /var/log/redis/sen tinel.log |  | sls-backend- server.RedisServer# |  |
|  | redis server _ |  |  |  | redis server log _ _ |  |  | /var/log/redis/red is.log |  | sls-backend- server.RedisServer# |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  |  |  |  | sMirrorServiceRole/m |  |  |  |
|  |  |  |  |  |  |  |  | irror service schedu _ _ |  | sls-ba serve |  |
|  | replication status _ |  | tion status |  | replication status |  |  |  |  |  |  |
|  |  |  |  |  | _ |  |  | le.LOG |  |  |  |
|  | schedule sql metering _ _ |  |  |  | scheduled sql meterin |  |  | /apsara/sls/sls Et _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Et _ |  |  |
|  |  |  |  |  |  | eduled sql meterin |  | lFrameworkPartitionR |  |  |  |
|  |  |  |  |  |  |  |  |  |  | sls-backend- server.SlsEtlFramewor |  |
|  |  |  | le sql metering _ _ |  | _ _ g | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | ole/etl metering.LOG _ |  |  |  |
|  | scm server _ |  |  |  | scm server |  |  | /apsara/sls/scm se _ |  | sls-backend- server.SlsScmServer# |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/scm se _ |  |  |
|  |  |  |  |  |  | server |  | rver/scm server.LOG _ |  |  |  |
|  |  |  |  |  | _ | _ |  |  |  |  |  |

|  |  | /var/log/redis/sen | sls-backe |
|---|---|---|---|
| is sentinel log _ _ | tinel.log |  |  |

|  |  | /var/log/redis/red | sls-ba |
|---|---|---|---|
| is server log _ _ | is.log |  |  |

日志服务

|  |  | scm server oplog _ _ |  | scm server oplog |  | /apsara/sls/scm se _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | /apsara/sls/scm se _ | sls-backend- |  |
|  |  |  |  |  | server oplog | rver/scm operation.L _ |  | s |  |
|  |  |  |  |  |  |  |  | s |  |
|  |  |  | _ | _ _ | _ _ |  |  |  |  |
|  |  |  |  |  |  | OG |  |  |  |
|  |  | scmc access log _ _ |  | scmc access log |  | /apsara/sls/nginx/ |  | sls-backend- server.SlsScmc# |  |
|  |  |  |  |  |  |  | /apsara/sls/nginx/ |  |  |
|  |  |  |  |  | c access log | logs/scmc access.log _ |  |  |  |
|  |  |  | _ | _ _ | _ _ |  |  |  |  |
|  |  | scmc err log _ _ |  | scmc err log _ _ |  | /apsara/sls/nginx/ logs/scmc err log _ _ |  |  |  |
|  |  | scmc op log _ _ |  | scmc op log _ _ |  | /apsara/sls/nginx/ logs/scmc op log _ _ |  |  |  |
|  |  | shennong log profile _ _ |  | 无 |  | 无 |  | sls-backend- server.SlsShennongW orker# |  |
|  |  | sls config service cac _ _ _ he |  | sls config service cac |  | /apsara/sls/sls Co _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Co _ | sls-backend- |  |
|  |  |  |  |  | config service cac | nfigServiceRole/conf |  | sls-backend- |  |
|  |  |  |  |  |  |  |  | server.SlsConfigServic |  |
|  |  |  | _ _ | _ _ _ he | _ _ |  |  |  |  |
|  |  |  |  |  |  | ig service cache.LOG _ _ |  |  |  |
|  |  | sls configservice log _ _ |  | sls configservice log |  | /apsara/sls Config _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls Config _ |  |  |
|  |  |  |  |  | configservice log | ServiceRole/sls conf _ |  |  |  |
|  |  |  |  | _ _ | _ |  |  |  |  |
|  |  |  |  |  |  | ig service.LOG _ |  |  |  |
|  |  |  |  | sls configservice log f |  | /apsara/sls/sls Co _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Co _ |  |  |
|  |  |  |  |  | configservice log f | nfigServiceRole/sls _ |  |  |  |
|  |  |  |  | _ _ _ uxiless | _ _ |  |  |  |  |
|  |  |  |  |  |  | config service.LOG _ |  |  |  |
|  |  |  |  | sls configservice quer |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR | sls-backend- server.SlsConfigServic |  |
|  |  |  |  |  | configservice quer | oot/sys/*ConfigServi |  |  |  |
|  |  |  |  |  |  |  |  | e# |  |
|  |  |  |  | _ _ y log |  |  |  |  |  |
|  |  |  |  |  |  | ce/config service qu _ _ |  |  |  |
|  |  |  |  | _ |  |  |  |  |  |
|  |  |  |  |  |  | ery.LOG |  |  |  |
|  |  | sls configservice quer _ _ y log _ |  |  |  |  |  |  |  |
|  |  |  |  | sls configservice quer |  | /apsara/sls/sls Co _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/sls/sls Co _ |  |  |
|  |  |  |  |  | configservice quer | nfigServiceRole/conf |  |  |  |
|  |  |  |  | _ _ y log fuxiless _ _ | _ |  |  |  |  |
|  |  |  |  |  |  | ig service query.LOG _ _ |  |  |  |

|  |  | /apsara/sls/nginx/ | sls-backend- server.SlsScmc# |
|---|---|---|---|
| c err log _ _ | logs/scmc err log _ _ |  |  |

|  |  | /apsara/sls/nginx/ |  |
|---|---|---|---|
| c op log _ _ | logs/scmc op log _ _ |  |  |

日志服务

|  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |
|  |  |  |  |  |  |  |  | sls-backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsConsole#/s |  |  |  |
|  | sls console error log _ _ _ |  |  | r log | sls console error log |  |  |  |  |  |  |
|  |  |  |  |  | _ _ _ |  |  | ls console/current/s _ |  |  |  |
|  |  |  |  |  |  |  |  | ls console/logs/erro _ |  |  |  |
|  |  |  |  |  |  |  |  | r.log |  |  |  |
|  | sls console info log _ _ _ |  |  |  |  |  |  | /cloud/app/sls- |  |  |  |
|  |  |  |  |  |  |  |  |  | /cloud/app/sls- |  |  |
|  |  |  |  |  |  |  |  | backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsConsole#/s |  |  |  |
|  |  | ls console info log _ _ _ |  |  | sls console info log |  |  |  |  |  |  |
|  |  |  |  |  | _ _ _ |  |  | ls console/current/s _ |  |  |  |
|  |  |  |  |  |  |  |  | ls console/logs/info _ |  |  |  |
|  |  |  |  |  |  |  |  | .log |  |  |  |
|  | sls consumergroup lo _ _ g |  |  |  | sls consumergroup lo _ _ |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | consumergroup lo _ |  | oot/sys/QuotaServer/ |  |  |  |
|  |  |  |  |  | g |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | monitor.LOG |  |  |  |
|  |  |  |  |  | sls consumergroup lo _ _ |  |  | /apsara/sls/sls Qu _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Qu _ |  |  |
|  |  |  |  |  |  | consumergroup lo _ |  | otaServerRole/monito |  |  |  |
|  |  |  |  |  | g fuxiless _ | uxiless |  |  |  |  |  |
|  |  |  |  |  |  |  |  | r.LOG |  |  |  |
|  | sls etl20 coordinator l _ _ _ og |  |  |  | sls etl20 coordinator l _ _ _ |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  |  | etl20 coordinator l _ _ |  | sEtl20CoordinatorRol |  |  |  |
|  |  |  |  |  |  |  |  |  |  | server.SlsEtl20C |  |
|  |  |  |  |  | og |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | e/SlsEtl20.LOG* |  |  |  |
|  | sls etl20 job checker l _ _ _ _ og |  |  |  | sls etl20 job checker _ _ _ _ |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  |  | etl20 job checker _ _ _ |  | sEtl20JobCheckerRole |  |  |  |
|  |  |  |  |  |  |  |  |  |  | server.SlsEtl20J kerRole# |  |
|  |  |  |  |  | log |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | /SlsEtl20.LOG* |  |  |  |
|  | sls etl20 sts proxy log _ _ _ _ |  |  |  | sls etl20 sts proxy lo _ _ _ _ |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  |  | etl20 sts proxy lo _ _ _ |  | sEtl20StsProxyRole/S |  |  |  |
|  |  |  |  |  |  |  |  |  |  | server.SlsEtl2 |  |
|  |  |  | _ _ _ |  | g |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | lsEtl20.LOG* |  |  |  |
|  | sls etl20 worker grou _ _ _ pb log _ |  |  |  | sls etl20 worker grou _ _ _ |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  |  | etl20 worker grou _ _ |  | sEtl20WorkerGroupBRo |  |  |  |
|  |  |  |  |  |  |  |  |  |  | server.SlsEtl20Wo |  |
|  |  |  |  |  | pb log _ | log |  |  |  |  |  |
|  |  |  |  |  |  |  |  | le/SlsEtl20.LOG* |  |  |  |
|  | sls etl20 worker log _ _ _ |  |  |  | sls etl20 worker log |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  |  | etl20 worker log |  | sEtl20WorkerRole/Sls |  |  |  |
|  |  |  |  |  |  |  |  |  |  | server.SlsE |  |
|  |  |  | _ _ |  | _ _ _ | _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Etl20.LOG* |  |  |  |

日志服务

|  |  |  | sls etl connector metr _ _ _ ics |  |  |  | /apsara/sls/sls Sl _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  |  |  | sEtl20WorkerGroupFux |  |  |  |
|  |  |  |  |  |  |  |  |  | sls-backend- server.SlsEtl20Worker |  |
|  |  |  |  | _ | etl-connector-metrics | connector-metrics |  |  | se |  |
|  |  |  |  |  |  |  | ilessRole/connector. |  | Gr |  |
|  |  |  |  |  |  |  | log |  |  |  |
|  |  |  | sls etl log _ _ |  | sls-etl20-fuxiless- |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  |  | etl20-fuxiless- | sEtl20WorkerGroupFux |  |  |  |
|  |  |  |  |  |  |  |  |  | sls-backend- server.SlsEtl20Work |  |
|  |  |  |  | log | log worker-log _ |  |  |  |  |  |
|  |  |  |  |  |  |  | ilessRole/work.log |  |  |  |
|  |  |  | sls fastcgi log _ _ |  | sls fastcgi log |  | /apsara/sls/fcgi a _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/fcgi a _ | sls-backend- |  |
|  |  |  |  |  |  | fastcgi log | gent/FastcgiAgent*.L |  | s |  |
|  |  |  |  |  |  |  |  |  | s |  |
|  |  |  |  | _ | _ _ | _ |  |  |  |  |
|  |  |  |  |  |  |  | OG |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  |  | oot/sys/ShennongWork |  |  |  |
|  |  |  |  |  | sls index status log |  |  |  |  |  |
|  |  |  |  |  |  |  | er/project index siz _ _ |  |  |  |
|  |  |  |  |  | _ _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  | e.LOG |  |  |  |
|  |  |  | sls index status log _ _ _ |  |  |  |  |  |  |  |
|  |  |  |  |  | sls index status log f |  | /apsara/sls/sls Sh _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Sh _ |  |  |
|  |  |  |  |  |  | index status log f | ennongWorkerRole/pro |  |  |  |
|  |  |  |  |  | _ _ _ _ uxiless | _ _ _ |  |  |  |  |
|  |  |  |  |  |  |  | ject index size.LOG _ _ |  |  |  |
|  |  |  |  |  | sls loghub shard statu |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | loghub shard statu | oot/sys/LoghubMaster |  |  |  |
|  |  |  |  |  | _ _ _ s log _ | _ _ |  |  |  |  |
|  |  |  |  |  |  |  | /loghub master meta. _ _ |  |  |  |
|  |  |  | sls loghub shard statu |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | LOG |  |  |  |
|  |  |  | _ _ _ s log _ |  |  |  |  |  |  |  |
|  |  |  |  |  | sls loghub shard statu _ _ _ |  | /apsara/sls/sls Lo _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Lo _ |  |  |
|  |  |  |  |  |  | loghub shard statu _ _ | ghubMasterRole/loghu |  |  |  |
|  |  |  |  |  | s log fuxiless _ _ | g fuxiless |  |  |  |  |
|  |  |  |  |  |  |  | b master meta.LOG _ _ |  |  |  |
|  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/tubo/TempR | server.SlsLoghubMast |  |
|  |  |  |  |  |  |  | oot/sys/LoghubMaster |  | er# |  |
|  |  |  |  |  | sls loghubmaster log _ _ | loghubmaster log |  |  |  |  |
|  |  |  |  |  |  |  | /sls loghub master.L _ _ |  |  |  |
|  |  |  |  |  |  |  | OG |  |  |  |
|  |  |  | sls loghubmaster log _ _ |  |  |  |  |  |  |  |
|  |  |  |  |  | sls loghubmaster log _ _ _ |  | /apsara/sls/sls Lo _ |  |  |  |
|  |  |  |  |  |  |  |  | /apsara/sls/sls Lo _ |  |  |
|  |  |  |  |  |  | loghubmaster log _ _ | ghubMasterRole/sls l _ |  |  |  |
|  |  |  |  |  | fuxiless | less |  |  |  |  |
|  |  |  |  |  |  |  | oghub master.LOG _ |  |  |  |

日志服务

| sls meta service _ _ |  |  |  |  | sls meta service |  |  | /apsara/sls/sls Sl _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  |  | meta service |  | sMetaServiceRole/Met |  |  |  |
|  |  | _ |  |  | _ _ | _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | aService.LOG |  |  |  |
| sls meta service oplo _ _ _ g |  |  |  |  | sls meta service oplo _ _ _ |  |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ |  |  |
|  |  |  |  |  |  | meta service oplo _ _ |  | sMetaServiceRole/Met |  |  |  |
|  |  |  |  |  | g |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | aServiceOplog.LOG |  |  |  |
| sls metering oms dat _ _ _ a |  |  |  |  |  |  |  | /apsara/sls SlsMet _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls SlsMet _ |  |  |
|  |  |  |  |  |  |  |  | eringServiceRole/oms |  |  |  |
|  |  |  |  |  |  |  |  |  |  | sls- |  |
|  |  | tering oms dat _ _ |  |  | oms |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | .log |  |  |  |
| sls metering service l _ _ _ og |  |  |  |  | sls metering service l _ _ _ |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  | metering service l _ _ |  | oot/sys/SlsMeteringS |  |  |  |
|  |  |  |  |  | og |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | ervice/stdout.out |  |  |  |
|  |  |  |  |  |  |  |  | /cloud/log/sls- |  |  |  |
|  |  |  |  |  |  |  |  |  | /cloud/log/sls- |  |  |
|  |  |  |  |  |  |  |  | backend- |  |  |  |
|  |  |  |  |  |  |  |  | server/SlsMeteringSe |  | sls-backend- |  |
|  | ls metering service l _ _ _ g |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | rvice#/sls metering _ _ |  | server.SlsMeteringSer |  |
|  |  |  |  |  |  |  |  | service app/tianji/s _ |  | vice |  |
|  |  |  |  |  | sls metering service l _ _ _ |  |  | tdout |  |  |  |
|  |  |  |  |  | og fuxiless _ |  |  |  |  |  |  |
| sls monitor log _ _ |  |  |  |  | sls monitor log |  |  | /apsara/sls/fcgi a _ gent/monitor *.LOG _ |  | sls-backend- server.SlsFastcgi# |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/fcgi a _ |  |  |
|  |  |  |  |  |  | monitor log |  | gent/monitor *.LOG _ |  |  |  |
|  |  |  |  | _ | _ _ | _ |  |  |  |  |  |
| sls operation agg log _ _ _ |  |  |  |  | sls operation agg log |  |  | /apsara/sls/fcgi a _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/fcgi a _ |  |  |
|  |  |  |  |  |  | operation agg log |  | gent/metering *.LOG _ |  |  |  |
|  |  |  | _ _ |  | _ _ _ | _ _ |  |  |  |  |  |
| sls operation log _ _ |  |  |  |  | sls operation log |  |  | /apsara/sls/fcgi a _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/sls/fcgi a _ |  |  |
|  |  |  |  |  |  | operation log |  | gent/ols operation*. _ |  |  |  |
|  |  | _ |  |  | _ _ | _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | LOG |  |  |  |

日志服务

|  | sls portal access log _ _ _ |  | sls portal access log _ _ _ |  | /apsara/sls/web/lo gs/access.log |  | sls-backend- server.SlsWeb# |  |
|---|---|---|---|---|---|---|---|---|
|  | sls portal api audit _ _ _ |  | sls portal api audit _ _ _ |  | /apsara/sls/web/lo gs/apidetail.log |  |  |  |
|  | sls portal http req _ _ _ |  | sls portal http req _ _ _ |  | /apsara/sls/web/lo gs/httpclient.log |  |  |  |
|  | sls portal normal _ _ |  | sls portal normal _ _ |  | /apsara/sls/web/lo gs/normal.log |  |  |  |
|  | sls portal sys info _ _ _ |  | sls portal sys info _ _ _ |  | /apsara/sls/web/lo gs/sysinfo.log |  |  |  |
|  | sls quotaserver log _ _ |  | sls quotaserver log |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  | quotaserver log | oot/sys/QuotaServer/ |  |  |  |
|  |  |  | _ _ | _ |  |  |  |  |
|  |  |  |  |  | quota server.LOG _ |  |  |  |
|  |  |  | sls quotaserver log fu _ _ _ |  | /apsara/sls/sls Qu _ |  |  |  |
|  |  |  |  |  |  | /apsara/sls/sls Qu _ |  |  |
|  |  |  |  | quotaserver log fu _ _ | otaServerRole/quota _ |  |  |  |
|  |  |  | xiless | ss |  |  |  |  |
|  |  |  |  |  | server.LOG |  |  |  |
|  | sls quotausage log _ _ |  | sls quotausage log |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  | /apsara/tubo/TempR | # |  |
|  |  |  |  | quotausage log | oot/sys/QuotaServer/ |  |  |  |
|  |  |  | _ _ | _ |  |  |  |  |
|  |  |  |  |  | charge.LOG |  |  |  |
|  |  |  | sls quotausage log fu _ _ _ |  | /apsara/sls/sls Qu _ |  |  |  |
|  |  |  |  |  |  | /apsara/sls/sls Qu _ |  |  |
|  |  |  |  | quotausage log fu _ _ | otaServerRole/charge |  |  |  |
|  |  |  | xiless | ss |  |  |  |  |
|  |  |  |  |  | .LOG |  |  |  |
|  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  | oot/sys/ShennongRepl |  |  |  |
|  |  |  | sls replayworker log _ _ | replayworker log |  |  |  |  |
|  |  |  |  |  | ayWorker/shennong re _ |  |  |  |
|  |  |  |  |  | play worker.LOG _ |  |  |  |
|  | sls replayworker log _ _ |  |  |  |  |  |  |  |
|  |  |  | sls replayworker log f |  | /apsara/sls/sls Sh _ |  |  |  |
|  |  |  |  |  |  | /apsara/sls/sls Sh _ | er# |  |
|  |  |  |  | replayworker log f | ennongReplayWorkerRo |  |  |  |
|  |  |  | _ _ _ uxiless | _ _ |  |  |  |  |
|  |  |  |  |  | le/shennong replay w _ _ |  |  |  |
|  |  |  |  |  | orker.LOG |  |  |  |

|  |  | /apsara/sls/web/lo |  |
|---|---|---|---|
| portal access log _ _ | gs/access.log |  |  |

|  |  | /apsara/sls/web/lo |  |
|---|---|---|---|
| portal api audit _ _ | gs/apidetail.log |  |  |

|  |  | /apsara/sls/web/lo | sls-backend- |
|---|---|---|---|
| portal http req _ _ | gs/httpclient.log |  |  |

|  |  | /apsara/sls/web/lo |  |
|---|---|---|---|
| portal normal _ | gs/normal.log |  |  |

|  |  | /apsara/sls/web/lo |  |
|---|---|---|---|
| portal sys info _ _ | gs/sysinfo.log |  |  |

日志服务

|  |  |  | sls service error log _ _ _ |  |  |  |  |  | /alidata/www/logs/ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | /alidata/www/logs/ |  |  |
|  |  |  |  |  |  |  |  |  | java/sls- |  |  |  |
|  |  |  |  |  |  | g | sls service error log _ _ _ | service error log |  |  |  |  |
|  |  |  |  |  |  |  |  |  | service/applog/error |  |  |  |
|  |  |  |  |  |  |  |  |  | .log |  |  |  |
|  |  |  | sls service info log _ _ _ |  |  |  |  |  | /alidata/www/logs/ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /alidata/www/logs/ |  |  |
|  |  |  |  |  |  |  |  |  | java/sls- |  |  |  |
|  |  |  |  |  |  |  | sls service info log _ _ _ | service info log |  |  |  |  |
|  |  |  |  |  |  |  |  |  | service/applog/info. |  |  |  |
|  |  |  |  |  |  |  |  |  | log |  |  |  |
|  |  |  |  |  |  |  | sls shennongworker lo |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  |  |  | shennongworker lo | oot/sys/ShennongWork |  |  |  |
|  |  |  |  |  |  |  | _ _ g | _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | er/shennong worker.L _ |  |  |  |
|  |  |  | sls shennongworker lo |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | OG |  |  |  |
|  |  |  | _ _ g |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | sls shennongworker lo _ _ |  | /apsara/sls/sls Sh _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sh _ |  |  |
|  |  |  |  |  |  |  |  | shennongworker lo _ | ennongWorkerRole/she |  |  |  |
|  |  |  |  |  |  |  | g fuxiless _ | uxiless |  |  |  |  |
|  |  |  |  |  |  |  |  |  | nnong worker.LOG _ |  |  |  |
|  |  |  | sls sync job |  |  |  |  |  | /apsara/cloud/app/ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/cloud/app/ |  |  |
|  |  |  |  |  |  |  |  |  | sls-backend- |  |  |  |
|  |  |  |  |  |  |  | sls-sync-job |  |  |  | sls-backend- |  |
|  |  |  |  |  |  |  |  |  | server/SyncJob#/sync |  | server.SyncJob# |  |
|  |  |  | _ _ |  |  |  |  |  |  |  | server. |  |
|  |  |  |  |  |  |  |  |  | job/current/log/sync |  |  |  |
|  |  |  |  |  |  |  |  |  | job.log |  |  |  |
|  |  |  | sls tool service _ _ |  |  |  | sls tool service |  | /apsara/sls/sls Sl _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sl _ | sls-backend- |  |
|  |  |  |  |  |  |  |  | tool service | sToolServiceRole/sls |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | server.SlsToolServi |  |
|  |  |  |  | _ |  |  | _ _ | _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | tool service.LOG _ _ |  |  |  |
|  |  |  | trace log _ |  |  |  | trace log |  | /apsara/shennong a _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/shennong a _ |  |  |
|  |  |  |  |  |  |  |  | e log | gent/tracer/index wo _ |  |  |  |
|  |  |  |  |  |  |  | _ | _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | rker trace.LOG _ |  |  |  |
|  |  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/tubo/TempR |  |  |
|  |  |  |  |  |  |  |  |  | oot/sys/ShennongWork |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | sls-backend- |  |
|  |  |  |  |  |  |  | worker input log _ _ | ker input log |  |  |  |  |
|  |  |  |  |  |  |  |  |  | er/shennong worker i _ _ |  | server.S |  |
|  |  |  |  |  |  |  |  |  | nput.LOG |  |  |  |
|  |  |  | worker input log _ _ |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | worker input log fuxil |  | /apsara/sls/sls Sh _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | /apsara/sls/sls Sh _ |  |  |
|  |  |  |  |  |  |  |  | ker input log fuxil | ennongWorkerRole/she |  |  |  |
|  |  |  |  |  |  |  | _ _ _ ess | _ _ _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | nnong worker input.L _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  | OG |  |  |  |

日志服务

### 通过SLS Pub Ops运维平台管理

**Project及云账号**

通过SLS Pub Ops运维平台可对Project及云账号进行管理。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部导航栏，选择**产品运维** > **存储运维** **> SLS****运维****·SLS Pub Ops**，进入运维平台。

**Project管理**

1. 登录SLS运维·SLS Pub Ops运维平台。
2. 在左侧导航栏，选择**Project****管理**，可查看可用区下全部的SLS Project信息。
3. 在SLS Project搜索栏，您可以输入Project名称或单击**高级搜索**后，在搜索框中输入云账号、地域、可用
区等信息，单击**立即查询**，可查询对应的Project信息。
4. 单击Project名称或操作列的**详情**，可查看该Project的基础信息如地域、可用区、登录名、云账号ID信
息，以及资源配额如logstore上限、shard上限等信息。 禁用/启用Project： 在基础信息区块，当该Project处于“已开启”状态时，单击状态字段旁的按钮，可禁用该 Project。

**说明**

禁用后该Project不可用，通过控制台访问会提示“project xxx（project名称）has been forbidden”。 当该Project处于禁用状态时，单击按钮，可重新启用该Project。 设置Project的资源配额： 单击**资源配额**旁的**编辑**按钮，在资源配额页面中，设置对应指标项的上限值。

**账号管理**

在账号列表中，云账号表示组织UID以及接入SLS的云产品（如负载均衡SLB、对象存储OSS等产品）的默认账号。可按照组织或接入SLS的云产品设置该账号可创建的Project数量及账号的可用性。
1. 登录SLS运维·SLS Pub Ops运维平台。
2. 在左侧导航栏，选择**账号管理**，可查看账号信息，如状态、账号可创建的Project最大值、修改时间等信
息。
3. 单击操作列的**修改**，账号处于启用状态时，单击对话框中的**状态**参数项的
按钮，可禁用该账号。反之账号处于禁用状态时，单击按钮，可启用该账号。
4. 在对话框中的**可创建****Project**数参数项，可设置该账号可创建的最大Project数量。
