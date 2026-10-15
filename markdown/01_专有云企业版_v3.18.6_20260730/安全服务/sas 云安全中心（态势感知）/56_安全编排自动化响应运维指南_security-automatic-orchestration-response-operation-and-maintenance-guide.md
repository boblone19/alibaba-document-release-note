---
title: "云安全中心（态势感知） 安全编排自动化响应运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 10
source_pdf: "56_安全编排自动化响应运维指南_security-automatic-orchestration-response-operation-and-maintenance-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sas/zh/security-automatic-orchestration-response-operation-and-maintenance-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（态势感知） 安全编排自动化响应运维指南

## 登录飞天基础运维平台

**前提条件**

已从部署人员或管理员处获取Apsara Uni-manager运维控制台的访问地址、用户名和密码。 Apsara Uni-manager运维控制台访问地址格式为ops.asconsole.intranet-domain-id.com。 推荐使用Chrome浏览器。

**操作步骤**

1. 打开浏览器。
2. 在地址栏中，输入Apsara Uni-manager运维控制台的访问地址ops.asconsole.intranet-domain-
id.com，按回车键。 您可以单击页面右上角的下拉按钮来进行语言切换。

**说明**

3. 输入正确的用户名及密码。
登录Apsara Uni-manager运维控制台的用户名和密码请从部署人员或管理员处获取。

**说明**

首次登录Apsara Uni-manager运维控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。 为提高安全性，密码必须满足以下要求： 英文大小写字母阿拉伯数字（0~9） 特殊符号，包括感叹号（！）、at（@）、井号（#）、美元符号（$）、百分号（%）等密码长度10~20个字符
4. 单击**登录**。
5. 在Apsara Uni-manager运维控制台的顶部菜单栏，选择**平台运维** > **飞天基础运维平台**。
警通知

## 查看告警通知

**操作步骤**

1. 登录飞天基础运维平台。
2. 在Apsara Uni-manager运维控制台的顶部菜单栏，选择**监控告警＞告警管理**＞**告警概览。**
3. 在告警管理左侧导航栏，查看服务的告警信息以及配置相关的告警通知。
控大盘

## 查看监控大盘

**操作步骤**

1. 登录飞天基础运维平台。
2. 在Apsara Uni-manager运维控制台的顶部菜单栏，选择**产品运维＞安全运维＞云盾运维中心**。
3. 在左侧导航栏，选择**监控告警**＞**系统监控**。
4. 在**系统监控**页面，单击**自动化编排**页签，查看安全自动编排响应(SOAR)服务的CPU使用率，负载以及运
行状态。
4. 在左侧导航栏，选择**监控告警**＞**业务监控。**
5. 在**系统监控**页面，单击**SOAR****安全编排自动化响应**页签。
控大盘
6. 单击**剧本执行监控**卡片，查看安全自动编排响应(SOAR)服务剧本运行的成功失败数量。
检任务

## 查看巡检任务

**操作步骤**

1. 登录飞天基础运维平台。
2. 在Apsara Uni-manager运维控制台的顶部菜单栏，选择**产品运维＞安全运维＞云盾运维中心**。
3. 在左侧导航栏，选择**巡检诊断**＞**巡检配置**。
4. 在**巡检模板**页面，选择自动化编排点击**立即巡检**。

**说明**

沙箱诊断，主要查询当前租户侧python沙箱的网络配置，是否符合预期。 全局诊断，主要巡检sophon-web和sophon-bluespace服务，系统资源的使用情况。
5. 切换至巡检记录，点击查看，查询巡检详细信息。
