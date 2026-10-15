---
title: "云原生关系型数据库 PolarDB PolarDB MySQL主备版 用户指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 155
source_pdf: "70_PolarDB MySQL主备版 用户指南_user-guide-2.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/polardb/zh/user-guide-2.pdf"
converter: line-classifier (PyMuPDF)
---

# 云原生关系型数据库 PolarDB PolarDB MySQL主备版 用户指南

## 内核版本发布记录

本文为您介绍了PolarDB MySQL主备版的内核版本发布情况。

**说明**

详细更新点请参见《**Hotfix****版本说明书》**中**《云原生关系型数据库****PolarDB**》章节。

**发布日期：2026-07-30**

v3.18.6r-polardb-hotfeature-SP009提供PolarDB MySQL主备版最新内核版本：

| 产品版本 | 语法兼容 | 内核小版本 |
|---|---|---|
| MySQL主备版 | 5.7 | 5.7.0.0.33.3 |
|  | 8.0（兼容8.0和8.4） | 8.0.0.1.44.5 |

## 登录云原生数据库PolarDB控制台

本节以Chrome浏览器为例，介绍云产品用户如何登录到云原生数据库PolarDB。

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。

**说明**

单击页面右上角的当前语言可以切换其它语言。 授权登录是第三方认证中配置了全局IdP设置才会显示，且“授权登录”名称用户可按需自定义。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
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
5. 在页面顶部的菜单栏中，单击**产品** > **数据库** > **关系型数据库** > **云原生数据库****PolarDB**。
例规格

## 实例规格

实例有不同的系列、版本、规格，性能也有区别，本文介绍PolarDB MySQL的实例规格。

**说明**

ARM架构不支持5.7。

**通用规格与独享规格对比**

| 规格类型 | 特点 | 适用场景 |
|---|---|---|
| 独享规格 | 每个独享规格的集群独占所分配到的计算资源 （如CPU）。 不会与同一服务器上的其他集群共享计算资源，性能更加稳定可靠。 | 对性能稳定性要求高，以数据库为核心系统的业务场景，如金融、电商、政务和大中型互联网业务等。 |
| 通用规格 | 同一服务器上的不同集群，会互相充分利用彼此空闲的计算资源（如CPU）。 通过复用计算资源享受规模红利，性价比更高。 | 有降低成本诉求，追求高性价比的应用场景。 |

**主实例**

**双机高可用版**

| 规格族 | 支持版本 | 规格代码 | CPU和内存 | 最大 IOPS | 最大连接数 | 存储空间 |
|---|---|---|---|---|---|---|
|  | 5.7、 8.0 | rds.mysql.t1.small | 1核 1GB | 1200 | 300 | 5GB~2000GB |
|  | 5.7、8.0 | rds.mysql.s1.small | 1核 2GB | 2000 | 600 |  |
|  | 5.7、8.0 | rds.mysql.s2.large | 2核 4GB | 4000 | 1200 |  |
|  | 5.7、8.0 | rds.mysql.s2.xlarge | 2核 8GB | 6000 | 2000 |  |
|  | 5.7、8.0 | rds.mysql.s3.large | 4核 8GB | 8000 | 2000 |  |
|  | 8.0 | rds.mysql.m1.medi um | 4核 16GB | 14000 | 4000 |  |
|  |  |  |  |  |  | 文档版本：2026072 |

例规格

|  | 5.7、8.0 | rds.mysql.c1.large | 8核 16GB | 20000 | 4000 |  |
|---|---|---|---|---|---|---|
|  | 5.7、8.0 | rds.mysql.c1.xlarge | 8核 32GB | 28000 | 8000 |  |
|  | 5.7、8.0 | rds.mysql.g2.2xlarg e | 16核 32GB | 40000 | 8000 | 50 GB~3000 GB |
| 通用型 |  |  |  |  |  |  |
|  | 5.7、8.0 | rds.mysql.c2.xlarge | 16核 64GB | 40000 | 16000 | 5GB~3000GB |
|  | 5.7、8.0 | rds.mysql.c2.xlp2 | 16核 96GB | 40000 | 24000 |  |
|  | 5.7 | rds.mysql.c2.2xlarg e | 16核128GB | 16000 | 32000 |  |
|  | 5.7、8.0 | rds.mysql.g2.3xlarg e | 24核 48GB | 40000 | 12000 | 50 GB~3000 GB |
|  | 5.7、8.0 | rds.mysql.x2.3xlarg e | 24核 48GB | 50000 | 12000 | 50 GB~3000 GB |
|  | 5.7、8.0 | rds.mysql.g4.3xlarg e | 24核 96GB | 50000 | 24000 |  |
|  | 5.7、8.0 | rds.mysql.g2.4xlarg e | 32核 64GB | 60000 | 16000 |  |
|  | 5.7、8.0 | rds.mysql.g4.4xlarg e | 32核 128GB | 60000 | 32000 |  |
|  | 5.7、8.0 | rds.mysql.g2.8xlarg e | 64核 128GB | 60000 | 32000 |  |
|  |  | mysql.x4.large.2 | 4核 16GB | 30000 | 2500 | 50GB~1000GB |
|  |  | mysql.x8.large.2 | 4核 32GB | 40000 | 5000 |  |
|  |  | mysql.x4.xlarge.2 | 8核 32GB | 45000 | 5000 | 500GB~3000G B |
|  |  | mysql.x8.xlarge.2 | 8核 64GB | 50000 | 10000 |  |

例规格

|  |  | mysql.x4.2xlarge.2 | 16核 64GB | 60000 | 10000 | 500 GB~3000 GB |
|---|---|---|---|---|---|---|
| 独享型 | 5.7、8.0 |  |  |  |  |  |
|  |  | mysql.x4.4xlarge.2 | 32核 128GB | 80000 | 20000 | 1000GB~6000G B |
|  |  | rds.mysql.x2.2xlarg e | 16核 32GB | 40000 | 8000 | 50 GB~2000 GB |
|  |  | rds.mysql.x4.3xlarg e | 24核 96GB | 50000 | 24000 |  |
|  |  | rds.mysql.x2.4xlarg e | 32核 64GB | 60000 | 16000 | 50 GB~3000 GB |
|  |  | rds.mysql.x4.4xlarg e | 32核 128GB | 60000 | 32000 |  |
|  |  | rds.mysql.x2.8xlarg e | 64核 128GB | 60000 | 32000 |  |
|  |  | mysql.x8.medium.2 | 2核 16GB | 15000 | 2500 | 50GB~1000GB |
|  |  | mysql.x8.large.2 | 4核 32GB | 40000 | 5000 |  |
|  |  | mysql.x8.xlarge.2 | 8核 64GB | 50000 | 10000 | 500GB~3000G B |
|  |  | mysql.x8.2xlarge.2 | 16核 128GB | 60000 | 20000 |  |
|  |  | mysql.x8.4xlarge.2 | 32核 256GB | 100000 | 40000 | 1000GB~6000G B |
|  |  | mysql.x8.8xlarge.2 | 64核 512GB | 150000 | 80000 |  |

### 只读实例

| 规格族 | 支持版本 | 规格代码 | CPU和内存 | 最大连接数 | 存储空间 |
|---|---|---|---|---|---|
|  |  | rds.mysql.t1.small | 1核 1GB | 300 |  |

| 云原生数据库 |  | PolarDB MySQ |  |  | L主备版用户指南·实例规格 |
|---|---|---|---|---|---|
| 通用型 | 5.7、8.0 |  |  |  | 5GB~2000GB |
|  |  | rds.mysql.s1.small | 1核 2GB | 600 |  |
|  |  | rds.mysql.s2.large | 2核 4GB | 1200 |  |
|  |  | rds.mysql.s2.xlarge | 2核 8GB | 2000 |  |
|  |  | rds.mysql.s3.large | 4核 8GB | 2000 |  |
|  |  | rds.mysql.m1.medium | 4核 16GB | 4000 |  |
|  |  | rds.mysql.c1.large | 8核 16GB | 4000 |  |
|  |  | rds.mysql.c1.xlarge | 8核 32GB | 8000 |  |
|  |  | rds.mysql.c2.xlarge | 16核 64GB | 16000 | 5GB~3000GB |
|  |  | rds.mysql.c2.xlp2 | 16核 96GB | 24000 |  |
| 独享型 | 5.7、8.0 | mysqlro.x8.medium.1 | 2核 16GB | 2500 | 50GB~1000GB |
|  |  | mysqlro.x4.large.1 | 4核 16GB | 2500 |  |
|  |  | mysqlro.x8.large.1 | 4核 32GB | 5000 |  |
|  |  | mysqlro.x4.xlarge.1 | 8核 32GB | 5000 |  |
|  |  | mysqlro.x8.xlarge.1 | 8核 64GB | 10000 | 500GB~3000G B |
|  |  | mysqlro.x4.2xlarge.1 | 16核 64GB | 10000 |  |
|  |  | mysqlro.x8.2xlarge.1 | 16核 128GB | 20000 |  |
|  |  | mysqlro.x4.4xlarge.1 | 32核 128GB | 20000 |  |
|  |  | mysqlro.x8.4xlarge.1 | 32核 256GB | 40000 | 1000GB~6000 GB |
|  |  | mysqlro.x8.8xlarge.1 | 64核 512GB | 80000 |  |

速入门

## 快速入门

### 使用限制

为保障实例的稳定及安全，PolarDB MySQL有部分使用上的约束，详情如下表所示：

| 约束项 | 使用约束 |
|---|---|
| 实例参数 | 大部分实例参数可以在PolarDB MySQL版专有云控制台或使用API进行修改。出于安全和稳定性考虑，部分参数不支持修改。 |
| 数据库root权限 | 不提供root或者sa权限。 |
| 数据库备份 | 可使用命令行或图形界面进行逻辑备份。 仅限通过PolarDB MySQL版专有云控制台或API进行物理备份。 |
| 数据库还原 | 可使用命令行或图形界面进行逻辑数据还原。 仅限通过PolarDB MySQL版专有云控制台或API进行物理还原。 |
| 搭建数据库复制 | PolarDB MySQL本身提供主备复制架构的双节点集群，无需您手动搭建。其中主备复制架构集群的备（slave）实例不对您开放，您的应用不可直接访问。 |
| 重启PolarDB实例 | 必须通过PolarDB MySQL版专有云控制台或API重启实例。 |
| 账号和数据库管理 | 默认需要通过PolarDB MySQL版专有云控制台进行账号和数据库管理。同时，MySQL也支持您通过创建高权限账号的方式来自行管理用户、密码和数据库。 |
| 普通账号 | 不可以进行授权。 控制台有账号管理和数据库管理的界面。 支持创建普通账号的实例也支持创建高权限账号。 |
| 高权限账号 | 可以为普通账号授权。 PolarDB MySQL版专有云控制台上账号管理和数据库管理的界面消失，相关操作只能通过代码进行。 开通高权限账号后无法回退。 |

### 使用流程

快速使用PolarDB MySQL版的基本流程包括创建PolarDB MySQL版实例、设置白名单、创建数据库、创建账号、连接实例。本章节向您介绍使用PolarDB MySQL版的基本步骤，旨在引导您一站式完成PolarDB MySQL版实例的搭建。 通常，从创建实例到可以开始使用实例，您需要完成以下操作： 速入门

### 1. 创建实例

实例是虚拟化的数据库服务器，您可以根据业务需求创建合适的实例。您可以在一个实例中创建和管理多个数据库。

### 2. 设置白名单

为保障数据库的安全稳定性，创建PolarDB MySQL版实例后，您需要将待访问实例的IP地址或IP段加入白名单中，以允许外部设备访问该实例。 白名单可以使得PolarDB MySQL版实例得到高级别的访问安全保护，建议您定期维护白名单。设置白名单不会影响实例的正常运行。
3. 创建数据库和创建账号

### 4. 通过DMS登录PolarDB数据库

完成创建实例、设置白名单、创建数据库和账号等操作后，您可以使用通用数据库客户端连接到PolarDB 实例。

### MySQL 8.4的兼容性说明

为响应社区安全演进，PolarDB MySQL版采用统一自研内核，通过不同的启动参数同时兼容MySQL 8.0与 MySQL 8.4。在完全兼容MySQL 8.0的基础上，对MySQL 8.4提供了**有限兼容**：支持其安全修复和内核参数配置，但暂不支持MySQL 8.4新增的语法、关键字、权限及内核特性。控制台中大版本统一显示为PolarDB MySQL 8，具体小版本（8.0或8.4）可通过控制台或API查询确认。

**安全保障（支持）**

所有MySQL高危/严重级别CVE漏洞均经评估。若涉及到PolarDB内核，将给出修复方案或补丁；若不涉及将仅作澄清。

**内核参数（支持）**

管控类语法未对用户开放，不涉及兼容性问题。 支持通过控制台或API配置与MySQL 8.4一致的内核参数 （如 `innodb_io_capacity` 、 `gtid_mode` 等）。 参数行为与官方MySQL 8.4保持一致，支持业务调优。

**新增语法与特性（不支持）**

PolarDB MySQL版对MySQL 8.4新语法、新关键字、新系统函数等上层特性暂不兼容，具体如下：

|  | 类别 |  | MySQL 8.4新增能力 |  |  | PolarDB MySQL 8.4兼容状态 |
|---|---|---|---|---|---|---|
|  | 新关键字 |  | AUTO , BERNOULLI , GTIDS , LOG , MANUAL , PARA LLEL , PARSE TREE , QUALIFY , S3 , TABLESAMPLE _ 等（可用反引号引用） |  |  | 不支持 |
|  | 新权限 |  | TRANSACTION GTID TAG , FLUSH PRIVILEGES , OPTIMIZ _ _ _ E LOCAL TABLE , SET ANY DEFINER , ALLOW NONEXISTENT _ _ _ _ _ DEFINER _ |  |  | 不支持 |
|  |  |  |  | TRANSACTION GTID TAG _ _ |  |  |
|  |  |  | E LOCAL TABLE _ _ |  |  |  |
|  |  |  | DEFINER _ |  |  |  |

|  |  | AUTO |
|---|---|---|
|  | LLEL |  |

| PARA |  |
|---|---|

| FLUSH PRIVILEGES _ |  |
|---|---|

| OPTIMIZ |  |
|---|---|
|  | 不支持 |

速入门

|  | GTID增强 |  | 带标签GTID格式 UUID:TAG:NUMBER ； gtid next='AUTOMATIC:mytag' 语 _ 法 |  |  | 不支持 |
|---|---|---|---|---|---|---|
|  | EXPLAIN增强 |  | EXPLAIN ... FOR SCHEMA schema name 、 EXPLAIN _ FORMAT=JSON INTO @var 、 explain json format version 变量 _ _ _ |  |  | 不支持 |
|  |  |  |  | EXPLAIN ... FOR SCHEMA schema name _ |  |  |
|  |  | IN增强 | FORMAT=JSON INTO |  |  |  |
|  |  |  | @var |  |  |  |
|  | mysqldump 增强 |  | --output-as-version 选项生成旧版复制术语 |  |  | 不支持 |
|  | 直方图 |  | ANALYZE TABLE ... UPDATE HISTOGRAM ... AUTO UPDATE |  |  | 不支持 |

| EXPLAIN |  |
|---|---|

**使用建议**

若当前使用MySQL 8.0，可无缝迁移至PolarDB MySQL 8.4版，完全兼容。 若计划使用MySQL 8.4，PolarDB可提供同等安全能力，但请避免使用8.4的新增语法或新增特性。 建议以MySQL 8.0为兼容基准进行应用开发、测试与生产部署，确保稳定性与兼容性。

**相关操作**

**创建8.4内核实例**

可参见创建实例教程，创建内核版本为8.4的PolarDB MySQL实例，并在新建实例时完成以下两项关键配置： 语法兼容：选择8**（兼容****8.0**和**8.4**）。 参数模板：选择 `mysql_innodb_8.4_standard_normal_safe` 。

**查看实例内核小版本**

**方法一：通过控制台查看**

访问**实例列表**页面或进入实例详情页，查看实例语法兼容大版本和语法兼容小版本。 速入门

**方法二：通过API查看**

通过API（DescribeDBInstances或DescribeDBInstanceAttribute）查看实例语法兼容大版本和语法兼容小版本。 返回字段将显示EngineVersion为8.4，grammarCompatibilityVersion为8.4.6。 例管理

## 实例管理

### 创建实例

本文介绍如何通过云原生数据库PolarDB专有云控制台创建PolarDB MySQL实例。

**前提条件**

在创建实例前，请先申请可以登录阿里云控制台的账号。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击左上角的**创建实例**。
3. 设置如下参数。

| 类别 | 配置 | 说明 |
|---|---|---|
| 基本信息 | 组织 | 实例所属组织。 |
|  | 资源集 | 实例所属资源集。 |
|  | 地域 | 实例所属地域。不同地域之间的产品内网不互通，创建实例后不支持更换地域。 |
|  | 部署方案 | 实例部署方案，目前支持单可用区部署和多可用区部署两种方案。 |
|  | 主节点可用区 | 实例主节点所属可用区。 |
|  | 备节点可用区 | 实例备节点所属的可用区。 说明仅当部署方案选择多可用区部署时，需要配置该选项。 |
|  | 芯片架构 | 实例所属主机的芯片架构。 |
|  | 数据库类型 | 选择MySQL 语法兼容。 |

| 原生数据库 |  |  |
|---|---|---|
| 规格配置 |  |  |
|  | 语法兼容 | 选择与MySQL兼容的内核版本。 5.7 8（兼容8.0和8.4） 重要选项中的“8.4”表示PolarDB自研数据库引擎对MySQL 8.4功能特性的兼容实现，并非基于原生MySQL 8.4版本。具体详情，请参见MySQL 8.4的兼容性说明。 |
|  | 参数模板 | 本参数仅当语法兼容配置项为8（兼容8.0和8.4）时可配置。 重要如需创建内核版本为8.4的集群，请务必将参数模板配置为 mysql innodb 8.4 standard normal safe 。若下拉选项中未显示 _ _ _ _ _ 该模板，请先参见《运维指南》中“开启PolarDB MySQL 8.4内核参数开关”教程，在Apsara Uni-manager运维控制台启用对应开关，启用后返回本页面刷新即可正常选择。若无运维平台操作权限，请联系阿里云技术支持协助开启。 |
|  | 展示数据库小版本的数量 | 展示的小版本个数，可指定数据库的内核小版本，不指定表示创建最新内核小版本。 重要若控制台未显示相关配置项，请先参见《运维指南》中“开启PolarDB指定内核小版本开关”教程，在Apsara Uni-manager运维控制台启用对应开关，启用后返回本页面刷新即可正常选择。若无运维平台操作权限，请联系阿里云技术支持协助开启。 |
|  | 数据库小版本 |  |
|  | 表名大小写 | 设置数据库表名是否区分大小写。默认为不区分大小写。 说明若您本地数据库区分大小写时，建议您与本地数据库保持一致，选择区分大小写，便于您后续进行数据迁移等其他操作。 默认为不区分大小写仅支持MySQL 8（兼容8.0和8.4）实例。 实例创建后不支持修改，请谨慎选择。 |
|  | 系列 | 数据库的系列，目前支持双机高可用版本和只读实例两种系列。 |
|  | 存储类型 | 数据库的存储类型，固定为本地SSD。 |

例管理

|  | 实例规格 | 实例的规格，不同的内存大小对应不同的最大连接数和IOPS，具体请以控制台界面为准。 |
|---|---|---|
|  | 存储空间 | 存储空间包括数据空间、系统文件空间、Binlog文件空间和事务文件空间。实际可用存储空间请以控制台界面为准。 |
| 网络 | 网络连接类型 | 实例支持的网络连接类型。目前支持公网连接和内网连接两种。 |
|  | 网络类型 | 实例支持的网络类型： 经典网络：经典网络中的云服务在网络中不进行隔离，只能依靠云服务自身的安全组或白名单策略来阻挡非法访问。 专有网络：（Virtual Private Cloud，简称VPC）专有网络帮助用户在阿里云上构建出一个隔离的网络环境。用户可以自定义专有网络里的路由表、IP地址范围和网关。建议您选择专有网络，更加安全。 说明选择专有网络后，需要选择对应的专有网络VPC和交换机VSwitch。 |
|  | IP类型 | IPv4：仅分配IPv4地址，适用于纯IPv4网络环境。 IPv4/v6双栈：同时分配IPv4和IPv6地址，适用于需要同时支持IPv4与IPv6客户端访问的混合网络场景。启用后需配置IPv6白名单以控制IPv6地址的访问权限。 说明如需配置该项参数需开启IPV6开关，具体操作，请参见《运维指南》中开启PolarDB IPv6开关章节。 如果提示未授权等信息，请参见租户组织对SLB服务授权操作。 |
|  | IP白名单 | 添加IP地址，允许这些IP地址访问该PolarDB实例。 说明 IP类型为IPv4/v6双栈时，IPv6白名单配置项可见且需配置。 |
|  | IPv6白名单 |  |
|  | 创建数量 | 创建的实例数量。 |

| 原生数据库 | PolarDB MySQL主备版用户指南·实例管理 |  |
|---|---|---|
| 实例设置 |  |  |
|  | 实例名称 | 实例的名称。实例名称需满足如下要求： 以字母或中文开头，支持数字、“:”、“ ”和“-”特殊字符。 _ 长度为2~64个字符。 不能以 http:// 或 https:// 开头。 |

4. 在最终创建实例前，请在页面右侧**配置概览**面板检查实例的整体配置，确保符合您的要求。
您可以单击右侧**配置概览**面板的**保存为配置模板**，将创建实例所需的配置参数保存为配置模板。后续创建实例时，可以使用指定的模板快速创建实例，省去逐一配置参数的复杂流程。 如果配额不足，可单击**管理**进行配置。具体操作，请参见**《统一云管平台****用户指南》**中的**《配额管**
**理》**章节。
5. 完成上述操作后，单击**提交**。

### 查看实例基本信息

您可以查看实例的基本信息、内网连接信息、运行状态、配置信息等详情。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 您可以通过如下两种方式进入实例**基本信息**页面：
在**实例列表**页面，单击目标实例的ID，进入实例**基本信息**页面。 在**实例列表**页面，单击目标实例所对应**操作**栏中的**管理**，进入实例**基本信息**页面。

### 重启实例

当实例出现连接数满或性能问题时，您可以手动重启实例。

**前提条件**

实例必须处于**运行中**状态。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 单击右上角的**重启实例**。

**说明**

重启实例会造成连接中断，因此在重启前请做好业务安排，谨慎操作。
4. 在弹出的窗口中，单击**确定**。

### 变更配置

如果当前实例配置无法满足应用的要求，或者当前实例的配置过高或者过低，您可以变更实例的配置，例如规格、存储空间。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
例管理
2. 在**实例列表**页面，单击目标实例ID。
3. 在**基本信息**页面的**配置信息**区域，单击**变更配置**。
4. 在**PolarDB****变配**页面，选择**系列**、**存储类型**、**实例规格**、**存储空间**和**变配时间**。
5. 完成参数配置后，单击**提交**。

### 设置可维护时间段

您可以根据业务需求设置PolarDB MySQL版实例的可运维时间段。

**背景信息**

为保障PolarDB MySQL版实例的稳定性，后端系统会不定期对实例进行维护操作。默认可维护时间段为 02:00~06:00，您可以根据业务规律将可维护时间段设置在业务低峰期，以避免维护过程中可能对业务造成的影响。

**注意事项**

实例维护当天，为保障整个维护过程的稳定性，实例会在可维护时间段之前进入**实例维护中**的状态。当实例处于该状态时，对数据库的访问以及查询类操作（如性能监控）不会受到任何影响，但除了账号管理、 在可维护时间段内，实例会发生1到2次连接闪断，请确保应用程序具有重连机制。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击实例ID或选择**操作** > **管理**。
3. 在**配置信息**区域，单击**可维护时间段**后的**设置**。
4. 选择一个可维护时间段，单击**确定**。

**说明**

时间段为北京时间。

### 修改数据复制方式

您可以根据自身业务特点，设置PolarDB MySQL版的主备实例之间的数据复制方式，以提高云数据库的可用性。

**背景信息**

半同步应用发起的更新在主实例执行完成后，会将日志同步传输到所有备库，当集群中的至少一个节点收到日志后，不需要等待节点执行日志内容，事务就算完成了提交。 当备实例不可用或者主备实例间出现网络异常时，半同步会退化为异步。 例管理异步应用发起更新请求，即进行增加、删除、修改数据的操作时，主实例完成操作后会立即响应应用，同时主实例向备实例异步复制数据。因此，在异步数据复制方式下，备实例不可用时不会影响主实例上的操作， 而主实例不可用时会引起主备库数据不一致的概率较低。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID。
3. 在左侧导航栏中，单击**服务可用性**。
4. 单击**修改数据复制方式**。
5. 在弹出的对话框中，选择数据复制方式，单击**确定**。

### 释放实例

您可以根据业务需求手动释放实例。

**注意事项**

只有在运行状态下的实例才能被手动释放。 释放后，实例立即被清除，数据不再保留，请提前备份数据。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例对应操作栏中的**释放实例**。
3. 在弹出的**释放实例**对话框中，单击**释放**。
例管理

**说明**

支持实例释放保护，删除PolarDB MySQL实例，需输入MFA动态码。具体操作配置，请参见《统一云管平台》用户指南中的风险操作设置章节，在配置页风险操作设置界面完成配置。

### 升级内核小版本

PolarDB MySQL版实例支持自动升级或手动升级内核小版本，内核小版本的升级涉及性能提升、新功能或问题修复等。

**功能介绍**

PolarDB MySQL版实例默认自动升级内核小版本，您可以在**基本信息**页面看到**小版本自动升级**的设置情况。
**自动升级**：每次重新登录实例控制台并查看实例基本信息时，系统会发起内核小版本的查询。若环境上有
新的内核小版本发布，则会触发自动升级，自动升级操作将会在您设置的可维护时间段内进行，设置可维
**手动升级**：每次重新登录实例控制台并查看实例基本信息时，系统会发起内核小版本的查询。若环境上有
新的内核小版本发布，系统不会自动升级小版本，您可以在实例的**基本信息**页面手动升级内核小版本。

**注意事项**

升级内核小版本会重启实例，PolarDB MySQL服务可能会出现一次30秒的闪断，请您尽量在业务低峰期执行升级操作，或确保您的应用有自动重连机制。 如果执行了升配等操作，实例会升级到新的内核小版本。

**修改自动升级设置**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在**配置信息**区域，单击**小版本自动升级**右侧的**设置**。
4. 选择**自动升级**或**手动升级**，单击**确定**。
1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在**配置信息**区域右侧单击**升级内核小版本**。
例管理

**说明**

4. 在弹出的对话框中，选择升级时间，单击**确定**。

**常见问题**

升级内核小版本是阿里云的内核小版本，不是MySQL的内核版本。您可以使用 `SHOW VARIABLES LIKE` '%polardb_version%' 查询您的内核小版本。 升级是直接升级到最新小版本。

### 实例回收站

实例进入回收站后，您可以在回收站中重建或销毁实例。

**重建实例**

1. 登录云原生数据库PolarDB控制台。
2. 在页面左上方选择实例所在的组织，单击左侧导航栏的**回收站**。
3. 找到被释放的实例，单击右侧操作列的**重建恢复**。
4. 在跳转的实例恢复页面，配置**区域**、**规格配置**和**网络类型**等实例信息，单击**提交**。

**说明**

如果**网络类型**为**专有网络**，则还需配置专有网络**VPC**和交换机**VSwitch**。 其他配置项默认与源实例一致，无法更改。

**销毁实例**

您可以在回收站中销毁不再使用的实例。

**警告**

销毁实例会同时销毁该实例的所有备份，包括常规数据备份、归档备份和日志备份且无法恢复，请谨慎操作。
1. 登录云原生数据库PolarDB控制台。
2. 在页面左上方选择实例所在的组织，单击左侧导航栏的**回收站**。
3. 找到目标实例，单击**立即销毁**，并在弹出的窗口中单击**确定**。

### 只读实例

#### 概述

PolarDB MySQL版的实例支持添加只读实例，在对数据库有大量读请求和少量写请求时，只读实例用于分担主实例的数据库压力。本章节主要介绍只读实例的功能特点以及功能限制。 例管理为了实现读取能力的弹性扩展，分担数据库压力，您可以在某个地域中创建一个或多个只读实例，利用只读实例满足大量的数据库读取需求，以此增加应用的吞吐量。 只读实例必须跟主实例在同一地域，但可以在不同的可用区。只读实例拓扑图如下所示：

| 云服务器 ECS 读写请求只读请求主备同步 PolarDB主实例 PolarDB备实例 PolarDB只读实例 PolarDB只读实例 PolarDB只读实例 |  |
|---|---|
| 主备 PolarDB主实例 PolarDB备实例 | PolarDB只读实例 PolarDB只读实例 PolarDB只读实例 |

PolarDB主实例 PolarDB只读实例
**只读实例有如下功能特点**：
规格可以与主实例不一致，并可以随时更改规格（没有时间限制），便于弹性升降级。 不需要维护账号与数据库，全部通过主实例同步。 独立的白名单配置。 提供系统性能监控。 PolarDB提供近20个系统性能的监控视图。例如磁盘容量、IOPS、连接数、CPU利用率、网络流量等。 用户可以轻松查看实例的负载。 提供优化建议：PolarDB提供多种优化建议。例如存储引擎检查、主键检查、大表检查、索引偏多、缺失索引等。用户可以根据优化建议并结合自身的应用来对数据库进行优化。

#### 创建只读实例

您可以通过创建不同规格的只读实例来满足业务需要。

**前提条件**

实例版本为双机高可用版（本地SSD盘）。

**注意事项**

1个主实例最多可以创建5个只读实例。 只读实例不支持备份设置以及临时备份。 只读实例不支持实例恢复。 只读实例不支持将数据迁移至只读实例。 只读实例不支持创建账号、删除账号、账号授权以及修改账号密码。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
例管理
3. 在**基本信息**页面的**实例分布**区域，单击只读实例右侧的**添加**。
4. 在**PolarDB****创建只读实例**页面设置只读实例的参数。

| 项目 | 参数 | 说明 |
|---|---|---|
| 区域 | 地域 | PolarDB实例所在地域。 |
| 规格配置 | 数据库类型 | 只读实例的数据库类型，与主实例一致，不可修改。 |
|  | 数据库版本 | 只读实例的数据库版本，与主实例一致，不可修改。 |
|  | 系列 | 固定为只读实例。 |
|  | 存储类型 | 只读实例的存储类型。 |
|  | 实例规格 | 只读实例规格。可以与主实例不一致，并且只读实例可以随时更改规格，便于弹性升降级。 |
|  | 存储空间 | 只读实例的存储空间，为保证数据同步有足够的I/O性能支撑，建议只读实例的规格和存储空间不小于主实例。 |
| 网络类型 | 网络类型 | 只读实例的网络类型，与主实例一致，不可修改。 |
|  | IP类型 | IPv4：仅分配IPv4地址，适用于纯IPv4网络环境。 IPv4/v6双栈：同时分配IPv4和IPv6地址，适用于需要同时支持 IPv4与IPv6客户端访问的混合网络场景。启用后需配置IPv6白名单以控制IPv6地址的访问权限。 |
|  | 专有网络vpc | 网络类型为专有网络时，您需要选择对应的VPC。 |
|  | 交换机vswitch | 网络类型为专有网络时，您需要选择对应的交换机。 |

5. 完成上述参数配置后，单击**提交**。

#### 查询只读实例详情

本章节介绍如何查询只读实例详情。您可以通过实例列表页面直接进入只读实例的管理页面，也可以通过主实例的只读实例列表进入只读实例的管理页面。管理方式与常规实例的管理类似，可执行的管理操作请以实际界面为准。

**直接通过只读实例查询实例详情**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标只读实例的ID，进入实例的**基本信息**页面。
例管理在实例列表中，**实例类型**为**只读实例**的就是只读实例。

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在**基本信息**页面，将鼠标移动到**实例分布**窗口中的**只读实例**的数字上，就会显示只读实例ID。
4. 单击只读实例ID，即可进入只读实例的基本信息页面。

### 标签管理

在实例数量较多的情况下，您可以创建多个标签，为实例绑定不同的标签对其进行分类，之后通过标签进行实例筛选。

**绑定标签**

1. 登录云原生数据库PolarDB控制台。
2. 在左侧导航栏单击实例列表。
3. 在**实例列表**页面，将鼠标移动到目标实例**标签**栏的
图标上。
4. 在**编辑标签**页面单击+**添加。**
5. 输入**标签键**与输入**标签值。**
6. 单击**确定。**

**根据标签筛选实例**

1. 登录云原生数据库PolarDB控制台。
2. 在左侧导航栏单击实例列表。
3. 在**实例列表**页面，将鼠标移动到目标实例**标签**栏的
图标上。
4. 单击**标签管理。**
5. 单击+**创建**/**选择标签并绑定资源**，选择目标标签。
6. 单击**下一步。**
7. 选择目标实例**资源所在的组织和资源集，**选择目标实例**资源所在区域，**选择目标实例所对应的**云产品。**
8. 单击**下一步。**
9. 单击**确认。**

**查看实例绑定的标签**

1. 登录云原生数据库PolarDB控制台。
2. 在左侧导航栏单击实例列表。
3. 在**实例列表**页面，将鼠标移动到目标实例**标签**栏的
图标上。 例管理

**解绑标签**

1. 登录云原生数据库PolarDB控制台。
2. 在左侧导航栏单击实例列表。
3. 在**实例列表**页面，将鼠标移动到目标实例**标签**栏的
图标上。
4. 在**编辑标签**页面，将鼠标移动到**标签值**后的图标
上。
5. 单击**确定。**
数配置

## 参数配置

### 设置实例参数

您可以通过PolarDB控制台查看和修改部分参数的值，并追溯参数变更历史。

**注意事项**

为保障实例稳定性，控制台仅开放部分参数的修改权限。 修改参数值前，请参考**可修改参数**页面中的**可修改参数值**列。 部分参数修改后需重启实例，具体请参见控制台上**可修改参数**页面中的**是否重启**列。建议您在业务低峰期操作，并确保应用程序具有重连机制。

**修改参数值**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**参数设置**。
4. 在该页面，您可进行如下操作：

**导出参数**

单击**导出参数**会以TXT格式将该实例的所有参数值保存到本地。

**批量修改参数文件并导入参数**

a. 导出的参数文件修改完成后，可以单击**导入参数**，将参数文件内容粘贴到对话框中。 b. 单击**确定**。 c. 单击页面中的**提交参数**。

**说明**

如果修改的参数需要重启实例才能生效，系统会提示您是否重启，建议您在业务低峰期操作，并确保应用程序具有重连机制。 参数的修改未提交时，如果想取消修改，请单击**撤销**。

**修改单个参数**

a. 在**可修改参数**列表内找到需要修改的参数，单击**运行参数值**列的 。 b. 根据提示的取值范围输入参数值，单击**确定**。 c. 单击页面中的**提交参数**。

**说明**

如果修改的参数需要重启实例才能生效，系统会提示您是否重启，建议您在业务低峰期操作，并确保应用程序具有重连机制。 参数的修改未提交时，如果想取消修改，请单击**撤销**。

**查看参数修改历史**

## 1. 登录云原生数据库PolarDB控制台

数配置
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**参数设置**。
4. 切换至**参数修改历史**页签下，选择时间范围并单击**确定**。

**参数说明**

| 参数名称 | 默认值 | 推荐值 | 是否重启 | 参数值范围 | 参数描述 |
|---|---|---|---|---|---|
| auto increme _ nt increment _ | 1 | 1 | 否 | [1-65535] | 设置自增列的步长，影响自增 ID的递增间隔。 |
| auto increme _ nt offset _ | 1 | 1 | 否 | [1-65535] | 设置自增列的起始值，用于分布式主从复制场景。 |
| autocommit | ON | ON | 否 | [ON\|OFF] | 控制自动提交模式，ON表示每次SQL语句后自动提交，OFF则需手动提交。 |
| automatic sp _ privileges _ | ON | ON | 否 | [ON\|OFF] | 自动为存储过程分配权限，ON 表示启用，OFF 表示禁用。 |
| avoid tempor _ al upgrade _ | OFF | OFF | 否 | [ON\|OFF] | 避免时间类型升级，ON表示禁止升级，OFF表示允许。 |
| back log _ | 3000 | 3000 | 是 | [0-65535] | 等待连接请求的队列长度生效。 |
| binlog cache _ _ size | 2097152 | 128KB | 否 | [4096- 16777216] | 二进制日志缓存大小，用于事务性语句的临时存储。 |
| binlog checks _ um | CRC32 | CRC32 | 是 | [CRC32\|NONE ] | 二进制日志校验算法，CRC32 表示使用 CRC32校验。 |

数配置

| binlog order _ _ commits | ON | ON | 否 | [ON\|OFF] | 按提交顺序写入二进制日志，ON表示启用，OFF表示禁用。 |
|---|---|---|---|---|---|
| binlog row im _ _ age | full | full | 否 | [full\|minimal] | 行模式二进制日志的记录方式，full表示记录完整行数据。 |
| binlog rows q _ _ uery log eve _ _ nts | OFF | OFF | 否 | [ON\|OFF] | 是否记录行级变更的查询事件，OFF表示禁用。 |
| binlog stmt c _ _ ache size _ | 32768 | 32768 | 否 | [4096- 16777216] | 非事务性语句的二进制日志缓存大小。 |
| block encrypt _ ion mode _ | "aes-128- ecb" | "aes-128- ecb" | 否 | ["aes-128- ecb"\|"aes- 192- ecb"\|"aes-2... | 数据块加密算法，如AES- 128-ECB。 |
| bulk insert b _ _ uffer size _ | 4194304 | 4194304 | 否 | [0- 4294967295] | 批量插入数据时的缓冲区大小。 |
| character set _ filesystem _ | binary | binary | 否 | [utf8\|latin1\|g bk\|binary] | 文件系统字符集，binary表示二进制处理。 |
| character set _ server _ | utf8 | utf8 | 是 | [utf8\|latin1\|g bk\|gb18030\|u tf8mb4] | 服务器默认字符集生效。 |
| concurrent in _ sert | 1 | 1 | 否 | [0\|1\|2] | 并发插入策略，0表示禁止，1表示允许，2表示仅允许末尾插入。 |
| connect time _ out | 10 | 10 | 否 | [1-3600] | 连接超时时间 （秒），用于客户端连接等待。 |
| default stora _ ge engine _ | InnoDB | InnoDB | 是 | [InnoDB\|inno db] | 默认存储引擎，InnoDB表示使用 InnoDB。 |

数配置

| default time _ _ zone | SYSTEM | Asia/Shanghai | 是 | [SYSTEM\|- 12:00\|- 11:00\|- 10:00\|-9:00\|... | 服务器默认时区，SYSTEM表示使用系统时区。 |
|---|---|---|---|---|---|
| default week _ _ format | 0 | 0 | 否 | [0-7] | 周格式设置，0 表示周日为一周开始。 |
| delay key wri _ _ te | ON | ON | 否 | [ON\|OFF\|ALL] | 延迟索引写入策略，ON表示启用延迟写入。 |
| delayed inser _ t limit _ | 100 | 100 | 否 | [1- 4294967295] | 延迟插入的最大行数，超过后强制写入。 |
| delayed inser _ t timeout _ | 300 | 300 | 否 | [1-3600] | 延迟插入超时时间（秒）。 |
| delayed queu _ e size _ | 1000 | 1000 | 否 | [1- 4294967295] | 延迟插入队列的最大容量。 |
| disconnect on _ expired pass _ _ word | ON | ON | 是 | [ON\|OFF] | 密码过期后断开连接，ON表示启用。 |
| div precision _ _ increment | 4 | 4 | 否 | [0-30] | 除法精度增加值，控制浮点运算精度。 |
| end markers _ _ in json _ | OFF | OFF | 否 | [ON\|OFF] | JSON数据中的结束标记，OFF 表示禁用。 |
| eq range ind _ _ ex dive limit _ _ | 100 | 100 | 否 | [0- 4294967295] | 等值范围查询的索引深入限制。 |
| explicit defau _ lts for timest _ _ amp | OFF | OFF | 否 | [ON\|OFF] | 显式定义时间戳默认值，OFF表示自动处理。 |
| flush time _ | 0 | 0 | 否 | [0-31536000] | 表缓存刷新时间 （秒），0表示禁用。 |

数配置

| ft max word l _ _ _ en | 84 | 84 | 是 | [10- 4294967295] | 全文索引最大单词长度 。 |
|---|---|---|---|---|---|
| ft min word l _ _ _ en | 4 | 4 | 是 | [1-3600] | 全文索引最小单词长度 。 |
| ft query expa _ _ nsion limit _ | 20 | 20 | 是 | [0-1000] | 查询扩展限制， 控制自然语言搜索结果。 |
| general log _ | OFF | OFF | 是 | OFF | 通用查询日志开关，OFF表示禁用。 |
| group concat _ max len _ _ | 1024 | 1024 | 否 | [4- 18446744073 70954752] | GROUP CONC _ AT函数的最大返回长度。 |
| host cache si _ _ ze | 644 | 644 | 否 | [0-65535] | 主机缓存大小， 用于存储连接信息。 |
| innodb adapti _ ve flushing _ | ON | ON | 否 | [ON\|OFF] | 自适应刷新策略，ON表示启用。 |
| innodb adapti _ ve flushing l _ _ wm | 10 | 10 | 否 | [0-70] | 自适应刷新低水位线，控制刷新频率。 |
| innodb adapti _ ve hash inde _ _ x | OFF | OFF | 否 | [ON\|OFF] | 自适应哈希索引，OFF表示禁用。 |
| innodb adapti _ ve max sleep _ _ delay _ | 150000 | 150000 | 否 | [1-1000000] | 自适应睡眠延迟最大值（微秒）。 |
| innodb autoe _ xtend increm _ ent | 64 | 64 | 否 | [1-1000] | 表空间自动扩展步长（页数）。 |
| innodb autoin _ c lock mode _ _ | 2 | 2 | 是 | [0\|1\|2] | 自增锁模式，0 表示传统模式，1表示交错模式，2表示无锁模式。 |

数配置

| innodb buffer _ pool dump a _ _ _ t shutdown _ | ON | ON | 否 | [ON\|OFF] | 关闭时转储缓冲池内容，ON表示启用。 |
|---|---|---|---|---|---|
| innodb buffer _ pool dump p _ _ _ ct | 25 | 25 | 否 | [1-100] | 缓冲池转储百分比。 |
| innodb buffer _ pool instanc _ _ es | {LEAST(DBIns tanceClassMe mory/107374 1824, 8)} | {LEAST(DBIns tanceClassMe mory/107374 1824, 8)} | 是 | [1-64] | 缓冲池实例数， 影响并发性能。 |
| innodb buffer _ pool load at _ _ _ startup _ | ON | ON | 是 | [ON\|OFF] | 启动时加载缓冲池内容，ON表示启用。 |
| innodb chang _ e buffer max _ _ size _ | 25 | 25 | 否 | [0-50] | 变更缓冲区最大大小（百分比）。 |
| innodb chang _ e buffering _ | all | all | 否 | [none\|inserts\| deletes\|chang es\|purge... | 变更缓冲策略，all表示启用所有类型。 |
| innodb check _ sum algorith _ m | crc32 | crc32 | 否 | [innodb\|crc32 \|none\|strict i _ nnodb\|st... | InnoDB页校验算法，crc32表示使用 CRC32。 |
| innodb cmp _ _ per index en _ _ abled | OFF | OFF | 否 | [ON\|OFF] | 按索引压缩统计，OFF表示禁用。 |
| innodb comm _ it concurrenc _ y | 0 | 0 | 是 | [0-1000] | 提交并发数，控制事务提交的并发性。 |
| innodb compr _ ession failure _ threshold pc _ _ t | 5 | 5 | 否 | [0-100] | 压缩失败阈值百分比。 |
| innodb compr _ ession level _ | 6 | 6 | 否 | [0-9] | 压缩级别（0- 9），数值越高压缩率越高。 |

数配置

| innodb compr _ ession pad p _ _ ct max _ | 50 | 50 | 否 | [0-70] | 压缩填充最大百分比。 |
|---|---|---|---|---|---|
| innodb concu _ rrency tickets _ | 5000 | 5000 | 否 | [1- 4294967295] | 线程并发票数， 控制并发事务数量。 |
| innodb deadl _ ock detect _ | ON | ON | 否 | [ON\|OFF] | 死锁检测开关，ON表示启用。 |
| innodb disabl _ e sort file ca _ _ _ che | ON | ON | 否 | [ON\|OFF] | 禁用排序文件缓存，ON表示启用。 |
| innodb flush _ _ method | O DIRECT _ | O DIRECT _ | 是 | [fsync\|O DSY _ NC\|littlesync\| nosync\|O ... _ | 数据刷新方法，O DIRECT _ 表示直接IO。 |
| innodb flush _ _ neighbors | 0 | 0 | 否 | [0\|1\|2] | 刷新相邻页策略，0表示禁用。 |
| innodb flush _ _ sync | ON | ON | 否 | [ON\|OFF] | 刷新操作是否同步，ON表示启用。 |
| innodb ft cac _ _ he size _ | 8000000 | 8000000 | 是 | [1600000- 80000000] | 全文索引缓存大小 。 |
| innodb ft ena _ _ ble diag print _ _ | OFF | OFF | 否 | [ON\|OFF] | 启用诊断输出，OFF表示禁用。 |
| innodb ft ena _ _ ble stopword _ | ON | ON | 否 | [ON\|OFF] | 启用停用词过滤，ON表示启用。 |
| innodb ft ma _ _ x token size _ _ | 84 | 84 | 是 | [10-84] | 全文索引最大令牌长度 。 |
| innodb ft min _ _ token size _ _ | 3 | 3 | 是 | [0-16] | 全文索引最小令牌长度 。 |

数配置

| innodb ft nu _ _ m word opti _ _ mize | 2000 | 2000 | 否 | [0-10000] | 优化词数，控制全文索引优化频率。 |
|---|---|---|---|---|---|
| innodb ft res _ _ ult cache limi _ _ t | 2000000000 | 2000000000 | 否 | [1000000- 4294967295] | 全文搜索结果缓存限制。 |
| innodb ft sort _ _ pll degree _ _ | 2 | 2 | 是 | [1-16] | 并行排序线程数 。 |
| innodb ft tota _ _ l cache size _ _ | 640000000 | 640000000 | 是 | [32000000- 1600000000] | 全文索引总缓存大小。 |
| innodb io cap _ _ acity | 20000 | 20000 | 否 | [0- 18446744073 709551615] | I/O容量，影响 InnoDB的I/O 调度。 |
| innodb io cap _ _ acity max _ | 40000 | 40000 | 否 | [0- 18446744073 709551615] | 最大I/O容量， 用于高负载场景。 |
| innodb large _ _ prefix | OFF | OFF | 否 | [ON\|OFF] | 大前缀支持，ON表示启用。 |
| innodb lock _ _ wait timeout _ | 50 | 50 | 否 | [1- 1073741824] | 锁等待超时时间 （秒）。 |
| innodb log ch _ _ ecksums | ON | ON | 否 | [ON\|OFF] | 事务日志校验，ON表示启用。 |
| innodb log co _ _ mpressed pa _ ges | OFF | OFF | 否 | [ON\|OFF] | 压缩事务日志页，OFF表示禁用。 |
| innodb log fil _ _ e size _ | {LEAST(DBIns tanceClassMe mory/6, 1572864000) } | 500M | 是 | [4194304- 10737418240 0] | 事务日志文件大小 。 |
| innodb lru sc _ _ an depth _ | {LEAST(DBIns tanceClassMe mory/104857 6/8, 8192)} | {LEAST(DBIns tanceClassMe mory/104857 6/8, 8192)} | 否 | [100- 18446744073 709551615] | LRU列表扫描深度，影响缓冲池管理。 |

数配置

| innodb max _ _ dirty pages p _ _ ct | 75 | 75 | 否 | [0-99] | 脏页百分比上限，控制刷新频率。 |
|---|---|---|---|---|---|
| innodb max _ _ dirty pages p _ _ ct lwm _ | 10 | 10 | 否 | [0-99] | 脏页低水位线， 用于动态调整刷新。 |
| innodb max _ _ purge lag _ | 0 | 0 | 否 | [0- 4294967295] | 最大清除延迟， 控制事务清理速度。 |
| innodb max _ _ purge lag del _ _ ay | 0 | 0 | 否 | [0-10000000] | 清除延迟最大等待时间（微秒）。 |
| innodb max _ _ undo log size _ _ | 1073741824 | 1073741824 | 否 | [10485760- 18446744073 709551615] | 撤销日志最大大小。 |
| innodb old bl _ _ ocks pct _ | 37 | 37 | 否 | [5-95] | 旧块占比，控制 LRU替换策略。 |
| innodb old bl _ _ ocks time _ | 1000 | 1000 | 否 | [0-1024] | 旧块停留时间 （毫秒）。 |
| innodb online _ alter log ma _ _ _ x size _ | 134217728 | 134217728 | 否 | [134217728- 2147483647] | 在线DDL日志最大大小。 |
| innodb open _ _ files | {LEAST(DBIns tanceClassCP U*500, 8000)} | {LEAST(DBIns tanceClassCP U*500, 8000)} | 是 | [1-8192] | 最大打开文件数，受CPU限制。 |
| innodb optimi _ ze fulltext on _ _ ly | OFF | OFF | 否 | [ON\|OFF] | 仅优化全文索引，OFF表示禁用。 |
| innodb page _ _ cleaners | {LEAST(DBIns tanceClassMe mory/107374 1824, 8)} | {LEAST(DBIns tanceClassMe mory/107374 1824, 8)} | 是 | [1-64] | 页面清理线程数。 |

数配置

| innodb print _ _ all deadlocks _ | OFF | OFF | 否 | [OFF\|ON] | 打印所有死锁信息，OFF表示禁用。 |
|---|---|---|---|---|---|
| innodb purge _ batch size _ _ | 300 | 300 | 是 | [1-5000] | 清除批次大小， 控制事务清理效率。 |
| innodb purge _ rseg truncat _ _ e frequency _ | 128 | 128 | 否 | [1-128] | 清除回滚段截断频率。 |
| innodb purge _ threads _ | {LEAST(DBIns tanceClassMe mory/107374 1824, 8)} | {LEAST(DBIns tanceClassMe mory/107374 1824, 8)} | 是 | [1-32] | 清除线程数，影响事务清理性能。 |
| innodb rando _ m read ahea _ _ d | OFF | OFF | 否 | [ON\|OFF] | 随机预读，OFF 表示禁用。 |
| innodb read _ _ ahead thresh _ old | 56 | 56 | 否 | [0-1024] | 预读阈值，控制预读行为。 |
| innodb read i _ _ o threads _ | 4 | 4 | 是 | [1-64] | 读取I/O线程数 。 |
| innodb rollba _ ck on timeou _ _ t | OFF | OFF | 是 | [OFF\|ON] | 超时回滚，ON 表示启用。 |
| innodb rollba _ ck segments _ | 128 | 128 | 否 | [1-128] | 回滚段数量，控制事务回滚能力。 |
| innodb sort b _ _ uffer size _ | 1048576 | 1048576 | 是 | [65536- 67108864] | 排序缓冲区大小 。 |
| innodb spin _ _ wait delay _ | 6 | 6 | 否 | [0- 4294967295] | 自旋等待延迟 （微秒）。 |
| innodb stats _ _ auto recalc _ | ON | ON | 否 | [ON\|OFF] | 自动重新计算统计信息，ON表示启用。 |

数配置

| innodb stats _ _ method | nulls equal _ | nulls equal _ | 否 | [nulls equal\|n _ ulls unequal\| _ nulls ig... _ | 统计信息计算方法，nulls equ _ al表示处理空值。 |
|---|---|---|---|---|---|
| innodb stats _ _ on metadata _ | OFF | OFF | 否 | [ON\|OFF] | 元数据操作时更新统计信息，OFF表示禁用。 |
| innodb stats _ _ persistent | ON | ON | 否 | [ON\|OFF] | 持久化统计信息，ON表示启用。 |
| innodb stats _ _ persistent sa _ mple pages _ | 20 | 20 | 否 | [0- 4294967295] | 持久化采样页数。 |
| innodb stats _ _ sample pages _ | 8 | 8 | 否 | [1- 4294967296] | 统计信息采样页数。 |
| innodb stats _ _ transient sam _ ple pages _ | 8 | 8 | 否 | [1- 4294967295] | 临时统计信息采样页数。 |
| innodb status _ output _ | OFF | OFF | 否 | [ON\|OFF] | 输出InnoDB状态信息，OFF表示禁用。 |
| innodb status _ output locks _ _ | OFF | OFF | 否 | [ON\|OFF] | 输出锁信息，OFF表示禁用。 |
| innodb strict _ _ mode | OFF | OFF | 否 | [ON\|OFF] | 严格模式，OFF 表示禁用。 |
| innodb sync _ _ array size _ | 128 | 128 | 是 | [1-1024] | 同步数组大小 。 |
| innodb sync _ _ spin loops _ | 30 | 30 | 否 | [0- 4294967295] | 自旋等待次数。 |
| innodb table _ _ locks | ON | ON | 否 | [ON\|OFF] | 表级锁，ON表示启用。 |

数配置

| innodb threa _ d concurrenc _ y | 0 | 0 | 否 | [0-1000] | 线程并发数，控制并发事务数量。 |
|---|---|---|---|---|---|
| innodb threa _ d sleep delay _ _ | 10000 | 10000 | 否 | [0-1000000] | 线程睡眠延迟 （微秒）。 |
| innodb undo _ _ log truncate _ | OFF | OFF | 否 | [ON\|OFF] | 撤销日志截断，OFF表示禁用。 |
| innodb write _ _ io threads _ | 4 | 4 | 是 | [1-64] | 写入I/O线程数 。 |
| interactive ti _ meout | 7200 | 7200 | 否 | [10-86400] | 交互式连接超时时间（秒）。 |
| join buffer siz _ _ e | {LEAST(DBIns tanceClassMe mory/104857 6*128, 262144)} | 352KB | 否 | [128- 4294967295] | 连接缓冲区大小，受内存限制。 |
| key cache ag _ _ e threshold _ | 300 | 300 | 否 | [100- 4294967295] | 键缓存年龄阈值，控制缓存淘汰。 |
| key cache bl _ _ ock size _ | 1024 | 1024 | 否 | [512-16384] | 键缓存块大小 （字节）。 |
| key cache di _ _ vision limit _ | 100 | 100 | 否 | [1-100] | 键缓存划分比例，控制热/冷数据分离。 |

数配置

| loose ssl ciph _ _ er | ALL:@SECLEV EL=0 | ALL:@SECLEV EL=0 | 是 | .* |  | 指定TLS连接允许的加密套件列表。服务端仅接受列表中定义的加密算法与客户端进行握手协商。若列表中的算法均不被客户端支持，TLS连接将建立失败。 默认值 ALL:@SEC LEVEL=0 表示允许所有安全等级的加密套件，以最大化兼容性；建议根据安全合规要求配置高强度算法组合（如禁用弱加密算法），但需确保业务客户端支持所选算法， 避免连接中断。 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | ALL:@SEC |  |
|  |  |  |  |  |  | LEVEL=0 |  |  |
| lc time name _ _ s | en US _ | en US _ | 否 | [ja JP\|pt BR\|e _ _ n US] _ |  | 时间格式区域设置，en US表 _ 示美国英语。 |  |  |
| local infile _ | ON | ON | 否 | [ON\|OFF] |  | 允许加载本地文件，ON表示启用。 |  |  |
| lock wait tim _ _ eout | 31536000 | 31536000 | 否 | [1- 1073741824] |  | 锁等待超时时间 （秒）。 |  |  |
| log error ver _ _ bosity | 2 | 2 | 否 | [1-3] |  | 错误日志详细级别，2表示详细信息。 |  |  |
| log queries n _ _ ot using inde _ _ xes | OFF | OFF | 否 | [ON\|OFF] |  | 记录未使用索引的查询，OFF表示禁用。 |  |  |
| log slow adm _ _ in statements _ | OFF | OFF | 否 | [ON\|OFF] |  | 记录慢管理语句，OFF表示禁用。 |  |  |

数配置

| log throttle q _ _ ueries not usi _ _ ng indexes _ | 0 | 0 | 否 | [0- 4294967295] | 未使用索引查询的节流限制。 |
|---|---|---|---|---|---|
| long query ti _ _ me | 1 | 1 | 否 | [0.1- 31536000] | 慢查询时间阈值 （秒）。 |
| loose ccl que _ _ ue bucket co _ _ unt | 4 | 4 | 否 | [1-64] | 队列桶数量，用于特定功能。 |
| loose ccl que _ _ ue bucket siz _ _ e | 64 | 64 | 否 | [1-4096] | 队列桶大小，用于特定功能。 |
| loose collatio _ n server _ | utf8 general _ _ ci | utf8 general _ _ ci | 是 | [utf8 bin\|utf8 _ general ci\|la _ _ tin1 bi... _ | 服务器默认排序规则，utf8 gene _ ral ci表示通用 _ 校对。 |
| loose innodb _ _ data file purg _ _ e | ON | ON | 否 | [ON\|OFF] | 启用InnoDB数据文件清理，ON表示启用。 |
| loose innodb _ _ data file purg _ _ e interval _ | 100 | 100 | 否 | [0-10000] | 数据文件清理间隔。 |
| loose innodb _ _ data file purg _ _ e max size _ _ | 512 | 512 | 否 | [16- 1073741824] | 数据文件清理最大大小。 |
| loose innodb _ _ log optimize _ _ ddl | OFF | OFF | 否 | [ON\|OFF] | 优化DDL日志，OFF表示禁用。 |
| loose innodb _ _ numa interle _ ave | ON | ON | 是 | [ON\|OFF] | NUMA交错配置，ON表示启用。 |
| loose innodb _ _ rds faster ddl _ _ | ON | ON | 否 | [ON\|OFF] | 加速DDL操作，ON表示启用。 |

数配置

| loose internal _ tmp disk sto _ _ _ rage engine _ | INNODB | INNODB | 否 | [INNODB\|MYI SAM] | 内部临时表磁盘引擎，INNODB 表示使用 InnoDB。 |
|---|---|---|---|---|---|
| loose max ex _ _ ecution time _ | 0 | 0 | 否 | [0- 4294967295] | 查询最大执行时间（毫秒）。 |
| loose max st _ _ atement time _ | 0 | 0 | 否 | [0- 4294967295] | 语句最大执行时间（毫秒）。 |
| loose opt rds _ _ enable show _ _ slave lag _ _ | ON | ON | 否 | [ON\|OFF] | 启用显示从库延迟，ON表示启用。 |
| loose opt rds _ _ last error gti _ _ _ d | ON | ON | 否 | [ON\|OFF] | 记录最后错误 GTID，ON表示启用。 |
| loose optimiz _ er trace _ | enabled=off,o ne line=off _ | enabled=off,o ne line=off _ | 否 | .* | 优化器追踪配置，默认关闭。 |
| loose optimiz _ er trace feat _ _ ures | greedy searc _ h=on,range o _ ptimizer=on, dynamic rang _ e= on,repeated _ subselect=on | greedy searc _ h=on,range o _ ptimizer=on, dynamic rang _ e=on,repeate d subselect= _ on | 否 | .* | 优化器追踪功能，如范围优化。 |
| loose perform _ ance point io _ _ stat interval _ | 2 | 2 | 否 | [0-60] | IO统计间隔 （秒）。 |
| loose perform _ ance point io _ _ stat volume s _ _ ize | 10000 | 10000 | 是 | [0-100000] | IO统计体积大小 。 |
| loose perform _ ance point lo _ _ ck rwlock en _ _ abled | ON | ON | 否 | [ON\|OFF] | 启用锁统计，ON表示启用。 |
| loose perform _ ance schema _ accounts siz _ _ e | 10000 | 10000 | 是 | [-1-1048576] | 账户统计大小 。 |

数配置

| loose perform _ ance schema _ digests size _ _ | 10000 | 10000 | 是 | [-1-1048576] | 查询摘要大小 。 |
|---|---|---|---|---|---|
| loose perform _ ance schema _ hosts size _ _ | 10000 | 10000 | 是 | [-1-1048576] | 主机统计大小 。 |
| loose perform _ ance schema _ max cond in _ _ _ stances | 10000 | 10000 | 是 | [-1-1048576] | 条件实例最大数 。 |
| loose perform _ ance schema _ max file inst _ _ _ ances | 1000 | 1000 | 是 | [-1-1048576] | 文件实例最大数 。 |
| loose perform _ ance schema _ max index s _ _ _ tat | 10000 | 10000 | 是 | [-1-1048576] | 索引统计最大数 。 |
| loose perform _ ance schema _ max metada _ _ ta locks _ | 10000 | 10000 | 是 | [-1-1048576] | 元数据锁最大数 。 |
| loose perform _ ance schema _ max mutex i _ _ _ nstances | 10000 | 10000 | 是 | [-1- 104857600] | 互斥锁实例最大数 。 |
| loose perform _ ance schema _ max prepare _ _ d statements _ instances _ | 1000 | 1000 | 是 | [-1-4194304] | 预处理语句实例最大数 。 |
| loose perform _ ance schema _ max progra _ _ m instances _ | 10000 | 10000 | 是 | [-1-1048576] | 程序实例最大数 。 |
| loose perform _ ance schema _ max rwlock _ _ _ instances | 10000 | 10000 | 是 | [-1- 104857600] | 读写锁实例最大数 。 |

数配置

| loose perform _ ance schema _ max socket _ _ _ instances | 1000 | 1000 | 是 | [-1-1048576] | 套接字实例最大数 。 |
|---|---|---|---|---|---|
| loose perform _ ance schema _ max table h _ _ _ andles | 10000 | 10000 | 是 | [-1-1048576] | 表句柄最大数 。 |
| loose perform _ ance schema _ max table in _ _ _ stances | 1000 | 1000 | 是 | [-1-1048576] | 表实例最大数 。 |
| loose perform _ ance schema _ max table lo _ _ _ ck stat _ | 10000 | 10000 | 是 | [-1-1048576] | 表锁统计最大数 。 |
| loose perform _ ance schema _ max thread _ _ _ instances | 10000 | 10000 | 是 | [-1-1048576] | 线程实例最大数 。 |
| loose perform _ ance schema _ setup actors _ _ size _ | 10000 | 10000 | 是 | [-1-1048576] | Actor设置大小 。 |
| loose perform _ ance schema _ setup object _ _ s size _ | 10000 | 10000 | 是 | [-1-1048576] | 对象设置大小 。 |
| loose perform _ ance schema _ users size _ _ | 10000 | 10000 | 是 | [-1-1048576] | 用户统计大小 。 |
| loose rds aud _ _ it max sql siz _ _ _ e | 8192 | 8192 | 否 | [0-32768] | 审计日志最大 SQL长度。 |
| loose rds che _ _ ck core file e _ _ _ nabled | ON | ON | 否 | [ON\|OFF] | 启用核心文件检查，ON表示启用。 |
| loose rds kill _ _ _ connections | 20 | 20 | 否 | [0- 18446744073 709551615] | 最大连接数，超过后终止连接。 |

数配置

| loose rds set _ _ connection i _ _ d enabled _ | ON | ON | 否 | [ON\|OFF] | 启用连接ID设置，ON表示启用。 |
|---|---|---|---|---|---|
| loose recycle _ bin _ | OFF | OFF | 否 | [ON\|OFF] | 启用回收站，ON表示启用。 |
| loose recycle _ bin retention _ _ | 604800 | 604800 | 否 | [86400- 1209600] | 回收站保留时间 （秒）。 |
| loose recycle _ scheduler _ | OFF | OFF | 否 | [ON\|OFF] | 回收站调度器，ON表示启用。 |
| loose sql safe _ _ updates _ | OFF | OFF | 否 | [ON\|OFF] | 安全更新模式，OFF表示禁用。 |
| loose thread _ _ pool enabled _ | ON | ON | 否 | [ON\|OFF] | 线程池启用，ON表示启用。 |
| loose thread _ _ pool oversubs _ cribe | 32 | 32 | 否 | [10-64] | 线程池超分配比例。 |
| loose thread _ _ pool size _ | 4 | 1 | 否 | [1-64] | 线程池大小，受 CPU限制。 |
| loose validate _ password ch _ _ eck user nam _ _ e | ON | ON | 否 | [ON\|OFF] | 验证密码是否包含用户名，ON 表示启用。 |
| loose validate _ password le _ _ ngth | 8 | 8 | 否 | [0-256] | 密码最小长度。 |
| loose validate _ password mi _ _ xed case cou _ _ nt | 1 | 1 | 否 | [0-256] | 混合大小写字符数要求。 |
| loose validate _ password nu _ _ mber count _ | 1 | 1 | 否 | [0-256] | 数字字符数要求。 |

数配置

| loose validate _ password po _ _ licy | 1 | 1 | 否 | [0\|1\|2] | 密码策略等级 （0-2）。 |
|---|---|---|---|---|---|
| loose validate _ password sp _ _ ecial char co _ _ unt | 1 | 1 | 否 | [0-256] | 特殊字符数要求。 |
| low priority u _ _ pdates | 0 | 0 | 否 | [0\|1] | 低优先级更新，0表示禁用。 |
| lower case ta _ _ ble names _ | 1 | 1 | 是 | [0\|1] | 表名大小写敏感性，1表示忽略大小写。 |
| master verify _ checksum _ | OFF | OFF | 否 | [ON\|OFF] | 主库校验和验证，OFF表示禁用。 |
| max allowed _ _ packet | 1073741824 | 1024M | 否 | [16384- 1073741824] | 客户端最大包大小（字节）。 |
| max binlog c _ _ ache size _ | 18446744073 709547520 | 18446744073 709547520 | 否 | [4096- 18446744073 709547520] | 二进制日志缓存最大大小。 |
| max binlog st _ _ mt cache siz _ _ e | 18446744073 709547520 | 18446744073 709547520 | 否 | [4096- 18446744073 709547520] | 非事务性语句缓存最大大小。 |
| max connect _ _ errors | 100 | 100 | 否 | [0- 4294967295] | 最大连接错误次数。 |
| max error co _ _ unt | 64 | 64 | 否 | [0-65535] | 最大错误消息数量。 |
| max heap ta _ _ ble size _ | 67108864 | 67108864 | 否 | [16384- 18446744073 70954752] | MEMORY表最大大小。 |
| max join size _ _ | 18446744073 709500000 | 18446744073 709500000 | 否 | [1- 18446744073 709551615] | 连接操作最大行数。 |

数配置

| max length f _ _ or sort data _ _ | 1024 | 1024 | 否 | [0-838860] | 排序数据最大长度。 |
|---|---|---|---|---|---|
| max points in _ _ geometry _ | 65536 | 65536 | 否 | [3-1048576] | 几何对象最大点数。 |
| max prepare _ d stmt count _ _ | 16382 | 16382 | 否 | [0-1048576] | 最大预处理语句数。 |
| max seeks fo _ _ r key _ | 18446744073 709500000 | 18446744073 709500000 | 否 | [1- 18446744073 709551615] | 键查找最大次数。 |
| max sort len _ _ gth | 1024 | 1024 | 否 | [4-8388608] | 排序操作最大长度。 |
| max sp recur _ _ sion depth _ | 0 | 0 | 否 | [0-255] | 存储过程递归深度限制。 |
| max write loc _ _ k count _ | 102400 | 102400 | 否 | [1-102400] | 写锁最大计数。 |
| metadata loc _ ks cache size _ _ | 1024 | 1024 | 是 | [1-1048576] | 元数据锁缓存大小 。 |
| min examine _ d row limit _ _ | 0 | 0 | 否 | [0- 4294967295] | 最小检查行数限制。 |
| myisam sort _ _ buffer size _ | 262144 | 262144 | 否 | [262144- 16777216] | MyISAM排序缓冲区大小。 |
| mysql native _ _ password pro _ xy users _ | OFF | OFF | 否 | [ON\|OFF] | 代理用户密码插件，OFF表示禁用。 |
| net buffer len _ _ gth | 16384 | 16384 | 否 | [1024- 1048576] | 网络缓冲区长度 （字节）。 |
| net read time _ _ out | 30 | 30 | 否 | [1- 18446744073 709551615] | 读超时时间 （秒）。 |

数配置

| net retry cou _ _ nt | 10 | 10 | 否 | [1- 4294967295] | 连接重试次数。 |
|---|---|---|---|---|---|
| net write tim _ _ eout | 60 | 60 | 否 | [1- 18446744073 709551615] | 写超时时间 （秒）。 |
| ngram token _ _ size | 2 | 2 | 是 | [0-20] | n-gram分词大小 。 |
| old password _ s | 0 | 0 | 否 | [0\|2] | 旧密码哈希算法，0表示禁用。 |
| open files lim _ _ it | 65535 | 65535 | 是 | [1- 18446744073 709551615] | 最大打开文件数 。 |
| optimizer pru _ ne level _ | 1 | 1 | 否 | [0\|1] | 优化器剪枝级别，0表示禁用。 |
| optimizer sea _ rch depth _ | 62 | 62 | 否 | [0-62] | 优化器搜索深度。 |
| optimizer tra _ ce limit _ | 1 | 1 | 否 | [0- 4294967295] | 优化器追踪记录限制。 |
| optimizer tra _ ce max mem _ _ size _ | 16384 | 16384 | 否 | [0- 4294967295] | 优化器追踪内存限制。 |
| optimizer tra _ ce offset _ | -1 | -1 | 否 | [- 2147483648- 2147483647] | 优化器追踪偏移量。 |
| performance _ schema | {LEAST(DBIns tanceClassMe mory/858993 4592, 1)} | {LEAST(DBIns tanceClassMe mory/858993 4592, 1)} | 是 | [0-1] | 性能模式启用，0表示禁用。 |
| preload buffe _ r size _ | 32768 | 32768 | 否 | [1024- 1073741824] | 预加载缓冲区大小。 |

数配置

| query alloc bl _ _ ock size _ | 8192 | 8192 | 否 | [1024-16384] | 查询分配块大小 （字节）。 |
|---|---|---|---|---|---|
| query cache l _ _ imit | 1048576 | 1048576 | 否 | [1-1048576] | 查询缓存单条结果最大大小。 |
| query cache _ _ min res unit _ _ | 1024 | 1024 | 否 | [512- 18446744073 709551608] | 查询缓存最小分配单元。 |
| query cache _ _ size | 0 | 0 | 否 | [0- 10485760000 ] | 查询缓存总大小，0表示禁用。 |
| query cache _ _ type | 0 | 0 | 是 | [0\|1\|2] | 查询缓存类型，0表示禁用。 |
| query cache _ _ wlock invalid _ ate | OFF | OFF | 否 | [ON\|OFF] | 写锁时失效缓存，OFF表示禁用。 |
| query preallo _ c size _ | 8192 | 8192 | 否 | [8192- 1048576] | 预分配查询缓冲区大小（字节）。 |
| range alloc bl _ _ ock size _ | 4096 | 4096 | 否 | [4096- 18446744073 709551615] | 范围分配块大小 （字节）。 |
| range optimiz _ er max mem _ _ size _ | 8388608 | 8388608 | 是 | [0- 18446744073 709551615] | 范围优化器内存限制 。 |
| rds reserved _ _ connections | 512 | 512 | 否 | [0-512] | 保留连接数。 |
| read buffer si _ _ ze | {LEAST(DBIns tanceClassMe mory/104857 6*128, 262144)} | 704KB | 否 | [8200- 2147479552] | 读缓冲区大小。 |
| relay log rec _ _ overy | OFF | OFF | 是 | [ON\|OFF] | 中继日志恢复，OFF表示禁用。 |

数配置

| session track _ gtids _ | OFF | OFF | 否 | [OFF\|OWN GT _ ID\|ALL GTIDS _ ] | 跟踪 GTID，OFF表示禁用。 |
|---|---|---|---|---|---|
| sha256 pass _ word proxy u _ _ sers | OFF | OFF | 否 | [ON\|OFF] | SHA-256密码代理用户，OFF 表示禁用。 |
| show compati _ bility 56 _ | OFF | OFF | 否 | [ON\|OFF] | 兼容MySQL 5.6特性，OFF 表示禁用。 |
| show old tem _ _ porals | OFF | OFF | 否 | [ON\|OFF] | 显示旧时间类型，OFF表示禁用。 |
| slave net tim _ _ eout | 60 | 60 | 否 | [15-300] | 从库网络超时时间（秒）。 |
| slave parallel _ type _ | LOGICAL CLO _ CK | LOGICAL CLO _ CK | 是 | [DATABASE\|L OGICAL CLOC _ K] | 从库并行类型，LOGICAL _ CLOCK表示逻辑时钟。 |
| slave type co _ _ nversions |  | - | 是 | [支持空格及\|ALL LOSSY _ \|ALL NON LO _ _ SSY\|ALL ... _ | 类型转换规则， 支持空格及 ALL LOSSY _ 等。 |
| slow launch t _ _ ime | 2 | 2 | 否 | [1-1024] | 慢启动时间 （秒）。 |
| slow query lo _ _ g | ON | ON | 否 | [ON\|OFF] | 慢查询日志开关，ON表示启用。 |
| sort buffer si _ _ ze | 262144 | 704KB | 否 | [32768- 4294967295] | 排序缓冲区大小。 |

数配置

| sql mode _ | ONLY FULL G _ _ ROUP BY,STR _ ICT TRANS T _ _ ABLES,NO ZE _ RO IN _ _ DATE,NO ZER _ O DATE,ERRO _ R FOR DIVISI _ _ ON BY ZERO, _ _ NO EN _ GINE SUBSTI _ TUTION | ONLY FULL G _ _ ROUP BY,STR _ ICT TRANS T _ _ ABLES,NO ZE _ RO IN DATE, _ _ NO ZERO DA _ _ TE,ERROR FO _ R DIVISION B _ _ Y ZERO,NO E _ _ NGINE SUBST _ ITUTION | 否 | (\支持空格及\|REAL AS F _ _ LOAT\|PIPES A _ S CONC... _ | SQL模式，控制 SQL语法和验证规则。 |
|---|---|---|---|---|---|
| stored progra _ m cache _ | 256 | 256 | 否 | [16-524288] | 存储程序缓存大小。 |
| sync master i _ _ nfo | 10000 | 10000 | 否 | [0- 18446744073 709551615] | 主库信息同步间隔（微秒）。 |
| sync relay lo _ _ g info _ | 10000 | 10000 | 否 | [0- 18446744073 709551615] | 中继日志信息同步间隔（微秒）。 |
| table definitio _ n cache _ | {LEAST(DBIns tanceClassMe mory/107374 1824*512, 2048) } | {LEAST(DBIns tanceClassMe mory/107374 1824*512, 2048)} | 否 | [400-524288] | 表定义缓存大小。 |
| table open c _ _ ache | {LEAST(DBIns tanceClassMe mory/107374 1824*256, 2048) } | {LEAST(DBIns tanceClassMe mory/107374 1824*256, 2048)} | 否 | [1-524288] | 表缓存大小。 |
| table open c _ _ ache instance _ s | {LEAST(DBIns tanceClassMe mory/107374 1824, 16)} | {LEAST(DBIns tanceClassMe mory/107374 1824, 16)} | 是 | [1-64] | 表缓存实例数。 |
| thread cache _ size _ | 256 | 256 | 否 | [0-16384] | 线程缓存大小。 |
| thread stack _ | 262144 | 262144 | 是 | [131072- 18446744073 709551615] | 线程栈大小（字节） 。 |

数配置

| tls version _ | TLSv1.2 | TLSv1.2 | 是 | [TLSv1,TLSv1. 1,TLSv1.2\|TLS v1,TLSv1.... | TLS版本，TLSv1.2表示使用指定版本。 |
|---|---|---|---|---|---|
| tmp table siz _ _ e | 2097152 | 2097152 | 否 | [262144- 134217728] | 内存临时表最大大小。 |
| transaction al _ loc block size _ _ | 8192 | 8192 | 否 | [1024- 131072] | 事务分配块大小 （字节）。 |
| transaction is _ olation | READ- COMMITTED | READ- COMMITTED | 否 | [READ- UNCOMMITTE D\|READ- COMMITTED\| RE... | 事务隔离级别，READ- COMMITTED 表示只能读取到已提交数据。 |
| transaction p _ realloc size _ | 4096 | 4096 | 否 | [1024- 131072] | 事务预分配大小 （字节）。 |
| updatable vie _ ws with limit _ _ | YES | YES | 否 | [YES\|NO] | 允许带LIMIT的视图更新，YES 表示启用。 |
| wait timeout _ | 86400 | 86400 | 否 | [1-31536000] | 非交互式连接超时时间（秒）。 |
| default authe _ ntication plug _ in | mysql native _ password _ | mysql native _ password _ | 是 | mysql native _ password、 _ sha256 pass _ word、 caching sha2 _ password _ | 用户密码加密算法。 |
| max user con _ _ nections | 600 | 2500 | 否 | [10-200000] | 用户账户允许的最大同时连接数。 |
| max connecti _ ons | 600 | 3032 | 否 | [1-200000] | 服务器允许的最大并发连接总数。 |
| default passw _ ord lifetime _ | 0 | 0 | 否 | [0-365] | 自动密码过期策略（默认密码生存期）。 |

### 使用参数模板

数配置在配置实例时，如果多个实例中存在一个或多个参数的配置相同，您可以使用参数模板功能，对这些参数进行集中管理，并快速应用到实例，从而提升参数管理效率和实例配置效率。

### 使用限制

目前仅语法兼容版本为8**（兼容****8.0**和**8.4**）版本的实例支持该功能，您可在实例详情页的**基本信息**页面中， 查看语法兼容版本。

**新建参数模板**

## 1. 登录云原生数据库PolarDB控制台

2. 在**主备版** > **参数模板**页面，单击**创建参数模板**，并设置以下参数。

| 参数 | 说明 |
|---|---|
| 模板名称 | 模板的名称。名称需要满足以下规则： 由英文、数字和下划线（ ）组成，以字母开头，不能包含中文。 _ 长度为8~64个字符。 |
| 数据库引擎 | 选择MySQL。 |
| 数据库版本 | 选择数据库引擎版本。 |
| 描述 | 备注该模板的相关信息，便于后续管理。长度为0~200个字符。 |
| 添加配置 | 单击添加配置会增加一行参数供用户选择参数名，并通过参考描述和可修改参数值设置配置值。 用户还可看到是否重启实例、参数默认值等信息。 说明需要配置下一个参数，请再次单击添加配置。 需要删除某个参数，请单击该参数右侧的删除。 |

3. 单击**确定**。

**应用参数模板**

参数模板创建后，用户可在如下两种场景下应用参数模板： 在新建实例时直接应用，新实例将自动继承模板中的配置。 如需批量应用于多个已有实例，可在**参数模板**页面选择目标模板，将其一键配置至最多10个实例。

**重要**

如果参数模板中存在需要重启实例的参数，建议您在业务低峰期操作，并确保应用程序具有重连机制。

## 1. 登录云原生数据库PolarDB控制台

2. 在**主备版** > **参数模板**页面，单击目标模板所在行**操作**列的**应用到实例**。
数配置
3. 在**应用到实例**页面，选择需要应用参数模板的实例，单击
移动到右侧，同时您可以通过**参数对比**查看参数模板中参数配置值与实例中参数配置值的差异。

**说明**

应用参数模板到多个实例上时，请注意以下问题： 请确认参数是否适用这些实例，请谨慎操作。 单次操作只能将参数模板应用到10个实例，如需将参数模板应用至10个以上的实例可分批操作。
4. 单击**确定**。

**复制参数模板**

## 1. 登录云原生数据库PolarDB控制台

2. 在**主备版** > **参数模板**页面，单击目标模板所在行**操作**列的**克隆，**并设置以下参数。
3.

| 参数 | 说明 |
|---|---|
| 模板名称 | 模板的名称，默认为原参数模板名称 clone，您也可以重新命名。名称需满足以下规则： _ 由英文、数字和下划线（ ）组成，以字母开头，不能包含中文。 _ 长度为8~64个字符。 |
| 数据库引擎 | 默认MySQL。 |
| 数据库版本 | 默认仅支持8（兼容8.0和8.4）。 |
| 描述 | 备注该模板的相关信息，便于后续管理。长度为0~200个字符。 |
| 添加配置 | 默认为原参数模板中的参数配置项，您也可以根据需要重新进行配置。 说明如果您需要添加某个参数，请单击添加配置。 如果您需要修改某个参数的配置值，请在该参数右侧的配置值输入框中重新输入。 如果您需要删除某个参数，请单击该参数右侧的删除。 |

4. 单击**确定**。

**删除参数模板**

## 1. 登录云原生数据库PolarDB控制台

2. 在**主备版** > **参数模板**页面，单击目标模板所在行**操作**列的**删除**。
3. 单击**确定**。
数配置

**附录：创建8.4内核实例的关键配置**

PolarDB默认提供名为 `mysql_innodb_8.4_standard_normal_safe` 的参数模板，用于标识和启用8.4功能兼容的自研内核。 若您希望创建8.4内核的实例，请务必在创建实例时完成以下两项配置： 语法兼容：选择8（兼容8.0和8.4）。 参数模板：选择 `mysql_innodb_8.4_standard_normal_safe` 。 号管理

## 账号管理

### 创建账号

创建PolarDB MySQL实例以及设置好白名单之后，您需要在实例中创建数据库和账号。本章节介绍如何创建高权限账号和普通账号。

**背景信息**

PolarDB MySQL版实例支持两种数据库账号：高权限账号和普通账号。您可以在控制台管理所有账号和数据库，账号拥有的具体权限请参见文末账号权限列表。

| 账号类型 | 说明 |
|---|---|
| 高权限账号 | 只能通过控制台或API创建和管理。 一个实例中只能创建一个高权限账号，可以管理所有普通账号和数据库。 开放了更多权限，可满足个性化和精细化的权限管理需求，例如可按用户分配不同表的查询权限。 可以断开任意账号的连接。 |
| 普通账号 | 可以通过控制台、API或者SQL语句创建和管理。 一个实例可以创建最多500个普通账号。 需要手动给普通账号授予特定数据库的权限。 普通账号不能创建和管理其他账号，也不能断开其他账号的连接。 |

| 账号类型 | 建库数量 | 建表数量 | 用户数 |
|---|---|---|---|
| 高权限账号 | 不限 | <20万 | 与实例内核参数相关。 |
| 普通权限账号 | 500 | <20万 | 与实例内核参数相关。 |

**创建高权限账号**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 单击**创建账号**。
5. 设置以下参数。
号管理

| 参数 | 说明 |
|---|---|
| 数据库账号 | 填写账号名称。要求如下： 长度为1~32个字符。 以字母开头，以字母或数字结尾。 由小写字母、大写字母、数字或下划线（ ）组成。 _ |
| 账号类型 | 选择高权限账号。 |
| 密码 | 设置账号密码。要求如下： 长度为8~32个字符。 必须包含大写字母、小写字母、数字或特殊字符中的任意三种或以上类型。 特殊字符包括 !@#$%^&*() +-= 。 _ 密码未使用互联网公开的常见密码，例如：password、123456、admin等，以加强数据库用户密码安全管理。 说明云原生数据库PolarDB支持按需自定义密码策略，但需先前往Apsara Uni-manager运维控制台配置自定义密码策略（配置方法，请参见《运维指南》中“配置PolarDB自定义密码策略”教程），配置完成后再返回本页面刷新页面，系统将自动应用已配置的密码策略， 并在输入不符合规则的密码时实时提示错误。 若无运维平台操作权限，请联系阿里云技术支持协助配置。 |
| 确认密码 | 再次输入密码。 |
| 备注说明 | 非必填。备注该账号的相关信息，便于后续账号管理。最多支持256个字符。 |

6. 单击**确定**。

**重置高权限账号**

如果高权限账号自身出现问题，例如权限被意外回收（REVOKE ），您可以通过输入高权限账号的密码来重置高权限账号的权限，使其恢复正常。

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 单击**高权限账号**右侧操作栏中的**重置账号权限**。
5. 输入高权限账号密码，单击**确定**。

**创建普通账号**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
号管理
4. 单击**创建账号**。
5. 设置以下参数。

| 参数 | 说明 |
|---|---|
| 数据库账号 | 填写账号名称。要求如下： 长度为1~32个字符。 以字母开头，以字母或数字结尾。 由小写字母、大写字母、数字或下划线（ ）组成。 _ |
| 账号类型 | 选择普通账号。 |
| 授权数据库 | 为该账号授予一个或多个数据库的权限。本参数可以留空，在创建账号后再给账号授权。 i. 从左侧选中一个或多个数据库，单击 > 添加到右侧。 ii. 在右侧框中，为某个数据库选择读写、只读、仅DDL或仅DML。 如果要为多个数据库批量设置相同的权限，则单击右侧框中右上角的按钮，比如全部设读写。 |
| 密码 | 设置账号密码。要求如下： 长度为8~32个字符。 必须包含大写字母、小写字母、数字或特殊字符中的任意三种或以上类型。 特殊字符为 !@#$%^&*() +-= 。 _ 密码未使用互联网公开的常见密码，例如：password、123456、admin等，以加强数据库用户密码安全管理。 说明云原生数据库PolarDB支持按需自定义密码策略，但需先前往Apsara Uni-manager运维控制台配置自定义密码策略（配置方法，请参见《运维指南》中“配置PolarDB自定义密码策略”教程），配置完成后再返回本页面刷新页面，系统将自动应用已配置的密码策略， 并在输入不符合规则的密码时实时提示错误。 若无运维平台操作权限，请联系阿里云技术支持协助配置。 |
| 确认密码 | 再次输入密码。 |
| 备注说明 | 非必填。备注该账号的相关信息，便于后续账号管理。最多支持256个字符。 |

6. 单击**确定**。

**账号导出**

号管理

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 在**账号管理**页面，单击
。
5. 在**导出**页面，您可选择**导出范围**和**需要导出的数据列**。
6. 单击**确定**。

**账号权限列表**

| 账号类型 | 授权类型 | 权限 |  |  |  |  |
|---|---|---|---|---|---|---|
| 高权限账号 | - | SELECT | INSERT | UPDATE | DELETE | CREATE |
|  |  | DROP | RELOAD | PROCESS | REFERENCES | INDEX |
|  |  | ALTER | CREATE TEMPORARY TABLES | LOCK TABLES | EXECUTE | REPLICATION SLAVE |
|  |  | REPLICATION CLIENT | CREATE VIEW | SHOW VIEW | CREATE ROUTINE | ALTER ROUTINE |
|  |  | CREATE USER | EVENT | TRIGGER | - | - |
|  | 只读 | SELECT | LOCK TABLES | SHOW VIEW | PROCESS | REPLICATION SLAVE |
|  |  | REPLICATION CLIENT | - | - | - | - |

| olarD 号管理 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 普通账号 |  |  |  |  |  |  |
|  | 读写 | SELECT | INSERT | UPDATE | DELETE | CREATE |
|  |  | DROP | REFERENCES | INDEX | ALTER | CREATE TEMPORARY TABLES |
|  |  | LOCK TABLES | EXECUTE | CREATE VIEW | SHOW VIEW | CREATE ROUTINE |
|  |  | ALTER ROUTINE | EVENT | TRIGGER | PROCESS | REPLICATION SLAVE |
|  |  | REPLICATION CLIENT | - | - | - | - |
|  | 仅DDL | CREATE | DROP | INDEX | ALTER | CREATE TEMPORARY TABLES |
|  |  | LOCK TABLES | CREATE VIEW | SHOW VIEW | CREATE ROUTINE | ALTER ROUTINE |
|  |  | PROCESS | REPLICATION SLAVE | REPLICATION CLIENT | - | - |
|  | 仅DML | SELECT | INSERT | UPDATE | DELETE | CREATE TEMPORARY TABLES |
|  |  | LOCK TABLES | EXECUTE | SHOW VIEW | EVENT | TRIGGER |
|  |  | PROCESS | REPLICATION SLAVE | REPLICATION CLIENT | - | - |

### 重置密码

在使用PolarDB过程中，如果忘记数据库账号密码，可以通过PolarDB MySQL版专有云控制台重新设置密码。

**前提条件**

实例状态为**运行中**。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
号管理
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 在目标账号右侧的操作栏中，单击**重置密码**。
5. 在弹出的对话框中，输入新密码并确认后，单击**确定**。

**说明**

密码要求如下： 长度为8~32个字符。 必须包含大写字母、小写字母、数字或特殊字符中的任意三种或以上类型。 特殊字符为： !@#$%^&*()_+-=

### 修改账号权限

在使用PolarDB过程中，您可以根据需要随时调整实例中账号的权限。

**前提条件**

您可以根据需要修改普通账号的权限。高权限账号的权限只能重置为初始状态，无法修改为指定的权限。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 在目标账号所对应的操作栏中，单击**修改权限**。
5. 设置如下参数。

| 配置 | 说明 |
|---|---|
| 授权数据库 | 在左侧未授权数据库区域中选中数据库，单击>并为所选数据库授权。或在右侧已授权数据库区域中选中数据库，单击移除取消数据库授权。 |
| 已授权数据库 | 在已授权数据库中，可以单独设置每个数据库的权限。也可以通过单击右上角的批量设置按钮（如全部设读写）批量设置所有数据库的权限。 只读：为账号授权数据库的读权限。 读写：为账号授权数据库的读写权限。 仅DDL：为账号授权数据库的DDL操作权限。 仅DML：为账号授权数据库的DML操作权限。 |

6. 配置完上述参数后，单击**确定**。

### 删除账号

号管理

**前提条件**

因业务结束或改变时，您可以在控制台上删除不需要的高权限账号、普通账号。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 在目标账号所对应的操作栏中，单击**删除**。
5. 在弹出的确认框中，单击**确定**。

**说明**

当账号状态为处理中时，无法删除。

### 锁定账号

您可以通过控制台锁定数据库账号。

**前提条件**

因业务结束或改变时，您可以在控制台上锁定不需要的高权限账号、普通账号。

### 锁定账号

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 在目标账号所对应的操作栏中，单击**锁定**。
5. 在弹出的确认框中，单击**确定**。

**解锁账号**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**账号管理**。
4. 在目标账号所对应的操作栏中，单击**解锁**。
5. 在弹出的确认框中，单击**确定**。
据库管理

## 数据库管理

### 创建数据库

创建PolarDB MySQL版实例以及设置好白名单之后，需要在实例中创建数据库和账号。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**数据库管理**。
4. 单击**创建数据库**。
5. 设置以下参数。

| 参数 | 说明 |
|---|---|
| 数据库（DB）名称 | 长度为1~64个字符。 以小写字母开头，以小写字母或数字结尾。 由小写字母、数字、下划线（ ）或中划线（-）组成。 _ 数据库名称在实例内必须是唯一的。 说明下划线（ ）会被视为2个字符。 _ |
| 支持字符集 | 从列表中选择需要的字符集。 |
| 授权账号 | 选中需要授权访问本数据库的账号。本参数可以留空，在创建数据库后再绑定账号。 说明此处只会显示普通账号，因为高权限账号拥有所有数据库的所有权限，不需要授权。 |
| 备注说明 | 非必填。用于备注该数据库的相关信息，便于后续数据库管理，最多支持256个字符。 |

6. 单击**创建**。

### 删除数据库

您可以在PolarDB MySQL版专有云控制台上删除已经废弃的数据库。

**操作步骤**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
据库管理
3. 在左侧导航栏中，单击**数据库管理**。
4. 找到需要删除的数据库，单击其右侧操作栏中的**删除**。
5. 在弹出的确认框中，单击**确定**，删除数据库。
据库连接

## 数据库连接

### 修改连接地址和端口

本章介绍如何查看和修改数据库的连接地址。

**查看连接地址和端口**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**数据库连接**。
1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**数据库连接**。
4. 单击**修改连接地址**。
5. 在弹出的对话框中，选择连接类型，设置外网连接地址及端口号，单击**确定**。

**说明**

由小写字母、大写字母、数字、中划线、点号组成，字母开头，且数字或字母结尾。 每组（两个"."之间）不超过63个字符，总长度不超过253个字符。 端口范围为3000~5999。

**申请或释放外网地址**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库连接**。
4. 单击公网地址右侧的**申请公网**或**释放公网**。

**重要**

申请公网时可自定义配置是否开启IPv6地址。 连接地址释放后无法恢复，只能重新申请。释放外网地址前，请确认您的应用程序已使用新的连接地址进行访问。
5. 单击**确定**。

**开启或关闭IPv6**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库连接**。
4. 打开或关闭**是否应用了****IPv6**列下的开关。
据库连接

**重要**

关闭IPv6连接地址后，通过IPv6地址访问数据库的业务连接将会中断，可能对正在运行的业务造成影响。请确认当前没有业务通过IPv6地址连接数据库后再进行操作。
5. 单击**确定**。

### 通过DMS登录PolarDB数据库

您可以通过阿里云的数据管理服务DMS登录 PolarDB MySQL版实例的数据库。

**前提条件**

**操作步骤**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 单击页面右上角的**登录数据库**，进入DMS的登录页面。
4. 在登录页面设置如下参数：
①：实例的地址和端口，格式为 <内网地址`>:<`内网端口号> ，例如rmbpxxxxxxx.xxx.aliyuncs.com:3433。查看内网地址和端口请参见查看连接地址和端口。 ②：实例的账号名称。 ③：实例的账号密码。
5. 单击**登录**。

**说明**

若您希望浏览器记住该账号的密码，可以先勾选**记住密码**，再单击**登录**。 据库连接

### 临时混访方案（同时保留经典网络和专

**有网络地址）**

为满足日益增多的网络迁移需求，PolarDB新增了网络混访功能，可实现在无访问中断的情况下将经典网络平滑迁移到VPC上。

**背景信息**

以往将PolarDB实例从经典网络迁移到VPC时，经典网络的内网地址会变为VPC的内网地址（连接字符串没有变化，背后的IP地址有变化），会造成1次30秒内的闪断，而且经典网络中的ECS将不能再通过内网访问该PolarDB实例，为了能够平滑迁移网络，PolarDB新增了网络混访功能。 混访是指PolarDB实例可以同时被经典网络和专有网络中的ECS访问。在混访期间，PolarDB实例会保留原经典网络的内网地址并新增一个VPC下的内网地址，迁移网络时不会出现闪断。 基于安全性及性能的考虑，我们推荐您仅使用VPC，因此混访期有一定的期限，原经典网络的内网地址在保留时间到期后会被自动释放，应用将无法通过经典网络的内网地址访问数据库。为避免对业务造成影响，您需要在混访期中将VPC下的内网地址配置到您所有的应用中，以实现平滑的网络迁移。 例如，某一公司要将经典网络迁移至VPC时，若选用混访的迁移方式，在混访期内，一部分应用通过VPC访问数据库，一部分应用仍通过原经典网络的内网地址访问数据库，等所有应用都可以通过VPC访问数据库时，就可以将原经典网络的内网地址释放掉，如下图所示。 经典网络平滑迁移至VPC ECS ECS 新购ECSECS ECSECS ECS ECS ECS ECS ECS ECS ECS ECS 新购ECS ECS ECS SQL SQL SQL SQL 经典网络

| Classic IP | VPC IP |
|---|---|

Classic IP VPC IP VPC 经典网络混访期 VPC

**功能限制**

在混访期间，有如下功能限制： 不支持切换成经典网络。 不支持迁移可用区。

**前提条件**

实例的网络类型是经典网络。 实例所在可用区已有可用的VPC和交换机。

**从经典网络迁移至VPC**

## 1. 登录云原生数据库PolarDB控制台

据库连接
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库连接**。
4. 单击**切换专有网络**。
5. 在弹出的对话框中，选择VPC和交换机，以及是否保留经典网络地址。
选择是否勾选**保留经典网络**，具体说明如下表所述。
**不勾选**：不保留经典网络地址，原经典网络地址变为VPC地址。
如果不保留经典网络地址，则切换网络类型时，PolarDB实例会发生一次30秒的闪断，而且经典网络的ECS对该PolarDB实例的内网访问会立即断开。
**勾选**：保留经典网络地址，同时生成一个新的VPC地址。表示使用混访模式，即PolarDB可以同时被经
典网络和VPC的ECS通过内网访问。 如果保留经典网络地址，则切换网络类型时，PolarDB实例不会发生闪断，而且经典网络的ECS对该PolarDB实例的内网访问也不会断开，直到经典网络地址到期才断开。 选择保留经典网络地址的有效时间，在这个时间到期前，请将VPC地址配置到VPC的ECS中，以实现业务平滑迁移到VPC。
6. 将VPC的ECS内网IP地址添加到PolarDB实例的专有网络白名单分组，使得ECS可以通过内网访问
PolarDB。如果没有专有网络的分组，请新建分组。如何添加白名单请参见设置白名单。

### 切换网络类型

您可以根据业务需求将PolarDB MySQL实例的网络类型在经典网络和专有网络之间切换。

**背景信息**

经典网络：实例之间不通过网络进行隔离，只能依靠实例自身的白名单策略来阻挡非法访问。 专有网络（VPC）：一个VPC就是一个隔离的网络环境。VPC的安全性较高，推荐您使用VPC网络。 您可以自定义VPC中的路由表、IP地址范围和网关。此外，您还可以通过专线或者VPN的方式将自建机房与阿里云VPC组合成一个虚拟机房，实现应用平滑上云。

**从专有网络（VPC）切换为经典网络**

PolarDB MySQL实例切换为经典网络后，内网地址不变（连接字符串不变，该字符串对应的IP地址会改变），VPC中的ECS将不能再通过该内网地址访问该PolarDB MySQL实例，请注意变更应用端的连接地址。

**说明**

在切换网络类型时，PolarDB MySQL服务可能会出现一次30秒的闪断，请您尽量在业务低峰期执行切换操作，或确保您的应用有自动重连机制，以避免闪断造成的影响。

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在页面左侧导航栏中单击**数据库连接**。
4. 在**数据库连接**页面，单击**切换为经典网络**。
5. 在弹出的对话框中，单击**确定**。

**从经典网络切换为专有网络（VPC）**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在页面左侧导航栏中单击**数据库连接**。
据库连接
4. 在**数据库连接**页面，单击**切换专有网络**。
5. 在弹出的对话框中，选择VPC和交换机，以及是否**保留原经典网络**地址，单击确定。

### 切换专有网络VPC和虚拟交换机

您可以直接切换PolarDB MySQL实例的专有网络VPC和虚拟交换机。

**前提条件**

PolarDB MySQL实例的网络类型为专有网络。

**操作步骤**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在页面左侧导航栏中单击**数据库连接**。
4. 在**数据库连接**页面，单击**切换交换机**。
5. 选择VPC和虚拟交换机，单击**确定**。

**说明**

如需新建VPC或虚拟交换机请单击**到控制台创建**。
6. 在弹出的风险提示框中单击**确定切换**。

**说明**

切换过程会有30秒闪断，请确保应用程序具有重连机制。 客户端缓存会导致只能读取数据，无法写入数据，请及时清理缓存。 据库代理

## 数据库代理

### 数据库独享代理

PolarDB MySQL提供数据库独享代理服务，基于独享代理提供更多高级功能，例如读写分离、连接池、事务拆分等。

**前提条件**

实例版本需为MySQL5.7或8.0双机高可用版（本地SSD盘）。

**背景信息**

PolarDB MySQL数据库独享代理服务是使用独立代理计算资源为当前实例提供代理服务，优势如下： 使用代理连接地址后可以不用反复变更应用内的连接地址，减少维护成本，只要不释放代理，代理连接地址可以永远使用。例如您在大促时期开启读写分离，大促结束后释放只读实例，关闭读写分离，也不用变更应用内的连接地址。 避免了共享实例代理时多用户争抢资源导致访问服务不稳定。 使用独立实例代理，资源可扩展，可承载更高流量。

**功能限制**

**注意事项**

当主实例或只读实例变更配置时可能会出现连接闪断。 使用代理连接地址时，如果没有启用事务拆分，事务请求都会路由到主实例。 使用代理连接地址进行读写分离时，不保证非事务读的一致性，业务上有读一致性需求可以封装到事务中。 使用代理连接地址时， `SHOW PROCESSLIST` 会将所有节点的结果合并后返回。 如果执行了Multi-Statements或存储过程，当前连接的后续请求会全部路由到主节点，需断开当前连接并重新连接才能恢复读写分离。 支持Hint语法 `/*FORCE_MASTER*/` 和 `/*FORCE_SLAVE*/` ，但是因为Hint的路由优先级最高，例如 Hint不受一致性、事务的约束，需要您评估是否可以用于业务。另外Hint语句里不能包含改变环境变量的语句，例如 /*FORCE_SLAVE*/ SET names utf8; ，可能导致后续业务出错。 独享代理的连接模型是1：N（即您的一个连接会后端连接到主实例和所有只读实例），建议开通独享代理后，主实例和只读实例的连接数规格尽量一致，否则业务的连接数会受限于最小规格的实例连接数限制。 开启独享代理后，新增只读实例或只读实例重启，只有新的连接的请求才会路由到新的只读实例或重启的只读实例，老的连接请求不会路由过去。 主实例与只读实例的参数**max_prepared_stmt_count**需要保持一致。
1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库代理**。
4. 单击**立即开启**。
据库代理
5. 在**开启数据库代理服务**页面，选择**网络类型**为**内网地址（经典地址）**或**外网地址**。

**页面介绍**

| 类别 | 参数 | 说明 |
|---|---|---|
| 代理地址 | 实例ID | 代理实例ID。 |
|  | 关联代理实例数量 | 代理连接地址关联的代理数量，可以通过增加代理数量提升代理处理请求的能力。 公测结束后增加代理数量会产生费用。 |
|  | 读写分离功能 | 代理连接地址是否开通了读写分离功能。详情请参见开启读写分离。 |
|  | 连接池 | 您可以选择关闭、开启会话级连接池或开启事务级连接池。 |
| 连接地址 | 连接地址 | 代理连接地址，独享代理目前提供一个代理地址，读写分离功能绑定该地址。 说明您可以单击右侧的复制地址将代理连接地址复制到剪贴板。 |
|  | 端口 | 代理连接地址的端口。 |
|  | 网络地址类型 | 代理地址的网络地址类型。 |
| 代理实例 | 代理类型 | 当前仅支持独享代理。 |
|  | 代理规格 | 代理的规格，当前仅支持2核CPU、4GB内存的规格。 |
|  | 开通数量 （个） | 代理的数量。最多60个。 说明推荐的代理个数为主实例及只读实例CPU核数的1/8（向上取整）。 例如主实例为8核CPU，只读实例为4核CPU，则推荐代理数量=⌈(8+4)/8⌉ = 2。 |

**代理版本升级**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库代理**。
据库代理
4. 在**代理地址**页面单击**大版本升级：****1.0****升级到****2.0**。
5. 在**小版本升级设置**页面选择**立即升级**或**可维护时间内进行升级**。
6. 单击**确定**。

**调整代理数量**

**说明**

调整代理数量会导致应用闪断，请确保系统具备重连机制。

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库代理**。
4. 在**代理实例**区域的**开通数量**右侧修改数量，并在**调整方案**右侧单击**应用**。
5. 在弹出的对话框中，您可以选择**立即切换**来立即应用变更的代理数量，也可以选择**可维护时间内进行切**
换或**指定切换开始时间**来设置变更生效的时间，单击**确定**。

**关闭代理服务**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库代理**。
4. 在右上角单击**关闭代理服务**。
5. 在弹出的对话框中，单击**确定**。

### 读写分离

#### 开启读写分离

读写分离是指通过独享代理地址（读写分离地址）实现读写请求的自动转发。

**前提条件**

实例版本为MySQL 5.7或8.0高可用版（本地SSD盘）。

**背景信息**

在对数据库有少量写请求，但有大量读请求的应用场景下，单个实例可能无法承受读取压力，甚至对业务产生影响。为了实现读取能力的弹性扩展，分担数据库压力，您可以创建一个或多个只读实例，利用只读实例满足大量的数据库读取需求。 据库代理创建只读实例后，您可以开通读写分离，开通读写分离后您会获得一个读写分离地址，在应用程序中配置读写分离地址，就可以使写请求自动转发到主实例，读请求自动转发到各个只读实例。

**读写分离地址和内外网地址区别**

开通读写分离后，您就可以将读写分离地址配置在应用程序中，客户端发出的请求到达该地址后会根据请求类型和实例权重自动分配给内部的各个实例。 应用程序中的地址如果是主实例的内网或外网地址，则请求只会交给主实例，而不会交给只读实例处理，必须在程序中添加主实例以及各个只读实例的地址及权重，才能达到读写分离地址的效果。

**转发逻辑**

只发往主实例所有DML操作（INSERT、UPDATE、DELETE、SELECT FOR UPDATE）。 所有DDL操作（建表/库、删表/库、变更表结构、权限等）。 所有事务中的请求。 用户自定义函数。 存储过程。 EXECUTE语句。 Multi Statements。 使用到临时表的请求。 SELECT last_insert_id()。 所有对用户变量的查询和更改。 SHOW PROCESSLIST。 KILL（SQL语句中的KILL，非命令KILL）。 发往只读实例或主实例非事务中的读请求。 据库代理 COM_STMT_EXECUTE命令。 总是发往所有实例所有系统变量的更改。 USE命令。 COM_STMT_PREPARE命令。 COM_CHANGE_USER、COM_QUIT、COM_SET_OPTION等命令。

**功能优势**

统一读写分离地址，方便维护。 不开通读写分离时，您需要在应用程序中分别配置主实例和每个只读实例的连接地址，才能实现将写请求发往主实例而将读请求发往只读实例。 PolarDB读写分离功能提供一个独享代理地址，您连接该地址后即可对主实例和只读实例进行读写操作， 读写请求被自动转发到对应实例，可降低维护成本。同时，您只需添加只读实例的个数，即可不断扩展系统的处理能力，应用程序无需做任何修改。 原生链路支持，提升性能，减少维护成本。 如果您在云上自行搭建代理层实现读写分离，数据在到达数据库之前需要经历多个组件的语句解析和转发，对响应延迟有较大的影响。而PolarDB读写分离内置在PolarDB原生生态里，能够有效降低延迟，提升处理速度，同时减少客户的维护成本。 可设权重和阈值，符合多场景使用。 您可以设置主实例和只读实例的读请求权重，以及设置只读实例的延迟阈值。 实例健康检查，提升数据库系统的可用性。 读写分离模块将自动对主实例和只读实例进行健康检查，当发现某个实例出现宕机或者延迟超过阈值时， 将不再分配读请求给该实例，读写请求在剩余的健康实例间进行分配。以此确保单个只读实例发生故障时，不会影响应用的正常访问。当实例被修复后，PolarDB会自动将该实例纳回请求分配体系内。

**说明**

为避免单点故障，建议您为一个主实例创建至少两个只读实例。

**注意事项**

当主实例或只读实例变更配置时，可能会出现连接闪断。 新增只读实例后，新建的连接才会被路由到新的只读实例上。 独享代理地址暂不支持SSL加密。 独享代理地址暂不支持压缩协议。 使用独享代理连接地址时，事务请求都会路由到主实例。 使用独享代理连接地址进行读写分离时，不保证非事务读的一致性，业务上有读一致性需求可以封装到事务中。 使用独享代理连接地址时， `show processlist` 会将所有节点的结果合并后返回。 如果开通了短连接优化功能， `show processlist` 可能会显示闲置的用户连接。 如果执行了Multi-Statements或存储过程，当前连接的后续请求会全部路由到主节点，需要断开当前连接并重新连接才能恢复读写分离。 支持Hint语法 `/*FORCE_MASTER*/` 和 `/*FORCE_SLAVE*/` ，但是因为Hint的路由优先级最高，例如 Hint不受一致性、事务的约束，需要您评估是否可以用于业务。另外Hint语句里不能包含改变环境变量的语句，例如 /*FORCE_SLAVE*/ set names utf8; ，可能导致后续业务出错。 据库代理

**前提条件**

**开通读写分离**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据库代理**。
4. 在**读写分离**页签，单击**立即开启**。
5. 设置如下参数。

| 参数 | 说明 |
|---|---|
| 延迟阈值 | 只读实例同步主实例数据时允许的最长延迟时间。若一个只读实例的延迟时间超过该阈值，则不论该只读实例的权重是多少，读请求都不会转发至该只读实例。 取值范围为0秒到3600秒。受限于SQL的执行情况，只读实例有一定的几率会出现延迟，建议该值不小于30秒。 |
| 权重分配 | 实例的读权重越高，处理的读请求越多。例如，假设主实例有3个只读实例，读权重分别为0、100、 200和200，则表示主实例不处理读请求（写请求仍然自动发往主实例），3个只读实例按照1：2：2 的比例处理读请求。 系统分配：系统根据实例规格自动分配各个实例的读权重。后续该主实例下新增的只读实例也会自动按照系统分配的权重加入到读写分离链路中，无需手动设置。 自定义：手动设置各个实例的读权重，范围为0~10000。后续该主实例下新增只读实例的读权重默认为0，需要您手动修改。 |

6. 单击**确定**。

#### 设置读写分离

您可以通过云原生数据库PolarDB控制台设置延迟阈值和自定义读权重分配。

**前提条件**

实例版本为MySQL 5.7或8.0高可用版（本地SSD盘）。

**操作步骤**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**数据库代理**。
4. 单击**读写分离**页签中的**设置读写分离**。
5. 设置如下参数。

| 参数 | 说明 |
|---|---|

据库代理

| 延迟阈值 | 只读实例同步主实例数据时允许的最长延迟时间。若一个只读实例的延迟时间超过该阈值，则不论该只读实例的权重是多少，读请求都不会转发至该只读实例。 取值范围为0秒到7200秒。受限于SQL的执行情况，只读实例有一定的几率会出现延迟，建议该值不小于30秒。 |
|---|---|
| 读权重分配 | 实例的读权重越高，处理的读请求越多。例如，假设主实例有3个只读实例，读权重分别为0、 100、200和200，则表示主实例不处理读请求（写请求仍然自动发往主实例），3个只读实例按照1：2：2的比例处理读请求。 系统分配：系统根据实例规格自动分配各个实例的读权重。后续该主实例下新增的只读实例也会自动按照系统分配的权重加入到读写分离链路中，无需手动设置。 自定义：手动设置各个实例的读权重，范围为0至10000。后续该主实例下新增只读实例的读权重默认为0，需要您手动修改。 |

6. 单击**确定**。

#### 关闭读写分离

**前提条件**

实例版本为MySQL 5.7或8.0高可用版（本地SSD盘）。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏，单击**数据库代理**。
4. 单击**读写分离**页签中的**关闭读写分离**。
5. 在弹出的**关闭读写分离**对话框中，单击**确定**。
控与报警

## 监控与报警

### 查看系统资源和引擎监控

为方便查看和掌握实例的运行状态，PolarDB MySQL版专有云控制台提供了丰富的性能监控项。

**前提条件**

实例版本为MySQL 5.7或8.0双机高可用版（本地SSD盘）。

**操作步骤**

1. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
2. 在左侧导航栏中，单击**监控与报警**。
3. 在**监控与报警**页面，选择**资源监控**、**引擎监控**或**部署监控**，并选择查询时间，即可查看相应的监控数据，
具体监控项介绍如下。

| 类别 | 监控项 | 说明 |
|---|---|---|
| 资源监控 | CPU和内存使用率（%） | 实例的CPU和内存使用率（不含操作系统占用）。 |
|  | 磁盘空间（单位：MByte） | 实例的磁盘空间使用量，包括： 磁盘空间总体使用量。 数据空间使用量。 日志空间使用量。 临时文件空间使用量。 系统文件空间使用量。 |
|  | IOPS（单位：次/秒） | 实例的每秒I/O请求次数。 |
|  | 当前总连接数 | 实例当前总连接数，包括活跃连接数和总连接数。 |
|  | 网络流量（单位：KB） | 实例每秒钟的输入、输出流量。 |
|  | TPS（平均每秒事务数）/QPS（平均每秒SQL语句执行次数） | 平均每秒事务数和平均每秒SQL语句执行次数。 |
|  | InnoDB缓存读命中率、使用率、脏块率（%） | InnoDB缓冲池的读命中率、利用率以及缓冲池脏块的百分比。 |
|  | InnoDB读写量（单位： KB） | InnoDB每秒读取和写入的数据量。 |

控与报警

|  | InnoDB缓存请求次数 | InnoDB每秒钟的读取和写入次数。 |
|---|---|---|
| 引擎监控 |  |  |
|  | InnoDB日志读/写/fsync | InnoDB每秒向日志文件的物理写入次数、日志写请求、向日志文件完成的fsync写数量。 |
|  | MySQL执行语句时在硬盘上自动创建的临时表的数量 | 数据库执行SQL语句时在硬盘上自动创建的临时表的数量。 |
|  | MySQL COMDML _ | 数据库每秒SQL语句执行次数，包括： Insert Delete Insert Select _ Replace Replace Select _ Select Update |
|  | MySQL RowDML _ | InnoDB每秒钟操作执行次数，包括： 每秒向日志文件的物理写次数。 每秒从InnoDB表读取、更新、删除、插入的行数。 |
|  | MySQL ThreadStatus线程 _ 状态 | 实例当前的线程状态。包括： 活跃线程数量。 线程连接数量。 |
|  | InnoDB每秒写入redo log日志量 （单位：bytes/s） | InnoDB平均每秒钟写入的数据量。 |
|  | MySQL ROW LOCK _ _ | InnoDB行锁等待次数和时长。包括： Innodb row lock waits：从数据库系统启动以来，行锁等待的总 _ _ _ 次数。 Innodb row lock time avg：平均行锁等待时长。 _ _ _ _ Innodb row lock time：所有InnoDB行锁等待时间的总和。 _ _ _ |
|  | MySQL SelectScan _ | 每秒全表扫描的次数。 |
| 部署监控 | 备节点复制线程状态 | 备节点复制线程状态。包括备节点IO线程状态和备节点SQL线程状态。 |
|  | 备节点复制延迟（单位： 秒） | 备节点复制延迟时间。 |

控与报警

### 设置报警规则

您可以通过PolarDB MySQL版专有云控制台创建报警规则，帮助您及时了解实例的监控数据异常并快速进行处理。

**前提条件**

实例版本为MySQL 5.7或8.0双机高可用版（本地SSD盘）。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**监控与报警**。
4. 在**报警**页签，单击**报警规则设置**。
5. 在**报警规则**页面，单击**创建告警规则**。
6. 在**创建**/**修改告警规则**页面，设置以下参数。

| 参数 | 说明 |
|---|---|
| 云产品选择 | 默认值，无需选择。 |
| 资源范围 | 报警规则的作用范围，取值范围如下： 实例维度：选择当前组织资源集下的一个或多个目标实例。 资源集维度：选择当前组织和地域下的目标资源集。 应用分组维度：选择当前组织和地域下的应用分组。 全部资源：报警规则作用于指定云产品的全部资源上，对于新加入的资源生效。 |
| 报警规则描述 | 报警规则的主体。当监控数据满足报警条件时，触发报警规则。 规则描述的设置方法如下： i. 单击创建报警规则。 ii. 在创建报警规则页面，设置规则名称、监控指标、监控维度、阈值及报警级别等。 iii. 单击确定。 |
| 沉默通道周期 | 报警发生后未恢复正常，间隔多久重复发送一次报警通知。取值：5分钟、15分钟、30 分钟、1小时、3小时、6小时、12小时和24小时。 当某监控指标超出报警阈值时触发报警，如果监控指标在通道沉默周期内持续超过报警阈值，在通道沉默周期内不会重复发送报警通知；如果监控指标在通道沉默周期后仍未恢复正常，则云监控将再次发送报警通知。 例如，当通道沉默周期设置为12小时时，如果超出报警阈值的监控指标在首次触发报警后12小时仍未恢复正常，云监控将再次发送报警通知。 |
| 生效时间 | 报警规则的生效时间。报警规则只在生效时间内检查监控数据是否超出报警阈值。 |

控与报警

| 报警回调 | 用于接收云监控通过POST请求推送报警消息的回调地址。 说明报警回调地址必须是云监控可访问的域名地址，仅支持HTTP协议，不支持填写 IP。 |
|---|---|
| 无数据处理方法 | 无报警时的处理方法。取值范围如下： 不做任何处理：无报警时不做任何处理。 发送无数据报警：无报警时发送无数据报警给报警联系人。 |
| 报警联系人 | 选择报警信息发送的用户。 |

7. 单击**确定**。
监控

## 云监控

### 查看监控大盘指标

云监控（CloudMonitor，CMS）页面提供了丰富的性能监控项和秒级监控频率，方便您掌握集群或实例的运行状态并通过细粒度的监控数据快速定位运维问题。

**监控大盘**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 您可以通过如下两种方式查看云监控信息。
i. 方式一 a. 在目标列表页面，单击目标实例或集群ID。 b. 在左侧导航栏中，选择**云监控**。 ii. 方式二 a. 在目标列表页面，单击目标实例监控列下的图标。 b. 查看相关监控数据。
4. 您可以根据业务需求选择查看所需的监控信息，相关监控指标请参见**《云监控****CMS****用户指南》**中**云监控**
**指标说明**-**数据库**章节。

**说明**

在**时间粒度**下拉框，您可以根据业务需求选择查看监控信息的时间段，支持查看**最近**1**分钟**到**最近****30** 天的数据。

### 报警历史

当报警发生后，可以查看报警历史信息。支持导出并下载报警历史信息，便于在本地进行数据分析。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击目标实例或集群ID。
4. 在左侧导航栏，单击**云监控**，选择**报警服务** > **报警历史**。
5. （可选）在**报警历史**页面，可通过**规则****ID**、**规则名称**、**报警级别**和时间来筛选报警历史记录。
6. 在报警历史页面，执行以下操作。

| 操作任务 | 操作步骤 |
|---|---|

监控

| 查看报警历史 | 在报警历史列表中，可以直接查看目标报警历史的产品名称、故障实例、发生时间、规则名称、状态、等级和通知对象。单击目标报警历史对应规格名称，可以查看报警规则详情。 说明报警历史默认支持查询最近2天的数据。 |
|---|---|
| 导出报警历史 | i. 在报警历史页面，单击页面右上方的 。 ii. 在导出任务对话框中，设置时间选择和任务名称后，单击确定。 |

### 报警规则

#### 创建报警规则

**背景信息**

报警规则在生效时间内，根据默认的探测频率检测报警指标是否超出所设定的阈值，一旦检测到云产品监控指标超出阈值（出现异常），按照设定的报警联系人或其他报警信息处理平台进行告警。

**说明**

最小报警探测频率为每分钟一次。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击目标实例或集群ID。
4. 在左侧导航栏，单击**云监控**，选择**报警服务** > **报警规则**。
5. 单击列表上方的**创建报警规则**。
6. 在**创建报警规则**面板中，根据实际需要设置相应配置项。

| 配置项 | 说明 |
|---|---|
| 云产品选择 | 默认，无需选择。 |
| 资源范围 | 报警规则关联资源的范围，支持以下几类。不同云产品可选择的范围类型存在一定差异。 实例维度：选择当前组织资源集下的一个或多个目标实例。 资源集维度：选择当前组织和地域下的目标资源集。 应用分组维度：选择当前组织和地域下的应用分组。 全部资源：默认不支持选择。 |

监控

| 资源选择 | 根据资源范围的选择，选择具体的资源实例、资源集或应用分组。 |
|---|---|
| 报警规则描述 | 报警规则的主体。当监控数据满足报警条件时，触发报警规则。 规则描述设置方法： i. 单击创建报警规则。 ii. 在创建报警规则面板，设置规则名称、指标维度、监控指标、阈值及报警级别等。 说明指标维度仅在资源范围选择实例维度时才会显示。 iii. 单击确认。 |
| 通道沉默周期 | 报警发生后未恢复正常，间隔多久重复发送一次报警通知。取值：5分钟、15分钟、30分钟、1小时、3小时、6小时、12小时和24小时。 当某监控指标超出报警阈值时触发报警，如果监控指标在通道沉默周期内持续超过报警阈值，在通道沉默周期内不会重复发送报警通知；如果监控指标在通道沉默周期后仍未恢复正常，则云监控将再次发送报警通知。 例如，当通道沉默周期设置为12小时时，如果超出报警阈值的监控指标在首次触发报警后12 小时仍未恢复正常，云监控将再次发送报警通知。 |
| 生效时间 | 报警规则的生效时间。报警规则只在生效时间内检查监控数据是否超出报警阈值。 |
| 报警回调 | 用于接收云监控通过POST请求推送报警消息的回调地址。 说明报警回调地址必须是云监控可访问的域名地址，仅支持HTTP协议，不支持填写IP。 |
| 无数据处理方法 | 无监控数据时报警的处理方式。 不做任何处理发送无数据报警 |
| 报警联系人 | 选择报警信息发送的用户组或用户。 默认的云账号报警联系人组是一个空账号，可用于测试报警规则的有效性。 |

7. 单击**确定**。

**规则描述配置项说明**

| 配置项 | 说明 |
|---|---|
| 规则名称 | 填写报警规则名称。 |

监控

| 监控指标 | 从当前报警规则所选择的云产品的所有监控指标中，选择目标指标项。各云产品的监控指标详情可参见云产品监控指标说明。 |
|---|---|
| 指标维度 | 指除实例ID之外的其他维度。仅在资源范围选择实例维度时才会显示。 |
| 阈值及报警级别（单位：%） | 报警级别分为紧急、警告和普通。 监控数据的聚合值类型可以选择平均值、最小值和最大值。 监控数据的周期可以选择连续、连续5个周期、连续10个周期、连续15个周期、连续30个周期、连续60个周期。 实际监控数据与报警阈值之间的比较关系，支持 “>”、“ >=”、“<”、“<= ”、“=”、 “!=”、“同比昨天同时间上涨”、“同比昨天同时间下降”、“环比上周期上涨”、“环比上周期下降”、“比上周期增量”、“比上周期降量”的选择。还支持设置阈值和触发次数，当监控数据达到设置的阈值的触发次数时，产生报警。 |

**规则配置示例**

为数据库实例创建一个名为example的报警规则，用于监控目标数据库实例的CPU使用率，当CPU使用率峰值（最大值）在五个探测周期内有三次大于等于70%的情况时触发报警，且报警级别为紧急。 适用于此场景的规则描述配置如下图所示。 监控

#### 管理报警规则

在报警规则列表中，可以对报警规则进行修改、禁用、启用、删除等操作。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击目标实例或集群ID。
4. 在左侧导航栏，单击**云监控**，选择**报警服务** > **报警规则**。
5. 选择目标报警规则，执行相关操作。

| 操作任务 | 操作步骤 |
|---|---|
| 查看报警规则详情 | 单击目标报警规则操作列的详情，在报警规则/报警历史/故障资源面板中可查看报警规则的详细信息。 |
| 判断规则有效性 | 单击目标报警规则有效性列的点击巡检，在有效性列可查看巡检结果。 说明若巡检结果异常，可单击检测结果，在弹出的面板中查看告警规则执行异常检测、告警规则加载检测、无效报警规则检测和告警规则回调检测结果。 单击重新检测，可重新检测规则有效性。 |
| 查看规则执行记录 | 单击目标报警规则规则执行记录列的查看规则执行记录，在报警规则执行记录面板中，可通过时间范围筛选执行记录。 |
| 修改报警规则 | i. 单击目标报警规则操作列的编辑。 ii. 在修改报警规则面板中，修改报警规则。相关配置参数说明请参见《创建报警规则》。 iii. 修改完成后，单击确定。 |
| 禁用报警规则 | 当需要手动停止云产品的服务，进行维护或升级时，可以禁用报警规则，避免因人为变更而收到大量且无用的报警通知。 说明请先确认报警规则的状态为正常后，再进行禁用。 单个禁用 a. 单击目标报警规则操作列的图标，单击禁用。 b. 在禁用报警规则对话框中，单击确定。 批量禁用 a. 选中目标报警规则前的复选框，然后单击列表左下角的禁用。 b. 在禁用报警规则对话框，单击确定。 |

监控

| 启用报警规则 | 完成云产品的维护或升级后，可以重新启用已被禁用的报警规则。 说明请先确认报警规则的状态为已禁用后，再进行禁用。 单个启用 a. 单击目标报警规则操作列的启用。 b. 在启用报警规则对话框中，单击确定。 批量启用 a. 选中目标报警规则前的复选框，然后单击列表左下角的启用。 b. 在启用报警规则对话框，单击确定。 |
|---|---|
| 删除报警规则 | 单个删除 a. 单击目标报警规则操作列的图标，单击删除。 b. 在删除报警规则对话框中，单击确定。 批量删除 a. 选中目标报警规则前的复选框，然后单击列表左下角的删除。 b. 在删除报警规则对话框中，单击确定。 |

据安全性

## 数据安全性

### 设置白名单

为了数据库的安全稳定，在创建PolarDB MySQL版实例后，需要先修改实例的白名单，将需要访问实例的 IP地址或者IP段加入到PolarDB MySQL版实例的白名单中。

**背景信息**

白名单可以让PolarDB MySQL版实例得到高级别的访问安全保护，建议您定期维护白名单。设置白名单不会影响PolarDB MySQL版实例的正常运行。 设置IP白名单：添加IP地址，允许这些IP地址访问该PolarDB MySQL版实例。 设置ECS安全组：添加ECS安全组，允许ECS安全组内的ECS实例访问该PolarDB MySQL版实例。

**说明**

若ECS实例需通过内网地址访问PolarDB，请确保两者位于同一地域且网络类型一致（如均为VPC）， 否则即使配置白名单也无法连通。

**注意事项**

默认的IP白名单分组只能被修改或清空，不能被删除。 每个IP白名单分组最多添加1000个IP或IP段。当IP较多时，建议合并为IP段填入，例如IPv4 的 `192.168.1.0/24` 或IPv6的 `2001:db8::/32` 。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**数据安全性**。
4. 在**白名单设置**页签中，执行以下任一操作：
编辑默认分组：单击 `default` 分组后的**编辑**。 新建自定义分组：单击**添加白名单分组**，创建时可指定网络类型为IPv4或IPv6，实现协议栈隔离管控。
5. 在弹出的面板中，您可以：
删除已有IP地址或网段。 单击**新增****IP**，输入需授权的IP地址或CIDR网段（如 `10.10.10.0/24` 表示 `10.10.10.x` 全网段均可访问）。

**说明**

多个条目请用英文逗号（,）分隔，逗号前后不得包含空格，例如：IPv4的 `192.168.1.0/24` 或 IPv6的 `2001:db8::/32` 。 单击**加载****ECS****内网****IP**，自动列出当前账号下所有ECS实例内网IP，便于快速选择。 单击**导入文件（****.txt**），可批量导入 `.txt` 格式的IP列表。 据安全性

**说明**

在 `default` 分组中新增IP后，系统将自动移除默认保留地址 `127.0.0.1` 。

### 设置SSL加密

为了提高链路安全性，您可以启用SSL（Secure Sockets Layer）加密，并安装SSL CA证书到需要的应用服务。SSL在传输层对网络连接进行加密，能提升通信数据的安全性和完整性，但会同时增加网络连接响应时间。

**前提条件**

实例版本为MySQL 5.7或8.0双机高可用版。

**注意事项**

SSL的证书有效期为1年，请在1年内更新证书有效期，否则使用加密连接的客户端程序将无法正常连接。 由于SSL加密的固有缺陷，启用SSL加密会显著增加CPU使用率，建议您仅在外网链路有加密需求的时候启用SSL加密。内网链路相对较安全，一般无需对链路加密。 读写分离地址不支持SSL加密。 关闭SSL加密会重启实例，请谨慎操作。

**开启SSL加密**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中，单击**数据安全性**。
4. 单击**SSL**页签。
5. 单击**未开通**前面的开关。
6. 在**设置****SSL**对话框中，选择要开通SSL加密的地址，单击**确定**。
7. 单击**下载****CA****证书**，下载SSL CA证书。
下载的文件为压缩包，包含如下三个文件： p7b文件：用于Windows系统中导入CA证书。 PEM文件：用于其他系统或应用中导入CA证书。 JKS文件：java中的truststore证书存储文件，密码统一为apsaradb，用于Java程序中导入CA证书链。

**说明**

在java中使用JKS证书文件时，jdk7和jdk8需要修改默认的jdk安全配置，在需要SSL访问的数据库所在机器的 `jre/lib/security/java.security` 文件中，修改如下两项配置：

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224 jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024
```

若不修改jdk安全配置，会报如下错误。其它类似报错，一般也都由Java安全配置导致。

```
javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm c onstraints
```

据安全性

**配置SSL CA证书**

开通SSL加密后，应用或者客户端连接PolarDB时需要配置SSL CA证书。本文以MySQL Workbench和 Navicat为例，介绍SSL CA证书的安装方法。其它应用或者客户端请参见对应产品的使用说明。

**MySQL Workbench配置方法**

1. 打开MySQL Workbench。
2. 选择**Database > Manage Connections**。
3. 启用**Use SSL**，并导入SSL CA证书，如下图所示。

**Navicat配置方法**

1. 打开Navicat。
2. 在目标数据库上单击鼠标右键，选择**编辑连接**。
据安全性
3. 单击**SSL**页签，选择.pem格式CA证书的路径，参照下图进行设置。
4. 单击**确定**。

**说明**

如果报 `connection is being used` 错误，是由于之前的会话未断开，请关闭Navicat重新打开。
5. 双击目标数据库测试能否正常连接。

**更新证书有效期**

**说明**

**更新有效期**操作将会重启实例，重启前请做好业务安排，谨慎操作。
1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
据安全性
3. 在左侧菜单栏中，单击**数据安全性**。
4. 单击**SSL**页签。
5. 单击**更新有效期**。
6. 在弹出的**更新****SSL****证书有效期**对话框中，单击**确定**。

**关闭SSL加密**

**说明**

关闭SSL加密会重启PolarDB实例，系统会触发主备切换降低影响，但仍建议您在业务低峰期操作。 SSL加密关闭后，数据库访问性能会有一定程度提升，但安全性上会有削弱，因此在非安全环境下不建议关闭SSL加密。
1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中，单击**数据安全性**。
4. 单击**SSL**页签。
5. 单击**已开通**前面的开关，在弹出的提示框中单击**确定**。

### 设置透明数据加密TDE

透明数据加密TDE（Transparent Data Encryption）可对数据文件执行实时I/O加密和解密，数据在写入磁盘之前进行加密，从磁盘读入内存时进行解密。TDE不会增加数据文件的大小，开发人员无需更改任何应用程序，即可使用TDE功能。

**前提条件**

实例类型为MySQL 5.7或8.0双机高可用版（本地SSD盘）。 已开通KMS。如果您未开通KMS，可在开通TDE过程中根据引导开通KMS。

**背景信息**

加密使用的密钥由密钥管理服务（KMS）产生和管理，PolarDB不提供加密所需的密钥和证书。部分可用区不仅可以使用阿里云自动生成的密钥，也可以使用自带的密钥材料生成数据密钥，然后授权PolarDB使用。

**注意事项**

**说明**

开通TDE加密功能的实例，误删后支持通过回收站进行数据恢复。 TDE开通过程中会重启实例造成连接中断，请做好业务安排，谨慎操作。 TDE开通后无法关闭。 TDE开通后无法修改密钥。 TDE开通后，用户如果要恢复数据到本地，需要先通过PolarDB解密数据。 TDE开通后，会显著增加CPU使用率。 使用已有自定义密钥时，需要注意： 禁用密钥、设置密钥删除计划或者删除密钥材料都会造成密钥不可用。 据安全性撤销授权关系后，重启PolarDB实例会导致PolarDB实例不可用。 需要使用主账号或者具有AliyunSTSAssumeRoleAccess权限的账号。

**使用由阿里云自动生成的密钥**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**数据安全性**。
4. 在**TDE**页签单击**未开通**左边的滑块。
5. 在**TDE****设置**对话框中，选择**使用由阿里云自动生成的密钥**，单击**确定**。

**使用已有自定义密钥**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中单击**数据安全性**。
4. 在**TDE**页签，单击**未开通**左边的滑块。
5. 在**TDE****设置**对话框中，选择**使用已有自定义密钥**，选择密钥，单击**确定**。

**说明**

如果没有自定义密钥，需要单击**前往创建**。

**加密操作**

登录数据库，执行如下命令，对要加密的表进行加密。

```
ALTER TABLE <tablename> engine＝innodb,encryption='Y';
```

**解密操作**

如果您要对TDE加密的表解密，请执行如下命令。

```
ALTER TABLE <tablename> engine＝innodb,encryption='N';
```

**常见问题**

Q：开启TDE后，常用数据库工具（Navicat等）还能正常使用吗？ A：可以正常使用。 Q：加密后查看数据为什么还是明文的？ A：查询数据时会解密并读取到内存，所以是明文显示。开启TDE可以防止备份泄露导致数据泄露，备份文件是加密的，无法用于恢复到本地，如果要恢复数据到本地，需要先解密数据。

### SQL审计

**背景信息**

PolarDB MySQL版的增量数据可以通过SQL审计或Binlog日志来查看，但是两者又有区别： 据安全性 SQL审计：类似于MySQL的审计日志，会统计所有DML和DDL操作信息，这些信息是系统通过网络协议分析所得。SQL审计不解析实际的参数值，在SQL查询量较大的时候会丢失少量记录。因此通过这种方式来统计增量数据可能会出现不准确的情况。 Binlog日志：准确记录数据库所有的增、删、改操作信息以及恢复用户的增量数据。Binlog日志先暂存在实例中，系统定期将实例中已经写完数据的Binlog日志转移至OSS保存7天。无法保存正在写入数据的 Binlog文件，所以在**备份恢复**页面，单击**一键上传****Binlog**后仍有部分Binlog日志没有被上传。这种方式可以准确记录数据库的增量数据，但是无法获取实时日志。

**注意事项**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中，单击**数据安全性**。
4. 单击**SQL****审计**页签。
您可以通过时间范围、数据库名称、数据库用户、关键词搜索或按Top SQL 耗时排序等条件查询SQL信息。

**说明**

SQL审计功能关闭后，包括历史审计内容在内的SQL审计记录会被清空。请将SQL审计内容导出并妥善
1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧菜单栏中，单击**数据安全性**。
4. 单击**SQL****审计**页签。
5. 单击**导出文件**，将SQL审计内容导出并妥善保存至本地。
6. 导出文件后，单击**关闭****SQL****审计**。
7. 在弹出的确认框中，单击**确定**。

**切换审计日志存储位置**

审计日志默认存储在SLS-inner，为缓解海量审计日志写入SLS-inner引发的性能压力，保障专有云平台管控平面稳定性及监控采集链路的正常运行，可根据需要将审计日志存储位置切换至SLS-PUB。
1. 登录云原生数据库PolarDB控制台。
2. 在左侧导航栏，单击**实例列表**，单击目标实例ID进入**基本信息**页面。
3. 在左侧菜单栏中，单击**数据安全性**。
4. 在页面右侧，单击**SQL****审计**页签。
据安全性
5. 开启审计日志存储至SLS-PUB。

**重要**

切换后无法回退，请谨慎操作。 务可用性

## 服务可用性

### 自动或手动主备切换

您可以设置主备实例自动切换或手动切换，切换后原来的主实例会变成备实例。

**背景信息**

自动切换：实例默认为自动切换，当主实例出现故障无法访问时，会自动切换到备实例。 手动切换：您可以随时手动对主备库进行切换。

**说明**

主备实例的数据会实时同步，您只能访问主实例，备实例仅作为备份形式存在，不提供业务访问。

**注意事项**

主备实例切换过程中可能会有闪断，请确保您的应用程序具有自动重连机制。 如果实例下挂载有只读实例，那么主备实例切换后，只读实例的数据会有几分钟的延迟，因为需要重建复制链路、同步增量数据等。

**手动切换主备实例**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，选择**服务可用性**。
4. 在页面右侧单击**主备库切换**。

**说明**

实例主备切换过程中可能会有1~2次闪断，请确保应用具备重连机制。
5. 在弹出的**实例主备切换**对话框中，选择主备切换时间，单击**确定**。

**常见问题**

Q：备实例可以访问吗？ A：不可以访问。您只能访问主实例，备实例仅作为备份形式存在，不提供业务访问。

### 修改数据复制方式

您可以根据自身业务特点，设置PolarDB MySQL主备实例之间的数据复制方式，以提高数据库可用性。

**前提条件**

实例版本为MySQL 5.7或8.0双机高可用版（本地SSD盘）。

**复制方式介绍**

半同步应用发起的更新在主实例执行完成后，会将日志同步传输到备实例，备实例收到日志，事务就算完成了提交，不需要等待备实例执行日志内容。 当备实例不可用或者主备实例间出现网络异常时，半同步会退化为异步。 务可用性异步应用发起更新请求，即进行增加、删除、修改数据的操作时，主实例完成操作后会立即响应应用，同时主实例向备实例异步复制数据。因此，在异步数据复制方式下，备实例不可用时不会影响主实例上的操作， 而主实例不可用时会引起主备库数据不一致的概率较低。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧的**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**服务可用性**。
4. 在页面右侧单击**修改数据复制方式**。
5. 在弹出的对话框中，选择数据复制方式，单击**确定**。

**常见问题**

Q：使用哪种数据复制方式好呢？ A：根据您的业务需求进行选择。如果要求极高的响应速度，建议您使用异步；其他情况下可以使用折中的方案，即半同步。

## 数据库备份与恢复

### 自动备份

PolarDB自动备份支持全量物理备份，PolarDB按照设定的备份策略自动备份数据。本章将介绍如何设置自动备份的备份策略。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**备份恢复**。
4. 在**备份设置**页签，单击**编辑**。

**说明**

为了确保数据安全，修改备份设置后，系统会将新设置的周期和时间与原设置进行对比，选择其中最近的时间点进行备份。即下一次备份可能仍会按原设置的周期和时间进行。例如原设置为星期三 19:00-20:00，您在星期三19:00之前修改设置为星期四19:00-20:00，系统在星期三19:00-20:00 仍然会进行备份。
5. 设置如下参数。

| 配置 | 说明 |
|---|---|
| 数据备份保留天数 | 数据备份文件可以保留7~730天，默认为7天。 |
| 备份周期 | 可以设置为一星期中的某一天或者某几天。 |
| 备份时间 | 可以设置为一天的任意时段，以小时为单位。建议设置为业务低峰期时间。 |
| 保留时长 | 设置常规备份（热备）的保留时长和实例释放前是否长期保留。 说明数据备份超过730天的备份集自动转化为归档备份，归档备份的保留天数大于等于30 天。 |
| 日志备份 | 可以设置是否开启日志备份。 重要关闭日志备份会导致所有日志备份被清除，并且无法使用按时间点恢复数据的功能。 |

| 日志备份保留天数 | 日志备份文件保留的天数，保留7～730天，默认为7天。 |
|---|---|

6. 完成上述参数配置后，单击**保存**。

### 手动备份

手动备份支持全量物理备份和全量逻辑备份，本章节介绍如何手动备份PolarDB数据。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 单击**基本信息**页面右上角的**备份实例**。
4. 设置好备份方式、备份策略，单击**确定**。

**说明**

备份方式有如下两种： 物理备份：直接备份所有数据库中的文件。 逻辑备份：通过SQL从数据库中抽取数据并以文本的形式进行备份。选择逻辑备份后，还需要选择备份策略： 实例备份：备份整个实例。 单库备份：备份实例中的某一个数据库。

### 下载数据备份和日志备份

为保障用户权益，PolarDB提供了未加密的数据备份和日志备份下载，方便用户存档，也可用于恢复到本地数据库。

**下载限制**

| 数据库类型 | 数据备份下载 | 日志备份下载 |
|---|---|---|
| MySQL | MySQL 5.7或8.0 本地SSD盘：支持下载全量的物理备份和逻辑备份。 | 所有版本均支持下载日志备份。 |

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中单击**备份恢复**。
4. 根据想要下载的备份类型，选择相应的标签页：
下载数据备份：选择**数据备份**页签。 下载日志备份：选择**日志备份**页签。
5. 选择要查询的时间范围。
6. 找到目标的数据备份或日志备份，并单击其对应**操作**栏中的**下载**。

**说明**

若数据备份用于数据恢复，请选择离要恢复的时间点最近的数据备份文件。 若日志备份是用于恢复到本地数据库，请注意如下事项： 日志备份的Binlog所在实例编号必须与数据备份的备份所在实例编号一致。 日志备份的起始时间段必须在您选择的数据备份时间点之后，在要恢复数据的时间点之前。
7. 在弹出的菜单中单击**已了解，要公网下载**。即可通过浏览器直接下载备份文件。

**说明**

在Linux系统中下载时，可以使用如下命令： `wget -c '<`备份文件下载地址`>' -O <`文件名称> -c：启用断点续传模式。 -O：将下载的结果保存为指定的文件名，建议您使用URL中包含的原文件名。 下载地址有多个参数时建议为下载地址添加单引号，避免下载失败。

### 一键上传Binlog

**背景信息**

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**备份恢复**，进入**备份恢复**页面。
4. 单击页面右上角的**一键上传****Binlog**。
5. 在弹出的**上传****Binlog**对话框中，单击**确定**。

### 数据库恢复

克隆实例是指新建一个实例，可以复制出与主实例一模一样的内容，包括实例数据和实例设置。克隆实例主要用于恢复主实例数据，或批量创建相同实例。

**前提条件**

创建克隆实例时，主实例需要满足如下条件： 主实例状态为运行中。 当前没有迁移任务。 已开启数据备份和日志备份。 若要按备份集克隆实例，则主实例必须至少有一个已完成备份的备份集。

**背景信息**

创建克隆实例有两种方式，分为指定备份集创建和指定有效期内备份的时间点创建。

**说明**

克隆实例仅复制主实例的内容，不复制主实例下只读实例的内容。复制内容包括主实例的数据库信息、账号信息和实例设置。例如白名单设置、备份设置、参数设置、阈值报警设置等。 克隆实例的数据库类型需要与主实例一致，其它设置均可与主实例不同。例如系列、可用区、网络类型、实例规格、存储空间等。若创建克隆实例是用于恢复主实例数据，建议您选择大于主实例的规格和存储空间，否则因性能限制，数据恢复所需时间可能会较长。 克隆实例的账号类型需要与主实例一致，但可以修改克隆实例的账号密码。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**备份恢复**。
4. 在**数据备份**的备份列表中，找到要恢复的备份，单击操作栏中的**恢复**。
5. 在弹出的**恢复**窗口中，单击**确定**
6. 在**PolarDB****恢复**页面，设置如下参数。

| 项目 | 选项 | 说明 |
|---|---|---|
| 区域 | 地域 | PolarDB实例所在地域。 |
| 数据库恢复 | 还原方式 | 主实例数据的还原方式，支持以下两种： 按时间点按备份集 |
|  | 还原时间 | 选择需要还原到的时间。 说明当还原方式为按时间点时，需要填写该参数。 |
|  | 备份集 | 选择需要还原的备份集。 说明当还原方式为按备份集时，需要填写该参数。 |
|  | 实例名称 | 克隆实例的名称。 |
|  | 数据库类型 | 数据库的类型，不可修改。 |

| 原生数据库 |  |  |
|---|---|---|
| 规格配置 |  |  |
|  | 数据库版本 | 数据库的版本，不可修改。 |
|  | 系列 | 数据库的系列，请以控制台界面为准。 |
|  | 存储类型 | 数据库的存储类型，请以控制台界面为准。 |
|  | 实例规格 | 克隆实例的实例规格。 说明建议您选择大于主实例的规格和存储空间，否则因性能限制，数据恢复所需时间可能较长。 |
|  | 存储空间 | 存储空间包括数据空间、系统文件空间、Binlog文件空间和事务文件空间。实际可用存储空间请以控制台界面为准。 说明本地SSD盘的独享套餐等规格，由于资源独享的原因，存储空间大小和实例规格绑定。 |
| 网络类型 | 网络类型 | PolarDB实例支持的网络类型： 经典网络：经典网络中的云服务在网络上不进行隔离，只能依靠云服务自身的安全组或白名单策略来阻挡非法访问。 专有网络：（Virtual Private Cloud，简称VPC）专有网络帮助用户在阿里云上构建出一个隔离的网络环境。用户可以自定义专有网络内的路由表、IP地址范围和网关。建议您选择专有网络，更加安全。 |
|  | VPC | 选择您的VPC。 说明当网络类型为专有网络时，需要填写该参数。 |
|  | VSwitch | 选择VPC下的交换机。 说明当网络类型为专有网络时，需要填写该参数。 |

7. 完成上述参数配置后，单击**提交**。

### Native Flashback

Native Flashback功能可以通过SQL语句查询或恢复指定时间点的数据，保证在误操作后可以快速获取历史数据。

**功能说明**

数据库运维过程中的误操作可能会给业务带来严重的影响，常见的恢复手段通过备份集恢复，需要额外的系统资源，在数据量较大时恢复时间不可控。 PolarDB MySQL版设计和实现了Native Flashback功能，无需复杂的恢复操作，通过简单的SQL语句即可查询或恢复误操作前的历史数据，节省了大量宝贵的时间，保证业务平稳运行。

**前提条件**

实例为PolarDB MySQL8.0集群系列。 内核小版本为8.0.0.1.42.1及以上。如何查看或升级内核小版本，请参见升级内核小版本。

**注意事项**

仅支持使用InnoDB引擎的表。 需要消耗额外的undo表空间，可以通过innodb_undo_space_supremum_size进行配置。 Native Flashback的查询结果取最接近指定时间点的数据，不保证查询到的数据与指定时间点的数据完全匹配。 暂不支持跨DDL操作的历史版本数据查询和恢复。例如您无法通过Native Flashback查询某个已经被删除的表的内容。

**语法**

Native Flashback提供了全新的 `AS OF` 语法，通过该语法指定需要回滚的时间。语法规则如下：

```
SELECT ... FROM <表名>
  AS OF TIMESTAMP <表达式>;
```

其中，在表达式中指定回滚的时间，该表达式支持多种形式，示例：

```
SELECT ... FROM tablename
  AS OF TIMESTAMP '2020-11-11 00:00:00';
SELECT ... FROM tablename
  AS OF TIMESTAMP now();
SELECT ... FROM tablename
  AS OF TIMESTAMP (SELECT now());
SELECT ... FROM tablename
  AS OF TIMESTAMP DATE_SUB(now(), INTERVAL 1 minute);
```

**参数说明**

| 参数名称 | 级别 | 说明 |
|---|---|---|

| innodb rds flashbac _ _ k task enabled _ _ | Global | Native Flashback的功能开关。 OFF（默认）：关闭。 ON：开启。 说明关闭Native Flashback功能时，需要同步将innodb undo retention参数设置为 _ _ 0。 命令行格式： --innodb-rds- flashback-task-enabled=# 。 |
|---|---|---|
| innodb undo retenti _ _ on | Global | 描述：undo记录的保留时长，超出该时长的undo记录无法查询。 取值范围：0~4294967295。默认值：0。单位：秒。 说明该参数的值越大，Native Flashback支持的回档查询时间越长，同时undo表空间占用的存储空间也会上升。 innodb rds flashback task enable _ _ _ _ d参数设置为OFF时，需同步将本参数设置为0。 命令行格式： --innodb-undo- retention=# 。 |
| innodb undo space _ _ _ supremum size _ | Global | undo表空间可占用的最大磁盘空间。 取值范围：0~4294967295。默认值：10240。单位： MB。 说明占用空间超过这个值时，忽略 innodb undo retention 参数强 _ _ 制清理undo记录。 命令行格式： --innodb-undo-space- supremum-size=# 。 |

|  |  |  | --innodb-rds- |  |
|---|---|---|---|---|
|  |  | flashback-task-enabled=# |  |  |

|  |  |  | --innodb-undo- |  |  |
|---|---|---|---|---|---|
|  |  | retention=# |  |  |  |

|  |  |  | --innodb-undo-space- |  |  |
|---|---|---|---|---|---|
|  |  | supremum-size=# |  |  |  |

| innodb undo space _ _ _ reserved size _ | Global |  | 预留的undo表空间大小， 在 innodb undo retention 参数非0的情况下，将 _ _ 使用这部分空间尽可能多地保留undo记录。 取值范围：0~4294967295。默认值：0。单位： MB。 说明该参数的值太大可能导致undo历史记录过多，影响实例性能。如非必要，请保持该参数为0。 命令行格式： --innodb-undo-space- reserved-size=# 。 |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  | --innodb-undo-space- |  |  |
|  |  |  |  | reserved-size=# |  |  |  |

**使用示例**

# 获取时间点

```
MySQL> SELECT now(); +---------------------+
| now()               |
+---------------------+
| 2025-05-23 15:43:09 |
+---------------------+ 1 row in set (0.00 sec)
```

# 查看数据

```
MySQL > SELECT * FROM mt1; +----+------+
| id | c1   |
+----+------+
|  1 |    1 |
|  2 |    2 |
|  3 |    3 |
|  4 |    4 |
|  5 |    5 |
+----+------+ 5 rows in set (0.00 sec)
```

# 不带`WHERE`条件的更新操作

```
MySQL > UPDATE mt1 SET c1 = 100; Query OK, 5 rows affected (0.00 sec) Rows matched: 5 Changed: 5 Warnings: 0 MySQL > SELECT * FROM mt1; +----+------+
| id | c1   |
+----+------+
|  1 |  100 |
|  2 |  100 |
|  3 |  100 |
|  4 |  100 |
```

|
5|

```
100|
```

```
|  5 |  100 |
+----+------+ 5 rows in set (0.00 sec)
```

# 查询历史时间点的数据，成功返回结果

```
MySQL > SELECT * FROM mt1 AS OF timestamp '2020-10-14 15:44:09'; +----+------+
| id | c1   |
+----+------+
|  1 |    1 |
|  2 |    2 |
|  3 |    3 |
|  4 |    4 |
|  5 |    5 |
+----+------+ 5 rows in set (0.00 sec)
```

# 如果超出保留的历史数据范围，返回失败

```
MySQL > SELECT * FROM mt1 AS OF timestamp '2020-10-13 14:44:09'; ERROR 7545 (HY000): The snapshot to find is out of range
```

# 开始恢复数据
MySQL > CREATE TABLE mt1_tmp LIKE mt1; # 创建一个与原表结构相同的临时表

```
Query OK, 0 rows affected (0.03 sec) MySQL > INSERT INTO mt1_tmp
             -> SELECT * FROM mt1 AS OF
```

-> TIMESTAMP '2020-10-14 15:44:09'; # 将原表中的历史数据写入临时表

```
Query OK, 5 rows affected (0.01 sec) Records: 5 Duplicates: 0 Warnings: 0
```

MySQL > SELECT * FROM mt1_tmp; # 确认临时表中的数据是否正确

```
+----+------+
| id | c1   |
+----+------+
|  1 |    1 |
|  2 |    2 |
|  3 |    3 |
|  4 |    4 |
|  5 |    5 |
+----+------+ 5 rows in set (0.00 sec) MySQL > rename TABLE mt1 TO mt1_bak,
```

-> mt1_tmp TO mt1; #（进行本操作需要先停止业务读写）更改原表表名为`mt1_bak`，并将临时表名改成原表表名，完成数据恢复

```
Query OK, 0 rows affected (0.02 sec)
```

MySQL > SELECT * FROM mt1; # 确认恢复完成后的数据

```
+----+------+
| id | c1   |
+----+------+
|  1 |    1 |
|  2 |    2 |
```

```
|  3 |    3 |
|  4 |    4 |
|  5 |    5 |
+----+------+ 5 rows in set (0.01 sec)
```

治服务

## 自治服务

### 自治服务简介

自治服务是一种基于机器学习和专家经验实现数据库自感知、自修复、自优化、自运维及自安全的云服务， 帮助用户消除数据库管理的复杂性及人工操作引发的服务故障，有效保障数据库服务的稳定、安全及高效。

**功能介绍**

自治服务主要包含如下功能：

### 一键诊断

诊断实例，并提供可视化的诊断结果供您查看。

### 会话管理

查看会话、统计会话、分析SQL和优化SQL。

### 实时性能

实时查看实例的QPS、TPS、连接数、网络流量等信息。

### 空间分析

查看空间概况、变化趋势、异常列表、表空间和数据空间。

### 锁分析

查看和分析数据库最近一次发生的死锁。

### 性能趋势

查看和对比性能趋势、自定义性能趋势大盘、查看异常诊断信息和查看实例拓扑结构。

### 慢SQL

查看慢日志趋势和统计信息。

### 诊断报告

自动或手动诊断实例，查看实例的健康状况、告警、慢SQL等信息。

### 一键诊断

自治服务提供PolarDB MySQL一键诊断功能，可以诊断实例并提供可视化的诊断结果。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**自治服务** > **一键诊断**。
4. 在**一键诊断**页签下，您可以查看如下信息。
当前资源使用率情况：查看目标实例当前的CPU、内存、IOPS、空间和连接的使用率。 数据库基本信息：查看数据库类型、实例来源、实例规格等基本信息。 数据库性能的全貌：查看当前实例在指定时间段内出现的危险、警告、慢SQL和死锁的情况，帮助您快速确认是否存在异常。 治服务

**说明**

您可以单击全貌图右上角的**发起诊断**对数据库进行一键诊断，诊断结束后您可以单击**查看历史**查看诊断历史的具体情况。

### 会话管理

自治服务提供PolarDB MySQL实例会话功能，可以查看、管理目标实例的会话。

**进入会话管理页面**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**自治服务** > **一键诊断**。
4. 单击**会话管理**，在该页面您可进行如下操作：

**实例会话**

**查看异常会话**

单击**异常**按钮，在弹出窗口中查看系统识别的异常会话（例如：长时间未提交的事务、高资源消耗会话等）。 针对异常会话，可单击操作列中的**优化**或**结束**按钮，进行针对性处理。

**查看关键指标**

将鼠标悬浮于活跃会话数、最大执行时间、CPU使用率、连接使用率等指标标题上，即可在浮窗中查看详细数据及趋势。

**其他核心功能**

**10**秒**SQL****分析**：单击页面右上角**10**秒**SQL****分析**，查看最近10秒内的SQL执行统计、慢SQL列表及
SQL概览，快速捕捉瞬时性能问题。 治服务
**SQL****限流**：单击**SQL****限流**，进入**SQL****限流**页面，设置规则对高负载或异常SQL进行自动限流，防止
资源耗尽。具体操作，请参见《SQL限流》章节。
**优化**：单击**优化**，对目标实例会话进行优化。具体操作，请参见《SQL优化》章节。
**导出活跃会话**。
**结束会话**：结束会话时，为确保操作安全，系统要求输入建立该会话的数据库账号及其密码进行身份
验证。您也可以使用更高权限的数据库账号（具有结束其他账号建立的会话的权限），例如高权限账号。

**说明**

在会话列表的**用户**列，可查看建立目标会话的数据库账号。 单击**结束会话历史记录**，可查询所有已终止会话的操作记录，包括任务ID、发起时间、 结束时间等信息，便于追溯与审计。

**会话统计**

**查看会话统计信息**

查看会话概要信息（如会话总数、运行中会话总数和运行中会话最长时间），查看按用户、按访问来源和按数据库等条件统计的会话总数及活跃数情况。

**导出会话统计信息**

按概要、按用户统计、按访问来源统计和按数据库统计等条件导出会话统计信息。

### 实时性能

自治服务提供PolarDB MySQL版实时性能功能，可以查看MySQL的实时性能。

**进入实时性能页面**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**自治服务** > **一键诊断**。
4. 单击**实时性能**页签。
系统将自动加载实时数据，您可切换**实时图表**或**实时表格**视图进行查看。具体详情，请参见实时性能。

**核心指标解读**

**实例基础信息概览**

| 模块 | 指标项 | 说明与运维建议 |
|---|---|---|
| Serve r信息 | 版本/运行时间 | 显示数据库内核版本（如 8.0.36 ）及实例累计运行时间（Uptime）。用于确认环境一致性及实例稳定性。 |

治服务

| 连接信息 | 连接数上限/当前连接数/活跃连接数 | 格式示例： 1200 / - / 3 。 连接数上限：实例允许的最大连接数。 当前连接数：当前已建立的TCP连接总数。 活跃连接数：当前正在执行SQL的连接数。 说明若“当前连接数”接近上限，需警惕连接风暴；若“活跃连接数”远小于“当前连接数”，可能存在大量空闲连接占用资源。 |
|---|---|---|
| Buffer Pool | 总页数/空闲页比例/ 脏页比例 | 展示InnoDB缓冲池状态。 空闲页比例：反映内存剩余空间。 脏页比例：反映待刷盘数据量。比例过高可能影响刷盘效率，导致IO抖动。 |

**吞吐量、负载与深层引擎指标**

| 分类 | 指标名称 | 详细说明 | 运维分析与建议 |
|---|---|---|---|
| 吞吐量 | QPS \| TPS | QPS：平均每秒SQL语句执行次数。 TPS：平均每秒事务数。 | 趋势分析：突增通常对应业务高峰。 异常排查：若QPS/TPS下降但CPU升高，通常存在锁等待或慢SQL阻塞。 |
| DML分布 | DML执行次数 | select：SELECT语句每秒执行次数。 insert：INSERT语句每秒执行次数。 update：UPDATE语句每秒执行次数。 delete：DELETE语句每秒执行次数。 | 业务画像：识别业务是读多写少还是写多读少，辅助制定索引优化策略（如读写分离架构调整）。 |
| 连接会话 | 连接数 | 活跃连接数：已打开连接中处于活跃状态的数量。 总连接数：已打开连接的总数量。 | 瓶颈定位：关注活跃连接数的波峰。若活跃连接数长时间维持高位，需检查是否有长事务或未释放的应用连接。 |
| 缓存效率 | InnoDB缓存 | 缓存命中率：从内存读取数据的比例。 缓存使用率：Buffer Pool的占用比例。 | 性能关键：命中率应接近100%。低命中率意味着大量请求穿透到磁盘（物理读），导致性能急剧下降。需考虑增大Buffer Pool或优化 SQL。 |

治服务

| 数据访问 | InnoDB访问行数 | rows read：每秒读取的InnoDB _ 行数。 rows inserted：每秒插入的 _ InnoDB行数。 rows updated：每秒更新的 _ InnoDB行数。 rows deleted：每秒删除的 _ InnoDB行数。 | 索引优化：若 rows read 极高但返回结果 _ 集很小，说明存在全表扫描，急需添加合适索引。 |
|---|---|---|---|
| IO读写 | 逻辑读/物理读 | 逻辑读：每秒逻辑读次数（从 Buffer Pool读取）。 物理读：每秒物理读次数（从磁盘读取）。 | IO瓶颈：物理读激增是性能杀手，通常由冷数据访问、Buffer Pool不足或缺少索引引起。 |
| 锁竞争 | 行锁平均锁定时间 | 单位通常为毫秒（ms），反映获取锁的平均耗时。 | 并发冲突：数值越高，说明事务间争用越激烈，可能导致应用端超时报错。 |
| 锁等待 | InnoDB行锁等待 | InnoDB行锁平均等待次数：统计周期内行锁平均等待次数。 InnoDB行锁当前等待次数：当前时刻正在等待行锁的次数。 | 阻塞源头：若此曲线不为0，说明存在阻塞。需结合“会话管理”功能查找阻塞源头（Blocker） 并终止异常会话。 |
| 临时资源 | 临时表、文件 | 临时表：创建临时表的数量。 临时文件：创建临时文件的数量。 | SQL优化：频繁创建磁盘临时文件会严重拖慢 SQL速度。通常是因为 sort buffer size 不足或缺少索引导 _ _ 致无法利用索引排序。 |
| 异常监控 | 慢查询 | 慢查询：两个相邻采集点间新增的慢查询数量差值（即该时间段内的慢查询增量）。 | 根因关联：慢查询突增往往是CPU飙升、响应变慢的直接原因。需立即抓取慢日志进行分析。 |
| 网络带宽 | 网络流量 | 总流量/流入流量/流出流量。 | 带宽限制：若流出流量打满实例带宽，会导致连接超时或丢包；若流入流量异常，需排查大字段写入或潜在攻击。 |

**视图切换与高级操作**

**实时图表和实时表格对比**

**实时图表**：适合观察趋势、波峰波谷以及多个指标间的关联性（例如QPS上升时CPU是否同步上升）。
**实时表格**：适合精确查看某一具体时间点的各项指标数值，方便记录基线数据或进行细微的数据对比。
表格中每一行代表一个采样时间点，列对应上述各项指标的具体数值。
**数据下载**：在**实时表格**页签下，单击页面右上角的**下载**按钮，可将当前报表数据导出至本地。
治服务

**参数说明**

点击页面左上角的**参数说明**，可以查看每个监控项的具体定义，帮助您更准确地解读数据。

**暂停/开始**

右上角显示“剩余刷新次数”，可手动控制页面的自动刷新频率，或在排查问题时点击**暂停**以固定某一时刻的状态进行详细分析。

**使用建议**

建立基线：在业务平稳期，观察并记录正常的QPS、TPS和CPU水位，作为后续故障对比的基准。 关联分析：避免孤立查看单一指标。例如，当发现QPS下降时，应立即检查InnoDB行锁等待是否升高， 或者慢查询是否增多，同时观察物理读是否有异常波动。 关注“毛刺”：图表中突然出现的尖峰（Spikes）通常对应具体的业务事件（如定时任务启动、促销秒杀），结合时间点回溯业务日志能快速定位问题。

### 空间分析

自治服务提供PolarDB MySQL版空间分析功能，可直观查看数据库实例的空间使用概况、空间剩余可用天数，以及数据库中某个表的空间使用情况、空间碎片、空间异常诊断等，帮助您及时发现数据库中的空间异常，避免影响数据库稳定性。

**进入空间分析页面**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**自治服务** > **一键诊断**。
4. 单击**空间分析**页签，可查看如下信息：
在**空间分析** > **空间概况**页签，可查看库表空间概况、异常列表、空间变化趋势和表空间等数据。 治服务在**空间分析** > **数据空间**页签，可查看每个数据库和单个表的空间使用情况。 单击目标表名可查看该表的字段和索引信息。

### 锁分析

治服务当数据库出现死锁、事务阻塞或元数据锁（MDL）等待等问题时，可借助DAS提供的锁分析功能，对锁等待关系进行可视化诊断，快速定位阻塞源头与依赖链路，有效提升问题排查效率，保障数据库服务的稳定性与高可用性。

**功能简介**

锁分析功能支持对数据库实例进行多维度的死锁分析、事务阻塞分析、元数据锁等待分析。
**最近死锁分析**：DAS基于 `SHOW ENGINE INNODB STATUS` 返回的最近一次死锁日志进行分析。如果发生
过多次死锁，DAS只会对最近一次死锁进行分析。
**其他锁分析**：DAS根据 `information_schema` 和 `performance_schema` 相关数据，实时分析数据库实
例当前会话中的元数据锁和事务阻塞情况。 元数据锁分析：DAS根据 `information_schema.processlist` 等的数据，推导锁等待关系，并生成相应的关系图。

| information schema.processlist _ | ， | information schema.innodb trx _ _ |
|---|---|---|

和 `performance_schema.data_lock_waits` （MySQL 8.0使用该数据）分析事务阻塞关系，并生成相应的关系图。

**操作步骤**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**自治服务** > **一键诊断**，在**锁分析**页签下：

**死锁分析**

i. **发起最近死锁诊断** 在**最近死锁分析**页签下，单击**创建分析**。

**说明**

若发生过多次死锁，触发分析时只能分析最近一次死锁，然后保留本次分析得到的死锁相关数据。 ii. **查看详情** a. 诊断完成后，选择时间段，单击最近死锁分析中诊断任务列表**详情**列下的**查看详情**，查看该时间段内曾经触发过的死锁诊断任务结果。 b. 弹出的抽屉页会显示对应死锁详情，点击查看即可。

**其他锁分析**

i. **发起其他锁分析诊断** 在**最近死锁分析**区域，单击**创建分析**。 治服务 ii. **查看详情** a. 单击诊断结果前的展开元数据锁等待和事务阻塞分析相关信息。 b. 单击**查看详情**，将显示对应的事务锁详情。

### 性能趋势

自治服务提供PolarDB MySQL版性能趋势功能，可查看目标实例的性能指标（如TPS、QPS、吞吐量等）。同时支持多种方式查看性能趋势，包括性能趋势区间查看、性能趋势对比查看和自定义性能趋势查看。

**进入性能趋势页面**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**自治服务** > **性能趋势**。
4. 您可以在**性能趋势**页面查看如下信息。
在**性能趋势**页签，可查看TPS/QPS、会话连接等性能变化趋势，还可单击**更多指标**自定义性能趋势展示详情。

**说明**

在指标趋势图中单击指标后的查询指标含义。 在**性能趋势对比查看**页签，可选择任意两个时间段，对比查看这两个时间段内的性能趋势情况。 在**自定义图表**页签，可自定义多个性能监控大盘，将需要的多个性能监控指标在同一个图表中进行展示，便于排查和分析问题。 治服务

**说明**

如果首次使用**自定义图表**功能，需要先创建监控大盘。

### 慢SQL

自治服务提供PolarDB MySQL版慢SQL功能，可以查看慢日志趋势、慢日志执行情况和慢日志优化建议。

**进入慢SQL页面**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏，单击**自治服务**>慢**SQL**，进入慢日志分析详情页。可查看以下信息：
在**慢日志趋势**区域查看目标实例的慢日志变化趋势。 单击**慢日志统计**页签，查看特定时间段的慢日志详情，针对目标SQL进行优化。 部分数据库实例暂不支持SQL优化能力，具体支持情况请以控制台界面为准。 单击**慢日志明细**页签，查看慢日志执行明细。

### 诊断报告

自治服务提供PolarDB MySQL版诊断报告功能，支持创建和查看诊断报告。

**进入诊断报告页面**

1. 登录云原生数据库PolarDB控制台。
2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏，单击**自治服务** > **诊断报告**，在该页面中：

**手动发起诊断**

单击**发起诊断**，选择诊断时间区间（支持近1小时、近3小时、近6小时、近12小时、近24小时），并单击**确认**，系统将立即启动诊断任务。

**配置自动诊断报告（定时生成）**

单击**自动生成报告设置**，勾选**定时触发**，并勾选日期和具体时间，单击**确认**。 治服务

**说明**

受系统调度与资源负载影响，自动报告可能存在延迟，请以实际生成时间为准。

**查看报告详情**

诊断完成后，报告将出现在列表中。单击目标诊断报告右侧操作列下的**查看报告**，进入详情页。报告维度包括实例健康状况、活跃会话列表、TOP 10慢SQL、高危SQL、TOP5 表空间、冗余索引、锁分析、性能趋势。 您可在诊断报告页面顶部右侧，单击**扣分详情**，查看本次诊断的扣分详情。 治服务

**下载诊断报告**

单击**查看报告**在实例诊断报告详情页，单击左侧**下载**，即可下载报告到本地，便于存档或分享。 治服务志管理

## 日志管理

PolarDB实例都支持日志管理，您可以通过控制台查询实例的错误日志和慢日志明细，帮助故障定位分析。

**操作步骤**

## 1. 登录云原生数据库PolarDB控制台

2. 在**实例列表**页面，单击目标实例ID或者单击实例右侧**操作**列下的**管理**，打开**基本信息**页面。
3. 在左侧导航栏中，单击**日志管理**。
4. 在**日志管理**页面，选择查询**慢日志明细**或者**主备切换日志**，选择时间范围，单击**查询**。

| 查询项 | 内容 |
|---|---|
| 慢日志明细 | 记录1个月内数据库中执行时间超过1秒的SQL语句，并进行相似语句去重。 说明控制台每分钟更新一次，实时的慢日志明细可以查看 mysql.slow log 表。 _ |
| 主备切换日志 | 记录主备实例切换的日志。 |

5. 在**日志管理**页面，选择查询**错误日志**。单击
在**导出**对话框中选择**导出范围**选择**全部**或者**选中数据**， 在**需要导出的数据列**中选择**采集时间**或者**错误信息**。

| 查询项 | 内容 |
|---|---|
| 错误日志 | 记录1个月内数据库运行出错的日志。 |

## PolarDB AI

### PolarDB 智能助手

PolarDB 智能助手是一款基于大模型技术打造的智能运维工具。它通过自然语言对话交互，帮助用户轻松查询实例状态、诊断性能瓶颈、获取参数调优建议以及解答产品知识疑问，让数据库运维变得简单高效。

**注意事项**

**提问精准**：提问时建议@选择实例ID、地域（Region）、时间范围及问题现象描述。
**上下文对话**：智能助手支持多轮对话，可基于前一轮的诊断结果进行追问。但涉及敏感操作（例如变更建
议）时，请谨慎评估后再执行。
**诊断时效性**：性能诊断依赖监控数据，建议在问题发生后尽快发起分析，以确保相关指标数据仍在保留期
内。
**会话异常**：如遇卡顿，请退出会话重新提问。
**决策审慎**：所有优化建议仅供参考，特别是变更操作建议，请在充分测试和评估后再执行。

**核心优势**

4大核心能力：涵盖“问、诊、巡、答”全链路运维场景。 18+诊断工具：覆盖日常运维诊断的全部需求，从性能监控到安全审计。 7×24小时在线：秒级响应，即问即答，随时待命。 0学习成本：采用自然语言交互模式，无需记忆复杂命令，像聊天一样运维。

**快速访问智能助手**

1. 登录云原生数据库PolarDB控制台。
2. 单击页面最右侧边栏的
图标进入对话界面。

**智能助手能力概览**

| 功能模块 | 核心描述 | 关键能力点 |
|---|---|---|

| 实例运行状态查询 | 一键查看集群基本信息、规格配置、 节点拓扑及参数详情。 | 基本信息概览。 实例拓扑结构。 当前参数配置。 |
|---|---|---|
| 实时性能监控 | 对关键性能指标进行趋势监控，快速发现异常波动和资源瓶颈。 | 核心性能指标。 历史趋势分析。 异常情况自动发现。 |
| CPU 和内存异常诊断 | 针对 CPU 飙高、内存泄漏等常见问题进行多维度的根因分析，并提供优化建议。 | CPU 深度诊断。 内存使用分析。 根因精准定位。 |
| 慢 SQL 诊断优化 | 深入分析慢日志，解读执行计划，提供具体的索引创建和 SQL 改写建议。 | 慢 SQL 识别。 执行计划可视化。 定制化优化建议。 |
| 会话与锁冲突分析 | 识别异常会话，检测长事务，快速排查死锁和锁阻塞问题。 | 异常会话捕捉。 死锁成因分析。 锁等待链条追踪。 |
| 安全审计与合规 | 进行权限审计、账号风险扫描、安全检查及敏感操作审计，确保合规。 | 权限粒度审计。 账号风险评估。 合规性检查报告。 |
| 备份与恢复管理 | 查看备份列表、校验备份策略完整性，并提供恢复相关信息。 | 备份任务列表。 策略配置查看。 恢复可行性确认。 |
| 巡检报告生成 | 一键生成综合巡检报告，覆盖性能、 资源、配置和安全四大维度。 | 健康度巡检。 资源利用率分析。 存储空间分析。 |
| 产品知识问答 | 基于官方文档知识库，回答关于产品功能、架构原理及最佳实践的问题。 | 产品文档检索。 参数含义说明。 最佳实践指导。 |

**典型实战场景**

**场景一：快速了解集群全貌**

用户指令：“查看当前集群的基本信息和运行状态” 助手反馈： 集群：polardb-prod-01 | MySQL 8.0 | 8C32G 节点：1 主 + 2 只读存储：256GB / 500GB | CPU 45% | 内存 62%

**场景二：慢 SQL 排查与优化**

用户指令：“最近有哪些慢 SQL？给 Top 3 和优化建议” 助手反馈： Top 3 慢 SQL：
1. SELECT * FROM orders ... 3.2s → 添加复合索引
2. UPDATE inventory ... 2.8s → 拆分批量操作
3. SELECT COUNT(*) ... 1.9s → 使用近似计数

**场景三：会话与锁等待排查**

用户指令：“有没有锁等待或阻塞的事务？” 助手反馈： 发现 2 个锁等待： 会话 1523 等待元数据锁 47s → 阻塞源：会话 1498 会话 1567 行锁等待 12s → 阻塞源：会话 1501

**场景四：安全合规检查**

用户指令：“帮我做一次安全合规检查” 助手反馈： SSL 已开启 TDE 未开启审计日志已开启高风险：白名单含 0.0.0.0/0

**场景五：生成实例巡检报告**

用户指令：“帮我生成一份实例巡检报告” 助手反馈： 性能正常磁盘使用率 78%（预计 6 周后需扩容） 检测到 3 个参数非推荐值安全与备份状态正常完整报告已生成

**场景六：参数调优建议**

用户指令："innodb_buffer_pool_size 建议设多大？” 助手反馈： 建议值：可用内存的 60%~80% 当前配置：16GB → 建议调整：20~24GB 注意：修改该参数需重启实例，建议先在测试环境验证。

**常用指令速查**

您可以直接复制以下指令到输入框使用：

**性能诊断**

帮我看看这个集群有什么问题 CPU 使用率飙高了，分析下原因查看内存使用情况和趋势查看重要性能指标总结

**SQL 与会话分析**

最近有哪些慢 SQL？给我 Top 10 查看执行计划和优化建议有没有异常会话或长事务？ 最近有没有死锁或锁等待？

**实例或备份查询**

查看集群基本信息和运行状态查看实例列表和节点状态查看备份列表和备份策略查看当前集群的参数配置

**安全和知识问答**

帮我做一次安全合规检查查看白名单配置 innodb_buffer_pool_size 建议设多大？ PolarDB 和 RDS MySQL 区别？

### 智能迁移

#### 智能迁移指引

云原生数据库PolarDB智能一键迁移是基于DTS能力构建的一站式数据库迁移平台，提供从场景选择、前置检查、任务配置到地址切换的全链路可视化引导流程。通过自动化配置与无缝切换能力，实现应用无感迁移；同时集成AI迁移助手，支持智能问答、日志诊断与优化建议，显著提升迁移效率与成功率。

**功能简介**

云原生数据库PolarDB智能一键迁移是一项面向企业级用户的全流程、低门槛、智能化数据库迁移解决方案。该功能将原本分散在多个控制台的操作整合至PolarDB控制台统一界面，用户无需跳转即可完成从实例准备到业务割接的全部动作。

**核心能力**

| 能力类别 | 功能说明 |
|---|---|

| 全链路可视化 | 四步引导式流程，状态清晰可见，所有操作闭环管理。 |
|---|---|
| 自动化配置 | 根据迁移场景自动匹配DTS链路、创建迁移任务，减少人工干预。 |
| 应用无感切换 | 支持数据库连接地址一键切换，业务零中断。 |
| AI智能辅助 | 内嵌AI迁移助手，实时解答问题、分析日志、给出修复建议。 |

**支持的迁移场景**

当前支持以下迁移路径，系统会根据所选场景自动加载对应的操作方案与检查项，确保迁移方案合规高效。

| 迁移链路分类 | 支持的迁移链路 |
|---|---|
| MySQL引擎迁移 | RDS MySQL到PolarDB MySQL主备版 RDS MySQL到PolarDB MySQL集群版 PolarDB MySQL主备版5.7到PolarDB MySQL主备版8.0 PolarDB MySQL主备版到PolarDB MySQL集群版 PolarDB MySQL集群版到PolarDB MySQL集群版 |
| PostgreSQL引擎迁移 | RDS PostgreSQL到PolarDB PostgreSQL主备版 PolarDB PostgreSQL主备版到PolarDB PostgreSQL主备版 |
| PolarDB-X引擎迁移 | RDS MySQL到PolarDB-X 2.0 PolarDB-X 2.0到PolarDB-X 2.0 |

### 使用流程

智能一键迁移采用线性四步引导模式，您可在同一页面完成全部迁移操作。

**步骤一：选择迁移场景**

1. 登录云原生数据库PolarDB控制台。
2. 在左侧导航栏中，进入**AI****能力** > **智能迁移**页面，选择源数据库和目标PolarDB实例类型。

**功能优势**

系统自动识别迁移需求，预填充后续流程所需参数； 自动推荐最优DTS链路与同步策略； 配置成本大幅降低，避免手动选型错误。

**步骤二：执行前置检查**

单击**去查看**，系统将根据所选场景跳转至官方迁移指南文档获取详细操作指引，以及迁移前检查清单等，例如源库是否开启Binlog及格式是否正确、安全组与白名单是否放通通信等。

**功能优势**

检查内容与场景强绑定，避免遗漏； 快速链接官网文档，排查效率大幅提升。

**步骤三：创建DTS数据迁移任务**

确认前置检查完成后，单击**去迁移**，系统将自动为您在该页面弹出DTS迁移任务配置页面，仅需根据步骤二中的方案要求填写关键信息，即可快速构建迁移链路。

**功能优势**

无需跳转至DTS控制台，所有任务状态在本页面集中展示； 配置时间大幅减少，任务快速启动； 任务异常实时告警，便于及时干预。

**步骤四：查看迁移结果并切换数据库地址**

当增量同步延迟趋近于0且无报错时，可进行最终的应用连接切换。

**说明**

建议在业务低峰期执行地址切换，并提前验证应用程序的重连机制。
1. 在**数据库迁移结果**区域确认迁移状态正常时，单击任务操作列下的**迁移地址**。
您可在结果列表中，查看任务的创建时间、运行状态、任务开始时源端行数和任务结束时目标端行数等详情。

**说明**

任务开始后若源端数据发生变化，会导致任务结束时目标端行数与源端不一致。
2. 在弹出的页签中，确认源库和目标库信息，单击**切换地址**。

**功能优势**

实现应用无感迁移，业务无中断； 切换过程可追溯、可回滚，安全保障高。

#### AI迁移助手

AI迁移助手是一键迁移平台的智能辅助工具，基于DTS MCP（Model Context Protocol）服务提供自然语言问答、任务状态查询和故障诊断能力，帮助用户快速解决迁移过程中的链路查询、配置指导与异常处理问题。

**功能简介**

AI迁移助手集成于PolarDB控制台“智能迁移”页面，通过理解用户提问，自动调用DTS后端数据与日志，提供准确的迁移支持建议。无需跳转，即可获得实时、可操作的解决方案。其中主要能力包括： 意图识别：支持中文自然语言输入，精准解析问题意图。 链路查询：查询当前Region支持的DTS迁移组合及连接方式（如云实例、公网IP）等。 配置指导：返回指定链路支持的迁移对象类型（表、索引等）和DDL操作范围等。 状态监控：实时获取任务运行状态、延迟、流量、同步进度等。 故障诊断：分析任务日志，定位异常原因并给出修复建议。

**使用入口**

**示例场景**

**场景1：查询迁移链路支持情况**

用户问题：当前环境是否支持RDS PostgreSQL到PolarDB PostgreSQL的迁移？支持的数据源连接方式有哪些（如云实例、公网IP等）？ AI智能响应：DTS MCP自动识别当前Region、产品版本及网络环境，实时返回该区域下所有可用的DTS链路组合，明确标注源和目标数据库类型、支持的连接模式（VPC内网/云实例/公网IP）及限制项。提升信息获取效率，减少因链路不明确导致的工单咨询量约20%。

**场景2：查询迁移任务如何配置**

用户问题：从RDS PostgreSQL云实例到PolarDB PostgreSQL的迁移链路中，支持哪些迁移对象类型和同步操作？ AI智能响应：DTS MCP根据用户输入的源端与目标端信息，自动检索并返回该链路支持的迁移对象（如表、视图、函数、存储过程等），以及支持的DDL/DML同步范围和操作限制，提供结构初始化、全量迁移、增量同步等阶段的配置指引，显著降低任务配置复杂度达20%。

**场景3：排查任务异常**

用户问题：DTS迁移任务l65e721当前运行是否正常？存在的异常如何应对？ AI智能响应：DTS MCP自动拉取任务实时状态、延迟趋势、同步进度、吞吐流量及错误日志，精准判断任务健康度；若检测到异常或潜在风险，AI助手将生成诊断报告并推荐修复方案，有效降低故障响应时间与人工介入需求，助力工单及预警量下降30%。

#### RDS MySQL到PolarDB MySQL版白屏化迁

**移方案**

本文为您介绍RDS MySQL到PolarDB MySQL版白屏化迁移方案，帮助您快速完成迁移操作。

**说明**

一键迁移功能依赖RDS、PolarDB、DTS和oneconsole，需要同时将上述组件版本升级至目标版本及以上。

**一.概述**

支持将RDS MySQL版实例迁移到PolarDB MySQL版实例，支持的MySQL版本如下：

| 源端 | 目标端 |
|---|---|
| RDS MySQL 5.6 | PolarDB 5.7、8.0 |
| RDS MySQL 5.7 | PolarDB 5.7、8.0 |
| RDS MySQL 8.0 | PolarDB 8.0（不支持降级大版本迁移） |

**用户告知**

需得到客户许可时操作。 迁移过程涉及实例连接地址的切换，建议在业务低峰期执行。

**优势说明**

支持连接地址迁移：可保留数据库原连接地址，应用端无需修改连接地址。 支持迁移回切：迁移切换后，若发现兼容性等问题，支持切回原来的实例。 迁移进度随时查看：支持查看当前的迁移进度，方便制定切换计划。 支持增量迁移，停机时间小于10分钟：通过DTS实现数据在线热迁移，数据迁移过程中无需停机。仅实例切换过程涉及一次闪断（即当业务从RDS MySQL切换至PolarDB时），需要申请约10分钟的停机窗口。

**限制说明**

不支持跨地域迁移：仅支持同一个Region中的实例进行迁移，不支持跨Region迁移。 如果涉及跨MySQL大版本迁移（如RDS MySQL5.7到PolarDB 8.0等），语法差异需要用户自行评估： 由于MySQL大版本之间并非完全兼容，当用户涉及跨大版本迁移时，应用对语法的兼容性需要自行评估。 连接地址切换的限制：切换地址仅进行DNS的切换，实际使用中有如下限制： 带地址切换只会互换RDS和PolarDB的域名；VSwitch、VIP等配置不会切换。端口也不会发生切换。 DNS缓存问题：切换域名后，可能会存在DNS解析缓存问题，在缓存过期时间内可能会出现连接不上数据库或数据库只支持读操作，无法执行写入操作等情况，可以通过手工刷新服务器的DNS缓存加速缓存更新。 其他限制及注意事项：请参见《数据传输服务DTS用户指南》中数据迁移配置案例下《从RDS MySQL迁移至PolarDB MySQL版》中源库和目标库的注意事项及限制。

**二.创建PolarDB实例**

使用前需要先手工创建PolarDB MySQL实例。建议您在正式迁移前，先进行测试数据的迁移和演练，充分评估好SQL语法兼容性，避免语法错误或数据混乱。

**创建PolarDB实例注意事项**

实例规格：推荐创建的实例规格与待迁移的RDS MySQL实例规格一致。 VPC网络：建议选择与现有环境一致的VPC网络。如果选择了不同的VPC，请迁移前确认VPC网络可以被应用端访问。 网络白名单：实例创建成功后，需要配置与RDS MySQL一致的IP白名单，避免实例切换后，应用无法访问PolarDB实例。 迁移前后实例ID发生了变化，如果涉及到如下场景，需要提前与相关应用系统沟通，确保迁移后相关系统也及时做好切换，否则，可能会导致应用系统使用异常。 带地址切换不涉及数据库连接地址和端口修改，对于已有的连接地址不受影响，但是当进行变更配置的时候，需要在如下的系统中重新配置： 数据库产品：DTS，DMS 通过云实例方式访问大数据产品：DataWorks，DataHub通过云实例方式访问云监控系统：切换到监控新的实例

**说明**

使用时需注意弹性伸缩产品ESS目前不支持PolarDB MySQL。

**三.迁移前置检查**

**仔细阅读DTS迁移限制说明，评估约束限制**

数据迁移是基于DTS实现的，在迁移前，请仔细阅读《数据传输服务DTS用户指南》中数据迁移配置案例下 《从RDS MySQL迁移至PolarDB MySQL版》中源库和目标库的注意事项及限制，明确注意事项和约束限制，并按要求完成迁移前的准备。

**语法兼容性检查**

如果涉及跨MySQL大版本迁移，请在迁移前做好应用的SQL语法兼容性验证和开发。确保迁移前后，应用都能正常使用。MySQL各版本间差异，请参见升级数据库版本和MySQL release notes。

**四.DTS数据迁移**

**操作步骤**

1. 登录云原生数据库PolarDB控制台，在左侧导航栏选择**AI****能力** > **智能迁移**。
2. 在智能迁移页面，单击**RDS MySQL**到**PolarDB-M** **主备版**。
3. 单击**去迁移**配置迁移任务。
4. 配置源库和目标库信息。

| 类别 | 配置 | 说明 |
|---|---|---|
| 无 | 任务名称 | DTS会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 实例地区 | 创建数据迁移实例时已指定，不可变更。 |
|  | 是否跨阿里云账号 | 选择不跨账号。 |
|  | RDS实例ID | 选择源RDS实例ID。 |
|  | 数据库账号 | 填入源RDS的数据库账号，需具备REPLICATION CLIENT、 REPLICATION SLAVE、SHOW VIEW和所有迁移对象的SELECT权限。 说明当源RDS实例的数据库类型为MySQL 5.5或MySQL 5.6时，无需配置数据库账号和数据库密码。 |
|  | 数据库密码 | 填入该数据库账号的密码。 |
|  | 连接方式 | 根据需求选择连接方式。如果设置为SSL安全连接，您需要提前开启RDS 实例的SSL加密功能。 |
| 目标库信息 | 实例地区 | 创建数据迁移实例时已指定，不可变更。 |
|  | 是否跨阿里云账号 | 选择不跨账号。 |
|  | PolarDB实例 ID | 选择目标PolarDB实例ID。 |
|  | 数据库账号 | 填入目标PolarDB MySQL版实例的数据库账号，需具备目标数据库的读写权限。 |
|  | 数据库密码 | 填入该数据库账号的密码。 |
|  | 连接方式 | 根据需求选择连接方式。 |

5. 配置完成后，单击页面下方的**测试连接以进行下一步**。
6. 如果您的PolarDB MySQL实例具备白名单设置，请将弹跳框中提示的DTS服务器的IP地址，加
入PolarDB MySQL版实例的白名单设置中。白名单设置完成后，单击**测试连接以进行下一步**。

**说明**

如果您的PolarDB MySQL实例无需进行白名单设置，请直接单击**测试连接以进行下一步**。
7. 选择迁移对象及迁移类型。

| 配置 | 说明 |
|---|---|
| 任务步骤 | 如果只需要进行全量数据迁移，同时选中库表结构迁移和全量迁移。 如果需要进行不停机迁移，同时选中库表结构迁移、全量迁移和增量迁移。 说明如果未选中增量迁移，为保障数据一致性，全量数据迁移期间请勿在源数据库中写入新的数据。 |
| 目标已存在表的处理模式 | 预检查并报错拦截：检查目标数据库中是否有同名的表。如果目标数据库中没有同名的表，则通过该检查项目；如果目标数据库中有同名的表，则在预检查阶段提示错误，数据迁移任务不会被启动。 忽略报错并继续执行：跳过目标数据库中是否有同名表的检查项。 警告选择为忽略报错并继续执行，可能导致数据不一致，给业务带来风险，例如： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录，则会保留目标库中的该条记录，即源库中的该条记录不会迁移至目标库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败。 |
| 目标库对象名称大小写策略 | 您可以配置目标实例中迁移对象的库名、表名和列名的英文大小写策略。默认情况下选择DTS默认策略，您也可以选择与源库、目标库默认策略保持一致。 |
| 源库对象 | 在源库对象框中单击待迁移的对象，然后单击图标将其移动至已选择对象框。 说明您可以根据实际情况，展开导航树进行正则搜索。 迁移对象选择的粒度为库、表。 |
| 已选择对象 | 默认情况下，迁移对象在目标库中的名称与源库保持一致。 说明如需按库或表级别选择迁移的SQL操作，请在已选择对象中右击待迁移对象，并在弹出的对话框中选择所需迁移的SQL操作。 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 |

8. 单击**下一步高级配置**，进行高级配置。

| 配置项目 | 配置说明 |
|---|---|
| 选择目标库的引擎类型 | 请根据实际情况，选择目标库的引擎类型为InnoDB或X-Engine。 |
| 源库、目标库无法连接后的重试时间 | 在迁移任务启动后，若源库或目标库连接失败则DTS会报错。对于可预期的报错，DTS会立即进行持续的重试连接，默认重试720分钟，您也可以在取值范围 （10~1440分钟）内自定义重试时间，建议设置30分钟以上。如果DTS在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明针对同源或者同目标的多个DTS实例，如DTS实例A和DTS实例B，设置网络重试时间时A设置30分钟，B设置60分钟，则重试时间以低的30分钟为准。 |

9. 上述配置完成后，单击页面下方的**下一步预检查并启动**。

**重要**

在数据迁移任务正式启动之前，会先进行预检查。只有预检查通过后，才能成功启动数据迁移任务。 如果预检查失败，请单击**查看详情**并请根据提示修复问题，然后重新进行预检查。
0. **预检查通过率**显示为100%时，单击**返回列表**。
如果未选择增量数据迁移，您只需等待迁移任务完成即可，迁移任务会自动结束；如果

**说明**

选择了增量数据迁移，迁移任务不会自动结束，您需要等待迁移任务处于**运行中**且无延迟时，手动结束迁移任务。

**五.切换数据库地址连接**

在迁移中单击切换即可。DNS切换后，客户端有缓存，可能还是会继续连接源数据库，需要断开源数据库的

**六.迁移回滚（可选）**

再次执行步骤五切换数据库地址链接即可将地址进行回迁。

#### PolarDB MySQL 5.7到PolarDB MySQL

### 白屏化迁移方案

本文为您介绍PolarDB MySQL 5.7到PolarDB MySQL 8.0白屏化迁移方案，帮助您快速完成迁移操作。

**说明**

一键迁移功能依赖RDS、PolarDB、DTS和oneconsole，需要同时将上述组件版本升级至目标版本及以上。

**一.概述**

支持将PolarDB MySQL 5.7 版实例迁移到PolarDB MySQL 8.0 版实例，常用于PolarDB MySQL大版本升级。 整体方案如下：新建PolarDB MySQL 8.0实例后，通过DTS进行数据在线迁移，迁移后切换地址即可。

**用户告知**

需得到客户许可时操作。 迁移过程涉及实例连接地址的切换，建议在业务低峰期执行。

**优势说明**

支持连接地址迁移：可保留数据库原连接地址，应用端无需修改连接地址。 支持迁移回切：迁移切换后，若发现兼容性等问题，支持切回原来的实例。 迁移进度随时查看：支持查看当前的迁移进度，方便制定切换计划。 支持增量迁移，停机时间小于10分钟：通过DTS实现数据在线热迁移，数据迁移过程中无需停机。仅实例切换过程涉及一次闪断（即当业务从PolarDB 5.7切换至PolarDB 8.0时），需要申请约10分钟的停机窗口。

**限制说明**

不支持跨地域迁移：仅支持同一个Region中的实例进行迁移，不支持跨Region迁移。 MySQL大版本之间并非完全兼容，当涉及跨大版本迁移时，应用对语法的兼容性需要自行评估。 连接地址切换的限制：切换地址仅进行DNS的切换，实际使用中有如下限制： 带地址切换只会互换RDS和PolarDB的域名；Vswitch、Vip等配置不会切换。端口也不会发生切换。 DNS缓存问题：切换域名后，可能会存在DNS解析缓存问题，在缓存过期时间内可能会出现连接不上数据库或数据库只支持读操作，无法执行写入操作等情况，可以通过手工刷新服务器的DNS缓存加速缓存更新。 其他限制及注意事项：请参见《数据传输服务DTS用户指南》中数据迁移配置案例下对应源库和目标库的注意事项及限制。

**二.创建PolarDB MySQL实例**

执行迁移操作前需创建PolarDB MySQL实例。建议在迁移正式版本前，先进行测试数据的迁移和演练，避免误操作导致的数据错误或混乱。

**注意事项**

实例规格：推荐创建的实例规格与待迁移的PolarDB 5.7实例规格一致。 VPC网络：建议选择与现有环境一致的VPC网络。如果选择了不同的VPC，请迁移前确认VPC网络可以被应用端访问。 网络白名单：实例创建成功后，需要配置与原PolarDB 5.7一致的IP白名单，避免实例切换后，应用无法访问PolarDB 8.0实例。 迁移前后的实例ID发生了变化，如果涉及到如下场景，建议提前与相关系统沟通，确保迁移后相关系统的切换。带地址切换不涉及数据库连接地址和端口修改，对于已有的连接地址不受影响，但是当进行变更配置的时候，需要您在如下的系统中重新配置： 数据库产品：DTS、DMS 通过云实例方式访问。 大数据产品： DataWorks、DataHub通过云实例方式访问。 云监控系统：切换到监控新的实例。

**三.迁移前置检查**

**仔细阅读DTS迁移限制说明，评估约束限制**

数据迁移是基于DTS实现的，在迁移前，请仔细阅读《数据传输服务DTS用户指南》中数据迁移配置案例下对应源库和目标库的注意事项及限制，明确注意事项和约束限制，并按要求完成迁移前的准备。

**语法兼容性检查**

请在迁移前做好应用的SQL语法兼容性验证和开发。确保迁移前后，应用都能正常使用。MySQL各版本间差异，请参见升级数据库版本和MySQL release notes。

**四.DTS数据迁移**

**操作步骤**

1. 登录云原生数据库PolarDB控制台，在左侧导航栏选择**AI****能力** > **智能迁移**。
2. 在智能迁移页面，单击**PolarDB-M****主备版** **5.7**到**PolarDB-M****主备版** **8.0**。
3. 单击**去迁移**配置迁移任务。
4. 配置源库和目标库信息。

| 类别 | 配置 | 说明 |
|---|---|---|
| 无 | 任务名称 | DTS会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
|  | 实例地区 | 创建数据迁移实例时已指定，不可变更。 |
|  | 是否跨阿里云账号 | 选择不跨账号。 |
|  | 架构类型 | 选择主备版。 |
|  | PolarDB实例 ID | 选择源PolarDB MySQL实例ID。 |

|  | 数据库账号 | 填入源PolarDB MySQL的数据库账号，需具备REPLICATION CLIENT、 REPLICATION SLAVE、SHOW VIEW和所有迁移对象的SELECT权限。 |
|---|---|---|
|  | 数据库密码 | 填入该数据库账号的密码。 |
|  | 连接方式 | 根据需求选择连接方式。如果设置为SSL安全连接，您需要提前开启 PolarDB MySQL实例的SSL加密功能。 |
|  | 实例地区 | 创建数据迁移实例时已指定，不可变更。 |
|  | 是否跨阿里云账号 | 选择不跨账号。 |
|  | 架构类型 | 选择主备版。 |
|  | PolarDB实例 ID | 选择目标PolarDB MySQL实例ID。 |
|  | 数据库账号 | 填入目标PolarDB MySQL版实例的数据库账号，需具备目标数据库的读写权限。 |
|  | 数据库密码 | 填入该数据库账号的密码。 |
|  | 连接方式 | 根据需求选择连接方式。如果设置为SSL安全连接，您需要提前开启 PolarDB MySQL实例的SSL加密功能。 |

5. 配置完成后，单击页面下方的**测试连接以进行下一步**。
6. 选择迁移对象及迁移类型。

| 配置 | 说明 |
|---|---|
| 任务步骤 | 如果只需要进行全量数据迁移，同时选中库表结构迁移和全量迁移。 如果需要进行不停机迁移，同时选中库表结构迁移、全量迁移和增量迁移。 说明如果未选中增量迁移，为保障数据一致性，全量数据迁移期间请勿在源数据库中写入新的数据。 |

| 目标已存在表的处理模式 | 预检查并报错拦截：检查目标数据库中是否有同名的表。如果目标数据库中没有同名的表，则通过该检查项目；如果目标数据库中有同名的表，则在预检查阶段提示错误，数据迁移任务不会被启动。 忽略报错并继续执行：跳过目标数据库中是否有同名表的检查项。 警告选择为忽略报错并继续执行，可能导致数据不一致，给业务带来风险，例如： 表结构一致的情况下，在目标库遇到与源库主键的值相同的记录，则会保留目标库中的该条记录，即源库中的该条记录不会迁移至目标库中。 表结构不一致的情况下，可能导致只能迁移部分列的数据或迁移失败。 |
|---|---|
| 目标库对象名称大小写策略 | 您可以配置目标实例中迁移对象的库名、表名和列名的英文大小写策略。默认情况下选择DTS默认策略，您也可以选择与源库、目标库默认策略保持一致。 |
| 源库对象 | 在源库对象框中单击待迁移的对象，然后单击图标将其移动至已选择对象框。 说明您可以根据实际情况，展开导航树进行正则搜索。 迁移对象选择的粒度为库、表。 |
| 已选择对象 | 默认情况下，迁移对象在目标库中的名称与源库保持一致。 说明如需按库或表级别选择迁移的SQL操作，请在已选择对象中右击待迁移对象，并在弹出的对话框中选择所需迁移的SQL操作。 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 |

7. 单击**下一步高级配置**，进行高级配置。

| 配置项目 | 配置说明 |
|---|---|
| 选择目标库的引擎类型 | 请根据实际情况，选择目标库的引擎类型为InnoDB或X-Engine。 |
| 源库、目标库无法连接后的重试时间 | 在迁移任务启动后，若源库或目标库连接失败则DTS会报错。对于可预期的报错，DTS会立即进行持续的重试连接，默认重试720分钟，您也可以在取值范围 （10~1440分钟）内自定义重试时间，建议设置30分钟以上。如果DTS在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明针对同源或者同目标的多个DTS实例，如DTS实例A和DTS实例B，设置网络重试时间时A设置30分钟，B设置60分钟，则重试时间以低的30分钟为准。 |

8. 上述配置完成后，单击页面下方的**下一步预检查并启动**。

**重要**

在数据迁移任务正式启动之前，会先进行预检查。只有预检查通过后，才能成功启动数据迁移任务。 如果预检查失败，请单击**查看详情**并请根据提示修复问题，然后重新进行预检查。
9. **预检查通过率**显示为100%时，单击**返回列表**。
如果未选择增量数据迁移，您只需等待迁移任务完成即可，迁移任务会自动结束；如果

**说明**

选择了增量数据迁移，迁移任务不会自动结束，您需要等待迁移任务处于**运行中**且无延迟时，手动结束迁移任务。

**五.切换数据库地址连接**

在迁移中单击切换即可。DNS切换后，客户端有缓存，可能还是会继续连接源数据库，需要断开源数据库的

**六.迁移回滚（可选）**

再次执行步骤五切换数据库地址链接即可将地址进行回迁。

### PolarDB MySQL通过MCP接入

**Dify的最佳实践**

本文介绍如何将PolarDB MySQL版实例接入API网关提供的MCP（Managed Capability Provider）服务，并在AI Studio的Dify平台中调用该数据库能力。MCP服务可将数据库操作封装为AI可调用的接口，适用于**智能问答、数据查询**场景（暂不支持数据变更和删除）。所有组件必须部署在**同一****VPC****网络下**以确保网络连通性。

**准备工作**

在开始操作前，请确认已完成以下准备工作：

**获取必要权限**

您的阿里云账号需具备以下产品的管理权限。 云数据库PolarDB API网关（Higress引擎） 容器服务Kubernetes版（ACK） 云解析DNS（PrivateZone） AI Studio（Dify）

**确认网络规划**

确保使用同一个VPC网络，用于统一部署以下资源。 PolarDB MySQL实例 API网关（Higress）所依赖的Kubernetes集群 Dify所在的AI资源池

**说明**

需提前在容器服务ACK控制台确认目标Kubernetes集群的VPC ID。

**前提条件**

| 组件 | 要求 |
|---|---|
| PolarDB MySQL实例 | 网络类型为专有网络（VPC） 与API网关所用Kubernetes集群位于同一VPC |
| API网关实例 | 引擎类型必须为Higress 成功导入目标Kubernetes集群与PolarDB实例同VPC |
| Dify实例 | 部署在与上述VPC相同的网络环境中必须安装MCP SSE插件 |
| 网络连通性 | PolarDB实例白名单需放通API网关的VPC外部IP Dify能通过私有DNS解析MCP域名 |

**说明**

若各组件不在同一VPC，需通过云企业网（CEN）、高速通道或VPC对等连接打通网络，本文暂不覆盖跨VPC场景。

**注意事项**

**权限安全**：为MCP服务创建的数据库账号为普通账号，仅授予必要只读权限即可。
**DNS****配置**：私有域名必须以英文句点 . 结尾（如 `mcp-mysql.example.com.` ），否则解析可能失
败。
**端口协议**：PolarDB MySQL默认端口为3306，MCP后端服务协议请选择HTTP（API网关内部会处理协
议转换）。
**重启影响**：修改数据库白名单或DNS配置后，可能需要等待数秒至数分钟生效。

**步骤1：创建AI网关实例**

1. 将**K8s****集群导入****API****网关控制台**
访问**API** **网关控制台**，在**集群管理**页面，单击**导入****K8s****集群**进行导入。

**重要**

API网关实例依赖的K8s集群和后续创建的PolarDB MySQL实例必须**位于同一****VPC****网络**。
**查找****K8s****集群****VPC****网络的方法**：访问**容器服务** **Kubernetes****版控制台**，在**集群**页面单击目
标集群名称，进入集群详情页后，在**集群信息**页面的**集群资源**页签下，即可查看到虚拟专有网络VPC的详情。
2. **创建网关实例**
在**AI****网关**页面，单击**创建实例**，重点关注如下参数的配置： 网关类型：选择**AI****网关**。 部署架构：选择**K8s**。 K8s集群：选择步骤1已导入的K8s集群。

**说明**

更多参数项的配置方法，请参见API网关官网教程中的“AI网关用户指南”手册中的“创建网关实例”教程。
3. **记录该网关实例的****VPC****外部****IP**
网关实例创建完成后，可在**API** **网关控制台概览**页面的**接入点**页签下获取该网关实例的VPC外部IP，并记录，用于后续数据库白名单配置。

**步骤2：创建并配置PolarDB MySQL实例**

1. **创建****PolarDB MySQL****实例**
创建时网络类型需选择**专有网络**，同时并确保所选VPC与API网关实例所依赖的K8s集群**位于同一****VPC**网络中。

### 2. 创建数据库

实例创建完成后，进入实例详情页的**数据库管理**页面，创建数据库 `mcp_db_server` ，并在数据库中插入测试数据，可通过DMS连接到PolarDB数据库并插入测试数据。

### 3. 创建账号

进入实例详情页的**账号管理**页面，创建普通账号并为其授权（只读权限）上一步已创建的数据库。

**说明**

目前MCP服务调用仅支持数据查询类，**暂不支持数据变更和删除**，因此仅授予只读权限即可。
4. **配置数据库白名单**
进入实例详情页的**数据安全性**页面，将1.3中已获取的API网关实例的VPC外部IP，添加至数据库实例的白名单分组中。
5. **记录数据库实例的内网连接地址和端口号**
用于后续在API网关中创建MCP服务配置。查看方法，请参见查看连接地址和端口。

**步骤3：在API网关中创建MCP服务**

**3.1 创建服务**

访问步骤1中已创建的网关实例，在实例详情页的**服务管理**页面中，创建服务。重点关注如下参数的配置： 来源类型：选择**DNS****域名**。 节点：选择步骤2.5已获取到的数据库实例的连接地址和端口。 协议类型：选择**HTTP**。

**说明**

更多参数项的配置方法，请参见API网关官网教程中的“AI网关用户指南”手册中的“创建服务”教程。

**3.2 创建域名**

访问步骤1中已创建的网关实例，在实例详情页的**域名管理**页面中，单击**关联域名**，协议选择**HTTP**。

**3.3 创建MCP服务**

访问步骤1中已创建的网关实例，在实例详情页的**MCP****管理**页面中，单击**创建****MCP****服务**。重点关注如下参数的配置： MCP接入点：选择3.2中创建的域名。 服务类型：选择**DB**。 后端服务：选择3.1中创建的服务。 数据库配置：数据库类型、用户名、密码和数据库名按照步骤2中的信息正确填写即可。

**说明**

更多参数项的配置方法，请参见API网关官网教程中的“AI网关用户指南”手册中的“MCP服务管理”教程。

**步骤4：配置私有DNS（使Dify可解析MCP域名）**

1. **添加域名**
访问**云解析** **DNS****控制台**，在**私网域名服务** **> VPC****私有域名**页面的**租户内网域名**页签下，单击**添加域** 名。重点关注**租户内网域名**参数的配置，填写3.2中的域名，**注意必须在域名末尾加**英文句号（.）。
2. **添加解析记录**
单击4.1已创建域名的**操作**列下的**解析配置**，在跳转的页面中单击**添加解析记录**。重点关注**添加条目**参数的配置，填入1.3中获取的IP，注意记录名称留空不填。
3. **关联****VPC**
单击4.1已创建域名的**操作**列下的**关联****VPC**，在弹出的对话框中配置**关联****VPC**，**所选****VPC****必须和****API****网关**
**实例对应的****VPC****网络一致**。

**步骤5：在Dify中调用MCP服务**

**说明**

使用Dify前，需提前完成如下准备工作，并知晓如下注意事项： 已存在资源池和资源配额。 在ACK控制台扩容新的ECS节点，并加入资源配额，推荐2台16核32G，200G硬盘的ECS的节点。 为防止出现不可预测的bug，或者创建Dify中由于资源抢占/节点污点不能容忍造成的Dify创建不顺利，建议创建Dify前，创建Dify专用资源配额，在其中添加ECS机器，后续在该资源配额上创建Dify。 默认配置下，一个Dify实例需要4核8GB的CPU。
1. **创建****Dify****实例**

**说明**

具体教程，请参见AI Studio官网教程中的“用户指南（AI Studio）”手册中的相关教程。 i. 进入**AI Studio****控制台**，访问**开源****Agent****开发平台** **> Dify****开源版**页面，单击**创建****Dify**按钮，打开新建Dify的页面。 ii. 基础配置：输入应用的名称、描述、选择已创建的资源配额、输入管理员密码，单击下一步。 iii. 参数等配置：建议Dify版本选择1.7.1，另外需要提前在OSS控制台创建一个Bucket，将其填写到参数配置项中（authVersion值保持不变请保持不变）。 iv. 选择安装插件：**MCP SSE****插件必须安装**，其他插件按需选择即可。 等待应用状态变为运行中即可，请耐心等待，一般在5分钟左右。
2. **添加****Dify****用户**

**说明**

创建前需确保已成功完成5.1操作创建了一个Dify实例，且其状态为运行中。 i. 进入**AI Studio****控制台**，访问**开源****Agent****开发平台** **> Dify****开源版**页面，单击目标Dify实例的**用户管** 理按钮，进入用户管理。 ii. 单击**添加用户**按钮添加一个用户。 iii. 在关联用户中选择一个未添加过的用户，输入8位密码，设置为**管理员**。
3. **添加****Dify****模型**
i. 单击Dify实例下的**模型服务管理**。 ii. 单击**添加模型**。 iii. 配置如下模型信息。

**说明**

选择完成后，会自动填入模型名称、模型地址和API Key，需注意，如果此处API Key一栏没有值，则表示您不是模型服务的创建人，请联系在线服务创建人获取API Key并手工填入。
4. **登录****Dify****实例**
i. 单击Dify实例下的 。 ii. 在弹出的对话框中，输入**邮箱地址**和**密码**，单击**登录**。
5. **配置****MCP****服务**
进入Dify实例后，依次单击**工具** > **发现和调用** **MCP** **工具** > **授权**，打开MCP插件的配置标签并进入配置。 编辑JSON配置： `sever_name` 按需配置即可， `url` 字段为3.3中创建的MCP服务详情页面的MCP管理页面中可获取， 复制SSE接入点即可。

```json
{
    "server_name": {
        "url": "xxxxxxxxxx",
        "headers": {},
        "timeout": 50,
        "sse_read_timeout": 50
    }
}
```

6. **进入应用调用大模型进行查询对话**
i. 保存MCP配置后，单击**工作室** > **某个具体应用。** ii. 进入应用后，添加MCP相关工具后，即可在右侧对话框中与大模型进行对话。 录

## 附录

### 租户组织对SLB服务授权操作

本文为您介绍如何完成SLB服务授权操作，帮助您快速解决问题。

**重要**

若您的业务场景需要申请创建并使用IPv6实例，必须确保当前租户组织已显式授予数据库产品访问SLB 服务的权限。若未完成此授权操作，则无法成功创建IPv6实例。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在页面顶部的菜单栏中，单击**配置**。
3. 在左侧导航栏，单击**RAM****服务角色**。
4. 在RAM服务角色页面，单击左上角**创建****RAM****服务角色**。
**服务名称**选择**负载均衡****SLB**，**授权组织名称**选择需要授权的组织即可。
5. 单击**确定**，完成授权。

### 配置模板

配置模板是一种用于快速创建实例的工具，它用于存储创建实例的自定义配置信息（不包含实例名称和密码），包括实例规格、存储空间和网络信息等。您可以使用指定的模板快速创建实例，省去逐一配置参数的复杂流程。

**特性与优势**

配置模板（以下简称模板）的所有配置都是可选的，提高了实例的弹性和可伸缩性，能够满足不同场景的个性化需求。
**预配置参数**：可预设创建实例的配置参数，如实例规格、存储空间和网络信息等。
**标准化与一致性**：通过模板确保所有实例遵循相同的配置标准，提高环境一致性，降低人为配置出错的风
险，便于管理和维护。
**快速部署**：通过选择模板快速创建实例，无需手动配置每一项设置，减少配置时间。

### 使用限制

**配额**：每个账号在每个地域下，单个资源集内最多可创建50个实例配置模板。
**参数可选**：创建配置模板时，所有参数都是可选的。但是，如果配置模板中未包含必要参数（例如实例规
格、镜像等），则在使用该模板创建实例时还需要补充这些必要参数。 录
**不可变**：配置模板一旦创建不可变。

**创建配置模板**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击**创建实例**或**创建集群**，然后配置所需的参数。
4. 配置完成后，单击右侧**配置概览**面板的**保存为配置模板**。
5. 在弹出的**保存为配置模板**对话框，设置**模板名称**、**共享范围**和**模板版本描述**，然后单击**确定**。

**使用配置模板创建实例**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击**创建实例**或**创建集群**，然后单击**模板创建**页签。
4. 在**选择模板**区域，选择需要使用的配置模板，待配置信息加载完成，检查所有配置信息。
您可以根据业务需要，修改创建实例所需参数。
5. 单击**提交**。

**管理配置模板**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**产品** > **数据库**，选择目标数据库产品。
3. 在目标列表页面，单击**创建实例**或**创建集群**，然后单击**模板创建**页签。
4. 在**选择模板**区域，单击**管理模板**。
5. 在模板列表页，可以对模板做以下操作。

| 操作 | 操作步骤 |
|---|---|
| 编辑模板 | i. 单击操作列的编辑。 ii. 修改模板的名称、描述和共享范围。 iii. 单击保存。 |

录

| 使用模板 | i. 单击操作列的使用模板。 ii. 待配置信息加载完成，检查所有配置信息。 您可以根据业务需要，修改创建实例所需参数。 iii. 根据页面提示，完成创建实例操作。 |
|---|---|
| 删除模板 | i. 单击操作列的删除。 ii. 在弹出的对话框，单击确定。 |
