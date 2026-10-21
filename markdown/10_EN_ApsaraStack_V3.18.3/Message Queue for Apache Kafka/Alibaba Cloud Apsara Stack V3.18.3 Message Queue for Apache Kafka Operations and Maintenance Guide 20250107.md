---
title: "Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka Operations and Maintenance Guide 20250107"
product_version: "V3.18.3"
doc_version: "20250107"
pdf_pages: 35
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka Operations and Maintenance Guide 20250107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97kafka/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Message%20Queue%20for%20Apache%20Kafka%20Operations%20and%20Maintenance%20Guide%2020250107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Message Queue for Apache Kafka Operations and Maintenance Guide 20250107

## Table of Contents

- 1 Overview
- 2 Routine maintenance
  - 2.1 Pod maintenance
    - 2.1.1 Query a list of pods
    - 2.1.2 Query the information about a pod
    - 2.1.3 Query the logs of a pod
    - 2.1.4 Restart a pod
    - 2.1.5 Query the information about PVs and PVCs
    - 2.1.6 FAQ
  - 2.2 Process maintenance
    - 2.2.1 Query the metric information of brokers
    - 2.2.2 Query logs
    - 2.2.3 Query the status of a topic
    - 2.2.4 Query the status of a consumer group
    - 2.2.5 Query the data of ZooKeeper
    - 2.2.6 Update the configurations of a topic
    - 2.2.7 FAQ
  - 2.3 Other maintenance operations
    - 2.3.1 Evaluate the capacity of a cluster
- 3 Routine inspection
  - 3.1 Inspect the status of pods
  - 3.2 Inspect the resource availability
  - 3.3 Inspect the service availability
  - 3.4 Inspect a physical server after a restart

## 1 Overview

You must perform various maintenance operations on ApsaraMQ for Kafka to ensure its stability and availability. ApsaraMQ for Kafka supports the following maintenance operations:

## 2 Routine maintenance

### 2.1 Pod maintenance

#### 2.1.1 Query a list of pods

This topic describes how to query a list of pods in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pod -o wide| grep alibaba-kafka command to query a list of pods.

```
alibaba-kafka-autotest-mp524 0/1 Completed 0 5h14m 10.XX.X.XX a36b10008.cloud.b10.amtest11 <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-0 2/2 Running 0 35m 10.XX.XX.XX a36b10204.cloud.b12.amtest11 <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-1 2/2 Running 0 35m 10.XX.XX.XX a36b10208.cloud.b12.amtest11 <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-2 2/2 Running 0 36m 10.XX.XX.XX a36b10008.cloud.b10.amtest11 <none> <none> alibaba-kafka-cluster-private-paas-default-0 2/2 Running 1 23h 10.XX.XX.XXX a36b10005.cloud.b10.amtest11 <none> <none> alibaba-kafka-cluster-private-paas-default-1 2/2 Running 0 23h 10.XX.XX.XXX a36b10203.cloud.b12.amtest11 <none> <none> alibaba-kafka-cluster-private-paas-default-2 2/2 Running 1 23h 10.XX.XX.XXX a36b10016.cloud.b10.amtest11 <none> <none> alibaba-kafka-console-6dcf5f9b59-bqvn6 1/1 Running 0 172m 10.XX.XX.XX a36b10203.cloud.b12.amtest11 <none> <none> alibaba-kafka-operator-6b9dbb49cc-s8s49 1/1 Running 0 23h 10.XX.XX.XXX a36b10203.cloud.b12.amtest11 <none> <none>
```

> **Note:** In most cases, the kafka-cluster cluster has three pods, the operator cluster has only one pod, and the manager cluster has one or two pods.
> The number of pods varies based on the deployment environment.
> In normal cases, pods are in the Running state.

#### 2.1.2 Query the information about a pod

If an exception occurs during the deployment of a pod, you can query the information about the pod in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl describe pod <pod>` command to query the information about a pod.

| example, if the name of a pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl describe pod alibaba-kafka-cluster-private-paas-default-0 |   |   |
|   |   | command |

```json
Name: alibaba-kafka-cluster-private-paas-default-0 Namespace: default Priority: 0 PriorityClassName: <none> Node: a36b10005.cloud.b10.amtest11/10.XX.XX.XXX Start Time: Sun, 30 Aug 2020 11:58:35 +0300 Labels: app=alibaba-kafka-broker
                    app.kubernetes.io/instance=alibaba-kafka
                    app.kubernetes.io/managed-by=Tiller
                    app.name=alibaba-kafka-cluster-private-paas-default
                    controller-revision-hash=alibaba-kafka-cluster-private-paas-defaul
t-66ff8bb98b
                    helm.sh/chart=alibaba-kafka-0.0.6-d460bef
                    kafka.env=private-pass
                    statefulset.kubernetes.io/pod-name=alibaba-kafka-cluster-private-p
aas-default-0 Annotations: networking.alibaba.com/ip:
                      {"Address":
{"IP":"10.XX.XX.XXX","Mask":"///8AA=="},"Gateway":"10.XX.XX.XXX","NetID":11,"Subnet":"s net-cn-qingdao-env17-amtest11001-a-1",... Status: Running IP: 10.XX.XX.XXX Controlled By: StatefulSet/alibaba-kafka-cluster-private-paas-default Containers:
  main:
    Container ID:
docker://3fa64fb320b9b7898ea6b008f08ed93fdbde08f04b7e0fb1ea1d699ecce1c4fe
    Image:          cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkabroker:efbede0b9a06ef5b8966ce7753ac11e605d943e57af0ebac1f336567ad7fc160
    Image ID:       docker-pullable://cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkabroker@sha256:66726a9c09e6c3cf6420b13e4e3a632383d3f1378c5324dbbd05b0a6d45aa631
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
      vpc_mode_vpc_id:                          vpc-rt1k708pzcXXX
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-default
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.XX.XX.XXX,10.XX.XX.XXX,10.XX.XX.XXX
      vpc_mode_delete_service_enable:           false
      vpc_mode_vsw_id:                          vsw-rt1fjm1djgXXX
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080
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
docker://57d3d96ad8775f6c956f68d70d34fdf616b598b927417597883d92e9287c09c8
    Image:          cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkaagent:4d43d896d38f1a8d00a3cb89df8184f0f18c517df3544a72a00d8de71b497eee
    Image ID:       docker-pullable://cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkaagent@sha256:43c876cc713aecab8361114070f8ca367ebe44bd959210c54ee28f4cd775a97f
```

```
agent@sha256:43c876cc713aecab8361114070f8ca367ebe44bd959210c54ee28f4cd775a97f
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
      vpc_mode_vpc_id:                          vpc-rt1k708pzc13i9gpzh22v
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-default
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.XX.XX.XXX,10.XX.XX.XXX,10.XX.XX.XXX
      vpc_mode_delete_service_enable:           false
      vpc_mode_vsw_id:                          vsw-rt1fjm1djgpia5suslag6
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080
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
QoS Class: Burstable Node-Selectors: networking.alibaba.com/asw=asw-cn-qingdao-env17-amtest11001-a Tolerations: node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events: <none>
```

> **Note:** In most cases, the value of the Events parameter is <none>.

#### 2.1.3 Query the logs of a pod

This topic describes how to query the logs of a pod in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl logs <pod>` command to query the logs of a pod.

|   | alibaba-kafka-operator-6b9dbb49cc-s8s49 |
|---|---|
| kubectl logs alibaba-kafka-operator-6b9dbb49cc-s8s49 |   |

```json
{"level":"info","ts":1598777607.4786668,"logger":"controller_kafka","msg":"Reconcile Kafka......","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-priv ate-release-alibaba-kafka","RequestID":1598777607478639249} {"level":"info","ts":1598777607.4789321,"logger":"controller_kafka","msg":"reconcileClu erStatus expire size:3, current size:3","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-private-r elease-alibaba-kafka","RequestID":1598777607478639249} {"level":"info","ts":1598777608.3835506,"logger":"controller_kafka","msg":"Reconcile Kafka......","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-priv ate-release-alibaba-kafka","RequestID":1598777608383517127} {"level":"info","ts":1598777608.3838317,"logger":"controller_kafka","msg":"reconcileClu erStatus expire size:3, current size:3","Request.Namespace":"default","Request.Name":"alibaba-kafka-cluster-private-r elease-alibaba-kafka","RequestID":1598777608383517127}
```

#### 2.1.4 Restart a pod

This topic describes how to restart a pod in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.

**Background information**

Pods cannot be directly restarted. If the state of a pod is abnormal, we recommend that you restart the process to resolve the issue. If the state of the pod is still abnormal and cannot be recovered after the process is restarted, you can delete the pod to resolve the issue.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl delete pod <pod>` command to delete a pod.

| example, if the name of a pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl delete pod alibaba-kafka-cluster-private-paas-default-0 |   |   |
|   |   | command. |

#### 2.1.5 Query the information about PVs and PVCs

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
local-pv-441b2d75 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-0 fast-disks 30d local-pv-4ead5521 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-0 fast-disks 26d local-pv-75c677f4 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-2 fast-disks 24d local-pv-8edeaa79 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-1 fast-disks 17d local-pv-8f2d4b7c 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 fast-disks 17d local-pv-bcf4f008 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-1 fast-disks 17d local-pv-bf995f4d 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-1 fast-disks 24d local-pv-ca97969f 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-2 fast-disks 34d local-pv-cd53c348 7393Gi RWO Delete Released default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba-kaf ka-2 fast-disks 34d pvc-3066e824-eb37-11ea-bf33-6805caa954d0 1Mi RWX Delete Bound kafka-autotest-default-cell/lxcfs-pvc lxcfs-sc 6h29m yoda-0409d39d-eb52-11ea-bf33-6805caa954d0 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-2 yoda-lvm 3h17m yoda-0c861b0b-e777-11ea-bf33-6805caa954d0 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-private-paas-default-0 yoda-lvm 5d1h yoda-5a840f48-e777-11ea-bf33-6805caa954d0 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-private-paas-default-1 yoda-lvm 5d1h yoda-b584d7ee-e777-11ea-bf33-6805caa954d0 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-private-paas-default-2 yoda-lvm 5d yoda-d3b992bb-eb51-11ea-bf33-6805caa954d0 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 yoda-lvm 3h18m yoda-edf9999c-eb51-11ea-bf33-6805caa954d0 90Gi RWO Delete Bound default/kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-1 yoda-lvm 3h18m
```

3. Run the `kubectl describe pv <pv>` command to query the information about a PV.

| kubectl describe pv local-pv-441b2d75 |   |   |
|---|---|---|
| whose name is | local-pv-441b2d75 | . |

```
Name: local-pv-441b2d75 Labels: <none> Annotations: pv.kubernetes.io/bound-by-controller: yes
                   pv.kubernetes.io/provisioned-by: local-volume-provisioner-a36b10204
.cloud.b12.amtest11-475232f9-cd51-11ea-bf33-6805caa954d0 Finalizers: [kubernetes.io/pv-protection] StorageClass: fast-disks Status: Released Claim: default/kafka-datadir-alibaba-kafka-cluster-private-release-alibaba -kafka-0 Reclaim Policy: Delete Access Modes: RWO VolumeMode: Filesystem Capacity: 7393Gi Node Affinity:
  Required Terms:
    Term 0:        kubernetes.io/hostname in [a36b10204.cloud.b12.amtest11]
Message: Source:
    Type:  LocalVolume (a persistent volume backed by local storage on a node)
    Path:  /var/lib/docker/data/disk/disk7
Events: <none>
```

**Query the information about PVCs**

1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pvc | grep kafka command to query the information about all PVCs.

```
kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 Bound yoda-d3b992bb-e b51-11ea-bf33-6805caa954d0 90Gi RWO yoda-lvm 3h29m kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-1 Bound yoda-edf9999c-e b51-11ea-bf33-6805caa954d0 90Gi RWO yoda-lvm 3h28m kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-2 Bound yoda-0409d39d-e b52-11ea-bf33-6805caa954d0 90Gi RWO yoda-lvm 3h28m kafka-datadir-alibaba-kafka-cluster-private-paas-default-0 Bound yoda-0c861b0be777-11ea-bf33-6805caa954d0 90Gi RWO yoda-lvm 5d1h kafka-datadir-alibaba-kafka-cluster-private-paas-default-1 Bound yoda-5a840f48e777-11ea-bf33-6805caa954d0 90Gi RWO yoda-lvm 5d1h kafka-datadir-alibaba-kafka-cluster-private-paas-default-2 Bound yoda-b584d7eee777-11ea-bf33-6805caa954d0 90Gi RWO yoda-lvm 5d1h
```

3. Run the `kubectl describe pvc <pvc>` command to query the information about a PVC.
For example, you can run the `kubectl describe pvc kafka-datadir-alibaba-kafka-cluster-`

|   | command to query the information ab |   |
|---|---|---|

```
 kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 .
```

```
Name: kafka-datadir-alibaba-kafka-cluster-multi-alibaba-kafka-0 Namespace: default StorageClass: yoda-lvm Status: Bound Volume: yoda-d3b992bb-eb51-11ea-bf33-6805caa954d0 Labels: app=alibaba-kafka-broker
               app.name=alibaba-kafka-cluster-multi-alibaba-kafka
Annotations: pv.kubernetes.io/bind-completed: yes
               pv.kubernetes.io/bound-by-controller: yes
               volume.beta.kubernetes.io/storage-provisioner:
yodaplugin.csi.alibabacloud.com
               volume.kubernetes.io/selected-node: a36b10204.cloud.b12.amtest11
Finalizers: [kubernetes.io/pvc-protection] Capacity: 90Gi Access Modes: RWO VolumeMode: Filesystem Events: <none> Mounted By: alibaba-kafka-cluster-multi-alibaba-kafka-0
```

#### 2.1.6 FAQ

This topic provides answers to frequently asked questions about pod maintenance.

**What do I do if pods remain in the Terminating state?**

Cause The network plug-in has a container failure. Solution Forcibly delete the pod that you want to manage. The deleted pod will be started in automatic scheduling. For example, to delete the pod whose name is `alibaba-kafka-cluster-private-paas-default-`

```
0 , run the kubectl delete pod alibaba-kafka-cluster-private-paas-default-0 -n default --
```

`force --grace-period=0` command.

**What do I do if pods remain in the Pending state?**

Cause Persistent volume (PV) resources are not ready. No suitable node is available for scheduling. Solution Run the `kubectl describe pod <pod>` command to query the resource information of a pod. Coordinate resources.

**What do I do if pods remain in the CrashloopBackoff state?**

Cause The ApsaraMQ for Kafka process is repeatedly restarted due to an incorrect ZooKeeper address. Solution

| kubectl describe pod <pod> |   |
|---|---|
| cd <filepath> | command to |

2. Run the `cd <filepath>` command to switch to the queried path. Then, check the log file
server.log.

| Note If you cannot access the pod, run the docker ps -a \| grep |   |
|---|---|
|   | docker ps -a \| grep |
| main.*alibaba.*kafka \| awk '{print $1}' \| xargs -i docker cp |   |
| {}:/home/admin/logs/alikafka/server.log |   |

**What do I do if pods remain in the Error state?**

Cause Some data remains after data is cleared for redeployment. Solution Delete the disk data from the physical server that corresponds to the node that you want to manage.

**What do I do if topic data is lost or unavailable due to**

**incremental broker IDs?**

Cause A data write error occurred before you mount a PV to a pod. As a result, the PV fails to be mounted to the pod. The resources of ApsaraMQ for Kafka are cleared, but ZooKeeper data is not cleared. As a result, data is lost on a PV. Solution
1. Run the `kubectl get kafka -o yaml > new_kafka.yaml` command to query the resources of
ApsaraMQ for Kafka and generate a YAML file that contains the queried data.
2. Run the `kubectl delete -f kafka.yaml` command to delete the resources of ApsaraMQ for
Kafka.

```
3. Run the  kubectl get pvc | grep "alibaba-kafka-cluster" | awk '{print $1}' | xargs
```

`kubectl delete pvc` command to delete persistent volume claim (PVC) resources.
4. Check the results.
i. Run the kubectl get pod | grep kafka.*cluster command to check whether pods are cleared. ii. Run the kubectl get pvc | grep kafka command to check whether PVC resources are cleared. iii. Run the kubectl get pv | grep kafka command to check whether PV resources are cleared.
5. Delete data from the ZooKeeper directory.
i. Run the `kubectl exec -it zk-middleware-0 bash` command to access the container in which ZooKeeper is deployed. ii. Run the `cd /usr/share/zookeeper/bin/` command to switch to the bin directory of ZooKeeper. iii. Run the `sh zkCli.sh -server <IP address of the ZooKeeper pod>:2188` command to connect to ZooKeeper.

| ls / | command to query all d |
|---|---|
| rmr /kafka-private-clusters |   |

v. Run the `rmr /kafka-private-clusters` command to delete data from the ZooKeeper directory.
6. Redeploy ApsaraMQ for Kafka.

| privileged: true |   | from the new kaf _ |
|---|---|---|
|   | kubectl create -f new kafka.yaml _ |   |

### 2.2 Process maintenance

#### 2.2.1 Query the metric information of brokers

**brokers**

This topic describes how to query the metric information of brokers in ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

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
```

```
|SocketServer_NetworkProcessorAvgIdlePercent                    Gauge           Value
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
6668.00 600000 GTE|
```

```
--------------------------------------------------------------------------------------- --------------------------------------------------------------- --------------------------------------------------------------------------------------- ---------------------------------------------------------------
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

#### 2.2.2 Query logs

This topic describes how to query the logs of ApsaraMQ for Kafka. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the `kubectl exec -it <pod> bash` to connect to the pod in ApsaraMQ for Kafka.

| mple, if the name of the pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl exec -it alibaba-kafka-cluster-private-paas-default-0 bash |   |   |
|   |   | comma |

3. Run the `sudo su admin` command to switch to the administrator account.
4. Run the `cd /home/admin/logs/alikafka` command to switch to the directory in which logs
are stored.
5. Run the **ls** command to query a list of log files.

```
commercial.log controller.log kafka-authorizer.log kafka-request.log kafka-reques t.log.1 log-cleaner.log metrics.log network.log server.log state-change.log unk nown.log
```

6. Run the `cat <filename>` command to query the information about a log file.

#### 2.2.3 Query the status of a topic

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

#### 2.2.4 Query the status of a consumer group

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

#### 2.2.5 Query the data of ZooKeeper

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

7. Run the `ls /<zk node>` command to query the data of a ZooKeeper node.
For example, if the name of a ZooKeeper node is zookeeper, run the `ls /zookeeper` command.

```
cZxid = 0x0 ctime = Thu Jan 01 08:00:00 CST 1970 mZxid = 0x0 mtime = Thu Jan 01 08:00:00 CST 1970 pZxid = 0x0 cversion = -1 dataVersion = 0 aclVersion = 0 ephemeralOwner = 0x0 dataLength = 0 numChildren = 1
```

**What to do next**

After you query the data of ZooKeeper, run the **quit** command to exit ZooKeeper.

```
Quitting... 2020-09-01 11:45:05,123 [myid:] - INFO [main:ZooKeeper@684] - Session: 0x300axxxx0ba c losed 2020-09-01 11:45:05,125 [myid:] - INFO [main-EventThread:ClientCnxn$EventThread@519] - EventThread shut down for session: 0x300axxxx0ba
```

#### 2.2.6 Update the configurations of a topic

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

#### 2.2.7 FAQ

This topic provides answers to frequently asked questions about process maintenance.

**How do I restart the ApsaraMQ for Kafka process for a pod?**

By default, the ApsaraMQ for Kafka process is asynchronously started during the deployment of a pod. You can run the livecheck command to check whether the process is alive.
1. Modify the check-health.sh file in the /home/admin/kafka-tool directory to enable keepalive
detection.
2. Restart the process.
i. Run the **kill** command to terminate the ApsaraMQ for Kafka process. ii. Modify the start_kafka.sh file. iii. Run the `sh start_kafka.sh` command to restart the ApsaraMQ for Kafka process.
3. Restore the check-health.sh file and restart the pod.

**How do I restart the ApsaraMQ for Kafka process if an**

**exception occurs in logs?**

You can restart the process by terminating the process. To terminate the process, use one of the following methods: Run a script to terminate the process.

| kubectl exec <pod> /bin/sh -c main /home/admin/KafkaProxy/bin/kafka-server- |   |
|---|---|
|   | command to terminate the process. |

Run commands to terminate the process. i. Run the `kubectl exec -it <pod name> /bin/bash` command to access a pod. ii. Run the `sudo su admin` command to switch to the administrator account. iii. Run the `jps` command to query all Java processes. iv. Run the `kill <pid>` command to terminate a process.

**What do I do if logs contain error information?**

Service logs are stored in the /home/admin/logs/alikafka directory, including important logs in the server.log and state-change.log files. In this example, the state-change.log file contains errors. The state-change.log file records information about the status of partitions. Errors often occur on the controller or during the conversion of partition states. Find the topic name in the error information and troubleshoot errors in the topic.
1. Run the `cd /home/admin/KafkaProxy` command to switch to the /home/admin/KafkaProxy
directory.

```
2. Run the  ./bin/kafka-topics.sh kafka-topics.sh --describe --bootstrap-server `hostname
```

-i`:9092 --topic {topic} command to query the information about a topic.

### 2.3 Other maintenance operations

#### 2.3.1 Evaluate the capacity of a cluster

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

## 3 Routine inspection

### 3.1 Inspect the status of pods

This topic describes how to inspect the status of pods. The information about the master node in ApsaraMQ for Kafka is obtained.
1. Connect to the master node in ApsaraMQ for Kafka.
2. Run the kubectl get pods -o wide | grep kafka command to query a list of pods in
ApsaraMQ for Kafka.

```
alibaba-kafka-cluster-multi-alibaba-kafka-0 2/2 Running 1 24h 10.XX.XX.XX a36b10204.cloud.b12.amtest11 <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-1 2/2 Running 4 24h 10.XX.XX.XX a36b10208.cloud.b12.amtest11 <none> <none> alibaba-kafka-cluster-multi-alibaba-kafka-2 2/2 Running 0 24h 10.XX.XX.XX a36b10008.cloud.b10.amtest11 <none> <none> alibaba-kafka-cluster-private-paas-default-0 2/2 Running 3 47h 10.XX.XX.XX a36b10005.cloud.b10.amtest11 <none> <none> alibaba-kafka-cluster-private-paas-default-1 2/2 Running 2 47h 10.XX.XX.XX a36b10203.cloud.b12.amtest11 <none> <none> alibaba-kafka-cluster-private-paas-default-2 2/2 Running 3 47h 10.XX.XX.XX a36b10016.cloud.b10.amtest11 <none> <none> alibaba-kafka-console-6dcf5f9b59-bqvn6 1/1 Running 0 26h 10.XX.XX.XX a36b10203.cloud.b12.amtest11 <none> <none> alibaba-kafka-operator-6b9dbb49cc-s8s49 1/1 Running 0 47h 10.XX.XX.XX a36b10203.cloud.b12.amtest11 <none> <none>
```

> **Note:** In normal cases, pods are in the Running state.

3. Run the `kubectl describe pod <pod>` command to query the information about a pod.

| example, if the name of a pod is | alibaba-kafka-cluster-private-paas-default-0 |   |
|---|---|---|
| kubectl describe pod alibaba-kafka-cluster-private-paas-default-0 |   |   |
|   |   | command |

```
Name: alibaba-kafka-cluster-private-paas-default-0 Namespace: default Priority: 0 PriorityClassName: <none> Node: a36b10005.cloud.b10.amtest11/10.XX.XX.XXX Start Time: Sun, 30 Aug 2020 11:58:35 +0300 Labels: app=alibaba-kafka-broker
                    app.kubernetes.io/instance=alibaba-kafka
                    app.kubernetes.io/managed-by=Tiller
appname=alibaba-kafka-cluster-private-paas-default
```

```json
                    app.name=alibaba-kafka-cluster-private-paas-default
                    controller-revision-hash=alibaba-kafka-cluster-private-paas-defaul
t-66ff8bb98b
                    helm.sh/chart=alibaba-kafka-0.0.6-d460bef
                    kafka.env=private-pass
                    statefulset.kubernetes.io/pod-name=alibaba-kafka-cluster-private-p
aas-default-0 Annotations: networking.alibaba.com/ip:
                      {"Address":
{"IP":"10.XX.XX.XXX","Mask":"///8AA=="},"Gateway":"10.XX.XX.XXX","NetID":11,"Subnet":"s net-cn-qingdao-env17-amtest11001-a-1",... Status: Running IP: 10.XX.XX.XXX Controlled By: StatefulSet/alibaba-kafka-cluster-private-paas-default Containers:
  main:
    Container ID:
docker://3fa64fb320b9b7898ea6b008f08ed93fdbde08f04b7e0fb1ea1d699ecce1c4fe
    Image:          cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkabroker:efbede0b9a06ef5b8966ce7753ac11e605d943e57af0ebac1f336567ad7fc160
    Image ID:       docker-pullable://cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkabroker@sha256:66726a9c09e6c3cf6420b13e4e3a632383d3f1378c5324dbbd05b0a6d45aa631
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
      vpc_mode_vpc_id:                          vpc-rt1k708pzcXXX
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-default
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.XX.XX.XXX,10.XX.XX.XXX,10.XX.XX.XXX
      vpcmodedeleteserviceenable:           false
```

```
pc_ode_deete_se ce_eabe: ase
      vpc_mode_vsw_id:                          vsw-rt1fjm1djgXXX
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080
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
docker://57d3d96ad8775f6c956f68d70d34fdf616b598b927417597883d92e9287c09c8
    Image:          cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkaagent:4d43d896d38f1a8d00a3cb89df8184f0f18c517df3544a72a00d8de71b497eee
    Image ID:       docker-pullable://cn-qingdao-env17-d01-
reg.docker.intra.env17e.shuguang.com/private-paas/alibaba-kafkaagent@sha256:43c876cc713aecab8361114070f8ca367ebe44bd959210c54ee28f4cd775a97f
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
      vpc_mode_vpc_id:                          vpc-rt1k708pzc13i9gpzh22v
      DEBUG_ENABLE:                             false
      zk_connect_time_out:                      36001
      vpc_mode_enable:                          true
      clusterName:                              private-paas-default
      get_ip_from_hostname:                     true
      prometheus_javaagent_port:                8081
      enable_2020_ssl:                          true
      proxy_port:                               9092
      vpc_mode_type:                            SingleTunnel
      middleware_zk_hosts:                      10.XX.XX.XXX,10.XX.XX.XXX,10.XX.XX.XXX
      vpc_mode_delete_service_enable:           false
      vpc_mode_vsw_id:                          vsw-rt1fjm1djgpia5suslag6
      KACONF_OFFSETS_TOPIC_REPLICATION_FACTOR:  3
      vips_9092:                                UNKNOWN_VARIABLE
      JMX_PORT:                                 19092
      vips_vpc:
192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080,192.XXX.XXX.XX:8080
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
QoS Class: Burstable Node-Selectors: networking.alibaba.com/asw=asw-cn-qingdao-env17-amtest11001-a Tolerations: node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events: <none>
```

> **Note:** In most cases, the value of the Events parameter is <none>.

### 3.2 Inspect the resource availability

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

### 3.3 Inspect the service availability

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

### 3.4 Inspect a physical server after a restart

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
