---
title: "Alibaba Cloud Apsara Stack V3.18.3 DataWorks Operations and Maintenance Guide 20250110"
product_version: "V3.18.3"
doc_version: "20250110"
pdf_pages: 108
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 DataWorks Operations and Maintenance Guide 20250110.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91%E6%B2%BB%E7%90%86%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20DataWorks%20Operations%20and%20Maintenance%20Guide%2020250110.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 DataWorks Operations and Maintenance Guide 20250110

## Table of Contents

- 1 Basic concepts and structure
  - 1.1 What is DataWorks?
  - 1.2 Benefits
  - 1.3 Introduction to data analytics
  - 1.4 DataWorks architecture in Apsara Stack V3
  - 1.5 Service directories
- 2 O&M by using Apsara Big Data Manager
  - 2.1 Log on to the ABM console
  - 2.2 DataWorks O&M overview
  - 2.3 Service O&M
    - 2.3.1 Data Warehouse
      - 2.3.1.1 Service overview
      - 2.3.1.2 Service health
      - 2.3.1.3 DataWorks service roles
      - 2.3.1.4 Service slots
      - 2.3.1.5 DataWorks service nodes
      - 2.3.1.6 Service settings
    - 2.3.2 Data Integration
      - 2.3.2.1 Data integration overview
      - 2.3.2.2 View Data Integration nodes
      - 2.3.2.3 View historical analysis information
    - 2.3.3 Cluster scaling
  - 2.4 Cluster O&M
    - 2.4.1 Cluster overview
    - 2.4.2 Cluster health
  - 2.5 Host O&M
    - 2.5.1 Host overview
    - 2.5.2 Host health
  - 2.6 Deep inspection
    - 2.6.1 Overview
    - 2.6.2 Inspect clusters
    - 2.6.3 Inspect the base_meat project
    - 2.6.4 Inspect the BaseBizAlisa service
    - 2.6.5 Inspect the BaseBizPhoenix service
    - 2.6.6 Inspect the BaseBizCdp service
    - 2.6.7 Appendix: Log on to a database
  - 2.7 Server role O&M
- 3 Common administration tools and commands
  - 3.1 Find the host where a service resides
  - 3.2 View cluster resources
  - 3.3 View service registration variables
  - 3.4 Commands to restart services
  - 3.5 View logs of a failed instance
  - 3.6 Rerun multiple instances at a time
  - 3.7 Stop multiple instances at a time
  - 3.8 Commonly used Linux commands
  - 3.9 View the slot usage of resource groups
- 4 Process daily administration operations
  - 4.1 Daily check
    - 4.1.1 Check the service status and basic server information
    - 4.1.2 Check the status of a gateway server
    - 4.1.3 Monitor service roles and servers
  - 4.2 View logs of the services
  - 4.3 Scale out a cluster that runs the base-biz-gateway service
  - 4.4 Scale in the base-biz-gateway cluster
  - 4.5 Restart the base-biz-tenant service
  - 4.6 Restart the Redis services
  - 4.7 Restart the base-biz-dmc service
  - 4.8 Restart the base-biz-alisa service
  - 4.9 Restart the base-biz-phoenix service
  - 4.10 Restart the base-biz-gateway service
  - 4.11 Restart DataWorks Data Service
  - 4.12 Restart base-biz-gateway
  - 4.13 Configure a resource group in a multi-region environment
  - 4.14 Configure a resource group for Data Integration in a multi-region environment
- 5 Common issues and solutions
  - 5.1 Nodes remain in the Pending (Resources) state
  - 5.2 An out-of-memory (OOM) error occurs when synchronizing data from an Oracle database
  - 5.3 A task does not run at the specified time
  - 5.4 The test service of base is not in the desired status
  - 5.5 The Data Management page does not display the number of tables and the usage of tables
  - 5.6 Logs are not automatically cleaned up
  - 5.7 The real-time analysis service is not in the desired status

## 1 Basic concepts and structure

**structure**

### 1.1 What is DataWorks?

DataWorks is an end-to-end big data platform based on compute engines such as MaxCompute and E-MapReduce. It integrates all processes from data collection to data display and from data analysis to application running. DataWorks provides various features to help you complete the entire research and development (R&D) process in a quick and effective manner. The entire R&D process involves data integration, data development, data governance, data service provisioning, data quality control, and data security assurance. DataWorks is an all-in-one solution for collecting, presenting, and analyzing data, and driving application development. It not only supports offline processing, analysis, and mining of large amounts of data, but also integrates core data-related technologies such as data development, data integration, production and operations and maintenance (O&M), real-time analysis, asset management, data quality control, data security assurance, and data sharing. In addition, it provides the DataService Studio and Machine Learning Platform for Artificial Intelligence (PAI) services. In 2018, Forrester, a globally recognized market research company, named Alibaba Cloud DataWorks and MaxCompute as a world-leading cloud-based data warehouse solution. This solution is by far the only solution from a Chinese company to receive such an acknowledgment. Building on the success of the previous version, DataWorks V2.0 incorporates several new additions, such as workflows and script templates. DataWorks V2.0 supports dual workspaces for development, isolates the development environment from the production environment, adopts standard development processes, and uses a specific mechanism to reduce errors in code.

### 1.2 Benefits

This topic describes the benefits of DataWorks. Powerful computing capabilities DataWorks integrates with compute engines that can process large amounts of data. DataWorks supports join operations for trillions of data records, millions of concurrent jobs, and petabytes (PB) of I/O throughput per day. The offline scheduling system can run millions of concurrent jobs. You can configure rules and alerts to monitor the running statuses of nodes in real time. DataWorks provides efficient and easy-to-use SQL and MapReduce engines, and supports most standard SQL syntax. MaxCompute protects user data from loss, breach, or theft by using multi-layer data storage and access security mechanisms, including triplicate backups, read/write request authentication, application sandboxes, and system sandboxes. End-to-end platform DataWorks provides the graphical user interface (GUI) and allows multiple users to collaborate on a workspace. DataWorks integrates all processes from data integration, processing, management, and monitoring to output. You can create and edit workflows in a visual manner by using the workflow designer. DataWorks provides a collaborative development environment. You can create and assign roles for varying nodes, such as development, online scheduling, maintenance, and data permission management, without locally processing data and nodes. Integration of heterogeneous data stores DataWorks supports batch synchronization of data among heterogeneous data stores at custom intervals in minutes, days, hours, weeks, or months. More than 400 pairs of heterogeneous data stores are supported. Web-based software DataWorks is an out-of-the-box service. You can use it on the Internet or an internal network without the need for installation and deployment. Multitenancy Data is isolated among different tenants. Each tenant controls permissions, processes data, allocates resources, and manages members in a unified and independent manner. Intelligent monitoring and alerting By setting monitoring thresholds, you can control the entire process of all nodes as well as monitor the running status of each node. Easy-to-use SQL editor The SQL editor supports automatic code and metadata completion, code formatting and folding, and pre-compilation. It offers two editor themes. These features ensure a good user experience. Comprehensive data quality monitoring DataWorks allows you to control the quality of data in heterogeneous data stores, offline data, and real-time data. You can check data quality, configure alert notifications, and manage connections. Convenient API development and management The DataService Studio service of DataWorks interacts with API Gateway. This makes it easy for you to develop and publish APIs for data sharing. Secure data sharing DataWorks enables you to de-identify sensitive data before you share it with other tenants, which ensures the security of your big data assets and maximizes their value.

### 1.3 Introduction to data analytics

This topic describes two typical scenarios of data analytics.

**Scenario 1: data synchronization and analysis**

Scenario 1 shows a typical scenario of data analytics.
1. Collect data from various databases to MaxCompute by using DataWorks.
2. Log on to DataWorks, create SQL, MapReduce, and shell nodes, and commit the nodes to
MaxCompute for data analysis.
3. Use DataWorks to synchronize the analysis results from MaxCompute to the databases
from which you collect data. Figure 1. Scenario 1

> **Note:** Base is the name of DataWorks from the technical perspective.

**Scenario 2: data synchronization**

DataWorks supports data synchronization between various databases. You can synchronize data by using DataWorks.

### 1.4 DataWorks architecture in Apsara Stack V3

**Apsara Stack V3**

This topic describes the architecture and services of DataWorks. Figure 1. DataWorks architecture The services shown in the preceding figure play an important role in task issuing and running. You can perform all O&M operations for DataWorks of Apsara Stack V3 in **Apsara**
**Infrastructure Management**. The following figure shows the services in DataWorks.
Figure 2. DataWorks services All services in DataWorks are deployed in Docker containers. You can log on to a host and run the docker ps command to view the containers in which the services are deployed. The following figure shows the architecture of each service except base-biz-gateway. Figure 3. Service architecture

### 1.5 Service directories

This topic describes the directory structure of each service.

**base-biz-gateway service**

The base-biz-gateway service receives and runs nodes from the DataWorks integrated development environment (IDE) and the scheduling system. Logs directory: stores the operational logs of the base-biz-gateway service. taskinfo directory: stores the code run by user nodes and the execution logs. target directory: the main directory of the base-biz-gateway service. This directory stores the service code, start script, stop script, and configuration files.

**base-biz-cdp service**

The base-biz-cdp service is used to synchronize data. Logs directory: stores the operational logs of the base-biz-cdp service. Conf directory: stores the configuration files of the base-biz-cdp service. Bin directory: stores the start script.

**Other services**

The base-biz-alisa service directory is used as an example. Logs directory: stores the operational logs of the base-biz-alisa service. Conf directory: stores the configuration files of the base-biz-alisa service. Bin directory: stores the start script.

## 2 O&M by using Apsara Big Data Manager

**Data Manager**

### 2.1 Log on to the ABM console

This topic describes how to log on to the Apsara Big Data Manager (ABM) console.

**Prerequisites**

**Procedure**

### 2.2 DataWorks O&M overview

This topic describes the DataWorks O&M features supported by Apsara Big Data Manager (ABM) and how to access the DataWorks O&M page.

**DataWorks O&M modules**

ABM provides the service, cluster, and host O&M modules for DataWorks. The following table describes the modules.

**Go to the DataWorks O&M page**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
**Data Warehouse** on the **Services** tab appears.
The **O&M** page consists of the following modules: **Services**, **Clusters**, and **Hosts**.

### 2.3 Service O&M

#### 2.3.1 Data Warehouse

##### 2.3.1.1 Service overview

The DataWorks Overview page displays the key operation metrics, including service overview, service status, instance scheduling information, and slot usage. On this page, you can also view the trend chart of the total number of finished tasks.

**Go to the Overview page under Services**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
the **Data Warehouse** page appears.

**Services**

This section displays the numbers of available services, unavailable services, and services that are being respectively upgraded.

**Roles**

This section displays all DataWorks service roles and their statuses. You can also view the expected and actual numbers of hosts in the desired state for each service role.

**Instance Scheduling**

This section displays the number of successful instances, number of instances not running, waiting duration, number of running instances, number of failed instances, and number of instances waiting for resources.

**Usage for Slot Resources**

This section displays the total number of slots, the number of used slots, the number of unavailable slots, and the number of idle slots for DataWorks.

> **Note:** Slots are resources that can be used by DataWorks for instance scheduling.

**Total Number of Finished Tasks**

This section displays the trend chart of the total number of finished nodes. The trend chart displays the trend lines of the number of nodes finished yesterday, the number of nodes finished today, and the average number of nodes finished each day over time in different colors.

##### 2.3.1.2 Service health

On the Health Status page for DataWorks, you can view all checkers of a cluster, including the checker details, check results for the hosts in the cluster, and schemes to clear alerts (if any). In addition, you can log on to a host and perform manual checks on the host.

**Entry**

1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** page under
the **Data Warehouse** page appears.
4. Select a cluster from the drop-down list, and then click the **Health Status** tab. The **Health**
**Status** page appears.
The **Health Status** page displays all checkers of the cluster and the check results for the hosts in the cluster. The check results are divided into **Critical**, **Warning**, and **Exception**. They are displayed in different colors. Pay attention to the check results, especially the
**Critical** and **Warning** results, and handle them in a timely manner.

**Supported operations**

On the **Health Status** page, you can view checker details, hosts with alerts, and alert causes. You can also log on to hosts with alerts, clear alerts, and run checkers again. For more information, see Cluster health.

##### 2.3.1.3 DataWorks service roles

The Service Roles tab displays information about DataWorks service roles, such as the role name, status, and expected and actual numbers of hosts in the desired state.

**Go to the Service Roles tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
**Data Warehouse** on the **Services** tab appears.
4. Select a cluster from the drop-down list and click the **Service Roles** tab.
The **Service Roles** tab displays information about all service roles, including the role status and expected and actual numbers of hosts in the desired state. The service role status can be **good**, **bad**, or **upgrading**.

**Supported operations on the Service Roles tab**

On the **Service Roles** tab, you can filter or sort service roles by column to facilitate information retrieval.

##### 2.3.1.4 Service slots

Slots are resources used to process tasks. Apsara Big Data Manager (ABM) allows you to view the slot information of DataWorks clusters, resource groups, and hosts. The information includes the maximum number of slots, the number of used slots, and slot usage. You can also migrate resource groups, modify the number of slots for resource groups or hosts, and modify the host status.

**Terms**

A data migration unit (DMU) represents the minimum operating capability required by a Data Integration task. This capability indicates the data synchronization processing capability in the case of limited CPU, memory, and network resources. Resources measured by DMU are allocated by slot. Each DMU occupies two slots.

**Entry**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** page
appears.
4. Select a cluster from the drop-down list and click the **Slot** tab.

**Cluster slots**

Click the **Cluster** tab on the **Slot** tab. The **Cluster** tab displays the slot overview of all DataWorks clusters, including the total number of slots, the numbers of used slots and available slots, and slot usage. It also displays the cluster running status. To view more information about the slots of a specified cluster, click the name of the cluster in the **Cluster Name** column. In the upper part of the page that appears, you can view the numbers of gateways, resource groups, slots, used slots, frozen slots, and available slots, and the slot usage of the cluster. You can also view the trend chart of slot usage over time in the lower part of the page. The trend chart displays trend lines for the number of used slots, the maximum number of slots, and the number of available slots in different colors. You can click the name of a metric under the chart to determine whether to display the related trend line in the chart. A highlighted metric name indicates that the related trend line is displayed, whereas a dimmed metric name indicates that the related trend line is not displayed.

**Resource group slots**

Click the **Group** tab on the **Slot** tab. The **Group** tab displays the slot overview of all DataWorks resource groups, including the maximum number of slots, the numbers of used slots and available slots, and slot usage. The tab also displays the name, cluster, project, and running status of each resource group. To view more information about slots of a specified resource group, click the ID of the resource group in the **Resource Group ID** column. In the upper part of the page that appears, you can view the current slot information of the resource group, such as the number of used slots and the maximum number of slots. You can also view the trend chart of slot usage over time, the nodes that occupy the slots, and the owners in the lower part. The trend chart displays trend lines for the number of used slots, the maximum number of slots, and the number of available slots in different colors. You can click the name of a metric under the chart to determine whether to display the related trend line in the chart. A highlighted metric name indicates that the related trend line is displayed, whereas a dimmed metric name indicates that the related trend line is not displayed.

**Change the number of slots for a resource group**

If the number of slots for a resource group is insufficient or excessive, you can change the number of slots to add or remove resources for the resource group.
1. On the **Group** tab, find the resource group for which you want to change the number of
slots, and click **Change Maximum Slots** in the Actions column.
2. In the dialog box that appears, change the value of **Maximum Slots**.
3. Click **Run**. A message appears, indicating that the action is submitted.

**Migrate a resource group**

If the slots in a cluster that is associated with a resource group are insufficient and slots cannot be added for the cluster, you can associate the resource group with another cluster.
1. On the **Group** tab, find the resource group that you want to manage. Then, move the
pointer over Change Maximum Slots in the Actions column and click **Bind Resource**
**Group**.
2. In the dialog box that appears, change the value of **Target Cluster**.
3. Click **Run**. A message appears, indicating that the action is submitted.

**Host slots**

Click the **Hostname** tab on the **Slot** tab. The **Hostname** tab displays the slot overview of all DataWorks hosts, including the maximum number of slots, the number of used slots, and the slot usage. The tab also displays the IP address, cluster, running status, activeness, and monitoring status of each host. To view more information about the slots of a specified host, click the name of the host in the
**Hostname** column.
In the upper part of the host details page, you can view the current slot information of the host, such as the number of used slots and the maximum number of slots. You can also view the trend chart of slot usage over time in the lower part of the page. The trend chart displays trend lines for the number of used slots, the maximum number of slots, and the number of available slots in different colors. You can click the name of a metric under the chart to determine whether to display the related trend line in the chart. A highlighted metric name indicates that the related trend line is displayed, whereas a dimmed metric name indicates that the related trend line is not displayed.

**Modify the host status**

A host can be in the normal, unavailable, or suspended state. You can modify the host status based on your business requirements.
1. On the **Hostname** tab, find the host whose status you want to modify and click **Change**
**Status** in the Actions column.
2. In the dialog box that appears, set **Status**.
3. Click **Run**. A message appears, indicating that the action is submitted.

**Change the number of slots for a host**

If the number of slots for a host is insufficient or excessive, you can change the number of slots to add or remove resources for the host.
1. On the **Hostname** tab, find the host that you want to manage and click **Change**
**Maximum Slots** in the Actions column.
2. In the dialog box that appears, change the value of **Maximum Slots**.
3. Click **Run**. A message appears, indicating that the action is submitted.

##### 2.3.1.5 DataWorks service nodes

The Nodes tab displays the nodes that are created by users in DataWorks. You can filter or sort nodes to facilitate information retrieval.

**Go to the Nodes tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
**Data Warehouse** on the **Services** tab appears.
4. Select a cluster from the drop-down list and click **Nodes**. The **Nodes** tab appears.
The **Nodes** tab displays the node information of the current cluster, including the workspace name, node name, node ID, data timestamp, owner, status, start time, end time, duration, priority, type, and instance ID.

**Filter nodes by status**

In the upper part of the **Nodes** tab, the numbers of nodes in all states are displayed. You can click a state to view the corresponding nodes. By default, nodes in the **Running** state are displayed.

**Filter nodes by time**

You can select a time period, including the date and time, in the upper-left corner of the node list to view the nodes in the corresponding time period.

**Supported operations on the Nodes tab**

You can filter nodes, sort nodes by column, and customize columns on the Nodes tab.

##### 2.3.1.6 Service settings

The Settings page allows you to change the values of configuration items for various service roles in DataWorks.
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** page under
the **Data Warehouse** page appears.
4. Select a cluster from the drop-down list, and then click the **Settings** tab. The **Settings**
page appears.

#### 2.3.2 Data Integration

##### 2.3.2.1 Data integration overview

The Overview page of Data Integration displays information in the Task Scheduling Overview, Today's Tasks, Third-party Dependencies - Response Time (milliseconds), Third-party Dependencies - Total Requests, and Third-party Dependencies - Request Error Rate sections.

**Procedure**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
the **Data Warehouse** page appears.
4. In the left-side navigation pane, click **Data Integration**. The **Overview** page appears.
After you set the **Aggregation Period** parameter and select a time period, you can view the desired information in the following sections:

**Task Scheduling Overview**

**Today's Tasks**

**Third-party Dependencies - Response Time (milliseconds)**

**Third-party Dependencies - Total Requests**

**Third-party Dependencies - Request Error Rate**

**Third-party Dependencies - Failed Requests**

##### 2.3.2.2 View Data Integration nodes

This topic describes how to view node information on the Tasks page of Data Integration, and obtain the required data such as the amount of synchronized data, synchronization speed, and node data volume.

**Go to the Tasks page**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
the **Data Warehouse** page appears.
4. In the left-side navigation pane, click **Data Integration**. The **Overview** page appears.
5. Click the **Tasks** tab. The **Instances** tab appears by default.

**View instance information**

On the **Instances** tab, you can filter instances by **Project Name**, **Resource Group**, **Host**,
**Status**, **Read Plug-in Type**, **Write Plug-in Type**, and **Data Source**. If you need to
customize more filter criteria, click **Advanced Search**. You can also click the request ID, synchronization script number, or resource group name to view the corresponding details. After you click the request ID, you can view the event type, IP address from which the request is submitted, and start time of the instance. After you click the synchronization script number, you can view the following information: On the **Job Statistics by Day** page, you can view the trends of the synchronized data volume, synchronization speed, and consumed time. On the **Job Statistics by Run** page, you can view the trends of the synchronized data volume, synchronization speed, and consumed time. On the **Jobs in the Final Status** page, you can view the trends of successful nodes, failed nodes, and killed nodes. After you click the resource group name, you can view the slot usage of the resource group. After you view the corresponding details, you can click **Back** to return to the **Instances** page under **Task**. On the Task page, you can also view the number of initialized nodes, submitted nodes, running nodes, failed, nodes, successful nodes, and nodes waiting to be scheduled.

**View multi-dimensional analysis information**

On the **Multi-dimensional Analysis** tab, you can filter historical analysis information by
**Project Name**, **Resource Group**, **Host**, **Status**, **Read Plug-in Type**, **Write Plug-in Type**,
or **Data Source** from the perspective of **Sync Data Size**, **Sync Speed**, or **Tasks**.

##### 2.3.2.3 View historical analysis information

On the Historical Analysis page, you can view information about multi-dimensional analysis, execution time analysis, and nodes rankings.

**Go to the Historical Analysis page**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab under
the **Data Warehouse** page appears.
4. In the left-side navigation pane, click **Data Integration**. The **Overview** page appears.
5. Click the **Historical Analysis** tab. The **Multi-dimensional Analysis** page appears.

**View multi-dimensional analysis information**

On the **Multi-dimensional Analysis** tab, you can filter historical analysis information by
**Project Name**, **Resource Group**, **Host**, **Status**, **Read Plug-in Type**, **Write Plug-in Type**,
or **Data Source** from the perspective of **Sync Data Size**, **Sync Speed**, **Time**, or **Tasks**.

**View execution time analysis information**

On the **Execution Time Analysis** tab, you can filter required execution time information by
**Project Name**, **Resource Group**, **Host**, **Status**, **Read Plug-in Type**, **Write Plug-in Type**,
or **Data Source**.

**View top 10 nodes**

On the **Task Rankings** tab, you can filter top 10 nodes by **Project Name**, **Resource Group**,
**Host**, **Status**, **Read Plug-in Type**, **Write Plug-in Type**, or **Data Source**.

#### 2.3.3 Cluster scaling

Apsara Big Data Manager (ABM) supports DataWorks cluster scaling. To scale out a DataWorks cluster, add physical hosts in the default cluster of Apsara Infrastructure Management to the DataWorks cluster. To scale in a DataWorks cluster, remove physical hosts from the DataWorks cluster to the default cluster of Apsara Infrastructure Management.

**Background information**

In Apsara Stack, scaling out a cluster involves complex operations. You must configure new physical hosts on Deployment Planner so that they can be added to the default cluster of Apsara Infrastructure Management. The default cluster of Apsara Infrastructure Management is considered as a resource pool that can provide resources for scaling out business clusters. To scale out a cluster, add physical hosts in the default cluster of Apsara Infrastructure Management to the cluster. To scale in a cluster, remove physical hosts from the cluster to the default cluster of Apsara Infrastructure Management. When you scale out a DataWorks cluster, ABM adds physical hosts in the default cluster to the DataWorks cluster. When you scale in a DataWorks cluster, ABM removes physical hosts from the DataWorks cluster to the default cluster. The server roles of physical hosts in DataWorks include **BaseBizCdpGatewayWithNc#** and **BaseBizGatewayWithNc#**. DataWorks cluster scaling supports only the two server roles.

**Prerequisites**

Scale-out The physical hosts that you want to add to your DataWorks cluster are in the default cluster of Apsara Infrastructure Management. The server role of the template host is **BaseBizCdpGatewayWithNc#** or
**BaseBizGatewayWithNc#**.
Scale-in The server role of the template host is **BaseBizCdpGatewayWithNc#** or
**BaseBizGatewayWithNc#**.

> **Note:** You can go to the **DataWorks** page. Then, click **O&M** in the upper-right corner, and click the **Services** tab. In the left-side navigation pane, click **Data** **Warehouse**. On the page that appears, click the **Instances** tab. In the server role list, find the server role **BaseBizCdpGatewayWithNc#** or **BaseBizGatewayWithNc#**, and click the server role name to go to the Apsara Infrastructure Management console and view the hosts with the server role **BaseBizCdpGatewayWithNc#** or **BaseBizGatewayWithNc#**.

**Scale out a DataWorks cluster**

You can add multiple hosts to a DataWorks cluster at a time to scale out the cluster. To achieve this, you must specify an existing host as the template host. During the scale-out, the configurations of the template host are copied to the hosts so that the hosts can be added to the cluster at a time.
1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** tab appears.
4. Select a cluster from the drop-down list and click the **Slot** tab.
5. On the **Slot** tab, click the **Hostname** tab. Then, select a physical host whose server role is
**BaseBizCdpGatewayWithNc#** or **BaseBizGatewayWithNc#** in the host list as the
template host.
6. Move the pointer over **Actions** in the upper-right corner and click **Scale-up for Normal**
**Hosts**. In the **Scale-up for Normal Hosts** panel, configure the parameters
Parameters:
**Refer Hostname**: the name of the template host. By default, the name of the selected
host is used.
**Hostname**: the name of the host that you want to add to the DataWorks cluster. Enter
the name of an available host in the default cluster for scale-out. If you want to add multiple hosts, enter multiple hostnames and separate the hostnames with commas (,).
7. Click **Run**. A message appears, indicating that the action is submitted.
8. View the scale-out status.
Move the pointer over **Actions** in the upper-right corner and click **Execution History** next to **Scale-up for Normal Hosts** to view the scale-out history. The scale-out may require a long period. In the Current Status column, **RUNNING** indicates that the execution is in progress, **SUCCESS** indicates that the execution is successful, and
**FAILED** indicates that the execution fails.
If **RUNNING** is displayed in the Current Status column, you can click **Details** in the Details column to view the steps and progress of the scale-out. If **FAILED** is displayed in the Current Status column, click **Details** in the Details column to locate the failure cause. For more information, see Locate the cause of a scaling failure.

**Scale in a DataWorks cluster**

You can remove physical hosts from a DataWorks cluster to the default cluster of Apsara Infrastructure Management to scale in the DataWorks cluster.
1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** page
appears.
4. Select a cluster from the drop-down list and click the **Slot** tab.
5. On the **Slot** tab, click the **Hostname** tab. Then, select a physical host whose server role is
**BaseBizCdpGatewayWithNc#** or **BaseBizGatewayWithNc#** in the host list as the
template host.
6. Move the pointer over **Actions** in the upper-right corner and click **Scale-down for Normal**
**Hosts**. In the **Scale-up for Normal Hosts** panel, configure the parameters.
Parameters:
**Hostname**: the name of the host that you want to remove from the DataWorks cluster.
By default, the name of the selected host is used.
**Biz Name**: the server role of the host that you want to remove from the DataWorks
cluster. Select the actual server role from the drop-down list. Valid values: **base-biz-**
**cdpgatewaywithnc#** and **base-biz-gatewaywithnc#**.
7. Click **Run**. A message appears, indicating that the action is submitted.
8. View the scale-in status.
Move the pointer over **Actions** in the upper-left corner and click **Execution History** next to **Scale-down for Normal Hosts** to view the scale-in history. The scale-in may require a long period. In the Current Status column, **RUNNING** indicates that the execution is in progress, **SUCCESS** indicates that the execution is successful, and
**FAILED** indicates that the execution fails.
If **RUNNING** is displayed in the Current Status column, you can click **Details** in the Details column to view the steps and progress of the scale-in. If **FAILED** is displayed in the Current Status column, click **Details** in the Details column to locate the failure cause. For more information, see Locate the cause of a scaling failure.

**Locate the cause of a scaling failure**

The method for locating the cause of a scale-out failure and that of a scale-in failure are similar. This section describes how to locate the cause of a scale-out failure.
1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner. The **Overview** page
appears.
4. Move the pointer over **Actions** in the upper-right corner and click **Execution History** next
to **Scale-up for Normal Hosts** to view the scale-out history.
5. In the panel that appears, click **Details** in the Details column of a failed execution to locate
the failure cause. You can locate the failure cause based on the following information: parameter settings, host details, scripts, and execution parameters.

### 2.4 Cluster O&M

#### 2.4.1 Cluster overview

The cluster overview page displays the overall running and health check information about a cluster. On this page, you can view the health check result and health check history of the cluster. You can also view the trend charts of CPU usage, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for the cluster.

**Entry**

1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner.
4. Click the **Clusters** tab at the top of the **O&M** page.
5. On the **Clusters** page, select a cluster in the left-side navigation pane, and then click the
**Overview** tab. The **Overview** page appears.

**Health Check**

This section displays the number of checkers deployed for the cluster and the respective number of Critical, Warning, and Exception alerts. Click **View Details** to go to the Health Status page. On this page, you can view the health check details. For more information, see Cluster health.

**Health Check History**

This section displays a record of the health checks performed on the cluster. Click **View Details** to go to the Health Status page. On this page, you can view the health check details. For more information, see Cluster health. You can click the event content of a check to view the exception items.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the cluster in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the cluster in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the cluster in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the cluster over time in different colors. These trend lines reflect the data transmission status of the cluster. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the cluster in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster in the specified period.

#### 2.4.2 Cluster health

On the Health Status page, you can view all checkers of a cluster, including the checker details, check results for the hosts in the cluster, and schemes to clear alerts (if any). In addition, you can log on to a host and perform manual checks on the host.

**Go to the Health Status page under Clusters**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner.
4. Click the **Clusters** tab at the top of the **O&M** page.
5. On the **Clusters** page, select a cluster in the left-side navigation pane, and click the
**Health Status** tab. The **Health Status** page appears.
On the **Health Status** tab, you can view all check items for the cluster and the check results for the hosts in the cluster. The following alerts may be reported on a host: **Critical**,
**Warning**, and **Exception**. The alerts are represented in different colors. You must handle
the alerts at the earliest opportunity, especially the **Critical** and **Warning** alerts. The following table describes the check results.

**View the details of a check item**

1. On the Health Status tab, find the check item whose details you want to view and click
**Details** in the Actions column. In the Details message, view the details of the check item.
The following information about the check item is displayed: **Name**, **Source**, **Alias**,
**Application**, **Type**, **Scheduling**, **Data Collection**, **Default Execution Interval**, and
**Description**. The schemes to clear alerts are provided in the description.
2. Click **Show More** to view more information about the check item.
You can view more information in the **Script**, **Target (TianJi)**, **Default Threshold**, and
**Mount Point** sections.

**View the hosts for which alerts are reported and causes for the**

**alerts**

You can view the check history and check results of a check item on a host.
1. On the Health Status tab, click the **+** icon on the left of a check item to show all alerts that
are triggered by the check item. You can view all hosts on which the check item is run.
2. Click a hostname. In the panel that appears, find the alert that you want to manage and
click **Details** in the Actions column to view the cause of the alert.

**Log on to a host**

You may need to log on to a host to handle alerts or other issues that occur on the host.
1. On the Health Status tab, click the **+** icon on the left of a check item to show all alerts that
are triggered by the check item. You can view all hosts on which the check item is run.
2. Click the **Login in** icon next to a hostname. The **TerminalService** page appears.
3. On the **TerminalService** page, click the hostname in the left-side navigation pane to log
on to the host.

**Run a check item again**

After you handle an alert for a host, click **Refresh** in the Actions column of the host to run the check item again for the host. This way, you can check whether the alert is cleared.

### 2.5 Host O&M

#### 2.5.1 Host overview

The host overview page displays the overall running information about a host in a DataWorks cluster. On this page, you can view the root disk usage, total usage, 1-minute load, 5-minute load, 15-minute load, health check result, and health check history of the host. You can also view the trend charts of CPU usage, disk usage, memory usage, load, packet transmission usage for the host.

**Entry**

1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner.
4. Click the **Hosts** tab at the top of the **O&M** page.
5. On the **Hosts** page, select a host in the left-side navigation pane, and then click the
**Overview** tab. The **Overview** page appears.

**Root Disk Usage, Total, and 1-Minute Load**

These sections display the root disk usage, total usage, and 1-minute load for the selected host. The Root Disk Usage section provides the usage of the /tmp directory. The Total section provides the system usage and user usage. The 1-Minute Load section provides the 1-minute, 5-minute, and 15-minute load averages.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the host in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the host in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the host in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the host over time in different colors. These trend lines reflect the data transmission status of the host. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the host in the specified period.

**Health Check**

This section displays the number of checkers deployed for the host and the respective number of Critical, Warning, and Exception alerts. Click **View Details** to go to the Health Status page. On this page, you can view the health check details. For more information, see Host health.

**Health Check History**

This section displays a record of the health checks performed on the host. Click **View Details** to go to the Health Status page. On this page, you can view the health check details. For more information, see Host health. You can click the event content of a check to view the exception items.

#### 2.5.2 Host health

On the Health Status page, you can view the checkers of the selected host, including the checker details, check results, and schemes to clear alerts (if any). In addition, you can log on to the host and perform manual checks on the host.

**Go to the Health Status page under Hosts**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner.
4. Click the **Hosts** tab at the top of the **O&M** page.
5. On the **Hosts** page, select a host in the left-side navigation pane, and click the **Health**
**Status** tab. The **Health Status** page appears.
On the **Health Status** page, you can view all checkers and the check results for the host. The check results are divided into **Critical**, **Warning**, and **Exception**. They are displayed in different colors. Pay attention to the check results, especially the **Critical** and **Warning** results, and handle them in a timely manner.

**View checker details**

1. On the Health Status page, click **Details** in the Actions column of a checker. In the dialog
box that appears, view the checker details. The checker details include the name, source, alias, application, type, default execution interval, and description of the checker, whether scheduling is enabled, and whether data collection is enabled. The schemes to clear alerts are provided in the description.
2. Click **Show More** at the bottom to view more information about the checker.
You can view information about the execution script, execution target, default threshold, and mount point for data collection.

**View alert causes**

You can view the check history and check results of a checker.
1. On the Health Status page, click **+** to expand a checker with alerts.
2. Click the hostname. In the dialog box that appears, click **Details** in the Actions column of a
check result to view the alert causes.

**Clear alerts**

On the Health Status page, click **Details** in the Actions column of a checker with alerts. In the dialog box that appears, view the schemes to clear alerts.

**Log on to a host**

To log on to a host to clear alerts or perform other operations, follow these steps:
1. On the Health Status page, click **+** to expand a checker with alerts.
2. Click the **Log On** icon of a host. The **TerminalService** page appears.
3. On the **TerminalService** page, click the hostname on the left to log on to the host.

**Run a checker again**

After you clear an alert for a host, click **Refresh** in the Actions column of the host to run the checker again for the host. In this way, you can check whether the alert is cleared.

### 2.6 Deep inspection

#### 2.6.1 Overview

DataWorks deep inspection covers and collects the monitoring alerts, resource usage, and key metrics of DataWorks. This allows you to check the health status of DataWorks in a visualized manner, prevent unexpected risks before major issues or faults occur, and ensure service stability.

> **Note:** Apsara Big Data Manager does not revoke inspection reports. However, the risks generated in all inspection reports and the corresponding thresholds are collected.

DataWorks deep inspection covers the following items:

#### 2.6.2 Inspect clusters

Cluster inspection helps you monitor the status of components and services. This topic describes how to use cluster inspection.

**Procedure**

1. Check the final state of the clusters on which DataWorks depends.
This step helps you check whether the clusters on which DataWorks depends are at desired state. If a cluster or server role is not at desired state, contact technical support. i. Inspect the MaxCompute cluster. For more information, see Overview. ii. Inspect the metabase cluster.
2. Check the final state of the DataWorks clusters.
This step helps you check whether the DataWorks clusters are at desired state. If a cluster or server role is not at desired state, contact technical support. i. Go to the **Deployment Summary** page. a. Log on to the Apsara Big Data Manager console. For more information, see Log on to the ABM console. b. In the upper-left corner of the page, click the icon. c. In the **Site Navigation** section, click **TIANJI**. d. In the top navigation bar, choose **Tasks > Deployment Summary**. ii. On the **Deployment Summary** page, click **Deployment Details** to confirm the final state of the clusters. Check whether the base cluster is at desired state. Check whether the clusters for other features are at desired state. If you have not purchased the clusters for other features and have not deployed the corresponding features, skip this step. For more information about the clusters for other features, see Clusters for other features.
3. Inspect the disk usage.
This step helps you check the usage of all disks related to DataWorks. If the usage of a disk exceeds the threshold, clean up the disk. If you cannot clean up a disk, contact technical support. i. Go to the **Deployment Summary** page. a. Log on to the Apsara Big Data Manager console. For more information, see Log on to the ABM console. b. In the upper-left corner of the page, click the icon. c. In the **Site Navigation** section, click **TIANJI**. d. In the top navigation bar, choose **Tasks > Deployment Summary**. ii. On the **Deployment Summary** page, click **Deployment Details** to view the disk usage.
4. Inspect the metadatabases.
This step helps you check whether the databases related to DataWorks are normal. If the database resources are insufficient, contact technical support. i. Log on to the ApsaraDB Operations and Maintenance system. ii. Search for instances whose names start with `dpbiz` . iii. Check whether the disk usage and other metrics are normal. If the disk usage exceeds 80%, the disks are normal.

**Clusters for other features**

The following table describes the clusters for other features.

| Component | Feature | Cluster (Apsara Infrastructure Management) |
|---|---|---|
| Data Map | DataWorksMetaFeature | BaseMapCluster- |
| Data Assets | DataWorksCapitalFeature | BaseAssetCluster- |
| Data Map Agility Edition | DataWorksMetaAgilityFeature | BaseMapCluster- |
| Data Assets Agility Edition | DataWorksCapitalAgilityFeature | BaseAssetCluster- |
| Data Quality | DataWorksDqcFeature | DataWorksDqcCluster- |
| DataService Studio | DataworkChangeFeature | BaseExchangeCluster- |
| Data Analysis | DataWorksRealtimeFeature | BaseRealtimeCluster- |
| Standard Technology Components | DataWorksStandardFeature | BaseStandardCluster- |
| Advanced Technology Components | DataWorksAdvancedFeature | BaseAdvancedCluster- |
| AppStudio | DataWorksAppStudio | DataWorksAppStudioCluster- |
| StreamStudio | DataWorksStreamStudio | DataWorksStreamStudioCluster - |
| GraphStudio | DataWorksGraphstudio | DataWorksGraphstudioCluster- |
| HoloStudio | DataWorksHoloStudio | DataWorksHoloStudioCluster- |
| Engine Operation Center Standard Edition | EngineOpsStandard | DataWorksEngineManageStand ardCluster- |
| Engine Operation Center Advanced Edition | EngineOpsAdvanced | DataWorksEngineManageAdvan cedCluster- |
| Migration Assistant Standard Edition | MigAssistStandard | MigAssistStandardCluster- |

| Migration Assistant Advanced Edition | MigAssistAdvanced | MigAssistAdvancedCluster- |
|---|---|---|
| Real-time Synchronization | DataSyncRTStandardFeature | DataSyncRTStandardCluster- |
| Data Modeling | DatamodDmpFeature | DatamodDmpCluster- |
| Resource Group for Data Scheduling and Data Integration | DataWorksGateway | GatewayExtCluster- |
| Resource group for DataService Studio | DataworkChangeExtFeature | BaseExchangeCluster- |
| Data Security Guard (OEM) | DataworkdsDSFeature | BaseSecurityCluster- |
| Data Security Guard Enhancement Package (OEM) | DsgAdvanced | DsgAdvancedCluster- |
| Data Safety Chain (OEM) | DataworkDschainFeature | BaseSecurityChainCluster- |
| DataBlau (OEM) | BaseDatablauFeature | BaseDatablauCluster- |
| Secure Multi-party Computation (OEM) | BaseMorseFeature | BaseMorseCluster- |

#### 2.6.3 Inspect the base_meat project

The base_meta project is a metadata project of DataWorks. The project is used to process data of DataWorks offline. This topic describes how to inspect the base_meat project to check the status of the tasks in the base_meta project.

**Procedure**

You must log on to the base_meta project to inspect the project. Perform the following steps:
1. Go to the **Apsara Infrastructure Management** console.
i. Log on to the Apsara Big Data Manager console. For more information, see Log on to the ABM console. ii. In the upper-left corner of the page, click the icon. iii. In the **Site Navigation** section, click **TIANJI**.
2. Obtain the logon address of the base_meta project.
i. Go to the Cluster Dashboard page of the BasicCluster cluster. In the **Apsara Infrastructure Management** console, click the **C** tab in the left-side navigation pane. Perform the steps shown in the following figure to go to the **Cluster**
**Dashboard** page of the BasicCluster cluster.
ii. In the **Cluster Resource** section, set the filter to **dns** for the **Type** column and **base-**
**biz-commonbase** for the **App** column.
iii. Obtain the logon address of the base_meta project in the **Parameters** column of the row that meets the filter conditions.
3. Obtain the logon username and password of the base_meta project.
i. Go to the Cluster Dashboard page of the MaxCompute cluster. On the **C** tab of the **Apsara Infrastructure Management** console, perform the steps shown in the following figure to go to the Cluster Dashboard page of the MaxCompute cluster. ii. In the **Cluster Resource** section, set the filter to **base_admin** for the **Name** column. iii. Find the service that meets the filter condition and click **Show More** in the **Result** column. You can obtain the logon username and password of the base_meta project.
4. Log on to the base_meta project in the DataWorks console.
5. Go to the Operation Center page to view the status of the MaxCompute project.
If the MaxCompute project is not running, contact technical support to troubleshoot the issue.

#### 2.6.4 Inspect the BaseBizAlisa service

You can inspect the BaseBizAlisa service to check the status of the service. The BaseBizAlisa service is used to manage remote tasks and gateways. This topic describes how to inspect the BaseBizAlisa service.

**Procedure**

1. Check the status of gateways.
A gateway is a basic hardware unit for DataWorks to run tasks. The following roles are involved: base-baseBizApp.BaseBizGateway# base-baseBizApp.BaseBizCdpGateway# base-baseBizApp.BaseBizGateway# base-baseBizApp.BaseBizCdpGateway# base-baseBizApp.BaseBizGatewaySearch# base-baseBizApp.BaseBizGatewayStreamX# You can check the status of the BaseBizAlisa service in the metadatabase of the service. i. Log on to the dpbizalisa database. For more information, see Appendix: Log on to a database. ii. Check the number of gateways. Execute the following statements to check the number of gateways in different scenarios: Total number of standard gateways: `select`

| node name,node address,cluster name,max slot,live,active type from _ _ _ _ _ |   |
|---|---|

```
dpbizalisa.alisa_node;
```

Number of Level-1 scheduling gateways: `select`

```
node_name,node_address,cluster_name,max_slot,live,active_type from dpbizalisa.alisa_node where cluster_name='sys_default';
```

Number of Level-2 scheduling gateways: `select`

```
node_name,node_address,cluster_name,max_slot,live,active_type from dpbizalisa.alisa_node where cluster_name='sys_default_cdp';
```

Number of non-standard gateways deployed on ECS: `select`

```
node_name,node_address,cluster_name,max_slot,active_type,live from alisa_node where node_name not regexp 'cloud|docker';
```

Total number of slots per cluster: `select cluster_name,sum(max_slot) from`

```
dpbizalisa.alisa_node group by cluster_name;
```

iii. Execute the select * from alisa_node; statement to query the alisa_node table. The following figure shows the sample result. If the value of the `active_type` or `live` field is not 1, the corresponding gateway is disabled or is under repair. Contact technical support to troubleshoot the issue.
2. Check whether a backlog of tasks exists.
If multiple records whose values of the `status` field are 2 and the number of the records is not decreasing, contact technical support to troubleshoot the issue. i. Log on to the dpbizalisa database. For more information, see Appendix: Log on to a database. ii. Execute the select count(1),status from dpbizalisa.alisa_task group by status; statement to check whether a backlog of tasks exists.
3. Inspect the dirty data of the service.
This step helps you check whether the service is running as expected. If dirty data exists and cannot be cleared automatically, contact technical support to troubleshoot the issue. i. Log on to the dpbizalisa database. For more information, see Appendix: Log on to a database. ii. Check the dirty data of the service. Execute the following statements:

```
 select count(*) alisa_task_callback from dpbizalisa.alisa_task_callback where
task_id not in (select task_id from alisa_task);
 select count(*) alisa_task_release from dpbizalisa.alisa_task_release where
task_id not in (select task_id from alisa_task);
 select count(*) alisa_task_on_node from dpbizalisa.alisa_task_on_node where
task_id not in (select task_id from alisa_task);
```

#### 2.6.5 Inspect the BaseBizPhoenix service

The BaseBizPhoenix service is used to schedule tasks. You need to check whether the metadatabase of the service needs to be cleared. This topic describes how to inspect the BaseBizPhoenix service.

**Procedure**

Perform the following steps to check whether the amount of historical data stored in the system is too large:
1. Log on to the dpbizphoenix database. For more information, see Appendix: Log on to a
database.
2. Check the amount of data.
Execute the following statements to view the amount of data in different scenarios: Number of instances that are scheduled per day: `select bizdate,count(*) from`

```
phoenix_task_inst where dag_type = 0 group by bizdate desc limit 10;
```

Total number of instances: select count(*) from dpbizphoenix.phoenix_task_inst; Amount of data in the phoenix_task_relation table: `select count(*) from`

```
phoenix_task_relation;
```

Amount of data in the phoenix_dag_inst table: select count(*) from phoenix_dag_inst; Amount of data in the phoenix_schedule_event table: `select count(*) from`

```
phoenix_schedule_event;
```

If the amount of data is too large, the system may be affected, and you need to manually clear the data. For example, if the phoenix_task_inst table contains more than one million data records, the table needs to be cleared.

#### 2.6.6 Inspect the BaseBizCdp service

The BaseBizCdp service provides multiple features. For example, the service is used to manage data sources, parse data integration tasks, and start data integration tasks. This topic describes how to inspect the BaseBizCdp service.

**Procedure**

Perform the following steps to check whether the `t_instance` table has more than 100,000 data records:
1. Log on to the dwcdp database. For more information, see Appendix: Log on to a database.
2. Execute the select count(*) from t_instance; statement to check the amount of data in
the table.

**Result**

If the number of data records exceeds 100,000, the system may be affected, and you need to manually clear the data.

#### 2.6.7 Appendix: Log on to a database

This topic describes how to log on to a database.

**Procedure**

Perform the following steps to log on to a database.
1. Log on to the Apsara Big Data Manager console.
For more information, see Log on to the ABM console.
2. In the upper-left corner of the page, click the
icon.
3. In the **Site Navigation** section, click **TIANJI**.
4. On the **C** tab of the **Apsara Infrastructure Management** console, perform the steps
shown in the following figure.

> **Note:** You must go to the Cluster Dashboard page of the cluster for the corresponding service to obtain the logon address of the database to which you want to log on. In the example shown in the following figure, the base service is used. In actual use, select the service based on your business scenario.

5. In the **Cluster Resource** section, set the filter to **db** for the **type** column. Find the
database in the **name** column and obtain the connection information of the database. Then, log on the database based on the connection information.

### 2.7 Server role O&M

This topic describes the server roles in DataWorks.

**Background information**

The following table describes the server roles provided in DataWorks.

| Server role | Service | Maximum quantity | Form | Port | High availability |
|---|---|---|---|---|---|
| BaseBizSso | Single sign-on (SSO) | 2 | Container | 7001 | Yes |
| BaseBizWkbench | Operation Center | 2 | Container | 7001 | Yes |
| Redis1 | Redis service | 1 | Container | 6379 or 26379 | Yes |
| Redis2 | Redis service | 2 | Container | 6379 or 26389 | Yes |
| BaseBizDmc | Data Map | 2 | Container | 7001 | Yes |
| BaseBizBaseapi | API scheduling | 2 | Container | 7001 | Yes |
| BaseBizDbinit | Database initialization | 1 | Container | N/A | N/A |
| BaseBizPhoenix | Scheduling engine | 3 | Container | 7001 | Yes |
| BaseBizAlisa | Execution engine | 2 | Container | 7001 | Yes |
| BaseBizConsole | Apsara Stack console | 2 | Container | 7001 | Yes |
| BaseBizTenant | Tenants | 2 | Container | 7001 | Yes |
| BaseBizMetaserv ice | Metadata | 2 | Container | 7001 | Yes |

| BaseBizMario | Real-time synchronization | 2 | Container | 7001 | Yes |
|---|---|---|---|---|---|
| BaseBizDashboar d | Data Integration dashboard | 2 | Container | 7001 | Yes |
| BaseBizCdp | Offline synchronization scheduling | 2 | Container | 7001 | Yes |
| BaseBizGateway | Scheduling gateway deployed in Docker | 2 | Container | 7001 | Yes |
| BaseBizCdpGate way | Offline synchronization gateway deployed in Docker | 2 | Container | 8000 | Yes |
| BaseBizGateway Search | Gateway for code search and backup or restoration | 2 | Container | 8000 | Yes |
| BaseBizGateway WithNc | Scheduling gateway deployed on a physical server | At least one | Physical server | 8000 | N/A |
| BaseBizCdpGate wayWithNc | Offline synchronization gateway deployed on a physical server | At least one | Physical server | 8000 | N/A |
| BaseBizCommon base | DataStudio | 4 | Container | 7001 | Yes |
| ServiceTest | Smoke testing | 1 | Container | N/A | N/A |
| DataworksDatao sPanel | Workspace and tenant management | 2 | Container | 7001 | Yes |
| DataworksMessa geCenter | Notification Center | 2 | Container | 7001 | Yes |
| BaseBizTsp | Code repository service | 2 | Container | 7001 | Yes |
| DataworksMosad | Intelligent monitoring | 2 | Container | 7001 | Yes |
| BaseBizDiide | Data Integration | 2 | Container | 7001 | Yes |
| DataworksNavig ation | Public header | 2 | Container | 7001 | Yes |

| BaseBizWormhol e | Wormhole service | 2 | Container | 7001 | Yes |
|---|---|---|---|---|---|
| BaseBizDataOsA piInit | POP API registration | 1 | Container | N/A | N/A |
| DataworksDsmG uard | Security Center | 2 | Container | 7001 | Yes |
| BaseBizGateway StreamX | Real-time synchronization gateway | 2 | Container | 8000 | Yes |
| BaseBizAlisaloga gent | Alisa log agent | 2 | Container | 7001 | Yes |
| DataworksExecut orNode | Real-time execution engine node | 2 | Container | 7001 | Yes |
| DataworksExecut orManager | Real-time execution engine manager | 2 | Container | 7001 | Yes |
| DataworksNode market | Custom node | 2 | Container | 7001 | Yes |
| DataworksMeasu re | Metering | 2 | Container | 7001 | Yes |
| DataworksLsp | Language Server Protocol (LSP)- based intelligent code editor | 2 | Container | 7001 | Yes |
| DataworksPlugin | Microservices framework | 2 | Container | 7001 | Yes |
| DataworksCdn | Frontend service | 2 | Container | 7001 | Yes |
| DataworksMetaPl uginService | Metadata plug-in service | 2 | Container | 7001 | Yes |
| BaseBizOps | O&M Assistant | 2 | Container | 7001 | Yes |
| DataworksElastic search | Elasticsearch service | 3 | Container | 9200/9300/ 9114 | Yes |

**View details of server roles**

1. Log on to the Apsara Infrastructure Management console. On the **C** tab in the upper-left
corner, select **base** as **Project**. Then, click the DataWorks cluster that you want to view.
2. In the **Service Instances** section of the **Cluster Dashboard** page, find **base-baseBizApp**
and click **Details** in the **Actions** column.
3. In the **Server Role List** section of the **Service Instance Information Dashboard** page,
view the details of server roles, such as the status.

**BaseBizSso#**

Role description The server role provides the SSO logon service and depends on the BaseBizDbinit# and Redis1# server roles. RMA or restart The physical server on which the server role is deployed supports the Return Merchandise Authorization (RMA) or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-sso/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizWkbench#**

Role description The server role provides the features of Operation Center and depends on the BaseBizDbinit#, BaseBizTenant#, and Redis1# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-wkbench/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**Redis1#**

Role description The server role provides the Redis service and does not depend on other server roles. RMA or restart None. Reclone The physical server on which the server role is deployed supports the reclone operation. Logs

```
Log path: /var/log/redis/redis.log and /var/log/redis/sentinel.log
```

Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**Redis2#**

Role description The server role provides the Redis service and depends on the Redis1# server role. RMA or restart None. Reclone The physical server on which the server role is deployed supports the reclone operation. Logs

```
Log path: /var/log/redis/redis.log and /var/log/redis/sentinel.log
```

Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizDmc#**

Role description The server role provides the features of Data Map and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-dmc/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizBaseapi#**

Role description The server role schedules the API service and depends on the BaseBizDbinit# and BaseBizTenant# server roles. RMA or restart None. Reclone The physical server on which the server role is deployed supports the reclone operation. Logs To view logs, run the following commands:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the BaseBizBaseapi container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id;
```

Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizDbinit#**

Role description The server role provides the database initialization service and does not depend on other server roles. RMA or restart None. Reclone The physical server on which the server role is deployed supports the reclone operation. Logs To view logs, run the following commands:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the BaseBizDbinit container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id ;
```

Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizPhoenix#**

Role description The server role provides the schedule engine and features such as generating instances of auto triggered nodes. The server role depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-phoenix/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizAlisa#**

Role description The server role provides the execution engine and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-alisa/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizConsole#**

Role description The server role provides the Apsara Stack console and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-console/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizTenant#**

Role description The server role provides the tenant service and depends on the BaseBizDbinit#, DataworksMessageCenter#, and Redis1# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-tenant/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizMetaservice#**

Role description The server role provides the metadata service and depends on the BaseBizAlisa#, BaseBizBaseapi#, BaseBizDbinit#, BaseBizPhoenix#, and BaseBizTenant# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-metaservice/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizMario#**

Role description The server role provides the real-time synchronization service and depends on the BaseBizAlisa#, BaseBizDbinit#, and BaseBizTenant# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-mario/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizDashboard#**

Role description The server role provides the Data Integration dashboard and depends on the BaseBizAlisa#, BaseBizDbinit#, and BaseBizTenant# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-dashboard/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizCdp#**

Role description The server role provides the offline synchronization scheduling service and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-cdp/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizGateway#**

Role description The server role provides the scheduling gateway deployed in Docker and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizCdpGateway#**

Role description The server role provides the offline synchronization gateway deployed in Docker and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizGatewaySearch#**

Role description The server role provides the gateway for code search and backup or restoration and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizGatewayWithNc#**

Role description The server role provides the scheduling gateway deployed on a physical server and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizCdpGatewayWithNc#**

Role description The server role provides the offline synchronization gateway deployed on a physical server and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizCommonbase#**

Role description The server role provides the features of DataStudio and depends on the BaseBizDbinit#, BaseBizTenant#, and Redis1# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-commonbase/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**ServiceTest#**

Role description The server role provides the smoke testing service. You can create smoke testing instances and verify features by using the server role. The server role is deployed as a Docker container. The server role depends on the BaseBizCommonbase# and BaseBizMetaservice# server roles. RMA or restart None. Reclone The physical server on which the server role is deployed supports the reclone operation. Logs To view logs, run the following commands:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the ServiceTest container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id;
```

Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksDataosPanel#**

Role description The server role provides the workspace and tenant management services and depends on the BaseBizDbinit# and BaseBizTenant# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-dataos-panel/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksMessageCenter#**

Role description The server role provides the features of Notification Center and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-message-center/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizTsp#**

Role description The server role provides the code repository service and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-tsp/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksMosad#**

Role description The server role provides the intelligent monitoring service and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-mosad/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizDiide#**

Role description The server role provides the Data Integration service and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-diide/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksNavigation#**

Role description The server role provides public headers and depends on the BaseBizDbinit# and BaseBizTenant# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-navigation/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizWormhole#**

Role description The server role provides the wormhole service and depends on the BaseBizDbinit# and Redis1# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-wormhole/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizDataOsApiInit#**

Role description The server role provides the POP API registration service and depends on the BaseBizTenant# server role. RMA or restart None. Reclone The physical server on which the server role is deployed supports the reclone operation. Logs To view logs, run the following commands:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the BaseBizDataOsApiInit container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id;
```

Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksDsmGuard#**

Role description The server role provides the features of Security Center and depends on the BaseBizTenant# and DataworksNavigation# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dsm-guard/logs/loginlogs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizGatewayStreamX#**

Role description The server role provides the real-time synchronization gateway and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizAlisalogagent#**

Role description The server role provides the Alisa log agent and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-alisalogagent/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksExecutorNode#**

Role description The server role provides the real-time execution engine node and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-executor-node/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksExecutorManager#**

Role description The server role provides the real-time execution engine manager and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-executor-manager/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksNodemarket#**

Role description The server role provides the custom node and depends on the BaseBizAlisa# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-nodemarket/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksMeasure#**

Role description The server role provides the metering service and depends on the BaseBizTenant# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-measure/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksLsp#**

Role description The server role provides the LSP-based intelligent code editor and does not depend on other server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-lsp/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksPlugin#**

Role description The server role provides the microservices framework and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-plugin/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksCdn#**

Role description The server role provides the frontend service and does not depend on other server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-cdn/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksMetaPluginService#**

Role description The server role provides the metadata plug-in service and depends on the BaseBizDbinit# server role. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-mps/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**BaseBizOps#**

Role description The server role provides the features of O&M Assistant and depends on the BaseBizDbinit# and Redis1# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-tenant-ops/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic.

**DataworksElasticsearch#**

Role description The server role provides the Elasticsearch service and depends on the Redis1# and Redis2# server roles. RMA or restart The physical server on which the server role is deployed supports the RMA or restart operation. You need to perform the operation on physical servers in batches. Reclone The physical server on which the server role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/elasticsearch-6.8.23/logs` Monitoring Check whether the server role is at desired state in the Apsara Infrastructure Management console. For more information, see the View details of server roles section in this topic. and commands

## 3 Common administration tools and commands

**tools and commands**

### 3.1 Find the host where a service resides

**resides**

This topic describes how to find the host where a service resides.

**Procedure**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **base-baseBizApp** service. On the **Machine Details** page, view information
about the host where the service resides.

### 3.2 View cluster resources

This topic describes how to view the applications, resources, status, and version of a cluster.

**Procedure**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **Cluster Resource** tab. Then, you can filter required cluster information by
**Server Role**, **Version**, **Name**, **Type**, or **Status**.
Find the target application and click **Details** in the **Application Result** column to view detailed information about the application. For example, if you need to log on to the and commands database of a specific application, you can find detailed logon information about the database in the **Application Result** message.

### 3.3 View service registration variables

**variables**

This topic describes how to view the registration variables of a service.

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Big Data Manager (ABM) console. ii. In the upper-left corner, click the icon and select **Site Navigation > TIANJI**.
2. In the left-side navigation pane of the Apsara Infrastructure Management console, choose
**O&M Tools > Service Registration Variable Dashboard**.
3. Switch the search type to search for the service that you want to view.
4. Click the
icon next to the content in the **Service Registration** column to view details about the registration variables of the service.

> **Note:** If a large number of data exists, you can click the data displayed in the **Service** **Registration** column to view the data in a separate window.

**Change the domain name of a service**

If your Apsara Stack version is 3.18.2 or later, the domain names in the registration information of some services are changed. The following table describes the changes.

| Baseline | Service name | Before change | After change |
|---|---|---|---|
|   | base-biz- commonbase | ide.${global:internet- domain} | ide.${global:console- private-domain} |
|   | base-biz- dashboard | dashboard.${global:interne t-domain} | dashboard.${global:consol e-private-domain} |
|   | base-biz-diide | di.${global:internet- domain} | di.${global:console- private-domain} |

and commands

| service-base- baseBizApp | base-biz-dmc | dmc.${global:internet- domain} | dmc.${global:console- private-domain} |
|---|---|---|---|
|   | base-biz-sso | cloudsso.${global:internet- domain} | cloudsso.${global:console- private-domain} |
|   | base-biz- wkbench | wkbench.${global:internet- domain} | wkbench.${global:console- private-domain} |
|   | dataworks-bff | bff.${global:internet- domain} | bff.${global:console- private-domain} |
|   | dataworks-cdn | ms.cdn.${global:internet- domain} | dataworks- cdn.${global:console- private-domain} |
|   | dataworks- dataos-panel | setting.${global:internet- domain} | setting.${global:console- private-domain} |
|   | dataworks-dsm- guard | approval.${global:internet- domain} | approval.${global:console- private-domain} |
|   |   | guard.${global:internet- domain} | guard.${global:console- private-domain} |
|   | dataworks-lsp | lsp.${global:internet- domain} | lsp.${global:console- private-domain} |
|   | dataworks- message-center | message.${global:internet- domain} | message.${global:console- private-domain} |
|   | dataworks- navigation | nav.${global:internet- domain} | nav.${global:console- private-domain} |
|   | dataworks- nodemarket | nodemarket.${global:intern et-domain} | nodemarket.${global:cons ole-private-domain} |
|   |   | ms.${global:internet- domain} | ms.${global:console- private-domain} |
|   |   | dwexcel-pivot- server.ms.${global:internet -domain} | dwexcel-pivot-server- ms.${global:console- private-domain} |

|   | tion tools |   |   |
|---|---|---|---|
|   | dataworks- plugin |   |   |
|   |   | pg- service.ms.${global:interne t-domain} | pg-service- ms.${global:console- private-domain} |
|   |   | morse- engine.ms.${global:interne t-domain} | morse-engine- ms.${global:console- private-domain} |
|   |   | dw-emr-meta- manager.ms.${global:inter net-domain} | dw-emr-meta-manager- ms.${global:console- private-domain} |
|   |   | mysql- service.ms.${global:interne t-domain} | mysql-service- ms.${global:console- private-domain} |
|   |   | model.${global:internet- domain} | Delete |
|   |   | model.${global:intranet- domain} |   |
|   |   | indicator.${global:internet- domain} |   |
|   |   | indicator.${global:intranet- domain} |   |
|   |   | dsd.${global:internet- domain} |   |
|   |   | dsd.${global:intranet- domain} |   |
|   |   | layer.${global:internet- domain} |   |
|   |   | layer.${global:intranet- domain} |   |
| service-base- dschain | dschain | dschain.dw.${global:region }.${global:internet- domain} | dschain- dw.${global:console- private-domain} |
| 2 |   | > Document Version: 2025011 |   |

| DataWorks |   |   |   |
|---|---|---|---|
|   |   | dschain- intra.dw.${global:region}.$ {global:intranet-domain} | dschain-intra- dw.${global:intranet- domain} |
| service-base- datablau | datablau-plugin | datastudio-er-model- web.ms.${global:internet- domain} | datastudio-er-model-web- ms.${global:console- private-domain} |
|   |   | datastudio-er-model- api.ms.${global:internet- domain} | datastudio-er-model-api- ms.${global:console- private-domain} |
|   |   | datablau- modelstore.ms.${global:int ernet-domain} | datablau-modelstore- ms.${global:console- private-domain} |
|   |   | datablau- store.ms.${global:internet- domain} | datablau-store- ms.${global:console- private-domain} |
|   |   | datablau- central.ms.${global:interne t-domain} | datablau-central- ms.${global:console- private-domain} |
| service-base- modelengine | dataworks- modelengine | model- engine.ms.${global:interne t-domain} | model.${global:console- private-domain} |
| service-base- dsgadvanced | dsg | dsgadvanced.${global:inter net-domain} | dsgadvanced.${global:con sole-private-domain} |
| service-base- migassist | dataworks- migration | migration.${global:internet -domain} | migration.${global:console -private-domain} |
| service-dataworks- holostudio | dataworks- holostudio | holostudio.${global:interne t-domain} | holostudio.${global:consol e-private-domain} |
| service-dataworks- graphstudio | dataworks- graphstudio | gs.${global:internet- domain} | gs.${global:console- private-domain} |
| service-dataworks- streamstudio | ssweb | ss.${global:internet- domain} | ss.${global:console- private-domain} |
| service-dataworks- dqc | base-biz- dqcsupervisor | dqc.${global:internet- domain} | dqc.${global:console- private-domain} |

and commands

| service-dataworks- dataassets | dataworks- dataassets | dataassets.${global:interne t-domain} | dataassets.${global:consol e-private-domain} |
|---|---|---|---|
| service-dataworks- asset | dataworks-asset | assetv2.${global:internet- domain} | assetv2.${global:console- private-domain} |
| service-dataworks- dataservice | dataservice web _ | ds.${global:internet- domain} | ds.${global:console- private-domain} |
| service-dataworks- realtime | dwexcel | da.${global:internet- domain} | da.${global:console- private-domain} |
| service-dataworks- dsgapp | dsg | dsg.${global:internet- domain} | dsg.${global:console- private-domain} |
| service-dataworks- openplatform | dataworks- openplatform | openplatform.${global:inte rnet-domain} | openplatform.${global:con sole-private-domain} |
| service-dataworks- governance | dataworks- datagovernance | dgc.${global:internet- domain} | dgc.${global:console- private-domain} |

### 3.4 Commands to restart services

Enter the container that runs the service as an admin user, and then run the following commands to restart services.

> **Note:** Only admin users can run the following commands to restart the service.

To restart the base-biz-cdp service, run the `/home/admin/cdp_server/bin/appctl.sh` `restart` command. To restart the base-biz-gateway service, run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/serverctl
```

`restart` command. To restart other services, run the `/home/admin/base-biz-[application name]/bin/jbossctl` `restart` command. For example, to restart the base-biz-alisa service, run `/home/admin/base-biz-`

```
alisa/bin/jbossctl
       restart .
```

### 3.5 View logs of a failed instance

This topic describes how to view logs of a failed instance in Operation Center.

**Procedure**

1. Log on to the DataWorks console.
2. On the DataStudio page, click
in the upper-left corner and choose **All Products >** and commands
**Operation Center**.
3. On the **Dashboard** page, click **Failed** in the **Instances** section. The **Cycle Instance** page
appears. On this page, you can view all the instances that failed to run in the current workspace.
4. Click the target instance, and then right-click the failed node on the DAG that appears on
the right side of the page.
5. Select **View Runtime Log**.

### 3.6 Rerun multiple instances at a time

**time**

You can use the batch rerun feature of DataWorks to rerun multiple instances at a time.

**Procedure**

1. Log on to the DataWorks console.
2. On the DataStudio page, click
in the upper-left corner and choose **All Products >**
**Operation Center**.
3. On the **Dashboard** page, click **Failed** in the **Instances** section. The **Cycle Instance** page
appears. On this page, you can view all the instances that failed to run in the current workspace.
4. Select the instances to be rerun.
5. Choose **More > Rerun** in the lower-left corner.
6. In the message that appears, click **Rerun**.

### 3.7 Stop multiple instances at a time

**time**

You can use the batch stop feature of DataWorks to stop multiple instances at a time.

**Procedure**

1. Log on to the DataWorks console.
2. On the DataStudio page, click
in the upper-left corner and choose **All Products >**
**Operation Center**.
3. On the **Dashboard** page, click **Running** in the **Instances** section. The **Cycle Instance**
page appears. On this page, you can view all the running instances in the current workspace.

> **Note:** You can stop only instances that are running.

4. Select the instances that you want to stop.
5. Choose **More > Stop** in the lower-left corner.
6. In the message that appears, click **Stop**.
and commands

### 3.8 Commonly used Linux commands

**commands**

This topic describes the commonly used Linux commands.

**Display workloads in the Linux system: top**

View the three numbers after load average, which indicate the workload averages for the last 5, 10, and 15 minutes, respectively. If you divide one of these numbers by the quantity of logical CPUs and the result is greater than 5, the Linux system is overloaded.

**List the sizes of files: du**

You can run the `du -sh` command with a file name added at the end to view the size of the specified file. If you run the `du -sh *` command, you can view the sizes of all the files in the current directory.

**List processes in the Linux system: ps**

You can run the `ps -ef` command to view the processes that are running in the Linux system.

**Search for strings: grep**

To search for a string in a specified log file and display all lines that contain the string, run the command in the following format:

```
grep ["String"] [File name]
```

To search for a string in a specified file and display only the first few lines that contain the string, run the command in the following format:

```
grep -C Number of lines ["String"] [File name]
```

> **Note:** The -C parameter is an uppercase letter. Set its value to a number.

To search for a string in a specified file and display only the last few lines that contain the string, run the command in the following format:

```
grep -A Number of lines ["String"] [File name]
```

**Terminate processes: kill**

You can run the `kill -9` command with the PID of a process added at the end to terminate the process.

**docker commands**

List all containers: `docker ps -a` List the logs of a container: `docker logs [Container ID]` Log on to a container: `docker exec -it [Container ID] bash` and commands

### 3.9 View the slot usage of resource groups

**resource groups**

This topic describes how to view the slot usage of a resource group. Scenario: When a large number of nodes are waiting for resources in Operation Center, you can run a set of commands to view the slot usage of each resource group. First, log on to the base-biz-alisa database. In an Apsara Stack V3 environment, select base from the Project drop-down list on the Clusters page in Apsara Infrastructure Management. Locate the base-biz-alisa service whose type is db in the filtered results. Right-click the Result column and choose Show More from the shortcut menu to obtain the connection information of the database. Then, run a MySQL command to log on to the database based on the obtained information. Run the following command to view the top 10 nodes by execution duration:

```
select task_id,gateway,slot,create_time from alisa_task where status=2 order by create_ time limit 10;
```

Run the following command to view the top 10 nodes by slot usage:

```
select task_id,gateway,slot,create_time from alisa_task where status=2 order by slot de sc limit 10;
```

Run the following command to view the total number of nodes for each slot. Based on the command output, you can find out nodes that occupy a large number of slot resources.

```
select slot,count(*) from alisa_task where status=2 group by slot;
```

Run the following command to view the slot usage of each resource group:

```
select exec_target,sum(slot) from alisa_task where status=2 group by exec_target;
```

View the status of each gateway server. If the values of live and active_type are 1 for any gateway server, the gateway server fails.

```
select * from alisa_node;
```

perations

## 4 Process daily administration operations

**administration operations**

### 4.1 Daily check

#### 4.1.1 Check the service status and basic server information

**server information**

This topic describes how to view the basic cluster information, server status, and the number of servers in the desired state.

**Procedure**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, click **Reports**.
3. On the **C** tab, select **base** from the **Project** drop-down list.
4. Move the pointer over
next to the target server and select **Dashboard**. On the **Cluster Dashboard** page, view information in the **Basic Cluster Information**,
**Machine Status Overview**, and **Machines in Final Status** sections.
If only blue is shown in the Machine Status Overview section, all servers in the current cluster are running properly. If yellow is shown in the Machine Status Overview section, errors occur on servers.

#### 4.1.2 Check the status of a gateway server

This topic describes how to check the status of a gateway server.

**Procedure**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, click **Reports**.
3. On the **C** tab, select **base** from the **Project** drop-down list.
4. Move the pointer over
next to the target server and select **Dashboard**.
5. In the **Cluster Resource** section, move the pointer over the **App** column and click
.
6. In the dialog box that appears, enter **base-biz-alisa** in the Filter field and click **Apply**
perations
**Filter**.
7. Filter services whose type is **db** in the same way.
8. Find the target service, right-click the information in the **Result** column, and then select
**Show More** to view the endpoint, username, and password for logging on to the database.
9. Connect to the database and run the following MySQL command to query the node
information:

```
Select * from alisa_node;
```

If the value of the **active_type** or **live** parameter in the command output contains -1 or 0, the service is abnormal. Contact Alibaba Cloud technical support engineers.

#### 4.1.3 Monitor service roles and servers

This topic describes how to view the details of monitored service roles and servers.

**Procedure**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **Services** tab and then click the **base-baseBizApp** service.
6. On the **Service Details** page, click the target service role to view the servers where the
service resides.
7. Find the target server and click **View** in the **Metric** column.
8. In the **Machine Metrics** dialog box, view the information on the **Server Role Metric** and
**Machine Metrics** tabs.

### 4.2 View logs of the services

Logs of the gateway service are stored in

```
 /home/admin/alisatasknode/logs/alisatasknode.log .
```

Logs of the cdp services are stored in `/home/admin/cdp_server/logs/cdp_server.log` . Logs of other services are stored in `/home/admin/base-biz-[service name]/base-biz-[service`

```
name].log .
```

For example, the logs of the base-biz-phoenix service are stored in `/home/admin/base-biz-`

```
phoenix/base-biz-phoenix.log .
```

perations

### 4.3 Scale out a cluster that runs the base-biz-gateway service

**the base-biz-gateway service**

This topic describes how to scale out a cluster that runs the base-biz-gateway service.

**Prerequisites**

Before you apply a scaling change, make sure that the system is running in a status that is conducive to the change. For example, make sure that the storage space is sufficient, and verify the prerequisites such as the permissions on the files, the owners and paths of the files, and the software version. Before you scale out a base cluster, make sure that it reaches the desired state and works as expected. A screenshot of the key initial configurations for the cluster is saved. IP addresses do not conflict. If you want to use a new buffer cluster for the scale-out operation, make sure that the IP addresses that Deployment Planner assigns to the servers in the cluster are not used in the current environment. This helps avoid exceptions arising from IP address conflicts after the scale-out. The clone_mode parameter is set to normal.

> **Note:** Apsara Infrastructure Management of V3.3 and later versions support cloning protection. Before the scale-out, you must set the clone_mode parameter to normal. After the scale-out is complete, set this parameter to block. Cloning protection is not required in Apsara Infrastructure Management of a version earlier than V3.3.

To set the clone_mode parameter to normal, perform the following steps: i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane, click **Reports**. iii. In the top navigation bar, choose **Operations > Cluster Operations**. iv. Click **Global Clone Switch**. In the **Global Clone Switch** dialog box, select **normal**. v. Click **OK**.

**Procedure**

1. Create a buffer cluster.
Skip this step if an existing buffer cluster has idle servers and the physical machine, memory, CPU, and disk size of the idle servers are the same as those of current servers that run the base-biz-gateway service. perations *In the scale-out procedure, use actual parameter values and IP addresses instead of the specific parameter values in this guide.

> **Note:** When you plan to scale out the cluster with Deployment Planner, make sure that the name of the new buffer cluster is different from that of any existing buffer cluster.

i. Copy and paste _tianji_imports to the /apsarapangu/disk3/u_disk/ directory of the OPS1 server and run the following command in the tianji_zhuque_sdk directory:

```
./tianji_zhuque_exchanger.py import --skip_packages -o ${Final status in Apsara Inf rastructure Management} -c tianji_dest.conf
```

ii. Log on to the **Apsara Infrastructure Management** console. Select **buffer** from the
**Project** drop-down list.
iii. Click the buffer cluster to view the status of servers in the cluster. iv. Run the following commands on the OPS1 server to call API operations to query scale-out information:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf ./tianji_clt machinestatus -c buffer --config clt2.conf
```

2. Scale in the buffer cluster by moving idle servers to the default cluster.

> **Note:** You can use the default cluster to scale out the cluster that runs the base-biz-cdp and base-biz-gateway services.

i. On the **Cluster Operations** page, click the desired buffer cluster. ii. On the **Cluster Details** page, click the **Cluster Configuration** tab. iii. Click the **machine_group.conf** file. Make sure that the value of **scalable** is **true** for the new buffer cluster. perations iv. Run the following commands on the OPS1 server to scale in the buffer cluster:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf (After you run this command, if a message indicating that a soft lin k already exists appears, proceed with the next command.) ./tianji_ops_tool.py contract_nc -c [buffer cluster name] -l [Hostname of the serve r to be removed], [Hostname of the server to be removed],.... --config clt2.conf -s [SRG name]
```

| Parameter | Description |
|---|---|
| -c | The name of the buffer cluster that you want to scale in, which starts with buffer-cluster. |
| -l | The list of hostnames of servers to be removed. Separate multiple hostnames with commas (,). |
| -s | The name of the SRG where the servers reside. You can find the SRG name in the machine group.conf file of the buffer cluster. _ |
| -config | The tianji clt file. _ Note These commands cannot contain Chinese characters. |

v. On the **Cluster Operations** page, verify that the servers are removed. vi. Run the following commands on the OPS1 server to call API operations to query scale-in information:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf (After you run this command, if a message indicating that a soft lin k already exists appears, proceed with the next command.) ./tianji_clt machinestatus -c default --config clt2.conf
```

vii. Go to the details page of the new buffer cluster, and check whether the configurations of the servers are deleted from the machine_group.conf file. If the configurations of the servers still exist, delete them from the machine_group.conf file and then submit a rolling task.
3. Add servers to the base cluster and specify the name of the SRG where the servers reside.
i. In the left-side navigation pane of the **Apsara Infrastructure Management** console, click **Reports**. ii. In the top navigation bar, choose **Operations > Cluster Operations**. perations iii. Right-click the desired base cluster and choose Monitoring > **Cluster Configuration**. On the page that appears, verify that **Clone Switch** is set to **Real Clone**. iv. Run the following commands to perform scaling. A rolling task is triggered after you run these commands.

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf (After you run this command, if a message indicating that a soft lin k already exists appears, proceed with the next command.)
```

To add servers to the cluster that runs the base-biz-gateway service, run the following command:

```
./tianji_ops_tool.py expand_nc -c [Base cluster name] -s BaseGwGroup -l [machine1,machine2] --config clt2.conf
```

To add servers to the cluster that runs the base-biz-cdp service, run the following command:

```
./tianji_ops_tool.py expand_nc -c [Base cluster name] -s BaseCdpGwGroup -l [machine 1,machine2] --config clt2.conf
```

v. Run the following command to call an API operation to query the scaling result:

```bash
curl http://127.0.0.1:7070/api/v3/column/m.*?m.id=[machine hostname]
```

vi. Log on to the OpsClone container and run the following command to view the clone status:

```
/home/tops/bin/python /root/opsbuild/bin/opsbuild.py acli list --status=ALL -n 1000 0 | vim -
```

4. Export the file that contains the information about the recent desired state.
After you complete the scale-out, export the file that contains the information about the recent desired state to Deployment Planner. This ensures the success of subsequent scalein and scale-out operations.
5. Verify the scale-out.
perations i. Check the heartbeat logs of the servers. Open the terminal of each added server, log on to the gateway container, and then run the `tail -f /home/admin/alisatasknode/logs/heartbeat.log` command. If the logs are refreshed every 5 seconds, the heartbeat service is run as expected. ii. Query the database information and check whether the servers are online. Log on to the **Apsara Infrastructure Management** console. Go to the **Cluster Details** page of the desired base cluster, click the **Cluster Resource** tab, set the Type parameter to **db**, and then find the **base-biz-alisa** service. Click **Details** in the
**Application Result** column to view the database connection information.
Connect to the database by using a MySQL command, and run the `select * from` alisa_node; command. The information about all servers that run the base-biz-gateway service appears. Check the values of the live and active_type parameters for each added server. If both the values are 1, the server is online.

### 4.4 Scale in the base-biz-gateway cluster

**cluster**

**Prerequisite**

If a server in the base-biz-gateway cluster fails, you can repair and restart the server to redeploy the server. If you want to remove a healthy server from the base-biz-gateway cluster, follow the instructions in this topic.

> **Note:** Before removing a healthy server, perform an on-site check to guarantee that the following conditions are met:
> No business applications are running on the server.
> The hostname of the server is correct.

**Procedure**

Perform checks before the scale-in
1. Perform an on-site check.
Collect the detailed information of the server to be removed and the cluster that contains the server.
2. Make sure that the value of the scalable tag is true for the service resource group (SRG) of
the server to be removed. If the value is false, change it to true and submit a rolling task. Log on to Apsara Infrastructure Management. In the left-side navigation pane, choose
**BasicCluster > Cluster Configuration File > machine_group.conf**. In this file, verify
that the value of the scalable tag is true for the SRG of the server to be removed. perations Stop the base-biz-gateway service
1. Log on to the server to be removed and run the ps -ef|grep gateway command to obtain
the container ID of the base-biz-gateway service.
2. Run the `docker exec -it [container ID] bash` command to enter the container.
3. Switch to the admin account and run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/servervtl stop  command.
```

4. Run the ps -ef|grep java command to check whether any process is running on the
server. If any process is running, run the `kill -9 [process ID]` command to terminate the process.
5. Delete the program directories from the server.
Clean up the disks of the server. Skip this step if you want to clone the server.

```
#rm -rf /home/admin/*
#rm -rf /opt/taobao/tbdpapp/
```

Move servers from the base-biz-gateway cluster to the default cluster in Apsara Infrastructure Management
1. Log on to the ops1 server and run the following commands to remove a server from the
base-biz-gateway cluster:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_dest. nf clt2.conf (After you run this command, if a message appears indicating that a symb olic link already exists, proceed with the next command.) ./tianji_ops_tool.py contract_nc -c [clusterName] -l [machineList] --config tianji_clt.conf -s [SRGname]
```

The parameters are described as follows: -c: Required. Set this parameter to the name of the base cluster to be scaled in. To obtain the cluster name, choose Operations > Cluster Operations in the top navigation bar and select base from the Project drop-down list. -l: Required. Set this parameter to the hostname of the server to be removed. Separate multiple hostnames with commas (,). -s: Required. Set this parameter to the SRG name of the server to be removed. Find the machine_group.conf file among the configuration files of the base cluster. In this file, find the SRG of the server to be removed. -config: Required. Set this parameter to tianji_clt.conf.
2. After you run the preceding command, check whether the scale-in operation succeeds in
Apsara Infrastructure Management. Go to the Cluster Operation and Maintenance Center of the base cluster.
3. On the **Cluster Operation and Maintenance Center** page, check the number of servers
that are being removed.
4. Click the number next to Machine: in: to identify the status of the servers that are being
removed. If the scale-in operation succeeds, the number of servers that are being removed decreases to zero. Otherwise, check the server status on this page. perations You can follow the preceding steps to scale in a node cluster by moving servers to the default cluster in Apsara Infrastructure Management. The following section describes how to remove servers from Apsara Infrastructure Management. Remove servers from Apsara Infrastructure Management
1. In the top navigation bar, choose **Operations > Machine Operations**.
2. On the Machine Operations page that appears, click **Machine Online/Offline** in the upper-
right corner.
3. In the Machine Online/Offline dialog box that appears, click Remove Machine.
4. On the Remove Machine tab, search for the server to be removed by hostname in the left-
side Enter Machine List section. You can only remove servers in the default cluster.
5. Confirm the information of the server and click **Clear Machines** to remove it.
Verify the server removal result
1. Check whether the server is moved to the default cluster in Apsara Infrastructure
Management. In the top navigation bar, choose **Operations > Machine Operations**. On the Machine Operations page that appears, search for the target server by hostname and check whether it is in the default cluster.
2. Check whether the server is removed from the default cluster.
In the top navigation bar, choose **Operations > Machine Operations**. On the Machine Operations page that appears, search for the server by hostname. If you cannot find the server in the search results, the server is removed.
3. To check whether the server is removed from the default cluster, run the following
command on the ops1 server to call the GetMachineInfo operation:

```bash
curl http://127.0.0.1:7070/api/v5/GetMachineInfo?hostname=$hostname
```

### 4.5 Restart the base-biz-tenant service

**service**

This topic describes how to go to the Service Details page and restart the base-biz-tenant service.

**Go to the Service Details page**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **base-baseBizApp** service. The **Service Details** page appears.

**Restart the base-biz-tenant service**

1. On the Service Details page, click the **base-baseBizApp.BaseBizTenant** service.
You can also enter BaseBizTenant in the **Server Role** field to search for the target service. perations
2. Click the name of the target server. The Machine Details page appears.
3. Click **Terminal** in the upper-right corner of the page.
4. In the left-side navigation pane of the **TerminalService** page, click the server name. The
configuration tab appears on the right-side of the page.
5. Enter docker ps|grep tenant and press Enter to view the ID of the server.
6. Enter `docker exec -it yourID bash` and press Enter to enter the corresponding container.

> **Note:** The yourID parameter specifies the container ID.

7. Enter `su - admin` and press Enter to switch to the admin user.
8. Enter `/home/admin/base-biz-tenant/bin/jbossctl restart` and press Enter to restart the
base-biz-tenant service. perations When the **OK** and **NGINX start Done** information appears, the base-biz-tenant service is restarted.

### 4.6 Restart the Redis services

This topic describes how to go to the Service Details page and restart the Redis services.

**Go to the Service Details page**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **base-baseBizApp** service. The **Service Details** page appears.

**Restart the Redis services**

1. On the Service Details page, click the **base-baseBizApp.Redis1#** service.
Redis services include Redis1 and redis2. This topic uses Redis1 as an example. You can also enter Redis in the **Server Role** field to search for the target service.
2. Click the name of the target server. The Machine Details page appears.
3. Click **Terminal** in the upper-right corner of the page.
4. In the left-side navigation pane of the **TerminalService** page, click the server name. The
configuration tab appears on the right-side of the page.
5. Enter docker ps|grep redis and press Enter to view the ID of the server.
6. Enter `docker exec -it yourID bash` and press Enter to enter the corresponding container.

> **Note:** The yourID parameter specifies the container ID.

perations
7. Enter the following statements and press Enter to restart the Redis service:

```
/etc/init.d/redis restart /etc/init.d/redis-sentinel restart
```

### 4.7 Restart the base-biz-dmc service

**service**

This topic describes how to go to the Service Details page and restart the base-biz-dmc service.

**Go to the Service Details page**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **base-baseBizApp** service. The **Service Details** page appears.

**Restart the base-biz-dmc service**

1. On the Service Details page, click the **base-baseBizApp.BaseBizDmc** service.
You can also enter BaseBizDmc in the **Server Role** field to search for the target service. perations
2. Click the name of the target server. The Machine Details page appears.
3. In the left-side navigation pane of the **TerminalService** page, click the server name. The
configuration tab appears on the right-side of the page.
4. Enter docker ps|grep dmc and press Enter to view the ID of the server.
5. Enter `docker exec -it yourID bash` and press Enter to enter the corresponding container.

> **Note:** The yourID parameter specifies the container ID.

6. Enter `su - admin` and press Enter to switch to the admin user.
7. Enter `/home/admin/base-biz-dmc/bin/jbossctl restart` and press Enter to restart the
base-biz-dmc service. perations When the **OK** and **NGINX start Done** information appears, the base-biz-dmc service is restarted.

### 4.8 Restart the base-biz-alisa service

**service**

This topic describes how to go to the Service Details page and restart the base-biz-alisa service.

**Go to the Service Details page**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **base-baseBizApp** service. The **Service Details** page appears.

**Restart the base-biz-alisa service**

1. On the Service Details page, click the **base-baseBizApp.BaseBizAlisa** service.
You can also enter BaseBizAlisa in the **Server Role** field to search for the target service. perations
2. Click the name of the target server. The Machine Details page appears.
3. Click **Terminal** in the upper-right corner of the page.
4. In the left-side navigation pane of the **TerminalService** page, click the server name. The
configuration tab appears on the right-side of the page.
5. Enter docker ps|grep alisa and press Enter to view the ID of the server.
6. Enter `docker exec -it yourID bash` and press Enter to enter the corresponding container.

> **Note:** The yourID parameter specifies the container ID.

7. Enter `su - admin` and press Enter to switch to the admin user.
8. Enter `/home/admin/base-biz-alisa/bin/jbossctl restart` and press Enter to restart the
base-biz-alisa service. When the **OK** and **NGINX start Done** information appears, the base-biz-alisa service is started. perations

### 4.9 Restart the base-biz-phoenix service

**service**

This topic describes how to go to the Service Details page and restart the base-biz-phoenix service.

**Go to the Service Details page**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
5. Click the **base-baseBizApp** service. The **Service Details** page appears.

**Restart the base-biz-phoenix service**

1. On the Service Details page, click the **base-baseBizApp.BaseBizPhoenix** service.
You can also enter BaseBizPhoenix in the **Server Role** field to search for the target service. perations
2. Click the name of the target server. The Machine Details page appears.
3. Click **Terminal** in the upper-right corner of the page.
4. In the left-side navigation pane of the **TerminalService** page, click the server name. The
configuration tab appears on the right-side of the page.
5. Enter docker ps|grep phoenix and press Enter to view the ID of the server.
6. Enter `docker exec -it yourID bash` and press Enter to enter the corresponding container.

> **Note:** The yourID parameter specifies the container ID.

7. Enter `su - admin` and press Enter to switch to the admin user.
8. Enter `/home/admin/base-biz-phoenix/bin/jbossctl restart` and press Enter to restart the
base-biz-phoenix service. When the **OK** and **NGINX start Done** information appears, the base-biz-phoenix service is started.

### 4.10 Restart the base-biz-gateway service

**service**

This topic describes how to go to the Service Details page and restart the base-biz-gateway service.

**Go to the Service Details page**

1. Log on to Apsara Infrastructure Management.
2. In the left-side navigation pane, choose **Operations > Cluster Operations**.
3. On the page that appears, select **base** from the **Project** drop-down list to filter clusters.
4. Click the name of the target cluster. The **Cluster Details** page appears.
perations
5. Click the **base-baseBizApp** service. The **Service Details** page appears.

**Restart the base-biz-gateway service**

1. On the Service Details page, click the **base-baseBizApp.BaseBizCdpGateway** service.
You can also enter BaseBizCdpGateway in the **Server Role** field to search for the target service.
2. Click the name of the target server. The Machine Details page appears.
3. Click **Terminal** in the upper-right corner of the page.
4. In the left-side navigation pane of the **TerminalService** page, click the server name. The
configuration tab appears on the right-side of the page.
5. Enter docker ps|grep gateway and press Enter to view the ID of the server.
6. Enter `docker exec -it yourID bash` and press Enter to enter the corresponding container.

> **Note:** The yourID parameter specifies the container ID.

7. Enter `su - admin` and press Enter to switch to the admin user.
8. Enter `/home/admin/alisatasknode/target/alisatasknode/bin/serverctl restart` and press
Enter to restart the base-biz-gateway service.

### 4.11 Restart DataWorks Data Service

**Service**

**Procedure**

1. In the ApsaraInfrastructureManagement console, search for dataworks-dataservice on the S
tab.
2. Hover over the vertical dots next to BasicCluster, and then click Operations to open the
Operations page to view the details of dataworks-dataservice. perations
3. Click the service instance name to open Service Instance Dashboard, and then find Service
Role List.
4. If you want to restart the server, select BaseBizDataServiceServer#. If you want to restart
the Web application, select BaseBizDataServiceWeb#. Hover over the vertical dots next to the service name, and then click **Details** to open the Service Role Dashboard page, and then find the virtual machine in the Server Information area.
5. Open the terminal window of the VM host, and run the docker ps|grep dataservice
command to find the container ID.

| docker exec -it [container ID] bash |   | command to enter the container. |
|---|---|---|
|   | /home/admin/data-service-web/bin/jbossctl |   |

`restart` command to restart the service. If you are restarting the server, run the `/home/admin/data-service-server/bin/jbossctl` `restart` command.
8. After you run the command, if the status is **OK** and the command output displays [ OK] --
SUCCESS at the end, the dataservice service is restarted successfully.

### 4.12 Restart base-biz-gateway

**Procedure**

1. In the Apsara Infrastructure Management console, select base from the project drop-down
list and then select BasicCluster from the search result.
2. On the Service tab in the lower part of the left-side navigation pane, double-click base-
baseBizApp, double-click BaseBizCdpGateway, and then the host that runs the service appears.
3. Open the terminal window of the host, and run the docker ps|grep gateway command to
find the container ID.
4. Run the `docker exec -it [container ID] bash` command to enter the container.
5. Switch to the admin account, and run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/serverctl restart  command to
```

restart the service.
6. After the service is restarted, run the ps -ef|grep java command to check whether the
process is started.

> **Note:** This method can only be used where the gateway service is deployed in a Docker container.

**For the service deployed on a physical server**

If the service is deployed on a physical server, use the following method to restart the service.
1. In the Apsara Infrastructure Management console, open the Dashboard page of
BasicCluster. In the cluster resource list, find and right-click the base-biz-alisa service that has a type of db, and then click Show More. The database logon address, username, and password are displayed.
2. Run the select * from alisa_node; command in the database to view the information of
all gateway servers, and use the node IP address to find and maintain the gateway server.
3. In the terminal window of the server, switch to the admin account, and then run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/serverctl restart  command.
```

perations

### 4.13 Configure a resource group in a multi-region environment

**in a multi-region environment**

In a multi-region environment, nodes in all regions are run on the resource group named sys_default in the central region by default. This is the cause of resource preemption and node backlog. To resolve the issues, you must isolate resources and enable level-1 scheduling nodes in your region to run on your own resource groups.

**Prerequisites**

Idle Elastic Compute Service (ECS) instance resources are available in a region rather than the central region. You can view the idle resources in the Apsara Infrastructure Management Framework console. Resource groups are created in DataWorks and resources are isolated. A custom resource group is specified as the default resource group in your workspace. Historical nodes that are run on the original default resource group are migrated to the new resource group. This is a high-risk operation.

**Create a resource group**

1. Go to the Schedule Resources page in DataWorks.
i. Log on to the DataWorks console. ii. Click the icon in the upper-left corner and choose **All Products > Project**
**Management**.
iii. In the left-side navigation pane, click **Schedule Resources**.
2. On the **Schedule Resources** page, click **Add scheduling resources** in the upper-right
corner.
3. In the **Add scheduling resources** dialog box, set the **Resource Name** and **Belonging**
**workspace** parameters.
In this example, the resource name is **region_test**. The resource group belongs to a tenant that is a level-1 department. All workspaces that are created by the tenant can use this resource group, whereas other tenants need to create their own resource groups. After a resource group is created, a cluster that corresponds to the resource group is also created. In the background database, you can view the resource group in the **alisa_group** table and view the cluster in the **alisa_cluster** table.
4. Click **Confirm**.
After you create the resource group, you can log on to the dpbizalisa background database to view detailed information about the resource group and cluster.

```
select group_name,group_display_name,cluster_name,max_slot where group_display_name='xxxx'; select cluster_name,username,password from alisa_cluster where cluster_name ='xxxx'; // max_slot: the number of slots that are assigned to the current resource group. The number is determined based on actual resources and requirements. You must set the num ber of slots to a proper value. // group_display_name: the name of the custom resource group. // cluster_name: the name of the cluster that corresponds to the custom resource grou
```

`p.`

**Migrate ECS instances to a new cluster**

1. To migrate an ECS instance, run the following command:
perations

```
update alisa_node set cluster_name='xxxxxx' where node_name='${hostname}';
```

2. To set the number of slots in the resource group to a proper value, run the following
command:

```
update alisa_group set max_slot = xxxx where group_display_name='region_test';
```

3. Restart the base-biz-alisa service. For more information, see Restart the base-biz-alisa
service.

> **Note:** Both base-biz-alisa services need to be restarted. After one base-biz-alisa service is restarted, you can restart the other.

**Specify the custom resource group as the default resource**

**group in your workspace**

1. Log on to the dwphoenix background database to view data.

```
select resource_group_id,name,identifier,is_default,project_env from phoenix_resgroup where name = 'region_test'; // resource_group_id: the ID of the resource group in the phoenix database. // name: the name of the resource group. // identifier: the name of the resource group in the alisa database. // project_env: the production environment or the development environment. select * from phoenix_app_resgroup where app_id=xxxx; // app_id: the ID of the project. The app_id parameter is equivalent to the project_i d parameter that is described in other topics.
```

2. Specify a new resource group as the default resource group in your workspace.

```
create table phoenix_app_resgroup_20200108_bak as select * from phoenix_app_resgroup; // Back up the table. update phoenix_app_resgroup set is_default=1 where is_default=0 and app_id=xxxx; update phoenix_app_resgroup set is_default=0 where app_id=xxxx and resource_group_id=1; select * from phoenix_app_resgroup where app_id=xxxx; // View data again after the ch ange.
```

> **Note:** After the change, one workspace has only two data entries whose is_default value is 1. If the preceding result is not displayed, the change is invalid. You must check the operations you have performed.
> The resource group belongs to a tenant so that you must change the default resource group for all workspaces that are created by the tenant.

**Change the resource group for multiple nodes at a time**

You can change the resource group for multiple nodes at a time on the Operation Center page. If a large number of nodes exist, you must perform the change operation multiple times on the page until the resource group is changed for all the nodes. If you do not want to change the resource group in that way, you can change the resource group for all the nodes at a time in the scheduled database. However, this is a high-risk operation. To change the resource group in the database, you must perform the operations based on your business requirements. You must write the code based on the data in the current environment by following the template. In this example, the resource group for nodes in the datam4 workspace is changed to the resource group named region_test in the following way: perations
1. Log on to the dwphoenix database that corresponds to the base-biz-phoenix service.
2. Query the ID of the resource group named sys_default. The obtained value is used as the
default ID.

```
select resource_group_id from phoenix_resgroup where name='Default Group';
```

3. Query the ID of the resource group named region_test. The obtained value is used as the
region_test_id value.

```
select resource_group_id from phoenix_resgroup where name='region_test';
```

4. Query the ID of the required workspace. The obtained value is used as the app_id value.

```
select app_id from phoenix_app_config where name="datam4";
```

5. Change the resource group for historical nodes in the workspace that you want to change
to the new resource group named region_test.

```
create table phoenix_node_def_20200108_bak as select * from phoenix_node_def; // Back up the table. update phoenix_node_def set resgroup_id={region_test_id} where resource_group_id={Def ault ID} and app_id={app_id};
```

This way, the resource group for historical nodes in the datam4 workspace is changed to the resource group named region_test. After the resource group is changed, test whether all the historical nodes can be run as expected.

### 4.14 Configure a resource group for Data Integration in a multi-region environment

**for Data Integration in a multi-**

**region environment**

This topic describes how to configure a resource group for Data Integration in a multi-region environment.

**Procedure**

1. On the Data Integration page in DataWorks, create a custom resource group.
perations This custom resource group must be real and can be used. In this example, you can specify the Elastic Compute Service (ECS) instance on which the **region_group** custom resource group is hosted as the default ECS instance to run nodes. i. Log on to the DataWorks console. ii. Click the icon in the upper-left corner and choose **All Products > Data Aggregation**
**> Data Integration**.
iii. In the left-side navigation pane, click **Custom Resource Group**. iv. Click **Add Resource Group** in the upper-right corner.
2. In the **Add Resource Group** wizard, perform the following steps:
i. In the **Create Resource Group** step, set the **Resource Group Name** parameter.

> **Note:** The name can contain letters, digits, and underscores (_), and must start with a letter.

ii. Click **Next**. iii. In the **Add Server** step, set the parameters as required. iv. Click **Next**. v. Perform the steps that are described in the **Install Agent** step.

> **Note:** If an error occurs when you run the `install.sh` command or you need to run it again, run the rm –rf install.sh command in the same directory as the
> `install.sh` command to delete the generated file. Then, run the `install.sh` command again.
> The commands to run during the installation and initialization process differ for each user. Run relevant commands based on the instructions on the initialization interface.

vi. Click **Next**. vii. In the **Test Connection** step, click **Refresh** and check the status of the ECS instance. viii. Click **Complete**. Resource groups that you have created on the Data Integration page can be used only in workspaces to which they belong. If you create a resource group in Workspace A, this resource group cannot be used in Workspace B. If you need to use a resource group in Workspace B, perform the preceding steps to create one in Workspace B.
3. View the newly created resource group in the alisa database.

```
select * from alisa_group where group_display_name='region_group'\G;
```

perations
4. Create an alisa cluster.
To deploy services in a new region, you must first create an alisa cluster. You can find the dpbizalisa database and execute the following SQL statements in this database:

```
insert ignore into alisa_cluster(
 cluster_name,
 cluster_display_name,
 username,
 password,
 create_time,
 last_modify_time
```

`)`

```
 values(
 'sys_region_cdp_${regionId}',
 'sys_region_cdp_${regionId}',
 'private_cluster',
 'tyn3n71c2oyhah447m6fnfuq',
 now(),
 now()
```

); Replace **${regionId}** in the code with an actual value. You can log on to the Apsara Infrastructure Management console and go to the **Cluster Configuration** tab to view the cluster file.
5. Migrate the ECS instance that you have bound to the custom resource group to this cluster.

```
update alisa_node set cluster_name='sys_region_cdp_${regionId}' where node_name='ECS instance name';
```

> **Note:** You must check the name of the ECS instance in the current region.

6. Mount the cluster that is created in this region to the resource group.

```
update alisa_group set cluster_name='sys_region_cdp_${regionId}' where group_name='4be29b9408f24bd4be1566131f97afb4';
```

In the code, **group_name** indicates the resource group name that is specified in Step 2.
7. Log on to the Apsara Infrastructure Management console and restart the BaseBizAlisa
service. perations
8. On the configuration tab of a sync node, select the name of the required custom resource
group, and save and commit the node. The preceding steps describe how to create a resource group in a region for the first time. If you need to create resource groups for multiple workspaces, repeat steps 1, 2, 3, 6, and 7 to create resource groups as required. To perform the rollback operation, run the following command:

```
update alisa_group set cluster_name='4be2***' where group_name='4be2***';
```

> **Note:** **group_name** and **cluster_name** indicate the name and cluster name of the custom resource group.

## 5 Common issues and solutions

**solutions**

### 5.1 Nodes remain in the Pending (Resources) state

**(Resources) state**

**Symptom**

After you log on to the DataWorks console and click **Operation Center** in the upper-right corner of the console, the following issue occurs on the **Dashboard** page that appears: The instances of many recurring nodes remain in the Pending (Resources) state for a long period of time.

**Causes**

The issue may occur due to any one of the following four reasons: A gateway server is overloaded or offline and its status value is -1 in the database. The slots that handle concurrent jobs are fully occupied. The disk on a gateway server is full. The system time of servers in the base cluster is out of sync with the time of the Network Time Protocol (NTP) server.

**Solutions**

To resolve this issue, follow these steps: Check the status of a gateway server in the database. i. Log on to the database that hosts the base-biz-alisa service. In Apsara Stack V3, you can find the database endpoint from the resource list of the base cluster in Apsara Infrastructure Management. ii. Run the select * from alisa_node; command to check the values of the active_type and live fields. If the value of the live field is -1, the server is offline. If the value of the active_type field is -1, the server is overloaded.

> **Note:** In either case, use SSH to connect to the gateway server and then check the server load and heartbeat.
> Run the `tail -f/home/admin/alisatasknode/logs/heartbeat.log` command to check the heartbeat of the gateway server.
> If the heartbeat log is updated every five seconds, the heartbeat is normal. Otherwise, check the configuration files for an error.
> Run the top command to display the load of the gateway server.
> The status of the server becomes -1 in the database as a result of the high load. In this case, check whether the CPU and memory are overloaded. You can find out the high-load processes in the output of the top command.
> You can run the ps -ef|greppid command to view processes of the specified node and identify which process causes the high load. To terminate a process, run the `kill -9 [process ID]` command. After the load drops, check whether the status of the server resumes to 1.

Check whether the slots that handle concurrent jobs are fully occupied. Log on to the database that hosts the base-biz-alisa service and run the following statements:

```
select group_name,max_slot from alisa_group where group_name like '%default%'; select exec_target,sum(slot) from alisa_task where status=2 group by exec_target;
```

Compare the query results of the two statements. The first statement returns the maximum number of slots that can be assigned in each resource group. The second statement returns the number of slots that are occupied in each resource group. If the query results of the two statements are the same or almost the same, all resource groups run out of slots. In this case, if a large number of nodes are running, the subsequent nodes do not run until the preceding nodes are completed. Run the following statement to list the top 10 nodes that require the longest runtime:

```
select task_id,gateway,slot,create_time from alisa_task where status=2 and create_tim e>current_time order by create_time desc limit 10;
```

Log on to the gateway server and run the ps -ef|grep task_id command.

> **Note:** Replace task_id in this command with one of the node IDs that are returned by the preceding SELECT statement. You can obtain the node name from the command output.

Then, you can troubleshoot the node. If required, run the `kill -9` command to terminate the node and release resources immediately. Otherwise, new nodes can start only after the existing nodes are completed. Check whether the disk on a gateway server is full. Log on to the gateway server and run the `df -h` command to check whether the disk attached to /home/admin is full. If the disk is full, run the `du-sh` command to identify the files in the /home/admin directory that consume a large amount of space. You can manually remove some large log files from the /home/admin/alisatasknode/taskinfo/ directory. Check the system time of servers in the base cluster against the time of the NTP server. i. Log on to the database that hosts the base-biz-alisa service and run the select now(); command to view the current time of the database. ii. Check the system time of servers in the base cluster against the time of the database. iii. Run the date command on the servers to check whether the system time of each server is synchronized with the time of the database. If the time difference is greater than 30 seconds, the base-biz-alisa service may fail. In this case, synchronize the system time of servers in the base cluster with the time of the NTP server.

> **Note:** In Apsara Stack V3, you can find the servers of the base cluster in the service list in the Apsara Infrastructure Management console and follow the proceeding steps to resolve the issue.

Rename the phoenix folder to change it to a .bak file and restart the base-biz-alisa service. If the issue persists after you perform the preceding steps, run the following command on the gateway server:

```
cd /home/admin/alisatasknode/taskinfo/prevDay/phoenix/
```

> **Note:** Replace prevDay in this command with the date of the previous day in the format YYYYMMDD, for example, 20180306.

In this directory, run the `mkdir test` command. If the error message "Cannot create directory too many links" appears, the issue occurs because the number of subdirectories in the directory has reached the maximum and you cannot create more subdirectories. To resolve this issue, follow these steps: i. Rename the /home/admin/alisatasknode/taskinfo/20180306/phoenix directory as /home/admin/alisatasknode/taskinfo/20180306/phoenix.bak. ii. Run the following command to restart the base-biz-alisa service:

```python
sudo su admin -c "/home/admin/alisatasknode/target/alisatasknode/bin/serverctlrestart"
```

> **Note:** This is a rare problem which tends to occur when a gateway server uses the third extended (ext3) file system.

### 5.2 An out-of-memory (OOM) error occurs when synchronizing data from an Oracle database

**occurs when synchronizing data**

**from an Oracle database**

**Description**

During the data synchronization from an Oracle database to MaxCompute or other platforms, an `java.lang.OutOfMemoryError: Java heap space` error is displayed in the task log.

**Cause**

This issue is often caused by a large volume of data in the data synchronization task, which causes a JVM OOM error.

**Solution**

Set a low fetchsize value. Use MySQL statements to connect to the cdp database, and modify the template configuration of the Oracle reader plug-in by changing the fetchsize value from 1024 to 128. Run the following statement:

```
update t_plugin_template set template=replace(template,'1024','128') where name='oracle' and type='reader';
```

Rerun the task after the fetchsize value is changed. To reset the fetchsize value, run the following statement:

```
update t_plugin_template set template=replace(template,'128','1024') where name='oracle' and type='reader';
```

### 5.3 A task does not run at the specified time

**specified time**

**Description**

A periodic task does not run, and no data is displayed in the overview.

**Solution**

1. Check whether periodic scheduling is enabled in this workspace.
On the Workspace Configuration page in Workspace Management, ensure that the periodic scheduling is enabled.
2. If it is enabled, check whether the phoenix service runs properly.
Connect to the phoenix database and run the following statement.

```
select to_char(to_timestamp(next_fire_time/1000),'YYYY-MM-DDHH24:MI:SS') from qrtz_tr iggers;
```

If the output contains 00:00:00 of the next day, the service is running properly. If not, you need to check whether the time of the two base-biz-phoenix containers are different. If the two containers have the same system time, you need to switch to the admin account and run the `/home/admin/base-biz-phoenix/bin/jbossctl restart` command to restart the phoenix service, and then check the time again.
3. After the time is corrected, you can run tasks that failed to run on the previous day.
Run the following command in either of the phoenix containers. Note that you can run this command only once.

```bash
curl -v -H "Accept:application/json"-H "Content-type: application/json"-X POST -d'{"o pCode":11,"opSEQ":12345,"opUser":"067605","name":"SYSTEM","bizdate":"2017-04-2300:00: 00","gmtdate":"2017-04-2400:00:00"}' http://localhost:7001/engine/2.0/flow/create_unified_daily
```

> **Note:** bizdate refers to the previous day, and gmtdate refers to the current day. Modify the command if needed before running it.

### 5.4 The test service of base is not in the desired status

**in the desired status**

1. On the S tab, select base-baseBizApp.
2. Select the cluster in the lower part of the left-side navigation pane, and then open the
dashboard.
3. View the report of service monitoring.
Analyze the causes of the failed test based on the log.

### 5.5 The Data Management page does not display the number of tables and the usage of tables

**does not display the number of**

**tables and the usage of tables**

**Description**

The Data Management page is blank.

**Solution**

1. Log on to the Apsara Infrastructure Management console, select odps from the project
drop-down list, and then open the HybridOdpsCluster dashboard page.
2. Find the accesskey type base_admin service in the Cluster Resource area.
3. Right-click the result field, and click Show More to view the username and the password.
4. Log on to DataWorks.

> **Note:** To log on to DataWorks, enter the domain name of base in the browser. By default, the domain name is ide.[your Apsara Stack second-level domain].

5. Select the base_meta workspace, and go to Administration.
Rerun all failed tasks, and then check whether the Data Management page is displayed properly. If the task fails again, contact Alibaba Cloud Customer Support.

### 5.6 Logs are not automatically cleaned up

**cleaned up**

**Description**

Logs are not cleaned up automatically because of an error.

**Solution**

Follow the following steps to clean up the logs manually.
1. Establish a terminal session to the VM.
2. Run the following command to clean up real-time analysis logs.

```
find /home/admin/cai/logs/cronolog/ -mtime +7 -type f -exec rm –rf {} \; find /home/admin/dw-realtime-analysis/logs/ -mtime +7 -type f -exec rm -rf {} \;
```

3. Run the following command to clean up base-biz-diide application logs.

```
find /home/admin/cai/logs/cronolog/ -mtime +7 -type f -exec rm –rf {} \; find /home/admin/base-biz-diide/logs/ -mtime +7 -type f -exec rm -rf {} \;
```

4. Run the following command to clean up base-biz-cdp application logs.

```
find /home/admin/cai/logs/cronolog/ -mtime +7 -type f -exec rm –rf {} \; find /home/admin/base-biz-cdp/logs/ -mtime +7 -type f -exec rm -rf {} \;
```

### 5.7 The real-time analysis service is not in the desired status

**is not in the desired status**

**Description**

The real-time analysis service is not in the desired status.

**Solution**

1. On the S tab, select dataworks-realtime.
2. Open the dashboard page of the cluster in the lower part of the left-side navigation pane.
3. View the report of service monitoring.
View the log to find out what caused the failed test.
