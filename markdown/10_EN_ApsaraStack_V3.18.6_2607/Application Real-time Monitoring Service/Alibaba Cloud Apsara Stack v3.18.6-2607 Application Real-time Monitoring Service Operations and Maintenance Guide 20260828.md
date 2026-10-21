---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 31
source_pdf: "b0f24a5a353a34ea_Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Operations and Main"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%BA%94%E7%94%A8%E5%AE%9E%E6%97%B6%E7%9B%91%E6%8E%A7%E6%9C%8D%E5%8A%A1ARMS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Application%20Real-time%20Monitoring%20Service%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Application Real-time Monitoring Service Operations and Maintenance Guide 20260828

## Table of Contents

- 1 O&M overview
  - 1.1 System architecture
  - 1.2 Deployment architecture
  - 1.3 Server role list
- 2 High-risk operations
- 3 Routine maintenance
  - 3.1 Log on to the Apsara Uni-manager Operations Console
  - 3.2 Log in to the Apsara Base O&M Platform
  - 3.3 Inspect components
  - 3.4 Perform O&M operations on ESDB
- 4 Troubleshooting
- 5 Alert handling
- 6 Log reference
- 7 FAQ
- 8 Upgrade guide

## 1 O&M overview

### 1.1 System architecture

This topic describes the system architecture of Application Real-Time Monitoring Service (ARMS). Data Query Console API Service TLog-Console Diamond Middware- ZooKeeper TLogst JStorm JStorm Data Aggregation Elasticsearch HBase JStorm Cluster Cluster Cluster Traces Log Collection (StarAgent) Collector Collector Collector Collector Cluster Active Active Active Reporting Reporting Reporting Application Application ARMS ARMS ARMS Application A Agent B Agent Agent In Apsara Stack, ARMS consists of the console and API service. Other services such as core computing and storage are dependent on TLog. For more information, see **Deployment**
**architecture**.

### 1.2 Deployment architecture

This topic describes the meaning of components in the ARMS deployment architecture.

| Component group | Component name | Description |
|---|---|---|
| ARMS | Console and API service | The console of the ARMS Application Monitoring product is mainly responsible for displaying the application list, distributed trace query and diagnosis, real-time application performance aggregation, dynamic discovery of distributed topology, and application-related settings. The API service mainly provides external API services. The console service and API service are deployed in the same container. |

| TLog | Collector | This component belongs to TLog. Applications report service invocation data by integrating the ARMS Agent. The Collector cluster is responsible for collecting the invocation data. |
|---|---|---|
|   | JStorm | This component belongs to TLog. The JStorm cluster includes two types of components: TLogst and JStorm. It is mainly responsible for log collection, traffic scrubbing, computation, and storage writing. |
|   | HBase | This component belongs to TLog. It is mainly responsible for storing the statistical data of ARMS Application Monitoring. |
|   | ESDB | This component belongs to TLog. It is mainly responsible for storing the detailed data of ARMS Application Monitoring. |
|   | TLog-Console | This component belongs to TLog. It is mainly responsible for collection point management and collection rule distribution. |

### 1.3 Server role list

This topic describes the server roles available in ARMS.

| Project | Cluster | Service | Server role | Description |
|---|---|---|---|---|
| ARMS | BasicCluste r | arms-arms- console | arms-arms- console.ArmsConsoleInit# | ARMS Application Monitoring console DB initialization. |
|   |   |   | arms-arms- console.ArmsConsoleProc ess# | ARMS Application Monitoring console. |
|   | ApmCluster | arms-apm | arms-apm.ArmsApmInit# | ARMS Application Monitoring resource initialization. |
|   |   | arms-arms- collector | arms-arms- collector.ArmsCollectorPro cess# | Used for trace data reported by Application Monitoring. |
|   |   | tlog- tlogEsdb | tlog-tlogEsdb.TlogEsdb# | ESDB cluster, used to store detailed data of Application Monitoring. |

| TLog | BasicCluste r |   |   |   |
|---|---|---|---|---|
|   |   | tlog- tlogHbase | tlog- tlogHbase.TlogHbase# | Hbase cluster, used to store statistical data of Application Monitoring. |
|   |   | tlog- tlogService | tlog-tlogService.Tlogst# | Node where JStorm cluster Nimbus is located. |
|   |   |   | tlog-tlogService.Jstorm# | Node where JStorm cluster Supervisor is located. |
|   |   |   | tlog-tlogService.TlogInit# | TLog DB resource initialization. |
|   |   |   | tlog- tlogService.TlogConsole# | TLog console. |

## 2 High-risk operations

Proceed with caution when performing high-risk operations during O&M tasks. High-risk operations in ARMS O&M are deletion of resources.

**Operation entry**

On the Resource Management page of the ARMS Management Console, you can view all resources used by ARMS. When logged in as an Admin account , you can delete resources on this page.

**Operational impact**

If you delete a resource, the tasks assigned to that resource cannot be automatically or manually stopped. The tasks will continue to run without being affected.

**Operational recommendations**

We recommend that you do not delete resources under any circumstances.

## 3 Routine maintenance

### 3.1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: regionid.aso.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open a web browser.
2. In the address bar, enter the URL of the Apsara Uni-manager Operations Console in the
format of region-id.aso.intranet-domain-id.com, and press the ENTER key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter your username and password.

> **Note:** Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, the password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
4. Click **Log In** to log on to the Apsara Uni-manager Operations Console.

### 3.2 Log in to the Apsara Base O&M Platform

**O&M Platform**

This topic describes how O&M engineers and other users log in to the Apsara Base O&M Platform.

**Prerequisites**

Obtain the access URL, username, and password for the Apsara Uni-manager Operations Console from deployment personnel or an administrator. The Apsara Uni-manager Operations Console access URL is in the format region-id.aso.intra net-domain-id.com. Chrome is the recommended browser.

**Procedure**

1. Open a browser.
2. In the address bar, enter the access URL for the Apsara Uni-manager Operations Console, r
egion-id.aso.intranet-domain-id.com, and press Enter.
3. Enter your username and password.

> **Note:** Obtain the username and password for the Apsara Uni-manager Operations Console from deployment personnel or an administrator.
> To switch languages, use the language selector in the upper-right corner of the page.

When you log in to the Apsara Uni-manager Operations Console for the first time, you must change your password. Follow the on-screen prompts to change your password. Your password must meet the following requirements: Uppercase and lowercase letters Numbers (0–9) Special characters (for example, !, @, #, $, and %) Password length: 10–20 characters
4. Click **Log In**.
5. In the top menu bar of the Apsara Uni-manager Operations Console, click **Platform O&M**.
6. From the drop-down list, in the **Apsara Base O&M Platform** section, select an entry to
configure.

### 3.3 Inspect components

This topic describes common system inspection methods.

**Inspect Diamond**

1. Log in to the Apsara Base O&M Platform.
2. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**. On the **Product & Cluster O&M** page, enter
`middleWareAll` in the **Product | Cluster** field, and click **Cluster Details** in the **Actions** column of the cluster that is displayed.
3. On the **Services** tab, enter
`middleWare-jmenv` in the **Service** field. Check whether the instances corresponding to the **middleWare-jmenv** service are normal.

**Inspect HBase**

1. Log in to the Apsara Base O&M Platform.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**. On the
**Service Management** page, enter
`tlog-tlogHbase` in the **Service** field.
3. On the **Service Instances** tab, click **Instance Details** in the **Actions** column of the
cluster that displayed.
4. On the **Component Details** page, click the **TlogHbase#** server role in the **Components**
pane.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of any instance. In the left-
side pane of the page that appears, click any HBase server to log on to the server, and run the following commands to open a shell session in the container:

```python
sudo docker ps sudo docker exec -it <ID of the HBase container> bash su hadoop cd ~/hbase-current/bin ./hbase shell
```

6. Run the `list` command to check whether the tlog-biz table exists.
7. Run the `describe 'tlog-biz'` command to check whether the coprocessor is properly
loaded for the tlog-biz table.
8. Run the `scan 'tlog-biz',{LIMIT=>10}` command to check whether data reading is normal.

**Inspect TLog**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > TLog > Middleware**. On the
page that appears, click a button. If the corresponding page can be opened, TLog is properly running.

**Inspect JStorm**

1. Log in to the Apsara Base O&M Platform.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**. On the
**Service Management** page, enter
`tlog-tlogService` in the **Service** field. On the **Service**
**Instances** tab, click **Instance Details** in the Actions column of the cluster that is
displayed.
3. On the **Service Instances** tab, click **Instance Details** in the **Actions** column of the
cluster that displayed.
4. On the **Component Details** page, click the **Tlogst#** server role in the **Components** pane.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of any instance. In the left-
side pane of the page that appears, click any TLogst server to log on to the server and run the following commands to open a shell session in the container:

```python
sudo docker ps sudo docker exec -it <ID of the TLogst container> bash
```

6. Run the `su admin` command to switch to the admin user.
7. Run the `jstorm list` command to check whether the topology and related nodes are
normal.

**Inspect the ARMS console**

Log on to the Application Real-Time Monitoring Service (ARMS) console. If the logon is successful, the ARMS console is normal.

### 3.4 Perform O&M operations on ESDB

**ESDB**

This topic describes the features and common O&M operations of Elasticsearch Database (ESDB). ESDB is a high-performance and cost-efficient distributed document database developed based on open source Elasticsearch. It supports efficient and real-time full-text retrieval, multi-dimensional query, geographic information query, and aggregate analysis. It provides integrated storage, search, and analysis capabilities for fields such as application search, O&M diagnostic analysis, and location-based services (LBS). It is committed to evolving into an intelligent analysis infrastructure in the next three years, aiming to provide efficient prediction and diagnostics capabilities to boost machine learning performance.

**ESDB architecture and engine**

ESDB adopts a shared-nothing distributed architecture. Service nodes of ESDB are categorized into master nodes and data nodes. Services read and write data through client nodes. Three master nodes are deployed in three data centers to ensure the availability of the cluster. The master is elected by using the bully algorithm. Data nodes store data and data replicas. The index mapping, number of shards, routing key, and number of nodes are determined based on the service data size and the query requirements. Data distribution is balanced in real time based on resource consumption such as the data volume of nodes. Data nodes ensure cross-data center disaster recovery. Data replicas are synchronously replicated among data nodes. If a shard fails, automatic switchover or failover is performed. You can expand the read capability by increasing the number of replicas. Write requests from client nodes are routed to the specified shards, whereas read requests are randomly assigned to any node and then forwarded to the specified primary and standby shards. Master Node Data Node Client Node (No Data or Master) Request Data Data Data Center Center Center For any write to ESDB, the destination shard needs to be located by specifying the shard key. You can add, update, and delete a record or a document. doc_id is the unique identifier of a record or document in a shard. When you update an existing doc_id, you do not need to obtain the complete historical record or document. Instead, you can update only the specified field. If a field without defined mapping appears, ESDB indexes this field based on the default mapping rules. Mapping rules can be dynamically modified, but the indexes of historical data are not rebuilt. Primary and standby replicas of ESDB are copies of records and documents, and are synchronously replicated. Translogs are recorded through write-ahead logging (WAL) to prevent data loss. Due to the difference in the timing of primary/standby replay requests and refreshes, ESDB ensures eventual consistency through versioning. To improve the write capability, ESDB introduces double hashing to balance loads in time series or logging scenarios. ESDB supports dynamic double hashing for scenarios with uneven hotspots. ESDB improves the write capability of hotspots through double hashing. It can push hash rules in real time to balance hotspots. After a hot shard is hashed to more nodes, queries also need to be distributed to more nodes. You can use a smooth hashing strategy to minimize the data loss during queries. The write performance and cost of ESDB are directly related to the size of transaction commit batches and the size, type, number, and value sparsity of indexed fields. A service does not necessarily facilitate efficient merging of individual shards. Therefore, ESDB implements batch merging on the server side. In addition, ESDB provides differentiated indexing strategies for frequently queried fields and rarely queried fields, reducing the indexing overhead of rarely queried fields. ESDB queries (including aggregate analysis) can be roughly divided into the following categories: Query with a shard key specified: queries only the specified shard. The performance cost of queries that carry doc_id is low. Query without a shard key: queries all shards. ESDB summarizes and sorts the query result before returning it. This type of query has a low throughput. ESDB supports queries and aggregation with any dimension and low QPS. ESDB supports near real-time (NRT) searches. ESDB builds new indexes in batches within a time period no longer than the refresh interval, so that new data can be queried. A shorter refresh interval means better real-time performance. However, to ensure write performance, indexes are append-only. A shorter refresh interval may result in more fragmented indexes, compromising the read performance. Considering the tradeoff between read and write performance, the default refresh interval is set to 1s. To ensure read performance, we recommend you merge indexes into fewer large indexes based on the index merge strategy. If your business requires real-time data visibility immediately after data is written, you can specify a forced refresh on the client. However, we recommend that you do not use this method frequently because the read and write performance may be impaired. ESDB does not guarantee transactionality. ESDB provides rich full-text retrieval capabilities. For more information, see Elasticsearch official documentation. ESDB has accumulated considerable capability in delivering real-time performance for equality queries. Composite indexes can effectively help services achieve significant performance improvements in complex queries at a low cost. The aggregate functions of ESDB can support some complex analysis. These functions mainly focus on time series, O&M, diagnostics, and geographic information scenarios. For more information, see Elasticsearch official documentation. Aggregations execute rapidly and deliver results nearly in real time like searches. In a request, the same copy of data is simultaneously retrieved, filtered, and analyzed in real time, without requiring predefinition as with Apache Hadoop.

**Common O&M operations**

CLI-based operations Elasticsearch cluster Query the health status of a cluster

```bash
curl IP:PORT/_cluster/health?pretty
```

View system statistics

```bash
curl IP:PORT/_cluster/stats?pretty
```

Query the pending tasks of a cluster

```bash
curl IP:PORT/_cluster/pending_tasks?pretty
```

View cluster configurations

```bash
curl IP:PORT/_cluster/settings?pretty
```

Specify slow log configurations of a cluster

```
index.search.slowlog.level: TRACE index.search.slowlog.threshold.query.warn: 10s index.search.slowlog.threshold.query.info: 5s index.search.slowlog.threshold.query.debug: 2s index.search.slowlog.threshold.query.trace: 500ms index.search.slowlog.threshold.fetch.warn: 1s index.search.slowlog.threshold.fetch.info: 800ms index.search.slowlog.threshold.fetch.debug:500ms index.search.slowlog.threshold.fetch.trace: 200ms
```

Query the hot threads for nodes in a cluster

```bash
curl IP:PORT/nodes/local/hotthreads
```

Adjust the log levels of a cluster

```bash
curl -XPUT IP:PORT/cluster/settings -d'{"transient":{"logger.root":"DEBUG"}}' curl -XPUT IP:PORT/cluster/settings -d'{"transient":{"logger.root":"INFO"}}'
```

Bring a node offline If a node is directly shut down, the corresponding replica can be recovered through automatic failover. Alternatively, you can configure a blacklist of shards. ESDB automatically transfers shards corresponding to the IP addresses in the blacklist to other nodes. After the transfer is complete, you can bring the empty node offline without affecting the service.

```json
curl -XPUT IP:PORT/_cluster/settings -d '{
 "transient" :{
 "cluster.routing.allocation.exclude._ip" : "IP"
```

`}` `}'` Index View the status of cluster shards

```bash
curl IP:PORT/_cat/Shards?v
```

View index settings

```bash
curl IP:PORT/INDEX/_settings?pretty
```

View index mappings

```bash
curl IP:PORT/INDEX_NAME/TYPE_NAME/_Mapping?pretty
```

Push the refresh interval

```bash
curl -XPUT IP:PORT/INDEX_NAME/_settings -d '{"index" : {"Refresh_interval" : "10s"}}'
```

Hot shard migration a. Disable allocation.

```bash
curl -XPUT IP:PORT/_cluster/settings -d '{"persistent": {"cluster.routing.allocation.enable": "none"}}'
```

b. Limit the allocation speed.

```bash
curl -XPUT IP:PORT/_cluster/settings -d '{"persistent":{"cluster.routing.allocation.node_concurrent_recoveries":8}}' curl -XPUT IP:PORT/_cluster/settings -d '{"persistent":{"cluster.routing.allocation.cluster_concurrent_rebalance":8}}' curl -XPUT IP:PORT/_cluster/settings -d
 '{"persistent":{"indices.recovery.max_bytes_per_sec":"600mb"}}'
```

c. Migrate shards.

```json
curl -XPUT IP:PORT/_cluster/reroute?pretty -d '{"commands":[{"move": {"index":"INDEX","Shard":SHARD_NUM,"from_node":"SOURCE_IP","to_node":"DES_IP"}}]}'
```

d. Enable allocation.

```bash
curl IP:PORT/_cluster/settings -d
 '{"persistent": {"cluster.routing.allocation.enable": "all"}}'
```

GUI-based operations Install Kibana.

## 4 Troubleshooting

This topic describes how to troubleshoot some common issues. Table 1. Troubleshooting methods for common issues

| Issue | Symptom | Analysis |   |   | Solution |   |   |
|---|---|---|---|---|---|---|---|
| A Docker container does not respond. | When you run the docker ps command in the Docker console to view the running information of all Docker containers, a Docker container does not respond. | - |   |   | 1. Run the docker |   |   |
|   |   |   |   |   |   | docker |   |
|   |   |   |   |   | inspect |   |   |
|   |   |   |   |   | {DockerIP} |   |   |
| Logs contain the Unknow Host error. | The arms-console.log file in /home/admin/logs/ of the Application Real- Time Monitoring Service (ARMS) console container or the *worker*.log file in /home/admin/logs of JStorm contains the "Unknow Host" error. | The domain name cannot be accessed. |   |   | Configure the mapping between the corresponding IP address and the domain name in /etc/hosts of the container. |   |   |
| The disk load of the ZooKeeper container is too high. | Excessive traffic causes high disk usage of the physical machine where the ZooKeeper container resides. | - |   |   | Mount the ZooKeeper container mounted on a SATA disk to an SSD disk. |   |   |

|   |   |   | docker |   |
|---|---|---|---|---|
|   |   | restart |   |   |
|   |   | {DockerID} |   |   |

| The "no router to host" error occurs on the ZooKeeper container. | The zookeeper.log file of the ZooKeeper container contains the "no router to host" error. | This error usually occurs in a ZooKeeper cluster in an HBase container and is usually caused by dirty data generated by changes. | Delete and restart the HMaster service from ZooKeeper. 1. Go to zkcli of the HBase container and run the following commands: ls /hbase/root- region-sever get /hbasedocker- em14- hbsmonitor/root -region-server delete /hbase/root- region-server quit hbase- daemon.sh start master 2. Run the jps command to check whether the HMaster process is started. |
|---|---|---|---|
| A basic module issue occurs. | The ARMS console cannot be opened. | - | Restart the ARMS console container. |
| A basic module issue occurs. | All time series data in the ARMS console drops to zero. | This issue is caused by HBase read exceptions. | For more information, see Inspect components. |

| A basic module issue occurs. | The ARMS data pulling delay is too high. | Log on to the TLog console, click Collection Points in the Actions column of the arms cloud group, and _ view the details of collection points arms cloud1 to _ arms cloudx. _ If the status is normal, this issue is not related to the collection process. If data continues to flow into the file but the status of the collection points is abnormal or it has been over 15 minutes since the last data pulling, the issue is related to JStorm. | For more information about JStorm inspection, see Inspect components. |
|---|---|---|---|

## 5 Alert handling

This topic describes how to handle common alerts.

**High disk usage**

1. Run the following command to view the disk usage:

```
df –h
```

2. Run the following commands to find and clear the directory and file that occupy the most
disk space: In this example, the catalina.out file occupies the most disk space.

```
cd /home/admin du --max-depth=1 –h cat /dev/null > ./catalina.out
```

**High memory usage**

1. Run the `top` command to query the process that occupies the most memory.
2. Run the following command with the obtained process ID (PID) to view the service
corresponding to the process:

```
ps aux|grep {PID}
```

If the system exhibits sustained high memory usage, contact Apsara Stack technical support engineers to check whether you need to scale out the memory.

**High CPU utilization**

Handle this alert by referring to the method described in the High memory usage section.

**Failed HTTP inspection**

Find the component on which the HTTP inspection fails, locate the specific cause of the failure on the corresponding server, and then start or restart the server to restore the corresponding feature. In Application Real-Time Monitoring Service (ARMS), the following two components expose services over HTTP: The arms-console-process container corresponding to the ARMS console The tlog-console container corresponding to the TLog console Both containers provide HTTP services by using Tomcat and Tengine. Tengine starts on port 80 and Tomcat starts on port 8080. HTTP requests are forwarded by Tengine from port 80 to port 8080. You can run the `curl -v 127.0.0.1:8080` and `curl -v 127.0.0.1:80` commands to determine whether the issue occurred on Tomcat or Tengine. To restart Tengine, run the following command:

```
/opt/taobao/tengine/bin/nginxctl restart #Run the command as the root user.
```

To restart Tomcat, run the following commands:

```
su admin #Switch to the admin user and run the following commands. ps aux | grep arms-c onsole # Run this command in the arms-console-process container. ps aux | grep tlog-con sole # Run this command in the tlog-console container. kill -9 <pid> # Kill the process based on the PID obtained by using the preceding commands.
 $CATALINA_HOME/bin/startup.sh # Run the Tomcat startup script.
```

## 6 Log reference

This topic describes the common log files of each component of Application Real-Time Monitoring Service (ARMS), including the log paths and descriptions.

**arms-console**

| Log path | Description |
|---|---|
| /home/admin/logs/arms/arms-console.log | The service logs of arms-console. |
| /home/admin/taobao-tomcat-production- 7.0.85/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/taobao-tomcat-production- 7.0.85/logs/localhost.log | The localhost logs of Tomcat. |

**arms-pop**

| Log path | Description |
|---|---|
| /home/admin/logs/arms/arms-pop.log | The service logs of arms-pop. |
| /home/admin/arms-pop/taobao-tomcat- production/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/arms-pop/taobao-tomcat- production/logs/localhost.log | The localhost logs of Tomcat. |

**arms-collector**

| Log path | Description |
|---|---|
| /home/admin/logs/arms/arms-collector.log | The service logs of arms-collector. |
| /home/admin/logs/arms/tracelogs | The service logs reported by the Application Monitoring module of users. Do not delete these logs. |
| /home/admin/taobao-tomcat-production- 7.0.85/logs/catalina.out | The catalina logs of Tomcat. |

| /home/admin/taobao-tomcat-production- 7.0.85/logs/localhost.log | The localhost logs of Tomcat. |
|---|---|

**tlogconsole**

| Log path | Description |
|---|---|
| /home/admin/tlogconsole/logs/tlog-console.log | The service logs of tlogconsole. |
| /home/admin/taobao-tomcat-production- 7.0.85/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/taobao-tomcat-production- 7.0.85/logs/localhost.log | The localhost logs of Tomcat. |

**middware-zookeeper**

| Log path | Description |
|---|---|
| /opt/taobao/zookeeper/zookeeper.out | The service logs of ZooKeeper. |

**JStorm cluster (including TLogst and JStorm Nimbus)**

| Log path | Description |
|---|---|
| /home/admin/logs/nimbus.log | The service logs of Nimbus in the JStorm cluster. |
| /home/admin/logs/supervisor.log | The logs of Supervisor in the JStorm cluster. |
| /home/admin/logs/check.log | The status check logs of Nimbus and Supervisor. |
| /home/admin/logs/xxxx-worker-<Port>.log | The logs of workers of collection points. |

**JStorm (including JStorm and JStorm Supervisor)**

| Log path | Description |
|---|---|
| /home/admin/logs/supervisor.log | The logs of Supervisor in the JStorm cluster. |
| /home/admin/logs/check.log | The status check logs of Supervisor. |

| /home/admin/logs/xxxx-worker-<Port>.log | The logs of workers of collection points. |
|---|---|

**HBase**

| Log path | Description |
|---|---|
| /home/hadoop/cluster-data/logs/hbase health.log _ | The health check logs of HBase. |
| /home/hadoop/cluster-data/hbase/logs/hbase- hadoop-master-xxx.log | The Master logs. |
| /home/hadoop/cluster-data/logs/hadoop-xxx- namenode-xxx.log | The NameNode logs. |
| /home/hadoop/cluster-data/hbase/logs/hbase- xxx-regionserver-xxx.log | The Region Server logs. |
| /home/hadoop/cluster-data/hbase/logs/hbase- xxx-zookeeper-xxx.log | The ZooKeeper logs. |

## 7 FAQ

This topic lists frequently asked questions about ARMS O&M.

**How to find the ARMS administrator account and password?**

In some scenarios, you must use the built-in ARMS administrator account. For example, data forwarding for a job is generated by a monitoring job that belongs to the ARMS administrator. Obtain the administrator account and password from the deployment engineer or administrator. To find the administrator account and password, follow these steps:
1. Log on to Apsara Infrastructure Management.
2. In the navigation pane on the left, choose **Resource Management > Product Cluster**
**O&M**. On the **Product Cluster O&M** page, enter `arms` in the **Product | Cluster** search
box. In the **Actions** column of the search result, click **Cluster Details**.
3. On the Cluster Details page, click the **Resource Details** tab. In the resource list on the
**Resource Details** tab, select **accesskey**.
4. In the **Resource Request Result** column, click the icon, and then click the content that
appears. In the **Resource Request Result** dialog box, view the ARMS administrator account and password.

**Handle HBase metric hot spot issues**

Application Monitoring metrics in ARMS are stored in HBase. A JStorm cluster analyzes the reported metric logs and writes them to HBase. Some regions experience serious HBase hot spot issues. This means only a few machines in the HBase cluster run at full load while other machines operate at low loads. Hot spot issues can affect business services. For example: High Filenum: Hot spot machines have high loads. This causes Region splitting to time out, increasing the number of files (Filenum) on the Region. Metric data loss: When a hot spot machine runs at full load, metrics written to that machine are affected. This causes metric data loss on the console. Metrics in HBase are distributed based on two dimensions: <organization + metric>. Apsara Stack environments usually have a primary production organization. As a result, a single organization can generate a large volume of metric data. This concentration of data can cause hot spot issues. If you confirm this issue exists in your environment, contact ARMS R&D for an optimization plan.

**How to check the Nimbus status?**

1. On the Nimbus machine, run the `jps` command to check for NimbusServer, Supervisor,
and Worker processes.
2. Run the `jstorm list` command to view Nimbus details.
3. Run the jstorm list | grep "host" | wc -l command to check how many topologies are
in the Active state. If the number of hosts does not match the number of JStorm clusters, a JStorm node container has failed.
4. Run the jstorm list | grep {topo name} command.
If the name of the data collection point in TLog is not found, the JStorm topology job has stopped running.

**How do you view error messages in the logs under**

**/home/admin/logs?**

1. Run the following command to identify the Worker.

```
cat -worker-.log* | grep Exception
```

2. Run the following command to view the logs on Nimbus.

```bash
grep 'kill' -A 20 /home/admin/logs/nimbus.log
# Also try other keywords.
```

3. Run the following command to view the supervisor.log file on each server. A copy of this log
is also on the Nimbus machine.

```
grep 'dead' -A 20 /home/admin/logs/supervisor.log
```

If an error such as HBase flush failed or HBase write queue is full is reported, the HBase module has failed.

**What to do if you encounter an invalid callback URL error**

**during logon?**

If you encounter an **Invalid callback URL** error during logon, follow these steps to resolve it.
1. Check whether the back_URL in the browser's address bar is correct. The preceding figure
shows a typical case where the back_URL is incorrectly set. It should be changed to the ARMS domain name.

> **Important:** Do not access ARMS using an IP address.

2. If you access ARMS using a domain name and the error persists, check whether the top-
level domain of Dauth matches the top-level domain of ARMS in the back_URL. Example: A scenario where both are consistent.

```
dauth.sgcloud.com arms.console.sgcloud.com
```

Example of an inconsistency

```
dauth.sgcloud.com arms.console.aliyun.com
```

**Can I start arms-console with the root account?**

Do not start arms-console with the root account. Doing so makes ARMS unavailable. The localhost.log file contains the following error:

```
Caused by: java.lang.RuntimeException: java.io.FileNotFoundException: /root/logs/mcms/i18n/i18nResourcesFile (No such file or directory)
```

`at`

```
com.alibaba.mcms.client.utils.McmsFileUtil.readI18nResourcesFile(McmsFileUtil.java:112)
```

`at`

```
com.alibaba.mcms.client.service.impl.McmsClientServiceImpl.initData(McmsClientServiceImpl ava:471)
```

`at`

```
com.alibaba.mcms.client.service.impl.McmsClientServiceImpl.initApp(McmsClientServiceImpl. va:401)
```

`at`

```
com.alibaba.mcms.client.service.impl.McmsClientServiceImpl.init(McmsClientServiceImpl.jav 348)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
```

`at`

```
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
```

`at`

```
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:606)
```

`at`

```
org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeCustom itMethod(AbstractAutowireCapableBeanFactory.java:1694)
```

`at`

```
org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMe ods(AbstractAutowireCapableBeanFactory.java:1633)
```

`at`

```
org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBe (AbstractAutowireCapableBeanFactory.java:1562)
        ... 27 more
        Caused by: java.io.FileNotFoundException:
/root/logs/mcms/i18n/i18nResourcesFile (No such file or directory)
        at java.io.FileInputStream.open(Native Method)
        at java.io.FileInputStream.<init>(FileInputStream.java:146)
```

`at`

```
com.alibaba.mcms.client.utils.McmsFileUtil.readI18nResourcesFile(McmsFileUtil.java:87)
        ... 37 more
```

**How to Resolve a Failed to access resource /WEB-INF/lib/.jar**

**Error During Process Startup**

When you manually upgrade arms-console or arms-pop, if you delete the /WEB-INF/lib directory and decompress the new package, many question mark files (???) appear in /WEB- INF/lib. If you start the process at this time, the error described in the title occurs. To resolve this issue, locate all question mark files in the /WEB-INF/lib directory, replace them with an empty JAR package, and then restart the process.

```
touch /home/admin/empty cp /home/admin/empty xxxxx.jar
```

**What to do if the Application Monitoring page does not display**

**content?**

Use Chrome version 42 or later. Issues are known to exist with Chrome versions earlier than 42.

**What to do if an application in Application Monitoring has no**

**monitoring data?**

If an application in Application Monitoring has no monitoring data, perform the following checks:
1. Confirm the status of the Application Monitoring job.
Application Monitoring corresponds to a unique system job in each region. Go to the Monitoring List to check whether the system job is in a normal state. A status of Running indicates that the job is normal.
2. Confirm whether it is an EDAS application.
For an EDAS application that is automatically synchronized by ARMS (meaning the user enabled Application Monitoring for the application in the EDAS console), Arms-Agent is automatically mounted to the application. However, if the application is synchronized through the EDAS database, Arms-Agent is not mounted by default. This results in no monitoring data. To resolve this issue, manually mount Arms-Agent and restart the application.
3. View the target application process and check whether the startup parameters include the
following required parameters:

```
-javaagent:/{user.workspace}/ArmsAgent/arms-bootstrap-1.7.0-SNAPSHOT.jar -Darms.licen seKey=xxxxx -Darms.appId=xxxxx
```

4. Check the Arms-Agent logs for the application startup.
The pid.log file in the ArmsAgent/log directory (for example, a***@46e26bf5be00697.log) contains relevant exception information. Read the file carefully for clues.

**What to do if a custom monitoring job has no data forwarding?**

If a custom monitoring job has no data forwarding, possible reasons include the following: The job status is abnormal The system job has an issue The TLog data collection status is abnormal Perform the following checks:
1. Check the user job's running status.
i. If the user job is not running, no data is ingested, and therefore no data is forwarded. ii. Confirm whether the data source can generate real-time data. If not, you can only find data in the centralized data storage of the custom monitoring job, but no data is forwarded.
2. Check the system job status.
Log on to ARMS as an administrator and check the status of the arms_monitor system job. If the job status is **New**, **Stopped**, or **Paused**, click **Start** in the **Actions** column.
3. Check the status of the data collector for the TLog corresponding to the system job.
Check the status of the data collector for the TLog corresponding to the system job. Go to the arms_cloud01 data collection point in the arms_cloud group and check whether the status in /home/admin/logs/eagleeye/stat-arms_stage.log is **Normal**.
4. Confirm that the Star Agent on the TLog host is normal.
i. Go to the host where the TLogst and JStorm containers are located and run the following command to view the processes.

```python
sudo lsof -i:8182
```

ii. Run the following command to stop all the found processes.

```python
sudo kill -9 <process ID>
```

iii. Wait about 10 seconds, then run the following command again to check if the processes still exist. If they do not, proceed to the next step.

```python
sudo lsof -i:8182
```

iv. Run the following command to enter the HBase container.

```bash
docker ps | grep hbase
```

v. Run the following command to stop the Star Agent.

```
/usr/alisys/dragoon/bin/agent.sh stop
```

vi. Run the following commands to enter the TLogst and JStorm containers respectively.

```python
sudo docker ps | grep jstorm sudo docker ps | grep tlogst
```

vii. In the TLogst and JStorm containers, run the following command to restart the Star Agent.

```
/usr/alisys/dragoon/bin/agent.sh restart
```

Wait a few minutes and return to the ARMS console to check whether data forwarding has returned to normal.

**What to do if you encounter an EDAS username length limit**

**error when syncing EDAS applications?**

When you sync EDAS applications in versions earlier than Shuguang V3.6.1, you may encounter a Username is limited to 20 characters error. Follow these steps to manually modify the frontend JS file to resolve the issue.
1. In the Chrome browser, open the ARMS console home page. Right-click a blank area and
select **View page source**. Find the frontend version number of ARMS. For example, in the following figure, the frontend version number is 1.2.2.
2. Run the following commands to open the frontend JS file for the corresponding version.

> **Note:** Replace `<version>` with the frontend version number found in the previous step (1.2.2 in this example).

```
cd /home/admin/arms_static/arms/<version> vi armsConsole.js
```

3. In the file, search for EDAS user name, delete the length limit `ng-maxlength="20"` , and
save the file.

**How to change the storage duration for Application Monitoring**

**trace data?**

The default storage duration for trace data is 7 days. To change it, locate the biz.properties file in the arms-console container, modify the `trace.store.time` configuration, and then restart the process.

**How to remove the restriction on Application Monitoring charts**

**in interactive dashboards?**

In an Apsara Stack environment, some versions of the interactive dashboard do not allow you to add Application Monitoring charts. Follow these steps to manually modify the frontend JS file to resolve the issue.
1. In the Chrome browser, open the ARMS console home page. Right-click a blank area and
select **View page source**. Find the frontend version number of ARMS. For example, in the following figure, the frontend version number is 1.2.2.
2. Run the following commands to open the frontend JS file for the corresponding version.

> **Note:** Replace `<version>` with the frontend version number found in the previous step (1.2.2 in this example).

```
cd /home/admin/arms_static/arms/<version> vi armsConsole.js
```

3. In the file, search for edb.addChart('appstat'), delete the following restriction, and save the
file.

```
ng-class=\"{disabled:!isCommercial||!isCommercial.traceStatus}\"
```

**How to change the alert cool-down period?**

The default alert cool-down period is 24 hours ( `noc.period.timestamps = 86400000` , in milliseconds). To change it, locate the biz.properties file in the arms-console container, modify the `noc.period.timestamps` configuration, and then restart the process.

**How to find the commitId of ARMS?**

When an issue occurs, you often need to confirm the baseline version. Follow these steps to find the commitId of ARMS.
1. Log on to Apsara Infrastructure Management.
2. In the navigation pane on the left, choose **Resource Management > Product Cluster**
**O&M**. On the **Product Cluster O&M** page, enter `arms` in the **Product | Cluster** search
box. In the **Actions** column of the search result, click **Cluster Details**.
3. On the **Cluster Details** page, click the **Cluster Configurations** tab.
4. On the **Cluster Configurations** tab, click the tag.conf file in the file list on the left. The
value of the `__zhuque_tags_productCommitId` parameter in the file is the commitId you are looking for.

## 8 Upgrade guide

This topic describes important considerations before performing a system upgrade. Typically, the product upgrades automatically with the platform, requiring no additional operations from you. Although manual upgrades are possible for specific requirements, we strongly recommend against them under all circumstances. Manual upgrades can interfere with future automatic upgrades and pose potential threats to business continuity. If you have specific requirements, you can contact Alibaba Cloud on-site personnel to obtain the operation guide for manual upgrades.
