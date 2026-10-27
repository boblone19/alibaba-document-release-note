---
title: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Defined Storage Operations and Maintenance Guide 20250208"
product_version: "V3.18.3"
doc_version: "20250208"
pdf_pages: 152
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Defined Storage Operations and Maintenance Guide 20250208.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%AE%9A%E4%B9%89%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Cloud%20Defined%20Storage%20Operations%20and%20Maintenance%20Guide%2020250208.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Cloud Defined Storage Operations and Maintenance Guide 20250208

## Table of Contents

- 1 Log on to the Apsara Uni-manager Operations Console
- 2 Feature overview
- 3 Permission configuration
  - 3.1 Manage permissions on CDS-OPS
- 4 Service overview
- 5 Resource management
  - 5.1 Search for resources
  - 5.2 Manage clusters
  - 5.3 Manage hosts
  - 5.4 Manage hard disks
- 6 Storage management
  - 6.1 Before you begin
  - 6.2 Manage EBS clusters (EBS-2.0 and CDS-EBS)
    - 6.2.1 Overview of EBS clusters
    - 6.2.2 View the overview information about a cluster
    - 6.2.3 View capacity information
    - 6.2.4 Monitor clusters
      - 6.2.4.1 View cluster monitoring information
      - 6.2.4.2 View monitoring data of BlockServer nodes
      - 6.2.4.3 View PANGU monitoring data
    - 6.2.5 Configure clusters
      - 6.2.5.1 Configure block rebalance
      - 6.2.5.2 Configure the EC mode
      - 6.2.5.3 Configure PANGU Service
    - 6.2.6 Manage services
      - 6.2.6.1 Manage BlockMaster nodes
      - 6.2.6.2 Manage BlockServer nodes
      - 6.2.6.3 Manage snapshot servers
      - 6.2.6.4 Manage PANGU Service
    - 6.2.7 Manage storage sets
    - 6.2.8 Manage disks
    - 6.2.9 Hot migration of disks
    - 6.2.10 Execute canary O&M tasks
  - 6.3 Manage EBS clusters (EBS-1.0)
    - 6.3.1 Overview of EBS clusters
    - 6.3.2 Cluster overview
    - 6.3.3 View capacity information
    - 6.3.4 Manage services
      - 6.3.4.1 View the information about a RiverCluster
      - 6.3.4.2 View the information about a RiverServer
      - 6.3.4.3 Manage PANGU Service
  - 6.4 Manage OSS clusters
    - 6.4.1 Overview of OSS clusters
    - 6.4.2 Cluster overview
    - 6.4.3 View capacity information
    - 6.4.4 Monitor clusters
      - 6.4.4.1 View cluster monitoring information
      - 6.4.4.2 Check the health status of a cluster
      - 6.4.4.3 Execute a background task
      - 6.4.4.4 View the monitoring data of third-party modules
      - 6.4.4.5 View PANGU monitoring data
    - 6.4.5 Configure clusters
      - 6.4.5.1 Modify KV configurations
      - 6.4.5.2 Configure the EC type
      - 6.4.5.3 Configure execution time for background tasks
      - 6.4.5.4 Configure a global flag
      - 6.4.5.5 Configure PANGU Service
    - 6.4.6 Manage services
      - 6.4.6.1 Manage KV services
      - 6.4.6.2 Manage access-layer services
      - 6.4.6.3 Manage PANGU Service
    - 6.4.7 Manage buckets
      - 6.4.7.1 Manage bucket information
      - 6.4.7.2 Query bucket information
      - 6.4.7.3 Configure QoS information
    - 6.4.8 Manage synchronization configurations
      - 6.4.8.1 Manage synchronization processes
      - 6.4.8.2 Configure a cross-region synchronization process
      - 6.4.8.3 Configure a cross-cloud synchronization process
      - 6.4.8.4 View monitoring data of cluster synchronization
    - 6.4.9 O&M robots
      - 6.4.9.1 Manage O&M robots
      - 6.4.9.2 View historical O&M tasks
  - 6.5 Manage log storage clusters
    - 6.5.1 Overview of Simple Log Service clusters
    - 6.5.2 Cluster overview
    - 6.5.3 View capacity information
    - 6.5.4 View PANGU monitoring data
    - 6.5.5 Configure clusters
      - 6.5.5.1 Configure an EC type
      - 6.5.5.2 Configure PANGU Service
    - 6.5.6 Manage PANGU Service
- 7 Monitoring center
  - 7.1 View the custom dashboard
  - 7.2 Monitor resources
  - 7.3 Query storage metrics
  - 7.4 Query service monitoring data
- 8 Event Alerts
  - 8.1 Alert overview
  - 8.2 Alert management
    - 8.2.1 Learn the alert handling process
    - 8.2.2 Handle current alerts
    - 8.2.3 View alert history
  - 8.3 Event center
- 9 Routine Inspection
  - 9.1 Inspection Center
  - 9.2 SLA monitoring
- 10 Intelligent O&M
  - 10.1 Host O&M
    - 10.1.1 View all workflows
    - 10.1.2 Initiate a CDS Cluster Scale Up workflow
    - 10.1.3 Initiate a CDS Cluster Scale Down workflow
    - 10.1.4 Initiate a CDS Cluster Node Maintenance workflow
  - 10.2 Maintain disks
    - 10.2.1 Maintain corrupted disks
    - 10.2.2 Actively replace a disk
    - 10.2.3 View disk maintenance history
  - 10.3 Log Management
    - 10.3.1 Collect log data
    - 10.3.2 Query logs
- 11 System Management
  - 11.1 View plug-in information
  - 11.2 View tasks
  - 11.3 Query audit logs
  - 11.4 System Cleanup
    - 11.4.1 Manage cleanup configurations
    - 11.4.2 Clear tasks
- 12 Data Service
  - 12.1 Manage CSG

ager Operations Console

## 1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key. ager Operations Console

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and Traditional Chinese are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. ager Operations Console The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log On**.

## 2 Feature overview

Cloud Defined Storage (CDS)-OPS is a centralized O&M platform for CDS. CDS-OPS allows you to perform routine O&M on storage clusters and the services that are deployed in the storage clusters, such as Object Storage Service (OSS), Elastic Block Storage (EBS), and Simple Log Service. This topic describes the features of CDS-OPS. You can use these features based on your business requirements.

> **Note:** If you have questions when you use the features of CDS-OPS, contact Apsara Stack technical support.

**Service overview**

On the CDS-Overview page, you can view the overall information of CDS, such as the total capacity usage, current alerts, used capacity distribution in different storage services, hardware resources, storage resources, and cluster status. This way, you can understand the overall information about CDS and handle exceptions at the earliest opportunity. For more information, see Service overview.

**Resource management**

You can use the resource management features to query the information about resources, such as clusters, hosts, and hard disks and manage these resources. The following table describes the features.

| Feature | Operation | Description | References |
|---|---|---|---|
| Resource search | Search for resources | On the Resource Search page, you can search for resources by entering a keyword in the search box. The system searches for all resources whose names or IDs contain the keyword in fuzzy match mode. You can also search for resources based on the host IP addresses, hostnames, cluster names, serial numbers of hard disks, frontend IDs of cloud disks, or bucket names in exact match mode. | Search for resources |
| Cluster management | Manage clusters | On the Cluster page, you can view all the clusters that are managed by CDS- OPS. You can also click the name of a cluster to view the details of the cluster, such as the attributes, monitoring data, hosts that belong to the cluster, cluster load, capacity analysis results, and resource roles. If you need to increase or decrease the number of physical hosts in a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Up or CDS Cluster Scale Down workflow. | Manage clusters |

| Host management | Manage hosts | On the Host page, you can view the hosts of all clusters and click the name of a host to view the details of the host, such as the attributes, monitoring data, hard disks, cluster to which the host belongs, and resource roles. If a host in a cluster fails, you can initiate a CDS Cluster Node Maintenance workflow. | Manage hosts |
|---|---|---|---|
| Hard disk management | Manage hard disks | On the Hard Disk page, you can view the information of hard disks in all clusters. You can also click the name of a hard disk to view the details of the hard disk, such as the chunk information, disk type, disk status, host to which the disk belongs, and resource roles. If a hard disk drive (HDD) fails, you can set the HDD status and replace the HDD. | Manage hard disks |

**Storage management**

You can use the storage management features to manage the capacity usage, alerts, and clusters of services such as EBS, OSS, and Simple Log Service. The following table describes the storage management features.

> **Note:** The features supported by a cluster vary based on the cluster type. The actual features that are available prevail.

| Feature | Operation | Description | References |
|---|---|---|---|
|   | Overview of OSS clusters | On the Cluster O&M page of OSS clusters, you can view the total capacity usage, current alerts, number of buckets, and number of objects of OSS clusters. You can also view the information about the deployed OSS clusters to understand the overall information about the clusters and handle exceptions at the earliest opportunity. | Overview of OSS clusters |
|   | Cluster overview | On the Overview tab of an OSS cluster, you can view the information about the cluster and the top 10 buckets from different dimensions. | Cluster overview |
|   | View capacity information | You can view the logical capacity usage, physical capacity usage, capacity distribution, and physical capacity usage trend of an OSS cluster based on your business requirements. | View capacity information |

|   | Monitor clusters | On the Monitor tab of an OSS cluster, you can view and manage the monitoring data, health status of the cluster, status of background tasks, and third-party monitoring data. | View cluster monitoring information Check the health status of a cluster Execute a background task View the monitoring data of third-party modules View PANGU monitoring data |
|---|---|---|---|
| OSS-1.0 and CDS-OSS cluster management |   |   |   |
|   | Configure clusters | O&M engineers can configure cluster settings such as the KV configurations, erasure coding (EC) type, execution time of background tasks, and global flags. | Modify KV configurations Configure the EC type Configure execution time for background tasks Configure a global flag Configure PANGU Service |
|   | Manage services | You can manage KV services, access- layer services, and PANGU Service for a cluster. | Manage KV services Manage access- layer services Manage PANGU Service |

|   | Manage bucket information | On the Bucket Details page, you can query buckets by cluster or location. You can also go to the Bucket Query page and query buckets by Apsara Stack tenant account, user ID (UID), or bucket name. After you query a bucket, you can view the bucket details and manage the bucket. You can configure quality of service (QoS) policies for users or buckets to limit the total upstream traffic, total downstream traffic, and total queries per second (QPS) of users or buckets. QoS policies prevents a single user or bucket from occupying excessive network and system resources. | Manage bucket information |
|---|---|---|---|
|   | Manage synchronization configurations | After you configure cross-region or cross-cloud configuration processes, you can the cross-region or cross-cloud configuration processes of a specific source cluster. For example, you can view the synchronization status, configure QoS policies, configure the number of subqueues, and view the monitoring data of cluster synchronization. | Manage synchronization tasks Configure a cross-region synchronize task Configure a cross-cloud synchronize task View monitoring data of cluster synchronization |
|   | Manage O&M robots and O&M history | You can use O&M robots to perform automatic O&M tasks, such as intelligent analysis and diagnostics on faulty machines, automatic adjustment of KV recycle bins, intelligent analysis and diagnostics on frequent issues, automatic remediation of KV CheckReady failures, automatic write prohibition and recovery of PANGU, and emergency solutions for file damages. O&M robots simplify O&M operations and improve O&M efficiency. On the O&M History tab, you can view the history of different types of O&M tasks that are automatically executed by O&M robots. | Manage O&M robots View historical O&M tasks |

|   | Overview of EBS clusters | On the Cluster O&M page of EBS clusters, you can view the total capacity usage, current alerts, number of disks, and number of snapshots of the EBS clusters. You can also view the information about the deployed EBS clusters to understand the overall information about the clusters and handle exceptions at the earliest opportunity. | Overview of EBS clusters |
|---|---|---|---|
|   | Cluster overview | On the Overview tab of an EBS cluster, you can view the physical capacity usage, number of disks, number of snapshots, and inspection items of the cluster. This way, you can understand the overall information about the cluster and handle exceptions at the earliest opportunity. | View the overview information about a cluster |
|   | View capacity information | On the Capacity tab of an EBS cluster, you can view the logical capacity usage, physical capacity usage, capacity distribution, physical capacity usage trend, and inventory capacity trend of the EBS cluster. | View capacity information |
|   | Monitor clusters | On the Monitor tab of an EBS cluster, you can view the performance monitoring data of the cluster from multiple dimensions, such as the cluster, BlockServer nodes, and PANGU. | View cluster monitoring information View monitoring data of BlockServer nodes View PANGU monitoring data |
|   | Configure clusters | On the Configure tab of an EBS cluster, O&M engineers can configure cluster settings such as block rebalance, EC type, and PANGU based on your business requirements. | Configure block rebalance Configure the EC mode Configure PANGU Service |

| EBS-2.0 and CDS-EBS cluster management |   |   |   |
|---|---|---|---|
|   | Manage services | On the Service tab of an EBS cluster, you can manage the primary BlockMaster node, BlockServer nodes, snapshot servers, and PANGU Service. | Manage BlockMaster nodes Manage BlockServer nodes Manage snapshot servers Manage PANGU Service |
|   | Manage storage sets | On the Storage Set page, you can search for an EBS storage set by cluster name or storage set ID, and then perform the following operations to manage the storage set: view information about the storage set, view disks in the storage set, view capacity usage in each partition of the storage set, and modify the clusters in each partition of the storage set. | Manage storage sets |
|   | Manage disks | On the Disk page, you can view the information about disks of all clusters, such as the attributes, monitoring data, and the clusters to which disks belong. EBS-2.0 clusters and CDS-EBS clusters allow you to modify the maximum IOPS and throughput of disks in the clusters. | Manage disks |
|   | Migrate disks (hot migration) | On the Hot Migration of Disks page, you can create hot migration tasks to migrate disks between EBS clusters. The disks remain available during the migration. This improves the O&M efficiency of disks. | Hot migration of disks |

|   | Perform canary O&M | You can initiate canary O&M tasks to run a common O&M command on multiple hosts at a time. This simplifies O&M operations and minimizes the impact in case of a failure. You can stop command execution at the earliest opportunity if the exit code of the command result is not 0. You can also specify a speed and an observation period for a canary O&M task. This way, the canary O&M task can run the O&M command at an appropriate speed on the specified hosts. During the execution of a canary O&M task, you can view the progress and results in real time. | Execute canary O&M tasks |
|---|---|---|---|
| EBS-1.0 cluster management | Overview of EBS clusters | On the Cluster O&M page of EBS clusters, you can view the total capacity usage, current alerts, number of disks, and number of snapshots of the EBS clusters. You can also view the information about the deployed EBS clusters to understand the overall information about the clusters and handle exceptions at the earliest opportunity. | Overview of EBS clusters |
|   | Cluster overview | On the Overview tab of an EBS cluster, you can view the physical capacity usage, number of disks, number of snapshots, and inspection items of the cluster. This way, you can understand the overall information about the cluster and handle exceptions at the earliest opportunity. | Cluster overview |
|   | View capacity information | The physical capacity usage of a cluster shows the capacity usage of the cluster. O&M engineers can scale up or scale down the cluster based on the capacity usage of the cluster. | View capacity information |

|   | Manage services | You can manage the RiverCluster and RiverServer servers of a cluster. You can also manage PANGU Service for a cluster. | View the information about a RiverCluster View the information about a RiverServer Manage PANGU Service |
|---|---|---|---|
|   | Overview of Simple Log Service clusters | On the Cluster O&M page of Simple Log Service clusters, you can view the capacity usage, current alerts, and deployment information about Simple Log Service clusters. This way, you can obtain the overall cluster information and handle exceptions at the earliest opportunity. | Overview of Simple Log Service clusters |
| CDS-SLS cluster management |   |   |   |
|   | Cluster overview | On the Overview tab, you can view the top 10 Logstores with the highest traffic and all projects in a cluster. You can also search for a specific project, modify project configurations, and delete projects that you no longer use. | Cluster overview |
|   | View capacity information | On the Capacity tab, you can view the logical capacity usage, physical capacity usage, and physical capacity usage trend of a Simple Log Service cluster. | View capacity information |
|   | View PANGU monitoring data | You can view PANGU monitoring data to analyze the cluster status in real time. | View PANGU monitoring data |
|   | Configure clusters | You can configure the EC type or PANGU for a cluster based on the number of servers. | Configure an EC type Configure PANGU Service |
|   | Manage PANGU Service | You can manage meta servers, chunk servers, and file information based on your business requirements. | Manage PANGU Service |

**Monitoring center**

After you select resources on the Resource Monitoring page, you can view the details of the resources on the monitoring dashboard. Supported resources include clusters, hosts, and disks. For more information, see View the custom dashboard, Monitor resources, Query storage metrics, and Query service monitoring data.

**Event alerts**

You can use the alert management and event center features to manage alerts and logs for clusters. The following table describes the features.

| Feature | Operation | Description | References |
|---|---|---|---|
| Alert overview | Alert overview | On the Alert Overview page, you can view the current alerts, alert statistics, and alert history. | Alert overview |
| Alert management | Handle current alerts | When alerts are triggered in the system, you can view the list of alerts and the details of an alert, such as the alert name, alert description, alert source, cluster name, alert severity, and user who confirmed the alert. We recommend that you handle alerts at the earliest opportunity by confirming or clearing the alerts based on your business requirements. | Learn the alert handling process Handle current alerts |
|   | View alert history | Alerts that are automatically or manually cleared are displayed on the Alert History page. You can view the information about the alerts within the specified time range, including the alert name, service, cluster name, description, source name, auto recovery status, confirmation status, and recovery time. | View alert history |
| Event center | Event center | You can view the events generated for EBS clusters of all versions in the event center. EBS versions include EBS-1.0, EBS-2.0, and CDS-EBS. | Event center |

**Routine inspection**

Routine inspection allows you to inspect clusters on a regular basis.

| Feature | Operation | Description | References |
|---|---|---|---|
| Routine inspection | Inspection center | By default, the system uses built-in inspection items to regularly inspect clusters. On the Inspection Center page, you can view the information about the latest inspection results of different inspection items and manually run inspection tasks. | Inspection Center |

|   | SLA monitoring | The system monitors key service level agreement (SLA) metrics of CDS in real time. This provides availability monitoring guarantee for scenarios such as software update, configuration change, and service O&M. This allows you to detect system exceptions at the earliest opportunity, and minimizes the impact when exceptions occur. | SLA monitoring |
|---|---|---|---|

**Intelligent O&M**

You can use the host O&M feature to perform intelligent O&M on clusters, use the log management feature to maintain logs, and use the hard disk maintenance feature to view the information about faulty hard disks in real time. You can hot replace faulty hard disks after the data of the faulty hard disks is backed up. The following table describes the features.

| Feature | Operation | Description | References |
|---|---|---|---|
| Host O&M | View all workflows | On the All Workflows tab of the Host O&M page, you can view the details of the scale-up, scale-down, and node maintenance workflows of different clusters. You can also manage the workflows based on your business requirements. | View all workflows |
|   | Initiate a CDS Cluster Scale Up workflow | If you need to add physical hosts to a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Up workflow to scale up the cluster. You can use the workflow to track the scale-up progress. This simplifies O&M operations and improves O&M efficiency. | Initiate a CDS Cluster Scale Up workflow |
|   | Initiate a CDS Cluster Scale Down workflow | If you need to remove physical hosts from a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Down workflow to scale down the cluster. You can use the workflow to track the scale- down progress. This simplifies O&M operations and improves O&M efficiency. | Initiate a CDS Cluster Scale Down workflow |
|   | Initiate a CDS Cluster Node Maintenance workflow | If you need to troubleshoot issues for a faulty physical host in a cluster, you can initiate a CDS Cluster Node Maintenance workflow. You can use the workflow to track the progress of node maintenance. This simplifies O&M operations and improves O&M efficiency. | Initiate a CDS Cluster Node Maintenance workflow |

| Log management | Collect log data | The system stores and indexes logs of key services in a centralized manner. You can query logs within a specific time range by service type, project, and storage service. | Collect log data |
|---|---|---|---|
|   | Query log data | The system stores and indexes logs of key services in a centralized manner. You can query logs within a specific time range by service type, project, and storage service. | Query logs |
| Hard disk maintenance | Maintain hard disks | When a hard disk drive (HDD) or Non- Volatile Memory Express (NVMe) solid- state drive (SSD) of a chunk server fails, you can view the information about the disk in real time and initiate disk replacement and disk hot maintenance after the data of the disk is backed up. If a healthy hard disk needs to be replaced because of capacity upgrade, performance upgrade, or routine maintenance, O&M engineers can initiate a disk replacement workflow. After the disk hot maintenance is complete, you can view the maintenance history of the disk. | Disk maintenance |

**System management**

You can use the system management features to manage system plug-ins and service logs. The following table describes the features.

| Feature | Operation | Description | References |
|---|---|---|---|
| Plug-in management | View plug-in information | By default, the system registers the deployed Apsara Stack data services, such as Cloud Storage Gateway (CSG). You can use the plug-in management feature to manage the registered Apsara Stack data services. | View plug-in information |
| Task management | View tasks | The system executes time-consuming tasks in an asynchronous manner. You can view the execution status of asynchronous tasks on the Tasks page. | View tasks |
| Service log management | Query audit logs | The audit logs record modifications to the system that are made by users. During security maintenance, you can filter the audit logs by using different keywords to quickly locate and handle security issues in a timely manner. | Query audit logs |

| System cleanup | Manage cleanup configurations | By default, the feature of automatically triggering compression tasks and cleanup tasks is disabled. You can manually enable the feature based on your business requirements. After you enable the auto trigger feature, the system automatically compresses service logs or clears tasks when the storage space reaches the specified threshold. | Manage cleanup configurations |
|---|---|---|---|
|   | Clear tasks | Task logs are stored on system disks. You can view the size, space usage, and compression status of the task logs based on the following aggregation dimensions: cluster, cluster and host, service, and service and component. You can compress or delete the logs based on your requirements to save storage on the system disks and improve the stability of system services. | Clear tasks |

**Data services**

| Feature | Operation | Description | References |
|---|---|---|---|
| CSG | Manage CSG | After you create and configure a Cloud Storage Gateway (CSG) instance, you can view the information about the CSG instance. You can also collect and download the OSS access logs that are generated by a Network File System (NFS) share or a Server Message Block (SMB) share, and the logs that are generated by sharing operations. | Manage CSG |

## 3 Permission configuration

### 3.1 Manage permissions on CDS-OPS

**OPS**

By default, the system administrator has the permissions to use all features of Cloud Defined Storage (CDS)-OPS. To meet the access control requirements for different users, the system supports the following roles for CDS-OPS: CDS administrator, CDS support, and CDS developer. These roles are granted different permissions on CDS-OPS.

**Roles for CDS-OPS**

A role is a collection of access permissions. You can assign different roles to different users to meet your requirements for system access control. The following table describes the permissions of the three roles for CDS-OPS.

| Role |   | Permission |
|---|---|---|
| CDS administrator |   | Has the permissions to perform most read operations and the permissions to perform a few modify operations. In most cases, the CDS administrator role is assigned to O&M staff to monitor the status of CDS. |
| CDS support |   | Has all the permissions of the CDS administrator role and the permissions to perform some regular read and write operations. |
| CDS developer |   | Has all the permissions of the CDS support role and the permissions to perform some high-risk O&M operations. Exercise caution when you assign this role to a user. |

**Add a user**

You can add a user and assign a role for CDS-OPS to the user to control the permissions of the user on CDS-OPS.

## 1 Log on to the Apsara Uni-manager Operations Console.

2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **User Management**. On the **User Management** tab,
click the **Users** tab.
4. On the **Users** tab, click **Add**.
5. In the **Add User** dialog box, configure the user information and click **OK**.

| Parameter | Description |
|---|---|

| Username | Enter a name for the user that you want to add. The name can be up to 48 characters in length and can contain digits, letters, underscores ( ), and _ hyphens (-). The email format is supported. |
|---|---|
| Password | Enter a password. The password must be 10 to 32 characters in length and must contain uppercase letters, lowercase letters, digits, and special characters. |
| Logon Policy | Select a logon policy. |
| Role | Set a user role, such as service O&M. |
| Department | Set a department. |
| Mobile phone | Enter a mobile phone number. |
| Email address | Enter an email address. |
| Allowed to Create AccessKey ID | Specify whether the user is allowed to create AccessKey pairs. |

## 4 Service overview

On the CDS-Overview page, you can view the overall information of Cloud Defined Storage (CDS), such as the total capacity usage, current alerts, used capacity distribution in different storage services, hardware resources, storage resources, and cluster status. This way, you can understand the overall information of CDS and handle exceptions at the earliest opportunity.
1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, click **CDS-Overview**.
3. On the **CDS-Overview** page, view the following information of CDS.
Overview information On the CDS-Overview page, you can view the overall information of CDS, such as the capacity usage, current alerts, hardware resources, and storage resources. The following table describes the metrics.

| Metric | Description |
|---|---|
| Capacity Usage | The total physical capacity of all clusters, consumed capacity, the capacity allocated to each storage service, and the usage of the capacity allocated to each storage service. |
| Current Alerts | The number of alerts at each severity in all clusters and the most recent five alerts. You can click More or an alert severity to go to the Current Alert page. On the Current Alert page, you can view and handle the alerts. For more information, see Handle current alerts. |
| Hardware Resource | The total number of hosts, the numbers of healthy and unhealthy hosts, the total number of hard disks, and the numbers of healthy and unhealthy hard disks in all clusters. You can click the number on the right side of Total Servers to go to the Host page, where you can view and manage hosts. For more information, see Manage hosts. You can click the number on the right side of a hard disk category to go to the Hard Disk page, where you can view and manage disks. For more information, see Manage hard disks. |
| Storage Resource | The numbers of storage clusters, disks, and buckets in all clusters. You can click the number on the right side of a storage resource to manage the storage resource. |

Cluster status In the Cluster Status section, you can view the information about all clusters that are managed by CDS-OPS. The information includes the cluster name, cluster update time, cluster types such as CDS-EBS, CDS-EBS&CDS-OSS, OSS, CDS-OSS, and EBS-1.0, percentage of the consumed capacity, total capacity, and consumed capacity. Clusters can be sorted in ascending or descending order by cluster name, total capacity, or used capacity. By default, clusters are sorted in ascending order by cluster name. You can select another sort method based on your business requirements. You can perform the following operations to go to the Cluster O&M page on which you can manage and configure a storage cluster: Find the EBS-1.0, OSS, CDS-EBS, CDS-OSS, file storage, or Simple Log Service cluster that you want to manage and click **O&M** in the upper-right corner of the cluster card. Find the CDS-EBS or integrated CDS-OSS cluster, move the pointer over **O&M** and select **Elastic Block Storage** or **OSS**.

## 5 Resource management

### 5.1 Search for resources

On the Resource Search page, you can search for resources by entering a keyword in the search box. The system searches for all resources whose names or IDs contain the keyword in fuzzy match mode. You can also search for resources based on the host IP addresses, hostnames, cluster names, serial numbers of hard disks, frontend IDs of cloud disks, or bucket names in exact match mode.

**Background information**

The following table describes the resources that can be managed by CDS Ops.

| Resource | Condition for exact match | Description |
|---|---|---|
| Cluster | Cluster name | A group of hosts. |
| Host | Host IP address or hostname | A physical server in a cluster. |
| Hard disk | Serial number of a hard disk | A physical storage device that stores data in a host. |
| Cloud disk | Frontend ID | A block storage resource for Elastic Compute Service (ECS). Cloud disks use a distributed triplicate mechanism and support the erasure coding (EC) replica policy. |
| Bucket | Bucket name | A container for objects that are stored in Object Storage Service (OSS). Every object in OSS is contained in a bucket. |

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Resource Management > Resource**
**Search**.
3. On the **Resource Search** page, enter a keyword in the search box and select a resource
from the matched results.

> **Note:** Fuzzy match is used when you enter a keyword to search for resources. After you enter a keyword in the search box, all resources whose names or IDs contain the keyword are displayed. If you want to search for a resource in exact match mode, enter the full name or ID of the resource.

After you select a resource, you can view the basic information and topology of the resource. The displayed information varies based on the resource type. The actual information that is displayed prevails. Basic information On the **Basic Information** tab, view the basic information of the resource, such as the attributes, monitoring data, and resource roles. In the **Attributes** section, click a resource identifier, such as a hostname or cluster name. The details page of the resource appears. On the details page of the resource, you can view the information of the resource and manage the resource. Resource topology On the **Resource Topology** tab, view the attributes and topology of the resource. The following figure shows the topology of an integrated CDS cluster. Click **More** for a resource to view the details of the resource.

### 5.2 Manage clusters

On the Cluster page, you can view all the clusters that are managed in the Cloud Defined Storage (CDS)-OPS console. You can click the name of a cluster to view the details of the cluster, such as the attributes, monitoring data, hosts that belong to the cluster, cluster load, capacity analysis results, and resource roles. If you need to increase or decrease the number of physical hosts in a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Up or CDS Cluster Scale Down workflow.

**Manage clusters in the cluster list**

1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Resource Management > Cluster**.
3. On the **Cluster** page, view the clusters and perform operations on the clusters based on
your business requirements. The following table describes the operations.

| Operation | Description |
|---|---|
| View cluster information | View the information about a cluster in the cluster list, such as the cluster name, cluster type, services that are deployed in the cluster, cluster capacity, and the last time when the cluster was updated. |
| Search for a cluster | Search for a cluster based on the cluster name or cluster type. |

| Scale up a cluster | If you need to increase the number of physical hosts in a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Up workflow. Important You cannot scale up or scale down Elastic Block Storage (EBS)-1.0 clusters. Find the cluster that you want to manage and clickC luster Scale-up in the Actions column to initiate a CDS Cluster Scale Up workflow. For more information, see Initiate a CDS Cluster Scale Up workflow. |
|---|---|
| Scale down a cluster | If you need to decrease the number of physical hosts in a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Down workflow. Important You cannot scale up or scale down EBS-1.0 clusters. Find the cluster that you want to manage and clickC luster Scale-down in the Actions column to initiate a CDS Cluster Scale Down workflow. For more information, see Initiate a CDS Cluster Scale Down workflow. |
| Rename a cluster | To rename a cluster, perform the following steps: i. Find the cluster that you want to manage and clickE dit Name in the Actions column. ii. In the Edit Name dialog box, specify a new name for the cluster. iii. Then, click OK. |
| View clusters details | Click the name of the cluster that you want to manage. On theC luster Details page, view the cluster attributes, monitoring data, hosts, storage pools, and resource roles. For more information, see the View the details of a cluster section of this topic. |

**View the details of a cluster**

1. On the **Cluster** page, click the name of the cluster that you want to manage.
2. On the **Cluster Details** page, view the cluster attributes, monitoring data, hosts, storage
pools, and resource roles. View cluster attributes In the Attributes section, view the attributes of the cluster, such as the cluster name, cluster type, total capacity, remaining capacity, total number of physical hosts, total number of hard disks, and total number of chunk servers. View host information On the **Host** tab, view the information about all hosts in the cluster and perform operations based on your business requirements. View the information about a host In the host list, view the host name, cluster, IP address, number of CPU cores, memory, status, and type. Search for a host Search for a host based on the hostname, host status, or number of CPU cores. You can click **Host**, **Meta Server**, or **Chunk Server** in the upper-right corner of the Host tab to filter hosts. View the details of a host Click the name of the host that you want to manage. On the **Host Details** page, view the host attributes, monitoring data, hard disks, clusters, storage pools, and resource roles. For more information, see the "View the details of a host" section of the Manage hosts topic. View service information On the Service tab, view the information about the services deployed in the cluster, such as the service names, service status, and server roles. Find the service that you want to manage and click the value in the **Server Role** column. In the dialog box that appears, view the details of the server role, such as the server role name and deployment status of the host. Click **OK** to close the dialog box. View monitoring data On the **Monitor** tab, select a time range to view the monitoring data of the cluster, such as the CPU utilization, memory usage, load, and IOPS. Move the pointer over a trend chart to view the data at a specific point in time. The CPU chart displays the CPU utilization and the Memory chart displays the memory usage in percentage. The Load chart displays the actual load of the system. The IOPS chart displays the actual number of reads and writes per second. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image. View the cluster load On the **Cluster Load** tab, view the upstream network load, downstream network load, and CPU load of the physical hosts in the cluster. In the charts, the load data is collected based on a 15-minute cycle. The system calculates and displays the average throughput of the network bandwidth and the average CPU utilization of the physical hosts during the cycle. Move the pointer over a bar for a physical host in a chart to view the average load of the physical host in the corresponding cycle. The unit of the upstream network load and downstream network load is Mbit/s. The CPU load is displayed in percentage. View resource roles On the **Logical Resources** tab, view the resource roles of the cluster.

> **Note:** The displayed resource roles vary based on the storage services that are deployed in the cluster. The actual resource roles that are displayed prevail.

Click **O&M** in the upper-right corner of a resource role to view storage clusters and perform O&M operations on the storage cluster.

### 5.3 Manage hosts

On the Host page, you can view the hosts of all clusters and click the name of a host to view the details of the host, such as the attributes, monitoring data, hard disks, cluster to which the host belongs, and resource roles. If a host in a cluster fails, you can initiate a CDS Cluster Node Maintenance workflow.

**Manage hosts in the host list**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Resource Management > Host**.
3. On the **Host** page, view the hosts in the host list and perform operations on the hosts
based on your business requirements. The following table describes the operations that you can perform on the hosts.

| Operation | Description |
|---|---|
| View host information in the host list | In the host list, view the host name, cluster, IP address, number of CPU cores, memory, status, and type. |
| Search for a host | Search for a host based on the cluster to which the host belongs, hostname, status, or number of CPU cores. |
| Maintain a host | Find the host that you want to maintain and clickR epair in the Actions column to initiate a CDS Cluster Node Maintenance workflow. For more information, see Initiate a CDS Cluster Node Maintenance workflow. |
| View the details of a cluster | Click the name of the cluster that you want to manage. On the Cluster Details page, view the cluster attributes, monitoring data, hosts, storage pools, and resource roles. For more information, see the "View the details of a cluster" section of the Manage clusters topic. |
| View the details of a host | Click the name of the host that you want to manage. On theH ost Details page, view the host attributes, monitoring data, hard disks, clusters, storage pools, and resource roles. For more information, see the "View the details of a host" section of the Manage hosts topic. |

**View the details of a host**

1. In the left-side navigation pane, choose **CDS-Resource Management > Host**.
2. On the **Host** page, find the host whose details you want to view and click the hostname.
3. On the **Host Details** page, view the details of the host, such as the attributes, hard disks,
cluster to which the host belongs, monitoring data, and resource roles. View host attributes View the attributes of the host, such as the hostname, IP address, number of CPU cores, and memory size. View host capacity information On the **Capacity** tab, view the capacity usage of the host and the capacity information of each hard disk in the host. Capacity Usage: includes the total capacity, used capacity, and percentage of used capacity of all hard disks in the host. Hard Disk Capacity: includes the health status, mount path, percentage of used capacity, hard disk SN, and disk ID of each HDD in the host, as well as the health status, percentage of used capacity, hard disk SN, and disk ID of each SDD. View the information of hard disks On the **Hard Disk** tab, view all hard disks of the host and perform operations based on your business requirements. View the information of hard disks In the hard disk list, view the device name, cluster, host, type, model, SN, total capacity, and health status. Search for a hard disk Search for a hard disk based on the name or status of the hard disk. View the details of a hard disk Click the device name. On the **Hard Disk Details** page, view the hard disk attributes, monitoring data, and host information. For more information, see the "View the details of a hard disk" section of the Manage hard disks topic. View the details of a cluster Click the name of the cluster that you want to manage. On the **Cluster Details** page, view the cluster attributes, monitoring data, hosts, storage pools, and resource roles. For more information, see the "View the details of a cluster" section of the Manage clusters topic. View server roles On the **Server Role** tab, view the information of the server roles of the host, such as the server role names, service names, and status. View the information of the cluster to which the host belongs On the **Cluster** tab, view the information of the cluster to which the host belongs, such as the cluster name, cluster type, services deployed in the cluster, and cluster capacity. Click the name of the cluster that you want to manage. On the **Cluster Details** page, view the cluster attributes, monitoring data, hosts, storage pools, and resource roles. For more information, see the "View the details of a cluster" section of the Manage clusters topic. View monitoring data On the **Monitor** tab, select a time range to view the monitoring data of CPU, memory, load, IOPS, Network Time Protocol (NTP), and traffic. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image. View resource roles On the **Logical Resources** tab, view the resource roles of the host.

### 5.4 Manage hard disks

On the Hard Disk page, you can view the information of hard disks in all clusters. You can also click the name of a hard disk to view the details of the hard disk, such as the attributes, monitoring data, host to which the hard disk belongs, and resource roles. If an HDD fails, you can specify the HDD status and replace the HDD.

**Manage hard disks in the hard disk list**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Resource Management > Hard Disk**.
3. On the **Hard Disk** page, view the hard disks in the hard disk list and perform operations on
the hard disks based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Search for a hard disk | Search for a hard disk based on the cluster to which the hard disk belongs, host to which the hard disk belongs, hard disk name, or health status. |
| View the details of a hard disk | Click the device name. On the Hard Disk Details page, view the hard disk attributes, monitoring data, and host information. For more information, see the "View the details of a hard disk" section of the Manage hard disks topic. |
| View the details of a cluster | Click the cluster name. On the Cluster Details page, view the cluster attributes, monitoring data, hosts, storage pools, and resource roles. For more information, see the "View the details of a cluster" section of the Manage clusters topic. |
| View the details of a host | Click the host name. On the Host Details page, view the host attributes, monitoring data, hard disks, clusters, storage pools, and resource roles. For more information, see the "View the details of a host" section of the Manage hosts topic. |

| Set hard disk status | The hard disk status is normal in most cases. To disable a hard disk because of a hard disk error or release of an idle hard disk, you can set the hard disk status to Shut-down. In this case, the system initiates data replication. After the backup status changes to Completed, the hard disk can be safely disabled. If the hard disk does not experience an exception but still needs to be replaced, you can set the hard disk status to Error. In this case, the system initiates data replication. After the backup status changes to Completed, you can perform hot maintenance on the hard disk. i. Click Set Status in the Actions column of the hard disk. ii. In the Disk Status dialog box, select a hard disk state. Valid values: Normal: The hard disk is running properly. Shut-down: The hard disk is offline. Error: The hard disk experiences an exception and requires maintenance. iii. Click OK. |
|---|---|

**View the details of a hard disk**

1. In the left-side navigation pane, choose **CDS-Resource Management > Hard Disk**.
2. On the **Hard Disk** page, find the hard disk whose details you want to view and click the
name of the hard disk.
3. On the **Hard Disk Details** page, view the details of the hard disk, such as the attributes,
monitoring data, host to which the disk belongs, and resource roles. View hard disk attributes In the Attributes section, view the attributes of the hard disk, such as the name, type, model, serial number, total capacity, and health status. View the information of the host to which the hard disk belongs On the **Host** tab, view the information of the host to which the hard disk belongs, such as the hostname, cluster to which the host belongs, IP address, number of CPU cores, memory, status, and host type. Click the host name. On the **Host Details** page, view the host attributes, monitoring data, hard disks, clusters, storage pools, and resource roles. For more information, see the "View the details of a host" section of the Manage hosts topic. Click the cluster name. On the **Cluster Details** page, view the cluster attributes, monitoring data, hosts, storage pools, and resource roles. For more information, see the "View the details of a cluster" section of the Manage clusters topic. View monitoring data On the **Monitor** tab, select a time range to view the monitoring data of hard disk IOPS. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

## 6 Storage management

### 6.1 Before you begin

You can view, monitor, configure, manage, or maintain clusters of various storage services. Supported management operations vary based on the cluster type.

**Supported cluster types**

The following table describes the types of clusters that you can manage in Cloud Defined Storage (CDS) Ops.

> **Note:** Various services may be deployed in a cluster. In this case, the cluster belongs to multiple cluster types.

| Cluster type | Description |
|---|---|
| OSS cluster | Object Storage Service (OSS) is a secure, cost-effective, and highly reliable cloud storage service of Alibaba Cloud. OSS allows you to store and obtain various unstructured data objects, such as text, images, audio, and videos, over networks at any time. You can use CDS Ops to manage CDS-OSS clusters and OSS clusters, and to use all the OSS features. You can manage OSS clusters and PANGU clusters under the CDS-OSS module. For more information, see Overview of OSS clusters. For CDS-OSS clusters, the bases of PANGU clusters are PANGU 2.0. You can use CDS Ops to manage PANGU 2.0 clusters. For managed OSS clusters, the bases of PANGU clusters are PANGU 1.0. You cannot use CDS Ops to manage PANGU 1.0 clusters. |
| SLS cluster | Simple Log Service (SLS) is an all-in-one log data management service. You can use SLS to collect, consume, query, and analyze log data without the need to invest in in-house data collection or processing systems. SLS allows you to process large amounts of data to improve the O&M efficiency. You can use CDS Ops to manage CDS-SLS clusters. You can manage SLS clusters and PANGU clusters under the CDS-Log Storage module. For more information, see Overview of Simple Log Service clusters. |

| EBS cluster | Elastic Block Storage (EBS) provides the elastic block storage service in the distributed storage architecture and the on-premises disks of physical machines. You can use CDS Ops to manage CDS-EBS clusters and EBS-1.0 or EBS-2.0 clusters. For CDS-EBS clusters and managed EBS-2.0 clusters, you can use all the EBS features in CDS Ops. You can manage EBS clusters and PANGU clusters under the CDS-Elastic Block Storage module. For more information, see Overview of EBS clusters. For managed EBS-1.0 clusters, you can view and perform basic O&M operations on the clusters in CDS Ops. You can manage EBS clusters and PANGU clusters under the CDS-Elastic Block Storage module. For more information, see Overview of EBS clusters. |
|---|---|

**Usage notes**

OSS and EBS can be deployed together only in CDS clusters. You cannot use CDS Ops to manage PANGU clusters of the managed OSS types. Exercise caution when you perform high-risk operations, such as cluster configuration modification, server restart, service restart, and file deletion. To perform the preceding high-risk operations, contact Alibaba Cloud for technical support.

### 6.2 Manage EBS clusters (EBS-2.0 and CDS-EBS)

**and CDS-EBS)**

#### 6.2.1 Overview of EBS clusters

On the Cluster O&M page of Elastic Block Storage (EBS) clusters, you can view the total capacity usage, current alerts, number of disks, and number of snapshots of the EBS clusters. You can also view the information about the deployed EBS clusters. This way, you can understand the overall information about the clusters and handle exceptions at the earliest opportunity.

**Procedure**

1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. On the **Cluster O&M** page, view the overall information about EBS clusters.
Overall information about EBS clusters On the Cluster O&M page, you can view the total capacity usage, current alerts, number of disks, and number of snapshots of all EBS clusters. The following table describes the metrics.

| Metric | Description |
|---|---|
| Capacity Usage | The total capacity, used capacity, and percentage of used capacity of all EBS clusters. |

| Current Alerts | The number of alerts at different levels in all EBS clusters and the recent five alert records. You can click More or the alert information to view and handle the current alert on the Current Alert page. For more information, see Handle current alerts. |
|---|---|
| Disks | The total number of disks in all EBS clusters. |
| Snapshots | The total number of snapshots that are created for the disks in all EBS clusters. |

Information about deployed clusters You can view the information about all the deployed EBS clusters that are managed by the Cloud Defined Storage (CDS) Ops platform. The cluster information includes the cluster suffix name, cluster update time, cluster type such as CDS-EBS or CDS-EBS&CDS- OSS, information about the data centers of the clusters, primary and secondary cluster identifiers (used for zone-disaster recovery), percentage of used space, total cluster capacity, and used capacity.

> **Note:** You can move the pointer over a cluster suffix name to view and copy the cluster ID.

Clusters can be sorted in ascending or descending order by name, total capacity, or used capacity. By default, clusters are sorted in descending order based on their used capacity. You can select a proper sorting method as required. You can also click **O&M** in the upper-right corner of a cluster section. On the Overview tab, view the monitoring data and configurations of the cluster.

#### 6.2.2 View the overview information about a cluster

**cluster**

On the Overview tab of a cluster, you can view the physical capacity usage, number of disks, number of snapshots, and inspection items of the cluster. This way, you can understand the overall information about the cluster and handle exceptions at the earliest opportunity.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the **CDS-Overview** tab, view the overall information about the cluster.
Overall information about the cluster You can view the used physical capacity, total physical capacity, number and status of master servers, number and status of storage servers, number of disks, and number of snapshots. The following table describes the metrics.

| Metric | Description |
|---|---|
| Total Physical Capacity | The total physical space of the Elastic Block Storage (EBS) cluster that is allocated by the PANGU File System layer. |
| Used Physical Capacity | The physical capacity that is used by the EBS layer, including the capacity occupied by internal data and user data. |
| Master Server BlockMaster | The total number of master servers, the number of normal master servers, and the number of abnormal master servers. |
| Storage Server BlockServer | The total number of storage servers, the number of normal storage servers, and the number of abnormal storage servers. |
| Disks | The total number of disks in the cluster. |
| Snapshots | The total number of snapshots that are created for disks in the cluster. |

Inspection items You can view the name, statistics, last execution time, and remarks of each inspection item. Monitoring data You can specify a time range or click a time range to view the monitoring data within the specified time range, including the cloud disk and snapshot trend chart, average latency, total cluster IOPS, and total cluster throughput of the EBS cluster. The following table describes the metrics.

| Metric | Description |
|---|---|
| Cloud Disk and Snapshot Trend Chart | The usage of disks and snapshots in the cluster. You can query the disk and snapshot usage of the cluster only by day. The monitoring data is generated on a daily basis. You can view the following monitoring data in the trend chart: Disks: the total number of disks. Snapshots: the total number of snapshots. |
| Average Latency | The average read latency and write latency of the cluster. You can view the following monitoring data in the trend chart: Read Latency: the average read latency. Write Latency: the average write latency. |

| Total Cluster IOPS | The total numbers of read operations and write operations per second in the cluster. You can view the following monitoring data in the trend chart: Read IOPS: the total number of read operations per second in the cluster. Write IOPS: the total number of write operations per second in the cluster. |
|---|---|
| Total Cluster Throughput | The total throughput of data reads and writes in the cluster. You can view the following monitoring data in the trend chart: Read: the total throughput of data reads in the cluster. Write: the total throughput of data writes in the cluster. |

You can click the name of a metric to show or hide the monitoring data in a chart. For example, you can click Disk Monitoring Data in the Cloud Disk and Snapshot Trend Chart to hide the monitoring data. Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

#### 6.2.3 View capacity information

On the Capacity tab of an Elastic Block Storage (EBS) cluster, you can view the logical capacity usage, physical capacity usage, capacity distribution, physical capacity usage trend, and inventory capacity trend of the EBS cluster.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Capacity** tab to view the capacity information about the cluster.
Logical Capacity Usage: You can view the used logical capacity, total logical capacity, and percentage of used logical capacity. The total logical capacity indicates the maximum volume of data that can be written. It includes the storage space that is occupied by internal logic modules, such as the metadata, GC, and recycle bin. The used logical capacity indicates the volume of data that has been written. Click **More** in the upper-right corner of the Logical Capacity Usage section. On the Overview tab, view the number of replicas in the cluster. Physical Capacity Usage: You can view the used physical capacity, total physical capacity, and percentage of used physical capacity. The total physical capacity indicates the maximum size of data that can be written to the cluster. The used physical capacity indicates the used physical capacity reported by PANGU. Click**More** in the upper-right corner of the Physical Capacity Usage section. On the Overview tab, view the details of the bare disk capacity, total capacity, system reserved capacity, OP reserved storage capacity, used capacity, and available capacity.

**Note**

If the inventory capacity is sufficient and the physical capacity usage reaches 80%, disk creation is not allowed. If the unused inventory capacity is less than the capacity of the newly created disk, disk creation also fails.

> If the physical capacity usage reaches 95%, data writing is not allowed.
> After you move the pointer over the
> icon on the right side of a capacity, the
> system displays the description and calculation formula of the capacity in the tooltip.

Distribution of Used Physical Storage Capacity: You can view the volume of data written to the disks, recoverable capacity and system occupied capacity, used capacity, inventory capacity, and oversold ratio. Capacity Trend On the **Capacity Trend** tab, select a time range to view the trend charts of physical capacity usage and inventory capacity. Physical Capacity Usage Trends: Specify a time range to view the Total Physical Capacity and Used Physical Capacity. Inventory Capacity Trend Chart: Specify a time range to view the trend chart of used inventory capacity. You can also click **Actions** in the upper-right corner to download data or save the trend chart as an image. Capacity Prediction After the system collects the capacity data of storage services deployed in a new cluster for 50 days, the system predicts the capacity usage for the next week once a day. You can perform operations such as cluster scale-up or scale-down based on the predicted capacity usage at the earliest opportunity. This prevents cluster failures that may be caused by exhausted storage capacity and ensures the security and stability of the cluster.

> **Note:** The predicted capacity usage is for reference only. Perform operations based on the actual capacity usage.

Capacity prediction depends on the accumulation of sufficient samples. If the number of data in a cluster is stored for less than 50 days, the system cannot predict the capacity. No prediction data is available for a newly deployed cluster. Click the **Capacity Prediction** tab to view the predicted physical capacity.

#### 6.2.4 Monitor clusters

##### 6.2.4.1 View cluster monitoring information

You can view the real-time and historical monitoring data of a cluster to obtain the cluster resource usage. Historical monitoring data includes the average latency in a specific time range and total IOPS of the cluster.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Monitor** tab.
5. In the left-side navigation pane, click **Cluster** to view the real-time monitoring data. You
can also specify a time range and view the historical monitoring data of the cluster. Real-time monitoring data includes the average read latency, average write latency, average read throughput, average write throughput, average read I/O size, average write I/O size, average read IOPS, average write IOPS, total read throughput, total write throughput, point in time, and the trend chart of historical average write latency in the last 10 minutes.

> **Note:** The unit of real-time monitoring data is displayed in the console.
> In the trend chart of historical average write latency in the last 10 minutes, the red area indicates that the values exceed the alert thresholds. Pay attention to the red area.

Historical monitoring data includes the average latency, total IOPS, and total throughput of the cluster. The following table describes the metrics.

| Metric | Description |
|---|---|
| Average Latency | The average read latency and write latency of the cluster. You can view the following monitoring data in the Average Latency trend chart: Read Latency: the average read latency of the cluster. Write Latency: the average write latency of the cluster. |

| Total Cluster IOPS | The total numbers of read and write operations per second in the monitored cluster. You can view the following monitoring data in the Total Cluster IOPS trend chart: Read IOPS: the total number of read operations per second in the cluster. Write IOPS: the total number of write operations per second in the cluster. |
|---|---|
| Total Cluster Throughput | The total throughput of data reads and writes in the cluster. You can view the following monitoring data in the Total Cluster Throughput trend chart: Read: the total throughput of data reads in the cluster. Write: the total throughput of data writes in the cluster. |

Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

##### 6.2.4.2 View monitoring data of BlockServer nodes

**nodes**

You can view the real-time monitoring data and historical monitoring data of a BlockServer node, such as the average latency within a specific time range and total IOPS. This allows you to know the resource usage of the BlockServer node at the earliest opportunity.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Monitor** tab.
5. In the left-side navigation tree, click **BlockServer** to view the real-time monitoring data.
You can also specify a node code and a time range to view the historical monitoring data of the BlockServer node. Real-time monitoring data includes the average read latency, average write latency, average read throughput, average write throughput, average read I/O size, average write I/O size, average read IOPS, average write IOPS, total read throughput, total write throughput, point in time, and the trend chart of historical average write latency in the last 10 minutes.

> **Note:** The unit of real-time monitoring data is displayed in the console.
> In the trend chart of historical average write latency in the last 10 minutes, the red area indicates that the values exceed the alert thresholds. Pay attention to the red area.

Historical monitoring data includes the average latency, total IOPS, and total data throughput. The following table describes the metrics.

| Metric | Description |
|---|---|
| Average Latency | The average read latency and write latency of the BlockServer node. You can view the following monitoring data in the trend chart: Read Latency: the average read latency. Write Latency: the average write latency. |
| Read/Write IOPS | The total number of read operations and write operations per second in the BlockServer node. You can view the following monitoring data in the trend chart: Read IOPS: the total number of read operations per second in the BlockServer node. Write IOPS: the total number of write operations per second in the BlockServer node. |
| Throughput | The total throughput of data reads and writes in the BlockServer node. You can view the following monitoring data in the trend chart: Read: the total throughput of data reads in the BlockServer node. Write: the total throughput of data writes in the BlockServer node. |

Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

##### 6.2.4.3 View PANGU monitoring data

You can view PANGU monitoring data to analyze the cluster status in real time.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Monitor** tab, and then click **Pangu Monitoring**.
5.
6. Click **Analytics**.
After the analysis is complete, you can view the check items, detection levels, and check results. You can click the name of a check item to view more details in the message that appears. Then, troubleshoot the error based on the error description, suggestions, and details.

#### 6.2.5 Configure clusters

##### 6.2.5.1 Configure block rebalance

By default, the block rebalance feature is enabled. If data is unevenly distributed because BlockServer nodes are added or stopped, the corresponding cluster automatically balances the number of segments on BlockServer nodes. This way, the resources of the cluster can be properly used.

**Background information**

O&M engineers can determine whether the segments are evenly distributed by checking the average number of segments on each BlockServer node and the variance in the number of segments on all BlockServer nodes.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Configure** tab.
5. In the left-side navigation tree, click **Rebalance**. Then, view the basic information and
configurations of the block rebalance feature. Basic Information: This section displays the average number of segments on each BlockServer node and the variance in the number of segments on all BlockServer nodes. Configurations of block rebalance: You can enable or disable the block rebalance feature in this section. By default, this feature is enabled.

##### 6.2.5.2 Configure the EC mode

By default, clusters use triplicate storage to ensure data reliability and consistency. However, you can also enable erasure coding (EC) to improve storage reliability. Compared with triplicate storage, EC can provide higher data reliability at lower data redundancy levels.

**Usage notes**

After you modify the EC configurations for clusters, the configurations take effect for both existing and new disks. After the EC mode is enabled for a cluster, you cannot disable this mode for the cluster, which means you cannot switch to the triplicate storage mode. Proceed with caution.

**Specify an EC type for a cluster**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Configure** tab.
5. In the left-side navigation tree, click **EC Configurations**. Turn on **EC Switch**.
6. Configure the **Configuration Type** parameter.
The EC types supported by the cluster are all displayed in the drop-down list. After you select a configuration type, the value of the Replicas parameter is displayed, which is calculated based on the selected configuration type.

> **Note:** Some clusters do not support the Configuration Type parameter. The actual page prevails.

7. Click **Save**.

**View EC configuration distribution for disks in a cluster**

The EC configuration of disks in a cluster is the same as the EC configuration of a cluster. In the **EC Configuration Distribution for Disks in a Cluster**section of the **EC**
**Configurations** tab, view the EC configuration distribution for disks in a cluster.
After you modify the EC configurations of the cluster, the existing disks are automatically switched to the EC mode. In the EC Configuration Distribution for Disks in a Cluster section, check whether all existing disks have been switched to the EC mode.

##### 6.2.5.3 Configure PANGU Service

You can view and configure the replica traffic control, cluster recycle bin, and full-cluster offline inspection features and service quotas and quality of service (QoS) based on your business requirements.

> **Important:** If you modify cluster information, system exceptions may occur. Proceed with caution.

Configure replica traffic control You can configure the maximum and minimum replication speeds based on your business requirements to control data replica traffic. If you need to quickly replicate data, you can increase the maximum and minimum replication speeds. If you do not want the replication to consume a large amount of resources, you can reduce the maximum and minimum replication speeds.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Configure** tab, and then click **Pangu Configuration**.
5. On the **Replica Flow Control** tab, you can view the names and values of replica traffic
control rules and change the values to modify the replication speed based on your business requirements.
6. Modify the replication speed based on your business requirements.
i. Click **Edit** in the **Actions** column of a replica traffic control rule. ii. In the **Modify Configuration** dialog box, modify the maximum or minimum replication speed. This way, you can set an upper or lower limit on the speed at which data is read from the source server or written to the destination server. The valid value of the maximum or minimum replication speed is 1 to 100000, measured in MB/s.

> **Important:** We recommend that you set the maximum or minimum replication read speed and the maximum or minimum replication write speed to the same value. Otherwise, data is replicated based on the smaller speed value that you set.

The read/write speed settings affect the performance of servers. Proceed with caution. iii. Click **OK**.

**Configure cluster recycle bin**

If the recycle bin feature is enabled, files that are deleted during various operations on a cluster are temporarily stored in the recycle bin. If the recycle bin feature is disabled, files deleted from a cluster are directly deleted and not stored in the recycle bin.
1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. Click the **Cluster Recycle Bin Settings** tab to view the recycle bin settings and modify
the settings based on your business requirements. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Recycle Bin (TRUE or FALSE) | Specifies whether to enable the recycle bin feature. Valid values: TRUE (default): enables the recycle bin feature. If the recycle bin feature is enabled, files deleted from the cluster are temporarily stored in the recycle bin. FALSE: disables the recycle bin feature. If the recycle bin feature is disabled, files deleted from the cluster are directly deleted and not stored in the recycle bin. |
| General Recycling Percentage | If the available disk space is smaller than the value specified by this parameter, junk data is deleted from the system at the general recycling speed. |
| Emergency Recycling Percentage | If the available disk space is smaller than the value specified by this parameter, junk data is deleted from the system at the emergency recycling speed. Note The emergency recycling speed is faster than the general recycling speed. |
| Recycle Bin Retention Period (Seconds) | In most cases, set this parameter to 86400. Valid values: 3600 to 8640000000. Unit: seconds. |

3. Modify the cluster recycle bin settings based on your business requirements.
i. Click **Edit** in the **Actions** column of a parameter. ii. In the **Modify Configuration** dialog box, change the value of the parameter based on your business requirements. You can configure multiple parameters to achieve the effect of operations described in the following table:

| Operation | Description |
|---|---|
| Disable automatic recycling | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 0. |
| Freeze the recycle bin | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 0, and set the Recycle Bin Retention Period (Seconds) parameter to 8640000000. Note After you freeze the recycle bin, files in the recycle bin are not deleted. This ensures data security. |
| Clear the recycle bin | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 100. |
| Disable the recycle bin feature | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 100. After all files in the recycle bin are deleted, set the Recycle Bin (TRUE or FALSE) parameter to FALSE. |

iii. Click **OK**.

**Enable or disable full-cluster offline inspection**

If you enable the full-cluster offline inspection feature, the system automatically analyzes the status of clusters on a regular basis.
1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. On the **Full-cluster Offline Inspection** tab, check whether the full-cluster offline
inspection feature is enabled. You can enable or disable the feature based on your business requirements.
3. Enable or disable the full-cluster offline inspection feature.
i. Click **Edit** in the **Actions** column. ii. In the **Modify Configuration** dialog box, change the status of the full-cluster offline inspection feature. Valid values: enable and disable. If you want to enable the full-cluster offline inspection feature, select enable. If you want to disable the feature, select disable. iii. Click **OK**.

**View quotas and QoS**

1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. Click the **Quotas and QoS** tab to view the basic information, quotas, and QoS of the
cluster.

> **Note:** The basic information and QoS are displayed only for hybrid clusters of CDS-OSS and CDS-EBS. If the cluster is a CDS-EBS cluster, only the quota of the Elastic Block Storage (EBS) service is displayed.

Basic Information: In this section, you can view the cluster type, QoS feature status, HDD VIOPS, SSD VIOPS, total storage usage, and total capacity of the SSD cache. Quota: In this section, you can view the current used capacity, capacity quota for cluster storage, and status of different services. QoS: In this section, you can view the proportions of different services on HDDs and SSDs.

#### 6.2.6 Manage services

##### 6.2.6.1 Manage BlockMaster nodes

BlockMaster is a type of management node that can be used to perform multiple operations. For example, you can manage the metadata of disks, and generate the information about a block device when you create the virtual block device. BlockMaster nodes can distribute segments to different BlockServer nodes and schedule garbage collection (GC) threads based on the invalid data and fragment data reported by BlockServer nodes. This feature allows you to view the information about a BlockMasrter node, such as the IP address and service location, check the server status, and obtain version information.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Service** tab.
5. In the left-side navigation tree, click **Primary Server BlockMaster** and view the details of
the BlockMaster nodes. You can also perform operations on the BlockMaster nodes based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|

| Query version information | You can use one of the following methods to obtain the version information about the server: Method 1: Click Obtain Version Information in the Actions column of the server. In the Obtain Version Information dialog box, view the server version information. Method 2: Click Obtain Version Information. In the Obtain Version Information dialog box, view the server version information. |
|---|---|
| Check server status | Check the status of a server. Find the server that you want to view and clickC heck Status in the Actions column. |

##### 6.2.6.2 Manage BlockServer nodes

BlockServer can call the FlatLogFile API to manage the segments that are stored in the data files of PANGU. This feature allows you to view the information about BlockServer nodes, such as the IP address, service location, and hard disk partition. You can also obtain version information.

**Background information**

BlockServer nodes use the Index Map data structure to maintain the relationship between the logical block address (LBA) of data in segments and the offset address in the actual storage file. This way, read requests can quickly locate the actual data in the files of PANGU. In addition, BlockServer nodes use read-ahead cache to reduce the I/O of flies. This can optimize the read speed. BlockServer nodes collect the percentage of garbage data and the fragmentation degree in segments and report them to BlockMaster nodes. Then, BlockMaster nodes schedule garbage collection (GC) threads to perform a GC or defragmentation task. After a GC task is complete, the system compacts block data to update the Index Map data structure and deletes invalid data files.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Service** tab.
5. In the left-side navigation tree, click **Storage Service BlockServer**. Then, view the
information about BlockServer nodes and obtain the server information based on your business requirements. You can use one of the following methods to obtain the server version information: Method 1: Click **Obtain Version Information** in the **Actions** column of the server. In the **Obtain Version Information** dialog box, view the server version information. Method 2: Click **Obtain Version Information**. In the **Obtain Version Information** dialog box, view the server version information.

##### 6.2.6.3 Manage snapshot servers

You can view the information about snapshot servers, such as the service address, load rate, number of uploads, number of replications, and number of lazy loads. You can also obtain version information.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Service** tab.
5. In the left-side pane, click **Snapshot Server**. Then, view the information about snapshot
servers and obtain the server information based on your business requirements. You can use one of the following methods to obtain the server version information: Method 1: Click **Obtain Version Information** in the **Actions** column of the server. In the **Obtain Version Information** dialog box, view the server version information. Method 2: Click **Obtain Version Information**. In the **Obtain Version Information** dialog box, view the server version information.

##### 6.2.6.4 Manage PANGU Service

You can manage meta servers, chunk servers, and file information based on your business requirements. Manage meta servers Meta servers are used to maintain cluster metadata and instruct upper-layer services on how to read and write data. You can manage a meta server to view the meta server information, switch the secondary meta server to the primary meta server, generate checkpoints for the meta server, and obtain the build information about the meta server.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Service** tab.
5. In the left-side navigation tree, click **Pangu Service**, and then click the **Meta Server** tab.
On this tab, view the information about the meta servers and perform operations on the meta servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Switch to the primary meta server | In most cases, you do not need to manually switch to the primary meta server. You need to manually switch to the primary meta server only if the current primary meta server fails. In most cases, the switchover takes a few seconds. To switch to the primary meta server, perform the following operations: Find the secondary meta server that you want to manage and click Switch to Primary Meta Server in the Actions column. |
| Generate checkpoints | Generate checkpoints to record the runtime data of the meta server. In most cases, the generated information is stored on the system disk of the meta server. To generate checkpoints, perform the following operations: Find the meta server that you want to manage and click Generate CPT in the Actions column. |
| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information, perform the following operations: Find the meta server that you want to manage and click Build Information in the Actions column. |

Manage chunk servers Chunk servers are used for actual read and write operations in clusters. You can manage a chunk server to view the chunk server information, specify the status of the chunk server, add the chunk server to or remove the chunk server from the blacklist, and obtain the build information about the chunk server.
1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**, and then click the **Chunk Server** tab.
On this tab, view the information about the chunk servers and perform operations on the chunk servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|

| Specify the chunk server status | Find the chunk server that you want to manage and clickS et Status in the Actions column. In the Set Server status dialog box, select a server state. You can select one of the following states: Read-only, Normal, and Shut-down. Warning Security risks may arise if you shut down a chunk server. Proceed with caution. |
|---|---|
| Add a server to the blacklist or remove a server from the blacklist | If upper-layer services do not need to write data to a chunk server for the moment, the chunk server can be added to the blacklist. After a chunk server is added to the blacklist, no chunks are assigned to the chunk server, and no data is written or copied to the chunk server. Warning After you add a server to the blacklist, the server becomes unavailable. Proceed with caution. To add a chunk server to the blacklist, perform the following operations: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Add to Blacklist. To remove a chunk server from the blacklist, perform the following operations: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Remove from Blacklist. |
| Restart services | Restarts the services on a chunk server. Warning Security risks may arise if you restart services. Proceed with caution. To restart the services on a chunk server, perform the following operations: Find the chunk server that you want to manage and click Restart Service in the Actions column. |

| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information about a chunk server, perform the following operations: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Build Information. |
|---|---|

**Manage files**

You can manage the files of a PANGU cluster. For example, you can manage the directories and files of a cluster and clear the recycle bin of the cluster.
1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**, and then click the **Files** tab. On this
tab, view the information about the system root directories and perform operations on the directories based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View the quotas on the root directory | Click View Root Directory Quota to view the quotas on the following items: EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength. The FileLogicalLength and FilePhysicalLength items are measured in bytes. The following list describes the quota items: EntryNumber: the total number of files and directories that can be stored in the root directory. FileNumber: the total number of files that can be stored in the root directory. FileLogicalLength: the maximum logical size of files in the root directory. FilePhysicalLength: the maximum physical size of files in the root directory. |
| Search for objects | Enter the ID of the file for which you want to search in the search box in the upper-right corner and click Search. |

| View and manage directories Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a directory: View the quotas on the directory Click View Quota in the Actions column. You can view the quotas on the EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength items. Fix or unfix the directory Click Fix in the Actions column to fix the directory. After the directory is fixed, you cannot move or delete the directory. To move or delete the directory, click Unfix in the Actions column to unfix the directory. |
|---|---|
| View and manage files Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a file: View the information about chunks Find the file that you want to manage and clickV iew Chunk Information in the Actions column. You can view the basic information and chunk information about the file. The basic information includes the file ID, file type, number of chunks, and application name. The chunk information includes the chunk ID, chunk status, and server. Modify the number of replicas PANGU stores multiple replicas of a file to improve the reliability of the file. You can configure the number of replicas for files. A file with more replicas improves data security but occupies larger storage space. We recommend that you set both the minimum number and maximum number of replicas to three. Find the file that you want to configure and clickE dition in the Actions column. Modify the Minimum Number of Replicas and Maximum Number of Replicas parameters to configure the number of replicas that are stored for the file in PANGU. If data is lost, copied, or migrated, the system copies or deletes the file based on the number of replicas. |
| Clear the recycle bin Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | Find the deleted/ directory and click Clear Recycle Bin in the Actions column to delete the files from the recycle bin. Note The file recycling policy of the deleted/ directory is the same as the settings of the cluster recycle bin. |

#### 6.2.7 Manage storage sets

You can search for an Elastic Block Storage (EBS) storage set by cluster name or storage set ID, and then perform the following operations to manage the storage set: View information about the storage set, view disks in the storage set, view capacity usage in each partition of the storage set, and modify the clusters in each partition of the storage set.

**Prerequisites**

**eequs**

**es**

A storage set is available. For information about how to create a storage set, see the "Create a storage set" topic under the EBS document in **CDS User Guide**.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Storage Set**.
3. On the **Storage Set** page, select a cluster or enter a storage set ID. Then, you can view
the information in the storage set list and perform operations based on your business requirements.

| Operation | Description |
|---|---|
| View information about a storage set | In the storage set list, you can view information about a storage set, such as the storage set ID, alert status, region, partition, and cluster. If Abnormal is displayed in the Alert Status column of a storage set, alerts are triggered by the storage set. You can perform the following operations to troubleshoot the issues and clear the alerts: Note The system can generate only capacity alerts for storage sets. If the storage set contains a partition that is not associated with a cluster, click Edit Cluster in the Actions column to associate the partition with a cluster. After you associate the partition with a cluster, wait for a period of time. If the partition is associated with the cluster, Normal is displayed in the Alert Status column of the storage set. If the partition fails to be associated with the cluster or the disk capacity of the cluster is insufficient, Abnormal remains in the Alert Status column of the storage set. If all the partitions of the storage set are associated with clusters, but the percentage of the consumed capacity of all the clusters in at least one partition reaches the alert threshold, scale up the clusters based on your business requirements. |

| Modify the clusters in partitions | By default, the partitions of a storage set are not associated with clusters. You can perform the following operations to associate the partitions of a storage set with clusters: Important A cluster can be associated with partitions of different storage sets. However, a cluster can be associated with only one partition within a storage set. i. Find the storage set that you want to manage and clickE dit Cluster in the Actions column. ii. In the Edit Partition Cluster dialog box, add clusters to or remove clusters from the partitions, and click OK. iii. In the Note message, click OK. |
|---|---|
| View monitoring data about capacity usage in partitions | You can view the status, total capacity, occupied capacity, percentage of consumed capacity, and capacity alert threshold of partitions in a storage set. Note If the percentage of the consumed capacity of all clusters associated with a partition reaches the alert threshold, the value in the Status column changes from Sufficient Capacity to Insufficient Capacity for the storage set. i. Find the storage set that you want to manage and clickC apacity Monitoring in the Actions column. ii. In the Partition Capacity Monitoring dialog box, view the capacity monitoring data of partitions. |
| View information about disks in a storage set | If you specify a storage set when you create a disk or an Elastic Compute Service (ECS) instance, you can view information about the disk and its relationship with the storage set. Click the ID of the storage set that you want to manage or clickD isk in the Actions column. On the Disk page, you can view the information about the disks in the storage set and manage the disks. For more information, see Manage disks. |

#### 6.2.8 Manage disks

You can view the information about the disks of all clusters, such as disk attributes, monitoring data, and the clusters to which disks belong.

**Prerequisites**

One or more disks are created. For more information, see the "Create a disk" topic of the "Getting started" chapter for Elastic Block Storage (EBS) in **Cloud Defined Storage User**
**Guide**.

**Manage disks**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Disk**.
3. On the **Disk** page, search for disks by cluster, storage set, or partition in a storage set.
After you search for disks, you can view the disk information and perform operations on the disks based on your business requirements. The following table describes the operations that you can perform.

> **Important:** Most O&M operations are available only for users who have the CDS support or CDS developer permissions.

| Operation | Description |
|---|---|
| View disk information | In the disk list, view the disk device, volume ID, size, disk type, replica, and EC configurations. |
| View disk details | Click the name of the disk that you want to manage. On theD isk Details page, view the attributes and monitoring data of the disk, and the cluster to which the disk belongs. |
| Modify the IOPS and maximum throughput | Warning This feature is available only for O&M. Proceed with caution. You can modify the maximum IOPS and throughput of a disk. Perform the following steps: Important When you scale up a disk, change the configurations of a disk without stopping services, or replace the OS installed on a disk, all Quality of Service (QoS) values of the disk are restored to the values that are automatically calculated by Elastic Compute Service (ECS). i. Find the disk that you want to manage and clickM odify Maximum IOPS and Throughput in the Actions column. ii. In the Modify Maximum IOPS and Throughout dialog box, specify a maximum throughput and a maximum IOPS based on the maximum throughput and maximum IOPS supported by the device. The throughput is measured in MB per second. To restore the maximum IOPS and throughput of a disk to their original values, click Reset. iii. Click OK. |

**View disk details**

1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Disk**.
3. On the **Disk** page, click the ID of the disk whose details you want to view.
4. On the **Disk Details** page, view the attributes and monitoring data of the disk, and the
cluster to which the disk belongs. View disk attributes In the **Attributes** section, view the information about the disk, such as the disk ID, device information, and disk name. View fine-grained monitoring data

> **Important:** You can view the fine-grained monitoring data only within the last hour.

On the **Near Real-time Monitoring** tab, specify a time range to view the fine-grained monitoring data of the disk, such as the read and write latency, throughput, read and write IOPS, I/O queue depth, and I/O block size. Move the pointer over a trend chart to view the data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image. View segmented latency

> **Important:** You can view the latency data only within the last hour.

If an exception occurs on a disk, you can view the segmented latency of I/O operations in different modules within a specific time range. This helps you find the module in which an exception occurs. On the **Segmented Latency** tab, specify a time range, the request type, the latency, and the data source of abnormal I/O. Then, you can view the latency of all I/O operations that meet the filter conditions within the specified time range.

> **Important:** Only abnormal I/O operations with a latency of greater than 1,000 milliseconds can be analyzed.

Find the I/O operation that you want to view, click the Plus icon on the left side of the value in the Duration column, and then view the latency of the I/O operation in different modules. Move the pointer over a module name and view the module details.

#### 6.2.9 Hot migration of disks

You can create hot migration jobs to migrate disks between Elastic Block Storage (EBS) clusters. The disks can still be used during the migration. This improves the O&M efficiency of disks.

**Usage notes**

Only premium performance disks and standard performance disks can be migrated. The disk type and disk ID remain unchanged after a disk is migrated. Hot migration can be performed only across zones. Disks that have snapshots with the instant access (IA) feature enabled cannot be migrated. Disks that are added to replication pairs cannot be migrated. The format and capacity of a disk cannot be changed after the disk is migrated. If the format of the disk in the source cluster is different from that in the destination cluster, the migration fails. The source cluster and the destination cluster must belong to the same Object Storage Service (OSS) region. The source cluster and the destination cluster cannot be the same. Otherwise, the migration fails. During the migration, an I/O latency of less than 1 second is normal. We recommend that you migrate disks during off-peak hours. The migration consumes network bandwidth. Therefore, you need to pay attention to the number of disks that are concurrently migrated. You can concurrently migrate up to 16 disks in a cluster. You can cancel a migration job before the job is complete. After a disk is migrated, if you want to migrate the disk back to the source cluster, create another migration job. After the migration is complete, the data is fully replicated from the source cluster to the destination cluster. To ensure data accuracy, the data of a disk data is retained in the source cluster for seven days before the disk is released. If the usage of the source cluster is more than 80%, the retention period of disk data in the source cluster may be shorter.

**Create a disk migration job**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Hot Migration of**
**Disks**.
3. On the **Hot Migration of Disks** page, configure and run a hot migration job.
i. Click **Create Migration Job**. ii. In the **Create Disk Migration Job** panel, enter a disk ID or select a disk. Enter a disk ID: Turn on **Enter Disk IDs** and enter a disk ID. You can enter multiple disk IDs at a time. Separate multiple disk IDs with commas (,). Select a disk: By default, **Enter Disk IDs** is turned off. Select a source cluster, and select the disk that you want to migrate from the disk list that is displayed. iii. Click **Next**. Select a destination cluster. iv. Click **Create**. The system starts to migrate the disks. The migration takes some time. Wait until the migration is complete.
4. **Optional.** Search for the migration job on the **Hot Migration of Disks** page.
Specify one or more of the following filter conditions: source cluster, destination cluster, DeviceKey, task type, and status. The state of a migration job can be Succeeded, Failed, Initializing, Invalid, Prepared, Created, Running, Stopped, Verify, Verifying, Verified, or Destroyed.

**What to do next**

After you create a hot migration job, you can view the migration details of each disk and perform the following operations: View the details of a hot migration job Find the hot migration job that you want to view and click **View Details** in the **Actions** column. In the **Details** panel, view the basic information and log details of the migration job. Restore a hot migration job If you want to restore a migration job that fails or is stopped, find the migration job and click
**Restore** in the **Actions** column. In the **Restore** message, click **OK**.
Close an invalid migration job If you want to close a migration job that is invalid, find the migration job and click **Close** in the **Actions** column. In the **Close** message, click **OK**. Stop a migration task If you want to stop a migration job that is in the Prepared, Created, Running, Verify, Verifying, or Verified state, find the migration job and click **Stop** in the **Actions** column. In the **Stop** message, click **OK**.

#### 6.2.10 Execute canary O&M tasks

You can initiate canary O&M tasks to run a common O&M command on multiple hosts at a time. This simplifies O&M operations and minimizes the impact in case of a failure. You can stop command execution at the earliest opportunity if the exit code of the command result is not 0. You can also specify a speed and observation period for a canary O&M task. This way, the canary O&M task can run the O&M command at an appropriate speed on the specified hosts. During the execution of a canary O&M task, you can view the progress and results in real time.

**Background information**

You can execute canary O&M tasks to run multiple common O&M commands at the same time, such as hostname and /apsara/deploy/pangu_blockadmin. Canary O&M provides the following features: You can configure canary policies to determine the duration of a canary O&M task, the interval between canary O&M tasks, and other O&M settings. You can configure a command whitelist. Only commands in the whitelist can be run on specific clusters. You can specify the cluster and the command status to filter O&M tasks.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Administration**.
3. On the **Canary O&M** page, click **Initiate Execution**.
4. In the **Initiate Execution** dialog box, configure the parameters. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Storage Type | The value is fixed to EBS. You cannot modify this parameter. |
| Cluster | The cluster on which the O&M commands are run. The system supports all types of clusters, including rivermaster clusters, compute clusters, and storage clusters. |
| Destination Machine | The machine on which the commands are run. You can select multiple machines. |
| Command | The commands that you want to run. You can run only verified commands. After you enter the commands, click Verify to check whether the commands are valid. Note Move the pointer over the icon next to the Command parameter and view the commands that are supported by the specified cluster. |
| Execution Reason | The reason why you want to run the commands. |
| Execution Timed Out | Optional. The timeout period of the commands that you want to run. Unit: seconds. Default value: 259200 (3 days). If the commands are still running after the timeout period ends, the commands fail to run. |
| Canary Speed | If you want to run multiple O&M commands at the same time, you can run the commands on specified machines in batches. Valid values: Single Machine: The number of batches is equal to the total number of machines. Each batch contains one machine. Default: Machines are divided into several batches based on the sequence in which you specify the machines. The number of machines in a batch increases as the task proceeds. A batch contains up to 16 machines. If the number of remaining machines is less than the required number of machines in the corresponding batch, the commands are run on all remaining machines in the last batch. Fastest: Machines are divided into several batches based on the sequence in which you specify the machines. A batch contains 16 machines. If the number of remaining machines is less than 16, the commands are run on all remaining machines in the last batch. The O&M commands are concurrently run on machines in a batch. |

| Observation Period | The interval between batches. The O&M commands start to run in a batch only after the commands are run in the previous batch. Important The number of machines in the batches in the observation period cannot exceed the total number of machines. |
|---|---|

5. Click **OK**. In the message that appears, click **OK**.
After a canary O&M task is executed, you can perform the following operations: View execution records Click **Details** in the **Actions** column of the canary O&M task. In the **Execution Details** panel, you can view the execution details, command details, and progress of the canary O&M task. In the **Progress Details** section, click **View** in the **Execution Result Details** column to view the detailed execution result. Re-execute the canary O&M task Click **Execute Again** in the **Actions** column. In the **Execute Again** dialog box, modify the parameters such as Destination Machine and Execution Reason and then click **OK** to re-execute the task. Find the canary O&M tasks of a specific cluster After you specify a cluster and an execution state, the system displays the O&M tasks in the specified state of the cluster.

### 6.3 Manage EBS clusters (EBS-1.0)

#### 6.3.1 Overview of EBS clusters

On the Cluster O&M page of Elastic Block Storage (EBS) clusters, you can view the total capacity usage, current alerts, number of disks, and number of snapshots of the EBS clusters. You can also view the information about the deployed EBS clusters. This way, you can understand the overall information about the clusters and handle exceptions at the earliest opportunity.

**Procedure**

1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. On the **Cluster O&M** page, view the overall information about EBS clusters.
Overall information about EBS clusters On the Cluster O&M page, you can view the total capacity usage, current alerts, number of disks, and number of snapshots of all EBS clusters. The following table describes the metrics.

| Metric | Description |
|---|---|

| Capacity Usage | The total capacity, used capacity, and percentage of used capacity of all EBS clusters. |
|---|---|
| Current Alerts | The number of alerts at different levels in all EBS clusters and the recent five alert records. You can click More or the alert information to view and handle the current alert on the Current Alert page. For more information, see Handle current alerts. |
| Disks | The total number of disks in all EBS clusters. |
| Snapshots | The total number of snapshots that are created for the disks in all EBS clusters. |

Information about deployed clusters You can view the information about all the deployed EBS clusters that are managed by the Cloud Defined Storage (CDS) Ops platform. The cluster information includes the cluster suffix name, cluster update time, cluster type such as CDS-EBS or CDS-EBS&CDS- OSS, information about the data centers of the clusters, primary and secondary cluster identifiers (used for zone-disaster recovery), percentage of used space, total cluster capacity, and used capacity.

> **Note:** You can move the pointer over a cluster suffix name to view and copy the cluster ID.

Clusters can be sorted in ascending or descending order by name, total capacity, or used capacity. By default, clusters are sorted in descending order based on their used capacity. You can select a proper sorting method as required. You can also click **O&M** in the upper-right corner of a cluster section. On the Overview tab, view the monitoring data and configurations of the cluster.

#### 6.3.2 Cluster overview

On the Overview tab of an Elastic Block Storage (EBS) cluster, you can view the physical capacity usage, number of disks, number of snapshots, and inspection items of the cluster. This way, you can understand the overall information about the cluster and handle exceptions at the earliest opportunity.

**Background information**

To manage the existing clusters, Cloud Defined Storage (CDS)-OPS displays EBS clusters that are based on PANGU V1.0 and PANGU clusters. This allows you to view the cluster information and manage PANGU clusters. You can use CDS-OPS to perform O&M operations on PANGU clusters but not EBS clusters that are based on PANGU V1.0.

**Procedure**

1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the **Overview** tab, view the overall information about the cluster.
Overall information about the cluster You can view the capacity usage, used physical capacity, total physical capacity, number and status of master servers, number and status of storage servers, number of disks, and number of snapshots. The following table describes the metrics.

| Metric | Description |
|---|---|
| Total Physical Capacity | The total physical capacity of the EBS cluster that is allocated by the PANGU layer. |
| Used Physical Capacity | The physical capacity that is used by the EBS layer, including the capacity occupied by internal data and user data. |
| Master Server RiverCluster | The total number of master servers, the number of normal master servers, and the number of abnormal master servers. |
| Storage Server RiverServer | The total number of storage servers, the number of normal storage servers, and the number of abnormal storage servers. |
| Cloud Disks | The total number of disks in the cluster. |
| Snapshots | The total number of snapshots that are created for disks in the cluster. |

Inspection items You can view the name, statistics, last execution time, and remarks of each inspection item. Monitoring data Specify a time range or click a time range to view the monitoring data of the EBS cluster within the specified time range, including the cloud disk and snapshot trend chart. You can query the disk and snapshot usage of the cluster only by day. The monitoring data is generated on a daily basis. You can click the name of a metric to show or hide the monitoring data in a chart. For example, you can click Disks or Snapshots in the disk and snapshot trend chart to hide the monitoring data. Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

#### 6.3.3 View capacity information

The physical capacity usage of a cluster shows the capacity usage of the cluster. O&M engineers can scale up or scale down the cluster based on the capacity usage of the cluster.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Capacity** tab to view the physical capacity information about the cluster.
The physical capacity information includes the total physical capacity, the consumed physical capacity, and the percentage of the consumed physical capacity. The total physical capacity indicates the maximum size of data that can be written to the cluster. The consumed physical capacity indicates the consumed physical capacity reported by PANGU.

> **Note:** After you move the pointer over the
> icon on the right side of a capacity, the system
> displays the description and calculation formula of the capacity in the tooltip.

#### 6.3.4 Manage services

##### 6.3.4.1 View the information about a RiverCluster

A RiverCluster is a management node of a storage service. The RiverCluster manages the information about disks, such as metadata, and allocates RiverServers to disks to achieve high availability. This topic describes how to view the information about a RiverCluster, such as the IP address and location.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Service** tab.
5. In the left-side pane, click **Primary Server RiverCluster** to view the details of
RiverClusters.

##### 6.3.4.2 View the information about a RiverServer

This topic describes how to view the information about a RiverServer, such as the IP address and location.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Service** tab.
5. In the left-side navigation pane, click **Storage Server RiverServer** to view the
information about RiverServers.

##### 6.3.4.3 Manage PANGU Service

CDS Ops allows you to perform O&M operations on PANGU clusters of Elastic Block Storage (EBS) 1.0, such as managing meta servers, managing chunk servers, and viewing file information. Manage meta servers Meta servers are used to maintain cluster metadata and instruct upper-layer services how to read and write data. You can manage a meta server to view the meta server information, switch the secondary meta server to the primary meta server, generate checkpoints for the meta server, and obtain the build information about the meta server.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Elastic Block Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Service** tab.
5. In the left-side navigation tree, click **Pangu Service**. Click the **Meta Server** tab. On this
tab, view the information about the meta servers and perform operations on the meta servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Switch the primary meta server | In most cases, you do not need to manually switch the primary meta server. You need to manually switch the primary meta server only if the current primary meta server fails. In most cases, the switchover takes a few seconds. To switch the primary meta server, perform the following operations: Find the secondary meta server that you want to manage and click Switch to Primary Meta Server in the Actions column. |
| Generate checkpoints | Generate checkpoints to record the runtime data of the meta server. In most cases, the generated information is stored on the system disk of the meta server. To generate checkpoints, perform the following operations: Find the meta server that you want to manage and click Generate CPT in the Actions column. |
| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information, perform the following steps: Find the meta server that you want to manage and click Build Information in the Actions column. |

Manage chunk servers Chunk servers are used for actual read and write operations in clusters. You can manage a chunk server to view the chunk server information, set the status of the chunk server, add the chunk server to or remove the chunk server from the blacklist, and obtain the build information about the chunk server.
1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**. Click the **Chunk Server** tab. On this
tab, view the information about the chunk servers and perform operations on the chunk servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|

| Set the chunk server status | Find the chunk server that you want to manage and clickS et Status in the Actions column. In the Set Server status dialog box, select a server state. You can select one of the following states: Read-only, Normal, and Shut-down. Warning Security risks may arise if you discontinue a server. Proceed with caution. |
|---|---|
| Add a server to the blacklist or remove a server from the blacklist | If upper-layer services do not need to write data to a chunk server for the moment, the chunk server can be added to the blacklist. After a chunk server is added to the blacklist, no chunks are assigned to the chunk server, and no data is written or copied to the chunk server. Warning After you add a server to the blacklist, the server becomes unavailable. Proceed with caution. To add a chunk server to the blacklist, perform the following steps: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Add to Blacklist. To remove a chunk server from the blacklist, perform the following steps: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Remove from Blacklist. |
| Restart services | Restart the services on a chunk server. Warning Security risks may arise if you restart services. Proceed with caution. To restart the services on a chunk server, perform the following steps: Find the chunk server that you want to manage and click Restart Service in the Actions column. |

| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information about a chunk server, perform the following steps: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Build Information. |
|---|---|

**Manage files**

You can manage the files of a PANGU cluster. For example, you can manage the directories and files of a cluster and clear the recycle bin of the cluster.
1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**. Click the **Files** tab. On this tab, view
the information about the system root directories and perform operations on the directories based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View the quotas on the root directory | Click View Root Directory Quota to view the quotas specified by the following parameters: EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength. The FileLogicalLength and FilePhysicalLength items are measured in bytes. The following list describes the quota items: EntryNumber: the total number of files and directories that can be stored in the root directory. FileNumber: the total number of files that can be stored in the root directory. FileLogicalLength: the maximum logical size of files in the root directory. FilePhysicalLength: the maximum physical size of files in the root directory. |
| Search for files | Enter the ID of the file for which you want to search in the search box in the upper-right corner and click Search. |
| View and manage directories Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a directory: View the quotas on the directory Click View Quota in the Actions column. You can view the quotas on the EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength items. Fix or unfix the directory Click Fix in the Actions column to fix the directory. After the directory is fixed, you cannot move or delete the directory. To move or delete the directory, click Unfix in the Actions column to unfix the directory. |

| View and manage files Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a file: View the information about chunks Find the file that you want to manage and clickV iew Chunk Information in the Actions column. You can view the basic information and chunk information about the file. The basic information includes the file ID, file type, number of chunks, and application name. The chunk information includes the chunk ID, chunk status, and server. Modify the number of replicas PANGU stores multiple replicas of a file to improve the reliability of the file. You can configure the number of replicas for files. A file with more replicas improves data security and occupies larger storage space. We recommend that you set both the minimum number and maximum number of replicas to three. Find the file that you want to configure and clickE dition in the Actions column. Modify the Minimum Number of Replicas and Maximum Number of Replicas parameters to configure the number of replicas that are stored for the file in PANGU. If data is lost, copied, or migrated, the system copies or deletes the file based on the number of replicas. |
|---|---|
| Clear the recycle bin Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | Find the deleted directory and click Clear Recycle Bin in the Actions column to delete the files in the recycle bin. Note The file recycling policy of a deleted directory is the same as the settings of the cluster recycle bin. |

### 6.4 Manage OSS clusters

#### 6.4.1 Overview of OSS clusters

On the Cluster O&M page of Object Storage Service (OSS) clusters, you can view the total capacity usage, current alerts, number of buckets, and number of objects of the OSS clusters. You can also view the information about the deployed OSS clusters. This way, you can understand the overall information about the clusters and handle exceptions at the earliest opportunity.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. On the **Cluster O&M** page, view the overall information about OSS clusters.
Overall information about OSS clusters On the Cluster O&M page, you can view the total capacity usage, current alerts, number of buckets, and number of objects of all OSS clusters. The following table describes the metrics.

| Metric | Description |
|---|---|
| Capacity Usage | The total capacity, used capacity, and percentage of used capacity of all OSS clusters. |
| Current Alerts | The number of alerts at different levels in all OSS clusters and the recent five alert records. You can click More or the alert information to view and handle the current alerts on the Current Alert page. For more information, see Handle current alerts. |
| Buckets | The total number of buckets in all OSS clusters. |
| Objects | The total number of objects in all OSS clusters. |

Information about deployed clusters You can view the information about all the deployed OSS clusters that are managed by the CDS-OPS platform. The cluster information includes the cluster name, cluster update time, cluster type such as CDS-EBS or CDS-EBS&CDS-OSS, information about the data centers of the clusters, primary and secondary cluster identifiers (used for zone-disaster recovery), percentage of used capacity, total cluster capacity, and used capacity.

> **Note:** Move the pointer over the cluster name and click the
> icon on the right to edit
> the cluster alias.

Clusters can be sorted in ascending or descending order by name, total capacity, or used capacity. By default, clusters are sorted in descending order based on their used capacity. You can select a proper sorting method as required. You can also click **O&M** in the upper-right corner of a cluster section. On the Overview tab, view the monitoring data and configurations of the cluster.

#### 6.4.2 Cluster overview

On the Overview tab of an Object Storage Service (OSS) cluster, you can view the information about the cluster and the top 10 buckets in different ranking lists.

**View an overview of a cluster**

On the Overview tab, view the cluster information including the physical capacity usage, number of buckets, number of objects, cluster monitoring information on the current day, storage, queries per second (QPS), bandwidth statistics, and latency.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the **Overview** tab, view the overall information about the cluster.

> **Note:** You can also choose **More O&M Capabilities** > **Object Storage Service O&M** in the upper-right corner of the Cluster O&M page to go to the OSS O&M console.

Overall information about the cluster On the Overview tab, view the cluster information including the physical capacity usage, number of buckets, number of objects, and cluster monitoring information on the current day. The following table describes the metrics.

| Metric | Description |
|---|---|
| Physical Capacity Usage | The percentage of used physical capacity, used physical capacity, and total physical capacity of the cluster. |
| Buckets | The total number of buckets in the cluster and the number of buckets that are created on the current day. |
| Objects | The total number of objects in the cluster and the number of objects that are uploaded on the current day. |
| Cluster Monitoring Information Today | The inbound traffic and outbound traffic of the cluster on the current day, total number of requests, number of read requests, and number of write requests of the cluster. |

Monitoring data You can specify a time range or click a time range to view the monitoring data of the OSS cluster within the specified time range, including the storage, QPS, bandwidth statistics, and latency. Storage: the storage size of buckets in the cluster. QPS: the number of API requests. Bandwidth Statistics: statistics on the amount of traffic generated by buckets in the cluster. Latency: the latencies of API requests and the maximum value of the latencies. Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

**View ranking lists of buckets**

You can view the top 10 buckets within a specific time range in several dimensions, such as internal errors, requests, and inbound and outbound traffic over the internal network.
1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Bucket Rankings** tab and specify a time range to view the ranking lists of
buckets in the cluster. Click a bucket name in a ranking list. On the Bucket Details page, view the bucket information.

#### 6.4.3 View capacity information

On the Capacity tab, you can view the logical capacity usage, physical capacity usage, capacity distribution, and physical capacity usage trend of an Object Storage Service (OSS) cluster based on your business requirements.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Capacity** tab to view the capacity information about the cluster.
Logical Capacity Usage: You can view the used logical capacity, total logical capacity, and percentage of used logical capacity of all OSS clusters. The total logical capacity indicates the maximum volume of data that can be written. It includes the storage space that is occupied by internal logic modules, such as the metadata, garbage collection (GC), and recycle bin. The used logical capacity indicates the volume of data that has been written. Click **More** in the upper-right corner of the Logical Capacity Usage section to view the number of replicas in the cluster. Physical Capacity Usage: You can view the used physical capacity, total physical capacity, and percentage of used physical capacity. The total physical capacity indicates the maximum size of data that can be written to the cluster. The used physical capacity indicates the used physical capacity reported by PANGU. Click**More** in the upper-right corner of the Physical Capacity Usage section to view the details of the bare disk capacity, total capacity, system reserved capacity, OP reserved storage capacity, used physical capacity, and available physical capacity. Distribution of used physical storage capacity: You can view information such as the capacity of user buckets, capacity of other service buckets, recoverable capacity and system occupied capacity, and used capacity. Capacity Trend Click the **Capacity Trend** tab. Specify a time range to view the total and used physical capacity.

> **Note:** Click **Actions** in the upper-right corner of a metric region. Select **Download Data** to download the monitoring data to your on-premises machine, or select **Save as** **Image** to save the monitoring data as an image.

Capacity Prediction After the system collects the capacity data of storage services deployed in a new cluster for 50 days, the system predicts the capacity usage for the next week once a day. O&M staff can perform operations such as cluster scale-up or scale-down based on the predicted capacity usage at the earliest opportunity. This prevents cluster failures that may be caused by exhausted storage capacity and ensures the security and stability of the cluster. Click the **Capacity Prediction** tab to view the predicted physical capacity usage.

> **Note:** The predicted capacity usage is for reference only. Perform operations based on the actual capacity usage.

Capacity prediction depends on the accumulation of sufficient samples. If the number of data in a cluster is less than 50 days old, the system cannot predict the capacity. No prediction data is available for a newly deployed cluster.

#### 6.4.4 Monitor clusters

##### 6.4.4.1 View cluster monitoring information

You can view the cluster information within a specific time range to obtain the cluster status. The cluster information includes the service level agreement (SLA), status of HTTP requests, storage capacity, queries per second (QPS), bandwidth statistics, and latency.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Monitor** tab.
5. In the left-side navigation pane, click **Monitoring**, and select a preset time range or
specify a custom time range to view the monitoring data of the cluster. You can view the following monitoring metrics: SLA: the service level agreement provided by Object Storage Service (OSS). The SLA of OSS can be calculated based on the following formula: `Number of non-5XX requests per`

```
10 seconds or 1 hour/Number of valid requests × 100% .
```

> **Important:** Requests for which the HTTP 503 error is returned are not included in the valid requests because HTTP 503 errors are commonly caused by invalid request parameters.

HTTP Status: the numbers of the returned 2XX, 3XX, 5XX, 403, 404, 499, and other 4XX status codes, and the percentage of requests for which each type of error codes is returned. Storage: the storage capacities of OSS buckets in the cluster. QPS: the numbers of different types of API requests. Bandwidth Statistics: the traffic volumes of OSS buckets in the cluster. Latency: the average and maximum latencies of API requests. Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

##### 6.4.4.2 Check the health status of a cluster

Key-value (KV) engine is a KV storage layer to store KV pairs. This helps you manage large amounts of index information. You can view the status of KV engines by checking the health status of a cluster.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Monitor** tab.
5. In the left-side pane, click **Health Check**. On the page that appears, click **Check**.
After you check the health status of a cluster, you can view the information about the checks, such as the checked item, name of the checked component, check results, and failure cause.

##### 6.4.4.3 Execute a background task

You can execute background tasks based on your business requirements. For example, you can execute Object Storage Service (OSS) lifecycle tasks and garbage collection (GC) tasks.

**Background information**

Background tasks can be manually or automatically executed. By default, the system automatically executes background tasks every day. You cannot disable the automatic execution of background tasks. Manual execution: You manually execute background tasks at a time. Automatic execution: The system automatically executes background tasks at the specified point in time every day. For more information, see Configure execution time for background tasks.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Monitor** tab.
5. In the left-side pane, click **Background Tasks**. On the page that appears, specify a date to
execute background tasks. Execute a lifecycle task In the **Lifecycle** section, click **Run Now**. In the **Note** dialog box, click **OK**. Execute a garbage collection task In the **Garbage Collection** section, click **Run Now**. In the **Note** dialog box, click **OK**. After a task is complete, you can view the information about the task, such as the status and duration. To view the details of the task, click **View Details** in the **Actions** column.

##### 6.4.4.4 View the monitoring data of third-party modules

**modules**

If a third-party module is used in a cluster, you can view the monitoring data to obtain the usage and status of the third-party module.

**Background information**

The following table describes the third-party modules on which Object Storage Service (OSS) depends.

| Third-party module | Description |
|---|---|
| ocm | The module is used to manage system information, including buckets, users, and clusters. |
| ram | The module is used to verify access permissions. |
| umm | The module is used to authenticate user identities. |
| sts ak _ | The Security Token Service (STS) module is used to grant temporary access permissions. |
| aggregate | The module is used for aggregation. |
| ak | The AccessKey module is used to authorize access to OSS. |
| imm | The Intelligent Media Management (IMM) module is used to process, analyze, and retrieve data such as documents, images, and videos in OSS buckets. |
| kms | The Key Management Service (KMS) module is used for key hosting and cryptographic operations. |
| mns | The Message Service module is used to send notifications about OSS event changes. |
| other | Other third-party modules. |
| proxy | The module provides features related to the upper-layer proxy of OSS. |
| ubsms | The module is used to check the security of user accounts. |

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Monitor** tab.
5. In the left-side pane, click **Third-Party Monitoring**. On the page that appears, select a
preset time range or specify a custom time range to view the monitoring data of third-party modules in the specified time range, such as the proportion of third-party service dependency, QPS trend of total requests for each module, and the QPS and latency of each module. By default, the system displays only the monitoring data of third-party modules with requests. You can move the pointer over the trend chart to view data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image.

##### 6.4.4.5 View PANGU monitoring data

You can view PANGU monitoring data to analyze the cluster status in real time.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Monitor** tab, and then click **Pangu Monitoring**.
5. Click **Analytics**.
After the analysis is complete, you can view the check items, check levels, and check results. You can click the name of a failed check item and view the error details in the dialog box that appears. Then, troubleshoot the error based on the error description, suggestions, and details.

#### 6.4.5 Configure clusters

##### 6.4.5.1 Modify KV configurations

You can modify the monitoring data capacity and other configurations of key-value (KV) servers. You can also enable or disable automatic partition splitting for KM masters. In most cases, you can retain the default KV configurations. We recommend that you modify the KV configurations under the guidance of technical experts.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Configure** tab.
5. In the left-side pane, click **KV Configurations**, and then click the KV Server tab or KM
Master tab to modify the KV configurations. After the modification is complete, you must wait for the new configurations to take effect. You can view the modification progress below the configuration item list. Modify the configurations of KV servers On the **KV Server** tab, click **Edit** in the **Actions** column of configuration items such as KV Monitoring Data Capacity (MB), Memfile Cell Dump Threshold, KV Reclaimed Bandwidth (MB), and Maximum Capacity of Log Data per Recycle (MB). Enable or disable automatic partition splitting for KM masters To enable or disable automatic partition splitting, click the **KM Master** tab, and then click
**Edit** in the **Actions** column of the Automatic Partition Split configuration item. By default,
automatic partition splitting is enabled. We recommend that you retain the default setting.

##### 6.4.5.2 Configure the EC type

If you enable the erasure coding (EC) mode, Object Storage Service (OSS) uses the configured EC type to store OSS data. You can configure an EC type based on the number of servers. This way, when the ECFoldChunks alert is triggered, you can view the number of folded chunks to measure the volume of folded data.

**Background information**

EC is a data protection method in which data is split, encoded, and then stored in a distributed manner. A piece of data is split into N original data chunks of the specified size, and M parity chunks are created during encoding. The total is N+M chunks. These chunks are stored in different servers, so at least N+M servers are required. The original data can be restored even if M servers fail, and M chunks are damaged or lost. When servers fail, multiple chunks can be folded to be stored on one server. In this case, fewer than N+M servers are used to store the chunks. However, this undermines data security. Up to M folded chunks can be stored on one server. If this server fails, all M chunks may be lost. If more than one servers fail, data loss occurs.

**Usage notes**

After the EC mode is enabled for a cluster, you cannot disable this mode for the cluster, which means you cannot switch to the triplicate storage mode. Proceed with caution.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Configure** tab.
5. In the left-side pane, click **EC Configurations**. On the page that appears, turn on EC
Switch and configure the Configuration Type parameter based on the number of servers. At least N+M servers are required to store N+M chunks. If more than one servers fail after chunks are folded, data loss occurs. To improve data security, we recommend that you use N+2M servers.
6. Click **Save**.

**View the number of folded chunks**

In normal cases, the number of folded chunks in a cluster is 0. If the number of available servers drops below N+M because some servers fail or enter the sub-healthy state, some data in the cluster is folded. You can view the number of folded chunks in a specified time period to measure the volume of folded data.

**Important**

The data folding in a cluster may be caused by server-related errors. We recommend that you check and handle related alerts at the earliest opportunity. For more information, see Handle current alerts.
1. On the Cluster O&M page, click the **Configure** tab.
2. In the left-side pane, click **EC Configurations**. In the **Number of Folded Chunks** section
of the page that appears, select a time period and click OK to view the number of folded chunks within the specified time period.

##### 6.4.5.3 Configure execution time for background tasks

**tasks**

If you want to run background tasks at a specific point in time, such as lifecycle tasks and garbage collection (GC) tasks, you can configure the execution time of tasks.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Configure** tab.
5. In the left-side pane, click **Task Configuration**. Select the Lifecycle or GC tab based on
your business requirements to configure execution time. After you configure an execution time for a background task, the system automatically runs the background task at the specified point in time. Background tasks are asynchronously configured with a specific delay. You can perform the following steps to view the status of the configuration: In the left-side navigation pane, choose CDS-System Management > Tasks. On the Tasks page, you can view the status of tasks. Configure execution time for lifecycle tasks On the **LifeCycle** tab, find the task that you want to manage and click **Edit** in the
**Actions** column. In the Modify Lifecycle Configurations dialog box, configure the Daily
Run Time parameter.

> **Important:** The execution time is displayed in UTC. Take note of the differences between the UTC time and the standard time of your region.

Configure execution time for GC tasks On the **GC** tab, find the task that you want to manage and click **Edit** in the **Actions** column. In the Modify GC Configurations dialog box, configure the Daily Run Time parameter.

> **Important:** The execution time is displayed in the standard time of your region.

##### 6.4.5.4 Configure a global flag

You can configure the settings of each service in the cluster based on your business requirements. In most cases, you can use the default global flag configuration. If you need to configure a global flag, configure the settings under the guidance of professional staff.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Configure** tab.
5. In the left-side pane, click **GlobalFlag Management**. On the page that appears, query or
configure global flags by using one of the following methods: On the **Lite Edition** tab, query or configure a global flag based on the global flag name. Query a global flag based on the global flag name Select a global flag name from the Flag Name drop-down list. The configurations of the global flag on different servers are displayed in the right-side table, such as the service type, flag value, and server IP address. Select a global flag name from the Flag Name drop-down list and configure the Flag parameter. Then, click **Submit** to configure the value of the global flag. On the **Professional Edition** tab, configure the parameters that are described in the following table and click **Submit**.

| Parameter | Description |
|---|---|
| Service Type | The type of the background service module. Valid values: oss service, _ oss, and img. |
| Roles | The role in the service. Valid values: all, master, and worker. You can configure this parameter only if you set the Service Type parameter to oss service. _ |
| Actions | The operation that you want to perform. Valid values: set: configures a global flag. get: queries a global flag. |
| Flag Name | The name of the global flag. |
| Flag | The value of the global flag. You can configure this parameter only if you set the Actions parameter to set. |
| Remarks | The remarks of the global flag. You can configure this parameter only if you set the Actions parameter to set. |

##### 6.4.5.5 Configure PANGU Service

You can view and configure the replica traffic control, cluster recycle bin, and full-cluster offline inspection features and service quotas based on your business requirements. Configure replica traffic control You can configure the maximum and minimum replication speeds based on your business requirements to control data replica traffic. If you want to quickly replicate data, you can increase the maximum and minimum replication speeds. If you do not want the replication to consume a large amount of resources, you can reduce the maximum and minimum replication speeds.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Configure** tab, and then click **Pangu Configuration**.
5. On the **Replica Flow Control** tab, you can view the names and values of replica traffic
control rules and change the values to modify the replication speed based on your business requirements.
6. Modify the replication speed based on your business requirements.
i. Click **Edit** in the **Actions** column of a replica traffic control rule. ii. In the **Modify Configuration** dialog box, modify the maximum or minimum replication speed. This way, you can set an upper or lower limit on the speed at which data is read from the source server or written to the destination server. The valid value of the maximum or minimum replication speed is 1 to 100000, measured in MB/s.

> **Important:** We recommend that you set the maximum or minimum replication read speed and the maximum or minimum replication write speed to the same value. Otherwise, data is replicated based on the smaller speed value that you set.

The read/write speed settings affect the performance of servers. Proceed with caution. iii. Click **OK**.

**Configure cluster recycle bin**

1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. Click the **Cluster Recycle Bin Settings** tab to view the recycle bin settings and modify
the settings based on your business requirements. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Recycle Bin (TRUE or FALSE) | Specifies whether to enable the recycle bin feature. Valid values: TRUE (default): enables the recycle bin feature. If the recycle bin feature is enabled, files deleted from the cluster are temporarily stored in the recycle bin. FALSE: disables the recycle bin feature. If the recycle bin feature is disabled, files deleted from the cluster are directly deleted and not stored in the recycle bin. |
| General Recycling Percentage | If the available disk space is smaller than the value specified by this parameter, junk data is deleted from the system at the general recycling speed. |

| Emergency Recycling Percentage | If the available disk space is smaller than the value specified by this parameter, junk data is deleted from the system at the emergency recycling speed. Note The emergency recycling speed is faster than the general recycling speed. |
|---|---|
| Recycle Bin Retention Period (Seconds) | In most cases, set this parameter to 86400. Valid values: 3600 to 8640000000. Unit: seconds. |

3. Modify the cluster recycle bin settings based on your business requirements.
i. Click **Edit** in the **Actions** column of a parameter. ii. In the **Modify Configuration** dialog box, change the value of the parameter based on your business requirements. You can configure multiple parameters to achieve the effect of operations described in the following table:

| Operation | Description |
|---|---|
| Disable automatic recycling | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 0. |
| Freeze the recycle bin | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 0, and set the Recycle Bin Retention Period (Seconds) parameter to 8640000000. Note After you freeze the recycle bin, files in the recycle bin are not deleted. This ensures data security. |
| Clear the recycle bin | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 100. |
| Disable the recycle bin feature | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 100. After all files in the recycle bin are deleted, set the Recycle Bin (TRUE or FALSE) parameter to FALSE. |

iii. Click **OK**.

**Enable or disable full-cluster offline inspection**

If you enable the full-cluster offline inspection feature, the system automatically analyzes the status of clusters on a regular basis.
1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. On the **Full-cluster Offline Inspection** tab, check whether the full-cluster offline
inspection feature is enabled. You can enable or disable the feature based on your business requirements.
3. Enable or disable the full-cluster offline inspection feature.
i. Click **Edit** in the **Actions** column. ii. In the **Modify Configuration** dialog box, change the status of the full-cluster offline inspection feature. Valid values: enable and disable. If you want to enable the full-cluster offline inspection feature, select enable. If you want to disable the feature, select disable. iii. Click **OK**.

**View quotas and QoS**

1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. Click the **Quotas and QoS** tab to view the basic information, quotas, and QoS of the
cluster.

> **Note:** The basic information and QoS are displayed only for hybrid clusters of CDS-OSS and CDS-EBS. If the cluster is a CDS-OSS cluster, only the quota of the Object Storage Service (OSS) service is displayed.

Basic Information: In this section, you can view the cluster type, QoS feature status, HDD VIOPS, SSD VIOPS, total storage usage, and total capacity of the SSD cache. Quota: In this section, you can view the current used capacity, capacity quota for cluster storage, and status of different services. QoS: In this section, you can view the proportions of different services on HDDs and SSDs.

#### 6.4.6 Manage services

##### 6.4.6.1 Manage KV services

In an index system, Key-value (KV) Master nodes can manage and schedule partitions. KV Server nodes can configure indexes of partitions and store data. Key Management (KM) Master nodes can schedule and distribute loads to balance loads of each partition. KM Server nodes can execute tasks. If O&M personnel need to analyze an issue, O&M personnel can locate and troubleshoot the issue by using the information about KV services such as KV Master and KV Server nodes or restarting the corresponding KV services.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Service** tab.
5. In the left-side pane, click **KV Service**. Click a tab based on your business requirements to
configure KV services. Configure KV Master nodes On the **KVMaster** tab, you can view the server information about the KV Master node and perform operations based on your business requirements.

| Operation | Description |
|---|---|
| Obtain the build information | Obtain the build information about a server. This helps you locate issues by providing the version information. Click Build Information in the Actions column. You can obtain detailed build information about the KV Master node. |
| Restart the service | Click Restart in the Actions column to restart the service of the KV Master node. Warning Security risks may arise if your restart services. Proceed with caution. |

Configure KV Server nodes On the **KVServer** tab, you can view the server information about the KV Server node and perform operations based on your business requirements.

| Operation | Description |
|---|---|
| Obtain the build information | Obtain the build information about a server. This helps you locate issues by providing the version information. Click Build Information in the Actions column. You can obtain detailed build information about the KV Server node. |
| Restart the service | Click Restart in the Actions column to restart the service of the KV Server node. Warning Security risks may arise if your restart services. Proceed with caution. |
| Add a server to the blacklist or remove a server from the blacklist | Click Add to Blacklist in the Actions column to add the server to the blacklist. Warning After you add a server to the blacklist, the server is unavailable. Proceed with caution. If you want to remove a blocked server from the blacklist, clickD elete Blacklist to remove the server from the blacklist. |

Configure KM Master nodes On the **KMMaster** tab, you can view the server information and scheduling information about the KM Master node and perform operations based on your business requirements.

| Operation | Description |
|---|---|
| View KM configurations | In the Host Management section, click View KM Configurations to view the configurations of the KM Master node. |
| Restart the service | In the Host Management section, find the server that you want to manage and click Restart in the Actions column to restart the service on the KM Master node. Warning Security risks may arise if your restart services. Proceed with caution. |
| View scheduling information | In the Scheduling Information section, specify a time range to view the scheduling information within the specified time range. |

Configure KM Server nodes On the **KMServer** tab, you can view the server information about the KM Server node and perform operations based on your business requirements.

> **Warning:** Security risks may arise if your restart services. Proceed with caution.

Find the server that you want to restart and click **Restart** in the **Actions** column to restart services on the KM Server node.

##### 6.4.6.2 Manage access-layer services

If O&M personnel analyzes an error and determines that the error is caused by an exception in an access-layer service, the O&M personnel can restart the access-layer service, such as TEngine, OssServer, and OssImageServer, to resolve the error.

**Background information**

> **Warning:** Do not restart services on frontend servers. Contact Alibaba Cloud for technical support if you need help.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the Cluster O&M page, click the **Service** tab.
5. In the left-side pane, click **Front-end Service**. On the page that appears, click the
TEngine, OssServer, or OssImageServer tab to manage the corresponding access-layer services. Manage TEngine On the **TEngine** tab, you can view the server IP addresses of TEngine and restart a service based on your business requirements. Click **Restart** in the **Actions** column to restart a service on TEngine. Manage OssServer On the **OssServer** tab, you can view the server IP addresses of OssServer and perform operations based on your business requirements.

| Operation | Description |
|---|---|
| Obtain the build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. Click Build Information in the Actions column to obtain the detailed build information about OssServer. |
| Restart a service | Click Restart in the Actions column to restart a service on OssServer. |

Manage OssImageServer On the **OssImageServer** tab, you can view the server IP addresses of OssImageServer and restart a service based on your business requirements. Click **Restart** in the **Actions** column to restart a service on OssImageServer.

##### 6.4.6.3 Manage PANGU Service

You can manage meta servers, chunk servers, and file information based on your business requirements. Manage meta servers
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the page that appears, click the **Service** tab.
5. In the left-side navigation tree, click **Pangu Service**. Click the **Meta Server** tab. On this
tab, view the information about the meta servers and perform operations on the meta servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Switch the primary meta server | In most cases, you do not need to manually switch the primary meta server. You need to manually switch the primary meta server only if the current primary meta server fails. In most cases, the switchover takes a few seconds. To switch the primary meta server, perform the following operations: Find the secondary meta server that you want to manage and click Switch to Primary Meta Server in the Actions column. |
| Generate checkpoints | Generate checkpoints to record the runtime data of the meta server. In most cases, the generated information is stored on the system disk of the meta server. To generate checkpoints, perform the following operations: Find the meta server that you want to manage and click Generate CPT in the Actions column. |
| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information, perform the following steps: Find the meta server that you want to manage and click Build Information in the Actions column. |

Manage chunk servers
1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**. Click the **Chunk Server** tab. On this
tab, view the information about the chunk servers and perform operations on the chunk servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Set the chunk server status | Find the chunk server that you want to manage and clickS et Status in the Actions column. In the Set Server status dialog box, select a server state. You can select one of the following states: Read-only, Normal, and Shut-down. Warning Security risks may arise if you shut down a server. Proceed with caution. |

| Add a server to the blacklist or remove a server from the blacklist | If upper-layer services do not need to write data to a chunk server for the moment, the chunk server can be added to the blacklist. After a chunk server is added to the blacklist, no chunks are assigned to the chunk server, and no data is written or copied to the chunk server. Warning After you add a chunk server to the blacklist, the chunk server is unavailable. Proceed with caution. To add a chunk server to the blacklist, perform the following steps: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Add to Blacklist. To remove a chunk server from the blacklist, perform the following steps: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Remove from Blacklist. |
|---|---|
| Restart services | Restart the services on a chunk server. Warning Security risks may arise if you restart services. Proceed with caution. To restart the services on a chunk server, perform the following steps: Find the chunk server that you want to manage and click Restart Service in the Actions column. |
| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information about a chunk server, perform the following steps: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Build Information. |

**Manage files**

1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**. Click the **Files** tab. On this tab, view
the information about the system root directories and perform operations on the directories based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View the quotas on the root directory | Click View Root Directory Quota to view the quotas on the following items: EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength. The FileLogicalLength and FilePhysicalLength items are measured in bytes. The following list describes the quota items: EntryNumber: the total number of files and directories that can be stored in the root directory. FileNumber: the total number of files that can be stored in the root directory. FileLogicalLength: the maximum logical size of files in the root directory. FilePhysicalLength: the maximum physical size of files in the root directory. |
| Search for files | Enter the ID of the file for which you want to search in the search box in the upper-right corner and click Search. |
| View and manage directories Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a directory: View the quotas on the directory Click View Quota in the Actions column. You can view the quotas on the EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength items. Fix or unfix the directory Click Fix in the Actions column to fix the directory. After the directory is fixed, you cannot move or delete the directory. To move or delete the directory, click Unfix in the Actions column to unfix the directory. |

| View and manage files Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a file: View the information about chunks Find the file that you want to manage and clickV iew Chunk Information in the Actions column. You can view the basic information and chunk information about the file. The basic information includes the file ID, file type, number of chunks, and application name. The chunk information includes the chunk ID, chunk status, and server. Modify the number of replicas PANGU stores multiple replicas of a file to improve the reliability of the file. You can configure the number of replicas for files. A file with more replicas improves data security and occupies larger storage space. We recommend that you set both the minimum number and maximum number of replicas to three. Find the file that you want to configure and clickE dition in the Actions column. Modify the Minimum Number of Replicas and Maximum Number of Replicas parameters to configure the number of replicas that are stored for the file in PANGU. If data is lost, copied, or migrated, the system copies or deletes the file based on the number of replicas. |
|---|---|
| Clear the recycle bin Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | Find the deleted directory and click Clear Recycle Bin in the Actions column to delete the files in the recycle bin. Note The file recycling policy of a deleted directory is the same as the settings of the cluster recycle bin. |

#### 6.4.7 Manage buckets

##### 6.4.7.1 Manage bucket information

On the Bucket page, you can view information about the buckets in a specific cluster or location, manage bucket attributes, and view monitoring information about the buckets.

**Prerequisites**

Object Storage Service (OSS) buckets are created. For more information, see the "Create buckets" topic of the OSS documentation in **CDS User Guide**.

**Query buckets**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Bucket > Buckets**.
3. On the **Buckets** page, select a cluster or a location.
After you search for the buckets, you can view the list of buckets and perform operations based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View bucket information | View the information about buckets, including the bucket name, UID, BID, storage type, and bucket version. |
| View bucket details | Click the name of a bucket. On the Bucket Details page, configure the bucket attributes and view the monitoring information about the bucket. For more information, see the Manage bucket details section of this topic. |

**Manage bucket details**

1. In the left-side navigation pane, choose **CDS-OSS > Bucket**.
2. On the **Bucket** page, click a bucket name.
3. On the **Bucket Details** page, configure the bucket attributes and view the monitoring
information about the bucket. Configure bucket attributes In the **Attributes** section, view the information about the bucket, such as the bucket name, bucket status, creation time, and storage type. You can also perform operations on the bucket attributes based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Configure the bucket status | a. Click Settings next to Bucket Status. b. In the Configure Bucket Status dialog box, select a state. You can select one of the following states for the bucket: Normal, Disable, The space is used up, and The liquidity quota is used up. c. Click OK. |

| Manage user information | You can manage the information about the bucket owner. You can view the user details, set the OSS usage status, view the change history of the OSS usage status, view the bucket names, and set a limit on the number of buckets. Click Details next to UID. In the User Details panel, view the username, UID, OSS usage status, change history, number of buckets, and limit on bucket quantity. You can also perform the following operations based on your business requirements: Set the OSS usage status Click Configure next to OSS Usage Status. In the Configure OSS Usage Status dialog box, select a state and enter the cause of the status change. You can select one of the following states: Normal, Disable, The space is used up, and The liquidity quota is used up. View the change history of the OSS usage status After the OSS usage status of a bucket changes, you can view the number of changes and the change history. Click View next to Change History. In the OSS Usage Status Change History message, view the change history of the OSS usage status, including the cause of change and the modification time. View bucket names Click View next to Buckets to view the names of the buckets that the user owns. Set a limit on the number of buckets Click Settings next to Limit on Bucket Quantity. In the Configure Limit on User Bucket Quantity dialog box, set the maximum number of buckets that can be created. If you set the Limit on Bucket Quantity parameter to -1, the maximum number of buckets that can be created is not limited. |
|---|---|

View the monitoring information about the bucket On the **Monitor** tab, specify a time range to view the service level agreement (SLA), traffic, queries per second (QPS), latency, HTTP status, and storage capacity of the bucket within the specified period of time. Move the pointer over a trend chart to view the data for a specific point in time. You can view the following monitoring data in the trend chart: SLA: the SLA that is provided by OSS. The SLA of OSS is calculated based on the following formula: `Number of requests for which a non-5XX status code is returned`

```
per 10 seconds or 1 hour/Number of valid requests × 100% .
```

Traffic: the traffic that is generated by the bucket. QPS: the number of API requests. Latency: the latencies of API requests and the maximum value of the latencies. HTTP status: the number of the returned 5xx, 403, 404, 499, 4xx_other, 2xx, and 3xx status codes and the percentage of the requests that return these codes. Storage capacity: the storage capacity of the bucket. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image. View resource attribute source data Click the icon in the upper-right corner to view the resource attribute source data.

##### 6.4.7.2 Query bucket information

You can query buckets by Apsara Stack tenant account, user ID (UID), or bucket name. After you query a bucket, you can view the bucket details, manage the bucket, and delete the bucket.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Bucket > Bucket Query**.
3. On the **Bucket Query** page, select a filter condition and enter a value.
The following table describes the supported filter conditions.

| Filter condition | Description |
|---|---|
| Apsara Stack Tenant Account | Enter the username of an Apsara Stack tenant account to query the buckets that belong to the account. |
| UID | Enter the UID of a user to query the buckets that belong to the user. |
| Bucket Name | Enter a bucket name to query a specific bucket. |

4. Click **View**.
The system displays the basic information about the user and the buckets that belong to the user. You can perform operations based on your business requirements. Manage basic user information In the **User Basic Information** section, you can view the user information, modify the user status, modify the number of buckets that can be created, and view the change history of the user status.

| Operation | Description |
|---|---|

| Modify user status | Important Modifying the user status is a high-risk operation. We recommend that you do not modify the user status unless necessary. User states include [OK] Normal State, [DISABLE] closed state, [SPACE FULL] _ storage space is full, and [FLOW FULL] Reach maximum traffic. You can _ modify the user status based on your business requirements. a. Click Modify user status in the Actions column. b. In the Modify user status dialog box, select a user status and specify the reason for changing the user status. c. Click Confirm. |
|---|---|
| Modify the number of buckets that can be created | Important Modifying the number of buckets that can be created is a high-risk operation. Proceed with caution. By default, a user can create a maximum of 100 buckets. You can adjust the maximum number of buckets that a user can create based on your business requirements. a. Click Modify the number of buckets that can be created in the Actions column. b. In the Modify the number of buckets that can be created dialog box, specify the maximum number of buckets that can be created. Valid values: 100 to 10000. Select a value based on your business requirements. c. Click Confirm. |
| View the status change history of the user | View the change history of the user, such as the operator who modified the user status, the modified status, and the reason. To view the change history, click View user status change history in the Actions column. |

Buckets that meet the filter conditions are displayed in the bucket list. You can view bucket information and manage buckets based on business requirements.

| Operation | Description |
|---|---|

| View bucket details | Find the bucket that you want to view and clickV iew Details in the Actions column. On the Bucket Query page, view the bucket details on the Bucket Basic Information and Data Monitoring tabs. View the basic information On the Bucket Basic Information tab, view the usage overview, basic information, and feature configurations of the bucket, and perform operations based on your business requirements. View usage information In the Usage overview section, click the Table or Graphics tab to switch the desired information layout. Click See more capacity details to view usage details. Manage buckets In the Basic information section, find the ViewBucket row in the table and click View in XML to view the bucket details in the XML format. Click Manage Bucket to go to the OSS O&M console where you can manage the bucket. Click View Modification History to view the change history of the bucket. If you want to view the details of a specific change record, click View in the Actions column. View monitoring data On the Data Monitoring tab, select a time range and a sampling interval, and click View to view the monitoring data that is collected at the specified interval within the specified time range. The monitoring data includes the service level agreement (SLA), traffic, queries per second (QPS), latency, HTTP status codes, and storage capacity. |
|---|---|

| Manage buckets | Find the bucket that you want to manage and clickM anage in the Actions column. Change the bucket status On the Modify status tab, select a bucket state and click Configure. Bucket states include [OK] Normal State, [DISABLE] closed state, [SPACE FULL] storage space is full, and [FLOW FULL] Reach _ _ maximum traffic. The default status is [OK] Normal State. If you do not prohibit valid operations on the bucket, use the default settings. If you want to prohibit all operations on the bucket, set the bucket to the [DISABLE] closed state or [FLOW FULL] Reach maximum _ traffic state. If you want to allow only the Get, List, and Delete operation on the bucket and prohibit the Put and Post operations on the bucket, set the bucket to the [SPACE FULL] storage space is full state. _ Configure the bucket ACL On the R&W permissions (ACL) settings tab, select an access control list (ACL) for the bucket and click Configure. You can set a bucket to Public reading, Public reading and writing, and Private. If you want to allow all users to read objects from and write objects to the bucket, set the bucket to Public reading and writing. If you want to allow only the bucket owner to write objects to the bucket and allow other users to only read objects from the bucket, set the bucket to Public reading. If you want to allow only the bucket owner to read objects from and write objects to the bucket and block access from all other users, set the bucket to Private. |
|---|---|
| Delete buckets | Important If you delete a bucket, all objects in the bucket are also deleted. Buckets and objects cannot be recovered after they are deleted. Proceed with caution. You can delete a bucket if you no longer use it. Find the bucket that you want to delete and clickD elete in the Actions column. In the Warning message, click Execute. |

##### 6.4.7.3 Configure QoS information

This topic describes how to configure quality of service (QoS) information for users or buckets to limit the total upstream traffic, total downstream traffic, and total queries per second (QPS) of users or buckets. QoS configuration prevents a single user or bucket from occupying excessive network and system resources.

**Manage user QoS information**

You can configure QoS information for users to limit the total upstream traffic, total downstream traffic, and total QPS available to users.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Bucket > QoS Configuration**.
3. On the **User QoS** tab, enter a UID, select a cluster, and then click **View**.
The system displays the QoS configuration information of the specified user.
4. If no QoS rule is configured for the user, you can add a QoS configuration as required.
i. Click **Add Configuration**. ii. In the Add Configuration dialog box, configure the UID, frontend server cluster, total upstream traffic, total downstream traffic, and total QPS. To configure QoS information for more metrics, such as the upstream traffic over the Internet and downstream traffic over the internal network, click **More Configuration**. To perform more fine-grained QoS configuration for CPU usage and specific operations, click the plus icon next to **More Configurations** and configure the maximum QPS. iii. Click **Determine**.

**Manage bucket QoS information**

You can configure QoS information for buckets to limit the total upstream traffic, total downstream traffic, and total QPS of buckets.
1. On the **QoS Configuration** page, click the **Bucket QoS** tab.
2. On the **Bucket QoS** tab, enter the name of the bucket that you want to search for and click
**View**.
The system displays information about the bucket for which the QoS rules are configured.
3. If no QoS rule is configured for a bucket, you can add a QoS configuration as required.
i. Click **Add Configuration**. ii. In the **Add Configuration** dialog box, configure the bucket name, total upstream traffic, total downstream traffic, and total QPS. To configure QoS information for more metrics, such as the upstream traffic over the Internet and downstream traffic over the internal network, click **More Configuration**. To protect the QoS configuration of a bucket from user throttling, turn on **Independent**
**of User Flow Control**.
To perform more fine-grained QoS configuration for CPU usage and specific operations, click the plus icon next to **More Configurations** and configure the maximum QPS. iii. Click **Determine**. By default, the QoS rule is disabled after it is configured. You can click **Enable** in the
**Actions** column of the QoS rule to make the QoS configuration of the bucket take effect.

**What to do next**

After a QoS rule is configured, you can manage the QoS rule based on your business requirements.

| Operation | Description |
|---|---|

| View the details of the QoS rule | Click Detail in the Actions column of the QoS rule to view the details of the QoS rule, such as extended configurations. |
|---|---|
| Modify the QoS rule | If the QoS rule does not meet your requirements, you can click Modify in the Actions column of the QoS rule to modify it. You can quickly modify the QoS rule by increasing or decreasing the parameter values. |
| Enable or cancel the QoS rule | To enable the QoS rule, click Enable in the Actions column. After the QoS rule is enabled, you can clickC ancel in the Actions column to disable it. |
| Quickly create a QoS rule | Click Copy in the Actions column of the QoS rule to copy the information of the QoS rule to quickly configure the QoS information of other resources. |

#### 6.4.8 Manage synchronization configurations

##### 6.4.8.1 Manage synchronization processes

This topic describes how to manage the cross-region or cross-cloud synchronization processes in a source cluster in a centralized manner. For example, you can view the synchronization status, configure the quality of service (QoS) settings, and configure the number of subqueues.

**Prerequisites**

Cross-region or cross-cloud synchronization processes are configured. For more information, see Configure cross-region synchronization processes and Configure crosscloud synchronization processes. Cross-region replication or cross-cloud replication is enabled for buckets in the Object Storage Service (OSS) console by using the Apsara Uni-manager Management Console. For more information, see the "Configure CRR rules" or "Configure cross-cloud replication" section of the Cloud Defined Storage User Guide.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Synchronization Management >**
**Synchronization Process Management**.
3. On the **Synchronization Process Management** page, select a source cluster and click
**Query**.
The information about related synchronization processes in the cluster is displayed on the page. You can manage the synchronization processes based on your business requirements. The following table describes the operations that you can perform:

| Operation | Description |
|---|---|
| View synchronization details | Click Detail in the Actions column of a synchronization process to view information about the process, such as the source bucket, source region, destination bucket, synchronization type, and synchronization status. |
| View the status of a synchronization process | Click Status in the Actions column of a synchronization process to view the detailed status information. |
| View the QoS settings of a synchronization process | Click View QOS in the Actions column of a synchronization process to view the QoS settings of the process, such as the bandwidth consumption and the queries per second (QPS) during incremental synchronization. |
| Configure the QoS settings of a synchronization process | Click Set up QOS in the Actions column of a synchronization process to configure parameters such as Execution type and Timing execution. |
| Configure the number of subqueues | Click Set the number of subqueues in the Actions column of a synchronization process to configure the number of subqueues in the process. |

##### 6.4.8.2 Configure a cross-region synchronization process

**process**

You must enable the cross-region synchronization process before you enable cross-region data replication between buckets. Then, log on to the Apsara Uni-manager Management Console and go to the OSS console to configure cross-region replication for the buckets.

**Prerequisites**

The region ID of the destination region is obtained.

**Usage notes**

The source and destination regions must reside in the same cloud, and the network between the two regions is connected.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Synchronization Management >**
**Cross-region Synchronization Process Configuration**.
3. On the **Cross-region Synchronization Process Configuration** page, click **Add**.
4. Select the source and destination regions and click **OK**.
After you configure the cross-region synchronization process, you can view the synchronization information, such as the source region and creation time. To modify the destination region, click **Modify** in the **Actions** column of the synchronization process.

**What to do next**

In the Apsara Uni-manager Management Console, go to the OSS console to configure crossregion replication. For more information, see the "Configure cross-region replication" topic under "OSS > Bucket" in CDS User Guide.

**Related operations**

To manage a synchronization process, such as viewing the synchronization status and configuring quality of service (QoS) for the synchronization process, you can perform the operations on the **Synchronization Process Management** page. For more information, see Manage a synchronization process.

##### 6.4.8.3 Configure a cross-cloud synchronization process

**process**

To enable cross-cloud data replication between buckets, you must configure a proxy user and a bucket in the destination cloud, enable the cross-cloud synchronization process, and then configure a cross-cloud replication task for the source bucket in the Apsara Uni-manager Management Console.

**Usage notes**

Make sure that the network between the two clouds is connected.

**Before you begin**

Before you configure a cross-cloud synchronization process, you must create a proxy user and a bucket in the destination cloud and grant permissions on the bucket in the source cloud.

**Create a proxy user in the destination cloud and grant**

**permissions to the user**

Create a proxy user in the Apsara Uni-manager Management Console of the destination cloud and grant the permissions to access OSS to the proxy user.
1. Log on to the Apsara Uni-manager Management Console of the destination cloud.
2. Create a Resource Access Management (RAM) role and grant permissions to the role.
i. In the top navigation bar, click **Enterprise**. In the left-side navigation pane, choose
**Permissions** > **Role Permissions**.
ii. On the Role Permissions page, click **Create Custom Role**. In the lower-left corner of the Create Role page, click **Advanced Settings**. Then, click **Create RAM Authorization**. iii. On the Create RAM Authorization page, configure the Role Name and Description parameters, and click **Create and Configure RAM Authorization** . iv. In the Role Permissions step, click the **Permissions** tab. Then, click **Add Policy**. v. In the Add Policy dialog box, click **Create Policy**. In the Create Policy dialog box, configure the policy name, enter the following policy content, and then click **OK**. `{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": "oss:*",
      "Resource": [
        "acs:oss:*:*:*"
```

`]` `}` `]` `}`
3. Create a user and a user group.
i. In the left-side navigation pane, choose **Users** > **User Groups**. ii. On the User Groups page, click **Create User Group**. In the Create User Group dialog box, configure the User Group Name, Organization, and Role Permissions parameters, and click **OK**.

> **Note:** Set the Role Permissions parameter to the RAM role that you created in the preceding step.

iii. In the left-side navigation pane, choose **Users** > **Users**. iv. On the System Users tab of the Users page, click **Create User**. In the Create User dialog box, configure the parameters, including the User Name, Display Name, Role, Organization, Phone, and Email parameters, and click **OK**.

> **Note:** You cannot set the Role parameter to the RAM role that you created in the preceding step.

v. In the AccessKey Information message, save the AccessKey pair of the user.
4. Record the UID.
i. In the left-side navigation pane, choose **Resources** > **Organizations**. ii. In the Organization Structure section, click the organization to which the created user belongs, click the User tab, and then click the name of the created user. On the page that appears, save the UID of the user.

**Add the proxy user to the OCM list in the destination cloud**

> **Important:** All modifications on the OCM list take effect 30 minutes later.

In the Apsara Uni-manager Management Console of the destination cloud, log on to the OSS O&M console and then add the proxy user to the OCM list.
1. Log on to the OSS O&M console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**. iii. In the left-side navigation pane, choose **CDS-OSS > Cluster O&M**. iv. In the **Deploy Clusters** section of the **Cluster O&M** page, find the cluster that you want to manage and click **O&M**.

> **Note:** You can also select a cluster from the drop-down list in the upper-right corner of the Cluster O&M page.

v. In the upper-right corner of the **Cluster O&M** page, choose **More O&M Capabilities >**
**Object Storage Service O&M**.
2. In the left-side navigation pane of the OSS O&M console, choose **Service O&M - OSS >**
**OCM list management**.
3. On the **Special users** tab of the **OCM List Management** page, click **Add**.
4. In the Add List dialog box, set UID to the UID of the proxy user and set type to
**as_sync_admin**.
5. Click **Add**.

**Create a bucket in the destination cloud**

Log on to the Apsara Uni-manager Management Console of the destination cloud and go to the OSS console to create a bucket. For more information, see the "Create buckets" topic under "OSS > Getting started" in CDS User Guide.

**Grant permissions to the source bucket by using bucket**

**policies in the source cloud**

Log on to the Apsara Uni-manager Management Console of the source cloud, go to the OSS console, and configure bucket policies to grant the source bucket the permissions to write data to the destination bucket.
1. Log on to the OSS console.
i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Object Storage Service**.
2. In the left-side navigation pane, click Buckets. On the Buckets page, click the name of the
bucket.
3. On the page that appears, click the **Basic Settings** tab and find the **Bucket Policy**
section.
4. Click **Settings**.
5. On the **Syntax** tab, click Edit and enter a policy.
The following sample code provides an example on how to configure a policy.

> **Note:** Set Principal to the UID of the proxy user. Replace `bucket-name` with the actual bucket name.

`{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Effect": "Allow",
      "Action": "oss:*",
      "Principal": [
        "266808895180*****"
```

`],`

```json
      "Resource": [
        "acs:oss:*:*:bucket-name",
        "acs:oss:*:*:bucket-name/*"
```

`]` `},` `{`

```json
      "Effect": "Deny",
      "Action": [
        "oss:PutBucket*",
        "oss:DeleteBucket*"
```

`],`

```json
      "Principal": [
        "266808895180*****"
```

`],`

```json
      "Resource": [
        "acs:oss:*:*:bucket-name",
        "acs:oss:*:*:bucket-name/*"
```

`]` `}` `]` `}`
6. Click **Save**.

**Procedure**

Log on to the Apsara Uni-manager Operations Console of the source cloud and go to the Cloud Defined Storage (CDS)-OPS console to configure cross-cloud synchronization.
1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Synchronization Management >**
**Cross-cloud Synchronization Configuration**.
3. On the **Cross-cloud Synchronization Configuration** page, click **Create**.
4. In the **Create Cross-Cloud Synchronization Task** dialog box, set the Destination Cloud
Name, Destination Cloud Region/Location, Destination Cloud Domain Name, Proxy Account AccessKey ID, and Proxy Account AccessKey parameters.

> **Note:** On the **Cross-cloud Synchronization Configuration** page of the destination cloud, you can click **View Parameters of the Current Cloud** to obtain the parameters of the cloud.

5. Click **Submit**.
After you configure the cross-cloud synchronization process, you can view the synchronization process information, such as the destination cloud name and destination cloud region/location, and manage the cross-cloud synchronization process.

| Operation | Description |
|---|---|
| View parameters of the current cloud | To use the current cloud as the destination cloud of another cloud, select a cluster and click Parameters of the Current Cloud. In the Parameters of the Current Cloud dialog box, view and copy the required information. |
| Update information in the destination cloud | To change the destination cloud or the information in the destination cloud, click Update in the Actions column of the destination cloud to modify the cross-cloud synchronization parameters. |
| Delete the destination cloud | If you no longer need to synchronize data to a destination cloud, click Delete in the Actions column to delete the cloud. |

**What to do next**

In the Apsara Uni-manager Management Console, go to the OSS console to configure crosscloud replication. For more information, see the "Configure cross-cloud replication" topic under "OSS > Bucket" in CDS User Guide.

**Related operations**

To manage synchronization process information, such as viewing the synchronization process status and configuring quality of service (QoS) for the synchronization process, you can perform the operations on the **Synchronization Process Management** page. For more information, see Manage a synchronization process.

##### 6.4.8.4 View monitoring data of cluster synchronization

**synchronization**

The monitoring data of cluster synchronization shows the synchronization status of clusters and helps you identify and manage issues in a timely manner.

**Background information**

By default, the synchronization monitoring data of all clusters in the region is displayed. The monitoring data of a cluster, such as the number of synchronized files and fragments, is displayed only if a synchronization task and a data replication task are configured for the cluster. You can check whether a data replication task is configured for a cluster on the
**Synchronization Process Management** page. For more information, see Manage
synchronization processes. If no synchronization task is configured for a cluster or a synchronization task is configured but no data replication task is configured, the values of the monitoring metrics are 0.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > Synchronization Management >**
**Cluster Synchronization Monitoring**.
3. On the **Cluster Synchronization Monitoring** page, select a time range and click **View**.
The system displays the synchronization monitoring data of clusters in each region within the specified time range, including the number of errors of each type, the number of synchronized files, and the number of fragments.

#### 6.4.9 O&M robots

##### 6.4.9.1 Manage O&M robots

You can use O&M robots to perform automatic O&M tasks, such as intelligent analysis and diagnostics on faulty machines, automatic adjustment of KV recycle bins, intelligent analysis and diagnostics on frequent issues, automatic remediation of KV CheckReady failures, automatic write prohibition and recovery of PANGU, and emergency solutions for file damages. O&M robots simplify O&M operations and improve O&M efficiency.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > O&M Robot**.
3. On the **O&M Robot** tab, perform operations based on your business requirements.
By default, all O&M robots are enabled. You can click **Disable** in the **Operation** column of an O&M robot to disable the robot. After you disable an O&M robot, you can click **Enable** in the **Operation** column to re-enable the O&M robot.

| O&M robot | Description |
|---|---|
| Intelligent Analysis and Diagnosis of Faulty Physical Machines | After this O&M robot is enabled, if the system detects a faulty machine in the periodic inspection, the system automatically analyzes and diagnoses the failure, and then provides O&M suggestions for troubleshooting the issue. |
| Automatic Adjustment of KV Recycle Bin | After this O&M robot is enabled, if the trigger threshold for automatic reduction or the trigger threshold for automatic increase is reached, the system automatically adjusts the KV recycle bin. You can click Edit in the Operation column of the O&M robot to modify the trigger thresholds. |
| Intelligent Analysis and Diagnosis of Hot Issues | After this O&M robot is enabled, if the system detects KV hot issues in the periodic inspection, the system automatically analyzes and diagnoses the causes of the KV hot issues, and then provides O&M suggestions for troubleshooting the issues. |
| Automatic Repair of KV CheckReady Failure | After this O&M robot is enabled, if the system detects that KV CheckReady fails in the periodic inspection, the system automatically fixes the issue that caused the KV CheckReady failure. |

| Pangu Automatic Write Prohibition and Recovery | After this O&M robot is enabled, if the write prohibition threshold is reached, the system automatically prohibits write operations to PANGU. If the write recovery threshold is reached, the system automatically recovers write operations to PANGU. You can click Edit in the Operation column of the O&M robot to modify the thresholds. |
|---|---|
| Emergency Solution to Handle File Damages | After this O&M robot is enabled, if the system detects damaged files in the periodic inspection, the system automatically repairs the damaged files. |
| Automatic Decrease of kvbakroot | After these O&M robots are enabled, the system automatically adjusts the retention period of redo logs and metadata in the kvbakroot directory. You can click Edit in the Operation column of the O&M robots to modify the thresholds. |
| Automatic Increase of kvbakroot |   |
| Automatic Adjustment of GC Partition Quantity | After this O&M robot is enabled, the system automatically adjusts the number of OSS GC partitions based on the cluster size. |

##### 6.4.9.2 View historical O&M tasks

On the O&M History tab, you can view the history of different types of O&M tasks that are automatically executed by O&M robots.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-OSS > O&M Robot**.
3. Click the **O&M History** tab, select an O&M task type and specify a time range.
After you query an O&M task, you can view the name, batch sequence number, status, start time, and end time of the O&M task.

> **Note:** The values in the **Status** column indicate the status of the O&M task. Valid values: SCHEDULABLE, RUNNING, PAUSED, HUMAN_PROCESSING, COMPLETED, FAILED, TIMEOUT, and TERMINATED. SCHEDULABLE indicates the O&M task is not running. RUNNING indicates the O&M task is running. PAUSED indicates the O&M task is paused. HUMAN_PROCESSING indicates the O&M task is paused and waiting to be processed. COMPLETED indicates the O&M task is complete. FAILED indicates the O&M task is failed. TIMEOUT indicates the O&M task times out. TERMINATED indicates the O&M task is terminated.

You can click the plus icon before an O&M task to view the running information about the O&M task, such as the workflow ID, O&M result, and trigger type.

### 6.5 Manage log storage clusters

#### 6.5.1 Overview of Simple Log Service clusters

**clusters**

On the Cluster O&M page, you can view the capacity usage, current alerts, and deployment information about Simple Log Service clusters. This way, you can obtain the overall cluster information and manage issues at the earliest opportunity.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. On the **Cluster O&M** page, view the overall information about Simple Log Service clusters.
Overall information about Simple Log Service clusters View the capacity usage and current alerts of all Simple Log Service clusters. The following table describes the monitoring metrics.

| Metric | Description |
|---|---|
| Capacity Usage | The total capacity, consumed capacity, and percentage of consumed capacity of all Simple Log Service clusters. |
| Current Alerts | The numbers of alerts at different levels and the most recent five alert records in all Simple Log Service clusters. You can click More or an alert level to view and handle the alerts on the Current Alert page. For more information, see Handle alerts. |

View cluster deployment information You can view the information about all the deployed Simple Log Service clusters that are managed on the CDS-OPS platform. The cluster information includes the cluster name, cluster update time, cluster type such as CDS-EBS or CDS-EBS&CDS-OSS, data centers of the clusters, primary and secondary cluster identifiers that are used for zone-disaster recovery, percentage of consumed capacity, total cluster capacity, and consumed capacity. Clusters can be sorted in ascending or descending order by name, total capacity, or used capacity. By default, clusters are sorted in descending order based on their used capacity. You can select a proper sorting method as required. Click **O&M** in the upper-right corner of the cluster card to go to the **Cluster O&M** page. On this page, you can view cluster details, analyze cluster monitoring data, and configure features.

#### 6.5.2 Cluster overview

On the Overview tab, you can view the top 10 Logstores with the highest traffic and all projects in a cluster. You can also search for a specific project, modify project configurations, and delete projects that you no longer use.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. On the **Overview** tab, view the top 10 Logstores that have the highest traffic and all
projects in the cluster. You can also perform the following operations on the projects: Search for a project Enter a project name or an Alibaba Cloud account or ID to search for a project. View project information Click the project name. In the panel that appears, view the cluster, status, owner, and traffic limit per minute of the project. Modify project configurations Find the project that you want to manage and click **Modify** in the **Actions** column. In the panel that appears, modify the configurations based on your business requirements and click **Save**.

> **Important:** You cannot modify the settings of the Project Name, Cluster, and Owner parameters.

Delete a project

> **Important:** If you delete a project, the data in the project is deleted. After you delete a project, the project cannot be restored. Proceed with caution.

Find the project that you want to delete and click **Delete** in the **Actions** column. In the
**Delete** message, confirm the project information and click **OK**.

#### 6.5.3 View capacity information

On the Capacity tab, you can view the logical capacity usage, physical capacity usage, and physical capacity usage trend of a Simple Log Service cluster.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Capacity** tab to view the capacity information about the cluster.
Logical Capacity Usage: You can view the used logical capacity, total logical capacity, and percentage of used logical capacity of all Simple Log Service clusters. The total logical capacity indicates the maximum volume of data that can be written. It includes the storage space that is occupied by internal logic modules, such as the metadata, garbage collection (GC), and recycle bin. The used logical capacity indicates the volume of data that has been written. Click **More** in the upper-right corner of the Logical Capacity Usage section to view the number of replicas in the cluster. Physical Capacity Usage: You can view the used physical capacity, total physical capacity, and percentage of used physical capacity. The total physical capacity indicates the maximum size of data that can be written to the cluster. The used physical capacity indicates the used physical capacity reported by PANGU. Click**More** in the upper-right corner of the Physical Capacity Usage section to view the details of the bare disk capacity, total capacity, system reserved capacity, OP reserved storage capacity, used physical capacity, and available physical capacity.

> **Note:** After you move the pointer over the
> icon on the right side of a capacity, the
> system displays the description and calculation formula of the capacity in the tooltip.

Physical Capacity Usage Trends: Click the **Capacity Trend** tab. Specify a time range to view the total and used physical capacity.

> **Note:** Click **Actions** in the upper-right corner of a metric region. Select **Download Data** to download the monitoring data to your on-premises machine, or select **Save as** **Image** to save the monitoring data as an image.

Capacity Prediction After the system collects the capacity data of storage services deployed in a new cluster for 50 days, the system predicts the capacity usage for the next week once a day. O&M staff can perform operations such as cluster scale-up or scale-down based on the predicted capacity usage at the earliest opportunity. This prevents cluster failures that may be caused by exhausted storage capacity and ensures the security and stability of the cluster. Click the **Capacity Prediction** tab to view the predicted physical capacity usage.

> **Note:** The predicted capacity usage is for reference only. Perform operations based on the actual capacity usage.

Capacity prediction depends on the accumulation of sufficient samples. If the number of data in a cluster is less than 50 days old, the system cannot predict the capacity. No prediction data is available for a newly deployed cluster.

#### 6.5.4 View PANGU monitoring data

You can view PANGU monitoring data to analyze the cluster status in real time.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Monitor** tab, and then click **Pangu Monitoring**.
5. On the **Pangu Monitoring** tab, click **Analytics**.
The system starts cluster analysis. After the analysis is complete, you can view the check items, check levels, and check results.

> **Note:** It takes a while to complete the cluster analysis.

You can click the name of a failed check item and view the error details in the dialog box that appears. Then, troubleshoot the error based on the error description, suggestions, and details.

#### 6.5.5 Configure clusters

##### 6.5.5.1 Configure an EC type

You can configure an erasure coding (EC) type for your Simple Log Service cluster based on the number of servers.

**Usage notes**

You cannot modify EC settings when O&M operations are performed on servers in the cluster. Wait until the O&M operations are complete and try again.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.
4. On the Cluster O&M page, click the **Configure** tab.
5. In the **EC Configuration** section, turn on EC Switch and configure an EC type based on the
number of servers. If the number of servers is 6 to 13, set the **Configuration Type** parameter to **2+2** or
**4+2**.
If the number of servers is greater than or equal to 14, set the **Configuration Type** parameter to **8+3**.
6. Click **Save**.

##### 6.5.5.2 Configure PANGU Service

You can view and configure the replica traffic control, cluster recycle bin, and full-cluster offline inspection features and service quotas based on your business requirements.

> **Important:** If you modify cluster information, system exceptions may occur. Proceed with caution.

View replica traffic control settings You can configure the maximum and minimum replication speeds based on your business requirements to control the rate of data replica traffic. If you need to quickly replicate data, you can increase the maximum and minimum replication speeds. If you do not want the replication to occupy a large amount of resources, you can decrease the maximum and minimum replication speeds.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Configure** tab, and then click **Pangu Configuration**.
5. On the **Replica Flow Control** tab, you can view the names and values of replica traffic
control rules and change the values to modify the replication speed based on your business requirements.
6. Modify the replication speed based on your business requirements.
i. Click **Edit** in the **Actions** column of a replica traffic control rule. ii. In the **Modify Configuration** dialog box, modify the maximum or minimum replication speed. This way, you can set an upper or lower limit on the speed at which data is read from the source server or written to the destination server. The valid value of the maximum or minimum replication speed is 1 to 100000, measured in MB/s.

> **Important:** We recommend that you set the maximum or minimum replication read speed and the maximum or minimum replication write speed to the same value. Otherwise, data is replicated based on the smaller speed value that you set.

The read/write speed settings affect the performance of servers. Proceed with caution. iii. Click **OK**.

**View cluster recycle bin configurations**

If the recycle bin feature is enabled, files that are deleted during various operations on a cluster are temporarily stored in the recycle bin. If the recycle bin feature is disabled, files deleted from a cluster are directly deleted and not stored in the recycle bin.
1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. Click the **Cluster Recycle Bin Settings** tab to view the recycle bin configurations and
modify the configurations based on your business requirements. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Recycle Bin (TRUE or FALSE) | Specifies whether to enable the recycle bin feature. Valid values: TRUE (default): enables the recycle bin feature. If the recycle bin feature is enabled, files deleted from the cluster are temporarily stored in the recycle bin. FALSE: disables the recycle bin feature. If the recycle bin feature is disabled, files deleted from the cluster are directly deleted and not stored in the recycle bin. |
| General Recycling Percentage | If the available disk space is smaller than the value specified by this parameter, junk data is deleted from the system at the general recycling speed. |
| Emergency Recycling Percentage | If the available disk space is smaller than the value specified by this parameter, junk data is deleted from the system at the emergency recycling speed. Note The emergency recycling speed is faster than the general recycling speed. |

| Recycle Bin Retention Period (Seconds) | In most cases, set this parameter to 86400. Valid values: 3600 to 8640000000. Unit: seconds. |
|---|---|

3. Modify the cluster recycle bin configurations based on your business requirements.
i. Click **Edit** in the **Actions** column of a parameter. ii. In the **Modify Configuration** dialog box, change the value of the parameter based on your business requirements. You can configure multiple parameters to achieve the effect of operations described in the following table:

| Operation | Description |
|---|---|
| Disable automatic recycling | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 0. |
| Freeze the recycle bin | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 0, and set the Recycle Bin Retention Period (Seconds) parameter to 8640000000. Note After you freeze the recycle bin, files in the recycle bin are not deleted. This ensures data security. |
| Clear the recycle bin | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 100. |
| Disable the recycle bin feature | Set the Recycle Bin (TRUE or FALSE) parameter to TRUE, and set both the General Recycling Percentage and Emergency Recycling Percentage parameters to 100. After all files in the recycle bin are deleted, set the Recycle Bin (TRUE or FALSE) parameter to FALSE. |

iii. Click **OK**.

**View full-cluster offline inspection status**

After you enable the full-cluster offline inspection feature, the system automatically analyzes the status of clusters on a regular basis.
1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. On the **Full-cluster Offline Inspection** tab, check whether the full-cluster offline
inspection feature is enabled. You can enable or disable the feature based on your business requirements.
3. Enable or disable the full-cluster offline inspection feature.
i. Click **Edit** in the **Actions** column. ii. In the **Modify Configuration** dialog box, change the status of the full-cluster offline inspection feature. Valid values: enable and disable. If you want to enable the full-cluster offline inspection feature, select enable. If you want to disable the feature, select disable. iii. Click **OK**.

**View quotas**

1. Click the **Configure** tab, and then click **Pangu Configuration**.
2. Click the **Quotas and QoS** tab to view the cluster quota information.
The quota information includes the consumed capacity, capacity quota on cluster storage, and quota status.

#### 6.5.6 Manage PANGU Service

You can manage meta servers, chunk servers, and file information based on your business requirements. Manage meta servers
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Log Storage > Cluster O&M**.
3. In the **Deploy Cluster** section of the **Cluster O&M** page, find the cluster that you want to
manage and click **O&M**.

> **Note:** You can also directly select the cluster in the upper-right corner of the page to view and manage the cluster.

4. Click the **Service** tab.
5. In the left-side navigation tree, click **Pangu Service**, and then click the **Meta Server** tab.
On this tab, view the information about the meta servers and perform operations on the meta servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Switch to the primary meta server | In most cases, you do not need to manually switch to the primary meta server. You need to manually switch to the primary meta server only if the current primary meta server fails. In most cases, the switchover takes a few seconds. To switch to the primary meta server, perform the following operations: Find the secondary meta server that you want to manage and click Switch to Primary Meta Server in the Actions column. |

| Generate checkpoints | Generate checkpoints to record the runtime data of the meta server. In most cases, the generated information is stored on the system disk of the meta server. To generate checkpoints, perform the following operations: Find the meta server that you want to manage and click Generate CPT in the Actions column. |
|---|---|
| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information, perform the following operations: Find the meta server that you want to manage and click Build Information in the Actions column. |

Manage chunk servers
1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**, and then click the **Chunk Server** tab.
On this tab, view the information about the chunk servers and perform operations on the chunk servers based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| Specify the chunk server status | Find the chunk server that you want to manage and clickS et Status in the Actions column. In the Set Server status dialog box, select a server state. You can select one of the following states: Read-only, Normal, and Shut-down. Warning Security risks may arise if you discontinue a server. Proceed with caution. |

| Add a server to the blacklist or remove a server from the blacklist | If upper-layer services do not need to write data to a chunk server for the moment, the chunk server can be added to the blacklist. After a chunk server is added to the blacklist, no chunks are assigned to the chunk server, and no data is written or copied to the chunk server. Warning After you add a chunk server to the blacklist, the chunk server is unavailable. Proceed with caution. To add a chunk server to the blacklist, perform the following operations: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Add to Blacklist. To remove a chunk server from the blacklist, perform the following operations: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Remove from Blacklist. |
|---|---|
| Restart services | Restarts the services on a chunk server. Warning Security risks may arise if you restart services. Proceed with caution. To restart the services on a chunk server, perform the following operations: Find the chunk server that you want to manage and click Restart Service in the Actions column. |
| Obtain build information | After you obtain the build information, you can provide the detailed version information to facilitate troubleshooting. To obtain the build information about a chunk server, perform the following operations: Find the chunk server that you want to manage, move the pointer over the icon in the Actions column, and then click Build Information. |

**Manage files**

1. Click the **Service** tab.
2. In the left-side navigation tree, click **Pangu Service**, and then click the **Files** tab. On this
tab, view the information about the system root directories and perform operations on the directories based on your business requirements. The following table describes the operations that you can perform.

| Operation | Description |
|---|---|
| View the quotas on the root directory | Click View Root Directory Quota to view the quotas on the following items: EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength. The FileLogicalLength and FilePhysicalLength items are measured in bytes. The following list describes the quota items: EntryNumber: the total number of files and directories that can be stored in the root directory. FileNumber: the total number of files that can be stored in the root directory. FileLogicalLength: the maximum logical size of files in the root directory. FilePhysicalLength: the maximum physical size of files in the root directory. |
| Search for objects | Enter the ID of the file for which you want to search in the search box in the upper-right corner and click Search. |
| View and manage directories Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a directory: View the quotas on the directory Click View Quota in the Actions column. You can view the quotas on the EntryNumber, FileNumber, FileLogicalLength, and FilePhysicalLength items. Fix or unfix the directory Click Fix in the Actions column to fix the directory. After the directory is fixed, you cannot move or delete the directory. To move or delete the directory, click Unfix in the Actions column to unfix the directory. |

| View and manage files Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | You can perform the following operations on a file: View the information about chunks Find the file that you want to manage and clickV iew Chunk Information in the Actions column. You can view the basic information and chunk information about the file, such as the file ID, file type, number of chunks, and application name. Modify the number of replicas PANGU stores multiple replicas of a file to improve the reliability of the file. You can configure the number of replicas for files. A file with more replicas improves data security but occupies larger storage space. We recommend that you set both the minimum number and maximum number of replicas to three. Find the file that you want to configure and clickE dition in the Actions column. Modify the Minimum Number of Replicas and Maximum Number of Replicas parameters to configure the number of replicas that are stored for the file in PANGU. If data is lost, copied, or migrated, the system copies or deletes the file based on the number of replicas. |
|---|---|
| Clear the recycle bin Warning A system exception may occur if you modify a directory or a file. Proceed with caution. | Find the deleted/ directory and click Clear Recycle Bin in the Actions column to delete the files from the recycle bin. Note The file recycling policy of the deleted/ directory is the same as the settings of the cluster recycle bin. |

## 7 Monitoring center

### 7.1 View the custom dashboard

You can view the monitoring metrics that you select from the Resource Monitoring page on the Custom Dashboard page.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Monitoring Center > Custom Dashboard**.
3. On the **Custom Dashboard** page, query or remove custom monitoring data.
Query monitoring data You can specify a time range to query the monitoring data of metrics that you select from the Resource Monitoring page. Remove monitoring data If you no longer need to view a monitoring data chart, click **Remove** in the upper-right corner of the chart.

### 7.2 Monitor resources

You can monitor the performance of various resources, such as clusters, hosts, and disks. You can also add monitoring metrics to your custom dashboard. This way, you can quickly view monitoring data of resources.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Monitoring Center > Resource**
**Monitoring**.
3. On the **Resource Monitoring** page, select a resource type.
Cluster To monitor clusters, click the **Cluster** tab. On the Cluster tab, select one or more clusters and query the CPU utilization, memory usage, load, and IOPS of the clusters. Host To monitor hosts, click the **Host** tab. On the Host tab, select the cluster in which the host resides, and query the CPU utilization, memory usage, load, IOPS, Network Time Protocol (NTP), and traffic of the host. Disk To monitor disks, click the **Disk** tab. On the Disk tab, select the cluster and host of the disk, select the disk that you want to monitor, and then query the IOPS of the disk. Click **Actions** in the upper-right corner of the IOPS chart. Select **Download Data** to download the monitoring data to your on-premises machine, or select **Save as Image** to save the monitoring data as an image.

### 7.3 Query storage metrics

You can query the storage metrics of Elastic Block Storage (EBS) and Object Storage Service (OSS) based on your business requirements.

**Query storage metrics of EBS**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Monitoring Center > Storage Metrics**.
3. On the Storage Metrics page, click the **Elastic Block Storage** tab. On the Elastic Block
Storage tab, query the cluster storage metrics of EBS. Specify a time range or click a time range to view the monitoring data of EBS within the specified time range, such as the inventory capacity trend chart, cloud disk and snapshot trend chart, physical capacity usage trend chart, average latency, and total IOPS and throughput of the EBS cluster. The following table describes the metrics.

| Metric | Description |
|---|---|
| Inventory Capacity Trend Chart | The inventory capacity usage of the cluster. You can query the inventory capacity usage of the cluster only by the day. The monitoring data of the current day is generated on the next day. |
| Cloud Disk and Snapshot Trend Chart | The usage of disks and snapshots in the cluster. You can query the disk and snapshot usage of the cluster only by day. The monitoring data is generated on a daily basis. You can view the following monitoring data in the trend chart: Disks: the total number of disks. Snapshots: the total number of snapshots. |
| Physical Capacity Usage Trend Chart | The physical capacity usage of the cluster. You can view the following monitoring data in the trend chart: Total Capacity: the maximum storage capacity of a cluster that can be used to write data. Used Capacity: the used physical capacity that is reported by PANGU. |
| Average Latency | The average read latency and write latency of the cluster. You can view the following monitoring data in the trend chart: Read Latency: the average read latency. Write Latency: the average write latency of the cluster. |

| Total Cluster IOPS | The total numbers of read operations and write operations per second in the cluster. You can view the following monitoring data in the trend chart: Read IOPS: the total number of read operations per second in the cluster. Write IOPS: the total number of write operations per second in the cluster. |
|---|---|
| Total Cluster Throughput | The total throughput of data reads and writes in the cluster. You can view the following monitoring data in the trend chart: Read: the total throughput of data reads in the cluster. Write: the total throughput of data writes in the cluster. |

**Query storage metrics of OSS**

1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-Monitoring Center > Storage Metrics**.
3. On the Storage Metrics page, click the **OSS** tab. On the OSS tab, query the storage metrics
of OSS. View cluster metrics of OSS In the left-side pane, click **Cluster Metrics**. You can specify a time range or click a time range to view the monitoring data within the specified time range, such as the bucket storage size, service level agreement (SLA), HTTP status, requests per second (QPS), bandwidth, and latency of the OSS cluster. View bucket metrics Click **Bucket Metrics**. In the Bucket Metrics section, enter a bucket name and specify a time range. You can also click a time range to view the metrics of the specified bucket, such as the storage usage, SLA, HTTP status, QPS, traffic, and Latency.

**Note**

To obtain the bucket name, go to the **Buckets** page of CDS-OSS. For more information, see Manage bucket information.

**What to do next**

Move the pointer over the data trendline to show data at a specific point in time. In the **Actions** column of each metric, you can select **Download Data** to download the monitoring data to your computer, or select **Save as Image** to save the monitoring data as an image. To add a metric to a custom dashboard, click **Add to Custom Dashboard** in the upperright corner and select the metric. For more information about how to view metrics on a custom dashboard, see View the custom dashboard.

### 7.4 Query service monitoring data

You can query service monitoring data based on your business requirements.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Monitoring Center > Service Monitoring**.
3. View the monitoring data of different services.
On the**Apsara Distributed File System** tab, select a cluster, a host, a time period, and metrics to view the corresponding monitoring data. The available metrics include PG_MS_CPUUsage, which measures the CPU usage by the master process, PG_CS_CPUUsage, which measures the CPU usage by the chunkserver process, PG_CS_DiskCapacity, which measures the disk usage by the chunkserver process, and PG_CS_ReadWriteThroughput, which measures the throughput of read/write operations other than replication for the chunkserver process. View the monitoring data of Object Storage Service (OSS) On the**OSS** tab, select a cluster, a host, a time period, and metrics to view the corresponding monitoring data. The available metrics include KV Add Latency, KV Query Latency, KV Read Amplication, and KV Write Amplication. View the monitoring data of Elastic Block Storage (EBS) On the**Elastic Block Storage** tab, select a cluster, a host, a time period, and metrics to view the corresponding monitoring data. The available metrics include PG_BM_MigrationMediumUsage, which measures the cluster usage, PG_BS_IoLatency, which measures the block server latency during each task, PG_BS_Throughput, which measures the read/write traffic processed by the block server per second, and PG_BS_Iops, which measures the number of I/O operations processed by the block server per second.

> **Note:** Click **Actions** in the upper-right corner of a chart to download the data or save the charge as an image.

## 8 Event Alerts

### 8.1 Alert overview

On the Alert Overview page, you can view the current alerts, alert statistics, and alert history.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Event Alerts > Alert Overview**.
3. On the **Alert Overview** page, view the alert information.

| Section | Description |
|---|---|
| Current Alerts | In this section, you can view the number of alerts at each level in all clusters and the most recent five alert records. You can click More in the upper-right corner of the section or an alert level to view and handle the alerts on the Current Alert page. |
| Alarm Statistics | In this section, alert statistics are displayed in charts by cluster or by service. The statistics include the current number of alerts. You can filter alerts by alert level. The most frequently triggered five alerts are displayed, including the alert name and frequently. |
| Alert History | In this section, the most recent five alert records are displayed, including the alert name, service, cluster name, and alert time. You can click More in the upper-right corner of the section to view the details of historical alerts on the Alert History page. |

### 8.2 Alert management

#### 8.2.1 Learn the alert handling process

This topic describes the process of handling alerts. Alerts can be handled by using the following process:
1. The alert owner handles alerts on a daily basis. For more information, see Handle current
alerts. The alert owner must check and handle alerts in a timely manner after receiving the alerts. After an alert and the related issues are handled, the alert owner can manually clear the alert. After you manually clear an alert, the alert is moved to the Alert History page.
2. View alert history on a regular basis. For more information, see View alert history.

#### 8.2.2 Handle current alerts

The alerts that are managed by Cloud Defined Storage (CDS)-OPS come from the CDS clusters and the clusters that are managed by CDS-OPS. After alerts are triggered in the system, you can view the list of alerts and the details of each alert, including the alert name, service, cluster name, description, resource name, and alert time. We recommend that you handle alerts at the earliest opportunity by confirming or clearing the alerts based on your business requirements.

**Procedure**

1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Event Alerts > Current Alert**.
The system automatically obtains and displays the current alert information about all clusters.
3. On the **Current Alert** page, select an alert name, a service, a cluster name, an alert level,
and a time range to view alerts that meet the filter alerts. To view the details of an alert, such as the alert ID and alert cause, click **Details** in the
**Actions** column.
4. Confirm or clear the alerts based on your business requirements.

| Operation | Description |
|---|---|
| Confirm an alert | After you receive an alert, you can confirm the alert to indicate that the alert is received and is being handled. Select the alert that you want to confirm and clickC onfirm Alert In the upper- left corner. After you confirm the alert, the value in the Confirmed column changes to Yes. |
| Clear an alert | After you resolve the issue of an alert or determine that an alert can be ignored, you can manually clear the alert to indicate that the alert is handled. After you manually clear an alert, the alert is moved to the Alert History page. Select the alert that you want to clear and clickM anually Clear in the upper-left corner. |

#### 8.2.3 View alert history

Alerts that are automatically or manually cleared are displayed on the Alert History page. You can view the information about alerts within a specified time period, including the alert name, service, cluster name, description, resource name, auto recovery status, confirmation status, and recovery time.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Event Alerts > Alert History**.
The system automatically obtains and displays the information about historical alerts of all clusters within one day.
3. On the **Alert History** page, select a service, a cluster, an alert level, and a time period to
view the corresponding historical alerts. The following table describes the items that are displayed on the Alert History page:

| Parameter | Description |
|---|---|
| Alert Name | The name of the alert. The severity is displayed to the left of the alert name. Valid values for severity: P1 Emergency, P2 Serious, P3 Warning, and P4 Reminder. |
| Service | The service for which the alert is triggered. |
| Cluster Name | The name of the cluster in which the alert is triggered. |
| Description | The description of the alert. |
| Resource Name | The details of the resource that triggers the alert, such as the cluster in which the alert is triggered. The information about alert sources varies based on the type of the alert. The actual alert source information prevails. |
| Alert Time | The time when the alert is triggered. |
| Recovered At | The time when the system automatically recovers or recovers after the alert is handled. If the alert is ignored and manually cleared, the recovery time is the time when the alert is manually cleared. |
| Auto Recovery | Indicates whether the system automatically recovers from the alert. Valid values: Yes: The alert is not confirmed but the system automatically recovers. No: The alert is manually handled and cleared. |
| Confirmed | Indicates whether the alert is manually handled. Valid values: Yes: The alert is manually handled. No: The alert is not manually handled. |
| Actions | The operations that can be performed on the alert. To view the details of an alert, such as the alert ID and cause, clickD etails in the Actions column. On the Alert Details page, click Handling suggestion to view the suggestions. Note If no suggestions are available, contact technical support. |

### 8.3 Event center

On the Event Center page, you can view the events generated for Elastic Block Storage (EBS) clusters of all types. EBS clusters include EBS-1.0 clusters, EBS-2.0 clusters, and CDS-EBS clusters.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Event Alerts > Event Center**.
The system automatically obtains and displays the event information within the last day in all clusters that contain the EBS service. Click **Details** in the **Actions** column of the event whose information you want to view. In the Event Details panel, you can view the information about the event such as the ID, event level, event type, submitter IP, occurrence time, and data.

> **Note:** Events are at the following levels: **Debugging**, **Notification**, **Warning**, and **Critical**. Pay attention to the events whose levels are **Warning** and **Critical**.

3. **Optional:** On the **Event Center** page, query events by specified conditions.
Simple query You can specify a time range to view all events within the specified time range. Advanced query Click **Advanced Filter** to specify filter conditions such as the time range, event type, event source, and event level. Click **Search** to view all events that meet the specified conditions.

## 9 Routine Inspection

### 9.1 Inspection Center

By default, the system uses built-in inspection items to regularly inspect clusters. On the Inspection Center page, you can view the information about the latest inspection results of different inspection items and manually run inspection tasks.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Routine Inspection > Inspection Center**.
The last inspection result of each inspection item is displayed.

> **Note:** Only Elastic Block Storage (EBS) supports inspection.

3. On the **Inspection Center** page, you can perform the following operations:
View the latest inspection results of a cluster Select a cluster name to view the latest inspection results of the cluster. The **Statistics** column displays the numbers of Critical, Warning, Error, and Normal inspection results in sequence. The **Last Executed At** column displays the time of the last inspection. Manually run an inspection task Find the inspection item that you want to inspect and click **Execute** in the Actions column. In the **Perform Inspection** message, click **OK**. View and export inspection results Find the inspection item that you want to view and click a number in the **Statistics** column. On the **Inspection Results** page, the results of the last inspection are displayed. On the **Inspection Results** page, you can perform the following operations: View the details of the last inspection View the information about the last inspection, including the cluster name, inspection status, and metric. Export the inspection execution details On the **Inspection Results** page, click **Export**. Filter inspection results by cluster name and inspection status Select a cluster name and a state to filter inspection details. View the execution history of an inspection item Find the inspection item that you want to view and click the time in the **Last Executed**
**At** column. On the **Inspection History** page, the inspection history of the last day is
displayed. You can perform the following operations on the **Inspection History** page: View inspection history View the start time, completion time, statistics, execution status, and progress of the inspection item of the last day.

> **Note:** The number of times that different inspection items are executed within a day varies based on the execution schedules.

Filter historical inspections Select a time range to filter historical inspections within the specified time range. View and export inspection results Click a number in the **Statistics** column. On the **Inspection Results** page, view and export the inspection results.

### 9.2 SLA monitoring

The system monitors key service level agreement (SLA) metrics of Cloud Defined Storage (CDS) in real time. This monitoring service provides an availability guarantee for scenarios such as software update, configuration change, and service O&M. This allows you to detect system exceptions at the earliest opportunity and minimize the impact when exceptions occur.

**View the SLA monitoring information**

1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Routine Inspection > SLA Monitoring**.
3. On the **SLA Monitoring** page, view the check results of SLA system links. The check is
performed every minute. You can also view the details of real-time SLA exceptions. In normal cases, the heartbeat check results in the last 5 minutes are displayed. The system automatically refreshes the heartbeat status and the details of real-time SLA exceptions every 1 minute. This allows O&M engineers to obtain the SLA system link status at the earliest opportunity when updating the system.

> **Important:** Only Elastic Block Storage (EBS) supports SLA monitoring.
> The system collects SLA data every minute. The displayed data may have a latency of minutes.
> If the SLA system link has exceptions, the Heartbeat Check section stops refreshing. In this case, the system displays the check results before the SLA system link has exceptions.
> If no new heartbeat check results are displayed for more than two minutes, you need to troubleshoot the issue. Make sure that the SLA metric query link is normal and that the clock of the server on which the service is running is not lagging behind.

If the SLA system link has exceptions, the exceptions that are detected by the current check are displayed in the **Details of Real-time SLA Exceptions** section. The following table describes the SLA exceptions.

> **Note:** The Details of Real-time SLA Exceptions section displays the exceptions that are detected in the last check. If no SLA exceptions are detected in the next check, the Details of Real-time SLA Exceptions section refreshes, and no exceptions are displayed. Use the view historical exceptions feature to view historical SLA exceptions.

| Parameter | Description |
|---|---|
| Time | The point in time at which the exception was reported. This point in time is slightly later than the actual point in time at which the exception occurred. |
| SLA Dimension | The dimension that is used for the SLA monitoring. Only cluster-level SLA monitoring is supported. Cluster Name is the only value in the SLA Dimension column. |
| Dimension Value | The value of the SLA dimension. The value is the cluster name. |
| Details | The details of the exception. You can move the pointer over the value in this column to view the complete exception information to help you identify the cause of the exception. Such information includes the cause of the exception and the IP address of the machine on which the exception occurred. |

**View historical SLA exceptions**

1. On the **SLA Monitoring** page, click **View Historical Exceptions**.
2. In the **History SLA Exceptions** panel, select a cluster name and specify a time range.
By default, historical SLA exceptions in the last hour are displayed. You can view historical SLA exceptions in the last 30 days.

## 10 Intelligent O&M

### 10.1 Host O&M

#### 10.1.1 View all workflows

On the All Workflows tab of the Host O&M page, you can view the details of the scale-up, scale-down, node replacement, and node maintenance workflows of different clusters. You can also manage the workflows based on your business requirements.

**Background information**

You can select one of the following types of workflow based on your business requirements: CDS Cluster Scale Up, CDS Cluster Scale Down, CDS Cluster Node Replacement, and CDS Cluster Node Repair. If you need to add or remove physical hosts in a cluster to optimize the allocation of computing and storage resources, you can initiate a CDS Cluster Scale Up or CDS Cluster Scale Down workflow. For more information, see Initiate a CDS Cluster Scale Up workflow and Initiate a CDS Cluster Scale Down workflow. If a physical host in a cluster is abnormal and needs to be replaced, you can initiate a CDS Cluster Node Replacement workflow. For more information, see Initiate a CDS Cluster Node Replacement workflow. If a physical host in the cluster fails and needs to be repaired, you can initiate a CDS Cluster Node Repair workflow. For more information, see Initiate a CDS Cluster Node Maintenance workflow.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Host O&M**.
3. On the **All Workflows** tab, view all workflows and perform operations based on your
business requirements.

| Operation | Description |
|---|---|

| Search for workflows | You can search for workflows by workflow type, status, and time range. To search for workflows by conditions, perform the following steps: i. Specify the cluster name, workflow type, and workflow status. The Workflow Status parameter indicates the status of workflows. Valid values: Schedulable: The workflow is created but not scheduled to run on a server. Running: The workflow is running. Paused: The workflow is automatically paused or manually paused because manual operations are required. For example, a node repair workflow is paused because the node must be powered off for maintenance. Pending Manual Intervention: Exceptions occur in a specific step of the workflow. If the exceptions are manually fixed and the step can be successfully executed, the restored workflow continues. Complete: The workflow is complete. You can view the execution duration and end time of a complete workflow. Failed: The workflow fails. If the workflow fails, contact Apsara Stack technical support. Timed Out: The workflow times out. Unexpectedly Terminated: If the workflow is waiting for manual intervention or is manually stopped, and the workflow no longer needs to be executed, the workflow is marked as discarded by an operator. ii. Specify the time range. |
|---|---|
| Restore workflows | You may need to manually intervene or stop a workflow due to exceptions. To restore the workflow, click Restore in the Execution Details column. Important If you want to forcefully redistribute a task, make sure that no relevant process is running on the server. If the logs are not refreshed after you restore the workflow, selectF orce Redistribute Task to forcefully redistribute the task when you try to restore the workflow again. |

| Manage workflows | View the workflow details and pause, repair, restore, or discard workflows based on your business requirements. Find the workflow that you want to manage. Click Details in the Actions column. In the Workflow Details panel, you can perform the following operations: View workflow information You can view the basic information about the workflow, steps of the workflow, and execution logs of the current step. Note The information and specific steps that are displayed vary based on workflow types. The information displayed in the console prevails. Click All Parameters to view the instance parameters and initialization parameters. Refresh workflow information Click Refresh to refresh the workflow information. Stop the workflow Click Stop to stop the execution of subsequent steps of the current workflow. Note After you click Stop, the system waits for the current step to finish before stopping the workflow. The system does not stop the current step that is being executed. If you want to stop the current step, stop the process of the step in the cluster. Restore the workflow You may need to manually intervene or stop the workflow due to exceptions. To restore the workflow, click Restore. Important If you want to forcefully redistribute a task, make sure that no relevant process is running on the server. If the logs are not refreshed after you restore the workflow, selectF orce Redistribute Task to forcefully redistribute the task when you try to restore the workflow again. Repair the workflow Click Repair to fix the workflow in which exceptions occur. Discard the workflow If the workflow is not complete and you no longer need to execute the workflow, click Discard to discard the workflow. Important A discarded workflow cannot be restored. Proceed with caution. |
|---|---|

#### 10.1.2 Initiate a CDS Cluster Scale Up workflow

**workflow**

If you need to add physical hosts to a cluster to properly allocate computing and storage resources, you can initiate a CDS Cluster Scale Up workflow to scale up the cluster. You can use the workflow to track the scale-up progress. This simplifies O&M operations and improves O&M efficiency.

**Prerequisites**

Before you scale up a cluster, make sure that the hosts used for the scale-up exist in the cluster of the buffer project. You can perform the following steps to check whether hosts are available in the clusters.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management**.
3. On the **Product & Cluster O&M** page, enter **buffer** in the **Product & Cluster** field.
4. Click **Cluster Details** in the **Actions** column, and then click the **Machines** tab. The list of
available hosts in the buffer is displayed.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Host O&M**.
3. On the Host O&M page, click the **Initiate Workflow** tab. On the Initiate Workflow tab, find
the CDS Cluster Scale Up workflow and click **Initiate** in the **Actions** column.
4. In the **Initiating the workflow [Scale Up]** dialog box, configure the Destination Cluster
and Up-scalable Hosts parameters. If you select an up-scalable host, **Forced machine model** and **Force Data Center**
**Consistent** are enabled by default to filter the hosts of the same model and data center as
the hosts in the cluster. We recommend that you select such hosts to ensure the overall performance and stability of the cluster.
5. Click **OK**.
The system starts to execute the workflows in sequence. The execution takes some time.

**What to do next**

View workflow progress and manage workflows. For more information, see View all workflows.

#### 10.1.3 Initiate a CDS Cluster Scale Down workflow

**workflow**

If you need to reduce the number of physical hosts in a cluster to change the allocation of computing and storage resources based on your requirements, you can initiate a CDS Cluster Scale Down workflow. You can use the workflow to track the scale-down progress. This simplifies O&M operations and improves O&M efficiency.

**Background information**

Before you initiate a CDS Cluster Scale Down workflow, take note of the following items: The cluster scale-down operation reduces the capacity and service capabilities of the cluster. Proceed with caution. The period of time that is required for the scale-down operation is positively correlated with the cluster usage. You can undeploy only worker nodes during the cluster scale-down operation. You can undeploy only one worker node at a time. Make sure that the cluster still has the required number of nodes after scale-down is complete.

> **Important:** The minimum number of nodes required varies depending on the storage service. The value displayed on the user interface shall prevail.

You cannot undeploy master nodes by performing scale-down operations. If you need to undeploy a master node, contact Apsara Stack technical support.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Host O&M**.
3. On the Host O&M page, click the **Initiate Workflow** tab. On the Initiate Workflow tab, find
the CDS Cluster Scale Down workflow and click **Initiate** in the **Actions** column.
4. In the **Initiating the workflow [Scale Down]** dialog box, configure the Destination
Cluster and Down-scalable Hosts parameters. If the host is down or disconnected, set **The host is down or disconnected.** to **Yes**. This way, the system accelerates the approval process in subsequent operations. Otherwise, set
**The host is down or disconnected.** to **No**.
5. Click **OK**.
The system starts to execute the workflows in sequence. The execution takes some time.

**What to do next**

View workflow progress and manage workflows. For more information, see View all workflows.

#### 10.1.4 Initiate a CDS Cluster Node Maintenance workflow

**Maintenance workflow**

When a physical host in a cluster fails and needs to be repaired, you can initiate a CDS Cluster Node Maintenance workflow to track the node maintenance process. This simplifies O&M operations and improves O&M efficiency.

**Background information**

Before you initiate a CDS Cluster Node Maintenance workflow, take note of the following items: The cluster maintenance process reduces the cluster capacity and service capabilities. Perform the operation during an appropriate period of time. The amount of time that is required for the maintenance is positively correlated with the cluster usage. You can repair only one node at a time by using a CDS Cluster Node Maintenance workflow.
1. Log on to the Cloud Defined Storage (CDS)-OPS console.
ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Host O&M**.
3. On the Host O&M page, click the **Initiate Workflow** tab. On the Initiate Workflow tab, find
the CDS Cluster Node Maintenance workflow and click **Initiate** in the **Actions** column.
4. In the **Initiating the workflow [Node Maintenance]** dialog box, configure the
Destination Cluster and Destination Host parameters and specify whether to enable the reclone feature and whether the host is down or disconnected. If you want to replace hardware such as the fan, power supply, and memory, you do not need to clone the host again. In this case, set **Reclone** to **No**. If you want to replace the system disk or repair the host, set **Reclone** to **Yes**. If the host is down or disconnected, set **The host is down or disconnected.** to **Yes**. This way, the system accelerates the approval process in subsequent operations. Otherwise, set
**The host is down or disconnected.** to **No**.
5. Click **OK**.
The system starts to execute the workflows in sequence. The execution takes some time.

**What to do next**

View workflow progress and manage workflows. For more information, see View all workflows.

### 10.2 Maintain disks

#### 10.2.1 Maintain corrupted disks

When a hard disk drive (HDD) or Non-Volatile Memory Express (NVMe) SSD disk of a chunk server is corrupted, you can view the information about the corrupted disk in real time and initiate disk replacement and disk hot maintenance after the data of the corrupted disk is backed up. After the disk hot maintenance is complete, you can view the maintenance history of the disk.

> **Note:** Cloud Parallel File Storage (CPFS) clusters do not support disk maintenance.

**Replace an HDD disk**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Disk Maintenance**.
3. On the Disk Maintenance page, click the Corrupted Disks tab. On the **Corrupted Disks** tab,
view and maintain corrupted disks. You can view the information about the disks, such as Chunk Server, Chunk Server IP Address, Disk ID, Disk Type, Status, Backup Status, and Process Status. When a disk is corrupted, the cluster automatically backs up the data of the disk. If the value of the **Backup Status** column of the disk is **Backup Completed**, the data of the disk is backed up.

> **Warning:** To prevent data loss, make sure that the data of a corrupted disk is backed up before you replace the disk.

i. Assist on-site maintenance personnel in locating the disk by turning on and off the disk light. a. Click **Locate Disk** in the **Actions** column of the corrupted disk. b. In the **Locate Disk** dialog box, click **On** next to **Disk Light Status**. After the disk light is turned on, you can click **Off** to turn off the light.

> **Note:** If the light fails to be turned on or the device does not support lighting, manually locate the corrupted disk. For more information about how to manually locate a disk, see Locate the physical location of a corrupted disk.

c. After you locate the disk, click **Disable**. ii. Initiate the disk replacement process.

> **Note:** If the current disk has an unfinished replacement process, click Replace Disk and the system will redirect you to the unfinished step in the disk replacement process.

a. Click **Replace Disk** in the **Actions** column of the corrupted disk. b. In the **Replace Disk** message, click **Confirm**. c. In the **Confirm** message, click **OK** to initiate the disk replacement process. iii. Perform a precheck. a. Click **Execute Check** to start a precheck. Precheck items include whether the chunk server of the disk is abnormal, disk status, and backup files. b. After the precheck is complete, click **Next**. iv. Uninstall the corrupted disk. a. Click **Execute Uninstall** to uninstall the corrupted disk. b. After the disk is uninstalled, click **Next**. v. Replace the corrupted disk with a new disk. a. Locate the corrupted disk based on the corrupted disk location and replace the disk. Click **Execute New Disk Identification**. If the disk is in a RAID architecture, the system obtains the location of the disk. You can locate the corrupted disk by turning on and off the disk light. If the disk does not have a RAID controller, you can locate the disk based on the corrupted disk locating process. You can verify whether the disk is correctly replaced by using the serial number. b. After you confirm the disk information, click **OK**. The system starts to recognize the new disk. If the new disk is not recognized, the system returns a warning message. The warning message does not interrupt subsequent steps. c. Click **Next**. vi. Initialize new disk. a. Set the device name of the new disk and click **Execute Initialize**. If the system recognizes the new disk in the previous step, you can select the name of the new disk from the drop-down list. Otherwise, manually specify a name for the new disk. b. After you confirm the disk information, click **OK** to initialize the new disk. c. After the new disk is initialized, click **Next**. vii. Attach the new disk. a. Click **Execute Attach** to attach the new disk. b. After the new disk is attached, click **Next**. viii. Activate the new disk. a. Click **Execute Activate** to activate the new disk. b. After the new disk is activated, click **Next**. ix. Verify the disk replacement result. a. Click **Execute Verify** to verify whether the disk is normal. b. After you confirm that the disk is normal, click **End**. c. In the **The process is ended.** message, click **OK**. After the disk replacement is complete, you can view the maintenance history of the disk on the **Disk Maintenance History** tab.

**Replace an NVMe SSD disk**

1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Disk Maintenance**.
3. On the Disk Maintenance page, click the Corrupted Disks tab. On the **Corrupted Disks** tab,
view and maintain corrupted disks. You can view the information about the disks, such as Chunk Server, Chunk Server IP Address, Disk ID, Disk Type, Status, Backup Status, and Process Status. When a disk is corrupted, the cluster automatically backs up the data of the disk. If the value of the **Backup Status** column of the disk is **Backup Completed**, the data of the disk is backed up.

> **Warning:** To prevent data loss, make sure that the data of a corrupted disk is backed up before you replace the disk.

i. Initiate a disk replacement process. a. Click **Replace Disk** in the **Actions** column of the corrupted disk. b. In the **Replace Disk** message, click **Confirm**.

> **Note:** NVMe SSDs cannot be located by turning on the light. Locate the disk to be replaced based on the disk location or the disk light status.

c. In the **Confirm** message, click **OK** to initiate the disk replacement process. ii. Check the environment. a. Click **Execute Check** to start an environment check. Environment check items include whether hot swapping is supported, whether the disk is in user mode, cluster usage, and workload, and whether the chunk server of the disk is abnormal. b. After the environment check is complete, click **Next**. iii. Check the backup status. Backup check items include the disk status, backup file status, and status file creation time. a. Click **Execute Check** to start a backup check. b. After the backup check is complete, click **Next**. iv. Uninstall the corrupted disk. In this step, the NVMe SSD disk is powered off. You can no longer manage the disk in user mode. After the power-off, if the disk has two lights including a power light, the power light is turned off. If the disk has only one light, the light stays on with no flashes because no data is written to the disk after the power-off. You can check the physical slot of the disk based on the status of lights. If you can see the disk serial number on the rack surface, confirm the serial number before you proceed. Otherwise, unplug the disk and confirm the disk serial number at the earliest opportunity. a. Click **Execute Uninstall** to uninstall the corrupted disk. b. After the disk is uninstalled, click **Next**. v. Replace the corrupted disk with a new disk. a. Locate the corrupted disk based on the corrupted disk location or the disk light status and replace the disk.

> **Important:** Make sure that the corrupted disk information matches the information about the disk whose disk light is off.

If the disk is in a RAID architecture, the system obtains the location of the disk. You can locate the corrupted disk by turning on and off the disk light. If the disk does not have a RAID controller, you can locate the disk based on the corrupted disk locating process. You can verify whether the disk is correctly replaced by using the serial number. b. After you confirm the new disk information, click **Execute Verify** to verify the new disk. c. After the verification is complete, click **Next**. vi. Switch the new disk to the user mode. In this step, the NVMe SSD disk is switched from the kernel mode to the user mode. a. Click **Execute Take Over** to switch the new disk to the user mode. b. After the new disk is switched to the user mode, click **Next**. vii. Initialize new disk. In this step, USSOS-related tools are used to initialize the new disk. a. Click **Execute Initialize** to initialize the new disk. b. After the new disk is initialized, click **Next**. viii. Activate the new disk. a. Click **Execute Activate** to activate the new disk. b. After the new disk is activated, click **Next**. ix. Verify the disk replacement result. After the new disk is activated and the disk is normal, you can end the disk replacement process. a. Click **Execute Verify** to verify whether the disk is normal. b. After you confirm that the disk is normal, click **End**. c. In the **The process is ended** message, click **OK**. After the disk replacement is complete, you can view the maintenance history of the disk on the **Disk Maintenance History** tab.

**What to do next**

After the disk replacement is complete, you can view the maintenance history of the disk on the **Disk Maintenance History** tab. For more information, see View disk maintenance history.

#### 10.2.2 Actively replace a disk

When a running hard disk needs to be replaced due to capacity upgrade, hard disk performance improvement, and regular maintenance, you can actively replace the disk. To replace a hard disk that is running properly, you need to change the status of the hard disk to Error, and then replace the hard disk by using the process of maintaining corrupted hard disks.

**Usage notes**

Change the status of the hard disk from Normal to **Error** before disk replacement. Do not manually restart the ChunkServer service during disk replacement.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Disk Maintenance**.
3. On the **Disk Maintenance** page, click the **Actively Replace Disk** tab.
4. Submit an active disk replacement request.
i. On the **Actively Replace Disk** tab, select the cluster name, chunk server, and hard disk. To view the chunk servers in a cluster, click **View Chunk Servers of Cluster** to go to the Chunk Servers page of the cluster. ii. Click **Submit**. iii. In the **OK** message, click **Modify**. The system automatically modifies the status of the hard disk. After the status of the hard disk is modified, click **View** in the **Change Status** dialog box. On the **Tasks** page, view the status of task for modifying the hard disk status.
5. Replace the disk.
On the **Corrupted Disks** tab, find the hard disk that you selected for the active disk replacement. For more information, see Maintain corrupted disks.

**What to do next**

After the disk is replaced, you can view the maintenance history of the disk on the **Disk**
**Maintenance History** tab. For more information, see View disk maintenance history.

#### 10.2.3 View disk maintenance history

After you replace a disk, you can view the detailed disk maintenance history, including the cluster, chunk server, disk ID, disk type, and execution status.

**Procedure**

1. Log on to the CDS O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Disk Maintenance**.
3. On the **Disk Maintenance** page, click the **Disk Maintenance History** tab.
4. On the **Disk Maintenance History** tab, view the disk maintenance history and perform
operations based on your business requirements. Find the maintenance record that you want to view and click **View Details** in the **Actions** column. On the **Disk Hot Maintenance Details** page, view the detailed maintenance history and continue executing or stopping in-progress maintenance tasks. The information displayed on the page of each step in the maintenance details is the snapshot information recorded during disk hot maintenance.

### 10.3 Log Management

#### 10.3.1 Collect log data

After you identify the abnormal services or modules based on an issue, you can manually collect their logs in the cluster to quickly locate and handle the issue.

**Background information**

> **Warning:** You must be granted the required permissions before you can collect and export user logs. You must follow the principle of least privilege (PoLP) and collect only the logs of the services that are related to the issue.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Log Collection**.
3. On the **Log Collection** page, click **Data Collection**.
4. In the **Data Collection** dialog box, configure the Type, Service Name, Cluster Name, Host
Name, and Time Range parameters, and click **Initiate Collection**.

**Note**

Current logs overwrite previous logs. You can select multiple values for the Type, Service Name, and Host name parameters. The **Service Name** parameter is required only if you set the **Type** parameter to **Service**
**Logs**.
After the data collection is complete, you can view the logs that are generated in the specified time range. To save the logs to your local computer, you can click **Download** in the **Result File** column of the log data that you want to save. A message indicating that the certificate is insecure appears. Click Trust to download the logs. The downloaded log file is in the tar.gz format. Decompress the file and view the logs.

#### 10.3.2 Query logs

The system centrally stores and indexes logs of key services. You can query logs within a time range by service type, project, and storage service.

**Background information**

Logs are not permanently stored. The system automatically clears logs on a regular basis. The log retention period varies based on service. The log retention period is determined by the size and the importance of logs, but cannot exceed 30 days.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Intelligent O&M > Log Search**.
3. On the **Log Search** page, configure the Type, Project, Storage, and Select Date
parameters. You can also specify a search condition. Valid values of the Type parameter are MANAGEMENT, OSS, SLS, and CHIJI.

> **Note:** The actual logs that can be queried prevail.

A search condition consists of a search statement and an analytic statement in the `Search`

| statement\|Analytic statement |   |
|---|---|
|   | . The search statem |

statement|Analytic statement format. Example: * | SELECT status, count(*) AS PV GROUP `BY status` . The search statement and the analytic statement are separated by a vertical bar (|). The search statement uses the proprietary syntax of Simple Log Service. A search statement can be executed alone. However, an analytic statement must be executed together with a search statement. You can use the log analysis feature to analyze the data in search results. You can also use the feature to analyze all data in a Logstore. For more information, see the "Simple Log Service > Query and analysis" topic in the **CDS**
**User Guide**.

| Statement | Description |
|---|---|
| Search statement | A search statement specifies one or more search conditions and returns the logs that meet the specified conditions. A search statement can be a keyword, a numeric value, a numeric value range, a space, or an asterisk (*). If you specify a space or an asterisk (*) as the search statement, no conditions are specified and all logs are returned. |
| Analytic statement | An analytic statement is used to aggregate or analyze all log data or the log data that meets the specified search conditions in a Logstore. |

4. Click **Query**.
The system displays the log data that meets the conditions.

> **Note:** Different types of logs have different formats. The actual log formats prevail.

## 11 System Management

### 11.1 View plug-in information

By default, the system registers the deployed Apsara Stack data services, such as Cloud Storage Gateway (CSG). You can use the plug-in management feature to view the registered Apsara Stack data services.

**Usage notes**

Cloud Defined Storage (CDS) automatically registers plug-ins, including cds-plugin-sgw and HDR-OPS. The plug-ins used by different storage clusters may be different. The actual plugins used by the cluster prevail. The cds-plugin-sgw plug-in can be installed only in CDS-OSS clusters and hybrid clusters of CDS-OSS and CDS-EBS. The HDR-OPS can be installed only in CDS-OSS clusters and hybrid clusters of Elastic Compute Service (ECS), CDS-OSS, and CDS-EBS.

**Procedure**

1. Log on to the CDS-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-System Management > Plug-ins**.
3. On the **Plug-ins** page, view the information about the registered data services.
Registered plug-ins may include cds-plugin-sgw and HDR-OPS. cds-plugin-sgw indicates the CSG service and HDR-OPS indicates the HDR-OPS service. To view the registration details of a plug-in, click the Plus icon on the left side of the plug-in name.

**What to do next**

Perform O&M operations on a registered data service. For more information, see Data Service.

### 11.2 View tasks

The system executes time-consuming tasks in an asynchronous manner. You can view the execution status of asynchronous tasks on the Tasks page.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-System Management > Tasks**.
The system automatically obtains and displays the tasks of the last day.
3. On the **Tasks** page, select a time range to view the information about the tasks within the
specified time range or perform operations based on your business requirements. View the task information In the task list, you can view the information about tasks, including the name, description, state, update time, and creation time.

> **Note:** The value in the **Status** column of a task indicates the state of the task.
> PROCESSING: The task is running.
> COMPLETED: The task is complete.
> FAILED: The task failed.
> CLEANING: The task failed and is being cleaned up.
> FAILED_CLEANUP_FAIL: The task failed and the cleanup also failed. Contact O&M personnel to handle the issue.

Redirect to the execution location Find the task that you want to manage and click **Redirect** in the **Execution Location** column to go to the page on which the asynchronous task is triggered. View the execution logs If a task has exceptions, you can click **Execution Logs** in the **Actions** column of the task to view the execution logs that can help you identify the cause. View details To view the details of the task, click **Details** in the **Actions** column.

### 11.3 Query audit logs

The audit logs record the modifications made by users to the system. During security maintenance, you can filter the audit logs by using different keywords to quickly locate and handle security issues in a timely manner.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-System Management > ActionTrail**.
Each time you go to the **ActionTrail** page, the system automatically queries your operations in the audit logs.
3. On the **ActionTrail** page, select a time range and specify filter conditions.

> **Note:** You can filter the logs by user, operation, object, and object attributes.

After you find a log record, you can view the user, operation, object, and object attributes of the log record. Click the plus icon in front of a log record to view the detailed request and response information about the log record.

### 11.4 System Cleanup

#### 11.4.1 Manage cleanup configurations

By default, the feature of automatically triggering compression tasks and cleanup tasks is disabled. You can manually enable the feature based on your business requirements. After you enable the auto trigger feature, the system automatically compresses service logs or clears tasks when the storage space reaches the specified threshold. You can also modify the automatic cleanup configurations such as enabling or disabling the auto trigger feature, modifying the thresholds, or deleting log cleanup configurations.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS)-OPS console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-System Management > System Cleanup**.
3. On the **System Cleanup** page, click **Automatic Cleaning Configuration** in the upper-
right corner.
4. On the **Clean up Configurations** page, view the quota and auto trigger threshold of each
service, and perform operations based on your business requirements. Enable or disable the auto trigger feature By default, the auto trigger feature is disabled. You can turn on the switch in the
**Auto Trigger** column to enable the auto trigger feature.
After you enable the auto trigger feature, you can turn off the switch in the **Auto**
**Trigger** column to disable the auto trigger feature.
Modify service quotas and auto trigger thresholds Find the service that you want to manage and click **Modify** in the **Actions** column. In the dialog box that appears, configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Service Quota | The maximum storage space that the service can use. |
| Safe Usage Level | The safe storage usage for the service logs. If the auto trigger feature is enabled and the storage space occupied by the logs is lower than the value of the Safe Usage Level parameter, the service logs are not compressed or cleaned up. |

| Usage Level for Compression | The log compression threshold. If the auto trigger feature is enabled and the storage space occupied by the service logs exceeds the value of the Usage Level for Compression parameter but is lower than the value of the Usage Level for Cleanup parameter, the system compresses the services logs until the storage space occupied by the service logs drops below the specified usage level for compression. The logs are compressed in chronological order from the earliest data to the latest data. You need to manually compress the logs that are generated before a specific date. For more information, see Clear tasks. |
|---|---|
| Usage Level for Cleanup | The log cleanup threshold. If the auto trigger feature is enabled and the storage space occupied by the logs exceeds the value of the Usage Level for Cleanup parameter, the system clears the logs until the storage space occupied by the logs drops below the value of the Usage Level for Cleanup parameter. The logs are cleared in chronological order from the earliest data to the latest data. You need to manually clear the logs that are generated before a specified date. For more information, see Clear tasks. |
| Auto Trigger | Specifies whether to enable the auto trigger feature. By default, this feature is disabled. After the auto trigger feature is enabled, the system automatically executes log compression and cleanup tasks based on the thresholds that you specify. |

Delete the log cleanup configurations

> **Important:** You can delete the log cleanup configurations of a service only after the service is stopped.

Find the service that you want to delete and click **Delete** in the **Actions** column. In the
**Confirm Deletion** message, click **OK**.
If the log cleanup configurations of a service are deleted but the service is still running, the log cleanup configurations are displayed again when the service generates logs. If the service is stopped and does not generate logs, the log cleanup configurations are no longer displayed.

#### 11.4.2 Clear tasks

The task logs are stored in system disks. You can view the size, space usage, and compression status of the logs in the following aggregation dimensions: Cluster, Cluster + Host, Service, and Service + Component. You can compress or delete logs based on your business requirements to save storage space in system disks and improve the stability of system services.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-System Management > System Cleanup**.
3. On the **System Cleanup** page, select the aggregation dimension, cluster, host, service,
and component to query logs that you want to clear. You can view the size, space usage, and compression status of the logs.
4. Click **Clear** in the **Actions** column.
5. In the **Clear Logs** dialog box, drag the slider to specify a time range. The system checks
the logs that are generated during the specified time range, and calculates the number of files that can be compressed and deleted and space that can be released.

> **Note:** Compression tasks and cleanup tasks are asynchronous operations. After the tasks are finished, you can view the execution results on the Tasks page.

To compress the logs, click **Start Compression**. In the message that appears, click
**Confirm** to start the compression task.
To clean up the logs, click **Start Cleanup**. In the message that appears, click **Confirm** to start the cleanup task.

## 12 Data Service

### 12.1 Manage CSG

After you create and configure a Cloud Storage Gateway (CSG) instance, you can view the gateway information and collect and download the gateway logs.

**Prerequisites**

An CSG instance is created and configured. For more information, see the Quick Start topic in the Cloud Storage Gateway chapter of the **OSS User Guide**.

**Procedure**

1. Log on to the Cloud Defined Storage (CDS) O&M platform console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products > Storage > CDS - OPS**.
2. In the left-side navigation pane, choose **CDS-Data Service > Storage Gateway Service**.
3. On the **Storage Gateway Service** page, click the **Overview** tab. You can perform the
following operations: View gateway information You can view the information about all gateways in the current system such as the ID, name, version, service IP address, type, and status. Collect and download the gateway logs You can collect the logs of only gateways that are in the **Running** state. Find the gateway that you want to manage. Click **Collect the logs** in the **Operation** column. You can collect the Object Storage Service (OSS) access logs that are generated by a Network File System (NFS) file share or Server Message Block (SMB) file share. You can also collect the logs that are generated by sharing operations. After the logs are collected, wait for a while and click **Refresh** to refresh the gateway information. Click **Download the logs** in the **Operation** column to download the logs.
