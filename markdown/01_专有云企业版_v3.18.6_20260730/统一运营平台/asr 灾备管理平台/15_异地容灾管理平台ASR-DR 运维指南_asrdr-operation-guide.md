---
title: "灾备管理平台 异地容灾管理平台ASR-DR 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 125
source_pdf: "15_异地容灾管理平台ASR-DR 运维指南_asrdr-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asr/zh/asrdr-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 灾备管理平台 异地容灾管理平台ASR-DR 运维指南

灾备管理中心

## 概述

本文介绍异地容灾管理平台ASR-DR运维的目的、要求、注意事项、以及寻求帮助的方式。

### 目的

指导维护人员对ASR-DR进行预防维护，确保其能够稳定运行。维护人员可以根据本手册的指导，处理维护过程中发现的问题。如果根据本手册无法解决系统问题，请寻求阿里云工程师的技术支持。

### 要求

维护人员必须拥有IT行业技能，包括计算机网络知识、计算机操作知识、问题分析排查能力。 维护人员必须经过相应培训，学习必要的产品操作知识，包括但不限于各模块工具的使用和维护。

**重要**

在维护操作过程中，维护人员务必遵守操作规章，确保人身安全和系统安全。对于用户数据，严格保密， 未经用户书面许可，禁止复制、传播用户数据。

### 注意事项

为了系统运行的稳定，避免意外事故的发生，维护人员需遵循以下事项。

**分层分权管理**

对网络、设备、系统、数据实行分层分权管理，相应业务的维护人员仅拥有完成自身角色任务相对应的权限， 防止越权操作而引起系统故障。

**系统安全**

在对系统进行任何操作前，需清楚的了解操作的结果，避免危险操作影响系统运行。 在操作过程中遇到的问题，需清楚记录以便问题排查和故障处理。

**人身和数据安全:**

操作电气设备时，必须根据设备要求做好安全措施。 需使用安全的设备接入业务网络。 未经授权，严禁对数据进行复制和传播。

**寻求帮助：**

维护人员在系统维护过程中如需相关帮助，可以联系阿里云技术支持获取帮助。 灾备管理中心

## 产品架构

### 组件架构

本文介绍ASR-DR内部及外部依赖的相关组件。

### 服务角色列表

本文介绍ASR-DR的Project、集群、服务、服务角色的详细信息清单，方便运维人员识别和定位故障。

| Project | 集群 | 服务 | 服务角色 | 描述 |
|---|---|---|---|---|
|  |  | asrdr-backend | asrdr- backend.backend | asrdr后端服务角色 |
|  |  |  | asrdr- backend.dbinit | asrdr数据库初始化服务角色 |

| 灾备管理中心 |  |  |  |  |
|---|---|---|---|---|
| asrdr | asrdrCluster |  |  |  |
|  |  |  | asrdr- backend.ServiceT est | asrdr后端服务测试角色 |
|  |  | asrdr-portal | asrdr-portal.ops- poral | asrdr运维平台前端服务角色 |
|  |  |  | asrdr- portal.portal | asrdr运营平台前端服务角色 |

灾备管理中心操作

## 运维常用操作

### 登录容器

本文以登录ASR-DR容器为例介绍登录容器的步骤，登录其他容器的操作步骤类似，您只需要替换相应的服务和服务角色即可。

**背景信息**

本文用到的相应容器列举如下。

| 产品 | 服务 | 服务角色 |
|---|---|---|
| ASR-DR | asrdr | asrdr-backend.backend# |
| POP | webapp-pop | webapp-pop.PopAliyunCom# |
| PolarDB-X | drds-console | drds-console.DrdsConsole# |
| DTS | dts-dts | dts-dts.DtsPortal# dts-dts.DtsMaster# |
| OSS | oss-chiji | oss-chiji.ChijiOssAll# |

**操作步骤**

1. 登录终端。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品列表**页面的**产品** | **集群**搜索框中输入asrdr，在目标集群**操作**列单击**集群详情**。 v. 在**服务列表**中单击**asrdr-backend**服务。 灾备管理中心操作 vi. 在**组件列表**中选择**backend#**组件。在**实例列表**中，单击某台机器**操作**列中的**Terminal**。
2. 以root账号执行如下命令查询容器的ID。

```bash
docker ps
```

3. 以root账号执行如下命令进入容器。

```bash
docker exec -it <容器ID> /bin/bash
```

### 登录ASR-DR元数据库

在飞天基础运维平台获取元数据库的登录信息后，通过OPS服务器登录ASR-DR元数据库。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在**产品列表**页面的**产品** | **集群**搜索框中输入asrdr，在目标集群**操作**列单击**集群详情**。
灾备管理中心操作
5. 选择**资源详情**页签，在资源名称输入框中输入**asrdr_v2**，确认**类型**为**db**后，在资源申请结果列单击
图标然后单击数据库信息，查看并记录数据库的登录信息。记录后关闭资源申请结果，单击隐藏数据库信息。
6. 登录OPS服务器。
7. 根据数据库连接信息登录ASR-DR元数据库。

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

灾备管理中心运维

## ASR-DR运维

### 日志管理

#### 查看ASR-DR日志

通过查看日志，您可以了解具体的错误信息。
1. 登录ASR-DR容器，具体步骤请参见登录容器。
2. 执行如下命令进入日志的文件夹路径。

```
cd /opt/tianji/log/
```

3. 执行 `ll` 命令查看日志文件列表。日志文件的用途如下表所示。

| 日志文件 | 描述 |
|---|---|
| api.log | ASR-DR调用云产品API的日志 |
| asrdr-audit.log | 审计日志 |
| complete.log | 整合的日志，包括所有日志信息 |
| framework.log | 后端框架日志 |
| gateway.log | 网关日志，即前端的请求日志 |
| machine-error.log | 状态机错误日志 |
| machine.log | 状态机日志 |
| service-error.log | 服务错误日志 |
| service.log | 服务日志 |

4. 根据ASR-DR控制台上实例日志的时间，选择对应日期的log文件，并查看日志。

**说明**

不带日期的文件即为当天的日志。 如果当前日志中没有查到错误信息，您可以切换到ASR-DR的其他容器查看操作日志，操作步骤类似。
5. （可选）您可以根据时间搜索具体的日志信息，命令格式如下。
灾备管理中心运维 `/<`时间>
6. （可选）执行以下内容，清理日志；如果日志占用太多容器空间，可以定时清理无用日志。
执行crontab -e，修改定时任务。

```
增加：0 1 * * * find /home/admin/logs/ -mtime +7 -type f -name "*.log*" -exec rm -f {}
```

\;表示每天1点清理，删除7天以上的日志。

#### 修改日志的默认配置

您可以在logback文件中配置日志的等级、日志的输出方式、保存时间、日志是否输出。

**操作步骤**

1. 登录ASR-DR容器，具体步骤请参见登录容器。
2. 备份 `/alidata/bin/start` 文件，以便有异常时进行回滚操作。

```
cp /alidata/bin/start /alidata/bin/start.bak
```

3. 在/alidata/bin目录下创建logback-spring.xml文件，用于配置日志信息。

```
cd /alidata/bin vi logback-spring.xml
```

4. 执行 `vi` 编辑 `/alidata/bin/start` 文件，按Insert进入编辑模式在java启动命令中增加 `--`

```
logging.config=<logback-spring.xml> 。类似如下：
```

灾备管理中心运维修改前：

```
java ${JAVA_OPTS} -jar /home/admin/asrdr/web-3.0.0.jar --server.port=8888 --spring.prof iles.active=prod &
```

修改后：

```
java ${JAVA_OPTS} -jar /home/admin/asrdr/web-3.0.0.jar --server.port=8888 --spring.prof iles.active=prod --logging.config=/logback-spring.xml &
```

**说明**

添加成功后按Esc退出编辑模式，输入：wq!保存并退出；<logback-spring.xml>为日志文件的路径。
5. 执行以下命令退出并重启ASR-DR容器。
# 如果在容器中，则退出`docker`

```
exit
```

# 重启`docker`，容器`ID`是进入容器时选择的`ID`

```bash
docker restart <容器ID>
```

6. 检查日志的输出是否符合预期。

**回滚方案**

1. 恢复 `/alidata/bin/start` 文件的配置。
# 恢复原备份的`start`文件

```
mv /alidata/bin/start.bak /alidata/bin/start
```

2. 重启ASR-DR容器。
# 如果在容器中，则退出`docker`

```
exit
```

# 重启`docker`，容器`ID`是进入容器时选择的`ID`

```bash
docker restart <容器ID>
```

### 停止ASR-DR节点

ASR-DR采用集群3节点部署，前端请求会通过SLB负载到任意节点。问题排查需要在3个ASR-DR查看，排查过程较麻烦。所以在排查问题时，建议关停2个ASR-DR节点，日志将在单点运行的ASR-DR容器中。

**风险**

请确保没有正在运维中的演练计划或故障计划，如果计划在运行中，执行该操作，可能导致发生节点切换， 增加RTO。 保护组将会运行到同一节点，如果保护组数量较大（超过200个时），单节点的负荷会较大。

**方案一：停止容器**

**说明**

关停容器会导致飞天基础运维平台检查ASR-DR不到终态。
1. 登录容灾所在的宿主机。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 灾备管理中心运维 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品列表**页面的**产品** | **集群**搜索框中输入asrdr，在目标集群**操作**列单击**集群详情**。 v. 在**服务列表**中单击**asrdr-backend**服务。 vi. 在**组件列表**中选择**backend#**组件。在**实例列表**中，单击某台机器**操作**列中的**Terminal**。
2. 以root账号执行如下命令进入目录。

```
cd /cloud/app/asrdr-portal/portal#
```

3. 以root账号执行如下命令，停止asrdr-backend容器。

```
/cloud/tool/tianji/tjc stop asrdr-backend.backend#
```

**方案二：停止进程**

1. 登录ASR-DR容器，具体请参见登录容器。
2. 备份 `/alidata/bin/check_app.sh` 文件，以便后期执行回滚操作。
灾备管理中心运维

```
cp /alidata/bin/check_app.sh /alidata/bin/check_appbak.sh
```

3. 执行以下命令，修改 `/alidata/bin/check_app.sh` 文件，将 exit $? 修改为 `exit 0` 。

```
vi /alidata/bin/check_app.sh
```

4. 执行如下命令获取ASR-DR进程的PID，并结束ASR-DR进程。

```
ps aux | grep <asrdr进程> kill -9 <pid>
```

5. 如果是V3.13.0之前的版本，您还需要执行如下命令结束nginx进程。

```
ps aux | grep <nginx进程> kill -9 <pid>
```

**回滚方案**

**方案一的回滚**

1. 登录容灾所在的宿主机。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品列表**页面的**产品** | **集群**搜索框中输入asrdr，在目标集群**操作**列单击**集群详情**。 v. 在**服务列表**中单击**asrdr-backend**服务。 灾备管理中心运维 vi. 在**组件列表**中选择**backend#**组件。在**实例列表**中，单击某台机器**操作**列中的**Terminal**。
2. 以root账号执行如下命令进入目录。

```
cd /cloud/app/asrdr-portal/portal#
```

3. 以root账号执行如下命令，重启asrdr-backend容器。

```
/cloud/tool/tianji/tjc start asrdr-backend.backend#
```

**方案二的回滚**

1. 用备份的 `/alidata/bin/check_app.sh` 文件，替换当前的 `check_app.sh` 文件。
2. 重启asrdr-backend容器。
# 如果在容器中，则退出`docker`

```
exit
```

# 重启`docker`，容器`ID`是进入容器时选择的`ID`

```bash
docker restart <容器ID>
```

### 更换JAR包

客户现场发现的问题，研发工程师修复代码后，可以用新的JAR包替换现场的JAR包，来修复现场的问题。

**背景信息**

通过JAR重新打包会使JAR包增大，对功能没有影响。 通过JAR打包后，Springboot启动时会出现log4j和logback依赖冲突。您可以在 `BOOT-INF/lib/` 目录下删除 `slf4j-log4j12` 这个JAR包，重新压缩来解决该问题。

**操作步骤**

1. 登录ASR-DR容器，具体请参见登录容器。
2. 执行如下命令备份 `/home/admin/asrdr/web-3.0.0.jar` 文件。

```
mv /home/admin/asrdr/web-3.0.0.jar /home/admin/web-3.0.0.jar.bak
```

3. 将新的 `web-3.0.0.jar` 文件拷贝到 `/home/admin/asrdr` 路径下。
灾备管理中心运维
4. 重启ASR-DR容器。
# 退出`docker`（如果在容器中）

```
exit
```

# 重启`docker`，容器`ID`是进入容器时选择的`ID`

```bash
docker restart <容器ID>
```

**回滚方案**

1. 登录ASR-DR容器，具体请参见登录容器。
2. 删除 `/home/admin/asrdr` 路径下的 `web-3.0.0.jar` 。

```
rm -rf ./web-3.0.0.jar
```

3. 用之前备份的 `web-3.0.0.jar.bak` 文件替换 `web-3.0.0.jar` 文件。
4. 重启ASR-DR容器。
# 退出`docker`（如果在容器中）

```
exit
```

# 重启`docker`，容器`ID`是进入容器时选择的`ID`

```bash
docker restart <容器ID>
```

灾备管理中心处理

## 常见运维处理

### RDS

#### RDS新增数据库和数据表

本文介绍如何对容灾保护中的RDS实例进行新增数据库和数据表，避免保护失败。

**背景信息**

容灾演练切换后，RDS的同步链路变成增量链路。DTS的增量同步链路不支持同步数据库结构。因此，在执行新增数据库和数据表时，需人工对ASR-DR及DTS的相关数据进行修改。

**场景一：源端新增数据库，且该数据库需要容灾保护**

1. 手动在备端新增数据库，并创建表结构。对同步账号授予读写权限。

**说明**

MySQL 5.7版本的同步账号为asr_sync_account。 MySQL 5.6版本的同步账号为dtssyncwriter。
2. 手动在主端创建数据库，并创建表结构。对同步账号授予读写权限。
ASR-DR检查到源端或备端新增了库，保护状态会从**保护中**变为**保护失败**。
3. 在ASR-DR控制台的保护组列表中，单击目标保护组右侧的
图标，选择**重保护**。 对应实体会进入重保护状态，并自动将该数据库加入同步对象中，等待进入保护中状态。由于DTS会启动新的任务去同步新增的数据库，直到子任务同步完成并合入原有主任务，此过程大概需要20分钟，因此需要观察DTS链路是否成功合入。

**场景二：源端新增数据库，且该数据库不需要容灾保护**

该场景不需修改同步对象，但需要修改ASR-DR数据库中的整库过滤标记。主备两端均需要给同步账号授予新增数据库的读写权限。
1. 手动在备端新增数据库，并创建表结构。对同步账号授予读写权限。

**说明**

MySQL 5.7版本的同步账号为asr_sync_account。 MySQL 5.6版本的同步账号为dtssyncwriter。
2. 手动在主端创建数据库，并创建表结构。对同步账号授予读写权限。
3. 在ASR-DR控制台设置过滤表，具体操作请参见异地容灾管理平台ASR-DR用户指南中的**业务容灾**> **修改过**
**滤表**章节。
灾备管理中心处理

|  | 说明 V3.15.0~3.18.6 2505的版本支持在ASR-DR控制台设置过滤表，3.18.6 2507及后续版本已删除过 _ _ 滤表功能。 V3.15.0之前的版本请通过如下方法修改： i. 登录ASR-DR数据库，具体请参见登录ASR-DR元数据库。 ii. 修改t am rdsSyncEntity的rwAccounts字段。在rwAccounts字段添加 ,新增的数据库.- _ _ .* 。 rwAccounts字段是按数据库.账号.* 的格式构造，*表示该数据库整库被过滤。账号字段目前全部为短划线（-）。多个数据库之间用英文半角逗号（,）隔开。 iii. 检查是否已成功修改，如果没有修改成功，请关闭ASR-DR服务后再修改。 iv. 重启ASR-DR服务。 |
|---|---|

**场景三：源端新增数据库，且需要容灾保护部分表**

1. 手动在备端新增数据库，并创建表结构。对同步账号授予读写权限。

**说明**

MySQL 5.7版本的同步账号为asr_sync_account。 MySQL 5.6版本的同步账号为dtssyncwriter。
2. 手动在主端创建数据库，并创建表结构。对同步账号授予读写权限。
3. 在ASR-DR控制台设置过滤表，具体操作请参见异地容灾管理平台ASR-DR用户指南中的**业务容灾**> **修改过**
**滤表**章节。

**说明**

V3.15.0~3.18.6_2505的版本支持在ASR-DR控制台设置过滤表，3.18.6_2507及后续版本已删除过滤表功能。

**场景四：保护中的数据库新增表，且该表不需要容灾保护**

1. 手动在主端创建表。
2. 停止ASR-DR节点，具体请参见停止ASR-DR节点。

**说明**

新增表之后，ASR-DR会定时将新增表加入同步对象中，DTS会将新增表加入同步对象进行同步。因此
3. 在ASR-DR控制台设置过滤表，具体操作请参见异地容灾管理平台ASR-DR用户指南中的**业务容灾**> **修改过**
**滤表**章节。

**说明**

V3.15.0~3.18.6_2505的版本支持在ASR-DR控制台设置过滤表，3.18.6_2507及后续版本已删除过滤表功能。

**场景五：保护中的数据库新增表，且该表需要容灾保护**

灾备管理中心处理在主端新增表之后，您需要在备端创建表结构。

**说明**

新增表之后，ASR-DR会定时将新增表加入同步对象中，DTS会将新增表加入同步对象进行同步。因此该场景下您不需要修改ASR-DR的配置。

#### 人工切换主备RDS实例

当生产站点的RDS故障，且ASR-DR故障时，您可以手工将业务切换至灾备站点的RDS。

**背景信息**

切换是指生产站点的RDS故障时，将业务切换至灾备站点的RDS。 回切是指执行切换后，当灾备站点的RDS故障，将业务从灾备站点的RDS回切至生产站点的RDS。 本文以人工切换的操作为例。 人工回切的操作步骤类似，您需要在生产站点的RDS实例执行如下操作。

**操作步骤**

1. 将灾备站点的RDS实例的账号权限改为**读写**。
i. 登录灾备站点的Apsara Uni-manager运营控制台。 ii. 在顶部菜单栏中选择**产品** > **数据库** > **云数据库** **RDS** 版。 iii. 在左侧导航栏中选择**实例列表**，在RDS实例列表中单击目标实例的**实例****ID/****名称**。 iv. 在左侧导航栏单击**账号管理**。 v. 选择业务使用的账号，在**操作**列中单击**修改权限**。 vi. 在**已授权数据库**区域，为账号授权数据库的**读写（****DDL+DML**）权限。 vii. 单击**确定**。
2. 检查灾备站点的RDS实例是否可以正常写入数据。

#### 人工恢复同步链路

当生产站点和灾备站点的RDS实例恢复正常，但是ASR-DR故障，无法短时间恢复的情况下，您可以人工恢复同步链路。
1. 将灾备RDS实例的账号权限改为**只读**。
i. 登录灾备站点的Apsara Uni-manager运营控制台。 ii. 在顶部菜单栏选择**产品** > **数据库** > **云数据库** **RDS** 版。 iii. 在左侧导航栏中单击**实例列表**，在RDS实例列表中单击目标实例的**实例****ID/****名称**。 iv. 在左侧导航栏单击**账号管理**。 v. 选择业务使用的账号，在**操作**列中单击**重置账号权限**。 vi. 在弹出的页面中输入数据库账号的密码，单击**确定**。 vii. 在**已授权数据库**区域，为账号授权数据库的**只读**权限。 viii. 单击**确定**。
2. 将主RDS实例的账号权限改为**读写（****DDL+DML**）。具体操作步骤参考上一步。
3. 登录灾备站点的DTS控制台，配置主RDS到备RDS的数据同步任务。具体操作步骤请参见DTS用户指南中
的**数据同步**>**数据同步配置案例**>**RDS MySQL****实例间的数据同步**章节。 灾备管理中心处理
4. 人工检查同步链路是否正常、数据同步是否正常。

### DNS

#### 实例日志提示rrSet inconsistent

本文介绍当DNS实例日志提示rrSet inconsistent时的原因和处理方法。

**问题现象**

在保护组列表中查看**保护组状态**为**保护失败**。在保护组详情中查看实例日志，日志内容为**rrSet**
**inconsistent**。

**可能原因**

生产站点DNS的域名解析记录和灾备站点DNS的域名解析记录不一致。

**解决方案**

1. 登录生产站点的DNS控制台，查看DNS域名的**记录集合**。
i. 选择对应的域名，单击**操作**列中**解析配置**。 ii. 在**解析设置**页面，单击**操作**列中**修改**。 iii. 查看并保存**记录值集合**的值。
2. 登录灾备站点的DNS控制台，将DNS域名的**记录值集合**修改为与生产站点一致，操作方法请参见上一步。
3. 登录灾备站点的ASR-DR，在**保护组详情**页面，单击实体列表中目标实例
图标，单击**重试**。 保护组重新进入**保护中**。

#### 实例日志提示not found record

**问题现象**

在保护组列表中查看**保护组状态**为**保护失败**。在保护组详情中查看DNS实例日志，日志内容为**not found**
**record, zoneId: xxx, rrName: xxx, cloudType: xxx**。

**可能原因**

生产站点或灾备站点DNS域名的主机记录未配置。 cloudType：表示生产站点或灾备站点。MAIN表示生产站点，BACKUP表示灾备站点。 zoneId：表示对应的DNS实例的ID。 rrName：表示主机记录的名称。

**解决方案**

1. 根据**cloudType**提示，登录生产站点或灾备站点的DNS控制台。
2. 选择对应的域名，单击**操作**列**解析配置**。
3. 在**解析设置**页面，单击右上角的**添加解析记录**，添加主机记录。
灾备管理中心处理

**说明**

主机记录中的**记录值集合**要和对端DNS的**记录值集合**保持一致。
4. 登录灾备站点的ASR-DR，在**保护组详情**页面，单击实体列表中目标实例
图标，单击**重试**。 保护组重新进入**保护中**。

#### 实例日志提示not found zone

**问题现象**

在保护组列表中查看**保护组状态**为**保护失败**。在保护组详情中查看DNS实例日志，日志内容为**not found**
**zone xxx cloudType: xxx**。

**可能原因**

在生产站点或灾备站点无法查询到对应的DNS域名实例。 cloudType：表示生产站点或灾备站点。MAIN表示生产站点，BACKUP表示灾备站点。 zone：表示对应的DNS实例名称。

**解决方案**

1. 根据**cloudType**提示，登录生产站点或灾备站点的DNS控制台。
2. 创建和对端一致的DNS域名实例。
3. 添加和对端一致的主机记录和解析记录。
4. 登录灾备站点的ASR-DR，在**保护组详情**页面，单击实体列表中目标实例
图标，单击**重试**。 保护组重新进入**保护中**。

### 云原生数据仓库AnalyticDB MySQL

**版3.0**

#### 重保护失败

本文介绍云原生数据仓库AnalyticDB MySQL版3.0（简称ADB3.0）实例执行重保护后，保护失败的处理方法。

**问题现象**

暂停同步链路后，执行**重保护**操作，保护组的状态为保护失败。

**问题原因**

重启同步链路的过程中，源端的ADB3.0实例会基于历史位点（上一次切换的位点）来判断主备实例的同步位点信息，导致链路失败。 灾备管理中心处理

**处理方案**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 在左侧导航栏中选择**实例管理**>**实例列表**。
4. 根据主端ADB3.0的集群ID搜索到对应的实例，单击**实例简述**列为**专享****/analyticdb/****主实例****/P4**的实例名
称。
5. 在**实例详情**页面的右上角单**切换到旧版**，在**实例信息**区域，查看并记录实例ID，单击**打开****console**。
6. 参考上述步骤，查看备端ADB3.0的实例ID，即repliId。
7. 在主端AnalyticDB Console控制台的左侧导航栏，单击**SQL Editor**，执行如下命令。提示 `gap`
`exist` 的错误。

```
replication master start <备实例的repliId>
```

8. 连接meta库执行如下命令。

```
delete from replication_switch_info;
```

9. 在ASR-DR控制台，对目标实例执行**重试**操作。
i. 在保护组列表中，单击目标保护组名称。 ii. 在**保护组详情**页面，单击实例列表中目标实例右侧的图标，单击**重试**。

#### 重新创建同步实体失败

灾备管理中心处理本文介绍重新创建云原生数据仓库AnalyticDB MySQL版3.0（简称ADB3.0）同步实体后，保护失败的处理方法。

**问题现象**

在ASR-DR上删除保护组中的ADB3.0实例，重新添加实体，保护组的状态为保护失败。

**问题原因**

删除同步实体时，历史任务没有清理干净。

**处理方案**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 在左侧导航栏中选择**实例管理**>**实例列表**。
4. 根据主端ADB3.0的集群ID搜索到对应的实例，单击**实例简述**列为**专享****/analyticdb/****主实例****/P4**的实例名
称。
5. 在**实例详情**页面的右上角单**切换到旧版**，在**实例信息**区域，查看并记录实例ID，单击**打开****console**。
6. 参考上述步骤，查看备端ADB3.0的实例ID，即repliId。
7. 在主端AnalyticDB Console控制台的左侧导航栏，单击**SQL Editor**，执行如下命令。提示 `gap`
`exist` 的错误。

```
select * from ation_schema.kepler_meta_cluster_replication_task where is_masteinformr = 1 and slave_cluster_name=<备实例的repliId>
```

若存在记录，则说明历史任务没有清理干净。
8. 执行如下命令清理历史任务。

```
replication master destroy slave <备实例的repliId>
```

9. 在ASR-DR控制台，对目标实例执行**重试**操作。
i. 在保护组列表中，单击目标保护组名称。 ii. 在**保护组详情**页面，单击实例列表中目标实例右侧的图标，单击**重试**。

#### 创建增量同步实体前置检查

本文介绍创建云原生数据仓库AnalyticDB MySQL版3.0（简称ADB 3.0）增量同步实体的前置检查操作。其中增量同步的前提是主备实例已成功执行全量同步，所以需要检查是否全量同步。

**处理方案**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 登录主端AnalyticDB Console。
灾备管理中心处理 i. 在左侧导航栏中，选择**实例管理**>**实例列表**。 ii. 根据主端ADB 3.0的集群ID搜索对应的实例，单击**实例简述**列为**专享****/analyticdb/****主实例****/P4**的用户实例名称。 iii. 在**实例详情**页面的右上角单**切换到旧版**，在**实例信息**区域，查看并记录实例ID，单击**打开****console**。
4. 查看备端ADB 3.0的实例ID，即repliId，并登录备端AnalyticDB Console，具体操作请参见上述步骤。
5. 查看主备端实例Cluster Name和Status。
i. 在主备端AnalyticDB Console左侧导航栏中，单击**SQL Editor**。 ii. 在**执行方式**下拉框中选择**META**。 iii. 在**数据库**区域，单击以**db**开头的数据库名。 iv. 执行如下命令，并记录主备端实例的 `MASTER_CLUSTER_NAME` 、 `SLAVE_CLUSTER_NAME` 和 `STATUS` 字段对应的值。

```
select * from cluster_replication_task;
```

主备端实例中存在记录 `MASTER_CLUSTER_NAME` 和 `SLAVE_CLUSTER_NAME` 字段的值分别和主备端实例的repliId保持一致，或者分别和备主端实例的repliId保持一致， `STATUS` 字段的值为**FINISH**，否则不能创建增量链路。

### PolarDB-X

#### 备实例删除数据库后未生效

**问题现象**

**问题原因**

**处理方案**

1. 登录云原生分布式数据库控制台。
2. 在实例列表查询到目标备实例。
3. 单击目标备实例ID，打开**基本信息**页面。
4. 单击页面右上角的**重启实例**。
5. 在**重启实例**对话框中单击**确定**。

**说明**

重启实例会造成连接中断，重启前请做好业务安排，谨慎操作。 灾备管理中心处理

#### 获取逻辑表的结构时提示表不存在

**问题现象**

**问题原因**

**处理方案**

1. 登录云原生分布式数据库控制台。
2. 在实例列表中定位到目标实例。
3. 单击目标实例ID打开**基本信息**页面。
4. 在左侧导航栏中单击**数据库连接**。
5. 单击右上角**登录数据库**。
6. 在目标PolarDB-X实例的数据库中，执行如下命令删除该逻辑表。

```
drop table if exists <table_name>;
```

**说明**

<table_name>请根据实际情况替换为具体的表占位符。
7. 重新创建该逻辑表。

```
CREATE TABLE <table_name> (
```

`//` 字段为原表结构内容

```
);
```

#### 修改PolarDB-X中RDS数据库的最大个数

PolarDB-X默认最多能创建30个RDS数据库，您可以在配置文件中修改CreateDrdsDB的值，调整最大个数。
1. 登录PolarDB-X的 `drds-console.DrdsConsole#` 服务角色所在的容器，具体操作步骤请参见登录容器。
2. 执行如下命令进入CreateDrdsDB文件所在目录。
`cd /home/admin/pop/apis #`临时文件路径

```bash
# or
```

`cd /home/admin/etc/batch/apis/ #`永久文件路径

```
ls | grep CreateDrdsDB vim 2017-10-16-CreateDrdsDB.xml
```

灾备管理中心处理
3. 执行 `vim` 命令，编辑 `CreateDrdsDB.xml` 文件，修改**CreateDrdsDB**的**maxNumber**的值。
4. 进入 `/home/admin/pop` ，执行如下命令使修改生效。

```
java -jar batch.jar
```

#### 创建PolarDB-X同步链路失败

**问题现象**

ASR-DR创建PolarDB-X同步链路失败，日志中提示DescribeDrdsShardingDbs接口超时。

**处理方案**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单中选择**产品运维** > **数据库运维** **> DRDS****运维****·DRDS****管家**。
灾备管理中心处理
3. 在左侧导航栏中选择**系统管理**>**参数配置**。
4. 单击**Console**页签。
5. 在搜索框中输入support_use_rtools_diamond，单击**support_use_rtools_diamond**右侧**操作**列中
的**修改**。

**说明**

如果无法搜索到该KEY，请单击**创建**，**FIRST_KEY**设置为 support_use_rtools_diamond，**VALUE**设置为false。
6. 将**VALUE**的值修改为false。单击**OK**。

#### 扩容PolarDB-X实例

灾备管理中心处理登录ASR-DR，确保ASR-DR没有在执行演练切换、演练回切、故障切换或故障回切。
1. 登录云原生分布式数据库控制台。
2. 在实例列表中定位到目标实例。
3. 单击目标实例ID，打开**基本信息**页面。
4. 在左侧导航栏中单击**配置与管理** > **数据库管理**。
5. 单击目标数据库右侧**管理**，打开数据库**基本信息**页面。
6. 在左侧导航栏中单击**配置与管理** > **扩容管理**。
7. 在**扩容管理**页面右上角，单击**扩容**。
8. 选择**平滑扩容**，单击**下一步**。
9. 等待**预检**通过后，单击**下一步**。

**说明**

如果预检失败，请根据页面提示进行修复。
0. 在**选择****RDS**页面，您可以选择**购买新****RDS**，或者**使用已有****RDS**。

**说明**

**购买新****RDS**：
i. 单击**购买新****RDS**标签页。 ii. 选择**存储类型**、**系列**、**规格**、**存储空间**、**可用区**以及**数量**。 iii. 单击**下一步**。
**使用已有****RDS**：
i. 单击**使用已有****RDS**标签页。 ii. 在左侧框中单击想要添加的RDS实例。 iii. 单击将选中的实例移动到右侧**已选择****RDS**中。 iv. 单击**下一步**。
1. 在**结果预览**页面，单击**开始扩容**。

**说明**

控制台默认会平均分配相应的物理分库至新添加的RDS实例上。您也可以手动在新增的RDS实例上添加或删除物理分库。
2. 单击页面右上角
图标，查看扩容任务进度。

**说明**

分别登录主备PolarDB-X控制台。请在主备两端同名的数据库先后执行平滑扩容操作。不要求顺序，但灾备管理中心处理
3. 在ASR-DR控制台，找到主备实例所在的保护组，记下当前的同步延迟时间，并删除该保护组里对应的保护
实例（如果保护组里只有一个保护实例，则删除保护组），记下该删除时间点T1。
4. 在PolarDB-X控制台，选择一个流量低峰时点，分别对主备PolarDB-X实例执行扩容切换操作。
等待两端切换完成，如下图所示。
5. 在ASR-DR控制台，新建或选择已有的一个增量保护组，将扩容的PolarDB-X添加其中，同步位点使用步骤
3里记录的删除时间点T1减去步骤3记录的同步延迟时间。静待PolarDB-X保护实体进入保护中的状态。
6. 确认主备PolarDB-X的数据一致后，分别在主备PolarDB-X控制台，单击**清理**。

### DTS

#### 查看DTS日志

在定位数据库产品容灾问题时，您需要查看DTS的Master日志、Portal日志或Node节点的日志。

**查看Master日志**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏中，选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务管理**。
4. 在**服务管理**页面的**服务**下拉框，搜索并筛选**dts-dts**。
5. 在**服务管理**页面中，单击**服务实例**页签。
6. 单击DTS集群**操作**列的**实例详情**。
7. 在组件列表选择**DtsMaster#**组件。
8. 单击操作列**Terminal**进入终端。
9. 以root账号执行如下命令查询容器的ID。

```bash
docker ps
```

灾备管理中心处理
0. 以root账号执行如下命令进入容器。

```bash
docker exec -it <容器ID> /bin/bash
```

1. 在 `/dts/master/logs/master.log` 目录下，查看日志。
# 使用搜索，即可定位到大部分常见错误

```
grep --color=auto -n -e 'keyword' /dts/master/logs/master.log
```

**查看Portal日志**

1. 参考上述步骤登录 `dts-dts.DtsPortal#` 服务角色所在的容器。
2. 在 `/dts/portal/logs/portal.log` 目录下，查看日志。

**查看DTS Node节点的日志**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单中选择**产品运维** > **数据库运维** **> DTS****运维****·DTS**。
3. 查找Node节点的IP地址。
i. 在**任务列表**中，单击类型为**同步**的目标任务名。 ii. 在**任务详情**页面，单击**同步**区域的**详情**。 iii. 查看并记录Node节点的IP地址。
4. 通过OPS服务器或飞天基础运维平台的Terminal登录DTSNode#组件。
`ssh <DTS Node`节点的`IP>`
5. 在 `/cloud/app/dts-dts/DtsNode#/dts_node/current/run/<taskId>` 目录下查看log和config文件。

```
cd /cloud/app/dts-dts/DtsNode#/dts_node/current/run/<taskId>
```

灾备管理中心处理

#### 同步链路创建失败

##### 日志提示cluster info is null.The input domain

**and region is invalid**

本文介绍DTS日志提示cluster info is null.The input domain and region is invalid的处理方案。

**问题现象**

ASR-DR创建数据库产品的同步链路失败，查看DTS的Portal日志，提示类似如下信息。

```
[{"success":false,"msg":"cluster info is null.The input domain and region is invalid.","c ode":404,"data":null}]
```

**问题原因**

DTS跨云同步配置错误。

**处理方案**

1. 登录rmdb数据库。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 灾备管理中心处理 iv. 在**产品列表**中搜索dts，在目标集群**操作**列单击**集群详情**。 v. 选择**资源详情**页签，找到**名称**为**rmdb**、**类型**为**db**的资源，在**资源申请结果**列单击图标，查看并记录数据库的登录信息。 vi. 登录OPS服务器，具体步骤请参见专有云如何登录OPS服务器。 vii. 根据数据库连接信息登录rmdb数据库。

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. 检查数据表中region和region_pattern的配置是否正确。例如Region的写法是否有问题（下划线和横线的
区别），是否缺少记录。正确的配置类似如下图。 具体的配置方法请参见《阿里云专有云企业版部署指南》中的**异地容灾部署** > **容灾配置** > **产品容灾配置** >

```
select * from region_pattern;
```

灾备管理中心处理

##### 日志提示Specified access key is not found

本文介绍DTS日志提示Specified access key is not found的处理方案。

**问题现象**

ASR-DR创建数据库产品的同步链路失败，查看DTS的Portal日志，搜索接口请求的Request ID，或者搜索**dts console**，提示 `Specified access key is not found` 。

**问题原因**

如果是跨云容灾场景，可能原因是dts-portal配置的对端AccessKey不正确。 如果是跨Region容灾场景，可能原因是中心Region的UMMAK向单元Region同步时出现问题。重建 UMMAK的同步链路即可。

**处理方案-跨云容灾场景**

1. 登录生产站点DtsPortal#服务角色所在的容器，具体操作请参见登录容器。
2. 检查 `/dts/portal/application.properties` 文件中配置的灾备站点的AccessKey是否正确。如果不正
确，请修改为正确的AccessKey。

**处理方案-跨Region容灾场景**

1. 在单元Region，登录baseService-umm-ak服务对应的UMMAK数据库。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品列表**中搜索baseServiceAll，在目标集群**操作**列单击**集群详情**。 v. 选择**资源详情**页签，找到**名称**为**ummak**、**类型**为**db**的资源，在**资源申请结果**列单击图标，查看并记录数据库的登录信息。 vi. 登录OPS服务器。 vii. 根据数据库连接信息登录ummak数据库。

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. 执行如下命令清除所有表。

```
truncate table ***
```

3. 在单元Region的飞天基础运维平台，重启**baseService-umm-ak.UmmInit#**服务角色，将会重新生
成umm-ak DTS任务。 i. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 灾备管理中心处理 ii. 在**产品列表**中搜索baseServiceAll，在目标集群**操作**列单击**集群详情**。 iii. 在服务列表中单击**baseService-umm-ak**服务。 iv. 选择**UmmInit#**组件，在对应机器的**操作**列中，单击**操作** > **重启**。

##### 日志提示InvalidAppId.NotFound

**问题现象**

ASR-DR创建数据库产品的同步链路失败，查看DTS的Portal日志，提示 `InvalidAppId.NotFound` 。

**问题原因**

App没有在灾备站点的VPC数据库注册成功。

**处理方案**

1. 在ASR-DR的元数据库的**t_base_vpc_entity**表中查询app_id的值。登录ASR-DR元数据库的步骤请参
2. 登录vpc-controller的数据库。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 灾备管理中心处理 iv. 在**产品列表**中搜索vpc，在目标集群**操作**列单击**集群详情**。 v. 选择**资源详情**页签，找到**名称**为**vpcregiondb**、**类型**为**db**的资源，在**资源申请结果**列单击图标，查看并记录数据库的登录信息。 vi. 登录OPS服务器。 vii. 根据数据库连接信息登录vpc-controller数据库。

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

3. 执行如下命令查看app、app_address_pool、app_server、app_access数据表中是否有ASR-DR配置的
数据。 如果在vpc-controller数据库中没有查到上述SQL的相关信息，表明VPC的注册信息过期或者没有注册成功。请继续执行步骤4。

```bash
select * from app where app_id='app-9nh4****h1qursq' and is_deleted=0\G;
# available_count最好为0
select * from app_address_pool where app_id='app-9nh4n****1qursq' and is_deleted=0\G;
```

# 根据`asrdr`的`docker`数量确定，如果`asrdr`服务的`docker`数量为3，则有3条记录

```
select * from app_server where app_id='app-9nh4n****h1qursq' and is_deleted=0\G;
```

# 其中`mapping ip/port`，是在经典网络中去访问`vpc`的地址

```
select * from app_access where app_id='app-9nh4n****h1qursq' and is_deleted=0\G;
```

**说明**

app_id的值请替换为步骤1中获取的app_id。
4. 登录DTS的**dtsdb**数据库。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 灾备管理中心处理 iv. 在**产品列表**中搜索dts，在目标集群**操作**列单击**集群详情**。 v. 选择**资源详情**页签，找到**名称**为**dtsdb**、**类型**为**db**的资源，在**资源申请结果**列单击图标，查看并记录数据库的登录信息。 vi. 登录OPS服务器。 vii. 根据数据库连接信息登录dtsdb数据库。

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

5. 在dts_mapping_app、dts_mapping_server和dts_mapping_pool数据表中删除旧的VPC注册信息。
6. 重启DTS的portal、master、node、cm和DrcSv4mysql服务。

##### 日志提示ram authorized

**问题现象**

ASR-DR创建数据库产品的同步任务失败，查看DTS的Portal日志，提示 `ram authorized` 。

**问题原因**

Apsara Uni-manager运营控制台上，对应的组织没有创建数据传输服务（DTS）的RAM服务角色。

**处理方案**

1. 登录Apsara Uni-manager运营控制台，选择**配置** > **RAM****服务角色**。
2. 在服务名称搜索数据传输服务，查看对应的组织是否已创建该RAM服务角色。
如果不存在相应的RAM服务角色，请给对应的组织创建**数据传输** **DTS**服务的RAM服务角色。具体操作步骤请参见异地容灾管理平台ASR-DR用户指南。 如果存在相应的RAM服务角色，请联系运维工程师进行处理。

##### 日志提示open_api_objects长度不足

本文介绍DTS日志提示Data truncation: Data too long for column 'open_api_objects'的处理方案。

**问题现象**

ASR-DR创建数据库产品的同步链路失败，查看DTS的Portal日志，提示 `Data truncation: Data too`

```
long for column 'open_api_objects' 。
```

**问题原因**

同步的对象太大。

**处理方案**

灾备管理中心处理
1. 登录DTS的dtsdb数据库。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品列表**中搜索dts，在目标集群**操作**列单击**集群详情**。 v. 选择**资源详情**页签，找到**名称**为**dtsdb**、**类型**为**db**的资源，在**资源申请结果**列单击图标，查看并记录数据库的登录信息。 vi. 登录OPS服务器。 vii. 根据数据库连接信息登录dtsdb数据库。

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. 执行如下命令修改open_api_objects的值。

```
ALTER TABLE migration_job_param MODIFY open_api_objects MEDIUMTEXT ; ALTER TABLE migration_job MODIFY RESERVED MEDIUMTEXT ;
```

#### 预检查异常

##### 提示拓扑结构不一致

**问题现象**

**问题解决**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单中选择**产品运维** > **数据库运维** **> DTS****运维****·DTS**。
3. 在任务列表中，单击类型为**同步**的目标任务名。
4. 在**任务详情**页面，单击**预检查**区域的**详情**。
灾备管理中心处理
5. 在**预检查**页面，单击**检查项**页签，屏蔽拓扑结构的检查项。
6. 单击**基本信息**页签，单击**重启**。

##### 提示CHECK_ERROR_SRC_USER_PSW

本文介绍DTS预检查失败，提示CHECK_ERROR_SRC_USER_PSW的处理方案。

**问题现象**

**处理方案**

1. 在Node所在的节点日志中查看error.log信息，具体操作步骤请参见查看DTS Node节点的日志。
2. 将 `/cloud/app/dts-dts/DtsNode#/dts_node/current/jar` 目录下的 `console.jar` 拷贝到task所在
目录，执行如下命令获取destUsr和destPsw。

```
cp /cloud/app/dts-dts/DtsNode#/dts_node/current/jar/console.jar /cloud/app/dts-dts/DtsN ode#/dts_node/current/run/<taskId>/ cd /cloud/app/dts-dts/DtsNode#/dts_node/current/run/<taskId> java -jar console.jar -e -print
```

灾备管理中心处理
3. 根据上一步中获取的destDbInst、destUsr和destPsw信息，执行 `telnet <destDbInst>` 命令查看网络
是否能正常连接。 如果网络无法正常连接，请执行如下步骤。
4. 重启DTS的Portal、Master、Node、Cm和DrcSv4mysql服务。

##### 提示CHECK_ERROR_DEST_USER_PSW

本文介绍DTS预检查时，目的端连通性检查失败，提示CHECK_ERROR_DEST_USER_PSW的处理方案。

**问题现象**

DTS预检查时，目的端连通性检查失败，提示 `CHECK_ERROR_DEST_USER_PSW` 。

**问题原因**

数据库实例的账号、密码错误。 数据库实例的白名单中没有添加DTS的IP地址。 DTS在创建同步任务时，默认会自动把自己的IP地址增加到数据库实例的白名单中。但如果源端数据库的白名单中已存在该IP地址，而目标端数据库的白名单中没有该IP地址。DTS不会在目标端数据库的白名单中再增加该IP地址。所以需要确保源端和目标端数据库的白名单中，都添加DTS的IP地址。

**处理方案**

手动在源端和目标端数据库的白名单中，添加DTS的IP地址。设置白名单的方法请参见云数据库RDS 用户指南中的**设置白名单**章节。

#### 增量数据服务异常

灾备管理中心处理

##### 增量数据服务卡在95%

**问题现象**

1. DTS运维控制台的任务详情中，预检查显示完成，但是增量数据服务一直在95%，但未提示失败。
2. 单击**增量数据服务**区域的**详情**，**DReader**和**DStore**的页面没有内容。

**问题原因**

DReader和DStore服务没有启动。

**处理方案**

1. 重启Portal、Master、Node、Cm和DrcSv4mysql服务角色。
2. 如果重启服务后问题依然没有解决，请查看DTS的Master日志。具体步骤请参见查看Master日志。
3. 如果日志中提示Node信息为空，类似如下图。则在所有Node的物理机上执行以下命令，重启进程。
灾备管理中心处理

```
ps -ef |grep 'service_manager_monitor|node.jar'|grep -v grep|awk '{print $2}'|xargs kil l -9
```

##### 增量数据服务失败

**问题现象**

1. DTS运维控制台的任务详情中，预检查显示完成，增量数据服务显示失败。
2. 单击**增量数据服务**区域的**详情**，**DReader**和**DStore**的页面有信息。

**处理方案**

1. 查看DTS的Master日志，在日志中查看topic_group是否被删除。具体操作步骤请参见查看Master日志。
2. 如果日志中发现topic_group被删除。请在DTS运维控制台重启增量数据服务。
i. 在DTS运维控制台，单击目标任务名称。 ii. 在任务详情页面的**增量数据服务**区域，单击**详情**。 灾备管理中心处理 iii. 在增量数据服务页面单击**重启（重建）**。

##### 提示format dblist error

本文介绍DTS运维控制台上，增量数据服务的错误信息提示format dblist error的处理方案。

**问题现象**

DTS运维控制台上，增量数据服务的错误信息提示 `format dblist error` 。类似如下图所示。

**问题原因**

存在空的同步对象。

**处理方案**

请检查同步对象的格式是否正确，去掉空的对象。

#### 同步数据异常

##### 提示store delay xxx second(s)

本文介绍DTS任务的同步步骤中，状态显示store delay xxx second(s)的处理方案。 灾备管理中心处理

**问题现象**

DTS任务的**同步**步骤中，状态显示 `store delay xxx second(s)` 。

**问题原因**

源端数据库没有写入数据。

##### 提示reader连不上dstore

**问题现象**

**问题原因**

源数据库修改了密码，但DTS同步任务的Topic中，配置的源数据库密码不会自动更新，导致同步失败。

**处理方案**

1. 登录DTS控制台。
2. 单击目标任务名称进入任务管理页面。
3. 在源端区域单击**修改密码**。
4. 根据界面提示输入密码至少3位，单击**确定**。

#### 恢复网络后，DTS任务没有自动恢复

本文介绍网络恢复后，DTS任务没有自动恢复的处理方案。

**问题现象**

网络中断，恢复网络后，DTS的同步任务没有自动恢复。

**处理方案**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单中选择**产品运维** > **数据库运维** **> DTS****运维****·DTS**。
3. 在任务列表中，单击目标任务，在**任务详情**页面，单击**同步**区域的**详情**。
4. 在**同步**页面，单击**重启**。
灾备管理中心处理
5. 等DTS恢复正常后，在ASR-DR控制台对目标保护实体执行重保护操作。
i. 在ASR-DR控制台的左侧导航栏，选择**业务容灾**>**保护组**。 ii. 在保护组列表中，单击目标保护组右侧的 ，选择**重保护**。

**说明**

如果网络中断超过18个小时，则Binlog可能丢失，此时，重保护只能重新建立全量链路。

#### 如何防止全量同步时Binlog日志丢失

本文介绍修改DStore保存Binlog文件的时间，防止全量同步时间较长时，Binlog日志被删除。

**背景信息**

DTS全量同步时，会将Binlog日志同步到DStore中，等全量同步完成后，再读取DStore中的Binlog日志。 DStore默认会将Binlog文件保存24小时。为了避免全量同步耗时很长时（例如超过24小时），Binlog日志已被删除，您可以修改DStore保存Binlog文件的时间。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单中选择**产品运维** > **数据库运维** **> DTS****运维****·DTS**。
3. 在任务列表中，单击目标任务。
4. 在**任务详情**页面，单击**DRC****信息**区域的Topic链接。
5. 在**DRC****控制台**，在对应Topic右侧**操作**列单击**选择**，在**操作**列单击**编辑**。
6. 更改保存时间。
i. 在对应Topic（假设为Topic A）的**操作**列，单击**关闭**。 DTS自动创建一个新的Topic（假设为Topic B）。 ii. 在Topic A所在行的**操作**列，单击**编辑**。 iii. 在**增量修改**页面，修改**数据保留时长**，单击**修改**。 iv. 在Topic A所在行的**操作**列，单击**重启**。单击**确定**。 灾备管理中心处理 v. 在Topic B所在行的**操作**列，单击**关闭**。 vi. 展开Topic A，在**状态**区域，检查有连接信息，类似如下图所示。 vii. 删除Topic B。

#### 如何防止主备中断时间过长导致Binlog日志丢失

您可以在RDS运维控制台上修改Binlog的本地保留时间，防止主备中断时间过长，导致Binlog日志丢失。

**背景信息**

RDS默认会将Binlog日志保留18小时。您可以在RDS运维控制台上修改Binlog的备份策略。

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 在左侧导航栏中选择**实例管理**>**实例列表**。单击目标实例名称。
4. 在**实例详情**的左侧导航栏中，单击**备份策略**。
5. 在**BINLOG****备份****ID**区域，单击**修改****BINLOG****备份策略**，设置**本地保留时间**。
6. 单击**提交**。

### OSS

#### 手工恢复OSS的同步链路

当主备OSS恢复正常，但是ASR-DR故障，无法短时间恢复的情况下，需要人工恢复OSS的同步链路。
1. 登录OSS控制台。
在Apsara Uni-manager运营控制台的顶部菜单栏，选择**产品**>**存储**>**对象存储****OSS**。
2. 在Bucket列表中单击目标Bucket。
3. 手动创建跨云同步链路。
灾备管理中心处理

**说明**

如果同步链路已存在，则忽略该步骤。 i. 单击**基础设置**页签，在**跨云复制**区域，单击**开启同步**。 ii. 在跨云复制面板配置数据同步的各项参数。

| 配置 | 说明 |
|---|---|
| 源Bucket地域 | 显示源Bucket所在地域。 |
| 源Bucket | 显示源Bucket名称。 |
| 同步目标云 | 输入目标云名称。 |
| 同步目标云地址 | 输入目标云Location。 |
| 目标Bucket | 填写目标Bucket名称。 |
| 数据同步对象 | 选择数据同步的对象。 全部文件进行同步：同步Bucket内所有文件。 指定文件名前缀进行同步：设置指定文件名前缀，可同步包含指定前缀的文件。单击添加可添加最多10个前缀。 |
| 数据同步策略 | 选择数据同步的策略。 增/改同步：仅将该Bucket内新增和更新的数据同步到目标Bucket。 增/删/改同步：将该Bucket的所有数据，包括新增、更新、删除操作同步到目标Bucket。 |
| 同步历史数据 | 选择是否同步设置跨云复制前Bucket已有的历史数据。 同步：将历史数据同步至目标Bucket。 不同步：仅同步设置跨云复制后上传或更新的文件。 |

iii. 单击**确定**保存配置。 等待3分钟左右，同步链路从**开启中**变为**运行中**。
4. 检查主备Bucket的数据是否一致。

#### OSS保护失败的排查思路

当OSS保护失败时，您可以从以下几方面去排查是否存在问题：
1. 检查源端OSS和备端OSS之间是否存在同步链路。
灾备管理中心处理如果同步链路不存在，则在ASR-DR的日志中查找 `getAddBucketReplicationRequest` 关键字，确认链路是否添加成功。如果添加失败，请联系ASR-DR产品研发工程师协助处理。
2. 检查ASR-DR上配置的OSS Endpoint是否正确。查看配置的方法请参见异地容灾管理平台ASR-DR用户指
南。
3. 检查chiji的版本大于等于v3.10 hotfix。

**说明**

v3.10 hotfix版本修复了OSS加速接口的问题。 i. 登录**oss-chiji.ChijiOssAll#**服务角色所在的容器，具体请参见登录容器。 ii. 查看 `/home/admin/admin_portal/ocm/ocm_cmd` 的 `setHistorySyncStatus` 参数的配置，正确的配置类似如下图所示。 如果配置没有问题，继续执行下一步。 iii. 退出容器，在生产站点的 `/cloud/log/oss-chiji/ChijiOssAll#/chiji_oss_all/logs` 目录中查看与ASR-DR日志里request_id相同的日志，重点看**ReplCloudService**类的日志。 如果日志显示类似如下信息，可能原因是chiji的版本低。

```json
{ "msg": "[system error] Failed to run cmd reload_sync_worker.py --sbucket=asrdr-32 1e-01 --slocation=oss-cn-****-d02-a --dbucket=asrdr-33e-10 --dlocation=oss-cn-****-d0 1-a! ERRORMSG = (255)exception run dsu failed!\n\n, pls contact chiji support, request_id: 601ef3f7-4cc3-****8f2c4cf22fbf", "code": -1, "format_version": "1.0", "success": false, "request_id": "601ef3f7-****-8f2c4cf22fbf", "value": {} }
```

4. 如果chiji的版本是匹配的，请查看加速接口的日志。如果日志显示成功，但返回200，请联系OSS产品技术
支持解决相关问题。

### MaxCompute

灾备管理中心处理

#### ASR-DR中配置MaxCompute项目返回空

**问题现象**

在ASR-DR的**添加实体**功能中，选择了主备DataWorks项目后，在选择MaxCompute项目时，查询不到

**问题原因**

MaxCompute和DataWorks需要满足如下要求，才允许建立容灾备份关系。 生产站点DataWorks的Project名称与灾备站点一致。

**处理方案**

1. 配置主备DataWorks的Project名称，确保一致。具体操作请参见DataWorks用户指南。
2. 配置主备MaxCompute的Project名称和任务云账号名称，确保一致。具体操作请参见MaxCompute用户
指南。

### MQ

#### 查看MQ实例主备端的消息详情

本文介绍ASR-DR无法查看MQ实例主备端消息消费和消息同步详情的处理方案。

**问题现象**

在ASR-DR无法查看MQ实例主备端消息消费和消息同步的详情。

**问题原因**

当前ASR-DR不具备此能力。

**处理方案**

1. 登录主备端mq-broker.DeployBroker#容器，具体操作，请参见登录容器。
2. 执行如下命令，查看消息消费和消息同步的详情。

```
sh rmq/bin/mqadmin consumerProgress -g <实例id>%<groupId> -t <实例id>%<topic>
```

灾备管理中心处理参数说明如下所示。

| 参数 | 描述 |
|---|---|
| Broker Offset | 主端所有消息。 |
| Consumer Offset | 已经消费的所有消息。 |
| Diff | 还未被消费的消息。 |
| LastTime | 最后消费时间。 |
| Diff Total | 未被消费消息总数。 |

#### 使用命令重置消费位点

主备切换后，备端查询已消费的消息数显示从0开始，或与主端相差较大时，您需要重置消费位点。

**问题现象**

当在ASR-DR执行主备切换后，在备端的消费者消费到大量重复消息，查看Consumer Offset是从0开始，或者与主端的Consumer Offset相差较大。查询Consumer Offset的具体操作，请参见查看MQ实例主备端的消息详情。

**问题原因**

MQ重置消费位点失败，主端的消费位点未被同步到备端，导致备端消费者在消息开始同步的时重新消费，备端将消费到大量重复的消息。

**处理方案**

1. 登录主备端mq-broker.DeployBroker#容器。具体操作，请参见登录容器。
2. 执行如下命令，重置消费位点。

```
sh rmq/bin/mqadmin resetOffsetByTime -g <实例id>%<groupId> -f true -s now -t <实例id>%<t opic>
```

灾备管理中心

## 校验容灾产品的数据一致性

本章节主要介绍在容灾切换过程中，当切换失败导致数据不一致、数据丢失时的处理方法。

### 全量校验并订正RDS和PolarDB-X的数

**据**

您可以通过备机房的DTS对RDS和PolarDB-X的数据库进行数据全量校验，并订正不一致的数据。

**背景信息**

**重要**

全量校验是对RDS和PolarDB-X的数据库进行全量数据遍历，该方式会影响数据库性能，请在业务低峰期联系现场运维工程师进行操作。
1. 登录备机房的Apsara Uni-manager运维控制台。
2. 在顶部菜单中选择**产品运维** > **数据库运维** **> DTS****运维****·DTS**。
3. 在**DTS****运维平台**的任务列表中查看DTS同步任务。单击任务名链接。
4. 在**任务详情**页面，单击右上角的**全量校验**。
5. 在**添加校验**页面配置相关参数，除了**是否订正**和**线程数**，其他参数请保持默认值。
灾备管理中心

**说明**

**是否订正**：请开启订正。
**线程数**：校验的并发数。线程数建议小于5，以免对数据库的压力过大。
6. 单击**添加**。
7. 在**任务列表**页面，单击上一步创建的校验任务的任务名。
8. 在**任务详情**页，单击**一致性校验**区域中的**详情**，查看校验的基本信息。
灾备管理中心在**基本信息**页面，单击**运行参数**后的**修改**，修改命令行参数，参数解释如下表所示。

| 名称 | 全称 | 描述 |
|---|---|---|
| -c | --config | 必选。配置文件路径。 |
| -x | --fix | 校验并订正。 说明订正数据差异必须指定该选项，默认关闭。 |
| -a | --server | DTS元数据库汇报选项，开启后会汇报进度和差异信息到数据库。默认为关闭。 |
| -l | --log | 指定日志、差异记录、订正sql 写入的文件路径。默认为程序所在路径。 |
| -b | --batch | 数据切片大小。默认值：3000，不建议修改。 |
| -A | --againbatch | 复检切片大小。请保留默认值300，不建议修改。 |
| -m | --max | 单表最大差异上限，当差异超过该值，退出该表校验。默认值 10000。 说明如果是异构数据源校验，建议适当调大该值。 |
| -p | --process | 指定校验线程池大小，与连接数同大小。默认值：4。云上建议2，集团建议7。 |

灾备管理中心

| -n | --nokey | 数据量小于该值的无唯一索引表才会被校验，RDS隐式索引被当作唯一索引处理。 该值过大可能导致慢sql 产生。默认值：10000， |
|---|---|---|
| -U | --upload | 与-a参数配合使用，指定上传到DTS元数据库中的差异最大值。默认值：300。 |
| -jobId | --jobId | 指定校验任务的jobId，DTS任务的唯一id。 |
| -encrypt | --encrypt | 配置文件采用DTS加密，与-jobId 配合使用。 |
| -L | --level | 与-x参数配合使用，指定订正级别。多个订正级别之间用正斜线 （/）分隔。例如：insert/update/delete。 |
| -ignore | --ignore | 暂不支持该参数。忽略级别，source/target/diff 的组合。 |
| -multiple | --multiple | 目的库使用等值查询，适用于分表到单表校验。无法校验目的多数据。 |
| -trim | --trim | 字符串对比忽略末尾空格，默认关闭。 |
| -singleindex | --singleindex | 使用单索引校验，适用于联合索引第一个字段有很高的区分度。默认关闭。oracle 开启该模式，查询性能有明显提升。 |
| -avoidCycle | --avoidCycle | 与-x 配合使用，开启防循环订正。默认关闭。 |
| -d | --diff | 校验上一次的差异。 |
| -record | --record | 校验上一次数据库记录的差异。 |

9. 在**一致性校验**的**校验对象**页签中查看校验结果。
灾备管理中心

**说明**

有差异的表，在**Diff Row**中单击图标可以查看差异详情。 您也可以通过日志查看校验结果，日志说明如下表所示。

| 场景 | 日志路径 | 备注 |
|---|---|---|
| 查询差异详情 | DTS运行节点机器/校验程序日志目录/diff | On master： 仅在源库存在的记录，仅仅打印索引。 On slave：仅在目的存在的记录，仅仅打印索引。 Different：源db和目的db索引相同，打印索引和差异字段，以及数据类型。 |
| 查询订正SQL | DTS运行节点机器/校验程序日志目录/sql | 无 |
| 查询当前差异信息 | DTS运行节点机器/校验程序日志目录/fullcheck.log | 如果界面的校验进度很慢，差异结果没有汇报，您可以在该日志中搜索WARN，该日志记录了差异记录的主键，可以通过源库和目的库人工对比数据。 |
| 查询具体的运行记录和报错信息 | DTS运行节点机器/校验程序日志目录/fullcheck.log | 如果要看对应的SQL执行详情，请在命令行加上参数 -g，所有的执行sql都会在日志里打印。 |

### 校验OSS数据一致性

您可以通过OSS赤骥工作流的创建bucket同步校验来查看主中心和备中心对应bucket的数据是否一致。

**操作步骤**

灾备管理中心
1. 登录主中心的数据魔方。
登录主中心的Apsara Uni-manager运维控制台，在顶部菜单栏单击**运维**。在左侧导航栏中单击**产品运维**
**管理** > **产品列表**。单击**存储** **> OSS**赤骥。
2. 在**数据魔方**的左侧导航栏中单击**运维支持** **> DRS****管理** > **跨云同步配置**。
3. 在**跨云同步管理**页面，选择一个集群，单击**查看本朵云参数**。
在**本朵云参数**页面查看并复制**本朵云名称**、**本朵云****Location**的值。
4. 在**跨云同步管理**页面，查看并复制**目标云名称**和**目标云****Location**的值。
5. 在**数据魔方**的左侧导航栏中单击**运维支持** > **赤骥工作流** > **工作流发布单**。
6. 在**所有工作流**页面，单击**创建任务**页签。
7. 配置相关参数，单击**提交**。

| 名称 | 描述 |
|---|---|
| 工作流名称 | 请选择bucket同步校验。 |
| 源集群 | 主中心的集群名称。 |
| 目标集群 | 备中心的集群名称。 |
| 源location | 步骤4中本朵云Location的值。 |
| 目标location | 步骤5中目标云Location的值。 |

灾备管理中心

| 源bucket | 主中心OSS的bucket的名称。 |
|---|---|
| 目标bucket | 备中心OSS的bucket的名称。 |
| 目标云 | 步骤5中目标云名称的值。 |
| 起始时间 | 可选参数。 |
| 定时执行 | 请根据实际需要选择定时执行的策略。 |
| 执行优先级 | 设置执行的优先级。保持默认值即可。 |
| 备注 | 填写该工作流的备注信息方便识别。 |

8. 单击**未完成的任务**页签，查看任务的执行状态。
9. 单击任务名称链接，在**任务详情**页签，查看任务的**操作状态**，若状态为**成功**，表示主备中心的对应bucket
的数据一致。

### 校验表格存储数据一致性

您可以在MaxCompute创建外部表，将Tablestore的数据导入到MaxCompute后，通过脚本查看数据是否一致。

**背景信息**

分别在主中心和备中心执行如下操作。
1. 登录MaxCompute控制台。
在Apsara Uni-manager运营控制台的顶部菜单栏中选择**产品** > **大数据计算** > **云原生大数据计算服务**
2. 创建云账号。
ii. 在**创建云账号**对话框中，设置云账号的名称和所属组织，单击**提交**。
3. 创建计算单元管理。
灾备管理中心 ii. 设置相关参数，单击**确认订单**。

**说明**

4. 创建计算引擎。
i. 在MaxCompute左侧导航栏单击**Project****管理**，在右侧单击**创建****Project**。

**说明**

**在DataWorks查询Tablestore数据条数**

1. 登录DataWorks控制台。
在Apsara Uni-manager运营控制台的顶部菜单栏中选择**产品** > **大数据计算** > **大数据开发治理平台**
**DataWorks** 。
2. **可选：**首次使用DataWorks时请添加MaxCompute引擎。

**说明**

如果界面提示没权限操作时，请单击切换组织和管理员权限进行操作。 i. 在DataWorks的顶部菜单栏中单击图标，进入工作空间列表。 ii. 在左侧导航栏中单击**计算引擎**，**MaxCompute****项目名称**选择对应的MaxCompute项目。
3. 在DataWorks的**DataStudio**页面新建业务流程。
灾备管理中心
4. 创建外部表。
ii. 在**新建节点**对话框中，设置节点名称和路径，单击**确认**。 灾备管理中心 iii. 创建一张MaxCompute的数据表，关联到Tablestore的某一张表。

```
set odps.sql.hive.compatible=true; set odps.sql.external.table.enable=true; CREATE EXTERNAL TABLE IF NOT EXISTS ots_external_table
```

`(--`（1）

```
id string, name string
```

)

```
STORED BY 'com.aliyun.odps.TableStoreStorageHandler'-- (2) WITH SERDEPROPERTIES (-- (3) 'tablestore.columns.mapping'=':id, :name',-- (4) 'tablestore.table.name'='test'-- (5)
```

)

```
LOCATION 'tablestore://<your_AccessKeyID>:<your_AccessKeySecret>@<YOUR_ENDPOINT>';-- (6) select count(*) as sum from ots_external_table;
```

| 标号 | 名称 | 描述 |
|---|---|---|
| （1） | id string, name string | 表字段。 |
| （2） | com.aliyun.odps.TableStoreSto rageHandler | MaxCompute内置的处理Tablestore数据的 StorageHandler，定义了MaxCompute和 Tablestore的交互，相关逻辑由MaxCompute实现。 |
| （3） | SERDEPROPERITES | 可以理解为提供参数选项的接口，在使用 TableStoreStorageHandler时，有两个必须指定的选项，分别是tablestore.columns.mapping和 tablestore.table.name。 |
| （4） | tablestore.columns.mapping | 必填选项。MaxCompute将要访问的 Tablestore表的列，包括主键和属性列。 其中，带 : 的表示 Tablestore主键，例如本示例中的 :vid 与 :gt ，其他均为属性列。在指定映射的时候，用户必须提供指定Tablestore表的所有主键，属性列无需全部提供，可以只提供需要通过MaxCompute来访问的属性列。 |
| （5） | tablestore.table.name | 需要访问的Tablestore表名。 如果指定的Tablestore 表名错误（不存在），则会报错。MaxCompute不会主动创建Tablestore表。 |
| （6） | LOCATION | 指定访问的Tablestore的实例信息，包括AccessKey ID、AccessKey Secret和endpoint。 |

5. 单击
图标执行脚本，查看主中心Tablestore的数据条数。 灾备管理中心
6. 在备中心执行以上步骤，如果备中心查询的数据条数和主中心一致，说明主备中心的Tablestore数据条数
一致。

### 校验MaxCompute数据一致性

校验MaxCompute数据一致性前需要提工单，找到研发同学获取校验工具，使用工具创建任务后，执行任务然后查看数据是否一致。

**操作步骤**

1. 创建任务。
使用接口/task/create，传入如下参数。 灾备管理中心

```json
{
 "srcRegionId": "cn-wulan-env200-d01",
 "srcInstanceId": "",
 "srcVpcId": "",
 "srcIp": "service.cn-wulan-env200-d01.odps.inter.env200.shuguang.com",
 "srcPort": 80,
 "srcAccountName": "nUYGMfdPj5Pz27Bn",
 "srcPassword": "0udAuvuQmUyFCOJknUcMbxVQMBdhgg",
 "dstRegionId": "cn-qingdao-env33-d01",
 "dstInstanceId": "",
 "dstVpcId": "",
 "dstIp": "service.cn-qingdao-env33-d01.odps.env33.com",
 "dstPort": 80,
 "dstAccountName": "6a3F0hFBKZow1iBK",
 "dstPassword": "qIGHPdTxdGOPBBi7Qh9FljXJfod5ty",
 "productName": "ODPS",
 "compareObjectList": [
 {
 "dbName": "consistency_test",
 "compareTables": [
 {
 "tableName": "t_1m"
 },
 {
 "tableName": "t_10m"
 },
 {
 "tableName": "t_100m"
 },
 {
 "tableName": "t_1g"
 },
 {
 "tableName": "t_10g"
 },
 {
 "tableName": "t_100g"
 }
```

]

```
 }
```

`],`

```json
 "timeout": 600000,
 "taskType": "STANDARD"
}
```

如果返回结果如下所示，则表示创建成功。 灾备管理中心
2. 启动任务。
使用接口/task/start，传入如下参数。

```json
{
 "taskId" : 253687010591954944
}
```

返回结果如下，表明启动成功： RUNNING/ARCHIVED并调用接口，返回结果均为：
3. 查看执行结果，执行结果成功或失败请参考下表。

| 场景 | 说明 | 回写内容 |
|---|---|---|

灾备管理中心

| 任务成功完成 | 说明任务已经执行完成，一致性校验成功，并正确显示各个子步骤的状态。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": true, "taskStatus": "FINISHED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692183383554, "costTime": 254385, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "FINISHED" } ], "detailLog": "" } } } |
|---|---|---|

灾备管理中心

| 超时导致失败 | 可以正确显示任务的失败原因为Timeout。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692185149634, "costTime": 60714, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "RUNNING" } ], "detailLog": "Timeout" } } } |
|---|---|---|

灾备管理中心

| 表缺失导致预校验失败 | 在子步骤状态中可以正确地显示在预校验时失败，失败原因为“获取目标端表结构失败”。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692185454492, "costTime": 6246, "stepStatus": [ { "stepName": "PRECHECK", "status": "FAILED" }, { "stepName": "CHECKROWCOUNT", "status": "" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "获取目标端表结构失败" } } } |
|---|---|---|

灾备管理中心

| 表行数不一致导致失败 | 在返回结果中，任务状态为失败，子步骤 CHECKROWCOUNT状态为失败，并成功显示失败原因。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692196225091, "costTime": 16451, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FAILED" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "目标端表:t 1m,数据行:4095,和源端 _ 数据行:4096 不一致" } } } |
|---|---|---|

灾备管理中心

| 表数据不一致导致失败 | 任务状态为失败，子步骤 CHECKDATA状态为失败，并成功显示失败原因。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692196609544, "costTime": 15402, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "FAILED" } ], "detailLog": "源端、目标端校验表t 1m的校验值不 _ 匹配，源端6ab792ad，目标端c9256398" } } } |
|---|---|---|

**相关操作**

| 任务名称 | 说明 | 操作内容 |
|---|---|---|

灾备管理中心

| 重试任务 | 重试任务的功能可以在任务失败时进行调用，调用后只会启动未开始运行的子任务，因此测试需要关注该功能是否正常。 重试任务时会重新在源端创建t 1m _ 表，确保该表与目标端一致，并调用/task/retry接口进行重试，获取任务执行结果。 此时，任务状态为成功，且耗时为 13778毫秒，是只对t 1m表进行一致 _ 性校验的时间，表明重试功能正常。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": true, "taskStatus": "FINISHED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692197074880, "costTime": 13778, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "FINISHED" } ], "detailLog": "" } } } 返回结果： { "timestamp": 1692201556515, "status": 500, "error": "Internal Server Error", "message": "The status of consistency is invalid", "path": "/asr-web/task/retry" } |
|---|---|---|

灾备管理中心

| 停止功能 | 该接口只能在任务状态为RUNNING时调用。启动任务，并调用接口/task/stop， 任务状态为STOPPED，在子步骤 CHECKROWCOUNT执行过程中停止。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "STOPPED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692198894885, "costTime": 7747, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "STOPPED" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "stopped" } } } 返回结果： { "timestamp": 1692201618671, "status": 500, "error": "Internal Server Error", "message": "The status of consistency is invalid", "path": "/asr-web/task/stop" } |
|---|---|---|

灾备管理中心

| 删除功能 | 当任务状态不是RUNNING时调用/task/delete，任务状态为 ARCHIVED。 | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "ARCHIVED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692198894885, "costTime": 7747, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "STOPPED" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "stopped" } } } 返回结果： { "timestamp": 1692201760347, "status": 500, "error": "Internal Server Error", "message": "The status of consistency is invalid", "path": "/asr-web/task/delete" } |
|---|---|---|

灾备管理中心

## 命令参考

### 如何使用CLISH命令

当ASR-DR出现异常，ASR-DR控制台无法登录时，运维人员可以通过命令行进行后台操作。

**警告**

操作前，请确保已深刻了解每个命令行的作用和可能带来的后果。 命令行操作的危险系数较高，需要谨慎操作。只有当ASR-DR系统出现异常，网页无法修复时才进行后台命令行操作。
1. 登录ASR-DR容器。具体操作，请参见登录容器。
2. 执行如下命令启动交互命令。

```
cd /alidata/bin/ java -jar clish-3.0.0.jar
```

3. 输入待执行的命令。

### 命令列表

### 同步实体

| 名称 | 描述 |
|---|---|
| skip-entity | 跳过当前同步实体执行计划步骤。 |
| suspend-entity | 暂停同步实体。 |
| stepover-entity | 同步实体单步骤跳过。 |
| reprotect-entity | 同步实体重保护。 |
| redo-entity | 同步实体重做。 |
| force-switch | 强制切换。 |

### 云中心

灾备管理中心

| 名称 | 描述 |
|---|---|
| del-cloud-instance | 删除用户与云实例的关联关系。 |
| del-cloud-center | 删除云中心。 |

### 保护组

| 名称 | 描述 |
|---|---|
| create-empty-pg | 创建空保护组。 |
| show-pg-sync-entity | 查看指定保护组包含的同步实体。 |
| delete-pg-shell | 删除保护组。 |
| move-sync-entity | 将同步实例搬迁到指定保护组ID里。 |

### 容灾计划

| 名称 | 描述 |
|---|---|
| plan-query | 查询容灾计划的详细信息。 |
| plan-query-ex | 查询容灾计划任务的详细信息。 |
| plan-force-delete | 强制删除计划，包括正在运行中的计划。 |

### VPC

| 名称 | 描述 |
|---|---|
| vpc-register-app | 注册VPC应用。 |
| vpc-show-registered-app | 查询已注册的VPC应用。 |
| vpc-remove-registered-app | 移除已注册的VPC应用。 |

灾备管理中心

| 名称 | 描述 |
|---|---|
| vpc-grant-access | 实例访问授权。 |
| vpc-show-grant-access | 查看指定VPC实例的授权列表。 |
| vpc-cancel-grant-access | 取消实例访问授权。 |

| 名称 | 描述 |
|---|---|
| xdm-clear-data | 清理xdm的数据。 |

| 名称 | 描述 |
|---|---|
| adb-force-start-sync | 强制启动同步链路。 |

### 配置相关

| 名称 | 描述 |
|---|---|
| param-add-param | 添加配置信息。 |
| param-modify-param | 修改配置信息。 |
| param-query-param | 查询配置信息。 |
| param-refresh-param | 刷新配置信息。 |
| param-modify-params | 修改产品的配置信息。 |
| param-query-params | 查询产品的配置信息。 |

**告警**

灾备管理中心

| 名称 | 描述 |
|---|---|
| alarm-create | 创建告警实例。 |
| alarm-query | 查询告警信息。 |
| send-alarm-msg | 发送告警信息。 |

### 告警规则

| 名称 | 描述 |
|---|---|
| rule-create | 创建告警规则。 |
| rule-query | 查询告警规则。 |
| rule-switch | 启用或停用告警规则。 |
| rule-update | 更新告警规则。 |
| rule-delete | 删除告警规则。 |

### 监控项

| 名称 | 描述 |
|---|---|
| monitor-item-query | 查询监控项。 |

### 同步实体

#### skip-entity

**命令语法**

**参数解释**

灾备管理中心

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -eid | 是 | 同步实体的ID。 |

**示例**

```
skip-entity -eid 5e81a414-4d88-4de3-9921-f1ef51f******
```

#### suspend-entity

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -eid | 是 | 同步实体的ID。 |

**示例**

```
suspend-entity -eid 45eadd00-68a4-462d-85fb-c81bb******
```

#### stepover-entity

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -eid | 是 | 同步实体的ID。 |

**示例**

```
stepover-entity -eid 45eadd00-68a4-462d-85fb-c81bb******
```

灾备管理中心

#### reprotect-entity

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -eid | 是 | 同步实体的ID。 |

**示例**

```
reprotect-entity -eid 45eadd00-68a4-462d-85fb-c81bbd******
```

#### redo-entity

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -eid | 是 | 同步实体的ID。 |

**示例**

```
redo-entity -eid 45eadd00-68a4-462d-85fb-c81bbd******
```

#### force-switch

**命令语法**

**参数解释**

灾备管理中心

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -sid | 是 | 同步实体的ID。 |

**示例**

```
force-switch -sid 45eadd00-68a4-462d-85fb-c81bb******
```

### 云中心

#### del-cloud-instance

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -uid | 是 | 用户的ID。 |
| -cid | 是 | 云实例的ID。 |

**示例**

```
del-cloud-instance -uid 5003 -cid bc982df6-f193-4aab-a6e2-b8b240******
```

#### del-cloud-center

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -cid | 是 | 待删除云中心的ID。 |

灾备管理中心

**示例**

```
del-cloud-center -cid e6671a7c-26af-4737-b930-1b37a5******
```

### 保护组

#### create-empty-pg

**命令语法**

```
create-empty-pg [-pname] string [-morgid] int [-borgid] int [-mcid] string [-bcid] string [-mrid] string [-brid] string [-d] string [-D] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pname | 是 | 保护组名称。 |
| -morgid | 是 | 生产站点组织的ID。 |
| -borgid | 是 | 灾备站点组织的ID。 |
| -mcid | 是 | 生产站点的ID。 |
| -bcid | 是 | 灾备站点的ID。 |
| -mrid | 是 | 生产站点地域的ID。 |
| -brid | 是 | 灾备站点地域的ID。 |
| -d | 是 | 同步方向，参数说明如下： FORWARD：正向。 REVERSE：反向。 |
| -D | 是 | 描述信息 |

**示例**

灾备管理中心

```
create-empty-pg -pname pgClish -morgid 30 -borgid 3 -mcid d132c3b0-4299-4d0a-9962-350****
* -bcid 61f1f331-76df-43be-8bf2-856e75d***** -mrid cn-qingdao-*****-d01 -brig cn-
qingdao-*****-d01 -d FORWARD -D testGroupBuileby****
```

#### show-pg-sync-entity

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pgId | 是 | 保护组的ID。 |

**示例**

```
show-pg-sync-entity -pgId 0f0cc4dc-c95f-47cb-b8b4-1a72e2******
```

#### delete-pg-shell

您可以使用delete-pg-shell删除保护组，不删除同步实例，同步实例变为游离态。

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pgId | 是 | 保护组的ID。 |

**示例**

```
delete-pg-shell -pgId cb973344-3a7d-49f5-8517-6245bd******
```

#### move-sync-entity

**命令语法**

灾备管理中心

```
move-sync-entity [-sid] string [-pgId] string [-p] int
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pgId | 是 | 保护组的ID。 |
| -sid | 是 | 同步实体ID。 |
| -p | 是 | 优先级。 |

**示例**

```
move-sync-entity -sid 5e81a414-4d88-4de3-9921-f1ef51f***** -pgId 472481ee-717c-41bc-b3b8- 192631f***** -p 3
```

### 容灾计划

#### plan-query

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -pid | 是 | 容灾计划的Id。 |

**示例**

**plan-query -pid 375c09d5-e803-4770-a3ec-fa4358**

#### plan-query-ex

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -pid | 是 | 容灾计划的Id。 |

灾备管理中心

**示例**

**plan-query-ex -pid 375c09d5-e803-4770-a3ec-b37fa4**

#### plan-force-delete

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -pid | 是 | 容灾计划的ID。 |

**示例**

```
plan-force-delete -pid f67e0b29-519a-433d-bf8f-b38fb4******
```

### VPC

#### vpc-register-app

**命令语法**

```
vpc-register-app [-c] string [r] string [-ips] strings
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -c | 是 | 云实例的ID。 |
| -r | 是 | 地域的ID。 |
| -ips | 是 | 注册的IP，为JSON数组格式。 |

**示例**

```
vpc-register-app -c ff28e461-fbec-449e-8d33-94d7f0****** -r cn-******-***-d01 -ips []
```

灾备管理中心

#### vpc-show-registered-app

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -c | 是 | 云实例的ID。 |
| -r | 是 | 地域的ID。 |

**示例**

```
vpc-show-registered-app -c ff28e461-fbec-449e-8d33-94d7f0****** -r cn-*****-***-d01
```

#### vpc-remove-registered-app

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -c | 是 | 云实例的ID。 |
| -r | 是 | 地域的ID。 |

**示例**

```
vpc-remove-registered-app -c ff28e461-fbec-449e-8d33-94d7f0****** -r cn-*****-***-d01
```

#### vpc-grant-access

**命令语法**

灾备管理中心

```
vpc-grant-access [-v] string [-i] string [-p] string [-r] string [-c] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -v | 是 | 实例所在VPC网络的ID。 |
| -i | 是 | 目标容灾产品实例的ID。 |
| -p | 是 | 实例端口。 |
| -r | 是 | 地域的ID。 |
| -c | 是 | 云实例的ID。 |

**示例**

```
vpc-grant-access -v vpc-7qc0ujuxfw838m9n****** -i rm-7qcv3h8q497****** -p 3306 -r cn-**** *-***-d01 -c a37eb466-cc43-4347-9e96-5685dbc*****
```

#### vpc-show-grant-access

**命令语法**

```
vpc-show-grant-access [-c] string [-i] string [-r] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -c | 是 | 云实例的ID。 |
| -i | 是 | 实例的ID。 |
| -r | 是 | 地域的ID。 |

**示例**

```
vpc-show-grant-access -c a37eb466-cc43-4347-9e96-5685dbc1**** -i rm-7qcv3h8q497****** -r cn-*****-***-d01
```

灾备管理中心

#### vpc-cancel-grant-access

**命令语法**

```
vpc-cancel-grant-access [-c] string [-v] string [-i] string [-p] string [-r] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -c | 是 | 云实例的ID。 |
| -v | 是 | 目标容灾产品实例所在VPC网络的ID。 |
| -i | 是 | 目标容灾产品实例的ID。 |
| -p | 是 | 实例端口。 |
| -r | 是 | 地域的ID。 |

**示例**

```
vpc-cancel-grant-access -c a37eb466-cc43-4347-9e96-5685dbc1**** -v vpc- 7qc0ujuxfw838m9n****** -i rm-7qcv3h8q497****** -p 3306 -r cn-*****-***-d01
```

### 云原生分布式数据库PolarDB-X

#### xdm-clear-data

**命令语法**

```
xdm-clear-data [-c] string [-r] string [-i] string [-t] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -c | 是 | 云实例ID。 |

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -r | 是 | 地域ID。 |
| -i | 是 | 云产品实例ID。 |
| -t | 是 | 云产品实例类型。 |

**示例**

```
xdm-clear-data -c a37eb466-cc43-4347-9e96-5685dbc1**** -r cn-*****-****-d01 -i rm-7qczre4 wb67****** -t ADB
```

### 云原生数据仓库AnalyticDB MySQL

**版3.0**

#### adb-force-start-sync

**命令语法**

```
adb-force-start-sync [-r] string [-c] string [-i] string [-pk] string [-oppId] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -r | 是 | 地域ID。 |
| -c | 是 | 云实例ID。 |
| -i | 是 | 产品实例的ID。 |
| -pk | 是 | 用户的Primary Key。 |
| -oppId | 是 | 目的端的集群ID。 |

**示例**

灾备管理中心

```
adb-force-start-sync -i drdsusrzl1****** -r cn-*****-***-d01 -c a624e61c-c37e-4771-be06-1 d725cd2**** -pk 1223333 -oppId 6aYxs
```

### 配置相关

#### param-add-param

**命令语法**

```
param-add-param [-pdn] string [-pn] string [-pv] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pdn | 是 | 产品名称。 |
| -pn | 是 | 属性名称。 |
| -pv | 是 | 属性值。 |

**示例**

#### param-modify-param

**命令语法**

```
param-modify-param [-pdn] string [-pn] string [-pv] string
```

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pdn | 是 | 产品名称。 |
| -pn | 是 | 属性名称。 |

| 异地容灾管理平台运维指南· | 命令参考 | 灾备管理中心 |
|---|---|---|

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pv | 是 | 属性值。 |

**示例**

#### param-query-param

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pdn | 是 | 产品名称。 |
| -pn | 是 | 属性名称。 |

**示例**

#### param-refresh-param

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pdn | 是 | 产品名称。 |
| -pn | 是 | 属性名称。 |

灾备管理中心

**示例**

#### param-modify-params

**命令语法**

**参数解释**

| 名称 |  | 是否必填 | 描述 |  |
|---|---|---|---|---|
| -pj |  | 是 | 产品中所有属性值的JSON数组集合。 格式如下： [{"product":"产品名称","params":{"配置项名称":"配置信息","配置项名称":"配置信息"}}] 多个配置信息间以英文半角逗号（,）隔开。 |  |
|  |  |  |  | [{"product":"产品名称","params":{"配置项名 |
|  |  |  | 称":"配置信息","配置项名称":"配置信息"}}] |  |

**示例**

```json
param-modify-params -pj '[{"product":"oss","params": {"apiRetryCount":"5","apiRetryDelay":"40000"}}]'
```

#### param-query-params

**命令语法**

**参数解释**

| 名称 | 是否必填 | 描述 |
|---|---|---|
| -pdn | 是 | 产品名称。 |

**示例**

灾备管理中心

### 告警

#### alarm-create

**命令语法**

**alarm-create [-r] string [-alarmObjId] string [-c] string**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -r | 是 | 告警规则ID。 |
| -alarmObjId | 是 | 告警对象信息。数组的 JSON对象，格式如下： [\"objectId1\",\"objectId2\"] |
| -c | 是 | 告警内容。 |

**示例**

**alarm-create -r 72b079c4-ce56-45cb-8dae- -alarmObjId [\"ef894d5d-3dee-4e6a-**

**b989-e946ede\"] -c test**

#### alarm-query

**命令语法**

**alarm-query [-n] string [--monitorId] string [-alarmObjName] string [-l] string [-st]**

**string [-et] string [-c] string**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -n | 否 | 告警规则名称。 |
| --monitorId | 否 | 监视项ID。 |
| -alarmObjName | 否 | 告警对象名称。 |
| -l | 否 | 告警规则等级，数值类型。您可以选择以下几种等级： 1：FATAL。 2：ERROR。 3：WARNING。 4：INFO。 |
| -st | 否 | 告警开始时间，格式为Unix时间戳。 说明您可以通过相关工具将时间转换为 Unix时间戳，单位为毫秒。 |

灾备管理中心

| -et | 否 | 告警结束时间，格式为Unix时间戳。 |
|---|---|---|
| -c | 否 | 云实例ID。 |

**示例**

**alarm-query -n testRule --monitorId PROTECT_STATE -l 2 -alarmObjName otsTest -st**

**"2021-11-25 00:00:00" -et "2021-11-25 23:59:59" -c 6ca60a24-2d3d-4221-b5d3-**

**b7998d5**

#### send-alarm-msg

**命令语法**

**send-alarm-msg [--monitorId] string [-l] string [-alarmObjName] string [-lookAddr]**

**string [-c] string [--notifyType] string [--notifyUserIds] string**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| --monitorId | 是 | 监视项ID。 |
| -l | 是 | 告警级别，数值类型。包括： 1：FATAL 2：ERROR 3：WARNING 4：INFO |
| -alarmObjName | 是 | 告警对象名称。 |
| -lookAddr | 是 | 告警详情的地址，用户看到告警后，可通过该地址查看告警详情。 |
| -c | 是 | 告警内容。 |
| --notifyType | 是 | 告警通知的类型，数据使用JSON数组格式。选项包括： ASO ANS DING _ ANS EMAIL _ ANS SMS _ |
| --notifyUserIds | 是 | 告警通知人的PrimaryKey。数据使用JSON数组格式。 |

**示例**

**send-alarm-msg --monitorId PROTECT_STATE -l 2 -alarmObjName testObj -lookAddr**

**WWW.example.COM -c example --notifyType [\"ANS_EMAIL\"] --notifyUserIds**

**[\"2638888\"]**

### 告警规则

#### rule-create

灾备管理中心

**命令语法**

**rule-create [-n] string [-c] string [--deptId] string [--monitorId] string [-o] string [-v]**

**string [-d] string [-l] string [--notifyUserIds] string [--notifyType] string**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -n | 是 | 告警规则名称。 |
| -c | 是 | 云实例ID。 |
| --deptId | 是 | 组织ID。 |
| --monitorId | 是 | 监听类型。 |
| -o | 是 | 比较符，例如等号（=）。 |
| -v | 是 | 匹配值。 |
| -d | 是 | 告警规则的描述。 |
| -l | 是 | 告警级别，数值类型。包括： 1：FATAL 2：ERROR 3：WARNING 4：INFO |
| --notifyUserIds | 是 | 告警通知人的用户名，使用JSON数组格式。 |
| --notifyType | 是 | 告警通知的类型，使用JSON数组格式。选项包括： ASO ANS DING _ ANS EMAIL _ ANS SMS _ |

**示例**

**rule-create -n testRule -c 6ca60a24-2d3d-4221-b5d3-b7998d5 --deptId 3 --**

**monitorId PROTECT_STATE -o = -v PROTECT_FAIL -d 测试描述 -l 2 --notifyUserIds**

**[\"ExampleUser\"] --notifyType [\"ANS_EMAIL\"]**

#### rule-query

**命令语法**

**rule-query [-n] string [-l] string [--deptId] string [--monitorId] string [-s] string [-c]**

**string**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|

灾备管理中心

| -n | 是 | 告警规则名称。 |
|---|---|---|
| -l | 否 | 告警级别，数值类型。包括： 1：FATAL 2：ERROR 3：WARNING 4：INFO |
| --deptId | 否 | 组织ID。 |
| --monitorId | 否 | 监视项的ID。 |
| -s | 否 | 规则状态，包括： STOPPED RUNNING |
| -c | 否 | 云实例ID。 |

**示例**

**rule-query -n testRule -s RUNNING -l 2 --deptIds [\"20\"] --monitorId PROTECT_STATE**

**-c 6ca60a24-2d3d-4221-b5d3-b79982c4**

#### rule-switch

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -rid | 是 | 告警规则ID。 |
| -s | 是 | 启用或停用告警规则。 RUNNING：启用 STOPPED：停用 |

**示例**

**rule-switch -rid 72b079c4-ce56-45cb--71b94f7e6f9c -s STOPPED**

#### rule-update

**命令语法**

**rule-update [-r] string [-n] string [--deptId] string [--monitorId] string [-o] string] [-**

**v] string [-d] string [-l] string [--notifyUserIds] string [--notifyType] string [-u] string**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|

灾备管理中心

| -r | 是 | 告警规则ID。 |
|---|---|---|
| -n | 是 | 告警规则名称。 |
| --deptId | 是 | 组织ID。 |
| --monitorId | 是 | 监控项 |
| -o | 是 | 比较符，例如等号（=）。 |
| -v | 是 | 匹配值。 |
| -d | 是 | 告警规则的描述。 |
| -l | 是 | 告警级别，数值类型。包括： 1：FATAL 2：ERROR 3：WARNING 4：INFO |
| --notifyUserIds | 是 | 告警通知人的用户名，使用JSON数组格式。 |
| --notifyType | 是 | 告警通知的类型，使用JSON数组格式。选项包括： ASO ANS DING _ ANS EMAIL _ ANS SMS _ |
| -u | 是 | 用户ID。 |

**示例**

**rule-update -n testRuleNew --deptId 20 --monitorId PROTECT_STATE -o = -v**

**PROTECT_FAIL -d 测试描述 -l 2 --notifyUserIds [\"testUser\"] --notifyType**

**[\"ANS_EMAIL\"] -r 76df66ad-ecdb-4b35-ac50-931e886 -u 123456789**

#### rule-delete

**命令语法**

**参数解释**

| 名称 | 是否必选 | 描述 |
|---|---|---|
| -r | 是 | 告警规则ID。 |
| -u | 是 | 用户ID。 |

**示例**

**rule-delete -r 9c8bdc83-3a32-4ae0--e8b7b1c31124 -u 123456789**

### 监控项

灾备管理中心

#### monitor-item-query

**命令语法**

**示例**

灾备管理中心

## 附录

### internet-domain、intranet-

**domain的查找方式**

**操作步骤**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 进入**产品列表**页面，在查询框中输入 `baseServiceAll` ，在目标集群**操作**列单击**集群详情**。
5. 在**集群详情**页面，单击**终态配置**页签。
6. 选中**kv.conf**文件，单击**显示内容**。
7. 在**kv.conf**文件中获取internet-domain和intranet-domain的值。

### DNS地址查找方式

本文介绍DNS地址的查找方式。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在**产品列表**中搜索dnsProduct，在目标集群**操作**列单击**集群详情**。
5. 单击**终态配置**页签，选择 `services/dnsService/user/dns.conf` 文件。
灾备管理中心
6. 单击**显示内容**，其中anycastVip为dns的NameServer IP，与DNS管控界面ServerIP一致。

**说明**

internetIps字段的前2个IP为DNS发起forward的源，这些IP分别绑定在bindServerRole容器中，通常情况下只有2个IP。

### 配置DNS域名转发

两朵云做主备容灾时，需要在生产端和灾备端分别配置域名访问，打通域名解析功能，本文指导用户如何配置 DNS域名访问。

**重要**

在配置过程中由于添加生产端opsDns到生产端的dnsProduct的转发需要修改tianji配置文件并rolling tianji集群，自动化配置风险较高，因此需要用户手动配置。其他内容会自动配置。

**前提条件**

生产端和灾备端网络已打通。 生产端已成功部署，并在容器内生成DNS配置文件。

**说明**

如果前提条件不满足，请参考手动配置DNS转发进行配置。

**自动化配置两端DNS域名转发**

1. 获取生产端opsadmin的AK/SK和pop-vip-ops。
i. 以opsadmin登录Apsara Uni-manager运维控制台。 ii. 单击右上角 ，单击**个人信息**。 灾备管理中心 iii. 获取opsadmin的AK/SK。 iv. 在菜单栏中选择**平台运维** > **飞天基础运维平台** > **资源管理**。 v. 在**产品集群运维**页面，输入webappAll，查看StandardCloudCluster集群详情。 vi. 单击**操作**列**集群详情**，在集群详情页面单击**资源详情**。 vii. 查看pop-vip-ops的资源详情，单击资源申请结果，获取并保存vip_ip的值。

**说明**

如果生产端的pop-vip-ops发生了变化，需要重新rolling生产端asrdr集群。 在灾备端ASR-DR容器内执行以下命令。 pop_vip_ops，ops_admin_ak，ops_admin_sk替换成上述步骤获取到的值，生产端到灾备端的DNS 转发规则和IP白名单配置完成，灾备端到生产端的DNS转发规则和IP白名单配置完成。

```
python alidata/bin/dns/auto_config_dns.py asrdr -v {pop_vip_ops} -a {ops_admin_ak} -s {ops_admin_sk}
```

灾备管理中心 viii. 在本端ASR-DR容器的/home/admin/asrdr/config/dns/dns_conf.{regionId}.ops获取内容。
2. 新增OPS-DNS到本云租户DNS的转发规则。
i. 登录至Apsara Uni-manager运维控制台。 ii. 在菜单栏中选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**产品集群运维**页面，输入tianji，搜索tianji集群。 iv. 单击**操作**列**集群详情**，在集群详情页面单击**终态配置**。 灾备管理中心 v. 在左侧搜索框中输入dns_zone.conf.jj2，单击显示内容，将步骤一获取到的dns_conf. {regionId}.ops内容添加到该文件中。 内容格式如下所示：

```
zone_forwarders:
  - zone: 对端云internet-domain
    forwarders:
```

    - 本云租户`DNS nameserver`地址
    - 本云租户`DNS nameserver`地址

```
  - zone: 对端云intranet-domain
    forwarders:
```

    - 本云租户`DNS nameserver`地址
    - 本云租户`DNS nameserver`地址
vi. 添加后单击**预览并提交**。 vii. 单击**集群****Rolling**。 viii. 待Tianji集群rolling完成后，为使tianji配置生效，下面两种方式选择一种执行： 进入ops1/2的dnsslave容器中分别执行：/root/opsbuild/deploy.py （执行该命令前要请关闭BGP 进程，否则在执行deploy.py期间会重启named，导致云平台域名解析一段时间不可用，通常情况下是秒级，对云平台无大影响，但存在小概率deploy卡住的情况存在，建议关闭进程。操作：通过ps aux | grep bgp过滤下，并kill -9。） 逐一重启DnsSlave#节点。（必须等待前一个重启到终态后再重启下一个。） 如果主云是同城容灾双机房，B机房也需要配置转发规则，执行上面使tianji配置生效的操作。
3. 检查执行结果。
i. 在Apsara Uni-manager运维控制台，选择**安全管理** > **网络安全** > **网络安全管理中心**。 灾备管理中心 ii. 在左侧导航栏中选择**东西向安全管理** **> DNS****转发规则**。 iii. 登录Apsara Uni-manager运营控制台，选择**产品** > **网络** > **云上网络** > **云解析** **DNS**。 iv. 在**云内全局域名**页面，选择**全局转发配置**页签。 v. tianji集群rolling成功，dns_zone.conf.jj2固化成功。

**手动配置DNS转发**

1. 将生产端/home/admin/asrdr/config/dns/路径下的dns配置文件dns_conf.{des_region}，拷贝到灾备
端ASR-DR容器/home/admin/asrdr/config/dns/下。（如果生产端没有部署ASR-DR，可以按照配置文件格式及命名规则将文件放至指定目录。）
2. 在灾备端的ASR-DR容器里执行以下命令。

```bash
python /alidata/bin/dns/auto_config_dns.py manual -r des_region
# des_region目标端region
```

当前操作在灾备端ASR-DR执行，仅完成灾备端到生产端的DNS转发规则和ip白名单配置灾备管理中心
3. 在本端ASR-DR容器的/home/admin/asrdr/config/dns/dns_conf.{regionId}.ops获取内容。
4. 参考上述步骤在生产端ASR-DR容器再执行一遍。
5. 新增OPS-DNS到本云租户DNS的转发规则。
i. 登录至Apsara Uni-manager运维控制台。 ii. 在菜单栏中选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**产品集群运维**页面，输入tianji，搜索tianji集群。 iv. 单击**操作**列**集群详情**，在集群详情页面单击**终态配置**。 灾备管理中心 v. 在左侧搜索框中输入dns_zone.conf.jj2，单击显示内容，将步骤三获取到的dns_conf. {regionId}.ops内容添加到该文件中。 内容格式如下所示：

```
zone_forwarders:
  - zone: 对端云internet-domain
    forwarders:
```

    - 本云租户`DNS nameserver`地址
    - 本云租户`DNS nameserver`地址

```
  - zone: 对端云intranet-domain
    forwarders:
```

    - 本云租户`DNS nameserver`地址
    - 本云租户`DNS nameserver`地址
vi. 添加后单击**预览并提交**。 vii. 单击**集群****Rolling**。 viii. 待tianji集群rolling完成后，为使tianji配置生效，下面两种方式选一种执行即可： 进入ops1/2的dnsslave容器中分别执行：/root/opsbuild/deploy.py （执行该命令前要请关闭BGP 进程，否则在执行deploy.py期间会重启named，导致云平台域名解析一段时间不可用，通常情况下是秒级，对云平台无大影响，但存在小概率deploy卡住的情况存在，建议关闭进程。操作：通过ps aux | grep bgp过滤下，并kill -9） 逐一重启DnsSlave#节点。（必须等待前一个重启到终态后再重启下一个） 如果主云是同城容灾双机房，B机房也需要配置转发规则，执行上面使tianji配置生效的操作。
6. 检查执行结果。
i. 在Apsara Uni-manager运维控制台，选择**安全管理** > **网络安全** > **网络安全管理中心**。 灾备管理中心 ii. 在左侧导航栏中选择**东西向安全管理** **> DNS****转发规则**。 iii. 登录Apsara Uni-manager运营控制台，选择**产品** > **网络** > **云上网络** > **云解析** **DNS**。 iv. 在**云内全局域名**页面，选择**全局转发配置**页签。 v. tianji集群rolling成功，dns_zone.conf.jj2固化成功。

### 配置DTS参数

两朵云做主备容灾时，数据库类产品需要对DTS进行相关配置。本文指导用户如何配置DTS。

**前提条件**

生产端和灾备端网络已打通。 生产端已成功部署ASRDR，并在容器内生成DTS SQL模板文件。

**说明**

如果前提条件无法满足，请参考手动配置本端DTS进行配置。

**自动化配置本端DTS**

1. 获取生产端opsadmin的AK/SK和pop_ops_vip。
i. 以opsadmin登录Apsara Uni-manager运维控制台。 ii. 单击右上角 ，单击**个人信息**。 灾备管理中心 iii. 获取opsadmin的AK/SK。 iv. 在菜单栏中选择**平台运维** > **飞天基础运维平台** > **资源管理**。 v. 在**产品集群运维**页面，输入webappAll，查看StandardCloudCluster集群详情。 vi. 单击**操作**列**集群详情**，在集群详情页面单击**资源详情**。 vii. 查看ops的资源详情，单击资源申请结果，获取vip_ip的值。
2. 登录灾备ASR-DR容器，请参见登录容器。
3. 在灾备端容器内执行以下命令。

```
python alidata/bin/dts/dts_new/auto_config_dts.py asrdr -v {pop_ops_vip} -a {ops_admin_ ak} -s {ops_admin_sk}
```

pop_ops_vip、ops_admin_ak和 ops_admin_sk替换成上述步骤获取到的值，脚本执行完成后会在灾备端DTS数据库插入生产端相关信息。
4. 在灾备端DTS数据库内执行以下命令，查看DTS数据库。

```
select * from region_pattern where pattern_expression = '^区域ID'\G
```

灾备管理中心

```
select * from config where config_code = 'cross_cloud_internet_check_flag'; select * from region_list where REGIONS like '%区域ID%'\G select * from dts_region_info where region = '区域ID'\G
```

灾备管理中心

**手动配置本端DTS**

**说明**

如果灾备端ASRDR容器无法访问生产端asrdr-backend申请的asrdr-backend-ops对应的VIP，建议手动配置本端DTS。
1. 将生产端asrdr容器里DTS的SQL模板/home/admin/asrdr/config/dts/dts_conf.{des_region}，拷贝到
灾备端端asrdr容器/home/admin/asrdr/config/dts/下。
2. 在灾备端容器内执行以下命令。

```bash
python alidata/bin/dts/dts_new/auto_config_dts.py manual -r {des_region}
# des_region目标region
```

灾备管理中心执行脚本时，会自动替换{current_region}，运行过程会输出实际执行的sql语句。
3. 在灾备端DTS数据库内执行以下命令，查看DTS数据库。

```
select * from region_pattern where pattern_expression = '^区域ID'\G select * from config where config_code = 'cross_cloud_internet_check_flag'; select * from region_list where REGIONS like '%区域ID%'\G select * from dts_region_info where region = '区域ID'\G
```

灾备管理中心

### 配置专线信息

配置专线信息需在部署ASR-DR运维平台时一并完成，若未配置，首页线形图将不能呈现数据。配置专线信息的具体步骤如下所示。 灾备管理中心
1. 下载脚本到本地并解压
2. 本地连接环境 VPN，连接步骤请参考 sgvpn 使用文档：sudo sgvpn con -e 128E -f。

**说明**

直接在环境中导入则无需连接VPN。
3. 配置 nrm_domain
i. 在任意门-环境元数据查询处，选择目标环境，在service搜索框输入 "baseService-network-base" 进行查询取值。数据库登 ii. 将上一步获取的nrm_domain的值替换到脚本中的domain.py中。 灾备管理中心
4. 导入DCI专线和互联专线数据。

**说明**

DCI专线数据以json格式写入Connections/DCInterConnections.json文件，互联专线数据以 json格式写入Connections/ExternalConnections.json文件。 DCI专线数据和互联专线数据都支持对象结构形式和数组形式。 具体的参数说明请参照AddDCInterConnection和AddExternalConnection。 灾备管理中心
5. 执行脚本python importConnections2db.py。
灾备管理中心 SR登录

#### AddDCInterConnection

**API描述**

调用该接口新增DCI专线实例。

**URL**

http://{nrm_endpoint}/nbs/api/AddDCInterConnection

**请求方式**

GET/POST

**Product**

Nbs

**Version**

2021-02-19

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 | 备注 |
|---|---|---|---|---|---|
| Name | str | 是 | test | 名称 |  |
| ConnectTyp e | str | 是 | InterDo main | DCI专线的类型，包含同城 、域间两种类型， 对应同城容灾和多 region 场景 | InterDomain:域间专线 IntraDomain:同城容灾 |
| Region | str | 是 | cn- qingdao -env66- d01 | 专线接入设备所属 Region |  |

灾备管理中心

| Idc | str | 是 | amtest1 1 | 专线接入设备所在的机房 |  |
|---|---|---|---|---|---|
| LineOperato r | str | 否 | test | DCI专线运营商属性 |  |
| AccessDevi ceId | str | 是 | ASW-A3- 5- H09.AM TEST66 | 专线接入的边界网络设备 |  |
| PhysicalPort | str | 是 | Port-01 | 专线接入的物理接口 |  |
| PortType | str | 是 | test | 专线接入的物理接口类型 | 手动输入 |
| Bandwidth | Int | 否 | 10000 | 接入的带宽，单位M |  |
| ConnectMo de | str | 是 | DirectCo nnect | 标明专线两侧的互联类型，直连、经过防火墙 | DirectConnect:直连 Firewall:防火墙 |
| FwMode | str | 否 | CloudFir ewall | 使用防火墙的类型，包含云防火墙及用户防火墙两类 | 如防火墙为True，可根据需要补充填写防火墙类型 CloudFirewall:云防火墙 UserFirewall:用户防火墙 Other:其他 |
| FwName | str | 否 | test | 防火墙名称 | 如防火墙为True，可根据需要补充填写防火墙相关名称 |
| FwDesc | str | 否 | test | 防火墙备注 | 如防火墙为True，可根据需要补充填写防火墙相关备注 |
| PeerRegion | str | 否 | cn- qingdao -env- d02 | 对端 Region | 如 ConnectType 为 InterDomain（域间专线） 时需要填写对端 Region |
| PeerIdc | str | 否 | amtest6 6 | 对端设备机房 | 如 ConnectType 为 InterDomain（域间专线） 时需要填写对端机房 |

灾备管理中心

| PeerAccess DeviceId | str | 是 | CSW- VM-VPC- G1- 1.AMTES T66 | 对端设备 |  |
|---|---|---|---|---|---|
| PeerPhysica lPort | str | 是 | port 02 _ | 对端设备端口 |  |
| PeerPortTyp e | str | 是 | test | 对端设备端口类型 |  |
| LocalIp | str | 是 | 1.1.1.1/ 30 | 本端IP地址 | Route 模式，书写格式为IP/ 掩码，例如：1.1.X.X/30 |
| PeerIp | str | 是 | 2.2.2.2/ 30 | 对端IP地址 | Route 模式，书写格式为IP/ 掩码，例如：1.1.X.X/30 |
| ConnectStat us | int | 是 | 1 | 专线的启用状态 | 1:启用 0：禁用 |
| Description | str | 否 | xxxxxxx | 备注 | 用来记录一些非标信息 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | 请求ID |
| Success | bool | true/false | 正常响应标识 |
| Code | str | 0 | 自定义响应状态码 |
| Message | str | success | 提示信息 |

**示例**

**请求示例**

灾备管理中心

```
 http://127.0.0.1:5050/nbs/api/AddDCInterConnection?
Name=LIGANG_03&ConnectType=LocalCity&Region=cn-qingdao-env66d01&Idc=amtest11&LineOperator=china&AccessDeviceId=ASW-A3-5-H09.AMTEST66&PhysicalPort=Port- 04&PortType=unkown&Bandwidth=10000&ConnectMode=Firewall&FwMode=CloudFirewall&FwName=firewall- 01&FwDesc=test for firewall&PeerIdc=amtest66&PeerAccessDeviceId=CSW-VM-VPC-G1- 1.AMTEST66&PeerPhysicalPort=Port- 002&PeerPortType=unkown&LocalIp=1.1.X.X/30&PeerIp=2.2.2.2/30&ConnectStatus=1&Description=just for test!!!&PeerRegion=cn-qingdao-env-d02
```

**正常响应**

```json
 { "Code": "0", "Message": "success", "RequestId": "bc56d938-e1b7-412c-a665-ba9a6f4a3ef5",
"Success": true }
```

**无数据/操作失败**

```json
 { "Message": "no data/update/delete", "Code": "4002", "RequestId": "d006a01a-3d87-4971-
a3fc-bb4cb2823799", "Success": true }
```

**异常响应**

40x，50x

```json
 { "Code": "InternalError", "Message": "The request processing has failed: [Errno 32]
Broken pipe", "RequestId": "2554a594-41a2-4346-93ac-5ac179f8b70f", "Success": false, "cost": 1, "eagleEyeTraceId": "2554a594-41a2-4346-93ac-5ac179f8b70f", "errCode":
```

`"ASO_NETWORK_INTERNALERROR", "errMessage": "`程序处理异常，请检查后端服务`", "errTitle": "`程序处理异

```json
常", "requestURI": "/slalink/fulllink/classic/idcinfo/IDCList", "responseVersion": "v1", "serviceRole": "baseServiceAll.baseService-network-base.nrm#", "success": false }
```

**说明**

可根据响应中的 Success 为 true 还是 false 判断响应是否正常。 获取数据列表的 api，虽然 Success 为 true，但仍需要判断 Data 是否为空列表（数组）[] 再进行取值渲染。可判断 Code 是否等于“0”进行渲染数据，“0”代表正常返回列表数据，非“0”代表数据列表为空, 无 Data 字段。 由于 POP 不支持下载 API，导出或下载文件均需直接访问 API 的 url。

**错误码**

| HttpCode | 错误码 | 错误信息 |
|---|---|---|
| 40x | ParameterError | 参数格式错误 |
| 40x | MissingParameter | 参数缺失 |
| 500 | InternalError | 程序处理异常 |
| 400 | UniqueError | 条目重复 |
| 400 | DBError | 数据读写异常 |

灾备管理中心

| 400 | Existing | 数据已存在 |
|---|---|---|
| 400 | NotExisting | 数据不存在 |

#### AddExternalConnection

**API描述**

该接口用于新增互联专线实例。

**URL**

http://{nrm_endpoint}/nbs/api/AddDCInterConnection

**请求方式**

GET/POST

**Product**

Nbs

**Version**

2021-02-19

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 | 备注 | asrdr运维平台使用该接口补充说明 |
|---|---|---|---|---|---|---|
| Name | str | 是 | test | 名称 |  | （可自由命名) |
| ConnectT ype | str | 是 | toInternet | 互联专线的类型 | toIdc:至-IDC toInternet:至- 互联网 | 默认：Resilience |
| Region | str | 是 | cn- qingdao- env66-d01 | 专线接入设备所属 Region |  | 备机房reginId（若单机房，则主备信息一致） |
| Idc | str | 是 | amtest11 | 专线接入设备所在的机房 |  | 备机房idc信息（若单机房，则主备信息一致） |
| LineOpera tor | str | 否 | test | DCI专线运营商属性 |  | （可为空） |
| AccessDe viceId | str | 是 | ASW-A3-5- H09.AMTES T66 | 专线接入的边界网络设备 |  | 备机房边界网络设备（若单机房，则主备信息一致） |

灾备管理中心

| PhysicalP ort | str | 是 | Port-01 | 专线接入的物理接口 |  | 备机房端口（若单机房， 则主备信息一致） |
|---|---|---|---|---|---|---|
| PortType | str | 否 | test | 专线接入的物理接口类型 | 手动输入 | （可为空） |
| Bandwidt h | Int | 否 | 10000 | 接入的带宽， 单位M |  | （可为空） |
| ConnectM ode | str | 是 | DirectConn ect | 标明专线两侧的互联类型， 直连、经过防火墙 | DirectConnect :直连 Firewall:防火墙 | 默认：DirectConnect |
| FwMode | str | 否 | CloudFirew all | 使用防火墙的类型，包含云防火墙及用户防火墙两类 | 如防火墙为 True，可根据需要补充填写防火墙类型 CloudFirewall: 云防火墙 UserFirewall: 用户防火墙 Other:其他 | （可为空） |
| FwName | str | 否 | test | 防火墙名称 | 如防火墙为 True，可根据需要补充填写防火墙相关名称 | （可为空） |
| FwDesc | str | 否 | test | 防火墙备注 | 如防火墙为 True，可根据需要补充填写防火墙相关备注 | （可为空） |
| PeerRegio n | str | 否 | cn- qingdao- env-d02 | 对端 Region | 如 ConnectType 为 InterDomain（ 域间专线）时需要填写对端 Region | 主机房reginId（若单机房，则主备信息一致） |

灾备管理中心

| PeerIdc | str | 否 | amtest66 | 对端设备机房 | 如 ConnectType 为 InterDomain（ 域间专线）时需要填写对端机房 | 主机房id（若单机房，则主备信息一致） |
|---|---|---|---|---|---|---|
| PeerAcces sDeviceId | str | 是 | CSW-VM- VPC-G1- 1.AMTEST6 6 | 对端设备 |  | 主机房设备名称（若单机房，则主备信息一致） |
| PeerPhysi calPort | str | 是 | port 02 _ | 对端设备端口 |  | 主机房物理端口（若单机房，则主备信息一致） |
| PeerPortT ype | str | 否 | test | 对端设备端口类型 |  | （可为空） |
| LocalIp | str | 否 | 1.1.1.1/30 | 本端IP地址 | Route 模式，书写格式为IP/掩码，例如： 1.1.X.X/30 | （可随便填，注意格式） |
| PeerIp | str | 否 | 2.2.2.2/30 | 对端IP地址 | Route 模式，书写格式为IP/掩码，例如： 1.1.X.X/30 | （可随便填，注意格式） |
| ConnectSt atus | int | 是 | 1 | 专线的启用状态 | 1:启用 0：禁用 | 默认：1 |
| Descriptio n | str | 否 | xxxxxxx | 备注 | 用来记录一些非标信息 | （可为空） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | 请求ID |
| Success | bool | true/false | 正常响应标识 |

灾备管理中心

| Code | str | 0 | 自定义响应状态码 |
|---|---|---|---|
| Message | str | success | 提示信息 |

**示例**

**请求示例**

```
 http://127.0.0.1:5050/nbs/api/AddExternalConnection?
Name=LIGANG_01&ConnectType=toInternet&Region=cn-qingdao-envd01&Idc=amtest11&LineOperator=china&AccessDeviceId=ASW-A3-4-H09.AMTEST66&PhysicalPort=Port- 01&PortType=unkown&Bandwidth=10000&ConnectMode=Firewall&FwMode=CloudFirewall&FwName=firewall- 01&FwDesc=test for firewall&PeerAccessDeviceId=HSW-02&PeerPhysicalPort=Port- 002&PeerPortType=unkown&LocalIp=1.1.X.X/30&ConnectStatus=1&Description=just for test !!!
```

**正常响应**

```json
 {
 "Code": "0",
 "Message": "success",
 "RequestId": "bc56d938-e1b7-412c-a665-ba9a6f4a3ef5",
 "Success": true
 }
```

**无数据/操作失败**

```json
 {
 "Message": "no data/update/delete",
 "Code": "4002",
 "RequestId": "d006a01a-3d87-4971-a3fc-bb4cb2823799",
 "Success": true
 }
```

**异常响应**40x，50x

```json
 {
 "Code": "InternalError",
 "Message": "The request processing has failed: [Errno 32] Broken pipe",
 "RequestId": "2554a594-41a2-4346-93ac-5ac179f8b70f",
 "Success": false,
 "cost": 1,
 "eagleEyeTraceId": "2554a594-41a2-4346-93ac-5ac179f8b70f",
 "errCode": "ASO_NETWORK_INTERNALERROR",
```

`"errMessage": "`程序处理异常，请检查后端服务`",` `"errTitle": "`程序处理异常`",` 灾备管理中心

```json
 "requestURI": "/slalink/fulllink/classic/idcinfo/IDCList",
 "responseVersion": "v1",
 "serviceRole": "baseServiceAll.baseService-network-base.nrm#",
 "success": false
 }
```

**说明**

可根据响应中的 Success 为 true 还是 false 判断响应是否正常。 获取数据列表的 API，虽然 Success 为 true，但仍需要判断 Data 是否为空列表（数组）[] 再进行取值渲染。可判断 Code 是否等于“0”进行渲染数据，“0”代表正常返回列表数据，非“0”代表数据列表为空，无 Data 字段。 由于POP不支持下载api，导出或下载文件均需直接访问api的url。

**错误码**

| HttpCode | 错误码 | 错误信息 |
|---|---|---|
| 40x | ParameterError | 参数格式错误 |
| 40x | MissingParameter | 参数缺失 |
| 500 | InternalError | 程序处理异常 |
| 400 | UniqueError | 条目重复 |
| 400 | DBError | 数据读写异常 |
| 400 | Existing | 数据已存在 |
| 400 | NotExisting | 数据不存在 |
