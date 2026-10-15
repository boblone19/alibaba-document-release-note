---
title: "Elastic File System NAS User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 42
source_pdf: "efc8fa3846efea39_Alibaba Cloud Apsara Stack V3.18.6 Elastic File System NAS User Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%98%BF%E9%87%8C%E4%BA%91%E5%BC%B9%E6%80%A7%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20EFS-NAS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elastic%20File%20System%20NAS%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Elastic File System NAS User Guide 20260701

## Table of Contents

- 1 What is EFS-NAS?
- 2 Usage notes
- 3 Getting started
  - 3.1 Log in to the EFS-NAS console
  - 3.2 Create a file system
  - 3.3 Create a user
  - 3.4 Create a share
  - 3.5 Mount an NFS file system
  - 3.6 Mount an SMB file system
- 4 Manage file systems
  - 4.1 View the detailed information about a file system
  - 4.2 Resize a file system
  - 4.3 Delete a file system
  - 4.4 Share management
    - 4.4.1 Manage NFS shares
    - 4.4.2 Manage SMB shares
- 5 User and user group management
  - 5.1 Manage users
  - 5.2 Manage user groups
- 6 Recycle bin
  - 6.1 Enable the recycle bin feature
  - 6.2 Restore files from the recycle bin
  - 6.3 Manage the recycle bin
- 7 Snapshots
  - 7.1 Create a snapshot
  - 7.2 Manage snapshots
  - 7.3 Create a scheduled snapshot policy
- 8 WORM
  - 8.1 Create a WORM policy
  - 8.2 Modify a WORM policy

## 1 What is EFS-NAS?

**Product overview**

Apsara Stack Elastic File Storage-File Storage NAS (EFS-NAS) is a file storage service for compute nodes, such as Elastic Compute Service (ECS) instances, Elastic High Performance Computing (E-HPC) clusters, and Container Service for Kubernetes (ACK) clusters. EFS-NAS is a distributed file system that provides the following benefits: shared access, scalability, high reliability, and high performance. EFS-NAS provides standard file access protocols. You can use EFS-NAS without the need to modify the configurations of applications.

**Service types**

EFS-NAS supports capacity-optimized and compute-optimized instance types to meet different business scenarios. Capacity-based instance Based on hybrid servers with both Solid-State Drives (SSDs) and Hard Disk Drives (HDDs). Provides a large-capacity, cost-effective solution for shared file storage. Suitable for cost-sensitive scenarios such as records management, data archiving, and video surveillance playback. Performance-oriented instance Based on all-flash servers with SSDs. Provides high-throughput, low-latency file access. Suitable for performance-sensitive scenarios such as high-performance computing (HPC), media editing, and database file storage.

**Core features**

File system mounting: You can mount a file system to multiple clients. Elastic scale-out: You can scale out file systems online to dynamically adjust capacity as your business grows. Mount targets: You can create mount targets for sharing through the Network File System (NFS) or Server Message Block (SMB) protocol. Quota management: You can set capacity quotas for organizations to achieve efficient resource allocation, cost control, and performance optimization. Single namespace capacity: The system allows a maximum capacity of 5 PiB for unified management of massive data. Maximum scale of a single cluster: The system supports up to 2,000 disks and scale-out as needed. Three-server initial deployment: You can start with a small-scale deployment and scale out smoothly as your business grows. Flexible storage pool deployment: The system supports dedicated resources and flexible planning for the underlying file storage cluster, reducing the initial investment in hardware.

## 2 Usage notes

Before you use Apsara Stack Elastic File Storage-File Storage NAS (EFS-NAS), take note of the following limits.

**Limits on file systems**

Maximum number of files in a single file system: 10 billion. Maximum size of a single file: 512 TiB. We recommend that the size of a single file should not exceed 4 TiB. Maximum directory depth: unlimited. We recommend that the directory depth should not exceed 20 levels. Maximum directory width: 100,000. Capacity of a single file system: 1 GiB to 5 PiB. A file system can be simultaneously mounted on and accessed by up to 2,000 compute nodes.

**Other limits**

Before you delete a file system, you must unmount the file system from the mount target on the compute node. Then, delete the share and file system. Before you delete a user group, you must remove the user group from the Server Message Block (SMB) share. Before you delete a user, you must remove the user from the user group and SMB share.

## 3 Getting started

### 3.1 Log in to the EFS-NAS console

This topic describes how to log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.
1. In the address bar of your browser, enter the service domain name for the Apsara Uni-
manager Management Console and press Enter. You can click the current language in the upper-right corner to switch to another language.
2. Enter your username and password.
You can obtain the username and logon password from an operations administrator. If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %.
3. Select **I Have Read And Agree To The Product Service Agreement, Privacy**
**Agreement, And User Agreement**.
The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement. The **Product Service Agreement**, **Privacy Agreement**, and **User**
**Agreement** are displayed only if they have been published. If none of these
agreements are published, you can skip this step.
4. Click **Account Logon** or **Authorized Logon**.
The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon".
5. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of
the following scenarios: When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**.
6. In the top navigation bar, choose **Products** > **Storage** > **EFS-NAS File System**.

### 3.2 Create a file system

This topic describes how to create a file system in the Apsara Stack Elastic File Storage-File Storage NAS (EFS-NAS) console.
1. Log in to the EFS-NAS console.
2. On the **File System Management** page, click **Create File System**.
3. On the **Create File System** page, configure the following parameters.
After you complete the configuration, you can view the brief information about the configuration in the right-side section of the page.

| Parameter |   | Description |
|---|---|---|
| Basic Information | Organization/R esource Set | The organization and resource set to which the file system belongs. |
|   | Region/Zone | The region and zone to which the file system belongs. |
|   | Storage Class | Valid values: Capacity Type and Performance Type. Capacity Type: a hybrid-flash storage server based on SSDs and HDDs. This storage type provides a large-capacity, cost- optimized shared file storage solution. It is applicable to cost- sensitive scenarios such as archive management, data archiving, and video surveillance playback. Performance-oriented: an all-flash storage server based on SSDs. This storage type provides high-throughput and low- latency file access. It is applicable to performance-sensitive scenarios such as high-performance computing, media editing, and database file storage. |
|   | File System Name | Enter a name for the file system. The name must be 3 to 32 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It cannot start with a hyphen (-) _ or contain only digits. |
|   | NFS Version | Select the version of the NFS protocol. v3 and v4 are supported. |
|   | Description | Enter a description for the file system. |
| Storage Configurati on | Total Capacity (GiB) | Enter the total capacity of the file system. Valid values: 1 to 5242880. Unit: GiB. |

4. Optional. If you want to set quotas for the resources of a service, click **Quota**
**Management** on the right side of the page to go to the **Quotas** page. For more
information, see the **Quota management** topic in User Guide - Apsara Uni-manager Mana gement Console.
5. Click **Submit**.

### 3.3 Create a user

This topic describes how to create a user.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation pane, click **User Group**.
3. Click **Create User** above the list and configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Region | Select a region. |
| uid | Enter the UID of the user. Valid values: 10000 to 999999999. Note UIDs are globally unique. |
| Username | Enter a username. |
| Password | Enter a password. |
| Confirm password | Enter the password again. |

4. Click **Submit** to create a user.

### 3.4 Create a share

In Apsara Stack Elastic File Storage-File Storage NAS (EFS-NAS), you must use a share to mount a file system on a compute node. This topic describes how to create shares.

**Prerequisites**

A file system is created. For more information, see Create a file system. A virtual private cloud (VPC) and a vSwitch are created. For more information, see the
**Create a VPC** and **Create a vSwitch** topics in **VPC User Guide**.

**Create a Network File System (NFS) share**

1. Log in to the EFS-NAS console.
2. On the File System Management page, find the file system that you want to manage, move
your pointer over **Create Share** in the Operation column, and then select **NFS Share**.
3. On the **Create NFS Share** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). It cannot start with a hyphen (-) or contain only digits. Note After an NFS share is created, the name cannot be changed. Exercise caution when you perform this operation. |
| VPC | Select the authorized VPC. |
| VSwitch | Select a vSwitch in the authorized VPC. Only clients in the vSwitch can access the file system through the share. |

4. Click **Submit**.
5. Configure client access permissions.
i. Click the ID or name of the file system or click **Details** in the Actions column to go to the details page of the file system. ii. In the upper-left corner of the **NFS Share** page, click **Client IP Details**. iii. In the **Client IP Details** dialog box, click **Add** and configure the following parameters:
**Type**: Select IP/Network Segment or All.
**Client IP**: This parameter is available only when the Type parameter is set to
IP/Network Segment. Enter the IP addresses or CIDR blocks of clients that are allowed to access the share.
**Permission**: Select Read-Only or Read/Write.
**Enable Root Anonymity**: After you turn on this switch, the root user of a remote client
is automatically mapped to an anonymous user. This prevents the root user from having the superuser permissions on the server. When the client writes a file to the server as the root user, the file owner on the server becomes nobody, not the root user.
**Enable All Anonymity**: If you turn on this switch, all client users are mapped to
anonymous users. All file operations are performed as anonymous users, and the original user information cannot be retained.
**Operation**: Delete the rule.
iv. Click **OK**.

**Manage SMB shares**

1. Log in to the EFS-NAS console.
2. On the File System Management page, find the file system that you want to manage, move
your pointer over **Create Share** in the Operation column, and then select **SMB Share**.
3. On the **Create SMB Share** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). It cannot start with a hyphen (-) or contain only digits. Note After an SMB share is created, the name cannot be changed. Exercise caution when you perform this operation. |
| VPC | Select an authorized VPC. Only clients in the VPC can access the file system through the share. |
| VSwitch | Select an authorized vSwitch. Only clients in the vSwitch can access the file system through the share. |
| User (Group) | Configure users who are authorized to access the file system through the share. Click New and configure the following parameters: User Group: allows you to grant permissions by user, user group, or all users. User: This parameter is required if you set the User Group parameter to User. Select authorized users from the drop-down list. User Group: This parameter is required if you set the User Group parameter to User Group. Select authorized user groups from the drop-down list. Permissions: Reading & Writing: You can read and write objects, including viewing content, modifying data, and changing attributes. The delete, execute, rename, or permission management operations are not supported. Read Only: You can view object content, read attributes, and read permissions. However, you cannot perform modify, write, delete, or execute operations. Read-Write (Delete Prohibited): You can read and write objects, and modify file data and attributes. You cannot delete objects or change their permissions or owners. Full Control: You can perform all operations on objects. For example, you can read, write, execute, delete, rename, and move objects, modify permissions (ACLs), and take ownership. Prohibited: prohibits any operation. |

| Does it distinguish between uppercase and lowercase? | Business systems are generally case-insensitive, and you do not need to turn on this switch. If sharing and interconnection among multiple OSs are involved, turn on this switch. After you turn on this switch, the performance can be improved. |
|---|---|
| Enable ABE? | After you turn on Access-Based Enumeration (ABE), only the shared files and directories to which the user has access permissions are displayed. This ensures data access security. |
| Enable Opportunity Locking? | An opportunistic lock is a temporary locking mechanism granted by a server to a client. It is designed to significantly improve file access performance, especially in environments with high network latency. After you turn on this switch, clients can exclusively access shared files for a period of time to reduce frequent access to the file server and network transfers. However, this may cause some issues, such as conflicts in concurrent file access. Exercise caution when you turn on this switch. |

4. After you complete the configuration, click **Submit**.

### 3.5 Mount an NFS file system

After you create a Network File System (NFS) share, you can use a mount target to mount an NFS file system on a compute node. This topic describes how to mount an NFS file system.

**Prerequisites**

A file system is created. For more information, see Create a file system. An NFS share is created. For more information, see Create an NFS share.

**Step 1: Install an NFS client**

Before you mount an NFS file system on a Linux Elastic Compute Service (ECS) instance, you must install an NFS client. If an NFS client is installed, skip this step.
1. Log in to a Linux ECS instance. For more information, see the **Connect to an instance**
section of the **Get started** topic in **ECS User Guide**.
2. Install an NFS client.
If CentOS, Red Hat Enterprise Linux (RHEL), or Alibaba Cloud Linux is running on the ECS instance, run the following command to install the NFS client:

```python
sudo yum install nfs-utils
```

If Ubuntu or Debian is running on the ECS instance, run the following commands to install the NFS client:

```python
sudo apt-get update sudo apt-get install nfs-common
```

**Step 2: Mount an NFS file system**

1. Log in to the Linux ECS instance. For more information, see the **Connect to an instance**
section of the **Get started** topic in **ECS User Guide**.
2. Mount the NFS file system.
You can log in to the EFS-NAS console to view the mount command. For more information, see View NFS share information. Sample mount commands: Mount a file system by using NFSv4.1:

```python
sudo mount -t nfs -o vers=4.1,async,rsize=1048576,wsize=1048576 192.0.2.1:/efs-nasxxxxx /mount_point
```

Mount a file system by using NFSv4.0:

```python
sudo mount -t nfs -o vers=4.0,minorversion=0,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvpo 192.0.2.1:/efs-nas-xxxxx /mount_point
```

Mount a file system by using NFSv3:

```
mount -t nfs -o vers=3,tcp,nolock,async,mountproto=tcp,rsize=1048576,wsize=1048576 192.0.2.1:/efs-nas-xxxxx /mount_point
```

Table 1. Parameters in the mount command

| Parameter | Description |
|---|---|
| vers | The protocol version. NFSv3, NFSv4.0, and NFSv4.1 are supported. vers=3: uses NFSv3 to mount the file system. vers=4.0: uses NFSv4.0 to mount the file system. vers=4.1: uses NFSv4.1 to mount the file system. |

| Mount options | When you mount a file system, you can specify multiple mount options. Separate multiple mount options with commas (,). The following mount options are available: rsize: specifies the size of each data block that a client can read from the file system. This option is used to read data between the client and the file system. Recommended value: 1048576. Unit: bytes. wsize: specifies the size of each data block that a client can write to the file system. This option is used to write data between the client and the file system. Recommended value: 1048576. Unit: bytes. Note To prevent performance degradation, we recommend that you set both the rsize and wsize parameters to 1048576. hard: specifies that applications stop accessing a file system when the file system is unavailable, and wait until the file system becomes available. We recommend that you specify this mount option. timeo: specifies the period in deciseconds (tenths of a second) for which the NFS client waits before the NFS client retries a request. Recommended value: 600 (60 seconds). Note If you need to modify the timeo parameter, we recommend that you specify 150 or a greater value. The timeo parameter is measured in deciseconds (tenths of a second). For example, the value 150 indicates 15 seconds. retrans: specifies the number of times that the NFS client retries a request. Recommended value: 2. noresvport: specifies that a new TCP port is used to ensure network continuity between the file system and the ECS instance when the network recovers from a failure. We recommend that you specify this mount option. Note When you configure parameters, take note of the following items: To prevent data inconsistency, we recommend that you do not use the soft mount option. If you specify the soft mount option, make sure that you understand the potential risks. We recommend that you do not set any other mount options that are different from the defaults. A decrease in performance may occur due to changes in specific mount options. These mount options include the size of the read or write buffer or the use of attribute caching. |
|---|---|

3. Run the `mount -l` command to view the mount result.
If a command output similar to the following example appears, the file system is mounted. After the file system is mounted, you can run the `df -h` command to view the size of the file system.
4. After the file system is mounted, you can read data from and write data to the NAS file
system on the ECS instance.

### 3.6 Mount an SMB file system

After you create a Server Message Block (SMB) share, you can use a mount target to mount an SMB file system on a compute node. This topic describes how to mount an SMB file system.

**Prerequisites**

A file system is created. For more information, see Create a file system. An SMB share is created. For more information, see Create an SMB share.
1. Log in to a Windows ECS instance. For more information, see the **Connect to an instance**
section of the **Get started** topic in **ECS User Guide**.
2. Start the following services on the Windows host:
Workstation a. Open the Windows Start menu. Choose **All Programs > Accessories > Run**. Alternatively, press `Win+R` , enter `services.msc` , and then press Enter to open the Services window. b. Make sure that the Workstation service is in the **Started** state and the startup type is
**Automatic**.
By default, the Workstation service is in the Started state. TCP/IP NetBIOS Helper To start the TCP/IP NetBIOS Helper service, perform the following steps: a. On the **Network and Sharing Center** page, click the active network connection. b. Select **Properties**. In the Connection Properties dialog box, double-click **Internet**
**Protocol Version 4 (TCP/IPv4)**. In the Internet Protocol Version 4 (TCP/IPv4)
Properties dialog box, click **Advanced**. c. In the **Advanced TCP/IP Settings** dialog box, choose **WINS > Enable NetBIOS over**
**TCP/IP**.
d. Open the Windows Start menu. Choose **All Programs > Accessories > Run**. Alternatively, press `Win+R` , enter `services.msc` , and then press Enter to open the Services window. e. Make sure that the TCP/IP NetBIOS Helper service is in the **Started** state and the startup type is **Automatic**. By default, the TCP/IP NetBIOS Helper service is in the Started state.
3. Open the Command Prompt and run the following command to mount the SMB file system:
Command syntax: `net use <Letter of the destination drive> <Domain name of the mount` `target> /user:[Username]` . Example:

```
net use D: \\192.0.2.1\smb-share /user:test-user
```

Letter of the destination drive: the letter of the drive on which you want to mount the SMB file system. Replace the value of the parameter with the letter of an actual destination drive. The letter of the destination drive must be different from the existing drive letters. Domain name of the mount target: When you create a mount target for a file system, the domain name of the mount target is automatically generated. You can replace the domain name based on your business requirements. In the EFS-NAS console, find the file system that you want to manage and click **Details** in the Operation column. On the details page of the file system, click the **SMB Share** tab to view the **Mount Command** column of a share. Username: the user who is authorized to access the file system when you create the SMB share. In the EFS-NAS console, find the file system that you want to manage, and click
**Details** in the Operation column. On the details page of the file system, click the **SMB**
**Share** tab, find the share that you want to view, and then choose **Edit > Add User**
**(Group)** in the Operation column to view or edit the authorized users or user groups.
4. Run the `net use` command to check the mount result.
5. After the file system is mounted, you can read data from and write data to the NAS file
system on the ECS instance.

## 4 Manage file systems

### 4.1 View the detailed information about a file system

**about a file system**

This topic describes how to view the detailed information about a file system.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. The file system list displays the basic information about each file system, including the
status, usage and total capacity, cluster, storage type, label, NFS version, organization and resource set, creator, and creation time.
3. You can click the ID of a file system or click Details in the Operation column to go to the
details page. On the details page, you can view NFS and SMB shares. For more information, see Share management.

### 4.2 Resize a file system

This topic describes how to resize a file system.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the file system list, click the
icon in the Operation column of the target file system and click **Modify Total Capacity**.
3. On the **Modify Total Capacity** page, you can view the current total capacity of the file
system. Enter a value for **New Total Capacity (GiB)**. The new capacity must be greater than the current capacity.
4. Click **Submit**.

### 4.3 Delete a file system

This topic describes how to delete a file system.

**Prerequisites**

The file system that you want to delete is unmounted from the mount target of the corresponding computing node, such as an Elastic Compute Service (ECS) instance. All shares are deleted.

**Warning**

After you delete a file system, the file system can no longer be restored. Proceed with caution and back up the data in the file system before you begin.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the file system, click the
icon in the Operation column of the target file system and click **Delete**.
3. In the message that appears, click **OK**.

### 4.4 Share management

Elastic File Storage-File Storage NAS (EFS-NAS) supports the Network File System (NFS) and Server Message Block (SMB) file access protocols, which allow you to access shared, elastic, highly reliable, and high-performance distributed file systems through shares without making any changes to your applications.

#### 4.4.1 Manage NFS shares

This topic describes the operations that you can perform to manage Network File System (NFS) shares.

**Create a Network File System (NFS) share**

1. Log in to the EFS-NAS console.
2. On the File System Management page, find the file system that you want to manage, move
your pointer over **Create Share** in the Operation column, and then select **NFS Share**.
3. On the **Create NFS Share** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). It cannot start with a hyphen (-) or contain only digits. Note After an NFS share is created, the name cannot be changed. Exercise caution when you perform this operation. |
| VPC | Select the authorized VPC. |
| VSwitch | Select a vSwitch in the authorized VPC. Only clients in the vSwitch can access the file system through the share. |

4. Click **Submit**.
5. Configure client access permissions.
i. Click the ID or name of the file system or click **Details** in the Actions column to go to the details page of the file system. ii. In the upper-left corner of the **NFS Share** page, click **Client IP Details**. iii. In the **Client IP Details** dialog box, click **Add** and configure the following parameters:
**Type**: Select IP/Network Segment or All.
**Client IP**: This parameter is available only when the Type parameter is set to
IP/Network Segment. Enter the IP addresses or CIDR blocks of clients that are allowed to access the share.
**Permission**: Select Read-Only or Read/Write.
**Enable Root Anonymity**: After you turn on this switch, the root user of a remote client
is automatically mapped to an anonymous user. This prevents the root user from having the superuser permissions on the server. When the client writes a file to the server as the root user, the file owner on the server becomes nobody, not the root user.
**Enable All Anonymity**: If you turn on this switch, all client users are mapped to
anonymous users. All file operations are performed as anonymous users, and the original user information cannot be retained.
**Operation**: Delete the rule.
iv. Click **OK**.

**View NFS share information**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. On the **NFS Share** tab, you can view the name, status, network information, mount target,
and mount command of each NFS share.
4. Click **Client Ip Details** above the list to view or modify the client IP addresses that are
allowed to access the file system.
5. Click **Connection Details** above the list to view the client IP addresses that are connected
to the file system and the NFS versions that are used.

**Delete an NFS share**

Before you delete an NFS share, make sure that no client uses the share to connect to the corresponding file system.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. On the **NFS Share** tab, find the target share and click **Delete** in the Operation column.
4. In the message that appears, click **OK**.

#### 4.4.2 Manage SMB shares

This topic describes the operations that you can perform to manage Server Message Block (SMB) shares.

**Manage SMB shares**

1. Log in to the EFS-NAS console.
2. On the File System Management page, find the file system that you want to manage, move
your pointer over **Create Share** in the Operation column, and then select **SMB Share**.
3. On the **Create SMB Share** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). It cannot start with a hyphen (-) or contain only digits. Note After an SMB share is created, the name cannot be changed. Exercise caution when you perform this operation. |
| VPC | Select an authorized VPC. Only clients in the VPC can access the file system through the share. |
| VSwitch | Select an authorized vSwitch. Only clients in the vSwitch can access the file system through the share. |
| User (Group) | Configure users who are authorized to access the file system through the share. Click New and configure the following parameters: User Group: allows you to grant permissions by user, user group, or all users. User: This parameter is required if you set the User Group parameter to User. Select authorized users from the drop-down list. User Group: This parameter is required if you set the User Group parameter to User Group. Select authorized user groups from the drop-down list. Permissions: Reading & Writing: You can read and write objects, including viewing content, modifying data, and changing attributes. The delete, execute, rename, or permission management operations are not supported. Read Only: You can view object content, read attributes, and read permissions. However, you cannot perform modify, write, delete, or execute operations. Read-Write (Delete Prohibited): You can read and write objects, and modify file data and attributes. You cannot delete objects or change their permissions or owners. Full Control: You can perform all operations on objects. For example, you can read, write, execute, delete, rename, and move objects, modify permissions (ACLs), and take ownership. Prohibited: prohibits any operation. |

| Does it distinguish between uppercase and lowercase? | Business systems are generally case-insensitive, and you do not need to turn on this switch. If sharing and interconnection among multiple OSs are involved, turn on this switch. After you turn on this switch, the performance can be improved. |
|---|---|
| Enable ABE? | After you turn on Access-Based Enumeration (ABE), only the shared files and directories to which the user has access permissions are displayed. This ensures data access security. |
| Enable Opportunity Locking? | An opportunistic lock is a temporary locking mechanism granted by a server to a client. It is designed to significantly improve file access performance, especially in environments with high network latency. After you turn on this switch, clients can exclusively access shared files for a period of time to reduce frequent access to the file server and network transfers. However, this may cause some issues, such as conflicts in concurrent file access. Exercise caution when you turn on this switch. |

4. After you complete the configuration, click **Submit**.

**View SMB share information**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. Click the **SMB Share** tab. On this tab, you can view the name, status, network information,
mount target, and mount command of each SMB share.

**Modify an SMB share**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. Click the **SMB Share** tab.
4. Find the target SMB share and choose **Edit > Add User (Group)** to add, modify, or delete
user access permissions.
5. Choose **Edit > Set Advanced Options** in the Operation column to enable or disable **Case**
**Sensitive**, **ABE**, and **Opportunity Lock**.

**Delete an SMB share**

Before you delete an SMB share, make sure that no client uses the share to connect to the corresponding file system.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. On the **SMB Share**, find the target SMB share and click **Delete** in the Operation column.
4. In the message that appears, click **OK**.
ment

## 5 User and user group management

**management**

### 5.1 Manage users

This topic describes how to manage users in the Elastic File Storage-File Storage NAS (EFS- NAS) console.

**Background information**

SMB shares in EFS-NAS allow you to manage user permissions. You can grant read and write permissions, read-only permissions, and full permissions to different users in order to ensure data access security.

**Create a user**

1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. On the **User** tab, click **Create User** and configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Region | Select a region. |
| uid | Enter the UID of the user. Valid values: 10000 to 999999999. Note UIDs are globally unique. |
| Username | Enter a username. |
| Password | Enter a password. |
| Confirm password | Enter the password again. |

4. Click **Submit** to create a user.

**Change the password**

1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
ment
3. On the **User** tab, find the target user and click **Update Password** in the Operation column.
4. Enter the new password, confirm the password, and click **OK**.

**Delete a user**

Before you delete a user, you must remove the user from SMB shares and user groups.
1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. On the **User** tab, find the target user and click **Delete** in the Operation column.
4. In the message that appears, click **OK**.

### 5.2 Manage user groups

This topic describes how to manage user groups in the Elastic File Storage-File Storage NAS (EFS-NAS) console.

**Background information**

SMB shares in EFS-NAS allow you to create user groups to manage users. You can select user groups when granting permissions to users to simplify permission management.

**Create a user group**

1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. Click the **User Group** tab and click **Create User Group** above the list.
4. Configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Region | Select a region. |
| User Group ID | Enter the ID of the user group. Valid values: 10000 to 999999999. Note User group IDs are globally unique. |
| User Group Name | Enter the name of the user group, which must not start with a digit. |

ment

| User Group Members | Select members. Note We recommend that you do not add more than 4,096 members to a user group. |
|---|---|

5. Click **Submit** to create a user group.

**View the details of a user group**

1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. Click the **User Group** tab. In the list, click the name of a user group or click **Details** in the
Operation column to go to the details page. On the details page, you can view the members in the user group and their regions.

**Modify members**

1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. Click the **User Group** tab, find the target user group, and click **Update Members** in the
Operation column.
4. Add or remove members and click **OK**.

**Delete a user group**

Before you delete a user group, you must remove the user group from SMB shares.
1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. Click the **User Group** tab, find the target user group, and click **Delete** in the Operation
column.
4. In the message that appears, click **OK**.

## 6 Recycle bin

If you accidentally delete files from an File Storage NAS (NAS) file system, your business may be interrupted or your data may be permanently lost. To prevent these issues, we recommend that you enable the recycle bin feature. After the recycle bin feature is enabled, deleted files and directories are temporarily stored in the recycle bin. You can also configure a retention policy to specify a time period for files in the recycle bin before they are permanently deleted. During the data retention period, you can restore these files and directories and their metadata such as user identifiers (UIDs), group identifiers (GIDs), and access control lists (ACLs).

**Background information**

If you enable the recycle bin feature, the deleted files and directories are temporarily stored in the recycle bin, including the following files and directories: The files that you deleted from EFS-NAS file systems on compute nodes, such as Elastic Compute Service (ECS) instances and containers. For example, if you run the `rm -f` `test01.text` command to delete the test01.text file, the test01.text file is dumped to the recycle bin. The files or directories that are automatically deleted by applications from EFS-NAS file systems on compute nodes. For example, if an application runs the `os.remove("test02.text")` Python code to delete the test02.text file, the test02.text file is dumped to the recycle bin. The files or directories that are deleted when you call the POSIX rename function. For example, the test_a.txt file and the test_b.txt file reside in the same directory. If you run the `mv test_a.txt test_b.txt` command, the test_b.txt file is dumped to the recycle bin. The temporary files that are generated by EFS-NAS file systems. For example, if you run the
**vim** command to edit a file, the `.swp` and `.swpx` temporary files are dumped to the
recycle bin. The application log files that are automatically rotated. For example, if you use NGINX to configure automatic log rotation, up to 20 log files can be retained. If the test.log.19 log file is rotated to the test.log.20 log file, the original test.log.20 log file is dumped to the recycle bin. If you overwrite a file but do not delete the file, the file is not dumped to the recycle bin. For example, if you call the open() function to open a file and write data to the file in w+ mode, the original file is not dumped to the recycle bin.

### 6.1 Enable the recycle bin feature

After you enable the recycle bin feature, deleted files are automatically added to the recycle bin. If you configure a retention policy, files in the recycle bin are permanently deleted when the specified retention period ends.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation pane, click **Recycle Bin**.
3. Click **Enable** in the upper-left corner. In the **Enable Recycle Bin** dialog box, configure the
parameters.

| Parameter | Description |
|---|---|
| Select a file system | Select the file system for which you want to enable the recycle bin feature. |
| Retention Plan | Valid values: Custom and Permanent retention. |
| Custom Retention Policy | If you select this option, you must configure the parameters of the retention policy. Specify the number of days for which files are retained in the recycle bin. Valid values: 1 to 365. |
| Filter Rules | Optional. Enter filtering rules, such as *.tmp. Separate multiple filter rules with commas (,). You can set the prefix or suffix to filter out files that do not need to be recycled. Files that match the filtering rules are not added to the recycle bin. Important Do not configure nested rules, such as *ab and *b or cd* and c*. |

4. Click **OK**.

### 6.2 Restore files from the recycle bin

**bin**

You can restore files from the recycle bin within the retention period that you specify.

**Usage notes**

You can restore only one file or directory in a single restore operation. If you restore a specified directory, all files in the directory are recursively restored. After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation pane, click **Recycle Bin**.
3. Click the ID of a file system to go to the **Recycle Bin Details** page.
4. Find the file that you want to restore and click **Recovery** in the Actions column.
The file list displays at most 100 data entries. If the file that you want to restore is not displayed in the list, enter the file name in the search box at the top of the page to search for the file. The current directory and the directory that starts with ~archive in the recycle bin are system directories that cannot be directly restored or deleted. Recycled files are stored in the current directory and then archived to the directory that starts with the ~archive for a period of time. You can select multiple files to be restored, click **Batch Recovery** in the lower part of the page, and then click **OK**.
5. In the **Confirm recovery?** dialog box, turn on or turn off **Overwrite a file with the same**
**name** and click **OK**.

### 6.3 Manage the recycle bin

You can delete files from the recycle bin, modify the retention policy of the recycle bin, empty the recycle bin, and disable the recycle bin.

| Operation | Description | Procedure |
|---|---|---|
| Permanently delete files from the recycle bin | If a file in the recycle bin is no longer used, you can permanently delete the file. Warning Files that are permanently deleted from the recycle bin cannot be restored. | 1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to manage and click the file system ID to go to the recycle bin details page. 4. Find the file that you want to delete and click Delete in the Actions column. You can select multiple files and click Batch Deletion below the list to delete the files at the same time. 5. Confirm the information and click OK. |
| Modify a retention policy | You can change the retention period of files at any time based on the usage of the file system. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to modify and click Modify Retention Plan in the Actions column. 4. In the Modify Retention Plan dialog box, modify the Retention Plan and Custom Retention Policy parameters. 5. Click OK. |

| Configure filtering rules | You can specify a prefix or a suffix to filter out files that do not need to be recycled. Files that match the filtering rules are not added to the recycle bin. Important Do not configure nested rules, such as *ab and *b or cd* and c*. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to manage and click Set Filtering Rules in the Actions column. 4. In the Set Filtering Rules dialog box, enter a prefix or suffix, such as *.tmp. 5. Click OK. |
|---|---|---|
| Clear the recycle bin | If you no longer use the files in the recycle bin, you can empty the recycle bin to reduce storage costs. Warning If you empty the recycle bin, all files in the recycle bin are permanently deleted and cannot be restored. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to manage, click the icon in the Actions column, and then select Clear Recycle Bin. 4. Check the information and click OK. |
| Disable the recycle bin feature | If you no longer need to use the files in the recycle bin or you no longer want to use the recycle bin feature, you can disable and empty the recycle bin. Warning If you disable the recycle bin, all files in the recycle bin are permanently deleted. If you disable and then enable the recycle bin again, the recycle bin is empty. The deleted files cannot be restored. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to manage, click the icon in the Actions column, and then select Close Recycle Bin. 4. Check the information and click OK. |

## 7 Snapshots

To prevent data loss caused by accidental operations, attacks, or viruses, you can use snapshots to periodically back up business data stored in file systems. To ensure the integrity and recoverability of data stored in an Elastic File Storage-File Storage NAS (EFS-NAS) file system, the system provides the snapshot feature. It allows you to create a read-only replica of the state of a file system at a certain point in time. Snapshots are classified into regular snapshots and scheduled snapshots, which can meet diverse data protection requirements. The differences between normal snapshots and scheduled snapshots are as follows: Normal snapshots: manually created by users. They are suitable for instant backup before important operations, such as system upgrades, configuration changes, and data migration. Scheduled snapshots: periodically generated by the system based on the scheduled snapshot policy. Scheduled snapshots are suitable for routine backup of important directories in a production environment to meet long-term protection requirements, such as legitimate data retention, prevention of accidental deletion, and automated O&M. We recommend that you formulate a tiered backup policy based on the actual business scenarios to balance security and resource costs.

### 7.1 Create a snapshot

Elastic File Storage-File Storage NAS (EFS-NAS) supports normal snapshots and scheduled snapshots. Normal snapshots are manually created by users on demand. Scheduled snapshots are automatically created by the system based on the scheduled snapshot policy. This topic describes how to create a snapshot for a file system.

**Usage notes**

A file system can have no more than 16 path levels. The path length of a normal snapshot must not exceed 4096, and the path length of a scheduled snapshot must not exceed 4047. We recommend that you retain 128 snapshots for a single file system. A maximum of 2,048 snapshots can be created. A maximum of 8,192 snapshots can be created for all file systems. If no snapshots are created for a file system, you cannot create another snapshot for the file system. We recommend that you create snapshots at an interval of more than 10 minutes. A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot. You can associate a maximum of eight scheduled snapshot policies with a single file system.If you associate different scheduled snapshot policies with a single file system,all the associated scheduled snapshot policies take effect on the file system.
1. Log in to the EFS-NAS console.
2. In the left-side navigation pane, click **Snapshot**.
3. On the **Directory Snapshot** tab of the **Snapshot** page, click **Create Snapshot**.
4. On the **Create Directory Snapshot** page, configure the following parameters.

**Normal snapshot configuration**

| Parameter | Description |
|---|---|
| Organization | The organization and resource set to which the file system belongs. |
| Resource Set |   |
| Region | The region to which the file system belongs. |
| Catalog | The file system for which you want to create a snapshot. |
| Snapshot Type | Select Manual Snapshot. |
| Name | Enter a name for the snapshot. The name must be 1 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |
| Description | Optional. Enter a description for the snapshot, such as the purpose of the snapshot or the context in which the snapshot is created. |
| Expiration Deletion | You can select Custom or Never Delete. Custom: Specify a snapshot retention period. If a snapshot expires and is not locked, the snapshot is automatically deleted. Never Delete: The system does not automatically delete the snapshot. |
| Custom Deletion Policy | This parameter is required if you set the Expiration Deletion parameter to Custom. Enter a value and select Hours, Days, Months, or Years to specify a file retention period. |
| Locked | Optional. After the snapshot is locked, it cannot be deleted. Note If you lock a snapshot, the snapshot is not automatically deleted even when the custom retention period ends. The snapshot can be deleted only after it is unlocked. |

**Scheduled snapshot configuration**

Before you create a scheduled snapshot, make sure that a scheduled snapshot policy is created. For more information, see Create a scheduled snapshot policy.

| Parameter | Description |
|---|---|
| Organization | The organization and resource set to which the file system belongs. |
| Resource Set |   |
| Region | The region to which the file system belongs. |
| Catalog | The file system for which you want to create a snapshot. |
| Snapshot Type | Select Scheduled Snapshot. |
| Description | Optional. Enter a description for the snapshot, such as the purpose of the snapshot or the context in which the snapshot is created. |
| Scheduling Policy | Select a scheduled snapshot policy for the file system. |
| First Snapshot | Specify the method used to create the first snapshot. Comply with Policy: The first snapshot is created based on the scheduled snapshot policy. Run Now: The first snapshot is created immediately. |

5. Click **Submit**.

**What to do next**

After a snapshot is created, you can restore files based on the snapshot and manage the snapshot.
**Restore files based on snapshots**: If a file is lost, find the directory of the corresponding
snapshot on an EFS-NAS cluster node and manually restore the file from the snapshot. If you want to restore files, contact Apsara Stack technical support. Manage snapshots: You can view and delete snapshots based on your business requirements.

### 7.2 Manage snapshots

After a snapshot is created, you can view the snapshot information, modify the snapshot attributes, lock or unlock the snapshot, and delete the snapshot.

| Operation | Description | Procedure |
|---|---|---|

| Query snapshot information | After a snapshot is created, you can view the organization, resource set, status, lock status, and expiration time of the snapshot. | 1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, view the detailed information about snapshots. |
|---|---|---|
| Modify snapshot attributes | You can modify the attributes of a snapshot based on its usage, including the snapshot name, description, expiration policy, expiration time, and lock status. Important You can modify the attributes of only normal snapshots. To modify a scheduled snapshot policy, see Create a scheduled snapshot policy. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, find the desired snapshot in the list and click Modify in the Operation column. 4. In the Modify Snapshot Policy dialog box, modify the attributes of the snapshot. 5. Click OK. |
| Lock or unlock a snapshot | You can lock snapshots used for long- term businesses. Locked snapshots cannot be deleted. To delete a locked snapshot, unlock it first. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, unlock or lock the desired snapshot. Lock a snapshot: Select the snapshot that you want to lock and click Lock below the list. In the message that appears, click OK. Unlock a snapshot: Select the snapshot that you want to unlock and click Unlock below the list. In the message that appears, click OK. |

| Delete a snapshot | If you no longer use a snapshot, you can delete it. Important Unlocked snapshots cannot be deleted. To delete an unlocked snapshot, unlock it first. For more information, refer to the steps for locking and unlocking snapshots. Deleted snapshots cannot be restored. Proceed with caution. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, use one of the following methods to delete snapshots. Delete a single snapshot: Click Delete in the Operation column of the snapshot. In the message that appears, click OK. Delete multiple snapshots at a time: Select the snapshots that you want to delete and click Delete in the Operation column. In the message that appears, click OK. |
|---|---|---|

### 7.3 Create a scheduled snapshot policy

**policy**

You can create a scheduled snapshot policy and then associate it with a file system to create snapshots at the scheduled time.

**Usage notes**

You can create a maximum of 128 scheduled snapshot policies. You can associate a maximum of eight scheduled snapshot policies with a single file system. Scheduled snapshot policies can be applied to any file systems within the selected organization, resource set, and region. Before you configure a policy, assess the cluster storage capacity and backup needs to avoid resource waste or performance degradation.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation pane, click **Snapshot**.
3. On the **Scheduled Snapshot Policy** tab of the **Snapshot** page, click **Create**
**SnapshotPolicy**.
4. On the **Create Scheduled Policy** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | The organization and resource set to which the scheduled snapshot policy belongs. |
| Resource Set |   |
| Region | The region to which the scheduled snapshot policy belongs. |

| Name | The name of the scheduled snapshot policy. The name must be 1 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). _ |
|---|---|
| Description | Optional. Enter a description for the policy, such as the purpose of the policy or the context in which the policy is created. |
| Snapshot Cycle | The snapshot generation cycle. You can select Daily, Weekly, or Monthly. If you select Weekly, specify the days of a week. If you select Monthly, specify the days of a month. |
| Snapshot Point in Time | The point in time at which a snapshot is automatically generated. Time Period: The system automatically generates snapshots within the specified time range. If you have specified an interval in minutes, the system will generate a snapshot at the specified interval every hour. Point in Time: The system automatically generates snapshots at the specified point in time. You can specify only specific hours, and you can specify multiple points in time. |
| Expiration Deletion | The deletion policy when snapshots expire. You can select Custom or Never Delete. Custom: Specify a snapshot retention period. After the retention period of a snapshot ends, the snapshot is automatically deleted. Never Delete: The system does not automatically delete snapshots. |
| Custom Deletion Policy | This parameter is required if you set the Expiration Deletion parameter to Custom. Enter a number and select Hours, Days, Months, or Years to specify a snapshot retention period. |

5. Click **Submit**.

**What to do next**

After you create a scheduled snapshot policy, you can manage the policy and scheduled snapshots.

| Operation | Description |
|---|---|
| View the information about a scheduled snapshot policy | In the scheduled snapshot policy list, you can view the information about each scheduled snapshot policy, including the policy name, snapshot plan, expiry deletion setting, and number of associated directories. |

| Modify a scheduled snapshot policy | You can modify scheduled snapshot policies to meet business requirements. 1. In the scheduled snapshot policy list, click Modify in the Operation column of the desired scheduled snapshot policy. 2. In the Modify Policy dialog box, modify the name, description, snapshot cycle, and time settings of the policy. 3. Click OK. |
|---|---|
| Delete a scheduled snapshot policy | You can delete scheduled snapshot policies that are no longer needed. Important Before you delete a scheduled snapshot policy, make sure that it is not associated with directories. The directory disassociation operation does not delete the corresponding directory. After you delete a scheduled snapshot policy, you cannot restore it. Proceed with caution. 1. Disassociate directories. If the policy to be deleted is associated with directories, you must disassociate it from the directories. i. In the scheduled snapshot policy list, click the name of the policy. ii. On the Policy details click Disassociate in the Operation column of the file system. In the message that appears, click OK. 2. Delete a scheduled snapshot policy In scheduled snapshot policy list, click Delete in the Operation column of the policy that you want to delete. In the message that appears, click OK. |

## 8 WORM

The Write Once Read Many (WORM) feature is used to ensure the security of data. After a WORM policy is enabled, file access is strictly limited within the protection period to prevent data changes once data is written. This can efficiently prevent user errors, unauthorized deletion, and blackmail attacks.

**Core benefits**

Prevent tampering and deletion During the protection period, file changes or deletion due to user errors or performed by malware are strictly prohibited to ensure data integrity. Meet compliance requirements The WORM feature can meet strict regulatory requirements in the finance, healthcare, and public service sectors and also provides audit logs for tracing. Support automated management File locking and expiration can be automatically triggered based on a retention policy. This greatly reduces O&M complexity. Support fine-grained control You can specify different protection periods for different file systems to meet diverse business requirements.

**Use scenarios**

Log archiving in the finance sector You can use the WORM feature to archive transaction logs, audit records, and other data that must be retained for long-term businesses and must not be changed. Medical imaging data storage Sensitive information such as PACS images and electronic medical records must not be tampered with during the legal preservation period to ensure the credibility of diagnosis and treatment. Enterprise legal affair and contract management After important materials such as contracts and intellectual property documents are uploaded, they are automatically protected to prevent internal tampering.

### 8.1 Create a WORM policy

After you enable a Write Once Read Many (WORM) policy for a file system, files will automatically enter the WORM state after they are written to the file system. You can also manually set files to the WORM state after the files are written to the file system. During the protection period, files are only readable. Any changes or deletion is prohibited to ensure data integrity and prevent tampering. This feature is suitable for scenarios such as data archiving for compliance needs, audit logs, and long-term data retention.

**Usage notes**

Currently, only the compliance mode is supported. In compliance mode, no user is allowed to delete or change directories or files within the WORM protection period. For compliance purposes, after a WORM policy is enabled for a file system, you cannot disable the WORM policy for the system or enable another WORM policy for the file system. Proceed with caution.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation tree, click **WORM Strategy**.
3. On the **WORM** page, click **Create Worm**.
4. On the **Create WORM** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | The organization and resource set to which the file system belongs. |
| Resource Set |   |
| Region | The region to which the file system belongs. |
| Catalog | The file system for which you want to create a WORM policy. |
| Auto-Lock Period | After a file is written to the file system and the file is not modified within the auto-lock period, the file automatically enters the WORM state. Enter a positive integer and select Minutes, Hours, or Days. |
| Default Retention Period | If no protection period is manually specified, the default protection period is applied after a file enters the WORM state. You can specify a time period or select Indefinite. If you select Indefinite, the file is permanently protected. |
| Minimum Retention Period | If a protection period is manually specified, files are protected based on the minimum and maximum protection periods. You can specify a time period or select Indefinite. If you select Indefinite, the protection period is set to the maximum. Important The value of Default Retention Period must be equal to or greater than the value of Minimum Retention Period, and it must be equal to or smaller than the value of Maximum Retention Period. After a file is written to the file system, perform the following steps to manually specify a protection period: i. Run the touch -a -t 202712310000 filename command to set the atime of the file to 2027-12-31, which means that the protection period of the file ends on December 31, 2027. ii. After the auto-lock period ends, the file automatically enters the WORM state. iii. The file cannot be modified or deleted before the protection period ends. |
| Maximum Retention Period |   |

5. Click **Submit**.
The following table describes file states and state transition after a WORM policy is enabled for a file system.

| File state | Description | State transition |
|---|---|---|
| Pending lock | A file enters this state after it is written to the file system. In this case, the file is readable and writable, and all users can modify the file. | The file enters the protected state in one of the following scenarios: It automatically enters the protected state if it is not modified within the auto-lock period. The status of the file is manually changed to protected. |
| Protecte d | The file is read-only. No changes are allowed. | Manually extend the protection period of the file to keep it in the protected state. After the protection period ends, the file enters the protection- expired state. |
| Protectio n expired | The file is readable and deletable. However, it cannot be modified. Note After the protection period of the file ends, you can run the touch -a command to set a protection period for the file. This way, the file will enter the WORM state again. | Manually extend the protection period of the file. Then, the file enters the protected state again. |

### 8.2 Modify a WORM policy

After you enable a Write Once Read Many (WORM) policy for a file system, you can extend the default protection period, minimum protection period, and maximum protection period based on your business requirements.

**Usage notes**

The protection periods of WORM can only be extended. You cannot shorten the protection periods.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation tree, click **WORM Strategy**.
3. In the WORM policy list, click **Modify** in the **Operation** column of a file system.
4. In the **Modify WORM** dialog box, extend the protection periods.
The value of **Default Retention Period** must be equal to or greater than the value of
**Minimum Retention Period**, and it must be equal to or smaller than the value of
**Maximum Retention Period**.
5. Click **OK**.
After the protection periods are extended, the changes take effect immediately on all files stored in the file system.
