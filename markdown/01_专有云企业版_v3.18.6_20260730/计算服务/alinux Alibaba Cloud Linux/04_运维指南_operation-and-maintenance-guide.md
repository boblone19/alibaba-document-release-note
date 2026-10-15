---
title: "Cloud Linux 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 98
source_pdf: "04_运维指南_operation-and-maintenance-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/alinux/zh/operation-and-maintenance-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# Cloud Linux 运维指南

Alibaba Cloud Linux

## 系统运维

### 安装SysOM工具

**环境要求**

**操作系统要求**

阿里云服务器操作系统V3。

**硬件要求**

CPU数建议8核以上，内存建议32G以上。如果需要热补丁功能，CPU数建议32核以上。 SysOM2.1 及之前的版本，只支持x86_64架构。

**软件包要求**

支持python3及python3相关软件包，grafana及grafana依赖包，make/gcc等编译软件包及相关依赖包，mysql/mariadb，redis，nfs-utils，rpcbind，wget，ssh，nginx，supervisord，yum，dnf 等。

**环境要求**

安装和运行过程要求SysOM部署环境可以访问外网。并且部署SysOM之前要确保selinux关闭，关闭方式如下： i. 编辑/etc/selinux/config。 ii. 将 `SELINUX=enforcing` 改成 `SELINUX=disabled` 。 iii. 保存文件后执行 `reboot` 重启机器即可。

**操作步骤**

1. 安装rpm包。

```bash
yum install sysom -y
```

默认安装路径为/usr/local/sysom。 默认配置使用的nginx对外端口为80，可以通过 `export SERVER_PORT=xxx` 来设置。

| 的内网IP是通过 | ip -4 route \| grep -v docker |  |
|---|---|---|
| export SERVER LOCAL IP=xxx.xxx.xxx.xxx _ _ |  |  |
|  |  | 来设 |

2. 首次部署初始化。
i. 首先设置本地IP（不能是虚拟网卡诸如docker0的IP，可以用 ip -4 route | grep -v docker 查看，假设查询出来是192.XXX.XXX.XX，注意下面的IP要替换成实际部署环境的IP）。

```
export SERVER_LOCAL_IP=192.XXX.XXX.XX
```

ii. 使用以下命令进行启动。

```
bash -x /usr/local/sysom/init_scripts/server/init.sh
```

**重要**

如果初始化阶段长时间卡在systemctl restart grafana-server，执行超时后再次执行上述命令即可。 Alibaba Cloud Linux 当服务日志输出下列日志表示部署成功：

```
Oct 10 12:58:51 mfeng bash[3217754]: /usr/local/sysom/init_scripts/server Oct 10 12:58:51 mfeng bash[3217754]: + for dir in `ls` Oct 10 12:58:51 mfeng bash[3217754]: + '[' -d init.sh ']' Oct 10 12:58:51 mfeng bash[3217754]: + for dir in `ls` Oct 10 12:58:51 mfeng bash[3217754]: + '[' -d stop.sh ']' Oct 10 12:58:51 mfeng bash[3217754]: + sed -i 's/^FIRST_INIT_DONE=0/FIRST_INIT_DONE=1/g' /usr/local/sysom/init_scripts/server/init.sh
```

### 访问和登录

**浏览器要求**

建议Safari版本15.6.1，Chrome版本109.0.5414.119，Microsoft Edge版本110.0.1587.50以上。

**操作步骤**

1. 打开浏览器，在地址栏输入“http://部署服务器的ip”（例如：http://172.XX.X.XXX），按“Enter”。

**说明**

HTTP默认端口为80，请确认防火墙已开通80端口。
2. 打开登录界面，如图所示，输入用户名和密码登录。（请向运维人员获取默认的用户名和密码）。

**修改密码**

为了您的系统安全，建议立即修改admin的密码。
1. 单击“账户密码修改”，输入用户名、原始密码和新密码并确认。
2. 单击“修改密码”，密码修改完成。
Alibaba Cloud Linux 参数说明如下表所示：

| 参数 | 说明 |
|---|---|
| 密码 | 设置登录用户密码需要满足以下要求： SysOM 2.1版本之前没要求。 SysOM 2.1之后的版本要求：密码不能少于8位且必须包含英文字母、数字、特殊字符三种及以上。 |

### 主机管理

#### 概述

作为SysOM管控界面，承担管理操作系统的集群增删、主机增删、终端操作系统等功能。您可以通过主机管理界面操作将需要管理的机器添加进管理界面，也可以一键登录到对应的机器进行shell操作系统。

#### 创建集群/批量导入集群

**创建集群**

**操作步骤**

1. 进入**主机管理**菜单，在下拉菜单中单击**集群列表**进入**集群管理**页面。
2. 单击**新建集群**打开新建集群弹出框，输入以下参数：

| 参数 | 说明 |
|---|---|
| 集群名称 | 设置集群名称需要满足以下要求：集群名称长度应小于128字符。 |
| 备注信息 | 输入集群的备注信息。 |

3. 单击**确认**，完成集群创建。如下图示：
Alibaba Cloud Linux

**批量导出集群**

**操作步骤**

1. 首先勾选需要导出的集群。
2. 然后单击“导出集群”按钮即可导出所选集群。如下图示：

**操作步骤**

1. 首先单击集群页面的“批量导入”按钮。
2. 单击“批量导入”弹出“批量导入”弹出框，单击“模板下载”将模板下载到本地。
3. 填入步骤2中的参数并保存文件。单击“单击上传”，选中保存的文件，单击“确认”完成集群批量导入。如
下图示： Alibaba Cloud Linux

#### 删除集群/批量删除集群

**删除集群**

1. 在集群列表中找到想要删除的集群。
2. 单击**操作**列的**删除**弹出确认删除提示框，单击**OK**即可将该集群信息删除。
1. 批量删除集群，选中需要删除集群的复选框，或者选中**集群名称**前的复选框选中所有集群。
2. 单击列表右上角的**批量删除**，完成集群的批量删除。

**说明**

包含主机的集群不允许被删除，若想删除则需要将主机删除或移出集群。

#### 导入主机/批量导入主机

**前提条件**

已成功创建集群。

**操作步骤**

**导入主机步骤**

i. 进入**主机管理**菜单，下拉菜单中选择单击**主机列表**进入**主机管理**页面。 Alibaba Cloud Linux ii. 单击**新建主机**打开新建主机弹出框，输入以下参数：

| 参数 | 说明 |
|---|---|
| 选择集群 | 选择已创建集群。 |
| 主机名称 | 主机名称为该主机在SysOM平台上的名称，需要满足以下要求：主机名称长度应小于100字符。 |
| 用户名称 | 输入被管理主机的用户的名称。 |
| 用户密码 | 输入被管理主机的用户的密码。 |
| IP地址 | 输入被管理主机的IP地址。 说明被管理主机与部署SysOM工具的环境需要保持可联通状态。 |
| 端口 | 输入被管理主机的SSH协议端口。 |
| 备注信息 | 输入备注信息。 |

iii. 单击**确认**，完成主机导入。

**说明**

当主机列表中“主机状态”为“运行中”时，主机导入成功；若为“异常”或“离线”，则导入失败。请检查主机信息、网络连通性及主机状态。 Alibaba Cloud Linux

**批量导入主机步骤**

i. 单击**批量导入**弹出**批量导入**弹出框。 ii. 如果未准备好的导入文件，单击下载导入模板，并填入主机信息。 iii. 单击**单击上传**，选中保存的文件。 iv. 单击**确认**完成主机批量导入。

#### 删除主机/批量删除主机

**删除主机**

1. 在主机列表中找到想要删除的主机。
2. 单击**操作**列的**删除**弹出确认删除提示框，单击**OK**即可将该主机删除。
Alibaba Cloud Linux
1. 选中需要删除的主机的复选框，或者选中**集群名称**前的复选框选中所有主机。
2. 单击列表右上角的**批量删除**，完成主机的批量删除。

#### 导出主机

**操作步骤**

1. 选中需要导出的主机的复选框，或者选中**集群名称**前的复选框选中所有主机。
2. 单击列表右上角的**导出数据**，完成主机数据的导出。

#### 编辑主机

Alibaba Cloud Linux

**操作步骤**

1. 在主机列表中找到想要删除的主机。
2. 单击**操作**列的**编辑**弹出编辑主机框，修改相应主机信息。

**说明**

目前仅支持“选择集群”和“备注信息”的编辑。
3. 单击**确认**即可完成主机信息的编辑。

#### 访问主机

**前提条件**

被访问的主机的“主机状态”为“运行中”。

**操作步骤**

1. 在主机列表中找到想要访问的主机。
2. 单击**操作**列的**终端**，在右侧打开该主机的在线终端，即可在页面访问主机并输入命令。

### 监控中心

#### 概述

监控是运维系统的重要组成部分。SysOM监控中心通过全方位收集、存储和展示操作系统以及典型应用的各项性能指标，用于评估集群软硬件资源使用率和任务负载状况，及时预警、发现潜在的风险因素；为系统性能分析、调优提供准确的数据参考，提升集群运维系统自动化率。

#### 系统监控

**前提条件**

已成功添加一台或多台主机，主机登录权限是root权限。

**操作步骤**

1. 进入**监控中心**菜单，下拉菜单中选择单击**系统监控**进入**系统监控**页面。
Alibaba Cloud Linux
2. 在左侧**机器列表**中单击需要查看的主机，右侧的监控面板，就会显示该主机的系统监控各个指标。
指标项简要说明（指标项较多，这里只列出部分）：

| 指标栏 | 指标项 | 说明 |
|---|---|---|
| Quick CPU/Mem/Disk | CPU Busy | Quick CPU/Mem/Disk：展示整机的整体资源使用情况，包括CPU/Mem/Disk等资源的总额情况。 CPU Busy：整机的CPU使用率。 Sys Load：整机的负载。 RAM Used：整机的内存使用率。 Root FS Used：根文件系统使用率。 CPU cores：CPU个数。 Uptime：机器运行时长。 |
|  | Sys Load |  |
|  | RAM Used |  |
|  | Swap Used |  |
|  | Root FS Used |  |
|  | CPU cores |  |
|  | Uptime |  |
| Basic CPU/Mem/Net/Dis k | CPU Basic | CPU几种状态的占用率情况 （System，User，IOwait，IRQS，idle，Other） |
|  | Memory Basic | Memory使用率基本情况 （Total，Used，Cache，free，swap） |
|  | Network Traffic Basic | 网络流量收发情况 |
|  | Disk Space Used Basic | 磁盘使用率情况 |

Alibaba Cloud Linux

| 其它 | NA | 根据CPU/Mem/Net/Disk深入展开的具体指标项。 |
|---|---|---|

### 宕机中心

#### 概述

宕机问题作为操作系统异常的一种极端情况，往往会对用户的应用产生重大影响。SysOM宕机中心将会为用户提供统一的宕机问题管理，包括宕机监控、已知问题管理、在线分析、解决方案等能力。通过多维度的宕机管理，降低宕机问题对用户的影响，提升用户业务的稳定性。

#### 宕机列表

**前提条件**

已成功添加一台或多台主机，主机登录权限是root权限。 节点端主机有宕机场景，否则SysOM服务端收集到的宕机数据为空。 宕机页面上只会显示以服务端时间为界限的过往时间内的宕机，如果节点因为时区等问题导致节点时间（可通过date命令查看）大于服务端时间将不会显示在宕机中心中。

**操作步骤**

1. 进入**宕机中心**菜单，下拉菜单中选择单击**宕机列表**进入**宕机列表**页面。
2. 在左侧**机器列表**中单击需要查看的主机，右侧的监控面板，就会显示该主机的系统监控各个指标。
指标说明：

| 指标栏 | 指标项 | 说明 |
|---|---|---|
| 核心指标 | 最近30天的宕机 | 最近30天的宕机总数 |
|  | 最近7天宕机总数 | 最近7天宕机总数 |
|  | 月宕机率 | 一个月内宕机的主机数/主机列表机器数 |
|  | 日宕机率（后续修正为“最近7天宕机率”） | 最近7天的宕机的主机数/主机列表机器数 |
|  | 主机名称 | 发生宕机的主机名称 |
|  | IP | 发生宕机的主机IP |
|  | 宕机时间 | 发生宕机的时间 |

Alibaba Cloud Linux

| 宕机列表 |  |  |
|---|---|---|
|  | 内核版本 | 发生宕机的主机的内核版本 |
|  | Vmcore | 是否有vmcore产生 |
|  | 解决方案 | 是否有对应的解决方案 |
|  | 宕机详情 | 跳转查看宕机的详细信息 |

3. 在**宕机列表**的**宕机详情**列，单击**查看**按钮，跳转到宕机详情页面。
4. 单击**录入解决方案**，用户可以根据当前已知的宕机方案来录入解决方案，这样使得后续如果有重复的宕机
时可以通过后台的自动关联功能直接获取宕机解决方案。
5. 输入**解决方案**，单击**确认**，会回跳到宕机详情页面。
Alibaba Cloud Linux
6. **宕机详情**页面的最下面，有宕机调用栈匹配结果，自动匹配调用栈，以及解决方案。

#### 宕机匹配

**前提条件**

宕机列表不为空。

**操作步骤**

1. 进入**宕机中心**菜单，下拉菜单中选择单击**宕机匹配**进入**宕机匹配**页面。
2. 在**相似调用栈**的输入框中输入宕机调用栈，然后单击**查询**按钮。
3. 单击**查询**按钮后，在下端的**宕机列表**中，就能知道，当前调用栈，在已有的宕机列表中，是否有相似的调
用栈，以及调用栈相似度。 Alibaba Cloud Linux
4. 用户可以根据相似度，单击**查看**按钮，可以跳转到对应的**宕机详情**页，查看解决方案。

### 诊断中心

#### 概述

操作系统作为非常底层的软件基础设施，运维难度较高，针对操作系统层面的问题，SysOM为用户提供了全方位的诊断能力，包括：系统健康检查（即一键诊断）、网络/内存/存储/调度深度诊断，通过全方位诊断帮助用户分析操作系统层面的各类问题。

#### 系统健康检查

**前提条件**

在主机管理界面已经成功添加一台或多台主机。 主机登录权限要是root权限（执行sysak需要）。

**功能描述**

系统健康检查功能提供一键式系统健康评估，对系统的配置、SLI、已知问题、日志和硬件进行检查，并详细罗列每一个检查项的检查状态。

**操作步骤**

1. 在输入框中的“实例IP中”输入要诊断的机器IP。
2. 单击**开始诊断**。
3. 单击**刷新**按钮检查任务是否成功。
4. 单击操作栏中的**查看诊断结果**，查看具体的诊断结果。如下图所示：
Alibaba Cloud Linux

#### 调度诊断中心

**前提条件**

在主机管理界面已经成功添加一台或多台主机。 主机登录权限是root权限（执行sysak需要）。

**调度抖动诊断**

**使用场景**

CPU长时间在内核态执行，导致用户态进程长期得不到调度；或者系统长时间关中断，导致CPU无法正常接收时钟中断进而引发调度抖动，导致业务进程突发调度延迟，甚至系统短暂hang。

**功能描述**

记录调度抖动发生的时间点、发生的次数、和抖动的具体数值，可以帮助用户更好的定位调度抖动的根因。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 诊断时间 | 持续诊断时长（时间单位：s） | 默认为20s |
| 诊断阈值 | 延迟的阈值（时间单位：ms），超过这个阈值的延迟样本将会被记录，低于阈值的延迟样本将会被忽略 | 默认为20ms |

**在线诊断**

Alibaba Cloud Linux
**事件总览：**目前有3类事件：调度延迟、sys延迟和irq延迟。不同的事件由具体的告警与否（及颜色）来
分辨。蓝色表示有告警事件发生，绿色表示正常（下图为异常时的数据展示）。
**抖动时间线图：**记录了调度抖动发生的时间点、发生的次数和抖动的具体数值（下图为异常时的数据显
示）。
**调度抖动详情：**将调具体的度抖动事件以表格的方式展示出来，下面是表中各列指标说明（下图为异常时
的数据显示）。

| date | class | latency | cpu | current | stamp | extern |
|---|---|---|---|---|---|---|

Alibaba Cloud Linux

| 表示调度抖动告警事件发生的日期 | 表示具体的调度抖动事件类型。目前有调度延迟、sys延迟和irq延迟3类 | 具体的抖动延迟值，单位 ms | 调度抖动告警发生的cpu号 | 受干扰的当前任务名字和pid | 发生调度抖动告警时的机器上的时间戳 | 额外信息。不同的 class有不同的额外信息： 调度延迟： nr running表 _ 示CPU队列上的排队的任务数量，prev表示当前CPU上前一个任务。 sys延迟：发生调度抖动告警时的上下文堆栈。 irq延迟：发生调度抖动告警时的上下文堆栈。 |
|---|---|---|---|---|---|---|

**系统负载分析**

**使用场景**

系统负载是服务器运维中的一个典型指标，可以用来评价系统是否产生运行瓶颈，而通过分析系统负载可以进行资源调度让业务更合理化的利用资源。通常来说，影响系统负载的有多方面因素，包括业务并发数量、 IO吞吐、内存压力等，甚至某些系统错误也会导致负载高。因此，当系统负载指标大于某个阈值时，需要及时的进行处理。

**功能描述**

SysOM负载分析诊断功能综合分析当前系统负载的影响面，给出主要进程的负载贡献度，在必要时还提供系统热点函数的火焰图，供用户进行更细粒度的分析，诊断负载异常的真实原因。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |

Alibaba Cloud Linux

**在线诊断**

**事件总览：**显示当前系统负载，并诊断负载是否对系统sys utils、硬中断、软中断、io有影响。
**进程分布：**诊断当前系统R和D状态的分布情况和导致系统负载高的贡献度。
**调度火焰图：**显示系统调度火焰图，可直接查询导致负载高的热点函数。

#### 存储诊断中心

**前提条件**

在主机管理界面已经成功添加一台或多台主机。 主机登录权限是root权限（执行sysak需要）。

**IO时延分析**

**使用场景**

Alibaba Cloud Linux 本功能主要应用于排查IO流量积压、存储设备异常等情况。此类异常情况容易造成IO请求处理慢，IO延迟高。从而造成机器性能损失或者明显抖动等情况。

**功能描述**

记录存储设备的历史IO延迟水位，并且统计每分钟访问IO延迟偏离历史水位的次数，用于快速定位导致IO 延迟偏高的位置。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 诊断时长 | 持续诊断时长（时间单位：s） | 必填，默认为10s |
| 时间阈值 | 保留IO延迟大于设定时间阈值的IO（时间单位： ms） | 必填，默认为1000ms |
| 目标磁盘 | 需要检测的磁盘名称，如sda，sdb等。 | 选填（不指定则诊断所有磁盘） |

**在线诊断**

**iolantency****总览：**表示在一个诊断周期内，捕捉到的超时IO的个数。
个数为0时，check result 的状态为normal，字体显示绿色，表示当前无异常的慢IO。 个数不为0时，check result 的状态为abnormal，字体显示红色，表示当前存在超出阈值的慢IO。

**说明**

注意：阈值在发起诊断的时候可以指定，不指定情况下，默认为1000ms，在诊断结果最右侧支持磁盘的checklist选择展示不同磁盘的数据，切换数据展示（下图为异常时的数据展示）。
**整体****IO****时延分布：**这部分展示IO整体在OS以及磁盘各个存储链路上的延迟分布，每个框图中的指标解读
为： 左上角为链路名，分别表示IO在经过此路径的延迟损耗，其中主要包括OS、Disk两部分，又根据IO的生命周期，进一步将OS中细分为block、driver、complete三部分（分别表示内核通用块层、驱动、 IO完成后回收三部分）。 Alibaba Cloud Linux 右上角表示在此链路耗时占整体耗时的百分比。 中间的max_us、avg_us、min_us则分别表示IO在此路径上的最大延迟、平均延迟、最小延迟，单位 us（下图为异常时的数据显示）。 单**IO****时延****metrics****展示：**该部分将捕捉到的每一个超时IO，通过时序数据曲线的方式展示出来，X轴为时间日期，Y轴为延迟（单位us），图中有5条曲线，分别表示每个IO的total delay、block delay、 driver delay、disk delay、complete delay，可以看出这个是更细粒度的针对每一个IO在存储各链路上的延迟分布（下图为异常时的数据显示）。
**Top10 IO** **详情：**这部分展示了IO总延迟大小排在前TOP10的IO的更多细节。
time：表示检测到此超时IO的时间日期，精确到ms。 abnormal：表示此IO延迟消耗最大的原因，以“延迟最大的路径（此路径耗时：IO整体耗时单位）”形式展示。 iotype：表示具体的IO操作，各字母缩写参考： W：Write R：Read S：Sync FWF：分别表示Flush/Write/FUA（force unit acess） M：Metadata D：Discard sector：表示此IO要访问磁盘的扇区编号。 datalen：表示此IO要访问的数据长度，单位byte。 comm：表示此IO的生产者进程名。 pid：表示此IO的生产者进程ID。 cpu：表示此IO在生命周期中的cpu轨迹，即由哪个cpu产生、又由哪个cpu派发、以及磁盘完成此IO 由哪个cpu响应的中断（下图为异常时的数据显示）。

**IO 流量分析**

**使用场景**

Alibaba Cloud Linux 此功能主要分析系统中的IO流量归属，例如想知道此时系统IO流量集中在哪个进程或者集中在哪个文件汇总，一般在IO Burst问题中会应用较多。

**功能描述**

此功能主要分析系统中的IO流量归属。诊断会根据此时系统的状态，检测不同磁盘下的IO流量，并分析IO流量的组成和IO流量大发生的原因（如有）。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 诊断时长 | 持续诊断时长（时间单位：s） | 必填，默认为15s |
| 目标磁盘 | 需要检测的磁盘名称，如sda，sdb 等。 | 选填（不指定则诊断所有磁盘） |

**在线诊断**

**诊断结论：**这部分展示一个summary信息，如在诊断期间检测到了多大的IO流量（通过iops、bps表示
在result列），产生这么大的流量的原因是什么（展示在reason列，包括信息有：产生流量大的进程及其访问的磁盘，进程产生的iops、IO吞吐和访问的目标文件。其中针对kworker刷脏这类异步IO，支持对实际写buffer IO进程的溯源能力），以及相关处理建议。 在诊断结果最右侧支持磁盘的checklist选择展示不同磁盘的数据，注意切换的是即将介绍的磁盘IO流量分析、进程IO流量分析、进程IO块大小分析这三部分的数据展示： Alibaba Cloud Linux
**磁盘****IO****流量分析：**该部分展示诊断期间，统计到的磁盘IO流量，支持通过磁盘的checklist选择展示不同
磁盘的数据，主要字段： diskname：磁盘/分区名称 r_rqm：诊断期间合并读操作的次数 w_rqm：诊断期间合并写操作的次数 r_bps：诊断期间读IO吞吐 w_bps：诊断期间写IO吞吐 wait：每个I/O平均所需的时间 r_wait：每个读操作平均所需的时间 w_wait：每个写操作平均所需的时间 util%：该硬盘设备的繁忙比率
**进程****IO****流量分析：**该部分展示诊断期间，进程级别IO流量，支持通过磁盘的checklist选择展示不同磁盘
的数据，主要字段： comm：进程名 tgid:pid：进程id信息 iops_rd：进程贡献的读iops bps_rd：进程贡献的读bps iops_wr：进程贡献的写iops bps_wr：进程贡献的写bps flushIO：表示此进程产生的flush IO个数 device：消费IO的目标磁盘 file：产生IO的来源文件其中尤其注意到，该功能支持kworker刷脏的IO溯源能力，所以可以看到在kworker进程下面存在子项， 展开可以看到实际产生脏页（写buffer io）的进程。
**进程****IO****块大小分析：**该部分展示诊断期间，进程级别IO提交到OS块层的块大小分布，支持通过磁盘的
checklist选择展示不同磁盘的数据，其中pat_WNK，表示IO大小为nKB以内的IO个数占比，large则表示大于512KB的大块IO的占比。

**IO hang 诊断**

**使用场景**

当存储设备异常时，业务进程的IO请求长时间得不到响应导致业务进程Hang住。

**功能描述**

监控系统每个存储设备的IO访问路径上是否存在IO HANG 问题。（检测出问题后，可以选择将IO 流量切换到正常的存储设备上，隔离异常的存储设备）。 Alibaba Cloud Linux

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 诊断时长 | 持续诊断时长（时间单位：s） | 必填，默认为10s |
| 时间阈值 | 保留IO延迟大于设定时间阈值的 IO（时间单位：ms） | 必填，默认为5000ms |
| 目标磁盘 | 需要检测的磁盘名称，如sda，sdb 等。 | 选填（不指定则诊断所有磁盘） |

**在线诊断**

**IO HANG** **总览：**表示在一个诊断周期内，检测是否有IO HANG。
无IO HANG 时，check result 的状态为normal，字体显示绿色。 有IO HANG 时，check result 的状态为abnormal，字体显示红色。 而Number of OS HANG 或者Number of Disk HANG，分别表示IO HANG 在OS或者磁盘的IO个数 （下图为异常时的数据展示）。 在诊断结果最右侧支持磁盘的checklist选择展示不同磁盘的数据，（如无IO HANG 异常磁盘则显示 overview一个选项），切换数据展示： Alibaba Cloud Linux
**TOP 10****详情：**这部分展示了HANG住持续时间的前TOP 10个IO的详情。
time：表示检测到此IO HANG的时间日期，精确到ms。 abnormal：表示此IO HANG异常的地方，以“HANG的异常点（具体原因）HANG了多久”形式展示。 iotype：表示具体的IO操作，如Write/Read/Discard 等等。 sector：表示此IO要访问磁盘的扇区编号。 datalen：表示此IO要访问的数据长度，单位byte。 iostate：表示此IO的状态。 inflight：表示未完成。 complete：表示已经标记完成。 cpu：表示此IO由进程在哪个cpu发起。 comm：表示此IO的生产者进程名。 pid：表示此IO的生产者进程id。 file：表示此IO的文件路径（下图为异常时的数据展示）。

#### 网络诊断中心

**前提条件**

在主机管理界面已经成功添加一台或多台主机（延迟诊断需要两台以上的机器）。 主机登录权限是root权限（执行sysak需要）。

**丢包诊断**

**使用场景**

网络是集群提供服务的唯一窗口，其稳定性将直接决定了集群服务的可用性。受到硬件设备、网络环境等因素的影响，网络系统不可避免地会出现多种丢包场景。及时观测到网络丢包行为，并溯源丢包源头，第一时间进行运维决策，消除丢包根源，对于服务稳定性保障具有重要的意义。

**功能描述**

SysOM丢包诊断通过记录丢包事件、丢包发生的硬件或网卡设备、丢包点等，并进一步分析丢包的原因， 帮助用户诊断定位网络丢包的问题。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 运行时间 | 持续诊断时长（时间单位：s） | 必填，默认为10s |

Alibaba Cloud Linux

**在线诊断**

丢包诊断以表格方式呈现，具体解析如下： 时间戳：显示时间信息。 网卡名称：如果是硬件或者网卡相关丢包，则会显示网卡名称。 丢包点：丢包点的形式是：内核丢包函数名+丢包点偏移+丢包次数。 丢包计数：主要展示当前周期内snmp、dev、netstat等相关丢包指标的变化情况。 丢包原因：显示丢包原因。

**抖动诊断**

**使用场景**

网络报文在收发过程中，受到各种不可控因素（如外部网络质量、系统资源调度等）影响，导致网络出现抖动现象。出现抖动的时候，可能网络数据包状态完全是正常的，但仍需对网络抖动进一步溯源，进一步锁定住网络抖动问题根源。

**功能描述**

基于ICMP报文，测出ping发起端的报文时延（发送路径）以及ping接收端的报文时延（接收路径）。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 运行时间 | 持续诊断时长（时间单位：s） | 必填，默认为10s |

**在线诊断**

（需要在节点上跑一个ping命令，如果机器有流量也可以）
1. 在输入框中输入诊断参数。
2. 单击**开始诊断**按钮开始诊断。
3. 在单击**开始诊断**按钮以后，单击表格右上方的刷新按钮，检查任务是否成功。
Alibaba Cloud Linux
4. 可以单击操作栏的**查看诊断结果**按钮查看诊断的结果，诊断的结果会在下方显示。

**重传诊断**

**使用场景**

由于网络拥塞等原因导致业务进程的TCP连接发生大量重传。

**功能描述**

记录重传的时间、IP、TCP socket 所处的状态和拥塞情况，帮助用户了解网络重传发生的情况。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |
| 运行时间 | 持续诊断时长（时间单位：s） | 必填，默认为10s |

**在线诊断**

Alibaba Cloud Linux 重传诊断以表格方式呈现，具体解析如下： 时间戳：显示重传时间。 ip 地址：五元组信息。 tcp 状态：tcp sock 所处的状态。 拥塞状态：拥塞机制所处的状态。

**时延诊断**

**使用场景**

和网络抖动诊断使用场景类似，由于受系统配置、网络质量等因素影响，导致网络出现了较大的传输延迟， 而该延迟将直接决定网络服务的时延。因此，如何快速、清晰地将数据包在网络数据传输整个过程中的展开出来，并诊断出导致网络时延原因的根源，对保障系统服务的稳定具有重要意义。

**功能描述**

抖动诊断目前仅支持icmp报文，即ping。其包含两个部分，一个是ping发起端的报文时延，即发送报文路径，另外一个是ping接收端的报文时延，即接收报文路径。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 源实例IP | 源节点IP | 必填 |
| 目标实例IP | 目的节点IP | 必填 |
| 运行时间 | 持续诊断时长（时间单位：s） | 必填，默认为10s |
| 追踪包数 | 模拟发包的最大报文数 | 必填，默认为100 |

Alibaba Cloud Linux

| 间隔毫秒数 | 模拟发包时两次发包的间隔毫秒数（时间单位：ms） | 必填，默认为1000ms |
|---|---|---|
| 报文协议 | 模拟发包的报文协议 | 必填，默认为ICMP |

**在线诊断**

发送报文路径：发送报文路径是ping的发起端的ICMP报文时延信息，包含： 内核发送：表示icmp echo报文在内核发送路径的时延。 外部链路：表示icmp报文在外部链路的耗时。 内核接收：表示icmp echo reply 报文内核接收路径的时延。 接收报文路径：接收报文路径是ping的接收端的icmp报文时延信息，包含： 内核接收：表示icmp echo报文在内核接收路径的延迟。 内核发送：表示ICMP echo reply 报文内核发送路径延迟。

#### 内存诊断中心

**前提条件**

在主机管理界面已经成功添加一台或多台主机。 主机登录权限是root权限（执行sysak需要）。 Alibaba Cloud Linux

**内存大盘**

**使用场景**

内存是一种重要的计算资源。清楚地掌握机器内存的动态有助于提前发现乃至阻止应用出现异常的风险。因此，SysOM内存大盘提供了查看当前整机内存情况（包括内核、用户态）的功能。用户可以在内存大盘中纵观集群的内存情况，做到运筹帷幄。

**功能描述**

内存大盘展示了机器当前的内存占比（包括内核、用户态的占比）情况，通过收集内存占比情况，用于分析机器运行中的潜在风险，让运维人员可以做到对风险的提前感知、提前发现。减少应用异常的风险。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填 |

**在线诊断**

**内存事件：**主要对内存相关风险一键检查，快速识别系统是否存在内存问题。
内存利用率：系统内存利用率。 内存泄漏：排查系统是否存在泄漏，以及泄漏的类型，目前支持slab, vmalloc 和伙伴系统三种泄漏识别。 memcg残留：评估memory cgroup 是否存在残留，过多的残留会严重影响系统性能，以及造成统计数据异常。 内存碎片化：评估系统是否存在内存碎片化，内存碎片化会导致系统性能下降。
**内存总览（****Overview****）：**内存总览展示系统所有内存的使用情况，实现内存的可维可测可追踪
（1+1+1=3），一般情况下总内存=内核内存（kernel）+应用内存（app）+ 空闲内存（free），在下一部分将会进一步细分内核内存和应用内存。 Alibaba Cloud Linux 总内存 kernel：表示操作系统内核内存总使用量。 app：表示用户态程序内存总使用量。 free：系统空闲内存。 内核内存：内核态内存，我们重点关注Sunreclaim，伙伴系统的使用量，我们通常说的内存泄漏通常都是这两个指标异常。 Sreclaimable：Slab可回收内存。 Sunreclaim：Slab不可回收内存。 PageTables：内核页表占用内存。 Vmalloc：内核调用vmalloc分配的内存。 KernelStack：进程的内核堆栈总内存。 AllocPages：内核调用alloc_pages等接口直接从伙伴系统分配的内存量，这类内存无法通过任何节点文件获取，使用过多会造成内存黑洞。 应用内存=>用户态内存，我们重点关注anon，shmem，filecache。 filecache：文件缓存内存，这类内存可以通过drop caches 回收。 anon：匿名内存，程序堆和栈内存，匿名内存占用过多，需要评估业务进程是否有内存泄漏，系统是否开启了透明大页。 mlock：系统锁住的内存量。 huge：hugetlb大页内存量。 buffer：块设备以及文件系统元信息占用的内存量。 shmem：共享内存（tmpfs）。业务进程退出后，tmpfs文件没有被删除或者tmpfs文件在打开状态下，直接被删除，都会导致shmem泄漏。
**进程内存：**以进程维度按内存大小排序，并分解成匿名内存，文件缓存和共享内存。
Alibaba Cloud Linux
**Cache Top**：展示Cache占用最多前五个文件和对应的进程。

**Cache 分析**

**使用场景**

此诊断功能一般用于分析当前系统内存Cache使用情况，可应用于分析系统Cache增大或容器使用Cache 较多等情况。

**功能描述**

分析容器，容器组，整机或者整机引入cgroup的cache内存及内存占用来源的文件，同时根据每个文件再详细分析引入的active cache和inactive cache。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP | 必填。 |
| 容器 | 容器ID或者pod名 | 必填，默认填空字符串""。 |
| 诊断类型 | 诊断类型： all：诊断实例上所用容器cache。 host：诊断实例主机cache。 pod：诊断pod内部cache。 container：诊断容器内部cache。 | 必填，默认填"all"。 |

**在线诊断**

Alibaba Cloud Linux 缓存排序：对缓存占用最多的几个文件的组成进行分析展示。

**OOM 诊断**

**使用场景**

业务进程内存泄漏容易导致系统发送OOM，当OOM发生时伴随着大量内核日志，而这些内核日志往往难于分析。

**功能描述**

本项诊断功能可以帮助用户定位内存泄漏的位置，并分析导致内存泄露的原因。

**诊断参数**

| 参数名 | 参数说明 | 是否必填 |
|---|---|---|
| 实例IP | 目标Node节点的IP。 | 必填 |
| 诊断时间 | 指定检测某个过去的时间，不指定代表检查最近一次，填写格式为：Unix毫秒时间戳。 | 选填 |

Alibaba Cloud Linux

**在线诊断**

oom分析总结果和建议（下图为异常时的数据展示）： 触发oom的进程和oom的次数（下图为异常时的数据展示）： 当前内存的水线和使用情况（下图为异常时的数据展示）： 使用内存进程的排序（下图为异常时的数据展示）： Alibaba Cloud Linux

#### 自定义诊断中心

**前提条件**

在主机管理界面已经成功添加一台或多台主机。

**操作步骤**

1. 在输入框中输入诊断参数。
2. 单击**开始诊断**按钮开始诊断。
3. 在单击**开始诊断**按钮以后，单击表格右上方的刷新按钮，检查任务是否成功。
4. 可以单击操作栏的**查看诊断结果**按钮查看诊断的结果，诊断的结果会在下方显示。如下图所示：

#### 离线导入功能

**使用场景**

Alibaba Cloud Linux 当目标机器没有被纳入管理，或者网络不通时，可以在机器上安装SysAK，然后直接执行SysAK命令进行诊断，最后将诊断结果在前端离线导入即可生成一条诊断记录，在前端以图形化的方式展示诊断结果。

**使用方式**

目前，在SysOM诊断中心的各个模块下基本实现了离线导入功能。下面将以调度诊断为例子，介绍离线导入功能的使用方法。
1. 单击右上方的**离线导入**按钮。
2. 输入实例ip，该实例ip不做校验，只用于区分不同机器离线导入的结果。
3. 在弹窗的离线日志中，输入离线日志（sysak命令在节点侧执行命令后，终端的输出结果）。
4. 单击**确认按钮**，在下方结果中查看结果。

### 日志中心

#### 概述

日志中心将会为用户提供日志审计的功能，便于管理员监控、管理所负责集群的运维情况。

#### 审计日志

**前提条件**

成功部署SysOM工具。

**操作步骤**

1. 进入**日志中心**菜单，下拉菜单中选择单击**审计日志**进入**审计日志**页面。
2. 在**审计日志**界面中，会展示所有接口调用的情况。日志列表简要说明：

| 列表名 | 说明 |
|---|---|

Alibaba Cloud Linux

| 时间 | API接口访问时间。 |
|---|---|
| 用户 | API接口调用的用户。 |
| 源IP | 用户源IP。 |
| 请求URL | 接口API。 |
| 请求方法 | 接口API的请求方法，GET/POST等。 |
| 返回状态 | 接口返回码，用于判断成功或者失败。 |
| 行为类型 | 接口的行为，操作行为，登录行为等。 |

#### 任务日志

**操作步骤**

1. 进入**日志中心**菜单，下拉菜单中选择单击**任务日志**进入**任务日志**页面。
2. 在**任务日志**界面中，会展示诊断任务的情况。日志列表简要说明：

| 列表名 | 说明 |
|---|---|
| 时间 | API接口访问时间。 |
| 任务ID | 诊断中心中发起诊断的ID。 |
| 状态 | 诊断任务成功或者失败。 |
| 参数列表 | 发起诊断任务请求的入参列表。 |

#### 告警日志

**操作步骤**

1. 进入**日志中心**菜单，下拉菜单中选择单击**告警日志**进入**告警日志**页面。
2. 在**告警日志**界面中，会展示所有告警消息的情况。日志列表简要说明：

| 列表名 | 说明 |
|---|---|

Alibaba Cloud Linux

| 告警时间 | 告警时间。 |
|---|---|
| 告警级别 | 告警级别，成功success，失败error。 |
| 类型 | 告警类型，目前是notification。 |
| 是否已读 | 告警是否已读。 |
| 告警内容 | 告警具体内容。 |

### 热补丁中心

#### 概述

内核热补丁，也叫hotfix。是一种以模块化的方式给Linux内核打补丁而无需重启系统的一项技术。基于这种技术，管理员可以在不重启机器的情况下，修复内核的BUG或者是安全漏洞，以此来提升系统的可用性以及稳定性。SysOM热补丁中心提供便捷的界面设计，允许用户通过简洁明了的方式制作热补丁，降低热补

#### 部署

热补丁中心在制作热补丁的时候需要用到较多的CPU资源。hotfix的制作在SysOM服务器上，一台机器既充当服务器，也充当构造器，这对机器的性能有较高的要求。如果希望热补丁的构建时长能够缩短，建议配置 sysom-hotfix。 sysom-hotfix-builder。 其配置在/usr/local/sysom/init_scripts/server文件中的描述为：

```
[hotfix] 6_sysom_hotfix [hotfix-builder] 6_sysom_hotfix_builder
```

在conf文件中填写hotfix与hotfix-builder即开启热补丁服务，如果需要关闭该服务，将其从conf文件中删除即可。

### 部署方式

SysOM默认会开启sysom_hotfix_builder服务。确保conf文件中同时填写了[hotfix]与[hotfix-builder]两项服务。 SysOM默认在/usr/local/sysom/init_scripts/server/6_sysom_hotfix_builder/init.sh程序中的nfs目录指向本机。 Alibaba Cloud Linux

```
/bin/bash
```

显示结果如下：

```
SERVER_DIR="sysom_server" HOTFIX_BUILDER_DIR=${SERVER_DIR}/sysom_hotfix_builder VIRTUALENV_HOME=${SERVER_HOME}/virtualenv SERVICE_NAME=sysom-hotfix-builder NFS_SERVER_IP=${SERVER_LOCAL_IP}
```

#### 热补丁列表

在该页面下，输入栏一共有四个，分别是：创建时间、内核版本、热补丁名称以及patch文件名称。以上四个输入栏输入的结果用于筛选转正式包的热补丁。输入筛选的条件，单击**查询**按钮，系统就会使用输入的条

#### 自定义内核版本配置

更多的用户可能会在其场景下维护他们自己的内核版本。因此，SysOM热补丁中心提供一个配置自定义内核版本的功能，以支持用户使用SysOM热补丁平台来制作他们自己维护的内核版本的热补丁。 在使用自定义内核版本的时候需要进行两部分的配置： 操作系统配置。 Alibaba Cloud Linux

**操作系统配置**

在配置操作系统的时候，需要为您的操作系统进行命名，然后配置操作系统的git仓库，以及填入用于构建 hotfix的镜像（如果不填入镜像，系统会使用默认提供的镜像进行hotfix构建）。

**说明**

请注意，配置操作系统的时候请勿使用git仓库方式进行配置。使用git仓库方式进行配置将会耗费大量时间。因此，本文只针对src包的方式进行配置。 在上图的例子中，用户配置了一个名为alinux3的操作系统，由于该操作系统使用源码包的方式进行管理， 而不是使用git源码仓进行管理的，因此在配置该操作系统的时候需要开启《使用源码包》按钮，填入 alinux3操作系统的源码包仓库链接：http://******.******.com/alinux/3/plus/source/SRPMS/；然后填入在构建该系列操作系统的内核热补丁时所采用的镜像：registry.cn-
********.********cs.com/sysom/hotfix_building:alinux3_v1.0（需要确保机器能够直接连接公网）。
（具体链接联系运维同学获取）。配置完成后，在构建alinux3内核版本的内核热补丁时，将会使用所配置的镜像进行构建。 操作系统配置解析：每一个内核版本都会属于某种操作系统的。 例如：3.10.0-123.el7.x86_64 -> Centos 4.19.91- 26.al8.x86_64 ->阿里云服务器操作系统V3。所以，需要配置一个操作系统来系列管理具体的内核版本。 Alibaba Cloud Linux 配置自定义内核版本的前序操作为配置该内核版本的操作系统。完成操作系统的配置后，可以在操作系统名的下拉框中选择已完成配置的系统。然后依次填入该内核版本的全量内核版本号（包括架构）、在git仓库下该内核版本的分支或者tag、该内核版本的kernel-devel包的下载地址以及该内核版本的kerneldebuginfo包的下载地址。

**说明**

本示例中，需要kernel-src包、kernel-debuginfo包以及kernel-devel包，这些包的链接请从 alinux3对应仓库获取。 如图中例子，针对具体内核版本5.10.134-009.1.ali5000.alnx3.x86_64，该内核版本属于alinux3操作系统，而alinux3的操作系统使用源码包管理方式，因此该内核版本的源码来源则填入该内核版本的内核源码包下载地址；对于devel包和debuginfo包相应填入包对应的下载地址。

#### 热补丁制作

在热补丁制作页面中，在输入栏中一共有三个输入栏，分别是内核版本、热补丁名称、文件上传。在该页面

**制作热补丁**

在制作热补丁的时候，如果制作的内核热补丁对应的内核版本属于是自行维护的内核版本（自定义内核）， 输入热补丁制作所需要的参数：内核版本、热补丁名称以及补丁文件。以内核版本5.10.134- 009.1.ali5000.alnx3.x86_64为例，填写热补丁名称test，并上传文件。 选择需要用于制作热补丁的patch。如果文件成功上传至服务器，则会显示图所示的情况（文件名为白色字体）。如果失败，下方的补丁将显示为红色字体。5.10-new-globals.patch的描述如下： Alibaba Cloud Linux

```
#diff-Nupr src.orig/fs/proc/cmdline.c src/fs/proc/cmdline.c
---src.orig/fs/proc/cmdline.c 2021-01-28 04:47:10.915473099 -0500 +++src/fs/proc/cmdline.c 2021-01-28 05:04:23.106898578 -0500 @@-17,3 +17,10 @@ static int __init proc_cmdline_init(void
  return 0;
 }
 fs_initcall(proc_cmdline_init);
```

+

```
+#include <linux/printk.h> +void kpatch_print_message(void) +{ + if(!jiffies) + printk("hello there!\n"); +} diff -Nupr src.orig/fs/proc/meminfo.c src/fs/proc/meminfo.c --- src.orig/fs/proc/meminfo.c 2021-01-28 04:47:10.916473090 -0500 +++ src/fs/proc/meminfo.c 2021-01-28 05:04:23.141898268 -0500 @@-19,6 +19,8 @@
 #include<asm/page.h>
 #include "internal.h"
+void kpatch_print_message(void);
```

+

```
 void __attribute__((weak)) arch_report_meminfo(struct seq_file *m)
 {
 }
@@-55,6 +57,7 @@ static int meminfo_proc_show(struct seq_sreclaimable = global_node_page_state_pages(NR_SLAB_RECLAIMABLE_B);
  sunreclaim
= global_node_page_state_pages(NR_SLAB_UNRECLAIMABLE_B); + kpatch_print_message();
 show_val_kb(m,"MemTotal: ", i.totalram);
 show_val_kb(m,"MemFree: ", i.freeram);
 show_val_kb(m,"MemAvailable: ", available);
```

按照上述给定的参数，在热补丁制作栏中输入所有参数后，单击创建按钮，如果已经有热补丁任务正在构建，则该热补丁任务会显示等待构建，直到上一个任务构建完成： Alibaba Cloud Linux 热补丁任务一共有四个状态：等待构建、正在构建、构建成功、构建失败。如果发现热补丁任务长期处于等待构建状态，请前往builder机器通过命令查看builder状态。

```
ps -aux | grep builder
```

**日志查看**

单击**查看日志**按钮，会跳转到新的页面，该页面将显示该热补丁任务执行所输出的日志信息。

**转正式包及下载**

对于制作成功的热补丁任务，其加载列中的下载按钮将会开放。 单击**下载**按钮可以将打包完成后的热补丁下载到您的机器上。而成功后制作的热补丁也可进行转正式包，如下图所示，需要注意的是，转正后的热补丁无法撤销其正式包状态。 Alibaba Cloud Linux

**自定义版本内核的hotfix制作**

在完成需要制作的内核版本的配置以后，可直接在《热补丁制作》页面通过输入该内核版本即可制作热补丁。 如上述内核版本5.10.134-009.1.ali5000.alnx3.x86_64所示，在完成了该内核版本的配置项添加后，前往热补丁制作页面，按照《热补丁制作》中的步骤填写制作所需参数后，单击添加按钮，即可制作。

**热补丁FAQ**

构建的时候，如果出现cloning kpatch-build时间太长；或者出现构建失败以后说kpatchbuild/kpatch-build: No such file or directory的情况，是因为git克隆kpatch-build仓库失败，此时可能需要检查网络配置，设置代理或者直接在/hotfix_build/hotfix/kpatch_space下直接克隆 https://gitee.com/anolis/kpatch-build.git这个仓库。 构建的时候，如果出现docker运行报错，需要在机器直接运行systemctl enable docker && systemctl start docker来使能docker，建议在部署SysOM前先安装docker。

### 其他运维工具

除了SysOM，Alinux 3 系统同时也提供了许多其他更便捷的轻量级运维工具，比如top、perf、sar等，以便于系统管理员监控系统的各项资源使用情况，对系统性能进行分析和优化。

#### perf

perf是一个强大的性能分析工具，用于在 Linux 系统上进行系统性能分析和调优。它是一个命令行工具集合，可以提供关于 CPU、内存、I/O 和其他系统资源的详细分析数据。该工具通过利用 Linux 内核中的性能事件计数器来实现性能分析。它使用硬件的性能计数器来统计指定事件发生的次数，并结合采样机制来收集性能数据。perf 将 tracepoint 产生的时间记录下来，生成报告，通过分析这些报告，管理员便可以了解程序运行期间内核的各种细节，对性能症状做出准确的诊断。以下是一些 perf工具的常用命令和用法的详细介绍： `perf list` ：列出系统上可用的硬件性能事件和软件事件。该命令将显示不同事件的名称、描述和对应的事件编号。 Alibaba Cloud Linux `perf top` ：以交互方式显示当前运行进程的性能数据。它提供实时的性能数据，并按照 CPU 使用率、内存使用率等进行排序。 `perf top -p <PID>` ：以交互方式显示指定进程的性能数据。使用 `-p` 选项后跟进程 ID（PID） 来监视指定的进程。 `perf stat <command>` ：运行指定的命令，并输出与其关联的性能计数器的统计信息。它提供了有关指定命令运行期间的 CPU、缓存、指令和分支等方面的统计数据。 Alibaba Cloud Linux

| perf stat -e <event1> |  |  |
|---|---|---|
| 件列表作为 | -e | 选项的参数 |

| <event2> <command> |  |  |
|---|---|---|
| 并使用 | <command> | 运 |

`perf record <command>` ：记录指定命令的性能数据，并将其保存到文件中（默认perf.data）。该命令会记录指定命令期间发生的硬件性能事件和软件事件的采样数据。

| perf record -e <event> <command> | ： |
|---|---|
| 事件名称或事件编号，并使用 |  |

`perf report <filename>` ：分析和报告之前使用 `perf record` 命令记录的性能数据。它会显示每个事件的发生次数、调用图、热点函数等信息。 `perf script` ：将记录的 perf数据转换为可读的文本形式。它会将 `perf record` 命令记录的数据转换为可供分析的文本格式。

#### sar

sar （System Activity Reporter）是 sysstat 工具集中的一个命令行工具，它用于收集和报告系统资源使用情况的统计信息。sar可以提供关于CPU利用率、内存使用、磁盘IO、网络流量、进程活动等方面的详细统计数据，并生成可视化的报告，以帮助系统管理员监控和分析系统性能。 以下是sar工具的基本用法：
**查看****CPU****利用率：** `sar -u`
这个命令将显示CPU的使用情况，包括用户态、系统态、空闲和等待IO等。
**查看内存使用情况：** `sar -r`
这个命令将显示内存使用情况，包括物理内存、虚拟内存、缓存和交换空间等。
**查看磁盘****IO**： `sar -b`
这个命令将显示磁盘IO统计信息，包括读写速率、IO请求队列长度等。
**查看网络统计信息：** `sar -n DEV`
这个命令将显示网络设备的统计信息，包括接收和发送的数据包、错误和丢弃的数据包等。
**查看进程统计信息：** `sar -p`
这个命令将显示进程的统计信息，包括进程的CPU利用率、内存使用情况等。 这只是sar工具的一些常用用法示例，还有更多选项和参数可用于自定义显示的统计信息。您可以通过 `man` `sar` 命令来查看完整的sar命令文档及其选项，以获取更详细的信息。 Alibaba Cloud Linux

## 性能调优

本文主要介绍KeenTune的部署、安装、启动和使用。在部署部分会说明单机部署和集群部署的不同方式， 同时也会说明各模块间可分可合来实现不同使用目的。在安装部分会重点说明使用yum源和使用源码进行安装的两种方式，在阿里云服务器操作系统V3上主要是使用yum源安装的方式。在启动部分会重点说明 systemd启动方式，以及所需要的配置管理。使用部分会说明命令行和Web进行任务管控，以及算法可视化的不同操作。

### 文档范围

本文涉及到的操作包括下表所示的各项功能：

| 功能类别 | 功能编号 | 功能名称 | 优先级 | 描述 |
|---|---|---|---|---|
| 基础功能 | 0.1 | KeenTune功能help列表 | P0 | 列出KeenTune的所有CLI及简单使用方式。 |
|  | 0.2 | KeenTune版本查询 | P1 | 查询KeenTue的版本。 |
|  | 0.3 | KeenTune初始化 | P2 | 进行KeenTune各组件的组网初始化，形成组网信息。 |
|  | 0.4 | KeenTune全量回滚 | P2 | 进行全量回退，回到KeenTune启动前的系统状态。 |
| 专家一键调优 | 1.1 | 专家一键调优配置的列表展示功能 | P0 | 列出能够使用的专家一键调优配置文件。 |
|  | 1.2 | 专家一键调优配置的详情展示功能 | P1 | 查看能够使用的专家一键调优配置文件详情。 |
|  | 1.3 | 专家一键调优配置的设置功能 | P0 | 设置一个专家一键调优配置文件。 |
|  | 1.4 | 专家一键调优配置的回退功能 | P0 | 回退一个专家一键调优配置文件。 |
|  | 1.5 | 专家一键调优配置的删除功能 | P1 | 删除一个专家一键调优配置文件。 |
|  | 1.6 | 专家一键调优配置的转换功能 | P2 | 将专家一键调优配置文件转换成智能参数优化配置文件。 |
|  | 2.1 | 智能参数调优配置文件展示功能 | P1 | 列出所有智能参数调优的知识库。 |

| libaba Cloud | Linux 运维指南·性能调优 |  |  |  |
|---|---|---|---|---|
| 智能参数调优 |  |  |  |  |
|  | 2.2 | 智能参数调优任务展示功能 | P2 | 列出当前正在运行的智能参数优化任务。 |
|  | 2.3 | 新建智能参数调优任务功能 | P0 | 执行一个智能参数调优任务。 |
|  | 2.4 | 删除智能参数调优任务功能 | P1 | 删除一个智能参数调优任务。 |
|  | 2.5 | 智能参数调优结果回滚功能 | P0 | 回滚一个智能参数调优任务的修改。 |
|  | 2.6 | 智能参数调优任务中断功能 | P2 | 停止一个智能参数调优任务。 |
|  | 2.7 | 智能参数调优数据持久化存储功能 | P2 | 持久化保存一个智能参数优化任务。 |
| 敏感参数识别 | 3.1 | 敏感参数识别任务展示功能 | P1 | 列出所有敏感参数识别任务。 |
|  | 3.2 | 新建敏感参数识别任务功能 | P0 | 执行一个敏感参数识别任务。 |
|  | 3.3 | 删除敏感参数识别任务功能 | P1 | 删除一个敏感参数识别任务。 |
|  | 3.4 | 中止敏感参数识别任务功能 | P1 | 停止一个敏感参数识别任务。 |
| 调优算法库 | 4.1 | 算法统一框架功能 | P1 | 提供KeenTune参数调优算法的统一框架。 |
|  | 4.2 | 推荐参数值搜索功能 | P2 | 提供参数空间搜索阶段使用的算法模块。 |
|  | 4.3 | 代理模型构建和训练功能 | P2 | 提供参数空间挖掘阶段使用的算法模型。 |
|  | 4.4 | 参数值采样功能 | P2 | 提供参数取值的采样的算法模型。 |
|  | 4.5 | 性能提升指标评估功能 | P2 | 提供损失函数的算法模型。 |
|  | 5.1 | 拓扑结构管控 | P2 | 展示KeenTune各模块及部署环境的拓扑结构图。 |
|  | 5.2 | 专家一键调优特性的可视化管控 | P2 | 提供专家一键调优特性的可视化操作。 |

| 运维指南·性能调 |  |  |  |  |
|---|---|---|---|---|
| 管控和算法可视化 |  |  |  |  |
|  | 5.3 | 智能参数调优特性的可视化管控 | P2 | 提供智能参数调优特性的可视化操作。 |
|  | 5.4 | 敏感参数识别特性的可视化管控 | P2 | 提供敏感参数识别特性的可视化操作。 |
|  | 5.5 | 智能参数调优算法的过程可视化 | P2 | 提供智能参数调优算法的过程可视化。 |
|  | 5.6 | 敏感参数识别算法的结果可视化 | P2 | 提供敏感参数识别算法的结果可视化。 |

### 部署方式

KeenTune提供单机性能优化和集群性能优化两种部署模式。需要注意的是，每一台需要控制参数的机器上都需要部署keentune-target。

#### 单机性能优化

在2.0版本中，KeenTune总共包含**keentuned**，**keentune-ui**，**keentune-target**，**keentune-**
**bench**，**keentune-brain**和**keenopt**六个组件。
其中keentuned提供用户命令行响应用户请求，keentune-target负责执行参数设置，这两个组件是 KeenTune的必备组件，有这两个组件即可进行专家一键式调优。用户需要将keentune-target部署到需要进行调优的机器上，将keentuned部署到与调优机器上或任意与其网络连通的机器上。 智能参数调优功能需要用户部署**keentuned**、**keentune-target**、**keentune-bench**和**keentune-**
**brain** 5个组件到不同的机器上，其中：
keentune-target需要部署在需要进行调优的机器上，负责参数的设置。 keentune-bench需要部署在能够执行benchmark的环境中，负责执行benchmark脚本进行性能评估。 keentune-brain部署在安装了算法相关依赖的环境中，负责执行参数优化算法，给出参数配置组合。以上环境都需要与keentuned保持网络连通或与keentuned在同一台机器上。 Alibaba Cloud Linux keentune-ui是可视化web组件，可以为用户提供web操作页面，需要安装在keentuned所在的机器上。 keenopt是包含自研算法和自研算法框架的算法库，需要安装在keentune-brain所在的机器上，与 keentune-brain自带的TPE、HORD、Random等经典调优算法相比，keenopt可以额外提供 KeenTune团队自研的pms等效率更高的优化算法。

#### 集群性能优化

集群性能优化部署中，用户可以在多个环境上同时运行keentune-target，实现对多个环境同时进行性能优化；也可以在多个环境上同时运行keentune-bench，并与keentune-target对应运行benchmark来进行性能评估。 根据实际业务运行的形态，benchmark工具与实际被测对象的关系是1对多或者多对1的关系，用户可以在 bench和target之间实现1对多或者多对1的映射关系。

### KeenTune安装步骤

**重要**

声明：所有操作需使用root权限。 确定好部署方式和对应机器部署相应KeenTune组件后，本章节会介绍如何安装KeenTune的每个组件。 KeenTune的每个组件都包括使用yum安装和使用源码安装两种方式。其中，使用yum安装更简单，但是使用源码安装可以部署最新版本的KeenTune。 keentuned

```bash
yum install -y keentuned
```

keentune-target Alibaba Cloud Linux

```bash
yum install -y keentune-target
```

keentune-bench

```bash
yum install -y keentune-bench
```

keentune-brain

```bash
yum install -y keentune-brain
```

keentune-ui

```bash
yum install -y httpd mod_ssl yum install -y keentune-ui
```

keenopt

```bash
yum install -y keenopt
```

### 配置和启动

KeenTune的所有配置均在keentuned这个管控组件进行管理，运行keentuned之前编辑配置文件 keentuned.conf。

```
mkdir /etc/keentune/keentuned/conf
```

若 conf 目录不存在则创建：

```
vim /etc/keentune/keentuned/conf/keentuned.conf
```

#### 配置target、brain和bench各组件的ip

如果keentune-target、keentune-brain和keentune-bench没有部署在keentuned所在机器上，则需要在配置文件中配置几个组件所在环境的ip地址。涉及到以下几个配置项：

```
[brain] BRAIN_IP = localhost [target-group-1] TARGET_IP = localhost [bench-group-1] BENCH_SRC_IP = localhost BENCH_DEST_IP = localhost
```

其中，BRAIN_IP为keentune-brain所在环境的ip地址，TARGET_IP为keentune-target所在环境的ip地址，BENCH_SRC_IP为keentune-bench所在环境的ip地址，BENCH_DEST_IP为benchmark脚本运行时的目标地址，一般与TARGET_IP相同[2]。在上面的样例中，IP配置为localhost。 Alibaba Cloud Linux

**说明**

[2] 定义benchmark脚本的时候，我们会将benchmark命令定义为诸如“python3 {remote_script_path} {target_ip}" 或者“bash {remote_script_path} {target_ip}”的形式， 这里BENCH_DEST_IP会填充到{target_ip}的位置，如果定义benchmark命令时没有占位符 {target_ip}，则配置项BENCH_DEST_IP失效。

#### 配置动态优化使用的参数

在配置文件中需要指定动态调优使用的参数（参数PARAMETER），如下面的示例，该参数的值是调优知识库的JSON文件，比如sysctl.json。这些文件在路径/etc/keentune/keentuned/parameter下进行管理。 如果需要自定义动态调优的参数，也需要把文件放到相同的目录下面。

```
[target-group-1] PARAMETER = sysctl.json
```

参数配置文件中有三级定义：domain，参数，参数属性。 在sysctl.json各部分内容的说明如下： 文件sysctl.json定义了参数域为“sysctl”的一组参数，该参数域在keentune-target中定义，包含了使用“sysctl”命令设置的系统参数。 “fs.aio-max-nr”和“fs.file-max”是参数名，定义了具体要设置的参数为“fs.aio-max-nr”和“fs.filemax”这两个系统参数。 参数属性包含dtype，range和step，其中dtype定义了参数取值的数据类型，range定义了参数取值的范围，step定义了搜索参数值时的间隔步长。 range越大搜索空间越大，step越小搜索粒度越小，二者都会使参数优化的准确度提高，相应的需要更多的搜索轮次。

```json
{
 "sysctl":{
 "fs.aio-max-nr":{
"dtype":"int",
 "range":[
 102400,
 10240000
```

`],`

```json
"step":102400
 },
 "fs.file-max":{
 "dtype":"int",
 "range":[
 102400,
 10240000
```

`],`

```json
"step":10240
 }
 }
```

Alibaba Cloud Linux 使用keentune param list命令（需启动keentuned服务后可执行，参考《启动服务》）可以查看当前可用的参数配置文件。KeenTune目前内置了sysctl、nginx、mycnf和nginx等参数的调优配置文件，和 fio、iperf、sysbench和wrk等benchmark参数的调优配置文件。KeenTune可以对系统和应用参数进行调优，也可对benchmark参数进行调优，对benchmark参数进行调优时，也称为智能控压。

```
keentune param list
```

命令执行后显示：

```
Parameter List fio.json iperf.json my_cnf.json nginx_conf.json sysbench.json sysctl.json wrk.json
```

#### 配置动态优化使用的benchmark脚本

运行参数智能优化还需要指定使用的benchmark脚本，我们使用BENCH_CONFIG配置项指定使用的 benchmark脚本，JSON格式的配置文件放在/etc/keentune/keentuned/benchmark/路径下。

```
[bench-group-1] BENCH_CONFIG = wrk_http_long.json
```

JSON格式的benchmark配置文件包含以下内容： benchmark_cmd指定了benchmark脚本的运行方式，这里使用了{remote_script_path}和 {target_ip}两个占位符，{remote_script_path}表示benchmark脚本本身在keentune-bench所在环境中的路径，{target_ip}则对应着配置文件中BENCH_DEST_IP配置项。 items指定了benchmark脚本中会报告哪些性能指标及其权重weight，negative为true时表示这个性能指标我们希望他尽可能高，strict为true时表示这个性能指标不能比baseline更差[3]。

**说明**

[3] 在存在多个性能指标时，由于各指标的权重不同，可能会出现牺牲部分指标使综合得分更高的情况，设定strict则表示这个指标是不能被“牺牲”的。 Alibaba Cloud Linux

```json
{
  "benchmark": [{
      "benchmark_cmd": "python3 {remote_script_path} {target_ip}",
      "local_script_path": "benchmark/wrk/wrk_http_long.py",
      "items": {
        "Requests_sec": {
          "negative": false,
          "weight": 100,
          "strict": false
        },
        "Transfer_sec": {
          "negative": false,
          "weight": 0,
          "strict": false
        },
        "Latency_90": {
          "negative": true,
          "weight": 0,
          "strict": true
        },
        "Latency_99": {
          "negative": true,
          "weight": 0,
          "strict": true
        }}}]}
```

使用keentune param list命令可以查看当前可用的benchmark配置文件，KeenTune内置了fio、iperf、 sysbench和wrk等benchmark工具的配置文件示例，但需要用户手动在运行keentune-bench的环境中安装对应的benchmark工具。

```
keentune param list
```

命令执行后显示：

```
Benchmark List bench_fio_disk_IOPS.json iperf_bench.json sysbench_mysql_read_write.json bench_tpce_db.json bench_tpch_db.json wrk_http_long.json wrk_http_short.json wrk_https_long.json wrk_https_short.json wrk_parameter_tuning.json
```

#### 配置算法

配置项AUTO_TUNING_ALGORITHM和SENSITIZE_ALGORITHM分别用来指定参数智能优化和敏感参数识别使用的算法。目前参数智能优化可用的算法包括HORD，Random，TPE，lamcts*， BGCS*，敏感参数识别可用的算法包括shap，lasso，univariate，gp，xsen，xgboost 。 Alibaba Cloud Linux

**说明**

* 需要安装keenopt使用。

```
[brain] AUTO_TUNING_ALGORITHM = tpe SENSITIZE_ALGORITHM = shap
```

#### 配置集群性能优化

**Target Group**

Target Group用来定义多个keentune-target终端同时进行参数配置的情况，根据不同keentune-target 终端参数配置是否相同，分为以下几种情况：

**不同环境配置相同参数**

```
[target-group-1] TARGET_IP = 192.XXX.X.1, 192.XXX.X.2 TARGET_PORT = XXXX PARAMETER = sysctl.json
```

定义两个不同的环境到同一个Target Group 中，可以实现两个环境始终保持相同的参数配置进行性能优化。

**不同环境配置不同参数**

```
[target-group-1] TARGET_IP = 192.XXX.X.1 TARGET_PORT = XXXX PARAMETER = sysctl.json [target-group-1] TARGET_IP = 192.XXX.X.2 TARGET_PORT = XXXX PARAMETER = sysctl.json
```

定义两个不同的环境到不同的Target Group 中，可以分别优化两个环境的参数，不必保持相同，此时参数智能优化的搜索空间扩大为前一种情况的两倍。

**混合参数配置**

```
[target-group-1] TARGET_IP = localhost TARGET_PORT = XXXX PARAMETER = sysctl.json [target-group-2] TARGET_IP = 192.XXX.X.1, 192.XXX.X.2 TARGET_PORT = XXXX PARAMETER = sysctl.json, nginx.json
```

也可以在一个参数配置中同时兼有两种情况，实现更复杂的调优配置。

**Bench Group**

Alibaba Cloud Linux

**一对多的benchmark配置**

```
[bench-group-1] BENCH_SRC_IP = localhost BENCH_SRC_PORT = XXXX BENCH_DEST_IP = localhost BENCH_CONFIG = wrk_http_long.json [bench-group-2] BENCH_SRC_IP = localhost BENCH_SRC_PORT = XXXX BENCH_DEST_IP = 192.XXX.X.1 BENCH_CONFIG = wrk_http_long.json
```

在localhost上部署keentune-bench，并将localhost和192.XXX.X.1作为目标，分别评估性能。

**多对一的benchmark配置**

```
[bench-group-1] BENCH_SRC_IP = localhost BENCH_SRC_PORT = XXXX BENCH_DEST_IP = localhost BENCH_CONFIG = wrk_http_long.json [bench-group-2] BENCH_SRC_IP = 192.XXX.X.1 BENCH_SRC_PORT = XXXX BENCH_DEST_IP = 192.XXX.X.2 BENCH_CONFIG = wrk_http_long.json
```

在localhost和192.XXX.X.1上分别部署keentune-bench，将192.XXX.X.2作为目标，评估性能。

#### 启动服务

执行以下命令启动服务：

```bash
systemctl start keentuned systemctl start keentune-brain systemctl start keentune-bench systemctl start keentune-target systemctl start httpd
```

### KeenTune的命令行使用

#### 专家一键调优

**keentune profile list**

使用 `keentune profile list` 命令，查看keentune中内置的专家配置文件，显示为available的文件可以在当前环境中使用，显示为active的文件表示当前环境已经激活这个文件。其中custom文件夹是用户定制的文件夹，允许用户增加、修改和删除。 执行如下命令： Alibaba Cloud Linux

```
keentune profile list
```

显示如下：

```
- custom
- application
[available]mysql.conf [available]nginx.conf [available]pgsql.conf [available]redis.conf
- basic
[available]cpu_high_load.conf [available]io_high_throughput.conf [available]net_high_throuput.conf [available]net_low_latency.conf
- ecs
[available]ecs-guest.conf [available]ecs-performance.conf
- tuned
[available]accelerator-performance.conf [available]atomic-guest.conf [available]atomic-host.conf [available]balanced.conf
```

**keentune profile set**

确认过专家配置文件的内容之后，我们使用 `keentuneprofile set` 命令设置mysql.conf使其在当前环境中生效，设置结果有以下几种情况： Recommendation (Manual Settings) 参数推荐和检查步骤： Recommendation：参数无法自动设置，需要参考帮助文档手动操作。 WARNING：参数不支持，可能是环境中没有需要的设备或者没有安装需要的依赖包，参数设置被跳过。 Alibaba Cloud Linux Profile Result (Auto Settings) 参数设置步骤： FAILED：参数设置失败，参数设置被跳过。 此处以MySQL为例：

```
keentune profile set mysql.conf
```

设置结果如下例所示：

```
[+] Recommendation (Manual Settings) [kernel_sec] E0PD: Please use E0PD security feature to avoid meltdown attack. Please refer to https://developer.aliyun.com/*******/*******? spm=a****.********.detail.94.3998*********kc&ex=yitian [WARNING] [cpu] governor: 'governor' can not backup [WARNING] [cpu] min_perf_pct: 'min_perf_pct' can not backup [+] Profile Result (Auto Settings) Group 1 Node 1: localhost [cpu] 1 Succeeded, 1 Failed, 0 Skipped [FAILED] energy_perf_bias: x86_energy_perf_policy: EPB not enabled on this platfo
```

`rm`

```
[sysctl] 6 Succeeded, 0 Failed, 0 Skipped
```

**keentune profile rollback**

使用 `keentune profile rollback` 命令回退所有参数设置，如：

```
keentune profile rollback
```

执行结果：

```
[ok] profile rollback successfully
```

**keentune profile info**

我们可以继续使用 `keentune profile info --name xxx.conf` 命令来查看每个专家配置文件的具体内容，包括调优参数域、调优参数取值等信息。以下为mysql.conf调优文件的详细内容：

```
keentune profile info --name mysql.conf
```

可以看到mysql.conf包括main，net，kernel_mem，kernel_sec和sysctl几个参数域（domain）， 其中main这个参数域为预留参数域，主要处理profile的继承和包含关系，mysql.conf这个profile中包含了ecs-guest.conf这个profile。net，kernel_mem，kernel_sec和sysctl分别对应一个参数域，其中kernel_sec不包含具体实现设置的参数，只包含参数设置推荐（recommend）其他三个参数域在 target中都有对应的实现代码。 Alibaba Cloud Linux

```
[main] include = ecs-guest.conf [net] XPS = different RPS = different smp_affinity = dedicated [kernel_mem] code_hugepage = 1 TLBI = "recommend: TLB range improvement. Please refer to https://developer.aliyun.com/*******/*******? spm=*****.*******.detail.55.399********Nkc&ex=yitian” [kernel_sec] E0PD = "recommend: Please use E0PD security feature to avoid meltdown attack. Please refer to https://developer.aliyun.com/*******/*******? spm=*****.********.detail.94.3998********kc&ex=yitian” [sysctl] kernel.sched_migration_cost_ns = 5000 kernel.sched_min_granularity_ns = 3000000 kernel.sched_wakeup_granularity_ns = 4000000
```

**keentune profile generate**

keentune还提供了能力，如果对当前的专家配置不满意，我们可以通过动态调优对其进行二次优化，使用 `keentune profile generate` 命令可以将专家配置文件转换成用于动态调优的配置文件，如下示例：

```
keentune profile generate --name mysql.conf --output mysql.json
```

可以看到有些参数没有被赋予调优范围[1]，这是由于部分参数只在profile中存在，没有调优配置文件[2]，生成调优配置文件时并不清楚这些参数可能的取值范围，无法进行动态优化，这些参数在调优中会被设置成固定的值。

**说明**

[1] 离散参数使用options字段描述取值范围，连续参数使用range字段描述取值范围。 [2] 根据/etc/keentune/paramter/下存在的所有调优配置文件决定。 Alibaba Cloud Linux

```json
{
    "cpu": {
        "energy_perf_bias": {"dtype": "string","value": "performance"},
        "force_latency": {"dtype": "string","value": "cstate.id:1"},
        "governor": {"dtype": "string","value": "performance"},
        "min_perf_pct": {"dtype": "int","value": 100}
    },
    "disk": {
        "readahead": {"dtype": "string","value": "\u003e4096"}
    },
    "kernel_mem": {
        "code_hugepage": {"dtype": "int","value": 1}
    },
    "net": {
        "RPS": {"dtype": "string","value": "different"},
        "XPS": {"dtype": "string","value": "different"},
        "smp_affinity": {"dtype": "string","value": "dedicated"}
    },
    "sysctl": {
        "kernel.numa_balancing": {"dtype": "int","options": ["0","1"],"value": 0},
        "kernel.sched_migration_cost_ns": {"dtype": "int","range":
[100000,5000000],"step": 100000,"value": 5000
        }
    }
}
```

#### 参数智能调优

**keentune param list**

使用 `keentune param list` 命令可以查看当前可用的参数配置文件，KeenTune目前内置了sysctl、 nginx、mycnf和nginx等参数的调优配置文件，和fio、iperf、sysbench和wrk等benchmark参数的调优配置文件[1]。 使用 `keentune param list` 命令可以查看当前可用的benchmark配置文件，KeenTune内置了fio、 iperf、sysbench和wrk等benchmark工具的配置文件示例，但需要用户手动在运行keentune-bench 的环境中安装对应的benchmark工具。KeenTune可以对系统和应用参数进行调优，也可对benchmark 参数进行调优，对benchmark参数进行调优时，也称为智能控压。

```
keentune param list
```

命令执行后显示： Alibaba Cloud Linux

```
Parameter List fio.json iperf.json my_cnf.json nginx_conf.json sysbench.json sysctl.json wrk.json Benchmark List bench_fio_disk_IOPS.json iperf_bench.json sysbench_mysql_read_write.json bench_tpce_db.json bench_tpch_db.json wrk_http_long.json wrk_http_short.json wrk_https_long.json wrk_https_short.json wrk_parameter_tuning.json
```

**keentune param tune**

确认好调优参数和发压配置文件后，我们可以使用 `keentune param tune` 命令来发起动态调优。 --job参数指定任务名，任务名尽量保证唯一。 --iteration参数指定调优轮次，默认值为100。

```
keentune param tune --job test --iteration 10
```

启动调优之后，KeenTune会将调优任务部署下去，但这并不代表任务已经成功运行起来了，用户需要查看任务日志来确认任务的运行情况。

```
[ok] Running Param Tune Success. iteration: 10 name: test see more details by log file: "/var/log/keentune/test.log"
```

如果调优出问题，可以通过打印日志信息排查：

```
cat /var/log/keentune/test.log
```

如下所示，这里的原因是我们没有安装需要的wrk工具：

```
Step1. Parameter auto tuning start, using algorithm = tpe. Step2. Run benchmark as baseline: [ERROR] prepare for tuning: tuning execute baseline benchmark:bench.group 1-1 msg:ben chmark running stderr: stderr = /bin/sh: wrk: 未找到命令
```

安装wrk之后重新进行调优，tuning正常运行，我们通过日志可以看到整个tuning过程： Alibaba Cloud Linux

```
Step1. Parameter auto tuning start, using algorithm = tpe. Step2. Run benchmark as baseline: [Requests_sec](weight: 100.0)average scores = 80558.773 Step3. AI Engine is ready.
```

调优开始的时候，首先会运行一次benchmark来作为性能基准，下面例子中的示例得分（81203.992） 是判断性能提升或者下降的基准值。

```
Step4. Start tuning, total iteration is 10. [Iteration 1] Benchmark result: [Requests_sec](weight: 100.0)average scores = 81203.992 Current optimal iteration: [Iteration 1]: [Requests_sec]Improved by 0.801% ... [Iteration 10] Benchmark result: [Requests_sec](weight: 100.0)average scores = 86829.539 Current optimal iteration: [Iteration 3]: [Requests_sec]Improved by 15.746%
```

调优过程中的每一轮都会生成一组参数配置并设置，然后运行一次benchmark[2]来判断当前参数配置对性能的影响，日志中会记录每轮调优中每个性能指标的具体数值（86829.539），并记录当前已知的最优参数配置出现的轮次（Iteration 3），和这个最优参数配置相对于基准值的提升幅度（15.746%）

```
Step5. Best configuration dump successfully. File list: /var/keentune/tuning_workspace/test2/test2_group1_best.json Step6. Tuning is finished, checking benchmark score of best configuration. [BEST] Benchmark result: [Requests_sec](weight: 100.0)average scores = 102574.320 [BEST] Tuning improvement: [Requests_sec]Improved by 27.329%
```

由于偶然性的存在，在调优结束之后会设置最优参数并重新执行一次benchmark[3]，来确定最终的性能得分（102574.320）和提升幅度（27.329%）

**说明**

[1] 配置项BASELINE_BENCH_ROUND可以调整benchmark运行轮次，多次运行取均值可以降低偶然性。 [2] 配置项TUNING_BENCH_ROUND可以调整benchmark运行轮次，多次运行取均值可以降低偶然性。 [3] 配置项RECHECK_BENCH_ROUND可以调整benchmark运行轮次，多次运行取均值可以降低偶然性。

**keentune param jobs**

keentune param jobs 命令可以查看所有调优任务的状态：

```
keentune param jobs
```

Alibaba Cloud Linux 显示结果如下：

```
namealgorithmiterationstatusstart_timeend_time testtpe10error2023-03-14 22:51:032023-03-14 22:51:04 test1tpe10error2023-03-14 23:04:152023-03-14 23:04:16 test2tpe10finish2023-03-14 23:09:552023-03-14 23:10:29
```

**keentune param stop**

keentune param stop命令可以中止当前运行的调优任务。

**keentune param rollback**

keentune param rollback命令可以回退调优任务中对参数进行的设置。

#### 敏感参数识别

**keentune sensitize train**

`keentune sensitize train` 命令可以根据调优的数据判断哪些参数是重要的，哪些参数是不重要的。 --data参数指定一个已经完成的调优任务的名字。 --job指定当前敏感参数任务的名字。 --trials参数指定运行多少次敏感参数算法。 此处需要说明，部分敏感参数分析算法，如基于Lasso，mutual information 等模型的简单算法输出较为稳定，不需要多次运行；对于更复杂的算法，如自有算法Xsen，SHAP，或基于XGBoost的分析算法，分析结果存在一定的偶然性，多次运行敏感参数算法可以提高计算的准确性。下面为示例执行命令：

```
keentune sensitize train --data test --job test2_sensi --trials 2
```

其中，test为“参数智能调优”任务运行出来的数据集合路径（请根据《参数智能调优》生成相关数据）。 以下为输出结果：

```
[ok] Running Sensitize Train Success. trials: 2 data: test job: test_sensi see more detailsby log file: "/var/log/keentune/keentuned-sensitize-traintest_sensi.log"
```

日志中会以表格的形式展示不同参数的敏感性和排序

```
+-------------------------------------------------+-------+-------+
|param name                                       |round 1|round 2|
+-------------------------------------------------+-------+-------+
|net.ipv4.icmp_echo_ignore_broadcasts@group-1     |0.0102 |0.0000 |
|net.ipv4.tcp_max_syn_backlog@group-1             |0.0102 |0.0000 |
|net.core.dev_weight@group-1                      |0.0102 |0.0000 |
|net.ipv4.tcp_keepalive_probes@group-1            |0.0102 |0.0000 |
|kernel.nmi_watchdog@group-1                      |0.0102 |0.0000 |
|vm.max_map_count@group-1                         |0.0102 |0.0000 |
|kernel.sched_autogroup_enabled@group-1           |0.0102 |0.0000 |
```

Alibaba Cloud Linux

**keentune sensitize jobs**

keentune sensitize jobs 命令可以查看所有敏感参数任务的状态。

```
keentune sensitize jobs
```

显示结果如下：

```
namealgorithmtrialsstatusstart_timeend_time test2_sensishap2error2023-03-14 23:35:342023-03-14 23:35:34 test2_sensi2lasso2finish2023-03-14 23:45:502023-03-14 23:46:00
```

**keentune sensitize stop**

keentune sensitize stop命令可以中止当前运行的敏感参数任务。

### KeenTune前端页面的部署和使用

#### 环境检查

新环境：确保 keentuned keentune-brain keentune-bench keentune-target keenopt 等组件的安装并服务已启动。 旧环境：只需要确保查看服务已启动即可。

**操作步骤**

1. 查看是否已安装 rpm 包。

```
rpm -qa keentuned keentune-bench keentune-brain keentune-target keenopt
```

2. 查看服务是否已启动。

```bash
systemctl status keentuned.service systemctl status keentune-bench.service systemctl status keentune-brain.service systemctl status keentune-target.service
```

3. 安装与启动。
如果确定服务尚未安装，可按如下步骤安装与启动服务。 Alibaba Cloud Linux i. 首先安装 RPM 包。

```bash
yum install -y keentuned keentune-brain keentune-target keentune-bench keenopt
```

如果其版本较低，需要更新 pip。

```
pip3 install --upgrade pip
```

安装 pip 依赖包。

```
pip3 install tornado==6.1 pip3 install pynginxconfig pip3 install numpy==1.19.5 pip3 install hyperopt==0.2.5 pip3 install requests==2.25.1 pip3 install scikit-learn==0.24.2 pip3 install shap pip3 install xgboost pip3 install pySOT pip3 install torch pip3 install gpytorch
```

**说明**

如果 pip3 下载失败，可以使用清华源尝试下载。 ii. 启动服务。

```bash
systemctl start keentuned keentune-brain keentune-target keentune-bench
```

**说明**

keenopt 仅是自研算法包，无需启动服务。

#### KeenTune前端页面

**说明**

该功能运行的环境需要能够支持图形界面。 通过单击网址<ip>可进入到 KEENTUNE 前端页面。新部署的环境，此时还没有初始化环境的配置，功能是无法使用的。 注意： IP 地址示例如下。 Alibaba Cloud Linux

**组件拓扑管理**

鼠标放在**一键式专家调优**、**智能参数调优**、**敏感参数识别**任意功能框上，即可看到配置环境的提示，或者直接单击图示中的齿轮配置按钮，进入配置页面。 一般情况下，使用的是默认的单机配置即可，复杂配置按需修改配置的内容即可。按照下图操作，实现配置：
1. 单击**示例**，将内容选中复制或者拖至文本框。
2. 单击**check**按钮，实现环境配置的检查与下发。
Alibaba Cloud Linux 生成一个环境的拓扑结构图以及对应的 YAML 配置文件： 单击**返回首页**，开启使用的旅程。 Alibaba Cloud Linux

#### 专家一键调优

在 KeenTune 首页界面单击**一键式专家调优**功能进入专家调优页面，该页面展示了调优专家知识库列表， 用户可根据某一项调优参数直接对环境进行设置，也可以根据调优经验创建自己的知识库。KEENTUNE 默认自带了 5 组专家经验知识库，如下所示展示了专家调优界面及对应的功能操作。 custom 分组置顶，管理用户创建或者通过智能参数调优 dump（详见智能参数调优章节）生成的知识库。新部署时，数量为 0。 application 管理 4 类数据库场景的专家知识库。 basic 管理基础的 cpu、net、io 等 5 个知识库。 ecs 管理适合于 ecs 环境的 2 个知识库。 tuned 管理迁移来自 tuned 的 23 个知识库功能。 按钮说明： 代表删除。 表示复制。 表示编辑。 表示回滚。 表示设置。

**查看 Profile**

通过直接单击知识库的名字可以查看知识库的详细内容，内容展示如下： Alibaba Cloud Linux 单击即可查看详情。 单击**我知道了**或者关闭按钮退出查看详情。

**设置 Profile**

如果想把某个知识库设置到环境中，直接单击其对应的**设置**按钮，选择要设置的组别后单击**设置**即可。 Alibaba Cloud Linux 选择一个group后单击**set**。 参数设置成功后页面弹窗会提示配置成功并显示参数配置成功、失败的个数，对应的配置文件的状态会改为**active**，回滚按钮点亮，同时会显示当前设置的组别及对应机器的 IP。 Alibaba Cloud Linux

**回滚 Profile**

调优结束后，如果想把环境恢复到最初的参数状态，直接单击**回滚**按钮，就可以对参数进行回滚。回滚成功后页面弹窗会提示回滚成功，配置文件状态恢复为**available**，回滚按钮置灰。 当执行回滚后，本组将没有 active 的 profile，此时一级标签将默认收缩。

**复制 Profile**

专家调优针对五个经典场景提供了 5 个默认的专家知识库，方便用户配置体验。考虑到知识库的永久可复用性，不支持修改，删除操作。如果有依据此类知识库，进行按需变更的需求，可以执行先复制，后编辑修改的操作，保证不破坏自带的专家经验知识库的完整性。同时对于自建的知识库也可进行复制修改操作。对想复制的某个知识库单击**复制**按钮，即可实现复制。 Alibaba Cloud Linux 单击**确定**。 可以看到刚复制的知识库已经出现在了列表中，且支持编辑、删除操作。 Alibaba Cloud Linux

**创建 Profile**

除了自带的知识库，以及用户依据自带的知识库复制产生的库以外，用户也可以根据自己的经验，按照指定的格式，手动编辑，创建专属于自己的知识库。单击**创建**按钮进入到创建页面，如下所示，保证知识库名的唯一性，若不清楚知识库的格式，可单击**示例**按钮查看，可以直接复制示例内容再单击**填写**进行粘贴修改。 填写一个唯一的名字，然后填写content，最后单击**确定**进行下发。 Alibaba Cloud Linux 在知识库列表中可以查看，新建的知识库已经在列表中了，支持编辑和删除操作。

**编辑操作**

用户通过复制、创建等生成的自己的知识库文件是支持编辑操作的，可以按需修改，默认的五个知识库是不支持编辑修改的。单击**编辑**按钮即可进入到编辑页面，用户可根据需要进行一些修改操作，类似于创建页面。编辑好后可通过单击知识库名来查看详情验证是否修改成功。 Alibaba Cloud Linux 填写一个唯一的名字，然后填写content，最后单击**确定**进行下发。 查看详情。 Alibaba Cloud Linux

**删除 Profile**

支持用户管理自己生成的知识库，如果不需要某个知识库了，支持删除操作。针对某个想要删除的知识库单击**删除**按钮，弹出删除弹框，单击是即可删除。 删除成功。 Alibaba Cloud Linux custom 列表中已删除刚才创建的知识库。

**列设置**

支持用户只查看某些想看的组别，隐藏掉不想看的部分，或者将自己重点关注的组别固定在首列或者列尾。 单击**列设置**按钮，展示已有的组别。 单击**Profile Count**选项按钮，可以看到 Profile Count 已被隐藏。 Alibaba Cloud Linux 重新单击 Profile Count 选项按钮或者单击【重置】按钮，恢复组别展示鼠标放在各组别按钮上，即可看到对应的**固定在列首**、**固定在列尾**按钮，通过单击对应的按钮将某个组别放在列首或者列尾。单击 Profile Count 的**固定在列首**按钮，可以看到 Profile Count 组放在了列首。 Alibaba Cloud Linux 单击**重置**按钮可恢复默认展示。

#### 智能参数调优

在 KeenTune 首页界面单击**智能参数调优**，进入智能参数调优页面，该页面展示了某个 tuning 任务调优的所有信息，包括任务名、使用算法名、任务状态、调优轮次、配置、耗时等信息及一些功能操作的展示。 单击页面上的**Create**按钮即可进入新建任务页面，如下所示，填入任务的各项配置后即可拉起新的任务。 配置 Bench、Target 服务时可参考示例来配置，注意任务名的唯一性。 Alibaba Cloud Linux 示例如下： 新建的任务已开始运行。 通过直接单击任务名或**Operations**按钮下的**Details**选项即可进入任务详情页面，详情页面主要分为三部分：基本信息、数据分布图、调优过程信息。 Alibaba Cloud Linux 基本信息部分主要展示了和调优任务相关的一些基本信息内容，包括任务名、调优轮次、使用算法、任务耗时等信息，可通过单击 Parameters、任务日志和 benchmark 对应的超链接来查看该任务的调优参数、调优日志和 benchmark 对应的 json 配置文件。 数据分布图部分展示了此次调优任务的benchmark 得分图、算法和 benchmark 运行时间图、参数得分关系图，可通过单击切换按钮分别查看。 调优过程信息部分展示了每轮调优的 benchmark 得分、损失值、当前轮次调优各参数详细信息等内容。 Alibaba Cloud Linux 单击对应任务的**Configuration**选项，即可查看该任务对应的配置文件，该页面展示了各服务对应的 IP、 端口、工作路径、默认算法、target和bench 服务的分组等信息。 单击对应任务**Operations**按钮下的**Log**选项即可进入日志详情页面，该页面展示了任务调优过程中的日志信息，包括所用到的 AI 算法、基线得分、调优轮次、每轮调优的 benchmark 得分以及提升/下降率等信息，可以清楚的了解整个调优过程的详细信息。 单击对应任务**Operations**按钮下的**Rollback**选项即可执行回滚操作，使环境恢复到默认参数设置，回滚成功后会显示回滚成功的提示信息。 Alibaba Cloud Linux 单击对应任务**Operations**按钮下的**Dump**选项即可将本任务最优调优参数固化到专家调优知识库，可在专家调优页面查看结果。 此时专家调优页面已生成固化后的知识库文件。 Alibaba Cloud Linux 单击对应任务**Operations**按钮下的**Rerun**选项即可进入重跑页面，类似于任务新建页面，根据所需修改部分内容，直接拉起任务重跑。 单击对应任务**Operations**按钮下的**Delete**选项即跳出删除弹窗，单击是即可删除当前任务。 Alibaba Cloud Linux 可以看到**04_04_tpe_copy**任务已被删除。 分别勾选两个或多个调优任务，此时**Compare**按钮被点亮，通过单击**Compare**按钮，可以查看对应多个调优任务的跑分对比图。 对比图如下： Alibaba Cloud Linux

#### 敏感参数识别

在 KeenTune 首页界面单击**敏感参数识别**功能进入敏感参数识别页面，该页面展示了某个 train 任务调优的所有信息，包括任务名、使用算法名、训练数据类型、任务状态、训练伦次、耗时等信息及一些功能操作的展示。 单击页面上的**Create**按钮即可进入新建任务页面，如下所示，填入任务的各项配置后即可拉起新的任务。 配置 Bench、Target 服务时可参考示例来配置，注意任务名的唯一性。 Alibaba Cloud Linux Name：输入任务名，确保任务名唯一。 Data：选择一个可供训练的智能参数任务。 Agorithm：选择一个可供训练的算法。 Trial：输入训练轮次。 示例如下： 新建的任务已经开始运行。 Alibaba Cloud Linux 通过直接单击任务名或**Operations**按钮下的**Details**选项即可进入任务详情页面，详情页面主要分为三部分：基本信息、敏感任务对比箱式图、参数敏感信息。 基本信息部分主要展示了和调优任务相关的一些基本信息内容，包括任务名、训练数据类型、所用算法、 耗时等信息。 敏感任务对比箱式图部分展示了此次任务调优参数的箱型图，可以直观的看到每个调优参数对应的敏感度的取值范围。 参数敏感信息部分展示了所有调优参数的详细信息，包括数据类型、取值范围、训练出来的敏感度等信息。 Alibaba Cloud Linux 单击对应任务**Operations**按钮下的**Log**选项即可进入日志详情页面，该页面展示了任务训练过程中的日志信息，包括所用到的采集数据、训练算法、训练轮次、每轮参数的敏感度等信息，可以清楚的了解整个训练过程的详细信息。 Alibaba Cloud Linux 单击对应任务**Operations**按钮下的**Rerun**选项即可进入重跑页面，类似于任务新建页面，根据所需修改部分内容，直接拉起任务重新运行。 当任务正在运行时，如果想停止正在运行的任务，单击对应任务**Operations**按钮下的**Stop**选项停止任务。 Alibaba Cloud Linux 可看任务已经成功停止，状态变为**abort**。 单击对应任务**Operations**按钮下的**Delete**选项即跳出删除弹窗，单击是即可删除当前任务。 Alibaba Cloud Linux 可以看到**04_04_train**任务已被删除。 分别勾选两个或多个敏感任务，此时**Compare**按钮被点亮，通过单击**Compare**，可以查看对应多个敏感任务对比箱式图显示结果。 Alibaba Cloud Linux
