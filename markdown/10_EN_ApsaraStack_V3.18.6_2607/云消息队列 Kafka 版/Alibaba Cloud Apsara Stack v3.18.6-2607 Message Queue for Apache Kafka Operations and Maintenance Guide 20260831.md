---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Message Queue for Apache Kafka Operations and Maintenance Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 44
source_pdf: "aea4b9061a1eaba3_Alibaba Cloud Apsara Stack v3.18.6-2607 Message Queue for Apache Kafka Operations and Maintenance Gu"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97%20Kafka%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Message%20Queue%20for%20Apache%20Kafka%20Operations%20and%20Maintenance%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Message Queue for Apache Kafka Operations and Maintenance Guide 20260831

## Table of Contents

- 1 Overview
- 2 Kafka Operations Console User Guide
  - 2.1 Log in to the Kafka Operations Console
  - 2.2 Overview
  - 2.3 Instance list
  - 2.4 Broker list
  - 2.5 Metadata management
  - 2.6 Upgrade a cluster
- 3 Routine maintenance
  - 3.1 Pod maintenance
    - 3.1.1 Query a list of pods
    - 3.1.2 Query the information about a pod
    - 3.1.3 Query the logs of a pod
    - 3.1.4 Restart a Pod
    - 3.1.5 Query the information about PVs and PVCs
    - 3.1.6 FAQ
  - 3.2 Process maintenance
    - 3.2.1 Query the metric information of brokers
    - 3.2.2 View log information
    - 3.2.3 Query the status of a topic
    - 3.2.4 Query the status of a consumer group
    - 3.2.5 Query the data of ZooKeeper
    - 3.2.6 Update the configurations of a topic
    - 3.2.7 FAQ
  - 3.3 Other maintenance operations
    - 3.3.1 Evaluate the capacity of a cluster
- 4 Routine inspection
  - 4.1 Inspect the status of pods
  - 4.2 Inspect the resource availability
  - 4.3 Inspect the service availability
  - 4.4 Inspect a physical server after a restart

## 1 Overview

You must perform various maintenance operations on ApsaraMQ for Kafka to ensure its stability and availability. ApsaraMQ for Kafka supports the following maintenance operations: r Guide

## 2 Kafka Operations Console User Guide

**User Guide**

### 2.1 Log in to the Kafka Operations Console

**Console**

This topic describes how to log in to the Kafka Operations Console. The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

r Guide
3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar, choose **Product Operation > Middleware > Kafka**
**Operations Console**.

### 2.2 Overview

This topic describes how to query the metrics of ApsaraMQ for Kafka.
1. Log in to the Kafka Operations Console.
2. By default, the **Overview** page is displayed. This page displays the metric overview, disk
usage top broker, inflow TPS top broker, outflow TPS top broker, alert statistics, and last 5 alert records.

| Section | Description |
|---|---|
| Indicator Overview | Total number of instances: displays the number of instances that are running in the system. Total number of brokers: the total number of online brokers in all clusters. You can click the number below Total number of brokers to go to the Broker Management page and view the details of brokers. Total number of topics: the number of topics that are created in the system. Total number of Consumers: the number of consumer instances that are connected to the cluster. |

r Guide

| Disk using TOP Broker | This section displays the brokers with the highest disk usage, including the name of each broker and the specific disk usage in percentage. |
|---|---|
| Inflow TPS TOP Broker | This section displays the top five brokers with the highest inbound message rate. Unit: bytes per second. |
| Outflow TPS TOP Broker | This section displays the top five brokers with the highest outbound message rate. Unit: bytes per second. |
| Alarm Statistics | This section displays the total number of alerts with different severity levels, such as P1 Critical, P2 Major, P3 Minor, and P4 Warning. |
| Last 5 alarm records | This section displays the most recent five alert records, including the alert item, severity, and alert time. Click View more to go to the Alert List page. On this page, you can view the alert information, including real-time alerts that are not handled and historical alerts that are handled. |

### 2.3 Instance list

This topic describes how to view, configure, and diagnose instances.
1. Log in to the Kafka Operations Console.
2. In the left-side navigation pane, click **Instances**.
3. The **Instance List** page displays the basic information about the instances.

> **Note:** The system synchronizes instance information every 10 minutes. Therefore, the instance data on the current page may be delayed.

| Parameter | Description |
|---|---|
| Instance ID | The ID of the ApsaraMQ for Kafka instance. |
| Status | The status of the ApsaraMQ for Kafka instance. |

r Guide

| Number of brokers | The number of broker nodes on the instance. |
|---|---|
| Number of topics | The number of topics that are created on each instance. |
| ConsumerGroups Quantity | The number of active consumer groups on each instance. |
| Inflow TPS B/s | The amount of data that is sent to the instance per second. |
| Outflow TPS B/s | The amount of data that is transmitted from the instance per second. |
| Version Number | The Kafka version used by the instance. |
| Operation | Click View to go to the Broker Management page. You can view the information about the brokers on the instance. Click Configuration. In the Instance configuration panel, you can view the keys and values of the current instance. Click Diagnosis to view the diagnostic report of the instance. In the Diagnostic Report dialog box, click View Details in the Operation column. The detailed diagnostic information is displayed in the JSON format. |

### 2.4 Broker list

This topic describes how to view broker details.
1. Log in to the Kafka Operations Console.
2. In the left-side navigation pane, click **Broker List**.
3. (Optional) On the **Broker List** page, you can quickly filter brokers by **instance ID** and
**Broker Name**.
The system synchronizes instance information every 10 minutes. Therefore, the instance data on the current page may be delayed.
4. The top of the **Broker List** page displays the ID, node count, and type of the current
instance. The list shows the basic information for each broker in the instance.

| Parameter | Description |
|---|---|
| Broker Name | The name of the broker node. |

r Guide

| Host IP | The broker node's host IP address. |
|---|---|
| Status | The operational status of the broker node. |
| Partition Count | The total number of topic partitions hosted on the broker node. |
| Inflow TPS (B/s) | The amount of data that flows into the broker node per second. |
| Outflow TPS (B/s) | The amount of data that flows out of the broker node per second. |

5. In the **Actions** column, click **View** to see the **Basic Information**, **Key Metrics**, and
**Process Information** for the broker.

| Section | Description |
|---|---|
| Basic Information | Displays information such as the broker name, IP address, status, and partition count. |

r Guide

| Key Metrics | Inbound Traffic: The amount of data, in bytes, that flows into the broker node per second. Outbound Traffic: The amount of data, in bytes, that flows out of the broker node per second. Inbound Traffic of Rejected Messages: The amount of message data, in bytes, rejected by the broker node per second. Inbound Messages: The number of messages received by the broker node per second. Produce Request Rate: The number of produce requests sent to the broker node per second. Fetch Request Rate: The number of fetch requests sent to the broker node per second. CPU Usage (main): The CPU usage of the broker's main process. CPU Usage (agent): The CPU usage of the agent process. Memory Usage (main): The memory usage of the broker's main process. Memory Usage (agent): The memory usage of the agent process. Used Disk Space: The amount of disk space used on the broker's node. Total Disk Space: The total disk capacity of the broker's node. Disk Usage: The percentage of disk space used on the broker's node. |
|---|---|
| Process Information | Displays information such as process ID, username, process name, CPU usage, memory usage, status, and thread count. |

### 2.5 Metadata management

On the Metadata Management page, you can use **ZooKeeper** to view and manage metadata structures of ApsaraMQ for Kafka.
1. Log in to the Kafka Operations Console.
2. In the left-side navigation pane, click **Metadata Management**.
3. On the **Metadata Management** page, view and manage ApsaraMQ for Kafka metadata.
**Broker ZooKeeper**: This tab displays the core metadata of ApsaraMQ for Kafka clusters
in ZooKeeper. r Guide a. Click the **Broker ZooKeeper** tab. On this tab, select the ID of an ApsaraMQ for Kafka instance from the **Instance ID** drop-down list. The metadata path of the instance is displayed on the left side of the tab.

> **Note:** Click **Refresh** to obtain the latest ZooKeeper data.

b. In the left-side navigation tree, click a node. The detailed data of the node is displayed on the right side.

> **Important:** a. Do not modify ZooKeeper data in the production environment. This may cause
> service interruptions.
> b. If you delete a node, the normal operation of ApsaraMQ for Kafka is affected.
> Proceed with caution.

Click **Edit node** to modify the JSON data of the node. This operation can be performed only in the environments that support writing. Click **Delete Node** to delete the ZooKeeper node.
**Middleware ZooKeeper**: This tab displays the metadata of ApsaraMQ for Kafka
middleware components in ZooKeeper. ApsaraMQ for Kafka middleware components include the following items: `kafka-console` : console-related configurations `kafkaReplicator` : replication task configurations `kafkaConnect` : Cloud Connector (CC) instance configurations a. Click the **Middleware ZooKeeper** tab. The metadata path is displayed on the left side of the tab.

> **Note:** Click **Refresh** to obtain the latest ZooKeeper data.

b. In the left-side navigation tree, click a node. The detailed data of the node is displayed on the right side.

> **Important:** a. Do not modify ZooKeeper data in the production environment. This may cause
> service interruptions.
> b. If you delete a node, the normal operation of ApsaraMQ for Kafka is affected.
> Proceed with caution.

Click **Edit node** to modify the JSON data of the node. This operation can be performed only in the environments that support writing. Click **Delete Node** to delete the ZooKeeper node.

### 2.6 Upgrade a cluster

r Guide On the **Cluster Upgrade** page, you can manage key components such as Broker, Connect, and Replicator in a visualized manner.

**Upgrade a cluster**

> **Note:** You can upgrade only the clusters whose **Upgrade Status** is **Upgrade Required**.

1. Log in to the Kafka Operations Console.
2. In the left-side navigation pane, click **Upgrade**.
3. On the **Cluster Upgrade** page, find the cluster that you want to upgrade and click
**Upgrade** in the **Operation** column.
4. In the **Cluster Upgrade** dialog box, confirm that the cluster information is correct,
configure the **Remark** parameter, and then click **OK**.

> **Note:** After the upgrade is complete, the **Upgrade Status** changes to **Up to date**.

**View the upgrade record**

1. Optional. On the **Cluster Upgrade** page, enter a keyword in the **Cluster Name** field or
select a component type from the **Component Type** drop-down list to search for clusters.
2. In the cluster list, you can view information such as **Cluster Name**, **Namespace**,
**Component Type**, **Upgrade Status**, and **Cluster Status**.
3. Find the cluster that you want to view and click **Upgrade History** in the **Operation**
column. In the Upgrade History panel, you can view the information about the cluster, such as **Upgrade Time**, **Before Upgrade Image**, **After Upgrade Image**, **Status**, and
**Operator**.
4. In the upgrade history list, click **Details** in the **Operation** column to view information such
as basic information, image changes, and upgrade process.

## 3 Routine maintenance

### 3.1 Pod maintenance

#### 3.1.1 Query a list of pods

This topic describes how to query a list of pods in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pod -o wide| grep alibaba-kafka command to query a list of pods.

```
alibaba-kafka-autotest-***** 0/1 Completed 0 5h14m 10.**.*.** a*******8.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-multi-*******-kafka-0 2/2 Running 0 35m 10.**.**.** a*******4.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-multi-*******-kafka-1 2/2 Running 0 35m 10.**.**.** a*******8.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-multi-*******-kafka-2 2/2 Running 0 36m 10.**.**.** a*******8.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-private-paas-*******-0 2/2 Running 1 23h 10.**.**.*** a*******5.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-private-paas-*******-1 2/2 Running 0 23h 10.**.**.*** a*******3.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-private-paas-*******-2 2/2 Running 1 23h 10.**.**.*** a*******6.cloud.b**.am****** <none> <none> alibaba-kafka-console-*******b59-bqvn6 1/1 Running 0 172m 10.**.**.** a*******3.cloud.b**.am****** <none> <none> alibaba-kafka-operator-*******9cc-s8s49 1/1 Running 0 23h 10.**.**.*** a*******3.cloud.b**.am****** <none> <none>
```

> **Note:** In most cases, the kafka-cluster cluster has three pods, the operator cluster has only one pod, and the manager cluster has one or two pods.
> The number of pods varies based on the deployment environment.
> In normal cases, pods are in the Running state.

#### 3.1.2 Query the information about a pod

If an exception occurs during the deployment of a pod, you can query the information about the pod in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl describe pod <pod>` command to query the information about a pod.

| example, if the name of a pod is | alibaba-kafka-cluster-private-paas-*******-0 |   |
|---|---|---|
| kubectl describe pod alibaba-kafka-cluster-private-paas-*******-0 |   |   |
|   |   | command |

```json
Name: alibaba-kafka-cluster-private-paas-*******-0 Namespace: default Priority: 0 PriorityClassName: <none> Node: a*******05.cloud.b**.am******/10.**.**.*** Start Time: Sun, 30 Aug 2020 11:58:35 +0300 Labels: app=alibaba-kafka-broker
                    app.kubernetes.io/instance=alibaba-kafka
                    app.kubernetes.io/managed-by=Tiller
                    app.name=alibaba-kafka-cluster-private-paas-*******
                    controller-revision-hash=alibaba-kafka-cluster-private-paas-defaul
t-*******98b
                    helm.sh/chart=alibaba-kafka-0.0.6-****bef
                    kafka.env=private-pass
                    statefulset.kubernetes.io/pod-name=alibaba-kafka-cluster-private-p
aas-*******-0 Annotations: networking.alibaba.com/ip:
                      {"Address":
{"IP":"10.**.**.***","Mask":"///8AA=="},"Gateway":"10.**.**.***","NetID":11,"Subnet":"s net-cn-*******-env**-amtest*****-a-1",... Status: Running IP: 10.**.**.*** Controlled By: StatefulSet/alibaba-kafka-cluster-private-paas-******* Containers:
  main:
    Container ID:
docker://3fa64fb32**************8f08ed93fdbde08f04b7e0fb1ea1d699ecce1c4fe
    Image:          cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkabroker:efbede0**************e7753ac11e605d943e57af0ebac1f336567ad7fc160
    Image ID:       docker-pullable://cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkabroker@sha256:66726a9c09**************4e3a632383d3f1378c5324dbbd05b0a6d45aa631
    Ports:          9092/TCP, 9093/TCP, 9592/TCP, 8081/TCP
    Host Ports:     0/TCP, 0/TCP, 0/TCP, 0/TCP
    State:          Running
      Started:      Sun, 30 Aug 2020 11:58:52 +0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  5Gi
    Requests:
      cpu:     2
      memory:  4Gi
```

`i`

```
[/h /di/kfk l/h
```

`k``h` `l``h`

```
h]dl
```

`i`

```
    Liveness:  exec [/home/admin/kafka-tools/check-health.sh] delay=900s timeout=180s
period=15s #success=1 #failure=3
    Environment:
      MOCK_DEADLOCK:                            false
      proxy_security_protocol_sasl_ssl:         true
      middleware_zk_port:                       2188
      sasl_ssl_requestip_mode:                  local
      vpc_mode_vpc_id:                          vpc-rt1k708pzc***
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-*******
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.**.**.***,10.**.**.***,10.**.**.***
      vpc_mode_delete_service_enable:           false
      vpc_mode_vsw_id:                          vsw-rt1fjm1djg***
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.***.***.**:8080,192.***.***.**:8080,192.***.***.**:8080
      vips_9093:                                UNKNOWN_VARIABLE
      async_start:                              true
      enable_prometheus_javaagent:              true
      cluster_env:                              private-pass
      enable_auto_updatevip:                    true
      aliyun_logs_kafka:                        /home/admin/logs/alikafka/*.log
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              4294967296 (requests.memory)
      request_cpu:                              2 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              4294967296 (requests.memory)
      request_cpu:                              2 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      proxy_cluster_name:                       private-paas-*******
    Mounts:
      /alidata1 from kafka-datadir (rw)
      /home/admin/logs from volume-0 (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-k2stw (ro)
  agent:
    Container ID:
docker://57d3d96ad8**************0d34fdf616b598b927417597883d92e9287c09c8
    Image:          cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkaagent:4d43d896d38**************f8184f0f18c517df3544a72a00d8de71b497eee
    Image ID:       docker-pullable://cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkaagent@sha256:43c876cc71**************70f8ca367ebe44bd959210c54ee28f4cd775a97f
```

```
agent@sha256:43c876cc71**************70f8ca367ebe44bd959210c54ee28f4cd775a97f
    Port:           9089/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 31 Aug 2020 09:33:06 +0300
    Last State:     Terminated
      Reason:       OOMKilled
      Exit Code:    143
      Started:      Sun, 30 Aug 2020 11:59:08 +0300
      Finished:     Mon, 31 Aug 2020 09:32:49 +0300
    Ready:          True
    Restart Count:  1
    Limits:
      cpu:     1
      memory:  1Gi
    Requests:
      cpu:     1
      memory:  512Mi
    Liveness:  exec [/home/admin/agent/bin/check.sh] delay=300s timeout=180s
period=15s #success=1 #failure=3
    Environment:
      MOCK_DEADLOCK:                            false
      proxy_security_protocol_sasl_ssl:         true
      middleware_zk_port:                       2188
      sasl_ssl_requestip_mode:                  local
      vpc_mode_vpc_id:                          vpc-rt1k708pzc13i*******v
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-*******
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.**.**.***,10.**.**.***,10.**.**.***
      vpc_mode_delete_service_enable:           false
      vpc_mode_vsw_id:                          vsw-rt1fjm1djgpia*******6
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.***.***.**:8080,192.***.***.**:8080,192.***.***.**:8080
      vips_9093:                                UNKNOWN_VARIABLE
      async_start:                              true
      enable_prometheus_javaagent:              true
      cluster_env:                              private-pass
      enable_auto_updatevip:                    true
      aliyun_logs_kafka:                        /home/admin/logs/alikafka/*.log
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              536870912 (requests.memory)
      request_cpu:                              1 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      replicas:                                 3
```

`ep`

```
cas:
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              536870912 (requests.memory)
      request_cpu:                              1 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      proxy_cluster_name:                       private-paas-*******
    Mounts:
      /home/admin/agent/logs from volume-1 (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-k2stw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kafka-datadir:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the
same namespace)
    ClaimName:  kafka-datadir-alibaba-kafka-cluster-private-paas-*******-0
    ReadOnly:   false
  volume-0:
    Type:          HostPath (bare host directory volume)
    Path:          /var/lib/docker/logs/alibaba-kafka/home/admin/logs
    HostPathType:  DirectoryOrCreate
  volume-1:
    Type:          HostPath (bare host directory volume)
    Path:          /var/lib/docker/logs/alibaba-kafka/home/admin/agent/logs
    HostPathType:  DirectoryOrCreate
  default-token-k2stw:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-k2stw
    Optional:    false
QoS Class: Burstable Node-Selectors: networking.alibaba.com/asw=asw-cn-*******-env**-amte*******-a Tolerations: node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events: <none>
```

> **Note:** In most cases, the value of the Events parameter is <none>.

#### 3.1.3 Query the logs of a pod

This topic describes how to query the logs of a pod in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl logs <pod>` command to query the logs of a pod.

|   | alibaba-kafka-operator-6b9dbb49cc-s8s49 |
|---|---|
| kubectl logs alibaba-kafka-operator-6b9dbb49cc-s8s49 |   |

```json
{"level":"info","ts":1598777607.4786668,"logger":"controller_kafka","msg":"Reconcile Kafka......","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-priv ate-release-alibaba-kafka","RequestID":1598777607478639249} {"level":"info","ts":1598777607.4789321,"logger":"controller_kafka","msg":"reconcileClu erStatus expire size:3, current size:3","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-private-r elease-alibaba-kafka","RequestID":1598777607478639249} {"level":"info","ts":1598777608.3835506,"logger":"controller_kafka","msg":"Reconcile Kafka......","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-priv ate-release-alibaba-kafka","RequestID":1598777608383517127} {"level":"info","ts":1598777608.3838317,"logger":"controller_kafka","msg":"reconcileClu erStatus expire size:3, current size:3","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-private-r elease-alibaba-kafka","RequestID":1598777608383517127}
```

#### 3.1.4 Restart a Pod

This topic describes how to restart a Pod for Message Queue for Apache Kafka.

> **Important:** This is a high-risk operation. Perform this procedure only with the assistance of O&M personnel.

**Background information**

Pods cannot be restarted directly. If a Pod becomes abnormal, first try restarting its process. If this fails and the Pod cannot be recovered, you can restart the Pod by deleting it. 1.
2. Run the `kubectl delete pod <pod>` command to delete the Pod.

| For example, if the Pod name is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl delete pod alibaba-kafka-cluster-private-paas-default-0 |   |   |
|   |   | . |

#### 3.1.5 Query the information about PVs and PVCs

**PVCs**

This topic describes how to query the information about persistent volumes (PVs) and persistent volume claims (PVCs) in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

**PV**

PVs are storage resources in a cluster that are configured by an administrator.

**PVC**

PVCs are storage requests from users. PVCs consume PVs. You can specify the size and access mode of a PVC.

**Query the information about PVs**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pv | grep kafka command to query the information about all PVs.

```
local-pv-44****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-0 fast-disks 30d local-pv-4e****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-0 fast-disks 26d local-pv-75****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-2 fast-disks 24d local-pv-8e****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-1 fast-disks 17d local-pv-8f****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 fast-disks 17d local-pv-bc****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-1 fast-disks 17d local-pv-bf****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-1 fast-disks 24d local-pv-ca****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-2 fast-disks 34d local-pv-cd****** 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-2 fast-disks 34d pvc-3066e824-eb37-11ea-bf33-6805caa****** 1Mi RWX Delete Bound kafka-autotest-default-cell/lxcfs-pvc lxcfs-sc 6h29m yoda-0409d39d-eb52-11ea-bf33-6805ca****** 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-2 yoda-lvm 3h17m yoda-0c861b0b-e777-11ea-bf33-6805caa***** 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-private-paas-default-0 yoda-lvm 5d1h yoda-5a840f48-e777-11ea-bf33-6805ca****** 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-private-paas-default-1 yoda-lvm 5d1h yoda-b584d7ee-e777-11ea-bf33-6805ca****** 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-private-paas-default-2 yoda-lvm 5d yoda-d3b992bb-eb51-11ea-bf33-6805ca****** 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 yoda-lvm 3h18m yoda-edf9999c-eb51-11ea-bf33-6805ca****** 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-1 yoda-lvm 3h18m
```

3. Run the `kubectl describe pv <pv>` command to query the information about a PV.

| kubectl describe pv local-pv-441b2d75 |   |   |
|---|---|---|
| whose name is | local-pv-441b2d75 | . |

```
Name: local-pv-44****** Labels: <none> Annotations: pv.kubernetes.io/bound-by-controller: yes
                   pv.kubernetes.io/provisioned-by: local-volume-provisioner-a36******
.cloud.b**.am******-47******-cd51-11ea-bf33-6805ca****** Finalizers: [kubernetes.io/pv-protection] StorageClass: fast-disks Status: Released Claim: default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba -kafka-0 Reclaim Policy: Delete Access Modes: RWO VolumeMode: Filesystem Capacity: 7393Gi Node Affinity:
  Required Terms:
    Term 0:        kubernetes.io/hostname in [a36******.cloud.b**.am******]
Message: Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /var/lib/docker/data/disk/disk7
Events: <none>
```

**Query the information about PVCs**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pvc | grep kafka command to query the information about all PVCs.

```
kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 Bound yoda-d3b992bb-e b51-11ea-bf33-6805c****** 90Gi RWO yoda-lvm 3h29m kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-1 Bound yoda-edf9999c-e b51-11ea-bf33-6805c****** 90Gi RWO yoda-lvm 3h28m kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-2 Bound yoda-0409d39d-e b52-11ea-bf33-6805c****** 90Gi RWO yoda-lvm 3h28m kafka-datadir-alibaba-kafka-cluster-private-paas-default-0 Bound yoda-0c861b0be777-11ea-bf33-6805c****** 90Gi RWO yoda-lvm 5d1h kafka-datadir-alibaba-kafka-cluster-private-paas-default-1 Bound yoda-5a840f48e777-11ea-bf33-6805c****** 90Gi RWO yoda-lvm 5d1h kafka-datadir-alibaba-kafka-cluster-private-paas-default-2 Bound yoda-b584d7eee777-11ea-bf33-6805c****** 90Gi RWO yoda-lvm 5d1h
```

3. Run the `kubectl describe pvc <pvc>` command to query the information about a PVC.
For example, you can run the `kubectl describe pvc kafka-datadir-alibaba-kafka-cluster-`

|   | command to query the information ab |   |
|---|---|---|

```
 kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 .
```

```
Name: kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 Namespace: default StorageClass: yoda-lvm Status: Bound Volume: yoda-d3b992bb-eb51-11ea-bf33-6805c****** Labels: app=alibaba-kafka-broker
               app.name=alibaba-kafka-cluster-multi-alibaba-kafka
Annotations: pv.kubernetes.io/bind-completed: yes
               pv.kubernetes.io/bound-by-controller: yes
               volume.beta.kubernetes.io/storage-provisioner:
yodaplugin.csi.alibabacloud.com
               volume.kubernetes.io/selected-node: a36******4.cloud.b**.am******
Finalizers: [kubernetes.io/pvc-protection] Capacity: 90Gi Access Modes: RWO VolumeMode: Filesystem Events: <none> Mounted By: alibaba-kafka-cluster-multi-alibaba-kafka-0
```

#### 3.1.6 FAQ

This topic describes common issues with pod operation and maintenance.

> **Important:** These are high-risk operations. Work with operations and maintenance (O&M) personnel before you proceed.

**Pod in Terminating state**

Cause The network plugin container has failed. Resolution Force delete the pod. After deletion, the system automatically reschedules the pod.

|   |   | alibaba-kafka-cluster-private-paas-default-0 | , run the command |
|---|---|---|---|
| kubectl delete pod alibaba-kafka-cluster-private-paas-default-0 -n default --force -- |   |   |   |
|   | . |   |   |

**Pod in Pending state**

Possible causes: The PV resource is not ready. No suitable node is available for scheduling. Resolution Run `kubectl describe pod <pod>` to check the resource status. Ensure that the required resources are available.

**Pod in CrashLoopBackoff state**

Cause This issue typically occurs when an incorrect ZooKeeper configuration address causes the Message Queue for Apache Kafka process to restart repeatedly. Resolution
1. Run `kubectl describe pod <pod>` to find the log path.
2. Navigate to the directory by running `cd <filepath>` , and then view the server.log file.

|   | docker ps -a \| grep main.*alibaba.*kafka \| awk |
|---|---|
| '{print $1}' \| xargs -i docker cp {}:/home/admin/logs/alikafka/server.lo |   |

> the log file to the host machine.

**Pod in Error state**

Cause This issue typically occurs when residual data remains after redeployment and cleanup. Resolution Delete the disk data from the node's physical machine.

**Incremental broker.id causes data loss or unavailability**

Possible causes: A write error on the disk prevented the PV resource from mounting. Cleaning up Message Queue for Apache Kafka resources without also cleaning up the ZooKeeper data leads to PV data loss. Resolution
1. Run `kubectl get kafka -o yaml > new_kafka.yaml` to save the YAML file.
2. Run `kubectl delete -f kafka.yaml` to delete the Message Queue for Apache Kafka
resources.

| kubectl get pvc \| grep "alibaba-kafka-cluster" \| awk '{print $1}' \| xargs kubectl |   |
|---|---|
|   | to delete the PVC resources. |

4. Verify that the resources have been cleaned up:
i. Run kubectl get pod | grep kafka.*cluster to verify that the pods are deleted. ii. Run kubectl get pvc | grep kafka to verify that the PVCs are deleted. iii. Run kubectl get pv | grep kafka to verify that the PVs are deleted.
5. Delete the data from the ZooKeeper path:
i. Run `kubectl exec -it zk-middleware-0 bash` to enter the ZooKeeper container. ii. Run `cd /usr/share/zookeeper/bin/` to change to the ZooKeeper bin directory. iii. Run `sh zkCli.sh -server <zookeeper-pod-ip>:2188` to connect to the ZooKeeper server. iv. Run `ls /` to list all directories in the root directory. v. Run `rmr /kafka-private-clusters` to delete the ZooKeeper path data.
6. Redeploy Message Queue for Apache Kafka:
i. In the new_kafka.yaml file, remove the `privileged: true` line. ii. Run `kubectl create -f new_kafka.yaml` to redeploy Message Queue for Apache Kafka.

### 3.2 Process maintenance

#### 3.2.1 Query the metric information of brokers

**brokers**

This topic describes how to query the metric information of brokers in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

|   | alibaba-kafka-cluster-private-paas-default-0 |
|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `java -jar kafka-pkgs/KafkaMetricChecker.jar broker` command to query the
metric information of brokers.

```
--------------------------------------------------------------------------------------- ---------------------------------------------------------------
|Network
```

|

```
|ObjectName                                                     Type            Attribu
eName Value Threshold Op| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|RequestChannel_RequestQueueSize                                Gauge           Value
0.00 500 GTE|
|RequestChannel_ResponseQueueSize                               Gauge           Value
0.00 500 GTE|
|RequestMetrics_ThrottleTimeMs_Fetch                            Histogram
75thPercentile 0.00 10 GTE|
|RequestMetrics_ThrottleTimeMs_Fetch                            Histogram
98thPercentile 0.00 10 GTE|
|RequestMetrics_ThrottleTimeMs_Fetch                            Histogram
50thPercentile 0.00 10 GTE|
|RequestMetrics_ThrottleTimeMs_Produce                          Histogram
75thPercentile 0.00 10 GTE|
|RequestMetrics_ThrottleTimeMs_Produce                          Histogram
98thPercentile 0.00 10 GTE|
|RequestMetrics_ThrottleTimeMs_Produce                          Histogram
50thPercentile 0.00 10 GTE|
|SocketServer_NetworkProcessorAvgIdlePercent                    Gauge           Value
```

|

```
1.00 0.3 LTE| --------------------------------------------------------------------------------------- --------------------------------------------------------------- --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|Server
```

|

```
|ObjectName                                                     Type            Attribu
eName Value Threshold Op| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|BrokerTopicMetrics_BytesInPerSec                               Meter           OneMinu
teRate 0.00 null null|
|BrokerTopicMetrics_BytesOutPerSec                              Meter           OneMinu
teRate 0.00 null null|
|BrokerTopicMetrics_BytesRejectedPerSec                         Meter           OneMinu
teRate 0.00 null null|
|BrokerTopicMetrics_FailedFetchRequestsPerSec                   Meter
OneMinuteRate 0.00 null null|
|BrokerTopicMetrics_FailedProduceRequestsPerSec                 Meter
OneMinuteRate 0.00 null null|
|BrokerTopicMetrics_MessagesInPerSec                            Meter           OneMinu
teRate 0.00 null null|
|BrokerTopicMetrics_TotalFetchRequestsPerSec                    Meter
OneMinuteRate 295.95 null null|
|BrokerTopicMetrics_TotalProduceRequestsPerSec                  Meter
OneMinuteRate 0.00 null null|
|KafkaRequestHandlerPool_RequestHandlerAvgIdlePercent           Meter           OneMin
uteRate 1.00 0.3 LTE|
|KafkaServer_BrokerState                                        Gauge           Value
3.00 3 NEQ|
|BrokerTopicMetrics_BytesRejectedPerSec                         Meter           OneMinu
teRate 0.00 1 GTE|
|BrokerTopicMetrics_FailedFetchRequestsPerSec                   Meter
OneMinuteRate 0.00 1 GTE|
|BrokerTopicMetrics_FailedProduceRequestsPerSec                 Meter
OneMinuteRate 0.00 1 GTE|
|Fetch                                                          Gauge           queue-s
ze 0.00 1 GTE|
|Produce                                                        Gauge           queue-s
ze 0.00 1 GTE| --------------------------------------------------------------------------------------- --------------------------------------------------------------- --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|Log
```

|

```
|ObjectName                                                     Type            Attribu
eName Value Threshold Op| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|LogCleanerManager_time-since-last-run-ms                       Gauge           Value
6668.00 600000 GTE| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
```

```
--------------------------------------------------------------- --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|Controller
```

|

```
|ObjectName                                                     Type            Attribu
eName Value Threshold Op| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|KafkaController_ActiveControllerCount                          Gauge           Value
1.00 1 NEQ|
|ControllerStats_LeaderElectionRateAndTimeMs                    Timer
75thPercentile 16.51 null null|
|ControllerStats_LeaderElectionRateAndTimeMs                    Timer
98thPercentile 16.51 null null|
|ControllerStats_LeaderElectionRateAndTimeMs                    Timer
OneMinuteRate 0.00 0.1 GTE|
|ControllerStats_LeaderElectionRateAndTimeMs                    Timer
50thPercentile 16.51 null null| --------------------------------------------------------------------------------------- --------------------------------------------------------------- --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|JVM
```

|

```
|ObjectName                                                     Type            Attribu
eName Value Threshold Op| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|Threading                                                      Gauge           DeadLoc
0.00 0 NEQ|
|GarbageCollector_G1 Young Generation                           Meter           Collect
ionTime 19201.00 null null|
|GarbageCollector_G1 Young Generation                           Meter           Collect
ionCount 124.00 null null|
|GarbageCollector_G1 Old Generation                             Meter           Collect
ionTime 0.00 null null|
|GarbageCollector_G1 Old Generation                             Meter           Collect
ionCount 0.00 null null|
|Memory                                                         Meter           HeapMem
ryUsage_Used_Mb 334.74 null null|
|Memory                                                         Meter           HeapMem
ryUsage_Max_Mb 204.72 null null|
|Memory                                                         Meter           NonHeap
emoryUsage_Used_Mb 80.63 null null| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
```

|   | Note To query the information about other metrics, run the java -jar kafka- pkgs/KafkaMetricChecker.jar command. |   |   |
|---|---|---|---|
|   |   | java -jar kafka- |   |
|   | pkgs/KafkaMetricChecker.jar |   |   |

#### 3.2.2 View log information

This topic describes how to view log information for ApsaraMQ for Kafka. You can also use the **Log Query** feature in **Log Center** on the Apsara Uni-manager Operations Console to query and analyze Kafka logs. For more information, see **Apsara Uni-**

**manager Operations Console User Guide > Platform O&M > Log Center > Log**

**Query**.
The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `cd /home/admin/logs/alikafka` command to switch to the log directory.
5. Run the **ls** command to list the log files.

```
commercial.log controller.log kafka-authorizer.log kafka-request.log kafka-reques t.log.1 log-cleaner.log metrics.log network.log server.log state-change.log unk nown.log
```

6. Run the `cat <filename>` command to view the information in a specific log file.

#### 3.2.3 Query the status of a topic

This topic describes how to query the status of a topic. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-topics.sh --describe --bootstrap-server
```

`hostname -i`:9092 --topic <topic> command to query the status of a topic.

| test | , run the |
|---|---|

For example, if the name of a topic is `test` , run the `sh`

```
/home/admin/KafkaProxy/bin/kafka-topics.sh --describe --bootstrap-server `hostname -
```

i`:9092 --topic test command.

```
Topic:test PartitionCount:12 ReplicationFactor:3 Configs:min.insync.replicas=1,flush.ms=1000,segment.bytes=268435456,retention.ms=864000 ,flush.messages=10000,max.message.bytes=10000000,unclean.leader.election.enable=false
        Topic: test     Partition: 0    Leader: 1003    Replicas: 1003,1002,1001
Isr: 1001,1003,1002
        Topic: test     Partition: 1    Leader: 1002    Replicas: 1002,1001,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 2    Leader: 1001    Replicas: 1001,1003,1002
Isr: 1003,1002,1001
        Topic: test     Partition: 3    Leader: 1003    Replicas: 1003,1001,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 4    Leader: 1002    Replicas: 1002,1003,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 5    Leader: 1001    Replicas: 1001,1002,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 6    Leader: 1003    Replicas: 1003,1002,1001
Isr: 1001,1003,1002
        Topic: test     Partition: 7    Leader: 1002    Replicas: 1002,1001,1003
Isr: 1003,1002,1001
        Topic: test     Partition: 8    Leader: 1001    Replicas: 1001,1003,1002
Isr: 1003,1002,1001
        Topic: test     Partition: 9    Leader: 1003    Replicas: 1003,1001,1002
Isr: 1001,1003,1002
        Topic: test     Partition: 10   Leader: 1002    Replicas: 1002,1003,1001
Isr: 1003,1002,1001
        Topic: test     Partition: 11   Leader: 1001    Replicas: 1001,1002,1003
Isr: 1003,1002,1001
```

#### 3.2.4 Query the status of a consumer group

This topic describes how to query the status of a consumer group. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.

```
4. Run the  sh /home/admin/KafkaProxy/bin/kafka-consumer-groups.sh --bootstrap-server
```

`hostname -i`:9092 --group <group> --describe command to query the status of a consumer group.

| CID-test | , run the |
|---|---|

For example, if the name of a consumer group is `CID-test` , run the `sh`

```
/home/admin/KafkaProxy/bin/kafka-consumer-groups.sh --bootstrap-server `hostname -
```

i`:9092 --group CID-test --describe command.

```
Consumer group 'CID-test' has no active members. TOPIC PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG CONSUMER-ID HOST CLIENT-ID test 6 14198 16644 2446 -
-               -
test 11 14307 16729 2422 -
-               -
test 10 14228 16601 2373 -
-               -
test 0 14335 16732 2397 -
-               -
test 7 14137 16595 2458 -
-               -
test 5 14334 16762 2428 -
-               -
test 8 14379 16809 2430 -
-               -
test 1 14209 16703 2494 -
-               -
test 4 14418 16790 2372 -
-               -
test 9 14352 16748 2396 -
-               -
test 3 14212 16661 2449 -
-               -
test 2 14161 16509 2348 -
-               -
```

#### 3.2.5 Query the data of ZooKeeper

This topic describes how to query the data of ZooKeeper. The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

By default, the ZooKeeper root directory of ApsaraMQ for Kafka is <zkHost:zkPort>/kafkaprivate-clusters/cluster-private-paas-default.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `sh /home/admin/kafka-tools/metadata.sh endPoint` command to query the
endpoint of ZooKeeper.

```
zookeeper.connect=10.XX.XX.XXX:2188,10.XX.XX.XXX:2188,10.XX.XX.XXX:2188/kafka-private -clusters/cluster-private-paas-default
```

5. Run the `sh /home/admin/zookeeper-3.4.8/bin/zkCli.sh -server <ZKConnect>` command to
connect to ZooKeeper.

```
Connecting to 10.XX.XX.XXX:2188 2020-09-01 11:31:49,580 [myid:] - INFO [main:Environment@100] - Client environment:zookeeper.version=3.4.8--1, built on 02/06/2016 03:18 GMT 2020-09-01 11:31:49,585 [myid:] - INFO [main:Environment@100] - Client environment:host.name=alibaba-kafka-cluster-private-paas-default-2.kafka-alibaba-kafk a-cluster-private-paas-default-hs.default.svc.cluster.local 2020-09-01 11:31:49,585 [myid:] - INFO [main:Environment@100] - Client environment:java.version=1.8.0_102 2020-09-01 11:31:49,588 [myid:] - INFO [main:Environment@100] - Client environment:java.vendor=Alibaba 2020-09-01 11:31:49,588 [myid:] - INFO [main:Environment@100] - Client environment:java.home=/opt/taobao/java/jre 2020-09-01 11:31:49,588 [myid:] - INFO [main:Environment@100] - Client environment:java.class.path=/home/admin/zookeeper- 3.4.8/bin/../build/classes:/home/admin/zookeeper- 3.4.8/bin/../build/lib/*.jar:/home/admin/zookeeper-3.4.8/bin/../lib/slf4j-log4j12-1.6 .1.jar:/home/admin/zookeeper-3.4.8/bin/../lib/slf4j-api- 1.6.1.jar:/home/admin/zookeeper-3.4.8/bin/../lib/netty- 3.7.0.Final.jar:/home/admin/zookeeper-3.4.8/bin/../lib/log4j- 1.2.16.jar:/home/admin/zookeeper-3.4.8/bin/../lib/jline- 0.9.94.jar:/home/admin/zookeeper-3.4.8/bin/../zookeeper- 3.4.8.jar:/home/admin/zookeeper- 3.4.8/bin/../src/java/lib/*.jar:/home/admin/zookeeper-3.4.8/bin/../conf: 2020-09-01 11:31:49,588 [myid:] - INFO [main:Environment@100] - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/
```

`b`

```
2020-09-01 11:31:49,588 [myid:] - INFO [main:Environment@100] - Client environment:java.io.tmpdir=/tmp 2020-09-01 11:31:49,588 [myid:] - INFO [main:Environment@100] - Client environment:java.compiler=<NA> 2020-09-01 11:31:49,589 [myid:] - INFO [main:Environment@100] - Client environment:os.name=Linux 2020-09-01 11:31:49,589 [myid:] - INFO [main:Environment@100] - Client environment:os.arch=amd64 2020-09-01 11:31:49,589 [myid:] - INFO [main:Environment@100] - Client environment:os.version=3.10.0-327.ali2014.alios7.x86_64 2020-09-01 11:31:49,589 [myid:] - INFO [main:Environment@100] - Client environment:user.name=admin 2020-09-01 11:31:49,589 [myid:] - INFO [main:Environment@100] - Client environment:user.home=/home/admin 2020-09-01 11:31:49,589 [myid:] - INFO [main:Environment@100] - Client environment:user.dir=/home/admin 2020-09-01 11:31:49,590 [myid:] - INFO [main:ZooKeeper@438] - Initiating client conn ection, connectString=10.XX.XX.XXX:2188 sessionTimeout=30000 watcher=org.apache.zookeeper.ZooKeeperMain$MyWatcher@3eb07fd3 Welcome to ZooKeeper! 2020-09-01 11:31:49,619 [myid:] - INFO [main-
```

`,` `y`

```
SendThread(10.XX.XX.XXX:2188):ClientCnxn$SendThread@1032] - Opening socket connection to server 10.XX.XX.XXX/10.XX.XX.XXX:2188. Will not attemptto authenticate using SASL (unknown error) JLine support is enabled 2020-09-01 11:31:49,718 [myid:] - INFO [main- SendThread(10.XX.XX.XXX:2188):ClientCnxn$SendThread@876] - Socket connection establis hed to 10.XX.XX.XXX/10.XX.XX.XXX:2188, initiating session 2020-09-01 11:31:49,725 [myid:] - INFO [main- SendThread(10.XX.XX.XXX:2188):ClientCnxn$SendThread@1299] - Session establishment com plete on server 10.XX.XX.XXX/10.XX.XX.XXX:2188, sessionid =0x300aaa7e6cf00ba, negotia ted timeout = 30000 WATCHER:: WatchedEvent state:SyncConnected type:None path:null
```

6. Run the `ls /` command to query the nodes of ZooKeeper.

```
[kafka-private-clusters, zookeeper]
```

7. Run the `get /<zk node>` command to query the data of a ZooKeeper node.
For example, if the name of a ZooKeeper node is zookeeper, run the `get /zookeeper` command.

```
cZxid = 0x0 ctime = Thu Jan 01 08:00:00 CST 1970 mZxid = 0x0 mtime = Thu Jan 01 08:00:00 CST 1970 pZxid = 0x0 cversion = -1 dataVersion = 0 aclVersion = 0 ephemeralOwner = 0x0 dataLength = 0 numChildren = 1
```

**What to do next**

After you query the data of ZooKeeper, run the **quit** command to exit ZooKeeper.

```
Quitting... 2020-09-01 11:45:05,123 [myid:] - INFO [main:ZooKeeper@684] - Session: 0x300axxxx0ba c losed 2020-09-01 11:45:05,125 [myid:] - INFO [main-EventThread:ClientCnxn$EventThread@519] - EventThread shut down for session: 0x300axxxx0ba
```

#### 3.2.6 Update the configurations of a topic

This topic describes how to update the configurations of a topic. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `sh /home/admin/kafka-tools/metadata.sh endPoint` command to query the
endpoint of ZooKeeper.

```
zookeeper.connect=10.XX.XX.XXX:2188,10.XX.XX.XXX:2188,10.XX.XX.XXX:2188/kafka-private -clusters/cluster-private-paas-default
5. Run the  sh kafka-configs.sh -zookeeper <zkconnect> --describe --entity-name <topic> --
```

`entity-type topics` command to query the configuration of a topic.

```
6. Run the  sh kafka-configs.sh -zookeeper <zkconnect> --alter --add-config <config kv> --
```

`entity-name <topic> --entity-type topic` command to update the configurations of a topic. For example, to change the message retention period of the topic whose name is `test` to 37,000 ms, run the `sh kafka-configs.sh -zookeeper <zkconnect> --alter --add-config`

```
retention.ms=37000 --entity-name test --entity-type topics command.
```

#### 3.2.7 FAQ

This topic lists common issues with process operations and maintenance.

**Precautions**

> **Warning:** The following operations are high-risk. Perform them only with the assistance of operations personnel.

**Restarting a Pod's Message Queue for Apache Kafka process**

By default, the Kafka process starts asynchronously and uses a liveness check to monitor its health.
1. Modify the /home/admin/kafka-tool/check-health.sh script to ensure the liveness check
succeeds.
2. Restart the process.
i. Use the **kill** command to terminate the Kafka process. ii. Modify start_kafka.sh. iii. Run the command `sh start_kafka.sh` to restart the Message Queue for Apache Kafka process.
3. Restore the health check, and then restart the Pod.

**Message Queue for Apache Kafka process log anomalies**

**require a restart**

To restart the process, terminate it by using one of the following methods: Use a script to terminate the process. Run the command `kubectl exec <pod> /bin/sh -c main /home/admin/KafkaProxy/bin/kafka-` `server-stop.sh` to terminate the process. Use commands to terminate the process. i. Run the command `kubectl exec -it <pod name> /bin/bash` to enter the Pod. ii. Run the command `sudo su admin` to switch to the administrator user. iii. Run the `jps` command to display all current Java processes. iv. Run the `kill <pid>` command to terminate the process.

**Troubleshoot ERROR exceptions in logs**

The service logs are located in the /home/admin/logs/alikafka directory. The most important log files are server.log and state-change.log. Take an exception in state-change.log as an example. The state-change.log file records information about partition states, and exceptions are typically related to the controller or partition state transitions. Investigate the topic mentioned in the exception.
1. Run the command `cd /home/admin/KafkaProxy` to switch to the /home/admin/KafkaProxy
directory.
2. Run the command ./bin/kafka-topics.sh --describe --bootstrap-server `hostname -
i`:9092 --topic {topic} to view the topic information.

### 3.3 Other maintenance operations

#### 3.3.1 Evaluate the capacity of a cluster

This topic describes how to evaluate the capacity of an ApsaraMQ for Kafka cluster, including disk usage and peak traffic. The information about the master node in ApsaraMQ for Kafka is obtained.

**Query the information about a cluster**

In this example, the `alibaba-kafka-cluster-private-paas-default-0` cluster is used. You must perform the following operations on three nodes.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Query the information about a node.
i. Run the `tsar --traffic -n 7 > traffic_day_7_hostname -i.txt` command. ii. Run the `tsar --cpu --mem -n 7 > cpu_mem_day_7_hostname -i.txt` command. iii. Run the `exit` command to exit the pod.

```
iv. Run the kubectl cp alibaba-kafka-cluster-private-paas-default-0:/home/admin/{File
```

`name}.txt {File name}.txt` command.
5. Query the disk usage.
i. Run the `kubectl exec -it <pod> bash` command to access the pod in which ApsaraMQ for Kafka is deployed.

|   | alibaba-kafka-cluster-private-paas-default-0 |
|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |

command. ii. Run the `sudo su admin` command to switch to the administrator account. iii. Run the `df -h /alidata1/` command to query the disk usage.
6. Check the traffic information of brokers on Grafana monitoring dashboards.
For more information, see the **View dashboards** topic in ApsaraMQ for Kafka **User Guide**.

**Evaluate the capacity**

Evaluate the capacity based on the queried node information.
1. Evaluate the disk capacity based on the message retention period and disk usage.
2. Evaluate whether the nodes encounter bottlenecks based on the queried peak duration and
peak traffic.

## 4 Routine inspection

### 4.1 Inspect the status of pods

This topic describes how to inspect the status of pods. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pods -o wide | grep kafka command to query a list of pods in
ApsaraMQ for Kafka.

```
alibaba-kafka-cluster-multi-alibaba-kafka-0 2/2 Running 1 24h 10.**.**.** a36******4.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-1 2/2 Running 4 24h 10.**.**.** a36******8.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-2 2/2 Running 0 24h 10.**.**.** a36******8.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-private-paas-default-0 2/2 Running 3 47h 10.**.**.** a36******5.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-private-paas-default-1 2/2 Running 2 47h 10.**.**.** a36******3.cloud.b**.am****** <none> <none> alibaba-kafka-cluster-private-paas-default-2 2/2 Running 3 47h 10.**.**.** a36******6.cloud.b**.am****** <none> <none> alibaba-kafka-console-6dc*****59-bqvn6 1/1 Running 0 26h 10.**.**.** a36*****3.cloud.b**.am****** <none> <none> alibaba-kafka-operator-6b***** 9cc-s8s49 1/1 Running 0 47h 10.**.**.** a36******3.cloud.b**.am****** <none> <none>
```

> **Note:** In normal cases, pods are in the Running state.

3. Run the `kubectl describe pod <pod>` command to query the information about a pod.

| example, if the name of a pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl describe pod alibaba-kafka-cluster-private-paas-default-0 |   |   |
|   |   | command |

```
Name: alibaba-kafka-cluster-private-paas-default-0 Namespace: default Priority: 0 PriorityClassName: <none> Node: a36b10005.cloud.b10.amtest11/10.**.**.*** Start Time: Sun, 30 Aug 2020 11:58:35 +0300 Labels: app=alibaba-kafka-broker
                    app.kubernetes.io/instance=alibaba-kafka
                    app.kubernetes.io/managed-by=Tiller
appname=alibaba-kafka-cluster-private-paas-default
```

```json
                    app.name=alibaba-kafka-cluster-private-paas-default
                    controller-revision-hash=alibaba-kafka-cluster-private-paas-defaul
t-66******8b
                    helm.sh/chart=alibaba-kafka-0.0.6-d460bef
                    kafka.env=private-pass
                    statefulset.kubernetes.io/pod-name=alibaba-kafka-cluster-private-p
aas-default-0 Annotations: networking.alibaba.com/ip:
                      {"Address":
{"IP":"10.**.**.***","Mask":"///8AA=="},"Gateway":"10.**.**.***","NetID":11,"Subnet":"s net-cn-*******-env**-amtest*****-a-1",... Status: Running IP: 10.**.**.*** Controlled By: StatefulSet/alibaba-kafka-cluster-private-paas-default Containers:
  main:
    Container ID:
docker://3fa64fb320b9b7898ea************fdbde08f04b7e0fb1ea1d699ecce1c4fe
    Image:          cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkabroker:efbede************66ce7753ac11e605d943e57af0ebac1f336567ad7fc160
    Image ID:       docker-pullable://cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkabroker@sha256:66726a9c************b13e4e3a632383d3f1378c5324dbbd05b0a6d45aa631
    Ports:          9092/TCP, 9093/TCP, 9592/TCP, 8081/TCP
    Host Ports:     0/TCP, 0/TCP, 0/TCP, 0/TCP
    State:          Running
      Started:      Sun, 30 Aug 2020 11:58:52 +0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  5Gi
    Requests:
      cpu:     2
      memory:  4Gi
    Liveness:  exec [/home/admin/kafka-tools/check-health.sh] delay=900s timeout=180s
period=15s #success=1 #failure=3
    Environment:
      MOCK_DEADLOCK:                            false
      proxy_security_protocol_sasl_ssl:         true
      middleware_zk_port:                       2188
      sasl_ssl_requestip_mode:                  local
      vpc_mode_vpc_id:                          vpc-rt1k708pzc***
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-default
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.**.**.***,10.**.**.***,10.**.**.***
      vpcmodedeleteserviceenable:           false
```

```
pc_ode_deete_se ce_eabe: ase
      vpc_mode_vsw_id:                          vsw-rt1fjm1djg***
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.***.***.**:8080,192.***.***.**:8080,192.***.***.**:8080
      vips_9093:                                UNKNOWN_VARIABLE
      async_start:                              true
      enable_prometheus_javaagent:              true
      cluster_env:                              private-pass
      enable_auto_updatevip:                    true
      aliyun_logs_kafka:                        /home/admin/logs/alikafka/*.log
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              4294967296 (requests.memory)
      request_cpu:                              2 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              4294967296 (requests.memory)
      request_cpu:                              2 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      proxy_cluster_name:                       private-paas-default
    Mounts:
      /alidata1 from kafka-datadir (rw)
      /home/admin/logs from volume-0 (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-k2stw (ro)
  agent:
    Container ID:
docker://57d3d96ad8775f*********d34fdf616b598b927417597883d92e9287c09c8
    Image:          cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkaagent:4d43d896************cb89df8184f0f18c517df3544a72a00d8de71b497eee
    Image ID:       docker-pullable://cn-*******-env**-d01-
reg.docker.intra.env***.shuguang.com/private-paas/alibaba-kafkaagent@sha256:43c*********ab8361114070f8ca367ebe44bd959210c54ee28f4cd775a97f
    Port:           9089/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 31 Aug 2020 09:33:06 +0300
    Last State:     Terminated
      Reason:       OOMKilled
      Exit Code:    143
      Started:      Sun, 30 Aug 2020 11:59:08 +0300
      Finished:     Mon, 31 Aug 2020 09:32:49 +0300
    Ready:          True
    Restart Count:  1
    Limits:
      cpu:     1
      memory:  1Gi
    Requests:
      cpu:     1
      memory:  512Mi
    Liveness:  exec [/home/admin/agent/bin/check.sh] delay=300s timeout=180s
```

```
period=15s #success=1 #failure=3
    Environment:
      MOCK_DEADLOCK:                            false
      proxy_security_protocol_sasl_ssl:         true
      middleware_zk_port:                       2188
      sasl_ssl_requestip_mode:                  local
      vpc_mode_vpc_id:                          vpc-rt1k708pzc13i9*******
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-default
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.**.**.***,10.**.**.***,10.**.**.***
      vpc_mode_delete_service_enable:           false
      vpc_mode_vsw_id:                          vsw-rt1fjm1djgpia********
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.***.***.**:8080,192.***.***.**:8080,192.***.***.**:8080
      vips_9093:                                UNKNOWN_VARIABLE
      async_start:                              true
      enable_prometheus_javaagent:              true
      cluster_env:                              private-pass
      enable_auto_updatevip:                    true
      aliyun_logs_kafka:                        /home/admin/logs/alikafka/*.log
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              536870912 (requests.memory)
      request_cpu:                              1 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      replicas:                                 3
      node_name:                                 (v1:spec.nodeName)
      request_mem:                              536870912 (requests.memory)
      request_cpu:                              1 (requests.cpu)
      pod_ip:                                    (v1:status.podIP)
      proxy_cluster_name:                       private-paas-default
    Mounts:
      /home/admin/agent/logs from volume-1 (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-k2stw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kafka-datadir:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the
same namespace)
```

```
    ClaimName:  kafka-datadir-alibaba-kafka-cluster-private-paas-default-0
    ReadOnly:   false
  volume-0:
    Type:          HostPath (bare host directory volume)
    Path:          /var/lib/docker/logs/alibaba-kafka/home/admin/logs
    HostPathType:  DirectoryOrCreate
  volume-1:
    Type:          HostPath (bare host directory volume)
    Path:          /var/lib/docker/logs/alibaba-kafka/home/admin/agent/logs
    HostPathType:  DirectoryOrCreate
  default-token-k2stw:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-k2stw
    Optional:    false
QoS Class: Burstable Node-Selectors: networking.alibaba.com/asw=asw-cn-*******-en***-amtest*****-a Tolerations: node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events: <none>
```

> **Note:** In most cases, the value of the Events parameter is <none>.

### 4.2 Inspect the resource availability

**availability**

This topic describes how to inspect the disk usage, abnormal metrics, and error logs. The information about the master node in ApsaraMQ for Kafka is obtained.

**Inspect the disk usage**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `df -h /alidata1/` command to query the disk usage.

```
Filesystem Size Used Avail Use% Mounted on /dev/mapper/vg_apsara_paas-yoda--0c861b0b--e777--11ea--bf33--6805caa954d0
                       89G  191M   88G   1% /alidata1
```

> **Note:** In most cases, the disk usage is lower than 90%.

**Inspect abnormal metrics**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

|   | alibaba-kafka-cluster-private-paas-default-0 |
|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |

3. Run the `sudo su admin` command to switch to the administrator account.

| java -jar /home/admin/kafka-pkgs/KafkaMetricChecker.jar broker -f |   |
|---|---|
|   | command to query the information about metrics. |

```
--------------------------------------------------------------------------------------- ---------------------------------------------------------------
|Controller
```

|

```
|ObjectName                                                     Type            Attribu
eName Value Threshold Op| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
|KafkaController_ActiveControllerCount                          Gauge           Value
0.00 1 NEQ| --------------------------------------------------------------------------------------- ---------------------------------------------------------------
```

**Inspect error logs**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

|   | alibaba-kafka-cluster-private-paas-default-0 |
|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `java -jar /home/admin/kafka-pkgs/KafkaLogChecker.jar log -g ERROR` command
to query the information about error logs. The returned result is empty.

**References**

For more information about how to check other monitored physical resources of pods on Grafana monitoring dashboards, see the **View dashboards** topic in ApsaraMQ for Kafka
**User Guide**.

### 4.3 Inspect the service availability

This topic describes how to inspect the service availability.

**q**

The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `cd /home/admin/KafkaProxy/bin` command to switch to the bin directory.

```
5. Run the  sh kafka-topics.sh --create --bootstrap-server <pod ip>:9092 --topic test --
```

`replication-factor 3 --partitions 12` command to create a topic. For more information about how to obtain the endpoint of ApsaraMQ for Kafka, see the
**Obtain an instance endpoint** topic in **ApsaraMQ for Kafka User Guide**.
6. Run the `cd /home/admin/kafka-pkgs` command to switch to the kafka-pkgs directory.
7. Run the `java -jar KafkaChecker.jar send -s <pod ip>:9092` command to send a
message.
8. Run the `cd /home/admin/KafkaProxy/bin` command to switch to the bin directory.

```
9. Run the  sh kafka-console-consumer.sh --from-beginning --topic test --group CID_test --
```

`bootstrap-server <pod ip>:9092` command to consume the messages.

### 4.4 Inspect a physical server after a restart

**a restart**

This topic describes how to inspect a physical server after a restart. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Inspect the status of pods.
For more information, see Inspect the status of pods.
2. Inspect the service availability.
For more information, see Inspect the service availability.
3. Connect to the master node in ApsaraMQ for Kafka.
4. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

5. Run the cat /alidata1/kafka/kafka-logs/meta.properties | grep broker command to
query the data of the meta.properties file.

```
broker.id=1001
```

> **Note:** After a physical server is restarted, ApsaraMQ for Kafka registers three brokers in pods based on the broker IDs in the meta.properties file. In normal cases, the broker IDs 1001, 1002, and 1003 are returned.
