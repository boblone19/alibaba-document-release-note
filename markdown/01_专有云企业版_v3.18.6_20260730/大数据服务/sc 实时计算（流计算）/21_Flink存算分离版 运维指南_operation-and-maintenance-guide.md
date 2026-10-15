---
title: "实时计算（流计算） Flink存算分离版 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 50
source_pdf: "21_Flink存算分离版 运维指南_operation-and-maintenance-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/operation-and-maintenance-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） Flink存算分离版 运维指南

实时计算（流计算）

## 作业运维

### 登录实时计算作业运维平台

**前提条件**

完成作业的开发和部署。相关操作，请参见《Flink存算分离版用户指南》。 作业状态为**运行中**。

**操作步骤**

1. 登录实时计算开发控制台。
登录步骤请参见《Flink存算分离版用户指南》中《登录实时计算开发控制台》章节。
2. 在左侧导航栏，单击**作业运维**。
3. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
4. 在不同页签，查看不同运维信息。

**后续步骤**

您可以单击作业列表右侧向右的箭头，展开作业列表，即关闭运维界面。此外，您也可以单击作业列表右侧向左的箭头展开运维界面。

### 修改作业状态

**前提条件**

完成作业和部署的创建。

**操作步骤**

1. 登录实时计算作业运维平台。
2. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
3. 根据需要单击以下按钮，修改作业状态。
其中，每个按钮的含义如下表所示。 实时计算（流计算）

| 操作名称 | 说明 |
|---|---|
| 启动 | 启动作业。 |
| 停止 | 停止作业。 |
| 创建快照 | 创建一个当前时刻的作业快照。 |
| 删除 | 删除作业。只能删除当前状态不为运行中的作业。 |

### 管理作业版本

本文将从对比作业版本、回滚作业版本、锁定作业版本、删除作业版本四个方面为您介绍如何管理作业版本。

**背景信息**

在作业开发页面，单击**部署**作业上线后，就会自动生成一个新版本。您可以对比当前编辑版本和历史版本的差异，实现回滚历史版本作业信息的需求。

**对比作业版本**

仅支持SQL代码和作业配置内容的对比，有差异的内容就会被标记出来。
1. 登录实时计算开发控制台。
登录步骤请参见《Flink存算分离版用户指南》中《登录实时计算开发控制台》章节。
2. 在左侧导航栏，单击**SQL****开发**。
3. 双击目标作业名称。
4. 在页面右侧，单击**版本信息**。
5. 在目标版本号对应的**操作**列，单击**对比**。
6. 在左侧**选择版本**中选择目标对比版本。
实时计算（流计算）

**回滚作业版本**

您可以将作业**部署**上线后产生的目标版本的作业信息回滚到当前编辑版本，当前编辑版本为您现在正在编辑的作业。
1. 登录实时计算开发控制台。
登录步骤请参见《Flink存算分离版用户指南》中《登录实时计算开发控制台》章节。
2. 在左侧导航栏，单击**SQL****开发**。
3. 双击目标作业名称。
4. 在页面右侧，单击**版本信息**。
5. 在目标版本号对应的**操作**列，选择**更多** > **回滚**。
6. 在弹出的对话框，单击**回滚**。
实时计算（流计算）

**锁定作业版本**

系统最多支持50个作业版本，超过50个后，系统会自动删除最旧的版本。您可以通过锁定指定版本，保证该版本不会被自动删除。
1. 登录实时计算开发控制台。
登录步骤请参见《Flink存算分离版用户指南》中《登录实时计算开发控制台》章节。
2. 在左侧导航栏，单击**SQL****开发**。
3. 双击目标作业名称。
4. 在页面右侧，单击**版本信息**。
5. 在目标版本号对应的**操作**列，选择**更多** > **锁定**。
锁定成功后，页面上方会弹出锁定成功的信息，且作业版本号前面会显示图标。 实时计算（流计算）

**说明**

不能删除锁定的作业版本，您需要先解锁再删除。如果您需要解锁，则需要选择**更多** > **解锁**。

**删除作业版本**

您可以删除一些您不需要的作业版本。
1. 登录实时计算开发控制台。
登录步骤请参见《Flink存算分离版用户指南》中《登录实时计算开发控制台》章节。
2. 在左侧导航栏，单击**SQL****开发**。
3. 双击目标作业名称。
4. 在页面右侧，单击**版本信息**。
5. 在目标版本号对应的**操作**列，选择**更多** > **删除**。
6. 在弹出的对话框，单击**删除**。

### 状态总览

本文为您介绍如何查看实时计算作业的状态。

**操作步骤**

1. 登录实时计算作业运维平台。
2. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
3. 单击**状态总览**页签。

**当前作业**

| 参数 | 说明 |
|---|---|
| 运行时长 | 作业启动后运行时长。 |
| 重启次数 | 作业重启的次数。 |

实时计算（流计算）

| 操作 | 作业详情：查看作业配置，与部署详情页面一致，包括基础配置、资源配置、运行参数配置、日志配置信息。 Flink UI：跳转到Flink Dashboard。 |
|---|---|
| Used/Total Slots | 使用任务槽占比。 |
| 启动时间 | 作业启动时间。 |
| 结束时间 | 作业最后一次修改时间。 |

**运行图**

运行图描述的是实时计算底层计算逻辑的执行图，每个组件代表不同的Task，数据流类似于任意有向无环图（DAG），每个数据流从一个或多个数据源开始，流向一个或多个数据结果表结束。为了更高效地分布式执行，实时计算底层会尽可能地将Operator的Subtask链接（Chain）在一起形成 Task（Operator Chain）。每个Task在一个线程中执行。 将Operators链接成Task，优化了以下问题： 减少线程之间的切换。 减少消息的序列化/反序列化。 减少数据在缓冲区的交换。 减少延迟的同时提高整体的吞吐量。 Operator代表的是每个计算逻辑的算子，而Task代表的是多个Operator的集合。为方便您更好地理解，我们把底层计算逻辑抽象成为视图，如下图所示。 可进行**专业模式**/**常规模式**切换。专业模式显示Backpressured及Busy情况。

**历史运行作业**

查看实例创建时间、停止时间、状态信息。 实时计算（流计算） 作业运行状态包括： RUNNING：按作业配置定义，启动作业。 CANCELLED：停止任何正在运行的作业。 SUSPENDED：先对当前运行的作业创建Savepoint，再停止作业。 FINISHED：作业运行完成。 TRANSITIONING：作业处于向期望状态的过渡阶段。 FAILED：作业向期望状态转换失败，需要手动处理。

### 运行事件

本文为您介绍如何查看作业运行事件。

**背景信息**

在作业的生命周期包括创建、运行、失败、完成、调度、取消中、已取消等阶段，会输出相关的事件信息， 可以从事件信息来初步判断作业是否正常运行。

**操作步骤**

1. 登录实时计算作业运维平台。
2. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
3. 单击**运行事件**。
运行事件页面默认展示信息发生的时间、信息内容和操作，其中**操作**列可以执行以下动作：
**复制信息**：单击**复制作业**，可以复制出事件的概要信息。
**作业详情**：选择**更多** > **作业详情**，可以查看作业实例产生事件的详细信息，包括**基础配置**、**资源配**
置、**运行参数配置**和**日志配置**等。
**搜索该作业事件**：选择**更多** > **搜索该作业事件**，展示当前事件对应的作业实例运行期间的事件。

### 状态集管理

系统检查点（Checkpoint）和作业快照（Savepoint）统称为状态集。本文为您介绍如何管理作业的状态集，包括创建、查看、删除和从指定状态恢复。

**背景信息**

| 概念 | 详情 |
|---|---|
| 系统检查点 （对应Apache Flink中的 Checkpoint） | 生命周期完全由Flink系统管理，您可以配置系统检查点间隔、系统检查点超时时间和两次系统检查点间最短间隔，并查看其生成情况。但无法手动创建和删除系统检查点，作业会默认保留一个系统检查点作为作业恢复时可选择的状态集中的一部分。 |

实时计算（流计算）

| 作业快照 （对应Apache Flink中的 Savepoint） | 生命周期完全由用户管理，具体表现在以下方面： 由用户在作业运行中或者结束时触发，或使用VVP平台进行单次或者定时触发。 删除也是由用户手工或使用VVP平台进行单次或者定时触发完成。 在作业启动时，可以基于某个作业快照进行作业状态恢复。 说明当配置为定时生成或清理时，系统是根据用户配置的规则进行，因此也属于用户管理。 |
|---|---|

**查看状态集的总览、历史和配置信息**

1. 登录实时计算作业运维平台。
2. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
3. 单击**状态集管理**页签。
4. 您可以进行以下操作。
总览

| 区域 | 总览信息 |
|---|---|
| 系统检查点 | 可以查看系统检查点信息，包括快照ID、完成时间、持续时间。 |
| 作业快照 | 可以查看上次成功和失败的作业快照信息，包括快照ID、完成时间、持续时间或失败时间。 |

历史

| 区域 | 总览信息 |
|---|---|
| 系统检查点 | 可以查看系统检查点的生成历史，包括检查点ID、状态、生成时间、生成耗时、增量存储大小和全量存储大小。 |
| 作业快照 | 可以查看作业快照的生成历史，包括快照ID、状态、快照类型、来源与备注、生成时间、生成耗时和相关操作（复制hdfs地址、从该快照恢复作业、删除此快照）。 |

配置您可以在此页签下配置定时自动创建作业快照和配置作业快照自动清理规则。 实时计算（流计算） 配置定时自动创建作业快照 a. 在**配置**页签，打开**作业快照定时自动生成**开关。 b. 单击**快捷设置**，在下拉列表中选择合适的时间设置为周期。

**说明**

最小间隔为10分钟。如果输入的Cron表达式小于10分钟，则系统默认按10分钟触发。 c. 单击**保存更改**。 d. （可选）如需重新设置，单击**重置**，会直接关闭**作业快照定时自动生成**功能。 配置作业快照自动清理规则

**重要**

快照清理会根据个数或保存时长来一同决定，满足其中一个条件即会被清理。 快照清理不包含手动点击触发生成的作业快照，此类快照只能在快照查看页面手动删除。 a. 在**配置**页签，打开**作业快照定时自动清理**开关。 b. 按需配置**历史快照保存个数**和**历史快照保存最长时间（单位：小时）**。 c. 单击**保存更改**。 d. （可选）如需重新设置，单击**重置**，会直接关闭**作业快照定时自动清理**功能。

**手动创建与删除作业快照**

**说明**

仅**运行中**的作业支持手动创建作业快照。
1. 进入目标作业快照创建界面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。 iii. 在**作业运维**页面右上角，单击**创建快照**。
2. 选择快照格式，并填写快照描述。
实时计算（流计算）
3. 单击**创建**。
您可以在作业运维界面选择**状态集管理** > **历史**页签，从**作业快照**列表中找到目标快照。在目标快照的操作列，选择**更多** > **删除此快照**。

**从（其他作业）指定快照恢复作业**

**说明**

仅**已停止**的作业支持从指定快照恢复作业。如果您的作业为**运行中**，则需要先停止作业。
1. 定位目标作业快照。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。 iv. 在**作业快照**列表中，找到目标快照。
2. 在目标快照**操作**列，选择**更多** > **从该快照恢复作业**。
3. 在**作业启动**配置对话框中选择**从其他作业恢复**选项，选择作业和快照配置作业启动信息。
4. 单击**启动**。

### 作业探查

#### 查看启动和运行日志

在作业为运行状态时，您可以查看其启动日志和运行日志。本文为您介绍如何查看启动日志和运行日志。

**背景信息**

| 类型 | 详情 |
|---|---|

实时计算（流计算）

| 启动日志 | Flink作业启动之后的日志，即从Flink环境被初始化一直到Job Manager被启动起来的中间日志。 说明启动日志中不包含调度日志，需要在运行事件中去查看相应的日志信息。例如资源不足、交换机IP不足都属于调度方面的问题。 |
|---|---|
| 运行日志 | Flink的Job Manager和Task Managers的日志可以在作业日志页面查看，也可以在Flink UI界面查看。 |

**前提条件**

作业为运行状态。

**注意事项**

支持日志分页，每页显示1 MB，大概会显示8000~9000行日志，基本可以帮您排查错误。如果在第一页还未定位到问题，请注意切换日志查看页码。

**查看启动日志**

1. 进入**作业运维**页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**作业探查**页签，单击左侧的**启动日志**，即可查看启动日志。

**查看运行日志**

**在作业日志页面查看运行日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**作业探查**页面的**运行日志**页签，单击**作业**右侧的下拉框，选择正在运行作业。
实时计算（流计算）
3. 查看Job Manager和Task Managers日志。
查看Job Manager日志在**Job Manager**页签下，单击**日志**。 查看Task Managers日志 a. 在**运行****Task Managers**页签下，单击**Path, ID**。 实时计算（流计算） b. 单击**日志**。

**在Flink UI页面查看运行日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**状态总览**页签下的**操作**行，单击**Flink UI**，默认进入**Apache Flink Dashboard**的**Overview**页
面。

**说明**

作业状态为**运行中**才出现**Flink UI**入口。
3. 在左侧导航栏，单击**Task Managers**或**Job Manager**。
单击**Task Managers** 后，单击目标**Path, ID**，在**logs**页签查看作业Task Manager日志。 单击**Job Manager**后，在**Logs**页签，查看作业Job Manager日志。

#### 查看运行异常日志

在作业启动或者运行异常时，您可以查看运行异常日志进行问题排查。本文为您介绍如何查看Job Manager 异常、失效Task Managers日志和慢Checkpoint对应的Task Managers日志。

**背景信息**

| 类型 | 详情 |
|---|---|
| Job Manager异常 | 如果作业出现Failover，导致作业运行失败，则需要查看Job Manager异常。 说明如果Job Manager都没启动起来，不属于Job Manager异常，需要在启动日志中去查看。 |

实时计算（流计算）

| 失效Task Managers日志 | 运行状态为正常的作业，不会有失败TM。但是对于风险等级较高的，可能有失败的TM，但 TM又被拉起了，这时可以查看失败的TM归档日志去定位可能的原因。 说明只有开启了日志归档才能查看失效Task Managers日志，并且只能查看日志归档中配置的保留天数之内的失效Task Managers日志。 |
|---|---|
| 慢Checkpoint对应的Task Managers 日志 | 作业运行过程中，如果某个Checkpoint运行耗时较长，您需要查看其具体的原因，则可以查看其关联的TM的日志。 |

**前提条件**

作业实例为运行状态。

**注意事项**

支持日志分页，每页显示1 MB，大概会显示8000~9000行日志，基本可以帮您排查错误。如果在第一页还未定位到问题，请注意切换页码查看日志。

**查看Job Manager异常**

1. 进入**作业运维**页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**作业探查**页签，选择左侧的**异常信息**页签后，查看Job Manager异常信息。

**说明**

在**异常历史**中，您可以查看近7天内产生的异常信息，并过滤异常类型后查看历史异常。

**查看失效Task Managers日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**作业探查**页签，选择**运行日志**后，选择正在运行的作业实例。
3. 单击**失效****Task Managers**页签，查看失效Task Managers日志。

**定位慢Checkpoint并查看对应Task Managers的日志**

1. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 查看慢Checkpoint日志信息。
i. 在**作业探查**页签，单击**Checkpoints**页签，单击**Checkpoints****历史**。 实时计算（流计算） ii. 查看**End to End Duration**列下的值，确认慢Checkpoint对应的ID。 iii. 单击慢Checkpoint对应的ID左侧的 ，确认慢Checkpoint对应的Operators节点。 iv. 单击Operators节点左侧的 ，展开查看每个SubTasks的情况。 v. 单击慢Checkpoint对应的SubTasks节点对应的**ID**。 vi. 在跳转页面的**运行** **Task Managers >** **日志**页签下，查看慢Checkpoint日志信息。

#### 查看历史作业实例日志

实时计算（流计算） 当Flink UI无法打开或需分析历史作业运行问题时，您可以查看历史作业实例日志定位问题。本文介绍如何

**背景信息**

如果出现以下情况，则您需要查看历史作业实例的日志： 您需要查看、搜索和分析历史作业实例的运行日志（系统默认保留最近5 MB大小的运行日志）。 Flink UI无法打开，需要查看Job Manager日志定位问题。

**前提条件**

查看历史作业实例日志需要您在日志配置中已打开日志归档功能。默认已开启日志归档功能，归档日志有效期7天。

**注意事项**

当日志文件达到指定大小时，系统将默认自动归档日志，并定期清理超过归档有效期的日志文件。作业停止后，未清理的归档日志将被保留下来，不会自动进行清理。若作业被删除，则相应的日志也将随之删除。 日志配置中默认会保留2个文件，每个文件大小为5 MB，不建议您修改该值。 实时计算（流计算）

**说明**

图片上的文件个数不包括正在写的文件，即如果这里配置为1，则最多会保存2个文件，一个保存在内存中，一个保存在您的本地磁盘中。

**在作业日志界面查看**

1. 进入作业运维页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**作业探查**页签，单击左侧**运行日志**。
3. 单击**作业**右侧的下拉框，选择历史运行作业。
4. 查看Job Manager和Task Managers日志。
在**Job Manager**或**Task Managers**页签，分别单击对应的日志名称，进行查看。

#### 修改运行作业日志级别

当INFO级别的日志无法满足您定位问题的需求时，您可以修改打印日志的级别为DEBUG。本文介绍如何动态修改日志级别及使用限制和注意事项。

**背景信息**

系统支持的日志级别从低到高的顺序与下面表格内容中的前后顺序一致。

| 级别 | 详情 |
|---|---|
| DEBUG | 系统运行状态的信息。 |
| INFO | 重要或者您感兴趣的信息。 |

**使用限制**

只支持设置为INFO或DEBUG，不支持设置为其他级别，以避免级别设置太高导致在日志中定位不到原因的问题。 实时计算（流计算） 支持修改整个JM的日志级别。 支持修改单个TM日志级别，不能一次性修改所有TM日志级别。如果需要修改所有TM日志级别，则需要您进行单独配置。

**注意事项**

日志级别修改为DEBUG后，会打印DEBUG、INFO、WARN、ERROR级别的日志。 日志级别修改为INFO后，只会打印INFO、WARN、ERROR级别的日志。 修改日志级别后，只会影响新输出的日志，之前已输出的日志不会受到影响。 DEBUG日志的开启会对作业性能造成少许影响。如果您没有定位问题的必要，建议将日志级别设置为 INFO。

**操作步骤**

1. 进入作业运维页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 在**作业探查**页签，单击左侧**运行日志**，选择正在运行的作业实例。
3. 修改Job Manager或Task Managers日志级别。

**修改Job Manager日志级别**

a. 在**Job Manager**页签，单击**日志**。 b. 单击**日志级别**右侧的**编辑**。 c. 单击**确定**。 d. 在下拉框中选择目标日志级别。 e. 单击**确定**。

**修改Task Managers日志级别**

a. 在**运行****Task Managers**页签，单击**Path, ID**。 实时计算（流计算） b. 单击**日志**。 c. 单击**日志级别**右侧的**编辑**。 d. 单击**确定**。 e. 在下拉框中选择目标日志级别。 f. 修改日志级别后，单击**确定**。

### 作业调优

#### 配置自动调优

Flink支持智能调优和定时调优两种调优模式。本文为您介绍如何配置智能调优和定时调优，以及配置过程中的注意事项。

**背景信息**

通常，您需要花费大量的时间进行作业调优。例如，新上线一个作业时，需要考虑如何配置该作业的资源、 并发个数、Task Manager个数及大小等。此外，作业运行过程中，还需要考虑如何调整作业资源，使作业处于最高资源利用率；作业出现反压或延时增大的情况时，需要考虑如何调整作业配置等。您可以根据以下信息，选择合适的调优模式。

| 调优模式 | 适用场景 | 使用优势 | 相关文档 |
|---|---|---|---|
| 未开启 （默认模式） | 不配置智能调优或定时调优，但想简单地优化下作业资源。 | 可以直接使用未开启状态下的资源建议来手动调整作业资源。 因为资源调优系统根据作业运行情况，给出资源调整建议，但是并不自动应用优化建议，需要您根据情况手动处理。 | 无。 |

实时计算（流计算）

| 智能调优 | 某作业X，使用资源30 CU，上线平稳运行一段时间后，发现在 Source无延迟、无反压的情况下，作业的CPU和内存使用率有时会很低。 此时如果您不想人工调节资源， 需要系统自动完成资源的调节， 可以使用智能调优功能。系统将在资源使用率比较低时，自动降低资源配置，在资源使用率提高达到一定阈值时，再自动提高资源配置。 | 帮您更合理地调整作业并行度和资源配置。 全局优化您的作业，解决作业吞吐量不足、全链路存在反压和资源浪费等各种性能调优问题。 | 默认的智能调优行为，请参见智能调优默认调优行为开启智能调优功能，请参见开启并配置智能调优。 |
|---|---|---|---|
| 定时调优 | 某作业Y，根据业务的特点，有明显的时间区间特征。例如，全天早09：00~19：00是业务高峰，19：00到第二天09：00是业务低峰。 此时您可以使用定时调优功能， 在高峰时间段使用30 CU，在业务低峰时使用10 CU。 说明您需要明确知道各个时间段的资源使用情况。 |  | 配置定时调优策略，请参见开启并配置定时调优。 |

**使用限制**

在开启unaligned checkpoint时，不支持调整并发。 智能调优不支持Session集群部署的作业。 智能调优无法解决流作业所有的性能瓶颈。 流作业性能问题是由上下游共同决定的，如果是Flink出现了瓶颈，可以通过Flink资源调优解决。但调优策略对作业的处理模式是基于一定的假设的。例如，流量平滑变化、不能有数据倾斜、每个算子的吞吐能力能够随并发度的升高而线性拓展。当业务逻辑严重偏离以上假设时，作业可能会存在异常。例如： 无法触发修改并发度的操作、作业不能达到正常状态和作业持续重启等。 自定义标量函数UDF、自定义聚合函数UDAF或自定义表值函数UDTF性能问题。 智能调优无法识别外部系统的问题。如果出现外部系统问题，您需要自行解决。 外部系统故障或访问变慢时，会导致作业并行度增大，加重外部系统的压力，导致外部系统雪崩。常见的外部系统问题如下： 数据总线DataHub分区不足或消息队列MQ吞吐量不足。 Sink性能问题。 云数据库RDS死锁。

**注意事项**

智能调优触发后需要重启作业，因此会导致作业短暂停止处理数据。 实时计算（流计算） 连续两次智能调优触发间隔为10分钟，您可以通过cooldown.minutes参数来调节触发智能调优的时间间隔。 如果您使用了DataStream作业或SQL自定义的Connector，请确认作业代码中未配置作业并行度，否则智能调优将无法调整作业资源，即智能调优配置无法生效。 新策略的触发时间和已有策略的触发时间间隔不能在半小时之内，否则新策略无法创建。

**智能调优默认调优行为**

如果您开启了智能调优，则系统默认会从并发度和内存两个方面为您进行智能调优： 智能调优会调整作业的并发度来满足作业流量变化所需要的吞吐。智能调优会监控消费源头数据的延迟变化情况、TaskManager（TM） CPU实际使用率和各个算子处理数据能力来调整作业的并发度。详情如下： 作业延迟Delay指标正常（不超过60s），不修改当前作业并发。 作业延迟Delay指标超过默认阈值60s，分以下两种情况来调整并发度： 延迟正在下降，不进行并发度调整。 延迟增加并且连续上升3分钟（默认值），默认调整作业并发度到当前实际TPS的两倍，但不超过设置的最大资源（默认值为64 CU）。 作业不存在延迟指标。 作业某VERTEX节点连续6分钟实际处理数据时间占比超过80%，调大作业并发度使得SLOT使用率降低到50%，但不超过设置的最大资源（默认为64 CU）。 所有TM的平均利用率连续6分钟超过80%，调高并发度使TM的CPU使用率降低到50%。 所有TM的最大CPU使用率连续24小时低于20%，且VERTEX的实际处理数据时间低于20%时，调低作业的并发度使CPU和VERTEX实际处理的时间占比提高到50%。 智能调优也会监控作业的内存使用和Failover情况，来调整作业的内存配置。详情如下： 在JobManager GC频繁或者发生OOM异常时，会调高JM的内存，默认最大调整到16 GiB。 在TM GC频繁或者发生OOM异常、HeartBeatTimeout异常时，会调高TM的内存，默认最大调整到 16 GiB。 在TM内存使用率超过95%时，会调大TM的内存。 在TM的实际内存使用率连续24小时低于30%时，降低TM内存的配置，默认最小调整到1.6 GiB。

**开启并配置智能调优**

1. 进入作业运维页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 打开智能调优模式。
i. 在**自动调优**页签，单击**调优配置**。 ii. 单击**当前应用模式**右侧的**编辑**。 iii. 在**当前应用模式**的下拉列表中，选择**智能调优**。 iv. 单击**保存**。 开启后，您会看到作业名称左侧的SQL图标会变为 。 如果您需要关闭已开启的智能调优，则可以在**调优配置** > **当前应用模式**中，选择**未开启**，单击**保存**。
3. 填写智能调优相关参数。
i. 在**智能模式设置**页签，单击**编辑**。 实时计算（流计算） ii. 填写智能调优配置信息。 相关的参数详情如下表所示。

| 参数 | 说明 |
|---|---|
| 调整间隔时间（分钟） | 作业调优重启生效一次之后，下一次再进行调优的时间间隔。 |
| 最大资源限制 | 作业自动调整资源可以扩容的最大资源上限，单位为CU。 |

实时计算（流计算）

| 更多参数配置 | 您可以配置的参数列表如下： parallelism.scale-up.interval ：两次并发度向上调整操作的最短间隔时间，默认值为 6min。 parallelism.scale-down.interval ：两次并发度向下调整操作的最短间隔时间，默认值为24h。 mem.scale-down.interval：调低内存时最小触发时间间隔。 默认值为25小时。25小时内，检测内存使用率如果小于阈值，则会降低内存，或建议降低内存。 parallelism.scale.max：并发度向上调整时，最大并发限制。 默认值为-1，表示最大并发没有限制。 parallelism.scale.min：并发度向下调整时，最小并发限制。 默认值为1，表示最小并发为1。 delay-detector.scale-up.threshold：可以容忍的最大延迟阈值。基于消费数据源头的延迟，来衡量作业处理吞吐的能力。 默认值为1分钟。当数据处理能力不足导致延迟超过1分钟，则会通过Scale Up方式来提高作业的吞吐能力，Scale Up方式包括增加并发或者拆Chain，或建议Scale Up。 slot-usage-detector.scale-up.threshold：当VERTEX处理数据时间占比大于该值时，触发调大并发度的操作。 默认值为0.8。监控数据处理节点（不包括Source节点）空闲时间。当持续大于阈值0.8时，降低作业的并行度以降低资源使用，或建议Scale Up。 slot-usage-detector.scale-down.threshold：当VERTEX处理数据时间占比大于该值时，触发调小并发度的操作。 默认值为0.2。监控数据处理节点（不包括Source节点）空闲时间。当持续小于阈值0.2时，提升作业的并行度以提升处理能力，或建议Scale Down。 slot-usage-detector.scale-up.sample-interval：监控slot空闲指标的时间间隔，以便计算该时间间隔的平均值。 默认值为3分钟，与slot-usage-detector.scale-up.threshold和slot-usage- detector.scale-down.threshold结合使用。当3分钟内的空闲时间平均值大于0.8或者小于0.2时，则进行scale-up或者scale-down。 resources.memory-scale-up.max：调整单个Task Manager和Job Manager的内存时，能调整到的最大值。 默认值为16 GiB。TM和JM进行智能调优或调大并发时，内存的上限为16 GiB。 |
|---|---|

iii. 单击**保存**。

**开启并配置定时调优**

1. 进入作业运维页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。
2. 打开智能调优模式。
i. 在**自动调优**页签，单击**调优配置**。 ii. 单击**当前应用模式**右侧的**编辑**。 iii. 在**当前应用模式**的下拉列表中，选择**定时调优**。 iv. 单击**保存**。
3. 单击**新建调优策略**。
i. 在**定时模式设置**页签，单击**新建调优策略**。 实时计算（流计算） ii. 填写基础配置信息。 配置说明如下表所示。

| 配置 | 说明 |
|---|---|
| 触发周期 | 您可以选择为单次触发、每天、每周和每月。当选择为每周和每月时，您还需要指定对应的生效日期范围。 |
| 生效时间 | 选择具体的生效时间。 |
| 策略描述 | 填写策略的描述信息。 |

iii. 单击**下一步**。
4. 配置资源设置信息。
您可以单击对话框右上角**从运行历史资源加载**获取历史资源配置，或者自定义资源配置，详情请参见配置作业资源。
5. 单击**确定**。
策略创建完成后，会在触发时间生效。您可以在对应策略的**操作**列下，编辑、删除或禁用该策略。

#### 配置作业资源

作业启动前或者作业上线后，您可以配置和修改作业资源，本文为您介绍如何配置和修改作业资源。 实时计算（流计算）

**使用限制**

仅SQL作业支持配置专家模式。

**操作步骤**

1. 进入资源配置入口页面。
ii. 在**作业运维**页面，单击目标作业名称，默认展开**部署详情**页面。 iii. 在**部署详情**页签，单击**资源配置**区域右侧的**编辑**。
2. 修改作业资源信息。

**基础模式（粗粒度）**

粗粒度是一种静态资源分配方式，您只需要给定每个TM的启动所需要的总资源（CPU和JVM总内存）， 系统会根据taskmanager.numberOfTaskSlots的值均匀分配所有资源。对于大多数简单作业，粗粒度即可满足要求。

| 配置项 | 说明 |
|---|---|
| 并发度 | 作业全局并发数。 |
| JobManager CPU | 根据Flink最佳实践，单个JM内存资源需要至少配置为0.25 core和1 GiB， 才能保证作业稳定运行。 |
| JobManager Memory | 单位为GiB，例如：4 GiB。最小值为1 GiB。 |
| TaskManager CPU | 根据Flink最佳实践，单个TM内存资源需要至少配置为1 core和4 GiB，才能保证作业稳定运行。 |
| TaskManager Memory | 单位为GiB，例如：4 GiB。最小值为1 GiB。 |
| 每个TaskManager Slot数 | 请填写TM的Slot数。 |

**专家模式（细粒度）**

**说明**

仅SQL作业支持配置专家模式。 细粒度是一种动态资源分配方式，您可以配置每个Task（甚至算子）所需要的资源，Flink会计算出每个 Slot需要的资源规格大小，动态的从可用资源池去申请完全匹配的TM和SLOT。对于复杂作业，粗粒度可能导致资源利用率低，因此需要细粒度资源对每个算子进行精细资源控制，从而提高资源使用率，满足作业吞吐的要求。 关于TM、JM、TASK或SLOT等概念，详情请参见Flink架构。

| 配置项 | 说明 |
|---|---|

实时计算（流计算）

| JobManager CPU | 根据Flink最佳实践，单个JM内存资源需要至少配置为0.25 core和1 GiB，才能保证作业稳定运行。 |
|---|---|
| JobManager Memory | 单位为GiB，例如：4 GiB。最小值为1 GiB。 |
| 配置计划 | 配置计划即配置SLOT资源，填写步骤和说明如下： i. 单击立刻获取。 ii. 单击SLOT框上的图标，修改SLOT配置信息。 此处设置的并发数为整个作业全局的并发数。设置完成后，系统将自动进行以下操作： 系统将自动为每个VERTEX设置相同的并发数。 系统会根据作业的计算逻辑按需自动生成Statebackend、Python和 Operator所需的内存，无需您手动进行配置。 系统默认会按照一个SLOT所需的全部内存大小（即Heap Memory、 Off-heap Memory、Statebackend、Python和Operator内存之和），以1:4的比例，生成一个SLOT所需的CPU。 说明建议在有明确异常或者需求时，再调整Heap Memory和Off-heap Memory的大小，例如作业出现OOM或严重GC等。因为在作业正常运行时，调整Heap Memory和Off-heap Memory的大小，不会明显改变作业的吞吐量。 iii. 单击VERTEX框上的图标，按需为某个VERTEX设置并发数。 |

实时计算（流计算）

|  | iv. 修改Operator并发数和Chain策略。 Chain策略说明如下： ALWAYS：始终可以和上下游算子Chain一起。 HEAD：当前算子作为Chain的头节点，只和上游算子断开Chain，下游节点仍和当前算子Chain在一起。 NEVER：当前算子不会与上下游算子进行Chain。 说明建议Source节点并发度和分区数成比例，即并发度数能整除分区数。例如Kafka有16个分区，则并发度建议设置为16、 8或4，这样可以避免数据倾斜。同时Source节点的并发度不宜设置太小，避免一个Source需要读取太多数据，导致出现入口瓶颈，影响作业吞吐。 |  |  |
|---|---|---|---|
|  |  | 说明建议Source节点并发度和分区数成比例，即并发度数能整除分区数。例如Kafka有16个分区，则并发度建议设置为16、 8或4，这样可以避免数据倾斜。同时Source节点的并发度不宜设置太小，避免一个Source需要读取太多数据，导致出现入口瓶颈，影响作业吞吐。 |  |
| 单击保存。 |  | 建议按需配置除Source外的其他节点的并发度。流量大的节点，并发设置大一些；流量小的节点，并发设置小一些。 |  |

v. 单击**确定**。 本文将从作业配置和Flink SQL优化两方面为您介绍如何提升Flink SQL作业性能。

**作业配置优化推荐方案**

资源优化技巧 VVP中限制了JobManager和TaskManager的CPU的实际使用大小，配置了多少个CPU，最大就只能使用多少个CPU。因此在资源优化时，建议： 作业并发大时：在作业的**资源配置**中，增加JobManager的资源，提高CPU和内存的大小，例如： Job Manager CPUs设置为4。 Job Manager Memory设置为8 GiB。 作业拓扑较复杂时，在作业的**资源配置**中，增加TaskManager的资源，提高CPU和内存的大小，例如： Task Manager CPUs设置为2。 Task Manager Memory设置为4 GiB。 不建议修改taskmanager.numberOfTaskSlots，保持默认值1。 提升吞吐和解决数据热点的推荐配置在作业**高级配置**的**更多****Flink****配置**里添加以下代码，详情请参见Group Aggregate优化技巧。

```
execution.checkpointing.interval: 180s state.backend: com.alibaba.flink.statebackend.GeminiStateBackendFactory table.exec.state.ttl: 129600000 table.exec.mini-batch.enabled: true table.exec.mini-batch.allow-latency: 5s table.optimizer.distinct-agg.split.enabled: true env.java.opts.taskmanager: -Xms4096m -XX:+UseParNewGC - XX:+UseCMSInitiatingOccupancyOnly -XX:CMSInitiatingOccupancyFraction=70 -verbose:gc - XX:+HeapDumpOnOutOfMemoryError -XX:+UseConcMarkSweepGC - XX:+UseCMSCompactAtFullCollection -XX:CMSMaxAbortablePrecleanTime=1000 -XX:+CMSClassU nloadingEnabled -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:SurvivorRatio=5 -XX:Pa rallelGCThreads=4
```

参数解释如下表所示。

| 参数 | 说明 |
|---|---|

实时计算（流计算）

| execution.checkpointing.interv al | Checkpoint间隔时间，单位为毫秒。 |
|---|---|
| state.backend | State backend的配置。 |
| table.exec.state.ttl | State数据的生命周期，单位为毫秒。 |
| table.exec.mini-batch.enabled | 是否开启minibatch。 |
| table.exec.mini-batch.allow- latency | 批量输出数据的时间间隔。 |
| table.optimizer.distinct- agg.split.enabled | 是否开启PartialFinal优化，解决COUNT DISTINCT热点问题。 |
| env.java.opts.taskmanager | 启动Java选项。 说明当源表为SLS时，不能设置该参数，否则会造成性能瓶颈。 |

**Group Aggregate优化技巧**

开启MiniBatch（提升吞吐） MiniBatch是缓存一定的数据后再触发处理，以减少对State的访问，从而提升吞吐并减少数据的输出量。 MiniBatch主要基于事件消息来触发微批处理，事件消息会按您指定的时间间隔在源头插入。 适用场景微批处理通过增加延迟换取高吞吐，如果您有超低延迟的要求，不建议开启微批处理。通常对于聚合场景，微批处理可以显著地提升系统性能，建议开启。 开启方式 MiniBatch默认关闭，您需要在作业**高级配置**中的**更多****Flink****配置**填写以下代码。

```
table.exec.mini-batch.enabled: true table.exec.mini-batch.allow-latency: 5s
```

参数解释如下表所示。

| 参数 | 说明 |
|---|---|
| table.exec.mini-batch.enabled | 是否开启mini-batch。 |
| table.exec.mini-batch.allow- latency | 批量输出数据的时间间隔。 |

开启LocalGlobal（解决常见数据热点问题） LocalGlobal本质上能够靠LocalAgg的聚合筛除部分倾斜数据，从而降低GlobalAgg的热点，提升性能。您可以结合下图理解LocalGlobal如何解决数据倾斜的问题。 实时计算（流计算） LocalGlobal优化将原先的Aggregate分成Local和Global两阶段聚合，即MapReduce模型中的 Combine和Reduce两阶段处理模式。第一阶段在上游节点本地攒一批数据进行聚合（localAgg），并输出这次微批的增量值（Accumulator）。第二阶段再将收到的Accumulator合并（Merge），得到最终的结果（GlobalAgg）。 适用场景提升普通聚合（例如SUM、COUNT、MAX、MIN和AVG）的性能，以及这些场景下的数据热点问题。 使用限制 LocalGlobal是默认开启的，但是有以下限制： 在minibatch开启的前提下才能生效。 需要使用AggregateFunction实现Merge。 判断是否生效观察最终生成的拓扑图的节点名字中是否包含GlobalGroupAggregate或LocalGroupAggregate。 开启PartialFinal（解决COUNT DISTINCT热点问题） 为了解决COUNT DISTINCT的热点问题，通常需要手动改写为两层聚合（增加按Distinct Key取模的打散层）。目前，实时计算提供了COUNT DISTINCT自动打散，即PartialFinal优化，您无需自行改写为两层聚合。PartialFinal和LocalGlobal的原理对比参见下图。 实时计算（流计算） LocalGlobal优化针对普通聚合（例如SUM、COUNT、MAX、MIN和AVG）有较好的效果，对于 COUNT DISTINCT收效不明显，因为COUNT DISTINCT在Local聚合时，对于DISTINCT KEY的去重率不高，导致在Global节点仍然存在热点问题。 适用场景使用COUNT DISTINCT，但无法满足聚合节点性能要求。

**说明**

不能在包含UDAF的Flink SQL中使用PartialFinal优化方法。 数据量较少的情况，不建议使用PartialFinal优化方法，浪费资源。因为PartialFinal优化会自动打散成两层聚合，引入额外的网络Shuffle。 开启方式默认不开启。如果您需要开启，则需要在作业**高级配置**中的**更多****Flink****配置**填写以下代码。

```
table.optimizer.distinct-agg.split.enabled: true
```

判断是否生效观察最终生成的拓扑图，是否由原来一层的聚合变成了两层的聚合。 AGG WITH CASE WHEN改写为AGG WITH FILTER语法（提升大量COUNT DISTINCT场景性能） 统计作业需要计算各种维度的UV，例如全网UV、来自手机客户端的UV、来自PC的UV等等。建议使用标准的AGG WITH FILTER语法来代替CASE WHEN实现多维度统计的功能。实时计算目前的SQL优化器能分析出Filter参数，从而同一个字段上计算不同条件下的COUNT DISTINCT能共享State，减少对State 的读写操作。性能测试中，使用AGG WITH FILTER语法来代替CASE WHEN能够使性能提升1倍。 适用场景对于同一个字段上计算不同条件下的COUNT DISTINCT结果的场景，性能提升很大。 原始写法

```
COUNT(distinct visitor_id) as UV1 , COUNT(distinct case when is_wireless='y' then v isitor_id else null end) as UV2
```

优化写法

```
COUNT(distinct visitor_id) as UV1 , COUNT(distinct visitor_id) filter (where is_wir eless='y') as UV2
```

**Flink SQL优化推荐方案**

TopN优化技巧高效去重方案高效的内置函数

**TopN优化技巧**

TopN算法当TopN的输入是非更新流（例如Source），TopN只有1种算法AppendRank。当TopN的输入是更新流时（例如经过了AGG或JOIN计算），TopN有3种算法，性能从高到低分别是：UpdateFastRank 、 UnaryUpdateRank和RetractRank。算法名字会显示在拓扑图的节点名字上。 实时计算（流计算） UpdateFastRank ：最优算法。 使用该算法需要具备2个条件： 输入流有PK（Primary Key）信息，例如ORDER BY AVG。 排序字段的更新是单调的，且单调方向与排序方向相反。例如，ORDER BY COUNT/COUNT_DISTINCT/SUM（正数）DESC。 如果您要获取到优化Plan，则您需要在使用ORDER BY SUM DESC时，添加SUM为正数的过滤条件，确保**total_fee**为正数。

```
insert
  into print_test
SELECT
  cate_id,
  seller_id,
  stat_date,
```

`pay_ord_amt --`不输出`rownum`字段，能减小结果表的输出量。

```
FROM (
    SELECT
```

`*,`

```
      ROW_NUMBER () OVER (
        PARTITION BY cate_id,
```

`stat_date --`注意要有时间字段，否则`State`过期会导致数据错乱。

```
        ORDER
          BY pay_ord_amt DESC
```

`) as rownum --`根据上游`sum`结果排序。

```
    FROM (
        SELECT
          cate_id,
          seller_id,
          stat_date,
```

`--`重点。声明`Sum`的参数都是正数，所以`Sum`的结果是单调递增的，因此`TopN`能使用优化算法， 只获取前`100`个数据。

```
          sum (total_fee) filter (
            where
              total_fee >= 0
          ) as pay_ord_amt
        FROM
          random_test
        WHERE
          total_fee >= 0
        GROUP
          BY cate_name,
          seller_id,
          stat_date,
          cate_id
      ) a
    ) WHERE
      rownum <= 100;
```

UnaryUpdateRank：性能仅次于UpdateFastRank的算法。使用该算法需要具备的条件是输入流中存在PK信息。 RetractRank：普通算法，性能最差，不建议在生产环境使用该算法。请检查输入流是否存在PK信息，如果存在，则可使用UnaryUpdateRank或UpdateFastRank算法进行优化。 TopN优化方法实时计算（流计算） 无排名优化 TopN的输出结果不需要显示rownum值，仅需在最终前端显示时进行1次排序，极大地减少输入结果表的数据量。无排名优化方法详情请参见Top-N。 增加TopN的Cache大小 TopN为了提升性能有一个State Cache层，Cache层能提升对State的访问效率。TopN的Cache命中率的计算公式如下。

```
cache_hit = cache_size*parallelism/top_n/partition_key_num
```

例如，Top100配置缓存10000条，并发50，当您的PatitionBy的Key维度较大时，例如10万级别时，Cache命中率只有**10000*50/100/100000=5%**，命中率会很低，导致大量的请求都会击中 State（磁盘），性能会大幅下降。因此当PartitionBy的Key维度特别大时，可以适当加大TopN的 Cache Size，相对应地也建议适当加大TopN节点的Heap Memory。

```
blink.topn.cache.size: 200000
```

默认10000条，调整TopN cache到200000，那么理论命中率能达到**200000*50/100/100000 =**
**100%**。
PartitionBy的字段中要有时间类字段例如每天的排名，要带上Day字段，否则TopN的最终结果会由于State TTL产生错乱。

**高效去重方案**

实时计算的源数据在部分场景中存在重复数据，去重成为了用户经常反馈的需求。实时计算有保留第一条 （Deduplicate Keep FirstRow）和保留最后一条（Deduplicate Keep LastRow）2种去重方案。 语法由于SQL上没有直接支持去重的语法，还要灵活地保留第一条或保留最后一条。因此我们使用了SQL的 ROW_NUMBER OVER WINDOW功能来实现去重语法。去重本质上是一种特殊的TopN。

```
SELECT * FROM (
   SELECT *,
    ROW_NUMBER() OVER (PARTITION BY col1[, col2..]
     ORDER BY timeAttributeCol [asc|desc]) AS rownum
   FROM table_name)
WHERE rownum = 1
```

| 参数 | 说明 |
|---|---|
| ROW NUMBER() _ | 计算行号的OVER窗口函数。行号从1开始计算。 |
| PARTITION BY col1[, col2..] | 可选。指定分区的列，即去重的KEYS。 |
| ORDER BY timeAttributeCol [asc\|desc]) | 指定排序的列，必须是一个时间属性的字段（即 Proctime或Rowtime）。可以指定顺序（Keep FirstRow）或者倒序 （Keep LastRow）。 |
| rownum | 仅支持 rownum=1 或 rownum<=1 。 |

如上语法所示，去重需要两层Query： i. 使用 `ROW_NUMBER()` 窗口函数来对数据根据时间属性列进行排序并标上排名。 当排序字段是Proctime列时，Flink就会按照系统时间去重，其每次运行的结果是不确定的。 当排序字段是Rowtime列时，Flink就会按照业务时间去重，其每次运行的结果是确定的。 ii. 对排名进行过滤，只取第一条，达到了去重的目的。 实时计算（流计算） 排序方向可以是按照时间列的顺序，也可以是倒序： Deduplicate Keep FirstRow：顺序并取第一条行数据。 Deduplicate Keep LastRow：倒序并取第一条行数据。 Deduplicate Keep FirstRow 保留首行的去重策略：保留KEY下第一条出现的数据，之后出现该KEY下的数据会被丢弃掉。因为STATE 中只存储了KEY数据，所以性能较优，示例如下。

```
SELECT * FROM (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY b ORDER BY proctime) as rowNum
  FROM T
```

)

```
WHERE rowNum = 1
```

以上示例是将T表按照b字段进行去重，并按照系统时间保留第一条数据。proctime在这里是源表T中的一个具有Processing Time属性的字段。如果您按照系统时间去重，也可以将proctime字段简化 proctime()函数调用，可以省略proctime字段的声明。 Deduplicate Keep LastRow 保留末行的去重策略：保留KEY下最后一条出现的数据。保留末行的去重策略性能略优于LAST_VALUE函数，示例如下。

```
SELECT * FROM (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY b, d ORDER BY rowtime DESC) as rowNum
  FROM T
```

)

```
WHERE rowNum = 1
```

以上示例是将T表按照b和d字段进行去重，并按照业务时间保留最后一条数据。rowtime在这里是源表T 中的一个具有Event Time属性的字段。

**高效的内置函数**

在使用内置函数时，您需要注意以下几点： 使用内置函数替换自定义函数实时计算的内置函数在持续的优化当中，请尽量使用内置函数替换自定义函数。实时计算对内置函数主要进行了如下优化： 优化数据序列化和反序列化的耗时。 新增直接对字节单位进行操作的功能。 KEY VALUE函数使用单字符的分隔符 KEY VALUE的签名： `KEYVALUE(content, keyValueSplit, keySplit, keyName)` ，当 keyValueSplit和KeySplit是单字符，例如，半角冒号（:）、半角逗号（,）时，系统会使用优化算法， 在二进制数据上直接寻找所需的keyName值，而不会将整个content进行切分，性能约提升30%。 LIKE操作注意事项

| 用 LIKE 'xxx%' 用 LIKE '%xxx' 。 用 LIKE '%xxx%' |  |  |
|---|---|---|
|  | LIKE '%xxx' |  |
|  | LIKE '%xxx%' |  |
| LIKE 'xxx' |  | ，等 |

实时计算（流计算） 如果需要匹配下划线（_），请注意要完成转义 LIKE '%seller/_id%' ESCAPE '/' 。下划线（_） 在SQL中属于单字符通配符，能匹配任何字符。如果声明为 LIKE '%seller_id%' ，则不单会匹配 `seller_id` ，还会匹配 `seller#id` 、 `sellerxid` 或 `seller1id` 等，导致结果错误。 慎用正则函数（REGEXP） 正则表达式是非常耗时的操作，对比加减乘除通常有百倍的性能开销，而且正则表达式在某些极端情况下可能会进入无限循环，导致作业阻塞，具体情况请参见Regex execution is too slow，因此建议使用 LIKE。 实时计算（流计算） 运维

## Flink应用运维

飞天基础运维控制台支持查看Flink应用产品实例详情。本文介绍如何查看Flink应用产品实例详情。

**查看Flink应用产品实例**

1. 登录飞天基础运维控制台。
i. 打开浏览器。 ii. 登录Apsara Uni-manager运维控制台。 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址后按回车键，输入正确的用户名和密码后，单击**账号登录**。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 iii. 在顶部菜单栏，单击**平台运维** > **飞天基础运维平台** > **资源管理**。
2. 查看Flink的产品实例详情。
i. 在左侧导航栏，选择**资源管理** > **产品集群运维**。 ii. 在**产品列表**下的**产品**|**集群**搜索框中搜索关键字**realtime-compute-flinkonoss**，单击目标集群右侧**操作**列的**集群详情**。 iii. 在**服务列表**页签下，单击右侧**操作**列的**详情**。 iv. 在**组件列表**下，单击目标组件名称，在右侧区域可查看组件的详细信息。示例图如下： 实时计算（流计算） 巡检

## Flink深度巡检

深度巡检覆盖并汇聚Flink的监控告警、资源水位与关键指标，可视化掌握平台运行健康状况，在发生重大问题甚至故障前，可以规避非预期的风险问题，保障稳定性。

**背景信息**

| 巡检项 |  | 检查说明 | 相关文档 |
|---|---|---|---|
| 集群巡检 |  | 日常维护、项目重保、确保管控组件状态正常，检查产品是否达到终态。 | 集群巡检 |
| 集群组件状态检查 |  | 检查集群组件是否正常启动运行。 | 集群组件状态巡检 |
| Flink资源使用 |  | 检查集群资源使用率是否在正常水位以内。 | Flink资源使用 |
| 流任务健康度检查 | Session和Job Pod 健康检查 | 检查流任务当前运行是否健康，是否有过失败现象。 | Session和Job Pod健康检查 |
|  | 确认任务在正常处理数据 | 检查流任务当前运行是否产出数据，是否有过失败现象。 | 确认任务在正常处理数据 |

**注意事项**

深度巡检摸底包括但不限于平台系统、硬件、库存、云平台用户实例使用、业务数据规模大小、业务请求压力等。

**集群巡检**

1. 登录飞天基础运维平台。
i. 打开浏览器。 ii. 登录Apsara Uni-manager运维控制台。 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址后按回车键，输入正确的用户名和密码后，单击**账号登录**。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 iii. 在顶部菜单栏，单击**平台运维**。 iv. 选择**飞天基础运维平台** > **资源管理**。
2. 查看Flink集群是否为**已达终态**状态。
i. 在左侧导航栏，单击**产品集群运维**。 ii. 在**产品列表**下的**产品**|**集群**搜索框中，搜索**realtime-compute-flinkonoss**。 iii. 查看目标集群的集群状态。 实时计算（流计算） 巡检
3. 确认巡检结果是否符合要求。
巡检结果要求：
**已达终态**状态：要求realtime-compute-flinkonoss集群状态无异常，可以正常使用。
**未达终态**状态：如果realtime-compute-flinkonoss集群状态异常，则需要查看该工作空间下的Pod为
何无法拉起。

**集群组件状态巡检**

1. 登录OPS1机器。
2. 执行以下K8s命令，查看集群组件状态。

```bash
kubectl get appinstance -nark-system -lproduct=realtime-compute | grep -v hdfs | grep -v sre-flink |grep -v ververica
```

3. 确认巡检结果是否符合要求。
巡检结果要求：查询结果中的所有app instance状态均为Ready。

**Flink资源使用**

1. 登录OPS1机器。
2. 执行以下K8s命令，查看Flink资源使用情况。

```bash
kubectl top node -l flinkonoss=true
```

3. 确认巡检结果是否符合要求。
巡检结果要求：CPU%和MEMORY%均不能超过90%。

**Session和Job Pod健康检查**

1. 使用用户账号登录实时计算开发控制台。
详情请参见**Flink****存算分离版****用户指南** > **登录实时计算开发控制台**章节。
2. 获取并记录目标Namespace名称和Workspace ID。
Namespace名称获取方法在**Workspace** **列表**下，找到目标Namespace名称即可。 实时计算（流计算） 巡检 Workspace ID获取方法单击目标Namespace名称操作列下的**控制台**，进入实时计算开发控制台。在顶部地址栏，获取 workspaces后的ID信息即可。
3. 登录OPS1机器。
4. 依次执行以下K8s命令，查看Session和Job Pod健康信息。
i. 执行以下命令，确认同时包含目标Workspace ID和Namespace的信息名称。

```bash
kubectl get ns | grep $<Workspace ID> | grep $<Namespace>
```

**说明**

$<Workspace ID> 、 $<Namespace> 需要根据步骤2获取的结果进行替换。 系统输出如下类似结果： ii. 执行以下命令，查看Session和Job Pod健康信息。

```bash
kubectl get po -n $<works-ns> |egrep "^job|^session"
```

**说明**

$<works-ns> 需要根据步骤a的查询结果进行替换。 系统输出如下类似结果：
5. 确认是否符合巡检结果要求。
巡检结果要求为： 所有的pod是提供流任务真正业务的pod。 STATUS必须为Running。 近期无RESTARTS。 AGE必须在5分钟以上。

**确认任务在正常处理数据**

1. 使用用户账号登录实时计算开发控制台。
详情请参见**Flink****存算分离版****用户指南** > **登录实时计算开发控制台**章节。
2. 在左侧导航栏，单击**作业运维**。
3. 单击目标作业名称。
实时计算（流计算） 巡检
4. 单击**状态总览**页签，按步骤确认以下内容。
确定源端有数据的情况下，任务处理数据在稳步增长。 确认所有的task都没有反压（当前在追数据的任务除外）。 单击目标运行状态名称，展开详情页签，单击**BackPressure**。 确认任务没有当前时间30min内的异常信息。 单击**作业探查**页签，单击**异常信息**。 实时计算（流计算） 巡检
5. 确认是否符合巡检结果要求。
巡检结果要求为： 所有的任务都处于CANCELLED或者RUNNING的状态，任务有长时间的其他状态皆视为异常。 source节点Records sent指标随刷新有增长。 所有算子中的SubTask的BackPressure的Status是ok状态，没有状态为HIGH的作业。 30分钟内没有异常信息，24小时内没有频繁异常信息。 实时计算（流计算）

## 常见问题

本文介绍在使用阿里云Flink产品时相关的常见问题。

**Flink任务长时间未启动，如何排查？**

针对阿里云专有云Flink产品中任务长时间未启动的问题，可按照以下结构化思路进行排查。该流程结合了作业状态、集群模式、资源调度、网络连通性及平台依赖等关键维度。

**白屏排查方案**

**确认作业当前状态**

1. 登录实时计算开发控制台。
2. 在左侧导航栏，单击**作业运维**。
3. 在**作业运维**页面，确认作业当前状态。
作业状态说明如下： TRANSITIONING：作业正在启动中（中间态），可能是资源调度慢、依赖等待或JM/TM启动延迟。 FAILED：作业启动失败，需查看日志定位具体错误。 ClusterUnreachable：VVP无法连接JobManager，说明JM未正常运行或网络不通。 如果状态长期为TRANSITIONING，则需要重点排查资源与JM/TM启动情况；如果状态为 ClusterUnreachable，则需要优先检查JM Pod是否就绪及网络策略。

**确认部署模式与资源可用性**

Session集群模式查看Session集群状态 Session集群需要提前手动启动，如果没有启动，则需要找到目标Session集群，单击目标集群**操作**列的**启动**，使其状态为**运行中**。 检查资源配置情况如果资源配置不足，新作业将卡在调度阶段，请保证Session集群的资源配置足够。具体操作如下： a. 找到目标Session集群，单击**操作**列下的**编辑**。 b. 在**编辑** **Session** **集群**页面的**资源配置**区域，修改资源信息。

**说明**

状态为**运行中**的Session集群无法修改资源信息。如果需要修改，请先停止集群。 Per-Job集群模式作业提交时会动态申请资源。如果资源不足、镜像拉取失败或者配额限制，都会导致集群无法创建。常见报错示例：

```
quota：k8s-xxx，requested： cpu=1， used：cpu=150，limited： cpu=150
```

请检查目标命名空间下CPU/Memory配额是否已达上限，如果已达上限，请评估是否需要进行资源扩容。

**黑屏排查方案**

**Session作业启动失败**

实时计算（流计算）

**重要**

因Session集群中JobManager是共用的，一旦JobManager异常将会导致该集群中的所有作业异常， 所以请勿在生产环境中使用Session集群。 登录实时计算开发控制台，进入Session集群页面，找到启动作业失败的目标Session集群，单击集群名称进入集群详情页面。

**Session资源问题**

因为Task Manager的数量或者Slot数不足的时候，任务调度会失败。所以建议先排查以下资源问题： 查看当前Session分配给Job Manager和Task Manager的资源是否充足。 在Session集群的**集群总览**页面中，查看当前Session集群用于执行作业的Slot数是否充足。

**说明**

默认情况下，Slot数为1，每一个Task Manager都只有唯一的Slot。如果设置Task Manager默认为1，并且Slot数>1，则每一个Task Manager分配4个Slot用于执行任务。

**作业启动异常日志定位**

在目标Session集群的详情页面，进入Job Manager或Task Manager详情页，看JobManager和 TaskManager的日志，定位具体原因。

**Per-Job作业启动失败**

Per-Job作业启动失败排查思路：
1. 在**作业运维**页面中找到未成功启动的作业，单击该作业名称进入作业详情页。
2. 查看作业当前的状态，通常为 `TRANSITIONING` 或者 `FAILED` 。
如果状态是 `FAILED` ，则可以尝试查看事件，分析具体的失败原因。

**说明**

一旦进入失败状态，管控会强制销毁JobManager和TaskManager的Pod。 如果状态是 `TRANSITIONING` ，则说明此时作业正在调度中。在这个状态下，可以进入作业详情页， 查看JobManager和TaskManager。

**说明**

优先查看是否已经拉起JM/TM，如果已经拉起JM，则优先查看JM的启动日志和容器日志；如果JM 和TM都已经拉起，则优先查看TM的日志。

**典型案例**

以下是一些常见的作业长时间未调度成功的现象和排查思路。

**TaskManager未成功注册到JobManager**

Flink的TaskManager的Pod被拉起之后，会尝试向JobManager进行注册，如果这个注册无法完成，则作业将无法启动成功。 实时计算（流计算）

**说明**

在Flink存算分离版中，JobManager拉起后就会将作业实例的状态改为Running。但在Flink企业版中，只有JobManager和TaskManager均拉起，且TaskManager都将自身注册到JobManager之后， 才会将作业实例状态改为Running。 经典场景： 网络波动大，导致TM向JM发起请求超时，正常如果是网络波动导致，这个过程可能仅比预期作业拉起时间稍长，但不会持续5~10分钟。 JM内部有异常，导致TM请求JM进行注册的请求长时间未处理，最终导致TM注册自身的请求超时。 需要注意的是，如果是第二种情况，则此时VVP的控制台无法展示TaskManager的详情，但实际从OPS上查询，可以查到租户Namespace下已经有TaskManager的Pod。 当从VVP控制台上无法看到TaskManager的详情时，请执行以下操作。
1. 在OPS上执行以下命令，查询租户Namespace中的Pod信息。
# 企业版查询租户`Namespace`中的`Pod`
# k8s-为固定前缀
# namespace请替换成自建`namespace`的名称

```bash
kubectl get pods -n k8s-${namespace}
```

# 存算分离版查询租户`Namespace`中的`Pod`
# rc-为固定前缀
# workspaceId请替换为租户创建的`workspace`的`ID`
# namespace请替换为自建`namespace`的名称

```bash
kubectl get pods -n rc-${workspaceId}-${namespace}
```

2. 查询到Pod后，可以根据VVP控制台中，作业详情页面中的作业ID进行过滤。
如果当前Namespace下作业实例很多，可以在上面执行的语句后追加 | grep ${jobId} 。其中， ${jobId} 需要替换为从VVP控制台中复制的作业ID。示例图如下： 如果TaskManager的Pod存在，此时可以判断为TM向JM注册自身时遇到问题，请优先在VVP控制台的JobManager详情页面，关注JM本身日志中存在的异常栈，解除异常后，通常TaskManager可以完成注册。 如果TaskManager的Pod不存在，此时应该是JM尝试请求底座K8s拉起TM的Pod时失败了，此时应该关注VVP管控组件agent的日志。 实时计算（流计算）
# 获取`Flink`企业版管控`Pod`

```bash
kubectl get pods -n ververica | grep ververica
```

# 获取`Flink`存算分离版租户`Agent`组件

```bash
kubectl get pods -n rc-${workspaceId}-vvp-deploy
```

# 企业版日志需要查看`appmanager`，`agent`是`appmanager`的一部分

```bash
kubectl logs ververica-ververica-xxxx -n ververica -c appmanager
```

# 存算分离版的`Agent`独立部署，建议`agent`和`appmanager`的日志一起看

```bash
kubectl get pods -n flinkonoss | grep appmanager kubectl logs appmanager-xxx -n flinkonoss kubectl logs appagent-appagent-xxxs -n rc-${workspaceId}-vvp-deploy
```

请在上述查询log的请求中使用关键字（例如JobId ）进行过滤，如果查不到，可以优先进入 appmanager的容器，将 `/vvp/logs/appmanager.log` 文件导出分析日志。

**底座apiserver响应慢，导致VVP向K8s集群调度作业的请求超时中断**

现象作业长时间处于启动中，租户的namespace下没有创建作业实例的JobManager和TaskManager。 排查思路需要围绕appmanager的日志尝试进行定位。 操作步骤参考以下命令，查询appmanager的日志。
# 获取`appmanager`管控节点
# Flink企业版

```bash
kubectl get pods -n ververica | grep ververica
```

# Flink存算分离版

```bash
kubectl get pods -n flinkonoss | grep appmanager
```

# 查询日志，查询时需要替换占位符
# Flink企业版

```bash
kubectl logs ${ververica-ververica-xxx-xxx} -n ververica -c appmanager [--since=5m] | grep ${JobId}
```

# Flink存算分离版

```bash
kubectl logs ${vvp-appmanager-xxx-xxx} -n flinkonoss [--since=5m] | grep "${JobId}"
```

**说明**

`--since=5m` 为可选，限定日志查询5分钟内的日志，可以一定程度上定位最近几分钟的日志。 特殊说明：由于appmanger负责作业的调度、状态机维护等，日志量较大，通过 `kubectl` 命令获取的时候，可能因为日志量大导致命令查不到想要的日志，此时可以以交互模式进入appmanager的容器中，查看原始日志文件。 实时计算（流计算）
# Flink企业版

```bash
kubectl exec -it ${ververica-ververica-xxx-xxx} -n ververica -c appmanager bash
```

# Flink存算分离版

```bash
kubectl exec -it ${vvp-appmanager-xxx-xxx} -n flinkonoss bash
```

# 日志路径

```
cd /vvp/logs
```

`ls` 此时可根据日志文件及归档的日志文件查询，例如：执行 cat appmanager.log | grep "xxx" 命令。 通常情况下，通过JobId可以查询到相关日志，找到日志头部的requestId，可以根据requestId进行 grep获取完整请求链路的日志，如果发现appmanager调度作业时出现 `timeout` 这种字段，一般可以判断是底座apiserver响应时间过长。

**外部存储IP未加白，连接外部存储失败导致作业失败**

背景在专有云v3.18.6版本的Flink中，由于安全限制，Flink需要通过networkpolicy进行网络隔离，除业务网段及部分底座组件（例如：apiserver、coredns）等必要组件外，通常对于外部存储组件，默认无法访问，需要通过vvp控制台，针对当前namespace进行IP加白后访问。 现象 Flink作业的JobManager长时间无法启动，在日志中可以看到类似于连接超时、 `SocketTimeOut` 之类的报错，通常就是因未操作IP加白导致的。 检查方式 i. 登录实时计算Flink版管理控制台。 ii. 找到目标Namespace，单击**操作**列下的**配置外部存储** **IP** 。 iii. 查看连接超时的域名对应的IP是否在此处进行了加白，如果未进行加白，请先添加IP白名单。

**Networkpolicy生效慢/Rama分配IP效率低导致作业启动超时**

背景在专有云v3.18.6版本开启networkpolicy白名单后，底座网络组件默认使用iptables对网络进行隔离。历史上曾经发现客户现场出现，单个namespace中存在大量的加白IP，导致每次作业启动的时候，等待networkpolicy生效的时间很长。 Flink在作业进行调度的时候，JobManager和TaskManager被拉起后，需要进行网络隔离探测（等待 networkpolicy生效），如果JobManager的Pod被创建成功后，在一段时间内作业没有运行（通常默认是5分钟），则JobManager会认为作业无法启动，强制进入失败状态。 JobManager和TaskManager的Pod，在networkpolicy探测成功后，会通过容器底座网络组件 Rama分配一个IP地址。 现象定位首先确定处于拉起中的JobManager和TaskManager是否带有Init Container。
# k8s- 为固定前缀，需要替换占位符

```bash
kubectl get pods -n k8s-${namespace}
```

# rc- 为固定前缀，需要替换占位符

```bash
kubectl get pods -n rc-${workspaceId}-${namespace}
```

实时计算（流计算） 如果这个Init container运行时间达到分钟级，就说明networkpolicy的探测拖慢了整体作业启动的进度。此时，可以考虑升级到sp006以上的版本，使用优化后的网络插件方案；如果是因为IP加白过多，则请联系阿里云技术支持处理。 当有大量作业批量启动时，每个Pod创建时会请求Rama进行IP分配，当这个量过大的时候，可能会导致 Rama内部的队列被打爆，导致Rama响应偏慢。
# Flink企业版

```bash
kubectl get pods -n k8s-${namespace} kubectl describe pod ${xxxx} -n k8s-${namespace}
```

# Flink存算分离版

```bash
kubectl get pods -n -${workspaceId}-${namespace} kubectl describe pod ${xxxx} -n -${workspaceId}-${namespace}
```

关注这个结果是否出现失败重试多次耗时长的问题。该问题和networkpolicy生效慢的问题产生叠加时， 很容易让作业调度启动的流程超时，导致JobManager的强制终止，最终作业失败。
