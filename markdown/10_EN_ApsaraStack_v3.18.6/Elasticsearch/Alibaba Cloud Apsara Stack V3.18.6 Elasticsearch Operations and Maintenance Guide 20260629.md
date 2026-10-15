---
title: "Elasticsearch Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260629"
pdf_pages: 127
source_pdf: "296e88bec1e1704b_Alibaba Cloud Apsara Stack V3.18.6 Elasticsearch Operations and Maintenance Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%A3%80%E7%B4%A2%E5%88%86%E6%9E%90%E6%9C%8D%E5%8A%A1%20Elasticsearch%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elasticsearch%20Operations%20and%20Maintenance%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Elasticsearch Operations and Maintenance Guide

## Table of Contents

- 1 Log in to the Elasticsearch O&M console
- 2 Cluster management
  - 2.1 Create an instance
  - 2.2 Manage the cluster list
  - 2.3 View basic instance information
  - 2.4 Log in to the Kibana console
  - 2.5 Log on to the Dashboards console
  - 2.6 Backup and recovery
    - 2.6.1 Snapshots
    - 2.6.2 Restore data from snapshots
  - 2.7 Plug-in management
    - 2.7.1 Install, update, and uninstall plug-ins
    - 2.7.2 Modify Configuration
  - 2.8 Cluster O&M
    - 2.8.1 Upgrade the version
    - 2.8.2 Security settings
    - 2.8.3 Instance specifications
    - 2.8.4 Modify configurations
    - 2.8.5 Upgrade the deployment method
- 3 Platform management
  - 3.1 Repository Management
  - 3.2 Plugin management
    - 3.2.1 Supported plugins
      - 3.2.1.1 Elasticsearch plugins
      - 3.2.1.2 Kibana plugins
      - 3.2.1.3 OpenSearch plugins
      - 3.2.1.4 Dashboard plugins
    - 3.2.2 Upload, update, and delete plugins
  - 3.3 Resource management
  - 3.4 Zone configuration
  - 3.5 Operation control
  - 3.6 Benchmark testing
- 4 Logging and monitoring
  - 4.1 View logs
  - 4.2 View the monitoring metrics of Elasticsearch clusters in the Apsara Uni-manager Operations Console
  - 4.3 Use custom dashboards to view metrics of Elasticsearch clusters
  - 4.4 Use Cloud Monitor to view the metrics of an Elasticsearch cluster
  - 4.5 Use Grafana to view metrics of Elasticsearch clusters
- 5 FAQ
  - 5.1 Availability issues
    - 5.1.1 Abnormal cluster states
    - 5.1.2 Business request exceptions
    - 5.1.3 Configuration update errors
    - 5.1.4 Abnormal cluster states caused by anti-affinity
    - 5.1.5 GUI exceptions
  - 5.2 Performance issues
    - 5.2.1 Slow queries
    - 5.2.2 Slow write requests
    - 5.2.3 High CPU usage
    - 5.2.4 High heap memory usage
    - 5.2.5 Heavy loads
  - 5.3 Issues related to the use of Elasticsearch
    - 5.3.1 Issues related to cluster creation
    - 5.3.2 View the basic information and monitoring information of a cluster
    - 5.3.3 Configure the analysis-ik dictionary

M console

## 1 Log in to the Elasticsearch O&M console

**O&M console**

This topic describes how users, such as O&M engineers, log in to the Elasticsearch O&M console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from the deployment personnel or administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: region-id.ops.console.intranet-domain-id.

**Usage notes**

We recommend that you use Google Chrome. Do not use the default elasticsearch-cluster cluster created during deployment in the elasticsearch namespace to host production workloads. This cluster is intended solely for functional verification. Upgrade compatibility is not guaranteed, and the upgrade process may result in data loss or service interruption. If you have used the cluster to host production workloads, immediately migrate data to a separately deployed service cluster.

**Procedure**

1. Open your browser.
2. In the address bar, enter the URL of the Apsara Uni-manager Operations Console and press
Enter. You can click the current language in the upper-right corner to switch to another language. Currently, Simplified Chinese and English are supported.
3. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length. M console
4. Click **Agree to Privacy Policy and Log In** .
By default, **I have read and agree to the Privacy Policy** is selected.
5. In the top navigation bar, choose **Product Operation > Big Data > Search and**
**Analytics Service O&M Console** to go to the **Elasticsearch O&M console.**

## 2 Cluster management

### 2.1 Create an instance

We recommend that you create clusters in the user-side console. If the clusters in the userside console cannot meet your business requirements, you can create clusters in the O&Mside console after assessing the O&M risks. For example, you can create clusters of low specifications for testing or create clusters of Elasticsearch versions other than the suggested versions in the O&M-side console. This topic describes how to create an Elasticsearch cluster in the O&M-side console. For instructions on how to create an instance in the console, see the **Elasticsearch User**
**Guide**, specifically the **Create an instance** section.

**Create an Elasticsearch instance**

1. Log on to the O&M console for Search & Analysis Service.
2. On the Instance Management page, click **Create Instance**. In the message that appears,
click **Confirm**.
3. Set Instance Type to **elasticsearch**.
4. In the **Basic Configuration** step, select a deployment mode, zone, chip architecture, and
version. Then, click **Next**. We recommend that you select V7.10.0 or V6.8.13.
5. Configure the parameters as described in the following table and click **Next**.

| Parameter | Description |
|---|---|
| Customer ID | The UID of the organization to which the user belongs. You can perform the following steps to obtain the UID: i. Log in to the Apsara Uni-manager Management Console. In the top navigation bar, click Enterprise. ii. On the Organizations page, click the organization that you want to manage. iii. On the right side of the organization list, click Manage AccessKey Pairs iv. In the Manage AccessKey Pairs dialog box, view the UID of the organization. |
| namespace | The namespace of the Elasticsearch cluster. The namespace is generated by the system and cannot be changed. |
| Cluster Name | Custom input. |

| Instance Specification | Click Modify to modify the resource configuration of each node type. Note We recommend that you create dedicated master nodes and client nodes separately for production clusters. The following example shows how to configure data nodes. Resource Limit: the amount of resources that the current node uses. Storage Type: the type of disk used by the node. The following disk types are supported: fast-disks (HDD), fast-disks-ssd (SSD), and yoda-lvm (shared disk). You can mount yoda-lvm disks to master nodes to optimize resource utilization. We recommend that you use SSDs in scenarios other than logging scenarios. We recommend that you do not mount yoda-lvm disks to data nodes due to high security risks. Number of nodes: The total number of nodes in the cluster is fixed. By default, the number of data nodes is 3, but this can be changed. Note If you configure only two data nodes for a cluster that does not contain dedicated master nodes, the cluster has a greater risk of split-brain. This may cause service unavailability. You cannot change the number. Per-node Storage Space: the storage space of each node in the cluster. After you configure this parameter, the system automatically allocates a qualified local disk to each data node based on the storage space that you specified. The specifications of the cluster depend on the size of a single disk. The disk does not support sharing or capacity expansion. Fully Dispersed Required: specifies whether to redeploy data nodes. This avoids deploying multiple data nodes on one physical machine and improves the availability of the cluster. If the number of physical machines is less than the number of data nodes, the cluster fails to be created. Configure this parameter as needed. JVM Configuration: Click the icon and add the configuration as needed. Example: -XX:InitiatingHeapOccupancyPercent=45 . |
|---|---|
| Plugin Configuration | Select the Elasticsearch and Kibana plug-ins to be installed when you create the cluster. |
| elasticsearch.yml | Customize the YML file of the Elasticsearch cluster. The file uses YAML in the format of key: value . The colon ( : ) must be followed by a space character. |

| kibana.yml | Customize the YML configuration file of the Kibana cluster. Note The YML configuration file for the Kibana cluster is available for configuration only when Kibana nodes are enabled. |
|---|---|

6. Click **Next** to configure network and system parameters.

| Parameter | Description |
|---|---|
| Network Type | Dedicated Network (single tunnel): The organization to which the virtual private cloud (VPC) and vSwitch belong must be the same as that specified by the Customer ID parameter. Dedicated Network (any tunnel): Do not select this network type unless it is necessary. Note IPv4 is supported by default. To use IPv4/IPv6 dual stack, make sure that the IPv4/IPv6 dual stack switch is turned on. Then, contact the technical support of Alibaba Cloud to modify the configuration file of the cluster. Change the values of the vip protocols and _ elasticsearch.vip protocols parameters in _ .spec.parameters to ipv4+ipv6 , and trigger the cluster to perform a rolling update to complete the configuration. |
| Login Name | elastic: the default account, which cannot be changed. It is used to access Elasticsearch and log in to Kibana. monitoring collector: the account used to manage services. Some _ management features need this account. Note The password must meet the following requirements: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ The password must be 12 to 32 characters in length. |

|   | vip protocols _ |
|---|---|
| elasticsearch.vip protocols _ |   |
| .spec.parameters |   |

7. Click **Start Creation**.
After the cluster is created, you are redirected to the **Instance Management** page. Check the status of the cluster. Wait until the cluster enters the Normal state. Before you use the cluster, you must configure a whitelist. Otherwise, you may encounter issues such as monitoring data collection failure or Kibana console login failure. For more information, see Security settings.

**Create an OpenSearch instance**

1. Log on to the O&M console for Search & Analysis Service.
2. On the Instance Management page, click **Create Instance**. In the dialog box that appears,
click **OK**.
3. Set Instance Type to **opensearch**.
4. In the **Basic Configuration** step, select a deployment mode, zone, chip architecture, and
version. Then, click **Next**. Currently, OpenSearch instances can be deployed only in a single zone.
5. Configure the cluster parameters as described in the following table, and then click **Next**.

| Parameter | Description |
|---|---|
| Customer ID | The UID of the user's organization. To obtain the UID, perform the following steps: i. Log on to the Apsara Uni-manager console and clickE nterprise. ii. On the Organization Management page, click the target organization. iii. To the right of the organization, click Manage Accesskey. iv. On the Manage AccessKey page, obtain the UID of the organization. |
| namespace | The namespace of the Elasticsearch cluster. The system generates the namespace. You cannot change it. |
| Cluster Name | Custom input. |

| Specifications | Click Modify to change the resource configuration of each node type. Note Set up dedicated master nodes and client nodes for production clusters. The following section uses data nodes as an example to describe node parameter settings: Resource Limit: The amount of resources that the current node requires. Storage Class: The disk type used by the node. The following three types are supported: fast-disks (HDD), fast-disks-ssd (SSD), and yoda-lvm (shared disk). Use yoda-lvm storage for master nodes to optimize resource utilization. Use SSDs to store data in all scenarios except for logging. Using yoda-lvm storage for data nodes poses high risks. Do not use this storage type. Select it with caution. Node Count: The number of nodes in the cluster. This parameter is enabled by default and cannot be changed. The default number of data nodes is 3. You can change this value. Note If dedicated master nodes are not enabled, a cluster with only two data nodes is at risk of a split-brain issue. This can cause service unavailability. This configuration is not supported. Per-node Storage: The storage space for each node in the cluster. After you set this parameter, the system allocates a local disk that meets the requirements to each data node based on the specified storage size. After the instance is created, its specifications are related to the size of a single disk. Sharing and scaling are not supported. Fully Disperse Nodes: Full dispersal avoids deploying multiple ES data nodes on a single physical machine and improves availability. However, if the number of physical machines is smaller than the number of data nodes, the instance cannot be created. Select this option based on your business scenario and platform planning. JVM Configuration: Click the icon and add the configuration as needed. Example: -XX:InitiatingHeapOccupancyPercent=45 . |
|---|---|
| Plugin Configuration | Select the OpenSearch and Dashboard plugins to install when you create the cluster. |
| opensearch.yml | Customize the YML configuration file for the OpenSearch cluster. This file uses the YAML markup language. The format is key: value . A space must follow the colon ( : ). |

| dashboard.yml | Customize the YML configuration file for the Dashboard cluster. Note The YML configuration file for the Dashboard cluster is displayed and can be configured only when Dashboard nodes are enabled. |
|---|---|

6. Click **Next** to configure the network and system.

| Parameter | Description |
|---|---|
| Network Type | Virtual Private Cloud (single tunnel): The organization to which the virtual private cloud (VPC) and vSwitch belong must match the customer ID. Virtual Private Cloud (any tunnel): Do not use the anytunnel network type unless necessary. Note By default, the network type supports IPv4. To use the IPv4/IPv6 dual- stack feature of the product, make sure that the master switch for the IPv4/IPv6 dual-stack feature is enabled for the current site. Then, contact Alibaba Cloud technical support to modify the cluster configuration file. Change the values of the .spec.parameters , vip protocols , _ and elasticsearch.vip protocols parameters to ipv4+ipv6 , _ and trigger a rolling update of the cluster to apply the configuration. |
| Account | admin: The default account. It cannot be changed. This account is used to access OpenSearch and log on to Dashboard. monitoring collector: The account used by the management service. Some _ management features depend on this account. Note Password requirements: The password must contain three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !@#$%^&* () +-=. _ The password must be 12 to 32 characters in length. |

|   | .spec.parameters |
|---|---|
| elasticsearch.vip protocols _ |   |

7. Click **Start Creation**.
After the instance is created, you are redirected to the **Instance Management** page. View the instance status and wait for the status to become Normal.

### 2.2 Manage the cluster list

After you create Elasticsearch clusters, you can view the basic information of all clusters in Instance Management in the left-side navigation panel. Log in to the Elasticsearch O&M console. The **Instance Management** page appears by default. On the **Instance Management** tab, you can view all clusters and perform the following operations:

| Operation | Description |
|---|---|
| Query or filter out a cluster | When you have a large number of clusters, you can filter clusters out by Instance ID, Customer ID, Instance Type, and namespace. |
| Manage a namespace | Click Manage next to namespace to delete unnecessary namespaces. |
| View the basic information of a cluster | The information includes Instance ID, Status, Cluster Health, Version, Instance Type, Data Node Count, Customer ID, Latest Version, and namespace. |
| Delete a cluster | Click Delete in the Action column to delete a cluster. Warning After the cluster is deleted, the related data is cleared and the cluster cannot be restored. Exercise caution when you perform this operation. |
| Refresh the cluster list | Click Refresh in the upper-right corner to obtain the latest status data of the cluster. |

### 2.3 View basic instance information

**information**

This topic describes how to view the basic information of an instance. This information includes the instance status, endpoint, Kibana (or Dashboard) access address, and instance configuration.

**Prerequisites**

An instance is created. For more information, see Create an instance.

**Procedure**

1. Log on to the Search & Analysis Service O&M console.
2. In the navigation pane on the left, click **Instance Management**.
3. On the **Instance Management** page, click the target **Instance ID**.
4. On the **Basic Information** page, you can view the basic information of the instance.
The **Basic Information** page displays key details about your instance. These details include its type, health status, chip architecture, version, deployment mode, creation time, and network information. The page also provides a cluster management entry, an endpoint, and the IP address and port of the domain name, which you can use to access your instance. Additionally, the page displays the configuration for each node type and a visualization of the cluster. This information helps you understand the instance configuration and decide whether to upgrade or downgrade the instance as needed.

### 2.4 Log in to the Kibana console

Apsara Stack Elasticsearch provides the Kibana console for you to scale your businesses. The Kibana console is seamlessly integrated into Elasticsearch. It lets you view the status of your Elasticsearch cluster in real time and manage the cluster. This topic describes how to log in to the Kibana console.

**Prerequisites**

The Elasticsearch instance is in the Normal state, and Kibana nodes are enabled. An account is prepared to log in to the Kibana console, and a whitelist is configured. For more information, see Security settings.

**Procedure**

1. Log in to the Search & Analysis Service console.
2. In the navigation pane on the left, click **Instance Management**.
3. On the **Instance Management** page, click the target **Instance ID**.
4. On the **Basic Information** page, click **Kibana** to the right of **Cluster Management**.
5. On the Kibana console log in page, enter your username and password, and then click **Log**
**In**.
The default username is elastic. The password is the one that you specified when you created the instance.
6. Click the
icon in the upper-left corner and choose **Management > Dev Tools** to go to the **Console** page.

### 2.5 Log on to the Dashboards console

**console**

The OpenSearch Dashboards console is the core visualization and interaction tool in the OpenSearch ecosystem. It provides a web-based user interface to query, analyze, visualize, and manage data stored in an OpenSearch cluster. With features such as rich charts, dashboards, log browsing, and alerting, you can efficiently explore data, monitor system status, and generate insights. This topic describes how to log on to the OpenSearch Dashboards console.

**Prerequisites**

The OpenSearch instance is in the Normal state and the Dashboard node is enabled.

**Procedure**

1. Log on to the OpenSearch Service for Elasticsearch console.
2. In the navigation pane on the left, click **Instance Management**.
3. On the **Instance Management** page, click the target **instance ID**.
4. On the **Basic Information** page, to the right of **Cluster Management**, click **Dashboard**.
5. Enter your username and password, and then click **Log In**.
The default username is admin. The password is the one that you set when you created the instance.
6. In the upper-left corner, click the
icon and choose **Management > Dev Tools** to go to the **Console** page.

### 2.6 Backup and recovery

#### 2.6.1 Snapshots

The snapshot backup feature lets you configure automatic backups and manually perform snapshot backups.

**Prerequisites**

An instance is created and in the Normal state. For more information, see Create an instance.

**Usage notes**

The scheduled backup feature occupies CPU, memory, and disk resources, which may compromise the performance of your instance.

**Procedure**

1. Log on to the Retrieval Analysis Service O&M console.
2. In the left navigation pane, click **Instance Management**.
3. On the **Instance Management** page, click the target **instance ID**.
4. In the navigation pane on the left, choose **Snapshot Backup > Automatic Backup**.
5. On the **Automatic Backup** page, select a repository and click **Save Repository**
**Configuration**.
If no repositories are available, you must first add a repository in Platform Management. For more information, see Add a repository.
6. Click **Modify Settings**. In the dialog box that appears, specify the backup interval, cycle,
and time, and click **Confirm**.

**Important**

The first snapshot backup of a cluster is a full backup of its data. The time required depends on the data volume. Perform snapshot backups during off-peak hours. Scheduled backups can reduce the query and write performance of the cluster. Set a reasonable frequency and time period for backups. Do not use a very short interval. After you confirm the settings, the system automatically backs up data based on the specified backup cycle. To back up data immediately, click **Backup Now**. After an automatic backup is complete, you can click **Disable Automatic Backup** to disable this feature. If you enable the feature again, you must re-associate a repository. Existing backup records are not affected. You can also query your snapshots and refresh the list. The snapshot list automatically deletes automatic backup records. The system runs a cleanup task once every hour and retains the 10 most recent records. Manual backup records, which are created when you click **Backup Now**, are not automatically deleted.

#### 2.6.2 Restore data from snapshots

The snapshot restoration feature allows you to restore Elasticsearch data from snapshots with a few clicks. It supports both automatic and manual data restoration from snapshots, as well as cross-cluster data restoration. This topic describes how to use the snapshot restoration feature to precisely restore specified index data.

**Scenarios**

This topic uses a real-world O&M scenario as an example: Four test indexes (index1, index2, index3, and index4) are created on an Elasticsearch cluster and a snapshot is taken for backup. After index1 and index2 are accidentally deleted, the snapshot restoration feature is used to precisely restore the indexes.

**Prerequisites**

An Elasticsearch cluster is created, and the cluster is in the normal state. For more information, see Create a cluster. The IP address of the Kibana service is added to the whitelist of the target cluster to enable the connection. For more information, see Security settings. A snapshot is created for the specified indexes and the snapshot ID is obtained. For more information, see Snapshots. A destination bucket is created in Object Storage Service (OSS). For more information, see
**Object Storage Service User Guide > Buckets > Create buckets**.

**Procedure**

1. Log in to the Elasticsearch O&M console.
2. In the left-side navigation pane, click **Instance Management**.
3. On the **Instance Management** page, click the value in the **Instance ID** column for the
cluster that you want to manage.
4. In the left-side navigation pane, choose **Snapshot Backup > Snapshot Restore**.
5. On the **Snapshot Restore** page, configure the snapshot from which you want to restore
data.

| Parameter | Description |
|---|---|
| Bucket | The name of the OSS bucket used to store cluster backup snapshots. You can run the GET snapshot command in the Kibana console _ to view the name. |

| Storage Path | The path of the snapshot in the bucket. Example: snapshot/test.es-essen/ . You can run the GET snapshot _ command in the Kibana console to view the path. |
|---|---|
| Snapshot ID | The ID of the snapshot. The system automatically generates a snapshot ID after the snapshot is taken. For more information about snapshots, see Snapshots. |
| Access Key | The AccessKey ID of your Apsara Stack tenant account. |
| Secret Key | The AccessKey secret of your Apsara Stack tenant account. |
| Advanced Parameters | The index to be restored from the snapshot. For more information, see the Elasticsearch Snapshot and restore syntax. Default value: _ {}. The following example shows how to restore index1 and index2 from the snapshot: {"indices":"index1,index2"} |

6. Click **Restore**.
Once the restoration task starts, you can check the specific restoration tasks in the Kibana

| GET cat/recovery?active only&v _ _ |   |   |
|---|---|---|
| n the | GET cat/indices?v _ | comma |

have been restored.

### 2.7 Plug-in management

#### 2.7.1 Install, update, and uninstall plug-ins

You must install a plug-in before you can use it. Built-in plug-ins are installed by default. This topic describes how to install a non-built-in plug-in.

**Background information**

Different instance types support different plug-ins.

| Instance type | Support |
|---|---|
| Elasticsearch instance | Elasticsearch plug-ins |
|   | Kibana plug-ins |
| OpenSearch instance | OpenSearch plug-ins |
| > Document Version: 20260629 | 1 |

| Operations and Maintenance Gui e·Cluster management | Elasticsearc |
|---|---|
|   | Dashboard plug-ins |

**Prerequisites**

An Elasticsearch cluster is created, and the cluster is in the normal state. For more information, see Create a cluster. If you use an Elasticsearch instance, you must add monitoring_collector to the whitelist. For more information, see Account security settings. This step is not required for OpenSearch instances.

**Procedure**

1. Log on to the Search & Analysis Service O&M console.
2. In the navigation pane on the left, click **Instance Management**.
3. On the **Instance Management** page, click the ID of the target **instance**.
4. In the navigation pane on the left, choose **Plugin Management > Elasticsearch Plugin**.
Elasticsearch plug-ins are used as an example in this topic. You can install other plugins by following the same procedure.
5. Install or update a plug-in.
Install a plug-in If the page displays large numbers of plug-ins, enter the name of the desired plug-in into the search box to find the plug-in. Fuzzy match is supported. Install a plugin: Click **Install** in the **Update** column for the target plugin. Install multiple plug-ins at a time: Select the plug-ins you want to install and click
**Batch Install**.

**Warning**

Plug-in installation triggers cluster restarts. Proceed with caution. Update a plug-in If a new version is available for an installed plug-in, the system displays the new version number in the **Updatable Plugin Version** column. To update the plug-in, click the
**Update** button in the corresponding row.
6. Click **OK**.
7. Select a cluster restart method as needed and click **OK**.
After you confirm the installation, the cluster automatically restarts. The plug-in is installed after the restart is complete. After you confirm the update, the cluster does not automatically restart. You must click the **Restart** button in the upper-right corner to apply the update. After the restart is complete, the new version number is displayed in the **Plugin Version** column. You can use the same method to install or update plug-ins on other plug-in pages. After a plug-in is installed or updated, you can click **Uninstall** or **Batch Uninstall** to remove the plug-in if it is no longer needed. If an error occurs during the plug-in installation or update, contact the O&M engineer.

#### 2.7.2 Modify Configuration

After you create an instance, you can modify the configuration files of its built-in plugins. This topic describes the procedure.

**Prerequisites**

An instance has been created and its status is Normal. For more information, see Create an instance.

**Procedure**

1. Log on to the Retrieval Analysis Service O&M console.
2. In the navigation pane on the left, click **Instance Management**.
3. On the **Instance Management** page, click the target **instance ID**.
4. In the navigation pane on the left, choose **Plugin Management > Elasticsearch**
**Plugins**.
Elasticsearch plug-ins are used as an example in this topic. You can install other plugins by following the same procedure.
5. Find the built-in plug-in that you want to modify and click **Modify Configuration** in the
Action column.

**Warning**

Modifying the configuration file of a plugin restarts the cluster. Confirm the operation before you proceed.
6. Click **Add File**.
7. In the **Add File** dialog box, enter the file name and click **OK**.
8. Click the file that you added and enter the plug-in configuration into the editor on the right
side.
9. Click **OK**. In the dialog box that appears, click **OK** again.
0. In the **Restart** dialog box, select a **Restart Method** and click **OK**.
The cluster then restarts. The plugin configuration file is updated after the restart is complete.

### 2.8 Cluster O&M

#### 2.8.1 Upgrade the version

This topic describes how to upgrade the kernel version during cluster Operations and Maintenance (O&M).

**Prerequisites**

An instance is created and its status is Normal. For more information, see Create an instance.

**Limits**

Only Elasticsearch instances support this feature. OpenSearch instances do not.

**Notes**

The upgrade process does not support rollbacks. Before you upgrade, perform a basic inspection and back up critical data. Do not directly upgrade clusters that have custom plugins installed. To reduce the impact on the cluster, ensure that the number of replicas for all indexes in the cluster is greater than 1. The upgrade operation triggers a cluster image update and restart. This may cause service jitter. Perform this operation during off-peak hours and monitor the cluster.

**Go to the cluster O&M page**

1. Log on to the Search and Analysis Service O&M console.
2. In the navigation pane on the left, click **Instance Management**.
3. On the **Instance Management** page, click the target **instance ID**.
4. In the navigation pane on the left, click **Cluster O&M**.

**Upgrade the kernel version**

1. Go to the cluster O&M page.
2. In the navigation pane on the left, click **Version Upgrade**.
3. If an upgradable version or kernel image is detected for your instance, click **Impact**
**Analysis** to view the upgrade details.
If no upgradable version or kernel image is detected, no action is required.
4. Click **Upgrade**.
5. In the dialog box that appears, click **Confirm**.
After the upgrade is complete, the cluster status is Normal, and the instance version and image version are updated to the latest versions.

#### 2.8.2 Security settings

Security settings let you enable the HTTPS protocol with one click, change the ES port number, manage the VPC internal-facing access whitelist, modify account information, and view certificate details.

**Use the HTTPS protocol**

HTTPS (Hyper Text Transfer Protocol Secure) is a secure version of HTTP that uses SSL (Secure Sockets Layer) to encrypt data during transmission. To protect your data, use the HTTPS protocol.

**Important**

By default, this feature is disabled for Elasticsearch instances. Enable it manually. For OpenSearch instances, this feature is enabled by default and cannot be disabled.
1. Go to the cluster O&M page.
2. In the navigation pane on the left, click **Security Settings**.
3. On the **Security Settings** page, click **Https Protocol**. Then, turn on the switch for this
feature as needed.

**Change the ES port number**

After creating an instance, you can change the port number as needed.
1. Go to the cluster O&M page.
2. In the navigation pane on the left, click **Security Settings**.
3. On the **Security Settings** page, in the **Port Number** area, enter the new port number and
click **Modify** to update it. The default port number is 9200. After a successful modification, a success message appears and the port number updates to the new value.

**Configure the VPC internal-facing access whitelist**

When you access an Alibaba Cloud Elasticsearch (ES) instance over an internal network, you must first add the IP address of the accessing device to the instance's whitelist. If you cannot access the ES instance, check whether the correct IP address is in the whitelist.
1. Go to the cluster O&M page.
2. In the navigation pane on the left, click **Security Settings**.
3. On the **Security Settings** page, click **VPC Internal-facing Access Whitelist**.
4. Click **Add IP Whitelist**. In the **IP Whitelist** dialog box, configure the **VPC** and **Whitelist**
**Information**.
5. Click **OK**.

**Account security settings**

Improve cluster and system security by specifying which users can log on to Kibana or the dashboard and by setting up a proper whitelist. After you create a new cluster, you must set up a whitelist first. Otherwise, you may encounter issues such as failing to collect monitoring data or being unable to log on to Kibana.
1. Go to the cluster O&M page.
2. In the navigation pane on the left, click **Security Settings**.
3. On the **Security Settings** page, click **Account Information** to view and modify account
details. View logon names elastic (or admin): The logon name is elastic for Elasticsearch instances and admin for OpenSearch instances. The elastic/admin account is the administrator account and has all superuser permissions.

**Important**

Resetting the password affects access to the instance with the elastic/admin account. It does not affect access with other non-elastic/admin accounts. For this reason, do not use the elastic/admin account to access the instance from your programs. Instead, use a custom user with the necessary permissions. kibanaserver: This is the account used by the Kibana service. It has the kibana_system permission, which includes only the least privilege required for Kibana initialization. It cannot read user data. The whitelist for this account must include the IP address where the Kibana service is located. If not configured correctly, Kibana will be inaccessible. monitoring_collector: This is the account used by the management service. It has the aliyun-ops permission. Some management features, such as collecting monitoring data and running automatic backups, depend on this account. It includes only the least privilege required for management and cannot read user data. The whitelist for this account must include all possible IP addresses of the management components. If not configured correctly, some management features will be degraded and become unavailable. For example, you cannot view monitoring data, enable automatic backups, or perform a switchover using ASR. Change password Click **Change Password** to change the password for the account. You do not need to restart the cluster. Modify whitelist

**Important**

Currently, only Elasticsearch instances support whitelist modification. OpenSearch instances do not. Click **Modify Whitelist** to change the whitelist configuration. To configure multiple IP addresses, separate them with a comma (,). For example,

```
 127.0.0.1,127.0.0.2 .
```

Specify an address range using CIDR notation. For example, `1.2.3.4/24` allows access to the ES instance from IP addresses in the 1.2.3.X CIDR block. `127.0.0.1` is the default empty whitelist. An account configured with this whitelist cannot remotely access the ES instance.

**View certificate information**

This certificate is used for communication between ES nodes. Nodes can access each other if the fingerprints of their issued certificates are the same.
1. Go to the cluster O&M page.
2. In the navigation pane on the left, click **Security Settings**.
3. On the **Security Settings** page, click **Certificate Information** to view the certificate
details.

**Important**

The current certificate is randomly generated by the system. To use the XDCR feature, CCS feature, or cross-cluster reindex in ES, the certificates of the primary and secondary clusters must be identical to establish a connection. Custom certificates are supported. To change a certificate, contact an on-site O&M engineer.

**Related information**

**Get an IP address**

**Method 1: Get the pod IP address for kibana, essen, or**

**exporter**

When you run the command on a terminal server, remove ${ } and keep the content inside.

```bash
 # Get the pod IP address. The namespace for kibana/exporter is the same as the cluster
's namespace. The namespace for essen is essen.
 kubectl get pod -n ${service_namespace} -owide
```

**Method 2: Get the IP CIDR block for the kibana, essen,**

**exporter, or snapshot service**

**Important**

The reason for getting the IP CIDR block is that the pod IP address from Method 1 can change if the pod restarts. Configuring a CIDR block avoids this issue. However, you must configure the whitelist with the least privilege granularity. For the effective CIDR block with the least privilege, consult the delivery or on-site security team. To get the possible IP CIDR blocks for the corresponding Elasticsearch service, obtain all CIDR block information for the current environment:

```bash
 kubectl get subnet
```

The address range is expressed in CIDR notation. For a shared deployment, any CIDR block may be allocated. For a dedicated deployment, ES instance resources are deployed on dedicated machines, but management services may still be located in any CIDR block.

**Important**

This method is for reference only. For specific details, consult the delivery or on-site security team.

**Troubleshoot errors and exceptions**

Cannot log on to the Kibana interface Error message: Version 6.x/7.x: kibana server is not ready yet Version 5.x: Authorization Exception Cause: The whitelist for the kibanaserver account is configured incorrectly. Solution: Modify the whitelist for the kibanaserver account. Add the IP address of the Kibana service to the whitelist. Can still log on to Kibana after the whitelist is disabled Symptom: You can still log on to Kibana after the whitelist is disabled. Cause: The Kibana interface was not re-initialized. Solution: Contact an on-site O&M engineer to restart the pod where Kibana is located. No monitoring data Symptom: The Grafana monitoring page shows "no data". Cause: The whitelist for the monitoring_collector account is configured incorrectly. Solution: Modify the whitelist for the monitoring_collector account. Add the IP address of the exporter service to the whitelist. Error when accessing the Elasticsearch plugin page Error message: 403 Forbidden:[Ip 23.5.**.** is not allow in ip white/black list] Cause: The whitelist for the monitoring_collector account is configured incorrectly. Solution: Modify the whitelist for the monitoring_collector account. Add the IP address of the essen service to the whitelist. Error when accessing the automatic backup page Error message: proxy request fail Cause: The whitelist for the monitoring_collector account is configured incorrectly. Solution: Modify the whitelist for the monitoring_collector account. Add the IP address of the essen service to the whitelist. Automatic backup does not work Symptom: A snapshot is not created at the scheduled time. Cause: The whitelist for the monitoring_collector account is configured incorrectly. Solution: Modify the whitelist for the monitoring_collector account. Add the IP address of the snapshot service to the whitelist. Kibana logon error Symptom: Logon fails even with the correct account and password (using monitoring_collector as an example). Cause: The whitelist for the account is configured incorrectly, or the **Can log on to**
**Kibana** feature is not enabled.
Solution: Add the IP address of the Kibana service to the account's whitelist and select
**Can log on to Kibana**.
Cross-cluster access error Error message: [][22.0.x.x:9300] general node connection failure Cause: The interacting clusters have different certificates. Solution: Consult an on-site O&M engineer, or see the instance management operations in the O&M guide.

#### 2.8.3 Instance specifications

You can modify the specifications of an instance to change the size of its nodes.

**Considerations**

Modifying the node configuration restarts the cluster. Confirm that you want to proceed.

**Procedure**

1. Go to the Cluster O&M page.
2. In the navigation pane on the left, click **Instance specifications**.
3. For the target node, click **Modify**.
4. Enter the node configuration.
For more information about the configuration parameters, see Create an instance.
5. Click **Save**.
6. In the dialog box, select a restart method for the cluster and click **OK**.

#### 2.8.4 Modify configurations

The cluster configuration feature of Elasticsearch allows you to configure the basic and advanced configurations of an Elasticsearch cluster as needed.

**Procedure**

**Important**

After you modify the configurations of an Elasticsearch cluster, the cluster is restarted. Proceed with caution.
1. Go to the Cluster Operations page of an Elasticsearch cluster.
2. In the left-side navigation pane, click **Configuration Modification**.
3. Modifies the configurations of the cluster.
Modify the basic configurations. In the **Basic Configuration** section, you can view the **System Configuration** parameter and modify the .yml file as needed. The configuration fields vary based on the instance version. The configuration fields displayed in the console prevail. elasticsearch.yml

**V7.10.0**

| Field | Value description | Field description |
|---|---|---|
| apack.accesslog.enabled | A Boolean value. Valid values: true false Default value: true. | Specifies whether to enable the access log audit feature. |
| apack.accesslog.search.enabl ed | A Boolean value. Valid values: true false Default value: true. | Specifies whether to display search request fields. |

| thread pool.write.queue size _ _ | A positive integer. Valid values: adjusted based on the size of the cluster and the needs of write operations, without a maximum or minimum value. Default value: 10000. | The size of the document write queue. |
|---|---|---|
| thread pool.search.queue siz _ _ e | A positive integer. Valid values: adjusted based on the size and load of the cluster. Default value: 1000. | The size of the document search queue. |
| cluster.routing.allocation.disk. watermark.low | A string. Default value: 85%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts not to allocate shards to this node. |
| cluster.routing.allocation.disk. watermark.high | A string. Default value: 90%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |
| cluster.routing.allocation.disk. watermark.flood stage _ | A string. Default value: 95%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster marks this node as non- allocable, attempts to move all shards from this node to other nodes, and sets the shards on this node to read-only. |
| action.auto create index _ _ | A Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if no index is available after a new document is uploaded. |
| action.destructive requires n _ _ ame | A Boolean value. Valid values: true false Default value: false. | Specifies whether you need to specify the index name when you delete an index. |

**V6.8.13**

| Field | Value description | Field description |
|---|---|---|
| action.auto create index _ _ | A Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if no index is available after a new document is uploaded. |
| action.destructive requires _ _ name | A Boolean value. Valid values: true false Default value: false. | Specifies whether you need to specify the index name when you delete an index. |
| thread pool.write.queue size _ _ | A positive integer. Valid values: adjusted based on the size of the cluster and the needs of write operations, without a maximum or minimum value. Default value: 200. | The size of the document write queue. |
| thread pool.search.queue si _ _ ze | A positive integer. Valid values: adjusted based on the size and load of the cluster. Default value: 1000. | The size of the document search queue. |
| cluster.routing.allocation.dis k.watermark.low | A string. Default value: 85%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts not to allocate shards to this node. |
| cluster.routing.allocation.dis k.watermark.high | A string. Default value: 90%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |

| cluster.routing.allocation.dis k.watermark.flood stage _ | A string. Default value: 95%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster marks this node as non-allocable, attempts to move all shards from this node to other nodes, and sets the shards on this node to read- only. |
|---|---|---|

**V5.5.3**

| Field | Value description | Field description |
|---|---|---|
| thread pool.bulk.queue size _ _ | A positive integer. Valid values: adjusted based on the size of the cluster and the needs of write operations, without a maximum or minimum value. Default value: 200. | The size of the document batch write queue. |
| thread pool.search.queue siz _ _ e | A positive integer. Valid values: adjusted based on the size and load of the cluster. Default value: 1000. | The size of the document search queue. |
| cluster.routing.allocation.disk. watermark.low | A string. Default value: 85%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts not to allocate shards to this node. |
| cluster.routing.allocation.disk. watermark.high | A string. Default value: 90%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |
| action.auto create index _ _ | A Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if no index is available after a new document is uploaded. |

| action.destructive requires n _ _ ame | A Boolean value. Valid values: true false Default value: false. | Specifies whether you need to specify the index name when you delete an index. |
|---|---|---|

opensearch.yml

**V3.1.0**

| Field | Value description | Field description |
|---|---|---|
| thread pool.write.queue size _ _ | A positive integer. Valid values: adjusted based on the size of the cluster and the needs of write operations, without a maximum or minimum value. Default value: 10000. | The size of the document write queue. |
| thread pool.search.queue siz _ _ e | A positive integer. Valid values: adjusted based on the size and load of the cluster. Default value: 1000. | The size of the document search queue. |
| cluster.routing.allocation.disk. watermark.low | A string. Default value: 85%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts not to allocate shards to this node. |
| cluster.routing.allocation.disk. watermark.high | A string. Default value: 90%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster attempts to reallocate shards to other nodes with lower disk usage. |

| cluster.routing.allocation.disk. watermark.flood stage _ | A string. Default value: 95%. You can also set this field to a fixed value that specifies the available disk space, such as 500 MB or 100 GB. | When the disk usage of a node reaches this threshold, the cluster marks this node as non- allocable, attempts to move all shards from this node to other nodes, and sets the shards on this node to read-only. |
|---|---|---|
| action.auto create index _ _ | A Boolean value. Valid values: true false Default value: true. | Specifies whether to automatically create an index if no index is available after a new document is uploaded. |
| action.destructive requires n _ _ ame | A Boolean value. Valid values: true false Default value: false. | Specifies whether you need to specify the index name when you delete an index. |

Modify the advanced configurations. On the **Configuration Modification** page, add ?advanced after the URL of the page and press the Enter key. The **Advanced Configuration** section appears. After you turn on **Enable Advanced Configuration**, you can update the advanced configurations as needed in the **app value** field.

#### 2.8.5 Upgrade the deployment method

You can upgrade the deployment method of a cluster, such as from a single-zone to a multizone deployment.

**Limits**

Only Elasticsearch instances support this feature. This feature is not supported for OpenSearch instances.

**Upgrade the deployment method**

**Important**

Deployment method upgrades are available only for clusters that were initially configured for dual-zone or multi-zone deployment.
1. Go to the Cluster O&M page.
2. In the navigation pane on the left, click **Deployment Method Upgrade**.
3. On the **Deployment Method Upgrade** page, check if the deployment method of the
current instance can be upgraded. If a message indicates that no deployment methods are available for upgrade, the current instance cannot be upgraded. To enable an upgrade, go to the Platform Management page and change the zone configuration. For more information, see Zone Configuration. If the page shows the instance ID/Name, Deployment Method (Before Upgrade), and Deployment Method (After Upgrade), the instance can be upgraded. Follow the subsequent steps to perform the upgrade. The deployment method can only be upgraded to the one specified in the zone configuration on the Platform Management page of the O&M console. Downgrades are not supported.
4. In the **Basic Check** section, follow the prompts to check if the instance meets the upgrade
requirements. After confirming that the requirements are met, click **Next**.
5. In the **Resource Assessment** section, assess the resources as prompted on the page.
After confirming that the resources meet the requirements, click **Next**.
6. In the **Risk Warning** section, review and confirm the risks as prompted. After confirmation,
click **Start**.
7. In the dialog box that appears, click **OK**.
After you click OK, the system begins to upgrade the deployment method, and the cluster restarts. The upgrade is complete when the cluster status changes to Normal.

## 3 Platform management

### 3.1 Repository Management

This topic describes how to use the repository management feature to manage the snapshot repositories of Elasticsearch. The automatic backup feature of Elasticsearch clusters relies on repositories. You can use this feature to query, add, modify, and delete repositories.

**Go to the Repository Management page**

1. Log on to the Elasticsearch O&M console.
2. In the navigation pane on the left, choose **Platform Management > Repository**
**Management**.

**Add a repository**

1. Go to the Repository Management page.
2. In the upper-right corner of the page, click **Add**.
3. In the dialog box that appears, enter a repository name, modify the repository
configuration, and then click **Confirm**.

| Field |   | Description |   |   |
|---|---|---|---|---|
| type |   | Default: oss. |   |   |
| access key id _ _ |   | In the Unified Cloud Management Platform, go to Enterprise > Resource Management > Organization Management. In the Organizational Structure section, select your target organization and click Manage AccessKey to obtain your AccessKey ID and AccessKey secret. |   |   |
| bucket |   | The name of the bucket you created in the Object Storage Service (OSS) console. |   |   |
| endpoint |   | In the Object Storage Service (OSS) console, click the name of your bucket. In the Endpoint section, copy the endpoint. The format is oss-cn-wulan-env**e-d01- a.inter.env**e.shuguang.com . |   |   |
|   |   |   | oss-cn-wulan-env**e-d01- |   |
|   |   | a.inter.env**e.shuguang.com |   |   |

| secret access key _ _ | In the Unified Cloud Management Platform, go to Enterprise > Resource Management > Organization Management. In the Organizational Structure section, select your target organization and click Manage AccessKey to obtain your AccessKey ID and AccessKey secret. |
|---|---|

After you add the repository, it appears in the repository list. If the newly added repository does not appear, click **Refresh** in the upper-right corner to refresh the list.

**Query repositories**

1. Go to the Repository Management page.
2. At the top of the page, you can select the query dimension.
You can search for repositories by **Repository Name** or **Repository Type**.
3. Enter the keyword.
The system automatically runs the query using fuzzy match.

**Modify a repository**

1. Go to the Repository Management page.
2. In the repository list, click **Edit** in the **Action** column of a repository.
3. In the dialog box that appears, modify the repository configuration and click **Confirm**. The
repository name is not modifiable.

**Important**

If automatic backup is enabled, modifying the repository does not affect the current automatic backup configuration. If automatic backup is disabled and you enable it after you modify the repository (for example, by changing the bucket name), new automatic backups use the updated repository configuration. In this case, you cannot view previous automatic backup data.

**Delete a repository**

1. Go to the Repository Management page.
2. In the repository list, click **Delete** in the **Action** column of a repository.

**Warning**

Deleted repositories cannot be recovered. Proceed with caution.
3. In the message that appears, click **Confirm**.

### 3.2 Plugin management

#### 3.2.1 Supported plugins

##### 3.2.1.1 Elasticsearch plugins

This topic lists the supported Elasticsearch plugins and their versions.

**Version 7.10.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| a-pack-core | Built-in | 7.10.0 | The A-Pack core plugin. It provides basic feature support and integration capabilities for Alibaba Cloud Elasticsearch. |
| aliyun-codec | Non-built-in | 7.10.0 | The Alibaba Cloud codec plugin. It optimizes index storage and query performance and supports custom data encoding policies. |
| aliyun-knn | Built-in | 7.10.0 | The Alibaba Cloud KNN plugin. It supports k-nearest neighbor (k-NN) vector search for similarity retrieval in AI and machine learning (ML) scenarios. |
| aliyun- optimization | Built-in | 7.10.0 | The Alibaba Cloud performance optimization plugin. It improves the efficiency of Elasticsearch clusters using storage and query optimization policies. |
| aliyun-qos | Non-built-in | 7.10.0 | The Alibaba Cloud Quality of Service (QoS) plugin. It manages resource allocation and request priorities to ensure the performance of critical tasks. |
| analysis-aliws | Custom | 7.10.0 | The Alibaba Cloud analysis (AliWS) plugin. It provides custom text processing features, such as industry- specific word segmentation. |
| analysis-icu | Built-in | 7.10.0 | The ICU analysis plugin. It integrates the ICU module from Lucene to support multilingual text processing, such as for Japanese, Korean, and Arabic. |

| analysis-ik | Built-in | 7.10.0 | The IK Chinese analysis plugin. It provides efficient Chinese word segmentation for scenarios such as E- commerce and news. |
|---|---|---|---|
| analysis- kuromoji | Built-in | 7.10.0 | The Japanese (Kuromoji) analysis plugin. It supports tokenization and grammatical parsing for Japanese text. |
| analysis- phonetic | Built-in | 7.10.0 | The phonetic analysis plugin. It uses a phonetic feature filter to enable fuzzy matching based on pronunciation, such as for name searches. |
| analysis-pinyin | Built-in | 7.10.0 | The Pinyin analysis plugin. It converts Chinese characters to Pinyin for tokenization and supports Chinese Pinyin search. |
| analysis-smartcn | Built-in | 7.10.0 | The Smart Chinese analysis plugin. It integrates the Smart Chinese module from Lucene to provide basic Chinese word segmentation. |
| analysis-stempel | Built-in | 7.10.0 | The Polish (Stempel) analysis plugin. It supports tokenization and morphological stemming for Polish text. |
| analysis- ukrainian | built-in | 7.10.0 | The Ukrainian analysis plugin. It supports tokenization and grammatical processing for Ukrainian text. |
| elasticsearch- repository-oss | Built-in | 7.10.0 | The OSS repository plugin. It lets you store Elasticsearch snapshots in Alibaba Cloud Object Storage Service (OSS) for long-term backup and recovery. |
| faster-bulk | No | 7.10.0 | The batch operation optimization plugin. It improves data write performance and reduces latency for batch indexing operations. |
| hybrid-cloud | Built-in | 7.10.0 | The hybrid cloud plugin. It supports hybrid deployments of Alibaba Cloud Elasticsearch with on-premises data centers and enables cross-environment data synchronization. |

| ingest- attachment | Built-in | 7.10.0 | The ingest attachment processor plugin. It uses Apache Tika to parse and extract text from attachments such as PDF and Office files. |
|---|---|---|---|
| mapper- murmur3 | Built-in | 7.10.0 | The Murmur3 hash mapping plugin. It computes and stores the hash of a field's value at index time. This is used to deduplicate data or accelerate searches. |
| mapper-size | Built-in | 7.10.0 | The document size mapping plugin. It records the original, uncompressed size of a document at index time to help monitor storage overhead. |
| opendistro- index- management | Non-built-in | 7.10.0 | The Open Distro index state management plugin. It automates the index lifecycle, such as scrolling, applying retention policies, and migrating between hot, warm, and cold states. |
| opendistro-job- scheduler | Custom | 7.10.0 | The Open Distro job scheduler plugin. It provides a distributed service for scheduling periodic tasks, such as monitoring and maintenance tasks. |
| opendistro secu _ rity | Built-in | 7.10.0 | The Open Distro security plugin. It provides access control, identity verification, and encryption features to secure Elasticsearch clusters. |
| repository-hdfs | Built-in | 7.10.0 | The HDFS repository plugin. It lets you store snapshots in Hadoop Distributed File System (HDFS). This is useful for big data ecosystem integration. |
| repository-s3 | Built-in | 7.10.0 | The S3 repository plugin. It lets you store snapshots in AWS S3 Object Storage Service. This is useful for cross- cloud backup scenarios. |
| sql | Built-in | 7.10.0 | The SQL query plugin. It lets you query Elasticsearch data using SQL syntax, which reduces the learning curve for users. |

| xdcr | Non-built-in | 7.10.0 | The cross-data center replication (XDCR) plugin. It enables multi-region data synchronization and high availability, and supports disaster recovery and data localization. |
|---|---|---|---|

**Version 6.8.13**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| a-pack- repository-oss | Built-in | 6.8.13 | The A-Pack OSS repository plugin. It lets you store Elasticsearch snapshots in Alibaba Cloud OSS for long-term backup and recovery. |
| a-pack-xdcr | Built-in | 6.8.13 | The A-Pack XDCR plugin. It enables multi- region data synchronization and high availability, and supports disaster recovery and data localization. |
| aliyun-knn | Built-in | 6.8.13 | The Alibaba Cloud KNN plugin. It supports k-NN vector search for similarity retrieval in AI and ML scenarios. |
| analysis-aliws | Built-in | 6.8.13 | The Alibaba Cloud analysis (AliWS) plugin. It provides custom text processing features, such as industry-specific word segmentation. |
| analysis-icu | Built-in | 6.8.13 | The ICU analysis plugin. It integrates the ICU module from Lucene to support multilingual text processing, such as for Japanese, Korean, and Arabic. |
| analysis-ik | Built-in | 6.8.13 | The IK Chinese analysis plugin. It provides efficient Chinese word segmentation for scenarios such as E-commerce and news. |
| analysis- kuromoji | Built-in | 6.8.13 | The Japanese (Kuromoji) analysis plugin. It supports tokenization and grammatical parsing for Japanese text. |
| analysis- phonetic | Built-in | 6.8.13 | The phonetic analysis plugin. It uses a phonetic feature filter to enable fuzzy matching based on pronunciation, such as for name searches. |

| analysis-pinyin | Built-in | 6.8.13 | The Pinyin analysis plugin. It converts Chinese characters to Pinyin for tokenization and supports Chinese Pinyin search. |
|---|---|---|---|
| analysis-smartcn | Built-in | 6.8.13 | The Smart Chinese analysis plugin. It integrates the Smart Chinese module from Lucene to provide basic Chinese word segmentation. |
| analysis-stempel | Built-in | 6.8.13 | The Polish (Stempel) analysis plugin. It supports tokenization and morphological stemming for Polish text. |
| analysis- ukrainian | Built-in | 6.8.13 | The Ukrainian analysis plugin. It supports tokenization and grammatical processing for Ukrainian text. |
| ingest- attachment | Built-in | 6.8.13 | The ingest attachment processor plugin. It uses Apache Tika to parse and extract text from attachments such as PDF and Office files. |
| mapper- murmur3 | Built-in | 6.8.13 | The Murmur3 hash mapping plugin. It computes and stores the hash of a field's value at index time. This is used to deduplicate data or accelerate searches. |
| mapper-size | Built-in | 6.8.13 | The document size mapping plugin. It records the original, uncompressed size of a document at index time to help monitor storage overhead. |
| opendistro-job- scheduler | Built-in | 6.8.13 | The Open Distro job scheduler plugin. It provides a distributed service for scheduling periodic tasks, such as monitoring and maintenance tasks. |
| opendistro alerti _ ng | Non-built-in | 6.8.13 | The Open Distro alerting plugin. It supports real-time alerting and notifications, such as email and Slack messages, based on search results. |
| opendistro index _ management _ | Built-in | 6.8.13 | The Open Distro index management plugin. It automates the index lifecycle, such as scrolling, applying retention policies, and migrating between hot, warm, and cold states. |

| opendistro secur _ ity | Built-in | 6.8.13 | The Open Distro security plugin. It provides access control, identity verification, and encryption features to secure Elasticsearch clusters. |
|---|---|---|---|
| opendistro sql _ | Non-built-in | 6.8.13 | The Open Distro SQL plugin. It lets you query Elasticsearch data using SQL syntax, which reduces the learning curve for users. |
| repository-hdfs | Built-in | 6.8.13 | The HDFS repository plugin. It lets you store snapshots in HDFS. This is useful for big data ecosystem integration. |
| repository-s3 | built-in | 6.8.13 | The S3 repository plugin. It lets you store snapshots in AWS S3 Object Storage Service. This is useful for cross-cloud backup scenarios. |
| sqlplugin | Built-in | 6.8.13 | The SQL query plugin. It lets you query Elasticsearch data using SQL syntax and provides SQL interface support that is not from Open Distro. |

**Version 5.5.3**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| analysis-icu | Built-in | 5.5.3 | The ICU analysis plugin. It integrates the ICU module from Lucene to support Unicode and multilingual text processing, such as for Japanese, Korean, and Arabic. |
| analysis-ik | Built-in | 5.5.3 | The IK Chinese analysis plugin. It uses IK Analyzer to provide efficient Chinese word segmentation and search optimization. |
| analysis- kuromoji | Built-in | 5.5.3 | The Japanese (Kuromoji) analysis plugin. It integrates the Kuromoji module from Lucene to support Japanese text analysis. |
| analysis- phonetic | Built-in | 5.5.3 | The phonetic analysis plugin. It uses a phonetic feature filter to enable fuzzy matching based on pronunciation, such as for name searches. |

| analysis-pinyin | Built-in | 5.5.3 | The Pinyin analysis plugin. It converts Chinese characters to Pinyin for tokenization and supports Chinese Pinyin search. |
|---|---|---|---|
| analysis-smartcn | Built-in | 5.5.3 | The Smart Chinese analysis plugin. It integrates the Smart Chinese module from Lucene to provide basic Chinese word segmentation. |
| analysis-stempel | Built-in | 5.5.3 | The Polish (Stempel) analysis plugin. It integrates the Stempel module from Lucene to support Polish text processing. |
| analysis- ukrainian | Built-in | 5.5.3 | The Ukrainian analysis plugin. It integrates the UkrainianMorfologikAnalyzer from Lucene to support Ukrainian text analysis. |
| elasticsearch- repository-oss | Built-in | 5.5.3 | The Alibaba Cloud OSS snapshot repository plugin. It lets you store Elasticsearch snapshots in Alibaba Cloud OSS. |
| gab-paas-plugin | Custom | 5.5.3 | The GAB Platform as a Service (PaaS) plugin. It provides feature support for integration with the Alibaba Cloud PaaS platform. Specific features depend on the business scenario. |
| ingest- attachment | Built-in | 5.5.3 | The ingest attachment processor plugin. It uses Apache Tika to parse and extract text from attachments such as PDF and Office files. |
| ingest-geoip | Built-in | 5.5.3 | The GeoIP analysis processor plugin. It uses the Maxmind database to look up geographic location data from an IP address. |
| ingest-user- agent | Built-in | 5.5.3 | The user agent information extraction processor plugin. It extracts information about devices, browsers, and more from a user agent string. |
| mapper- attachments | Built-in | 5.5.3 | The attachment mapping plugin. It lets you store the content of rich text files, such as PDF and Office documents, as a field and perform full-text searches on it. |

| mapper- murmur3 | Built-in | 5.5.3 | The Murmur3 hash mapping plugin. It computes and stores the hash of a field's value at index time. |
|---|---|---|---|
| mapper-size | Built-in | 5.5.3 | The document size mapping plugin. It records the original, uncompressed size of a document at index time. |
| pangu | Built-in | 5.5.3 | The Pangu repository plugin. It lets you store snapshots in the Alibaba Cloud Pangu distributed storage system. |
| repository-hdfs | Built-in | 5.5.3 | The HDFS repository plugin. It lets you store snapshots in HDFS. |
| repository-s3 | Built-in | 5.5.3 | The S3 repository plugin. It lets you store snapshots in AWS S3 Object Storage Service. |
| search-guard-5 | Built-in | 5.5.3 | The Search Guard 5 security plugin. It provides access control, authentication, and authorization features for Elasticsearch 5. |
| sql | Built-in | 5.5.3 | The SQL query plugin. It lets you query Elasticsearch data using SQL syntax. |

##### 3.2.1.2 Kibana plugins

This topic lists the plugins supported by Kibana and their corresponding versions.

**Version 7.10.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| opendistro- alerting | Non-built-in | 7.10.0 | Open Distro Kibana alerting plugin. Create, manage, and trigger alert rules based on Elasticsearch data in Kibana. |

**Version 6.8.13**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|

| bsearch querybuild _ er | Non-built-in | 6.8.13 | BSearch query builder plugin. Provides a visualization tool to build and test BSearch query statements. |
|---|---|---|---|
| kibana- prometheus- exporter | Non-built-in | 6.8.13 | Kibana Prometheus metrics exporter plugin. Exports Kibana monitoring data (such as performance metrics) to the Prometheus monitoring system. |
| opendistro-alerting | Non-built-in | 6.8.13 | Open Distro Kibana alerting plugin. Create, manage, and trigger alert rules based on Elasticsearch data in Kibana. |

**Version 5.5.3**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| searchguard | Built-in | 5.5.3 | Search Guard Kibana plugin. Integrates Elasticsearch security features (such as access control and identity verification) into Kibana for unified permission management. |

##### 3.2.1.3 OpenSearch plugins

This topic lists the plugins supported by OpenSearch and their corresponding versions.

**Version 3.1.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| analysis-ik | Built-in | 3.1.0 | The IK analyzer for OpenSearch. |
| opensearch- repository-oss- plugin | Built-in | 3.1.0 | Enables integration with Alibaba Cloud OSS as a snapshot repository for backup and recovery operations. |
| prometheus- exporter | Built-in | 3.1.0 | Exposes OpenSearch metrics in Prometheus format. This supports monitoring and alerting through Prometheus and Grafana. |
| opensearch- alerting | Built-in | 3.1.0 | Provides real-time alerting based on search results. It lets you define triggers and actions. |

| opensearch- asynchronous- search | Built-in | 3.1.0 | Supports long-running searches by executing queries asynchronously and retrieving the results later. |
|---|---|---|---|
| opensearch-cross- cluster-replication | Built-in | 3.1.0 | Enables cross-cluster replication for high availability, disaster recovery, and data localization. |
| opensearch- custom-codecs | Built-in | 3.1.0 | Adds support for custom index codecs to optimize storage and performance for specific use cases. |
| opensearch-flow- framework | Built-in | 3.1.0 | Provides a framework to build and manage guided workflows and multi-step processes. |
| opensearch- geospatial | Built-in | 3.1.0 | Extends the geospatial search and analysis capabilities of OpenSearch, including GeoJSON and shape queries. |
| opensearch-index- management | Built-in | 3.1.0 | Automates index lifecycle management, including rollovers, retention policies, and state transitions (hot/warm/cold). |
| opensearch-job- scheduler | Built-in | 3.1.0 | Provides a distributed task scheduling service for periodic tasks, such as monitoring and maintenance. |
| opensearch-knn | Built-in | 3.1.0 | Supports k-nearest neighbor (k-NN) vector search for similarity search and AI/ML applications. |
| opensearch-ltr | Built-in | 3.1.0 | Supports learning to rank (LTR) based on machine learning models to improve search relevance. |
| opensearch- notifications | Built-in | 3.1.0 | A centralized notification service that sends alerts through channels such as email, Slack, and Chime. |
| opensearch- notifications-core | Built-in | 3.1.0 | The core module of the notification system. It provides APIs and a messaging infrastructure. |
| opensearch- observability | Built-in | 3.1.0 | A unified observability solution for logs, metrics, traces, and user experience. |

| opensearch- reports-scheduler | Built-in | 3.1.0 | Schedules and distributes reports generated from dashboards and visualizations on a regular basis. |
|---|---|---|---|
| opensearch- security | Built-in | 3.1.0 | A comprehensive security plugin that provides authentication, authorization, encryption, and audit logs. |
| opensearch-sql | Built-in | 3.1.0 | Provides a SQL interface to query OpenSearch indexes using familiar SQL syntax. |
| opensearch- system-templates | Built-in | 3.1.0 | Manages system-generated index templates used for internal OpenSearch features and plugins. |
| query-insights | Built-in | 3.1.0 | Analyzes search query performance, latency, and resource usage to optimize relevance and efficiency. |

##### 3.2.1.4 Dashboard plugins

This topic lists the supported Dashboard plugins and their versions.

**Version 3.1.0**

| Plugin name | Built-in | Plugin version | Description |
|---|---|---|---|
| indexManagement Dashboards | Built-in | 3.1.0 | Provides an interface to monitor and manage index lifecycles. Supported operations include rollover, deletion, and state transition. |

#### 3.2.2 Upload, update, and delete plugins

The plugin management feature lets you upload, update, and delete Elasticsearch, Logstash, Kibana, OpenSearch, and Dashboard plugins. The plugins described in this topic are platform plugins managed separately by instance version. Plugin installation and upgrades depend on the platform's plugin library.

**Go to the plug-in management page**

1. Log on to the Search & Analytics Service O&M console.
2. In the navigation pane on the left, click **Platform Management**.
3. Under **Plugin Management**, click **Elasticsearch Plugin**, **Logstash Plugin**, **Kibana**
**Plugin**, **OpenSearch Plugin**, or **Dashboard Plugin** to go to the corresponding plugin
management page. This topic uses Elasticsearch plugins as an example. The operations for other types of plugins are similar.

**View platform plug-ins**

1. Go to the plug-in management page.
2. In the top-left corner of the page, select a version to view the plugins that the platform
supports. The following figure uses Elasticsearch plugins as an example.

**Upload a plug-in**

**Important**

You can upload custom plugins, but not all custom plugins are supported. For example, plugins related to X-Pack, such as Security, ML, Alerting, index lifecycle management (ILM), and Reporting, are not supported. Third-party plugins that depend on the X-Pack API are also not supported.
1. Go to the plug-in management page.
2. In the top-left corner of the page, select the version.
3. Click **Upload Plugin**.
4. In the **Upload Plugin** dialog box, upload the plug-in installation package.
5. Click **Upload**.
After the upload is successful, the plugin appears in the plugin list. If the uploaded plugin is not visible, click **Refresh** in the upper-right corner to refresh the plugin list and check again.

**Update a plug-in**

**Important**

Built-in plugins cannot be updated.
1. Go to the plug-in management page.
2. In the upper-left corner, select the version.
3. Click **Update** in the **Action** column of a plug-in.
4. In the **Update Plugin** dialog box, upload the plug-in installation package.
5. Click **Upload**.

**Delete a plug-in**

**Warning**

After a plugin is deleted, it must be reinstalled before you can use it again. Proceed with caution. If an existing cluster uses the plugin to be deleted, the cluster's rolling operations, scale-out operations, and automatic restarts will fail after the plugin is deleted.
1. Go to the plug-in management page.
2. In the top-left corner of the page, select the version.
3. Click **Delete** in the **Action** column of a plug-in.
4. Click **Confirm**.

### 3.3 Resource management

This topic describes how to view the resource usage of physical machines on the Resource Management page.

**Procedure**

1. Log in to the Elasticsearch O&M console.
2. In the left-side navigation pane, choose **Platform Management > Resource**
**Management > Resource Management**.
3. On the **Resource Management** page, enter the name of the target physical machine in
the search box and view the resource usage. The displayed resource usage includes **Physical Server Name**, **CPU Allocated**
**Resources**, **CPU Remaining Resources**, **CPU**, **Memory Allocated Resources**, **Memory**
**Remaining Resources**, and **Memory Size**.

### 3.4 Zone configuration

The zone configuration feature lets you manage zones based on the deployment method of Elasticsearch clusters. This topic describes how to modify the zone configuration.

**Limits**

Zone configuration is supported only for Elasticsearch instances that are deployed with a dual-zone or multi-zone configuration. OpenSearch instances currently support only single-zone deployments.

**Modify the zone configuration**

1. Log in to the Elasticsearch O&M console.
2. In the navigation pane on the left, choose **Platform Management > Availability Zone**
**Configuration > Availability Zone Configuration**.
3. On the **Availability Zone Configuration** page, click **Modify Configuration**.
4. Select a deployment method and zones as needed.
5. Click **Save**.

### 3.5 Operation control

The operation control feature lets you manage the network type and resource ownership of newly created instances and control user-initiated modification operations based on your business needs.

**Procedure**

1. Log in to the Elasticsearch Operations and Maintenance (O&M) console.
2. In the navigation pane on the left, choose **Platform Management > Operation Control**
**> Operation Control**.
3. On the **Operation Control** page, configure the network type control, resource ownership,
and modification operation control settings for newly created instances.

**Warning**

This configuration affects user access. Modify this configuration with caution. Follow the instructions and notes on the console.

**The network type control setting for newly created instances of the current**

**cloud platform (ascm-Elasticsearch)**: **Allow AnyTunnel usage** or **Disallow**
**AnyTunnel usage**.
For security purposes, we recommend that you select SingleTunnel when you create a cluster. If you want to limit the use of AnyTunnel, you can select **Disallow AnyTunnel**
**usage**. The change takes effect only on clusters created after you make the change. The
existing clusters are not affected.

**The resource ownership for newly created instances of the current cloud**

**platform (ascm-Elasticsearch)**: **Dedicated resource pool** or **Shared resource pool**.

**The modification operation control setting for the current cloud platform**

**(ascm-Elasticsearch)**: **Allow changes (users can perform instance modification**
**operations in both the user console and the O&M console)**, **Disallow changes**
**only in the user console**, or **Disallow all changes**.
If your cloud platform is under lockdown or you need to restrict modification operations for a specific period, you can update this setting. When this option is set to **Disallow all changes**, operations such as cluster creation, scale-out, configuration modification, or plugin installation are not allowed in either the user console or the O&M console. The display of information is not affected.
4. Click **Modify**.

### 3.6 Benchmark testing

To verify whether a new Elasticsearch (ES) cluster configuration meets your business requirements, use the benchmark testing feature in Alibaba Cloud ES. This feature evaluates the cluster's read and write performance through a one-click test.

**Introduction to one-click benchmark testing plans**

A one-click benchmark test consists of two parts: Machine performance test: Evaluates the performance of cluster hardware, including CPU, memory, and disk I/O. Key metrics are as follows: CPU speed: single-core computing capability CPU dispatch speed: context switching scheduling capability Memory write speed: memory write throughput Memory read speed: memory read throughput Disk I/O read speed: disk read throughput Disk I/O write speed: disk write throughput ESRally stress testing: Evaluates the write and query performance of the cluster. The stress testing configurations are as follows:

| Item | Description |
|---|---|
| ESRally configurations | The default ESRally tracks are used. |
| Dataset | The preset http logs dataset from ESRally is used to simulate test _ scenarios. |
| Number of shards | Primary shards: 5 Replica shards: 0 |
| bulk size _ | 5,000 documents are submitted in each batch operation. |
| bulk indexing client _ _ s | 8 clients are used to concurrently execute batch indexing operations. |
| Output | The report is generated in CSV format. |

**Procedure**

**Important**

Benchmark testing requires reading and writing data on the destination cluster, which affects the cluster's read and write performance. Run tests on production clusters with caution.
1. Log on to the Search & Analysis Service O&M console.
2. In the left navigation pane, click **Platform Management**.
3. Choose **Benchmark Testing > Benchmark Testing**.
4. Create a test.
i. Enter the instance ID, username, and password for the instance that you want to test. ii. As needed, select a test plan and specify whether to force execution. Default stress test: Uses ESRally for stress testing. Default stress test with automatic deletion of the test index after completion: This option uses the default stress test and adds an operation to delete the test index once the test finishes. iii. Click **Confirm**. The new test task appears in the list on the Benchmark Testing page.
5. View the benchmark test results.
During test execution, click **View Job** to view the execution information of the test task. Wait for the test task to complete, and then click **View Results**. The performance test results for the destination cluster appear in the dialog box. In the **View Results** dialog box, click **Download Detailed Results** to download the test results to your computer for viewing.
6. (Optional) Delete benchmark test results
On the Benchmark Testing page, in the **Actions** column, click **Delete** for the target test record to delete it. Select the records that you want to delete and click **Batch Delete** to delete multiple records at once.

## 4 Logging and monitoring

### 4.1 View logs

This topic describes the types and levels of Elasticsearch logs and how to view logs.

**Log types**

**Control component logs**: include the logs of ESSEN, Bingo, cms_sync**-**deploy, Operator,
and the baseline Elasticsearch cluster. The following table describes the namespaces to which the components belong.

| Component Name | namespace |
|---|---|
| ESSEN and cms-sync-deploy | essen |
| Bingo | bingo |
| Operator and the baseline Elasticsearch cluster | elasticsearch |

**Cluster logs**: include the logs of Elasticsearch clusters and Elasticsearch audit logs.

**Log levels**

**warn**: warning information.
**error**: error information, which indicates a program error.
If logs of the error type are generated or you have any questions about the logs, submit a ticket.

**View the logs of control components**

1. Log on to the OPS1 machine.
2. Run the following command to obtain the component name ${podname}:

```bash
kubectl get pod -n ${namespace}
```

| ${namespace} | indicates the na |
|---|---|
|   | ${namespace} |
| component, set |   |

${namespace} indicates the namespace of the component. To view the logs of the ESSEN
3. Run the following command to view the component logs:

```bash
kubectl logs ${podname} -n ${namespace} | tail -n 500
```

**View product logs**

You can use one of the following methods to view the logs of the baseline Elasticsearch cluster and the logs of an Elasticsearch cluster. Method 1: This mode lets you view up to 100 log entries in the user-side console. i. Log in to the user-side console of the Elasticsearch cluster. For more information, see **Log on to the Alibaba Cloud Elasticsearch Service conso**
**le** in the **Elasticsearch User Guide**.
ii. In the navigation pane on the left, click **Instance List**. iii. On the **Instance List** page, click the ID of the target instance. iv. In the **Node Visualization** section of the **Basic Information** page, move the pointer over the desired node and click **View Node Logs**. In the message that appears, view the node logs. Method 2: i. Log on to the OPS1 machine. ii. Run the following command to obtain the component name ${podname} :

```bash
kubectl get pod -n ${namespace}
```

${namespace} indicates the namespace of the component. The baseline Elasticsearch cluster is used as an example. In this case, set ${namespace} to elasticsearch. iii. Run the following command to view the component logs.

```bash
kubectl logs ${podname} -n ${namespace} | tail -n 500
```

Method 3:

**Important**

You can use this method to view the logs of an Elasticsearch cluster whose version is V5.5.3, V6.8.13, or V7.10. For more information, see the Determine whether an image uses an old or new Elasticsearch version section of this topic. i. Log on to the OPS1 machine. ii. Run the following command to obtain the component name ${podname} :

```bash
kubectl get pod -n ${namespace}
```

${namespace} indicates the namespace of the component. The baseline Elasticsearch cluster is used as an example. In this case, set ${namespace} to elasticsearch. iii. Run the following command to log in to an Elasticsearch container:

```bash
kubectl exec -it ${podname} -c es bash -n elasticsearch
```

${podname} indicates the name of the component that you obtained. iv. Run the following command to access the folder of the logs:

```
cd /usr/share/elasticsearch/logs/
```

All node logs of an Elasticsearch cluster are stored in the /usr/share/elasticsearch/logs/ directory of the container. v. Run the following command to view log files: `ls` Method 4: i. Log on to the Apsara Uni-manager Operations Console. ii. Choose **Platform O&M > Log Query** to go to the Log Query page. iii. On the **Platform Logs** tab, specify filter conditions to search for logs. By default, Elasticsearch has slow indexing logs disabled. Before you query slow indexing logs, you need to manually modify the Elasticsearch configuration to load the `log4j` configuration file to enable slow indexing logs. For more information, see Slow Log. Set **Products** to `elasticsearch` and **Log Name** to `elasticsearchlog` , and specify other filter conditions as needed. In the **Export List** section, you can filter for target logs by keyword, such as `index.search.accesslog` , or choose to display only abnormal logs. Move the pointer over the desired log to view the log details, such as the log time, log level, IP address, request, and response. Elasticsearch cluster logs:

| Log type | Log File Name | Description | Use scenario |
|---|---|---|---|
| Main log | elasticsear ch- cluster.log | This type of log records the health status of an Elasticsearch cluster and the information about query and write operations performed on indexes. Logs for write operations include logs generated for index creation, index mapping updates, and full write queues. Logs for query operations include logs generated for query queues and query exceptions. | View the status of each node in an Elasticsearch cluster or view information about query and write operations, such as information about network connectivity between nodes, full garbage collection (GC), index creation or deletion, or errors reported for cluster-level queries. If errors occur in your business, we recommend that you first view the cluster logs and monitoring data of your cluster to troubleshoot performance or configuration issues. For more information, see Logging. |
| Searc h slow query logs | elasticsear ch- cluster ind _ ex search _ slowlog.lo _ g | When a query's execution time exceeds the specified threshold, information about the query is recorded in the Redis Slow Log. The slow query threshold is preconfigured in the index template of the scenario- based template. The default configuration is optimal, and you can apply it with a single click. For more information, see Index template configuration. | If a long period of time is required to complete a read operation in your business, you can view slow search logs to troubleshoot the issue. Read operations that require a longer period of time to complete consume more cluster resources. If many slow logs are generated for a cluster, check the resource usage and loads of the cluster to identify the items that cause bottleneck issues. Then, scale out resources for the cluster to ensure the stability of the cluster. For more information, see Slow Log. |

| Slow indexi ng log | elasticsear ch- cluster ind _ ex indexin _ g slowlog. _ log | If the time that is required to complete a write operation exceeds a specific threshold, the write operation is considered as a slow write operation, and the system displays information about the operation in slow indexing logs. The slow write threshold is configured with an optimal default value in the scenario-based index template, which you can apply with a single click. For more information, see Index Template Configuration. | If a long period of time is required to complete a write operation in your business, you can view slow indexing logs to troubleshoot the issue. Write operations that require a longer period of time to complete consume more cluster resources. If many slow logs are generated for a cluster, check the resource usage and loads of the cluster to identify the items that cause bottleneck issues. Then, scale out resources for the cluster to ensure the stability of the cluster. For more information, see Slow Log. |
|---|---|---|---|
| GC log | gc.log | The logs of a garbage collector contain information about GC triggered by JVM heap memory usage. You can obtain GC details, including information about GC based on Old GC, Concurrent Mark Sweep (CMS) GC, Full GC, and Minor GC. | If a performance bottleneck occurs on a cluster, you can view GC details in the GC logs of the cluster and check whether GC operations require a long period of time to complete or are frequently performed. If such GC operations exist, scale out resources for the cluster at your earliest opportunity to ensure the stability of the cluster. Note By default, Elasticsearch clusters use the CMS garbage collector. However, for data nodes with 32 GB or more of memory, the G1 garbage collector is recommended to improve Garbage Collection (GC) efficiency. |
| Audit log | elasticsear ch- cluster au _ dit log.log _ | This type of log records information about auditing of operations that are performed on an Elasticsearch cluster, such as the create, delete, modify, and query operations. | If your identity fails to be verified when you access an Elasticsearch cluster, a connection to the cluster is denied, you need to view the access events of the cluster, or you need to check whether suspicious events exist, you can troubleshoot the issue or perform the desired operation based on the audit logs of the cluster. |

| SSL trans missio n log | elasticsear ch- cluster ssl _ transport. _ log | In an Elasticsearch cluster, communication between nodes is encrypted using SSL or TLS to ensure data security and prevent data stealing or tampering. SSL transmission logs are used to record errors and exceptions during SSL or TLS connection establishment, handshake, and data transmission. | Query the detailed information about data transmission over SSL between Elasticsearch nodes. |
|---|---|---|---|
| Depre cation logs | elasticsear ch- cluster de _ precation.l og | Using APIs or features that have been replaced or removed in Elasticsearch clusters may cause system stability issues or errors. Deprecation logs record the use of deprecated APIs and features in Elasticsearch clusters. | Helps you promptly identify deprecated APIs and features that are still in use in the cluster, so you can take measures to fix or migrate them. |

You can view the log output configuration in the $ES_HOME/config/log4j2.properties file. For more information about the log4j configuration, see Appenders.

**View product audit logs**

The procedure for viewing audit logs varies based on the Elasticsearch version used by the image. You need to determine whether the image uses an old Elasticsearch version or a new version. For more information, see the Determine whether an image uses an old or new Elasticsearch version section of this topic.

**View Audit Logs for Clusters Based on Older Image Versions**

1. Log in to the Kibana console of the Elasticsearch cluster. For more information, see Log in to
the Kibana console. In this example, a cluster of Elasticsearch V7.10 is used. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.
2. In the navigation pane on the left, click the
icon and choose **Management > Dev**
**Tools**.
3. On the **Console** tab, run the following commands to view audit logs.
i. Query the index name of the audit logs.

```
GET _cat/indices/security*
```

ii. Query the content of the index using a custom query statement.

```
GET ${index_name}/_search
```

`{`

```
    …  #The query statement.
```

`}` ${index_name} indicates the name of the audit index. iii. Count the number of audit indexes.

```
GET security-auditlog-*/_search
```

`{`

```json
  "size": 0,
  "aggs": {
    "c": {
      "terms": {
        "field": "audit_category.keyword",
        "size": 10
```

`}` `}` `}` `}`

**View new version image cluster audit log**

1. Log on to the OPS1 machine.
2. Run the following command to obtain the component name ${podname} :

```bash
kubectl get pod -n ${namespace}
```

${namespace} indicates the namespace of the component. The baseline Elasticsearch cluster is used as an example. In this case, set ${namespace} to elasticsearch.
3. Run the following command to log in to an Elasticsearch container:

```bash
kubectl exec -it ${podname} -c es bash -n elasticsearch
```

${podname} indicates the name of the component that you obtained.
4. Run the following command to access the folder of the logs:

```
cd /usr/share/elasticsearch/logs/
```

All node logs of an Elasticsearch cluster are stored in the /usr/share/elasticsearch/logs/ directory of the container.
5. Run the following command to view log files:
`ls` You can run the `ls` command to list all types of Elasticsearch logs. The audit log file is named elasticsearch-cluster_audit_log.log.
6. View the audit logs.

```
cat -n elasticsearch-cluster_audit_log.log
```

**Identifying new and old image versions**

An image is considered a new version if its tag is greater than or equal to the version listed below. Otherwise, it is an old version.

| Architecture | Version |
|---|---|
| x86 | 5.5.3 0.0.0 3 2 _ _ _ 6.3.2 1.0.3 _ 6.8.13 1.3.0 8 1 _ _ _ 6.8.2 1.0.6 _ 7.10.0 1.6.0 13 1 _ _ _ 7.2.1 1.0.3 _ 7.4.0 1.0.2 _ |
| Arm | 6.8.13 1.3.0 3 1 _ _ _ 7.10.0 1.6.0 3 1 _ _ _ |

You can run the following command to view the tag number of an image:

```bash
kubectl get es ${es_name} -o yaml -n ${namespace} | grep -w image
```

${es_name} indicates the name of the Elasticsearch cluster. ${namespace} specifies the namespace of the Elasticsearch instance.

|   | kubectl get es -A |
|---|---|
| ${es name} _ |   |

You can run the `kubectl get es -A` command to query the mapping between the The baseline Elasticsearch cluster is used as an example. Run the `kubectl get es` elasticsearch-cluster -o yaml -n elasticsearch | grep -w image command to query the tag number of the image. The following figure shows the result. The retrieved image tag is 6.8.13_1.3.0_5-arm64. For the ARM architecture, version 6.8.13_1.3.0_5 is newer than 6.8.13_1.3.0_3_1. Therefore, this baseline cluster uses a newer image version.

### 4.2 View the monitoring metrics of Elasticsearch clusters in the Apsara Uni-manager Operations Console

**of Elasticsearch clusters in the**

**Apsara Uni-manager Operations**

**Console**

The default monitoring and alerting feature in the Apsara Uni-manager Operations Console allows you to view the Elasticsearch monitoring metrics, track real-time service status, and promptly address potential risks to ensure stable service operation. This topic describes each monitoring metric and its impact.

**View monitoring metrics**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alert > Alert Management > Alert List**.
3. On the **Alert List** page, select **elasticsearch** from the **Resource Owner** drop-down list to
view the default monitoring metrics of the Elasticsearch service. The Elasticsearch service supports the following alerts: Elasticsearch_health_up Elastic_Cluster_Health_RED Elastic_Cluster_Health_Yellow Elasticsearch_Pending_Tasks Elasticsearch_JVM_Heap_Too_High Elasticsearch_JVM_Heap_Warning Elasticsearch_Disk_Out_Of_Space Elasticsearch_Disk_Space_Low Elasticsearch_Cpu_Usage_Too_High Elasticsearch_Count_of_JVM_GC_Runs Elasticsearch_slow_young_gc Elasticsearch_slow_old_gc Elasticsearch_young_gc_surge Elasticsearch_old_gc_surge Elasticsearch_XDCR_Too_Many_Repository Elasticsearch_XDCR_Synchronize_Error Elasticsearch_XDCR_Synchronize_Max In addition to the default monitoring metrics, you can also use the capabilities of the operations console to customize alert rules based on your business scenarios. For more information, see **Alert rules** in **Alert management** of **Apsara Uni-manager**
**Operations Console User Guide**.

**Elasticsearch_health_up**

**Description**

If the cluster health status cannot be obtained, this alert is immediately triggered.

**Impact**

This alert obtains information from the `_cluster/health` interface of the cluster. This alert indicates that the `_cluster/health` port does not respond. In this case, the cluster may be under heavy load or even unavailable.

**Elastic_Cluster_Health_RED**

**Description**

If the cluster health status is red, this alert is immediately triggered.

**Impact**

The primary shard of an index is not assigned.

**Elastic_Cluster_Health_Yellow**

**Description**

If the cluster health status remains yellow for five minutes, this alert is triggered.

**Impact**

The unassigned replica shards belonging to the index compromise the high availability of the cluster.

**Elasticsearch_Pending_Tasks**

**Description**

If the cluster has a pending task for five minutes, this alert is triggered.

**Elasticsearch_JVM_Heap_Too_High**

**Description**

If the usage of the Java Virtual Machine (JVM) remains greater than 90% for five minutes, this alert is triggered.

**Impact**

The cluster is under heavy load, which may increase the latency for some services.

**Elasticsearch_JVM_Heap_Warning**

**Description**

If the JVM usage remains greater than 80% for five minutes, this alert is triggered.

**Impact**

The cluster is under heavy load, which may increase the latency for some services.

**Elasticsearch_Disk_Out_Of_Space**

**Description**

If the available disk space of the cluster remains less than 10% of the total space, this alert is triggered immediately.

**Impact**

This may cause an index write failure.

**Elasticsearch_Disk_Space_Low**

**Description**

If the available disk space of the cluster remains less than 20% of the total space for two minutes, this alert is triggered.

**Impact**

The disk usage reaches the alert threshold.

**Elasticsearch_Cpu_Usage_Too_High**

**Description**

If the CPU load of the cluster remains greater than 90% for one minute, this alert is triggered.

**Impact**

The cluster is under heavy load, which may increase the service latency.

**Elasticsearch_Count_of_JVM_GC_Runs**

**Description**

If the number of JVM garbage collection (GC) events per second remains greater than five for one minute, this alert is triggered.

**Elasticsearch_slow_young_gc**

**Description**

If the Young GC duration per second remains greater than 0.5 seconds for five minutes, this alert is triggered.

**Elasticsearch_slow_old_gc**

**Description**

If the Old GC duration per second remains greater than 0.8 seconds for five minutes, this alert is triggered.

**Elasticsearch_young_gc_surge**

**Description**

if the time of the Young GC remains greater than 10 times the average time in the last three hours for five minutes, this alert is triggered.

**Elasticsearch_old_gc_surge**

**Description**

If the time of the old GC remains greater than 10 times of the average time in the last three hours for five minutes, this alert is triggered.

**Elasticsearch_XDCR_Too_Many_Repository**

Only XDCR-related alerts are supported in V6.8.13. XDCR-related alerts are not supported in V7.10.0.

**Description**

If a secondary XDCR cluster corresponds to multiple primary XDCR clusters, this alert is triggered.

**Impact**

XDCR synchronization is abnormal.

**Elasticsearch_XDCR_Synchronize_Error**

Only XDCR-related alerts are supported in V6.8.13. XDCR-related alerts are not supported in V7.10.0.

**Description**

If data written into the XDCR primary cluster is not synchronized to the secondary cluster and this situation lasts for five minutes, this alert is triggered.

**Impact**

Synchronization exceptions affect disaster recovery.

**Elasticsearch_XDCR_Synchronize_Max**

Only XDCR-related alerts are supported in V6.8.13. XDCR-related alerts are not supported in V7.10.0.

**Description**

If the index synchronization speed of the secondary cluster remains lower than the write speed of primary cluster index for five minutes, this alert is triggered.

### 4.3 Use custom dashboards to view metrics of Elasticsearch clusters

**view metrics of Elasticsearch**

**clusters**

This topic describes how to view the metrics of Elasticsearch clusters on a custom dashboard.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alert > Monitor Management > TianjiMon**
    - **- Dashboard**.
3. In the left-side navigation pane, choose **Data Dashboard > Custom Dashboard**.
4. In the **Dashboard directory** list, select **Elasticsearch Monitoring Dashboard**.
5. Click the dashboard name **ElasticSearch** or **OpenSearch Cluster Dashboard** to access
the dashboard and view the metrics. The key metrics are described as follows. The metrics displayed in the console shall prevail.

**ElasticSearch metrics**

| Category | Metric | Description |
|---|---|---|
| Cluster | Cluster health | The cluster health status. The overall availability is identified by colors: green (all shards are properly allocated), yellow (replica shards are unallocated, posing risks), and red (primary shards are unallocated, indicating data loss). |
|   | Node state | The node role status, which distinguishes the role types such as data nodes and coordinating nodes and their distribution. |
|   | Data state max | The maximum resource usage on data nodes. This metric monitors the peak utilization of CPU, Java Virtual Machine (JVM) heap memory, and disk space on data nodes. |
|   | Coordinating state max | The maximum resource usage on coordinating nodes. This metric monitors the peak load of CPU and JVM heap memory on coordinating nodes (non- data/ingest nodes). |
|   | Index State | The core status metric for indexes. This metric includes the memory occupied by document values, the number of segments, and the total number of documents, reflecting the health of the underlying index structure. |
|   | Pending tasks | The pending cluster tasks. This metric displays cluster-level operations awaiting execution, such as index creation and shard allocation. A continuously non-zero or increasing value indicates primary node overload or task blocking. |

|   | Tripped for breakers | The circuit breaker trigger statistics. This metric tracks the number of requests rejected due to memory overload. A value greater than 0 indicates excessive memory pressure on the node. |
|---|---|---|
|   | Open file descriptors per cluster | The total number of cluster file descriptors. This metric reflects the total number of open file handles across all nodes. An excessively large value may lead to system resource exhaustion. |
|   | Active shards | The total number of active shards, which is the sum of primary and replica shards in the cluster that are currently in service. |
|   | Active primary shards | The number of active primary shards, which indicates the number of primary shards in the cluster currently available for write operations. |
|   | Shard per node | This metric realizes load balance of shards between nodes by calculating the average number of primary shards on each data node. An excessively large value may lead to hot issues. |
|   | Unassigned shards | The number of shards that have not been successfully allocated to any node. A value greater than 0 indicates inaccessible data or degraded query performance. |
| Shards |   |   |
|   | Initializing shards | The number of shards being initialized, which indicates the number of shards in the recovery or creation process. A continuously large value indicates slow cluster recovery. |
|   | Relocating shards | The number of shards being relocated, which indicates the number of shards that are migrating between nodes. This metric reflects the intensity of cluster load balancing. |
|   | Delayed shards | The number of shards whose allocation is delayed due to timeout or unmet conditions. |
| Nodes & Indices | Nodes stats | The real-time node resource status. This metric displays node-level metrics of CPU, JVM memory, disk space, and system load, as well as the index storage volume and the total number of documents and segments. |
|   | > Document Version: 2026062 |   |

| sticsearch |   |   |
|---|---|---|
|   | Index stats | The core performance metrics of indexes. This metric includes key statistics such as the number of shards and replicas, the total number of documents, storage volume, active queries, and segment memory. |
| JVM Garbage Collection | Young GC count | The rate of young garbage collection (GC), which indicates the frequency of JVM young GC triggers per unit of time. A high frequency may indicate excessively fast object creation. |
|   | Old GC count | The rate of old GC, which indicates the frequency of JVM old GC triggers per unit of time. A high frequency may indicate memory leaks or insufficient heap configuration. |
|   | Young GC time | The time consumed by JVM young GC per unit of time on CPU. This metric affects write and query latency. |
|   | Old GC time | The time consumed by JVM old GC per unit of time on CPU. Prolonged pauses can cause service stutters. |
| Translog | Total translog operations | The rate of change in total transaction log operations, which indicates the number of operations written to the transaction log per unit of time. This metric reflects the intensity of the write load. |
|   | Total translog size in bytes | The change rate of the transaction log size, which indicates the number of bytes increased in the transaction log per unit of time. An excessively large size may impact the recovery speed. |
| Breakers | Tripped for breakers | The circuit breaker trigger statistics. This metric measures the number of requests rejected due to memory overload. A value greater than 0 indicates excessive memory pressure on the node. |
|   | Estimated size in bytes of breaker | The estimated number of memory bytes for circuit breakers. This system compares the estimated number of memory bytes of the current request against the circuit breaker threshold to prevent Out-of-Memory (OOM) errors. |
|   | CPU usage | The node CPU usage, which indicates the percentage of CPU resource consumption at the operating system level. |

| erations and Maintena Logging and monitorin |   |   |
|---|---|---|
| CPU and Memory |   |   |
|   | Young - JVM heap memory used | The amount of JVM heap memory used in the young generation (Eden/Survivor spaces). |
|   | Load1 average | The average CPU load of the node over the last one minute, which reflects short-term pressure. |
|   | Old - JVM heap memory used | The amount of JVM heap memory used in the old generation. A continuous increase may indicate memory leaks. |
|   | Load5 average | The average CPU load of the node over the last five minutes. This metric reflects medium-term pressure trends. |
|   | JVM non-heap memory usage | The percentage of non-heap memory (such as Metaspace and thread stacks) occupied by JVMs. |
|   | Load15 average | The average CPU load of the node over the last 15 minutes, which reflects long-term pressure trends. |
|   | JVM peak memory usage | The highest historical JVM memory usage in bytes, used for capacity planning. |
|   | JVM heap memory used | The percentage of heap memory occupied by JVMs relative to the maximum heap memory. Exercise caution if the value exceeds 75%. |
| Disk and Network | Disk IO throughput | The amount of data read from and written to the disk per unit of time (in KB/s), which reflects storage performance bottlenecks. |
|   | Total Disk Operations rate | The total IOPS (including the number of read and write operations) of a disk per unit of time. A large value may impact query latency. |
|   | Disk usage size | The number of disk bytes occupied by the Elasticsearch data directory on the node. |
|   | Network usage sent | The number of data bytes transmitted outbound (such as shard recovery and replica synchronization) from the node per unit of time. |
|   | Disk usage | The percentage of used space in the data directory against the total space. If the value exceeds 85%, capacity expansion is required. |
|   | > Document Version: 2026062 |   |

|   | Network usage received | The number of data bytes received (during client writes, cross-node queries, and other operations) by the node per unit of time. |
|---|---|---|
|   | Documents count on node | The total number of index documents hosted on the current node, which reflects the balance of data distribution. |
|   | Documents indexed rate | The number of successfully written documents per unit of time, which serves as a core write performance metric. |
| Documents |   |   |
|   | Documents deleted rate | The number of documents deleted per unit of time. A high frequency may impact segment merging efficiency. |
|   | Documents merged rate | The number of documents processed by segment merge operations per unit of time, which reflects the background optimization load. |
|   | Documents merged bytes | The number of data bytes processed by segment merge operations per unit of time. A large value consumes significant I/O resources. |
| Total Operations and time | Node indexing operations rate | The number of indexing requests processed by a single node per unit of time. |
|   | Node indexing operations time | The average time (in seconds) taken by a single node to process a single indexing request, which affects write latency. |
|   | Node query operations rate | The number of query requests processed by a single node per unit of time. |
|   | Node query operations time | The average time (in seconds) taken by a single node to process a single query request, which directly impacts user experience. |
|   | Index indexing operations rate | The number of indexing requests processed by a single index per unit of time. |
|   | Index Indexing operations time | The average time (in seconds) taken by a single index to process a single indexing request. |

|   | Index query operations rate | The number of query requests processed by a single index per unit of time. |
|---|---|---|
|   | Index query operations time | The average time (in seconds) taken by a single index to process a single query request. |
|   | Merging time | The total time (in seconds) consumed by segment merge operations per unit of time. A large value will slow down write performance. |
|   | Throttle time for index store | The cumulative wait time of operations throttled due to disk I/O overload, which reflects storage bottlenecks. |
|   | Other Operations rate | The request frequency statistics for operations including get, refresh, and flush. |
|   | Other operations time | The average processing time per operation for operations including get, refresh, and flush. |
| Thread Pool | Write threads active | The number of active threads that process index and delete requests. A continuously large value indicates heavy write pressure. |
|   | Write thread queued | The number of pending index and delete requests queued for processing. |
|   | Write thread rejected | The number of write requests rejected due to a full queue or insufficient resources. |
|   | Search threads active | The number of active threads that process search requests. A large value indicates heavy query load. |
|   | Search thread queued | The number of pending search requests queued for processing. |
|   | Search thread rejected | The number of search requests rejected due to a full queue or insufficient resources. |
|   | Thread Pool others threads active | The number of active threads that process non- write and non-query operations, such as merges and snapshots. |
|   | Thread Pool others operations queued | The number of pending non-write and non-query requests queued for processing. |

|   | Thread Pool others operations rejected | The number of non-write and non-query requests rejected by thread pools. |
|---|---|---|
|   | Thread Pool operations completed | The total number of requests successfully processed by all thread pools per unit of time. |
| Caches | Field data memory size | The number of bytes occupied by the fielddata cache used for aggregations and sorting. |
|   | Field data evictions | The number of times the fielddata cache is forcibly cleared due to insufficient memory. High-frequency cleanups lead to performance degradation. |
|   | Query cache size | The number of bytes of memory occupied by cached query results. |
|   | Query cache evictions | The rate at which cache entries are evicted due to insufficient space, which impacts repeated query performance. |
|   | Evictions from filter cache | The number of times filter caches are evicted due to memory pressure, which impacts range query performance. |
| Segments | Count of index segments | The total number of Lucene segments in the current index. An excessive number of segments reduces query efficiency. |
|   | Current memory size of segments in bytes | The number of bytes of metadata cached in memory for all index segments (excluding document data). |
| Indices: Count of documents and Total size | Count of documents with only primary shards | The total number of documents hosted across all primary shards (excluding replicas), which reflects the effective data volume. |
|   | Total size of stored index data in bytes with only primary shards on all nodes | The total number of raw data bytes of primary shards across all nodes (excluding replicas), which is used for capacity planning. |
|   | Total size of stored index data in bytes with all shards on all nodes | The total number of data bytes of both primary and replica shards across all nodes, which reflects the actual disk usage. |

| Indices: Index writer | Index writer with only primary shards on all nodes in bytes | The number of bytes of documents temporarily stored in memory and pending refresh for primary shards. |
|---|---|---|
|   | Index writer with all shards on all nodes in bytes | The number of bytes of documents temporarily stored in memory and pending refresh for both primary and replica shards. |
| Indices: Segments | Segments with only primary shards on all nodes | The total number of Lucene segments contained across all primary shards. |
|   | Segments with all shards on all nodes | The total number of Lucene segments across all primary and replica shards (as replicas are stored independently). |
|   | Size of segments with only primary shards on all nodes in bytes | The total number of bytes occupied by segment metadata in memory for primary shards. |
|   | Size of segments with all shards on all nodes in bytes | The total number of bytes occupied by segment metadata in memory for both primary and replica shards. |
| Indices: Doc values | Doc values with only primary shards on all nodes in bytes | The number of bytes of doc values columnar _ memory used for aggregations and sorting in primary shards. |
|   | Doc values with all shards on all nodes in bytes | The total number of bytes of memory occupied by doc values in both primary and replica shards. _ |
| Indices: Fields | Size of fields with only primary shards on all nodes in bytes | The number of bytes of memory occupied by field metadata (field names and types) in primary shards. |
|   | Size of fields with all shards on all nodes in bytes | The total number of bytes of memory occupied by field metadata in both primary and replica shards. |
| Indices: Fixed bit | Size of fixed bit with only primary shards on all nodes in bytes | The number of bytes of bitset memory used for the inverted index in primary shards. |
|   | Size of fixed bit with all shards on all nodes in bytes | The total number of bytes of memory occupied by bitset in both primary and replica shards. |

| Indices: Norms | Size of norms with only primary shards on all nodes in bytes | The number of bytes of memory occupied by field normalization factors (such as text length) in primary shards. |
|---|---|---|
|   | Size of norms with all shards on all nodes in bytes | The total number of bytes of memory occupied by normalization factors in both primary and replica shards. |
| Indices: Points | Size of points with only primary shards on all nodes in bytes | The number of bytes of memory (used for geographic and numeric fields) occupied by BKD trees in primary shards. |
|   | Size of points with all shards on all nodes in bytes | The number of bytes of memory (used for geographic and numeric fields) occupied by BKD trees in both primary and replica shards. |
| Indices: Terms | Size of terms with only primary shards on all nodes in bytes | The number of bytes of memory occupied by the inverted index dictionary (terms) in primary shards. |
|   | Number of terms with all shards on all nodes in bytes | The number of bytes of memory occupied by the inverted index dictionary (terms) in both primary and replica shards. |
| Indices: Version map | Size of version map with only primary shards on all nodes in bytes | The number of bytes of memory occupied by version maps used for optimistic locking in primary shards. |
|   | Size of version map with all shards on all nodes in bytes | The number of bytes of memory occupied by version maps used for optimistic locking in both primary and replica shards. |
| XDCR: synchronous stats | XDCR | The XDCR plug-in and switch status. |
|   | XDCR tasks number | The current number of indexes that are synchronized by XDCR. |
|   | xdcr synchronous rate for index | The number of documents successfully synchronized to the remote cluster per unit of time, calculated by index. |
|   | Unsynchronized document number for index | The number of unsynchronized documents between the local and remote clusters, calculated by index. |

| Note XDCR-related metrics are supported only in version |   |   |   |   |
|---|---|---|---|---|
|   | Note XDCR-related metrics are supported only in version |   | xdcr synchronous rate for shard | The number of documents successfully synchronized to the remote cluster per unit of time, calculated by shard. |
|   |   |   | Unsynchronized document number for shard | The number of unsynchronized documents between the local and remote clusters, calculated by shard. |
|   | 6.8.13 and are currently unsupported in version 7.10.0. |   |   |   |
| XDCR: local stats Note XDCR-related metrics are supported only in version 6.8.13 and are currently unsupported in version 7.10.0. |   |   | Local document number | The number of local documents. The total number of documents in the XDCR source cluster, calculated by index or repository. |
|   |   |   | Local seq number | The local sequence number. The latest operation sequence number in the XDCR source cluster, calculated by index or repository. |
|   |   |   | Local checkpoint | The local checkpoint. The safely persisted operation sequence number in the XDCR source cluster, calculated by index or repository. |
|   |   |   | Local global checkpoint | The local global checkpoint. The sequence number of the persisted operation agreed upon by all shards in the XDCR source cluster, calculated by index or repository. |
| XDCR: remote stats Note XDCR-related metrics are supported only in version 6.8.13 and are currently unsupported in version 7.10.0. |   |   | Remote document number | The number of remote documents. The total number of documents in the XDCR destination cluster, calculated by index or repository. |
|   |   |   | Remote seq number | The remote sequence. The latest operation sequence number in the XDCR destination cluster, calculated by index or repository. |
|   |   |   | Remote checkpoint | The remote checkpoint. The applied operation sequence number in the XDCR destination cluster, calculated by index or repository. |
|   |   |   | Remote global checkpoint | The remote global checkpoint. The applied operation sequence number agreed upon by all shards in the XDCR destination cluster, calculated by index or repository. |

**OpenSearch metrics**

| Category | Metric | Description |
|---|---|---|

| Cluster health status and key metrics | Cluster status | Displays the overall health status of the entire cluster. Green: indicates that all primary and replica shards are allocated, and the cluster is healthy. Yellow: indicates that all primary shards are allocated, but some replica shards are not allocated, posing risks of data loss. Red: indicates that some primary shards are not allocated, meaning data has been lost and the cluster is unavailable. |
|---|---|---|
|   | Pending tasks | Displays the number of cluster-level tasks that have not yet been executed, such as index creation and shard allocation. A continuously non-zero or increasing value indicates that the master node is under heavy load or issues block task execution. |
|   | Shard status | Provides an overview of the overall situation of cluster shards. Pay special attention to the number of "unallocated shards". A value greater than 0 means that some data may be inaccessible or that query performance has degraded. |
|   | Memory usage | Displays the physical memory (Resident Set Size) consumed by the JVM process on each node. This metric reflects the node's consumption of host memory resources. |
|   | Disk usage | Monitors the disk usage percentage of the data path on each node. Excessive disk usage (> 85%) will trigger shard migration and may even cause the entire node to enter read-only mode, severely impacting cluster stability. |
|   | CPU usage | Displays the CPU usage percentage of each node. Continuously high CPU usage indicates that the node is under significant computing pressure, which may be caused by complex queries, high-concurrency indexing operations, or background tasks. |
|   | File descriptor usage | Displays the file descriptor (FD) usage of each node. FD is a valuable resource for processing files and network connections. A high usage (close to 100%) indicates a severe resource bottleneck. |

|   | Circuit breaker triggers | Displays the total number of times circuit breakers have been triggered within the selected time range. Circuit breakers are designed to prevent JVM crashes caused by OOM errors. Any value greater than 0 indicates that the node has experienced memory pressure and requires vigilance. |
|---|---|---|
|   | Number of nodes | Displays the total number of nodes and the number of data nodes in the cluster. Data nodes are the core nodes that store data and execute indexing, searching, and other operations. |
|   | Total number of documents | Displays the total number of documents across all indexes on each node in the cluster, which reflects the scale of data stored. |
|   | Number of HTTP connections | Displays the cumulative total number of connections established with each node by using the HTTP protocol. A continuously increasing value reflects historical connection activity and does not directly indicate the current number of active connections. |
|   | Number of transport service connections | Displays the number of open connections for internal cluster communication (Transport service). An abnormally high number of connections may indicate communication issues between nodes or "split-brain" risks. |
|   | Number of open file descriptors | Displays the number of currently open file handles on each node. This is a critical OS resource metric. An excessively large value (approaching the system limit) will prevent the node from opening new files or accepting new connections, which results in service interruptions. |
|   | Circuit breaker usage | Displays the percentage of estimated memory used by the parent circuit breaker relative to its configured limit. A ratio exceeding 80% requires attention, indicating that memory requests are approaching the threshold, which may lead to request rejections or even circuit breaker triggering. |
|   | GC frequency | Displays the frequency of JVM GC events, grouped by node and GC type (old/young). Frequent GC, especially old GC, causes application pauses that severely impact query and indexing performance. |

| Resource usage and performance monitoring |   |   |
|---|---|---|
|   | Cache hit rate | Displays the hit rates for the query cache and request cache. A high hit rate (> 80%) indicates effective caching, which significantly improves query performance and reduces CPU load. A low hit rate suggests that query patterns do not efficiently use the cache or that the cache size is configured too small. |
|   | Indexing and query latency (key performance) | Displays the time taken for a single indexing operation and query operation. This is the most critical performance metric and directly impacts user experience. A sudden increase in latency is usually related to resource bottlenecks (CPU and disk I/O), unreasonable queries, or data skew. |
| Thread pool monitoring | Length of the queue in key thread pools | Displays the length of the task queue waiting for execution in critical thread pools, such as search and write. A continuously backlogged queue is a direct signal of high node load, which indicates that the request rate exceeds the processing rate. This may lead to request timeouts or rejections. |
|   | Number of active threads in key thread pools | Displays the number of active threads that are executing tasks in critical thread pools. When the number of active threads continuously reaches the maximum limit of the thread pool, it means the node's processing capacity has reached its upper limit, and new requests will have to wait in the queue. |
|   | Ratio of query time to fetch time | This ratio helps locate the source of query bottlenecks. If the ratio is significantly less than 1, it indicates that the time is primarily spent in the data fetching phase, possibly due to slow disk I/O or a low cache hit rate. If the ratio is close to 1 or greater than 1, it indicates that the time is primarily spent in the query and computation phase. This indicates inefficient queries or CPU bottlenecks. |
|   | Cache eviction rate | Displays the rate at which existing data in the fielddata and query caches is evicted due to insufficient space. Frequent evictions indicate insufficient cache space, preventing the cache from functioning effectively and increasing memory and CPU pressure. |

| Business errors and anomaly detection |   |   |
|---|---|---|
|   | Maximum task wait time | Displays the maximum time a cluster management task (such as shard allocation) has waited in a queue. A large or continuously increasing value indicates that the master node is overloaded or cluster-level issues block the execution of background tasks. |
|   | Write failure rate | Displays the rate (in times per second) at which documents fail to be indexed due to various reasons (such as mapping errors or full disk). Any value greater than 0 indicates a risk of data loss and requires immediate investigation. |
|   | Scroll query rate | Displays the initiation rate of scroll queries. Scroll queries are suitable for large-scale data pagination but consume node memory. High concurrency or long-running scroll queries are common performance killers. |
|   | Number of documents processes in ingest | Displays the number of documents currently being processed in the ingest pipeline. Ingest processing consumes CPU and memory. A continuously large value indicates heavy preprocessing pressure. |
|   | Document indexing rate | Displays the number of documents successfully indexed per second. This metric reflects the write throughput of a cluster and is key to evaluating its write capacity. |
|   | Indexing latency | Displays the average time taken for a single document indexing operation. Increased latency is usually related to resource bottlenecks (such as CPU and disk I/O), complex ingest pipelines, or an excessive number of shards. |
|   | Search rate | Displays the number of queries executed per second. This metric reflects the query load and throughput of a cluster. |
|   | Average query latency | Displays the average time taken for a single query operation, which is the most critical metric for measuring query performance. High latency is typically caused by slow queries, data skew, or resource bottlenecks, directly impacting user experience. |

| Indexing and search performance analysis |   |   |
|---|---|---|
|   | Document deletion rate | Displays the total number of pending deleted documents across all indexes on each node in a cluster. A sudden increase in this value is usually related to massive deletion operations. The space occupied by these documents will be reclaimed during segment merging. |
|   | Number of open search contexts | Reflects how many long-running queries (such as deep pagination and large aggregations) are currently active. A high large indicates that a large number of potential slow queries are consuming node memory, which may lead to OOM errors. |
|   | Index throttling time ratio | Displays the proportion of the time indexing operations spend waiting due to throttling relative to the total time. A large value indicates that node I/O or CPU resources are insufficient. The system actively limits writes to ensure stability, which reduces indexing throughput. |
|   | Merge throttling time ratio | Displays the proportion of the time segment merge operations spend waiting due to throttling relative to the total time. A large value indicates that background merge operations are causing immense I/O pressure. The system actively limits merging to prevent it from affecting frontend read/write performance. |
|   | Document merge rate | Displays the number of documents merged per second during a segment merging process. This metric reflects the intensity of background merge activities. A continuously high rate consumes significant I/O and CPU resources. |
|   | Fielddata memory size | Displays the size of JVM heap memory occupied by fielddata used for operations such as sorting and aggregations. This memory is uncontrollable and can easily spike due to improper queries, making it a primary contributor to OOM errors. |
|   | Query cache size | Displays the size of JVM heap memory occupied by the query cache. Monitoring its size helps evaluate cache configuration and prevents it from expanding excessively and squeezing out memory required by other business operations. |

| Cache and memory monitoring |   |   |
|---|---|---|
|   | Segment memory usage | Displays the total memory occupied by all index segments. Small, fragmented segments significantly increase memory overhead. Periodic forced merges can optimize segment memory usage. |
|   | Number of times fielddata being evicted | Displays the rate at which old data is evicted from the fielddata cache due to insufficient memory. Frequent evictions represent a massive waste of performance, indicating that the fielddata cache is configured too small or there are severe issues with the queries. |
|   | Query cache statistics | Comprehensively displays the hit rate, miss rate, and eviction status of the query cache to evaluate its effectiveness and pressure. |
|   | Number of segments | Displays the total number of Lucene segments across all indexes on the node. An excessive number of segments consumes a large amount of memory and file handles, and degrades query performance. Too many segments usually need to be optimized through forced merging. |
| JVM monitoring | Heap memory usage | Displays the percentage of heap memory occupied by JVMs. This is the most critical memory metric. A continuous usage above 85% will trigger frequent GC and may even lead to OOM errors. Healthy heap memory usage should form a healthy sawtooth curve, rising in a wave-like pattern before being reclaimed by GC. |
|   | Non-heap memory usage | Displays the percentage of non-heap memory (such as thread stacks, code cache, and class metadata) used by JVMs. A continuous increase in non-heap memory is usually related to class loading or thread creation issues. Although rare, it is difficult to troubleshoot when it occurs. |
|   | GC frequency | Displays the number of JVM GC events per second, grouped by node and GC type (old/young). Frequent GC, especially old GC, causes application pauses that severely impact query and indexing performance. |
|   | Average GC duration | Displays the average time taken for a single GC operation. Excessively long GC durations cause prolonged "Stop-The-World" application pauses, making users noticeably feel service stutters. |

|   | JVM memory usage in the old generation | Specifically monitors the usage of JVM memory pools in the old generation. The JVM memory pools in the old generation store long-lifecycle objects. A continuously increasing usage indicates a memory leak or insufficient heap memory configuration. This serves as the final warning before OOM. |
|---|---|---|
|   | Disk I/O rate | Displays the byte rate of disk reads and writes on each node. High write I/O is usually related to indexing and merging, while high read I/O is related to queries. I/O capability is the primary performance bottleneck in disk-bound scenarios. |
|   | Disk I/O operation rate | Displays the operation rate of disk reads and writes on each node. Combined with the byte rate, this metric helps determine whether the I/O pattern is random or sequential. |
| Disk I/O and network transmission monitoring |   |   |
|   | Inter-node network I/O | Displays the network traffic for internal communication between cluster nodes. Queries and data replication (such as replica synchronization and shard migration) generate internal network traffic. |
|   | Inter-node packet rate | Displays the network packet rate for internal communication between cluster nodes. Under the same traffic volume, a greater number of packets indicates greater network overhead and lower efficiency. |
|   | Transaction log size | Displays the total size of transaction logs for all shards on each node. The transaction log (Translog) ensures data is not lost, but an excessively large Translog will consume significant time during recovery. Its size is usually positively correlated with the indexing rate. |
|   | Number of uncommitted operations for transaction logs | Displays the number of operations that have not yet been flushed from transaction logs to disk segment files. A continuously increasing value indicates high refresh pressure and will increase data recovery time in the event of a node failure. |

|   | The current number of refresh listeners. | This metric indicates how many queries are waiting for the index refresh to complete. If this value remains high, it indicates heavy indexing pressure, where new data cannot become visible in a timely manner and query requests may be blocked, severely impacting real-time performance. |
|---|---|---|
|   | The current number of active merge tasks. | Merging is one of the most I/O and CPU- intensive background operations. Monitoring the number of active merges helps determine whether the node is currently under significant pressure from background maintenance, which will directly affect frontend request latency. |

For more information about how to customize a dashboard, go to **General O&M >**

**Monitoring management > Cloud platform monitoring > Data dashboard >**

**Custom dashboard** in **Apsara Uni-manager Operations Console User Guide** .

### 4.4 Use Cloud Monitor to view the metrics of an Elasticsearch cluster

**metrics of an Elasticsearch cluster**

This topic describes how to use Cloud Monitor to view the metrics of an Elasticsearch cluster, including the metrics for cluster monitoring, node monitoring, and index monitoring. This helps you understand the running status of a cluster in real time and handle potential risks.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Products**.
3. In the **Migration and O&M Management** section, click **Cloud Monitor**.
4. Use either of the following methods to view the metrics of an Elasticsearch cluster:
**Method 1**: Use **Cloud Monitor**
a. In the left-side navigation pane, choose **Cloud Resource Monitoring > Cloud**
**Service Monitoring**.
b. On the **Cloud Service Monitoring** page, choose **Big data (number plus) >**
**Elasticsearch on k8s**. Alternatively, search for **Elasticsearch on k8s** in the cloud
service search box and then click the desired service. c. In the **Instance ID** list, click the ID of the cluster that you want to manage. The **APP**
**monitor** tab is displayed.
d. On the **APP monitor**, **Node monitoring**, and **Table monitoring** tabs, view metrics for the corresponding categories. For more information about metrics, see Metrics for cloud service monitoring.
**Method 2**: View the data in a **metric warehouse**
a. In the left-side navigation pane, choose **Cloud Resource Monitoring > Namespace**. b. On the **Time series indicator** tab, search for **Elasticsearch on k8s** in the search box in the **List of cloud products** section. c. In the right-side section, you can view the metrics of the cloud service. For more information about metrics, see Metrics for namespaces.

**Metrics**

The metrics for cloud service monitoring are the same as those for namespaces. They differ only in their presentation formats.

**Metrics for cloud service monitoring**

**Instance monitoring**

| Metric name | Metric name | Metric dimension | Metric aggregation value | Unit | Minimum aggregati on period |
|---|---|---|---|---|---|
| ClusterStatus | ClusterStatus | instanceId | Value,Maximu m | short | 60 |
| PendingTaskCount | PendingTaskCo unt | instanceId | Maximum,Valu e | short | 60 |
| PendingTaskMaxW aitTime | PendingTaskMa xWaitTime | instanceId | Maximum,Valu e | millisecond s | 60 |
| DataNodes | DataNodes | instanceId | Value | short | 60 |
| ActiveShards | ActiveShards | instanceId | Value | short | 60 |
| NodeActiveShards | NodeActiveShar ds | instanceId | Value | short | 60 |
| UnassignedShards | UnassignedShar dshards | instanceId | Value | short | 60 |

**Node monitoring**

| Metric name | Metric name | Metric dimension | Metric aggregation value | Unit | Minimum aggregat ion period |
|---|---|---|---|---|---|

| NodeCPUUtil | NodeCPUUtil | instanceId,no deName | Maximum,Avera ge | percen t | 60 |
|---|---|---|---|---|---|
| NodeDiskUtil | NodeDiskUtil | instanceId,no deName | Maximum,Avera ge | percen t | 60 |
| NodeHeapMemoryU til | NodeHeapMe moryUtil | instanceId,no deName | Maximum,Avera ge | percen t | 60 |
| NodeLoad1 | NodeLoad1 | instanceId,no deName | Maximum,Avera ge | short | 60 |
| NodeLoad5 | NodeLoad5 | instanceId,no deName | Maximum,Avera ge | short | 60 |
| NodeLoad15 | NodeLoad15 | instanceId,no deName | Maximum,Avera ge | short | 60 |
| OldGCTotalCount | OldGCTotalCo unt | instanceId,no deName | Value | short | 60 |
| YoungGCTotalCount | YoungGCTotal Count | instanceId,no deName | Value | short | 60 |
| OldGCTotalTime | OldGCTotalTim e | instanceId,no deName | Value | s | 60 |
| YoungGCTotalTime | YoungGCTotal Time | instanceId,no deName | Value | s | 60 |
| OldGCCostTime | OldGCCostTim e | instanceId,no deName | Maximum,Avera ge | millisec onds | 60 |
| YoungGCCostTime | YoungGCCostT ime | instanceId,no deName | Maximum,Avera ge | millisec onds | 60 |
| OldGCRate | OldGCRate | instanceId,no deName | Maximum,Avera ge | ops | 60 |
| YoungGCRate | YoungGCRate | instanceId,no deName | Maximum,Avera ge | ops | 60 |
| AvailableDiskSize | AvailableDiskS ize | instanceId,no deName | Maximum,Avera ge | gbytes | 60 |

| NodeHeapMemory | NodeHeapMe mory | instanceId,no deName | Maximum,Avera ge | gbytes | 60 |
|---|---|---|---|---|---|
| NodeDocumentCoun t | NodeDocumen tCount | instanceId,no deName | Maximum,Avera ge | short | 60 |
| NodeSegmentCount | NodeSegment Count | instanceId,no deName | Maximum,Avera ge | short | 60 |
| NodeDiskIOOperatio nsRate | NodeDiskIOOp erationsRate | instanceId,no deName | Maximum,Avera ge | ops | 60 |
| NodeWriteIOOperati onsRate | NodeWriteIOO perationsRate | instanceId,no deName | aximum,Averag e,Value | ops | 60 |
| NodeReadIOOperati onsRate | NodeReadIOO perationsRate | instanceId,no deName | Maximum,Avera ge,Value | ops | 60 |
| IndexThread | IndexThread | instanceId,no deName | Maximum,Avera ge,Value | short | 60 |
| WriteThread | WriteThread | instanceId,no deName | Maximum,Avera ge,Value | short | 60 |
| NodeData | NodeData | instanceId,no deName | Maximum,Avera ge | mbytes | 60 |
| NodeIndexMemoryL ucene | NodeIndexMe moryLucene | instanceId,no deName | Maximum,Avera ge | kbytes | 60 |
| NodeIndexMemoryT erms | NodeIndexMe moryTerms | instanceId,no deName | Maximum,Avera ge | kbytes | 60 |
| NodeIndexMemoryP oints | NodeIndexMe moryPoints | instanceId,no deName | Maximum,Avera ge | kbytes | 60 |
| NodeIndexingLatenc y | NodeIndexingL atency | instanceId,no deName | Maximum,Avera ge,Value | millisec onds | 60 |
| NodeSearchLatency | NodeSearchLa tency | instanceId,no deName | Maximum,Avera ge,Value | millisec onds | 60 |

| IndexThreadQueue | IndexThreadQ ueue | instanceId,no deName | Maximum,Avera ge,Value | short | 60 |
|---|---|---|---|---|---|
| IndexThreadRejecte d | IndexThreadR ejected | instanceId,no deName | Maximum,Avera ge,Value | short | 60 |
| WriteThreadQueue | WriteThreadQ ueue | instanceId,no deName | Maximum,Avera ge,Value | short | 60 |
| WriteThreadRejecte d | WriteThreadRe jected | instanceId,no deName | Maximum,Avera ge,Value | short | 60 |

**Table monitoring**

| Metric name | Metric name | Metric dimension | Metric aggregation value | Unit | Minimum aggregati on period |
|---|---|---|---|---|---|
| IndexRate | IndexRate | instanceId,inde xName | Maximum,Avera ge | ops | 60 |
| SearchRate | SearchRate | instanceId,inde xName | Maximum,Avera ge | ops | 60 |
| AvgIndexTim e | AvgIndexTime | instanceId,inde xName | Maximum,Avera ge | milliseco nds | 60 |
| AvgSearchTi me | AvgSearchTime | instanceId,inde xName | Maximum,Avera ge | milliseco nds | 60 |
| IndexDocume ntCount | IndexDocument Count | instanceId,inde xName | Maximum,Avera ge,Value | short | 60 |
| IndexSegmen tAllShard | IndexSegmentAll Shard | instanceId,inde xName | Maximum,Avera ge,Value | short | 60 |
| IndexSegmen tPrimaries | IndexSegmentPri maries | instanceId,inde xName | Maximum,Avera ge,Value | short | 60 |
| FielddataMem oryBytesTotal | FielddataMemor yBytesTotal | instanceId,inde xName | Maximum,Avera ge,Value | bytes | 60 |
| IndexMemory Terms | IndexMemoryTer ms | instanceId,inde xName | Maximum,Avera ge,Value | bytes | 60 |

| IndexMemory Points | IndexMemoryPoi nts | instanceId,inde xName | Maximum,Avera ge,Value | bytes | 60 |
|---|---|---|---|---|---|
| IndexDisk | IndexDisk | instanceId,inde xName | Maximum,Avera ge,Value | bytes | 60 |
| IndexDiskPri maries | IndexDiskPrimari es | instanceId,inde xName | Maximum,Avera ge,Value | bytes | 60 |

**Metrics for namespaces**

| Metric name | Associat ed service | Metric name | Metric dimensio n | Metric aggregati on value | Unit | Minimu m aggrega tion period |
|---|---|---|---|---|---|---|
| NodeActiveSha rds | Elasticsea rchK8s | NodeActiveSh ards | instanceId | Value | short | 60 |
| ClusterStatus | Elasticsea rchK8s | ClusterStatus | instanceId | Value,Maxi mum | short | 60 |
| PendingTaskCo unt | Elasticsea rchK8s | PendingTaskC ount | instanceId | Maximum,V alue | short | 60 |
| PendingTaskM axWaitTime | Elasticsea rchK8s | PendingTaskM axWaitTime | instanceId | Maximum,V alue | millisec onds | 60 |
| NodeCPUUti | Elasticsea rchK8s | NodeCPUUtil | instanceId, nodeName | Maximum,A verage | percent | 60 |
| NodeDiskUtil | Elasticsea rchK8s | NodeDiskUtil | instanceId, nodeName | Maximum,A verage | percent | 60 |
| NodeHeapMem oryUtil | Elasticsea rchK8s | NodeHeapMe moryUtil | instanceId, nodeName | Maximum,A verage | percent | 60 |
| NodeLoad1 | Elasticsea rchK8s | NodeLoad1 | instanceId, nodeName | Maximum,A verage | short | 60 |
| NodeLoad5 | Elasticsea rchK8s | NodeLoad5 | instanceId, nodeName | Maximum,A verage | short | 60 |

| NodeLoad15 | Elasticsea rchK8s | NodeLoad15 | instanceId, nodeName | Maximum,A verage | short | 60 |
|---|---|---|---|---|---|---|
| OldGCTotalCou nt | Elasticsea rchK8s | OldGCTotalCo unt | instanceId, nodeName | Value | short | 60 |
| YoungGCTotalC ount | Elasticsea rchK8s | YoungGCTotal Count | instanceId, nodeName | Value | short | 60 |
| OldGCTotalTim e | Elasticsea rchK8s | OldGCTotalTi me | instanceId, nodeName | Value | s | 60 |
| YoungGCTotalT ime | Elasticsea rchK8s | YoungGCTotal Time | instanceId, nodeName | Value | s | 60 |
| YoungGCRate | Elasticsea rchK8s | YoungGCRate | instanceId, nodeName | Maximum,A verage | ops | 60 |
| OldGCRate | Elasticsea rchK8s | OldGCRate | instanceId, nodeName | Maximum,A verage | ops | 60 |
| YoungGCCostTi me | Elasticsea rchK8s | YoungGCCost Time | instanceId, nodeName | Maximum,A verage | millisec onds | 60 |
| OldGCCostTim e | Elasticsea rchK8s | OldGCCostTim e | instanceId, nodeName | Maximum,A verage | millisec onds | 60 |
| IndexRate | Elasticsea rchK8s | IndexRate | instanceId, indexNam e | Maximum,A verage | ops | 60 |
| AvgIndexTime | Elasticsea rchK8s | AvgIndexTime | instanceId, indexNam e | Maximum,A verage | millisec onds | 60 |
| SearchRate | Elasticsea rchK8s | SearchRate | instanceId, indexNam e | Maximum,A verage | ops | 60 |
| AvgSearchTim e | Elasticsea rchK8s | AvgSearchTim e | instanceId, indexNam e | Maximum,A verage | millisec onds | 60 |
| DataNodes | Elasticsea rchK8s | DataNodes | instanceId | Value | short | 60 |

| ActiveShards | Elasticsea rchK8s | ActiveShards | instanceId | Value | short | 60 |
|---|---|---|---|---|---|---|
| UnassingnedSh ards | Elasticsea rchK8s | UnassignedSh ards | instanceId | Value | short | 60 |
| AvailableDiskSi ze | Elasticsea rchK8s | AvailableDisk Size | instanceId, nodeName | Maximum,A verage | gbytes | 60 |
| NodeHeapMem ory | Elasticsea rchK8s | NodeHeapMe mory | instanceId, nodeName | Maximum,A verage | gbytes | 60 |
| NodeDocument Count | Elasticsea rchK8s | NodeDocume ntCount | instanceId, nodeName | Maximum,A verage | short | 60 |
| NodeSegmentC ount | Elasticsea rchK8s | NodeSegment Count | instanceId, nodeName | Maximum,A verage | short | 60 |
| NodeDiskIOOp erationsRate | Elasticsea rchK8s | NodeDiskIOOp erationsRate | instanceId, nodeName | Maximum,A verage | ops | 60 |
| NodeWriteIOOp erationsRate | Elasticsea rchK8s | NodeWriteIOO perationsRate | instanceId, nodeName | Maximum,A verage,Valu e | ops | 60 |
| NodeReadIOOp erationsRate | Elasticsea rchK8s | NodeReadIOO perationsRate | instanceId, nodeName | Maximum,A verage,Valu e | ops | 60 |
| IndexThread | Elasticsea rchK8s | IndexThread | instanceId, nodeName | Maximum,A verage,Valu e | short | 60 |
| WriteThread | Elasticsea rchK8s | WriteThread | instanceId, nodeName | Maximum,A verage,Valu e | short | 60 |
| NodeData | Elasticsea rchK8s | NodeData | instanceId, nodeName | Maximum,A verage | mbytes | 60 |
| NodeIndexMe moryLucene | Elasticsea rchK8s | NodeIndexMe moryLucene | instanceId, nodeName | Maximum,A verage | kbytes | 60 |

| NodeIndexMe moryTerms | Elasticsea rchK8s | NodeIndexMe moryTerms | instanceId, nodeName | Maximum,A verage | kbytes | 60 |
|---|---|---|---|---|---|---|
| NodeIndexMe moryPoints | Elasticsea rchK8s | NodeIndexMe moryPoints | instanceId, nodeName | Maximum,A verage | kbytes | 60 |
| NodeSearchLat ency | Elasticsea rchK8s | NodeSearchLa tency | instanceId, nodeName | Maximum,A verage,Valu e | millisec onds | 60 |
| NodeIndexingL atency | Elasticsea rchK8s | NodeIndexing Latency | instanceId, nodeName | Maximum,A verage,Valu e | millisec onds | 60 |
| IndexDocumm entCount | Elasticsea rchK8s | IndexDocume ntCount | instanceId, indexNam e | Maximum,A verage,Valu e | short | 60 |
| IndexSegment AllShard | Elasticsea rchK8s | IndexSegment AllShard | instanceId, indexNam e | Maximum,A verage,Valu e | short | 60 |
| IndexSegment Primaries | Elasticsea rchK8s | IndexSegment Primaries | instanceId, indexNam e | Maximum,A verage,Valu e | short | 60 |
| FielddataMemo ryBytesTotal | Elasticsea rchK8s | FielddataMem oryBytesTotal | instanceId, indexNam e | Maximum,A verage,Valu e | bytes | 60 |
| IndexMemoryT erms | Elasticsea rchK8s | IndexMemory Terms | instanceId, indexNam e | Maximum,A verage,Valu e | bytes | 60 |
| IndexMemoryP oints | Elasticsea rchK8s | IndexMemory Points | instanceId, indexNam e | Maximum,A verage,Valu e | bytes | 60 |
| IndexDisk | Elasticsea rchK8s | IndexDisk | instanceId, indexNam e | Maximum,A verage,Valu e | bytes | 60 |
| IndexDiskPrima ries | Elasticsea rchK8s | IndexDiskPrim aries | instanceId, indexNam e | Maximum,A verage,Valu e | bytes | 60 |

| IndexThreadQu eue | Elasticsea rchK8s | IndexThreadQ ueue | instanceId, nodeName | Maximum,A verage,Valu e | short | 60 |
|---|---|---|---|---|---|---|
| IndexThreadRe jected | Elasticsea rchK8s | IndexThreadR ejected | instanceId, nodeName | Maximum,A verage,Valu e | short | 60 |
| WriteThreadQu eue | Elasticsea rchK8s | WriteThreadQ ueue | instanceId, nodeName | Maximum,A verage,Valu e | short | 60 |
| WriteThreadRej ected | Elasticsea rchK8s | WriteThreadR ejected | instanceId, nodeName | Maximum,A verage,Valu e | short | 60 |

### 4.5 Use Grafana to view metrics of Elasticsearch clusters

**Elasticsearch clusters**

This topic describes how to view the metrics of Elasticsearch clusters on the Grafana dashboard.

**Procedure**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Kubernetes Cluster Management**. By default, the **Kubernetes**
**Cluster Overview** page appears.
3. In the **Nodes** section, find a node and click **Node Performance Data** in the **Actions**
column. The **Kubernetes / Nodes** page appears.
4. In the left-side navigation pane, click the
icon, enter **Elasticsearch** in the search field and click **ElasticSearch** in the search results.
5. On the **ElasticSearch** dashboard page, select a cluster from the **Cluster** drop-down list to
view the metrics of the cluster. The ElasticSearch metrics are described as follows. The metrics displayed in the console shall prevail.

| Category | Metric | Description |
|---|---|---|
|   | Cluster health | The cluster health status. The overall availability is identified by colors: green (all shards are properly allocated), yellow (replica shards are unallocated, posing risks), and red (primary shards are unallocated, indicating data loss). |

| erations and Maintena Logging and monitorin |   |   |
|---|---|---|
| Cluster |   |   |
|   | Node state | The node role status, which distinguishes the role types such as data nodes and coordinating nodes and their distribution. |
|   | Data state max | The maximum resource usage on data nodes. This metric monitors the peak utilization of CPU, Java Virtual Machine (JVM) heap memory, and disk space on data nodes. |
|   | Coordinating state max | The maximum resource usage on coordinating nodes. This metric monitors the peak load of CPU and JVM heap memory on coordinating nodes (non- data/ingest nodes). |
|   | Index State | The core status metric for indexes. This metric includes the memory occupied by document values, the number of segments, and the total number of documents, reflecting the health of the underlying index structure. |
|   | Pending tasks | The pending cluster tasks. This metric displays cluster-level operations awaiting execution, such as index creation and shard allocation. A continuously non-zero or increasing value indicates primary node overload or task blocking. |
|   | Tripped for breakers | The circuit breaker trigger statistics. This metric measures the number of requests rejected due to memory overload. A value greater than 0 indicates excessive memory pressure on the node. |
|   | Open file descriptors per cluster | The total number of cluster file descriptors. This metric reflects the total number of open file handles across all nodes. An excessively large value may lead to system resource exhaustion. |
|   | Active shards | The total number of active shards, which is the sum of primary and replica shards in the cluster that are currently in service. |
|   | Active primary shards | The number of active primary shards, which indicates the number of primary shards in the cluster currently available for write operations. |
|   | Shard per node | This metric realizes load balance of shards between nodes by calculating the average number of primary shards on each data node. An excessively large value may lead to hot issues. |

| Shards |   |   |
|---|---|---|
|   | Unassigned shards | The number of shards that have not been successfully allocated to any node. A value greater than 0 indicates inaccessible data or degraded query performance. |
|   | Initializing shards | The number of shards being initialized, which indicates the number of shards in the restoration or creation process. A continuously large value indicates slow cluster recovery. |
|   | Relocating shards | The number of shards being relocated, which indicates the number of shards that are migrating between nodes. This metric reflects the intensity of cluster load balancing. |
|   | Delayed shards | The number of shards whose allocation is delayed due to timeout or unmet conditions. |
| Nodes & Indices | Nodes stats | The real-time node resource status. This metric displays node-level metrics of CPU, JVM memory, disk space, and system load, as well as the index storage volume and the total number of documents and segments. |
|   | Index stats | The core performance metrics of indexes. This metric includes key statistics such as the number of shards and replicas, the total number of documents, storage volume, active queries, and segment memory. |
| JVM Garbage Collection | Young GC count | The rate of young garbage collection (GC), which indicates the frequency of JVM young GC triggers per unit of time. A high frequency may indicate excessively fast object creation. |
|   | Old GC count | The rate of old GC, which indicates the frequency of JVM old GC triggers per unit of time. A high frequency may indicate memory leaks or insufficient heap configuration. |
|   | Young GC time | The time consumed by JVM young GC per unit of time on CPU. This metric affects write and query latency. |
|   | Old GC time | The time consumed by JVM old GC per unit of time on CPU. Prolonged pauses can cause service stutters. |

| Translog | Total translog operations | The rate of change in total transaction log operations, which indicates the number of operations written to the transaction log per unit of time. This metric reflects the intensity of the write load. |
|---|---|---|
|   | Total translog size in bytes | The change rate of the transaction log size, which indicates the number of bytes increased in the transaction log per unit of time. An excessively large size may impact the recovery speed. |
| Breakers | Tripped for breakers | The circuit breaker trigger statistics. This metric measures the number of requests rejected due to memory overload. A value greater than 0 indicates excessive memory pressure on the node. |
|   | Estimated size in bytes of breaker | The estimated number of memory bytes for circuit breakers. This system compares the estimated number of memory bytes of the current request against the circuit breaker threshold to prevent Out-of-Memory (OOM) errors. |
| CPU and Memory | CPU usage | The node CPU usage, which indicates the percentage of CPU resource consumption at the operating system level. |
|   | Young - JVM heap memory used | The amount of JVM heap memory used in the young generation (Eden/Survivor spaces). |
|   | Load1 average | The average CPU load of the node over the last one minute, which reflects short-term pressure. |
|   | Old - JVM heap memory used | The amount of JVM heap memory used in the old generation. A continuous increase may indicate memory leaks. |
|   | Load5 average | The average CPU load of the node over the last five minutes. This metric reflects medium-term pressure trends. |
|   | JVM non-heap memory usage | The percentage of non-heap memory (such as Metaspace and thread stacks) occupied by JVMs. |
|   | Load15 average | The average CPU load of the node over the last 15 minutes, which reflects long-term pressure trends. |

|   | JVM peak memory usage | The highest historical JVM memory usage in bytes, used for capacity planning. |
|---|---|---|
|   | JVM heap memory used | The percentage of heap memory occupied by JVMs relative to the maximum heap memory. Exercise caution if the value exceeds 75%. |
|   | Disk IO throughput | The amount of data read from and written to the disk per unit of time (in KB/s), which reflects storage performance bottlenecks. |
|   | Total Disk Operations rate | The total IOPS (including the number of read and write operations) of a disk per unit of time. A large value may impact query latency. |
|   | Disk usage size | The number of disk bytes occupied by the Elasticsearch data directory on the node. |
| Disk and Network |   |   |
|   | Network usage sent | The number of data bytes transmitted outbound (such as shard recovery and replica synchronization) from the node per unit of time. |
|   | Disk usage | The percentage of used space in the data directory against the total space. If the value exceeds 85%, capacity expansion is required. |
|   | Network usage received | The number of data bytes received (during client writes, cross-node queries, and other operations) by the node per unit of time. |
| Documents | Documents count on node | The total number of index documents hosted on the current node, which reflects the balance of data distribution. |
|   | Documents indexed rate | The number of successfully written documents per unit of time, which serves as a core write performance metric. |
|   | Documents deleted rate | The number of documents deleted per unit of time. A high frequency may impact segment merging efficiency. |
|   | Documents merged rate | The number of documents processed by segment merge operations per unit of time, which reflects the background optimization load. |
| Document Version: 20 | 260629 9 |   |

|   | Documents merged bytes | The number of data bytes processed by segment merge operations per unit of time. A large value consumes significant I/O resources. |
|---|---|---|
|   | Node indexing operations rate | The number of indexing requests processed by a single node per unit of time. |
| Total Operations and time | Node indexing operations time | The average time (in seconds) taken by a single node to process a single indexing request, which affects write latency. |
|   | Node query operations rate | The number of query requests processed by a single node per unit of time. |
|   | Node query operations time | The average time (in seconds) taken by a single node to process a single query request, which directly impacts user experience. |
|   | Index indexing operations rate | The number of indexing requests processed by a single index per unit of time. |
|   | Index Indexing operations time | The average time (in seconds) taken by a single index to process a single indexing request. |
|   | Index query operations rate | The number of query requests processed by a single index per unit of time. |
|   | Index query operations time | The average time (in seconds) taken by a single index to process a single query request. |
|   | Merging time | The total time (in seconds) consumed by segment merge operations per unit of time. A large value will slow down write performance. |
|   | Throttle time for index store | The cumulative wait time of operations throttled due to disk I/O overload, which reflects storage bottlenecks. |
|   | Other Operations rate | The request frequency statistics for operations including get, refresh, and flush. |
|   | Other operations time | The average processing time per operation for operations including get, refresh, and flush. |

| Thread Pool | Write threads active | The number of active threads that process index and delete requests. A continuously large value indicates heavy write pressure. |
|---|---|---|
|   | Write thread queued | The number of pending index and delete requests queued for processing. |
|   | Write thread rejected | The number of write requests rejected due to a full queue or insufficient resources. |
|   | Search threads active | The number of active threads that process search requests. A large value indicates heavy query load. |
|   | Search thread queued | The number of pending search requests queued for processing. |
|   | Search thread rejected | The number of search requests rejected due to a full queue or insufficient resources. |
|   | Thread Pool others threads active | The number of active threads that process non- write and non-query operations, such as merges and snapshots. |
|   | Thread Pool others operations queued | The number of pending non-write and non-query requests queued for processing. |
|   | Thread Pool others operations rejected | The number of non-write and non-query requests rejected by thread pools. |
|   | Thread Pool operations completed | The total number of requests successfully processed by all thread pools per unit of time. |
| Caches | Field data memory size | The number of bytes occupied by the fielddata cache used for aggregations and sorting. |
|   | Field data evictions | The number of times the fielddata cache is forcibly cleared due to insufficient memory. High-frequency cleanups lead to performance degradation. |
|   | Query cache size | The number of bytes of memory occupied by cached query results. |
|   | Query cache evictions | The rate at which cache entries are evicted due to insufficient space, which impacts repeated query performance. |
| Document Version: 20 | 260629 9 |   |

|   | Evictions from filter cache | The number of times filter caches are evicted due to memory pressure, which impacts range query performance. |
|---|---|---|
| Segments | Count of index segments | The total number of Lucene segments in the current index. An excessive number of segments reduces query efficiency. |
|   | Current memory size of segments in bytes | The number of bytes of metadata cached in memory for all index segments (excluding document data). |
| Indices: Count of documents and Total size | Count of documents with only primary shards | The total number of documents hosted across all primary shards (excluding replicas), which reflects the effective data volume. |
|   | Total size of stored index data in bytes with only primary shards on all nodes | The total number of raw data bytes of primary shards across all nodes (excluding replicas), which is used for capacity planning. |
|   | Total size of stored index data in bytes with all shards on all nodes | The total number of data bytes of both primary and replica shards across all nodes, which reflects the actual disk usage. |
| Indices: Index writer | Index writer with only primary shards on all nodes in bytes | The number of bytes of documents temporarily stored in memory and pending refresh for primary shards. |
|   | Index writer with all shards on all nodes in bytes | The number of bytes of documents temporarily stored in memory and pending refresh for both primary and replica shards. |
| Indices: Segments | Segments with only primary shards on all nodes | The total number of Lucene segments contained across all primary shards. |
|   | Segments with all shards on all nodes | The total number of Lucene segments across all primary and replica shards (as replicas are stored independently). |
|   | Size of segments with only primary shards on all nodes in bytes | The total number of bytes occupied by segment metadata in memory for primary shards. |
|   | Size of segments with all shards on all nodes in bytes | The total number of bytes occupied by segment metadata in memory for both primary and replica shards. |
|   | > Document Version: 2026062 |   |

|   |   | Operations and Maintenance Gu de·Logging and monitorin |
|---|---|---|
|   | Doc values with only primary shards on all nodes in bytes | The number of bytes of doc values columnar _ memory used for aggregations and sorting in primary shards. |
| Indices: Doc values |   |   |
|   | Doc values with all shards on all nodes in bytes | The total number of bytes of memory occupied by doc values in both primary and replica shards. _ |
| Indices: Fields | Size of fields with only primary shards on all nodes in bytes | The number of bytes of memory occupied by field metadata (field names and types) in primary shards. |
|   | Size of fields with all shards on all nodes in bytes | The total number of bytes of memory occupied by field metadata in both primary and replica shards. |
| Indices: Fixed bit | Size of fixed bit with only primary shards on all nodes in bytes | The number of bytes of bitset memory used for the inverted index in primary shards. |
|   | Size of fixed bit with all shards on all nodes in bytes | The total number of bytes of memory occupied by bitset in both primary and replica shards. |
| Indices: Norms | Size of norms with only primary shards on all nodes in bytes | The number of bytes of memory occupied by field normalization factors (such as text length) in primary shards. |
|   | Size of norms with all shards on all nodes in bytes | The total number of bytes of memory occupied by normalization factors in both primary and replica shards. |
| Indices: Points | Size of points with only primary shards on all nodes in bytes | The number of bytes of memory (used for geographic and numeric fields) occupied by BKD trees in primary shards. |
|   | Size of points with all shards on all nodes in bytes | The number of bytes of memory (used for geographic and numeric fields) occupied by BKD trees in both primary and replica shards. |
| Indices: Terms | Size of terms with only primary shards on all nodes in bytes | The number of bytes of memory occupied by the inverted index dictionary (terms) in primary shards. |
| Document Version: 20 | 260629 9 |   |

| erations and Maintena Logging and monitorin | nce Gui Elasticsearc g |   |
|---|---|---|
|   | Number of terms with all shards on all nodes in bytes | The number of bytes of memory occupied by the inverted index dictionary (terms) in both primary and replica shards. |
| Indices: Version map | Size of version map with only primary shards on all nodes in bytes | The number of bytes of memory occupied by version maps used for optimistic locking in primary shards. |
|   | Size of version map with all shards on all nodes in bytes | The number of bytes of memory occupied by version maps used for optimistic locking in both primary and replica shards. |
| XDCR: synchronous stats Note XDCR-related metrics are supported only in version 6.8.13 and are currently unsupported in version 7.10.0. | XDCR | The XDCR plug-in and switch status. |
|   | XDCR tasks number | The current number of indexes that are synchronized by XDCR. |
|   | xdcr synchronous rate for index | The number of documents successfully synchronized to the remote cluster per unit of time, calculated by index. |
|   | Unsynchronized document number for index | The number of unsynchronized documents between the local and remote clusters, calculated by index. |
|   | xdcr synchronous rate for shard | The number of documents successfully synchronized to the remote cluster per unit of time, calculated by shard. |
|   | Unsynchronized document number for shard | The number of unsynchronized documents between the local and remote clusters, calculated by shard. |
| XDCR: local stats Note XDCR-related metrics are supported only in version 6.8.13 and are currently unsupported in version 7.10.0. | Local document number | The number of local documents. The total number of documents in the XDCR source cluster, calculated by index or repository. |
|   | Local seq number | The local sequence number. The latest operation sequence number in the XDCR source cluster, calculated by index or repository. |
|   | Local checkpoint | The local checkpoint. The safely persisted operation sequence number in the XDCR source cluster, calculated by index or repository. |
| 0 | > Document Version: 2026062 |   |

|   | Local global checkpoint | The local global checkpoint. The sequence number of the persisted operation agreed upon by all shards in the XDCR source cluster, calculated by index or repository. |
|---|---|---|
| XDCR: remote stats Note XDCR-related metrics are supported only in version 6.8.13 and are currently unsupported in version 7.10.0. | Remote document number | The number of remote documents. The total number of documents in the XDCR destination cluster, calculated by index or repository. |
|   | Remote seq number | The remote sequence. The latest operation sequence number in the XDCR destination cluster, calculated by index or repository. |
|   | Remote checkpoint | The remote checkpoint. The applied operation sequence number in the XDCR destination cluster, calculated by index or repository. |
|   | Remote global checkpoint | The remote global checkpoint. The applied operation sequence number agreed upon by all shards in the XDCR destination cluster, calculated by index or repository. |

## 5 FAQ

### 5.1 Availability issues

#### 5.1.1 Abnormal cluster states

You can use the dashboards or run Elasticsearch commands to check the status of Elasticsearch clusters. This topic describes how to troubleshoot Elasticsearch cluster issues that are in abnormal states.

**Query the health status of a cluster**

You can view the health status of Elasticsearch clusters by using the following methods: View the health status of clusters in the cluster list of the Elasticsearch O&M console. For more information, see Cluster list. View the health status of clusters on the custom dashboard. For more information, see View Elasticsearch monitoring metrics. View the health status of clusters in Cloud Monitor. For more information, see Use Cloud Monitor to view the metrics of an Elasticsearch cluster. View the health status of clusters in the Grafana dashboard. For more information, see Use the Grafana dashboard to view the metrics of an Elasticsearch cluster. Run Elasticsearch commands to check the status of Elasticsearch clusters. Log in to the Kibana console and run the `GET _cluster/health` command to check the cluster status. You can also run the `GET _cat/nodes` command to view node information. Log in to OPS1 and run the `kubectl get es -A` command to check the cluster status.

**Cluster health status and exception description**

The cluster health is indicated by using the green, yellow, and red colors.

| Cluster health | Description |
|---|---|
| green | The cluster is in the normal state, and all shards are assigned as expected. |
| yellow | The cluster is available, but some replica shards are not assigned. |
| red | Some primary shards cannot be assigned due to indexes in the red state. Data cannot be written to these indexes. Consequently, the cluster fails to provide services as normal. |

If the cluster is in the yellow or red state, the cluster has primary or replica shards that cannot be assigned. The following table describes the common causes of unassigned shards.

| Field | Cause |
|---|---|
| INDEX CREATED _ | Shards are not assigned during index creation. When you create an index, you must wait for Elasticsearch to assign all shards to nodes. |
| CLUSTER RECOVERED _ | Shards are not assigned because the cluster is not completely restored. If a cluster fails or restarts, shards are re-assigned only after the cluster is completely restored. |
| INDEX REOPENED _ | Shards are not assigned because a disabled index is enabled again. When a disabled index is enabled again, its shards need to be re- assigned. |
| DANGLING INDEX IMPORTED _ _ | Shards are not assigned because a dangling index is imported. If an index can be found on data nodes but does not exist in the cluster state, the index is known as a dangling index. For example, after a node is disconnected, indexes that are more than the value of cluster.indices.tombstones.size (the default is 500) are deleted from the cluster. After the node is added to cluster again, the local indexes are imported to the cluster. In this scenario, no corresponding metadata exists in the cluster state. As a result, the deleted indexes become dangling indexes. The most common solution is to delete these dangling indexes. |
| NEW INDEX RESTORED _ _ | Shards are not assigned because data is restored to a new index. When data is restored to a new index from another index in an Elasticsearch cluster, shards are assigned to nodes. |
| EXISTING INDEX RESTORED _ _ | Shards are not assigned because data is restored to a disabled index. When an index is disabled, all shards of the index are unassigned. These shards cannot be assigned before the index is enabled. |
| REPLICA ADDED _ | A replica shard is not assigned because a replica is explicitly added. When you add a replica for an index, you may need to wait for Elasticsearch to assign the replica to a node. |
| ALLOCATION FAILED _ | Shards are not assigned because Elasticsearch fails to assign the shards. This issue may be caused by corrupted data files, insufficient replicas, or shard assigning policy. |

| NODE LEFT _ | A shard is not assigned because the node to host the shard is removed from the cluster. This issue may be caused by node or network failures or occur during node maintenance. |
|---|---|
| REROUTE CANCELLED _ | Not assigned due to explicit cancellation of reroute command. In Elasticsearch, you can call the cluster/reroute API to _ manually reroute shards. However, if you cancel the reroute operation during the process, shards will become unassigned. |
| REINITIALIZED | Shards are not assigned because the status of the index changes from Enabled to Initialized. This issue may occur during Elasticsearch node restarts or be caused by corrupted data files. |
| REALLOCATED REPLICA _ | A shard is not assigned because its replicas are re-assigned. Elasticsearch will attempt to re-assign the replicas of a shard on other nodes if a better node is found. This may cause unassigned shards. |

**Solutions**

**Method 1: Use the Kibana console**

1. Log in to the Kibana console of the Elasticsearch cluster. For more information, see Log in
to the Kibana console. In this example, an Elasticsearch V7.10 cluster is used. Different operations may be required to log in to the Kibana console of clusters of other versions.
2. In the left-side navigation pane, click the
icon, and then choose **Management > Dev**
**tools**.
3. On the **Console** page, run the corresponding command to troubleshoot the issue.
i. View the health status of the clusters.

```
GET _cluster/health
```

ii. Query the number of the abnormal shard and the name of the index to which the shard belongs.

```
GET _cat/shards?v&h=index,shard,prirep,state,node,unassigned.reason
```

iii. View the reason why a shard is unassigned.

```
GET _cluster/allocation/explain
```

`{`

```json
   "index": "${indexName}",
   "shard": ${shardNum},
   "primary": false
```

`}`

|   | ${indexName} |
|---|---|
| ${shardNum} |   |

Replace ${indexName} with the name of the abnormal index. Replace ${shardNum} with the number of the abnormal shard.
4. Troubleshoot the issue based on the reason, the descriptions in the Cluster health status
and exception description section of this topic, and the actual situation.

**Method 2: Use the terminal**

1. Log in to the Apsara Infrastructure Management console, and click Terminal of the machine
hosting the **essen** pod for the target Elasticsearch cluster.
2. Run the corresponding command for troubleshooting.
i. Query the number of the abnormal shard and the name of the index to which the abnormal shard belongs, and record the result in the shards.txt file.

```bash
curl -XGET -uelastic:${Password of the Elasticsearch cluster} "http://${ip}:${port}/_cat/shards? v&h=index,shard,prirep,state,node,unassigned.reason" > shards.txt
```

When you run the command, replace the following variables:

| Variable | Description |
|---|---|
| ${Password of the Elasticsearch cluster} | The password that you specified when you created the Elasticsearch cluster. |
| ${ip} | The IP address to which the domain name of the Elasticsearch cluster is resolved. For more information, see View the basic information of an Elasticsearch cluster. |
| ${port} | The protocol port. For more information, see View the basic information of an Elasticsearch cluster. |

|   |   | ${Password of the | The password tha |
|---|---|---|---|
|   | Elasticsearch cluster} |   |   |

ii. View the number of the abnormal shard and the name of the index to which the shard belongs.

```
cat shards.txt | grep UNASSIGNED
```

iii. View the reason why the shard is unassigned.

```bash
curl -XPOST -uelastic:${Password of the Elasticsearch cluster} "http://${ip}:${port}/_cluster/allocation/explain?pretty" -H 'Content-Type:applicat ion/json' -d '{"index":"${Index name}","shard":${Shard number},"primary":false}'
```

When you run the command, replace the following variables:

|   | Variable |   | Description |
|---|---|---|---|
|   | ${Password of the Elasticsearch cluster} |   | The password that you specified when you created the Elasticsearch cluster. |
|   |   | ${Password of the | The password tha |
|   | Elasticsearch cluster} |   |   |
|   | ${ip} |   | The IP address to which the domain name of the Elasticsearch cluster is resolved. For more information, see View the basic information of an Elasticsearch cluster. |
|   | ${port} |   | The protocol port. For more information, see View the basic information of an Elasticsearch cluster. |
|   | ${Index name} |   | Replace with the name of the abnormal index obtained in the previous step. |
|   | ${Shard number} |   | Replace with the number of the abnormal shard obtained in the previous step. |

`"primary":false` indicates a replica shard, and `"primary":true` indicates primary shard.
3. Troubleshoot the issue based on the reason, the descriptions in the Cluster health status and
exception description section of this topic, and the actual situation. If the issue persists, collect the troubleshooting information and submit a ticket to the technical support of Alibaba Cloud. You must attach a screenshot of the abnormal state to the ticket and describe the operations you performed in detail.

**Example on troubleshooting a cluster whose health status is**

**yellow**

If the health status of a cluster is yellow, some replica shards are unassigned. In this case, troubleshoot the issue as follows:
1. In the Kibana console, run the following command to view the health status of the cluster
and the number of unassigned shards.

```
GET _cluster/health
```

2. The cluster is in the yellow state, and three shards are unassigned. Then, locate the cause.

```
GET _cluster/allocation/explain
```

3. The code for the reason why the shards are unassigned is `NODE_LEFT` . According to the
common causes of unassigned shards and the actual situation, some nodes in the cluster may be disconnected.
4. Run the following command to query the cluster node information and check whether nodes
are disconnected:

```
GET _cat/nodes?v
```

5. The result indicates that the data-0 node is disconnected, which causes the cluster to enter
the yellow state. In this case, you need to restore the data-0 node and re-add it to the cluster.

#### 5.1.2 Business request exceptions

This topic describes how to troubleshoot Elasticsearch cluster access failures.

**Procedure**

When a business request sent to an Elasticsearch cluster is abnormal, if the request is a slow request, see Slow queries to troubleshoot the issue. If access to the Elasticsearch cluster fails, perform the following steps to troubleshoot the issue.
1. Check whether the Elasticsearch cluster is in the Normal state.
i. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this example, the Elasticsearch V7.10 cluster is used. Different operations may be required to log in to the Kibana console of clusters of other versions. ii. In the left-side navigation pane, click the icon and choose **Management > Dev**
**Tools**.
iii. On the **Console** tab, run the following command to check whether the state of the index to be accessed is normal:

```
GET _cat/indices
```

If the index is in the red state, refer to Abnormal cluster states.
2. If the cluster is in the Normal state, check the network. Make sure that the application and
cluster reside in the same network. If they reside in different networks, switch to the same network. If the Elasticsearch cluster uses the SingleTunnel network type, the client must be connected to the same virtual private cloud (VPC) and vSwitch of the cluster.
3. If the application and cluster reside in the same network, run the following command on the
client to check whether access to the cluster is normal:

```bash
curl ${IP address of the Elasticsearch cluster domain}:9200 -uelastic:${Password of t he Elasticsearch cluster}
```

When you run the command, replace the following variables:

| Variable |   | Description |
|---|---|---|
| ${IP address of the |   | The IP address to which the domain name of the Elasticsearch cluster is resolved. For more information about how to obtain the IP address, see View the basic information of an Elasticsearch cluster. |
|   | ${IP address of the | IP address, see View the ba |
| Elasticsearch cluster |   |   |
|   |   | c |
| domain} |   |   |

| ${Password of the Elasticsearch cluster} | The password that you specified when you created the Elasticsearch cluster. |
|---|---|

|   | ${Password of the | The password th |
|---|---|---|
| Elasticsearch cluster} |   |   |

If the cluster can be accessed, check the application. If the cluster cannot be accessed, contact technical support. You must attach a screenshot of the issue to the ticket and describe the operations you performed in detail.

#### 5.1.3 Configuration update errors

This topic describes how to troubleshoot configuration update errors in Elasticsearch clusters.

**Procedure**

When you update the configuration of an Elasticsearch cluster, if the cluster remains in the
**Updating** state for a long period of time, you need to check whether the cluster is abnormal.
1. Log in to OPS1 and run the following command to check the node status:

```bash
kubectl get pod -n ${Namespace of the Elasticsearch cluster} | grep ${Name of the Ela sticsearch cluster}
```

When you run the command, replace the following variables:

| Variable | Description |
|---|---|
| ${Namespace of the Elasticsearch cluster} | The namespace to which the abnormal cluster belongs. You can log in to the Elasticsearch O&M console and click the Instance Management tab to find the variable. |
| ${Name of the Elasticsearch cluster} | The name of the abnormal cluster. |

|   |   |   | namespace |
|---|---|---|---|
|   | ${Namespace of the | The namespace | namespace |
| Elasticsearch cluster} |   |   |   |

|   |   | ${Name of the | The name o |
|---|---|---|---|
|   | Elasticsearch cluster} |   |   |

If a node remains in a state other than Running, the cluster configuration update is abnormal.
2. Query and analyze the log of the abnormal node.

```bash
kubectl logs ${Pod name of the Elasticsearch node} -c es -n ${Namespace of the Elasti csearch cluster}
```

When you run the command, replace the following variables:

| Variable | Description |
|---|---|

| ${Pod name of the Elasticsearch node} | The pod name of the abnormal node in Step 1. Example: test***- master-2. |
|---|---|
| ${Namespace of the Elasticsearch node} | The namespace to which the abnormal cluster belongs. You can log in to the Elasticsearch O&M console and click the Instance Management tab to find the variable. |

|   | ${Pod name of the | The pod nam |
|---|---|---|
| Elasticsearch node} |   |   |

|   |   |   | namespace |
|---|---|---|---|
|   | ${Namespace of the | The namesp | namesp |
| Elasticsearch node} |   |   |   |

3. If the log of the abnormal node is empty or no errors are thrown, check the operator log.

```bash
kubectl logs ${Pod name of the operator} -n elasticsearch
```

|   | kubectl get pod -n elasticsearch \| grep operator |
|---|---|
| ${Pod name of the operator} |   |

4. Analyze the preceding logs to locate the cause of the update error and troubleshoot the
issue. If the issue persists, perform the preceding steps to collect information and submit a ticket for technical support. You must attach a screenshot of the issue to the ticket and describe the operations you performed in detail.

#### 5.1.4 Abnormal cluster states caused by anti-affinity

**anti-affinity**

If your cluster is in an abnormal state due to anti-affinity, you can follow the steps in this topic to troubleshoot the issue.

**Background information**

Elasticsearch allows you to configure cluster anti-affinity to avoid deploying multiple data nodes or dedicated master nodes on the same physical machine. The anti-affinity rule for dedicated master nodes is strict, and the anti-affinity rule for data nodes is loose. Strict anti-affinity rule for dedicated master nodes: Multiple master nodes must not be scheduled to the same physical machine. Loose anti-affinity rule for data nodes: Try to avoid scheduling multiple data nodes to the same physical machine if possible. However, take resource utilization into consideration, you may have to schedule data nodes to the same physical machine if the number of physical machines is insufficient. In this case, Elasticsearch uses node attributes to avoid scheduling the primary and replica shards of the same index to the same physical machine. This prevents data loss caused by the failure of the physical machine. In addition, Elasticsearch indicates the unhealthy status of a cluster by changing the status of the cluster to yellow with Open Distro indexes. If you still want to deploy multiple data nodes on the same physical machine in this scenario, you need to modify the corresponding configuration so that the cluster can enter the green state. For more information, see the Fix a cluster in the yellow state due to the loose anti-affinity rule for data nodes section in this topic.

**Fix a cluster in the yellow state due to the loose anti-affinity**

**rule for data nodes**

1. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the
Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this example, a cluster of Elasticsearch V7.10 is used. The procedure may vary depending on the Elasticsearch version. The actual console page prevails.
2. In the left-side navigation pane, click the
icon and choose **Management > Dev Tools**.
3. On the **Console** tab, run the following command to view the distribution of nodes. Make
sure that the nodes are deployed across at least two physical machines.

```
GET _cat/nodeattrs?v&s=value
```

4. Modify the `cluster.routing.allocation.awareness.force.node_name.values` setting.

```
PUT _cluster/settings
```

`{`

```json
  "persistent": {
    "cluster.routing.allocation.awareness.force.node_name.values" : ""
```

`}` `}`

**Important**

You may need to replace awareness with node_ip for certain clusters. The actual cluster configuration prevails. When node migration occurs, pay attention to the node distribution and make sure that the nodes are deployed across at least two physical machines.
5. After all indexes are assigned, reset the setting in case all nodes are migrated to the same
physical machine.

```
PUT _cluster/settings
```

`{`

```json
  "persistent": {
    "cluster.routing.allocation.awareness.force.node_name.values" : null
```

`}` `}`

#### 5.1.5 GUI exceptions

This topic describes how to troubleshoot GUI exceptions that may occur when you use Elasticsearch. Failure to log in to the Kibana console Error message: Elasticsearch V6.X/7.X: kibana server is not ready yet Elasticsearch V5.X: Authorization Exception Cause: The whitelist of the kibanaserver account is improperly configured. Solution: Add the IP address of the Kibana service to the whitelist of the kibanaserver account. You can still log in to the Kibana console after the Kibana whitelist is disabled Exception: You can still log in to the Kibana console after the Kibana whitelist is disabled. Cause: The Kibana page is not reinitialized. Solution: Contact the on-site O&M engineer to restart the pod that runs the Kibana service. No monitoring data is displayed Exception: "no data" is displayed on the Grafana monitoring page. Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the exporter service to the whitelist of the monitoring_collector account. An error is thrown when you access the Elasticsearch plug-in page Error message: 403 Forbidden:[Ip 23.5.**.** is not allow in ip white/black list] Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the essen service to the whitelist of the monitoring_collector account. An error is thrown when you access the automatic backup page Error message: proxy request fail Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the essen service to the whitelist of the monitoring_collector account. Automatic backup does not take effect Exception: The snapshot is not taken normally after the specified time point. Cause: The whitelist of the monitoring_collector account is improperly configured. Solution: Modify the whitelist of the monitoring_collector account and add the IP address of the snapshot service to the whitelist of the monitoring_collector account. Kibana login error Exception: The account password is correct, but a login error is thrown (monitoring_collector is used as an example). Cause analysis: The whitelist of the account is not configured properly, or **Can Login to**
**Kibana** is not selected.
Solution: Add the IP address of the Kibana service to the whitelist of the account and select **Can Login to Kibana**. Cross-cluster access error (XDCR cluster synchronization failure) Error message: [][22.0.x.x:9300] general node connection failure Cause: The clusters that need to intercommunicate use different certificates. Solution: Contact the O&M engineer or refer to the cluster management operations in the O&M guide. For more information, see Security settings.

### 5.2 Performance issues

#### 5.2.1 Slow queries

This topic describes how to troubleshoot slow queries.

**Procedure**

1. Check whether all machines are slow or only some machines are slow.
i. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this example, an Elasticsearch V7.10 instance is used. Different operations may be required to log in to the Kibana console of instances of other versions. ii. In the left-side navigation pane, click the icon and choose **Management > Dev**
**Tools**.
iii. On the **Console** tab, run the following command: Call the profile API operation to obtain the profile content. Replace the values in the ${Index name} and `query` fields as needed.

```
GET /${Index name}/_search?human=true
```

`{`

```json
    "profile": true,
    "_source": false,
    "query": {
       "Your business code"
```

`}` `}` If you use other query methods, insert `"profile": true` into the code of the query. The returned result shows node IDs and the time required for handling the query on each node. If the query is slow on all nodes, all machines are slow. If the query is slow only on some nodes, some machines are slow. Query the correlation between node IDs and cluster pod names to locate the pod of a slow machine.

```
GET _cluster/state
```

2. Troubleshoot the issue based on the result.
If all machines are slow, you need to check the syntax used by the query. If some machines are slow, try the query again. If the issue persists, a single machine is faulty. If the issue does not occur, it is caused by an I/O issue. In both scenarios, submit a ticket to the technical support.

#### 5.2.2 Slow write requests

This topic describes how to troubleshoot slow write requests.

**Procedure**

1. Determine whether an individual write request is slow or all write requests are slow due to
heavy loads. If an individual write request is slow, test the request in other environments to determine whether the issue is caused by the environment. If all write requests are slow due to heavy loads, compare the cluster performance with the performance baseline.
2. If the issue is not caused by the preceding factors, check whether a performance bottleneck
exists. i. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this example, an Elasticsearch V7.10 cluster is used. Different operations may be required to log in to the Kibana console of clusters of other versions. ii. In the left-side navigation pane, click the icon and choose **Management > Dev**
**Tools**.
iii. On the **Console** page, run the following command to query node information and sort nodes by node name:

```
GET _cat/nodes?v&s=n
```

Check whether the value of **cpu** is excessively large. A value greater than 90 indicates heavy CPU loads. Alternatively, check whether the value of load_5m is greater than the number of CPU cores allocated to the pods of the cluster. If yes, the CPU loads are excessively high. iv. If the CPU loads are excessively high, you need to query the thread information.

```
GET _nodes/hot_threads
```

If the system returns a large number of write threads or merge threads of specific index shards, write operations are occupying CPU resources. Check the thread information again after the write operations are complete. If the CPU loads are still high, submit a ticket to the technical support.
3. If the CPU loads are normal, you need to query the write thread pool.

```
GET _cat/thread_pool/write?v
```

If the value of **queue** is not 0, the write loads are high. The cluster is overwhelmed by write requests. In this case, submit a ticket to the technical support.
4. Check for memory bottlenecks.
View the old garbage collection (GC) information on the Grafana dashboard for Elasticsearch. For more information, see Use Grafana to view the metrics of an Elasticsearch cluster. Old GC will cause stutters. In this case, submit a ticket to the technical support.
5. Check for disk bottlenecks.
i. Log in to OPS1 and run the following command to access the pod where the data node of the Elasticsearch cluster is hosted:

```bash
kubectl -n ${Namespace of the Elasticsearch cluster} exec -it ${Name of the Elastic search data pod} -c es /bin/bash
```

When you run the command, replace the following variables:

|   |   | Variable |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|
|   |   | ${Namespace of the Elasticsearch cluster} |   |   | The namespace to which the cluster belongs. You can log in to the Elasticsearch O&M console and click the Instance Management tab to find the variable. |   |   |
|   |   |   |   |   | You can run the kubectl get pod -n ${Namespace of the |   |   |
|   |   |   |   |   |   | kubectl get pod -n ${Namespace of the |   |
|   |   |   |   |   | You can run t |   |   |
|   |   |   | ${Name of the |   | Elasticsear |   |   |
|   |   | Elasticsearch data pod} |   |   |   |   |   |
|   |   |   |   |   | Elasticsearch cluster} |   |   |

|   | ${Namespace of the | The namespace | namespace |
|---|---|---|---|
| Elasticsearch cluster} |   |   |   |

ii. View the usage of all disks. Pay attention to the read rate (rkB/s), write rate (wkB/s), and disk usage (%util).

```
iostat -xm 3
```

`-m` indicates that MB is used as the unit for the read and write rates. `3` indicates that the read interval is 3 seconds. Data is refreshed every 3 seconds. iii. Find the overloaded disk on the disk usage, and then run the following command to view the information of the disk. The Device column shows the disk name.

```
iostat -xm ${Name of the disk} 3
```

Replace ${Name of the disk} with the value output in the previous step. iv. Collect disk information and submit a ticket to the technical support. If the issue persists, perform the preceding steps to collect information and submit a ticket to the technical support. You must attach a screenshot of the issue to the ticket and describe the operations you performed in detail.

#### 5.2.3 High CPU usage

This topic describes how to troubleshoot Elasticsearch clusters whose CPU usage is excessively high.

**Procedure**

When the CPU usage of a cluster exceeds 80, troubleshoot the cluster as follows.
1. Log in to the Grafana dashboard for Elasticsearch and check whether the CPU usage
remains at a high level. For more information, see Use Grafana to view the metrics of an Elasticsearch cluster. If the CPU usage is consistently high, perform the following steps to troubleshoot the issue.
2. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the
Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this topic, an Elasticsearch V7.10 cluster is used. Different operations may be required to log in to the Kibana console of clusters of other versions.
3. In the left-side navigation pane, click the
icon and choose **Management > Dev Tools**.
4. On the **Console** tab, run the following command to query the name of the node whose CPU
usage is excessively high:

```
GET _cat/nodes?v&h=cpu,name
```

5. On the **Console** tab, run the following command to query the hot_thread information of the
node with high CPU usage:

```
GET _nodes/${Name of the node with high CPU usage}/hot_threads
```

Replace ${Name of the node with high CPU usage} as needed based on the query result obtained in Step 4.
6. Troubleshoot the issue based on the hot_threads information and the actual situation.
If the issue persists, perform the preceding steps to collect information and submit a ticket to the technical support. You must attach a screenshot of the issue to the ticket and describe the operations you performed in detail.

#### 5.2.4 High heap memory usage

This topic describes how to troubleshoot Elasticsearch clusters whose heap memory usage is excessively high.

**Procedure**

When the heap memory usage of a cluster exceeds 90, troubleshoot the cluster as follows.
1. Log in to the Grafana dashboard for Elasticsearch and check whether the heap memory
usage remains at a high level. In addition, view the garbage collection (GC) metrics. For more information, see Use Grafana to view the metrics of an Elasticsearch cluster. If the heap memory usage is consistently high, perform the following steps to troubleshoot the issue.
2. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the
Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this example, the Elasticsearch V7.10 cluster is used. Different operations may be required to log in to the Kibana console of clusters of other versions.
3. In the left-side navigation pane, click the
icon and choose **Management > Dev Tools**.
4. On the **Console** page, run the following command to view the total memory occupied by all
segments on each node:

```
GET _cat/nodes?v&h=name,sm
```

If the memory occupied by segments on a node is excessively large, you need to reduce the memory usage by performing the following operations. i. Delete indexes that are no longer needed.

**Warning**

You cannot restore deleted indexes. Proceed with caution. Replace the ${Index name} in the following sections based on your requirements.

```
DELETE ${Index name}
```

ii. Disable indexes that are currently not in use and enable them when you need to use them.

```
POST ${Index name}/_close
```

5. View the memory usage of fielddata.
View fielddata of the cluster

```
GET _stats/fielddata?human
```

View fielddata of all nodes

```
GET _nodes/stats/indices/fielddata?human
```

View fielddata of an index

```
GET ${Index name}/_stats/fielddata?human
```

If the fielddata occupies excessive memory, clear the cache by running the following commands. Clean up all fielddata caches

```
POST _cache/clear?fielddata=true
```

Clean up the fielddata cache of an index

```
POST ${index name}/_cache/clear?fielddata=true
```

6. View the memory usage of query_cache.
Query the query_cache of the cluster.

```
GET _stats/query_cache?human
```

Query the query_cache of all nodes.

```
GET _nodes/stats/indices/query_cache?human
```

Query the query_cache of a node.

```
GET _nodes/${Node name}/stats/indices/query_cache?human
```

Query the query_cache of an index.

```
GET ${Index name}/_stats/query_cache?human
```

If query_cache occupies excessive memory, clear the cache by running the following commands. Clear all query_cache

```
POST _cache/clear?query=true
```

Clear the query_cache of an index

```
POST ${Index name}/_cache/clear?query=true
```

If the issue persists, perform the preceding steps to collect information and submit a ticket for technical support. You must attach a screenshot of the issue to the ticket and describe the operations you performed in detail.

#### 5.2.5 Heavy loads

This topic describes how to troubleshoot an overloaded Elasticsearch cluster.

**Procedure**

If the value of the Load5 average metric of a node remains greater than the value of the available_processors parameter for a long period of time, the node is overloaded. In this scenario, you can use one of the following methods to troubleshoot the issue:
1. Obtain the value of the Load5 average metric of the node.
i. Go to the Grafana dashboard of the Elasticsearch cluster. For more information, see Use Grafana to view the metrics of an Elasticsearch cluster. ii. Check whether the value of the Load5 average metric of each node is consistently high If the value of the Load5 average metric of a node remains high for a long period of time, record the name of the node and the value of the Load5 average metric.
2. Obtain the value of the available_processors metric of the node.
i. Log in to the Kibana console of the Elasticsearch cluster and go to the homepage of the Kibana console as prompted. For information about how to log in to the Kibana console, see Log in to the Kibana console. In this example, an Elasticsearch V7.10 cluster is used. Different operations may be required to log in to the Kibana console of clusters of other versions. ii. In the left-side navigation pane, click the icon, and then choose **Management > Dev**
**tools**.
iii. On the **Console** page, run the following command to query the value of available_processors of the desired node.

```
GET _nodes/${Name of the Elasticsearch node}/? filter_path=*.*.os.available_processors
```

Replace ${Name of the Elasticsearch node} with the name of the node in Step 1.
3. Check whether the loads of the cluster are high.
If the value of available_processors is greater than the value of the Load5 average metric recorded in Step 1, the node is overloaded. Proceed to the following steps.
4. On the **Console** page, run the following command to query the hot_threads value of the
node with high load: Replace ${Name of the Elasticsearch node with high load} based on the actual situation.

```
GET /_nodes/${Name of the Elasticsearch node with high load}/hot_threads
```

5. Troubleshoot the issue based on the value of the hot_threads metric and the actual
situation. If the issue persists, collect the troubleshooting information and submit a ticket to the technical support of Alibaba Cloud.

### 5.3 Issues related to the use of Elasticsearch

**Elasticsearch**

#### 5.3.1 Issues related to cluster creation

This topic describes how to troubleshoot issues that occur when you create an Elasticsearch cluster in the Apsara Uni-manager Operations Console. When you create an Elasticsearch cluster in the console, a 400 error may occur, the cluster may remain in the Updating state for a long period of time, or the cluster is not in the green health state, such as the yellow or unknown health state.

**Background Information**

For more information about how to create an Elasticsearch cluster in the Apsara Unimanager Management Console, see the **Create a cluster** topic in **Elasticsearch User**
**Guide**.
For more information about how to create an Elasticsearch cluster in the Apsara Unimanager Operations Console, see Create an instance.

**Overview**

This topic describes the common issues that may occur when you create Elasticsearch clusters in the Apsara Uni-manager Operations Console and how to troubleshoot these issues. A 400 error occurs when you create a cluster The cluster remains in the Updating state during cluster creation for a long period of time The cluster is not in the green health state after cluster creation

**A 400 error occurs when you create a cluster**

**Issue**

The following error is thrown: This error message indicates that the number of data nodes is greater than five but no dedicated master nodes are specified, or the number of data nodes is two but no dedicated master nodes are specified.

**Solution**

Recreate the cluster. If you specify two data nodes when you create the cluster, a dedicated master node is required. If you specify more than five data nodes, a dedicated master node is also required.

**The cluster remains in the Updating state during cluster**

**creation for a long period of time**

**Issue**

This means that the deployment of the cluster has not reached the final state.

**Solution**

1. Log in to the OPS1 server.
2. Query the information about the created cluster. Obtain the namespace of the cluster.

```bash
kubectl get es -A | grep ${Cluster name}
```

Replace ${Cluster name} with the actual name.
3. Query the pod information of the cluster. Obtain the name of the pod whose status is not
Running.

```bash
kubectl get pod -n ${Cluster namespace}
```

Replace ${Cluster namespace} based on the query result obtained in Step 2.
4. View the details of the pod whose status is not Running.

```bash
kubectl describe pod ${podname} -n ${Cluster namespace}
```

${podname} indicates the name of the pod whose status is not Running. Replace it based on the query result in step 3. Replace ${Cluster namespace} based on the query result obtained in Step 2.
5. Find the reason why the pod is not in the Running state and fix the issue.
If the issue persists, perform the preceding steps to collect information and submit a ticket to the technical support. You must attach a screenshot of the issue to the ticket and describe the operations you performed in detail.

**The cluster is not in the green health state after cluster**

**creation**

**Issue**

An unhealthy Elasticsearch cluster refers to a cluster whose health status is unknown during cluster creation or a cluster whose health status is red or yellow after the cluster is created.

**The cluster health status is unknown during cluster creation**

In most cases, after the deployment of a cluster reaches the final state, the cluster enters the green state. If the cluster does not enter this state after a long period of time, see The cluster remains in the Updating state during cluster creation for a long period of time section of this topic.

**The cluster health status is red or yellow after cluster creation**

Log in to the Kibana console and refer to Abnormal cluster states. For more information about how to log in to the Kibana console, see Log in to the Kibana console.

#### 5.3.2 View the basic information and monitoring information of a cluster

**monitoring information of a cluster**

This topic describes how to view the basic information and monitoring information of an Elasticsearch cluster for cluster O&M.

**View the basic information of the cluster**

If the cluster is created in the Apsara Uni-manager Management Console, go to the Apsara Uni-manager Management Console to view the basic information of the cluster. In the instance list, click the ID of the cluster to view the basic information of the cluster. For more information, see the **View the basic information of a cluster** topic in **Elasticsearch**
**User Guide**.
If the cluster is created in the Apsara Uni-manager Operations Console, go to the Apsara Uni-manager Operations Console to view the basic information of the cluster. In the instance list, click the ID of the cluster to view the basic information of the cluster. For more information, see Create a cluster.

**View the monitoring information of the cluster**

If the cluster is created in the Apsara Uni-manager Management Console, choose **Products**

**> Migration and O&M Management > CloudMonitor > Cloud Resource Monitoring**

**> Product Monitoring > Big data (number plus) > Elasticsearch on k8s**. Click the ID
of the cluster or click **Monitoring chart** in the **Operation** column of the cluster to view the monitoring information. For more information, see the **Manage cloud service monitoring** topic in **Cloud Monitor User Guide**. If the cluster is created in the Apsara Uni-manager Operations Console, choose

**Monitor&Alert > Monitor Management > Cloud Platform Monitoring Dashboard >**

**Data Dashboard > Custom Dashboard > Elasticsearch Monitoring Dashboard** and
view the monitoring information. For more information, see the **Custom dashboards** topic in **Apsara Uni-manager Operations Console User Guide** .

#### 5.3.3 Configure the analysis-ik dictionary

analysis-ik is a built-in Chinese tokenization plugin for Alibaba Cloud Elasticsearch, designed specifically for indexing and searching Chinese text. With precise Chinese tokenization capabilities, this plugin improves search relevance and serves as a core component in Chinese-language scenarios such as E-commerce, government services, and log analysis.This topic describes how to use this plugin.

**Prerequisites**

Enable the whitelist. For details, see Account security settings.

**Limits**

The size of each uploaded custom dictionary file must be less than 1 MB. If you upload multiple custom dictionary files, their combined size must also be less than 1 MB. Otherwise, the upload fails.

**Notes**

This operation restarts the instance. Proceed with caution.

**Procedure**

1. Go to the plugin configuration page.
i. Log on to the Elasticsearch O&M console. ii. In the instance list, click the target instance ID. iii. In the navigation pane on the left, choose **Plugin management > Elasticsearch**
**plugins**.
iv. In the plugin list, find the **analysis-ik** plugin and click **Modify configuration** on the right.
2. Add files.
i. Add a custom file. a. On the configuration page, click **Add file** and enter a custom file name in the dialog box. This topic uses `extra_main_1.dic` as an example.

**Important**

You can customize the file name, but do not change the extension `.dic` . b. Click the created file name and edit its content on the right. Example:

```
Xixi Wetland Multiple lines of content aaabbb
```

ii. Add the IKAnalyzer.cfg.xml file. Click **Add file** again, name it `IKAnalyzer.cfg.xml` , and then edit its content on the right. The content is as follows:

```xml
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd"> <properties>
 <comment>IK Analyzer extension configuration</comment>
 <!--Users can configure their own extension dictionaries here -->
 <entry key="ext_dict">extra_main_1.dic</entry>
  <!--Users can configure their own extension stop word dictionaries here-->
 <entry key="ext_stopwords">custom/ext_stopword.dic</entry>
  <!--Users can configure remote extension dictionaries here -->
 <entry key="remote_ext_dict">location</entry>
  <!--Users can configure remote extension stop word dictionaries here-->
 <entry key="remote_ext_stopwords">http://xxx.com/xxx.dic</entry>
</properties>
```

**Important**

In the preceding code, replace the value after `key="ext_dict"` with the file name

|   | extra main 1.dic _ _ |
|---|---|
| ; |   |

from step a ( `extra_main_1.dic` ). If you have multiple files, separate them with a
3. Select the two files you created and click **OK**.
4. In the confirmation dialog box, click **OK**.
5. Select a restart method and click **OK**.
The instance now restarts. After the restart succeeds, the configuration takes effect.

**Verify the result**

Log on to Kibana for the target instance and run the following command to submit an analyzer and a tokenization string.

```
POST _analyze
```

`{`

```json
"analyzer": "ik_max_word", "text": "Xixi Wetland"
```

`}` Expected result: The system chunks the input text and extracts terms defined in your custom dictionary. If the output appears as follows, the operation succeeded. `{`

```json
  "tokens" : [
```

`{`

```json
      "token" : "Xixi Wetland",
      "start_offset" : 0,
      "end_offset" : 4,
      "type" : "CN_WORD",
      "position" : 0
```

`},` `{`

```json
      "token" : "Wetland",
      "start_offset" : 2,
      "end_offset" : 4,
      "type" : "CN_WORD",
      "position" : 1
```

`}` `]` `}`
