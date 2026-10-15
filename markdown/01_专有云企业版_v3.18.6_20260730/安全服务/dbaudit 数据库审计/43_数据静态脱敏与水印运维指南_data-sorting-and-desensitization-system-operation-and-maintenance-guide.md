---
title: "数据库审计 数据静态脱敏与水印运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 20
source_pdf: "43_数据静态脱敏与水印运维指南_data-sorting-and-desensitization-system-operation-and-maintenance-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/dbaudit/zh/data-sorting-and-desensitization-system-operation-and-maintenance-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据库审计 数据静态脱敏与水印运维指南

述

## 运维概述

**目的**

本手册指导运维人员对Apsara Uni-manager运维控制台进行预防性地维护，确保数据库静态脱敏与水印系统稳定运行。运维人员可以根据本手册的指导，处理维护过程中发现的系统问题。如果根据本手册无法解决问题，请联系阿里云技术工程师处理。

**运维要求**

运维人员必须拥有IT行业技能，包括计算机网络知识、计算机操作知识、问题分析排查能力。 运维人员必须经过阿里云系统岗前培训，学习必要的阿里云系统知识，包括但不限于系统原理、组网、特性使用和维护工具的使用。

**重要**

在维护操作过程中，运维人员务必遵守操作规章，确保人身安全和系统安全。对用户数据严格保密，未经用户书面许可，禁止复制、传播用户数据。 检

## 日常巡检

### 登录Apsara Uni-manager运营控制

**台**

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击页面右上角的当前语言可以切换其它语言。 授权登录是第三方认证中配置了全局IdP设置才会显示，且“授权登录”名称用户可按需自定义。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。 检
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**管理员强制开启MFA后的首次登录**

a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。

**您已开启并绑定MFA**

输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《 Apsara Uni-manager运营控制台用户指南》的**管理多因素认** 证章节。

**相关操作**

**忘记密码**

1. 用户忘记登录密码时，单击密码输入框下方的**忘记密码**。
2. 在忘记密码页面，输入**账户名**、**邮箱**和验证码后，单击**确认**。

**说明**

账户名请输入当前账号的用户名，邮箱请输入注册账号的Email地址。 重置密码的链接将发至邮箱，进入链接后用户可输入新密码。

### 查看实例状态

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
检
2. 在顶部菜单栏，选择**安全** > **数据安全** > **数据静态脱敏与水印**。
3. 通过查看**状态**以及**高可用状态**，查看两大关键信息。
**状态**：实例当前运行状态。
**高可用状态**：高可用模式是否正常启用。

**异常处理原则**

若在状态查看中发现以下两类情况，需立即启动排查流程，避免问题扩大： 状态标识为**异常**。 状态长期显示**升级中**（如超过2小时未完成升级，即判定为异常）。

### 查看概况

**概述**

从宏观层面把控脱敏与水印模块的全量运行情况，核心按时间维度（支持按日、周、月、自定义周期）统计展示关键数据，具体包括数据源数量、已发现敏感类型、敏感表数量、敏感文件数、脱敏任务运行次数、已脱敏数据量及相关脱敏任务TOP排名。同时支持将统计结果导出为doc、PDF等格式，便于后续汇报归档。 建议重点聚焦**数据源分析**（核心关注数据源数量波动、敏感类型/表/文件分布）和**脱敏任务分析**（重点跟踪任务运行频次、脱敏数据量变化及运行状态），通过这两大维度精准掌握模块运行态势，快速定位全局层面的异常趋势。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**安全** > **数据安全** > **数据静态脱敏与水印**。
3. 定位到目标实例，在**操作**列单击**详情**。
检
4. 查看实例的**概况**。

### 查看任务

**概述**

查看任务状态与结果，需覆盖发现任务、脱敏任务、水印任务、溯源任务、匿名化任务、列加密任务六大类任务，重点核查三项核心维度，确保任务正常推进。 一是运行状态，确认是否存在异常报错、卡顿等问题。 二是任务进度，排查是否出现停滞不前、进度卡死的情况。 三是耗时时长，判断是否存在耗时过长（超出同类任务常规阈值）或过短（疑似未完整执行）的异常。 若发现上述任一问题，需立即查看任务详情，结合日志信息进一步分析确认原因，为后续问题排查和解决提供精准依据。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**安全** > **数据安全** > **数据静态脱敏与水印**。
3. 定位到目标实例，在**操作**列单击**详情**。
检
4. 分别在**数据发现**、**数据脱敏**、**数据溯源**、K**匿名隐私保护**、**列加密**页签，查看任务的运行状态等。
情

## 指标详情

**查看CMS监控大盘**

数据静态脱敏与水印产品已经对接CMS平台，登录产品-云监控，查看产品运行状态。
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **迁移与运维管理** > **云监控**。
3. 在左侧导航栏，选择**云资源监控** > **云产品监控**，搜索数据静态脱敏与水印产品。
4. 单击目标实例，查看产品的监控数据。
运维人员通过CMS平台可直观查看以下核心信息，实现对产品运行状态的全面把控。 实例使用情况：包括实例启用数量、各实例业务负载分布、使用频率等，精准掌握实例运行饱和度。 实例运行状态：同步展示各实例是否正常运行、有无异常告警等信息，与白屏页面状态核查形成互补。 资源使用状态：实时监控实例对应的服务器CPU、内存、磁盘空间等资源占用情况，提前预警资源不足等潜在风险。 警处理

## 核心告警处理

针对数据库静态脱敏与水印系统的核心告警主要包括：CPU、内存、磁盘水位超限的告警。当发生该类告警后应当迅速登录对应实例查看促发因素，必要时请联系阿里云技术支持同学。 ）

## 云盾ECS登录（yundun_vpc下部

**署的产品）**

**跳板机登录信息查询**

1. 确认部署形态：on Tianji 、on PaaS。

**3182以下版本：天基部署。**

进入**OPS1**机器通过以下命令获取oem数据库连接，进入oem数据库。

```bash
curl -s http://127.0.0.1:7070/api/v3/column/service.res.result|awk -F '": "' '/db_p assword/{print $2}'|awk -F'"' '/yundunoem/{s="mysql -h"$44" -u"$36" -p"$4" -D"$40" -P"$12;gsub("\\\\","",s);print s}'
```

**3182及以上版本：PAAS部署。**

进入**OPS1**机器通过以下命令获取oem数据库连接，进入oem数据库。

```
db_data=$(kubectl get secret yundunoem-minirds-secret -n yundun-basic -oyaml | grep db_ | grep -v f:db_); OLD_IFS="$IFS"; IFS=' '; db=(${db_data}); IFS="$OLD_IFS"; db_ host=$(echo ${db[1]}| base64 -d); db_name=$(echo ${db[3]}| base64 -d); db_password= $(echo ${db[5]}| base64 -d); db_port=$(echo ${db[7]}| base64 -d); db_user=$(echo ${ db[9]}| base64 -d); echo "mysql -u${db_user} -P${db_port} -h${db_host} -D${db_name} -p${db_password}"
```

2. 获取跳板机登录信息：VIP 、反向代理。
i. 执行以下SQL获取VIP（Yundun3.16.2SP023以下版本支持VIP方式登录）。

```
select name,instance_info from o_cluster_resource where cluster_id = (select id fro m o_cluster where name = 'yundun_vpc' and status in ('UPGRADE_SUCCESS','PRODUCE_SUCCESS')) and type in ('ALB','PASSWORD')\G
```

） ii. 执行以下SQL获取反向代理（推荐方式）。

```
select name,instance_info from o_cluster_resource where cluster_id = (select id fro m o_cluster where name = 'yundun_vpc' and status in ('UPGRADE_SUCCESS','PRODUCE_SUCCESS')) and type in ('REVERSE_VIP','PASSWORD')\G
```

3. 登录跳板机。

**on tianji**

进入oem容器。进入OPS1机器，使用以下命令进入yundunoem容器内。

```bash
hostname=$(curl -s localhost:7070/api/v3/column/c.id?c.project=yundun-advance | gre p Basic | awk -F '"' '{print $4}' | head -n 1) machine=$(curl -s "localhost:7070/api/v5/ListMachineSR?cluster=${hostname}" | /home /tops/bin/python -m json.tool | grep '"hostname":' | sort | uniq | grep -v vm | awk -F '"' '{print $4}' | head -n 1) ssh $machine containerId=$(docker ps --format "{{.ID}} {{.Names}}" | grep 'oem' | awk '{print $1 }') docker exec -it ${containerId} bash
```

进入跳板机。

```
ssh -p ${mappingPort} root@${mappingIp}
```

**on paas**

OPS1机器，使用以下命令进入yundunoem容器内。

```bash
kubectl exec -it yundun-oem-0 bash -n yundun-basic
```

进入跳板机。

```
ssh -p ${mappingPort} root@${mappingIp}
```

**数据库脱敏ECS信息查询**

在oem数据库，通过以下sql查询数据其中cluster_type值在新产品接入时需向相关人员获取，instance_id值一般会在页面中显示。如果想查询所有的产品，只需要去除instance_id查询条件即可。

```
SELECT name, instance_info AS info, TYPE FROM o_cluster_resource WHERE TYPE IN ('ECS', 'PASSWORD') AND NAME LIKE '%ecs%' AND cluster_id IN ( SELECT cluster_id FROM o_commodity_cluster WHERE instance_id = 'discoverymask-CU9KdFfwv2eaflsfYs') \G
```

） 查询出数据如下，其中privateIpAddress值为ecs的ip，password为ecs的密码。

**ecs密码解密**

3181版本ECS增加了密码加密，需要解密。 解密ecs密码方法，进入到oem容器的 `/home/admin/yundun-csm-private/` 目录下，执行以下命令。
#将'${xxxx}'用实际密码替换

```
java -Dfile.encoding=utf-8 -jar yundun-csm-client-1.0.1.jar $(echo $(env | grep csm_ima ge_secretKey) |awk -F '=' '{print $2}') decryptPassword '{"password":"${xxxx}"}'
```

#示例

```
java -Dfile.encoding=utf-8 -jar yundun-csm-client-1.0.1.jar $(echo $(env | grep csm_ima ge_secretKey) |awk -F '=' '{print $2}') decryptPassword '{"password":"xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxx"}'
```

#3.18.3以上版本使用以下方法解密。

```
java -Dfile.encoding=utf-8 -jar yundun-csm-client-1.0.1.jar $(echo $(env | grep csm_ima ge_secretKey) |awk -F '=' '{print $2}') Password/decryptPassword '{"password":"xxxxxx"}'
```

题排查

## 常见问题排查

### 云盾控制台创建或升级失败

按以下逻辑分层排查，精准定位故障根因。
1. 核查产品镜像部署/升级状态优先判断产品镜像是否已完整完成部署或升级动作，未完成则将此环节作为
排查核心前置，重点确认镜像拉取、部署进度及是否存在资源冲突等问题。
2. 若镜像部署/升级已完成，进入下一步核查。
3. 核查核心进程启动状态重点检查Java进程及DC进程是否成功启动，进程未启动是该故障的高频原因。
镜像成功部署的前提下进行系统自检，200表示成功。

```bash
curl -k 'https://127.0.0.1:443/user/getSystemStatus.action'
```

4. 若进程未启动，需通过日志排查启动失败原因（如配置错误、依赖缺失、权限不足等）。

**警告**

日志详情查看需提前登录云原生产品对应的ECS实例，操作前请确认具备对应实例的登录权限，同时做好操作记录，避免影响其他业务运行。

### 数据源问题

#### 数据源测试连接失败

检查静脱设备配置的数据库连接信息是否正确，找客户确认客户提供的数据库连接信息是否正确。 检查静脱设备到数据库服务器的网络是否畅通，比如进入脱敏系统后台使用ping和nc命令验证。 检查数据库版本静脱是否支持、数据库本身服务是否正常是否有登录限制，可以用其他设备配置静脱产品的IP地址，然后使用第三方客户端工具通过jdbc尝试连接数据库。

#### 文件源创建失败

检查 `/dbfw_dc` 是否有足够剩余磁盘空间。 检查 / 是否有足够剩余磁盘空间。

#### 远程文件源测试连接失败

检查静脱设备配置的ftp连接信息，尤其是路径信息是否正确。 检查静脱设备到ftp服务器的网络是否畅通，比如进入脱敏系统后台使用ping和nc命令验证。 检查ftp设备服务是否正常，可以使用其他设备通过第三方工具尝试登录ftp服务。

#### 案例：测试连接报错socket read timeout

**问题描述**

题排查连接oracle时报错socket read timeout。

**问题原因**

连接的数据库是Oracle的rac，客户提供的连接IP没有提供oracle服务。

**解决办法**

客户重新提供IP后连接成功。

### 发现任务问题

#### 发现任务有表失败

查看发现任务日志 `/dbfw_bkup/tasklog/DISCOVER_TASK_*.log` 中报错信息。 检查数据库用户权限是否足够。 检查数据库服务是否正常，可以直接连接数据库进行select操作进行验证。

#### 发现结果不准确

查看发现任务日志 `/dbfw_bkup/tasklog/DISCOVER_TASK_*.log` 中的发现规则命中比例，然后前台页面检查发现规则的确认比例设置。 前台页面查看数据样本。 使用数据库客户端工具直接查看源库数据。

#### 发现任务卡死

查看发现任务日志 `/dbfw_bkup/tasklog/DISCOVER_TASK_*.log` ，确定卡在哪个阶段或哪张表。 如发现任务卡在某张表，连接源库查看表状态是否正常、是否有锁表、能否正常查询。 获取java进程的jstack信息，过几分钟再获取一次，将两次的jstack信息发给阿里云技术支持同学。

#### 案例：创建发现任务时schema下看到的表少于源

**库实际的表**

**问题描述**

某客户现场反馈Oracle的源库有590张表，但是创建发现任务时只能看到578张表。

**问题原因**

经检查，另外12张表是临时表，临时表不执行脱敏，所以创建发现任务时临时表会被过滤掉。

**解决办法**

产品机制，可直接向客户解释。 可以用 `select temporary,count(*) from user_tables group by temporary` 语句在源库查询表是否为临时表，如下图，temporary为Y的是临时表，为N的不是临时表，在创建发现任务时只能看到 temporary属性为N的表。 题排查

### 脱敏任务问题

#### 字段脱敏异常

查看脱敏任务日志 `/dbfw_bkup/tasklog/MASK_TASK_*.log` 中报错信息。 获取日志中报错数据，通过静脱前台脱敏算法页面进行脱敏验证。 直连源库查看是否有脏数据。 检查脱敏算法及参数配置是否正确。

#### 数据入库异常

查看脱敏任务日志 `/dbfw_bkup/tasklog/MASK_TASK_*.log` 中报错信息。 查看源库和目标库表结构是否一致。 查看是否有超长或违反主外键约束、唯一约束情况。 查看目标库数据库空间是否已满。 查看目标库数据库服务是否正常。

#### 脱敏性能极慢

检查是否有大量脱敏异常。 检查静脱系统资源使用情况，是否压力很大。 检查源库、目标库资源使用情况，是否压力很大。

#### 脱敏任务有表失败

查看脱敏任务日志 `/dbfw_bkup/tasklog/MASK_TASK_*.log` 中报错信息。 查看源库、目标库服务是否正常，脱敏任务失败的时间点是否有报错记录。 查看失败的表在源库是否正常，查看目标库是否存在对应schema。

#### 表初始化失败

查看脱敏任务日志 `/dbfw_bkup/tasklog/MASK_TASK_*.log` 中报错信息。 检查目标库是否有同名对象占用表名。 检查脱敏表是否有主外键关联，且关联表不在脱敏任务中。 查看后台库privicy_table_info中该表ddl是否正确，可将ddl在目标库验证是否能正常执行。 题排查

#### 对象迁移失败

查看脱敏任务日志 `/dbfw_bkup/tasklog/MASK_TASK_*.log` 中报错信息。 查看后台库table_object中该对象的ddl是否正确，可将ddl在目标库验证是否能正常执行。

#### 脱敏任务卡死

查看脱敏任务日志 `/dbfw_bkup/tasklog/MASK_TASK_*.log` ，确定卡在哪个阶段或哪张表。 如发现脱敏任务卡在某张表，连接源库和目标库查看表状态是否正常是否有锁表，能否正常查询。 获取java进程的jstack信息，过几分钟再获取一次，将两次的jstack信息发给阿里云技术支持同学。

#### 案例：脱敏后不脱敏的字段入库时报错字段超长

**问题描述**

执行oracle库到库脱敏任务时，有一不脱敏的列，类型为char(5)，但是入库时报超长。

**问题原因**

检查字符集发现源oracle库字符集为gbk，目标oracle库的字符集是utf-8，该列数据是一个汉字后面加3个空格，汉字在gbk字符集中存储长度为2，在utf8中变成3，导致超长（例如男字在gbk中存储为C4D0，在 utf8中变成E794B7）。

**解决办法**

脱敏目标库改为GBK字符集的数据库。
