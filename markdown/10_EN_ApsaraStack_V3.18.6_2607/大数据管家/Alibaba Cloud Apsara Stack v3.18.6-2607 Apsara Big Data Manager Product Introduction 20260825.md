---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Big Data Manager Product Introduction 20260825"
product_version: "V3.18.6_2607"
doc_version: "20260825"
pdf_pages: 12
source_pdf: "f84d03c5103ea232_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Big Data Manager Product Introduction 20260825.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%AE%A1%E5%AE%B6/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20Big%20Data%20Manager%20Product%20Introduction%2020260825.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara Big Data Manager Product Introduction 20260825

## Table of Contents

- 1 Apsara Big Data Manager
  - 1.1 Features
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Features

## 1 Apsara Big Data Manager

Apsara Big Data Manager (ABM) is an operations and maintenance (O&M) platform tailored for big data products. ABM supports monitoring, management, and O&M in multiple dimensions, such as business, services, clusters, and hosts. Customer O&M teams or on-site personnel can use ABM to perform O&M operations on big data products and manage the products in an efficient and centralized manner.

### 1.1 Features

Apsara Big Data Manager (ABM) provides the following functional modules for big data products: Monitor, O&M, and Management. The Monitor module helps you monitor the status of big data products in real time. The O&M and Management modules allow you to perform O&M and management operations by using a graphical user interface (GUI) based on multiple dimensions, such as business, services, clusters, and hosts.

**Monitor**

**Dashboard**: allows you to view the overview of the key metrics of MaxCompute,
DataWorks, Realtime Compute, and DataHub.
**Repository**: allows you to view the resource usage of MaxCompute, DataWorks, and
DataHub.
**Health**: allows you to view the monitoring items of each big data service and the alerts of
different levels of urgency and check the monitoring items and alerts again after the alerts are handled.
**Reports**: allows you to view the inspection results of each big data service.

**O&M**

**Business**: provides O&M features that are dedicated for big data products.
MaxCompute: allows you to manage and optimize projects and jobs. DataHub: displays information about projects and topics in DataHub clusters. Realtime Compute: displays information about projects, jobs, and queues in Realtime Compute clusters. Elasticsearch: allows you to configure clusters and system settings. MaxCompute and DataWorks: allows you to configure and manage geo-disaster recovery in the configuration center. You can configure protection groups, rehearsal plans, and failure plans.
**Services**: displays O&M information about big data products. The information includes all
service roles in a cluster and the resource usage trend of each service role. This tab also provides specific information about the following big data products: MaxCompute: displays information about Control, Fuxi, Pangu, and Tunnel Service. DataWorks: displays information about data warehouses. DataWorks: displays information about data warehouses and data integration. DataHub: displays information about Control, Fuxi, and Pangu. Realtime Compute: displays information about Realtime Compute, Yarn, and Hadoop Distributed File System (HDFS).
**Clusters**: displays O&M information about clusters. The information includes the overview
and the health status of clusters.
**Hosts**: displays O&M information about hosts. The information includes the overview of
hosts.
**Jobs**: allows you to run jobs to perform O&M operations on big data products. Jobs are
classified into cron jobs and common jobs. The system can automatically run cron jobs at a specified time on a schedule. You can also manually run cron jobs. Common jobs can only be manually run.
**Health Checks**: includes Monitoring Configuration and Patrol Configuration.
The Monitoring Configuration tab provides various built-in check items for each big data service. The system automatically checks service faults and sends alerts based on the scheduling items and check items. If a check item does not meet the requirements, the system reports an alert. You can also configure custom scheduling intervals and modify the status of scheduling items and check items. The information displayed on this tab helps you identify and handle service faults at the earliest opportunity. The Patrol Configuration tab allows you to manage inspection items and inspection scenarios. The system manages inspection items at a specified time on a schedule. You can also manually manage inspection items. This helps prevent potential risks of major issues or service faults.
**Processes**: allows you to process manual tasks, define processes, and view process
instances.
**Operation Logs**: provides the records of all O&M operations that are performed in the
ABM console and the details of each operation. You can identify the causes of service faults based on the operation records.

### 1.2 Benefits

Apsara Big Data Manager (ABM) allows you to perform O&M operations on big data products and manage the products in a centralized manner. ABM helps enhance the stability of big data products, reduce O&M costs, and improve the efficiency of O&M. ABM provides benefits in various aspects, such as cluster health monitoring, resource usage analysis, and a graphical user interface (GUI) for O&M and management operations.

**Cluster health monitoring**

Allows you to monitor and configure the devices, resources, and services of the clusters of big data products, and collects and displays performance metrics of the clusters in real time.

**Resource usage analysis**

Displays the status of devices, resources, and services of clusters in real time, provides the historical data of the devices, resources, and services, and supports data aggregation and analysis to help you evaluate the health status of a cluster. If the evaluation result indicates potential risks in the cluster, related engineers can be immediately notified.

**GUI for O&M and management operations**

Provides a GUI on which you can view performance metrics and perform common O&M operations.

### 1.3 Scenarios

If you are using Apsara Stack and have deployed one or more big data services, you need to use Apsara Big Data Manager (ABM) to perform operations and maintenance (O&M) on these big data services.

**Apsara Stack Enterprise and big data services**

If you are using Apsara Stack Enterprise and have deployed one or more big data services, such as MaxCompute or DataWorks, you need to use ABM to perform O&M operations on these big data services.

**Apsara Stack Agility SE and big data services**

If you are using Apsara Stack Agility SE and have deployed one or more big data services, such as MaxCompute or DataWorks, you need to use ABM to perform O&M operations on these big data services.

**Apsara Stack Agility PaaS and big data services**

If you are using Apsara Stack Agility PaaS and have deployed one or more big data services, such as Alibaba Cloud Realtime Compute for Apache Flink, you need to use ABM to perform O&M operations on these big data services.

### 1.4 Features

This topic describes the features that are provided in the Apsara Big Data Manager (ABM) console.

| Service | Module | Feature | Description |
|---|---|---|---|
| ABM | Monitoring | Instrument cluster | Displays the key operation metrics of MaxCompute, DataWorks, StreamCompute, and DataHub, including cluster resource usage, traffic, and the running overview of jobs and tasks. |
|   |   | Resource Library | Displays the resource usage in MaxCompute, DataWorks, and DataHub. |
|   |   | Degree of health | Provides built-in scheduling and monitoring items and displays the monitoring items and alerts of ABM. |
|   |   | Report | Provides in-depth health check of ABM services, businesses, and capacity details, and generates reports. |
|   | Operation and maintenan ce | Business operation and maintenance | Allows you to view cron job statistics, specify geo- disaster recovery security configurations, manage protection groups, and perform routine drills and failovers. |
|   |   | Environment operation and maintenance | Allows you to view the basic components of a single host. |
|   |   | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |

|   | uction·Apsara |   |   |
|---|---|---|---|
|   | Manageme nt |   |   |
|   |   | Health Management | Allows you to configure monitoring and scheduling items, inspection items, inspection scenarios, and scenario combinations. |
|   |   | Process Services | Allows you to view details of manual tasks, process definitions, and process instances. |
|   |   | Operational Audit | Records the history of O&M operations and the details of each operation. |
|   | Monitoring | Degree of health | Provides built-in scheduling and monitoring items and displays the monitoring items and alerts of DataHub. |
|   |   | Report | Provides in-depth health check of DataHub services, businesses, and capacity details, and generates reports. |
| DataHub |   |   |   |
|   | Operation and maintenan ce | Business operation and maintenance | Allows you to view the information about DataHub projects, log sources, hot machine analysis, and data archiving tasks. |
|   |   | Service operation and maintenance | Allows you to perform O&M operations on control, Job Scheduler, and Apsara Distributed File System services, and displays the information about service instances. |
|   |   | Cluster O&M | Displays the overview, health, and machine list of DataHub clusters, and supports node scaling. |
|   |   | Host O&M | Allows you to view the host list and the overview and server role information of specified hosts. |
|   | Manageme nt | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |
|   |   | Health Management | Allows you to configure monitoring and scheduling items, inspection items, inspection scenarios, and scenario combinations. |
|   |   | Process Services | Allows you to view details of manual tasks, process definitions, and process instances. |
|   |   | Operational Audit | Records the history of O&M operations and the details of each operation. |

| DataWorks | Monitoring | Degree of health | Provides built-in scheduling and monitoring items and displays the monitoring items and alerts of DataWorks. |
|---|---|---|---|
|   |   | Report | Provides in-depth health check of DataWorks services, businesses, and capacity details, and generates reports. |
|   | Operation and maintenan ce | Service operation and maintenance | Provides a task instance list and multi-dimensional analysis for data integration services, and provides the slot management feature for data workshop services. |
|   |   | Cluster O&M | Displays the overview, health, and machine list of DataWorks clusters, and supports node scaling. |
|   |   | Host O&M | Allows you to view the host list and the overview and server role information of specified hosts. |
|   | Manageme nt | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |
|   |   | Health Management | Allows you to configure monitoring and scheduling items, inspection items, inspection scenarios, and scenario combinations. |
|   |   | Process Services | Allows you to view details of manual tasks, process definitions, and process instances. |
|   |   | Operational Audit | Records the history of O&M operations and the details of each operation. |
| Flink | Operation and maintenan ce | Business operation and maintenance | Displays the information about the Flink queue and the overall cluster resource inventory. |
|   | Manageme nt | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |
|   | Monitoring | Degree of health | Provides built-in scheduling and monitoring items and displays the monitoring items and alerts of Hologres. |
|   | ersion: 20260 |   |   |

| roduct Introd Data Manager | uction·Apsara |   |   |
|---|---|---|---|
| Hologres |   |   |   |
|   |   | Report | Provides in-depth health check of Hologres services, businesses, and capacity details, and generates reports. |
|   | Operation and maintenan ce | Service operation and maintenance | Allows you to perform O&M operations on Job Scheduler and Apsara Distributed File System services, and displays the overview, service roles, and node lists of these services. |
|   |   | Cluster O&M | Displays the overview, health, and machine list of Hologres clusters, and supports the synchronization of region information. |
|   |   | Host O&M | Allows you to view the host list and the overview and server role information of specified hosts. |
|   | Manageme nt | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |
|   |   | Health Management | Allows you to configure monitoring and scheduling items, inspection items, inspection scenarios, and scenario combinations. |
|   |   | Process Services | Allows you to view details of manual tasks, process definitions, and process instances. |
|   |   | Operational Audit | Records the history of O&M operations and the details of each operation. |
|   | Monitoring | Degree of health | Provides built-in scheduling and monitoring items and displays the monitoring items and alerts of MaxCompute. |
|   |   | Report | Provides in-depth health check of MaxCompute services, businesses, and capacity details, and generates reports. |
|   | Operation and maintenan ce | Business operation and maintenance | Allows you to perform project management, quota group management, job management, and business governance, including file merging, file archiving, and multi-dimensional resource analysis. |
|   |   | Service operation and maintenance | Allows you to perform O&M operations on control, Job Scheduler, Apsara Distributed File System, Lindorm Tunnel Service, and replication services, displays service instances, and allows you to modify service instance configurations. |

| MaxComp ute |   |   |   |
|---|---|---|---|
|   |   | Cluster O&M | Displays the overview, health, and machine list of MaxCompute clusters, and supports node scaling. |
|   |   | Host O&M | Allows you to view the host list and the overview and server role information of specified hosts. |
|   | Manageme nt | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |
|   |   | Recycling Management | Allows you to modify the rules for recycling custom chart data and default chart data. |
|   |   | Health Management | Allows you to configure monitoring and scheduling items, inspection items, inspection scenarios, and scenario combinations. |
|   |   | Process Services | Allows you to view details of manual tasks, process definitions, and process instances. |
|   |   | Operational Audit | Records the history of O&M operations and the details of each operation. |
| Stream Compute (Blink) | Analysis | Job Analysis | Provides diagnostic analysis of a single job and allows you to view the diagnostics history. |
|   |   | Queue Analysis | Provides diagnostic analysis of a single queue in a cluster and allows you to view the diagnostics history. |
|   | Monitoring | Degree of health | Provides built-in scheduling and monitoring items and displays the monitoring items and alerts of StreamCompute. |
|   |   | Report | Provides in-depth health check of StreamCompute services, businesses, and capacity details, and generates reports. |
|   | Operation and maintenan ce | Business operation and maintenance | Allows you to manage StreamCompute projects, jobs, and queues. |
|   |   | Service operation and maintenance | Displays the overview of Blink, YARN, and Hadoop Distributed File System (HDFS) services. |

|   |   | Cluster O&M | Displays the overview, health, and machine list of StreamCompute clusters, and supports node scaling. |
|---|---|---|---|
|   |   | Host O&M | Allows you to view the host list and the overview and server role information of specified hosts. |
|   | Manageme nt | Job Services | Allows you to run ordinary jobs and cron jobs, and view the job execution history. |
|   |   | Health Management | Allows you to configure monitoring and scheduling items, inspection items, inspection scenarios, and scenario combinations. |
|   |   | Process Services | Allows you to view details of manual tasks, process definitions, and process instances. |
|   |   | Operational Audit | Records the history of O&M operations and the details of each operation. |
