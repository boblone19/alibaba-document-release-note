---
title: "ApsaraStack Parallel File System User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 14
source_pdf: "15ec2af985e548d4_Alibaba Cloud Apsara Stack V3.18.6 ApsaraStack Parallel File System User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%AB%98%E6%80%A7%E8%83%BD%E5%B9%B6%E8%A1%8C%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8APFS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraStack%20Parallel%20File%20System%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# ApsaraStack Parallel File System User Guide 20260701

## Table of Contents

- 1 What is APFS?
- 2 Getting Started
  - 2.1 Log on to the APFS console
  - 2.2 Create an APFS file system
  - 2.3 Limits
- 3 APFS list
  - 3.1 Manage APFS file systems
  - 3.2 Scale up an APFS file system
  - 3.3 Resource monitoring
  - 3.4 Data flow
- 4 FAQ
  - 4.1 No inventory for sales

## 1 What is APFS?

**Overview**

ApsaraStack Parallel File System (APFS) is a cloud-defined, distributed parallel file system service. APFS delivers high performance that is required for large-scale parallel training in intelligent computing scenarios and offers features such as intelligent data management, reliable data security, flexible deployment, and elastic scaling of resources. AFPS applies to scenarios where Hygon DCUs, Ascend GPUs, and Hygon storage cluster are used.

## 2 Getting Started

### 2.1 Log on to the APFS console

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

> **Note:** **First login**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forgotten password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your login scenario: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA code and click **Authentication**. You have enabled and bound MFA: Enter the six-digit MFA code and click **Authentication**.

> **Note:** For more information about how to bind and enable MFA, see **Security Center** > **MFA** > **Manage MFA** in Apsara Uni-manager Operations Console User Guide.

5. In the top navigation bar, choose **Products > Storage > APFS** to go to the ApsaraStack
Parallel File System (APFS) console.

### 2.2 Create an APFS file system

1. Log on to the ApsaraStack Parallel File System (APFS) console.
2. On the APFS page, click **Create File System** in the upper-left corner.
3. On the Create File System page, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | From the drop-down list, select an organization for the file system. |
| Resource Set | From the drop-down list, select a resource set for the file system. |
| Geography | From the drop-down list, select a region for the file system. |
| Availability Zone | From the drop-down list, select a zone for the file system. |
| File System Type | Specify the type of the file system. By default, BMEFS is selected. |
| Cluster | Specify a cluster for the file system. |
| Specifications | Only Performance APFS file systems can be created. |
| Capacity (TiB) | Specify the capacity of the file system. Valid values: 1 to 1000. |
| Description | Enter a description for the file system. The description must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and colons (:). It _ must start with a letter. It cannot start with http:// or https://. |

4. Click **Submit**.
5. After a file system is created, you can view the status, specifications, and capacity of the
file system in the APFS list. To mount a file system, log on to the Bare Metal Computing Platform (BMCP) console. For more information, see the **Clusters and nodes** topic in
**BMCP User Guide**.

### 2.3 Limits

This topic describes the limits of ApsaraStack Parallel File System (APFS). Only performance APFS file systems are supported. The maximum total capacity of a Performance APFS file system is 25 PiB. You can only mount an APFS file system to a Bare Metal Computing Platform (BMCP) cluster in the BMCP console. By default, mount targets are automatically created. You cannot create additional mount targets. You must scale up APFS file systems when data is not read or written. Cluster scale-down is not supported.

## 3 APFS list

### 3.1 Manage APFS file systems

**View an APFS file system**

An ApsaraStack Parallel File System (APFS) file system is created. For more information, see Create an APFS file system.
1. Log on to the APFS console.
2. On the APFS page, you can search for a file system by **File System ID** or **File System**
**Name**.
3. On the APFS page, find the file system that you want to view, and click the
icon in the
**Monitoring** column to view monitoring metrics such as capacity, bandwidth, and
read/write IOPS of the file system.
4. On the APFS page, click a file system ID or click **Details** in the **Actions** column to view the
basic information about the file system.
5. On the **Basic Information** tab, you can view the ID, status, specifications, and capacity of
the file system.

**Delete an APFS file system**

Before you delete an APFS file system, the file system is unmounted from the mount target. Deleted APFS file systems cannot be restored. Make sure that you back up the data stored in an APFS file system before you delete it. After you delete an APFS file system, resources of the file system are not immediately released. The disk space occupied by the file system is released seven days later.
1. Log on to the APFS console.
2. On the APFS page, find the file system that you want to delete and click **Delete** in the
**Actions** column.
3. In the dialog box that appears, click **OK**.

**Modify the description of an APFS file system**

1. On the APFS page, find the file system for which you want to modify the description, move
the pointer over the **File System ID/Name** column, and click the icon.
2. In the dialog box that appears, enter a new description.
3. Then, click **OK**.

> **Note:** The description of the file system must be 2 to 128 characters in length and can contain letters, digits, underscores (_), hyphens (-), and colons (:). It must start with a letter. It cannot start with `http://` or `https://` .

### 3.2 Scale up an APFS file system

1. An ApsaraStack Parallel File System (APFS) file system is created. For more information, see
Create an APFS file system.
2. No data is being read from or written to the APFS file system.
1. Log on to the APFS console.
2. On the APFS page, find the file system that you want to scale up and click **Scale Up** in the
Actions column.
3. On the File system expansion page, select a value for the **Total new capacity (TiB)**
parameter.

> **Note:** The new total capacity cannot be lower than the current total capacity and cannot exceed the maximum total capacity. The maximum total capacity of a Performance APFS file system is 1 PiB.

4. Click **Submit** to complete the scale-up.

### 3.3 Resource monitoring

This topic describes how to view monitoring metrics and create alert rules for ApsaraStack Parallel File System (APFS) resources. An APFS file system is created. For more information, see Create an APFS file system.
1. Log on to the APFS console.
2. Click **APFS**, and then click the ID or name of a file system or click **Details** in the Actions
column to go to the File System Details page.
3. On the File System Details page, click the **Monitoring** tab in the upper-left corner to view
monitoring metrics such as capacity, bandwidth, and read/write IOPS of the file system.
4. You can also click the
icon in the upper-right corner of the chart to create an alert rule. For more information, see the **Create an alert rule** topic in **CloudMonitor User Guide**.
5. After an alert rule is created, you can choose **Products > Migration and O&M**
**Management > CloudMonitor** in the top navigation bar and click **Alert Service** in the
left-side navigation pane to view and manage the alert rule.

### 3.4 Data flow

This topic describes how to configure data replication between ApsaraStack Parallel File System (APFS) and Object Storage Service (OSS).

**Scenarios**

Data replication from APFS to OSS: The data stored in an APFS file system is replicated to an OSS bucket for data backup. Data that is infrequently accessed can be transferred to and stored in an OSS bucket to reduce storage costs. Data replication from OSS to APFS: OSS supports multiple data importing methods. You can use this feature to import data from on-premises databases or other systems into an OSS bucket, and then replicate the data from the OSS bucket to an APFS file system. This data replication method improves data transmission efficiency. You can replicate large amounts of data that was accumulated and stored in an OSS bucket to an APFS file system for AI training and other purposes. The Resource Access Management (RAM) role AliyunOSSPrivateCloudDrsSyncRole is granted to your organization. For more information, see the **Service-linked role** topic of
**Configurations** in **Apsara Uni-manager Management Console User Guide** .
1. Log on to the APFS console.
2. On the APFS page, click the ID or name of the file system for data replication or click
**Details** in the **Actions** column to go to the File System Details page. On the page that
appears, click the **Data Flow** tab to go to the data flow task page.

> **Note:** If the system detects that the current organization is not granted the RAM role AliyunOSSPrivateCloudDrsSyncRole, the **Authorize Access to Cloud Resources** dialog box appears when you go to the data flow task page. In this case, you can select an organization in the dialog box to complete the authorization.

3. Click **Create Data Flow Task**. In the Create Data Flow Task dialog box, configure the
parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Task Type | APFS > OSS: Data is replicated from APFS to OSS. OSS > APFS: Data is replicated from OSS to APFS. |

| Data Source | Instructions for filling parameters for data replication in which an OSS bucket is the data source or destination path: Select the bucket where the data is stored from the drop-down list. Specify the specific path of files that are stored in the bucket. For example: /source file/file01.txt _ Instructions for filling parameters for data replication in which an APFS file system is the data source or destination path: You need to specify the relative path of the destination file or directory under the default mount target. Note The default mount target of an APFS file system is /mnt/efs-xxx. For example, the default mount target of the file system efs-01d27e2c is /mnt/efs-01d27e2c. Path filling rules: File path: If the full path of the destination file is /mnt/efs-xxx/a.jpg, you need to enter a.jpg or /a.jpg. You only need to enter the part of the path that starts from the default mount target, with or without a forward slash (/). Directory path: If the full path of the destination directory is /mnt/efs-xxx/bigdir/dir1, you need to enter bigdir/dir1 or /bigdir/dir1. Similarly, you can choose whether to add a forward slash (/). Examples: For the destination file /mnt/efs-xxx/images/photo.png, you can enter images/photo.png or /images/photo.png. For the destination directory /mnt/efs-xxx/data/files, you can enter data/files or /data/files. Important Make sure that the path you enter is a path relative to the default mount point, not a full absolute path. If the path contains special characters, such as spaces and Chinese characters, escape them properly or enclose the path in quotation marks. |
|---|---|
| Destinatio n Path |   |
| Descriptio n | Enter the description of the data replication task. |

> **Note:** The amount of data for a single data flow task cannot exceed 100 TiB.

4. Click **OK** to submit the data replication task.
5. After a replication task is created, you can view relevant information of the replication task,
such as task status, task type, task result, data source, destination path, description, and creation time, in the data flow task list.

## 4 FAQ

This topic provides answers to frequently asked questions (FAQ) about ApsaraStack Parallel File System (APFS).

### 4.1 No inventory for sales

This topic describes solutions for the failure to create an ApsaraStack Parallel File System (APFS) file system due to insufficient inventory.

**Symptom**

When you create or scale up an APFS file system, the following exception message may appear.

**Solutions**

Solution 1: Decrease the capacity of the file system. Scenario 2: Modify the zone of the file system. Solution 3: Delete any redundant file system, contact the on-site O&M engineer to release disk space, and then create or scale up the file system again.
