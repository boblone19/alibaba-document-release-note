---
title: "实时计算（流计算） 运维指南（Blink）"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 47
source_pdf: "06_运维指南（Blink）_enterprise-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/enterprise-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） 运维指南（Blink）

实时计算（流计算）

## 作业状态

### 概述

作业状态展示了整个Job实时运行的情况和瞬时值，您可以通过整个作业的状态来分析、判断作业的状态是否健康，是否达到了您的预期。 Figure 1. 作业状态

### Task状态

Task状态分为创建、运行、失败、完成、调度、取消中、已取消7种状态。从每个状态来判断这个作业是否运行正常。

### 健康分

为了方便您快速定位作业性能问题，实时计算定义了健康分检查机制。 作业健康分< 60分代表当前节点有数据堆积、处理数据的性能不够，需要使用自动配置调优或者手动配置调优来解决。您可以根据自己的业务需求来进行调优。

### 作业瞬时值

表 1. 作业参数说明

| 名称 | 作用描述 |
|---|---|
| 计算耗时 | 表示整个Job的计算性能。 |
| 输入TPS | 表示的是每秒从源端读到的Block数，对于日志服务而言，可以将多条数据打包到一个LogGroup读取，Block 数反映的是从源端每秒读取LogGroup数量。 |
| 输入RPS | 表示每秒读取数据源表的RPS数，单位是条/秒。 |

实时计算（流计算）

| 输出RPS | 表示每秒写入数据结果的RPS数，单位是条/秒。 |
|---|---|
| 输入BPS | 表示每秒流量的传输速率，单位是Byte/秒。 |
| 使用CPU | 表示单个Job当前CPU的使用数量。 |
| 启动时间 | 表示该Job的启动的时间。 |
| 运行时长 | 表示该Job的启动后运行的时间。 |

### 运行拓扑图

运行拓扑图描述的是实时计算底层计算逻辑的执行图，而每个组件代表的是不同的Task，每个数据流从一个或多个数据源开始，流向一个或多个的数据的结果表中结束。数据流类似于任意有向无环图（DAG）。为了更高效地分布式执行，实时计算底层会尽可能地将Operator的Subtask链接（Chain）在一起形成Task。 每个Task在一个线程中执行。 将Operators链接成Task，是对以下问题的优化： 减少线程之间的切换。 减少消息的序列化/反序列化。 减少数据在缓冲区的交换。 减少延迟的同时提高整体的吞吐量。 Operator代表的是每个计算逻辑的算子，而Task代表是多个Operator的集合。

**视图模式**

为方便您更好地理解，我们把底层计算逻辑抽象成为视图，如视图模式所示。 图 1. 视图模式鼠标移动到Task时会显示Task的详细信息，具体参数说明如参数说明所示。表 1. 参数说明

| 名称 | 信息描述 |
|---|---|
| ID | 在运行拓扑图的编码 |
| PARALLEL | 并发量 |

实时计算（流计算）

| CPU | 单个并发的CPU |
|---|---|
| MEM | 单个并发的内存 |
| TPS | 每秒读取上游数据的BLOCK数 |
| LATENCY | Task节点的计算耗时 |
| DELAY | Task节点的业务延时 |
| IN Q _ | Task节点的输入队列的百分比 |
| OUT Q _ | Task节点的输出队列的百分比 |

点击Task节点，即可进入详情页面，查看Task的里线程的列表，如Task详情页面所示。 图 2. Task详情页面为更好地帮助您，TaskMetric页签下提供了每个Task的曲线指标图，如Task的曲线指标图所示。 图 3. Task的曲线指标图

**列表模式**

实时计算不仅提供视图模式，同样也提供每个Task的列表模式。如列表模式所示。 图 4. 列表模式实时计算（流计算） 参数说明如参数说明所示。表 2. 参数说明

| 名称 | 信息描述 |
|---|---|
| ID | 表示在运行拓扑图的编码 |
| Name | 表示每个Task的详情信息 |
| Status | 表示每个Task的运行的状态 |
| INQ max | 表示Task节点的输入队列，单位是百分比 |
| OUTQ max | 表示Task节点的输出队列，单位是百分比 |
| RecvCnt sum | 表示Task节点接收到的数据量 |
| SendCnt sum | 表示Task节点的发送的数据量 |
| TPS sum | 表示每秒读取上游的信息量 |
| Delay max | 表示Task节点的业务延时 |
| Task | 表示每个Task节点的并发的运行状态 |
| StartTime | 表示Task节点的启动时间 |
| Durations(s) | 表示Task节点的运行时间 |

实时计算（流计算）

## 数据曲线

### 概述

实时计算提供了当前作业的核心指标概览页面，您可以通过此工具对当前运行作业的运行情况进行一键诊断，未来实时计算还会提供更多的基于作业现状深度智能分析算法，以辅助您进行智能化、自动化诊断。 Figure 1. 数据曲线页面

**说明**

上述所有指标在实时计算作业运行状态下才会显示，暂停以及停止状态均不显示。 作业指标是实时计算系统异步后台采集，有一定延迟。因此，在作业启动一分钟内，指标无法显示，等待一分钟后各项指标才能逐步采集到位。

### Overview

Faiover Rate指当前JOB出现错误或者异常情况次数的百分比数。您可以从Faiover Rate的曲线中更好的分析Job的问题。

**业务延时**

链路延时指当前实时计算处理时刻减去流式数据业务时间戳（如果业务时间不存在，使用上游的 DataHub/ogHub等均会对进入的数据加入系统时间戳），该数据集中反映出当前实时计算全链路的时效情况。例如，当前实时计算时间点为凌晨5点，但实时计算读取处理的数据存储时间戳为凌晨1点，意味着当前实时计算处理的数据还是1点的数据，即处理的数据相比于当前处理时间落后近4个小时，则业务延时就是4 小时。业务延时用来监控全链路的数据进度，如果源头采集数据由于故障没有进入DataHub，链路延时也会随之逐渐增大。如业务延时图示所示。 图 1. 业务延时图示实时计算（流计算） 根据业务延时又分为三个细粒度的层次。 最小延时：指各SOURCE中SHARD的最小的业务延时值。 图 2. 最小延时图示最大延时：指各SOURCE中SHARD的最大的业务延时值。 图 3. 最大延时图示平均延时：指各SOURCE中所有SHARD的平均的业务延时值。 图 4. 平均延时图示实时计算（流计算）

**各Source的TPS数据输入**

数据输入是对该实时计算作业所有的流式数据输入进行统计，给您一个直观的检测数据存储 TPS（Trasactions Per Second）情况，记录每秒读取数据源表的BLOCK的数量。与RPS的不同，RPS是读取数据源TPS的block数解析后的数据，单位是条/秒。 例如对于日志服务，一秒读取N个LogGroup，解析出来M个日志记录，而解析出的数据就是数据输入的 RPS。 图 5. 各Source的TPS数据输入

**各Sink的数据输出**

数据输出对于该实时计算作业所有的数据输出进行统计，给您一个直观的检测数据存储RPS（Records Per Second）情况。 输出的并非是流式数据存储，而是全部数据存储。

**说明**

通常在系统运维过程中，如果出现没有数据输出的情况，除了检查上游是否存在数据输入，同样要检查下游是否真的存在数据输出。 图 6. 各Sink的数据输出实时计算（流计算）

**各Source的RPS数据输入**

数据输入是对该实时计算作业所有的流式数据输入进行统计，给您一个直观的检测数据存储RPS（Record Per Secodng）情况。通常，我们在系统运维过程中，如果出现没有数据输出的情况，就需要查看该值是否从源头数据输入就已经没有数据了。 图 7. 各Source的RPS数据输入

**各Source的数据流量输入**

流量输入对于该实时计算作业所有的流式数据输入进行统计，给您一个直观的检测数据流量BPS（Byte Per Second）情况，记录每秒读取输入源表的流量的统计。 图 8. 各Source的数据流量输入

**CPU使用**

实时计算（流计算） CPU占用反映的是实时计算作业对于CPU资源消耗情况，实时计算提供了两个指标反映CPU占用情况。 申请的CPU的数据量当前作业使用CPU的曲线值图 9. CPU使用

**MEM使用**

内存使用率反映的是实时计算作业对内存资源消耗情况，实时计算提供两个指标反映内存占用情况。 申请的内存的数量当前作业使用内存的曲线值图 10. MEM使用

**各Source的脏数据**

各Source的脏数据反映了实时计算的Source段是否有脏数据。 图 11. 各Source的脏数据实时计算（流计算）

### Advanced View

实时计算提供可以恢复数据流应用到一致状态的容错机制（Checkpoint），容错机制的核心就是持续创建分布式数据流及其状态的一致快照。这些快照在系统遇到故障时，充当可以回退的一致性检查点分布式快照的核心概念之一是数据栅栏（Barrier）。这些Barrier被插入到数据流中，作为数据流的一部分和数据一起向下流动。Barrier不会干扰正常数据，数据流严格有序。一个Barrier把数据流分割成两部分： 一部分进入到当前快照。 另一部分进入下一个快照。 每一个Barrier都带有快照 ID，并且Barrier之前的数据都进入了此快照。Barrier不会干扰数据流处理，所以非常轻量。多个不同快照的多个Barrier会在流中同时出现，即多个快照可能同时创建。 图 1. 数据栅栏 Barrier在数据源端插入，当snapshot n的Barrier插入后，系统会记录当前snapshot位置值n（用Sn表示）。然后Barrier继续往下流动，当一个operator从其输入流接收到所有标识snapshot n的barrier时， 它会向其所有输出流插入一个标识snapshot n的Barrier。当sink operator（DAG流的终点）从其输入流接收到所有barrier n时，它向the checkpoint coordinator确认snapshot n已完成。当所有sink都确认了这个快照，快照就被标识为完成。 图 2. Barrier工作机制实时计算（流计算） Checkpoint Duration表示每次做Checkpoint保存状态所花费的时间，单位是MS。 Checkpoint Size表示的是每次做Checkpoint的SIZE的大小，单位是MiB。 checkpoint Alignment Time表示当前节点做Checkpointpoint时等待上游所有节点到达当前节点的时间，也就是当sink operator（DAG流的终点）从其输入流接收到所有barrier n时，它向the checkpoint coordinator确认snapshot n已完成。当所有sink都确认了这个快照，快照就被标识为完实时计算（流计算）

**Get**

在一定时间内每个SUBTASK Get操作ROCKSDB所花费的时间（最大值）。 图 7. Get

**Put**

在一定时间内每个SUBTASK Put操作ROCKSDB所花费的时间（最大值）。 图 8. Put

**Seek**

在一定时间内每个SUBTASK Seek操作ROCKSDB所花费的时间（最大值）。 图 9. Seek 实时计算（流计算）

**State Size**

衡量Job内部state存储大小（如果增量过快Job是异常的）。 图 10. State Size

**CMS GC Time**

衡量Job底层container进行GC花费的时间。 图 11. CMS GC Time

**CMS GC Rate**

衡量Job底层container进行GC的频率。 图 12. CMS GC Rate 实时计算（流计算）

### Delay

**Source SubTask最大延迟Top 15**

Source SubTask指数据源端的每个并发，这个数据指标是统计的每个Source的并发的业务延时的时间。 图 1. Source SubTask最大延迟Top 15

### Throughput

**Task Input TPS**

Task Input TPS指作业级别所有的Task的数据的输入。 图 1. Task Input TPS 实时计算（流计算）

**Task Output TPS**

Task Output TPS指作业级别所有的Task的数据的输出。 图 2. Task Output TPS

### Queue

实时计算（流计算）

### Tracing

高级用户使用的参数如下所示。 task级别的每秒处理所花费的时间。

**Time Used In Waiting Oputput Per Second**

task级别的每秒等待输出的时间。

**TaskLatency**

JOB级别的每个task的计算延时的曲线。

**WaitOutput**

task级别的等待输出的曲线。

**WaitInput**

task级别的等待输入的曲线。

**Source Latency**

Source里每个并发的延时曲线。

### Process

进程级别的每个进程内存的使用曲线。 实时计算（流计算）

**Memory NonHeap Used**

每个进程的非heap存储量曲线。 图 2. Memory NonHeap Used

**CPU Usage**

进程级别的每个进程CPU的使用曲线。 图 3. CPU Usage

### JVM

**Memory Heap Used**

整个Job使用的JVM heap存储量。 图 1. Memory Heap Used 实时计算（流计算）

**Memory NonHeap Used**

整个Job使用的JVM 非heap存储量。 图 2. Memory NonHeap Used

**Threads Count**

整个Job的线程数。 图 3. Threads Count

**GC（CMS）**

整个Job GC的次数。 图 4. GC（CMS） 实时计算（流计算） 实时计算（流计算）

## FailOver

实时计算提供了当前作业的FailOver页面，您可以通过这个页面判断当前运行作业的运行情况是否正常。 图 1. 作业运行正常图 2. 作业运行异常实时计算（流计算） 实时计算（流计算）

## CheckPoint

实时计算提供可以恢复数据流应用到一致状态的容错机制（CheckPoint）。容错机制的核心就是持续创建分布式数据流及其状态的一致快照。这些快照在系统遇到故障时，充当可以回退的一致性检查点 Completed Checkpoints表示的是已经完成的CheckPoints的信息，参数说明如Completed Checkpoints参数说明所示。表 1. Completed Checkpoints参数说明

| 名称 | 详情描述 |
|---|---|
| ID | 做CheckPoint的ID编号 |
| StartTime | 开始的时间 |
| Durations(ms) | 花费的时间 |

Task Latest Completed Checkpoint表示的最新一次checkpoint的详细信息，参数说明如Task Latest Completed Checkpoint参数说明所示。表 2. Task Latest Completed Checkpoint参数说明

| 名称 | 详情描述 |
|---|---|
| SubTask ID | 做SubTask的ID编号 |
| State Size | 做CheckPoint的大小 |
| Durations(ms) | 花费的时间 |

实时计算（流计算）

## JobManager

当实时计算集群启动后，首先会启动一个JobManger和一个或多个的TaskManager。由Client提交任务给 JobManager，JobManager再调度任务到各个TaskManager去执行，然后TaskManager将心跳和统计信息汇报给JobManager。TaskManager之间以流的形式进行数据的传输。 JobManager主要负责调度Job并协调Task做checkpoint，职责上很像Storm的Nimbus。从Client处接收到Job和JAR包等资源后，会生成优化后的执行计划，并以Task的单元调度到各个TaskManager去执行。 实时计算（流计算）

## TaskExecutor

实时计算集群启动后，首先会启动一个JobManger和一个或多个的TaskManager。由Client提交任务给 JobManager，JobManager再调度任务到各个TaskManager 去执行，然后TaskManager将心跳和统计信息汇报给JobManager。TaskManager之间以流的形式进行数据的传输。 TaskManager在启动的时候就设置好了槽位数（Slot），每个slot能启动一个Task，Task为线程。从 JobManager处接收需要部署的Task，部署启动后，与自己的上游建立Netty连接，接收数据并处理。 每个Task Manager的详细信息如Task Manager详情所示。 图 1. Task Manager详情实时计算（流计算）

## 血缘关系

实时计算作业的血缘关系集中反映了一个实时计算作业上下游数据的依赖关系，对于作业较为复杂的上下游业务依赖，数据拓扑更加能够清晰地反映出上下游依赖信息，如血缘关系页面所示。 图 1. 血缘关系页面

**数据抽样**

作业上下游提供了数据抽样功能，该功能和数据开发页面一致，方便您在数据运维页面进行随时数据探测， 方便您定位问题。在作业上下游中，点击表名称后的按钮即可打开数据抽样功能。 图 2. 打开数据抽样功能图 3. 数据抽样窗口实时计算（流计算） 实时计算（流计算）

## 属性参数

属性参数提供了当前作业的详情信息，包括当前运行信息以及历史运行记录。 属性参数页面如属性参数页面所示。 图 1. 属性参数页面

**作业代码**

可以预览整个SQL作业，点击**编辑作业**跳转到**开发**页面。

**资源配置**

资源配置提供了JOB运行的所有资源的配置，CPU、MEM、并发数等资源配置。

**运行属性**

运行属性提供了当前JOB的最基本的运行信息，参数说明如作业属性所示。表 1. 作业属性

| 序号 | 详细描述 |
|---|---|
| 1 | 作业名称 |
| 2 | 作业ID |
| 3 | 引用资源 |
| 4 | 运行引擎 |
| 5 | 最近操作人 |
| 6 | 操作动作 |
| 7 | 创建人员 |
| 8 | 创建时间 |
| 9 | 最近修改人 |
| 10 | 最近修改时间 |

**运行参数**

实时计算（流计算）

**历史记录**

记录了作业操作的所有版本信息，包括操作人、启动时间、停止时间等。

**作业参数**

作业的其他额外的作业参数，例如调试用的分割符。 实时计算（流计算）

## 自动配置调优

**背景**

在实时计算作业的各个算子和实时计算作业上下游性能达标和稳定的前提下，自动配置调优功能可以帮助您更合理的分配各算子的资源和并发度等配置，全局优化作业，调节作业吞吐量不足、作业全链路的反压等性能调优的问题。 出现下列情况时，自动配置调优功能可以作出优化，但无法彻底解决实时计算作业的性能瓶颈，需要你自行解决性能瓶颈或联系阿里云团队解决性能瓶颈。 用户实时计算作业上下游有性能问题： 实时计算作业上游的数据源有性能问题，例如DataHub分区不足、MQ吞吐不够等，需要用户扩大相应数据源的分区。 实时计算作业下游的数据Sink有性能问题，例如RDS死锁等。 用户实时计算作业的自定义函数 (UDF、UDAF、 UDTF) 有性能问题。

**新作业操作**

1. 在SQ开发完成后，通过语法检查后，点击**上线**，出现如下的界面：
资源配置
**智能****CU****配置**：autoconf算法会基于系统默认配置生成CU数进行优化资源配置，如果是第一次运行，
算法会根据经验值生成一份初始配置。(建议作业运行了10分钟以上再使用智能配置，重复3到5次才能调优出最佳的配置)
**使用上次资源配置**：就是使用最近一次保存的资源配置，如果上一次是智能配置的，就使用上一次智能
配置的结果，如果上一次是手工配置的，就使用上次手工配置的结果。 推荐选择**智能****CU****配置**，第一次不需要指定CU数，使用系统默认配置即可。

**说明**

2. 使用默认配置启动作业，出现如下的界面：
数据检查实时计算（流计算）
3. 启动作业。
启动作业举例说明：第一次缺省配置生成的资源配置为71个CU，作业一定要运行10分钟以上。 示例
4. 开始调优。
用户需要资源调优，例如:用户手动配置40CU用智能模式启动。(40的CU数是用户自行

**说明**

指定调整的，根据具体的作业情况适当的增加或者是减小。CU的最小配置建议不小于缺省配置总数的50%，最低CU数不能小于1CU。例如:71*50% = 35.5CU ，假如无法满足作业理想的吞吐量就需要增加适量的CU数，每次增加的CU数，建议是上一次CU总数的30%以上，如：上一次是10CU下次就需要增加到13CU。)如果第一次调优不满足用户的需求，可以调优多次，可以根据每次调优Job 的状态来增加或减少资源数。 调优实时计算（流计算）
5. 调优后的结果如下：
调优结果如果是新任务，不要选择**使用上次资源配置**，否则会报错：

**说明**

报错页面

**已有作业操作**

调优流程如下： 调优流程老的作业在进行调优前，一定要检查是否是有状态的计算。因为在调优的过程中可能会清除之前作业保存的状态，所以请务必谨慎操作。 实时计算（流计算） 当用户作业有改动时（如用户对作业的SQL有修改，或更改了实时计算的版本），自动配置调优功能不保证能按照之前的运行信息进行调优。原因是这些改动会导致拓扑信息变化，造成数据曲线无法对应和状态无法复用等问题，自动配置调优功能无法根据运行历史信息作出调优判断，此时再使用自动配置调优会报异常。 解决方法是从步骤1开始，将改动后的任务当做新任务，重新走一遍流程。 异常页面重复新作业的调优步骤，使用最新的配置启动作业： 按最新配置恢复

**常见问题**

任务运行的时间较短，会造成采样得到的有用信息较少，会影响autoconf算法的效果，建议延长运行时间，确认source rps等数据曲线稳定2~3分钟后即可。 任务运行有异常（FailOver），会影响结果的准确性，建议用户检查和修复FailOver的问题。 任务的数据量比较少，会影响结果的准确性，建议多追溯一些历史数据。 影响的因素有很多，自动配置调优autoconf不能保证下一次生成的配置一定比上一次的好。如果还不

**调优建议**

每次触发智能配置前任务稳定运行超过10分钟，这样有利于autoconf搜集到准确的运行时指标信息。 autoconf可能需要3~5次迭代才能见效，即需要你重复上述的上线和运维步骤若干次。 使用autoconf时，你可以故意让任务追数据甚至造成反压，这会更利于快速收敛看到效果。 实时计算（流计算） 自动配置调优功能通过Json配置文件与实时计算进行交互。用户在调优后，可以通过查看Json配置文件了解通过Bayes作业编辑界面查看。 通过Bayes作业运维界面查看。 Json 配置说明： 实时计算（流计算）

```json
"autoConfig" : {
    "goal": {  // autoconf 目标
```

`"maxResourceUnits": 10000.0, //` 单个`Blink`作业最大可用`CU`数，不能修改，查看时可忽略 `"targetResoureUnits": 20.0 //` 用户指定`CU`数。用户指定`20CU`，这里就是`20.0` }， `"result" : { // autoconf` 结果！这里很重要

```json
      "scalingAction" : "ScaleToTargetResource",  // autoconf 的运行行动 *
      "allocatedResourceUnits" : 18.5, // autoconf 分配的总资源
      "allocatedCpuCores" : 18.5,      // autoconf 分配的总CPU
      "allocatedMemoryInMB" : 40960    // autoconf 分配的总内存
      "messages" : "xxxx"  // 很重要！ *
    }
}
```

scalingAction: **InitialScale**代表初次运行，**ScaleToTargetResource**代表非初次运行。 如果没有messages，代表运行正常。如果有messages，代表需要分析。messages有两种，如下所示： warning 提示：表示正常运行情况但有潜在问题，需要用户注意，如source的分区不足等。 error或者exception提示：常伴有 `Previous job statistics and configuration will be used` ，代表autoconf失败。失败有两种原因： 用户作业或实时计算版本有修改，autoconf无法复用以前的信息。 有 xxxException 代表autoconf遇到问题，需要跟据信息、日志等综合分析。如没有足够的信息， 请联系产品支持和开发团队。

**异常信息问题**

IllegalStateException异常： 出现如下的异常说明内部状态 state 无法复用，需要停止任务清除状态后重追数据。 如果无法切到备链路，担心对线上业务有影响，可以在**开发**界面右侧的**作业属性**里面选择上个版本进行回滚，等到业务低峰期的时候再重追数据。

```
java.lang.IllegalStateException: Could not initialize keyed state backend.
```

`at`

```
org.apache.flink.streaming.api.operators.AbstractStreamOperator.initKeyedState(AbstractSt amOperator.java:687)
```

`at`

```
org.apache.flink.streaming.api.operators.AbstractStreamOperator.initializeState(AbstractS eamOperator.java:275)
```

`at`

```
org.apache.flink.streaming.runtime.tasks.StreamTask.initializeOperators(StreamTask.java:8
```

) `at`

```
org.apache.flink.streaming.runtime.tasks.StreamTask.initializeState(StreamTask.java:856)
    at org.apache.flink.streaming.runtime.tasks.StreamTask.invoke(StreamTask.java:292)
    at org.apache.flink.runtime.taskmanager.Task.run(Task.java:762)
    at java.lang.Thread.run(Thread.java:834)
Caused by: org.apache.flink.api.common.typeutils.SerializationException: Cannot seriali ze/deserialize the object.
```

`at`

```
com.alibaba.blink.contrib.streaming.state.AbstractRocksDBRawSecondaryState.deserializeSta Entry(AbstractRocksDBRawSecondaryState.java:167)
```

`at` 实时计算（流计算） `at`

```
com.alibaba.blink.contrib.streaming.state.RocksDBIncrementalRestoreOperation.restoreRawSt eData(RocksDBIncrementalRestoreOperation.java:425)
```

`at`

```
com.alibaba.blink.contrib.streaming.state.RocksDBIncrementalRestoreOperation.restore(Rock BIncrementalRestoreOperation.java:119)
```

`at`

```
com.alibaba.blink.contrib.streaming.state.RocksDBKeyedStateBackend.restore(RocksDBKeyedSt eBackend.java:216)
```

`at`

```
org.apache.flink.streaming.api.operators.AbstractStreamOperator.createKeyedStateBackend(A tractStreamOperator.java:986)
```

`at`

```
org.apache.flink.streaming.api.operators.AbstractStreamOperator.initKeyedState(AbstractSt amOperator.java:675)
    ... 6 more
Caused by: java.io.EOFException
    at java.io.DataInputStream.readUnsignedByte(DataInputStream.java:290)
    at org.apache.flink.types.StringValue.readString(StringValue.java:770)
```

`at`

```
org.apache.flink.api.common.typeutils.base.StringSerializer.deserialize(StringSerializer. va:69)
```

`at`

```
org.apache.flink.api.common.typeutils.base.StringSerializer.deserialize(StringSerializer. va:28)
```

`at`

```
org.apache.flink.api.java.typeutils.runtime.RowSerializer.deserialize(RowSerializer.java:
```

`9)` `at`

```
org.apache.flink.api.java.typeutils.runtime.RowSerializer.deserialize(RowSerializer.java:
```

) `at`

```
com.alibaba.blink.contrib.streaming.state.AbstractRocksDBRawSecondaryState.deserializeSta Entry(AbstractRocksDBRawSecondaryState.java:162)
    ... 11 more
```

实时计算（流计算）

## 手动配置调优

### 概述

手动性能调优的内容主要有3种类型： 资源调优：主要对作业中的Operator的并发数（parallelism）、CPU（core）、堆内存 （heap_memory）等参数进行调优； 下面我们对以上3类调优进行介绍，参数调优后将生成新的配置，Job需重新上线启动/恢复才能使用新的配置，本文最后章节将讲述如何重新启用新的配置。

### 资源调优

**分析问题**

1. 如下图所示，2号的TASK节点的输入队列已达到100%造成数据堆积反压到它的上游1号的TASK节点，输
出队列造成数据堆积。
2. 单击2号的TASK节点，找到队列已达到100%的TaskExecutor。
3. 查看TaskExecutor的CPU和内存的使用量，根据使用量来调大相应的CPU和MEM。
Figure 3. CPU和MEM 实时计算（流计算）

**性能调优**

1. 进入调优窗口。
Figure 4. 调优窗口
2. 打开可视化编辑。
Figure 5. 可视化编辑页面
3. 找到2号task对应的Group（若有）或Operator，可以按Group批量修改或对单个Operator进行参数修
改。 实时计算（流计算） 按Group批量修改 Figure 6. 批量修改单个Operator修改 Figure 7. 单节点修改实时计算（流计算）
4. 配置参数后，点击右上角的**应用当前配置并关闭窗口**，即可保存当前配置。

**说明**

如果在调优的过程中发现虽然调大了某个Group的资源配置但是并没有太大的效果，需要把其中的 Operator节点全部拆开，来判断到底是哪个子节点有异常。找到该子节点后，只需调优该节点即可。 将Operator子节点拆开的方法：点击需要修改的Operator，将其参数chainingStrategy修改为 HEAD，若其已为HEAD，需要将其后面的第一个Operator修改为HEAD。 chainingStrategy三个参数的说明如下： ALWAYS：代表把单个的节点合并成一个大的GROUP里面。 NEVER：保持不变。 HEAD ：表示把在合并成一个GROUP里面单个节点拆分出来。

**资源参数的配置原则和建议**

可以调整的参数如下所示： parallelism source 资源根据上游Partition数来。例如source的个数是16，那么source的并发可以配置为16,8,4等，不要超过16。 中间的处理节点根据预估的QPS计算。对于小任务来说，和source一样的并发度就够了。QPS高的任务，可以配大点，例如 64、128 或者 256。 sink节点并发度和下游存储的Partition数相关，一般是下游Partition个数的2~3倍。如果配置太大会导致写超时或失败。例如下游SINK的个数是16，那么sink的并发最大可以配置48。 core CPU，默认0.1，根据实际CPU使用配置（但最好能被1整除），一般建议0.25。 heap_memory 堆内存，默认256MB，根据实际内存使用配置单击GROUP就可以编辑以上参数。 如果有GROUP BY 的TASK节点可以配置下述参数。 state_size：state大小，默认为0。如果operator有用state,需要把state_size配成1，表示该 operator会用state，job在申请资源的时候会额外为该operator申请内存，供state访问使用；如果不配成1，job可能被yarn kill。

**说明**

state_size需要配成1的operator有：group by、join、over和window。 虽然有这么多配置项，对普通用户来说，只需要关心：core，parallelism和 heap_memory。 整个job 建议core:mem=1:4，即一个核对应4G内存。

### 作业参数调优

miniBatch设置：该设置只能优化group by。Flink SQL纯流模式下，每来一条数据都会去操作state，io 消耗较大，设置miniBatch后，同一个key的一批数据只访问一次state，且只输出最新的一条数据，即减少了state访问也减少了向下游的数据更新。miniBatch设置如下所示。
1. 表示整个job允许的延迟。

```
blink.miniBatch.allowLatencyMs=5000
```

实时计算（流计算） y
2. 单个batch的size。

```
blink.miniBatch.size=1000
```

图 1. miniBatch设置

### 上下游参数调优

由于实时计算的特性，每条数据均会触发上下游存储的读写，会对上下游存储形成性能压力。您可以通过设置批量读写参数，批量的读写上下游存储数据来降低对上下游存储的压力。以下数据存储支持批量读写参数。 表 1. 参数配置

| 名称 | 参数 | 详情 | 设置参数值 |
|---|---|---|---|
| DataHub源表 | batchReadSize | 单次读取条数 | 可选，默认为10 |
| DataHub结果表 | batchSize | 单次写入条数 | 可选，默认为300 |
| 日志服务（LogService） 源表 | batchGetSize | 单次读取logGroup条数 | 可选，默认为10 |
| 分析型数据库MySQL版 （分析型数据库MySQL 版）结果表 | batchSize | 每次写的批次大小 | 可选，默认为1000 |
| 云数据库（RDS）结果表 | batchSize | 每次写的批次大小 | 可选，默认为50 |

在相应数据存储DDL声明的WITH参数列表中，新增以上参数即可完成批量读写设置。例

**说明**

如，DataHub源表DDL声明的WITH参数列表中，新增 batchReadSize=’500‘ 。 实时计算（流计算）

### 重新启用新配置

配置完成后，需要重新启动/恢复作业才能使新配置生效。
1. 上线作业，配置方式选择**使用上次资源配置**。
Figure 1. 资源配置
2. 暂停原作业。
Figure 2. 暂停原作业
3. 恢复原作业，选择**按最新配置恢复**，否则新配置无法生效。
Figure 3. 恢复原作业 Figure 4. 按最新配置恢复
4. 重新恢复后，可通过**运维** > **运行信息** **> Vertex****拓扑**查看新的配置是否生效。

**说明**

一般情况下，我们不建议采用先停止Job再启动的方式使新配置生效，因为Job停止后status状态会消除，可能会导致计算结果不一致。 实时计算（流计算）

### 概念介绍

global isChainingEnabled：表示是否启用chain策略，默认为true，不需要更改。 nodes id ：节点id号，自动生成且唯一，不需要更改。 uid：节点uid号，用于计算operator id，如果不设置，会使用id。 pact：节点类型，例如Data Source，Operator，Data Sink等，不需要更改。 name：节点名字，您可以自定义。 slotSharingGroup：default，不需要更改。 chainingStrategy：chain的策略，有HEAD、ALWAYS和NEVER，不需要更改。 parallelism：并发度，默认为1，可以根据实际数据量改大点。 core：CPU，默认0.1，根据实际CPU使用配置（但最好能被1整除），一般建议0.25。 heap_memory：堆内存，默认256MB，根据实际内存使用配置。 direct_memory：jvm堆外内存，默认0，建议不要改。 native_memory：jvm堆外内存，jni使用，默认 0，建议用10MB。 Chain Flink SQL任务是一个DAG图，会有很多个节点（Operator），有些上下游的节点在运行时是可以合成一个点的，这称之为chain。对于chain之后的点，CPU取最大的最大值，内存取总和。例如 Node1{256MB，0.2core}，Node2{128MB，0.5core}，Node3{128MB，0.25core}，那么这三个点chain后的CPU是 0.5core，内存是 512MB。chain的规则简单来说就是：并发度需要一样。但是，有些节点之间是不能合在一起的，比如groupBy。一般来说，尽可能的让节点都chain在一起，减少网络传输。
