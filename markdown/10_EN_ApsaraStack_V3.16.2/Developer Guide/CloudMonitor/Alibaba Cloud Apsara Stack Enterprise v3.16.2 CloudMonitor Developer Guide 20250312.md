---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 CloudMonitor Developer Guide"
product_version: "V3.16.2"
doc_version: "20250312"
pdf_pages: 174
source_pdf: "288b8545e01fe1c4_Alibaba Cloud Apsara Stack Enterprise v3.16.2 CloudMonitor Developer Guide 20250312.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%91%E6%8E%A7CMS/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20CloudMonitor%20Developer%20Guide%2020250312.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 CloudMonitor Developer Guide

## Table of Contents

- 1 CloudMonitor API Reference
  - 1.1 Common parameters
  - 1.2 Metrics for Apsara Stack services
  - 1.3 API Reference
    - 1.3.1 Cloud Products
      - 1.3.1.1 DescribeProjectMeta
      - 1.3.1.2 DescribeMetricLast
      - 1.3.1.3 DescribeMetricList
      - 1.3.1.4 DescribeMetricMetaList
    - 1.3.2 Threshold-triggered alert rules
      - 1.3.2.1 DescribeMetricRuleList
      - 1.3.2.2 PutResourceMetricRule
      - 1.3.2.3 DescribeMetricRuleCount
      - 1.3.2.4 DeleteMetricRules
      - 1.3.2.5 EnableMetricRules
      - 1.3.2.6 DisableMetricRules
      - 1.3.2.7 DescribeAlertingMetricRuleResources
      - 1.3.2.8 DeleteMetricRuleResources
      - 1.3.2.9 DescribeAlertHistoryList

## 1 CloudMonitor API Reference

**Reference**

### 1.1 Common parameters

**Common request parameters**

Common request parameters must be included in all API requests of the Apsara Uni-manager Management Console. Table 1: Common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. For more information, see Obtain API information. |
| Product | Strin g | Yes | The name of the service to which the API operation belongs. Set the value to Cms. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Example: 2019-01-01. |
| RegionId | Strin g | Yes | The region ID. For more information, see the Obtain a region ID section of the Obtain the values of common request headers topic. |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is used to access the service. For more information, see Obtain AccessKey credentials. |
| Signature | Strin g | Yes | The signature string. For more information, see Signature method. |
| SignatureMe thod | Strin g | Yes | The algorithm that is used to encrypt the signature string. Valid values: HMAC-SHA1 and HMAC-SHA256. |
| SignatureVer sion | Strin g | Yes | The version of the algorithm that is used to encrypt the signature string. Valid values: 1.0 and 2.0. |
| SignatureNo nce | Strin g | Yes | A unique and random number that is used to prevent replay attacks. We recommend that you use different numbers for different requests. |
| Timestamp | Strin g | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01-01T12:00:00Z. |
| Format | Strin g | No | The format of the response. Set the value to JSON. |

The Signature, SignatureMethod, SignatureVersion, SignatureNonce, Timestamp, and Format parameters are encapsulated into the SDK. You do not need to specify these parameters. To obtain the values of the `Product` and `Version` parameters in the Apsara Uni-manager Management Console, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Others > API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. In the **Search by operation name** search box, enter the name of an operation to query its
information.

**Common request headers**

| Header | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information, see the Obtain an organization ID section of the Obtain the values of common request headers topic. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information, see the Obtain a resource set ID section of the Obtain the values of common request headers topic. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. For more information, see the Obtain an instance ID section of the Obtain the values of common request headers topic. |

When you call the API operations of cloud services, you must specify the **x-**
**acs-organizationid**, **x-acs-resourcegroupid**, and **x-acs-instanceid** headers to
identify the instance on which you want to perform the operation, and the organization and resource set to which the instance belongs. If you call an API operation to create an instance or query the information about one or more instances, you do not need to specify the x-acs-instanceid header. If you do not specify the request headers when you call an API operation, the root organization and root resource set are used by default.

**Common response parameters**

Responses are returned in the unified format for API requests. The following HTTP status code indicates the request status: 2xx: indicates that the request is successful. 4xx or 5xx: indicates that the request failed. Responses are returned in the JSON format. Each response returns a unique request ID regardless of whether the request is successful.

### 1.2 Metrics for Apsara Stack services

**services**

This topic describes the metrics supported by each service.

**Usage notes**

You can call CloudMonitor API operations to query metric data within the last 31 days. The value of the **Dimensions** parameter is a JSON string in the format of `{"instanceId":"`

```
<Instance ID of an Apsara Stack service>"} .
```

When you call an API operation provided by CloudMonitor, you must specify the
**Namespace** and **Period** parameters.

**ECS**

**Basic metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds. The metrics described in the following table are collected from the virtual host layer and are slightly different from metrics collected in the operating system.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS) CPU Utilization | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| (ECS)InternetInRa te(Classic Network) | Bit/s | InternetInRate | userId and instanceId | The rate of inbound traffic over the Internet. |
| (ECS)IntranetInRa te | Bit/s | IntranetInRate | userId and instanceId | The rate of inbound traffic over the intranet. |
| (ECS)InternetOut Rate(Classic Network) | Bit/s | InternetOutRate | userId and instanceId | The rate of outbound traffic over the Internet. |
| (ECS)IntranetOut Rate | Bit/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic over the intranet. |
| (ECS)DiskReadBP S | Bytes/s | DiskReadBPS | userId and instanceId | The number of bytes read from all disks per second. |
| (ECS)DiskWriteBP S | Bytes/s | DiskWriteBPS | userId and instanceId | The number of bytes written to all disks per second. |

| (ECS)DiskReadIO PS | Count/s | DiskReadIOPS | userId and instanceId | The number of read I/O operations per second (IOPS) of all disks. |
|---|---|---|---|---|
| (ECS)DiskWriteIO PS | Count/s | DiskWriteIOPS | userId and instanceId | The number of write IOPS of all disks. |

**Operating system-related metrics**

To collect operating system-related metrics of Elastic Compute Service (ECS) instances, you must install a monitoring plug-in. To install a monitoring plug-in, perform the following operations: In the left-side navigation pane of the CloudMonitor console, click Cloud Service Monitoring. On the Cloud product monitoring page, click **ECS**. On the **Host monitoring** page, select the instances that you want to monitor and click **Bulk install or upgrade**
**plug-ins** below the instance list.
Metric data is displayed in the monitoring chart in 5 to 10 minutes after the monitoring plug-in is installed. Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 15. Default value: 15. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)cpu.total | % | cpu total _ | userId and instanceId | The CPU utilization. |
| (Agent)memory.u sed.utilization | % | memory usedutilization _ | userId and instanceId | The memory usage. |
| (Agent)load.15m | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |

| (Agent)load.1m | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |
|---|---|---|---|---|
| (Agent)load.5m | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
| Host.diskusage.ut ilization | % | diskusage utilization _ | userId, instanceId, and device | The disk usage. |
| (Agent)fs.inode.u tilization device _ | % | fs inodeutilization _ | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |
| (Agent)disk.read. bps device _ | Byte s/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |
| (Agent)disk.read.i ops device _ | Coun t/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |

| (Agent)disk.write. bps device _ | Byte s/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
|---|---|---|---|---|
| (Agent)disk.write. iops device _ | Coun t/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent)network.t cp.connection st _ ate | Coun t | net tcpconnection _ | userId, instanceId, and state | The number of TCP connections in each state. |
| (Agent)process.e xpend pid _ | N/A | process.expend | userId, instanceId, name, and pid | The detailed statistical metrics for the top 5 processes. |
| (Agent)process.c ount processnam _ e | Coun t | process.number | userId, instanceId, and processName | The number of matched processes. |
| io saturation | % | disk io util _ _ | userId, instanceId, and device | The I/O saturation. |
| Agent(zombie pr _ ocess number) _ | Coun t | zombieProcessNumber | userId and instanceId | The total number of zombie processes. |
| Agent(total proce _ ss number) _ | Coun t | totalProcessNumber | userId and instanceId | The total number of processes. |
| Agent(swap parti _ tion usage) _ | % | swapUtilization | userId and instanceId | The usage of the swap partition. |
| Agent(networkou t drop ratio) _ _ | % | networkout drop ratio _ _ | userId, instanceId, and device | The loss rate of packets that are sent by network interface controllers (NICs). |
| Agent(networkou t error ratio) _ _ | % | networkout error ratio _ _ | userId, instanceId, and device | The sending error rate of NICs. |

| Agent(networkin _ drop ratio) _ | % | networkin drop ratio _ _ | userId, instanceId, and device | The loss rate of packets that are received by NICs. |
|---|---|---|---|---|
| Agent(networkin _ error ratio) _ | % | networkin error ratio _ _ | userId, instanceId, and device | The receiving error rate of NICs. |

**Disk-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 15. Default value: 15. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Descriptio n |
|---|---|---|---|---|
| Total Disk Space | GB | DiskSerialTotal | userId, instanceId, and id serial _ | The total capacity of disks. |
| Disk Space Used | GB | DiskSerialUsed | userId, instanceId, and id serial _ | The used disk capacity. |
| (Agent) Percentage of cloud disk usage | % | DiskSerialUsePercent | userId, instanceId, and id serial _ | The percentage of used disk capacity. |
| Free Disk Space | GB | DiskSerialFree | userId, instanceId, and id serial _ | The available disk capacity. |

**GPU-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| > Document Version: 20250 | 312 |   |   | 1 |
|---|---|---|---|---|

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)gpu.decoder.utiliz ation gpuid _ | % | gpu decoder utilizat _ _ ion | userId, instanceId, and gpuId | The decoder usage of a GPU. |
| (Agent)gpu.encoder.utiliz ation gpuid _ | % | gpu encoder utilizat _ _ ion | userId, instanceId, and gpuId | The encoder usage of a GPU. |
| (Agent)gpu.temperature _ gpuid | °C | gpu gpu temperatur _ _ e | userId, instanceId, and gpuId | The GPU temperature. |
| (Agent)gpu.usedutilizatio n gpuid _ | % | gpu gpu usedutiliza _ _ tion | userId, instanceId, and gpuId | The GPU utilization. |
| (Agent)gpu.memory.free. space gpuid _ | Bytes | gpu memory freesp _ _ ace | userId, instanceId, and gpuId | The idle video memory of a GPU. |
| (Agent)gpu.memory.free. utilization gpuid _ | % | gpu memory freeuti _ _ lization | userId, instanceId, and gpuId | The percentage of the idle video memory of a GPU. |
| (Agent)gpu.memory.used .space gpuid _ | Bytes | gpu memory useds _ _ pace | userId, instanceId, and gpuId | The used video memory of a GPU. |
| gpu memory usedutilizat _ _ ion | % | gpu memory usedut _ _ ilization | userId, instanceId, and gpuId | The video memory usage of a GPU. |
| (Agent)gpu.power.readin gspowerdraw gpuid _ | W | gpu power readings _ _ power draw _ _ | userId, instanceId, and gpuId | The GPU power. |

**ApsaraDB RDS**

By default, an old link is used for ApsaraDB RDS. ApsaraDB RDS supports four types of engines: MySQL, SQL Server, PolarDB, and PostgreSQL.

**ApsaraDB RDS for MySQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| NetworkInRate | Bit/s | MySQL NetworkI _ nNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| NetworkOutRate | Bit/s | MySQL NetworkO _ utNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS _ | Count/s | MySQL QPS _ | userId and instanceId | The number of QPS of the ApsaraDB RDS for MySQL instance. |

| Docker Cpu Usage | % | DockerCpuUsage | userId and instanceId | The CPU usage of the database proxy. |
|---|---|---|---|---|

**ApsaraDB RDS for SQL Server**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| NetworkInRate | Bit/s | SQLServer Netw _ orkInNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for SQL Server instance per second. |
| NetworkOutRate | Bit/s | SQLServer Netw _ orkOutNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for SQL Server instance per second. |

**ApsaraDB RDS for PolarDB**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilization | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsU tilization | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilizatio n | % | DiskUsage | userId and instanceId | The disk usage. |

| IOPSUtilizatio n | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
|---|---|---|---|---|
| MemoryUtiliz ation | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average active connections per CPU PG cloud disk _ | Count | ActiveConnections | userId and instanceId | The average number of active connections per CPU. |
| Inode Usage PG _ Disk | % | InodeUsage | userId and instanceId | The Inode usage. |
| Read-only synchronization delay PG cloud _ disk | Second s | ReadLag | userId and instanceId | The synchronization latency of the read-only instance. |
| Database Age PG _ Disk | xids | DBAge | userId and instanceId | The age of the database. |
| Read-only Stream replication state pg cloud _ disk | Value | StreamingStatus | userId and instanceId | The stream replication status of the read-only instance. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| Pg disk space _ usage | % | local fs size usage _ _ _ | userId and instanceId | The disk usage. |

| PG Memory Usage _ | % | mem usage _ | userId and instanceId | The memory usage. |
|---|---|---|---|---|

**ApsaraDB RDS (New)**

ApsaraDB RDS also supports a new link. Data is collected at 60-second intervals. ApsaraDB RDS (New) supports three types of engines: MySQL, PolarDB, and PostgreSQL.

**ApsaraDB RDS for MySQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL NetworkInNew _ _ new | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |

| MySQL Network outflow bandwidth (new) | Bit/s | MySQL NetworkOutNew _ new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
|---|---|---|---|---|
| MySQL queries per second (new) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second for the ApsaraDB RDS for MySQL instance. |
| DataDelay | Second s | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
| RWDelay (New) | Second | RWDelay | userId, instanceId, and slave | The read and write latency. |
| ThreadsConnected | Count | ThreadsConnected | userId and instanceId | The number of thread connections. |
| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
| SlowQueriesPs | Count | SlowQueriesPs | userId and instanceId | The number of slow queries per second. |
| Total Wait Time for Row Locks (New) | Millisec onds | InnodbRowLockTime | userId and instanceId | The total wait time for row locks. |
| Average Wait Time for Row Locks (New) | Millisec onds | InnodbRowLockTimeAv g | userId and instanceId | The average wait time for row locks. |
| Row Lock Waits (New) | Count | InnodbRowLockWaits | userId and instanceId | The number of wait times for row locks. |

| Total Number of Connections (New) | Count | TotalConnections | userId and instanceId | The total number of connections. |
|---|---|---|---|---|
| Average number of active MySQL connections | Count | MySQL ActiveSession _ | userId and instanceId | The average number of active connections to the ApsaraDB for MySQL instance. |
| Innodb row lock cu _ _ _ rrent waits _ | Count | Innodb row lock curre _ _ _ nt waits _ | userId and instanceId | The number of sessions that are waiting for row locks. |
| mdl lock session _ _ | Count | mdl lock session _ _ | userId and instanceId | The number of connections blocked by metadata locks (MDLs). |
| lock deadlocks _ | Count | lock deadlocks _ | userId and instanceId | The number of deadlocks. |

**ApsaraDB RDS for PolarDB**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |

| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
|---|---|---|---|---|
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| PPAS Primary/Standby Disconnect | Count | PPAS ReplicationNum _ | userId and instanceId | The number of disconnection s between primary and secondary ApsaraDB RDS for PPAS instances. 1: The primary and secondary ApsaraDB RDS for PPAS instances are connected. 0: The primary and secondary ApsaraDB RDS for PPAS instances are disconnecte d. |
| PPAS primary/standby delay | Seconds | PPAS ReplicationLag _ | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PPAS instances. |

| PG ActiveConnect _ ionsPerCpu | Count | PG ActiveConnections _ PerCpu | userId and instanceId | The average number of active connections per core to the PolarDB for Oracle Enterprise Edition database that uses local disks. |
|---|---|---|---|---|
| PG Database age _ | xids | PG O DBAge _ _ | userId and instanceId | The age of the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
| PG SwellTime _ | Seconds | PG SwellTime _ | userId and instanceId | The period during which the PolarDB for Oracle Enterprise Edition database that uses local SSDs experiences storage bloat. |
| PG CheckpointLat _ encyMB | MB | PG CheckpointLatency _ MB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay during a checkpoint process. |

| PG InactiveSlots _ | Count | PG InactiveSlots _ | userId and instanceId | The number of times that the replication slot is disconnected in the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
|---|---|---|---|---|
| PG ReplayLatency _ InMB | MB | PG ReplayLatencyInM _ B | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay. |

**ApsaraDB RDS for PostgreSQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage ne _ w | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |

| Memory usage (new) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| PG primary/standby disconnection | Count | PG ReplicationNum _ | userId and instanceId | The number of connections between the primary and secondary ApsaraDB RDS for PostgreSQL instances. 1: The primary and secondary ApsaraDB RDS for PostgreSQL instances are connected. 0: The primary and secondary ApsaraDB RDS for PostgreSQL instances are disconnecte d. |
| PG primary/standby delay | Seconds | PG ReplicationLag _ | userId and instanceId | The latency between the primary and secondary ApsaraDB RDS for PostgreSQL instances. |

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average number of active connections per CPU PG cloud _ disk (new) | Count | ActiveConnections ne _ w | userId and instanceId | The average number of active connections per CPU. |

| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| INODE usage PG _ cloud disk (new) | % | InodeUsage new _ | userId and instanceId | The inode usage. |
| Pg disk space _ usage | % | local fs size usage _ _ _ | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |
| Read-only synchronization delay PG cloud _ disk (new) | Second s | ReadLag new _ | userId and instanceId | The synchronization latency of the read-only instance. |
| Database age PG _ cloud disk (new) | xids | DBAge new _ | userId and instanceId | The age of the database. |
| Read-only Stream Copy Status PG _ Cloud Disk (New) | Value | StreamingStatus new _ | userId and instanceId | The streaming replication status of the read-only instance. |

| Number of Primary/Secondar y Connections (Value 0 indicates disconnected. Value 1 indicates connected.) | Count | PG ESSD ReplicationN _ _ um | userId and instanceId | The number connections between the primary and secondary ApsaraDB RDS for PostgreSQL instances. 1: The primary and secondary ApsaraDB RDS for PostgreSQL instances are connected. 0: The primary and secondary ApsaraDB RDS for PostgreSQL instances are disconnected . |
|---|---|---|---|---|
| PG cloud disk primary/stan _ dby delay | Second s | PG ESSD ReplicationL _ _ ag | userId and instanceId | The latency between primary and secondary ApsaraDB RDS for PostgreSQL instances. |

**SLB**

Set the **Namespace** parameter to **acs_slb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceActiveCo nnection | Count | InstanceActiveConnec tion | userId, instanceId, and protocol | The number of active TCP connections. |

| InstanceInactiveC onnection | Count | InstanceInactiveConn ection | userId, instanceId, and protocol | The number of inactive connections on the port. |
|---|---|---|---|---|
| InstanceDropCon nection | Count/s | InstanceDropConnecti on | userId, instanceId, and protocol | The number of connections dropped from the listener per second. |
| InstancecDropTra fficRX | Bit/s | InstanceDropTrafficRX | userId, instanceId, and protocol | The number of inbound bits dropped from the listener per second. |
| InstanceDropTraf ficTX | Bit/s | InstanceDropTrafficTX | userId, instanceId, and protocol | The number of outbound bits dropped from the listener per second. |
| InstanceDropPac ketRX | Count/s | InstanceDropPacketR X | userId, instanceId, and protocol | The number of inbound packets dropped per second on an instance. |
| InstanceDropPac ketRX | Count/s | InstanceDropPacketT X | userId, instanceId, and protocol | The number of outbound packets dropped per second on an instance. |
| InstanceMaxConn ection | Count/s | InstanceMaxConnecti on | userId, instanceId, and protocol | The number of concurrent connections per second on the port. |
| InstanceNewCon nection | Count | InstanceNewConnecti on | userId, instanceId, and protocol | The number of new TCP connections. |
| InstancePacketR X | Count/s | InstancePacketRX | userId, instanceId, and protocol | The number of inbound packets per second. |

| InstancePacketTX | Count/s | InstancePacketTX | userId, instanceId, and protocol | The number of outbound packets per second. |
|---|---|---|---|---|
| InternetInRate | Bit/s | InstanceTrafficRXNew | userId, instanceId, and protocol | The inbound bandwidth. |
| InternetOutRate | Bit/s | InstanceTrafficTXNew | userId, instanceId, and protocol | The outbound bandwidth. |
| HealthyServerCo unt | Count | InstanceHeathyServer Count | userId, instanceId, port, and vip | The number of normal ECS instances that are added as backend servers. |
| UnhealthyServer Count | Count | InstanceUnhealthySer verCount | userId, instanceId, port, and vip | The number of abnormal ECS instances that are added as backend servers. |
| Sum of inflow bandwidth | Bit/s | InstanceTrafficRXNew SUM _ | userId, instanceId, and protocol | The total inbound bandwidth. |
| Sum of outflow bandwidth | Bit/s | InstanceTrafficTXNew SUM _ | userId, instanceId, and protocol | The total outbound bandwidth. |
| Seven-layer instance Qps | Request s/s | InstanceSevenFloorQp s | userId and instanceId | The QPS at Layer 7. |
| InstanceFailConn ection | Count | InstanceFailConnectio n | userId and instanceId | The number of failed connections to the instance per second. |
| Instance Layer -7 Back-end Health Check Failure Rate | % | InstanceSeventhFloor UnhealthyServerRate | userId, instanceId, and rip | The percentage of backend ECS instances that fail to pass the health check at Layer 7. |

| QPS usage of seven-tier instances | % | InstanceSevenFloorQp sRate | userId and instanceId | The QPS usage of the instance at Layer 7. |
|---|---|---|---|---|
| Maximum instance connections usage | % | InstanceMaxConnecti onRate | userId and instanceId | The maximum connection utilization of the instance. |

**Port-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| TCPActiveConnec tion | Count | ActiveConnection | userId, instanceId, port, and protocol | The number of active TCP connections per second. |
| TCPInactiveConn ection | Count | InactiveConnecti on | userId, instanceId, port, and protocol | The number of inactive TCP connections. |
| DropConnection | Count/s | DropConnection | userId, instanceId, port, and protocol | The number of connections dropped from the listener per second. |
| DropTrafficRX | Bit/s | DropTrafficRX | userId, instanceId, port, and protocol | The number of inbound bits dropped from the listener per second. |
| DropTrafficTX | Bit/s | DropTrafficTX | userId, instanceId, port, and protocol | The number of outbound bits dropped from the listener per second. |
| DropPacketRX | Count/s | DropPacketRX | userId, instanceId, port, and protocol | The number of inbound packets that are dropped per second. |
| DropPacketTX | Count/s | DropPacketTX | userId, instanceId, port, and protocol | The number of outbound packets that are lost per second. |

| MaxConnection | Count/s | MaxConnection | userId, instanceId, port, and protocol | The number of concurrent connections to the TCP port per second. |
|---|---|---|---|---|
| TCPNewConnecti on | Count | NewConnection | userId, instanceId, port, and protocol | The number of new TCP connections. |
| PacketInPerSecon d | Count/s | PacketRX | userId, instanceId, port, and protocol | The number of inbound packets per second. |
| PacketOutPerSec ond | Count/s | PacketTX | userId, instanceId, port, and protocol | The number of outbound packets per second. |
| IntranetInRate | Bit/s | TrafficRXNew | userId, instanceId, port, and protocol | The inbound bandwidth. |
| IntranetOutRate | Bit/s | TrafficTXNew | userId, instanceId, port, and protocol | The outbound bandwidth. |
| HealthyServerCo unt | Count | HeathyServerCou nt | userId, instanceId, port, and vip | The number of normal ECS instances that are added as backend servers. |
| UnhealthyServer Count | Count | UnhealthyServer Count | userId, instanceId, port, and vip | The number of abnormal ECS instances that are added as backend servers. |
| Port inflow bandwidth sum | Bit/s | TrafficRXNew SU _ M | userId, instanceId, port, and protocol | The total inbound bandwidth. |
| Port outflow bandwidth sum | Bit/s | TrafficTXNew SU _ M | userId, instanceId, port, and protocol | The total outbound bandwidth. |

| Seven layers Qps | Requests/s | SevenFloorQps | userId, instanceId, and port | The number of queries per second at Layer 7. |
|---|---|---|---|---|
| Number of connection failures per second | Count | FailConnection | userId, instanceId, and port | The number of failed connections per second. |
| Failure rate of seven-tier back- end health check | % | SeventhFloorUnh ealthyServerRate | userId, instanceId, port, and vip | The percentage of backend ECS instances that fail to pass the health check at Layer 7. |

**OSS**

Set the **Namespace** parameter to **acs_oss_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Overview**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |
| The number of valid requests. | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |
| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Bytes | InternetSend | userId and BucketName | The outbound traffic over the Internet. |

| InternetRecv | Bytes | InternetRecv | userId and BucketName | The inbound traffic over the Internet. |
|---|---|---|---|---|
| IntranetSend | Bytes | IntranetSend | userId and BucketName | The outbound traffic over the intranet. |
| IntranetRecv | Bytes | IntranetRecv | userId and BucketName | The inbound traffic over the intranet. |
| CDNSend | Bytes | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CDNRecv | Bytes | CdnRecv | userId and BucketName | The CDN inbound traffic. |
| SyncSend | Bytes | SyncSend | userId and BucketName | The outbound traffic that is generated when you use the cross-region replication feature. |
| SyncRecv | Bytes | SyncRecv | userId and BucketName | The inbound traffic that is generated when you use the cross-region replication feature. |
| MeteringStorage Utilization | Bytes | MeteringStorage Utilization | userId and BucketName | The size of the storage in use. |
| Storage Size (GB) | GB | MeteringStorage UtilizationGB | userId and BucketName | The storage size. |
| Storage Usage | % | MeteringStorage UtilizationPercent | userId and BucketName | The storage usage. |

**Request status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ServerErrorCount | Count | ServerErrorCount | userId and BucketName | The number of requests with a server error. |
| ServerErrorRate | % | ServerErrorRate | userId and BucketName | The ratio of requests with a server error. |
| NetworkErrorCou nt | Count | NetworkErrorCou nt | userId and BucketName | The number of requests with a network error. |
| NetworkErrorRate | % | NetworkErrorRat e | userId and BucketName | The ratio of requests with a network error. |
| AuthorizationErro rCount | Count | AuthorizationErro rCount | userId and BucketName | The number of requests with an authorization error. |
| ResourceNotFoun dErrorCount | Count | ResourceNotFoun dErrorCount | userId and BucketName | The number of requests with an error indicating that resources cannot be found. |
| ClientTimeoutErr orCount | Count | ClientTimeoutErr orCount | userId and BucketName | The number of requests with a client timeout error. |
| ClientOtherErrorC ount | Count | ClientOtherError Count | userId and BucketName | The number of requests with other client errors. |
| AuthorizationErro rRate | % | AuthorizationErro rRate | userId and BucketName | The ratio of requests with an authorization error. |

| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error indicating that resources cannot be found. |
|---|---|---|---|---|
| Client Timeout Error Request Proportion | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | % | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The total number of successful requests. |
| RedirectCount | Count | RedirectCount | userId and BucketName | The total number of redirect requests. |
| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |
| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirected requests. |

**Maximum latency-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum end-to-end (E2E) latency of GetObject requests. |
| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |

| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
|---|---|---|---|---|
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPostObjectE2 eLatency | Milliseconds | MaxPostObjectE2 eLatency | userId and BucketName | MaxPostObjectE2 eLatency |
| MaxPostObjectSe rverLatency | Milliseconds | MaxPostObjectSe rverLatency | userId and BucketName | The maximum server latency of PostObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |
| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |

| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |
|---|---|---|---|---|
| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |

**Metrics related to successful requests of different types**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GetObjectCount | Count | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PutObjectCount | Count | PutObjectCount | userId and BucketName | The number of successful PutObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |
| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |

| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |
|---|---|---|---|---|
| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

**ApsaraDB for Redis (Old)**

Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| Failed Operations | Count | FailedCount | userId and instanceId | The number of failed operations. |
| Cache Inbound Bandwidth | Bytes/s | IntranetIn | userId and instanceId | The inbound traffic over the intranet. |
| Inbound Bandwidth Usage | % | IntranetInRatio | userId and instanceId | The inbound bandwidth usage. |
| Cache Outbound Bandwidth | Bytes/s | IntranetOut | userId and instanceId | The outbound traffic over the intranet. |

| Outbound Bandwidth Usage | % | IntranetOutRatio | userId and instanceId | The outbound bandwidth usage. |
|---|---|---|---|---|
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| Used QPS | Count/s | UsedQPS | userId and instanceId | The number of used QPS. |

**ApsaraDB for Redis (New)**

Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**ApsaraDB for Redis Standard Edition instances and ApsaraDB for Redis**

**Read/write splitting instances**

ApsaraDB for Redis Standard Edition instances and ApsaraDB for Redis Read/write splitting instances share a set of metrics.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Standard Edition) | % | StandardConnec tionUsage | userId and instanceId | The connection utilization. |
| Incoming Bandwidth (Standard Edition) | Kbit/s | StandardIntranet In | userId and instanceId | The inbound bandwidth. |
| Incoming Bandwidth Utilization (Standard Edition) | % | StandardIntranet InRatio | userId and instanceId | The inbound bandwidth usage. |
| Outgoing Bandwidth (Standard Edition) | Kbit/s | StandardIntranet Out | userId and instanceId | The outbound bandwidth. |

| Outgoing Bandwidth Usage (Standard Edition) | % | StandardIntranet OutRatio | userId and instanceId | The outbound bandwidth usage. |
|---|---|---|---|---|
| Memory Usage (Standard Edition) | % | StandardMemory Usage | userId and instanceId | The memory usage. |
| QPS usage (standard version) | % | StandardQPSUsa ge | userId and instanceId | The QPS usage. |
| CPU usage (standard edition) | % | StandardCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average Visits Per Second (Standard Edition) | Count/s | StandardUsedQP S | userId and instanceId | The average QPS. |
| Total QPS (Standard Edition) | Count/s | StandardTotalQp s | userId and instanceId | The total QPS. |
| Current Total Connections (Standard Edition) | Count | StandardTotalCo nnections | userId and instanceId | The total number of connections. |
| Used Connection | Count | StandardUsedCo nnection | userId and instanceId | The number of active connections. |
| Average Response Time (Standard Edition) | Milliseconds | StandardAvgRt | userId and instanceId | The average response time. |
| Data Node Hit Ratio (Standard Edition) | % | StandardHitRate | userId and instanceId | The hit rate. |

**ApsaraDB for Redis instances that use the cluster architecture**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Connection Usage (Cluster Edition) | % | ShardingConnect ionUsage | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| Incoming Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranetI n | userId and instanceId | The inbound bandwidth. |
| Outgoing Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranet Out | userId and instanceId | The outbound bandwidth. |
| Incoming Bandwidth Usage (Cluster Edition) | % | ShardingIntranetI nRatio | userId and instanceId | The inbound bandwidth usage. |
| Outgoing Bandwidth Usage (Cluster Edition) | % | ShardingIntranet OutRatio | userId and instanceId | The outbound bandwidth usage. |
| Memory Usage (Cluster Edition) | % | ShardingMemory Usage | userId and instanceId | The memory usage. |
| QPS usage (cluster version) | % | ShardingQPSUsa ge | userId and instanceId | The QPS usage. |
| CPU usage (Cluster Edition) | % | ShardingCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average visits per second (cluster version) | Count/s | ShardingUsedQP S | userId and instanceId | The average QPS. |
| Total QPS (cluster version) | Count/s | ShardingTotalQp s | userId and instanceId | The total QPS. |
| Total Current Connections (Cluster Edition) | Count | ShardingTotalCo nnections | userId and instanceId | The total number of connections. |
| Used Connection | Count | ShardingUsedCo nnection | userId and instanceId | The number of active connections. |
| Average Response Time (Cluster Edition) | Millisec onds | ShardingAvgRt | userId and instanceId | The average response time. |

| Data Node Hit Ratio (Cluster Edition) | % | ShardingHitRate | userId and instanceId | The hit rate. |
|---|---|---|---|---|

**Cluster Edition - Node**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Node) | % | NodeConnection Usage | userId, instanceId, and nodeId | The connection utilization. |
| Incoming Bandwidth (Node) | Kbit/s | NodeIntranetIn | userId, instanceId, and nodeId | The inbound bandwidth. |
| Outgoing Bandwidth (Node) | Kbit/s | NodeIntranetOut | userId, instanceId, and nodeId | The outbound bandwidth. |
| Incoming Bandwidth Utilization (Node) | % | NodeIntranetInR atio | userId, instanceId, and nodeId | The inbound bandwidth usage. |
| Outgoing Bandwidth Utilization (Node) | % | NodeIntranetOut Ratio | userId, instanceId, and nodeId | The outbound bandwidth usage. |
| Memory Usage (Node) | % | NodeMemoryUs age | userId, instanceId, and nodeId | The memory usage. |
| QPS usage (node) | % | NodeQPSUsage | userId, instanceId, and nodeId | The QPS usage. |
| CPU usage (node) | % | NodeCpuUsage | userId, instanceId, and nodeId | The CPU utilization. |
| Average Visits Per Second (Node) | Count/s | NodeUsedQPS | userId, instanceId, and nodeId | The average QPS. |

| Total QPS (nodes) | Count/s | NodeTotalQps | userId, instanceId, and nodeId | The total QPS. |
|---|---|---|---|---|
| Total Current Connections (Nodes) | Count | NodeTotalConne ctions | userId, instanceId, and nodeId | The total number of connections. |
| Used Connection | Count | NodeUsedConne ction | userId, instanceId, and nodeId | The number of active connections. |
| Average response time | Millisecond s | NodeAvgRt | userId and instanceId | The average response time. |
| Hit rate | % | NodeHitRate | userId and instanceId | The hit rate. |

**ApsaraDB for MongoDB (Old)**

Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU Utilization | % | CPUUtilization | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n | % | MemoryUtilizatio n | userId, instanceId, and role | The memory usage. |
| DiskUtilization | % | DiskUtilization | userId, instanceId, and role | The disk usage. |
| IOPS Usage | % | IOPSUtilization | userId, instanceId, and role | The IOPS usage. |

| Connection Usage | % | ConnectionUtiliza tion | userId, instanceId, and role | The connection utilization. |
|---|---|---|---|---|
| QPS | Count | QPS | userId, instanceId, and role | The number of requests per second. |
| UsedConnections | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

**Disk-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceUsedDisk Space | Bytes | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |
| LogUsedDiskSpac e | Bytes | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
| Disk Space Occupied by Logs | Bytes | LogDiskAmount | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IntranetIn | Bytes | IntranetIn | userId, instanceId, and role | The inbound traffic over the intranet. |
| IntranetOut | Bytes | IntranetOut | userId, instanceId, and role | The outbound traffic over the intranet. |
| Requests | Count | NumberRequests | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| OpCounters for Command | Count | OpCommand | userId, instanceId, and role | The number of Command operations. |
| OpCounters for Delete | Count | OpDelete | userId, instanceId, and role | The number of Delete operations. |
| OpCounters for Getmore | Count | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpCounters for Insert | Count | OpInsert | userId, instanceId, and role | The number of Insert operations. |
| OpCounters for Query | Count | OpQuery | userId, instanceId, and role | The number of Query operations. |
| OpCounters for Update | Count | OpUpdate | userId, instanceId, and role | The number of Update operations. |

**ApsaraDB for MongoDB (New)**

Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPUUtilization ne _ w | % | CPUUtilization ne _ w | userId, instanceId, and role | The CPU utilization. |

| MemoryUtilizatio n new _ | % | MemoryUtilizatio n new _ | userId, instanceId, and role | The memory usage. |
|---|---|---|---|---|
| Disk Usage (New) | % | DiskUtilization n _ ew | userId, instanceId, and role | The disk usage. |
| IOPS usage (new) | % | IOPSUtilization n _ ew | userId, instanceId, and role | The IOPS usage. |
| Connection Usage (New) | % | ConnectionUtiliza tion new _ | userId, instanceId, and role | The connection utilization. |
| Visits per second (new) | Count | QPS new _ | userId, instanceId, and role | The number of requests per second. |
| Connection Usage (New) | Count | ConnectionAmou nt new _ | userId, instanceId, and role | The number of used connections. |
| Current Total Connections (New) | Count | TotalConnections | userId, instanceId, and role | The total number of connections. |

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| The amount of disk space occupied by the instance (new) | Bytes | InstanceDiskAmo unt new _ | userId, instanceId, and role | The disk space occupied by the instance. |
| Amount of disk space occupied by data (new) | Bytes | DataDiskAmount new _ | userId, instanceId, and role | The disk space occupied by data. |
| The amount of disk space occupied by the log (new) | Bytes | LogDiskAmount _ new | userId, instanceId, and role | The disk space occupied by logs. |

| loudMonitor |   |   | Developer G | uide·CloudMonitor PI Referenc |
|---|---|---|---|---|

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Intranet Inflow (New) | Bytes | IntranetIn new _ | userId, instanceId, and role | The inbound traffic over the intranet. |
| Intranet outbound traffic (new) | Bytes | IntranetOut new _ | userId, instanceId, and role | The outbound traffic over the private network. |
| Number of requests (new) | Count | NumberRequests new _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Command Operations (new) | Count | OpCommand ne _ w | userId, instanceId, and role | The number of Command operations. |
| Number of Delete operations (new) | Count | OpDelete new _ | userId, instanceId, and role | The number of Delete operations. |
| Number of Getmore operations (new) | Count | OpGetmore new _ | userId, instanceId, and role | The number of Getmore operations. |
| Number of Insert operations (new) | Count | OpInsert new _ | userId, instanceId, and role | The number of Insert operations. |
| Number of Query operations (new) | Count | OpQuery new _ | userId, instanceId, and role | The number of Query operations. |

| Number of Update operations (new) | Count | OpUpdate new _ | userId, instanceId, and role | The number of Update operations. |
|---|---|---|---|---|

**Basic metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster) CPU usage | % | CPUUtilization new _ cluster _ | userId, instanceId, and role | The CPU utilization. |
| (Cluster Version) Memory Usage | % | MemoryUtilization _ new cluster _ | userId, instanceId, and role | The memory usage. |
| (Cluster Edition) Disk Usage | % | DiskUtilization ne _ w cluster _ | userId, instanceId, and role | The disk usage. |
| (Cluster version) IOPS usage | % | IOPSUtilization ne _ w cluster _ | userId, instanceId, and role | The IOPS usage. |
| (Cluster Edition) Connection Usage | % | ConnectionUtilizati on new cluster _ _ | userId, instanceId, and role | The connection utilization. |
| (Cluster Version) Visits Per Second | Count | QPS new cluster _ _ | userId, instanceId, and role | The QPS. |
| (Cluster Edition) Connection Usage | Count | ConnectionAmount new cluster _ _ | userId, instanceId, and role | The number of used connections. |
| (Cluster Edition) Total Number of Connections | Count | TotalConnections _ cluster | userId, instanceId, and role | The total number of connections. |

**Disk capacity-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) The amount of disk space occupied by the instance | Bytes | InstanceDiskAmoun t new cluster _ _ | userId, instanceId, and role | The disk space occupied by the instance. |

| (Cluster Edition) The amount of disk space occupied by data | Bytes | DataDiskAmount n _ ew cluster _ | userId, instanceId, and role | The disk space occupied by data. |
|---|---|---|---|---|
| (Cluster Edition) The amount of disk space occupied by logs | Bytes | LogDiskAmount ne _ w cluster _ | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Version) Intranet Inflow | Bytes | IntranetIn new cl _ _ uster | userId, instanceId, and role | The inbound traffic over the intranet. |
| (Cluster Version) Intranet outbound traffic | Bytes | IntranetOut new _ _ cluster | userId, instanceId, and role | The outbound traffic over the intranet. |
| (Cluster Version) Number of Requests | Coun t | NumberRequests new cluster _ _ | userId, instanceId, and role | The number of requests. |

**Operation count-related metrics (Cluster Edition)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Cluster Edition) Command Operation Times | Count | OpCommand _ new cluster _ | userId, instanceId, and role | The number of Command operations. |
| (Cluster version) Delete operations | Count | OpDelete ne _ w cluster _ | userId, instanceId, and role | The number of Delete operations. |
| (Cluster version) Getmore Operations | Count | OpGetmore n _ ew cluster _ | userId, instanceId, and role | The number of Getmore operations. |
| (Cluster version) Insert operations | Count | OpInsert new _ cluster _ | userId, instanceId, and role | The number of Insert operations. |

| (Cluster Version) Query Operation Times | Count | OpQuery new _ cluster _ | userId, instanceId, and role | The number of Query operations. |
|---|---|---|---|---|
| (Cluster Edition) Update Operation Times | Count | OpUpdate ne _ w cluster _ | userId, instanceId, and role | The number of Update operations. |

**AnalyticDB for PostgreSQL**

Set the **Namespace** parameter to **acs_hybriddb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Computing and storage-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Computing and Storage Integration] Connection Usage | % | ConnectionUsage | userId, instanceId, and role | The connection utilization. |
| [Integration of Computing and Storage] CpuUsage | % | CpuUsage | userId, instanceId, and role | The CPU utilization. |
| [Computing and Storage Integration] DiskUsage | % | DiskUsage | userId, instanceId, and role | The disk usage. |
| [Integration of computing and storage] IOPSUsage | % | IOPSUsage | userId, instanceId, and role | The IOPS utilization. |
| [Computing and Storage Integration] MemoryUsage | % | MemoryUsage | userId, instanceId, and role | The memory usage. |

**Storage reservation-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| adbpg master cn _ _ t unhealth _ | Count | adbpg master cn _ _ t unhealth _ | instanceId, instance compon _ ent, and hostname | The number of abnormal coordinator nodes. |
|---|---|---|---|---|
| adbpg segment _ _ cnt unhealth _ | Count | adbpg segment _ _ cnt unhealth _ | instanceId, instance compon _ ent, and hostname | The number of abnormal compute nodes. |
| adbpg instance _ _ disk used mb _ _ | MB | adbpg instance _ _ disk used mb _ _ | instanceId, instance compon _ ent, and hostname | The amount of used disk space. |
| adbpg instance _ _ disk usage perce _ _ nt | % | adbpg instance _ _ disk usage perce _ _ nt | instanceId, instance compon _ ent, and hostname | The disk usage. |
| Storage Reservation Instance Active Connections | Count | adbpg conn acti _ _ ve | instanceId, instance compon _ ent, and hostname | The number of active connections on the instance. |
| adbpg conn idle _ _ | Count | adbpg conn idle _ _ | instanceId, instance compon _ ent, and hostname | The number of idle connections on the instance. |
| adbpg conn Cou _ _ nt | Count | adbpg conn cou _ _ nt | instanceId, instance compon _ ent, and hostname | The number of connections of the coordinator node. |
| adbpg query blo _ _ cked | Count | adbpg query blo _ _ cked | instanceId, instance compon _ ent, and hostname | The number of blocked queries on the instance. |
| adbpg query que _ _ ued | Count | adbpg query qu _ _ eued | instanceId, instance compon _ ent, and hostname | The number of queued queries on the instance. |
| [Storage Reservation] Number of active queries on the master node instance (new) | Count | adbpg query acti _ _ ve | instanceId, instance compon _ ent, and hostname | The number of active queries on the instance. |

| [Storage Reservation] Number of nodes (new) whose master node coordinates the node out of sync | Count | adbpg master cn _ _ t repl not sync _ _ _ | instanceId, instance compon _ ent, and hostname | The number of coordinator nodes that are in the out-of-sync state. |
|---|---|---|---|---|
| [Storage Reservation] Number of nodes that coordinates nodes that are out of sync | Count | adbpg segment _ _ cnt repl not syn _ _ _ c | instanceId, instance compon _ ent, and hostname | The number of compute nodes that are in the out-of-sync state. |
| node cpu used p _ _ _ ercent | % | node cpu used p _ _ _ ercent | instanceId, instance compon _ ent, and hostname | The CPU utilization of the node. |
| node mem used _ _ _ percent | % | node mem used _ _ percent _ | instanceId, instance compon _ ent, and hostname | The memory usage of the node. |
| node disk iops _ _ | Count | node disk iops _ _ | instanceId, instance compon _ ent, and hostname | The IOPS of the node. |
| [Storage Reservation] Node Disk Usage | MB | node disk used _ _ _ mb | instanceId, instance compon _ ent, and hostname | The used disk space of the node. |
| node disk used _ _ _ percent | % | node disk used _ _ _ percent | instanceId, instance compon _ ent, and hostname | The disk usage of the node. |

**AnalyticDB for PostgreSQL (New)**

Set the **Namespace** parameter to **acs_hybriddb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Computing and storage integration metrics (primary node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Computing and Storage Integration] Primary Node Connection Number Usage (New) | % | ConnectionUsageM aster | userId, instanceId, and role | The usage of primary node connections. |
| [Integration of computing and storage] master node CPU usage (new) | % | CpuUsageMaster | userId, instanceId, and role | The CPU utilization of the primary node. |
| [Computing and Storage Integration] Primary Node Disk Usage (New) | % | DiskUsageMaster | userId, instanceId, and role | The disk usage of the primary node. |
| [Integration of computing and storage] master node IO throughput usage (new) | % | IOPSUsageMaster | userId, instanceId, and role | The IOPS usage of the primary node. |
| [Computing and Storage Integration] Master Node Memory Usage (New) | % | MemoryUsageMast er | userId, instanceId, and role | The memory usage of the primary node. |

**Storage reservation-related metrics (primary node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Storage Reservation] Number of Master Node Coordination Node Connections (New) | Coun t | adbpg conn coun _ _ t master _ | instance id, _ instance componen _ t, and hostname | The number of coordinator node connections. |
| [Storage Reservation] CPU usage of the master node (new) | % | node cpu used p _ _ _ ercent master _ | instance id, _ instance componen _ t, and hostname | The CPU utilization of the primary node. |

| [Storage Reservation] Primary Node Memory Usage (New) | % | node mem used _ _ _ percent master _ | instance id, _ instance componen _ t, and hostname | The memory usage of the primary node. |
|---|---|---|---|---|
| [Storage Reservation] Number of abnormal master node coordination nodes (new) | Coun t | adbpg master cn _ _ t unhealth maste _ _ r | instance id _ | The number of abnormal coordinator nodes of the primary node. |
| [Storage Reservation] The number of nodes (new) whose master node coordinates the node out of sync. | Coun t | adbpg master cn _ _ t repl not sync _ _ _ _ master | instance id _ | The number of primary nodes that are not synchronized to coordinator nodes. |
| [Storage Reservation] Number of Queued Queries of Primary Node Instances (New) | Coun t | adbpg query que _ _ ued master _ | instance id _ | The number of queued queries on the primary node instance. |
| [Reserved storage] Number of active connections of the primary node instance (new) | Coun t | adbpg conn activ _ _ e master _ | instance id _ | The number of active connections to the primary node instance. |
| [Storage Reservation] Number of active queries on the master node instance (new) | Coun t | adbpg query acti _ _ ve master _ | instance id _ | The number of active queries on the primary node instance. |
| [Storage Reservation] Number of idle connections of the master node instance (new) | Coun t | adbpg conn idle _ _ _ master | instance id _ | The number of idle connections of the primary node instance. |

**Computing-storage integration metrics (compute node group)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Integration of computing and storage] CPU usage of computing group nodes (new) | % | CpuUsageSegment | userId, instanceId, and role | The CPU utilization of the nodes in the compute group. |

| [Computing and Storage Integration] Computing Group Node Disk Usage (New) | % | DiskUsageSegment | userId, instanceId, and role | The disk usage of the nodes in the compute group. |
|---|---|---|---|---|
| [Integration of computing and storage] I/O throughput usage of computing group nodes (new) | % | IOPSUsageSegmen t | userId, instanceId, and role | The IOPS usage of the nodes in the compute group. |
| [Computing and Storage Integration] Computing Group Node Memory Usage (New) | % | MemoryUsageSeg ment | userId, instanceId, and role | The memory usage of the nodes in the compute group. |

**Storage reservation-related metrics (compute group node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Storage Reservation] CPU usage of Compute Group Node (New) | % | node cpu used per _ _ _ cent segment _ | instance id, _ instance compon _ ent, and hostname | The CPU utilization of nodes in the compute group. |
| [Storage reservation] Memory Usage of Compute Group Node (New) | % | node mem used pe _ _ _ rcent segment _ | instance id, _ instance compon _ ent, and hostname | The memory usage of nodes in the compute group. |
| [Storage Reservation] Compute group node disk usage (new) | % | node disk used per _ _ _ cent segment _ | instance id, _ instance compon _ ent, and hostname | The disk usage of nodes in the compute group. |
| [Storage Reservation] Calculate the disk usage of the group node instance (new) | % | adbpg instance dis _ _ k usage percent se _ _ _ gment | instance id _ | The disk usage of node instances in the compute group. |

| [Reserved Storage] Local Data Read IOPS | Count /s | node disk iops rea _ _ _ d segment _ | instance id _ | The read IOPS of nodes in the compute group. |
|---|---|---|---|---|
| [Reserved Storage] Local Data Write IOPS | Count /s | node disk iops writ _ _ _ e segment _ | instance id _ | The write IOPS of nodes in the compute group. |
| [Reserved Storage] Local Data File Size | MB | adbpg local data di _ _ _ r size segment _ _ | instance id _ | The size of files in the nodes in the compute group. |

**VPN Gateway**

Set the **Namespace** parameter to **acs_vpn**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IPSec.connection. rxPkgs | Packets/s | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate at which packets are received over the IPsec-VPN connection. |
| IPSec.connection. txpkgs | Packets/s | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate at which packets are sent over the IPsec- VPN connection. |
| IPSec.connection. rx.rate | Bit/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits of the connection per second. |
| IPSec.connection. tx.rate | Bit/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits of the connection per second. |
| SSL Client Count | Count | ssl client.count _ | userId, instanceId, and ipsecId | The number of connections. |

**AnalyticDB for MySQL V3.0**

Set the **Namespace** parameter to **acs_adb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connections | Count | connections | userId and instanceId | The rate of inbound packets of the connection. |
| Average CPU usage of nodes | % | worker avg cpu _ _ _ used | userId and instanceId | The CPU utilization of the node. |
| Query the average CPU usage of a computing node | % | executor avg cp _ _ u used _ | userId and instanceId | The CPU utilization of a compute node. |
| (Reserved Mode) Maximum Node Disk Usage | % | worker max nod _ _ e disk used perc _ _ _ ent | userId and instanceId | The maximum disk usage of the node in reserved mode. |
| Disk usage | % | disk used percen _ _ t | userId and instanceId | The disk usage in reserved mode. |
| (Elastic Mode) Maximum Node Disk Usage | MB | worker max nod _ _ e disk used MB _ _ _ | userId and instanceId | The maximum used disk space of the node in elastic mode. |
| (Elastic Mode) Disk Cold Data Usage | MB | ColdDataDiskUsa ge | userId and instanceId | The used disk space for cold data in elastic mode. |
| (Elastic Mode) Disk Hot Data Usage | MB | HotDataDiskUsag e | userId and instanceId | The used disk space for hot data in elastic mode. |

| Average disk reads | MB | worker avg read _ _ bytes _ | userId and instanceId | The read throughput of the read-write node. |
|---|---|---|---|---|
| Average disk writes | MB | worker avg write _ _ bytes _ | userId and instanceId | The write throughput of the storage node. |
| Query the read throughput of compute nodes | MB | executor avg re _ _ ad bytes MB _ _ | userId and instanceId | The read throughput of the compute node. |
| Query compute node write throughput | MB | executor avg wri _ _ te bytes MB _ _ | userId and instanceId | The write throughput of the compute node. |
| Disk read throughput | Count/s | worker avg read _ _ iops _ | userId and instanceId | The read IOPS of the read-write node. |
| Disk write throughput | Count/s | worker avg write _ _ iops _ | userId and instanceId | The write IOPS of the read-write node. |
| Query compute node read IOPS | Count/s | executor avg re _ _ ad iops _ | userId and instanceId | The read IOPS of the compute node. |
| Query compute node write IOPS | Count/s | executor avg wri _ _ te iops _ | userId and instanceId | The write IOPS of the compute node. |
| Disk IO usage | % | worker avg io ut _ _ _ il | userId and instanceId | The disk I/O usage. |
| QPS | Count/s | qps | userId and instanceId | The number of QPS. |
| Average query time | Milliseconds | query avg rt _ _ | userId and instanceId | The average query time. |
| Maximum query time | Milliseconds | query max rt _ _ | userId and instanceId | The maximum query time. |

| Total query average waiting time | Milliseconds | query total wait _ _ _ time | userId and instanceId | The average query waiting time. |
|---|---|---|---|---|
| TPS | Count/s | tps | userId and instanceId | The number of transactions per second (TPS). |
| Average write response time | Milliseconds | insert avg rt _ _ | userId and instanceId | The average write response time. |
| Maximum write response time | Milliseconds | insert max rt _ _ | userId and instanceId | The maximum write response time. |
| Write throughput | MB | insert in bytes _ _ | userId and instanceId | The write throughput. |

**PolarDB-X 1.0**

Set the **Namespace** parameter to **acs_polarx_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | useId and InstanceId | The CPU utilization. |
| Memory Usage | % | MemoryUtilization | useId and InstanceId | The memory usage. |
| Network input | Bytes/ s | NetworkInputTraffi c | useId and InstanceId | The inbound traffic. |
| Network output | Bytes/ s | NetworkOutputTraf fic | useId and InstanceId | The outbound traffic. |
| Average number of logical requests per second | Count | LogicQPS | useId and InstanceId | The average number of logical requests per second. |

| Average Logical Response Time | Millise conds | LogicRT | useId and InstanceId | The average response time of logical requests. |
|---|---|---|---|---|
| Average number of physical requests per second | Count | PhysicsQPS | useId and InstanceId | The average number of physical requests per second. |
| Average Physical Response Time | Millise conds | PhysicsRT | useId and InstanceId | The average response time of physical requests. |
| Number of connections | Count | ConnectionCount | useId and InstanceId | The total number of sessions. |
| Number of active sessions | Count | ThreadCount | useId and InstanceId | The number of active sessions. |
| Average Logical Errors per Second | Count | LogicErrorCount | useId and InstanceId | The average number of logical errors per second. |

**PolarDB-X 2.0**

**Compute node-related metrics**

Set the **Namespace** parameter to **acs_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| Number of connections | Count | ConnectionCount | userId and instanceId | The total number of sessions. |
| Average number of logical requests per second | Count | LogicQPS | userId and instanceId | The number of requests per second. |

| Average Logical Response Time | Millis econ ds | LogicRT | userId and instanceId | The average response time of logical requests. |
|---|---|---|---|---|
| Memory Usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| Network input | Bit/s | NetworkInputTraffic | userId and instanceId | DRDS NetworkInput Traffic |
| Network output | Bit/s | NetworkOutputTraffic | userId and instanceId | DRDS NetworkOutputTra ffic |
| Average number of physical requests per second | Count | PhysicsQPS | userId and instanceId | The physical QPS. |
| Average Physical Response Time | Millis econ ds | PhysicsRT | userId and instanceId | The physical response time. |
| Number of active sessions | Count | ThreadCount | userId and instanceId | The number of active threads. |
| Heap memory usage | % | HeapMemoryUsage | userId and instanceId | The heap memory usage. |
| Log directory size | Bytes | LogSize | userId and instanceId | The size of the log directory. |
| Number of errors per second | Count | SecondErrorCount | userId and instanceId | The number of errors per second. |
| Physical slow SQL per second | Count | SecondPhysicalSqlCoun t | userId and instanceId | The number of physical slow SQL queries per second. |
| Slow requests per second | Count | SecondRequestCount | userId and instanceId | The number of slow QPS. |
| spill directory size | Bytes | SpillSize | userId and instanceId | The size of the spill directory. |

| Temporary directory size | Bytes | TmpSize | userId and instanceId | The size of the temporary directory. |
|---|---|---|---|---|

**Data node-related metrics**

The **Namespace** parameter to **acs_polarxsn_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU Utilization (New) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk Usage (New) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS Usage (New) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory Utilization (New) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| Inbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkInNew _ new _ | userId and instanceId | The inbound traffic to the MySQL data node per second. |
| Outbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkOutNe _ w new _ | userId and instanceId | The outbound traffic from the MySQL data node per second. |
| QPS of an ApsaraDB RDS for MySQL Instance (New) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second on the MySQL data node. |

**EIP**

Set the **Namespace** parameter to **acs_vpc_eip**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| net rx.rate _ | Bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |
| net rxPkgs.rate _ | Count/s | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
| net tx.rate _ | Bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |
| net txPkgs.rate _ | Count/s | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
| Out Ratelimit Drop Speed | Packets/s | out ratelimit dro _ _ p speed _ | userId and instanceId | The outbound packet loss rate. |
| In Ratelimit Drop Speed | Packets/s | in ratelimit drop _ _ speed _ | userId and instanceId | The inbound packet loss threshold. |

**API Gateway**

Set the **Namespace** parameter to **acs_apigateway_dashboard**. Set the **Period** parameter to an integral multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseconds | Latency | userId, region, and apiUid | The response time. |

| SumQPS | Count | SumQPS | userId, region, and apiUid | The total QPS. |
|---|---|---|---|---|
| TrafficRX | KB | TrafficRX | userId, region, and apiUid | The inbound traffic. |
| TrafficTX | KB | TrafficTX | userId, region, and apiUid | The outbound traffic. |
| code2XX Number | Count | code2XX | userId, region, and apiUid | The number of times that a 2XX HTTP status code is returned. |
| code4XX Number | Count | code4XX | userId, region, and apiUid | The number of times that a 4XX HTTP status code is returned. |
| code5XX Number | Count | code5XX | userId, region, and apiUid | The number of times that a 5XX HTTP status code is returned. |

**Hologres**

Set the **Namespace** parameter to **acs_hologres**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total Connections Used | Count | connection num _ | userId and instanceId | The number of SQL connections. |
| Connection Usage | % | connection usag _ e | userId and instanceId | The connection utilization of an instance. |
| Export QPS | Count/s | record output qp _ _ s | userId and instanceId | The QPS. |

| Micro batch size | Count/s | scan batchsize _ | userId and instanceId | The size of the micro batch. |
|---|---|---|---|---|
| CPU Utilization | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| memory usage | % | memory usage _ | userId and instanceId | The memory usage. |
| storage usage _ | Bytes | storage usage _ | userId and instanceId | The used storage. |
| I/O Write Throughput | Bytes/s | io write through _ _ put | userId and instanceId | The write I/O throughput per second. |
| I/O Read Throughput | Bytes/s | io read throughp _ _ ut | userId and instanceId | The read I/O throughput per second. |

**Status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Failed Query Qps | Count/s | failed query qps _ _ | userId and instanceId | The number of failed QPS. |
| Query Latency Detail | Milliseconds | query latency _ | instanceId, userId, and cmdType | The latency of the query. |
| Query QPS Detail | Count/s | query qps _ | instanceId, userId, and cmdType | The detailed QPS data. |

**Tablestore**

Set the **Namespace** parameter to **acs_ots_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Instance VCU | Count/s | InstanceVCU | userId and instanceName | The virtual compute units (VCUs) of the instance. |
| Reserved VCU | Count/s | InstanceReserve dVCU | userId and instanceName | The reserved VCUs of the instance. |
| Internal Read CU | Count/s | InstanceFreeRea dCU NoOp _ | userId and instanceName | The internal read capacity units (CUs). |
| Internal Write CU | Count/s | InstanceFreeWrit eCU NoOp _ | userId and instanceName | The internal write CUs. |
| Over ReadCU | Count/s | InstanceOverRea dCU NoOp _ | userId and instanceName | The excess read CUs of the instance. |
| Over WriteCU | Count/s | InstanceOverWrit eCU NoOp _ | userId and instanceName | The excess write CUs of the instance. |
| Read CU | Count/s | InstanceReadCU _ NoOp | userId and instanceName | The operation read CUs. |
| Write CU | Count/s | InstanceWriteCU _ NoOp | userId and instanceName | The operation write CUs. |
| Total Request | Count/s | InstanceRequest Number NoOp _ | userId and instanceName | The total number of requests. |
| 2xx Request | Count/s | InstanceCount2x xNumber NoOp _ | userId and instanceName | The number of requests for which a 2XX HTTP status code is returned. |

| 429 Request | Count/s | InstanceCount42 9Number NoOp _ | userId and instanceName | The number of requests for which the HTTP status code 429 is returned. |
|---|---|---|---|---|
| 4xx Request | Count/s | InstanceCount4x xNumber NoOp _ | userId and instanceName | The number of requests for which a 4XX HTTP status code is returned. |
| 5xx Request | Count/s | InstanceCount5x xNumber NoOp _ | userId and instanceName | The number of requests for which a 5XX HTTP status code is returned. |
| Internet Inbound | Bytes/s | InstanceExtranetI n NoOp _ | userId and instanceName | The inbound traffic over the Internet. |
| Internet Outbound | Bytes/s | InstanceExtranet Out NoOp _ | userId and instanceName | The outbound traffic over the Internet. |
| Free Outbound Internet | Bytes/s | InstanceFreeExtr anetOut NoOp _ | userId and instanceName | The free outbound traffic over the Internet. |
| Total Rows | Count/s | InstanceRowCou nt NoOp _ | userId and instanceName | The total number of rows. |
| Failed Rows | Count/s | InstanceFailRowC ount NoOp _ | userId and instanceName | The number of failed rows. |

**NAT Gateway**

Set the **Namespace** parameter to **acs_nat_gateway**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Total number of sessions | Count | curr num _ | userId and instanceId | The total number of sessions. |
|---|---|---|---|---|
| Capacity Discard Connections (Cumulative Value) | Count | capacity drop _ | userId and instanceId | The number of capacity-dropped connections. |
| Number of new discarded connections (cumulative value) | Count | ratelimit drop _ | userId and instanceId | The number of new dropped connections. |
| Capacity Discard Connections Per Second | Count/s | capacity drop in _ _ c | userId and instanceId | The number of capacity-dropped connections per second. |
| Number of new and discarded connections per second | Count/s | ratelimit drop in _ _ c | userId and instanceId | The number of new dropped connections per second. |
| Number of new connections per second | Count/s | establish rate _ | userId and instanceId | The number of new connections per second. |

**Elasticsearch on Kubernetes**

Set the **Namespace** parameter to **acs_elasticsearch**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| ClusterStatus | Value | ClusterStatus | userId and instanceId | The status of the cluster. Valid values: 0: green, which indicates normal. 1: yellow, which indicates warning. 2: red, which indicates exception. |
|---|---|---|---|---|
| Number of tasks waiting to be executed | Count | PendingTaskCou nt | userId and instanceId | The number of tasks waiting to be executed. |
| The maximum waiting time for a task to be executed | Milliseconds | PendingTaskMax WaitTime | userId and instanceId | The maximum waiting time for a task to be executed. |
| Number of data nodes | Count | DataNodes | userId and instanceId | The number of data nodes. |
| Active Shards | Count | ActiveShards | userId and instanceId | The number of active shards. |
| Unallocated Shards | Count | UnassingnedShar dsShards | userId and instanceId | The number of unallocated shards. |

**Node-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Node CPU usage | % | NodeCPUUtil | userId, instanceId, and nodeName | The CPU utilization of the node. |
| Node disk usage | % | NodeDiskUtil | userId, instanceId, and nodeName | The disk usage of the node. |

| NodeHeapMemor yUtilization | % | NodeHeapMemor yUtil | userId, instanceId, and nodeName | The heap memory usage of the node. |
|---|---|---|---|---|
| Node cpu 1min load | Value | NodeLoad1 | userId, instanceId, and nodeName | The average load of the node over the last 1 minute. |
| Node cpu 5min load | Value | NodeLoad5 | userId, instanceId, and nodeName | The average load within 5 minutes of the node. |
| Node cpu 15min load | Value | NodeLoad15 | userId, instanceId, and nodeName | The average load within 15 minutes of the node. |
| Node OldGC times-Cumulative Value | Count | OldGCTotalCount | userId, instanceId, and nodeName | The total number of times that garbage collection (GC) is performed in the old generation space of the node. |
| Node OldGC Time- Accumulation Value | Milliseconds | OldGCTotalTime | userId, instanceId, and nodeName | The total amount of time consumed by GC in the old generation space of the node. |
| Node OldGC average time consumption | Milliseconds | OldGCCostTime | userId, instanceId, and nodeName | The average amount of time consumed by GC in the old generation space of the node. |
| Node OldGC rate | Count/s | OldGCRate | userId, instanceId, and nodeName | The rate of GC in the old generation space of the node. |
| Node YoungGC times-Cumulative Value | Count | YoungGCTotalCo unt | userId, instanceId, and nodeName | The total number of times that GC is performed in the young generation space of the node. |

| Node YoungGC Time- Accumulation Value | Count | YoungGCTotalTi me | userId, instanceId, and nodeName | The total amount of time consumed by GC in the young generation space of the node. |
|---|---|---|---|---|
| Average Node YoungGC Time Consumption (MS) | Milliseconds | YoungGCCostTim e | userId, instanceId, and nodeName | The average amount of time consumed by GC in the young generation space of the node. |
| Node YoungGC rate | Count/s | YoungGCRate | userId, instanceId, and nodeName | The rate of GC in the young generation space of the node. |
| Node Free Disk Space | GB | AvailableDiskSize | userId, instanceId, and nodeName | The available disk space of the node. |
| Node heap memory usage | GB | NodeHeapMemor y | userId, instanceId, and nodeName | The heap memory usage of the node. |
| Number of node documents | Count | NodeDocumentC ount | userId, instanceId, and nodeName | The number of documents on the node. |
| Number of node segments | Count | NodeSegmentCo unt | userId, instanceId, and nodeName | The number of node segments. |
| Disk IO Rate | Count/s | NodeDiskIOOper ationsRate | userId, instanceId, and nodeName | The disk I/O rate. |
| Disk write rate | Count/s | NodeWriteIOOper ationsRate | userId, instanceId, and nodeName | The disk write rate. |
| Disk read rate | Count/s | NodeReadIOOper ationsRate | userId, instanceId, and nodeName | The disk read rate. |
| Number of threads | Count | IndexThread | userId, instanceId, and nodeName | The number of threads. |

| Query thread | Count | WriteThread | userId, instanceId, and nodeName | The number of query threads. |
|---|---|---|---|---|
| Node data size | MB | NodeData | userId, instanceId, and nodeName | The size of the data disk of the node. |
| Various memory usage of nodes | KB | NodeIndexMemor yLucene | userId, instanceId, and nodeName | The various memory usage of the node. |
| Node terms memory usage | KB | NodeIndexMemor yTerms | userId, instanceId, and nodeName | The terms memory usage of the node. |
| Node points memory usage | KB | NodeIndexMemor yPoints | userId, instanceId, and nodeName | The points memory usage of the node. |
| NodeSearchLaten cy | Milliseconds | NodeSearchLaten cy | userId, instanceId, and nodeName | The average duration of a single query. |
| Average Time Consumption of a Single Index | Milliseconds | NodeIndexingLat ency | userId, instanceId, and nodeName | The average amount of time that is consumed by a single index. |

**Index-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Write rate | Count/s | IndexRate | userId and indexName | The write rate. |
| Average write time | Milliseconds | AvgIndexTime | userId and indexName | The average amount of time that is consumed by a single write operation. |
| Query Rate | Count/s | SearchRate | userId and indexName | The query rate. |

| Average time consumption of a single query | Milliseconds | AvgSearchTime | userId and indexName | The average amount of time that is consumed by a single query. |
|---|---|---|---|---|
| Number of indexed documents | Count | IndexDocummen tCount | userId and indexName | The number of indexed documents. |
| Total Number of Segments | Count | IndexSegmentAll Shard | userId and indexName | The total number of segements. |
| Number of main segmentation | Count | IndexSegmentPri maries | userId and indexName | The number of primary shard segments. |
| Field memory | Bytes | FielddataMemory BytesTotal | userId and indexName | The field memory. |
| Index terms memory | Bytes | IndexMemoryTer ms | userId and indexName | The memory of the index terms. |
| Node points memory usage | Bytes | IndexMemoryPoi nts | userId and indexName | The memory of index points. |
| Index data size | Bytes | IndexDisk | userId and indexName | The size of the index data. |
| Index master slice data size | Bytes | IndexDiskPrimari es | userId and indexName | The data size of the primary shard of the index. |

**ApsaraMQ for RocketMQ**

Set the **Namespace** parameter to **acs_rocketmq_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| Message retention duration | Hour | MessageRetentio nPeriod | userId and instanceId | The retention duration of messages. |
|---|---|---|---|---|
| ReceiveMessage CountPerInstance | Count/min | ReceiveMessage CountPerInstance | userId and instanceId | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerInstance | Count/min | SendMessageCou ntPerInstance | userId and instanceId | The number of messages that the producer sends per minute. |
| Consumer(Instan ce) receives message TPS | Count/min | ReceiveMessage TPSPerInstance | userId and instanceId | The TPS for receiving messages by the consumer per minute. |
| Producer(Instanc e) sends messages TPS | Count/min | SendMessageTPS PerInstance | userId and instanceId | The TPS for sending messages by the producer per minute. |

**Group-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer Gid | Count | ConsumerLag | userId, instanceId, and groupId | The number of accumulated messages. |
| ReceiveMessage CountPerGid | Count/min | ReceiveMessage CountPerGid | userId, instanceId, and groupId | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGid | Count/min | SendDLQMessag eCountPerGid | userId, instanceId, and groupId | The number of dead-letter messages generated per minute. |

| Producer(GroupId ) Number of messages sent per minute | Count/min | SendMessageCou ntPerGid | userId, instanceId, and groupId | The number of messages that the producer sends per minute. |
|---|---|---|---|---|
| Consumer(GroupI d) receives messages TPS | Count/min | ReceiveMessage TPSPerGid | userId, instanceId, and groupId | The TPS for receiving messages by the consumer per minute. |
| Producer(GroupId ) sends messages TPS | Count/min | SendMessageTPS PerGid | userId, instanceId, and groupId | The TPS for sending messages by the producer per minute. |

**Topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ReceiveMessage CountPerTopic | Count/min | ReceiveMessage CountPerTopic | userId, instanceId, and topic | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerTopic | Count/min | SendMessageCou ntPerTopic | userId, instanceId, and topic | The number of messages sent by the producer per minute. |
| Consumer (Topic) receives message TPS | Count/min | ReceiveMessage TPSPerTopic | userId, instanceId, and topic | The TPS for receiving messages by the consumer per minute. |
| Producer(Topic) sends messages TPS per minute | Count/min | SendMessageTPS PerTopic | userId, instanceId, and topic | The TPS for sending messages by the producer per minute. |

**Group and topic-related metrics**

| > Document Version | : 20250312 |   |   | 7 |
|---|---|---|---|---|

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer GidTopic | Count | ConsumerLagPer GidTopic | userId, instanceId, groupId, and topic | The number of accumulated messages. |
| ReceiveMessage CountPerGidTopic | Count/min | ReceiveMessage CountPerGidTopi c | userId, instanceId, groupId, and topic | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGidTop ic | Count/min | SendDLQMessag eCountPerGidTop ic | userId, instanceId, groupId, and topic | The number of dead-letter messages generated per minute. |
| Producer(GroupId & Topic) Number of messages sent per minute | Count/min | SendMessageCou ntPerGidTopic | userId, instanceId, groupId, and topic | The number of messages that the producer sends per minute. |

**NAS**

Set the **Namespace** parameter to **acs_nas**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**File system-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Aligned Size | Bytes | AlignedSize | userId and fileSystemId | The data volume of General-purpose File Storage NAS (NAS) file systems, excluding the Infrequent Access (IA) storage medium. |

| Storage Usage of IA Storage Medium | Bytes | SecondaryAligne dSize | userId and fileSystemId | The data volume of the IA storage medium. |
|---|---|---|---|---|
| File Count | Bytes | FileCount | userId and fileSystemId | The number of files. |
| Read IOPS | Operations/ s | IopsRead | userId and fileSystemId | The average read IOPS per minute. |
| Write IOPS | Operations/ s | IopsWrite | userId and fileSystemId | The average write IOPS per minute. |
| Read Latency | Milliseconds | LatencyRead | userId and fileSystemId | The average read latency per minute. |
| Write Latency | Milliseconds | LatencyWrite | userId and fileSystemId | The average write latency per minute. |
| Metadata QPS | Requests/s | QpsMeta | userId and fileSystemId | The average QPS of metadata per minute. |
| Metadata delay | Milliseconds | LatencyMeta | userId and fileSystemId | The average latency of metadata. |
| Read Throughput | Bytes/s | ThruputRead | userId and fileSystemId | The average read throughput per minute. |
| Write Throughput | Bytes/s | ThruputWrite | userId and fileSystemId | The average write throughput per minute. |
| Maximum usable capacity | Bytes | Quota | userId and fileSystemId | The maximum available capacity. |
| Maximum number of files | Count | MaxFileCount | userId and fileSystemId | The maximum number of files. |

**PolarDB**

Set the **Namespace** parameter to **acs_polardb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**PolarDB-M**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-M) Connection Usage | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| (PolarDB-M) CPU usage | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| (PolarDB-M) Memory Usage | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| Number of active connections | Count | Active Session _ new _ | userId and instanceId | The number of active connections. |
| Storage Engine IO throughput per second | KB | Iops throughou _ t new _ | userId and instanceId | The I/O throughput of the storage engine per second. |
| Storage engine IO times per second | Count/s | Mps new _ | userId and instanceId | The number of I/O operations of the storage engine per second. |
| IO times per second | Count/s | DataIo Ps new _ _ | userId and instanceId | The number of I/O operations per second. |
| Number of queries | Count | Queries Ps ne _ _ w | userId and instanceId | The number of QPS. |
| Slow queries per second | Count/s | SlowQueries Ps _ new _ | userId and instanceId | The number of slow queries per second. |
| TPS | Count/s | Tps M _ | userId and instanceId | The TPS. |

| Blktag Usage | % | BlktagUsage | userId and instanceId | The usage of blktags. |
|---|---|---|---|---|
| BlktagLeft | MB | BlktagLeft | userId and instanceId | The remaining size of blktags. |
| InodeUsage | % | InodeUsage | userId and instanceId | The inode usage. |
| InodeLeft | MB | InodeLeft | userId and instanceId | The remaining size of inodes. |
| DiskLeft | % | DiskLeft | userId and instanceId | The remaining disk space. |
| DiskUsage | MB | DiskUsage | userId and instanceId | The disk usage. |

**PolarDB-O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-O)TPS | % | Tps O _ | userId and instanceId | The TPS. |
| (PolarDB-O) database CPU usage | % | Cgroup Cpu To _ _ tal | userId and instanceId | The CPU utilization of the database. |
| Cgroup Mem Usage _ _ | % | Cgroup Mem U _ _ sage | userId and instanceId | The memory usage of the database. |
| (PolarDB-O) Connection Usage | % | Connection Rati _ o | userId and instanceId | The connection utilization. |
| (PolarDB-O) Connections | Count | Connections O _ | userId and instanceId | The number of connections. |
| (PolarDB-O) Active Connections | Count | Active Connecti _ ons | userId and instanceId | The number of active connections. |
| (PolarDB-O)PFS reads IOPS | Frequenc y | Pfsd Read Iops _ _ | userId and instanceId | The read IOPS of the Polar file system (PFS). |

| (PolarDB-O)PFS writes IOPS | Frequenc y | Pfsd Write Iops _ _ | userId and instanceId | The write IOPS of the PFS. |
|---|---|---|---|---|
| (PolarDB-O) Database Age | xids | Db Age _ | userId and instanceId | The age of the database. |
| (PolarDB-O) Local Disk Usage | % | Local Disk Usa _ _ g | userId and instanceId | The local disk usage. |

**DTS**

Set the **Namespace** parameter to **acs_dts_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ChangeTrackin gLatency | Seconds | ChangeTrackingLatenc y | userId and instanceId | The latency of the change tracking task. |
| Synchronizatio nLatency | Seconds | SynchronizationLatenc y | userId and instanceId | The latency of the data synchronization task. |
| MigrationLaten cy | Seconds | MigrationLatency | userId and instanceId | The latency of the data migration task. |

**Stream Computing (Blink)**

Set the **Namespace** parameter to **acs_blink**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| FetchedDelay | Seconds | FetchedDelay | userId, regionId, projectName, and jobName | The processing latency. |
|---|---|---|---|---|
| Response Delay | % | inputDelay | userId, regionId, projectName, and jobName | The service latency. |
| Read RPS | RPS | ParserTpsRate | userId, regionId, projectName, and jobName | The read records per second (RPS). |
| Write RPS | RPS | SinkOutTpsRate | userId, regionId, projectName, and jobName | The write RPS. |
| FailoverRate | % | TaskFailoverRate | userId, regionId, projectName, and jobName | The failover rate. |

**MaxCompute**

Set the **Namespace** parameter to **acs_maxcompute_prepay**. Set the **Period** parameter to an integer multiple of 300. Default value: 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Project Use Space | Bytes | project used size _ _ | instanceId | The space used by the project. |
| Project upper limit space | Bytes | project max size _ _ | instanceId | The maximum space of the project. |
| Project space usage | % | project used rate _ _ | instanceId | The usage of the project space. |
| Number of files used by the project | Count | project used file _ _ _ number | instanceId | The number of files used by the project. |

**Realtime Compute for Apache Flink**

Set the **Namespace** parameter to **acs_flink.** Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Overview**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Times a Job Is Restarted upon a Failure | Count | flink jobmanager job nu _ _ _ mRestarts | userId and jobId | The number of times that a job is restarted upon a failure. |
| Job Duration | Milliseco nds | flink jobmanager job upti _ _ _ me | userId and jobId | The job duration. |
| Running Jobs | Count | flink jobmanager numRu _ _ nningJobs | userId and jobId | The number of jobs in progress. |
| Available Slots | Count | flink jobmanager taskSlo _ _ tsAvailable | userId and jobId | The number of available slots. |
| Total Number of Slots for a Task | Count | flink jobmanager taskSlo _ _ tsTotal | userId and jobId | The total number of slots for a task. |
| TM Quantity | Count | flink jobmanager numRe _ _ gisteredTaskManagers | userId and jobId | The number of task managers (TMs). |
| Processing Latency | Milliseco nds | flink taskmanager job ta _ _ _ sk operator currentEmitE _ _ ventTimeLag | userId and jobId | The processing latency. |
| Transmission Latency | Seconds | flink taskmanager job ta _ _ _ sk operator currentFetch _ _ EventTimeLag | userId and jobId | The transmission latency. |
| Total Number of Input Data Records of All Operators | N/A | flink taskmanager job ta _ _ _ sk operator numRecordsI _ _ n | userId and jobId | The total number of input data records of all operators. |
| Total Number of Output Data Records | Count | flink taskmanager job ta _ _ _ sk operator numRecords _ _ Out | userId and jobId | The total number of output data records. |

| Number of Input Data Records per Second for All Data Streams | Count/s | flink taskmanager job ta _ _ _ sk operator numRecordsI _ _ nPerSecond | userId and jobId | The number of input data records per second for all data streams. |
|---|---|---|---|---|
| Number of Output Data Records per Second for All Data Streams | Count/s | flink taskmanager job ta _ _ _ sk operator numRecords _ _ OutPerSecond | userId and jobId | The number of output data records per second for all data streams. |
| Number of Data Records Not Read by the Source | Count | flink taskmanager job ta _ _ _ sk operator pendingReco _ _ rds | userId and jobId | The number of data records that are not read by the source. |
| Duration for Which Data Is Not Processed in the Source | Milliseco nds | flink taskmanager job ta _ _ _ sk operator sourceIdleTi _ _ me | userId and jobId | The duration for which data is not processed in the source. |

**Checkpoint**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total Number of Checkpoints | Count | flink jobmanager job total _ _ _ NumberOfCheckpoints | userId and jobId | The total number of checkpoints. |
| Number of Failed Checkpoints | Count | flink jobmanager job num _ _ _ berOfFailedCheckpoints | userId and jobId | The number of failed checkpoints. |
| Number of Completed Checkpoints | Count | flink jobmanager job num _ _ _ berOfCompletedCheckpoint s | userId and jobId | The number of completed checkpoints. |
| Number of In- progress Checkpoints | Count | flink jobmanager job num _ _ _ berOfInProgressCheckpoint s | userId and jobId | The number of checkpoints in progress. |
| Duration of the Last Checkpoint | Millisec onds | flink jobmanager job lastC _ _ _ heckpointDuration | userId and jobId | The duration of the last checkpoint. |
| Size of the Last Checkpoint | Bytes | flink jobmanager job lastC _ _ _ heckpointSize | userId and jobId | The size of the last checkpoint. |

| Developer Guide·Clo I Reference | udMonitor | A |   | CloudMonito |
|---|---|---|---|---|

**State**

| Console-based metric | Uni t | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Maximum Latency in a State Data Cleanup | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name st _ _ _ _ ateClearLatency | userId and jobId | The maximum latency in a state data cleanup. |
| Maximum Latency in Single ValueState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name val _ _ _ _ ueStateGetLatency | userId and jobId | The maximum latency in a query of the value state. |
| Maximum Latency in Single ValueState Access (Update) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name val _ _ _ _ ueStateUpdateLatency | userId and jobId | The maximum latency in an update of the value state. |
| Maximum Latency in Single AggregatingState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name ag _ _ _ _ gregatingStateGetLatency | userId and jobId | The maximum latency in a query of the aggregated value. |
| Maximum Latency in Single AggregatingState Access (Add) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name ag _ _ _ _ gregatingStateAddLatency | userId and jobId | The maximum latency that occurs when an aggregated value is added. |
| Maximum Latency in Single AggregatingState Access (MerageNamespaces) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name ag _ _ _ _ gregatingStateMergeName spacesLatency | userId and jobId | The maximum latency that occurs when the aggregation states of namespaces are merged. |
| Maximum Latency in Single ReducingState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name re _ _ _ _ ducingStateGetLatency | userId and jobId | The maximum latency in a query of the reduced value. |

| Maximum Latency in Single ReducingState Access (Add) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name re _ _ _ _ ducingStateAddLatency | userId and jobId | The maximum latency that occurs when a value is added to the state. |
|---|---|---|---|---|
| Maximum Latency in Single ReducingState Access (MerageNamespaces) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name re _ _ _ _ ducingStateMergeNamesp acesLatency | userId and jobId | The maximum latency that occurs when aggregation states of namespaces are merged. |
| Maximum Latency in Single MapState Access (IsEmpty) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIsEmptyLatency | userId and jobId | The maximum latency in a check on whether a map contains any key- value mappings. |
| Maximum Latency in Single MapState Access (teratorHasNext) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorHasNextLat ency | userId and jobId | The maximum latency in a check on whether the next entry exists. |
| Maximum Latency in Single MapState Access (IteratorNext) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorNextLatenc y | userId and jobId | The maximum latency in a query of the next key- value pair during the iteration of entries in a MapState. |
| Maximum Latency in Single MapState Access (IteratorRemove) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorRemoveLat ency | userId and jobId | The maximum latency in a removal of an entry during the iteration of a MapState. |
| Maximum Latency in Single MapState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateGetLatency | userId and jobId | The maximum latency in a query of a key-value pair in a MapState. |
| Maximum Latency in Single MapState Access (Put) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStatePutLatency | userId and jobId | The maximum latency that occurs when a key-value pair is written to a MapState. |

| Maximum Latency in Single MapState Access (PutAll) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStatePutAllLatency | userId and jobId | The maximum latency that occurs when a group of key-value pair is written to a MapState. |
|---|---|---|---|---|
| Maximum Latency in Single MapState Access (Remove) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateRemoveLatency | userId and jobId | The maximum latency that occurs when a key-value pair is removed from a MapState. |
| Maximum Latency in Single MapState Access (Contains) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateContainsLatency | userId and jobId | The maximum latency in a check on whether a key- value pair exists in a MapState. |
| Maximum Latency in Single MapState Access (EntriesInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateEntriesInitLatency | userId and jobId | The maximum latency that occurs when a MapState is initialized. |
| Maximum Latency in Single MapState Access (KeysInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateKeysInitLatency | userId and jobId | The maximum latency that occurs when keys of a MapState are loaded during the initialization of the MapState. |
| Maximum Latency in Single MapState Access (ValuesInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateValuesInitLatency | userId and jobId | The maximum latency that occurs when values of a MapState are loaded during the initialization of the MapState. |
| Maximum Latency in Single MapState Access (IteratorInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorInitLatency | userId and jobId | The maximum latency that occurs when an iterator is initialized. |
| Maximum Latency in Single ListState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateGetLatency | userId and jobId | The maximum latency in a query of the key-value pairs in a ListState. |

| Maximum Latency in Single ListState Access (Add) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateAddLatency | userId and jobId | The maximum latency that occurs when a key-value pair is added to a ListState. |
|---|---|---|---|---|
| Maximum Latency in Single ListState Access (AddAll) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateAddAllLatency | userId and jobId | The maximum latency that occurs when a group of key-value pairs is added to a ListState. |
| Maximum Latency in Single ListState Access (Update) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateUpdateLatency | userId and jobId | The maximum latency that occurs when data in a ListState is updated. |
| Maximum Latency in Single ListState Access (MergeNamespaces) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateMergeNamespacesLat ency | userId and jobId | The maximum latency that occurs when namespaces are merged. |
| Maximum Latency in Single SortedMapState Access (FirstEntry) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name so _ _ _ _ rtedMapStateFirstEntryLat ency | userId and jobId | The maximum latency that occurs when the first entry in a sorted MapState is queried. |
| Maximum Latency in Single SortedMapState Access (LastEntry) | Ma xim um Lat enc y in Sin gle Sor ted Ma pSt ate Acc ess (La stE ntr y) | flink taskmanager job tas _ _ _ k operator state name so _ _ _ _ rtedMapStateLastEntryLate ncy | userId and jobId | The maximum latency that occurs when the last entry in a sorted MapState is queried. |

**Network**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Input Pool Usage | % | flink taskmanager job tas _ _ _ k buffers inPoolUsage _ _ | userId and jobId | The usage of the input pool. |
| Output Pool Usage | % | flink taskmanager job tas _ _ _ k buffers outPoolUsage _ _ | userId and jobId | The usage of the output pool. |
| Input Queue Length | Valu e | flink taskmanager job tas _ _ _ k buffers inputQueueLeng _ _ th | userId and jobId | The length of the input queue. |
| Output Queue Length | Valu e | flink taskmanager job tas _ _ _ k buffers outputQueueLe _ _ ngth | userId and jobId | The length of the output queue. |

**I/O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total Number of Input Bytes | Bytes | flink taskmanager job tas _ _ _ k operator numBytesIn _ _ | userId and jobId | The total number of input bytes. |
| Total Number of Input Bytes per Second (Local) | Bytes/s | flink taskmanager job tas _ _ _ k numBytesInLocalPerSec _ ond | userId and jobId | The total number of input bytes per second of a local system. |
| Total Number of Input Bytes per Second (Remote) | Bytes/s | flink taskmanager job tas _ _ _ k numBytesInRemotePerS _ econd | userId and jobId | The total number of input bytes per second of a remote system. |
| Total Number of Input Buffers per Second (Local) | Bytes/s | flink taskmanager job tas _ _ _ k numBuffersInLocalPerSe _ cond | userId and jobId | The total amount of data imported from buffers per second in a local system. |

| Total Number of Input Buffers per Second (Remote) | Bytes/s | flink taskmanager job tas _ _ _ k numBuffersInRemotePer _ Second | userId and jobId | The total amount of data imported from buffers per second in a remote system. |
|---|---|---|---|---|
| Total Number of Input Bytes per Second (Operator) | Bytes/s | flink taskmanager job tas _ _ _ k operator numBytesInPer _ _ Second | userId and jobId | The total number of input bytes received by an operator per second. |
| Total Number of Output Bytes | Bytes | flink taskmanager job tas _ _ _ k operator numBytesOut _ _ | userId and jobId | The total number of output bytes. |
| Total Number of Output Bytes per Second | Bytes/s | flink taskmanager job tas _ _ _ k numBytesOutPerSecond _ | userId and jobId | The total number of output bytes per second. |
| Total Number of Output Buffers per Second | Bytes/s | flink taskmanager job tas _ _ _ k numBuffersOutPerSecon _ d | userId and jobId | The total number of bytes that are sent from buffers per second. |
| Total Number of Output Bytes per Second (Operator) | Bytes/s | flink taskmanager job tas _ _ _ k operator numBytesOutP _ _ erSecond | userId and jobId | The total number of output bytes sent by an operator per second. |
| Total Number of Data Records That Flow into Each Subtask | Count | flink taskmanager job tas _ _ _ k numRecordsIn _ | userId and jobId | The total amount of data received by each subtask. |
| Total Number of Data Records That Are Exported by Each Subtask | Count | flink taskmanager job tas _ _ _ k numRecordsOut _ | userId and jobId | The total amount of data exported by each subtask. |

| Total Number of Data Records That Flow into Each Subtask per Second | Count/ s | flink taskmanager job tas _ _ _ k numRecordsInPerSecond _ | userId and jobId | The total amount of data received by each subtask per second. |
|---|---|---|---|---|
| Total Number of Data Records That Are Exported by Each Subtask per Second | Count/ s | flink taskmanager job tas _ _ _ k numRecordsOutPerSeco _ nd | userId and jobId | The total amount of data exported by each subtask per second. |
| Time Required by Each Subtask to Export the Last Data Record to the Sink | Second s | flink taskmanager job tas _ _ _ k operator currentSendTi _ _ me | userId and jobId | The duration that is required by each subtask to export the last data record to the sink. |

**Watermark**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Time When Each Task Receives the Latest Watermark | Millis econ ds | flink taskmanager job ta _ _ _ sk currentInputWatermar _ k | userId and jobId | The time when each task receives the latest watermark. |
| Time When Each Task Receives the Latest Watermark (Operator) | Millis econ ds | flink taskmanager job ta _ _ _ sk operator currentInput _ _ Watermark | userId and jobId | The time when each task receives the last watermark in an operator. |
| Time When Each Task Transmits the Latest Watermark (Operator) | Millis econ ds | flink taskmanager job ta _ _ _ sk operator currentOutpu _ _ tWatermark | userId and jobId | The time when each task sends the last watermark in an operator. |
| Watermark Latency | Millis econ ds | flink taskmanager job ta _ _ _ sk operator watermarkLa _ _ g | userId and jobId | The latency of watermarks. |

**CPU**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU Load of a Single JM | % | flink jobmanager Statu _ _ s JVM CPU Load _ _ _ | userId and jobId | The CPU load of a JobManager. |
| CPU Load of a Single TM | % | flink taskmanager Stat _ _ us JVM CPU Load _ _ _ | userId and jobId | The CPU load of a TaskManager. |
| CPU Utilization of a Single TM | % | flink taskmanager Stat _ _ us ProcessTree CPU Us _ _ _ age | userId and jobId | The CPU utilization of a TaskManager. |

**Memory**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Heap Memory of JM (Used) | Byte s | flink jobmanager Status _ _ JVM Memory Heap Use _ _ _ _ d | userId and jobId | The heap memory used by the JobManager. |
| Heap Memory of JM (Committed) | Byte s | flink jobmanager Status _ _ JVM Memory Heap Co _ _ _ _ mmitted | userId and jobId | The heap memory allocated by the JobManager. |
| Heap Memory of JM (Max) | Byte s | flink jobmanager Status _ _ JVM Memory Heap Ma _ _ _ _ x | userId and jobId | The maximum heap memory that can be used by the JobManager. |
| Non-Heap Memory for JM (Used) | Byte s | flink jobmanager Status _ _ JVM Memory NonHeap _ _ _ Used _ | userId and jobId | The non-heap memory that is allocated by the JobManager. |
| Non-Heap Memory of JM (Committed) | Byte s | flink jobmanager Status _ _ JVM Memory NonHeap _ _ _ Committed _ | userId and jobId | The non-heap memory that is allocated by the JobManager. |

| Non-Heap Memory of JM (Max) | Byte s | flink jobmanager Status _ _ JVM Memory NonHeap _ _ _ Max _ | userId and jobId | The maximum non-heap memory that can be used by the JobManager. |
|---|---|---|---|---|
| Used Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory Heap Us _ _ _ _ ed | userId and jobId | The heap memory used by the TaskManager |
| Committed Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory Heap Co _ _ _ _ mmitted | userId and jobId | The heap memory allocated by the TaskManager. |
| Max. Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory Heap M _ _ _ _ ax | userId and jobId | The maximum heap memory that can be used by the TaskManager. |
| Used Non-Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory NonHea _ _ _ p Used _ | userId and jobId | The non-heap memory used by the TaskManager. |
| Committed Non-Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory NonHea _ _ _ p Committed _ | userId and jobId | The non-heap memory allocated by the TaskManager. |
| Max. Non-Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory NonHea _ _ _ p Max _ | userId and jobId | The maximum non-heap memory that can be used by the TaskManager. |
| Memory of the Entire Process by Using Linux | Byte s | flink taskmanager Statu _ _ s ProcessTree Memory _ _ _ RSS | userId and jobId | The amount of memory consumed by the entire process on Linux. |

**JVM**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Threads of JM | Count | flink jobmanager Status _ _ _ JVM Threads Count _ _ | userId and jobId | The number of threads of the JobManager. |
| Number of Threads of TM | Count | flink taskmanager Statu _ _ s JVM Threads Count _ _ _ | userId and jobId | The number of threads of a TaskManager. |
| Number of GCs on JM (ParNew) | Count | flink jobmanager Status _ _ _ JVM GarbageCollector Pa _ _ rNew Count _ | userId and jobId | The number of GCs performed by using ParNew on a JobManager. |
| Number of GCs on JM (ConcurrentMarkSwe ep) | Count | flink jobmanager Status _ _ _ JVM GarbageCollector Co _ _ ncurrentMarkSweep Cou _ nt | userId and jobId | The number of GCs performed by using Concurrent Mark Sweep (CMS). |
| Duration of Each GC on JM (ParNew) | Millisec onds | flink jobmanager Status _ _ _ JVM GarbageCollector Pa _ _ rNew Time _ | userId and jobId | The duration of each GC performed by using ParNew. |
| Duration of Each GC on JM (ConcurrentMarkSwe ep) | Millisec onds | flink jobmanager Status _ _ _ JVM GarbageCollector Co _ _ ncurrentMarkSweep Tim _ e | userId and jobId | The duration of each GC performed by using CMS. |
| Number of GCs on TM (ParNew) | Count | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ParNew Count _ | userId and jobId | The number of GCs performed by using ParNew on a TaskManager. |
| Number of GCs on TM (ConcurrentMarkSwe ep) | Count | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ConcurrentMarkSweep C _ ount | userId and jobId | The number of GCs performed by using CMS on a TaskManager. |

| Duration of Each GC on JM (ParNew) | Millisec onds | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ParNew Time _ | userId and jobId | The duration of each GC performed by using ParNew on a TaskManager. |
|---|---|---|---|---|
| Duration of Each GC on JM (ConcurrentMarkSwe ep) | Millisec onds | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ConcurrentMarkSweep Ti _ me | userId and jobId | The duration of each GC performed by using CMS on a TaskManager. |
| Total Classes Loaded After the JVM Where the JM Resides Is Created | Value | flink jobmanager Status _ _ _ JVM ClassLoader Classes _ _ Loaded |   | The total number of classes loaded after the Java Virtual Machine (JVM) where the JobManager resides is created. |
| Total Classes Unloaded After the JVM Where the JM Resides Is Created | Value | flink jobmanager Status _ _ _ JVM ClassLoader Classes _ _ Unloaded | userId and jobId | The total number of classes unloaded after the JVM where the JobManager resides is created. |
| Total Classes Loaded After the JVM Where the TM Resides Is Created | Value | flink taskmanager Statu _ _ s JVM ClassLoader Class _ _ _ esLoaded | userId and jobId | The total number of classes loaded after the JVM where the TaskManager resides is created. |
| Total Classes Unloaded After the JVM Where the TM Resides Is Created | Value | flink taskmanager Statu _ _ s JVM ClassLoader Class _ _ _ esUnloaded | userId and jobId | The total number of classes unloaded after the JVM where the TaskManager resides is created. |

**CSG**

Set the **Namespace** parameter to **acs_csg_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| csg gateway cpu us _ _ _ age percentage _ | % | csg gateway cpu usage _ _ _ percentage _ | userId and instanceId | The CPU utilization of the gateway. |
| csg gateway memor _ _ y usage percentage _ _ | % | csg gateway memory u _ _ _ sage percentage _ | userId and instanceId | The memory usage of the gateway. |
| csg gateway cache _ _ _ usage percentage _ | % | csg gateway cache usa _ _ _ ge percentage _ | userId, instanceId, and shareName | The cache space usage of the gateway. |
| csg gateway running _ _ state _ | Count | csg gateway running st _ _ _ ate | userId, instanceId, and shareName | The status of the gateway. |
| csg gateway share _ _ _ upload queue num _ _ | Count | csg gateway file share _ _ _ _ upload queue num _ _ | userId, instanceId, and shareName | The number of queued requests for uploading files to a bucket. |
| csg gateway file sha _ _ _ re remaining meta s _ _ _ pace bytes _ | Bytes | csg gateway file share _ _ _ _ remaining meta space _ _ _ bytes | userId, instanceId, and shareName | The remaining metadata space for gateway file share. |
| csg gateway file sha _ _ _ re throttling state _ _ | Count | csg gateway file share _ _ _ _ throttling state _ | userId, instanceId, and shareName | The throttling status of the gateway share. |
| csg gateway file sha _ _ _ re read write rate K _ _ _ _ Bps | Kbit/s | csg gateway file share _ _ _ _ read write rate KBps _ _ _ | userId, instanceId, and shareName | The read and write rate of gateway file share. |

| csg gateway file sha _ _ _ re read IOPS _ _ | Kbit/s | csg gateway file share _ _ _ _ read IOPS _ | userId, instanceId, and shareName | The read IOPS of gateway file share. |
|---|---|---|---|---|
| csg gateway file sha _ _ _ re write IOPS _ _ | Kbit/s | csg gateway file share _ _ _ _ write IOPS _ | userId, instanceId, and shareName | The write IOPS of gateway file share. |
| csg gateway file sha _ _ _ re upload rate KBps _ _ _ | Kbit/s | csg gateway file share _ _ _ _ upload rate KBps _ _ | userId, instanceId, and shareName | The rate at which the shared file is uploaded to OSS buckets. |

**Lindorm**

Set the **Namespace** parameter to **acs_lindorm**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Wide table engine-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Wide Table Engine Metrics-Read Requests-Read Request Volume | Rows/s | WTEM RR readRequestVolu _ _ me | userId and instanceId | The number of read requests per second in the wide table engine. |
| Wide table engine metric-read request- read average RT | Millisec onds | WTEM RR readAverageRT _ _ | userId and instanceId | The average response time of read requests in the wide table engine. |
| Wide Table Engine Metrics-Read Request-Read Traffic | Value | WTEM RR readTraffic _ _ | userId and instanceId | The read traffic in the wide table engine. |
| Wide table engine metric-read request- Get request volume | Rows/s | WTEM RR getRequestVolum _ _ e | userId and instanceId | The number of GET requests per second in the wide table engine. |

| Wide table engine metric-read request- Get average RT | Millisec onds | WTEM RR getAverageRT _ _ | userId and instanceId | The average response time of GET requests in the wide table engine. |
|---|---|---|---|---|
| Wide table engine metric-read request- Get P99 RT | Millisec onds | WTEM RR getP99RT _ _ | userId and instanceId | The average P99 response time of read requests in the wide table engine. |
| Wide table engine metrics-read requests-Scan requests | Reques ts/s | WTEM RR scanRequestVolu _ _ me | userId and instanceId | The number of SCAN requests per second in the wide table engine. |
| Wide table engine metric-read request- Scan average RT | Millisec onds | WTEM RR scanAverageRT _ _ | userId and instanceId | The average response time of SCAN requests in the wide table engine. |
| Wide table engine metric-read request- Scan P99 RT | Millisec onds | WTEM RR scanP99RT _ _ | userId and instanceId | The average P99 response time of SCAN requests in the wide table engine. |
| Wide Table Engine Metrics-Write Requests-Write Request Volume | Reques ts/s | WTEM WR writeRequestVol _ _ ume | userId and instanceId | The number of requests per second in the wide table engine. |
| Wide Table Engine Metrics-Write Request-Write Average RT | Millisec onds | WTEM WR writeRequests _ _ | userId and instanceId | The average response time of write request in the wide table engine. |
| Wide Table Engine Metrics-Write Request-Write Traffic | Value | WTEM WR writeTraffic _ _ | userId and instanceId | The write traffic in the wide table engine. |

| Wide Table Engine Metrics-Write Requests-Put Total Requests | Reques ts/s | WTEM WR putTotalRequest _ _ Volume | userId and instanceId | The number of PUT requests per second in the wide table engine. |
|---|---|---|---|---|
| Wide table engine metric-write request- Put average RT | Millisec onds | WTEM WR putAverageRT _ _ | userId and instanceId | The average response time of PUT requests in the wide table engine. |
| Wide Table Engine Metrics-Write Requests-Put Requests | Reques ts/s | WTEM WR putRequestVolu _ _ me | userId and instanceId | The number of PUT requests per second in the wide table engine. |
| WTEM WR exceeding _ _ MemstoreUpperLimit | Count | WTEM WR exceedingMemst _ _ oreUpperLimit | userId and instanceId | The number of times that the memstore limit has been exceeded. |
| Wide table engine metric-write request- Put P99 RT | Millisec onds | WTEM WR putP99RT _ _ | userId and instanceId | The average P99 response time of PUT requests in the wide table engine. |
| Wide table engine metric -- SQLv2- Number of SQL connections | Count | WTEM SQLv2 sQLConnectio _ _ nCount | userId and instanceId | The number of SQL connections. |
| Wide Table Engine Metrics-SQLv2- Number of select requests | Reques ts/s | WTEM SQLv2 selectRequest _ _ Count | userId and instanceId | The number of SELECT requests per second. |
| Wide table engine metrics-SQLv2-select request p99 time consumption | Millisec onds | WTEM SQLv2 selectP99Req _ _ uestTime | userId and instanceId | The average P99 response time of SELECT requests in the wide table engine. |
| Wide Table Engine Metrics-SQLv2- Number of upsert requests | Reques ts/s | WTEM SQLv2 upsertReques _ _ tCount | userId and instanceId | The number of UPSERT requests. |

| Wide Table Engine Metrics-SQLv2-upsert Request p99 Time | Millisec onds | WTEM SQLv2 upsertP99Req _ _ uestTime | userId and instanceId | The average P99 response time of UPSERT requests. |
|---|---|---|---|---|
| Wide Table Engine Metrics-SQLv2- Number of delete requests | Reques ts/s | WTEM SQLv2 deleteReques _ _ tCount | userId and instanceId | The number of DELETE requests. |
| Wide table engine metric -- SQLv2- delete request p99 time consumed | Millisec onds | WTEM SQLv2 deleteP99Req _ _ uestTime | userId and instanceId | The average P99 response time of DELETE requests. |
| WTEM CL rSRegionC _ _ ount | Count | WTEM CL rSRegionCount _ _ | userId and instanceId | The number of regions managed by the region server. |
| Wide Table Engine Metrics-Cluster Load- Handler Queue Length | Count | WTEM CL handlerQueueLen _ _ gth | userId and instanceId | The number of requests queued on the Handler. |
| Wide Table Engine Metrics-Cluster Load- Compaction Queue Length | Count | WTEM CL compactionQueu _ _ eLength | userId and instanceId | The number of requests in the compaction queue. |
| Wide Table Engine metric-SQLv2-median time spent on delete requests | Millisec onds | WTEM SQLv2 deleteMedian _ _ RequestTime | userId and instanceId | The P50 response time of DELETE requests. |
| Wide table engine metric-SQLv2-median upsert request time | Millisec onds | WTEM SQLv2 upsertMedian _ _ RequestTime | userId and instanceId | The P50 response time of UPSERT requests. |
| Wide table engine metric-SQLv2-median time spent on select requests | Millisec onds | WTEM SQLv2 selectMedian _ _ RequestTime | userId and instanceId | The P50 response time of SELECT requests. |

**Time series engine-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Timing Engine Metrics-Write Volume | Points/ s | TSEM WV _ | userId and instanceId | The amount of data written per second. |
| Timing Engine Metrics-Failure Amount | Points/ s | TSEM FV _ | userId and instanceId | The amount of data that fails to be written. |
| Timing Engine Metrics-Write Request Volume | Reques ts/s | TSEM writeRequestVolume _ | userId and instanceId | The number of write requests per second. |
| Time series engine metrics-write average RT | Millisec onds | TSEM writeAverageRT _ | userId and instanceId | The average response time of write requests. |
| Timing Engine Metrics-Write RT P99 | Millisec onds | TSEM writeRTP99 _ | userId and instanceId | The average P99 response time of write requests. |
| Time Series Engine Metrics-Read Request Volume | Reques ts/s | TSEM readRequestVolume _ | userId and instanceId | The number of read requests per second. |
| Time Series Engine Metrics-Number of Active Connections | Count | TSEM activeConnectionsCou _ nt | userId and instanceId | The number of active connections. |
| Time Series Engine Metrics-Number of Active Statements | Count | TSEM activesStatementCou _ nt | userId and instanceId | The number of active statements. |
| Timing Engine Metrics-Number of Active Resultsets | Count | TSEM activeResultSetCount _ | userId and instanceId | The number of active result sets. |
| Time Series Engine Metrics-Insert Rows | Rows/s | TSEM insertRowCount _ | userId and instanceId | The number of inserted rows. |
| Timing Engine Metrics-Select Number of Scan Lines | Rows/s | TSEM selectScanRowCount _ | userId and instanceId | The number of scanned rows. |

| Time Series Engine Metrics-Number of Select requests | Rows/s | TSEM selectRequestCount _ | userId and instanceId | The number of SELECT requests. |
|---|---|---|---|---|
| Time Series Engine metric-Select average RT | Millisec onds | TSEM selectAverageRT _ | userId and instanceId | The average response time of SELECT requests. |
| Time series engine metrics-Select time consumption P99 | Millisec onds | TSEM selectTimeP99 _ | userId and instanceId | The average P99 response time of SELECT requests. |
| Time Series Engine Metrics - Client Connections | Count | TSEM clientConnectionCoun _ t | userId and instanceId | The number of client connections. |
| Time Series Engine Metrics - Average RT for API-based Multi- value Query | Millisec onds | TSEM queryAverageRT mqu _ _ ery | userId and instanceId | The average response time of multi-value queries based on API. |
| Time Series Engine Metrics - Average RT for API-based Single- value Query | Millisec onds | TSEM TSEM queryAverageR _ _ T query _ | userId and instanceId | The average response time of single-value queries based on API. |
| Time Series Engine Metrics - RT for API- based Multi-value Query (P99) | Millisec onds | TSEM queryRTP99 mquery _ _ | userId and instanceId | The P99 response time of multi-value queries. |
| Time Series Engine Metrics - RT for API- based Single-value Query (P99) | Millisec onds | TSEM queryRTP99 query _ _ | userId and instanceId | The P99 response time of single-value queries. |
| Time Series Engine Metrics-Number of Timelines | Count | TSEM timelineCount _ | userId and instanceId | The number of time series. |

**File engine-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| File Engine Metrics- Storage (Hot Storage) Usage- Storage Usage | Value | FEM SU storageUsed _ _ | userId and instanceId | The usage of hot storage space. |
|---|---|---|---|---|
| File Engine Metrics- Storage (Hot Storage) Usage-Total Storage | Value | FEM SU totalStorage _ _ | userId and instanceId | The total hot storage space. |
| File Engine Metrics- Storage (Hot Storage) Usage- (lindorm Multi-AZ) | Value | FEM SU dfs fsnamesystem _ _ _ _ capacitytotal | userId and instanceId | The usage of hot storage in multiple zones of Lindorm. |
| File Engine Metrics- Storage (Hot Storage) Usage- (Lindorm Multi-AZ) | Value | FEM SU dfs fsnamesystem _ _ _ _ capacityused | userId and instanceId | The usage of hot storage in multiple zones of Lindorm. |
| File Engine Indicator- Storage (Hot Storage) Level | % | FEM sWatermark _ | userId and instanceId | The usage of the hot storage. |
| File Engine Metrics- NameNode Operands (times/sec)- create file ops _ _ | Operati ons/s | FEM NO create file ops _ _ _ _ | userId and instanceId | The number of times that files are created on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- delete file ops _ _ | Operati ons/s | FEM NO delete file ops _ _ _ _ | userId and instanceId | The number of times that files are deleted from NameNodes per second. |

| File Engine Metrics- NameNode Operands (times/sec)- add block ops _ _ | Operati ons/s | FEM NO add block ops _ _ _ _ | userId and instanceId | The number of times that blocks are added to NameNodes per second. |
|---|---|---|---|---|
| File Engine Metrics- NameNode Operands (times/sec)- get blockloc ops _ _ | Operati ons/s | FEM NO _ | userId and instanceId | The number of times that blocks are queried on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- get file info ops _ _ _ | Operati ons/s | FEM NO get file info ops _ _ _ _ _ | userId and instanceId | The number of times that files are queried on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- list dir ops _ _ | Operati ons/s | FEM NO list dir ops _ _ _ _ | userId and instanceId | The number of times that directories are queried on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- block report ops _ _ | Operati ons/s | FEM NO block report ops _ _ _ _ | userId and instanceId | The number of times that reports of blocks are exported on NameNodes per second. |
| File engine metrics- DataNode read traffic | Value | FEM dataNodeReadTraffic _ | userId and instanceId | The read traffic of DataNodes. |
| File engine metrics- DataNode write traffic | Value | FEM dataNodeWriteTraffic _ | userId and instanceId | The write traffic of DataNodes. |

**Container Service Monitoring**

Set the **Namespace** parameter to **acs_k8s**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Cluster**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU resource limit | Cores | cluster.cpu.limit | user id and _ cluster name _ | The maximum number of CPU cores that can be used by a container. |
| CPU resource request | Cores | cluster.cpu.request | user id and _ cluster name _ | The minimum number of CPU cores requested by a container during scheduling. |
| CPU usage | Cores | cluster.cpu.usage rate _ | user id and _ cluster name _ | The CPU utilization. |
| cpu usage of cluster dimension | % | cluster.cpu.utilization | user id and _ cluster name _ | The CPU utilization. |
| Filesystem resource available | Bytes | cluster.filesystem.available | user id and _ cluster name _ | The size of the file system that is available to the cluster. |
| Filesystem resource limit | Bytes | cluster.filesystem.limit | user id and _ cluster name _ | The maximum number of file systems in the cluster. |
| Cluster Memory Limits | Bytes | cluster.memory.limit | user id and _ cluster name _ | The maximum memory of the cluster. |
| Cluster Memory Requests | Bytes | cluster.memory.request | user id and _ cluster name _ | The memory requested by the cluster. |
| cluster.memory.utiliz ation | % | cluster.memory.utilization | user id and _ cluster name _ | The memory usage of the cluster. |

**Node**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| node.cpu.allocatabl e | Cores | node.cpu.allocatable | userId, cluster, and node | node.cpu.node allocatable _ |
|---|---|---|---|---|
| node.cpu.capacity | Cores | node.cpu.capacity | userId, cluster, and node | node.cpu.capa city |
| node.cpu.limit | Cores | node.cpu.limit | userId, cluster, and node | node.cpu.limit |
| node.cpu.oversale r _ ate | % | node.cpu.oversale rate _ | userId, cluster, and node | The oversold ratio of CPU resources. |
| node.cpu.request | Cores | node.cpu.request | userId, cluster, and node | The CPU resources requests by the node. |
| node.cpu.reservatio n | core | node.cpu.reservation | userId, cluster, and node | The reserved CPU resources of the node. |
| node.cpu.usage rat _ e | Cores | node.cpu.usage rate _ | userId, cluster, and node | The CPU usage. |
| node.cpu.utilization | % | node.cpu.utilization | userId, cluster, and node | The CPU utilization. |
| node.filesystem.avai lable | Count | node.filesystem.available | userId, cluster, and node | The number of file systems that can be used by the node. |
| node.filesystem.ino des | Count | node.filesystem.inodes | userId, cluster, and node | The number of file systems that can be used by the node. |
| node.filesystem.limi t | Count | node.filesystem.limit | userId, cluster, and node | The number of file systems that can be used by the node. |

| node.filesystem.usa ge | Count | node.filesystem.usage | userId, cluster, and node | The file system usage. |
|---|---|---|---|---|
| node.memory.alloca table | GB | node.memory.allocatable | userId, cluster, and node | The memory allocated to the node. |
| node.memory.cache | GB | node.memory.cache | userId, cluster, and node | The memory cache of the node. |
| node.memory.capac ity | Count | node.memory.capacity | userId, cluster, and node | The memory capacity of the node. |
| node.memory.limit | Count | node.memory.limit | userId, cluster, and node | The maximum memory that can be used by the node. |
| node.memory.major page faults _ _ | Count | node.memory.major page f _ _ aults | userId, cluster, and node | The number of major page faults that occur on the node. |
| node.memory.major page faults rate _ _ _ | Count | node.memory.major page f _ _ aults rate _ | userId, cluster, and node | The rate at which major page faults occur on the node. |
| node.memory.overs ale rate _ | % | node.memory.oversale rate _ | userId, cluster, and node | The oversold ratio of memory resources. |
| node.memory.page _ faults | Count | node.memory.page faults _ | userId, cluster, and node | The number of page faults that occur on the node. |
| node.memory.page _ faults rate _ | Count | node.memory.page faults r _ _ ate | userId, cluster, and node | The rate at which page faults occur on the node. |

| node.memory.reque st | Count | node.memory.request | userId, cluster, and node | The rate at which page faults occur on the node. |
|---|---|---|---|---|
| node.memory.reser vation | Count | node.memory.reservation | userId, cluster, and node | The reserved memory of the node. |
| node.memory.rss | Count | node.memory.rss | userId, cluster, and node | The resident set size (RSS). |
| node.memory.usage | Count | node.memory.usage | userId, cluster, and node | The used memory. |
| node.memory.utiliza tion | Count | node.memory.utilization | userId, cluster, and node | The memory usage. |
| node.memory.worki ng set _ | Count | node.memory.working set _ | userId, cluster, and node | The working set memory of the node. |
| node.network.rx err _ ors | Count | node.network.rx errors _ | userId, cluster, and node | The number of receive errors that occur on the network of the node. |
| node.network.rx err _ ors rate _ | % | node.network.rx errors rate _ _ | userId, cluster, and node | The rate at which receive errors occur on the network of the node. |
| node.network.rx rat _ e | Count/ s | node.network.rx rate _ | userId, cluster, and node | The number of send errors that occur on the network of the node. |
| node.network.tx err _ ors rat _ | % | node.network.tx errors rat _ _ | userId, cluster, and node | The rate at which send errors occur on the network of the node. |

**Pod**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| pod.cpu.limit | Cores | pod.cpu.limit | userId, cluster, namespace, type, app, and pod | The maximum amount of CPU resources that can be used by the pod. |
| pod.cpu.oversale rat _ e | % | pod.cpu.oversale rate _ | userId, cluster, namespace, type, app, and pod | The oversold ratio of CPU resources. |
| pod.cpu.request | Cores | pod.cpu.request | userId, cluster, namespace, type, app, and pod | The minimum amount of CPU resources requested by the pod. |
| pod.cpu.usage rate _ | Cores | pod.cpu.usage rate _ | userId, cluster, namespace, type, app, and pod | The CPU usage of the pod. |
| pod.cpu.utilization | % | pod.cpu.utilization | userId, cluster, namespace, type, app, and pod | The CPU utilization of the pod. |
| pod.filesystem.availa ble | Bytes | pod.filesystem.available | userId, cluster, namespace, type, app, and pod | The available size of the file system in the pod. |
| pod.filesystem.limit | Bytes | pod.filesystem.limit | userId, cluster, namespace, type, app, and pod | The maximum size of file systems in the pod. |
| pod.filesystem.usage | Bytes | pod.filesystem.usage | userId, cluster, namespace, type, app, and pod | The file systems used by the pod. |
| pod.filesystem.utiliza tion | % | pod.filesystem.utilization | userId, cluster, namespace, type, app, and pod | The file system usage of the pod. |

| pod.memory.cache | Bytes | pod.memory.cache | userId, cluster, namespace, type, app, and pod | The memory resource cache of the pod. |
|---|---|---|---|---|
| pod.memory.limit | Bytes | pod.memory.limit | userId, cluster, namespace, type, app, and pod | The maximum memory that can be allocated to the pod. |
| pod.memory.oversal e rate _ | % | pod.memory.oversale rate _ | userId, cluster, namespace, type, app, and pod | The oversold ratio of memory resources. |
| pod.memory.request | Bytes | pod.memory.request | userId, cluster, namespace, type, app, and pod | The minimum amount of memory resources requested by the pod. |
| pod.memory.rss | Bytes | pod.memory.rss | userId, cluster, namespace, type, app, and pod | The RSS of the pod. |
| pod.memory.utilizati on | % | pod.memory.utilization | userId, cluster, namespace, type, app, and pod | The memory usage of the pod. |
| pod.memory.working set _ | Bytes | pod.memory.working set _ | userId, cluster, namespace, type, app, and pod | The amount of memory of the container. |
| pod.network.rx error _ s rate _ | Count/ s | pod.network.rx errors rate _ _ | userId, cluster, namespace, type, app, and pod | The rate at which receive errors occur in the network of the pod. |
| pod.network.rx rate _ | Bytes/s | pod.network.rx rate _ | userId, cluster, namespace, type, app, and pod | The rate at which the pod receives data. |

| pod.network.tx error _ s rate _ | Bytes/s | pod.network.tx errors rate _ _ | userId, cluster, namespace, type, app, and pod | The rate at which send errors occur in the network of the pod. |
|---|---|---|---|---|
| pod.network.tx rate _ | Bytes/s | pod.network.tx rate _ | userId, cluster, namespace, type, app, and pod | The rate at which the pod sends data. |

**Deployment**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| deployment.cpu.limit | Cores | deployment.cpu.limit | userId, cluster, namespace, type, and app | The maximum amount of CPU resource that can be allocated to the Deployment. |
| deployment.cpu.usag e rate _ | Cores | deployment.cpu.usage rate _ | userId, cluster, namespace, type, and app | The CPU resources used by the Deployment. |
| deployment.filesyste m.available | Bytes | deployment.filesystem.avai lable | userId, cluster, namespace, type, and app | The size of the file system available to the Deployment. |
| deployment.filesyste m.limit | Bytes | deployment.filesystem.limit | userId, cluster, namespace, type, and app | The maximum number of file systems that can be used by the Deployment. |
| deployment.filesyste m.usage | Bytes | deployment.filesystem.usa ge | userId, cluster, namespace, type, and app | The used size of the file system of the Deployment. |
| deployment.filesyste m.utilization | % | deployment.filesystem.utili zation | userId, cluster, namespace, type, and app | The file system usage of the Deployment. |

| deployment.memory.l imit | Bytes | deployment.memory.limit | userId, cluster, namespace, type, and app | The maximum size of memory that can be allocated to the Deployment. |
|---|---|---|---|---|
| deployment.memory. request | Bytes | deployment.memory.reque st | userId, cluster, namespace, type, and app | The minimum amount of memory resources requested by the Deployment. |
| deployment.memory. working set _ | Bytes | deployment.memory.worki ng set _ | userId, cluster, namespace, type, and app | The working set memory of the Deployment. |
| deployment.network.r x errors rate _ _ | Bytes/s | deployment.network.rx err _ ors rate _ | userId, cluster, namespace, type, and app | The rate at which receive errors occur in the network of the Deployment. |
| deployment.network.t x errors rate _ _ | Bytes/s | deployment.network.tx err _ ors rate _ | userId, cluster, namespace, type, and app | The rate at which send errors occur in the network of the Deployment. |

### 1.3 API Reference

#### 1.3.1 Cloud Products

##### 1.3.1.1 DescribeProjectMeta

You can call this operation to query information of monitored services in Cloud Monitor. The information obtained by this operation includes the service description, namespace, and tags.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action |   | String | Yes | DescribeProject Meta |   | The operation that you want to perform. Set the value to DescribeProjectMeta. |   |   |
|---|---|---|---|---|---|---|---|---|
| callerType |   | String | No | "" |   | The type of the caller. |   |   |
|   |   |   |   |   |   | The tags of metrics. You can specify tags of metrics to filter services. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag |   |   |
|   |   |   |   |   |   |   | [{"name":"Tag |   |
|   |   |   |   |   |   | name","value":"Tag value"}, |   |   |
|   |   |   |   |   |   | {"name":"Tag name","value":"Tag |   |   |
|   |   |   |   |   |   | value"}] |   |   |
| Labels |   | String | No | [{"name":"prod uct","value":"EC S"}] |   |   |   |   |

| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
|---|---|---|---|---|
| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. Note Apsara Stack does not limit the value of this parameter. If you want to view all desired entries on a small number of pages, set this parameter to a greater value. |
| RequestId | string | No | sdsdsdd | The ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RequestId | String | 4C2061B2-3B1B- 43BF-A4A4- C53426F479C0 | The ID of the request. |
| Resources | Array | N/A | The information of services found. |
| Resource | N/A | N/A | The information of a service found. |
| Description | String | CDN | The description of the service. |

|   |   |   |   |   |   | The tags of metrics. Services were filtered based on the specified tags. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag name","value":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag name","value":"Tag |   |
|   |   |   |   |   |   | value"},{"name":"Tag |   |   |
|   |   |   |   |   |   | name","value":"Tag value"}] |   |   |
|   | Labels | String |   |   | [{"groupFlag":true }] |   |   |   |
|   | Namespace | String |   |   | acs cdn _ | The namespace of the service, which is used to distinguish between services. Typically, the value of the format is acs Abbreviation of the service _ name . |   |   |
|   |   |   |   |   |   |   | acs Abbreviation of the service _ |   |
|   |   |   |   |   |   | name |   |   |
|   | Success | Boolean |   |   | true | Indicates whether the call was successful. |   |   |

| Total | String | 12 | The total number of entries returned. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeProjectMeta &<Common request parameters>
```

Sample success responses The response content varies with the services that are actually monitored. `JSON` format `{`

```json
 "PageNumber":1,
 "PageSize":5,
 "RequestId":"4C2061B2-3B1B-43BF-A4A4-C53426F479C0",
 "Success":true,
 "Code":200,
 "Total":62,
 "Resources":{
  "Resource":[{
     "Description": "ECS",
     "Labels": "[{\"name\":\"product\",\"value\":\"ECS\"},
{\"name\":\"productCategory\",\"value\":\"ecs,ecs_net_interface,hpc_node,hpc_cluster\"}, {\"name\":\"groupFlag\",\"value\":\"true\"},{\"name\":\"cnName\",\"value\":\"ECS\"},{\" name\":\"enName\",\"value\":\"ECS\"}]",
     "Namespace": "acs_ecs_dashboard"
```

`},` `]` `}` `}`

##### 1.3.1.2 DescribeMetricLast

Queries the latest monitoring data of a monitored object.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricL ast | The operation that you want to perform. Set the value to DescribeMetricLast. |

| MetricName | String | Yes | CPUUtilization | The name of the monitoring metric. |   |   |   |
|---|---|---|---|---|---|---|---|
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. This parameter is used to differentiate services. Format: acs service name. _ |   |   |   |
| Dimensions | String | No | [{"instanceId":" XXXXXX"}] | The dimensions based on which the monitoring data of the specified resource is queried. The value is a collection of key- value pairs. A typical key- value pair is instanceId:XXXXXX . You can specify up to 20 instance IDs in each call. Each key or value can be 1 to 64 bytes in length. A key or value that contains more than 64 characters is truncated and the first 64 bytes are retained. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward slashes (/), _ and backslashes (\). Note If you set Dimensions to ordered strings in the request, the value of this parameter is a key-value map expressed in JSON strings. |   |   |   |
|   |   |   |   |   |   | key- |   |
|   |   |   |   |   | key- |   |   |
| StartTime | String | No | 2019-01-31 10:00:00 | The beginning of the time range to query. This value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. Note You can query data in a time range that spans 31 days at most within the last 270 days. |   |   |   |

|   | value |   |
|---|---|---|
|   | value |   |

| EndTime | String | No | 2019-01-31 10:10:00 | The end of the time range to query. This value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. Note You can query data within the last 270 days. |
|---|---|---|---|---|
| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression that is used to calculate the query results in real time. |
| Length | String | No | 1000 | The number of entries per page. Default value: 1000. |
| NextToken | String | No | 1576143285000 9dd70bb64cff1f 0fff6c0b08ffff07 3be5fb1e785e2 b020f7fed9b5e1 37bd810a6d6cff 5ae**** | The pagination token. If the number of results exceeds the maximum number of entries allowed per page, a pagination token is returned. This pagination token can be used as a request parameter to retrieve a new page of results. If a response does not contain pagination tokens, all query results are returned. |
| Period | String | No | 60 | The interval at which the monitoring data is queried. In most cases, the interval is the same as that for reporting metric data. Unit: seconds. If you do not specify this parameter, raw data is queried at the reporting interval specified when the corresponding metric was created. If a statistical period was specified for the corresponding alert rule, raw data is queried based on the statistical period. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 021472A6-25E3- 4094-8D00- BA4B6A5486C3 | The request ID. |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request was successful. |
| Success | Boolean | true | Indicates whether the request was successful. |
| Period | String | 60 | The interval at which the monitoring data was queried. Unit: seconds. |
| NextToken | String | xxxxxx | The pagination token. |
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The monitoring data. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricLast &MetricName=CPUUtilization &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<QueryMetricListResponse>
    <Period>60</Period>
    <Datapoints>
        <Datapoints>
            <timestamp>1490152860000</timestamp>
            <Maximum>100</Maximum>
            <userId> 123456789876****</userId>
            <Minimum>93.1</Minimum>
```

```xml
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.52</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490152920000</timestamp>
            <Maximum>100</Maximum>
            <userId> 123456789876**** </userId>
            <Minimum>92.59</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.49</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490152980000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.86</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.44</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153040000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.43</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.36</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153100000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>93.55</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.51</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153160000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>93.1</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.52</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153220000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.59</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.42</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153280000</timestamp>
            <Maximum>100</Maximum>
```

```xml
            <userId>123456789876****</userId>
            <Minimum>91.18</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.34</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153340000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.86</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.46</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153400000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.18</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.35</Average>
        </Datapoints>
    </Datapoints>
    <RequestId>6661EC50-8625-4161-B349-E0DD59002AB7</RequestId>
    <Success>true</Success>
    <Code>200</Code>
</QueryMetricListResponse>
```

`JSON` format `{`

```json
 "Period":"60",
 "Datapoints":[
```

`{`

```json
   "timestamp":1490152860000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490152920000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.49
```

`},` `{`

```json
   "timestamp":1490152980000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
```

`,`

```json
   "Average":99.44
```

`},` `{`

```json
   "timestamp":1490153040000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.43,
   "Average":99.36
```

`},` `{`

```json
   "timestamp":1490153100000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.55,
   "Average":99.51
```

`},` `{`

```json
   "timestamp":1490153160000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490153220000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.42
```

`},` `{`

```json
   "timestamp":1490153280000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.34
```

`},` `{`

```json
   "timestamp":1490153340000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.46
```

`},` `{`

```json
   "timestamp":1490153400000,
   "Maximum":100,
   "userId":"123456789876****",
```

```json
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.35
```

`}` `],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

`}`

##### 1.3.1.3 DescribeMetricList

Queries the monitoring data of a metric for a cloud service in a specific period. For more information about how to specify values for the Namespace, Project, Metric, Period, and Dimensions parameters for Apsara Stack services, see Major metrics of Apsara Stack services.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricLi st | The operation that you want to perform. Set the value to DescribeMetricList. |
| MetricName | String | Yes | cpu idle _ | The name of the monitoring metric. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. This parameter is used to differentiate services. Format: acs service name. _ |

| Dimensions | String | Yes | [{"instanceId": "i- abcdefgh12****" }] | The dimensions based on which the monitoring data of the specified resource is queried. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX. You can specify up to 10 instance IDs in each call. Each key or value can be 1 to 64 bytes in length. A key or value that contains more than 64 characters is truncated and the first 64 bytes are retained. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note If you set Dimensions to ordered strings in the request, the value of this parameter is a key-value map expressed in JSON strings. |   |
|---|---|---|---|---|---|
| EndTime | String | No | 2019-01-30 00:10:00 | The end of the time range to query. The following formats are supported: UNIX timestamp: the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. UTC time: the UTC time in the YYYY-MM-DDThh:mm:ssZ format. |   |
| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression that is used to calculate the query results in real time. Only the groupby expression is supported. This expression is similar to the GROUP BY statement that is used in databases. |   |
| Length | String | No | 1000 | The number of entries per page. Default value: 1000. |   |

|   | BY |
|---|---|

| NextToken | String | No | 1576148535000 9dd70bb64cff1f 0fff750b08ffff07 3be5fb1e785e2 b020f1a949d5e a14aea7fed82f0 1dd87311 | The pagination token. Note You do not need to specify this parameter if you only want to query entries on the first page. This pagination token can be used as a request parameter to retrieve a new page of results. If null is returned, all query results are returned. |
|---|---|---|---|---|
| Period | String | No | 60 | The interval at which the monitoring data is queried. Unit: seconds. Valid values: 60, 300, and 900, which represent 1 minute, 5 minutes, and 15 minutes, respectively. Note Specify this parameter based on your business requirements. For example, if you set this parameter to 60, only 1,000 records are returned, though a total of 1,440 records are generated. This is because the maximum number of records that can be returned for each query is 1,000. If you set this parameter to 300, 288 records are returned. |

| StartTime | String | No | 2019-01-30 00:00:00 | The beginning of the time range to query. The following formats are supported: UNIX timestamp: the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC. UTC time: the UTC time in the YYYY-MM-DDThh:mm:ssZ format. Note The period specified by StartTime and EndTime includes the point in time specified by EndTime but does not include the point in time specified by StartTime. The start time must be earlier than the end time. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3121AE7D-4AFF- 4C25-8F1D- C8226EBB1F42 | The request ID. |
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request was successful. |
| Success | Boolean | true | Indicates whether the request was successful. |
| NextToken | String | 15761441850009d d70bb64cff1f0fff6d 0b08ffff073be5fb1 e785e2b020f7fed9 b5e137bd810a6d6 cff5aee816 | The pagination token. Note You do not need to specify this parameter if you only want to query entries on the first page. This pagination token can be used as a request parameter to retrieve a new page of results. If null is returned, all query results are returned. |

| Period | String | 60 | The interval at which monitoring data was queried. Unit: seconds. Valid values: 60, 300, and 900. |
|---|---|---|---|
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The monitoring data. |
| Message | String | Success | The returned message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricList &MetricName=cpu_idle &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Period>60</Period> <Datapoints>
    <timestamp>1490152860000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.1</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.52</Average>
</Datapoints> <Datapoints>
    <timestamp>1490152920000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.59</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.49</Average>
</Datapoints> <Datapoints>
    <timestamp>1490152980000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.86</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.44</Average>
</Datapoints> <Dt it>
```

```xml
<Datapoints>
    <timestamp>1490153040000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.43</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.36</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153100000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.55</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.51</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153160000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.1</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.52</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153220000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.59</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.42</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153280000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.18</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.34</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153340000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.86</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.46</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153400000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.18</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
<Average>9935</Average>
```

```xml
    <Average>99.35</Average>
</Datapoints> <RequestId>6A5F022D-AC7C-460E-94AE-B9E75083D027</RequestId> <Success>true</Success> <Code>200</Code>
```

`JSON` format `{`

```json
 "Period":"60",
 "Datapoints":[
```

`{`

```json
   "timestamp":1490152860000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490152920000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.49
```

`},` `{`

```json
   "timestamp":1490152980000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.44
```

`},` `{`

```json
   "timestamp":1490153040000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.43,
   "Average":99.36
```

`},` `{`

```json
   "timestamp":1490153100000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.55,
   "Average":99.51
```

`},` `{`

```json
   "timestamp":1490153160000,
   "Maximum":100,
```

```json
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490153220000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.42
```

`},` `{`

```json
   "timestamp":1490153280000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.34
```

`},` `{`

```json
   "timestamp":1490153340000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.46
```

`},` `{`

```json
   "timestamp":1490153400000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.35
```

`}` `],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

`}`

##### 1.3.1.4 DescribeMetricMetaList

Queries the descriptions of time series metrics that are supported in CloudMonitor. This operation is used with DescribeMetricList and DescribeMetricLast.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

|   | Action | String |   | Yes |   | DescribeMetricM etaList | The operation that you want to perform. Set the value to DescribeMetricMetaList. |   |
|---|---|---|---|---|---|---|---|---|
|   | Namespace | String |   | Yes |   | acs kvstore _ | The namespace of the service. You can call the DescribeProjectMeta operation to query the namespace of each service. |   |
|   |   |   |   |   |   |   | The tags of the metric. You must specify the tags in the following format: [{&quot;name&quot;:&quot |   |
|   |   |   |   |   |   |   |   | [{&quot;name&quot;:&quot |
|   |   |   |   |   |   |   | ;Tag |   |
|   |   |   |   |   |   |   | key&quot;,&quot;value&quot;:&quo |   |
|   |   |   |   |   |   |   | t;Tag value&quot;}, |   |
|   |   |   |   |   |   |   | {&quot;name&quot;:&quot;Tag |   |
|   |   |   |   |   |   |   | key&quot;,&quot;value&quot;:&quo |   |
|   |   |   |   |   |   | [{&quot;name& | t;Tag value&quot;}] |   |
|   | Labels | String |   | No |   | quot;:&quot;pro ductCategory&q uot;,&quot;value &quot;:&quot;kv store old&quot; _ }] |   |   |
|   | MetricName | String |   | No |   | CPUUtilization | The name of the metric. The metric with the specified name is matched. |   |
|   | PageNumber | Integer |   | No |   | 1 | The number of the page to return. Default value: 1. |   |
|   | PageSize | Integer |   | No |   | 30 | The number of entries to return on each page. Default value: 30. |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. |

| Code | String |   | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |   |
|---|---|---|---|---|---|
| RequestId | String |   | 0CCE0AF0-053C- 4B13-A583- DC9A85785D49 | The request ID for troubleshooting. |   |
| Message | String |   | success | The error message returned. |   |
| Resources |   |   |   | The information of metrics found. |   |
| Resource |   |   |   | The information of a metric found. |   |
| Description | String |   | CPUUtilization | The description of the metric. |   |
| Dimensions | String |   | instanceId | The dimensions of the metric. Separate multiple dimensions with commas (,). |   |
|   |   |   | [{&quot;name&qu ot;:&quot;alertUnit &quot;,&quot;value &quot;:&quot;Byte s&quot;}, {&quot;name&quo t;:&quot;minAlertP eriod&quot;,&quot; | The tags of the metric. The value is a JSON array string in the format of [{&quot;name&quot;:&quot;Tag |   |
|   |   |   |   |   | [{&quot;name&quot;:&quot;Tag |
|   |   |   | value&quot;:&quot | name&quot;,&quot;value&quot;:&quot;Ta |   |
|   |   |   | ;60&quot;}, {&quot;name&quo | g value&quot;}] |   |
| Labels | String |   | t;:&quot;metricCat egory&quot;,&quot ;value&quot;:&quo t;instanceId&quot; }, {&quot;name&quo t;:&quot;instanceT ype&quot;,&quot;v alue&quot;:&quot; disaster&quot;}, {&quot;name&quo t;:&quot;is alarm& _ quot;,&quot;value& quot;:&quot;true&q uot;}, {&quot;name&quo t;:&quot;productCa tegory&quot;,&quo t;value&quot;:&qu ot;kvstore old&quo _ t;}] |   |   |
| MetricName | String |   | CPUUtilization | The name of the metric that you want to query. |   |

| Namespace | String | acs kvstore _ | The namespace of the service. The namespace is in the format of acs Service _ name. |
|---|---|---|---|
| Periods | String | 60,300 | The statistical period of the metric. Separate multiple periods with commas (,). Example: 15,60,900. |
| Statistics | String | Average,Minimum, Maximum | The statistical method of the metric. Separate multiple statistical methods with commas (,). Example: Average,Minimum,Maximum. |
| Unit | String | % | The unit of the metric. |
| TotalCount | String | 12 | The total number of records. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricMetaList &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses The response content varies with the services that are actually monitored. `XML` format

```json
<DescribeMetricMetaListResponse>
    <TotalCount>120</TotalCount>
    <RequestId>EA94B362-973C-4D6B-BE94-6774E18915C2</RequestId>
    <Success>true</Success>
    <Code>200</Code>
    <Resources>
        <Resource>
            <Description>ECS.CPUUtilization</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>CPUUtilization</MetricName>
            <Labels>[{"name":"alertUnit","value":"%"},
{"name":"alertDefault","value":"80"},{"name":"minAlertPeriod","value":"60"}, {"name":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Lab els>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
```

```json
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The number of read operations performed on the system disk per
second.</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"instanceId"},{ "name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The number of write operations performed on the system disk
per second.</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"instanceId"},{ "name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupCPUUtilization</MetricName>
```

```json
            <Labels>[{"name":"alertUnit","value":"%"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
```

```xml
            <Unit>Count/Second</Unit>
        </Resource>
    </Resources>
</DescribeMetricMetaListResponse>
```

`JSON` format `{`

```json
 "TotalCount":1853,
 "RequestId":"CDE9EAFF-D54E-4024-BBFC-B0AAC883143B",
 "Success":true,
 "Code":200,
 "Resources":{
  "Resource":[
```

`{`

```json
    "Description":"The rated capacity of the disk",
    "MetricName":"ads.diskSize",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"300\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"Mbytes\"}, {\"name\":\"productCategory\",\"value\":\"ads\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"Mbytes"
```

`},` `{`

```json
    "Description":"The used space of the disk",
    "MetricName":"ads.diskUsed",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"300\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"Mbytes"
```

`},` `{`

```json
    "Description":"The disk usage",
    "MetricName":"ads.diskUsedPercent",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"300\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The number of unconsumed messages in the queue",
    "MetricName":"QueueMessageAccumulation",
    "Statistics":"Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of new messages in the queue per minute",
    "MetricName":"QueueMessageInput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"n ame\":\"unitFactor\",\"value\":\"1\"},{ \"name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of unconsumed messages in the queue",
    "MetricName":"QueueMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages generated by the instance per minute",
    "MetricName":"VhostMessageInput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"},
```

```json
{\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages consumed by the instance per minute",
    "MetricName":"VhostMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Latency",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"ms\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"ms"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"SumQPS",
    "Statistics":"Count",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"TrafficRX",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\" \"\" tiCt \"\"
```

`l`

```
\"\"i
```

`t`

```
Id\"}
```

```json
{\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"KBytes"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"TrafficTX",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"KBytes"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code2XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code4XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"tru\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code5XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]", "Dimensions":"userIdregionapiUid"
```

```json
    Dimensions:userId,region,apiUid,
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"pps"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.rate",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1048576\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"pps"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.rate",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1048576\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
```

```
esos:use
```

`d,`

```json
staced,
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.ratePercent",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"Maximum network traffic per unit time",
    "MetricName":"BPS",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"GroupBPS",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"groupId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"GroupInternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"groupId\"},
```

```json
{\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bytes"
```

`},` `{`

```json
    "Description":"The downstream traffic",
    "MetricName":"InternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bytes"
```

`},` `{`

```json
    "Description":"The average number of accesses in the specified time range",
    "MetricName":"QPS",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"UserQPS",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"alertDefault\",\"value\":\"Count\"}, {\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":""
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Usercode4xx",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
```

```json
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Usercode5xx",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"UserhitRate",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The percentage of 4XX HTTP status codes over total status codes in t
he specified time range",
    "MetricName":"code4xx",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"%"
```

`}` `]` `}` `}`

#### 1.3.2 Threshold-triggered alert rules

##### 1.3.2.1 DescribeMetricRuleList

Queries alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricR uleList | The operation that you want to perform. Set the value to DescribeMetricRuleList. |
| Namespace | String | No | acs ecs dashbo _ _ ard | The namespace of the service. Note For more information, see Metrics for Apsara Stack services. |
| MetricName | String | No | cpu total _ | The name of the metric. Note For more information, see Metrics for Apsara Stack services. |
| EnableState | Boolean | No | true | Specifies whether to query enabled or disabled alert rules. Valid values: true: queries enabled alert rules. false: queries disabled alert rules. This parameter is empty by default, which indicates that both enabled and disabled rules are queried. |
| Page | String | No | 1 | The number of pages in which the results are returned. Default value: 1. |
| PageSize | String | No | 10 | The number of entries to return on each page. Default value: 10. |
| AlertState | String | No | ALARM | The status of the alert rule. Valid values: OK: No active alerts are triggered. ALARM: At least one alert is triggered. INSUFFICIENT DATA: No data is _ available. |

| Dimensions | String | No | {&quot;instance Id&quot;:&quot;i - xy123****&quot ;} | The dimension map of the monitored resources. The value is a collection of key- value pairs. A typical key- value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note If you hope to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | key- |   |
|   |   |   |   |   | key- |   |   |
| RuleName | String | No | ECS CPU alert rule | The name of the alert rule. Note This parameter supports fuzzy match. |   |   |   |
| GroupId | String | No | 123456 | The ID of the application group. |   |   |   |
| RuleIds | String | No | a151cd6023eac ee2f0978e0386 3cc1697c89508 12**** | The ID of the alert rule. Note You can specify up to 20 IDs at a time. Separate multiple IDs with commas (,). |   |   |   |

|   | value |   |
|---|---|---|
|   | value |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0E657631-CD6C- 4C24-9637- 98D000B9272C | The ID of the request. |
| Code | Integer | 200 | The HTTP status code. Note A code of 200 indicates that the request succeeds. |

| Total | String | 21 | The total number of returned entries. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the call was successful. |
| Alarms | Array | None | The list of alert rules. |
| Alarm | None | None | Details of the alert rule. |
| AlertState | String | OK | The status of the alert rule. Valid values: OK: No active alerts are triggered. ALARM: At least one alert is triggered. INSUFFICIENT DATA: No data is _ available. |
| ContactGroups | String | Default alert contacts | The contact information about alerts. |
| Dimensions | String | {&quot;userId&quo t;:&quot;4342&quo t;,&quot;instanceId &quot;:&quot;2123 12&quot;} | The dimension map of the monitored resources. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), _ forward slashes (/), and backslashes (\). Note If you hope to see a key- value map expressed by JSON strings, set Dimensions to ordered strings. |
| EffectiveInterv al | String | 00:00-23:59 | The time period during which the alert rule is effective. |
| EnableState | Boolean | true | Indicates whether enabled or disabled alert rules are queried. Valid values: true: Enabled alert rules are queried. false: Disabled alert rules are queried. This parameter is empty by default, which indicates that both enabled and disabled rules are queried. |

|   | key-value |
|---|---|
| key-value |   |

| Escalations | None | None | The conditions that trigger different levels of alerts. |
|---|---|---|---|
| Critical | None | None | The conditions that trigger critical-level alerts. |
| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator of the threshold for critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical method for critical-level alerts. |
| Threshold | String | 90 | The threshold for critical-level alerts. |
| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for critical-level alerts before a critical-level alert is triggered. |
| Info | None | None | The conditions for triggering info-level alerts. |

| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator of the threshold for info-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
|---|---|---|---|
| Statistics | String | Average | The statistical method for info-level alerts. |
| Threshold | String | 90 | The threshold for info-level alerts. |
| Times | String | 1 | The consecutive number of times for which the metric value exceeds the threshold for info-level alerts before an alert is triggered. |
| Warn | None | None | The conditions for triggering warn-level alerts. |

| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator of the threshold for warn-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
|---|---|---|---|
| Statistics | String | Average | The statistical method for warn-level alerts. |
| Threshold | String | 90 | The threshold for warn-level alerts. |
| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for warn-level alerts before a warn-level alert is triggered. |
| GroupId | String | 123456 | The ID of the application group. |
| GroupName | String | My application group | The name of the application group. Note If the alert rule is associated with an application group, the name of the application group is returned in this parameter. |
| MailSubject | String | An alert occurs | The subject of the alert notification email. |
| MetricName | String | cpu total _ | The name of the metric. |
| Namespace | String | acs ecs dashboard _ _ | The namespace of the service. |

| NoEffectiveInt erval | String | 00:00-23:59 | The time period during which the alert rule is ineffective. |
|---|---|---|---|
| Period | String | 60 | The statistical period. |
| Resources | String | [{\&quot;instanceI d\&quot;:\&quot;i- a2d5q7pm3f9yr29 e****\&quot;}, {\&quot;instanceId \&quot;:\&quot;i- a2d5q7pm3f9yr29 e****\&quot;} | The resources that are associated with the alert rule. |
| RuleId | String | a151cd6023eacee 2f0978e03863cc16 97c895012**** | The ID of the alert rule. |
| RuleName | String | My alert rule | The name of the alert rule. |
| SilenceTime | String | 86400 | The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: 86400. Minimum value: 3600. Only one alert is sent during each mute duration, even if the metric value exceeds the alert rule threshold several times. |
| SourceType | String | METRIC | The type of the alert rule. Valid values: METRIC: the alert rule for time series metrics. EVENT: the alert rule for event-type metrics. This type was used in earlier versions and has been discarded. |
| Webhook | String | http://www.aliyun.c om | The callback URL. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleList &amp;<公共请求参数>
```

Sample success responses `XML` format

```xml
<Alarms>
    <Alarm>
```

`/`

```xml
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>Group name</GroupName>
        <Webhook/>
        <Subject>aaabbb</Subject>
        <EffectiveInterval>00:00-23:59</EffectiveInterval>
        <RuleName>My alert rule</RuleName>
        <NoEffectiveInterval/>
        <GroupId>3596360</GroupId>
        <EvaluationCount>3</EvaluationCount>
        <MetricName>cpu_total</MetricName>
        <Threshold>92</Threshold>
        <State>OK</State>
        <Enable>true</Enable>
        <SilenceTime>86400</SilenceTime>
        <Dimensions>[{}]</Dimensions>
        <RuleId>a151cd6023eacee2f0978e03863cc1697c89508e2b61****</RuleId>
        <Namespace>acs_ecs_dashboard</Namespace>
        <ContactGroups>Test</ContactGroups>
        <Escalations>
            <Critical>
                <Statistics>Average</Statistics>
                <Threshold>92</Threshold>
                <Times>3</Times>
                <ComparisonOperator>GreaterThanOrEqualToThreshold</ComparisonOperator>
            </Critical>
            <Info/>
            <Warn/>
        </Escalations>
        <ComparisonOperator>>=</ComparisonOperator>
        <Resources>[{&quot;instanceId&quot;:&quot;i-a2d5q7pm3f12****&quot;}]
</Resources>
    </Alarm>
    <Alarm>
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>demo</GroupName>
        <Webhook/>
        <Subject>${serviceType}-${metricName}-
${levelDescription}Notification{dimensions})</Subject>
        <EffectiveInterval>00:00-23:59</EffectiveInterval>
        <RuleName>xxxxxxxxxxxxxxx</RuleName>
        <NoEffectiveInterval/>
        <GroupId>12345</GroupId>
        <EvaluationCount>3</EvaluationCount>
        <MetricName>cpu_total</MetricName>
        <Threshold>90</Threshold>
        <State>OK</State>
        <Enable>true</Enable>
        <SilenceTime>86400</SilenceTime>
        <Dimensions>[{}]</Dimensions>
        <RuleId>alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****</RuleId>
        <Namespace>acs_ecs_dashboard</Namespace>
        <ContactGroups>rongfei</ContactGroups>
<Escalations>
```

```xml
        <Escalations>
            <Critical>
                <Statistics>Average</Statistics>
                <Threshold>6666</Threshold>
                <Times>3</Times>
                <ComparisonOperator>GreaterThanOrEqualToThreshold</ComparisonOperator>
            </Critical>
            <Info/>
            <Warn/>
        </Escalations>
        <ComparisonOperator>>=</ComparisonOperator>
        <Resources>[{&quot;instanceId&quot;:&quot;host-fTcUci7****&quot;}</Resources>
    </Alarm>
</Alarms> <RequestId>0F05309F-8863-4B2A-8F52-C6AA00E701B4</RequestId> <Success>true</Success><Code>200</Code><Total>102</Total>
```

`JSON` format

```
{ &quot;RequestId&quot;:&quot;0F05309F-8863-4B2A-8F52-C6AA00E701B4&quot;, &quot;Alarms&quot;:{ &quot;Alarm&quot;:[ { &quot;Period&quot;:60, &quot;Statistics&quot;:&quot;Average&quot;, &quot;GroupName&quot;:&quot;Group name&quot ;, &quot;Webhook&quot;:&quot;&quot;, &quot;Subject&quot;:&quot;aaabbb&quot;, &quot;Effe ctiveInterval&quot;:&quot;00:00-23:59&quot;, &quot;RuleName&quot;:&quot;My alert rule&q uot;, &quot;NoEffectiveInterval&quot;:&quot;&quot;, &quot;GroupId&quot;:&quot;3596360&quot;, &quot;EvaluationCount&quot;:3, &quot;MetricName&quot;:&quot;cpu_total&quot;, &quot;State&quot;:&quot;OK&quot;, &quot;T hreshold&quot;:&quot;92&quot;, &quot;Enable&quot;:true, &quot;SilenceTime&quot;:86400, &quot;Dimensions&quot;:&quot;[{}]&quot;, &quot;RuleId&quot;:&quot;a151cd6023eacee2f0978e03863cc1697c89508e2b61****&quot;, &quot; Namespace&quot;:&quot;acs_ecs_dashboard&quot;, &quot;ContactGroups&quot;:&quot;Test&quot;, &quot;ComparisonOperator&quot;:&quot;>=&quot;, &quot;Escalations&quot;:{ &quot;Critical&quot;:{ &quot;Statistics&quot;:&quot;Average&quot;, &quot;Threshold&quot;:&quot;92&quot;, &quot;Times&quot;:3, &quot;ComparisonOperator&quot;:&quot;GreaterThanOrEqualToThreshold&quot; }, &quot;Info&quot;:{}, &quot;Warn&quot;:{} }, &quot;Resources&quot;:&quot; [{\&quot;instanceId\&quot;:\&quot;i-a2d5q7pm3f12****\&quot;}]&quot; }, { &quot;Period&quot;:60, &quot;Statistics&quot;:&quot;Average&quot;, &quot;GroupName&quot;:&quot;demo&quot;, &quot;Webhook&quot;:&quot;&quot;, &quot;Subject&quot;:&quot;${serviceType}-${metricName}- ${levelDescription}Notification(${dimensions})&quot;, &quot;EffectiveInterval&quot;:&quot;00:00-23:59&quot;, &quot;RuleName&quot;:&quot;xxxxxxxxxxxxxxx&quot;, &quot;NoEffectiveInterval&quot;:&quot;&quot;, &quot;GroupId&quot;:&quot;12345&quot;, &q uot;EvaluationCount&quot;:3, &quot;MetricName&quot;:&quot;cpu_total&quot;, &quot;State&quot;:&quot;OK&quot;, &quot;Threshold&quot;:&quot;90&quot;, &quot;Enable&quot;:true, &quot;SilenceTime&quot;:86400, &quot;Dimensions&quot;:&quot;[{ }]&quot;, &quot;RuleId&quot;:&quot;alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****&quot;, &quot;Namespace&quot;:&quot;acs_ecs_dashboard&quot;, &quot;ContactGroups&quot;:&quot;rongfei&quot;, &quot;ComparisonOperator&quot;:&quot;>=&quot;, &quot;Escalations&quot;:{ &quot;Critical&quot;:{ &quot;Statistics&quot;:&quot;Average&quot;, &quot;Threshold&quot;:&quot;6666&quot;, &quot;Times&quot;:3, &quot;ComparisonOperator&quot;:&quot;GreaterThanOrEqualToThreshold&quot; }, &quot;Info&quot;:{}, &quot;Warn&quot;:{} }, &quot;Resources&quot;:&quot; [{\&quot;instanceId\&quot;:\&quot;host-fTcUci7****\&quot;}&quot; } ] }, &quot;Success&quot;:true, &quot;Code&quot;:&quot;200&quot;, &quot;Total&quot;:102 }
```

##### 1.3.2.2 PutResourceMetricRule

Creates an alert rule for a performance metric of a resource. For more information about the sample values of request parameters such as `Namespace` , `MetricName` and `Dimensions` for cloud services, see Metrics for Apsara Stack services.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | PutResourceMet ricRule | The operation that you want to perform. Set the value to PutResourceMetricRule. |
|---|---|---|---|---|
| ContactGroups | String | Yes | Default alert contact group | The alert contact groups. Note Separate multiple groups with commas (,). |
| MetricName | String | Yes | cpu total _ | The name of the metric. Note For more information, see Metrics for Apsara Stack services. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. Note For more information, see Metrics for Apsara Stack services. |
| Resources | String | Yes | [{"instanceId":"x xxxxxx"}] | The resource for which the alert rule is applied. Note For more information, see the Dimensions of the metric in Metrics for Apsara Stack services. |
| RuleId | String | Yes | a151cd6023eac ee2f0978e0386 3cc1697c89508 **** | The ID of the alert rule. Note The ID is generated by the caller. You can specify an existing ID to modify the corresponding alert rule or specify a new ID to create an alert rule. |
| RuleName | String | Yes | My alert rule | The name of the alert rule. |
| Webhook | String | No | http://ww.aliyun. com | The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. |
| EffectiveInterv al | String | No | 00:00-23:59 | The time period during which the alert rule is effective. |

| NoEffectiveInt erval | String | No | 00:00-06:00 | The time period during which the alert rule is ineffective. |
|---|---|---|---|---|
| SilenceTime | Integer | No | 86400 | The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: 86400. Note Only one alert is reported during each mute period even if the metric value consecutively exceeds the alert rule threshold several times. |
| Interval | String | No | 60 | The interval at which the system checks whether the alert rule is triggered. The default value is the lowest frequency at which the metric is checked. Unit: seconds. Note For more information about the frequency at which the metric is checked, see DescribeMetricMetaList. |
| EmailSubject | String | No | An alert occurs | The subject of the alert notification email. |
| Period | String | No | 60 | The aggregation cycle of monitoring data. The value is an integer multiple of 60. Unit: seconds. The default value is the frequency at which monitoring data is collected. |
| Escalations.Cri tical.Statistics | String | No | Average | The statistical methods for Critical- level alerts. |

| Escalations.Cri tical.Comparis onOperator | String | No |   |   | The operator that is used to compare the metric value with the threshold. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in last monitoring cycle LessThanLastPeriod : less than the metric value in last monitoring cycle |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Cri tical.Threshold | String | No |   | 90 | The threshold for Critical-level alerts. |   |   |
| Escalations.Cri tical.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the trigger condition before a Critical- level alert is triggered. |   |   |
| Escalations.Wa rn.Statistics | String | No |   | Average | The statistical methods for Warn- level alerts. |   |   |

| Escalations.Wa rn.Comparison Operator | String | No |   |   | The operator that is used to compare the metric value with the threshold. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in last monitoring cycle LessThanLastPeriod : less than the metric value in last monitoring cycle |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Wa rn.Threshold | String | No |   | 90 | The threshold for Warn-level alerts. |   |   |
| Escalations.Wa rn.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the trigger condition before a Warn-level alert is triggered. |   |   |
| Escalations.Inf o.Statistics | String | No |   | Average | The statistical methods for Info-level alerts. |   |   |

| Escalations.Inf o.Comparison Operator | String | No |   |   | The operator that is used to compare the metric value with the threshold. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in last monitoring cycle LessThanLastPeriod : less than the metric value in last monitoring cycle |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Inf o.Threshold | String | No |   | 90 | The threshold for Info-level alerts. |   |   |
| Escalations.Inf o.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the trigger condition before an Info-level alert is triggered. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request succeeded. |

| Message | String | success | The error message. |
|---|---|---|---|
| RequestId | String | 65D50468-ECEF- 48F1-A6E1- D952E89D9436 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutResourceMetricRule &amp;ContactGroups=Default alert con tact group &amp;MetricName=cpu_total &amp;Namespace=acs_ecs_dashboard &amp;Resources=[{ &quot;instanceId&quot;:&quot;xxxxxxx&quot;}] &amp;RuleId=a151cd6023eacee2f0978e03863cc1697c89508**** &amp;RuleName=My alert rule &am
```

p;<公共请求参数`>` Sample success responses `XML` format

```xml
<Code>200</Code><Message>success</Message> <RequestId>65D50468-ECEF-48F1-A6E1-D952E89D9436</RequestId> <Success>true</Success>
```

`JSON` format

```
{ &quot;Message&quot;:&quot;success&quot;, &quot;RequestId&quot;:&quot;65D50468-ECEF-48 F1-A6E1-D952E89D9436&quot;, &quot;Success&quot;:true, &quot;Code&quot;:&quot;200&quot;
```

`}`

##### 1.3.2.3 DescribeMetricRuleCount

Queries the number of alert rules in each state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | No | DescribeMetricR uleCount | The operation that you want to perform. Set the value to DescribeMetricRuleCount. |
| MetricName | String | No | cpu total _ | The name of the metric . |

| Namespace | String | No | acs ecs dashbo _ _ ard | The namespace of the service. You can call the DescribeMetricMetaList operation to query namespaces. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call is successful. |
| Message | String | The Request is not authorization. | The returned message. |
| MetricRuleCou nt | N/A | N/A | The number of alert rules in each state. |
| Alarm | Integer | 5 | The number of alert rules based on which alerts were triggered and not cleared. |
| Disable | Integer | 0 | The number of disabled alert rules. |
| Nodata | Integer | 0 | The number of alert rules for which status data is unavailable. |
| Ok | Integer | 40 | The number of alert rules that do not have active alerts triggered. |
| Total | Integer | 45 | The total number of alert rules. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMetricRuleCountResponse>
      <Success>true</Success>
      <Code>200</Code>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <MetricRuleCount>
            <Ok>40</Ok>
            <Disable>0</Disable>
            <Total>45</Total>
            <Nodata>0</Nodata>
            <Alarm>5</Alarm>
      </MetricRuleCount>
</DescribeMetricRuleCountResponse>
```

`JSON` format `{`

```json
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":"200",
 "MetricRuleCount":{
  "Ok":40,
  "Disable":0,
  "Nodata":0,
  "Total":45,
  "Alarm":5
```

`}` `}`

##### 1.3.2.4 DeleteMetricRules

You can call this operation to delete one or more alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Id.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c7e12*** * | The ID of the alert rule. |
| Action | String | No | DeleteMetricRul es | The operation that you want to perform. Set the value to DeleteMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
|---|---|---|---|
| Message | String | success | The error message. |
| RequestId | String | E5599964-8D0D- 40DC-8E90- 27A619384B81 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteMetricRules &Id.1=ab05733c97b7ce239fb1b53393dc1697c7e12**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</DeleteMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"E5599964-8D0D-40DC-8E90-27A619384B81",
 "Success":true,
 "Code":"200"
```

`}`

##### 1.3.2.5 EnableMetricRules

Enables one or more alert rules.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RuleId.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c123**** | The ID of the alert rule. |
| Action | String | No | EnableMetricRul es | The operation that you want to perform. Set the value to EnableMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c123**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnableMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</EnableMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":200
```

`}`

**Error codes**

For a list of error codes, visit the API Error Center. For a list of error codes, visit the API Error Center.

##### 1.3.2.6 DisableMetricRules

You can call this operation to disable one or more alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableMetricRul es | The operation that you want to perform. Set the value to DisableMetricRules. |
| RuleId.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c7e012** ** | The ID of the alert rule. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DisableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c7e012**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DisableMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</DisableMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":"200"
```

`}`

##### 1.3.2.7 DescribeAlertingMetricRuleResources

You can call this operation to query the resources that have active alerts triggered based on an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlerting MetricRuleResou rces | The operation that you want to perform. Set the value to DescribeAlertingMetricRuleResources . |
| GroupId | String | No | 123456 | The ID of the application group. |
| Page | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |

| RuleId | String | No | alerRuleId**** | The ID of the alert rule. Note You must specify at least one of the GroupId and RuleId parameters. If you specify both parameters, only entries that meet both conditions are returned. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B868619-77B4- 4623-AD64- 6181EA7CF8FA | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Total | Integer | 1 | The total number of entries returned. |
| Resources | Array | None | The list of resources to which the alert rule applies. |
| Resource | None | None | The information of a resource to which the alert rule applies. |
| Enable | String | true | Indicates whether the alert rule is enabled for the resource. |
| GroupId | String | 123456 | The ID of the application group. Note If the alert rule is associated with an application group, the ID of the application group is returned in this parameter. |
| LastAlertTime | String | 1554718182000 | The last time when an alert was triggered for the resource based on the alert rule. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |

| LastModifyTim e | String | 1554723762000 | The time when the resource was last modified. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
| MetricValues | String | {"timestamp":155 4723720000,"Valu e":631} | The metric value that triggered the alert based on the alert rule. The value is a JSON string. |
| Resource | String | userId=177541323 192****,taskId=3** **,instanceId=i- bp1a0v6yzqrms01 k**** | The resource for which an alert was triggered based on the alert rule. |
| RetryTimes | String | 3 | The consecutive number of times for which the metric value was measured before an alert was triggered. |
| RuleId | String | alerRuleId**** | The ID of the alert rule. |
| RuleName | String | cpuAlert | The name of the alert rule. |
| StartTime | String | 1545901080000 | The time when the resource was associated with the alert rule. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| Threshold | String | 400 | The alert threshold. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeAlertingMetricRuleResources &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Total>1</Total> <Resources>
    <Resource>
        <Enable>true</Enable>
        <Resource>userId=12****,instanceId=i-bp1a012****</Resource>
        <RuleId>alerRuleId****</RuleId>
        <RetryTimes>3</RetryTimes>
        <LastAlertTime>1554718182000</LastAlertTime>
        <MetricValues>{"timestamp":1554723720000,"Value":631}</MetricValues>
        <LastModifyTime>1554723762000</LastModifyTime>
        <StartTime>1545901080000</StartTime>
        <RuleName>cpuAlert</RuleName>
        <Threshold>400</Threshold>
        <GroupId>123456</GroupId>
    </Resource>
</Resources> <Success>true</Success>
```

`JSON` format `{`

```json
 "Success":true,
 "Total":1,
 "Resources":{
  "Resource":[
```

`{`

```json
    "LastAlertTime":1554718182000,
    "Resource":"userId=12****,instanceId=i-bp1a012****",
    "Threshold":"400",
    "Enable":true,
    "LastModifyTime":1554723762000,
    "RuleId":"alerRuleId****",
    "MetricValues":"{\"timestamp\":1554723720000,\"Value\":631}",
    "RetryTimes":3,
    "StartTime":1545901080000,
    "RuleName":"cpuAlert",
    "GroupId":"123456"
```

`}` `]` `}` `}`

##### 1.3.2.8 DeleteMetricRuleResources

Disassociates resources from an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DeleteMetricRul eResources | The operation that you want to perform. Set the value to DeleteMetricRuleResources. |
|---|---|---|---|---|
| Resources | String | Yes | [{"instanceId":"* ****ixxxId1"}] | The associated resources. The value is a JSON array. |
| RuleId | String | No | rr- bp18017n6iolv* *** | The ID of the alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8A35882-90C6- 4F03-BBEB- 153C180398EA | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request succeeded. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRuleResources &amp;Resources= [{&quot;instanceId&quot;:&quot;*****ixxxId1&quot;}] &amp;RuleId=rr-bp18017n6iolv**** &a
```

mp;<公共请求参数`>` Sample success responses `XML` format

```xml
<RequestId>0671A721-0D7A-4F11-BB77-2416325D65AB</RequestId> <Success>true</Success> <Message>success</Message><Code>200</Code>
```

`JSON` format `{`

```json
    "Message":"success",
    "RequestId":"0671A721-0D7A-4F11-BB77-2416325D65AB",
    "Success":true,
    "Code":"200"
```

`}`

##### 1.3.2.9 DescribeAlertHistoryList

Queries historical alerts.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlertHis toryList | The operation that you want to perform. Set the value to DescribeAlertHistoryList. |
| RuleId | String | No | aaaabbb123 | The ID of the alert rule. |
| RuleName | String | No | My Alert Rule | The name of the alert rule. |
| Namespace | String | No | acs ecs dashboa _ _ rd | The namespace of the service. Note For more information, see DescribeMetricMetaList or Metrics. |
| MetricName | String | No | cpu total _ | The name of the metric. Note For more information, see DescribeMetricMetaList or Metrics. |
| GroupId | String | No | 123456 | The ID of the application group. |

| Status | String | No | 2 | Specifies whether to mute alerts. Valid values: 2: Alerts are muted and are not triggered within the silence period, even if the condition specified in the alert rule is met. 0: Alerts can be triggered. |
|---|---|---|---|---|
| State | String | No | ALARM | The alert status. Valid values: ALARM: Alerts are triggered. OK: No alerts are triggered. |
| Ascending | Boolean | No | true | The chronological order in which alerts are sorted. Default value: true. Valid values: true: the reverse chronological order. false: the chronological order. |
| StartTime | String | No | 1554085998000 | The beginning of the time range to query. This value is a UNIX timestamp that represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | String | No | 1554085998000 | The end of the time range to query. This value is a UNIX timestamp that represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| PageSize | Integer | No | 10 | The number of entries per page. |
| Page | Integer | No | 1 | The page number. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 189B35DD-68BA- ******57F0BE12C885 | The request ID. |

| Code | String | 200 | The HTTP status code. The 200 HTTP status code indicates that the request was successful. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request was successful. Default value: true. Valid values: true false |
| Total | String | 2 | The total number of returned entries. |
| AlarmHistoryList | Array |   | The details of historical alerts. |
| -AlertTime | Long | 1554105040000 | The time when the alert was triggered. |
| -ContactALIIMs | List | My TradeManager | The TradeManager accounts that receive alert notifications. |
| -ContactGroups | List | Alert Contact Groups | The alert contact groups. |
| -ContactMails | List | test@example.com | The email addresses that receive alert notifications. |
| -ContactSmses | List | 12345678900 | The mobile numbers to which the alert notifications were sent. |
| -Contacts | List | My Alert Contacts | The alert contacts. |
| -Dimensions | String | {"instanceId":"i- 2zebwilv3xfdg1****"} | The associated resources. |
| -EvaluationCount | Integer | 2 | The consecutive number of times for which the metric value is measured before the alert is triggered. |
| -Expression | String | $Average>=1 | The expression that is used to trigger alerts. |

| -GroupId | String | 123456 | The ID of the application group. |
|---|---|---|---|
| -InstanceName | String | ali-186xxxx123456 | The instance name. |
| -LastTime | Long | 347020693 | The time when the status last changed. |
| -Level | String | P3 | The alert level. Valid values: P2: Alert notifications are sent by using phone calls, text messages, emails, TradeManager, and DingTalk chatbots. P3: Alert notifications are sent by using text messages, emails, TradeManager, and DingTalk chatbots. P4: Alert notifications are sent by using emails and DingTalk chatbots. |
| -MetricName | String | cpu total _ | The name of the metric. Note For more information, see DescribeMetricMetaList or Metrics. |
| -Namespace | String | acs ecs dashboard _ _ | The namespace of the service. Note For more information, see DescribeMetricMetaList or Metrics. |
| -RuleId | String | d97a65a7-70d2-4a8a- 97bf-1a9147**** | The ID of the alert rule. |
| -RuleName | String | My Alert | The name of the alert rule. |

| -State | String | ALARM | The alert status. Valid values: ALARM: Alerts are triggered. OK: No alerts are triggered. |
|---|---|---|---|
| -Status | Integer | 2 | Indicates whether alerts are muted. Valid values: 2: Alerts are muted and are not triggered within the silence period, even if the condition specified in the alert rule is met. 0: Alerts can be triggered. |
| -Value | String | 5.39 | The threshold based on which the alert was triggered for the metric. |
| -Webhooks | String | http://www.****.com/we bhook.html | The callback URL. |
| Message | String | The Request is not authorization. | The message that is returned for the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlertHistoryList &<Common request parameters>
```

Sample success responses XML format

```xml
<DescribeAlertHistoryList>
   <AlarmHistoryList>
      <AlarmHistory>
         <Value>4.41</Value>
         <LastTime>881140083</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_xxxxxx</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
```

```xml
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2******3"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
      <AlarmHistory>
         <Value>2.13</Value>
         <LastTime>760058</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_us****</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2z*****"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
   </AlarmHistoryList>
   <RequestId>FEBE3561-166F-******-020B26F30318</RequestId>
   <Success>true</Success>
   <Code>200</Code>
   <Total>102390</Total>
</DescribeAlertHistoryList>
```

JSON format

```xml
<DescribeAlertHistoryList>
   <AlarmHistoryList>
      <AlarmHistory>
         <Value>4.41</Value>
         <LastTime>881140083</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarmxxxxxx</AlertName>
```

`_`

```xml
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2******3"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
      <AlarmHistory>
         <Value>2.13</Value>
         <LastTime>760058</LastTime>
         <Webhooks></Webhooks>
         <ContactSmses></ContactSmses>
         <RuleName>test-auto-scaling-0001</RuleName>
         <GroupId>123456</GroupId>
         <AlertName>putNewAlarm_us****</AlertName>
         <EvaluationCount>1</EvaluationCount>
         <Status>2</Status>
         <AlertState>ALARM</AlertState>
         <MetricName>cpu_total#60</MetricName>
         <ContactMails></ContactMails>
         <AlertTime>1554986620000</AlertTime>
         <Dimensions>{"instanceId":"i-2z*****"}</Dimensions>
         <RuleId>bfae2ca5b4e07d2c7278772eccda169808c7b****</RuleId>
         <Contacts></Contacts>
         <Namespace>acs_ecs</Namespace>
         <ContactALIIMs></ContactALIIMs>
         <ContactGroups></ContactGroups>
         <Expression>$Average&gt;=1</Expression>
         <Level>P3</Level>
         <InstanceName></InstanceName>
      </AlarmHistory>
   </AlarmHistoryList>
   <RequestId>FEBE3561-166F-******-020B26F30318</RequestId>
   <Success>true</Success>
   <Code>200</Code>
   <Total>102390</Total>
</DescribeAlertHistoryList>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| 403 | InvalidAuthorization | InvalidAuthorization. | You do not have the required permissions. |
|---|---|---|---|
| 403 | InvalidAuthorization | Permission denied. | You do not have the required permissions. |
| 403 | NotAuthSLR | You are not authorized role AliyunServiceRoleFor CloudMonitor. | You do not grant the required permissions to the AliyunServiceRoleForCloudM onitor role. |
| 400 | ParameterInvalid | The parameter is missing or invalid. %s | The parameter is missing or invalid. |
| 404 | ResourceNotFound | The specified resource is not found. | The specified resource does not exist. |
| 429 | ResourceOverLimit | The resource has exceeded the limit. %s | The resource has reached or exceeded the upper limit. |
