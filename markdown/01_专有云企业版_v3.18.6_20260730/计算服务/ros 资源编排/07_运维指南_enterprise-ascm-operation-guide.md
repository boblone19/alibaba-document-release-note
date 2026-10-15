---
title: "资源编排 运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 6
source_pdf: "07_运维指南_enterprise-ascm-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ros/zh/enterprise-ascm-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 资源编排 运维指南

资源编排

## 资源编排组件运维

### API Server

API Server主要用来接收ROS请求，发送请求到rabbitmq集群，并发送Engine Server的返回结果给调用组件构成 Engine Server和API Server共享3台机器，全部都挂载在一个特殊的负载均衡实例下面。 运维方法 API Server的基本操作： #/usr/local/ros-python/bin/python/home/admin/ros-

```
service/bin/ros-api{stop|status|--daemon}
```

健康评判标准关联组件可用性：ROS服务可用。

### Engine Server

Engine Server主要用于处理所有堆栈的请求，和API Server共享3台机器。 运维方法 Engine Server的基本操作： `/usr/local/ros-python/bin/python /home/admin/ros-`

```
service/bin/ros-engine {stop|status|--daemon}
```

健康评判标准关联组件可用性：ROS服务可用。

### rabbitmq集群

rabbitmq集群主要用于接收由API Server推送的请求，以及Engine Server推送的请求处理结果。 组件构成 rabbitmq集群主要是消息订阅部分。采用非持久化存储方案，对于每个节点都采用磁盘模式。每一条消息都直接写入集群中每个节点对应的队列中。由于rabbitmq集群的各个节点之间会相互通信，为确保数据的准确性，正常情况下，rabbitmq的节点工作数量最小为[集群节点总数/2向上取整]。当节点中的数据不一致时，slave节点会从master节点中同步队列消息。 运维方法 rabbitmq信息的存放路径：/opt/rabbitmq-server/。 资源编排常用的rabbitmq命令有：

```
查询集群状态 sudo /usr/local/sbin/rabbitmq-server/sbin/rabbitmqctl cluster_status
```

| Nodes |  |
|---|---|
| Disc |  |
| Mem |  |
| Running nodes _ |  |
| Partition | ：集 |

查询集群vhosts `sudo /usr/local/sbin/rabbitmqctl list_vhosts` 正常情况下，vhosts有两个，一个是/，一个是以区域命名的vhost。 健康评判标准自身可用性：CPU、内存正常，rabbitmq服务正常（无脑裂、队列正常、消息消费正常）。 关联组件可用性：ROS服务可用。

### Notify Server

Notify Server作为VPC网络中ECS实例的代理服务器，帮助ECS发送用户数据的执行状态或信息到ROS服务。 组件构成运维方法假设该负载均衡实例的虚拟IP为：10.152.XX.XX，通过curl `http://10.152.XX.XX:80/health-` 健康评判标准自身可用性：CPU、内存正常。 关联组件可用性：ROS服务可用。
