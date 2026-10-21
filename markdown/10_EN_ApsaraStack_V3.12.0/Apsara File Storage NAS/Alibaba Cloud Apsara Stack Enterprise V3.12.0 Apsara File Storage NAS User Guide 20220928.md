---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara File Storage NAS User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 58
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara File Storage NAS User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E5%AD%98%E5%82%A8/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Apsara%20File%20Storage%20NAS%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Apsara File Storage NAS User Guide 20220928

## Table of Contents

- 1 What is Apsara File Storage NAS?
- 2 Precautions
- 3 Quick start
  - 3.1 Log on to the Apsara File Storage NAS console
  - 3.2 Create a file system
  - 3.3 Create a permission group and add rules
  - 3.4 Add a mount target
  - 3.5 Mount an NFS file system
  - 3.6 Mount an SMB file system
- 4 File systems
  - 4.1 View the details of a file system
  - 4.2 Delete a file system
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
- 8 Create and manage a unified namespace
- 9 Manage the file lifecycle
- 10 Directory-level ACLs that grant the read and write access
  - 10.1 Overview
  - 10.2 Features
  - 10.3 Use POSIX ACLs to control access
  - 10.4 Use NFSv4 ACLs to control access

ge NAS?

## 1 What is Apsara File Storage NAS?

NAS? NAS is a cloud service that provides file storage for compute nodes. These compute nodes include Elastic Compute Service (ECS) instances and Alibaba Cloud Container Service for Kubernetes (ACK) nodes. NAS supports multiple standard file access protocols. NAS is a distributed file system that offers a variety of benefits. These benefits include unlimited capacity, scalable performance, shared access, high reliability, and high availability. You can work with NAS without the need to modify existing applications. Compared with traditional user-created data stores, NAS helps you reduce a large number of maintenance costs and mitigate data security risks. You can mount an NAS file system on multiple compute nodes at the same time. This helps you reduce a large number of costs in data transmission and synchronization. You can perform the following operations on an NAS file system: Create NAS file systems and mount points. Create permission groups for NAS file systems and add rules to permission groups. This allows access to file systems from specific IP addresses or CIDR blocks. This also allows you to grant different levels of access permissions to IP addresses or CIDR blocks. Mount file systems on compute nodes. These compute nodes include ECS instances and ACK nodes. NAS allows you to access file systems by using the standard Network File System (NFS) and Server Message Block (SMB) protocols. You can also use POSIX-based APIs to access file systems. Manage file systems, mount points, and permission groups in the NAS console. Call NAS API operations to manage file systems.

## 2 Precautions

Before you use NAS, you must familiarize yourself with the following limits. Limits on file systems Maximum number of files in a single file system: 1 billion. Maximum name length: 255 bytes. Maximum size of a single file: 32 TB. Maximum directory depth: 1,000 levels deep. Maximum capacity of a single file system: 10 PB for NAS Capacity and 1 PB for NAS Performance. Maximum number of compute nodes on which you can mount a single file system: 10,000.

> **Note:** The file system allows simultaneous access from the 10,000 compute nodes. Maximum size of a protocol packet: 4 MB. Maximum number of Change Notify requests: 512. Limits on NFS clients Limits on the usage of NFS clients are listed as follows. You can open a maximum of 32,768 files at a time on an NFS client. Files in the list folder and its subfolders are not counted as part of the total number of open files. Each unique mount on an NFS client can acquire a maximum of 8,192 locks across a maximum of 256 unique file or process pairs. For example, a single process can acquire one or more locks on 256 separate files, or 8 processes can each acquire one or more locks on 32 files. We recommend that you do not use an NFS client in a Windows environment to access an NFS file system. Limits on SMB clients Each file or folder can be opened a maximum of 8,192 times in parallel across compute nodes that each have a file system mounted and users that share access to each of these file systems. This represents a maximum of 8,192 active file handlers for each file system. A maximum of 65,536 active file handlers can exist on a file system. Limits on the NFS protocol NAS supports the NFSv3 and NFSv4 protocols. NFSv4.0 does not support the following attributes: FATTR4_MIMETYPE, FATTR4_QUOTA_AVAIL_HARD, FATTR4_QUOTA_AVAIL_SOFT, FATTR4_QUOTA_USED, FATTR4_TIME_BACKUP, and FATTR4_TIME_CREATE. If one of the preceding attributes is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on a client that has the file system mounted. NFSv4.1 does not support the following attributes: FATTR4_DIR_NOTIF_DELAY, FATTR4_DIR_NOTIF_DELAY, FATTR4_DACL, FATTR4_SACL, FATTR4_CHANGE_POLICY, FATTR4_FS_STATUS, FATTR4_LAYOUT_HINT, FATTR4_LAYOUT_TYPES, FATTR4_LAYOUT_ALIGNMENT, FATTR4_FS_LOCATIONS_INFO, FATTR4_MDSTHRESHOLD, FATTR4_RETENTION_GET, FATTR4_RETENTION_SET, FATTR4_RETENTEVT_GET, FATTR4_RETENTEVT_SET, FATTR4_RETENTION_HOLD, FATTR4_MODE_SET_MASKED, FATTR4_FS_CHARSET_CAP. If one of the preceding attributes is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on a client that has the file system mounted. NFSv4 does not support the following operations: OP_DELEGPURGE, OP_DELEGRETURN, and NFS4_OP_OPENATTR. If one of the preceding operations is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on a client that has the file system mounted. NFSv4 does not support delegations. The following issues are related to user IDs (UIDs) and group IDs (GIDs): On Linux, mappings between UIDs or GIDs and usernames or group names are defined in configurations files. For NFSv3 file systems, if the mapping between an ID and a name is defined in a configuration file, the name is displayed. If no mapping can be found for a UID or GID, the UID or GID is displayed. For NFSv4 file systems, the usernames and group names are displayed as nobody for all files if the version of a Linux kernel is earlier than 3.0. If the kernel version is later than 3.0, the rule used by NFSv3 file systems applies to display files. Not ice If a file or directory is stored on an NFSv4 file system and the Linux kernel version is earlier than 3.0, we recommend that you do not use the chown or chgrp command. If you use either one of the commands, the UID and GID of the file or directory will change to nobody. Limits on the SMB protocol NAS supports protocols including SMB 2.1 or later and operating systems including Windows 7, and Windows Server 2008 R2 or later. However, NAS does not support Windows Vista, or Windows Server 2008 or earlier. Compared with SMB 2.1 or later, SMB 1.0 has lower performance and functionality. Furthermore, Windows products that support SMB 1.0 are no longer offered or supported. Extended file attributes and client-side caching based on leases. Input/output control (IOCTL) or file system control (FSCTL) operations, such as creating sparse files, compressing files, retrieving NIC status, and creating reparse points. Alternate data streams. Identity authentication provided by Active Directory (AD) or Lightweight Directory Access Protocol (LDAP). Several features provided by SMB 3.0 or later, such as SMB Direct, SMB Multichannel, SMB Directory Leasing, and persistent handles. Access control lists (ACLs) on files or directories.


## 3 Quick start

### 3.1 Log on to the Apsara File Storage NAS console

NAS console This topic describes how to log on to the Apsara File Storage NAS console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, select Product s and click Apsara File St orage NAS.

### 3.2 Create a file system

This topic describes how to create a file system in the Apsara File Storage NAS console. Context Before you create a file system, you must note the following limitations: You can use an Alibaba Cloud account to create a maximum of 1,000 file systems. The maximum capacity of a NAS Performance file system is 1 PB. The maximum capacity of a NAS Capacity file system is 10 PB. If you want to increase the maximum storage capacity, we recommend that you contact Alibaba Cloud Technical Support. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List and click Creat e File Syst em.
3. In the Creat e File Syst em dialog box, set the required parameters.
The following table lists the required parameters.

| Parameter | Description |
|---|---|
| Region | Select a region where you need to create a file system. |
| Organization | Select an organization from the drop-down list for the instance. |
| Resource Set | Select a resource set from the drop-down list for the instance. |

| Parameter | Description |
|---|---|
| File System Name | The name of the file system. The name must be 2 o 256 characters in length and can contain letters, digits, and special characters. These special characters include underscores ( ) and hyphens (-). The name must start with a letter and cannot start with _ http:// or https://. |
| Storage Type | The storage type. Select Perf ormance or Capacit y based on your business requirements. The maximum capacity of an NAS Performance file system is 1 PB. The maximum capacity of an NAS Capacity file system is 10 PB. |
| Protocol Type | The protocol type. Select NFS or SMB based on your business requirements. We recommend that you mount Network File System (NFS) file systems on Linux clients and Server Message Block (SMB) file systems on Windows clients. |
| Capacity (TB) | The capacity of the file system. The capacity of an NAS Performance file system ranges from 0.5 TB to 1024 TB. The capacity of an NAS Capacity file system ranges from 0.5 TB to 10240 TB. |

4. Click OK to complete the creation.

### 3.3 Create a permission group and add rules

add rules This topic describes how to create a permission group and add rules to the permission group in the Apsara File Storage NAS console. Context In NAS, each permission group represents a whitelist. You can add rules to a permission group to allow access to a file system from specific IP addresses or CIDR blocks. You can also grant different access permissions to different IP addresses or CIDR blocks. You can use an Alibaba Cloud account to create a maximum of 100 permission groups. If you want to increase the limit, we recommend that you contact Alibaba Cloud Technical Support. Creates a permission group
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > Permission Group and click Creat e Permission Group.
3. In the Creat e Permission Group dialog box, specify the required parameters.
The following table lists the required parameters.

| Parameter | Description |
|---|---|
| Organization | The organization to which the permission group belongs. |
| Resource Set | The resource set to which the permission group belongs. |
| Region | The region where you want to create the permission group. |
| Name | The name of the permission group. The name must be 3 to 64 characters in length and can contain letters, digits, and hypens (-). |
| Network Type | The network type. Select Classic Net work or VPC based on your business requirements. |

4. Click OK to complete the creation of the permission group.
Create a rule
1. Log on to the Apsara File Storage NAS console.
2. On the Permission Group page, find the target permission group and click Manage.
3. Click Add Rule.
4. In the Add Rule dialog box that appears, specify the required parameters.
The following table lists the required parameters.

| Parameter | Description |
|---|---|
| Authorization Address | Specifies the authorized object to which the rule applies. You can specify an IP address or CIDR block. Only IP addresses are available for permission groups of the classic network type. |
| Read/Write Permission | Specifies whether to allow read-only or read/write access to the file system from the authorized object. Valid values: Read-only and Read/Writ e. |
| User Permission | Specifies whether to limit a Linux user's access to a file system. Do not limit root users (no squash): allows access to a file system _ from root users. Limit root users (root squash): denies access to a file system from _ root users. All root users are treated as nobody users. Limit all users (all squash): denies access to a file system from all _ users including root users. All users are treated as nobody users. The nobody user is created by default on Linux. The user has only the most basic permissions and can access only the open content of servers. This feature offers high security. |
| Priority | When multiple rules are applied to an authorized object, the rule with the highest priority takes effect. Valid values: 1 to 100, in which 1 is the highest priority. |

5. Click OK to complete the creation of the rule.

### 3.4 Add a mount target

This topic describes how to add a mount target. After an Apsara File Storage NAS file system is created, you must add a mount target to the file system. Then, you can use the mount target to mount the file system on compute nodes. These compute nodes include Elastic Compute Service (ECS) instances and Alibaba Cloud Container Service for Kubernetes (ACK) nodes. Prerequisites A file system is created. For more information, see Create a file system. A permission group and a rule are created. For more information, see Create a permission group and add rules. Context A mount target is an endpoint that resides in a VPC or classic network. Each mount target corresponds to a file system. Mount targets of the VPC and classic network types are available for NAS file systems. You use a mount target to mount a file system on multiple compute nodes for shared access. These compute nodes include ECS instances and ACK nodes. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system and click Manage.
4. On the Mount T arget tab, click Add Mount T arget .
5. In the Add Mount T arget dialog box that appears, specify the required parameters.
Mount T arget T ype: includes VPC and Classic Net work. Mount targets of the classic network type allow access only from ECS instances that belong to the same Alibaba Cloud account as the mount targets. If you want to create a mount target of the VPC type, specify the following parameters.

| Parameter | Description |
|---|---|
| VPC | The VPC. Not e The VPC you specify must be the same as the VPC where the compute nodes reside. These compute nodes include ECS instances and ACK nodes. |
| VSwitch | The VSwitch. |
| Permission Group | The permission group. |

If you want to create a mount target of the classic network type, specify the following parameters.

| Parameter | Description |
|---|---|
| Permission Group | The permission group. |

6. Click OK to complete the configuration.

### 3.5 Mount an NFS file system

This topic describes how to mount a Network File System (NFS) file system. Before you mount a file system, you must create the file system and a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes. These compute nodes include Elastic Compute Service (ECS) instances and Alibaba Cloud Container Service for Kubernetes (ACK) nodes. Prerequisites A file system is created. For more information, see Create a file system. A permission group and a rule are created. For more information, see Create a permission group and add rules. A mount target is created. This topic takes a mount target of the VPC type as an example. For more information, see Add a mount target. If you create a mount target of the VPC type for a file system, you can mount the file system only on ECS instances that reside in the same VPC as the mount target. You can specify a permission group for the mount target. Then, you can add several rules to the permission group. The authorization address of a rule must match the IP range of the VPC that hosts the ECS instances. If you create a mount target of the classic network type for a file system, you can mount the file system only on ECS instances that belong to the same Alibaba Cloud account as the mount target. You can specify a permission group for the mount target. Then, you can add several rules to the permission group. The authorization address of a rule must match the IP range of the private network that hosts the ECS instances. A compute node is created. This topic takes a Linux ECS instance as an example. Step 1: Install an NFS client Before you mount an NFS file system on a Linux ECS instance, you must install an NFS client. If an NFS client is instaned, skip this step.
1. Log on to the Linux ECS instance. For more information, see the Quick st art > Connect t o an ECS
inst ance topic of the ECS User Guide .
2. Install the NFS client.
If CentOS, RHEL, or Aliyun Linux runs on the ECS instance, use the following command to install the NFS client.

```python
sudo yum install nfs-utils
```

If Ubuntu or Debian runs on the ECS instance, use the following commands to install the NFS client.

```python
sudo apt-get update sudo apt-get install nfs-common
```

Step 2: Mount an NFS file system
1. Log on to the Linux ECS instance. For more information, see the Quick st art > Connect t o an ECS
inst ance topic of the ECS User Guide .
2. Mount the NFS file system.
Use the following command to mount the NFS file system. In the command, replace file-systemid.region.nas.aliyuncs.com:/ /mnt with a value that is specific to your environment. To mount an NFSv4 file system, use the following command.

```python
sudo mount -t nfs -o vers=4.0,minorversion=0,rsize=1048576,wsize=1048576,hard,timeo=6 00,retrans=2,noresvport file-system-id.region.nas.aliyuncs.com:/ /mnt
```

To mount an NFSv3 file system, use the following command.

```python
sudo mount -t nfs -o vers=3,nolock,proto=tcp,rsize=1048576,wsize=1048576,hard,timeo=6 00,retrans=2,noresvport file-system-id.region.nas.aliyuncs.com:/ /mnt
```

Mount parameters

| Parameter | Description |
|---|---|
| file-system- id.region.nas.aliyuncs. com:/ /mnt | Specifies the mount target of the NAS file system, the forward slash (/) following the mount target specifies the root directory of the NAS file system, and /mnt specifies a local directory that resides on the Linux ECS instance. You must replace the example values based on your business requirements. The mount target, for example, file-system-id.region.nas.aliyuncs.com. To obtain information about a mount target, follow these steps. Log on to the NAS console, find the target system, click Manage next to the file system to go to the Details page. The Details page shows information about the mount target. The directory of the NAS file system: specifies the root directory (/) or a subdirectory (/sub1). If a subdirectory is specified, make sure that the subdirectory exists. The local directory on which you want to mount a file system: specifies the root directory (/) or a subdirectory (/mnt) of a system such as Linux. If a subdirectory is specified, make sure that the subdirectory exists. |
| vers | The version of the file system. Only NFSv3 and NFSv4 are available. |
| Mount option | When you mount a file system, multiple mount options are available. Separate multiple mount options with commas (,). For more information, see the following . Not e When you specify mount options, take note of the following items. To avoid a decrease in performance, we recommend that you specify the maximum value (1048576) for both the rsize mount option and the wsize mount option. If you need to modify the timeo mount option, we recommend that you specify a minimum of 150 for the mount option. The timeo mount option is measured in deciseconds (tenths of a second). For example, a value of 150 indicates 15 seconds. To avoid data inconsistency, we recommend that you do not use the soft mount option. Use caution with the soft mount option. We recommend that you use the default values for other mount options. For example, a decrease in performance may occur due to changes in some mount options. These mount options include the size of the read or write buffer or the use of attribute caching. |

Mount options

| Option | Description |
|---|---|
| rsize | Specifies the maximum number of bytes in each read request that the NFS client can receive. Recommended value: 1048576. |
| wsize | Specifies the maximum number of bytes in each write request that the NFS client can send. Recommended value: 1048576. |
| hard | Specifies that applications must stop accessing a file system when the file system is unavailable, and wait until the file system is available. We recommended that you use the hard mount option. |
| timeo | Specifies the time in deciseconds (tenths of a seconds) that the NFS client waits before it retries an NFS request. Recommended value: 600. |
| retrans | Specifies the number of times the NFS client retries a request. Recommended value: 2. |
| noresvport | Specifies that the NFS client uses a different TCP source port for a new network connection to ensure data integrity. We recommend that you use the noresvport mount option. |

3. Use the `mount -l` command to view the mount result.
The following figure shows an example of a successful mount. After a file system is mounted, you can use the `df -h` command to view the size of the file system.
4. After you mount an NAS file system on an ECS instance, you can access the file system from the
ECS instance. You can access the file system in the same way you access a local directory. The following figure shows an example.

### 3.6 Mount an SMB file system

This topic describes how to mount a Server Message Block (SMB) file system. Before you mount a file system, you must create the file system and a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes such as Elastic Compute Service (ECS) instances. Prerequisites
1. A file system is created. For more information, see Create a file system.
2. A permission group and a rule are created. For more information, see Create a permission group and
add rules.
3. A mount target is created. This topic takes a mount target of the Classic Network type as an
example. For more information, see Add a mount target. If you create a mount target of the VPC type for a file system, you can mount the file system only on ECS instances that reside in the same VPC as the mount target. You can specify a permission group for the mount target. Then, you can add several rules to the permission group. The authorization address of a rule must match the IP range of the VPC that hosts the ECS instances. If you create a mount target of the Classic Network type for a file system, you can mount the file system only on ECS instances that belong to the same Alibaba Cloud account as the mount target. You can specify a permission group for the mount target. Then, you can add several rules to the permission group. The authorization address of a rule must match the IP range of the private network that hosts the ECS instances.
4. An ECS instance is created. This topic takes a Windows ECS instance as an example.
5. The following Windows services are started:
Workstation a. Choose All Programs > Accessories > Run, or press `Win+R` and enter `services.msc` to open the Services console. b. Find the Workstation service and ensure that the service is Running and the startup type is Aut omat ic. The default state for the Workstation service is Running. TCP/IP NetBIOS Helper Follow these steps to start the TCP/IP NetBIOS Helper service: a. Double-click Net work and Sharing Cent er and right-click the active network connection. b. Click Propert ies to open the Local Area Network Properties dialog box. Double-click Int ernet Prot ocol Version 4 (T CP/IPv4) to open the Internet Protocol Version 4 (TCP/IPv4) Properties dialog box, and then click Advanced. c. In the Advanced T CP/IP Set t ings dialog box, choose WINS > Enable Net BIOS over T CP/IP. d. Choose All Programs > Accessories > Run, or press `Win+R` and enter `services.msc` to open the Services console. e. Find the TCP/IP NetBIOS Helper service and make sure that the service is Running and the startup type is Aut omat ic. The default state for the TCP/IP NetBIOS Helper service is Running. Procedure
1. Log on to a Windows ECS instance. For more information, see the Quick st art > Connect t o an
ECS inst ance topic of the ECS User Guide .
2. Open the command prompt and use the following command to mount the file system.

```
net use D: \\file-system-id.region.nas.aliyuncs.com\myshare
```

The syntax of the command is net use <the letter of a local drive> \\<the domain name of a

```
mount target>\myshare .
```

The letter of a local drive: specifies a drive on which you need to mount a file system. You can specify the target drive based on your business requirements. The target drive must be different from any existing drives. The domain name of the mount target: When you create a mount target for a file system, the domain name of the mount target is automatically generated. You can replace the domain name based on your business requirements. To obtain the mount target of the file system, follow these steps. Log on to the NAS console, find the target file system, and click Manage to go to the Details page. myshare: specifies the name of an SMB share. You cannot change the name.
3. Use the `net use` command to check mount results.
The following figure shows an example of a successful mount.
4. After you mount an NAS file system on an ECS instance, you can access the file system from the
ECS instance.

## 4 File systems

### 4.1 View the details of a file system

This topic describes how to view the details of a file system. The details include the information about the file system and information about the attached mount targets. Prerequisites A file system is created. For more information, see Create a file system. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system and click Manage to go to the Details page of the file system.
The following sections are available on the Details page of the file system. Basic Inf ormat ion: includes information about the file system. The information includes the ID, region, protocol type, and storage type. Mount T arget : includes mount targets for the file system. You can manage mount targets in the section.

### 4.2 Delete a file system

This topic describes how to delete a file system in the Apsara File Storage NAS console. Prerequisites A file system is created. For more information, see Create a file system. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system, and click Manage.
Before you can delete a file system, you must remove all mount targets from the file system. Use caution when you delete a file system. After a file system is deleted, the data on the file system cannot be restored. We recommend that you ensure that all data is backed up.
4. In the Delet e File Syst em dialog box, click OK to complete the deletion.

## 5 Mount targets

### 5.1 View mount targets

This topic describes how to view mount targets in the Apsara File Storage NAS console. Context A file system is created. For more information, see Create a file system. A permission group and a rule are created. For more information, see Create a permission group and add rules. A mount target is created. For more information, see Add a mount target. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system and click Manage.
4. In the Mount T arget section, view mount targets in the file system.

### 5.2 Enable or disable a mount target

This topic describes how to enable or disable a mount target. You can control access to a mount target from clients by enabling or disabling the mount target. Prerequisites A file system is created. For more information, see Create a file system. A permission group and a rule are created. For more information, see Create a permission group and add rules. A mount target is created. For more information, see Add a mount target. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system and click Manage.
4. After you find the mount target that you want to disable or enable, you can perform the following
operations: Disable the mount target. Click Disable. In the Disable Mount Target dialog box, click OK to deny access to the mount target from clients. Enable the mount target. Click Enable. In the Enable Mount Target dialog box, click OK to allow access to the mount target from clients.

### 5.3 Delete a mount target

This topic describes how to delete a mount target in the Apsara File Storage NAS console. Prerequisites A file system is created. For more information, see Create a file system. A permission group and a rule are created. For more information, see Create a permission group and add rules. A mount target is created. For more information, see Add a mount target. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system and click Manage.
4. Find the mount target that you want to delete and click Delet e.
Use caution when you delete a mount target. After you delete a mount target, the mount target cannot be restored.
5. In the Delete Mount Target dialog box, click OK.

### 5.4 Modify the permission group of a mount target

mount target You must add a permission group to each mount target. You can modify the permission group of a mount target in the Apsara File Storage NAS console. Prerequisites A file system is created. For more information, see Create a file system. A permission group and a rule are created. For more information, see Create a permission group and add rules. A mount target is created. For more information, see Add a mount target. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the target file system, and click Manage.
4. Find the mount target that you want to modify and click Modif y Permission Group.
5. In the Modif y Permission Group dialog box, change the permission group and click OK.

## 6 Permission groups

### 6.1 View permission groups

This topic describes how to view permission groups in the Apsara File Storage console. Prerequisites A permission group is created. For more information, see Create a permission group and add rules. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > Permission Group and view permission groups in the region.

### 6.2 Delete a permission group

This topic describes how to delete a permission group in the Apsara File Storage NAS console. Prerequisites A permission group is created. For more information, see Create a permission group and add rules. Operating system
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > Permission Group.
3. Find the target permission group and click Delet e.
Permission groups in use cannot be deleted. Before you can delete a permission group, you must remove the permission group from the linked mount target.
4. In the Delete Permission Group dialog box, click OK.

### 6.3 Manage permission group rules

This topic describes how to manage permission group rules in the Apsara File Storage NAS console. The management includes viewing the details of rules, modifying rules, and deleting rules. Prerequisites A permission group and a permission group rule are created. For more information, see Create a permission group and add rules. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > Permission Group.
3. Find the target permission group and click Manage.
4. On the Rules page, you can perform the following operations:
View all rules for the permission group. Modify a rule. Find the target rule and click Edit to modify the details of the rule. The details include the aut horizat ion address, read/writ e permissions, user permission, and priorit y. Delete a rule. Find the target rule and click Delet e. In the Delete Rule dialog box, click OK.

## 7 Manage quotas

This topic describes how to use the Alibaba Cloud quota_tool tool to manage quotas on Elastic Compute Service (ECS) instances that have Apsara File Storage NAS file systems mounted. You can configure, view, and cancel quotas on these ECS instances. Prerequisites An NFS file system of the NAS Capacity or NAS Performance type is mounted on an ECS instance. For more information, see Mount an NFS file system. Context NAS allows you to view and manage directory-level quotas. Directory-level quotas specify the maximum number of files in each directory and the maximum storage space for these files. From the perspective of the application scope, quotas are sorted into quotas for all users and quotas for a single user or group. Quotas for all users specify the maximum storage space for files that all users can create in a directory. Quotas for a single user or group specify the maximum storage space for files that a user or group can create in a directory. From the perspective of the restriction level, quotas are sorted into statistical quotas and restriction quotas. Statistical quotas collect only the usage of storage space. You can query and view statistical data. Restriction quotas specify the maximum capacity of storage space for files that you can create in a directory. If the limit is exceeded, you may fail to create a file or subdirectory, append data to a file, or perform other operations. Not ice Only statistical quotas are available. NAS performs asynchronous calculation for quotas at the backend. When you use the quota_tool tool to query statistical data about quotas, the process requires a period of time to complete. In most cases, the time period is about 5 to 15 minutes. Configure quotas This topic uses the /mnt directory as an example.
1. Log on to an Elastic Compute Service (ECS) instance by using a root account.
You can use the quota_tool tool on an ECS instance that has a NAS file system mounted. You must run the tool with the root permissions. The following describes how to use the quota_tool tool on the ECS instance.
2. Use the following command to download the quota_tool tool.

```
wget https://nasimport.oss-cn-shanghai.aliyuncs.com/quota_tool_v1.0 -O quota_tool
```

3. Use the following command to grant the execute permission to the quota_tool tool.

```python
sudo chmod a+x quota_tool
```

4. Configure quotas.
For each file system, you can configure quotas only for a maximum of 10 directories. The syntax of the command that you use to configure quotas is `sudo ./quota_tool set --dir [D`

```
IR] [OPTION] .
```

| Parameter | Description |
|---|---|
| --dir [DIR] | Specifies the directory for which you want to configure quotas. For example, --dir /mnt/data/. |
| OPTION | Specifies the required options. Not e When you specify options, you must follow these rules: 1. the --accounting option is required. 2. One of the --alluser, --uid, and -- gid options is required. . --accounting: specifies a statistical quota. --alluser: specifies a directory-level quota for all users. --uid: specifies the UID of a user. For example, --uid 505 indicates the quota is configured only for the user whose UID is 505. --gid: specifies the GID of a group. For example, --gid 1000 indicates the quota is configured only for the group whose GID is 1000. |

The following examples describe how to configure quotas. Use the following command to configure a statistical quota for the /mnt/data/ directory to limit the total number of files that reside in a directory.

```python
sudo ./quota_tool set --dir /mnt/data/ --accounting --alluser
```

Use the following command to configure a statistical quota for the /mnt/data/ directory to limit the total number of files that can be created by the user whose UID is 505.

```python
sudo ./quota_tool set --dir /mnt/data/ --accounting --uid 505
```

Query quotas After you configure a quota for an NAS directory, you can query statistical data about the quota for the directory.
1. Log on to an Elastic Compute Service (ECS) instance by using a root account.
2. Use the following command to query quotas.

```python
sudo ./quota_tool get --dir /mnt/data/ --all
```

In the preceding command, the --all parameter is optional. If you specify the parameter, statistical data about all quotas that are configured for the file system returns. The first time you query a quota, a state called Initializing appears. After the Init ializing process is complete, you can query the quota and a result showing success appears. The duration of the initialization process is based on the number of files and subdirectories in a directory. After the initialization process is complete, you can query quotas daily. A delay of 5 to 10 minutes may occur before the expected FileCountReal and SizeReal appear. This occurs due to the asynchronous calculation for quotas at the backend. The following table lists parameters that are included in a response in the JSON format.

| Parameter | Description |
|---|---|
| Path | Indicates a directory for which you query a quota. |
| Report | Includes all information about a quota that is specified for a directory, for example, UID and GID. |
| ReportStatus | The state for the query of a quota. |
| FileCountLimit | Indicates the limit for the number of files. A value of Empty indicates no limit. |
| FileCountReal | Indicates the total number of files including subdirectories, files, and special files that reside in a directory. |
| QuotaType | Accounting indicates a statistical quota and Force indicates a restriction quota. |
| Uid | Indicates the UID of a user. A value of All indicates all users. |
| Gid | Indicates the GID of a group. A value of All indicates all groups. |
| SizeLimit | Indicates the maximum capacity of files that reside in a directory. A value of Empty indicates no limit. |
| SizeReal | Indicates the total capacity of files that reside in a directory. |

Cancel quotas You can cancel a quota.
1. Log on to an ECS instance.
2. Use the following command to cancel quotas.
The syntax of the command that you can use to cancel quotas is `sudo ./quota_tool cancel --di`

```
r [DIR] [OPTION] .
```

| Parameter | Description |
|---|---|
| --dir [DIR] | Specifies the directory for which you want to cancel quotas, for example, -dir /mnt/data/. |
| OPTION | Specifies the required options. Not e When you specify the OPTION parameter, one of the -- alluser, --uid, and --gid options is required. --alluser: specifies a directory-level quota for all users. --uid: specifies the UID of a user. For example, --uid 505 indicates that the quota is canceled for the user whose UID is 505. --gid: specifies the GID of a group. For example, --gid 505 indicates that the quota is canceled for the group whose GID is 505. |

The following examples describes how to cancel quotas. If you have configured a quota for the /mnt/data/ directory, use the following command to cancel the quota for the user whose UID is 100.

```python
sudo ./quota_tool cancel --dir /mnt/data/ --uid 100
```

If you have configured a quota for the /mnt/data/ directory, use the following command to cancel the quota for all users.

```python
sudo ./quota_tool cancel --dir /mnt/data/ --alluser
```

ified namespace

## 8 Create and manage a unified namespace

namespace This topic describes how to create a unified namespace and add mount targets in the Apsara File Storage NAS console. The topic also describes how to add, remove, and modify file systems in a namespace, view namespace details, and enable the cross-domain mount orchestration feature. Features A unified namespace allows you to mount multiple file systems in a NAS cluster by using a single domain name. You do not need to maintain multiple mount targets and directories. You can create mount targets for a namespace. You can use a unified namespace to manage multiple file systems in the same way as you manage a single file system. A unified namespace contains a virtual root directory in which file systems are the first-level subdirectory. You can mount the file systems by using their mount targets even if you add the file systems to a unified namespace. Limits A unified namespace has the following limits: You can add a maximum of 1,000 file systems to each unified namespace. The mapping name of a file system in a unified namespace cannot exceed 255 characters in length. It can contain only letters, digits, and the following special characters: . +-_()<>@# The mapping name of a file system in a namespace cannot exceed 255 characters. It can contain only letters, digits, and the following special characters: . +-_()<>@# The number of mount targets that are created for a namespace must be the same as that of file systems. You can create a maximum of 20 namespaces in each region. You can mount a unified namespace only by using the NFSv3 protocol. The file systems that are added to a namespace must belong to the same user and cluster as the namespace. The storage type, protocol type, and encryption type of the file systems must be the same. The mapping name of a file system must be unique in each unified namespace. File systems can be mapped only to first-level subdirectories in a unified namespace. You cannot modify the access permissions, owner, or access control list (ACL). Procedure Create a unified namespace and add mount targets. Log on to the Apsara File Storage NAS console. In the left-side navigation pane, choose Unif ied Namespace > Unif ied List of Namespaces. On the page that appears, you can create a unified namespace and add mount targets. ified namespace To identify CIDR blocks when you mount unified namespaces across regions, we recommend that you use different VPC CIDR blocks. For example, you can use `192.168.0.0/16` for Region 1 and `172.16.0.0/16` for Region 2. For more information, see Cross-domain mount orchestration. Add a file system in a unified namespace. After you create a unified namespace, you can add file systems and set the mapping name. The mapping name is the name of the virtual directory. Remove a file system from a unified namespace. You can remove an existing file system from the unified namespace. The file system is not deleted but removed from the list of file systems in the namespace. Modify the name of the file system mapping. You can also modify the name of the file system mapping in a namespace. If file systems in a namespace are in different mount modes, modification of the mapping name may cause connection failure. View the details of a unified namespace. The details of a namespace are divided into three types: Properties Mount target list You can create or delete mount targets. File system list You can add or remove file systems. Cross-domain mount orchestration In traditional solutions, you can add file systems to a namespace only when the file systems and the namespace are in the same region. To resolve the issue, NAS provides the cross-domain mount orchestration feature. To use this feature, perform the following operations: Create a unified namespace and add mount targets. Map the file systems to the local directory tree of a Network File System (NFS) client by using the feature. After the orchestration is complete, specify the root directory to generate an automatic mount script. ified namespace Not ice The added mount targets or attached directories cannot be modified after they are specified. You can remove the mount targets. However, if you add the mount targets again, you can only attach them to the original root directory. An NFS client runs the automatic mount script to mount the domain names to the local directory. This allows NFS to access file systems across regions. The local directory for each unified namespace is: <user-defined Root Directory>`/`<mapping path for a namespace>. Different regions have different VPCs. To enable the cross-domain mount orchestration feature, you must establish connections between different VPCs. In the following example, two VPCs in two regions are used to demonstrate how to establish VPC connections and how to mount file systems on an Elastic Compute Service (ECS) instance.
1. Create two VPCs.
Log on to the Apsara File Storage NAS console. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud to go to the VPC console. Create VPCs for Region 1 and Region 2. Configure the following CIDR blocks: Region 1: `192.168.1.0/24` (skvpc1) Region 2: `192.168.2.0/24` (skvpc2)
2. Configure a peering connection across regions.
Configure a peering connection between the VPCs of the two regions. Configure a peering connection in Region 1 to connect skvpc1 and skvpc2. i. Configure the route table for skvpc1. Send the CIDR block `192.168.2.0/24` to skvpc1 and add the CIDR block to the route table of skvpc1. a. In the left-side navigation pane, choose VPC > Rout e T ables. On the page that appears, find skvpc1 and click Manage. b. Click Add Rout e Ent ry and set the required parameters. Click Creat e VPC-t o-VPC Connect ion to configure a peering connection between skvpc1 and skvpc2. Dest inat ion CIDR Block must be the same as the CIDR block of skvpc2. Select Rout er Int erf ace (T o VPC) from the Next Hop T ype drop-down list. If you configure a peering connection across regions for the first time, no VPCs are available. ii. Create a VPC-to-VPC connection Click Create VPC-to-VPC Connection to go to the Creat e Peering Connect ion page. Specify the source VPC ID, destination VPC ID, and bandwidth based on your business requirements. After the VPC-to-VPC connection is created, the Express Connect page appears. If the initiator and acceptor are in the Activated state, the connection between skvpc1 and skvpc2 is established. ified namespace iii. View VPC-to-VPC connection. Return to the Add Rout e Ent ry page. Click Refresh. The VPC-to-VPC connection that you have created appears in the VPC list. Use the preceding procedure to configure a peering connection in Region 2 to connect skvpc1 and skvpc2. Select the VPC-to-VPC connection from the VPC list and click OK to add a route entry. When you add a route entry for Region 2, you can select the VPC-to-VPC connection from the VPC list. `vpc-6b` xxxx`42t` is the ID of skvpc1.
3. Add rules for NAS access groups.
In the top navigation bar, choose Product s > St orage > Apsara File St orage NAS. In the leftside navigation pane, choose File Syst em > Access Group > NasT imor, and click Management Rules. On the page that appears, click Add Rules. In the dialog box that appears, set the authorized address, read/write permissions, user permissions, and priority. For example, add the IP address segment of skvpc2.
4. Create a mount target.
In Region 2, you can create a mount target for skvpc2. The mount target is used to mount file systems on a specified namespace. In Region 1, you can create a mount target for skvpc1. The mount target is used to mount file systems on a specified namespace.
5. Create an ECS instance.
For example, if you select skvpc2 when you create an ECS instance, you can mount file systems on the ECS instance. The following figure shows how to select skvpc2 when you create an ECS instance. In most cases, each ECS instance uses an independent VPC. You do not need to establish connections between VPCs that are used by mount targets of a namespace in two regions. Instead, you must establish connections between the VPC that is used by mount targets of the namespace and of the VPC that is used by the ECS instance.

## 9 Manage the file lifecycle

This topic describes how to use the Apsara File Storage NAS console to manage the file lifecycle, configure lifecycle management policies, and store cold data as Infrequent Access (IA) data. In the NAS console, you can create, view, and modify lifecycle management policies. You can also query the usage of primary storage and IA storage. Prerequisites A Network File System (NFS) file system of the NAS Capacity or NAS Performance type is mounted on an Elastic Compute Service (ECS) instance. For more information, see Mount an NFS file system. Context NAS provides the lifecycle management feature that allows you to manage cold data. You can configure lifecycle management policies to transfer infrequently accessed data to a specified OSS bucket. This allows you to reduce the storage cost. You can still access the data that is stored in the OSS bucket. Limits The lifecycle management feature supports only NFS file systems. Server Message Block (SMB) file systems or file systems whose data is encrypted are not supported. Additional considerations The lifecycle management feature allows you to transfer cold data to a specified OSS bucket. You must be the owner of the specified file system and OSS bucket. You cannot delete the OSS bucket before you transfer cold data to the original file system. If you delete the file system, data may be lost and NAS clusters may be affected. You cannot revoke Resource Access Management (RAM) permissions on NAS. We recommend that you minimize the permissions of OSS bucket to prevent data leakage. We recommend that you use an independent OSS bucket for NAS. This reduces the risk of deleting cold data by accident if you store the cold data with other business data in the same OSS bucket. Preparations
1. Authorize NAS by using RAM.
You must grant permissions to NAS before NAS can access the specified OSS bucket to read and write data. Not ice When you create a RAM role, the organization that you specify is the department where the file system resides, for example, bms. You need to grant permissions to NAS only once for an organization. i. Log on to the Apsara Stack Cloud Management (ASCM) console. ii. Choose Conf igurat ions > RAM Aut horizat ion > RAM Roles > Creat e RAM Role to activate OSS authorization for the user. iii. View the authorization status of bms in the role list to confirm that AliyunNASTieringRole is on the list.
2. Create an OSS bucket.
You can use an existing OSS bucket or create an OSS bucket. You can set different OSS buckets for each file system. If you use an existing OSS bucket, note the following information: The bucket is in the first cluster in the region. The domain name of the first cluster starts with oss- whereas the names of the other clusters start with ossxxxx. Make sure that the bucket and the file system belong to the same department. Log on to the ASCM console. In the top navigation bar, choose Product s > Object St orage Service to go to the OSS console. In the left-side navigation pane, click the add icon. Create an OSS bucket for the RAM user. When you create an OSS bucket, note the following information: Select st andard from the st orage class drop-down list, and the fist cluster from the Cluster drop-down list. The domain name of the first cluster starts with oss- whereas the names of the other clusters start with ossxxxx. Make sure that the bucket and the file system belong to the same department. Procedure After the preparations are complete, you can use the lifecycle management feature in the NAS console. Make sure that an NFS file system of the NAS Capacity or NAS Performance type is mounted on an ECS instance. For more information, see Mount an NFS file system.
1. Create a lifecycle management policy
i. Log on to the ASCM console. In the top navigation bar, choose Product s > Apsara File St orage NAS. ii. In the left-side navigation pane, click Lif e Cycle Management . On the page that appears, click Create Policy to create a lifecycle management policy. After you create a lifecycle management policy for a specific directory of the file system, NAS transfers cold data to the specified OSS bucket. You can set the following parameters: Policy Name: Specify a unique policy name. File System: Specify a file system. Directory Path: Specify a directory path on the instance. You can enter a forward slash (/) to indicate the root directory. If you select Recursive Subdirect ory, all subdirectories in the directory are recurred. Management Rules: Specify a rule to manage files that have not been accessed more than 14, 30, 60, or 90 days. OSS Bucket: Specify the OSS bucket to which cold data is transferred. Cold data in a file system must be transferred to an OSS bucket. Only the OSS buckets of the organization where the file system resides are displayed in the list.
2. View the lifecycle management policies
Log on to the ASCM console. In the left-side navigation pane, click Lif e Cycle Management . On the page that appears, you can view the lifecycle management policies. You can also screen the policies by file system ID.
3. Modify a lifecycle management policy
Log on to the ASCM console. In the left-side navigation pane, click Lif e Cycle Management . On the page that appears, you can modify the lifecycle management policies.You can set the following parameters: Recursive Subdirectory Management Rules
4. Query the usage of primary storage and IA storage
You can query the primary storage and IA storage usage of the file systems that have lifecycle management policies configured. Log on to the ASCM console. In the left-side navigation pane, click File Syst em List .

## 10 Directory-level ACLs that grant the read and write access

grant the read and write access

### 10.1 Overview

Apsara File Storage NAS supports NFSv4 access control lists (ACLs) and Portable Operating System Interface (POSIX) ACLs. This topic describes POSIX ACLs and NFSv4 ACLs. It also lists precautions for using these ACLs. Access control and user management are important for enterprise-level users who want to share files between different users and groups by using a shared file system. To control access to different files and directories, you can grant users and groups different types of access. NAS provides Network File System (NFS) ACLs to allow you to meet specific requirements. An ACL consists of one or more access control entries (ACEs) that each grant a user or group one or more permissions to access a file or directory. The NFSv3 protocol includes the extended support for POSIX ACLs. POSIX ACLs extend the support for access control over file mode creation masks. You can grant permissions to specific users and groups besides users of the owner, group, and other classes. Permissions can also be inherited from parent objects. For more information, see acl - Linux man page. The NFSv4 protocol includes extended support for NFSv4 ACLs that provide more fine-grained access control than POSIX ACLs do. For more information, see nfs4_acl - Linux man page. You can mount an NFSv3 file system that has NFSv4 ACLs applied. These NFSv4 ACLs will then be converted into POSIX ACLs. You can also mount an NFSv4 file system that has POSIX ACLs applied. These POSIX ACLs will then be converted into NFSv4 ACLs. If you use NFS ACLs, we recommend that you mount NFSv4 file systems and control access by using NFSv4 ACLs rather than file mode creation masks or POSIX ACLs. This is because: NFSv4 ACLs and POSIX ACLs are not fully compatible. The interaction between ACLs and file mode creation masks is not in an ideal state. The file systems that are mounted by using the NFSv3 do not support locks. For more information about NFS ACL features, see Features. Precautions for using POSIX ACLs We recommend that you use the default inheritance method that allows a subdirectory or file to inherit the same ACL from the parent directory. This allows you to avoid configuring another ACL when you create a new file or subdirectory in the parent directory. We recommend that you retain a minimum number of ACEs because a file system needs to scan all ACEs each time it performs permission verification. Abuse of ACLs may diminish the performance of file systems. Use caution when you configure ACLs by using the recursive method ( `setfacl -R` ). Large amounts of metadata are produced when you perform a recursive operation on a directory that contains a large number of files and subdirectories. This may affect your businesses. Before you configure ACLs, we recommend that you manage groups and related permissions. For example, you can add a user to one or more groups. If you want to add, remove, or modify permissions for a user, we recommend that you move the user to a group that has the required permissions. You do not need to modify the ACL of a group as long as the structure of groups remains unchanged. We recommend that you configure ACLs for groups rather than single users. This provides a simple and effective time-saving method to control access and ensure the better organization of permissions. You can apply a POSIX ACL to multiple objects that resides on different clients. In such cases, you must ensure that the ACL you apply to each object is the same. Apsara File Storage NAS stores user IDs (UIDs) and group IDs (GIDs) at the backend. You must ensure that the mappings between a username or group name and a UID or GID are the same. We recommend that you grant the least permissions to the other class because all users have the permissions that are granted to the other class. A potential security vulnerability may be exposed if the other class has more permissions than any ACE. We recommended that you configure the least permissions for the other class. Before creating files or directories, you can use the `umask 777` command to configure the file mode creation mask. This command sets the file mode creation mask to 000 when the mask is used as a parameter to create a new file or directory. This ensures that the newly created file or directory has the least permissions. For more information, see umask and the default file mode creation mask. After you enable POSIX ACLs, the semantics of the other class for the POSIX ACL are equal to the semantics of the EVERYONE@ principal. The semantics of the other class for the file mode creation mask are also equal to the semantics of the EVERYONE@ principal. When a system performs permission verification, the system treats the other class the same as the EVERYONE@ principal. Precautions for using NFSv4 ACLs Use UIDs or GIDs such as UID 1001 to configure ACLs. We recommend that you do not configure the file mode creation mask after you configure an NFSv4 ACL. The `nfs4_setfacl` command provides -a, -x, -m, and other options. You can use these options to add, remove, or modify ACEs. However, we recommend that you use `nfs4_setfacl -e <file>` the command to edit an ACL in an interactive mode. We recommend that you configure the least permissions for the EVERYONE@ principal because NFSv4 ACLs only support allow rather than deny ACEs. A potential security vulnerability may be exposed if the EVERYONE@ principal has more permissions than other ACEs. NFSv4 ACLs have fine-grained permissions. In most cases, it is unnecessary to subdivide permissions at such a fine-grained level. For example, if you have the write access (w) to a file but do not have the append-only (a) access, an error may occur when you write data to the file. The same issue occurs for a directory. To avoid unexpected permission errors, we recommend that you specify a capital w (W) as a parameter when you use the `nfs4_setfacl` command to configure an ACL. The `nfs4_setfac` `l` command converts W to a full write access permission. For a file, W is expanded to wadT. For a directory, W is expanded to wadTD. We recommend that you use the default inheritance method that allows a subdirectory or file to inherit the same ACL from the parent directory. This allows you to avoid configuring another ACL when you create a new file or subdirectory in the parent directory. We recommend that you retain a minimum number of ACEs because a file system needs to scan all ACEs each time it performs permission verification. Abuse of ACLs may diminish the performance of file systems. Use caution when you configure ACLs by using the recursive method ( `nfs4_setfacl -R` ). Large amounts of metadata are generated when you perform a recursive operation on a directory that contains a large number of files and subdirectories. This may affect your businesses. Before you configure ACLs, we recommend that you manage groups and related permissions. For example, you can add a user to one or more groups. If you want to add, remove, or modify permissions for a user, we recommend that you move the user to a group that has the required permissions. You do not need to modify the ACL of a group as long as the structure of groups remains unchanged. We recommend that you configure ACLs for groups rather than single users. This provides a simple and effective time-saving method to control access and ensure the better organization of permissions.

### 10.2 Features

This topic describes the features of NFSv4 access control lists (ACLs) and POSIX ACLs. Features of Apsara File Storage NAS NFSv4 ACLs Only access control entries (ACEs) of the allow type are supported. ACEs of the following types are not supported: deny, audit, and alarm. Deny ACEs increase the complexity of access control. In most cases, complexity leads to confusion and increases potential security risks. As agreed by the industry, we recommend that you avoid using deny ACEs. For more information about why deny ACEs are not recommended, see FAQ. Audit and alarm ACEs are not available for NFS file systems. Instead, you can audit file systems and configure alerts based on auditing results in the NAS console. If no ACL is specified for a file or a directory, the default ACL that corresponds to the predefined file mode creation mask is applied.

```bash
touch file [root@vbox test]# ls -l file -rw-r--r--. 1 root root 0 May 6 14:27 file [root@vbox test]# nfs4_getfacl file
# file: file
A::OWNER@:rwatTnNcCy A::GROUP@:rtncy A::EVERYONE@:rtncy
```

An ACL is an ordered list that contains and deduplicates ACEs. This scheme ensures that permissions defined in an ACL are clear and informative. If you apply both a new ACE and an existing ACE to the same object and the existing ACE is inherited from the parent object, the permissions of the new ACE override the permissions of the existing ACE. For example: In most cases, ACEs that include the following principals are queued in sequence at the beginning of an ACL: OWNER@, GROUP@, and EVERYONE@. These ACEs take precedence over other ACEs.

```bash
[root@vbox test]# nfs4_getfacl file
# file: file
A::OWNER@:rwaxtTnNcCy A::GROUP@:rtncy A::EVERYONE@:rtncy A::1001:rwaxtTNcCy
```

Add an ACE of the read and write permissions to the following ACL for a user principal named 1009. The ACE is placed after the ACE that is defined for a user principal named 1001 based on the predefined order.

```bash
[root@vbox test]# nfs4_setfacl -a A::1009:X file [root@vbox test]# nfs4_getfacl file
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:tcy A::1001:rwaxtTNcCy A::1009:xtcy
```

Add a new ACE that includes the execute permission to the ACL for the user principal named 1009. The system automatically merges the execute permission into the existing ACE for the 1009 user principal.

```bash
[root@vbox test]# nfs4_setfacl -a A::1009:W file [root@vbox test]# nfs4_getfacl file
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:tcy A::1001:rwaxtTNcCy A::1009:waxtTncCy
```

Add the f and d inheritance flags to an ACE that includes a user principal named 1009. Then, the system splits the ACE into two ACEs. One ACE has an extra inheritance flag named i specified, which indicates an inherit-only ACE. The other ACE only applies to the file object without inheritance flags. If the inheritance type of an existing ACE matches the type for one of the two ACEs, the system combines the existing ACE with the ACE out of the two ACEs. The two matching ACEs are combined into one ACE.

```bash
[root@vbox test]# nfs4_setfacl -a A:fd:1009:R file [root@vbox test]# nfs4_getfacl file
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:tcy A::1001:rwaxtTNcCy A::1009:rwaxtTNcCy A:fdi:1009:r
```

All ACEs can be inherited. i. For example, the OWNER@ principal has the write access, the GROUP@ principal has the read access, and the EVERYONE@ has no access to the dir directory.

```bash
[root@vbox nfs]# nfs4_getfacl dir
# file: dir
A::OWNER@:rwaDxtTnNcCy A::GROUP@:rxtcy A::EVERYONE@:tncy
```

ii. Add an ACE that grants a user principal named 1000 the read, write, and execute access to the dir directory. The f and d inheritance flags are also specified for the ACE.

```bash
[root@vbox nfs]# nfs4_setfacl -a A:fd:1000:rwx dir [root@vbox nfs]# nfs4_getfacl dir
# file: dir
A::OWNER@:rwaDxtTcCy A::GROUP@:rxtcy A::EVERYONE@:tcy A::1000:rwx A:fdi:1000:rwx
```

iii. When you create a file or subdirectory in the dir directory, the file or the subdirectory automatically inherits all ACEs from the dir directory.

```bash
[root@vbox nfs]# touch dir/file [root@vbox nfs]# nfs4_getfacl dir/file
# file: dir/file
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy A::1000:rwx [root@vbox nfs]# mkdir dir/subdir [root@vbox nfs]# nfs4_getfacl dir/subdir
# file: dir/subdir
A::OWNER@:rwaDxtTcCy A::GROUP@:rwaDxtcy A::EVERYONE@:rwaDxtcy A:fdi:1000:rwx
```

We recommend that you grant the least privileges to the EVERYONE@ principal. Before you perform the following steps, we recommend that you run the `umask 777` command. This command ensures that no access to a file or directory is granted when the file or directory is created. For more information, see Why doesn't umask change execute permissions on files? When Linux calls functions to create files or directory, the predefined file mode creation mask is used as a request parameter. You can obtain the final ACL for a child object from the overlap of the inherited ACL (parent to child) and the file mode creation mask, as specified in the RFC7530 standard. When you modify the group bits of a file mode creation mask based on the standard, permissions included in an ACL for each group must be less than or equal to permissions defined in group bits. However, this scheme results in an invalid inheritance for groups. For example, you create a file and the file attempts to inherit A:RWX from a parent object. However, the predefined file mode creation mask sets the group bits to R. The final permission for the file becomes A:R. In actual practice, we recommend that you only modify file mode creation masks for ACLs that include the following principals: OWNER@, GROUP@, and EVERYONE@. This prevents against potential issues and ensures that semantics are clear. To remove permissions for a group, we recommend that you remove the ACE that relates to the group. You need to manage mappings between usernames or group names and user IDs (UIDs) or group IDs (GIDs) across multiple independent instances. NAS NFS adopts IP security groups rather than usernames to authenticate users. When you configure NFSv4 ACLs, UIDs or GIDs that are included in ACEs are stored in Linux. When you print an ACL for an object in a shell, Linux automatically loads the /etc/passwd file and converts UIDs or GIDs into usernames or group names. You need to manage mappings between usernames or group names and UIDs or GIDs across multiple instances. You must ensure a username or group name is mapped to its UID or GID. NFSv4 ACLs can be printed by using extended attributes.

```bash
[root@vbox nfs]# getfattr -n system.nfs4_acl file
# file: file
system.nfs4_acl=0sAAAABgAAAAAAAAAAABYBhwAAAAZPV05FUkAAAAAAAAAAAAAAABIAhwAAAAZHUk9VUEAAAAA AAAAAAAAAABIAhwAAAAlFVkVSWU9ORUAAAAAAAAAAAAAAAAAAAAEAAAAEMTAwMAAAAAAAAAALAAAAAwAAAAQxMDAw AAAAAAAAAEAAFgGQAAAABTEwMDAxAAAA
```

Tools such as cp are supported for migrating NFSv4 ACLs. NAS allows you to migrate NFSv4 ACLs by using the cp, tar, and rsync tools. For more information, see How to preserve NFS v4 ACLs via extended attributes when copying file. The following `cp --preserve=xattr file1 file2` command makes a copy of the file1 file as the file2 file while making a copy of the ACL of the file1 file for the file2 file. The `cp -ar dir1 dir2` command makes a copy of the dir1 directory as the dir2 directory while making a copy of the ACL of the dir1 directory for the dir2 directory. You may fail to migrate NFSv4 ACLs if the version of the rsync tool is earlier than 3.1.2.

```bash
[root@vbox nfs]# nfs4_getfacl file1
# file: file1
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy A::1000:rtncy [root@vbox nfs]# cp --preserve=xattr file1 file2 [root@vbox nfs]# nfs4_getfacl file2
# file: file2
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy A::1000:rtncy [root@vbox nfs]# cp -ar dir1 dir2
```

Interaction between NFSv4 ACLs and file mode creation masks is supported. The modification for the ACL of an object may change the file mode creation mask of the object. The modification for the file mode creation mask of an object may change the ACL of the object. For example, the file mode creation mask of the file object is 0666.

```bash
[root@vbox nfs]# ls -l file -rw-rw-rw-. 1 root root 0 May 3 2019 file [root@vbox nfs]# nfs4_getfacl file
# file: file
A::OWNER@:rwatTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy
```

If you add the execute permission to the file mode creation mask by modifying the owner bits, the execute permission is also added to the ACE that includes the OWNER@ principal.

```bash
[root@vbox nfs]# chmod u+x file [root@vbox nfs]# ls -l file -rwxrw-rw-. 1 root root 0 May 3 2019 file [root@vbox nfs]# nfs4_getfacl file
# file: file
A::OWNER@:rwaxtTcCy A::GROUP@:rwatcy A::EVERYONE@:rwatcy
```

If you add the execute permission to an ACE that includes the GROUP@ principal, the execute permission is also added to the related file mode creation mask.

```
[root@vbox nfs]# nfs4_setfacl -a A::GROUP@:x file [root@vbox nfs]# ls -l file -rwxrwxrw-. 1 root root 0 May 3 2019 file
```

| Not e In the interaction between ACLs and file mode creation masks, the EVERYONE@ principal is equal to the others class. When you modify the others class, the change also applies to the EVERYONE@ principal. This operation results in a slight impact on the semantics of permissions. For example, the current file mode creation mask is 177. After you run the ch mod o+r command, all users that include the file owner and group members have the read permission. This occurs because the read permission is added to the related ACE that includes the EVERYONE@ principal. If no change is applied to the default file mode creation mask, the owner and group classes still have no read permission after you run the chmod o+r command. If no change is applied to NFSv4 ACLs, the others class of the file mode creation mask keeps the same semantics. If an NFSv4 ACL is changed, the semantics of the others class change to the semantics of the EVERYONE@ principal and the latest semantics remain. We recommend that you do not use file mode creation masks after using NFSv4 ACLs. |   |   |
|---|---|---|
|   | ch |   |

Interaction between NFSv4 ACLs and POSIX ACLs is supported. You can mount NFSv3 file systems that have NFSv4 ACLs applied. These NFSv4 ACLs will then be converted into POSIX ACLs. You can also mount NFSv4 file systems that have POSIX ACLs applied. These POSIX ACLs will then be converted into NFSv4 ACLs. The semantics of POSIX ACLs are different from the semantics of NFSv4 ACLs. For example, the inheritance rules that apply to POSIX ACLs do not differentiate files and directories. NFSv4 ACLs have more permissions than POSIX ACLs, which have only read, write, and execute permissions. We recommend that you use either NFSv4 ACLs or POSIX ACLs to prevent against potential issues. For example, you configure an NFSv4 ACL for the dir0 directory. The permissions are listed as follows.

```
[root@vbox test] sudo nfs4_getfacl dir0 A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:fdi:EVERYONE@:tncy A:fdi:OWNER@:tTnNcCy A:fdi:GROUP@:tncy A:g:19064:rxtncy A:g:19065:rwaDxtTnNcCy A:fdig:19064:rxtncy A:fdig:19065:rwaDxtTnNcCy
```

You configure a POSIX ACL for the dir0 directory. The permissions are listed as follows.

```
[root@vbox test] sudo getfacl dir0 user::--group::--group:players:r-x group:adminis:rwx mask::rwx other::--default:user::--default:group::--default:group:players:r-x default:group:adminis:rwx default:mask::rwx default:other::---
```

For example, you configure an NFSv4 ACL for the dir0/file file. The permissions are listed as follows.

```
[root@vbox test] sudo nfs4_getfacl dir0/file A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:g:19064:rxtncy A:g:19065:rwaxtTnNcCy
```

For example, you configure a POSIX ACL for the dir0/file file. The permissions are listed as follows.

```
[root@vbox test] sudo getfacl dir0/file user::--group::--group:players:r-x group:adminis:rwx mask::rwx other::---
```

The number of NFSv4 ACLs is limited. NAS supports a maximum of 100,000 ACLs that are different from one another in each file system. Each ACL contains a maximum of 500 ACEs. We recommend that you do not abuse ACLs and ACEs. This reduces the time and resources consumed for verifying permissions. Features of NAS POSIX ACLs Permissions that are specified for the other class apply to all users. Everyone includes the owner, group, and users that are related to each ACE. The other class is equal to the EVERYONE@ principal of an NFSv4 ACL. We recommend that you grant the least permissions to the other class in all cases. For example, the following ACL is configured for the myfile file. Although the ACE contains a user named alice who does not have the write permission, the write permission propagates to the ACE because the permission is specified for the other class.

```bash
[root@vbox 3]# getfacl myfile
# file: myfile
# owner: root
# group: root
user::rwuser:alice:r-group::r-mask::r-other::rw-
```

Permissions that are configured by ACLs will not be changed after you run the `chmod` command. We recommend that you avoid modifying the file mode creation mask of a file that has a POSIX ACL applied. You can configure permissions for the file by modifying the POSIX ACL. i. For example, an ACE that grants the players group the read and write access to the myfile file.

```bash
[root@vbox 3]# getfacl myfile
# file: myfile
# owner: root
# group: root
user::rwuser:player:rwgroup::rwgroup:players:rwmask::rwother::---
```

ii. The `chmod g-w myfile` or `chmod u-w myfile` command does not change the permissions that are granted to the player user and the players group, which is different from the POSIX ACL standard. However, this ensures that permissions that are granted by POSIX ACLs to non-reserved users are the same after you modify permissions by using file mode creation masks. The nonreserved users include all users except for the users of the owner, group, and other classes.

```bash
[root@vbox 3]# getfacl myfile
# file: myfile
# owner: root
# group: root
user::r-user:player:rwgroup::r-group:players:rwmask::rwother::---
```

If the execute permission is not granted to the group and other classes of an ACL, the ACL has no execute permission. The rule is predefined in Linux. The execute action is allowed by the backend of NAS. However, to make the execute permission in the ACL effective, you must grant the execute permission to the group or other class. For example, if the group and other classes do not have the execute access to the myfile file, the player user cannot execute the file.

```bash
[root@vbox 3]# getfacl myfile
# file: myfile
# owner: root
# group: root
user::rwuser:player:r-x group::r-mask::r-x other::r--
```

If you grant the execute permission to the group class, the execute permission also propagates to the player user.

```bash
[root@vbox 3]# getfacl myfile
# file: myfile
# owner: root
# group: root
user::rwuser:player:r-x group::r-x mask::r-x other::r--
```

If you configure inheritable NFSv4 ACLs for directories, these settings may not conform to the POSIX ACL standard when these directories reside in NFSv3 file systems. Inheritance rules that apply to files are different from those that apply to directories in NFSv4 ACLs. The same inheritance rules apply to both files and directories in POSIX ACLs. We recommend that you apply either NFS4 ACLs or POSIX ACLs to an NFS file system to prevent against potential issues. File mode creation masks cannot be modified. The file mode creation mask of a POSIX ACL is yielded by the combination and interaction of permissions from all users and groups. The mask has no practical meaning and cannot be changed. You need to manage mappings between usernames or group names and user IDs (UIDs) or group IDs (GIDs) across multiple instances. Apsara File Storage NAS NFS adopts IP security groups rather than usernames to authenticate users. When you configure POSIX ACLs, UIDs or GIDs that are included in ACEs are stored in Linux. When you print an ACL for an object in a shell, Linux automatically loads the /etc/passwd file and converts UIDs or GIDs into actual usernames or group names. You need to manage mappings between usernames or group names and UIDs or GIDs across multiple instances. You must ensure a username or group name is mapped to its related UID or GID. POSIX ACLs can be printed by using extended attributes.

```bash
[root@vbox nfs]# getfattr -n system.posix_acl_access file
# file: file
system.posix_acl_access=0sAgAAAAEAAAD/////AgAFACAEAAAEAAAA/////xAABQD/////IAABAP////8=
```

POSIX ACLs can be migrated by using tools such as cp. NAS allows you to migrate POSIX ACLs by using the cp, tar, and rsync tools. For more information, see How to preserve NFS v4 ACLs via extended attributes when copying file. The following `cp --preserve=xattr file1 file2` command makes a copy of the file1 file as the file2 file while making a copy of the ACL of the file1 file for the file2 file. The `cp -ar dir1 dir2` command makes a copy of the dir1 directory as the dir2 directory while making a copy of the ACL of the dir1 directory for the dir2 directory. You may fail to migrate POSIX ACLs if the version of the rsync tool is earlier than 3.1.2.

```bash
[root@vbox nfs]# getfacl file1 user::--user:player:r-x group::--mask::r-x other::--x [root@vbox nfs]# cp --preserve=xattr file1 file2 [root@vbox nfs]# getfacl file2
# file: file2
user::--user:player:r-x group::--mask::r-x other::--x [root@vbox nfs]# cp -ar dir1 dir2
```

The number of POSIX ACLs is limited. NAS supports a maximum of 100,000 ACLs that are different from one another in each file system. Each ACL contains a maximum of 500 ACEs. We recommend that you do not abuse ACLs and ACEs. This reduces the time and resources consumed for verifying permissions. FAQ Why are deny ACEs not supported? The position of an ACE that resides in an ACL is important. The sequence for ACEs that reside in an NFSv4 ACL is random. A deny ACE may be placed in any position of an NFSv4 ACL. For example, an ACL contains two ACEs: A::Alice:r and D::Alice:r. The position of the ACEs determines whether the user named Alice has the write permission. When you configure an ACL, you must consider the position of each ACE. The number of ACEs in an ACL experiences a sharp increase. You may have difficulties to combine and deduplicate ACEs in an ACL because the sequencing for ACEs is not mandatory. The number of ACEs may increase up to tens or hundreds over a long period of time. To manage the final permissions that are produced by these ACEs, you need to check each ACE. The process to check is strenuous and time-consuming. The interactions between file mode creation masks and ACLs become more complex after deny ACEs are applied because deny features do not exist in file mode creation masks. If deny ACEs are available, you may need to add several ACEs to an ACL when the file mode creation mask is changed. For example, if you change the file mode creation mask to -rw-rw-rw, you need to add the following ACEs to an ACL. You must add the ACEs in sequence at the beginning of the ACL.

```
A::OWNER@:rw D::OWNER@:x A::GROUP@:rw D::GROUP@:x A::EVERYONE@:rw D::EVERYONE@:x
```

If deny ACEs are unavailable, you can sequence and deduplicate ACEs. You do not need to differentiate the EVERYONE@ principal and the other class. You can modify an ACL with ease when the file mode creation mask is changed. In such cases, you only need to find ACEs that contain the OWNER@, GROUP@, and EVERYONE@ principals and modify these ACEs as follows.

```
A::OWNER@:rw A::GROUP@:rw A::EVERYONE@:rw
```

Conversions between NFSv4 ACLs and POSIX ACLs are not supported in some cases. POSIX ACLs do not support deny ACEs. If deny ACEs are included in an NFSv4 ACL, you cannot convert the ACL into a POSIX ACL.

### 10.3 Use POSIX ACLs to control access

access This topic describes how to configure Portable Operating System Interface (POSIX) access control lists (ACLs). You can use POSIX ACLs to control access to files and directories that reside in an NFSv3 file system. Prerequisites An NFSv3 file system is mounted. For more information, see Mount an NFS file system. Commands Before you configure POSIX ACLs, we recommend that you familiarize yourself with the related commands.

| Command | Description |
|---|---|
| getfacl <filename> | Shows the ACL that applies to the specified file. |
| setfacl -m g::w <filename> | Grants the owing group the write access. |
| setfacl -m u:player:w <filename> | Grants the player user the write access. |
| setfacl -m g:players:rwx <filename> | Grants the players group the read, write, and execute access. |

| User Guide·Directory-level ACLs tha grant the read and write access | Apsara File Storage NA |
|---|---|

| Command | Description |
|---|---|
| setfacl -x g:players <filename> | Removes permissions from the players group |
| getfacl file1 \| setfacl --set-file=- file2 | Copies the ACL for the file1 file to the file2 file. |
| setfacl -b file1 | Removes all extended ACEs from the file1 file. The base ACEs of the owner, group, and others are retained. |
| setfacl -k file1 | Removes all default ACEs from the file1 file. |
| nfs4 setfacl -R -m g:players:rw dir _ | Grants the players group the read and write access to files and subdirectories in the dir directory. |
| setfacl -d -m g:players:rw dir1 | Grants the players group the read and write access to the newly created files and subdirectories in the dir1 directory. |

Procedure To control access to files and directories by configuring NFS ACLs, follow these steps.
1. Create users and groups.
In this example, the following users are created: player, admini, and anonym. The following groups are created: players and adminis. The player user is added to the players group and the admini user is added to the adminis group.

```python
sudo useradd player sudo groupadd players sudo usermod -g players player sudo useradd admini sudo groupadd adminis sudo usermod -g adminis admini sudo useradd anonym
```

2. Configure POSIX ACLs to control access to files and directories.
Use the following commands to complete the operations: create a directory named dir0 and grant the players group the read-only access, the adminis group the read, write, and execute permissions, and the others class no access to all the files in the dir0 directory.

```python
sudo umask 777 sudo mkdir dir0 sudo setfacl -m g:players:r-x dir0 sudo setfacl -m g:adminis:rwx dir0 sudo setfacl -m u::--- dir0 sudo setfacl -m g::--x dir0 sudo setfacl -m o::--- dir0 sudo setfacl -d -m g:players:r-x dir0 sudo setfacl -d -m g:adminis:rwx dir0 sudo setfacl -d -m u::--- dir0 sudo setfacl -d -m g::--x dir0 sudo setfacl -d -m o::--- dir0
```

Use the `sudo getfacl dir0` command to verify the result after the configuration is complete.

```bash
# file: dir0
# owner: root
# group: root
user::--group::--x group:players:r-x group:adminis:rwx mask::rwx other::--default:user::--default:group::--x default:group:players:r-x default:group:adminis:rwx default:mask::rwx default:other::---
```

3. Verify the ACL configuration.
i. Verify that the admini user has read and write access to the dir0/file file.

```
[root@vbox test] sudo su admini -c 'touch dir0/file' [root@vbox test] sudo su admini -c 'echo 123 > dir0/file'
```

ii. Use the following command to verify the read-only access of the player user.

```bash
[root@vbox test] sudo su player -c 'touch dir0/file' touch: cannot touch ‘dir0/file’: Permission denied [root@vbox test] sudo su player -c 'cat dir0/file' [root@vbox test] sudo su player -c 'echo 456 >> dir0/file' bash: dir0/file: Permission denied [root@vbox test] sudo su player -c 'getfacl dir0/file'
# file: dir0/file
# owner: admini
# group: adminis
user::--group::--group:players:r-x group:adminis:rwx mask::rwx other::---
```

iii. Verify that the anonym user does not have access to the dir0/file file.

```
[root@vbox test] sudo su anonym -c 'ls dir0' ls: cannot open directory dir0: Permission denied [root@vbox test] sudo su anonym -c 'cat dir0/file' cat: dir0/file: Permission denied [root@vbox test] sudo su anonym -c 'getfacl dir0/file' getfacl: dir0/file: Permission denied
```

Related operations If you want to remove user permissions, use the following method. When you use NFSv4 ACLs, we recommend that you sort each user into different groups. This allows you to configure permissions for a group rather than a separate user. To disable access to an object from a user, you can remove the user from a group that has access to the object. For example, the following commands remove the admini user from the adminis group and add the user to the adminis2 group.

```
[root@vbox test] sudo groupadd adminis2 [root@vbox test] sudo usermod -g adminis2 admini [root@vbox test] id admini uid=1057(admini) gid=1057(admini) groups=1061(adminis2) [root@vbox test] sudo su admini -c 'ls dir0' ls: cannot open directory dir0: Permission denied [root@vbox test] sudo su admini -c 'cat dir0/file' cat: dir0/file: Permission denied [root@vbox test] sudo su admini -c 'getfacl dir0/file' getfacl: dir0/file: Permission denied
```

### 10.4 Use NFSv4 ACLs to control access

access This topic describes how to configure NFSv4 access control lists (ACLs) and apply these ACLs to NFSv4 file systems to control access to files and directories. Prerequisites An NFSv4 file system is mounted. For more information, see Mount an NFS file system. Context You can mount an NFSv4 file system on an Elastic Compute Service (ECS) instance that runs Linux and install the Linux-specific nfs4-acl-tools tool on the instance. You can use the standard nfs4_getfacl and nfs4_setfacl tools to configure NFSv4 ACLs after the installation is completed. Commands Before you configure NFSv4 ACLs, we recommend that you familiarize yourself with the related commands.

| Command | Description |
|---|---|
| nfs4 getfacl <filename> _ | Views the access permissions for the specified file. |
| nfs4 setfacl -a A::GROUP@:W <filename> _ | Adds an access control entry (ACE) that grants the GROUP@ principal the write access to the specified file. |
| nfs4 setfacl -a A::1000:W <filename> _ | Adds an ACE that grants a user principal named 1000 the write access to the specified file. |

|   | User Guide·Directory-level ACLs th |
|---|---|

| Command |   | Description |
|---|---|---|
| nfs4 setfacl -a A:g:10001:W <filename> _ |   | Adds an ACE that grants a group principal named 10001 the write access to the specified file. |
| nfs4 setfacl -e <filename> _ |   | Edits an ACL in an interactive mode. |
| nfs4 getfacl <filename> > saved acl.txt _ _ |   | Saves a list of permissions for the specified file as a TXT file. |
| nfs4 setfacl -S saved acl.txt <filename> _ _ |   | Configures permissions for the specified file by using a TXT file that includes a list of ready-made permissions. |
| nfs4 setfacl -m A::1001:rwaxTNcCy _ A::1001:rxtcy file1 |   | Modifies the permission of an ACE that applies to the file1 file. |
| nfs4 getfacl file1 \| nfs4 setfacl -S - _ _ file2 |   | Copies the permissions for the file1 file to the file2 file. |
| nfs4 getfacl file1 \| grep @ \| nfs4 setfacl _ _ -S - file1 |   | Deletes all ACEs that apply to the file1 file except for ACEs that include the following principals: OWNER@, GROUP@, and EVERYONE@. |
| nfs4 setfacl -R -a A:g:10001:rW dir _ |   | Adds an ACE that grants a group principal named 10001 the read and write access to files and subdirectories in the dir directory. |
| find dir -type f -exec sh -c 'for ace in |   |   |
|   | find dir -type f -exec sh -c 'for ace in | Deletes ACEs that grant a user principal named 1005 |
| $(nfs4 getfacl \{} \| grep "^A.*\:1005\:"); _ |   | Deletes ACEs that grant a user principal |
|   |   | access to files in the dir directory. |
| do nfs4 setfacl -x $ace \{}; done' \; _ |   |   |

|   | nfs4 setfacl -m A::1001:rwaxTNcCy _ | Modifies t |
|---|---|---|
| A::1001:rxtcy file1 |   |   |

|   | nfs4 getfacl file1 \| nfs4 setfacl -S - _ _ |   |
|---|---|---|
| file2 |   |   |

|   | nfs4 getfacl file1 \| grep @ \| nfs4 setfacl _ _ | Deletes al for ACEs t |
|---|---|---|
| -S - file1 |   |   |

| nfs4 setfacl -a A:fdg:10001:rW dir1 _ | Adds an ACE that grants a group principal named 10001 the read and write access to new files and subdirectories in the dir1 directory. |
|---|---|
| nfs4 setfacl -a A:fg:10001:rx dir1 _ | Adds an ACE that grants a group principal named 10001 the read, write, and execute access to all newly created files in the dir1 directory. |

Procedure To control access to files and directories by configuring NFSv4 ACLs, follow these steps.
1. Create users and groups.
In this example, the following users are created: player, admini, and anonym. The following groups are created: players and adminis. The player user is added to the players group and the admini user is added to the adminis group.

```python
sudo useradd player sudo groupadd players sudo usermod -g players player sudo useradd admini sudo groupadd adminis sudo usermod -g adminis admini sudo useradd anonym
```

2. Install the related tools to configure NFSv4 ACLs.
If you have installed these tools, skip this step.

```python
sudo yum -y install nfs4-acl-tools
```

3. Obtain the group IDs of the players and adminis groups.
Open the /etc/group file. The group IDs of the players and adminis groups are displayed as follows:

```
players:x:19064:player adminis:x:19065:admini
```

4. Configure NFSv4 ACLs for files and directories.
Use the following commands to complete the operations: create a directory named dir0 and add ACEs that grant the players group the read-only access, the adminis group the read, write, and execute access, and other users no access to all the files in the dir0 directory.

```python
sudo umask 777 sudo mkdir dir0 sudo nfs4_setfacl -a A:fdg:19064:RX dir0 sudo nfs4_setfacl -a A:fdg:19065:RWX dir0 sudo nfs4_setfacl -a A:fdg:OWNER@: dir0 sudo nfs4_setfacl -a A:fdg:GROUP@: dir0 sudo nfs4_setfacl -a A:fdg:EVERYONE@: dir0
```

Use the `sudo nfs4_getfacl dir0` command to verify the configuration.

```
A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:fdi:EVERYONE@:tncy A:fdi:OWNER@:tTnNcCy A:fdi:GROUP@:tncy A:g:19064:rxtncy A:g:19065:rwaDxtTnNcCy A:fdig:19064:rxtncy A:fdig:19065:rwaDxtTnNcCy
```

5. Verify the configuration of the ACL.
i. Use the following commands to verify the read and write access of the admini user.

```
[root@vbox test] sudo su admini -c 'touch dir0/file' [root@vbox test] sudo su admini -c 'echo 123 > dir0/file'
```

ii. Use the following command to verify the read-only access of the player user.

```
[root@vbox test] sudo su player -c 'touch dir0/file' touch: cannot touch ‘dir0/file’: Permission denied [root@vbox test] sudo su player -c 'echo 456 >> dir0/file' bash: dir0/file: Permission denied [root@vbox test] sudo su player -c 'cat dir0/file' [root@vbox test] sudo su player -c 'nfs4_getfacl dir0/file' A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:g:19064:rxtncy A:g:19065:rwaxtTnNcCy
```

iii. Use the following command to verify that the anonym user does not have access to the /dir0/file file.

```
[root@vbox test] sudo su anonym -c 'ls dir0' ls: cannot open directory dir0: Permission denied [root@vbox test] sudo su anonym -c 'cat dir0/file' cat: dir0/file: Permission denied [root@vbox test] sudo su anonym -c 'nfs4_getfacl dir0/file' Invalid filename: di
```

Related operations If you want to remove user permissions, use the following method. When you use NFSv4 ACLs, we recommend that you sort each user into different groups. This allows you to configure permissions only for a group rather than a separate user. To disable access to an object from a user, you can remove the user from a group that has access to the object. For example, use the following commands to remove the admini user from the adminis group and add the user to the adminis2 group:

```
[root@vbox test] sudo groupadd adminis2 [root@vbox test] sudo usermod -g adminis2 admini [root@vbox test] id admini uid=1057(admini) gid=1057(admini) groups=1054(adminis2) [root@vbox test] sudo su admini -c 'ls dir0' ls: cannot open directory dir0: Permission denied [root@vbox test] sudo su admini -c 'cat dir0/file' cat: dir0/file: Permission denied [root@vbox test] sudo su admini -c 'nfs4_getfacl dir0/file' Invalid filename: dir0/file
```
