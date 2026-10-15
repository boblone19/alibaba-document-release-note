---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 22
source_pdf: "37f3489d788387fa_Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis Operations and Maintenance Guide 20260828.p"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%8F%AF%E8%A7%82%E6%B5%8B%E9%93%BE%E8%B7%AF%20OpenTelemetry%20%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Tracing%20Analysis%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Tracing Analysis Operations and Maintenance Guide 20260828

## Table of Contents

- 1 O&M overview
- 2 Service architecture
  - 2.1 System architecture
  - 2.2 Deployment architecture
  - 2.3 Server roles
- 3 System inspection
  - 3.1 Log on to the Apsara Uni-manager Operations Console
  - 3.2 Log on to the Apsara Infrastructure Management console
  - 3.3 Inspect Diamond
  - 3.4 Inspect HBase
  - 3.5 Inspect JStorm
  - 3.6 Inspect ESDB
  - 3.7 Inspect Collector
  - 3.8 Inspect the Tracing Analysis console
- 4 Security maintenance
  - 4.1 Account and password maintenance
  - 4.2 Log audit

## 1 O&M overview

This guide helps O&M engineers perform preventive maintenance on Apsara Stack Tracing Analysis to ensure the long-term stable operation of the system. O&M engineers can follow the instructions in this guide to handle the system issues that are identified during maintenance. If O&M engineers encounter system issues that are not covered in this guide, they can contact Apsara Stack technical support.

**Requirements**

O&M engineers must possess IT skills, including the knowledge of computer networks, computer operations, and troubleshooting. In addition, O&M engineers must pass the pre-job training and learn the knowledge for the Apsara Stack system. The required knowledge for the system includes system principles, networking, features, and the usage of maintenance tools. During the maintenance, O&M engineers must comply with operation procedures to ensure personal safety and system security. No part of user data may be copied or disseminated in any form or by any means without prior written consent from users.

**Usage notes**

To ensure a stable system and prevent unexpected events, O&M engineers must comply with the following guidelines: Hierarchical permission management Permissions on networks, devices, systems, and data are granted based on the services and roles of O&M engineers. This prevents system faults that are caused by unauthorized operations. System security Before O&M engineers perform system operations, they must be aware of the impacts of the operations. This prevents the system from being affected by risky operations. O&M engineers must clearly record the details about the issues that are encountered during the operations. This helps O&M engineers troubleshoot the issues. Personal safety and data security O&M engineers must take measures to ensure safety based on device manuals when they use electrical equipment. O&M engineers must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Contact us**

O&M engineers can contact Apsara Stack technical support for help during the maintenance.

## 2 Service architecture

### 2.1 System architecture

This topic describes the system architecture of Tracing Analysis. In Apsara Stack, Tracing Analysis consists of the console and API service. Other services such as core computing and storage are dependent on TLog. For more information, see Deployment architecture.

### 2.2 Deployment architecture

This topic describes the deployment architecture of Tracing Analysis.

| Category | Component | Description |
|---|---|---|

| Tracing Analysis | Tracing Analysis console | The Tracing Analysis console displays a list of applications, provides the query and diagnostics of distributed traces, collects application performance data in real time, dynamically discovers distributed topologies, and supports application- related settings. The API service provides services by using API operations. The console and API service are deployed in the same container. |
|---|---|---|
|   | ARMS- Collector | This component belongs to TLog. After applications integrate the client SDKs of Tracing Analysis to report service call data, the Collector cluster collects the reported service call data. |

| TLog |   |   |
|---|---|---|
|   | JStorm | This component belongs to TLog. The JStorm cluster consists of the TLogst and JStorm components. The JStorm cluster is responsible for log collection, cleansing, computing, and writing to storage. |
|   | HBase | This component belongs to TLog. The HBase cluster is responsible for storing the statistics of Tracing Analysis. |
|   | ESDB | This component belongs to TLog. The ESDB cluster is responsible for storing the detailed data of Tracing Analysis. |
|   | TLog-Console | This component belongs to TLog and is responsible for managing collection points and distributing collection rules. |

### 2.3 Server roles

This topic describes the server roles of Tracing Analysis.

| Project | Cluster | Service | Server role | Description |
|---|---|---|---|---|

| Application Real- Time Monitoring Service (ARMS) | BasicCluster | arms-arms- console | arms-arms- console.ArmsCon soleInit# | This server role is used to initialize databases for the Tracing Analysis console, which is shared between Tracing Analysis and ARMS. |
|---|---|---|---|---|
|   |   |   | arms-arms- console.ArmsCon soleProcess# | This server role is the Tracing Analysis console, which is shared between Tracing Analysis and ARMS. |
|   | XtraceCluster | arms-xtrac | arms- xtrace.ArmsXtrac eInit# | This server role is used to initialize Tracing Analysis resources. |
| TLog | BasicCluster | arms-arms- collector | arms-arms- collector.ArmsCol lectorProcess# | This server role is used to receive the trace data reported by Tracing Analysis. |
|   |   | tlog-tlogEsdb | tlog- tlogEsdb.TlogEsd b# | This server role is the ESDB cluster, which is used to store the detailed data of Tracing Analysis. |
|   |   | tlog-tlogHbase | tlog- tlogHbase.TlogHb ase# | This server role is the HBase cluster, which is used to store the statistics of Tracing Analysis. |
|   |   | tlog-tlogService | tlog- tlogService.Tlogs t# | This server role is the node on which Nimbus runs in the JStorm cluster. |
|   |   |   | tlog- tlogService.Jstor m# | This server role is the node on which Supervisor runs in the JStorm cluster. |
|   |   |   | tlog- tlogService.TlogI nit# | This server role is used to initialize TLog database resources. |
| > Document Version | : 20260828 |   |   |   |

|   |   |   | tlog- tlogService.TlogC onsole# | This server role is the TLog console. |
|---|---|---|---|---|

## 3 System inspection

### 3.1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open a web browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the correct username and password.

**Note**

Obtain the username and password that are used to log in to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account. The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .

### 3.2 Log on to the Apsara Infrastructure Management console

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open a web browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the correct username and password.

**Note**

Obtain the username and password that are used to log in to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account. The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted. To enhance security, make sure that your password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation > Apsara Infrastructure Management > Resources** .

### 3.3 Inspect Diamond

This topic describes how to inspect Diamond.
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**.
3. In the upper part of the **Service Management** page, search for and select `middleWare-`
`jmenv` from the **Service** drop-down list. On the **Service Instances** tab, click **Instance**
**Details** in the **Actions** column to check whether the instances of `middleWare-jmenv` are
in a normal state. If so, the `middleWare-jmenv` service is normal. If not, contact on-site technical support.

### 3.4 Inspect HBase

This topic describes how to inspect HBase.
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**.
3. In the upper part of the **Service Management** page, search for and select `tlog-`
`tlogHbase` from the **Service** drop-down list. On the **Service Instances** tab, click **Instance**
**Details** in the **Actions** column.
4. On the **Component Details** page, click `TlogHbase#` in the **Components** pane.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of an instance. In the left-side
pane of the page that appears, click the machine name to log on to the machine. Run the following command to log on to the container:

```python
sudo docker ps | grep hbase sudo docker exec -it <HBase container ID> bash
```

6. Run the following command to switch to the hadoop user:

```
su hadoop
```

7. Run the following commands to check whether the `tlog-biz` table exists:

```
cd ~/hbase-current/bin list
```

If so, continue with Step 8. If not, contact on-site technical support.
8. Run the following command to check whether `coprocessor` is loaded for the `tlog-biz`
table:

```
describe 'tlog-biz'
```

If so, continue with Step 9. If not, contact on-site technical support.
9. Run the following command to check whether data can be read as expected:

```
scan 'tlog-biz',LIMIT=>10
```

If so, the service is normal. If not, contact on-site technical support.

### 3.5 Inspect JStorm

This topic describes how to inspect JStorm.
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**.
3. In the upper part of the **Service Management** page, search for and select `tlog-`
`tlogService` from the **Service** drop-down list. On the **Service Instances** tab, click
**Instance Details** in the **Actions** column.
4. On the **Component Details** page, click `Tlogst#` in the **Components** pane.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of an instance. In the left-side
pane of the page that appears, click the machine name to log on to the machine. Run the following commands to log on to the container:

```python
sudo docker ps | grep tlogst sudo docker exec -it <tlogst container ID> bash // The tlogst container ID is retu rned in the output of the sudo docker ps | grep tlogst command.
```

6. Run the following command and enter the password of the admin user to switch to the
admin user:

```
su admin
```

7. Run the following command to check whether the `topologies` and related nodes are
running as expected:

```
jstorm list
```

If so, the service is normal. If not, contact on-site technical support.

### 3.6 Inspect ESDB

This topic describes how to inspect ESDB.
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**.
3. In the upper part of the **Service Management** page, search for and select `tlog-`
`tlogEsdb` from the **Service** drop-down list. On the **Service Instances** tab, click **Instance**
**Details** in the **Actions** column.
4. On the **Component Details** page, click `TlogEsdb#` in the **Components** pane.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of an instance. In the left-side
pane of the page that appears, click the machine name to log on to the machine. Run the following commands to log on to the container:

```python
sudo docker ps | grep esdb sudo docker exec -it <esdb container ID> bash // The esdb container ID is return ed in the output of the sudo docker ps | grep esdb command.
```

6. Run the following command and enter the password of the hadoop user to switch to the
hadoop user:

```
su hadoop
```

7. Run the following command to check whether the cluster is in a normal state:

```bash
curl --user arms_admin:arms_admin -POST "IP:9200/_cluster/health?pretty" // Rep lace IP with the actual IP address.
```

If so, continue with Step 9. If not, contact on-site technical support. The preceding figure shows a sample output. The status parameter in the output indicates the status of the ESDB cluster. In the preceding figure, the cluster is in the yellow state. Valid values of the status parameter:
**green**: All primary and replica shards are assigned. The cluster is 100% available.
**yellow**: All primary shards are assigned but one or more replica shards are missing. In
this case, no data is lost and search results remain intact. However, the high availability of the cluster is weakened. If more shards are missing, data is lost. If the cluster is in the yellow state, troubleshoot the issue at the earliest opportunity.
**red**: One or more primary shards and all of their replica shards are missing. In this case,
data is lost and only partial data is returned to search requests. An exception is returned to the write requests sent to the missing shards. You can run the following command to resolve the issue:

```bash
curl --user arms_admin:arms_admin -POST 'ip:9200/_cat/indices?v'
```

**Note**

You can run this command to view the information of all indexes. Find the indexes in the red state. If the cluster has a large number of indexes, you can copy the index information to a file and search for indexes and shards by using the keyword red. If the indexes in red are not required, you can delete the indexes. Then, the cluster enters the green state. You can also run reroute commands to forcibly assign the shards. This operation may be risky. Proceed with caution.
8. Run the following command to check whether the cluster has abnormal indexes:

```bash
curl --user arms_admin:arms_admin -POST 'ip:9200/_cat/indices?v'
```

Determine whether an index is abnormal based on its name. Except for system indexes, each index name uses a valid date as the suffix in the following format: Year-Month-Day or Year-Month. If a large number of index names contain an invalid date, the cluster has abnormal indexes. You can delete the abnormal indexes. Examples of abnormal index names:

```
arms_trace_armsmg_7042-04-13 arms_trace_armsmg_2476-02-17 arms_trace_armsmg_7040-03-06 arms_trace_armsmg_7034-12-25 arms_trace_armsmg_7035-08-19 arms_trace_armsmg_2496-01-08
```

If the cluster does not have abnormal indexes, the service is normal.

### 3.7 Inspect Collector

This topic describes how to inspect Collector.
1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane, choose **O&M Tools > Service Management**.
3. In the upper part of the **Service Management** page, search for and select `arms-arms-`
`collector` from the **Service** drop-down list. On the **Service Instances** tab, click **Instance**
**Details** in the **Actions** column.
4. On the **Component Details** page, click `ArmsCollectorProcess#` in the **Components**
pane.
5. On the **Instances** tab, click **Terminal** in the **Actions** column of an instance. In the left-side
pane of the page that appears, click the machine name to log on to the machine. Run the following command to log on to the container:

```python
sudo docker ps | grep collector sudo docker exec -it <collector container ID> bash
```

6. Run the following command and enter the password of the admin user to switch to the
admin user:

```
su admin
```

7. Run the following command to check whether the service is normal:

```bash
curl -v 127.0.0.1:8080
```

As shown in the preceding figure, if the command output contains `200 OK` and `true` , the service is normal. Otherwise, contact on-site support.

### 3.8 Inspect the Tracing Analysis console

**console**

Log on to the user-side environment. If you can open the Tracing Analysis console, the service is normal. Otherwise, contact on-site support.

## 4 Security maintenance

### 4.1 Account and password maintenance

**maintenance**

The accounts and passwords of Tracing Analysis are the same as those of the Apsara Unimanager Management Console. The accounts and passwords of TLog are the same as those of the Apsara Uni-manager Operations Console.

### 4.2 Log audit

This topic describes the logs of Tracing Analysis. Table 1. Tracing Analysis console

| Log path | Description |
|---|---|
| /home/admin/logs/arms/arms-console.log | The business logs of ARMS- Console. |
| /home/admin/taobao-tomcat-production-7.0.85/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/taobao-tomcat-production-7.0.85/logs/localhost.log | The localhost logs of Tomcat. |

Table 2. Tracing Analysis API service

| Log path | Description |
|---|---|
| /home/admin/logs/arms/arms-pop.log | The business logs of ARMS-Pop. |
| /home/admin/arms-pop/taobao-tomcat-production/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/arms-pop/taobao-tomcat- production/logs/localhost.log | The localhost logs of Tomcat. |

Table 3. ARMS-Collector

| Log path | Description |
|---|---|
| /home/admin/logs/arms/arms-collector.log | The service logs of ARMS- Collector. |
| /home/admin/logs/arms/tracelogs | The business logs reported by Tracing Analysis SDKs. Do not delete these logs. |
| /home/admin/taobao-tomcat-production-7.0.85/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/taobao-tomcat-production-7.0.85/logs/localhost.log | The localhost logs of Tomcat. |

Table 4. TLog-Console

| Log path | Description |
|---|---|

| /home/admin/tlogconsole/logs/tlog-console.log | The business logs of TLog- Console. |
|---|---|
| /home/admin/taobao-tomcat-production-7.0.85/logs/catalina.out | The catalina logs of Tomcat. |
| /home/admin/taobao-tomcat-production-7.0.85/logs/localhost.log | The localhost logs of Tomcat. |

Table 5. JStorm cluster (the TLogst component and Nimbus in the JStorm cluster)

| Log path | Description |
|---|---|
| /home/admin/logs/nimbus.log | The business logs of Nimbus in the JStorm cluster. |
| /home/admin/logs/supervisor.log | The logs of Supervisor in the JStorm cluster. |
| /home/admin/logs/check.log | The status check logs of Nimbus and Supervisor. |
| /home/admin/logs/xxxx-worker-<Port>.log | The logs of workers of collection points. |

Table 6. JStorm cluster (the JStorm component and Supervisor in the JStorm cluster)

| Log path | Description |
|---|---|
| /home/admin/logs/supervisor.log | The logs of Supervisor in the JStorm cluster. |
| /home/admin/logs/check.log | The status check logs of Supervisor. |
| /home/admin/logs/xxxx-worker-<Port>.log | The logs of workers of collection points. |

Table 7. HBase cluster

| Log path | Description |
|---|---|
| /home/hadoop/cluster-data/logs/hbase health.log _ | The health check logs of HBase. |
| /home/hadoop/cluster-data/hbase/logs/hbase-hadoop-master- xxx.log | The Master logs. |
| /home/hadoop/cluster-data/logs/hadoop-xxx-namenode-xxx.log | The NameNode logs. |
| /home/hadoop/cluster-data/hbase/logs/hbase-xxx-regionserver- xxx.log | The Region Server logs. |
| /home/hadoop/cluster-data/hbase/logs/hbase-xxx-zookeeper- xxx.log | The ZooKeeper logs. |

Table 8. ESDB cluster

| Log path | Description |
|---|---|
| /disk1/test cluster.log _ | The runtime logs of ESDB. |
