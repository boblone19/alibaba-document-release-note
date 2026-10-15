---
title: "DataWorks 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 884
source_pdf: "06_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/dide/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# DataWorks 开发指南

DataWorks

## API简介

本文为您介绍DataWorks OpenAPI的列表详情。

**OpenAPI列表**

DataWorks OpenAPI包括租户、元数据、数据开发、数据集成、运维中心、数据质量、数据服务、调度、

**租户**

| API名称 | API描述 |
|---|---|
| CreateProject | 调用CreateProject接口创建项目。 |
| DeleteProject | 调用DeleteProject接口删除项目空间。 |
| BindProjectCalcEngin es | 调用BindProjectCalcEngines，绑定引擎。 |
| AddProjectMemberTo Role | 调用AddProjectMemberToRole，添加DataWorks工作空间的成员至目标角色。使用该接口前，您需要先添加目标账号为DataWorks工作空间的成员。 |
| CreateConnection | 调用CreateConnection创建一个数据源。 |
| CreateProjectMembe r | 调用CreateProjectMember，添加一个用户至DataWorks工作空间。 |
| CreateDataSource | 调用CreateDataSource接口，创建DataWorks数据源。 |
| DeleteConnection | 调用DeleteConnection删除一个数据源。 |
| DeleteProjectMembe r | 调用DeleteProjectMember，从DataWorks工作空间移除用户。 |
| DeleteDataSource | 调用DeleteDataSource接口，删除一个数据源。 |
| GetProject | 调用GetProject查询一个DataWorks工作空间的信息。 |
| GetProjectDetail | 调用GetProjectDetail查询一个DataWorks工作空间的信息。 |
| ListDataSources | 调用ListDataSources接口，查询DataWorks数据源列表。 |

DataWorks

| ListCalcEngines | 调用ListCalcEngines查看计算引擎列表。 |
|---|---|
| ListConnections | 调用ListConnections查询数据源列表。 |
| ListProjectMembers | 调用ListProjectMembers查询DataWorks工作空间中已存在成员的列表。 |
| ListProjectRoles | 调用ListProjectRoles获取工作空间所有角色的列表。 |
| ListProjects | 调用ListProjects，分页列出用户所在租户下的DataWorks工作空间列表。 |
| ListProjectIds | 调用ListProjectIds，使用目标阿里云账号（包括阿里云主账号或RAM用户）的ID获取其拥有角色权限的DataWorks工作空间的ID列表。 |
| ListResourceGroups | 调用ListResourceGroups查看指定类型的资源组列表。 |
| RemoveProjectMemb erFromRole | 调用RemoveProjectMemberFromRole，将DataWorks工作空间内的用户从 DataWorks角色中移除。 |
| UpdateConnection | 调用UpdateConnection更新一个数据源。 |
| UpdateDataSource | 调用UpdateDataSource接口，更新数据源。 |

### 元数据

| API名称 | API描述 |
|---|---|
| AddToMetaCategory | 调用AddToMetaCategory添加表至指定的类目。 |
| CheckMetaPartition | 调用CheckMetaPartition检查分区是否存在。 |
| CheckMetaTable | 调用CheckMetaTable检查表是否存在。 |
| CreateMetaCategory | 调用CreateMetaCategory创建类目。 |
| CreateTable | 调用CreateTable创建一个MaxCompute的表或视图。 |
| CreateTableTheme | 调用CreateTableTheme创建主题。不建议使用该API，后续将有新API上线覆盖此功能。 |

DataWorks

| CreateTableLevel | 调用CreateTableLevel创建层级。不建议使用该API，后续将有新API上线覆盖此功能。 |
|---|---|
| DeleteFromMetaCate gory | 调用DeleteFromMetaCategory从指定的类目中移除表。 |
| DeleteMetaCategory | 调用DeleteMetaCategory删除类目。 |
| DeleteTable | 调用DeleteTable删除MaxCompute表。 |
| DeleteTableLevel | 调用DeleteTableLevel删除层级。不建议使用该API，后续将有新API上线覆盖此功能。 |
| DeleteTableTheme | 调用DeleteTableTheme删除主题。不建议使用该API，后续将有新API上线覆盖此功能。 |
| GetDDLJobStatus | 调用GetDDLJobStatus获取创建表、更新表和删除表的任务状态。 |
| GetMetaDBInfo | 调用GetMetaDBInfo获取引擎实例的基本元数据信息。 |
| GetMetaDBTableList | 调用GetMetaDBTableList获取引擎实例中的表。 |
| GetMetaCategory | 调用GetMetaCategory查询类目树。 |
| GetMetaColumnLinea ge | 调用GetMetaColumnLineage获取字段的血缘关系。 |
| GetMetaMetrics | 调用GetMetaMetrics获取概览数据，包含instance数目、storage数据等。 |
| GetMetaStorageTren d | 调用GetMetaStorageTrend获取存储趋势。 |
| GetMetaTableBasicIn fo | 调用GetMetaTableBasicInfo获取表的基础信息。 |
| GetMetaTableColum n | 调用GetMetaTableColumn获取表的字段信息。 |
| GetMetaTableChang eLog | 调用GetMetaTableChangeLog获取表的变更日志。 |
| GetMetaTableFullInfo | 调用GetMetaTableFullInfo获取表的完整信息（包括字段信息）。 |

DataWorks

| GetMetaTableIntroWi ki | 调用GetMetaTableIntroWiki获取表的使用说明。 |
|---|---|
| GetMetaTableLineag e | 调用GetMetaTableLineage获取表的血缘关系。 |
| GetMetaTableListByC ategory | 调用GetMetaTableListByCategory查询指定类目下的表。 |
| GetMetaTableOutput | 调用GetMetaTableOutput获取表的产出信息。 |
| GetMetaTablePartitio n | 调用GetMetaTablePartition获取表的分区列表。 |
| ListMetaDB | 调用ListMetaDB查询数据库列表。 |
| ListTableLevel | 调用ListTableLevel查询层级列表。不建议使用该API，后续将有新API上线覆盖此功能。 |
| ListTableTheme | 调用ListTableTheme查询主题列表。不建议使用该API，后续将有新API上线覆盖此功能。 |
| SearchMetaTables | 调用SearchMetaTables根据条件搜索表。 |
| SearchMetaTableByK ey | 调用SearchMetaTableByKey实现基于关键词的元数据表搜索，以便快速定位目标数据。 |
| UpdateMetaCategory | 调用UpdateMetaCategory更新类目。 |
| UpdateMetaTable | 调用UpdateMetaTable更新表的Meta信息。 |
| UpdateMetaTableIntr oWiki | 调用UpdateMetaTableIntroWiki更新表的说明信息，当数据不存在时增加信息。 |
| UpdateTable | 调用UpdateTable更新MaxCompute表。 |
| UpdateTableLevel | 调用UpdateTableLevel更新层级。不建议使用该API，后续将有新API上线覆盖此功能。 |
| UpdateTableModelInf o | 调用UpdateTableModelInfo修改表的主题、层级和物理分类等信息。不建议使用该 API，后续将有新API上线覆盖此功能。 |

DataWorks

| UpdateTableTheme | 调用UpdateTableTheme更新主题。不建议使用该API，后续将有新API上线覆盖此功能。 |
|---|---|
| UpdateTableAddColu mn | 调用UpdateTableAddColumn更新MaxCompute表的字段信息。 |
| GetMetaTableTheme Level | 调用GetMetaTableThemeLevel获取表的主题和层级信息。 |

### 数据开发

| API名称 | API描述 |
|---|---|
| CreateFile | 调用CreateFile，在数据开发中创建一个文件。目前不支持调用该接口创建数据集成节点任务。 |
| CreateFolder | 调用CreateFolder创建文件夹。 |
| CreateUdfFile | 调用CreateUdfFile，在数据开发中创建函数类型文件。 |
| CreateBusiness | 调用CreateBusiness，创建数据开发（DataStudio）的业务流程。 |
| CreateResourceFile | 调用CreateResourceFile上传资源。 |
| DeleteBusiness | 调用DeleteBusiness删除业务流程。 |
| DeleteFile | 调用DeleteFile删除数据开发中的文件。 |
| DeleteFolder | 调用DeleteFolder删除数据开发页面的文件夹。 |
| DeployFile | 调用DeployFile发布文件至生产环境。 |
| EstablishRelationTabl eToBusiness | 调用EstablishRelationTableToBusiness，导入表至业务流程。相当于在数据开发页面右键单击业务流程，选择导入表的操作。 |
| GetBusiness | 调用GetBusiness查询业务流程的详情。 |
| GetDeployment | 调用GetDeployment获取发布包的详情。 |
| GetFileVersion | 调用GetFileVersion获取文件的版本详情。 |

DataWorks

| GetFile | 调用GetFile获取文件的详情。 |
|---|---|
| GetFolder | 调用GetFolder获取文件夹的详情。 |
| GetNodeTypeListInfo | 调用GetNodeTypeListInfos查询节点类型信息，包括类型Code和类型名称. |
| ListBusiness | 调用ListBusiness查询业务流程的列表。 |
| ListFiles | 调用ListFiles查询文件列表。 |
| ListFileVersions | 调用ListFileVersions查询文件的版本列表。 |
| ListFolders | 调用ListFolders查询文件夹的列表。 |
| SubmitFile | 调用SubmitFile，提交文件至调度系统的开发环境，生成对应的任务。该API是异步处理，您可以使用GetDeployment接口获取文件的提交状态。 |
| UpdateFile | 调用UpdateFile更新已创建的文件节点。调试或调用该接口时，填写的参数必须和该节点原本的文件配置不同。例如，源节点的某参数值为A，则需要变更为B后再提交。如果仍填写A，会报invalid异常。 |
| UpdateBusiness | 调用UpdateBusiness更新业务流程。 |
| UpdateFolder | 调用UpdateFolder更新文件夹的信息。 |
| UpdateUdfFile | 调用UpdateUdfFile更新函数的文件信息。 |
| UpdateResourceFile | 调用UpdateResourceFile更新资源文件。 |
| UpdateIDEEventResul t | 调用UpdateIDEEventResult接口，在数据开发过程中触发扩展点时，通过将扩展程序对扩展点事件的检查结果返回给数据开发系统。 |
| CheckFileDeployment | 当您在DataWorks数据开发页面创建的文件提交成功后，文件将进入发布检查状态，DataWorks会将文件发布检查事件返回给您，您需要根据事件内容判断该文件是否可以继续进行发布校验。此时，可以通过调用CheckFileDeployment接口，将待发布文件的检查结果返回至DataWorks。 |
| GetIDEEventDetail | 调用GetIDEEventDetail查询触发扩展点事件时的数据快照。 |
| ListDeployments | 调用ListDeployments查询发布包列表信息。 |

DataWorks

| OfflineNode | 您可以调用OfflineNode下线节点。 |
|---|---|
| addNode | 该API用于在DataWorks中创建新的节点。 |
| DeleteNode | 该接口用于删除数据开发节点。 |
| SelectNodeList | 该接口用于查询指定租户下的节点列表。 |
| UpdateNode | 该接口用于更新数据开发节点信息。 |

### 数据集成

| API名称 | API描述 |
|---|---|
| CreateDISyncTask | 调用CreateDISyncTask创建数据集成同步任务。 |
| GetDataSourceMeta | 调用GetDataSourceMeta获取目标数据源的Meta信息。 |
| ListDIProjectConfig | 调用ListDIProjectConfig查看当前工作空间中数据集成同步解决方案任务默认的全局配置。 |
| TestNetworkConnecti on | 调用TestNetworkConnection接口，测试目标数据源与所使用资源组的网络连通性。 |
| UpdateDIProjectConfi g | 调用UpdateDIProjectConfig修改当前工作空间中数据集成同步解决方案任务默认的全局配置。 |
| UpdateDISyncTask | 调用UpdateDISyncTask更新数据集成同步任务。 |
| GetDISyncTask | 调用GetDISyncTask获取数据集成实时同步任务或同步解决方案的详情。 |
| GetDISyncInstanceInf o | 调用GetDISyncInstanceInfo接口，获取实时同步任务和同步解决方案任务的运行状态。 |
| ListRefDISyncTasks | 调用ListRefDISyncTasks查看数据集成同步任务。 |

### 数据建模

| API名称 | API描述 |
|---|---|

DataWorks

| QueryPublicModelEng ine | 调用QueryPublicModelEngine查询数据建模引擎的信息。 |
|---|---|
| SearchElement | 调用SearchElement接口，使用名称和中文名查询对象。默认为表和字段，仅搜索模型的master分支。 |
| UpdateModel | 调用UpdateModel接口，修改一个模型属性。 |
| UpdatePublicDomain | 调用UpdatePublicDomain接口，修改一个公共数据标准的内容。 |
| UpdateDomainCode | 调用UpdateDomainCode接口，修改一个标准代码。 |
| GetModelApplyDomai nStatus | 调用GetModelApplyDomainStatus接口，获取模型所使用数据标准的相关信息。 |
| DeleteDomainCodes | 调用DeleteDomainCodes接口，删除一组标准代码。 |
| CreatePublicDomain | 调用CreatePublicDomain接口，创建公共数据标准。 |
| AddDomainCode | 调用AddDomainCode接口，创建一个标准代码。 |
| DeletePublicDomains | 调用DeletePublicDomains接口，删除公共数据标准。 |

### 运维中心

| API名称 | API描述 |
|---|---|
| CreateDagCompleme nt | 调用CreateDagComplement创建补数据工作流。 |
| CreateDagTest | 调用CreateDagTest创建冒烟测试工作流。 |
| CreateRemind | 调用CreateRemind创建自定义报警规则。 |
| DeleteRemind | 调用DeleteRemind删除自定义监控报警规则。 |
| GetBaselineConfig | 调用GetBaselineConfig获取配置详情。 |
| GetBaselineKeyPath | 调用GetBaselineKeyPath获取基线实例的关键路径。 |

DataWorks

| GetBaselineStatus | 调用GetBaselineStatus获取基线实例的详情。 |
|---|---|
| GetDag | 调用GetDag，根据DagId获取Dag详情。GetDag支持查询手动业务流程、手动任务、 补数据的Dag详情信息，不支持查询日常调度Dag详情。 |
| GetInstance | 调用GetInstance获取实例的详情。 |
| GetInstanceConsume TimeRank | 调用GetInstanceConsumeTimeRank获取实例运行时长排行。 |
| GetInstanceCountTre nd | 调用GetInstanceCountTrend获取周期实例数量的趋势。 |
| GetInstanceErrorRank | 调用GetInstanceErrorRank获取近一个月节点的出错排行。 |
| GetInstanceLog | 调用GetInstanceLog获取实例的日志。 |
| GetInstanceStatusSta tistic | 调用GetInstanceStatusStatistic获取实例任务不同运行状态的数量统计。 |
| GetNode | 调用GetNode获取节点的详情。 |
| GetNodeCode | 调用GetNodeCode获取节点的代码。 |
| GetNodeOnBaseline | 调用GetNodeOnBaseline获取基线上的节点。 |
| GetNodeChildren | 调用GetNodeChildren获取节点下游列表。 |
| GetNodeParents | 调用GetNodeParents获取节点上游列表。 |
| GetRemind | 调用GetRemind获取自定义监控报警规则的详情。 |
| GetSuccessInstanceTr end | 调用GetSuccessInstanceTrend获取当天任务分时段的统计趋势。 |
| GetTopic | 调用GetTopic获取事件的详情。 |
| GetTopicInfluence | 调用GetTopicInfluence获取事件影响的基线实例列表。 |
| GetFileTypeStatistic | 调用GetFileTypeStatistic获取节点任务类型的分布情况。 |

DataWorks

| ListFileType | 调用ListFileType查询任务节点的类型信息，包括类型Code和类型名称。 |
|---|---|
| ListAlertMessages | 调用ListAlertMessages获取报警信息的列表。 |
| ListBaselineConfigs | 调用ListBaselineConfigs获取基线列表。 |
| ListBaselineStatuses | 调用ListBaselineStatuses获取基线实例列表。 |
| ListDataServicePublis hedApis | 调用ListDataServicePublishedApis获取数据服务API的发布态信息列表。 |
| ListDags | 调用ListDags接口，根据OpSeq（补数据唯一标识）获取单次补数据的所有Dag详情。 |
| ListInstances | 调用ListInstances获取实例的列表。 |
| ListInstanceAmount | 调用ListInstanceAmount获取指定时间段周期实例数量的趋势。 |
| ListInstanceHistory | 调用ListInstanceHistory，获取所有实例历史记录，任务重跑一次就会生成一条历史记录。 |
| ListSuccessInstanceA mount | 调用ListSuccessInstanceAmount，获取业务日期当天生成的周期实例任务，在业务日期的不同整点时刻，运行成功的实例数量统计趋势。 |
| ListManualDagInstanc es | 调用ListManualDagInstances获取手动执行的业务流程实例的信息。 |
| ListNodes | 调用ListNodes获取节点的列表。 |
| ListInnerNodes | 调用ListInnerNodes接口，获取内部节点详情，例如查询组合节点、循环节点等节点类型的内部节点。但是该接口不支持获取PAI节点的内部节点详情。 |
| ListNodeIO | 调用ListNodeIO查询上下游节点的信息，只能查询一层。 |
| ListNodeInputOrOutp ut | 调用ListNodeInputOrOutput接口，查询当前节点的输入输出信息。 |
| ListNodesByOutput | 调用ListNodesByOutput根据节点的输出结果精确查询目标节点。 |
| ListNodesByBaseline | 调用ListNodesByBaseline获取基线中的节点。 |

DataWorks

| ListReminds | 调用ListReminds获取或搜索自定义监控规则列表。 |
|---|---|
| ListTopics | 调用ListTopics获取或搜索事件列表。 |
| RestartInstance | 调用RestartInstance重启实例。 |
| ResumeInstance | 调用ResumeInstance恢复暂停状态的实例。 |
| RunTriggerNode | 调用RunTriggerNode运行一个触发式节点。 |
| RunCycleDagNodes | 调用RunCycleDagNodes创建补数据工作流。 |
| RunManualDagNodes | 调用RunManualDagNodes执行手动业务流程。手动业务流程必须已经在环境界面提交发布，提交发布后运维中心才会显示对应手动业务流程，您才可以使用该接口调用执行。 |
| RunSmokeTest | 调用RunSmokeTest创建冒烟测试工作流。 |
| SetSuccessInstance | 调用SetSuccessInstance，重置失败状态的实例为成功。 |
| StopInstance | 调用StopInstance终止实例。 |
| SuspendInstance | 调用SuspendInstance暂停实例。 |
| TopTenElapsedTimeIn stance | 调用TopTenElapsedTimeInstance获取已运行完成（即运行状态为成功或失败）的实例运行时长的排行情况。 |
| TopTenErrorTimesInst ance | 调用TopTenErrorTimesInstance获取近一个月节点的出错排行。 |
| UpdateRemind | 调用UpdateRemind更新自定义报警规则。 |
| UpdateNodeOwner | 调用UpdateNodeOwner修改目标节点的负责人。 |
| UpdateNodeRunMode | 调用UpdateNodeRunMode冻结或解冻目标节点。 |

### 数据质量

| API名称 | API描述 |
|---|---|

DataWorks

| CreateQualityEntity | 调用CreateQualityEntity创建数据质量的分区表达式。 |
|---|---|
| CreateQualityFollower | 调用CreateQualityFollower创建分区表达式的订阅人。 |
| CreateQualityRelative Node | 调用CreateQualityRelativeNode创建分区表达式关联。 |
| CreateQualityRule | 调用CreateQualityRule创建质量监控规则。 |
| DeleteQualityEntity | 调用DeleteQualityEntity删除分区表达式。 |
| DeleteQualityFollower | 调用DeleteQualityFollower删除分区表达式的订阅人。 |
| DeleteQualityRelative Node | 调用DeleteQualityRelativeNode删除调度关联。 |
| DeleteQualityRule | 调用DeleteQualityRule删除规则。 |
| GetQualityEntity | 调用GetQualityEntity获取分区表达式。 |
| GetQualityFollower | 调用GetQualityFollower获取分区表达式的订阅人。 |
| GetQualityRule | 调用GetQualityRule获取规则的信息。 |
| ListQualityResultsByE ntity | 调用ListQualityResultsByEntity，根据分区表达式查询历史校验结果。 |
| ListQualityResultsByR ule | 调用ListQualityResultsByRule，根据校验规则校验数据源的质量，并查询校验结果。 |
| ListQualityRules | 调用ListQualityRules根据分区表达式获取规则列表。 |
| UpdateQualityFollowe r | 调用UpdateQualityFollower更新订阅关系。 |
| UpdateQualityRule | 调用UpdateQualityRule更新规则。 |

### 数据服务

| API名称 | API描述 |
|---|---|

DataWorks

| AbolishDataServiceApi | 调用AbolishDataServiceApi下线数据服务API。 |
|---|---|
| CreateDataServiceApi | 调用CreateDataServiceApi创建数据服务API。 |
| CreateDataServiceApi Authority | 调用CreateDataServiceApiAuthority新增数据服务API授权。 |
| CreateDataServiceFol der | 调用CreateDataServiceFolder创建数据服务文件夹。 |
| CreateDataServiceGro up | 调用CreateDataServiceGroup创建数据服务业务流程。 |
| DeleteDataServiceApi | 调用DeleteDataServiceApi删除数据服务API。 |
| DeleteDataServiceApi Authority | 调用DeleteDataServiceApiAuthority取消数据服务API授权。 |
| GetDataServiceApi | 调用GetDataServiceApi查询数据服务API开发态的详情。 |
| GetDataServiceApplic ation | 调用GetDataServiceApplication查询数据服务App的详情。 |
| GetDataServiceFolder | 调用GetDataServiceFolder查询数据服务文件夹。 |
| GetDataServiceGroup | 调用GetDataServiceGroup查询数据服务业务流程。 |
| GetDataServicePublis hedApi | 调用GetDataServicePublishedApi查询数据服务API的发布态信息。 |
| ListDataServiceApis | 调用ListDataServiceApis获取数据服务API开发中的信息列表。 |
| ListDataServiceApiAut horities | 调用ListDataServiceApiAuthorities获取授权给他人的API列表。 |
| ListDataServiceApplic ations | 调用ListDataServiceApplications获取数据服务应用的基础信息列表。 |
| ListDataServiceAuthor izedApis | 调用ListDataServiceAuthorizedApis获取获得授权的API信息列表。 |

DataWorks

| ListDataServiceFolder s | 调用ListDataServiceFolders查询数据服务文件夹列表。 |
|---|---|
| ListDataServiceGroup s | 调用ListDataServiceGroups查询数据服务业务流程列表。 |
| PublishDataServiceApi | 调用PublishDataServiceApi发布数据服务API。 |
| UpdateDataServiceApi | 调用UpdateDataServiceApi更新数据服务API开发态的信息。 |

**调度**

| API名称 | API描述 |
|---|---|
| CreateManualDag | 调用CreateManualDag触发手动业务流程执行。手动业务流程必须已经在界面提交发布，运维中心能够找到对应的手动业务流程，才能使用该接口。 |
| GetInstanceStatusCou nt | 调用GetInstanceStatusCount获取实例不同状态的数量统计。 |
| GetManualDagInstanc es | 调用GetManualDagInstances，获取手动执行的业务流程实例的信息。 |
| ListProgramTypeCount | 调用ListProgramTypeCount获取节点任务类型的分布。 |
| SearchNodesByOutput | 调用SearchNodesByOutput，根据输出精确查询节点。 |

| API名称 | API描述 |
|---|---|
| AddRuleConfig | 调用AddRuleConfig接口新增数据识别规则。 |
| AddRuleConfigMessag e | 调用AddRuleConfigMessage接口新增数据识别规则。 |
| UpdateRuleConfig | 调用UpdateRuleConfig修改数据识别规则。 |
| UpdateRuleConfigMes sage | 调用UpdateRuleConfigMessage修改数据识别规则。 |

DataWorks

| DeleteRuleConfig | 调用DeleteRuleConfig接口删除数据识别规则。 |
|---|---|
| DeleteRuleConfigMess age | 调用DeleteRuleConfigMessage删除敏感规则。 |
| DesensitizeData | 调用DesensitizeData输入待脱敏数据，返回脱敏后的结果数据。 |
| GetRuleConfig | 调用GetRuleConfig获取数据识别规则。 |
| GetRuleConfigMessag e | 调用GetRuleConfigMessage获取数据识别规则。 |
| GetRuleDataMessage | 调用GetRuleDataMessage根据规则查询分级或者分级查询规则。 |
| GetRuleMessage | 调用GetRuleMessage根据规则查询分级或者分级查询规则。 |
| GetSensLevel | 调用GetSensLevel获取敏感规则分级列表。 |
| GetSensLevelMessage | 调用GetSensLevelMessage接口获取分级列表。 |
| GetSensTableLevel | 第三方调用GetSensTableLevel接口获取安全等级。 |
| GetSensTableLevelMe ssage | 调用GetSensTableLevelMessage获取保护伞接口安全等级。 |
| GetOpSensitiveData | 调用GetOpSensitiveData接口，获取租户下所有DataWorks工作空间指定日期的敏感数据访问记录。 |
| GetSensitiveData | 调用GetSensitiveData，获取租户下所有DataWorks工作空间的最新敏感数据识别结果。 |
| ScanSensitiveData | 调用ScanSensitiveData识别输入数据中是否存在敏感数据。 |
| AddSenRule | 该接口用于在DataWorks中创建并配置新的数据识别规则。 |
| AddSensLevel | 该接口用于在DataWorks中添加新的敏感级别配置。 |
| DeleteSenRule | 该接口用于删除DataWorks中的敏感规则。 |
| GetSenRule | 该接口用于查询敏感规则。 |

| 开发指南·API简介 | DataWork |
|---|---|

| GetSensitiveCountDat a | 获取指定租户的敏感数据统计信息。 |
|---|---|
| UpdateRiskInfoData | 该接口用于更新指定实例的风险信息数据。 |
| UpdateSenRule | 该接口用于更新敏感规则。 |
| UpdateSensitive | 该接口用于更新敏感数据规则配置的接口。 |

### 安全中心

| API名称 | API描述 |
|---|---|
| CreatePermissionApply Order | 调用CreatePermissionApplyOrder创建一个权限申请单。 |
| ApprovePermissionApp lyOrder | 调用ApprovePermissionApplyOrder审批一个权限申请单。 |
| ListPermissionApplyOr ders | 调用ListPermissionApplyOrders查询权限申请单列表。 |
| GetPermissionApplyOr derDetail | 调用GetPermissionApplyOrderDetail查询一个权限申请单的详细信息。 |
| RevokeColumnPermiss ion | 调用RevokeColumnPermission，撤销用户的表字段权限。 |
| RevokeTablePermissio n | 调用RevokeTablePermission，撤销用户的表权限。 |

### 迁移助手

| API名称 | API描述 |
|---|---|
| GetMigrationProcess | 调用GetMigrationProcess获取导入导出任务的进度状态。 |
| StartMigration | 调用StartMigration启动执行导入导出任务。 |

DataWorks

| GetMigrationSummary | 调用GetMigrationSummary获取导入或导出任务的信息。 |
|---|---|
| ListMigrations | 调用ListMigrations获取迁移任务列表。 |

### 开放平台

| API名称 | API描述 |
|---|---|
| GetExtension | 调用GetExtension接口，获取某个扩展程序详情。 |
| GetOptionValueForProj ect | 调用GetOptionValueForProject接口，获取扩展程序选项配置在项目空间下的配置。 |

DataWorks

## 准备工作

### 获取AccessKey

访问身份验证中通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。本文将为您描述如何获取通过RAM授权的AccessKey。

**前提条件**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**背景信息**

AccessKey支持两种授权模式： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 本文仅为您介绍如何获取通过RAM授权的AccessKey，通过STS授权的AccessKey获取方式请参见获取 STS AccessKey。 推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，将鼠标悬停在当前登录用户的头像上，单击**个人信息**。
DataWorks
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。
DataWorks

## 通过POP网关调用专有云API

当您需要通过 POP 网关调用专有云 DataWorks API 时，本文提供完整的 Java SDK 接入指引，包括服务地址、AccessKey、产品名、RegionId 和 Endpoint 名称等关键参数的配置方法，以及鉴权逻辑和调用示例。

**重要**

DataWorks HTTP API 已停止维护，请您尽快迁移至 Java SDK。

**服务地址Endpoint**

通常服务地址的规则为字符串 `dataworks+`专有云的部署域名。 假设专有云的 DataWorks IDE 访问地址为 `http://ide.envxxx.yyyyy.com` ： 普通单机房模式的环境：Endpoint以 `dataworks-public` 为前缀。则服务地址为 `dataworks-`

```
public.envxxx.yyyyy.com 。
```

多Region环境：Endpoint以 `dataworks-public-vpc` 为前缀。则服务地址为 `dataworks-public-`

```
vpc.envxxx.yyyyy.com 。
```

**说明**

DataWorks POP 网关已实现 IPv4/IPv6 双栈支持。如需使用产品的 IPv4/IPv6 双栈能力，请联系阿里云技术支持完成**平台侧的** **IPv6** **能力前置改造**和**产品** **IPv6** **的启用**（详情可参见《**专有云****VPC** **运维**
**指南**》中的**网络变更** > **功能编排** **> IPv6****大盘章节**）。

**AccessID和AccessKey**

专有云用户的阿里云账号的 AccessID 和 AccessKey。

**产品名**

产品名为固定的字符串： `dataworks-public` 。

**RegionId和Endpoint名称**

RegionId 为固定值 default。 EndpointName 为固定值 default。

**调用授权**

3.13及之后的版本无需授权，您可以直接调用。

**SDK调用**

Client端发送请求，携带指定参数发送至服务地址，会跳转到POP（API网关），在POP中经过一系列鉴权，鉴权失败直接返回结果，鉴权通过会跳转到具体的API服务，API调用成功返回相应的参数和结果。

**调用示例代码**

DataWorks

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dataworks_public.model.v20200518.*;
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-qingdao", "
<accessKeyId>", "<accessSecret>");
        DefaultProfile.addEndpoint("", "dataworks-public“, "endpoint");
        IAcsClient client = new DefaultAcsClient(profile);
        GetDataServiceApiRequest request = new GetDataServiceApiRequest();
        request.setTenantId(123);
        request.setProjectId(123);
        request.setApiId(123);
        try {
            GetDataServiceApiResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
        }
    }
}
```

DataWorks

## OpenAPI参考

### 租户

#### CreateProject

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 地域ID。 |
| ProjectNa me | Strin g | Query | 是 | autotest | 引擎或者数据源的名称。 |
| ProjectDe scription | Strin g | Query | 是 | test describe _ | 工作空间的详细描述信息。 |
| DisableDe velopmen t | Boole an | Query | 否 | false | 是否禁用开发角色，取值如下： false ：默认值，开启开发角色。 true ：禁用开发角色。 |
| IsAllowDo wnload | Integ er | Query | 否 | 1 | 是否允许下载ide上查询的结果，取值如下： 1 ：默认值，允许下载。 0 ：不允许下载。 |
| ProjectMo de | Integ er | Query | 否 | 1 | 工作空间模式： 简单工作空间模式为2。 标准工作空间模式为3。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectIde ntifier | Strin g | Query | 是 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与 ProjectId参数，二者必须设置其一，用来确定本次API 调用操作的DataWorks工作空间。 |
| Resource ManagerR esourceGr oupId | Strin g | Query | 否 | rg-acfmzbn7pt**** | 资源组ID。 |
| Tags | Repe atList | Query | 否 | ["tag1", "tag2", "tag3"] | 待绑定的数据资产标签列表。 |
| -Key | Strin g |  | 是 | batch | 标签Key。 |
| -Value | Strin g |  | 是 | 100.0 | 阈值数值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Success | Boolean | Boolean | 是否请求成功。 |
| Data | Long | 1234 | 返回结果数据。 |

**示例**

请求示例 DataWorks

```
&RegionId=default &ProjectName=autotest &ProjectDescription=test_describe &ProjectIdentifier=dw_project
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":1234,
 "Success":false
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>1234</Data> <Success>false</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 100003001 | Invalid.Tenant.ConnectionNotE xists | The connection does not exist. |
| 400 | 100002003 | Invalid.Tenant.ProjectNotExists | The project does not exist. |
| 400 | 100002001 | Invalid.Tenant.UserNotInProjec t | The user is not in the project. |
| 403 | 100002002 | Invalid.Tenant.UserIsNotProjec tOwnerOrAdmin | The user is not a project administrator or owner. |
| 403 | 100001001 | Invalid.Tenant.UserNotInTenan t | The user is not in tenant. |

#### DeleteProject

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 地域ID。 |
| ProjectId | Long | Query | 是 | 10000 | 工作空间的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Success | Boolean | Boolean | 是否请求成功。 |
| Data | Struct | { "HttpStatusCode": 200, "Success": true } | 返回结果数据。 |

**示例**

请求示例

```
&RegionId=default &ProjectId=10000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":"{   \"HttpStatusCode\": 200,   \"Success\": true }",
 "Success":false
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>{ &quot;HttpStatusCode&quot;: 200, &quot;Success&quot;: true }</Data> <Success>false</Success>
```

**错误码**

DataWorks

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1120010003 | Invalid.DI.Parameter | The parameter is invalid. |
| 403 | 1120010001 | Forbidden.DI.NoPrivilege | No access. |
| 500 | 1120010002 | InternalError.DI.Parameter | A DI internal error occurred. |

#### BindProjectCalcEngines

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID。 |
| ProjectId | Long | Query | 是 | 10000 | 工作空间的ID。 |
| CalcEngin eId | Long | Query | 是 | 1 | 表示计算引擎的唯一标识符，示例值“1”可能对应默认或基础计算引擎。 |
| DevCalcE ngineId | Long | Query | 否 | 2 | 表示计算引擎的唯一标识符，示例值“1”可能对应默认或基础计算引擎。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Success | Boolean | Boolean | 是否请求成功。 |
| Data | Boolean | { "HttpStatusCode": 200, "Success": true } | 返回结果数据。 |

**示例**

DataWorks 请求示例

```
http(s)://[Endpoint]/?Action=BindProjectCalcEngines &RegionId= &ProjectId= &CalcEngineId=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":false,
 "Success":false
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>false</Data> <Success>false</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 100003001 | Invalid.Tenant.ConnectionNotE xists | The connection does not exist. |
| 400 | 100002003 | Invalid.Tenant.ProjectNotExists | The project does not exist. |
| 400 | 100002001 | Invalid.Tenant.UserNotInProjec t | The user is not in the project. |
| 403 | 100002002 | Invalid.Tenant.UserIsNotProjec tOwnerOrAdmin | The user is not a project administrator or owner. |
| 403 | 100001001 | Invalid.Tenant.UserNotInTenan t | The user is not in tenant. |

#### AddProjectMemberToRole

调用AddProjectMemberToRole，添加DataWorks工作空间的成员至目标角色。使用该接口前，您需要先添加目标账号为DataWorks工作空间的成员。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | AddProjectMem berToRole | 系统规定参数。取值： AddProjectMemberToRole。 |
|---|---|---|---|---|
| ProjectId | Long | 是 | 27 | DataWorks工作空间的ID。您可以通过 ListProjects接口获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RoleCode | String | 是 | role project gue _ _ st | DataWorks工作空间角色的Code。您可以调用ListProjectRoles获取角色的 Code。 |
| UserId | String | 是 | 1234 | 阿里云账号ID。您可以登录DataWorks控制台，鼠标悬停至顶部菜单栏右侧的用户头像，查看账号ID。 |
| ClientToken | String | 否 | 1AFAE64E- D1BE-432B- A9***** | 幂等字段，建议使用UUID。用于唯一标识此次调用操作。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AFAE64E-D1BE- 432B-A9**** | 请求的ID。用于定位日志，排查问题。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddProjectMemberToRole &ProjectId=27 &RegionId=default &RoleCode=role_project_guest &UserId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>1AFAE64E-D1BE-432B-A9****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "1AFAE64E-D1BE-432B-A9****"
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### CreateConnection

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateConnectio n | 系统规定参数。取值： CreateConnection。 |
| ConnectionType | String | 是 | rds | 连接串的类型。常用类型枚举如下： odps mysql rds oss sqlserver polardb oracle mongodb emr postgresql analyticdb for mysql _ _ hybriddb for postgresql _ _ holo |
|  |  |  |  | 数据源的详细信息。部分常用数据源样例如下： odps |

| 开发指南·OpenAPI参 | 考 |  |  | DataWork |
|---|---|---|---|---|
|  |  |  |  | { "accessId": "xssssss", "accessKey": "xsaxsaxsa", "authType": 2, "endpoint": "http://service.odps.aliyun.c om/api", "project": "xsaxsax", "tag": "public" } mysql { "database": "xsaxsa", "instanceName": "rm- xsaxsa", "password": "xsaxsa", "rdsOwnerId": "xasxsa", "regionId": "cn-shanghai", "tag": "rds", "username": "xsaxsa" } rds { "configType": 1, "tag": "rds", "database": "xsaxsa", "username": "xsaxsa", "password": "xssaxsa$32050", "instanceName": "rm- xsaxs", "rdsOwnerId": "11111111" } oss { "accessId": "sssssxx", "accessKey": "xsaxaxsaxs", "bucket": "xsa-xs-xs", "endpoint": "http://oss- cn-shanghai.aliyuncs.com", "tag": "public" } |

DataWorks

| Content | String | 是 | {"database":"db name","instance Name":"instance name","passwor d":"password","r dsOwnerId":"12 3","username":" | sqlserver { "jdbcUrl": "jdbc:sqlserver://xsaxsa- xsaxsa.database.xxx.cn:123;Da tabaseName=xsxs-xsxs", "password": "sdasda$fs", "tag": "public", "username": "sxaxacdacdd" } polardb { "clusterId": "pc- sdadsadsa", "database": "dsadsadsa", "ownerId": "121212122", "password": "sdasdafssa", "region": "cn-shanghai", "tag": "polardb", "username": "asdadsads" } oracle { "jdbcUrl": "jdbc:oracle:saaa:@xxxxx:1521 :PROD", "password": "sxasaxsa", "tag": "public", "username": "sasfadfa" } mongodb { "address": " [\"xsaxxsa.mongodb.rds.aliyun cs.com:3717\"]", "database": "admin", "password": "sadsda@", |
|---|---|---|---|---|
|  |  |  | username"} | "tag": "public", "username": "dsadsadas" } emr |

DataWorks

|  |  |  |  | { "accessId": "xsaxsa", "emrClusterId": "C-dsads", "emrResourceQueueName": "default", "emrEndpoint": "emr.aliyuncs.com", "accessKey": "dsadsad", "emrUserId": "224833315798889783", "name": "sasdsadsa", "emrAccessMode": "simple", "region": "cn-shanghai", "authType": "2", "emrProjectId": "FP- sdadsad" } postgresql { "jdbcUrl": "jdbc:postgresql://xxxx:1921/ ssss", "password": "sdadsads", "tag": "public", "username": "sdsasda" } analyticdb for mysql _ _ { "instanceId": "am- sadsada", "database": "xsxsx", "username": "xsxsa", "password": "asdadsa", "connectionString": "am- xssxsxs.ads.aliyuncs.com:3306 " } hybriddb for postgresql _ _ |
|---|---|---|---|---|

DataWorks

|  |  |  |  | { "connectionString": "gp- xsaxsaxa- master.gpdbmaster.rds.aliyunc s.com", "database": "xsaxsaxas", "password": "xsaxsaxsa@11", "instanceId": "gp- xsaxsaxsa", "port": "541132", "ownerId": "xsaxsaxsas", "username": "sadsad" } holo { "accessId": "xsaxsaxs", "accessKey": "xsaxsaxsa", "database": "xsaxsaxsa", "instanceId": "xsaxa", "tag": "aliyun" } kafka { "instanceId": "xsax-cn- xsaxsa", "regionId": "cn-shanghai", "tag": "aliyun", "ownerId": "1212121212112" } |
|---|---|---|---|---|
| EnvType | Integer | 是 | 1 | 数据源所属的环境，包括0（开发环境）和 1（生产环境）。 |
| Name | String | 是 | abc | 数据源的名称。 |
| ProjectId | Long | 是 | 1 | 数据源关联的工作空间ID。您可以通过 ListProjects接口获取工作空间ID。 |

DataWorks

| RegionId | String | 是 | default | 区域ID，为固定值default。 |  |  |
|---|---|---|---|---|---|---|
| Description | String | 否 | abc | 连接串的描述。 |  |  |
| SubType | String | 否 | mysql | 连接串的子类型，针对某些父类型type下包含子类型的场景。目前有以下组合： 父类型： rds 子类型： mysql 、 sqlserver 或 postgresql 。 |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 123 | 数据源ID。 |
| HttpStatusCod e | String | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 **** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
&ConnectionType=rds &Content= {"database":"dbname","instanceName":"instancename","password":"password","rdsOwnerId":"12 ,"username":"username"} &EnvType=1 &Name=abc &ProjectId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc141151593763****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>123</Data> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{"RequestId":"0bc141151593763****","HttpStatusCode":"200","Data":"123","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### CreateProjectMember

调用CreateProjectMember，添加一个用户至Dataworks工作空间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateProjectMe mber | 系统规定参数。取值： CreateProjectMember。 |
| ProjectId | Long | 是 | 27 | Dataworks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| UserId | String | 是 | 1234 | 待添加的用户ID。 |
| ClientToken | String | 否 | 1AFAE64E- D1BE-432B- A9**** | 幂等串，建议使用UUID。 |
| RoleCode | String | 否 | role project gue _ _ st | 角色code，非必填，当不为空，则用户一并添加到此角色中 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AFAE64E-D1BE- 432B-A9**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateProjectMember &ProjectId=27 &RegionId=default &UserId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>1AFAE64E-D1BE-432B-A9****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "1AFAE64E-D1BE-432B-A9****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
| 400 | Invalid.Tenant.User AlreadyInProject | The user already exists in the project. | 待添加用户已经存在于工作空间中。 |
| 400 | Invalid.Tenant.User NotInTenant | The user is not in the tenant. | 待添加成员不在租户中。 |

DataWorks

#### CreateDataSource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDataSour ce | 系统规定参数。取值： CreateDataSource。 |
|  |  |  |  | 数据源的详细信息。部分常用数据源样例如下： odps { "accessId": "xssssss", "accessKey": "xsaxsaxsa", "authType": 2, "endpoint": "http://service.odps.aliyun.c om/api", "project": "xsaxsax", "tag": "public" } mysql { "database": "xsaxsa", "instanceName": "rm- xsaxsa", "password": "xsaxsa", "rdsOwnerId": "xasxsa", "regionId": "cn-shanghai", "tag": "rds", "username": "xsaxsa" } rds |

DataWorks

|  |  |  |  | { "configType": 1, "tag": "rds", "database": "xsaxsa", "username": "xsaxsa", "password": "xssaxsa$32050", "instanceName": "rm- xsaxs", "rdsOwnerId": "11111111" } oss { "accessId": "sssssxx", "accessKey": "xsaxaxsaxs", "bucket": "xsa-xs-xs", "endpoint": "http://oss- cn-shanghai.aliyuncs.com", "tag": "public" } sqlserver { "jdbcUrl": |
|---|---|---|---|---|
|  |  |  |  | "jdbc:sqlserver://xsaxsa- xsaxsa.database.xxx.cn:123;Da tabaseName=xsxs-xsxs", "password": "sdasda$fs", "tag": "public", "username": "sxaxacdacdd" } polardb { "clusterId": "pc- sdadsadsa", "database": "dsadsadsa", "ownerId": "121212122", "password": "sdasdafssa", "region": "cn-shanghai", "tag": "polardb", "username": "asdadsads" } oracle |

DataWorks

| Content | String | 是 | {"database":"db name","instance Name":"instance name","passwor d":"password","r dsOwnerId":"12 3","username":" username"} | { "jdbcUrl": "jdbc:oracle:saaa:@xxxxx:1521 :PROD", "password": "sxasaxsa", "tag": "public", "username": "sasfadfa" } mongodb { "address": " [\"xsaxxsa.mongodb.rds.aliyun cs.com:3717\"]", "database": "admin", "password": "sadsda@", "tag": "public", "username": "dsadsadas" } emr { "accessId": "xsaxsa", "emrClusterId": "C-dsads", "emrResourceQueueName": "default", "emrEndpoint": "emr.aliyuncs.com", "accessKey": "dsadsad", "emrUserId": "224833315798889783", "name": "sasdsadsa", "emrAccessMode": "simple", "region": "cn-shanghai", "authType": "2", "emrProjectId": "FP- sdadsad" } postgresql |
|---|---|---|---|---|

DataWorks

|  |  |  |  | { "jdbcUrl": "jdbc:postgresql://xxxx:1921/ ssss", "password": "sdadsads", "tag": "public", "username": "sdsasda" } analyticdb for mysql _ _ { "instanceId": "am- sadsada", "database": "xsxsx", "username": "xsxsa", "password": "asdadsa", "connectionString": "am- xssxsxs.ads.aliyuncs.com:3306 " } hybriddb for postgresql _ _ { "connectionString": "gp- xsaxsaxa- master.gpdbmaster.rds.aliyunc s.com", "database": "xsaxsaxas", "password": "xsaxsaxsa@11", "instanceId": "gp- xsaxsaxsa", "port": "541132", "ownerId": "xsaxsaxsas", "username": "sadsad" } holo { "accessId": "xsaxsaxs", "accessKey": "xsaxsaxsa", "database": "xsaxsaxsa", "instanceId": "xsaxa", "tag": "aliyun" } |
|---|---|---|---|---|

DataWorks

|  |  |  |  | kafka { "instanceId": "xsax-cn- xsaxsa", "regionId": "cn-shanghai", "tag": "aliyun", "ownerId": "1212121212112" } |
|---|---|---|---|---|
| DataSourceType | String | 是 | rds | 数据源的类型。常用类型如下： odps mysql rds oss sqlserver polardb oracle mongodb emr postgresql analyticdb for mysql _ _ hybriddb for postgresql _ _ holo |
| EnvType | Integer | 是 | 1 | 数据源所属的环境，包括0（开发环境）和 1（生产环境）。 |
| Name | String | 是 | abc | 数据源的名称。 |
| ProjectId | Long | 是 | 1 | 数据源所在的DataWorks工作空间ID。您可以通过ListProjects接口获取工作空间 ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Description | String | 否 | abc | 数据源的描述信息。 |

DataWorks

| SubType | String | 否 | mysql | 数据源的子类型。仅当DataSourceType 参数配置为rds时，该参数生效。 当DataSourceType参数配置为rds时， 该参数可以配置为mysql、sqlserver或 postgresql。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 123 | 数据源ID。 |
| HttpStatusCod e | String | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 **** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
&Content= {"database":"dbname","instanceName":"instancename","password":"password","rdsOwnerId":"12 ,"username":"username"} &DataSourceType=rds &EnvType=1 &Name=abc &ProjectId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc141151593763****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>123</Data> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc141151593763****",
    "HttpStatusCode": 200,
    "Data": 123,
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
| 400 | ConnectionAlready Exist | The connection with envType %s and name %s already exists. | 连接串名称重复 |
| 400 | DataSource.Check RamRoleFailure | Failed to check the RAM role. AccountId %s. roleArn %s. | 校验数据源权限失败 |
| 400 | DataSource.Conne ctionStrProperty.Pa tternNotMatch | The pattern value %s is invalid. The correct pattern is %s. | 数据源连接串属性不匹配规则 |
| 400 | Invalid.DataSource. DataSourceTypeNo tSupport | The dataSourceType %s and subType %s are not supported. | 数据源类型暂不支持 |
| 400 | MissingParam.Conn ectionStr.Property | You must specify property %s required by the data source connection string. | 数据源连接串信息必填属性缺失 |
| 400 | Invalid.DataSource. DataSourceTypeNo tExist | The data source type %s does not exist. | 数据源类型不存在。 |

#### DeleteConnection

**请求参数**

DataWorks

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteConnectio n | 系统规定参数。取值： DeleteConnection。 |
| ConnectionId | Long | 是 | 1 | 数据源ID，您可以调用listConnection获取数据源的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否成功删除。 |
| HttpStatusCod e | String | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 5**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&ConnectionId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937635****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <Success>true</Success>
```

`JSON` 格式

```json
{"RequestId":"0bc1411515937635****","HttpStatusCode":"200","Data":"true","Success":"true"
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### DeleteProjectMember

调用DeleteProjectMember，从DataWorks工作空间移除用户。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteProjectMe mber | 系统规定参数。取值： DeleteProjectMember。 |
| ProjectId | Long | 是 | 27 | Dataworks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| UserId | String | 是 | 1234 | 用户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AFAE64E-D1BE- 432B-A9**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteProjectMember &ProjectId=27 &RegionId=default &UserId=1234
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>1AFAE64E-D1BE-432B-A9****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "1AFAE64E-D1BE-432B-A9****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
| 400 | Invalid.Tenant.User AlreadyInProject | The user already exists in the project. | 待添加用户已经存在于工作空间中。 |
| 400 | Invalid.Tenant.User NotInTenant | The user is not in the tenant. | 待添加成员不在租户中。 |

#### DeleteDataSource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDataSour ce | 系统规定参数。取值： DeleteDataSource。 |
| DataSourceId | Long | 是 | 1 | 数据源ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 请求是否成功。 |
| HttpStatusCod e | String | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 5**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&DataSourceId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937635****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1411515937635****",
    "HttpStatusCode": 200,
    "Data": true,
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |

DataWorks

| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
|---|---|---|---|
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
| 400 | Invalid.Operation | You cannot delete the bindingCalcEngine that is bound to the data source. | 数据源绑定的计算引擎不允许删除 |

#### GetProject

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetProject | 系统规定参数。取值：GetProject。 |
| ProjectId | Long | 是 | 27 | DataWorks工作空间ID。您可以通过 ListProjects接口获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 工作空间的描述信息。 |
| Appkey | String | 0 | 该字段已废弃。 |
| BaseProject | Boolean | false | 该字段已废弃。 |
| DefaultDiReso urceGroupIden tifier | String | group 280749521* _ *** | 购买MaxCompute独享资源组时，默认分配的资源组的标识。 |
| Destination | Integer | 0 | 该字段已废弃。 |
| DevStorageQu ota | String | 0 | 该字段已废弃。 |

DataWorks

| DevelopmentT ype | Integer | 4 | 工作空间的开发类型，目前均为4。该字段已废弃。 |
|---|---|---|---|
| DisableDevelo pment | Boolean | true | 是否禁用开发角色，取值如下： 0，开启开发角色。 1，禁用开发角色。 默认取值为0。 |
| EnvTypes | List | ["PROD"] | 工作空间包含的环境： 简单模式只有生产环境（PROD）。 标准模式包含开发环境（DEV）和生产环境 （PROD）。 |
| GmtCreate | String | Oct 10, 2019 3:42:53 PM | 创建工作空间时间，示例格式Dec 3, 2019 9:12:20 PM。 |
| GmtModified | String | Dec 3, 2019 9:12:20 PM | 修改工作空间的时间，示例格式为Dec 3, 2019 9:12:20 PM。 |
| IsAllowDownlo ad | Integer | 1 | 是否允许下载ide上查询的结果，取值如下： 1，允许下载。 0，不允许下载。 |
| IsDefault | Integer | 1 | 是否为默认工作空间，取值如下： 1，是。 0，否。 |
| MaxFlowNode | Integer | 1 | 该字段已废弃。 |
| ProdStorageQ uota | String | 1 | 该字段已废弃。 |
| ProjectDescrip tion | String | abc | 工作空间的描述。 |
| ProjectId | Integer | 27 | 工作空间的ID。 |
| ProjectIdentifi er | String | abc | 工作空间的标识。 |
| ProjectMode | Integer | 2 | 工作空间的模式，取值如下： 2，表示简单工作空间模式。 3，表示标准工作空间模式。 |

DataWorks

| ProjectName | String | abc | 工作空间的显示名称。 |
|---|---|---|---|
| ProjectOwnerB aseId | String | 18229311**** | 工作空间所有者的阿里云ID。 |
| ProtectedMod e | Integer | 1 | 工作空间是否开启了保护模式，取值如下： 1，开启保护模式。 0，未开启保护模式。 |
| ResidentArea | String | private | 工作空间的类型，private为私有区，swap为交换区。 |
| SchedulerMax RetryTimes | Integer | 3 | 默认出错自动重跑的次数。 |
| SchedulerRetr yInterval | Integer | 120000 | 默认出错自动重跑的时间间隔，单位为ms。取值最大为30分钟，注意单位转换。 |
| Status | Integer | 0 | 工作空间的状态，取值如下： AVAILABLE(0)，工作空间运行正常。 DELETED(1)，工作空间已被删除。 INITIALIZING(2)，初始化工作空间。 INIT FAILED(3)，工作空间初始化失败。 _ FORBIDDEN(4)，手动禁用工作空间。 DELETING(5)，正在删除工作空间。 DEL FAILED(6)，工作空间删除失败。 _ FROZEN(7)，工作空间欠费冻结。 UPDATING(8)，更新工作空间（为工作空间添加并初始化计算引擎）。 UPDATE FAILED(9)，更新工作空间（为工 _ 作空间添加并初始化计算引擎）失败。 |
| TablePrivacyM ode | Integer | 1 | MaxCompute表的可见性权限，取值如下： 0，租户内用户不可见MaxCompute表。 1，租户内用户可见MaxCompute表。 |
| TenantId | Long | 280749521 | 租户ID。 |
| UseProxyOdps Account | Boolean | true | 访问MaxCompute引擎是否使用代理账号。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 5973**** | 请求的ID。用于定位日志，排查问题。 |

DataWorks

| Success | Boolean | true | 是否成功查询工作空间的信息。 |
|---|---|---|---|

**示例**

请求示例

```
&ProjectId=27 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937635973****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <ProjectOwnerBaseId>18229311****</ProjectOwnerBaseId>
    <Destination>0</Destination>
    <ProjectName>abc</ProjectName>
    <IsAllowDownload>1</IsAllowDownload>
    <DevelopmentType>4</DevelopmentType>
    <GmtModified>Dec 3, 2019 9:12:20 PM</GmtModified>
    <DisableDevelopment>true</DisableDevelopment>
    <BaseProject>false</BaseProject>
    <ProjectDescription>abc</ProjectDescription>
    <ProjectMode>2</ProjectMode>
    <Status>0</Status>
    <ProjectIdentifier>abc</ProjectIdentifier>
    <IsDefault>1</IsDefault>
    <DevStorageQuota>0</DevStorageQuota>
    <SchedulerMaxRetryTimes>3</SchedulerMaxRetryTimes>
    <ProjectId>27</ProjectId>
    <ResidentArea>private</ResidentArea>
    <UseProxyOdpsAccount>true</UseProxyOdpsAccount>
    <TenantId>280749521</TenantId>
    <GmtCreate>Oct 10, 2019 3:42:53 PM</GmtCreate>
    <MaxFlowNode>1</MaxFlowNode>
    <ProtectedMode>1</ProtectedMode>
    <Appkey>0</Appkey>
    <TablePrivacyMode>1</TablePrivacyMode>
    <ProdStorageQuota>1</ProdStorageQuota>
    <DefaultDiResourceGroupIdentifier>group_280749521****
</DefaultDiResourceGroupIdentifier>
    <SchedulerRetryInterval>120000</SchedulerRetryInterval>
    <EnvTypes>["PROD"]</EnvTypes>
</Data> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1411515937635973****",
    "HttpStatusCode": 200,
    "Data": {
        "ProjectOwnerBaseId": "18229311****",
        "Destination": 0,
        "ProjectName": "abc",
        "IsAllowDownload": 1,
        "DevelopmentType": 4,
        "GmtModified": "Dec 3, 2019 9:12:20 PM",
        "DisableDevelopment": true,
        "BaseProject": false,
        "ProjectDescription": "abc",
        "ProjectMode": 2,
        "Status": 0,
        "ProjectIdentifier": "abc",
        "IsDefault": 1,
        "DevStorageQuota": 0,
        "SchedulerMaxRetryTimes": 3,
        "ProjectId": 27,
        "ResidentArea": "private",
        "UseProxyOdpsAccount": true,
        "TenantId": 280749521,
        "GmtCreate": "Oct 10, 2019 3:42:53 PM",
        "MaxFlowNode": 1,
        "ProtectedMode": 1,
        "Appkey": 0,
        "TablePrivacyMode": 1,
        "ProdStorageQuota": 1,
        "DefaultDiResourceGroupIdentifier": "group_280749521****",
        "SchedulerRetryInterval": 120000,
        "EnvTypes": "[\"PROD\"]"
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |

DataWorks

| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
|---|---|---|---|

#### GetProjectDetail

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetProjectDetail | 系统规定参数。取值： GetProjectDetail。 |
| ProjectId | Long | 是 | 27 | DataWorks工作空间ID。您可以通过 ListProjects接口获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 工作空间的描述信息。 |
| DefaultDiReso urceGroupIden tifier | String | group 280749521* _ *** | 购买MaxCompute独享资源组时，默认分配的资源组的标识。 |
| DevelopmentT ype | Integer | 4 | 工作空间的开发类型，目前均为4。该字段已废弃。 |
| EnvTypes | List | ["PROD"] | 工作空间包含的环境： 简单模式只有生产环境（PROD）。 标准模式包含开发环境（DEV）和生产环境 （PROD）。 |
| GmtCreate | String | Oct 10, 2019 3:42:53 PM | 创建工作空间时间，示例格式Dec 3, 2019 9:12:20 PM。 |
| GmtModified | String | Dec 3, 2019 9:12:20 PM | 修改工作空间的时间，示例格式为Dec 3, 2019 9:12:20 PM。 |

DataWorks

| IsAllowDownlo ad | Integer | 1 | 是否允许下载ide上查询的结果，取值如下： 1：允许下载。 0：不允许下载。 |
|---|---|---|---|
| ProjectDescrip tion | String | abc | 工作空间的描述。 |
| ProjectId | Integer | 27 | 工作空间的ID。 |
| ProjectIdentifi er | String | abc | 工作空间的标识。 |
| ProjectMode | Integer | 2 | 工作空间的模式，取值如下： 2：表示简单工作空间模式。 3：表示标准工作空间模式。 |
| ProjectName | String | abc | 工作空间的显示名称。 |
| ProjectOwnerB aseId | String | 18229311**** | 工作空间所有者的阿里云ID。 |
| ProtectedMod e | Integer | 1 | 工作空间是否开启了保护模式，取值如下： 1：开启保护模式。 0：未开启保护模式。 |
| ResidentArea | String | private | 工作空间的类型，private为私有区，swap为交换区。 |
| SchedulerMax RetryTimes | Integer | 3 | 默认出错自动重跑的次数。 |
| SchedulerRetr yInterval | Integer | 120000 | 默认出错自动重跑的时间间隔，单位为ms。取值最大为30分钟，注意单位转换。 |
| Status | Integer | 0 | 工作空间的状态，取值如下： AVAILABLE(0)，工作空间运行正常。 DELETED(1)，工作空间已被删除。 INITIALIZING(2)，初始化工作空间。 INIT FAILED(3)，工作空间初始化失败。 _ FORBIDDEN(4)，手动禁用工作空间。 DELETING(5)，正在删除工作空间。 DEL FAILED(6)，工作空间删除失败。 _ FROZEN(7)，工作空间欠费冻结。 UPDATING(8)，更新工作空间（为工作空间添加并初始化计算引擎）。 UPDATE FAILED(9)，更新工作空间（为工 _ 作空间添加并初始化计算引擎）失败。 |

DataWorks

| TenantId | Long | 280749521 | 租户ID。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 5973**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 是否成功查询工作空间的信息。 |

**示例**

请求示例

```
&ProjectId=27 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937635973****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Status>0</Status>
    <ProjectIdentifier>abc</ProjectIdentifier>
    <ProjectOwnerBaseId>18229311****</ProjectOwnerBaseId>
    <SchedulerMaxRetryTimes>3</SchedulerMaxRetryTimes>
    <ProjectName>abc</ProjectName>
    <IsAllowDownload>1</IsAllowDownload>
    <DevelopmentType>4</DevelopmentType>
    <ProjectId>27</ProjectId>
    <GmtModified>Dec 3, 2019 9:12:20 PM</GmtModified>
    <ResidentArea>private</ResidentArea>
    <TenantId>280749521</TenantId>
    <GmtCreate>Oct 10, 2019 3:42:53 PM</GmtCreate>
    <ProtectedMode>1</ProtectedMode>
    <ProjectDescription>abc</ProjectDescription>
    <ProjectMode>2</ProjectMode>
    <DefaultDiResourceGroupIdentifier>group_280749521****
</DefaultDiResourceGroupIdentifier>
    <SchedulerRetryInterval>120000</SchedulerRetryInterval>
    <EnvTypes>["PROD"]</EnvTypes>
</Data> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1411515937635973****",
    "HttpStatusCode": 200,
    "Data": {
        "Status": 0,
        "ProjectIdentifier": "abc",
        "ProjectOwnerBaseId": "18229311****",
        "SchedulerMaxRetryTimes": 3,
        "ProjectName": "abc",
        "IsAllowDownload": 1,
        "DevelopmentType": 4,
        "ProjectId": 27,
        "GmtModified": "Dec 3, 2019 9:12:20 PM",
        "ResidentArea": "private",
        "TenantId": 280749521,
        "GmtCreate": "Oct 10, 2019 3:42:53 PM",
        "ProtectedMode": 1,
        "ProjectDescription": "abc",
        "ProjectMode": 2,
        "DefaultDiResourceGroupIdentifier": "group_280749521****",
        "SchedulerRetryInterval": 120000,
        "EnvTypes": "[\"PROD\"]"
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### ListDataSources

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | ListDataSources | 系统规定参数。取值： ListDataSources。 |
|---|---|---|---|---|
| Name | String | 是 | 查询的数据源名称。 | 查询的数据源名称。 |
| ProjectId | Long | 是 | 1 | 数据源所在的DataWorks工作空间ID。您可以通过ListProjects接口获取工作空间 ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| DataSourceType | String | 否 | rds | 数据源的类型。常用的类型如下： odps mysql rds oss sqlserver polardb oracle mongodb emr postgresql analyticdb for mysql _ _ hybriddb for postgresql _ _ holo |
| SubType | String | 否 | mysql | 数据源的子类型。仅当DataSourceType 参数配置为RDS时，该参数生效。 当DataSourceType参数配置为RDS时， 该参数可以配置为mysql、sqlserver或 postgresql。 |
| Status | String | 否 | mysql | 数据源的状态。取值如下： ENABLED，正常。 DISABLED，禁用。 |
| EnvType | Integer | 否 | 1 | 数据源所属的环境，包括0（开发环境）和 1（生产环境）。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大为 100条。 |
| PageNumber | Integer | 否 | 1 | 分页查询的页码。取值为大于等于1的正整数。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 数据源的查询结果。 |
| DataSources | Array of DataSources |  | 数据源列表。 |
| BindingCalcEn gineId | Integer | 123 | 数据源关联的计算引擎ID。 |
| ConnectStatus | Integer | 1 | 数据源的状态。取值如下： 1，表示数据源正常使用。 2，表示数据源已禁用。 |
|  |  |  | 数据连接串的相关信息。格式为JSON格式。常用的数据源对应的连接串样例如下： MaxCompute json { "pubEndpoint": "http://service.cn.maxcompute.aliy un.com/api", "accessId": "xxxxxxx", "securityToken": null, "endpoint": "http://service.cn.maxcompute.aliy un-inc.com/api", "accessKey": "***", "name": "PRE PROJECT A engine", _ _ _ "project": "PRE PROJECT A", _ _ "vpcEndpoint": "http://service.cn.maxcompute.aliy un-inc.com/api", "region": "cn-shanghai", "authType": "2" } mysql json { "configType": "1", "database": "mysql d111b", _ "instanceName": "rm-xxxxxx", "password": "***", "rdsOwnerId": "12133xxxxxx", "tag": "rds", "username": "mysql db111" _ } |

DataWorks

| Content | String | {"pubEndpoint":"ht tp://service.cn.max compute.aliyun.co m/api","accessId":" TMP.3KecGjvzy3i8 MYfn2BGHgF7EHG yBFZcHm7GgngrA BVRyvvKQrfF5kskR 36xP361C3dqwbGo 7SGYptAeGyiTwHX qLaBUvYC","securit yToken":null,"endp oint":"http://service .cn.maxcompute.al iyun- inc.com/api","acce ssKey":"***","name ":"PRE PROJECT A _ _ _ engine","project":" PRE PROJECT A","v _ _ pcEndpoint":"http:/ /service.cn.maxco mpute.aliyun- | sqlserver json { "configType": "1", "jdbcUrl": "jdbc:sqlserver://rm- xxxxx.sqlserver.rds.aliyuncs.com:1 433;DatabaseName=sqlserver db1", _ "password": "***", "tag": "public", "username": "sqlserver db111" _ } oss json { "accessId": "LTAINbR9Uxxxx", "accessKey": "***", "bucket": "bigxxx1223", "configType": "1", "endpoint": "http://oss-cn- hangzhou.aliyuncs.com", "tag": "public" |
|---|---|---|---|
|  |  | inc.com/api","regio n":"cn- shanghai","authTy pe":"2"} | } postgresql json { "configType": "1", "database": "cdp xxx", _ "instanceName": "rm-xxxx", "password": "***", "rdsOwnerId": "121xxxxx", "tag": "rds", "username": "cdp xxx" _ } redis json { "address": "[{\"host\":\"r- xxxx.redis.rds.aliyuncs.com\",\"po rt\":6379}]", "aliyunKp": "12xxxx", "password": "***", "tag": "public" } ads |

DataWorks

|  |  |  | json { "configType": "1", "password": "***", "schema": "ads demo", _ "tag": "public", "url": "ads-xxx-xxxx.cn- hangzhou- 1.ads.aliyuncs.com:3029", "username": "lslslsls" } |
|---|---|---|---|
| DataSourceTy pe | String | rds | 数据源的类型。常用类型如下： odps mysql rds oss sqlserver polardb oracle mongodb emr postgresql analyticdb for mysql _ _ hybriddb for postgresql _ _ holo |
| DefaultEngine | Boolean | false | 数据源关联的引擎是否为同类型数据源选用的默认引擎。 |
| Description | String | a connection | 数据源的描述信息。 |
| EnvType | Integer | 1 | 数据源所在的环境。取值如下： 0，开发环境。 1，生产环境。 |
| GmtCreate | String | Mar 17, 2021 4:09:32 PM | 创建数据源的时间。时间格式示例为Mar 17, 2021 4:09:32 PM。 |
| GmtModified | String | Mar 17, 2021 4:09:32 PM | 修改数据源的时间。时间格式示例为Mar 17, 2021 4:09:32 PM。 |

DataWorks

| Id | Integer | 1 | 数据源ID。 |
|---|---|---|---|
| Name | String | abc | 数据源的名称。 |
| Operator | String | 193543050**** | 最近一次修改数据源的阿里云用户ID。 |
| ProjectId | Integer | 123 | 数据源关联的工作空间ID。 |
| Sequence | Integer | 300 | 排序字段。数据源按此字段从大到小排序。 |
| Shared | Boolean | false | 是否为共享的数据源。 |
| Status | Integer | 1 | 数据源的状态。取值如下： 1，表示数据源正常使用。 2，表示数据源已禁用。 |
| SubType | String | mysql | 数据源的子类型。仅当DataSourceType参数配置为RDS时，该参数生效。 当DataSourceType参数配置为RDS时，该参数可以配置为mysql、sqlserver或postgresql。 |
| TenantId | Long | 1234567 | 租户ID。 |
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 100 | 每页显示的条数，默认为10条，最大为100条。 |
| TotalCount | Integer | 233 | 数据源的总数。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 59**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 DataWorks `&Name=`查询的数据源名称。

```
&ProjectId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```json
<RequestId>0bc14115159376359****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>233</TotalCount>
    <PageSize>100</PageSize>
    <PageNumber>1</PageNumber>
    <DataSources>
        <Status>1</Status>
        <Operator>193543050****</Operator>
        <ConnectStatus>1</ConnectStatus>
        <SubType>mysql</SubType>
        <Description>a connection</Description>
        <BindingCalcEngineId>123</BindingCalcEngineId>
        <ProjectId>123</ProjectId>
        <GmtModified>Mar 17, 2021 4:09:32 PM</GmtModified>
        <Sequence>300</Sequence>
        <Shared>false</Shared>
        <EnvType>1</EnvType>
        <Name>abc</Name>
        <DefaultEngine>false</DefaultEngine>
        <TenantId>1234567</TenantId>
        <GmtCreate>Mar 17, 2021 4:09:32 PM</GmtCreate>
        <Content>
{"pubEndpoint":"http://service.cn.maxcompute.aliyun.com/api","accessId":"TMP.3KecGjvzy3i8 fn2BGHgF7EHGyBFZcHm7GgngrABVRyvvKQrfF5kskR36xP361C3dqwbGo7SGYptAeGyiTwHXqLaBUvYC","securi Token":null,"endpoint":"http://service.cn.maxcompute.aliyuninc.com/api","accessKey":"***","name":"PRE_PROJECT_A_engine","project":"PRE_PROJECT_A","v Endpoint":"http://service.cn.maxcompute.aliyun-inc.com/api","region":"cnshanghai","authType":"2"}</Content>
        <DataSourceType>rds</DataSourceType>
        <Id>1</Id>
    </DataSources>
</Data> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc14115159376359****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 233,
        "PageSize": 100,
        "PageNumber": 1,
        "DataSources": {
            "Status": 1,
            "Operator": "193543050****",
            "ConnectStatus": 1,
            "SubType": "mysql",
            "Description": "a connection",
            "BindingCalcEngineId": 123,
            "ProjectId": 123,
            "GmtModified": "Mar 17, 2021 4:09:32 PM",
            "Sequence": 300,
            "Shared": false,
            "EnvType": 1,
            "Name": "abc",
            "DefaultEngine": false,
            "TenantId": 1234567,
            "GmtCreate": "Mar 17, 2021 4:09:32 PM",
            "Content": "
{\"pubEndpoint\":\"http://service.cn.maxcompute.aliyun.com/api\",\"accessId\":\"TMP.3KecG zy3i8MYfn2BGHgF7EHGyBFZcHm7GgngrABVRyvvKQrfF5kskR36xP361C3dqwbGo7SGYptAeGyiTwHXqLaBUvYC\" "securityToken\":null,\"endpoint\":\"http://service.cn.maxcompute.aliyuninc.com/api\",\"accessKey\":\"***\",\"name\":\"PRE_PROJECT_A_engine\",\"project\":\"PRE_P JECT_A\",\"vpcEndpoint\":\"http://service.cn.maxcompute.aliyuninc.com/api\",\"region\":\"cn-shanghai\",\"authType\":\"2\"}",
            "DataSourceType": "rds",
            "Id": 1
        }
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |

DataWorks

| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
|---|---|---|---|

#### ListCalcEngines

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListCalcEngines | 系统规定参数。取值： ListCalcEngines。 |
| CalcEngineType | String | 是 | ODPS | 计算引擎类型。目前支持ODPS、EMR、 BLINK、HOLO、MaxGraph、 HYBRIDDB FOR POSTGRESQL、 _ _ ADB MYSQL、HADOOP CDH，不区分 _ _ 大小写。 |
| Name | String | 是 | abc | 查询的计算引擎名称，精确匹配。 |
| ProjectId | Long | 是 | 27 | 计算引擎所属的Dataworks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| EnvType | String | 否 | PRD | 计算引擎所属的环境，包括开发环境 （DEV）和生产环境（PRD）。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大20 条。 |
| PageNumber | Integer | 否 | 1 | 分页查询页码。大于等于1的正整数，默认为1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 计算引擎的分页查询结果。 |
| CalcEngines | Array of CalcEngines |  | 计算引擎列表。 |
| BindingProjectI d | Integer | 27 | 计算引擎绑定的工作空间ID。 |

DataWorks

|  |  | BindingProject Name |  | String |  |  | abc |  | 计算引擎关联的工作空间名称。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | CalcEngineTyp e |  | String |  |  | ODPS |  | 计算引擎类型。值枚举列表 ODPSEMRBLINKHOLOMaxGraphHYBRIDDB FOR POSTGRESQLADB MYSQLHADOOP C _ _ _ _ DH |  |  |  |  |
|  |  | DwRegion |  | String |  |  | cn-zhangjiakou |  | 计算引擎关联的Dataworks工作空间所在的地域。 |  |  |  |  |
|  |  | EngineId |  | Integer |  |  | 35 |  | 计算引擎ID。 |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 计算引擎的详细信息。 ODPS { "pubEndpoint": |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | { |  |
|  |  |  |  |  |  |  |  |  |  | "pubEndpoint": |  |  |  |
|  |  |  |  |  |  |  |  |  | "service.cn.maxcompute.aliyun.com/a |  |  |  |  |
|  |  |  |  |  |  |  |  |  | pi", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "endpoint": |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "service.cn.maxcompute.aliyun- |  |  |  |  |
|  |  |  |  |  |  |  |  |  | inc.com/api", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "resourceGroupType": "ODPS", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "resourceGroupId": |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "361826516****", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "vpcEndpoint": |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "service.cn.maxcompute.aliyun- |  |  |  |  |
|  |  |  |  |  |  |  |  |  | inc.com/api", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "projectName": |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "onefall test zjk", _ _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "taskSameAsOwner": "true" |  |  |  |  |
|  |  |  |  |  |  |  |  |  | } |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | { |  |  |
|  |  |  |  |  |  |  |  |  |  | "emrClusterId": "C-xxx", |  |  |  |
|  |  |  |  |  |  |  |  |  | "specs": " |  |  |  |  |
|  |  |  |  |  |  |  |  |  | {\"emrClusterId\":\"C- |  |  |  |  |
|  |  |  |  |  |  |  |  |  | xxx\",\"emrAccessMode\":\"simple\", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | \"emrResourceQueueName\":\"default\ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | ",\"emrProjectId\":\"FP-xxx\"}", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "endpoint": "emr.aliyuncs.com", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "emrResourceQueueName": |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "default", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "emrAccessMode": "simple", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "resourceGroupType": "DW", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "projectName": "xx-xxxx", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "emrProjectId": "FP-xxxx", |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "taskSameAsOwner": "false" |  |  |  |  |
|  |  |  |  |  |  |  |  |  | } |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | { |  |
|  |  |  |  |  |  |  |  |  |  | "bayesProjectId": "xxxx", |  |  |  |
|  |  |  |  |  |  |  |  |  | "bayesProjectName": |  |  |  |  |

DataWorks

|  |  |  |  |  |  | "xc blxxixxxnk 1", _ _ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | "cluster": "xxxssxsx", |  |  |  |
|  |  |  |  |  |  | "endpoint": |  |  |  |
|  |  |  |  |  |  | "https://stream.console.aliyun.com" |  |  |  |
|  |  |  |  |  |  | , |  |  |  |
|  |  |  |  |  |  | "engineType": "BLINK", |  |  |  |
|  |  |  |  |  |  | "name": "xsxsxxxxx", |  |  |  |
|  |  |  |  |  |  | "projectName": |  |  |  |
|  |  |  |  |  |  | "xc blxxxsxink 1", _ _ |  |  |  |
|  |  |  |  |  |  | "queue": |  |  |  |
|  |  |  |  |  |  | "root.xc blxsxxxxxxink 1", _ _ |  |  |  |
|  |  |  |  |  |  | "resourceGroupType": "DW", |  |  |  |
|  |  |  |  |  |  | "specs": " |  |  |  |
|  |  |  |  |  |  | {\"cluster\":\"xxxxxx\",\"bayesProj |  |  |  |
|  |  |  |  |  |  | ectName\":\"xc blxxixxxnk 1\",\"bay _ _ |  |  |  |
|  |  |  |  |  |  | esProjectId\":\"ssxxxsa\",\"name\": |  |  |  |
|  |  |  |  |  |  | \"sxsxsxxx\",\"queue\":\"root.sxxsx |  |  |  |
|  |  |  |  |  |  | xsx\"}", |  |  |  |
|  |  |  |  |  |  | "taskSameAsOwner": false |  |  |  |
|  |  |  |  |  |  | } |  |  |  |
|  |  |  |  |  |  |  |  | { |  |
|  |  |  |  |  |  |  | "endpoint": "hgprecn-cn- |  |  |
|  |  |  |  |  |  | xsxssxsx-cn-shanghai- |  |  |  |
|  |  |  |  |  |  | internal.hologres.aliyuncs.com:80", |  |  |  |
|  |  |  |  |  |  | "engineType": "ODPS", |  |  |  |
|  |  |  |  |  |  | "odpsEndpoint": "hgprecn-cn- |  |  |  |
|  |  |  |  |  |  | xsxssxxs-cn-shanghai- |  |  |  |
|  |  |  |  |  |  | internal.hologres.aliyuncs.com:80", |  |  |  |
|  |  |  |  |  |  | "odpsProjectName": "xsxssxsxsx", |  |  |  |
|  |  |  |  |  |  | "projectName": "xsxssxsxsx", |  |  |  |
|  |  |  |  |  |  | "resourceGroupType": "DW", |  |  |  |
|  |  |  |  |  |  | "specs": " |  |  |  |
|  |  |  |  |  |  | {\"pubEndpoint\":\"hgprecn-cn- |  |  |  |
|  |  |  |  |  |  | xsxssxsxs-cn- |  |  |  |
|  |  |  |  |  |  | shanghai.hologres.aliyuncs.com:80\" |  |  |  |
|  |  |  |  |  |  | ,\"commonBuyInstanceId\":\"hgprecn- |  |  |  |
|  |  |  |  |  |  | cn- |  |  |  |
|  |  |  |  |  |  | xsxsxsxs\",\"project\":\"holo upxsx _ |  |  |  |
|  |  |  |  |  |  | grade1\",\"common buy instance id\" _ _ _ |  |  |  |
|  |  |  |  |  |  | :\"hgprecn-cn- |  |  |  |
|  |  |  |  |  |  | xsxsxs\",\"endpoint\":\"hgprecn- |  |  |  |
|  |  |  |  |  |  | cn-xsxxsxs-cn-shanghai- |  |  |  |
|  |  |  |  |  |  | internal.hologres.aliyuncs.com:80\" |  |  |  |
|  |  |  |  |  |  | ,\"port\":\"80\",\"host\":\"hgprecn |  |  |  |
|  |  |  |  |  |  | -cn-xsxsxsxs-cn-shanghai- |  |  |  |
|  |  |  |  |  |  | internal.hologres.aliyuncs.com\",\" |  |  |  |
|  |  |  |  |  |  | vpcEndpoint\":\"hgprecn-cn- |  |  |  |
|  |  |  |  |  |  | xsxsxsxs-cn-shanghai- |  |  |  |
|  |  |  |  |  |  | vpc.hologres.aliyuncs.com:80\",\"au |  |  |  |
|  |  |  |  |  |  | thType\":2,\"region\":\"cn- |  |  |  |
|  |  |  |  |  |  | shanghai\"}", |  |  |  |

DataWorks

|  |  |  |  |  |  |  |  |  |  | "taskSameAsOwner": false } MaxGraph { "endpoint": "http://pre- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | "taskSameAsOwner": false |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | } |  |  |  |  |  |
|  |  |  |  |  |  |  |  | {"pubEndpoint":"ht |  |  |  | { |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | "endpoint": "http://pre- |  |  |  |  |
|  |  |  |  |  |  |  |  | tp://service.cn.max |  | graphcompute.aliyuncs.com", |  |  |  |  |  |
|  |  |  |  |  |  |  |  | compute.aliyun.co |  | "engineType": "ODPS", |  |  |  |  |  |
|  |  |  |  |  |  |  |  | m/api","endpoint":" |  | "odpsEndpoint": "http://pre- |  |  |  |  |  |
|  |  |  |  |  |  |  |  | http://service.cn.m |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | axcompute.aliyun- |  | graphcompute.aliyuncs.com", |  |  |  |  |  |
|  |  |  |  |  |  |  |  | inc.com/api","resou |  | "odpsProjectName": "xsxsxsxs", |  |  |  |  |  |
|  |  |  |  |  |  |  |  | rceGroupType":"O |  | "projectName": "xsxsxsxs", |  |  |  |  |  |
|  |  |  | EngineInfo |  |  | Map |  | DPS","resourceGro |  | "resourceGroupType": "DW", |  |  |  |  |  |
|  |  |  |  |  |  |  |  | upId":"361826516* |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "taskSameAsOwner": false |  |  |  |  |  |
|  |  |  |  |  |  |  |  | ***","vpcEndpoint": |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | "http://service.cn. |  | } |  |  |  |  |  |
|  |  |  |  |  |  |  |  | maxcompute.aliyu n- inc.com/api","proje ctName":"onefall t |  |  |  |  |  | { |  |
|  |  |  |  |  |  |  |  |  |  |  | _ _ "endpoint": |  |  |  |  |
|  |  |  |  |  |  |  |  |  | e":"onefall t | "hybriddb for postgresql mo12121ck _ _ _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  | _ est zjk","taskSame | _ |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | endpoint", |  |  |  |  |  |
|  |  |  |  |  |  |  |  | _ |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | AsOwner":"true"} |  | "engineType": "ODPS", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "odpsEndpoint": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "hybriddb for postgresql m121212ock _ _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | endpoint", _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "odpsProjectName": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "sxasaxsaxaxas", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "projectName": "sxasaxsaxaxas", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "resourceGroupType": "DW", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "specs": " |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | {\"connectionString\":\"gp- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | xsxsxsxxs.gpdb.rds.aliyuncs.com\",\ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "database\":\"xsxsxxsxs\",\"passwor |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | d\":\"xxxxxxx\",\"instanceId\":\"gp |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | - |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | cdcdacdacda\",\"port\":\"3432\",\"o |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | wnerId\":\"12121212\",\"username\": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | \"sdasaddsa\"}", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "taskSameAsOwner": false |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | } |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | { |  |  |
|  |  |  |  |  |  |  |  |  |  |  | _ "endpoint": |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "adb mysql mock endpoint", _ _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "engineType": "ODPS", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "odpsEndpoint": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "adb mysql mock endpoint", _ _ _ |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "odpsProjectName": "am- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | xsaxaxa", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "projectName": "am-xsxsaxa", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "resourceGroupType": "DW", |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | "specs": " |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | {\"connectionString\":\"am- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | xsaxsa.ads.aliyuncs.com:3306\",\"da |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | tabase\":\"xsaxsaxa\",\"password\": |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | \"xsaxsaxassxsa\",\"instanceId\":\" |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | am- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | xsaxsasx\",\"username\":\"xsaxsadsd |  |  |  |  |  |

DataWorks

|  |  |  |  |  | \"}", "taskSameAsOwner": false } HADOOP CDH { _ "bindingBaseId": "xsaxsaxs", |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  | \"}", |  |  |
|  |  |  |  |  | "taskSameAsOwner": false |  |  |
|  |  |  |  |  | } |  |  |
|  |  |  |  |  |  |  | { |
|  |  |  |  |  |  | _ "bindingBaseId": "xsaxsaxs", |  |
|  |  |  |  |  | "endpoint": "xsaaaaa", |  |  |
|  |  |  |  |  | "engineType": "ODPS", |  |  |
|  |  |  |  |  | "odpsEndpoint": "axsxaxssxs", |  |  |
|  |  |  |  |  | "odpsProjectName": "ssxxax", |  |  |
|  |  |  |  |  | "projectName": "xsaxsaxsa", |  |  |
|  |  |  |  |  | "resourceGroupId": 45208xxxxxx, |  |  |
|  |  |  |  |  | "resourceGroupType": "GATEWAY", |  |  |
|  |  |  |  |  | "specs": "{\"cluster\": |  |  |
|  |  |  |  |  | {\"hive\": |  |  |
|  |  |  |  |  | {\"hiveServer2Url\":\"jdbc:hive2:// |  |  |
|  |  |  |  |  | xxxxxxer-1-cn-shanghai-pre- |  |  |
|  |  |  |  |  | kerberos- |  |  |
|  |  |  |  |  | 1:10000\",\"hiveMetastore\":\"thrif |  |  |
|  |  |  |  |  | t://xxxxxxxr-1-cn-shanghai-pre- |  |  |
|  |  |  |  |  | kerberos- |  |  |
|  |  |  |  |  | 1:9083\",\"version\":\"2.1.1\"},\"c |  |  |
|  |  |  |  |  | onfigFiles\": |  |  |
|  |  |  |  |  | {\"coreSite\":\"4534574xxxxxx\",\"h |  |  |
|  |  |  |  |  | dfsSite\":\"453457919xxxxxxx\",\"ma |  |  |
|  |  |  |  |  | predSite\":\"45345750xxxxxx\",\"yar |  |  |
|  |  |  |  |  | nSite\":\"4534575xxxxx\",\"krb5Conf |  |  |
|  |  |  |  |  | \":\"4534576xxxxx1\",\"hiveSite\":\ |  |  |
|  |  |  |  |  | "453457xxxxx20\"},\"spark\": |  |  |
|  |  |  |  |  | {\"version\":\"2.4.0\"},\"cdh\": |  |  |
|  |  |  |  |  | {\"version\":\"6.3.2\"},\"hdfs\": |  |  |
|  |  |  |  |  | {\"version\":\"3.0.0\"},\"impala\": |  |  |
|  |  |  |  |  | {\"impalaUrl\":\"jdbc:impala://cdh- |  |  |
|  |  |  |  |  | xsxssxxsx-1-cn-shanghai-pre- |  |  |
|  |  |  |  |  | kerberos- |  |  |
|  |  |  |  |  | 1:21050\",\"version\":\"3.2.0\"},\" |  |  |
|  |  |  |  |  | yarn\":{\"YarnUrl\":\"http://cdh- |  |  |
|  |  |  |  |  | xsxsxsxsxs-1-cn-shanghai-pre- |  |  |
|  |  |  |  |  | kerberos- |  |  |
|  |  |  |  |  | 1:8032\",\"webUrl\":\"http://cdh- |  |  |
|  |  |  |  |  | xsxsxssxxssx-1-cn-shanghai-pre- |  |  |
|  |  |  |  |  | kerberos- |  |  |
|  |  |  |  |  | 1:8088\",\"version\":\"3.0.0\"},\"p |  |  |
|  |  |  |  |  | resto\": |  |  |
|  |  |  |  |  | {\"prestoUrl\":\"jdbc:presto://cdh- |  |  |
|  |  |  |  |  | xssxsxxsxsxs-1-cn-shanghai-pre- |  |  |
|  |  |  |  |  | kerberos- |  |  |
|  |  |  |  |  | 1:8080/hive/default\",\"version\":\ |  |  |
|  |  |  |  |  | "0.244.1\"}},\"instanceId\":161sdad |  |  |
|  |  |  |  |  | s733,\"authDetail\": |  |  |
|  |  |  |  |  | {\"principal\":\"hive@HADOOP.COM\", |  |  |
|  |  |  |  |  | \"keytabFileId\":\"45345815xsxsxs3\ |  |  |
|  |  |  |  |  | ",\"type\":\"kerberos\",\"username\ |  |  |
|  |  |  |  |  | ":\"xsxsxsxsa@HADOOP.COM\"},\"resGr |  |  |

DataWorks

|  |  |  | oupStatus\":\"\",\"hadoopAuthType\" |  |
|---|---|---|---|---|
|  |  |  | :\"kerberos\",\"clusterIdentifier\" |  |
|  |  |  | :\"xssxsxsxsx\",\"clusterId\":xsxsx |  |
|  |  |  | ,\"resGroupId\":4520870619xsxssxxs, |  |
|  |  |  | \"accessMode\":\"security\",\"authT |  |
|  |  |  | ype\":2}", |  |
|  |  |  | "taskSameAsOwner": false |  |
|  |  |  | } |  |
| EnvType | String | PRD |  |  |
| GmtCreate | String | Oct 10, 2019 3:42:44 PM | 计算引擎的创建时间。时间戳 |  |
| IsDefault | Boolean | true | 是否为当前类型的默认计算引擎。 |  |
| Name | String | abc | 计算引擎的显示名称。 |  |
| Region | String | cn-zhangjiakou | 计算引擎所在的地域。 |  |
| TaskAuthType | String | PROJECT | 计算引擎的访问身份。 USER 当前用户 PROJECT 项目执行用户 SUBACCOUNT 子账号 STS ROLE sts角色 _ |  |
| TenantId | Long | 1234567 | 租户ID。 |  |
| PageNumber | Integer | 1 | 页码。 |  |
| PageSize | Integer | 20 | 每页显示的条数，默认为10条，最大100条。 |  |
| TotalCount | Integer | 1 | 计算引擎的总数。 |  |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |  |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |  |
| Success | Boolean | true | 是否成功查看计算引擎列表。 |  |

**示例**

请求示例 DataWorks

```
&CalcEngineType=ODPS &Name=abc &ProjectId=27 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```json
<RequestId>0bc1ec92159376****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>1</TotalCount>
    <PageSize>20</PageSize>
    <PageNumber>1</PageNumber>
    <CalcEngines>
        <BindingProjectId>27</BindingProjectId>
        <IsDefault>true</IsDefault>
        <EngineInfo>
{"pubEndpoint":"http://service.cn.maxcompute.aliyun.com/api","endpoint":"http://service.c maxcompute.aliyuninc.com/api","resourceGroupType":"ODPS","resourceGroupId":"361826516****","vpcEndpoint":" tp://service.cn.maxcompute.aliyuninc.com/api","projectName":"onefall_test_zjk","taskSameAsOwner":"true"}</EngineInfo>
        <EngineId>35</EngineId>
        <TenantId>1234567</TenantId>
        <GmtCreate>Oct 10, 2019 3:42:44 PM</GmtCreate>
        <TaskAuthType>PROJECT</TaskAuthType>
        <BindingProjectName>abc</BindingProjectName>
        <DwRegion>cn-zhangjiakou</DwRegion>
        <Region>cn-zhangjiakou</Region>
        <CalcEngineType>ODPS</CalcEngineType>
        <EnvType>PRD</EnvType>
        <Name>abc</Name>
    </CalcEngines>
</Data> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 1,
        "PageSize": 20,
        "PageNumber": 1,
        "CalcEngines": {
            "BindingProjectId": 27,
            "IsDefault": true,
            "EngineInfo": "
{\"pubEndpoint\":\"http://service.cn.maxcompute.aliyun.com/api\",\"endpoint\":\"http://se ice.cn.maxcompute.aliyuninc.com/api\",\"resourceGroupType\":\"ODPS\",\"resourceGroupId\":\"361826516****\",\"vpcE point\":\"http://service.cn.maxcompute.aliyuninc.com/api\",\"projectName\":\"onefall_test_zjk\",\"taskSameAsOwner\":\"true\"}",
            "EngineId": 35,
            "TenantId": 1234567,
            "GmtCreate": "Oct 10, 2019 3:42:44 PM",
            "TaskAuthType": "PROJECT",
            "BindingProjectName": "abc",
            "DwRegion": "cn-zhangjiakou",
            "Region": "cn-zhangjiakou",
            "CalcEngineType": "ODPS",
            "EnvType": "PRD",
            "Name": "abc"
        }
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### ListConnections

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListConnections | 系统规定参数。取值： ListConnections。 |
| Name | String | 是 | abc | 查询的数据源名称。 |
| ProjectId | Long | 是 | 76086 | 数据源所在的工作空间名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ConnectionType | String | 否 | rds | 连接串的类型。 |
| SubType | String | 否 | mysql | 连接串的子类型。 |
| Status | String | 否 | 1 | 数据源的状态。 |
| EnvType | Integer | 否 | 1 | 数据源所在工作空间的类型。 |
| PageSize | Integer | 否 | 10 | 分页查询每页的大小。 |
| PageNumber | Integer | 否 | 1 | 分页查询页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 连接串的分页查询结果。 |
| Connections | Array of Connections |  | 连接串列表。 |
| BindingCalcEn gineId | Integer | 123 | 数据源关联的计算引擎ID。 |
| ConnectStatus | Integer | 1 | 数据源的状态。 |
| ConnectionTyp e | String | mysql | 数据源的类型。 |

DataWorks

| Content | String | {\"database\":\"xxx \",\"instanceName\ ":\"xxx\",\"passwor d\":\"xxx\",\"rdsOw nerId\":\"xxx\",\"tag \":\"rds\",\"usernam e\":\"xxx\"} | 数据源的详细信息。 |
|---|---|---|---|
| DefaultEngine | Boolean | false | 数据源关联的引擎是否为同类型下的默认引擎。 |
| Description | String | a connection | 描述数据源。 |
| EnvType | Integer | 1 | 数据源所在的环境。 |
| GmtCreate | String | Oct 10, 2019 3:42:53 PM | 创建数据源的时间。 |
| GmtModified | String | Oct 10, 2019 3:42:53 PM | 修改数据源的时间。 |
| Id | Integer | 1 | 数据源ID。 |
| Name | String | abc | 数据源的名称。 |
| Operator | String | 193543050**** | 数据源最后操作人的阿里云ID。 |
| ProjectId | Integer | 123 | 数据源关联的工作空间ID。 |
| Sequence | Integer | 300 | 排序字段。 |
| Shared | Boolean | false | 是否为共享的数据源。 |
| Status | Integer | 1 | 数据源的状态。 |
| SubType | String | mysql | 数据源的子类型。 |
| TenantId | Long | 1234567 | 租户ID。 |
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 20 | 每页的大小。 |
| TotalCount | Integer | 3 | 数据源的总数。 |

DataWorks

| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
|---|---|---|---|
| RequestId | String | 0bc141151593763 59**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Name=abc &ProjectId=76086 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc14115159376359****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>3</TotalCount>
    <PageSize>20</PageSize>
    <PageNumber>1</PageNumber>
    <Connections>
        <Status>1</Status>
        <Operator>193543050****</Operator>
        <ConnectStatus>1</ConnectStatus>
        <SubType>mysql</SubType>
        <Description>a connection</Description>
        <ConnectionType>mysql</ConnectionType>
        <BindingCalcEngineId>123</BindingCalcEngineId>
        <ProjectId>123</ProjectId>
        <GmtModified>Oct 10, 2019 3:42:53 PM</GmtModified>
        <Sequence>300</Sequence>
        <Shared>false</Shared>
        <EnvType>1</EnvType>
        <Name>abc</Name>
        <DefaultEngine>false</DefaultEngine>
        <TenantId>1234567</TenantId>
        <GmtCreate>Oct 10, 2019 3:42:53 PM</GmtCreate>
        <Content>
{\"database\":\"xxx\",\"instanceName\":\"xxx\",\"password\":\"xxx\",\"rdsOwnerId\":\"xxx\ \"tag\":\"rds\",\"username\":\"xxx\"}</Content>
        <Id>1</Id>
    </Connections>
</Data> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "0bc14115159376359****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 3,
        "PageSize": 20,
        "PageNumber": 1,
        "Connections": {
            "Status": 1,
            "Operator": "193543050****",
            "ConnectStatus": 1,
            "SubType": "mysql",
            "Description": "a connection",
            "ConnectionType": "mysql",
            "BindingCalcEngineId": 123,
            "ProjectId": 123,
            "GmtModified": "Oct 10, 2019 3:42:53 PM",
            "Sequence": 300,
            "Shared": false,
            "EnvType": 1,
            "Name": "abc",
            "DefaultEngine": false,
            "TenantId": 1234567,
            "GmtCreate": "Oct 10, 2019 3:42:53 PM",
            "Content": "
{\\\"database\\\":\\\"xxx\\\",\\\"instanceName\\\":\\\"xxx\\\",\\\"password\\\":\\\"xxx\\ ,\\\"rdsOwnerId\\\":\\\"xxx\\\",\\\"tag\\\":\\\"rds\\\",\\\"username\\\":\\\"xxx\\\"}",
            "Id": 1
        }
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

DataWorks

#### ListProjectMembers

调用ListProjectMembers查询DataWorks工作空间中已存在成员的列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| ProjectId | Long | Query | 是 | 27 | Dataworks工作空间的ID。 |
| PageNum ber | Integ er | Query | 否 | 1 | 分页查询时的页码。范围1- 50000。 |
| PageSize | Integ er | Query | 否 | 10 | 分页查询时，每页的大小。 范围5-100。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1AFAE64E-D1BE- 432B-A9**** | 请求ID。 |
| Data | Struct |  | 查询结果。 |
| - ProjectMembe rList | Array |  | 工作空间的成员列表。 |
| -- ProjectRoleList | Array |  | 成员所拥有的角色列表。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- ProjectRoleCo de | String | role project guest _ _ | 角色Code。可调用ListProjectRoles接口获取项目所有角色列表。 系统预设角色枚举如下: role project owner项目所有者 _ _ role project admin空间管理员 _ _ role project dev开发 _ _ role project pe运维 _ _ role project deploy部署 _ _ role project guest访客 _ _ role project security安全管理员 _ _ role project tester体验者 _ _ role project erd模型设计师 _ _ |
| --- ProjectRoleId | Integer | 24 | 角色ID。 |
| --- ProjectRoleNa me | String | 项目所有者 | 角色的名称。 |
| --- ProjectRoleTyp e | String | 0 | 角色的类型。枚举如下： 0 系统预设角色 1 用户自定义角色 |
| --Nick | String | zhangsan | 工作空间成员的昵称。 |
| -- ProjectMembe rId | String | 121 | 成员的用户ID。 |
| -- ProjectMembe rName | String | 张三 | 成员的名称。 |
| -- ProjectMembe rType | String | 1 | 成员的类型。 1：阿里云主账号（USER ALIYUN） _ 5：RAM USER子账号 （USER UBACCOUNT） _ 6：RAM ROLE角色（USER STS ROLE） _ _ |
| --Status | String | 0 | 状态。 0：有效。 1：删除。 |
| -PageNumber | Integer | 1 | 当前的页码。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -PageSize | Integer | 10 | 每页的大小。 |
| -TotalCount | Integer | 3 | 结果的总条数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListProjectMembers &RegionId=default &ProjectId=27
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"1AFAE64E-D1BE-432B-A9****",
 "Data":{
  "TotalCount":3,
  "PageSize":10,
  "PageNumber":1,
  "ProjectMemberList":[
   {
    "Status":"0",
    "ProjectRoleList":[
     {
```

`"ProjectRoleName":"`项目所有者`",`

```json
      "ProjectRoleType":"0",
      "ProjectRoleCode":"role_project_guest",
      "ProjectRoleId":24
     }
```

`],`

```json
    "ProjectMemberType":"1",
    "ProjectMemberId":"121",
    "Nick":"zhangsan",
    "ProjectMemberName":"张三"
   }
```

]

```
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>1AFAE64E-D1BE-432B-A9****</RequestId> <Data>
 <TotalCount>3</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <ProjectMemberList>
  <Status>0</Status>
  <ProjectRoleList>
   <ProjectRoleName>项目所有者</ProjectRoleName>
   <ProjectRoleType>0</ProjectRoleType>
   <ProjectRoleCode>role_project_guest</ProjectRoleCode>
   <ProjectRoleId>24</ProjectRoleId>
  </ProjectRoleList>
  <ProjectMemberType>1</ProjectMemberType>
  <ProjectMemberId>121</ProjectMemberId>
  <Nick>zhangsan</Nick>
  <ProjectMemberName>张三</ProjectMemberName>
 </ProjectMemberList>
</Data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 100003001 | Invalid.Tenant.ConnectionNotE xists | The connection does not exist. |
| 400 | 100002003 | Invalid.Tenant.ProjectNotExists | The project does not exist. |
| 403 | 100002002 | Invalid.Tenant.UserIsNotProjec tOwnerOrAdmin | The user is not a project administrator or owner. |
| 400 | 100002001 | Invalid.Tenant.UserNotInProjec t | The user is not in the project. |
| 403 | 100001001 | Invalid.Tenant.UserNotInTenan t | The user is not in tenant. |

#### ListProjectRoles

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | ListProjectRoles | 系统规定参数。取值： ListProjectRoles |
| RequestId | Strin g | System | 是 | 1AFAE64E-D1BE432B- A9**** | 请求ID。 |
| callerType | Strin g | System | 是 | sub | 账号类型，取值范围： customer：阿里云主账号类型。 AssumedRoleUser：角色账号。 sub：RAM 子账号。 |
| ProjectId | Long | Query | 是 | 27 | Dataworks工作空间的ID。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ProjectRoleList | Array | / | 工作空间的角色列表。 |
| -ProjectRoleId | Integer | 24 | 工作空间的角色ID。 |
| - ProjectRoleTyp e | String | 0 | 工作空间的角色类型。枚举值: 0：预设角色类型。 2：用户自定义角色类型。 |
| - ProjectRoleNa me | String | 项目所有者 | 工作空间的角色名称。 |
| - ProjectRoleCo de | String | role project owner _ _ | 工作空间的角色Code。 |
| RequestId | String | 1AFAE64E-D1BE- 432B-A9**** | 请求ID。 |

**示例**

请求示例 DataWorks

```
&ProjectId=27 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "1AFAE64E-D1BE-432B-A9****",
    "ProjectRoleList": {
```

`"ProjectRoleName": "`项目所有者`",`

```json
        "ProjectRoleType": 0,
        "ProjectRoleId": 24,
        "ProjectRoleCode": "role_project_owner"
    }
}
```

`XML` 格式

```xml
<RequestId>1AFAE64E-D1BE-432B-A9****</RequestId> <ProjectRoleList>
    <ProjectRoleName>项目所有者</ProjectRoleName>
    <ProjectRoleType>0</ProjectRoleType>
    <ProjectRoleId>24</ProjectRoleId>
    <ProjectRoleCode>role_project_owner</ProjectRoleCode>
</ProjectRoleList>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### ListProjects

调用ListProjects，分页列出用户所在租户下的DataWorks工作空间列表。 DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListProjects | 系统规定参数。取值：ListProjects。 |
| PageNumber | Integer | 是 | 1 | 分页的页码。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageResult | Struct |  | 查询的结果。 |
| PageNumber | Integer | 1 | 当前的页码。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| ProjectList | Array of Project |  | DataWorks工作空间的结果列表。 |
| ProjectDescrip tion | String | 测试空间 | 工作空间的详细描述信息。 |
| ProjectId | Long | 1212 | 工作空间的ID。 |
| ProjectIdentifi er | String | test | 工作空间的编码。 |
| ProjectName | String | 测试空间 | 工作空间的名称。 |
| ProjectOwnerB aseId | String | 122222 | 工作空间所有者的用户ID。 |
| ProjectStatus | Integer | 0 | 工作空间的状态。 |
| ProjectStatusC ode | String | AVAILABLE | 工作空间的状态码。 |
| TotalCount | Integer | 123 | 结果的总条数。 |

DataWorks

| RequestId | String | 20658801*** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&PageNumber=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>20658801***</RequestId> <PageResult>
    <TotalCount>123</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <ProjectList>
        <ProjectIdentifier>test</ProjectIdentifier>
        <ProjectOwnerBaseId>122222</ProjectOwnerBaseId>
        <ProjectStatusCode>AVAILABLE</ProjectStatusCode>
        <ProjectStatus>0</ProjectStatus>
        <ProjectName>测试空间</ProjectName>
        <ProjectId>1212</ProjectId>
        <ProjectDescription>测试空间</ProjectDescription>
    </ProjectList>
</PageResult>
```

`JSON` 格式

```json
{
    "RequestId": "20658801***",
    "PageResult": {
        "TotalCount": 123,
        "PageSize": 10,
        "PageNumber": 1,
        "ProjectList": {
            "ProjectIdentifier": "test",
            "ProjectOwnerBaseId": 122222,
            "ProjectStatusCode": "AVAILABLE",
            "ProjectStatus": 0,
```

`"ProjectName": "`测试空间`",`

```json
            "ProjectId": 1212,
            "ProjectDescription": "测试空间"
        }
    }
}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 400 | Invalid.Tenant.User AlreadyInProject | The user already exists in the project. | 待添加用户已经存在于工作空间中。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### ListProjectIds

调用ListProjectIds，使用目标阿里云账号（包括阿里云主账号或RAM用户）的ID获取其拥有角色权限的 DataWorks工作空间的ID列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListProjectIds | 系统规定参数。取值：ListProjectIds。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| UserId | String | 是 | 171111 | 目标阿里云账号ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ProjectIds | List | 75777 | 返回的DataWorks工作空间ID。 返回结果为目标阿里云账号所拥有角色权限的 DataWorks工作空间的ID列表，此处仅以一个工作空间ID示例。 |
| RequestId | String | 0b57ff7216278945 532771749d**** | 请求ID。此次请求的唯一标识，用于定位日志， 排查问题。 |

**示例**

请求示例 DataWorks

```
&RegionId=default &UserId=171111
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0b57ff7216278945532771749d****</RequestId> <ProjectIds>75777</ProjectIds>
```

`JSON` 格式

```json
{
    "RequestId": "0b57ff7216278945532771749d****",
    "ProjectIds": 75777
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### ListResourceGroups

该接口用于查看指定类型的资源组列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| Resource GroupTyp e | Integ er | Query | 否 | 3 | 需要查看的资源组类型 ID。 取值如下： 0：DataWorks 1：调度，默认值 2：MaxCompute 3：API 4：数据集成 7：下单购买独享调度资源组时，生成的购买资源 ID 9：dataService 当取值表示引擎时，查看的资源组列表为购买该类型引擎时创建的资源组列表。 |
| Keyword | Strin g | Query | 否 | abc | 关键字。用于模糊查询资源组名称和资源组标识。 |
| BizExtKey | Strin g | Query | 否 | default | 资源组的类别。取值如下： default：公共资源组， 默认值 single：独享资源组 |
| Resource ManagerR esourceGr oupId | Strin g | Query | 否 | rg-acfmzbn7pti3**** | 资源组 ID。 |
| Tags | Repe atList | Query | 否 | / | 标签列表。 |
| -Key | Strin g |  | 否 | Env | 标签键。 |
| -Value | Strin g |  | 否 | Test | 标签值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | / | 资源组列表。 |
| -Tags | Array | / | 标签列表。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Key | String | Env | 标签键。 |
| --Value | String | Test | 标签值。 |
| -Status | Integer | 0 | 资源组的状态。取值如下： 0：NORMAL，表示资源组状态正常，处于运行中或服务中。 1：STOP，表示资源组已到期，处于冻结状态。 2：DELETED，表示资源组已被释放或销毁。 3：CREATING，表示资源组正在创建或启动。 4：CREATE FAILED，表示资源组创建或启 _ 动失败。 5：UPDATING，表示资源组正在扩容或升级。 6：UPDATE FAILED，表示资源组扩容或升 _ 级失败。 7：DELETING，表示资源组正在被释放或销毁。 8：DELETE FAILED，表示资源组释放或销 _ 毁失败。 9：TIMEOUT，表示对资源组执行的操作超时。所有变更操作均可能会超时，该枚举值暂时仅提供给数据服务使用。 |
| -UpdateTime | String | Jul 9, 2018 2:43:37 PM | 最近一次更新资源组的时间。 |
| -IsDefault | Boolean | true | 是否为默认资源组。取值如下： true：是默认资源组 false：非默认资源组 |
| -Cluster | String | AY18G | 集群的名称。该参数仅对于 MaxCompute 和 PAI 资源组类型生效。 |
| -EnableKp | Boolean | false | 是否使用 Kp（关键人）访问。取值如下： true：表示 MaxCompute 引擎使用阿里云账号 UID 作为访问账户的显示名称。 false：表示 MaxCompute 引擎使用阿里云账号名称作为访问账户的显示名称。 其余类型无意义。该参数仅对 MaxCompute 引擎生效。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ResourceGrou pType | String | 3 | 资源组的类型。取值如下： 0：DataWorks 2：MaxCompute 3：PAI 4：数据集成 7：调度 9：dataService |
| -CreateTime | String | Jul 9, 2018 2:43:37 PM | 创建集群的时间。格式示例为 Jul 9, 2018 2:43:37 PM。 |
| -Identifier | String | e1815577-2f4e- 4c5e-b29**** | 资源组的标识。 |
| -Mode | String | SHARE | 资源组的类型。取值如下： ISOLATE：预付费的独享资源组 SHARE：后付费的公共资源组 DEVELOP：开发者版本 |
| -BizExtKey | String | default | 资源组的类别。取值如下： default：公共资源组 single：独享资源组 |
| -Sequence | Integer | 300 | 序列字段。用于将已创建的资源组按照创建的序号从小到大升序排序。 |
| -Specs | Map | {} | 资源组的详细信息。{}中显示的内容为资源组的详细信息。 |
| -Name | String | abc | 资源组的名称。 |
| -Id | Long | 10001 | 资源组 ID。 |
| -TenantId | Long | 1234567 | 租户ID。 |
| - ResourceMana gerResourceGr oupId | String | rg-acfmzbn7**** | 资源组 ID。 |
| HttpStatusCod e | Integer | 200 | 请求返回码。 |
| RequestId | String | 0bc141151593763 5973**** | 请求 ID。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListResourceGroups &RegionId=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0bc1411515937635973****",
 "HttpStatusCode":200,
 "Data":[
  {
   "Status":0,
   "IsDefault":true,
   "Tags":[
    {
     "Value":"Test",
     "Key":"Env"
    }
```

`],`

```json
   "CreateTime":"Jul 9, 2018 2:43:37 PM",
   "Mode":"SHARE",
   "Cluster":"AY18G",
   "Sequence":300,
   "ResourceGroupType":"3",
   "Name":"abc",
   "ResourceManagerResourceGroupId":"rg-acfmzbn7****",
   "TenantId":1234567,
   "Identifier":"e1815577-2f4e-4c5e-b29****",
   "EnableKp":false,
   "BizExtKey":"default",
   "UpdateTime":"Jul 9, 2018 2:43:37 PM",
   "Id":10001,
   "Specs":{}
  }
```

`],`

```json
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0bc1411515937635973****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
  <Status>0</Status>
  <IsDefault>true</IsDefault>
  <Tags>
    <Value>Test</Value>
    <Key>Env</Key>
  </Tags>
  <CreateTime>Jul 9, 2018 2:43:37 PM</CreateTime>
  <Mode>SHARE</Mode>
  <Cluster>AY18G</Cluster>
  <Sequence>300</Sequence>
  <ResourceGroupType>3</ResourceGroupType>
  <Name>abc</Name>
  <ResourceManagerResourceGroupId>rg-acfmzbn7****</ResourceManagerResourceGroupId>
  <TenantId>1234567</TenantId>
  <Identifier>e1815577-2f4e-4c5e-b29****</Identifier>
  <EnableKp>false</EnableKp>
  <BizExtKey>default</BizExtKey>
  <UpdateTime>Jul 9, 2018 2:43:37 PM</UpdateTime>
  <Id>10001</Id>
  <Specs  />
</Data> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 100003001 | Invalid.Tenant.ConnectionNotE xists | The connection does not exist. |
| 400 | 100002003 | Invalid.Tenant.ProjectNotExists | The project does not exist. |
| 400 | 100002001 | Invalid.Tenant.UserNotInProjec t | The user is not in the project. |
| 403 | 100002002 | Invalid.Tenant.UserIsNotProjec tOwnerOrAdmin | The user is not a project administrator or owner. |
| 403 | 100001001 | Invalid.Tenant.UserNotInTenan t | The user is not in tenant. |

#### RemoveProjectMemberFromRole

调用RemoveProjectMemberFromRole，将Dataworks工作空间内的用户从Dataworks角色中移除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | RemoveProjectM emberFromRole | 系统规定参数。取值： RemoveProjectMemberFromRole。 |
|---|---|---|---|---|
| ProjectId | Long | 是 | 27 | Dataworks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RoleCode | String | 是 | role project gue _ _ st | Dataworks工作空间的角色Code。可调用接口ListProjectRoles获取项目有哪些角色code列表。 默认预设角色枚举如下： role project owner项目所有者 _ _ role project admin空间管理员 _ _ role project dev开发 _ _ role project pe运维 _ _ role project deploy部署 _ _ role project guest访客 _ _ role project security安全管理员 _ _ role project tester体验者 _ _ role project erd模型设计师 _ _ |
| UserId | String | 是 | 1234 | 用户的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AFAE64E-D1BE- 432B-A9**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveProjectMemberFromRole &ProjectId=27 &RegionId=default &RoleCode=role_project_guest &UserId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>1AFAE64E-D1BE-432B-A9****</RequestId>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "1AFAE64E-D1BE-432B-A9****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### UpdateConnection

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateConnecti on | 系统规定参数。取值： UpdateConnection。 |
| ConnectionId | Long | 是 | 1 | 数据源ID。您可以通过ListConnections 接口获取项目空间下的数据源ID。 |
|  |  |  |  | 数据源的详细信息。部分常用数据源样例如下： odps |

DataWorks

|  |  |  |  | { |
|---|---|---|---|---|
|  |  |  |  | "accessId": "xssssss", "accessKey": "xsaxsaxsa", "authType": 2, "endpoint": "http://service.odps.aliyun.c om/api", "project": "xsaxsax", "tag": "public" } mysql { "database": "xsaxsa", "instanceName": "rm- xsaxsa", "password": "xsaxsa", "rdsOwnerId": "xasxsa", "regionId": "cn-shanghai", "tag": "rds", "username": "xsaxsa" } rds { "configType": 1, "tag": "rds", "database": "xsaxsa", "username": "xsaxsa", "password": "xssaxsa$32050", "instanceName": "rm- xsaxs", "rdsOwnerId": "11111111" } oss { "accessId": "sssssxx", "accessKey": "xsaxaxsaxs", "bucket": "xsa-xs-xs", "endpoint": "http://oss- cn-shanghai.aliyuncs.com", "tag": "public" } |

DataWorks

| Content | String | 是 | {"database":"db name","instance Name":"instance name","passwor d":"password","r dsOwnerId":"12 3","username":" username"} | sqlserver { "jdbcUrl": "jdbc:sqlserver://xsaxsa- xsaxsa.database.xxx.cn:123;Da tabaseName=xsxs-xsxs", "password": "sdasda$fs", "tag": "public", "username": "sxaxacdacdd" } polardb { "clusterId": "pc- sdadsadsa", "database": "dsadsadsa", "ownerId": "121212122", "password": "sdasdafssa", "region": "cn-shanghai", "tag": "polardb", "username": "asdadsads" } oracle { "jdbcUrl": "jdbc:oracle:saaa:@xxxxx:1521 :PROD", "password": "sxasaxsa", "tag": "public", "username": "sasfadfa" } mongodb { "address": " [\"xsaxxsa.mongodb.rds.aliyun cs.com:3717\"]", "database": "admin", "password": "sadsda@", "tag": "public", "username": "dsadsadas" } emr |
|---|---|---|---|---|
| 07 |  |  |  | > 文档版本：2026072 |

DataWorks

|  |  |  |  | { "accessId": "xsaxsa", "emrClusterId": "C-dsads", "emrResourceQueueName": "default", "emrEndpoint": "emr.aliyuncs.com", "accessKey": "dsadsad", "emrUserId": "224833315798889783", "name": "sasdsadsa", "emrAccessMode": "simple", "region": "cn-shanghai", "authType": "2", "emrProjectId": "FP- sdadsad" } postgresql { "jdbcUrl": "jdbc:postgresql://xxxx:1921/ ssss", "password": "sdadsads", "tag": "public", "username": "sdsasda" } analyticdb for mysql _ _ { "instanceId": "am- sadsada", "database": "xsxsx", "username": "xsxsa", "password": "asdadsa", "connectionString": "am- xssxsxs.ads.aliyuncs.com:3306 " } hybriddb for postgresql _ _ |
|---|---|---|---|---|

DataWorks

|  |  |  |  | { "connectionString": "gp- xsaxsaxa- master.gpdbmaster.rds.aliyunc s.com", "database": "xsaxsaxas", "password": "xsaxsaxsa@11", "instanceId": "gp- xsaxsaxsa", "port": "541132", "ownerId": "xsaxsaxsas", "username": "sadsad" } holo { "accessId": "xsaxsaxs", "accessKey": "xsaxsaxsa", "database": "xsaxsaxsa", "instanceId": "xsaxa", "tag": "aliyun" } kafka { "instanceId": "xsax-cn- xsaxsa", "regionId": "cn-shanghai", "tag": "aliyun", "ownerId": "1212121212112" } |
|---|---|---|---|---|
| EnvType | Integer | 是 | 1 | 数据源所属的环境，包括0（开发环境）和 1（生产环境）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Description | String | 否 | abc | 描述数据源。 |
| Status | String | 否 | ENABLED | 数据源的状态，包括ENABLED（正常）和 DISABLED（异常）。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | false | 请求是否成功更新。 |
| HttpStatusCod e | String | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```json
&ConnectionId=1 &Content= {"database":"dbname","instanceName":"instancename","password":"password","rdsOwnerId":"12 ,"username":"username"} &EnvType=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>false</Data> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD- EFG*****","HttpStatusCode":"200","Data":"false","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |

DataWorks

| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
|---|---|---|---|
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |

#### UpdateDataSource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateDataSour ce | 系统规定参数。取值： UpdateDataSource。 |
|  |  |  |  | 需要修改的目标数据源的详细信息。 不支持修改数据源的类型，例如，您不可以修改odps类型的数据源为mysql类型。 部分常用数据源的信息样例如下： odps { "accessId": "xssssss", "accessKey": "xsaxsaxsa", "authType": 2, "endpoint": "http://service.odps.aliyun.c om/api", "project": "xsaxsax", "tag": "public" } mysql { "database": "xsaxsa", "instanceName": "rm- xsaxsa", "password": "xsaxsa", "rdsOwnerId": "xasxsa", "regionId": "cn-shanghai", "tag": "rds", "username": "xsaxsa" } rds |

DataWorks

|  |  |  |  | { "configType": 1, "tag": "rds", "database": "xsaxsa", "username": "xsaxsa", "password": "xssaxsa$32050", "instanceName": "rm- xsaxs", "rdsOwnerId": "11111111" } oss { "accessId": "sssssxx", "accessKey": "xsaxaxsaxs", "bucket": "xsa-xs-xs", "endpoint": "http://oss- cn-shanghai.aliyuncs.com", "tag": "public" } |
|---|---|---|---|---|
|  |  |  |  | sqlserver { "jdbcUrl": "jdbc:sqlserver://xsaxsa- xsaxsa.database.xxx.cn:123;Da tabaseName=xsxs-xsxs", "password": "sdasda$fs", "tag": "public", "username": "sxaxacdacdd" } polardb { "clusterId": "pc- sdadsadsa", "database": "dsadsadsa", "ownerId": "121212122", "password": "sdasdafssa", "region": "cn-shanghai", "tag": "polardb", "username": "asdadsads" } oracle |

DataWorks

| Content | String | 是 | {"accessId":"xss ssss","accessKey ":"xsaxsaxsa","a uthType":2,"end point":"http://ser vice.odps.aliyun. com/api","projec t":"xsaxsax","tag ":"public"} | { "jdbcUrl": "jdbc:oracle:saaa:@xxxxx:1521 :PROD", "password": "sxasaxsa", "tag": "public", "username": "sasfadfa" } mongodb { "address": " [\"xsaxxsa.mongodb.rds.aliyun cs.com:3717\"]", "database": "admin", "password": "sadsda@", "tag": "public", "username": "dsadsadas" } emr { "accessId": "xsaxsa", "emrClusterId": "C-dsads", "emrResourceQueueName": "default", "emrEndpoint": "emr.aliyuncs.com", "accessKey": "dsadsad", "emrUserId": "224833315798889783", "name": "sasdsadsa", "emrAccessMode": "simple", "region": "cn-shanghai", "authType": "2", "emrProjectId": "FP- sdadsad" } postgresql |
|---|---|---|---|---|

DataWorks

|  |  |  |  | { "jdbcUrl": "jdbc:postgresql://xxxx:1921/ ssss", "password": "sdadsads", "tag": "public", "username": "sdsasda" } analyticdb for mysql _ _ { "instanceId": "am- sadsada", "database": "xsxsx", "username": "xsxsa", "password": "asdadsa", "connectionString": "am- xssxsxs.ads.aliyuncs.com:3306 " } hybriddb for postgresql _ _ { "connectionString": "gp- xsaxsaxa- master.gpdbmaster.rds.aliyunc s.com", "database": "xsaxsaxas", "password": "xsaxsaxsa@11", "instanceId": "gp- xsaxsaxsa", "port": "541132", "ownerId": "xsaxsaxsas", "username": "sadsad" } holo { "accessId": "xsaxsaxs", "accessKey": "xsaxsaxsa", "database": "xsaxsaxsa", "instanceId": "xsaxa", "tag": "aliyun" } |
|---|---|---|---|---|

DataWorks

|  |  |  |  | kafka { "instanceId": "xsax-cn- xsaxsa", "regionId": "cn-shanghai", "tag": "aliyun", "ownerId": "1212121212112" } |
|---|---|---|---|---|
| DataSourceId | Long | 是 | 1 | 需要更新的数据源ID。 |
| EnvType | Integer | 是 | 1 | 数据源所在的环境。取值如下： 0，开发环境。 1，生产环境。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Description | String | 否 | xxx | 数据源的描述信息。 |
| Status | String | 否 | ENABLED | 数据源的状态。该字段已废弃，请勿使用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否成功更新数据源。 |
| HttpStatusCod e | String | 200 | HTTP状态码。 |
| RequestId | String | 0bc141151593763 59**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 DataWorks

```json
&Content= {"accessId":"xssssss","accessKey":"xsaxsaxsa","authType":2,"endpoint":"http://service.odp aliyun.com/api","project":"xsaxsax","tag":"public"} &DataSourceId=1 &EnvType=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc14115159376359****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc14115159376359****",
    "HttpStatusCode": 200,
    "Data": true,
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Tenant.Con nectionNotExists | The connection does not exist. | 数据源不存在。 |
| 400 | Invalid.Tenant.Proj ectNotExists | The project does not exist. | 项目不存在。 |
| 403 | Invalid.Tenant.User IsNotProjectOwner OrAdmin | The user is not a project administrator or owner. | 用户不是项目负责人或者项目管理员。 |
| 400 | Invalid.Tenant.User NotInProject | The user is not in the project. | 用户不在项目中。 |
| 403 | Invalid.Tenant.User NotInTenant | The user is not in tenant. | 用户不在租户中。 |
| 400 | MissingParam.Conn ectionStr.Property | You must specify property %s required by the data source connection string. | 数据源连接串信息必填属性缺失 |
| 400 | DataSource.Check RamRoleFailure | Failed to check the RAM role. AccountId %s. roleArn %s. | 校验数据源权限失败 |

DataWorks

| 400 | DataSource.Conne ctionStrProperty.Pa tternNotMatch | The pattern value %s is invalid. The correct pattern is %s. | 数据源连接串属性不匹配规则 |
|---|---|---|---|
| 400 | DataSource.NotFou nd | The specified data source ID %s does not exist. | 数据源不存在 |
| 400 | Invalid.Connection. Empty | You must specify the connection parameter. | 数据源参数为空 |
| 400 | Invalid.DataSource. DataSourceTypeNo tExist | The data source type %s does not exist. | 数据源类型不存在。 |
| 400 | Invalid.DataSource. DataSourceTypeNo tSupport | The dataSourceType %s and subType %s are not supported. | 数据源类型暂不支持 |
| 400 | Invalid.Operation | You cannot delete the bindingCalcEngine that is bound to the data source. | 数据源绑定的计算引擎不允许删除 |
| 400 | Required.Paramete r.Empty | You must specify the parameter %s. | 必填参数缺失 |

### 元数据

#### AddToMetaCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddToMetaCate gory | 系统规定参数。取值： AddToMetaCategory。 |
| CategoryId | Long | 是 | 5 | 类目的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否成功添加表至指定的类目。 |

DataWorks

| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&CategoryId=5 &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CheckMetaPartition

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CheckMetaPartit ion | 系统规定参数。取值： CheckMetaPartition。 |
| Partition | String | 是 | ds=202005 | 分区的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |
| ClusterId | String | 否 | abc | EMR集群的ID。 |
| DatabaseName | String | 否 | abc | 数据库的名称。 |
| TableName | String | 否 | abc | 表名。 |
| DataSourceType | String | 否 | emr | 数据类型，包括odps和emr。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 分区是否存在。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CheckMetaPartition &Partition=ds=202005 &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

#### CheckMetaTable

**请求参数**

DataWorks

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CheckMetaTable | 系统规定参数。取值： CheckMetaTable。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |
| ClusterId | String | 否 | abc | EMR集群的ID。 |
| DatabaseName | String | 否 | abc | EMR数据库的名称。 |
| TableName | String | 否 | abc | EMR表名。 |
| DataSourceType | String | 否 | emr | 数据类型，odps或者emr。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 表是否存在。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |

**示例**

请求示例

```
&RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <Data>true</Data>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376",
    "Data": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

DataWorks

#### CreateMetaCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateMetaCate gory | 系统规定参数。取值： CreateMetaCategory。 |
| Name | String | 是 | category name _ | 类目的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Comment | String | 否 | category 1 | 类目的备注信息。 |
| ParentId | Long | 否 | 0 | 父类目的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 类目信息。 |
| CategoryId | Long | 223 | 类目的ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=CreateMetaCategory &Name=category_name &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <CategoryId>223</CategoryId>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "CategoryId": 223
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
|---|---|---|---|
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Invalid.Meta.Categ oryForbidden | Failed to delete the category. The current category is associated with a table and cannot be operated. | 类目删除失败，当前类目存在关联表，不能进行操作。 |
| 400 | Invalid.Meta.Categ oryIllegalDepth | A category can contain a maximum of 4 levels. | 类目层级超过4级。 |
| 403 | Invalid.Meta.Categ oryIllegalTenant | The tenant ID is different in the parent and child categories. | 父子类目的租户ID不一致。 |
| 400 | Invalid.Meta.Categ oryNameDuplicate | The category name is duplicated at this level. | 同一层级下，类目名称重复。 |
| 500 | Invalid.Meta.Categ oryRelationDuplicat e" | The table is already bound to the category. | 类目已经关联该表。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateTable

**请求参数**

DataWorks

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateTable | 系统规定参数。取值：CreateTable。 |
| Columns.N.Colu mnName | String | 是 | columnName1 | 字段的名称。 CreateTable API当前最多支持配置100个字段。 |
| Columns.N.Colu mnType | String | 是 | string | 字段的类型。 |
| HasPart | Integer | 是 | 0 | 创建的MaxCompute表是否为分区表，包括1（是）和0（否）。该字段已废弃，请勿使用。 目前代码会根据 Column.N.isPartitionCol参数判断 MaxCompute表是否为分区表，当 Column.N.isPartition参数取值为1时， 则认为MaxCompute表为分区表。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | tablename | 表的名称。 |
| Columns.N.Colu mnNameCn | String | 否 | 中文名 | 字段的中文名称。 |
| Columns.N.SeqN umber | Integer | 否 | 1 | 字段的序列号。您可以指定字段在表中的排序，默认按照创建请求的顺序排序。 如果字段为分区字段，则不支持配置 Columns.N.SeqNumber。 |
| Columns.N.Leng th | Integer | 否 | 10 | 字段的长度。 |
| Columns.N.IsPart itionCol | Integer | 否 | 0 | 当前字段是否为分区字段： 1为分区字段。 0为非分区字段。 |
| Columns.N.IsPri maryKey | Integer | 否 | 1 | 是否是主键。 |
| Columns.N.IsNull able | Integer | 否 | 1 | 是否允许为空。 |
| Columns.N.Com ment | String | 否 | 备注 | 字段的备注信息。 |
| IsView | Integer | 否 | 0 | 指定创建视图或创建表： 0为创建表。 1为创建视图。 |

DataWorks

| Visibility | Integer | 否 | 1 | 表或工作空间是否可见： 0为表和工作空间均不可见。 1为表和工作空间均可见。 2为仅工作空间可见。 |
|---|---|---|---|---|
| LifeCycle | Integer | 否 | 10 | 表的生命周期。默认取值为空，表示永久存储。 |
| CategoryId | Long | 否 | 101 | 关联类目的ID。您可以通过 GetMetaCategory接口查询可以关联的类目ID。 |
| LogicalLevelId | Long | 否 | 101 | 逻辑层级ID。 |
| PhysicsLevelId | Long | 否 | 101 | 物理层级ID。 |
| ExternalTableTy pe | String | 否 | 0 | 外部表的存储类型。取值如下： 0表示OSS。 1表示TableStore。 2表示Volume。 3表示MySQL。 |
| Location | String | 否 | location | 外部表的存储地址。 |
| ProjectId | Long | 否 | 23 | DataWorks工作空间的ID。 |
| Endpoint | String | 否 | odps://abc | MaxCompute的Endpoint。 |
| EnvType | Integer | 否 | 1 | DataWorks工作空间的环境。取值如下： 0表示开发环境。 1表示生产环境。 |
| Themes.N.Them eId | Long | 否 | 101 | 主题ID。 |
| Themes.N.Them eLevel | Integer | 否 | 101 | 主题ID对应的主题层级。 |
| AppGuid | String | 否 | odps.test | MaxCompute项目的ID，格式为 odps. {projectName}。 |
| Comment | String | 否 | 备注 | 备注信息。 |

|  | {projectName}。 |
|---|---|

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | abcdef | 请求ID。 |
| TaskInfo | Struct |  | 请求任务的信息。 请求任务提交成功后，会被分为多个子任务有序执行。当前子任务执行成功后，才会继续执行下一个子任务，所有子任务执行完毕，该请求任务结束。 如下情况，请求任务会终止，您需要根据错误码信息解决问题后重新发起请求任务： 请求任务提交失败。 请求任务提交成功后，任意子任务执行失败。 |
| Content | String | success | 当前子任务的执行状态详细信息。具体如下： 执行成功，则显示success。 执行失败则显示对应的报错详情。 |
| NextTaskId | String | abc1 | 即将执行的子任务ID。如果该字段为空，则表示所有子任务均已结束。您可以使用获取到的ID， 从GetDDLJobStatus接口查询对应子任务的状态。 |
| Status | String | success | 当前执行的子任务的状态信息。取值如下： operating表示子任务正在执行中。 success表示子任务执行成功。 failure表示子任务执行失败。详细的报错信息请参见Content参数。 |
| TaskId | String | success | 当前执行的子任务ID。 |

**示例**

请求示例

```
&Columns.1.ColumnName=columnName1 &Columns.1.ColumnType=string &HasPart=0 &RegionId=default &TableName=tablename
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<TaskInfo>
    <Status>success</Status>
    <TaskId>success</TaskId>
    <Content>success</Content>
    <NextTaskId>abc1</NextTaskId>
</TaskInfo> <RequestId>abcdef</RequestId>
```

`JSON` 格式

```json
{"TaskInfo": {"Status":"success","TaskId":"success","Content":"success","NextTaskId":"abc1"},"RequestI :"abcdef"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateTableTheme

调用CreateTableTheme创建主题。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | CreateTableThe me | 系统规定参数。取值： CreateTableTheme。 |
|---|---|---|---|---|
| Level | Integer | 是 | 1 | 主题的层级，包括1（一级主题）和2（二级主题）。 |
| Name | String | 是 | 主题名称 | 主题的名称。 |
| ProjectId | Long | 是 | 123 | DataWorks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ParentId | Long | 否 | 122 | 父类层级ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 500 | 错误码。 |
| ErrorMessage | String | An internal system error occurred. Try again later. | 错误消息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | ABCd | 请求ID。 |
| Success | Boolean | false | 是否成功。 |
| ThemeId | Long | 123 | 生成的主题ID。 |

**示例**

请求示例

```
&Level=1
```

`&Name=`主题名称

```
&ProjectId=123 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<ThemeId>123</ThemeId> <RequestId>ABCd</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>500</ErrorCode> <ErrorMessage>An internal system error occurred. Try again later.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"ThemeId":"123","RequestId":"ABCd","HttpStatusCode":"200","ErrorCode":"500","ErrorMessag :"An internal system error occurred. Try again later.","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateTableLevel

调用CreateTableLevel创建层级。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | CreateTableLev el | 系统规定参数。取值： CreateTableLevel。 |
|---|---|---|---|---|
| LevelType | Integer | 是 | 1 | 层级的类型，包括1（逻辑层级）和2（物理层级）。 |
| Name | String | 是 | 层级1 | 层级的名称。 |
| ProjectId | Long | 是 | 123 | DataWorks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Description | String | 否 | 层级的描述 | 层级的描述。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误消息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| LevelId | Long | 123 | 层级ID。 |
| RequestId | String | 123456789**** | 请求ID。 |
| Success | Boolean | true | 是否成功创建层级。 |

**示例**

请求示例

```
&LevelType=1
```

`&Name=`层级1

```
&ProjectId=123 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<RequestId>123456789****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <LevelId>123</LevelId> <Success>true</Success>
```

`JSON` 格式

```json
{"RequestId":"123456789****","HttpStatusCode":"200","ErrorCode":"1031203110005","ErrorMes ge":"The specified parameters are invalid.","LevelId":"123","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteFromMetaCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | DeleteFromMeta Category | 系统规定参数。取值： DeleteFromMetaCategory。 |
|---|---|---|---|---|
| CategoryId | Long | 是 | 5 | 类目的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否成功删除表。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteFromMetaCategory &CategoryId=5 &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteMetaCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | DeleteMetaCate gory | 系统规定参数。取值： DeleteMetaCategory。 |
|---|---|---|---|---|
| CategoryId | Long | 是 | 23 | 类目的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 业务数据。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteMetaCategory &CategoryId=23 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 403 | Invalid.Meta.Categ oryForbidden | Failed to delete the category. The current category is associated with a table and cannot be operated. | 类目删除失败，当前类目存在关联表，不能进行操作。 |
| 400 | Invalid.Meta.Categ oryIllegalDepth | A category can contain a maximum of 4 levels. | 类目层级超过4级。 |
| 403 | Invalid.Meta.Categ oryIllegalTenant | The tenant ID is different in the parent and child categories. | 父子类目的租户ID不一致。 |

DataWorks

| 400 | Invalid.Meta.Categ oryNameDuplicate | The category name is duplicated at this level. | 同一层级下，类目名称重复。 |
|---|---|---|---|
| 500 | Invalid.Meta.Categ oryRelationDuplicat e" | The table is already bound to the category. | 类目已经关联该表。 |
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteTable

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteTable | 系统规定参数。取值：DeleteTable。 |
| EnvType | Integer | 是 | 1 | DataWorks环境的类型，包括0（开发环境）和1（生产环境）。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | table1 | MaxCompute表的名称。 |
| AppGuid | String | 否 | odps.test | MaxCompute项目的唯一标识，格式为 odps.{projectName}。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1234-ABCD- EFG***** | 请求ID。 |
| TaskInfo | Struct |  | 删除表的任务信息。 |
| Content | String | success | 任务的内容。 |
| NextTaskId | String | abc1 | 正在运行的任务ID。 |
| Status | String | success | 已经结束的任务状态。 |
| TaskId | String | abc | 已经结束的任务ID。 |

**示例**

请求示例

```
&EnvType=1 &ProjectId=10001 &RegionId=default &TableName=table1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TaskInfo>
    <Status>success</Status>
    <TaskId>abc</TaskId>
    <Content>success</Content>
    <NextTaskId>abc1</NextTaskId>
</TaskInfo> <RequestId>1234-ABCD-EFG*****</RequestId>
```

`JSON` 格式

```json
{"TaskInfo": {"Status":"success","TaskId":"abc","Content":"success","NextTaskId":"abc1"},"RequestId":" 34-ABCD-EFG*****"}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteTableLevel

调用DeleteTableLevel删除层级。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteTableLeve l | 系统规定参数。取值： DeleteTableLevel。 |
| LevelId | Long | 是 | 123 | 需要删除的层级ID。您可以从ListLevel接口获取。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DeleteResult | Boolean | true | 删除结果。 |

DataWorks

| RequestId | String | 0000-ABCD- EFG****** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&LevelId=123 &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG******</RequestId> <DeleteResult>true</DeleteResult>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG******","DeleteResult":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteTableTheme

DataWorks 调用DeleteTableTheme删除主题。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteTableThe me | 系统规定参数。取值： DeleteTableTheme。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ThemeId | Long | 是 | 10002 | 主题ID。 |
| ProjectId | Long | 否 | 10001 | DataWorks工作空间ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DeleteResult | Boolean | true | 删除结果。 |
| ErrorCode | String | 500 | 错误码。 |
| ErrorMessage | String | An internal system error occurred. Try again later. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 主题是否删除成功： true：是 false：否 |

**示例**

请求示例

```
&RegionId=default &ThemeId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>500</ErrorCode> <ErrorMessage>An internal system error occurred. Try again later.</ErrorMessage> <DeleteResult>true</DeleteResult> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD- EFG*****","HttpStatusCode":"200","ErrorCode":"500","ErrorMessage":"An internal system e rror occurred. Try again later.","DeleteResult":"true","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetDDLJobStatus

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDDLJobStatu s | 系统规定参数。取值： GetDDLJobStatus。 |

DataWorks

| RegionId | String | 是 | default | 区域ID，为固定值default。 |
|---|---|---|---|---|
| TaskId | String | 是 | abc | DDL任务的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 任务的详情。 |
| Content | String | success | 任务的内容。 |
| NextTaskId | String | abc | 正在进行的TaskID。如果为空，说明全部任务已经结束。 |
| Status | String | success | 任务的状态。 |
| TaskId | String | abc | 任务ID。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
&RegionId=default &TaskId=abc
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <Data>
    <Status>success</Status>
    <TaskId>abc</TaskId>
    <Content>success</Content>
    <NextTaskId>abc</NextTaskId>
</Data>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","Data": {"Status":"success","TaskId":"abc","Content":"success","NextTaskId":"abc"}}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaDBInfo

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaDBInfo | 系统规定参数。取值：GetMetaDBInfo。 |
| AppGuid | String | 是 | odps.some engi _ ne name _ | 引擎ID，格式为引擎类型.引擎名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ClusterId | String | 否 | abc | EMR集群的clusterId。 |
| DatabaseName | String | 否 | abc | EMR集群的数据库。 |
| DataSourceType | String | 否 | emr | 数据类型，包括odps和emr。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| AppGuid | String | odps.engine name _ | 引擎ID，格式为引擎类型.引擎名称。 |
| ClusterBizId | String | abc | emr集群id，针对查询emr数据情况 |
| Comment | String | 备注 | 备注 |
| CreateTime | Long | 1541576644000 | 创建引擎的时间。 |
| Endpoint | String | http://service.odps stg.aliyun-inc.com/ | 服务地址Endpoint。 |
| EnvType | Integer | 1 | 环境类型：0表示非生产表，1表示生产表。 |
| Location | String | hdfs:// | emr数据库对应数据存储地址。针对emr情况 |
| ModifyTime | Long | 1541576644000 | 修改引擎的时间。 |
| Name | String | abc | 数据库名称 |
| OwnerId | String | 23 | 工作空间Owner的云账号ID。 |
| OwnerName | String | 323 | 工作空间Owner的名称。 |
| ProjectId | Long | 22 | 工作空间ID。 |
| ProjectName | String | test | 工作空间的名称。 |
| ProjectNameC n | String | 测试项目 | 工作空间的显示名称。 |
| TenantId | Long | 233 | 租户ID。 |
| Type | String | hive | 数据库类型 |
| RequestId | String | 0bc1411515937*** * | 请求ID。 |

**示例**

DataWorks 请求示例

```
&AppGuid=odps.some_engine_name &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937****</RequestId> <Data>
    <Comment>备注</Comment>
    <ModifyTime>1541576644000</ModifyTime>
    <OwnerName>323</OwnerName>
    <ProjectNameCn>测试项目</ProjectNameCn>
    <ProjectName>test</ProjectName>
    <CreateTime>1541576644000</CreateTime>
    <ProjectId>22</ProjectId>
    <AppGuid>odps.engine_name</AppGuid>
    <EnvType>1</EnvType>
    <Name>abc</Name>
    <Type>hive</Type>
    <TenantId>233</TenantId>
    <OwnerId>23</OwnerId>
    <Endpoint>http://service.odpsstg.aliyun-inc.com/</Endpoint>
    <ClusterBizId>abc</ClusterBizId>
    <Location>hdfs://</Location>
</Data>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1411515937****",
    "Data": {
        "Comment": "备注",
        "ModifyTime": 1541576644000,
        "OwnerName": 323,
```

`"ProjectNameCn": "`测试项目`",`

```json
        "ProjectName": "test",
        "CreateTime": 1541576644000,
        "ProjectId": 22,
        "AppGuid": "odps.engine_name",
        "EnvType": 1,
        "Name": "abc",
        "Type": "hive",
        "TenantId": 233,
        "OwnerId": 23,
        "Endpoint": "http://service.odpsstg.aliyun-inc.com/",
        "ClusterBizId": "abc",
        "Location": "hdfs://"
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.AppNo tExist | The MaxCompute project does not exist. | MaxCompute项目不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

#### GetMetaDBTableList

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaDBTabl eList | 系统规定参数。取值： GetMetaDBTableList。 |
| AppGuid | String | 是 | odps.testProject Name | 项目的唯一标识，格式为odps. {projectName}。仅当数据类型为odps 时，需要配置该参数。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| PageNumber | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大为 100条。 |
| ClusterId | String | 否 | abc | EMR集群的ID，仅当数据类型为emr时， 需要配置该参数。 |

DataWorks

| DatabaseName | String | 否 | abc | 数据库的名称。 |
|---|---|---|---|---|
| DataSourceType | String | 否 | odps | 数据类型，目前仅支持odps和emr。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| PageNumber | Integer | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大为100条。 |
| TableEntityList | Array of TableEntityList |  | 实例数据列表。 |
| DatabaseNam e | String | abc | 数据库的名称。 |
| TableGuid | String | odps.engine name. _ tname | 表的唯一标识。 |
| TableName | String | tname | 表的名称。 |
| TotalCount | Long | 20 | 计算引擎的总数。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaDBTableList &AppGuid=odps.testProjectName &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <Data>
    <TotalCount>20</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <TableEntityList>
        <TableName>tname</TableName>
        <TableGuid>odps.engine_name.tname</TableGuid>
        <DatabaseName>abc</DatabaseName>
    </TableEntityList>
</Data>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "Data": {
        "TotalCount": 20,
        "PageSize": 10,
        "PageNumber": 1,
        "TableEntityList": {
            "TableName": "tname",
            "TableGuid": "odps.engine_name.tname",
            "DatabaseName": "abc"
        }
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.AppNo tExist | The MaxCompute project does not exist. | MaxCompute项目不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |

DataWorks

| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

#### GetMetaCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaCategor y | 系统规定参数。取值： GetMetaCategory。 |
| ParentCategoryI d | Long | 是 | 333 | 类目树的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| PageNum | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| DataEntityList | Array of DataEntityList |  | Data实例列表。 |
| CategoryId | Long | 133 | 类目的ID。 |
| Comment | String | category 1 | 类目的备注信息。 |
| CreateTime | Long | 1541576644000 | 创建类目的时间。 |
| Depth | Integer | 1 | 类目的层数。 |
| LastOperatorId | String | 12345 | 上一次操作的用户ID。 |
| ModifiedTime | Long | 1541576644000 | 修改类目的时间。 |
| Name | String | category 1 | 类目的名称。 |
| OwnerId | String | 123 | 类目所有者的ID。 |
| ParentCategor yId | Long | 12 | 父类目的ID。 |
| PageNum | Integer | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Long | 10 | 类目的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |

DataWorks

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
&ParentCategoryId=333 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>10</TotalCount>
    <PageSize>10</PageSize>
    <PageNum>1</PageNum>
    <DataEntityList>
        <CategoryId>133</CategoryId>
        <Comment>category 1</Comment>
        <OwnerId>123</OwnerId>
        <ModifiedTime>1541576644000</ModifiedTime>
        <LastOperatorId>12345</LastOperatorId>
        <CreateTime>1541576644000</CreateTime>
        <Depth>1</Depth>
        <ParentCategoryId>12</ParentCategoryId>
        <Name>category 1</Name>
    </DataEntityList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 10,
        "PageSize": 10,
        "PageNum": 1,
        "DataEntityList": {
            "CategoryId": 133,
            "Comment": "category 1",
            "OwnerId": 123,
            "ModifiedTime": 1541576644000,
            "LastOperatorId": 12345,
            "CreateTime": 1541576644000,
            "Depth": 1,
            "ParentCategoryId": 12,
            "Name": "category 1"
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |

DataWorks

| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
|---|---|---|---|
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 403 | Invalid.Meta.Categ oryForbidden | Failed to delete the category. The current category is associated with a table and cannot be operated. | 类目删除失败，当前类目存在关联表，不能进行操作。 |
| 400 | Invalid.Meta.Categ oryIllegalDepth | A category can contain a maximum of 4 levels. | 类目层级超过4级。 |
| 403 | Invalid.Meta.Categ oryIllegalTenant | The tenant ID is different in the parent and child categories. | 父子类目的租户ID不一致。 |
| 400 | Invalid.Meta.Categ oryNameDuplicate | The category name is duplicated at this level. | 同一层级下，类目名称重复。 |
| 500 | Invalid.Meta.Categ oryRelationDuplicat e" | The table is already bound to the category. | 类目已经关联该表。 |
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaColumnLineage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetMetaColumn Lineage | 系统规定参数。取值： GetMetaColumnLineage。 |
|---|---|---|---|---|
| ColumnGuid | String | 是 | odps.engine na _ me.table name. _ column name _ | 字段的唯一标识。 |
| Direction | String | 是 | up | 字段的上下游方向：up表示上游，down 表示下游。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| PageNum | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ClusterId | String | 否 | abc | EMR集群的ID，针对EMR情况。 |
| DatabaseName | String | 否 | abc | 数据库的名称。 |
| TableName | String | 否 | abc | 表名称。 |
| ColumnName | String | 否 | abc | 字段名称。 |
| DataSourceType | String | 否 | emr | 数据类型，包括odps或emr。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| DataEntityList | Array of DataEntityList |  | 实例数据列表。 |
| ClusterId | String | abc | emr集群id |
| ColumnGuid | String | odps.engine name. _ table name.1 _ | 字段的唯一标识。 |
| ColumnName | String | 1 | 字段的名称。 |

DataWorks

| DatabaseNam e | String | abc | 数据库名称 |
|---|---|---|---|
| TableName | String | abc | 表名 |
| PageNum | Integer | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Long | 20 | 字段的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaColumnLineage &ColumnGuid=odps.engine_name.table_name.column_name &Direction=up &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>20</TotalCount>
    <PageSize>10</PageSize>
    <PageNum>1</PageNum>
    <DataEntityList>
        <TableName>abc</TableName>
        <ColumnName>1</ColumnName>
        <ColumnGuid>odps.engine_name.table_name.1</ColumnGuid>
        <ClusterId>abc</ClusterId>
        <DatabaseName>abc</DatabaseName>
    </DataEntityList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 20,
        "PageSize": 10,
        "PageNum": 1,
        "DataEntityList": {
            "TableName": "abc",
            "ColumnName": 1,
            "ColumnGuid": "odps.engine_name.table_name.1",
            "ClusterId": "abc",
            "DatabaseName": "abc"
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaMetrics

获取概览数据，包含instance数目、storage数据等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetMetaMetrics | 系统规定参数。取值： GetMetaMetrics。 |
|---|---|---|---|---|
| DataSourceType | String | 是 | odps | 数据源类型，支持odps和emr。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| Data | Struct |  |  | 返回数据对象。 |
| LargestProject s | Array of LargestProject s |  |  | 存储量最大的项目列表。 |
| DataSize | Long |  | 100 | 数据大小。 |
| ProjectName | String |  | project1 | 项目名称。 |
| LargestTables | Array of LargestTables |  |  | 存储量最大的表。 |
| DataSize | Long |  | 100 | 数据大小。 |
| TableGuid | String |  | odps.project1.table | 表Guid，格式为 odps.${projectName}.${tableName} 。 |
|  |  |  | 1 |  |
| TableName | String |  | table1 | 表名称。 |
| TotalClusters | String |  | 10 | 全部emr集群数量。 |
| TotalProjects | String |  | 10 | 全部odps项目数量。 |
| TotalStorage | Long |  | 10 | 总的存储量。 |
| TotalTables | String |  | 10 | 全部表数量 |
| ErrorCode | String |  | success | 错误码。 |

DataWorks

| ErrorMessage | String | success | 错误消息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | http状态码，成功时200，其他情况非200。 |
| RequestId | String | EESDFAFBADSF123 3 | 请求ID。 |
| Success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
&DataSourceType=odps &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>EESDFAFBADSF1233</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalProjects>10</TotalProjects>
    <TotalStorage>10</TotalStorage>
    <TotalClusters>10</TotalClusters>
    <TotalTables>10</TotalTables>
    <LargestTables>
        <TableName>table1</TableName>
        <TableGuid>odps.project1.table1</TableGuid>
        <DataSize>100</DataSize>
    </LargestTables>
    <LargestProjects>
        <ProjectName>project1</ProjectName>
        <DataSize>100</DataSize>
    </LargestProjects>
</Data> <ErrorCode>success</ErrorCode> <ErrorMessage>success</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{"RequestId":"EESDFAFBADSF1233","HttpStatusCode":"200","Data": {"TotalProjects":"10","TotalStorage":"10","TotalClusters":"10","TotalTables":"10","Larges ables": [{"TableName":"table1","TableGuid":"odps.project1.table1","DataSize":"100"}],"LargestProj ts": [{"ProjectName":"project1","DataSize":"100"}]},"ErrorCode":"success","ErrorMessage":"succ s","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |

#### GetMetaStorageTrend

获取存储趋势。

**请求参数**

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaStorage Trend | 系统规定参数。取值： GetMetaStorageTrend。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回数据对象。 |
| TableEntityList | Array of TableEntityList |  | table对象列表。 |
| Date | String | 2021-12-23 | 时间格式：yyyy-MM-dd。 |
| Storage | Long | 12343 | 存储量大小。 |
| Value | Long | 1233 | 存储量大小。 |
| TotalCount | Long | 10 | 总的数据量。 |
| ErrorCode | String | success | 错误码。 |
| ErrorMessage | String | success | 错误消息。 |
| HttpStatusCod e | Integer | 200 | http状态码，成功的时候200。 |
| RequestId | String | ADSFDSFWEWE | 请求ID。 |
| Success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaStorageTrend &RegionId=default
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<RequestId>ADSFDSFWEWE</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>10</TotalCount>
    <TableEntityList>
        <Storage>12343</Storage>
        <Value>1233</Value>
        <Date>2021-12-23</Date>
    </TableEntityList>
</Data> <ErrorCode>success</ErrorCode> <ErrorMessage>success</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{"RequestId":"ADSFDSFWEWE","HttpStatusCode":"200","Data": {"TotalCount":"10","TableEntityList":[{"Storage":"12343","Value":"1233","Date":"2021-12 -23"}]},"ErrorCode":"success","ErrorMessage":"success","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |

DataWorks

| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
|---|---|---|---|
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |

#### GetMetaTableBasicInfo

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableBa sicInfo | 系统规定参数。取值： GetMetaTableBasicInfo。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | MaxCompute表的唯一标识。格式为 odps.projectName.tableName。 |
| ClusterId | String | 否 | abc | emr集群的ID，仅当数据类型为emr时， 需要配置该参数。 您可以登录emr的控制台，获取集群ID。 |
| DatabaseName | String | 否 | abc | 数据库的名称。 |
| TableName | String | 否 | abc | 表的名称。 |
| DataSourceType | String | 否 | emr | 数据类型，包括odps和emr。 |
| Extension | Boolean | 否 | false | 是否包含扩展字段。 扩展字段包含读取次数、收藏次数、浏览次数等。 仅当数据类型为ODPS时，该参数生效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |

DataWorks

| Caption | String | 中文名 | 表的中文名称。 |
|---|---|---|---|
| ClusterId | String | abc | EMR集群的ID。 |
| ColumnCount | Integer | 3 | 字段的个数。 |
| Comment | String | test table | 表的描述。 |
| CreateTime | Long | 1589870294000 | 创建表的时间。 |
| DataSize | Long | 10 | 表占用的存储空间。单位为Byte。 |
| DatabaseNam e | String | abc | 数据库的名称。 |
| EnvType | Integer | 1 | 环境类型，取值如下： 0表示开发表。 1表示生产表。 |
| FavoriteCount | Long | 6 | 表的收藏次数。仅当Extension参数取值为true 时才会返回该参数，并且该参数仅对odps数据类型生效。 |
| IsPartitionTabl e | Boolean | true | 是否为分区表，取值如下： true：是分区表。 false：不是分区表。 |
| IsView | Boolean | false | 是否为视图，取值如下： true：是视图。 false：不是视图。 |
| IsVisible | Integer | 1 | 表的可见性： 0表示目标表对工作空间成员可见。 1表示目标表对租户内成员可见。 2表示目标表对租户间成员均可见。 3表示目标表仅对责任人可见。 |
| LastAccessTim e | Long | 1589870294000 | 最近一次访问表的时间。 |
| LastDdlTime | Long | 1589870294000 | 最近一次变更表结构的时间。 |
| LastModifyTim e | Long | 1589870294000 | 最近一次更新表的时间。 |

DataWorks

| LifeCycle | Integer | 5 | 表的生命周期。单位为天。 |
|---|---|---|---|
| Location | String | hdfs:// | Hive数据库的存储地址。 |
| OwnerId | String | 123 | 表所有者的ID。 |
| PartitionKeys | String | ab | Hive分区。 |
| ProjectId | Long | 232 | 工作空间的ID。 |
| ProjectName | String | test | 工作空间的名称。 |
| ReadCount | Long | 3 | 表的读取次数。仅当Extension参数取值为true 时才会返回该参数，并且该参数仅对odps数据类型生效。 |
| TableGuid | String | odps.engine name. _ table name _ | 表的唯一标识。 |
| TableName | String | odps.engine name. _ table name _ | 表的名称。 |
| TenantId | Long | 12345 | 租户ID。 |
| ViewCount | Long | 2 | 表的浏览次数。仅当Extension参数取值为true 时才会返回该参数，并且该参数仅对odps数据类型生效。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1411515937 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=GetMetaTableBasicInfo &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <IsView>false</IsView>
    <LifeCycle>5</LifeCycle>
    <IsPartitionTable>true</IsPartitionTable>
    <ProjectName>test</ProjectName>
    <LastAccessTime>1589870294000</LastAccessTime>
    <LastModifyTime>1589870294000</LastModifyTime>
    <EnvType>1</EnvType>
    <OwnerId>123</OwnerId>
    <DataSize>10</DataSize>
    <PartitionKeys>ab</PartitionKeys>
    <Comment>test table</Comment>
    <ColumnCount>3</ColumnCount>
    <ClusterId>abc</ClusterId>
    <LastDdlTime>1589870294000</LastDdlTime>
    <CreateTime>1589870294000</CreateTime>
    <DatabaseName>abc</DatabaseName>
    <ProjectId>232</ProjectId>
    <ViewCount>2</ViewCount>
    <Caption>中文名</Caption>
    <TableName>odps.engine_name.table_name</TableName>
    <TenantId>12345</TenantId>
    <TableGuid>odps.engine_name.table_name</TableGuid>
    <FavoriteCount>6</FavoriteCount>
    <IsVisible>1</IsVisible>
    <ReadCount>3</ReadCount>
    <Location>hdfs://</Location>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1411515937",
    "HttpStatusCode": 200,
    "Data": {
        "IsView": false,
        "LifeCycle": 5,
        "IsPartitionTable": true,
        "ProjectName": "test",
        "LastAccessTime": 1589870294000,
        "LastModifyTime": 1589870294000,
        "EnvType": 1,
        "OwnerId": 123,
        "DataSize": 10,
        "PartitionKeys": "ab",
        "Comment": "test table",
        "ColumnCount": 3,
        "ClusterId": "abc",
        "LastDdlTime": 1589870294000,
        "CreateTime": 1589870294000,
        "DatabaseName": "abc",
        "ProjectId": 232,
        "ViewCount": 2,
```

`"Caption": "`中文名`",`

```json
        "TableName": "odps.engine_name.table_name",
        "TenantId": 12345,
        "TableGuid": "odps.engine_name.table_name",
        "FavoriteCount": 6,
        "IsVisible": 1,
        "ReadCount": 3,
        "Location": "hdfs://"
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |

DataWorks

| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
|---|---|---|---|
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |

#### GetMetaTableColumn

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableCo lumn | 系统规定参数。取值： GetMetaTableColumn。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。您可以通过调用 GetMetaDBTableList，获取表的唯一标识。 |
|---|---|---|---|---|
| PageNum | Integer | 否 | 1 | 请求获取的数据页码数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ClusterId | String | 否 | C- 010A704DA760* *** | EMR集群的ID，您可以登录EMR管理控制台，获取集群ID。 |
| DatabaseName | String | 否 | abc | EMR的数据库名称。 |
| TableName | String | 否 | abc | EMR的表名称。您可以通过调用 GetMetaDBTableList接口，获取表名称。 |
| DataSourceType | String | 否 | emr | 数据类型，当前仅支持取值为emr。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| ColumnList | Array of ColumnList |  | 字段的信息。 |
| Caption | String | data column | 字段的描述。 |
| ColumnGuid | String | odps.engine name. _ table name.name _ | 字段的唯一标识。 |
| ColumnName | String | name | 字段的名称。 |
| ColumnType | String | string | 字段的类型。 |
| Comment | String | comment | 字段的备注。 |
| IsForeignKey | Boolean | true | 字段是否为外键，取值如下： true，是外键。 false，不是外键。 |

DataWorks

| IsPartitionColu mn | Boolean | false | 字段是否为分区字段，取值如下： true，是分区字段。 false，不是分区字段。 |
|---|---|---|---|
| IsPrimaryKey | Boolean | false | 字段是否为主键，取值如下： true，是主键。 false，不是主键。 |
| Position | Integer | 1 | 字段的排序。 |
| RelationCount | Long | 2 | 字段热度。 |
| PageNum | Integer | 1 | 请求获取的数据页码数，用于翻页。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Long | 100 | 字段的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableColumn &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNum>1</PageNum>
    <ColumnList>
        <Comment>comment </Comment>
        <ColumnName>name</ColumnName>
        <ColumnGuid>odps.engine_name.table_name.name</ColumnGuid>
        <ColumnType>string</ColumnType>
        <Position>1</Position>
        <IsPartitionColumn>false</IsPartitionColumn>
        <IsForeignKey>true</IsForeignKey>
        <Caption>data column</Caption>
        <IsPrimaryKey>false</IsPrimaryKey>
    </ColumnList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNum": 1,
        "ColumnList": {
            "Comment": "comment",
            "ColumnName": "name",
            "ColumnGuid": "odps.engine_name.table_name.name",
            "ColumnType": "string",
            "Position": 1,
            "IsPartitionColumn": false,
            "IsForeignKey": true,
            "Caption": "data column",
            "IsPrimaryKey": false
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

DataWorks

| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
|---|---|---|---|
| 400 | InvalidParameter.M eta.GuidFormat | The GUID format is invalid. | Guid信息错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

#### GetMetaTableChangeLog

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableCh angeLog | 系统规定参数。取值： GetMetaTableChangeLog。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识，格式为 odps.projectName.tableName。您可以通过调用GetMetaDBTableList，获取表的唯一标识。 说明当前仅支持 GetMetaTableChangeLog调用获取MaxCompute表的变更日志。 |
| PageNumber | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ChangeType | String | 否 | ALTER TABLE _ | 变更类型，包括CREATE TABLE、 _ ALTER TABLE、DROP TABLE、 _ _ ADD PARTITION和DROP PARTITION。 _ _ |
| ObjectType | String | 否 | TABLE | 变更主体类别，包括TABLE和 PARTITION。 |
| StartDate | String | 否 | 2020-06-01 00:00:00 | 表变更的开始日期，格式为yyyy-MM-dd HH:mm:ss。 如果输入的日期校验失败，则系统默认获取当前时间为表变更的开始日期。 当输入的变更开始日期和结束日期都校验失败时，则系统自动获取最近30天的表变更记录。 |
| EndDate | String | 否 | 2020-06-02 00:00:00 | 表变更的结束日期，格式为yyyy-MM-dd HH:mm:ss。 如果输入的日期校验失败，则系统默认获取当前时间为表变更的结束日期。 当输入的变更开始日期和结束日期都校验失败时，则系统自动获取最近30天的表变更记录。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Struct |  | 业务数据。 |
|---|---|---|---|
| DataEntityList | Array of DataEntityList |  | 实例列表。 |
| ChangeConten t | String | " [{\"action\":\"ADD _ COLUMN\",\"value\" : [{\"originName\":\" \",\"originType\":\"\ ",\"originComment\ ":\"\",\"name\":\"id\ ",\"type\":\"struct< name:string>\",\"c omment\":\"\"}]}]", | 变更的内容。 |
| ChangeType | String | CREATE TABLE _ | 变更的类型。 |
| CreateTime | Long | 1590722845000 | 创建表的时间。 |
| ModifiedTime | Long | 1590722845000 | 修改表的时间。 |
| ObjectType | String | TABLE | 变更主体的类别，包括TABLE和PARTITION。 |
| Operator | String | abc | 操作者的名称。 |
| PageNumber | Integer | 10 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 1 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Long | 10 | 表的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

DataWorks 请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableChangeLog &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>10</TotalCount>
    <PageSize>1</PageSize>
    <PageNumber>10</PageNumber>
    <DataEntityList>
        <Operator>abc</Operator>
        <ObjectType>TABLE</ObjectType>
        <ChangeContent>"[{\"action\":\"ADD_COLUMN\",\"value\":
[{\"originName\":\"\",\"originType\":\"\",\"originComment\":\"\",\"name\":\"id\",\"type\" "struct&lt;name:string&gt;\",\"comment\":\"\"}]}]",</ChangeContent>
        <ModifiedTime>1590722845000</ModifiedTime>
        <CreateTime>1590722845000</CreateTime>
    </DataEntityList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 10,
        "PageSize": 1,
        "PageNumber": 10,
        "DataEntityList": {
            "Operator": "abc",
            "ObjectType": "TABLE",
            "ChangeContent": "\"[{\\\"action\\\":\\\"ADD_COLUMN\\\",\\\"value\\\":
[{\\\"originName\\\":\\\"\\\",\\\"originType\\\":\\\"\\\",\\\"originComment\\\":\\\"\\\", \"name\\\":\\\"id\\\",\\\"type\\\":\\\"struct&lt;name:string&gt;\\\",\\\"comment\\\":\\\" \"}]}]\",",
            "ModifiedTime": 1590722845000,
            "ChangeType": "CREATE_TABLE",
            "CreateTime": 1590722845000
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |

DataWorks

| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
|---|---|---|---|
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaTableFullInfo

调用GetMetaTableFullInfo接口，获取表的完整信息（包括字段信息）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableFu llInfo | 系统规定参数。取值： GetMetaTableFullInfo。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。您可以通过调用 GetMetaDBTableList，获取表的唯一标识。 |
| PageNum | Integer | 否 | 1 | 请求获取的页码数，用于分页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ClusterId | String | 否 | C- 010A704DA760* *** | EMR集群的ID，您可以登录EMR管理控制台，获取集群ID。 |

DataWorks

| DatabaseName | String | 否 | abc | EMR的数据库名称。您可以通过调用 ListMetaDB接口，获取数据库名称。 |
|---|---|---|---|---|
| TableName | String | 否 | abc | EMR的表名称。您可以通过调用 GetMetaDBTableList接口，获取表名称。 |
| DataSourceType | String | 否 | emr | 数据类型，当前仅支持取值为emr。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| ClusterId | String | C- 010A704DA760*** * | EMR集群的ID。 |
| ColumnList | Array of ColumnList |  | 字段列表。 |
| Caption | String | data comment | 字段的描述信息。 |
| ColumnGuid | String | odps.engine name. _ table name.1 _ | 字段的唯一标识。 |
| ColumnName | String | name1 | 字段的名称。 |
| ColumnType | String | string | 字段的类型。 |
| Comment | String | comment | 字段的备注。 |
| IsForeignKey | Boolean | false | 段是否为外键，取值如下： true，是外键。 false，不是外键。 |
| IsPartitionColu mn | Boolean | false | 字段是否为分区字段，取值如下： true，是分区字段。 false，不是分区字段。 |
| IsPrimaryKey | Boolean | false | 字段是否为主键，取值如下： true，是主键。 false，不是主键。 |

DataWorks

| Position | Integer | 1 | 字段的排序。 |
|---|---|---|---|
| Comment | String | comment | 表的备注信息。 |
| CreateTime | Long | 1589870293000 | 创建表的时间。该结果显示为时间戳，您可以根据使用的时区将时间戳转换为相应日期。 |
| DataSize | Long | 10 | 表占用的存储空间，单位为字节（B）。 |
| DatabaseNam e | String | abc | 数据库的名称。 |
| EnvType | Integer | 0 | 环境类型，取值如下： 0表示开发环境的表。 1表示生产环境的表。 |
| IsVisible | Integer | 1 | 表是否可见，取值如下： 0表示该表对工作空间成员可见。 1表示该表对租户内可见。 2表示该表在租户间均可见。 3表示该表仅对责任人可见。 |
| LastAccessTim e | Long | 1589870294000 | 最后一次访问表的时间。该结果显示为时间戳， 您可以根据使用的时区将时间戳转换为相应日期。 |
| LastDdlTime | Long | 1589870294000 | 最后变更表结构的时间。该结果显示为时间戳， 您可以根据使用的时区将时间戳转换为相应日期。 |
| LastModifyTim e | Long | 1589870294000 | 最后更新表的时间。该结果显示为时间戳，您可以根据使用的时区将时间戳转换为相应日期。 |
| LifeCycle | Integer | 5 | 表的生命周期，单位为天。 |
| Location | String | hdfs://localhost:77 7/user/hadoop/test. txt | Hive表的存储地址。 |
| OwnerId | String | 124 | 表所有者的ID。 |
| PartitionKeys | String | abc | 分区键。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |

DataWorks

| ProjectName | String | test | 表所在工作空间的名称。 |
|---|---|---|---|
| TableGuid | String | odps.engine name. _ table name _ | 表的唯一标识。 |
| TableName | String | table-test | 表的名称。 |
| TenantId | Long | 10002 | 租户ID。 |
| TotalColumnC ount | Long | 22 | 字段的总数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableFullInfo &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <LifeCycle>5</LifeCycle>
    <Comment>comment</Comment>
    <ClusterId>C-010A704DA760****</ClusterId>
    <ProjectName>test</ProjectName>
    <LastDdlTime>1589870294000</LastDdlTime>
    <TotalColumnCount>22</TotalColumnCount>
    <CreateTime>1589870293000</CreateTime>
    <DatabaseName>abc</DatabaseName>
    <ProjectId>10001</ProjectId>
    <LastAccessTime>1589870294000</LastAccessTime>
    <LastModifyTime>1589870294000</LastModifyTime>
    <EnvType>0</EnvType>
    <TableName>table-test</TableName>
    <TenantId>10002</TenantId>
    <TableGuid>odps.engine_name.table_name</TableGuid>
    <OwnerId>124</OwnerId>
    <DataSize>10</DataSize>
    <PartitionKeys>abc</PartitionKeys>
    <IsVisible>1</IsVisible>
    <Location>hdfs://localhost:777/user/hadoop/test.txt</Location>
    <ColumnList>
        <Comment>comment</Comment>
        <ColumnName>name1</ColumnName>
        <ColumnGuid>odps.engine_name.table_name.1</ColumnGuid>
        <ColumnType>string</ColumnType>
        <Position>1</Position>
        <IsPartitionColumn>false</IsPartitionColumn>
        <IsForeignKey>false</IsForeignKey>
        <Caption>data comment</Caption>
        <IsPrimaryKey>false</IsPrimaryKey>
    </ColumnList>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data": {"LifeCycle":"5","Comment":"comment","ClusterId":"C- 010A704DA760****","ProjectName":"test","LastDdlTime":"1589870294000","TotalColumnCount":" ","CreateTime":"1589870293000","DatabaseName":"abc","ProjectId":"10001","LastAccessTime": 589870294000","LastModifyTime":"1589870294000","EnvType":"0","TableName":"table-test"," TenantId":"10002","TableGuid":"odps.engine_name.table_name","OwnerId":"124","DataSize":"1 ,"PartitionKeys":"abc","IsVisible":"1","Location":"hdfs://localhost:777/user/hadoop/test. t","ColumnList": [{"Comment":"comment","ColumnName":"name1","ColumnGuid":"odps.engine_name.table_name.1"," lumnType":"string","Position":"1","IsPartitionColumn":"false","IsForeignKey":"false","Cap on":"data comment","IsPrimaryKey":"false"}]},"ErrorCode":"1031203110005","ErrorMessage":"The spec ified parameters are invalid.","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |

DataWorks

| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
|---|---|---|---|
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaTableIntroWiki

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableInt roWiki | 系统规定参数。取值： GetMetaTableIntroWiki。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |
| WikiVersion | Long | 否 | 1 | 使用说明的版本。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| Content | String | # 业务需求\n\n&lt;a name=&quot;xiw5 n&quot; | 表的描述信息。 |
| CreateTime | Long | 1584444247000 | 表的创建时间。 |
| Creator | String | abc | 表的创建者。 |
| CreatorName | String | abc | 表的创建者的名称。 |

DataWorks

| ModifiedTime | Long | 1584444247000 | 表修改时间。 |
|---|---|---|---|
| Version | Long | 1 | 版本信息。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableIntroWiki &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <ModifiedTime>1584444247000</ModifiedTime>
    <Version>1</Version>
    <Content># 业务需求\n\n&amp;lt;a name=&amp;quot;xiw5n&amp;quot;</Content>
    <CreateTime>1584444247000</CreateTime>
    <Creator>abc</Creator>
    <CreatorName>abc</CreatorName>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式 DataWorks

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data": {"ModifiedTime":"1584444247000","Version":"1","Content":"# 业务需求\\n\\n&lt;a name=&quot;xiw5n&quot;","CreateTime":"1584444247000","Creator":"abc","CreatorName":"abc"} ErrorCode":"Invalid.Tenant.ConnectionNotExists","ErrorMessage":"The connection does not exist.","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### GetMetaTableLineage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableLi neage | 系统规定参数。取值： GetMetaTableLineage。 |
| Direction | String | 是 | up | 字段的上下游方向：up表示上游，down 表示下游。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |
| NextPrimaryKey | String | 否 | odps.engine na _ me.table name1 _ | 分页的逻辑，请根据请求返回参数 HasNext=true和key填写。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ClusterId | String | 否 | abc | EMR集群的ID，针对EMR情况。 |
| DatabaseName | String | 否 | abc | 数据库的名称。 |
| TableName | String | 否 | abc | 表名。 |
| DataSourceType | String | 否 | emr | 数据类型，包括odps或emr。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| DataEntityList | Array of DataEntityList |  | 表信息。 |

DataWorks

| CreateTimesta mp | Long | 1638720736000 | 创建时间。 |
|---|---|---|---|
| TableGuid | String | odps.tt.name | 表的唯一标识。 |
| TableName | String | name | 表的名称。 |
| HasNext | Boolean | true | 是否还有下一页。 |
| NextPrimaryKe y | String | odps.tt.2 | 分页的逻辑，请根据请求返回参数 HasNext=true和key填写。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableLineage &Direction=up &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <HasNext>true</HasNext>
    <NextPrimaryKey>odps.tt.2</NextPrimaryKey>
    <DataEntityList>
        <TableName>name</TableName>
        <TableGuid>odps.tt.name</TableGuid>
        <CreateTimestamp>1638720736000</CreateTimestamp>
    </DataEntityList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "HasNext": true,
        "NextPrimaryKey": "odps.tt.2",
        "DataEntityList": {
            "TableName": "name",
            "TableGuid": "odps.tt.name",
            "CreateTimestamp": 1638720736000
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.GuidFormat | The GUID format is invalid. | Guid信息错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |

DataWorks

| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
|---|---|---|---|
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

#### GetMetaTableListByCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMetaTableLis tByCategory | 系统规定参数。取值： GetMetaTableListByCategory。 |
| CategoryId | Long | 是 | 23 | 类目的ID，您可以调用 GetMetaCategory获取类目的ID。 |

DataWorks

| RegionId | String | 是 | default | 区域ID，为固定值default。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| PageNumber | Integer | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TableGuidList | List | odps.engine name. _ table name _ | 表的列表。 |
| TotalCount | Long | 20 | 表的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableListByCategory &CategoryId=23 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>20</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <TableGuidList>odps.engine_name.table_name</TableGuidList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 20,
        "PageSize": 10,
        "PageNumber": 1,
        "TableGuidList": "odps.engine_name.table_name"
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |

DataWorks

| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
|---|---|---|---|
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 403 | Invalid.Meta.Categ oryForbidden | Failed to delete the category. The current category is associated with a table and cannot be operated. | 类目删除失败，当前类目存在关联表，不能进行操作。 |
| 400 | Invalid.Meta.Categ oryIllegalDepth | A category can contain a maximum of 4 levels. | 类目层级超过4级。 |
| 403 | Invalid.Meta.Categ oryIllegalTenant | The tenant ID is different in the parent and child categories. | 父子类目的租户ID不一致。 |
| 400 | Invalid.Meta.Categ oryNameDuplicate | The category name is duplicated at this level. | 同一层级下，类目名称重复。 |
| 500 | Invalid.Meta.Categ oryRelationDuplicat e" | The table is already bound to the category. | 类目已经关联该表。 |
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaTableOutput

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetMetaTableOu tput | 系统规定参数。取值： GetMetaTableOutput。 |
|---|---|---|---|---|
| EndDate | String | 是 | 2020-05-27 | 结束日期。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| StartDate | String | 是 | 2020-06-27 | 开始日期。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |
| PageNumber | Integer | 否 | 1 | 分页的页数。默认值为1，最小值为1，最大值为30。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| DataEntityList | Array of DataEntityList |  | 实例列表。 |
| EndTime | String | 1511107200000 | 结束时间。 |
| ProjectId | Long | 333 | 工作空间的ID。 |
| StartTime | String | 1511107200000 | 开始时间。 |
| TableGuid | String | odps.engine name. _ table name _ | 表的唯一标识。 |
| TaskId | String | 32 | 节点ID。 |
| TaskInstanceId | Long | 3521 | 实例ID。 |
| WaitTime | String | 323 | 等待时间。 |

DataWorks

| PageNumber | Integer | 1 | 分页的页数。默认值为1，最小值为1，最大值为 30。 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Long | 100 | 表的总数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableOutput &EndDate=2020-05-27 &RegionId=default &StartDate=2020-06-27 &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <DataEntityList>
        <TaskInstanceId>3521</TaskInstanceId>
        <TableGuid>odps.engine_name.table_name</TableGuid>
        <TaskId>32</TaskId>
        <EndTime>1511107200000</EndTime>
        <ProjectId>333</ProjectId>
        <StartTime>1511107200000</StartTime>
        <WaitTime>323</WaitTime>
    </DataEntityList>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "DataEntityList": {
            "TaskInstanceId": 3521,
            "TableGuid": "odps.engine_name.table_name",
            "TaskId": 32,
            "EndTime": 1511107200000,
            "ProjectId": 333,
            "StartTime": 1511107200000,
            "WaitTime": 323
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaTablePartition

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetMetaTablePa rtition | 系统规定参数。取值： GetMetaTablePartition。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | 表的唯一标识。 |
| PageNumber | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ClusterId | String | 否 | abc | emr集群id。针对emr情况 |
| DatabaseName | String | 否 | abc | 数据库名称 |
| TableName | String | 否 | abc | 表名称 |
| DataSourceType | String | 否 | emr | 数据类型。odps或者emr |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 业务数据。 |
| DataEntityList | Array of DataEntityList |  | 实例列表。 |
| Comment | String | 备注 | 备注 |
| CreateTime | Long | 1590032868000 | 创建分区的时间。 |
| DataSize | Long | 19 | 分区的大小，单位为Byte。 |
| ModifiedTime | Long | 1590032868000 | 修改分区的时间。 |
| PartitionGuid | String | odps.engine name. _ table name.pt=20 _ 170614 | 分区的唯一标识。 |
| PartitionLocati on | String | abc | Hive分区的地址。 |

DataWorks

| PartitionName | String | pt=20170614 | 分区的名称。 |
|---|---|---|---|
| PartitionPath | String | abc | 分区的目录。 |
| PartitionType | String | abc | 分区的类型。 |
| RecordCount | Long | 233 | 分区的数据量。 |
| TableGuid | String | odps.engine name. _ table name _ | 表的唯一标识。 |
| PageNumber | Integer | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Long | 100 | 分区的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTablePartition &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <DataEntityList>
        <PartitionName>pt=20170614</PartitionName>
        <Comment>备注</Comment>
        <PartitionGuid>odps.engine_name.table_name.pt=20170614</PartitionGuid>
        <TableGuid>odps.engine_name.table_name</TableGuid>
        <ModifiedTime>1590032868000</ModifiedTime>
        <DataSize>19</DataSize>
        <CreateTime>1590032868000</CreateTime>
        <PartitionPath>abc</PartitionPath>
        <PartitionType>abc</PartitionType>
        <PartitionLocation>abc</PartitionLocation>
        <RecordCount>233</RecordCount>
    </DataEntityList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "DataEntityList": {
            "PartitionName": "pt=20170614",
            "Comment": "备注",
            "PartitionGuid": "odps.engine_name.table_name.pt=20170614",
            "TableGuid": "odps.engine_name.table_name",
            "ModifiedTime": 1590032868000,
            "DataSize": 19,
            "CreateTime": 1590032868000,
            "PartitionPath": "abc",
            "PartitionType": "abc",
            "PartitionLocation": "abc",
            "RecordCount": 233
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

#### ListMetaDB

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListMetaDB | 系统规定参数。取值：ListMetaDB。 |
| DataSourceType | String | 是 | emr | 数据类型，当前仅支持取值为emr。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| PageNum | Integer | 否 | 1 | 页码数。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大为 100条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DatabaseInfo | Struct |  | 数据库的信息。 |
| DbList | Array of DbList |  | 数据库列表。 |
| CreateTimeSta mp | Long | 1111176825 | 创建数据库的时间。该结果显示为时间戳，您可以根据使用的时区将时间戳转换为相应日期。 |
| Location | String | hdfs://localhost:77 7/user/hadoop/test. txt | 存储数据库的地址。 |
| ModifiedTimeS tamp | Long | 1111176825 | 更新数据库的时间。 |
| Name | String | name | 数据库的名称。 |
| OwnerId | String | 123123123 | Owner的ID。 |
| Type | String | HIVE | 数据库的类型。 |

DataWorks

| UUID | String | 32342 | 数据库的唯一标识。 |
|---|---|---|---|
| TotalCount | Long | 10 | 数据库的总数。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
&DataSourceType=emr &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <DatabaseInfo>
    <TotalCount>10</TotalCount>
    <DbList>
        <Type>HIVE</Type>
        <OwnerId>123123123</OwnerId>
        <ModifiedTimeStamp>1111176825</ModifiedTimeStamp>
        <UUID>32342</UUID>
        <CreateTimeStamp>1111176825</CreateTimeStamp>
        <Location>hdfs://localhost:777/user/hadoop/test.txt</Location>
        <Name>name</Name>
    </DbList>
</DatabaseInfo>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","DatabaseInfo":{"TotalCount":"10","DbList":[{"Type":" HIVE","OwnerId":"123123123","ModifiedTimeStamp":"1111176825","UUID":"32342","CreateTimeSt p":"1111176825","Location":"hdfs://localhost:777/user/hadoop/test.txt","Name":"name"}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 400 | Invalid.Meta.AppNo tExist | The MaxCompute project does not exist. | MaxCompute项目不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListTableLevel

调用ListTableLevel查询层级列表。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | ListTableLevel | 系统规定参数。取值：ListTableLevel。 |
|---|---|---|---|---|
| LevelType | Integer | 是 | 1 | 层级的类型，包括1（逻辑层级）和2（物理层级）。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |
| TableLevelInfo | Struct |  | 层级的信息。 |
| LevelList | Array of LevelList |  | 层级列表。 |
| Description | String | 层级的描述。 | 层级的描述。 |
| LevelId | Long | 123 | 层级ID。 |
| LevelType | Integer | 1 | 层级的类型，包括1（逻辑层级）和2（物理层级）。 |
| Name | String | 层级1 | 层级名称。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| TotalCount | Long | 10 | 层级的总数。 |

DataWorks

**示例**

请求示例

```
&LevelType=1 &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TableLevelInfo>
    <TotalCount>10</TotalCount>
    <LevelList>
```

`<Description>`层级的描述。`</Description>`

```xml
        <LevelType>1</LevelType>
        <ProjectId>10001</ProjectId>
        <LevelId>123</LevelId>
        <Name>层级1</Name>
    </LevelList>
</TableLevelInfo> <RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"TableLevelInfo":{"TotalCount":"10","LevelList":[{"Description":"层级的描述。","LevelTyp e":"1","ProjectId":"10001","LevelId":"123","Name":"层级1"}]},"RequestId":"0000-ABCD-EFG*
****","HttpStatusCode":"200","ErrorCode":"1031203110005","ErrorMessage":"The specified
parameters are invalid.","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |

DataWorks

| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
|---|---|---|---|
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListTableTheme

调用ListTableTheme查询主题列表。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTableTheme | 系统规定参数。取值： ListTableTheme。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ParentId | Long | 否 | 123 | 父类ID。 |
| PageNum | Integer | 否 | 1 | 分页的页码数。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 层级数据。 |
| ThemeList | Array of ThemeList |  | 层级列表。 |
| CreateTimeSta mp | Long | 123432343243 | 创建层级的时间。 |
| Creator | String | 1234555 | 层级的创建人。 |

DataWorks

| Level | Integer | 1 | 1（一级层级）和2（二级层级）。 |
|---|---|---|---|
| Name | String | 层级的名称。 | 层级的名称。 |
| ParentId | Long | 122 | 父节点ID。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| ThemeId | Long | 123 | 主题ID。 |
| TotalCount | Long | 10 | 内容总数量。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
&ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>10</TotalCount>
    <ThemeList>
        <ParentId>122</ParentId>
        <ThemeId>123</ThemeId>
        <ProjectId>10001</ProjectId>
        <Level>1</Level>
        <Creator>1234555</Creator>
        <CreateTimeStamp>123432343243</CreateTimeStamp>
```

`<Name>`层级的名称。`</Name>`

```xml
    </ThemeList>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data": {"TotalCount":"10","ThemeList": [{"ParentId":"122","ThemeId":"123","ProjectId":"10001","Level":"1","Creator":"1234555","C ateTimeStamp":"123432343243","Name":"层级的名称。 "}]},"ErrorCode":"1031203110005","ErrorMessage":"The specified parameters are invalid." ,"Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### SearchMetaTables

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SearchMetaTabl es | 系统规定参数。取值： SearchMetaTables。 |
| AppGuid | String | 是 | odps.engine na _ me | 表所在工作空间的标识。 |
| DataSourceType | String | 是 | emr | 数据类型，包括ODPS和emr。 |
| Keyword | String | 是 | test | 关键字采用分词匹配算法搜索表名，如果没有匹配的字段则返回空值。默认按照下划线分词搜索。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| PageNumber | Integer | 否 | 1 | 分页查询页码。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| EntityType | Integer | 否 | 0 | 表的类型：0表示table，1表示view。如果不填，则默认搜索全部类型。 |
| ClusterId | String | 否 | abc | EMR集群的ID，仅当数据类型为EMR时， 需要配置该参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回数据。 |
| DataEntityList | Array of DataEntityList |  | 实例列表。 |

DataWorks

| ClusterId | String | abc | EMR集群ID。 |
|---|---|---|---|
| DatabaseNam e | String | abc | 数据库名称。 |
| EntityType | Integer | 0 | 表的类型： 0表示table。 1表示view。 |
| EnvType | Integer | 1 | 环境类型： 1表示生产环境。 0表示开发环境。 |
| OwnerId | String | 123 | 工作空间Owner的云账号ID。 |
| ProjectId | Long | 323 | 工作空间的ID。 |
| ProjectName | String | test | 工作空间的名称。 |
| TableGuid | String | odps.engine name. _ test name _ | 表的唯一标识。 |
| TableName | String | test name _ | 表的名称。 |
| TenantId | Long | 12345 | 租户ID。 |
| PageNumber | Integer | 1 | 分页查询页码。 |
| PageSize | Integer | 10 | 分页查询每页的大小。 |
| TotalCount | Long | 100 | 表的总数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |

DataWorks

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
&AppGuid=odps.engine_name &DataSourceType=emr &Keyword=test &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <DataEntityList>
        <EntityType>0</EntityType>
        <TableName>test_name</TableName>
        <TenantId>12345</TenantId>
        <TableGuid>odps.engine_name.test_name</TableGuid>
        <OwnerId>123</OwnerId>
        <ClusterId>abc</ClusterId>
        <ProjectName>test</ProjectName>
        <ProjectId>323</ProjectId>
        <DatabaseName>abc</DatabaseName>
        <EnvType>1</EnvType>
    </DataEntityList>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "DataEntityList": {
            "EntityType": 0,
            "TableName": "test_name",
            "TenantId": 12345,
            "TableGuid": "odps.engine_name.test_name",
            "OwnerId": 123,
            "ClusterId": "abc",
            "ProjectName": "test",
            "ProjectId": 323,
            "DatabaseName": "abc",
            "EnvType": 1
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 400 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 400 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目获取计算引擎失败。 |

DataWorks

| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
|---|---|---|---|
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |
| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |

#### SearchMetaTableByKey

提供基于关键词的元数据表搜索功能，帮助用户快速定位目标数据表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| Keyword | Strin g | Query | 否 | ODPS SQL | 关键字。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TenantId | Long | Query | 是 | 10241024 | 租户ID。您可登录 DataWorks控制台，进入数据开发（DataStudio） 页面，单击右上方当前登录用户名称，选择菜单 > 用户信息，获取租户ID。 |
| AppGuid | Strin g | Query | 否 | odps.test | MaxCompute项目的唯一标识，格式为odps. {projectName}。 |
| TableGuid | Repe atList | Query | 否 | odps.engine name.table _ name _ | 表的唯一标识。 |
| LoginNam e | Strin g | Query | 否 | testuser | 用户登录名。 |
| UserAcces sKeyId | Strin g | Query | 否 | CU********Yh | 生产云运营管理员的AK。 |
| Pk | Strin g | Query | 否 | 259258662544****** | 用户账号的主键。 若仅传入 pk参数，则根据pk参数查询。若传入请求参数 LoginName和 UserAccessKeyId中的任意一个，则可不传入此参数。若请求参数都不传，则返回报错。 |
| RoleCode | Strin g | Query | 否 | role project guest _ _ | DataWorks工作空间角色的Code。您可以调用 ListProjectRoles获取角色的Code。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNumber | Long | Query | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Long | Query | 否 | 100 | 每页显示的数据条数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | { "HttpStatusCode": 200, "Success": true } | 返回结果数据。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TableGuid | String | odps.engine name. _ table name _ | 表的唯一标识。 |
| -Guid | String | odps.autotest.test _ output table 1 _ _ | 表id。 |
| -AppGuid | String | odps.engine name _ | 引擎ID，格式为引擎类型.引擎名称 。 |
| -ProjectId | Long | 1234 | 工作空间的ID。 |
| -EnvType | Integer | 0 | 表所属环境。取值范围： 0：DEV，开发环境 1：PROD，生产环境 |
| -ProjectName | String | autotest | 工作空间的显示名称。 |
| -LastDdlTime | String | 1589870294000 | 最近一次变更表结构的时间。该结果显示为时间戳，您可以根据使用的时区将时间戳转换为相应日期。 |
| -CreateTime | String | 1710239005403 | 实例的创建时间。该结果显示为时间戳，您可以根据使用的时区将时间戳转换为相应日期。 |
| - LastModifyTim e | String | 1589870294000 | 最后更新表的时间。该结果显示为时间戳，您可以根据使用的时区将时间戳转换为相应日期。 |
| -OwnerId | String | 123 | 负责人的ID。 |
| - LastAccessTim e | String | 1589870294000 | 最近一次访问表的时间。该结果显示为时间戳， 您可以根据使用的时区将时间戳转换为相应日期。 |
| -DataSize | Long | 10 | 表占用的存储空间。单位为Byte。 |
| -Type | String | Fixed | 阈值计算方式。取值范围： Fixed Fluctation FluctationDiscreate Auto Average Variance |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Comment | String | test | 本次文件版本的说明。 |
| -IsVisible | Integer | 1 | 表的可见性。取值范围： 0：目标表对工作空间成员可见 1：目标表对租户内成员可见 2：目标表对租户间成员均可见 3：目标表仅对责任人可见 |
| -IsView | Integer | 0 | 是否为视图，取值范围： 1：true，是视图 0：false，不是视图 |
| -TenantId | String | 1 | 租户ID。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SearchMetaTableByKey &RegionId=default &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "Data":[
  {
   "IsView":0,
   "Comment":"test",
   "ProjectName":"autotest",
   "LastDdlTime":"1589870294000",
   "CreateTime":"1710239005403",
   "ProjectId":1234,
   "AppGuid":"odps.engine_name",
   "Guid":"odps.autotest.test_output_table_1",
   "LastModifyTime":"1589870294000",
   "LastAccessTime":"1589870294000",
   "EnvType":0,
   "TableGuid":"odps.engine_name.table_name",
   "Type":"Fixed",
   "TenantId":"1",
   "OwnerId":"123",
   "DataSize":10,
   "IsVisible":1
  }
```

]

```
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <Data>
  <IsView>0</IsView>
  <Comment>test</Comment>
  <ProjectName>autotest</ProjectName>
  <LastDdlTime>1589870294000</LastDdlTime>
  <CreateTime>1710239005403
  </CreateTime>
  <ProjectId>1234</ProjectId>
  <AppGuid>odps.engine_name</AppGuid>
  <Guid>odps.autotest.test_output_table_1</Guid>
  <LastModifyTime>1589870294000</LastModifyTime>
  <LastAccessTime>1589870294000</LastAccessTime>
  <EnvType>0</EnvType>
  <TableGuid>odps.engine_name.table_name</TableGuid>
  <Type>Fixed</Type>
  <TenantId>1</TenantId>
  <OwnerId>123</OwnerId>
  <DataSize>10</DataSize>
  <IsVisible>1</IsVisible>
</Data>
```

**错误码**

DataWorks

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 1010010013 | InternalError.Meta.NoCalcEngi ne | An error occurred while retrieving the compute engine based on the MaxCompute project. |
| 500 | 1010010015 | InternalError.Meta.TenantTime Out | Failed to connect to the interface network. |
| 500 | 1010019999 | InternalError.Meta.Unknown | An unknown error occurred while processing your request. |
| 403 | 1010010014 | Forbidden.Meta.NoTenant | The user is not the owner of any tenants. |
| 400 | 1010020001 | Invalid.Meta.AppNotExist | The MaxCompute project does not exist. |
| 400 | 1010010016 | InvalidParameter.Meta.Commo nError | The specified parameter is invalid. |
| 400 | 1010010010 | InvalidParameter.Meta.Illegal | The app guid parameter is invalid. |
| 400 | 1010010017 | InvalidParameter.Meta.IllegalD ate | The date format is invalid. |
| 400 | 1010010011 | InvalidParameter.Meta.IllegalP ageError | The parameter for paging is invalid. |
| 400 | 1010010018 | InvalidParameter.Meta.NotExis t | The object does not exist. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |

DataWorks

#### UpdateMetaCategory

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateMetaCate gory | 系统规定参数。取值： UpdateMetaCategory。 |
| CategoryId | Long | 是 | 2 | 类目的ID。 |
| Name | String | 是 | category name | 类目的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Comment | String | 否 | category name | 类目的备注信息。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否成功更新类目。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0bc1ec92159376 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateMetaCategory &CategoryId=2 &Name=category name &RegionId=default
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.Meta. NoCalcEngine | An error occurred while retrieving the compute engine based on the MaxCompute project. | 根据ODPS项目{0}获取计算引擎失败。 |
| 500 | InternalError.Meta. TenantTimeOut | Failed to connect to the interface network. | 接口网络不通。 |

DataWorks

| 500 | InternalError.Meta. Unknown | An unknown error occurred while processing your request. | 未知错误。 |
|---|---|---|---|
| 403 | Invalid.Meta.Categ oryForbidden | Failed to delete the category. The current category is associated with a table and cannot be operated. | 类目删除失败，当前类目存在关联表，不能进行操作。 |
| 400 | Invalid.Meta.Categ oryIllegalDepth | A category can contain a maximum of 4 levels. | 类目层级超过4级。 |
| 403 | Invalid.Meta.Categ oryIllegalTenant | The tenant ID is different in the parent and child categories. | 父子类目的租户ID不一致。 |
| 400 | Invalid.Meta.Categ oryNameDuplicate | The category name is duplicated at this level. | 同一层级下，类目名称重复。 |
| 500 | Invalid.Meta.Categ oryRelationDuplicat e" | The table is already bound to the category. | 类目已经关联该表。 |
| 400 | Invalid.Meta.Table NotExist | The table does not exist. | 表不存在。 |
| 400 | InvalidParameter.M eta.CommonError | The specified parameter is invalid. | 请求参数错误。 |
| 400 | InvalidParameter.M eta.Illegal | The app guid parameter is invalid. | App参数错误。 |
| 400 | InvalidParameter.M eta.IllegalDate | The date format is invalid. | 日期格式错误。 |
| 400 | InvalidParameter.M eta.IllegalPageError | The parameter for paging is invalid. | 分页信息错误。 |
| 400 | InvalidParameter.M eta.NotExist | The object does not exist. | 数据不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateMetaTable

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateMetaTabl e | 系统规定参数。取值： UpdateMetaTable。 |
| EnvType | Integer | 是 | 1 | DataWorks的环境，包括0（开发环境） 和1（生产环境）。 |

DataWorks

| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | table1 | 表的名称。 |
| TableGuid | String | 否 | odps.test.table1 | 表的唯一标识，格式为odps. {projectName}.{tableName}。 |
| NewOwnerId | String | 否 | 12345 | 新的OwnerId，为空时不更新。 |
| AddedLabels | String | 否 | a,b,c | 需要增加的标签名称，使用英文逗号（,） 分隔。 |
| RemovedLabels | String | 否 | a,b,c | 需要删除的标签名称，使用英文逗号（,） 分隔。 |
| CategoryId | Long | 否 | 101 | 需要关联的类目ID。 |
| Visibility | Integer | 否 | 1 | 编辑表的可见性，包括0（不可见）、 1（可见）和2（工作空间可见）。 |
| Caption | String | 否 | 中文名 | 表的中文名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | cn-shanghai | 地域的信息，通常是服务所在的地域。例如，华东2（上海）是cn-shanghai，华北3（张家口） 是cn-zhangjiakou。您无需填写RegionId，会根据调用的endpoint自动解析。 |
| UpdateResult | Boolean | true | 是否更新成功。 |

**示例**

请求示例

```
&EnvType=1 &ProjectId=10001 &RegionId=default &TableName=table1
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>cn-shanghai</RequestId> <UpdateResult>true</UpdateResult>
```

`JSON` 格式

```json
{"RequestId":"cn-shanghai","UpdateResult":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateMetaTableIntroWiki

调用UpdateMetaTableIntroWiki更新表的说明信息，当数据不存在时增加信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateMetaTabl eIntroWiki | 系统规定参数。取值： UpdateMetaTableIntroWiki。 |
| Content | String | 是 | abc | 表说明的详情。 |

DataWorks

| RegionId | String | 是 | default | 区域ID，为固定值default。 |
|---|---|---|---|---|
| TableGuid | String | 是 | odps.test.table1 | 表的唯一标识，格式为odsp. {projectName}.{tableName}。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 地域的信息，通常是服务所在的地域。例如，华东2（上海）是cn-shanghai，华北3（张家口） 是cn-zhangjiakou。您无需填写RegionId，会根据调用的endpoint自动解析。 |
| UpdateResult | Boolean | true | 更新结果。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateMetaTableIntroWiki &Content=abc &RegionId=default &TableGuid=odps.test.table1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <UpdateResult>true</UpdateResult>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","UpdateResult":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |

DataWorks

| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
|---|---|---|---|
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateTable

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateTable | 系统规定参数。取值：UpdateTable。 |
| Columns.N.Colu mnName | String | 是 | abc | 字段的名称。 |
| Columns.N.Colu mnType | String | 是 | string | 字段的类型，请参见MaxCompute支持的字段类型。 |
| HasPart | Integer | 是 | 0 | 需要更新的MaxCompute表是否为分区表，包括0（否）和1（是）。该字段已废弃，请勿使用。 目前代码会根据 Column.N.isPartitionCol参数判断 MaxCompute表是否为分区表，当 Column.N.isPartition参数取值为1时， 则认为MaxCompute表为分区表。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | tablename | MaxCompute表名称。 |
| Columns.N.Colu mnNameCn | String | 否 | 中文名 | 字段的中文名称。 |
| Columns.N.SeqN umber | Integer | 否 | 1 | 字段的序号。如果字段为分区字段，则不支持配置Columns.N.SeqNumber。 |
| Columns.N.Leng th | Integer | 否 | 10 | 字段的长度。 |

DataWorks

| Columns.N.IsPart itionCol | Integer | 否 | 0 | 是否为分区字段，包括0（否）和 1（是）。 |
|---|---|---|---|---|
| Columns.N.IsPri maryKey | Integer | 否 | 1 | 是否为主键字段，包括0（否）和 1（是）。 |
| Columns.N.IsNull able | Integer | 否 | 1 | 是否允许为空，包括0（否）和1（是）。 |
| Columns.N.Com ment | String | 否 | 备注 | 字段的备注。 |
| IsView | Integer | 否 | 0 | 是否为视图，包括0（否）和1（是）。该字段已废弃，请勿使用。 |
| Visibility | Integer | 否 | 1 | 表的可见性，包括0（对所有成员不可见）、1（对所有成员可见）和2（对工作空间成员可见）。 |
| LifeCycle | Integer | 否 | 10 | 表的生命周期，单位为天。生命周期为空时，表示永久存储。 |
| CategoryId | Long | 否 | 101 | 关联的类目ID。 |
| LogicalLevelId | Long | 否 | 101 | 逻辑层级ID。 |
| PhysicsLevelId | Long | 否 | 101 | 物理层级ID。 |
| ExternalTableTy pe | String | 否 | 1 | 外表的类型，包括0（OSS）、 1（TableStore）、2（Volume）和 3（MySQL）。该字段已废弃，请勿使用。 |
| Location | String | 否 | location | 外表的存储地址。该字段已废弃，请勿使用。 |
| ProjectId | Long | 否 | 10001 | DataWorks工作空间ID。 |
| Endpoint | String | 否 | odps:// | MaxCompute Endpoint。不填时，默认取项目对应的Endpoint。 |
| EnvType | Integer | 否 | 1 | DataWorks工作空间的环境，包括0（开发环境）和1（生产环境）。 |

DataWorks

| Themes.N.Them eId | Long | 否 | 101 | 关联的主题ID。 |
|---|---|---|---|---|
| Themes.N.Them eLevel | Integer | 否 | 101 | 主题ID对应的层级。 |
| AppGuid | String | 否 | odps.test | MaxCompute项目的唯一标识，格式为 odps.{projectName}。 |
| CreateIfNotExist s | Boolean | 否 | true | 表是否存在： true：是，表存在。 false：否，表不存在。 该字段已废弃，请勿使用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| TaskInfo | Struct |  | 请求任务的信息。 请求任务提交成功后，会被分为多个子任务有序执行。当前子任务执行成功后，才会继续执行下一个子任务，所有子任务执行完毕，该请求任务结束。如下情况，请求任务会终止，您需要根据错误码信息解决问题后重新发起请求任务： 请求任务提交失败。 请求任务提交成功后，任意子任务执行失败。 |
| Content | String | success | 当前子任务的执行状态详细信息。具体如下： 执行成功，则显示success。 执行失败则显示对应的报错详情。 |
| NextTaskId | String | abc1 | 即将执行的子任务ID。如果该字段为空，则表示所有子任务均已结束。您可以使用获取到的ID， 从GetDDLJobStatus接口查询对应子任务的状态。 |
| Status | String | success | 当前执行的子任务的状态信息。取值如下： operating表示子任务正在执行中。 success表示子任务执行成功。 failure表示子任务执行失败。详细的报错信息请参见Content参数。 |
| TaskId | String | abc | 当前执行的子任务ID。 |

**示例**

DataWorks 请求示例

```
&Columns.1.ColumnName=abc &Columns.1.ColumnType=string &HasPart=0 &RegionId=default &TableName=tablename
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TaskInfo>
    <Status>success</Status>
    <TaskId>abc</TaskId>
    <Content>success</Content>
    <NextTaskId>abc1</NextTaskId>
</TaskInfo> <RequestId>0000-ABCD-EFG*****</RequestId>
```

`JSON` 格式

```json
{"TaskInfo": {"Status":"success","TaskId":"abc","Content":"success","NextTaskId":"abc1"},"RequestId":" 00-ABCD-EFG*****"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### UpdateTableLevel

调用UpdateTableLevel更新层级。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateTableLev el | 系统规定参数。取值： UpdateTableLevel。 |
| LevelId | Long | 是 | 123 | 需要更新的层级ID。您可以通过ListLevel 获取。 |
| LevelType | Integer | 是 | 1 | 层级的类型，包括1（逻辑层级）和2（物理层级）。 |
| Name | String | 是 | 层级的名称。 | 层级的名称。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Description | String | 否 | 层级的描述 | 层级的描述。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

DataWorks

| UpdateResult | Boolean | false | 是否成功返回结果。 |
|---|---|---|---|

**示例**

请求示例

```
&LevelId=123 &LevelType=1
```

`&Name=`层级的名称。

```
&ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <UpdateResult>false</UpdateResult> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD- EFG*****","HttpStatusCode":"200","ErrorCode":"1031203110005","ErrorMessage":"The specif ied parameters are invalid.","UpdateResult":"false","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

DataWorks

| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateTableModelInfo

调用UpdateTableModelInfo修改表的主题、层级和物理分类等信息。不建议使用该API，后续将有新API 上线覆盖此功能。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateTableMo delInfo | 系统规定参数。取值： UpdateTableModelInfo。 |
| FirstLevelTheme Id | Long | 是 | 101 | 一级主题ID。 |
| LevelId | Long | 是 | 101 | 层级ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| SecondLevelThe meId | Long | 是 | 101 | 二级主题ID。 |
| TableGuid | String | 是 | odps.test.table1 | 表的唯一标识，格式为odps. {projectName}.{tableName}。 |
| LevelType | Integer | 否 | 1 | 层级类型，包括1（逻辑层级）和2（物理层级）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| UpdateResult | Boolean | true | 表是否更新成功。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=UpdateTableModelInfo &FirstLevelThemeId=101 &LevelId=101 &RegionId=default &SecondLevelThemeId=101 &TableGuid=odps.test.table1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <UpdateResult>true</UpdateResult>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","UpdateResult":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateTableTheme

调用UpdateTableTheme更新主题。不建议使用该API，后续将有新API上线覆盖此功能。

**请求参数**

DataWorks

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateTableThe me | 系统规定参数。取值： UpdateTableTheme。 |
| Name | String | 是 | 主题的名称 | 主题的名称。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ThemeId | Long | 是 | 123 | 主题ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | cn-shanghai | 地域的信息，通常是服务所在的地域。例如，华东2（上海）是cn-shanghai，华北3（张家口） 是cn-zhangjiakou。您无需填写RegionId，会根据调用的endpoint自动解析。 |
| Success | Boolean | false | 调用是否成功。 |
| UpdateResult | Boolean | true | 是否成功返回更新结果： true：是 false：否 |

**示例**

请求示例 `&Name=`主题的名称

```
&ProjectId=10001 &RegionId=default &ThemeId=123
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>cn-shanghai</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <UpdateResult>true</UpdateResult> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"cnshanghai","HttpStatusCode":"200","ErrorCode":"1031203110005","ErrorMessage":"The specif ied parameters are invalid.","UpdateResult":"true","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateTableAddColumn

调用UpdateTableAddColumn更新MaxCompute表的字段信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | UpdateTableAdd Column | 系统规定参数。取值： UpdateTableAddColumn。 |
|---|---|---|---|---|
| Column.N.Colum nName | String | 是 | abc | 字段的名称。 |
| Column.N.Colum nType | String | 是 | string | 字段的类型，请参见MaxCompute支持的字段类型。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.engine na _ me.table name _ | MaxCompute表的唯一标识。格式为 odps.projectName.tableName。 |
| Column.N.Colum nNameCn | String | 否 | 中文 | 字段的中文名称。 |
| Column.N.Comm ent | String | 否 | 备注 | 字段的备注信息。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | abc | 请求ID。 |
| TaskInfo | Struct |  | 请求任务的信息。 请求任务提交成功后，会被分为多个子任务有序执行。当前子任务执行成功后，才会继续执行下一个子任务，所有子任务执行完毕，该请求任务结束。如下情况，请求任务会终止，您需要根据错误码信息解决问题后重新发起请求任务： 请求任务提交失败。 请求任务提交成功后，任意子任务执行失败。 |
| Content | String | success | 当前子任务的执行状态详细信息。具体如下： 执行成功，则显示success。 执行失败则显示对应的报错详情。 |
| NextTaskId | String | abc1 | 即将执行的子任务ID。如果该字段为空，则表示所有子任务均已结束。 |
| Status | String | success | 当前执行的子任务的状态信息。取值如下： operating表示子任务正在执行中。 success表示子任务执行成功。 failure表示子任务执行失败。详细的报错信息请参见Content参数。 |

DataWorks

| TaskId | String | abc2 | 当前执行的子任务ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTableAddColumn &Column.1.ColumnName=abc &Column.1.ColumnType=string &RegionId=default &TableGuid=odps.engine_name.table_name
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TaskInfo>
    <Status>success</Status>
    <TaskId>abc2</TaskId>
    <Content>success</Content>
    <NextTaskId>abc1</NextTaskId>
</TaskInfo> <RequestId>abc</RequestId>
```

`JSON` 格式

```json
{
    "TaskInfo": {
        "Status": "success",
        "TaskId": "abc2",
        "Content": "success",
        "NextTaskId": "abc1"
    },
    "RequestId": "abc"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |

DataWorks

| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
|---|---|---|---|
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetMetaTableThemeLevel

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TableGuid | Strin g | Query | 是 | odps.project1.name1 | 表的唯一ID，格式为 odps.${projectName }.${tableName} 。 |
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |
| DataSourc eType | Strin g | Query | 是 | MaxCompute | 数据类型，目前只支持 MaxCompute。 |

|  |  | odps.${projectName |
|---|---|---|
|  | }.${tableName} |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrorMessage | String | success | 错误信息。 |
| RequestId | String | 16A96B9A-F203- 4EC5-8E43- CB92E68F**** | 请求ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorCode | String | 1010010011 | 错误码。 |
| Entity | Struct | / | 返回数据。 |
| -Theme | Array | / | 主题信息。 |
| --ParentId | Long | 0 | 父主题ID。 |
| --Name | String | level1 | 主题名称。 |
| --ThemeId | Long | 1 | 主题ID。 |
| --Level | Integer | 1 | 主题类型，取值： 1：一级主题。 2：二级主题。 |
| -Level | Array | / | 层级信息。 |
| --Type | Integer | 1 | 层级类型，取值： 1：逻辑层级。 2：物理层级。 |
| --Description | String | description test _ | 层级的描述。 |
| --Name | String | level1 | 层级名称。 |
| --LevelId | Long | 1 | 层级ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMetaTableThemeLevel &TableGuid=odps.project1.name1 &RegionId=default &DataSourceType=MaxCompute
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "Entity":{
  "Theme":[
   {
    "ParentId":0,
    "ThemeId":1,
    "Level":1,
    "Name":"level1"
   }
```

`],`

```json
  "Level":[
   {
    "Type":1,
    "Description":"description_test",
    "LevelId":1,
    "Name":"level1"
   }
```

]

```json
 },
 "RequestId":"16A96B9A-F203-4EC5-8E43-CB92E68F****",
 "HttpStatusCode":200,
 "ErrorCode":"1010010011",
 "ErrorMessage":"success",
 "Success":true
}
```

`XML` 格式

```xml
<Entity>
 <Theme>
  <ParentId>0</ParentId>
  <ThemeId>1</ThemeId>
  <Level>1</Level>
  <Name>level1</Name>
 </Theme>
 <Level>
  <Type>1</Type>
  <Description>description_test</Description>
  <LevelId>1</LevelId>
  <Name>level1</Name>
 </Level>
</Entity> <RequestId>16A96B9A-F203-4EC5-8E43-CB92E68F****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>1010010011</ErrorCode> <ErrorMessage>success</ErrorMessage> <Success>true</Success>
```

**错误码**

DataWorks

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1010030001 | Invalid.Meta.TableNotExist | The table does not exist. |
| 400 | 1010010016 | InvalidParameter.Meta.Commo nError | The specified parameter is invalid. |
| 400 | 1010010010 | InvalidParameter.Meta.Illegal | The app guid parameter is invalid. |
| 400 | 1010010017 | InvalidParameter.Meta.IllegalD ate | The date format is invalid. |
| 400 | 1010010011 | InvalidParameter.Meta.IllegalP ageError | The parameter for paging is invalid. |
| 400 | 1010010018 | InvalidParameter.Meta.NotExis t | The object does not exist. |
| 403 | 1010010014 | Forbidden.Meta.NoTenant | The user is not the owner of any tenants. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 500 | 1010010013 | InternalError.Meta.NoCalcEngi ne | An error occurred while retrieving the compute engine based on the MaxCompute project. |
| 500 | 1010010015 | InternalError.Meta.TenantTime Out | Failed to connect to the interface network. |
| 500 | 1010019999 | InternalError.Meta.Unknown | An unknown error occurred while processing your request. |

DataWorks

### 数据开发

#### CreateFile

调用CreateFile，在数据开发中创建一个文件。目前不支持调用该接口创建数据集成节点任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | CreateFile | 系统规定参数。取值： CreateFile |
| FileFolder Path | Strin g | Body | 否 | 业务流程/第一个业务流程/MaxCompute/文件夹1/ 文件夹2 | 文件的路径。 |
| ProjectId | Long | Body | 否 | 10000 | Dataworks工作空间的ID， 您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
| FileName | Strin g | Body | 是 | 文件名 | 文件的名称。 |
| FileDescri ption | Strin g | Body | 否 | 这里是文件描述 | 文件的描述信息。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileType | Integ er | Body | 是 | 10 | 文件的代码类型。 常用的代码类型包括 6（Shell）、10（ODPS SQL）、11（ODPS MR）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS对象检查）、257（EMR Shell）、258（EMR Spark Shell）、 259（EMR Presto）、 260（EMR Impala）、 900（实时同步）、 1089（跨租户节点）、 1091（Hologres开发）、 1093（Hologres SQL）、 1100（赋值节点）、 1221（PyODPS 3）。 您可以调用ListFiles接口中的FileTypes参数，查询文件的代码类型。 |
| Owner | Strin g | Body | 否 | 1000000000001 | 文件责任人的阿里云用户 ID。如果该参数为空，则默认使用调用者的阿里云用户 ID。 |
| Content | Strin g | Body | 否 | SHOW TABLES; | 文件代码内容，不同代码类型（fileType）的文件，代码格式不同。您可以在运维中心找到对应类型的任务， 右键单击查看代码，查看具体的代码格式。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| AutoRerun Times | Integ er | Body | 否 | 3 | 出错自动重跑的次数，最多 10次。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AutoRerun IntervalMil lis | Integ er | Body | 否 | 120000 | 出错自动重跑间隔，单位为毫秒，最大为1800000毫秒 （30分钟）。对应页面上的调度配置>时间属性>出错自动重跑间隔。页面上时间的单位为分钟，请在调用时注意时间的转换。 |
| RerunMod e | Strin g | Body | 否 | ALL ALLOWED _ | 重跑属性，包括 ALL ALLOWED（运行成功 _ 或失败后皆可重跑）、 FAILURE ALLOWED（运 _ 行成功后不可重跑，运行失败后可以重跑）和 ALL DENIED（运行成功或 _ 失败皆不可重跑）。对应页面上的调度配置>时间属性 >重跑属性。 |
| Stop | Boole an | Body | 否 | false | 是否暂停调度，对应页面上的调度配置>时间属性>暂停调度。 |
| ParaValue | Strin g | Body | 否 | a=x b=y | 调度参数，对应页面上的调度配置>基础配置>参数。 |
| StartEffec tDate | Long | Body | 否 | 936923400000 | 自动调度开始生效的毫秒时间戳，对应页面上的调度配置>时间属性>生效时间> 开始时间的毫秒时间戳。 |
| EndEffect Date | Long | Body | 否 | 4155787800000 | 停止自动调度的毫秒时间戳，对应页面上的调度配置 >时间属性>生效时间>结束时间的毫秒时间戳。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CronExpre ss | Strin g | Body | 否 | 00 05 00 * * ? | 自动调度的cron表达式，该参数与 DataWorks 控制台中，数据开发任务的“调度配置>时间属性>cron 表达式”对应。 每天凌晨5点30分定时调度：00 30 05 * * ? 每个小时的第 15 分钟定时调度：00 15 00-23/1 * * ? 每隔十分钟调度一次： 00 00/10 * * * ? 每天 8 点到 17 点，每隔十分钟调度一次：00 00- 59/10 8-17 * * * ? 每月的 1 日 0 点 20 分自动调度：00 20 00 1 * ? 从 1 月 1 日 0 点 10 分开始，每过 3 个月调度一次：00 10 00 1 1-12/3 ? 每周二、周五的 0 点 5 分自动调度：00 05 00 * * 2,5 由于 DataWorks 调度系统的规则，cron 表达式有以下限制： 最短调度间隔时间为5 分钟。 每天最早调度时间为0 点 5 分。 |
| CycleType | Strin g | Body | 否 | DAY | 调度周期的类型，包括 NOT DAY（分钟、小时） _ 和DAY（日、周、月），对应页面上的调度配置>时间属性>调度周期。 |
| Dependen tType | Strin g | Body | 否 | NONE | 依赖上一周期的方式，包括 NONE（取消勾选依赖上一周期）、SELF（本节点）、 CHILD（一层子节点）和 USER DEFINE（自定 _ 义）。 |
| Dependen tNodeIdLis t | Strin g | Body | 否 | abc | 依赖上一周期的节点列表。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InputList | Strin g | Body | 否 | project root,project.file1 _ ,project.001 out _ | 文件依赖的上游文件的输出，对应到调度配置>调度依赖>父节点输出名称一列的值，以英文逗号（,）分隔。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | Dataworks项目的唯一标识符，即数据开发页面顶部切换项目处的英文标识。 该参数与projectId参数二者必须设置其一，以确定本次API 调用操作的Dataworks项目。 |
| Resource GroupIden tifier | Strin g | Body | 否 | group 37582743485243 _ 7 | 文件发布成任务后，任务执行时对应的资源组。对应页面上调度配置>资源属性> 调度资源组的配置。 您可以通过ListResourceGroups 接口获取工作空间可用的资源组列表。 ResourceGroupType传 1，拿到结果后取出 Identifier字段。 |
| Resource GroupId | Long | Body | 否 | 375827434852437 | 已废弃。 文件发布成任务后，任务执行时对应的资源组。对应页面上调度配置> 资源属性>调度资源组的配置。 与 ResourceGroupIdentifier 二者设置其一即可。您可以通过ListResourceGroups 接口获取工作空间可用的资源组列表。 ResourceGroupType传 1，拿到结果后取出Id字段。 |
| Connectio nName | Strin g | Body | 否 | odps first _ | 文件发布成任务后，任务执行时连接的数据源，对应页面顶部的选择数据源下拉列表。 您可以通过 ListResourceGroups接口获取工作空间可用的数据源列表，拿到结果后取出 Name字段。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AutoParsi ng | Boole an | Body | 否 | true | 文件是否开启自动解析功能。取值如下： true：文件会自动解析代码。 false：文件不会自动解析代码。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖”选择“同周期”时的“代码解析”对应。 |
| Scheduler Type | Strin g | Body | 否 | NORMAL | 调度的类型，取值如下： NORMAL：正常调度任务。 MANUAL：手动任务， 不会被日常调度，对应手动业务流程下的节点。 PAUSE：暂停任务。 SKIP：空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| Advanced Settings | Strin g | Body | 否 | {"queue":"default","SPA RK CONF":"--conf _ spark.driver.memory=2 g"} | 任务的高级配置。 该参数与DataWorks控制台中，EMR Spark Streaming和EMR Streaming SQL数据开发任务，编辑页面右侧导航栏的“高级设置“对应。 当前仅EMR Spark Streaming和EMR Streaming SQL任务支持配置该参数，并且参数为 JSON格式。 |
| StartImme diately | Boole an | Body | 否 | true | 发布后是否立即启动。 该参数与DataWorks控制台中，EMR Spark Streaming和EMR Streaming SQL数据开发任务，编辑页面右侧导航栏的“配置>时间属性>启动方式“对应。 |
| StartRight Now | Boole an | Body | 否 | false | 发布后是否立即生成实例。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| Data | Long | 1000001 | 文件创建成功后的ID。 |
| RequestId | String | 0000-ABCD-EFG | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| Success | Boolean | true | 调用是否成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |

**示例**

请求示例 `&FileName=`文件名

```
&FileType=10 &RegionId=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG",
    "HttpStatusCode": 200,
    "Data": 1000001,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>1000001</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

DataWorks

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### CreateFolder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateFolder | 系统规定参数。取值：CreateFolder。 |
| FolderPath | String | 是 | 业务流程/系统数据/MaxCompute/ 导入层 | 文件夹的路径。您可以参考数据开发API调用示例文档中“创建后ide目录结构”小节的目录结构创建。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | String | bdfd68**** | 新建文件夹的唯一标识符。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD-EFG | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 `&FolderPath=`业务流程/系统数据`/MaxCompute/`导入层

```
&ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>bdfd68****</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG",
    "HttpStatusCode": 200,
    "Data": "bdfd68****",
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateUdfFile

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateUdfFile | 系统规定参数。取值：CreateUdfFile。 |
| ClassName | String | 是 | com.alibaba.dat aworks.api.udf.S tringConcat | 函数定义所在的类名，对应创建函数表单的类名一项。 |
| FileFolderPath | String | 是 | 业务流程/第一个业务流程/函数/字符串处理函数 | 函数文件所在的文件夹路径。 |
| FileName | String | 是 | StringConcat | 函数的名称。 |
| FunctionType | String | 是 | STRING | 函数的分类，对应创建函数表单中的函数类型一项，包括MATH（数学运算函数）、AGGREGATE（聚合函数）、 STRING（字符串处理函数）、DATE（日期处理函数）、ANALYTIC（窗口函数） 和OTHER（其他函数）。 |

DataWorks

| ProjectId | Long | 是 | 10000 | Dataworks工作空间的ID，您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Resources | String | 是 | string-concat- 1.0.0.jar,commo ns-lang-2.6.jar | 函数引用的资源名列表，对应创建表中的资源列表。多个资源名称之间使用英文逗号（,）分隔。 |
| UdfDescription | String | 是 | 把几个字符串连接起来生成一个新的字符串 | 函数用途的说明，对应创建函数表单中的描述。 |
| CmdDescription | String | 否 | StringConcat(Str ing... substrs) | 函数调用的命令格式，对应创建函数表单中的命令格式。 |
| ParameterDescri ption | String | 否 | 需要连接的字符串列表 | 函数入参的说明，对应创建函数表单中的参数说明。 |
| ReturnValue | String | 否 | 所有字符串按照输入顺序前后连接生成的新字符串 | 函数的返回值说明，对应创建函数表单中的返回值。 |
| Example | String | 否 | StringConcat('a', 'b', 'c') | 函数调用示例，对应创建函数表单中的示例。 |
| ProjectIdentifier | String | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。 该参数与projectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 100000002 | 文件创建成功后的ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |

DataWorks

| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
|---|---|---|---|
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&ClassName=com.alibaba.dataworks.api.udf.StringConcat
```

`&FileFolderPath=`业务流程/第一个业务流程/函数/字符串处理函数

```
&FileName=StringConcat &FunctionType=STRING &ProjectId=10000 &RegionId=default &Resources=string-concat-1.0.0.jar,commons-lang-2.6.jar
```

`&UdfDescription=`把几个字符串连接起来生成一个新的字符串 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>100000002</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": 100000002,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateBusiness

调用CreateBusiness，创建数据开发（DataStudio）的业务流程。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateBusiness | 系统规定参数。取值：CreateBusiness。 |
| BusinessName | String | 是 | 我的业务流程 | 业务流程名称，同一个项目空间下的业务流程名称必须唯一。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectId | Long | 否 | 10000 | DataWorks工作空间的ID，您可以登录 DataWorks控制台，进入工作空间管理页面查看ID。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间的唯一标识符（即工作空间名称）。您可以登录DataWorks控制台，进入工作空间配置页面查看名称。 该参数与projectId参数二者必须设置其一，以确定本次API调用操作的 DataWorks项目。 |
| Description | String | 否 | 这是一个通过接口创建的业务流程 | 业务流程的描述信息。 |
| Owner | String | 否 | 1000000000001 | 业务流程对应责任人的阿里云账号ID。您可以登录DataWorks控制台，鼠标悬停至顶部菜单栏右侧的用户头像，查看账号 ID。如果该参数为空，则默认使用调用者的阿里云账号ID。 |

DataWorks

| UseType | String | 否 | NORMAL | 业务流程所属的功能模块。取值如下： NORMAL（数据开发） MANUAL BIZ（手动业务流程） _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BusinessId | Long | 100001 | 业务流程ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 `&BusinessName=`我的业务流程

```
&RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <BusinessId>100001</BusinessId> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "BusinessId": 100001,
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateResourceFile

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateResource File | 系统规定参数。取值： CreateResourceFile。 |
| ConnectionNam e | String | 是 | test | 引擎名称。 |
| FileFolderPath | String | 是 | 业务流程/test1/MaxCo mpute/test flod _ er 123 _ | 节点目录。 |

DataWorks

| FileName | String | 是 | test | 节点名称。 |
|---|---|---|---|---|
| FileType | Integer | 是 | 13 | 节点类型。 |
| OssDownloadLin k | String | 是 | http://oss.aliyun. com | OSS下载链接。 |
| ProjectId | Long | 是 | 10001 | 工作空间ID。 |
| IsMaxcompute | Boolean | 否 | true | 资源是否上传到ODPS。 true：上传。 false：不上传。 |
| StorageUri | String | 否 | 无法使用 | 资源的存储路径。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FileId | Long | 10001 | 节点ID。 |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateResourceFile &ConnectionName=test &FileFolderPath=业务流程/test1/MaxCompute/test_floder_123 &FileName=test &FileType=13 &OssDownloadLink=http://oss.aliyun.com &ProjectId=10001
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376****</RequestId> <FileId>10001</FileId>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0bc1ec92159376****",
    "FileId": 10001
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteBusiness

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteBusiness | 系统规定参数。取值：DeleteBusiness。 |
| BusinessId | Long | 是 | 1000001 | 业务流程的ID，您可以调用ListBusiness 接口，根据名称查询对应业务流程的ID。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&BusinessId=1000001 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteFile

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteFile | 系统规定参数。取值：DeleteFile。 |
| FileId | Long | 是 | 10000001 | 文件的ID，您可以使用ListFlies接口查询对应文件的ID。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FileId=10000001 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

DataWorks

| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteFolder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteFolder | 系统规定参数。取值：DeleteFolder。 |
| FolderId | String | 是 | 2eb6f9**** | 文件夹的ID，您可以通过ListFolders查询对应文件夹的ID。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FolderId=2eb6f9**** &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeployFile

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeployFile | 系统规定参数。取值：DeployFile。 |
| FileId | Long | 是 | 10000001 | 文件的ID，您可以通过ListFiles查询对应文件的ID。 该参数与NodeId参数配置一个即可。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |
| Comment | String | 否 | 第一次发布任务 | 本次发布的说明信息。 |
| NodeId | Long | 否 | 2000001 | 待发布文件在调度系统对应的任务ID。该参数与FileId参数配置一个即可。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 30000001 | 发布包的ID，后续需要将该ID作为参数调用 GetDeployment接口，获取本次发布的具体情况。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FileId=10000001 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>30000001</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": 30000001,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### EstablishRelationTableToBusiness

调用EstablishRelationTableToBusiness，导入表至业务流程。相当于在数据开发页面右键单击业务流程，选择导入表的操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | EstablishRelatio nTableToBusine ss | 系统规定参数。取值： EstablishRelationTableToBusiness。 |
| BusinessId | String | 是 | 1000001 | 业务流程的ID，您可以使用ListBusiness 获取对应业务流程的ID。 |
| FolderId | String | 是 | 2eb6f9**** | 文件夹的ID，您可以使用ListBusiness或者ListFolders获取对应文件夹的ID。 |
| ProjectId | Long | 是 | 10000 | Dataworks工作空间的ID，您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableGuid | String | 是 | odps.dw project _ .tb1 | 表的UUID。 |

DataWorks

| ProjectIdentifier | String | 否 | dw | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。 该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD-EFG | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EstablishRelationTableToBusiness &BusinessId=1000001 &FolderId=2eb6f9**** &ProjectId=10000 &RegionId=default &TableGuid=odps.dw_project.tb1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetBusiness

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestId | Strin g | System | 否 | 0000-ABCD-EFG**** | 系统参数，无需配置。 |
| callerUid | Long | System | 否 | 1640133467**** | 系统参数，无需配置。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| IspSignatu re | Strin g | System | 否 | **** | 系统参数，无需配置。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与 ProjectId参数，二者必须设置其一，用来确定本次API 调用操作的DataWorks工作空间。 |
| BusinessI d | Long | Body | 是 | 1000000001 | 业务流程的ID，您可以调用 ListBusiness接口获取。 |
| app ip _ | Strin g | System | 否 | 192.168.XX.XX | 系统参数，无需配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |
| Data | Struct | / | 业务流程列表的详情。 |

| 开发指南·OpenAPI参 | 考 |  | DataWork |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -Owner | String | 34824327**** | 业务流程的责任人。 |
| -Description | String | 我的第一个业务流程 | 业务流程的描述信息。 |
| -ProjectId | String | 10000 | 业务流程所在工作空间的ID。 |
| -BusinessId | Long | 3000001 | 业务流程的ID。 |
| - BusinessName | String | 我的第一个业务流程 | 程业务流程的名称。 |
| -UseType | String | NORMAL | 业务流程所属的功能模块，包括NORMAL（数据开发）和MANUAL BIZ（手动业务流程）。 _ |
| -GlobalParam | String | [{"key":"test key"," _ value":"test v"}] _ | 业务流程参数。 |

**示例**

请求示例

```
&BusinessId=1000000001 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":{
  "Owner":"34824327****",
```

`"Description":"`我的第一个业务流程`",` `"BusinessName":"`我的第一个业务流程`",`

```json
  "UseType":"NORMAL",
  "ProjectId":"10000",
  "BusinessId":3000001,
  "GlobalParam":"[{\"key\":\"test_key\",\"value\":\"test_v\"}]"
 },
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

DataWorks `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
 <Owner>34824327****</Owner>
```

`<Description>`我的第一个业务流程`</Description>` `<BusinessName>`我的第一个业务流程`</BusinessName>`

```xml
 <UseType>NORMAL</UseType>
 <ProjectId>10000</ProjectId>
 <BusinessId>3000001</BusinessId>
 <GlobalParam>
[{&quot;key&quot;:&quot;test_key&quot;,&quot;value&quot;:&quot;test_v&quot;}]</GlobalPa ram> </Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetDeployment

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetDeployment | 系统规定参数。取值： GetDeployment。 |
|---|---|---|---|---|
| DeploymentId | Long | 是 | 3000001 | 发布包的ID。执行SubmitFile和 DeployFile时，都会生成一个对应的发布包ID。 |
| ProjectId | Long | 是 | 10000 | Dataworks工作空间的ID，您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。 该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 发布包的详情。 |
| Deployment | Struct |  | 发布包的详情。 |
| CreateTime | Long | 1593877765000 | 发布包生成的毫秒时间戳。 |
| CreatorId | String | 20030**** | 发布包创建者的阿里云用户ID。 |
| ErrorMessage | String | 成功 | 当发布包执行失败（status为2）后，该字段记录具体的错误信息。 |
| ExecuteTime | Long | 1593877765000 | 发布包开始执行的毫秒时间戳。 |
| FromEnvironm ent | Integer | 0 | 执行本次发布所在的环境，包括0（本地）和 1（开发环境）。 |
| HandlerId | String | 2003**** | 发布包执行者的阿里云用户ID。 |
| Name | String | ods user info d- _ _ _ 2020-07- 04 20030**** _ | 发布包的名称，显示在任务发布>发布包列表页面。 |

DataWorks

| Status | Integer | 1 | 发布包当前的状态，包括0（就绪）、1（成功） 和2（失败）。 |
|---|---|---|---|
| ToEnvironmen t | Integer | 1 | 发布文件信息的目标环境，包括1（开发环境） 和2（生产环境）。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&DeploymentId=3000001 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Deployment>
        <Status>1</Status>
        <HandlerId>2003****</HandlerId>
        <ExecuteTime>1593877765000</ExecuteTime>
        <CreatorId>20030****</CreatorId>
        <ToEnvironment>1</ToEnvironment>
        <CreateTime>1593877765000</CreateTime>
        <FromEnvironment>0</FromEnvironment>
        <ErrorMessage>成功</ErrorMessage>
        <Name>ods_user_info_d-2020-07-04_20030****</Name>
    </Deployment>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "Deployment": {
            "Status": 1,
            "HandlerId": "2003****",
            "ExecuteTime": 1593877765000,
            "CreatorId": "20030****",
            "ToEnvironment": 1,
            "CreateTime": 1593877765000,
            "FromEnvironment": 0,
            "ErrorMessage": "成功",
            "Name": "ods_user_info_d-2020-07-04_20030****"
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetFileVersion

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetFileVersion | 系统规定参数。取值：GetFileVersion。 |
| FileId | Long | 是 | 1000001 | 文件的ID，您可以通过ListFiles查询对应文件的ID。 |
| FileVersion | Integer | 是 | 2 | 需要查询的文件版本。 |
| ProjectId | Long | 是 | 10000 | Dataworks工作空间的ID，您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。 该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 文件的版本详情。 |

DataWorks

| ChangeType | String | UPDATE | 本次文件版本的变更类型，包括CREATE、 UPDATE和DELETE。 |
|---|---|---|---|
| Comment | String | 第二次版本提交 | 本次文件版本的说明。 |
| CommitTime | Long | 1593881265000 | 文件版本生成的毫秒时间戳。 |
| CommitUser | String | 7384234**** | 生成本次文件版本的阿里云用户ID。 |
| FileContent | String | SHOW TABLES; | 生成本次文件版本的文件代码。 |
| FileName | String | ods user info d _ _ _ | 生成本次文件版本的文件名。 |
| FilePropertyCo ntent | String | {"fileName":"ods u _ ser info d","fileTyp _ _ e":10} | 生成本次文件版本的文件基本信息。 |
| FileVersion | Integer | 2 | 文件的版本。 |
| IsCurrentProd | Boolean | true | 本次文件版本是否为当前生产环境的最新版本。 |
| NodeContent | String | {"cycleType":0,"cr onExpress":"00 05 00 * * ?"} | 本次文件版本生成时的调度配置。 |
| NodeId | Long | 3000001 | 文件版本生成时对应的调度任务ID。 |
| Status | String | COMMITTED | 文件版本当前的状态，包括COMMITTING（提交中）、COMMITTED或CHECK OK（已提 _ 交）、PACKAGED（准备发布）、 DEPLOYING（发布中）、DEPLOYED（已发布）和CANCELLED（取消发布）。 |
| UseType | String | NORMAL | 文件所属的功能模块，包括NORMAL（数据开发）、MANUAL（手动任务）、 MANUAL BIZ（手动工作流）、SKIP（数据开 _ 发的空跑调度）、ADHOCQUERY（临时查询） 和COMPONENT（组件管理）。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |

DataWorks

| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
|---|---|---|---|
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FileId=1000001 &FileVersion=2 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Status>COMMITTED</Status>
    <FileContent>SHOW TABLES;</FileContent>
    <CommitUser>7384234****</CommitUser>
```

`<Comment>`第二次版本提交`</Comment>`

```xml
    <ChangeType>UPDATE</ChangeType>
    <UseType>NORMAL</UseType>
    <CommitTime>1593881265000</CommitTime>
    <FileName>ods_user_info_d</FileName>
    <FilePropertyContent>{"fileName":"ods_user_info_d","fileType":10}
</FilePropertyContent>
    <FileVersion>2</FileVersion>
    <NodeId>3000001</NodeId>
    <IsCurrentProd>true</IsCurrentProd>
    <NodeContent>{"cycleType":0,"cronExpress":"00 05 00 * * ?"}</NodeContent>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "Status": "COMMITTED",
        "FileContent": "SHOW TABLES;",
        "CommitUser": "7384234****",
```

`"Comment": "`第二次版本提交`",`

```json
        "ChangeType": "UPDATE",
        "UseType": "NORMAL",
        "CommitTime": 1593881265000,
        "FileName": "ods_user_info_d",
        "FilePropertyContent": "{\"fileName\":\"ods_user_info_d\",\"fileType\":10}",
        "FileVersion": 2,
        "NodeId": 3000001,
        "IsCurrentProd": true,
        "NodeContent": "{\"cycleType\":0,\"cronExpress\":\"00 05 00 * * ?\"}"
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetFile

该接口用于获取文件的详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 DataWorks

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以进入工作空间配置页面获取工作空间ID。 该参数与ProjectIdentifier 参数，二者必须设置其一， 用来确定本次API调用操作的DataWorks工作空间。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间的名称。您可以进入工作空间配置页面获取工作空间名称。 该参数与ProjectId参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| FileId | Long | Body | 否 | 100000001 | 文件的ID。您可以调用 ListFiles接口查询对应文件的ID。 |
| NodeId | Long | Body | 否 | 200000001 | 调度节点的ID。您可以调用 ListFiles接口获取节点ID。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| ErrorMessage | String | "" | 调用失败时，返回的错误信息。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| ErrorCode | String | "" | 调用失败时，返回的错误码。 |
| Success | Boolean | true | 调用是否成功。 |
| Data | Struct | / | 文件的详情。 |

| 开发指南·OpenAPI参 | 考 |  | DataWork |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -File | Struct | / | 文件的基本信息。 |
| -- CommitStatus | Integer | 0 | 文件当前的提交状态，包括0（未提交最新的代码）和1（已提交最新的代码）。 |
| --AutoParsing | Boolean | true | 文件是否开启自动解析功能。取值如下： true：文件会自动解析代码。 false：文件不会自动解析代码。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖”选择“同周期”时的“代码解析”对应。 |
| --Owner | String | 110755000425**** | 任务的责任人的账号ID。 |
| --CreateTime | Long | 1710239005403 | 文件创建的时间戳，单位为毫秒。 |
| --FileType | Integer | 10 | 文件的代码类型。文件类型，不同文件类型其代码不同。 |
| -- CurrentVersio n | Integer | 3 | 文件当前已经提交的最新版本号。 |
| --BizId | Long | 1000001 | 文件所属的业务流程ID。该字段已废弃，请使用 BusinessId字段。 |
| --LastEditUser | String | 62465892**** | 最近一次编辑文件的用户ID。 |
| --FileName | String | ods user info d _ _ _ | 文件名称。 |
| -- ConnectionNa me | String | odps source _ | 执行文件对应的任务时，所使用的数据源名称。 |
| --UseType | String | NORMAL | 文件所属的功能模块。取值： NORMAL：数据开发。 MANUAL：手动任务。 MANUAL BIZ：手动业务流程。 _ SKIP：数据开发的空跑调度。 ADHOCQUERY：临时查询。 COMPONENT：组件管理。 |
| --FileFolderId | String | 2735c2**** | 文件所在文件夹的ID。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ParentId | Long | 122 | 如果当前文件是组合节点文件的内部文件，该字段标识对应组合节点文件的ID。 |
| --CreateUser | String | 11075500042XXXX X | 创建用户的账号ID。 |
| -- IsMaxCompute | Boolean | true | 如果当前文件是MaxCompute资源文件，该字段标识该资源文件是否需要上传至 MaxCompute。 仅当文件是MaxCompute资源文件时才需要配置该参数。 |
| --BusinessId | Long | 1000001 | 文件所属的业务流程ID。 |
| -- FileDescription | String | my test datastudio file | 文件的描述信息。 |
| -- DeletedStatus | String | RECYCLE | 文件的删除状态。取值如下： NORMAL：未删除。 RECYCLE BIN：回收站。 _ DELETED：被删除。 |
| --LastEditTime | Long | 1593879116000 | 最近一次编辑文件的时间戳，单位为毫秒。 |
| --Content | String | SHOW TABLES; | 文件的代码。 |
| --NodeId | Long | 33115 | 提交文件后，在调度系统生成的调度任务 ID。 |
| -- AdvancedSetti ngs | String | {\"priority\":\"1\",\" ENABLE SPARKSQL _ JDBC\":false,\"FLO _ W SKIP SQL ANAL _ _ _ YZE\":false,\"queue \":\"default\"} | 任务的高级配置。 该参数与DataWorks控制台中，EMR数据开发任务，编辑页面右侧导航栏的“高级设置“对应。 当前EMR Shell任务不支持配置高级参数。 |
| --FileId | Long | 1234123 | 文件ID。 |
| - NodeConfigura tion | Struct | / | 文件的调度属性配置。 |
| --InputList | Array | / | 依赖的上游文件输出信息。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---Input | String | dw project root _ _ | 文件依赖的上游文件的输出名称。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖“选择”同周期“时”依赖的上游节点”下的“输出名”对应。 |
| ---ParseType | String | MANUAL | 配置文件依赖的方式，取值如下： MANUAL：手动配置。 AUTO：自动解析。 |
| --OutputList | Array | / | 文件的输出信息。 |
| --- RefTableName | String | ods user info d _ _ _ | 文件的输出值。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 调度依赖“选择”同周期“时的“本节点的输出”下的“输出表名”对应。 |
| ---Output | String | ods user info d _ _ _ | 文件的输出名称。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖“选择”同周期“时的“本节点的输出”下的“输出名”对应。 |
| -- InputParamete rs | Array | / | 节点上下文输入参数信息。 |
| --- ParameterNa me | String | input | 节点上下文输入参数的参数名称。在代码中可以使用${...}方式引用该参数。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输入参数“的”参数名“对应。 |
| ---ValueSource | String | project 001.parent _ node:outputs _ | 节点上下文输入参数的取值来源。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输入参数“的”取值来源“对应。 |
| -- OutputParame ters | Array | / | 节点的上下文输出参数信息。 |
| --- ParameterNa me | String | output | 节点上下文输出参数的参数名称。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输出参数“的”参数名“对应。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---Value | String | 222 | 节点上下文输出参数的表达式。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输出参数“的”取值“对应。 |
| ---Type | String | 1 | 节点上下文输出参数表达式的类型。取值如下： 1：表示常量。 2：表示变量。 3：表示参数节点透传变量。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输出参数“的”类型“对应。 |
| ---Description | String | a connection | 节点上下文输出的参数描述。 |
| --RerunMode | String | ALL ALLOWED _ | 重跑属性。取值如下： AllDenied：失败或成功都不可重跑。 FailureAllowed：只有失败可重跑。 AllAllowed：失败或成功均可重跑。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>重跑属性”配置内容对应。 |
| -- SchedulerType | String | NORMAL | 调度的类型，取值如下： NORMAL：正常调度任务。 MANUAL：手动任务，不会被日常调度。 PAUSE：暂停任务。 SKIP：空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| --Stop | Boolean | false | 是否暂停调度，取值如下： true：暂停调度。 false：不暂停调度。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>调度类型”配置为”暂停调度“时对应。 |
| --ParaValue | String | a=x b=y | 调度参数。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 参数”对应。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- StartEffectDat e | Long | 936923400000 | 开始自动调度的毫秒时间戳。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>生效日期”配置的开始时间的毫秒时间戳对应。 |
| -- EndEffectDate | Long | 1671694850000 | 停止自动调度的时间戳，单位为毫秒。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>生效日期”配置的结束时间的毫秒时间戳对应。 |
| --CycleType | String | DAY | 调度周期的类型，包括NOT DAY（分钟、小 _ 时）和DAY（日、周、月）。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>调度周期”对应。 |
| -- DependentNod eIdList | String | 5,10,15,20 | 当DependentType参数配置为USER DEFINE _ 时，用于设置当前文件具体依赖的节点ID。依赖多个节点时，使用英文逗号（,）分隔。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖”配置为“上一周期”后， 依赖项选择”其他节点“时配置的内容对应。 |
| -- ResourceGrou pId | Long | 1111111111 | 文件发布成任务后，任务执行时对应的资源组。 |
| -- DependentTyp e | String | USER DEFINE _ | 依赖上一周期的方式。取值： SELF：依赖项选择本节点。 CHILD：依赖项选择一级子节点。 USER DEFINE：依赖项选择其他节点。 _ NONE：未选择依赖项，即不会依赖上一周期。 |
| -- AutoRerunTim es | Integer | 3 | 出错自动重跑的次数。 |
| -- AutoRerunInte rvalMillis | Integer | 1200 | 出错自动重跑时间间隔，单位为毫秒。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>出错自动重跑”的”重跑间隔“配置对应。 控制台中“重跑间隔”的时间单位为分钟，请在调用时注意转换时间。 |
| --CronExpress | String | 00 00 00 * * ? | 文件定时调度的cron表达式。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- StartImmediat ely | Boolean | true | 发布后是否立即启动。 该参数与DataWorks控制台中，EMR Spark Streaming和EMR Streaming SQL数据开发任务，编辑页面右侧导航栏的“配置>时间属性>启动方式“对应。 |
| -- ApplySchedule Immediately | String | true | 是否发布后立即生效调度配置。 |
| -- StartRightNow | String | true | 发布后是否立即生成实例。与 ApplyScheduleImmediately参数取值一致。 |
| - ResourceDown loadLink | Struct | / | 资源下载链接，指向可供用户直接下载的文件 URL。 |
| -- downloadLink | String | http://**** | 资源下载地址链接。 |

**示例**

请求示例

```
&RegionId=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":{
  "File":{
   "ParentId":122,
   "Owner":"110755000425****",
   "CreateTime":1710239005403,
   "CurrentVersion":3,
   "FileName":"ods_user_info_d",
   "UseType":"NORMAL",
   "CreateUser":"11075500042XXXXX",
   "IsMaxCompute":true,
   "ConnectionName":"odps_source",
   "LastEditTime":1593879116000,
   "FileDescription":"my test datastudio file",
   "AdvancedSettings":"
{\\\"priority\\\":\\\"1\\\",\\\"ENABLE_SPARKSQL_JDBC\\\":false,\\\"FLOW_SKIP_SQL_ANALYZE\ ":false,\\\"queue\\\":\\\"default\\\"}",
   "FileType":10,
"LastEditUser""62465892****"
```

DataWorks

```json
   "LastEditUser":"62465892****",
   "Content":"SHOW TABLES;",
   "CommitStatus":0,
   "DeletedStatus":"RECYCLE",
   "NodeId":33115,
   "AutoParsing":true,
   "FileId":1234123,
   "FileFolderId":"2735c2****",
   "BizId":1000001,
   "BusinessId":1000001
  },
  "ResourceDownloadLink":{
   "downloadLink":"http://****"
  },
  "NodeConfiguration":{
   "InputList":[
    {
     "Input":"dw_project_root",
     "ParseType":"MANUAL"
    }
```

`],`

```json
   "CycleType":"DAY",
   "ResourceGroupId":1111111111,
   "Stop":false,
   "StartRightNow":"false",
   "DependentType":"USER_DEFINE",
   "SchedulerType":"NORMAL",
   "StartImmediately":true,
   "CronExpress":"00 00 00 * * ?",
   "OutputList":[
    {
     "Output":"ods_user_info_d",
     "RefTableName":"ods_user_info_d"
    }
```

`],`

```json
   "EndEffectDate":1671694850000,
   "OutputParameters":[
    {
     "Type":"1",
     "Description":"a connection",
     "Value":"222",
     "ParameterName":"output"
    }
```

`],`

```json
   "DependentNodeIdList":"5,10,15,20",
   "AutoRerunIntervalMillis":1200,
   "StartEffectDate":936923400000,
   "AutoRerunTimes":3,
   "RerunMode":"ALL_ALLOWED",
   "ParaValue":"a=x b=y",
   "ApplyScheduleImmediately":"true",
   "InputParameters":[
    {
     "ValueSource":"project_001.parent_node:outputs",
"ParameterName":"input"
```

DataWorks

```
     ParameterName:input
    }
```

]

```json
  }
 },
 "ErrorCode":"",
 "ErrorMessage":"",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
  <File>
    <ParentId>122</ParentId>
    <Owner>110755000425****</Owner>
    <CreateTime>1710239005403</CreateTime>
    <CurrentVersion>3</CurrentVersion>
    <FileName>ods_user_info_d</FileName>
    <UseType>NORMAL</UseType>
    <CreateUser>11075500042XXXXX</CreateUser>
    <IsMaxCompute>true</IsMaxCompute>
    <ConnectionName>odps_source</ConnectionName>
    <LastEditTime>1593879116000</LastEditTime>
    <FileDescription>my test datastudio file</FileDescription>
    <AdvancedSettings>
{\&quot;priority\&quot;:\&quot;1\&quot;,\&quot;ENABLE_SPARKSQL_JDBC\&quot;:false,\&quot;F W_SKIP_SQL_ANALYZE\&quot;:false,\&quot;queue\&quot;:\&quot;default\&quot;} </AdvancedSettings>
    <FileType>10</FileType>
    <LastEditUser>62465892****</LastEditUser>
    <Content>SHOW TABLES;</Content>
    <CommitStatus>0</CommitStatus>
    <DeletedStatus>RECYCLE</DeletedStatus>
    <NodeId>33115</NodeId>
    <AutoParsing>true</AutoParsing>
    <FileId>1234123</FileId>
    <FileFolderId>2735c2****</FileFolderId>
    <BizId>1000001</BizId>
    <BusinessId>1000001</BusinessId>
  </File>
  <ResourceDownloadLink>
    <downloadLink>http://****</downloadLink>
  </ResourceDownloadLink>
  <NodeConfiguration>
    <InputList>
      <Input>dw_project_root</Input>
      <ParseType>MANUAL</ParseType>
    </InputList>
    <CycleType>DAY</CycleType>
    <ResourceGroupId>1111111111</ResourceGroupId>
    <Stop>false</Stop>
```

`St`

```
tRihtN
```

fl

```
/St tRihtN
```

DataWorks

```xml
    <StartRightNow>false</StartRightNow>
    <DependentType>USER_DEFINE</DependentType>
    <SchedulerType>NORMAL</SchedulerType>
    <StartImmediately>true</StartImmediately>
    <CronExpress>00 00 00 * * ?</CronExpress>
    <OutputList>
      <Output>ods_user_info_d</Output>
      <RefTableName>ods_user_info_d</RefTableName>
    </OutputList>
    <EndEffectDate>1671694850000</EndEffectDate>
    <OutputParameters>
      <Type>1</Type>
      <Description>a connection</Description>
      <Value>222</Value>
      <ParameterName>output</ParameterName>
    </OutputParameters>
    <DependentNodeIdList>5,10,15,20</DependentNodeIdList>
    <AutoRerunIntervalMillis>1200</AutoRerunIntervalMillis>
    <StartEffectDate>936923400000</StartEffectDate>
    <AutoRerunTimes>3</AutoRerunTimes>
    <RerunMode>ALL_ALLOWED</RerunMode>
    <ParaValue>a=x b=y</ParaValue>
    <ApplyScheduleImmediately>true</ApplyScheduleImmediately>
    <InputParameters>
      <ValueSource>project_001.parent_node:outputs</ValueSource>
      <ParameterName>input</ParameterName>
    </InputParameters>
  </NodeConfiguration>
</Data> <ErrorCode /> <ErrorMessage /> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |

|  | DataWorks |  |  | 开发指南·OpenAPI参考 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |

#### GetFolder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetFolder | 系统规定参数。取值：GetFolder。 |
| FolderId | String | 是 | 273**** | 文件夹的ID。您可以调用ListFolders接口获取文件夹ID。该参数与FolderPath参数配置一个即可。 |
| FolderPath | String | 是 | 业务流程/我的第一个业务流程/MaxCompute/ ods层 | 文件夹的路径。您可以调用ListFolders接口获取文件夹路径。该参数与FolderId参数配置一个即可。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 文件夹的详情。 |
| FolderId | String | 2735**** | 文件夹的ID。 |

DataWorks

| FolderPath | String | 业务流程/我的第一个业务流程/MaxCompute/od s层 | 文件夹的路径。 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FolderId=273****
```

`&FolderPath=`业务流程/我的第一个业务流程`/MaxCompute/ods`层

```
&ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
```

`<FolderPath>`业务流程/我的第一个业务流程`/MaxCompute/ods`层`</FolderPath>`

```xml
    <FolderId>2735****</FolderId>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
```

`"FolderPath": "`业务流程/我的第一个业务流程`/MaxCompute/ods`层`",`

```json
        "FolderId": "2735****"
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetNodeTypeListInfo

调用GetNodeTypeListInfos查询节点类型信息，包括类型Code和类型名称。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNodeTypeLis tInfo | 系统规定参数。取值： GetNodeTypeListInfo。 |
| PageNumber | Integer | 是 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 是 | 10 | 请求的数据页大小，最大值为100。 |

DataWorks

| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |
| Keyword | String | 否 | ODPS SQL | 节点类型的名称，您可以在DataStudio目录树中看到某个节点类型的名称，支持中英文，与locale需要对齐。支持模糊搜索，不填的情况下返回所有节点类型。 |
| Locale | String | 否 | zh-CN | 语言筛选，支持zh-CN和en-US。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NodeTypeInfoL ist | Struct |  | 符合条件的节点类型信息列表。 |
| NodeTypeInfo | Array of NodeTypeInfo |  | 单个节点类型的信息。 |
| NodeType | Integer | 10 | 节点类型Type（数字）。 |
| NodeTypeNam e | String | ODPS SQL | 节点类型的名称。 |
| PageNumber | Integer | 1 | 当前数据页的页码。 |
| PageSize | Integer | 10 | 当前数据页的大小。 |
| TotalCount | Integer | 127 | 满足查询条件的数据总条数。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=GetNodeTypeListInfo &PageNumber=1 &PageSize=10 &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <NodeTypeInfoList>
    <TotalCount>127</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <NodeTypeInfo>
        <NodeTypeName>ODPS SQL</NodeTypeName>
        <NodeType>10</NodeType>
    </NodeTypeInfo>
</NodeTypeInfoList>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","NodeTypeInfoList": {"TotalCount":"127","PageSize":"10","PageNumber":"1","NodeTypeInfo": [{"NodeTypeName":"ODPS SQL","NodeType":"10"}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

#### ListBusiness

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestId | Strin g | System | 否 | EAF3C248-E123-**** | 系统参数，无需配置。 |
| callerUid | Long | System | 否 | 31063db679**** | 系统参数，无需配置。 |
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| IspSignatu re | Strin g | System | 否 | **** | 系统参数，无需配置。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与 ProjectId参数，二者必须设置其一，用来确定本次API 调用操作的DataWorks工作空间。 |
| PageNum ber | Integ er | Body | 是 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integ er | Body | 是 | 10 | 每页显示的数据条数，默认为10条，最大为100条。 |
| Keyword | Strin g | Body | 否 | my | 关键字，用于模糊匹配业务流程的名称。 |

| DataWorks |  |  |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| app ip _ | Strin g | System | 否 | 192.168.XX.XX | 系统参数，无需配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |
| Data | Struct | / | 业务流程列表的详情。 |
| -Business | Array | / | 业务流程的详情。 |
| --Owner | String | 34824327**** | 业务流程的责任人。 |
| --Description | String | 我的第一个业务流程 | 业务流程的描述信息。 |
| --ProjectId | Long | 10000 | 业务流程所在工作空间的ID。 |
| --BusinessId | Long | 3000001 | 业务流程的ID。 |
| -- BusinessName | String | 我的第一个业务流程 | 业务流程的名称。 |
| --UseType | String | NORMAL | 业务流程所属的功能模块，包括NORMAL（数据开发）和MANUAL BIZ（手动业务流程）。 _ |
| --GlobalParam | String | [{"key":"test key"," _ value":"test v"}] _ | 业务流程参数。 |
| -PageNumber | Integer | 1 | 当前数据页的页码。 |
| -PageSize | Integer | 10 | 当前数据页的数据条数。 |

| 开发指南·OpenAPI | 参考 |  | DataWork |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -TotalCount | Integer | 13 | 满足查询条件的数据总条数。 |

**示例**

请求示例

```
&RegionId=default &PageNumber=1 &PageSize=10
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":{
  "TotalCount":13,
  "PageSize":10,
  "PageNumber":1,
  "Business":[
   {
    "Owner":"34824327****",
```

`"Description":"`我的第一个业务流程`",` `"BusinessName":"`我的第一个业务流程`",`

```json
    "UseType":"NORMAL",
    "ProjectId":10000,
    "BusinessId":3000001,
    "GlobalParam":"[{\"key\":\"test_key\",\"value\":\"test_v\"}]"
   }
```

]

```json
 },
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
 <TotalCount>13</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <Business>
  <Owner>34824327****</Owner>
```

`<Description>`我的第一个业务流程`</Description>` `<BusinessName>`我的第一个业务流程`</BusinessName>`

```xml
  <UseType>NORMAL</UseType>
  <ProjectId>10000</ProjectId>
  <BusinessId>3000001</BusinessId>
  <GlobalParam>
[{&quot;key&quot;:&quot;test_key&quot;,&quot;value&quot;:&quot;test_v&quot;}]</GlobalPa ram>
 </Business>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListFiles

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 DataWorks

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestId | Strin g | System | 否 | 7BEEA660-A45A-45E3- 98CC-AFC65E715C23 | 请求ID。入参中无需配置。 |
| callerUid | Long | System | 否 | 123 | 来源ID。无需配置。 |
| FileFolder Path | Strin g | Body | 否 | 业务流程/我的第一个业务流程/MaxCompute/ods层 | 文件所在的文件夹路径。 |
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| Keyword | Strin g | Body | 否 | ods | 文件名称的关键字，用于模糊匹配。 |
| RegionId | Strin g | Host | 否 | default | 区域ID，为固定值 default。 |
| IspSignatu re | Strin g | System | 否 | *** | 无需配置。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与 ProjectId参数，二者必须设置其一，用来确定本次API 调用操作的DataWorks工作空间。 |
| PageNum ber | Integ er | Body | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示的条数，默认为10 条，最大为100条。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| UseType | Strin g | Body | 否 | NORMAL | 文件所属的功能模块，包括 NORMAL（数据开发）、 MANUAL（手动任务）、 MANUAL BIZ（手动工作 _ 流）、SKIP（数据开发空跑调度）、 ADHOCQUERY（临时查询）和COMPONENT（组件管理）。 |
| FileTypes | Strin g | Body | 否 | 10,23 | 文件的代码类型，常用的代码类型包括6（Shell）、 10（ODPS SQL）、 11（ODPS MR）、23（数据集成）、24（ODPS Script）、97（PAI）、 98（组合节点）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS对象检查）、257（EMR Shell）、258（EMR Spark Shell）、 259（EMR Presto）、 260（EMR Impala）、 900（实时同步）、 1002（PAI内部节点）、 1089（跨租户节点）、 1091（Hologres开发）、 1093（Hologres SQL）、 1100（赋值节点）、 1106（遍历节点 （foreach））、 1221（PyODPS 3）。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Owner | Strin g | Body | 否 | 3726346**** | 文件责任人。 |
| NodeId | Long | Body | 否 | 123541234 | 调度节点的ID。 |
| app ip _ | Strin g | System | 否 | *** | 无需配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| RequestId | String | 0000-ABCD-EFG | 请求ID。用于出现错误后排查问题。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |
| Data | Struct | / | 满足条件的文件列表。 |
| -Files | Array | / | 文件详情。 |
| -- CommitStatus | Integer | 1 | 文件当前的提交状态，包括0（未提交最新的代码）和1（已提交最新的代码）。 |
| --AutoParsing | Boolean | true | 文件是否开启自动解析功能。取值如下： true： 文件会自动解析代码。 false：文件不会自动解析代码。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖”选择“同周期”时的“代码解析”对应。 |
| --Owner | String | 3872572**** | 文件责任人的阿里云用户ID。 |
| --CreateTime | Long | 1593950832000 | 文件创建时间的毫秒时间戳。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --FileType | Integer | 10 | 文件的代码类型，常用的代码类型包括 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| -- CurrentVersio n | Integer | 2 | 文件当前已经提交的最新版本号。 |
| --BizId | Long | 300000 | 文件所属的业务流程ID。该字段已废弃，请使用 BusinessId字段。 |
| --LastEditUser | String | 38748246285727 | 最近一次编辑文件的用户阿里云用户ID。 |
| --FileName | String | ods user info d _ _ _ | 文件的名称。 |
| -- ConnectionNa me | String | odps first _ | 文件对应的任务执行时所使用的引擎实例ID。 |
| --UseType | String | NORMAL | 文件所属的功能模块，包括NORMAL（数据开发）、MANUAL（手动任务）、 MANUAL BIZ（手动工作流）、SKIP（数据开 _ 发的空跑调度）、ADHOCQUERY（临时查询） 和COMPONENT（组件管理）。 |
| --FileFolderId | String | 2735c2**** | 文件所在文件夹的ID。 |
| --FileId | Long | 10000001 | 文件的ID。 |
| --ParentId | Long | -1 | 如果当前文件是组合节点文件的内部文件，该字段标识对应组合节点文件的ID。 |

| 开发指南·OpenAPI参 | 考 |  | DataWork |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --CreateUser | String | 382762**** | 文件创建人的阿里云用户ID。 |
| -- IsMaxCompute | Boolean | false | 如果当前文件是MaxCompute资源文件，该字段标识该资源文件是否需要上传至 MaxCompute。仅当文件是MaxCompute资源文件时才需要配置该参数。 |
| --BusinessId | Long | 300000 | 文件所属的业务流程ID。 |
| -- FileDescription | String | my test datastudio file | 文件的描述信息。 |
| --LastEditTime | Long | 1593950832000 | 最近一次编辑文件的毫秒时间戳。 |
| --Content | String | SHOW TABLES; | 文件代码。 |
| --NodeId | Long | 300001 | 提交文件后，在调度系统生成的调度任务的ID。 |
| -PageNumber | Integer | 1 | 请求的数据页数。 |
| -PageSize | Integer | 10 | 每页显示的数据条数。 |
| -TotalCount | Integer | 13 | 满足条件的数据总条数。 |

**示例**

请求示例

```
&RegionId=default
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 13,
        "PageSize": 10,
        "PageNumber": 1,
        "Files": {
            "ParentId": -1,
            "Owner": "3872572****",
            "CurrentVersion": 2,
            "UseType": "NORMAL",
            "FileName": "ods_user_info_d",
            "CreateTime": 1593950832000,
            "CreateUser": "382762****",
            "IsMaxCompute": false,
            "ConnectionName": "odps_first",
            "LastEditTime": 1593950832000,
            "FileDescription": "my test datastudio file",
            "FileType": 10,
            "LastEditUser": 38748246285727,
            "Content": "SHOW TABLES;",
            "CommitStatus": 1,
            "NodeId": 300001,
            "AutoParsing": "",
            "FileId": 10000001,
            "FileFolderId": "2735c2****",
            "BizId": 300000,
            "BusinessId": ""
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>13</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Files>
        <ParentId>-1</ParentId>
        <Owner>3872572****</Owner>
        <CurrentVersion>2</CurrentVersion>
        <UseType>NORMAL</UseType>
        <FileName>ods_user_info_d</FileName>
        <CreateTime>1593950832000</CreateTime>
        <CreateUser>382762****</CreateUser>
        <IsMaxCompute>false</IsMaxCompute>
        <ConnectionName>odps_first</ConnectionName>
        <LastEditTime>1593950832000</LastEditTime>
        <FileDescription>my test datastudio file</FileDescription>
        <FileType>10</FileType>
        <LastEditUser>38748246285727</LastEditUser>
        <Content>SHOW TABLES;</Content>
        <CommitStatus>1</CommitStatus>
        <NodeId>300001</NodeId>
        <AutoParsing/>
        <FileId>10000001</FileId>
        <FileFolderId>2735c2****</FileFolderId>
        <BizId>300000</BizId>
        <BusinessId/>
    </Files>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### ListFileVersions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListFileVersions | 系统规定参数。取值：ListFileVersions。 |
| FileId | Long | 是 | 100000001 | 文件的ID，您可以通过ListFiles查询对应文件的ID。 |
| ProjectId | Long | 是 | 10000 | Dataworks工作空间的ID，您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。 该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |
| PageNumber | Integer | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 文件的版本列表。 |

DataWorks

| FileVersions | Array of FileVersion |  | 文件的版本详情。 |
|---|---|---|---|
| ChangeType | String | UPDATE | 本次文件版本的变更类型，包括CREATE、 UPDATE和DELETE。 |
| Comment | String | 第二次版本提交 | 本次文件版本的说明。 |
| CommitTime | Long | 1593881265000 | 生成文件版本的毫秒时间戳。 |
| CommitUser | String | 73842342**** | 生成本次文件版本的阿里云用户UID。 |
| FileContent | String | SHOW TABLES; | 生成本次文件版本的文件代码。 |
| FileName | String | ods user info d _ _ _ | 生成本次文件版本的文件名。 |
| FilePropertyCo ntent | String | {"fileName":"ods u _ ser info d","fileTyp _ _ e":10} | 生成本次文件版本的文本基本信息。 |
| FileVersion | Integer | 2 | 文件的版本。 |
| IsCurrentProd | Boolean | false | 本次文件版本是否为当前生产环境的最新版本。 |
| NodeContent | String | {"cycleType":0,"cr onExpress":"00 05 00 * * ?"} | 生成本次文件版本的调度配置。 |
| NodeId | Long | 1234 | 生成文件版本时对应的调度任务ID。 |
| Status | String | COMMITTED | 文件版本当前的状态，包括COMMITTING（提交中）、COMMITTED或CHECK OK（已提 _ 交）、PACKAGED（准备发布）、 DEPLOYING（发布中）、DEPLOYED（已发布）和CANCELLED（取消发布）。 |
| UseType | String | NORMAL | 文件所属的功能模块，包括NORMAL（数据开发）、MANUAL（手动任务）、 MANUAL BIZ（手动工作流）、SKIP（数据开 _ 发的空跑调度）、ADHOCQUERY（临时查询） 和COMPONENT（组件管理）。 |
| PageNumber | Integer | 1 | 当前数据页的页码。 |
| PageSize | Integer | 10 | 当前数据页的大小。 |

DataWorks

| TotalCount | Integer | 13 | 满足查询条件的数据总条数。 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FileId=100000001 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>13</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <FileVersions>
        <Status>COMMITTED</Status>
        <FileContent>SHOW TABLES;</FileContent>
```

`<Comment>`第二次版本提交`</Comment>`

```xml
        <CommitUser>73842342****</CommitUser>
        <ChangeType>UPDATE</ChangeType>
        <UseType>NORMAL</UseType>
        <FilePropertyContent>{"fileName":"ods_user_info_d","fileType":10}
</FilePropertyContent>
        <FileName>ods_user_info_d</FileName>
        <CommitTime>1593881265000</CommitTime>
        <FileVersion>2</FileVersion>
        <NodeId>1234</NodeId>
        <IsCurrentProd>false</IsCurrentProd>
        <NodeContent>{"cycleType":0,"cronExpress":"00 05 00 * * ?"}</NodeContent>
    </FileVersions>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 13,
        "PageSize": 10,
        "PageNumber": 1,
        "FileVersions": {
            "Status": "COMMITTED",
            "FileContent": "SHOW TABLES;",
```

`"Comment": "`第二次版本提交`",`

```json
            "CommitUser": "73842342****",
            "ChangeType": "UPDATE",
            "UseType": "NORMAL",
            "FilePropertyContent": "
{\"fileName\":\"ods_user_info_d\",\"fileType\":10}",
            "FileName": "ods_user_info_d",
            "CommitTime": 1593881265000,
            "FileVersion": 2,
            "NodeId": 1234,
            "IsCurrentProd": false,
            "NodeContent": "{\"cycleType\":0,\"cronExpress\":\"00 05 00 * * ?\"}"
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

#### ListFolders

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListFolders | 系统规定参数。取值：ListFolders。 |
| PageNumber | Integer | 是 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integer | 是 | 10 | 每页显示的数据条数，默认为10条，最大为100条。 |
| ParentFolderPat h | String | 是 | 业务流程/我的第一个业务流程/MaxCompute | 父文件夹的路径。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 满足条件的文件夹的列表信息。 |
| Folders | Array of Folders |  | 文件夹的列表。 |
| FolderId | String | 2735c2**** | 文件夹的ID。 |
| FolderPath | String | 业务流程/我的第一个业务流程/MaxCompute/od s层 | 文件夹的路径。 |

DataWorks

| PageNumber | Integer | 1 | 当前数据页的页码。 |
|---|---|---|---|
| PageSize | Integer | 10 | 当前数据页的数据条数。 |
| TotalCount | Integer | 13 | 满足查询条件的数据总条数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&PageNumber=1 &PageSize=10
```

`&ParentFolderPath=`业务流程/我的第一个业务流程`/MaxCompute`

```
&ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>13</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Folders>
```

`<FolderPath>`业务流程/我的第一个业务流程`/MaxCompute/ods`层`</FolderPath>`

```xml
        <FolderId>2735c2****</FolderId>
    </Folders>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 13,
        "PageSize": 10,
        "PageNumber": 1,
        "Folders": {
```

`"FolderPath": "`业务流程/我的第一个业务流程`/MaxCompute/ods`层`",`

```json
            "FolderId": "2735c2****"
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### SubmitFile

调用SubmitFile，提交文件至调度系统的开发环境，生成对应的任务。该API是异步处理，您可以使用

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | SubmitFile | 系统规定参数。取值：SubmitFile。 |
|---|---|---|---|---|
| FileId | Long | 是 | 1000000 | 文件的ID，您可以通过ListFiles查询对应文件的ID。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |
| Comment | String | 否 | 第一次提交任务 | 本次提交的说明信息。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 3000001 | 发布包的ID，后续需要将该ID作为参数调用 GetDeployment接口，获取本次发布的具体情况。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 DataWorks

```
&FileId=1000000 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>3000001</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": 3000001,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

#### UpdateFile

调试或调用该接口时，填写的参数必须和该节点原本的文件配置不同。例如，源节点的某参数值为A，则需要变更为B后再提交。如果仍填写A，会报invalid异常。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Content | Strin g | Body | 否 | SELECT "1"; | 文件代码内容，不同代码类型（fileType）的文件，代码格式不同。您可以在运维中心，右键单击对应类型的任务，选择查看代码，查看具体的代码格式。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| AutoRerun Times | Integ er | Body | 否 | 3 | 文件出错后，自动重跑的次数。 |
| AutoRerun IntervalMil lis | Integ er | Body | 否 | 120000 | 出错自动重跑时间间隔，单位为毫秒。最大为 1800000 毫秒（30 分钟）。 该参数与 DataWorks 控制台中，数据开发任务的“调度配置>时间属性>出错自动重跑”的”重跑间隔“配置对应。 控制台中“重跑间隔”的时间单位为分钟，请在调用时注意转换时间。 |
| RerunMod e | Strin g | Body | 否 | ALL ALLOWED _ | 重跑属性。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>重跑属性”配置内容对应。 枚举值: FAILURE ALLOWED(运 _ 行成功后不可重跑，运行失败后可重跑) ALL DENIED(运行成功 _ 或失败后皆不可重跑) ALL ALLOWED(运行成 _ 功或失败后皆可重跑) |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Stop | Boole an | Body | 否 | false | 是否暂停调度。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>调度类型”配置为”暂停调度“时对应。 枚举值: true(暂停调度) false(不暂停调度) |
| ParaValue | Strin g | Body | 否 | x=a y=b z=c | 调度参数。 该参数与DataWorks控制台中，数据开发任务的“调度配置>参数”对应。 |
| StartEffec tDate | Long | Body | 否 | 936923400000 | 开始自动调度的毫秒时间戳，单位为毫秒。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>生效日期”配置的开始时间的毫秒时间戳对应。 |
| EndEffect Date | Long | Body | 否 | 4155787800000 | 停止自动调度的时间戳，单位为毫秒。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>生效日期”配置的结束时间的毫秒时间戳对应。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CronExpre ss | Strin g | Body | 否 | 00 00-59/5 1-23 * * ? | 自动调度的cron表达式，该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>cron表达式”对应。 示例如下： 每天凌晨5点30分定时调度：00 30 05 * * ? 每个小时的第15分钟定时调度：00 15 00-23/1 * * ? 每隔十分钟调度一次： 00 00/10 * * * ? 每天8点到17点，每隔十分钟调度一次：00 00- 59/10 8-17 * * * ? 每月的1日0点 20 分自动调度：00 20 00 1 * ? 从1月1日0点10分开始， 每过3个月调度一次：00 10 00 1 1-12/3 ? 每周二、周五的0点5分自动调度：00 05 00 * * 2,5 由于DataWorks调度系统的规则，cron表达式有以下限制： 最短调度间隔时间为5分钟。 每天最早调度时间为0点 5分。 |
| CycleType | Strin g | Body | 否 | NOT DAY _ | 调度周期的类型。 该参数与DataWorks控制台中，数据开发任务的“调度配置>时间属性>调度周期”对应。 默认值：DAY 枚举值: DAY(日、周、月) NOT DAY(分钟、小时) _ |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Dependen tType | Strin g | Body | 否 | USER DEFINE _ | 依赖上一周期的方式。 枚举值: NONE(未选择依赖项， 即不会依赖上一周期) USER DEFINE(依赖项选 _ 择其他节点) CHILD(依赖项选择一级子节点) SELF(依赖项选择本节点) |
| Dependen tNodeIdLis t | Strin g | Body | 否 | 5,10,15,20 | 当DependentType参数配置为USER DEFINE时，用 _ 于设置当前文件具体依赖的节点ID。依赖多个节点时， 使用英文逗号（,）分隔。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖”配置为“上一周期”后，依赖项选择”其他节点“时配置的内容对应。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |
| FileId | Long | Body | 是 | 100000001 | 文件的ID。您可以调用 ListFiles接口获取文件ID。 |
| OutputList | Strin g | Body | 否 | dw project.ods user inf _ _ _ o d _ | 文件的输出。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖“选择”同周期“时的”本节点的输出”下的“输出名”对应。 |
| Resource GroupIden tifier | Strin g | Body | 否 | default group _ | 文件发布成任务后，任务执行时对应的资源组。您可以调用ListResourceGroups 获取工作空间可用的资源组列表。 |
| Connectio nName | Strin g | Body | 否 | odps first _ | 文件对应任务执行时，任务使用的数据源标识符。您可以调用ListDataSources获取可用的数据源列表。 |

| DataWorks |  |  |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Owner | Strin g | Body | 否 | 18023848927592 | 文件所有者的用户ID。 |
| AutoParsi ng | Boole an | Body | 否 | true | 文件是否开启自动解析功能。 该参数与DataWorks控制台中，数据开发任务的“调度配置>调度依赖”选择“同周期”时的“代码解析”对应。 枚举值: true(文件会自动解析代码) false(文件不会自动解析代码) |
| Scheduler Type | Strin g | Body | 否 | SKIP | 调度的类型。 枚举值: NORMAL(正常调度任务) SKIP(空跑任务，被日常调度，但启动调度时直接被置为成功) PAUSE(暂停任务) MANUAL(手动任务，不会被日常调度，对应手动业务流程下的节点) |
| Advanced Settings | Strin g | Body | 否 | {"queue":"default","SPA RK CONF":"--conf _ spark.driver.memory=2 g"} | 任务的高级配置。 该参数与DataWorks控制台中，EMR Spark Streaming和EMR Streaming SQL数据开发任务，编辑页面右侧导航栏的“高级设置“对应。 当前仅EMR Spark Streaming和EMR Streaming SQL任务支持配置该参数，并且参数为 JSON格式。 |
| StartImme diately | Boole an | Body | 否 | true | 发布后是否立即启动。 该参数与DataWorks控制台中，EMR Spark Streaming和EMR Streaming SQL数据开发任务，编辑页面右侧导航栏的“配置>时间属性>启动方式“对应。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InputPara meters | Strin g | Body | 否 | [{"ValueSource": "project 001.first node: _ _ bizdate param","Parame _ terName": "bizdate input"}] _ | 节点的上下文输入参数。参数为JSON格式，包含的字段可参考GetFile接口返回值中的InputParameters参数结构。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输入参数“对应。 |
| OutputPar ameters | Strin g | Body | 否 | [{"Type": 1,"Value": "${bizdate}","Paramete rName": "bizdate param"}] _ | 节点的上下文输出参数。参数为JSON格式，包含的字段可参考GetFile接口返回值中的OutputParameters参数结构。 该参数与DataWorks控制台中，数据开发任务的“调度配置>节点上下文>本节点输出参数“对应。 |
| StartRight Now | Boole an | Body | 否 | false | 发布后是否立即生成实例。 枚举值: true(发布后立即生成实例) false(发布后不立即生成实例) |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| RequestId | String | 0000-ABCD-EFGH- IJKLMNOPQ | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 DataWorks

```
&RegionId=default &FileId=100000001
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFGH-IJKLMNOPQ",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFGH-IJKLMNOPQ</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |

#### UpdateBusiness

DataWorks

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestId | Strin g | System | 否 | 7BEEA660-A45A-**** | 系统参数，无需配置。 |
| callerUid | Long | System | 否 | 31063db679**** | 系统参数，无需配置。 |
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| IspSignatu re | Strin g | System | 否 | **** | 系统参数，无需配置。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与 ProjectId参数，二者必须设置其一，用来确定本次API 调用操作的DataWorks工作空间。 |
| BusinessN ame | Strin g | Body | 否 | MyBusiness | 业务流程的名称。您可以调用ListBusiness接口获取。 |
| Descriptio n | Strin g | Body | 否 | modified from my first business | 业务流程的描述信息。 |
| Owner | Strin g | Body | 否 | 348428**** | 业务流程的责任人。您可以调用ListBusiness接口获取。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| BusinessI d | Long | Body | 是 | 300000 | 业务流程的ID，您可以调用 ListBusiness接口获取。 |
| GlobalPar am | Strin g | Body | 否 | [{"key":"test key","value _ ":"test v"}] _ | 业务流程参数。 |
| app ip _ | Strin g | System | 否 | 192.168.XX.XX | 系统参数，无需配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&RegionId=default &BusinessId=300000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateFolder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateFolder | 系统规定参数。取值：UpdateFolder。 |
| FolderId | String | 是 | 2735c2c19d58 | 文件夹的ID，您可以调用ListFolders获取文件夹的ID。 |
| FolderName | String | 是 | MySecondFolder | 文件夹的名称。 |

DataWorks

| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ProjectIdentifier | String | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。该参数与ProjectId 参数，二者必须设置其一，用来确定本次 API调用操作的DataWorks工作空间。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&FolderId=2735c2c19d58 &FolderName=MySecondFolder &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateUdfFile

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateUdfFile | 系统规定参数。取值：UpdateUdfFile。 |

DataWorks

| ClassName | String | 是 | com.alibaba.dat aworks.api.udf.S tringConcat | 函数定义所在的类名，对应创建函数表单的类名。 |
|---|---|---|---|---|
| FileFolderPath | String | 是 | 业务流程/第一个业务流程/函数/字符串处理函数 | 函数文件所在文件夹的路径。 |
| FileId | String | 是 | 10000001 | 文件的ID。 |
| FunctionType | String | 是 | STRING | 函数的分类，对应创建函数表单中的函数类型，包括MATH（数学运算函数）、 AGGREGATE（聚合函数）、 STRING（字符串处理函数）、DATE（日期处理函数）、ANALYTIC（窗口函数） 和OTHER（其他函数）。 |
| ProjectId | Long | 是 | 10000 | Dataworks工作空间的ID，您可以单击页面右上角的小扳手图标，进入工作空间管理页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Resources | String | 是 | string-concat- 1.0.0.jar,commo ns-lang-2.6.jar | 函数引用的资源名列表，使用英文逗号 （,）分隔，对应创建函数表单中的资源列表。 |
| UdfDescription | String | 是 | 把几个字符串连接起来生成一个新的字符串 | 函数用途的说明，对应创建函数表单中的描述。 |
| CmdDescription | String | 否 | StringConcat(Str ing... substrs) | 函数的调用命令格式，对应创建函数表单中的命令格式。 |
| ParameterDescri ption | String | 否 | 需要连接的字符串列表 | 函数入参的说明，对应创建函数表单中的参数说明。 |
| ReturnValue | String | 否 | 所有字符串按照输入顺序前后连接生成的新字符串 | 函数的返回值说明，对应创建函数表单中的返回值。 |
| Example | String | 否 | StringConcat('a', 'b', 'c') | 函数的调用示例，对应创建函数表单中的示例。 |
| ProjectIdentifier | String | 否 | dw project _ | Dataworks工作空间的唯一标识符，即数据开发页面顶部切换工作空间处的英文标识。 该参数与ProjectId参数二者必须设置其一，以确定本次API调用操作的 Dataworks工作空间。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&ClassName=com.alibaba.dataworks.api.udf.StringConcat
```

`&FileFolderPath=`业务流程/第一个业务流程/函数/字符串处理函数

```
&FileId=10000001 &FunctionType=STRING &ProjectId=10000 &RegionId=default &Resources=string-concat-1.0.0.jar,commons-lang-2.6.jar
```

`&UdfDescription=`把几个字符串连接起来生成一个新的字符串 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateResourceFile

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateResource File | 系统规定参数。取值： UpdateResourceFile。 |
| FileId | Long | 是 | 10001 | 节点ID。 |
| FileName | String | 是 | test | 节点名称。 |
| OssDownloadLin k | String | 是 | http://oss.aliyun. com | OSS下载链接。 |
| ProjectId | Long | 是 | 10001 | 工作空间ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0bc1ec92159376** ** | 请求ID |

DataWorks

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateResourceFile &FileId=10001 &FileName=test &OssDownloadLink=http://oss.aliyun.com &ProjectId=10001
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### UpdateIDEEventResult

调用UpdateIDEEventResult接口，在数据开发过程中触发扩展点时，通过将扩展程序对扩展点事件的检查结果返回给数据开发系统。

**请求头**

DataWorks 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| MessageId | Strin g | Body | 否 | 8abcb91f-d266-4073- b907-2ed670378ed1 | DataWorks开放消息的消息ID。当触发扩展点事件后，您可以从接收到的事件消息中获取消息ID。 |
| RegionId | Strin g | Host | 否 | default | 区域ID，为固定值default 。 |
| Extension Code | Strin g | Body | 否 | 8abcb91f-d266-4073- b907-2ed670378ed1 | 扩展程序的唯一标识。您可以登录DataWorks控制台，进入开放平台的 Extensions页签查看标识。 |
| CheckRes ult | Strin g | Body | 否 | OK | 扩展程序对本次扩展点事件的检查状态。取值如下： OK：扩展程序对本次扩展点事件检查通过。 FAIL：扩展程序对本次扩展点事件检查不通过。您需要查看并及时处理报错，以免影响后续程序的正常执行。 WARN：扩展程序对本次扩展点事件检查通过，但存在警告。 |
| CheckRes ultTip | Strin g | Body | 否 | Succeeded | 扩展程序对本次扩展点事件进行检查的摘要信息。该信息会显示在您当前的开发页面上，当本次检查存在警告或者检查不通过时，您可以通过该摘要信息快速定位原因。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 8abcb91f-d266- 4073-b907- 2ed670378ed1 | 请求的唯一标识，用于后续错误排查使用。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=UpdateIDEEventResult
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"8abcb91f-d266-4073-b907-2ed670378ed1"
}
```

`XML` 格式

```xml
<RequestId>8abcb91f-d266-4073-b907-2ed670378ed1</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |

#### CheckFileDeployment

当您在DataWorks数据开发页面创建的文件提交成功后，文件将进入发布检查状态，DataWorks会将文件发布检查事件返回给您，您需要根据事件内容判断该文件是否可以继续进行发布校验。此时，可以通过调用 CheckFileDeployment接口，将待发布文件的检查结果返回至DataWorks。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | CheckFileDeploy ment | 系统规定参数。取值： CheckFileDeployment。 |
|---|---|---|---|---|
| CheckerInstance Id | String | 是 | 66 123455623 _ _ 2 | 文件检查器所属的实例ID。您可以从文件发布检查事件中的CheckerInstanceId获取。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Status | String | 是 | OK | 待发布文件的检查状态，取值如下： OK，表示文件检查通过。 WARN，表示文件检查通过，但是存在警告。 FAIL，表示文件检查未通过。 |
| CheckDetailUrl | String | 否 | https://result.ali yun.com/? checkerInstance Id= | 已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 86d5a5ac-0cc0- 4c5f-a374- a15713b252ab | 请求ID，用于后续问题排查。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CheckFileDeployment &CheckerInstanceId=66_123455623_2 &RegionId=default &Status=OK
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>86d5a5ac-0cc0-4c5f-a374-a15713b252ab</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "86d5a5ac-0cc0-4c5f-a374-a15713b252ab"
}
```

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetIDEEventDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| MessageId | Strin g | Body | 是 | 8abcb91f-d266-4073- b907-2ed67037**** | DataWorks开放消息的消息ID。当触发扩展点事件后，您可以从接收到的事件消息中获取消息ID。 |
| ProjectId | Long | Body | 是 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 16A96B9A-F203- 4EC5-8E43- CB92E68F**** | 请求ID。用于定位日志，排查问题。 |
| EventDetail | Struct |  | 触发扩展点事件时的数据快照。 不同类型的消息事件，数据快照的有效字段存在差异，具体请参考各消息事件的字段说明。 |
| - FileExecutionC ommand | Struct |  | 文件代码执行时的快照，当Message类型为 IDE FILE EXECUTE BEFORE时有效。 _ _ _ |
| --FileId | Long | 1234123 | 文件的ID。 |
| -- DataSourceNa me | String | MaxCompute 001 _ | 表所属计算引擎的唯一标识。 |
| --Content | String | SHOW TABLES; | 生成本次文件版本的代码。 |
| --FileType | Long | 10 | 文件类型。不同文件类型其代码不同，常用的代码及其表示的类型包括6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、 24（ODPS Script）、99（虚拟节点）、 221（PyODPS 2）、225（ODPS Spark）、 227（EMR Hive）、228（EMR Spark）、 229（EMR Spark SQL）、230（EMR MR）、 239（OSS对象检查）、257（EMR Shell）、 258（EMR Spark Shell）、259（EMR Presto）、260（EMR Impala）、900（实时同步）、1089（跨租户节点）、 1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| -DeletedFile | Struct |  | 删除文件时的快照信息，当Message类型为 IDE FILE DELETE BEFORE时有效。 _ _ _ |
| --Owner | String | 7384234**** | 文件责任人。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --FileType | Long | 10 | 文件类型。不同文件类型其代码不同，常用的代码及其表示的类型包括6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、 24（ODPS Script）、99（虚拟节点）、 221（PyODPS 2）、225（ODPS Spark）、 227（EMR Hive）、228（EMR Spark）、 229（EMR Spark SQL）、230（EMR MR）、 239（OSS对象检查）、257（EMR Shell）、 258（EMR Spark Shell）、259（EMR Presto）、260（EMR Impala）、900（实时同步）、1089（跨租户节点）、 1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| -- CurrentVersio n | Long | 1 | 当前文件的最新版本。 |
| --BusinessId | Long | 74328 | 文件所属的业务流程ID。 |
| --FileName | String | hello dataworks.sq _ l | 文件名称。 |
| -- DataSourceNa me | String | MaxCompute 001 _ | 表所属计算引擎的唯一标识。 |
| --UseType | String | NORMAL | 文件所属的功能模块。取值： NORMAL：数据开发。 MANUAL：手动任务。 MANUAL BIZ：手动业务流程。 _ SKIP：数据开发的空跑调度。 ADHOCQUERY：临时查询。 COMPONENT：组件管理。 |
| --FolderId | String | aldurie78l2falure | 文件所属的文件夹ID，您可以调用GetFolder查询文件夹详情。 |
| --ParentFileId | Long | 1234122 | 文件所属的循环节点或遍历节点的ID。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Content | String | SHOW TABLES; | 生成本次文件版本的代码。 |
| --NodeId | Long | 421429 | 调度节点的ID。 |
| --FileId | Long | 1234123 | 文件的ID。 |
| - CommittedFile | Struct |  | 文件提交和发布时的快照。 仅当Message类型为 IDE FILE SUBMIT BEFORE或 _ _ _ IDE FILE DEPLOY BEFORE时有效。 _ _ _ |
| --FileId | Long | 1234123 | 文件的ID。 |
| --Content | String | SHOW TABLES; | 生成本次文件版本的代码。 |
| --Committor | String | 7384234**** | 生成本次文件版本的阿里云用户ID。 |
| --FileType | Long | 10 | 文件类型。不同文件类型其代码不同，常用的代码及其表示的类型包括6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、 24（ODPS Script）、99（虚拟节点）、 221（PyODPS 2）、225（ODPS Spark）、 227（EMR Hive）、228（EMR Spark）、 229（EMR Spark SQL）、230（EMR MR）、 239（OSS对象检查）、257（EMR Shell）、 258（EMR Spark Shell）、259（EMR Presto）、260（EMR Impala）、900（实时同步）、1089（跨租户节点）、 1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| --ChangeType | String | UPDATE | 本次文件版本的变更类型，包括CREATE、 UPDATE和DELETE。 |
| --FileName | String | hello dataworks.sq _ l | 文件名称。 |
| --NodeId | Long | 421429 | 调度节点的ID。 |
| --Comment | String | 新建的一张表。 | 表的备注信息。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --UseType | String | NORMAL | 文件所属的功能模块。取值： NORMAL：数据开发。 MANUAL：手动任务。 MANUAL BIZ：手动业务流程。 _ SKIP：数据开发的空跑调度。 ADHOCQUERY：临时查询。 COMPONENT：组件管理。 |
| -- FilePropertyCo ntent | Struct |  | 文件的更多属性。 |
| --- DataSourceNa me | String | MaxCompute 001 _ | 文件关联的计算引擎唯一标识。 |
| ---ParentFileId | Long | 1234122 | 文件所属的循环节点或遍历节点的ID。 |
| ---BusinessId | Long | 74328 | 文件所属的业务流程ID。 |
| --- CurrentVersio n | Long | 1 | 当前文件的最新版本。 |
| ---Owner | String | 7384234**** | 文件责任人。 |
| ---FolderId | String | aldurie78l2falure | 文件所属的文件夹ID，您可以调用GetFolder查询文件夹详情。 |
| -- NodeConfigura tion | Struct |  | 文件的调度属性配置。 |
| ---InputList | Array |  | 文件依赖的上游文件输出。 |
| ----Input | String | dw project.002 out _ _ | 文件的输出名称。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 调度依赖“选择”同周期“时的“本节点的输出名称”列值对应。 |
| ----ParseType | String | MANUAL | 配置文件依赖的方式，取值： MANUAL：手动配置。 AUTO：自动解析。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---OutputList | Array |  | 文件的输出。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 调度依赖“选择”同周期“时的”本节点的输出名称”对应。 |
| ---- RefTableName | String | ods user info d _ _ _ | 文件的输出值。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 调度依赖“选择”同周期“时的“本节点的输出表”列的值对应。 |
| ----Output | String | dw project.002 out _ _ | 文件的输出名称。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 调度依赖“选择”同周期“时的“本节点的输出名称”列值对应。 |
| ---RerunMode | String | ALL ALLOWED _ | 重跑属性。取值： ALL ALLOWED：运行成功或失败后皆可重 _ 跑。 FAILURE ALLOWED：运行成功后不可重 _ 跑，运行失败后可以重跑。 ALL DENIED：运行成功或失败皆不可重跑。 _ 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 时间属性 > 重跑属性”配置内容对应。 |
| --- SchedulerType | String | NORMAL | 调度的类型，取值如下： NORMAL：正常调度任务。 MANUAL：手动任务，不会被日常调度，对应手动业务流程下的节点。 PAUSE：暂停任务。 SKIP：空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| ---ParaValue | String | a=x b=y | 调度参数。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 参数”对应。您可以参考调度参数配置。 |
| ---CycleType | String | DAY | 调度周期的类型，包括NOT DAY（分钟、小 _ 时）和DAY（日、周、月）。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 时间属性 > 调度周期”对应。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- DependentNod eIdList | String | 5,10,15,20 | 当DependentType参数配置为USER DEFINE _ 时，用于设置当前文件具体依赖的节点ID。依赖多个节点时，使用英文逗号（,）分隔。 该参数与DataWorks控制台中，数据开发任务的“调度配置 > 调度依赖”配置为“上一周期”后， 依赖项选择”其他节点“时配置的内容对应。 |
| --- ResourceGrou pId | Long | 375827434852437 | 文件发布成任务后，任务执行时使用的资源组。 您可以调用ListResourceGroups获取工作空间可用的资源组列表。 |
| --- AutoRerunTim es | Long | 3 | 自动重跑次数。 |
| --- AutoRerunInte rvalMillis | Long | 120000 | 自动重跑间隔，单位：毫秒。 |
| ---CronExpress | String | 00 05 00 * * ? | 调度Cron表达式。 |
| --- DependentTyp e | String | USER DEFINE _ | 依赖上一周期的方式。取值： SELF：依赖项选择本节点。 CHILD：依赖项选择一级子节点。 USER DEFINE：依赖项选择其他节点。 _ NONE：未选择依赖项，即不会依赖上一周期。 |
| -TableModel | Struct |  | 表提交和发布时的快照，当Message类型为 IDE TABLE SUBMIT BEFORE和 _ _ _ IDE TABLE DEPLOY BEFORE时有效。 _ _ _ |
| --Columns | Array |  | 字段列表。 |
| --- ColumnName | String | ID | 字段名称。 |
| ---ColumnType | String | BIGINT | 字段类型。 |
| --- IsPartitionColu mn | Boolean | false | 是否为分区字段，取值： true：是分区字段。 false：非分区字段。 |
| ---Comment | String | ID | 字段备注。 |

|  | DataWorks |  |  | 开发指南·OpenAPI参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Env | String | DEV | 表所属环境。取值： DEV：开发环境。 PROD：生产环境。 |
| --LifeCycle | Long | 7 | 表的生命周期。单位：天。 |
| --TableName | String | tb hello _ | 表名称。 |
| -- DataSourceNa me | String | MaxCompute 001 _ | 表所属计算引擎的唯一标识。 |
| --Comment | String | 新建的一张表。 | 表的备注信息。 |
| --Location | String | hdfs://path/to/objec t | 外部表的Location信息。 |

**示例**

请求示例

```
&MessageId=8abcb91f-d266-4073-b907-2ed67037**** &ProjectId=10000 &RegionId=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"16A96B9A-F203-4EC5-8E43-CB92E68F****",
 "EventDetail":{
  "CommittedFile":{
   "Committor":"7384234****",
```

`"Comment":"`第二次版本提交`",`

```json
   "FileType":10,
   "ChangeType":"UPDATE",
   "NodeConfiguration":{
    "CycleType":"DAY",
    "DependentNodeIdList":"5,10,15,20",
    "ResourceGroupId":375827434852437,
    "AutoRerunIntervalMillis":120000,
    "DependentType":"USER_DEFINE",
    "InputList":{
     "Input":"dw_project_root",
     "ParseType":"MANUAL"
    },
    "AutoRerunTimes":3,
```

DataWorks ,

```json
    "RerunMode":"ALL_ALLOWED",
    "OutputList":{
     "Output":"dw_project.002_out",
     "RefTableName":"ods_user_info_d"
    },
    "SchedulerType":"NORMAL",
    "ParaValue":"a=x b=y",
    "CronExpress":"00 05 00 * * ?"
   },
   "Content":"SHOW TABLES;",
   "FileName":"hello_dataworks.sql",
   "UseType":"NORMAL",
   "NodeId":421429,
   "FileId":1234123,
   "FilePropertyContent":{
    "ParentFileId":1234122,
    "Owner":"7384234****",
    "DataSourceName":"MaxCompute_001",
    "CurrentVersion":1,
    "FolderId":"aldurie78l2falure",
    "BusinessId":74328
   }
  },
  "TableModel":{
   "LifeCycle":7,
   "TableName":"tb_hello",
```

`"Comment":"`新建的一张表。`",`

```json
   "DataSourceName":"MaxCompute_001",
   "Env":"DEV",
   "Columns":{
    "ColumnName":"ID",
    "Comment":"ID",
    "ColumnType":"BIGINT",
    "IsPartitionColumn":false
   },
   "Location":"hdfs://path/to/object"
  },
  "FileExecutionCommand":{
   "DataSourceName":"MaxCompute_001",
   "FileType":10,
   "Content":"SHOW TABLES",
   "FileId":1234123
  },
  "DeletedFile":{
   "ParentFileId":1234122,
   "Owner":"7384234****",
   "FileType":10,
   "DataSourceName":"MaxCompute_001",
   "Content":"SHOW TABLES;",
   "CurrentVersion":1,
   "FileName":"hello_dataworks.sql",
   "UseType":"NORMAL",
   "NodeId":421429,
   "FileId":1234123,
```

DataWorks

```json
   "FolderId":"aldurie78l2falure",
   "BusinessId":74328
  }
 }
}
```

`XML` 格式

```xml
<RequestId>16A96B9A-F203-4EC5-8E43-CB92E68F****</RequestId> <EventDetail>
 <CommittedFile>
  <Committor>7384234****</Committor>
```

`<Comment>`第二次版本提交`</Comment>`

```xml
  <FileType>10</FileType>
  <ChangeType>UPDATE</ChangeType>
  <NodeConfiguration>
   <CycleType>DAY</CycleType>
   <DependentNodeIdList>5,10,15,20</DependentNodeIdList>
   <ResourceGroupId>375827434852437</ResourceGroupId>
   <AutoRerunIntervalMillis>120000</AutoRerunIntervalMillis>
   <DependentType>USER_DEFINE</DependentType>
   <InputList>
    <Input>dw_project_root</Input>
    <ParseType>MANUAL</ParseType>
   </InputList>
   <AutoRerunTimes>3</AutoRerunTimes>
   <RerunMode>ALL_ALLOWED</RerunMode>
   <OutputList>
    <Output>dw_project.002_out</Output>
    <RefTableName>ods_user_info_d</RefTableName>
   </OutputList>
   <SchedulerType>NORMAL</SchedulerType>
   <ParaValue>a=x b=y</ParaValue>
   <CronExpress>00 05 00 * * ?</CronExpress>
  </NodeConfiguration>
  <Content>SHOW TABLES;</Content>
  <FileName>hello_dataworks.sql</FileName>
  <UseType>NORMAL</UseType>
  <NodeId>421429</NodeId>
  <FileId>1234123</FileId>
  <FilePropertyContent>
   <ParentFileId>1234122</ParentFileId>
   <Owner>7384234****</Owner>
   <DataSourceName>MaxCompute_001</DataSourceName>
   <CurrentVersion>1</CurrentVersion>
   <FolderId>aldurie78l2falure</FolderId>
   <BusinessId>74328</BusinessId>
  </FilePropertyContent>
 </CommittedFile>
 <TableModel>
  <LifeCycle>7</LifeCycle>
  <TableName>tb_hello</TableName>
```

`<Comment>`新建的一张表。`</Comment>`

```xml
  <DataSourceName>MaxCompute001</DataSourceName>
```

DataWorks

```xml
ataSouceae aCopute_00 /ataSouceae
  <Env>DEV</Env>
  <Columns>
   <ColumnName>ID</ColumnName>
   <Comment>ID</Comment>
   <ColumnType>BIGINT</ColumnType>
   <IsPartitionColumn>false</IsPartitionColumn>
  </Columns>
  <Location>hdfs://path/to/object</Location>
 </TableModel>
 <FileExecutionCommand>
  <DataSourceName>MaxCompute_001</DataSourceName>
  <FileType>10</FileType>
  <Content>SHOW TABLES</Content>
  <FileId>1234123</FileId>
 </FileExecutionCommand>
 <DeletedFile>
  <ParentFileId>1234122</ParentFileId>
  <Owner>7384234****</Owner>
  <FileType>10</FileType>
  <DataSourceName>MaxCompute_001</DataSourceName>
  <Content>SHOW TABLES;</Content>
  <CurrentVersion>1</CurrentVersion>
  <FileName>hello_dataworks.sql</FileName>
  <UseType>NORMAL</UseType>
  <NodeId>421429</NodeId>
  <FileId>1234123</FileId>
  <FolderId>aldurie78l2falure</FolderId>
  <BusinessId>74328</BusinessId>
 </DeletedFile>
</EventDetail>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |

#### ListDeployments

**使用说明**

该功能与DataWorks控制台任务发布页面的发布包列表功能对应。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Region | Strin g | Host | 否 | default | 服务所在的地域，为固定值default 。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间的名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。 该参数与ProjectId参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 该参数与ProjectIdentifier 参数，二者必须设置其一， 用来确定本次API调用操作的DataWorks工作空间。 |
| Creator | Strin g | Body | 否 | 20030**** | 发布包创建者的阿里云用户 ID。 |
| EndCreate Time | Long | Body | 否 | 1593877765000 | 生成发布包的时间，用UNIX 时间戳表示，单位：毫秒。 |
| Executor | Strin g | Body | 否 | 2003**** | 发布包执行者的阿里云用户 ID。 |

|  | 开发指南·Open | API参考 |  |  |  | DataWork | s |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| EndExecut eTime | Long | Body | 否 | 1593877765000 | 发布包开始执行的时间，用 UNIX时间戳表示，单位：毫秒。 |
| Status | Integ er | Body | 否 | 1 | 发布包当前的状态。取值： 0：发布包已准备就绪。 1：发布包发布成功。 2：发布包发布失败。 6：发布包被驳回。 |
| Keyword | Strin g | Body | 否 | hello | 发布包名称的关键字。 DataWorks支持模糊匹配，即输入关键字，即可查询包含该关键字的发布包。 |
| PageNum ber | Integ er | Body | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Integ er | Body | 否 | 20 | 每页显示的条数，默认为10 条，最大为100条。 |
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 16A96B9A-F203- 4EC5-8E43- CB92E68F**** | 请求ID。用于定位日志，排查问题。 |
| Data | Struct |  |  |
| -Deployments | Array |  |  |
| --Status | Integer | 1 | 发布包当前的状态。取值： 0：发布包已准备就绪。 1：发布包发布成功。 2：发布包发布失败。 6：发布包被驳回。 |
| -- ErrorMessage | String | OK | 当发布包执行失败时，用于记录错误信息。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --CreateTime | Long | 1593877765000 | 发布包创建的时间戳，用UNIX时间戳表示，单位：毫秒。 |
| --Executor | String | 2003**** | 发布包执行者的阿里云用户ID。 |
| --Creator | String | 2003**** | 发布包创建者的阿里云用户ID。 |
| --ExecuteTime | Long | 1593877765000 | 执行发布包的时间，用UNIX时间戳表示，单位： 毫秒。 |
| --Name | String | auto created _ | 发布包的名称。 |
| --Id | Long | 11111 | 发布包的ID，您可以根据此ID调用 GetDeployment接口，获取发布包详情。 |
| -PageNumber | Long | 1 | 数据页数。 |
| -PageSize | Long | 10 | 每页显示的数据条数。 |
| -TotalCount | Long | 13 | 数据总条数。 |

**示例**

请求示例

```
&RegionId=default
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"16A96B9A-F203-4EC5-8E43-CB92E68F****",
 "Data":{
  "Deployments":{
   "Status":1,
   "Executor":"2003****",
   "ExecuteTime":1593877765000,
   "CreateTime":1593877765000,
   "Creator":"2003****",
   "Id":11111,
   "ErrorMessage":"OK",
   "Name":"auto_created"
  },
  "TotalCount":13,
  "PageSize":10,
  "PageNumber":1
 }
}
```

`XML` 格式

```xml
<RequestId>16A96B9A-F203-4EC5-8E43-CB92E68F****</RequestId> <Data>
 <Deployments>
  <Status>1</Status>
  <Executor>2003****</Executor>
  <ExecuteTime>1593877765000</ExecuteTime>
  <CreateTime>1593877765000</CreateTime>
  <Creator>2003****</Creator>
  <Id>11111</Id>
  <ErrorMessage>OK</ErrorMessage>
  <Name>auto_created</Name>
 </Deployments>
 <TotalCount>13</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
</Data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
|---|---|---|---|
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |

#### OfflineNode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NodeId | Long | Body | 是 | 1234 | 节点ID。 |
| ProjectId | Long | Body | 是 | 10001 | 工作空间的ID。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。 |
| Success | String | true | 调用是否成功。 |

**示例**

请求示例

```
&NodeId=1234 &ProjectId=10001 &RegionId=default
```

&公共请求参数正常返回示例 DataWorks `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "Success":"true"
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1120010003 | Invalid.DI.Parameter | The parameter is invalid. |
| 403 | 1120010001 | Forbidden.DI.NoPrivilege | No access. |
| 500 | 1120010002 | InternalError.DI.Parameter | A DI internal error occurred. |

#### addNode

该API用于在DataWorks中创建新的节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NodeNam e | Strin g | Query | 是 | liux test n**** _ _ | 节点名称。 |
| ParentId | Strin g | Query | 是 | 121 | 父类ID。 |
| BusinessK ey | Strin g | Query | 是 | 1111111111 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Boolean | true | 返回结果数据。 |
| DynamicError Code | Boolean | Invalid.Tenant.Con nectionNotExists | 错误码。取值同ErrorCode。 |
| DynamicError Message | Boolean | The connection does not exist. | 错误信息。取值同ErrorMessage。 |

**示例**

请求示例

```
&NodeName=liux_test_n**** &ParentId=121 &BusinessKey=1111111111
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "DynamicErrorMessage":false,
 "HttpStatusCode":400,
 "Data":true,
 "DynamicErrorCode":false,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <DynamicErrorMessage>false</DynamicErrorMessage> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <DynamicErrorCode>false</DynamicErrorCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### DeleteNode

该接口用于删除数据开发节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NodeId | Strin g | Query | 是 | 1234 | 节点ID。 |
| BusinessK ey | Strin g | Query | 是 | 11111111111 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Boolean | true | 返回结果数据。 |
| DynamicError Code | Boolean | Invalid.Tenant.Con nectionNotExists | 错误码。取值同ErrorCode。 |
| DynamicError Message | Boolean | The connection does not exist. | 错误信息。取值同ErrorMessage。 |

**示例**

请求示例

```
&NodeId=1234 &BusinessKey=11111111111
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "DynamicErrorMessage":false,
 "HttpStatusCode":400,
 "Data":true,
 "DynamicErrorCode":false,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <DynamicErrorMessage>false</DynamicErrorMessage> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <DynamicErrorCode>false</DynamicErrorCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

DataWorks

#### SelectNodeList

该接口用于查询指定租户下的节点列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | String | { "nodeName": "业务", "sensitiveNotNull": false, "nodeParent": "第一级", "childrenList": [ { "nodeName": "账户信息", "sensitiveNotNull": false, "nodeParent": "第一级/第二级", "childrenList": [ { "nodeName": "特有账户信息", "sensitiveNotNull": true, "childrenList": null, "nodeId": "c9d705c4-217e- 40d4-bb93- 5c2ce6a42e86", "nodeOldId": "c9d705c4-217e- 40d4-bb93- 5c2ce6a42e86", "parentId": "e874ed8b-06f3- 42d0-a876- f394635bb83a" } ], "nodeId": "e874ed8b-06f3- 42d0-a876- f394635bb83a", "nodeOldId": "e874ed8b-06f3- 42d0-a876- f394635bb83a", "parentId": "fbd03611-af79- 4d61-8504- 55e3fe3f2381" } ], "nodeId": "fbd03611-af79- 4d61-8504- 55e3fe3f2381", "nodeOldId": "fbd03611-af79- 4d61-8504- 55e3fe3f2381", "parentId": "39be58b1-58b6- 4965-8e3e- 7d1360de764f" } | 返回结果数据。 |

**示例**

请求示例

```
&TenantId=10241024
```

&公共请求参数 DataWorks 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":"{      \"nodeName\": \"业务\",      \"sensitiveNotNull\": false,
\"nodeParent\": \"第一级\", \"childrenList\": [ { \"nodeName\": \"账户信息\", \"sensitiveNotNull\": false, \"nodeParent\": \"第一级/第二级\", \"childrenList\": [ { \"nodeName\": \"特有账户信息\", \"sensitiveNotNull\": true, \"childrenList\": null, \"nodeId\": \"c9d705c4-217e-40d4-bb93-5c2ce6a42e86\", \"nodeOldId\": \"c9d705c4-217e-40d4-bb93-5c2ce6a42e86\", \"parentId\": \"e874ed8b-06f3-42d 0-a876-f394635bb83a\" } ], \"nodeId\": \"e874ed8b-06f3-42d0 -a876-f394635bb83a\", \"nodeOldId\": \"e874ed8b-06f3-42d0-a876-f394635bb83a\", \"parentId\": \"fbd03611-af79-4d61-8504-55e3fe3f2381\" } ], \"nodeId\": \"fbd03611-af79-4d61-8504-55e3fe3f2381\", \"nodeOldId\": \"fbd03611-af79-4d61-8504 -55e3fe3f2381\", \"parentId\": \"39be58b1-58b6-4965-8e3e-7d1360de764f\" }",
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>{
      &quot;nodeName&quot;: &quot;业务&quot;,
      &quot;sensitiveNotNull&quot;: false,
      &quot;nodeParent&quot;: &quot;第一级&quot;,
      &quot;childrenList&quot;: [
        {
          &quot;nodeName&quot;: &quot;账户信息&quot;,
          &quot;sensitiveNotNull&quot;: false,
          &quot;nodeParent&quot;: &quot;第一级/第二级&quot;,
          &quot;childrenList&quot;: [
            {
              &quot;nodeName&quot;: &quot;特有账户信息&quot;,
              &quot;sensitiveNotNull&quot;: true,
              &quot;childrenList&quot;: null,
              &quot;nodeId&quot;: &quot;c9d705c4-217e-40d4-bb93-5c2ce6a42e86&quot;,
              &quot;nodeOldId&quot;: &quot;c9d705c4-217e-40d4-bb93-5c2ce6a42e86&quot;,
              &quot;parentId&quot;: &quot;e874ed8b-06f3-42d0-a876-f394635bb83a&quot;
            }
```

`],`

```
          &quot;nodeId&quot;: &quot;e874ed8b-06f3-42d0-a876-f394635bb83a&quot;,
          &quot;nodeOldId&quot;: &quot;e874ed8b-06f3-42d0-a876-f394635bb83a&quot;,
          &quot;parentId&quot;: &quot;fbd03611-af79-4d61-8504-55e3fe3f2381&quot;
        }
```

`],`

```xml
      &quot;nodeId&quot;: &quot;fbd03611-af79-4d61-8504-55e3fe3f2381&quot;,
      &quot;nodeOldId&quot;: &quot;fbd03611-af79-4d61-8504-55e3fe3f2381&quot;,
      &quot;parentId&quot;: &quot;39be58b1-58b6-4965-8e3e-7d1360de764f&quot;
    }</Data>
 <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode>
 <ErrorMessage>The connection does not exist.</ErrorMessage>
 <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### UpdateNode

该接口用于更新数据开发节点信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NodeNam e | Strin g | Query | 是 | liux test n**** _ _ | 节点名称。 |
| NodeId | Strin g | Query | 是 | 1234 | 节点ID。 |
| BusinessK ey | Strin g | Query | 是 | 111111111111111111 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| Success | Boolean | true | 是否请求成功。 |

| 开发指南·OpenAPI | 参考 |  | DataWork |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Boolean | true | 返回结果数据。 |

**示例**

请求示例

```
&NodeName=liux_test_n**** &NodeId=1234 &BusinessKey=111111111111111111
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":true,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |

DataWorks

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

### 数据集成

#### CreateDISyncTask

DataWorks目前仅支持直接使用CreateDISyncTask接口创建数据集成离线同步任务，而数据集成实时同步任务和解决方案同步任务则需要先调用GenerateDISyncTaskConfigForCreating和 QueryDISyncTaskConfigProcessResult接口，获取异步生成创建数据集成同步任务时需要的参数，再将该参数作为CreateDISyncTask接口的入参，使用CreateDISyncTask接口创建相应的实时同步任务和解决方案同步任务。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDISyncTa sk | 系统规定参数。取值： CreateDISyncTask。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| TaskContent | String | 是 | {"type":"job","ve rsion":"2.0","ste ps": [{"stepType":"m ysql","paramete r": {"envType":1,"d atasource":"mys ql pub","column _ ": ["id","name","cr eate time","age _ ","score","t 01"], _ "connection": [{"datasource":" mysql pub","tab _ le": ["u pk"]}],"wher _ e":"","splitPk":"id ","encoding":"UT F- 8"},"name":"Re ader","category" :"reader"}, {"stepType":"od ps","parameter": {"partition":"pt= ${bizdate}","tru ncate":true,"dat asource":"odps f _ irst","envType": 1,"column": ["id","name","cr eate time","age _ ","score","t 01"], _ "emptyAsNull":f alse,"tableCom ment":"null","ta ble":"u pk"},"na _ me":"Writer","ca tegory":"writer" }],"setting": {"executeMode" :null,"errorLimit" : {"record":""},"s peed": {"concurrent":2, "throttle":false} },"order": {"hops": [{"from":"Reade r","to":"Writer"}] }} | 使用脚本模式配置数据集成离线同步任务的配置内容。 当前仅支持通过CreateDISyncTask接口创建数据集成离线同步任务。 |
|---|---|---|---|---|
| TaskName | String | 是 | new di task _ _ | 创建的数据集成同步任务的名称。 |

DataWorks

| TaskParam | String | 是 | {"FileFolderPath ":"业务流程/XXX/ 数据集成","ResourceGr oup":"S res gro _ _ up XXX XXXX"} _ _ | 数据集成同步任务的配置参数。目前支持配置如下参数： FileFolderPath：表示数据集成同步任务的存放路径。 ResourceGroup：表示数据集成同步任务所使用的数据集成资源组标识 （Identifier）。 |
|---|---|---|---|---|
| TaskType | String | 是 | DI OFFLINE _ | 创建的数据集成同步任务的任务类型。 目前仅支持使用CreateDISyncTask接口创建数据集成离线同步任务 （DI OFFLINE）。 _ |
| ClientToken | String | 否 | 0000-ABCD- EFG**** | 幂等参数，该参数可为空。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回数据。 |
| FileId | Long | 1000001 | 成功创建的数据集成同步任务的任务ID。 |
| Message | String | 不合法的目录路径： 业务流程/重兴xxxx/ 数据集成 | 创建数据集成同步任务失败的原因描述。 |
| Status | String | success | 创建数据集成同步任务的结果状态。取值如下： success：表示创建任务成功。 fail：表示创建任务失败。 |
| RequestId | String | 0bc141151593763 5973**** | 请求ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 DataWorks

```json
&ProjectId=10000 &RegionId=default &TaskContent={"type":"job","version":"2.0","steps":[{"stepType":"mysql","parameter":{"e nvType":1,"datasource":"mysql_pub","column": ["id","name","create_time","age","score","t_01"],"connection": [{"datasource":"mysql_pub","table": ["u_pk"]}],"where":"","splitPk":"id","encoding":"UTF- 8"},"name":"Reader","category":"reader"},{"stepType":"odps","parameter": {"partition":"pt=${bizdate}","truncate":true,"datasource":"odps_first","envType":1,"colum
```

:

```json
["id","name","create_time","age","score","t_01"],"emptyAsNull":false,"tableComment":"null "table":"u_pk"},"name":"Writer","category":"writer"}],"setting": {"executeMode":null,"errorLimit":{"record":""},"speed": {"concurrent":2,"throttle":false}},"order":{"hops":[{"from":"Reader","to":"Writer"}]}} &TaskName=new_di_task
```

`&TaskParam={"FileFolderPath":"`业务流程`/XXX/`数据集

```
成","ResourceGroup":"S_res_group_XXX_XXXX"} &TaskType=DI_OFFLINE
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937635973****</RequestId> <Data>
    <Status>success</Status>
```

`<Message>`不合法的目录路径：业务流程/重兴`xxxx/`数据集成`</Message>`

```xml
    <FileId>1000001</FileId>
</Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1411515937635973****",
    "Data": {
        "Status": "success",
```

`"Message": "`不合法的目录路径：业务流程/重兴`xxxx/`数据集成`",`

```json
        "FileId": 1000001
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.DI.Paramete r | The parameter is invalid. | 参数错误 |

DataWorks

| 400 | Invalid.DI.Paramete r.File.Existed | The file name already exists. | 参数不合法，文件名已存在 |
|---|---|---|---|
| 403 | Forbidden.DI.NoPri vilege | No access. | 没有权限访问 |
| 500 | InternalError.DI.Par ameter | A DI internal error occurred. | 数据集成内部业务错误 |

#### GetDataSourceMeta

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataSource Meta | 系统规定参数。取值： GetDataSourceMeta。 |
| DatasourceNam e | String | 是 | mysql name _ | 目标数据源的名称。 |
| PageNumber | Long | 是 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Long | 是 | 10 | 每页显示的数据条数。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| EnvType | String | 否 | 1 | 目标数据源所属的环境。取值如下： 0：开发环境。 1：生产环境。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 获取目标数据源Meta信息的返回的结果。 |
| Message | String | read datasource time out | 获取目标数据源Meta信息失败后的原因描述。如果获取目标数据源的Meta信息成功，则该参数的返回值为空。 |

DataWorks

|  |  |  |  |  |  | 返回的目标数据源的Meta信息。返回的信息为 JSON格式。 {"dbTables": |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | {"dbTables": |  |
|  |  |  |  |  |  | [{"dbName":"testdb","schema": |  |  |
|  |  |  |  | {"dbTables": |  |  |  |  |
|  |  |  |  |  |  | [{"tableInfos": |  |  |
|  |  |  |  | [{"dbName":"testd |  | [{"dbName":"testdb","enable":true,"ta |  |  |
|  |  |  |  | b","schema": |  |  |  |  |
|  |  |  |  | [{"tableInfos": |  | ble":"table1","tableName":"table1"}]} |  |  |
|  |  |  |  | [{"dbName":"testd |  | ,{"tableInfos": |  |  |
|  |  |  |  | b","enable":true,"t |  | [{"dbName":"testdb","enable":true,"ta |  |  |
|  | Meta |  | String | able":"table1","tabl |  | ble":"table2","tableName":"table2"}]} |  |  |
|  |  |  |  | eName":"table1"}] |  |  |  |  |
|  |  |  |  | },{"tableInfos": |  | ]}]} |  |  |
|  |  |  |  | [{"dbName":"testd b","enable":true,"t able":"table2","tabl eName":"table2"}] }]}]} |  |  |  |  |
|  | Status |  | String | success |  | 获取目标数据源Meta信息的结果状态。取值如下： success：表示获取目标数据源的Meta信息成功。 fail：表示获取目标数据源的Meta信息失败。 您可以查看Message参数定位失败原因。 |  |  |
|  | RequestId |  | String | 0000-ABCD-EFG |  | 本次调用的唯一ID。用于出现错误后定位日志， 排查问题。 |  |  |
|  | Success |  | Boolean | true |  | 请求是否成功。取值如下： true：成功。 false：失败。 |  |  |

**示例**

请求示例

```
&DatasourceName=mysql_name &PageNumber=1 &PageSize=10 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```json
<RequestId>0000-ABCD-EFG</RequestId> <Data>
    <Status>success</Status>
    <Meta>{"dbTables":[{"dbName":"testdb","schema":[{"tableInfos":
[{"dbName":"testdb","enable":true,"table":"table1","tableName":"table1"}]}, {"tableInfos": [{"dbName":"testdb","enable":true,"table":"table2","tableName":"table2"}]}]}]}</Meta>
    <Message>read datasource time out</Message>
</Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG",
    "Data": {
        "Status": "success",
        "Meta": "{\"dbTables\":[{\"dbName\":\"testdb\",\"schema\":[{\"tableInfos\":[{\"
dbName\":\"testdb\",\"enable\":true,\"table\":\"table1\",\"tableName\":\"table1\"}]},{\ "tableInfos\": [{\"dbName\":\"testdb\",\"enable\":true,\"table\":\"table2\",\"tableName\":\"table2\"}]}] }",
        "Message": "read datasource time out"
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.DI.NoPri vilege | No access. | 没有权限访问 |
| 500 | InternalError.DI.Par ameter | A DI internal error occurred. | 数据集成内部业务错误 |
| 400 | Invalid.DI.Paramete r | The parameter is invalid. | 参数错误 |

#### ListDIProjectConfig

调用ListDIProjectConfig查看当前工作空间中数据集成同步解决方案任务默认的全局配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDIProjectCon fig | 系统规定参数。取值： ListDIProjectConfig。 |

DataWorks

| DestinationType | String | 是 | elasticsearch | 数据集成同步解决方案任务的目的端数据源。该参数不能为空。 调用ListDIProjectConfig查看同步解决方案的全局配置目前仅支持配置目的端数据源为analyticdb for mysql、odps、 _ _ elasticsearch、holo、mysql及 polardb。 |
|---|---|---|---|---|
| ProjectId | Long | 是 | 1000 | DataWorks工作空间的ID。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| SourceType | String | 是 | mysql | 数据集成同步解决方案任务的源端数据源。 调用ListDIProjectConfig查看同步解决方案的全局配置目前仅支持配置源端数据源为oracle、mysql、polardb、 datahub、drds及 analyticdb for mysql。 _ _ 如果不配置源端数据源，则默认全局配置对所有的源端数据源均生效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 查看目标工作空间中数据集成同步解决方案任务默认全局配置的返回结果。 |

DataWorks

| Config | String | {"RENAMECOLUMN ":"WARNING","DRO PTABLE":"WARNIN G","CREATETABLE" :"WARNING","MODI FYCOLUMN":"WAR NING","TRUNCATET ABLE":"WARNING", "DROPCOLUMN":" WARNING","ADDC OLUMN":"WARNING ","RENAMETABLE": "WARNING"} | 数据集成同步解决方案任务默认的全局配置内容 （即对不同DDL消息类型配置的默认处理策略）。示例如下： {"RENAMECOLUMN":"WARNING","DROPTA BLE":"WARNING","CREATETABLE":"WARNI NG","MODIFYCOLUMN":"WARNING","TRUN CATETABLE":"WARNING","DROPCOLUMN": "WARNING","ADDCOLUMN":"WARNING","R ENAMETABLE":"WARNING"} DDL消息类型如下： RENAMECOLUMN：重命名列。 DROPTABLE：删除表。 CREATETABLE：新建表。 MODIFYCOLUMN：修改列类型。 TRUNCATETABLE：清空表。 DROPCOLUMN：删除列。 ADDCOLUMN：新增列。 RENAMETABLE：重命名表。 DataWorks收到对应类型的DDL消息时，处理策略如下： WARNING：直接丢弃该消息，同时会在实时同步日志中记录告警信息，指明该消息因执行出错被丢弃。 IGNORE：直接丢弃该消息，不再向目的端数据源发送。 CRITICAL：实时同步任务直接显示出错状态并终止运行。 NORMAL：将相应消息继续下发给目的端数据源，由目的端数据源来处理。因为不同目的端数据源对DDL消息处理策略可能会不同，因此DataWorks只执行转发操作。 |
|---|---|---|---|
| RequestId | String | 0000-ABCD-EFG | 本次调用的唯一ID。用于出现错误后定位日志， 排查问题。 |
| Success | Boolean | true | 请求是否成功。取值如下： true：成功。 false：失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDIProjectConfig &DestinationType=elasticsearch &ProjectId=1000 &RegionId=default &SourceType=mysql
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```json
<RequestId>0000-ABCD-EFG</RequestId> <Data>
    <Config>
{"RENAMECOLUMN":"WARNING","DROPTABLE":"WARNING","CREATETABLE":"WARNING","MODIFYCOLUMN":"W NING","TRUNCATETABLE":"WARNING","DROPCOLUMN":"WARNING","ADDCOLUMN":"WARNING","RENAMETABLE "WARNING"}</Config> </Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG",
    "Data": {
        "Config": "
{\"RENAMECOLUMN\":\"WARNING\",\"DROPTABLE\":\"WARNING\",\"CREATETABLE\":\"WARNING\",\"MOD YCOLUMN\":\"WARNING\",\"TRUNCATETABLE\":\"WARNING\",\"DROPCOLUMN\":\"WARNING\",\"ADDCOLUM ":\"WARNING\",\"RENAMETABLE\":\"WARNING\"}"
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.DI.NoPri vilege | No access. | 没有权限访问 |
| 500 | InternalError.DI.Par ameter | A DI internal error occurred. | 数据集成内部业务错误 |
| 400 | Invalid.DI.Paramete r | The parameter is invalid. | 参数错误 |

#### TestNetworkConnection

调用TestNetworkConnection接口，测试目标数据源与所使用资源组的网络连通性。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TestNetworkCon nection | 系统规定参数。取值： TestNetworkConnection。 |
| DatasourceNam e | String | 是 | mysql name _ | 目标数据源的名称。 |

DataWorks

| EnvType | String | 是 | 1 | 目标数据源所属的环境。取值如下： 0：开发环境。 1：生产环境。 |
|---|---|---|---|---|
| ProjectId | Long | 是 | 10000 | 目标数据源所在的DataWorks工作空间 ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| ResourceGroup | String | 是 | S res group 2X _ _ _ XXX4 1619100X _ XXXX | 目标数据源所使用的资源组的标识 （Identifier）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD-EFG | 本次调用的唯一ID。用于出现错误后定位日志， 排查问题。 |
| Success | Boolean | true | 请求是否成功。 |
| TaskList | Struct |  | 测试数据源与资源组网络连通性的返回结果。 |
| ConnectMessa ge | String | 可连通 | 测试目标数据源与其所使用资源组的网络连通性失败后的原因描述。如果数据源与资源组网络连通性测试成功，则该参数的返回值为空。 |
| ConnectStatus | Boolean | true | 测试目标数据源与其所使用资源组网络连通性的结果状态。取值如下： true：表示目标数据源与其所使用资源组的网络连通成功。 false：表示目标数据源与其所使用资源组的网络连通失败。您可以查看 ConnectMessage参数定位失败原因。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=TestNetworkConnection &DatasourceName=mysql_name &EnvType=1 &ProjectId=10000 &RegionId=default &ResourceGroup=S_res_group_2XXXX4_1619100XXXXX
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG</RequestId> <TaskList>
    <ConnectStatus>true</ConnectStatus>
    <ConnectMessage>可连通</ConnectMessage>
</TaskList> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG",
    "TaskList": {
        "ConnectStatus": true,
        "ConnectMessage": "可连通"
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.DI.NoPri vilege | No access. | 没有权限访问 |
| 500 | InternalError.DI.Par ameter | A DI internal error occurred. | 数据集成内部业务错误 |
| 400 | Invalid.DI.Paramete r | The parameter is invalid. | 参数错误 |

#### UpdateDIProjectConfig

调用UpdateDIProjectConfig修改当前工作空间中数据集成同步解决方案任务默认的全局配置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateDIProject Config | 系统规定参数。取值： UpdateDIProjectConfig。 |

DataWorks

| DestinationType | String | 是 | odps | 数据集成同步解决方案任务的目的端数据源。该参数不能为空。 调用UpdateDIProjectConfig修改同步解决方案的全局配置，目前仅支持配置目的端数据源为analyticdb for mysql、 _ _ odps、elasticsearch、holo、mysql及 polardb。 |
|---|---|---|---|---|
| ProjectConfig | String | 是 | {"RENAMECOLU MN":"WARNING", "DROPTABLE":" WARNING","CRE ATETABLE":"WA RNING","MODIFY COLUMN":"WAR NING","TRUNCA TETABLE":"WAR NING","DROPCO LUMN":"WARNIN G","ADDCOLUM N":"WARNING"," RENAMETABLE": "WARNING"} | 修改后的数据集成同步解决方案任务默认的全局配置内容（即对不同DDL消息类型配置的默认处理策略）。请使用JSON格式。示例如下： {"RENAMECOLUMN":"WARNING","DR OPTABLE":"WARNING","CREATETABL E":"WARNING","MODIFYCOLUMN":"W ARNING","TRUNCATETABLE":"WARNI NG","DROPCOLUMN":"WARNING","AD DCOLUMN":"WARNING","RENAMETAB LE":"WARNING"} DDL消息类型如下： RENAMECOLUMN：重命名列。 DROPTABLE：删除表。 CREATETABLE：新建表。 MODIFYCOLUMN：修改列类型。 TRUNCATETABLE：清空表。 DROPCOLUMN：删除列。 ADDCOLUMN：新增列。 RENAMETABLE：重命名表。 DataWorks收到对应类型的DDL消息时， 处理策略如下： WARNING：直接丢弃该消息，同时会在实时同步日志中记录告警信息，指明该消息因执行出错被丢弃。 IGNORE：直接丢弃该消息，不再向目的端数据源发送。 CRITICAL：实时同步任务直接显示出错状态并终止运行。 NORMAL：将相应消息继续下发给目的端数据源，由目的端数据源来处理。因为不同目的端数据源对DDL消息处理策略可能会不同，因此DataWorks只执行转发操作。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| SourceType | String | 是 | mysql | 数据集成同步解决方案任务的源端数据源。 调用UpdateDIProjectConfig修改同步解决方案任务的全局配置，目前仅支持配置源端数据源为oracle、mysql、 polardb、datahub、drds及 analyticdb for mysql。 _ _ 如果不配置源端数据源，则默认全局配置对所有的源端数据源均生效。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 修改目标工作空间中数据集成同步解决方案任务默认全局配置的返回结果。 |
| Status | String | success | 修改数据集成同步解决方案任务默认的全局配置是否成功。取值如下： success：修改成功。 fail：修改失败。 |
| RequestId | String | 0000-ABCD-EFG | 本次调用的唯一ID。用于出现错误后定位日志， 排查问题。 |
| Success | Boolean | true | 请求是否成功。取值如下： true：成功。 false：失败。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=UpdateDIProjectConfig &DestinationType=odps &ProjectConfig= {"RENAMECOLUMN":"WARNING","DROPTABLE":"WARNING","CREATETABLE":"WARNING","MODIFYCOLUMN":"W NING","TRUNCATETABLE":"WARNING","DROPCOLUMN":"WARNING","ADDCOLUMN":"WARNING","RENAMETABLE "WARNING"} &ProjectId=10000 &RegionId=default &SourceType=mysql
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG</RequestId> <Data>
    <Status>success</Status>
</Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG",
    "Data": {
        "Status": "success"
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.DI.NoPri vilege | No access. | 没有权限访问 |
| 500 | InternalError.DI.Par ameter | A DI internal error occurred. | 数据集成内部业务错误 |
| 400 | Invalid.DI.Paramete r | The parameter is invalid. | 参数错误 |

#### UpdateDISyncTask

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateDISyncTa sk | 系统规定参数。取值： UpdateDISyncTask。 |
| FileId | Long | 是 | 1000000 | 需要更新的数据集成同步任务的任务ID。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| TaskContent | String | 是 | {"type":"job","ve rsion":"2.0","ste ps": [{"stepType":"m ysql","paramete r": {"envType":1,"d atasource":"mys ql pub","column _ ": ["id","name","cr eate time","age _ ","score","t 01"], _ "connection": [{"datasource":" mysql pub","tab _ le": ["u pk"]}],"wher _ e":"","splitPk":"id ","encoding":"UT F- 8"},"name":"Re ader","category" :"reader"}, {"stepType":"od ps","parameter": {"partition":"pt= ${bizdate}","tru ncate":true,"dat asource":"odps f _ irst","envType": 1,"column": ["id","name","cr eate time","age _ ","score","t 01"], _ "emptyAsNull":f alse,"tableCom ment":"null","ta ble":"u pk"},"na _ me":"Writer","ca tegory":"writer" }],"setting": {"executeMode" :null,"errorLimit" : {"record":""},"s peed": {"concurrent":2, "throttle":false} },"order": {"hops": [{"from":"Reade r","to":"Writer"}] }} | 更新已创建的数据集成同步任务通过脚本模式配置的任务内容。当前仅支持通过 UpdateDISyncTask接口更新数据集成离线同步任务。如果您无需更新数据集成同步任务的配置内容，则可将该参数置为空。 |
|---|---|---|---|---|
| TaskParam | String | 是 | {"ResourceGrou p":"S res group _ _ XXX XXXX"} _ _ | 更新数据集成同步任务的配置参数。请使用JSON格式。 目前仅支持更新数据集成同步任务的配置参数ResourceGroup，即数据集成同步任务所使用的数据集成资源组标识 （Identifier）。 如果您无需更新数据集成同步任务的配置参数，则可将该参数置为空。 |

DataWorks

| TaskType | String | 是 | DI OFFLINE _ | 修改的数据集成同步任务的任务类型。 目前仅支持使用UpdateDISyncTask接口修改数据集成离线同步任务 （DI OFFLINE）。 _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 更新数据集成同步任务的返回结果。 |
| Message | String | ResourceGroup: [S res group XXX] _ _ _ is invalid. | 更新数据集成同步任务失败后的原因描述。如果更新数据集成同步任务成功，则该参数的返回值为空。 |
| Status | String | success | 更新数据集成同步任务的结果状态。取值如下： success：表示更新数据集成同步任务成功。 fail：表示更新数据集成同步任务失败。 |
| RequestId | String | 0bc141151593763 5973**** | 请求ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 请求是否成功。取值如下： true：成功。 false：失败。 |

**示例**

请求示例 DataWorks

```json
&FileId=1000000 &ProjectId=10000 &RegionId=default &TaskContent={"type":"job","version":"2.0","steps":[{"stepType":"mysql","parameter":{"e nvType":1,"datasource":"mysql_pub","column": ["id","name","create_time","age","score","t_01"],"connection": [{"datasource":"mysql_pub","table": ["u_pk"]}],"where":"","splitPk":"id","encoding":"UTF- 8"},"name":"Reader","category":"reader"},{"stepType":"odps","parameter": {"partition":"pt=${bizdate}","truncate":true,"datasource":"odps_first","envType":1,"colum
```

:

```json
["id","name","create_time","age","score","t_01"],"emptyAsNull":false,"tableComment":"null "table":"u_pk"},"name":"Writer","category":"writer"}],"setting": {"executeMode":null,"errorLimit":{"record":""},"speed": {"concurrent":2,"throttle":false}},"order":{"hops":[{"from":"Reader","to":"Writer"}]}} &TaskParam={"ResourceGroup":"S_res_group_XXX_XXXX"} &TaskType=DI_OFFLINE
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1411515937635973****</RequestId> <Data>
    <Status>success</Status>
    <Message>ResourceGroup:[S_res_group_XXX] is invalid.</Message>
</Data> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1411515937635973****",
    "Data": {
        "Status": "success",
        "Message": "ResourceGroup:[S_res_group_XXX] is invalid."
    },
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.DI.NoPri vilege | No access. | 没有权限访问 |
| 500 | InternalError.DI.Par ameter | A DI internal error occurred. | 数据集成内部业务错误 |

DataWorks

| 400 | Invalid.DI.Paramete r | The parameter is invalid. | 参数错误 |
|---|---|---|---|

#### GetDISyncTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Query | 是 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |
| TaskType | Strin g | Query | 是 | DI REALTIME _ | 目标数据源所关联的数据集成任务类型。取值： DI REALTIME：表示数 _ 据集成实时同步任务。 DI SOLUTION：表示数 _ 据集成同步解决方案。 |
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |
| FileId | Long | Query | 是 | 100 | 当TaskType为 DI REALTIME时，则 _ FileId为实时同步任务的文件ID。 当TaskType为 DI SOLUTION时，则 _ FileId为同步解决方案的任务ID。 您可以调用ListFiles接口获取文件ID或任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。取值： true：成功。 false：失败。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 16A96B9A-F203- 4EC5-8E43- CB92E68F**** | 请求ID。用于定位日志，排查问题。 |
| Data | Struct |  | 数据集成任务的返回结果。 |
| -Code | String | { "extend": { "mode": "wizard", "resourceGroup": "S res group 2871 _ _ _ 14642182658 156 _ 0324290517" }, "nodeDef": {}, "order": { "hops": [ { "from": "datahub 8htXSsfi _ S2vtZCVG", "to": "datahub CRHBAy _ GfhSaLmv2f" } ] }, "setting": { "errorLimit": {}, "jvmOption": "" }, "steps": [ { "stepType": "datahub", "category": "writer", "displayName": "DataHub1", "parameter": { "batchSize": 1000, "datasource": "datahub cloud de _ _ v test", "topic": _ "dwd tfc opt spee _ _ _ d rid amap rt" }, _ _ _ "name": "datahub CRHBAy _ GfhSaLmv2f", "gui": { "x": 262, "y": 325 } }, { "stepType": "datahub", "displayName": "DataHub2", "parameter": { "datasource": "datahub uric test _ _ ", "topic": "dwd tfc opt spee _ _ _ d rid amap rt 330 _ _ _ _ 000", "batchSize": 1000 }, "name": "datahub 8htXSsfi _ S2vtZCVG", "gui": { "x": 268, "y": 160.5 }, "category": "writer" } ] } | 如果TaskType为DI REALTIME，则表示实时 _ 同步任务的详情。 如果TaskType为DI SOLUTION，则为null。 _ |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Status | String | Success | 数据集成同步任务的结果状态。取值： Success：表示数据集成同步任务成功。 Fail：表示数据集成同步任务失败。 |
| -Message | String | fileId:[100] is invalid. | 数据集成同步任务失败后的原因描述。 如果数据集成同步任务成功，则该参数为空。 |
| -SolutionDetail | Struct |  | 如果TaskType为DI REALTIME，则为null。 _ 如果TaskType为DI SOLUTION，则表示同 _ 步解决方案任务的详情。 |
| --Status | String | 0 | 同步解决方案的执行状态，取值： 0：成功 1：未运行 2：运行中 3：失败 4：提交 5：待人工确认 6：人工确认完成 7：其他 8：等待 9：已删除 |
| --Type | String | holo | 同步解决方案任务的类型。 |
| --StartTime | String | 2021-12-07 14:40:51 | 同步解决方案任务的开始时间。 |
| --CreatorName | String | dataworks di _ | 同步解决方案任务的创建者名称。 |
| --ProjectId | Long | 10000 | 同步解决方案任务所在的项目ID。 |
| --SourceType | String | mysql | 同步解决方案任务源端的类型。 |
|  |  | { "holoDatasource": "holo", "offlineSyncConfig" : { "nodeNameRule": "oneclick holo di $ _ _ _ {db table name sr _ _ _ c} to ${db table _ _ _ _ name dest}", _ "resourceGroup": "group 219193793 _ 999490" }, |  |

DataWorks

| 参数名称 | 类型 | "processRuleId": 示例 1007, | 说明 |
|---|---|---|---|
| -- ProcessConten t | String | "readerConcurrent" : 10, "realtimeSyncConfi g": { "content": { "order": { "hops": [ { "from": "reader", "to": "writer" } ] }, "setting": { "speed": { "readerConcurrent" : 10 } }, "steps": [ { "stepType": "mysql", "name": "reader", "category": "reader", "parameter": { "connection": [ { "datasource": "mm", "datasourceType": "mysql", "table": [] } ] } }, { "stepType": "holo", "name": "writer", "category": "writer", "parameter": { "datasource": "holo", "writeMode": "replay", "datasourceSchem a": "public", "tableMappingRule ": { "datasource": [ { "tableRule": [], "srcDatasourceNa me": "mm" } ] } } } ] }, "extend": { "mode": "migration holo", _ "resourceGroup": "group 219193793 _ 999490" } }, "setting": { "autoCreateWorkfl ow": true, "userDefinedFileNa meExpression": "oneclick" }, "srcType": "mysql", "tableMappingRule FromRealtimeSync Config": { "datasource": [ { "srcDatasourceNa me": "mm", "tableRule": [] } ] } } | 同步解决方案的配置详情。 |
| --Name | String | holo 20211206161 _ 025 | 同步解决方案任务的名称。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ProcessExtra | String | { "processType": "new", "tableNum": 300 } | 同步解决方案任务的额外参数。 |
| --SubmitTime | String | 2021-12-07 14:40:51 | 同步解决方案任务提交的时间。 |
| --Id | Long | 100 | 同步解决方案的任务ID。 |

**示例**

请求示例

```
&ProjectId=10000 &TaskType=DI_REALTIME &RegionId=default &FileId=100
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"16A96B9A-F203-4EC5-8E43-CB92E68F****",
 "Data":{
  "Status":"Success",
  "Message":"fileId:[100] is invalid.",
  "Code":"{  \"extend\": {    \"mode\": \"wizard\",    \"resourceGroup\":
\"S_res_group_287114642182658_1560324290517\" }, \"nodeDef\": {}, \"order\": { \" hops\": [ { \"from\": \"datahub_8htXSsfiS2vtZCVG\", \"to\": \"datahub _CRHBAyGfhSaLmv2f\" } ] }, \"setting\": { \"errorLimit\": {}, \"jvmOptio n\": \"\" }, \"steps\": [ { \"stepType\": \"datahub\", \"category\": \"wr iter\", \"displayName\": \"DataHub1\", \"parameter\": { \"batchSize\": 1000, \"datasource\": \"datahub_cloud_dev_test\", \"topic\": \"dwd_tfc_opt _speed_rid_amap_rt\" }, \"name\": \"datahub_CRHBAyGfhSaLmv2f\", \"gui\": { \"x\": 262, \"y\": 325 } }, { \"stepType\": \"datahub\", \"displayName\": \"DataHub2\", \"parameter\": { \"datasource\": \"datahub_ur ic_test\", \"topic\": \"dwd_tfc_opt_speed_rid_amap_rt_330000\", \"batchSiz e\": 1000 }, \"name\": \"datahub_8htXSsfiS2vtZCVG\", \"gui\": { \" x\": 268, \"y\": 160.5 }, \"category\": \"writer\" } ]}",
  "SolutionDetail":{
   "Status":"0",
   "Type":"holo",
   "ProcessContent":"{  \"holoDatasource\": \"holo\",  \"offlineSyncConfig\": {
\"nodeNameRule\": \"oneclick_holo_di_${db_table_name_src}_to_${db_table_name_dest}\", \"resourceGroup\": \"group_219193793999490\" }, \"processRuleId\": 1007, \"readerConcurrent\": 10, \"realtimeSyncConfig\": { \"content\": { \"order\": { \"hops\": [ { \"from\": \"reader\", \"to\": \"wri ter\" } ] }, \"setting\": { \"speed\": { \"read erConcurrent\": 10 } }, \"steps\": [ { \"stepType\":
```

\ \ \ \ \ \ \ \ \ \ \ DataWorks

```json
\"mysql\", \"name\": \"reader\", \"category\": \"reader\", \" parameter\": { \"connection\": [ { \"datasource\": \"mm\", \"datasourceType\": \"mysql\", \"table\": [] } ] } }, { \"stepType\": \"holo\", \"name\": \"writer\", \"category\": \"writer\", \"parameter\": { \"datasource\": \"holo\", \"writeMode\": \"replay\", \"datasourceSchema\": \"public\", \"tableMappingRule\": { \"data source\": [ { \"tableRule\": [], \"srcDa tasourceName\": \"mm\" } ] } } } ] }, \"extend\": { \"mode\": \"migration_holo\", \"resourceGroup\": \"gr oup_219193793999490\" } }, \"setting\": { \"autoCreateWorkflow\": true, \"use rDefinedFileNameExpression\": \"oneclick\" }, \"srcType\": \"mysql\", \"tableMappingRuleFromRealtimeSyncConfig\": { \"datasource\": [ { \"srcDa tasourceName\": \"mm\", \"tableRule\": [] } ] }}",
   "SourceType":"mysql",
   "StartTime":"2021-12-07 14:40:51",
   "ProjectId":10000,
   "Id":100,
   "SubmitTime":"2021-12-07 14:40:51",
   "CreatorName":"dataworks_di",
   "ProcessExtra":"{  \"processType\": \"new\",  \"tableNum\": 300}",
   "Name":"holo_20211206161025"
  }
 },
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>16A96B9A-F203-4EC5-8E43-CB92E68F****</RequestId> <Data>
 <Status>Success</Status>
 <Message>fileId:[100] is invalid.</Message>
 <Code>{
  &quot;extend&quot;: {
    &quot;mode&quot;: &quot;wizard&quot;,
    &quot;resourceGroup&quot;: &quot;S_res_group_287114642182658_1560324290517&quot;
  },
  &quot;nodeDef&quot;: {},
  &quot;order&quot;: {
    &quot;hops&quot;: [
      {
        &quot;from&quot;: &quot;datahub_8htXSsfiS2vtZCVG&quot;,
        &quot;to&quot;: &quot;datahub_CRHBAyGfhSaLmv2f&quot;
      }
```

]

```
  },
  &quot;setting&quot;: {
    &quot;errorLimit&quot;: {},
    &quot;jvmOption&quot;: &quot;&quot;
  },
  &quot;steps&quot;: [
    {
      &quot;stepType&quot;: &quot;datahub&quot;,
```

DataWorks

```
      &quot;category&quot;: &quot;writer&quot;,
      &quot;displayName&quot;: &quot;DataHub1&quot;,
      &quot;parameter&quot;: {
        &quot;batchSize&quot;: 1000,
        &quot;datasource&quot;: &quot;datahub_cloud_dev_test&quot;,
        &quot;topic&quot;: &quot;dwd_tfc_opt_speed_rid_amap_rt&quot;
      },
      &quot;name&quot;: &quot;datahub_CRHBAyGfhSaLmv2f&quot;,
      &quot;gui&quot;: {
        &quot;x&quot;: 262,
        &quot;y&quot;: 325
      }
    },
    {
      &quot;stepType&quot;: &quot;datahub&quot;,
      &quot;displayName&quot;: &quot;DataHub2&quot;,
      &quot;parameter&quot;: {
        &quot;datasource&quot;: &quot;datahub_uric_test&quot;,
        &quot;topic&quot;: &quot;dwd_tfc_opt_speed_rid_amap_rt_330000&quot;,
        &quot;batchSize&quot;: 1000
      },
      &quot;name&quot;: &quot;datahub_8htXSsfiS2vtZCVG&quot;,
      &quot;gui&quot;: {
        &quot;x&quot;: 268,
        &quot;y&quot;: 160.5
      },
      &quot;category&quot;: &quot;writer&quot;
    }
```

]

```xml
}</Code>
  <-SolutionDetail>
   <Status>0</Status>
   <Type>holo</Type>
   <ProcessContent>{
  &quot;holoDatasource&quot;: &quot;holo&quot;,
  &quot;offlineSyncConfig&quot;: {
    &quot;nodeNameRule&quot;:
&quot;oneclick_holo_di_${db_table_name_src}_to_${db_table_name_dest}&quot;,
    &quot;resourceGroup&quot;: &quot;group_219193793999490&quot;
  },
  &quot;processRuleId&quot;: 1007,
  &quot;readerConcurrent&quot;: 10,
  &quot;realtimeSyncConfig&quot;: {
    &quot;content&quot;: {
      &quot;order&quot;: {
        &quot;hops&quot;: [
          {
            &quot;from&quot;: &quot;reader&quot;,
            &quot;to&quot;: &quot;writer&quot;
          }
```

]

```
      },
      &quot;setting&quot;: {
        &quot;speed&quot;: {
```

DataWorks

```
          &quot;readerConcurrent&quot;: 10
        }
      },
      &quot;steps&quot;: [
        {
          &quot;stepType&quot;: &quot;mysql&quot;,
          &quot;name&quot;: &quot;reader&quot;,
          &quot;category&quot;: &quot;reader&quot;,
          &quot;parameter&quot;: {
            &quot;connection&quot;: [
              {
                &quot;datasource&quot;: &quot;mm&quot;,
                &quot;datasourceType&quot;: &quot;mysql&quot;,
                &quot;table&quot;: []
              }
```

]

```
          }
        },
        {
          &quot;stepType&quot;: &quot;holo&quot;,
          &quot;name&quot;: &quot;writer&quot;,
          &quot;category&quot;: &quot;writer&quot;,
          &quot;parameter&quot;: {
            &quot;datasource&quot;: &quot;holo&quot;,
            &quot;writeMode&quot;: &quot;replay&quot;,
            &quot;datasourceSchema&quot;: &quot;public&quot;,
            &quot;tableMappingRule&quot;: {
              &quot;datasource&quot;: [
                {
                  &quot;tableRule&quot;: [],
                  &quot;srcDatasourceName&quot;: &quot;mm&quot;
                }
```

]

```
            }
          }
        }
```

]

```
    },
    &quot;extend&quot;: {
      &quot;mode&quot;: &quot;migration_holo&quot;,
      &quot;resourceGroup&quot;: &quot;group_219193793999490&quot;
    }
  },
  &quot;setting&quot;: {
    &quot;autoCreateWorkflow&quot;: true,
    &quot;userDefinedFileNameExpression&quot;: &quot;oneclick&quot;
  },
  &quot;srcType&quot;: &quot;mysql&quot;,
  &quot;tableMappingRuleFromRealtimeSyncConfig&quot;: {
    &quot;datasource&quot;: [
      {
        &quot;srcDatasourceName&quot;: &quot;mm&quot;,
        &quot;tableRule&quot;: []
      }
```

] DataWorks ]

```xml
  }
}</ProcessContent>
    <SourceType>mysql</SourceType>
    <StartTime>2021-12-07 14:40:51</StartTime>
    <ProjectId>10000</ProjectId>
    <Id>100</Id>
    <SubmitTime>2021-12-07 14:40:51</SubmitTime>
    <CreatorName>dataworks_di</CreatorName>
    <ProcessExtra>{
  &quot;processType&quot;: &quot;new&quot;,
  &quot;tableNum&quot;: 300
}</ProcessExtra>
     <Name>holo_20211206161025</Name>
    </-SolutionDetail>
   </Data>
   <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1120010003 | Param.Invalid | The parameter is invalid. |
| 403 | 1120010001 | Forbidden.Access | Access is forbidden. |
| 500 | 1120010002 | InternalError.System | An internal error occurred. |

#### GetDISyncInstanceInfo

调用GetDISyncInstanceInfo接口，获取实时同步任务和同步解决方案任务的运行状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Query | 是 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 该参数用来确定本次API调用操作使用的DataWorks 工作空间。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskType | Strin g | Query | 是 | DI REALTIME _ | 目标数据源所关联的数据集成同步任务的任务类型。取值如下： DI REALTIME：表示数 _ 据集成实时同步任务。 DI SOLUTION：表示数 _ 据集成同步解决方案。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| FileId | Long | Query | 是 | 100 | 当TaskType为 DI REALTIME时，则 _ FileId为实时同步任务的文件ID。 当TaskType为 DI SOLUTION时，则 _ FileId为同步解决方案的任务ID。 您可以调用ListFiles接口获取任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。取值如下： true：成功。 false：失败。 |
| RequestId | String | 0bc141151593763 5973**** | 请求ID。用于定位日志，排查问题。 |
| Data | Struct |  |  |
| -Status | String | RUN | 如果taskType为DI REALTIME，则status为 _ 实时任务的运行状态。包括：PAUSE、 NORUN、RUN、KILLING、WAIT。 如果taskType为DI SOLITION， 则status为 _ 同步解决方案的运行状态。包括：success、 fail。 |
| -Message | String | fileId[100] is invalid | 获取同步任务运行状态失败后的原因描述。如果获取数据集成同步任务成功，则该参数的返回值为空。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Name | String | streamx name _ | 如果taskType为DI REALTIME，则name为 _ 实时同步任务的名称。 如果taskType为DI SOLITION， 则name为 _ 空。 |
| -SolutionInfo | Struct |  |  |
| --StepDetail | Array |  |  |
| ---Status | String | success | 同步解决方案运行步骤的状态。 |
| ---StepId | Long | 1 | 同步解决方案运行步骤的ID。 |
| ---StepName | String | 创建base表 | 同步解决方案运行步骤的名称。 |
| ---Info | String | {\"fusionProps\": {\"dataSource\": [{\"fileName\":\"hol o 2022102016161 _ 3\",\"status\":\"SUC CESS\"}]},\"custo mProps\": {\"showSN\":true,\" columns\": [{\"dataIndex\":\"fil eName\",\"width\": 0.8,\"title\":\"实时同步名称\"}, {\"dataIndex\":\"st atus\",\"width\":0.2, \"title\":\"状态 \"}]},\"component Name\":\"Table\"} | 同步解决方案运行信息。 |
| --Status | String | run | 同步解决方案运行状态。 |
| --Id | Long | 100 | 同步解决方案任务ID。 |
| --CreatorName | String | dataworks 3h1 _ | 同步解决方案任务创建者名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDISyncInstanceInfo &ProjectId=10000 &TaskType=DI_REALTIME &RegionId=default &FileId=100
```

&公共请求参数 DataWorks 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0bc1411515937635973****",
 "Data":{
  "Status":"RUN",
  "Message":"fileId[100] is invalid",
  "SolutionInfo":{
   "Status":"run",
   "StepDetail":{
    "Status":"success",
    "StepId":1,
    "StepName":"创建base表",
    "Info":"{\\\"fusionProps\\\":{\\\"dataSource\\\":
[{\\\"fileName\\\":\\\"holo_20221020161613\\\",\\\"status\\\":\\\"SUCCESS\\\"}]},\\\"cust Props\\\":{\\\"showSN\\\":true,\\\"columns\\\": [{\\\"dataIndex\\\":\\\"fileName\\\",\\\"width\\\":0.8,\\\"title\\\":\\\"实时同步名称\\\" },{\\\"dataIndex\\\":\\\"status\\\",\\\"width\\\":0.2,\\\"title\\\":\\\"状态\\\"}]},\\\" componentName\\\":\\\"Table\\\"}"
   },
   "Id":100,
   "CreatorName":"dataworks_3h1"
  },
  "Name":"streamx_name"
 },
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0bc1411515937635973****</RequestId> <Data>
 <Status>RUN</Status>
 <Message>fileId[100] is invalid</Message>
 <SolutionInfo>
  <Status>run</Status>
  <StepDetail>
   <Status>success</Status>
   <StepId>1</StepId>
   <StepName>创建base表</StepName>
   <Info>{\&quot;fusionProps\&quot;:{\&quot;dataSource\&quot;:
[{\&quot;fileName\&quot;:\&quot;holo_20221020161613\&quot;,\&quot;status\&quot;:\&quot;SU ESS\&quot;}]},\&quot;customProps\&quot;: {\&quot;showSN\&quot;:true,\&quot;columns\&quot;: [{\&quot;dataIndex\&quot;:\&quot;fileName\&quot;,\&quot;width\&quot;:0.8,\&quot;title\&qu
```

;:\&quot;实时同步名称\&quot;},

```xml
{\&quot;dataIndex\&quot;:\&quot;status\&quot;,\&quot;width\&quot;:0.2,\&quot;title\&quot; &quot;状态\&quot;}]},\&quot;componentName\&quot;:\&quot;Table\&quot;}</Info>
  </StepDetail>
  <Id>100</Id>
  <CreatorName>dataworks_3h1</CreatorName>
 </SolutionInfo>
 <Name>streamx_name</Name>
</Data> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1120010003 | Param.Invalid | The parameter is invalid. |
| 403 | 1120010001 | Forbidden.Access | Access is forbidden. |
| 500 | 1120010002 | InternalError.System | An internal error occurred. |

#### ListRefDISyncTasks

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Query | 是 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间ID。 |
| Datasourc eName | Strin g | Query | 是 | mysql datasource _ | 需要查看的目标数据源名称。您可以调用 ListDataSources接口获取数据源名称。 |
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |
| TaskType | Strin g | Query | 是 | DI OFFLINE _ | 目标数据源所关联的数据集成同步任务类型。取值： DI OFFLINE：表示数据 _ 集成离线同步任务。 DI REALTIME：表示数 _ 据集成实时同步任务。 |
| RefType | Strin g | Query | 是 | from | 选择目标数据源作为数据集成同步任务的源端或目的端。取值： from：目标数据源作为数据集成同步任务的源端。 to：目标数据源作为数据集成同步任务的目的端。 |
| PageNum ber | Long | Query | 否 | 1 | 请求的数据页数，用于翻页。 |
| PageSize | Long | Query | 否 | 100 | 每页显示的数据条数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 请求是否成功。取值如下： true：成功。 false：失败。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 16A96B9A-F203- 4EC5-8E43- CB92E68F**** | 请求ID。用于定位日志，排查问题。 |
| Data | Struct |  | 数据集成任务的返回结果。 |
| -DISyncTasks | Array |  | 数据集成任务的返回结果。 |
| -- DiSourceDatas ource | String | mysql datasource _ | 源端数据源名称。 |
| --TaskType | String | DI OFFLINE _ | 目标数据源所关联的数据集成同步任务类型。 |
| -- DiDestination Datasource | String | maxcompute data _ source | 目的端数据源名称。 |
| --NodeName | String | test note 01 _ _ | 节点名称。 |
| --NodeId | Long | 122333 | 节点ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListRefDISyncTasks &ProjectId=10000 &DatasourceName=mysql_datasource &RegionId=default &TaskType=DI_OFFLINE &RefType=from
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"16A96B9A-F203-4EC5-8E43-CB92E68F****",
 "Data":{
  "DISyncTasks":{
   "DiDestinationDatasource":"maxcompute_datasource",
   "NodeName":"test_note_01",
   "DiSourceDatasource":"mysql_datasource",
   "TaskType":"DI_OFFLINE",
   "NodeId":122333
  }
 },
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>16A96B9A-F203-4EC5-8E43-CB92E68F****</RequestId> <Data>
 <DISyncTasks>
  <DiDestinationDatasource>maxcompute_datasource</DiDestinationDatasource>
  <NodeName>test_note_01</NodeName>
  <DiSourceDatasource>mysql_datasource</DiSourceDatasource>
  <TaskType>DI_OFFLINE</TaskType>
  <NodeId>122333</NodeId>
 </DISyncTasks>
</Data> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1120010003 | Invalid.DI.Parameter | The parameter is invalid. |
| 400 | 1120010004 | Invalid.DI.Parameter.File.Existe d | The file name already exists. |
| 403 | 1120010001 | Forbidden.DI.NoPrivilege | No access. |
| 500 | 1120010002 | InternalError.DI.Parameter | A DI internal error occurred. |

### 数据建模

#### QueryPublicModelEngine

**使用说明**

每次调用该接口均需使用FML语句请求获取查询信息。 除了数仓分层、业务过程和数据域查询外，其他引擎信息查询均可使用分页查询方式。您可以在FML语句 DataWorks 结尾增加 `offset num limit num` 语句，表示查询信息时的偏移量及每次返回的页数。目前偏移量取值仅支持为页数的倍数。 每次调用该接口时，最多返回1000条数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Text | Strin g | Body | 是 | show dim tables | 输入查询引擎信息的FML语句，当前仅支持show语句。 |
| ProjectId | Strin g | Body | 是 | 1234 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |
| RegionId | Strin g | Host | 否 | default | 服务所在的地域，为固定值default 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ReturnValue | Map | [ { "gmtModified": 最后修改时间, "code": "表名", "creatorId": "创建人 ID", "creatorName": "创建人名称", "modifierId": "修改人ID", "gmtCreate": 创建时间, "type": 表类型, "ownerId": "负责人ID", "uuid": "系统ID", "businessUnitUuid" : "业务板块ID", "detailType": "表二级类型", "ownerName": "负责人名称", "name": "表显示名", "modifierName": "最后修改人名称", "businessProcessU uid": "业务过程ID" } ] | 数据建模引擎信息的结果。 |
| RequestId | String | 4CFB2DED-7D9B- 4C42-B4AA- CFF4991D**** | 请求ID。用于定位日志，排查问题。 |

DataWorks

**返回结果说明**

**查询数仓分层使用的FML语句**

```
 show layers;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | dws | 数仓分层编码。 |
| englishName | String | dws | 数仓分层英文名。 |
| name | String | 汇总层 | 数仓分层中文名。 |
| ownerId | String | 0123456 | 负责人ID。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| description | String | 汇总层描述 | 备注。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询数据域使用的FML语句**

```
 show domains;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | member | 数据域编码。 |
| englishName | String | member | 数据域英文名。 |
| name | String | 会员 | 数据域中文名。 |
| ownerId | String | 0123456 | 负责人ID。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| businessUnitCode | String | bu-123456 | 业务板块编码。 |
| description | String | 会员域备注 | 备注。 |
| uuid | String | obj-123456 | 对象唯一标识。 |

|  | DataWorks |  |  | 开发指南·OpenAPI参考 |  |
|---|---|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseIdID。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseIdID。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询业务过程使用的FML语句**

无条件列表查询： show business_processes; 根据code查询业务过程： show business_processes where code='bp-code'; 根据数据域查询业务过程： show business_processes where data_domain='dm-code'; 输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | bp-123456 | 业务过程编码。 |
| englishName | String | pay | 业务过程英文名。 |
| name | String | 付款 | 业务过程中文名。 |
| dataDomainCode | String | trade | 所属数据域编码。 |
| dataDomainName | String | 交易 | 所属数据域中文名。 |
| dataDomainUuid | String | dm-123456 | 所属数据域UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| description | String | 付款 | 备注。 |
| source | Integer | 2 | 创建来源。可取值如下： 1：系统创建。 2：用户创建。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | creatorId | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |

|  | 开发指南·OpenAPI参考 |  |  | DataWork | s |
|---|---|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询业务分类使用的FML语句**

```
 show business_categories;
 show business_categories where code='code';
 show business_categories where keyword='keyword',
 show business_categories where uuid='uuid'
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| categoryDetail | DirectoryDetailDTO | {"uuid": "cate uuid", _ "code": "trd", "name": "交易"} | 业务分类详细信息。 |
| name | String | 电商 | 目录名称。 |
| detailType | String | DICT | 目录子类型。 |
| parentUuid | String | dy-123456 | 父级目录UUID。 |
| description | String | 描述信息 | 目录描述。 |
| code | String | ind | 业务分类code。 |
| dataDomains | List | [{"uuid": "domain1", "code": "trd", "name": "交易域"}] | 业务分类下挂靠数据域。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| businessUnitCode | String | bu-123456 | 业务板块编码。 |
| description | String | 描述信息 | 目录描述。 |
| categoryPath | String | tm.ind | 业务分类path。 |

**查询数据集市使用的FML语句**

```
 show markets;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| categoryDetail | DirectoryDetailDTO | {"uuid": "cate uuid", _ "code": "trd", "name": "交易"} | 数据集市详细信息。 |
| name | String | 电商 | 目录名称。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| detailType | String | DICT | 目录子类型。 |
| parentUuid | String | dy-123456 | 父级目录UUID。 |
| description | String | 描述信息 | 目录描述。 |
| code | String | ind | 业务分类code。 |
| subDetailType | String | common | 目录子类型细分类型。 |
| auditDTOList | List | [{"baseId":"123","sho wName":"test"}] | 审核人员列表。 |
| code | String | member | 数据域编码。 |
| englishName | String | member | 数据域英文名。 |
| name | String | 会员 | 数据域中文名。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| businessUnitCode | String | bu-123456 | 业务板块编码。 |
| description | String | 会员域备注 | 备注。 |
| auditDTOList | List | [{"baseId":"123","sho wName":"test"}] | 审核人员列表。 |
| categoryPath | String | tm.ind | 业务分类path。 |

**查询主题域使用的FML语句**

```
 show subjects;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| categoryDetail | DirectoryDetailDTO | {"uuid": "cate uuid", _ "code": "trd", "name": "交易"} | 主题详细信息。 |
| name | String | 电商 | 目录名称。 |
| detailType | String | DICT | 目录子类型。 |
| parentUuid | String | dy-123456 | 父级目录UUID。 |
| description | String | 描述信息 | 目录描述。 |
| code | String | ind | 业务分类code。 |
| subDetailType | String | common | 目录子类型细分类型。 |

| ·OpenAPI |  |  | DataWork |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| auditDTOList | List | [{"baseId":"123","sho wName":"test"}] | 审核人员列表。 |
| code | String | member | 数据域编码。 |
| englishName | String | member | 数据域英文名。 |
| name | String | 会员 | 数据域中文名。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| businessUnitCode | String | bu-123456 | 业务板块编码。 |
| description | String | 会员域备注 | 备注。 |
| auditDTOList | List | [{"baseId":"123","sho wName":"test"}] | 审核人员列表。 |
| categoryPath | String | tm.ind | 业务分类path。 |

**查询数据标准集使用的FML语句**

```
 show dict groups;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| name | String | 电商 | 目录名称。 |
| detailType | String | DICT | 目录子类型。 |
| parentUuid | String | dy-123456 | 父级目录UUID。 |
| description | String | 描述信息 | 目录描述。 |
| code | String | ind | 业务分类code。 |
| uuid | List | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询数据标准使用的FML语句**

```
 show dicts;
```

DataWorks 输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | shop type _ | 英文缩写。 |
| englishName | String | shop type | 英文名称。 |
| name | String | 店铺类型 | 中文名称。 |
| no | String | SN00001 | 标准编号。 |
| dataType | String | STRING | 数据类型。 |
| length | Integer | 10 | 列长度。 |
| numericalPrecision | Integer | 2 | 列精度。 |
| notNull | Boolean | false | 是否不为空。 |
| defaultValue | String | 旗舰店 | 默认值。 |
| parentNo | String | SN0001 | 父级标准编号。 |
| parentName | String | 店铺 | 父级标准名称。 |
| codeTableNo | String | shop type _ | 引用码表编号。 |
| codeTableName | String | 店铺类型码表 | 引用码表名称。 |
| codeTableUuid | String | tb-0001 | 引用码表UUID。 |
| directoryUuid | String | 所属目录UUID | 所属目录UUID。 |
| directoryName | String | 店铺目录 | 所属目录名称。 |
| description | String | remark | 备注。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询标准代码使用的FML语句**

```
 show code tables;
```

输出参数 DataWorks

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | shop type _ | 代码编码。 |
| name | String | 店铺类型 | 代码名称。 |
| extendName | String | shop type | 英文名称。 |
| description | String | remark | 描述。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询度量单位组使用的FML语句**

```
 show measure_unit groups;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| name | String | 电商 | 目录名称。 |
| detailType | String | DICT | 目录子类型。 |
| parentUuid | String | dy-123456 | 父级目录UUID。 |
| description | String | 描述信息 | 目录描述。 |
| code | String | ind | 分类code。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询度量单位使用的FML语句**

DataWorks

```
 show measure_units;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | yuan | 英文缩写。 |
| englishName | String | RMB | 英文名称。 |
| name | String | 元 | 列中文名称。 |
| directoryUuid | String | di-0001 | 单位分组UUID。 |
| directoryName | String | 货币 | 单位分组名称。 |
| description | String | remark | 备注。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询标准代码内容使用的FML语句**

```
 show codes from code_table；
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| codeContent | String | 0 | code内容值。 |
| extendNameContent | String | female | 扩展标准代码名称。 |
| nameContent | String | 女性 | 标准代码名称。 |
| description | String | remark | 标准代码描述。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |

| 开发指南·OpenAPI参考 |  |  | DataWork |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询命名词典使用的FML语句**

```
 show naming dicts;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | shop | 英文缩写。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| extendName | String | shop | 英文名称。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |
| name | String | 店铺 | 中文名称。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| uuid | String | obj-123456 | 对象唯一标识。 |

**查询表信息使用的FML语句**

```
 show tables;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | dim shop _ | 表编码。 |
| name | String | 店铺维度表 | 表中文名。 |
| type | Integer | 1 | 表类型。可取值如下： 0：事实表。 1：维度表。 |
| detailType | String | normal | 表具体类型。可取值如下： normal：普通维度。 enum：枚举维度。 transaction：事务事实。 |

DataWorks

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| businessProcessUuid | String | bp-123456 | 业务过程UUID。 |
| businessUnitUuid | String | bu-123456 | 业务板块UUID。 |
| dataWarehouseLayerU uid | String | ly-123456 | 数仓层UUID。 |
| businessCategoryUuid | String | bc-123456 | 业务分类UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| description | String | 店铺表备注 | 备注。 |
| config | String | json字符串 | 拓展属性配置。 |
| lifeCycle | Integer | 365 | 表生命周期。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询维度表使用的FML语句**

```
 show dim tables;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | dim shop _ | 表编码。 |
| name | String | 店铺维度表 | 表中文名。 |
| type | Integer | 1 | 表类型。可取值如下： 0：事实表。 1：维度表。 |
| detailType | String | normal | 表具体类型。可取值如下： normal：普通维度。 enum：枚举维度。 transaction：事务事实。 |
| businessProcessUuid | String | bp-123456 | 业务过程UUID。 |

| 开发指南·OpenAPI参考 |  |  | DataWork |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| businessUnitUuid | String | bu-123456 | 业务板块UUID。 |
| dataWarehouseLayerU uid | String | ly-123456 | 数仓层UUID。 |
| businessCategoryUuid | String | bc-123456 | 业务分类UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| description | String | 店铺表备注 | 备注。 |
| config | String | json字符串 | 拓展属性配置。 |
| lifeCycle | Integer | 365 | 表生命周期。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询事实表信息使用的FML语句**

```
 show fact tables;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | dim shop _ | 表编码。 |
| name | String | 店铺维度表 | 表中文名。 |
| type | Integer | 1 | 表类型。可取值如下： 0：事实表。 1：维度表。 |
| detailType | String | normal | 表具体类型。可取值如下： normal：普通维度。 enum：枚举维度。 transaction：事务事实。 |
| businessProcessUuid | String | bp-123456 | 业务过程UUID。 |
| businessUnitUuid | String | bu-123456 | 业务板块UUID。 |

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dataWarehouseLayerU uid | String | ly-123456 | 数仓层UUID。 |
| businessCategoryUuid | String | bc-123456 | 业务分类UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| description | String | 店铺表备注 | 备注。 |
| config | String | json字符串 | 拓展属性配置。 |
| lifeCycle | Integer | 365 | 表生命周期。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询汇总表使用的FML语句**

```
 show dws tables;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dataDomainUuid | String | dm-12345 | 数据域UUID。 |
| dataDomainCode | String | member | 数据域Code。 |
| dataDomainName | String | 会员 | 数据域名字。 |
| timePeriods | List | [{"uuid": "uuid", "code": "code", "name": "中文名称"}] | 时间周期列表。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| code | String | dws 001 _ | 表名。 |
| name | String | 支付汇总表 | 表中文名称。 |
| adjuncts | List | [{"uuid": "uuid", "code": "code", "name": "中文名称"}] | 修饰词列表。 |

| 开发指南·OpenAPI参考 |  |  | DataWork |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dimensions | List | [{"uuid": "uuid", "code": "code", "name": "中文名称"}] | 粒度。 |
| bizEntityUuid | String | dim-123456 | 业务对象UUID。 |
| bizEntityCode | String | dim shop _ | 业务对象英文缩写。 |
| bizEntityName | String | 店铺表 | 业务对象中文名称。 |
| relUuid | String | dim a-123456 _ | 关联维度UUID。 |
| type | Integer | 1 | 表类型。可取值如下： 0：事实表。 1：维度表。 |
| detailType | String | normal | 表具体类型。可取值如下： normal：普通维度。 enum：枚举维度。 transaction：事务事实。 |
| businessProcessUuid | String | bp-123456 | 业务过程UUID。 |
| businessUnitUuid | String | bu-123456 | 业务板块UUID。 |
| dataWarehouseLayerU uid | String | ly-123456 | 数仓层UUID。 |
| businessCategoryUuid | String | bc-123456 | 业务分类UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| description | String | 店铺表备注 | 备注。 |
| config | String | json字符串 | 拓展属性配置。 |
| lifeCycle | Integer | 365 | 表生命周期。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询应用表使用的FML语句**

```
 show ads tables;
```

DataWorks 输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dataDomainUuid | String | dm-12345 | 数据域UUID。 |
| dataDomainCode | String | member | 数据域Code。 |
| dataDomainName | String | 会员 | 数据域名称。 |
| timePeriods | List | [{"uuid": "uuid", "code": "code", "name": "中文名称"}] | 时间周期列表。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| code | String | dws 001 _ | 表名。 |
| name | String | 支付汇总表 | 表中文名称。 |
| adjuncts | List | [{"uuid": "uuid", "code": "code", "name": "中文名称"}] | 修饰词列表。 |
| dimensions | List | [{"uuid": "uuid", "code": "code", "name": "中文名称"}] | 粒度。 |
| bizEntityUuid | String | dim-123456 | 业务对象UUID。 |
| bizEntityCode | String | dim shop _ | 业务对象英文缩写。 |
| bizEntityName | String | 店铺表 | 业务对象中文名称。 |
| relUuid | String | dim a-123456 _ | 关联维度UUID。 |
| type | Integer | 1 | 表类型。可取值如下： 0：事实表。 1：维度表。 |
| detailType | String | normal | 表具体类型。可取值如下： normal：普通维度。 enum：枚举维度。 transaction：事务事实。 |
| businessProcessUuid | String | bp-123456 | 业务过程UUID。 |
| businessUnitUuid | String | bu-123456 | 业务板块UUID。 |
| dataWarehouseLayerU uid | String | ly-123456 | 数仓层UUID。 |
| businessCategoryUuid | String | bc-123456 | 业务分类UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |

| 开发指南·OpenAPI参考 |  |  | DataWork |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| description | String | 店铺表备注 | 备注。 |
| config | String | json字符串 | 拓展属性配置。 |
| lifeCycle | Integer | 365 | 表生命周期。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询表信息同时返回字段信息使用的FML语句**

```
 show full tables;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| tableUuid | String | tb-123456 | 表UUID。 |
| tableCode | String | dim shop _ | 表编码。 |
| tableName | String | 店铺表 | 表名称。 |
| columnCode | String | shop id _ | 列编码。 |
| columnName | String | 店铺Id | 列名称。 |
| columnUuid | String | col-123456 | 列UUID。 |
| columnType | String | STRING | 列数据类型。 |
| columnCategory | String | ATTRIBUTE | 列类别。 |

**查询列信息使用的FML语句**

```
 show columns from table_code;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| code | String | seller id _ | 列编码。 |
| name | String | 卖家Id | 列中文名。 |
| dataType | String | STRING | 数据类型。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| type | String | ATTRIBUTE | 字段类型。 |
| isPrimaryKey | Boolean | false | 是否主键。 |
| isPartitionKey | Boolean | false | 是否分区键。 |
| partitionOrder | Integer | 1 | 分区键顺序。 |
| notNull | Boolean | true | 是否非空。 |
| dataDictionaryUuid | String | member id _ | 数据字典编码。 |
| dataDictionaryCode | String | 会员Id | 数据字典名称。 |
| codeTableUuid | String | cd-123456 | 关联码表UUID。 |
| codeTableCode | String | sex | 关联码表编码。 |
| codeTableName | String | 性别 | 关联码表名称。 |
| measureUnitCode | String | percent | 关联单位编码。 |
| measureUnitName | String | 分 | 关联单位名称。 |
| sourceProjectName | String | autotest | 来源项目名称。 |
| sourceTableCode | String | dict | 来源表编码。 |
| sourceColumnCode | String | age | 来源字段编码。 |
| sourceRelationTag | String | label | 冗余关系标签。 |
| description | String | 字段备注 | 备注。 |
| orderId | String | 1 | 字段顺序。 |
| columnGroupName | Integer | col group 1 _ _ | 所属字段组。 |
| config | String | json字符串 | 拓展属性配置。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询修饰词使用的FML语句**

DataWorks

```
 show adjuncts;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| businessUnitUuid | String | bu-123456 | 业务板块UUID。 |
| businessUnitCode | String | test bu _ | 业务板块CODE。 |
| businessUnitName | String | 测试板块 | 业务板块NAME。 |
| dataDomainUuid | String | dt-123456 | 数据域UUID。 |
| dataDomainCode | String | member | 数据域CODE。 |
| dataDomainName | String | 会员域 | 数据域NAME。 |
| categoryUuid | String | cy-123456 | 业务分类UUID。 |
| categoryCode | String | trade | 业务分类CODE。 |
| categoryName | String | 电商 | 业务分类NAME。 |
| type | AdjunctTypeEnum | DIM VAL _ | 修饰词类型。 |
| code | String | beauty | 英文缩写。 |
| name | String | 美妆 | 中文名称。 |
| extendName | String | beauty | 英文名称。 |
| description | String | 美妆描述 | 描述。 |
| bizExpression | String | 用于报表统计口径 | 业务口径。 |
| expression | String | beauty = 1 | 修饰词语义表达式。 |
| bizEntityUuid | String | dim-123456 | 业务对象UUID。 |
| bizEntityCode | String | dim shop _ | 业务对象英文缩写。 |
| bizEntityName | String | 店铺表 | 业务对象中文名称。 |
| relUuid | String | dim a-123456 _ | 关联维度UUID。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| isDeleted | DeleteTagEnum | NO | 是否被删除。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询时间周期使用的FML语句**

```
 show time_periods;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| businessUnitUuid | String | bu-123456 | 所属的业务板块。 |
| businessUnitCode | String | test bu _ | 业务板块CODE。 |
| type | TimePeriodTypeEnum | DAY | 时间周期类型。 |
| typeName | String | 天 | 时间周期类型名称。 |
| code | String | 1d | 英文缩写。 |
| name | String | 1天 | 中文名称。 |
| extendName | String | 1d | 英文名称。 |
| description | String | 时间周期描述 | 描述。 |
| isDeleted | DeleteTagEnum | NO | 是否被删除。 |
| timeBegin | String | start expression _ | 开始时间表达式。 |
| timeEnd | String | end expression _ | 结束时间表达式。 |
| gmtCreate | TimeStamp | 1633885261000 | 创建时间。 |
| gmtModified | TimeStamp | 1633885261000 | 修改时间。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |
| ownerId | String | 0123456 | 负责人BaseId。 |
| ownerName | String | 甲乙丙丁 | 负责人名称。 |
| beginOffset | Integer | 1 | 开始周期偏移量。 |
| endOffset | Integer | 1 | 结束周期偏移量。 |

DataWorks

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| firstDay | Integer | 1 | 周期第一天(必填场景： type in[WEEK, MONTH, QUARTER, YEAR]）,"+ "取值范围:"+ "WEEK（初始星期，周日:1, 周一:2, 周二:3, 周三:4, 周四:5, 周五:6, 周六:7）, "+ "MONTH(初始号，月初:1, 月末:99, 2 号到27号:[2~27]), "+ "QUARTER(初始月，1月到12月:[0~11]), "+ "YEAR(初始月，1月到12 月:[0~11])。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |

**查询原子指标使用的FML语句**

```
 show atomic indicators;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dataDistinct | YesOrNoEnum | YES | 数据是否需要去重。可取值如下： YES NO |
| aggFunctionType | AggFunctionEnum | SUM | 指标聚合函数类型。可取值如下： SUM COUNT AVG MAX MIN RATE RANK UNDEFINED |
| calExpression | String | price | 计算口径(code)。 |
| dataType | DataTypeNameEnum | TINYINT | 数据类型。可取值为： TINYINT、SMALLINT、 INT、BIGINT、 BINARY、FLOAT、 DOUBLE、DECIMAL、 VARCHAR、CHAR、 STRING、DATE、 DATETIME、 TIMESTAMP、 BOOLEAN、ARRAY、 MAP、STRUCT、JSON。 |

DataWorks

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dataRound | String | N | 数据精度。可取值如下： N M |
| dataUnitUuid | String | du-123456 | 指标单位UUID。 |
| dataUnitCode | String | percent | 指标单位CODE。 |
| dataUnitName | String | 分 | 指标单位名称。 |
| bizExpression | String | 支付金额汇总 | 业务口径。 |
| dataRollUpType | String | AGG FUNCTION _ | 数据上卷方式。可取值如下： AGG FUNCTION _ SUM THEN RATE _ _ RATE THEN AVG _ _ NOT SUPPORT _ |
| businessUnitUuid | String | bu-0001 | 业务板块UUID。 |
| businessUnitCode | String | project code _ | 业务板块Code。 |
| businessProcessUuid | String | di-0002 | 业务过程UUID。 |
| businessProcessCode | String | pay | 业务过程Code。 |
| businessProcessName | String | 支付 | 业务过程Name。 |
| dataDomainUuid | String | di-0003 | 数据域UUID。 |
| dataDomainCode | String | trd | 数据域Code。 |
| dataDomainName | String | 交易 | 数据域Name。 |
| categoryUuid | String | di-0001 | 业务分类UUID。 |
| categoryCode | String | tb | 业务分类Code。 |
| categoryName | String | 淘宝 | 业务分类Name。 |
| type | String | ATOMIC | 指标类型。可取值如下： ATOMIC DERIVATIVE DERIVATIVE COMPOSI _ TE |
| code | String | pay amt _ | 英文缩写。 |
| name | String | 支付金额 | 中文名称。 |
| extendName | String | pay amount | 英文名称。 |
| description | String | remark | 描述。 |

DataWorks

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| status | String | NORMAL | 指标状态。可取值如下： DRAFT DEV NORMAL |
| ownerId | String | 0001 | 负责人BaseId。 |
| ownerName | String | 负责人姓名 | 负责人名称。 |
| isDeleted | DeleteTagEnum | NO | 是否被删除。可取值如下： YES NO |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询派生指标使用的FML语句**

```
 show derivative indicators;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| timePeriodUuid | String | tp-0001 | 时间周期UUID。 |
| timePeriodCode | String | 1d | 时间周期英文缩写。 |
| timePeriodName | String | 近1天 | 时间周期中文名称。 |
| adjunctUuids | List | ["adj-001"] | 修饰词UUID列表。 |
| adjunctCodes | List | ["male"] | 修饰词英缩写列表。 |
| adjunctNames | List | 男性 | 修饰词中文名称列表。 |
| atomicIndicatorUuid | String | ind-a-0001 | 原子指标UUID。 |
| atomicIndicatorCode | String | pay amt _ | 原子指标英文缩写。 |
| atomicIndicatorName | String | 支付金额 | 原子指标中文名称。 |

DataWorks

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| dataType | DataTypeNameEnum | BIGINT | 数据类型。可取值为： TINYINT、SMALLINT、 INT、BIGINT、 BINARY、FLOAT、 DOUBLE、DECIMAL、 VARCHAR、CHAR、 STRING、DATE、 DATETIME、 TIMESTAMP、 BOOLEAN、ARRAY、 MAP、STRUCT、JSON。 |
| bizEntityUuid | String | dim-123456 | 业务对象UUID。 |
| bizEntityCode | String | dim shop _ | 业务对象英文缩写。 |
| bizEntityName | String | 店铺表 | 业务对象中文名称。 |
| relUuid | String | dim a-123456 _ | 关联维度UUID。 |
| indHash | String | hash-0001 | 指标hash。 |
| suggestCode | String | pay amt 1d _ _ | 推荐编码。 |
| businessUnitUuid | String | bu-0001 | 业务板块UUID。 |
| businessUnitCode | String | project code _ | 业务板块Code。 |
| businessProcessUuid | String | di-0002 | 业务过程UUID。 |
| businessProcessCode | String | pay | 业务过程Code。 |
| businessProcessName | String | 支付 | 业务过程Name。 |
| dataDomainUuid | String | di-0003 | 数据域UUID。 |
| dataDomainCode | String | trd | 数据域Code。 |
| dataDomainName | String | 交易 | 数据域Name。 |
| categoryUuid | String | di-0001 | 业务分类UUID。 |
| categoryCode | String | tb | 业务分类Code。 |
| categoryName | String | 淘宝 | 业务分类Name。 |
| type | IndicatorTypeEnum | ATOMIC | 指标类型。可取值如下： ATOMIC DERIVATIVE DERIVATIVE COMPOSI _ TE |
| code | String | pay amt _ | 英文缩写。 |
| name | String | 支付金额 | 中文名称。 |
| extendName | String | pay amount | 英文名称。 |

|  | 开发指南·OpenAPI参考 |  |  | DataWork | s |
|---|---|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| description | String | remark | 描述。 |
| status | IndicatorStatusEnum | NORMAL | 指标状态。可取值如下： DRAFT DEV NORMAL |
| ownerId | String | 0001 | 负责人BaseId。 |
| ownerName | String | 负责人姓名 | 负责人名称。 |
| isDeleted | DeleteTagEnum | NO | 是否被删除。可取值如下： YES NO |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 修改时间。 |
| creatorId | String | 0123456 | 创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 创建人名称。 |
| modifierId | String | 0123456 | 修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 修改人名称。 |

**查询复合指标使用的FML语句**

```
 show derivative composite indicators;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| businessUnitCode | String | project code _ | 工作空间名称。 |
| businessProcessUuid | String | di-0002 | 业务过程UUID。 |
| businessProcessCode | String | pay | 业务过程Code。 |
| businessProcessName | String | 支付 | 业务过程名称。 |
| dataDomainUuid | String | di-0003 | 数据域UUID。 |
| dataDomainCode | String | trd | 数据域Code。 |
| dataDomainName | String | 交易 | 数据域名称。 |
| categoryUuid | String | di-0001 | 业务分类UUID。 |
| categoryCode | String | tb | 业务分类Code。 |
| categoryName | String | 淘宝 | 业务分类名称。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| type | String | DERIVATIVE COMPOSI _ TE | 计算模式。可取值 DERIVATIVE COMPOSI _ TE （计算表达式）、 DERIVATIVE COMPARI _ SON（同环比）。 |
| code | String | pay amt _ | 指标英文缩写。 |
| name | String | 支付金额 | 指标中文名称。 |
| extendName | String | pay amount | 指标英文名称。 |
| description | String | remark | 指标描述信息。 |
| calculateExpression | String | {@pay amt 1d[近1天 _ _ _ 支付金额]}/{@pay amt 1m[ _ _ 近30天支付金额]} _ | 计算表达式。 |
| comparisonPeriodType | String | DAY MOM _ | 同环比对比类型。取值如下： DAY MOM（日环 _ 比）、 WEEK MOM（周 _ 环比）、WEEK YOY（周 _ 同比）、 MONTH MOM（月环 _ 比）、MONTH YOY（月 _ 同比）、 QUARTER MOM（季度 _ 环比）、 YEAR MOM（年环 _ 比）、YEAR YOY（年同 _ 比）。 |
| comparisonIndicatorU uid | String | obj-123456 | 同环比对比指标的UUID。 |
| comparisonIndicatorCo de | String | pay amt 1d _ _ | 同环比对比指标的英文缩写。 |
| comparisonIndicatorN ame | String | 近1天支付金额 _ | 同环比对比指标的中文名称。 |
| ownerId | String | 0001 | 指标负责人的BaseId。 |
| ownerName | String | 张三 | 指标负责人的姓名。 |
| isDeleted | DeleteTagEnum | NO | 是否被删除，可取值YES 或NO。 |
| uuid | String | obj-123456 | 对象唯一标识。 |
| gmtCreate | TimeStamp | 1644397025000 | 指标创建时间。 |
| gmtModified | TimeStamp | 1644459965000 | 指标修改时间。 |
| creatorId | String | 0123456 | 指标创建人BaseId。 |
| creatorName | String | 甲乙丙丁 | 指标创建人名称。 |

|  | 开发指南·OpenAPI参考 |  |  | DataWork | s |
|---|---|---|---|---|---|

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| modifierId | String | 0123456 | 指标修改人BaseId。 |
| modifierName | String | 甲乙丙丁 | 指标修改人名称。 |

**查询单个指标所依赖模型的相关信息，使用的FML语句**

```
 show statistic indicator table_code;
```

输出参数

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| uuid | String | obj-123456 | 指标唯一标识。 |
| code | String | pay amt _ | 指标英文缩写。 |
| name | String | 支付金额 | 指标中文名称。 |
| extendName | String | pay amount | 指标英文名称。 |
| relations | List | 示例请参见下文 | 依赖指标的模型信息列表，EntityInfo的结构参见下文。 |

EntityInfo的结构示例及参数描述： [

```json
    {
        "uuid": "uuid",
        "code": "code",
```

`"name": "`中文名称`",`

```json
        "extendName": "full name in English",
        "entityType": "EntityTypeEnum.BASE_DERIVATIVE_INDICATOR",
```

`"entityTypeName": "`实体类型名称`",`

```json
        "entitySubType": "DERIVATIVE_INDICATOR",
```

`"entitySubTypeName": "`实体子类型名称`",`

```json
        "ownerId": "0001",
```

`"ownerName": "`负责人姓名"

```
    }
```

]

| 参数名 | 参数类型 | 示例值 | 描述信息 |
|---|---|---|---|
| uuid | String | obj-123456 | 模型唯一标识。 |
| code | String | dws 001 _ | 模型英文缩写。 |
| name | String | 支付汇总表 | 模型中文名称。 |
| extendName | String | dws 001 _ | 模型英文名称。 |

DataWorks

| 参数名 |  |  | 参数类型 |  |  |  | 示例值 |  |  | 描述信息 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| entityType |  |  | EntityTypeEnum |  |  |  | Table |  |  | 依赖指标的实体类型。取值包括但不限于 TABLE、 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | TABLE、 |  |  |
|  |  |  |  |  |  |  |  |  |  | BASE ATOMIC INDICATO _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | R、 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | BASE DERIVATIVE INDI _ _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  | CATOR |  |  |  |
| entityTypeName |  |  | String |  |  |  | 表 |  |  | 实体类型名称。 |  |  |  |
| entitySubType |  |  | String |  |  |  | DWS TABLE |  |  | 实体子类型。取值包括但不限于 DWS TABLE、 _ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | DWS TABLE、 _ |  |
|  |  |  |  |  |  |  |  |  |  | ATOMIC INDICATOR、 _ |  |  |  |
|  |  |  |  |  |  |  | _ |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | DERIVATIVE INDICATOR _ |  |  |  |
| entitySubTypeName |  |  | String |  |  |  | 汇总表 |  |  | 实体子类型名称。 |  |  |  |
| ownerId |  |  | String |  |  |  | 0001 |  |  | 负责人BaseId。 |  |  |  |
| ownerName |  |  | String |  |  |  | 张三 |  |  | 负责人名称。 |  |  |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=QueryPublicModelEngine &Text=show dim tables &ProjectId=1234
```

&公共请求参数
### 请求示例补充说明
`//javasdk`调用的`Demo`示例如下：

```
 QueryPublicModelEngineRequest request = new QueryPublicModelEngineRequest();
 request.setProjectId(this.projectId);
 request.setText("show layers;");
 QueryPublicModelEngineResponse response = client.getAcsResponse(request);
```

`//`以下仅用于演示如何输出`JSON`数据，实际使用时请根据需求处理返回数据。

```java
 ObjectMapper objectMapper = new ObjectMapper();
 objectMapper.enable(SerializationFeature.INDENT_OUTPUT);
 objectMapper.setTimeZone(TimeZone.getTimeZone("GMT+8"));
 String s = objectMapper.writeValueAsString(obj);
 System.out.println(s);
```

正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"4CFB2DED-7D9B-4C42-B4AA-CFF4991D****",
 "ReturnValue":""
}
```

`XML` 格式

```xml
<RequestId>4CFB2DED-7D9B-4C42-B4AA-CFF4991D****</RequestId> <ReturnValue />
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ME 000 B 0001 _ _ _ | Valid.FML.NoPermission | You are not authorized to access the project resources. |
| 400 | ME 003 P 006 _ _ _ | Valid.FML.OnlySupportQuerySt atement | Only FML query statement is supported. |
| 400 | ME 001 P 0046 _ _ _ | Valid.FML.ProjectNotExist | The project does not exist. |
| 400 | ME 003 P 004 _ _ _ | Valid.FML.StatementNotValid | The FML statement is invalid. |
| 400 | ME 000 B 0021 _ _ _ | Valid.FML.ProductExpired | 智能数据建模产品购买已到期 |
| 400 | ME 000 B 0020 _ _ _ | Valid.FML.ProductNotActivated | 智能数据建模产品未开通 |
| 500 | ME 003 S 001 _ _ _ | Execute.FML.ProcessError | Failed to execute FML statement. |

**文档补充说明**

**返回示例补充说明**

DataWorks `// JAVA SDK`调用的`Demo`示例返回结果如下

```json
 {
  "requestId" : "x-request-id",
  "returnValue" : [ {
    "uuid" : "obj-123456",
    "gmtCreate" : 1638857552348,
    "gmtModified" : 1638857552351,
    "creatorId" : "0123456",
```

`"creatorName" : "`甲乙丙丁`",`

```json
    "modifierId" : "0123456",
```

`"modifierName" : "`甲乙丙丁`",`

```json
    "code" : "dws",
    "englishName" : "dws",
```

`"name" : "`汇总层`",`

```json
    "ownerId" : "0123456",
```

`"ownerName" : "`甲乙丙丁`",` `"description" : "`汇总层描述"

```
  } ]
}
```

#### SearchElement

调用SearchElement接口，使用名称和中文名查询对象。默认为表和字段，仅搜索模型的master分支。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| TagIds | Strin g | Body | 否 | [12,34] | 标签ID列表。 |
| TypeIds | Strin g | Body | 否 | [80000004,80000005] | 搜索类型ID列表，默认是表和字段。 |
| PageSize | Long | Body | 是 | 10 | 当前数据页的数据条数。 |
| Keyword | Strin g | Body | 是 | my | 搜索关键字。 |
| CurrentPa ge | Long | Body | 是 | 1 | 当前数据页面，0为第一页。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RequestT oken | Strin g | Body | 否 | SESSION=fca548fa- a495-459d-9210- d39d2637c9e9 | 请求token。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  | 返回数据。 |
| -Data | Long |  | 返回数据信息。 |
| -Alias | String | 表4 | 别名。 |
| -CombinedId | String | 11/4 | 绑定ID。 |
| -DomainId | String | 1ccaf409f3644665 9341d3b5a144a7b 5 | 数据标准ID。 |
| -ElementId | Long | 4 | 元素ID。 |
| -EndVersion | Long | 6 | 元素结束版本。 |
| -Id | Long | 78 | 自增ID。 |
| -ModelId | Long | 12 | 模型ID。 |
| -ModelName | String | test map _ | 模型名称名称。 |
| -ModelType | String | MySQL | 模型类型。 |
| -Name | String | Table 4 _ | 元素名称。 |
| -ParentId | Long | 2 | 父对象ID。 |
| -Path | String | Model Repository/ 机构管理/test map _ | 元素路径。 |
| -RefCode | String | 78es | 关联编码。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ResultType | String | Simple | 结果类型，固定返回Simple。 |
| -StartVersion | Long | 3 | 元素起始版本。 |
| -TenantId | Long | 10000 | 租户ID。 |
| -TypeId | Long | 80000005 | 类型ID。 |
| -UseProto | Boolean | true | 是否使用Proto保存模型。 |
| RequestId | String | C404EE27-8DCE- 4602-B9D1- ECA3BDC8D4D1 | 调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| ErrorData | Struct |  | 报错信息。 |
| -ErrorCode | Long | 1000001 | 错误码。 |
| -ErrorType | String |  | 错误类型。 |
| -ErrorMessage | String | The connection does not exist. | 错误信息。 |
| - RootErrorType | String |  | 根错误码。 |
| - RootErrorMess age | String | You have no permission | 根错误信息。 |

**示例**

请求示例

```
&RegionId=default &PageSize=10 &Keyword=my &CurrentPage=1
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"C404EE27-8DCE-4602-B9D1-ECA3BDC8D4D1",
 "Data":{
  "ParentId":2,
  "Path":"Model Repository/机构管理/test_map",
  "TypeId":80000005,
  "ModelName":"test_map",
  "UseProto":true,
  "Data":"",
  "StartVersion":3,
  "EndVersion":6,
  "ResultType":"Simple",
  "Name":"Table_4",
  "CombinedId":"11/4",
  "TenantId":10000,
  "DomainId":"1ccaf409f36446659341d3b5a144a7b5",
  "RefCode":"78es",
  "Alias":"表4",
  "ModelType":"MySQL",
  "Id":78,
  "ElementId":4,
  "ModelId":12
 },
 "ErrorData":{
  "ErrorType":"",
  "RootErrorType":"",
  "RootErrorMessage":"You have no permission",
  "ErrorCode":1000001,
  "ErrorMessage":"The connection does not exist."
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>C404EE27-8DCE-4602-B9D1-ECA3BDC8D4D1</RequestId> <Data>
 <ParentId>2</ParentId>
 <Path>Model Repository/机构管理/test_map</Path>
 <TypeId>80000005</TypeId>
 <ModelName>test_map</ModelName>
 <UseProto>true</UseProto>
 <Data  />
 <StartVersion>3</StartVersion>
 <EndVersion>6</EndVersion>
 <ResultType>Simple</ResultType>
 <Name>Table_4</Name>
 <CombinedId>11/4</CombinedId>
 <TenantId>10000</TenantId>
 <DomainId>1ccaf409f36446659341d3b5a144a7b5</DomainId>
 <RefCode>78es</RefCode>
 <Alias>表4</Alias>
 <ModelType>MySQL</ModelType>
 <Id>78</Id>
 <ElementId>4</ElementId>
 <ModelId>12</ModelId>
</Data> <ErrorData>
 <ErrorType  />
 <RootErrorType  />
 <RootErrorMessage>You have no permission</RootErrorMessage>
 <ErrorCode>1000001</ErrorCode>
 <ErrorMessage>The connection does not exist.</ErrorMessage>
</ErrorData>
```

#### UpdateModel

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| ModelId | Long | Body | 是 | 111 | 模型ID。 |
| CategoryI d | Long | Body | 是 | 3 | 目录ID。 |
| Descriptio n | Strin g | Body | 否 | 这是模型的描述 | 模型描述。 |

| 开发指南·Open | API参考 |  |  |  | DataWork |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | model 1 _ | 模型名称。 |
| Owner | Strin g | Body | 否 | admin | 模型所有者。 |
| Phase | Long | Body | 是 | 1 | 模型阶段。 |
| TenantId | Long | Body | 否 | 10000 | 租户ID。 |
| RequestT oken | Strin g | Body | 否 | SESSION=fca548fa- a495-459d-9210- d39d2637c9e9 | 请求token。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CategoryId | Long | 3 | 目录ID。 |
| CreatedOn | Long | 1704333985383 | 模型创建时间。 |
| CurrentVersio n | Long | 2 | 模型当前版本。 |
| Deleted | Boolean | false | 模型是否被删除。 |
| DepartmentId | Long | 2 | 部门ID。 |
| Description | String | 这是个xx模型 | 模型描述。 |
| Frozen | Boolean | false | 模型是否被冻结。 |
| Id | Long | 1112 | 自增ID。 |
| LastModificati onTimestamp | String | 1704333985383 | 模型上次修改时间。 |
| LastModifier | String | admin | 模型上次修改账号。 |
| LockTimestam p | Long | 1704333985383 | 模型锁定时间。 |
| Locked | Boolean | false | 加锁状态。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Locker | String | admin | 模型锁定账号。 |
| ModelType | String | MySQL | 模型类型。 |
| Name | String | model 1 _ | 模型名称。 |
| ObjCount | Long | 10 | 对象数。 |
| Owner | String | admin | 模型所有者。 |
| Phase | Integer | 1 | 模型阶段。 |
| ReferredModel Id | Long | 1122 | 关联模型ID。 |
| Seed | Integer | 10 | 模型种子。 |
| UseProto | Boolean | false | 模型是否压缩。 |
| RequestId | String | C404EE27-8DCE- 4602-B9D1- ECA3BDC8D4D1 | 请求ID。 |
| RequestId | String | C404EE27-8DCE- 4602-B9D1- ECA3BDC8D4D1 | 请求ID。 |
| ErrorData | Struct |  | 错误信息。 |
| -ErrorCode | Long | 10001 | 错误码。 |
| -ErrorType | String |  | 错误类型。 |
| -ErrorMessage | String | The connection does not exist. | 错误消息。 |
| - RootErrorType | String |  | 根错误码。 |
| - RootErrorMess age | String | You have no permission | 根错误信息。 |

**示例**

DataWorks 请求示例

```
&RegionId=default &ModelId=111 &CategoryId=3 &Name=model_1 &Phase=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "CategoryId":3,
 "LockTimestamp":1704333985383,
 "LastModifier":"admin",
 "Owner":"admin",
```

`"Description":"`这是个`xx`模型`",`

```json
 "Locker":"admin",
 "Phase":1,
 "RequestId":"C404EE27-8DCE-4602-B9D1-ECA3BDC8D4D1",
 "CurrentVersion":2,
 "UseProto":false,
 "Frozen":false,
 "Name":"model_1",
 "LastModificationTimestamp":"1704333985383",
 "Locked":false,
 "Seed":10,
 "ModelType":"MySQL",
 "CreatedOn":1704333985383,
 "Deleted":false,
 "DepartmentId":2,
 "Id":1112,
 "ReferredModelId":1122,
 "ObjCount":10,
 "ErrorData":{
  "ErrorType":"",
  "RootErrorType":"",
  "RootErrorMessage":"You have no permission",
  "ErrorCode":10001,
  "ErrorMessage":"The connection does not exist."
 }
}
```

`XML` 格式 DataWorks

```xml
<CategoryId>3</CategoryId> <LockTimestamp>1704333985383</LockTimestamp> <LastModifier>admin</LastModifier> <Owner>admin</Owner> <Description>这是个xx模型</Description> <Locker>admin</Locker> <Phase>1</Phase> <RequestId>C404EE27-8DCE-4602-B9D1-ECA3BDC8D4D1</RequestId> <CurrentVersion>2</CurrentVersion> <UseProto>false</UseProto> <Frozen>false</Frozen> <Name>model_1</Name> <LastModificationTimestamp>1704333985383</LastModificationTimestamp> <Locked>false</Locked> <Seed>10</Seed> <ModelType>MySQL</ModelType> <CreatedOn>1704333985383</CreatedOn> <Deleted>false</Deleted> <DepartmentId>2</DepartmentId> <Id>1112</Id> <ReferredModelId>1122</ReferredModelId> <ObjCount>10</ObjCount> <ErrorData>
 <ErrorType  />
 <RootErrorType  />
 <RootErrorMessage>You have no permission</RootErrorMessage>
 <ErrorCode>10001</ErrorCode>
 <ErrorMessage>The connection does not exist.</ErrorMessage>
</ErrorData>
```

#### UpdatePublicDomain

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Content | Strin g | Body | 否 | {"code":"aaa","enName" :"","name":"","values": [{"name":"","value":"","e nName":"","definition":"" ,"order":""}]} | 请求文本。 |
| Base64Co ntent | Strin g | Body | 否 | eyJjb2RlIjoiYWFhIiwiZW5 OYW1lIjoiIiwibmFtZSI6IiI sInZhbHVlcyI6W3sibmFt ZSI6IiIsInZhbHVlIjoiIiwiZ W5OYW1lIjoiIiwiZGVma W5pdGlvbiI6IiIsIm9yZGV yIjoiIn1dfQ | 文本的Base64编码。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Integ er | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Boolean | false | 返回数据。 |
| RequestId | String | 6ccb9f57-0b72- 4b00-be28- e989cfd2c903 | 请求ID。用于定位日志，排查问题。 |
| ErrorData | Struct |  | 返回的报错数据。 |
| -ErrorCode | Long | 1 | 错误码。 |
| -ErrorType | String | user | 错误类型。 |
| -ErrorMessage | String | The connection does not exist | 错误信息。 |
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主程序报错类型。 |
| - RootErrorMess age | String | The project does not exist | 主程序报错信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePublicDomain
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"12345678",
 "Data":"",
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

`XML` 格式

```xml
<RequestId>12345678</RequestId> <Data /> <ErrorData>
 <ErrorType>user</ErrorType>
 <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType>
 <RootErrorMessage>The project does not exist</RootErrorMessage>
 <ErrorCode>1</ErrorCode>
 <ErrorMessage>The connection does not exist</ErrorMessage>
</ErrorData>
```

#### UpdateDomainCode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Content | Strin g | Body | 否 | { "id": "d278db54d1e841cca02 3e9cb5f4b5b08", "chName": "英语", "enName": "English", "abbrivation": "english", "path": ["测试"], "description": "这是业务定义", "domainCode": "ad001", "timestamp": 1710839677938, "version": 1, "dataType": "string", "notNull": true, "dataScale": "3", "dataPrecision": 1, "udps": [], "submitter": "11877909784501696", "pathString": "测试" } | 请求文本。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Base64Co ntent | Strin g | Body | 否 | eyJjb2RlIjoiYWFhIiwiZW5 OYW1lIjoiIiwibmFtZSI6IiI sInZhbHVlcyI6W3sibmFt ZSI6IiIsInZhbHVlIjoiIiwiZ W5OYW1lIjoiIiwiZGVma W5pdGlvbiI6IiIsIm9yZGV yIjoiIn1dfQ | 文本的Base64编码。 |
| ProjectId | Integ er | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Boolean | true | 返回数据。 |
| RequestId | String | 6ccb9f57-0b72- 4b00-be28- e989cfd2c903 | 请求ID。用于定位日志，排查问题。 |
| ErrorData | Struct |  | 返回的报错数据。 |
| -ErrorCode | Long | 1 | 错误码。 |
| -ErrorType | String | user | 错误类型。 |
| -ErrorMessage | String | The connection does not exist | 错误信息。 |
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主程序的错误类型。 |
| - RootErrorMess age | String | The project does not exist | 主程序的错误信息。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"6ccb9f57-0b72-4b00-be28-e989cfd2c903",
 "Data":true,
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

`XML` 格式

```xml
<RequestId>6ccb9f57-0b72-4b00-be28-e989cfd2c903</RequestId> <Data>true</Data> <ErrorData>
 <ErrorType>user</ErrorType>
 <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType>
 <RootErrorMessage>The project does not exist</RootErrorMessage>
 <ErrorCode>1</ErrorCode>
 <ErrorMessage>The connection does not exist</ErrorMessage>
</ErrorData>
```

#### GetModelApplyDomainStatus

调用GetModelApplyDomainStatus接口，获取模型所使用数据标准的相关信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ModelId | Long | Body | 是 | 10 | 模型ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array | { "P":true, "EId":2, "DRefC":"ad001 ", "MId":10, "TN":"student", "CN":"age", "DEn":"English", "DSub":"测试", "TA":"学生表", "CA":"性别", "DCn":"英语", "DId":"d278db54d1 e841cca023e9cb5f 4b5b08" } | 模型的相关数据。 |
| -MId | Long | 10 | Model ID的缩写，模型ID。 |
| -EId | Long | 2 | Element ID的缩写，元素ID。 |
| -CN | String | age | Column Name的缩写，字段名称。 |
| -CA | String | 性别 | Column Alias的缩写，字段别名。 |
| -TN | String | student | Table Name的缩写，表名称。 |
| -TA | String | 学生表 | Table Alias的缩写，表别名。 |
| -DEn | String | English | Domain en Name的缩写，数据标准的英文名称。 |
| -DCn | String | 英语 | Domain ch Name的缩写，数据标准的中文名称。 |
| -DSub | String | 测试 | Domain Subject的缩写，标准分类。 |
| -DId | String | d278db54d1e841c ca023e9cb5f4b5b0 8 | Domain ID的缩写，标准ID。 |
| -DRefC | String | ad001 | Domain Ref Code的缩写，引用代码。 |
| -P | Boolean | true | Is Public Domain的缩写，是否是公共标准。 |
| ErrorData | Struct |  | 返回的报错数据。 |
| -ErrorCode | Long | 1 | 错误码。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| -ErrorType | String | user | 错误类型。 |
|---|---|---|---|
| -ErrorMessage | String | The connection does not exist | 错误信息。 |
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主程序的错误类型。 |
| - RootErrorMess age | String | The project does not exist | 主程序的错误信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetModelApplyDomainStatus &ModelId=10
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Data":{
  "P":true,
  "EId":2,
  "DRefC":"ad001",
  "MId":10,
  "TN":"student",
  "CN":"age",
  "DEn":"English",
```

`"DSub":"`测试`",` `"TA":"`学生表`",` `"CA":"`性别`",` `"DCn":"`英语`",`

```json
  "DId":"d278db54d1e841cca023e9cb5f4b5b08"
 },
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

`XML` 格式 DataWorks

|  | <Data> <P>true</P> <EId>2</EId> <DRefC>ad001 </DRefC> <MId>10</MId> <TN>student</TN> <CN>age</CN> <DEn>English</DEn> <DSub>测试</DSub> <TA>学生表</TA> <CA>性别</CA> <DCn>英语</DCn> <DId>d278db54d1e841cca023e9cb5f4b5b08</DId> </Data> <ErrorData> <ErrorType>user</ErrorType> <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType> <RootErrorMessage>The project does not exist</RootErrorMessage> <ErrorCode>1</ErrorCode> <ErrorMessage>The connection does not exist</ErrorMessage> </ErrorData> |
|---|---|

#### DeleteDomainCodes

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Body | 否 | 100001 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |
| Content | Strin g | Body | 否 | ["del001“] | 待删除的标准代码的 CODE。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Boolean | false | 请求是否成功。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6ccb9f57-0b72- 4b00-be28- e989cfd2c903 | 请求ID。用于定位日志，排查问题。 |
| ErrorData | Struct | { "ErrorType":"user", "RootErrorType":"I nvalid.Tenant.Proje ctNotExists", "RootErrorMessage ":"The project does not exist", "ErrorCode":1, "ErrorMessage":"Th e connection does not exist" } | 返回的错误数据。 |
| -ErrorCode | Long | 1 | 错误码。 |
| -ErrorType | String | user | 错误类型。 |
| -ErrorMessage | String | The connection does not exist | 错误信息。 |
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主接口错误类型。 |
| - RootErrorMess age | String | The project does not exist | 主接口错误信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePublicDomains
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"6ccb9f57-0b72-4b00-be28-e989cfd2c903",
 "Data":false,
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

DataWorks `XML` 格式

```xml
<RequestId>6ccb9f57-0b72-4b00-be28-e989cfd2c903</RequestId> <Data>false</Data> <ErrorData>
 <ErrorType>user</ErrorType>
 <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType>
 <RootErrorMessage>The project does not exist</RootErrorMessage>
 <ErrorCode>1</ErrorCode>
 <ErrorMessage>The connection does not exist</ErrorMessage>
</ErrorData>
```

#### CreatePublicDomain

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Content | Strin g | Body | 否 | { "path": ["测试"], "domainCode": "ad001", "enName": "English", "abbrivation": "english", "chName": "英语", "description": "这是业务定义", "dataType": "string", "dataScale": "2", "notNull": true, "udps": [], "dataPrecision": "1" } | 请求文本。 |
| Base64Co ntent | Strin g | Body | 否 | ewoJInBhdGgiOiBbIua1i +ivlSJdLAoJImRvbWFpbk NvZGUiOiAiYWQwMDEiL AoJImVuTmFtZSI6ICJFbm dsaXNoIiwKCSJhYmJyaX ZhdGlvbiI6ICJlbmdsaXNo IiwKCSJjaE5hbWUiOiAi6I ux6K+tIiwKCSJkZXNjcml wdGlvbiI6ICLov5nmmK/k uJrliqHlrprkuYkiLAoJImRh dGFUeXBlIjogInN0cmluZ yIsCgkiZGF0YVNjYWxlIjo gIjIiLAoJIm5vdE51bGwiOi B0cnVlLAoJInVkcHMiOiB bXSwKCSJkYXRhUHJlY2lz aW9uIjogIjEiCn0= | 请求文本的base64编码。 |
| ProjectId | Integ er | Body | 否 | 10006 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |

DataWorks

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6ccb9f57-0b72- 4b00-be28- e989cfd2c903 | 请求ID。用于定位日志，排查问题。 |
| Data | Struct | { "Path":"[\"测试 \"]", "Category":"1", "Description":"这是业务定义", "Abbrivation":"engl ish", "DataPrecision":1, "NotNull":true, "Timestamp":1710 839677938, "ChineseName":"英语", "Submitter":"1187 7909784501696", "DomainCode":"ad 001", "Version":1, "DataScale":2, "DataType":"string ", "Id":"d278db54d1e 841cca023e9cb5f4 b5b08", "ReferenceCode":" 100", "AdditionalProperti es":"[]", "EnglishName":"En glish" } | 返回数据。 |
| - AdditionalProp erties | String | [{ "propertyId": 1001, "name": "名字", "category": "STANDARD", "order": 1 }] | 自定义属性。 |
| -Path | String | ["测试"] | 多级分类。 |
| -Id | String | d278db54d1e841c ca023e9cb5f4b5b0 8 | 数据标准的编号。 |
| -Category | String | 1 | 数据标准的分类。 |
| -ChineseName | String | 英语 | 数据标准的中文名称。 |
| -EnglishName | String | English | 数据标准的英文名称。 |
| -Description | String | 这是业务定义 | 业务定义。 |

|  | 开发指南·OpenAPI参 | 考 |  | DataWork | s |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DataType | String | string | 数据类型。 |
| -DataScale | Integer | 2 | 数据长度。 |
| -Abbrivation | String | english | 数据标准的英文缩写。 |
| -DataPrecision | Integer | 1 | 数据精度。 |
| -NotNull | Boolean | true | 该参数可以为空。 |
| - ReferenceCod e | String | 100 | 引用代码。 |
| -Timestamp | Long | 1710839677938 | 创建数据标准的时间戳。 |
| -DomainCode | String | ad001 | 数据标准的标准ID。 |
| -Version | Integer | 1 | 数据标准的版本。 |
| -Submitter | String | 118779097845016 96 | 提交用户。 |
| ErrorData | Struct |  | 返回的错误数据。 |
| -ErrorCode | Long | 1 | 错误码。 |
| -ErrorType | String | user | 错误类型。 |
| -ErrorMessage | String | The connection does not exist | 错误信息。 |
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主接口的错误类型。 |
| - RootErrorMess age | String | The project does not exist | 主接口的错误信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreatePublicDomain
```

&公共请求参数 DataWorks 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"6ccb9f57-0b72-4b00-be28-e989cfd2c903",
 "Data":{
  "Path":"[\"测试\"]",
  "Category":"1",
```

`"Description":"`这是业务定义`",`

```json
  "Abbrivation":"english",
  "DataPrecision":1,
  "NotNull":true,
  "Timestamp":1710839677938,
  "ChineseName":"英语",
  "Submitter":"11877909784501696",
  "DomainCode":"ad001",
  "Version":1,
  "DataScale":2,
  "DataType":"string",
  "Id":"d278db54d1e841cca023e9cb5f4b5b08",
  "ReferenceCode":"100",
  "AdditionalProperties":"[{\t\"propertyId\": 1001,\t\"name\": \"名字\",\t\"category\":
\"STANDARD\",\t\"order\": 1}]",
  "EnglishName":"English"
 },
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>6ccb9f57-0b72-4b00-be28-e989cfd2c903</RequestId> <Data>
 <Path>[&quot;测试&quot;]</Path>
 <Category>1</Category>
```

`<Description>`这是业务定义`</Description>`

```xml
 <Abbrivation>english</Abbrivation>
 <DataPrecision>1</DataPrecision>
 <NotNull>true</NotNull>
 <Timestamp>1710839677938</Timestamp>
 <ChineseName>英语</ChineseName>
 <Submitter>11877909784501696</Submitter>
 <DomainCode>ad001</DomainCode>
 <Version>1</Version>
 <DataScale>2</DataScale>
 <DataType>string</DataType>
 <Id>d278db54d1e841cca023e9cb5f4b5b08</Id>
 <ReferenceCode>100</ReferenceCode>
 <AdditionalProperties>[{
 &quot;propertyId&quot;: 1001,
 &quot;name&quot;: &quot;名字&quot;,
 &quot;category&quot;: &quot;STANDARD&quot;,
 &quot;order&quot;: 1
}]</AdditionalProperties>
  <EnglishName>English</EnglishName>
 </Data>
 <ErrorData>
  <ErrorType>user</ErrorType>
  <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType>
  <RootErrorMessage>The project does not exist</RootErrorMessage>
  <ErrorCode>1</ErrorCode>
  <ErrorMessage>The connection does not exist</ErrorMessage>
 </ErrorData>
```

#### AddDomainCode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Content | Strin g | Body | 否 | { "code": "col001", "enName": "colours", "name": "颜色", "values": [{ "name": "红色", "value": "c1", "enName": "red", "definition": "就是红色的含义", "order": 0 }, { "name": "黑色", "value": "c2", "enName": "black", "definition": "就是黑色的含义", "order": 1 }], "datasetName": "主题" } | 添加一个标准代码CODE。 |
| Base64Co ntent | Strin g | Body | 否 | eyJjb2RlIjoiYWFhIiwiZW5 OYW1lIjoiIiwibmFtZSI6IiI sInZhbHVlcyI6W3sibmFt ZSI6IiIsInZhbHVlIjoiIiwiZ W5OYW1lIjoiIiwiZGVma W5pdGlvbiI6IiIsIm9yZGV yIjoiIn1dfQ== | 请求文本的base64编码。 |
| ProjectId | Integ er | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6ccb9f57-0b72- 4b00-be28- e989cfd2c903 | 请求ID。用于定位日志，排查问题。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Struct | { "tenantId": 200, "id": 2, "code": "col001", "name": "颜色", "enName": "colours", "datasetName": "主题", "submitter": "11877909784501 696", "lastModification": 1710777600000, "values": [ { "name": "红色", "enName": "red", "value": "c1", "definition": "就是红色的含义", "order": 0 }, { "name": "黑色", "enName": "black", "value": "c2", "definition": "就是黑色的含义", "order": 1 } ], "typeId": 80010098 } | 返回的标准代码信息。 |
| -Values | Array | [ { "name": "红色", "enName": "red", "value": "c1", "definition": "就是红色的含义", "order": 0 }, { "name": "黑色", "enName": "black", "value": "c2", "definition": "就是黑色的含义", "order": 1 } ] | 标准代码的候选值。 |
| --Name | String | 黑色 | 中文名称。 |
| --EnName | String | black | 英文名称。 |
| --Value | String | c2 | 取值。 |
| --Definition | String | 就是黑色的含义 | 描述。 |
| --Definition2 | String | 描述 | 描述2。 |
| --Definition3 | String | 描述 | 描述3。 |
| --ParentValue | String | cc | 父值。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Order | Integer | 1 | 排序。 |
| -Id | Long | 2 | 数据ID。 |
| -Code | String | col001 | 标准代码Code。 |
| -Name | String | 颜色 | 标准代码的中文名称。 |
| -EnName | String | colours | 标准代码的英文名称。 |
| -DatasetName | String | 主题 | 主题名称。 |
| -Submitter | String | 118779097845016 96 | 提交用户。 |
| - LastModificati on | String | 1710777600000 | 最近一次修改标准代码的时间。 |
| -TenantId | Integer | 200 | 租户ID。 |
| -IsNew | Boolean | true | 是否新建。 |
| -TypeId | Integer | 80010098 | 类型ID。 |
| ErrorData | Struct | { "ErrorType":"user", "RootErrorType":"I nvalid.Tenant.Proje ctNotExists", "RootErrorMessage ":"The project does not exist", "ErrorCode":1, "ErrorMessage":"Th e connection does not exist" } | 返回的错误数据。 |
| -ErrorCode | Long | 1 | 错误码。 |
| -ErrorType | String | user | 错误类型。 |
| -ErrorMessage | String | The connection does not exist | 错误信息。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主接口的错误类型。 |
| - RootErrorMess age | String | The project does not exist | 主接口的错误信息。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"6ccb9f57-0b72-4b00-be28-e989cfd2c903",
 "Data":{
  "TypeId":80010098,
  "TenantId":200,
  "Submitter":"11877909784501696",
  "EnName":"colours",
  "DatasetName":"主题",
  "Id":2,
  "LastModification":"1710777600000",
  "IsNew":true,
  "-Values":{
   "Order":1,
   "ParentValue":"cc",
   "EnName":"black",
   "Definition3":"描述",
   "Value":"c2",
```

`"Definition":"`就是黑色的含义`",`

```json
   "Definition2":"描述",
```

`"Name":"`黑色"

```json
  },
  "Code":"col001",
```

`"Name":"`颜色"

```json
 },
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>6ccb9f57-0b72-4b00-be28-e989cfd2c903</RequestId> <Data>
 <TypeId>80010098</TypeId>
 <TenantId>200</TenantId>
 <Submitter>11877909784501696</Submitter>
 <EnName>colours</EnName>
 <DatasetName>主题</DatasetName>
 <Id>2</Id>
 <LastModification>1710777600000</LastModification>
 <IsNew>true</IsNew>
 <-Values>
  <Order>1</Order>
  <ParentValue>cc</ParentValue>
  <EnName>black</EnName>
  <Definition3>描述</Definition3>
  <Value>c2</Value>
```

`<Definition>`就是黑色的含义`</Definition>`

```xml
  <Definition2>描述</Definition2>
  <Name>黑色</Name>
 </-Values>
 <Code>col001</Code>
 <Name>颜色</Name>
</Data> <ErrorData>
 <ErrorType>user</ErrorType>
 <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType>
 <RootErrorMessage>The project does not exist</RootErrorMessage>
 <ErrorCode>1</ErrorCode>
 <ErrorMessage>The connection does not exist</ErrorMessage>
</ErrorData>
```

#### DeletePublicDomains

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Body | 否 | 10006 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |
| Content | Strin g | Body | 否 | ["d278db54d1e841cca0 23e9cb5f4b5b08"] | 要删除的数据标准ID列表。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Boolean | true | 请求是否成功。 |
| RequestId | String | 6ccb9f57-0b72- 4b00-be28- e989cfd2c903 | 请求ID。用于定位日志，排查问题。 |
| ErrorData | Struct |  | 返回的错误数据。 |
| -ErrorCode | Long | 1 | 错误码。 |
| -ErrorType | String | user | 错误类型。 |
| -ErrorMessage | String | The connection does not exist | 错误信息。 |
| - RootErrorType | String | Invalid.Tenant.Proj ectNotExists | 主接口错误类型。 |
| - RootErrorMess age | String | The project does not exist | 主接口错误信息。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePublicDomains
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"6ccb9f57-0b72-4b00-be28-e989cfd2c903",
 "Data":true,
 "ErrorData":{
  "ErrorType":"user",
  "RootErrorType":"Invalid.Tenant.ProjectNotExists",
  "RootErrorMessage":"The project does not exist",
  "ErrorCode":1,
  "ErrorMessage":"The connection does not exist"
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>6ccb9f57-0b72-4b00-be28-e989cfd2c903</RequestId> <Data>true</Data> <ErrorData>
 <ErrorType>user</ErrorType>
 <RootErrorType>Invalid.Tenant.ProjectNotExists</RootErrorType>
 <RootErrorMessage>The project does not exist</RootErrorMessage>
 <ErrorCode>1</ErrorCode>
 <ErrorMessage>The connection does not exist</ErrorMessage>
</ErrorData>
```

### 运维中心

#### CreateDagComplement

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| ProjectEnv | Strin g | Body | 是 | PROD | 工作空间的环境，包括 PROD和DEV。 |
| StartBizDa te | Strin g | Body | 是 | 2020-05-20 00:00:00 | 补数据的起始业务日期。 |
| Name | Strin g | Body | 是 | xm test _ | 工作流的名称。 |
| RootNodeI d | Long | Body | 是 | 1234 | 补数据的起始节点ID。 |
| IncludeNo deIds | Strin g | Body | 是 | 74324,74325 | 包含的节点ID列表。如果只补一个节点的数据，该节点需要在includeNodeIds 中。 |
| ExcludeNo deIds | Strin g | Body | 否 | 1234 | 可选参数，排除无需补数据的节点ID列表。 |
| BizBeginTi me | Strin g | Body | 否 | 00:00:00 | 可选参数，任务的开始时间。小时调度任务需要设置该参数。 |

|  | 开发指南·Open | API参考 |  |  |  | DataWork | s |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| BizEndTim e | Strin g | Body | 否 | 23:00:00 |  |  | 可选参数，小时调度任务需要，任务的结束时间 |  |  |
| Parallelis m | Boole an | Body | 是 | false |  |  | 是否可以并发执行。 |  |  |
| EndBizDat e | Strin g | Body | 是 | 2020-05-21 00:00:00 |  |  | 补数据的结束业务日期。 |  |  |
| NodePara ms | Strin g | Body | 否 | {"171232":"dt=$bizdate tbods=$tbods"} |  |  | 可选参数，节点的参数。 标准格式为： {"节点 |  |  |
|  |  |  |  |  |  |  |  | {"节点 |  |
|  |  |  |  |  |  |  | id":"key1=value1 |  |  |
|  |  |  |  |  |  |  | key2=value2"} |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Long | 111 | 工作流ID的列表。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| ErrorMessage | String | test | 错误信息。 |
| Success | Boolean | true | 调用是否成功。 |
| ErrorCode | String | 0 | 错误码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateDagComplement &EndBizDate=2020-05-21 00:00:00 &IncludeNodeIds=74324,74325 &Name=xm_test &Parallelism=false &ProjectEnv=PROD &RegionId=default &RootNodeId=1234 &StartBizDate=2020-05-20 00:00:00
```

`&<`公共请求参数> DataWorks 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": 111,
    "ErrorCode": 0,
    "ErrorMessage": "test",
    "Success": true
}
```

`XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>111</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>test</ErrorMessage> <Success>true</Success>
```

#### CreateDagTest

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDagTest | 系统规定参数。取值：CreateDagTest。 |
| Bizdate | String | 是 | 2020-05-26 00:00:00 | 业务日期。 |
| Name | String | 是 | xm create test _ _ | 工作流的名称。 |
| NodeId | Long | 是 | 1234 | 节点的ID。您可以调用ListNodes接口获取节点ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD（生产环境）和DEV（开发环境）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| NodeParams | String | 否 | bizdate=$bizdat e tbods=$tbods | 节点的参数。配置为一个JSON字符串，Key为节点 ID，Value为参数实际取值。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 3333333 | 工作流的ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&Bizdate=2020-05-26 00:00:00 &Name=xm_create_test &NodeId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>3333333</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": 3333333,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

#### CreateRemind

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | CreateRemind | 系统规定参数。取值： CreateRemind |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| RemindNa me | Strin g | Body | 是 | test error remind _ _ | 自定义规则的名称，不能超过128个字符。 |
| DndEnd | Strin g | Body | 否 | 08:00 | 免打扰截止时间，格式为 hh:mm。hh的取值范围为 0,23，mm的取值范围为 0,59。 |
| RemindUn it | Strin g | Body | 是 | NODE | 对象的类型，包括 NODE（任务节点）、 BASELINE（基线） 、 PROJECT（工作空间）和 BIZPROCESS（业务流程）。 |
| NodeIds | Strin g | Body | 否 | 1,2,3 | RemindUnit（对象类型） 为NODE（任务节点）时， 监控的任务节点ID。多个ID 之间使用英文逗号（,）分隔，一个规则最多监控50个节点。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| BaselineId s | Strin g | Body | 否 | 1,2,3 | 当RemindUnit（对象类型）为BASELINE（基线） 时，监控的基线ID。多个ID 之间使用英文逗号（,）分隔，一个规则最多监控5条基线。 |
| ProjectId | Long | Body | 否 | 9527 | 当RemindUnit（对象类型）为PROJECT（工作空间）时，监控的工作空间 ID。一个规则只能监控一个工作空间。 |
| BizProcess Ids | Strin g | Body | 否 | 1,2,3 | 当RemindUnit（对象类型）为BIZPROCESS（业务流程）时，监控的业务流程 ID。多个业务流程ID之间使用英文逗号（,）分隔，一个规则最多监控5个业务流程。 |
| RemindTy pe | Strin g | Body | 是 | FINISHED | 触发条件，包括 FINISHED（完成）、 UNFINISHED（未完成）、 ERROR（出错）、 CYCLE UNFINISHED（周 _ 期未完成）、 TIMEOUT（运行超时）和 EXHAUSTED ERROR（自 _ 动重跑后仍出错）。 |
| MaxAlertT imes | Integ er | Body | 否 | 2 | 最大报警次数。最小值为 1，最大值为10，默认值为 3。 |
| AlertInterv al | Integ er | Body | 否 | 1800 | 最小报警间隔，单位为秒。 最小值为1200，默认值为 1800。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Detail | Strin g | Body | 否 | {"hour":23,"minu":59} | 不同触发条件的说明如下： 当RemindType（触发条件）为FINISHED（完成） 时，传空。 当 RemindType（触发条件） 为UNFINISHED（未完成） 时，传参格式为 {"hour":23,"minu":59}。 hour的取值范围为 0,47，minu的取值范围为 0,59。 当 RemindType（触发条件） 为ERROR（出错）时，传空。 当RemindType（触发条件）为 CYCLE UNFINISHED（周 _ 期未完成）时，传参格式为 {"1":"05:50","2":"06:50" ,"3":"07:50","4":"08:50", "5":"09:50","6":"10:50"," 7":"11:50","8":"12:50"," 9":"13:50","10":"14:50", "11":"15:50","12":"16:50 ","13":"17:50","14":"18: 50","15":"19:50","16":"2 0:50","17":"21:50","18": "22:50","19":"23:50","20 ":"24:50","21":"25:50"} 。JSON字符串key为周期号，取值范围为1,288。 value为该周期对应的未完成时间，格式为hh:mm。 hh的取值范围为0,47，mm 的取值范围为0,59。 当 RemindType（触发条件） 为TIMEOUT（运行超时） 时，传参格式为1800，单位为秒。即从开始运行起， 运行超过30分钟触发报警。 |
| AlertUnit | Strin g | Body | 是 | OWNER | 报警接收对象的粒度，包括 OWNER（任务责任人）和 OTHER（指定的人）。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AlertMeth ods | Strin g | Body | 是 | SMS,MAIL | 报警的方式，包括MAIL（邮件），SMS（短信）和 PHONE（电话，仅 DataWorks专业版及以上版本支持）。多个报警方式之间使用英文逗号（,）分隔。 |
| AlertTarge ts | Strin g | Body | 否 | 9527952795279527 | 当AlertUnit（报警接收人） 为OWNER（节点任务责任人）时，传空。 当 AlertUnit（报警接收人）为 OTHER（指定的人）时， 传入指定用户的阿里云 UID。多个阿里云UID之间使用英文逗号（,）分隔，最多支持10个。 |
| RobotUrls | Strin g | Body | 否 | https://oapi.dingtalk.com /robot/send? access token=********** _ ******************** | 钉钉群机器人的webhook 地址，多个webhook地址之间使用英文逗号（,）分隔。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| Data | Long | 1234 | 创建自定义监控规则成功后，返回的自定义规则 ID。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |
| ErrorCode | String | 1031203110005 | 错误码。 |

**示例**

请求示例 DataWorks

```
&RegionId=default &RemindName=test_error_remind &RemindUnit=NODE &RemindType=FINISHED &AlertUnit=OWNER &AlertMethods=SMS,MAIL
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": 1234,
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>1234</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

| 开发指南·Open | API参考 |  | DataWork |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | Forbidden.Wkbenc h.BaselineNoPermi ssion | You are not authorized to access the baseline. | 无对应的基线权限。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | Forbidden.Wkbenc h.NoProject | You have not joined any project. | 尚未加入任何工作空间。 |
| 500 | Invalid.Wkbench.N odeNotExist | The node does not exist. | 节点不存在。 |
| 500 | Invalid.Wkbench.Ba selineNotExist | The baseline does not exist. | 基线不存在。 |
| 500 | Forbidden.Wkbenc h.RemindOverlimit | The maximum number of reminders is exceeded. | 自定义提醒规则创建超限。 |

#### DeleteRemind

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRemind | 系统规定参数。取值：DeleteRemind。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RemindId | Long | 是 | 1234 | 自定义监控报警规则的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Boolean | true | 是否删除成功，包括true（删除成功）和 false（删除失败）。 |
|---|---|---|---|
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&RegionId=default &RemindId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | Forbidden.Wkbenc h.RemindNoPermis sion | You are not authorized to modify the reminder. | 无权限修改该自定义提醒规则。 |
| 500 | Invalid.Wkbench.Re mindNotExist | The reminder does not exist. | 自定义提醒规则不存在。 |

#### GetBaselineConfig

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetBaselineConf ig | 系统规定参数。取值： GetBaselineConfig。 |
| BaselineId | Long | 是 | 1234 | 基线的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 基线的详情。 |
| BaselineId | Long | 1234 | 基线的ID。 |

DataWorks

| BaselineName | String | 基线名称 | 基线的名称。 |
|---|---|---|---|
| BaselineType | String | DAILY | 基线类型，包括DAILY（天基线）和 HOURLY（小时基线）。 |
| ExpHour | Integer | 7 | 天基线的预警小时，取值范围为0, 47。 |
| ExpMinu | Integer | 30 | 天基线的预警分钟，取值范围为0, 59。 |
| HourExpDetail | String | {"1":"03:28","2":"0 4:28","3":"05:28"," 4":"06:28","5":"07: 28","6":"08:28","7": "09:28","8":"10:28" ,"9":"11:28","10":"1 2:28","11":"13:28", "12":"14:28","13":" 15:28","14":"16:28 ","15":"17:28","16": "18:28","17":"19:2 8","18":"20:28","19 ":"21:28","20":"22: 28","21":"23:28","2 2":"24:28","23":"25 :28","24":"26:28"} | 小时基线的预警时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为0,47，mm的取值范围为0,59。 |
| HourSlaDetail | String | {"1":"03:58","2":"0 4:58","3":"05:58"," 4":"06:58","5":"07: 58","6":"08:58","7": "09:58","8":"10:58" ,"9":"11:58","10":"1 2:58","11":"13:58", "12":"14:58","13":" 15:58","14":"16:58 ","15":"17:58","16": "18:58","17":"19:5 8","18":"20:58","19 ":"21:58","20":"22: 58","21":"23:58","2 2":"24:58","23":"25 :58","24":"26:58"} | 小时基线的承诺时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为0,47，mm的取值范围为0,59。 |
| IsDefault | Boolean | true | 是否为工作空间的默认基线，包括true（是）和 false（否）。 |
| Owner | String | 9527952**** | 基线责任人的阿里云UID。有多个责任人时，使用英文逗号（,）分隔。 |
| Priority | Integer | 1 | 基线的优先级，取值集合为{1,3,5,7,8}。 |
| ProjectId | Long | 1234 | 工作空间的ID。 |

DataWorks

| SlaHour | Integer | 9 | 天基线的承诺小时，取值范围为0, 47。 |
|---|---|---|---|
| SlaMinu | Integer | 30 | 天基线的承诺分钟，取值范围为0, 59。 |
| UseFlag | Boolean | true | 基线是否开启，包括true（开启）和false（未开启）。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 401 | HTTP返回码。 |
| RequestId | String | ecb967ec-c137- 48a5-860**** | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&BaselineId=1234 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```json
<RequestId>ecb967ec-c137-48a5-860****</RequestId> <HttpStatusCode>401</HttpStatusCode> <Data>
    <IsDefault>true</IsDefault>
    <BaselineId>1234</BaselineId>
    <HourSlaDetail>
{"1":"03:58","2":"04:58","3":"05:58","4":"06:58","5":"07:58","6":"08:58","7":"09:58","8": 0:58","9":"11:58","10":"12:58","11":"13:58","12":"14:58","13":"15:58","14":"16:58","15":" :58","16":"18:58","17":"19:58","18":"20:58","19":"21:58","20":"22:58","21":"23:58","22":" :58","23":"25:58","24":"26:58"}</HourSlaDetail>
    <ExpHour>7</ExpHour>
    <ExpMinu>30</ExpMinu>
    <Owner>9527952****</Owner>
    <SlaHour>9</SlaHour>
    <Priority>1</Priority>
    <SlaMinu>30</SlaMinu>
    <HourExpDetail>
{"1":"03:28","2":"04:28","3":"05:28","4":"06:28","5":"07:28","6":"08:28","7":"09:28","8": 0:28","9":"11:28","10":"12:28","11":"13:28","12":"14:28","13":"15:28","14":"16:28","15":" :28","16":"18:28","17":"19:28","18":"20:28","19":"21:28","20":"22:28","21":"23:28","22":" :28","23":"25:28","24":"26:28"}</HourExpDetail>
    <ProjectId>1234</ProjectId>
    <UseFlag>true</UseFlag>
    <BaselineType>DAILY</BaselineType>
    <BaselineName>基线名称</BaselineName>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "ecb967ec-c137-48a5-860****",
    "HttpStatusCode": 401,
    "Data": {
        "IsDefault": true,
        "BaselineId": 1234,
        "HourSlaDetail": "
{\"1\":\"03:58\",\"2\":\"04:58\",\"3\":\"05:58\",\"4\":\"06:58\",\"5\":\"07:58\",\"6\":\" :58\",\"7\":\"09:58\",\"8\":\"10:58\",\"9\":\"11:58\",\"10\":\"12:58\",\"11\":\"13:58\",\ 2\":\"14:58\",\"13\":\"15:58\",\"14\":\"16:58\",\"15\":\"17:58\",\"16\":\"18:58\",\"17\": 19:58\",\"18\":\"20:58\",\"19\":\"21:58\",\"20\":\"22:58\",\"21\":\"23:58\",\"22\":\"24:5 ",\"23\":\"25:58\",\"24\":\"26:58\"}",
        "ExpHour": 7,
        "ExpMinu": 30,
        "Owner": "9527952****",
        "SlaHour": 9,
        "Priority": 1,
        "SlaMinu": 30,
        "HourExpDetail": "
{\"1\":\"03:28\",\"2\":\"04:28\",\"3\":\"05:28\",\"4\":\"06:28\",\"5\":\"07:28\",\"6\":\" :28\",\"7\":\"09:28\",\"8\":\"10:28\",\"9\":\"11:28\",\"10\":\"12:28\",\"11\":\"13:28\",\ 2\":\"14:28\",\"13\":\"15:28\",\"14\":\"16:28\",\"15\":\"17:28\",\"16\":\"18:28\",\"17\": 19:28\",\"18\":\"20:28\",\"19\":\"21:28\",\"20\":\"22:28\",\"21\":\"23:28\",\"22\":\"24:2 ",\"23\":\"25:28\",\"24\":\"26:28\"}",
        "ProjectId": 1234,
        "UseFlag": true,
        "BaselineType": "DAILY",
```

`"BaselineName": "`基线名称"

```json
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | Forbidden.Wkbenc h.BaselineNoPermi ssion | You are not authorized to access the baseline. | 无对应的基线权限。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Wkbe nch.ServiceError | An internal error occurred. | 服务开小差了。 |

DataWorks

| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetBaselineKeyPath

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetBaselineKey Path | 系统规定参数。取值： GetBaselineKeyPath。 |
| BaselineId | Long | 是 | 1234 | 基线的ID。 |
| Bizdate | String | 是 | 2020-07- 07T00:00:00+0 800 | 业务日期，需要使用yyyy-MM- dd'T'HH:mm:ssZ的UTC格式。 |
| InGroupId | Integer | 是 | 1 | 基线实例周期号。天基线为1，小时基线的取值范围为1,24。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Array of Data |  | 关键路径信息。 |
|---|---|---|---|
| Bizdate | Long | 1553443200000 | 实例的业务日期时间戳。 |
| InGroupId | Integer | 1 | 实例周期号，取值范围为1,288。 |
| InstanceId | Long | 12345 | 实例的ID。 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 9527952**** | 节点责任人的阿里云UID。 |
| PrgType | Integer | 10 | 节点类型，常用的节点类型包括数据集成 （23）、MaxCompute SQL（10）、 Shell（6）和虚节点（99）。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| Runs | Array of Runs |  | 实例的运行记录。 |
| AbsTime | Long | 1553531402000 | 实例的预计开始运行时间+历史平均运行时长得到的时间戳。 |
| BeginCast | Long | 1553531686000 | 实例预计开始运行的时间戳。 |
| BeginRunning Time | Long | 1553531401000 | 实例实际开始运行的时间戳。 |
| BeginWaitRes Time | Long | 1553531401000 | 实例开始进入等待资源状态的时间戳。 |
| BeginWaitTim eTime | Long | 1553531400000 | 实例开始进入等待时间状态的时间戳。 |
| Bizdate | Long | 1553443200000 | 实例的业务日期时间戳。 |
| CycTime | Long | 1553443200000 | 实例的定时时间戳。 |
| EndCast | Long | 1553531687000 | 实例的预计运行结束时间戳。 |

DataWorks

| FinishTime | Long | 1553531401000 | 实例的实际运行结束时间戳。 |
|---|---|---|---|
| InGroupId | Integer | 1 | 实例周期号，取值范围为1,288。 |
| InstanceId | Long | 1234 | 实例的ID。 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 9527952**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| Status | String | SUCCESS | 实例的状态，包括NOT RUN（未运行）、 _ WAIT TIME（等待时间）、 _ WAIT RESOURCE（等待资源）、 _ RUNNING（运行中）、CHECKING（校检中）、CHECKING CONDITION（条件检测 _ 中）、FAILURE（运行失败）和SUCCESS（运行成功）。 |
| Topics | Array of Topics |  | 实例关联的事件信息。 |
| AddTime | Long | 1553531401000 | 事件发现时间戳。 |
| InstanceId | Long | 1234 | 实例的ID。 |
| TopicId | Long | 1234 | 事件的ID。 |
| TopicName | Long | 1234 | 事件的名称。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |

DataWorks

| Success | Boolean | true | 调用是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetBaselineKeyPath &BaselineId=1234 &Bizdate=2020-07-07T00:00:00+0800 &InGroupId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <PrgType>10</PrgType>
    <Owner>9527952****</Owner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
    <InstanceId>12345</InstanceId>
    <NodeId>1234</NodeId>
    <ProjectId>1234</ProjectId>
    <InGroupId>1</InGroupId>
    <Bizdate>1553443200000</Bizdate>
    <Runs>
        <Status>SUCCESS</Status>
        <Owner>9527952****</Owner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
        <InstanceId>1234</InstanceId>
        <ProjectId>1234</ProjectId>
        <CycTime>1553443200000</CycTime>
        <BeginWaitTimeTime>1553531400000</BeginWaitTimeTime>
        <InGroupId>1</InGroupId>
        <Bizdate>1553443200000</Bizdate>
        <BeginRunningTime>1553531401000</BeginRunningTime>
        <BeginCast>1553531686000</BeginCast>
        <AbsTime>1553531402000</AbsTime>
        <FinishTime>1553531401000</FinishTime>
        <NodeId>1234</NodeId>
        <BeginWaitResTime>1553531401000</BeginWaitResTime>
        <EndCast>1553531687000</EndCast>
    </Runs>
    <Topics>
        <InstanceId>1234</InstanceId>
        <TopicId>1234</TopicId>
        <AddTime>1553531401000</AddTime>
        <TopicName>1234</TopicName>
    </Topics>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "PrgType": 10,
        "Owner": "9527952****",
```

`"NodeName": "`节点名称`",`

```json
        "InstanceId": 12345,
        "NodeId": 1234,
        "ProjectId": 1234,
        "InGroupId": 1,
        "Bizdate": 1553443200000,
        "Runs": {
            "Status": "SUCCESS",
            "Owner": "9527952****",
```

`"NodeName": "`节点名称`",`

```json
            "InstanceId": 1234,
            "ProjectId": 1234,
            "CycTime": 1553443200000,
            "BeginWaitTimeTime": 1553531400000,
            "InGroupId": 1,
            "Bizdate": 1553443200000,
            "BeginRunningTime": 1553531401000,
            "BeginCast": 1553531686000,
            "AbsTime": 1553531402000,
            "FinishTime": 1553531401000,
            "NodeId": 1234,
            "BeginWaitResTime": 1553531401000,
            "EndCast": 1553531687000
        },
        "Topics": {
            "InstanceId": 1234,
            "TopicId": 1234,
            "AddTime": 1553531401000,
            "TopicName": 1234
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.BaselineNoPermi ssion | You are not authorized to access the baseline. | 无对应的基线权限。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | Invalid.Wkbench.Ba selineStatusNotExis t | The BaselineStatus does not exist. | 基线实例不存在。 |

#### GetBaselineStatus

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetBaselineStat us | 系统规定参数。取值： GetBaselineStatus。 |
| BaselineId | Long | 是 | 1234 | 基线的ID。 |
| Bizdate | String | 是 | 2020-07- 07T00:00:00+0 800 | 业务日期，需要使用UTC格式（yyyy- MM-dd'T'HH:mm:ssZ）。 |

DataWorks

| InGroupId | Integer | 是 | 1 | 基线实例的周期号。天基线为1，小时基线的取值范围为1,24。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 基线实例的详情。 |
| BaselineId | Long | 1234 | 基线的ID。 |
| BaselineName | String | 基线名称 | 基线的名称。 |
| Bizdate | Long | 1553443200000 | 业务日期时间戳。 |
| BlockInstance | Struct |  | 关键实例信息。 |
| EndCast | Long | 1553443200000 | 实例的预计完成时间戳。 |
| FinishTime | Long | 1553443200000 | 实例的实际完成时间戳。 |
| InstanceId | Long | 12345 | 实例的ID。 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 9527952795**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| Status | String | SUCCESS | 实例的状态，包括NOT RUN（未运行）、 _ WAIT TIME（等待时间）、 _ WAIT RESOURCE（等待资源）、 _ RUNNING（运行中）、CHECKING（校检中）、CHECKING CONDITION（条件检测 _ 中）、FAILURE（运行失败）和SUCCESS（运行成功）。 |
| Buffer | Float | 1200 | 基线实例的余量，单位为秒。 |

DataWorks

| EndCast | Long | 1553443200000 | 基线实例的预计产出时间戳。 |
|---|---|---|---|
| ExpTime | Long | 1553443200000 | 基线实例的预警时间戳。 |
| FinishStatus | String | UNFINISH | 基线实例是否完成，包括UNFINISH（未完成） 和FINISH（已完成）。 |
| FinishTime | Long | 1553443200000 | 当FinishStatus（基线实例完成状态）为 FINISH（已完成）时，返回基线实例的完成时间戳。 |
| InGroupId | Integer | 1 | 基线实例的周期号。天基线为1，小时基线的取值范围为1,24。 |
| LastInstance | Struct |  | 最晚实例信息。 |
| EndCast | Long | 1553443200000 | 实例的预计完成时间戳。 |
| FinishTime | Long | 1553443200000 | 实例的实际完成时间戳。 |
| InstanceId | Long | 12345 | 实例的ID。 |
| NodeId | Long | 12345 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 9527952795**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 12345 | 节点所在工作空间的ID。 |
| Status | String | SUCCESS | 实例的状态，包括NOT RUN（未运行）、 _ WAIT TIME（等待时间）、 _ WAIT RESOURCE（等待资源）、 _ RUNNING（运行中）、CHECKING（校检中）、CHECKING CONDITION（条件检测 _ 中）、FAILURE（运行失败）和SUCCESS（运行成功）。 |
| Owner | String | 9527952795**** | 基线责任人的阿里云UID。多个责任人之间使用英文逗号（,）分隔。 |
| Priority | Integer | 1 | 基线的优先级，取值范围为{1,2,5,7,8}。 |

DataWorks

| ProjectId | Long | 1234 | 基线所在工作空间的ID。 |
|---|---|---|---|
| SlaTime | Long | 1553443200000 | 基线实例的承诺时间戳。 |
| Status | String | SAFE | 基线的状态，包括ERROR（异常）、SAFE（安全）、DANGROUS（预警）和OVER（破线）。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&BaselineId=1234 &Bizdate=2020-07-07T00:00:00+0800 &InGroupId=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Status>SAFE</Status>
    <Buffer>1200</Buffer>
    <BaselineId>1234</BaselineId>
    <Owner>9527952795****</Owner>
    <Priority>1</Priority>
    <FinishStatus>UNFINISH</FinishStatus>
    <ProjectId>1234</ProjectId>
    <InGroupId>1</InGroupId>
    <ExpTime>1553443200000</ExpTime>
    <Bizdate>1553443200000</Bizdate>
    <FinishTime>1553443200000</FinishTime>
    <BaselineName>基线名称</BaselineName>
    <SlaTime>1553443200000</SlaTime>
    <EndCast>1553443200000</EndCast>
    <LastInstance>
        <Status>SUCCESS</Status>
        <Owner>9527952795****</Owner>
        <FinishTime>1553443200000</FinishTime>
```

`<NodeName>`节点名称`</NodeName>`

```xml
        <InstanceId>12345</InstanceId>
        <NodeId>12345</NodeId>
        <ProjectId>12345</ProjectId>
        <EndCast>1553443200000</EndCast>
    </LastInstance>
    <BlockInstance>
        <Status>SUCCESS</Status>
        <Owner>9527952795****</Owner>
        <FinishTime>1553443200000</FinishTime>
```

`<NodeName>`节点名称`</NodeName>`

```xml
        <InstanceId>12345</InstanceId>
        <NodeId>1234</NodeId>
        <ProjectId>1234</ProjectId>
        <EndCast>1553443200000</EndCast>
    </BlockInstance>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "Status": "SAFE",
        "Buffer": 1200,
        "BaselineId": 1234,
        "Owner": "9527952795****",
        "Priority": 1,
        "FinishStatus": "UNFINISH",
        "ProjectId": 1234,
        "InGroupId": 1,
        "ExpTime": 1553443200000,
        "Bizdate": 1553443200000,
        "FinishTime": 1553443200000,
```

`"BaselineName": "`基线名称`",`

```json
        "SlaTime": 1553443200000,
        "EndCast": 1553443200000,
        "LastInstance": {
            "Status": "SUCCESS",
            "Owner": "9527952795****",
            "FinishTime": 1553443200000,
```

`"NodeName": "`节点名称`",`

```json
            "InstanceId": 12345,
            "NodeId": 12345,
            "ProjectId": 12345,
            "EndCast": 1553443200000
        },
        "BlockInstance": {
            "Status": "SUCCESS",
            "Owner": "9527952795****",
            "FinishTime": 1553443200000,
```

`"NodeName": "`节点名称`",`

```json
            "InstanceId": 12345,
            "NodeId": 1234,
            "ProjectId": 1234,
            "EndCast": 1553443200000
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetDag

调用GetDag，根据DagId获取Dag详情。GetDag支持查询手动业务流程、手动任务、补数据的Dag详情信息，不支持查询日常调度Dag详情。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDag | 系统规定参数。取值：GetDag。 |
| DagId | Long | 是 | 1231414523411 11 | DagId可以是补数据 CreateDagComplement，测试 CreateTest，执行手动业务流程 CreateManualDag等接口返回的 DagId。 |
| ProjectEnv | String | 是 | PROD | 调度运维环境的标识：PROD表示生产环境，DEV表示开发环境。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | Dag的详情信息。 |
| Bizdate | Long | 1605052800000 | 业务日期。 |
| CreateTime | Long | 1605052800000 | 创建时间。 |
| CreateUser | String | 173662940004854 5 | 创建人。 |
| DagId | Long | 12345678 | GAG ID。 |
| FinishTime | Long | 1605052800000 | 结束时间。 |
| Gmtdate | Long | 1605052800000 | Gmtdate。 |
| ModifyTime | Long | 1605052800000 | 修改时间。 |
| Name | String | dag test _ | Dag的名称。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| StartTime | Long | 1605052800000 | 开始时间。 |
| Status | String | FAILURE | DAG的状态，包括CREATED（已创建）、 RUNNING（运行中）、FAILURE（运行失败） 和SUCCESS（运行成功）。 |
| Type | String | MANUAL | DAG的类型，包括MANUAL（手动任务工作流）、SMOKE TEST（冒烟测试工作流）、 _ SUPPLY DATA（补数据）和 _ BUSINESS PROCESS DAG（一次性业务流程 _ _ 工作流）。 |
| ErrorCode | String | 200 | 错误码。 |
| ErrorMessage | String | Invalid.Tenant.Con nectionNotExists | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |

DataWorks

| RequestId | String | 7782a299-b291- 4fee-8424- cf8058ef**** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
&DagId=123141452341111 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7782a299-b291-4fee-8424-cf8058ef****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Gmtdate>1605052800000</Gmtdate>
    <Status>FAILURE</Status>
    <ModifyTime>1605052800000</ModifyTime>
    <Type>MANUAL</Type>
    <FinishTime>1605052800000</FinishTime>
    <CreateTime>1605052800000</CreateTime>
    <StartTime>1605052800000</StartTime>
    <ProjectId>10001</ProjectId>
    <CreateUser>1736629400048545</CreateUser>
    <DagId>12345678</DagId>
    <Bizdate>1605052800000</Bizdate>
    <Name>dag_test</Name>
</Data> <ErrorCode>200</ErrorCode> <ErrorMessage>Invalid.Tenant.ConnectionNotExists</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"7782a299-b291-4fee-8424-cf8058ef****","HttpStatusCode":"200","Data":{"Gmt date":"1605052800000","Status":"FAILURE","ModifyTime":"1605052800000","Type":"MANUAL","Fi shTime":"1605052800000","CreateTime":"1605052800000","StartTime":"1605052800000","Project ":"10001","CreateUser":"1736629400048545","DagId":"12345678","Bizdate":"1605052800000","N e":"dag_test"},"ErrorCode":"200","ErrorMessage":"Invalid.Tenant.ConnectionNotExists","Suc ss":"false"}
```

#### GetInstance

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstance | 系统规定参数。取值：GetInstance。 |
| InstanceId | Long | 是 | 1234 | 实例的ID。您可以调用ListInstances获取。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD（生产环境）和DEV（开发环境）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 实例的详细信息。 |
| BaselineId | Long | 123123 | 基线ID。 |
| BeginRunning Time | Long | 1590416703313 | 实例任务开始运行的时间。 |
| BeginWaitRes Time | Long | 1590416703313 | 实例任务开始等待资源的时间。 |
| BeginWaitTim eTime | Long | 1590416703313 | 实例任务开始等待调度的时间。 |
| Bizdate | Long | 1590336000000 | 业务日期。通常为该任务运行时间的前一天。 |
| Connection | String | odps first _ | 连接串。 |
| CreateTime | Long | 1590416703313 | 实例的创建时间。 |
| CycTime | Long | 1590422400000 | 实例任务的定时时间。 |
| DagId | Long | 338450167 | 工作流的ID。 |

DataWorks

| DagType | String | DAILY | 工作流的类型，取值如下： DAILY（日常调度） MANUAL（手动任务） SMOKE TEST（冒烟测试） _ SUPPLY DATA（补数据） _ |
|---|---|---|---|
| DqcDescriptio n | String | [{"projectName":"z tjy dim","tableNam _ e":"dim user agent _ _ manage area a"," _ _ _ partition":"ds\u003 d$[yyyy-mm-dd- 1]"}] | DQC分区规则串。 |
| DqcType | Integer | 1 | DQC类型，取值如下： 0表示有关联dqc。 1表示没有关联dqc。 |
| ErrorMessage | String | test | 信息 |
| FinishTime | Long | 11713307578 | 实例任务运行的结束时间。 |
| InstanceId | Long | 11713307578 | 实例的ID。 |
| ModifyTime | Long | 1590416703313 | 实例任务的最新修改时间。 |
| NodeId | Long | 33115 | 节点的ID。 |
| NodeName | String | kzh | 节点的名称。 |
| ParamValues | String | bizdate=$bizdate tbods=$tbods tbdw=$tbdw tbpmic=$tbpmic tbpidx=$tbpidx tbptcif=$tbptcif | 参数信息。 |
| Priority | Integer | 1 | 实例运行优先级，取值分为1、3、5、7和8。取值越大，优先级越高。默认优先级为1。 |
| RelatedFlowId | Long | 123123 | 关联的业务流程ID。 |
| RepeatInterval | Long | 60000 | 调度任务运行出错后，重新调整调度频率，单位为毫秒（ms）。 |
| Repeatability | Boolean | true | 实例任务是否可以重复执行。 |

DataWorks

| Status | String | NOT RUN _ | 任务的状态，取值如下： NOT RUN（未运行） _ WAIT TIME（等待定时时间dueTime或 _ cycleTime到来） WAIT RESOURCE（等待资源） _ RUNNING（运行中） CHECKING（下发给数据质量进行数据校检） CHECKING CONDITION（正在进行分支条 _ 件校检） FAILURE（执行失败） SUCCESS（执行成功） |
|---|---|---|---|
| ErrorCode | String | 0 | 错误码。 |
| ErrorMessage | String | test | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&InstanceId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <BaselineId>123123</BaselineId>
    <Status>NOT_RUN</Status>
    <ModifyTime>1590416703313</ModifyTime>
    <NodeName>kzh</NodeName>
    <DagType>DAILY</DagType>
    <InstanceId>11713307578</InstanceId>
    <DqcType>1</DqcType>
    <Priority>1</Priority>
    <CreateTime>1590416703313</CreateTime>
    <ParamValues>bizdate=$bizdate tbods=$tbods tbdw=$tbdw tbpmic=$tbpmic tbpidx=$tbpidx
tbptcif=$tbptcif</ParamValues>
    <Connection>odps_first</Connection>
    <RelatedFlowId>123123</RelatedFlowId>
    <BeginWaitTimeTime>1590416703313</BeginWaitTimeTime>
    <CycTime>1590422400000</CycTime>
    <DagId>338450167</DagId>
    <BeginRunningTime>1590416703313</BeginRunningTime>
    <Bizdate>1590336000000</Bizdate>
    <Repeatability>true</Repeatability>
    <FinishTime>11713307578</FinishTime>
    <DqcDescription>
[{"projectName":"ztjy_dim","tableName":"dim_user_agent_manage_area_a","partition":"ds\u00 $[yyyy-mm-dd-1]"}]</DqcDescription>
    <NodeId>33115</NodeId>
    <BeginWaitResTime>1590416703313</BeginWaitResTime>
    <ErrorMessage>test</ErrorMessage>
    <RepeatInterval>60000</RepeatInterval>
</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>test</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": {
        "BaselineId": 123123,
        "Status": "NOT_RUN",
        "ModifyTime": 1590416703313,
        "NodeName": "kzh",
        "DagType": "DAILY",
        "InstanceId": 11713307578,
        "DqcType": 1,
        "Priority": 1,
        "CreateTime": 1590416703313,
        "ParamValues": "bizdate=$bizdate tbods=$tbods tbdw=$tbdw tbpmic=$tbpmic
tbpidx=$tbpidx tbptcif=$tbptcif",
        "Connection": "odps_first",
        "RelatedFlowId": 123123,
        "BeginWaitTimeTime": 1590416703313,
        "CycTime": 1590422400000,
        "DagId": 338450167,
        "BeginRunningTime": 1590416703313,
        "Bizdate": 1590336000000,
        "Repeatability": true,
        "FinishTime": 11713307578,
        "DqcDescription": "
[{\"projectName\":\"ztjy_dim\",\"tableName\":\"dim_user_agent_manage_area_a\",\"partition :\"ds\\u003d$[yyyy-mm-dd-1]\"}]",
        "NodeId": 33115,
        "BeginWaitResTime": 1590416703313,
        "ErrorMessage": "test",
        "RepeatInterval": 60000
    },
    "ErrorCode": 0,
    "ErrorMessage": "test",
    "Success": true
}
```

#### GetInstanceConsumeTimeRank

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstanceCon sumeTimeRank | 系统规定参数。取值： GetInstanceConsumeTimeRank。 |
| Bizdate | String | 是 | 2020-09- 21T00:00:00+0 800 | 业务日期，精确到天。您需要使用yyyy- MM-dd'T'HH:mm:ssZ的UTC格式。 |

DataWorks

| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceConsu meTimeRank | Struct |  | 实例运行时长的排行记录。 |
| ConsumeTime Rank | Array of ConsumeTime Rank |  | 实例运行时长的排行数据。 |
| Bizdate | Long | 1600963200000 | 实例运行的业务日期。 |
| Consumed | Long | 1000 | 实例运行时长，单位为s。 |
| InstanceId | Long | 95279527 | 实例ID。 |
| NodeId | Long | 9527 | 任务节点的ID。 |
| NodeName | String | 节点的名称 | 节点的名称。 |
| Owner | String | 952795279527 | 节点责任人的阿里云UID。 |
| PrgType | Integer | 10 | 任务的类型。 |
| UpdateTime | Long | 1600963200000 | 排行更新时间戳。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetInstanceConsumeTimeRank &Bizdate=2020-09-21T00:00:00+0800 &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

|  | <RequestId>0000-ABCD-EFG*****</RequestId> <InstanceConsumeTimeRank> <UpdateTime>1600963200000</UpdateTime> <ConsumeTimeRank> <PrgType>10</PrgType> <Owner>952795279527</Owner> <InstanceId>95279527</InstanceId> <NodeName>节点的名称</NodeName> <NodeId>9527</NodeId> <Consumed>1000</Consumed> <Bizdate>1600963200000</Bizdate> </ConsumeTimeRank> </InstanceConsumeTimeRank> |
|---|---|

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","InstanceConsumeTimeRank": {"UpdateTime":"1600963200000","ConsumeTimeRank": [{"PrgType":"10","Owner":"952795279527","InstanceId":"95279527","NodeName":"节点的名称"," NodeId":"9527","Consumed":"1000","Bizdate":"1600963200000"}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
|---|---|---|---|
| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetInstanceCountTrend

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstanceCou ntTrend | 系统规定参数。取值： GetInstanceCountTrend。 |
| BeginDate | String | 是 | 2020-04- 02T00:00:00+0 800 | 起始业务日期，精确到天。您需要使用 yyyy-MM-dd'T'HH:mm:ssZ的UTC格式。 |
| EndDate | String | 是 | 2020-09- 10T00:00:00+0 800 | 截止业务日期，精确到天。您需要使用 yyyy-MM-dd'T'HH:mm:ssZ的UTC格式。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceCount s | Array of IntanceCounts |  | 实例数量趋势数据。 |
| Count | Integer | 9527 | 实例的数量。 |
| Date | Long | 1600963200000 | 业务日期对应的时间戳。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

DataWorks

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetInstanceCountTrend &BeginDate=2020-04-02T00:00:00+0800 &EndDate=2020-09-10T00:00:00+0800 &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <InstanceCounts>
    <Count>9527</Count>
    <Date>1600963200000</Date>
</InstanceCounts>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","InstanceCounts": [{"Count":"9527","Date":"1600963200000"}]}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |

DataWorks

| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
|---|---|---|---|
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.NoProject | You have not joined any project. | 尚未加入任何工作空间。 |
| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetInstanceErrorRank

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstanceErro rRank | 系统规定参数。取值： GetInstanceErrorRank。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceErrorR ank | Struct |  | 节点出错的排行数据。 |
| ErrorRank | Array of ErrorRank |  | 节点近一个月出错排行数据。 |
| Count | Integer | 3 | 节点出错的次数。 |
| NodeId | Long | 9527 | 节点的ID。 |
| NodeName | String | 节点的名称 | 节点的名称。 |
| Owner | String | 952795279527 | 节点责任人的阿里云UID。 |

DataWorks

| PrgType | Integer | 10 | 节点任务的类型。 |
|---|---|---|---|
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| UpdateTime | Long | 1600963200000 | 出错排行更新的时间戳。 |
| RequestId | String | 952795279527**** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetInstanceErrorRank &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>952795279527****</RequestId> <InstanceErrorRank>
    <UpdateTime>1600963200000</UpdateTime>
    <ErrorRank>
        <PrgType>10</PrgType>
        <Owner>952795279527</Owner>
```

`<NodeName>`节点的名称`</NodeName>`

```xml
        <ProjectId>10001</ProjectId>
        <NodeId>9527</NodeId>
        <Count/>
    </ErrorRank>
</InstanceErrorRank>
```

`JSON` 格式

```json
{"RequestId":"952795279527****","InstanceErrorRank": {"UpdateTime":"1600963200000","ErrorRank": [{"PrgType":"10","Owner":"952795279527","NodeName":"节点的名称","ProjectId":"10001","NodeId":"9527","Count":""}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |

DataWorks

| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetInstanceLog

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstanceLog | 系统规定参数。取值： GetInstanceLog。 |
| InstanceId | Long | 是 | 12345 | 实例的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |

DataWorks

| RegionId | String | 是 | default | 区域ID，为固定值default。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | String | log content _ | 日志的内容。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
&InstanceId=12345 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>log_content</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD- EFG*****","HttpStatusCode":"200","Data":"log_content","ErrorCode":"Invalid.Tenant.Connect nNotExists","ErrorMessage":"The connection does not exist.","Success":"false"}
```

#### GetInstanceStatusStatistic

DataWorks 调用GetInstanceStatusStatistic获取实例任务不同运行状态的数量统计。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstanceStat usStatistic | 系统规定参数。取值： GetInstanceStatusStatistic。 |
| BizDate | String | 是 | 2020-01-01 | 获取不同实例状态数量的业务日期。格式为yyyy-MM-dd HH:mm:ss。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括PROD（生产环境）和 DEV（开发环境）。 |
| ProjectId | Long | 是 | 1234 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，用于定位日志，排查问题。 |
| StatusCount | Struct |  | 实例状态的数量统计。 |
| FailureCount | Integer | 1 | 运行失败的实例数量。 |
| NotRunCount | Integer | 1 | 未运行的实例数量。 |
| RunningCount | Integer | 1 | 运行中的实例数量。 |
| SuccessCount | Integer | 1 | 运行成功的实例数量。 |
| TotalCount | Integer | 1 | 实例的总数。 |
| WaitResCount | Integer | 1 | 等待资源的实例数量。 |
| WaitTimeCoun t | Integer | 1 | 等待运行的实例数量。 |

**示例**

DataWorks 请求示例

```
http(s)://[Endpoint]/?Action=GetInstanceStatusStatistic &BizDate=2020-01-01 &ProjectEnv=PROD &ProjectId=1234 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StatusCount>
    <TotalCount>1</TotalCount>
    <FailureCount>1</FailureCount>
    <RunningCount>1</RunningCount>
    <WaitResCount>1</WaitResCount>
    <SuccessCount>1</SuccessCount>
    <NotRunCount>1</NotRunCount>
    <WaitTimeCount>1</WaitTimeCount>
</StatusCount> <RequestId>0000-ABCD-EFG****</RequestId>
```

`JSON` 格式

```json
{
    "StatusCount": {
        "TotalCount": 1,
        "FailureCount": 1,
        "RunningCount": 1,
        "WaitResCount": 1,
        "SuccessCount": 1,
        "NotRunCount": 1,
        "WaitTimeCount": 1
    },
    "RequestId": "0000-ABCD-EFG****"
}
```

#### GetNode

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNode | 系统规定参数。取值：GetNode。 |
| NodeId | Long | 是 | 1234 | 节点的ID。 |

DataWorks

| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 节点的详情。 |
| BaselineId | Long | 123456 | 基线ID |
| Connection | String | odps first dev _ _ | 连接串 |
| CronExpress | String | 00 00 00 * * ? | cron表达式。 |
| Description | String | test | 节点的描述信息。 |
| DqcDescriptio n | String | [{"projectName":"t est 0923001","tabl _ eName":"test table _ 001","partition":"d _ s\u003d$[yyyymm dd]"}, {"projectName":"te st 0923001","table _ Name":"test table _ _ 002","partition":"N OTAPARTITIONTAB LE"}] | DQC分区规则串 |
| DqcType | Integer | 1 | DQC类型，0表示有关联dqc，1表示没有关联 dqc |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | sql节点 | 节点的名称。 |
| OwnerId | String | 17366294**** | 负责人的ID。 |
| ParamValues | String | a=b | 额外的参数。 |
| Priority | Integer | 1 | 任务优先级，1/3/5/7/8 |

DataWorks

| ProgramType | String | ODPS SQL _ | 节点的类型。 |
|---|---|---|---|
| ProjectId | Long | 1234 | 工作空间的ID。 |
| RelatedFlowId | Long | 123 | 关联业务流程ID |
| RepeatInterval | Long | 60 | 出错后重新调度频率 |
| Repeatability | String | true | 是否可以重复运行。 |
| ResGroupNam e | String | 默认资源组 | 资源组的名称。 |
| SchedulerType | String | NORMAL | 调度的类型，取值如下： NORMAL：正常调度任务。 MANUAL：手动任务，不会被日常调度。 PAUSE：暂停任务。 SKIP：空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID，用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&NodeId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```json
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <BaselineId>123456</BaselineId>
    <ResGroupName>默认资源组</ResGroupName>
    <Description>test</Description>
    <NodeName>sql节点</NodeName>
    <DqcType>1</DqcType>
    <Priority>1</Priority>
    <ParamValues>a=b</ParamValues>
    <Connection>odps_first_dev</Connection>
    <ProjectId>1234</ProjectId>
    <RelatedFlowId>123</RelatedFlowId>
    <SchedulerType>NORMAL</SchedulerType>
    <CronExpress>00 00 00 * * ?</CronExpress>
    <Repeatability>true</Repeatability>
    <OwnerId>17366294****</OwnerId>
    <DqcDescription>
[{"projectName":"test_0923001","tableName":"test_table_001","partition":"ds\u003d$[yyyymm ]"}, {"projectName":"test_0923001","tableName":"test_table_002","partition":"NOTAPARTITIONTABL }]</DqcDescription>
    <NodeId>1234</NodeId>
    <ProgramType>ODPS_SQL</ProgramType>
    <RepeatInterval>60</RepeatInterval>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": {
        "BaselineId": 123456,
```

`"ResGroupName": "`默认资源组`",`

```json
        "Description": "test",
        "NodeName": "sql节点",
        "DqcType": 1,
        "Priority": 1,
        "ParamValues": "a=b",
        "Connection": "odps_first_dev",
        "ProjectId": 1234,
        "RelatedFlowId": 123,
        "SchedulerType": "NORMAL",
        "CronExpress": "00 00 00 * * ?",
        "Repeatability": true,
        "OwnerId": "17366294****",
        "DqcDescription": "
[{\"projectName\":\"test_0923001\",\"tableName\":\"test_table_001\",\"partition\":\"ds\\u 3d$[yyyymmdd]\"}, {\"projectName\":\"test_0923001\",\"tableName\":\"test_table_002\",\"partition\":\"NOTAPA ITIONTABLE\"}]",
        "NodeId": 1234,
        "ProgramType": "ODPS_SQL",
        "RepeatInterval": 60
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### GetNodeCode

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNodeCode | 系统规定参数。取值：GetNodeCode。 |
| NodeId | Long | 是 | 1234 | 节点的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | String | select a; | 节点的代码。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
&NodeId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>select a;</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data":"select a;","ErrorCode":"Invalid.Tenant.ConnectionNotExists","ErrorMessage":"The connection doe s not exist.","Success":"false"}
```

#### GetNodeOnBaseline

**请求参数**

DataWorks

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNodeOnBase line | 系统规定参数。取值： GetNodeOnBaseline。 |
| BaselineId | Long | 是 | 1234 | 基线的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of Data |  | 节点的列表 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 9527952**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD-E**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | String | true | 调用是否成功。 |

**示例**

请求示例

```
&BaselineId=1234 &RegionId=default
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Owner>9527952****</Owner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
    <ProjectId>1234</ProjectId>
    <NodeId>1234</NodeId>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-E****",
    "HttpStatusCode": 200,
    "Data": {
        "Owner": "9527952****",
```

`"NodeName": "`节点名称`",`

```json
        "ProjectId": 1234,
        "NodeId": 1234
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | Forbidden.Wkbenc h.BaselineNoPermi ssion | You are not authorized to access the baseline. | 无对应的基线权限。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 500 | InternalError.Wkbe nch.ServiceError | An internal error occurred. | 服务开小差了。 |
|---|---|---|---|
| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Invalid.Wkbench.Ba selineNotExist | The baseline does not exist. | 基线不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetNodeChildren

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNodeChildre n | 系统规定参数。取值： GetNodeChildren。 |
| NodeId | Long | 是 | 123456878 | 节点ID。您可以进入管控台的运维中心界面，查看节点ID。 |
| ProjectEnv | String | 是 | PROD | 调度运维中心的环境标识。PROD表示生产环境，DEV表示开发环境。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Struct |  | 返回的节点信息列表。 |
|---|---|---|---|
| Nodes | Array of Nodes |  | 节点列表。 |
| BaselineId | Long | 12345656 | 基线ID。 |
| CronExpress | String | 00 00 * * * * | 定时表达式。用于定时调度执行节点任务。 |
| NodeId | Long | 1244564565 | 节点ID。 |
| NodeName | String | 节点名称。 | 节点名称。 |
| OwnerId | String | 123124561341251 321 | 节点Owner的DataWorks UID。 |
| Priority | Integer | 3 | 优先级。取值为1~8，数值越大，优先级越高。 |
| ProgramType | String | ODPS SQL _ | 节点类型。 |
| ProjectId | Long | 12315412412 | 节点所在项目空间的ID。 |
| Repeatability | Boolean | true | 节点任务运行失败是否可重跑。 true，重跑。 false，不重跑。 |
| SchedulerType | String | NORMAL | 调度类型。取值如下： NORMAL，正常调度任务。 MANUAL，手动任务，不会被日常调度。 PAUSE，暂停任务，被日常调度，但启动调度时直接被置为失败。 SKIP，空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| ErrorCode | String | 1060010000000 | 错误码。 |
| ErrorMessage | String | err | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 本次调用的唯一ID。 出现错误后，您可以根据该ID排查问题。 | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |

DataWorks

| Success | Boolean | true | 调用是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
&NodeId=123456878 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 `<RequestId>`本次调用的唯一`ID`。出现错误后，您可以根据该`ID`排查问题。`</RequestId>`

```xml
<HttpStatusCode>200</HttpStatusCode> <Data>
    <Nodes>
        <BaselineId>12345656</BaselineId>
        <Repeatability>true</Repeatability>
        <OwnerId>123124561341251321</OwnerId>
```

`<NodeName>`节点名称。`</NodeName>`

```xml
        <Priority>3</Priority>
        <ProjectId>12315412412</ProjectId>
        <NodeId>1244564565</NodeId>
        <ProgramType>ODPS_SQL</ProgramType>
        <SchedulerType>NORMAL</SchedulerType>
        <CronExpress>00 00 * * * *</CronExpress>
    </Nodes>
</Data> <ErrorCode>1060010000000</ErrorCode> <ErrorMessage>err</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```
{
```

`"RequestId": "`本次调用的唯一`ID`。出现错误后，您可以根据该`ID`排查问题。`",`

```json
    "HttpStatusCode": 200,
    "Data": {
        "Nodes": {
            "BaselineId": 12345656,
            "Repeatability": true,
            "OwnerId": 123124561341251330,
```

`"NodeName": "`节点名称。`",`

```json
            "Priority": 3,
            "ProjectId": 12315412412,
            "NodeId": 1244564565,
            "ProgramType": "ODPS_SQL",
            "SchedulerType": "NORMAL",
            "CronExpress": "00 00 * * * *"
        }
    },
    "ErrorCode": 1060010000000,
    "ErrorMessage": "err",
    "Success": true
}
```

#### GetNodeParents

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNodeParents | 系统规定参数。取值： GetNodeParents。 |
| NodeId | Long | 是 | 1234545621123 4 | 节点ID。您可以进入管控台的运维中心界面，查看节点ID。 |
| ProjectEnv | String | 是 | PROD | 调用GetNodeParents获取节点上游列表。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回的节点信息列表。 |
| Nodes | Array of Nodes |  | 节点列表。 |

| 开发指南·OpenAPI参 | 考 |  | DataWork |
|---|---|---|---|

| BaselineId | Long | 1244564565 | 基线ID。 |
|---|---|---|---|
| CronExpress | String | 定时表达式。用于定时调度执行节点任务。 | 定时表达式。用于定时调度执行节点任务。 |
| NodeId | Long | 1244564565 | 节点ID。 |
| NodeName | String | test Node _ | 节点名称。 |
| OwnerId | String | 123124561341251 321 | 节点Owner的DataWorks UID。 |
| Priority | Integer | 3 | 优先级。取值为1~8，数值越大，优先级越高。 |
| ProgramType | String | ODPS SQL _ | 节点类型。 |
| ProjectId | Long | 12315412412 | 节点所在项目空间的ID。 |
| Repeatability | Boolean | true | 节点任务运行失败是否可重跑。 true，重跑。 false，不重跑。 |
| SchedulerType | String | NORMAL | 调度类型。取值如下： NORMAL，正常调度任务。 MANUAL，手动任务，不会被日常调度。 PAUSE，暂停任务，被日常调度，但启动调度时直接被置为失败。 SKIP，空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| ErrorCode | String | 1060010000000 | 错误码。 |
| ErrorMessage | String | err | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 错误信息。 | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

DataWorks

**示例**

请求示例

```
&NodeId=12345456211234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 `<RequestId>`错误信息。`</RequestId>`

```xml
<HttpStatusCode>200</HttpStatusCode> <Data>
    <Nodes>
        <BaselineId>1244564565</BaselineId>
        <Repeatability>true</Repeatability>
        <OwnerId>123124561341251321</OwnerId>
        <NodeName>test_Node</NodeName>
        <Priority>3</Priority>
        <ProjectId>12315412412</ProjectId>
        <NodeId>1244564565</NodeId>
        <ProgramType>ODPS_SQL</ProgramType>
        <SchedulerType>NORMAL</SchedulerType>
```

`<CronExpress>`定时表达式。用于定时调度执行节点任务。`</CronExpress>`

```xml
    </Nodes>
</Data> <ErrorCode>1060010000000</ErrorCode> <ErrorMessage>err</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```
{
```

`"RequestId": "`错误信息。`",`

```json
    "HttpStatusCode": 200,
    "Data": {
        "Nodes": {
            "BaselineId": 1244564565,
            "Repeatability": true,
            "OwnerId": 123124561341251330,
            "NodeName": "test_Node",
            "Priority": 3,
            "ProjectId": 12315412412,
            "NodeId": 1244564565,
            "ProgramType": "ODPS_SQL",
            "SchedulerType": "NORMAL",
```

`"CronExpress": "`定时表达式。用于定时调度执行节点任务。"

```json
        }
    },
    "ErrorCode": 1060010000000,
    "ErrorMessage": "err",
    "Success": true
}
```

#### GetRemind

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRemind | 系统规定参数。取值：GetRemind。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RemindId | Long | 是 | 1234 | 自定义监控规则的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 自定义监控规则的详情。 |
| AlertInterval | Integer | 1800 | 最小报警间隔，单位为秒。 |
| AlertMethods | List | SMS,MAIL | 报警的方式，包括MAIL（邮件）、SMS（短信）和PHONE（电话，仅DataWorks专业版及以上版本支持）。多个报警方式之间使用英文逗号（,）分隔。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| AlertTargets | List | 952795279527952 7 | 当AlertUnit（报警接收人）为OWNER（节点任务责任人）时，返回空。 当AlertUnit（报警接收人）为OTHER（指定的人）时，返回指定用户的阿里云UID。多个阿里云UID之间使用英文逗号（,）分隔。 |
|---|---|---|---|
| AlertUnit | String | OWNER | 报警接收对象的粒度，包括OWNER（任务责任人）和OTHER（指定的人）。 |
| Baselines | Array of Baselines |  | 当RemindUnit（对象类型）为BASELINE（基线）时，该规则监控的基线列表。 |
| BaselineId | Long | 1234 | 基线的ID。 |
| BaselineName | String | 基线名称 | 基线的名称。 |
| BizProcesses | Array of BizProcesses |  | 当RemindUnit（对象类型）为 BIZPROCESS（业务流程）时，该规则监控的业务流程列表。 |
| BizId | Long | 9527 | 业务流程ID |
| BizProcessNa me | String | 业务流程名称 | 业务流程名称 |

DataWorks

| Detail | String | {"hour":23,"minu": 59} | 当RemindType（触发条件）为 FINISHED（完成）时，返回空。 当RemindType（触发条件）为 UNFINISHED（未完成）时，返回格式为 {"hour":23,"minu":59}。hour的取值范围为0,47，minu的取值范围为0,59。 当RemindType（触发条件）为ERROR（出错）时，返回空。 当RemindType（触发条件）为 CYCLE UNFINISHED（周期未完成）时，返 _ 回格式为 {"1":"05:50","2":"06:50","3":"07:50","4": "08:50","5":"09:50","6":"10:50","7":"11: 50","8":"12:50","9":"13:50","10":"14:50" ,"11":"15:50","12":"16:50","13":"17:50", "14":"18:50","15":"19:50","16":"20:50"," 17":"21:50","18":"22:50","19":"23:50"," 20":"24:50","21":"25:50"}。JSON字符串 key为周期号，取值范围为1,288。value为该周期对应的未完成时间，格式为hh:mm。 hh的取值范围为0,47，mm的取值范围为0,59。 当RemindType（触发条件）为 TIMEOUT（运行超时）时，返回格式为 1800，单位为秒。即从开始运行起，运行超过30分钟触发报警。 |
|---|---|---|---|
| DndEnd | String | 08:00 | 免打扰截止时间，格式为hh:mm。hh的取值范围为0,23，mm的取值范围为0,59。 |
| DndStart | String | 00:00 | 免打扰起始时间，格式为hh:mm。hh的取值范围为0,23，mm的取值范围为0,59。 |
| Founder | String | 9527951795**** | 自定义监控规则创建人的阿里云UID。 |
| MaxAlertTimes | Integer | 3 | 最大报警次数。 |
| Nodes | Array of Nodes |  | 当RemindUnit（对象类型）为NODE（任务节点）时，该规则监控的节点列表。 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 9527951795**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |

DataWorks

| Projects | Array of Projects |  | 当RemindUnit（对象类型）为PROJECT（工作空间）时，该规则监控的工作空间列表。 |
|---|---|---|---|
| ProjectId | Long | 1234 | 工作空间的ID。 |
| RemindId | Long | 1234 | 自定义监控规则的ID。 |
| RemindName | String | 规则名称 | 规则的名称。 |
| RemindType | String | 规则名称 | 触发条件，包括FINISHED（完成）、 UNFINISHED（未完成）、ERROR（出错）、 CYCLE UNFINISHED（周期未完成）和 _ TIMEOUT（运行超时）。 |
| RemindUnit | String | NODE | 对象的类型，包括NODE（任务节点）、 BASELINE（基线）、PROJECT（工作空间）和 BIZPROCESS（业务流程）。 |
| Robots | Array of Robots |  | 钉钉群机器人的webhook地址列表。 |
| AtAll | Boolean | true | 是否@所有人，包括true（是）和false（否）。 |
| WebUrl | String | https://oapi.dingtal k.com/robot/send? access token=**** _ ******************* ******* | 钉钉群机器人的webhook地址。 |
| Useflag | Boolean | true | 自定义监控规则是否开启，包括true（开启）和 false（关闭）。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD-EFGH- IJKLMNOPQ | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

DataWorks 请求示例

```
&RegionId=default &RemindId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFGH-IJKLMNOPQ</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <AlertInterval>1800</AlertInterval>
    <DndStart>00:00</DndStart>
    <RemindId>1234</RemindId>
    <AlertUnit>OWNER</AlertUnit>
    <DndEnd>08:00</DndEnd>
    <RemindUnit>NODE</RemindUnit>
    <Founder>9527951795****</Founder>
    <Useflag>true</Useflag>
    <RemindType>规则名称</RemindType>
    <Detail>{"hour":23,"minu":59}</Detail>
    <MaxAlertTimes>3</MaxAlertTimes>
    <RemindName>规则名称</RemindName>
    <Projects>
        <ProjectId>1234</ProjectId>
    </Projects>
    <BizProcesses>
```

`<BizProcessName>`业务流程名称`</BizProcessName>`

```xml
        <BizId>9527</BizId>
    </BizProcesses>
    <Robots>
        <AtAll>true</AtAll>
        <WebUrl>https://oapi.dingtalk.com/robot/send?
access_token=******************************</WebUrl>
    </Robots>
    <Nodes>
        <Owner>9527951795****</Owner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
        <ProjectId>1234</ProjectId>
        <NodeId>1234</NodeId>
    </Nodes>
    <Baselines>
        <BaselineId>1234</BaselineId>
        <BaselineName>基线名称</BaselineName>
    </Baselines>
    <AlertMethods>SMS,MAIL</AlertMethods>
    <AlertTargets>9527952795279527</AlertTargets>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFGH-IJKLMNOPQ",
    "HttpStatusCode": 200,
    "Data": {
        "AlertInterval": 1800,
        "DndStart": "00:00",
        "RemindId": 1234,
        "AlertUnit": "OWNER",
        "DndEnd": "08:00",
        "RemindUnit": "NODE",
        "Founder": "9527951795****",
        "Useflag": true,
```

`"RemindType": "`规则名称`",`

```json
        "Detail": "{\"hour\":23,\"minu\":59}",
        "MaxAlertTimes": 3,
```

`"RemindName": "`规则名称`",`

```json
        "Projects": {
            "ProjectId": 1234
        },
        "BizProcesses": {
```

`"BizProcessName": "`业务流程名称`",`

```json
            "BizId": 9527
        },
        "Robots": {
            "AtAll": true,
            "WebUrl": "https://oapi.dingtalk.com/robot/send?
access_token=******************************"
        },
        "Nodes": {
            "Owner": "9527951795****",
```

`"NodeName": "`节点名称`",`

```json
            "ProjectId": 1234,
            "NodeId": 1234
        },
        "Baselines": {
            "BaselineId": 1234,
```

`"BaselineName": "`基线名称"

```json
        },
        "AlertMethods": "SMS,MAIL",
        "AlertTargets": 9527952795279528
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetSuccessInstanceTrend

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetSuccessInsta nceTrend | 系统规定参数。取值： GetSuccessInstanceTrend。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceStatus Trend | Struct |  | 分时段实例状态的统计趋势。 |

DataWorks

| AvgTrend | Array of AvgTrend |  | 历史平均趋势。 |
|---|---|---|---|
| Count | Integer | 10 | 实例的数量。 |
| TimePoint | String | 01:00 | 时间点，分别为00:00～23:00。 |
| TodayTrend | Array of TodayTrend |  | 今日趋势。 |
| Count | Integer | 10 | 实例的数量。 |
| TimePoint | String | 01:00 | 时间点，分别为00:00～23:00。 |
| YesterdayTren d | Array of YesterdayTren d |  | 昨日的趋势。 |
| Count | Integer | 10 | 实例的数量。 |
| TimePoint | String | 01:00 | 时间点，分别为00:00～23:00。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetSuccessInstanceTrend &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <InstanceStatusTrend>
    <YesterdayTrend>
        <TimePoint>01:00</TimePoint>
        <Count>10</Count>
    </YesterdayTrend>
    <AvgTrend>
        <TimePoint>01:00</TimePoint>
        <Count>10</Count>
    </AvgTrend>
    <TodayTrend>
        <TimePoint>01:00</TimePoint>
        <Count>10</Count>
    </TodayTrend>
</InstanceStatusTrend>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","InstanceStatusTrend":{"YesterdayTrend": [{"TimePoint":"01:00","Count":"10"}],"AvgTrend": [{"TimePoint":"01:00","Count":"10"}],"TodayTrend": [{"TimePoint":"01:00","Count":"10"}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

DataWorks

| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
|---|---|---|---|
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetTopic

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetTopic | 系统规定参数。取值：GetTopic。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TopicId | Long | 是 | 1234 | 事件的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 事件的详情。 |
| AddTime | Long | 1553524393000 | 事件发现时间戳。 |
| AlertTime | Long | 1553524393000 | 首次报警时间戳。 |
| Assigner | String | 952795**** | 指派人的阿里云UID。 |
| BaselineBuffer | Long | 3600 | 最差基线实例余量，单位为秒。 |
| BaselineId | Long | 1234 | 最差基线实例的基线ID。 |
| BaselineInGro upId | Integer | 1 | 最差基线实例的周期号。 |
| BaselineName | String | 基线名称 | 最差基线实例的基线名称。 |

DataWorks

| BaselineStatus | String | SAFE | 基线的状态，包括ERROR（异常）、SAFE（安全）、DANGROUS（预警）和OVER（破线）。 |
|---|---|---|---|
| Buffer | Long | 1200 | 事件的余量，单位为秒。 |
| DealTime | Long | 1553524393000 | 最后处理时间戳。 |
| DealUser | String | 952795**** | 最后处理人的阿里云UID。 |
| FixTime | Long | 1553524393000 | 事件恢复时间戳。 |
| HappenTime | Long | 1553524393000 | 事件发生的时间戳。事件发生和被发现可能存在时间差。 |
| InstanceId | Long | 12345 | 事件关联的实例ID。 |
| NextAlertTime | Long | 1553524393000 | 下次报警时间戳。 |
| NodeId | Long | 1234 | 事件关联的任务节点ID。 |
| NodeName | String | 节点名称 | 事件关联的任务节点名称。 |
| Owner | String | 952795**** | 事件责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 事件关联任务节点所在工作空间的ID。 |
| TopicId | Long | 1234 | 事件的ID。 |
| TopicName | String | 1234出错 | 事件的名称。 |
| TopicStatus | String | FIXING | 事件的状态，包括IGNORE（已忽略）、 NEW（新发现）、FIXING（处理中）和 RECOVER（已恢复）。 |
| TopicType | String | ERROR | 事件的类型，包括SLOW（变慢）和ERROR（出错）。 |
| ErrorCode | String | 1031203110005 | 错误码。 |

DataWorks

| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD-EFGH- IJKLMNOPQ | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&RegionId=default &TopicId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFGH-IJKLMNOPQ</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Buffer>1200</Buffer>
    <BaselineId>1234</BaselineId>
    <FixTime>1553524393000</FixTime>
    <Owner>952795****</Owner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
    <InstanceId>12345</InstanceId>
    <BaselineStatus>SAFE</BaselineStatus>
    <ProjectId>1234</ProjectId>
    <TopicStatus>FIXING</TopicStatus>
    <AddTime>1553524393000</AddTime>
    <HappenTime>1553524393000</HappenTime>
    <BaselineInGroupId>1</BaselineInGroupId>
    <AlertTime>1553524393000</AlertTime>
    <TopicName>1234出错</TopicName>
    <TopicType>ERROR</TopicType>
    <NextAlertTime>1553524393000</NextAlertTime>
    <DealUser>952795****</DealUser>
    <Assigner>952795****</Assigner>
    <NodeId>1234</NodeId>
    <BaselineName>基线名称</BaselineName>
    <BaselineBuffer>3600</BaselineBuffer>
    <TopicId>1234</TopicId>
    <DealTime>1553524393000</DealTime>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFGH-IJKLMNOPQ",
    "HttpStatusCode": 200,
    "Data": {
        "Buffer": 1200,
        "BaselineId": 1234,
        "FixTime": 1553524393000,
        "Owner": "952795****",
```

`"NodeName": "`节点名称`",`

```json
        "InstanceId": 12345,
        "BaselineStatus": "SAFE",
        "ProjectId": 1234,
        "TopicStatus": "FIXING",
        "AddTime": 1553524393000,
        "HappenTime": 1553524393000,
        "BaselineInGroupId": 1,
        "AlertTime": 1553524393000,
        "TopicName": "1234出错",
        "TopicType": "ERROR",
        "NextAlertTime": 1553524393000,
        "DealUser": "952795****",
        "Assigner": "952795****",
        "NodeId": 1234,
```

`"BaselineName": "`基线名称`",`

```json
        "BaselineBuffer": 3600,
        "TopicId": 1234,
        "DealTime": 1553524393000
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |

DataWorks

| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
|---|---|---|---|
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Wkbe nch.ServiceError | An internal error occurred. | 服务开小差了。 |
| 500 | Invalid.Wkbench.To picNotExist | The topic does not exist. | 事件不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetTopicInfluence

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetTopicInfluenc e | 系统规定参数。取值： GetTopicInfluence。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TopicId | Long | 是 | 1234 | 事件的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 事件影响的基线实例列表。 |
| Influences | Array of Influences |  | 影响的基线实例列表。 |
| BaselineId | Long | 1234 | 基线的ID。 |
| BaselineName | String | 基线名称 | 基线的名称。 |
| Bizdate | Long | 1553356800000 | 基线实例的业务日期时间戳。 |
| Buffer | Long | 360 | 基线实例的余量，单位为秒。 |

DataWorks

| InGroupId | Integer | 1 | 基线实例的周期号。天基线为1，小时基线的取值范围为1,24。 |
|---|---|---|---|
| Owner | String | 952795**** | 基线责任人的阿里云UID。多个责任人之间使用英文逗号（,）分隔。 |
| Priority | Integer | 1 | 基线的优先级，取值范围为{1,2,5,7,8}。 |
| ProjectId | Long | 1234 | 基线所在工作空间的ID。 |
| Status | String | SAFE | 基线的状态，包括ERROR（异常）、SAFE（安全）、DANGROUS（预警）和OVER（破线）。 |
| TopicId | Long | 1234 | 事件的ID。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&RegionId=default &TopicId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TopicId>1234</TopicId>
    <Influences>
        <Buffer>360</Buffer>
        <Status>SAFE</Status>
        <BaselineId>1234</BaselineId>
        <Owner>952795****</Owner>
        <Priority>1</Priority>
        <ProjectId>1234</ProjectId>
        <BaselineName>基线名称</BaselineName>
        <InGroupId>1</InGroupId>
        <Bizdate>1553356800000</Bizdate>
    </Influences>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TopicId": 1234,
        "Influences": {
            "Buffer": 360,
            "Status": "SAFE",
            "BaselineId": 1234,
            "Owner": "952795****",
            "Priority": 1,
            "ProjectId": 1234,
```

`"BaselineName": "`基线名称`",`

```json
            "InGroupId": 1,
            "Bizdate": 1553356800000
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |

DataWorks

| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Wkbe nch.ServiceError | An internal error occurred. | 服务开小差了。 |
| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
| 500 | Invalid.Wkbench.To picNotExist | The topic does not exist. | 事件不存在。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetFileTypeStatistic

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetFileTypeStati stic | 系统规定参数。取值： GetFileTypeStatistic。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括DEV（开发环境） 和PROD（生产环境）。 |
| ProjectId | Long | 是 | 123465 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。 |

DataWorks

| RegionId | String | 是 | default | 区域ID，为固定值default。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ProgramTypeA ndCounts | Array of ProgramTypeA ndCount |  | 节点的类型和数量。 |
| Count | Integer | 1 | 节点的数量。 |
| ProgramType | String | ODPS SQL _ | 节点的类型。 常用的类型如下： 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| RequestId | String | SDFSDFSDF- SDFSDF-SDFDSF- SDFSDF | 请求的ID，用于定位日志，排查问题。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetFileTypeStatistic &ProjectEnv=PROD &ProjectId=123465 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>SDFSDFSDF-SDFSDF-SDFDSF-SDFSDF</RequestId> <ProgramTypeAndCounts>
    <Count>1</Count>
    <ProgramType>ODPS_SQL</ProgramType>
</ProgramTypeAndCounts>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "SDFSDFSDF-SDFSDF-SDFDSF-SDFSDF",
    "ProgramTypeAndCounts": {
        "Count": 1,
        "ProgramType": "ODPS_SQL"
    }
}
```

#### ListFileType

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProjectId | Long | Body | 否 | 10000 | DataWorks工作空间的 ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。该参数与 ProjectIdentifier参数，二者必须设置其一，用来确定本次API调用操作的 DataWorks工作空间。 |
| RegionId | Strin g | Host | 是 |  | 区域ID，为固定值default 。 |
| ProjectIde ntifier | Strin g | Body | 否 | dw project _ | DataWorks工作空间名称。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间名称。 该参数与 ProjectId参数，二者必须设置其一，用来确定本次API 调用操作的DataWorks工作空间。 |
| PageNum ber | Integ er | Body | 是 | 1 | 请求数据的页码数。 |
| PageSize | Integ er | Body | 是 | 50 | 每页显示的数据条数，最大值为100。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Keyword | Strin g | Body | 否 | ODPS SQL | 节点类型的名称。您可以登录DataWorks控制台，进入数据开发界面，在左侧导航栏查看某类型节点的名称。配置说明如下： 支持查看中英文名称，但该参数查看的名称语言需要与Locale参数的语言类型一致。 支持模糊搜索。 如果不配置该参数，则会返回所有节点类型的名称。 |
| Locale | Strin g | Body | 否 | zh-CN | 选择查询的语言，支持查询 zh-CN和en-US语言的节点类型信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求ID。用于出现错误后排查问题。 |
| NodeTypeInfoL ist | Struct |  | 返回的节点类型信息列表。 |
| -NodeTypeInfo | Array |  | 单个节点类型的信息。 |
| -- NodeTypeNam e | String | ODPS SQL | 节点类型的名称。 常用的代码及名称类型对应关系如下： 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --NodeType | Integer | 10 | 节点类型的Code信息。 常用的代码及名称类型对应关系如下： 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| -PageNumber | Integer | 1 | 当前数据页的页码。 |
| -PageSize | Integer | 50 | 当前数据页显示的数据条数。 |
| -TotalCount | Integer | 127 | 满足查询条件的数据总条数。 |

**示例**

请求示例

```
&RegionId= &PageNumber=1 &PageSize=50
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "NodeTypeInfoList":{
  "-NodeTypeInfo":{
   "NodeTypeName":"ODPS SQL",
   "NodeType":10
  },
  "TotalCount":127,
  "PageSize":50,
  "PageNumber":1
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <NodeTypeInfoList>
 <-NodeTypeInfo>
  <NodeTypeName>ODPS SQL</NodeTypeName>
  <NodeType>10</NodeType>
 </-NodeTypeInfo>
 <TotalCount>127</TotalCount>
 <PageSize>50</PageSize>
 <PageNumber>1</PageNumber>
</NodeTypeInfoList>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |

#### ListAlertMessages

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListAlertMessag es | 系统规定参数。取值： ListAlertMessages。 |
| BeginTime | String | 是 | 2020-04- 02T00:00:00+0 800 | 起始报警时间，需要使用yyyy-MM- dd'T'HH:mm:ssZ的UTC格式。 |
| EndTime | String | 是 | 2020-04- 04T00:00:00+0 800 | 截止报警时间，需要使用yyyy-MM- dd'T'HH:mm:ssZ的UTC格式。 |

DataWorks

| PageNumber | Integer | 是 | 1 | 分页的页数。默认值为1、最小值为1、最大值为30。 |
|---|---|---|---|---|
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10，最大100 条。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RemindId | Long | 否 | 9527 | 自定义规则的ID，当AlertRuleTypes（报警规则类型）包括USER DEFINE自定义 _ 规则时生效。 |
| AlertMethods | String | 否 | SMS,MAIL,PHON E | 报警方式，包括MAIL（邮件）、SMS（短信）和PHONE（电话，仅DataWorks专业版及以上版本支持）。多个报警方式之间使用英文逗号（,）分隔。 |
| AlertUser | String | 否 | 123456 | 报警接收人的阿里云UID。 |
| AlertRuleTypes | String | 否 | 否 GLOBAL,USER D _ EFINE,OHTER | 规则类型，包括GLOBAL（全局规则）、 USER DEFINE（自定义规则）和 _ OTHER（其它）。多个规则类型之间使用英文逗号（,）分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回的报警信息列表。 |
| AlertMessages | Array of AlertMessages |  | 报警信息列表。 |
| AlertId | Long | 1234 | 报警ID。 |
| AlertMessageS tatus | String | READY TO SEND _ _ | 发送状态，包括READY TO SEND（准备发 _ _ 送）、SEND FAIL（发送失败）、 _ SEND SUCCESS（发送成功）和 _ SEND OVERLIMIT（报警超限）。 _ |
| AlertMethod | String | SMS | 报警方式，包括MAIL（邮件）、SMS（短信） 和 PHONE（电话，仅DataWorks专业版及以上版本支持）。 |
| AlertTime | Long | 1553531401000 | 报警的时间戳。 |

DataWorks

| AlertUser | String | 9527952795**** | 接收人的阿里云UID。 |
|---|---|---|---|
| Content | String | 节点出错 | 报警的内容。 |
| Instances | Array of Instances |  | 当Source（报警来源）为REMIND ALERT（自 _ 定义提醒）时，返回触发自定义监控规则的实例列表。其它类型的报警来源返回为空。 |
| InstanceId | Long | 12345 | 实例的ID。 |
| NodeId | Long | 12345 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| Status | String | NOT RUN _ | 实例状态，包括NOT RUN （未运行）、 _ WAIT TIME（等待时间）、 _ WAIT RESOURCE（等待资源）、 _ RUNNING（运行中）、CHECKING（校检中）、CHECKING CONDITION（条件检测 _ 中）、FAILURE（运行失败）和SUCCESS（运行成功）。 |
| Nodes | Array of Nodes |  | 不同的报警来源返回不同的节点列表： 当Source（报警来源）为NODE _ CYCLE ALERT（节点成环报警）时，返回成 _ 环的节点类型。 当Source（报警来源）为 NODE LONELY ALERT（节点孤立报警） _ _ 时，返回孤立的节点类型。 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 95279527952**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| RemindId | Long | 1234 | 当Source（报警来源）为REMIND ALERT（自 _ 定义报警）时，返回触发的自定义监控规则ID。 |

DataWorks

| RemindName | String | 自定义监控规则名称 | 当Source（报警来源）为REMIND ALERT（自 _ 定义提醒）时，返回触发的自定义监控规则名称。 |
|---|---|---|---|
| SlaAlert | Struct |  | 当Source（报警来源）为SLA ALERT（基线报 _ 警）时，返回触发基线预警的基本实例信息。当报警来源为其它类型时，返回为空。 |
| BaselineId | Long | 1234 | 基线的ID。 |
| BaselineName | String | 基线名称 | 基线的名称。 |
| BaselineOwner | String | 952795279**** | 基线责任人的阿里云UID，多个UID之间使用英文逗号（,）分隔。 |
| Bizdate | Long | 1553443200000 | 基线实例的业务日期时间戳。 |
| InGroupId | Integer | 1 | 基线实例的周期号：天基线为1，小时基线范围为1,24。 |
| ProjectId | Long | 1234 | 基线所在工作空间的ID。 |
| Status | String | SAFE | 基线状态，包括ERROR（异常）、SAFE（安全）、DANGROUS（预警）和OVER（破线）。 |
| Source | String | REMIND ALERT _ | 报警来源，包括REMIND ALERT（自定义报 _ 警）、TOPIC ALERT（事件告警）、 _ SLA ALERT（基线预警）、 _ NODE CYCLE ALERT（节点成环报警）和 _ _ NODE LONELY ALERT（节点孤立报警）。 _ _ |
| Topics | Array of Topics |  | 当Source（报警来源）为TOPIC ALERT（全局 _ 事件告警）时，返回触发报警的事件列表。当报警来源为其它类型时，返回结果为空。 |
| InstanceId | Long | 12345 | 事件关联的实例ID。 |
| NodeId | Long | 12345 | 事件关联的节点ID。 |
| TopicId | Long | 12345 | 事件的ID。 |
| TopicName | String | 9527出错 | 事件的名称。 |

DataWorks

| TopicOwner | String | 9527952795**** | 事件责任人的阿里云UID。 |
|---|---|---|---|
| TopicStatus | String | FIXING | 事件状态，包括IGNORE（已忽略），NEW（新发现）、 FIXING（处理中）和RECOVER（已恢复）。 |
| PageNumber | String | 1 | 当前的页数。 |
| PageSize | String | 10 | 每页的大小。 |
| TotalCount | String | 100 | 报警信息的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&BeginTime=2020-04-02T00:00:00+0800 &EndTime=2020-04-04T00:00:00+0800 &PageNumber=1 &PageSize=10 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <AlertMessages>
        <AlertMessageStatus>READY_TO_SEND</AlertMessageStatus>
        <AlertUser>9527952795****</AlertUser>
        <RemindId>1234</RemindId>
        <AlertId>1234</AlertId>
```

`<Content>`节点出错`</Content>`

```xml
        <AlertMethod>SMS</AlertMethod>
        <Source>REMIND_ALERT</Source>
        <AlertTime>1553531401000</AlertTime>
```

`<RemindName>`自定义监控规则名称`</RemindName>`

```xml
        <Instances>
            <Status>NOT_RUN</Status>
            <InstanceId>12345</InstanceId>
```

`<NodeName>`节点名称`</NodeName>`

```xml
            <ProjectId>1234</ProjectId>
            <NodeId>12345</NodeId>
        </Instances>
        <Nodes>
            <Owner>95279527952****</Owner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
            <ProjectId>1234</ProjectId>
            <NodeId>1234</NodeId>
        </Nodes>
        <Topics>
            <TopicOwner>9527952795****</TopicOwner>
            <InstanceId>12345</InstanceId>
            <NodeId>12345</NodeId>
            <TopicId>12345</TopicId>
            <TopicStatus>FIXING</TopicStatus>
            <TopicName>9527出错</TopicName>
        </Topics>
        <SlaAlert>
            <Status>SAFE</Status>
            <BaselineId>1234</BaselineId>
            <BaselineOwner>952795279****</BaselineOwner>
            <ProjectId>1234</ProjectId>
            <BaselineName>基线名称</BaselineName>
            <InGroupId>1</InGroupId>
            <Bizdate>1553443200000</Bizdate>
        </SlaAlert>
    </AlertMessages>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

| { "RequestId": "0000-ABCD-EFG****", "HttpStatusCode": 200, "Data": { "TotalCount": 100, "PageSize": 10, "PageNumber": 1, "AlertMessages": { "AlertMessageStatus": "READY TO SEND", _ _ "AlertUser": "9527952795****", "RemindId": 1234, "AlertId": 1234, "Content": "节点出错", "AlertMethod": "SMS", "Source": "REMIND ALERT", _ "AlertTime": 1553531401000, "RemindName": "自定义监控规则名称", "Instances": { "Status": "NOT RUN", _ "InstanceId": 12345, "NodeName": "节点名称", "ProjectId": 1234, "NodeId": 12345 }, "Nodes": { "Owner": "95279527952****", "NodeName": "节点名称", "ProjectId": 1234, "NodeId": 1234 }, "Topics": { "TopicOwner": "9527952795****", "InstanceId": 12345, "NodeId": 12345, "TopicId": 12345, "TopicStatus": "FIXING", "TopicName": "9527出错" }, "SlaAlert": { "Status": "SAFE", "BaselineId": 1234, "BaselineOwner": "952795279****", "ProjectId": 1234, "BaselineName": "基线名称", "InGroupId": 1, "Bizdate": 1553443200000 } } }, "ErrorCode": "Invalid.Tenant.ConnectionNotExists", "ErrorMessage": "The specified parameters are invalid.", "Success": true } |  |
|---|---|

DataWorks

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### ListBaselineConfigs

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListBaselineConf igs | 系统规定参数。取值： ListBaselineConfigs。 |
| PageNumber | Integer | 是 | 1 | 分页的页数。默认值为1，最小值为1，最大值为30。 |
| PageSize | Integer | 是 | 10 | 每页返回的数据行数。默认值为10，最小值为1，最大值为100。 |

DataWorks

| ProjectId | Long | 是 | 1234 | 工作空间的ID。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Owner | String | 否 | 95279527**** | 基线责任人阿里云UID。 |
| Priority | String | 否 | 1,3,5,7,8 | 基线的优先级，取值范围为{1,3,5,7,8} 。多个优先级之间使用英文逗号（,）分隔。 |
| Useflag | Boolean | 否 | true | 是否开启，包括true（开启）和false（未开启）。 |
| BaselineTypes | String | 否 | DAILY,HOURLY | 基线类型，包括DAILY（天基线）和 HOURLY（小时基线）。多个类型之间使用英文逗号（,）分隔。 |
| SearchText | String | 否 | 基线名称搜索关键字 | 基线名称的搜索关键字。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回的基线列表。 |
| Baselines | Array of Baselines |  | 基线列表。 |
| BaselineId | Long | 1234 | 基线的ID。 |
| BaselineName | String | 基线名称 | 基线的名称。 |
| BaselineType | String | DAILY | 基线类型，包括DAILY（天基线）和 HOURLY（小时基线）。 |
| ExpHour | Integer | 7 | 天基线的预警小时，取值范围为0, 47。 |
| ExpMinu | Integer | 30 | 天基线的预警分钟，取值范围为0, 59。 |

DataWorks

| HourExpDetail | String | {"1":"03:28","2":"0 4:28","3":"05:28"," 4":"06:28","5":"07: 28","6":"08:28","7": "09:28","8":"10:28" ,"9":"11:28","10":"1 2:28","11":"13:28", "12":"14:28","13":" 15:28","14":"16:28 ","15":"17:28","16": "18:28","17":"19:2 8","18":"20:28","19 ":"21:28","20":"22: 28","21":"23:28","2 2":"24:28","23":"25 :28","24":"26:28"} | 小时基线的预警时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为0,47，mm的取值范围为0,59。 |
|---|---|---|---|
| HourSlaDetail | String | {"1":"03:58","2":"0 4:58","3":"05:58"," 4":"06:58","5":"07: 58","6":"08:58","7": "09:58","8":"10:58" ,"9":"11:58","10":"1 2:58","11":"13:58", "12":"14:58","13":" 15:58","14":"16:58 ","15":"17:58","16": "18:58","17":"19:5 8","18":"20:58","19 ":"21:58","20":"22: 58","21":"23:58","2 2":"24:58","23":"25 :58","24":"26:58"} | 小时基线的承诺时间配置（JSON格式），key为周期号，value为hh:mm格式。hh的取值范围为0,47，mm的取值范围为0,59。 |
| IsDefault | Boolean | true | 是否为工作空间的默认基线，包括true（是）和 false（否）。 |
| Owner | String | 952795**** | 基线责任人的阿里云UID。有多个责任人时，使用英文逗号（,）分隔。 |
| Priority | Integer | 1 | 基线的优先级，取值集合为{1,3,5,7,8}。 |
| ProjectId | Long | 9527 | 基线所在工作空间的ID。 |
| SlaHour | Integer | 9 | 天基线的承诺小时，取值范围为0, 47。 |
| SlaMinu | Integer | 30 | 天基线的预警分钟，取值范围为0, 59。 |
| UseFlag | Boolean | true | 基线是否开启，包括true（开启）和false（未开启）。 |
| PageNumber | Integer | 1 | 当前的页数。 |

DataWorks

| PageSize | Integer | 10 | 每页的大小。 |
|---|---|---|---|
| TotalCount | Integer | 100 | 基线的总数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListBaselineConfigs &PageNumber=1 &PageSize=10 &ProjectId=1234 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```json
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Baselines>
        <IsDefault>true</IsDefault>
        <BaselineId>1234</BaselineId>
        <HourSlaDetail>
{"1":"03:58","2":"04:58","3":"05:58","4":"06:58","5":"07:58","6":"08:58","7":"09:58","8": 0:58","9":"11:58","10":"12:58","11":"13:58","12":"14:58","13":"15:58","14":"16:58","15":" :58","16":"18:58","17":"19:58","18":"20:58","19":"21:58","20":"22:58","21":"23:58","22":" :58","23":"25:58","24":"26:58"}</HourSlaDetail>
        <ExpHour>7</ExpHour>
        <ExpMinu>30</ExpMinu>
        <Owner>952795****</Owner>
        <SlaHour>9</SlaHour>
        <Priority>1</Priority>
        <SlaMinu>30</SlaMinu>
        <HourExpDetail>
{"1":"03:28","2":"04:28","3":"05:28","4":"06:28","5":"07:28","6":"08:28","7":"09:28","8": 0:28","9":"11:28","10":"12:28","11":"13:28","12":"14:28","13":"15:28","14":"16:28","15":" :28","16":"18:28","17":"19:28","18":"20:28","19":"21:28","20":"22:28","21":"23:28","22":" :28","23":"25:28","24":"26:28"}</HourExpDetail>
        <ProjectId>9527</ProjectId>
        <UseFlag>true</UseFlag>
        <BaselineType>DAILY</BaselineType>
        <BaselineName>基线名称</BaselineName>
    </Baselines>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "Baselines": {
            "IsDefault": true,
            "BaselineId": 1234,
            "HourSlaDetail": "
{\"1\":\"03:58\",\"2\":\"04:58\",\"3\":\"05:58\",\"4\":\"06:58\",\"5\":\"07:58\",\"6\":\" :58\",\"7\":\"09:58\",\"8\":\"10:58\",\"9\":\"11:58\",\"10\":\"12:58\",\"11\":\"13:58\",\ 2\":\"14:58\",\"13\":\"15:58\",\"14\":\"16:58\",\"15\":\"17:58\",\"16\":\"18:58\",\"17\": 19:58\",\"18\":\"20:58\",\"19\":\"21:58\",\"20\":\"22:58\",\"21\":\"23:58\",\"22\":\"24:5 ",\"23\":\"25:58\",\"24\":\"26:58\"}",
            "ExpHour": 7,
            "ExpMinu": 30,
            "Owner": "952795****",
            "SlaHour": 9,
            "Priority": 1,
            "SlaMinu": 30,
            "HourExpDetail": "
{\"1\":\"03:28\",\"2\":\"04:28\",\"3\":\"05:28\",\"4\":\"06:28\",\"5\":\"07:28\",\"6\":\" :28\",\"7\":\"09:28\",\"8\":\"10:28\",\"9\":\"11:28\",\"10\":\"12:28\",\"11\":\"13:28\",\ 2\":\"14:28\",\"13\":\"15:28\",\"14\":\"16:28\",\"15\":\"17:28\",\"16\":\"18:28\",\"17\": 19:28\",\"18\":\"20:28\",\"19\":\"21:28\",\"20\":\"22:28\",\"21\":\"23:28\",\"22\":\"24:2 ",\"23\":\"25:28\",\"24\":\"26:28\"}",
            "ProjectId": 9527,
            "UseFlag": true,
            "BaselineType": "DAILY",
```

`"BaselineName": "`基线名称"

```json
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |

DataWorks

| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
|---|---|---|---|
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### ListBaselineStatuses

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListBaselineStat uses | 系统规定参数。取值： ListBaselineStatuses。 |
| Bizdate | String | 是 | 2020-07- 07T00:00:00+0 800 | 业务日期，需要使用UTC格式（yyyy- MM-dd'T'HH:mm:ssZ）。 |
| PageNumber | Integer | 是 | 1 | 分页的页数。默认值为1，最小值为1，最大值为30。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认值为10，最大值为 100。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Priority | String | 否 | 1,3,5,7,8 | 基线的优先级，取值范围为{1,3,5,7,8}。 多个优先级之间使用英文逗号（,）分隔。 |
| SearchText | String | 否 | 基线名称搜索关键字 | 基线名称搜索关键字。 |
| Owner | String | 否 | 9527952795**** | 基线责任人的阿里云UID。 |

DataWorks

| TopicId | Long | 否 | 1234 | 相关事件的ID。 |
|---|---|---|---|---|
| FinishStatus | String | 否 | FINISH,UNFINISH | 基线实例是否完成，包括UNFINISH（未完成）、FINISH（已完成）。多个状态之间使用英文逗号（,）分隔。 |
| Status | String | 否 | SAFE,DANGROU S,OVER | 基线的状态，包括ERROR（异常）、 SAFE（安全）、DANGROUS（预警）和 OVER（破线）。多个状态之间使用英文逗号（,）分隔。 |
| BaselineTypes | String | 否 | DAILY,HOURLY | 基线的类型，包括DAILY（天基线）和 HOURLY（小时基线）。多个类型之间使用英文逗号（,）分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回的基线实例列表。 |
| BaselineStatus es | Array of BaselineStatus es |  | 基线实例列表。 |
| BaselineId | Long | 1234 | 基线的ID。 |
| BaselineName | String | 基线名称 | 基线的名称。 |
| Bizdate | Long | 1553443200000 | 业务日期时间戳。 |
| Buffer | Long | 1800 | 基线实例的余量，单位为秒。 |
| EndCast | Long | 1553531400000 | 基线实例的预计完成时间。 |
| ExpTime | Long | 1553531400000 | 基线实例的预警时间。 |
| FinishStatus | String | UNFINISH | 基线实例是否完成，包括UNFINISH（未完成） 和FINISH（已完成）。 |
| FinishTime | Long | 1553531400000 | 当FinishStatus（基线实例完成状态）为 FINISH（已完成）时，返回基线实例的完成时间戳。 |

DataWorks

| InGroupId | Integer | 1 | 基线实例的周期号。天基线为1，小时基线的取值范围为1,24。 |
|---|---|---|---|
| Owner | String | 9527952795**** | 基线责任人的阿里云UID。多个责任人之间使用英文逗号（,）分隔。 |
| Priority | Integer | 1 | 基线的优先级，取值范围为{1,2,5,7,8}。 |
| ProjectId | Long | 1234 | 基线所在工作空间的ID。 |
| SlaTime | Long | 1553531400000 | 基线实例的实际完成时间。 |
| Status | String | SAFE | 基线的状态，包括ERROR（异常）、SAFE（安全）、DANGROUS（预警）和OVER（破线）。 |
| PageNumber | Integer | 1 | 当前的页数。 |
| PageSize | Integer | 10 | 每页的大小。 |
| TotalCount | Integer | 100 | 基线实例的总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListBaselineStatuses &Bizdate=2020-07-07T00:00:00+0800 &PageNumber=1 &PageSize=10 &RegionId=default
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <BaselineStatuses>
        <Status>SAFE</Status>
        <Buffer>1800</Buffer>
        <BaselineId>1234</BaselineId>
        <Owner>9527952795****</Owner>
        <Priority>1</Priority>
        <FinishStatus>UNFINISH</FinishStatus>
        <ProjectId>1234</ProjectId>
        <InGroupId>1</InGroupId>
        <ExpTime>1553531400000</ExpTime>
        <Bizdate>1553443200000</Bizdate>
        <FinishTime>1553531400000</FinishTime>
        <BaselineName>基线名称</BaselineName>
        <SlaTime>1553531400000</SlaTime>
        <EndCast>1553531400000</EndCast>
    </BaselineStatuses>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "BaselineStatuses": {
            "Status": "SAFE",
            "Buffer": 1800,
            "BaselineId": 1234,
            "Owner": "9527952795****",
            "Priority": 1,
            "FinishStatus": "UNFINISH",
            "ProjectId": 1234,
            "InGroupId": 1,
            "ExpTime": 1553531400000,
            "Bizdate": 1553443200000,
            "FinishTime": 1553531400000,
```

`"BaselineName": "`基线名称`",`

```json
            "SlaTime": 1553531400000,
            "EndCast": 1553531400000
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |

DataWorks

| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### ListDataServicePublishedApis

调用ListDataServicePublishedApis获取数据服务API的发布态信息列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataServiceP ublishedApis | 系统规定参数。取值： ListDataServicePublishedApis。 |
| PageNumber | Integer | 是 | 1 | 页码，从1开始，默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectId | Long | 是 | 10000 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10001 | 租户ID。 |
| ApiNameKeywor d | String | 否 | 我的API名称 | API名称的关键词，过滤得到API名称包含该关键词的API。 |
| ApiPathKeyword | String | 否 | /test/ | API路径的关键词，过滤得到API路径包含该关键词的API。 |
| CreatorId | String | 否 | 12345 | API创建者的阿里云ID，过滤得到该用户创建的API。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | API发布态信息返回。 |
| Apis | Array of Api |  | API发布态信息列表。 |

DataWorks

| ApiId | Long | 10002 | API的ID。 |
|---|---|---|---|
| ApiMode | Integer | 0 | API的类型，可选枚举值包括0（向导API）、 1（脚本API）和2（注册API）。 |
| ApiName | String | 我的API名称 | API的名称。 |
| ApiPath | String | /test/1 | API的路径。 |
| CreatedTime | String | 2020-06- 23T00:21:01+0800 | 创建时间。 |
| CreatorId | String | 1234567 | 创建人的阿里云ID。 |
| Description | String | 测试API描述 | 描述信息。 |
| GroupId | String | ab123 | 分组ID。 |
| ModifiedTime | String | 2020-06- 23T00:21:01+0800 | 最新修改时间。 |
| OperatorId | String | 2345678 | 最新编辑人阿里云ID |
| ProjectId | Long | 10000 | 工作空间的ID。 |
| Protocols | List | 0 | API协议，可选枚举值包括0（HTTP）和 1（HTTPS）。 |
| RegistrationDe tails | Struct |  | 注册API详情，只有注册API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| RegistrationErr orCodes | Array of RegistrationErr orCode |  | 注册API的错误码列表。 |
| ErrorCode | String | 1001 | 错误码 |
| ErrorMessage | String | fail to call | 错误信息 |
| ErrorSolution | String | retry | 错误解决方案 |

DataWorks

| RegistrationRe questParamet ers | Array of RegistrationRe questParamet er |  | 注册API的请求参数列表。 |
|---|---|---|---|
| DefaultValue | String | default1 | 默认值 |
| ExampleValue | String | example1 | 示例值 |
| IsRequiredPar ameter | Boolean | true | 是否必填 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean |
| ParameterDes cription | String | description1 | 描述 |
| ParameterNa me | String | name1 | 参数名称 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值有： 0：Equal 1：Like 2：Const 3：In 向导API支持Equal、Like、In；脚本API支持 Equal；注册API支持Equal、Const。 |
| ParameterPosi tion | Integer | 0 | 参数位置，可选枚举值有： 0：Path 1：Query 2：Head 3：Body 向导和脚本API，只支持Query；注册 API，GET、DELETE方法支持Query、 Head，PUT、POST方法支持Query、Head、 Body。 |
| ServiceConten tType | Integer | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API支持 JSON，注册API支持JSON和XML。 |

DataWorks

| ServiceHost | String | http://www.abc.co m | 后端服务地址。 |
|---|---|---|---|
| ServicePath | String | /index | 后端服务路径。 |
| ServiceReques tBodyDescripti on | String | {"abc":1} | 后端请求body内容的描述。 |
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |
| RequestMetho d | Integer | 0 | API的请求方式，可选枚举值包括0（GET）、 1（POST）、2（PUT）和3（DELTE）。向导和脚本API支持GET和POST。注册API支持 GET、POST、PUT和DELETE。 |
| ResponseCont entType | Integer | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API支持 JSON，注册API支持JSON和XML。 |
| ScriptDetails | Struct |  | 脚本API详情，只有脚本API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例 |
| IsPagedRespo nse | Boolean | true | 返回是否分页 |
| Script | String | select a from t | QL脚本 |
| ScriptConnecti on | Struct |  | 脚本API数据源信息 |
| ConnectionId | Long | 123 | 数据源ID |
| TableName | String | t | 数据源表名 |
| ScriptErrorCod es | Array of ScriptErrorCod e |  | 脚本API错误码列表 |
| ErrorCode | String | 1001 | 错误码 |
| ErrorMessage | String | fail to call | 错误信息 |
| ErrorSolution | String | retry | 错误解决方案 |

DataWorks

| ScriptRequest Parameters | Array of ScriptRequest Parameter |  | 脚本API请求参数列表 |
|---|---|---|---|
| DefaultValue | String | default1 | 默认值 |
| ExampleValue | String | example1 | 示例值 |
| IsRequiredPar ameter | Boolean | true | 是否必填 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean |
| ParameterDes cription | String | description1 | 描述 |
| ParameterNa me | String | param1 | 参数名称 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值有： 0：Equal 1：Like 2：Const 3：In 向导API支持Equal、Like、In；脚本API支持 Equal；注册API支持Equal、Const。 |
| ParameterPosi tion | Integer | 0 | 参数位置，可选枚举值有： 0：Path 1：Query 2：Head 3：Body 向导和脚本API，只支持Query；注册 API，GET、DELETE方法支持Query、 Head，PUT、POST方法支持Query、Head、 Body。 |
| ScriptRespons eParameters | Array of ScriptRespons eParameter |  | 脚本API返回参数列表 |

DataWorks

| ExampleValue | String | example2 | 示例值 |
|---|---|---|---|
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean |
| ParameterDes cription | String | description2 | 描述 |
| ParameterNa me | String | param2 | 参数名称 |
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例 |
| Status | Integer | 1 | API的状态，可选枚举值包括0（未发布）和 1（已发布）。 |
| TenantId | Long | 10001 | 租户ID。 |
| Timeout | Integer | 10000 | 超时时间，单位毫秒ms |
| VisibleRange | Integer | 0 | 可见范围，可选枚举值包括0（工作空间）和 1（私有）。 |
| WizardDetails | Struct |  | 向导API详情，只有向导API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |
| WizardConnec tion | Struct |  | 向导API的数据源信息。 |
| ConnectionId | Long | 123 | 数据源ID。 |
| TableName | String | 1 | 数据源的表名称。 |

DataWorks

| WizardErrorCo des | Array of WizardErrorCo de |  | 向导API的错误码列表。 |
|---|---|---|---|
| ErrorCode | String | 1001 | 错误码。 |
| ErrorMessage | String | fail to call | 错误信息。 |
| ErrorSolution | String | retry | 错误解决方案。 |
| WizardReques tParameters | Array of WizardReques tParameter |  | 向导API的请求参数列表。 |
| DefaultValue | String | default1 | 默认值。 |
| ExampleValue | String | example1 | 示例值。 |
| IsRequiredPar ameter | Boolean | true | 是否必填。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description1 | 描述信息。 |
| ParameterNa me | String | param1 | 参数的名称。 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值包括0（Equal）、 1（Like）、2（Const）和3（In）。向导模式 API支持Equal、Like和In，脚本模式API支持 Equal，注册API支持Equal和Const。 |
| ParameterPosi tion | Integer | 0 | 参数的位置，可选枚举值包括0（Path）、 1（Query）、2（Head）和3（Body）。向导和脚本API仅支持Query。注册API中的GET、 DELETE方法支持Query、Head，PUT、POST 方法支持Query、Head和Body。 |
| WizardRespon seParameters | Array of WizardRespon seParameter |  | 向导API的返回参数列表。 |
| ExampleValue | String | example2 | 示例值。 |

DataWorks

| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
|---|---|---|---|
| ParameterDes cription | String | description2 | 描述信息。 |
| ParameterNa me | String | param2 | 参数的名称。 |
| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Integer | 100 | 总记录数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServicePublishedApis &PageNumber=1 &PageSize=10 &ProjectId=10000 &RegionId=default &TenantId=10001
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
```

DataWorks

```xml
    <Apis>
        <Status>1</Status>
        <VisibleRange>0</VisibleRange>
        <Description>测试API描述</Description>
        <CreatedTime>2020-06-23T00:21:01+0800</CreatedTime>
```

`<ApiName>`我的`API`名称`</ApiName>`

```xml
        <Timeout>10000</Timeout>
        <RequestMethod>0</RequestMethod>
        <CreatorId>1234567</CreatorId>
        <ProjectId>10000</ProjectId>
        <ResponseContentType>0</ResponseContentType>
        <OperatorId>2345678</OperatorId>
        <GroupId>ab123</GroupId>
        <TenantId>10001</TenantId>
        <ModifiedTime>2020-06-23T00:21:01+0800</ModifiedTime>
        <ApiMode>0</ApiMode>
        <ApiId>10002</ApiId>
        <ApiPath>/test/1</ApiPath>
        <Protocols>0</Protocols>
        <RegistrationDetails>
            <ServiceRequestBodyDescription>{"abc":1}</ServiceRequestBodyDescription>
            <SuccessfulResultSample>{"success": true}</SuccessfulResultSample>
            <ServiceContentType>0</ServiceContentType>
            <ServicePath>/index</ServicePath>
            <FailedResultSample>{"success": false}</FailedResultSample>
            <ServiceHost>http://www.abc.com</ServiceHost>
            <RegistrationErrorCodes>
                <ErrorCode>1001</ErrorCode>
                <ErrorSolution>retry</ErrorSolution>
                <ErrorMessage>fail to call</ErrorMessage>
            </RegistrationErrorCodes>
            <RegistrationRequestParameters>
                <DefaultValue>default1</DefaultValue>
                <ExampleValue>example1</ExampleValue>
                <ParameterDataType>0</ParameterDataType>
                <ParameterPosition>0</ParameterPosition>
                <ParameterName>name1</ParameterName>
                <ParameterOperator>0</ParameterOperator>
                <ParameterDescription>description1</ParameterDescription>
                <IsRequiredParameter>true</IsRequiredParameter>
            </RegistrationRequestParameters>
        </RegistrationDetails>
        <ScriptDetails>
            <Script>select a from t</Script>
            <IsPagedResponse>true</IsPagedResponse>
            <SuccessfulResultSample>{"success": true}</SuccessfulResultSample>
            <FailedResultSample>{"success": false}</FailedResultSample>
            <ScriptErrorCodes>
                <ErrorCode>1001</ErrorCode>
                <ErrorSolution>retry</ErrorSolution>
                <ErrorMessage>fail to call</ErrorMessage>
            </ScriptErrorCodes>
            <ScriptResponseParameters>
                <ExampleValue>example2</ExampleValue>
```

P t

```
DtT 0/P
```

t

```
DtT
```

DataWorks

```xml
                <ParameterDataType>0</ParameterDataType>
                <ParameterName>param2</ParameterName>
                <ParameterDescription>description2</ParameterDescription>
            </ScriptResponseParameters>
            <ScriptRequestParameters>
                <DefaultValue>default1</DefaultValue>
                <ExampleValue>example1</ExampleValue>
                <ParameterDataType>0</ParameterDataType>
                <ParameterPosition>0</ParameterPosition>
                <ParameterName>param1</ParameterName>
                <ParameterOperator>0</ParameterOperator>
                <ParameterDescription>description1</ParameterDescription>
                <IsRequiredParameter>true</IsRequiredParameter>
            </ScriptRequestParameters>
            <ScriptConnection>
                <TableName>t</TableName>
                <ConnectionId>123</ConnectionId>
            </ScriptConnection>
        </ScriptDetails>
        <WizardDetails>
            <IsPagedResponse>true</IsPagedResponse>
            <SuccessfulResultSample>{"success": true}</SuccessfulResultSample>
            <FailedResultSample>{"success": false}</FailedResultSample>
            <WizardErrorCodes>
                <ErrorCode>1001</ErrorCode>
                <ErrorSolution>retry</ErrorSolution>
                <ErrorMessage>fail to call</ErrorMessage>
            </WizardErrorCodes>
            <WizardResponseParameters>
                <ExampleValue>example2</ExampleValue>
                <ParameterDataType>0</ParameterDataType>
                <ParameterName>param2</ParameterName>
                <ParameterDescription>description2</ParameterDescription>
            </WizardResponseParameters>
            <WizardRequestParameters>
                <DefaultValue>default1</DefaultValue>
                <ExampleValue>example1</ExampleValue>
                <ParameterDataType>0</ParameterDataType>
                <ParameterPosition>0</ParameterPosition>
                <ParameterName>param1</ParameterName>
                <ParameterOperator>0</ParameterOperator>
                <ParameterDescription>description1</ParameterDescription>
                <IsRequiredParameter>true</IsRequiredParameter>
            </WizardRequestParameters>
            <WizardConnection>
                <TableName>1</TableName>
                <ConnectionId>123</ConnectionId>
            </WizardConnection>
        </WizardDetails>
    </Apis>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "Apis": {
            "Status": 1,
            "VisibleRange": 0,
```

`"Description": "`测试`API`描述`",`

```json
            "CreatedTime": "2020-06-23T00:21:01+0800",
```

`"ApiName": "`我的`API`名称`",`

```json
            "Timeout": 10000,
            "RequestMethod": 0,
            "CreatorId": 1234567,
            "ProjectId": 10000,
            "ResponseContentType": 0,
            "OperatorId": 2345678,
            "GroupId": "ab123",
            "TenantId": 10001,
            "ModifiedTime": "2020-06-23T00:21:01+0800",
            "ApiMode": 0,
            "ApiId": 10002,
            "ApiPath": "/test/1",
            "Protocols": 0,
            "RegistrationDetails": {
                "ServiceRequestBodyDescription": "{\"abc\":1}",
                "SuccessfulResultSample": "{\"success\": true}",
                "ServiceContentType": 0,
                "ServicePath": "/index",
                "FailedResultSample": "{\"success\": false}",
                "ServiceHost": "http://www.abc.com",
                "RegistrationErrorCodes": {
                    "ErrorCode": 1001,
                    "ErrorSolution": "retry",
                    "ErrorMessage": "fail to call"
                },
                "RegistrationRequestParameters": {
                    "DefaultValue": "default1",
                    "ExampleValue": "example1",
                    "ParameterDataType": 0,
                    "ParameterPosition": 0,
                    "ParameterName": "name1",
                    "ParameterOperator": 0,
                    "ParameterDescription": "description1",
                    "IsRequiredParameter": true
                }
            },
            "ScriptDetails": {
                "Script": "select a from t",
                "IsPagedResponse": true,
```

DataWorks

```json
                "SuccessfulResultSample": "{\"success\": true}",
                "FailedResultSample": "{\"success\": false}",
                "ScriptErrorCodes": {
                    "ErrorCode": 1001,
                    "ErrorSolution": "retry",
                    "ErrorMessage": "fail to call"
                },
                "ScriptResponseParameters": {
                    "ExampleValue": "example2",
                    "ParameterDataType": 0,
                    "ParameterName": "param2",
                    "ParameterDescription": "description2"
                },
                "ScriptRequestParameters": {
                    "DefaultValue": "default1",
                    "ExampleValue": "example1",
                    "ParameterDataType": 0,
                    "ParameterPosition": 0,
                    "ParameterName": "param1",
                    "ParameterOperator": 0,
                    "ParameterDescription": "description1",
                    "IsRequiredParameter": true
                },
                "ScriptConnection": {
                    "TableName": "t",
                    "ConnectionId": 123
                }
            },
            "WizardDetails": {
                "IsPagedResponse": true,
                "SuccessfulResultSample": "{\"success\": true}",
                "FailedResultSample": "{\"success\": false}",
                "WizardErrorCodes": {
                    "ErrorCode": 1001,
                    "ErrorSolution": "retry",
                    "ErrorMessage": "fail to call"
                },
                "WizardResponseParameters": {
                    "ExampleValue": "example2",
                    "ParameterDataType": 0,
                    "ParameterName": "param2",
                    "ParameterDescription": "description2"
                },
                "WizardRequestParameters": {
                    "DefaultValue": "default1",
                    "ExampleValue": "example1",
                    "ParameterDataType": 0,
                    "ParameterPosition": 0,
                    "ParameterName": "param1",
                    "ParameterOperator": 0,
                    "ParameterDescription": "description1",
                    "IsRequiredParameter": true
                },
                "WizardConnection": {
"TableName"
```

DataWorks

```json
                    "TableName": 1,
                    "ConnectionId": 123
                }
            }
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListDags

根据OpSeq（补数据唯一标识）获取单次补数据的所有Dag详情。 Dag Type的类型： MANUAL：手动任务工作流 SMOKE_TEST：冒烟测试工作流 SUPPLY_DATA：补数据 BUSINESS_PROCESS_DAG：一次性业务流程工作流 Dag Status的类型： CREATED：已创建 RUNNING：运行中 FAILURE：运行失败 SUCCESS：运行成功

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| OpSeq | Long | Body | 是 | 123 | 补数据唯一标识。 |
| ProjectEnv | Strin g | Body | 是 | PROD | 调度运维环境的标识： PROD表示生产环境，DEV 表示开发环境。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 7782a299-b291- 4fee-8424- cf8058efa8e8 | 请求的ID。用于定位日志，排查问题。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |
| Data | Struct |  | Dag的详情信息。 |
| -Dags | Array |  | 返回的实体。 |
| --Type | String | MANUAL FLOW _ | DAG的类型，包括： MANUAL（手动任务工作流） SMOKE TEST（冒烟测试工作流） _ SUPPLY DATA（补数据） _ BUSINESS PROCESS DAG（一次性业务流 _ _ 程工作流） |
| --Status | String | FAILURE | DAG的状态，包括: CREATED（已创建） RUNNING（运行中） FAILURE（运行失败） SUCCESS（运行成功） |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --FinishTime | Long | 1605052800000 | 结束时间。 |
| --CreateTime | Long | 1605052800000 | 创建时间。 |
| --ProjectId | Long | 112345 | 工作空间的ID。 |
| --DagId | Long | 351249682 | DagId。 |
| --Gmtdate | Long | 1605052800000 | Gmtdate。 |
| --StartTime | Long | 1605052800000 | 开始时间。 |
| --CreateUser | String | 173662940004854 5 | 创建人。 |
| --Bizdate | Long | 1605052800000 | 业务日期。 |
| --Name | String | test dag _ | Dag的名称。 |
| --ModifyTime | Long | 1605052800000 | 修改时间。 |
| --OpSeq | Long | 123 | 操作的标识码。 |

**示例**

请求示例

```
&RegionId=default &OpSeq=123 &ProjectEnv=PROD
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"7782a299-b291-4fee-8424-cf8058efa8e8",
 "HttpStatusCode":200,
 "Data":{
  "-Dags":{
   "Status":"FAILURE",
   "ModifyTime":1605052800000,
   "CreateTime":1605052800000,
   "ProjectId":112345,
   "StartTime":1605052800000,
   "CreateUser":"1736629400048545",
   "DagId":351249682,
   "Bizdate":1605052800000,
   "Name":"test_dag",
   "Gmtdate":1605052800000,
   "Type":"MANUAL_FLOW",
   "OpSeq":123,
   "FinishTime":1605052800000
  }
 },
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>7782a299-b291-4fee-8424-cf8058efa8e8</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
 <Dags>
  <Status>FAILURE</Status>
  <ModifyTime>1605052800000</ModifyTime>
  <CreateTime>1605052800000</CreateTime>
  <ProjectId>112345</ProjectId>
  <StartTime>1605052800000</StartTime>
  <CreateUser>1736629400048545</CreateUser>
  <DagId>351249682</DagId>
  <Bizdate>1605052800000</Bizdate>
  <Name>test_dag</Name>
  <Gmtdate>1605052800000</Gmtdate>
  <Type>MANUAL_FLOW</Type>
  <OpSeq>123</OpSeq>
  <FinishTime>1605052800000</FinishTime>
 </Dags>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

#### ListInstances

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListInstances | 系统规定参数。取值：ListInstances。 |
| NodeId | Long | 是 | 100000000000 | 节点的ID。您可以调用ListNodes查看节点ID信息。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括PROD（生产环境）和 DEV（开发环境）。 |
| ProjectId | Long | 是 | 12345 | 工作空间的ID。您可以调用ListProjects查看空间ID信息。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| NodeName | String | 否 | openmr 8**** _ | 节点的名称。您可以调用ListNodes查看节点名称。 |
| Owner | String | 否 | 193379**** | 负责人的ID，即工作空间管理员的账号 UID。您可登录阿里云控制台后，在账号管理的安全管理中查看账号UID。 |
| BizName | String | 否 | test bizName _ | 业务流程的名称。您可以调用 ListBusiness查看业务流程信息。 |
| ProgramType | String | 否 | ODPS SQL _ | 节点的类型。您可以调用ListNodes查看节点类型。 |
| PageNumber | Integer | 否 | 1 | 页码数。最小值1，最大值100。 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 该接口目前不支持指定实例列表的排序方式，实例列表默认按照实例ID和实例创建的时间倒序排序。 |
| DagId | Long | 否 | 33845 | 工作流的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Struct |  | 实例的列表。 |
|---|---|---|---|
| Instances | Array of Instance |  | 实例的信息。 |
| BaselineId | Long | 123123 | 基线ID。 |
| BeginRunning Time | Long | 1590416703313 | 实例任务开始运行的时间。 |
| BeginWaitRes Time | Long | 1590416703313 | 实例任务开始等待资源的时间。 |
| BeginWaitTim eTime | Long | 1590416703313 | 实例任务开始等待调度的时间。 |
| Bizdate | Long | 1590336000000 | 执行调度任务的日期。通常为该任务运行时间的前一天。 |
| Connection | String | odps first _ | 连接串。 |
| CreateTime | Long | 1590416703313 | 实例的创建时间。 |
| CycTime | Long | 1590422400000 | 调度任务的运行时间。 |
| DagId | Long | 33845 | 工作流的ID。 |
| DagType | String | DAILY | 工作流的类型，取值如下： DAILY（日常调度） MANUAL（手动任务） SMOKE TEST（冒烟测试） _ SUPPLY DATA（补数据） _ |
| DqcDescriptio n | String | [{"projectName":"z tjy dim","tableNam _ e":"dim user agent _ _ manage area a"," _ _ _ partition":"ds\u003 d$[yyyy-mm-dd- 1]"}] | DQC分区规则串。 |
| DqcType | Integer | 1 | DQC类型，取值如下： 0表示有关联dqc。 1表示没有关联dqc。 |

DataWorks

| ErrorMessage | String | error message | 实例运行的报错信息。该字段已废弃，您可以调用GetInstanceLog接口获取执行任务的相关报错信息。 |
|---|---|---|---|
| FinishTime | Long | 1590416703313 | 调度任务的结束时间。 |
| InstanceId | Long | 1234 | 实例的ID。 |
| ModifyTime | Long | 1590416703313 | 调度任务的最新修改时间。 |
| NodeId | Long | 33115 | 节点的ID。 |
| NodeName | String | kzh | 节点的名称。 |
| ParamValues | String | bizdate=$bizdate tbods=$tbods | 参数的信息。 |
| Priority | Integer | 1 | 实例运行优先级，取值分为1、3、5、7和8。取值越大，优先级越高。默认优先级为1。 |
| RelatedFlowId | Long | 123456 | 关联的业务流程ID。 |
| RepeatInterval | Long | 60000 | 调度任务运行出错后，重新调整调度频率，单位为毫秒（ms）。 |
| Repeatability | Boolean | true | 实例任务是否可以重复执行。 |
| Status | String | NOT RUN _ | 任务的状态，取值如下： NOT RUN（未运行） _ WAIT TIME（等待定时时间dueTime或 _ cycleTime到来） WAIT RESOURCE（等待资源） _ RUNNING（运行中） CHECKING（下发给数据质量进行数据校检） CHECKING CONDITION（正在进行分支条 _ 件校检） FAILURE（执行失败） SUCCESS（执行成功） |
| PageNumber | Integer | 1 | 页码数。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |

DataWorks

| TotalCount | Integer | 66 | 实例的总数。 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Proj ectNotExists | 错误码。 |
| ErrorMessage | String | The project does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&NodeId=100000000000 &ProjectEnv=PROD &ProjectId=12345 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>66</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Instances>
        <BaselineId>123123</BaselineId>
        <Status>NOT_RUN</Status>
        <ModifyTime>1590416703313</ModifyTime>
        <NodeName>kzh</NodeName>
        <DagType>DAILY</DagType>
        <InstanceId>1234</InstanceId>
        <DqcType>1</DqcType>
        <Priority>1</Priority>
        <ParamValues>bizdate=$bizdate tbods=$tbods</ParamValues>
        <CreateTime>1590416703313</CreateTime>
        <Connection>odps_first</Connection>
        <RelatedFlowId>123456</RelatedFlowId>
        <BeginWaitTimeTime>1590416703313</BeginWaitTimeTime>
        <CycTime>1590422400000</CycTime>
        <DagId>33845</DagId>
        <BeginRunningTime>1590416703313</BeginRunningTime>
        <Bizdate>1590336000000</Bizdate>
        <Repeatability>true</Repeatability>
        <FinishTime>1590416703313</FinishTime>
        <DqcDescription>
[{"projectName":"ztjy_dim","tableName":"dim_user_agent_manage_area_a","partition":"ds\u00 $[yyyy-mm-dd-1]"}]</DqcDescription>
        <NodeId>33115</NodeId>
        <BeginWaitResTime>1590416703313</BeginWaitResTime>
        <ErrorMessage>error message</ErrorMessage>
        <RepeatInterval>60000</RepeatInterval>
    </Instances>
</Data> <ErrorCode>Invalid.Tenant.ProjectNotExists</ErrorCode> <ErrorMessage>The project does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 66,
        "PageSize": 10,
        "PageNumber": 1,
        "Instances": {
            "BaselineId": 123123,
            "Status": "NOT_RUN",
            "ModifyTime": 1590416703313,
            "NodeName": "kzh",
            "DagType": "DAILY",
            "InstanceId": 1234,
            "DqcType": 1,
            "Priority": 1,
            "ParamValues": "bizdate=$bizdate tbods=$tbods",
            "CreateTime": 1590416703313,
            "Connection": "odps_first",
            "RelatedFlowId": 123456,
            "BeginWaitTimeTime": 1590416703313,
            "CycTime": 1590422400000,
            "DagId": 33845,
            "BeginRunningTime": 1590416703313,
            "Bizdate": 1590336000000,
            "Repeatability": true,
            "FinishTime": 1590416703313,
            "DqcDescription": "
[{\"projectName\":\"ztjy_dim\",\"tableName\":\"dim_user_agent_manage_area_a\",\"partition :\"ds\\u003d$[yyyy-mm-dd-1]\"}]",
            "NodeId": 33115,
            "BeginWaitResTime": 1590416703313,
            "ErrorMessage": "error message",
            "RepeatInterval": 60000
        }
    },
    "ErrorCode": "Invalid.Tenant.ProjectNotExists",
    "ErrorMessage": "The project does not exist.",
    "Success": true
}
```

#### ListInstanceAmount

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | ListInstanceAmo unt | 系统规定参数。取值： ListInstanceAmount。 |
|---|---|---|---|---|
| BeginDate | String | 是 | 2021-06- 13T00:00:00+0 800 | 开始业务日期，精确到天。该参数需要配置为yyyy-MM-dd'T'HH:mm:ssZ的UTC 格式。 |
| EndDate | String | 是 | 2021-06- 16T00:00:00+0 800 | 结束业务日期，精确到天。该参数需要配置为yyyy-MM-dd'T'HH:mm:ssZ的UTC 格式。 |
| ProjectId | Long | 是 | 10000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceCount s | Array of IntanceCounts |  | 周期实例数量在指定时间段的趋势数据。 |
| Count | Integer | 9527 | 周期实例的数量。 |
| Date | Long | 1623772800000 | 获取周期实例数量的业务日期，此处显示业务日期对应的时间戳。 |
| RequestId | String | 95279527adhfj**** | 请求ID。用于出现错误后排查问题。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListInstanceAmount &BeginDate=2021-06-13T00:00:00+0800 &EndDate=2021-06-16T00:00:00+0800 &ProjectId=10000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>95279527adhfj****</RequestId> <InstanceCounts>
    <Count>9527</Count>
    <Date>1623772800000</Date>
</InstanceCounts>
```

`JSON` 格式

```json
{
    "RequestId": "95279527adhfj****",
    "InstanceCounts": {
        "Count": 9527,
        "Date": 1623772800000
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.NoProject | You have not joined any project. | 尚未加入任何工作空间。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### ListInstanceHistory

调用ListInstanceHistory，获取所有实例历史记录，任务重跑一次就会生成一条历史记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Long | Body | 是 | 1234 | 实例的ID。您可以调用 ListInstances获取。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| ProjectEnv | Strin g | Body | 否 | PROD | 工作空间的环境，包括 PROD（生产环境）和 DEV（开发环境），默认获取PROD（生产环境）的实例数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Instances | Array |  | 实例列表 |
| -Status | String | NOT RUN _ | 任务的状态，取值如下： NOT RUN（未运行） _ WAIT TIME（等待定时时间DueTime或 _ CycTime到来） WAIT RESOURCE（等待资源） _ RUNNING（运行中） CHECKING（下发给数据质量进行数据校检） CHECKING CONDITION（正在进行分支条 _ 件校检） FAILURE（执行失败） SUCCESS（执行成功） |
| -CycTime | Long | 1590422400000 | 调度任务的运行时间，返回时间戳格式。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - BeginRunning Time | Long | 1590416703313 | 实例开始运行的时间，返回时间戳格式。 |
| -FinishTime | Long | 1590416703313 | 调度任务的结束时间，返回时间戳格式。 |
| -ErrorMessage | String | error message | 实例运行的报错信息。该字段已废弃，您可以调用GetInstanceLog接口获取执行任务的相关报错信息。 |
| -CreateTime | Long | 1590416703313 | 实例的创建时间。 |
| -DagId | Long | 33845 | 工作流的ID。 |
| -TaskType | String | NORMAL(0) | 任务实例的调度类型，取值如下： NORMAL(0)：正常调度任务。该任务被日常调度。 MANUAL(1)：手动任务。该任务不会被日常调度。 PAUSE(2)：冻结任务。该任务被日常调度， 但启动调度时直接被置为失败状态。 SKIP(3)：空跑任务。该任务被日常调度，但启动调度时直接被置为成功状态。 SKIP UNCHOOSE(4)：临时工作流中未选择 _ 的任务，仅存在于临时工作流中，启动调度时直接被置为成功状态。 SKIP CYCLE(5)：未到运行周期的周或月任 _ 务。该任务被日常调度，但启动调度时直接被置为成功状态。 CONDITION UNCHOOSE(6)：上游实例中 _ 有分支（IF）节点，但是该下游节点未被分支节点选中，直接置为空跑任务。 REALTIME DEPRECATED(7)：实时生成的 _ 已经过期的周期实例，该类型的任务直接被置为成功状态。 |
| -DagType | String | 1 | DQC类型，取值如下： 0表示有关联dqc。 1表示没有关联dqc。 |
| -ModifyTime | Long | 1590416703313 | 调度任务的最新修改时间。 |
| -InstanceId | Long | 1234 | 实例的ID。 |
| - BeginWaitRes Time | Long | 1590416703313 | 实例任务开始等待资源的时间。 |

|  | 开发指南·OpenAPI参 | 考 |  | DataWork | s |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Bizdate | Long | 1590336000000 | 执行调度任务的日期。通常为该任务运行时间的前一天。 |
| -NodeName | String | kzh | 节点的名称。 |
| - BeginWaitTim eTime | Long | 1590416703313 | 实例任务开始等待调度的时间。 |
| -NodeId | Long | 33115 | 节点的ID。 |
| - InstanceHistor yId | Long | 1 | 实例的历史档案编号。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。取值如下： true：调用成功。 false：调用失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListInstanceHistory &InstanceId=1234 &RegionId=default
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "Instances":{
  "Status":"NOT_RUN",
  "ModifyTime":1590416703313,
  "InstanceHistoryId":1,
  "DagType":"1",
  "InstanceId":1234,
  "NodeName":"kzh",
  "CreateTime":1590416703313,
  "CycTime":1590422400000,
  "BeginWaitTimeTime":1590416703313,
  "DagId":33845,
  "BeginRunningTime":1590416703313,
  "Bizdate":1590336000000,
  "FinishTime":1590416703313,
  "TaskType":"NORMAL(0)",
  "NodeId":33115,
  "BeginWaitResTime":1590416703313,
  "ErrorMessage":"error message"
 },
 "RequestId":"E6F0DBDD-5AD****",
 "Success":true
}
```

`XML` 格式

```xml
<Instances>
 <Status>NOT_RUN</Status>
 <ModifyTime>1590416703313</ModifyTime>
 <InstanceHistoryId>1</InstanceHistoryId>
 <DagType>1</DagType>
 <InstanceId>1234</InstanceId>
 <NodeName>kzh</NodeName>
 <CreateTime>1590416703313</CreateTime>
 <CycTime>1590422400000</CycTime>
 <BeginWaitTimeTime>1590416703313</BeginWaitTimeTime>
 <DagId>33845</DagId>
 <BeginRunningTime>1590416703313</BeginRunningTime>
 <Bizdate>1590336000000</Bizdate>
 <FinishTime>1590416703313</FinishTime>
 <TaskType>NORMAL(0)</TaskType>
 <NodeId>33115</NodeId>
 <BeginWaitResTime>1590416703313</BeginWaitResTime>
 <ErrorMessage>error message</ErrorMessage>
</Instances> <RequestId>E6F0DBDD-5AD****</RequestId> <Success>true</Success>
```

#### ListSuccessInstanceAmount

调用ListSuccessInstanceAmount，获取业务日期当天生成的周期实例任务，在业务日期的不同整点时刻，运行成功的实例数量统计趋势。 DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListSuccessInsta nceAmount | 系统规定参数。取值： ListSuccessInstanceAmount。 |
| ProjectId | Long | 是 | 9527 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceStatus Trend | Struct |  | 在业务日期的不同时刻，运行成功的实例数量统计趋势数据。 |
| AvgTrend | Array of AvgTrend |  | 历史平均趋势。 |
| Count | Integer | 10 | 运行成功的实例数量。 |
| TimePoint | String | 01:00 | 时间点。取值范围为00:00～23:00中的整点小时时间，例如00:00、01:00、02:00等等。 |
| TodayTrend | Array of TodayTrend |  | 业务日期当天的趋势。 |
| Count | Integer | 10 | 运行成功的实例数量。 |
| TimePoint | String | 01:00 | 时间点。取值范围为00:00～23:00中的整点小时时间，例如00:00、01:00、02:00等等。 |
| YesterdayTren d | Array of YesterdayTren d |  | 业务日期前一天的趋势。 |
| Count | Integer | 10 | 运行成功的实例数量。 |
| TimePoint | String | 01:00 | 时间点。取值范围为00:00～23:00中的整点小时时间，例如00:00、01:00、02:00等等。 |
| RequestId | String | 952795279527ab* *** | 请求ID。用于出现错误后排查问题。 |

DataWorks

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListSuccessInstanceAmount &ProjectId=9527 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>952795279527ab****</RequestId> <InstanceStatusTrend>
    <YesterdayTrend>
        <TimePoint>01:00</TimePoint>
        <Count>10</Count>
    </YesterdayTrend>
    <AvgTrend>
        <TimePoint>01:00</TimePoint>
        <Count>10</Count>
    </AvgTrend>
    <TodayTrend>
        <TimePoint>01:00</TimePoint>
        <Count>10</Count>
    </TodayTrend>
</InstanceStatusTrend>
```

`JSON` 格式

```json
{
    "RequestId": "952795279527ab****",
    "InstanceStatusTrend": {
        "YesterdayTrend": {
            "TimePoint": "01:00",
            "Count": 10
        },
        "AvgTrend": {
            "TimePoint": "01:00",
            "Count": 10
        },
        "TodayTrend": {
            "TimePoint": "01:00",
            "Count": 10
        }
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

DataWorks

| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListManualDagInstances

调用ListManualDagInstances获取手动执行的业务流程实例的信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListManualDagIn stances | 系统规定参数。取值： ListManualDagInstances。 |
| DagId | String | 是 | 7000001231241 | 触发手动业务流程运行的Dag实例ID。 |
| ProjectEnv | String | 是 | RPOD | 运维中心的调度环境标识，包括 PROD（生产环境）和DEV（开发环境）。 |

DataWorks

| ProjectName | String | 是 | test workspace _ | 手动业务流程所属的工作空间名称。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Instances | Array of Instances |  | 手动业务流程的内部实例列表。 |
| BeginRunning Time | Long | 1605178414676 | 实例任务开始运行的时间。 |
| BeginWaitRes Time | Long | 1605178414676 | 实例任务开始等待资源的时间。 |
| BeginWaitTim eTime | Long | 1605178414676 | 实例任务开始等待调度的时间。 |
| BizDate | Long | 1605178414676 | 业务日期。通常为该任务运行时间的前一天。 |
| CreateTime | Long | 1605178414676 | 实例任务的创建时间。 |
| CycTime | Long | 1605178414676 | 实例任务的定时时间。 |
| DagId | Long | 350850491 | 手动业务流程实例的DagId。 |
| DagType | String | 5 | 手动业务流程的标识。 |
| FinishTime | Long | 1605178414676 | 实例任务运行的结束时间。 |
| InstanceId | Long | 11726873619 | 内部实例ID。 |
| ModifyTime | Long | 1605178414676 | 最近一次修改实例任务的时间。 |
| NodeId | Long | 37851 | 业务流程的内部节点ID。 |
| NodeName | String | test2 | 节点的名称。 |
| ParamValues | String | xxx=yyy | 实例的参数信息。 |

DataWorks

| Status | String | SUCCESS | 实例任务的状态，取值如下： NOT RUN（未运行） _ WAIT TIME（等待定时时间DueTime或 _ CycleTime到来） WAIT RESOURCE（等待资源） _ RUNNING（运行中） CHECKING（下发给数据质量进行数据校检） CHECKING CONDITION（正在进行分支条 _ 件校检） FAILURE（执行失败） SUCCESS（执行成功） |
|---|---|---|---|
| TaskType | String | MANUAL | 实例任务的调度类型，取值如下： NORMAL(0)：正常调度任务。该任务被日常调度。 MANUAL(1)：手动任务。该任务不会被日常调度。 PAUSE(2)：冻结任务。该任务被日常调度， 但启动调度时直接被置为失败状态。 SKIP(3)：空跑任务。该任务被日常调度，但启动调度时直接被置为成功状态。 SKIP UNCHOOSE(4)：临时工作流中未选择 _ 的任务，仅存在于临时工作流中，启动调度时直接被置为成功状态。 SKIP CYCLE(5)：未到运行周期的周或月任 _ 务。该任务被日常调度，但启动调度时直接被置为成功状态。 CONDITION UNCHOOSE(6)：上游实例中 _ 有分支（IF）节点，但是该下游节点未被分支节点选中，直接置为空跑任务。 REALTIME DEPRECATED(7)：实时生成的 _ 已经过期的周期实例，该类型的任务直接被置为成功状态。 |
| RequestId | String | SDFSDFSDF- SDFSDF-SDFDSF- SDFSDF | 请求ID，用于定位日志，排查问题。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListManualDagInstances &DagId=7000001231241 &ProjectEnv=RPOD &ProjectName=test_workspace &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<Instances>
    <Status>SUCCESS</Status>
    <ModifyTime>1605178414676</ModifyTime>
    <NodeName>test2</NodeName>
    <DagType>5</DagType>
    <InstanceId>11726873619</InstanceId>
    <ParamValues>xxx=yyy</ParamValues>
    <CreateTime>1605178414676</CreateTime>
    <BeginWaitTimeTime>1605178414676</BeginWaitTimeTime>
    <CycTime>1605178414676</CycTime>
    <DagId>350850491</DagId>
    <BeginRunningTime>1605178414676</BeginRunningTime>
    <FinishTime>1605178414676</FinishTime>
    <TaskType>MANUAL</TaskType>
    <NodeId>37851</NodeId>
    <BeginWaitResTime>1605178414676</BeginWaitResTime>
    <BizDate>1605178414676</BizDate>
</Instances> <RequestId>SDFSDFSDF-SDFSDF-SDFDSF-SDFSDF</RequestId>
```

`JSON` 格式

```json
{
    "Instances": {
        "Status": "SUCCESS",
        "ModifyTime": 1605178414676,
        "NodeName": "test2",
        "DagType": 5,
        "InstanceId": 11726873619,
        "ParamValues": "xxx=yyy",
        "CreateTime": 1605178414676,
        "BeginWaitTimeTime": 1605178414676,
        "CycTime": 1605178414676,
        "DagId": 350850491,
        "BeginRunningTime": 1605178414676,
        "FinishTime": 1605178414676,
        "TaskType": "MANUAL",
        "NodeId": 37851,
        "BeginWaitResTime": 1605178414676,
        "BizDate": 1605178414676
    },
    "RequestId": "SDFSDFSDF-SDFSDF-SDFDSF-SDFSDF"
}
```

#### ListNodes

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | ListNodes | 系统规定参数。取值：ListNodes。 |
|---|---|---|---|---|
| ProjectEnv | String | 是 | PROD | 运行的环境，包括DEV和PROD。 |
| ProjectId | Long | 是 | 1234 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Owner | String | 否 | 193379**** | 负责人的ID。 |
| BizName | String | 否 | test bizName _ | 业务流程的名称。 |
| ProgramType | String | 否 | ODPS SQL _ | 节点的类型。 |
| PageNumber | Integer | 否 | 1 | 页码数。最小值1，最大值100 |
| PageSize | Integer | 否 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| NodeName | String | 否 | liux test n**** _ _ | 节点的名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 节点的列表。 |
| Nodes | Array of Nodes |  | 节点的信息。 |
| BaselineId | Long | 123456 | 基线ID |
| Connection | String | odps first _ | 连接串 |
| CronExpress | String | 00 00 00 * * ? | cron表达式。 |
| Description | String | test | 节点的描述信息。 |

DataWorks

| DqcDescriptio n | String | [{"projectName":"z tjy dim","tableNam _ e":"dim user agent _ _ manage area a"," _ _ _ partition":"ds\u003 d$[yyyy-mm-dd- 1]"}] | DQC分区规则串 |
|---|---|---|---|
| DqcType | Integer | 1 | DQC类型，0表示有关联dqc，1表示没有关联 dqc |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | liux test n**** _ _ | 节点的名称。 |
| OwnerId | String | 19337906836551 | 负责人的ID。 |
| ParamValues | String | a=b | 额外的参数。 |
| Priority | Integer | 1 | 优先级，1/3/5/7/8 |
| ProgramType | String | ODPS SQL _ | 节点的类型。 |
| ProjectId | Long | 33671 | 工作空间的ID。 |
| RelatedFlowId | Long | 1231123 | 关联业务流程ID |
| RepeatInterval | Long | 60 | 出错后重新调度频率 |
| Repeatability | Boolean | true | 是否可以重复运行。 |
| ResGroupNam e | String | 默认资源组 | 资源组的名称。 |
| SchedulerType | String | NORMAL | 调度的类型，取值如下： NORMAL：正常调度任务。 MANUAL：手动任务，不会被日常调度。 PAUSE：暂停任务。 SKIP：空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| PageNumber | Integer | 1 | 页码数。 |

DataWorks

| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。” |
|---|---|---|---|
| TotalCount | Integer | 66 | 符合条件的节点总数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&ProjectEnv=PROD &ProjectId=1234 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>66</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Nodes>
        <BaselineId>123456</BaselineId>
        <ResGroupName>默认资源组</ResGroupName>
        <Description>test</Description>
        <NodeName>liux_test_n****</NodeName>
        <DqcType>1</DqcType>
        <Priority>1</Priority>
        <ParamValues>a=b</ParamValues>
        <Connection>odps_first</Connection>
        <ProjectId>33671</ProjectId>
        <RelatedFlowId>1231123</RelatedFlowId>
        <SchedulerType>NORMAL</SchedulerType>
        <CronExpress>00 00 00 * * ?</CronExpress>
        <Repeatability>true</Repeatability>
        <OwnerId>19337906836551</OwnerId>
        <DqcDescription>
[{"projectName":"ztjy_dim","tableName":"dim_user_agent_manage_area_a","partition":"ds\u00 $[yyyy-mm-dd-1]"}]</DqcDescription>
        <NodeId>1234</NodeId>
        <ProgramType>ODPS_SQL</ProgramType>
        <RepeatInterval>60</RepeatInterval>
    </Nodes>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 66,
        "PageSize": 10,
        "PageNumber": 1,
        "Nodes": {
            "BaselineId": 123456,
```

`"ResGroupName": "`默认资源组`",`

```json
            "Description": "test",
            "NodeName": "liux_test_n****",
            "DqcType": 1,
            "Priority": 1,
            "ParamValues": "a=b",
            "Connection": "odps_first",
            "ProjectId": 33671,
            "RelatedFlowId": 1231123,
            "SchedulerType": "NORMAL",
            "CronExpress": "00 00 00 * * ?",
            "Repeatability": true,
            "OwnerId": 19337906836551,
            "DqcDescription": "
[{\"projectName\":\"ztjy_dim\",\"tableName\":\"dim_user_agent_manage_area_a\",\"partition :\"ds\\u003d$[yyyy-mm-dd-1]\"}]",
            "NodeId": 1234,
            "ProgramType": "ODPS_SQL",
            "RepeatInterval": 60
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### ListInnerNodes

调用ListInnerNodes接口，获取内部节点详情，例如查询组合节点、循环节点等节点类型的内部节点。但是该接口不支持获取PAI节点的内部节点详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProgramT ype | Strin g | Body | 否 | ODPS SQL _ | 文件的代码类型。 常用的代码及其对应的文件类型包括6（Shell）、 10（ODPS SQL）、 11（ODPS MR）、23（数据集成）、24（ODPS Script）、97（PAI）、 98（组合节点）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS对象检查）、257（EMR Shell）、258（EMR Spark Shell）、 259（EMR Presto）、 260（EMR Impala）、 900（实时同步）、 1002（PAI内部节点）、 1089（跨租户节点）、 1091（Hologres开发）、 1093（Hologres SQL）、 1100（赋值节点）、 1106（遍历节点 （foreach））、 1221（PyODPS 3），您可以调用ListNodes查看节点类型。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页码数。最小值1，最大值 100 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示的条数，默认为10 条，最大100条。 |
| ProjectId | Long | Body | 是 | 1234 | 工作空间的ID。 |
| ProjectEnv | Strin g | Body | 否 | PROD | 运行的环境，包括DEV和 PROD，默认PROD。 |
| NodeNam e | Strin g | Body | 否 | liux test n**** _ _ | 节点名称。 |
| OuterNod eId | Long | Body | 是 | 1234 | 内部节点所属的组合节点 ID。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |
| Paging | Struct |  | 分页信息。 |
| -Nodes | Array |  | 内部节点列表。 |
| -- SchedulerType | String | NORMAL | 调度的类型，取值如下： NORMAL：正常调度任务。 MANUAL：手动任务，不会被日常调度。 PAUSE：暂停任务。 SKIP：空跑任务，被日常调度，但启动调度时直接被置为成功。 |
| -- RepeatInterval | Long | 60 | 出错后重新调度频率。 |
| --Repeatability | Boolean | true | 是否可以重复运行。 |
| --ProjectId | Long | 123 | 工作空间的ID。 |
| --ProgramType | String | ODPS SQL _ | 节点的类型。 |
| --Priority | Integer | 1 | 优先级，1/3/5/7/8。 |
| --OwnerId | String | 1933****36551 | 负责人的ID。 |
| --Connection | String | odps first _ | 连接串。 |
| --ParamValues | String | a=b | 额外的参数。 |
| --DqcType | String | 1 | DQC类型，0表示有关联dqc，1表示没有关联 dqc。 |
| --BaselineId | Long | 123 | 基线ID。 |
| --Description | String | test | 节点的描述信息。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --NodeName | String | liux test n**** _ _ | 节点的名称。 |
| -- ResGroupNam e | String | 默认资源组 | 资源组的名称。 |
| --BusinessId | Long | 123 | 业务流程ID。 |
| -- DqcDescriptio n | String | [{"projectName":"z tjy dim","tableNam _ e":"dim user agent _ _ manage area a"," _ _ _ partition":"ds\u003 d$[yyyy-mm-dd- 1]"}] | DQC分区规则串。 |
| --CronExpress | String | 00 00 00 * * ? | cron表达式。 |
| --NodeId | Long | 12 | 节点的ID。 |
| -PageNumber | Integer | 1 | 页码数。 |
| -PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| -TotalCount | Integer | 100 | 符合条件的节点总数。 |

**示例**

请求示例

```
&RegionId=default &ProjectId=1234 &OuterNodeId=1234
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"E6F0DBDD-5AD****",
 "Paging":{
  "TotalCount":100,
  "PageSize":10,
  "PageNumber":1,
  "Nodes":{
   "BaselineId":123,
   "Description":"test",
```

`"ResGroupName":"`默认资源组`",`

```json
   "NodeName":"liux_test_n****",
   "Priority":1,
   "DqcType":"1",
   "ParamValues":"a=b",
   "ProjectId":123,
   "Connection":"odps_first",
   "SchedulerType":"NORMAL",
   "CronExpress":"00 00 00 * * ?",
   "Repeatability":true,
   "OwnerId":"1933****36551",
   "DqcDescription":"
[{\"projectName\":\"ztjy_dim\",\"tableName\":\"dim_user_agent_manage_area_a\",\"partition :\"ds\\u003d$[yyyy-mm-dd-1]\"}]",
   "NodeId":12,
   "ProgramType":"ODPS_SQL",
   "BusinessId":123,
   "RepeatInterval":60
  }
 },
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <Paging>
 <TotalCount>100</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <Nodes>
  <BaselineId>123</BaselineId>
  <Description>test</Description>
  <ResGroupName>默认资源组</ResGroupName>
  <NodeName>liux_test_n****</NodeName>
  <Priority>1</Priority>
  <DqcType>1</DqcType>
  <ParamValues>a=b</ParamValues>
  <ProjectId>123</ProjectId>
  <Connection>odps_first</Connection>
  <SchedulerType>NORMAL</SchedulerType>
  <CronExpress>00 00 00 * * ?</CronExpress>
  <Repeatability>true</Repeatability>
  <OwnerId>1933****36551</OwnerId>
  <DqcDescription>
[{&quot;projectName&quot;:&quot;ztjy_dim&quot;,&quot;tableName&quot;:&quot;dim_user_agent anage_area_a&quot;,&quot;partition&quot;:&quot;ds\u003d$[yyyy-mm-dd-1]&quot;}]</DqcDesc ription>
  <NodeId>12</NodeId>
  <ProgramType>ODPS_SQL</ProgramType>
  <BusinessId>123</BusinessId>
  <RepeatInterval>60</RepeatInterval>
 </Nodes>
</Paging> <Success>true</Success>
```

#### ListNodeIO

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListNodeIO | 系统规定参数。取值：ListNodeIO。 |
| IoType | String | 是 | output | 上下游，包括input和output。 |
| NodeId | Long | 是 | 1234 | 节点的ID。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括DEV和PROD。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of Data |  | 节点的列表。 |
| Data | String | dataworks a.1234 _ _ out | 输入或输出名称。 |
| NodeId | Long | 1234 | 节点ID。 |
| TableName | String | dataworks a.datast _ udio tenant waitre _ _ s alarm _ | 输入或输出表的表名。 |
| ErrorCode | String | 0 | 错误码。 |
| ErrorMessage | String | test | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID，用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&IoType=output &NodeId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TableName>dataworks_a.datastudio_tenant_waitres_alarm</TableName>
    <NodeId>1234</NodeId>
    <Data>dataworks_a.1234_out</Data>
</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>test</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": {
        "TableName": "dataworks_a.datastudio_tenant_waitres_alarm",
        "NodeId": 1234,
        "Data": "dataworks_a.1234_out"
    },
    "ErrorCode": 0,
    "ErrorMessage": "test",
    "Success": true
}
```

#### ListNodeInputOrOutput

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListNodeInputOr Output | 系统规定参数。取值： ListNodeInputOrOutput。 |
| IoType | String | 是 | output | 用于指定查询节点为上游节点还是下游节点。取值如下： input，上游节点。 output，下游节点。 |
| NodeId | Long | 是 | 12314567 | 节点的ID。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括DEV（开发环境）和 PROD（生产环境）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of Data |  | 输入输出列表。 |
| Data | String | xxxx.123141254 o _ ut | 输入输出节点名称。 |
| NodeId | Long | 1234667 | 节点ID。 |
| TableName | String | dwd xxx table _ _ | 关联的表名称。 |
| ErrorCode | String | Invalid.Tenant.Proj ectNotExists | 错误码。 |
| ErrorMessage | String | The project does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID，用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListNodeInputOrOutput &IoType=output &NodeId=12314567 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TableName>dwd_xxx_table</TableName>
    <NodeId>1234667</NodeId>
    <Data>xxxx.123141254_out</Data>
</Data> <ErrorCode>Invalid.Tenant.ProjectNotExists</ErrorCode> <ErrorMessage>The project does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": {
        "TableName": "dwd_xxx_table",
        "NodeId": 1234667,
        "Data": "xxxx.123141254_out"
    },
    "ErrorCode": "Invalid.Tenant.ProjectNotExists",
    "ErrorMessage": "The project does not exist.",
    "Success": true
}
```

#### ListNodesByOutput

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListNodesByOut put | 系统规定参数。取值： ListNodesByOutput。 |
| Outputs | String | 是 | aaaaa.1231412 _ out,bbbb.12313 123 out _ | 节点的输出名称。支持配置多个输出名称，配置多个名称时请使用英文逗号（,） 分隔。 |
| ProjectEnv | String | 是 | PROD | 调度运维中心的环境标识，PROD表示生产环境，DEV表示开发环境。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Array of OutputNodePa ir |  | 返回的目标节点信息列表。 |
|---|---|---|---|
| NodeList | Array of Node |  | input和output对应的节点信息列表。 |
| BaselineId | Long | 1235667 | 基线ID。 |
| Connection | String | odps first _ | 数据源名称。 |
| CronExpress | String | 00 00 00 * * ? | cron表达式。 |
| Description | String | test | 节点的描述信息。 |
| DqcDescriptio n | String | [{"projectName":"z tjy dim","tableNam _ e":"dim user agent _ _ manage area a"," _ _ _ partition":"ds\u003 d$[yyyy-mm-dd- 1]"}] | DQC分区规则串。 |
| DqcType | Integer | 1 | DQC类型，0表示有关联dqc，1表示没有关联 dqc。 |
| FileType | String | ODPS SQL _ | 节点的类型。 常用的节点类型如下： 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
| NodeId | Long | 125677 | 节点的ID。 |
| NodeName | String | liux test n**** _ _ | 节点的名称。 |
| OwnerId | String | 19337906836551 | 负责人的ID。 |
| ParamValues | String | a=b | 节点的调度参数。 |

DataWorks

| Priority | Integer | 1 | 节点运行的优先级，取值分为1、3、5、7和8。 取值越大，优先级越高。默认优先级为1。 |
|---|---|---|---|
| ProgramType | String | ODPS SQL _ | 节点的类型。该参数已废弃，节点类型请参考 FileType。 |
| ProjectId | Long | 33671 | 工作空间的ID。 |
| RelatedFlowId | Long | 1235655464 | 关联的业务流程ID。 |
| RepeatInterval | Integer | 60 | 节点运行出错后重新调度的频率。 |
| Repeatability | Boolean | true | 是否可以重复运行。 |
| ResGroupNam e | String | 默认资源组 | 资源组的名称。 |
| SchedulerType | String | NORMAL | 节点任务的调度类型，取值如下： NORMAL：正常调度任务。该任务被日常调度。 MANUAL：手动任务。该任务不会被日常调度。 PAUSE：冻结任务。该任务被日常调度，但启动调度时直接被置为失败状态。 SKIP：空跑任务。该任务被日常调度，但启动调度时直接被置为成功状态。 |
| Output | String | test 0709 1.63000 _ _ 3556 out _ | 当前节点的输出名称。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | SDFSDFSDF- asdfDFSDF- SDFSDf-SDfSFD | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 DataWorks

```
&Outputs=aaaaa.1231412_out,bbbb.12313123_out &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>SDFSDFSDF-asdfDFSDF-SDFSDf-SDfSFD</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Output>test_0709_1.630003556_out</Output>
    <NodeList>
        <BaselineId>1235667</BaselineId>
        <ResGroupName>默认资源组</ResGroupName>
        <Description>test</Description>
        <NodeName>liux_test_n****</NodeName>
        <DqcType>1</DqcType>
        <Priority>1</Priority>
        <ParamValues>a=b</ParamValues>
        <Connection>odps_first</Connection>
        <ProjectId>33671</ProjectId>
        <RelatedFlowId>1235655464</RelatedFlowId>
        <SchedulerType>NORMAL</SchedulerType>
        <CronExpress>00 00 00 * * ?</CronExpress>
        <Repeatability>true</Repeatability>
        <OwnerId>19337906836551</OwnerId>
        <FileType>ODPS_SQL</FileType>
        <DqcDescription>
[{"projectName":"ztjy_dim","tableName":"dim_user_agent_manage_area_a","partition":"ds\u00 $[yyyy-mm-dd-1]"}]</DqcDescription>
        <NodeId>125677</NodeId>
        <ProgramType>ODPS_SQL</ProgramType>
        <RepeatInterval>60</RepeatInterval>
    </NodeList>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "SDFSDFSDF-asdfDFSDF-SDFSDf-SDfSFD",
    "HttpStatusCode": 200,
    "Data": {
        "Output": "test_0709_1.630003556_out",
        "NodeList": {
            "BaselineId": 1235667,
```

`"ResGroupName": "`默认资源组`",`

```json
            "Description": "test",
            "NodeName": "liux_test_n****",
            "DqcType": 1,
            "Priority": 1,
            "ParamValues": "a=b",
            "Connection": "odps_first",
            "ProjectId": 33671,
            "RelatedFlowId": 1235655464,
            "SchedulerType": "NORMAL",
            "CronExpress": "00 00 00 * * ?",
            "Repeatability": true,
            "OwnerId": 19337906836551,
            "FileType": "ODPS_SQL",
            "DqcDescription": "
[{\"projectName\":\"ztjy_dim\",\"tableName\":\"dim_user_agent_manage_area_a\",\"partition :\"ds\\u003d$[yyyy-mm-dd-1]\"}]",
            "NodeId": 125677,
            "ProgramType": "ODPS_SQL",
            "RepeatInterval": 60
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### ListNodesByBaseline

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListNodesByBas eline | 系统规定参数。取值： ListNodesByBaseline。 |
| BaselineId | Long | 是 | 1234 | 基线的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of Data |  | 基线中的节点列表。 |
| NodeId | Long | 1234 | 节点的ID。 |
| NodeName | String | 节点的名称。 | 节点的名称。 |
| Owner | String | 9527952**** | 节点责任人的阿里云UID。 |
| ProjectId | Long | 1234 | 节点所在工作空间的ID。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD-E**** | 请求ID。用于出现错误后排查问题。 |
| Success | String | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListNodesByBaseline &BaselineId=1234 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-E****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Owner>9527952****</Owner>
```

`<NodeName>`节点的名称。`</NodeName>`

```xml
    <ProjectId>1234</ProjectId>
    <NodeId>1234</NodeId>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-E****",
    "HttpStatusCode": 200,
    "Data": {
        "Owner": "9527952****",
```

`"NodeName": "`节点的名称。`",`

```json
        "ProjectId": 1234,
        "NodeId": 1234
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | Forbidden.Wkbenc h.BaselineNoPermi ssion | You are not authorized to access the baseline. | 无对应的基线权限。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.Wkbe nch.ServiceError | An internal error occurred. | 服务开小差了。 |

DataWorks

| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Invalid.Wkbench.Ba selineNotExist | The baseline does not exist. | 基线不存在。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListReminds

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListReminds | 系统规定参数。取值：ListReminds。 |
| PageNumber | Integer | 是 | 1 | 分页的页数。默认值为1，最小值为1，最大值为30。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| Founder | String | 否 | 9527952795**** | 创建人的阿里云UID。 |
| NodeId | Long | 否 | 1234 | 规则的对象，任务节点ID。您可以根据任务节点ID搜索覆盖该任务节点的自定义监控规则。 |

DataWorks

| RemindTypes | String | 否 | FINISHED,ERRO R | 触发条件，包括FINISHED（完成）、 UNFINISHED（未完成）、ERROR（出错）、CYCLE UNFINISHED（周期未完 _ 成）和TIMEOUT（运行超时）。多个触发条件之间使用英文逗号（,）分隔。 |
|---|---|---|---|---|
| AlertTarget | String | 否 | 9527952795**** | 报警接收人的阿里云UID。 |
| SearchText | String | 否 | 模糊搜索规则名称 | 搜索规则名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回的自定义监控规则列表。 |
| PageNumber | Integer | 1 | 当前的页数。 |
| PageSize | Integer | 10 | 每页的大小。 |
| Reminds | Array of Reminds |  | 自定义监控规则列表。 |
| AlertMethods | List | SMS | 报警的方式，包括MAIL（邮件）、SMS（短信）和PHONE（电话，仅DataWorks专业版及以上版本支持）。 |
| AlertTargets | List | 952795**** | 报警接收人的阿里云UID列表。 |
| AlertUnit | String | OWNER | 报警接收对象的粒度，包括OWNER（任务责任人）和OTHER（指定的人）。 |
| BaselineIds | List | 9527 | 当RemindUnit（对象类型）为BASELINE（基线）时，监控的基线ID列表。 |
| BizProcessIds | List | 9527 | 当RemindUnit（对象类型）为 BIZPROCESS（业务流程）时，监控的基线ID列表。 |
| DndEnd | String | 08:00 | 免打扰起始时间，格式为hh:mm。hh的取值范围为0,23，mm的取值范围为0,59。 |
| DndStart | String | 00:00 | 规则创建人的阿里云UID。 |

DataWorks

| Founder | String | 952795**** | 规则创建人的阿里云UID。 |
|---|---|---|---|
| NodeIds | List | 1234 | 当RemindUnit（对象类型）为NODE（任务节点）时，监控的节点ID列表。 |
| ProjectIds | List | 1234 | 当RemindUnit（对象类型）为PROJECT（工作空间）时，监控的节点ID列表。 |
| RemindId | Long | 1234 | 自定义监控规则的ID。 |
| RemindName | String | 规则名称 | 自定义监控规则的名称。 |
| RemindType | String | FINISHED | 触发条件，包括FINISHED（完成）、 UNFINISHED（未完成）、ERROR（出错）、 CYCLE UNFINISHED（周期未完成）和 _ TIMEOUT（运行超时）。 |
| RemindUnit | String | NODE | 对象的类型，包括NODE（任务节点）、 BASELINE（基线）、PROJECT（工作空间）和 BIZPROCESS（业务流程）。 |
| Useflag | Boolean | true | 规则是否开启，包括true（开启）和false（关闭）。 |
| TotalCount | Integer | 100 | 自定义监控规则的总数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 DataWorks

```
&PageNumber=1 &PageSize=10 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Reminds>
        <DndStart>00:00</DndStart>
        <RemindId>1234</RemindId>
        <AlertUnit>OWNER</AlertUnit>
        <DndEnd>08:00</DndEnd>
        <RemindUnit>NODE</RemindUnit>
        <Founder>952795****</Founder>
        <Useflag>true</Useflag>
        <RemindType>FINISHED</RemindType>
        <RemindName>规则名称</RemindName>
        <NodeIds>1234</NodeIds>
        <BaselineIds>9527</BaselineIds>
        <ProjectIds>1234</ProjectIds>
        <BizProcessIds>9527</BizProcessIds>
        <AlertMethods>SMS</AlertMethods>
        <AlertTargets>952795****</AlertTargets>
    </Reminds>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "Reminds": {
            "DndStart": "00:00",
            "RemindId": 1234,
            "AlertUnit": "OWNER",
            "DndEnd": "08:00",
            "RemindUnit": "NODE",
            "Founder": "952795****",
            "Useflag": true,
            "RemindType": "FINISHED",
```

`"RemindName": "`规则名称`",`

```json
            "NodeIds": 1234,
            "BaselineIds": 9527,
            "ProjectIds": 1234,
            "BizProcessIds": 9527,
            "AlertMethods": "SMS",
            "AlertTargets": "952795****"
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

DataWorks

| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### ListTopics

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTopics | 系统规定参数。取值：ListTopics。 |
| BeginTime | String | 是 | 2019-03- 24T00:00:00+0 800 | 起始发现时间，需要使用UTC格式（yyyy- MM-dd'T'HH:mm:ssZ）。 |
| EndTime | String | 是 | 2019-03- 25T23:00:00+0 800 | 截止发现时间，需要使用UTC格式（yyyy- MM-dd'T'HH:mm:ssZ）。 |
| PageNumber | Integer | 是 | 1 | 分页的页数。默认值为1，最小值为1，最大值为30。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TopicTypes | String | 否 | ERROR,SLOW | 事件的类型，包括SLOW（变慢）和 ERROR（出错）。多个事件类型之间使用英文逗号（,）分隔。 |
| TopicStatuses | String | 否 | IGNORE,NEW,FIX ING,RECOVER | 事件的状态，包括IGNORE（已忽略）、 NEW（新发现）、FIXING（处理中）和 RECOVER（已恢复）。多个事件状态之间使用英文逗号（,）分隔。 |
| NodeId | Long | 否 | 1234 | 事件关联的任务节点ID，与参数 InstanceId互斥。 |

DataWorks

| InstanceId | Long | 否 | 12345 | 事件关联的实例ID，与参数NodeId互斥。 |
|---|---|---|---|---|
| Owner | String | 否 | 952795**** | 事件责任人的阿里云UID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回的事件列表。 |
| PageNumber | Integer | 1 | 当前的页数。 |
| PageSize | Integer | 10 | 每页的大小。 |
| Topics | Array of Topics |  | 事件列表。 |
| AddTime | Long | 1553524393000 | 事件发现的时间戳。 |
| FixTime | Long | 1553524393000 | 事件恢复的时间戳。 |
| HappenTime | Long | 1553524393000 | 事件发生的时间戳，事件发生和被发现存在一定的时间差。 |
| InstanceId | Long | 12345 | 事件关联的实例ID。 |
| NodeId | Long | 1234 | 事件关联的任务节点ID。 |
| NodeName | String | 节点名称 | 任务节点的名称。 |
| NodeOwner | String | 952795**** | 任务节点责任人的阿里云UID |
| ProjectId | Long | 1234 | 任务节点所在工作空间的ID。 |
| TopicId | Long | 1234 | 事件的ID。 |
| TopicName | String | 1234出错 | 事件的名称。 |
| TopicStatus | String | NEW | 事件的状态，包括IGNORE（已忽略）、 NEW（新发现）、FIXING（处理中）和 RECOVER（已恢复）。 |

DataWorks

| TopicType | String | ERROR | 事件的类型，包括SLOW（变慢）和ERROR（出错）。 |
|---|---|---|---|
| TotalCount | Integer | 10 | 事件的总数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&BeginTime=2019-03-24T00:00:00+0800 &EndTime=2019-03-25T23:00:00+0800 &PageNumber=1 &PageSize=10 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>10</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Topics>
        <FixTime>1553524393000</FixTime>
        <TopicType>ERROR</TopicType>
        <NodeOwner>952795****</NodeOwner>
```

`<NodeName>`节点名称`</NodeName>`

```xml
        <InstanceId>12345</InstanceId>
        <ProjectId>1234</ProjectId>
        <NodeId>1234</NodeId>
        <TopicId>1234</TopicId>
        <TopicStatus>NEW</TopicStatus>
        <AddTime>1553524393000</AddTime>
        <HappenTime>1553524393000</HappenTime>
        <TopicName>1234出错</TopicName>
    </Topics>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 10,
        "PageSize": 10,
        "PageNumber": 1,
        "Topics": {
            "FixTime": 1553524393000,
            "TopicType": "ERROR",
            "NodeOwner": "952795****",
```

`"NodeName": "`节点名称`",`

```json
            "InstanceId": 12345,
            "ProjectId": 1234,
            "NodeId": 1234,
            "TopicId": 1234,
            "TopicStatus": "NEW",
            "AddTime": 1553524393000,
            "HappenTime": 1553524393000,
            "TopicName": "1234出错"
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### RestartInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RestartInstance | 系统规定参数。取值： RestartInstance。 |
| InstanceId | Long | 是 | 1234 | 实例的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 调用重启实例接口后，返回的结果详情。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | q32ety**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 DataWorks

```
&InstanceId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>q32ety****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "q32ety****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### ResumeInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResumeInstance | 系统规定参数。取值： ResumeInstance。 |
| InstanceId | Long | 是 | 1234 | 实例的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Boolean | true | 调用ResumeInstance接口后，返回的结果详情。 |
|---|---|---|---|
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&InstanceId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### RunTriggerNode

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RunTriggerNode | 系统规定参数。取值： RunTriggerNode。 |
| AppId | Long | 是 | 10001 | 触发式节点所属的DataWorks工作空间 ID。工作空间ID可参见ListProjects查询。 |
| BizDate | Long | 是 | 1606200230105 | 触发式节点实例所在的业务日期时间戳。 |
| CycleTime | Long | 是 | 1606200230105 | 触发式节点对应节点任务的定时时间戳。 |
| NodeId | Long | 是 | 10000011 | 触发式节点的节点ID。您可参见 ListNodes获取节点ID信息。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&AppId=10001 &BizDate=1606200230105 &CycleTime=1606200230105 &NodeId=10000011 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### RunCycleDagNodes

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | RunCycleDagNodes | 系统规定参数。取值： RunCycleDagNodes。 |
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| ProjectEnv | Strin g | Body | 是 | PROD | 工作空间的环境，PROD表示生产环境，DEV表示开发环境。 |
| StartBizDa te | Strin g | Body | 是 | 2020-05-20 00:00:00 | 补数据的起始业务日期。格式为yyyy-MM-dd 00:00:00。 |
| Name | Strin g | Body | 是 | xm test _ | 工作流的名称。 |
| RootNodeI d | Long | Body | 是 | 1234 | 补数据的起始节点ID。 |
| ExcludeNo deIds | Strin g | Body | 否 | 1234,123465 | 无需补数据的节点ID列表， 在这个列表中的节点会生成空跑实例，空跑实例被调度后会直接运行成功，不会执行脚本内容。 |
| BizBeginTi me | Strin g | Body | 否 | 00:00:00 | 任务的开始时间。仅小时调度任务需要设置该参数，格式为HH:mm:ss，取值范围为 00:00:00~23:59:59。 |
| BizEndTim e | Strin g | Body | 否 | 01:00:00 | 任务的结束时间。仅小时调度任务需要设置该参数，格式为HH:mm:ss，取值范围为 00:00:00~23:59:59。 |
| Parallelis m | Boole an | Body | 是 | false | 是否可以同时对多个节点进行补数据操作。 |
| EndBizDat e | Strin g | Body | 是 | 2020-05-21 00:00:00 | 补数据的结束业务日期。格式为yyyy-MM-dd 00:00:00。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NodePara ms | Strin g | Body | 否 | {74324:"a=123 b=456"} | 配置为一个JSON字符串，Key为节点ID，Value 为参数的实际取值。 |
| IncludeNo deIds | Strin g | Body | 是 | 74324,74325 | 补数据的节点ID。对多个节点补数据时，多个节点ID使用逗号（,）分隔。 |
| StartFutur eInstanceI mmediate ly | Boole an | Body | 否 | false | 是否立刻运行未来调度时间的实例。如果设置为true， 则大于当前时间的实例会立刻运行，否则会等待调度时间。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Long | 111 | 工作流ID的列表。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | default | 区域ID，为固定值default。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| Success | Boolean | true | 调用是否成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |

**示例**

请求示例

```
&RegionId=default &ProjectEnv=PROD &StartBizDate=2020-05-20 00:00:00 &Name=xm_test &RootNodeId=1234 &Parallelism=false &EndBizDate=2020-05-21 00:00:00 &IncludeNodeIds=74324,74325
```

&公共请求参数 DataWorks 正常返回示例 `JSON` 格式

```json
{
    "RequestId": "default",
    "HttpStatusCode": 200,
    "Data": 111,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

`XML` 格式

```xml
<RequestId>default</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>111</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

#### RunManualDagNodes

调用RunManualDagNodes执行手动业务流程。手动业务流程必须已经在环境界面提交发布，提交发布后运维中心才会显示对应手动业务流程，您才可以使用该接口调用执行。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RunManualDagN odes | 系统规定参数。取值： RunManualDagNodes。 |
| BizDate | String | 是 | 2020-11-11 00:00:00 | 业务日期的值为小于等于当前日期-1天。 例如，今天是2020年11月11日，则业务日期需要是2020年11月10日的00:00:00 或者该日期之前的日期。业务日期的时分秒信息均填写00。 |
| FlowName | String | 是 | test workflow _ | 手动业务流程的名称。 |
| ProjectEnv | String | 是 | PROD或者DEV | 调度运维中心的环境标识。PROD表示生产环境，DEV表示开发环境。 |
| ProjectName | String | 是 | test workspace _ | 手动业务流程所属的工作空间英文名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| NodeParameters | String | 否 | {"20000123121 ": "key1=val2 key2=val2", "20000123124": "kkkk=vvvvv aaaa=bbbb"} | 传递手动业务流程执行时的节点参数信息，一个JSON格式： { "<手动业务流程内部的某个节点ID>": "节点的调度参数信息，和数据开发调度配置里面的参数格式保持一致", "<手动业务流程内部的某个节点ID>": "节点的调度参数信息，和数据开发调度配置里面的参数格式保持一致" } |
|---|---|---|---|---|
| DagParameters | String | 否 | {"kaaaa": "vaaaaa", "kbbbb": "vbbbbb"} | 业务流程参数，该参数会同步至本次Dag 的所有实例中。如果内部节点的调度参数引用了DagParameters中的业务流程参数，则节点的对应参数值会被替换为 DagParameter中的业务流程参数。 |
| IncludeNodeIds | String | 否 | 74324,74325 | 如果需要运行手动业务流程里面部分节点 ID，可以设置该参数。多个节点ID使用逗号（,）分隔。您可以通过调用ListNodes 接口获取节点ID。 |
| ExcludeNodeIds | String | 否 | 123,456 | 如果不需要运行业务流程里面的部分节点 ID列表，在这个列表中的节点会生成空跑实例，空跑实例被调度后会直接运行成功，不会执行脚本内容。多个节点ID使用逗号（,）分隔。 |
| ProjectId | Long | 否 | 123 | 项目ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DagId | Long | 700000123123141 | 手动业务流程运行Dag的实例ID。您可以通过接口和该DagId查询此次手动业务流程运行的内部节点实例的详细信息和状态。 |
| RequestId | String | AASFDFSDFG- DFSDF-DFSDFD- SDFSDF | 请求唯一标识。 |

**示例**

请求示例

```
&BizDate=2020-11-11 00:00:00 &FlowName=test_workflow &ProjectEnv=PROD或者DEV &ProjectName=test_workspace &RegionId=default
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<RequestId>AASFDFSDFG-DFSDF-DFSDFD-SDFSDF</RequestId> <DagId>700000123123141</DagId>
```

`JSON` 格式

```json
{
    "RequestId": "AASFDFSDFG-DFSDF-DFSDFD-SDFSDF",
    "DagId": 700000123123141
}
```

#### RunSmokeTest

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RunSmokeTest | 系统规定参数。取值：RunSmokeTest。 |
| Bizdate | String | 是 | 2020-05-26 00:00:00 | 业务日期。 |
| Name | String | 是 | xm create test _ _ | 工作流的名称。 |
| NodeId | Long | 是 | 1234 | 节点的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD（生产环境）和DEV（开发环境）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| NodeParams | String | 否 | bizdate=$bizdat e tbods=$tbods | 节点的参数。配置为一个JSON字符串，Key为节点 ID，Value为参数实际取值。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Long | 3333333 | 工作流的ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |

DataWorks

| ErrorMessage | String | The connection does not exist. | 错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
&Bizdate=2020-05-26 00:00:00 &Name=xm_create_test &NodeId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>3333333</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": 3333333,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": false
}
```

#### SetSuccessInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | SetSuccessInsta nce | 系统规定参数。取值： SetSuccessInstance。 |
|---|---|---|---|---|
| InstanceId | Long | 是 | 1234 | 实例的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 调用SetSuccessInstance接口后，返回的结果详情。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SetSuccessInstance &InstanceId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### StopInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StopInstance | 系统规定参数。取值：StopInstance。 |
| InstanceId | Long | 是 | 1234 | 实例的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 调用停止实例接口后，返回的结果详情。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

DataWorks 请求示例

```
&InstanceId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### SuspendInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SuspendInstanc e | 系统规定参数。取值： SuspendInstance。 |
| InstanceId | Long | 是 | 1234 | 实例的ID。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 调用SuspendInstance接口后，返回的结果详情。 |
| ErrorCode | String | Invalid.Tenant.Proj ectNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0baf87f0159376*** * | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&InstanceId=1234 &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0baf87f0159376****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ProjectNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0baf87f0159376****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ProjectNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

DataWorks

#### TopTenElapsedTimeInstance

调用TopTenElapsedTimeInstance获取已运行完成（即运行状态为成功或失败）的实例运行时长的排行情况。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TopTenElapsedT imeInstance | 系统规定参数。取值： TopTenElapsedTimeInstance。 |
| ProjectId | Long | 是 | 100000 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceConsu meTimeRank | Struct |  | 实例运行时长的排行记录。 |
| ConsumeTime Rank | Array of ConsumeTime Rank |  | 实例运行时长的排行数据。 |
| BusinessDate | Long | 1600963200000 | 实例运行的业务日期。 |
| Consumed | Long | 1000 | 实例运行时长，单位为s。 |
| InstanceId | Long | 95279527 | 实例ID。 |
| NodeId | Long | 9527 | 任务节点的ID。 |
| NodeName | String | 节点名称 | 节点的名称。 |
| Owner | String | 952795279527 | 节点责任人的阿里云UID。 |

DataWorks

| ProgramType | Integer | 10 | 任务的类型。 常见的类型如下： 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
|---|---|---|---|
| UpdateTime | Long | 1600963200000 | 实例运行时长排行更新时间戳。 |
| RequestId | String | 6347364dadsfadf** ** | 请求ID。用于出现错误后排查问题。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=TopTenElapsedTimeInstance &ProjectId=100000 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>6347364dadsfadf****</RequestId> <InstanceConsumeTimeRank>
    <UpdateTime>1600963200000</UpdateTime>
    <ConsumeTimeRank>
        <Owner>952795279527</Owner>
        <BusinessDate>1600963200000</BusinessDate>
        <InstanceId>95279527</InstanceId>
```

`<NodeName>`节点名称`</NodeName>`

```xml
        <NodeId>9527</NodeId>
        <Consumed>1000</Consumed>
        <ProgramType>10</ProgramType>
    </ConsumeTimeRank>
</InstanceConsumeTimeRank>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "6347364dadsfadf****",
    "InstanceConsumeTimeRank": {
        "UpdateTime": 1600963200000,
        "ConsumeTimeRank": {
            "Owner": 952795279527,
            "BusinessDate": 1600963200000,
            "InstanceId": 95279527,
```

`"NodeName": "`节点名称`",`

```json
            "NodeId": 9527,
            "Consumed": 1000,
            "ProgramType": 10
        }
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### TopTenErrorTimesInstance

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TopTenErrorTim esInstance | 系统规定参数。取值： TopTenErrorTimesInstance。 |
| ProjectId | Long | 是 | 9527 | DataWorks工作空间的ID。您可以登录 DataWorks管控台，进入工作空间配置页面获取工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InstanceErrorR ank | Struct |  | 节点出错的排行数据。 |
| ErrorRank | Array of ErrorRank |  | 节点近一个月出错排行数据。 |
| Count | Integer | 5 | 节点出错的次数。 |
| NodeId | Long | 9527 | 节点的ID。 |
| NodeName | String | 节点的名称 | 节点的名称。 |
| Owner | String | 952795279527 | 节点责任人的阿里云UID。 |

DataWorks

| ProgramType | Integer | 10 | 节点任务的类型。 常用的类型如下： 6（Shell）、10（ODPS SQL）、11（ODPS MR）、23（数据集成）、24（ODPS Script）、99（虚拟节点）、221（PyODPS 2）、225（ODPS Spark）、227（EMR Hive）、228（EMR Spark）、229（EMR Spark SQL）、230（EMR MR）、239（OSS 对象检查）、257（EMR Shell）、258（EMR Spark Shell）、259（EMR Presto）、 260（EMR Impala）、900（实时同步）、 1089（跨租户节点）、1091（Hologres开发）、1093（Hologres SQL）、1100（赋值节点）、1221（PyODPS 3）。 |
|---|---|---|---|
| ProjectId | Long | 9527 | DataWorks工作空间的ID。 |
| UpdateTime | Long | 1600963200000 | 出错排行更新的时间戳。 |
| RequestId | String | 952795279527**** | 请求ID。用于出现错误后排查问题。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=TopTenErrorTimesInstance &ProjectId=9527 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>952795279527****</RequestId> <InstanceErrorRank>
    <UpdateTime>1600963200000</UpdateTime>
    <ErrorRank>
        <Owner>952795279527</Owner>
```

`<NodeName>`节点的名称`</NodeName>`

```xml
        <ProjectId>9527</ProjectId>
        <NodeId>9527</NodeId>
        <ProgramType>10</ProgramType>
        <Count>5</Count>
    </ErrorRank>
</InstanceErrorRank>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "952795279527****",
    "InstanceErrorRank": {
        "UpdateTime": 1600963200000,
        "ErrorRank": {
            "Owner": 952795279527,
```

`"NodeName": "`节点的名称`",`

```json
            "ProjectId": 9527,
            "NodeId": 9527,
            "ProgramType": 10,
            "Count": 5
        }
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 403 | ResourceNotAuthor ized.Api | You are not authorized to access the resources. | 您无法访问未取得授权的资源。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | Invalid.Wkbench.Pa rameter | The specified parameters are invalid. | 参数错误。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### UpdateRemind

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateRemind | 系统规定参数。取值：UpdateRemind。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RemindId | Long | 是 | 1234 | 自定义监控规则ID。 |
| RemindName | String | 否 | update remindn _ ame | 自定义规则的名称，不能超过128个字符。 |
| DndEnd | String | 否 | 08:00 | 免打扰截止时间，格式为hh:mm。hh的取值范围为0,23 ，mm的取值范围为0,59。 |
| RemindUnit | String | 否 | NODE | 对象的类型，包括NODE（任务节点）、 BASELINE（基线）、PROJECT（工作空间）和BIZPROCESS（业务流程）。 |
| NodeIds | String | 否 | 1,2,3 | 当RemindUnit（对象类型）为NODE（任务节点）时，监控的任务节点ID。多个ID 之间使用英文逗号（,）分隔，一个规则最多监控50个节点。 |
| BaselineIds | String | 否 | 1,2,3 | 当RemindUnit（对象类型）为 BASELINE（基线）时，监控的基线ID。 多个ID之间使用英文逗号（,）分隔，一个规则最多监控5条基线。 |
| ProjectId | Long | 否 | 1234 | 当RemindUnit（对象类型）为 PROJECT（工作空间）时，监控的工作空间ID。一个规则只能监控一个工作空间。 |
| BizProcessIds | String | 否 | 1,2,3 | 当RemindUnit（对象类型）为 BIZPROCESS（业务流程）时，监控的业务流程ID。多个ID之间使用英文逗号（,） 分隔，一个规则最多监控5个业务流程。 |

DataWorks

| RemindType | String | 否 | FINISHED | 触发条件，包括FINISHED（完成）、 UNFINISHED（未完成）、ERROR（出错）、 CYCLE UNFINISHED（周期未完 _ 成）和TIMEOUT（运行超时）。 |
|---|---|---|---|---|
| MaxAlertTimes | Integer | 否 | 3 | 最大报警次数。最小值为1，最大值为 10，默认值为3。 |
| AlertInterval | Integer | 否 | 1800 | 最小报警间隔，单位为秒。最小值为 1200，默认值为1800。 |
| Detail | String | 否 | {"hour":23,"min u":59} | 不同触发条件的说明如下： 当RemindType（触发条件）为 FINISHED（完成）时，传空。 当RemindType（触发条件）为 UNFINISHED（未完成）时，传参格式为{"hour":23,"minu":59}。hour的取值范围为0,47，minu的取值范围为0,59。 当RemindType（触发条件）为 ERROR（出错）时，传空。 当RemindType（触发条件）为 CYCLE UNFINISHED（周期未完成） _ 时，传参格式为 {"1":"05:50","2":"06:50","3":"07:5 0","4":"08:50","5":"09:50","6":"10: 50","7":"11:50","8":"12:50","9":"13 :50","10":"14:50","11":"15:50","12 ":"16:50","13":"17:50","14":"18:50 ","15":"19:50","16":"20:50","17":"2 1:50","18":"22:50","19":"23:50","2 0":"24:50","21":"25:50"}。JSON字符串key为周期号，取值范围为1,288。value为该周期对应的未完成时间，格式为hh:mm。hh的取值范围为0,47，mm的取值范围为0,59。 当RemindType（触发条件）为 TIMEOUT（运行超时）时，传参格式为 1800，单位为秒。即从开始运行起，运行超过30分钟触发报警。 |
| AlertUnit | String | 否 | OWNER | 报警接收对象的粒度，包括OWNER（任务责任人）和OTHER（指定的人）。 |
| AlertMethods | String | 否 | SMS,MAIL | 报警的方式，包括MAIL（邮件）、 SMS（短信）和 PHONE（电话，仅 DataWorks专业版及以上版本支持） 。多个报警方式之间使用英文逗号（,）分隔。 |

DataWorks

| AlertTargets | String | 否 | 9527952795279 527 | 当AlertUnit（报警接收人）为 OWNER（节点任务责任人）时，传空。 当AlertUnit报警接收人）为 OTHER（指定的人）时，传入指定用户的阿里云UID。多个阿里云UID之间使用英文逗号（,）分隔，最多支持10个。 |
|---|---|---|---|---|
| UseFlag | Boolean | 否 | true | 开启和关闭规则，包括true（开启）和 false（关闭）。 |
| RobotUrls | String | 否 | https://oapi.ding talk.com/robot/s end? access token=* _ **************** ************* | 钉钉群机器人的webhook地址，多个 webhook地址之间使用英文逗号（,）分隔。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 更新自定义监控规则是否成功，包括true（成功）和false（失败）。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&RegionId=default &RemindId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | Forbidden.Wkbenc h.BaselineNoPermi ssion | You are not authorized to access the baseline. | 无对应的基线权限。 |
| 500 | Forbidden.Wkbenc h.ProjectNoPermiss ion | You are not authorized to access the workspace. | 工作空间无权限。 |
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
|---|---|---|---|
| 500 | Forbidden.Wkbenc h.RemindNoPermis sion | You are not authorized to modify the reminder. | 无权限修改该自定义提醒规则。 |
| 500 | Invalid.Wkbench.Re mindNotExist | The reminder does not exist. | 自定义提醒规则不存在。 |

#### UpdateNodeOwner

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateNodeOwn er | 系统规定参数。取值： UpdateNodeOwner。 |
| NodeId | Long | 是 | 1234 | 节点的ID。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括开发环境（DEV）和生产环境（PRD）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| UserId | String | 是 | 1933790683655 1 | 节点负责人的阿里云账号ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 返回值。取值如下： true：表示调用成功。 false：表示调用失败。 |

**示例**

请求示例 DataWorks

```
&NodeId=1234 &ProjectEnv=PROD &RegionId=default &UserId=19337906836551
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "Success": true
}
```

#### UpdateNodeRunMode

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateNodeRun Mode | 系统规定参数。取值： UpdateNodeRunMode。 |
| NodeId | Long | 是 | 1234 | 节点的ID。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括开发环境（DEV）和生产环境（PRD）。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| SchedulerType | Integer | 是 | 0 | 需要对目标节点执行的操作。取值如下： 0：表示解冻目标节点。 2：表示冻结目标节点。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| RequestId | String | E6F0DBDD- 5AD**** | 请求的ID。用于定位日志，排查问题。 |
|---|---|---|---|
| Success | Boolean | true | 返回值。取值如下： true：表示调用成功。 false：表示调用失败。 |

**示例**

请求示例

```
&NodeId=1234 &ProjectEnv=PROD &RegionId=default &SchedulerType=0
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "E6F0DBDD-5AD****",
    "Success": true
}
```

### 数据质量

#### CreateQualityEntity

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateQualityEn tity | 系统规定参数。取值： CreateQualityEntity。 |
| EntityLevel | Integer | 是 | 0 | 包括0（SQl完成时校检）和1（task完成时校检）。 |

DataWorks

| EnvType | String | 是 | ODPS | 引擎或者数据源的类型。 |
|---|---|---|---|---|
| MatchExpression | String | 是 | dt=$[yyyymmdd ] | 分区表达式。 |
| ProjectName | String | 是 | autotest | 引擎的项目名称或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | dual | 表的名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Integer | 12345 | 新创建的分区表达式ID。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | Your project is not relative with your account. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP请求错误码。 |
| RequestId | String | 011e1231u3**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateQualityEntity &EntityLevel=0 &EnvType=ODPS &MatchExpression=dt=$[yyyymmdd] &ProjectName=autotest &RegionId=default &TableName=dual
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>011e1231u3****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>12345</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>Your project is not relative with your account.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "011e1231u3****",
    "HttpStatusCode": 200,
    "Data": 12345,
    "ErrorCode": 401,
    "ErrorMessage": "Your project is not relative with your account.",
    "Success": true
}
```

#### CreateQualityFollower

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateQualityFol lower | 系统规定参数。取值： CreateQualityFollower。 |
| AlarmMode | Integer | 是 | 1 | 订阅的方式，包括1（邮件）、2（邮件和短信）、4（钉钉群机器人）和5（钉钉群机器人@ALL）。 |
| EntityId | Long | 是 | 12345 | 分区表达式的ID。 |
| Follower | String | 是 | 123 | 订阅人的账号ID。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Integer | 12345 | 新创建的订阅关系ID。 |
|---|---|---|---|
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP错误码。 |
| RequestId | String | ecb967ec-c137- 48**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateQualityFollower &AlarmMode=1 &EntityId=12345 &Follower=123 &ProjectName=autotest &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>ecb967ec-c137-48****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>12345</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "ecb967ec-c137-48****",
    "HttpStatusCode": 200,
    "Data": 12345,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

DataWorks

#### CreateQualityRelativeNode

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateQualityRe lativeNode | 系统规定参数。取值： CreateQualityRelativeNode。 |
| EnvType | String | 是 | CreateQualityRe lativeNode | 引擎或者数据源的类型。 |
| MatchExpression | String | 是 | ODPS | 分区表达式。 |
| NodeId | Long | 是 | 12321 | 调度节点ID。 |
| ProjectId | Long | 是 | 123 | 工作空间的ID。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | dual | 表的名称。 |
| TargetNodeProje ctId | Long | 是 | 1234 | 关联调度的节点ID。 |
| TargetNodeProje ctName | String | 是 | autotest | 关联调度的节点项目。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否关联成功。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP错误码。 |

DataWorks

| RequestId | String | ecb967ec-c137- 48**** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateQualityRelativeNode &MatchExpression=ODPS &NodeId=12321 &ProjectId=123 &ProjectName=autotest &RegionId=default &TableName=dual
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>ecb967ec-c137-48****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "ecb967ec-c137-48****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### CreateQualityRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | CreateQualityRu le | 系统规定参数。取值： CreateQualityRule。 |
|---|---|---|---|---|
| BlockType | Integer | 是 | 0 | 规则的强弱：0表示弱规则，1表示强规则。 |
| Checker | Integer | 是 | 9 | 校验器的ID。 |
| EntityId | Long | 是 | 15224 | 分区表达式的ID。 |
| MethodName | String | 是 | count/table cou _ nt | 采样方。如果是自定义SQL，该参数的值为user define。 _ |
| PredictType | Integer | 是 | 0 | 是否为动态阈值：0表示非动态阈值、1表示动态阈值规则。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RuleName | String | 是 | 1234 | 规则的名称。 |
| RuleType | Integer | 是 | 0 | 规则的类型：0表示系统定义、1表示用户自定义、2表示项目级规则。 |
| Comment | String | 否 | 验证 | 规则的描述信息。 |
| ExpectValue | String | 否 | 0 | 期望值。 |
| Trend | String | 否 | abs | 趋势。 |
| Operator | String | 否 | > | 比较符。 |
| Property | String | 否 | table id _ | 规则的字段。如果是表级别校验，行数为 table count、大小为table size字段。 _ _ |
| PropertyType | String | 否 | bigint | 字段的类型，表级table，字段级填写 bigint等。 |
| WhereCondition | String | 否 | table id>1 _ | 过滤条件或自定义SQL。 |

DataWorks

| CriticalThreshold | String | 否 | 20 | 橙色阈值。 |
|---|---|---|---|---|
| WarningThreshol d | String | 否 | 10 | 红色阈值。 |
| TemplateId | Integer | 否 | 7 | 模板的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | String | 12345 | 新建的规则ID。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | ecb967ec-c137- 48**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&BlockType=0 &Checker=9 &EntityId=15224 &MethodName=count/table_count &PredictType=0 &ProjectName=autotest &RegionId=default &RuleName=1234 &RuleType=0
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>ecb967ec-c137-48****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>12345</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "ecb967ec-c137-48****",
    "HttpStatusCode": 200,
    "Data": 12345,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### DeleteQualityEntity

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteQualityEn tity | 系统规定参数。取值： DeleteQualityEntity。 |
| EntityId | Long | 是 | 1234 | 分区表达式的ID。 |
| EnvType | String | 是 | ODPS | 引擎或者数据源的类型。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 调用DeleteQualityEntity接口后，返回的结果详情。 |
| ErrorCode | String | 401 | 错误码。 |

DataWorks

| ErrorMessage | String | You have no permission. | 错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP错误码。 |
| RequestId | String | ecb967ec-c137- 48**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteQualityEntity &EntityId=1234 &EnvType=ODPS &ProjectName=autotest &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>ecb967ec-c137-48****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "ecb967ec-c137-48****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### DeleteQualityFollower

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | DeleteQualityFol lower | 系统规定参数。取值： DeleteQualityFollower。 |
|---|---|---|---|---|
| FollowerId | Long | 是 | 1234 | 订阅人。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 删除是否成功。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 6d739ef6-098a- 47**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteQualityFollower &FollowerId=1234 &ProjectName=autotest &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>6d739ef6-098a-47****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "6d739ef6-098a-47****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### DeleteQualityRelativeNode

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteQualityRel ativeNode | 系统规定参数。取值： DeleteQualityRelativeNode。 |
| EnvType | String | 是 | ODPS | 引擎或者数据源的类型。 |
| MatchExpression | String | 是 | dt=$[yyyymmdd ] | 分区表达式。 |
| NodeId | Long | 是 | 156234 | 节点ID。 |
| ProjectId | Long | 是 | 12345 | 工作空间的ID。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | dual | 表的名称。 |
| TargetNodeProje ctId | Long | 是 | 12345 | 关联调度节点的项目ID。 |
| TargetNodeProje ctName | String | 是 | autotest | 关联调度节点的项目。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Boolean | true | 删除是否成功。 |
|---|---|---|---|
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP错误码。 |
| RequestId | String | 6d739ef6-098a- 47**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteQualityRelativeNode &EnvType=ODPS &MatchExpression=dt=$[yyyymmdd] &NodeId=156234 &ProjectId=12345 &ProjectName=autotest &RegionId=default &TableName=dual
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>6d739ef6-098a-47****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "6d739ef6-098a-47****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### DeleteQualityRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteQualityRul e | 系统规定参数。取值： DeleteQualityRule。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RuleId | Long | 是 | 1234 | 规则ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 删除是否成功。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 6d739ef6-098a- 47**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例 DataWorks

```
&ProjectName=autotest &RegionId=default &RuleId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>6d739ef6-098a-47****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "6d739ef6-098a-47****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### GetQualityEntity

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetQualityEntity | 系统规定参数。取值： GetQualityEntity。 |
| EnvType | String | 是 | odps | 引擎或数据源的类型。 |
| MatchExpression | String | 是 | dt=$[yyyymmdd ] | 分区表达式。 |
| ProjectName | String | 是 | autotest | 引擎或数据源的名称。您可以从数据源配置中获取名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| TableName | String | 是 | dual | 分区表名称。您可以调用查看分区表名称。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of EntityDto |  | 返回信息。 |
| CreateTime | Long | 1593964800000 | 创建分区表达式的时间。 |
| EntityLevel | Integer | 0 | 分区表达式的级别，取值如下： 0（SQL级别），指每段SQL语句执行完毕后都会触发DQC执行校验。 1（任务级别），指所有SQL语句均执行完毕后，统一进行校验。 |
| EnvType | String | odps | 引擎或者数据源的类型。 |
| Followers | String | 1822931**** | 订阅人，接收告警信息的阿里云账号ID。 |
| HasRelativeNo de | Boolean | true | 是否关联调度，取值如下： true，已关联调度。 false，未关联调度。 |
| Id | Long | 4003918 | 分区表达式ID。 |
| MatchExpressi on | String | dt=$[yyyymmdd- 1] | 分区表达式。 |
| ModifyTime | Long | 1593964800000 | 更新分区表达式的时间。 |
| ModifyUser | String | 1822931**** | 更新人，指更新分区表达式的账号ID。 |
| OnDuty | String | 1822931**** | 责任人，指配置分区表达式的账号ID。 |
| ProjectName | String | autotest | 引擎或数据源的名称。 |
| RelativeNode | String | [{"projectName":"x c DP****","nodeId" _ :7000026****}] | 分区表达式关联的调度节点信息，包括： ProjectName，调度节点所在的项目名称。 NodeID，调度节点的节点ID。 |

DataWorks

| Sql | Integer | 0 | SQL级别的分区表达式。 |
|---|---|---|---|
| TableName | String | test dqc de**** _ _ | 分区表名称。 |
| Task | Integer | 0 | 任务节点。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 6d739ef6-098a- 47**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&EnvType=odps &MatchExpression=dt=$[yyyymmdd] &ProjectName=autotest &RegionId=default &TableName=dual
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>6d739ef6-098a-47****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <ModifyTime>1593964800000</ModifyTime>
    <Task>0</Task>
    <ModifyUser>1822931****</ModifyUser>
    <HasRelativeNode>true</HasRelativeNode>
    <ProjectName>autotest</ProjectName>
    <CreateTime>1593964800000</CreateTime>
    <OnDuty>1822931****</OnDuty>
    <Followers>1822931****</Followers>
    <MatchExpression>dt=$[yyyymmdd-1]</MatchExpression>
    <EnvType>odps</EnvType>
    <Sql>0</Sql>
    <TableName>test_dqc_de****</TableName>
    <Id>4003918</Id>
    <RelativeNode>[{"projectName":"xc_DP****","nodeId":7000026****}]</RelativeNode>
    <EntityLevel>0</EntityLevel>
</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "6d739ef6-098a-47****",
    "HttpStatusCode": 200,
    "Data": {
        "ModifyTime": 1593964800000,
        "Task": 0,
        "ModifyUser": "1822931****",
        "HasRelativeNode": true,
        "ProjectName": "autotest",
        "CreateTime": 1593964800000,
        "OnDuty": "1822931****",
        "Followers": "1822931****",
        "MatchExpression": "dt=$[yyyymmdd-1]",
        "EnvType": "odps",
        "Sql": 0,
        "TableName": "test_dqc_de****",
        "Id": 4003918,
        "RelativeNode": "[{\"projectName\":\"xc_DP****\",\"nodeId\":7000026****}]",
        "EntityLevel": 0
    },
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### GetQualityFollower

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetQualityFollo wer | 系统规定参数。取值： GetQualityFollower。 |
| EntityId | Long | 是 | 1234 | 分区表达式的ID。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of Follower |  | 订阅关系的信息。 |
| AlarmMode | Integer | 1 | 告警的模式，取值如下： 1（邮件） 2（邮件和短信） 4（钉钉群机器人或hook） 5（钉钉群机器人@ALL） |
| EntityId | String | 1234 | 分区表达式的ID。 |
| Follower | String | 1234 | 订阅人，用于接收告警信息。 |
| Id | Long | 123 | 订阅关系的ID。 |
| ProjectName | String | autotest | 引擎或者数据源的名称。 |
| TableName | String | dual | 分区表的名称。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |

DataWorks

| RequestId | String | 38cbdef0-f6cf-49 | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetQualityFollower &EntityId=1234 &ProjectName=autotest &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>38cbdef0-f6cf-49</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <EntityId>1234</EntityId>
    <TableName>dual</TableName>
    <ProjectName>autotest</ProjectName>
    <Follower>1234</Follower>
    <Id>123</Id>
    <AlarmMode>1</AlarmMode>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "38cbdef0-f6cf-49",
    "HttpStatusCode": 200,
    "Data": {
        "EntityId": 1234,
        "TableName": "dual",
        "ProjectName": "autotest",
        "Follower": 1234,
        "Id": 123,
        "AlarmMode": 1
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

DataWorks

#### GetQualityRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetQualityRule | 系统规定参数。取值：GetQualityRule。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| RuleId | Long | 是 | 1234 | 校验规则的ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 获取的规则信息。 |
| BlockType | Integer | 1 | 校验规则的强弱。强弱表示规则的重要程度。取值如下： 1，表示强规则。 0，表示弱规则。 您可以根据实际需求设置重要的规则为强规则。 如果使用强规则并触发了红色告警，则会阻塞调度任务。 |
| Checker | Integer | 9 | 校验器ID。该字段对应前端的ID标识，需要由 pkId转换。 |
| CheckerName | String | compared with a fixed value | 校验器的名称。 |
| Comment | String | 校验主键唯一 | 校验规则的描述信息。 |
| CriticalThresho ld | String | 20 | 红色告警阈值。表示与样本预期的偏离程度。您可以根据业务需求自定义该阈值。使用强规则并触发红色阈值，会阻塞调度任务。 |
| EntityId | Long | 165523 | 分区表达式的ID。 |
| ExpectValue | String | 30 | 期望值。 |

DataWorks

| FixCheck | Boolean | true | 固定值校验。 |
|---|---|---|---|
| Id | Long | 123232 | 规则的ID。 |
| MethodId | Integer | 8 | 采集样本数据方法的ID。 |
| MethodName | String | table count _ | 采集样本数据方法的名称。包括avg、count、 sum、min、max、count distinct、 _ user defined、table count、table size、 _ _ _ table dt load count、 _ _ _ table dt refuseload count、null value、 _ _ _ _ null value/table count、(table count- _ _ _ count distinct)/table count、table count- _ _ _ count distinct等。 _ |
| OnDuty | String | 1822931**** | 配置校验规则的账号ID。 |
| Operator | String | >= | 操作符。 |
| PredictType | Integer | 0 | 操作符。是否为动态阈值： 0表示非动态阈值。 1表示动态阈值规则。 |
| Property | String | id | 规则属性的字段，即被校验数据源表的column 名称。 |
| RuleName | String | 查看表波动 | 规则的名称。 |
| RuleType | Integer | 0 | 规则的类型。 |
| TemplateId | Integer | 7 | 使用的校验模板的ID。 |
| TemplateNam e | String | SQL task table rows, 1,7, 30 days fluctuation test | 使用的校验模板的名称。 |
| Trend | String | abs | 校验结果的趋势。 |
| WarningThres hold | String | 10 | 橙色告警阈值。表示与样本预期的偏离程度，您可以根据业务需求自定义该阈值。 |
| WhereConditio n | String | id>10 | 校验任务使用的过滤条件或自定义SQL语句。 |

DataWorks

| ErrorCode | String | 401 | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 576b9457-2cf5- 4**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&ProjectName=autotest &RegionId=default &RuleId=1234
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>576b9457-2cf5-4****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Operator>&gt;=</Operator>
```

`<Comment>`校验主键唯一`</Comment>`

```xml
    <Checker>9</Checker>
    <CriticalThreshold>20</CriticalThreshold>
    <CheckerName>compared with a fixed value</CheckerName>
    <ExpectValue>30</ExpectValue>
    <WarningThreshold>10</WarningThreshold>
    <Trend>abs</Trend>
    <OnDuty>1822931****</OnDuty>
    <WhereCondition>id&gt;10</WhereCondition>
    <RuleType>0</RuleType>
    <EntityId>165523</EntityId>
    <MethodId>8</MethodId>
    <FixCheck>true</FixCheck>
    <BlockType>1</BlockType>
    <PredictType>0</PredictType>
    <TemplateName>SQL task table rows, 1,7, 30 days fluctuation test</TemplateName>
    <MethodName>table_count</MethodName>
    <Id>123232</Id>
    <Property>id</Property>
```

`<RuleName>`查看表波动`</RuleName>`

```xml
    <TemplateId>7</TemplateId>
</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "576b9457-2cf5-4****",
    "HttpStatusCode": 200,
    "Data": {
        "Operator": "&gt;=",
```

`"Comment": "`校验主键唯一`",`

```json
        "Checker": 9,
        "CriticalThreshold": 20,
        "CheckerName": "compared with a fixed value",
        "ExpectValue": 30,
        "WarningThreshold": 10,
        "Trend": "abs",
        "OnDuty": "1822931****",
        "WhereCondition": "id&gt;10",
        "RuleType": 0,
        "EntityId": 165523,
        "MethodId": 8,
        "FixCheck": true,
        "BlockType": 1,
        "PredictType": 0,
        "TemplateName": "SQL task table rows, 1,7, 30 days fluctuation test",
        "MethodName": "table_count",
        "Id": 123232,
        "Property": "id",
```

`"RuleName": "`查看表波动`",`

```json
        "TemplateId": 7
    },
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### ListQualityResultsByEntity

调用ListQualityResultsByEntity，根据分区表达式查询历史校验结果。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListQualityResult sByEntity | 系统规定参数。取值： ListQualityResultsByEntity。 |
| EndDate | String | 是 | 2020-09-21 00:00:00 | 查询校验结果的截止时间，格式为yyyy- MM-dd HH:mm:ss。 |
| EntityId | Integer | 是 | 152322134 | 分区表达式ID。您可以调用 GetQualityEntity获取分区表达式ID。 |

DataWorks

| PageNumber | Integer | 是 | 1 | 页码数。 |
|---|---|---|---|---|
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。您可以从数据源配置中获取名称。 |
| StartDate | String | 是 | 2020-09-20 00:00:00 | 查询校验结果的开始时间，格式为yyyy- MM-dd HH:mm:ss。 |
| RegionId | String | 否 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 校验结果的顶层结构体。 |
| PageNumber | Integer | 1 | 页码数。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| RuleChecks | Array of RuleChecks |  | 校验结果的列表。 |
| ActualExpressi on | String | ds=20200912 | 被校验的数据源表的实际分区。 |
| BeginTime | Long | 1600704000000 | 执行校验操作的开始时间。 |
| BizDate | Long | 1600704000000 | 业务日期。如果被校验的业务主体为离线数据， 则业务日期通常为执行校验操作的前一天。 |
| BlockType | Integer | 0 | 校验规则的强弱。强弱表示规则的重要程度。取值如下： 1，表示强规则。 0，表示弱规则。 您可以根据实际需求设置重要的规则为强规则。如果使用强规则并触发了红色告警，则会阻塞调度任务。 |
| CheckResult | Integer | 0 | 校验结果： 0：正常 1：橙色告警 2：红色告警 |

DataWorks

| CheckResultSt atus | Integer | 0 | 校验结果状态： 0：正常 1：橙色告警 2：红色告警 |
|---|---|---|---|
| CheckerId | Integer | 7 | 校验器的ID。 |
| CheckerName | String | fulx | 校验器的名称。 |
| CheckerType | Integer | 1 | 校验类型。取值如下： 1，波动比较（VOLATILITY CHECK） _ 2，固定值比较（FIXEDVALUE CHECK） _ |
| Comment | String | 校验规则的描述。 | 校验规则的描述。 |
| CriticalThresho ld | Float | 0.5 | 红色阈值。表示与样本预期的偏离程度。您可以根据业务需求自定义该阈值。使用强规则并触发红色阈值，会阻塞调度任务。 |
| DateType | String | YMD | 调度周期的类型。通常为YMD，即年任务、月任务、天任务。 |
| DiscreteCheck | Boolean | true | 是否为离散校验。取值如下： true：是离散校验。 false：非离散校验。 |
| EndTime | Long | 1600704000000 | 查询校验结果的截止时间。 |
| EntityId | Integer | 15432322 | 分区表达式ID。 |
| ExpectValue | Float | 200 | 期望值。 |
| ExternalId | String | 1112323123 | 调度任务的节点ID。 |
| ExternalType | String | CWF | 调度系统的类型。目前仅支持CWF。 |
| FixedCheck | Boolean | false | 是否为固定值校验。取值如下： true：是固定值校验。 false：非固定值校验。 |

DataWorks

| Id | Integer | 121212121 | 主键ID。 |
|---|---|---|---|
| IsPrediction | Boolean | false | 是否为预测的结果。取值如下： true：是预测的结果。 false：不是预测的结果。 |
| LowerValue | Float | 2344 | 预测结果的下限。根据您设置的阈值自动生成。 |
| MatchExpressi on | String | ds=$[yyyymmdd] | 分区表达式。 |
| MethodName | String | count distinct _ | 采集样本数据的方法。包括avg、count、 sum、min、max、count distinct、 _ user defined、table count、table size、 _ _ _ table dt load count、 _ _ _ table dt refuseload count、null value、 _ _ _ _ null value/table count、(table count- _ _ _ count distinct)/table count、table count- _ _ _ count distinct等。 _ |
| Op | String | > | 比较符。 |
| ProjectName | String | autotest | 需要进行数据质量校验的引擎或者数据源名称。 |
| Property | String | type | 规则属性的字段，即被校验数据源表的column 名称。 |
| ReferenceValu e | Array of ReferenceValu e |  | 历史样本值。 |
| BizDate | String | 2020-12-03 | 业务日期。如果被校验的业务主体为离线数据， 则业务日期通常为执行校验操作的前一天。 |
| DiscreteProper ty | String | 0 | 通过group by分组后的样本字段取值。例如 group by性别字段，则DiscreteProperty为男生、女生和null。 |
| SingleCheckRe sult | Integer | 0 | 校验结果。 |
| Threshold | Float | 0.5 | 阈值。 |
| Value | Float | 19 | 校验值。 |
| ResultString | String | test | 校验结果的字符串形式。 |

DataWorks

| RuleId | Integer | 123123232 | 规则ID。 |
|---|---|---|---|
| RuleName | String | 规则的名称。 | 规则的名称。 |
| SampleValue | Array of SampleValue |  | 当前使用的样本。 |
| BizDate | String | 2020-12-03 | 业务日期。如果被校验的业务主体为离线数据， 则业务日期通常为执行校验操作的前一天。 |
| DiscreteProper ty | String | 0 | 通过group by分组后的样本字段取值。例如 group by性别字段，则DiscreteProperty为男生、女生和null。 |
| Value | Float | 19 | 当前样本值。 |
| TableName | String | dual | 进行校验的表名称。 |
| TaskId | String | 16008552981681a 0d6**** | 校验任务的ID。 |
| TemplateId | Integer | 5 | 使用的校验模板的ID。 |
| TemplateNam e | String | 字段唯一值个数期望值校验 | 使用的校验模板的名称。 |
| TimeCost | String | 202 | 执行校验任务花费的时间，单位为秒。 |
| Trend | String | abs | 校验结果的趋势。 |
| UpperValue | Float | 25555 | 预测上限。设置阈值后自动生成。 |
| WarningThres hold | Float | 0.1 | 橙色阈值。表示与样本预期的偏离程度，您可以根据业务需求自定义该阈值。 |
| WhereConditio n | String | id>0 | 校验任务使用的规则过滤条件。 |
| TotalCount | Long | 50 | 数据的总记录数。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |

DataWorks

| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListQualityResultsByEntity &EndDate=2020-09-21 00:00:00 &EntityId=152322134 &PageNumber=1 &PageSize=10 &ProjectName=autotest &StartDate=2020-09-20 00:00:00
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>50</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <RuleChecks>
        <Op>&gt;</Op>
        <TaskId>16008552981681a0d6****</TaskId>
        <CheckerName>fulx</CheckerName>
        <DiscreteCheck>true</DiscreteCheck>
        <EndTime>1600704000000</EndTime>
        <ProjectName>autotest</ProjectName>
        <ExpectValue>200</ExpectValue>
        <WarningThreshold>0.1</WarningThreshold>
        <RuleId>123123232</RuleId>
        <BeginTime>1600704000000</BeginTime>
        <WhereCondition>id&gt;0</WhereCondition>
        <CheckResultStatus>0</CheckResultStatus>
        <MatchExpression>ds=$[yyyymmdd]</MatchExpression>
        <UpperValue>25555</UpperValue>
        <IsPrediction>false</IsPrediction>
        <CheckResult>0</CheckResult>
```

`<TemplateName>`字段唯一值个数期望值校验`</TemplateName>`

```xml
        <FixedCheck>false</FixedCheck>
        <TimeCost>202</TimeCost>
        <MethodName>count_distinct</MethodName>
        <ResultString>test</ResultString>
        <DateType>YMD</DateType>
```

DataWorks

```xml
        <Property>type</Property>
```

`<RuleName>`规则的名称。`</RuleName>`

```xml
        <TemplateId>5</TemplateId>
        <BizDate>1600704000000</BizDate>
```

`<Comment>`校验规则的描述。`</Comment>`

```xml
        <CriticalThreshold>0.5</CriticalThreshold>
        <ExternalId>1112323123</ExternalId>
        <CheckerType>1</CheckerType>
        <Trend>abs</Trend>
        <ExternalType>CWF</ExternalType>
        <CheckerId>7</CheckerId>
        <EntityId>15432322</EntityId>
        <TableName>dual</TableName>
        <BlockType>0</BlockType>
        <ActualExpression>ds=20200912</ActualExpression>
        <Id>121212121</Id>
        <LowerValue>2344</LowerValue>
        <ReferenceValue>
            <SingleCheckResult>0</SingleCheckResult>
            <Value>19</Value>
            <DiscreteProperty>0</DiscreteProperty>
            <BizDate>2020-12-03</BizDate>
            <Threshold>0.5</Threshold>
        </ReferenceValue>
        <SampleValue>
            <Value>19</Value>
            <DiscreteProperty>0</DiscreteProperty>
            <BizDate>2020-12-03</BizDate>
        </SampleValue>
    </RuleChecks>
</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式 DataWorks

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data": {"TotalCount":"50","PageSize":"10","PageNumber":"1","RuleChecks": [{"Op":">","TaskId":"16008552981681a0d6****","CheckerName":"fulx","DiscreteCheck":"true", ndTime":"1600704000000","ProjectName":"autotest","ExpectValue":"200","WarningThreshold":" 1","RuleId":"123123232","BeginTime":"1600704000000","WhereCondition":"id>0","CheckResultS tus":"0","MatchExpression":"ds=$[yyyymmdd]","UpperValue":"25555","IsPrediction":"false","
```

`eckResult":"0","TemplateName":"`字段唯一值个数期望值校

```
验","FixedCheck":"false","TimeCost":"202","MethodName":"count_distinct","ResultString":"te t","DateType":"YMD","Property":"type","RuleName":"规则的名称。 ","TemplateId":"5","BizDate":"1600704000000","Comment":"校验规则的描述。","CriticalThresho ld":"0.5","ExternalId":"1112323123","CheckerType":"1","Trend":"abs","ExternalType":"CWF", heckerId":"7","EntityId":"15432322","TableName":"dual","BlockType":"0","ActualExpression" ds=20200912","Id":"121212121","LowerValue":"2344","ReferenceValue": [{"SingleCheckResult":"0","Value":"19","DiscreteProperty":"0","BizDate":"2020-12-03","T hreshold":"0.5"}],"SampleValue":[{"Value":"19","DiscreteProperty":"0","BizDate":"2020-1 2-03"}]}]},"ErrorCode":"401","ErrorMessage":"You have no permission.","Success":"false"}
```

#### ListQualityResultsByRule

调用ListQualityResultsByRule，根据校验规则校验数据源的质量，并查询校验结果。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListQualityResult sByRule | 系统规定参数。取值： ListQualityResultsByRule。 |
| EndDate | String | 是 | 2020-09-22 00:00:00 | 查询校验结果的截止时间，格式为yyyy- MM-dd HH:mm:ss。 |
| PageNumber | Integer | 是 | 1 | 页码数。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectName | String | 是 | autotest | 需要进行数据质量校验的引擎或者数据源名称。 |
| RuleId | Integer | 是 | 152322134 | 使用的校验规则ID。您可以使用该规则ID 与分区表达式等信息进行联合查询。 |
| StartDate | String | 是 | 2020-09-20 00:00:00 | 查询校验结果的开始时间，格式为yyyy- MM-dd HH:mm:ss。 |
| RegionId | String | 否 | default | 区域ID，为固定值default。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 校验结果的顶层结构体。 |
| PageNumber | Integer | 1 | 页码数。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| RuleChecks | Array of RuleChecks |  | 校验结果的列表。 |
| ActualExpressi on | String | ds=20200925 | 被校验的数据源表的实际分区。 |
| BeginTime | Long | 1600704000000 | 执行校验操作的开始时间。 |
| BizDate | Long | 1600704000000 | 业务日期。如果被校验的业务主体为离线数据， 则业务日期通常为执行校验操作的前一天。 |
| BlockType | Integer | 1 | 校验规则的强弱。强弱表示规则的重要程度。取值如下： 1，表示强规则。 0，表示弱规则。 您可以根据实际需求设置重要的规则为强规则。如果使用强规则并触发了红色告警，则会阻塞调度任务。 |
| CheckResult | Integer | 2 | 校验结果，0正常 1橙色告警 2红色告警 |
| CheckResultSt atus | Integer | 2 | 校验结果状态，0正常 1告警 2阻塞 |
| CheckerId | Integer | 7 | 校验器的ID。 |
| CheckerName | String | fulx | 校验器的名称。 |
| CheckerType | Integer | 0 | 校验器的类型。 |
| Comment | String | 校验规则的描述。 | 校验规则的描述。 |
| CriticalThresho ld | Float | 0.6 | 红色阈值。表示与样本预期的偏离程度。您可以根据业务需求自定义该阈值。使用强规则并触发红色阈值，会阻塞调度任务。 |

DataWorks

| DateType | String | YMD | 调度周期的类型。通常为YMD，即年任务、月任务、天任务。 |
|---|---|---|---|
| DiscreteCheck | Boolean | false | 是否为离散校验。取值如下： true：是离散校验。 false：非离散校验。 |
| EndTime | Long | 1600704000000 | 查询校验结果的截止时间。 |
| EntityId | Integer | 14534343 | 分区表达式ID。 |
| ExpectValue | Float | 90 | 期望值。 |
| ExternalId | String | 123112232 | 调度任务的节点ID。 |
| ExternalType | String | CWF | 调度系统的类型。目前仅支持CWF。 |
| FixedCheck | Boolean | false | 是否为固定值校验。取值如下： true：是固定值校验。 false：非固定值校验。 |
| Id | Integer | 2231123 | 主键ID。 |
| IsPrediction | Boolean | false | 是否为预测的结果。取值如下： true：是预测的结果。 false：不是预测的结果。 |
| LowerValue | Float | 2344 | 预测下限。根据您设置的阈值自动生成。 |
| MatchExpressi on | String | ds=$[yyyymmdd] | 分区表达式。 |
| MethodName | String | max | 采集样本数据的方法。包括avg、count、 sum、min、max、count distinct、 _ user defined、table count、table size、 _ _ _ table dt load count、 _ _ _ table dt refuseload count、null value、 _ _ _ _ null value/table count、(table count- _ _ _ count distinct)/table count、table count- _ _ _ count distinct等。 _ |
| Op | String | > | 比较符。 |

DataWorks

| ProjectName | String | autotest | 需要进行数据质量校验的引擎或者数据源名称。 |
|---|---|---|---|
| Property | String | type | 规则属性的字段，即被校验数据源表的column 名称。 |
| ReferenceValu e | Array of ReferenceValu e |  | 历史样本值。 |
| BizDate | Long | 1600704000000 | 业务日期。如果被校验的业务主体为离线数据， 则业务日期通常为执行校验操作的前一天。 |
| DiscreteProper ty | String | type1 | 通过group by分组后的样本字段取值。例如 group by性别字段，则DiscreteProperty为男生、女生和null。 |
| SingleCheckRe sult | Integer | 2 | 校验结果的字符串。 |
| Threshold | Float | 0.2 | 阈值。 |
| Value | Float | 20 | 样本值。 |
| ResultString | String | ResultString | 校验结果的字符串形式。 |
| RuleId | Integer | 123421 | 规则ID。 |
| RuleName | String | 规则的名称。 | 规则的名称。 |
| SampleValue | Array of SampleValue |  | 当前使用的样本。 |
| BizDate | Long | 1600704000000 | 业务日期。如果被校验的业务主体为离线数据， 则业务日期通常为执行校验操作的前一天。 |
| DiscreteProper ty | String | type2 | 通过group by分组后的样本字段取值。例如 group by性别字段，则DiscreteProperty为男生、女生和null。 |
| Value | Float | 23 | 样本值。 |
| TableName | String | dual | 进行校验的表名称。 |
| TaskId | String | 16008552981681a 0d6**** | 校验任务的ID。 |

DataWorks

| TemplateId | Integer | 5 | 使用的校验模板的ID。 |
|---|---|---|---|
| TemplateNam e | String | 字段唯一值个数期望值校验 | 使用的校验模板的名称。 |
| TimeCost | String | 10 | 执行校验任务花费的时间。 |
| Trend | String | up | 校验结果的趋势。 |
| UpperValue | Float | 22200 | 预测上限。设置阈值后自动生成。 |
| WarningThres hold | Float | 0.1 | 橙色阈值。表示与样本预期的偏离程度，您可以根据业务需求自定义该阈值。 |
| WhereConditio n | String | type!='type2' | 校验任务使用的过滤条件。 |
| TotalCount | Long | 200 | 数据的总记录数。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListQualityResultsByRule &EndDate=2020-09-22 00:00:00 &PageNumber=1 &PageSize=10 &ProjectName=autotest &RuleId=152322134 &StartDate=2020-09-20 00:00:00
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ReqestId>0000ABCDEFG*****</ReqestId>
```

DataWorks

|  | <RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data> <TotalCount>200</TotalCount> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <RuleChecks> <Op>&gt;</Op> <TaskId>16008552981681a0d6****</TaskId> <CheckerName>fulx</CheckerName> <DiscreteCheck>false</DiscreteCheck> <EndTime>1600704000000</EndTime> <ProjectName>autotest</ProjectName> <ExpectValue>90</ExpectValue> <WarningThreshold>0.1</WarningThreshold> <RuleId>123421</RuleId> <BeginTime>1600704000000</BeginTime> <WhereCondition>type!='type2'</WhereCondition> <CheckResultStatus>2</CheckResultStatus> <MatchExpression>ds=$[yyyymmdd]</MatchExpression> <UpperValue>22200</UpperValue> <IsPrediction>false</IsPrediction> <CheckResult>2</CheckResult> <TemplateName>字段唯一值个数期望值校验</TemplateName> <FixedCheck>false</FixedCheck> <TimeCost>10</TimeCost> <MethodName>max</MethodName> <ResultString>ResultString</ResultString> <DateType>YMD</DateType> <Property>type</Property> <RuleName>规则的名称。</RuleName> <TemplateId>5</TemplateId> <BizDate>1600704000000</BizDate> <Comment>校验规则的描述。</Comment> <CriticalThreshold>0.6</CriticalThreshold> <ExternalId>123112232</ExternalId> <CheckerType>0</CheckerType> <Trend>up</Trend> <ExternalType>CWF</ExternalType> <CheckerId>7</CheckerId> <EntityId>14534343</EntityId> <TableName>dual</TableName> <BlockType>1</BlockType> <ActualExpression>ds=20200925</ActualExpression> <Id>2231123</Id> <LowerValue>2344</LowerValue> <ReferenceValue> <SingleCheckResult>2</SingleCheckResult> <Value>20</Value> <DiscreteProperty>type1</DiscreteProperty> <BizDate>1600704000000</BizDate> <Threshold>0.2</Threshold> </ReferenceValue> <SampleValue> <Value>23</Value> |  |
|---|---|---|

DataWorks

```xml
            <Value>23</Value>
            <DiscreteProperty>type2</DiscreteProperty>
            <BizDate>1600704000000</BizDate>
        </SampleValue>
    </RuleChecks>
</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data": {"TotalCount":"200","PageSize":"10","PageNumber":"1","RuleChecks": [{"Op":">","TaskId":"16008552981681a0d6****","CheckerName":"fulx","DiscreteCheck":"false" EndTime":"1600704000000","ProjectName":"autotest","ExpectValue":"90","WarningThreshold":" 1","RuleId":"123421","BeginTime":"1600704000000","WhereCondition":"type!='type2'","CheckR ultStatus":"2","MatchExpression":"ds=$[yyyymmdd]","UpperValue":"22200","IsPrediction":"fa
```

`e","CheckResult":"2","TemplateName":"`字段唯一值个数期望值校

```json
验","FixedCheck":"false","TimeCost":"10","MethodName":"max","ResultString":"ResultString" DateType":"YMD","Property":"type","RuleName":"规则的名称。 ","TemplateId":"5","BizDate":"1600704000000","Comment":"校验规则的描述。","CriticalThresho ld":"0.6","ExternalId":"123112232","CheckerType":"0","Trend":"up","ExternalType":"CWF","C ckerId":"7","EntityId":"14534343","TableName":"dual","BlockType":"1","ActualExpression":" =20200925","Id":"2231123","LowerValue":"2344","ReferenceValue": [{"SingleCheckResult":"2","Value":"20","DiscreteProperty":"type1","BizDate":"160070400000 ,"Threshold":"0.2"}],"SampleValue": [{"Value":"23","DiscreteProperty":"type2","BizDate":"1600704000000"}]}]},"ErrorCode":"401 "ErrorMessage":"You have no permission.","Success":"false"}
```

#### ListQualityRules

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListQualityRules | 系统规定参数。取值： ListQualityRules。 |
| EntityId | Long | 是 | 1234 | 分区表达式的ID。您可以调用 GetQualityEntity获取分区表达式ID。 |
| PageNumber | Integer | 是 | 1 | 页码数。 |
| PageSize | Integer | 是 | 20 | 每页显示的条数，默认为10条，最大为 100条。 |

DataWorks

| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。您可以从数据源配置中获取名称。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 获取的规则列表。 |
| PageNumber | Integer | 1 | 页码数。 |
| PageSize | Integer | 20 | 每页显示的条数，默认为10条，最大为100条。 |
| Rules | Array of Rules |  | 校验规则的详情。 |
| BlockType | Integer | 0 | 校验规则的强弱。强弱表示规则的重要程度。取值如下： 1，表示强规则。 0，表示弱规则。 您可以根据实际需求设置重要的规则为强规则。 如果使用强规则并触发了红色告警，则会阻塞调度任务。 |
| CheckerId | Integer | 7 | 校验器ID。 |
| Comment | String | 校验表规则 | 规则的描述信息。 |
| CriticalThresho ld | String | 40 | 红色告警阈值。表示与样本预期的偏离程度。您可以根据业务需求自定义该阈值。使用强规则并触发红色阈值，会阻塞调度任务。 |
| EntityId | Integer | 1234 | 分区表达式的ID。 |
| ExpectValue | String | 1000 | 期望值。 |
| FixCheck | Boolean | true | 是否为强规则。 |
| HistoryCritical Threshold | String | history max:80%,history min:50% | 历史红色告警阈值。 |

DataWorks

| HistoryWarnin gThreshold | String | history max:40%,history min:10% | 历史橙色告警阈值。 |
|---|---|---|---|
| Id | Integer | 1234 | 规则的ID。 |
| MatchExpressi on | String | dt=$[yyyymmdd] | 分区表达式。 |
| MethodId | Integer | 21 | 采集样本数据方法的ID。 |
| MethodName | String | count/table count _ | 采集样本数据方法的名称。包括avg、count、 sum、min、max、count distinct、 _ user defined、table count、table size、 _ _ _ table dt load count、 _ _ _ table dt refuseload count、null value、 _ _ _ _ null value/table count、(table count- _ _ _ count distinct)/table count、table count- _ _ _ count distinct等。 _ |
| OnDuty | String | 1912**** | 配置校验规则的账号ID。 |
| ProjectName | String | autotest | 引擎或者数据源的名称。 |
| Property | String | id | 字段的名称。 |
| PropertyKey | String | table count _ | 用于数据质量前端规则联动，可以忽略。 |
| RuleCheckerR elationId | Integer | 132323 | 规则详情的内部关联ID。 |
| RuleType | Integer | 0 | 规则的类型： 0表示系统创建。 1表示用户创建。 2表示项目级规则。 |
| TableName | String | dual | 表的名称。 |
| TemplateId | Integer | 7 | 使用的校验模板的ID。 |
| TemplateNam e | String | sql任务表行数，1、 7、30天波动检测 | 使用的校验模板的名称。 |
| Trend | String | abs | 校验结果的趋势。 |

DataWorks

| WarningThres hold | String | 10 | 橙色告警阈值。表示与样本预期的偏离程度，您可以根据业务需求自定义该阈值。 |
|---|---|---|---|
| TotalCount | Long | 400 | 返回数据总量。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 38cbdef0-f6cf- 49**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&EntityId=1234 &PageNumber=1 &PageSize=20 &ProjectName=autotest &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>38cbdef0-f6cf-49****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>400</TotalCount>
    <PageSize>20</PageSize>
    <PageNumber>1</PageNumber>
    <Rules>
```

`<Comment>`校验表规则`</Comment>`

```xml
        <HistoryCriticalThreshold>history max:80%,history min:50%
</HistoryCriticalThreshold>
        <HistoryWarningThreshold>history max:40%,history min:10%
</HistoryWarningThreshold>
        <CriticalThreshold>40</CriticalThreshold>
        <RuleCheckerRelationId>132323</RuleCheckerRelationId>
        <ExpectValue>1000</ExpectValue>
        <ProjectName>autotest</ProjectName>
        <WarningThreshold>10</WarningThreshold>
        <Trend>abs</Trend>
        <OnDuty>1912****</OnDuty>
        <RuleType>0</RuleType>
        <CheckerId>7</CheckerId>
        <MatchExpression>dt=$[yyyymmdd]</MatchExpression>
        <EntityId>1234</EntityId>
        <TableName>dual</TableName>
        <MethodId>21</MethodId>
        <FixCheck>true</FixCheck>
        <BlockType>0</BlockType>
```

`<TemplateName>sql`任务表行数，1、7、`30`天波动检测`</TemplateName>`

```xml
        <MethodName>count/table_count</MethodName>
        <Id>1234</Id>
        <Property>id</Property>
        <PropertyKey>table_count</PropertyKey>
        <TemplateId>7</TemplateId>
    </Rules>
</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "38cbdef0-f6cf-49****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 400,
        "PageSize": 20,
        "PageNumber": 1,
        "Rules": {
```

`"Comment": "`校验表规则`",`

```json
            "HistoryCriticalThreshold": "history max:80%,history min:50%",
            "HistoryWarningThreshold": "history max:40%,history min:10%",
            "CriticalThreshold": 40,
            "RuleCheckerRelationId": 132323,
            "ExpectValue": 1000,
            "ProjectName": "autotest",
            "WarningThreshold": 10,
            "Trend": "abs",
            "OnDuty": "1912****",
            "RuleType": 0,
            "CheckerId": 7,
            "MatchExpression": "dt=$[yyyymmdd]",
            "EntityId": 1234,
            "TableName": "dual",
            "MethodId": 21,
            "FixCheck": true,
            "BlockType": 0,
```

`"TemplateName": "sql`任务表行数，1、7、`30`天波动检测`",`

```json
            "MethodName": "count/table_count",
            "Id": 1234,
            "Property": "id",
            "PropertyKey": "table_count",
            "TemplateId": 7
        }
    },
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

#### UpdateQualityFollower

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateQualityFo llower | 系统规定参数。取值： UpdateQualityFollower。 |

DataWorks

| AlarmMode | Integer | 是 | 2 | 订阅关系：1表示邮件、2表示邮件和短信、4表示钉钉群机器人、5表示钉钉群机器人@all。 |
|---|---|---|---|---|
| Follower | String | 是 | 1912232**** | 订阅人。 |
| FollowerId | Long | 是 | 1234 | 订阅关系的ID。 |
| ProjectName | String | 是 | autotest | 引擎或者数据源的名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 是否更新成功。 |
| ErrorCode | String | 401 | 错误码。 |
| ErrorMessage | String | You have no permission | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| RequestId | String | 576b9457-2cf5- 4**** | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateQualityFollower &AlarmMode=2 &Follower=1912232**** &FollowerId=1234 &ProjectName=autotest &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>576b9457-2cf5-4****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>401</ErrorCode> <ErrorMessage>You have no permission</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "576b9457-2cf5-4****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 401,
    "ErrorMessage": "You have no permission",
    "Success": true
}
```

#### UpdateQualityRule

**注意**

如果校验规则是固定值，则需要传入Operator和ExpectValue。 如果校验规则是动值校验（包括自助规则和模板规则），则需要Trend为up、down、abs其中的一个。 红色阈值和橙色阈值不能同时为空。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | UpdateQualityRule | 系统规定参数。取值： UpdateQualityRule。 |
| BlockType | Integ er | Body | 否 | 0 | 校验规则的强弱。强弱表示规则的重要程度。取值如下： 1：表示强规则。 0：表示弱规则。您可以根据实际需求设置重要的规则为强规则。如果使用强规则并触发了红色告警，则会阻塞调度任务。 |
| EntityId | Long | Body | 否 | 123 | 分区表达式的ID。您可以调用ListQualityRules接口获分区表达式ID。 |

| 开发指南·Open | API参考 |  |  |  | DataWork |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| Comment | Strin g | Body | 否 | 校验表行数 | 校验规则的描述信息。 |
|---|---|---|---|---|---|
| Checker | Integ er | Body | 否 | 9 | 校验器ID。您可以调用 ListQualityRules接口获取校验器ID。 |
| ExpectVal ue | Strin g | Body | 否 | 300 | 校验结果的期望值。 |
| Id | Long | Body | 是 | 1234 | 校验规则的ID。您可以调用 ListQualityRules接口获取规则ID。 |
| Trend | Strin g | Body | 否 | up | 校验结果的趋势。取值如下： up：表示上升趋势。 down：表示下降趋势。 abs：表示绝对值。 |
| MethodNa me | Strin g | Body | 否 | table count _ | 采集样本数据方法的名称。 包括avg、count、sum、 min、max、 count distinct、 _ user defined、 _ table count、 _ table size、 _ table dt load count、 _ _ _ table dt refuseload cou _ _ _ nt、null value、 _ null value/table count、 _ _ (table count- _ count distinct)/table co _ _ unt、table count- _ count distinct等。 _ |
| Operator | Strin g | Body | 否 | > | 比较符。包括>、>=、=、 ≠、<和<=等。当 Checker=9时，Operator 为必选参数。 |
| ProjectNa me | Strin g | Body | 是 | autotest | 引擎或者数据源的名称。您可以登录DataWorks控制台，进入工作空间管理页面获取名称。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Property | Strin g | Body | 否 | id | 字段的名称。 |
| PropertyT ype | Strin g | Body | 否 | bigint | 字段的类型。 |
| RuleType | Integ er | Body | 否 | 0 | 规则的类型： 0：表示系统创建。 1：表示用户创建。 2：表示项目级规则。 |
| WhereCon dition | Strin g | Body | 否 | dt=$[yyyymmdd] | 校验任务使用的过滤条件或自定义SQL语句。 |
| CriticalThr eshold | Strin g | Body | 否 | 10 | 红色告警阈值。表示与样本预期的偏离程度。您可以根据业务需求自定义该阈值。 使用强规则并触发红色阈值，会阻塞调度任务。 |
| WarningT hreshold | Strin g | Body | 否 | 5 | 橙色告警阈值。表示与样本预期的偏离程度，您可以根据业务需求自定义该阈值。 |
| TemplateI d | Integ er | Body | 否 | 7 | 使用的校验模板的ID。您可以调用ListQualityRules接口获取校验模板的ID。 |
| RegionId | Strin g | Host | 否 | default | 区域ID，为固定值 default。 |
| RuleName | Strin g | Body | 否 | 校验表行数规则 | 校验规则的名称。 |
| PredictTyp e | Integ er | Body | 否 | 0 | 校验规则类型的标识。取值如下： 0：表示校验规则为统计分析规则。 2：表示校验规则为动态阈值规则。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OpenSwit ch | Boole an | Body | 否 | true | 规则的启用或停用状态，用于控制质量规则是否在生产环境中运行。 true：在数据质量规则关联产出表数据的调度任务执行时，便会触发质量规则校验。 false：在数据质量规则关联产出表数据的调度任务执行时，不会触发质量规则校验。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP返回码。 |
| Data | Boolean | true | 校验规则是否更新成功。 |
| ErrorMessage | String | You have no permission. | 错误信息。 |
| RequestId | String | 576b9457-2cf5- 4**** | 请求ID。用于出现错误后排查问题。 |
| ErrorCode | String | 0 | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&Id=1234 &ProjectName=autotest
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式 DataWorks

```json
{
    "RequestId": "576b9457-2cf5-4****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 0,
    "ErrorMessage": "You have no permission.",
    "Success": true
}
```

`XML` 格式

```xml
<RequestId>576b9457-2cf5-4****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>You have no permission.</ErrorMessage> <Success>true</Success>
```

### 数据服务

#### AbolishDataServiceApi

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AbolishDataServ iceApi | 系统规定参数。取值： AbolishDataServiceApi。 |
| ApiId | Long | 是 | 10000 | 数据服务API的ID。 |
| ProjectId | Long | 是 | 10001 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10002 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 数据服务API是否下线成功。 |

DataWorks

| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AbolishDataServiceApi &ApiId=10000 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### CreateDataServiceApi

**请求头**

DataWorks 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| ProjectId | Long | Body | 是 | 10000 | 工作空间的ID。 |
| ApiName | Strin g | Body | 是 | Test API name | API 的名称，支持汉字、英文、数字和下划线（ ）， _ 且只能以英文和汉字开头，4~50 个字符。 |
| GroupId | Strin g | Body | 是 | Business process ID | 业务流程的 ID。 |
| ApiMode | Integ er | Body | 是 | 0 | API 的类型。取值范围： 0：向导API 1：脚本API 2：注册API |
| RequestM ethod | Integ er | Body | 是 | 0 | API 的请求方式。取值范围： 0：GET 1：POST 2：PUT 3：DELETE 向导和脚本 API 支持 GET 和 POST。注册 API 支持 GET、POST、PUT 和 DELETE。 |
| Response ContentTy pe | Integ er | Body | 是 | 0 | API 的返回数据类型。取值范围： 0：JSON 1：XML 向导和脚本 API 支持 JSON。注册 API 支持 JSON 和 XML。 |
| Timeout | Integ er | Body | 是 | 10000 | 超时时间，单位为毫秒 （ms），取值范围为(0, 30000]。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| VisibleRan ge | Integ er | Body | 是 | 0 | 可见范围。取值范围： 0：工作空间 1：私有 |
| Protocols | Strin g | Body | 是 | 0,1 | API 的协议。支持多个值， 多个值之间使用英文逗号 （,）分隔。取值范围： 0：HTTP 1：HTTPS |
| WizardDet ails | Strin g | Body | 否 | {"isPagedResponse":tru e,"wizardConnection": {"connectionId":122786, "tableName":"person"}," wizardRequestParamete rs": [{"columnName":"id","d efaultValue":"","example Value":"1","isRequiredPa rameter":true,"paramete rDataType":2,"paramete rDescription":"","parame terName":"id","paramet erOperator":0,"paramet erPosition":0}],"wizardR esponseParameters": [{"columnName":"id","e xampleValue":"11","par ameterDataType":2,"par ameterDescription":"","p arameterName":"id"}]} | 向导 API 的详情，请参见 GetDataServiceApi 接口 wizardDetails 字段的 JSON String。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ScriptDeta ils | Strin g | Body | 否 | {"isPagedResponse":fals e,"script":"select id as id1, name as name1 from person where id=${inputid}","scriptCo nnection": {"connectionId":122786, "tableName":"person"}," scriptRequestParameter s": [{"defaultValue":"","exa mpleValue":"","isRequire dParameter":true,"para meterDataType":0,"para meterDescription":"","pa rameterName":"inputid", "parameterOperator":0," parameterPosition":1}]," scriptResponseParamete rs": [{"exampleValue":"","pa rameterDataType":0,"pa rameterDescription":""," parameterName":"id1"}, {"exampleValue":"","par ameterDataType":0,"par ameterDescription":"","p arameterName":"name1 "}]} | 脚本 API 的详情，请参见 GetDataServiceApi 接口 scriptDetails 字段的 JSON String。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Registrati onDetails | Strin g | Body | 否 | {"failedResultSample":"f ail","registrationErrorCo des": [{"errorCode":"e1","erro rMessage":"msg1","error Solution":"sol1"}, {"errorCode":"e2","error Message":"msg2","error Solution":"sol2"}],"regist rationRequestParameter s": [{"columnName":"","def aultValue":"","exampleV alue":"","isRequiredPara meter":true,"parameter DataType":0,"parameter Description":"","paramet erName":"id","paramete rOperator":0,"parameter Position":1}, {"columnName":"","defa ultValue":"xx","example Value":"","isRequiredPar ameter":true,"parameter DataType":0,"parameter Description":"","paramet erName":"cc","paramete rOperator":2,"parameter Position":2}],"serviceCo ntentType":1,"serviceHo st":"http://www.baidu.co m","servicePath":"/[uid]" ,"serviceRequestBodyDe scription":"body","succe ssfulResultSample":"suc cess"} | 注册 API 的详情，请参见 GetDataServiceApi 接口 registrationDetails 字段的 JSON String。 |
| ApiPath | Strin g | Body | 是 | /test/1 | API 的路径，支持英文、数字、下划线（ ）和连字符 _ （-），且只能以斜线（/） 开头，不能超过 200 个字符。 |
| ApiDescri ption | Strin g | Body | 是 | Test API description | API 的描述信息。 |
| FolderId | Long | Body | 否 | 0 | 创建 API 的目标文件夹 ID，业务流程下根文件夹 ID 等于 0，用户自建文件夹 ID 大于 0。 |
| SqlMode | Long | Body | 否 | 0 | SQL模式。向导模式时，该值不生效。取值范围： 0：基础SQL 1：高级SQL |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Resource GroupId | Long | Body | 否 | 3242432423 | 独享资源组 ID。 |
| RequestC ontentTyp e | Integ er | Body | 否 | 0 | 请求数据类型。取值范围： 0：xml 1：json 2：form |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP 状态码。 |
| Data | Long | 1000001 | 创建的 API ID。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求 ID，一次请求的唯一标识。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateDataServiceApi &RegionId= &ProjectId=10000 &ApiName=Test API name &GroupId=Business process ID &ApiMode=0 &RequestMethod=0 &ResponseContentType=0 &Timeout=10000 &VisibleRange=0 &Protocols=0,1 &ApiPath=/test/1 &ApiDescription=Test API description
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":1000001,
 "ErrorCode":"null",
 "ErrorMessage":"null",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>1000001</Data> <ErrorCode>null</ErrorCode> <ErrorMessage>null</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |

#### CreateDataServiceApiAuthority

调用CreateDataServiceApiAuthority新增数据服务API授权。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | CreateDataServi ceApiAuthority | 系统规定参数。取值： CreateDataServiceApiAuthority。 |
|---|---|---|---|---|
| ApiId | Long | 是 | 10001 | API的ID。 |
| AuthorizedProjec tId | Long | 是 | 10002 | 被授权的工作空间ID。 |
| EndTime | Long | 是 | 1600531564 | 授权有限期结束时间，Unix时间戳，单位为s。例如1600531564，代表北京时间 2020-09-20 00:06:04。 |
| ProjectId | Long | 是 | 10003 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 1004 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD-EF**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 授权是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateDataServiceApiAuthority &ApiId=10001 &AuthorizedProjectId=10002 &EndTime=1600531564 &ProjectId=10003 &RegionId=default &TenantId=1004
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EF****</RequestId> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{"RequestId":"0000-ABCD-EF****","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateDataServiceFolder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDataServi ceFolder | 系统规定参数。取值： CreateDataServiceFolder。 |
| FolderName | String | 是 | 测试文件夹 | 文件夹的名称。 |
| GroupId | String | 是 | 1000abcd | 文件夹的目标业务流程ID。 |
| ParentId | Long | 是 | 0 | 文件夹的目标父文件夹ID。业务流程根文件夹ID等于0，用户创建的文件夹ID大于 0。 |
| ProjectId | Long | 是 | 10001 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| TenantId | Long | 是 | 10002 | 租户ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FolderId | Long | 123 | 创建的文件夹ID。 |
| RequestId | String | 0000-ABCD-E**** | 请求ID，一次请求的唯一标识。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateDataServiceFolder
```

`&FolderName=`测试文件夹

```
&GroupId=1000abcd &ParentId=0 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-E****</RequestId> <FolderId>123</FolderId>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-E****","FolderId":"123"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

DataWorks

| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### CreateDataServiceGroup

在多Region场景下，此API不支持传入单元Region的API网关分组ID，即**ApiGatewayGroupId** 字段， 只支持中心Region。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| TenantId | Long | Body | 是 | 10002 | 租户ID。 |
| ProjectId | Long | Body | 是 | 10001 | 工作空间的ID。 |
| ApiGatew ayGroupId | Strin g | Body | 是 | 1000abcd | 业务流程绑定的API网关分组ID，您可以进入API网关控制台分组详情页面进行查看。 |
| GroupNa me | Strin g | Body | 是 | 业务流程名称 | 业务流程的名称。 |
| Descriptio n | Strin g | Body | 否 | 测试业务流程 | 业务流程的描述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| GroupId | String | ds 12345 _ | 创建的业务流程ID。 |
| RequestId | String | 0000-ABCD-EF**** | 请求ID，一次请求的唯一标识。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=CreateDataServiceGroup &RegionId=default &TenantId=10002 &ProjectId=10001 &ApiGatewayGroupId=1000abcd
```

`&GroupName=`业务流程名称 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EF****",
 "GroupId":"ds_12345"
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EF****</RequestId> <GroupId>ds_12345</GroupId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |

#### DeleteDataServiceApi

**请求参数**

DataWorks

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDataServi ceApi | 系统规定参数。取值： DeleteDataServiceApi。 |
| ApiId | Long | 是 | 10000 | 数据服务API的ID。 |
| ProjectId | Long | 是 | 10001 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10002 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 删除是否成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDataServiceApi &ApiId=10000 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### DeleteDataServiceApiAuthority

调用DeleteDataServiceApiAuthority取消数据服务API授权。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | DeleteDataServi ceApiAuthority | 系统规定参数。取值： DeleteDataServiceApiAuthority。 |
|---|---|---|---|---|
| ApiId | Long | 是 | 10001 | API的ID。 |
| AuthorizedProjec tId | Long | 是 | 10002 | 被取消授权的工作空间ID。 |
| ProjectId | Long | 是 | 10003 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10004 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD-EF**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 取消授权是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDataServiceApiAuthority &ApiId=10001 &AuthorizedProjectId=10002 &ProjectId=10003 &RegionId=default &TenantId=10004
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EF****</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EF****","Success":"true"}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetDataServiceApi

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值 default。 |
| ProjectId | Long | Body | 是 | 10001 | 工作空间的 ID。 |
| ApiId | Long | Body | 是 | 10000 | 数据服务 API 的 ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP 状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求 ID，一次请求的唯一标识。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorMessage | String | The specified parameters are invalid. | 错误信息。 |
| Success | Boolean | true | 调用是否成功。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| Data | Struct | / | 返回数据。 |
| -Protocols | List | 0 | API 协议，取值范围： 0：HTTP 1：HTTPS |
| -Timeout | Integer | 10000 | 超时时间，单位为毫秒（ms）。 |
| -Status | Integer | 0 | API 的状态，取值范围： 0：未发布 1：已发布 |
| -ApiId | Long | 10000 | 数据服务 API 的 ID。 |
| -ApiMode | Integer | 0 | API 的类型，取值范围： 0：向导 API 1：脚本 API 2：注册 API |
| -ProjectId | Long | 10001 | 工作空间的 ID。 |
| - ResponseCont entType | Integer | 0 | API 的返回数据类型，取值范围： 0：JSON 1：XML 向导和脚本 API 支持 JSON，注册 API 支持 JSON 和 XML。 |
| -CreatorId | String | 1234567 | 创建人的账号 ID。 |
| -VisibleRange | Integer | 0 | 可见范围，取值范围： 0：工作空间 1：私有 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ModifiedTime | String | 2020-06- 23T00:21:01+0800 | 最新修改时间。 |
| -OperatorId | String | 2345678 | 最新编辑人的账号 ID。 |
| -GroupId | String | ab123**** | 分组 ID。 |
| -Description | String | test | 描述信息。 |
| -FolderId | Long | 0 | 文件夹 ID。 |
| - RequestMetho d | Integer | 0 | API 的请求方式，取值范围： 0：GET 1：POST 2：PUT 3：DELETE 向导和脚本 API 支持 GET 和 POST。注册 API 支持 GET、POST、PUT 和 DELETE。 |
| -CreatedTime | String | 2020-06- 23T00:21:01+0800 | 创建时间。 |
| -ApiName | String | testapi | API 的名称。 |
| -TenantId | Long | 10002 | 租户 ID。 |
| -ApiPath | String | /test/1 | API 的路径。 |
| - RegistrationDe tails | Struct | / | 注册 API 的详情，只有注册 API 返回。 |
| -- RegistrationErr orCodes | Array | / | 注册API的错误码列表。 |
| --- ErrorMessage | String | fail to call | 错误信息。 |
| ---ErrorCode | String | 1001 | 错误码。 |
| --- ErrorSolution | String | retry | 错误解决方案。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- RegistrationRe questParamet ers | Array | / | 注册API的请求参数列表。 |
| --- ColumnName | String | column1 | 绑定的表字段名称。 |
| --- ParameterNa me | String | name1 | 参数的名称。 |
| --- ParameterPosi tion | Integer | 0 | 参数的位置，取值范围： 0：Path 1：Query 2：Head 3：Body 向导和脚本API仅支持Query。注册API中的 GET、DELETE方法支持Query、Head，PUT、 POST方法支持Query、Head和Body。 |
| --- ParameterDes cription | String | description1 | 描述信息。 |
| --- DefaultValue | String | default1 | 默认值。 |
| --- ParameterOpe rator | Integer | 0 | 运算符，取值范围： 0：Equal 1：Like 2：Const 3：In 向导模式API支持Equal、Like和In，脚本模式 API支持Equal，注册API支持Equal和Const。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- ParameterDat aType | Integer | 0 | 数据类型，取值范围： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean 6：StringList 7：IntList 8：LongList 9：FloatList 10：DoubleList 11：BooleanList |
| --- ExampleValue | String | example1 | 示例值。 |
| --- IsRequiredPar ameter | Boolean | true | 是否必填。 |
| --ServiceHost | String | http://example.aliy undoc.com | 后端服务地址。 |
| -- ServiceConten tType | Integer | 0 | API 返回数据类型，取值范围： 0：JSON 1：XML 向导和脚本 API 只支持 JSON；注册 API 支持 JSON 和 XML。 |
| --ServicePath | String | /index | 后端服务路径。 |
| -- SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |
| -- FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| -- ServiceReques tBodyDescripti on | String | {"abc":1} | 后端请求body内容的描述。 |
| -ScriptDetails | Struct | / | 脚本API的详情，只有脚本API返回。 |
| -- ScriptRequest Parameters | Array | / | 脚本API的请求参数列表。 |

| 开发指南·OpenAPI参 | 考 |  | DataWork |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --- ColumnName | String | column1 | 绑定的表字段名称。 |
| --- ParameterNa me | String | param1 | 参数的名称。 |
| --- ParameterPosi tion | Integer | 0 | 参数的位置，取值范围： 0：Path 1：Query 2：Head 3：Body 向导和脚本API仅支持Query。注册API中的 GET、DELETE方法支持Query、Head，PUT、 POST方法支持Query、Head和Body。 |
| --- ParameterDes cription | String | description1 | 描述信息。 |
| --- DefaultValue | String | default1 | 默认值。 |
| --- ParameterOpe rator | Integer | 0 | 运算符，取值范围： 0：Equal 1：Like 2：Const 3：In 向导模式API支持Equal、Like和In，脚本模式 API支持Equal，注册API支持Equal和Const。 |
| --- ParameterDat aType | Integer | 0 | 数据类型，取值范围： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean 6：StringList 7：IntList 8：LongList 9：FloatList 10：DoubleList 11：BooleanList |
| --- ExampleValue | String | example1 | 示例值。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- IsRequiredPar ameter | Boolean | true | 是否必填。 |
| -- ScriptRespons eParameters | Array | / | 脚本API的返回参数列表。 |
| --- ParameterDes cription | String | description2 | 描述信息。 |
| --- ColumnName | String | column2 | 绑定的表字段名称。 |
| --- ParameterNa me | String | param2 | 参数的名称。 |
| --- ParameterDat aType | Integer | 0 | 数据类型，取值范围： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean 6：StringList 7：IntList 8：LongList 9：FloatList 10：DoubleList 11：BooleanList |
| --- ExampleValue | String | example2 | 示例值。 |
| --Script | String | select a from t | SQL脚本。 |
| -- IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| -- ScriptConnecti on | Struct | / | 脚本API的数据源信息。 |
| ---TableName | String | t | 数据源表的名称。 |
| --- ConnectionId | Long | 123 | 数据源ID。 |

| 开发指南·OpenAPI参 | 考 |  | DataWork |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -WizardDetails | Struct | / | 向导API详情，只有向导API返回。 |
| -- WizardReques tParameters | Array | / | 向导API的请求参数列表。 |
| --- ColumnName | String | column1 | 绑定的表字段名称。 |
| --- ParameterNa me | String | param1 | 参数的名称。 |
| --- ParameterPosi tion | Integer | 0 | 参数的位置，取值范围： 0：Path 1：Query 2：Head 3：Body 向导和脚本API仅支持Query。注册API中的 GET、DELETE方法支持Query、Head，PUT、 POST方法支持Query、Head和Body。 |
| --- ParameterDes cription | String | description1 | 描述信息。 |
| --- DefaultValue | String | default1 | 默认值。 |
| --- ParameterOpe rator | Integer | 0 | 运算符，取值范围： 0：Equal 1：Like 2：Const 3：In 向导模式API支持Equal、Like和In，脚本模式 API支持Equal，注册API支持Equal和Const。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- ParameterDat aType | Integer | 0 | 数据类型，取值范围： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean 6：StringList 7：IntList 8：LongList 9：FloatList 10：DoubleList 11：BooleanList |
| --- ExampleValue | String | example1 | 示例值。 |
| --- IsRequiredPar ameter | Boolean | true | 是否必填。 |
| -- WizardRespon seParameters | Array | / | 向导模式的返回参数列表。 |
| --- ParameterDes cription | String | description2 | 描述信息。 |
| --- ColumnName | String | column2 | 绑定的表字段名称。 |
| --- ParameterNa me | String | param2 | 参数的名称。 |
| --- ParameterDat aType | Integer | 0 | 数据类型，取值范围： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean 6：StringList 7：IntList 8：LongList 9：FloatList 10：DoubleList 11：BooleanList |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- ExampleValue | String | example2 | 示例值。 |
| -- IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| -- WizardConnec tion | Struct | / | 向导API的数据源信息。 |
| ---TableName | String | t | 数据源的表名称。 |
| --- ConnectionId | Long | 123 | 数据源ID。 |

在返回数据Data中，新增返回参数SqlMode，展示脚本模式时的SQL模式。

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SqlMode | Long | 0 | SQL模式。向导模式时， 该值不生效。取值范围： - 0：基础SQL - 1：高级SQL |

**示例**

请求示例

```
&RegionId=default &ProjectId=10001 &ApiId=10000
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":200,
 "Data":{
  "Status":0,
  "ScriptDetails":{
   "Script":"select a from t",
   "IsPagedResponse":true,
   "ScriptRequestParameters":[
    {
     "ColumnName":"column1",
     "DefaultValue":"default1",
     "ExampleValue":"example1",
     "ParameterDataType":0,
     "ParameterPosition":0,
```

DataWorks ,

```json
     "ParameterName":"param1",
     "ParameterOperator":0,
     "ParameterDescription":"description1",
     "IsRequiredParameter":true
    }
```

`],`

```json
   "ScriptResponseParameters":[
    {
     "ColumnName":"column2",
     "ExampleValue":"example2",
     "ParameterDataType":0,
     "ParameterName":"param2",
     "ParameterDescription":"description2"
    }
```

`],`

```json
   "ScriptConnection":{
    "TableName":"t",
    "ConnectionId":123
   }
  },
  "Protocols":0,
  "VisibleRange":0,
  "Description":"test ",
  "CreatedTime":"2020-06-23T00:21:01+0800",
  "RegistrationDetails":{
   "ServiceRequestBodyDescription":"{\"abc\":1}",
   "RegistrationRequestParameters":[
    {
     "ColumnName":"column1",
     "DefaultValue":"default1",
     "ExampleValue":"example1",
     "ParameterDataType":0,
     "ParameterPosition":0,
     "ParameterName":"name1",
     "ParameterOperator":0,
     "ParameterDescription":"description1",
     "IsRequiredParameter":true
    }
```

`],`

```json
   "ServiceContentType":0,
   "SuccessfulResultSample":"{\"success\": true}",
   "ServicePath":"/index",
   "FailedResultSample":"{\"success\": false}",
   "ServiceHost":"http://example.aliyundoc.com",
   "RegistrationErrorCodes":[
    {
     "ErrorCode":"1001",
     "ErrorMessage":"fail to call",
     "ErrorSolution":"retry"
    }
```

]

```json
  },
  "ApiName":"testapi",
  "Timeout":10000,
```

DataWorks

```json
  "CreatorId":"1234567",
  "RequestMethod":0,
  "ProjectId":10001,
  "ResponseContentType":0,
  "OperatorId":"2345678",
  "FolderId":0,
  "GroupId":"ab123****",
  "TenantId":10002,
  "ModifiedTime":"2020-06-23T00:21:01+0800",
  "WizardDetails":{
   "IsPagedResponse":true,
   "WizardConnection":{
    "TableName":"t",
    "ConnectionId":123
   },
   "WizardResponseParameters":[
    {
     "ColumnName":"column2",
     "ExampleValue":"example2",
     "ParameterDataType":0,
     "ParameterName":"param2",
     "ParameterDescription":"description2"
    }
```

`],`

```json
   "WizardRequestParameters":[
    {
     "ColumnName":"column1",
     "DefaultValue":"default1",
     "ExampleValue":"example1",
     "ParameterDataType":0,
     "ParameterPosition":0,
     "ParameterName":"param1",
     "ParameterOperator":0,
     "ParameterDescription":"description1",
     "IsRequiredParameter":true
    }
```

]

```json
  },
  "ApiId":10000,
  "ApiMode":0,
  "ApiPath":"/test/1"
 },
 "ErrorCode":"1031203110005",
 "ErrorMessage":"The specified parameters are invalid.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
  <Status>0</Status>
<ScriptDetails>
```

DataWorks

```xml
  <ScriptDetails>
    <Script>select a from t</Script>
    <IsPagedResponse>true</IsPagedResponse>
    <ScriptRequestParameters>
      <ColumnName>column1</ColumnName>
      <DefaultValue>default1</DefaultValue>
      <ExampleValue>example1</ExampleValue>
      <ParameterDataType>0</ParameterDataType>
      <ParameterPosition>0</ParameterPosition>
      <ParameterName>param1</ParameterName>
      <ParameterOperator>0</ParameterOperator>
      <ParameterDescription>description1</ParameterDescription>
      <IsRequiredParameter>true</IsRequiredParameter>
    </ScriptRequestParameters>
    <ScriptResponseParameters>
      <ColumnName>column2</ColumnName>
      <ExampleValue>example2</ExampleValue>
      <ParameterDataType>0</ParameterDataType>
      <ParameterName>param2</ParameterName>
      <ParameterDescription>description2</ParameterDescription>
    </ScriptResponseParameters>
    <ScriptConnection>
      <TableName>t</TableName>
      <ConnectionId>123</ConnectionId>
    </ScriptConnection>
  </ScriptDetails>
  <Protocols>0</Protocols>
  <VisibleRange>0</VisibleRange>
  <Description>test </Description>
  <CreatedTime>2020-06-23T00:21:01+0800</CreatedTime>
  <RegistrationDetails>
    <ServiceRequestBodyDescription>{&quot;abc&quot;:1}</ServiceRequestBodyDescription>
    <RegistrationRequestParameters>
      <ColumnName>column1</ColumnName>
      <DefaultValue>default1</DefaultValue>
      <ExampleValue>example1</ExampleValue>
      <ParameterDataType>0</ParameterDataType>
      <ParameterPosition>0</ParameterPosition>
      <ParameterName>name1</ParameterName>
      <ParameterOperator>0</ParameterOperator>
      <ParameterDescription>description1</ParameterDescription>
      <IsRequiredParameter>true</IsRequiredParameter>
    </RegistrationRequestParameters>
    <ServiceContentType>0</ServiceContentType>
    <SuccessfulResultSample>{&quot;success&quot;: true}</SuccessfulResultSample>
    <ServicePath>/index</ServicePath>
    <FailedResultSample>{&quot;success&quot;: false}</FailedResultSample>
    <ServiceHost>http://example.aliyundoc.com</ServiceHost>
    <RegistrationErrorCodes>
      <ErrorCode>1001</ErrorCode>
      <ErrorMessage>fail to call</ErrorMessage>
      <ErrorSolution>retry</ErrorSolution>
    </RegistrationErrorCodes>
  </RegistrationDetails>
  <ApiName>testapi</ApiName>
```

DataWorks

```xml
  <Timeout>10000</Timeout>
  <CreatorId>1234567</CreatorId>
  <RequestMethod>0</RequestMethod>
  <ProjectId>10001</ProjectId>
  <ResponseContentType>0</ResponseContentType>
  <OperatorId>2345678</OperatorId>
  <FolderId>0</FolderId>
  <GroupId>ab123****</GroupId>
  <TenantId>10002</TenantId>
  <ModifiedTime>2020-06-23T00:21:01+0800</ModifiedTime>
  <WizardDetails>
    <IsPagedResponse>true</IsPagedResponse>
    <WizardConnection>
      <TableName>t</TableName>
      <ConnectionId>123</ConnectionId>
    </WizardConnection>
    <WizardResponseParameters>
      <ColumnName>column2</ColumnName>
      <ExampleValue>example2</ExampleValue>
      <ParameterDataType>0</ParameterDataType>
      <ParameterName>param2</ParameterName>
      <ParameterDescription>description2</ParameterDescription>
    </WizardResponseParameters>
    <WizardRequestParameters>
      <ColumnName>column1</ColumnName>
      <DefaultValue>default1</DefaultValue>
      <ExampleValue>example1</ExampleValue>
      <ParameterDataType>0</ParameterDataType>
      <ParameterPosition>0</ParameterPosition>
      <ParameterName>param1</ParameterName>
      <ParameterOperator>0</ParameterOperator>
      <ParameterDescription>description1</ParameterDescription>
      <IsRequiredParameter>true</IsRequiredParameter>
    </WizardRequestParameters>
  </WizardDetails>
  <ApiId>10000</ApiId>
  <ApiMode>0</ApiMode>
  <ApiPath>/test/1</ApiPath>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040001 | Throttling.Api | The request for this resource has exceeded your available limit. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 500 | 9990010002 | InternalError.System | An internal system error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |

#### GetDataServiceApplication

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataService Application | 系统规定参数。取值： GetDataServiceApplication。 |
| ApplicationId | Long | 是 | 10000 | App的ID，可在API网关控制台上查看应用信息。 |
| ProjectId | Long | 是 | 10001 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10002 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | App详情。 |
| ApplicationCod e | String | CODE123 | API调用认证方式一，简单身份认证中的 AppCode。 |
| ApplicationId | Long | 10000 | App的ID。 |

DataWorks

| ApplicationKey | String | KEY123 | API调用认证方式二，加密签名身份认证中的 AppKey。 |
|---|---|---|---|
| ApplicationNa me | String | 测试应用 | 应用名称。 |
| ApplicationSec ret | String | SECRET123 | API调用认证方式二，加密签名身份认证中的 AppSecret。 |
| ProjectId | Long | 10001 | 关联工作空间的ID。 |
| ErrorCode | String | 0 | 错误码。 |
| ErrorMessage | String | 正常 | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataServiceApplication &ApplicationId=10000 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <ApplicationKey>KEY123</ApplicationKey>
    <ApplicationSecret>SECRET123</ApplicationSecret>
    <ApplicationName>测试应用</ApplicationName>
    <ProjectId>10001</ProjectId>
    <ApplicationId>10000</ApplicationId>
    <ApplicationCode>CODE123</ApplicationCode>
</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>正常</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "ApplicationKey": "KEY123",
        "ApplicationSecret": "SECRET123",
```

`"ApplicationName": "`测试应用`",`

```json
        "ProjectId": 10001,
        "ApplicationId": 10000,
        "ApplicationCode": "CODE123"
    },
    "ErrorCode": 0,
    "ErrorMessage": "正常",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### GetDataServiceFolder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataServiceF older | 系统规定参数。取值： GetDataServiceFolder。 |
| FolderId | Long | 是 | 10001 | 文件夹的ID。 |
| ProjectId | Long | 是 | 10002 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10003 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Folder | Struct |  | 文件夹详情。 |
| CreatedTime | String | 2020-09- 24T18:37:51+0800 | 文件夹创建时间。 |
| FolderId | Long | 11 | 文件夹ID。 |
| FolderName | String | test | 文件夹名称。 |
| GroupId | String | ds 11111 _ | 文件夹所属业务流程的ID。 |
| ModifiedTime | String | 2020-09- 25T18:37:51+0800 | 文件夹修改时间。 |
| ParentId | Long | 0 | 父文件夹ID。业务流程下根文件夹ID等于0，用户创建文件夹ID大于0。 |

DataWorks

| ProjectId | Long | 1001 | DataWorks工作空间ID。 |
|---|---|---|---|
| TenantId | Long | 10002 | 租户ID。 |
| RequestId | String | 0000-ABCD- EFG****** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataServiceFolder &FolderId=10001 &ProjectId=10002 &RegionId=default &TenantId=10003
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG******</RequestId> <Folder>
    <ParentId>0</ParentId>
    <TenantId>10002</TenantId>
    <CreatedTime>2020-09-24T18:37:51+0800</CreatedTime>
    <ModifiedTime>2020-09-25T18:37:51+0800</ModifiedTime>
    <ProjectId>1001</ProjectId>
    <FolderId>11</FolderId>
    <FolderName>test</FolderName>
    <GroupId>ds_11111</GroupId>
</Folder>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG******","Folder": {"ParentId":"0","TenantId":"10002","CreatedTime":"2020-09- 24T18:37:51+0800","ModifiedTime":"2020-09- 25T18:37:51+0800","ProjectId":"1001","FolderId":"11","FolderName":"test","GroupId":"ds_11 1"}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
|---|---|---|---|
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetDataServiceGroup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataService Group | 系统规定参数。取值： GetDataServiceGroup。 |
| GroupId | String | 是 | ds 123 _ | 业务流程的ID。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10002 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Group | Struct |  | 业务流程详情。 |
| ApiGatewayGr oupId | String | 100abc | 业务流程绑定的API网关分组ID。 |
| CreatedTime | String | 2020-09- 24T18:37:51+0800 | 业务流程的创建时间。 |
| CreatorId | String | 123456789 | 创建人UID，部分历史业务流程创建人的UID可能为空。 |

DataWorks

| Description | String | 业务流程的描述 | 业务流程的描述。 |
|---|---|---|---|
| GroupId | String | ds 123 _ | 业务流程ID。 |
| GroupName | String | 业务流程名称 | 业务流程名称。 |
| ModifiedTime | String | 2020-09- 24T18:37:51+0800 | 修改时间。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| TenantId | Long | 10002 | 租户ID。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataServiceGroup &GroupId=ds_123 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Group>
```

`<GroupName>`业务流程名称`</GroupName>`

```xml
    <TenantId>10002</TenantId>
    <CreatedTime>2020-09-24T18:37:51+0800</CreatedTime>
```

`<Description>`业务流程的描述`</Description>`

```xml
    <ModifiedTime>2020-09-24T18:37:51+0800</ModifiedTime>
    <CreatorId>123456789</CreatorId>
    <ApiGatewayGroupId>100abc</ApiGatewayGroupId>
    <ProjectId>10001</ProjectId>
    <GroupId>ds_123</GroupId>
</Group> <RequestId>0000-ABCD-EFG*****</RequestId>
```

`JSON` 格式 DataWorks

```json
{"Group":{"GroupName":"业务流程名称","TenantId":"10002","CreatedTime":"2020-09-24T18:37:5 1+0800","Description":"业务流程的描述","ModifiedTime":"2020-09- 24T18:37:51+0800","CreatorId":"123456789","ApiGatewayGroupId":"100abc","ProjectId":"10001 "GroupId":"ds_123"},"RequestId":"0000-ABCD-EFG*****"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### GetDataServicePublishedApi

调用GetDataServicePublishedApi查询数据服务API的发布态信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetDataServiceP ublishedApi | 系统规定参数。取值： GetDataServicePublishedApi。 |
| ApiId | Long | 是 | 10001 | API的ID。 |
| ProjectId | Long | 是 | 10002 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10003 | 租户ID。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | API的最新发布态信息。 |
| ApiId | Long | 10001 | 数据服务API的ID。 |
| ApiMode | Integer | 0 | API的类型，可选枚举值包括0（向导API）、 1（脚本API）和2（注册API）。 |
| ApiName | String | test | API的名称。 |
| ApiPath | String | /test/1 | API的路径。 |
| CreatedTime | String | 2020-06- 23T00:21:01+0800 | 创建时间。 |
| CreatorId | String | 123456789 | 创建人的阿里云ID。 |
| Description | String | 测试API。 | 描述信息。 |
| GroupId | String | ab12** | 分组ID。 |
| ModifiedTime | String | 2020-06- 23T00:21:01+0800 | 最近修改的时间。 |
| OperatorId | String | 234567891 | 最新编辑人的阿里云ID。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| Protocols | List | 0 | API协议，多值列表，可选枚举值包括 0（HTTP）和1（HTTPS）。 |
| RegistrationDe tails | Struct |  | 注册API详情，只有注册API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| RegistrationErr orCodes | Array of RegistrationErr orCode |  | 注册API的错误码列表。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |

DataWorks

| ErrorSolution | String | retry | 错误解决方案。 |
|---|---|---|---|
| RegistrationRe questParamet ers | Array of RegistrationRe questParamet er |  | 注册API的请求参数列表。 |
| DefaultValue | String | default1 | 默认值。 |
| ExampleValue | String | sample1 | 示例值。 |
| IsRequiredPar ameter | Boolean | true | 是否必填。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description1 | 描述信息。 |
| ParameterNa me | String | name1 | 参数名称。 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值包括0（Equal）、 1（Like）、2（Const）和3（In）。向导模式 API支持Equal、Like和In，脚本模式API支持 Equal，注册API支持Equal和Const。 |
| ParameterPosi tion | Integer | 0 | 参数的位置，可选枚举值包括0（Path）、 1（Query）、2（Head）和3（Body）。向导和脚本API仅支持Query。注册API中的GET、 DELETE方法支持Query、Head，PUT、POST 方法支持Query、Head和Body。 |
| ServiceConten tType | Integer | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API支持 JSON，注册API支持JSON和XML。 |
| ServiceHost | String | http://www.***.com | 后端服务地址。 |
| ServicePath | String | /index | 后端服务路径。 |
| ServiceReques tBodyDescripti on | String | {"abc":1} | 后端请求body内容的描述。 |
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |

DataWorks

| RequestMetho d | Integer | 0 | API的请求方式，可选枚举值包括0（GET）、 1（POST）、2（PUT）和3（DELTE）。向导和脚本API支持GET和POST。注册API支持 GET、POST、PUT和DELETE。 |
|---|---|---|---|
| ResponseCont entType | Integer | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API支持 JSON，注册API支持JSON和XML。 |
| ScriptDetails | Struct |  | 脚本API详情，只有脚本API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| Script | String | select a from t | SQL脚本。 |
| ScriptConnecti on | Struct |  | 脚本API的数据源信息。 |
| ConnectionId | Long | 1001 | 数据源的ID。 |
| TableName | String | tablename | 数据源的表名称。 |
| ScriptErrorCod es | Array of ScriptErrorCod e |  | 脚本API的错误码列表。 |
| ErrorCode | String | 1001 | 错误码。 |
| ErrorMessage | String | fail to call | 错误信息。 |
| ErrorSolution | String | retry | 错误解决方案。 |
| ScriptRequest Parameters | Array of ScriptRequest Parameter |  | 脚本API的请求参数列表。 |
| DefaultValue | String | default1 | 默认值。 |
| ExampleValue | String | example1 | 示例值。 |
| IsRequiredPar ameter | Boolean | true | 是否必填。 |

DataWorks

| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean |
|---|---|---|---|
| ParameterDes cription | String | description1 | 参数描述。 |
| ParameterNa me | String | paraname | 参数名称。 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值有： 0：Equal 1：Like 2：Const 3：In 向导API支持Equal、Like、In；脚本API支持 Equal；注册API支持Equal、Const。 |
| ParameterPosi tion | Integer | 0 | 参数位置，可选枚举值有： 0：Path 1：Query 2：Head 3：Body 向导和脚本API，只支持Query；注册 API，GET、DELETE方法支持Query、 Head，PUT、POST方法支持Query、Head、 Body。 |
| ScriptRespons eParameters | Array of ScriptRespons eParameter |  | 脚本API的返回参数列表。 |
| ExampleValue | String | example2 | 示例值。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description2 | 参数描述。 |
| ParameterNa me | String | paraname2 | 参数名称。 |
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |

DataWorks

| Status | Integer | 1 | API的状态，可选枚举值包括0（未发布）和 1（已发布）。 |
|---|---|---|---|
| TenantId | Long | 10002 | 租户ID。 |
| Timeout | Integer | 1000 | 超时时间，单位为毫秒（ms）。 |
| VisibleRange | Integer | 0 | 可见范围，可选枚举值包括0（工作空间）和 1（私有）。 |
| WizardDetails | Struct |  | 向导API详情，只有向导API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |
| WizardConnec tion | Struct |  | 向导API的数据源信息。 |
| ConnectionId | Long | 123 | 数据源的ID。 |
| TableName | String | tablename2 | 数据源的表名称。 |
| WizardErrorCo des | Array of WizardErrorCo de |  | 向导API的错误码列表。 |
| ErrorCode | String | 1001 | 错误码。 |
| ErrorMessage | String | fail to call | 错误信息。 |
| ErrorSolution | String | retry | 错误解决方案。 |
| WizardReques tParameters | Array of WizardReques tParameter |  | 向导API的请求参数列表。 |
| DefaultValue | String | default3 | 默认值。 |
| ExampleValue | String | example3 | 示例值。 |

DataWorks

| IsRequiredPar ameter | Boolean | true | 是否必填。 |
|---|---|---|---|
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description3 | 参数描述。 |
| ParameterNa me | String | paraname3 | 参数名称。 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值包括0（Equal）、 1（Like）、2（Const）和3（In）。向导模式 API支持Equal、Like和In，脚本模式API支持 Equal，注册API支持Equal和Const。 |
| ParameterPosi tion | Integer | 0 | 参数的位置，可选枚举值包括0（Path）、 1（Query）、2（Head）和3（Body）。向导和脚本API仅支持Query。注册API中的GET、 DELETE方法支持Query、Head，PUT、POST 方法支持Query、Head和Body。 |
| WizardRespon seParameters | Array of WizardRespon seParameter |  | 向导API的返回参数列表。 |
| ExampleValue | String | example4 | 示例值。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description4 | 参数描述。 |
| ParameterNa me | String | paraname4 | 参数名称。 |
| ErrorCode | String | 200 | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

DataWorks

| Success | Boolean | true | 是否调用成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetDataServicePublishedApi &ApiId=10001 &ProjectId=10002 &RegionId=default &TenantId=10003
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <Status>1</Status>
    <VisibleRange>0</VisibleRange>
    <Description>测试API。</Description>
    <CreatedTime>2020-06-23T00:21:01+0800</CreatedTime>
    <ApiName>test</ApiName>
    <Timeout>1000</Timeout>
    <RequestMethod>0</RequestMethod>
    <CreatorId>123456789</CreatorId>
    <ProjectId>10001</ProjectId>
    <ResponseContentType>0</ResponseContentType>
    <OperatorId>234567891</OperatorId>
    <GroupId>ab12**</GroupId>
    <TenantId>10002</TenantId>
    <ModifiedTime>2020-06-23T00:21:01+0800</ModifiedTime>
    <ApiMode>0</ApiMode>
    <ApiId>10001</ApiId>
    <ApiPath>/test/1</ApiPath>
    <Protocols>0</Protocols>
    <RegistrationDetails>
        <ServiceRequestBodyDescription>{"abc":1}</ServiceRequestBodyDescription>
        <SuccessfulResultSample>{"success": true}</SuccessfulResultSample>
        <ServiceContentType>0</ServiceContentType>
        <ServicePath>/index</ServicePath>
        <FailedResultSample>{"success": false}</FailedResultSample>
        <ServiceHost>http://www.***.com</ServiceHost>
        <RegistrationErrorCodes>
            <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode>
            <ErrorSolution>retry</ErrorSolution>
            <ErrorMessage>The connection does not exist.</ErrorMessage>
        </RegistrationErrorCodes>
        <RegistrationRequestParameters>
            <DefaultValue>default1</DefaultValue>
            <ExampleValue>sample1</ExampleValue>
```

`<P` t

```
DtT >0</P
```

t

```
DtT
```

> DataWorks

```xml
            <ParameterDataType>0</ParameterDataType>
            <ParameterPosition>0</ParameterPosition>
            <ParameterName>name1</ParameterName>
            <ParameterOperator>0</ParameterOperator>
            <ParameterDescription>description1</ParameterDescription>
            <IsRequiredParameter>true</IsRequiredParameter>
        </RegistrationRequestParameters>
    </RegistrationDetails>
    <ScriptDetails>
        <Script>select a from t</Script>
        <IsPagedResponse>true</IsPagedResponse>
        <SuccessfulResultSample>{"success": true}</SuccessfulResultSample>
        <FailedResultSample>{"success": false}</FailedResultSample>
        <ScriptErrorCodes>
            <ErrorCode>1001</ErrorCode>
            <ErrorSolution>retry</ErrorSolution>
            <ErrorMessage>fail to call</ErrorMessage>
        </ScriptErrorCodes>
        <ScriptResponseParameters>
            <ExampleValue>example2</ExampleValue>
            <ParameterDataType>0</ParameterDataType>
            <ParameterName>paraname2</ParameterName>
            <ParameterDescription>description2</ParameterDescription>
        </ScriptResponseParameters>
        <ScriptRequestParameters>
            <DefaultValue>default1</DefaultValue>
            <ExampleValue>example1</ExampleValue>
            <ParameterDataType>0</ParameterDataType>
            <ParameterPosition>0</ParameterPosition>
            <ParameterName>paraname</ParameterName>
            <ParameterOperator>0</ParameterOperator>
            <ParameterDescription>description1</ParameterDescription>
            <IsRequiredParameter>true</IsRequiredParameter>
        </ScriptRequestParameters>
        <ScriptConnection>
            <TableName>tablename</TableName>
            <ConnectionId>1001</ConnectionId>
        </ScriptConnection>
    </ScriptDetails>
    <WizardDetails>
        <IsPagedResponse>true</IsPagedResponse>
        <SuccessfulResultSample>{"success": true}</SuccessfulResultSample>
        <FailedResultSample>{"success": false}</FailedResultSample>
        <WizardErrorCodes>
            <ErrorCode>1001</ErrorCode>
            <ErrorSolution>retry</ErrorSolution>
            <ErrorMessage>fail to call</ErrorMessage>
        </WizardErrorCodes>
        <WizardResponseParameters>
            <ExampleValue>example4</ExampleValue>
            <ParameterDataType>0</ParameterDataType>
            <ParameterName>paraname4</ParameterName>
            <ParameterDescription>description4</ParameterDescription>
        </WizardResponseParameters>
<WizardRequestParameters>
```

DataWorks

```xml
        <WizardRequestParameters>
            <DefaultValue>default3</DefaultValue>
            <ExampleValue>example3</ExampleValue>
            <ParameterDataType>0</ParameterDataType>
            <ParameterPosition>0</ParameterPosition>
            <ParameterName>paraname3</ParameterName>
            <ParameterOperator>0</ParameterOperator>
            <ParameterDescription>description3</ParameterDescription>
            <IsRequiredParameter>true</IsRequiredParameter>
        </WizardRequestParameters>
        <WizardConnection>
            <TableName>tablename2</TableName>
            <ConnectionId>123</ConnectionId>
        </WizardConnection>
    </WizardDetails>
</Data> <ErrorCode>200</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data": {"Status":"1","VisibleRange":"0","Description":"测试API。","CreatedTime":"2020-06-23T00: 21:01+0800","ApiName":"test","Timeout":"1000","RequestMethod":"0","CreatorId":"123456789" ProjectId":"10001","ResponseContentType":"0","OperatorId":"234567891","GroupId":"ab12**", enantId":"10002","ModifiedTime":"2020-06- 23T00:21:01+0800","ApiMode":"0","ApiId":"10001","ApiPath":"/test/1","Protocols":"0","Regi rationDetails":{"ServiceRequestBodyDescription":" {\"abc\":1}","SuccessfulResultSample":"{\"success\": true}","ServiceContentType":"0","ServicePath":"/index","FailedResultSample":"{\"success \": false}","ServiceHost":"http://www.***.com","RegistrationErrorCodes": [{"ErrorCode":"Invalid.Tenant.ConnectionNotExists","ErrorSolution":"retry","ErrorMessage" The connection does not exist."}],"RegistrationRequestParameters": [{"DefaultValue":"default1","ExampleValue":"sample1","ParameterDataType":"0","ParameterPo tion":"0","ParameterName":"name1","ParameterOperator":"0","ParameterDescription":"descrip on1","IsRequiredParameter":"true"}]},"ScriptDetails":{"Script":"select a from t","IsPag edResponse":"true","SuccessfulResultSample":"{\"success\": true}","FailedResultSample":"{\"success\": false}","ScriptErrorCodes": [{"ErrorCode":"1001","ErrorSolution":"retry","ErrorMessage":"fail to call"}],"ScriptResponseParameters": [{"ExampleValue":"example2","ParameterDataType":"0","ParameterName":"paraname2","Paramete escription":"description2"}],"ScriptRequestParameters": [{"DefaultValue":"default1","ExampleValue":"example1","ParameterDataType":"0","ParameterP ition":"0","ParameterName":"paraname","ParameterOperator":"0","ParameterDescription":"des iption1","IsRequiredParameter":"true"}],"ScriptConnection": {"TableName":"tablename","ConnectionId":"1001"}},"WizardDetails": {"IsPagedResponse":"true","SuccessfulResultSample":"{\"success\": true}","FailedResultSample":"{\"success\": false}","WizardErrorCodes": [{"ErrorCode":"1001","ErrorSolution":"retry","ErrorMessage":"fail to call"}],"WizardResponseParameters": [{"ExampleValue":"example4","ParameterDataType":"0","ParameterName":"paraname4","Paramete escription":"description4"}],"WizardRequestParameters": [{"DefaultValue":"default3","ExampleValue":"example3","ParameterDataType":"0","ParameterP ition":"0","ParameterName":"paraname3","ParameterOperator":"0","ParameterDescription":"de ription3","IsRequiredParameter":"true"}],"WizardConnection": {"TableName":"tablename2","ConnectionId":"123"}}},"ErrorCode":"200","ErrorMessage":"The connection does not exist.","Success":"true"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

DataWorks

| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
|---|---|---|---|
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListDataServiceApis

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataService Apis | 系统规定参数。取值： ListDataServiceApis。 |
| PageNumber | Integer | 是 | 1 | 页码，从1开始，默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectId | Long | 是 | 10000 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10001 | 租户ID。 |
| ApiNameKeywor d | String | 否 | 我的API名称 | API名称的关键词，过滤得到API名称包含该关键词的API。 |
| ApiPathKeyword | String | 否 | /test/ | API路径的关键词，过滤得到API路径包含该关键词的API。 |
| CreatorId | String | 否 | 12345 | API创建者的阿里云ID，过滤得到该用户创建的API。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 返回开发中API的信息。 |

DataWorks

| Apis | Array of Api |  | API开发态信息列表。 |
|---|---|---|---|
| ApiId | Long | 10002 | API的ID。 |
| ApiMode | Integer | 0 | API的类型，可选枚举值包括0（向导API）、 1（脚本API）和2（注册API）。 |
| ApiName | String | 我的API名称 | API的名称。 |
| ApiPath | String | /test/1 | API的路径。 |
| CreatedTime | String | 2020-06- 23T00:21:01+0800 | 创建时间。 |
| CreatorId | String | 1234567 | 创建人的阿里云ID。 |
| Description | String | 测试API描述 | API的描述信息。 |
| FolderId | Long | 0 | 文件夹ID。 |
| GroupId | String | abcde123456789 | 分组ID。 |
| ModifiedTime | String | 2020-06- 23T00:21:01+0800 | 最新修改时间。 |
| OperatorId | String | 2345678 | 最新编辑人的阿里云ID。 |
| ProjectId | Long | 10000 | 工作空间的ID。 |
| Protocols | List | 0 | API的协议，多值列表，可选枚举值包括 0（HTTP）和1（HTTPS）。 |
| RegistrationDe tails | Struct |  | 注册API的详情，只有注册API返回。 |
| FailedResultSa mple | String | {"success": false} | 错误返回示例。 |
| RegistrationErr orCodes | Array of RegistrationErr orCode |  | 注册API的错误码列表。 |
| ErrorCode | String | 1001 | 错误码。 |

DataWorks

| ErrorMessage | String | fail to call | 错误信息。 |
|---|---|---|---|
| ErrorSolution | String | retry | 错误解决方案。 |
| RegistrationRe questParamet ers | Array of RegistrationRe questParamet er |  | 注册API的请求参数列表。 |
| ColumnName | String | column1 | 绑定的表字段名称，仅向导模式支持。 |
| DefaultValue | String | default1 | 默认值。 |
| ExampleValue | String | example1 | 示例值。 |
| IsRequiredPar ameter | Boolean | true | 是否必填。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description1 | 描述的信息。 |
| ParameterNa me | String | name1 | 参数的名称。 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值包括0（Equal）、 1（Like）、2（Const）和3（In）。向导模式 API支持Equal、Like和In，脚本模式API支持 Equal，注册API支持Equal和Const。 |
| ParameterPosi tion | Integer | 0 | 参数的位置，可选枚举值包括0（Path）、 1（Query）、2（Head）和3（Body）。向导和脚本API仅支持Query。注册API中的GET、 DELETE方法支持Query、Head，PUT、POST 方法支持Query、Head和Body。 |
| ServiceConten tType | Integer | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API支持 JSON，注册API支持JSON和XML。 |
| ServiceHost | String | http://www.abc.co m | 后端服务地址。 |
| ServicePath | String | /index | 后端服务路径。 |

DataWorks

| ServiceReques tBodyDescripti on | String | {"abc":1} | 后端请求body内容的描述信息。 |
|---|---|---|---|
| SuccessfulRes ultSample | String | {"success": true} | 正常返回示例。 |
| RequestMetho d | Integer | 0 | API的请求方式，可选枚举值包括0（GET）、 1（POST）、2（PUT）和3（DELTE）。向导和脚本API支持GET和POST。注册API支持 GET、POST、PUT和DELETE。 |
| ResponseCont entType | Integer | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API支持 JSON，注册API支持JSON和XML。 |
| ScriptDetails | Struct |  | 脚本API的详情，只有脚本API返回。 |
| IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| Script | String | select a from t | SQL脚本。 |
| ScriptConnecti on | Struct |  | 脚本API的数据源信息。 |
| ConnectionId | Long | 123 | 数据源ID。 |
| TableName | String | t | 数据源表的名称。 |
| ScriptRequest Parameters | Array of ScriptRequest Parameter |  | 脚本API的请求参数列表。 |
| ColumnName | String | column1 | 绑定的表字段名称，仅向导模式支持。 |
| DefaultValue | String | default1 | 默认值 |
| ExampleValue | String | example1 | 示例值 |
| IsRequiredPar ameter | Boolean | true | 是否必填 |

DataWorks

| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean |
|---|---|---|---|
| ParameterDes cription | String | description1 | 描述 |
| ParameterNa me | String | name1 | 参数名称 |
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值有： 0：Equal 1：Like 2：Const 3：In 向导API支持Equal、Like、In；脚本API支持 Equal；注册API支持Equal、Const。 |
| ParameterPosi tion | Integer | 0 | 参数位置，可选枚举值有： 0：Path 1：Query 2：Head 3：Body 向导和脚本API，只支持Query；注册 API，GET、DELETE方法支持Query、 Head，PUT、POST方法支持Query、Head、 Body。 |
| ScriptRespons eParameters | Array of ScriptRespons eParameter |  | 脚本API的返回参数列表。 |
| ColumnName | String | column2 | 绑定的表字段名称，仅向导模式有 |
| ExampleValue | String | example2 | 示例值 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值： 0：String 1：Int 2：Long 3：Float 4：Double 5：Boolean |

DataWorks

| ParameterDes cription | String | description2 | 描述 |
|---|---|---|---|
| ParameterNa me | String | param2 | 参数名称 |
| Status | Integer | 0 | API的状态，可选枚举值包括0（未发布）和 1（已发布）。 |
| TenantId | Long | 10000 | 租户ID。 |
| Timeout | Integer | 10000 | 超时时间，单位为毫秒（ms）。 |
| VisibleRange | Integer | 0 | 可见范围，可选枚举值包括0（工作空间）和 1（私有）。 |
| WizardDetails | Struct |  | 向导API的详情，只有向导API返回。 |
| IsPagedRespo nse | Boolean | true | 返回是否分页。 |
| WizardConnec tion | Struct |  | 向导API的数据源信息。 |
| ConnectionId | Long | 123 | 数据源ID。 |
| TableName | String | t | 数据源表的名称。 |
| WizardReques tParameters | Array of WizardReques tParameter |  | 向导API的请求参数列表。 |
| ColumnName | String | column1 | 绑定的表字段名称，仅向导模式支持。 |
| DefaultValue | String | default1 | 默认值。 |
| ExampleValue | String | example1 | 示例值。 |
| IsRequiredPar ameter | Boolean | true | 是否必填。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description1 | 描述信息。 |

DataWorks

| ParameterNa me | String | param1 | 参数名称。 |
|---|---|---|---|
| ParameterOpe rator | Integer | 0 | 运算符，可选枚举值包括0（Equal）、 1（Like）、2（Const）和3（In）。向导API支持Equal、Like和In，脚本API支持Equal，注册 API支持Equal和Const。 |
| ParameterPosi tion | Integer | 0 | 参数的位置，可选枚举值包括0（Path）、 1（Query）、2（Head）和3（Body）。向导和脚本API仅支持Query。注册API中的GET、 DELETE方法支持Query、Head，PUT、POST 方法支持Query、Head和Body。 |
| WizardRespon seParameters | Array of WizardRespon seParameter |  | 向导模式的返回参数列表。 |
| ColumnName | String | column2 | 绑定的表字段名称，仅向导模式支持。 |
| ExampleValue | String | example2 | 示例值。 |
| ParameterDat aType | Integer | 0 | 数据类型，可选枚举值包括0（STRING）、 1（INT）、2（LONG）、3（FLOAT）、 4（DOUBLE）和5（BOOLEAN）。 |
| ParameterDes cription | String | description2 | 描述信息。 |
| ParameterNa me | String | param2 | 参数的名称。 |
| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Integer | 100 | 总记录数。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |

DataWorks

| Success | Boolean | true | 调用是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServiceApis &PageNumber=1 &PageSize=10 &ProjectId=10000 &RegionId=default &TenantId=10001
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG****","HttpStatusCode":"200","Data": {"TotalCount":"100","PageSize":"10","PageNumber":"1","Apis": [{"Status":"0","VisibleRange":"0","Description":"测试API描述","CreatedTime":"2020-06-23T 00:21:01+0800","ApiName":"我的API名称","Timeout":"10000","RequestMethod":"0","CreatorId":"1234567","ProjectId":"10000","Respo seContentType":"0","FolderId":"0","OperatorId":"2345678","GroupId":"abcde123456789","Tena Id":"10000","ModifiedTime":"2020-06- 23T00:21:01+0800","ApiMode":"0","ApiId":"10002","ApiPath":"/test/1","Protocols":"0","Regi rationDetails":{"ServiceRequestBodyDescription":" {\"abc\":1}","SuccessfulResultSample":"{\"success\": true}","ServiceContentType":"0","ServicePath":"/index","FailedResultSample":"{\"success \": false}","ServiceHost":"http://www.abc.com","RegistrationErrorCodes": [{"ErrorCode":"1001","ErrorSolution":"retry","ErrorMessage":"fail to call"}],"RegistrationRequestParameters": [{"DefaultValue":"default1","ColumnName":"column1","ExampleValue":"example1","ParameterDa Type":"0","ParameterPosition":"0","ParameterName":"name1","ParameterOperator":"0","Parame rDescription":"description1","IsRequiredParameter":"true"}]},"ScriptDetails":{"Script": "select a from t","IsPagedResponse":"true","ScriptResponseParameters": [{"ColumnName":"column2","ExampleValue":"example2","ParameterDataType":"0","ParameterName "param2","ParameterDescription":"description2"}],"ScriptRequestParameters": [{"DefaultValue":"default1","ColumnName":"column1","ExampleValue":"example1","ParameterDa Type":"0","ParameterPosition":"0","ParameterName":"name1","ParameterOperator":"0","Parame rDescription":"description1","IsRequiredParameter":"true"}],"ScriptConnection":{"TableN ame":"t","ConnectionId":"123"}},"WizardDetails": {"IsPagedResponse":"true","WizardResponseParameters": [{"ColumnName":"column2","ExampleValue":"example2","ParameterDataType":"0","ParameterName "param2","ParameterDescription":"description2"}],"WizardRequestParameters": [{"DefaultValue":"default1","ColumnName":"column1","ExampleValue":"example1","ParameterDa Type":"0","ParameterPosition":"0","ParameterName":"param1","ParameterOperator":"0","Param erDescription":"description1","IsRequiredParameter":"true"}],"WizardConnection":{"Table Name":"t","ConnectionId":"123"}}}]},"ErrorCode":"Invalid.Tenant.ConnectionNotExists","Err Message":"The connection does not exist.","Success":"true"}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListDataServiceApiAuthorities

调用ListDataServiceApiAuthorities获取授权给他人的API列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataService ApiAuthorities | 系统规定参数。取值： ListDataServiceApiAuthorities。 |
| PageNumber | Integer | 是 | 1 | 页码，从1开始，默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectId | Long | 是 | 10000 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10001 | 租户ID。 |
| ApiNameKeywor d | String | 否 | 我的API名称 | API名称的关键词，通过过滤获取API名称包含该关键词的API。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 授权给他人的API列表。 |
| ApiAuthorizati onList | Array of ApiAuthorizati on |  | 授权给他人的API列表和授权详情。 |
| ApiId | Long | 10002 | API的ID。 |
| ApiName | String | 我的API名称 | API的名称。 |
| ApiPath | String | /test/1 | API的路径。 |
| ApiStatus | Integer | 0 | API的状态，可选枚举值包括0（未发布）和 1（已发布）。 |
| AuthorizationR ecords | Array of AuthorizationR ecord |  | 授权给他人的授权详情列表。 |
| CreatedTime | String | 2020-06- 23T00:21:01+0800 | 授权时间。 |
| CreatorId | String | 12345 | 授权者的阿里云用户ID。 |
| EndTime | String | 2020-06- 24T00:21:01+0800 | 授权有效期的截止时间。 |
| ProjectId | Long | 10004 | 获得授权的工作空间ID。 |
| CreatedTime | String | 2020-06- 23T00:21:01+0800 | API的创建时间。 |
| CreatorId | String | 12345 | API负责人的阿里云ID。 |
| GroupId | String | ab123 | 分组ID。 |
| ModifiedTime | String | 2020-06- 23T00:21:01+0800 | API的最近更新时间。 |
| ProjectId | Long | 10000 | 工作空间的ID。 |
| TenantId | Long | 10001 | 租户ID。 |
| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |

DataWorks

| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
|---|---|---|---|
| TotalCount | Integer | 100 | 总记录数。 |
| ErrorCode | String | 0 | 错误码。 |
| ErrorMessage | String | 正常 | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServiceApiAuthorities &PageNumber=1 &PageSize=10 &ProjectId=10000 &RegionId=default &TenantId=10001
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <ApiAuthorizationList>
        <TenantId>10001</TenantId>
        <CreatedTime>2020-06-23T00:21:01+0800</CreatedTime>
        <ModifiedTime>2020-06-23T00:21:01+0800</ModifiedTime>
```

`<ApiName>`我的`API`名称`</ApiName>`

```xml
        <CreatorId>12345</CreatorId>
        <ProjectId>10000</ProjectId>
        <ApiStatus>0</ApiStatus>
        <ApiId>10002</ApiId>
        <ApiPath>/test/1</ApiPath>
        <GroupId>ab123</GroupId>
        <AuthorizationRecords>
            <CreatedTime>2020-06-23T00:21:01+0800</CreatedTime>
            <EndTime>2020-06-24T00:21:01+0800</EndTime>
            <CreatorId>12345</CreatorId>
            <ProjectId>10004</ProjectId>
        </AuthorizationRecords>
    </ApiAuthorizationList>
</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>正常</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "ApiAuthorizationList": {
            "TenantId": 10001,
            "CreatedTime": "2020-06-23T00:21:01+0800",
            "ModifiedTime": "2020-06-23T00:21:01+0800",
```

`"ApiName": "`我的`API`名称`",`

```json
            "CreatorId": 12345,
            "ProjectId": 10000,
            "ApiStatus": 0,
            "ApiId": 10002,
            "ApiPath": "/test/1",
            "GroupId": "ab123",
            "AuthorizationRecords": {
                "CreatedTime": "2020-06-23T00:21:01+0800",
                "EndTime": "2020-06-24T00:21:01+0800",
                "CreatorId": 12345,
                "ProjectId": 10004
            }
        }
    },
    "ErrorCode": 0,
    "ErrorMessage": "正常",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |
|---|---|---|---|

#### ListDataServiceApplications

调用ListDataServiceApplications获取数据服务应用的基础信息列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataService Applications | 系统规定参数。取值： ListDataServiceApplications。 |
| PageNumber | Integer | 是 | 1 | 页码，从1开始，默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectIdList | String | 是 | 10000,100001 | 指定工作空间ID查询应用。支持多值，多值之间使用英文逗号（,）分隔。最少指定 1个工作空间ID，最多指定50个工作空间 ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 100002 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 查询得到的应用基础信息。 |
| Applications | Array of Application |  | 应用的基础信息列表。 |
| ApplicationId | Long | 20000 | 应用ID。 |
| ApplicationNa me | String | 我的应用 | 应用的名称。 |
| ProjectId | Long | 10000 | 工作空间的ID。 |

DataWorks

| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Integer | 100 | 总记录数。 |
| ErrorCode | String | 0 | 错误码。 |
| ErrorMessage | String | 正常 | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD-EFG*** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServiceApplications &PageNumber=1 &PageSize=10 &ProjectIdList=10000,100001 &RegionId=default &TenantId=100002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG***</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Applications>
        <ApplicationName>我的应用</ApplicationName>
        <ProjectId>10000</ProjectId>
        <ApplicationId>20000</ApplicationId>
    </Applications>
</Data> <ErrorCode>0</ErrorCode> <ErrorMessage>正常</ErrorMessage> <Success>true</Success>
```

DataWorks `JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG***",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "Applications": {
```

`"ApplicationName": "`我的应用`",`

```json
            "ProjectId": 10000,
            "ApplicationId": 20000
        }
    },
    "ErrorCode": 0,
    "ErrorMessage": "正常",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListDataServiceAuthorizedApis

调用ListDataServiceAuthorizedApis获取获得授权的API信息列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | ListDataService AuthorizedApis | 系统规定参数。取值： ListDataServiceAuthorizedApis。 |
|---|---|---|---|---|
| PageNumber | Integer | 是 | 1 | 页码，从1开始，默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectId | Long | 是 | 10000 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10001 | 租户ID。 |
| ApiNameKeywor d | String | 否 | 我的API名称 | API名称的关键词，通过过滤获取API名称包含该关键词的API。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Struct |  | 获得授权的API信息。 |
| ApiAuthorized List | Array of ApiAuthorized |  | 获得授权的API列表。 |
| ApiId | Long | 10002 | API的ID。 |
| ApiName | String | 我的API名称 | API的名称。 |
| ApiPath | String | /test/1 | API的路径。 |
| ApiStatus | Integer | 0 | API的状态，可选枚举值包括0（未发布）和 1（已发布）。 |
| CreatedTime | String | 2020-06- 23T00:21:01+0800 | API的创建时间。 |
| CreatorId | String | 12345 | API负责人阿里云ID |
| GrantCreatedT ime | String | 2020-06- 23T00:21:01+0800 | API的授权时间。 |

DataWorks

| GrantEndTime | String | 2020-06- 24T00:21:01+0800 | API的授权到期时间。 |
|---|---|---|---|
| GrantOperator Id | String | 23456 | 授权者的阿里云ID。 |
| GroupId | String | abcde123456789 | 分组ID。 |
| ModifiedTime | String | 2020-06- 23T00:21:01+0800 | API的最近更新时间。 |
| ProjectId | Long | 10000 | 工作空间的ID。 |
| TenantId | Long | 10001 | 租户ID。 |
| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Integer | 100 | 总记录数。 |
| ErrorCode | String | 1031203110005 | 错误码。 |
| ErrorMessage | String | The specified parameters are invalid. | 错误信息 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServiceAuthorizedApis &PageNumber=1 &PageSize=10 &ProjectId=10000 &RegionId=default &TenantId=10001
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <ApiAuthorizedList>
        <GrantEndTime>2020-06-24T00:21:01+0800</GrantEndTime>
        <TenantId>10001</TenantId>
        <CreatedTime>2020-06-23T00:21:01+0800</CreatedTime>
        <ModifiedTime>2020-06-23T00:21:01+0800</ModifiedTime>
        <GrantOperatorId>23456</GrantOperatorId>
```

`<ApiName>`我的`API`名称`</ApiName>`

```xml
        <CreatorId>12345</CreatorId>
        <ProjectId>10000</ProjectId>
        <ApiStatus>0</ApiStatus>
        <GrantCreatedTime>2020-06-23T00:21:01+0800</GrantCreatedTime>
        <ApiId>10002</ApiId>
        <ApiPath>/test/1</ApiPath>
        <GroupId>abcde123456789</GroupId>
    </ApiAuthorizedList>
</Data> <ErrorCode>1031203110005</ErrorCode> <ErrorMessage>The specified parameters are invalid.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": {
        "TotalCount": 100,
        "PageSize": 10,
        "PageNumber": 1,
        "ApiAuthorizedList": {
            "GrantEndTime": "2020-06-24T00:21:01+0800",
            "TenantId": 10001,
            "CreatedTime": "2020-06-23T00:21:01+0800",
            "ModifiedTime": "2020-06-23T00:21:01+0800",
            "GrantOperatorId": 23456,
```

`"ApiName": "`我的`API`名称`",`

```json
            "CreatorId": 12345,
            "ProjectId": 10000,
            "ApiStatus": 0,
            "GrantCreatedTime": "2020-06-23T00:21:01+0800",
            "ApiId": 10002,
            "ApiPath": "/test/1",
            "GroupId": "abcde123456789"
        }
    },
    "ErrorCode": 1031203110005,
    "ErrorMessage": "The specified parameters are invalid.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

DataWorks

#### ListDataServiceFolders

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataServiceF olders | 系统规定参数。取值： ListDataServiceFolders。 |
| PageNumber | Integer | 是 | 1 | 页码，从1开始。默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10002 | 租户ID。 |
| GroupId | String | 否 | 10003 | 指定文件夹所属业务流程的ID。 |
| FolderNameKey word | String | 否 | 文件夹名称关键词 | 文件夹名称关键词，可以进行子串匹配。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FolderPagingR esult | Struct |  | 文件夹列表的分页结果。 |
| Folders | Array of Folder |  | 文件夹列表。 |
| CreatedTime | String | 2020-09- 24T18:37:51+0800 | 文件夹的创建时间。 |
| FolderId | Long | 11 | 文件夹的ID。 |
| FolderName | String | filename | 文件夹名称。 |
| GroupId | String | 10003 | 文件夹所属业务流程的ID。 |

DataWorks

| ModifiedTime | String | 2020-09- 24T18:37:51+0800 | 文件夹的编辑时间。 |
|---|---|---|---|
| ParentId | Long | 0 | 父文件夹的ID。业务流程下根文件夹ID等于0， 用户创建文件夹ID大于0。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| TenantId | Long | 10002 | 租户ID。 |
| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Integer | 100 | 总记录数。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServiceFolders &PageNumber=1 &PageSize=10 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <FolderPagingResult>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Folders>
        <ParentId>0</ParentId>
        <TenantId>10002</TenantId>
        <CreatedTime>2020-09-24T18:37:51+0800</CreatedTime>
        <ModifiedTime>2020-09-24T18:37:51+0800</ModifiedTime>
        <ProjectId>10001</ProjectId>
        <FolderId>11</FolderId>
        <FolderName>filename</FolderName>
        <GroupId>10003</GroupId>
    </Folders>
</FolderPagingResult>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","FolderPagingResult": {"TotalCount":"100","PageSize":"10","PageNumber":"1","Folders": [{"ParentId":"0","TenantId":"10002","CreatedTime":"2020-09- 24T18:37:51+0800","ModifiedTime":"2020-09- 24T18:37:51+0800","ProjectId":"10001","FolderId":"11","FolderName":"filename","GroupId":" 003"}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### ListDataServiceGroups

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDataService Groups | 系统规定参数。取值： ListDataServiceGroups。 |
| PageNumber | Integer | 是 | 1 | 页码，从1开始，默认值为1。 |
| PageSize | Integer | 是 | 10 | 每页显示的条数，默认为10条，最大100 条。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10003 | 租户ID。 |
| GroupNameKey word | String | 否 | 测试业务流程 | 业务流程名称关键词，可以进行子串匹配。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| GroupPagingR esult | Struct |  | 业务流程的分页结果。 |
| Groups | Array of Group |  | 业务流程列表。 |
| ApiGatewayGr oupId | String | 100abc | 业务流程绑定的API网关分组ID。 |
| CreatedTime | String | 2020-09- 24T18:37:51+0800 | 业务流程的创建时间。 |
| CreatorId | String | 123123123123 | 创建人UID，部分历史业务流程的创建人UID可能为空。 |
| Description | String | 业务流程的描述 | 业务流程的描述。 |
| GroupId | String | ds 123abc _ | 业务流程的ID。 |

DataWorks

| GroupName | String | 业务流程名称 | 业务流程名称。 |
|---|---|---|---|
| ModifiedTime | String | 2020-09- 24T18:37:51+0800 | 业务流程的编辑时间。 |
| ProjectId | Long | 10001 | DataWorks工作空间ID。 |
| TenantId | Long | 10003 | 租户ID。 |
| PageNumber | Integer | 1 | 页码，和请求中的PageNumber一致。 |
| PageSize | Integer | 10 | 每页显示的条数，默认为10条，最大100条。 |
| TotalCount | Integer | 100 | 总记录数。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListDataServiceGroups &PageNumber=1 &PageSize=10 &ProjectId=10001 &RegionId=default &TenantId=10003
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <GroupPagingResult>
    <TotalCount>100</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <Groups>
```

`<GroupName>`业务流程名称`</GroupName>`

```xml
        <TenantId>10003</TenantId>
        <CreatedTime>2020-09-24T18:37:51+0800</CreatedTime>
```

`<Description>`业务流程的描述`</Description>`

```xml
        <ModifiedTime>2020-09-24T18:37:51+0800</ModifiedTime>
        <CreatorId>123123123123</CreatorId>
        <ProjectId>10001</ProjectId>
        <ApiGatewayGroupId>100abc</ApiGatewayGroupId>
        <GroupId>ds_123abc</GroupId>
    </Groups>
</GroupPagingResult>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","GroupPagingResult": {"TotalCount":"100","PageSize":"10","PageNumber":"1","Groups":[{"GroupName":"业务流程名称 ","TenantId":"10003","CreatedTime":"2020-09-24T18:37:51+0800","Description":"业务流程的描述","ModifiedTime":"2020-09- 24T18:37:51+0800","CreatorId":"123123123123","ProjectId":"10001","ApiGatewayGroupId":"100 c","GroupId":"ds_123abc"}]}}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

#### PublishDataServiceApi

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | PublishDataServ iceApi | 系统规定参数。取值： PublishDataServiceApi。 |
| ApiId | Long | 是 | 10000 | API的ID。 |
| ProjectId | Long | 是 | 10001 | 工作空间的ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TenantId | Long | 是 | 10002 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 发布是否成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=PublishDataServiceApi &ApiId=10000 &ProjectId=10001 &RegionId=default &TenantId=10002
```

`&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

#### UpdateDataServiceApi

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateDataServ iceApi | 系统规定参数。取值： UpdateDataServiceApi。 |
| ApiDescription | String | 是 | 测试API描述 | API的描述信息。 |
| ApiId | Long | 是 | 10000 | API的ID。 |
| ApiPath | String | 是 | /test/2 | API的路径。 |
| ProjectId | Long | 是 | 10001 | 工作空间的ID。 |
| Protocols | String | 是 | 0,1 | API协议，可选枚举值包括0（HTTP）和 1（HTTPS）。支持多值，多个值之间使用英文逗号（,）分隔。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

DataWorks

| RequestMethod | Integer | 是 | 0 | API的请求方式，可选枚举值包括 0（GET）、1（POST）、2（PUT）和 3（DELTE）。向导和脚本API支持GET和 POST。注册API支持GET、POST、PUT和 DELETE。 |
|---|---|---|---|---|
| ResponseConten tType | Integer | 是 | 0 | API的返回数据类型，可选枚举值包括 0（JSON）和1（XML）。向导和脚本API 支持JSON，注册API支持JSON和XML。 |
| TenantId | Long | 是 | 10001 | 租户ID。 |
| Timeout | Integer | 是 | 10000 | 超时时间，单位为毫秒（ms），取值范围为(0, 30000]。) |
| VisibleRange | Integer | 是 | 0 | 可见范围，可选枚举值包括0（工作空间） 和1（私有）。 |
| WizardDetails | String | 否 | {"isPagedRespo nse":true,"wizar dConnection": {"connectionId": 122786,"tableN ame":"person"}, "wizardRequestP arameters": [{"columnName ":"id","defaultVa lue":"","example Value":"1","isRe quiredParameter ":true,"paramet erDataType":2," parameterDescri ption":"","param eterName":"id"," parameterOpera tor":0,"paramet erPosition":0}]," wizardResponse Parameters": [{"columnName ":"id","exampleV alue":"11","para meterDataType" :2,"parameterDe scription":"","par ameterName":"i d"}]} | 向导API的详情，请参见 GetDataServiceApi接口wizardDetails 字段的JSON String。 |

DataWorks

| ScriptDetails | String | 否 | {"isPagedRespo nse":false,"scrip t":"select id as id1, name as name1 from person where id=${inputid}"," scriptConnection ": {"connectionId": 122786,"tableN ame":"person"}, "scriptRequestP arameters": [{"defaultValue" :"","exampleVal ue":"","isRequire dParameter":tru e,"parameterDat aType":0,"para meterDescriptio n":"","parameter Name":"inputid", "parameterOper ator":0,"parame terPosition":1}], "scriptResponse Parameters": [{"exampleValu e":"","parameter DataType":0,"pa rameterDescript ion":"","paramet erName":"id1"}, {"exampleValue ":"","parameter DataType":0,"pa rameterDescript ion":"","paramet erName":"name 1"}]} | 脚本API的详情，请参见 GetDataServiceApi接口scriptDetails字段的JSON String。 |
|---|---|---|---|---|

DataWorks

| RegistrationDeta ils | String | 否 | {"failedResultSa mple":"fail","regi strationErrorCod es": [{"errorCode":"e 1","errorMessag e":"msg1","error Solution":"sol1" }, {"errorCode":"e 2","errorMessag e":"msg2","error Solution":"sol2" }],"registrationR equestParamete rs": [{"columnName ":"","defaultValu e":"","exampleV alue":"","isRequi redParameter":t rue,"parameter DataType":0,"pa rameterDescript ion":"","paramet erName":"id","p arameterOperat or":0,"paramete rPosition":1}, {"columnName" :"","defaultValue ":"xx","example Value":"","isReq uiredParameter" :true,"parameter DataType":0,"pa rameterDescript ion":"","paramet erName":"cc","p arameterOperat or":2,"paramete rPosition":2}],"s erviceContentTy pe":1,"serviceHo st":"http://www.b aidu.com","servi cePath":"/[uid]"," serviceRequestB odyDescription": "body","successf ulResultSample" :"success"} | 注册API的详情，请参见 GetDataServiceApi接口 registrationDetails字段的JSON String。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 更新API是否成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |

DataWorks

| ErrorMessage | String | The connection does not exist. | 错误信息。 |
|---|---|---|---|
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDataServiceApi
```

`&ApiDescription=`测试`API`描述

```
&ApiId=10000 &ApiPath=/test/2 &ProjectId=10001 &Protocols=0,1 &RegionId=default &RequestMethod=0 &ResponseContentType=0 &TenantId=10001 &Timeout=10000 &VisibleRange=0
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0000-ABCD-EFG****",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": "Invalid.Tenant.ConnectionNotExists",
    "ErrorMessage": "The connection does not exist.",
    "Success": true
}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError.Syste m | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |
| 429 | Throttling.Api | The request for this resource has exceeded your available limit. | 对该资源的请求已超过您的可用上限。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 403 | Forbidden.Access | Access is forbidden. Please first activate DataWorks Enterprise Edition or Flagship Edition. | 您被限制访问，请开通DataWorks 企业版或旗舰版。 |

### 调度

#### CreateManualDag

调用CreateManualDag触发手动业务流程执行。手动业务流程必须已经在界面提交发布，运维中心能够找到对应的手动业务流程，才能使用该接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateManualDa g | 系统规定参数。取值： CreateManualDag。 |
| BizDate | String | 是 | 2020-11-11 00:00:00 | 业务日期的值为小于等于当前日期-1天。 例如，今天是2020年11月11日，则业务日期需要是2020年11月10日的00:00:00 或者该日期之前的日期。业务日期的时分秒信息均填写00。 |
| FlowName | String | 是 | test workflow _ | 手动业务流程的名称。 |

DataWorks

|  |  |  |  | {"20000123121 |  | 传递手动业务流程执行时的节点参数信息，一个JSON格式： { "<手动业务流 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | { "<手动业务流 |  |
|  |  |  |  |  | 0000123121 | 程内部的某个节点ID>": "节点的调度参 |  |  |
|  |  |  |  | ": "key1=val2 key2=val2", | key1=val2 |  |  |  |
|  |  |  |  |  |  | 数信息，和数据开发调度配置里面的参数 |  |  |
| NodeParameters | ters | String | 是 |  |  |  |  |  |
|  |  |  |  | "20000123124": |  | 格式保持一致", "<手动业务流程内部的 |  |  |
|  |  |  |  | "kkkk=vvvvv |  | 某个节点ID>": "节点的调度参数信息， |  |  |
|  |  |  |  | aaaa=bbbb"} |  |  |  |  |
|  |  |  |  |  |  | 和数据开发调度配置里面的参数格式保持 |  |  |
|  |  |  |  |  |  | 一致" } |  |  |
| ProjectEnv |  | String | 是 | PROD |  | 调度运维中心的环境标识。PROD表示生产环境，DEV表示开发环境。 |  |  |
| ProjectName |  | String | 是 | test workspace _ |  | 手动业务流程所属的工作空间英文名称。 |  |  |
| RegionId |  | String | 是 | default |  | 区域ID，为固定值default。 |  |  |
| DagParameters |  | String | 否 | {"kaaaa": "vaaaaa", "kbbbb": "vbbbbb"} |  | 业务流程参数，该参数会同步至本次Dag 的所有实例中。如果内部节点的调度参数引用了DagParameters中的业务流程参数，则节点的对应参数值会被替换为 DagParameter中的业务流程参数。 |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DagId | Long | 700000123121111 | 手动业务流程运行Dag的实例ID。您可以通过接口和该DagId查询此次手动业务流程运行的内部节点实例的详细信息和状态。 |
| RequestId | String | AASFDFSDFG- DFSDF-DFSDFD- SDFSDF | 请求唯一标识。 |

**示例**

请求示例

```
&BizDate=2020-11-11 00:00:00 &FlowName=test_workflow &NodeParameters={"20000123121": "key1=val2 key2=val2", "20000123124": "kkkk=vvvvv aaaa= bbbb"} &ProjectEnv=PROD &ProjectName=test_workspace &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>AASFDFSDFG-DFSDF-DFSDFD-SDFSDF</RequestId> <DagId>700000123121111</DagId>
```

`JSON` 格式

```json
{"RequestId":"AASFDFSDFG-DFSDF-DFSDFD-SDFSDF","DagId":"700000123121111"}
```

#### GetInstanceStatusCount

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetInstanceStat usCount | 系统规定参数。取值： GetInstanceStatusCount。 |
| BizDate | String | 是 | 2020-01-01 | 实例的业务日期。 |
| ProjectEnv | String | 是 | PROD | 运行的环境，包括PROD和DEV。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| StatusCount | Struct |  | 实例的状态统计。 |
| FailureCount | Integer | 1 | 失败实例的数量。 |
| NotRunCount | Integer | 1 | 未运行实例的数量。 |
| RunningCount | Integer | 1 | 运行中实例的数量。 |
| SuccessCount | Integer | 1 | 成功实例的数量。 |

DataWorks

| TotalCount | Integer | 6 | 实例的总数。 |
|---|---|---|---|
| WaitResCount | Integer | 1 | 等待资源实例的数量。 |
| WaitTimeCoun t | Integer | 1 | 满足条件开始等待运行的实例数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetInstanceStatusCount &BizDate=2020-01-01 &ProjectEnv=PROD &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<StatusCount>
    <TotalCount>6</TotalCount>
    <FailureCount>1</FailureCount>
    <RunningCount>1</RunningCount>
    <WaitResCount>1</WaitResCount>
    <SuccessCount>1</SuccessCount>
    <NotRunCount>1</NotRunCount>
    <WaitTimeCount>1</WaitTimeCount>
</StatusCount> <RequestId>0000-ABCD-EFG*****</RequestId>
```

`JSON` 格式

```json
{"StatusCount": {"TotalCount":"6","FailureCount":"1","RunningCount":"1","WaitResCount":"1","SuccessCount" 1","NotRunCount":"1","WaitTimeCount":"1"},"RequestId":"0000-ABCD-EFG*****"}
```

#### GetManualDagInstances

调用GetManualDagInstances，获取手动执行的业务流程实例的信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetManualDagIn stances | 系统规定参数。取值： GetManualDagInstances。 |

DataWorks

| DagId | String | 是 | 7000001231234 | 触发手动业务流程运行的Dag实例ID。您可以调用CreateManualDag接口获取。 |
|---|---|---|---|---|
| ProjectEnv | String | 是 | PROD | 运维中心的调度环境标识，包括 PROD（生产环境）和DEV（开发环境）。 |
| ProjectName | String | 是 | test workspace _ | 手动业务流程所属的工作空间名称。您可以进入DataWorks管控台，在工作空间配置页面获取。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Instances | Array of Instances |  | 手动业务流程的内部实例列表。 |
| BeginRunning Time | Long | 1605178414676 | 实例任务开始运行的时间。 |
| BeginWaitRes Time | Long | 1605178414676 | 实例任务开始等待资源的时间。 |
| BeginWaitTim eTime | Long | 1605178414676 | 实例任务开始等待调度的时间。 |
| BizDate | Long | 1605178414676 | 业务日期。通常为该任务运行时间的前一天。 |
| CreateTime | Long | 1605178414676 | 实例任务的创建时间。 |
| CycTime | Long | 1605178414676 | 实例任务的定时时间。 |
| DagId | Long | 350123123 | 手动业务流程实例的DagId。 |
| DagType | String | 3 | 手动业务流程的类型。 |
| FinishTime | Long | 1605178414676 | 实例任务运行的结束时间。 |
| InstanceId | Long | 11726873619 | 内部实例ID。 |
| ModifyTime | Long | 1605178414676 | 实例任务最新的修改时间。 |

DataWorks

| NodeId | Long | 37851 | 业务流程的内部节点ID。 |
|---|---|---|---|
| NodeName | String | nodename | 节点的名称。 |
| ParamValues | String | xxx | 实例的参数信息。 |
| Status | String | WAIT TIME _ | 实例任务的状态，取值如下： NOT RUN（未运行） _ WAIT TIME（等待定时时间dueTime或 _ cycleTime到来） WAIT RESOURCE（等待资源） _ RUNNING（运行中） CHECKING（下发给数据质量进行数据校检） CHECKING CONDITION（正在进行分支条 _ 件校检） FAILURE（执行失败） SUCC ESS（执行成功） |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetManualDagInstances &DagId=7000001231234 &ProjectEnv=PROD &ProjectName=test_workspace &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<Instances>
    <Status>WAIT_TIME</Status>
    <ModifyTime>1605178414676</ModifyTime>
    <NodeName>nodename</NodeName>
    <DagType>3</DagType>
    <InstanceId>11726873619</InstanceId>
    <ParamValues>xxx</ParamValues>
    <CreateTime>1605178414676</CreateTime>
    <BeginWaitTimeTime>1605178414676</BeginWaitTimeTime>
    <CycTime>1605178414676</CycTime>
    <DagId>350123123</DagId>
    <BeginRunningTime>1605178414676</BeginRunningTime>
    <FinishTime>1605178414676</FinishTime>
    <NodeId>37851</NodeId>
    <BeginWaitResTime>1605178414676</BeginWaitResTime>
    <BizDate>1605178414676</BizDate>
</Instances> <RequestId>0000-ABCD-EFG*****</RequestId>
```

`JSON` 格式

```json
{"Instances": [{"Status":"WAIT_TIME","ModifyTime":"1605178414676","NodeName":"nodename","DagType":"3"," stanceId":"11726873619","ParamValues":"xxx","CreateTime":"1605178414676","BeginWaitTimeTi ":"1605178414676","CycTime":"1605178414676","DagId":"350123123","BeginRunningTime":"16051 414676","FinishTime":"1605178414676","NodeId":"37851","BeginWaitResTime":"1605178414676", izDate":"1605178414676"}],"RequestId":"0000-ABCD-EFG*****"}
```

#### ListProgramTypeCount

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListProgramType Count | 系统规定参数。取值： ListProgramTypeCount。 |
| ProjectEnv | String | 是 | PROD | 工作空间的环境，包括PROD和DEV。 |
| ProjectId | Long | 是 | 10001 | DataWorks工作空间ID。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| ProgramTypeA ndCounts | Array of ProgramTypeA ndCount |  | 节点的类型和数量。 |
|---|---|---|---|
| Count | Integer | 2 | 节点数量。 |
| ProgramType | String | ODPS SQL | 节点的类型。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListProgramTypeCount &ProjectEnv=PROD &ProjectId=10001 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <ProgramTypeAndCounts>
    <Count>2</Count>
    <ProgramType>ODPS SQL</ProgramType>
</ProgramTypeAndCounts>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","ProgramTypeAndCounts": [{"Count":"2","ProgramType":"ODPS SQL"}]}
```

#### SearchNodesByOutput

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SearchNodesBy Output | 系统规定参数。取值： SearchNodesByOutput。 |
| Outputs | String | 是 | aaaaa.1231412 _ out,bbbb.12313 123 out _ | 节点的输出串。支持多个值，多个值时请使用英文逗号（,）分隔。 |

DataWorks

| ProjectEnv | String | 是 | PROD | 调度运维中心环境标识：PROD表示生产环境，DEV表示开发环境。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Map | { "test 0709 1.6300 _ _ 03558 out": { _ "nodeId": 21673, "nodeName": "hour sql", _ "ownerId": 123123123124, "cronExpress": "00 00 00-23/2 * * ?", "repeatability": true, "programType": "ODPS SQL", _ "projectId": 11111, "schedulerType": "NORMAL", "priority": 1, "baselineId": 20001721, "connection": "odps first" }, _ "test 0709 1.6300 _ _ 03556 out": { _ "nodeId": 21671, "nodeName": "start", "ownerId": 123141231231, "cronExpress": "00 */10 00-23 * * ?", "repeatability": true, "programType": "VIRTUAL", "projectId": 1111, "schedulerType": "NORMAL", "priority": 1, "baselineId": 20001721 } } | 返回数据为一个Map，Key是用户输入的每个 output，Value是output对应的节点信息。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。 |
| ErrorMessage | String | The connection does not exist. | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |

DataWorks

| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
|---|---|---|---|
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=SearchNodesByOutput &Outputs=aaaaa.1231412_out,bbbb.12313123_out &ProjectEnv=PROD &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```json
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>{ "test_0709_1.630003558_out": { "nodeId": 21673, "nodeName": "hour_sql", "ownerI d": 123123123124, "cronExpress": "00 00 00-23/2 * * ?", "repeatability": true, "program Type": "ODPS_SQL", "projectId": 11111, "schedulerType": "NORMAL", "priority": 1, "basel ineId": 20001721, "connection": "odps_first" }, "test_0709_1.630003556_out": { "nodeId" : 21671, "nodeName": "start", "ownerId": 123141231231, "cronExpress": "00 */10 00-23 *
* ?", "repeatability": true, "programType": "VIRTUAL", "projectId": 1111,
"schedulerType": "NORMAL", "priority": 1, "baselineId": 20001721 } }</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>false</Success>
```

`JSON` 格式

```json
{"RequestId":"0000-ABCD-EFG*****","HttpStatusCode":"200","Data":"{ \"test_0709_1.630003558_out\": { \"nodeId\": 21673, \"nodeName\": \"hour_sql\", \"owner Id\": 123123123124, \"cronExpress\": \"00 00 00-23/2 * * ?\", \"repeatability\": true, \"programType\": \"ODPS_SQL\", \"projectId\": 11111, \"schedulerType\": \"NORMAL\", \"p riority\": 1, \"baselineId\": 20001721, \"connection\": \"odps_first\" }, \"test_0709_1.630003556_out\": { \"nodeId\": 21671, \"nodeName\": \"start\", \"ownerId\ ": 123141231231, \"cronExpress\": \"00 */10 00-23 * * ?\", \"repeatability\": true, \"p rogramType\": \"VIRTUAL\", \"projectId\": 1111, \"schedulerType\": \"NORMAL\", \"priori ty\": 1, \"baselineId\": 20001721 } }","ErrorCode":"Invalid.Tenant.ConnectionNotExists","ErrorMessage":"The connection does not exist.","Success":"false"}
```

### 数据保护伞

#### AddRuleConfig

DataWorks 新增数据识别规则接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddRuleConfig | 系统规定参数。取值：AddRuleConfig。 |
| Owner | String | 是 | dsg uat _ | 负责人 。 |
| RuleDesc | String | 是 | 手机号规则 | 规则描述。 |
| RuleDetailJson | String | 是 | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRul es": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } | 规则详细Json，RuleDetailJson分为三部分，格式如下示例： { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } 字段取值详情请参见下文的补充说明。 |
| RuleGroup | String | 是 | 自定义规则 | 规则聚类标签。 |
| SensLevel | String | 是 | L1 | 敏感等级。 |

DataWorks

| Status | String | 是 | 0 | 规则生效状态，包括1：生效、0：失效。 |
|---|---|---|---|---|
| Type | String | 是 | 手机号 | 规则名。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 新增成功。 |
| ErrorCode | String | 500 | 错误码。 |
| ErrorMessage | String | InternalError.Unkn own | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| Success | Boolean | false | 调用是否成功。 |

**示例**

请求示例

```
&Owner=dsg_uat
```

`&RuleDesc=`手机号规则

```json
&RuleDetailJson={ "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] }
```

`&RuleGroup=`自定义规则

```
&SensLevel=L1 &Status=0
```

`&Type=`手机号 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>InternalError.Unknown</ErrorMessage> <Success>false</Success>
```

DataWorks `JSON` 格式

```json
{"RequestId":"0000-ABCD- EFG*****","HttpStatusCode":"200","Data":"true","ErrorCode":"500","ErrorMessage":"Internal ror.Unknown","Success":"false"}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

RuleDetailJson分为三部分，如下示例：

```json
{
 "contentRule": {
```

`"dataType": "`座机号`",`

```json
  "regExp": null
 },
 "metaRules": [{
  "compareType": "equal",
  "param": "a.b.c",
  "metaType": "guid",
 }],
 "excludeMetaRules": [{
  "compareType": "equal",
  "param": "c.d.e",
  "metaType": "guid",
 }]
}
```

其中：
**ContentRule**：为内容识别规则，与MetaRules二选一。
DataWorks ContentRule包含**规则名**和**规则内容**，规则名可以是内置规则名、正则表达式、自生成识别模型名、样本库名；当规则名为正则式匹配时，规则内容则传递正则内容。
**metaRules**：为字段扫描规则，与ContentRule二选一。
metaRules包含**规则名**和**规则内容**，规则名为固定值，通过元数据识别；规则内容包含**compareType**、**param**、**metaType**。
**compareType**：比较类型，取值为固定值：**equal**或**regexp**。如果param包含 *, 传**regexp**, 否
则传**equal**。
**param**：字段扫描内容，可使用通配符
，格式为 `project.table.column` ；例如，a.b.c 表示匹配project为a ，表名称为b的c列字段；a.b. 表示匹配a的project中b表的任意列字段。
**metaType**：元数据匹配类型，取值为固定值guid。
**excludeMetaRules**：字段扫描排除项；非必填。包含**规则名**和**规则内容**，取值与**metaRules**的规
**则名**和**规则内容**一致。

#### AddRuleConfigMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddRuleConfigM essage | 系统规定参数。取值： AddRuleConfigMessage。 |
| Owner | String | 是 | uat | 负责人 。入参配置此参数时，需同步配置指定Type（规则名称）参数。 |
| RuleDesc | String | 是 | 手机号规则 | 规则描述。 |
|  |  |  |  | 规则详细Json，RuleDetailJson分为三部分，如下示例： |

DataWorks

|  |  |  |  | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ |
|---|---|---|---|---|
| RuleDetailJson | String | 是 | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRul es": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } | "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } 其中： ContentRule：为内容识别规则，与 MetaRules二选一 。 ContentRule包含规则名和规则内容， 规则名可以是内置规则名、正则表达式、自生成识别模型名、样本库名；当规则名为正则式匹配时， 规则内容则传递正则内容。 metaRules：为字段扫描规则，与 ContentRule二选一。 metaRules包含规则名和规则内容，规则名为固定值，通过元数据识别；规则内容包含compareType、param、meta Type。 compareType：比较类型，取值为固定值：equal或regexp。如果 param包含 *, 传regexp, 否则传equal。 param：字段扫描内容，可使用通配符 ，格式为 project.table.column ； 例如 ，a.b.c 表示匹配project为a ，表名称为b的c列字段；a.b. 表示匹配a的project中b表的任意列字段。 metaType：元数据匹配类型，取值为固定值guid。 excludeMetaRules：字段扫描排除项 ；非必填。包含规则名和规则内容， 取值与metaRules的规则名和规则内 |
| RuleGroup | String | 是 | 自定义规则 | 容一致。 规则聚类标签。 |

DataWorks

| SensLevel | String | 是 | L1 | 敏感等级。 |
|---|---|---|---|---|
| Status | String | 是 | 0 | 规则生效状态，包含生效、失效。 |
| TenantId | String | 是 | 5414453514757 45 | 租户ID。 |
| Type | String | 是 | 手机号 | 规则名 ，入参配置此参数时，需同步配置指定Owner（负责人）参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 新增结果。 true：新增成功。 false：新增失败。 |
| ErrorCode | String | 40001 | 错误码。 |
| ErrorMessage | String | 错误异常 | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddRuleConfigMessage &Owner=uat
```

`&RuleDesc=`手机号规则

```json
&RuleDetailJson={ "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] }
```

`&RuleGroup=`自定义规则

```
&SensLevel=L1 &Status=0 &TenantId=541445351475745
```

`&Type=`手机号 `&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <Data>true</Data> <ErrorCode>40001</ErrorCode> <ErrorMessage>错误异常</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "Data": true,
    "ErrorCode": 40001,
```

`"ErrorMessage": "`错误异常`",`

```json
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### UpdateRuleConfig

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | UpdateRuleConfi g | 系统规定参数。取值： UpdateRuleConfig。 |
|---|---|---|---|---|
| Id | Long | 是 | 1 | ID。 |
| Owner | String | 是 | uat | 账号名称。 |
| RuleDesc | String | 是 | 手机号规则 | 规则描述。 |
| RuleDetailJson | String | 是 | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRul es": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } | 规则详细Json，RuleDetailJson分为三部分，如下示例： { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } 其中： ContentRule：为内容识别规则，与 MetaRules二选一 。 ContentRule包含规则名和规则内容， 规则名可以是内置规则名、正则表达式、自生成识别模型名、样本库名；当规则名为正则式匹配时， 规则内容则传递正则内容。 metaRules：为字段扫描规则，与 ContentRule二选一。 metaRules包含规则名和规则内容，规则名为固定值，通过元数据识别；规则内容包含compareType、param、meta Type。 compareType：比较类型，取值为固定值：equal或regexp。如果 param包含 *, 取值regexp, 否则取值equal。 |

DataWorks

|  |  |  |  | param：字段扫描内容，可使用通配符 * ，格式为 project.table.column ； 例如 ， a.b.c 表示匹配project 为a ，表名称为b的c列字段； a.b.* 表示匹配a的project 中b表的任意列字段。 metaType：元数据匹配类型，取值为固定值guid。 excludeMetaRules：字段扫描排除项 ；非必填。包含规则名和规则内容， 取值与metaRules的规则名和规则内容一致 |
|---|---|---|---|---|
| RuleGroup | String | 是 | 正则规则 | 规则聚类标签。 |
| SensLevel | String | 是 | L1 | 规则等级。 |
| Status | String | 是 | 0 | 规则生效状态，包含生效、失效。 |
|  |  |  |  | 规则名 ，入参配置此参数时，需同步配置 |
| Type | String | 是 | 手机号 | 指定Owner（负责人）参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 更新结果。 |
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit. | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |

DataWorks

| Success | Boolean | true | 请求是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
&Id=1 &Owner=uat
```

`&RuleDesc=`手机号规则

```json
&RuleDetailJson={ "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] }
```

`&RuleGroup=`正则规则

```
&SensLevel=L1 &Status=0
```

`&Type=`手机号 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <Data>true</Data> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit.</E rrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "Data": true,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |

DataWorks

| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
|---|---|---|---|
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### UpdateRuleConfigMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateRuleConfi gMessage | 系统规定参数。取值： UpdateRuleConfigMessage。 |
| Id | Long | 是 | 1 | ID。 |
| Owner | String | 是 | uat | 账号。 |
| RuleDesc | String | 是 | 手机号规则 | 手机号规则。 |
|  |  |  |  | 规则详细Json，RuleDetailJson分为三部分，如下示例： |

DataWorks

|  |  |  | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ | { "contentRule": { "dataType": "座机号", "regExp": null }, |
|---|---|---|---|---|
| RuleDetailJson | String | 是 | "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRul es": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } | "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } 其中： ContentRule：为内容识别规则，与 MetaRules二选一 。 ContentRule包含规则名和规则内容， 规则名可以是内置规则名、正则表达式、自生成识别模型名、样本库名；当规则名为正则式匹配时， 规则内容则传递正则内容。 metaRules：为字段扫描规则，与 ContentRule二选一。 metaRules包含规则名和规则内容，规则名为固定值，通过元数据识别；规则内容包含compareType、param、meta Type。 compareType：比较类型，取值为固定值：equal或regexp。如果 param包含 *, 取值regexp, 否则取值equal。 |
| RuleGroup | String | 是 | 正则规则 | param：字段扫描内容，可使用通规则聚配类符标签* 。，格式为 project.table.column ； |
| SensLevel | String | 是 | L1 | 例如 ， a.b.c 表示匹配project 规则等级。 为a，表名称为b的c列字段； a.b.* 表示匹配a的project |
| Status | String | 是 | 0 | 中b表的任意列字段。 规则生效状态，包含生效、失效 metaType：元数据匹配类型，取值为固定值guid。 |
| TenantId | String | 是 | 5414453514757 45 | 租户exIDc。ludeMetaRules：字段扫描排除项 ；非必填。包含规则名和规则内容， |
| Type | String | 是 | 手机号 | 取值与metaRules的规则名和规则内容一致。 规则名称。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 更新结果。 |
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateRuleConfigMessage &Id=1 &Owner=uat
```

`&RuleDesc=`手机号规则

```json
&RuleDetailJson={ "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] }
```

`&RuleGroup=`正则规则

```
&SensLevel=L1 &Status=0 &TenantId=541445351475745
```

`&Type=`手机号 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <Data>true</Data> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "Data": true,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### DeleteRuleConfig

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRuleConfi g | 系统规定参数。取值： DeleteRuleConfig。 |
| Id | Long | 是 | 1 | 规则ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

DataWorks

| Data | Boolean | true | 删除结果。 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit. | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
&Id=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <Data>true</Data> <ErrorCode>9990040002</ErrorCode> <ErrorMessage> The request for this resource has exceeded your daily available limit.< /ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "Data": true,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit.",
    "Success": true
}
```

**错误码**

DataWorks

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### DeleteRuleConfigMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRuleConfi gMessage | 系统规定参数。取值： DeleteRuleConfigMessage。 |
| Id | Long | 是 | 1 | 规则ID。 |
| TenantId | String | 是 | 5414453514757 45 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 删除结果。 |
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit. | 错误信息。 |

DataWorks

| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
|---|---|---|---|
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteRuleConfigMessage &Id=1 &TenantId=541445351475745
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <Data>true</Data> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit.</E rrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "Data": true,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |

DataWorks

| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
|---|---|---|---|
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### DesensitizeData

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DesensitizeData | 系统规定参数。取值： DesensitizeData。 |
| Data | String | 是 | 15365291784 | 输入的待脱敏数据。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| SceneCode | String | 是 | default scene _ _ _ code | 脱敏场景码。您可以进入DataWorks管控台的数据保护伞，在数据脱敏管理页面查看 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DesensitizeDat a | String | { "desensData": "**198807120510* *" } | 脱敏后的结果数据。 |
| RequestId | String | BCA321BA-46C5- 40E9-8A08-6****** | 请求ID，一次请求的唯一标识。 |

**示例**

请求示例

```
&Data=15365291784 &RegionId=default &SceneCode=_default_scene_code
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>BCA321BA-46C5-40E9-8A08-6****** </RequestId> <DesensitizeData>{ "desensData": "**198807120510**" }</DesensitizeData>
```

`JSON` 格式

```json
{
    "RequestId": "BCA321BA-46C5-40E9-8A08-6******",
    "DesensitizeData": "{ \"desensData\": \"**198807120510**\" }"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.NoTenan t | The tenant information cannot be obtained using user ID. | 无法获取租户的信息。 |
| 500 | InternalError.DQC. BizError | An internal error occurred. | 内部服务错误。 |

#### GetRuleConfig

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRuleConfig | 系统规定参数。取值：GetRuleConfig。 |
| Id | Long | 是 | 1 | 规则ID。 |
| Owner | String | 是 | uat | 账户名称。 |
| RuleDesc | String | 是 | 手机号规则 | 规则描述。 |

DataWorks

| RuleDetailJson | String | 是 | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRul es": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } | 规则详细Json，RuleDetailJson分为三部分，如下示例： { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } 其中： ContentRule：为内容识别规则，与 MetaRules二选一 。 ContentRule包含规则名和规则内容， 规则名可以是内置规则名、正则表达式、自生成识别模型名、样本库名；当规则名为正则式匹配时， 规则内容则传递正则内容。 metaRules：为字段扫描规则，与 ContentRule二选一。 metaRules包含规则名和规则内容，规则名为固定值，通过元数据识别；规则内容包含compareType、param、meta Type。 compareType：比较类型，取值为固定值：equal或regexp。如果 param包含 *, 取值regexp, 否则取值equal。 param：字段扫描内容，可使用通配符 * ，格式为 project.table.column ； 例如 ， a.b.c 表示匹配project 为a ，表名称为b的c列字段； a.b.* 表示匹配a的project 中b表的任意列字段。 metaType：元数据匹配类型，取值为固定值guid。 excludeMetaRules：字段扫描排除项 ；非必填。包含规则名和规则内容， 取值与metaRules的规则名和规则内容一致。 |
|---|---|---|---|---|

DataWorks

| RuleGroup | String | 是 | 分类 | 规则聚类标签。 |
|---|---|---|---|---|
| SensLevel | String | 是 | L2 | 规则等级。 |
| Status | String | 是 | 0 | 规则生效状态，包含生效、失效。 |
| Type | String | 是 | 手机号 | 规则名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 返回结果 |
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。用于出现错误后排查问题。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&Id=1 &Owner=uat
```

`&RuleDesc=`手机号规则

```json
&RuleDetailJson={ "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] }
```

`&RuleGroup=`分类

```
&SensLevel=L2 &Status=0
```

`&Type=`手机号 `&<`公共请求参数> 正常返回示例 DataWorks `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <Data>true</Data> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "Data": true,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetRuleConfigMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetRuleConfigM essage | 系统规定参数。取值： GetRuleConfigMessage。 |
|---|---|---|---|---|
| PageNum | Integer | 是 | 1 | 请求的数据页数，用于翻页。 |
| TenantId | String | 是 | 5414453514757 45 | 租户ID。 |
| Type | String | 否 | 手机号 | 规则名称。 |
| Status | String | 否 | 0 | 规则生效状态，包含生效、失效。 |
| Owner | String | 否 | uat | 账号名称。 |
| PageSize | Integer | 否 | 10 | 分页字段，每页显示的数据条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。用于出现错误后排查问题。 |
| RuleConifgDat a | Struct |  | 返回结果。 |
| Rules | Array of SensList |  | 规则列表。 |
| BydAccuracy | Float | 80 | 前天的准确率。 |
| CreateTime | Long | 1546504580000 | 创建时间。 |
| IsCustom | Boolean | true | 是否是自定义类型。 |
| LocaleType | String | 手机号 | 国际化名称。 |

DataWorks

| Owner | String | uat | 操作账号。 |
|---|---|---|---|
| RuleDesc | String | 手机号规则 | 规则介绍。 |
| RuleDetailJson | String | { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules ": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } | 规则详细Json，RuleDetailJson分为三部分，如下示例： { "contentRule": { "dataType": "座机号", "regExp": null }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] } 其中： ContentRule：为内容识别规则，与 MetaRules二选一 。 ContentRule包含规则名和规则内容，规则名可以是内置规则名、正则表达式、自生成识别模型名、样本库名；当规则名为正则式匹配时， 规则内容则传递正则内容。 metaRules：为字段扫描规则，与 ContentRule二选一。 metaRules包含规则名和规则内容，规则名为固定值，通过元数据识别；规则内容包含compareType、param、metaType 。 compareType：比较类型，取值为固定值：equal或regexp。如果param包含 *, 取值regexp, 否则取值equal。 param：字段扫描内容，可使用通配符 * ，格式为 project.table.column ； 例如 ， a.b.c 表示匹配project为a ，表名称为b的c列字段； a.b.* 表示匹配a的 project中b表的任意列字段。 metaType：元数据匹配类型，取值为固定值guid。 excludeMetaRules：字段扫描排除项 ； 非必填。包含规则名和规则内容，取值 |

DataWorks

|  |  |  | 与metaRules的规则名和规则内容一致。 |
|---|---|---|---|
| RuleGroup | String | 内置规则 | 聚类tag，标签。 |
| UpdateTime | Long | 1664159839646 | 更新时间。 |
| YdAccuracy | Float | 100 | 昨天的准确率。 |
| TotalCount | Integer | 100 | 规则总数。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetRuleConfigMessage &PageNum=1 &TenantId=541445351475745
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```json
<RequestId>0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <RuleConifgData>
    <TotalCount>100</TotalCount>
    <Rules>
        <Owner>uat</Owner>
        <RuleDetailJson>{  "contentRule": {   "dataType": "座机号",   "regExp": null  },
"metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", }], "excludeMetaRules": [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", }] }</RuleDetailJson>
        <BydAccuracy>80</BydAccuracy>
        <IsCustom>true</IsCustom>
        <CreateTime>1546504580000</CreateTime>
        <UpdateTime>1664159839646</UpdateTime>
```

`<RuleDesc>`手机号规则`</RuleDesc>`

```xml
        <LocaleType>手机号</LocaleType>
        <YdAccuracy>100</YdAccuracy>
        <RuleGroup>内置规则</RuleGroup>
    </Rules>
</RuleConifgData> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "RuleConifgData": {
        "TotalCount": 100,
        "Rules": {
            "Owner": "uat",
            "RuleDetailJson": "{  \"contentRule\": {  \t\"dataType\": \"座机号\",  \t\"re
gExp\": null }, \"metaRules\": [{ \t\"compareType\": \"equal\", \t\"param\": \"a.b.c\", \t\"metaType\": \"guid\", }], \"excludeMetaRules\": [{ \t\"compareType\": \"equal\", \t\"param\": \"c.d.e\", \t\"metaType\": \"guid\", }] }
```

`",`

```json
            "BydAccuracy": 80,
            "IsCustom": true,
            "CreateTime": 1546504580000,
            "UpdateTime": 1664159839646,
```

`"RuleDesc": "`手机号规则`",`

```json
            "LocaleType": "手机号",
            "YdAccuracy": 100,
```

`"RuleGroup": "`内置规则"

```json
        }
    },
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

#### GetRuleDataMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRuleDataMes sage | 系统规定参数。取值： GetRuleDataMessage。 |
| TenantId | String | 是 | 5414453514757 45 | 租户ID。 |
| Type | String | 否 | 手机号 | 规则名称。 |
| SensLevelAlias | String | 否 | 机密 | 等级名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| LevelRuleData | Struct |  | 分级信息。 |
| LevelRuleList | Array of LevelRuleList |  | 敏感分级列表。 |
| OpAccount | String | uat | 账号。 |
| SensLevel | String | L1 | 分级信息。 |
| SensLevelAlias | String | 机密 | 分级名称。 |
| Type | String | 邮箱 | 规则类型。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |

DataWorks

| Success | Boolean | true | 调用是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetRuleDataMessage &TenantId=541445351475745
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <LevelRuleData>
    <LevelRuleList>
        <OpAccount>uat</OpAccount>
        <Type>邮箱</Type>
        <SensLevelAlias>机密</SensLevelAlias>
        <SensLevel>L1</SensLevel>
    </LevelRuleList>
</LevelRuleData> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "LevelRuleData": {
        "LevelRuleList": {
            "OpAccount": "uat",
```

`"Type": "`邮箱`",`

```json
            "SensLevelAlias": "机密",
            "SensLevel": "L1"
        }
    },
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

| 开发指南·Open | API参考 |  | DataWork |
|---|---|---|---|

| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
|---|---|---|---|
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetRuleMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRuleMessage | 系统规定参数。取值： GetRuleMessage。 |
| Type | String | 否 | 手机号 | 规则名称。 |
| SensLevelAlias | String | 否 | 机密 | 规则等级名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |

DataWorks

| LevelRuleData | Struct |  | 返回结果。 |
|---|---|---|---|
| LevelRuleList | Array of LevelRuleList |  | 返回结果列表。 |
| OpAccount | String | uat | 账号信息。 |
| SensLevel | String | L1 | 等级。 |
| SensLevelAlias | String | 机密 | 等级名称。 |
| Type | String | 手机号 | 规则名称。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <LevelRuleData>
    <LevelRuleList>
        <OpAccount>uat</OpAccount>
```

`<Type>`手机号`</Type>`

```xml
        <SensLevelAlias>机密</SensLevelAlias>
        <SensLevel>L1</SensLevel>
    </LevelRuleList>
</LevelRuleData> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "LevelRuleData": {
        "LevelRuleList": {
            "OpAccount": "uat",
```

`"Type": "`手机号`",`

```json
            "SensLevelAlias": "机密",
            "SensLevel": "L1"
        }
    },
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetSensLevel

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetSensLevel | 系统规定参数。取值：GetSensLevel。 |

**返回数据**

DataWorks

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limi | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| SensLevelData | Struct |  | 返回结果。 |
| SensList | Array of SensList |  | 返回列表。 |
| Count | Integer | 1 | 结果统计。 |
| OpAccount | String | uat | 操作人员账户。 |
| OpTime | Long | 1664159839646 | 操作时间。 |
| SensLevel | String | L1 | 等级。 |
| SensLevelAlias | String | 机密 | 等级名称。 |
| Success | Boolean | true | 请求结果。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<SensLevelData>
    <SensList>
        <OpAccount>uat</OpAccount>
        <SensLevelAlias>机密</SensLevelAlias>
        <Count>1</Count>
        <SensLevel>L1</SensLevel>
        <OpTime>1664159839646</OpTime>
    </SensList>
</SensLevelData> <RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limi</Err orMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "SensLevelData": {
        "SensList": {
            "OpAccount": "uat",
            "SensLevelAlias": "机密",
            "Count": 1,
            "SensLevel": "L1",
            "OpTime": 1664159839646
        }
    },
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mi",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |

DataWorks

| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
|---|---|---|---|
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetSensLevelMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetSensLevelMe ssage | 系统规定参数。取值： GetSensLevelMessage。 |
| TenantId | String | 是 | 5414453514757 45 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 请求ID。 |
| SensLevelData | Struct |  | 返回结果。 |
| SensList | Array of SensList |  | 返回结果列表。 |
| Count | Integer | 1 | 统计。 |
| OpAccount | String | uat | 账号信息。 |
| OpTime | Long | 1664159839646 | 操作时间。 |

DataWorks

| SensLevel | String | L1 | 敏感等级。 |
|---|---|---|---|
| SensLevelAlias | String | 机密 | 敏感等级名称。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetSensLevelMessage &TenantId=541445351475745
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SensLevelData>
    <SensList>
        <OpAccount>uat</OpAccount>
        <SensLevelAlias>机密</SensLevelAlias>
        <Count>1</Count>
        <SensLevel>L1</SensLevel>
        <OpTime>1664159839646</OpTime>
    </SensList>
</SensLevelData> <RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式 DataWorks

```json
{
    "SensLevelData": {
        "SensList": {
            "OpAccount": "uat",
            "SensLevelAlias": "机密",
            "Count": 1,
            "SensLevel": "L1",
            "OpTime": 1664159839646
        }
    },
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetSensTableLevel

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

DataWorks

| Action | String | 是 | GetSensTableLe vel | 系统规定参数。取值： GetSensTableLevel。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit. | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |
| sensTableList | Array of SensTableList |  | 敏感结果。 |
| OpAccount | String | uat | 账户名称。 |
| SensLevelNam e | String | 机密 | 等级名称。 |
| SensTables | String | tables | 敏感表信息。 |
| Status | String | 0 | 敏感结果生效状态生效或者不生效。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <sensTableList>
    <Status>0</Status>
    <OpAccount>uat</OpAccount>
    <SensLevelName>机密</SensLevelName>
    <SensTables>tables</SensTables>
</sensTableList> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit.</E rrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "sensTableList": {
        "Status": 0,
        "OpAccount": "uat",
        "SensLevelName": "机密",
        "SensTables": "tables"
    },
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit.",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |
| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

DataWorks

#### GetSensTableLevelMessage

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetSensTableLe velMessage | 系统规定参数。取值： GetSensTableLevelMessage。 |
| TenantId | String | 是 | 5414453514757 45 | 租户ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ErrorCode | String | 9990040002 | 错误码。 |
| ErrorMessage | String | The request for this resource has exceeded your daily available limit | 错误信息。 |
| HttpStatusCod e | Integer | 429 | HTTP状态码。 |
| RequestId | String | 0a0a07e31663921 4411658883ecd10 | 本次调用的唯一ID。出现错误后，您可以根据该 ID排查问题。 |
| Success | Boolean | true | 调用是否成功。 |
| sensTableList | Array of SensTableList |  | 表安全分级列表。 |
| OpAccount | String | uat | 操作人。 |
| SensLevelNam e | String | 机密 | 安全等级名称。 |
| SensTables | String | tables | 指定表字段。 |
| Status | String | 0 | 状态。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=GetSensTableLevelMessage &TenantId=541445351475745
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId> 0a0a07e316639214411658883ecd10</RequestId> <HttpStatusCode>429</HttpStatusCode> <sensTableList>
    <Status>0</Status>
    <OpAccount>uat</OpAccount>
    <SensLevelName>机密</SensLevelName>
    <SensTables>tables</SensTables>
</sensTableList> <ErrorCode>9990040002</ErrorCode> <ErrorMessage>The request for this resource has exceeded your daily available limit</Er rorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "0a0a07e316639214411658883ecd10",
    "HttpStatusCode": 429,
    "sensTableList": {
        "Status": 0,
        "OpAccount": "uat",
        "SensLevelName": "机密",
        "SensTables": "tables"
    },
    "ErrorCode": 9990040002,
    "ErrorMessage": "The request for this resource has exceeded your daily available li
mit",
    "Success": true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. | 对该资源的请求已超过您的每日可用上限。 |
| 429 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. | 该资源已经达到您的使用上限，请提交工单进行咨询。 |
| 429 | Throttling.System | The DataWorks system is busy. Try again later. | DataWorks系统繁忙，请稍后再试。 |

DataWorks

| 429 | Throttling.User | Your request is too frequent. Try again later. | 您的请求过于频繁，请尝试放缓请求速度。 |
|---|---|---|---|
| 500 | Forbidden.Not.Serv er | The dataworksAPI service is not available in this area. Please try it in another area. | 该地域还未开放DataWorks的API 服务，请尝试其它地域。 |
| 500 | InternalError.UserId .Missing | An internal system error occurred. Try again later. | 系统内部错误，请稍后再试。 |

#### GetOpSensitiveData

调用GetOpSensitiveData接口，获取租户下所有DataWorks工作空间指定日期的敏感数据访问记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| Name | Strin g | Query | 是 | [ {"dbType":"hologres","in stanceName":"ABC","dat abaseName":"abc"}, {"dbType":"ODPS.ODPS" ,"projectName":"adbc"} ] | 获取访问记录的条件设置。 可选的参数如下： dbType：数据类型。 instanceName：实例名称。 databaseName：数据库名称。 projectName：项目名称。 clusterName：集群名称。 示例获取Hologres中ABC 实例的abc数据库的敏感数据访问记录： [ {"dbType":"hologres","i nstanceName":"ABC","d atabaseName":"abc"} ] 实际使用时，您需要根据业务使用的引擎进行配置。 |
| PageSize | Integ er | Query | 是 | 1 | 每页展示的数据量，最小值为1，最大值为1000。 |
| PageNo | Integ er | Query | 是 | 100 | 页码数。最小值为1，最大值为1000。 |

| DataWorks |  |  |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Date | Strin g | Query | 是 | 20210116 | 获取访问记录的日期。格式为：yyyyMMdd。 |
| OpType | Strin g | Query | 否 | SQL SELECT _ | 用户对数据的操作类型。取值如下： SQL SELECT，访问行 _ 为。例如，使用SELECT 查询数据。 TUNNEL DOWNLOAD _ ，导出行为。例如，下载数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| OpSensitiveDa ta | String | "opSensDatas": [ { "sensLevel": "L4", "opTime": "2021- 02-07 00:14:51", "opAccount": "ALIYUN$dsg test", _ "sensType": "手机号", "sql": "select * from dsg demo.tbl phon _ _ ebook where phone no = _ '1331111****';" } ], "totalCount": 6 | 返回的敏感数据记录信息。包括totalCount（敏感数据总条数）和opRiskDatas（风险数据列表）。 其中opRiskDatas（风险数据列表）包括： sensType：敏感类型。 sensLevel：敏感级别（数字越大表示敏感程度越高）。 opType：操作类型。 sql：操作执行的sql语句。 opAccount：执行操作的账号。 opTime：执行操作的时间。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=GetOpSensitiveData &RegionId=default &Name=[ {"dbType":"hologres","instanceName":"ABC","databaseName":"abc"}, {"dbType":"ODPS.ODPS","projectName":"adbc"} ] &PageSize=1 &PageNo=100 &Date=20210116
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "OpSensitiveData":"\"opSensDatas\": [       {         \"sensLevel\": \"L4\",         \"
opTime\": \"2021-02-07 00:14:51\", \"opAccount\": \"ALIYUN$dsg_test\", \ "sensType\": \"手机号\", \"sql\": \"select * from dsg_demo.tbl_phonebook where p hone_no = &#39;1331111****&#39;;\" } ], \"totalCount\": 6" }
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <OpSensitiveData>&quot;opSensDatas&quot;: [ { &quot;sensLevel&quot;: &quot ;L4&quot;, &quot;opTime&quot;: &quot;2021-02-07 00:14:51&quot;, &quot;op Account&quot;: &quot;ALIYUN$dsg_test&quot;, &quot;sensType&quot;: &quot;手机号&q uot;, &quot;sql&quot;: &quot;select * from dsg_demo.tbl_phonebook where phone_no = &amp;#39;1331111****&amp;#39;;&quot; } ], &quot;totalCount&quot;: 6</OpSensitiveData>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | 1010010016 | Invalid.Param | The request parameter is invalid. |
| 403 | 1010010014 | Forbidden.NoTenant | The tenant information cannot be obtained using user ID. |
| 500 | 100000500 | InternalError.DQC.BizError | An internal error occurred. |

**文档补充说明**

访问错误中心查看更多错误码。

#### GetSensitiveData

调用GetSensitiveData，获取租户下所有DataWorks工作空间的最新敏感数据识别结果。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | 是 | 10 | 每页返回的数据量，最大值为1000。 |
| PageNo | Integ er | Query | 是 | 1 | 页码数，最小值为1。 |

| DataWorks |  |  |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| Name | Strin g | Query | 是 | [ {"dbType":"hologres","in stanceName":"ABC","dat abaseName":"abc"}, {"dbType":"odps","proje ctName":"adbc"} ] | 获取访问记录的条件设置。 可选的参数如下： dbType：数据类型。 instanceName：实例名称。 databaseName：数据库名称。 projectName：项目名称。 clusterName：集群名称。 示例获取Hologres中ABC 实例的abc数据库的敏感数据访问记录： {"dbType":"hologres","i nstanceName":"ABC","d atabaseName":"abc"} 实际使用时，您需要根据业务使用的引擎进行配置。 |

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| TenantId | String | 是 | 111111 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG***** | 请求ID。 |
| SensitiveData | Map | { "sensDatas": [ { "sensLevel": "L1", "guid": "dsg demo.animal. _ dog", "sensType": "姓名" } ], "totalCount": 2171 } | 返回的敏感数据信息。包括totalCount（敏感数据总条数）和sensDatas（敏感数据列表）。 其中sensDatas（敏感数据列表）包括： guid：租户元数据的唯一id，例如 ODPS.ODPS类型数据的guid由 project.table.column组成。 sensType：敏感类型。 sensLevel：敏感级别。 |

**示例**

请求示例 DataWorks

```json
&PageSize=10 &PageNo=1 &RegionId=default &Name=[ {"dbType":"hologres","instanceName":"ABC","databaseName":"abc"}, {"dbType":"odps","projectName":"adbc"} ] &TenantId=111111
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG*****",
 "SensitiveData":{
  "sensDatas":[
   {
    "sensLevel":"L1",
    "guid":"dsg_demo.animal.dog",
    "sensType":"姓名"
   }
```

`],`

```json
  "totalCount":2171
 }
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG*****</RequestId> <SensitiveData>
 <sensDatas>
  <sensLevel>L1</sensLevel>
  <guid>dsg_demo.animal.dog</guid>
  <sensType>姓名</sensType>
 </sensDatas>
 <totalCount>2171</totalCount>
</SensitiveData>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 1010010014 | Forbidden.NoTenant | The tenant information cannot be obtained using user ID. |
| 500 | 100000500 | InternalError.DQC.BizError | An internal error occurred. |
| 400 | 1010010016 | Invalid.Param | The request parameter is invalid. |

DataWorks

#### ScanSensitiveData

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ScanSensitiveDa ta | 系统规定参数。取值： ScanSensitiveData。 |
| Data | String | 是 | 13900001234 | 待识别的数据。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求ID，一次请求的唯一标识。 |
| Sensitives | Map | sensDatas | 识别出的敏感数据信息。 sensDatas表示识别出的敏感数据规则列表，包括： hitCount：命中率，该数据命中规则的次数。 ruleName：规则名称 |

**示例**

请求示例

```
&Data=13900001234 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Sensitives>sensDatas</Sensitives> <RequestId>0000-ABCD-EFG****</RequestId>
```

`JSON` 格式 DataWorks

```json
{
    "Sensitives": "sensDatas",
    "RequestId": "0000-ABCD-EFG****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | Forbidden.Meta.No Tenant | The user is not the owner of any tenants. | 当前的用户不是任何租户的所有者。 |
| 500 | InternalError.DQC. BizError | An internal error occurred. | 内部服务错误。 |

#### AddSenRule

该接口用于在DataWorks中创建并配置新的数据识别规则。 该接口不支持新增自生成和样本库规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| HitThresh old | Strin g | Query | 是 | 50 | 命中阈值。若抽样数据中， 超过阈值百分比（例如，60%）的数据命中NER 模型，则认为命中该敏感字段。取值：0~100之间的整数。 |
| Type | Strin g | Query | 是 | 手机号 | 规则名 ，入参配置此参数时，需同步配置指定Owner （负责人）参数。 |
| Status | Strin g | Query | 是 | 1 | 规则的生效状态。 枚举值: 0(失效) 1(生效) |
| Owner | Strin g | Query | 是 | 193379**** | 负责人 ，入参配置此参数时，需同步配置指定Type （规则名称）参数。 |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RuleDesc | Strin g | Query | 否 | 手机号规则 | 规则描述。 |
| RuleDetail Json | Strin g | Query | 是 | { "contentTemplates": [{ "name": "正则式匹配", "localeName": "正则式匹配", "templateJsonStr": " {\" clazz\":\"com.alipay. _ dsgclient.sdk.dsg.fastsca n.engine.cond.RegExpCo ndition\"}", "regex": null, "uuid": null, "desc": "", "custom": false }] } | 规则详细 Json，RuleDetailJson分为三部分，如下示例： { "contentRule": { "dataType": "银行卡号", "regExp": null， " clazz":"com.alip _ ay.dsgclient.sdk.d sg.fastscan.engine .cond.BankCardCond " }, "metaRules": [{ "compareType": "equal", "param": "a.b.c", "metaType": "guid", " clazz":"com.alip _ ay.dsgclient.sdk.d sg.fastscan.engine .cond.DftMetaCond" }], "excludeMetaRules" : [{ "compareType": "equal", "param": "c.d.e", "metaType": "guid", " clazz":"com.alip _ ay.dsgclient.sdk.d sg.fastscan.engine .cond.DftMetaCond" }] } |

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SensLevel | Strin g | Query | 是 | Critical | 表示敏感级别。 |
| RuleGroup | Strin g | Query | 是 | test | 用于数据处理流程的规则集合，如数据清洗、格式转换、聚合计算等。 |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |
| NodeId | Strin g | Query | 是 | 1234 | 节点ID。 |

| DataWorks |  |  |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NodePare nt | Strin g | Query | 是 | 客户/个人/个人自然信息/个人基本概况信息 | 分类结点的父结点信息。 |
| Recognize RulesType | Integ er | Query | 是 | 1 | 敏感数据识别规则类型。 枚举值: 1(正则) 2(内置) 3(样本库) 4(自生成模型) |

RuleDetailJson详细说明： ：为内容识别规则，与MetaRules二选一。 ContentRule包含**规则名** 和**规则内**

**ContentRule**

，规则名可以是内置规则名、正则表达式、当规则名为正则式匹配时，规则内容则传递正则内容。

**容**

：为字段扫描规则，与ContentRule二选一。 metaRules包含**规则名** 和**规则内容** ，

**metaRules**

规则名为固定值，通过元数据识别；规则内容包含**compareType** 、**param** 、**metaType** 。 ：比较类型，取值为固定值：**equal** 或**regexp** 。如果param包含 *,

**compareType**

传**regexp** , 否则传**equal** 。 ：字段扫描内容，可使用通配符* ，格式为 `project.table.column` ；例如，a.b.c 表示

**param**

匹配project为a ，表名称为b的c列字段；a.b.* 表示匹配a的project中b表的任意列字段。 ：元数据匹配类型，取值为固定值guid。

**metaType**

：字段扫描排除项；非必填。包含**规则名** 和**规则内容** ，取值

**excludeMetaRules**

与**metaRules** 的**规则名** 和**规则内容** 一致。 ： name 对应参数中的dataType，templateJsonStr 对应clazz。

**clazz**

**参数说明**

| 参数 | 类型 | 描述 |
|---|---|---|
| ContentRule | Struct | 内容识别规则。 ContentRule 与 MetaRules 二选一，二者必填其一。 |
| -Name | string | 规则名：内置规则名或正则表达式。 自生成和样本库不支持。 |
| -Content | string | 规则内容：当规则名为正则表达式时，此处传入正则内容。 |
| MetaRules | Array | 字段扫描规则。 ContentRule 与 MetaRules 二选一，二者必填其一。 |
| -Name | string | 规则名，固定值： 元数据识别 。 |
| -Contents | Array | 规则内容列表。 |

DataWorks

| 参数 | 类型 | 描述 |
|---|---|---|
| --CompareType | string | 比较类型，固定值： equal 或 regexp 。 若 Param 包含通配符 * ， 应设为 regexp ；否则为 equal 。 |
| --Param | string | 字段扫描路径，格式： project.table.column ，支持通配符 * 。 示例： - a.b.c ：匹配 project=a, table=b, column=c； - a.b.* ：匹配 project=a, table=b, 任意列。 |
| --MetaType | string | 元数据匹配类型，固定值： guid 。 |
| ExcludeMetaRules | Array | 字段扫描排除规则（非必填）。 |
| -Name | string | 规则名，固定值： 元数据识别 。 |
| -Contents | Array | 排除规则内容列表。 |
| --CompareType | string | 比较类型，固定值： equal 或 regexp 。 若 Param 包含通配符 * ， 应设为 regexp ；否则为 equal 。 |
| --Param | string | 字段扫描路径，格式： project.table.column ，支持通配符 * 。 示例： - a.b.c ：匹配 project=a, table=b, column=c； - a.b.* ：匹配 project=a, table=b, 任意列。 |
| --MetaType | string | 元数据匹配类型，固定值： guid 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| Success | Boolean | true | 是否请求成功。 |
| Data | Boolean | true | 返回结果数据。 |

**示例**

请求示例

```
&HitThreshold=50
```

`&Type=`手机号

```json
&Status=1 &Owner=193379**** &RuleDetailJson={
 "contentTemplates": [{
```

`"name": "`正则式匹配`",` `"localeName": "`正则式匹配`",`

```json
  "templateJsonStr": "
{\"_clazz\":\"com.alipay.dsgclient.sdk.dsg.fastscan.engine.cond.RegExpCondition\"}",
  "regex": null,
  "uuid": null,
  "desc": "",
  "custom": false
 }]
} &SensLevel=Critical &RuleGroup=test &TenantId=10241024 &NodeId=1234
```

`&NodeParent=`客户/个人/个人自然信息/个人基本概况信息

```
&RecognizeRulesType=1
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":true,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### AddSensLevel

DataWorks 该接口用于在DataWorks中添加新的敏感级别配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OpAccoun t | Strin g | Query | 是 | uat | 执行本次操作的人员名称。 |
| SensLevel Alias | Strin g | Query | 是 | L1 | 敏感等级。 |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| Success | Boolean | true | 是否请求成功。 |
| Data | Boolean | true | 返回结果数据。 |

**示例**

请求示例

```
&OpAccount=uat &SensLevelAlias=L1 &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":true,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### DeleteSenRule

DataWorks 该接口用于删除DataWorks中的敏感规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Query | 是 | 860438872620113XXXX | 敏感规则ID。 |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Boolean | true | 返回结果数据。 |
| DynamicError Code | Boolean | Invalid.Tenant.Con nectionNotExists | 错误码。取值同ErrorCode。 |
| DynamicError Message | Boolean | The connection does not exist. | 错误信息。取值同ErrorMessage。 |

**示例**

请求示例

```
&Id=860438872620113XXXX &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "DynamicErrorMessage":false,
 "HttpStatusCode":400,
 "Data":true,
 "DynamicErrorCode":false,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <DynamicErrorMessage>false</DynamicErrorMessage> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <DynamicErrorCode>false</DynamicErrorCode> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

DataWorks

#### GetSenRule

该接口用于查询敏感规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | Strin g | Query | 否 | 手机号 | 规则名。 |
| Status | Strin g | Query | 否 | 0 | 脱敏规则的生效状态。 枚举值: 0(失效) 1(生效) |
| Owner | Strin g | Query | 否 | user1 | 负责人。 |
| PageSize | Integ er | Query | 否 | 10 | 每页显示的条数，默认为10 条，最大100条。 |
| PageNum | Integ er | Query | 是 | 1 | 请求的数据页数，用于翻页。 |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Struct | / | 返回结果数据。 |

|  | 开发指南·OpenAPI参 | 考 |  | DataWork | s |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Rules | Array | / | 规则列表。 |
| -- RuleDetailJson | String | { "contentTemplates ": [{ "name": "正则式匹配", "localeName": "正则式匹配", "templateJsonStr": " {\" clazz\":\"com.al _ ipay.dsgclient.sdk. dsg.fastscan.engin e.cond.RegExpCon dition\"}", "regex": null, "uuid": null, "desc": "", "custom": false }] } | 规则详情JSON。详情请参见AddSenRule接口的 RuleDetailJson参数描述。 |
| --LocaleType | String | ru RU _ | 国际化规则名称。 |
| --RuleDesc | String | Please customize the password expiration time detection standard as | 规则描述。 |
| --Owner | String | 110755000425XXX X | 责任人。 |
| --UpdateTime | Long | 1600963200000 | 修改时间戳。 |
| --RuleGroup | String | 示例值 | 聚类tag，标签。 |
| --IsCustom | Boolean | false | 是否是自定义类型。 |
| --BydAccuracy | Float | 0.95 | 前天的准确率。 |
| --YdAccuracy | Float | 0.95 | 昨天的准确率。 |
| --CreateTime | Long | 1727055811000 | 创建时间。 |
| --SenId | Long | 1111111111 | 规则ID。 |
| --NodeParent | Long | 12345 | 分类分级标签。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TotalCount | Integer | 42 | 总数。 |

**示例**

请求示例

```
&PageNum=1 &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":{
  "TotalCount":42,
  "Rules":[
   {
    "Owner":"110755000425XXXX",
    "RuleDetailJson":"{\t\"contentTemplates\": [{\t\t\"name\": \"正则式匹配
\",\t\t\"localeName\": \"正则式匹配\",\t\t\"templateJsonStr\": \" {\\\"_clazz\\\":\\\"com.alipay.dsgclient.sdk.dsg.fastscan.engine.cond.RegExpCondition\\\" ",\t\t\"regex\": null,\t\t\"uuid\": null,\t\t\"desc\": \"\",\t\t\"custom\": false\t}]}",
    "BydAccuracy":0.95,
    "IsCustom":false,
    "SenId":1111111111,
    "CreateTime":1727055811000,
    "UpdateTime":1600963200000,
    "LocaleType":"ru_RU",
    "RuleDesc":"Please customize the password expiration time detection standard as",
    "YdAccuracy":0.95,
    "NodeParent":12345,
```

`"RuleGroup":"`示例值"

```
   }
```

]

```json
 },
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>
 <TotalCount>42</TotalCount>
 <Rules>
  <Owner>110755000425XXXX</Owner>
  <RuleDetailJson>{
 &quot;contentTemplates&quot;: [{
  &quot;name&quot;: &quot;正则式匹配&quot;,
  &quot;localeName&quot;: &quot;正则式匹配&quot;,
  &quot;templateJsonStr&quot;: &quot;
{\&quot;_clazz\&quot;:\&quot;com.alipay.dsgclient.sdk.dsg.fastscan.engine.cond.RegExpCond ion\&quot;}&quot;,
  &quot;regex&quot;: null,
  &quot;uuid&quot;: null,
  &quot;desc&quot;: &quot;&quot;,
  &quot;custom&quot;: false
 }]
}</RuleDetailJson>
   <BydAccuracy>0.95</BydAccuracy>
   <IsCustom>false</IsCustom>
   <SenId>1111111111</SenId>
   <CreateTime>1727055811000</CreateTime>
   <UpdateTime>1600963200000</UpdateTime>
   <LocaleType>ru_RU</LocaleType>
   <RuleDesc>Please customize the password expiration time detection standard as</RuleD
esc>
   <YdAccuracy>0.95</YdAccuracy>
   <NodeParent>12345</NodeParent>
   <RuleGroup>示例值</RuleGroup>
  </Rules>
 </Data>
 <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode>
 <ErrorMessage>The connection does not exist.</ErrorMessage>
 <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### GetSensitiveCountData

获取指定租户的敏感数据统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |
| Type | Strin g | Query | 否 | odps.odps | 引擎类型。 默认值： odps.odps |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| SensData | Map | / | 废弃参数，暂不使用。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 是否请求成功。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | Invalid.Tenant.Connect ionNotExists | 错误码。200标识查询任务成功。 |
| errorMessage | String | The connection does not exist. | 调用失败时返回的错误信息。 |
| httpStatusCode | Integer | 400 | HTTP 返回状态码。 |
| data | Object | / | 返回结果数据。 |
| -totalTables | Integer | 114 | 数据库中表的总数。 |
| -totalCols | Integer | 1446 | 数据库中所有表的列（字段）总数。 |
| -sensTables | Integer | 10 | 包含敏感数据的表的数量。 |
| -sensCols | Integer | 17 | 包含敏感数据的列（字段）的总数。 |
| dynamicErrorCode | String | Invalid.Tenant.Connect ionNotExists | 错误码。取值同 ErrorCode。 |
| dynamicErrorMessage | String | The connection does not exist. | 错误信息。取值同 ErrorMessage。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetSensitiveCountData &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "httpStatusCode": 200,
    "data": {
        "totalTables": 114,
        "totalCols": 1446,
        "sensTables": 10,
        "sensCols": 17
    },
    "requestId": null,
    "dynamicErrorCode": null,
    "dynamicErrorMessage": null
}
```

DataWorks `XML` 格式

```xml
<success>true</success> <errorCode /> <errorMessage /> <httpStatusCode>200</httpStatusCode> <data>
 <totalTables>114</totalTables>
 <totalCols>1446</totalCols>
 <sensTables>10</sensTables>
 <sensCols>17</sensCols>
</data> <requestId /> <dynamicErrorCode /> <dynamicErrorMessage />
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | 1010010014 | Forbidden.NoTenant | The tenant information cannot be obtained using user ID. |
| 500 | 100000500 | InternalError.DQC.BizError | An internal error occurred. |
| 400 | 1010010016 | Invalid.Param | The request parameter is invalid. |

#### UpdateRiskInfoData

该接口用于更新指定实例的风险信息数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstIds | Strin g | Query | 是 | ACC001 | 数据访问和数据导出的唯一标识。 |
| Status | Strin g | Query | 是 | INIT | 状态。 枚举值: HAS RISK(有风险) _ NO RISK(无风险) _ INIT(待处理) |
| Tags | Strin g | Query | 否 | ["tag1", "tag2", "tag3"] | 标签。 |

| 开发指南·Open | API参考 |  |  |  | DataWork |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Content | Strin g | Query | 否 | test | 描述。 |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Boolean | true | 返回结果数据。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateRiskInfoData &InstIds=ACC001 &Status=INIT &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":true,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### UpdateSenRule

该接口用于更新敏感规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

DataWorks

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| HitThresh old | Integ er | Query | 是 | 50 | 命中阈值。若抽样数据中， 超过阈值百分比（例如，60%）的数据命中NER 模型，则认为命中该敏感字段。取值：0~100之间的整数。 |
| Type | Strin g | Query | 是 | 手机号 | 规则名。 |
| Status | Strin g | Query | 是 | 0 | 脱敏规则的生效状态。 枚举值: 0(失效) 1(生效) |
| RuleDesc | Strin g | Query | 否 | 安全基线01 | 规则描述。 |
| RuleDetail Json | Strin g | Query | 是 | { "contentTemplates": [{ "name": "正则式匹配", "localeName": "正则式匹配", "templateJsonStr": " {\" clazz\":\"com.alipay. _ dsgclient.sdk.dsg.fastsca n.engine.cond.RegExpCo ndition\"}", "regex": null, "uuid": null, "desc": "", "custom": false }] } | 规则详情，详情请参见 AddSenRule接口的 RuleDetailJson参数描述。 |
| SensLevel | Strin g | Query | 是 | L1 | 敏感级别，涉及机密或至关重要的信息，需最高级别防护措施。 |
| RuleGroup | Strin g | Query | 是 | 用户行为规则组 | 用于数据处理流程的规则集合，如数据清洗、格式转换、聚合计算等。 |
| Id | Strin g | Query | 是 | 860438872620113XXXX | 规则ID。 |
| Owner | Strin g | Query | 是 | user1 | 操作人。 |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |
| NodeId | Strin g | Query | 是 | 1234 | 节点ID。 |
| NodePare nt | Strin g | Query | 是 | 客户/个人/个人自然信息/个人基本概况信息 | 分类结点的父结点信息。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Recognize RulesType | Integ er | Query | 是 | 1 | 敏感数据识别规则类型。 枚举值: 1(正则表达式) 2(内置规则) 3(样本库) 4(自生成模型) |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Boolean | true | 返回结果数据。 |

**示例**

请求示例 DataWorks

```
&HitThreshold=50
```

`&Type=`手机号

```json
&Status=0 &RuleDetailJson={
 "contentTemplates": [{
```

`"name": "`正则式匹配`",` `"localeName": "`正则式匹配`",`

```json
  "templateJsonStr": "
{\"_clazz\":\"com.alipay.dsgclient.sdk.dsg.fastscan.engine.cond.RegExpCondition\"}",
  "regex": null,
  "uuid": null,
  "desc": "",
  "custom": false
 }]
} &SensLevel=L1
```

`&RuleGroup=`用户行为规则组

```
&Id=860438872620113XXXX &Owner=user1 &TenantId=10241024 &NodeId=1234
```

`&NodeParent=`客户/个人/个人自然信息/个人基本概况信息

```
&RecognizeRulesType=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":true,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

DataWorks

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

#### UpdateSensitive

该接口用于更新敏感数据规则配置的接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RuleName | Strin g | Query | 是 | rename rule 1 _ _ | 规则名称。 |
| Guid | Strin g | Query | 是 | dataworks test 001.myp _ _ hone odps email.mypho _ _ ne02#ODPS.ODPS | 表id |
| TenantId | Strin g | Query | 是 | 10241024 | 租户ID。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否请求成功。 |
| ErrorCode | String | Invalid.Tenant.Con nectionNotExists | 错误码。200标识查询任务成功。 |
| ErrorMessage | String | The connection does not exist. | 调用失败时，返回的错误信息。 |
| HttpStatusCod e | Integer | 400 | HTTP返回码。 |
| RequestId | String | 0000-ABCD- EFG**** | 请求唯一ID。 |
| Data | Boolean | true | 返回结果数据。 |

**示例**

请求示例

```
&RuleName=rename_rule_1 &Guid=dataworks_test_001.myphone_odps_email.myphone02#ODPS.ODPS &TenantId=10241024
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"0000-ABCD-EFG****",
 "HttpStatusCode":400,
 "Data":true,
 "ErrorCode":"Invalid.Tenant.ConnectionNotExists",
 "ErrorMessage":"The connection does not exist.",
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>0000-ABCD-EFG****</RequestId> <HttpStatusCode>400</HttpStatusCode> <Data>true</Data> <ErrorCode>Invalid.Tenant.ConnectionNotExists</ErrorCode> <ErrorMessage>The connection does not exist.</ErrorMessage> <Success>true</Success>
```

**错误码**

DataWorks

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 429 | 9990040002 | Throttling.Api.Risk | The request for this resource has exceeded your daily available limit. |
| 429 | 9990040003 | Throttling.Resource | You have reached the limit for the resource. Please contact us by submitting a ticket. |
| 429 | 9990020001 | Throttling.System | The DataWorks system is busy. Try again later. |
| 429 | 9990020002 | Throttling.User | Your request is too frequent. Try again later. |
| 403 | 9990010001 | Forbidden.Access | Access is forbidden. Activate DataWorks first. |
| 500 | 9990010003 | Forbidden.Not.Server | The dataworksAPI service is not available in this area. Please try it in another area. |
| 500 | 9990019999 | InternalError.Unknown | The specified error occurred. Try again later. |
| 500 | 9990030002 | InternalError.UserId.Missing | An internal system error occurred. Try again later. |
| 400 | 9990030003 | InternalError.Bad.Parameters | Your request has bad parameters |

### 安全中心

#### CreatePermissionApplyOrder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreatePermissio nApplyOrder | 系统规定参数。取值： CreatePermissionApplyOrder。 |
| ApplyObject.N.A ctions | String | 是 | Select,Describe | 申请的权限类型，一次申请多种类型权限时使用逗号（,）分隔。目前仅支持申请 Select、Describe、Drop、Alter、 Update、Download类型。 |

DataWorks

| ApplyObject.N.C olumnMetaList.N .Name | String | 是 | aColumnName | 申请目标列的权限，此处输入列名称。如果申请全表的权限，则需要输入表的所有列名。 仅当MaxCompute项目开启了 labelSecurity，才可以申请部分列的权限。如果MaxCompute项目没有开启 labelSecurity，则只能申请全表的权限。 |
|---|---|---|---|---|
| ApplyObject.N.N ame | String | 是 | aTableName | 申请的对象。目前仅支持申请 MaxCompute表的权限，此处需要输入目标表的名称。 |
| ApplyReason | String | 是 | I need to use this table | 申请的原因。用于管理员进行评估审批。 |
| ApplyUserIds | String | 是 | 2678426004089 93176,2678426 00408993177 | 申请权限的阿里云账户UID，当同时为多个账号申请权限时，使用逗号（,）隔开。 |
| MaxComputeProj ectName | String | 是 | aMaxcomputePr ojectName | 申请权限的MaxCompute项目名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| WorkspaceId | Integer | 是 | 12345 | 申请权限的MaxCompute项目所属的 DataWorks工作空间ID，您可以进入 DataWorks工作空间配置页面，查询工作空间ID。 |
| Deadline | Long | 否 | 1617115071885 | 申请权限的到期时间。此处需要输入一个 unix时间戳，不输入默认到期时间为2065 年1月1日。 如果MaxCompute项目未开启 LabelSecurity，或申请的表字段安全等级为0或小于等于申请账号的安全等级时，只能申请永久权限。 您可以进入DataWorks工作空间的管理页面，在MaxCompute引擎的高级配置页面，查看是否启动列级别访问控制。 您可以进入DataWorks工作空间，在数据地图查看字段的安全等级，在成员管理页面查看账号的安全等级。 |
| OrderType | Integer | 否 | 1 | 申请单类型。目前仅支持取值为1，表示对象ACL权限申请。 |
| EngineType | String | 否 | odps | 申请权限的计算引擎类型。目前仅支持取值为odps，表示仅支持申请 MaxCompute计算引擎的权限。 |

DataWorks

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FlowId | List | ee276e6e-5d34- 46d8-b848- bca7879ed233 | 生成的申请单ID。当同时申请多个对象并且各个对象的审批人不同时，会根据不同的审批人生成多张申请单，此时会返回一个数组。 |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreatePermissionApplyOrder &ApplyObject.1.Actions=Select,Describe &ApplyObject.1.ColumnMetaList.1.1ame=aColumnName &ApplyObject.1.1ame=aTableName &ApplyReason=I need to use this table &ApplyUserIds=267842600408993176,267842600408993177 &MaxComputeProjectName=aMaxcomputeProjectName &RegionId=default &WorkspaceId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<FlowId>ee276e6e-5d34-46d8-b848-bca7879ed233</FlowId> <RequestId>0bc1ec92159376****</RequestId>
```

`JSON` 格式

```json
{
    "FlowId": "ee276e6e-5d34-46d8-b848-bca7879ed233",
    "RequestId": "0bc1ec92159376****"
}
```

#### ApprovePermissionApplyOrder

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ApprovePermissi onApplyOrder | 系统规定参数。取值： ApprovePermissionApplyOrder。 |

DataWorks

| ApproveAction | Integer | 是 | 1 | 执行的审批动作，取值如下： 1：同意。 2：拒绝。 |
|---|---|---|---|---|
| ApproveComme nt | String | 是 | agree | 审批的备注信息。 |
| FlowId | String | 是 | 48f36729-05f9- 4a40-9286- 933fd940f30a | 审批的申请单ID，您可以调用 ListPermissionApplyOrders接口获取。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ApproveSucce ss | Boolean | true | 审批是否成功。 |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ApprovePermissionApplyOrder &ApproveAction=1 &ApproveComment=agree &FlowId=48f36729-05f9-4a40-9286-933fd940f30a &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0bc1ec92159376****</RequestId> <ApproveSuccess>true</ApproveSuccess>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376****",
    "ApproveSuccess": true
}
```

#### ListPermissionApplyOrders

DataWorks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListPermissionA pplyOrders | 系统规定参数。取值： ListPermissionApplyOrders。 |
| EngineType | String | 是 | odps | 申请单的计算引擎类型。目前仅支持取值为odps，表示仅支持申请MaxCompute 计算引擎的权限。 |
| OrderType | Integer | 是 | 1 | 申请单类型。目前仅支持取值为1，表示对象ACL权限申请。 |
| QueryType | Integer | 是 | 1 | 申请单的查询类型。取值如下： 0：我提交的申请单。 1：由我审批的申请单。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| FlowStatus | Integer | 否 | 1 | 申请单的状态。取值如下： 1：待审批。 2：审批通过，授权成功。 3：审批通过，授权失败。 4：审批拒绝。 |
| WorkspaceId | Integer | 否 | 12345 | 申请单所属的工作空间ID，不输入则返回所有工作空间的申请单。您可登录 DataWorks控制台，进入工作空间配置页面，查询工作空间ID。 |
| MaxComputeProj ectName | String | 否 | aMaxComputePr oject | 申请单所属的MaxCompute项目名称，不输入则返回所有MaxCompute项目的申请单。 |
| TableName | String | 否 | aTableName | 申请单包含的表名称，不输入则返回所有表的申请单。 |
| StartTime | Long | 否 | 1616200471885 | 查询目标起始时间发起的申请单，配置为一个unix时间戳。不输入则表示查询所有的申请单。 |
| EndTime | Long | 否 | 1617200471885 | 查询目标截至时间的申请单，配置为一个 unix时间戳。不输入则表示查询截至当前时间的申请单。 |

DataWorks

| PageNum | Integer | 否 | 1 | 分页查询页码。大于等于1的正整数，默认为1。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 100 | 每页显示的条数，默认为10条，最大100 条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ApplyOrders | Struct |  | 权限申请单的分页查询结果。 |
| ApplyOrder | Array of Orders |  | 权限申请单列表。 |
| ApplyBaseId | String | 267842600408993 176 | 提交申请单的阿里云用户UID。 |
| ApplyTimesta mp | Long | 1615284086000 | 申请单的提交时间，显示为一个unix时间戳。 |
| ApproveConte nt | Struct |  | 申请单的内容。 |
| ApplyReason | String | I need to use this table | 申请的原因。用于管理员进行评估审批。 |
| OrderType | Integer | 1 | 申请单类型。目前仅支持取值为1，表示对象 ACL权限申请。 |
| ProjectMeta | Struct |  | 申请对象的内容。 |
| ObjectMetaList | Array of ObjectMetaList |  | 申请的对象信息。 |
| Actions | List | Select,Describe | 申请的权限类型，一次申请多种类型权限时使用英文逗号（,）分隔。 目前仅支持申请Select、Describe、Drop、 Alter、Update、Download类型。 |
| ObjectName | String | aTableName | 申请的表名称。 |
| WorkspaceNa me | String | aWorkspaceName | 申请权限的MaxCompute项目所属的 DataWorks工作空间名称。 |
| FlowId | String | ad8da78d-8135- 455e-9486- 27cf213fc140 | 申请单ID。 |

DataWorks

| FlowStatus | Integer | 2 | 申请单的状态。取值如下： 1：待审批。 2：审批通过，授权成功。 3：审批通过，授权失败。 4：审批拒绝。 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 10 | 每页显示的条数。 |
| TotalCount | Integer | 150 | 返回的权限申请单总数。 |
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListPermissionApplyOrders &EngineType=odps &OrderType=1 &QueryType=1 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376****</RequestId> <ApplyOrders>
    <TotalCount>150</TotalCount>
    <PageSize>10</PageSize>
    <PageNumber>1</PageNumber>
    <ApplyOrder>
        <ApplyTimestamp>1615284086000</ApplyTimestamp>
        <FlowId>ad8da78d-8135-455e-9486-27cf213fc140</FlowId>
        <ApplyBaseId>267842600408993176</ApplyBaseId>
        <FlowStatus>2</FlowStatus>
        <ApproveContent>
            <OrderType>1</OrderType>
            <ApplyReason>I need to use this table</ApplyReason>
            <ProjectMeta>
                <WorkspaceName>aWorkspaceName</WorkspaceName>
                <ObjectMetaList>
                    <ObjectName>aTableName</ObjectName>
                    <Actions>Select,Describe</Actions>
                </ObjectMetaList>
            </ProjectMeta>
        </ApproveContent>
    </ApplyOrder>
</ApplyOrders>
```

`JSON` 格式

```json
{
    "RequestId": "0bc1ec92159376****",
    "ApplyOrders": {
        "TotalCount": 150,
        "PageSize": 10,
        "PageNumber": 1,
        "ApplyOrder": {
            "ApplyTimestamp": 1615284086000,
            "FlowId": "ad8da78d-8135-455e-9486-27cf213fc140",
            "ApplyBaseId": 267842600408993180,
            "FlowStatus": 2,
            "ApproveContent": {
                "OrderType": 1,
                "ApplyReason": "I need to use this table",
                "ProjectMeta": {
                    "WorkspaceName": "aWorkspaceName",
                    "ObjectMetaList": {
                        "ObjectName": "aTableName",
                        "Actions": "Select,Describe"
                    }
                }
            }
        }
    }
}
```

DataWorks

#### GetPermissionApplyOrderDetail

调用GetPermissionApplyOrderDetail查询一个权限申请单的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 区域ID，为固定值default 。 |
| FlowId | Strin g | Query | 是 | 48f36729-05f9-4a40- 9286-933fd940**** | 权限申请单ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |
| ApplyOrderDet ail | Struct |  | 申请单详情。 |
| - ApproveAccou ntList | Array |  | 审批申请单的阿里云账号列表。 |
| --BaseId | String | 182293110403**** | 审批申请单的阿里云用户UID。 |
| - GranteeObject List | Array |  | 申请权限的账号信息。 |
| --GranteeType | Integer | 1 | 申请权限的主体类型。目前只支持1（用户）。 |
| -- GranteeTypeS ub | Integer | 103 | 申请权限的主体子类型，取值如下： 101：生产云账号。 103：个人云账号。 105：代他人申请云账号。 |
| -- GranteeName | String | RAM$dataworks 3 _ h1 1:StsRamUser( _ StsRamUser) | 申请权限的云账号名称。格式与MaxCompute 的账号格式一致。 主账号为ALIYUN$+账号名。 子账号为RAM$+账号名。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --GranteeId | String | 26784260040899* *** | 申请权限的阿里云用户UID。 |
| -ApplyBaseId | String | 26784260040899* *** | 提交申请单的阿里云用户UID。 |
| - ApplyTimesta mp | Long | 1615284086000 | 发起申请单的时间，显示为一个unix时间戳。 |
| -FlowId | String | ad8da78d-8135- 455e-9486- 27cf213f**** | 申请单ID。 |
| -FlowStatus | Integer | 2 | 申请单的状态。取值如下： 1：待审批。 2：审批通过，授权成功。 3：审批通过，授权失败。 4：审批拒绝。 |
| - ApproveConte nt | Struct |  | 申请的具体内容。 |
| --ApplyReason | String | 需要使用表 | 申请的原因，用于管理员审批参考。 |
| --Deadline | Long | 1617115071885 | 申请权限的到期时间。此处显示为一个unix时间戳。 如果MaxCompute项目未开启LabelSecurity， 或申请的表字段安全等级为0或小于等于申请账号的安全等级时，只能申请永久权限。 |
| --OrderType | Integer | 1 | 申请单类型。目前仅支持取值为1，表示对象 ACL权限申请。 |
| --ProjectMeta | Struct |  | 申请对象所属的项目和工作空间信息。 |
| --- ObjectMetaList | Array |  | 申请对象的详细信息。 |
| ---- ColumnMetaLi st | Array |  | 申请对象的列字段信息。 |
| ----- ColumnName | String | aColumnName | 申请的列名称。 |
| ----- ColumnComm ent | String | 字段描述 | 申请的列描述。 |

| DataWorks |  |  | 开发指南·OpenAPI参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---- ObjectName | String | aTableName | 申请的表名。 |
| --- MaxComputeP rojectName | String | aMaxComputeProje ct | 申请对象所在的MaxCompute项目。 |
| ---WorkspaceId | Integer | 12345 | 申请对象所在的DataWorks工作空间ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetPermissionApplyOrderDetail &RegionId=default &FlowId=48f36729-05f9-4a40-9286-933fd940****
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"0bc1ec92159376****",
 "ApplyOrderDetail":{
  "ApplyTimestamp":1615284086000,
  "FlowId":"ad8da78d-8135-455e-9486-27cf213f****",
  "-GranteeObjectList":{
   "GranteeType":1,
   "GranteeId":"26784260040899****",
   "GranteeName":"RAM$dataworks_3h1_1:StsRamUser(StsRamUser)",
   "GranteeTypeSub":103
  },
  "-ApproveContent":{
   "OrderType":1,
   "Deadline":1617115071885,
```

`"ApplyReason":"`需要使用表`",`

```json
   "--ProjectMeta":{
    "MaxComputeProjectName":"aMaxComputeProject",
    "---ObjectMetaList":{
     "----ColumnMetaList":{
      "ColumnName":"aColumnName",
```

`"ColumnComment":"`字段描述"

```json
     },
     "ObjectName":"aTableName"
    },
    "WorkspaceId":12345
   }
  },
  "-ApproveAccountList":{
   "BaseId":"182293110403****"
  },
  "ApplyBaseId":"26784260040899****",
  "FlowStatus":2
 }
}
```

`XML` 格式 DataWorks

```xml
<RequestId>0bc1ec92159376****</RequestId> <ApplyOrderDetail>
 <ApplyTimestamp>1615284086000</ApplyTimestamp>
 <FlowId>ad8da78d-8135-455e-9486-27cf213f****</FlowId>
 <-GranteeObjectList>
  <GranteeType>1</GranteeType>
  <GranteeId>26784260040899****</GranteeId>
  <GranteeName>RAM$dataworks_3h1_1:StsRamUser(StsRamUser)</GranteeName>
  <GranteeTypeSub>103</GranteeTypeSub>
 </-GranteeObjectList>
 <-ApproveContent>
  <OrderType>1</OrderType>
  <Deadline>1617115071885</Deadline>
```

`<ApplyReason>`需要使用表`</ApplyReason>`

```xml
  <--ProjectMeta>
   <MaxComputeProjectName>aMaxComputeProject</MaxComputeProjectName>
   <---ObjectMetaList>
    <----ColumnMetaList>
     <ColumnName>aColumnName</ColumnName>
     <ColumnComment>字段描述</ColumnComment>
    </----ColumnMetaList>
    <ObjectName>aTableName</ObjectName>
   </---ObjectMetaList>
   <WorkspaceId>12345</WorkspaceId>
  </--ProjectMeta>
 </-ApproveContent>
 <-ApproveAccountList>
  <BaseId>182293110403****</BaseId>
 </-ApproveAccountList>
 <ApplyBaseId>26784260040899****</ApplyBaseId>
 <FlowStatus>2</FlowStatus>
</ApplyOrderDetail>
```

#### RevokeColumnPermission

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RevokeColumnP ermission | 系统规定参数。取值： RevokeColumnPermission。 |
| Columns | String | 是 | id,name | 需要撤销权限的字段名称。一次撤销多个字段的权限时，使用逗号（,）分隔。 当前仅支持撤销MaxCompute表字段的权限。 |

DataWorks

| MaxComputeProj ectName | String | 是 | aMaxcomputePr ojectName | 需要撤销权限的字段所在的MaxCompute 项目名称。您可以登录DataWorks控制台，进入工作空间配置页面，查询 DataWorks工作空间绑定的 MaxCompute项目名称。 |
|---|---|---|---|---|
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | aTableName | 需要撤销权限的字段所属的MaxCompute 表名称。 |
| WorkspaceId | Long | 是 | 12345 | 需要撤销权限的字段所在的DataWorks工作空间ID。您可以登录DataWorks控制台，进入工作空间配置页面，查询工作空间ID。 |
| RevokeUserNam e | String | 否 | RAM$dataworks 3h1 1:stsramus _ _ er | 撤销字段权限的阿里云账号名称。账号格式与MaxCompute的账号格式一致。 主账号为ALIYUN$+账号名。 子账号为RAM$+账号名。 该参数与RevokeUserId参数配置一个即可。如果同时配置了该参数与 RevokeUserId参数，但二者取值不同，则系统会以RevokeUserId参数的配置内容为准。 |
| RevokeUserId | String | 否 | 2678426004089 93176 | 撤销字段权限的阿里云账号ID。您可以登录DataWorks控制台，进入安全设置页面获取账号ID。 该参数与RevokeUserName参数配置一个即可。如果同时配置了该参数与 RevokeUserName参数，但二者取值不同，则系统会以RevokeUserId参数的配置内容为准。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |
| RevokeSucces s | Boolean | true | 撤销操作是否成功。 |

**示例**

请求示例 DataWorks

```
http(s)://[Endpoint]/?Action=RevokeColumnPermission &Columns=id,name &MaxComputeProjectName=aMaxcomputeProjectName &RegionId=default &TableName=aTableName &WorkspaceId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RevokeSuccess>true</RevokeSuccess> <RequestId>0bc1ec92159376****</RequestId>
```

`JSON` 格式

```json
{
    "RevokeSuccess": true,
    "RequestId": "0bc1ec92159376****"
}
```

#### RevokeTablePermission

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RevokeTablePer mission | 系统规定参数。取值： RevokeTablePermission。 |
| Actions | String | 是 | Select,Describe | 需要撤销的表的操作权限，一次撤销多种操作权限时使用逗号（,）分隔。 目前仅支持撤销MaxCompute表的 Select、Describe、Download等操作权限。 |
| MaxComputeProj ectName | String | 是 | aMaxcomputePr ojectName | 需要撤销权限的表所在的MaxCompute项目名称。您可以登录DataWorks控制台， 进入工作空间配置页面，查询DataWorks 工作空间绑定的MaxCompute项目名称。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |
| TableName | String | 是 | aTableName | 需要撤销权限的MaxCompute表名称。 |

DataWorks

| WorkspaceId | Long | 是 | 12345 | 需要撤销权限的MaxCompute表所属的 DataWorks工作空间ID。您可以登录 DataWorks控制台，进入工作空间配置页面，查询工作空间ID。 |
|---|---|---|---|---|
| RevokeUserNam e | String | 否 | RAM$dataworks 3h1 1:stsramus _ _ er | 撤销表权限的云账号名称。账号格式与 MaxCompute的账号格式一致。 主账号为ALIYUN$+账号名。 子账号为RAM$+账号名。 该参数与RevokeUserId参数配置一个即可。如果同时配置了该参数与 RevokeUserId参数，但二者取值不同，则系统会以RevokeUserId参数的配置内容为准。 |
| RevokeUserId | String | 否 | 2678426004089 93176 | 撤销表权限的阿里云账号ID。您可以登录 DataWorks控制台，进入安全设置页面获取账号ID。 该参数与RevokeUserName参数配置一个即可。如果同时配置了该参数与 RevokeUserName参数，但二者取值不同，则系统会以RevokeUserId参数的配置为准。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0bc1ec92159376** ** | 请求ID。 |
| RevokeSucces s | Boolean | true | 撤销操作是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RevokeTablePermission &Actions=Select,Describe &MaxComputeProjectName=aMaxcomputeProjectName &RegionId=default &TableName=aTableName &WorkspaceId=12345
```

`&<`公共请求参数> 正常返回示例 `XML` 格式 DataWorks

```xml
<RevokeSuccess>true</RevokeSuccess> <RequestId>0bc1ec92159376****</RequestId>
```

`JSON` 格式

```json
{
    "RevokeSuccess": true,
    "RequestId": "0bc1ec92159376****"
}
```

### 迁移助手

#### GetMigrationProcess

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetMigrationPro cess | 系统规定参数。取值： GetMigrationProcess。 |
| MigrationId | Long | 是 | 123456 | 导入导出包的ID。您可以调用 CreateImportMigration接口获取。 |
| ProjectId | Long | 是 | 123456 | 项目空间的ID。您可以进入DataWorks项目空间的设置页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Array of ProgressTaskIt em |  | 导入导出任务的进度信息，包括导入导出任务所有步骤的名称和进度状态。 |
| TaskName | String | IMPORE PREPARE _ | 导入导出任务的步骤名称。 |
| TaskStatus | String | SUCCESS | 导入导出任务的步骤运行状态。取值如下： INIT，初始状态。 RUNNING，运行中。 FAILURE，运行失败。 SUCCESS，运行成功。 |

DataWorks

| ErrorCode | String | 110001123456 | 错误码。 |
|---|---|---|---|
| ErrorMessage | String | test error msg | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | 请求ID。 | 请求ID。 |
| Success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMigrationProcess &MigrationId=123456 &ProjectId=123456 &RegionId=default
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>请求ID。</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>
    <TaskName>IMPORE_PREPARE</TaskName>
    <TaskStatus>SUCCESS</TaskStatus>
</Data> <ErrorCode>110001123456</ErrorCode> <ErrorMessage>test error msg</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "请求ID。",
    "HttpStatusCode": 200,
    "Data": {
        "TaskName": "IMPORE_PREPARE",
        "TaskStatus": "SUCCESS"
    },
    "ErrorCode": 110001123456,
    "ErrorMessage": "test error msg",
    "Success": true
}
```

DataWorks

#### StartMigration

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | StartMigration | 系统规定参数。取值：StartMigration。 |
| MigrationId | Long | 是 | 123456 | 导入导出包的ID。 |
| ProjectId | Long | 是 | 123456 | 项目空间的ID。您可以进入DataWorks项目空间的设置页面查看。 |
| RegionId | String | 是 | default | 区域ID，为固定值default。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 启动执行导入导出任务的状态信息。 true，任务启动成功。 false，任务启动失败。 |
| ErrorCode | String | 110001123445 | 错误码。 |
| ErrorMessage | String | test error msg | 错误信息。 |
| HttpStatusCod e | Integer | 200 | HTTP状态码。 |
| RequestId | String | FSDFSDF- WERWER-XVCX- DSFSDF | 请求ID。 |
| Success | Boolean | true | 调用是否成功。 |

**示例**

请求示例

```
&MigrationId=123456 &ProjectId=123456 &RegionId=default
```

`&<`公共请求参数> DataWorks 正常返回示例 `XML` 格式

```xml
<RequestId>FSDFSDF-WERWER-XVCX-DSFSDF</RequestId> <HttpStatusCode>200</HttpStatusCode> <Data>true</Data> <ErrorCode>110001123445</ErrorCode> <ErrorMessage>test error msg</ErrorMessage> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "FSDFSDF-WERWER-XVCX-DSFSDF",
    "HttpStatusCode": 200,
    "Data": true,
    "ErrorCode": 110001123445,
    "ErrorMessage": "test error msg",
    "Success": true
}
```

#### GetMigrationSummary

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |
| ProjectId | Long | Body | 是 | 12345 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间管理页面获取ID。 |
| MigrationI d | Long | Body | 是 | 1234 | 导入、导出任务的ID。 您可以调用 CreateImportMigration获取导入任务的ID，调用 CreateExportMigration获取导出任务的ID。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 19999A96-71BA- 1845-B455- ED620EF4**** | 请求的ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 调用是否成功。取值： true：调用成功。 false：调用失败。您可以通过请求ID定位问题。 |
| Data | Struct |  | 导入、导出任务详情。 |
| -MigrationId | Long | 1234 | 任务的ID。 |
| -Name | String | test export 01 _ _ | 任务的名称。 |
| -GmtCreate | Long | 1589904000000 | 任务的创建时间。用UNIX时间戳表示，单位：毫秒。 |
| -GmtModified | Long | 1589904000000 | 任务的修改时间。用UNIX时间戳表示，单位：毫秒。 |
| -CreateUser | String | 982293332403**** | 任务创建人的用户ID。 |
| -OpUser | String | 982293332403**** | 任务操作人的用户ID。 |
| -Status | String | EXPORT SUCCESS _ | 导入、导出任务的执行状态。取值： INIT：任务为初始状态。 EDITING：任务在编辑中。 IMPORTING：任务在导入中。 IMPORT ERROR：任务导入失败。 _ IMPORT SUCCESS：任务导入成功。 _ EXPORTING：任务在导出中。 EXPORT ERROR：任务导出失败。 _ EXPORT SUCCESS：任务导出成功。 _ REVOKED：任务被取消。 PARTIAL SUCCESS：仅部分任务导入或导出 _ 成功。 |
| -ProjectId | Long | 12345 | 任务所在DataWorks空间的ID。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DownloadUrl | String | https://shanghai- xxx-oss.oss-cn- shanghai.aliyuncs. com/pre/store/f10 _ bf47 b4fa7df0860f _ .zip? Expires=16395409 03&OSSAccessKeyI d=******eF4Lv5j&S ignature=q***** | 导出任务包的下载链接。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetMigrationSummary &RegionId=default &ProjectId=12345 &MigrationId=1234
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"19999A96-71BA-1845-B455-ED620EF4****",
 "Data":{
  "Status":"EXPORT_SUCCESS",
  "GmtCreate":1589904000000,
  "GmtModified":1589904000000,
  "ProjectId":12345,
  "CreateUser":"982293332403****",
  "MigrationId":1234,
  "OpUser":"982293332403****",
  "Name":"test_export_01",
  "DownloadUrl":"https://shanghai-xxx-oss.oss-cn-
shanghai.aliyuncs.com/pre/store/f10_bf47_b4fa7df0860f.zip? Expires=1639540903&OSSAccessKeyId=******eF4Lv5j&Signature=q*****"
 },
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>19999A96-71BA-1845-B455-ED620EF4****</RequestId> <Data>
 <Status>EXPORT_SUCCESS</Status>
 <GmtCreate>1589904000000</GmtCreate>
 <GmtModified>1589904000000</GmtModified>
 <ProjectId>12345</ProjectId>
 <CreateUser>982293332403****</CreateUser>
 <MigrationId>1234</MigrationId>
 <OpUser>982293332403****</OpUser>
 <Name>test_export_01</Name>
 <DownloadUrl>https://shanghai-xxx-oss.oss-cn-
shanghai.aliyuncs.com/pre/store/f10_bf47_b4fa7df0860f.zip? Expires=1639540903&amp;OSSAccessKeyId=******eF4Lv5j&amp;Signature=q*****</DownloadUrl> </Data> <Success>true</Success>
```

#### ListMigrations

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | default | 服务所在的地域，为固定值default 。 |
| ProjectId | Long | Body | 是 | 12345 | DataWorks工作空间的 ID。您可以登录 DataWorks控制台，进入工作空间配置页面获取工作空间ID。 |
| MigrationT ype | Strin g | Body | 是 | IMPORT | 迁移任务的操作类型。包括：IMPORT、EXPORT。 |
| Owner | Strin g | Body | 否 | 193379**** | 负责人的ID。 |
| PageNum ber | Integ er | Body | 否 | 1 | 请求数据的页码，默认值 1，最大值100。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示的数据条数，默认值10，最大值100。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F9198AA3-9010- 53D5-9714- DC446142**** | 请求ID。用于定位日志，排查问题。 |
| Success | Boolean | true | 请求是否成功。取值： true：成功。 false：失败。 |
| Data | Struct |  | 返回数据。 |
| -Migrations | Array |  | 迁移任务列表。 |
| --Id | Long | 436064 | 主键ID。 |
| --Name | String | test task 1638498 _ _ 642279 | 任务名称。 |
| --PackageType | String | DATAWORKS MOD _ EL | 导入、导出包的类型，取值： DWMA：标准格式。 DATAWORKS MODEL：标准格式。 _ DATAWORKS V2：专有云（V3.6.1- _ V3.11）。 DATAWORKS V3：专有云（V3.12及以 _ 上）。 DWMA和DATAWORKS MODEL可通用。 _ |
| -- MigrationType | String | EXPORT | 迁移任务的操作类型。 IMPORT：导入。 EXPORT：导出。 |
| --CreateTime | Long | 1703667003916 | 创建时间，用UNIX时间戳表示，单位：毫秒。 |
| --UpdateTime | Long | 1703667182911 | 更新时间，用UNIX时间戳表示，单位：毫秒。 |
| --CreateUser | String | 123123**** | 创建人。 |
| -- CreateUserNa me | String | 3h1 test _ | 创建人名称。 |
| --UpdateUser | String | 1231**** | 更新人。 |

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- UpdateUserNa me | String | 3h1 test _ | 更新人名称。 |
| --ProjectId | Long | 72132 | 任务所在DataWorks空间的ID。 |
| --TenantId | Long | 16307 | 租户ID。 |
| --Status | String | SUCCESS | 导入、导出迁移任务的执行状态。取值： INIT：任务为初始状态。 EDITING：任务在编辑中。 RUNNING，任务在运行中。 FAILURE，任务运行失败。 SUCCESS，任务运行成功。 |
| --Message | String | An internal system error occurred. datasource kafka region is not cn- chengdu, can't open network for it | 错误信息。 |
| --DownloadUrl | String | 自动化测试创建 | 导出任务的描述信息。 |
| --Description | String | 自动化测试创建 | 导出任务的描述信息。 |
| -PageNumber | Integer | 1 | 当前的页数。 |
| -PageSize | Integer | 10 | 每页显示的条数。 |
| -TotalCount | Integer | 20 | 总记录数。 |

**示例**

请求示例

```
&RegionId=default &ProjectId=12345 &MigrationType=IMPORT
```

&公共请求参数正常返回示例 `JSON` 格式 DataWorks

```json
{
 "RequestId":"F9198AA3-9010-53D5-9714-DC446142****",
 "Data":{
  "TotalCount":20,
  "PageSize":10,
  "PageNumber":1,
  "Migrations":{
   "UpdateUserName":"3h1_test",
   "Status":"SUCCESS",
```

`"Description":"`自动化测试创建`",`

```json
   "Message":"An internal system error occurred. datasource kafka region is not cn-chen
gdu, can't open network for it",
   "CreateTime":1703667003916,
   "ProjectId":72132,
   "CreateUser":"123123****",
   "MigrationType":"EXPORT",
   "CreateUserName":"3h1_test",
   "Name":"test_task_1638498642279",
   "TenantId":16307,
   "PackageType":"DATAWORKS_MODEL",
   "UpdateTime":1703667182911,
   "UpdateUser":"1231****\t",
   "Id":436064,
   "DownloadUrl":"http://geoip-sdk-user.oss-cn-
zhangjiakou.aliyuncs.com/product/v1/ipv4/trace/v1.20220424123842.dex? Expires=1650780849&OSSAccessKeyId=*****eF4Lv5j&Signature=q*****"
  }
 },
 "Success":true
}
```

`XML` 格式 DataWorks

```xml
<RequestId>F9198AA3-9010-53D5-9714-DC446142****</RequestId> <Data>
 <TotalCount>20</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <Migrations>
  <UpdateUserName>3h1_test</UpdateUserName>
  <Status>SUCCESS</Status>
```

`<Description>`自动化测试创建`</Description>`

```xml
  <Message>An internal system error occurred. datasource kafka region is not cn-chengdu
, can&#x27;t open network for it</Message>
  <CreateTime>1703667003916</CreateTime>
  <ProjectId>72132</ProjectId>
  <CreateUser>123123****</CreateUser>
  <MigrationType>EXPORT</MigrationType>
  <CreateUserName>3h1_test</CreateUserName>
  <Name>test_task_1638498642279</Name>
  <TenantId>16307</TenantId>
  <PackageType>DATAWORKS_MODEL</PackageType>
  <UpdateTime>1703667182911</UpdateTime>
  <UpdateUser>1231**** </UpdateUser>
  <Id>436064</Id>
  <DownloadUrl>http://geoip-sdk-user.oss-cn-
zhangjiakou.aliyuncs.com/product/v1/ipv4/trace/v1.20220424123842.dex? Expires=1650780849&amp;OSSAccessKeyId=*****eF4Lv5j&amp;Signature=q*****</DownloadUrl>
 </Migrations>
</Data> <Success>true</Success>
```

### 开放平台

#### GetExtension

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | default | 区域ID，为固定值 default。 |
| Extension Code | Strin g | Query | 是 | ce4*********086da5 | 扩展程序唯一编码。 |

**返回数据**

DataWorks

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0000-ABCD-EFG | 请求的ID。用于定位日志，排查问题。 |
| Extension | Struct |  | 扩展程序详情。 |
| -BindEventList | Array |  | 扩展点列表。 |
| --EventCode | String | commit-file | 扩展点事件编码。 |
| --EventName | String | 文件提交前置事件 | 扩展点事件名称。 |
| - EventCategory List | Array |  | 事件类型列表。 |
| -- CategoryCode | String | file-change | 事件类型编码。 |
| -- CategoryName | String | 文件变更事件 | 事件类型名称。 |
| - ExtensionCode | String | ce4*********086da 5 | 扩展程序唯一码。 |
| - ExtensionNam e | String | 名称 | 扩展程序名称。 |
| - ExtensionDesc | String | 这是一个描述 | 扩展程序描述。 |
| -HelpDocUrl | String | https://www.aliyun. com/ | 扩展程序帮助文档链接。 |
| -Status | Integer | 0 | 扩展程序状态： 0：测试中, 1：上线中, 3：禁用中, 4：审批中, 5：审批通过, 6：审批不通过。 |
| -ProjectTesting | Long | 13552 | 测试用的项目空间，当扩展程序处于测试中时， 只有测试项目空间可使用。 |
| -DetailUrl | String | https://www.aliyun. com/ | 扩展程序详情地址，用来扩展程序使用者查看本次被卡流程的详情。 |
| - ParameterSett ing | String | extension.project.d isabled=projectId1, projectId2,projectId 3 | 参数配置信息。 |
| -OptionSetting | String | 选项配置 | 选项配置。 |

DataWorks

**示例**

请求示例

```
&ExtensionCode=ce4*********086da5
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Extension":{
  "Status":0,
  "ExtensionName":"名称",
  "ParameterSetting":"extension.project.disabled=projectId1,projectId2,projectId3",
```

`"ExtensionDesc":"`这是一个描述`",` `"OptionSetting":"`选项配置`",`

```json
  "DetailUrl":"https://www.aliyun.com/",
  "ExtensionCode":"ce4*********086da5",
  "-EventCategoryList":{
   "CategoryCode":"file-change",
```

`"CategoryName":"`文件变更事件"

```json
  },
  "HelpDocUrl":"https://www.aliyun.com/",
  "-BindEventList":{
```

`"EventName":"`文件提交前置事件`",`

```json
   "EventCode":"commit-file"
  },
  "ProjectTesting":13552
 },
 "RequestId":"0000-ABCD-EFG"
}
```

`XML` 格式 DataWorks

```xml
<Extension>
 <Status>0</Status>
 <ExtensionName>名称</ExtensionName>
<ParameterSetting>extension.project.disabled=projectId1,projectId2,projectId3</ParameterS ting>
```

`<ExtensionDesc>`这是一个描述`</ExtensionDesc>`

```xml
 <OptionSetting>选项配置</OptionSetting>
 <DetailUrl>https://www.aliyun.com/</DetailUrl>
 <ExtensionCode>ce4*********086da5</ExtensionCode>
 <-EventCategoryList>
  <CategoryCode>file-change</CategoryCode>
```

`<CategoryName>`文件变更事件`</CategoryName>`

```xml
 </-EventCategoryList>
 <HelpDocUrl>https://www.aliyun.com/</HelpDocUrl>
 <-BindEventList>
```

`<EventName>`文件提交前置事件`</EventName>`

```xml
  <EventCode>commit-file</EventCode>
 </-BindEventList>
 <ProjectTesting>13552</ProjectTesting>
</Extension> <RequestId>0000-ABCD-EFG</RequestId>
```

#### GetOptionValueForProject

调用GetOptionValueForProject接口，获取扩展程序选项配置在项目空间下的配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 否 | default | 区域ID，为固定值default 。 |
| Extension Code | Strin g | Body | 否 | ce4*********086da5 | 扩展程序唯一编码 |
| ProjectId | Strin g | Body | 否 | 234 | 工作空间的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E6F0DBDD- 5AD**** | 请求ID。 |
| OptionValue | String | {"cuNumber":"0"} | 示例中的cuNumber是自定义的Key。 |

DataWorks

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetOptionValueForProject
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"E6F0DBDD-5AD****",
 "OptionValue":"{\"cuNumber\":\"0\"}"
}
```

`XML` 格式

```xml
<RequestId>E6F0DBDD-5AD****</RequestId> <OptionValue>{&quot;cuNumber&quot;:&quot;0&quot;}</OptionValue>
```
