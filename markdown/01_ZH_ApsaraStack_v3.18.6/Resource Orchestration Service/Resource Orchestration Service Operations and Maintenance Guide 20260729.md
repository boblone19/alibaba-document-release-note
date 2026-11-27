---
title: "资源编排 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 6
source_pdf: "07_运维指南_enterprise-ascm-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ros/zh/enterprise-ascm-operation-guide.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# 资源编排 运维指南

## 目录

- 1 资源编排组件运维
  - 1.1 API Server
  - 1.2 Engine Server
  - 1.3 rabbitmq集群
  - 1.4 Notify Server

资源编排

## 1 资源编排组件运维

### 1.1 API Server

API Server主要用来接收ROS请求，发送请求到rabbitmq集群，并发送Engine Server的返回结果给调用方。API Server是前端业务与后端业务连接的枢纽。 组件构成 Engine Server和API Server共享3台机器，全部都挂载在一个特殊的负载均衡实例下面。 运维方法 API Server信息的存放路径：/home/admin /ros-server/bin/。 API Server的基本操作： `#/usr/local/ros-python/bin/python/home/admin/ros-`

```
service/bin/ros-api{stop|status|--daemon}
```

`stop` ：停止API Server。 `status` ：查询API Server状态。 `--daemon` ：以daemon的方式启动API Server。 健康评判标准自身可用性：CPU、内存正常，API Server服务正常。 关联组件可用性：ROS服务可用。

### 1.2 Engine Server

Engine Server主要用于处理所有堆栈的请求，和API Server共享3台机器。 运维方法 API Server信息的存放路径：/home/admin /ros-server/bin/。 Engine Server的基本操作： `/usr/local/ros-python/bin/python /home/admin/ros-`

```
service/bin/ros-engine {stop|status|--daemon}
```

`stop` ：停止Engine Server。 `status` ：查询Engine Server状态。 `--daemon` ：以daemon的方式启动Engine Server。 健康评判标准自身可用性：CPU、内存正常，Engine Server服务正常。 关联组件可用性：ROS服务可用。

### 1.3 rabbitmq集群

rabbitmq集群主要用于接收由API Server推送的请求，以及Engine Server推送的请求处理结果。 组件构成主要由rabbitmq集群的各个节点组成。 rabbitmq集群主要是消息订阅部分。采用非持久化存储方案，对于每个节点都采用磁盘模式。每一条消息都直接写入集群中每个节点对应的队列中。由于rabbitmq集群的各个节点之间会相互通信，为确保数据的准确性，正常情况下，rabbitmq的节点工作数量最小为[集群节点总数/2向上取整]。当节点中的数据不一致时，slave节点会从master节点中同步队列消息。 运维方法 rabbitmq信息的存放路径：/opt/rabbitmq-server/。 资源编排常用的rabbitmq命令有：

```
查询集群状态 sudo /usr/local/sbin/rabbitmq-server/sbin/rabbitmqctl cluster_status
```

| Nodes |   |
|---|---|
| Disc |   |
| Mem |   |
| Running nodes _ |   |
| Partition | ：集 |

`Nodes` ：表示集群中所有的节点信息。 `Disc` ：表示集群使用的是磁盘模式。 `Mem` ：表示集群使用的是内存模式，非持久化数据。 `Running_nodes` ：表示集群现在正在运行的节点信息。 `Partition` ：集群是否分区（脑裂）的信息。如果为[]，表示集群没有发生脑裂；如果不为空，表示集群的节点被分裂为若干个partition。 查询集群vhosts `sudo /usr/local/sbin/rabbitmqctl list_vhosts` 正常情况下，vhosts有两个，一个是/，一个是以区域命名的vhost。 健康评判标准自身可用性：CPU、内存正常，rabbitmq服务正常（无脑裂、队列正常、消息消费正常）。 关联组件可用性：ROS服务可用。

### 1.4 Notify Server

Notify Server作为VPC网络中ECS实例的代理服务器，帮助ECS发送用户数据的执行状态或信息到ROS服务。 组件构成 Notify Server有三台服务器，全部都挂载在一个特殊的负载均衡实例下面。 运维方法假设该负载均衡实例的虚拟IP为：10.152.XX.XX，通过curl `http://10.152.XX.XX:80/health-` `check` 可以查看Notify Server是否在工作。 健康评判标准自身可用性：CPU、内存正常。 关联组件可用性：ROS服务可用。
