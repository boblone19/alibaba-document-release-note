---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS User Guide 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 68
source_pdf: "a46a15d3aee9df1f_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS User Guide 20260827.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20NAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20File%20Storage%20NAS%20User%20Guide%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS User Guide 20260827

## Table of Contents

- 1 What is NAS?
- 2 Usage notes
- 3 Quick start
  - 3.1 Log on to the NAS console
  - 3.2 Create a file system
  - 3.3 Create a permission group and add rules
  - 3.4 Add a mount point
  - 3.5 Mount an NFS file system
  - 3.6 Mount an SMB file system
- 4 File systems
  - 4.1 View the details of a file system
  - 4.2 Delete a file system
  - 4.3 Scale up a file system
- 5 Mount targets
  - 5.1 View mount targets
  - 5.2 Enable or disable a mount target
  - 5.3 Delete a mount target
  - 5.4 Modify the permission group of a mount target
- 6 Permission groups
  - 6.1 View permission groups
  - 6.2 Delete a permission group
  - 6.3 Manage permission group rules
- 7 Manage quotas
- 8 Manage unified namespaces
- 9 Lifecycle management
- 10 Directory-level ACLs that grant the read and write access
  - 10.1 Overview
  - 10.2 Features
  - 10.3 Use POSIX ACLs to control access
  - 10.4 Use NFSv4 ACLs to control access

## 1 What is NAS?

File Storage NAS (NAS) is a cloud service that provides file storage solutions for compute nodes. The compute nodes include Elastic Compute Service (ECS) instances and Container Service for Kubernetes (ACK) clusters. NAS provides standard file access protocols. You can use the distributed file storage solution that provides shared access, scalability, high reliability, and high performance without the need to modify the configurations of the applications. You can mount a NAS file system on multiple compute nodes at a time. This reduces a large number of costs in data transmission and synchronization. NAS is extremely elastic and extensible. The performance of an NAS cluster linearly increases with the size of the cluster. A single NAS cluster supports hundreds of storage nodes and can store tens of petabytes of data. You can perform the following operations: Create a NAS file system and mount target. Create a permission group for the file system and add rules to the permission group. This allows access from specific IP addresses or CIDR blocks to the file system. This also allows you to grant different levels of access permissions to the IP addresses or CIDR blocks. Mount the file system to compute nodes, such as ECS instances and ACK clusters. NAS allows you to access the file system by using the Network File System (NFS) and Server Message Block (SMB) protocols. You can also call POSIX-based APIs to access the file system. Manage file systems, mount targets, and permission groups in the NAS console. Call NAS API operations to manage file systems.

## 2 Usage notes

Before you use File Storage NAS (NAS), take note of the following limits.

**Limits on file systems**

Maximum number of files in each file system: 1 billion. Maximum length of a file system name: 128 characters. Maximum size of each file: 32 TiB. Maximum directory depth: 1,000 levels. Maximum capacity of a Capacity NAS file system: 10 PiB. Maximum number of compute nodes on which a file system can be mounted and from which the file system allows simultaneous access: 10,000. Maximum size of a protocol packet: 4 MiB. Maximum number of Change Notify requests: 512.

**Limits on NFS clients**

The following list describes the limits on the usage of NFS clients: You can open up to 32,768 files at a time on an NFS client. Files in the list folder and its subfolders are not counted as part of the total number of open files. Each mount on an NFS client can obtain up to 8,192 locks across up to 256 files or processes. For example, a single process can obtain one or more locks on 256 separate files, or 8 processes can each obtain one or more locks on 32 files. We recommend that you do not use an NFS client in a Windows host to access an NFS file system.

**Limits on SMB clients**

Each file or folder can be opened up to 8,192 times in parallel across compute nodes that each have a file system mounted and users that share access to each of these file systems. This represents up to 8,192 active file handlers for each file system. A file system can have up to 65,536 active file handles.

**Limits on the NFS protocol**

NAS supports the NFSv3 and NFSv4 protocols. NFSv4.0 does not support the following attributes: FATTR4_MIMETYPE, FATTR4_QUOTA_AVAIL_HARD, FATTR4_QUOTA_AVAIL_SOFT, FATTR4_QUOTA_USED, FATTR4_TIME_BACKUP, and FATTR4_TIME_CREATE. If one of the preceding attributes is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on the client on which the file system is mounted. NFSv4.1 does not support the following attributes: FATTR4_DIR_NOTIF_DELAY, FATTR4_DIR_NOTIF_DELAY, FATTR4_DACL, FATTR4_SACL, FATTR4_CHANGE_POLICY, FATTR4_FS_STATUS, FATTR4_LAYOUT_HINT, FATTR4_LAYOUT_TYPES, FATTR4_LAYOUT_ALIGNMENT, FATTR4_FS_LOCATIONS_INFO, FATTR4_MDSTHRESHOLD, FATTR4_RETENTION_GET, FATTR4_RETENTION_SET, FATTR4_RETENTEVT_GET, FATTR4_RETENTEVT_SET, FATTR4_RETENTION_HOLD, FATTR4_MODE_SET_MASKED, and FATTR4_FS_CHARSET_CAP. If one of the preceding attributes is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on the client on which the file system is mounted. NFSv4 does not support the following operations: OP_DELEGPURGE, OP_DELEGRETURN, and NFS4_OP_OPENATTR. If one of the preceding operations is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on the client on which the file system is mounted. NFSv4 does not support delegations. UID and GID On Linux, mappings between UIDs or GIDs and usernames or group names are defined in configuration files. For NFSv3 file systems, if the mapping between an ID and a name is defined in a configuration file, the name is displayed. If no mapping can be found for a UID or GID, the UID or GID is displayed. For NFSv4 file systems, if the version of a Linux kernel is earlier than 3.0, the usernames and group names are displayed as nobody for all files. If the kernel version is later than 3.0, the rule used by NFSv3 file systems applies to display files.

> **Important:** If the Linux kernel version is earlier than 3.0, we recommend that you do not run the change owner or chgrp command for files or directories in an NFSv4 file system. Otherwise, the UID and GID of the file or directory are changed to nobody.

**Limits on the SMB protocol**

NAS supports the SMB 2.1 protocol and later versions. NAS also supports operating systems including Windows 7, Windows Server 2008 R2, and later versions. NAS does not support Windows Vista, Windows Server 2008, or earlier versions. Compared with SMB 2.1 and later versions, SMB 1.0 provides lower performance and fewer features. Windows products that support only SMB 1.0 have reached end of support. SMB file systems do not support extended file attributes or lease-based client-side caching. SMB file systems do not support I/O control (IOCTL) or file system control (FSCTL) operations. For example, you cannot create sparse files, compress files, check the status of network interface cards (NICs), or create reparse points. SMB file systems do not support alternate data streams. SMB file systems do not support identity authentication that is provided by Active Directory (AD) or Lightweight Directory Access Protocol (LDAP). SMB file systems do not support several features that are provided by SMB 3.0 or later, such as SMB Direct, SMB Multichannel, SMB Directory Leasing, and Persistent File Handle. SMB file systems do not support access control lists (ACLs) on files or directories.

**Other limits**

Before you delete a NAS file system, you must unmount the file system from the mount target on the compute node. Then, delete the mount target and the file system.

## 3 Quick start

### 3.1 Log on to the NAS console

This topic describes how to log on to the File Storage NAS console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

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

5. In the top navigation bar, click **Products**. In the **Storage** section, click **File Storage NAS**.

### 3.2 Create a file system

This topic describes how to create a file system in the File Storage NAS (NAS) console.

**Background information**

Before you create a file system, take note of the following items: You can use an Alibaba Cloud account to create a maximum of 1,000 file systems. The maximum capacity of a Capacity NAS file system is 10 PiB. If you want to increase the maximum storage capacity, we recommend that you contact Alibaba Cloud technical support.

**Procedure**

1. Log in to the File Storage NAS console.
2. In the left-side navigation pane, choose **File System > File System List**. On the page
that appears, click **Create File System**.
3. On the **Create File System** page, configure the following parameters.
After you complete the configuration, the configuration information is displayed in the rightside section. The following table describes the required parameters.

| Parameter |   | Description |
|---|---|---|
| Billing Configurati on | Billing Method | The Pay-as-you-go and Subscription billing methods are available. Pay-as-you-go: You can use the service first. Fees are charged afterward based on the actual amount of resources that you used. This method is suitable for scenarios in which business usage frequently fluctuates, which allows users to flexibly utilize resources based on actual needs and avoid waste. Subscription: You can directly subscribe to resources for a fixed period of time, and fees are charged based on the quantity and subscription duration. No additional fees are incurred within the billing cycle. This method is suitable for scenarios where business usage is relatively stable. Note This parameter is displayed only if the administrator has configured billing rules in the operations center. For more information about the billing rules, see the Billing rules topic in Apsara Uni-manager Management Console User Guide. |

| Area | Organization/R esource Set | The organization and resource set to which the file system belongs. |
|---|---|---|
|   | Region/Zone ID | The region and zone to which the file system belongs. |
|   | Cluster | The cluster where the file system resides. |
| Basic Configurati ons | File System Name | The name of the file system. The file system name must comply with the following naming conventions: The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with http:// or https://. The name can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). |
| Storage Configurati ons | Storage Class | Select Capacity. The maximum capacity of a Capacity NAS file system is 10 PiB. |
|   | Protocol Type | The protocol. Select NFS or SMB based on your business requirements. We recommend that you mount Network File System (NFS) file systems on Linux clients and Server Message Block (SMB) file systems on Windows clients. |
|   | Capacity (TiB) | The capacity of the file system. Valid values: 0.1 to 10240. Unit: TiB. |

4. Optional. If you want to set quotas for the resources of a service, click **Quota**
**Management** on the right side of the page to go to the **Quotas** page. For more
information, see the **Quota management** topic in User Guide - Apsara Uni-manager Mana gement Console.
5. After you configure the preceding parameters, click **Confirm Order**.

### 3.3 Create a permission group and add rules

**add rules**

This topic describes how to create a permission group and add rules to the permission group in the File Storage NAS (NAS) console.

**Background information**

In NAS, each permission group functions as a whitelist. By adding rules to a permission group, you can authorize specific IP addresses or CIDR blocks to access the file system, and grant them different levels of access permissions.

**Precautions**

Each Alibaba Cloud account can create up to 100 permission groups. To increase the upper limit, contact the Alibaba Cloud technical support. NAS supports only IPv4 by default. To use IPv6, contact the Alibaba Cloud technical support to enable the IPv6 feature for your cluster before proceeding.

**Create a permission group**

1. Log in to the File Storage NAS console.
2. Select **File System > Permission Group**. On the **Permission Group** page, click **Create**
**Permission Group**.
3. In the **Create Permission Group** dialog box, configure the parameters.
After the configuration, you can view the configuration overview in the right-side section of the page. The following table describes the required parameters.

| Parameter |   | Description |
|---|---|---|
| Area | Organization/Res ource Set | The organization and resource set to which the permission group belongs. |
|   | Region | The region in which to create the permission group. |
| Basic Configurations | Permission Group Name | The name of the permission group. The naming rules for a permission group are as follows: The name must be 3 to 64 characters in length. The name can contain letters, digits, and hyphens (-). |
|   | Network Type | The network type. Select Classic Network or VPC based on your business requirements. Important You must select VPC when using the IPv6 feature. |
|   | Description | Enter the description of the permission group. It must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), and colons (:). It must start _ with a letter, and cannot start with http:// or https://. |

4. Click **Submit**. The permission group is created.

**Add a rule to the permission group**

1. Log in to the File Storage NAS console.
2. On the **Permission Group** page, find the target permission group and click **Manage**
**Rules** in the **Actions** column.
3. Click **Create Rule**.
4. In the **Create Rule** dialog box, configure the parameters.
The following table describes the required parameters.

| Parameter | Description |
|---|---|
| Authorization Type | By default, permission groups support only IPv4 Access Address. After enabling the IPv6 feature for a cluster, you can select IPv6 Access Address. Select an authorization type based on the IP address type. |
| Authorized Address | The authorization object to which the rule is applied. You can specify an IP address or CIDR block. Only IP addresses are available for permission groups of the classic network type. |
| Read/Write Permissions | Allows authorization objects to perform read-only or read /write operations on the file system, supporting Read-only and Read/Write. |
| User Permissions | Whether to restrict the access of Linux users of the authorized object to the file system. No Anonymity (no squash): Allows the root user to access the file _ system. Root User Anonymity (root squash): Maps the nobody user to the _ root user. General Anonymity (all squash): All users are mapped as nobody _ users. The nobody user is the default user of the Linux and can only access public content on the server. It has the characteristics of low permissions and high security. |
| Priority | If the same authorization object matches multiple rules, a high-priority rule overwrites a low-priority rule. You can select 1 to 100.1 is the highest priority. |

5. Click **OK** to add the rule.

**Batch add rules**

1. Prepare a local EXCEL file to import rules. Configure the rule data as described in the
following table.

| Table heade r | SourceCidrIp | RWAccessType | UserAccessType | Priority |
|---|---|---|---|---|

| Rule | The authorization object to which the rule is applied. You can specify an IP address or CIDR block. Only IP addresses are available for permission groups of the classic network type. | Read/write permissions: RDONLY: Read- only RDWR: Read/Write | User permissions: no squash: No _ Anonymity root squash: Root User _ Anonymity all squash: General _ Anonymity | The priority of the permissions. Valid values: 1 to 100. A value of 1 indicates the highest priority. |
|---|---|---|---|---|

Example:
2. Log in to the File Storage NAS console.
3. On the **Permission Group** page, find the target permission group and click **Manage**
**Rules** in the **Actions** column.
4. Click **Create Rules**. In the pop-up dialog box, select the rule file that you want to import
and click **Open**.
5. In the **Create Rules** dialog box, view or modify the rules. After you confirm the rules, select
the rules to add and click **Submit**.

### 3.4 Add a mount point

In File Storage NAS (NAS), you must use a mount point to mount file systems to compute nodes (ECS instances or containers). This topic describes how to add a mount point.

**Prerequisites**

Make sure that you have completed the following operations: Create a file system. Create a permission group and add rules. You have created a Virtual Private Cloud (VPC) in the same region as the NAS file system, and an Elastic Compute Service (ECS) instance in that VPC.

> **Important:** To use IPv6, select VPC as the network type and configure IPv6 endpoint authorization when you create a permission group and rules; assign an IPv6 CIDR block when you create a VPC; and enable IPv6 private network when you create an ECS instance.

**Background Information**

A mount point is an access endpoint for a file system instance within a VPC or classic network. Each mount point corresponds to a domain name. NAS supports two types of mount points: VPC and Classic Network.

> **Note:** The same mount point can be mounted simultaneously by multiple compute nodes (ECS instances or containers) for shared access.

**Procedure**

1. Log in to the File Storage NAS console.
2. Select **File System > File Systems**.
3. Find the target file system and click **Manage**.
4. In the left-side navigation pane, select **Mount Targets**.
5. In the **Mount Target** section, click **Add Mount Target**.
6. In the **Add Mount Target** dialog box, configure the parameters.
**Mount Target Type**: Includes **VPC** and **Classic Network**.

> **Note:** Classic Network-type mount points can be accessed only by ECS instances under the same Alibaba Cloud account.

If you want to add a VPC-type mount point, configure the following parameters.

> **Important:** To use IPv6, turn on the **Enable IPv6** switch, and then select a VPC that supports IPv6, its associated vSwitch, and a permission group authorized for IPv6 endpoint access.
> A VPC labeled **Dual-Stack** in the VPC list indicates that IPv4/IPv6 dual-stack is enabled for the VPC.

> An ECS instance must have IPv6 private network enabled before accessing NAS over IPv6.

| Parameter | Description |
|---|---|
| VPC Network | Select an existing VPC network. Note The VPC network and vSwitch must match those selected for the compute nodes (ECS instances or containers). |
| vSwitch | Select a vSwitch created under the VPC network. |
| Permission Group | Select an existing permission group. |
| Enable IPv6 | Turn on the Enable IPv6 switch to enable IPv6 for the mount point. |

If you want to add a Classic Network-type mount point, configure the following parameters.

| Parameter | Description |
|---|---|
| Permission Group | Select an existing permission group. |

7. Click **OK** to add the mount point.

### 3.5 Mount an NFS file system

Before you mount a file system, you must create the file system and a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes. The compute nodes include Elastic Compute Service (ECS) instances and Container Service for Kubernetes (ACK) clusters. This topic describes how to mount a Network File System (NFS) file system.

**Prerequisites**

A file system is created. For more information, see Create a file system. A permission group is created and one or more rules are added to the permission group. For more information, see Create a permission group and add rules. A mount target is created. In this example, a mount target of the VPC type is used. For more information, see Add a mount point. If the mount target of a file system resides in a virtual private cloud (VPC), you can mount the file system only on an ECS instance in the VPC. The IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target. If the mount target of a file system resides in the classic network, you can mount the file system only on an ECS instance that belongs to the same Alibaba Cloud account as the mount target. The private IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target. A compute node is created. In this example, a Linux ECS instance is used.

**Step 1: Install an NFS client**

Before you mount an NFS file system on a Linux ECS instance, you must install an NFS client. If an NFS client is installed, skip this step.
1. Log on to the Linux ECS instance. For more information, see the **Connect to an instance**
section of the Get started topic in ECS User Guide.
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

1. Log on to the Linux ECS instance. For more information, see the **Connect to an instance**
section of the Get started topic in ECS User Guide.
2. Mount the NFS file system.
Run the following command to mount the NFS file system. In the command, replace `file-` `system-id.region.nas.aliyuncs.com:/ /mnt` with an actual value. Use the NFSv4 protocol to mount a file system:

```python
sudo mount -t nfs -o vers=4.0,minorversion=0,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvpo file-system-id.region.nas.aliyuncs.com:/ /mnt
```

Use the NFSv3 protocol to mount a file system:

```python
sudo mount -t nfs -o vers=3,nolock,proto=tcp,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvpo file-system-id.region.nas.aliyuncs.com:/ /mnt
```

Table 1. Mount parameters

| Parameter | Description |
|---|---|

| file-system- id.region.nas.aliyu ncs.com:/ /mnt | <Endpoint of the mount target>:<Name of the shared directory> <Path of the mount directory>. Replace the domain name of the mount target, the name of the shared directory, and the path of the mount directory with actual values. Endpoint of the mount target: You can log on to the NAS console, find the file system that you want to manage, and then click Manage to go to the Details page. Then, you can obtain the endpoint of the mount target of the file system on the Mounting Use tab. Directory of the NAS file system: the root directory (/) or a subdirectory, for example, /sub1. If a subdirectory is specified, make sure that the subdirectory exists. Path of the mount directory : the root directory / of the Linux ECS instance or a subdirectory, for example, /mnt. If the mount directory is a subdirectory, make sure that the subdirectory exists. |
|---|---|
| vers | The protocol version of the file system. Only NFSv3 and NFSv4 are supported. vers=3: uses NFSv3 to mount the file system. vers=4.0: uses NFSv4 to mount the file system. |

| Mount options. | If you want to mount a file system, you can specify multiple mount options. Separate multiple mount options with commas (,). For example, you can specify the following mount options: rsize: specifies the size of each data block that a client can read from the file system. Recommended value: 1048576. Unit: bytes. wsize: specifies the size of each data block that a client can write to the file system. Recommended value: 1048576. Unit: bytes. Note To prevent performance degradation, we recommend that you specify the maximum value (1048576) for both the rsize mount option and the wsize mount option. hard: specifies that applications stop accessing a file system when the file system is unavailable, and wait until the file system is available. We recommend that you enable the hard parameter. timeo: specifies the period of time for which the NFS client waits before the client retries to send a request. Unit: deciseconds (tenths of a second). Recommended value: 600 (60 seconds). Note If you need to modify the timeo mount option, we recommend that you specify 150 or a greater value. The timeo mount option is measured in deciseconds (tenths of a second). For example, the value 150 indicates 15 seconds. retrans: specifies the number of retries after the NFS client fails to send a request. Recommended value: 2. noresvport: specifies that a new TCP port is used to ensure network connectivity between the file system and the ECS instance when the network recovers from failure. We recommend that you enable the noresvport parameter. Note When you configure parameters, take note of the following items: To prevent data inconsistency, we recommend that you do not use the soft mount option. Use of the soft option is at your own risk. We recommend that you use the default values for other mount options. A decrease in performance may occur due to changes in specific mount options. These mount options include the size of the read or write buffer or the use of attribute caching. |
|---|---|

3. Run the `mount -l` command to view the mount result.
If the output that is similar to the following information appears, the mount is successful. After the file system is mounted, you can run the `df -h` command to view the size of the file system.
4. After the SMB file system is mounted, you can read data from and write data to the NAS file
systems on the ECS instance. You can access the file system the same way you access a local directory. The following figure shows an example.

### 3.6 Mount an SMB file system

Before you mount a file system, you must create the file system and a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes such as Elastic Compute Service (ECS) instances. This topic describes how to mount a Server Message Block (SMB) file system.

**Prerequisites**

1. A file system is created. For more information, see Create a file system.
2. A permission group is created and one or more rules are added to the permission group.
For more information, see Create a permission group and add rules.
3. A mount target is created. In this example, a mount target of the VPC type is used. For
more information, see Add a mount point. If the mount target of a file system resides in a virtual private cloud (VPC), you can mount the file system only on an ECS instance in the VPC. The IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target. If the mount target of a file system resides in the classic network, you can mount the file system only on an ECS instance that belongs to the same Alibaba Cloud account as the mount target. The private IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target.
4. An ECS instance is created. In this example, a Windows ECS instance is used.
5. The following services on the Windows host are started:
Workstation a. Choose **All Programs > Accessories > Run**, or press `Win+R` and enter `services.msc` to go to the Services console. b. Make sure that the Workstation service is in the **Started** state and the startup type is
**Automatic**.
By default, the Workstation service is in the Started state. TCP/IP NetBIOS Helper To start the TCP/IP NetBIOS Helper service, perform the following steps: a. On the **Network and Sharing Center** page, click the active network connection. b. Click **Properties** to open the Local Area Network Properties dialog box. Double-click
**Internet Protocol Version 4 (TCP/IPv4)** to open the Internet Protocol Version 4
(TCP/IPv4) Properties dialog box, and then click **Advanced**. c. In the **Advanced TCP/IP Settings** dialog box, choose **WINS > Enable NetBIOS over**
**TCP/IP**.
d. Choose **All Programs > Accessories > Run**, or press `Win+R` and enter `services.msc` to go to the Services console. e. Make sure that the TCP/IP NetBIOS Helper service is in the **Started** state and the startup type is **Automatic**. By default, the TCP/IP NetBIOS Helper service is in the Started state.

**Procedure**

1. Log on to the Windows ECS instance. For more information, see the **Connect to an**
**instance** section of the Get started topic in ECS User Guide.
2. Open the Command Prompt and run the following command to mount an SMB file system:

```
net use D: \\file-system-id.region.nas.aliyuncs.com\myshare
```

The syntax of the command is net use <the letter of a local drive> \\<the domain name

```
of a mount target>\myshare .
```

Letter of the destination drive: the letter of the drive on which you want to mount an SMB file system. Replace the value of the parameter with the letter of an actual destination drive.

> **Note:** The letter of the destination drive must be different from the existing drive letters.

The domain name of the mount target: When you create a mount target for a file system, the domain name of the mount target is automatically generated. You can replace the domain name based on your business requirements. To obtain the mount target of the file system, perform the following steps: Log on to the NAS console, find the file system that you want to manage, and then click **Manage** to go to the Details page. myshare: the name of the shared SMB directory. You cannot change the name.
3. Run the `net use` command to check the mount result.
If the output that is similar to the following information appears, the mount is successful.
4. After the SMB file system is mounted, you can read data from and write data to the NAS file
systems on the ECS instance.

## 4 File systems

### 4.1 View the details of a file system

**system**

This topic describes how to view the details of a file system. The details include the information about the file system and the attached mount targets. You can view the details of a file system in the File Storage NAS console.

**Prerequisites**

A file system is created. For information about how to detach a tag policy from an object, see Create a file system.

**Procedure**

1. Log on to the NAS console.
2. Choose **NAS > File System List**.
3. Find the file system and click **Management** to go to the details page of the file system.
The details page consists of the following sections:
**Basic Information**: In this section, the information about the file system is displayed.
The information includes the ID, region, protocol type, and storage specifications.
**Mounting Targets**: In this section, the list of mount targets attached to the file system
is displayed. You can manage the mount targets and view the clients on which the file system is mounted.
**Quota Management**: In this section, the quota status of each directory in the file
system is displayed. You can create, modify, and delete quotas for each directory.

### 4.2 Delete a file system

This topic describes how to delete a file system in the File Storage NAS console.

**Prerequisites**

The number of mount targets is 0. For more information about how to view the number of mount targets, see View the details of a file system.

**Procedure**

1. Log on to the NAS console.
2. Choose **NAS > File System List**.
3. Find the file system that you want to manage, and click **Manage**.

> **Important:** Before you can delete a file system, you must remove all mount targets from the file system.
> Proceed with caution when you delete a file system. After a file system is deleted, the data on the file system cannot be restored. Make sure that all data is backed up.

4. In the **Delete File System** dialog box, click **OK** to complete the deletion.

### 4.3 Scale up a file system

If the used space of an File Storage NAS file system reaches the specified capacity, data can no longer be written to the file system. To ensure the availability of the NAS service, we recommend that you scale up the file system before the used space reaches the specified capacity. This topic describes how to scale up a file system in the NAS console.

**Prerequisites**

Create a file system.

> **Important:** A file system can be scaled up but cannot be scaled down. . A Capacity NAS file system can be scaled out to up to 10 PiB.

**Procedure**

1. Log in to the File Storage NAS console.
2. In the left-side navigation pane, choose **File System > File System List**.
3. Find the file system and click **Upgrade** in the **Operations** column.
4. In the **Upgrade** dialog box, specify a desired capacity for the file system in the **New Total**
**Capacity** field.
5. Click **OK**.

## 5 Mount targets

### 5.1 View mount targets

This topic describes how to view mount targets in the File Storage NAS console.

**Background information**

The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Optional. The update package is verified.

**Procedure**

1. Log in to the File Storage NAS console.
2. Choose **NAS > File System List**.
3. Find the file system and click **Management** in the Actions column.
4. In the left-side navigation pane, click **Mounting Targets**. On the **Mounting Target** tab,
view the mount targets of the file system.

### 5.2 Enable or disable a mount target

**target**

This topic describes how to enable or disable a mount target. You can control access to a mount target from clients by enabling or disabling the mount target.

**Prerequisites**

The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Optional. The update package is verified.

**Procedure**

1. Log in to the File Storage NAS console.
2. Choose **NAS > File System List**.
3. Find the file system and click **Management** in the Actions column.
4. In the left-side navigation pane, click **Mounting Targets**. After you find the mount target
that you want to disable or enable, you can perform the following operations: To disable the mount target, click **Disable**. In the Disable Mount Target dialog box, click
**OK** to deny access to the mount target from clients.
To enable the mount target, click **Enable**. In the Enable Mount Target dialog box, click
**OK** to allow access to the mount target from clients.

### 5.3 Delete a mount target

This topic describes how to delete a mount target in the File Storage NAS console.

**Prerequisites**

A file system is unmounted from the compute node such as an ECS instance and ACK cluster on which you mounted the file system by using a mount target. The mount targets that are created by using a Cross-domain mount orchestration are deleted.

**Procedure**

1. Log in to the File Storage NAS console.
2. Choose **NAS > File System List**.
3. Find the file system and click **Management** in the Actions column.
4. In the left-side navigation pane, click **Mounting Targets**.
5. Find the mount target that you want to delete and click **Delete**.

> **Important:** Proceed with caution when you delete a mount target. After you delete a mount target, you cannot restore the mount target.

6. In the Delete Permission Group message, click **OK**.

### 5.4 Modify the permission group of a mount target

**of a mount target**

You must add a permission group to each mount target. You can modify the permission group of a mount target in the File Storage NAS console.

**Prerequisites**

The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Optional. The update package is verified.

**Procedure**

1. Log on to the NAS console.
2. Choose **File System > File System List**.
3. Find the file system and click **Management** in the Actions column.
4. Click **Mounting Targets** to go to the **Mounting Target** tab.
5. Find the mount target that you want to modify and click **Modify Permission Group**.
6. In the **Modify Permission Group** dialog box, change the permission group and click **OK**.

## 6 Permission groups

### 6.1 View permission groups

This topic describes how to view permission groups in the File Storage console.

**Prerequisites**

A permission group is created. For information about how to detach a tag policy from an object, see Create a permission group and add rules.

**Procedure**

1. Log in to the File Storage NAS console.
2. Choose **File System > Permission Group** and view the permission groups.

### 6.2 Delete a permission group

This topic describes how to delete a permission group in the File Storage NAS console.

**Prerequisites**

A permission group is created. For more information, see Create a permission group and add rules.

**Operating system**

1. Log on to the File Storage NAS console.
2. Choose **NAS > Permission Group**.
3. Find the target permission group and click **Delete**.

> **Note:** Permission groups in use cannot be deleted. Before you can delete a permission group, you must remove the permission group from the linked mount target.

4. In the Delete Permission Group dialog box, click **OK**.

### 6.3 Manage permission group rules

**rules**

This topic describes how to manage permission group rules in the File Storage NAS console. The management includes viewing the details of rules, modifying rules, and deleting rules.

**Prerequisites**

A permission group and a permission group rule are created. For more information, see Create a permission group and add rules.

**Procedure**

1. Log on to the NAS console.
2. Choose **NAS > Permission Group**.
3. Find the target permission group and click **Manage**.
4. On the Rules page, you can perform the following operations:
View all rules for the permission group. Modify a rule. Find the target rule and click **Edit** to modify the details of the rule. The details include the **authorization address**, **read/write permissions**, **user**
**permission**, and **priority**.
Delete a rule. Find the target rule and click **Delete**. In the Delete Rule dialog box, click
**OK**.

## 7 Manage quotas

File Storage NAS (NAS) provides the quota management feature to help you view and manage directory quotas. This topic describes how to create directory quotas, assign quotas to users, delete a quota that is assigned to a user, and edit a quota that is assigned to a user.

**Prerequisites**

A Network File System (NFS) file system of the NAS Capacity type is mounted on an Elastic Compute Service (ECS) instance. For more information, see Mount an NFS file system.

**Quota types**

| Category | Quota type |
|---|---|
| Applicable scope | Directory quotas for all users: the maximum storage space for files that all users can create in a directory of a file system. Directory quotas for a specific user or user group: the maximum storage space for files that a user or user group can create in a directory of a file system. |
| Quota level | Statistical quotas: If you create a statistical quota for a file system, NAS calculates only the usage of storage space in the file system. You can query and view statistical data. Restrictive quotas: If the used storage space for a specified directory in a file system exceeds the quota, you cannot create files or directories, or append data to the files or directories. |

> **Important:** To prevent potential security risks, we recommend that you evaluate and test restrictive quotas before you create the restrictive quotas for core business-related directories.
> NAS performs asynchronous calculation for quotas at the backend. Therefore, the operation to enable or disable a restrictive quota at the backend requires 5 to 15 minutes to take effect.

**Limits**

Only NFS file systems are supported. Quotas For a single file system, you can configure quotas for a maximum of 500 directories. The maximum directory depth is eight levels. For example, the depth of the root directory / is zero level. The depth of the /workspace directory is one level. The depth of the /workspace/dir1 directory is two levels.

**Create a directory quota**

1. Log in to the File Storage NAS console.
2. Choose **NAS > File System List**.
3. Find the target file system and click **Manage** in the Actions column. In the left-side
navigation pane of the page that appears, click **Quota Management**.
4. On the **Quota Management** page, click **Create Directory Quota**.
5. In the **Create Directory Quota** dialog box, enter the directory in the **Directory Path**
field.

> **Important:** The value of the **Directory Path** field of a quota is the absolute path of the directory in the NFS file system, instead of the local path on the compute node.
> The directory path cannot contain Chinese characters.

For example, a NAS file system is mounted at the `/mnt` directory. The root directory is

| / | , and the N |
|---|---|

`/` , and the NAS file system has a level-1 subdirectory `/dir0` and a level-2 subdirectory `/dir/subdir1` . If you want to configure a quota for the root directory, level-1 subdirectory, and level-2 subdirectory, enter the following directory paths: Root directory: `/` Level-1 subdirectory: `/dir0` Level-2 subdirectory: `/dir/subdir1`
6. Query the status of the quota.
After the quota is created, the quota is automatically initialized and is in the **Initializing** state. The duration of the initialization process depends on the number of files and subdirectories in the directory of your file system. After the quota is initialized, the quota is in the **Running** state. In the list of user quotas, a quota for which the user type is All Users and the quota type is Statistical is automatically generated. You can change only the quota type, but not the user type of the user quota.

**Assign a directory quota to a user**

For a statistical quota, you can view the size and number of files that are used by a user or user group in a directory. For a restrictive quota, you can limit the size and number of files that a user or user group can create in a directory.

> **Note:** Only NFS file systems support directory quotas for a specific user or user group.
> Only one type of quota can be configured for each user type.

**Procedure**

On the **Quota Management** page, find the directory path and click **Manage Quotas** in the Actions column. In the panel that appears, click **Assign Quota to User**. In the Assign Quota to User dialog box, configure the parameters. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| User Type | Yes | The user type. Valid values: UID, GID, and All Users. The value UID indicates a user. The value GID indicates a user group. The value All Users indicates all users. You can assign different quotas to multiple users for a directory. |

| ID | No | This parameter is required if you set the User Type parameter to UID or GID. This parameter specifies the ID of a user or the group ID (GID) of a user group. Example: If you want to assign a quota to a user whose ID is 500, set the User Type parameter to UID and set the ID parameter to 500. If you want to assign a quota to a user group whose ID is 100, set the User Type parameter to GID and set the ID parameter to 100. |
|---|---|---|
| Quota Type | Yes | Statistical: If you set this parameter to Statistical, NAS calculates only the usage of storage space in a specified directory of the file system. Restrictive: If you set this parameter to Restrictive and the restrictive quota is used up, I/O operations can no longer be performed. |
| Capacity Limit (GiB) | No | This parameter is required if you set the Quota Type parameter to Restrictive. This parameter specifies the maximum size of files that a user can create in a directory. Note The minimum value is 1 GiB and the maximum value is 10,000,000 GiB. You must configure at least one of the Capacity Limit (GiB) and File Limit parameters. |
| File Limit | No | This parameter is required if you set the Quota Type parameter to Restrictive. This parameter specifies the maximum number of files and subdirectories that a user can create in a directory. Note You must configure at least one of the Capacity Limit (GiB) and File Limit parameters. The minimum number of files is 1, and the maximum number of files is 1,000,000,000. |

**Delete a directory quota that is assigned to a user**

In the list of quotas, find the quota that you want to delete and click **Delete** in the Actions column.

> **Note:** When you delete a directory from a file system, NAS also deletes all the directory quotas and user quotas configured for the directory.

**Modify a directory quota that is assigned to a user**

In the list of quotas, find the quota that you want to modify, and click **Edit** in the Actions column. You can modify the quota type, capacity limit, and file limit of the quota.

> **Note:** The Capacity Limit and File Limit parameters are available only for restrictive quotas. You must modify at least one of the two parameters.

spaces

## 8 Manage unified namespaces

**namespaces**

This topic describes how to create a unified namespace and create a mount target for the unified namespace in the Apsara File Storage NAS console. The topic also describes how to add, remove, and modify file systems in a namespace, view namespace details, and enable the cross-domain mount orchestration feature.

**Features**

A unified namespace allows you to mount multiple file systems on a NAS cluster by using a single endpoint. You do not need to maintain multiple mount targets and mount directories. You can create a mount target for a unified namespace. You can use a unified namespace to manage multiple file systems the same way you manage a single file system. A unified namespace contains a virtual root directory in which file systems are the first-level subdirectories. After you add a file system to a unified namespace, you can still mount the file system by using the mount targets of the file system.

**Limits**

A unified namespace has the following limits: You can add a maximum of 1,000 file systems to each unified namespace. The mapping name of a file system in a unified namespace cannot exceed 255 characters in length. The name can contain only letters, digits, and the following special characters: .+-_()<>@# To enable a cross-domain mount orchestration, the mount directory name of a unified namespace cannot exceed 255 characters. The name can contain only letters, digits, and the following special characters: .+-_()<>@# You can create up to two mount targets for each unified namespace. You can create up to 20 namespaces in each region. You can mount a unified namespace only by using the NFSv3 protocol. The file systems that are added to a namespace must belong to the same Alibaba Cloud account and cluster as the namespace. The storage type, protocol type, and encryption type of the file systems must be the same. The mapping name of a file system must be unique in each unified namespace. File systems can be mapped only to first-level subdirectories in a unified namespace. You cannot modify the access permissions, owner, or access control lists (ACLs).

**Basic features of unified namespace**

Create a unified namespace and create a mount target for the unified namespace. i. Log on to the NAS console. ii. In the left-side navigation pane, choose **Unified Namespace > Unified Namespaces**. iii. On the **Unified Namespaces** page, click **Create Namespace**. Then, create a namespace and a mount target for the namespace as prompted. spaces

> **Note:** If you create mount targets in virtual private clouds (VPCs) for unified namespaces in different regions, we recommend that you use different CIDR blocks. This way, the CIDR blocks can be identified when you mount unified namespaces across regions. For example, you can use `192.168.0.0/16` for Region 1 and

`172.16.0.0/16` for Region 2. For more information, see Step 1: Create a VPC in the Cross-domain mount orchestration section. Add a file system to the unified namespace. After you create the unified namespace, you can add a file system and specify a mapping name for the file system.

> **Note:** The mapping name is the name of the virtual directory for the file system.

Remove the file system from the unified namespace. You can remove the existing file system from the unified namespace.

> **Note:** The file system is not deleted but removed from the file system list of the namespace.

Change the mapping name of the file system. You can change the mapping name of the file system in the unified namespace.

> **Note:** If a symbolic or hard link exists between a file system and another file system, a connection failure may occur when you modify the mapping name of the file system.

View the details of the unified namespace. The details of the namespace are divided into three sections: Properties Mount target list

> **Note:** You can create or delete mount targets.

File system list

> **Note:** You can add or remove file systems.

spaces

**Cross-domain mount orchestration**

In traditional solutions, you can add a file system to a namespace only if the file system and namespace reside in the same region. To add file systems to namespaces across multiple regions, NAS provides the cross-domain mount orchestration feature. To use this feature, perform the following operations: Create a unified namespace and a mount target for the namespace. Map the unified namespace to the local directory tree of a client by using the cross-domain mount orchestration feature. After the orchestration is complete, specify the root directory to generate an automatic mount script.

> **Important:** The specified mount target and mapping path cannot be modified after the map is created. You can remove the map. However, if you create the map again, the specified mount target can only be attached to the original mapping path.

To mount the namespace on a client, you can run the automatic mount script on the client. This allows the client to access file systems across regions. The format of the local path on the client for each unified namespace is `<Specified root directory>/<Mapping path of the`

```
namespace> .
```

To enable a cross-domain mount orchestration for different VPCs that reside in different regions, you must establish VPC connections. The following procedure provides an example on how to establish VPC connections and enable a cross-domain mount.
1. Create two VPCs.
i. Log on to the NAS console. ii. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**. spaces iii. On the **Create VPC** page, create two VPCs. One VPC is for Region 1 and the other VPC is for Region 2. Create a VPC named skvpc1 `192.168.1.0/24` for Region 1. Create a VPC named skvpc2 `192.168.2.0/24` for Region 2.
2. Configure an Express Connect circuit across regions.
Configure two Express Connect circuits between the VPCs of the two regions. Configure one Express Connect circuit in Region 1 to connect skvpc1 to skvpc2. spaces i. Configure a route table for skvpc1. Add the CIDR block `192.168.2.0/24` of skvpc2 to the route table of skvpc1. a. In the left-side navigation pane, click **Route Tables**. b. On the **Route Tables** page, find the instance ID of skvpc1 and click **Management** in the Actions column. c. On the **Routing entry list** tab, click **Add route entry**. In the dialog box that appears, configure the parameters. Click **Create VPC-to-VPC Connection** to configure an Express Connect circuit between skvpc1 and skvpc2.

> **Note:** Specify the CIDR block of skvpc2 for **Destination CIDR Block**.
> Select **Router Interface (VPC Direction)** from the **Next hop type** drop- down list.
> The first time you configure an Express Connect circuit across regions, no VPCs are available.

spaces ii. Create a VPC-to-VPC connection a. Click Create VPC interconnection to go to the **Create Peering Connection** page. On the page that appears, specify the source VPC ID, destination VPC ID, and bandwidth based on your business requirements. Click **Submit**. b. After the VPC-to-VPC connection is created, click **Back to Console** to go to the VPC-to- VPC page. If the initiator and acceptor are in the Activated state, the connection from skvpc1 to skvpc2 is established. Establish the other connection from skvpc2 to skvpc1 in Region 2. iii. View the VPC-to-VPC connection. Go to the **Add Route Entry** page. The VPC-to-VPC connection that you created appears in the VPC list. Configure the other Express Connect circuit in Region 2 to connect skvpc2 to skvpc2. spaces Perform the preceding procedure. In the Add Route Entry panel, select the VPC-to-VPC connection from the VPC list and click **OK**. The route entry is added to skvpc2 in Region 2. You can select the VPC-to-VPC connection that you created from the VPC list. `vpc-ew2xxxx` is the ID of skvpc1.
3. Add a rule to a permission group.
i. In the top navigation bar, choose **Products > Storage > Apsara File Storage NAS**. ii. In the left-side navigation pane, choose **Permission Group**. On the Permission Group page, find the permission group to which you want to add a rule, or create a permission group. Then, click **Add Rule**. iii. Click **Add Rule**. In the dialog box that appears, specify an authorized address and read and write permissions. In the following figure, the IP segment of skvpc1 is added.
4. Creates a mount target.
In Region 2, you can create a mount target that resides in skvpc2 for the specified unified namespace. In Region 1, you can create a mount target that resides in skvpc1 for the specified unified namespace.
5. Create an Elastic Compute Service (ECS) instance.
For example, if you select skvpc2 when you create an ECS instance, you can mount file systems on the ECS instance without the need to establish a VPC connection. The following figure shows an example. spaces

> **Note:** In most cases, each ECS instance uses an independent VPC. You do not need to establish connections between VPCs that are used by mount targets of namespaces in two different regions. However, you must establish connections between the VPC that is used by mount targets of the namespace and the VPC that is used by the ECS instance.

nt

## 9 Lifecycle management

File Storage NAS (NAS) provides the lifecycle management feature. By configuring a lifecycle policy, you can dump cold data to Object Storage Service (OSS). In the NAS console, you can create, view, and modify lifecycle policies. You can also query the usage of General-purpose NAS storage and IA storage.

**Prerequisites**

A Capacity Network File System (NFS) file system is mounted to an Elastic Compute Service (ECS) instance. For more information, see Mount an NFS file system.

**Background information**

The lifecycle management feature of NAS allows you to separate hot data and cold data. You can configure lifecycle policies so that files that are not accessed for a long period of time are automatically dumped to OSS. Data stored in OSS can be accessed by using the original method.

**Limits**

The lifecycle management feature supports only NFS file systems. Server Message Block (SMB) file systems and file systems whose data is encrypted are not supported.

**Usage notes**

In Apsara Stack, the lifecycle management feature allows you to dump cold data from a NAS file system to a specified OSS bucket. However, you must be the owner of the specified NAS file system and OSS bucket. You cannot delete the OSS bucket before you retrieve the cold data to the NAS file system. Otherwise, data loss may occur, and the associated NAS cluster may become unavailable. You cannot revoke permissions that you granted to NAS by using Resource Access Management (RAM). We recommend that you minimize the permissions on the OSS bucket to prevent data leaks. You cannot configure lifecycle policies for the OSS bucket to prevent cold data from being deleted. We recommend that you use an independent OSS bucket for the lifecycle management feature of NAS. This prevents cold data from being accidentally deleted if you store the cold data with other business data in the same OSS bucket. Even if the lifecycle policy is deleted, you cannot delete the OSS bucket or the objects stored in the bucket. Otherwise, data loss may occur and the NAS cluster may become unavailable. However, you can delete the OSS bucket if the OSS bucket does not have data dumped from the NAS file system.

**Preparations**

1. Authorize NAS by using RAM.
To use the lifecycle management feature, you must grant access permissions on OSS to NAS. This way, NAS can read data from and write data to the specified OSS bucket. nt

> **Important:** If you want to create a RAM role, you must specify an organization to which the OSS bucket belongs. In this example, an organization named nas-test is specified.
> You need to grant permissions to NAS only once for an organization.

i. Log in to the Apsara Uni-manager Management Console. ii. In the top navigation bar, click **Configurations**. iii. On the **Service-linked Roles** page, click **Create Service-linked Role** to create a RAM role and grant access permissions on OSS to the role. iv. View the authorization status of nas-test in the role list to verify that AliyunNASTieringRole is in the list.
2. Create an OSS bucket.
You can use an existing OSS bucket or create an OSS bucket. If you have multiple NAS file systems, you can configure an OSS bucket for each file system.

> **Note:** If you use an existing OSS bucket, the following requirements must be met:
> The OSS bucket is in the first cluster of the region. The domain name of the first cluster starts with oss-, and the domain names of the other clusters start with oss xxxx-.
> The OSS bucket and the file system belong to the same organization.

nt In the top navigation bar, choose **Products > Object Storage Service**. In the left-side navigation pane, click **Buckets**. On the Buckets page, click **Create Bucket**. In the Create Bucket panel, configure the parameters. In this example, an OSS bucket named nastiering is created. The OSS bucket is used to store cold data.

> **Note:** Before you create an OSS bucket, the following requirements must be met:
> **Storage Class** is set to **Standard**, and the first cluster in the region is selected for the OSS cluster. The domain name of the first cluster starts with oss-, and the domain names of the other clusters start with ossxxxx-.
> The OSS bucket and the file system belong to the same organization.

**Get started**

1. Create a lifecycle policy.
i. In the top navigation bar, choose **Products > Apsara File Storage NAS**. ii. In the left-side navigation pane, click **Lifecycle Management**. nt iii. On the **Lifecycle Management** page, click **Create Policy** and configure the parameters. After you create a lifecycle policy for a directory in the file system, NAS dumps the cold data that meets the rule of the policy to the OSS bucket. When you create a lifecycle policy, you must configure the following parameters: Policy Name: the name of the policy. The name must be unique within different policies. File System: the file system for which the lifecycle policy is configured. Directory Path: the directory path on the file system. The path must start with a forward slash (/). You can enter a forward slash (/) to indicate the root directory. If you select **Recursive Subdirectory**, all subdirectories in the directory are traversed. Management Rule: You can select a pre-configured rule to dump files that are not accessed for more than 14, 30, 60, or 90 days. OSS Bucket: the OSS bucket to which cold data is dumped.

> **Note:** Cold data in a file system can be dumped to only one OSS bucket.
> Only the OSS buckets of the organization to which the file system belongs are displayed in the OSS Bucket list.

nt
2. View the lifecycle policy.
On the **Lifecycle Management** page, you can view the lifecycle policy that you have created. You can also filter lifecycle policies by file system ID.
3. Modify the lifecycle policy.
On the **Lifecycle Management** page, you can modify the lifecycle policy. You can configure the following parameters: Recursive Subdirectory Management Rule
4. Query the usage of the General-purpose NAS storage and IA storage.
nt In the left-side navigation pane, click **File Systems**. You can query the usage of Generalpurpose NAS storage and IA storage within the file system for which you have configured the lifecycle policy. hat grant the read and write acce ss

## 10 Directory-level ACLs that grant the read and write access

**grant the read and write**

**access**

### 10.1 Overview

File Storage NAS supports NFSv4 access control lists (ACLs) and Portable Operating System Interface for UNIX (POSIX) ACLs. This topic introduces POSIX ACLs and NFSv4 ACLs and describes the usage notes for these ACLs. Access control and user management are important for enterprise users who need to share files among different users and groups by using a shared file system. To control access to different files and directories, you can grant users and groups different types of access. NAS provides Network File System (NFS) ACLs to allow you to meet specific requirements. An ACL consists of one or more access control entries (ACEs) that each grant a user or group one or more permissions to access a file or directory. The NFSv3 protocol implements access control by using the file mode creation mask (umask). The POSIX ACL feature is an extension to this permission model. You can grant permissions to specific users and groups in addition to the owner, group, and other classes. In a file system, a directory or file can inherit the permissions from its parent directory. For more information, see acl(5) - Linux man page. The NFSv4 ACL feature is an extension to the NFSv4 protocol. Compared with POSIX ACLs, NFSv4 ACLs provide finer-grained access control. For more information, see nfs4_acl(5) - Linux man page. You can use the NFSv3 protocol to mount a file system to which NFSv4 ACLs are applied. After the file system is mounted, the NFSv4 ACLs are converted into POSIX ACLs. You can also use the NFSv4 protocol to mount a file system to which POSIX ACLs are applied. After the file system is mounted, the POSIX ACLs are converted into NFSv4 ACLs. However, NFSv4 ACLs and POSIX ACLs are not fully compatible. The interaction between ACLs and the umask is not in an ideal state. NFSv3 file systems do not support locks. Therefore, if you use NFS ACLs, we recommend that you use the NFSv4 protocol to mount file systems and configure only NFS ACLs for the file systems. We also recommend that you do not use the umask or POSIX ACLs along with NFSv4 ACLs. For more information, see Features.

**Usage notes for POSIX ACLs**

We recommend that you use the default method that allows a subdirectory or file to inherit the ACL from the parent directory. Then, you do not need to configure another ACL when you create a file or subdirectory in the parent directory. A file system scans all ACEs each time it performs a permission check. To ensure optimal performance, we recommend that you retain a minimum number of ACEs. If redundant ACLs exist, the performance of the file system degrades. Proceed with caution when you configure ACLs by using the recursive method ( `setfacl -` `R` ). A large amount of metadata is generated when you apply an ACL recursively to a directory that contains a large number of files and subdirectories. This may negatively affect your business. hat grant the read and write acce ss Before you configure ACLs, we recommend that you manage groups and the corresponding permissions. For example, you can add a user to one or more groups. To add, remove, or change permissions for a user, you can move the user to a group that has the required permissions. You need to modify the ACL of the group only if the group structure changes. We recommend that you configure ACLs for groups rather than individual users. This is a simple and time-saving method to implement access control. You can apply a POSIX ACL to a user or group that accesses the file system from multiple clients. NAS identifies the user or group based on the user ID (UID) or group ID (GID). Therefore, you must set the same UID or GID for the user or group on the clients. All users have the permissions that are granted to the other class. Therefore, we recommend that you grant the least permissions to the other class. If the other class has more permissions than an ACE, a security vulnerability may exist. We recommended that you grant the least permissions to the other class. Before you create files or directories, run the `umask 777` command to configure the umask. This command sets the umask to 000 when a file or directory is being created. This ensures that the new file or directory has the least permissions. For more information about umask and the default mode, see Why doesn't umask change execute permissions on files? After you enable the POSIX ACL feature, the other class is moved to the everyone@ user category and the umask is also set. When NAS performs a permission check, NAS treats the other class as everyone.

**Usage notes for NFSv4 ACLs**

We recommend that you use UIDs or GIDs such as UID 1001 to configure ACLs. We recommend that you do not configure the umask along with NFSv4 ACLs. The `nfs4_setfacl` command provides multiple options such as the -a, -x, and -m options to add, remove, and modify ACEs. We recommend that you run the `nfs4_setfacl -e` `<file>` command to edit an ACL in an editor. NAS NFSv4 ACLs support Allow ACEs rather than Deny ACEs. All users have the permissions that are granted to everyone. Therefore, we recommend that you grant the least permissions to everyone. If everyone has more permissions than an ACE, a security vulnerability may exist. NFSv4 ACLs support fine-grained permissions. In most cases, permission control based on fine-grained write permissions is unnecessary. For example, if a user has the write-data (w) access to a file but does not have the append-data (a) access, an error may occur when the user writes data to the file. The same issue occurs for a directory. To prevent unexpected permission errors, we recommend that you specify a capital W when you run the `nfs4_setfacl` command to configure an ACL. The `nfs4_setfacl` command specifies full write access. For a file, W is expanded to wadT. For a directory, W is expanded to wadTD. We recommend that you use the default method that allows a subdirectory or a file to inherit the ACL from the parent directory. Then, you do not need to configure another ACL when you create a file or subdirectory in the parent directory. A file system scans all ACEs each time it performs a permission check. To ensure optimal performance, we recommend that you retain a minimum number of ACEs. If redundant ACLs exist, the performance of the file system degrades. Proceed with caution when you configure ACLs by using the recursive method ( `nfs4_setfacl -R` ). A large amount of metadata is generated when you apply an ACL recursively to a directory that contains a large number of files and subdirectories. This may negatively affect your business. hat grant the read and write acce ss Before you configure ACLs, we recommend that you manage groups and the corresponding permissions. For example, you can add a user to one or more groups. To add, remove, or change permissions for a user, you can move the user to a group that has the required permissions. You need to modify the ACL of the group only if the group structure changes. We recommend that you configure ACLs for groups rather than individual users. This is a simple and time-saving method to implement access control.

### 10.2 Features

This topic describes the features of NFSv4 access control lists (ACLs) and POSIX ACLs.

**Features of File Storage NAS NFSv4 ACLs**

Only access control entries (ACEs) of the allow type are supported. ACEs of the following types are not supported: deny, audit, and alarm. Deny ACEs increase the complexity of access control. In most cases, complexity leads to confusion and increases potential security risks. As agreed by the industry, we recommend that you do not use deny ACEs. For more information about why deny ACEs are not recommended, see FAQ. Audit and alarm ACEs are not available for NFS file systems. However, you can audit file systems and configure alerts based on auditing results in the NAS console. If no ACL is set for a file or a directory, the default ACL that corresponds to the predefined umask is applied. Example: i. Run the `touch file` command to enter the file. ii. Run the `ls -l file` command to view the permissions on the file.

```
-rw-r--r--. 1 root root 0 May 6 14:27 file
```

iii. Run the `nfs4_getfacl file` command to view the current ACL permissions on the file.

```bash
# file: file
A::OWNER@:rwatTnNcCy A::GROUP@:rtncy A::EVERYONE@:rtncy
```

An ACL is an ordered list that contains and deduplicates ACEs. This scheme ensures that the permissions defined in an ACL are clear and informative. If you apply both a new ACE and an existing ACE to the same object and the existing ACE is inherited from the parent object, the permissions of the new ACE override the permissions of the existing ACE. Example: Run the `nfs4_getfacl file` command to view the ACL permissions on the file. ACEs that include the principals OWNER, GROUP, and EVERYONE are queued in this sequence at the beginning of an ACL. These ACEs take precedence over other ACEs.

```bash
# file: file
A::OWNER@:rwaxtTnNcCy A::GROUP@:rtncy A::EVERYONE@:rtncy A::1001:rwaxtTNcCy
```

hat grant the read and write acce ss Add an ACE of the read and write permissions to the following ACL for a user principal named 1009. The ACE is placed after the ACE that is defined for a user principal named 1001 based on the predefined order. Run the following commands:

```
nfs4_setfacl -a A::1009:X file nfs4_getfacl file
```

Sample command output:

```bash
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:tcy A::1001:rwaxtTNcCy A::1009:waxtTncCy
```

Add a new ACE that includes the execute permissions to the ACL for the user principal named 1009. The system automatically merges the execute permissions to the existing ACE for the 1009 user principal. Run the following commands:

```
nfs4_setfacl -a A::1009:W file nfs4_getfacl file
```

Sample command output:

```bash
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:tcy A::1001:rwaxtTNcCy A::1009:waxtTncCy
```

Add the f and d inheritance flags to an ACE that includes a user principal named 1009. Then, the system splits the ACE into two ACEs. One ACE has an extra inheritance flag named i, which indicates an inherit-only ACE. The other ACE applies to only the file object that does not have inheritance flags. If the inheritance type of an existing ACE matches the type of one of the two ACEs, the system combines the existing ACE with this ACE into one ACE. Run the following commands:

```
nfs4_setfacl -a A:fd:1009:R file nfs4_getfacl file
```

Sample command output:

```bash
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:tcy A::1001:rwaxtTNcCy A::1009:rwaxtTNcCy A:fdi:1009:r
```

hat grant the read and write acce ss All ACEs can be inherited. i. For example, the OWNER principal has the write permissions, the GROUP principal has the read permissions, and the EVERYONE has no permissions on the dir directory. Run the following commands:

```
nfs4_getfacl dir
```

Sample command output:

```bash
# file: dir
A::OWNER@:rwaDxtTnNcCy A::GROUP@:rxtcy A::EVERYONE@:tncy
```

ii. Add an ACE that grants a user principal named 1000 the read, write, and execute permissions on the dir directory. The f and d inheritance flags are also specified for the ACE. Run the following commands:

```
nfs4_setfacl -a A:fd:1000:rwx dir nfs4_getfacl dir
```

Sample command output:

```bash
# file: dir
A::OWNER@:rwaDxtTcCy A::GROUP@:rxtcy A::EVERYONE@:tcy A::1000:rwx A:fdi:1000:rwx
```

iii. When you create a file or subdirectory in the dir directory, the file or the subdirectory automatically inherits all ACEs from the dir directory. Create a file in the dir directory Run the following commands:

```
touch dir/file nfs4_getfacl dir/file
```

Sample command output:

```bash
# file: dir/file
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy A::1000:rwx
```

hat grant the read and write acce ss Create a subdirectory in the dir directory Run the following commands:

```
mkdir dir/subdir nfs4_getfacl dir/subdir
```

Sample command output:

```bash
# file: dir/subdir
A::OWNER@:rwaDxtTcCy A::GROUP@:rwaDxtcy A::EVERYONE@:rwaDxtcy A:fdi:1000:rwx
```

> **Note:** We recommend that you grant the least permissions to the EVERYONE principal. Before you run one of the preceding commands, we recommend that you run the

`umask 777` command. This command ensures that no access to a file or directory is granted when the file or directory is created. For more information about umask and the default mode, see Why doesn't umask change execute permissions on files?

> When Linux calls functions to create files or directories, the predefined umask is used as a request parameter. You can obtain the final ACL for a child object from the overlap of the inherited ACL (parent to child) and the umask, as specified in the RFC 7530 standard. When you modify the group bits of a umask based on the standard, the permissions included in an ACL for each group must be less than or equal to the permissions defined in the group bits. However, this results in an invalid inheritance for groups. For example, if you want the subfile to inherit Group A:RWX but the predefined umask GROUPS:R is used as a request parameter, the ACE included in the ACL of Group A is then changed to Group A: R. In actual business scenarios, we recommend that you modify umasks only for ACLs that include the following principals: OWNER, GROUP, and EVERYONE. This prevents potential issues and ensures that the semantics are clear. To remove permissions from a group, we recommend that you remove the ACE that is associated with the group.

You must manage the mappings between usernames or group names and user IDs (UIDs) or group IDs (GIDs) across multiple independent instances. File Storage NAS NFS uses IP security groups instead of usernames to authenticate users. When you configure NFSv4 ACLs, UIDs or GIDs that are included in ACEs are stored in Linux. When you print an ACL for an object in a shell, Linux automatically loads the /etc/passwd file and converts UIDs or GIDs into usernames or group names. You must manage the mappings between usernames or group names and UIDs or GIDs across multiple instances. You must make sure that each username is mapped to its corresponding UID, and each group name is mapped to its corresponding GID. You can print NFSv4 ACL by using extended attributes. Run the following commands:

```
getfattr -n system.nfs4_acl file
```

hat grant the read and write acce ss Sample command output:

```bash
# file: file
system.nfs4_acl=0sAAAABgAAAAAAAAAAABYBhwAAAAZPV05FUkAAAAAAAAAAAAAAABIAhwAAAAZHUk9VUEA AAAAAAAAAAAABIAhwAAAAlFVkVSWU9ORUAAAAAAAAAAAAAAAAAAAAEAAAAEMTAwMAAAAAAAAAALAAAAAwAAAA MDAwAAAAAAAAAEAAFgGQAAAABTEwMDAxAAAA
```

You can use tools such as cp to migrate NFSv4 ACLs. NAS allows you to migrate NFSv4 ACLs by using the cp, tar, and rsync tools. For more information, see How to preserve NFS v4 ACLs via extended attributes when copying file.

| cp --preserve=xattr file1 file2 |   |   |
|---|---|---|
| file2. The | cp -ar dir1 dir2 | com |

copies file1 to file2.

> **Note:** NFSv4 ACLs may fail to be migrated if the version of the rsync tool is earlier than 3.1.2.

Example 1: Migrate the ACL of a file. a. Run the `nfs4_getfacl file1` command to view the ACL permissions of the file1 file.

```bash
# file: file1
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy A::1000:rtncy
```

b. Run the `cp --preserve=xattr file1 file2` command to copy the ACL of the file1 file to the ACL of the file2 file. Example 2: Migrate the ACL of a directory. a. Run the `nfs4_getfacl file2` command to view the ACL permissions of the file2 file. b. Run the `cp -ar dir1 dir2` command to copy the ACL of the dir1 directory to the dir2 directory.

```bash
# file: file2
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy A::1000:rtncy
```

NFSv4 ACLs can interact with umasks. If you modify the ACL of an object, the umask of the object is changed. If you modify the umask of an object, the ACL of the object is also changed. For example, the umask of the file object is 0666. The following example shows the file permissions and ACL permissions: Run the `ls -l file` command to view the permissions on the file.

```
-rw-rw-rw-. 1 root root 0 May 3 2019 file
```

hat grant the read and write acce ss Run the `nfs4_getfacl file` command to view the ACL permissions of the file.

```bash
# file: file
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy
```

If you add the execute permissions to the umask by modifying the owner bits, the execute permissions are also added to the ACE that includes the OWNER principal. Example: a. Run the `chmod u+x file` command to grant the execute permissions to the OWNER principal. b. Run the `ls -l file` command to view the permissions on the file.

```
-rwxrw-rw-. 1 root root 0 May 3 2019 file
```

c. Run the `nfs4_getfacl file` command to verify that the execute permissions are granted to the OWNER principal.

```bash
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy
```

If you add the execute permissions to an ACE that includes the GROUP principal, the execute permissions are also added to the umask. Run the `nfs4_setfacl -a A::GROUP@:x file` command to grant the execute permissions to the GROUP principal. Run the `ls -l file` command to view the permissions on the file.

```
-rwxrwxrw-. 1 root root 0 May 3 2019 file
```

> **Note:** In the interactions between ACLs and umasks, the EVERYONE principal is equivalent to the other class. When you modify the other class, the change also applies to the EVERYONE principal. This operation has a slight impact on the semantics of permissions. For example, the current umask is 177. After you run the `chmod o+r` command, all users that include the file owner and group members have the read permissions. This is because the read permissions are added to the ACE that includes the EVERYONE principal. If no change is applied to the default umask, the owner and group classes still do not have the read permissions after you run the chmod o+r command.
> If no change is applied to NFSv4 ACLs, the semantics of the other class of the file mode remain unchanged. If you modify an NFSv4 ACL, the semantics of the other class change to the semantics of the EVERYONE principal and the latest semantics remain unchanged. We recommend that you do not use umasks together with NFSv4 ACLs.

Interactions between NFSv4 ACLs and POSIX ACLs are supported. You can mount NFSv3 file systems that have NFSv4 ACLs. These NFSv4 ACLs are then converted to POSIX ACLs. You can also mount NFSv4 file systems that have POSIX ACLs. These POSIX ACLs are then converted to NFSv4 ACLs. hat grant the read and write acce ss

> **Note:** The semantics of POSIX ACLs are different from the semantics of NFSv4 ACLs. For example, the inheritance rules that apply to POSIX ACLs do not differentiate files or directories. NFSv4 ACLs have more permissions than POSIX ACLs. POSIX ACLs have only read, write, and execute permissions. To prevent potential issues, we recommend that you use either NFSv4 ACLs or POSIX ACLs.

If you configure an NFSv4 ACL for the dir0 directory, the following permissions are required. Run the following commands:

```python
sudo nfs4_getfacl dir0
```

Sample command output:

```
A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:fdi:EVERYONE@:tncy A:fdi:OWNER@:tTnNcCy A:fdi:GROUP@:tncy A:g:19064:rxtncy A:g:19065:rwaDxtTnNcCy A:fdig:19064:rxtncy A:fdig:19065:rwaDxtTnNcCy
```

If you configure a POSIX ACL for the dir0 directory, the following permissions are required. Run the following commands:

```python
sudo getfacl dir0
```

Sample command output:

```
user::--group::--group:players:r-x group:adminis:rwx mask::rwx other::--default:user::--default:group::--default:group:players:r-x default:group:adminis:rwx default:mask::rwx default:other::---
```

If you configure an NFSv4 ACL for the dir0/file file, the following permissions are required. Run the following commands:

```python
sudo nfs4_getfacl dir0/file
```

hat grant the read and write acce ss Sample command output:

```
A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:g:19064:rxtncy A:g:19065:rwaxtTnNcCy
```

If you configure a POSIX ACL for the dir0/file file, the following permissions are required. Run the following commands:

```python
sudo getfacl dir0/file
```

Sample command output:

```
user::--group::--group:players:r-x group:adminis:rwx mask::rwx other::---
```

The number of NFSv4 ACLs is limited. By default, NAS supports a maximum of 100,000 different ACLs in each file system. Each ACL can contain a maximum of 500 ACEs.

> **Note:** We recommend that you do not exceed the limits of ACLs or ACEs. Otherwise, more time and resources are consumed to verify permissions.

**Features of NAS POSIX ACLs**

Permissions that are specified for users of the other class apply to everyone. Everyone includes the owner, groups, and users that are related to each ACE. The other class is equal to the EVERYONE principal of an NFSv4 ACL.

> **Note:** We recommend that you grant the least permissions to users of the other class.

For example, the following ACL is configured for the myfile file. Although the ACE contains a user named alice who does not have the write permissions, the write permissions propagate to the ACE because the permissions are specified for users of the other class.

```bash
# file: myfile
# owner: root
# group: root
user::rwuser:alice:r-group::r-mask::r-other::rw-
```

hat grant the read and write acce ss Permissions that are configured by ACLs are not changed after you run the `chmod` command.

> **Note:** We recommend that you do not modify the umask of a file to which a POSIX ACL is applied. You can configure permissions for the file by modifying the POSIX ACL.

i. For example, an ACE that grants the players group the read and write permissions on the myfile file.

```bash
# file: myfile
# owner: root
# group: root
user::rwuser:player:rwgroup::rwgroup:players:rwmask::rwother::---
```

ii. The `chmod g-w myfile` or `chmod u-w myfile` command does not change the permissions that are granted to the player user or the players group. This is different from the POSIX ACL standard. However, this ensures that the permissions granted by POSIX ACLs to non-reserved users are the same after you modify permissions by using the umask. Non-reserved users include all users except for the users of the owner, group, and other classes.

```bash
# file: myfile
# owner: root
# group: root
user::r-user:player:rwgroup::r-group:players:rwmask::rwother::---
```

If the execute permissions are not granted to the group or other class of an ACL, the ACL does not have the execute permissions. The rule is predefined in Linux. The execute action is allowed by the backend of NAS. However, to ensure that the execute permissions in the ACL are effective, you must grant the execute permissions to the group or other class. For example, if the group and other classes do not have the execute permissions on the myfile file, the player user cannot execute the file. Example:

```bash
# file: myfile
# owner: root
# group: root
user::rwuser:player:r-x group::r-mask::r-x other::r--
```

hat grant the read and write acce ss If you grant the execute permissions to the group class, the execute permissions also propagate to the player user. Example:

```bash
# file: myfile
# owner: root
# group: root
user::rwuser:player:r-x group::r-x mask::r-x other::r--
```

If you configure inheritable NFSv4 ACLs for directories that reside in NFSv3 file systems, these settings may not conform to the POSIX ACL standard. Inheritance rules that apply to files are different from inheritance rules that apply to directories in NFSv4 ACLs. The same inheritance rules apply to both files and directories in POSIX ACLs.

> **Note:** To prevent potential issues, we recommend that you apply either NFS4 ACLs or POSIX ACLs to an NFS file system.

The umask value cannot be modified. The umask of a POSIX ACL is generated by the permissions or operations of all users and groups. The umask has no practical meaning and cannot be changed. You must manage the mappings between usernames or group names and UIDs or GIDs across multiple instances. File Storage NAS NFS uses IP security groups instead of usernames to authenticate users. When you configure POSIX ACLs, UIDs or GIDs that are included in ACEs are stored in Linux. When you print an ACL for an object in a shell, Linux automatically loads the /etc/passwd file and converts UIDs or GIDs to actual usernames or group names. You must manage the mappings between usernames or group names and UIDs or GIDs across multiple instances. You must make sure that each username is mapped to its corresponding UID, and each group name is mapped to its corresponding GID. You can print POSIX ACL by using extended attributes. Run the following commands:

```
getfattr -n system.posix_acl_access file
```

Sample command output:

```bash
# file: file
system.posix_acl_access=0sAgAAAAEAAAD/////AgAFACAEAAAEAAAA/////xAABQD/////IAABAP////8
```

You can use tools such as cp to migrate POSIX ACLs. NAS allows you to migrate POSIX ACLs by using the cp, tar, and rsync tools. For more information, see How to preserve NFS v4 ACLs via extended attributes when copying file.

| cp --preserve=xattr file1 file2 |   |   |
|---|---|---|
| file2. The | cp -ar dir1 dir2 | com |

copies file1 to file2. hat grant the read and write acce ss

> **Note:** POSIX ACLs may fail to be migrated if the version of the rsync tool is earlier than 3.1.2.

Example 1: Migrate the ACL permissions of the file. a. Run the `getfacl file1` command to view the ACL permissions of the file1 file.

```
user::--user:player:r-x group::--mask::r-x other::--x
```

b. Run the `cp --preserve=xattr file1 file2` command to copy the ACL of the file1 file to the ACL of the file2 file. Example 2: Migrate the ACL of a directory. a. Run the `getfacl file2` command to view the ACL permissions of the file2 file.

```bash
# file: file2
user::--user:player:r-x group::--mask::r-x other::--x
```

b. Run the `cp -ar dir1 dir2` command to copy the ACL of the dir1 directory to the dir2 directory. The number of POSIX ACLs is limited. By default, NAS supports a maximum of 100,000 different ACLs in each file system. Each ACL can contain a maximum of 500 ACEs.

> **Note:** We recommend that you do not exceed the limits of ACLs or ACEs. Otherwise, more time and resources are consumed to verify permissions.

**FAQ**

Why are deny ACEs not supported? The position of an ACE that resides in an ACL is important. The sequence for ACEs that reside in an NFSv4 ACL is random. A deny ACE may be placed in any position of an NFSv4 ACL. For example, an ACL contains two ACEs: A::Alice:r and D::Alice:r. The position of the ACEs determines whether the user named Alice has the write permissions.

> **Note:** When you configure an ACL, you must consider the position of each ACE.

The number of ACEs in an ACL has a sharp increase. hat grant the read and write acce ss The ACEs in an ACL may be difficult to combine and deduplicate because it is not mandatory to sequence ACEs. The number of ACEs may increase up to tens or hundreds over a long period of time. To manage the final permissions that are produced by these ACEs, you need to check each ACE. The check process is strenuous and time-consuming. The interactions between the umask and ACLs become more complex after deny ACEs are applied. This is because deny features do not exist in the umask. If deny ACEs are available, you may need to add several ACEs to an ACL when the umask is changed. For example, if you change the umask to -rw-rw-rw, you need to add the following ACEs to the ACL. You must add the ACEs in sequence at the beginning of the ACL.

```
A::OWNER@:rw D::OWNER@:x A::GROUP@:rw D::GROUP@:x A::EVERYONE@:rw D::EVERYONE@:x
```

If deny ACEs are unavailable, you can sort and deduplicate ACEs while the ACEs for the everyone class and the other class are not differentiated. If you change the umask, you can modify ACLs by changing ACEs for the owner, group, and everyone classes into the following content:

```
A::OWNER@:rw A::GROUP@:rw A::EVERYONE@:rw
```

Conversions between NFSv4 ACLs and POSIX ACLs are not supported. POSIX ACLs do not support deny ACEs. If deny ACEs are included in an NFSv4 ACL, you cannot convert the ACL to a POSIX ACL.

### 10.3 Use POSIX ACLs to control access

**access**

This topic describes how to configure Portable Operating System Interface (POSIX) access control lists (ACLs) to control access to the files and directories in an NFSv3 file system.

**Prerequisites**

An NFSv3 file system is mounted. For more information, see Mount an NFS file system.

**Description**

Before you configure POSIX ACLs, we recommend that you get familiar with specific commands. The following table describes the commands.

| Command | Description |
|---|---|
| getfacl <filename> | Queries the ACL that applies to the specified file. |
| setfacl -m g::w <filename> | Adds an access control entry (ACE) that grants the write permissions on a specified file to the GROUP@ principal. |
| setfacl -m u:player:w <filename> | Grants the player user the write permissions. |

hat grant the read and write acce ss

| setfacl -m g:players:rwx <filename> | Grants the players group the read, write, and execute permissions. |
|---|---|
| setfacl -x g:players <filename> | Revokes permissions from the players group |
| getfacl file1 \| setfacl --set-file=- file2 | Copies the ACL for the file1 file to the file2 file. |
| setfacl -b file1 | Removes all extended ACEs from the file1 file. The base ACEs of the owner, group, and others are retained. |
| setfacl -k file1 | Removes all default ACEs from the file1 file. |
| nfs4 setfacl -R -m g:players:rw dir _ | Grants the players group the read and write permissions on the files and subdirectories in the dir directory. |
| setfacl -d -m g:players:rw dir1 | Grants the players group the read and write permissions on the new files and subdirectories in the dir1 directory. |

**Procedure**

To control access to files and directories by configuring NFS ACLs, perform the following steps:
1. Create users and groups.
In this example, the following users are created: player, admini, and anonym. The following groups are created: players and adminis. The player user is added to the players group and the admini user is added to the adminis group.

```python
sudo useradd player sudo groupadd players sudo usermod -g players player sudo useradd admini sudo groupadd adminis sudo usermod -g adminis admini sudo useradd anonym
```

2. Configure POSIX ACLs to control access to files and directories.
Run the following commands to complete the operations: Create a directory named dir0 and grant the players group the read-only permissions, the adminis group the read, write, and execute permissions, and the others class no permissions on the files in the dir0 directory.

```python
sudo umask 777 sudo mkdir dir0 sudo setfacl -m g:players:r-x dir0 sudo setfacl -m g:adminis:rwx dir0 sudo setfacl -m u::--- dir0 sudo setfacl -m g::--x dir0 sudo setfacl -m o::--- dir0 sudo setfacl -d -m g:players:r-x dir0 sudo setfacl -d -m g:adminis:rwx dir0 sudo setfacl -d -m u::--- dir0 sudo setfacl -d -m g::--x dir0 sudo setfacl -d -m o::--- dir0
```

hat grant the read and write acce ss Run the `sudo getfacl dir0` command to verify the configuration.

```bash
# file: dir0
# owner: root
# group: root
user::--group::--x group:players:r-x group:adminis:rwx mask::rwx other::--default:user::--default:group::--x default:group:players:r-x default:group:adminis:rwx default:mask::rwx default:other::---
```

3. Verify the configuration of the ACL.
i. Run the following commands to verify that the admini user has the read and write permissions.

```python
sudo su admini -c 'touch dir0/file' sudo su admini -c 'echo 123 > dir0/file'
```

ii. Run the following command to verify that the player user has the read-only permissions. Run the `sudo su player -c 'touch dir0/file'` command to create a file named file in the dir0 directory. If the output is similar to the following information, the player user does not have the permissions to create the file file.

```
touch: cannot touch ‘dir0/file’: Permission denied
```

Run the `sudo su player -c 'cat dir0/file'` command to view the content of the dir0/file file. Run the `sudo su player -c 'echo 456 >> dir0/file'` command to append data to the dir0/file file.

```
bash: dir0/file: Permission denied
```

Run the `sudo su player -c 'getfacl dir0/file'` command to view the permissions that the player user has on the dir0/file file.

```bash
# file: dir0/file
# owner: admini
# group: adminis
user::--group::--group:players:r-x group:adminis:rwx mask::rwx other::---
```

hat grant the read and write acce ss iii. Run the following commands to verify that the anonym user does not have permissions on specific resources: Run the `sudo su anonym -c 'ls dir0'` command to view the files in the dir0 directory. If the output is similar to the following information, the anonym user does not have permissions on the dir0 directory.

```
ls: cannot open directory dir0: Permission denied
```

Run the `sudo su anonym -c 'cat dir0/file'` command to view the content of the file. If the output is similar to the following information, the anonym user does not have the permissions to view the content of the file.

```
cat: dir0/file: Permission denied
```

Run the `sudo su anonym -c 'getfacl dir0/file'` command to query the permissions that the anonym user has on the file. If the output is similar to the following information, the anonym user does not have permissions on the file.

```
getfacl: dir0/file: Permission denied
```

**What to do next**

You can use the following method to revoke permissions from a user. If you want to use NFSv4 ACLs, we recommend that you add each user to groups. This allows you to configure permissions for a group rather than a separate user. To revoke permissions on an object from a user, you can remove the user from the group that is granted permissions on the object. For example, run the following commands to remove the admini user from the adminis group and add the user to the adminis2 group:

| sudo groupadd adminis2 | comman |
|---|---|
| sudo usermod -g adminis2 admini |   |

adminis group and add the user to the adminis2 group.
3. Run the `id admini` command to query the ID information about the admini user.

```
uid=1057(admini) gid=1057(admini) groups=1061(adminis2)
```

4. Run the following commands to check the permissions that the admini user has:
Run the `sudo su admini -c 'ls dir0'` command. If the output is similar to the following information, the admini user does not have permissions on the dir0 directory.

```
ls: cannot open directory dir0: Permission denied
```

Run the `sudo su admini -c 'cat dir0/file'` command. If the output is similar to the following information, the admini user does not have the permissions to view the content of the dir0/file file.

```
cat: dir0/file: Permission denied
```

Run the `sudo su admini -c 'getfacl dir0/file'` command. If the output is similar to the following information, the admini user does not have permissions on the dir0/file file.

```
getfacl: dir0/file: Permission denied
```

hat grant the read and write acce ss

### 10.4 Use NFSv4 ACLs to control access

**access**

This topic describes how to configure NFSv4 access control lists (ACLs) and use the ACLs to control access to the files or directories in an NFSv4 file system.

**Prerequisites**

An NFSv4 file system is mounted. For more information, see Mount an NFS file system.

**Background information**

You can mount an NFSv4 file system on a Linux Elastic Compute Service (ECS) instance and install the Linux-specific nfs4-acl-tools tool on the instance. After the tool is installed, you can use the standard nfs4_getfacl and nfs4_setfacl tools to configure NFSv4 ACLs.

**Description**

Before you configure NFSv4 ACLs, we recommend that you get familiar with specific commands. The following table describes the commands.

| Command | Description |
|---|---|
| nfs4 getfacl <filename> _ | Views the ACL that applies to a specified file |
| nfs4 setfacl -a A::GROUP@:W <filename> _ | Adds an access control entry (ACE) that grants the write permissions on a specified file to the GROUP@ principal. |
| nfs4 setfacl -a A::1000:W <filename> _ | Adds an ACE that grants the write permissions on a specified file to a user principal named 1000. |
| nfs4 setfacl -a A:g:10001:W <filename> _ | Adds an ACE that grants the write permissions on a specified file to a user principal named 10001. |
| nfs4 setfacl -e <filename> _ | Modifies an ACL in interactive mode. |
| nfs4 getfacl <filename> > _ saved acl.txt _ | Saves a list of permissions on a specified file as a TXT file. |
| nfs4 setfacl -S saved acl.txt _ _ <filename> | Configures permissions on a specified file by using a TXT file that includes a list of permissions. |
| nfs4 setfacl -m A::1001:rwaxTNcCy _ A::1001:rxtcy file1 | Modifies an ACE that applies to the file1 file. |
| nfs4 getfacl file1 \| nfs4 setfacl -S - _ _ file2 | Copies the ACL for the file1 file to the file2 file. |
| nfs4 getfacl file1 \| grep @ \| _ nfs4 setfacl -S - file1 _ | Removes all ACEs that apply to the file1 file except for ACEs that include the following principals: OWNER@, GROUP@, and EVERYONE@. |

|   | nfs4 getfacl <filename> > _ |
|---|---|
| saved acl.txt _ |   |

|   | nfs4 setfacl -S saved acl.txt _ _ |
|---|---|
| <filename> |   |

|   | nfs4 setfacl -m A::1001:rwaxTNcCy _ | Modifies an A |
|---|---|---|
| A::1001:rxtcy file1 |   |   |

|   | nfs4 getfacl file1 \| nfs4 setfacl -S - _ _ | Co |
|---|---|---|
| file2 |   |   |

|   | nfs4 getfacl file1 \| grep @ \| _ | except for AC |
|---|---|---|
| nfs4 setfacl -S - file1 _ |   |   |

hat grant the read and write acce ss

| nfs4 setfacl -R -a A:g:10001:rW dir _ |   | Adds an ACE that grants the read and write permissions on the files and subdirectories in the dir directory to a group principal named 10001. |
|---|---|---|
| find dir -type f -exec sh -c 'for ace in |   |   |
|   | find dir -type f -exec sh -c 'for ace in |   |
| $(nfs4 getfacl \{} \| grep _ |   |   |
|   |   | Removes ACEs that grant permissions on th in the dir directory to a user principal name |
|   |   | in the dir dir |
| "^A.*\:1005\:"); do nfs4 setfacl -x $ace _ |   | 1005. |
| \{}; done' \; |   |   |

| nfs4 setfacl -a A:fdg:10001:rW dir1 _ | Adds an ACE that grants the read and write permissions on new files and subdirectories in the dir1 directory to a group principal named 10001. |
|---|---|
| nfs4 setfacl -a A:fg:10001:rx dir1 _ | Adds an ACE that grants the read, write, and execute permissions on all new files in the dir1 directory to a group principal named 10001. |

**Procedure**

To control access to files and directories by configuring NFSv4 ACLs, perform the following steps.
1. Create users and groups.
In this example, the following users are created: player, admini, and anonym. The following groups are created: players and adminis. The player user is added to the players group and the admini user is added to the adminis group.

```python
sudo useradd player sudo groupadd players sudo usermod -g players player sudo useradd admini sudo groupadd adminis sudo usermod -g adminis admini sudo useradd anonym
```

2. Install the required tools to configure NFSv4 ACLs.
If you have installed these tools, skip this step.

```python
sudo yum -y install nfs4-acl-tools
```

3. Obtain the IDs of the players and adminis groups.
Open the /etc/group file. The IDs of the players and adminis groups are displayed.

```
players:x:19064:player adminis:x:19065:admini
```

4. Configure NFSv4 ACLs to control access to files and directories.
Run the following commands to complete the operations: Create a directory named dir0 and add ACEs that grant the read-only permissions on all files in the dir0 directory to the players group, grant the read, write, and execute permissions to the adminis group, and do not grant permissions to other users. hat grant the read and write acce ss

```python
sudo umask 777 sudo mkdir dir0 sudo nfs4_setfacl -a A:fdg:19064:RX dir0 sudo nfs4_setfacl -a A:fdg:19065:RWX dir0 sudo nfs4_setfacl -a A:fdg:OWNER@: dir0 sudo nfs4_setfacl -a A:fdg:GROUP@: dir0 sudo nfs4_setfacl -a A:fdg:EVERYONE@: dir0
```

Run the `sudo nfs4_getfacl dir0` command to verify the configuration.

```
A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:fdi:EVERYONE@:tncy A:fdi:OWNER@:tTnNcCy A:fdi:GROUP@:tncy A:g:19064:rxtncy A:g:19065:rwaDxtTnNcCy A:fdig:19064:rxtncy A:fdig:19065:rwaDxtTnNcCy
```

5. Verify the configuration of the ACL.
i. Run the following commands to verify that the admini user has the read and write permissions.

```python
sudo su admini -c 'touch dir0/file' sudo su admini -c 'echo 123 > dir0/file'
```

ii. Run the following command to verify that the player user has the read-only permissions. Run the `sudo su player -c 'touch dir0/file'` command. If the output is similar to the following information, the player user does not have the permissions to create the dir0/file file.

```
touch: cannot touch ‘dir0/file’: Permission denied
```

Run the `sudo su player -c 'echo 456 >> dir0/file'` command. If the output is similar to the following information, the player user does not have the write permissions on the dir0/file file.

```
bash: dir0/file: Permission denied
```

Run the `sudo su player -c 'cat dir0/file'` command. If the output is similar to the following information, the player user does not have the permissions to view the content of the dir0/file file. Run the `sudo su player -c 'nfs4_getfacl dir0/file'` command to view the permissions that the player user has on the dir0/file file.

```
A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:g:19064:rxtncy A:g:19065:rwaxtTnNcCy
```

hat grant the read and write acce ss iii. Run the following command to verify that the anonym user does not have permissions on specific resources: Run the `sudo su anonym -c 'ls dir0'` command. If the output is similar to the following information, the anonym user does not have permissions on the dir0 directory.

```
ls: cannot open directory dir0: Permission denied
```

Run the `sudo su anonym -c 'cat dir0/file'` command. If the output is similar to the following information, the anonym user does not have the permissions to view the content of the dir0/file file.

```
cat: dir0/file: Permission denied
```

Run the `sudo su anonym -c 'nfs4_getfacl dir0/file'` command. If the output is similar to the following information, the anonym user does not have permissions on the dir0/file file.

```
Invalid filename: dir0/file
```

**What to do next**

You can use the following method to revoke permissions from a user. If you want to use NFSv4 ACLs, we recommend that you add each user to groups. This allows you to configure permissions for a group rather than a separate user. To revoke permissions on an object from a user, you can remove the user from the group that is granted permissions on the object. For example, you can run the following commands to remove the admini user from the adminis group and add the user to the adminis2 group:

| sudo groupadd adminis2 | comman |
|---|---|
| sudo usermod -g adminis2 admini |   |

adminis group and add the user to the adminis2 group.
3. Run the `id admini` command to view the ID information about the admini user.

```
uid=1057(admini) gid=1057(admini) groups=1054(adminis2)
```

4. Run the following commands to check the permissions that the admini user has:
Run the `sudo su admini -c 'ls dir0'` command. If the output that is similar to the following information appears, the admini user does not have permissions on the dir0 directory.

```
ls: cannot open directory dir0: Permission denied
```

Run the `sudo su admini -c 'cat dir0/file'` command. If the output that is similar to the following information appears, the admini user does not have the permissions to view the content of the dir0/file file.

```
cat: dir0/file: Permission denied
```

Run the `sudo su admini -c 'nfs4_getfacl dir0/file'` command. If the output that is similar to the following information appears, the admini user does not have permissions on the dir0/file file.

```
Invalid filename: dir0/file
```
