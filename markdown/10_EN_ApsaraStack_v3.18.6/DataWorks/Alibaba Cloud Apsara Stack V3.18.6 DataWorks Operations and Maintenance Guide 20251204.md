---
title: "DataWorks Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20251204"
pdf_pages: 137
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 DataWorks Operations and Maintenance Guide 20251204.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/DataWorks/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20DataWorks%20Operations%20and%20Maintenance%20Guide%2020251204.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# DataWorks Operations and Maintenance Guide

## Basic concepts and

**structure**

### What is DataWorks?

DataWorks, formerly known as Big Data Development Suite, is a one-stop platform for intelligent big data development and governance. It is built on compute engines such as MaxCompute and E-MapReduce (EMR). DataWorks provides a comprehensive suite of tools for data integration, development, governance, services, quality control, and security. DataWorks provides a one-stop solution for the entire data lifecycle, from data collection and presentation to analysis and application development. It supports offline processing, analysis, and data mining of massive amounts of data. DataWorks also integrates core data processes, such as data integration, data development, production operations and maintenance (O&M), real-time analysis, asset management, data quality, data security, and data sharing. Additionally, DataWorks provides DataService Studio and an online development platform for Machine Learning Platform for Artificial Intelligence (PAI). In 2018, the analytics firm Forrester ranked the DataWorks and MaxCompute solution second in the world among cloud data warehouses. It was the only Chinese product to be included in the evaluation. DataWorks V2.0 builds on V1.0 by adding business flows and components. This version improves the data development system by supporting dual-project development, isolating development and production environments, enforcing development standards, and reducing code errors. Data asset Data analysis Data Quality Data security map reports

**Comprehensive**

Asset Metadata Intelligent Resource discovery/Asset parsing/Data monitoring optimization (beta)

**data**

**governance**

management exploration XStudio: Cloud-based IDE with plug-ins for various engines

**Intelligent**

Interactive query Graph computing Data service development development (beta) development

**data**

**Glo**

**development**

Real-time data Offline data Machine learning

**intell**

development development development (PAI)

**big d**

**Unified task**

Cross-engine Cross-cycle Cross-region Node context Scheduling flow

**platf**

**scheduling**

scheduling scheduling parameter logic control hybrid scheduling passing Disparate data Global Metadata

**Unified**

Metadata Metadata

**Metadata**

acquisition and warehouse Service source

**Center**

management construction

**Global data**

Concurrency Batch Incremental Real-time Dirty data

**integration**

synchronization synchronization synchronization monitoring control (beta) MaxComputeProprietary E-MapReduceOpen- RealtimeComputeReal- GraphComputeGraph HologresInteractive big data computing time computing computing and analysis source big data

**Compute**

service computing service analysis

**and storage**

**engines**

OSS HDFS DB IoT

### Benefits

This topic describes the benefits of DataWorks. Powerful computing capabilities DataWorks integrates with compute engines that can process large amounts of data. DataWorks supports join operations for trillions of data records, millions of concurrent jobs, and petabytes (PB) of I/O throughput per day. The offline scheduling system can run millions of concurrent jobs. You can configure rules and alerts to monitor the running statuses of nodes in real time. DataWorks provides efficient and easy-to-use SQL and MapReduce engines, and supports most standard SQL syntax. MaxCompute protects user data from loss, breach, or theft by using multi-layer data storage and access security mechanisms, including triplicate backups, read/write request authentication, application sandboxes, and system sandboxes. End-to-end platform DataWorks provides the graphical user interface (GUI) and allows multiple users to collaborate on a workspace. DataWorks integrates all processes from data integration, processing, management, and monitoring to output. You can create and edit workflows in a visual manner by using the workflow designer. DataWorks provides a collaborative development environment. You can create and assign roles for varying nodes, such as development, online scheduling, maintenance, and data permission management, without locally processing data and nodes. Integration of heterogeneous data stores DataWorks supports batch synchronization of data among heterogeneous data stores at custom intervals in minutes, days, hours, weeks, or months. More than 400 pairs of heterogeneous data stores are supported. Web-based software DataWorks is an out-of-the-box service. You can use it on the Internet or an internal network without the need for installation and deployment. Multitenancy Data is isolated among different tenants. Each tenant controls permissions, processes data, allocates resources, and manages members in a unified and independent manner. Intelligent monitoring and alerting By setting monitoring thresholds, you can control the entire process of all nodes as well as monitor the running status of each node. Easy-to-use SQL editor The SQL editor supports automatic code and metadata completion, code formatting and folding, and pre-compilation. It offers two editor themes. These features ensure a good user experience. Comprehensive data quality monitoring DataWorks allows you to control the quality of data in heterogeneous data stores, offline data, and real-time data. You can check data quality, configure alert notifications, and manage connections. Convenient API development and management The DataService Studio service of DataWorks interacts with API Gateway. This makes it easy for you to develop and publish APIs for data sharing. Secure data sharing DataWorks enables you to de-identify sensitive data before you share it with other tenants, which ensures the security of your big data assets and maximizes their value.

### Introduction to Data

**Development**

This topic describes two common scenarios for Data Development.

**Scenario 1: Data synchronization and data analysis**

The following is a typical Data Development scenario:
1. Use DataWorks to collect data from various databases into MaxCompute.
2. Use DataWorks to send SQL, MR, or SHELL statements to MaxCompute for data analysis.
3. Use DataWorks to synchronize the analysis results from MaxCompute back to the original
databases. DataX data synchronization Data RDS collection SQL/MR/Shell Data ODPSCompu and storage analysis Design Oracle workflow SQL/MR/Shell Scheduled task ads ...

**Note**

Base is an alternative name for DataWorks that appears in some technical contexts.

**Scenario 2: Data synchronization**

DataWorks supports data synchronization between different types of databases. For scenarios that require only data synchronization, DataWorks provides a simplified process. Data Oracle ads synchronization Data RDS Oracle synchronization Data Oracle ODPS synchronization

### DataWorks architecture

This topic describes the core architecture and components of DataWorks. BaseBizTenant (tenant Account management) management layer

| Application BaseBizCommonbase (IDE) layer |   |
|---|---|
| API BaseBizBaseapi (API) layer |   |
| Scheduling BaseBizPhoenix (scheduling control control) |   |
| layer |   |
| BaseBizAlisa (task resource management) Execution layer BaseBizGateway(execButaisoenBizGateway(exec node) node) |   |
| Compute MaxCompute engine |   |

The components in DataWorks are critical for submitting and executing your tasks. All O&M for the V3 environment is performed in **Apsara Infrastructure Management**. The following figure shows the modules that make up DataWorks. All DataWorks services are deployed in containers. The following figure shows the output after you log on to a host and run the `docker ps` command to view the containers where the services are deployed. Except for the gateway service, the internal structure of a single application is shown in the following figure. Domain name SLB Nginx Nginx Port Port

### Service directories

This topic describes the directory structure of each service.

**base-biz-gateway service**

The base-biz-gateway service receives and runs nodes from the DataWorks integrated development environment (IDE) and the scheduling system. Logs directory: stores the operational logs of the base-biz-gateway service. taskinfo directory: stores the code run by user nodes and the execution logs. target directory: the main directory of the base-biz-gateway service. This directory stores the service code, start script, stop script, and configuration files.

**base-biz-cdp service**

The base-biz-cdp service is used to synchronize data. Logs directory: stores the operational logs of the base-biz-cdp service. Conf directory: stores the configuration files of the base-biz-cdp service. Bin directory: stores the start script.

**Other services**

The base-biz-alisa service directory is used as an example. Logs directory: stores the operational logs of the base-biz-alisa service. Conf directory: stores the configuration files of the base-biz-alisa service. Bin directory: stores the start script.

## O&M by using Apsara Big

**Data Manager**

### Log on to the ABM console

This topic describes how to log on to the Apsara Big Data Manager (ABM) console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

**Note**

You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter the username and password.

**Note**

Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, click **Product**
**Operation**.
6. Choose **Big Data > Bigdata Manager** to go to the homepage of the ABM console.

### Monitoring

#### Health

In the Apsara Big Data Manager (ABM) console, the Degree of health page allows you to view the monitoring items of each big data service and the alerts of different levels of severity and check the monitoring items and alerts again after the alerts are handled.

**Procedure**

1. Log in to the ABM console.
After you log in to the **ABM** console, the **Instrument cluster** page appears by default. You can click the icon in the upper-left corner and select the big data service that you want to view.
2. In the top navigation bar, click **Monitoring**.
3. Click the **Degree of health** tab to view the health check result.
The Degree of health page displays the monitoring items, monitoring sources, severity level, and monitoring details. You can filter data based on your business requirements.

#### Reports

In the Apsara Big Data Manager (ABM) console, the Report page allows you to view the inspection results of each big data service.

**Procedure**

1. Log in to the ABM console.
After you log in to the **ABM** console, the **Instrument cluster** page appears by default. You can click the icon in the upper-left corner and select the big data service that you want to view.
2. In the top navigation bar, click **Monitoring**.
3. Click the **Report** tab to view the reports.
The Report page displays the following information about each report: ID, Report Name, Product, Template Name, Instance Type, Created By, and Created At. You can also view the details about each report.

### O&M

#### DataWorks O&M overview

This topic describes the DataWorks O&M features supported by Apsara Big Data Manager (ABM) and how to use the DataWorks O&M features.

**O&M modules**

ABM provides the service, cluster, and host O&M modules for DataWorks. The following table describes the modules.

| Module | Feature | Description |
|---|---|---|
| Service operation and maintenance > Data workshop | Overview | Displays the key O&M metrics, including service overview, service status, instance scheduling information, and slot usage. You can also view the trend chart of the total number of complete tasks. |
|   | Service role | Displays the service roles of DataWorks. |
|   | Slot | Displays information about slot usage in DataWorks and allows you to change the number of slots in resource groups and hosts. |
|   | Instance | Displays information about instances. |
|   | Project | Displays the projects of each tenant and allows you to change the default resource group of projects and nodes. |

|   | Business insights | Displays the number of tasks created or modified on the previous day by type and the corresponding trend chart. |
|---|---|---|
|   | Configuration | Allows you to modify the configurations of DataWorks service roles based on your business requirements. |
|   | Restart service alisa | Allows you to restart the base-biz-alisa service. |
|   | Scale-up for normal hosts and scale-down for normal hosts | Allows you to add or remove physical hosts in DataWorks. |
| Service operation and maintenance > Data Integration | Overview | Displays information in the following charts: Current operating status, Three-way dependency-total number of calls, Three-way dependency-call response time Max(ms), Tripartite Dependency-Call Failure Rate(ErrorRate), and Three-way dependency-QPS number of failed calls. |
|   | Instance | Displays the number of tasks of the current day by status and allows you to view the trend chart of multi-dimensional analysis on the tasks of the current day. |
|   | Historical analysis | Displays the trend charts of multi-dimensional analysis and time consumption analysis and the information about top tasks. |
| Cluster O&M | Overview | Displays the key metrics and health check results of a cluster in the Running Health, CPU, DISK, LOAD, MEMORY, and PACKAGE sections. |
|   | Health | Displays all monitoring metrics of a cluster. You can view the details of monitoring metrics, solutions to the alerts triggered by the monitoring metrics, and status of each monitoring metric. You can also log on to a host and manually perform checks on the host. |
| Host O&M | Overview | Displays the information about a host in the Machine Information, Machine Service Role Status, CPU, DISK, LOAD, MEMORY, and PACKAGE sections. |
|   | Server Role | Displays the information about service roles, including the cluster, service instance, and role name. |

**Work with DataWorks O&M features**

1. Log on to the ABM console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **Operation and maintenance**.
The **Overview** tab of the **Service operation and maintenance > Data workshop** page appears.

#### Service O&M

##### Data Warehouse

###### Service overview

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

**Note**

Slots are resources that can be used by DataWorks for instance scheduling.

**Total Number of Finished Tasks**

This section displays the trend chart of the total number of finished nodes. The trend chart displays the trend lines of the number of nodes finished yesterday, the number of nodes finished today, and the average number of nodes finished each day over time in different colors.

###### DataWorks service roles

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

###### Service slots

Slots are resources used to process tasks. Apsara Big Data Manager (ABM) allows you to view the slot information of DataWorks clusters, resource groups, and hosts. The information includes the maximum number of slots, the number of used slots, and slot usage. You can also migrate resource groups, modify the number of slots for resource groups or hosts, and modify the host status.

**Terms**

The resources required by Data Integration tasks are measured in data migration units (DMUs). A DMU contains a specific amount of resources, including CPU, memory, and network resources. It represents the minimum processing capability of a Data Integration task to synchronize data. Resources measured by DMU are allocated by slot. Each DMU occupies two slots.

**Entry**

1. Log on to the ABM console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**. The **Overview** tab of **Data**
**Warehouse** under **Services** appears.
4. Select a cluster from the drop-down list and click the **Slot** tab.

**Cluster slots**

Click the **Cluster** tab on the **Slot** tab. The **Cluster** tab displays the slot overview of all DataWorks clusters, including the total number of slots, the numbers of used slots and available slots, and slot usage. It also displays the cluster status. To view the slot details of a cluster, click the name of the cluster in the **Cluster Name** column. In the upper part of the cluster details page, you can view the numbers of gateways, resource groups, slots, used slots, frozen slots, and available slots, and the slot usage of the cluster. You can also view the trend chart of slot usage over time in the lower part of the page. The trend chart displays trend lines for the number of used slots, the maximum number of slots, and the number of available slots in different colors. You can click a metric name below the chart to display or hide the related trend line. A highlighted metric name indicates that the related trend line is displayed, whereas a dimmed metric name indicates that the related trend line is hidden.

**Create a cluster**

1. In the upper-right corner of the **Cluster** tab, click **Add Cluster**.
2. In the **Add Cluster** panel, configure the parameters.

| Parameter | Description |
|---|---|
| Cluster Name | The name of the cluster. |
| Region in Apsara Infrastructure Management | The region of the cluster. |
| Tenant Name | The tenant to which the cluster belongs. |
| Valid | The status of the cluster. Valid values: Valid and Invalid. |

3. Click **Run**.

**Scale out a cluster**

1. In the upper-right corner of the **Cluster** tab, click **Scale out Cluster**.
2. In the **Bind Host to Cluster** dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Destination alisa Cluster | The name of the destination cluster. |

| Region in Apsara Infrastructure Management Framework | The region of the cluster. |
|---|---|
| base Cluster in Apsara Infrastructure Management Framework | The base cluster in Apsara Infrastructure Management. |
| Host | The host. |
| Cluster Type | The cluster type. |
| Source alisa Cluster | The name of the source cluster. |

3. Click **Run**.

**Resource group slots**

Click the **Group** tab on the **Slot** tab. The **Group** tab displays the slot overview of all DataWorks resource groups, including the maximum number of slots, the numbers of used slots and available slots, and slot usage. It also displays the name, cluster, project, and status of each resource group. To view the slot details of a resource group, click the ID of the resource group in the
**Resource Group ID** column.
In the upper part of the resource group details page, you can view the current slot information of the resource group, such as the numbers of used slots, the maximum number of slots, the ratio of tasks under the resource group to tasks in the project, and the distribution of node types. You can also view the trend chart of slot usage over time, the nodes that occupy the slots, and the owners in the lower part of the page. The trend chart displays trend lines for the number of used slots, the maximum number of slots, and the number of available slots in different colors. You can click a metric name below the chart to display or hide the related trend line. A highlighted metric name indicates that the related trend line is displayed, whereas a dimmed metric name indicates that the related trend line is hidden.

**Create a resource group**

1. In the upper-right corner of the **Group** tab, click **Add Resource Group**.
2. In the **Add Resource Group** panel, configure the parameters.

| Parameter | Description |
|---|---|
| Cluster Name | The cluster associated with the resource group. |
| Resource Group Name | The name of the resource group. |
| Maximum Slots | The maximum number of slots. |
| Resource Group ID | The ID of the resource group. |

3. Click **Run**.

**Change the number of slots for a resource group**

If the number of slots for a resource group is insufficient or excessive, you can change this number to add or remove resources for the resource group.
1. On the **Group** tab, find the resource group that you want to manage and click **Change**
**Maximum Slots** in the Actions column.
2. In the panel that appears, modify the **Maximum Slots** parameter.
3. Click **Run**.

**Migrate a resource group**

If the cluster associated with a resource group has insufficient slots but does not support more slots, you can associate the resource group with another cluster.
1. On the **Group** tab, find the resource group that you want to manage and click **Bind**
**Resource Group**.
2. In the panel that appears, modify the **Target Cluster** parameter.
3. Click **Run**.

**Host slots**

Click the **Hostname** tab on the **Slot** tab. The **Hostname** tab displays the slot overview of all DataWorks hosts, including the maximum number of slots, the number of used slots, and the slot usage. It also displays the IP address, cluster, status, activeness, and monitoring status of each host. To view the slot details of a host, click the name of the host in the **Hostname** column. In the upper part of the host details page, you can view the current slot information of the host, such as the number of used slots and the maximum number of slots. You can also view the trend chart of slot usage over time in the lower part of the page. The trend chart displays trend lines for the number of used slots, the maximum number of slots, and the number of available slots in different colors. You can click a metric name below the chart to display or hide the related trend line. A highlighted metric name indicates that the related trend line is displayed, whereas a dimmed metric name indicates that the related trend line is hidden.

**Modify the host status**

A host can be in the Normal, Unavailable, or Suspended state. You can modify the host status based on your business requirements.
1. On the **Hostname** tab, find the host that you want to manage and click **Change Status** in
the Actions column.
2. In the panel that appears, modify the **Status** parameter.
3. Click **Run**.

**Change the number of slots for a host**

If the number of slots for a host is insufficient or excessive, you can change this number to add or remove resources for the host.
1. On the **Hostname** tab, find the host that you want to manage and click **Change**
**Maximum Slots** in the Actions column.
2. In the panel that appears, modify the **Maximum Slots** parameter.
3. Click **Run**.

**Scale out or in a cluster**

For more information, see Cluster scaling.

**Cluster association**

Click the **Cluster Association** tab on the **Slot** tab. The **Cluster Association** tab displays the information about clusters on which the base-bizalisa service is deployed, including tenant ID, tenant name, Apsara Infrastructure Management region, cluster name, cluster type, and status. You can perform operations on the clusters.

**Associate a cluster**

1. On the **Cluster Association** tab, find the cluster that you want to manage and click **Bind**
**Relationship** in the **Actions** column.
2. In the **Bind to ABM Alisa** dialog box, configure the **Tenant Name** and **Region in Apsara**
**Infrastructure Management** parameters.
3. Click **Run**.

**Modify the status of a cluster**

1. On the **Cluster Association** tab, find the cluster that you want to manage and click
**Modify Status** in the **Actions** column.
2. In the **Modify Alisa Cluster Status** dialog box, configure the **Cluster Status** parameter.
Valid values: **Valid** and **Invalid**.
3. Click **Run**.

**Modify the type of a cluster**

1. On the **Cluster Association** tab, find the cluster that you want to manage and click **High-**
**risk Operations** in the **Actions** column.
2. In the **[Fault Fixing]-[High-risk Operations] Modify Scheduling Cluster Type** dialog
box, configure the **Cluster Type** parameter. Valid values: **Scheduling Cluster** and **Synchronize Cluster**.
3. Click **Run**.

**Resource analysis**

Click the **Resource Analysis** tab on the **Slot** tab. The **Resource Analysis** tab displays information about the dpbizalisa database, including the number of dirty data records, status and type distribution of current tasks, distribution of occupied resource groups, and ongoing task instances.

**View runtime logs**

1. On the **Resource Analysis** tab, find the task that you want to manage and click **View Run**
**Logs** in the **Actions** column.
2. In the **Run Logs** panel, view the runtime logs.
3. Click **Compare Versions** to view the differences.

**Terminate a task**

1. On the **Resource Analysis** tab, select the task that you want to manage and click
**Terminate Tasks**.
2. In the **Terminate Alisa Task** panel, click **Run**.

###### DataWorks service nodes

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

###### DataWorks projects

DataWorks provides a list of tenant projects on DataWorks. You can filter and sort the projects in the Apsara Big Data Manager (ABM) console.

**View DataWorks projects**

1. Log on to the ABM console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **Operation and maintenance**.
The **Overview** tab of the **Service operation and maintenance > Data workshop** page appears.
4. Select a cluster from the drop-down list and click the **Project** tab.
The **Project** tab displays the project ID, project name, ODPS engine name, environment, tenant ID, project owner, ID of the default resource group, and identifier of the default resource group.

**Update a project or the default resource group of a node**

Updating the default resource group of a project is similar to updating the default resource group of a node. In this example, the default resource group of a project is updated.
1. On the **Project** tab, find the project that you want to manage and click **Update project**
**default Resource Group** in the **Actions** column.
2. In the **Update project default Resource Group** dialog box, select a resource group from
the **Target resource group identity** drop-down list.
3. Click **Run**. A message appears, indicating that the operation has been submitted.

**Other operations supported by DataWorks projects**

Filter projects You can filter projects by **Tenant Name** and **Environment**. Select a tenant name or an environment and click the icon to filter projects. Sort projects You can sort projects by column in ascending or descending order. You can click the icon to the right of a column to sort existing projects. The icon indicates that the projects are sorted in ascending order, while the icon indicates that the projects are sorted in descending. The icon indicates that project sorting is canceled. Export project information Click **Export** in the upper-right corner of **project list**. In the **Create Download** dialog box, specify a download path and a file name, and click **Download** to export the project list. If you select **Open after download**, the exported project list is displayed by default.

###### Service configurations

The Configuration tab allows you to modify the configuration items of the service roles of DataWorks based on your business requirements.

**Go to the Settings tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**. The **Overview** tab of **Data**
**Warehouse** under **Services** appears.
4. Select a cluster from the drop-down list and click the **Settings** tab.

**Modify a configuration item**

1. On the **Settings** tab, find the configuration item that you want to modify and click **Modify**
in the **Actions** column.
2. In the **Edit Setting** panel, modify the **configValue** parameter.
3. Click **Run**.

###### Cluster scaling

Apsara Big Data Manager (ABM) supports DataWorks cluster scaling. To scale out a DataWorks cluster, add physical hosts in the default cluster of Apsara Infrastructure Management to the DataWorks cluster. To scale in a DataWorks cluster, remove physical hosts from the DataWorks cluster to the default cluster of Apsara Infrastructure Management.

**Background information**

In Apsara Stack, scaling out a cluster involves complex operations. You must configure new physical hosts on Deployment Planner so that they can be added to the default cluster of Apsara Infrastructure Management. The default cluster of Apsara Infrastructure Management is considered as a resource pool that can provide resources for scaling out business clusters. To scale out a cluster, add physical hosts in the default cluster of Apsara Infrastructure Management to the cluster. To scale in a cluster, remove physical hosts from the cluster to the default cluster of Apsara Infrastructure Management. When you scale out a DataWorks cluster, ABM adds physical hosts in the default cluster to the DataWorks cluster. When you scale in a DataWorks cluster, ABM removes physical hosts from the DataWorks cluster to the default cluster. The server roles of physical hosts in DataWorks include **BaseBizCdpGatewayWithNc#** and **BaseBizGatewayWithNc#**. DataWorks cluster scaling supports only the two server roles.

**Prerequisites**

Scale-out The physical hosts that you want to add to your DataWorks cluster are in the default cluster of Apsara Infrastructure Management. The server role of the template host is **BaseBizCdpGatewayWithNc#** or
**BaseBizGatewayWithNc#**.
Scale-in The server role of the template host is **BaseBizCdpGatewayWithNc#** or
**BaseBizGatewayWithNc#**.

**Note**

You can go to the **DataWorks** page. Then, click **O&M** in the upper-right corner, and click the **Services** tab. In the left-side navigation pane, click **Data**
**Warehouse**. On the page that appears, click the **Instances** tab. In the server role list,
find the server role **BaseBizCdpGatewayWithNc#** or **BaseBizGatewayWithNc#**, and click the server role name to go to the Apsara Infrastructure Management console and view the hosts with the server role **BaseBizCdpGatewayWithNc#** or
**BaseBizGatewayWithNc#**.

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

##### Data Integration

###### Data Integration overview

The Overview tab of Data Integration displays information in the Task Scheduling Overview, Today's Tasks, Third-party Dependencies - Total Requests, Third-party Dependencies - Response Time (milliseconds), Third-party Dependencies - Request Error Rate, and Thirdparty Dependencies - Failed Requests sections.

**Procedure**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**. The **Overview** tab of **Data**
**Warehouse** under **Services** appears.
4. In the left-side navigation pane, click Data Integration. The **Overview** tab under Data
Integration appears. After you configure the **Aggregation Period** parameter and select a time period, you can view information in the following sections:

**Task Scheduling Overview**

**Today's Tasks**

**Third-party Dependencies - Response Time (milliseconds)**

**Third-party Dependencies - Total Requests**

**Third-party Dependencies - Request Error Rate**

**Third-party Dependencies - Failed Requests**

###### Data Integration instances

This topic describes how to view instance information on the Instance tab of Data Integration and analyze data from multiple dimensions such as synchronized data volume, synchronization speed, and number of tasks.

**Go to the Instance tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**. The **Overview** tab of **Data**
**Warehouse** under **Services** appears.
4. In the left-side navigation pane, click Data Integration. The **Overview** tab appears.
5. Click the **Instance** tab. The **Instances** tab appears.

**View instance information**

On the **Instances** tab, you can filter instances by configuring parameters such as **Project**
**Name**, **Resource Group**, **Host**, **Status**, **Read Plug-in Type**, **Write Plug-in Type**, and
**Data Source**.
You can also click the request ID, synchronization script number, or resource group name to view the corresponding details. After you click the request ID, you can view the event type, source IP address, and start time of the instance. After you click the synchronization script number, you can view the following information: In the **Job Statistics by Day** section, you can view the trends of the synchronized data volume, synchronization speed, and consumed time by day. In the **Job Statistics by Run** section, you can view the trends of the synchronized data volume, synchronization speed, and consumed time by fixed interval. In the **Historical Trend of Terminated Tasks** section, you can view the trends of successful, failed, and killed tasks. After you click the resource group name, you can view the slot usage of the resource group. After you view the corresponding details, you can click **Back** to return to the **Instances** tab. On the Instances tab, you can also view the number of initialized, submitted, pending, ongoing, failed, and successful tasks.

**View multi-dimensional analysis information**

On the **Multi-dimensional Analysis of Current Day** tab, you can filter data by configuring parameters such as **Project Name**, **Resource Group**, **Host**, **Status**, **Read Plug-in Type**,
**Write Plug-in Type**, and **Data Source**. Then, you can view analysis information from
multiple dimensions such as synchronized data volume, synchronization speed, and number of tasks.

###### View historical analysis information

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

#### Cluster O&M

##### Cluster overview

The Overview tab displays the key metrics and health check results of a cluster in the Health Check, CPU, DISK, LOAD, MEMORY, and PACKAGE sections.

**Go to the Overview tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**.
4. On the **O&M** page, click the **Cluster O&M** tab.
5. In the upper-left corner of the **Cluster O&M** page, select a cluster from the drop-down list.
Then, click the **Overview** tab.

**Health Check**

This section displays the number of check items of the cluster and the respective number of Critical, Warning, and Exception alerts. Click **View Details** to view the health check details on the Health tab.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the cluster within the specified period of time.

**DISK**

The DISK chart shows the trend line of the storage usage for the cluster over time. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the cluster within the specified period of time.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster within the specified period of time.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, and available memory size for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the cluster within the specified period of time.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the cluster over time in different colors. These trend lines reflect the data transmission status of the cluster. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the cluster within the specified period of time.

##### Cluster health

On the Health Status page, you can view all checkers of a cluster, including the checker details, check results for the hosts in the cluster, and schemes to clear alerts (if any). In addition, you can log on to a host and perform manual checks on the host.

**Go to the Health Status page under Clusters**

1. Log on to the ABM console.
2. Click
in the upper-left corner and select **DataWorks**.
3. On the page that appears, click **O&M** in the upper-right corner.
4. Click the **Clusters** tab at the top of the **O&M** page.
5. On the **Clusters** page, select a cluster in the left-side navigation pane, and click the
**Health Status** tab. The **Health Status** page appears.
On the **Health** tab, you can view all check items for the cluster and the check results for the hosts in the cluster. The following alerts may be reported on a host: **Critical**, **Warning**, and **Exception**. The alerts are represented in different colors. You must handle the alerts at the earliest opportunity, especially the **Critical** and **Warning** alerts. The following table describes the check results.

**View the details of a check item**

1. On the **Health** tab, find the check item that you want to view and click **Details** in the
**Actions** column. In the dialog box that appears, view the details of the check item.
The following information about the check item is displayed: **Name**, **Source**, **Alias**,
**Application**, **Type**, **Default Parameters**, **Custom Parameters**, and **Description**. The
methods to clear alerts are provided in the description.
2. Click **Show More** to view more information about the check item.
You can view more information in the **Script**, **Target (TianJi)**, **Default Threshold**, and
**Custom Threshold** sections.

**View the hosts for which alerts are reported and the causes for**

**the alerts**

You can view the check history and check results of a check item on a host.
1. On the **Health** tab, click the
icon on the left of a check item to show all alerts that are triggered by the check item. You can view all hosts on which the check item is run.
2. Click a hostname. In the panel that appears, find the alert that you want to manage and
click **Details** in the Actions column to view the cause of the alert.

**Clear alerts**

On the Health Status page, click **Details** in the Actions column of a checker with alerts. In the dialog box that appears, view the schemes to clear alerts.

**Run a check item again**

After you handle an alert for a host, click **Refresh** in the Actions column of the host to run the check item again for the host. This way, you can check whether the alert is cleared.

#### Host O&M

##### Host overview

The Overview tab displays the information about a host in the Machine Information, Server Role Status, CPU, DISK, LOAD, MEMORY, and PACKAGE sections.

**Go to the Overview tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**.
4. On the **O&M** page, click the **Host O&M** tab.
5. On the left side of the **Host O&M** page, select a host. Then, click the **Overview** tab.
This tab displays the detailed information about a host, the status of server roles, and the trend charts of key metrics.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the host in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the host in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the host in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the host over time in different colors. These trend lines reflect the data transmission status of the host. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the host in the specified period.

##### Host server roles

The Server Role tab displays the information about server roles, including cluster, service instance, and role name.

**Go to the Service Role tab**

1. Log on to the Apsara Big Data Manager (ABM) console.
2. Click the
icon in the upper-left corner and select **DataWorks**.
3. In the upper-right corner of the page that appears, click **O&M**.
4. On the **O&M** page, click the **Host O&M** tab.
5. On the left side of the **Host O&M** page, select a host. Then, click the **Server Role** tab.

### Management

#### Overview

The management module is the configuration and software management center of Apsara Big Data Manager (ABM). It is an important functional module that supports and customizes O&M items for services. The management module supports the following features: Jobs: allows you to run jobs to perform O&M operations on big data products. API Management: allows you to manage the permissions of ABM APIs. Health Checks: allows you to create health check items and apply them to service hosts. Operation Logs: allows you to view the job execution records and other service O&M operations in ABM.

#### Jobs

##### Overview

This topic describes the UIs for job management and terms related to jobs in Apsara Big Data Manager (ABM). ABM allows you to run jobs to perform O&M operations on big data services. Jobs in ABM are run to perform O&M operations on physical devices in a cluster. The Jobs page contains the
**Job Execution** page.

**Terms**

Terms related to jobs include: Ordinary job: A job that can only be manually run. No timer is set. Cron job: A job that is automatically run based on timer settings.

**Job Execution page**

The **Job Execution** page contains the following tabs: Jobs You can view and run ordinary jobs, and view their execution history. You can search for a specific ordinary job. Cron Jobs You can enable, disable, view, or run cron jobs, and view their execution history. You can search for a specific cron job. Execution History You can view the execution history of ordinary and cron jobs. You can specify multiple filter conditions to search for a specific job and view the execution history of the specific job.

##### Jobs

###### Manually run a job

After you have created an ordinary job, you must manually run the job in order to perform O&M operations on the product. You can also manually run a cron job.

**Prerequisites**

You must have an ABM administrator account.

**Procedure**

1. Log on to the ABM console.
2. Click **Management** in the upper-right corner. On the page that appears, click **Jobs** in the
left-side navigation pane.
3. Click **Ordinary Jobs** on the **Job Execution** page.
If you need to manually run a cron job, click **Cron Jobs**. The procedure to manually run a cron job is the same as that of an ordinary job. This topic takes ordinary jobs as an example.
4. In the **Ordinary Jobs** list, click **Run** in the Actions column of a job.
5. Confirm the job risks in the dialog box that appears, and click **Confirm**.
After you have confirmed, a record is automatically generated on the **Execution History** page. For more information, see View execution history.
6. On the job execution page, click **Start** at the top to start the execution.
You can find the record about a job on the **Execution History** page, and click **View** to go to the detailed execution page.

###### Enable or disable a cron job

When a cron job is generated from a scheme, the job is disabled by default. You must manually enable it. If you do not need the cron job to run during a specified time period, you can manually disable it.

**Prerequisites**

You must have an ABM administrator account.

**Procedure**

1. Log on to the ABM console.
2. Click **Management** in the upper-right corner. On the page that appears, click **Jobs** in the
left-side navigation pane.
3. On the **Job Execution** page, click **Cron Jobs**.
4. On the **Cron Jobs** page, you can enable or disable a cron job.
To enable a cron job in the inactive status, click **Enable** in the Actions column of the cron job. After a cron job is enabled, its **status** changes to **Active**. The **Enable** button is replaced by **Disable**. To disable a cron job in the active status, click **Disable** in the Actions column of the cron job. After a cron job is disabled, its **status** changes to **Inactive**. The **Disable** button is replaced by **Enable**.

###### View the execution history of a job

Apsara Big Data Manager (ABM) allows you to view the execution history of a specific job to learn the execution status of it.

**Prerequisites**

An ABM administrator account is obtained.

**Background information**

After you confirm to run a job, ABM generates logs for the job execution. You can learn the execution status by using the log data. The **Execution History** page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter setting information, and allows you to download execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the **Pending** state or retry the execution of a job that is in the
**Exception** state.
This topic describes how to view the execution history of an ordinary job. You can follow a similar procedure to view the execution history of a cron job.

**Procedure**

1. Log on to the ABM console.
2. Click **Management** in the upper-right corner. On the page that appears, click **Jobs** in the
left-side navigation pane.
3. Click the **Ordinary Jobs** tab on the **Job Execution** page.
4. On the **Ordinary Jobs** page, click **History** in the Actions column of an ordinary job. The
**Execution History** page appears.
You can view the execution history of this job on the **Execution History** page. For more information, see View execution history.

###### View execution history

Apsara Big Data Manager (ABM) allows you to view the execution history of jobs and schemes to learn about their execution details.

**Prerequisites**

An ABM administrator account is obtained.

**Background information**

After you have confirmed the execution of a job, a record is automatically generated on the Execution History page. The **Execution History** page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter setting information, and allows you to download execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the **Pending** state or retry the execution of a job that is in the
**Exception** state.

**Procedure**

1. Log on to the ABM console.
2. In the upper-right corner of the ABM console, click **Management**. In the left-side
navigation pane of the page that appears, click **Jobs**.
3. On the **Job Execution** page, click the **Execution History** tab.
4. If a large number of execution records exist, filter them by a combination of one or more of
the following filter conditions: **job name**, **creator**, **execution status**, and time range. Then, click to search for the desired records.
5. Click **View** in the Actions column of a record to view the execution details.
The following table lists the operations that you can perform on records in different states.

| Execution status | Feature | Procedure |
|---|---|---|
| All states | View the parameter configuration | Click Parameter Configuration in the upper-right corner of the job details page, and select Context Parameters or Global Parameters to view the context parameters or global parameters of the job. |
|   | Download execution details | Click Download Execution Details in the upper-right corner of the job details page to download the job execution details to your on-premises machine. Save the job into a TXT file. The execution details record the JSON and raw data of job execution. |
|   | View the execution details of steps | On the Servers page of a step, click View Details in the Actions column of a server. The execution details of the step on the server, including the execution output, appear in the Execution Details section. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|   | Refresh the page | If the job is in the running state, you can clickR efresh in the upper-right corner of the job details page to view the latest execution status. |
| Pending | Start the job | Click Start in the upper-right corner of the job details page to start the job. |
|   | Cancel the job | Click Cancel in the upper-right corner of the job details page to cancel the job. |
| Unconfirmed | Complete the manual operation | At the manual step that you want to perform, follow the instructions and click OK to go to the next step. |
|   | Roll back to the complete status of the previous step | At the manual step that you want to perform, click Rollback to roll back to the complete status of the previous step. |
|   | Cancel the job | Click Cancel to cancel the job. |
|   | Retry the step that has exceptions | In the step that has exceptions, click Retry to execute the step again. |
|   | Skip the step that has exceptions | In the step that has exceptions, click Skip to skip this step and execute the subsequent steps. |

| erations and Mainte O&M by using Apsa anager |   |   |
|---|---|---|
|   | nance Gui ra Big Dat | DataWork |
| Exception |   |   |
|   | Roll back to the complete status of the previous step | In the step that has exceptions, click Rollback to roll back to the complete status of the previous step. |
|   | Reset the step that has exceptions to the Pending state | In the step that has exceptions, click Reset to reset the step to the Pending state. When the step that has exceptions is reset to the Pending state, the execution status becomes Paused. You can click Continue in the upper-right corner of the job details page to execute the step again. |
|   | View the execution details of steps that has exceptions | On the Servers page of a step, click View Details in the Actions column of a certain server. The execution details of the step on the server, including the execution output and error message, appear in the Execution Details section. After you view the details of the server that has exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Retry to execute the step again on the server. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
| Failure | Retry the failed step | In the failed step, click Retry to execute the step again. |
|   | Skip the failed step | In the failed step, click Skip to skip this step and execute the subsequent steps. |
|   | Roll back to the complete status of the previous step | In the failed step, click Rollback to roll back to the complete status of the previous step. |
|   | Reset the failed step to the Pending state | In the failed step, click Reset to reset the step to the Pending state. When the failed step is reset to the Pending state, the execution status becomes Paused. You can click Continue in the upper-right corner of the job details page to execute the step again. |

|   | View the execution details of failed steps | On the Servers page of a step, click View Details in the Actions column of a certain server. The execution details of the step on the server, including the execution output and error message, appear in the Execution Details section. After you view the details of the server that has exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Retry to execute the step again on the server. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|---|---|---|
|   | Cancel the job | Click Cancel in the upper-right corner of the job details page to cancel the job. |

#### Health management

##### Health management

Apsara Big Data Manager (ABM) provides a wide variety of built-in checkers for each big data service. These checkers are used to check service faults and send alerts. This helps you detect and fix faults in a timely manner.

**Prerequisites**

Your ABM account is granted the required permissions on services on which you want to perform O&M. The alert sources and checkers of the monitoring items are obtained.

**Background information**

Different services have different scheduling and monitoring items, but the configuration and operations that can be performed on services are the same. This topic describes the scheduling and monitoring items of MaxCompute. Scheduling: Checkers run scheduling scripts on the servers of specific TianJi roles and generate raw alert data. Raw alert data provides information about the checker, server, alert severity, and alert content. Raw alert data is stored in the ABM database. Monitoring: You can mount checkers to service pages in ABM. You can configure filter policies to display alerts about high priority checkers. Both the scheduling items and monitoring items are built-in and you cannot add more scheduling and monitoring items. However, you can modify some parameters of the items, such as whether to enable an item, running parameters, and description. In addition, you can configure mount points of the monitoring items or delete monitoring items.

**View details and mount points of scheduling items**

The mount points of scheduling items are built-in and you cannot add, modify, or delete mount points. The mount points of the scheduling items correspond to the list of all hosts corresponding to the Apsara Infrastructure Management role that runs the scheduling script.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**. The **Scheduling** tab appears. The **Scheduling** tab displays all scheduling items of the current product.
4. On the **Scheduling** tab, find the desired scheduling item and click **View** in the Actions
column to view the details of the scheduling item.
5. Click the plus sign to expand a scheduling item. Then, view the mount points of the
scheduling item.

**Modify a scheduling item**

You can configure the scheduling interval and running parameters of a scheduling item, and configure whether to enable the scheduling item.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**. The **Scheduling** tab appears.
4. On the **Scheduling** tab, find the desired scheduling item and click **Edit** in the Actions
column. In the Modify Checker dialog box, configure relevant parameters.
**Type**: The value **System Default** indicates that parameters, such as **Execution Interval**
and **Parameters**, use the default settings. The value **Custom** indicates that the parameters can be customized.

**Note**

Configure the **Execution Interval** parameter based on the **crontab** command.
5. Click **OK**. The scheduling item is modified.

**View faulty hosts**

You can view all the faulty hosts in the current cluster.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**. The **Scheduling** tab appears.
4. In the upper-right corner of the Scheduling tab, click **Faulty Servers** to view the faulty
hosts in the cluster. The list of the faulty hosts shows all faulty hosts in the current cluster and the role of each host in the Apsara Infrastructure Management.

**Modify a monitoring item**

You can modify the name and description of a monitoring item and determine whether to enable the monitoring item. The alert sources and checkers of monitoring items are built-in. We recommend that you do not modify them.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears. The **Monitoring** tab displays all monitoring items of the current service.
5. On the **Monitoring** tab, find the desired monitoring item and click **Modify** in the Actions
column to modify the configuration of the monitoring item.
6. Click **OK**. The scheduling item is modified.

**Add a mount point for a monitoring item**

After a mount point is added for a monitoring item, the monitoring item mounts the raw alert data to the O&M page of each service in the ABM console.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears.
5. On the **Monitoring** tab, click the plus sign to expand a monitoring item. Then, view the
mount points of the monitoring item.
6. Click **Add Mount Point** under the mount point list. In the Add Amount Point dialog box,
configure relevant parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Mount Point | The mount point to which the required inspection result of this monitoring item that you want to mount. For example, the value odps/host indicates that the result is mounted to the host O&M page of MaxCompute. |
| Filter Policy | Valid values: None: All alerts generated by the monitoring item is displayed. Custom: The alerts generated by the monitoring item in accordance with the filter configured for the service tree node are displayed. Node Name: The alerts whose node name is the same as the name of the current node are displayed. |
| Enabled | Specifies whether the mount point takes effect. |

7. Click **OK**. The scheduling item is modified.

**Delete a mount point from a monitoring item**

1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears.
5. On the **Monitoring** tab, click the plus sign to expand a monitoring item. Then, view the
mount points of the monitoring item.
6. Find the desired mount point and click **Delete** in the Mount Point column. In the message
that appears, click **OK**. The mount point is deleted.

**Delete a monitoring item**

1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears.
5. Find the desired monitoring item and click **Delete** in the Actions column. In the message
that appears, click **OK**. The monitoring item is deleted.

##### Inspection management

The inspection management feature of Apsara Big Data Manager (ABM) allows you to configure inspection scenarios, inspection items, and scenario combinations based on your business requirements.

**Prerequisites**

Your ABM account is granted the required permissions on services on which you want to perform O&M.

**Go to the Management page**

1. Log in to the ABM console.
2. In the upper-left corner, click the
icon and select the big data service that you want to manage.
3. In the top navigation bar, click **Management** to go to the Management page.

**Create a scenario**

1. In the left-side navigation pane, click **Health Management**. On the page that appears,
choose **Patrol Configuration > Scenes**.
2. In the upper-right corner of the Scenes tab, click **Create Scene**. In the Create Scene panel,
configure the parameters based on your business requirements.
3. Click **Submit**.
After a scenario is created, you can **Edit**, **Start Patrol**, **Manage Patrol Items**, and view
**Execution History** of the scenario.

**Create an inspection item**

1. In the left-side navigation pane, click **Health Management**. On the page that appears,
choose **Patrol Configuration > Patrol Items**.
2. In the upper-right corner of the Patrol Items tab, click **Create Patrol Item**.
3. In the **Create Patrol Item** panel, configure the parameters based on your business
requirements.
4. Click **Submit**.
After an inspection item is created, you can **Edit** and **Delete** the inspection item.

**Create a scenario combination**

1. In the left-side navigation pane, click **Health Management**. On the page that appears,
choose **Patrol Configuration > Scenario Combination**.
2. In the upper-right corner of the Scenario Combination tab, click **Create Scene**.
3. In the **Create Scene** panel, configure the parameters based on your business
requirements.
4. Click **Submit**.
After a scenario combination is created, you can **Edit**, **Manage Patrol Items**, and view
**Execution History** of the scenario combination.

#### Operation auditing

This feature allows you to view the O&M operations of the current service of Apsara Big Data Manager (ABM). The details of each operation are provided for retrieval and fault locating.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on the corresponding service.

**Background**

You can view operation logs by service. For example, to view the operation logs of MaxCompute, you must go to the MaxCompute page first. The following describes how to view the operation logs of MaxCompute.

**Note**

This page displays only the O&M operations of a service. Note that the O&M operations of job services are not included.

**Procedure**

1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click **MaxCompute**.
3. Click **Management** in the upper-right corner of the MaxCompute page, and then click
**Operation Audit** in the left-side navigation pane of the **Management** page.
The **Operation Audit** page displays the O&M operations of the current service. In this example, the information about MaxCompute O&M operations is displayed, including the operation name, operation ID, status, submission time, start time, end time, operator, and implementation method.
4. Click **Details** for an operation to view the O&M operation details.
You can also view the causes of failed steps in detail.
5. If an O&M operation fails, view the cause of the failure.
6. When the task is in the Failure, Not Started, Pending, or Exception state, perform the
operations listed in the following table based on your situation.

| State | Executable operation |
|---|---|
| Not Started | Click Start to start the task. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |
| Pending | Follow the instructions and click OK to go to the next step. Click Rollback to roll back to the complete status of the previous step. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |
| Exception | Click Retry to run the step again. Click Skip to skip this step and execute the subsequent steps. Click Rollback to roll back to the complete status of the previous step. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |

| Failure | Click Retry to run the step again. Click Skip to skip this step and execute the subsequent steps. Click Rollback to roll back to the complete status of the previous step. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |
|---|---|

7. To download the O&M operation execution logs, click **Download Execution Details** at the
top to save the logs to your local device.

## Deep inspection

### Overview

DataWorks deep inspection covers and collects the monitoring alerts, resource usage, and key metrics of DataWorks. This allows you to check the health status of DataWorks in a visualized manner, prevent unexpected risks before major issues or faults occur, and ensure service stability.

**Note**

Apsara Big Data Manager does not revoke inspection reports. However, the risks generated in all inspection reports and the corresponding thresholds are collected. DataWorks deep inspection covers the following items: Inspect clusters Inspect the base_meta project Inspect the BaseBizAlisa service Inspect the BaseBizPhoenix service Inspect the BaseBizCdp service

### Introduction to DataWorks

**service roles**

This topic describes the common service roles of DataWorks and how to view the service roles.

**Background information**

DataWorks has 43 service roles. The following table describes the service roles.

| Service role | Description | Quantity | Form | Port | High reliability |
|---|---|---|---|---|---|
| BaseBizSso | Single sign-on (SSO) | 2 | Container | 7001 | Yes |
| BaseBizWkbench | O&M center | 2 | Container | 7001 | Yes |
| Redis1 | Redis service | 1 | Container | 6379/26379 | Yes |
| Redis2 | Redis service | 2 | Container | 6379/26389 | Yes |
| BaseBizDmc | Data map | 2 | Container | 7001 | Yes |
| BaseBizBaseapi | API scheduling | 2 | Container | 7001 | Yes |

| BaseBizDbinit | Database initialization | 1 | Container | N/A | N/A |
|---|---|---|---|---|---|
| BaseBizPhoenix | Scheduling engine | 3 | Container | 7001 | Yes |
| BaseBizAlisa | Execution engine | 2 | Container | 7001 | Yes |
| BaseBizConsole | Apsara Stack console | 2 | Container | 7001 | Yes |
| BaseBizTenant | Tenant | 2 | Container | 7001 | Yes |
| BaseBizMetaserv ice | Metadata | 2 | Container | 7001 | Yes |
| BaseBizMario | Real-time synchronization | 2 | Container | 7001 | Yes |
| BaseBizDashboar d | Data integration dashboard | 2 | Container | 7001 | Yes |
| BaseBizCdp | Offline synchronization scheduling | 2 | Container | 7001 | Yes |
| BaseBizGateway | Scheduling gateway deployed in Docker | 2 | Container | 7001 | Yes |
| BaseBizCdpGate way | Offline synchronization gateway deployed in Docker | 2 | Container | 8000 | Yes |
| BaseBizGateway Search | Gateway for code search and backup or restoration | 2 | Container | 8000 | Yes |
| BaseBizGateway WithNc | Scheduling gateway deployed on a physical server | At least one | Physical server | 8000 | N/A |

| BaseBizCdpGate wayWithNc | Offline synchronization gateway deployed on a physical server | At least one | Physical server | 8000 | N/A |
|---|---|---|---|---|---|
| BaseBizCommon base | DataStudio | 4 | Container | 7001 | Yes |
| ServiceTest | Smoke testing | 1 | Container | N/A | N/A |
| DataworksDatao sPanel | Workspace and tenant management | 2 | Container | 7001 | Yes |
| DataworksMessa geCenter | Notification center | 2 | Container | 7001 | Yes |
| BaseBizTsp | Code repository service | 2 | Container | 7001 | Yes |
| DataworksMosad | Intelligent monitoring | 2 | Container | 7001 | Yes |
| BaseBizDiide | Data synchronization | 2 | Container | 7001 | Yes |
| DataworksNavig ation | Public header | 2 | Container | 7001 | Yes |
| BaseBizWormhol e | Wormhole service | 2 | Container | 7001 | Yes |
| BaseBizDataOsA piInit | POP API registration | 1 | Container | N/A | N/A |
| DataworksDsmG uard | Security center | 2 | Container | 7001 | Yes |
| BaseBizGateway StreamX | Real-time synchronization gateway | 2 | Container | 8000 | Yes |
| BaseBizAlisaloga gent | Alisa log agent | 2 | Container | 7001 | Yes |

| DataworksExecut orNode | Real-time execution engine node | 2 | Container | 7001 | Yes |
|---|---|---|---|---|---|
| DataworksExecut orManager | Real-time execution engine manager | 2 | Container | 7001 | Yes |
| DataworksNode market | Custom node | 2 | Container | 7001 | Yes |
| DataworksMeasu re | Metering | 2 | Container | 7001 | Yes |
| DataworksLsp | Language Server Protocol (LSP)- based intelligent code editor | 2 | Container | 7001 | Yes |
| DataworksPlugin | Microservices framework | 2 | Container | 7001 | Yes |
| DataworksCdn | Frontend service | 2 | Container | 7001 | Yes |
| DataworksMetaPl uginService | Metadata plug-in service | 2 | Container | 7001 | Yes |
| BaseBizOps | O&M assistant | 2 | Container | 7001 | Yes |
| DataworksElastic search | Elasticsearch service | 3 | Container | 9200/9300/ 9114 | Yes |

**View service roles**

1. Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
Platform Operation > Apsara Infrastructure Management > Resource Management. In the left-side navigation pane, choose Resource Management > Product & Cluster O&M. On the
**Product & Cluster O&M** page, enter **base** in the **Product | Cluster** search box and press
the Enter key.
2. Find the DataWorks cluster that you want to manage and click **Cluster Details** in the
**Actions** column. The **Cluster Details** page appears.
3. On the **Services** tab, find the service that you want to query and click **Details** in the
Actions column. The service role is displayed in the left-side Components pane.

**BaseBizSso#**

Role description This service role provides the SSO logon service and depends on the BaseBizDbinit# and Redis1# service roles. RMA or restart The physical servers on which the service role is deployed support the Remote Maintenance Agent (RMA) or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-sso/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizWkbench#**

Role description This service role provides the features of an O&M center and depends on the BaseBizDbinit#, BaseBizTenant#, and Redis1# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-wkbench/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**Redis1#**

Role description This service role provides the Redis service and does not depend on other service roles. RMA or restart None. Reclone The physical server on which the service role is deployed supports the reclone operation. Logs

```
Log path: /var/log/redis/redis.log and /var/log/redis/sentinel.log
```

Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**Redis2#**

Role description This service role provides the Redis service and depends on the Redis1# service role. RMA or restart None. Reclone The physical server on which the service role is deployed supports the reclone operation. Logs

```
Log path: /var/log/redis/redis.log and /var/log/redis/sentinel.log
```

Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizDmc#**

Role description This service role provides the features of Data Map and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-dmc/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizBaseapi#**

Role description This service role schedules the API service and depends on the BaseBizDbinit# and BaseBizTenant# service roles. RMA or restart None. Reclone The physical server on which the service role is deployed supports the reclone operation. Logs Log path:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the BaseBizBaseapi container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id;
```

Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizDbinit#**

Role description This service role provides the database initialization service and does not depend on other service roles. RMA or restart None. Reclone The physical server on which the service role is deployed supports the reclone operation. Logs Log path:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the BaseBizDbinit container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id ;
```

Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizPhoenix#**

Role description This service role provides the schedule engine and features such as generating instances of auto triggered nodes, and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-phoenix/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizAlisa#**

Role description This service role provides the execution engine and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-alisa/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizConsole#**

Role description This service role provides the Apsara Stack console and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-console/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizTenant#**

Role description This service role provides the tenant service and depends on the BaseBizDbinit#, DataworksMessageCenter#, and Redis1# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-tenant/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizMetaservice#**

Role description This service role provides the metadata service and depends on the BaseBizAlisa#, BaseBizBaseapi#, BaseBizDbinit#, BaseBizPhoenix#, and BaseBizTenant# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-metaservice/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizMario#**

Role description This service role provides the real-time synchronization service and depends on the BaseBizAlisa#, BaseBizDbinit#, and BaseBizTenant# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-mario/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizDashboard#**

Role description This service role provides the Data Integration dashboard and depends on the BaseBizAlisa#, BaseBizDbinit#, and BaseBizTenant# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-dashboard/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizCdp#**

Role description This service role provides the offline synchronization scheduling service and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-cdp/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizGateway#**

Role description This service role provides the scheduling gateway deployed in Docker and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizCdpGateway#**

Role description This service role provides the offline synchronization gateway deployed in Docker and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizGatewaySearch#**

Role description This service role provides the gateway for code search and backup or restoration and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizGatewayWithNc#**

Role description This service role provides the scheduling gateway deployed on a physical server and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizCdpGatewayWithNc#**

Role description This service role provides the offline synchronization gateway deployed on a physical server and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizCommonbase#**

Role description This service role provides the features of DataStudio and depends on the BaseBizDbinit#, BaseBizTenant#, and Redis1# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-commonbase/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**ServiceTest#**

Role description This service role provides the smoke testing service. You can create smoke testing instances and verify features by using this service role, which is deployed as a Docker container. This service role depends on the BaseBizCommonbase# and BaseBizMetaservice# service roles. RMA or restart None. Reclone The physical server on which the service role is deployed supports the reclone operation. Logs Log path:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the ServiceTest container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id;
```

Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksDataosPanel#**

Role description This service role provides the workspace and tenant management services and depends on the BaseBizDbinit# and BaseBizTenant# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-dataos-panel/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksMessageCenter#**

Role description This service role provides the features of Notification Center and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-message-center/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizTsp#**

Role description This service role provides the code repository service and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-tsp/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksMosad#**

Role description This service role provides the intelligent monitoring service and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-mosad/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizDiide#**

Role description This service role provides the Data Integration service and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-diide/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksNavigation#**

Role description This service role provides public headers and depends on the BaseBizDbinit# and BaseBizTenant# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-navigation/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizWormhole#**

Role description This service role provides the wormhole service and depends on the BaseBizDbinit# and Redis1# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-wormhole/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizDataOsApiInit#**

Role description This service role provides the POP API registration service and depends on the BaseBizTenant# service role. RMA or restart None. Reclone The physical server on which the service role is deployed supports the reclone operation. Logs Log path:

```bash
-- View the status of all Docker containers and obtain the docker_id parameter of the BaseBizDataOsApiInit container. docker ps -a; -- Retrieve the logs of the container. You need to use this command to retrieve logs because the volume of logs is large. docker logs $docker_id;
```

Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksDsmGuard#**

Role description This service role provides the features of Security Center and depends on the BaseBizTenant# and DataworksNavigation# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dsm-guard/logs/loginlogs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizGatewayStreamX#**

Role description This service role provides the real-time synchronization gateway and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/alisatasknode/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizAlisalogagent#**

Role description This service role provides the Alisa log agent and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-biz-alisalogagent/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksExecutorNode#**

Role description This service role provides the real-time execution engine node and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-executor-node/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksExecutorManager#**

Role description This service role provides the real-time execution engine manager and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-executor-manager/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksNodemarket#**

Role description This service role provides the custom node and depends on the BaseBizAlisa# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-nodemarket/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksMeasure#**

Role description This service role provides the metering service and depends on the BaseBizTenant# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-measure/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksLsp#**

Role description This service role provides the LSP-based intelligent code editor and does not depend on other service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-lsp/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksPlugin#**

Role description This service role provides the microservices framework and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-plugin/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksCdn#**

Role description This service role provides the frontend service and does not depend on other service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-cdn/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksMetaPluginService#**

Role description This service role provides the metadata plug-in service and depends on the BaseBizDbinit# service role. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/dataworks-mps/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**BaseBizOps#**

Role description This service role provides the features of O&M Assistant and depends on the BaseBizDbinit# and Redis1# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/base-tenant-ops/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

**DataworksElasticsearch#**

Role description This service role provides the Elasticsearch service and depends on the Redis1# and Redis2# service roles. RMA or restart The physical servers on which the service role is deployed support the RMA or can be restarted. You must restart the physical servers in batches. Reclone The physical server on which the service role is deployed supports the reclone operation. You need to perform the operation on physical servers in batches. Logs Log path: `/home/admin/elasticsearch-6.8.23/logs` Monitoring Check whether the service role is in the desired state in the Apsara Infrastructure Management console. For more information, see the View service roles section of this topic.

### Inspect clusters

Cluster inspection helps you monitor the status of components and services. This topic describes how to use inspect clusters.

**Procedure**

1. Check the final state of the clusters on which DataWorks depends.
This step checks whether the clusters on which DataWorks depends are in the desired state. If a cluster or service role is not in the desired state, request technical support. i. Inspect the ODPS cluster. ii. Inspect the metabase cluster.
2. Check the final state of the DataWorks clusters.
This step checks whether the DataWorks clusters are in the desired state. If a cluster or service role is not in the desired state, request technical support. Log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose
**Platform Operation** > **Apsara Infrastructure Management** > **Resource**
**Management**. On the Product & Cluster O&M page, check whether DataWorks clusters
in the base category are in the desired state. Check whether the clusters for other features are in the desired state. If you have not purchased clusters for other features, the features are not deployed. Skip this step. For more information, see the Clusters of other features section of this topic.
3. Inspect the disk usage.
This step checks the usage of all disks related to DataWorks. If the usage of a disk exceeds the threshold, clean up the disk. If you cannot clean up a disk, request technical support. In the left-side navigation pane, choose **Resource Management** > **Base Machine**
**Resource Dashboard**. Find the DataWorks machines and check the disk usage in the
Local Dedicated Disk and Local Shared Disk columns.
4. Inspect the metabase.
This step checks whether the databases related to DataWorks are working as expected. If database resources are insufficient, request technical support. i. In the top-navigation bar, choose **Product Operation** > **Databases** > **ApsaraDB**
**Operations and Maintenance System**.
ii. In the left-side navigation pane, choose **Instance management** > **Instance List**. Click the name of the DataWorks database instance that you want to view to go to the instance details page. iii. In the **Performance Information** section, check the disk usage metrics.

**Clusters of other features**

The following table describes the clusters of other features.

| Service or component | feature | Cluster (Apsara Infrastructure Management) |
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
| Resource Group for DataService Studio | DataworkChangeExtFeature | BaseExchangeCluster- |
| Data Security Guard (OEM) | DataworkdsDSFeature | BaseSecurityCluster- |
| Data Security Guard Enhancement Package (OEM) | DsgAdvanced | DsgAdvancedCluster- |
| Data Safety Chain (OEM) | DataworkDschainFeature | BaseSecurityChainCluster- |
| DataBlau (OEM) | BaseDatablauFeature | BaseDatablauCluster- |
| Secure Multi-party Computation (OEM) | BaseMorseFeature | BaseMorseCluster- |

### Inspect the base_meta project

The base_meta project is a metadata project of DataWorks. The project is used to process data of DataWorks offline. This topic describes how to inspect the base_meta project to check the status of the tasks in the base_meta project.

**Procedure**

To inspect the project, you must log on to the base_meta project. Perform the following steps to log on to the base_meta project:
1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Obtain the logon address of the base_meta project.
i. On the Product & Cluster O&M page, find the BasicCluster of the base service. ii. Click Cluster Details in the Actions column to go to the **Cluster Details** page. Click the Resource Details tab. On the **Resource Details** tab, enter **base-biz-commonbase** in the **Resource Name** field and filter resources of the **dns** type. iii. View the value of the **Resource Application Result** column to obtain the logon address of the base_meta project.
3. Obtain the username and password of the base_meta project.
i. Go to the details page of the MaxCompute cluster. ii. Click the Resource Details tab. On the **Resource Details** page, enter **base_admin** in the
**Resource Name** field.
iii. Find base_admin and click the icon in the **Resource Application Result** column to obtain the username and password that are used to log on to the base_meta project.
4. Log in to the base_meta project in the DataWorks console.
5. Go to the Operation Center page to view the status of the MaxCompute project.
If the MaxCompute project is not running, contact technical support for troubleshooting.

### Inspect the BaseBizAlisa

**service**

You can inspect the BaseBizAlisa service to check the status of the service. The BaseBizAlisa service is used to manage remote tasks and gateways. This topic describes how to inspect the BaseBizAlisa service.

**Procedure**

1. Check the status of gateways.
A gateway is a basic hardware unit for DataWorks to run tasks. The following roles are involved: base-baseBizApp.BaseBizGateway# base-baseBizApp.BaseBizCdpGateway# base-baseBizApp.BaseBizGateway# base-baseBizApp.BaseBizCdpGateway# base-baseBizApp.BaseBizGatewaySearch# base-baseBizApp.BaseBizGatewayStreamX# You can check the status of the BaseBizAlisa service in the metadatabase of the service. i. Log on to the dpbizalisa database. For more information, see Appendix: Log in to a database. ii. Check the number of gateways. Execute the following statements to check the number of gateways in different scenarios: Total number of standard gateways: `select`

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
If multiple records whose values of the `status` field are 2 and the number of the records is not decreasing, contact technical support to troubleshoot the issue. i. Log on to the dpbizalisa database. For more information, see Appendix: Log in to a database. ii. Execute the select count(1),status from dpbizalisa.alisa_task group by status; statement to check whether a backlog of tasks exists.
3. Inspect the dirty data of the service.
This step helps you check whether the service is running as expected. If dirty data exists and cannot be cleared automatically, contact technical support to troubleshoot the issue. i. Log on to the dpbizalisa database. For more information, see Appendix: Log in to a database. ii. Check the dirty data of the service. Execute the following statements:

```
 select count(*) alisa_task_callback from dpbizalisa.alisa_task_callback where
task_id not in (select task_id from alisa_task);
 select count(*) alisa_task_release from dpbizalisa.alisa_task_release where
task_id not in (select task_id from alisa_task);
 select count(*) alisa_task_on_node from dpbizalisa.alisa_task_on_node where
task_id not in (select task_id from alisa_task);
```

### Inspect the BaseBizPhoenix

**service**

The BaseBizPhoenix service is used to schedule tasks. You need to check whether the metadatabase of the service needs to be cleared. This topic describes how to inspect the BaseBizPhoenix service.

**Procedure**

Perform the following steps to check whether the amount of historical data stored in the system is too large:
1. Log on to the dpbizphoenix database. For more information, see Appendix: Log in to a
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

### Inspect the BaseBizCdp

**service**

The BaseBizCdp service provides multiple features. For example, the service is used to manage data sources, parse data integration tasks, and start data integration tasks. This topic describes how to inspect the BaseBizCdp service.

**Procedure**

Perform the following steps to check whether the `t_instance` table has more than 100,000 data records:
1. Log on to the dwcdp database. For more information, see Appendix: Log in to a database.
2. Execute the select count(*) from t_instance; statement to check the amount of data in
the table.

**Result**

If the number of data records exceeds 100,000, the system may be affected, and you need to manually clear the data.

### Appendix: Log in to a

**database**

This topic describes how to log in to a database.

**Procedure**

To log in to a database, perform the following steps.
1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the BasicCluster details page.

**Note**

You must go to the cluster details page for the corresponding service to obtain the logon address of the database to which you want to log in. In this example, the base service is used. You need to select the service based on your business scenario.
3. On the **Resource Details** tab of the **Cluster Details** page, filter resources of the **db** type.
View the value in the Resource Application Result column of the corresponding database and obtain the name of and connection information about the database. Then, log in the database based on the connection information. and commands

## Common administration

**tools and commands**

### View the servers on which a

**service is deployed**

This topic describes how to view the servers on which a service is deployed.

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. On the Services tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page. In the Components section, click a service and view the servers
on which the service is deployed. and commands

### View cluster resources

This topic describes how to view the applications, resources, status, and version of a cluster.

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. Click the **Resource Details** tab. You can filter resources in the cluster by **Resource**
**Name**, **Related Version**, **Type**, and **Resource Status**.
Find the resource that you want to view and click the icon in the **Resource Application**
**Result** column to view the application details. For example, if you want to log in to the
database of a specific application, you can view detailed logon information about the database in the **Resource Application Parameters** message. and commands

### View service registration

**variables**

This topic describes how to view the registration variables of a service.

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. In the left-side navigation pane, choose **O&M Tools > Service Registration Variable**
**Dashboard**.
3. On the Service Registration Variable Dashboard page, switch the filter condition type to
search for the service that you want to view.
4. Find the service and click the
icon next to the value in the **Service Registration** column to view the details of the registration variables of the service.

**Note**

If a large amount of data exists, you can click the data displayed in the **Service**
**Registration** column to view the content in the Registration Variables message.

**Change the domain name of a service**

If you use Apsara Stack V3.18.2 or later, the domain names in the registration information of specific services are changed. The following table describes the changes.

| Baseline | Service name | Before change | After change |
|---|---|---|---|
|   | base-biz- commonbase | ide.${global:internet- domain} | ide.${global:console- private-domain} |
|   | base-biz- dashboard | dashboard.${global:interne t-domain} | dashboard.${global:consol e-private-domain} |
|   | base-biz-diide | di.${global:internet- domain} | di.${global:console- private-domain} |
|   | base-biz-dmc | dmc.${global:internet- domain} | dmc.${global:console- private-domain} |
|   | base-biz-sso | cloudsso.${global:internet- domain} | cloudsso.${global:console- private-domain} |

and commands

|   | base-biz- wkbench | wkbench.${global:internet- domain} | wkbench.${global:console -private-domain} |
|---|---|---|---|
|   | dataworks-bff | bff.${global:internet- domain} | bff.${global:console- private-domain} |
|   | dataworks-cdn | ms.cdn.${global:internet- domain} | dataworks- cdn.${global:console- private-domain} |
| service-base- baseBizApp |   |   |   |
|   | dataworks- dataos-panel | setting.${global:internet- domain} | setting.${global:console- private-domain} |
|   | dataworks-dsm- guard | approval.${global:internet- domain} | approval.${global:console- private-domain} |
|   |   | guard.${global:internet- domain} | guard.${global:console- private-domain} |
|   | dataworks-lsp | lsp.${global:internet- domain} | lsp.${global:console- private-domain} |
|   | dataworks- message-center | message.${global:internet- domain} | message.${global:console -private-domain} |
|   | dataworks- navigation | nav.${global:internet- domain} | nav.${global:console- private-domain} |
|   | dataworks- nodemarket | nodemarket.${global:intern et-domain} | nodemarket.${global:cons ole-private-domain} |
|   |   | ms.${global:internet- domain} | ms.${global:console- private-domain} |
|   |   | dwexcel-pivot- server.ms.${global:internet -domain} | dwexcel-pivot-server- ms.${global:console- private-domain} |
|   |   | pg- service.ms.${global:interne t-domain} | pg-service- ms.${global:console- private-domain} |
|   |   | morse- engine.ms.${global:interne t-domain} | morse-engine- ms.${global:console- private-domain} |

and commands

|   |   | dw-emr-meta- manager.ms.${global:inter net-domain} | dw-emr-meta-manager- ms.${global:console- private-domain} |
|---|---|---|---|
|   | dataworks- plugin |   |   |
|   |   | mysql- service.ms.${global:interne t-domain} | mysql-service- ms.${global:console- private-domain} |
|   |   | model.${global:internet- domain} | N/A |
|   |   | model.${global:intranet- domain} |   |
|   |   | indicator.${global:internet- domain} |   |
|   |   | indicator.${global:intranet- domain} |   |
|   |   | dsd.${global:internet- domain} |   |
|   |   | dsd.${global:intranet- domain} |   |
|   |   | layer.${global:internet- domain} |   |
|   |   | layer.${global:intranet- domain} |   |
| service-base- dschain | dschain | dschain.dw.${global:region }.${global:internet- domain} | dschain- dw.${global:console- private-domain} |
|   |   | dschain- intra.dw.${global:region}.$ {global:intranet-domain} | dschain-intra- dw.${global:intranet- domain} |
|   |   | datastudio-er-model- web.ms.${global:internet- domain} | datastudio-er-model-web- ms.${global:console- private-domain} |

| DataWorks |   |   |   |
|---|---|---|---|
| service-base- datablau | datablau-plugin |   |   |
|   |   | datastudio-er-model- api.ms.${global:internet- domain} | datastudio-er-model-api- ms.${global:console- private-domain} |
|   |   | datablau- modelstore.ms.${global:int ernet-domain} | datablau-modelstore- ms.${global:console- private-domain} |
|   |   | datablau- store.ms.${global:internet- domain} | datablau-store- ms.${global:console- private-domain} |
|   |   | datablau- central.ms.${global:interne t-domain} | datablau-central- ms.${global:console- private-domain} |
| service-base- modelengine | dataworks- modelengine | model- engine.ms.${global:interne t-domain} | model.${global:console- private-domain} |
| service-base- dsgadvanced | dsg | dsgadvanced.${global:inter net-domain} | dsgadvanced.${global:con sole-private-domain} |
| service-base- migassist | dataworks- migration | migration.${global:internet -domain} | migration.${global:consol e-private-domain} |
| service-dataworks- holostudio | dataworks- holostudio | holostudio.${global:interne t-domain} | holostudio.${global:consol e-private-domain} |
| service-dataworks- graphstudio | dataworks- graphstudio | gs.${global:internet- domain} | gs.${global:console- private-domain} |
| service-dataworks- streamstudio | ssweb | ss.${global:internet- domain} | ss.${global:console- private-domain} |
| service-dataworks- dqc | base-biz- dqcsupervisor | dqc.${global:internet- domain} | dqc.${global:console- private-domain} |
| service-dataworks- dataassets | dataworks- dataassets | dataassets.${global:interne t-domain} | dataassets.${global:consol e-private-domain} |
| service-dataworks- asset | dataworks-asset | assetv2.${global:internet- domain} | assetv2.${global:console- private-domain} |

and commands

| service-dataworks- dataservice | dataservice web _ | ds.${global:internet- domain} | ds.${global:console- private-domain} |
|---|---|---|---|
| service-dataworks- realtime | dwexcel | da.${global:internet- domain} | da.${global:console- private-domain} |
| service-dataworks- dsgapp | dsg | dsg.${global:internet- domain} | dsg.${global:console- private-domain} |
| service-dataworks- openplatform | dataworks- openplatform | openplatform.${global:inter net-domain} | openplatform.${global:con sole-private-domain} |
| service-dataworks- governance | dataworks- datagovernance | dgc.${global:internet- domain} | dgc.${global:console- private-domain} |

### Commands to restart services

Enter the container that runs the service as an admin user, and then run the following commands to restart services.

**Note**

Only admin users can run the following commands to restart the service. To restart the base-biz-cdp service, run the `/home/admin/cdp_server/bin/appctl.sh` `restart` command. To restart the base-biz-gateway service, run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/serverctl
```

`restart` command. To restart other services, run the `/home/admin/base-biz-[application name]/bin/jbossctl` `restart` command. For example, to restart the base-biz-alisa service, run `/home/admin/base-biz-`

```
alisa/bin/jbossctl
       restart .
```

### View logs of a failed instance

This topic describes how to view logs of a failed instance in Operation Center.

**Procedure**

1. Log on to the DataWorks console.
2. On the DataStudio page, click
in the upper-left corner and choose **All Products >**
**Operation Center**.
3. On the **Dashboard** page, click **Failed** in the **Instances** section. The **Cycle Instance** page
appears. On this page, you can view all the instances that failed to run in the current workspace.
4. Click the target instance, and then right-click the failed node on the DAG that appears on
and commands the right side of the page.
5. Select **View Runtime Log**.

### Rerun multiple instances at a

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

### Stop multiple instances at a

**time**

You can use the batch stop feature of DataWorks to stop multiple instances at a time.

**Procedure**

1. Log on to the DataWorks console.
2. On the DataStudio page, click
in the upper-left corner and choose **All Products >**
**Operation Center**.
3. On the **Dashboard** page, click **Running** in the **Instances** section. The **Cycle Instance**
page appears. On this page, you can view all the running instances in the current workspace.

**Note**

You can stop only instances that are running.
4. Select the instances that you want to stop.
5. Choose **More > Stop** in the lower-left corner.
6. In the message that appears, click **Stop**.

### Commonly used Linux

**commands**

This topic describes the commonly used Linux commands.

**Display workloads in the Linux system: top**

and commands View the three numbers after load average, which indicate the workload averages for the last 5, 10, and 15 minutes, respectively. If you divide one of these numbers by the quantity of logical CPUs and the result is greater than 5, the Linux system is overloaded.

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

**Note**

The -C parameter is an uppercase letter. Set its value to a number. To search for a string in a specified file and display only the last few lines that contain the string, run the command in the following format:

```
grep -A Number of lines ["String"] [File name]
```

**Terminate processes: kill**

You can run the `kill -9` command with the PID of a process added at the end to terminate the process.

**docker commands**

List all containers: `docker ps -a` List the logs of a container: `docker logs [Container ID]` Log on to a container: `docker exec -it [Container ID] bash`

### View the slot usage of

**resource groups**

This topic describes how to view the slot usage of a resource group. Scenario: When a large number of nodes are waiting for resources in Operation Center, you can run a set of commands to view the slot usage of each resource group. and commands First, log on to the base-biz-alisa database. In an Apsara Stack V3 environment, select base from the Project drop-down list on the Clusters page in Apsara Infrastructure Management. Locate the base-biz-alisa service whose type is db in the filtered results. Right-click the Result column and choose Show More from the shortcut menu to obtain the connection information of the database. Then, run a MySQL command to log on to the database based on the obtained information. Run the following command to view the top 10 nodes by execution duration:

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

## Process daily

**administration operations**

### Daily check

#### Check the service status and server

**information**

This topic describes how to view the basic information about a cluster, server status, and the number of servers at desired state.

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. In the left-side navigation pane, choose **Resource Management > Machines**.
3. On the Machines page, find the server that you want to manage and click **Machine Status**
**Dashboard** in the **Actions** column. On the page that appears, view the basic information
and process status of the server.

#### Check the status of a gateway server

This topic describes how to check the status of a gateway server.

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the BasicCluster details page.
perations
3. Click the Resource Details tab. On the **Resource Details** tab, enter **dpbizalisa** in the
**Resource Name** field, and filter resources of the **db** type.
4. Find the resource that you want to view and click the
icon in the Resource Application Result column to view the address, username, and password used to log in to the database.
5. Connect to the database and run the following MySQL command to query the node
information:

```
Select * from alisa_node;
```

If -1 or 0 is returned for the **active_type** or **live** parameter, the service is abnormal. In this case, contact Apsara Stack technical support.

#### Monitor service roles and servers

This topic describes how to view the details of monitored service roles and servers.

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used. perations
3. Click the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
Components Details page.
4. In the **Components** section, find the component that you want to manage and click its
name. On the right side of the page, view the servers on which the component is deployed.
5. Find the server that you want to manage and choose **Component Information > Metrics**
in the **Actions** column.
6. In the **Component Metrics** dialog box, view the information on the **Component Metrics**
and **Machine Metrics** tabs.

### View logs of the services

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

### Scale out the cluster that runs

**the base-biz-gateway service**

This topic describes how to scale out the base cluster that runs the base-biz-gateway service.

**Prerequisites**

The system is conducive to change. For example, make sure that the storage space is sufficient, and verify the prerequisites such as the permissions on the files, the owners and paths of the files, and the software version. The base cluster is at desired state and works as expected. A screenshot of the key initial configurations of the cluster is saved. IP addresses do not conflict. If you want to use a new buffer cluster for the scale-out operation, make sure that the IP addresses that Deployment Planner assigns to the servers in the cluster are not used in the current environment. This prevents exceptions due to IP address conflicts after the scale-out.

**Procedure**

1. Create a buffer cluster.
perations Skip this step if an existing buffer cluster has idle servers and the physical machine, memory, CPU, and disk size of the idle servers are the same as those of current servers that run the base-biz-gateway service. Note: In the scale-out procedure, use actual parameter values and IP addresses instead of the parameter values in this example.

**Note**

When you plan to scale out the cluster by using Deployment Planner, make sure that the name of the new buffer cluster is different from that of any existing buffer cluster. i. Copy and paste _tianji_imports to the /apsarapangu/disk3/u_disk/ directory of the OPS1 server and run the following command in the tianji_zhuque_sdk directory:

```
./tianji_zhuque_exchanger.py import --skip_packages -o ${Desired state of Apsara In frastructure Management} -c tianji_dest.conf
```

ii. Log in to the **Apsara Infrastructure Management console** . In the left-side navigation pane, choose **Resource Management > Product & Cluster O&M**. In the **Products** section of the Product & Cluster O&M page, find the **buffer** service. iii. Find the buffer cluster that you want to view and click Cluster Details in the Actions column to go to the details page of the cluster. On this page, view the status of servers in the cluster. iv. Run the following commands on the OPS1 server to call API operations to query scale-out information:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf ./tianji_clt machinestatus -c buffer --config clt2.conf
```

2. Scale in the buffer cluster by moving idle servers to the default cluster.

**Note**

You can use the default cluster to scale out the cluster that runs the base-biz-cdp and base-biz-gateway services. i. On the **Cluster Details** page, click the **Desired State Configuration** tab. perations ii. Click the **machine_group.conf** file. Make sure that the value of the **scalable** parameter is **true** for the new buffer cluster. iii. Run the following commands on the OPS1 server to scale in the buffer cluster:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf (If a message indicating that a soft link already exists appears aft er you run this command, proceed with the next command.) ./tianji_ops_tool.py contract_nc -c [buffer cluster name] -l [Hostname of the serve r to be removed], [Hostname of the server to be removed],.... --config clt2.conf -s [SRG name]
```

| Parameter | Description |
|---|---|
| -c | The name of the buffer cluster that you want to scale in, which starts with buffer-cluster. |
| -l | The list of hostnames of servers to be removed. Separate multiple hostnames with commas (,). |
| -s | The name of the service resource group (SRG) to which the servers belong. You can find the SRG name in the machine group.conf file _ of the buffer cluster. |
| -config | The tianji clt file. _ Note These commands cannot contain Chinese characters. |

iv. On the **Product & Cluster O&M** page, verify whether the servers are removed. perations v. Run the following commands on the OPS1 server to call API operations to query scale-in information:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf (If a message indicating that a soft link already exists appears aft er you run this command, proceed with the next command.) ./tianji_clt machinestatus -c default --config clt2.conf
```

vi. Go to the details page of the new buffer cluster and check whether the configurations of the servers are deleted from the machine_group.conf file. If the configurations of the servers still exist, delete them from the machine_group.conf file and then submit a rolling task.
3. Add servers to the base cluster and specify the name of the SRG to which the servers
belong. i. In the left-side navigation pane of the **Apsara Infrastructure Management** console, choose Resource Management > **Product & Cluster O&M**. ii. On the **Product & Cluster O&M** page, find the base cluster. iii. Click **Cluster Details** in the Actions column. On the Cluster Details page, verify whether the **Cluster clone parameters** is set to **True clone**. perations iv. Run the following commands to perform scaling. A rolling task is triggered after you run these commands.

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_des conf clt2.conf (If a message indicating that a soft link already exists appears aft er you run this command, proceed with the next command.)
```

To add servers to the cluster that runs the base-biz-gateway service, run the following command:

```
./tianji_ops_tool.py expand_nc -c [base cluster name] -s BaseGwGroup -l [machine1,machine2] --config clt2.conf
```

To add servers to the cluster that runs the base-biz-cdp service, run the following command:

```
./tianji_ops_tool.py expand_nc -c [BasicCluster cluster name] -s BaseCdpGwGroup -l [machine1,machine2] --config clt2.conf
```

v. Run the following command to call an API operation to query the scaling result:

```bash
curl http://127.0.0.1:7070/api/v3/column/m.*?m.id=[machine hostname]
```

vi. Log in to the OpsClone container and run the following command to view the clone status:

```
/home/tops/bin/python /root/opsbuild/bin/opsbuild.py acli list --status=ALL -n 1000 0 | vim -
```

4. Export the file that contains the information about the recent desired state.
After you complete the scale-out, export the file that contains the information about the recent desired state to Deployment Planner. This ensures the success of subsequent scalein and scale-out operations.
5. Verify the result.
i. Check the heartbeat logs of the servers. Open the terminal of each added server, log on to the gateway container, and then run the `tail -f /home/admin/alisatasknode/logs/heartbeat.log` command. If the logs are refreshed every 5 seconds, the heartbeat service is run as expected. perations ii. Query the database information and check whether the servers are online. Log in to the **Apsara Infrastructure Management console** . Go to the **Cluster Details** page of the base cluster, click the **Resource Details** tab, and then search for the **base-**
**biz-alisa** service of the **db** type. Click the
icon in the **Resource Application Result** column to view the database connection information. Connect to the database by executing a MySQL command and run the `select * from` alisa_node; command. The information about all servers that run the base-biz-gateway service appears. Check the values of the live and active_type parameters for each added server. If both the values are 1, the server is online.

### Scale in the cluster that runs

**the base-biz-gateway service**

**Usage notes**

If a server that runs the base-biz-gateway service fails, you can redeploy the server after it is repaired. If you want to remove a healthy server from the cluster that runs the base-biz-gateway service, perform the steps described in this topic.

**Note**

Before you remove a healthy server, perform an on-site check to ensure that the following conditions are met: No business applications are running on the server. The hostname of the server is correct.

**Procedure**

Perform checks before the scale-in
1. Perform an on-site check.
Collect the detailed information about the server to be removed and the cluster of the server.
2. Make sure that the value of the scalable parameter is true for the service resource group
(SRG) of the server to be removed. If the value is false, change it to true and submit a rolling task. perations Log in to the Apsara Infrastructure Management console. In the left-side navigation pane, choose **Resource Management > Product & Cluster O&M**. On the Product & Cluster O&M page, find the base cluster and click Cluster Details in the Actions column to go to the cluster details page. On the Desired State Configuration tab, click the
**machine_group.conf** file and verify whether the value of the scalable parameter is true.
Stop the base-biz-gateway service
1. Log in to the server to be removed and run the ps -ef|grep gateway command to obtain
the container ID of the base-biz-gateway service.
2. Run the `docker exec -it [container-id] bash` command to log on to the container.
3. Switch to the admin account and run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/servervtl stop  command.
```

4. Run the ps -ef|grep java command to check whether any process is running on the
server. If a running process exists, run the `kill -9 [process ID]` command to terminate the process.
5. Delete the program directories from the server.
Clean up the disks of the server. Skip this step if you want to clone the server.

```
#rm -rf /home/admin/*
#rm -rf /opt/taobao/tbdpapp/
```

Scale in the cluster by moving servers to the default cluster
1. Run the following commands on the OPS1 server to scale in the cluster:

```
cd /cloud/app/tianji-tools/PrivateCloudTool#/tianji_ops_tool/current ln -s /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controller/tianji_dest. nf clt2.conf (If a message indicating that a soft link already exists appears after y ou run this command, proceed with the next command.) ./tianji_ops_tool.py contract_nc -c [clusterName] -l [machineList] --config tianji_clt.conf -s [SRGname]
```

Parameters: -c: the name of the base cluster to be scaled in. To obtain the cluster name, go to the Product & Cluster O&M page and search for the base cluster. This parameter is required. -l: the hostname of the server to be removed. Separate multiple hostnames with commas (,). This parameter is required. perations -s: the name of the SRG to which the server to be removed belongs. This parameter is required. To view the SRG name, find the machine_group.conf file of the base cluster and view the SRG name in the file. -config: the tianji_clt configuration file. This parameter is required.
2. After you run the preceding commands, check whether the scale-in operation succeeds in
the Apsara Infrastructure Management console. You can follow the preceding steps to scale in a cluster by moving servers to the default cluster in Apsara Infrastructure Management. If you want to remove a server from Apsara Infrastructure Management, perform the steps described in the following section. Remove a server from Apsara Infrastructure Management
1. In the left-side navigation pane, choose **Resource Management > Machines**.
2. On the Machines page, click **Publish/Unpublish**. On the page that appears, click the
**Machine Unpublishing** tab.
3. Find the server that you want to remove.
i. Search for the server to be removed by hostname in the left-side Machines section. You can only remove servers in the default cluster. ii. If the server can be removed, the server is displayed on the right side of the page. Click
**Clear** in the Actions column to remove the server.
Verify the result
1. Check whether a server is moved from your cluster to the default cluster.
In the left-side navigation pane, choose **Resource Management > Machines**. On the Machines page, search for the server by hostname and check whether it is in the default cluster.
2. Check whether a server is removed from Apsara Infrastructure Management
In the left-side navigation pane, choose **Resource Management > Machines**. On the Machines page, search for the server by hostname. If you cannot find the server in the search results, the server is removed.
3. You can also run the following command on the OPS1 server to call the GetMachineInfo
operation to check whether the server is removed from Apsara Infrastructure Management:

```bash
curl http://127.0.0.1:7070/api/v5/GetMachineInfo?hostname=$hostname
```

perations

### Restart the BaseBizTenant

**service**

This topic describes how to restart the BaseBizTenant service on the Component Details page.

**Go to the Component Details page**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. On the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page.

**Restart the BaseBizTenant service**

1. In the Components section, find **BaseBizTenant** and click its name.
2. Find the server on which the service is deployed and click its name to go to the server
details page.
3. Click **Terminal** in the upper-right corner.
4. In the left-side navigation pane, click the server name. The configuration tab appears on
the right side of the page.
5. Enter docker ps|grep tenant in the code editor and press Enter to view the server ID.
perations
6. Enter `docker exec -it yourID bash` in the code editor and press Enter to go to the
corresponding container.

**Note**

You need to replace yourID with a container ID.
7. Enter `su - admin` in the code editor and press Enter to switch to the admin account.
8. Enter `/home/admin/base-biz-tenant/bin/jbossctl restart` in the code editor and press
Enter to restart the BaseBizTenant service. If the **OK** and **NGINX start Done** messages appear, the BaseBizTenant service is restarted.

### Restart the Redis service

This topic describes how to restart the Redis service on the Component Details page.

**Go to the Component Details page**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used. perations
3. On the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page.

**Restart the Redis service**

1. In the Components section, find the **Redis1** service and click its name.
2. Find the server on which the service is deployed and click its name to go to the server
details page.
3. Click **Terminal** in the upper-right corner.
4. In the left-side navigation pane, click the server name. The configuration tab appears on
the right side of the page.
5. Enter docker ps|grep redis in the code editor and press Enter to view the server ID.
6. Enter `docker exec -it yourID bash` in the code editor and press Enter to go to the
corresponding container.

**Note**

You need to replace yourID with a container ID.
7. Enter the following statements in the code editor and press Enter to restart the Redis
service:

```
/etc/init.d/redis restart /etc/init.d/redis-sentinel restart
```

perations

### Restart the BaseBizDmc

**service**

This topic describes how to restart the BaseBizDmc service on the Component Details page.

**Go to the Component Details page**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. On the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page.

**Restart the BaseBizDmc service**

1. In the Components section, find the **BaseBizDmc** service and click its name.
2. Find the server on which the service is deployed and click its name to go to the server
details page.
3. In the left-side navigation pane, click the server name. The configuration tab appears on
the right side of the page.
4. Enter docker ps|grep dmc in the code editor and press Enter to view the server ID.
perations
5. Enter `docker exec -it yourID bash` in the code editor and press Enter to go to the
corresponding container.

**Note**

You need to replace yourID with a container ID.
6. Enter `su - admin` in the code editor and press Enter to switch to the admin account.
7. Enter `/home/admin/base-biz-dmc/bin/jbossctl restart` in the code editor and press Enter
to restart the BaseBizDmc service. If the **OK** and **NGINX start Done** messages appear, the BaseBizDmc service is restarted.

### Restart the BaseBizAlisa

**service**

This topic describes how to restart the BaseBizAlisa service on the Component Details page.

**Go to the Component Details page**

1. Log in to the **Apsara Infrastructure Management** console.
perations Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. On the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page.

**Restart the BaseBizAlisa service**

1. In the Components section, find the **BaseBizAlisa** service and click its name.
2. Find the server on which the service is deployed and click its name to go to the server
details page.
3. Click **Terminal** in the upper-right corner.
4. In the left-side navigation pane, click the server name. The configuration tab appears on
the right side of the page.
5. Enter docker ps|grep alisa in the code editor and press Enter to view the server ID.
6. Enter `docker exec -it yourID bash` in the code editor and press Enter to go to the
corresponding container.

**Note**

You need to replace yourID with a container ID.
7. Enter `su - admin` in the code editor and press Enter to switch to the admin account.
8. Enter `/home/admin/base-biz-alisa/bin/jbossctl restart` in the code editor and press
Enter to restart the BaseBizAlisa service. perations If the **OK** and **NGINX start Done** messages appear, the BaseBizAlisa service is restarted.

### Restart the BaseBizPhoenix

**service**

This topic describes how to restart the BaseBizPhoenix service on the Component Details page.

**Go to the Component Details page**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. On the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page.

**Restart the BaseBizPhoenix service**

1. In the Components section, find the **BaseBizPhoenix** service and click its name.
2. Find the server on which the service is deployed and click its name to go to the server
details page. perations
3. Click **Terminal** in the upper-right corner.
4. In the left-side navigation pane, click the server name. The configuration tab appears on
the right side of the page.
5. Enter docker ps|grep phoenix in the code editor and press Enter to view the server ID.
6. Enter `docker exec -it yourID bash` in the code editor and press Enter to log on to the
corresponding container.

**Note**

You need to replace yourID with the container ID.
7. Enter `su - admin` in the code editor and press Enter to switch to the admin account.
8. Enter `/home/admin/base-biz-phoenix/bin/jbossctl restart` in the code editor and press
Enter to restart the BaseBizPhoenix service. If the **OK** and **NGINX start Done** messages appear, the BaseBizPhoenix service is restarted.

### Restart the

**BaseBizCdpGateway service**

This topic describes how to restart the BaseBizCdpGateway service on the Component Details page.

**Go to the Component Details page**

1. Log in to the **Apsara Infrastructure Management** console.
perations Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used.
3. On the **Services** tab, find the **base-baseBizApp** service and click its name to go to the
**Component Details** page.

**Restart the BaseBizCdpGateway service**

1. In the Components section, find the **BaseBizCdpGateway** service and click its name.
2. Find the server on which the service is deployed and click its name to go to the server
details page.
3. Click **Terminal** in the upper-right corner.
4. In the left-side navigation pane, click the server name. The configuration tab appears on
the right side of the page.
5. Enter docker ps|grep gateway in the code editor and press Enter to view the server ID.
6. Enter `docker exec -it yourID bash` in the code editor and press Enter to enter the
corresponding container.

**Note**

You need to replace yourID with a container ID.
7. Enter `su - admin` in the code editor and press Enter to switch to the admin account.
8. Enter `/home/admin/alisatasknode/target/alisatasknode/bin/serverctl restart` in the code
editor and press Enter to restart the BaseBizCdpGateway service. perations

### Restart the dataworks-

**dataservice service**

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of a cluster. In this example, the BaseExchangeCluster cluster is
used.
3. On the **Services** tab, find the **dataworks-dataservice** service and click its name to go to
the Component Details page.
4. On the Component Details page, click the component that you want to manage. The server
information is displayed on the right side of the page.
5. Click Terminal in the Actions column of a server. Run the docker ps|grep phoenix
command to obtain the container ID.
6. Run the `docker exec -it [Container ID] bash` command to log on to the container.
7. Switch to the admin account and run the `/home/admin/data-service-web/bin/jbossctl`
`restart` command to restart the service. perations If you are restarting the server, run the `/home/admin/data-service-server/bin/jbossctl` `restart` command.
8. If the service is in the **OK** state and the command output displays [ OK] -- SUCCESS at the
end, the dataworks-dataservice service is restarted.

### Restart the

**BaseBizCdpGateway service**

**Procedure**

1. Log in to the **Apsara Infrastructure Management** console.
Log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose

**Platform Operation > Apsara Infrastructure Management > Resource**

**Management**.
2. Go to the details page of your cluster. In this example, the BasicCluster cluster of the base
service is used. perations
3. On the Services tab, find the **base-baseBizApp** service and click its name to go to the
Component Details page.
4. In the Components section, find the BaseBizCdpGateway service and click its name. The
servers on which the BaseBizCdpGateway service is deployed appear on the right side of the page.
5. Click Terminal in the Actions column of a server. Run the docker ps|grep gateway
command to obtain the container ID. perations
6. Run the `docker exec -it [Container ID] bash` command to log on to the container.
7. Switch to the admin account and run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/serverctl restart  command to
```

restart the service.
8. After you restart the service, run the ps -ef|grep java command to check whether the
process is started.

**Note**

The preceding steps can be performed to restart the BaseBizCdpGateway service that is deployed in a container.

**Restart the BaseBizCdpGateway service deployed on physical**

**machines**

Perform the following steps to restart the BaseBizCdpGateway service that is deployed on physical machines:
1. Log in to the Apsara Infrastructure Management console, and go to the details page of the
BasicCluster cluster. Click the Resource Details tab. On the Resource Details tab, find the base-biz-alisa service of the db type and view the value in the Resource Application Result column to obtain the database connection information.
2. Run the select * from alisa_node; command in the database to view all information
about the BaseBizCdpGateway service. Then, you can log on to the cluster by using the obtained IP address and perform O&M operations on the BaseBizCdpGateway service.
3. Log in to the server on which the BaseBizCdpGateway service is deployed, switch to the
admin account, and then run the

```
 /home/admin/alisatasknode/target/alisatasknode/bin/serverctl restart  command.
```

perations

### Configure a resource group

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

3. Restart the base-biz-alisa service. For more information, see Restart the BaseBizAlisa
service.

**Note**

Both base-biz-alisa services need to be restarted. After one base-biz-alisa service is restarted, you can restart the other.

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

**Note**

After the change, one workspace has only two data entries whose is_default value is 1. If the preceding result is not displayed, the change is invalid. You must check the operations you have performed. The resource group belongs to a tenant so that you must change the default resource group for all workspaces that are created by the tenant.

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

### Configure a resource group

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

**Note**

The name can contain letters, digits, and underscores (_), and must start with a letter. ii. Click **Next**. iii. In the **Add Server** step, set the parameters as required. iv. Click **Next**. v. Perform the steps that are described in the **Install Agent** step.

**Note**

If an error occurs when you run the `install.sh` command or you need to run it again, run the rm –rf install.sh command in the same directory as the `install.sh` command to delete the generated file. Then, run the `install.sh` command again. The commands to run during the installation and initialization process differ for each user. Run relevant commands based on the instructions on the initialization interface. vi. Click **Next**. vii. In the **Test Connection** step, click **Refresh** and check the status of the ECS instance. viii. Click **Complete**. Resource groups that you have created on the Data Integration page can be used only in workspaces to which they belong. If you create a resource group in Workspace A, this resource group cannot be used in Workspace B. If you need to use a resource group in Workspace B, perform the preceding steps to create one in Workspace B.
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

**Note**

You must check the name of the ECS instance in the current region.
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

**Note**

**group_name** and **cluster_name** indicate the name and cluster name of
the custom resource group.

## Common issues and

**solutions**

### Nodes remain in the Pending

**(Resources) state**

**Symptom**

After you log on to the DataWorks console and click **Operation Center** in the upper-right corner of the console, the following issue occurs on the **Dashboard** page that appears: The instances of many recurring nodes remain in the Pending (Resources) state for a long period of time.

**Causes**

The issue may occur due to any one of the following four reasons: A gateway server is overloaded or offline and its status value is -1 in the database. The slots that handle concurrent jobs are fully occupied. The disk on a gateway server is full. The system time of servers in the base cluster is out of sync with the time of the Network Time Protocol (NTP) server.

**Solutions**

To resolve this issue, follow these steps: Check the status of a gateway server in the database. i. Log on to the database that hosts the base-biz-alisa service. In Apsara Stack V3, you can find the database endpoint from the resource list of the base cluster in Apsara Infrastructure Management. ii. Run the select * from alisa_node; command to check the values of the active_type and live fields. If the value of the live field is -1, the server is offline. If the value of the active_type field is -1, the server is overloaded.

**Note**

In either case, use SSH to connect to the gateway server and then check the server load and heartbeat. Run the `tail -f/home/admin/alisatasknode/logs/heartbeat.log` command to check the heartbeat of the gateway server. If the heartbeat log is updated every five seconds, the heartbeat is normal. Otherwise, check the configuration files for an error. Run the top command to display the load of the gateway server. The status of the server becomes -1 in the database as a result of the high load. In this case, check whether the CPU and memory are overloaded. You can find out the high-load processes in the output of the top command. You can run the ps -ef|greppid command to view processes of the specified node and identify which process causes the high load. To terminate a process, run the `kill -9 [process ID]` command. After the load drops, check whether the status of the server resumes to 1. Check whether the slots that handle concurrent jobs are fully occupied. Log on to the database that hosts the base-biz-alisa service and run the following statements:

```
select group_name,max_slot from alisa_group where group_name like '%default%'; select exec_target,sum(slot) from alisa_task where status=2 group by exec_target;
```

Compare the query results of the two statements. The first statement returns the maximum number of slots that can be assigned in each resource group. The second statement returns the number of slots that are occupied in each resource group. If the query results of the two statements are the same or almost the same, all resource groups run out of slots. In this case, if a large number of nodes are running, the subsequent nodes do not run until the preceding nodes are completed. Run the following statement to list the top 10 nodes that require the longest runtime:

```
select task_id,gateway,slot,create_time from alisa_task where status=2 and create_tim e>current_time order by create_time desc limit 10;
```

Log on to the gateway server and run the ps -ef|grep task_id command.

**Note**

Replace task_id in this command with one of the node IDs that are returned by the preceding SELECT statement. You can obtain the node name from the command output. Then, you can troubleshoot the node. If required, run the `kill -9` command to terminate the node and release resources immediately. Otherwise, new nodes can start only after the existing nodes are completed. Check whether the disk on a gateway server is full. Log on to the gateway server and run the `df -h` command to check whether the disk attached to /home/admin is full. If the disk is full, run the `du-sh` command to identify the files in the /home/admin directory that consume a large amount of space. You can manually remove some large log files from the /home/admin/alisatasknode/taskinfo/ directory. Check the system time of servers in the base cluster against the time of the NTP server. i. Log on to the database that hosts the base-biz-alisa service and run the select now(); command to view the current time of the database. ii. Check the system time of servers in the base cluster against the time of the database. iii. Run the date command on the servers to check whether the system time of each server is synchronized with the time of the database. If the time difference is greater than 30 seconds, the base-biz-alisa service may fail. In this case, synchronize the system time of servers in the base cluster with the time of the NTP server.

**Note**

In Apsara Stack V3, you can find the servers of the base cluster in the service list in the Apsara Infrastructure Management console and follow the proceeding steps to resolve the issue. Rename the phoenix folder to change it to a .bak file and restart the base-biz-alisa service. If the issue persists after you perform the preceding steps, run the following command on the gateway server:

```
cd /home/admin/alisatasknode/taskinfo/prevDay/phoenix/
```

**Note**

Replace prevDay in this command with the date of the previous day in the format YYYYMMDD, for example, 20180306. In this directory, run the `mkdir test` command. If the error message "Cannot create directory too many links" appears, the issue occurs because the number of subdirectories in the directory has reached the maximum and you cannot create more subdirectories. To resolve this issue, follow these steps: i. Rename the /home/admin/alisatasknode/taskinfo/20180306/phoenix directory as /home/admin/alisatasknode/taskinfo/20180306/phoenix.bak. ii. Run the following command to restart the base-biz-alisa service:

```python
sudo su admin -c "/home/admin/alisatasknode/target/alisatasknode/bin/serverctlrestart"
```

**Note**

This is a rare problem which tends to occur when a gateway server uses the third extended (ext3) file system.

### An out-of-memory (OOM) error

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

### A task does not run at the

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

**Note**

bizdate refers to the previous day, and gmtdate refers to the current day. Modify the command if needed before running it.

### What do I do if the number

**and usage of tables are not**

**displayed on the Data Map page?**

**Description**

The number and usage of tables are not displayed on the Data Map page.

**Solution**

1. Log in to the Apsara Infrastructure Management console and go to the details page of the
MaxCompute cluster.
2. Click the Resource Details tab. On the Resource Details tab, search for the base_admin
resource of the accesskey type.
3. Find the resource that you want to manage and view the value in the Resource Application
Result column to obtain the username and password.
4. Use the obtained username and password to log in to the base_meta project.

**Note**

To log in to the base_meta project, enter the domain name of the base_meta project in the address bar of your browser. By default, the domain name is in the following format: ide.Apsara Stack second-level domain.
5. Go to the Operation Center page of the base_meta project.
If a failed task exists, rerun the task. After the task is rerun, check whether data is displayed on the Data Map page as expected. If the task fails to be rerun, contact Apsara Stack technical support for troubleshooting.

### Logs are not automatically

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
