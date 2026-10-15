---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Elastic File System NAS User Guide 20260902"
product_version: "V3.18.6_2607"
doc_version: "20260902"
pdf_pages: 50
source_pdf: "03deb6b106b070a8_Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Elastic File System NAS User Guide 202"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/CDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Cloud%20Defined%20Storage%20Elastic%20File%20System%20NAS%20User%20Guide%2020260902.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Cloud Defined Storage Elastic File System NAS User Guide 20260902

## Table of Contents

- 1 What is EFS-NAS?
- 2 Limits
- 3 Getting started
  - 3.1 Log in to the EFS-NAS console
  - 3.2 Create a file system
  - 3.3 Create a user
  - 3.4 Create a share
  - 3.5 Mount an NFS file system
  - 3.6 Mount an SMB file system
- 4 Manage file systems
  - 4.1 View the detailed information about a file system
  - 4.2 Scale up a file system
  - 4.3 Delete a file system
  - 4.4 Share management
    - 4.4.1 Manage NFS shares
    - 4.4.2 Manage SMB shares
  - 4.5 Freeze and thawing file systems
  - 4.6 File system quotas
- 5 User and user group management
  - 5.1 User management
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

EFS-NAS supports two instance types, capacity and performance, to meet different business scenarios. Capacity instances Run on servers with a mix of Solid-State Drives (SSDs) and Hard Disk Drives (HDDs). Provide a large-capacity, cost-optimized shared file storage solution. Suitable for cost-sensitive scenarios such as archive management, data archiving, and video surveillance playback. Performance instances Run on all-flash SSD servers. Provide high-throughput, low-latency file access. Suitable for performance-sensitive scenarios such as high-performance computing (HPC), media editing, and database file storage.

**Core features**

File system mounting: Multiple clients can mount the file system. Elastic scaling: You can scale out the file system online and dynamically adjust the capacity as your business grows. Mount points: You can generate mount points through Network File System (NFS) or Server Message Block (SMB) protocol shares. Quota management: You can set capacity quotas by organization to achieve rational resource allocation, cost control, and performance optimization. Unique namespace capacity: A single namespace supports up to 5 PiB of capacity for unified management of mass data. Maximum cluster scale: A single cluster supports up to 2,000 disks and scales out horizontally on demand. Minimum three-node deployment: You can start with three nodes to meet the needs of small-scale business and smooth scaling. Flexible storage pool deployment: You can dedicate and flexibly plan resources at the underlying layer of the storage cluster to reduce initial equipment investment.

## 2 Limits

Review the following limits before using File Storage NAS.

**File system limits**

Maximum files per file system: 10 billion. Maximum size per file: 512 TiB. A file size of 4 TiB or less is recommended. Maximum directory depth: Unlimited. A directory depth of 20 levels or less is recommended. Maximum directory width: 100,000 entries. Capacity per file system: 1 GiB to 5 PiB. Maximum concurrent mounts per file system: 2,000.

**Other limits**

To delete a file system, first unmount it from all clients and delete its associated share. To delete a user group, first remove it from the SMB share. To delete a user, first remove them from their user group and any associated SMB shares.

## 3 Getting started

### 3.1 Log in to the EFS-NAS console

This topic describes how to log in to the EFS-NAS console.

**Prerequisites**

You have obtained the service domain name for the Apsara Uni-manager Management Console from the deployment personnel. Use the Google Chrome browser.

**Procedure**

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
6. In the top navigation bar, select **Products**. In the **Storage** section, click **File Storage**
**EFS-NAS**.

### 3.2 Create a file system

This topic describes how to create a file system in the EFS-NAS console.

**Procedure**

1. Sign in to the EFS-NAS console.
2. Select **File System Management**, and click **Create File System**.
3. On the **Create File System** page, configure the parameters for the file system.
After you configure the parameters, a configuration summary appears in the pane on the right.

| Parameter |   | Description |
|---|---|---|
| Basic Information | Organization/R esource Set | Select the organization and resource set for the file system. |
|   | Region/Cluster | Select the region and cluster for the file system. |
|   | Storage Class | Supported types are Capacity and Performance. Capacity: Based on hybrid flash servers with SSDs and HDDs, this type provides large-capacity, cost-optimized shared file storage. It is ideal for cost-sensitive scenarios such as archive management, data archiving, and video surveillance playback. Performance: Based on all-flash SSD servers, this type provides high-throughput, low-latency file access. It is ideal for performance-sensitive scenarios such as high- performance computing, media editing, and database file storage. |
|   | File System Name | Enter a name for the file system. The name must be 3 to 32 characters long and can contain uppercase and lowercase letters, Chinese characters, digits, underscores ( ), hyphens (-), _ and periods (.). The name cannot contain only digits or start with a hyphen (-). The file system name cannot be changed after creation. |
|   | NFS Version | Select the NFS protocol version. Supported versions are v3 and v4. |
|   | Description | Enter a description for the file system. |
| Storage Configurati on | Total Capacity (GiB) | Specify the total capacity for the file system, which must be an integer from 1 to 5,242,880. |

4. Optional. If you want to set quotas for the resources of a service, click **Quota**
**Management** on the right side of the page to go to the **Quotas** page. For more
information, see the **Quota management** topic in User Guide - Apsara Uni-manager Mana gement Console.
5. Click **Submit** to create the file system.

### 3.3 Create a user

Learn how to create a user.

**Procedure**

1. Sign in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. In the upper-left corner of the page, click **Create User** and configure the following
parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Region | Select a region. |
| Uid | The system automatically enters a value, which you can modify. Valid values: 10000 to 999999999. Note The uid must be globally unique. |
| Username | Enter a username. |
| Password | Enter a password. |
| Confirm Password | Enter the password again to confirm. |

4. Click **Submit** to create the user.

### 3.4 Create a share

In EFS-NAS, you use shares to mount file systems to clients. This topic describes how to create a share.

**Prerequisites**

Create a file system. Create a Virtual Private Cloud (VPC) and a vSwitch. For more information, see the **Virtual**
**Private Cloud** and **vSwitch** sections of the **Virtual Private Cloud (VPC) User Guide**.
(Optional) To use the IPv6 protocol, you must create a VPC and a vSwitch that support IPv6. You must also contact Alibaba Cloud technical support to enable this feature.

**Create an NFS share**

1. Log on to the EFS-NAS console.
2. Select File System Management, click **Create Share** in the **Operation** column of the
target file system, and select **NFS Share**.
3. On the **Create NFS Share** page, configure the parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters long and can contain uppercase and lowercase letters, Chinese characters, digits, underscores ( ), hyphens (-), and periods (.). The _ name cannot consist solely of numbers or start with a hyphen. Choose the name carefully, as it cannot be changed after the share is created. |
| Protocol Version | Select an IP protocol version: ipv4 or ipv6. If you select IPv6, the VPC drop-down list shows only VPCs that support IPv6. Note The IPv6 option is available only after the IPv6 feature is enabled. |
| VPC | Select the VPC to which you want to grant access. |
| vSwitch | Select a vSwitch within the authorized VPC. Only clients in this vSwitch can access the file system through this share. |

4. Click **Submit**.
5. Configure client access permissions.
i. Click the file system ID/name or **Details** in the **Operation** column to go to the file system details page. ii. In the upper-left corner of the **NFS share** page, click **Client IP Details**. iii. In the **Client IP Details** dialog box, click **Add a new one**, and configure the following parameters:
**Type**: IP address/CIDR block or All.
**Client IP**: When the type is IP address/CIDR block, enter the allowed client IP
addresses or CIDR blocks. IPv4 and IPv6 addresses are supported.
**Permission**: Set to read-only or read/write.
**Enable Root Anonymity**: When enabled, the root user of a remote client is
automatically mapped to an anonymous user, which denies the user superuser permissions on the server. When a client writes a file as the root user, the owner of the file on the server becomes nobody instead of root.
**Enable****All Anonymity**: When enabled, all client users are mapped to the anonymous
user. All file operations are performed as the anonymous user, and the original user information cannot be retained.
**Operation**: Delete the rule.
iv. Click **OK** to save the settings.

**SMB share**

1. Log on to the EFS-NAS console.
2. Select File System Management, click **Create Share** in the **Operation** column of the
target file system, and then select **SMB Share**.
3. On the **Create SMB Share** page, configure the parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters long and can contain uppercase and lowercase letters, Chinese characters, digits, underscores ( ), hyphens (-), and periods (.). The _ name cannot consist solely of numbers or start with a hyphen. Choose the name carefully, as it cannot be changed after the share is created. |
| Protocol Version | Select the IP protocol version. You can select ipv4 or ipv6. If you select IPv6, the VPC drop-down list displays only VPCs that support IPv6. Note The IPv6 option is available only after the IPv6 feature is enabled. |
| VPC | Select the VPC to grant access. Clients must be in this VPC to access the file system via this share. |
| vSwitch | Select a vSwitch in the specified VPC. Clients must be in this vSwitch to access the file system via this share. |

| User(Group) | Configure the users who are authorized to access the file system through the share. Click Add and configure the following parameters: User Range: User: Click the checkboxes to select authorized users from the drop-down list. User Group: Select the user group to authorize from the drop- down list. All: Grant permissions to all users. Permission: Read/Write: Allows users to read and write objects, which includes viewing content, modifying data, and changing attributes. This permission does not allow changing access permissions. Read-only: Allows users to view object content and read attributes and permissions, but they cannot modify, write, or delete the object. Read/Write (Removal Disallowed): Allows users to read and write object content and modify file data and attributes, but they cannot delete the object, change its permissions, or take ownership. Full Control: Allows users to perform any operation on the object, including read, write, execute, delete, rename, and move. Users can also modify permissions (ACLs) and take ownership. Disallow: Denies all operations. |
|---|---|
| Case Sensitivity | Most systems are not case-sensitive, so you can typically leave this option disabled. Enable it for interoperability when sharing between multiple operating systems. Enabling this option can improve performance. |
| Enable ABE | Access-Based Enumeration (ABE) filters directory listings to show users only the files and folders they have permission to access. This enhances data security by hiding inaccessible resources from view. |
| Enable Oplock | Opportunistic locking allows a client to cache a file locally by acquiring a temporary lock from the server. This caching mechanism significantly improves file access performance, especially in high- latency networks, by reducing server requests. However, it can sometimes cause concurrent access conflicts, so use this feature with caution. |

4. Click **Submit**.

### 3.5 Mount an NFS file system

After you create an NFS share, you can mount the file system to a client from the console or by connecting to an ECS instance.

**Prerequisites**

A file system is created. An NFS share is created. (Optional) If you want to use IPv6, make sure that an IPv6 address is assigned to the ECS instance.

**Method 1: From the console**

**Mount a file system**

You can mount an NFS share directly to an ECS instance from the console. The system uses Cloud Assistant to run the mount command automatically, eliminating the need to log on to the instance.
1. Log on to the EFS-NAS console.
2. Click the name of the file system to open its details page.
3. On the **NFS Shares** page, find the target NFS share and click **Mount** in the **Operation**
column.
4. In the **Mount** dialog box, configure the following parameters:

| Parameter | Description |   |   |
|---|---|---|---|
| Mount Absolute Path | Enter the absolute path of the mount point. For example, /mnt/nfs . |   |   |
|   | Configure the mount parameters. The default value is vers=3,tcp,nolock,async,mountproto=tcp,rsize=1048576,wsize=104 576 . You can modify the value based on your business requirements. For more information about supported parameters, see Mount options. |   |   |
|   |   | vers=3,tcp,nolock,async,mountproto=tcp,rsize=1048576,wsize=104 | 8 |
| Mount Parameters | 576 |   |   |
| Automatic Mount | If you enable this option, the system automatically runs the mount command after the ECS instance restarts. If you disable this option, you must manually run the mount command after the ECS instance restarts. |   |   |
| ECS Instance List | Select the ECS instances to which you want to mount the file system. You can search for instances by instance name, instance ID, or IP address. The list displays the instance ID/name, operating system, IP address, and client status. |   |   |

5. Click **Confirm Mount**.

**Important**

If a batch mount operation fails, the system does not automatically retry. A mount failure usually indicates a configuration error, such as the client's IP address not being added to the permission group. Troubleshoot the issue and then run the mount operation again.
6. After the mount command is issued, the system displays a message that includes the
command ID. You can click the link to view the command execution results on the Cloud Assistant page.

**Unmount a file system**

1. Log on to the EFS-NAS console.
2. Click the name of the file system to go to its details page.
3. On the **NFS Shares** page, find the target NFS share and click **Uninstall** in the **Operation**
column.
4. In the **Uninstall** dialog box, configure the following parameters:
**Uninstall Absolute Path**: Enter the mount point path that you want to unmount. For
example, `/mnt/nfs` .
**ECS Instance List**: Select the ECS instances from which you want to unmount the file
system. You can search for instances by instance name.
5. Click **Confirm Unmount**.
6. After the unmount command is issued, the system displays a message that includes the
command ID. You can click the link to view the command execution results on the Cloud Assistant page.

**Method 2: From an ECS instance**

**Mount a file system**

**Step 1: Install an NFS client**

Before you mount an NFS file system to a Linux ECS instance, you must install an NFS client. If an NFS client is already installed, skip this step.
1. Log on to an ECS instance (Linux). For more information, see the **ECS User Guide**'s **Quick**
**Start > Connect to an instance** section.
2. Install the NFS client.
If you are using CentOS, Red Hat, or Aliyun Linux, run the following command:

```python
sudo yum install nfs-utils
```

If you are using Ubuntu or Debian, run the following commands:

```python
sudo apt-get update sudo apt-get install nfs-common
```

**Step 2: Manually mount the NFS file system**

1. Log on to the ECS instance (Linux system). For more information, see the **Quick Start >**
**Connect to an instance** section in the **ECS User Guide**.
2. Mount the NFS file system.
You can find the mount command in the EFS-NAS console. For more information, see View information about an NFS share. Example mount commands: To mount the file system by using NFSv4.1:

```python
sudo mount -t nfs -o vers=4.1,async,rsize=1048576,wsize=1048576 192.0.2.1:/efs-nasxxxxx /mount_point
```

To mount the file system by using NFSv4.0:

```python
sudo mount -t nfs -o vers=4.0,minorversion=0,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvpo 192.0.2.1:/efs-nas-xxxxx /mount_point
```

To mount the file system by using NFSv3:

```
mount -t nfs -o vers=3,tcp,nolock,async,mountproto=tcp,rsize=1048576,wsize=1048576 192.0.2.1:/efs-nas-xxxxx /mount_point
```

To mount the file system over IPv6 by using NFSv4.1:

```python
sudo mount -t nfs -o vers=4.1,async,rsize=1048576,wsize=1048576 [2001:db8::1]:/efsnas-xxxxx /mount_point
```

The IPv6 address must be enclosed in square brackets ( `[]` ). To mount the file system over IPv6 by using NFSv3:

```python
sudo mount -t nfs -o vers=3,nolock,async,proto=tcp6,mountproto=tcp6,rsize=1048576,wsize=1048576 [2001:db 8::1]:/efs-nas-xxxxx /mount_point
```

For an IPv6 mount with NFSv3, you must set the `proto` and `mountproto` parameters to `tcp6` . Table 1. Mount command parameters

| Parameter | Description |
|---|---|
| vers | The NFS protocol version. NFSv3, NFSv4.0, and NFSv4.1 are supported. vers=3: Mounts the file system by using NFSv3. vers=4.0: Mounts the file system by using NFSv4.0. vers=4.1: Mounts the file system by using NFSv4.1. |

| Mount option | You can specify multiple mount options, separated by commas (,). rsize: The size, in bytes, of the data blocks that the client uses for read requests. The recommended value is 1048576. wsize: The size, in bytes, of the data blocks that the client uses for write requests. The recommended value is 1048576. Note If you need to change the I/O size parameters (rsize and wsize), we recommend that you use the maximum value (1048576) to prevent performance degradation. hard: If the Apsara File Storage NAS service is temporarily unavailable, this option stops applications using the file system and forces them to wait until the service is back online. We recommend that you use this option. timeo: The time, in tenths of a second, that the NFS client waits for a response before it retries a request. The recommended value is 600 (60 seconds). Note If you must change the timeout parameter (timeo), we recommend that you use a value of 150 or greater. The unit of this parameter is 0.1 seconds, so a value of 150 represents 15 seconds. retrans: The number of times the NFS client retries a request. The recommended value is 2. noresvport: Uses a new TCP port when a network connection is re- established. This ensures that the connection is not interrupted when the network recovers from a failure. We recommend that you use this option. proto: Specifies the network transport protocol. For IPv6 mounts, set this parameter to tcp6 . mountproto: Specifies the mount protocol. For IPv6 mounts, set this parameter to tcp6 . Note When you configure the parameters, take note of the following: Do not use the soft option due to the risk of data inconsistency. If you choose to use the soft option, you are responsible for any associated risks. Avoid setting any mount options other than the default ones. Changing the read or write buffer size or disabling attribute caching can reduce performance. |
|---|---|

Run the `mount -l` command to view the mount result. The mount is successful if the output is similar to the following: After the mount succeeds, you can also run the `df -h` command to view the current capacity of the file system. After the mount succeeds, you can access the EFS-NAS file system from your ECS instance and perform read and write operations.

**Unmount a file system**

Unmount the file system from your ECS instance when you no longer need to access it or want to change the mount point.
1. Log on to a Linux ECS instance. For more information, see the **Quick Start > Connect to**
**an instance** section in the **ECS User Guide**.
2. Run the following command to view the currently mounted file systems:

```
df -h
```

In the output, find the mount point path of the EFS-NAS file system, such as `/mnt/nfs` .
3. Run the following command to unmount the file system:

```python
sudo umount /mnt/nfs
```

Replace `/mnt/nfs` with the actual path of your mount point.
4. Run the following command to verify that the file system is successfully unmounted:

```
df -h | grep efs-nas
```

No output indicates that the file system has been successfully unmounted.

### 3.6 Mount an SMB file system

After you create a share, you can use a mount point to mount the file system to a client. This topic describes how to mount an SMB file system.

**Prerequisites**

You have created a file system. You have created an SMB share. (Optional) To use IPv6, ensure your ECS instance has an IPv6 address.

**Procedure**

1. Log on to your Windows-based ECS instance. For more information, see the **ECS User**
**Guide** in the **Quick Start > Connect to instance** section.
2. Ensure that the following two Windows services are running.
Workstation a. Navigate to **All Programs > Accessories > Run** or press `Win+R` . In the Run dialog box, enter `services.msc` and press Enter. b. In the Services window, find Workstation and verify that its Status is **Started** and its Startup Type is **Automatic**. By default, the Workstation service is running. TCP/IP NetBIOS Helper Follow these steps to enable the TCP/IP NetBIOS Helper service: a. Open **Network and Sharing Center** and click your active network connection. b. Click **Properties**, double-click **Internet Protocol Version 4**, and then click
**Advanced**.
c. In the **Advanced TCP/IP Settings** dialog box, on the **WINS > Enable NetBIOS over**
**TCP/IP**.
d. Navigate to **All Programs > Accessories > Run** or press `Win+R` . In the Run dialog box, enter `services.msc` and press Enter. e. In the Services window, find TCP/IP NetBIOS Helper and verify that its Status is **Started** and its Startup Type is **Automatic**. By default, the TCP/IP NetBIOS Helper service is running.
3. Open a Command Prompt window and run the following command to mount the file system.
Command format: `net use <target-drive-letter> <mount-command> /user:<user-name>` . `<target-drive-letter>` : The drive letter that you want to map on your Windows system. The drive letter must be available. `<mount-command>` : The mount point address that is automatically generated when you create the mount point. You can obtain this value from the EFS-NAS console. Find your file system, click **Details**, click the **SMB Share** tab, and then view the **Mount Command** for the target share. `<user-name>` : The user authorized to access the file system, which you specify when creating the SMB share. To view or edit this user in the EFS-NAS console, find your file system and click **Details**. On the **SMB Share** tab, find the target share, and in the
**Operation** column, click **Edit > Add User (Group)**.
IPv4 mount command example:

```
net use D: \\192.0.2.1\smb-share /user:test-user
```

IPv6 mount command example:

```
net use Z: \\2001-0db8-1.ipv6-literal.net\smb-share /user:test-user
```

4. Run the `net use` command to verify the mount.
5. After mounting the file system, you can access it on your ECS instance to read and write
data.

## 4 Manage file systems

### 4.1 View the detailed information about a file system

**about a file system**

This topic describes how to view the detailed information about a file system.

**Procedure**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. The file system list displays the basic information about each file system, including the
status, usage and total capacity, cluster, storage type, label, NFS version, organization and resource set, creator, and creation time.
3. You can click the ID of a file system or click Details in the Operation column to go to the
details page. On the details page, you can view NFS and SMB shares. For more information, see Share management.

### 4.2 Scale up a file system

This topic explains how to increase the total capacity of a file system.

**Procedure**

1. Log on to the EFS-NAS console.
2. In the file system list, find the file system you want to scale up, and in its **Operation**
column, click the icon and then click **Capacity Expansion**.
3. On the **Capacity Expansion** page, review the current total capacity and enter a new value
in **New Total Capacity (GiB)**. The new total capacity must be greater than the current total capacity.
4. Click **Submit**.

### 4.3 Delete a file system

Delete a file system that you no longer need.

**Prerequisites**

The file system is unmounted from all clients. All sharing settings are deleted. The file system is not in a frozen state. To delete a frozen file system, you must first unfreeze it. All subdirectory quotas are deleted.

**Procedure**

**Warning**

Deleting a file system is an irreversible action. Ensure that you have backed up your data before you proceed.
1. Log on to the EFS-NAS console.
2. In the file system list, select the file systems to delete.
**Delete a single item**: In the **Operation** column of the target file system, click the
icon, and click **Delete**.
**Batch deletion**: Select the checkboxes next to the target file systems and click **Batch**
**Deletion** below the list. In the **Batch Deletion** dialog box, confirm the list of file systems
to be deleted.

**Important**

File systems in a frozen state cannot be deleted. If a batch deletion includes frozen file systems, a dialog box identifies the items that cannot be processed. After you confirm, only the eligible file systems are deleted.
3. Click **OK**.

### 4.4 Share management

Elastic File Storage-File Storage NAS (EFS-NAS) supports the Network File System (NFS) and Server Message Block (SMB) file access protocols, which allow you to access shared, elastic, highly reliable, and high-performance distributed file systems through shares without making any changes to your applications.

#### 4.4.1 Manage NFS shares

This topic describes the operations that you can perform to manage Network File System (NFS) shares.

**Create an NFS share**

1. Log on to the EFS-NAS console.
2. Select File System Management, click **Create Share** in the **Operation** column of the
target file system, and select **NFS Share**.
3. On the **Create NFS Share** page, configure the parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters long and can contain uppercase and lowercase letters, Chinese characters, digits, underscores ( ), hyphens (-), and periods (.). The _ name cannot consist solely of numbers or start with a hyphen. Choose the name carefully, as it cannot be changed after the share is created. |

| Protocol Version | Select an IP protocol version: ipv4 or ipv6. If you select IPv6, the VPC drop-down list shows only VPCs that support IPv6. Note The IPv6 option is available only after the IPv6 feature is enabled. |
|---|---|
| VPC | Select the VPC to which you want to grant access. |
| vSwitch | Select a vSwitch within the authorized VPC. Only clients in this vSwitch can access the file system through this share. |

4. Click **Submit**.
5. Configure client access permissions.
i. Click the file system ID/name or **Details** in the **Operation** column to go to the file system details page. ii. In the upper-left corner of the **NFS share** page, click **Client IP Details**. iii. In the **Client IP Details** dialog box, click **Add a new one**, and configure the following parameters:
**Type**: IP address/CIDR block or All.
**Client IP**: When the type is IP address/CIDR block, enter the allowed client IP
addresses or CIDR blocks. IPv4 and IPv6 addresses are supported.
**Permission**: Set to read-only or read/write.
**Enable Root Anonymity**: When enabled, the root user of a remote client is
automatically mapped to an anonymous user, which denies the user superuser permissions on the server. When a client writes a file as the root user, the owner of the file on the server becomes nobody instead of root.
**Enable****All Anonymity**: When enabled, all client users are mapped to the anonymous
user. All file operations are performed as the anonymous user, and the original user information cannot be retained.
**Operation**: Delete the rule.
iv. Click **OK** to save the settings.

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

**Important**

Before you delete an NFS share, make sure that no client uses the share to connect to the corresponding file system.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. On the **NFS Share** tab, find the target share and click **Delete** in the Operation column.
4. In the message that appears, click **OK**.

#### 4.4.2 Manage SMB shares

This topic describes the operations that you can perform to manage Server Message Block (SMB) shares.

**SMB share**

1. Log on to the EFS-NAS console.
2. Select File System Management, click **Create Share** in the **Operation** column of the
target file system, and then select **SMB Share**.
3. On the **Create SMB Share** page, configure the parameters.

| Parameter | Description |
|---|---|
| Share Name | Enter a name for the share. The name must be 3 to 32 characters long and can contain uppercase and lowercase letters, Chinese characters, digits, underscores ( ), hyphens (-), and periods (.). The _ name cannot consist solely of numbers or start with a hyphen. Choose the name carefully, as it cannot be changed after the share is created. |
| Protocol Version | Select the IP protocol version. You can select ipv4 or ipv6. If you select IPv6, the VPC drop-down list displays only VPCs that support IPv6. Note The IPv6 option is available only after the IPv6 feature is enabled. |
| VPC | Select the VPC to grant access. Clients must be in this VPC to access the file system via this share. |
| vSwitch | Select a vSwitch in the specified VPC. Clients must be in this vSwitch to access the file system via this share. |

| User(Group) | Configure the users who are authorized to access the file system through the share. Click Add and configure the following parameters: User Range: User: Click the checkboxes to select authorized users from the drop-down list. User Group: Select the user group to authorize from the drop- down list. All: Grant permissions to all users. Permission: Read/Write: Allows users to read and write objects, which includes viewing content, modifying data, and changing attributes. This permission does not allow changing access permissions. Read-only: Allows users to view object content and read attributes and permissions, but they cannot modify, write, or delete the object. Read/Write (Removal Disallowed): Allows users to read and write object content and modify file data and attributes, but they cannot delete the object, change its permissions, or take ownership. Full Control: Allows users to perform any operation on the object, including read, write, execute, delete, rename, and move. Users can also modify permissions (ACLs) and take ownership. Disallow: Denies all operations. |
|---|---|
| Case Sensitivity | Most systems are not case-sensitive, so you can typically leave this option disabled. Enable it for interoperability when sharing between multiple operating systems. Enabling this option can improve performance. |
| Enable ABE | Access-Based Enumeration (ABE) filters directory listings to show users only the files and folders they have permission to access. This enhances data security by hiding inaccessible resources from view. |
| Enable Oplock | Opportunistic locking allows a client to cache a file locally by acquiring a temporary lock from the server. This caching mechanism significantly improves file access performance, especially in high- latency networks, by reducing server requests. However, it can sometimes cause concurrent access conflicts, so use this feature with caution. |

4. Click **Submit**.

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

**Important**

Before you delete an SMB share, make sure that no client uses the share to connect to the corresponding file system.
1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. Click the ID of a file system or click **Details** in the Operation column to go to the details
page of the file system.
3. On the **SMB Share**, find the target SMB share and click **Delete** in the Operation column.
4. In the message that appears, click **OK**.

### 4.5 Freeze and thawing file systems

**systems**

This topic describes how to batch freeze and thawing EFS-NAS file systems.

**Background**

When an EFS-NAS file system is frozen, you cannot delete it, expand it, or create an NFS/SMB share on it. You can use the batch freeze and batch thawing features to change the status of multiple file systems at once.

**Batch freeze**

1. Log on to the EFS-NAS console.
2. On the **File System Management** page, select the checkboxes next to the file systems
that you want to freeze.
3. Click **Batch Freeze** at the bottom of the list.
4. In the **Batch Freeze** dialog box, confirm the list of file systems to be frozen and click **OK**.
If any selected file systems cannot be frozen (for example, because they are already frozen), a message appears listing them. After you confirm, the system freezes only the eligible file systems.

**Batch thawing**

1. Log on to the EFS-NAS console.
2. On the **File System Management** page, select the checkboxes next to the file systems
that you want to thawing.
3. Click **Batch Thawing** at the bottom of the list.
4. In the **Batch Thawing** dialog box, confirm the list of file systems to be unfrozen and click
**OK**.
If any selected file systems cannot be unfrozen (for example, because they are not frozen), a message appears listing them. After you confirm, the system unfreezes only the eligible file systems.

### 4.6 File system quotas

This topic describes how to manage file system quotas, including how to create, view, modify, and delete directory quotas.

**Background**

EFS-NAS allows you to set quotas on a file system to limit storage capacity and the number of files. This helps you effectively manage storage resources in multi-user environments and prevents a single directory or user from consuming excessive storage resources. There are three types of file system quotas:
**directory quota**: Sets a quota on a specified directory to limit its overall storage capacity
and number of files.
**user quota**: Sets a quota for a specified user within a directory, limiting the user's storage
capacity and file count in that directory.
**user group quota**: Sets a quota for a specified user group within a directory, limiting the
user group's storage capacity and file count in that directory. Each quota type supports two dimensions: **capacity quota** and **file count quota**. You must enable at least one dimension. Each dimension has three levels:
**hard quota**: The absolute limit. If this limit is exceeded, the system blocks write operations
and triggers an alert.
**soft quota**: If this limit is exceeded, a grace period begins. You can continue to perform
write operations during the grace period. After the grace period expires, write operations are blocked.
**recommended quota**: If this limit is exceeded, the system triggers an alert, but write
operations are not affected.

**Prerequisites**

You have created a file system, and the file system is running. You have created a share and mounted the file system to an ECS instance.

**Create a quota**

1. Log on to the EFS-NAS console.
2. In the file system list, click the name or ID of the target file system.
3. On the **Directory Quota** tab, click **Create Directory Quota**.
4. In the **Create Directory Quota** dialog box, configure the following parameters:

| Parameter | Description |
|---|---|
| Quota Type | The supported types are Directory Quota, FS user quota, and FS User Group quota. Note You cannot create user quotas or user group quotas for non-empty directories. |
| Directory Path | Configure this parameter when the quota type is Directory Quota. Enter the path of the subdirectory for which you want to set a quota, such as dir1/teamA . The path is relative to the root directory of the current file system. If the specified directory does not exist, the system automatically creates it. |
| FS user | This parameter is required when Quota type is set to FS user quota. Select the user for whom you want to set a quota. |
| FS User Group | This parameter is required when Quota type is set to FS User Group quota. Select the user group for which you want to set a quota. |
| Fixed Capacity Ratio | When this feature is enabled, the soft capacity quota and recommended capacity quota are automatically calculated based on a percentage of the hard capacity quota. The formulas are: soft quota = hard quota × ratio, and recommended quota = soft quota × ratio. |
| Capacity Ratio | This parameter is required if you enable Fixed capacity ratio. Valid values: 60% to 95%. |
| Capacity Hard Quota | The maximum storage space that the directory can use, in GiB .Exceeding this quota triggers an alert and blocks further write operations. |
| Capacity Soft Quota | The soft limit for the directory's storage capacity, in GiB. Exceeding this quota triggers an alert and starts a grace period, during which write operations are still allowed. If you enable Fixed capacity ratio, this value is automatically calculated and cannot be manually modified. |
| Capacity Grace Time | The duration of the grace period after the soft quota is exceeded, in days. The maximum value is 365. After the grace period expires, write operations are blocked. This parameter is required if you set a soft quota. |
| Recommended Capacity Quota | The recommended limit for the directory's storage capacity, in GiB. If you enable Fixed capacity ratio, this value is automatically calculated and cannot be manually modified. If this limit is exceeded, the system triggers an alert, but write operations are not affected. |

| Fixed Proportion Of Files | When this feature is enabled, the soft file count quota and recommended file count quota are automatically calculated based on a percentage of the hard file count quota. The formulas are: soft quota = hard quota × ratio, and recommended quota = soft quota × ratio. |
|---|---|
| File Ratio | This parameter is required if you enable Fixed file count ratio. Valid values: 60% to 95%. |
| Hard Quota OfFiles | The maximum number of files and subdirectories that can be created in the directory. Exceeding this quota triggers an alert and blocks further write operations. |
| File Count Soft Quota | The soft limit for the number of files in the directory. Exceeding this quota triggers an alert and starts a grace period, during which write operations are still allowed. If you enable Fixed file count ratio, this value is automatically calculated and cannot be manually modified. |
| Time Limit For The Number Of Files | The duration of the grace period after the soft file count quota is exceeded, in days. The maximum value is 365. After the grace period expires, write operations are blocked. This parameter is required if you set a soft quota. |
| Recommended File Quota | The recommended limit for the number of files in the directory. When the number of files reaches this recommended quota, the system triggers an alert, but write operations are not affected. If you enable Fixed file count ratio, this value is automatically calculated and cannot be manually modified. |

**Important**

You must enable at least the hard capacity quota or the hard file count quota.
5. Click **OK**.

**View directory quotas**

1. In the file system list, click the name or ID of the target file system.
2. Click the **Directory Quota** tab to view the configured directory quotas for the current file
system. Information such as the directory path, quota type, capacity usage, and file count usage is displayed.

**Modify a directory quota**

1. On the **Directory Quota** tab of the file system details page, find the target directory and
click **Modify** in the **Operation** column.
2. In the **Modify directory quota** dialog box, change the values for the capacity quota or file
count quota.
3. Click **OK**.

**Delete a directory quota**

**Warning**

Deleting a directory quota removes its capacity and file count limits.
1. On the **Directory Quota** tab of the file system details page, find the target directory and
click **Delete** in the **Operation** column.
2. In the confirmation dialog box, click **OK**.
ment

## 5 User and user group management

**management**

### 5.1 User management

This document describes user management for EFS-NAS file systems.

**Background information**

EFS-NAS supports user-based permission management for shares that use the SMB protocol. You can assign different permission levels, such as read and write, read-only, or full control, to different users to ensure secure data access.

**Create a user**

1. Sign in to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. In the upper-left corner of the page, click **Create User** and configure the following
parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource set. |
| Region | Select a region. |
| Uid | The system automatically enters a value, which you can modify. Valid values: 10000 to 999999999. Note The uid must be globally unique. |
| Username | Enter a username. |
| Password | Enter a password. |
| Confirm Password | Enter the password again to confirm. |

4. Click **Submit** to create the user.

**Update a password**

1. Log on to the EFS-NAS console.
ment
2. In the left-side navigation pane, click **User Group**.
3. On the **User** page, find the target user and click **Update Password** in the **Operation**
column.
4. Enter and confirm the new password, then click **OK**.

**Delete a user**

**Important**

Before deleting a user, remove them from all SMB shares and user groups.
1. Log on to the EFS-NAS console.
2. In the left-side navigation pane, click **User Group**.
3. On the **User** page, find the target user and click **Delete** in the **Operation** column.
4. Click **OK**.

### 5.2 Manage user groups

This topic describes how to manage user groups for EFS-NAS file systems.

**Background information**

EFS-NAS supports user groups for SMB shares. You can grant permissions to a user group to simplify authorization management for multiple users.

**Create a user group**

1. Log on to the EFS-NAS console.
2. In the left navigation pane, click **User Group**.
3. On the **User Group** tab, click **Create User Group** in the upper-left corner.
4. Configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization. |
| Resource Set | Select a resource group. |
| Region | Select a region. |
| User Group ID | The system automatically assigns an ID, but you can change it. The value must be between 10,000 and 999,999,999. Note The user group ID must be globally unique. |

ment

| User Group Name | Enter a user group name. The name cannot start with a number. |
|---|---|
| User Group Members | Select the members. Note A user group should contain no more than 4,096 members. |

5. Click **Submit**.

**View user group details**

1. Log on to the EFS-NAS console.
2. In the left navigation pane, click **User Group**.
3. On the **User Group** tab, click a user group name or **Details** in the **Operation** column to
view the group's members and region.

**Update members**

1. Log on to the EFS-NAS console.
2. In the left navigation pane, click **User Group**.
3. On the **User Group** tab, find the target user group and click **Update Members** in the
**Operation** column.
4. Add or remove members, and then click **OK**.

**Delete a user group**

**Important**

You must remove a user group from all associated SMB shares before you can delete it.
1. Log on to the EFS-NAS console.
2. In the left navigation pane, click **User Group**.
3. On the **User Group** tab, find the target user group and click **Delete** in the **Operation**
column.
4. Click **OK**.

## 6 Recycle bin

To prevent business disruption or permanent data loss from accidental file deletions, we recommend enabling the Recycle Bin. When enabled, the Recycle Bin temporarily stores deleted files and directories. You can configure a retention policy to permanently delete these items after a specified period. During the retention period, you can restore these files and their metadata, including UID, GID, and ACLs.

**Background information**

When the Recycle Bin is enabled, deleted files or directories are moved to the Recycle Bin. Examples include: Files in an EFS-NAS file system that you manually delete from a client. For example, if you run the `rm -f test01.text` command to delete the filetest01.text, the filetest01.text is moved to the Recycle Bin. Files or directories in an EFS-NAS file system that are automatically deleted by an application on a client. For example, if a Python application uses `os.remove("test02.text")` to delete the filetest02.text, the filetest02.text is moved to the Recycle Bin. Files or directories that are deleted by a POSIX rename operation. For example, if a directory contains bothtest_a.txt andtest_b.txt, and you run the `mv test_a.txt test_b.txt` command, the originaltest_b.txt file is overwritten and moved to the Recycle Bin. Temporary files generated by applications using the EFS-NAS file system. For example, when you edit a file with the**vim** command, temporary files such as `.swp` and `.swpx` are moved to the Recycle Bin. Log files that are automatically rotated by an application. For example, if Nginx is configured to automatically rotate logs and keep a maximum of 20 log files, when the log filetest.log.19 is renamed totest.log.20, the originaltest.log.20 file is overwritten and moved to the Recycle Bin. Overwriting a file's content does not move the file to the Recycle Bin. For example, calling the open() function in w+ mode to write to a file does not move the file to the Recycle Bin.

### 6.1 Enable the recycle bin feature

After you enable the recycle bin feature, deleted files are automatically added to the recycle bin. If you configure a retention policy, files in the recycle bin are permanently deleted when the specified retention period ends.

**Procedure**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation pane, click **Recycle Bin**.
3. Click **Enable** in the upper-left corner. In the **Enable Recycle Bin** dialog box, configure the
parameters.

| Parameter | Description |
|---|---|

| Select a file system | Select the file system for which you want to enable the recycle bin feature. |
|---|---|
| Retention Plan | Valid values: Custom and Permanent retention. |
| Custom Retention Policy | If you select this option, you must configure the parameters of the retention policy. Specify the number of days for which files are retained in the recycle bin. Valid values: 1 to 365. |
| Filter Rules | Optional. Enter filtering rules, such as *.tmp. Separate multiple filter rules with commas (,). You can set the prefix or suffix to filter out files that do not need to be recycled. Files that match the filtering rules are not added to the recycle bin. Important Do not configure nested rules, such as *ab and *b or cd* and c*. |

4. Click **OK**.

### 6.2 Restore files from the recycle bin

**bin**

You can restore files from the recycle bin within the retention period that you specify.

**Usage notes**

You can restore only one file or directory in a single restore operation. If you restore a specified directory, all files in the directory are recursively restored. After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.

**Procedure**

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

| Clear the recycle bin | If you no longer use the files in the recycle bin, you can empty the recycle bin to reduce storage costs. Warning If you empty the recycle bin, all files in the recycle bin are permanently deleted and cannot be restored. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to manage, click the icon in the Actions column, and then select Clear Recycle Bin. 4. Check the information and click OK. |
|---|---|---|
| Disable the recycle bin feature | If you no longer need to use the files in the recycle bin or you no longer want to use the recycle bin feature, you can disable and empty the recycle bin. Warning If you disable the recycle bin, all files in the recycle bin are permanently deleted. If you disable and then enable the recycle bin again, the recycle bin is empty. The deleted files cannot be restored. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Recycle Bin. 3. Find the file system that you want to manage, click the icon in the Actions column, and then select Close Recycle Bin. 4. Check the information and click OK. |

## 7 Snapshots

To prevent data loss caused by accidental operations, attacks, or viruses, you can use snapshots to periodically back up business data stored in file systems. To ensure the integrity and recoverability of data stored in an Elastic File Storage-File Storage NAS (EFS-NAS) file system, the system provides the snapshot feature. It allows you to create a read-only replica of the state of a file system at a certain point in time. Snapshots are classified into regular snapshots and scheduled snapshots, which can meet diverse data protection requirements. The differences between normal snapshots and scheduled snapshots are as follows: Normal snapshots: manually created by users. They are suitable for instant backup before important operations, such as system upgrades, configuration changes, and data migration. Scheduled snapshots: periodically generated by the system based on the scheduled snapshot policy. Scheduled snapshots are suitable for routine backup of important directories in a production environment to meet long-term protection requirements, such as legitimate data retention, prevention of accidental deletion, and automated O&M. We recommend that you formulate a tiered backup policy based on the actual business scenarios to balance security and resource costs.

### 7.1 Create a snapshot

EFS-NAS supports two types of snapshots: manual snapshots and automatic snapshots. You can create a manual snapshot on demand, while the system creates automatic snapshots based on an automatic snapshot policy. This topic explains how to create a snapshot for a file system.

**Usage notes**

The directory depth of a file system cannot exceed 16 levels. The path length for a manual snapshot cannot exceed 4,096 characters, and the path length for an automatic snapshot cannot exceed 4,047 characters. For a single file system, we recommend keeping up to 128 snapshots. You can create a maximum of 2,048 snapshots per file system. The total number of snapshots across all your file systems cannot exceed 8,192. You cannot create a snapshot for a file system while another is being created. We recommend waiting at least 10 minutes between creating snapshots for the same file system. A snapshot captures data at a specific point in time and does not include any data added during the creation process. You can associate a single file system with a maximum of eight automatic snapshot policies. If you associate multiple automatic snapshot policies with a single file system, all policies take effect simultaneously.

**Procedure**

1. Log on to the EFS-NAS console.
2. In the left-side navigation pane, click **Snapshot**.
3. On the **Snapshot** page, on the **Directory Snapshot** tab, click **Create Snapshot**.
4. In the **Create Directory Snapshot** page, configure the following parameters.

**Manual snapshot**

| Parameter | Description |
|---|---|
| Organization | Select the organization and resource group of the file system. |
| Resource Group |   |
| Region | Select the region where the file system is located. |
| Catalog | Select the file system for which you want to create a snapshot. |
| Snapshot type | Select Manual Snapshot. |
| Name | Enter a name for the snapshot. The name must be 1 to 128 characters long and can contain uppercase letters, lowercase letters, digits, periods (.), underscores ( ), and hyphens (-). _ |
| Description | (Optional) Enter a brief description, such as the purpose or context of the snapshot. |
| Expiration Deletion | Select Custom or Never Delete. Custom: Set a custom retention period. The system automatically deletes the snapshot after the period expires, unless the snapshot is locked. Never Delete: The system never automatically deletes the snapshot. |
| Custom Deletion Policy | This parameter is required if you select Custom for the Expiration Deletion parameter. Enter a number and select Hours, Days, Months, or Years to define the retention period. |
| Lock | (Optional) If you enable this option, the snapshot cannot be deleted. Note A locked snapshot is not automatically deleted, even after its retention period expires. You must unlock the snapshot before you can delete it. |

**Automatic snapshot**

**Important**

Before you create an automatic snapshot, make sure you have created an automatic snapshot policy.

| Parameter | Description |
|---|---|
| Organization | Select the organization and resource group of the file system. |
| Resource Set |   |
| Region | Select the region where the file system is located. |
| Catalog | Select the file system for which you want to create a snapshot. |
| Snapshot Type | Select Scheduled Snapshot. |
| Scheduled Policy | Select the automatic snapshot policy for the file system. Note You can only select policies that belong to the same cluster as the file system. |
| First Snapshot | Determines when the first snapshot is created. Follow Policy: The system creates the first snapshot according to the schedule in the automatic snapshot policy. Execute Now: The system creates the first snapshot immediately. |

5. Click **Submit** to create the snapshot.

**Related Operations**

After a snapshot is created, you can use it to restore files and manage the snapshot.
**Restore files from a snapshot** : If data is lost, you can locate the snapshot's directory on
the EFS-NAS cluster node and manually restore the required files. For assistance with file restoration, contact Alibaba Cloud Technical Support. Manage snapshots: View snapshot details and delete snapshots as needed.

### 7.2 Manage snapshots

After a snapshot is created, you can view the snapshot information, modify the snapshot attributes, lock or unlock the snapshot, and delete the snapshot.

| Operation | Description | Procedure |
|---|---|---|

| Query snapshot information | After a snapshot is created, you can view the organization, resource set, status, lock status, and expiration time of the snapshot. | 1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, view the detailed information about snapshots. |
|---|---|---|
| Modify snapshot attributes | You can modify the attributes of a snapshot based on its usage, including the snapshot name, description, expiration policy, expiration time, and lock status. Important You can modify the attributes of only normal snapshots. To modify a scheduled snapshot policy, see Create a scheduled snapshot policy. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, find the desired snapshot in the list and click Modify in the Operation column. 4. In the Modify Snapshot Policy dialog box, modify the attributes of the snapshot. 5. Click OK. |
| Lock or unlock a snapshot | You can lock snapshots used for long- term businesses. Locked snapshots cannot be deleted. To delete a locked snapshot, unlock it first. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, unlock or lock the desired snapshot. Lock a snapshot: Select the snapshot that you want to lock and click Lock below the list. In the message that appears, click OK. Unlock a snapshot: Select the snapshot that you want to unlock and click Unlock below the list. In the message that appears, click OK. |
| Delete a snapshot | If you no longer use a snapshot, you can delete it. Important Unlocked snapshots cannot be deleted. To delete an unlocked snapshot, unlock it first. For more information, refer to the steps for locking and unlocking snapshots. Deleted snapshots cannot be restored. Proceed with caution. | 1. Log in to the EFS-NAS console. 2. In the left-side navigation pane, click Snapshot. 3. On the Directory Snapshot tab, use one of the following methods to delete snapshots. Delete a single snapshot: Click Delete in the Operation column of the snapshot. In the message that appears, click OK. Delete multiple snapshots at a time: Select the snapshots that you want to delete and click Delete in the Operation column. In the message that appears, click OK. |

### 7.3 Create a scheduled snapshot policy

**policy**

Create an automatic snapshot policy that you can later associate with a file system to enable automatic snapshots.

**Usage notes**

You can create a maximum of 128 automatic snapshot policies. You can associate a single file system with up to 8 automatic snapshot policies. An automatic snapshot policy applies to file systems within the selected organization, resource group, region, and cluster. Before you configure a policy, evaluate your cluster's storage capacity and backup requirements to prevent resource waste or performance degradation.

**Procedure**

1. Log on to the EFS-NAS console.
2. In the left navigation pane, click **Snapshot**.
3. On the **Snapshot** page, click the **Scheduled Snapshot Policy** tab, and then click **Create**
**SnapshotPolicy**.
4. On the **Create Scheduled Policy** page, configure the following parameters.

| Parameter | Description |
|---|---|
| Organization | The organization and resource set to which the automatic snapshot policy belongs. |
| Resource Set |   |
| Region | The region to which the automatic snapshot policy belongs. |
| Cluster | The cluster where the policy will apply. This policy can be associated only with file systems in the same cluster. |
| Name | The name of the automatic snapshot policy. The name must be 1 to 128 characters in length and can contain uppercase letters, lowercase letters, digits, periods (.), underscores ( ), and hyphens (-). _ |
| Description | (Optional) Enter a brief description to explain the purpose or background of the automatic snapshot policy. |

| Snapshot Cycle | The interval at which automatic snapshots are created. You can select Daily, Weekly, or Monthly. If you select Weekly, specify the day of the week. If you select Monthly, specify the day of the month. |
|---|---|
| Snapshot Point in Time | The time when the system automatically creates snapshots. Time Period: The system automatically creates snapshots within the selected time period at the configured interval. If you set an interval in minutes, the system creates a snapshot at that minute of each hour. Point in Time: The system automatically creates snapshots at the selected time points. You can select multiple on-the-hour time points. |
| Delete on Expiration | The expiration and deletion policy for snapshots. You can select Custom or Never Delete. Custom: Specify a custom retention period for automatic snapshots. After a snapshot expires, it is automatically deleted. Never Delete: The system never automatically deletes these snapshots. |
| Custom Deletion Policy | This parameter is required when you set Delete on Expiration to Custom. Specify the retention period by entering a value and selecting a unit (Hours, Days, Months, or Years). |

5. Click **Submit**.

**Related operations**

After you create an automatic snapshot policy, you can manage the policy and its snapshots.

| Feature | Description |
|---|---|
| View automatic snapshot policy details | In the list of automatic snapshot policies, you can view information such as the policy name, snapshot schedule, expiration and deletion settings, and the number of associated file systems. |
| Modify an automatic snapshot policy | You can modify an automatic snapshot policy if it no longer meets your business requirements. 1. In the list of automatic snapshot policies, find the policy that you want to modify and click Modify in the Operation column. 2. In the Modify Policy dialog box, modify the policy name, description, recurrence, and time settings. 3. Click OK. |

| Delete an automatic snapshot policy | You can delete automatic snapshot policies that you no longer need. Important Before you delete an automatic snapshot policy, make sure that it is not associated with any file systems. Unassociating a policy from a file system does not delete the file system itself. An automatic snapshot policy cannot be recovered after it is deleted. Proceed with caution. 1. Unassociate file systems. If the policy is associated with any file systems, you must first unassociate them. i. In the list of automatic snapshot policies, click the name of the policy. ii. On the Policy details page, find the file system that you want to unassociate, click Disassociate in the Operation column, and then confirm the action. 2. Delete the automatic snapshot policy. In the list of automatic snapshot policies, find the policy that you want to delete, click Delete in the Operation column, and then confirm the deletion. |
|---|---|

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

**Procedure**

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

**Procedure**

1. Log in to the Elastic File Storage-File Storage NAS (EFS-NAS) console.
2. In the left-side navigation tree, click **WORM Strategy**.
3. In the WORM policy list, click **Modify** in the **Operation** column of a file system.
4. In the **Modify WORM** dialog box, extend the protection periods.

**Important**

The value of **Default Retention Period** must be equal to or greater than the value of
**Minimum Retention Period**, and it must be equal to or smaller than the value of
**Maximum Retention Period**.
5. Click **OK**.
After the protection periods are extended, the changes take effect immediately on all files stored in the file system.
