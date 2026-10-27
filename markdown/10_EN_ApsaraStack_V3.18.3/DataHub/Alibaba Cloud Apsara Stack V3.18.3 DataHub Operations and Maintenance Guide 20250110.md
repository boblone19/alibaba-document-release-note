---
title: "Alibaba Cloud Apsara Stack V3.18.3 DataHub Operations and Maintenance Guide 20250110"
product_version: "V3.18.3"
doc_version: "20250110"
pdf_pages: 33
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 DataHub Operations and Maintenance Guide 20250110.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%95%B0%E6%8D%AE%E6%80%BB%E7%BA%BF/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20DataHub%20Operations%20and%20Maintenance%20Guide%2020250110.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 DataHub Operations and Maintenance Guide 20250110

## Table of Contents

- 1 Concepts and architecture
  - 1.1 Concepts
  - 1.2 Architecture
    - 1.2.1 Feature oriented architecture
    - 1.2.2 Technical architecture
- 2 Commands and tools
  - 2.1 Common commands for the Apsara system
  - 2.2 Common commands for Apsara Distributed File System
  - 2.3 Common commands for Job Scheduler
  - 2.4 Xstream
  - 2.5 Monitor DataHub performance in the console
- 3 Routine maintenance
  - 3.1 Remove chunk servers from the DataHub cluster
  - 3.2 Add chunk servers to the DataHub cluster
  - 3.3 Restore data after a power outage
  - 3.4 Reimage frontend and chunk servers
  - 3.5 Upgrade or redeploy DataHub
  - 3.6 Shut down problematic chunk servers
  - 3.7 Shut down the DataHub cluster
  - 3.8 Replace a hard drive with a new one on the pangu_cs node
- 4 Exceptions and solutions
- 5 Appendix
  - 5.1 Installation environment
  - 5.2 Deployment directories and services
  - 5.3 Error codes

## 1 Concepts and architecture

### 1.1 Concepts

**Project**

A project is an organizational unit in DataHub, which contains one or more topics. DataHub projects are independent from MaxCompute projects. Projects that you create in MaxCompute cannot be used in DataHub.

**Topic**

Topic is the smallest unit for data subscription and publication. You can use topics to distinguish different types of streaming data. For more information about projects and topics, see Limits in Product Introduction.

**Time-to-live of records**

Time-to-live indicates the period that each record can be retained in the topic. Unit: days. Minimum value: 1. Maximum value: 7.

**Shard**

Shards are channels that allow for writing data into a topic concurrently. Each shard has a unique ID. Shards can be in different status. For more information about the status of shards, see the following table. Each active shard consumes certain server resources. We recommended that you create shards as needed.

> **Note:** Table 1. Status description

| Status | Description |
|---|---|
| Activating | All shards in a topic are being activated when the topic is created. A shard cannot perform read or write operations as it is being activated. |
| Active | Read and write operations are enabled when a shard is in Active status. |
| Deactivating | A shard is being deactivated when it is being split or merged with another shard. A shard cannot perform read or write operations as it is being deactivated. |
| Deactivated | After the split or merge operation is completed, the shard is deactivated. A shard is read only when it is in Deactivated status. |

**Hash key range**

The range of hash key values for a shard, which is in [starting hash key, ending hash key) format. The hashing mechanism ensures that all records with the same partition key are written to the same shard.

**Merge**

The operation that merges two adjacent shards. Two shards are considered adjacent if the union of the hash key ranges for the two shards forms a contiguous set with no gaps.

**Split**

The operation that splits one shard into two adjacent shards.

**Record**

A record is a unit of data that is written into DataHub.

**Record type**

The data type of records in a topic. Tuple and blob are supported. A tuple is a sequence of immutable objects. A blob is a chunk of binary data stored as a single entity.

> **Note:** The following data types are supported in a tuple topic:Table 2. Tuple data types

| Type | Description | Value range |
|---|---|---|
| Bigint | An 8-byte signed integer. Note Do not use the minimum value (- 9223372036854775808) because this is a system reserved value. | -9223372036854775807 to 9223372036854775807 |
| String | A string. Only UTF-8 encoding is supported. | The size of a string must not exceed 1 MB. |
| Boolean | One of two possible values. | Valid values: True and False, true and false, or 0 and 1. |
| Double | An 8-byte double-precision floating point. | -1.0 10308 to 1.0 10308 |
| TimeStamp | A timestamp, | accurate to the millisecond. |

> In a blob topic, a chunk of binary data is stored as a record. Records written into DataHub are Base64 encoded.

**Service roles**

Table 3. Service roles

| Product | Service role | Description |
|---|---|---|
| DataHub | Xstream | Receives read and write requests from the frontend server and forwards the requests to the Apsara Distributed File System. |
|   | Shipper/Connector | Synchronizes data from DataHub to other Alibaba Cloud services including MaxCompute, ApsaraDB RDS for MySQL, and Object Storage Service (OSS). |
|   | Coordinator | Saves checkpoints for subscribed applications in the system. You can resume data consumption from any checkpoint you saved. |
|   | Frontend | Receives all the read and write requests. |

Run the following command on the admin gateway of a cluster to retrieve the services deployed on the cluster:

```
r al
```

Figure 1. Services deployed on the cluster Run the following command on the admin gateway of the cluster to retrieve the service role and servers where the service is running:

```
r wwl $WorkItemName
```

Figure 2. Service role and servers where the service is running

### 1.2 Architecture

#### 1.2.1 Feature oriented architecture

DataHub feature oriented architecture shows the feature oriented architecture of DataHub. Figure 1. DataHub feature oriented architecture The architecture of DataHub is composed of four layers: **client**, **access layer**, **logical layer**, and **storage and scheduling layer**.

**Clients**

DataHub supports the following types of clients: SDKs: DataHub provides a variety of SDKs for C++, Java, Python, Ruby, and Go. Command line tools (CLTs): You can run CLTs in Windows, Linux, or Mac environments. You can manage projects and topics by running corresponding commands. Console: In the console, you can manage projects and topics, create subscriptions, view shard details, monitor topic performance, and manage DataConnector. DataHub agents for data acquisition: Logstash, Fluentd, and Oracle GoldenGate (OGG).

**Access layer**

DataHub can be accessed by using HTTP and HTTPS. DataHub supports RAM authorization and offers horizontal scalability.

**Logical layer**

The logical layer handles the key features of DataHub including project and topic management, data read and write, checkpoint-based data restoration, traffic statistics, and data archive. Based on key features, the logic layer is composed of the following modules: StorageBroker, Metering, Coordinator, and DataConnector. StorageBroker: Enables data read and write of DataHub. Adopts the log file storage model of the Apsara Distributed File System, halving the read/write volume compared with write ahead logs transfer. Stores three copies of data to ensure that no data is lost if a server fault occurs. Supports disaster recovery between data centers. Supports data write caching to ensure efficient consumption of real-time data. Supports independent read caching of historical data to enable concurrent consumption of the same data. Metering: Supports shard-level billing based on the consumption period. Coordinator: Supports checkpoint-based storage. Provides 150,000 QPS per node. Supports horizontal scaling of processing capacity. DataConnector: Supports automatic data synchronization from DataHub to other Alibaba Cloud products including MaxCompute, Object Storage Service (OSS), AnalyticDB, ApsaraDB RDS for MySQL, Table Store, Elasticsearch, and Function Compute.

**Storage and scheduling layer**

Storage: Based on the log file storage model of the Apsara system, DataHub supports append operations and solid state drive (SSD)-based hybrid disk storage. Data in each shard is stored in a separate file based on the record time of the data. Scheduling: Based on the scheduling module of Job Scheduler, DataHub assigns shards to the nodes based on the traffic that occurs on each shard, which does not occupy the CPU or memory of Job Scheduler. DataHub supports failovers within milliseconds and hot upgrades.

#### 1.2.2 Technical architecture

DataHub technical architecture shows the technical architecture of DataHub. Figure 1. DataHub technical architecture The figure shows the process from data ingestion to consumption.
1. Shard, the smallest unit for data management in DataHub, is a first-in, first-out (FIFO)
collection of records.
2. Data in each shard is stored in a set of log files on the Apsara Distributed File System.
3. The master distributes each shard to a broker. Each broker is responsible for the read and
write operations of multiple shards.
4. The frontend server finds a broker based on the project, topic, and shard information
specified in the request and forwards the request to the broker.
5. DataConnector reads data from the broker and forwards the data to other Alibaba Cloud
services.

**Data collector**

You can write data into DataHub from applications developed by using SDKs and data collection tools including Logstash and Fluentd. You can also write data using Data Transmission Service (DTS) and StreamCompute.

**Frontend server**

Frontend servers constitute the access layer and support horizontal scaling. You can call RESTful APIs to access DataHub. RAM authorization is supported.

**Master**

The master handles metadata management and shard scheduling. It supports create, read, update, and delete operations on projects and topics. Master also supports split and merge operations on shards.

**Broker**

Broker handles read and write operations in each shard including data indexing, caching, and file organization and management.

**DataConnector**

DataConnector forwards data in DataHub to other Alibaba Cloud services. DataConnector provides different features for various destination services. These include automatically creating partitions in MaxCompute and converting data streams into files stored in OSS.

## 2 Commands and tools

### 2.1 Common commands for the Apsara system

**Apsara system**

DataHub is built based on the Apsara system. Both DataHub and the Apsara system including Job Scheduler, Apsara Distributed File System, and Apsara Name Service and Distributed Lock Synchronization System are hosted by Apsara Infrastructure Management Framework. Run the following command to view the server roles that are installed on the server:

```
tj_show
```

Run the following command to view all server roles:

```
tj_show –l
```

Run the following command to retrieve a list of servers that the pangu_chunkserver server role is installed on:

```
tj_show -r pangu.PanguChunkserver# //The hostnames of the servers are returned. tj_show -r pangu.PanguChunkserver# -ip //The IP addresses of the servers are returned
```

`.` Run the following command to retrieve a list of servers that the FrontEnd server role is installed on:

```
tj_show –r datahub-frontend.Frontend#
```

Run the following command to retrieve a list of servers that the WebConsole server role is installed on:

```
tj_show –r datahub-webconsole.WebConsole#
```

### 2.2 Common commands for Apsara Distributed File System

**Apsara Distributed File System**

Commands for Apsara Distributed File System start with pu or puadmin. To view the complete description of a command, enter the command followed by **--help** and press enter. Run the following command similar to the Is command used in Linux to retrieve the file content in a specific directory:

```
pu ls
```

Run the following command to upload local files to Apsara Distributed File System:

```
pu put
```

Run the following command to retrieve metadata:

```
pu meta
```

Run the following command to retrieve details about all masters in Apsara Distributed File System:

```
puadmin gems
```

Run the following command to retrieve details about all chunk servers:

```
puadmin lscs
```

Run the following command to view version information:

```
puadmin --buildinfo
```

Before maintaining a chunk server, remove the chunk server from the cluster. Perform the following operations: i. Run the following command to retrieve the current status of a chunk server:

```
pyadmin cs -stat tcp://x.x.x.x:10260
```

ii. Run the following command to remove the chunk server from the cluster by setting its status to shutdown:

```
pyadmin cs -stat tcp://x.x.x.x:10260 --set=shutdown
```

iii. After the maintenance is completed, run the following command to add the chunk server back to the cluster:

```
pyadmin cs -stat tcp://x.x.x.x:10260 --set=normal
```

### 2.3 Common commands for Job Scheduler

**Scheduler**

| The commands for Job Scheduler start with | r | , which is encapsulation of rpc.sh. |
|---|---|---|
| alias r='sh /apsara/deploy/rpc wrapper/rpc.sh' _ |   |   |

Run the following command to retrieve all services and service jobs:

```
r al
```

> **Note:** Typically, service jobs are deployed on the DataHub cluster. The list returned has many entries.

Run the following command to retrieve the status of a service:

```
r wwl $servicename
```

Run the following command to terminate a service:

```
r sstop $servicename
```

Run the following command to start a service:

```
r sstart $servicename
```

Run the following command to retrieve a list of all resources in the cluster:

```
r ttrl
```

Run the following command to retrieve a list of idle resources in the cluster:

```
r tfrl
```

You can run other commands for scheduling purposes as needed.

### 2.4 Xstream

You can run commands on a service terminal by using Xstream for maintenance purposes.

> **Note:** To use the Xstream tool, you must log on as the administrator.

1. Log on to the Apsara Infrastructure Management Framework console. In the top navigation
bar, select **Operations > Cluster Operations**. In the left-side navigation pane, enter datahub in the search bar on the **C** tab page. Figure 1. Search for a cluster
2. Click the cluster that appears in the search result. On the lower part of the left-side
navigation pane, select the **Service** tab and search for **datahub-webconsole**. Figure 2. Double-click the datahub-webconsole service
3. Double-click the **datahub-webconsole** service and double-click **WebConsole#**.
Figure 3. Double-click WebConsole#
4. Hover your mouse pointer over the vertical dots next to the result that appears and select
**Terminal** to open the TerminalService window.
Figure 4. Click Terminal Figure 5. Open the TerminalService window On the TerminalService window, you can use Xstream to run commands for operations and maintenance purposes.
1. Run the following command and find the IP address of the ChildMaster in the first line
returned. Access the server that the ChildMaster is running by using Secure Shell (SSH).

```
r wwl Datahub/XStreamServicex
```

Figure 6. Find the IP address of the ChildMaster
2. Run the following command to enter the specified directory:

```
cd /apsara/tubo/TempRoot/Datahub/XStreamServicex/tool
```

3. Run the following command to configure environment variables:

```
export LD_LIBRARY_PATH=/apsara/lib64/:../lib/
```

4. Run the following command to view resources:

```
./xstream_tool -x x mo
```

Figure 7. View resources If **LoadingPartitions**, **UnloadingPartitions**, and **StartingWorker** are returned with values, run the command again. If these parameters are repeatedly returned with values, an error may occur when the shards are being activated or deactivated.
5. Run the following command to check the status of all brokers:

```
./xstream_tool gws -x x -r broker
```

Figure 8. Check the status of all brokers When 0 is returned for **UnloadedPartition** and **UnconnectedWorker**, the brokers are functioning properly.
6. Run the following command to check the status of all shards in the topic:

```
./xstream_tool -x x lsw -p $project -t $topic -r broker
```

Figure 9. Check the status of all shards in the topic From the command output, you can easily find the problematic shards.

> **Note:** We recommend that you do not run other commands by using Xstream except for those displayed in the examples. If you need to run other commands, contact an operations engineer.

### 2.5 Monitor DataHub performance in the console

**in the console**

In the DataHub console, you can obtain performance statistics. For more information about how to log on to the DataHub console, see Log on to the DataHub console in User Guide. Follow these steps to check the monitoring data:
1. In the Apsara Stack Management Console, navigate to the DataHub console. On the
**Projects** tab page, click **View** in the Actions column of a project.
2. On the project details page, click **View** in the Actions column of a topic.
3. On the topic details page, click the **Metric** tab.
Figure 1. Performance metrics

## 3 Routine maintenance

### 3.1 Remove chunk servers from the DataHub cluster

**the DataHub cluster**

**Prerequisite**

None.

**Procedure**

1. Check the environment.
i. Check the cluster status. Before performing the operation, check that the cluster is in final status and is running properly. a. Log on to the Apsara Infrastructure Management Framework console. On the upper part of the left-side navigation pane, enter tianji in the search bar on the **C** tab page. b. Hover over the vertical dots next to the cluster that appears in the search result. Then select **Dashboard** to go to the **Cluster Dashboard** page. c. In the **Service Instances List**, check whether the Final Status of all instances for tianji is True. Figure 1. Check whether all instances are in final status d. Follow the same steps to navigate to the **Cluster Dashboard** page of the DataHub cluster and confirm that all DataHub instances are in final status. For assistance, contact an operations engineer. Figure 2. Check whether all instances are in final status We recommend that you screenshot the key configuration information before performing the operation. ii. Note down the configurations of the servers to be removed from the cluster for verification purpose. Figure 3. Note down the configurations of the servers to be removed from the cluster

> **Note:** Do not remove any servers that are deployed with both frontend and chunk processes.

2. On the ops server, run the following commands to move one or more chunk servers from
the DataHub cluster to the default cluster:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_dest. nf clt2.conf ./tianji_ops_tool.py contract_nc -c clusterName -l machineList --config tianji_clt2.conf -s SRGname
```

> **Note:** Parameters:
> -c: (Required) The name of the cluster that the servers are removed from.
> -s: (Required) The name of the server role group (SRG) that the servers are removed from.
> --config: (Required) The tianji_clt configuration file.
> -l: (Required) The hostnames of the servers to be removed. Use commas (,) to separate multiple hostnames.

The command output is as follows:

```
machines removed from cluster XXX, newversion: 53111bf22f40e64d5343e0a73a2bce3241b7dac5 -- Indicates that the operation is completed.
```

3. Check whether the servers are removed from the cluster.
i. In the top navigation bar, select **Operations > Cluster Operations**. On the upper part of the left-side navigation pane, select the **C** tab and enter DataHub in the search bar. ii. Hover over the cluster that appears and select **Cluster Operation and Maintenance**
**Center** to enter the **Cluster Operation and Maintenance Center** page.
Figure 4. Enter the Cluster Operation and Maintenance Center page iii. Check whether the servers have been removed from the DataHub cluster. Figure 5. Check whether the servers have been removed from the DataHub cluster

> **Note:** Click the number displayed next to Server s-out in the **Scale-In Scale-Out** box to check the corresponding server details. If the command is executed properly, the number displayed next to Server s-out gradually decreases until it turns 0.

4. Verify that the servers have been removed from the DataHub cluster.
i. Check whether the tianji and DataHub clusters are in final status. a. Log on to the Apsara Infrastructure Management Framework console. On the upper part of the left-side navigation pane, select the **C** tab and enter tianji in the search bar. b. Hover over the cluster that appears and click**Dashboard** to enter the **Cluster**
**Dashboard** page.
c. In **Service Instances List**, check whether the Final Status of all instances for tianji is True. Figure 6. Check whether all instances are in final status d. Follow the same steps to navigate to the **Cluster Dashboard** page of the DataHub cluster and confirm that all DataHub instances are in final status. If you have any problems, contact an operations engineer. Figure 7. Check whether all instances are in final status ii. Navigate to the Cluster Configuration page. Check whether the servers have been removed from the corresponding SRG by comparing the chunk server configurations against those noted down before the operation.

### 3.2 Add chunk servers to the DataHub cluster

**DataHub cluster**

**Prerequisite**

None.

**Procedure**

1. Check the environment.
i. Check the cluster status. Before performing the operation, make sure that the cluster is in final status and is running properly. a. Log on to the Apsara Infrastructure Management Framework console. On the upper part of the left-side navigation pane, enter tianji in the search bar on the **C** tab page. b. Hover over the vertical dots next to the cluster that appears in the search result. Then select **Dashboard** to go to the **Cluster Dashboard** page. c. In the **Service Instances List**, make sure that the Final Status of all instances for tianji is True. Figure 1. Make sure all instances are in final status d. Follow the same steps to navigate to the **Cluster Dashboard** page of the DataHub cluster and confirm that all DataHub instances are in final status. If you have any problems, contact an operations engineer. Figure 2. Make sure that all instances are in final status We recommend that you screenshot the key configuration information before performing the operation. Before adding chunk servers to the cluster, set the clone mode to normal. After the operation is completed, change the clone mode back to block. The path in the Apsara Infrastructure Management Framework console to configure the clone mode is as follows: **Operations > Cluster Operations > Global Clone Switch**. Check whether the DataHub cluster is in Real Clone mode. Figure 3. Check whether the DataHub cluster is in Real Clone mode ii. Check whether the server is added to Apsara Infrastructure Management Framework and used by the default cluster. a. In the top navigation bar, select **Operations > Machine Operations**. On the Machine Operations page, check whether the server is in the default cluster. Figure 4. Check whether the server is in the default cluster b. If the server has not been added to Apsara Infrastructure Management Framework, upload a server configuration file to the framework. The procedure is as follows: a. In the top navigation bar, select **Operations > Machine Operations**. On the
**Machine Operations** page, click **Machine Online/Offline**.
b. In the dialog box that appears, click Download Schema on the **Add Machine** tab page to download the configuration file. Complete the information in the file. The nodename, Sn, and Ip parameters are required. Click **Click to upload** to upload the configuration file. After the file is uploaded, you can find the server in the default cluster. Figure 5. Add a server to Apsara Infrastructure Management Framework
2. On the ops server, run the following command to add a server to the specified cluster. After
the command is executed, a rolling task begins.

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_dest. nf clt2.conf ./tianji_ops_tool.py expand_nc -c Cluster -s SRG -l machine1,machine2 --config clt2. conf
```

> **Note:** Parameters:
> -c: (Required) The name of the cluster to be added with servers.
> -s: (Required) The name of the server role group (SRG) to be added with servers. The SRG must already exist in Apsara Stack Management Framework. You can check whether the SRG exists in the framework in the machine_group.conf file. If the SRG does not exist, deploy the SRG by using the Deployment Planner.
> --config: (Required) The tianji_clt configuration file.
> -l: (Required) The hostnames of the servers to be added. Use commas (,) to separate multiple hostnames.

3. Check the rolling progress in the Apsara Infrastructure Management Framework console.
Figure 6. Check the rolling progress
4. Check the clone progress of the server in the Apsara Infrastructure Management
Framework console.

> **Note:** In the top navigation bar, select **Reports > System Reports**. On the System Reports page, search for State of machine clone report.

Figure 7. Check the clone progress of the server
5. When the rolling task is completed and the Server Status is GOOD, the server is added to
the cluster. Figure 8. Server added to the cluster
6. Verify that the server has been added to the cluster.
i. Log on to the Apsara Infrastructure Management Framework console. Navigate to the
**Cluster Dashboard** page of the DataHub cluster and check whether the cluster is in
final status. Figure 9. Check whether the cluster is in final status ii. Check whether the server has been applied with the specified server role. Figure 10. Check whether the server has been applied with the specified server role.
7. Check the monitoring data of the newly added server.
Log on to the Apsara Infrastructure Management Framework console. Navigate to the Server Details page of the newly added server and check whether there is monitoring data. If no monitoring data is available, restart the following three server roles: AcceleratorAgg#/AcceleratorMaster#/AcceleratorSource#.
8. Verify that the newly added server starts running properly.
Log on to the terminal of the newly added server. Run the ps -ef |egrep "front|broker" command to make sure that the server starts running properly. Figure 11. Verify that the newly added server starts running properly

**Rollback plan**

1. Remove the server that failed to be added to the DataHub cluster.
On the ops1 server, run the following commands to remove a server to the default cluster. If you need to remove multiple servers to the default cluster, run the commands to remove them one by one.

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_dest. nf clt2.conf ./tianji_ops_tool.py contract_nc -c HybridOdpsCluster-A-datahubx -s ComputerServer -l machine1 --config clt2.conf ./tianji_ops_tool.py contract_nc -c HybridOdpsCluster-A-datahubx -s ComputerServer -l machine2 --config clt2.conf
```

> **Note:** Parameters:
> -c: (Required) The name of the cluster that servers are removed from.
> -s: (Required) The name of the SRG that servers are removed from.
> --config: (Required) The tianji_clt configuration file.
> -l: (Required) The hostname of the server that failed to be added to the specified cluster.

2. Check whether the rollback operation takes effect.
i. In the top navigation bar, select **Operations > Cluster Operations**. On the upper part of the left-side navigation pane, hover over the vertical dots next to the target cluster and click **Cluster Operation and Maintenance Center**. Figure 12. Cluster Operation and Maintenance Center ii. On the Cluster Operation and Maintenance Center page, make sure that the server has been removed. Figure 13. Cluster Operation and Maintenance Center
3. Run the following commands to check the server removal task.

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_dest. nf clt2.conf ./tianji_clt machinestatus -c default --config clt2.conf
```

4. Check whether the server information has been deleted from the cluster configuration file.
Navigate to the Cluster Configuration File page of the DataHub cluster and check whether the server information has been deleted from the cluster configuration file. If the server information is still in the machine_group.conf file, delete the information manually. Submit the changes to start a rolling task and wait for the task to complete.

### 3.3 Restore data after a power outage

**outage**

**Prerequisite**

None.

**Procedure**

1. DataHub is based on the distributed storage technology of Apsara Distributed File System.
Therefore, a power outage may cause data loss. After a power outage occurs, run the following command to check in the DataHub console whether data stored in Apsara Distributed File System has been lost.

```
puadmin fs -abnchunk|grep NONE|awk '{print $1}'|awk -F"_" '{print $1}'|while read lin e;do puadmin whois $line;done|grep FileId|awk '{print $4}' |sort|uniq >/home/admin/lostfile -- Ignore directories that start with /deleted/ and send all other directories to an operations engineer to check for lost data.
```

2. Restore data based on file types.
If DataHub files have been lost, inform your users to re-create the corresponding topics. If metadata has been lost, re-install the corresponding package or initialize the docker container.
3. After the data is restored, wait until the tianji cluster is in final status. For assistance,
contact an operations engineer.

### 3.4 Reimage frontend and chunk servers

**servers**

**Prerequisite**

If a system exception occurs and the hardware is functioning properly, reimage the server, server containers, and server roles.

**Procedure**

1. Log on to the Apsara Infrastructure Management Framework console. In the top navigation
bar, select **Operations > Machine Operations**. On the Machine Operations page, search for the physical server by hostname and click **Actions** to open the **Operations Machine** dialog box. Figure 1. Open the Operations Server dialog box
2. Select **Reclone** and click **Confirm**.
Figure 2. Create a clone task
3. Check the clone task progress in the Apsara Infrastructure Management Framework
console.

> **Note:** In the top navigation bar, select **Reports > System Reports**. On the System Reports page, you can find the State of machine clone report. In The Progress of Machine Clone, you can search for the server by machine name.

Figure 3. Check the clone task progress

### 3.5 Upgrade or redeploy DataHub

**Prerequisite**

None.

**Procedure**

1. Check the environment.
i. Log on to the Apsara Infrastructure Management Framework console. On the upper part of the left-side navigation pane, enter tianji in the search bar on the **C** tab page. ii. Hover over the vertical dots next to the cluster that appears in the search result and select **Dashboard** to go to the **Cluster Dashboard** page. iii. In the **Service Instances List**, check that the Final Status of all instances for tianji is True. Figure 1. Check whether all instances are in final status iv. Follow the same steps to navigate to the **Cluster Dashboard** page of the DataHub cluster and confirm that all DataHub instances are in final status. If you have any problems, contact an operations engineer. Figure 2. Check whether all instances are in final status
2. Upgrade or redeploy DataHub.
Redeploy DataHub: If the DataHub service is unavailable due to exceptions on clusters, redeploy DataHub. a. Log on to the Apsara Infrastructure Management Framework console. In the top navigation bar, select **Operations > Cluster Operations**. On the Cluster Operations page, enter datahub in the search bar for **Cluster**. Figure 3. Search for a cluster b. Click the cluster that appears in the search result to enter the Cluster Dashboard page. On the lower part of the navigation pane, click the **Service** tab, enter **datahub-**
**webconsole** in the search bar, and then double-click the service.
Figure 4. Search for the datahub-webconsole service c. Double-click the **datahub-webconsole** service. Then double-click **WebConsole#**. Figure 5. Enter the WebConsole# tab page d. On the WebConsole# tab page, hover over the vertical dots next to the result that appears and select **Terminal** to open the TerminalService window. Figure 6. Select Terminal Figure 7. Open the TerminalService window e. Run the following command as the administrator to restart DataHub on all servers:

```
/home/admin/datahub_service/deploy/control start
```

Upgrade DataHub: You can simultaneously upgrade the DataHub cluster and the output package from Apsara Infrastructure Management Framework console.
3. Verify that DataHub has been upgraded or re-deployed.
i. Log on to the Apsara Infrastructure Management Framework console. To search for the tianji cluster, in the left-side navigation pane, enter tianji in the search bar on the **C** tab page. ii. Hover over the vertical dots next to the tianji cluster and select **Dashboard** to go to the
**Cluster Dashboard** page.
iii. In the **Service Instances List**, check that the Final Status of all instances for tianji is True. Figure 8. Check whether all instances are in final status iv. Follow the same steps to navigate to the **Cluster Dashboard** page of the DataHub cluster and confirm that all instances for DataHub are in final status. If you have any problems, contact an operations engineer. Figure 9. Check whether all instances are in final status

### 3.6 Shut down problematic chunk servers

**servers**

**Prerequisite**

None.

**Procedure**

1. Configure the action and action status for the problematic chunk server.
i. Log on to the ops1 server and set action to rma and action status to pending for the problematic chunk server. In this example, the hostname of the problematic chunk server is m1. Run the following command to configure the action and action status for the problematic chunk server:

```bash
curl "http://127.0.0.1:7070/api/v5/SetMachineAction?hostname=m1" -d '{"action_name":"rma", "action_status":"pending"}'
```

The command output is as follows: `{`

```json
    "err_code": 0,
    "err_msg": "",
    "data": [
```

`{`

```json
            "hostname": "m1"
```

`}` `]` `}` Figure 1. Set action to rma and action status to pending for the problematic chunk server

> **Note:** Replace the IP address and hostname in the sample code with those of your problematic chunk server.

ii. Configure audit logs.

```bash
curl "http://127.0.0.1:7070/api/v5/AddAuditLog?object=/m/m1&category=action" -d '{" category":"action", "from":"tianji.HealingService#", "object":"/m/m1", "content": " {\n \"action\" : \"/action/rma\",\n \"description\" : \"/monitor/rma=error, mti me: 1513488046851649\",\n \"status\" : \"pending\"\n}\n" }'
```

> **Note:** Replace the IP address and hostname in the sample code with those of your problematic chunk server.
> Replace the mtime parameter value in the sample code with the current time.
> Run the following command to retrieve mtime. The sample code is for your reference only. The command is as follows:

```bash
curl "http://127.0.0.1:7070/api/v5/GetMachineInfo? hostname=m1&attr=action_name,action_status,action_description@mtime"
```

> The command output is as follows:
> `{`

```json
    "err_code": 0,
    "err_msg": "",
    "data": {
        "action_description": "",
        "action_description@mtime": 1516168642565661,
        "action_name": "rma",
        "action_name@mtime": 1516777552688111,
        "action_status": "pending",
        "action_status@mtime": 1516777552688111,
        "hostname": "m1",
        "hostname@mtime": 1516120875605211
```

`}`

> `}`
> Figure 2. Retrieve mtime

2. Wait for approval.
i. Check the action status of the server. Run the following command to check the action status of the server:

```bash
curl "http://127.0.0.1:7070/api/v5/GetMachineInfo?hostname=m1"
```

The command output is a long list. We recommend that you search for the server by the key word **"action_status": "pending"**. After confirming that the action status is pending, you can approve the action in the Apsara Infrastructure Management Framework console. a. In the top navigation bar, select **Operations > Cluster Operations**. On the upper part of the left-side navigation pane, enter datahub in the search bar on the **C** tab page. b. Hover over the vertical dots next to the cluster that appears in the search result and select **Cluster Operation and Maintenance Center** to enter the **Cluster**
**Operation and Maintenance Center** page.
c. In the **Server List** of **Cluster Operation and Maintenance Center**, find the chunk server to be shut down, click **Actions**, and then select **Approve Action**. Figure 3. Approve the action d. In the **Approve Action** dialog box, select **approved** for the action and click **OK**. ii. Check the action status of the server role. When the status is approved or done, you can shut down the server for maintenance. Run the following command to check the action status:

```bash
curl http://127.0.0.1:7070/api/v5/GetMachineInfoPackage? hostname=m1&attr=sr.id,sr.action_name,sr.action_status
```

The command output is a long list of items. We recommend that you search for the server by the key word **"action_status": "done"**.
3. After the action of the server changes to rma and action status changes to approved or
done, shut down the server. Restart the server after the maintenance is completed.
4. After the server is restarted, run the following command to configure the action status of
the server:

```json
curl "http://127.0.0.1:7070/api/v5/SetMachineAction?hostname=m1&action_name=rma" -d ' {"action_name":"rma","action_status":"done", "force":true}'
```

5. Log on to the Apsara Infrastructure Management Framework console. Navigate to the
**Cluster Dashboard** page of the DataHub cluster to check whether the cluster is in final
status. Figure 4. Check whether the cluster is in final status

### 3.7 Shut down the DataHub cluster

**cluster**

**Prerequisite**

None.

**Procedure**

1. Terminate DataHub services.
i. On the webconsole server, run the following commands as an administrator and make sure that no data is returned:

```
puadmin fs -abnchunk -t none puadmin fs -abnchunk -t onecopy puadmin fs -abnchunk -t lessmin
```

ii. On the webconsole server, run the following commands as an administrator to terminate all services run by chunk servers in the Apsara system:

```
r ttrl |grep disk |awk '{print $1}' > tubo.list pssh -h tubo.list -i "/apsara/cloud/tool/tianji/apsarad stop"
```

iii. On the webconsole server, run the following command as an administrator to make sure that all services in the Apsara system have been terminated:

```
pssh -h tubo.list -i "/apsara/cloud/tool/tianji/apsarad status"
```

2. Shut down the cluster.
3. Restart DataHub services.
i. On the webconsole server, run the following command as an administrator to restart all services run by chunk servers in the Apsara system:

```
r ttrl |grep disk |awk '{print $1}' > tubo.list pssh -h tubo.list -i "/apsara/cloud/tool/tianji/apsarad start"
```

ii. On the webconsole server, run the following command as an administrator to make sure that all services in the Apsara system are functioning properly:

```
pssh -h tubo.list -i "/apsara/cloud/tool/tianji/apsarad status"
```

### 3.8 Replace a hard drive with a new one on the pangu_cs node

**new one on the pangu_cs node**

**Prerequisite**

Obtain the following information: The hostname or the IP address. The drive letters of the problematic drive. For example, /dev/sdk. The ID of the problematic drive. For example, if the path of the problematic drive in the Apsara Distributed File System is /apsarapangu/disk5, the drive ID is 5. You can also obtain the drive ID by running the following command: puadmin lscs -m

**Procedure**

1. Run the following command to check that the drive to be replaced is in DISK_ERROR status.

```
puadmin lscs -m
```

> **Note:** If the hard drive is not in DISK_ERROR status, run the following command to change the status:

```
puadmin cs -stat tcp://hostname or IP address:10260 -d drive ID --set=ERROR
```

2. Run the following command to unmount the drive. In this example, the drive letters of the
drive to be unmounted are /dev/sdk.

```python
sudo umount /dev/sdk1
```

> **Note:** Ignore this operation if the df command output shows that the drive is not mounted.

3. After the unmount operation is completed, replace the hard drive in hot swap mode.
4. Upload the **sudo repair_app_disk.sh** script to the server and execute the script to format
the drive.
5. Run the following command to set the drive status in the Apsara Distributed File System to
OK:

```
puadmin cs -stat tcp://hostname or IP address:10260 -d drive ID --set=OK
```

6. Restart the server. After the server is started up, it detects a new hard drive.

> **Note:** Kill the processes running on the pangu_cs chunk server and restart the server. Restarting a chunk server does not affect the continuity of your business because DataHub adopts a distributed storage model.

7. Run the following command to check whether the drive status is DISK_OK.

```
puadmin lscs -m
```

You can log on to the server to confirm that the drive has the chunks sub-directory. For example, the chunks exists in the /apsarapangu/disk5/chunks/ directory and new chunks are written into the sub-directory.

## 4 Exceptions and solutions

This section describes some of the common error codes in the current version and corresponding solutions.

**Error Code: LimitEceeded**

Cause: The error code is returned because you can create up to 5 projects and 20 topics in a project in the previous version of DataHub. Solution: In the latest version, you can create up to 10 projects and 1,000 topics in a project. Perform the following operations to change the project or topic limits:
1. Obtain the hostname of the ApsaraDB RDS for MySQL database from the following path:
/home/admin/datahub/service/deploy/env.cfg.
2. Access the corresponding ApsaraDB RDS for MySQL database. In the config_meta table,
check the values of ProjectLimit4User and TopicLimit4Project.
3. Run the following commands to update the configurations. The new configurations take
about 1 minute to take effect. You do not need to restart the database.

```
update config_meta set config_value = 10 where config_type = ‘ProjectLimit4User’; update config_meta set config_value = 1000 where config_type = ‘TopicLimit4Project’;
```

**Error code: IanlnvalidParameter**

Cause: The error code is returned when StreamCompute attempts to capture records from DataHub by using an invalid timestamp. The timestamp you submit to the StreamCompute task is later than the current time, which may be caused by inaccurate local system time. Solution: Correct your local system time by using the Network Time Protocol (NTP) or specify a timestamp that is for example 10 minutes earlier than the local system time.

**Error code: InvalidCursor**

Cause: The error code is returned when StreamCompute attempts to capture records from DataHub by using an invalid or expired cursor. An error may have occurred while StreamCompute is processing records from several days ago. When the time-to-live of the records expires and the records are deleted from DataHub, the cursor of these records is invalid. Solution: Contact technical support for StreamCompute to learn about the cause of the task.

**Error code: Parse response failed**

Cause: This is probably caused by an invalid endpoint. For example, you may enter the console address as endpoint. Solution: Perform a smoke test to check whether the system is running properly. If yes, check whether the endpoint is incorrect in the Apsara Infrastructure Management Framework console. Find the endpoint from the following path in the console: **DataHubCluster >**

**Cluster Dashboard > Cluster Resource > Service: datahub-frontend > dns in the**

**Parameters and Result columns**.

**Error code: InternalServerError**

Cause: Retry the smoke test or StreamCompute task. If the error code is still returned, an internal server error may occur. If the galaxy logs record this type of errors that occurred a long time ago, ignore these errors. Solution: Use the following methods to search for corresponding logs to diagnose the issue. If you have any problems, screenshot the logs and contact technical support. In the logs directory of DataHubServer, search for the log files based on the specific time that the error occurred. The specific time can be found in the RequestId. RequestId is the unique ID of the request generated by DataHubServer. If more than one error occur, find the logs that are marked as **ERROR** in the logs directory of DataHubServer.

## 5 Appendix

### 5.1 Installation environment

Operation system: AliOS5U7-x86-64 Template: Bigdata

### 5.2 Deployment directories and services

**services**

Table 1. Services

| Name | Type | Description |
|---|---|---|
| service-datahub-service | Controller | The service that is used to deploy DataHub backend services and used as the admin gateway of Apsara system. |
| service-datahub-webconsole | Controller | The service that is used to deploy the DataHub console and configured on the same container as service-datahub- service. |
| service-datahub-frontend | Worker | The service that is used to deploy frontend servers and used as chunk servers. |
| Chunkserver | Worker | The service that is used to deploy chunk servers in Apsara Distributed File System. |
| PanguMaster | Controller | The service that is used to deploy three masters in Apsara Distributed File System. |
| NuwaMaster | Controller | The service that is used to deploy three masters of Apsara Name Service and Distributed Lock Synchronization System. |
| FuxiMaster | Controller | The service that is used to deploy two masters of Job Scheduler. |

Table 2. Deployment directories and corresponding services

| Module | Directory | Service |
|---|---|---|
| Datahub/XStreamServicex | /home/admin/datahub service _ | service-datahub-service |
| Datahub/ShipperServicex | /home/admin/datahub service _ | service-datahub-service |
| Datahub/CoordinatorServicex | /home/admin/datahub service _ | service-datahub-service |
| WebConsole | /home/admin/datahub webcon _ sole | service-datahub-webconsole |
| Smoke | /home/admin/datahub smoke _ | service-datahub-frontend |
| Frontend | /home/admin/datahub fronten _ d server _ | service-datahub-frontend |

### 5.3 Error codes

Table 1. Error codes

| Error code | HTTP status code | Description |
|---|---|---|
| InvalidUriSpec | 400 | The error code is returned when the request URI is invalid. This is probably caused by invalid topic or project names. |
| InvalidParameter | 400 | The error code is returned when a parameter is invalid. For more information about the cause of the error, see the error message. |
| Unauthorized | 401 | The error code is returned when the signature is incorrect. This is usually caused by an incorrect AccessKey or a time difference of more than 15 minutes between the client and the server. |
| NoPermission | 403 | The error code is returned when you do not have the permission to perform the operation. |
| InvalidSchema | 400 | The error code is returned when the schema format is invalid. |
| InvalidCursor | 400 | The error code is returned when the cursor is invalid or has expired. |
| NoSuchProject | 404 | The error code is returned when the specified project does not exist. |
| NoSuchTopic | 404 | The error code is returned when the specified topic does not exist. |
| NoSuchShard | 404 | The error code is returned when the specified shard ID does not exist. |
| ProjectAlreadyExist | 400 | The error code is returned when the project name already exists. |
| TopicAlreadyExist | 400 | The error code is returned when the topic name already exists. |
| InvalidShardOperation | 405 | The error code is returned when the operation on the shard is not allowed. For example, you are not allowed to write data into a shard when it is in Deactivated status. |
| LimitExceeded | 400 | The error code is returned when a specified threshold is exceeded. For example, you create no more than 512 shards in a topic and 20 topics in a project. |
| InternalServerError | 500 | The error code is returned when an unknown or internal error occurs or when the system is being upgraded. For more information about the cause of the error, obtain the request ID or search DataHub server logs for InternalServerError. |
