---
title: "Application Real-time Monitoring Service Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20251205"
pdf_pages: 31
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Application Real-time Monitoring Service Operations and Maintenance Guide 20251205.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BA%94%E7%94%A8%E5%AE%9E%E6%97%B6%E7%9B%91%E6%8E%A7%E6%9C%8D%E5%8A%A1%20ARMS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Application%20Real-time%20Monitoring%20Service%20Operations%20and%20Maintenance%20Guide%2020251205.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Application Real-time Monitoring Service Operations and Maintenance Guide

## O&M overview

### System architecture

This topic describes the system architecture of Application Real-Time Monitoring Service (ARMS). Data Query Console API Service TLog-Console Diamond Middware- ZooKeeper TLogst JStorm JStorm Data Aggregation Elasticsearch HBase JStorm Cluster Cluster Cluster Traces Log Collection (StarAgent) Collector Collector Collector Collector Cluster Active Active Active Reporting Reporting Reporting Application Application ARMS ARMS ARMS Application A Agent B Agent Agent In Apsara Stack, ARMS consists of the console and API service. Other services such as core computing and storage are dependent on TLog. For more information, see **Deployment**
**architecture**.

### Deployment architecture

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

### Server role list

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

## High-risk operations

Proceed with caution when performing high-risk operations during O&M tasks. High-risk operations in ARMS O&M are deletion of resources.

**Operation entry**

On the Resource Management page of the ARMS Management Console, you can view all resources used by ARMS. When logged in as an Admin account , you can delete resources on this page.

**Operational impact**

If you delete a resource, the tasks assigned to that resource cannot be automatically or manually stopped. The tasks will continue to run without being affected.

**Operational recommendations**

We recommend that you do not delete resources under any circumstances.

## Routine maintenance

### Log on to the Apsara Uni-

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: regionid.aso.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open a web browser.
2. In the address bar, enter the URL of the Apsara Uni-manager Operations Console in the
format of region-id.aso.intranet-domain-id.com, and press the ENTER key.

**Note**

You can select a language from the drop-down list in the upper-right corner of the page.
3. Enter your username and password.

**Note**

Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, the password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
4. Click **Log In** to log on to the Apsara Uni-manager Operations Console.

### Log on to the Apsara

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: regionid.aso.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open a web browser.
2. In the address bar, enter the URL of the Apsara Uni-manager Operations Console in the
format of region-id.aso.intranet-domain-id.com, and press the ENTER key.
3. Enter your username and password.

**Note**

Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator. You can select a language from the drop-down list in the upper-right corner of the page. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, the password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, move the pointer
over **Platform Operations**.
6. In the **Apsara Infrastructure Management** section, click the module that you want to
access.

### Inspect components

This topic describes common system inspection methods.

**Inspect Diamond**

1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**. On the **Product & Cluster O&M** page, enter
`middleWareAll` in the **Product | Cluster** field, and click **Cluster Details** in the **Actions** column of the cluster that is displayed.
3. On the **Services** tab, enter
`middleWare-jmenv` in the **Service** field. Check whether the instances corresponding to the **middleWare-jmenv** service are normal.

**Inspect HBase**

1. Log on to the Apsara Infrastructure Management console.
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

1. Log on to the Apsara Infrastructure Management console.
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

### Perform O&M operations on

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

## Troubleshooting

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

## Alert handling

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

## Log reference

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

## FAQ

This topic provides answers to some frequently asked questions about the O&M of Application Real-Time Monitoring Service (ARMS).

**How do I query the username and password of the ARMS**

**administrator?**

In some scenarios, the built-in administrator account of ARMS is required. For example, the information about task data flows is generated by monitoring tasks of the ARMS administrator. You can obtain the username and password of the ARMS administrator from a deployment engineer or an on-site administrator. You can also perform the following steps to query the username and password of the ARMS administrator:
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**. On the **Product & Cluster O&M** page, enter
`arms` in the **Product | Cluster** field, and click **Cluster Details** in the **Actions** column of the cluster that is displayed.
3. On the **Cluster Details** page, click the **Resource Details** tab. On the **Resource Details**
tab, find the resource whose type is **accesskey**.
4. Click the icon in the **Resource Application Result** column of the resource and then click
the information that appears. In the **Resource Application Result** dialog box, view the username and password of the ARMS administrator.

**How do I view the Nimbus status?**

1. Run the `jps` command on the Nimbus server to check whether the NimbusServer,
Supervisor, and Worker processes exist.
2. Run the `jstorm list` command to view the Nimbus details.
3. Run the jstorm list | grep "host" | wc -l command to view the topologies that are in
the Active state. If the number of hosts does not match that of nodes in the JStorm cluster, JStorm node containers may be faulty.
4. Run the jstorm list | grep {topo name} command.
If the name of the corresponding collection point in TLog is not found, the topology task of JStorm has stopped running.

**How do I retrieve error information in logs stored in**

**/home/admin/logs?**

1. Run the following command to determine the worker on which an exception was thrown:

```
cat -worker-.log* | grep Exception
```

2. Run the following command to view the Nimbus logs:

```bash
grep 'kill' -A 20 /home/admin/logs/nimbus.log
# You can also use other keywords.
```

3. Run the following command to view the supervisor.log file on all servers, including the
Nimbus server:

```
grep 'dead' -A 20 /home/admin/logs/supervisor.log
```

If an error such as HBase flush failed or HBase write queue full is reported, it can be preliminarily determined that the HBase module is faulty.

**What do I do if an error indicating invalid callback URL is**

**reported during logon?**

If you encounter an error indicating **invalid callback URL** during logon, perform the following steps to resolve the issue:
1. Check whether the back_url value in the address bar of the browser is correct. The
preceding figure shows a typical scenario where the back_url value is incorrect and must be changed to the domain name of ARMS.

**Important**

It is forbidden to access ARMS by using an IP address.
2. If the preceding error still occurs when you access ARMS by using a domain name, check
whether the top-level domain name of DAuth is the same as the top-level domain name of ARMS in the back_url value. Example: same top-level domain name

```
dauth.sgcloud.com arms.console.sgcloud.com
```

Example: different top-level domain names

```
dauth.sgcloud.com arms.console.aliyun.com
```

**Can I use the root account to start arms-console?**

No. Do not use the root account to start arms-console. Otherwise, ARMS becomes unavailable, and the following error information is recorded in localhost.log:

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

**What do I do if the error message Failed to access resource**

**/WEB-INF/lib/.jar is reported during the startup of**

**processes?**

After you delete /WEB-INF/lib and decompress the new package when you manually upgrade arms-console or arms-pop, a large number of files whose names contain question marks (?) appear in /WEB-INF/lib. If a process starts at this time, the error described in the question occurs. To resolve this issue, find all files whose names contain question marks (?) in the /WEB-INF/lib directory, replace them with empty JAR packages, and restart the process.

```
touch /home/admin/empty cp /home/admin/empty xxxxx.jar
```

**What do I do if the page of Application Monitoring does not**

**display any content?**

Use Google Chrome 42 or later. This issue may occur if you use Google Chrome of a version earlier than 42.

**What do I do if no monitoring data is available for applications**

**in Application Monitoring?**

Perform the following steps to troubleshoot this issue:
1. Check whether the status of the application monitoring tasks is normal.
Each section in Application Monitoring corresponds to a unique system task. You can view the status of the system task in the monitoring list. If the task is in the Running state, the task is normal.
2. Check whether the application is an Enterprise Distributed Application Service (EDAS)
application. If you have enabled Application Monitoring for an EDAS application in the EDAS console, ARMS automatically synchronizes the monitoring data of the application, and the ARMS agent is automatically associated with the application. By default, if the monitoring data is synchronized from the EDAS database, the ARMS agent is not associated with the application, resulting in the absence of the monitoring data. To resolve this issue, manually associate the ARMS agent with the application and restart the application.
3. Check whether the startup parameters of the application process include the following
required parameters:

```
-javaagent:/{user.workspace}/ArmsAgent/arms-bootstrap-1.7.0-SNAPSHOT.jar -Darms.licen seKey=xxxxx -Darms.appId=xxxxx
```

4. Check the ARMS agent logs related to application startup.
Log files named in the format of PID.log, such as aokcdqn3ly@46e26bf5be00697.log, in the ArmsAgent/log directory contain relevant exception information. Read these logs for clues.

**What do I do if no monitoring data is forwarded for a custom**

**monitoring task?**

Possible causes: The task status is abnormal. The system task is malfunctioning. The TLog collection status is abnormal. To troubleshoot the issue, perform the following steps:
1. Check the status of the custom monitoring task.
i. If the task is not running, no incoming traffic is produced. As a result, no data is forwarded. ii. Check whether the data source can generate real-time data. If not, data can only be found in the dataset of the custom monitoring task, but no data is forwarded.
2. Check the status of the system task.
Log on to the ARMS console as an administrator and check the status of the system task arms_monitor. If the task is in the **Creating**, **Stopped**, or **Paused** state, click **Start** in the
**Actions** column.
3. Check the status of the TLog collector corresponding to the system task.
Go to the arms_cloud01 collection point in the arms_cloud group, and check whether the status of /home/admin/logs/eagleeye/stat-arms_stage.log is **Normal**.
4. Check whether the StarAgent of the TLog host is normal.
i. Go to the hosts where the TLogst and JStorm containers of TLog reside and run the following command to view the processes:

```python
sudo lsof -i:8182
```

ii. Run the following command to terminate all the processes retrieved in the previous step:

```python
sudo kill -9 <PID>
```

iii. Wait for about 10 seconds, and then run the following command to check whether the processes exist. If not, proceed to the next step.

```python
sudo lsof -i:8182
```

iv. Run the following command to access the HBase container:

```bash
docker ps | grep hbase
```

v. Run the following command to stop the StarAgent:

```
/usr/alisys/dragoon/bin/agent.sh stop
```

vi. Run the following commands to access the JStorm and TLogst containers:

```python
sudo docker ps | grep jstorm sudo docker ps | grep tlogst
```

vii. Run the following command separately in the TLogst and JStorm containers to restart the StarAgent:

```
/usr/alisys/dragoon/bin/agent.sh restart
```

Wait a few minutes and return to the ARMS console to check whether data forwarding is normal.

**What do I do if an error is reported indicating that the EDAS**

**username exceeds the length limit when I synchronize data of**

**an EDAS application?**

When you synchronize data of an EDAS application in Apsara Stack V3.6.1, you may encounter an error indicating that the username cannot exceed 20 characters in length. Perform the following steps to modify the frontend JavaScript file to resolve the issue:
1. Open the homepage of the ARMS console in Google Chrome. Right-click on a blank area of
the page and select **View Page Source**. Find the frontend version of ARMS. For example, in the following figure, the version is 1.2.2.
2. Run the following commands to open the frontend JavaScript file of the corresponding
version:

**Note**

Replace `<version>` with the frontend version found in the previous step, which is 1.2.2 in this example.

```
cd /home/admin/arms_static/arms/<version> vi armsConsole.js
```

3. Search for "EDAS username" in the file, delete the `ng-maxlength="20"` setting that
specifies the length limit, and save the file.

**How do I modify the trace data retention period of Application**

**Monitoring?**

By default, trace data is retained for seven days. To modify the retention period, find the biz.properties file in the arms-console container, modify the setting of `trace.store.time` , and then restart the process.

**How do I remove the limitations on application monitoring**

**charts in an interactive dashboard?**

In Apsara Stack, the interactive dashboards of some versions do not allow you to add application monitoring charts. Perform the following steps to modify the frontend JavaScript file to resolve the issue:
1. Open the homepage of the ARMS console in Chrome. Right-click on a blank area of the page
and select **View Page Source**. Find the frontend version of ARMS. For example, in the following figure, the version is 1.2.2.
2. Run the following commands to open the frontend JavaScript file of the corresponding
version:

**Note**

Replace `<version>` with the frontend version found in the previous step, which is 1.2.2 in this example.

```
cd /home/admin/arms_static/arms/<version> vi armsConsole.js
```

3. Search for "edb.addChart('appstat')" in the file, remove the following restrictive setting, and
save the file:

```
ng-class=\"{disabled:!isCommercial||!isCommercial.traceStatus}\"
```

**How do I modify the alert quiescent period?**

By default, the alert quiescent period is 24 hours based on the setting `noc.period.timestamps` `= 86400000` (in ms). To modify the alert quiescent period, find the biz.properties file in the arms-console container, modify the `noc.period.timestamps` setting, and then restart the process.

**How do I query the commit ID of ARMS?**

If an issue occurs, you usually need to check the baseline version. You can perform the following steps to query the commit ID of ARMS.
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **Resource Management > Product & Cluster**
**O&M**. On the **Product & Cluster O&M** page, enter
`arms` in the **Product | Cluster** field, and click **Cluster Details** in the **Actions** column of the cluster that is displayed.
3. On the **Cluster Details** page, click the **Desired State Configuration** tab.
4. On the **Desired State Configuration** tab, click the tag.conf file in the left-side file list. The
value of `__zhuque_tags_productCommitId` in the file is the commit ID of ARMS.

## Upgrade guide

This topic describes important considerations before performing a system upgrade. Typically, the product upgrades automatically with the platform, requiring no additional operations from you. Although manual upgrades are possible for specific requirements, we strongly recommend against them under all circumstances. Manual upgrades can interfere with future automatic upgrades and pose potential threats to business continuity. If you have specific requirements, you can contact Alibaba Cloud on-site personnel to obtain the operation guide for manual upgrades.
