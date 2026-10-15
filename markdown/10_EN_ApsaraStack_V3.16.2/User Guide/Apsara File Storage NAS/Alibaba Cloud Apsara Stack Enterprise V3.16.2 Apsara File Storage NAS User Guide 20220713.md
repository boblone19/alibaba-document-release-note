---
title: "Alibaba Cloud Apsara Stack Enterprise V3.16.2 Apsara File Storage NAS User Guide 20220713"
product_version: "V3.16.2"
doc_version: "20220713"
pdf_pages: 66
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.16.2 Apsara File Storage NAS User Guide 20220713.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230602/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.16.2%20Apsara%20File%20Storage%20NAS%20User%20Guide%2020220713.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise V3.16.2 Apsara File Storage NAS User Guide 20220713

## What is NAS?

Apsara File Storage NAS is a cloud service that provides file storage solutions for compute nodes. The compute nodes include Elastic Compute Service (ECS) instances, Elastic High Performance Computing (E- HPC) instances, and Container Service for Kubernetes (ACK) clusters. NAS provides standard file access protocols. You can use the distributed file storage solution that provides shared access, scalability, high reliability, and high performance without the need to modify the configurations of the applications. You can mount a NAS file system on multiple compute nodes at a time. This reduces a large number of costs in data transmission and synchronization. You can perform the following operations: Create a NAS file system and mount target. Create a permission group for the file system and add rules to the permission group. This allows access from specific IP addresses or CIDR blocks to the file system. This also allows you to grant different levels of access permissions to the IP addresses or CIDR blocks. Mount the file system on compute nodes. The compute nodes include ECS instances and ACK clusters. NAS allows you to access the file system by using the Network File System (NFS) and Server Message Block (SMB) protocols. You can also call POSIX-based APIs to access the file system. Manage file systems, mount targets, and permission groups in the NAS console. Call NAS API operations to manage file systems.

## Usage notes

Before you use NAS, take note of the following limits. Limits on file systems Maximum number of files in each file system: 1 billion. Maximum length of a file system name: 255 bytes. Maximum size of each file: 32 TB. Maximum directory depth: 1,000 levels. Maximum capacity of a Capacity NAS file system: 10 PB. Maximum number of compute nodes on which a file system can be mounted and from which the file system allows simultaneous access: 10,000. Maximum size of a protocol packet: 4 MB. Maximum number of Change Notify requests: 512. Limits on NFS clients The following list describes the limits on the usage of NFS clients: You can open up to 32,768 files at a time on an NFS client. Files in the list folder and its subfolders are not counted as part of the total number of open files. Each mount on an NFS client can obtain up to 8,192 locks across up to 256 files or processes. For example, a single process can obtain one or more locks on 256 separate files, or 8 processes can each obtain one or more locks on 32 files. We recommend that you do not use an NFS client in a Windows host to access an NFS file system. Limits on SMB clients Each file or folder can be opened up to 8,192 times in parallel across compute nodes that each have a file system mounted and users that share access to each of these file systems. This represents up to 8,192 active file handlers for each file system. A file system can have up to 65,536 active file handles. Limits on the NFS protocol NAS supports the NFSv3 and NFSv4 protocols. NFSv4.0 does not support the following attributes: FATTR4_MIMETYPE, FATTR4_QUOTA_AVAIL_HARD, FATTR4_QUOTA_AVAIL_SOFT, FATTR4_QUOTA_USED, FATTR4_TIME_BACKUP, and FATTR4_TIME_CREATE. If one of the preceding attributes is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on the client on which the file system is mounted. NFSv4.1 does not support the following attributes: FATTR4_DIR_NOTIF_DELAY, FATTR4_DIR_NOTIF_DELAY, FATTR4_DACL, FATTR4_SACL, FATTR4_CHANGE_POLICY, FATTR4_FS_STATUS, FATTR4_LAYOUT_HINT, FATTR4_LAYOUT_TYPES, FATTR4_LAYOUT_ALIGNMENT, FATTR4_FS_LOCATIONS_INFO, FATTR4_MDSTHRESHOLD, FATTR4_RETENTION_GET, FATTR4_RETENTION_SET, FATTR4_RETENTEVT_GET, FATTR4_RETENTEVT_SET, FATTR4_RETENTION_HOLD, FATTR4_MODE_SET_MASKED, and FATTR4_FS_CHARSET_CAP. If one of the preceding attributes is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on the client on which the file system is mounted. NFSv4 does not support the following operations: OP_DELEGPURGE, OP_DELEGRETURN, and NFS4_OP_OPENATTR. If one of the preceding operations is applied to a file system, an NFS4ERR_ATTRNOTSUPP error appears on the client on which the file system is mounted. NFSv4 does not support delegations. UID and GID On Linux, mappings between UIDs or GIDs and usernames or group names are defined in configurations files. For NFSv3 file systems, if the mapping between an ID and a name is defined in a configuration file, the name is displayed. If no mapping can be found for a UID or GID, the UID or GID is displayed. For NFSv4 file systems, if the version of a Linux kernel is earlier than 3.0, the usernames and group names are displayed as nobody for all files. If the kernel version is later than 3.0, the rule used by NFSv3 file systems applies to display files. Not ice If the Linux kernel version is earlier than 3.0, we recommend that you do not run the chown or chgrp command for files or directories in an NFSv4 file system. Otherwise, the UID and GID of the file or directory are changed to nobody. Limits on the SMB protocol NAS supports the SMB 2.1 protocol and later versions. NAS also supports operating systems including Windows 7, Windows Server 2008 R2, and later versions. NAS does not support Windows Vista, Windows Server 2008, or earlier versions. Compared with SMB 2.1 and later versions, SMB 1.0 provides lower performance and fewer features. Windows products that support only SMB 1.0 have reached end of support. SMB file systems do not support extended file attributes and client-side caching based on leases. SMB file systems do not support I/O control (IOCTL) or file system control (FSCTL) operations. For example, you cannot create sparse files, compress files, check the status of network interface cards (NICs), or create reparse points. SMB file systems do not support alternate data streams. SMB file systems do not support identity authentication that is provided by Active Directory (AD) or Lightweight Directory Access Protocol (LDAP). SMB file systems do not support several features that are provided by SMB 3.0 or later, such as SMB Direct, SMB Multichannel, SMB Directory Leasing, and Persistent File Handle. SMB file systems do not support access control lists (ACLs) on files or directories. Other limits Before you delete a NAS file system, you must unmount the file system from the compute node on which you mounted the file system by using a mount target. Then, delete the mount target and the file system.

## Quick start

### Log on to the NAS console

This topic describes how to log on to the Apsara File Storage NAS console. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click Aut hent icat e. For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Operations Console User Guide.
5. In the top navigation bar, click Product s. In the St orage section, click Apsara File St orage NAS.

### Create a file system

This topic describes how to create a file system in the Apsara File Storage NAS console. Context Before you create a file system, take note of the following items: You can use an Alibaba Cloud account to create up to 1,000 file systems. The maximum capacity of a Capacity NAS file system is 10 PB. If you want to increase the maximum storage capacity, we recommend that you contact Alibaba Cloud technical support. Procedure
1. Log on to the NAS console.
2. In the left-side navigation pane, choose File Syst em > File Syst em List . On the page that
appears, click Creat e File Syst em.
3. In the Creat e File Syst em panel, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region | Select the region in which you want to create the file system. |
| Organization | Select the organization to which the file system belongs. |
| Resource Set | Select the resource set to which the file system belongs. |
| Zone | Select the zone where the file system resides. |
| Cluster | Select the cluster where the file system resides. |
| File System Name | The name of the file system. The name of each file system must comply with the following naming conventions: The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
| Storage Type | Select Capacit y. The maximum capacity of a Capacity NAS file system is 10 PB. |
| Protocol Type | The protocol type. Select NFS or SMB based on your business requirements. We recommend that you mount Network File System (NFS) file systems on Linux clients and Server Message Block (SMB) file systems on Windows clients. |

| Parameter | Description |
|---|---|
| Capacity | The capacity of the file system. Valid values: 0.5 to 10240. Unit: TB. |

4. After you configure the preceding parameters, click Submit .

### Create a permission group and

add rules This topic describes how to create a permission group and add rules to the permission group in the Apsara File Storage NAS console. Context In Apsara File Storage NAS, each permission group represents a whitelist. You can add rules to a permission group to allow access to a file system from specific IP addresses or CIDR blocks. You can also grant different access permissions to different IP addresses or CIDR blocks. You can use an Alibaba Cloud account to create up to 100 permission groups. If you want to increase the limit, we recommend that you contact Alibaba Cloud technical support. Create a permission group
1. Log on to the NAS console.
2. Choose File Syst em > Permission Group and click Creat e Permission Group.
3. In the Creat e Permission Group dialog box, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | The organization to which the permission group belongs. |
| Resource Set | The resource set to which the permission group belongs. |
| Region | The region in which you want to create the permission group. |
| Name | The name of the permission group. The name of each permission group must comply with the following naming conventions: The name must be 3 to 64 characters in length. The name can contain letters, digits, and hyphens (-). |
| Network Type | The network type. Valid values: Classic Net work and VPC. Select a network type based on your business requirements. |

4. After you configure the preceding parameters, click OK.
Create a rule
1. Log on to the NAS console.
2. On the Permission Group page, find the permission group to which you want to add a rule and
click Manage.
3. Click Add Rules.
4. In the Add Rules dialog box, configure the parameters.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Authorized Address | Specifies the authorized object to which the rule applies. You can specify an IP address or CIDR block. Only IP addresses are available for permission groups of the classic network type. |
| Read/Write Permissions | Specifies whether to allow read-only or read/write access to the file system from the authorized object. Valid values: Read-only and Read/Writ e. |
| User Permissions | Specifies whether to limit access from Linux to the file system. Do not limit root users (no squash): allows access to a file system _ from root users. Limit root users (root squash): denies access to a file system from _ root users. All root users are considered nobody users. Limit all users (all squash): denies access to a file system from all _ users, including root users. All users are considered nobody users. The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system. |
| Priority | Specifies the priority of the rule. If multiple rules are applied to an authorized object, the rule that has the highest priority takes effect. Valid values: 1 to 100. A value of 1 indicates the highest priority. |

5. Click OK to create the rule.

### Create a mount target

After an Apsara File Storage NAS file system is created, you must create a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes. The compute nodes include Elastic Compute Service (ECS) instances and Container Service for Kubernetes (ACK) clusters. This topic describes how to create a mount target. Prerequisites The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Context A mount target is an endpoint that resides in a virtual private cloud (VPC) or the classic network. Each mount target corresponds to a file system. NAS file systems support mount targets of the VPC and classic network types. You can use a mount target to mount a file system on multiple compute nodes for shared access. The compute nodes include ECS instances and ACK nodes. Procedure
1. Log on to the NAS console.
2. Choose NAS > File Syst em List .
3. Find the file system and click Management in the Actions column.
4. In the left-side navigation page, select Mount T arget s.
5. On the Mount T arget tab, click Add Mount T arget .
6. In the Add Mount T arget dialog box, configure the following parameters.
Mount T arget T ype: The type of the mount target. Valid values: VPC and Classic Net work. Mount targets of the classic network type allow access only from ECS instances that belong to the same Alibaba Cloud account as the mount targets. If you want to create a mount target in a VPC, configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| VPC Network | Select the VPC in which you want to create the mount target. Not e The VPC that you specified must be the same as the VPC in which the compute nodes reside. The compute nodes include ECS instances and ACK nodes. |
| Switch | Select a vSwitch that resides in the VPC. |
| Permission Group | Select an existing permission group. |

If you want to create a mount target in the classic network, configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Permission Group | Select an existing permission group. |

7. Click OK to create the mount target.

### Mount an NFS file system

Before you mount a file system, you must create the file system and a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes. The compute nodes include Elastic Compute Service (ECS) instances and Container Service for Kubernetes (ACK) clusters. This topic describes how to mount a Network File System (NFS) file system. Prerequisites A file system is created. For more information, see Create a file system. A permission group is created and one or more rules are added to the permission group. For more information, see Create a permission group and add rules. A mount target is created. In this example, a mount target of the VPC type is used. For more information, see Add a mount target. If the mount target of a file system resides in a virtual private cloud (VPC), you can mount the file system only on an ECS instance in the VPC. The IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target. If the mount target of a file system resides in the classic network, you can mount the file system only on an ECS instance that belongs to the same Alibaba Cloud account as the mount target. The private IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target. A compute node is created. In this example, a Linux ECS instance is used. Step 1: Install an NFS client Before you mount an NFS file system on a Linux ECS instance, you must install an NFS client. If an NFS client is installed, skip this step.
1. Log on to the Linux ECS instance. For more information, see the Connect to an instance section of
the Get started topic in ECS User Guide.
2. Install an NFS client.
If CentOS, Red Hat Enterprise Linux (RHEL), or Alibaba Cloud Linux is running on the ECS instance, run the following command to install the NFS client:

```python
sudo yum install nfs-utils
```

If Ubuntu or Debian is running on the ECS instance, run the following commands to install the NFS client:

```python
sudo apt-get update sudo apt-get install nfs-common
```

Step 2: Mount an NFS file system
1. Log on to the Linux ECS instance. For more information, see the Connect to an instance section of
the Get started topic in ECS User Guide.
2. Mount the NFS file system.
Run the following command to mount the NFS file system. In the command, replace `file-system-` `id.region.nas.aliyuncs.com:/ /mnt` with an actual value. Use the NFSv4 protocol to mount a file system:

```python
sudo mount -t nfs -o vers=4.0,minorversion=0,rsize=1048576,wsize=1048576,hard,timeo=6 00,retrans=2,noresvport file-system-id.region.nas.aliyuncs.com:/ /mnt
```

Use the NFSv3 protocol to mount a file system:

```python
sudo mount -t nfs -o vers=3,nolock,proto=tcp,rsize=1048576,wsize=1048576,hard,timeo=6 00,retrans=2,noresvport file-system-id.region.nas.aliyuncs.com:/ /mnt
```

Mount parameters

| Parameter | Description |
|---|---|
| file-system- id.region.nas.aliyuncs. com:/ /mnt | <Endpoint of the mount target>:<Name of the shared directory> <Path of the mount directory>. Replace the domain name of the mount target, the name of the shared directory, and the path of the mount directory with actual values. Endpoint of the mount target: You can log on to the NAS console, find the file system that you want to manage, and then click Manage to go to the Details page. Then, you can obtain the endpoint of the mount target of the file system on the Mount ing Use tab. Directory of the NAS file system: the root directory (/) or a subdirectory, for example, /sub1. If a subdirectory is specified, make sure that the subdirectory exists. Path of the mount directory : the root directory / of the Linux ECS instance or a subdirectory, for example, /mnt. If the mount directory is a subdirectory, make sure that the subdirectory exists. |
| vers | The protocol version of the file system. Only NFSv3 and NFSv4 are supported. vers=3: uses NFSv3 to mount the file system. vers=4.0: uses NFSv4 to mount the file system. |
| Mount options. | If you want to mount a file system, you can specify multiple mount options. Separate multiple mount options with commas (,). For example, you can specify the following mount options: rsize: specifies the size of each data block that a client can read from the file system. Recommended value: 1048576. Unit: bytes. wsize: specifies the size of each data block that a client can write to the file system. Recommended value: 1048576. Unit: bytes. Not e To prevent performance degradation, we recommend that you specify the maximum value (1048576) for both the rsize mount option and the wsize mount option. hard: specifies that applications stop accessing a file system when the file system is unavailable, and wait until the file system is available. We recommend that you enable the hard parameter. timeo: specifies the period of time for which the NFS client waits before the client retries to send a request. Unit: deciseconds (tenths of a second). Recommended value: 600 (60 seconds). Not e If you need to modify the timeo mount option, we recommend that you specify 150 or a greater value. The timeo mount option is measured in deciseconds (tenths of a second). For example, the value 150 indicates 15 seconds. retrans: specifies the number of retries after the NFS client fails to send a request. Recommended value: 2. |

| Parameter | noresvport: specifies that a new TCP port is used to ensure network Description connectivity between the file system and the ECS instance when the |
|---|---|
|   | network recovers from failure. We recommend that you enable the noresvport parameter. Not e When you configure parameters, take note of the following items: To prevent data inconsistency, we recommend that you do not use the soft mount option. Use of the soft option is at your own risk. We recommend that you use the default values for other mount options. A decrease in performance may occur due to changes in specific mount options. These mount options include the size of the read or write buffer or the use of attribute caching. |

3. Run the `mount -l` command to view the mount result.
If the output that is similar to the following information appears, the mount is successful. After the file system is mounted, you can run the `df -h` command to view the size of the file system.
4. After the SMB file system is mounted, you can read data from and write data to the NAS file
systems on the ECS instance. You can access the file system the same way you access a local directory. The following figure shows an example.

### Mount an SMB file system

Before you mount a file system, you must create the file system and a mount target for the file system. Then, you can use the mount target to mount the file system on compute nodes such as Elastic Compute Service (ECS) instances. This topic describes how to mount a Server Message Block (SMB) file system. Prerequisites
1. A file system is created. For more information, see Create a file system.
2. A permission group is created and one or more rules are added to the permission group. For more
information, see Create a permission group and add rules.
3. A mount target is created. In this example, a mount target of the VPC type is used. For more
information, see Add a mount target. If the mount target of a file system resides in a virtual private cloud (VPC), you can mount the file system only on an ECS instance in the VPC. The IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target. If the mount target of a file system resides in the classic network, you can mount the file system only on an ECS instance that belongs to the same Alibaba Cloud account as the mount target. The private IP address of the ECS instance must be added as an authorized address to a rule in the permission group that is attached to the mount target.
4. An ECS instance is created. In this example, a Windows ECS instance is used.
5. The following services on the Windows host are started:
Workstation a. Choose All Programs > Accessories > Run, or press `Win+R` and enter `services.msc` to go to the Services console. b. Make sure that the Workstation service is in the St art ed state and the startup type is Aut omat ic. By default, the Workstation service is in the Started state. TCP/IP NetBIOS Helper To start the TCP/IP NetBIOS Helper service, perform the following steps: a. On the Net work and Sharing Cent er page, click the active network connection. b. Click Propert ies to open the Local Area Network Properties dialog box. Double-click Int ernet Prot ocol Version 4 (T CP/IPv4) to open the Internet Protocol Version 4 (TCP/IPv4) Properties dialog box, and then click Advanced. c. In the Advanced T CP/IP Set t ings dialog box, choose WINS > Enable Net BIOS over T CP/IP. d. Choose All Programs > Accessories > Run, or press `Win+R` and enter `services.msc` to go to the Services console. e. Make sure that the TCP/IP NetBIOS Helper service is in the St art ed state and the startup type is Aut omat ic. By default, the TCP/IP NetBIOS Helper service is in the Started state. Procedure
1. Log on to the Windows ECS instance. For more information, see the Connect to an instance section
of the Get started topic in ECS User Guide.
2. Open the Command Prompt and run the following command to mount an SMB file system:

```
net use D: \\file-system-id.region.nas.aliyuncs.com\myshare
```

The syntax of the command is net use <the letter of a local drive> \\<the domain name of a

```
mount target>\myshare .
```

Letter of the destination drive: the letter of the drive on which you want to mount an SMB file system. Replace the value of the parameter with the letter of an actual destination drive. The letter of the destination drive must be different from the existing drive letters. The domain name of the mount target: When you create a mount target for a file system, the domain name of the mount target is automatically generated. You can replace the domain name based on your business requirements. To obtain the mount target of the file system, perform the following steps: Log on to the NAS console, find the file system that you want to manage, and then click Manage to go to the Details page. myshare: the name of the shared SMB directory. You cannot change the name.
3. Run the `net use` command to check the mount result.
If the output that is similar to the following information appears, the mount is successful.
4. After the SMB file system is mounted, you can read data from and write data to the NAS file
systems on the ECS instance.

## File systems

### View the details of a file system

This topic describes how to view the details of a file system. The details include the information about the file system and the attached mount targets. You can view the details of a file system in the Apsara File Storage NAS console. Prerequisites A file system is created. For information about how to detach a tag policy from an object, see Create a file system. Procedure
1. Log on to the NAS console.
2. Choose NAS > File Syst em List .
3. Find the file system and click Management to go to the details page of the file system.
The details page consists of the following sections: Basic Inf ormat ion: In this section, the information about the file system is displayed. The information includes the ID, region, protocol type, and storage specifications. Mount ing T arget s: In this section, the list of mount targets attached to the file system is displayed. You can manage the mount targets and view the clients on which the file system is mounted. Quot a Management : In this section, the quota status of each directory in the file system is displayed. You can create, modify, and delete quotas for each directory.

### Delete a file system

This topic describes how to delete a file system in the Apsara File Storage NAS console. Prerequisites The number of mount targets is 0. For more information about how to view the number of mount targets, see View the details of a file system. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > File Syst em List .
3. Find the file system that you want to manage, and click Manage.
Not ice Before you can delete a file system, you must remove all mount targets from the file system. Proceed with caution when you delete a file system. After a file system is deleted, the data on the file system cannot be restored. Make sure that all data is backed up.
4. In the Delet e File Syst em dialog box, click OK to complete the deletion.

### Scale up a file system

If the used space of an Apsara File Storage NAS file system reaches the specified capacity, data can no longer be written to the file system. To ensure the availability of the NAS service, we recommend that you scale up the file system before the used space reaches the specified capacity. This topic describes how to scale up a file system in the NAS console. Prerequisites A file system is created. For more information, see Create a file system. Not ice A file system can be scaled up but cannot be scaled down. . A Capacity NAS file system can be scaled out to up to 10 PB. Procedure
1. Log on to the NAS console.
2. In the left-side navigation pane, choose File Syst em > File Syst em List .
3. Find the file system and click Upgrade in the Operat ions column.
4. In the Upgrade dialog box, specify a desired capacity for the file system in the New T ot al
Capacit y field.
5. Click OK.

## Mount targets

### View mount targets

This topic describes how to view mount targets in the Apsara File Storage NAS console. Context The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Optional. The update package is verified. Procedure
1. Log on to the NAS console.
2. Choose NAS > File Syst em List .
3. Find the file system and click Management in the Actions column.
4. In the left-side navigation pane, click Mount ing T arget s. On the Mount ing T arget tab, view the
mount targets of the file system.

### Enable or disable a mount target

This topic describes how to enable or disable a mount target. You can control access to a mount target from clients by enabling or disabling the mount target. Prerequisites The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Optional. The update package is verified. Procedure
1. Log on to the NAS console.
2. Choose NAS > File Syst em List .
3. Find the file system and click Management in the Actions column.
4. In the left-side navigation pane, click Mount ing T arget s. After you find the mount target that
you want to disable or enable, you can perform the following operations: To disable the mount target, click Disable. In the Disable Mount Target dialog box, click OK to deny access to the mount target from clients. To enable the mount target, click Enable. In the Enable Mount Target dialog box, click OK to allow access to the mount target from clients.

### Delete a mount target

This topic describes how to delete a mount target in the Apsara File Storage NAS console. Prerequisites A file system is unmounted from the compute node such as an ECS instance and ACK cluster on which you mounted the file system by using a mount target. The mount targets that are created by using a Cross-domain mount orchestration are deleted. Procedure
1. Log on to the NAS console.
2. Choose NAS > File Syst em List .
3. Find the file system and click Management in the Actions column.
4. In the left-side navigation pane, click Mount ing T arget s.
5. Find the mount target that you want to delete and click Delet e.
Not ice Proceed with caution when you delete a mount target. After you delete a mount target, you cannot restore the mount target.
6. In the Delete Permission Group message, click OK.

### Modify the permission group of a

mount target You must add a permission group to each mount target. You can modify the permission group of a mount target in the Apsara File Storage NAS console. Prerequisites The following operations are completed: Create a file system of application management in Kubernetes clusters Create a permission group and add rules of application management in ECS clusters Optional. The update package is verified. Procedure
1. Log on to the NAS console.
2. Choose File Syst em > File Syst em List .
3. Find the file system and click Management in the Actions column.
4. Click Mount ing T arget s to go to the Mount ing T arget tab.
5. Find the mount target that you want to modify and click Modif y Permission Group.
6. In the Modif y Permission Group dialog box, change the permission group and click OK.

## Permission groups

### View permission groups

This topic describes how to view permission groups in the Apsara File Storage console. Prerequisites A permission group is created. For information about how to detach a tag policy from an object, see Create a permission group and add rules. Procedure
1. Log on to the NAS console.
2. Choose File Syst em > Permission Group and view the permission groups.

### Delete a permission group

This topic describes how to delete a permission group in the Apsara File Storage NAS console. Prerequisites A permission group is created. For more information, see Create a permission group and add rules. Operating system
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > Permission Group.
3. Find the target permission group and click Delet e.
Permission groups in use cannot be deleted. Before you can delete a permission group, you must remove the permission group from the linked mount target.
4. In the Delete Permission Group dialog box, click OK.

### Manage permission group rules

This topic describes how to manage permission group rules in the Apsara File Storage NAS console. The management includes viewing the details of rules, modifying rules, and deleting rules. Prerequisites A permission group and a permission group rule are created. For more information, see Create a permission group and add rules. Procedure
1. Log on to the Apsara File Storage NAS console.
2. Choose NAS > Permission Group.
3. Find the target permission group and click Manage.
4. On the Rules page, you can perform the following operations:
View all rules for the permission group. Modify a rule. Find the target rule and click Edit to modify the details of the rule. The details include the aut horizat ion address, read/writ e permissions, user permission, and priorit y. Delete a rule. Find the target rule and click Delet e. In the Delete Rule dialog box, click OK.

## Manage quotas

This topic describes how to use the Alibaba Cloud quota_tool tool to manage quotas on Elastic Compute Service (ECS) instances that have Apsara File Storage NAS file systems mounted. You can configure, view, and cancel quotas on these ECS instances. Prerequisites A Network File System (NFS) file system of the NAS Capacity or NAS Performance type is mounted on an ECS instance. For more information, see Mount an NFS file system. Context Apsara File Storage NAS provides the quota management feature to help you view and manage directory quotas. A directory quota specifies the maximum number of files in a directory of a NAS file system and the maximum storage space for these files. Directory quotas can be classified into the quotas for all users and the quotas for a single user or user group. The quotas for all users specify the maximum storage space for files that all users can create in a directory. The quotas for a single user or user group specify the maximum storage space for files that a user or user group can create in a directory. Directory quotas can also be classified into statistical quotas and restricted quotas. If you create a statistical quota for a directory, NAS calculates only the storage usage of the directory. You can query and view the statistical data. If you create a restricted quota for a directory and the storage usage exceeds the quota, you can no longer create files or subdirectories for the directory, or write data to the directory. Not ice Only statistical quotas are available. NAS performs asynchronous calculation for quotas at the backend. When you use the quota_tool tool to query the statistical data about quotas, the process requires a period of time to complete. In most cases, the time period is about 5 to 15 minutes. Configure quotas This topic uses the /mnt directory as an example.
1. Log on to a Linux ECS instance by using a root account.
You can use the quota_tool tool on an ECS instance that has a NAS file system mounted. You must run the tool with the root permissions. This example shows you how to use the quota_tool tool on the ECS instance.
2. Run the following command to download the quota_tool tool.

```
wget https://nasimport.oss-cn-shanghai.aliyuncs.com/quota_tool_v1.0 -O quota_tool
```

3. Run the following command to grant the execute permissions to the quota_tool tool.

```python
sudo chmod a+x quota_tool
```

4. Configure quotas.
For each file system, you can configure quotas for a maximum of 10 directories. You can run the `sudo ./quota_tool set --dir [DIR] [OPTION]` command to configure quotas. The following table describes the parameters.

| Parameter | Description |
|---|---|
| --dir [DIR] | The directory for which you want to configure quotas, for example, --dir /mn t/data/. |
| OPTION | The required options. Not e When you specify options, you must follow these rules: 1. You must specify the --accounting option. 2. You must specify one of the --alluser, --uid, and --gid options. --accounting: specifies a statistical quota. --alluser: specifies a directory quota for all users. --uid: specifies the UID of a user. For example, --uid 505 specifies that the quota is configured only for the user whose UID is 505. --gid: specifies the GID of a group. For example, --gid 1000 specifies that the quota is configured only for the group whose GID is 1000. |

The following examples show you how to configure quotas. Run the following command to configure a statistical quota for the /mnt/data/ directory to limit the total number of files in the directory.

```python
sudo ./quota_tool set --dir /mnt/data/ --accounting --alluser
```

Run the following command to configure a statistical quota for the /mnt/data/ directory to limit the total number of files that can be created by the user whose UID is 505.

```python
sudo ./quota_tool set --dir /mnt/data/ --accounting --uid 505
```

Query quotas After you configure a quota for a directory in a NAS file system, you can query the statistical data about the directory quota.
1. Log on to the ECS instance by using a root account.
2. Run the following command to query quotas.

```python
sudo ./quota_tool get --dir /mnt/data/ --all
```

In the preceding command, the --all parameter is optional. If you specify the parameter, the statistical data about all quotas that are configured for the file system is returned. The first time you query a quota, the returned status of the quota is Init ializing. After the initialization process is completed, the returned status of the quota is Success. The duration of the initialization process depends on the number of files and subdirectories in the directory of your file system. After the initialization process is completed, you can query quotas daily. The returned values of the FileCountReal and SizeReal parameters are collected 5 to 10 minutes earlier. This is because the statistical data about quotas is asynchronously calculated at the backend. The following table describes the parameters that are included in a JSON-formatted response.

| Parameter | Description |
|---|---|
| Path | The directory for which you query a quota. |
| Report | The statistical data about the directory quota. The statistical data is returned based on the specified UID and GID. |
| ReportStatus | The status of the query. |
| FileCountLimit | The limit on the number of files. The value Empty indicates no limit. |
| FileCountReal | The total number of files in the directory, including subdirectories, files, and special files. |
| QuotaType | The quota type. Valid values: Accounting and Force. Accounting indicates a statistical quota and Force indicates a restricted quota. |
| Uid | The UID of a user. The value All indicates all users. |
| Gid | The GID of a group. The value All indicates all groups. |
| SizeLimit | The upper limit of file size. The value Empty indicates no limit. |
| SizeReal | The total size of files in the directory. |

Cancel quotas You can cancel quotas that you no longer need.
1. Log on to the ECS instance.
2. Run the following command to cancel quotas.
You can run the `sudo ./quota_tool cancel --dir [DIR] [OPTION]` command to cancel quotas. The following table describes the parameters.

| Parameter | Description |
|---|---|
| --dir [DIR] | The directory for which you want to cancel quotas, for example, -dir /mnt/d ata/. |
| OPTION | The required options. Not e You must specify one of the --alluser, --uid, and --gid options. --alluser: specifies a directory quota for all users. --uid: specifies the UID of a user. For example, --uid 505 specifies that the quota is canceled for the user whose UID is 505. --gid: specifies the GID of a group. For example, --gid 1000 specifies that the quota is canceled for the group whose GID is 1000. |

The following examples show you how to cancel quotas. If you have configured a quota for the /mnt/data/ directory, run the following command to cancel the quota for the user whose UID is 100.

```python
sudo ./quota_tool cancel --dir /mnt/data/ --uid 100
```

If you have configured a quota for the /mnt/data/ directory, run the following command to cancel the quota for all users.

```python
sudo ./quota_tool cancel --dir /mnt/data/ --alluser
```

aces

## Manage unified namespaces

This topic describes how to create a unified namespace and create a mount target for the unified namespace in the Apsara File Storage NAS console. The topic also describes how to add, remove, and modify file systems in a namespace, view namespace details, and enable the cross-domain mount orchestration feature. Features A unified namespace allows you to mount multiple file systems on a NAS cluster by using a single endpoint. You do not need to maintain multiple mount targets and mount directories. You can create a mount target for a unified namespace. You can use a unified namespace to manage multiple file systems the same way you manage a single file system. A unified namespace contains a virtual root directory in which file systems are the first-level subdirectories. After you add a file system to a unified namespace, you can still mount the file system by using the mount targets of the file system. Limits A unified namespace has the following limits: You can add a maximum of 1,000 file systems to each unified namespace. The mapping name of a file system in a unified namespace cannot exceed 255 characters in length. The name can contain only letters, digits, and the following special characters: .+-_()<>@# To enable a cross-domain mount orchestration, the mount directory name of a unified namespace cannot exceed 255 characters. The name can contain only letters, digits, and the following special characters: .+-_()<>@# You can create up to two mount targets for each unified namespace. You can create up to 20 namespaces in each region. You can mount a unified namespace only by using the NFSv3 protocol. The file systems that are added to a namespace must belong to the same Alibaba Cloud account and cluster as the namespace. The storage type, protocol type, and encryption type of the file systems must be the same. The mapping name of a file system must be unique in each unified namespace. File systems can be mapped only to first-level subdirectories in a unified namespace. You cannot modify the access permissions, owner, or access control lists (ACLs). Basic features of unified namespace Create a unified namespace and create a mount target for the unified namespace. i. Log on to the NAS console. ii. In the left-side navigation pane, choose Unif ied Namespace > Unif ied Namespaces. iii. On the Unif ied Namespaces page, click Creat e Namespace. Then, create a namespace and a mount target for the namespace as prompted. aces If you create mount targets in virtual private clouds (VPCs) for unified namespaces in different regions, we recommend that you use different CIDR blocks. This way, the CIDR blocks can be identified when you mount unified namespaces across regions. For example, you can use `192.168.0.0/16` for Region 1 and `172.16.0.0/16` for Region
2. For more information, see Step 1: Create a VPC in the Cross-domain mount orchestration
section. Add a file system to the unified namespace. After you create the unified namespace, you can add a file system and specify a mapping name for the file system. The mapping name is the name of the virtual directory for the file system. Remove the file system from the unified namespace. You can remove the existing file system from the unified namespace. The file system is not deleted but removed from the file system list of the namespace. Change the mapping name of the file system. You can change the mapping name of the file system in the unified namespace. If a symbolic or hard link exists between a file system and another file system, a connection failure may occur when you modify the mapping name of the file system. View the details of the unified namespace. The details of the namespace are divided into three sections: Properties Mount target list You can create or delete mount targets. File system list You can add or remove file systems. aces Cross-domain mount orchestration In traditional solutions, you can add a file system to a namespace only if the file system and namespace reside in the same region. To add file systems to namespaces across multiple regions, NAS provides the cross-domain mount orchestration feature. To use this feature, perform the following operations: Create a unified namespace and a mount target for the namespace. Map the unified namespace to the local directory tree of a client by using the cross-domain mount orchestration feature. After the orchestration is complete, specify the root directory to generate an automatic mount script. Not ice The specified mount target and mapping path cannot be modified after the map is created. You can remove the map. However, if you create the map again, the specified mount target can only be attached to the original mapping path. To mount the namespace on a client, you can run the automatic mount script on the client. This allows the client to access file systems across regions. The format of the local path on the client for each unified namespace is <Specified root directory>`/`<Mapping path of the namespace>. To enable a cross-domain mount orchestration for different VPCs that reside in different regions, you must establish VPC connections. The following procedure provides an example on how to establish VPC connections and enable a cross-domain mount.
1. Create two VPCs.
i. Log on to the NAS console. ii. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud. aces iii. On the Creat e VPC page, create two VPCs. One VPC is for Region 1 and the other VPC is for Region 2. Create a VPC named skvpc1 `192.168.1.0/24` for Region 1. Create a VPC named skvpc2 `192.168.2.0/24` for Region 2.
2. Configure an Express Connect circuit across regions.
Configure two Express Connect circuits between the VPCs of the two regions. Configure one Express Connect circuit in Region 1 to connect skvpc1 to skvpc2. aces i. Configure a route table for skvpc1. Add the CIDR block `192.168.2.0/24` of skvpc2 to the route table of skvpc1. a. In the left-side navigation pane, click Rout e T ables. b. On the Rout e T ables page, find the instance ID of skvpc1 and click Management in the Actions column. c. On the Rout ing ent ry list tab, click Add rout e ent ry. In the dialog box that appears, configure the parameters. Click Creat e VPC-t o-VPC Connect ion to configure an Express Connect circuit between skvpc1 and skvpc2. Specify the CIDR block of skvpc2 for Dest inat ion CIDR Block. Select Rout er Int erf ace (VPC Direct ion) from the Next hop t ype dropdown list. The first time you configure an Express Connect circuit across regions, no VPCs are available. aces ii. Create a VPC-to-VPC connection a. Click Create VPC interconnection to go to the Creat e Peering Connect ion page. On the page that appears, specify the source VPC ID, destination VPC ID, and bandwidth based on your business requirements. Click Submit . b. After the VPC-to-VPC connection is created, click Back t o Console to go to the VPC-to- VPC page. If the initiator and acceptor are in the Activated state, the connection from skvpc1 to skvpc2 is established. Establish the other connection from skvpc2 to skvpc1 in Region 2. iii. View the VPC-to-VPC connection. Go to the Add Rout e Ent ry page. The VPC-to-VPC connection that you created appears in the VPC list. aces Configure the other Express Connect circuit in Region 2 to connect skvpc2 to skvpc2. Perform the preceding procedure. In the Add Route Entry panel, select the VPC-to-VPC connection from the VPC list and click OK. The route entry is added to skvpc2 in Region 2. You can select the VPC-to-VPC connection that you created from the VPC list. `vpc-ew2`xxxx is the ID of skvpc1.
3. Add a rule to a permission group.
i. In the top navigation bar, choose Product s > St orage > Apsara File St orage NAS . ii. In the left-side navigation pane, choose Permission Group. On the Permission Group page, find the permission group to which you want to add a rule, or create a permission group. Then, click Add Rule. iii. Click Add Rule. In the dialog box that appears, specify an authorized address and read and write permissions. In the following figure, the IP segment of skvpc1 is added.
4. Creates a mount target.
In Region 2, you can create a mount target that resides in skvpc2 for the specified unified namespace. In Region 1, you can create a mount target that resides in skvpc1 for the specified unified namespace.
5. Create an Elastic Compute Service (ECS) instance.
For example, if you select skvpc2 when you create an ECS instance, you can mount file systems on the ECS instance without the need to establish a VPC connection. The following figure shows an example. aces In most cases, each ECS instance uses an independent VPC. You do not need to establish connections between VPCs that are used by mount targets of namespaces in two different regions. However, you must establish connections between the VPC that is used by mount targets of the namespace and the VPC that is used by the ECS instance.

## Lifecycle management

This topic describes how to use the lifecycle management feature in the Apsara File Storage NAS console. The topic also describes how to configure lifecycle policies and dump cold data to an Infrequent Access (IA) storage medium based on the policies. In the NAS console, you can create, view, and modify lifecycle policies. You can also query the usage of General-purpose NAS storage and IA storage media. Prerequisites A Network File System (NFS) file system of the Capacity or Performance type is mounted on an Elastic Compute Service (ECS) instance. For more information, see Mount an NFS file system. Context The lifecycle management feature of NAS allows you to use tiered storage to manage hot data and cold data. You can configure lifecycle policies and dump infrequently accessed data to an IA storage medium based on the policies to reduce your storage costs. You can still access the data in the IA storage medium the same way you access the data in a NAS file system. Limits The lifecycle management feature supports only NFS file systems. Server Message Block (SMB) file systems and file systems whose data is encrypted are not supported. Usage notes In Apsara Stack, the lifecycle management feature allows you to dump cold data from a NAS file system to a specified Object Storage Service (OSS) bucket. However, you must be the owner of the specified NAS file system and OSS bucket. You cannot delete the OSS bucket before you retrieve the cold data to the NAS file system. Otherwise, data loss may occur and the associated NAS cluster may become unavailable. You cannot revoke permissions that you granted to NAS by using Resource Access Management (RAM). We recommend that you minimize the permissions on the OSS bucket to prevent data leaks. We recommend that you use an independent OSS bucket for the lifecycle management feature of NAS. This prevents cold data from being accidentally deleted if you store the cold data with other business data in the same OSS bucket. Prepare for data migration
1. Authorize NAS by using RAM.
To use the lifecycle management feature, you must grant access permissions on OSS to NAS. This way, NAS can read data from and write data to specified OSS buckets. Not ice If you want to create a RAM role, you must specify an organization in which the file system resides. In this example, an organization named nas-test is specified. You need to grant permissions to NAS only once for an organization. i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, click Conf igurat ions. iii. On the RAM Roles page, click Creat e Service-linked Role to create a RAM role and grant access permissions on OSS to the role. iv. View the authorization status of nas-test in the role list to verify that AliyunNASTieringRole is in the list.
2. Create an OSS bucket.
You can use an existing OSS bucket or create an OSS bucket. NAS allows you to configure multiple OSS buckets for each file system. If you use an existing OSS bucket, the following requirements must be met: The OSS bucket is in the first cluster of the region. The domain name of the first cluster starts with oss- and the domain names of the other clusters start with ossxxxx. The OSS bucket and the file system belong to the same organization. In the top navigation bar, choose Product s > Object St orage Service. In the left-side navigation pane, click Bucket s. On the Buckets page, click Creat e Bucket . On the Create OSS Bucket page, configure the parameters. In this example, an OSS bucket named nastiering is created. The OSS bucket is used to store cold data. Before you create an OSS bucket, the following requirements must be met: St orage Class is selected as St andard and the first cluster in the region is selected for the OSS cluster. The domain name of the first cluster starts with oss- and the domain names of the other clusters start with ossxxxx. The OSS bucket and the file system belong to the same organization. Get started with Alibaba Cloud Elasticsearch
1. Create a lifecycle policy.
i. In the top navigation bar, choose Product s > Apsara File St orage NAS. ii. In the left-side navigation pane, click Lif ecycle Management . iii. On the Lif ecycle Management page, click Creat e Policy and configure the parameters. After you create a lifecycle policy for a directory in the file system, NAS dumps the cold data that meets the rule of the policy to the IA storage medium. If you want to create a lifecycle policy, you must configure the following parameters: Policy Name: the name of the policy. The name must be unique within different policies. File System: the file system for which the lifecycle policy is configured. Directory Path: the directory path on the file system. The path must start with a forward slash (/). You can enter a forward slash (/) to indicate the root directory. If you select Recursive Subdirect ory, all subdirectories in the directory are recurred. Management Rules: the pre-configured rules of the policy. You can select a rule to dump files that are not accessed for more than 14, 30, 60, or 90 days to an IA storage medium. OSS Bucket: the OSS bucket to which cold data is dumped. Cold data in a file system can be dumped to only one OSS bucket. Only the OSS buckets of the organization in which the file system resides are displayed in the OSS Bucket list.
2. View the lifecycle policy.
On the Lif ecycle Management page, you can view the lifecycle policy that you have created. You can also filter the policies by file system ID.
3. Modify the lifecycle policy.
On the Lif ecycle Management page, you can modify the lifecycle policy. You can configure the following parameters: Recursive Subdirectory Management Rule
4. Query the usage of the General-purpose NAS storage and IA storage medium.
In the left-side navigation pane, click File Syst em List . You can query the usage of Generalpurpose NAS storage and IA storage medium within the file system for which you configured the lifecycle policy.

## Directory-level ACLs that

grant the read and write access

### Overview

Apsara File Storage NAS supports NFSv4 access control lists (ACLs) and Portable Operating System Interface for UNIX (POSIX) ACLs. This topic introduces POSIX ACLs and NFSv4 ACLs and describes the usage notes for these ACLs. Access control and user management are important for enterprise users who need to share files among different users and groups by using a shared file system. To control access to different files and directories, you can grant users and groups different types of access. NAS provides Network File System (NFS) ACLs to allow you to meet specific requirements. An ACL consists of one or more access control entries (ACEs) that each grant a user or group one or more permissions to access a file or directory. The NFSv3 protocol implements access control by using the file mode creation mask (umask). The POSIX ACL feature is an extension to this permission model. You can grant permissions to specific users and groups in addition to the owner, group, and other classes. In a file system, a directory or file can inherit the permissions from its parent directory. For more information, see acl(5) - Linux man page. The NFSv4 ACL feature is an extension to the NFSv4 protocol. Compared with POSIX ACLs, NFSv4 ACLs provide finer-grained access control. For more information, see nfs4_acl(5) - Linux man page. You can use the NFSv3 protocol to mount a file system to which NFSv4 ACLs are applied. After the file system is mounted, the NFSv4 ACLs are converted into POSIX ACLs. You can also use the NFSv4 protocol to mount a file system to which POSIX ACLs are applied. After the file system is mounted, the POSIX ACLs are converted into NFSv4 ACLs. However, NFSv4 ACLs and POSIX ACLs are not fully compatible. The interaction between ACLs and the umask is not in an ideal state. NFSv3 file systems do not support locks. Therefore, if you use NFS ACLs, we recommend that you use the NFSv4 protocol to mount file systems and configure only NFS ACLs for the file systems. We also recommend that you do not use the umask or POSIX ACLs along with NFSv4 ACLs. For more information, see Features. Usage notes for POSIX ACLs We recommend that you use the default method that allows a subdirectory or file to inherit the ACL from the parent directory. Then, you do not need to configure another ACL when you create a file or subdirectory in the parent directory. A file system scans all ACEs each time it performs a permission check. To ensure optimal performance, we recommend that you retain a minimum number of ACEs. If redundant ACLs exist, the performance of the file system degrades. Proceed with caution when you configure ACLs by using the recursive method ( `setfacl -R` ). A large amount of metadata is generated when you apply an ACL recursively to a directory that contains a large number of files and subdirectories. This may negatively affect your business. Before you configure ACLs, we recommend that you manage groups and the corresponding permissions. For example, you can add a user to one or more groups. To add, remove, or change permissions for a user, you can move the user to a group that has the required permissions. You need to modify the ACL of the group only if the group structure changes. We recommend that you configure ACLs for groups rather than individual users. This is a simple and time-saving method to implement access control. You can apply a POSIX ACL to a user or group that accesses the file system from multiple clients. NAS identifies the user or group based on the user ID (UID) or group ID (GID). Therefore, you must set the same UID or GID for the user or group on the clients. All users have the permissions that are granted to the other class. Therefore, we recommend that you grant the least permissions to the other class. If the other class has more permissions than an ACE, a security vulnerability may exist. We recommended that you grant the least permissions to the other class. Before you create files or directories, run the `umask 777` command to configure the umask. This command sets the umask to 000 when a file or directory is being created. This ensures that the new file or directory has the least permissions. For more information about umask and the default mode, see Why doesn't umask change execute permissions on files? After you enable the POSIX ACL feature, the other class is moved to the everyone@ user category and the umask is also set. When NAS performs a permission check, NAS treats the other class as everyone. Usage notes for NFSv4 ACLs We recommend that you use UIDs or GIDs such as UID 1001 to configure ACLs. We recommend that you do not configure the umask along with NFSv4 ACLs. The `nfs4_setfacl` command provides multiple options such as the -a, -x, and -m options to add, remove, and modify ACEs. We recommend that you run the `nfs4_setfacl -e <file>` command to edit an ACL in an editor. NAS NFSv4 ACLs support Allow ACEs rather than Deny ACEs. All users have the permissions that are granted to everyone. Therefore, we recommend that you grant the least permissions to everyone. If everyone has more permissions than an ACE, a security vulnerability may exist. NFSv4 ACLs support fine-grained permissions. In most cases, permission control based on fine-grained write permissions is unnecessary. For example, if a user has the write-data (w) access to a file but does not have the append-data (a) access, an error may occur when the user writes data to the file. The same issue occurs for a directory. To prevent unexpected permission errors, we recommend that you specify a capital W when you run the `nfs4_setfacl` command to configure an ACL. The `nfs4` `_setfacl` command specifies full write access. For a file, W is expanded to wadT. For a directory, W is expanded to wadTD. We recommend that you use the default method that allows a subdirectory or a file to inherit the ACL from the parent directory. Then, you do not need to configure another ACL when you create a file or subdirectory in the parent directory. A file system scans all ACEs each time it performs a permission check. To ensure optimal performance, we recommend that you retain a minimum number of ACEs. If redundant ACLs exist, the performance of the file system degrades. Proceed with caution when you configure ACLs by using the recursive method ( `nfs4_setfacl -R` ). A large amount of metadata is generated when you apply an ACL recursively to a directory that contains a large number of files and subdirectories. This may negatively affect your business. Before you configure ACLs, we recommend that you manage groups and the corresponding permissions. For example, you can add a user to one or more groups. To add, remove, or change permissions for a user, you can move the user to a group that has the required permissions. You need to modify the ACL of the group only if the group structure changes. We recommend that you configure ACLs for groups rather than individual users. This is a simple and time-saving method to implement access control.

### Features

This topic describes the features of NFSv4 access control lists (ACLs) and POSIX ACLs. Features of Apsara File Storage NAS NFSv4 ACLs Only access control entries (ACEs) of the allow type are supported. ACEs of the following types are not supported: deny, audit, and alarm. Deny ACEs increase the complexity of access control. In most cases, complexity leads to confusion and increases potential security risks. As agreed by the industry, we recommend that you do not use deny ACEs. For more information about why deny ACEs are not recommended, see FAQ. Audit and alarm ACEs are not available for NFS file systems. However, you can audit file systems and configure alerts based on auditing results in the NAS console. If no ACL is set for a file or a directory, the default ACL that corresponds to the predefined umask is applied. Example: i. Run the `touch file` command to enter the file. ii. Run the `ls -l file` command to view the permissions on the file.

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

Add an ACE of the read and write permissions to the following ACL for a user principal named 1009. The ACE is placed after the ACE that is defined for a user principal named 1001 based on the predefined order. Run the following commands:

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

All ACEs can be inherited. i. For example, the OWNER principal has the write permissions, the GROUP principal has the read permissions, and the EVERYONE has no permissions on the dir directory. Run the following commands:

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

Create a subdirectory in the dir directory Run the following commands:

```
mkdir dir/subdir nfs4_getfacl dir/subdir
```

Sample command output:

```bash
# file: dir/subdir
A::OWNER@:rwaDxtTcCy A::GROUP@:rwaDxtcy A::EVERYONE@:rwaDxtcy A:fdi:1000:rwx
```

We recommend that you grant the least permissions to the EVERYONE principal. Before you run one of the preceding commands, we recommend that you run the `umask 777` command. This command ensures that no access to a file or directory is granted when the file or directory is created. For more information about umask and the default mode, see Why doesn't umask change execute permissions on files? When Linux calls functions to create files or directories, the predefined umask is used as a request parameter. You can obtain the final ACL for a child object from the overlap of the inherited ACL (parent to child) and the umask, as specified in the RFC 7530 standard. When you modify the group bits of a umask based on the standard, the permissions included in an ACL for each group must be less than or equal to the permissions defined in the group bits. However, this results in an invalid inheritance for groups. For example, if you want the subfile to inherit Group A:RWX but the predefined umask GROUPS:R is used as a request parameter, the ACE included in the ACL of Group A is then changed to Group A: R. In actual business scenarios, we recommend that you modify umasks only for ACLs that include the following principals: OWNER, GROUP, and EVERYONE. This prevents potential issues and ensures that the semantics are clear. To remove permissions from a group, we recommend that you remove the ACE that is associated with the group. You must manage the mappings between usernames or group names and user IDs (UIDs) or group IDs (GIDs) across multiple independent instances. Apsara File Storage NAS NFS uses IP security groups instead of usernames to authenticate users. When you configure NFSv4 ACLs, UIDs or GIDs that are included in ACEs are stored in Linux. When you print an ACL for an object in a shell, Linux automatically loads the /etc/passwd file and converts UIDs or GIDs into usernames or group names. You must manage the mappings between usernames or group names and UIDs or GIDs across multiple instances. You must make sure that each username is mapped to its corresponding UID, and each group name is mapped to its corresponding GID. You can print NFSv4 ACL by using extended attributes. Run the following commands:

```
getfattr -n system.nfs4_acl file
```

Sample command output:

```bash
# file: file
system.nfs4_acl=0sAAAABgAAAAAAAAAAABYBhwAAAAZPV05FUkAAAAAAAAAAAAAAABIAhwAAAAZHUk9VUEAAA AAAAAAAAAAAABIAhwAAAAlFVkVSWU9ORUAAAAAAAAAAAAAAAAAAAAEAAAAEMTAwMAAAAAAAAAALAAAAAwAAAAQx MDAwAAAAAAAAAEAAFgGQAAAABTEwMDAxAAAA
```

You can use tools such as cp to migrate NFSv4 ACLs. NAS allows you to migrate NFSv4 ACLs by using the cp, tar, and rsync tools. For more information, see How to preserve NFS v4 ACLs via extended attributes when copying file.

| cp --preserve=xattr file1 file2 |   |   |
|---|---|---|
| he | cp -ar dir1 dir2 | command co |

NFSv4 ACLs may fail to be migrated if the version of the rsync tool is earlier than 3.1.2. Example 1: Migrate the ACL of a file. a. Run the `nfs4_getfacl file1` command to view the ACL permissions of the file1 file.

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

Run the `nfs4_getfacl file` command to view the ACL permissions of the file.

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

In the interactions between ACLs and umasks, the EVERYONE principal is equivalent to the other class. When you modify the other class, the change also applies to the EVERYONE principal. This operation has a slight impact on the semantics of permissions. For example, the current umask is 177. After you run the `chmod o+r` command, all users that include the file owner and group members have the read permissions. This is because the read permissions are added to the ACE that includes the EVERYONE principal. If no change is applied to the default umask, the owner and group classes still do not have the read permissions after you run the chmod o+r command. If no change is applied to NFSv4 ACLs, the semantics of the other class of the file mode remain unchanged. If you modify an NFSv4 ACL, the semantics of the other class change to the semantics of the EVERYONE principal and the latest semantics remain unchanged. We recommend that you do not use umasks together with NFSv4 ACLs. Interactions between NFSv4 ACLs and POSIX ACLs are supported. You can mount NFSv3 file systems that have NFSv4 ACLs. These NFSv4 ACLs are then converted to POSIX ACLs. You can also mount NFSv4 file systems that have POSIX ACLs. These POSIX ACLs are then converted to NFSv4 ACLs. The semantics of POSIX ACLs are different from the semantics of NFSv4 ACLs. For example, the inheritance rules that apply to POSIX ACLs do not differentiate files or directories. NFSv4 ACLs have more permissions than POSIX ACLs. POSIX ACLs have only read, write, and execute permissions. To prevent potential issues, we recommend that you use either NFSv4 ACLs or POSIX ACLs. If you configure an NFSv4 ACL for the dir0 directory, the following permissions are required. Run the following commands:

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

Sample command output:

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

The number of NFSv4 ACLs is limited. By default, NAS supports a maximum of 100,000 different ACLs in each file system. Each ACL can contain a maximum of 500 ACEs. We recommend that you do not exceed the limits of ACLs or ACEs. Otherwise, more time and resources are consumed to verify permissions. Features of NAS POSIX ACLs Permissions that are specified for users of the other class apply to everyone. Everyone includes the owner, groups, and users that are related to each ACE. The other class is equal to the EVERYONE principal of an NFSv4 ACL. We recommend that you grant the least permissions to users of the other class. For example, the following ACL is configured for the myfile file. Although the ACE contains a user named alice who does not have the write permissions, the write permissions propagate to the ACE because the permissions are specified for users of the other class.

```bash
# file: myfile
# owner: root
# group: root
user::rwuser:alice:r-group::r-mask::r-other::rw-
```

Permissions that are configured by ACLs are not changed after you run the `chmod` command. We recommend that you do not modify the umask of a file to which a POSIX ACL is applied. You can configure permissions for the file by modifying the POSIX ACL. i. For example, an ACE that grants the players group the read and write permissions on the myfile file.

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

If you grant the execute permissions to the group class, the execute permissions also propagate to the player user. Example:

```bash
# file: myfile
# owner: root
# group: root
user::rwuser:player:r-x group::r-x mask::r-x other::r--
```

If you configure inheritable NFSv4 ACLs for directories that reside in NFSv3 file systems, these settings may not conform to the POSIX ACL standard. Inheritance rules that apply to files are different from inheritance rules that apply to directories in NFSv4 ACLs. The same inheritance rules apply to both files and directories in POSIX ACLs. To prevent potential issues, we recommend that you apply either NFS4 ACLs or POSIX ACLs to an NFS file system. The umask value cannot be modified. The umask of a POSIX ACL is generated by the permissions or operations of all users and groups. The umask has no practical meaning and cannot be changed. You must manage the mappings between usernames or group names and UIDs or GIDs across multiple instances. Apsara File Storage NAS NFS uses IP security groups instead of usernames to authenticate users. When you configure POSIX ACLs, UIDs or GIDs that are included in ACEs are stored in Linux. When you print an ACL for an object in a shell, Linux automatically loads the /etc/passwd file and converts UIDs or GIDs to actual usernames or group names. You must manage the mappings between usernames or group names and UIDs or GIDs across multiple instances. You must make sure that each username is mapped to its corresponding UID, and each group name is mapped to its corresponding GID. You can print POSIX ACL by using extended attributes. Run the following commands:

```
getfattr -n system.posix_acl_access file
```

Sample command output:

```bash
# file: file
system.posix_acl_access=0sAgAAAAEAAAD/////AgAFACAEAAAEAAAA/////xAABQD/////IAABAP////8=
```

You can use tools such as cp to migrate POSIX ACLs. NAS allows you to migrate POSIX ACLs by using the cp, tar, and rsync tools. For more information, see How to preserve NFS v4 ACLs via extended attributes when copying file. The following `cp --preserve=xattr file1 file2` command copies the ACL of file1 when it copies file1 to file2. The `cp -ar dir1 dir2` command copies the ACL of file1 when it copies file1 to file2. POSIX ACLs may fail to be migrated if the version of the rsync tool is earlier than 3.1.2. Example 1: Migrate the ACL permissions of the file. a. Run the `getfacl file1` command to view the ACL permissions of the file1 file.

```
user::--user:player:r-x group::--mask::r-x other::--x
```

b. Run the `cp --preserve=xattr file1 file2` command to copy the ACL of the file1 file to the ACL of the file2 file. Example 2: Migrate the ACL of a directory. a. Run the `getfacl file2` command to view the ACL permissions of the file2 file.

```bash
# file: file2
user::--user:player:r-x group::--mask::r-x other::--x
```

b. Run the `cp -ar dir1 dir2` command to copy the ACL of the dir1 directory to the dir2 directory. The number of POSIX ACLs is limited. By default, NAS supports a maximum of 100,000 different ACLs in each file system. Each ACL can contain a maximum of 500 ACEs. We recommend that you do not exceed the limits of ACLs or ACEs. Otherwise, more time and resources are consumed to verify permissions. FAQ Why are deny ACEs not supported? The position of an ACE that resides in an ACL is important. The sequence for ACEs that reside in an NFSv4 ACL is random. A deny ACE may be placed in any position of an NFSv4 ACL. For example, an ACL contains two ACEs: A::Alice:r and D::Alice:r. The position of the ACEs determines whether the user named Alice has the write permissions. When you configure an ACL, you must consider the position of each ACE. The number of ACEs in an ACL has a sharp increase. The ACEs in an ACL may be difficult to combine and deduplicate because it is not mandatory to sequence ACEs. The number of ACEs may increase up to tens or hundreds over a long period of time. To manage the final permissions that are produced by these ACEs, you need to check each ACE. The check process is strenuous and time-consuming. The interactions between the umask and ACLs become more complex after deny ACEs are applied. This is because deny features do not exist in the umask. If deny ACEs are available, you may need to add several ACEs to an ACL when the umask is changed. For example, if you change the umask to -rw-rw-rw, you need to add the following ACEs to the ACL. You must add the ACEs in sequence at the beginning of the ACL.

```
A::OWNER@:rw D::OWNER@:x A::GROUP@:rw D::GROUP@:x A::EVERYONE@:rw D::EVERYONE@:x
```

If deny ACEs are unavailable, you can sort and deduplicate ACEs while the ACEs for the everyone class and the other class are not differentiated. If you change the umask, you can modify ACLs by changing ACEs for the owner, group, and everyone classes into the following content:

```
A::OWNER@:rw A::GROUP@:rw A::EVERYONE@:rw
```

Conversions between NFSv4 ACLs and POSIX ACLs are not supported. POSIX ACLs do not support deny ACEs. If deny ACEs are included in an NFSv4 ACL, you cannot convert the ACL to a POSIX ACL.

### Use POSIX ACLs to control

access This topic describes how to configure Portable Operating System Interface (POSIX) access control lists (ACLs) to control access to the files and directories in an NFSv3 file system. Prerequisites An NFSv3 file system is mounted. For more information, see Mount an NFS file system. Description Before you configure POSIX ACLs, we recommend that you get familiar with specific commands. The following table describes the commands.

| Command | Description |
|---|---|
| getfacl <filename> | Queries the ACL that applies to the specified file. |
| setfacl -m g::w <filename> | Adds an access control entry (ACE) that grants the write permissions on a specified file to the GROUP@ principal. |
| setfacl -m u:player:w <filename> | Grants the player user the write permissions. |
| setfacl -m g:players:rwx <filename> | Grants the players group the read, write, and execute permissions. |
| setfacl -x g:players <filename> | Revokes permissions from the players group |

| t | User Guide·Directory-level ACLs tha grant the read and write access | Apsara File Storage NA | S |
|---|---|---|---|

| Command | Description |
|---|---|
| getfacl file1 \| setfacl --set-file=- file2 | Copies the ACL for the file1 file to the file2 file. |
| setfacl -b file1 | Removes all extended ACEs from the file1 file. The base ACEs of the owner, group, and others are retained. |
| setfacl -k file1 | Removes all default ACEs from the file1 file. |
| nfs4 setfacl -R -m g:players:rw dir _ | Grants the players group the read and write permissions on the files and subdirectories in the dir directory. |
| setfacl -d -m g:players:rw dir1 | Grants the players group the read and write permissions on the new files and subdirectories in the dir1 directory. |

Procedure To control access to files and directories by configuring NFS ACLs, perform the following steps:
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

Run the `sudo getfacl dir0` command to verify the configuration.

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

Run the `sudo su player -c 'cat dir0/file'` command to view the content of the dir0/fi le file. Run the `sudo su player -c 'echo 456 >> dir0/file'` command to append data to the dir0/file file.

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

iii. Run the following commands to verify that the anonym user does not have permissions on specific resources: Run the `sudo su anonym -c 'ls dir0'` command to view the files in the dir0 directory. If the output is similar to the following information, the anonym user does not have permissions on the dir0 directory.

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

What to do next You can use the following method to revoke permissions from a user. If you want to use NFSv4 ACLs, we recommend that you add each user to groups. This allows you to configure permissions for a group rather than a separate user. To revoke permissions on an object from a user, you can remove the user from the group that is granted permissions on the object. For example, run the following commands to remove the admini user from the adminis group and add the user to the adminis2 group:
1. Run the `sudo groupadd adminis2` command to create a group named adminis2.
2. Run the `sudo usermod -g adminis2 admini` command to remove the admini user from the
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

### Use NFSv4 ACLs to control

access This topic describes how to configure NFSv4 access control lists (ACLs) and use the ACLs to control access to the files or directories in an NFSv4 file system. Prerequisites An NFSv4 file system is mounted. For more information, see Mount an NFS file system. Context You can mount an NFSv4 file system on a Linux Elastic Compute Service (ECS) instance and install the Linux-specific nfs4-acl-tools tool on the instance. After the tool is installed, you can use the standard nfs4_getfacl and nfs4_setfacl tools to configure NFSv4 ACLs. Description Before you configure NFSv4 ACLs, we recommend that you get familiar with specific commands. The following table describes the commands.

| Command |   | Description |
|---|---|---|
| nfs4 getfacl <filename> _ |   | Views the ACL that applies to a specified file |
| nfs4 setfacl -a A::GROUP@:W <filename> _ |   | Adds an access control entry (ACE) that grants the write permissions on a specified file to the GROUP@ principal. |
| nfs4 setfacl -a A::1000:W <filename> _ |   | Adds an ACE that grants the write permissions on a specified file to a user principal named 1000. |
| nfs4 setfacl -a A:g:10001:W <filename> _ |   | Adds an ACE that grants the write permissions on a specified file to a user principal named 10001. |
| nfs4 setfacl -e <filename> _ |   | Modifies an ACL in interactive mode. |
| nfs4 getfacl <filename> > saved acl.txt _ _ |   | Saves a list of permissions on a specified file as a TXT file. |
| nfs4 setfacl -S saved acl.txt <filename> _ _ |   | Configures permissions on a specified file by using a TXT file that includes a list of permissions. |
| nfs4 setfacl -m A::1001:rwaxTNcCy _ A::1001:rxtcy file1 |   | Modifies an ACE that applies to the file1 file. |
| nfs4 getfacl file1 \| nfs4 setfacl -S - _ _ file2 |   | Copies the ACL for the file1 file to the file2 file. |
| nfs4 getfacl file1 \| grep @ \| nfs4 setfacl _ _ -S - file1 |   | Removes all ACEs that apply to the file1 file except for ACEs that include the following principals: OWNER@, GROUP@, and EVERYONE@. |
| nfs4 setfacl -R -a A:g:10001:rW dir _ |   | Adds an ACE that grants the read and write permissions on the files and subdirectories in the dir directory to a group principal named 10001. |
| find dir -type f -exec sh -c 'for ace in |   |   |
|   | find dir -type f -exec sh -c 'for ace in | Removes ACEs that grant permissions on the files in |
| $(nfs4 getfacl \{} \| grep "^A.*\:1005\:"); _ |   | Removes ACEs that grant permissions o |
|   |   | the dir directory to a user principal name |
| do nfs4 setfacl -x $ace \{}; done' \; _ |   |   |

|   | nfs4 setfacl -m A::1001:rwaxTNcCy _ | Modifies |
|---|---|---|
| A::1001:rxtcy file1 |   |   |

|   | nfs4 getfacl file1 \| nfs4 setfacl -S - _ _ |   |
|---|---|---|
| file2 |   |   |

|   | nfs4 getfacl file1 \| grep @ \| nfs4 setfacl _ _ | Removes for ACEs t |
|---|---|---|
| -S - file1 |   |   |

| nfs4 setfacl -a A:fdg:10001:rW dir1 _ | Adds an ACE that grants the read and write permissions on new files and subdirectories in the dir1 directory to a group principal named 10001. |
|---|---|
| nfs4 setfacl -a A:fg:10001:rx dir1 _ | Adds an ACE that grants the read, write, and execute permissions on all new files in the dir1 directory to a group principal named 10001. |

Procedure To control access to files and directories by configuring NFSv4 ACLs, perform the following steps.
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
Run the following commands to complete the operations: Create a directory named dir0 and add ACEs that grant the read-only permissions on all files in the dir0 directory to the players group, grant the read, write, and execute permissions to the adminis group, and do not grant permissions to other users.

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

Run the `sudo su player -c 'echo 456 >> dir0/file'` command. If the output is similar to the following information, the player user does not have the write permissions on the dir0/fil e file.

```
bash: dir0/file: Permission denied
```

Run the `sudo su player -c 'cat dir0/file'` command. If the output is similar to the following information, the player user does not have the permissions to view the content of the dir0/file file. Run the `sudo su player -c 'nfs4_getfacl dir0/file'` command to view the permissions that the player user has on the dir0/file file.

```
A::OWNER@:tTnNcCy A::GROUP@:tncy A::EVERYONE@:tncy A:g:19064:rxtncy A:g:19065:rwaxtTnNcCy
```

iii. Run the following command to verify that the anonym user does not have permissions on specific resources: Run the `sudo su anonym -c 'ls dir0'` command. If the output is similar to the following information, the anonym user does not have permissions on the dir0 directory.

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

What to do next You can use the following method to revoke permissions from a user. If you want to use NFSv4 ACLs, we recommend that you add each user to groups. This allows you to configure permissions for a group rather than a separate user. To revoke permissions on an object from a user, you can remove the user from the group that is granted permissions on the object. For example, you can run the following commands to remove the admini user from the adminis group and add the user to the adminis2 group:
1. Run the `sudo groupadd adminis2` command to create a group named adminis2.
2. Run the `sudo usermod -g adminis2 admini` command to remove the admini user from the
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
