---
title: "Database Backup Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20250626"
pdf_pages: 14
source_pdf: "60dc3650c771f9c2_Alibaba Cloud Apsara Stack V3.18.6 Database Backup Operations and Maintenance Guide 20250626.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%A4%87%E4%BB%BD/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Database%20Backup%20Operations%20and%20Maintenance%20Guide%2020250626.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Database Backup Operations and Maintenance Guide

## Table of Contents

- 1 DBS O&M console overview
- 2 Logon to the DBS O&M console
- 3 Task management
  - 3.1 Manage tasks
  - 3.2 Manage a task module
- 4 Resource management
  - 4.1 View DBS resources
  - 4.2 Unpublish DBS resources
  - 4.3 View DBS CIDR blocks
- 5 Usage
  - 5.1 View all subtasks in a backup plan
  - 5.2 Quickly view a full backup task or a backup set download task
  - 5.3 Manually restart a task

## 1 DBS O&M console overview

The Database Backup Service (DBS) O&M console is a backend O&M system for DBS. This topic describes the features of this console.

**Features**

This console provides the following features: You can view and manage all existing tasks and abnormal tasks, task execution details, and information about the source and destination databases. You can view the running status of DBS resources, unpublished DBS resources, and DBS CIDR blocks. e

## 2 Logon to the DBS O&M console

**console**

This topic describes how users such as O&M engineers log on to the DBS O&M console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.
3. Enter the username and password.
e Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Management Console, choose

**Products**

6. Select **DBS** from the **Database O&M** drop-down list to go to the **DBS O&M console**.

## 3 Task management

### 3.1 Manage tasks

This topic describes how to view and manage all existing and abnormal tasks on the task management page.
1. Log on to the DBS O&M console.
2. In the left-side navigation pane, choose **Tasks > All Tasks**.
3. In the upper part of the page, you can enter a keyword in the search box and click **Search**
to search for tasks. On the **All Tasks** page, you can also click **Advanced Options** to specify more filter conditions to filter tasks.
4. Find the task that you want to manage and click the task name.
5. On the **Task Details** page, perform operations described in the following table based on
your business requirements.

| Task management category | Operation |
|---|---|
| View the details of the task | View information about your instance, the task, and your source and destination databases. |
| View the basic information of a module | i. Click Details of a task module, such as the schema backup module, full backup module, continuous incremental backup module, or precheck module. ii. On the Basic Information tab, view information about a task module, including task ID, IP address of a service node on which the task is running, and node version. |
| View user operation records | In the Task Information section, click View User Actions next to Task ID to view the operation records of the task. |
| Modify the configurations of the task | In the Task Information section, click Modify Configurations to change task configurations based on your business requirements. Then, click OK. |

| Release the task | In the Task Information section, click Release Task. Then, click OK in the message that appears. Warning After a task is released, all the data of the task is deleted and cannot be retrieved. Proceed with caution. |
|---|---|
| Verify full data | In the upper-right corner of the Task Details page, click Full Data Verification to configure a verification task. Then,click Add. |

**Related operations**

You can also choose **Tasks > Abnormal Tasks** to view all anomalous tasks within your account, and then click the name of an abnormal task to go to the task details page for viewing or managing the task. Related operations are the same as those mentioned in the
**Procedure** section of this topic. This section is for reference only.

### 3.2 Manage a task module

A DBS task contains multiple modules. This topic describes how to manage a task module.
1. Log on to the DBS O&M console.
2. In the left-side navigation pane, choose **Tasks > All Tasks** or choose **Tasks > Abnormal**
**Tasks**.
3. Find the task that you want to manage and click the task name.
4. In the upper part of the **Task Details** page, the state of each module of the task is
displayed. The color of a module indicates the state of the module: Red: the Abnormal state. Blue: the Running state. Yellow: the Paused state. Green: the Complete or Not Delayed state.
5. Find a module and click **Details** to go to the management page of the module.
6. On the management page of the module, perform the following operations based on your
business requirements: The following list provides an example on how to manage the full backup module. The management operations of another module are the same as those in this example. You can go to the details page of each module to view specific management operations. On the **Basic Information** tab, you can restart, pause, skip, reset, or fail the module, or modify the memory of the running service node. On the **Migration Objects** tab, you can view information such as object type and migration status. On the **Operation History** tab, you can view the O&M operation records of the module. On the **Operation Logs** tab, you can view the operation logs of the module. You can also perform operations on the logs, such as pulling, tracking, previewing, and downloading.

## 4 Resource management

### 4.1 View DBS resources

This topic describes how to view the overview information of DBS resources. This helps you understand the status of DBS resources.
1. Log on to the DBS O&M console.
2. In the left-side navigation pane, choose **Resources > DBS Resources**.
On the DBS Resources page, information about all DBS resources is displayed. The information of a resource includes the region where the resource resides, CPU utilization, and memory usage. You can select the region where the resource resides in the top bar of the **DBS**
**Resources** page. Then, you can enter the resource IP and click **Search** to filter the
resource. You can click the trend icon in the **Network** column to filter a time range and view network traffic trends within the time range.

### 4.2 Unpublish DBS resources

This topic describes how to unpublish DBS resources in the DBS O&M console.
1. Log on to the DBS O&M console.
2. In the left-side navigation pane, choose **Resources > DBS Resources**.
3. Select one or more DBS resources and click **Unpublish Machine** below the DBS resource
list to unpublish the service node where the resources reside. Running service nodes are not allowed to go offline.

### 4.3 View DBS CIDR blocks

This topic describes how to view DBS CIDR blocks. This helps you obtain the IP addresses of regions and network types to which DBS servers belong, which enables you to troubleshoot DBS connectivity issues. For example, you can check whether the CIDR blocks of DBS servers in the same region and network type as a database instance or a self-managed database are added to an IP address whitelist of the instance or the firewall rules of the database.
1. Log on to the DBS O&M console.
2. In the left-side navigation pane, choose **Resources > DBS CIDR Blocks**.
By default, the CIDR blocks of all regions and network types are displayed. In the upper part of the CIDR block list page, specify a region and a network type. Then, click **Search** to filter CIDR blocks. Click the icon in the upper-right corner to copy the CIDR blocks.

## 5 Usage

### 5.1 View all subtasks in a backup plan

**plan**

This topic describes how to view all subtasks in a backup plan, including full backup tasks, incremental tasks, backup set download tasks, and restoration tasks. This helps you have a comprehensive insight into the overall operation of the backup plan.
1. Log on to the DBS O&M console.
2. Choose **Tasks > All Tasks**.
3. On the **Tasks** page, enter the ID of a backup plan in the upper-right corner and then click
**Search**.
To obtain the ID of a backup plan, log on to the Apsara Uni-manager Management Console, and then choose **Databases** > **DBS** in the top navigation pane to visit the DBS console. In the left-side navigation pane of the DBS console, click **Backup Plans** to visit the backup plan list page. On this page, you can obtain the ID of the backup plan that you want to manage.
4. Expand the task that you want to manage and then view all subtasks below the task.
5. Click the name of a subtask to go to the subtask details page. On this page, view specific
task nodule, such as the schema backup module, full backup module, and continuous incremental backup module.
6. Click **Details** next to a module to go to the module details page. On this page, view the
basic module information, backup objects, operation records, and operation logs. For more information about tasks and modules, see Manage tasks and Manage a module of a task.

### 5.2 Quickly view a full backup task or a backup set download task

**task or a backup set download**

**task**

In specific scenarios, you must view the running details of a full backup task or a backup set download task. This way, you can plan your business in a timely manner. This topic excludes traditional task viewing methods and describes a convenient and quick way.
1. Log on to the DBS O&M console.
2. Choose **Tasks > All Tasks**.
3. On the **Tasks** page, click a task name.
4. Replace the ID in your address bar with the ID of backup set or download task to be
queried. Then, press the Enter key. Method to obtain the ID of a backup set or a download task: i. Log on to the Apsara Uni-manager Management Console, and then choose
**Databases** > **DBS** in the top navigation pane to visit the DBS console.
ii. In the left-side navigation pane of the DBS console, click **Backup Plans** to visit the backup plan list page. On this page, click the name of the backup plan whose ID you want to obtain. You will be redirected to the backup plan details page. iii. In the left-side navigation pane of this page, choose **Backup Tasks > Full Data**
**Backup**. On the page that appears, copy the ID of the backup set that you want to
download. Alternatively, click **Backup Set Download** In the left-side navigation pane of the backup plan details page to copy the ID of a download task.

### 5.3 Manually restart a task

This topic describes how to manually restart a task.
1. Log on to the DBS O&M console.
2. In the left-side navigation pane, choose **Tasks > All Tasks** or choose **Tasks > Abnormal**
**Tasks**.
3. Find the task that you want to manage and click the task name.
4. On the **Task Details** page, click **Details** next to a task module.
The following list provides an example on how to manage the **Full Backup** module. The management operations of another module are the same as those in this example. You can go to the details page of each module to view specific management operations.
5. On the **Basic Information** tab of the page that appears, select **Restart** for **Status**.
If the task is abnormal, you must restart it.
