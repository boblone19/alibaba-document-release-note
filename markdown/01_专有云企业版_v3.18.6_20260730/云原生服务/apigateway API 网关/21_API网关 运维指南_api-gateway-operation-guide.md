---
title: "网关 API网关 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 11
source_pdf: "21_API网关 运维指南_api-gateway-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apigateway/zh/api-gateway-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 网关 API网关 运维指南

API 网关

## 运维概述

### 运维简介

本文介绍API网关运维的目的、要求、注意事项、以及寻求帮助的方式。

**目的**

本手册指导维护人员对API网关进行预防性维护，确保系统长期稳定运行。维护人员可以根据本手册的指导，处理维护过程中发现的系统问题。如果根据本手册无法解决系统问题，请寻求阿里云API网关工程师的技术支持。

**要求**

维护人员必须拥有IT行业技能，包括计算机网络知识、分布式存储操作知识、问题分析排查能力。 维护人员必须经过阿里云系统岗前培训，学习必要的阿里云API网关知识，包括但不限于系统原理、组网、特性使用和维护工具的使用。

**重要**

在维护操作过程中，维护人员务必遵守操作规章，确保人身安全和系统安全。对用户数据严格保密，未经用户书面许可，禁止复制、传播用户数据。

**注意事项**

为了系统的稳定运行，避免意外事故的发生，维护人员需遵循以下事项： 分层分权管理： 对网络、设备、系统、数据实行分层分权管理，相应业务的维护人员仅拥有完成自身角色任务相对应的权限，防止越权操作而引起系统故障。 系统安全： 在对系统进行任何操作前，需清楚地了解操作的结果，避免危险操作影响系统运行。 在操作过程中遇到的问题，需清楚记录以便问题排查和故障处理。 人身和数据安全： 操作电气设备时，必须根据设备要求做好安全措施。 需使用安全的设备接入业务网络。 未经授权，严禁对数据进行复制和传播。

**寻求帮助**

维护人员在系统维护过程中，如果需要相关帮助，可以联系阿里云API网关技术支持获取帮助。

### 运维架构

本文介绍API网关的运维架构。 API 网关如上图所示，运维主要围绕底座控制台和租户侧控制面、数据面进行。 API 网关

## 运维流程

本文介绍API网关的运维流程。

**网关组件清单**

**cop-console**：网关产品控制台。
**higress-controller**：网关控制器，负责监听K8s资源的更新，并推送给网关数据面。
**higress-gateway**：网关数据面，负责转发流量。
**higress-plugin-server**：网关插件服务器，负责提供插件依赖，数据面会按需拉取插件服务中的插
件。
**redis-builtin**：网关默认提供的一个内置Redis，用于token限流、MCP会话保持等场景。
**rrsa-info-server**：网关开启内容安全后的依赖组件，用于凭证加载。

**网关管控组件Pod巡检**

登录 OPS 服务器，执行 `kubectl get pod -n csb-cop` 命令，查看网关管控组件Pod是否处于终态。

**网关客用集群组件Pod巡检**

1. 登录客户集群master节点/跳板机。
2. 执行以下命令，查看AI网关组件Pod是否处于终态。

```bash
kubectl get pod –n higress-system
```

3. 执行以下命令，查看API网关组件Pod是否处于终态。

```bash
kubectl get pod -n apigateway-system
```

**网关管控组件日志**

1. 登录 cop-console 容器。
2. 执行 `cd /home/admin/cop-console/logs` 命令，进入日志所在目录。
3. 执行 `ls` ，查看日志文件。
API 网关

**说明**

debug.log：业务日志。 import.log：数据迁移日志。 remoting.log：网络连接日志。 scheduler_task.log：定时任务日志。

**网关数据面日志**

执行以下命令查看：

```bash
kubectl logs <higress-gateway-pod-name> -n higress-system kubectl logs <cop-gateway-pod-name> -n apigateway-system
```

**网关路由配置运维**

执行以下命令：

```bash
kubectl get ingress -n higress-system
```

**网关插件配置运维**

执行以下命令：

```bash
kubectl get wasmplugin -n higress-system
```

API 网关

## 常见问题

本文介绍API网关的常见问题以及处理方法。

**网关数据面问题定位思路**

通常情况下，大量流量都集中于数据面组件： `deployment/higress-gateway` 。因此，当该组件出现问题时，其影响范围最大，快速定位问题显得尤为重要。

**判断响应所属的节点**

判断方法：是否存在 `response header: x-envoy-upstream-service-time` 。 若存在，这表明 Higress-gateway 已成功将请求转发至 upstream service，但 upstream service 返回了错误状态。在这种情况下，需要对 upstream service 进行分析，以判断可能的原因。 若不存在，则说明错误信息是由 Higress-gateway 直接返回的，此时可能存在以下两种情况： gateway 本身的转发、拦截规则存在问题。 gateway 无法连接到 upstream service 。 意图：根据 response header 可以确定 50% 的问题原因。

**判断 higress-gateway 的转发规则是否有误**

判断方法：通过 logs 的 error log 确定哪些插件存在下发失败的情况。 意图：根据 higress-gateway 的 logs 可以感知到 40% 的问题原因。

**网关访问不通模型服务**

**问题表现**

直接请求模型服务能够正常返回，但经过网关代理后则无法成功请求。

**解决方案**

1. 检查路由、服务、域名等配置是否正确。
2. 排查 higress-gateway 日志，通常可直接锁定根因。
3. 排查ai-proxy配置是否符合预期。
4. 登录 higress-gateway 容器，使用 `telnet/curl` 测试模型服务是否能访问通，排除网络/安全组等问
题。
5. 进一步查看 higress-gateway 日志，排查配置下发问题。

**页面显示401问题**

**问题表现**

请求网关返回401状态码通常表明存在认证问题。在此类情况下，需要明确识别是网关认证未通过，还是后端服务认证未通过。 API 网关

**解决方案**

1. 通过响应头中的 server 字段进行判断，若包含 "envoy" 字样，则表示请求未转发至后端，网关认证未
通过。
2. 如果确定是网关的认证问题，按以下思路排查：
i. 是否携带消费者凭证。 ii. 是否配置Bearer前缀。
3. 进一步查看 higress-gateway 日志，排查配置下发问题。

**页面显示403问题**

**问题表现**

请求网关返回403状态码通常表示存在认证问题。此类问题需要明确判断是由于网关认证未通过，还是后端服务认证未通过。

**解决方案**

1. 判断哪个链路节点存在认证未通过的情况。
2. 如果确定是网关的认证问题，则排查消费者是否有授权路由。
3. 进一步查看 higress-gateway 日志，排查配置下发问题。

**页面显示404问题**

**问题表现**

请求网关返回404错误通常表明存在路由配置问题。在此类情况下，需要进一步甄别是由于网关路由未找到，还是上游服务未提供对应的API。

**解决方案**

1. 判断哪个链路节点的服务访问点不存在。
2. 如果确定是网关的路由不存在，按以下思路排查：
i. 对应路由的配置是否存在？ ii. 对应路由配置的路由条件是否和请求一致？ iii. 对应的路由配置是否成功下发到数据面，参考如下命令： kubectl exec ${higress-gateway-pod-

```
name} -nhigress-system -- curl -v "127.0.0.1:15000/config_dump" > config_dump.json 。
```

3. 进一步查看 higress-gateway 日志，排查配置下发问题。

**503 service unavailable 问题**

**问题表现**

请求网关返回 503，通常是路由关联的上游服务存在问题。

**解决方案**

1. 确认关联的上游服务是否可以正常访问？
建议在 Higress-gateway pod中通过 `curl` 命令直接测试连通性，避免不同环境的 DNS 差异导致联通性存在问题。
2. 确认关联的上游服务配置是否正确？
确认对应的路由成功发到数据参考如命 API 网关
3. 确认对应的路由配置是否成功下发到数据面，参考如下命令： kubectl exec ${higress-gateway-

```
pod-name} -nhigress-system -- curl -v "127.0.0.1:15000/config_dump" > config_dump.json 。
```

4. 进一步查看 higress-gateway 日志，排查配置下发问题。

**限流不生效**

**问题表现**

配置了ai-token-ratelimit或者cluster-key-rate-limit，但限流未生效。

**解决方案**

1. 对照文档，检查插件配置是否正确，例如格式问题或者Redis未配置。
2. 排查 higress-gateway 中是否存在 Redis 连接问题。
3. 排查 higress-gateway 中是否存在明显的配置解析问题。
4. 检查响应头中的限流相关值是否未达到阈值。
