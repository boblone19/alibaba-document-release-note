---
title: "专有云部署服务 JOK部署指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 12
source_pdf: "03_JOK部署指南_jok-deployment-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asdelivery/zh/jok-deployment-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 专有云部署服务 JOK部署指南

流程

## JOK功能测试完整操作流程

**重要**

工具包含功能测试和转维检查，功能测试当前工具只支持**新建项目**场景（包括新建国产化项目）功能测试，暂不支持**扩容**、**升级**场景。 进行功能测试之前，请确保已升级相应版本的Hotfix，至少ascm、oneconsole、aso、bcc等产品的Hotfix确保升级，否则可能因为页面不同导致测试产生问题。 工具使用完成后，需要将pocDocker停掉。

**现场测试前准备**

主要介绍JOK工具包的获取、下载，和账号准备。

**前提条件**

已注册阿里云官网账号，并已有阿里云CSM完成账号专有云官网权限授权。

**下载步骤**

1. 打开浏览器（推荐Chrome）。
2. 在地址栏中输入飞天企业版在线管理平台地址（飞天企业版在线管理平台），然后按下**回车**键，进入飞天
企业版在线管理平台页面。

**说明**

在您首次登录飞天企业版在线管理平台后，若出现无权限访问，请联系阿里云CSM进行权限申请。
3. 单击左侧导航栏的**软件中心**>**下载申请**，单击“专有云交付验收工具(JOK)”，进入下载页面。
流程
4. 在对话框中，输入选择**JOK****版本号**、**CPU****类型**及**目标云实例**等相关信息。
5. 阅读并勾选《使用条款》和《相关风险》。
6. 单击**开始下载**，即可下载目标JOK安装包。

**环境准备**

1. **功能测试前准备。**
i. **创建****admin****账户。** ASCM部署完成之后就有一个admin用户(**运营管理员**)，其默认的密码是：Admin123@ascm，所以无需再创建运营管理用户。 流程 ii. **创建资源集。** 使用运营管理员登录ascm，创建如下的组织和资源集结构，在ASCM中，创建了组织之后会默认创建出一个资源集。组织结构、组织名称、资源集名称务必和下图保持一致。 root -- 根组织 atjok -- 一级组织默认资源集: ResourceSet(atjok) 新增资源集: ResourceSet(atjoknew) atjok1 -- 二级组织默认资源集: ResourceSet(atjok1) atjok11 -- 三级组织默认资源集: ResourceSet(atjok11) atjok12 -- 三级组织默认资源集: ResourceSet(atjok12) atjok2 -- 二级组织默认资源集: ResourceSet(atjok2) atjok21 -- 三级组织默认资源集: ResourceSet(atjok21) atjok22 -- 三级组织默认资源集: ResourceSet(atjok22) atjoktest -- 一级组织默认资源集: ResourceSet(atjoktest) 流程 iii. **创建****atjok****账户。** 在企业-用户管理页面中，添加用户：**atjok**，组织：**atjok**，角色：**组织管理员，**修改其密码为：**Atjok123@ascm** iv. **创建** **SubAccount** **账户。** 在企业-用户管理页面中，添加用户：**SubAccount**，组织：**atjok**，角色：**组织管理员，**修改其密码为：**Admin123@ascm** v. **云盾测试准备（包含云盾测试所需账户创建）。**

**1、一级组织atjok下账号创建：**

**1.1、创建atjokyd 账户**

密码一定要记得修改，修改密码后务必登录atjokyd用户，在个人页面切换当前角色，⚠️修改默认角色为全局组织安全管理员在企业-用户管理页面中,添加一个atjokyd用户,其组织为atjok,角色为组织安全管理员、组织管理员、 安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、平台安全配置管理员、平台安全监察员、全局组织安全监察员，修改其密码为Atjok123@ascm 修改其默认角色为【全局组织安全管理员】 注意：如果现场没有这么多用户角色可选，就有哪些选哪些用户名为 atjokyd 密码为 Atjok123@ascm

**1.2、创建atjoksas 账户**

密码一定要记得修改在企业-用户管理页面中,添加一个atjoksas用户,其组织为atjok,角色为组织安全管理员,修改其密码为 Atjok123@ascm 用户名为 atjoksas 密码为 Atjok123@ascm

**2、一级组织atjoktest下账号创建：**

**2.1、创建atjoktest 账户**

密码一定要记得修改在企业-用户管理页面中,添加一个atjoktest用户,其组织为atjoktest,角色为全局组织安全管理员、组织安全管理员、安全系统配置管理员、平台安全管理员、平台安全配置管理员,修改其密码为 Atjok123@ascm 修改其默认角色为【全局组织安全管理员】 用户名为 atjoktest 密码为 Atjok123@ascm

**3、RAM服务角色授权**

⚠️atjok组织授权角色：“云安全中心”、“堡垒机”/“租户侧堡垒机”、“漏洞扫描”、“态势感知”、“云盾安骑士”、“数据库审计”、“云防火墙”服务角色【找不到的RAM角色可不授权】 流程 ⚠️atjoktest组织授权角色：“云安全中心”、“云盾安骑士”、“云防火墙”服务角色【找不到的RAM角色可不授权】 授权方法：使用admin用户登录ASCM 页面 , 点击配置, 新增RAM角色, 选择组织, 选择RAM服务角色，点击确定

**部署步骤**

1. 下载下来的jok压缩包上传环境及部署。
i. **工具部署机器。**

| 企业版 | 一般的（非大规模） | OPS#4 |
|---|---|---|
|  | 大规模 | OPS#Buffer的第一台 |
| 敏捷版 | 全量版（天基装机） | OPS#3 |

登录现场选用的机器，进入/root/，mkdir pocTest目录，然后将客户端文件上传到现场环境选用的机器上的 /root/pocTest目录下。 ii. **MD5****值验证** 使用md5sum对文件md5进行校验，确保输出的值和文件命中的md5部分相同。 a. 如果下载完成之后后缀名不是.tgz，现场需重命名。 b. 使用tar xvf进行解压，不要单独用gunzip。

```
#md5sum pocTest-20191012_102551-v1.0.0-4a040f8f91d48cde6417bb5bec6d1230.tgz
4a040f8f91d48cde6417bb5bec6d1230 pocTest-20191012_102551-v1.0.0- 4a040f8f91d48cde6417bb5bec6d1230.tgz
```

2. **解压部署。**
流程 i. 进入选用机器的/root/pocTest目录，tar xvf ${文件名}解压该文件，会得到如下两个文件： ii. 在/root/pocTest目录下，执行 `bash install.sh` 命令进行客户端安装。 返回如下示例，如果其中有报错kubectl之类的问题，无需处理，确保docker成功拉起。 流程 iii. 运行完成后，会启动一个以pocDocker开头的容器。

```bash
docker ps -a | grep pocDocker
```

这个容器以host模式启动，无法使用固定端口（其他程序可能占用），容器启动时会自动找一个可以使用的端口，使用 `docker logs` 容器id|grep 'start nginx at' 得到客户端的访问端口，客户端访问链接为http://${ops4_ip}:端口号。

**功能测试执行**

1. **登录。**
账号：tianyan 密码：Tianyan@123!
2. **准备工作**
流程 i. 启动服务。 访问JOK控制台，启动后界面如下： ii. 检查Jok是否正常启动。 等待一段时间，单击**验收测试**切换界面，**验收测试**界面会提示组织和资源集检查正常，可以开始CASE 测试。
