---
title: "容器镜像服务 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 8
source_pdf: "07_运维指南_enterprise-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/acr/zh/enterprise-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 容器镜像服务 运维指南

容器镜像服务

## 运维概述

### 运维简介

本文介绍容器镜像服务ACR运维的目的、要求、注意事项、以及寻求帮助的方式。

**目的**

本手册指导维护人员对容器镜像服务ACR进行预防性维护，确保系统长期稳定运行。维护人员可以根据本手册的指导，处理维护过程中发现的系统问题。如果根据本手册无法解决系统问题，请寻求阿里云容器镜像服务ACR工程师的技术支持。

**要求**

维护人员必须拥有IT行业技能，包括计算机网络知识、分布式存储操作知识、问题分析与排查能力。 维护人员必须经过阿里云系统岗前培训，学习必要的阿里云容器镜像服务ACR知识，包括但不限于系统原理、组网、特性使用和维护工具的使用。

**重要**

在维护操作过程中，维护人员务必遵守操作规章，确保人身安全和系统安全。对用户数据严格保密，未经用户书面许可，禁止复制、传播用户数据。

**注意事项**

为了系统的稳定运行，避免意外事故的发生，维护人员需遵循以下事项： 分层分权管理： 对网络、设备、系统、数据实行分层分权管理，相应业务的维护人员仅拥有完成自身角色任务所对应的权限，防止越权操作而引起系统故障。 系统安全： 在对系统进行任何操作前，需清楚地了解操作的结果，避免危险操作影响系统运行。 在操作过程中遇到的问题，需清楚记录以便问题排查和故障处理。 人身和数据安全： 操作电气设备时，必须根据设备要求做好安全措施。 需使用安全的设备接入业务网络。 未经授权，严禁对数据进行复制和传播。

**寻求帮助**

维护人员在系统维护过程中，如果需要相关帮助，可以联系阿里云容器镜像服务ACR技术支持获取帮助。

### 运维架构

本文介绍容器镜像服务ACR的运维架构。 ACR的运维架构如下图所示： 容器镜像服务

| 运维大类 | 描述 |
|---|---|
| 例行维护 | 包括统一巡检、查看和处理告警。 |
| 故障处理 | 联系阿里云的TAM驻场和SRE专家组协助处理。 |

容器镜像服务

## 运维流程

本文介绍容器镜像服务ACR的运维流程。

**ACR组件清单**

**天基基线组件**

**cr-authentication**：ACR鉴权组件。
**cr-cleaner**：ACR负责清理相关镜像的组件。
**cr-init**：ACR负责注册 API 的组件。
**cr-manager**：ACR管控组件。
**cr-openapi**： ACR中用于和RAM联动鉴权的组件。
**cr-registry**：存储ACR中镜像的组件。
**cr-sync**：ACR中用于同步镜像的组件。
**cr-chart**：ACR中用于Chart的组件。
**cr-convertor**：ACR中用于镜像加速的组件。

**PaaS 基线组件**

**acr-ee**：ACR中负责注册API的组件。
**cr-chart**：ACR负责Chart的组件。
**cr-convertor**：ACR中用于镜像加速的组件。
**manager**：ACR管控组件。
**cr-registry**：存储ACR中镜像的组件。
**cr-unimanager-configinit**：ACR中的前端组件。
**multi-instance**：ACR中用于多实例的组件。

**ACR PaaS 版本组件Pod巡检**

登录ACR所在VM，执行 `kubectl get pod -n acr-system` 命令，查看ACR基线组件Pod是否处于终态。

**ACR 天基容器组件巡检**

登录ACR所在VM，执行 sudo docker ps -a | grep acr 命令，查看ACRPaaS基线组件容器状态。 容器镜像服务

**ACR 天基管控组件日志查看**

登录ACR所在VM，执行 `sudo docker logs <docker-acr-manager-name>` 命令，查看ACRPaaS基线组件容器状态。

**ACR PaaS 容器管控组件日志查看**

登录ACR所在VM，执行 `kubectl logs <manager-pod-name> -n acr-system` 命令，查看ACRPaaS基线组件管控容器状态。
