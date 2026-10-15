---
title: "专有云部署服务 ASI部署指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 8
source_pdf: "06_ASI部署指南_empty-manual.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asdelivery/zh/empty-manual.pdf"
converter: line-classifier (PyMuPDF)
---

# 专有云部署服务 ASI部署指南

## 下载ASI安装包

主要介绍ASI工具包的获取、下载。

**前提条件**

已注册阿里云官网账号，并已有阿里云CSM完成账号专有云官网权限授权。

**操作步骤**

1. 打开浏览器（推荐Chrome）。
2. 在地址栏中输入飞天企业版在线管理平台地址（飞天企业版在线管理平台），然后按下**回车**键，进入飞天
企业版在线管理平台页面。

**说明**

在您首次登录飞天企业版在线管理平台后，若出现无权限访问，请联系阿里云CSM进行权限申请。
3. 单击左侧导航栏的**软件中心**>**下载申请**，单击**ASI**，进入下载页面。
4. 在对话框中，输入选择**ASI****版本号**、**CPU****类型**及**目标云实例**等相关信息。
5. 阅读并勾选《使用条款》和《相关风险》。
6. 单击**开始下载**，即可下载目标ASI安装包。

## 部署ASI

ASI是专有云的可视化部署、扩容、升级工具，所以在集群部署前需要在ops1节点上安装ASI工具。本文介

**前提条件**

备机房ops1机器已安装操作系统。 DCI并网已经完成（备机房部署场景下）。

**操作步骤**

1. 登录ops1机器。
2. 挂载移动硬盘到 `/mnt` 目录。

```
mount /dev/sdm /mnt
```

**重要**

| 其中， | /dev/sdm |
|---|---|
| Disk |  |
|  | 命令查看磁盘 |

`/mnt` 是硬盘的挂载点，在ASI拷包环节，可以根据实际情况调整挂载点。
3. 上传ASI安装包到ops1节点 `/home/admin/ASI` 目录下。
4. 解压ASI安装包。

```
tar -zxvf ASI.tar.gz
```

5. 部署ASI。
`cd ASI //`进入部署脚本所在目录
6. 检查ASI部署是否成功。

```
ps -ef | grep asi
```

返回结果中有如上类似信息，则说明ASI部署成功。

**说明**

## ASI命令和日志

本文介绍ASI的重启、停止和全新部署命令，以及如何排查ASI的安装错误。

| 操作项 | 操作方法 |
|---|---|
| 错误排查 | 运行cd ASI/logs命令进入logs目录，查看setup lib.log以及服务的log _ asi server.log。现场安装环境可能不同，导致部分依赖安装失败，需要具体问题具 _ 体分析。 |
| 重启ASI | 命令：./asi asu run.sh restart _ _ |
| 停止ASI | 命令：./asi asu run.sh stop _ _ |
| 全新部署 | 命令：./asi asu run.sh start _ _ |
