---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara File Storage NAS Operations and Maintenance Guide 20250102"
product_version: "V3.18.3"
doc_version: "20250102"
pdf_pages: 28
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara File Storage NAS Operations and Maintenance Guide 20250102.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20File%20Storage%20NAS%20Operations%20and%20Maintenance%20Guide%2020250102.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara File Storage NAS Operations and Maintenance Guide 20250102

## Table of Contents

- 1 Service architecture
- 2 Apsara Uni-manager Operations Console user guide
  - 2.1 Log on to the Apsara Uni-manager Operations Console
  - 2.2 User data
  - 2.3 Cluster management
  - 2.4 Network management
    - 2.4.1 Mount target management
  - 2.5 Monitoring
    - 2.5.1 Inspection configurations
    - 2.5.2 Inspection history
  - 2.6 O&M support
    - 2.6.1 Workflow management
      - 2.6.1.1 Workflow release orders
        - 2.6.1.1.1 Scale out a cluster
        - 2.6.1.1.2 Scale in a cluster
        - 2.6.1.1.3 Shut down a server
      - 2.6.1.2 Workflow instances
      - 2.6.1.3 Workflow definitions
    - 2.6.2 Commands
  - 2.7 NAS dashboard
  - 2.8 Background audit
- 3 Routine maintenance
  - 3.1 View the status of a KV service
  - 3.2 Query the information about file systems and users
  - 3.3 Query the information about a cluster recycle job
  - 3.4 View the module service logs of a NAS cluster
  - 3.5 Set the disk usage limit

## 1 Service architecture

File Storage NAS (NAS) is a cloud service that provides file storage for compute nodes such as Elastic Compute Service (ECS) instances and Container Service for Kubernetes (ACK) clusters. NAS supports standard file access protocols. NAS file systems are based on Apsara Distributed File System. NAS maintains three copies for each data file across multiple storage nodes. Frontend nodes receive and cache connection requests from Network File System (NFS) clients. Frontend nodes are highly available because they are stateless and distributed. In a cluster of six nodes, less than 30 minutes is required to restore one TB of data. The larger the cluster size, the faster the restoration speed. For more information, see **NAS Technical Whitepaper**.

## 2 Apsara Uni-manager Operations Console user guide

**Operations Console user**

**guide**

### 2.1 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: ops.asconsole.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.

### 2.2 User data

On the User Data page, you can view the details of user data and file systems.

**Basic information management**

You can view the list of users and the list of file systems. Perform the following steps: View the list of users i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > NAS Storage** iii. In the left-side navigation pane, choose **User Data > Basic Information > Users**. To view the data of a specific user in the list, click **Overview** in the Actions column. View the list of file systems i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Product Operation > Storage > NAS Storage** iii. In the left-side navigation pane, choose **User Data > Basic Information > File**
**System List**.
To view the details of a file system in the list, click the ID of the file system.

**User data overview**

You can query user data by **UID** and **date**. Perform the following steps:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **User Data > User Data Overview**. On the User
Data Overview page, enter a **UID**, select a **date**, and then click **View**.

### 2.3 Cluster management

In the Cluster Management section, you can view the region information and cluster information.

**Region information management**

You can view the region information by performing the following steps:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Cluster Management > Region Information**
**Management**.
4. On the **Region Information Management** page, view the region information.

> **Note:** You can click **Refresh** in the right-right corner of the page to refresh the region information.

**Cluster information management**

You can view the details of each cluster, including the region, cluster name, cluster environment, nuwa address, and AG address. Perform the following steps:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Cluster Management > Cluster Information**
**Management**.
4. On the **Cluster Information** page, click the cluster name. In the **Cluster Details** dialog
box, view the details of the cluster.

> **Note:** You can click **Refresh** in the right-right corner of the **Cluster Information** page to refresh the cluster information.

### 2.4 Network management

#### 2.4.1 Mount target management

On the Mount Target Management page, you can view the details of mount targets and refresh the health status of mount targets.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Network Management > Mount Target**
**Management**.
4. In the **Search Condition** section of the **Mount Target Management** page, select **Search**
**by VIP**, enter a virtual IP address (VIP), and then click **Search**.
Configure the following filter conditions: **Region**, **Network Type**, **Category**, **Network**, and **Port**. Click a mount target in the **Port** column to view its details. Click **Refresh Health Status** to refresh the health status of a mount target.

### 2.5 Monitoring

> **Important:** The current version does not support the **Alert History** and **Alert Configuration** features. Only the **Inspection Configuration** and **Inspection History** features are supported.

#### 2.5.1 Inspection configurations

The system provides built-in inspection tasks. You can switch task status, query task details, edit task configurations, delete existing tasks, and immediately execute tasks. This helps you better understand the inspection status and ensure operational security.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Monitoring Center > Inspection**
**Configurations**.
4. On the **Inspection Tasks** page, select a search type, enter a task category, set the **Type**
and **Status** of the task, and then click **Search**. After the configuration is complete, you can perform the following operations:

> **Note:** In the current version, you cannot create monitoring tasks.

Query the inspection history of a task In the task list, click the name of a task in the **Task Name** column. On the **Inspection**
**Results** page, view the inspection history.
Switch the status of a task In the **Task Status** column, turn on or off the status switch of the task. Query the details of a task In the **Actions** column, click **Details**. In the **Task Details** dialog box, view the task details. Edit a task If a task is in the **Disabled** state, click **Edit** in the **Actions** column. In the **Edit**
**Monitoring Task** dialog box, configure the parameters and click **OK**.
Delete a task If a task is in the **Disabled** state, click **Delete** in the **Actions** column. In the message that appears, click **Yes**. Execute a task immediately If a task is in the **Enabled** state, click **Execute** in the **Actions** column. In the message that appears, click **Yes**. After the inspection task is executed, you can view its details on the **Inspection History** page.

#### 2.5.2 Inspection history

You can query the inspection results of a task in the Data Cube console, including the type, start time, end time, status, and logs of the task. This helps you better understand the inspection results and ensure the normal operation of your business.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Monitoring Center > Inspection History**.
4. On the **Inspection Results** page, select a task type, search method, and time range, and
then click **Search**. You can turn off **Show All Tasks** or turn on **Show Abnormal Tasks** to view only abnormal tasks. After the configuration is complete, you can view the historical results of the specified task type, including the name, type, start time, end time, and status of the task. You can also perform the following operations based on your business requirements: View all details of a task Find the task that you want to view and click **View All** in the **Actions** column to view all details of the task, including the inspection results and alert information. View the details of an abnormal task Find the abnormal task that you want to view and click **View Exceptions** in the **Actions** column. On the View Exceptions page, you can view the details of the task, such as the inspection results and alert information. View the logs of a task Find the task that you want to view and click **View All** or **View Exceptions** in the
**Actions** column. Click **Log** in the **Log** column to view the logs of the task.

### 2.6 O&M support

#### 2.6.1 Workflow management

##### 2.6.1.1 Workflow release orders

You can query the task details of all workflows in the Data Cube console, including the details of published, uncompleted, completed, and specified tasks. You can also create new tasks and view task statistics so that you can better understand the task process and optimize task orchestration.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > Workflow Management >**
**Workflow Release Order**.
The **All Workflows** page has multiple tabs. You can perform operations based on your business requirements. Published Tasks Click the **Published Tasks** tab, configure the filter conditions, and then click the icon to filter the tasks. After the filter conditions are configured, you can query the completion status and task type of all published tasks. You can also perform the following operations on this tab. Query the details of a task In the **Task Number** column, click the task number to query the task details. You can also view the workflow and parameters of the task. View task parameters Find the task that you want to view and click **View Parameters** in the **Actions** column. In the panel that appears, view the parameters of the task. Restart a task For a task whose **Task Status** is **Failed**, click **Restart** in the **Actions** column to submit the task again. Uncompleted Tasks Click the **Uncompleted Tasks** tab, configure the filter conditions, and then click the icon to filter the tasks. After the filter conditions are configured, you can query the completion status and task type of all uncompleted tasks. You can also perform the following operations on this tab. Query the details of a task In the **Task Number** column, click the task number to query the task details. You can also view the workflow, parameters, and skip the task. View task parameters Find the task that you want to view and click **View Parameters** in the **Actions** column. In the panel that appears, view the parameters of the task. Restart a task For a task whose **Task Status** is **Failed**, click **Restart** in the **Actions** column to submit the task again. Completed Tasks Click the **Completed Tasks** tab, configure the filter conditions, and then click the icon to filter the tasks. After the filter conditions are configured, you can query the completion status and task type of all completed tasks. You can also perform the following operations on this tab. Query the details of a task In the **Task Number** column, click the task number to query the task details. You can also view the workflow and parameters of the task. View task parameters Find the task that you want to view and click **View Parameters** in the **Actions** column. In the panel that appears, view the parameters of the task. Task Details Click the **Task Details** tab. Select **Release Order Number** or **Object (IP)**, enter the content, and then click **Search**. If you select **Release Order Number**, you can query the information about tasks, including the task type, cluster, and parameters. You can also view the parameters and change the pause policy of failed tasks. If you select **Object (IP)**, you can click the icon to further filter the execution status and task type of all tasks under the object. Create Task Click the **Create Task** tab. You can select a workflow type from the **Workflow Name** drop-down list. You can also click **View Workflow List**. On the **Published Tasks** page, you can view the existing task types and select a workflow type from the **Workflow**
**Name** drop-down list.
After you select a workflow type, select a cluster, scheduled execution type, execution priority, and execution type, enter a description, and then click **Submit**. In the message that appears, click **Yes**. After the task is created, you can view the task status and information on the **Published Tasks** page. For more information about how to create a task, see Scale out a cluster, Scale in a cluster, and Shut down a server. You can also click **Generate Submission Link** to obtain the task link and paste it to the clipboard. Task Statistics Click the **Task Statistics** tab. On this tab, you can view the number of pending and running tasks of different task types, as well as the corresponding number of successes and failures. You can also click the icon in the **Executing** column to view information such as the task status and the name of the step. Click the number in the **Number** column to view the details of the workflow instance. For more information about workflow instances, see Workflow instances.

###### 2.6.1.1.1 Scale out a cluster

This topic describes how to add servers of a service role to a cluster to scale out the cluster.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > Workflow Management >**
**Workflow Release Order**.
4. On the **Create Task** tab, select the name of the scale-out workflow from the **Workflow**
**Name** drop-down list.
The following scale-out workflows are supported: ocm server scale-out, kv server scale-out, quota master scale-out, quota server scale-out, tiering master scale-out, and tiering server scale-out.
5. Select your cluster from the **Cluster** drop-down list. Make sure that you select the same
cluster in the **Apsara Infrastructure Management console** .
6. In the **Add Machine** section, select a server name.
The kv server scale-out workflow is used as an example. The operation is the same for other workflows. In this example, the server name is

```
 a34a13014.cloud.a13.amtest66(10.66.xx.xx) .
```

> **Note:** You do not need to add other servers to the scale-out workflow. You only need to perform operations on the servers owned by the service role.

In the **Apsara Infrastructure Management console** , you can view the name and IP address of a specified server. You can perform the following steps to log on to the Apsara Infrastructure Management console: i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane, click **Machine Management**. iv. Select **Hostname/IP Address**, **Status**, **Product**, or **Cluster** from the **Hostname/IP**
**Address** drop-down list, and enter the corresponding value in the text box to filter the
machines that you want to manage.
7. Configure other parameters.
Scheduled Execution: In the list, select a method to schedule the workflow. Execution Priority: Set the priority of task execution. Execution Type: In the list, select the type of the execution workflow.

> **Note:** Add a task description.

8. Click **Submit** to create a workflow.
9. On the **Published Tasks** tab, view all published workflows.
In the **Task Completion Status** column, three task statuses appear: **Executing**, **Failed**, and **Successful**.
0. **Optional.** View the cause of a failed task.
Click the ID of a failed task. The **Task Details** tab appears. Click **Workflow** to view the details. Click **Logs** to view the operational logs of the workflow.

> **Note:** The verification steps for other workflows are the same as that of the kv server.
> In the NFS service of Apsara Infrastructure Management, you can view all server IP addresses.

**Expected result**

The scale-out workflow is successful.

###### 2.6.1.1.2 Scale in a cluster

This topic describes how to remove servers of a service role from a cluster to scale in the cluster.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > Workflow Management >**
**Workflow Release Order**.
4. On the **Create Task** tab, select the name of the scale-in workflow from the **Workflow**
**Name** drop-down list.
The following scale-in workflows are supported: nfs server scale-in, smb server scale-in, kv server scale-in, ocm server scale-in, quota master scale-in, quota server scale-in, tiering master scale-in, and tiering server scale-in.

> **Important:** During scale-in, service access may be affected and latency may occur. We recommend that you perform scale-in operations during off-peak hours.

5. Select your cluster from the **Cluster** drop-down list. Make sure that you select the same
cluster in the **Apsara Infrastructure Management console** .
6. In the **Remove Machine** section, select a server name.
The scale-in workflow for quota_server is used as an example. The operation is the same for other workflows. In this example, the server name is `10.66.x.x` .

> **Note:** You do not need to add other servers to the scale-in workflow. You only need to perform operations on the servers owned by the service role.

In the **Apsara Infrastructure Management console** , you can view the name and IP address of a specified server. You can perform the following steps to log on to the Apsara Infrastructure Management console: i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane, click **Machine Management**. iv. Select **Hostname/IP Address**, **Status**, **Product**, or **Cluster** from the **Hostname/IP**
**Address** drop-down list, and enter the corresponding value in the text box to filter the
machines that you want to manage.
7. Configure other parameters.
Scheduled Execution: In the list, select a method to schedule the workflow. Execution Priority: Set the priority of task execution. Execution Type: In the list, select the type of the execution workflow.

> **Note:** Add a task description.

8. Click **Submit** to create a workflow.
9. On the **Published Tasks** tab, view all published workflows.
In the **Task Completion Status** column, three task statuses appear: **Executing**, **Failed**, and **Successful**.
0. **Optional.** View the cause of a failed task.
Click the ID of a failed task. The **Task Details** tab appears. Click **Workflow** to view the details. Click **Logs** to view the operational logs of the workflow.

**Expected result**

The scale-in workflow is successful.

###### 2.6.1.1.3 Shut down a server

This topic describes how to shut down an abnormal server of a service role in a cluster.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > Workflow Management >**
**Workflow Release Order**.
4. On the **Create Task** tab, select **Remove Machine** from the **Workflow Name** drop-down
list.

> **Important:** After a server is shut down, latency may occur. We recommend that you shut down servers during off-peak hours.

5. Select your cluster from the **Cluster** drop-down list. Make sure that you select the same
cluster in the **Apsara Infrastructure Management console** .
6. In the **Remove Machine** section, select a server name.

> **Note:** In the NFS service of Apsara Infrastructure Management, you can view all server IP addresses.

7. Configure other parameters.
Scheduled Execution: In the list, select a method to schedule the workflow. Execution Priority: Set the priority of task execution. Execution Type: In the list, select the type of the execution workflow.

> **Note:** Add a task description.

8. Click **Submit** to create a workflow.
9. On the **My Tasks** tab, view all published workflows.
In the **Task Completion Status** column, three task statuses appear: **Executing**, **Failed**, and **Successful**.
0. View the cause of a failed task.
Click the ID of a failed task. The **Task Details** tab appears. Click **Workflow** to view the details. Click **Logs** to view the operational logs of the workflow.

**Expected result**

The server shutdown workflow is successful.

##### 2.6.1.2 Workflow instances

You can view the list of workflow instances in the Data Cube console and manage the workflow instances based on your business requirements. For example, you can fix failed instances and remove obsolete instances. This helps you allocate resources and improve the automation level of your business.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > Workflow Management >**
**Workflow Instances**.
4. Select **Workflow Instance ID** or **Operator**, enter the content, and then click **Search**.
Click the icon to perform further filtering. After the search scope is configured, you can query the workflow instance ID, task type, completion status, start time, and execution status on the current page. In the **Workflow ID** column, you can click the ID of a workflow to query its details. You can also stop, restore, refresh, and repair workflow instances.

##### 2.6.1.3 Workflow definitions

You can view workflow definitions in the Data Cube console, including the activity steps of each workflow category, so that you can better manage workflows.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > Workflow Management >**
**Workflow Definitions**.
On the **Workflow Definitions** page, you can view the activity steps of each workflow category.

#### 2.6.2 Commands

The Data Cube console provides an easy-to-use, visual interface for you to run commands. You can customize commands and view the command execution history so that you can quickly solve difficult problems, efficiently locate difficult problems, and improve the efficiency of automated O&M.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **O&M Support > White Screen Commands >**
**Custom Commands**.
On the **Custom Commands** page, you can perform the following operations: Call a command template to run a command Click the **My Commands** tab. In the **Recently Used** and **Favorite Commands** sections, find the command that you want to run and click its name. You can also click **Select Command Template** in the upper-right corner and click the name of a command. On the details page of the command, you can call the command template, select
**Execution Machine** and **Execution Timeout Period**, and configure the template
content. Then, click **Run** to run the command. View the execution history of a command Click the **Execution History** tab and enter a keyword or select an execution status to search for a command. After the configuration is complete, you can view the execution history of the command, including the execution machine, execution status, and time. You can click **Execution Result** in the **Actions** column to view the execution result.

### 2.7 NAS dashboard

On the Business Overview page, you can view business data by region and time. On the Inventory Management page, you can view the Pangu data, KV data, and data trends of your clusters by time. This helps you quickly understand business data and manage inventory.

**Business overview**

You can view various business data by region and time, including the storage volume, storage volume by type, storage volume by protocol, and number of file systems. Perform the following steps:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **NAS Dashboard > Business Overview**.
4. On the **Business Data Overview** page, select a region and a time range, and then click
**View**.

> **Note:** You can also select a preset time range in the upper-right corner of the page.

5. On the page, view the **Storage Size**, **Storage Size by Type**, **Storage Size by Protocol**,
and **File System Number**.

**Inventory management**

You can view the Pangu data, KV data, and data change trends of your clusters by time. Perform the following steps:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **NAS Dashboard > Inventory Management**. The
**Inventory Level** page appears.
4. On the **Inventory Level** page, specify the **Dimension** and **Time** parameters, and click
**View**.

> **Note:** You can select **Pangu Data** or **KV Data** from the Dimension drop-down list to view the data storage capacity.

5. In the displayed data list, perform the following operations:
Click the chart icon in the Capacity column of a data item to view the corresponding trend chart. Click **View Details** in the Actions column to view the details of a data record.

### 2.8 Background audit

On the Background Audit page, you can view the operation logs of the management and control platform and the reports of platform access. This helps you better control and track the operation logs of the management and control platform and improve O&M efficiency.

**Operation logs**

The audit logs record the modifications made by users to the system. During security maintenance, you can filter the audit logs by using different keywords to quickly locate and handle security issues in a timely manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Background Audit > Operation Logs**.
4. On the **Operation Logs** page, select a time range and click **Search**.
You can also click the check box next to **Add Filter Condition** and select **Operator**, **IP**,
**Operation Log**, or **Operation Name** from the drop-down list.
You can move the pointer over an operation log to view the complete information of the operation log.

**Platform access reports**

On the Platform Access Reports page, you can view the following information: **User Access**
**Details**, **Percentage of All Operations**, **Operation Details**, **Daily Access PV**, and **Daily**
**Access UV**. You can perform the following steps to query data based on a time range:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Storage > NAS Storage**
3. In the left-side navigation pane, choose **Background Audit > Platform Access Reports**.
4. On the **Platform Access Reports** page, select a time range and click **Search**.
You can view the following information: **User Access Details**, **Percentage of All**
**Operations**, **Operation Details**, **Daily Access PV**, and **Daily Access UV**.

## 3 Routine maintenance

### 3.1 View the status of a KV service

**service**

This topic describes how to check whether the KV service of a File Storage NAS (NAS) cluster is normal.
1. Find the RecycleJob role in the nas-recycle service of the cluster and log on to the target
machine.
2. Use the kuadmin tool to view the NAS app service added to the KV service.
Command

```
/apsara/deploy/kuadmin listapp
```

Sample response If an error occurs in the output of the listapp command, the kvmaster service is abnormal.
3. Use the ku tool to check whether the KV service is normal.
Command

```
/apsara/deploy/ku checkready nas checkready ocm
```

Sample response If no output is returned for the checkready command or the status is NO, the KV service is abnormal.
4. Use the mcu tool to view the status and information of the kvmaster service.
i. Query the kvmaster service, which is typically 3master. Command

```
/apsara/deploy/mcu gas
```

Sample response ii. Query kvmaster config. Command

```
/apsara/deploy/mcu gac
```

Sample response

### 3.2 Query the information about file systems and users

**file systems and users**

1. Find the RecycleJob role in the nas-recycle service of your cluster and log on to the target
machine.
2. Use the ocm_cmd and ku tools to query the file system ID (fsid) and the corresponding
partition. i. Query the volume and fsid by specifying the username. Command

```
/apsara/deploy/ocm_cmd list_volume -u <user>
```

Sample response ii. Query the partition corresponding to the file system by specifying the fsid parameter. Command

```
/apsara/deploy/ku querypart nas <fsid>
```

Sample response
3. In the RecycleJob role, use the ocm_cmd tool to query the information about the NAS cluster
and permission group. Query the volume and fsid by specifying the username. Command

```
/apsara/deploy/ocm_cmd list_volume -u <user>
```

Sample response
4. Query the information about deleted volumes.
Command

```
/apsara/deploy/ocm_cmd list_deleted_volume
```

Sample response
5. Query the mount information by user and volume.
Command

```
/apsara/deploy/ocm_cmd get_volume_mount_info -u <user> -v <volume>
```

Sample response
6. Query the protocol type of the file system by user and volume.
Command

```
/apsara/deploy/ocm_cmd get_volume_protocoltype -u <user> -v <volume>
```

Sample response 1 indicates the Network File System (NFS) protocol. 2 indicates the Server Message Block (SMB) protocol. 3 indicates the combination of NFS and SMB.
7. Query the permission group by user.
Command

```
/apsara/deploy/ocm_cmd list_access_group -u <user>
```

Sample response
8. Query the permission policy by user and permission group.
Command

```
/apsara/deploy/ocm_cmd list_access_rule -u <user> -g <group>
```

Sample response
9. Modify the protocol type of the file system by user and volume.

```
/apsara/deploy/ocm_cmd update_volume_protocoltype -u <user> -v <volume> --protocolTyp e <1/2/3>
```

0. Query the partition and distance information.
i. Query the kvserver information of the cluster. Command

```
/apsara/deploy/ku --interactive=false --command=getallserver --appname=nas |grep 10280|grep tcp|awk '{print $2}'
```

Sample response ii. Query the partition and distance information based on the kvserver information. Command

```
/apsara/deploy/ofsu --interactive=false --command=getpartdist --param1=<kvserver> --param2=nas | grep -v PID
```

Sample response
1. Query the detailed information of the file system.
i. Query all partitions. Command

```
/apsara/deploy/ku --interactive=false --command=getallpart --param1=nas | grep tc p | awk '{print $3}'
```

Sample response ii. Query the file system by specifying the partition. Command

```
/apsara/deploy/ofsu --interactive=false --command=getfilesystem --appname=nas --p aram1=<partition>
```

Sample response iii. Query file system details by user and volume. Command

```
/apsara/deploy/ofsu --interactive=false --command=getfsinfo --appname=nas --param 1=<user> --param2=<volume>
```

Sample response
2. Query the azone and location information of the NAS cluster.
i. Obtain the ocm tool. The access_id and access_key is required.

```
vim /cloud/app/nasnfs/NFSSupervisor#/nfs_supervisor/current/conf.merge/ocm_cmd.json
```

ii. Record the ocm_host, access_id, and access_key information and use the ocm tool to query the location information. Command

```
/apsara/deploy/ocm_tool lli --ocm_host=<ocm_host> --access_id=<access_id> --acces s_key=<access_key>
```

Sample response

### 3.3 Query the information about a cluster recycle job

**cluster recycle job**

1. Find the RecycleJob role in the nas-recycle service of the cluster and use the nas_ju tool to
query the current recycle job of the cluster. Command

```
/apsara/deploy/nas_ju list
```

Sample response
2. Query the details of the recycle job by specifying the job name.
Command

```
/apsara/deploy/nas_ju info <job_name>
```

Example

```
/apsara/deploy/nas_ju info volume_recycle_20171024105007
```

Sample response

### 3.4 View the module service logs of a NAS cluster

**of a NAS cluster**

1. Find the RecycleJob role in the nas-recycle service of the cluster and view the logs of the KV
service. After you use the ku and kuadmin tools to determine whether the KV service is abnormal, you can view the corresponding ku.LOG and kuadmin.LOG in the /apsara/deploy/log directory to obtain the error message.
2. Log on to the OcmServer machine to view the ocm logs.
Generally, three ocm machines are deployed for load balancing. To find specific request logs, you may need to check the three machines.

```
vim /cloud/log/nas-ocm/OcmServer#/ocm_server/ocm_server.LOG
```

3. Log on to the Tengine machine under the nas-ocm service to view the NGINX logs.

```
cd/cloud/log/nasocm/Tengine#/tengine
```

```
cd /cloud/log/nas-ocm/Tengine#/tengine
```

The tengine_starter.log file stores the startup logs. The latest access_log file stores the success logs and the error_log file stores the error logs.
4. Log on to the NFSServer machine to view the ganesha logs.

```
vim /cloud/log/nas-kvengine/KVServer#/kv_server/ganesha.LOG
```

### 3.5 Set the disk usage limit

By setting the disk usage limit, you can control the total amount of data written to disks. When the data write volume reaches the limit, the system denies data writing. When the data write volume drops below the limit, the system resumes data writing. To set the disk usage limit, perform the following steps:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane, click **Product & Cluster O&M**. Enter **nas** in the **Product |**
**Cluster** search box.
4. Find your cluster and click **Cluster Details** in the Actions column.
5. On the **Desired State Configuration** tab, choose **services > nas-nfs > user >**
**nfs_supervisor** in the file list, and configure the nfs_supervisor.json file.
`{`

```json
    "nas_disk_usage_limit":90
```

`}` The value of the **nas_disk_usage_limit** parameter is a percentage. Data writing stops when the data write volume reaches the specified value. We recommend that you set the value to **90**. If the nfs_supervisor.json file is not created for your cluster, perform the following operations: i. On the right side of the **services > nas-nfs > user** folder, choose
**> Create File**.
Create a folder named nfs_supervisor. ii. In the **Create File** dialog box, set **Creation Type** to **Folder** and **File/Folder Name** to nfs_supervisor.json, and then click **OK**. iii. On the right side of the nfs_supervisor folder, choose
**> Create File**. Create a file
named nfs_supervisor.json. iv. In the **Create File** dialog box, set **Creation Type** to **File** and **File/Folder Name** to nfs_supervisor.json. v. Configure the nfs_supervisor.json file. `{`

```json
    "nas_disk_usage_limit":90
```

`}` The value of the **nas_disk_usage_limit** parameter is a percentage. Data writing stops when the data write volume reaches the specified value. We recommend that you set the value to **90**.
6. After the configuration is changed, the cluster is rolled again and the configuration takes
effect.

> **Note:** After data writing is disabled, you can use one of the following methods to resume data writing:
> Delete the file system or file content and perform write operations seven days later. The system recycles deleted data within seven days.
> Change the value of the nas_disk_usage_limit parameter.

**Verify the configuration**

To verify the configuration, perform the following steps:
1. Create a file system and mount it.
2. Write data to the file system and make sure that the data volume reaches the limit. Verify
that data writing is disabled. The use of other commands, such as ACL commands, is not affected.
3. View logs.
