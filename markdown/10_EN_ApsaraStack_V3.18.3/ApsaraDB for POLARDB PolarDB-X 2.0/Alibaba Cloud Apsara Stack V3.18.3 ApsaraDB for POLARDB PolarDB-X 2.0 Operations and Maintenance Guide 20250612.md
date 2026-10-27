---
title: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for POLARDB PolarDB-X 2.0 Operations and Maintenance Guide 20250612"
product_version: "V3.18.3"
doc_version: "20250612"
pdf_pages: 15
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for POLARDB PolarDB-X 2.0 Operations and Maintenance Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E5%8E%9F%E7%94%9F%E6%95%B0%E6%8D%AE%E5%BA%93PolarDB-X/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20ApsaraDB%20for%20POLARDB%20PolarDB-X%202.0%20Operations%20and%20Maintenance%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for POLARDB PolarDB-X 2.0 Operations and Maintenance Guide 20250612

## Table of Contents

- 1 Log on to the ApsaraDB Operations and Maintenance System
- 2 Instance management
  - 2.1 View instance details
  - 2.2 View instance change records
- 3 Task management
  - 3.1 View workflow O&M information
  - 3.2 Handle failed tasks on PolarDB-X
- 4 Cluster management
- 5 Proactive O&M
  - 5.1 View HA logs and node re-build tasks
  - 5.2 Mark a host offline

saraDB Operations and Maintena nce System

## 1 Log on to the ApsaraDB Operations and Maintenance System

**Operations and Maintenance**

**System**

This topic describes how to log on to the ApsaraDB Operations and Maintenance System.

**Prerequisites**

Before you log on to the ApsaraDB Operations and Maintenance System using the endpoint, make sure that you have obtained the endpoint, username, and password of the ApsaraDB Operations and Maintenance System from the deployment engineer or system administration. Before you log on to the ApsaraDB Operations and Maintenance System using the Apsara Uni-manager Operations Console, make sure that you have obtained the username, and password of the ApsaraDB Operations and Maintenance System from the deployment engineer or system administration. A web browser is available. We recommend that you use Google Chrome.

**Use the endpoint**

1. In the address bar of the browser, enter the endpoint of the ApsaraDB Operations and
Maintenance System.
2. Enter your **username** and **password** and then click **Log On**.

**Use the Apsara Uni-manager Operations Console**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Products**.
3. Choose **Databases > ApsaraDB Operations and Maintenance System** .
ement

## 2 Instance management

### 2.1 View instance details

This topic describes how to view the details and topology of an instance.

**PolarDB-X instance structure**

A PolarDB-X instance consists of four elements: compute nodes (CNs), storage nodes (DNs), global meta service (GMS), and Change data capture (CDC) nodes. The following figure shows the architecture of an instance.

**Key components**

Global meta service (GMS): provides distributed metadata and a global timestamp distributor named Timestamp Oracle (TSO) and maintains meta information such as tables, schemas, and statistics. GMS also maintains security information such as accounts and permissions. Compute node: provides a distributed SQL engine that contains core optimizers and executors. A CN uses a stateless SQL engine to provide distributed routing and computing and uses the two-phase commit protocol (2PC) to coordinate distributed transactions. A CN also executes DDL statements in a distributed manner and maintains global indexes. Data node: provides a data storage engine. A data node uses Paxos to provide highly reliable storage services and uses multiversion concurrency control (MVCC) for distributed transactions. A data node also provides the pushdown computation feature to push down operators such as Project, Filter, Join, and Agg in distributed systems, and supports local SSDs and shared storage. CDC node: provides a primary/secondary replication protocol that is compatible with MySQL. The primary/secondary replication protocol is compatible with the protocols and data formats that are supported by MySQL binary logging. CDC uses the primary/secondary replication protocol to exchange data.

**View instance details**

## 1 Log on to the ApsaraDB Operations and Maintenance System.

2. Choose **Instance Management > Instance List**.
3. Click **Advanced Search** at the top and filter instances using the search boxes.
ement
4. Find the instance and click its name in the **User instance name** column. On the **Basic**
**Information** page, you can view the instance topology.
In the topology: Logic instance: the logical instance name of the entire cluster. For most O&M tasks and from the user perspective, logical instances are displayed. Normal child instance: the compute node cluster to which the PolarDB-X instance is attached. No O&M tasks are performed on the child instance. On the Instance Details page of the child instance, you can view the information about the compute nodes. Normal RDS instance (pxc-xdb-m-****): the GMS instance. Only one GMS instance is displayed. It is an independent ApsaraDB RDS for MySQL instance that you can perform O&M tasks. Normal RDS instance (pxc-xdb-s-****): the data node cluster. Each data node is an independent ApsaraDB RDS for MySQL instance. You can search for the instance name in the ApsaraDB RDS for MySQL console to go to the O&M page of this instance on the ApsaraDB Operations and Maintenance System. All O&M tasks available for ApsaraDB RDS for MySQL instances are applicable to this instance. PolarDB-X calls APIs to perform O&M tasks on ApsaraDB RDS for MySQL instances. For example, PolarDB-X performs create, change configurations, upgrade, and release tasks to trigger creating, changing configurations of, upgrading, and releasing ApsaraDB RDS for MySQL instances. Normal RDS instance (pxc-******-cdc): the CDC node of the PolarDB-X instance. Although it is an ApsaraDB RDS for MySQL instance, it is not independently available for O&M tasks. This instance combines the binlogs of all data nodes into one as the logical binlogs of the PolarDB-X instance and provides the unified binlog service in the distributed database.

### 2.2 View instance change records

This topic describes how to view API logs and HA logs.

**View API logs**

2. Choose **Instance Management > Instance List**.
3. Click **Advanced Search** at the top and filter instances using the search boxes.
ement
4. Find the instance and click its name in the **User instance name** column.
5. In the left-side navigation pane, click **Instance Change Records**. On the page that
appears, click the **API Logs** tab. API logs record the details of the RDS API requests called by the instance, including the request time, API name, and source IP address. In routine O&M, you can obtain call information such as instance request parameters, errors, and request IDs on this tab.

**View HA logs**

2. Choose **Instance Management > Instance List**.
3. Click **Advanced Search** at the top and filter instances using the search boxes.
4. Find the instance and click its name in the **User instance name** column.
5. In the left-side navigation pane, click **Instance Change Records**. On the page that
appears, click the **HA Logs** tab. HA logs record the causes and effects of instance HA switchover actions. In routine O&M, you can obtain information for discovering instance switchover causes or switchover failures.

## 3 Task management

### 3.1 View workflow O&M information

**information**

This topic describes how to view the task list and workflow O&M information. A workflow is triggered when you perform O&M tasks on an instance, such as creating an instance, restarting the instance, and changing its configurations. When the workflow is completed, the related O&M task ends. If a step in the workflow fails, you must troubleshoot the failure.

**View the task list**

2. Choose **Instance Management > Instance List**.
3. Click **Advanced Search** at the top and filter PolarDB-X instances using the search boxes.
4. Find the instance and click its name in the **User instance name** column.
5. In the left-side navigation pane, click **Task Management**. On the right side of the page,
you can view all tasks: interrupting tasks, waiting tasks, interrupted tasks, temporarily closed tasks, suspending tasks, and running tasks. You can filter tasks and specify which columns to display.

**View workflow details pages**

On the Task Management page, click a **task ID** to go to the workflow details page.
**Basic Information**: displays the basic information of the workflow, including the task ID,
workflow ID, workflow duration, and start and end time.
**Current Execution Logs**: displays the execution logs of the current step.
**Workflow Steps**: displays the execution details of each step of the workflow, such as the
execution time, parameters, status, and duration. It also displays the operations in each step, such as retry, step redirection, and temporary closing. The following figure shows a successful step. If a step fails, the retry, step redirection, and temporary closing are supported. The following figure shows a failed step.
**Task Intervention Logs**: displays the operation information of each workflow O&M.
**Interrupted Workflows**: When you click this button, the Interrupted Tasks tab appears.
Click the ID of the interrupted task to go to the workflow details page. You can use it to handle interrupted steps. Retry: Click it to retry the current step. If the step is still interrupted, contact Alibaba Cloud technical support personnel. Temporarily Close: If a workflow does not need to be processed or does not need to be processed temporarily, close the workflow to avoid affecting other workflows. Contact Alibaba Cloud technical support personnel for performing this operation. Redirect to Specified Step: You are redirected to another step. Contact Alibaba Cloud technical support personnel for performing this operation.

### 3.2 Handle failed tasks on PolarDB-X

**PolarDB-X**

The data nodes and GMS of the PolarDB-X cluster are independent ApsaraDB RDS for MySQL instances. Therefore, ApsaraDB RDS for MySQL workflows are triggered when you create, change configurations of, upgrade, release, or add nodes to a PolarDB-X instance. If a ApsaraDB RDS for MySQL workflow fails, the corresponding PolarDB-X task also fails. All PolarDB-X task steps are idempotent and can be retried. However, in special cases (such as when an ApsaraDB RDS for MySQL task fails), you need to handle the failures. This topic describes how to handle common ApsaraDB RDS for MySQL task failures.

**Failed to create a PolarDB-X instance**

If a PolarDB-X instance fails to be created and you are stuck in the wait_create_xdb_complete step of the create_polardbx_cluster task, the possible cause is that timeout occurs when PolarDB-X waits for creating data nodes and the GMS. Solution: Check whether the tasks of creating these ApsaraDB RDS for MySQL instances are normal. Then, perform operations such as retrying the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide. On the PolarDB-X instance details page, click the corresponding ApsaraDB RDS for MySQL instance. In the left-side navigation pane of the page that appears, click **Task List**. On the page that appears, you can find the workflows of the corresponding data nodes and GMS.

**Failed to release a PolarDB-X instance**

In the delete_polardbx_cluster task, if you are stuck in the drop_storage or drop_meta_db step (releasing the GMS and data nodes), you can keep retrying. (If the ApsaraDB RDS for MySQL instance is not in the Running state, you need to wait for other ApsaraDB RDS for MySQL tasks to be executed before you continue to retry.) If you are stuck in the wait_drop_storage step, you are waiting for the ApsaraDB RDS for MySQL release task to be completed. Check whether the ApsaraDB RDS for MySQL release task is normal. Then, perform operations such as retrying the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed to change configurations of a PolarDB-X instance**

In the modify_polardbx_cluster task, if you are stuck in the modify_storage_srv_class step, you are waiting for changing the configurations of storage nodes and the GMS. If the resources are insufficient, this step fails. You can increase cluster resources. If no resources are available, you can jump to the do_disable_aurora step and continue to change the configurations of compute nodes. In the modify_polardbx_cluster task, if you are stuck in the wait_xdb_status_activation step (waiting for the configuration change task of ApsaraDB RDS for MySQL to complete), check whether the configuration change task of ApsaraDB RDS for MySQL is normal. Then, perform operations such as retrying the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed to upgrade the engine version of a PolarDB-X instance**

In the upgrade_polardbx_cluster task, if you are stuck in the upgrade_storage_version step, you are waiting for upgrading the storage nodes and GMS. If the ApsaraDB RDS for MySQL instance is not in the Running state, it will fail. You can wait until other ApsaraDB RDS for MySQL tasks are finished and retry this task. In the upgrade_polardbx_cluster task, if you are stuck in the wait_xdb_status_activation step (waiting for the upgrade task of ApsaraDB RDS for MySQL to complete), check whether the upgrade task of ApsaraDB RDS for MySQL is normal. Then, perform operations such as retrying the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed to add nodes to a PolarDB-X instance**

In the add_node_polardbx_cluster task, if you are stuck in the wait_new_storage_activation step (waiting for the data nodes to be created). Check whether the task to create these ApsaraDB RDS for MySQL instances is normal. Then, perform operations such as retrying the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed to back up a PolarDB-X instance**

If you are stuck in the wait_backup_job_finished step, you are waiting for the task to back up the new data nodes to complete. If you are stuck in the additional_backup_set_info step, you are waiting for obtaining backup set information and proportional backup set sizes of ApsaraDB RDS for MySQL. This step will fail because the task is completed when wait_backup_job_finished is displayed, but the backup set is unavailable. You also need to check the status of the backup task of the data node. On the instance details page of each data node, click **Backup and Restoration** in the leftside navigation pane to view the status of the backup task. ment

## 4 Cluster management

2. In the left-side navigation pane, click **Cluster Management**.
3. Filter clusters using the search boxes at the top and find the cluster you want to view.
4. Click the **cluster name** to go to the cluster details page.
5. Find the machine and click **Details** in the line, you can view the instance information.

## 5 Proactive O&M

### 5.1 View HA logs and node re-build tasks

**build tasks**

A PolarDB-X instance allows multiple compute nodes to concurrently provide services and does not support primary/secondary switchover. However, when a single node is abnormal, the system automatically removes traffic from it and triggers a node re-build task. In the left-side navigation pane of the ApsaraDB Operations and Maintenance System, click
**Instance List**. On the page that appears, find the instance and click its name in the **User**
**instance name** column. On the page that appears, click **Instance Change Records**.
View the removing traffic actions in HA logs. View the status of the node re-build tasks in **Task List**.

### 5.2 Mark a host offline

In the left-side navigation pane of the ApsaraDB Operations and Maintenance System, click
**System Hosts** or **User Hosts**. On the page that appears, click the IP address of a host or
click **Details** in the Actions column to go the Host Details page. PolarDB-X allows you to mark a host as offline. In this case, the system automatically triggers node re-build tasks for all compute nodes on the host.
