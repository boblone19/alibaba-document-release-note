---
title: "灾备管理平台 同城容灾管理平台ASR 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 92
source_pdf: "05_同城容灾管理平台ASR 运维指南_local-disaster-recovery-o-m-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asr/zh/local-disaster-recovery-o-m-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 灾备管理平台 同城容灾管理平台ASR 运维指南

灾备管理中心

## 概述

### 运维简介

同城容灾管理平台ASR（Apsara Stack Resilience）是一款专注于混合容灾备份与恢复的云平台产品，可用于保障企业的数据安全和业务连续性。本文介绍同城容灾管理平台运维的目的、要求、注意事项和寻求帮助的途径。

**目的**

本手册主要指导维护人员同城容灾管理平台ASR进行预防性的维护，确保系统长期稳定运行。维护人员可以根据本手册的指导，处理维护过程中发现的系统问题。如果根据本手册无法解决系统问题，请寻求阿里云工程师的技术支持。

**要求**

运维人员必须拥有IT行业技能，包括计算机网络知识、计算机操作知识、问题分析排查能力。 运维人员必须经过阿里云系统岗前培训，具备必要的阿里云系统知识，包括但不限于系统原理、组网、特性使用和维护工具的使用。

**重要**

在维护操作过程中，运维人员务必遵守操作规章，确保人身安全和系统安全。对用户数据严格保密，未经用户书面许可，禁止复制、传播用户数据。

**注意事项**

为了系统的稳定运行，避免意外事故的发生，运维人员需要遵循以下事项： 分层分权管理对网络、设备、系统、数据实行分层分权管理，相应业务的运维人员仅拥有完成自身角色任务相对应的权限，防止越权操作而引起系统故障。 系统安全在对系统进行任何操作前，需要清楚地了解操作的结果，避免危险操作影响系统运行。 在操作过程中遇到的问题，需要清楚记录，以便问题排查和故障处理。 人身和数据安全操作电气设备时，必须根据设备要求做好安全措施。 需使用安全的设备接入业务网络。 未经授权，严禁对数据进行复制和传播。

**寻求帮助**

运维人员在系统维护过程中，如果需要相关帮助，请联系阿里云技术支持。

### 运维架构

本文介绍同城容灾管理平台ASR相关运维操作概况。 灾备管理中心同城容灾管理平台ASR运维操作主要包括： 平台监控：提供产品监控和同步监控功能。 产品监控：支持监控云产品或者组件在主备机房的运行状态、告警情况以及有哪些产品是双活。 同步监控：查看RDS、OSS、Tablestore的数据同步延迟满足度、同步正常实例数、同步异常实例数，以及各实例的同步延迟时间等。 平台检查：提供环境检查和产品检查功能。 环境检查：检查项包括是否做A'、集群部署、产品版本、产品基线、DNS资源、VIP资源、数据库资源、机房间网络情况、BGP路由，查看各检查项是否满足容灾的条件。

### 角色列表

本文描述同城容灾管理平台ASR不同角色支持的运维操作。

| 登录方式 |  | 容灾场景登录 |  |  | 日常场景登录 |  |
|---|---|---|---|---|---|---|
| 角色 |  | 高级运维 | 普通运维 | 访客 | 系统管理员 | 产品运维员 |
| 主机房 | 查看告警 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 |
|  | 产品监控 | 支持 | 支持 | 支持 | 支持 | 支持 |
|  | 同步监控 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 |
|  | > 文档版本：2026072 |  |  |  |  |  |

| 灾备管理中心 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 环境检查 | 支持 | 支持 | 支持 | 支持 | 支持 |
|  | 产品检查 | 支持 | 支持 | 支持 | 支持 | 支持 |
| 备机房 | 查看告警 | 支持 | 支持 | 支持 | 支持 | 支持 |
|  | 产品监控 | 支持 | 支持 | 支持 | 支持 | 支持 |
|  | 同步监控 | 支持 | 支持 | 支持 | 支持 | 支持 |
|  | 环境检查 | 支持 | 支持 | 支持 | 支持 | 支持 |
|  | 产品检查 | 支持 | 支持 | 支持 | 支持 | 支持 |

灾备管理中心运维操作

## ASR平台运维操作

### 快速入门

#### 登录ASR控制台

同城容灾管理平台ASR针对日常运维、容灾逃逸和租户运营场景提供了三种登录方式。

**说明**

后续文档中同城容灾管理平台ASR简称ASR控制台。

**前提条件**

使用统一运维平台登录时，您已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为<region-id>.console.<intranet-domain-id>。 使用容灾逃逸登录时，您已从部署人员或管理员处获取ASR的访问地址、用户名和密码。

**说明**

主机房故障时需登录备机房ASR，备机房故障登录主机房ASR，两者域名不同。 ASR备机房的访问地址格式为asr-xs-<region-id>.console.<intranet-domainid>/user/login。 ASR主机房的访问地址格式为asr-xm-<region-id>.console.<intranet-domainid>/user/login。 使用租户运营场景登录时，您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。

**统一运维平台登录**

**说明**

根据Apsara Uni-manager运维控制台为同城容灾配置的不同权限，登录同城容灾管理平台后所呈现的视图将会有所差异（如果登录用户具有多个权限时，则展现的菜单项是所有角色权限的合集）。具体如下： Apsara Uni-manager运维控制台为同城容灾用户仅配置容灾监控权限时，展示运维态监控中心菜单项、日常态平台监控和概览菜单项。 Apsara Uni-manager运维控制台为同城容灾用户仅配置容灾演练权限时，展示日常态视图菜单项和运维态监控中心菜单项。 Apsara Uni-manager运维控制台为同城容灾用户仅配置容灾运维权限时，只展示运维态视图功能模块，且无法切换至日常态视图。 Apsara Uni-manager运维控制台为同城容灾用户同时配置容灾监控和容灾运维，或配置系统管理员权限时，将展示日常态和运维态的功能，并支持两者之间进行切换。
1. 打开浏览器。
2. 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址，按回车键。
灾备管理中心运维操作

**说明**

您可以单击右上角的当前语言切换其它语言。当前支持简体中文、English语言切换。
3. 输入正确的用户名及密码。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 若连续输入密码错误三次，系统将启动图片验证码登录功能；若连续输入错误五次，账户将被锁定，请联系管理员进行激活。 首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码必须满足以下要求： 必须包含英文大小写字母。 必须包含阿拉伯数字（0~9）。 必须包含特殊符号，包括感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等。 密码长度为10~20个字符。
4. 单击**账号登录**。
5. 在顶部菜单中选择**平台运维** > **容灾管理** > **同城容灾管理平台** **ASR** 。
灾备管理中心运维操作
6. 单击左侧导航栏上方的
，可切换主/备机房。
7. （可选）单击左侧导航栏日常态/运维态，可切换至另一个视图页面。

**说明**

用户需具备容灾监控、容灾演练或系统管理员中任一权限，方可支持视图切换操作。

**容灾逃逸登录**

灾备管理中心运维操作

**重要**

容灾逃逸登录开关默认处于关闭状态。如需通过该方式进行登录，请提前启用该开关并设置登录密码， 具体请参见逃逸登录管理。
1. 在浏览器地址栏中，输入同城容灾管理平台ASR的访问地址，单击回车键。

**说明**

主机房故障时需登录备机房ASR，备机房故障登录主机房ASR，两者域名不同。 ASR备机房的访问地址格式为asr-xs-<region-id>.console.<intranet-domainid>/user/login。 ASR主机房的访问地址格式为asr-xm-<region-id>.console.<intranet-domainid>/user/login。

**说明**

您可以单击右上角的当前语言下拉切换语言，支持简体中文和English。
2. 输入正确的用户名和密码。

**说明**

登录ASR的用户名和密码请从部署人员或管理员处获取。
3. 单击**登录**。
灾备管理中心运维操作
4. 单击页面顶部日常态/运维态，可切换至另一个视图页面。
5. 单击页面顶部机房可跳转至相应机房页面。

**租户运营登录**

如果您需要按业务应用维度恢复单块业务与容灾演练，可通过登录Apsara Uni-manager运营控制台创建保护组。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
灾备管理中心运维操作

**说明**

单击页面右上角的当前语言可以切换其它语言。 授权登录是第三方认证中配置了全局IdP设置才会显示，且“授权登录”名称用户可按需自定义。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**管理员强制开启MFA后的首次登录**

a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。 灾备管理中心运维操作

**您已开启并绑定MFA**

输入6位MFA码后单击**认证**。

**说明**

绑定并开启MFA的操作请参见《 Apsara Uni-manager运营控制台用户指南》的**管理多因素认** 证章节。
5. 在顶部菜单中选择**产品**。
6. 在菜单中选择**容灾与备份**。
7. 在**容灾与备份**区域选择**容灾服务** > **同城容灾管理平台** **ASR** 。

#### 查看平台监控项

##### 产品监控

本文介绍产品监控的检查方法和期望结果。

**监控方法**

1. 登录同城容灾管理平台ASR（主机房）或同城容灾管理平台ASR（备机房），登录方法请参见登录ASR控
制台。
2. 在左侧导航栏中选择**平台监控** > **产品监控**。
3. 在**产品监控**页面，可以查看所有产品的**功能状态**、**主服务位置**、**巡检结果**等监控项信息，以及部分产品
的**容灾实例数**和容灾库存水位信息。

**说明**

查看监控项信息需要确保数据更新时间与实际查看时间一致。

**期望结果**

期望所有列无标红项。若存在异常，则需要根据错误信息排查解决问题，或提单联系阿里云技术支持修复。

##### 同步监控

本文介绍同步监控的检查方法和期望结果。

**监控方法**

1. 登录备机房ASR控制台。
2. 在左侧导航栏中选择**平台监控** > **同步监控**。
3. 在同步监控页面，可以查看RDS、Redis、PolarDB-X 2.0、MongoDB、AnalyticDB
PostgreSQL版、OSS、Hologres、Tablestore和PolarDB本地盘（Polar-M和Polar-PG）的数据同步延迟满足度、同步正常实例数、同步异常实例数，以及各实例的同步延迟时间等。对于同步异常的实例， 会以红色显示在实例列表顶端。

**说明**

查看监控项信息需要确保数据更新时间与实际查看时间一致。 灾备管理中心运维操作

**期望结果**

数据同步延迟满足度为100%。

**说明**

若不满足要求，则需要对标红的实例排查解决同步延迟问题，或提单联系阿里云技术支持修复。

### 核心告警处理

#### 告警项说明

| 告警项 | 告警说明 | 告警级别 | 告警详情 |
|---|---|---|---|
| inspect db resourc _ _ e | 元数据库的连接异常或读写状态是只读状态。 | P2 | 请参见inspect db resource。 _ _ |
| drei product _ | 检查核心底座云产品 DNS、SLB、MiniRDS 的容灾切换能力。 | P2 | 请参见drei product。 _ |
| rpo check _ | RDS或OSS同步延迟时间超过阈值或同步中断。 | P2 | 告警产品为RDS，请参见rpo check（RDS）。 _ 告警产品为OSS，请参见rpo check（OSS）。 _ |
| sync check _ | 云产品容灾巡检异常。 | P2 | 告警产品为MiddleWareAll，请参见sync check（MiddleWareAll）。 _ 告警产品为minirds-mt/rds，请参见sync check（minirds-mt/rds）。 _ 告警产品为 TableStore/TableStoreInner，请参见sync check（TableStore/TableStore _ Inner）。 告警产品为SLB，sync check（SLB）。 _ 告警产品为Kafka，请参见sync check（Kafka）。 _ 告警产品为Elasticsearch，请参见sync check（Elasticsearch）。 _ |
| inspect product cl _ _ uster aplus _ | 云产品集群未做A'。 | P2 | 请参见inspect product cluster aplus。 _ _ _ |
| inspect product cl _ _ uster version _ | 主备机房产品版本不一致。 | P2 | 请参见inspect product cluster version。 _ _ _ |

灾备管理中心运维操作

| inspect product va _ _ riable | 产品基线变量检查未通过。 | P2 | 请参见inspect product variable。 _ _ |
|---|---|---|---|
| inspect product cl _ _ uster deploy _ | 存在非对等部署的云产品。 | P2 | 请参见inspect product cluster deploy。 _ _ _ |

#### inspect_db_resource

此告警点主要检测元数据库连接情况或者元数据库的读写状态，出现此告警表示元数据库连接失败或者元数据库状态为只读状态，可能会导致数据无法写入，影响依赖产品的正常运行。

**告警属性**

| 告警ID | 监控项 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| inspect d _ b resour _ ce | inspect d _ b resour _ ce | Bcmc# | P2 | bcmc | 实例主库状态或读写状态异常 | 每30分钟执行一次 |

**适用版本**

适用于专有云企业版v3.14及后续版本。

**告警原因**

实例状态异常。 实例读写状态异常。

**告警影响**

可能会导致数据无法写入，影响依赖产品的正常运行。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。
1. 登录飞天基础运维平台。
2. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。
3. 在产品列表中查询bcmc，在主集群**操作**列单击**集群详情**。
4. 在服务列表中单击**bcmc**服务名称。
5. 选择**Bcmc#**组件。
6. 切换至**资源列表**页签，找到**名称**和**类型**分别为**asr**和**db**的资源，在其**资源申请结果**列中查看db_host、
user、db_password、db_port、db_name的取值。
7. 登录上报告警所在机器。
8. 执行如下命令，检查数据库是否可以正常连接。
灾备管理中心运维操作

**说明**

请在环境内有MySQL客户端的地方执行登录数据库命令。

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

系统显示如下类似结果，表示连接正常，请根据实际情况确认。

**说明**

如果数据库连接失败，请联系RDS产研团队处理。
9. 执行如下SQL语句，查看数据库读写状态。

```
show global variables like "read_only";
```

系统显示如下类似结果，请根据实际情况确认。 如果**read_only**显示**ON**，表示状态只读，需要修改只读状态。 执行如下SQL语句，修改只读状态。

```
set global read_only = 0;
```

0. 根据告警信息获取异常实例名称。
1. 登录杜康数据库管理平台。
2. 查看实例详细报错信息，如果是实例未启动连接失败，需要重启实例。
i. 进入告警实例所在主机。 灾备管理中心运维操作 ii. 执行如下命令，查看并记录启动异常实例的命令。

```
cat /etc/init.d/mysql | grep ${端口号}
```

系统显示如下类似结果，请根据实际情况确认。 iii. 执行如下命令，启动异常实例。

```
/u01/mysql56/bin/mysqld_safe --defaults-file=/etc/my${端口号}.cnf &
```

iv. 执行如下命令，并查看实例是否启动成功。 ps aux|grep ${端口号} 系统显示如下类似结果，请根据实际情况确认。

**说明**

如果实例启动失败，请联系RDS产研团队处理。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

#### drei_product

此告警点主要检测minirds实例是否可切换、实例主备同步是否有延迟，是否存在单可用区实例、minirds 集群中serviceTest#的状态。出现此告警表示存在以上任意一个以及多个情况。

**告警属性**

| 告警ID | 监控项 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|

灾备管理中心运维操作

| drei prod _ uct | drei prod _ uct | Bcmc# | P2 | minirds- mt | 触发条件有多种，例如： 实例连接失败。 主备同步延迟。 单可用区存在实例。 备机房存在实例。 minirds集群中 serviceTest#未达终态。 | 每30分钟执行一次 |
|---|---|---|---|---|---|---|

**适用版本**

适用于专有云企业版v3版本。

**告警原因**

触发该告警的原因有很多种，例如： 实例连接失败。 主备同步延迟。 单可用区存在实例。 备机房存在实例。

**告警影响**

由于存在多种告警原因，所以告警影响也不尽相同，例如： 主备同步延迟，在主备同步延迟很大的情况下，如果主机房挂掉，会有数据丢失的风险。 minirds集群中serviceTest#未达终态，可能会导致集群中的功能以及业务受到影响。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**备机房存在实例处理方法**

如果备机房存在实例，这种一般不用处理，实例会自动做可用区对齐，自动切回到主机房。

**单可用区存在实例处理方法**

如果有单可用区实例，需要进行实例的单变双操作。
1. 登录主机房的minirds-integrator.RebuildSlave容器。
2. 进入该容器执行如下命令，将conf.yml.j2文件复制到指定目录。

```bash
docker cp conf.yml.j2 ${容器ID}:/meta/usr/local/rds/rebuild/conf.yml.j2
```

灾备管理中心运维操作 conf.yml.j2配置文件如下：

```bash
# conf.yml.j2
db:
  host: {{db_dbaas_host}}
  port: {{db_dbaas_port}}
  user_name: {{db_dbaas_user}}
  password: {{db_dbaas_password}}
  db_name: {{db_dbaas_name}}
cluster:
  cluster_name: {{CLUSTER_NAME}}
  db_type: {{DB_TYPE}}
  db_version: {{DB_VERSION}}
  site_name: {{SITE_NAME}}
  ips: ""
```

`max_tasks: 10 #`并行的任务数 `ins_names: "" #`需要重搭的实例名逗号分隔必需指定不然不工作

```
api:
  rdsapi: {{RDS_API_URL}}
timeout: {{TIMEOUT}}
```

3. 联系阿里云技术支持获取rebuild文件并解压，将所有文件复制到RebuildSlave容器。

```bash
docker cp ${rebuild文件名}:/usr/local/rds/rebuild/
```

4. 复制完成后，执行如下命令，重启RebuildSlave容器。

```bash
docker stop ${容器ID} docker start ${容器ID}
```

**不可切换实例、主备同步延迟、实例连接失败处理方法**

1. 根据告警信息获取异常实例名称。
2. 登录杜康数据库管理平台。
3. 查看实例详细报错信息。
ii. 如果是主备同步延迟，请参见备库重搭进行处理。 iii. 如果是不可切换实例，请参见备库重搭进行处理。
1. 登录飞天基础运维平台。
2. 在**产品集群运维**中查看minirds-maotai集群中serviceTest#组件是否已达终态。
3. 如果serviceTest#组件未达终态，考虑通过重启解决。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

#### rpo_check

灾备管理中心运维操作

##### 概述

rpo_check告警主要用于检测RDS或OSS的同步延迟状态，当同步延迟时间超过阈值或同步中断时出现该告警，不同产品出现该告警的处理方式不同。

##### rpo_check（RDS）

此告警点主要检测RDS容灾实例的同步延迟状态，出现此告警表示RDS的同步延迟时间超过阈值或同步中断，可能会导致数据丢失或容灾切换失败。本文档主要描述告警产品为RDS时的rpo_check告警项相关信息。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| rpo check _ | rpo check _ | Bcmc# | P2 | RDS | RDS容灾实例的同步延迟超过用户设定的阈值，或同步延迟中断 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.12及后续版本。

**告警原因**

当dr_service检查RDS产品实例同步延迟时，出现连接异常或执行SQL报错，RPO缺省值为负数，具体原因请参见下表。

| 引擎 | 缺省值 | 原因 |
|---|---|---|
| mysql | -1 | slave连接失败。 执行sql报错。 Seconds Behind Master值为null。 _ _ |
| pgsql | -1/-2 | 连接dbaas执行sql报错。 获取aurora的账号信息失败。 从库连接失败/不可用。 pglog diff为null。 _ |
| mongo | -2 | 主备库连接失败/不可用。 |

灾备管理中心运维操作

| redis | -1/-2 | 执行sql报错。 slave连不上。 |
|---|---|---|

**告警影响**

同步延迟监控状态异常，可能会导致： 同步延迟过高，主节点故障时可能会导致数据丢失过多。 备实例访问不通，容灾切换失败，或切换后实例无法使用。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 在**杜康数据库管理平台**左侧导航栏中，选择**系统管理**> **容灾管理**> **容灾切换**。
4. 在**容灾切换**页面查看异常详情，并联系RDS运维人员修复异常项。
如果实例未启动，需要重启实例。 a. 进入告警实例主节点所在主机。

**说明**

以下步骤以mysql实例异常为例。 b. 执行如下命令，如果未能找到实例进程，则说明实例未启动。

```
ps aux | grep ${端口号}
```

c. 执行如下命令，查看并记录启动异常实例的命令。

```
cat /etc/init.d/mysql | grep ${端口号}
```

系统显示如下类似结果，请根据实际情况确认。 灾备管理中心运维操作 d. 执行如下命令，启动异常实例。

```
/u01/mysql56/bin/mysqld_safe --defaults-file=/etc/my${端口号}.cnf &
```

e. 执行如下命令，并查看实例是否启动成功。 ps aux|grep ${端口号} 系统显示如下类似结果，请根据实际情况确认。

**说明**

如果实例启动失败或其他异常情况，请联系RDS运维人员处理。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

##### rpo_check（OSS）

此告警点主要检测OSS容灾实例的同步延迟状态，出现此告警表示OSS的同步延迟时间超过阈值或同步中断，可能会导致数据丢失或容灾切换失败。本文档主要描述告警产品为OSS时的rpo_check告警项相关信息。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| rpo check _ | rpo check _ | Bcmc# | P2 | OSS | OSS容灾实例的同步延迟超过用户设定的阈值，或同步延迟中断 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.12及后续版本。

**告警原因**

QPS过高、消息堆积。

**告警影响**

同步延迟监控状态异常，可能会导致： 同步延迟过高，主节点故障时可能会导致数据丢失过多。 备实例访问不通，容灾切换失败，或切换后实例无法使用。 灾备管理中心运维操作

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。
1. 检查同步边是否打开。
i. 登录飞天基础运维平台。 ii. 在**飞天基础运维平台**页面的左侧导航栏中，选择**产品集群运维**。 iii. 在产品列表中查询oss，在集群**操作**列单击**集群详情**。 iv. 在**服务列表**页面，单击**oss-ocm-server**服务。 v. 选择**OcmServer#**组件。 vi. 在机器列表中，单击实例**操作**列的**Terminal**，登录oss-ocm-server.OcmServer#终端机器。

```
vii. 进入 /cloud/app/oss-ocm-server/OcmServer#/ocm_server/current 目录。
```

viii. 执行如下命令获取OCM_CMD的accessID和accessKey。

```
cat ocm_conf.json | grep -A 10 "accessID"
```

ix. 执行如下命令获取master_ocm_host。

```
cat ocm_conf.json | grep master_ocm_host
```

x. 执行如下配置命令，其中accessID、accessKey和master_ocm_host为上述步骤获取的值。

```
./ocm_cmd config --id=${accessID} --key=${accessKey} --host ${master_ocm_host}
```

xi. 执行如下命令，检查<BucketSyncMeta>标签下的内容符合预期。

```
./ocm_cmd gbm bucketName
```

**说明**

检查项及预期： a. 同步边是否存在：存在<BucketSyncMeta>标签说明同步边存在。 b. 同步方向是否符合预期：<BucketSyncMeta>标签下，存在<SrcBucket>、 <SrcLocation>、<DestBucket>、<DestLocation>标签，并且符合预期： a. <SrcBucket>、<SrcLocation>的值分别与<BucketMeta>标签下<Name>、 <Location>标签值一致。 b. <DestBucket>、<DestLocation>的值与对端机房信息一致。 c. 同步状态是否正常：<BucketSyncMeta>标签下，<SyncStatus>标签值为0或1。 执行结果示例如下。 灾备管理中心运维操作

```xml
<?xml version="1.0" encoding="UTF-8"?> <BucketMeta>
  <Name>wd-test</Name>
  <Owner>1276207919333070</Owner>
  <Application>file</Application>
  <Location>oss-cn-qingdao-env9b-amtest52002-b</Location>
  <CreateTime>Thu, 17 Dec 2020 06:09:29 GMT</CreateTime>
  <CacheTime>1608534489</CacheTime>
  <Comment></Comment>
  <Acl>public-read-write</Acl>
  <BucketStatus>ok</BucketStatus>
  <BucketMode>default</BucketMode>
  <RequestPayer>BucketOwner</RequestPayer>
  <BucketPolicy>
    <LogBucket></LogBucket>
    <LogPrefix></LogPrefix>
    <Location>oss-cn-qingdao-env9b-amtest52002-b</Location>
    <DisallowEmptyRefer>false</DisallowEmptyRefer>
    <WhiteReferrerList />
    <CommonHeaderList />
    <AccessAllowedTypeList />
    <MimeTypeConfig>
      <MimeTypeRules />
    </MimeTypeConfig>
    <BucketChargeType>
      <FlowChargeType>PayByTraffic</FlowChargeType>
    </BucketChargeType>
    <CacheControlConfiguration />
    <MaxImageSize>-1</MaxImageSize>
    <UrlRewriteScript></UrlRewriteScript>
    <CompatMask>4</CompatMask>
    <TransferAccType></TransferAccType>
    <SourceProtectSuffix>*</SourceProtectSuffix>
    <IAMPolicy></IAMPolicy>
    <EnableDualCluster>false</EnableDualCluster>
    <IndexFile></IndexFile>
    <ErrorFile></ErrorFile>
    <SysObjectTagsStr></SysObjectTagsStr>
    <DataRedundancyType>0</DataRedundancyType>
    <ObjectHashFunction>NULL</ObjectHashFunction>
    <ObjectOverwriteCond>ALL</ObjectOverwriteCond>
    <AuthorizationConfiguration />
  </BucketPolicy>
  <CORSConfiguration />
  <BucketFlowLimits>
    <MaxQps>-1</MaxQps>
    <MaxSendFlow>-1</MaxSendFlow>
    <MaxRecvFlow>-1</MaxRecvFlow>
    <MaxIntranetQps>-1</MaxIntranetQps>
    <MaxIntranetSendFlow>-1</MaxIntranetSendFlow>
    <MaxIntranetRecvFlow>-1</MaxIntranetRecvFlow>
    <MaxTotalQps>-1</MaxTotalQps>
    <MaxIntranetTotalQps>-1</MaxIntranetTotalQps>
  </BucketFlowLimits>
```

灾备管理中心运维操作

```xml
  <BucketUserQos>
    <MaxHourExtranetSendFlow>-1</MaxHourExtranetSendFlow>
    <MaxDayExtranetSendFlow>-1</MaxDayExtranetSendFlow>
    <MaxHourIntranetSendFlow>-1</MaxHourIntranetSendFlow>
    <MaxDayIntranetSendFlow>-1</MaxDayIntranetSendFlow>
    <StorageCapacity>1073741824</StorageCapacity>
  </BucketUserQos>
  <BID>26842</BID>
  <StorageType>standard</StorageType>
  <DualClusterStatus>1</DualClusterStatus>
  <BucketSyncMeta>
    <SyncStatus>1</SyncStatus>
    <SyncSubStatus>0</SyncSubStatus>
    <SyncHistoryStatus>1024</SyncHistoryStatus>
    <SyncAcl>0</SyncAcl>
    <SyncBackupStatus>0</SyncBackupStatus>
    <CreateTime>1608189511</CreateTime>
    <ModifyTime>1608189637</ModifyTime>
    <SrcBucket>wd-test</SrcBucket>
    <SrcLocation>oss-cn-qingdao-env9b-amtest52002-b</SrcLocation>
    <DestBucket>wd-test</DestBucket>
    <DestLocation>oss-cn-qingdao-env9b-d01-a</DestLocation>
    <HistoryCpt></HistoryCpt>
    <HistoryMpartKeyCpt></HistoryMpartKeyCpt>
    <HistoryUploadIdCpt></HistoryUploadIdCpt>
    <HistoryObjectSyncEnabled>true</HistoryObjectSyncEnabled>
    <Type>0</Type>
    <TransferType>0</TransferType>
    <VipProxy></VipProxy>
    <Speed>0</Speed>
    <ScanType>1</ScanType>
    <SubNum>0</SubNum>
    <ScheduleType>0</ScheduleType>
    <ScheduleBandwidth>0</ScheduleBandwidth>
    <RuleId></RuleId>
    <Version>5c665d30e017456e840fa11358f9ff97</Version>
    <NeedPartitionList>false</NeedPartitionList>
    <IsQpsTask>false</IsQpsTask>
    <IgnoreNewFileForHistory>true</IgnoreNewFileForHistory>
  </BucketSyncMeta>
  <BucketSyncMeta>
    <SyncStatus>4</SyncStatus>
    <SyncSubStatus>1</SyncSubStatus>
    <SyncHistoryStatus>768</SyncHistoryStatus>
    <SyncAcl>0</SyncAcl>
    <SyncBackupStatus>0</SyncBackupStatus>
    <CreateTime>1608185369</CreateTime>
    <ModifyTime>1608190889</ModifyTime>
    <SrcBucket>wd-test</SrcBucket>
    <SrcLocation>oss-cn-qingdao-env9b-d01-a</SrcLocation>
    <DestBucket>wd-test</DestBucket>
    <DestLocation>oss-cn-qingdao-env9b-amtest52002-b</DestLocation>
    <HistoryCpt></HistoryCpt>
    <HistoryMpartKeyCpt></HistoryMpartKeyCpt>
```

灾备管理中心运维操作

```xml
    <HistoryUploadIdCpt></HistoryUploadIdCpt>
    <HistoryObjectSyncEnabled>true</HistoryObjectSyncEnabled>
    <Type>0</Type>
    <TransferType>0</TransferType>
    <VipProxy></VipProxy>
    <Speed>0</Speed>
    <ScanType>1</ScanType>
    <SubNum>0</SubNum>
    <ScheduleType>0</ScheduleType>
    <ScheduleBandwidth>0</ScheduleBandwidth>
    <RuleId></RuleId>
    <Version>b6dbaeb845fb4c23bed94c5d717fa00e</Version>
    <NeedPartitionList>false</NeedPartitionList>
    <IsQpsTask>false</IsQpsTask>
    <IgnoreNewFileForHistory>true</IgnoreNewFileForHistory>
  </BucketSyncMeta>
  <BucketVpcipBindList />
  <Tagging>
    <TagSet />
  </Tagging>
</BucketMeta>
```

2. 检查OSS RPO值是否正常。
i. 登录飞天基础运维平台。 ii. 在**飞天基础运维平台**页面的左侧导航栏中，选择**产品集群运维**。 iii. 在产品列表中查询oss，在集群**操作**列单击**集群详情**。 iv. 在**服务列表**页面，单击**oss-chiji-agent**服务。 v. 选择**ChijiAgent#**组件。 vi. 在机器列表中，单击某台机器**操作**列中的**Terminal**，登录oss-chiji-agent.ChijiAgent#终端机器。 vii. 执行如下命令，计算OSS RPO的值。

```
/apsara/deploy/dsu GetSyncTaskProgress 源location#目标location#源bucket#目标bucket
```

**说明**

命令中的源location、目标location、源bucket、目标bucket需要替换为步骤1中 <SrcLocation>、<DestLocation>、<SrcBucket>、<DestBucket>标签的值。 执行结果中 `new file last sync time` 为最近一次文件同步时间，当前时间减去该值则为OSS RPO值。 若同步边正常，OSS RPO过大，常见原因是QPS过高、消息堆积造成，联系OSS运维人员处理。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

#### sync_check

灾备管理中心运维操作

##### 概述

sync_check告警主要用于检测容灾实例的容灾状态，当云产品容灾巡检异常时出现该告警，不同产品出现该告警的处理方式不同。 告警产品为MiddleWareAll，请参见sync_check（MiddleWareAll）。 告警产品为minirds-mt/rds，请参见sync_check（minirds-mt/rds）。 告警产品为TableStore/TableStoreInner，请参见sync_check（TableStore/TableStoreInner）。 告警产品为Elasticsearch，请参见sync_check（Elasticsearch）。

##### sync_check（MiddleWareAll）

此告警点主要检测MiddleWareAll容灾实例的容灾状态，出现此告警表示MiddleWareAll容灾巡检异常， 可能会导致容灾切换失败或依赖的云产品容灾能力异常。本文档主要描述告警产品为MiddleWareAll时的

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | middleWar eAll | ASR上 MiddleWar eAll容灾巡检异常 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.12及后续版本。

**告警原因**

MiddleWareAll中vipserver组件的distroThreshold阈值默认是0.7。 MiddleWareAll产品不到终态。

**告警影响**

MiddleWareAll容灾状态异常，可能会导致： 容灾切换失败。 依赖MiddleWareAll产品的云产品容灾能力异常。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**vipserver组件的distroThreshold阈值配置错误的处理方法**

灾备管理中心运维操作
1. 登录middleWare-vipserver.Server#容器。
2. 执行如下命令查看distroThreshold的值，默认为0.7。

```bash
curl -s http://vipserver.tbsite.net/vipserver/api/switches | python -m json.tool
```

3. 执行如下命令修改distroThreshold值为0.45。

```json
curl-s"http://${diamond_host}/diamond-server/basestone.do?method=syncUpdateAll"-d 'da taId=com.taobao.vipserver.switches&group=VIPSERVER_GROUP&content= {"distroThreshold":0.45}'
```

**说明**

diamond_host查询方法： i. 登录飞天基础运维平台。 ii. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。 iii. 在产品列表中查询middleWareAll，在**操作**列单击**集群详情**。 iv. 在服务列表中单击**middleWare-diamond**服务名称。 v. 切换至**注册变量**页签中查询diamond_host取值。
4. 执行如下命令验证distroThreshold的值为0.45。

```bash
curl -s http://vipserver.tbsite.net/vipserver/api/switches | python -m json.tool
```

**MiddleWareAll产品不到终态的处理方法**

1. 登录飞天基础运维平台。
2. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。
3. 在产品列表中查询middleWareAll，在**操作**列单击**集群详情**。
4. 在服务列表中，单击未达终态的服务名称。
5. 在组件列表中，选择异常的组件，在机器**操作**列中单击**操作** > **重启**。
灾备管理中心运维操作

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

##### sync_check（minirds-mt/rds）

此告警点主要检测minirds-mt/rds容灾实例的容灾状态，出现此告警表示minirds-mt/rds容灾巡检异常， 可能会导致数据丢失、实例无法容灾切换或实例访问异常。本文档主要描述告警产品为minirds-mt/rds时的

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | minirds- mt rds | ASR控制台上minirds- mt/rds容灾巡检异常 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.12及后续版本。

**告警原因**

实例同步状态异常 minirds-mt/rds实例主备数据差异较大，导致主备之间需要的同步时间较长或不再同步。 sshtunnel不通 bcmc中部分产品的容灾切换和容灾巡检脚本需要打通到产品SR的SSH通道，以便于登录到SR容器中执行容灾巡检和容灾切换。 由于产品基线sshtunnel配置缺失或配置错误、tianji-sshtunnel产品问题以及其他问题，导致bcmc到产品SR的SSH通道没有正常打通，从而导致bcmc容灾巡检脚本执行异常。

**告警影响**

主备同步延迟过大，主节点故障时可能会导致数据丢失。 实例无法容灾切换，主节点故障时，实例无法自动切换到备节点，影响可用性。 实例访问异常，依赖该实例的云产品或应用运行异常。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**实例同步状态异常的处理方法**

处理方法以RDS产品为例。
1. 登录Apsara Uni-manager运维控制台。
灾备管理中心运维操作
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 进入杜康数据库管理平台，在左侧导航栏单击**系统管理**。
4. 在**系统管理**界面左侧导航栏选择**容灾管理**> **容灾切换**，在**从库最大延迟**列中查看实例延迟时间。

**说明**

若延迟时间大于0，小于60，等待主备数据同步。 若延迟时间小于-1，需要联系TAM支持人员做实例备库重搭。 若延迟时间为正整数，数值较大，且没有降低的趋势，则联系数据库运维人员检查。

**sshtunnel不通的处理方法**

1. 检查对端服务MiniRDS的sshd进程是否开启。
ii. 执行 ps -ef|grep sshd 检测sshd进程。 如果ssh的进程未启动，可以手动执行 `/usr/sbin/sshd` 来启动sshd进程。 如果容器中sshd进程不存在，通过 `yum install sshd` 安装sshd插件。
2. 修改bcmc集群sshtunnel配置。
i. 登录飞天基础运维平台。 ii. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。 iii. 在**产品列表**中查询bcmc，在目标集群**操作**列单击**集群详情**。 iv. 进入**集群详情**页面，切换至**终态配置**页签。 灾备管理中心运维操作

```
v. 修改 /services/tianji-sshtunnel-client/user/SSHTunnelClient/ssh_tunnel_bcmc.conf 文
```

件。添加FromProduct、FromClusterType、FromServerRole、FromService、FromUser、 ToProduct、ToClusterType、ToServerRole、ToService、ToUser信息，修改完成后提交变更。

**说明**

FromClusterType、FromServerRole注意区分单元与中心，中心使用BcmcCluster、Bcmc， 单元使用Bcmc4GeneralCluster、Bcmc4General，代码示例：

```
- FromProduct: bcmc
```

`//FromClusterType: Bcmc4GeneralCluster //`注意：中心使用`BcmcCluster`，单元使用`Bcmc4`

```
GeneralCluster
```

`//FromServerRole: Bcmc4General //`注意：中心使用`Bcmc`，单元使用`Bcmc4General`

```
  FromClusterType: BcmcCluster
  FromServerRole: Bcmc
  FromService: bcmc
  FromUser: root
```

`ToClusterType: maotai_7u //`需要打通的产品集群类型 `ToServerRole: Aurora //`需要打通的产品的`ServerRole`

```
  ToUser: root
```

3. 验证SSH隧道已打通。
i. 登录bcmc.Bcmc#容器。 灾备管理中心运维操作 ii. 在目录 `/home/admin/bcmc/config` 下执行 cat MINIRDS.py | grep "CURRENT_IP_LIST" ，获取 iii. 手动执行 `ssh <ip`地址> 命令，上一步IP列表中的IP都是通的。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

##### sync_check（TableStore/TableStoreInner）

此告警点主要检测TableStore/TableStoreInner容灾实例的容灾状态，出现此告警表示 TableStore/TableStoreInner容灾巡检异常，可能会导致数据丢失、实例无法容灾切换或实例访问异常。 本文档主要描述告警产品为TableStore/TableStoreInner时的sync_check告警项相关信息。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | ots tianji | ASR控制台上 TableStore /TableStore Inner容灾巡检异常 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.12及后续版本。

**告警原因**

灾备管理中心运维操作

**告警影响**

主备同步延迟过大，主节点故障时可能会导致数据丢失。 实例无法容灾切换。 实例访问异常，依赖该实例的云产品或应用运行异常。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**没有建立同步链路或同步中断的处理方法**

处理方法以TableStore为例。
1. 登录飞天基础运维平台。
2. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。
3. 在**产品列表**中查询ots，在目标集群**操作**列单击**集群详情**。
4. 在**服务列表**页签，单击**TableStore**服务。
5. 选择**InitCluster#**组件。
6. 在机器列表中，单击某台机器**操作**列中的**Terminal**，登录TableStore.InitCluster#终端机器。
7. 检查 `/apsara/ots_replication_tool/log/ots.log` 日志中有以下报错。
8. 执行 ps -ef|grep rep 找到init_cluster的进程，并kill该进程，等待进程被重新拉起。
9. 再次观察日志，等待同步。日志类似下图，说明已建立同步。
灾备管理中心运维操作

**说明**

日志刷新可能有点慢，kill进程后需要等待一两分钟观察。

**实例数据同步延迟过大的处理方法**

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**处理步骤**

1. 进入 `new_ots_replication_tool` 目录。
2. 为了避免有异常分片的问题，检查集群所有表的同步状态（执行较慢，取决于表数量），执行命

```
令 ./rep_checker.py check_table_rep_status 。
```

**说明**

有同步关系的实例的表同步状态已经通过 `./command.py get_rep_status` 命令检查。因此，本步骤也可以仅检查没有同步关系的实例的表同步状态（相比全量检查更快速）。执行以下命令：

```
./rep_checker.py check_table_rep_status --only_check_non_rep_inst 1
```

如果检查无问题，结果示例如下，确认结果中有“CheckResult: SUCCESS”字段，需要联系TAM支持人员提供支持，查看实例数据同步延迟过大的具体原因。 灾备管理中心运维操作

```
Check cluster ots-ssd-A-20210813-0013, instance _qoib6uAo2c4b86nXje(deleted), table _qoib6uAo2c4b86nXje#SqlOnlineIndexTaskTable ... Check cluster ots-ssd-A-20210813-0013, instance otstunnelm0013, table _t7GRGGuPAkKQ dHHMSh#sourceNunV ... Check cluster ots-ssd-A-20210813-0013, instance otstunnelm0013, table _t7GRGGuPAkKQ dHHMSh#targetOJJr ... Check cluster ots-ssd-A-20210813-0013, instance otssmoke0013, table otssmoke0013#test_base_api_table ... Check cluster ots-ssd-A-20210813-0013, instance otssmoke0013, table otssmoke0013#test_base_monitor ... Check cluster ots-ssd-B-20210813-00a6, instance otssmoke00a6, table otssmoke00a6#test_base_api_table ... Check cluster ots-ssd-B-20210813-00a6, instance otssmoke00a6, table otssmoke00a6#test_base_monitor ... -------------------------------- [CheckTableRepStatus] CheckResult: SUCCESS. --------------------------------
```

如果执行失败，或检查有异常，根据异常信息分情况处理。 a. 检查结果中出现表的同步状态非预期。 有同步关系的实例，表同步状态为TERMINATED说明表同步被关闭了；为SUSPENDED说明全量未完成，或者增量暂停状态。以上非预期情况，需要根据具体环境来看。 没有同步关系的实例，表同步状态不是TERMINATED。可能由于黑名单未处理，可以采用黑名单修复的方式解决，其他情况需要根据具体环境来判断。 b. 检查结果中，显示有Index表，不支持同步。 当前数据同步仅能同步主表的数据，不支持index表，包括local index和global index，备表上面也没有index表。 若实例有local index，在V3.16版本前，切换实例也会因为local index的问题而卡住，对于带 local index实例需要加黑名单。 建议对于有index表的实例，需要确认后，都将实例加入黑名单中，同时该实例也不能支持同城容灾。 c. 检查过程中报错，出现分片的同步状态是UNKNOWN。 原因可能是分片有异常，单独查看有问题的表的分片，通过执行 sql lp | grep 分片确认这些分片的机器分布。可能的原因是有单台或部分worker上分片卡住，登录对应worker查看是否有读写 pangu卡住的相关日志。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

##### sync_check（SLB）

此告警点主要检测SLB容灾实例的容灾状态，出现此告警表示SLB容灾巡检异常，可能会导致实例无法容灾切换或流量无法正常转发。本文档主要描述告警产品为SLB时的sync_check告警项相关信息。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|

灾备管理中心运维操作

| sync check _ | sync check _ | Bcmc# | P2 | slb | ASR控制台上SLB容灾巡检异常 | 1分钟执行一次 |
|---|---|---|---|---|---|---|

**适用版本**

适用于专有云企业版v3.12及后续版本。

**告警原因**

SSH隧道异常由于产品基线sshtunnel配置缺失或配置错误，tianji-sshtunnel产品bug问题以及其他问题，导致bcmc 到产品SR的SSH通道没有正常打通，从而导致bcmc容灾巡检脚本执行异常。 bcmc需要打通到主备机房slb-controller.SlbControlMaster#容器的SSH免密隧道，SSH隧道不通会报错。 异常实例监听不为0 实例在转发面LVS上的配置信息和管控数据库中记录的信息不一致导致的，需要修复异常监听实例。

**告警影响**

SLB容灾状态异常，可能会导致： 实例无法容灾切换。 流量无法正常转发，依赖SLB的云产品或应用运行异常。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**SSH隧道异常的处理方法**

1. 检查对端服务SLB的sshd进程是否开启。
i. 登录SLB服务容器。 ii. 执行 ps -ef|grep sshd 检测sshd进程。 如果ssh的进程未启动，可以手动执行 `/usr/sbin/sshd` 来启动sshd进程。 如果容器中sshd进程不存在，通过 `yum install sshd` 安装sshd插件。
2. 修改bcmc集群sshtunnel配置。
i. 登录飞天基础运维平台。 灾备管理中心运维操作 ii. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。 iii. 在**产品列表**中查询bcmc，在目标集群**操作**列单击**集群详情**。 iv. 进入**集群详情**页面，切换至**终态配置**页签。

```
v. 修改 /services/tianji-sshtunnel-client/user/SSHTunnelClient/ssh_tunnel_bcmc.conf 文
```

件。添加FromProduct、FromClusterType、FromServerRole、FromService、FromUser、 ToProduct、ToClusterType、ToServerRole、ToService、ToUser信息，修改完成后提交变更。

**说明**

FromClusterType、FromServerRole注意区分单元与中心，中心使用BcmcCluster、Bcmc， 单元使用Bcmc4GeneralCluster、Bcmc4General，代码示例：

```
- FromProduct: bcmc
```

`//FromClusterType: Bcmc4GeneralCluster //`注意：中心使用`BcmcCluster`，单元使用`Bcmc4`

```
GeneralCluster
```

`//FromServerRole: Bcmc4General //`注意：中心使用`Bcmc`，单元使用`Bcmc4General`

```
  FromClusterType: BcmcCluster
  FromServerRole: Bcmc
  FromService: bcmc
  FromUser: root
```

`ToProduct: slb //`需要打通的产品 `ToClusterType: slb_controller_Cluster //`需要打通的产品集群类型 `ToServerRole: SlbControlMaster //`需要打通的产品的`ServerRole` `ToService: slb-controller //`需要打通的产品的`Service`

```
  ToUser: root
```

3. 验证SSH隧道已打通。
i. 登录bcmc.Bcmc#容器。 灾备管理中心运维操作 ii. 在目录 `/home/admin/bcmc/config` 下执行 cat SLB.py | grep `"slb_control_master_iplist"` ，获取slb-controller.SlbControlMaster#的IP列表，如下图所示。 iii. 手动执行 `ssh <ip`地址> 命令，上一步IP列表中的IP都是通的。

**异常实例监听不为0的处理方法**

1. 排查健康检查问题。
i. 登录slb-controller.SlbAg#容器。 ii. 执行如下命令运行健康检查脚本，主要的健康检查脚本存放路径 `/deploy/alimonitor/script` 。

```
python checkHealth.py
```

iii. 检查 `/home/slb/ag/slb-test_run.log` 日志，找到error信息，检查导致健康检查失败的关键字。
2. 排查异常的lb问题。
ii. 执行如下命令检查异常的lb信息。查看北向数据的lb的status（异常情况包括provisioning、init、 configuring）和版本号是否一致。

```
select * from loadbalancer where current_version != target_version or (status not i n ("active", "deleted")) limit 100;
```

灾备管理中心运维操作 iii. 执行如下命令检查南向数据是否生成。查看南向数据的status（正常为Created）和版本号是否一致。

```
select * from network_conf where instance_id like '%lb_global_id%' \G
```

iv. 执行如下命令检查binding的生成情况。查看LvsGroup、lvs的status和版本号是否一致。

```
select * from network_conf_binding where network_conf_instance_id like "%xxxx%" \G
```

**说明**

命令中xxxx需要替换为network_conf表的instance_id。 v. 执行如下命令检查event事件。

```
select * from event where source_instance_id like '%lb_global_id%' \G
```

通过event的request_id把事件的tree打印出来。

```
info admin detail_event event_id ${instance_id}
```

北向数据存在，network_conf和binding数据不存在，一般表示lb创建失败，还未下发到南向。 北向数据存在，network_conf数据存在，binding表的数据不存在，一般表示lb创建成功，但是未下发到转发设备上。 北向数据存在，network_conf和binding数据存在，一般表示lb创建成功，配置已下发到转发设备上。
3. 排查异常的vip问题。
ii. 执行如下命令检查异常的vip信息。查看北向数据的vip的status（异常情况包括configuring_fail、 configuring、stopping、stopping_fail、starting、starting_fail）和版本号是否一致。

```
select * from vip where current_version != target_version or (status not in ("runni ng","stopped")) limit 100;
```

iii. 执行如下命令检查南向数据是否生成。查看南向数据的status（正常为Created）和版本号是否一致。

```
select * from network_conf where instance_id like '%listener_id%' \G
```

iv. 执行如下命令检查binding的生成情况。查看LvsGroup、lvs的status和版本号是否一致。

```
select * from network_conf_binding where network_conf_instance_id like "%xxxx%" \G
```

**说明**

命令中xxxx需要替换为network_conf表的instance_id。 灾备管理中心运维操作 v. 执行如下命令检查event事件。

```
select * from event where source_instance_id like '%listener_id%'\G
```

通过event的request_id把事件的tree打印出来。

```
info admin detail_event event_id ${instance_id}
```

北向数据存在，network_conf和binding数据不存在，一般表示vip创建失败，还未下发到南向。 北向数据存在，network_conf数据存在，binding表的数据不存在，一般表示vip创建成功，但是未下发到转发设备上。 北向数据存在，network_conf和binding数据存在，一般表示vip创建成功，配置已下发到转发设备上。
4. 根据排查的原因联系SLB运维人员协助解决。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

##### sync_check（Kafka）

此告警点主要检测Kafka容灾实例的容灾状态，出现此告警表示Kafka容灾巡检异常，可能会导致数据丢失、实例无法容灾切换或实例访问异常。本文档主要描述告警产品为Kafka时的sync_check告警项相关信息。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | kafka | ASR控制台上Kafka容灾巡检异常 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.16及后续版本。

**告警原因**

当前Kafka集群还未进行容灾配置，需要完成Kafka集群的容灾配置。

**告警影响**

Kafka容灾状态异常，可能会导致： 主备未配置数据同步，主节点故障时可能会导致数据丢失。 实例无法容灾切换。 实例访问异常，依赖该实例的应用运行异常。

**处理方法**

灾备管理中心运维操作

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**确认报错信息**

在ASR控制台**平台监控**> **产品监控**页面中，Kafka**容灾能力**监控项提示**No disaster recovery**
**instance**，且**主节点位置**为**未获取到**。

**前提条件**

环境中至少需要有2个Kafka集群和2个Replicator，且需要满足以下条件： 2个Kafka集群需要分布在主备不同的机房（不同AZ）。 2个Replicator需要分布在主备不同的机房（不同AZ）。 Kafka集群必须先成功创建出VIP，且需要做容灾配置的两个Kafka集群的VIP类型需要一致。VIP类型为 AnyTunnel或SingleTunnel，如果是创建SingleTunnel VIP，需要保证两个Kafka集群选择同一个 VPC。

**处理步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **中间件** > **消息队列** **Kafka** 版。
3. 进入**消息队列****Kafka**版页面，在左侧菜单栏**实例列表**中确认实例满足前提条件。
4. 在左侧菜单栏**容灾集群列表**中，创建容灾实例。
i. 单击**创建容灾集群**。 灾备管理中心运维操作 ii. 填写**容灾集群名称**，单击**下一步**。 iii. 在源**Kafka****实例**中选择主Kafka集群实例，在源**KafkaReplicator****实例**中选择主Replicator实例，单击**下一步**。 iv. 在**目标****Kafka****实例**中选择备Kafka集群实例，在**目标****KafkaReplicator****实例**中选择备Replicator实例，单击**创建**。 灾备管理中心运维操作

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

##### sync_check（Elasticsearch）

此告警点主要检测Elasticsearch容灾实例的容灾状态，出现此告警表示Elasticsearch容灾巡检异常，可能会导致数据丢失、实例无法容灾切换或实例访问异常。本文档主要描述告警产品为Elasticsearch时的

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | elasticsear ch | ASR控制台上 Elasticsear ch容灾巡检异常 | 1分钟执行一次 |

**适用版本**

适用于专有云企业版v3.16及后续版本。

**告警原因**

当前Elasticsearch集群还未进行容灾配置，需要完成Elasticsearch集群的容灾配置。

**告警影响**

Elasticsearch容灾状态异常，可能会导致： 主备未配置数据同步，主节点故障时可能会导致数据丢失。 实例无法容灾切换。 实例访问异常，依赖该实例的应用运行异常。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。

**确认报错信息**

在ASR控制台**平台监控**> **产品监控**页面中，Elasticsearch的容灾状态监测异常。 灾备管理中心运维操作

**前提条件**

在Apsara Uni-manager运维控制台创建用户asr_es，并给该用户授予elasticsearch_read角色权限。

**处理步骤**

1. 使用asr_es用户登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **大数据运维**> **elasticsearch****搜索服务管控**。
3. 进入**ESSEN**控制台，在左侧导航栏**实例管理**中，单击**创建实例**。
4. 在**基础配置**页面中，选择版本，单击**下一步**。
5. 在**集群配置**页面中，填写集群信息，单击**下一步**。
6. 在**网络及系统配置**页面中，网络类型选择**专有网络****(any tunnel)**，并设置登录密码，单击**开始创建**。
7. 参考上述操作在主机房和备机房各创建一个集群，设置相同的登录密码。
8. 在ops1机器上执行以下命令运行ES_ha_init.py脚本。

```bash
# ${masterInstance} 表示主集群instanceID ; ${slaveInstance} 表示备集群instanceID ;
```

${masterNamespace} 表示主集群所在命名空间 ; ${slaveNamespace} 表示备集群所在命名空间 ; ${masterIDC} 表示主机房`IDC`名称 ; ${slaveIDC} 表示备机房`IDC`名称 ; ${UserDomain} 表示用户自定义的用来访问`es`集群的域名

```
/home/tops/bin/python ES_ha_init.py -mi ${masterInstance} -si ${slaveInstance} -mn ${ masterNamespace} -sn ${slaveNamespace} -md ${masterIDC} -sd ${slaveIDC} -d ${UserDoma in} 示例: /home/tops/bin/python ES_ha_init.py -mi es-a -si es-b -mn xdcr-test-a -sn xdcr-t est-b -md amtest17 -sd amtest34 -d es-visit.xdcr-test.intra.env11e.shuguang.com
```

**说明**

脚本使用注意事项 : 已经被设置为备集群的实例不允许再被设置为主集群实例。 已经绑定IP的域名默认不允许使用，可以添加-f参数，强制使用指定的域名。 查询当前的容灾实例列表： `/home/tops/bin/python ES_ha_init.py -a list` 。 在刚增量部署完es容灾服务之后，在未创建es容灾实例的情况下，asr的容灾巡检页面可能会报错，可以执行 `/home/tops/bin/python ES_ha_init.py -a init` 命令触发相关数据库的数据源配置初始化。

**注意事项**

灾备管理中心运维操作不允许创建“.”开头或者“security-auditlog”开头的索引（该类型的索引不会进行数据同步）。 备机房删除index会触发同步，因此无法删除；而主机房如果删除index，备机房的index会同步删除。 client要求设置DNS缓存尽可能短（不能超过10秒）。 断电回切时，需要先在（断电前的）主机房执行如下命令开启同步链路，提前触发数据同步，避免容灾切换时一直block在数据同步阶段。
# 开启同步链路（可以在`asr`上校验数据同步链路是否配置成功） ${masterInstance} 表示主集群
instanceID ; ${user} 表示备集群实例用户名 ; ${password} 表示备集群实例用户密码 ; ${slaveClus `terMgmtVip}` 表示备集群实例的管理域域名

```bash
curl -XPOST -u ${user}:${password} ${slaveClusterMgmtVip}:9200/_xdcr/${masterInstance}?excludes=.*,security-auditlog*
```

`kibana`白屏操作（断电前的主集群）：

```
POST /_xdcr/${masterInstance}?excludes=.*,security-auditlog*
```

# 查看数据同步进度(当查询结果的第三列和第四列的数据一致时说明数据同步完成）${user} 表示备集群实例用
户名 ; ${password} 表示备集群实例用户密码 ; ${slaveClusterMgmtVip} 表示备集群实例的管理域域名

```bash
curl -u ${user}:${password} ${slaveClusterMgmtVip}:9200/_cat/xdcr? h=repository,index,localGCP,remoteGCP
```

`kibana`白屏操作（备集群）：

```
GET /_cat/xdcr?h=repository,index,localGCP,remoteGCP
```

断网回切时，除需要先在（断网前的）主机房手动配置开启同步链路之外，还可能需要将主机房索引 index删除，触发一次全量同步（根据现场是否可以接受主备集群部分数据不一致判断）。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

#### inspect_product_cluster_aplus

此告警点主要检测同城容灾主机房产品集群是否做了A'，出现此告警表示存在产品集群未做A'，可能会导致容灾切换失败。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| inspect pro _ duct cluste _ r aplus _ | inspect pro _ duct cluste _ r aplus _ | Bcmc# | P2 | bcmc | 同城容灾主机房集群未执行A'操作 | 30分钟执行一次 |

**适用版本**

适用于专有云企业版v3.14及后续版本。 灾备管理中心运维操作

**告警原因**

除ECS计算集群、存储集群外，其他所有在备机房部署的集群，其对应的主机房集群均需要做A'操作。

**说明**

只在主机房部署而未在备机房部署的集群，不需要做A'操作。

**告警影响**

云产品未完成同城容灾部署，容灾切换失败。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。
1. 针对双机房部署的集群中主集群未做A'的产品执行A'操作。

**重要**

注意事项： 执行A'之前，请确保主备集群都已到达终态。 基础中间件（middleWareAll、dauthProduct、aliware-taokeeper、middlewaredncs），必须在产品到达终态后立刻执行A'操作。 执行A'过程中，产品有先后顺序，请严格按照产品A'提交顺序进行。 MQ、OSS、Tablestore产品执行A'会有业务闪断，操作前需要跟客户申请变更窗口。 产品A'提交顺序 A'操作是集群级别的，建议顺序提交，即等待前一个提交命令返回成功，并在TianJi上观察到开始 rolling后，再继续提交下一个集群的升级。集群提交顺序如下：

**重要**

不在表格内的集群，可以在RDS集群提交后提交，BCMC集群最后提交A'操作。 MiniRDS在执行A'操作时会自动下发跨机房备库重搭，重搭过程不影响数据库实例读写， 可以第一个提交，同时并发提交其他集群。备库重搭时间会比较久，并且会有一定概率的迁移失败，现场操作人员需要密切监控MiniRDS和RDS的运维控制台，观察是否有中断或失败的迁移任务，如有请及时处理。

| 顺序ID | 产品 | 集群（现场请以实际为准） |
|---|---|---|
| 1 | tianji | tianji-A-e68c |
| 2 | minirds-mt | integrator-A-20200212-e682 maotai-A-20200212-e681 |

灾备管理中心运维操作

| 3 | baseServiceAll | StandardCloudCluster-A |
|---|---|---|
| 4 | webappAll | StandardCloudCluster |
| 5 | vnet | VnetCluster |
| 6 | xnet2 | Xnet2Cluster |
| 7 | ram | BasicCluster |
| 8 | qitian | qitianCluster |
| 9 | opsapi | opsapiCluster |
| 10 | tongque | tongqueCluster |
| 11 | asa | asaCluster |
| 12 | aso | asoCluster |
| 13 | slb | slbCluster slb yaochi Cluster _ _ |
| 14 | vpc | vpcAzoneCluster vpcRegionCluster vpcRegionXnetCluster vpcYaochiCluster |
| 15 | ecs | ECS-controller-A-e68d ECS-controller-A-e68f |
| 16 | oss | OssHybridCluster 重要如果您不想全量Bucket做同城容灾，请先不要执行OSS的A'操作，具体方案请联系OSS研发团队获取。 |

灾备管理中心运维操作

| 17 | rds | brain kvstore-yaochi maotai nosql-cleaneye pgsql ppassql proxy rds-dr-service rds-yaochi redis |
|---|---|---|
| 18 | On PaaS产品 | 根据现场On PaaS产品而定。 |
| 19 | bcmc | BcmcCluster-A |

a. 登录主机房ops1机器。 b. 执行如下命令，更新主机房的集群配置。

```
cd /apsarapangu/disk3/u_disk/upgrade_tools/tianji_zhuque_sdk ./upgrade_A_to_Aplus.py -z [$ZONE] -p [$PROJECT] -c [$CLUSTER] --tianjiCltConfig
```

**说明**

参数说明： $ZONE：主机房集群所在的Zone。 $PROJECT：主机房集群所在的project的名称。 $CLUSTER：主机房集群的名称。 命令示例：

```
cd /apsarapangu/disk3/u_disk/upgrade_tools/tianji_zhuque_sdk ./upgrade_A_to_Aplus.py -z cn-haikou-xxxx-xxxx-a -p tianji -c tianji-A- /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controlle
```

On PaaS产品A'操作（适用于v3.17之前版本） a. 下载arkctl工具。 灾备管理中心运维操作 b. 执行以下命令，获取环境中的所有On PaaS产品。

```
arkctl product list -iz
```

c. 执行以下命令，查看产品是否处于rolling状态。

```
arkctl product rolling ${id}
```

**说明**

id是上一步查询出来的产品ID。 d. 执行如下命令，查看产品是否处于Ready状态。

```
arkctl product list -iz
```

如果查询结果显示Ready状态，则说明部署成功。 On PaaS产品A'操作（适用于v3.17及之后版本） a. 下载arkctl工具。 b. 执行以下命令，获取环境中的所有On PaaS产品。

```
arkctl product list -iz
```

c. 执行以下命令检查haApsaraStack变量的值如果为 `true` ，则直接返回成功；如果为 `false` ， 则继续执行A'操作。

```
arkctl dr aplus ${id}
```

**说明**

id是上一步查询出来的产品ID。
2. 重新执行是否做A'检查，期望**未做****A'****产品列表**为空。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。 灾备管理中心运维操作

#### inspect_product_cluster_version

此告警点主要检测主备机房产品版本是否一致，出现此告警表示主备机房产品版本不一致，可能会导致容灾切换失败或切换后云产品功能变化。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| inspect pro _ duct cluste _ r version _ | inspect pro _ duct cluste _ r version _ | Bcmc# | P2 | bcmc | 主备机房产品版本不一致 | 30分钟执行一次 |

**适用版本**

适用于专有云企业版v3.14及后续版本。

**告警原因**

在同城容灾场景下，容灾的云产品必须要保证主备机房产品版本保持一致，不一致的产品会上报异常。

**告警影响**

产品集群版本检查状态异常，可能会导致： 容灾切换失败。 切换后，云产品功能变化。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。 针对主备机房部署版本不一致的云产品，请联系TAM支持人员升级产品版本。

#### inspect_product_variable

此告警点主要检测tianji API获取的bcmc依赖的基线变量与bcmc渲染出来的基线变量是否一致，出现此告警表示基线变量不一致，可能会导致容灾切换失败。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| inspect pro _ duct varia _ ble | inspect pro _ duct varia _ ble | Bcmc# | P2 | bcmc | ASR控制台上产品基线变量检查不通过 | 30分钟执行一次 |

灾备管理中心运维操作

**适用版本**

适用于专有云企业版v3.14及后续版本。

**告警原因**

由于云产品升级、扩容，或云产品服务发生了迁移，从而导致通过tianji API获取的bcmc依赖的基线变量与 bcmc渲染出来的基线变量不一致。

**说明**

|  | /opt/tianji/conf.tmpl |
|---|---|
| application-conf.yml |  |

bcmc中渲染出来的基线变量可参考 `/alidata/conf/antx.properties` 文件。

**告警影响**

容灾切换失败。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。 如果某产品执行过扩容操作，会导致bcmc的基线变量发生变化，需要重新rolling bcmc并重新渲染。 i. 登录飞天基础运维平台。 ii. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。 iii. 在**产品列表**中查询bcmc，在目标集群**操作**列单击**集群详情**。 iv. 进入**集群详情**页面，切换至**终态配置**页签。 v. 修改kv.conf文件，在kv.conf文件最后一行末尾处按回车键，然后单击**预览并提交**。 vi. 在预览窗口中输入描述，单击**提交**。 如果bcmc本该获取到某产品备机房集群的变量却获取到主机房集群的变量，那可能是该产品最近做过增量部署，需要检查bcmc集群配置中的serviceid.conf文件，删除对应的配置。 i. 登录飞天基础运维平台。 ii. 在**飞天基础运维平台**左侧导航栏中，选择**产品集群运维**。 iii. 在**产品列表**中查询bcmc，在目标集群**操作**列单击**集群详情**。 iv. 进入**集群详情**页面，切换至**终态配置**页签。 灾备管理中心运维操作 v. 在serviceid.conf文件中删除对应产品的配置行。

**说明**

如果上述步骤未解决告警问题，请提工单（服务请求单）联系阿里云技术支持。

#### inspect_product_cluster_deploy

此告警点主要检测主备机房云产品集群是否对等部署，出现此告警表示检测到非对等部署的云产品，可能会导致容灾切换失败、切换后云产品访问异常或云产品负载过高。

**告警属性**

| 告警ID | 监控项名称 | 告警来源 | 告警级别 | 告警产品 | 触发条件 | 执行周期 |
|---|---|---|---|---|---|---|
| inspect pro _ duct cluste _ r deploy _ | inspect pro _ duct cluste _ r deploy _ | Bcmc# | P2 | bcmc | 主备机房云产品集群部署不对等 | 30分钟执行一次 |

**适用版本**

适用于专有云企业版v3.14及后续版本。

**告警原因**

在同城容灾的场景下，除个别支持非对等容灾的产品外，需要做容灾的云产品必须要保证主备机房云产品版本保持一致、云产品集群对等部署，检查到非对等部署的云产品会上报异常。

**说明**

支持非对等部署的产品清单：RDS、Redis、OSS、ECS、MaxCompute。

**告警影响**

集群部署检查状态异常，可能会导致： 容灾切换失败。 切换后，非对等部署的云产品访问异常。 灾备管理中心运维操作切换后，云产品负载过高。

**处理方法**

**警告**

所有告警处理方法涉及到修改产品任何配置，均需要走生产变更流程确认方案的可行性以及流程规范性，若属紧急应急范畴需客户与TAM同时同意方可执行，否则不允许直接执行处理方法的任何步骤。 联系现场TAM支持人员确认云产品部署是否有误，若部署有误则增量部署集群后重新发起检查，若部署无误则忽略异常。

#### 附录

##### 登录Apsara Uni-manager运营控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
灾备管理中心运维操作

**说明**

单击页面右上角的当前语言可以切换其它语言。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
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

绑定并开启MFA的操作请参见管理多因素认证。

**相关操作**

**忘记密码**

1. 用户忘记登录密码时，单击密码输入框下方的**忘记密码**。
2. 在忘记密码页面，输入**账户名**、**邮箱**和验证码后，单击**确认**。
灾备管理中心运维操作

**说明**

账户名请输入当前账号的用户名，邮箱请输入注册账号的Email地址。 重置密码的链接将发至邮箱，进入链接后用户可输入新密码。

##### 登录Apsara Uni-manager运维控制台

本文介绍运维工程师等相关用户如何登录到Apsara Uni-manager运维控制台。

**前提条件**

已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为region-id.ops.console.intranet-domain-id。 推荐使用Chrome浏览器。

**操作步骤**

1. 打开浏览器。
2. 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址，按回车键。

**说明**

您可以单击右上角的当前语言切换其它语言。当前支持简体中文、英文、繁体中文三种语言切换。
3. 输入正确的用户名及密码。
灾备管理中心运维操作

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码必须满足以下要求： 必须包含英文大小写字母。 必须包含阿拉伯数字（0~9）。 必须包含特殊符号，包括感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等。 密码长度为10~20个字符。
4. 单击**账号登录**。

##### 登录容器

本文介绍登录容器的具体操作步骤，以登录bcmc.Bcmc#容器为例。

**操作步骤**

1. 登录终端。
ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品集群运维**页面，搜索bcmc服务。 v. 在目标集群的**操作**列，单击**集群详情**。 vi. 在服务列表中，单击**bcmc**。 灾备管理中心运维操作 vii. 选择**Bcmc#**组件，在**实例列表**页签下，单击实例**操作**列的**Terminal**。
2. 执行如下命令查询容器的ID。

```bash
docker ps
```

3. 执行如下命令进入容器。

```bash
docker exec -it <容器ID> /bin/bash
```

##### 登录xuanyuan数据库

本文介绍登录SLB的xuanyuan数据库的具体操作。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在产品列表中查询slb，在slbCluster-A集群**操作**列单击**集群详情**。
5. 在服务列表中单击**slb-controller**服务名称。
6. 选择**SlbControlMaster#**组件。
7. 切换至**资源列表**页签，找到**名称**和**类型**分别为**xuanyuan**和**db**的资源，在其**资源申请结果**列中查看
db_host、user、db_password、db_port、db_name的取值。 灾备管理中心运维操作
8. 切换至**实例列表**页签，在任一实例的**操作**列单击**Terminal**。
9. 执行如下命令，登录xuanyuan数据库。db_host、user、db_password、db_port、db_name的取值
请参见步骤7。

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

##### 登录飞天基础运维平台系统

**前提条件**

已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为region-id.ops.asconsole.intranet-domain-id。 推荐使用Chrome浏览器。

**操作步骤**

1. 打开浏览器。
2. 在地址栏中，输入Apsara Uni-manager运维控制台访问地址，按回车键。

**说明**

您可以单击右上角的下拉列表切换语言。
3. 输入正确的用户名及密码。

**说明**

登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。 首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码必须满足以下要求： 必须包含英文大小写字母。 必须包含阿拉伯数字（0~9）。 必须包含特殊符号，包括感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等。 密码长度为10~20个字符。
4. 单击**登录**。
灾备管理中心运维操作
5. 在顶部菜单栏，选择**平台运维** > **飞天基础运维平台** > **资源管理**。

##### 备库重搭

本文为您介绍备库重搭的操作方法，帮助您更快了解备库重搭。

**操作步骤**

**1.查看异常实例基本信息、链路类型、端口和主库IP信息**

1. 登录杜康数据库管理平台。
2. 选择**实例管理**> **实例列表**，单击需要操作的实例，进入实例详情页面。
如果是DNS链路类型，登录实例所在主机，执行如下命令查看是否解析正确。如果解析失败，联系产研同学协助解决。 dig ${域名} 如果是lvs链路类型，确认机房信息IP与主实例机器IP是否一致。如果不一致，请停止操作并联系产研同学协助解决。

**2.主备库read_only参数检查**

1. 登录主库，请参见登录异常实例。
2. 执行如下SQL语句，查看主库的读写状态。
i. 当结果显示为ON，即为主库异常。

```
 show variables like 'read_only';
```

ii. 执行如下SQL语句，把read_only参数设置为OFF。

```
 set global read_only = 0;
```

3. 登录备库。
4. 执行如下SQL语句，查看备库的读写状态。
灾备管理中心运维操作 i. 当结果显示为OFF，即为备库异常。

```
 show variables like 'read_only';
```

ii. 执行如下SQL语句，把read_only参数设置为ON。

```
 set global read_only = 1;
```

**3.方案实施**

1. 登录杜康数据库管理平台。
2. 选择**实例管理**> **实例列表**，单击需要操作的实例。
3. 选择**备份策略**> **创建临时备份**，在弹出的窗口中，选择**FULL**> **主库物理备份**> **点击查看**> **确定**。

**说明**

必须为不存在MyISAM表。
4. 单击**备份恢复**，确认能够看到主库的临时备份，说明已经完成。（18小时内即可）
5. 在**基本信息**页面最下方，单击**重搭**[**备库重搭**|**节点重搭**]，在弹出的窗口中，勾选**是否强制主库备份**，选择
对应的主机，选择重搭方式。

**说明**

本地重搭表示在原备库所在的主机上重搭，跨机表示重选主机。 灾备管理中心运维操作
6. 单击**提交**。
7. 单击**任务管理**，观察任务进度，直到任务完成。

**说明**

如果存在失败任务，联系产研同学协助解决。
8. 登录异常实例。
9. 执行如下SQL语句，查看返回结果。

```
show slave status\G
```

系统显示如下类似结果，表示重搭成功。

##### 登录异常实例

**操作步骤**

灾备管理中心运维操作
1. 登录杜康数据库管理平台。
2. 选择**实例管理** > **实例列表**，找到异常的实例名并进入实例详情页面。
3. 在**主机实例信息**区域，查看并记录异常实例的**主机名称**和**ip&port**。
4. 登录飞天基础运维平台。
5. 在首页搜索主机名称，单击**Terminal**，进入异常节点。
6. 执行如下命令，登录异常实例。

```bash
sudo my ${port}
```

**说明**

如果是root用户，可不用 `sudo` 命令。 系统显示如下类似结果：
7. 显示 `mysql>` 表示登录成功。
灾备管理中心维操作

## 云产品运维操作

### TianJi

#### 终态检查

本文介绍在飞天基础运维平台查看产品终态情况的检查方法和期望结果。

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在**产品集群运维**页面，查看主备机房产品终态情况。

**期望结果**

未达终态：0个。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

### DNS

#### 数据一致性检查

**检查方法**

1. 检查主机房dnsslave数据一致性。
i. 登录主机房ops1或ops2的DnsSlave服务容器。 ii. 将脚本localIdc_slave_and_slave_compare.py拷贝至 `/root/opsbuild/tools/dataConsistCheck/` ，执行以下命令检查主机房ops1和ops2数据一致性。

```
python /root/opsbuild/tools/dataConsistCheck/localIdc_slave_and_slave_compare.py
```

2. 检查主机房etcd与dnsslave数据一致性。
i. 登录主机房ops.OpsDnsSlave#服务容器。 灾备管理中心维操作 ii. 将脚本localIdc_etcd_and_slave_compare.py拷贝至 `/root/opsbuild/tools/dataConsistCheck/` ，执行以下命令检查主机房etcd与dnsslave数据一致性。

```
python /root/opsbuild/tools/dataConsistCheck/localIdc_etcd_and_slave_compare.py
```

3. 检查主/备机房etcd集群数据一致性。
i. 登录主/备机房ops.OpsDnsSlave#服务容器。 ii. 将脚本masterIdcEtcd_and_secondIdcEtcd_compare.py拷贝至 `/root/opsbuild/tools/dataConsistCheck/` ，执行以下命令检查主/备机房etcd集群数据一致性。

```
python /root/opsbuild/tools/dataConsistCheck/masterIdcEtcd_and_secondIdcEtcd_compare.py
```

4. 检查备机房etcd与dnsslave数据一致性。
i. 登录备机房ops.OpsDnsSlave#服务容器。 ii. 将脚本localIdc_etcd_and_slave_compare.py拷贝至 `/root/opsbuild/tools/dataConsistCheck/` ，执行以下命令检查备机房etcd与dnsslave数据一致性。

```
python /root/opsbuild/tools/dataConsistCheck/localIdc_etcd_and_slave_compare.py
```

**期望结果**

1. 命令执行结果类似下图，在ops1和ops2上获取到当前zone的rr数量一致。

**说明**

rr是Resource Records的缩写。 当前zone在ops1和ops2上的rr数量不一致时，高亮显示差异，格式为：rr:{'ops1': [],'ops2':[]}。 bcmc-minirds-check是ASR测试域名。如果命令执行结果中高亮提示bcmc-minirdscheck存在差异，请忽略不计。
2. 命令执行结果类似下图，在etcd集群中、ops1和ops2上获取到当前zone的rr数量一致。

**说明**

当etcd和ops1上的rr数量不一致时，高亮显示差异，格式为：rr:{'ops1':[],'etcd':[]}。 灾备管理中心维操作
3. 命令执行结果类似下图，在两个etcd集群中获取到当前zone的rr数量一致。

**说明**

当两个etcd集群中的rr数量不一致时，高亮显示差异，格式为：rr:{'FirstEtcd':[],'SecondEtcd': []}。
4. 命令执行结果类似下图，在etcd集群中、ops1和ops2上获取到当前zone的rr数量一致。

**说明**

当etcd和ops1上的rr数量不一致时，高亮显示差异，格式为：rr:{'ops1':[],'etcd':[]}。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### 域名解析服务检查

本文介绍检查DNS域名解析服务是否能解析IP地址的检查方法和期望结果。

**检查方法**

分别在主备机房的ops1和ops2机器执行 `dig +short dnsapi1.tbsite.net` ，查看是否可以正常解析出 IP地址。 灾备管理中心维操作

**期望结果**

正确解析IP地址。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

### MiniRDS

#### 任务检查

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维**> **管控服务运维**> **元数据库运维****·Mini****杜康**。
3. 进入Mini杜康数据库管理平台，在左侧导航栏选择**任务管理**，依次选择**中断的任务**/**等待的任务**/**临时关闭**
**的任务**/**暂停的任务**/**运行的任务**，查看列表中任务详情。

**期望结果**

**中断的任务**/**等待的任务**/**临时关闭的任务**/**暂停的任务**/**运行的任务**各项均无任务。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### 实例容灾检查

灾备管理中心维操作

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维**> **管控服务运维**> **元数据库运维****·Mini****杜康**。
3. 进入Mini杜康数据库管理平台，在左侧导航栏单击**系统管理。**
4. 在**系统管理**界面左侧导航栏选择**容灾管理**>**容灾切换**，在下方列表中查询实例状态。

**期望结果**

除dbaas_db外，所有**实例可用**、**可切换**状态为**OK**，且从库最大**延迟**的值大于等于0，小于60。
**主库信息**为**读写**状态，**从库信息**为**只读**状态。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### 实例状态检查

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维**> **管控服务运维**> **元数据库运维****·Mini****杜康**。
灾备管理中心维操作
3. 进入Mini杜康数据库管理平台，在左侧导航栏选择**实例管理**>**实例列表**，根据**CPU**/**QPS**/**连接数**/**磁盘使**
**用率**分别排序，查看实例各项信息。

**期望结果**

所有实例**CPU**/**QPS**/**连接数**/**磁盘使用率**均小于或等于50%。

**说明**

若不满足要求，则建议根据现场实际情况决定是否需要扩容，或提单联系阿里云技术支持处理。

### RDS

#### 任务检查

本文介绍RDS任务状态检查的方法和期望结果。

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 进入杜康数据库管理平台，在左侧导航栏单击**任务管理**，依次选择**中断的任务**/**等待的任务**/**临时关闭的任**
务/**暂停的任务**/**运行的任务**，查看列表中任务详情。

**期望结果**

灾备管理中心维操作
**中断的任务**/**等待的任务**/**临时关闭的任务**/**暂停的任务**/**运行的任务**各项均无任务。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### 实例容灾检查

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
3. 进入杜康数据库管理平台，在左侧导航栏单击**系统管理**。
4. 在**系统管理**界面左侧导航栏选择**容灾管理**>**容灾切换**，在下方列表中查询实例状态。

**期望结果**

所有**实例可用**、**可切换**状态**OK**，且从库最大**延迟**的值大于等于0，小于60。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### 实例状态检查

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **数据库运维**> **云数据库统一运维平台**·**杜康**。
灾备管理中心维操作
3. 进入杜康数据库管理平台，在左侧导航栏单击**实例管理**>**实例列表**，根据**CPU**/**QPS**/**连接数**/**磁盘使用**
率分别排序，查看实例各项信息。

**期望结果**

所有实例**CPU**/**QPS**/**连接数**/**磁盘使用率**均**小于或等于****50%**。

**说明**

若不满足要求，则建议根据现场实际情况决定是否需要扩容，或提单联系阿里云技术支持处理。

### SLB

#### LVS状态检查

**检查方法**

1. 登录slb-controller.SlbAg#容器。
2. 使用cli执行如下命令。

```
list admin lb_node
```

**期望结果**

灾备管理中心维操作
**configuration**均为**Enabled**，**online_status**均为**online**。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### proxy状态检查

本文介绍proxy状态的检查方法和期望结果。

**检查方法**

1. 登录slb-controller.SlbAg#容器。
2. 使用cli执行下述命令。

```
list admin proxy
```

**期望结果**

**configuration**均为**Enabled**，**online_status**均为**online**。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### keyserver状态检查

本文介绍keyserver状态的检查方法和期望结果。

**检查方法**

1. 登录slb-controller.SlbAg#容器。
2. 使用cli执行下述命令。

```
list admin keyserver
```

**期望结果**

**status**均为**online**。
灾备管理中心维操作

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

### OSS

#### 检查是否有location不在主机房的bucket

本文介绍检查bucket的location是否都在主机房的检查方法和期望结果。

**检查方法**

1. 登录oss_meta数据库。
2. 通过 select cluster,location from location_table; ，查看主机房location对应的机房集群。

```
3. 通过 select name,location from oss_meta_bucket where location <>"{主机房location}"; ，查
```

看location不在主机房的bucket列表。

**期望结果**

查询结果为空。

**说明**

结果为空意味着所有的bucket的location都在主机房。 若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

### ECS

灾备管理中心维操作

#### nc状态检查

本文介绍nc状态的检查方法和期望结果。

**检查方法**

1. 登录ecs的houyi-reg数据库。
2. 执行 select id,ip,status,hostname,biz_status from nc; 命令查看所有nc状态。

**期望结果**

所有nc状态都是free。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

### TableStore/TableStoreInner

#### 产品状态检查

本文介绍检查Tablestore、Tablestore-inner产品状态的前置操作和检查项。

**前置操作**

1. 下载new_ots_replication_tool.tar.gz工具包。
灾备管理中心维操作
2. 登录Apsara Uni-manager运维控制台。
3. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
4. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
5. 在**产品集群运维**页面，查询ots集群，单击**操作**列的**集群详情**。
6. 在服务列表中单击**TableStore**服务名称。
7. 选择**PortalAgServer#**组件，在**实例列表**页签下，单击实例**操作**列的**Terminal**，登录终端机器。
8. 在任意目录下使用admin用户解压工具包。
9. 解压后自动生成 `new_ots_replication_tool` 目录，进入对应目录，执行后续检查项。

**检查项**

1. 主备同步状态检查。
2. 集群配置检查。
3. 实例黑名单检查。
4. 表同步状态检查。
5. 主备表的meta配置检查。

##### 主备同步状态检查

本文介绍检查主备同步的检查方法和期望结果。

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**检查方法**

1. 进入 `new_ots_replication_tool` 目录。
2. 执行命令 `./command.py get_rep_status` 。
执行结果示例： 灾备管理中心维操作

**说明**

如果AllReplicationDone为true，表示当前时刻同步延迟为0，否则查看 MinLastSyncTime，计算与当前时间差为同步延迟时间。 RepStatus里有每个实例下表的同步状态，确认每个表的同步都已经进入增量阶段 （ReplicationStatus为Live）。如果有表的状态为Unknown，表示该表同步被手动暂停或者关闭了；如果是Bootstrap状态，表示在全量同步阶段，全量同步完成会变成增量 （Live）。 NoRepInfoInstanceCount为没有同步关系的实例数，这些实例一般为黑名单实例，command.py脚本不会获取这些实例的同步状态。

**期望结果**

AllReplicationDone为true。 RepStatus里每个实例下表的ReplicationStatus为Live。 NoRepInfoInstanceCount为0。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

##### 集群配置检查

本文介绍检查集群配置的检查方法和期望结果。

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**检查方法**

1. 进入 `new_ots_replication_tool` 目录。
灾备管理中心维操作
2. 执行命令 `./rep_checker.py check_cluster_config` 。
如果检查无问题，结果示例如下，确认结果中“CheckResult: SUCCESS”字段。

```
-------------------------------- [CheckClusterConfig] CheckResult: SUCCESS. --------------------------------
```

如果执行失败，或检查有异常，根据异常信息分情况处理。

**期望结果**

结果中有“CheckResult: SUCCESS”字段。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

##### 实例黑名单检查

本文介绍检查实例黑名单的检查方法和期望结果。

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**检查方法**

1. 进入 `new_ots_replication_tool` 目录。
2. 执行命令 `./rep_checker.py check_black_list` 。
如果检查无问题，结果示例如下，确认结果中“CheckResult: SUCCESS”字段。

```
check black instance: otssmoke0013 ... check black instance: otstunnelm0013 ... check black instance: otssmoke00a6 ... check black instance: otstunnelm00a6 ... -------------------------------- [CheckBlackList] CheckResult: SUCCESS. --------------------------------
```

如果执行失败，或检查有异常，根据异常信息分情况处理。

**期望结果**

结果中有“CheckResult: SUCCESS”字段。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

##### 表同步状态检查

灾备管理中心维操作本文介绍检查表同步状态的检查方法和期望结果。

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**检查方法**

1. 进入 `new_ots_replication_tool` 目录。
2. 为了避免有异常分片的问题，检查集群所有表的同步状态（执行较慢，取决于表数量），执行命

```
令 ./rep_checker.py check_table_rep_status 。
```

**说明**

有同步关系的实例的表同步状态已经通过 `./command.py get_rep_status` 命令检查。因此，本步骤也可以仅检查没有同步关系的实例的表同步状态（相比全量检查更快速）。执行以下命令：

```
./rep_checker.py check_table_rep_status --only_check_non_rep_inst 1
```

如果检查无问题，结果示例如下，确认结果中“CheckResult: SUCCESS”字段。

```
Check cluster ots-ssd-A-20210813-0013, instance _qoib6uAo2c4b86nXje(deleted), table _qoib6uAo2c4b86nXje#SqlOnlineIndexTaskTable ... Check cluster ots-ssd-A-20210813-0013, instance otstunnelm0013, table _t7GRGGuPAkKQ dHHMSh#sourceNunV ... Check cluster ots-ssd-A-20210813-0013, instance otstunnelm0013, table _t7GRGGuPAkKQ dHHMSh#targetOJJr ... Check cluster ots-ssd-A-20210813-0013, instance otssmoke0013, table otssmoke0013#test_base_api_table ... Check cluster ots-ssd-A-20210813-0013, instance otssmoke0013, table otssmoke0013#test_base_monitor ... Check cluster ots-ssd-B-20210813-00a6, instance otssmoke00a6, table otssmoke00a6#test_base_api_table ... Check cluster ots-ssd-B-20210813-00a6, instance otssmoke00a6, table otssmoke00a6#test_base_monitor ... -------------------------------- [CheckTableRepStatus] CheckResult: SUCCESS. --------------------------------
```

如果执行失败，或检查有异常，根据异常信息分情况处理。

**期望结果**

结果中有“CheckResult: SUCCESS”字段。 当结果中不包含“CheckResult: SUCCESS”字段，可能有以下几种情况：
1. 检查结果中出现表的同步状态非预期。
有同步关系的实例，表同步状态为TERMINATED说明表同步被关闭了；为SUSPENDED说明全量未完成，或者增量暂停状态。以上非预期情况，需要根据具体环境来看。 没有同步关系的实例，表同步状态不是TERMINATED。可能由于黑名单未处理，可以采用黑名单修复的方式解决，其他情况需要根据具体环境来判断。
2. 检查结果中，显示有Index表，不支持同步。
灾备管理中心维操作当前数据同步仅能同步主表的数据，不支持index表，包括local index和global index，备表上面也没有index表。 若实例有local index，在V3.16版本前，切换实例也会因为local index的问题而卡住，对于带local index实例需要加黑名单。 建议对于有index表的实例，需要确认后，都将实例加入黑名单中，同时该实例也不能支持同城容灾。
3. 检查过程中报错，出现分片的同步状态是UNKNOWN。
原因可能是分片有异常，单独查看有问题的表的分片，通过执行 sql lp | grep 分片确认这些分片的机器分布。可能的原因是有单台或部分worker上分片卡住，登录对应worker查看是否有读写pangu卡住的相关日志。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

##### 主备表的meta配置检查

本文介绍检查主备表的meta配置的检查方法和期望结果。

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**检查方法**

1. 进入 `new_ots_replication_tool` 目录。
2. 执行命令 `./rep_checker.py check_table_meta` 。
如果检查无问题，结果示例如下，确认结果中“CheckResult: SUCCESS”字段。

```
Check cluster ots-ssd-A-20210813-0013, instance bcmc-bct-SSD, table _t7UC1fLM7OYuMU bxwW#bcmc_bct ... Check cluster ots-ssd-A-20210813-0013, instance drbs, table _t7dsKSbg4AUgx76yeg#ip_access ... -------------------------------- [CheckTableMeta] CheckResult: SUCCESS. --------------------------------
```

如果检查失败，表示有配置不一致，示例如下。 示例说明：lt-ots-test00实例的test001表，主集群TTL为86400000，备集群TTL为-1（永不过期），此时需要订正备集群的TTL配置，请参见主备表配置不一致订正方法。

```
[CheckTableMeta] CheckResult: FAIL. [CheckTableMeta] Detail: [WARNING]: [instance: lt-ots-test00, table: test001], TTL mismatch, primary value: 86400000, secondary value: -1.
```

灾备管理中心维操作

**说明**

MaxVersions：表中每列保存的最大版本数。 TTL：数据过期时间。 Stream：是否打开增量日志的开关。

**期望结果**

结果中有“CheckResult: SUCCESS”字段。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

### ASO

#### 流量检查

本文介绍网络设备端口状态、流量的检查方法和期望结果。

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**产品运维**> **网络运维**> **网络运维控制台**。
3. 在网络运维控制台左侧菜单栏选择**基础网络**>**网元管理**。
4. 在设备列表中单击ISW或MSW的设备名称。
灾备管理中心维操作
5. 查看端口**管理状态**和**操作状态**。
6. 单击端口名称，查看端口流量。

**期望结果**

端口**管理状态**和**操作状态**全部为**Up**，流量正常。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。

#### 告警检查

本文介绍Apsara Uni-manager运维控制台上告警的查看方法和期望结果。

**检查方法**

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**监控告警** > **告警管理** > **告警概览**。
3. 查看告警详情。

**期望结果**

灾备管理中心维操作无告警。

**说明**

若不满足要求，则需要排查解决问题，或提单联系阿里云技术支持修复。 灾备管理中心

## 常见问题

### 如何解决ASR备机房VIP资源异常的问

**题**

本章节介绍如何查看主备机房记录的IP值以及对于异常情况如何处理的解决方案。

**问题描述**

ASR备机房vip资源异常，表现为部分节点可以Ping通，部分节点无法Ping通，并且部分节点在服务运维中无法搜索到对应的vip资源。

**可能原因**

飞天基础运维平台中资源大盘查到的nc_list比同城管理平台ASR的RealServer IP多。 飞天基础运维平台中资源大盘查到的nc_list比同城管理平台ASR的RealServer IP少。 飞天基础运维平台中资源大盘查到的nc_list和同城管理平台ASR的RealServer IP一样多，仅仅是比对结果异常。

**解决方案**

1. 查看主备机房记录的IP值。
i. 登录运维控制台。 ii. 在顶部菜单中选择**平台运维** > **容灾管理** > **同城容灾管理平台****ASR****（备机房）**。 iii. 在左侧菜单中选择**平台检查** > **环境检查**。 iv. 在**VIP****资源**区域，将鼠标放置在**资源名称**为**remotemock**的**RealServer IP**列。
2. 在资源大盘中查找并记录NC中的IP地址。
i. 在顶部菜单中选择**平台运维** > **飞天基础运维平台** > **资源管理**。 ii. 在左侧导航栏中单击**运维工具** > **资源大盘**。 iii. 在**资源大盘**页面选择**集群**，输入ECS，单击 。 灾备管理中心 iv. 单击类型为vip同时Name为上一步服务名称的Result列，查看nc_list的IP。 如果天基查到的nc_list比同城管理平台ASR的SLB查到的多，则需要在飞天基础运维平台里面查看 nc里面多出来的IP对应的机器是否属于这个服务，如果属于，需要SLB将realserver加上去。 如果天基查到的nc_list比同城管理平台ASR的SLB查到的少，则需要在天基里面查看下多出来的IP的机器是不是属于这个服务，如果是，可能是天基资源申请的问题，需要飞天基础运维平台那边订正。 请联系飞天基础运维平台的产品团队定位处理。 如果天基查到的nc_list比同城管理平台ASR的SLB查到的一样多，则需要联系具体异常的产品团队定位处理。
3. 添加RealServer。

**警告**

添加或移除RealServer需与对应VIP归属产品或客户进行确认方可执行，一般核实无误后进行操作无业务影响，误操作风险较高容易中断业务。确认可执行后请联系SLB团队协助添加或移除RealServer。

**验证结果**

1. 登录运维控制台。
2.
3. 在左侧菜单中选择**平台检查** > **环境检查**。
4. 在**VIP****资源**区域，查看**比对结果**列是否已正常。
比对结果正常，问题处理结束。 比对结果异常，请联系服务异常的产品团队定位处理。 灾备管理中心

## 附录

### 查看ASR日志

本文介绍ASR相关日志的所在目录和查看方法。

**操作步骤**

1. 登录bcmc.Bcmc#容器。
2. 选择需要查看的日志文件，日志文件说明详见下表。

| 日志文件 | 描述 |
|---|---|
| /home/admin/bcmc/logs/error.log | bcmc错误日志。 |
| /home/admin/bcmc/logs/info.log | bcmc运行日志。 |
| /home/admin/bcmc/logs/scripts/script.log | bcmc执行脚本日志。 |
| /home/admin/bcmc/scripts/{产品名}/logs/{产品名} synccheck.log _ | 各产品脚本巡检日志。 |
| /home/admin/bcmc/scripts/{产品名}/logs/{产品名} switch.log _ | 各产品切换日志。 |

**说明**

不带日期的日志文件为当天的日志文件。
3. 查看日志，以查看bcmc错误日志为例。
i. 执行 `cd /home/admin/bcmc/logs/` 进入日志所在目录。 灾备管理中心 ii. 执行 `ll` 查看目录中的所有文件。 iii. 执行 `vim error.log` 查看错误日志详情。 iv. 执行 `/2022-12-15 00:04:03` 可以搜索具体时间的日志详情。

**说明**

时间以实际需要进行修改。 v. 执行 `:q` 退出日志详情查看页面。

### 登录容器

本文介绍登录容器的具体操作步骤，以登录bcmc.Bcmc#容器为例。

**操作步骤**

1. 登录终端。
灾备管理中心 ii. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。 iv. 在**产品集群运维**页面，搜索bcmc服务。 v. 在目标集群的**操作**列，单击**集群详情**。 vi. 在服务列表中，单击**bcmc**。 vii. 选择**Bcmc#**组件，在**实例列表**页签下，单击实例**操作**列的**Terminal**。
2. 执行如下命令查询容器的ID。

```bash
docker ps
```

3. 执行如下命令进入容器。

```bash
docker exec -it <容器ID> /bin/bash
```

灾备管理中心

### 登录tianji-sshtunnel数据库

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在产品列表中查询tianji，在主集群**操作**列单击**集群详情**。
5. 在服务列表中单击**tianji-sshtunnel**服务名称。
6. 选择**SSHTunnelMaster#**组件。
7. 切换至**资源列表**页签，找到**名称**和**类型**分别为**sshtunnel**和**db**的资源，在其**资源申请结果**列中查看
db_host、user、db_password、db_port、db_name的取值。
8. 切换至**实例列表**页签，在任一实例的**操作**列单击**Terminal**。
9. 执行如下命令，登录tianji-sshtunnel数据库。db_host、user、db_password、db_port、db_name
的取值请参见步骤7。

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

### 登录oss_meta数据库

1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在产品列表中查询oss，在主集群**操作**列单击**集群详情**。
5. 在服务列表中单击**oss-ocm-server**服务名称。
6. 选择**DBInit#**组件。
7. 切换至**资源列表**页签，找到**名称**和**类型**分别为**oss_meta**和**db**的资源，在其**资源申请结果**列中查看
db_host、user、db_password、db_port、db_name的取值。
8. 切换至**实例列表**页签，在任一实例的**操作**列单击**Terminal**。
灾备管理中心
9. 执行如下命令，登录oss_meta数据库。db_host、user、db_password、db_port、db_name的取值
请参见步骤7。

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

### 登录houyi-reg数据库

本文介绍登录ecs的houyi-reg数据库的具体操作。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **资源管理**。
3. 在**飞天基础运维平台**左侧导航栏中，选择**资源管理** > **产品集群运维**。
4. 在产品列表中查询ecs，在ECS-controller-A集群**操作**列单击**集群详情**。
5. 在服务列表中单击**ecs-houyi**服务名称。
6. 选择**Regionmaster#**组件。
7. 切换至**资源列表**页签，找到**名称**和**类型**分别为**houyi_reg**和**db**的资源，在其**资源申请结果**列中查看
db_host、user、db_password、db_port、db_name的取值。
8. 切换至**实例列表**页签，在任一实例的**操作**列单击**Terminal**。
9. 执行如下命令，登录houyi_reg数据库。db_host、user、db_password、db_port、db_name的取值
请参见步骤7。

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

### 主备表配置不一致的订正方法

本文介绍MaxVersions或者TTL不一致、Stream开关不一致的订正方法。

**背景描述**

**MaxVersions或者TTL不一致**

一般是用户建表后，业务运行过程中，调整了MaxVersion或TTL配置。 如果主集群MaxVersions或TTL比备集群小（TTL的-1视为最大值，表示不过期），那么备集群上保留的数据更多，直接订正备的MaxVersions和TTL。 如果主集群MaxVersions或TTL比备集群大（TTL的-1视为最大值，表示不过期），那么备集群上可能已经存在数据不全的问题。需要确认是否需要重新全量同步一次，还是直接订正备集群配置。

**Stream开关不一致**

一般是主集群上Stream打开了（用于增量导出任务等），备集群上没有打开。直接订正备集群，打开 Stream功能。

**前提条件**

1. 登录ots集群的TableStore.PortalAgServer#终端机器。
2. 使用admin用户解压new_ots_replication_tool.tar.gz工具包。

**订正方法**

1. 进入 `new_ots_replication_tool` 目录。
2. 执行以下命令修改备集群配置。
灾备管理中心

**说明**

命令中需要指定实例名、表名，每次修改一个表的配置，仅修改备集群，不影响主集群。

```
./rep_checker.py sync_table_meta_for_secondary 实例名表名
```

执行结果示例：

```
$./rep_checker.py sync_table_meta_for_secondary lt-ots-test00 test001 secondary cluster: ots-ssd-B-20210813-00a6, table: _tBTC6DyGWKYBrHKstl#test001, set T TL to 86400000 OK!
```
