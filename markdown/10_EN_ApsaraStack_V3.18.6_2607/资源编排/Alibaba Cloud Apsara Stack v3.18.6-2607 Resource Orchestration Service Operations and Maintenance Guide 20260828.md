---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 7
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Operations and Maintenance Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%B5%84%E6%BA%90%E7%BC%96%E6%8E%92/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Resource%20Orchestration%20Service%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Operations and Maintenance Guide 20260828

Operations and Maintenance Gui Resource Orchestration Service

## ROS component O&M

### API Server

The API Server is used to receive ROS requests, send requests to RabbitMQ clusters, and send the responses returned by the Engine Server to callers. The API Server is used to connect the frontend and backend services. Components The Engine Server and API Server share three servers, all of which are attached to a special Server Load Balancer (SLB) instance. O&M methods The storage path of the API Server information is /home/admin/ros-server/bin/. Basic operations of the API Server: `#/usr/local/ros-python/bin/python/home/admin/ros-`

```
service/bin/ros-api{stop|status|--daemon}
```

`stop` : stops the API Server. `status` : queries the status of the API Server. `--daemon` : starts the API Server in daemon mode. Health criteria Intrinsic availability: The CPU usage and system memory are within the normal range. The API Server is running normally. Associated component availability: ROS is available.

### Engine Server

The Engine Server is used to process stack requests. It shares the three servers with the API Server. O&M methods The storage path of the API Server information is /home/admin/ros-server/bin/. Basic operation of the Engine Server: `/usr/local/ros-python/bin/python`

```
/home/admin/ros-service/bin/ros-engine {stop|status|--daemon}
```

`stop` : stops the Engine Server. `status` : queries the status of the Engine Server. `--daemon` : starts the Engine Server in daemon mode. Health criteria Intrinsic availability: The CPU usage and system memory are within the normal range. The Engine Server is running normally. Associated component availability: ROS is available.

### RabbitMQ clusters

RabbitMQ clusters are used to receive requests from the API Sever and responses from the Engine Server. Components RabbitMQ clusters are composed of nodes. Operations and Maintenance Gui Resource Orchestration Service RabbitMQ clusters are used for messaging. Nodes in the clusters use disks for nonpersistent storage. Messages are written into the queues that correspond to the nodes. Nodes in a cluster can communicate with each other. Typically, to ensure data accuracy, the minimum number of working nodes is set to [Total number of nodes/2] rounded up. If data of nodes are inconsistent, the secondary nodes synchronize queue messages from the primary nodes. O&M methods The storage path of the RabbitMQ information is /opt/rabbitmq-server/. Common RabbitMQ commands are as follows:

| You can run the following command to query the cluster status: |   |
|---|---|
| /usr/local/sbin/rabbitmq-server/sbin/rabbitmqctl cluster status _ |   |

| Nodes |   |
|---|---|
| Disc |   |
| Mem |   |
| Running nodes _ |   |
| Partition | : ind |

`Nodes` : indicates the nodes in the cluster. `Disc` : indicates that the cluster uses disks for storage. `Mem` : indicates that the cluster uses memory for non-persistent storage. `Running_nodes` : indicates the information of the running nodes in the cluster. `Partition` : indicates the partitions of the cluster. If the value field is brackets [], the cluster has no partitions. If this parameter is not empty, the cluster nodes are divided into several partitions. You can run the following command to query the virtual hosts in a cluster: `sudo`

```
/usr/local/sbin/rabbitmqctl list_vhosts
```

Typically, there are two virtual hosts. One is displayed as a forward slash (/), and the other is named based on the region where it resides. Health criteria Intrinsic availability: The CPU usage and system memory are within the normal range. RabbitMQ is running normally, which indicates that clusters have no partitions, queues are properly processed, and messages are properly consumed. Associated component availability: ROS is available.

### Notify Server

The Notify Server is the proxy server for ECS instances that reside in a VPC. It sends the execution status and information of operations on ECS instances to ROS. Components Operations and Maintenance Gui Resource Orchestration Service The Notify Server consists of three servers, all of which are attached to a special SLB instance. O&M methods For example, the virtual IP address of the SLB instance is 10.152.XX.XX. You can run curl `http://10.152.XX.XX:80/health-check` to check whether the Notify Server is running. Health criteria Intrinsic availability: The CPU usage and system memory are within the normal range. Associated component availability: ROS is available.
