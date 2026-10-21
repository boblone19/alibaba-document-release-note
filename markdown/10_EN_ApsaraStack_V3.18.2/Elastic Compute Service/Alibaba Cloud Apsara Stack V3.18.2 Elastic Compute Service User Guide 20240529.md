---
title: "Alibaba Cloud Apsara Stack V3.18.2 Elastic Compute Service User Guide 20240529"
product_version: "V3.18.2"
doc_version: "20240529"
pdf_pages: 310
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Elastic Compute Service User Guide 20240529.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/ECS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Elastic%20Compute%20Service%20User%20Guide%2020240529.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Elastic Compute Service User Guide 20240529

## Table of Contents

- 1 What is ECS?
  - 1.1 Overview
  - 1.2 Instance lifecycle
- 2 Instructions
  - 2.1 Suggestions
  - 2.2 Limits
  - 2.3 Usage notes on Linux operating systems
  - 2.4 Usage notes on Windows operating systems
  - 2.5 Notice on defense against DDoS attacks
- 3 Quick start
  - 3.1 Overview
  - 3.2 Log on to the ECS console
  - 3.3 Create a security group
  - 3.4 Create an instance by using the wizard
  - 3.5 Connect to an instance
    - 3.5.1 Overview
    - 3.5.2 Connect to a Linux instance by using SSH commands in Linux or Mac OS X
    - 3.5.3 Connect to a Linux instance by using a remote connection tool in Windows
    - 3.5.4 Connect to a Windows instance from a Windows computer by using Remote Desktop
    - 3.5.5 Connect to an instance by using a VNC management terminal
- 4 Instances
  - 4.1 Overview
  - 4.2 Create an instance by using the wizard
  - 4.3 Connect to an instance
    - 4.3.1 Overview
    - 4.3.2 Connect to a Linux instance by using SSH commands in Linux or Mac OS X
    - 4.3.3 Connect to a Linux instance by using a remote connection tool in Windows
    - 4.3.4 Connect to a Windows instance from a Windows computer by using Remote Desktop
    - 4.3.5 Install the certificate for VNC in Windows
    - 4.3.6 Connect to an instance by using a VNC management terminal
  - 4.4 Manage instance status
    - 4.4.1 Stop an instance
    - 4.4.2 Start an instance
    - 4.4.3 Restart an instance
    - 4.4.4 Delete an instance
  - 4.5 Manage instance attributes
    - 4.5.1 View instance information
    - 4.5.2 Modify the attributes of an instance
    - 4.5.3 Reset the logon password of an instance
    - 4.5.4 Change the VNC password
    - 4.5.5 Enable and disable release protection for instances
    - 4.5.6 Instance user data
  - 4.6 Manage the instance recycle bin
    - 4.6.1 Set the retention period
    - 4.6.2 Restore an instance
    - 4.6.3 Permanently delete instances
  - 4.7 Change the instance type
    - 4.7.1 Upgrade or downgrade the instance type of an instance
    - 4.7.2 Perform a hot configuration change to change the instance type of an instance
  - 4.8 Replace the operating system of an instance
  - 4.9 View the monitoring information of an instance
  - 4.10 Add an instance to a security group
  - 4.11 Change the private IP address of an instance
  - 4.12 Assign an IPv6 address to an instance
  - 4.13 Export a list of instances
  - 4.14 Manage NVIDIA drivers
    - 4.14.1 Installation guideline for NVIDIA drivers
    - 4.14.2 Install a GPU driver
      - 4.14.2.1 Install a GPU driver on a GPU-accelerated compute-optimized Linux instance
      - 4.14.2.2 Install a GPU driver on a GPU-accelerated compute-optimized Windows instance
    - 4.14.3 Install a GRID driver
      - 4.14.3.1 Install a GRID driver on a vGPU-accelerated Linux instance
      - 4.14.3.2 Install a GRID driver on a GPU-accelerated Windows instance
    - 4.14.4 Uninstall an NVIDIA driver
      - 4.14.4.1 Uninstall a GPU driver
      - 4.14.4.2 Uninstall a GRID driver
    - 4.14.5 Update an NVIDIA driver
- 5 Super computer clusters
  - 5.1 Overview
  - 5.2 Create an SCC
  - 5.3 Add nodes to an SCC
  - 5.4 View the details of a super computing cluster
  - 5.5 Modify the attributes of an SCC
  - 5.6 Delete an SCC
- 6 Disks
  - 6.1 Overview
  - 6.2 Create a disk
  - 6.3 Attach a data disk
  - 6.4 Partition and format disks
    - 6.4.1 Format a data disk for a Linux instance
    - 6.4.2 Format a data disk on a Windows ECS instance
  - 6.5 View disk details
  - 6.6 Roll back a disk by using a snapshot
  - 6.7 Change the category of a disk
  - 6.8 Modify the properties of a disk
  - 6.9 Change the name and description of a disk
  - 6.10 Resize a disk
  - 6.11 Support the NVMe protocol and multi-attach feature
    - 6.11.1 Overview of disks that support NVMe
    - 6.11.2 Enable the multi-attach feature
  - 6.12 Encrypt a disk
    - 6.12.1 Overview
    - 6.12.2 Encrypt a system disk
    - 6.12.3 Encrypt a data disk
  - 6.13 Re-initialize disks
    - 6.13.1 Re-initialize a system disk
    - 6.13.2 Re-initialize a data disk
  - 6.14 Detach a data disk
  - 6.15 Release a data disk
- 7 Images
  - 7.1 Overview
  - 7.2 View instances that use a specific image
  - 7.3 Public images
    - 7.3.1 Overview
    - 7.3.2 Find a public image
  - 7.4 Custom images
    - 7.4.1 Overview of custom images
    - 7.4.2 Create a custom image
    - 7.4.3 Modify the attributes of a custom image
    - 7.4.4 Find a custom image
    - 7.4.5 Share a custom image
      - 7.4.5.1 Share a custom image
      - 7.4.5.2 Modify the sharing scope of a custom image
    - 7.4.6 Encrypt a custom image
    - 7.4.7 Set the boot mode of a custom image
    - 7.4.8 Import custom images
      - 7.4.8.1 Limits on importing images
      - 7.4.8.2 Convert the format of an image
      - 7.4.8.3 Import an image
    - 7.4.9 Export a custom image
    - 7.4.10 Delete a custom image
  - 7.5 Shared custom images
    - 7.5.1 Overview
    - 7.5.2 Find a shared custom image
  - 7.6 Globally shared images
    - 7.6.1 Overview
    - 7.6.2 Find a globally shared image
- 8 Snapshots
  - 8.1 Overview
  - 8.2 Disk snapshots
    - 8.2.1 Create snapshots
    - 8.2.2 View snapshot details
    - 8.2.3 Roll back a disk by using a snapshot
    - 8.2.4 Create a custom image from a snapshot
    - 8.2.5 Delete snapshots
  - 8.3 Use snapshot-consistent groups
    - 8.3.1 Create a snapshot-consistent group
    - 8.3.2 Roll back disks by using a snapshot-consistent group
    - 8.3.3 Delete a snapshot-consistent group
  - 8.4 Use automatic snapshots
    - 8.4.1 Create an automatic snapshot policy
    - 8.4.2 View automatic snapshot policies
    - 8.4.3 Modify an automatic snapshot policy
    - 8.4.4 Apply or cancel an automatic snapshot policy
    - 8.4.5 Delete an automatic snapshot policy
- 9 Security groups
  - 9.1 Overview
  - 9.2 Create a security group
  - 9.3 Add a security group rule
  - 9.4 Add ECS instances to a security group
  - 9.5 Manage security groups
    - 9.5.1 View security groups
    - 9.5.2 Modify a security group
    - 9.5.3 Remove instances from a security group
    - 9.5.4 Delete a security group
  - 9.6 Manage security group rules
    - 9.6.1 Modify security group rules
    - 9.6.2 Clone a security group rule
    - 9.6.3 Export security group rules
    - 9.6.4 Import security group rules
    - 9.6.5 Delete a security group rule
- 10 RAM role management
  - 10.1 Attach an instance RAM role to an ECS instance
  - 10.2 Replace the instance RAM role of an ECS instance
  - 10.3 Detach an instance RAM role from an ECS instance
- 11 Elastic Network Interfaces
  - 11.1 Overview
  - 11.2 Create an ENI
  - 11.3 Bind a secondary ENI to an instance
  - 11.4 Configure a secondary ENI
  - 11.5 View ENIs
  - 11.6 Modify the attributes of a secondary ENI
  - 11.7 Unbind a secondary ENI from an ECS instance
  - 11.8 Delete a secondary ENI
- 12 Key pairs
  - 12.1 Overview
  - 12.2 Create a key pair
  - 12.3 Import a key pair
  - 12.4 Bind a key pair to an instance
  - 12.5 Unbind SSH key pairs
  - 12.6 Add or replace a key pair
  - 12.7 View public key information
- 13 Deployment sets
  - 13.1 Overview
  - 13.2 Create a deployment set
  - 13.3 View deployment sets
  - 13.4 Change the deployment set of an instance
  - 13.5 Modify a deployment set
  - 13.6 Delete a deployment set
- 14 Monitoring & maintenance
  - 14.1 Configure monitoring thresholds for organizations
  - 14.2 View the list of monitored organizations
  - 14.3 Configure monitoring metric thresholds for instances
  - 14.4 View the list of monitored instances
  - 14.5 Reclaim instance resources
- 15 Cloud Assistant
  - 15.1 Overview
  - 15.2 Configure the Cloud Assistant client
    - 15.2.1 Install the Cloud Assistant client
    - 15.2.2 Configure DNS resolution for Cloud Assistant
    - 15.2.3 Start or stop the Cloud Assistant client
  - 15.3 Use Cloud Assistant
    - 15.3.1 Create a command
    - 15.3.2 Run a command
    - 15.3.3 Upload files to ECS instances
    - 15.3.4 Clone a command
    - 15.3.5 Delete a command
  - 15.4 Cron expression
- 16 View asynchronous tasks
- 17 Dedicated hosts
  - 17.1 Create a dedicated host
  - 17.2 Share a host
  - 17.3 Create a host group
  - 17.4 Create an ECS instance on a host
  - 17.5 Add dedicated hosts to a host group
- 18 Install FTP software
  - 18.1 Overview
  - 18.2 Install and configure vsftp in CentOS
  - 18.3 Install vsftp in Ubuntu or Debian
  - 18.4 Build an FTP site in Windows Server 2008
  - 18.5 Build an FTP site in Windows Server 2012

## 1 What is ECS?

### 1.1 Overview

Elastic Compute Service (ECS) is a type of computing service that features elastic processingcapabilities. Compared with physical servers, ECS can be more efficientlymanaged and is more user-friendly. You can create instances, resize disks, and add or release any number of ECS instances at any time based on your business needs. An ECS instance is a virtual computing environment that contains the most basic components of computers such as the CPU, memory, and storage. Users perform operations on ECS instances. Instances are core components of ECS, and operations can be performed on instances by using the ECS console. Other resources such as block storage, images, and snapshots can only be used after they are integrated into ECS instances. For more information, see ECS components. Figure 1. ECS components

### 1.2 Instance lifecycle

The lifecycle of an ECS instance begins when the instance is created and ends when the instance is released. This topic describes the instance states in the ECS console as well as state attributes and their corresponding instance states in API responses. The following table describes the instance states in the ECS console and their corresponding instance states in API responses.

| State | State attribute | Description | State in an API response |
|---|---|---|---|

| Instance being created | Intermediate | The instance is being created and waiting to start. If an instance remains in this state for an extended period of time, an exception has occurred. | Pending |
|---|---|---|---|
| Starting | Intermediate | When you start or restart an instance by using the ECS console or by calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Starting state for an extended period of time, an exception has occurred. | Starting |
| Running | Stable | While an instance is in the Running state, the instance can function normally and can accommodate your business needs. | Running |
| Stopping | Intermediate | When you stop an instance by using the ECS console or by calling an API operation, the instance enters this state before it enters the Stopped state. If an instance remains in the Stopping state for an extended period of time, an exception has occurred. | Stopping |
| Stopped | Stable | An instance enters this state when it is stopped. Instances in the Stopped state cannot provide external services. | Stopped |
| Reinitializin g | Intermediate | When you re-initialize the system disk or a data disk of an instance by using the ECS console or calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Reinitializing state for an extended period of time, an exception has occurred. | Stopped |
| Changing system disk | Intermediate | When you replace the system disk of an instance by using the ECS console or by calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Changing system disk state for an extended period of time, an exception has occurred. | Stopped |

The following figure shows the transitions between instance states in API responses.

## 2 Instructions

### 2.1 Suggestions

Consider the following suggestions to use Elastic Compute Service (ECS) more efficiently: ECS instances with 4 GiB or higher memory must use a 64-bit operating system. A 32-bit operating system can be used for instances with a maximum of 4 GiB of memory. A 32-bit Windows operating system can support up to 4 CPU cores. To ensure service continuity and prevent service unavailability due to failovers, we recommend that you configure service applications to start automatically on system startup.

### 2.2 Limits

Before you use Elastic Compute Service (ECS) instances, familiarize yourself with the following limits.

**General limits**

Windows operating systems support up to 64 vCPUs in instance specifications. You cannot install virtualization software such as VMware on instances or use virtualization software to re-virtualize instances. ECS does not support sound card applications. Only GPU-accelerated instances support virtual sound cards. External hardware devices, such as hardware dongles, USB flash drives, external hard disks, and bank U keys, cannot be directly connected to ECS instances. ECS does not support multicast protocols. We recommend that you use unicast protocols instead.

**Instance type limits**

**Elastic Block Storage (EBS) limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of system disks on a single instance | 1 | N/A |
| Maximum number of data disks on a single instance | 64 Note You can attach up to 16 data disks to an instance when you create the instance. If the instance requires additional data disks, attach more data disks after the instance is created. | N/A |

| Capacity of a single system disk | Windows Server: 40 GiB to 500 GiB Red Hat: 40 GiB to 500 GiB CoreOS and FreeBSD: 30 GiB to 500 GiB Other Linux distributions: 20 GiB to 500 GiB | N/A |
|---|---|---|
| Capacity of a single data disk | 20 GB~32,768 GB | N/A |
| Mount points of system disks | /dev/vda | N/A |
| Mount points of data disks | /dev/vd[b-z] | N/A |

**Snapshot limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of snapshots in an account | 100,000 | N/A |
| Maximum number of manual snapshots that can be retained for a single disk | 256 | N/A |
| Maximum number of automatic snapshots that can be retained for a single disk | 1000 | N/A |
| Maximum number of automatic snapshot policies that can be retained per region in an account | 100 | N/A |

**Image limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of images in an account | 100,000 | N/A |
| Maximum number of users with whom a single image can be shared | 50 | N/A |
| Support of instance types for images | Instance types that have 4 GiB or more of memory do not support 32-bit images. | N/A |

**SSH key pair limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of SSH key pairs per region in an account | 500 | N/A |

| Instance types that support SSH key pairs | Non-I/O optimized instances of Generation I instance families do not support SSH key pairs. | N/A |
|---|---|---|
| Images that support SSH key pairs | Linux images only. | N/A |

**Security group limits**

| Item | Requirement or limit on basic security groups | Requirement or limit on advanced security groups |
|---|---|---|
| Maximum number of security groups in an account | 100,000 | The requirement is the same as that on basic security groups. |
| Maximum number of ECS instances that can be contained in a security group | This limit varies based on the number of private IP addresses that can be contained in the security group. | No limit. |
| Maximum number of security groups to which an ECS instance can belong | 5 You can submit a ticket to raise the limit to 10 or 16 security groups. | The requirement is the same as that on basic security groups. |
| Maximum number of security groups to which an elastic network interface (ENI) of an ECS instance can belong |   |   |
| Maximum number of inbound and outbound rules in a security group | 200 | The requirement is the same as that on basic security groups. |
| Maximum number of inbound and outbound rules in all security groups to which an ENI belongs | 1,000 | The requirement is the same as that on basic security groups. |
| Maximum number of private IP addresses that can be contained in a security group of the Virtual Private Cloud (VPC) type | 2,000 | 65,536 |

**Deployment set limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of deployment sets in an account | 640 | N/A |
| Maximum number of instances that can be contained in a single deployment set | Up to 20 instances can be contained in a deployment set within a single zone. The maximum number of instances that can be contained in a deployment set within a region is calculated by using the following formula: 20 × Number of zones in the region. | N/A |

**Cloud Assistant limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of Cloud Assistant commands in an account | No limit. | N/A |
| Retention period of a Cloud Assistant command execution record | 28 days | N/A |
| Maximum number of Cloud Assistant command execution records that can be retained | 100000 | N/A |
| Maximum number of the activation codes that can be used to register Cloud Assistant managed instances. | 5000 | N/A |

**ENI limits**

| Item | Requirement or limit | Adjustable |
|---|---|---|
| Maximum number of secondary ENIs that can be created | A limited number of ENIs can be created per region in an account. The ENI quota is displayed on the Quota Overview page of the Apsara Uni-manager Management Console. | N/A |

**Instance family ga1**

To create a ga1 instance, use one of the following images for which drivers are pre-installed: Ubuntu 16.04 for which an AMD GPU driver is pre-installed Windows Server 2016 English edition for which an AMD GPU driver is pre-installed Windows Server 2008 R2 English edition for which an AMD GPU driver is pre-installed Take note of the following items: A ga1 instance uses an optimized driver provided by Alibaba Cloud and AMD. The driver is installed in images provided by Alibaba Cloud and is currently unavailable for download. If the GPU driver malfunctions due to the removal of related components, you must replace the system disk to restore GPU-related features.

> **Note:** This operation results in data loss.

If the driver malfunctions when an improper image is selected during ga1 instance creation, you must replace the system disk to select an image for which an AMD GPU driver is preinstalled. For Windows Server 2008 or earlier, you cannot connect to instances by using Virtual Network Computing (VNC) after the GPU driver takes effect. VNC does not respond and a black screen appears or the system is stuck on the splash screen. You can use other methods such as Remote Desktop Protocol (RDP) to access the system. RDP does not support DirectX, OpenGL, or other related applications. You must install the VNC service and client, or use other supported protocols such as PCOIP and XenDesktop HDX 3D.

**Instance families gn4, gn5i, and gn5**

Bandwidth: If you use a Windows Server 2008 R2 image for a gn4 instance, you cannot use the Connect to VNC feature in the ECS console to connect to the instance after the installed GPU driver takes effect. You must set the bandwidth to a non-zero value or associate an elastic IP address (EIP) with the created instance. Image: If an NVIDIA GPU driver does not need to be pre-installed, you can select any image to create an instance based on your business requirements and then install an NVIDIA GPU driver on the instance. For more information, see Installation guideline for NVIDIA drivers.

### 2.3 Usage notes on Linux operating systems

**operating systems**

Before you use Linux operating systems, take note of the following items: Do not modify the content of the default /etc/issue files in Linux instances. If you modify the content of the default /etc/issue file on a Linux instance and use the instance to create a custom image, the operating system distribution contained in the image cannot be recognized. As a result, Linux instances that are created from the image cannot start. Do not arbitrarily modify the permissions of each directory on the partition in which the root directory is located, especially the permissions of the /etc, /sbin, /bin, /boot, /dev, /usr, and /lib directories. If you incorrectly modify the permissions, errors may occur. Do not rename, delete, or disable the root account. Do not compile the Linux kernel or perform operations on the kernel. For example, if you upgrade the Linux kernel, the following issues may occur: The core components of the operating system greatly change, which may cause risks and potential issues. You must assess the upgrade operation and resolve the issues. If you upgrade the Linux kernel to a version that is not supported in the Yellowdog Updater Modified (YUM) repository for the operating system, the following common risks and issues may occur: System instability: The new kernel may cause the operating system to be unstable. Before you upgrade the kernel, fully assess and validate the upgrade operation. Software incompatibility: Specific software that runs as expected on the original kernel may not run as expected on the new kernel. Update the software or modify the software configurations. Affected performance and functionality: Default kernel options and features may change during the upgrade, which may affect system performance and functionality. Security vulnerabilities: The new kernel may contain unknown security vulnerabilities. Loss of support: If you use a non-official kernel, you may be unable to obtain some official technical support or relevant kernel security updates. Difficulty in kernel rollback: If issues occur after the upgrade, the kernel may be difficult to roll back to the original version. If your ECS instance is in the production environment, exercise caution when you upgrade the Linux kernel. Do not enable SELinux on Linux operating systems except for CentOS and Red Hat. Do not arbitrarily change the media access control (MAC) addresses of network interface controllers (NICs). We recommend that you do not use swap partitions. Do not enable the NetWorkManager service. The service conflicts with the internal network service of the system and causes network errors.

### 2.4 Usage notes on Windows operating systems

**operating systems**

Before you use Windows operating systems, take note of the following items: If a Windows instance uses local disks as data disks, the instance is at risk of data loss. If you are unsure about the reliability of the data architecture, we recommend that you use cloud disks to create Windows instances. Do not close the built-in shutdownmon.exe process. Otherwise, the server may require an extended period of time to restart. Do not rename, delete, or disable the Administrator account. Otherwise, the server usage may be affected. We recommend that you do not use virtual memory. Do not uninstall PV drivers. Do not arbitrarily change the media access control (MAC) addresses of network interface controllers (NICs). If you change the name of your computer, you must synchronously change the following key values in the registry. If you do not synchronously change the key values in the registry, the change does not take effect, which may cause the installation of specific thirdparty programs to fail.

```
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ActiveComputerName HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
```

### 2.5 Notice on defense against DDoS attacks

**DDoS attacks**

You need to purchase Anti-DDoS Pro to defend against DDoS attacks. For more information, see **Apsara Stack Security Product Introduction** .

## 3 Quick start

### 3.1 Overview

This topic describes how to create and connect to an Elastic Compute Service (ECS) instance. Perform the following operations: A security group acts as a virtual firewall to control inbound and outbound traffic for ECS instances. Each ECS instance must belong to at least one security group. When you create an instance, you must select a security group for the instance. An ECS instance is a virtual server that contains the basic components of a server, such as CPUs, memory, an operating system, network configurations, and disks. After a security group is created, you can select an instance type based on your business requirements to create instances in the security group. Select a method to connect to an instance based on the network configurations and operating system of the instance and the operating system of your computer. After you connect to the instance, you can perform operations on it such as installing applications.

### 3.2 Log on to the ECS console

This topic describes how to log on to the Elastic Compute Service (ECS) console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**You log on to the Apsara Uni-manager Management Console for the first time**

**after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see **Manage MFA** in **Apsara** **Uni-manager Management Console User Guide**.

5. In the top navigation bar, choose **Products > Elastic Computing > Elastic Compute**
**Service**.

### 3.3 Create a security group

Security groups are an important means to implement network security isolation. They control network traffic to or from one or more Elastic Compute Service (ECS) instances.

**Background information**

Security groups determine whether instances in the same VPC, region, and account can communicate with each other. By default, if the instances belong to the same security group, they can communicate with each other over the internal network. If the instances belong to different security groups, you can allow mutual access between the security groups to allow the instances to communicate with each other over the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Security Group**.
5. Configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization | Yes | Select an organization in which to create the security group. Make sure that the security group and the VPC belong to the same organization. |
|   | Resource Set | Yes | Select a resource set in which to create the security group. Make sure that the security group and the VPC belong to the same resource set. |
|   | Region | Yes | Select a region in which to create the security group. Make sure that the security group and VPC reside within the same region. |
|   | Zone | Yes | Select a zone in which to create the security group. |
| Basic Configuration s | Sharing Scope | Yes | Select the scope for which to share the security group. Valid values: Current Resource Set, Current Organization and Subordinate Organizations, and Current Organization. |
|   | VPC | Yes | Select an existing VPC or click Create VPC to create a VPC. After you create a VPC, you can go back to the Create Security Group page and click the icon to view the most recent list of VPCs. For information about the parameters that are used to create a VPC, see the Create a VPC topic in VPC User Guide. |
|   | Security group name | Yes | Enter a name for the security group. The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, underscores ( ), hyphens (-), and colons (:). It _ cannot start with http:// or https:// . |
|   | Description | No | Enter a description for the security group for easy management. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ periods (.), commas (,), and colons (:). It must start with a letter and cannot start with http:// or https:// . |

6. Click **Submit**.
After the security group is created, it is displayed on the Security Groups page.

**What to do next**

After the security group is created, it contains no security group rules. You can add security group rules to allow or deny access to or from the Internet or internal network for ECS instances within the security group. For more information, see Add a security group rule. Each ECS instance must belong to at least one security group. You can add an instance to one or more security groups. For more information, see Add ECS instances to a security group.

### 3.4 Create an instance by using the wizard

**the wizard**

An Elastic Compute Service (ECS) instance is a virtual machine that contains basic components, such as the CPU, memory, operating system, network settings, and disks.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For more information, see **VPCs**
**and vSwitches > VPC management > Create a VPC** and **VPCs and vSwitches >**
**vSwitch management > Create a vSwitch** in the VPC User Guide in the Apsara Stack
Documentation Center. If you want to assign an IPv6 address to the instance that you want to create, make sure that the VPC and vSwitch are associated with IPv6 CIDR blocks. For more information, see
**Quick start > Create an IPv6 VPC** in the VPC User Guide in the Apsara Stack
Documentation Center. A security group is created. For more information, see Create a security group.

**Background information**

Specific limits apply when you create GPU-accelerated instances. For more information, see Limits.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance**.
5. Configure the basic settings.
In the Basic Settings step, configure the basic attributes and the basic resources that are required to create an instance. The basic attributes include the organization, resource set, region, and zone. The basic resources include the instance type, image, and storage. After you complete the basic settings, click **Next**. You can click **Configuration Preview** in the lower part of the page to view the instance information. The information includes the settings that you configured and the settings that you need to specify. i. Configure the basic attributes of the instance. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization for which you want to create the instance. |
| Resource Set | Yes | Select the resource set in which you want to create the instance. |
| Region | Yes | Select the region in which you want to create the instance. |
| Zone | Yes | Select the zone in which you want to create the instance. Zones are physical locations in the same region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |

ii. Configure the instance specifications, such as the instance family and instance type. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Support Hot Configuration Changes | No | If you turn on the switch, you can change the instance type without the need to stop the instance. For more information, see Perform a hot configuration change on an instance to change the instance type. |
| Filter | No | Specify the number of vCPUs, memory size, or instance type name based on your business requirements to search for instance types. |

| Hardware Manufacturers | Yes | Select a hardware manufacturer. Valid values: Intel/X86 Hygon/X86 Kunpeng/ARM Phytium/ARM Yitian/ARM SW Others Note The actual hardware manufacturers that are supported are displayed on the Create Instance page in the ECS console. |
|---|---|---|
| Category | Yes | Select an instance category. Valid values: Dedicated Shared Local SSD Local HDD Super Computing Cluster ECS Bare Metal Instance Others Note The actual instance types that are supported are displayed on the Create Instance page in the ECS console. |

| Specification | Yes | Select an instance type. The instance type list consists of multiple columns, including Instance Family, Instance Type, Instance Family Level, CPU Type, Memory, and Internal Bandwidth. Select an instance type based on your business requirements. Note For more information about instance families and instance types, see the Introduction to Instance Famil ies and Instance Types in the Apsara Stack ECS documentation. Instance types that have specific vCPU and memory combinations do not support Windows Server images. For more information, see Limits. Important If you create a GPU-accelerated instance, install a GPU driver on the instance based on the operating system of the instance. Except that you must install GPU drivers on GPU- accelerated instances, you can manage GPU- accelerated instances in the same manner as you manage non-GPU-accelerated instances. For information about how to install GPU drivers on NVIDIA GPU-accelerated instances, see Installation guideline for NVIDIA drivers. For information about how to install GPU drivers on instances that are equipped with GPUs from other manufacturers, see the official documents of the manufacturers. If you create an instance of a Super Computing Cluster (SCC) instance type, you must configure the Super Computing Cluster parameter, instead of the Deployment Set parameter. When you select an SCC instance type, the Deployment Set parameter is not displayed on the Create Instance page. The VPC and Security Groups parameters may be affected by the VPC ID and security group ID of the SCC. For more information about SCCs, see Overview of super computing clusters. |
|---|---|---|

| Super Computing Cluster | Subject to Category and instance type | Specify the ID of an SCC. You can select an existing SCC or click Create Cluster to create an SCC. After the SCC is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent SCC list. For more information about how to create an SCC, see Create an SCC. This parameter is available and can be configured only if you set Category to Super Computing Cluster and select an SCC instance type. When you create an instance of an SCC instance type, this parameter is required. |
|---|---|---|
| Number of Cluster Instances | Subject to Super Computing Cluster | The number of nodes (ECS instances) in the SCC. This parameter is automatically configured and cannot be modified after you configure the Super Computing Cluster parameter. |

iii. Configure the image that you want the instance to use. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image, Custom Image, Shared Custom Image, and Global Shared Images. Note For more information, see Overview of images. |

| Public Image | Subject to Image Type | Select a public image. Public images that are provided by Alibaba Cloud without operating system licenses deliver high security and stability. Public images for Windows Server operating systems and mainstream Linux operating systems are provided. This parameter is required if you set Image Type to Public Image. When you use an image that supports Dynamic Host Configuration Protocol version 6 (DHCPv6) to create an instance, an IPv6 address is automatically assigned to the instance. The instance can use the IPv6 address to communicate over the internal network. If you use an image that does not support DHCPv6 to create an instance, you must manually assign an IPv6 address to the instance. The following images support DHCPv6: Linux images CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images Note To use an IPv6 address to communicate over the Internet, you must enable public bandwidth for the IPv6 address. For more information, see the "Step 4: Purchase IPv6 Internet bandwidth" section in Quick start > Create an IPv6 VPC in the VPC U ser Guide in the Apsara Stack Documentation Center. |
|---|---|---|
| Custom Image | Subject to Image Type | Select a custom image. Custom images are created from instances or snapshots or imported from your computer. This parameter is required if you set Image Type to Custom Image. |
| Shared Custom Image | Subject to Image Type | Select a shared custom image. Shared custom images are the custom images that are shared by other level-1 organizations to your organization. This parameter is required if you set Image Type to Shared Custom Image. |

| Global Shared Images | Subject to Image Type | Select a globally shared image. Globally shared images are the custom images that are globally shared by an administrator in the Apsara Uni-manager Operations Console. This parameter is required if you set Image Type to Global Shared Images. |
|---|---|---|

iv. Configure the storage settings of the instance. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Creation Method | Yes | Select the method that you want to use to create a disk. Valid values: Disk Creation and Storage Set Creation. To create a disk in a partition of a specific storage set, select Storage Set Creation. Important If only Disk Creation is displayed, storage sets are not supported in the current environment. You must first configure storage sets. Before you create a disk in a partition of a storage set, make sure that the storage set is created and the partition is configured. For more information, see EBS > Storage sets > Create a storage set in the CDS User Guide in the Apsara Stack Documentation Center. |
| Storage Set | Subject to Creation Method | Select a storage set. This parameter is required if you set Creation Method to Storage Set Creation. |
| Partition | Subject to Creation Method | Specify a partition number. This parameter is required if you set Creation Method to Storage Set Creation. |

| System Disks | Yes | Configure the system disk on which you want to install the operating system. Different Elastic Block Storage (EBS) clusters support different disk categories. New EBS clusters that are deployed in Cloud Defined Storage (CDS) support premium performance disks and standard performance disks. EBS clusters in CDS that are created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks. Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs. The system disk capacity can range from 20 GB to 500 GB. Note The actual minimum system disk capacity varies based on the image type. The capacity range that is displayed on the ECS console prevails. You can specify a name for the system disk based on your business requirements. |
|---|---|---|

| Data Disks | No | Add data disks to store instance data. Different EBS clusters support different disk categories. New EBS clusters that are deployed in CDS support premium performance disks and standard performance disks. EBS clusters in CDS that are created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks. Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs. You can attach up to 16 data disks to an instance. The maximum capacity of each data disk is 32,768 GB. You can specify a name for each data disk based on your business requirements. You can configure the Release with Instance and Encryption parameters for each data disk. To encrypt a data disk, configure the following parameters: Encryption Method: Select AES256 or SM4. Encryption Key: You can select a key that is created in Key Management Service. Note You can add data disks after you create the instance. For more information, see Attach a data disk. |
|---|---|---|

6. Configure the network settings.
You can make network and security group configurations to allow the instance to communicate with the Internet and other resources and to safeguard the instance on the network. After you complete the network settings, click **Next**.

| Parameter | Required | Description |
|---|---|---|

| VPC | Yes | Select the VPC in which you want to create the instance. Select an existing VPC or click Create VPC to create a VPC. After the VPC is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent VPC list. For more information about how to create a VPC, see VPCs and vSwitches > VPC management > Create a VPC in the VPC User Guide in the Apsara Stack Documentation Center. Important If you select an SCC instance type and specify an SCC that has a VPC ID, the VPC ID of the SCC is automatically populated in the field and cannot be modified. For more information, see Add nodes to an SCC. |
|---|---|---|
| VSwitch | Yes | Select the vSwitch to which you want to connect the instance. Select an existing vSwitch or click Create vSwitch to create a vSwitch. After the vSwitch is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent vSwitch list. For more information about how to create a vSwitch, see VPCs and vSwitches > vSwitch management > Create a vSwitch in the VPC User Guide in the Apsara Stack Documentation Center. |
| Private IP Address | No | Specify a private IPv4 address for the instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you do not specify a private IP address, the system allocates a private IP address to the instance. |
| IPv6 | No | Specify whether to assign an IPv6 address to the instance. |

| Security Groups | Yes | Select an existing security group or click Create Security Group to create a security group. After the security group is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent security group list. For more information about how to create a security group, see Create a security group. Important If you select an SCC instance type and specify an SCC that has a security group ID, the security group ID of the SCC is automatically populated in the field and cannot be modified. For more information, see Add nodes to an SCC. |
|---|---|---|

7. Configure the system settings.
The system settings include the logon password, hostname, and user data of the instance. You can view the instance settings that you configure in the ECS console after you create the instance. After you complete the system settings, click **Next**. i. Configure logon credentials. You can use logon credentials to securely log on to the instance. For information about how to connect to an instance, see Instance connecting overview.

> **Important:** You cannot specify a logon password for an instance that is created from the arm_neokylin_7u6_64_20G_20210205.raw or arm_centos_7_6_64_20G_20210205.raw image. You can use a key pair to log on to the instance.

| Parameter | Description |
|---|---|

|   | Key Pair |   | Select an existing key pair or click Create Key Pair to create a key pair. After the key pair is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent key pair list. For more information, see Create a key pair. Note Key pairs can be used to log on to only Linux instances. |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   | Enter and confirm a password. When you log on to an instance by using a username and a password, the default username is root for Linux and administrator for Windows. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include () ' ~ ! @ # $ % ^ & * - + = \| {} [] : ; ' < > , . ? / . For Windows _ instances, the password cannot start with a forward slash (/). Important If you use an NFS, UOS, or Kylin image to create an instance, the logon password of the instance must meet the following requirements based on the image type: NFS: If you use the NFS V4 G195 x86 20G image, _ _ _ _ the password must be at least eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. Supported special characters include: ( ) ' ~ ! |   |   |   |   |   |
|   |   |   |   | Important If you use an NFS, UOS, or Kylin image to create an instance, the logon password of the instance must meet the following requirements based on the image type: NFS: If you use the NFS V4 G195 x86 20G image, _ _ _ _ the password must be at least eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. Supported special characters include: ( ) ' ~ ! |   |   |   |   |
|   |   |   |   |   |   | echo |   |   |
|   |   |   |   |   | ( ) ' ~ ! |   |   |   |
|   |   |   |   | @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , _ |   |   |   |   |
|   |   |   |   | . ? / |   |   |   |   |

|   |   | () ' ~ ! @ # $ % ^ & |
|---|---|---|
|   | * - + = \| {} [] : ; ' < > , . ? / _ |   |

|   | Custom Password |   |   |   |   |   | UOS: If you use the uos server20 1032d x64 20G _ _ _ _ or arm uos server20 1032d 20G image, the _ _ _ _ password must be 8 to 512 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. The monotonous character sequences in the password can be up to four characters in length. Example: 1234. Supported special characters include: ( ) ' ~ ! @ # $ % ^ & * - + = \| { } [ ] _ : ; ' < > , . ? / If you use the uos server20 1040d x64 20G _ _ _ _ or arm uos server20 1040d 20G image, the _ _ _ _ password must be 8 to 512 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. The monotonous character |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   | echo |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | ( ) |   |
|   |   |   |   |   |   |   |   | ' ~ ! @ # $ % ^ & * - + = \| { } [ ] _ |   |   |   |   |   |   |
|   |   |   |   |   |   |   | : ; ' < > , . ? / |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | echo |   |   |
|   |   |   |   |   |   |   | sequences in the password can be up to three characters in length. Example: 123. The number of consecutive identical characters in the password cannot exceed three. Example: aaa. Supported special characters include: ( ) ' ~ ! @ # $ % ^ |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ( ) ' ~ ! @ # $ % ^ |   |   |   |
|   |   |   |   |   |   |   | & * - + = \| { } [ ] : ; ' < > , . ? _ |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | / |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | echo "xxx" \| cracklib- |   |   |   |   |
|   |   |   |   |   |   |   | check |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ( ) ' ~ ! @ # $ % ^ & * - |   |   |   |   |   |
|   |   |   |   |   |   |   | + = \| { } [ ] : ; ' < > , . ? / _ |   |   |   |   |   |   |   |

| Later | After the instance is created, bind the key pair or reset the instance password. |
|---|---|

ii. Configure the basic system settings for the instance, such as the instance name and deployment set. If you want to create multiple instances, you can specify sequential instance names and hostnames to facilitate management.

| Parameter | Required | Description |
|---|---|---|
| Quantity | Yes | You can create up to 100 instances at the same time by using the wizard. The number of instances cannot exceed the quota. The quota is displayed on the homepage of the Apsara Uni-manager Management Console. |
| Instance Name | Yes | Enter a name for the instance. The name must be 2 to 110 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), periods (.), and hyphens (-). _ When you create multiple instances, their names are automatically suffixed with incremental three-digit numbers in order. By default, the incremental suffixes range from 001 to 100. Examples: LocalHost001 and LocalHost002, and MyInstance001 and MyInstance002. |
| Instance Description | No | Enter a description for the instance. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . The description can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |

| Hostname | No | Enter the hostname that you want to display in the operating system. Take note of the following items: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For Windows instances, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). For Linux instances, you can specify the hostname based on the following requirements: The hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). You can use the ${instance id} _ placeholder to pass instance IDs into the hostname. For example, if you set Hostname to k8s-${instance id} and _ the instance is assigned an ID of i- 123abc**** , the hostname of the instance is k8s-i-123abc**** . |   |   |
|---|---|---|---|---|
|   |   |   | i- |   |
| Instance Release Protection | No | You can enable the instance release protection feature to prevent instances from being manually released, which can effectively minimize loss caused by accidental operations or the lack of timely communication among team members. |   |   |
| Tags | No | Select or create tags. Each tag consists of a tag key and a tag value. You can add tags to resources that have identical characteristics, such as resources that belong to the same organization and resources that serve the same purpose. You can use tags to search for and manage resources in an efficient manner. You can specify up to 20 tags. |   |   |

| Deployment Set Important This parameter is not displayed if you select an SCC instance type to create instances. | No | Select an existing deployment set or click Create Deployment Set to create a deployment set. After the deployment set is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent deployment set list. For more information about how to create a deployment set, see Create a deployment set. A deployment set is a policy that controls the distribution of ECS instances. You can use deployment sets to design disaster recovery and service availability solutions when you create ECS instances. You can use deployment sets to disperse or aggregate instances. |
|---|---|---|

iii. Configure advanced options. You can run user data as scripts on instance startup to automate instance configuration. You can also pass user data into instances as common data. For more information, see Instance user data. In the User Data field, enter the user data that you prepared. If the user data is already encoded in Base64, turn on **Based64 Encoded Data**.
8. In the Confirmation step, check the basic settings, network settings, and system
configurations of the instance, and then click **Submit**.

**Result**

The new instance that you create appears on the Instances page. When the instance is being created, it is in the **Preparing** state. After the instance is created, it enters the **Running** state.

### 3.5 Connect to an instance

#### 3.5.1 Overview

After an instance is created, you can connect to the instance to perform operations, such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that use public IP addresses. For more information, see the following topics: Connect to a Linux instance by using SSH commands in Linux or Mac OS X Connect to a Linux instance by using a remote connection tool in Windows Connect to a Windows instance from a Windows computer by using Remote Desktop Use the VNC feature in the Elastic Computer Service (ECS) console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator.The username of a Linux instance is root.

#### 3.5.2 Connect to a Linux instance by using SSH commands in Linux or Mac OS X

**SSH commands in Linux or Mac OS X**

This topic describes how to use SSH commands to connect to a Linux instance.

**Prerequisites**

The instance and the security group are created. The instance is in the **Running** state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

1. Enter the following command and press the Enter key:

```
ssh root@<EIP of the instance>
```

2. Enter the instance password of the root user and press the Enter key.

#### 3.5.3 Connect to a Linux instance by using a remote connection tool in Windows

**remote connection tool in Windows**

This topic describes how to connect to a Linux instance by using the PuTTY tool.

**Prerequisites**

Connection tools are used in a similar way. In this example, PuTTY is used to connect to a Linux instance. To download PuTTY, go to the Putty official website.
1. Download and install PuTTY for Windows.
2. Start the PuTTY client and complete the following settings:
**Host Name (or IP Address)**: Enter the elastic IP address of the instance to which you
want to connect.
**Port**: Specify the default port 22.
**Connection Type**: Select **SSH**.
**Saved Session**: Enter a session name, and then click **Save**. After the settings are saved,
PuTTY records the name and IP address of the instance.
3. Click **Open** to connect to the instance.
The first time you connect to the instance, a PuTTY security alert is displayed. Click **Yes** to proceed.
4. Enter **root** as the username and press the
`Enter` key.
5. Enter the password of the instance and press the
`Enter` key. The following message indicates that you are connected to the instance.

```
Welcome to aliyun Elastic Compute Server!
```

#### 3.5.4 Connect to a Windows instance from a Windows computer by using Remote Desktop

**Windows computer by using Remote Desktop**

This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC).

**Prerequisites**

A Windows instance is created and added to a security group. The instance is in the **Running** state. A logon password is set for the instance. An elastic IP address (EIP) is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

1. Use one of the following methods to enable RDC:

> **Note:** In this topic, an on-premises computer that runs Windows 10 is used. Operations may vary based on your operating system.

On the taskbar of the Windows desktop, enter `mstsc` in the search box. Then, click
**Remote Desktop Connection** in the search results.
Press the Windows logo key+R. In the **Run** dialog box, enter `mstsc` and click **OK**.
2. In the **Remote Desktop Connection** dialog box, enter the EIP of the instance and click
**Show Options**.
3. Enter the username of the instance.
The default username is **administrator**.
4. **Optional:**If you do not want to enter the password during subsequent connections, select
**Allow me to save credentials** .
5. Click **Connect**.
6. In the **Windows Security** dialog box, enter the password corresponding to the username
that you entered and click **OK**.

**Result**

If the Windows desktop appears, a connection to the Windows instance is established. If an error message is returned indicating that an authentication error occurs and the function requested is not supported, install CredSSP updates and try again. Follow the following steps to install the updates:
1. Connect to the instance by using Virtual Network Computing (VNC). For more information,
see Connect to an instance by using a VNC management terminal.
2. Choose **Start > Control Panel**.
3. Click **System and Security**.
4. Click **Check for updates** in the **Windows Updates** section.
5. If updates are available, click **Install updates**.
6. Restart the instance.

#### 3.5.5 Connect to an instance by using a VNC management terminal

**management terminal**

If other remote connection tools such as PuTTy, Xshell, and SecureCRT are not installed or do not work properly, you can access your instances by using a VNC management terminal in the ECS console.

**Prerequisites**

The instance to which you want to connect is in the **Running** state. The root certificate is imported to your web browser. For more information, see Install the certificate for VNC in Windows. The VNC password is reset if it is your first time to connect to the instance after the instance is created. For more information, see Change the VNC password.

**Background information**

The VNC password is used to log on to a VNC management terminal in the ECS console, whereas the instance password is used to log on to the instance. You can use a VNC management terminal to connect to an instance to solve specific issues. The following table lists some of the issues.

| Issue | Solution |
|---|---|
| The instance starts slowly due to self-check on startup. | Check the self-check progress. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear and consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to connect and click **Remote Connection** in the
**Actions** column.
5. Enter the VNC password and click **OK**.
After you are logged on to the VNC management terminal, a logon page similar to the following one appears.
6. Enter your username and password.
For a Linux instance, enter the username `root` and the logon password.

> **Note:** When you log on to the Linux instance, the password is not displayed when you enter it. Press the Enter key after you enter the password.

For a Windows instance, to use a keyboard shortcut such as Ctrl+Alt+Delete, click the List icon in the upper-left corner of the page and select the keyboard shortcut from the drop-down list. Enter the username and password as prompted. Then, click the Log On icon, such as .

## 4 Instances

### 4.1 Overview

An Elastic Compute Service (ECS) instance is a virtual server that includes basic components such as CPUs, memory, an operating system (OS), network configurations, and disks. You can use management tools provided by Alibaba Cloud such as the ECS console and ECS API to create and manage ECS instances. You can manage the status of ECS instances and their deployed applications in the same manner as you would do with local servers. You can also upgrade the capabilities (such as compute and storage capabilities) of your ECS instances as your requirements increase.

**Basic instance configurations**

The following basic configurations of ECS instances determine the basic resources that the instances require: Instance types Instance types define the basic attributes of ECS instances, such as compute capacity, storage capacity, and networking capacity. Instance types must be used together with images, Elastic Block Storage (EBS) devices, and network resources to create ECS instances that serve different purposes. ECS provides a variety of instance families for typical use scenarios. Each instance family consists of multiple instance types that have different compute capabilities and are suited to different scenarios and requirements. For more information, see **Instance families and**
**instance types** in the ECS documentation.
Images contain the information necessary to run ECS instances, such as OSs and initialization data of applications. Alibaba Cloud provides ready-to-use images for Windows Server and several mainstream Linux OSs. You can also create or import your own images to save time in making repeated configurations. Storage ECS instances use their attached system disks and data disks for storage. Each instance must have a system disk attached. The first time the instance starts, the OS is installed and instance configurations are initialized based on the system disk image. Cloud disks can be used as system disks or data disks. Local disks can be used only as data disks and are available only for specific instance types, such as instance types with local HDDs. If you want your instances to have more storage space, you can resize their attached cloud disks or attach more cloud disks after the instances are created. For more information, see Create a disk and Attach a data disk. Business data is an important asset. Cloud disks use a triplicate mechanism to ensure the durability of data. To ensure that your data remains available, we recommend that you back up your data on a regular basis. You can create snapshots of cloud disks to back up disk data. If you are using local disks, you must implement data redundancy at the application layer to ensure data availability. In addition to basic configurations, you can also configure network configurations, security groups, and OSs for instances. For more information, see Create an instance by using the wizard.

**Security suggestions**

When you use Apsara Stack services, we recommend that you follow security suggestions to improve resource security, such as the following ones: Suggestions for permission control: Use the Enterprise Permissions features to control which users can manage resources such as instances and what permissions to grant to the users. Suggestions for security features: Use security features such as security hardening and cloud disk encryption to ensure the security of data and runtime environments. Suggestions for network security: Use virtual private clouds (VPCs) to isolate services of different security levels. Use security groups to control inbound and outbound traffic for instances and allow instances access to the Internet only when required to minimize the attack surface area of resources.

### 4.2 Create an instance by using the wizard

**the wizard**

An Elastic Compute Service (ECS) instance is a virtual machine that contains basic components, such as the CPU, memory, operating system, network settings, and disks.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For more information, see **VPCs**
**and vSwitches > VPC management > Create a VPC** and **VPCs and vSwitches >**
**vSwitch management > Create a vSwitch** in the VPC User Guide in the Apsara Stack
Documentation Center. If you want to assign an IPv6 address to the instance that you want to create, make sure that the VPC and vSwitch are associated with IPv6 CIDR blocks. For more information, see
**Quick start > Create an IPv6 VPC** in the VPC User Guide in the Apsara Stack
Documentation Center. A security group is created. For more information, see Create a security group.

**Background information**

Specific limits apply when you create GPU-accelerated instances. For more information, see Limits.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance**.
5. Configure the basic settings.
In the Basic Settings step, configure the basic attributes and the basic resources that are required to create an instance. The basic attributes include the organization, resource set, region, and zone. The basic resources include the instance type, image, and storage. After you complete the basic settings, click **Next**. You can click **Configuration Preview** in the lower part of the page to view the instance information. The information includes the settings that you configured and the settings that you need to specify. i. Configure the basic attributes of the instance. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization for which you want to create the instance. |
| Resource Set | Yes | Select the resource set in which you want to create the instance. |
| Region | Yes | Select the region in which you want to create the instance. |
| Zone | Yes | Select the zone in which you want to create the instance. Zones are physical locations in the same region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |

ii. Configure the instance specifications, such as the instance family and instance type. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Support Hot Configuration Changes | No | If you turn on the switch, you can change the instance type without the need to stop the instance. For more information, see Perform a hot configuration change on an instance to change the instance type. |
| Filter | No | Specify the number of vCPUs, memory size, or instance type name based on your business requirements to search for instance types. |

| Hardware Manufacturers | Yes | Select a hardware manufacturer. Valid values: Intel/X86 Hygon/X86 Kunpeng/ARM Phytium/ARM Yitian/ARM SW Others Note The actual hardware manufacturers that are supported are displayed on the Create Instance page in the ECS console. |
|---|---|---|
| Category | Yes | Select an instance category. Valid values: Dedicated Shared Local SSD Local HDD Super Computing Cluster ECS Bare Metal Instance Others Note The actual instance types that are supported are displayed on the Create Instance page in the ECS console. |

| Specification | Yes | Select an instance type. The instance type list consists of multiple columns, including Instance Family, Instance Type, Instance Family Level, CPU Type, Memory, and Internal Bandwidth. Select an instance type based on your business requirements. Note For more information about instance families and instance types, see the Introduction to Instance Famil ies and Instance Types in the Apsara Stack ECS documentation. Instance types that have specific vCPU and memory combinations do not support Windows Server images. For more information, see Limits. Important If you create a GPU-accelerated instance, install a GPU driver on the instance based on the operating system of the instance. Except that you must install GPU drivers on GPU- accelerated instances, you can manage GPU- accelerated instances in the same manner as you manage non-GPU-accelerated instances. For information about how to install GPU drivers on NVIDIA GPU-accelerated instances, see Installation guideline for NVIDIA drivers. For information about how to install GPU drivers on instances that are equipped with GPUs from other manufacturers, see the official documents of the manufacturers. If you create an instance of a Super Computing Cluster (SCC) instance type, you must configure the Super Computing Cluster parameter, instead of the Deployment Set parameter. When you select an SCC instance type, the Deployment Set parameter is not displayed on the Create Instance page. The VPC and Security Groups parameters may be affected by the VPC ID and security group ID of the SCC. For more information about SCCs, see Overview of super computing clusters. |
|---|---|---|
| Super Computing Cluster | Subject to Category and instance type | Specify the ID of an SCC. You can select an existing SCC or click Create Cluster to create an SCC. After the SCC is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent SCC list. For more information about how to create an SCC, see Create an SCC. This parameter is available and can be configured only if you set Category to Super Computing Cluster and select an SCC instance type. When you create an instance of an SCC instance type, this parameter is required. |

| Number of Cluster Instances | Subject to Super Computing Cluster | The number of nodes (ECS instances) in the SCC. This parameter is automatically configured and cannot be modified after you configure the Super Computing Cluster parameter. |
|---|---|---|

iii. Configure the image that you want the instance to use. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image, Custom Image, Shared Custom Image, and Global Shared Images. Note For more information, see Overview of images. |

| Public Image | Subject to Image Type | Select a public image. Public images that are provided by Alibaba Cloud without operating system licenses deliver high security and stability. Public images for Windows Server operating systems and mainstream Linux operating systems are provided. This parameter is required if you set Image Type to Public Image. When you use an image that supports Dynamic Host Configuration Protocol version 6 (DHCPv6) to create an instance, an IPv6 address is automatically assigned to the instance. The instance can use the IPv6 address to communicate over the internal network. If you use an image that does not support DHCPv6 to create an instance, you must manually assign an IPv6 address to the instance. The following images support DHCPv6: Linux images CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images Note To use an IPv6 address to communicate over the Internet, you must enable public bandwidth for the IPv6 address. For more information, see the "Step 4: Purchase IPv6 Internet bandwidth" section in Quick start > Create an IPv6 VPC in the VPC U ser Guide in the Apsara Stack Documentation Center. |
|---|---|---|
| Custom Image | Subject to Image Type | Select a custom image. Custom images are created from instances or snapshots or imported from your computer. This parameter is required if you set Image Type to Custom Image. |
| Shared Custom Image | Subject to Image Type | Select a shared custom image. Shared custom images are the custom images that are shared by other level-1 organizations to your organization. This parameter is required if you set Image Type to Shared Custom Image. |

| Global Shared Images | Subject to Image Type | Select a globally shared image. Globally shared images are the custom images that are globally shared by an administrator in the Apsara Uni-manager Operations Console. This parameter is required if you set Image Type to Global Shared Images. |
|---|---|---|

iv. Configure the storage settings of the instance. The following table describes the parameters.

| Parameter | Required | Description |
|---|---|---|
| Creation Method | Yes | Select the method that you want to use to create a disk. Valid values: Disk Creation and Storage Set Creation. To create a disk in a partition of a specific storage set, select Storage Set Creation. Important If only Disk Creation is displayed, storage sets are not supported in the current environment. You must first configure storage sets. Before you create a disk in a partition of a storage set, make sure that the storage set is created and the partition is configured. For more information, see EBS > Storage sets > Create a storage set in the CDS User Guide in the Apsara Stack Documentation Center. |
| Storage Set | Subject to Creation Method | Select a storage set. This parameter is required if you set Creation Method to Storage Set Creation. |
| Partition | Subject to Creation Method | Specify a partition number. This parameter is required if you set Creation Method to Storage Set Creation. |

| System Disks | Yes | Configure the system disk on which you want to install the operating system. Different Elastic Block Storage (EBS) clusters support different disk categories. New EBS clusters that are deployed in Cloud Defined Storage (CDS) support premium performance disks and standard performance disks. EBS clusters in CDS that are created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks. Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs. The system disk capacity can range from 20 GB to 500 GB. Note The actual minimum system disk capacity varies based on the image type. The capacity range that is displayed on the ECS console prevails. You can specify a name for the system disk based on your business requirements. |
|---|---|---|

| Data Disks | No | Add data disks to store instance data. Different EBS clusters support different disk categories. New EBS clusters that are deployed in CDS support premium performance disks and standard performance disks. EBS clusters in CDS that are created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks. Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs. You can attach up to 16 data disks to an instance. The maximum capacity of each data disk is 32,768 GB. You can specify a name for each data disk based on your business requirements. You can configure the Release with Instance and Encryption parameters for each data disk. To encrypt a data disk, configure the following parameters: Encryption Method: Select AES256 or SM4. Encryption Key: You can select a key that is created in Key Management Service. Note You can add data disks after you create the instance. For more information, see Attach a data disk. |
|---|---|---|

6. Configure the network settings.
You can make network and security group configurations to allow the instance to communicate with the Internet and other resources and to safeguard the instance on the network. After you complete the network settings, click **Next**.

| Parameter | Required | Description |
|---|---|---|

| VPC | Yes | Select the VPC in which you want to create the instance. Select an existing VPC or click Create VPC to create a VPC. After the VPC is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent VPC list. For more information about how to create a VPC, see VPCs and vSwitches > VPC management > Create a VPC in the VPC User Guide in the Apsara Stack Documentation Center. Important If you select an SCC instance type and specify an SCC that has a VPC ID, the VPC ID of the SCC is automatically populated in the field and cannot be modified. For more information, see Add nodes to an SCC. |
|---|---|---|
| VSwitch | Yes | Select the vSwitch to which you want to connect the instance. Select an existing vSwitch or click Create vSwitch to create a vSwitch. After the vSwitch is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent vSwitch list. For more information about how to create a vSwitch, see VPCs and vSwitches > vSwitch management > Create a vSwitch in the VPC User Guide in the Apsara Stack Documentation Center. |
| Private IP Address | No | Specify a private IPv4 address for the instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you do not specify a private IP address, the system allocates a private IP address to the instance. |
| IPv6 | No | Specify whether to assign an IPv6 address to the instance. |

| Security Groups | Yes | Select an existing security group or click Create Security Group to create a security group. After the security group is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent security group list. For more information about how to create a security group, see Create a security group. Important If you select an SCC instance type and specify an SCC that has a security group ID, the security group ID of the SCC is automatically populated in the field and cannot be modified. For more information, see Add nodes to an SCC. |
|---|---|---|

7. Configure the system settings.
The system settings include the logon password, hostname, and user data of the instance. You can view the instance settings that you configure in the ECS console after you create the instance. After you complete the system settings, click **Next**. i. Configure logon credentials. You can use logon credentials to securely log on to the instance. For information about how to connect to an instance, see Instance connecting overview.

> **Important:** You cannot specify a logon password for an instance that is created from the arm_neokylin_7u6_64_20G_20210205.raw or arm_centos_7_6_64_20G_20210205.raw image. You can use a key pair to log on to the instance.

| Parameter | Description |
|---|---|

|   | Key Pair |   | Select an existing key pair or click Create Key Pair to create a key pair. After the key pair is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent key pair list. For more information, see Create a key pair. Note Key pairs can be used to log on to only Linux instances. |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   | Enter and confirm a password. When you log on to an instance by using a username and a password, the default username is root for Linux and administrator for Windows. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include () ' ~ ! @ # $ % ^ & * - + = \| {} [] : ; ' < > , . ? / . For Windows _ instances, the password cannot start with a forward slash (/). Important If you use an NFS, UOS, or Kylin image to create an instance, the logon password of the instance must meet the following requirements based on the image type: NFS: If you use the NFS V4 G195 x86 20G image, _ _ _ _ the password must be at least eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. Supported special characters include: ( ) ' ~ ! |   |   |   |   |   |
|   |   |   |   | Important If you use an NFS, UOS, or Kylin image to create an instance, the logon password of the instance must meet the following requirements based on the image type: NFS: If you use the NFS V4 G195 x86 20G image, _ _ _ _ the password must be at least eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. Supported special characters include: ( ) ' ~ ! |   |   |   |   |
|   |   |   |   |   |   | echo |   |   |
|   |   |   |   |   | ( ) ' ~ ! |   |   |   |
|   |   |   |   | @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , _ |   |   |   |   |
|   |   |   |   | . ? / |   |   |   |   |

|   |   | () ' ~ ! @ # $ % ^ & |
|---|---|---|
|   | * - + = \| {} [] : ; ' < > , . ? / _ |   |

|   | Custom Password |   |   |   |   |   | UOS: If you use the uos server20 1032d x64 20G _ _ _ _ or arm uos server20 1032d 20G image, the _ _ _ _ password must be 8 to 512 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. The monotonous character sequences in the password can be up to four characters in length. Example: 1234. Supported special characters include: ( ) ' ~ ! @ # $ % ^ & * - + = \| { } [ ] _ : ; ' < > , . ? / If you use the uos server20 1040d x64 20G _ _ _ _ or arm uos server20 1040d 20G image, the _ _ _ _ password must be 8 to 512 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" \| cracklib-check command to check whether the password meets this requirement. The monotonous character |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   | echo |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | ( ) |   |
|   |   |   |   |   |   |   |   | ' ~ ! @ # $ % ^ & * - + = \| { } [ ] _ |   |   |   |   |   |   |
|   |   |   |   |   |   |   | : ; ' < > , . ? / |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | echo |   |   |
|   |   |   |   |   |   |   | sequences in the password can be up to three characters in length. Example: 123. The number of consecutive identical characters in the password cannot exceed three. Example: aaa. Supported special characters include: ( ) ' ~ ! @ # $ % ^ |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ( ) ' ~ ! @ # $ % ^ |   |   |   |
|   |   |   |   |   |   |   | & * - + = \| { } [ ] : ; ' < > , . ? _ |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | / |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | echo "xxx" \| cracklib- |   |   |   |   |
|   |   |   |   |   |   |   | check |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ( ) ' ~ ! @ # $ % ^ & * - |   |   |   |   |   |
|   |   |   |   |   |   |   | + = \| { } [ ] : ; ' < > , . ? / _ |   |   |   |   |   |   |   |

| Later | After the instance is created, bind the key pair or reset the instance password. |
|---|---|

ii. Configure the basic system settings for the instance, such as the instance name and deployment set. If you want to create multiple instances, you can specify sequential instance names and hostnames to facilitate management.

| Parameter | Required | Description |
|---|---|---|
| Quantity | Yes | You can create up to 100 instances at the same time by using the wizard. The number of instances cannot exceed the quota. The quota is displayed on the homepage of the Apsara Uni-manager Management Console. |
| Instance Name | Yes | Enter a name for the instance. The name must be 2 to 110 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), periods (.), and hyphens (-). _ When you create multiple instances, their names are automatically suffixed with incremental three-digit numbers in order. By default, the incremental suffixes range from 001 to 100. Examples: LocalHost001 and LocalHost002, and MyInstance001 and MyInstance002. |
| Instance Description | No | Enter a description for the instance. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . The description can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |

| Hostname | No | Enter the hostname that you want to display in the operating system. Take note of the following items: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For Windows instances, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). For Linux instances, you can specify the hostname based on the following requirements: The hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). You can use the ${instance id} _ placeholder to pass instance IDs into the hostname. For example, if you set Hostname to k8s-${instance id} and _ the instance is assigned an ID of i- 123abc**** , the hostname of the instance is k8s-i-123abc**** . |   |   |
|---|---|---|---|---|
|   |   |   | i- |   |
| Instance Release Protection | No | You can enable the instance release protection feature to prevent instances from being manually released, which can effectively minimize loss caused by accidental operations or the lack of timely communication among team members. |   |   |
| Tags | No | Select or create tags. Each tag consists of a tag key and a tag value. You can add tags to resources that have identical characteristics, such as resources that belong to the same organization and resources that serve the same purpose. You can use tags to search for and manage resources in an efficient manner. You can specify up to 20 tags. |   |   |

| Deployment Set Important This parameter is not displayed if you select an SCC instance type to create instances. | No | Select an existing deployment set or click Create Deployment Set to create a deployment set. After the deployment set is created, go back to the ECS instance creation wizard and click the icon to obtain the most recent deployment set list. For more information about how to create a deployment set, see Create a deployment set. A deployment set is a policy that controls the distribution of ECS instances. You can use deployment sets to design disaster recovery and service availability solutions when you create ECS instances. You can use deployment sets to disperse or aggregate instances. |
|---|---|---|

iii. Configure advanced options. You can run user data as scripts on instance startup to automate instance configuration. You can also pass user data into instances as common data. For more information, see Instance user data. In the User Data field, enter the user data that you prepared. If the user data is already encoded in Base64, turn on **Based64 Encoded Data**.
8. In the Confirmation step, check the basic settings, network settings, and system
configurations of the instance, and then click **Submit**.

**Result**

The new instance that you create appears on the Instances page. When the instance is being created, it is in the **Preparing** state. After the instance is created, it enters the **Running** state.

### 4.3 Connect to an instance

#### 4.3.1 Overview

After an instance is created, you can connect to the instance to perform operations, such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that use public IP addresses. For more information, see the following topics: Connect to a Linux instance by using SSH commands in Linux or Mac OS X Connect to a Linux instance by using a remote connection tool in Windows Connect to a Windows instance from a Windows computer by using Remote Desktop Use the VNC feature in the Elastic Computer Service (ECS) console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator.The username of a Linux instance is root.

#### 4.3.2 Connect to a Linux instance by using SSH commands in Linux or Mac OS X

**SSH commands in Linux or Mac OS X**

This topic describes how to use SSH commands to connect to a Linux instance.

**Prerequisites**

The instance and the security group are created. The instance is in the **Running** state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

1. Enter the following command and press the Enter key:

```
ssh root@<EIP of the instance>
```

2. Enter the instance password of the root user and press the Enter key.

#### 4.3.3 Connect to a Linux instance by using a remote connection tool in Windows

**remote connection tool in Windows**

This topic describes how to connect to a Linux instance by using the PuTTY tool.

**Prerequisites**

Connection tools are used in a similar way. In this example, PuTTY is used to connect to a Linux instance. To download PuTTY, go to the Putty official website.
1. Download and install PuTTY for Windows.
2. Start the PuTTY client and complete the following settings:
**Host Name (or IP Address)**: Enter the elastic IP address of the instance to which you
want to connect.
**Port**: Specify the default port 22.
**Connection Type**: Select **SSH**.
**Saved Session**: Enter a session name, and then click **Save**. After the settings are saved,
PuTTY records the name and IP address of the instance.
3. Click **Open** to connect to the instance.
The first time you connect to the instance, a PuTTY security alert is displayed. Click **Yes** to proceed.
4. Enter **root** as the username and press the
`Enter` key.
5. Enter the password of the instance and press the
`Enter` key. The following message indicates that you are connected to the instance.

```
Welcome to aliyun Elastic Compute Server!
```

#### 4.3.4 Connect to a Windows instance from a Windows computer by using Remote Desktop

**Windows computer by using Remote Desktop**

This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC).

**Prerequisites**

A Windows instance is created and added to a security group. The instance is in the **Running** state. A logon password is set for the instance. An elastic IP address (EIP) is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

1. Use one of the following methods to enable RDC:

> **Note:** In this topic, an on-premises computer that runs Windows 10 is used. Operations may vary based on your operating system.

On the taskbar of the Windows desktop, enter `mstsc` in the search box. Then, click
**Remote Desktop Connection** in the search results.
Press the Windows logo key+R. In the **Run** dialog box, enter `mstsc` and click **OK**.
2. In the **Remote Desktop Connection** dialog box, enter the EIP of the instance and click
**Show Options**.
3. Enter the username of the instance.
The default username is **administrator**.
4. **Optional:**If you do not want to enter the password during subsequent connections, select
**Allow me to save credentials** .
5. Click **Connect**.
6. In the **Windows Security** dialog box, enter the password corresponding to the username
that you entered and click **OK**.

**Result**

If the Windows desktop appears, a connection to the Windows instance is established. If an error message is returned indicating that an authentication error occurs and the function requested is not supported, install CredSSP updates and try again. Follow the following steps to install the updates:
1. Connect to the instance by using Virtual Network Computing (VNC). For more information,
see Connect to an instance by using a VNC management terminal.
2. Choose **Start > Control Panel**.
3. Click **System and Security**.
4. Click **Check for updates** in the **Windows Updates** section.
5. If updates are available, click **Install updates**.
6. Restart the instance.

#### 4.3.5 Install the certificate for VNC in Windows

**Windows**

Before you can log on to the Virtual Network Computing (VNC) management terminal, you must export the relative certificate from the site such as the Apsara Uni-manager Management Console and install the certificate in a browser on your computer.

**Background information**

The VNC feature is provided by the VNC proxy service. The VNC proxy service uses a different certificate than that of Apsara Infrastructure Management Framework. The certificate of the VNC proxy service must be imported manually.
1. Export the certificate from the Apsara Uni-manager Management Console.
i. Log on to the Apsara Uni-manager Management Console. Then, press the **F12** key or
**Fn+F12** to view and select the certificate.
In this example, the Chrome browser is used. Press the **F12** key to open Chrome DevTools and click View certificate on the Security tab, as shown in the following figure. ii. In the **Certificate** window, click the **Certificate Path** tab, select the root certificate, and then click **View Certificate**. iii. In the **Certificate** window, click the **Details** tab and then click **Copy to File**. iv. In the **Certificate Export Wizard**, click **Next**. v. Select **DER encoded binary X.509 (.CER)** as the format and then click **Next**. vi. Click **Browse**, select the location where to store the certificate, enter a file name, and then click **Save**. vii. Click **Next**. viii. Click **Complete**. ix. Then, click **OK**.
2. Install the certificate in a browser on your on-premises computer.
i. Double-click the certificate. ii. In the **Certificate** window, click **Install Certificate**. iii. In the **Certificate Import Wizard**, click **Next**. iv. Select **Place all certificates in the following store** and click **Browse**. v. In the **Select Certificate Store** window, select **Trusted Root Certificate Authority** and then click **OK**. vi. In the **Certificate Import Wizard**, click **Next**. vii. Click **Complete**. viii. If a security warning message is displayed, click **Yes**.
3. Restart your browser and log on to the Apsara Uni-manager Management Console.
After the certificate is installed, the security warning message is no longer displayed on the left of the URL when you log on to the Apsara Uni-manager Management Console.

#### 4.3.6 Connect to an instance by using a VNC management terminal

**management terminal**

If other remote connection tools such as PuTTy, Xshell, and SecureCRT are not installed or do not work properly, you can access your instances by using a VNC management terminal in the ECS console.

**Prerequisites**

The instance to which you want to connect is in the **Running** state. The root certificate is imported to your web browser. For more information, see Install the certificate for VNC in Windows. The VNC password is reset if it is your first time to connect to the instance after the instance is created. For more information, see Change the VNC password.

**Background information**

The VNC password is used to log on to a VNC management terminal in the ECS console, whereas the instance password is used to log on to the instance. You can use a VNC management terminal to connect to an instance to solve specific issues. The following table lists some of the issues.

| Issue | Solution |
|---|---|
| The instance starts slowly due to self-check on startup. | Check the self-check progress. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear and consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to connect and click **Remote Connection** in the
**Actions** column.
5. Enter the VNC password and click **OK**.
After you are logged on to the VNC management terminal, a logon page similar to the following one appears.
6. Enter your username and password.
For a Linux instance, enter the username `root` and the logon password.

> **Note:** When you log on to the Linux instance, the password is not displayed when you enter it. Press the Enter key after you enter the password.

For a Windows instance, to use a keyboard shortcut such as Ctrl+Alt+Delete, click the List icon in the upper-left corner of the page and select the keyboard shortcut from the drop-down list. Enter the username and password as prompted. Then, click the Log On icon, such as .

### 4.4 Manage instance status

#### 4.4.1 Stop an instance

You can stop the instances that you do not use for the moment. The stop operation interrupts services that are running on the instances. Exercise caution when you perform this operation.

**Prerequisites**

The instance is in the **Running** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to stop instances:
To stop a single instance at a time, find the instance and choose **Instance Status >**
**Stop Instance** in the **Actions** column.
To stop one or more instances at a time, select the instances and click **Stop** in the lower part of the Instances page.
5. In the message that appears, click **Stop Instance**.

**Result**

When an instance is being stopped, its state in the **Status** column changes from **Running** to
**Stopping**. When the instance is stopped, its state changes to **Stopped**.

#### 4.4.2 Start an instance

If an Elastic Compute Service (ECS) instance is in a state (such as Stopped) in which it cannot provide services, you must start the instance before you can use it. This topic describes how to start an instance in the ECS console.

**Prerequisites**

The instance is in the **Stopped** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to start an instance:
To start a single instance at a time, find the instance and choose **Instance Status >**
**Start Instance** in the **Actions** column.
To start one or more instances at a time, select the instances and click **Start** in the lower part of the Instances page.
5. In the message that appears, click **Start Instance**.

**Result**

When an instance is being started, its state in the **Status** column changes from **Stopped** to
**Starting**. When the instance is started, its state changes to **Running**.

#### 4.4.3 Restart an instance

After you change the logon passwords or install system updates for instances, you must restart the instances. The restart operation stops the instances for a short period of time and interrupts services that are running on the instances. Exercise caution when you perform this operation.

**Prerequisites**

The instances that you want to restart are in the **Running** state.

> **Warning:** The restart operation stops the instances for a short period of time and interrupts services that are running on the instances. Exercise caution when you perform this operation.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
Useoneofthefollowingmethodstorestartinstances:
4. Use one of the following methods to restart instances:
To restart a single instance at a time, find the instance and choose **Instance Status >**
**Restart Instance** in the **Actions** column.
To restart one or more instances at a time, select the instances and click **Restart** in the lower part of the Instances page.
5. In the dialog box that appears, specify whether to forcefully restart the instances.
If you select **Force Restart**, the instances are forcefully restarted. This may result in the loss of unsaved data. If you do not select **Force Restart**, the instances are gracefully restarted.
6. Click **Restart Instance**.

**Result**

When an instance is being restarted, its state in the **Status** column changes from **Running** to **Stopping**. When the instance is restarted, its state changes to **Running**.

#### 4.4.4 Delete an instance

You can delete Elastic Compute Service (ECS) instances that are no longer needed to release their resources. This topic describes how to delete an instance.

**Prerequisites**

The instance that you want to delete is in the **Stopped** state.

**Background information**

Deleted instances cannot be recovered. We recommend that you back up data before you delete instances. If data disks are released along with the instances, the disk data cannot be recovered. For more information, see Create a snapshot. To ensure business continuity, we recommend that you select **Move to Recycle Bin** when you delete an instance. This way, the deleted instance is moved to the recycle bin and retained there for a specified period of time. Make sure that your business is not affected by the instance delete operation before you permanently delete the instance.

> **Note:** Instances that use local disks cannot be moved to the recycle bin.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete an instance.
To delete a single instance at a time, perform the following operations: a. Find the instance and choose **Instance Status > Delete** in the **Actions** column. b. In the dialog box that appears, select **Move to Recycle Bin** as needed. Then, click
**Delete**.
To delete one or more instances at a time, perform the following operations: a. Select the instances that you want to delete and click **Delete** in the lower part of the Instances page. b. In the dialog box that appears, select **Move to Recycle Bin** as needed. Then, click
**Delete**.

> **Note:** When deleted instances are moved to the recycle bin, the instances enter a retention period, which is three days by default. During the retention period, the computing resources (vCPUs and memory) of the instances are released, their elastic IP addresses are disassociated, and their storage resources are retained. If you do not restore resources from the recycle bin during the retention period, the resources are automatically deleted when the retention period expires, and cannot be restored. You can restore the instances from the recycle bin anytime during the retention period. For more information, see Restore an instance.

### 4.5 Manage instance attributes

#### 4.5.1 View instance information

You can view the list of Elastic Compute Service (ECS) instances in your account and the details of individual instances. The details of an instance include the basic configurations, disks, snapshots, security groups, and elastic network interfaces (ENIs).

**View the information of instances on the Overview page**

By default, the **Overview** page is displayed when you log on to the ECS console. The **Overview** page consists of the following sections:

**Instance Overview**

This section shows statistics about ECS instance resources in the current region that belong to all resource sets under the current organization in your account. The statistics include the total number of instances, number of running instances, number of images, number of disks, number of security groups, number of snapshots, CPU quota, memory quota, and disk quota.

**Top 10 Organizations by Quota Usage**

This section shows the 10 organizations that have the highest quota usage. You can click
**By CPU Quota Usage**, **By Memory Quota Usage**, or **By Storage Quota Usage** to list
the 10 organizations that have the highest CPU, memory, or disk quota usage and view the recent quota usage rankings and trends of the organizations.

**Top 20 Instances by Resource Usage**

This section shows the 20 instances that have the highest resource usage. You can click **By**
**CPU Utilization** or **By Memory Usage** to list the 20 instances that have the highest CPU
utilization or memory usage and check whether the resource usage of these instances meets your expectations. This section shows organizations that have high and low quota usage and instances that have high and low resource usage and provides suggestions for optimizing resource allocation to improve resource utilization.

**View the information of a single instance on the Instance**

**Details page**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option to search for instances.
Select a filer option from the drop-down list and enter relevant information to search for instances. Click **Advanced Filter**, specify multiple filter options, and then click **Search**. The following table describes the filter options in the Advanced Filter section.

| Filter option | Description |
|---|---|
| Instance Name | Enter an instance name to search for the instance. |
| Instance ID | Enter an instance ID to search for the instance. |
| IP Address | Enter the IP address of an instance to search for the instance. |
| VPC ID | Enter a virtual private cloud (VPC) ID to search for instances that belong to the VPC. |
| The image ID. | Enter an image ID to search for instances that use the image. |
| Security Group ID | Enter a security group ID to search for instances that belong to the security group. |
| Platform | Enter a operating system name to search for instances that use the operating system. |
| Instance Type | Enter an instance type to search for instances of the instance type. |
| Deployment Set ID | Enter a deployment set ID to search for the instances that belong to the deployment set. |
| Zone | Enter a zone to search for instances that reside in the zone. |
| Key Pair Name | Enter a key pair name to search for instances that have the key pair bound. |
| Network Type | Enter a network type to search for instances of the network type. |
| Tag | Click the Tag field and then select tag keys in theT ag key section or tag values in the Tag value section to search for instances that have the tags added. |

5. You can use one of the following methods to go to the Instance Details page of an instance
and view the basic information and configurations of the instance: On the Instances page, click the instance ID in the **Instance ID/Name** column. On the Instances page, click **Manage** in the **Actions** column.

#### 4.5.2 Modify the attributes of an instance

After you create an instance, you can modify the name, description, and user data of the instance based on your business requirements.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and then choose **Instance Settings > Modify Instance Properties**.
5. In the **Modify Instance Properties** dialog box, modify the following parameters of the
instance:
**Instance Name**: The name of the instance. The name must be 2 to 128 characters in
length. The name must start with a letter and cannot start with `http://` or `https://` . The name can contain letters, digits, periods (.), underscores (_), hyphens (-), and colons (:).
**Hostname**: The hostname that is displayed in the operating system. Take note of the
following items: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For Windows instances, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). For Linux instances, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-).
**Instance Description**: The description of the instance. The description must be 2 to 256
characters in length and cannot start with `http://` or `https://` . The description can contain letters, digits, periods (.), underscores (_), and hyphens (-).
**User Data**: The user data of the instance. For information about user data, see Instance
user data.
6. Click **OK**.

#### 4.5.3 Reset the logon password of an instance

**instance**

If you did not set a logon password when you created an Elastic Compute Service (ECS) instance or if you have forgotten the password, you can reset the password.

**Limits**

Logon passwords cannot be reset for ECS instances that are created from the arm_neokylin_7u6_64_20G_20210205.raw or arm_centos_7_6_64_20G_20210205.raw image. You can bind key pairs to the instances for logons. For more information, see Bind a key pair to an instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage and use one of the following methods to reset
its logon password: Reset the logon password on the Instance Details page. Click the instance ID in the **Instance ID/Name** column. In the upper-right corner of the Instance Details page, choose **More > Reset Instance Password**. Click **Manage** in the **Actions** column. In the upper-right corner of the Instance Details page, choose **More > Reset Instance Password**. In the **Actions** column, click the icon and then choose **Password/Key Pair > Reset**
**Instance Password**.
5. Enter and confirm a new password and click **OK**.
The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - _ + = | { }

```
[ ] : ; ' < > , . ? /
```

The passwords of Windows instances cannot start with a forward slash (/).

> **Important:** If instances run Unity Operating System (UOS), NFS, or Kylin operating systems, the following limits on passwords apply:
> NFS: For an instance that uses the NFS_V4_G195_x86_20G image, the password must be at least eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" | cracklib-check command to check whether the password meet this requirement. Supported

| ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < _ |   |
|---|---|

```
> , . ? /
```

> UOS:
> For an instance that uses the uos_server20_1032d_x64_20G or arm_uos_server20_1032d_20G image, the password must be 8 to 512 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words from the cracklib dictionary, and you can run the echo "xxx" | cracklib-check command to check whether the password meets this requirement. The monotonic character sequences in the password can be up to four characters in length. Example: 1234. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - _ + = |

```
{ } [ ] : ; ' < > , . ? /
```

> For an instance that uses the uos_server20_1040d_x64_20G or arm_uos_server20_1040d_20G image, the password must be 8 to 512 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words from the cracklib dictionary, and you can run the echo "xxx" | cracklib-check command to check whether the password meets this requirement. The monotonic character sequences in the password can be up to three characters in length. Example: 123. The number of consecutive identical characters in the password cannot exceed three. Example: aaa. Supported special characters include ( ) `

```
~ ! @ # $ % ^ & * - _ + = | { } [ ] : ; ' < > , . ? /
```

> Kylin: For an instance that uses a Kylin image, the password must be at least eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain words that are included in the cracklib dictionary, and you can run the echo "xxx" | cracklib-check command to check whether the password meets this requirement. Supported special characters include ( ) ` ~

|   | ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / _ |
|---|---|

6. Restart the instance in the ECS console or by calling an API operation for the new password
to take effect. For more information, see RebootInstance in the **ECS Developer Guide** or Restart an instance.

#### 4.5.4 Change the VNC password

If you use Virtual Network Computing (VNC) to connect to an Elastic Compute Service (ECS) instance for the first time or if you forget the VNC password, you can change the VNC password.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance whose VNC password you want to change and use one of the
following methods to change the VNC password: On the Instance Details page, change the VNC password. On the Instances page, click the ID of the instance in the **Instance ID/Name** column. In the upper-right corner of the Instance Details page, choose **More > Reset VNC**
**Password**.
On the Instances page, click **Manage** in the **Actions** column. In the upper-right corner of the Instance Details page, choose **More > Reset VNC Password**. In the **Actions** column, click the icon and choose **Password/Key Pair > Reset VNC**
**Password**.
5. In the **Reset VNC Password** dialog box, enter and confirm a new password and then click
**OK**.
The password must be eight characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ! @ ~ ` # $ % ^ * ( ) _ - + = { [ } ] : ; , . ? /

```
| \
```

> **Note:** If your instance is a non-I/O optimized instance, you must restart the instance in the ECS console for the new password to take effect.

#### 4.5.5 Enable and disable release protection for instances

**for instances**

You can enable release protection for Elastic Compute Service (ECS) instances to prevent manual release. This topic describes how to enable and disable release protection for ECS instances and how to check whether release protection is enabled for an instance.

**Background information**

The release protection feature cannot prevent the automatic release of instances that is triggered by normal reasons, such as the following ones: The automatic release time that you set for the instance arrives. The instance does not comply with applicable security compliance policies. The instance was automatically created by Auto Scaling and is removed during subsequent scale-in events.

**Enable release protection when you create an instance**

This section describes how to enable release protection when you create an instance. For more information about how to create an instance, see Create an instance by using the provided wizard.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Instances** page, click **Create Instance**.
5. In the **Basic Settings** step, configure parameters based on your needs and click **Next**.
6. In the **Network Settings** step, configure parameters based on your needs and click **Next**.
7. In the **System Configurations** step, turn on **Instance Release Protection**, configure
other parameters based on your needs, and then click **Next**.
8. In the **Confirmation** step, confirm the configurations and click **Submit**.

**Change the release protection settings**

You can enable or disable release protection for an instance by modifying the attributes of the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and then choose **Instance Settings > Change Release Protection Settings**.
5. In the dialog box that appears, optionally select **Release Protection**.
6. Click **OK**.

**Check whether release protection is enabled for an instance**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Instances** page, use one of the following methods to view details of an instance:
In the **Instance ID/Name** column, click the ID of the instance. Find the instance and click **Manage** in the **Actions** column.
5. On the **Instance Details** tab, check the **Release Protection** parameter in the
**Configurations** section. If the value is Yes, release protection is enabled. If the value is no,
release protection is disabled.

#### 4.5.6 Instance user data

The user data feature provided by Elastic Compute Service (ECS) allows you to customize the startup behaviors of instances and pass data into instances.

**Background information**

This feature is applicable to both Windows and Linux instances. You can use this feature to perform the following operations: Run scripts during instance startup. Pass user data as common data into an ECS instance for future reference.

**Usage notes**

The user data feature can be used only when instances meet the following requirements: Network type: Virtual Private Cloud (VPC) Image: a system image or a custom image that is derived from a system image Operating system: one of the operating systems listed in Supported operating systemsTable 1. Supported operating systems

| Windows | Linux |
|---|---|
| Windows Server 2016 64-bit Windows Server 2012 64-bit Windows Server 2008 64-bit | CentOS Ubuntu SUSE Linux Enterprise OpenSUSE Debian Aliyun Linux |

To configure user data scripts, enter user data based on the operating system type and script type.

> **Note:** Only English characters are supported.

If your data is Base64-encoded, select **Enter Base64 Encoded Information** .

> **Note:** The size of the user data script cannot exceed 16 KB before Base64 encoding.

For Linux instances, the script format must meet the requirements described in Types of user data scripts for Linux instances. For Windows instances, the scripts must start with `[bat]` or `[powershell]` . After an instance is started, run commands to view the following information: Execution results of the user data script Data that is passed into the instance
**Console**: You can modify the user data of instances in the console. The type of the
modified user data script determines whether the script needs to be re-executed. For example, if the `bootcmd` script in **Cloud Config** is modified for Linux instances, the script is automatically executed each time the instances are restarted.
**API**: You can also call API operations to work with instance user data. For more information,
see **CreateInstance** and **ModifyInstanceAttribute** in **ECS Developer Guide**.

**User data scripts of Linux instances**

User data scripts for Linux instances are implemented based on the cloud-init architecture. The scripts are used to complete automated configurations of Linux instances. User data scripts are compatible with cloud-init.

**Description of user data scripts for Linux instances**

User data scripts for Linux instances are executed after the instances are started but before `/etc/init` is executed. By default, user data scripts for Linux instances can only be executed with root permissions.

**Types of user data scripts for Linux instances**

**User-Data Script**

Description: the script that is used to customize configurations, such as a shell script. Format: The first line must start with #! . Example: #!/bin/sh . Limit: The script including the first line is limited to 16 KB in raw form before it is Base64encoded. Frequency: The script is executed only when instances are started for the first time. Example:

```
#!/bin/sh
echo "Hello World. The time is now $(date -R)!" | tee /root/output10.txt
```

**Cloud Config Data**

Description: the predefined data that is used to configure services, such as specifying YUM repositories or importing SSH keys. Format: The first line must be `#cloud-config` . Limit: The script including the first line is limited to 16 KB in raw form before it is Base64encoded. Frequency: The script execution frequency varies based on the specific service. Example:

```
#cloud-config
apt: primary:
- arches: [default]
uri: http://us.archive.ubuntu.com/ubuntu/
```

**Include**

Description: The configuration content in the script can be saved as a text file and passed into cloud-init as a URL. Format: The first line must be `#include` . Limit: The script including the first line is limited to 16 KB in raw form before it is Base64encoded. Frequency: The script execution frequency varies based on the script type in the text file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/cloudconfig
```

**GZIP format**

Description: cloud-init limits the size of each user data script to 16 KB. If the size of a file exceeds 16 KB, you can compress the file before you pass it into the user data script. Format: The .gz file is passed into the user data script as a URL in `#include` . Frequency: The script execution frequency varies based on the script content contained in the GZIP file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/config.gz
```

**View the user data of a Linux instance**

To view the user data of a Linux instance, run the following command in the instance:

```bash
curl http://100.100.100.200/latest/user-data
```

**User data scripts for Windows instances**

User data scripts for Windows instances are developed by Alibaba Cloud and can be used to initialize Windows instances. The following types of user data scripts for Windows instances are available: Batch processing program: The first line starts with `[bat]` . The script is limited to 16 KB in raw form before it is Base64-encoded. PowerShell script: The first line starts with `[powershell]` . The script is limited to 16 KB in raw form before it is Base64-encoded.

**View the user data of a Windows instance**

To view the user data of a Windows instance, run the following PowerShell command in the instance:

```
Invoke-RestMethod http://100.100.100.200/latest/user-data/
```

### 4.6 Manage the instance recycle bin

**bin**

#### 4.6.1 Set the retention period

When you put Elastic Compute Service (ECS) instances into the recycle bin, the instances enter a retention period. This topic describes how to set the retention period.

**Prerequisites**

Only the admin account can set the retention period.

**Background information**

When an instance enters a retention period, its computing resources (CPU and memory) are released, its elastic IP address is disassociated, but its storage resources are retained. When the retention period expires, the ECS instance and its storage resources are completely destroyed and cannot be recovered. The default retention period is three days. You can set an appropriate retention period of up to 30 days and 23 hours based on your business requirements. The retention period can be configured for the recycle bin instead of a specific instance.

> **Important:** After you set the retention period, instances in the recycle bin are completely destroyed and cannot be recovered after the retention period expires.

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Recycle Bin**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Recycle Bin page, click **Set Retention Period**.
5. In the **Set Retention Period** dialog box, specify a period of time and click **OK**.

**Result**

You can view the retention period above the instance list on the Recycle Bin page.

#### 4.6.2 Restore an instance

When you place Elastic Compute Service (ECS) instances into the recycle bin, the instances enter a retention period. During the retention period, you can restore the instance anytime based on your business requirements.

**Background information**

When instances are restored from the recycle bin, computing resources (vCPUs and memory) are automatically re-assigned to the instances. If the instances require elastic IP addresses (EIPs), you must manually associate EIPs with the instances. For more information, see the
**Associate an EIP with an ECS instance** topic in the **EIP User Guide**.

> **Note:** When you delete instances to the recycle bin, their computing resources are automatically reclaimed. Your attempt to restore instances from the recycle bin may fail due to insufficient quotas or computing resources. Before you restore instances, make sure that your quotas and computing resources are sufficient.

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Recycle Bin**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Restore an instance from the recycle bin.
Use one of the following methods to restore the instance from the recycle bin: To restore a single instance, find the instance in the recycle bin and click **Restore** in the Actions column. In the message that appears, click **OK**. To restore one or more instances at a time, select the instances and click **Restore** in the lower-left corner of the page. In the message that appears, click **OK**.

#### 4.6.3 Permanently delete instances

You can permanently delete the instances that you no longer need from the recycle bin. This topic describes how to permanently delete instances.

**Background information**

The instances that are permanently deleted cannot be restored. Make sure that your business is not interrupted before you permanently delete instances.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Recycle Bin**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the instance list, view information about all instances in the retention period, including
the **instance ID, instance name**, **instance type**, and **automatic release time** of the instances.
5. Permanently delete instances from the recycle bin.
You can use one of the following methods to permanently delete instances: To delete a single instance, click **Permanently Delete** in the Actions column corresponding to the instance. In the message that appears, click **Delete**. To delete one or more instances at a time, select all instances that you want to delete, and then click **Permanently Delete** in the lower-left corner of the Instances page. In the message that appears, click **Delete**.

### 4.7 Change the instance type

#### 4.7.1 Upgrade or downgrade the instance type of an instance

**type of an instance**

If the instance type of an Elastic Compute Service (ECS) instance does not meet your application requirements, you can change the instance type. This topic describes how to upgrade or downgrade the instance type of an instance.

**Prerequisites**

The instance whose instance type you want to upgrade or downgrade is in the **Stopped** state.

> **Note:** Service interruptions may occur when you stop instances. We recommend that you stop instances during off-peak hours.

**Limits**

The following limits apply when you upgrade or downgrade the instance type of an instance: When you upgrade or downgrade the instance to a new instance type, the instance specifications including the vCPU, memory, and internal bandwidth specifications are changed together. These specifications cannot be separately changed. Two consecutive instance type changes of an instance must be at least 10 minutes apart.

> **Warning:** When you change the instance type of an instance, the underlying information such as CPU FLAGS of the instance may change and your application authorization codes may become invalid.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and then click **Upgrade/Downgrade**.
5. On the **Modify ECS instance** page, select a different instance type and click **Submit**.
6. Start the instance in the ECS console or by calling an API operation for the new instance
type to take effect. For more information, see **StartInstance** in the **ECS Developer Guide** or Start an instance.

#### 4.7.2 Perform a hot configuration change to change the instance type of an instance

**change the instance type of an instance**

You can change the instance type of an Elastic Compute Service (ECS) instance to meet your application requirements for vCPUs, memory, and internal bandwidth. Compared with the instance type change feature, the hot configuration change feature allows you to change the instance type of an ECS instance without the need to stop the instance.

**Prerequisites**

The ECS instance supports the hot configuration change feature. **Support Hot**
**Configuration Changes** is turned on when the ECS instance is created in the ECS console.
For more information, see Create an instance by using the wizard.

> **Note:** Instance types that support the hot configuration change feature are displayed in the ECS console.

**Limits**

When you perform a hot configuration change to change the instance type of an ECS instance, the following limits apply: ECS instances that run Windows and Debian do not support the hot configuration change feature. When you upgrade or downgrade an ECS instance to a different instance type, the instance specifications including the vCPU, memory, and internal bandwidth specifications are changed at the same time and cannot be separately changed. You can perform up to four hot configuration changes in sequence for an ECS instance. After you restart, stop, or start the ECS instance, the hot configuration change count is reset to zero. After a hot configuration change on the ECS instance fails, you cannot perform hot configuration changes on the ECS instance. If you enabled non-uniform memory access (NUMA) on physical machines in an ECS cluster, the hot configuration change feature of ECS instances that are created in the cluster has only proof of concept (PoC) capabilities. Before you upgrade an ECS instance to a different instance type, log on to the instance and run the `free -m` command to check the amount of remaining memory. You can perform an upgrade operation on the instance only if the total amount of `free` and `available` memory is greater than or equal to the value calculated by using the following formula: 80 M + N × 64 M. If you perform a hot configuration change to upgrade the instance type of an ECS instance that does not have sufficient available memory, an out of memory (OOM) error may occur on the instance and affect your business. The following section describes the parameters in the preceding formula: 80 M: the minimum safe water level. N × 64 M: The ratio of the amount of available memory to the amount of hot-swap memory, which is indicated by the size value, is 1:64. When you upgrade an ECS instance to a different instance type, each additional GB of memory requires an additional 64 M of available memory.

> **Warning:** When you perform a hot configuration change, the underlying information of the ECS instance such as CPU FLAGS may change, As a result, your application authorization codes may become invalid.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance that you want to manage. In the **Actions** column, choose
> **Hot**

**Configuration Change**.
5. In the **Hot Configuration Change** dialog box, select a desired instance type and click **OK**.

### 4.8 Replace the operating system of an instance

**of an instance**

When you use an Elastic Compute Service (ECS) instance, you can replace the operating system based on your business requirements. This topic describes how to replace the operating system of an ECS instance.

**Prerequisites**

After the operating system of an instance is replaced, the original system disk is released and its data is lost and cannot be restored. We recommend that you back up data before you replace an operating system. For more information, see Create snapshots. The instance is in the Stopped state. If the instance is not stopped, stop the instance. For more information, see Stop instances.

**Usage notes**

Risks may arise when you replace the operating system of an instance. Before you perform this operation, take note of the following items: After you replace the operating system of an instance, a new system disk is assigned to the instance. The system disk ID changes, and the original system disk is released. Data stored on the original system disk is lost and cannot be restored. The category of the system disk, the IP addresses of the instance, and the media access control (MAC) addresses of the elastic network interfaces (ENIs) that are bound to the instance remain unchanged. After you replace the operating system of an instance, you must redeploy environments on the new system disk to run services. The snapshots of the original system disk cannot be used to roll back the new system disk, but can be used to create custom images. Take note of the following items about the snapshots based on the snapshot type: The manual snapshots of the original system disk are not automatically released. If **Delete Automatic Snapshots While Releasing Disk** is enabled for the original system disk, the automatic snapshots of the disk are automatically released along with the disk. If **Delete Automatic Snapshots While Releasing Disk** is not enabled for the original system disk, the automatic snapshots of the disk are automatically retained. If you want to replace Windows Server operating systems with Linux operating systems or replace Linux operating systems with Windows Server operating systems, take note of the following items: Make sure that the **hostname** of the instance meets the requirements of the replacement operating system, and delete invalid characters. For information about how to change the hostname, see **ModifyInstanceAttribute** in the **ECS User Guide** or Modify the attributes of an instance. If you want to replace the operating system of an instance with a Windows Server operating system, take note of the following items: Make sure that the system disk has at least 1 GiB of available space reserved. Otherwise, the instance may not be able to start after the operating system is replaced. If your instance is a non-I/O optimized instance, you cannot replace the operating system of the instance in the ECS console. You can only call the ReplaceSystemDisk operation to replace the operating system by using a specific Windows Server public image. For more information about **ReplaceSystemDisk**, see **ECS Developer Guide**. For more information, see Image overview.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance for which you want to replace the operating system and choose
>
**Disks and Image > Replace Operating System** in the **Actions** column.
5. In the **Replace Operating System** dialog box, specify the information of the new
operating system.

| Parameter | Description |
|---|---|
| Image Type | Select an image type for the new operating system. Valid values: Public Image Custom Image Shared Custom Image |
| Image ID | Enter the ID of the new image. |
| System Disk (GB) | Specify the capacity of the new system disk based on your business requirements and the image limits. The minimum disk capacity is determined by the original disk capacity and the image type, while the maximum disk capacity is 500 GB. Linux Capacity limit (GB): [Max{20, Original disk capacity}, 500] Windows Capacity limit (GB): [Max{40, Original disk capacity}, 500] |

6. Click **OK**.
7. Restart the instance by using the ECS console or calling an API operation for the new
operating system to take effect. For more information, see **StartInstance** in the **ECS Developer Guide** or Start an instance.

**View the results**

On the Instance Details page, you can view the new operating system of the instance.

### 4.9 View the monitoring information of an instance

**information of an instance**

You can view monitoring charts in the CloudMonitor console to learn about the running conditions of Elastic Compute Service (ECS) instances. This topic describes how to go to the CloudMonitor console to view the monitoring information of an ECS instance.

**Background information**

CloudMonitor provides real-time monitoring, alerting, and notification services for resources to protect your services and business. For more information, see **CloudMonitor > Overview** in the Apsara Uni-manager Management Console User Guide in the Apsara Stack Documentation Center.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. View the monitoring information of an instance in the **Monitoring** panel or on the
**Monitoring** tab.
**Monitoring** panel: In the instance list, find the ECS instance whose monitoring
information you want to view and click the icon in the **Monitoring** column.
**Monitoring** tab:
a. On the Instances page, click the instance ID in the **Instance ID/Name** column. b. On the Instance Details page, click the **Monitoring** tab. You can view the monitoring information that is described in the following table in the
**Monitoring** panel or on the **Monitoring** tab.

> **Note:** You can also click **More** to go to the CloudMonitor console and view the details of the monitoring information of the instance. The following table describes the monitoring information.

| Item | Description |
|---|---|
| Monitoring type | The monitoring information of an ECS instance includes basic monitoring information and monitoring information about the instance operating system, GPUs, processes, disks, and networks. |
| Monitoring period | You can specify a period of time during which monitoring data is collected. Valid values: Hourly monitoring periods: 1 Hour, 3 Hours, 6 Hours, and 12 Hours Daily monitoring periods: 1 Day, 3 Days, 7 Days, and 14 Days Custom: Specify the start time and the end time to define a monitoring period based on your business requirements. You can specify the previous 5, 10, or 15 minutes as the monitoring period. |

| Monitoring metric | For information about monitoring metrics, see Cloud Monitor Service > Cloud service monitoring > Metrics in the Apsara Uni-manager M anagement Console User Guide in the Apsara Stack Documentation Center. Note By default, the average values of each monitoring metric are displayed. You can select Maximum or Minimum Value from the drop-down list of a monitoring metric to view the maximum or minimum values. |
|---|---|

### 4.10 Add an instance to a security group

**group**

You can add Elastic Compute Service (ECS) instances to security groups and configure security group rules to manage network access for the instances.

**Prerequisites**

The destination security groups and the instances must reside in the same virtual private cloud (VPC).

**Background information**

Security groups are used as virtual firewalls to provide security isolation and implement network access control for instances. Security groups determine whether the instances in the same account that are deployed in the same VPC and region can connect to each other over the internal network. By default, if the instances belong to the same security group, they can connect to each other over the internal network. If the instances belong to different security groups, you can authorize mutual access between the security groups to allow the instances to connect to each other over the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group to which you want to add an instance. In the **Actions** column, click
the icon and then select **Manage Instances**.
5. Click **Add Instance**.
6. In the Add Instance dialog box, select an instance and click **OK**.
An instance can belong to up to five security groups. After an instance is added to a security group, the rules of the security group automatically take effect on the instance.

### 4.11 Change the private IP address of an instance

**address of an instance**

Each instance is assigned a private network interface and associated with a private IP address. You can change the private IP address of an instance. The new private IP address must be within the CIDR block of the vSwitch to which the instance is connected and must not be in use by another instance.

**Prerequisites**

The instance is in the **Stopped** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and then choose **Network and Security Group > Change Private IP Address**.
5. Enter a new private IP address.
The new private IP address must be within the CIDR block of the vSwitch to which the instance is connected. The IP address must not be in use by another instance or be reserved for specific purposes. For example, if the CIDR block of the vSwitch is 192.168.1.0/24, you can use an IP address in the range of 192.168.1.1 to 192.168.1.254. The first address 192.168.1.0 is reserved to identify the subnet itself, and the last address 192.168.1.255 is reserved as the broadcast address. You can use neither of the first address and the last address.
6. Click **OK**.

### 4.12 Assign an IPv6 address to an instance

**instance**

Compared with IPv4 addresses, IPv6 addresses are more sufficient and allow more types of devices to access the Internet. If your network environment supports IPv6, you can assign IPv6 addresses to exiting Elastic Compute Service (ECS) instances. This topic describes how to assign an IPv6 address to an ECS instance.

**Prerequisites**

The vSwitch and virtual private cloud (VPC) of the ECS instance are associated with an IPv6 CIDR block. For more information, see **Create an IPv6 VPC** in the **Apsara Stack VPC**
**User Guide**.
The instance family of the ECS instance supports IPv6.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and then choose **Network and Security Group > Manage Secondary Private IP**
**Addresses**.
5. In the **Manage Secondary Private IP Addresses** dialog box, click **Enable** next to the
**IPv6 Addresses** parameter.

> **Note:** Specific instance families do not support IPv6.

6. On the vSwitch details page, check whether IPv6 is enabled for the vSwitch.
If IPv6 is not enabled for the vSwitch, click **Open IPv6** next to the **IPv6 network segment** parameter.
7. In the **Manage Secondary Private IP Addresses** dialog box, click **OK**.

**Result**

After the configuration is complete, you can click the ID of the instance to go to the **Instance**
**Details** page and view the **IPV6** parameter to check whether an IPv6 address is assigned to
the instance.

### 4.13 Export a list of instances

You can export a list of Elastic Compute Service (ECS) instances based on your business requirements in the ECS console and download and save the list only as a `.xlsx` file to your computer.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the ECS instance list, select one or more instances and click the
icon in the upperright corner.

> **Note:** To export a list of all ECS instances, click the
> icon in the upper-right corner without
> selecting ECS instances.

5. In the **Export** dialog box, configure the parameters to specify the scope of the instance list
that you want to export.

| Parameter | Description |
|---|---|
| Export Data by Scope | All: exports a list of all ECS instances. Selected Data: exports a list of specific ECS instances. |
| Columns to Export | Select the columns that you want to export. You must select Instance ID/Name. |

6. Click **OK**.
If you export a list of a small number of ECS instances, the system automatically downloads the exported file on the current page to your computer. If you export a list of a large number of ECS instances, go to the Download Report page in the Operations console and download the exported file to your computer.

> **Important:** The default threshold for the number of ECS instance that can be included in the exported list is 500. You can contact Alibaba Cloud technical support to modify the threshold.

| Number of ECS instances | Download operation |   | Exported file |   |
|---|---|---|---|---|
| ≤ 500 | The system automatically exports instance data as configured and downloads the exported file to your computer. |   | Information about the exported file: File name: ecs instance _ _ XXX . File format: .xlsx . File content: instance information, such as instance IDs, instance names, operating systems, instance status, instance descriptions, regions, organizations, resource sets, and zones. |   |
| > 500 | i. In the The report export task is created. dialog box, click Go to Download Center. ii. On the Download Report page, find the exported file that you want to download and click Download Report in the Actions column. The system automatically downloads the exported file to your computer. |   |   |   |

### 4.14 Manage NVIDIA drivers

#### 4.14.1 Installation guideline for NVIDIA drivers

**drivers**

If drivers are not configured for your GPU-accelerated instances, you must install NVIDIA drivers on your instances. The driver types that you can install on the instances may vary based on the scenarios and instance types. This topic describes how to select GPUaccelerated instance types during instance creation and install NVIDIA drivers on GPUaccelerated instances in different scenarios.

**GPU-accelerated instance types**

Select suitable GPU-accelerated instance types during instance creation. For information about GPU-accelerated instance types, see the **ECS Instance Families & Instance Types**.

> **Note:** You can manage GPU-accelerated instances in the same manner that you manage non-GPU-accelerated instances, except for the drivers that are required by GPU- accelerated instances.

**Drivers**

You can install the following NVIDIA drivers on GPU-accelerated instances: GPU driver: drives physical GPUs. GRID driver: accelerates graphics processing.

**Install drivers on vGPU-accelerated instances**

vGPU-accelerated instances, such as vgn6i instances, use vGPUs. You can install only GRID drivers on vGPU-accelerated instances. Specific GPU-related features may be unavailable for the vGPU-accelerated instances because NVIDIA GRID licenses are not activated for the GPUs that the instances use. You must install GRID drivers and activate GRID licenses on the instances to use the GPU-related features. The following table describes the driver types that you can install on vGPU-accelerated instances for different scenarios.

| Operating system | Driver type | Recommended scenario | References |
|---|---|---|---|
| Windows Server | GRID drivers | Graphics computing scenarios, such as Open Graphics Library (OpenGL) and Direct3D scenarios | Install a GRID driver on a GPU-accelerated Windows instance |
| Linux, such as Alibaba Cloud Linux, CentOS, Ubuntu, or SUSE Linux | GRID drivers | Common computing scenarios, such as deep learning and AI | Install a GRID driver on a vGPU-accelerated Linux instance |

**Install drivers on GPU-accelerated compute-optimized**

**instances**

The following table describes the driver types that you can install on GPU-accelerated compute-optimized instances for different scenarios.

| Operating system | Driver type | Recommended scenario | References |
|---|---|---|---|
| Linux, such as Alibaba Cloud Linux, CentOS, Ubuntu, or SUSE Linux | GPU drivers | Common computing scenarios, such as deep learning, AI, and scientific computing | Install a GPU driver on a GPU-accelerated compute- optimized Linux instance |
|   | GPU drivers | Graphics computing scenarios, such as OpenGL and Direct3D scenarios | Install a GPU driver on a GPU-accelerated compute- optimized Linux instance |
| Windows Server | GPU drivers | Common computing scenarios, such as deep learning, AI, and scientific computing | Install a GPU driver on a GPU-accelerated compute- optimized Windows instance |
|   | GRID drivers | Graphics computing scenarios, such as OpenGL and Direct3D scenarios | Install a GRID driver on a GPU-accelerated Windows instance |

#### 4.14.2 Install a GPU driver

##### 4.14.2.1 Install a GPU driver on a GPU-accelerated compute-optimized Linux instance

**compute-optimized Linux instance**

After you create a GPU-accelerated compute-optimized instance from an image for which a GPU driver is not pre-installed, install a GPU driver to use the instance. This topic describes how to install a GPU driver on a GPU-accelerated compute-optimized Linux instance.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance.

**Background information**

GPU-accelerated instances support only GPU drivers that are suitable for the operating systems of the instances. This topic describes how to install a GPU driver on a GPUaccelerated compute-optimized Linux instance.

> **Note:** If your GPU-accelerated compute-optimized instance runs Windows, perform the operations that are described in Install a GPU driver on a GPU-accelerated compute- optimized Windows instance to install a GPU driver on the instance.

1. Download a GPU driver.
i. Visit the NVIDIA Driver Downloads page on the NVIDIA official website.

> **Note:** For information about how to install and configure NVIDIA drivers, see NVIDIA Driver Installation Quickstart Guide.

ii. Configure filters and click **SEARCH** to search for a driver that is suitable for your instance. The following table describes the filters.

| Filter | Description | Example |
|---|---|---|

| Product Type Product Series Product | Configure Product Type, Product Series, and Product based on the GPUs with which your GPU-accelerated compute- optimized instance is equipped. For information about how to view instance specifications, see View instance information. For information about the GPUs that are supported by each instance type, see the Heterogeneous computing and heterogeneous ECS Bare Metal Instance families topics in the ECS Instance Families and Instance Types | Data Center / Tesla P-Series Tesla P100 |
|---|---|---|
| Operating System | Select a Linux operating system version based on the image of the instance. If the Operating System drop-down list does not contain the operating system that your instance runs, click Show All Operating Systems in the lower part of the drop-down list. If you cannot find a Linux version that matches the image of the instance, select Linux 64-bit. | Linux 64-bit |
| CUDA Toolkit | Select a CUDA Toolkit version. | 11.2 |
| Language | Select a language for the driver. | Chinese (Simplified) |
| Recommended/B eta | By default, All is selected. You can use the default setting. | All |

iii. In the search result, find the driver version that you want to download, and then click the driver name. iv. On the details page of the driver, click **Download**. On the **Download** page, right-click
**Download** and select **Copy link address**.
2. Connect to the instance.
For more information, see Instance connecting overview.
3. Run the `wget` command that contains the download link address that you copied in **Step**
**1** to download the driver installation package. Sample command:

```
wget https://cn.download.nvidia.com/tesla/460.73.01/NVIDIA-Linux-x86_64-460.73.01.run
```

4. Install the GPU driver.
The operations that you must perform to install the GPU driver vary based on the operating system of the instance.

**CentOS**

i. Run the following command to check whether the kernel-devel and kernel-headers packages are installed on the GPU-accelerated compute-optimized instance:

```
rpm -qa | grep $(uname -r)
```

If the command output includes the version information of the kernel-devel and kernelheaders packages, the packages are installed. Sample command output:

```
kernel-3.10.0-1062.18.1.el7.x86_64 kernel-devel-3.10.0-1062.18.1.el7.x86_64 kernel-headers-3.10.0-1062.18.1.el7.x86_64
```

If the command output does not include the version information of the kernel-devel (ke rnel-devel-*) and kernel-headers (kernel-headers-*) packages, install the packages. For more information, see kernel-devel and kernel-headers.

> **Important:** Make sure that the version of the kernel-devel package is the same as the version of the kernel. Otherwise, a compilation error occurs when you install RPM Package Manager for your driver. Check the version number of kernel-* in the command output before you download kernel-devel. In the preceding command output, the version number of the kernel is 3.10.0-1062.18.1.el7.x86_64.

ii. Grant permissions and install the GPU driver. In this example, a Linux 64-bit driver package in the .run format is downloaded. Example: NVIDIA-Linux-x86_64-xxxx.run. Run the following commands to grant permissions on the GPU driver and install the GPU driver:

```
chmod +x NVIDIA-Linux-x86_64-xxxx.run sh NVIDIA-Linux-x86_64-xxxx.run
```

iii. Run the following command to check whether the driver is installed:

```
nvidia-smi
```

The following command output indicates that the GPU driver is installed. iv. Install NVIDIA Fabric Manager. Make sure that the version of NVIDIA Fabric Manager matches your driver version. You must install an NVIDIA Fabric Manager version that matches your driver version only for ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, and ecs.sccgn7ex instances. Otherwise, you cannot use the instances as expected.

> **Important:** If your instance is a GPU-accelerated compute-optimized instance that does not belong to the ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, or ecs.sccgn7ex instance family, skip this step.

a. Install NVIDIA Fabric Manager. You can install NVIDIA Fabric Manager by using the source code or an installation package. The commands that are required to install NVIDIA Fabric Manager vary based on the instance operating system. The following example shows how to install driver version 460.91.03 on CentOS 7.x and CentOS 8.x. Set `driver_version` to the driver version that you downloaded in **Step 1**.

**Source code**

CentOS 7.x

```bash
driver_version=460.91.03 yum -y install yum-utils yum-config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/cuda-rh el7.repo yum install -y nvidia-fabric-manager-${driver_version}-1
```

CentOS 8.x

```
driver_version=460.91.03 driver_version_main=$(echo $driver_version | awk -F '.' '{print $1}') distribution=rhel8 ARCH=$( /bin/arch ) dnf config-manager --add-repo http://developer.download.nvidia.com/compute/cuda/repos/$distribution/${ARCH}/c a-$distribution.repo dnf module enable -y nvidia-driver:${driver_version_main} dnf install -y nvidia-fabric-manager-0:${driver_version}-1
```

**Installation package**

CentOS 7.x

```
driver_version=460.91.03 wget http://mirrors.cloud.aliyuncs.com/nvidia-cuda/rhel7/x86_64/nvidia-fabric -manager-${driver_version}-1.x86_64.rpm rpm -ivh nvidia-fabric-manager-${driver_version}-1.x86_64.rpm
```

CentOS 8.x

```
driver_version=460.91.03 wget http://mirrors.cloud.aliyuncs.com/nvidia-cuda/rhel8/x86_64/nvidia-fabric -manager-${driver_version}-1.x86_64.rpm rpm -ivh nvidia-fabric-manager-${driver_version}-1.x86_64.rpm
```

b. Run the following commands to start NVIDIA Fabric Manager:

```bash
systemctl enable nvidia-fabricmanager systemctl start nvidia-fabricmanager
```

c. Run the following command to check whether NVIDIA Fabric Manager is installed:

```bash
systemctl status nvidia-fabricmanager
```

The following command output indicates that NVIDIA Fabric Manager is installed.

**Ubuntu and other operating systems**

i. Grant permissions and install the GPU driver. In this example, a Linux 64-bit driver package in the .run format is downloaded. Example: NVIDIA-Linux-x86_64-xxxx.run. Run the following commands to grant permissions on the GPU driver and install the GPU driver:

```
chmod +x NVIDIA-Linux-x86_64-xxxx.run sh NVIDIA-Linux-x86_64-xxxx.run
```

ii. Run the following command to check whether the driver is installed:

```
nvidia-smi
```

The following command output indicates that the GPU driver is installed. iii. Install NVIDIA Fabric Manager. Make sure that the version of NVIDIA Fabric Manager matches your driver version. You must install an NVIDIA Fabric Manager version that matches your driver version only for ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, and ecs.sccgn7ex instances. Otherwise, you cannot use the instances as expected.

> **Important:** If your instance is a GPU-accelerated compute-optimized instance that does not belong to the ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, or ecs.sccgn7ex instance family, skip this step.

a. Install NVIDIA Fabric Manager. You can install NVIDIA Fabric Manager by using the source code or an installation package. The following example shows how to install driver version 460.91.03 on Ubuntu 16.04, Ubuntu 18.04, or Ubuntu 20.04. Set `driver_version` to the driver version that you downloaded in **Step 1**.

**Source code**

Ubuntu 16.04, Ubuntu 18.04, or Ubuntu 20.04

```
driver_version=460.91.03 driver_version_main=$(echo $driver_version | awk -F '.' '{print $1}') distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g') wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cud $distribution.pin mv cuda-$distribution.pin /etc/apt/preferences.d/cuda-repository-pin-600 wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/7fa f80.pub apt-key add 7fa2af80.pub rm 7fa2af80.pub echo "deb http://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64 /"
| tee /etc/apt/sources.list.d/cuda.list
apt-get update apt-get -y install nvidia-fabricmanager- ${driver_version_main}=${driver_version}-*
```

**Installation package**

Ubuntu 16.04

```
driver_version=460.91.03 driver_version_main=$(echo $driver_version | awk -F '.' '{print $1}') wget http://mirrors.cloud.aliyuncs.com/nvidia-cuda/ubuntu1604/x86_64/nvidia-f abricmanager-${driver_version_main}_${driver_version}-1_amd64.deb dpkg -i nvidia-fabricmanager-${driver_version_main}_${driver_version}-1_amd64 .deb
```

Ubuntu 18.04

```
driver_version=460.91.03 driver_version_main=$(echo $driver_version | awk -F '.' '{print $1}') wget http://mirrors.cloud.aliyuncs.com/nvidia-cuda/ubuntu1804/x86_64/nvidia-f abricmanager-${driver_version_main}_${driver_version}-1_amd64.deb dpkg -i nvidia-fabricmanager-${driver_version_main}_${driver_version}-1_amd64 .deb
```

Ubuntu 20.04

```
driver_version=460.91.03 driver_version_main=$(echo $driver_version | awk -F '.' '{print $1}') wget http://mirrors.cloud.aliyuncs.com/nvidia-cuda/ubuntu2004/x86_64/nvidia-f abricmanager-${driver_version_main}_${driver_version}-1_amd64.deb dpkg -i nvidia-fabricmanager-${driver_version_main}_${driver_version}-1_amd64 .deb
```

b. Run the following commands to start NVIDIA Fabric Manager:

```bash
systemctl enable nvidia-fabricmanager systemctl start nvidia-fabricmanager
```

c. Run the following command to check whether NVIDIA Fabric Manager is installed:

```bash
systemctl status nvidia-fabricmanager
```

The following command output indicates that NVIDIA Fabric Manager is installed.

##### 4.14.2.2 Install a GPU driver on a GPU-accelerated compute-optimized Windows instance

**compute-optimized Windows instance**

After you create a GPU-accelerated compute-optimized Windows instance, no GPU driver is automatically installed on the instance. Download a GPU driver from the NVIDIA official website and install the driver on the instance to use the instance. This topic describes how to install a GPU driver on a GPU-accelerated compute-optimized Windows instance.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance.

**Background information**

GPU-accelerated instances support only GPU drivers that are suitable for the operating systems of the instances. This topic describes how to install a GPU driver on a GPUaccelerated compute-optimized Windows instance. If your GPU-accelerated computeoptimized instance runs Linux, perform the operations that are described in Install a GPU driver on a GPU-accelerated compute-optimized Linux instance to install a GPU driver on the instance.
1. Connect to the instance.
For more information, see Instance connecting overview.
2. On the remote desktop, visit the NVIDIA Driver Downloads page on the NVIDIA official
website.
3. Configure filters and click **SEARCH** to search for a driver that is appropriate for your
instance. The following table describes the filters.

| Filter | Description | Example |
|---|---|---|
| Product Type Product Series Product | Configure Product Type, Product Series, and Product based on the GPUs with which your GPU-accelerated compute-optimized instance is equipped. For information about how to view instance specifications, see View instance information. For information about the GPUs that are supported by each instance type, see the ECS Instance Families & Instance Types. | Data Center / Tesla P-Series Tesla P100 |
| Operating System | Select a Windows operating system version based on the image of the instance. | Windows 10 64-bit |
| Windows Driver Type | Select a driver type. | Standard |
| CUDA Toolkit | Select a CUDA Toolkit version. | 11.2 |
| Language | Select a language for the driver. | Chinese (Simplified) |
| Recommended/B eta | By default, All is selected. You can use the default setting. | All |

4. In the search result, find the driver version that you want to download, and then click the
driver name.
5. On the details page of the driver, click **Download**. On the **Download** page, click
**Download**.
6. After the driver is downloaded, open the folder in which the driver installation package is
stored. Double-click the installation package and install the driver as prompted.

> **Note:** Windows Remote Desktop Protocol (RDP) does not support applications, such as DirectX and Open Graphics Library (OpenGL) applications, for Windows instances on which the installed GPU drivers are in effect. In this case, you must install the Virtual Network Console (VNC) service and client or use protocols such as PC over IP (PCoIP) and XenDesktop HDX 3D that support the applications.

After you install the driver, you can open Device Manager. In the left-side navigation pane, click Display adapters to check whether the driver is installed. If the driver appears, the driver is installed.

#### 4.14.3 Install a GRID driver

##### 4.14.3.1 Install a GRID driver on a vGPU-accelerated Linux instance

**accelerated Linux instance**

If you create vGPU-accelerated instances, you must install GRID drivers on the instances. If NVIDIA GRID licenses are not activated for the GPUs that are used by GPU-accelerated instances, GPU-related features do not take effect on the instances. You must obtain and activate the GRID licenses to use the features. This topic describes how to install a GRID driver on a vGPU-accelerated Linux instance, activate a GRID license, and test the GRID driver. In the examples, an ecs.vgn6i instance that runs Ubuntu 16.04 64-bit is used.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance. A remote connection tool, such as VNC Viewer, is installed on your computer. A GRID license and a GRID driver installation package are obtained.

> **Note:** The GRID driver version must be suitable for the instance type and region of your vGPU- accelerated instance.

**Background information**

If you use a GPU-accelerated compute-optimized Linux instance, we recommend that you install a GPU driver on the instance. For more information, see Install a GPU driver on a GPUaccelerated compute-optimized Linux instance.

**Install a GRID driver**

1. Disable Nouveau.
Nouveau is an open-source driver that is pre-installed in specific Linux distributions. If Nouveau is installed in the Linux distribution that you use, you must disable the driver before you install another driver. i. Connect to the instance. For more information, see Overview. ii. Run the following command to check whether the blacklist-nouveau.conf file exists:

```
ls /etc/modprobe.d/blacklist-nouveau.conf
```

If the file does not exist, run the following command to create the file:

```
vim /etc/modprobe.d/blacklist-nouveau.conf
```

iii. Add the following information to the blacklist-nouveau.conf file to disable Nouveau.

> **Note:** If the following code is already added to the file, skip this step.

```
blacklist nouveau blacklist lbm-nouveau options nouveau modeset=0
```

iv. Run the following command to check whether the system loads the Nouveau module:

```
lsmod | grep nouveau
```

If the command output is not empty, run the following commands to create kernel initramfs:

```
rmmod nouveau update-initramfs -u
```

If the command output is empty, proceed to the next step. v. Run the following command to restart the instance:

```
reboot
```

2. Install the obtained GRID driver on the instance based on the instance family.
ecs.vgn6i

```
chmod +x NVIDIA-Linux-x86_64-430.63-grid.run ./NVIDIA-Linux-x86_64-430.63-grid.run
```

ecs.vgn6i-vws or ecs.vgn7i-vws

```
chmod +x NVIDIA-Linux-x86_64-460.91.03-grid.run ./NVIDIA-Linux-x86_64-460.91.03-grid.run
```

3. Run the following command to check whether the GRID driver is installed:

```
nvidia-smi
```

If the command output includes the GRID driver information that is shown in the following figure, the driver is installed. In the preceding output, `Driver Version` indicates the GRID driver version and `CUDA` `Version` indicates the latest CUDA version that is supported by the driver version. The following table describes specific GRID driver versions and the latest CUDA versions that are supported by the GRID driver versions.

> **Important:** If a CUDA version is returned after you run the `nvidia-smi` command on a GPU- accelerated instance, the version is the latest CUDA version that is supported by the GRID driver. However, this does not indicate that the CUDA version is installed on the instance. The GRID driver does not include CUDA. You must install the CUDA Toolkit.

| vGPU software version | GRID driver version | Latest CUDA version supported |
|---|---|---|
| 13.5 | 470.161.03 | 11.4 |
| 13.1 | 470.82.01 | 11.4 |
| 12.3 | 460.91.03 | 11.2 |

| 9.4 | 430.99 | 10.1 |
|---|---|---|

4. Add a license server.
i. Run the following command to go to the /etc/nvidia directory:

```
cd /etc/nvidia
```

ii. Run the following command to create the gridd.conf file:

```
cp gridd.conf.template gridd.conf
```

iii. Add the following information about the license server to the gridd.conf file:

```
ServerAddress=<IP address of the license server> ServerPort=<Port of the license server. Default value: 7070.)> FeatureType=1
```

5. Run the following command to restart the instance for the configurations of the license
server to take effect:

```
reboot
```

6. Check whether the license is activated.
i. Connect to the instance. For more information, see Overview. ii. Run the following command to check the status of the license:

```bash
systemctl status nvidia-gridd
```

If the command output includes **License acquired successfully**, the license is activated.

**Test the GRID driver**

The following section describes how to use an OpenGL Extension to the X Window System (GLX) application to test the GRID driver that is installed on a vGPU-accelerated instance. In this example, a vGPU-accelerated instance that runs Ubuntu 16.04 64-bit is used.
1. Prepare an environment to test the GRID driver.
i. Run the following command to install x11vnc:

```
apt-get install x11vnc
```

ii. Run the lspci | grep NVIDIA command to query the GPU BusID. In this example, the GPU BusID is `00:07.0` . iii. Configure the X Server environment and reboot the system. a. Run the `nvidia-xconfig --enable-all-gpus --separate-x-screens` command.

|   | "Section Device" |
|---|---|
| BusID "PCI:0:7:0" |   |

b. Add the obtained value of the BusID parameter to `"Section Device"` in the /etc/X11/xorg.conf file. In this example, `BusID "PCI:0:7:0"` is added. c. Run the `reboot` command to restart the system.
2. Run the following command to install the GLX application:

```
apt-get install mesa-utils
```

3. Run the `startx` command to start X Server.
If the `startx` command is unavailable, run the `apt-get install xinit` command to install xinit. When you run the `startx` command, the `hostname: Name or service not known` error message may appear. The error message does not affect the startup of X Server. You can run the `hostname` command to obtain the hostname of your instance. Then, you can modify the /etc/hosts file by replacing the value of the `hostname` parameter that follows `127.0.0.1` with the hostname of the instance.
4. Start a new terminal session of the SSH client and run the following command to start
x11vnc:

```
x11vnc -display :1
```

The following command output indicates that x11vnc is started. In this case, you can connect to the instance by using a VNC application, such as VNC Viewer.
5. Log on to the ECS console.
6. Add an inbound rule that allows traffic on TCP 5900 port to a security group of the instance.
For more information, see Add a security group rule.
7. On your computer, start the VNC application such as VNC Viewer, enter `public IP address`
`of the instance: 5900` to connect to the instance, and then go to a K Desktop Environment (KDE) desktop.
8. Run the `glxinfo` command to view the configurations that are supported by the current
NVIDIA GRID driver. i. Start another SSH session on a client. ii. Run the `export DISPLAY=:1` command. iii. Run the glxinfo –t command to list the configurations that are supported by the current GRID driver.
9. Run the `glxgears` command to test the GRID driver.
i. On the KDE desktop, right-click anywhere and select **Run Command**. ii. Run the `glxgears` command to start the testing application. If a window that is shown in the following figure appears, the GRID driver works as expected.

##### 4.14.3.2 Install a GRID driver on a GPU-accelerated Windows instance

**accelerated Windows instance**

If you want to run graphics-intensive workloads such as OpenGL and Direct3D on a GPUaccelerated compute-optimized Windows instance or a vGPU-accelerated Windows instance, you must install a GRID driver on the instance. This topic describes how to install a GRID driver and activate a GRID license.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance. A remote connection tool is installed on your computer. A GRID license and a GRID driver installation package are obtained.

> **Note:** The GRID driver version must be suitable for the instance type and region of your vGPU-accelerated instance.

**Background information**

The procedure for installing a GRID driver on a GPU-accelerated Windows instance is the same as the procedure for installing a GRID driver on a vGPU-accelerated Windows instance. This topic describes how to install a GRID driver and activate a GRID license on a vGPUaccelerated instance. In this example, a vgn6i instance that runs Windows Server 2019 is used.
1. Connect to the instance.
For more information, see Connect to a Windows instance from a Windows computer by using Remote Desktop.
2. Install the GRID driver that you obtained.
i. Double-click the installation package. In the dialog box that appears, click **OK**. The package is automatically decompressed. ii. In the **NVIDIA Installer** dialog box, click **AGREE AND CONTINUE**. iii. Accept the default settings and click **NEXT**. iv. After the driver is installed, click **RESTART NOW**.
3. After you restart the instance, connect to the instance and check whether the GRID driver is
installed. i. Connect to the instance. For more information, see Connect to a Windows instance from a Windows computer by using Remote Desktop.

> **Important:** Do not use VNC to connect to the GPU-accelerated instance in the Elastic Compute Service (ECS) console. VNC cannot render GPU output, which results in a black screen.

ii. On your Windows desktop, move the pointer over the icon, right-click the icon, and then click **Device Manager**. iii. In the **Device Manager** dialog box, click **Display adapters** and check whether the GRID driver appears. In this example, an **NVIDIA GRID T4-8Q** driver appears. The following figure shows that the driver is installed.
4. Add a license server and activate the license.
i. On your Windows desktop, right-click anywhere on the screen and select **NVIDIA**
**Control Panel**.
ii. In the left-side navigation pane of the **NVIDIA Control Panel** dialog box, choose
**Licensing > Manage License**.
iii. On the **Manage License** page, enter the IP address and port number of the license server that you obtained and click **Apply**. Reopen the **NVIDIA Control Panel** dialog box. If the message that is shown in the following figure appears, the license is activated.

#### 4.14.4 Uninstall an NVIDIA driver

##### 4.14.4.1 Uninstall a GPU driver

You can uninstall a GPU driver from a GPU-accelerated instance. The commands that you run to uninstall a GPU driver vary based on the installation method of the driver and the operating system of the instance.

**Background information**

You can use GPU-accelerated instances only if the required drivers are installed on the instances. If you uninstall a driver from your instance, install another driver that is suitable for the instance type and operating system to ensure that the instance runs as expected. For more information, see Update an NVIDIA driver. If a GPU driver is automatically installed when you create a GPU-accelerated instance, the operations that you perform to uninstall the driver vary based on the operating system of the instance: Ubuntu: Uninstall a GPU driver by using a .deb package. CentOS or SUSE Linux: Uninstall a GPU driver by using a .run package. For information about how to uninstall GPU drivers from different operating systems, see the following sections in this topic: Windows: Uninstall a GPU driver from Windows Linux: Uninstall a GPU driver from Ubuntu Uninstall a GPU driver from CentOS Uninstall a GPU driver from SUSE Linux

> **Note:** To uninstall a GPU driver from a GPU-accelerated instance that runs Linux, you must log on to the instance as the `root` user. If you are a regular user, run the `sudo` command to obtain the permissions of the `root` user before you proceed.

**Uninstall a GPU driver from Windows**

In this example, a GPU-accelerated compute-optimized gn6i instance that runs Windows Server 2019 is used.
1. Connect to the instance.
For more information, see Overview.
2. In the lower-left corner of a Windows desktop, click the
icon and then click **Control**
**Panel**.
3. In the **Control Panel**, click **Uninstall a program**.
4. Right-click the GPU driver that you want to uninstall and select **Uninstall/Change**.
5. In the **NVIDIA Uninstaller** dialog box, click **UNINSTALL**.
6. After you uninstall the driver, click **RESTART NOW**.
When you restart the instance, the GPU driver is uninstalled.

**Uninstall a GPU driver from Ubuntu**

If you used a .deb installation package to install a GPU driver on an instance that runs Ubuntu, we recommend that you perform the following operations to uninstall the GPU driver. In this example, NVIDIA driver 410.104, CUDA 10.0.130, and cuDNN 7.5.0 are used.
1. Run the following command to uninstall the GPU driver:

```
apt-get remove --purge nvidia-*
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```bash
apt autoremove --purge cuda-10-0 rm -rf /usr/local/cuda-10.0
```

3. Run the following command to restart the instance:

```
reboot
```

If you used a .run installation package to install a GPU driver on an instance that runs Ubuntu, we recommend that you perform the following operations to uninstall the GPU driver:
1. Run the following command to uninstall the GPU driver:

```
/usr/bin/nvidia-uninstall
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```
/usr/local/cuda/bin/cuda-uninstaller rm -rf /usr/local/cuda-10.0
```

> **Note:** The commands that you run to uninstall a driver may vary based on the CUDA version. If you cannot find the cuda-uninstaller file, check whether a file whose name starts with uninstall_cuda exists in the /usr/local/cuda/bin/ directory. If a file whose name starts with uninstall_cuda exists in the directory, replace cuda-uninstaller in the preceding command with the name of the file.

3. Run the following command to restart the instance:

```
reboot
```

**Uninstall a GPU driver from CentOS**

If you used a .run installation package to install a GPU driver on an instance that runs CentOS, we recommend that you perform the following operations to uninstall the GPU driver. In this example, NVIDIA driver 410.104, CUDA 10.0.130, and cuDNN 7.5.0 are used.
1. Run the following command to uninstall the GPU driver:

```
/usr/bin/nvidia-uninstall
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```
/usr/local/cuda/bin/cuda-uninstaller rm -rf /usr/local/cuda-10.0
```

> **Note:** The commands that you run to uninstall a driver may vary based on the CUDA version. If you cannot find the cuda-uninstaller file, check whether a file whose name starts with uninstall_cuda exists in the /usr/local/cuda/bin/ directory. If a file whose name starts with uninstall_cuda exists in the file, replace cuda-uninstaller in the preceding command with the name of the file.

3. Run the following command to restart the instance:

```
reboot
```

If you used a .rpm installation package to install a GPU driver on an instance that runs CentOS 7, we recommend that you perform the following operations to uninstall the GPU driver:
1. Run the following commands to uninstall the GPU driver:

```bash
yum remove xorg-x11-drv-nvidia nvidia-kmod cuda-drivers yum remove nvidia-diag-driver-local-repo-rhel7-410.104
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```bash
yum remove /usr/local/cuda-10.0 rm -rf /usr/local/cuda-10.0
```

3. Run the following command to restart the instance:

```
reboot
```

If you used a .rpm installation package to install a GPU driver on an instance that runs CentOS 6, we recommend that you perform the following operations to uninstall the GPU driver:
1. Run the following commands to uninstall the GPU driver:

```bash
yum remove xorg-x11-drv-nvidia nvidia-kmod cuda-drivers yum remove nvidia-diag-driver-local-repo-rhel6-410.104
```

2. Run the following command to uninstall the CUDA library:

```bash
yum remove /usr/local/cuda-10.0
```

3. Run the following command to restart the instance:

```
reboot
```

**Uninstall a GPU driver from SUSE Linux**

If you used a .run installation package to install a GPU driver on an instance that runs SUSE Linux, we recommend that you perform the following operations to uninstall the GPU driver. In this example, CUDA 9.0.176 is used.
1. Run the following command to uninstall the GPU driver:

```
/usr/bin/nvidia-uninstall
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```
/usr/local/cuda/bin/uninstall_cuda_9.0.pl rm -rf /usr/local/cuda-9.0
```

3. Run the following command to restart the instance:

```
reboot
```

##### 4.14.4.2 Uninstall a GRID driver

This topic describes how to uninstall a GRID driver from a GPU-accelerated instance. The procedure for uninstalling a GRID driver may vary based on the instance operating system.

**Background information**

You can use GPU-accelerated instances only if required drivers are installed on the instances. If you uninstall a driver from your instance, install another driver that is suitable for the instance type and operating system to ensure that the instance runs as expected. For more information, see Update an NVIDIA driver.

**Uninstall a GRID driver from a Windows instance**

The following section describes how to uninstall a GRID driver from a vGPU-accelerated Windows instance. In this example, a vgn6i instance that runs Windows Server 2019 is used.
1. Connect to the instance.
For more information, see Overview.
2. In the lower-left corner of a Windows desktop, click the
icon and then click **Control**
**Panel**.
3. In the **Control Panel**, click **Uninstall a program**.
4. Right-click the GRID driver that you want to uninstall and select **Uninstall/Change**.
5. In the **NVIDIA Uninstaller** dialog box, click **UNINSTALL**.
6. After you uninstall the driver, click **RESTART NOW**.
When the instance is restarted, the GRID driver is uninstalled.

**Uninstall a GRID driver from a Linux instance**

The following section describes how to uninstall a GRID driver from a vGPU-accelerated Linux instance. In this example, a vgn6i instance that runs Ubuntu 18.04 is used.
1. Connect to the instance by using VNC.
For more information, see Connect to an instance by using a VNC management terminal.
2. Uninstall the GRID driver by following the on-screen instructions.
i. Run the following command to uninstall the driver:

```
nvidia-uninstall
```

ii. If you are asked whether to back up the X configuration file as shown in the following figure, we recommend that you accept the default value `NO` and press the Enter key.

> **Note:** The command output may vary based on the operating system. Select a value based on the actual scenario.

iii. The following command output indicates that the driver is uninstalled. Click **OK** and press the Enter key.

#### 4.14.5 Update an NVIDIA driver

If your NVIDIA driver version is not suitable for your scenario or if your GPU-accelerated instance becomes unavailable after you install an incorrect NVIDIA driver type or version, you can perform an NVIDIA driver update by uninstalling the current driver and then installing the required driver. This topic describes how to uninstall and install NVIDIA drivers on different operating systems.
1. Uninstall an NVIDIA driver.
To uninstall your NVIDIA driver, perform the operations that are described in the following topics based on the driver type:
2. Install a new NVIDIA driver.
The operations that you must perform to install an NVIDIA driver vary based on the driver type. To install a GPU driver on an instance, perform the operations that are described in the following topics based on the operating system of the instance: Install a GPU driver on a GPU-accelerated compute-optimized Linux instance Install a GPU driver on a GPU-accelerated compute-optimized Windows instance To install a GRID driver on an instance, perform the operations that are described in the following topics based on the operating system of the instance:

> **Important:** vGPU-accelerated instances support only GRID driver versions that are compatible with their instance types. If you install a GRID driver version that is incompatible with the instance type of a vGPU-accelerated instance, the instance becomes unavailable. Before you install a GRID driver on a vGPU- accelerated instance, make sure that the driver version is compatible with the instance type.

ers

## 5 Super computer clusters

### 5.1 Overview

This topic describes the features of Super Computing Cluster (SCC) instance families in Elastic Compute Service (ECS) and the instance types in SCC instance families. This topic also provides a comparison between SCCs, physical machines, and virtual machines.

**Introduction**

SCC is developed based on ECS Bare Metal Instance to significantly improve the network performance and acceleration ratio of large-scale clusters by using the high-speed Remote Direct Memory Access (RDMA)-based interconnections. SCC provides all benefits of ECS Bare Metal Instance and high-bandwidth, low-latency networks. SCC is used in scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analytics, and audio and video processing. In SCCs, nodes (ECS instances of SCC instance types) are connected over highbandwidth, low-latency RDMA networks to ensure the high parallelism of applications in areas such as high-performance computing, artificial intelligence, and machine learning. RDMA over Converged Ethernet (RoCE) networks rival InfiniBand networks in terms of connection speed and can support more Ethernet-based applications. SCC can work with ECS to provide ultra-high-performance parallel computing resources for Elastic High Performance Computing (E-HPC) to achieve cloud-based super computing. For information about E-HPC, see **What is E-HPC?** in the E-HPC User Guide in the Apsara Stack Documentation Center.

**Comparison between SCCs, physical machines, and virtual**

**machines**

The following table describes the comparison between the features of SCCs, physical machines, and virtual machines. In the table, Y indicates that the feature is supported, N indicates that the feature is not supported, and N/A indicates that the feature is not applicable.

| Feature type | Feature | SCC | Physical machine | Virtual machine |
|---|---|---|---|---|
| Automated O&M | Delivery within minutes | Y | N | Y |
| Computing | Zero performance loss | Y | Y | N |
|   | Zero feature loss | Y | Y | N |
|   | Zero resource contention | Y | Y | N |
|   | Compatibility with ECS disks | Y | N | Y |

| User Guide·Super co rs | mputer clust Elastic Compute Servic |   |   |   |
|---|---|---|---|---|
| Storage |   |   |   |   |
|   | Boot from system disks | Y | N | Y |
|   | Quick reset of system disks | Y | N | Y |
|   | Use of ECS images | Y | N | Y |
|   | Cold migration between physical and virtual machines | Y | N | Y |
|   | No need to install an operating system | Y | N | Y |
|   | No need for local RAIDs, and better protection of data in disks | Y | N | Y |
| Network | Compatibility with virtual private clouds (VPCs) | Y | N | Y |
|   | No communication bottlenecks between physical and virtual machine clusters in VPCs | Y | N | Y |
| Control | Compatibility with existing ECS management systems | Y | N | Y |
|   | Consistent user experience on features, such as Virtual Network Computing (VNC), with that on virtual machines | Y | N | Y |
| 23 | > Document Version: 2024052 |   |   |   |

ers

|   | Out-of-band (OOB) network security | Y | N | N/A |
|---|---|---|---|---|

**Instance types**

You can add only ECS instances of SCC instance types as nodes to SCCs. For information about SCC instance types, see **Intel-based instance families > SCC instance families** in the ECS Instance Families & Instance Types in the Apsara Stack Documentation Center.

### 5.2 Create an SCC

Super Computing Cluster (SCC) provides ultra-high-performance, high-parallelism computing cluster services by using heterogeneous accelerators such as CPUs and GPUs that are connected over high-speed Remote Direct Memory Access (RDMA) networks. SCC is used in scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analytics, and audio and video processing. This topic describes how to create an SCC.

**Precautions**

Take note of the following items: When you create an SCC, you cannot specify a security group ID and a virtual private cloud (VPC) ID for the SCC. The first time you add Elastic Compute Service (ECS) instances of SCC instance types to the SCC, a security group ID and a VPC ID are automatically configured for the SCC. For more information, see Add nodes to an SCC. When you create an SCC, a deployment set is automatically created in the ECS console. You can choose **Deployment Sets & Elasticity > Deployment Sets** in the left-side navigation pane to view the deployment set on the Deployment Sets page. The deployment set is named `hpc-null-deploymentset` . The Deployment Granularity parameter of the deployment set is set to **Network Switch** and the Deployment Policy parameter is set to
**Loose Aggregation**. For information about deployment sets, see Overview of deployment
sets.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Cluster**.
5. On the **Create Super Computing Cluster** page, configure the parameters that are
described in the following table.

| Parameter | Description |
|---|---|
| Organization | Select the organization for which to create the SCC. |
| Resource Set | Select the resource set in which to create the SCC. |

ers

| Region | Select the region in which to create the SCC. |
|---|---|
| Cluster Name | Enter a name for the SCC. The name must be 2 to 128 characters in length. The name cannot start with a special character or a digit. The name can contain underscores ( ), hyphens (-), _ and colons (:). |
| Cluster Description | Enter a description for the SCC based on your business requirements. |

6. Click **Submit**.

**Result**

You can view the new SCC on the Supper Computing Clusters page. For more information, see View an SCC.

**What to do next**

You can add ECS instances of SCC instance types to the SCC. For more information, see Add nodes to an SCC.

### 5.3 Add nodes to an SCC

After you create a super computing cluster (SCC), you can add nodes to the SCC by scaling up the SCC or by selecting an SCC instance type to create Elastic Compute Service (ECS) instances in the SCC.

**Prerequisites**

An SCC is created. For information about how to create an SCC, see Create an SCC.

**Background information**

After an SCC is created, the SCC is a logical cluster that does not contain nodes (ECS instances of SCC instance types) and does not have a security group ID or virtual private cloud (VPC) ID. The first time you add ECS instances to a new SCC, the security group ID and VPC ID of the ECS instances are automatically configured as the security group ID and VPC ID of the SCC and cannot be modified.

> **Important:** The security group ID and VPC ID of the SCC are automatically passed to ECS instances that are added to the SCC. All ECS instances of SCC instance types in an SCC have the same security group ID and VPC ID.

**Limits on nodes**

When you add nodes to an SCC, take note of the limits that are described in the following table.

| Item | Description |
|---|---|

ers

| ECS instance type | The nodes that you want to add must be ECS instances of SCC instance types. You can select SCC instance types to create ECS instances. For more information, see Intel-based instance families > SCC instance families in the Introduction to Instance Families and Instance Types in the Apsara Stack ECS documentation. |
|---|---|
| Image | Public images for the following operating system versions are supported: Anolis OS 8.4 ANCK (SCC) CentOS 7.5 (SCC) CentOS 7.9 (SCC) For more information, see Overview of images. |
| Network | No limits apply to an SCC that does not have a security group ID or VPC ID. The following limits apply to an SCC that has a security group ID and a VPC ID: VPC: You can use only the VPC ID of the SCC to create ECS instances in the SCC. Security group: You can use only the security group ID of the SCC to create ECS instances in the SCC. |

**Scale up an SCC**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the SCC to which you want to add nodes. In the **Actions** column, click **Scale Up**.
5. On the **Create Instance** page, create ECS instances.
Take note of the parameters that are described in the following table. For information about how to create an ECS instance, see Create an instance by using the wizard. ers

| Parameter or section | Description |
|---|---|
| Specification | The value of Category is fixed to Super Computing Cluster. |
| Instance Type | Select an instance type. |
| Super Computing Cluster | The ID of the SCC to which you want to add nodes is automatically populated in this field and cannot be changed. |
| Number of Cluster Instances | The number of ECS instances in the SCC, which is automatically specified and cannot be changed. |

If the SCC already contains ECS instances, the parameters that are described in the following table are automatically specified.

| Parameter | Description |
|---|---|
| VPC | The VPC ID of the SCC is automatically populated and cannot be changed. |
| Security Group | The security group ID of the SCC is automatically populated and cannot be changed. |

**Create ECS instances in an SCC**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Instances** page, click **Create Instance**.
5. On the **Create Instance** page, create ECS instances.
ers Take note of the parameters that are described in the following table. For information about how to create an ECS instance, see Create an instance by using the wizard.

| Parameter or section | Description |
|---|---|
| Specification | Set Category to Super Computing Cluster. |
| Instance Type | Select an instance type. |
| Super Computing Cluster | Select an existing SCC or click Create Cluster to create an SCC. After the SCC is created, go back to the Create Instance page and click the icon to obtain the most recent SCC list. For more information, see Create an SCC. Important This parameter is available and can be configured only when you set Category to Super Computing Cluster and select an SCC instance type. |
| Number of Cluster Instances | The number of ECS instances in the selected SCC, which is automatically specified and cannot be changed. |

If the SCC already contains ECS instances, the parameters that are described in the following table are automatically specified.

| Parameter | Description |
|---|---|
| VPC | The VPC ID of the SCC is automatically populated and cannot be changed. |

ers

| Security Group | The security group ID of the SCC is automatically populated and cannot be changed. |
|---|---|

### 5.4 View the details of a super computing cluster

**computing cluster**

You can view the details of a super computing cluster in the super computing cluster list.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Super Computing Clusters** page, find the super computing cluster that you want
to view and view the details of the cluster. The following table describes the cluster parameters.

| Parameter | Description |   |   |
|---|---|---|---|
| Organization | The organization to which the super computing cluster belongs. |   |   |
| Resource Set | The resource set to which the super computing cluster belongs. |   |   |
| Cluster Name | The name of the super computing cluster. |   |   |
| Cluster Description | The description of the super computing cluster. |   |   |
| Instances | The number of instances in the super computing cluster. You can click the number to go to the Instances page to view the information of all instances in the cluster. |   |   |
| Specifications | The total number of vCPUs and size of memory of all instances in the cluster. If no instances are added to the cluster, the value is vCPU: 0 Cores Memory:0 GiB . |   |   |
|   |   | vCPU: 0 Cores |   |
| Security Group ID | The security group ID of the cluster. If no instances are added to the cluster, this parameter is empty. |   |   |

|   | Memory:0 GiB |
|---|---|

ers

| VPC ID | The virtual private cloud (VPC) ID of the cluster. If no instances are added to the cluster, this parameter is empty. |
|---|---|
| Actions | Scale Up: Add instances to the cluster. For more information, see Add nodes to an SCC. Edit: Modify the attributes of a super computing cluster. For more information, see Modify the attributes of n SCC. Delete: Delete super computing clusters that are no longer needed. For more information, see Delete an SCC. |

### 5.5 Modify the attributes of an SCC

**SCC**

You can modify the following attributes of a super computing cluster (SCC) based on your business requirements: name and description.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the SCC whose attributes you want to modify. In the **Actions** column, click **Edit**.
5. In the **Edit** dialog box, modify the attributes of the SCC.

| Parameter | Description |
|---|---|
| Cluster Name | Enter a new name for the SCC. The name must be 2 to 128 characters in length. The name cannot start with a special character or a digit. It can contain underscores ( ), hyphens (-), and _ colons (:). |
| Description | Enter a new description for the SCC based on your business requirements. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

6. Click **OK**.

### 5.6 Delete an SCC

If you no longer need a super computing cluster (SCC), you can delete it.

**Prerequisites**

All Elastic Compute Service (ECS) instances are deleted from the SCC that you want to delete. For information about how to delete an ECS instance, see Delete an instance. ers

> **Important:** The amount of time that is required to release ECS instances in the background is several minutes. After you delete ECS instances from the SCC, we recommend that you wait 5 minutes to 10 minutes before you delete the SCC.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the SCC that you want to delete. In the **Actions** column, click **Delete**.
5. In the message that appears, verify the SCC information and click **Delete**.

## 6 Disks

### 6.1 Overview

This topic describes the categories of disks and operations that can be performed on disks.

**Categories of disks**

Disks are block-level storage devices provided by Apsara Stack for Elastic Compute Service (ECS) instances. Disks can be classified based on their performance or purposes.

**Performance-based classification**

Disks can be classified into ultra disks, shared ultra disks, standard SSDs, shared standard SSDs, standard performance disks, and premium performance disks based on their performance. Ultra disks and shared ultra disks are ideal for medium I/O load scenarios and deliver up to 5,000 random IOPS. Standard SSDs and shared standard SSDs are ideal for I/O-intensive scenarios and deliver up to 25,000 random IOPS. Standard performance disks and premium performance disks are ideal for online transaction processing (OLTP) databases and NoSQL databases and deliver up to 25,000 random IOPS.

> **Important:** Different Cloud Defined Storage (CDS)-Elastic Block Storage (EBS) clusters support different disk categories.
> New CDS-EBS clusters support premium performance disks and standard performance disks.
> CDS-EBS clusters that were created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks.
> Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs.

The following table compares the performance of different disk categories.

| Category | Standard SSD and shared standard SSD | Ultra disk and shared ultra disk | Standard performance disk | Premium performance disk |
|---|---|---|---|---|
| Maximum capacity of a single disk | 32,768 GB | 32,768 GB | 32,768 GB | 32,768 GB |
| Maximum IOPS | 25,000 | 5,000 | 5,000 | 25,000 |
| Maximum throughput | 300 MB/s | 140 MB/s | 140 MB/s | 300 MB/s |
| Formula for calculating the IOPS per disk | min{1,800 + 30 × Capacity, 25,000} | min{1,800 + 8 × Capacity, 5,000} | min{1,800 + 8 × Capacity, 5,000} | min{1,800 + 30 × Capacity, 25,000} |

| Formula for calculating the throughput per disk (MB/s) | min{120 + 0.5 × Capacity, 300} | min{100 + 0.15 × Capacity, 140} | min{100 + 0.15 × Capacity, 140} | min{120 + 0.5 × Capacity, 300} |
|---|---|---|---|---|
| API parameter value | cloud ssd _ | cloud efficiency _ | cloud sperf _ | cloud pperf _ |
| Usage scenario | Small and medium-sized development and test environments that require high data durability | Development and testing applications System disks | OLTP databases: relational databases such as MySQL, PostgreSQL, Oracle, and SQL Server databases NoSQL databases: non-relational databases such as MongoDB, HBase, and Cassandra databases Elasticsearch distributed logs: Elasticsearch, Logstash, and Kibana (ELK) log analysis |   |

**Purpose-based classification**

Disks can be classified into system disks and data disks based on their purposes. System disks are created and released along with the ECS instances to which they are attached and have the same lifecycle as the instances. Shared access is not allowed for system disks. Data disks can be created separately or along with ECS instances. Shared access is not allowed for data disks. A data disk created together with an ECS instance has the same lifecycle as the instance, and is released along with the instance. Data disks that are separately created can be released along with or independently of the ECS instance to which they are attached. The maximum capacity that a data disk can have is determined by its category.

**Related operations**

You can perform operations on disks based on your business needs. The following table describes the operations that can be performed on disks.

| Operation | Description | References |
|---|---|---|
| Create a disk | You can create an empty disk to use as a data disk. | Create a disk |
| Attach a data disk | Separately created disks can be attached to instances within the same zone only as data disks. | Attach a data disk |
| Partition and format a disk | Before you can use a separately created disk that is attached to a Linux or Windows instance, you must partition and format the disk on the instance. | Format a data disk for a Linux instance Format a data disk on a Windows ECS instance |
| View disks | You can view the list of created disks and the details of a single disk. | View disk details |

| Roll back a disk by using a snapshot | If you have created snapshots of a disk, you can use a snapshot to roll back the disk to the point in time when the snapshot was created. | Roll back a disk by using a snapshot |
|---|---|---|
| Change the category of a disk | You can change the category of a disk online based on your business requirements without stopping the service. | Change the category of a disk |
| Modify the properties of a disk | You can modify the properties of a created disk, including the Release Disk with Instance and Release Automatic Snapshots with Disk properties. | Modify the properties of a disk |
| Modify the name and description of a disk | You can modify the name and description of a created disk. | Change the name and description of a disk |
| Resize a disk | You can resize the system disk or data disks of an instance online or offline. After you resize a disk of an instance offline, you must restart the instance for the resize operation to take effect. | Resize a disk |
| Enable multi-attach | When you create a premium performance disk, you can enable the multi-attach feature for the disk. | Enable the multi-attach feature |
| Encrypt a disk | You can encrypt a new disk to improve security in a simple and secure manner. | Encrypt a system disk Encrypt a data disk |
| Re-initialize a disk | You can re-initialize a system disk or data disk so that the disk can return to the state it was in when the disk was created. | Re-initialize a system disk Re-initialize a data disk |
| Detach a data disk | You can detach a data disk from an instance when the instance no longer needs the disk. You can also detach a data disk from an instance and then attach the disk to another instance within the same zone. | Detach a data disk |
| Release a data disk | You can manually release disks that are no longer needed. When a disk is released, all data stored on the disk is deleted. | Release a data disk |

### 6.2 Create a disk

You can create a data disk separately and then attach it to an Elastic Compute Service (ECS) instance to increase the storage space of the instance. This topic describes how to create an empty data disk.

**Limits**

Determine the number and sizes of data disks that you need before you create them. Take note of the following limits:

> **Note:** System disks cannot be created separately.

The maximum number of data disks that can be attached to a single instance varies based on the instance type. A single premium performance disk that has the multi-attach feature enabled can be attached to up to 16 ECS instances at the same time. Each ultra disk, shared ultra disk, standard SSD, shared SSD, premium performance disk, or standard performance disk can be up to 32 TiB in size. Disks cannot be combined in ECS. They are independent of each other. You cannot combine multiple disks into one by formatting them. A snapshot can back up data only of a single disk. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across disks. If you use LVM to create a logical volume across multiple existing disks, data discrepancy may occur when you restore disks from snapshots.

**Create a disk on the Disks page**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Disk**.
5. On the Create Disk page, configure the parameters.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization | Yes | Select the organization for which to create the disk. |
|   | Resource Set | Yes | Select the resource set in which to create the disk. |
|   | Region | Yes | Select the region in which to create the disk. |
|   | Zone | Yes | Select the zone in which to create the disk. |

|   | Creation Method | Yes | Select a method to use to create the disk. Valid values: Disk Creation Storage Set Creation Note Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to resources in the storage set. You can use storage sets to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see Create a storage set in the CDS User Guide. |
|---|---|---|---|
|   | Storage Set | Yes | Select a storage set to use to create the disk. Note This parameter is required when you set Creation Method to Storage Set Creation. |
|   | Partition | Yes | Specify the number of a partition in the specified storage set to use to create the disk. A storage set must contain two or more partitions. Note This parameter is required when you set Creation Method to Storage Set Creation. |
|   | Name | Yes | Enter a name for the disk. If you create only a single disk, the name must be 2 to 128 characters in length. If you create multiple disks at a time, the name must be 2 to 125 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |

| Basic Configurations |   |   |   |
|---|---|---|---|
|   | Quantity | Yes | Specify the number of disks that you want to create. Valid values: 1 to 100. |
|   | Specifications | Yes | Select a disk category. Different CDS- EBS clusters support different disk categories. New CDS-EBS clusters support the following disk categories: Premium Performance Disk Standard Performance Disk CDS-EBS clusters that are created in Apsara Stack V3.15.0 and earlier support the following disk categories: Ultra Disk Standard SSD Premium Performance Disk Standard Performance Disk Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs. Important If you have used shared ultra disks and shared standard SSDs, you can continue to use them. If you have never used shared ultra disks or shared standard SSDs, you cannot use disks of these categories. |
|   | Disk Size | Yes | Specify a disk size in the range of 20 GB to 32,768 GB. |
|   | Multi-attach | No | Specify whether to enable multi- attach for the disk. For more information, see Overview of disks that support NVMe. Note This parameter is required when you set Specifications to Premium Performance Disk. |
|   | Encryption | No | Specify whether to encrypt the disk. |

|   | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required when you set Encryption to Yes. Valid values: AES256 SM4 |
|---|---|---|---|
|   | Encryption Key | No | Select a key to use to encrypt the disk. This parameter is required when you set Encryption to Yes. Note If no keys are available, create a key in Key Management Service (KMS). |
|   | Use Snapshot | No | Specify whether to create the disk from a snapshot. If you select Yes, you must select a snapshot. If you select a snapshot, the size of the disk is determined based on the size of the selected snapshot. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is smaller than the snapshot size, the disk is created with the snapshot size. |

6. Click **Submit**.

**Create a disk on the Instance Details page**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Instances page, click the instance ID in the **Instance ID/Name** column.
5. On the **Instance Details** page, click the **Disks** tab.
6. Click **Create Disk**.
7. On the Create Disk page, configure the parameters.

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Organization | Yes | Select the organization for which to create the disk. |

| er Guide·Disks | Elastic Compute Servic |   |   |
|---|---|---|---|
| Area |   |   |   |
|   | Resource Set | Yes | Select the resource set in which to create the disk. |
|   | Region | Yes | Select the region in which to create the disk. |
|   | Zone | Yes | Select the zone in which to create the disk. |
|   | Creation Method | Yes | Select a method to use to create the disk. Valid values: Disk Creation Storage Set Creation Note Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to resources in the storage set. You can use storage sets to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see Create a storage set in the CDS User Guide. |
|   | Storage Set | Yes | Select a storage set to use to create the disk. Note This parameter is required when you set Creation Method to Storage Set Creation. |
|   | Partition | Yes | Specify the number of a partition in the specified storage set to use to create the disk. A storage set must contain two or more partitions. Note This parameter is required when you set Creation Method to Storage Set Creation. |

| Basic Configurations |   |   |   |
|---|---|---|---|
|   | Name | Yes | Enter a name for the disk. If you create only a single disk, the name must be 2 to 128 characters in length. If you create multiple disks at a time, the name must be 2 to 125 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
|   | Quantity | Yes | Specify the number of disks that you want to create. Valid values: 1 to 100. |
|   | Specifications | Yes | Select a disk category. Different CDS- EBS clusters support different disk categories. New CDS-EBS clusters support the following disk categories: Premium Performance Disk Standard Performance Disk CDS-EBS clusters that are created in Apsara Stack V3.15.0 and earlier support the following disk categories: Ultra Disk Standard SSD Premium Performance Disk Standard Performance Disk Existing EBS clusters continue to provide shared ultra disks and shared standard SSDs. Important If you have used shared ultra disks and shared standard SSDs, you can continue to use them. If you have never used shared ultra disks or shared standard SSDs, you cannot use disks of these categories. |
|   | Disk Size | Yes | Specify a disk size in the range of 20 GB to 32,768 GB. |

|   | Multi-attach | No | Specify whether to enable multi- attach for the disk. For more information, see Overview of disks that support NVMe. Note This parameter is required when you set Specifications to Premium Performance Disk. |
|---|---|---|---|
|   | Encryption | No | Specify whether to encrypt the disk. |
|   | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required when you set Encryption to Yes. Valid values: AES256 SM4 |
|   | Encryption Key | No | Select a key to use to encrypt the disk. This parameter is required when you set Encryption to Yes. Note If no keys are available, create a key in Key Management Service (KMS). |
|   | Use Snapshot | No | Specify whether to create the disk from a snapshot. If you select Yes, you must select a snapshot. If you select a snapshot, the size of the disk is determined based on the size of the selected snapshot. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is smaller than the snapshot size, the disk is created with the snapshot size. |

8. Click **Submit**.

**View the results**

The disk that you created is displayed in the disk list and is in the **Available** state.

**What to do next**

After the disk is created, you can attach the disk and partition and format it. For more information, see the following topics:

### 6.3 Attach a data disk

You can attach a separately created disk as a data disk to an instance that resides in the same zone.

**Prerequisites**

The disk resides in the same zone as the instance to which you want to attach the disk. The instance is in the Running (Running) or **Stopped** (**Stopped**) state. The disk is in the **Available** (Available) state.

**Background information**

Before you attach disks, take note of the following items: Disks that were created along with instances are already attached to the instances. A disk can be attached only to an instance that is located in the same zone and region as the disk. Each disk can be attached only to a single instance at the same time. Disks that do not support the multi-attach feature or disks for which the multi-attach feature is disabled can be attached only to a single instance at the same time. A disk that supports the multi-attach feature can be attached to multiple instances at the same time. For more information, see Overview of disks that support NVMe. Each Shared Block Storage device can be attached to up to four instances at the same time.

**Attach a disk on the Instance Details page**

If you want to attach multiple disks to an instance, go to the details page of the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance and click the instance ID.
5. On the **Instance Details** page, click the **Disks** tab.
6. Click **Attach Disk**.
7. In the **Attach Disk** dialog box, select a disk from the **Disk** drop-down list.
8. Click **OK**.
9. Create partitions and file systems on the disk after the disk is attached to the instance.

> **Note:** After the disk is attached to the instance, the disk cannot be used on the instance. For example, you cannot view the mount information of the disk attached to a Linux instance by running the `df -h` command. You must perform operations based on the operating system type of the instance to make the disk usable on the instance. For more information, see the following topics:

**Attach a disk on the Disks page**

If you want to attach multiple disks to different instances, go to the Disks page.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find a disk whose state in the **Status** column is **Available** and choose
> **Attach** in the

**Actions** column.
5. In the Attach dialog box, configure parameters to attach the disk.

| Parameter | Description |
|---|---|
| Instance | Select the instance to which you want to attach the disk. |
| Release Disk with Instance | If you select this option, the disk is automatically released when its associated instance is released. If you do not select this option, the disk is retained when its associated instance is released. Note If the disk that you want to attach is a system disk that was detached from another instance, the instance specified by Release Disk with Instance refers to the instance from which the disk was detached, instead of the current instance. |

6. Click **OK**.
When the disk is attached, its state changes to **Running**.
7. Create partitions and file systems on the disk after the disk is attached to the instance.

> **Note:** After the disk is attached to the instance, the disk cannot be used on the instance. For example, you cannot view the mount information of the disk attached to a Linux instance by running the `df -h` command. You must perform operations based on the operating system type of the instance to make the disk usable on the instance. For more information, see the following topics:

### 6.4 Partition and format disks

#### 6.4.1 Format a data disk for a Linux instance

Data disks created separately are not partitioned or formatted. This topic describes how to partition and format a data disk of a Linux instance.

**Prerequisites**

The data disk that you want to manage is attached to a Linux instance.
1. Connect to the Linux instance.
For more information, see Overview.
2. Run the **fdisk -l** command to view all data disks attached to the instance.
If /dev/vdb is not displayed in the command output, no data disk is attached to the ECS instance. Check whether the data disk that you want to manage is attached to the instance.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00000000
```

3. Partition the data disk.
i. Run the **fdisk /dev/vdb** command. ii. Enter `n` to create a partition. iii. Enter `p` to set the partition type to primary partition. iv. Enter the partition sequence number and press the ENTER key. In this example, `1` is entered to create Partition 1. v. Enter a sequence number for the first available sector. You can press the ENTER key to accept the default value, or enter a value ranging from 1 to 41,610 and then press the ENTER key. In this example, the default value is used. vi. Enter the sequence number for the last sector. You can press the ENTER key to accept the default value, or enter a value ranging from 1 to 11,748 and then press the ENTER key. In this example, the default value is used. vii. **Optional:**To create multiple partitions, repeat steps ii to vi until all primary partitions are created. viii. Run the **wq** command to start partitioning the data disk.

```
[root@iZ********eZ ~]# fdisk /dev/vdb Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel Building a new DOS disklabel with disk identifier 0x01ac58fe. Changes will remain in memory only, until you decide to write them. After that, of course, the previous content won't be recoverable. Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite) WARNING: DOS-compatible mode is deprecated. It's strongly recommended to
         switch off the mode (command 'c') and change display units to
         sectors (command 'u').
Command (m for help): n Command action
   e   extended
   p   primary partition (1-4)
```

`p`

```
Partition number (1-4): 1 First cylinder (1-41610, default 1): Using default value 1 Last cylinder, +cylinders or +size{K,M,G} (1-41610, default 41610): Using default value 41610 Command (m for help): wq The partition table has been altered!
```

4. Run the **fdisk -l** command to view the partitions.
If /dev/vdb1 is displayed in the command output, a partition named vdb1 is created.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x01ac58fe Device Boot Start End Blocks Id System /dev/vdb1 1 41610 20971408+ 83 Linux
```

5. Format the new partition. In this example, the **mkfs.ext3 /dev/vdb1** command is used to
format the new partition as ext3. The amount of time required for formatting depends on the disk size. You can also format the new partition to another file system. For example, run the **mkfs.ext4 /dev/vdb1** command to format the partition as ext4. ext4 is a deeper improvement over ext3 than ext3 was over ext2. ext3 was mostly about adding journaling to ext2, but ext4 modifies important data structures of the file system. ext4 provides better performance and reliability and more features.

```
[root@iZ********leZ ~]# mkfs.ext3 /dev/vdb1 mke2fs 1.41.12 (17-May-2010) Filesystem label= OS type: Linux Block size=4096 (log=2) Fragment size=4096 (log=2) Stride=0 blocks, Stripe width=0 blocks 1310720 inodes, 5242852 blocks 262142 blocks (5.00%) reserved for the super user First data block=0 Maximum filesystem blocks=4294967296 160 block groups 32768 blocks per group, 32768 fragments per group 8192 inodes per group Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
    4096000
Writing inode tables: done Creating journal (32768 blocks): done Writing superblocks and filesystem accounting information: done This filesystem will be automatically checked every 25 mounts or 180 days, whichever comes first. Use tune2fs -c or -i to override.
```

| echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab ion of the new partition to the /etc/fstab file. Then, run the | command to write cat /etc/fstab |
|---|---|

command to view the information of the new partition. Ubuntu 12.04 does not support barriers. To write the information of the new partition to the /etc/fstab file, run the `echo '/dev/vdb1 /mnt ext3 barrier=0 0 0' >> /etc/fstab` command. In this example, the partition information is added to the ext3 file system. You can also modify the ext3 parameter to add the partition information to another type of file system. To mount the data disk to a specific folder for specific purposes, such as storing web pages, modify the /mnt part of the preceding command.

```
[root@iZ********eZ ~]# echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab [root@iZbp19cdhgdj0aw5r2izleZ ~]# cat /etc/fstab
```

`#`

```bash
# /etc/fstab
# Created by anaconda on Thu Aug 14 21:16:42 2014
```

`#`

```bash
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
```

`#`

```
UUID=94e4e384-0ace-437f-bc96-057dd64f**** / ext4 defaults,barrier=0 1 1 tmpfs /dev/shm tmpfs defaults 0 0 devpts /dev/pts devpts gid=5,mode=620 0 0 sysfs /sys sysfs defaults 0 0 proc /proc proc defaults 0 0 /dev/vdb1 /mnt ext3 defaults 0 0
```

7. Run the following command to mount the new partition: Run the **mount -a** command to
mount all the partitions listed in the /etc/fstab file and run the **df -h** command to view the result. If the following information is displayed, the new partitions are mounted and ready for use.

```
[root@iZ********eZ ~]# mount -a [root@iZ********eZ ~]# df -h Filesystem Size Used Avail Use% Mounted on /dev/vda1 40G 5.6G 32G 15% / tmpfs 499M 0 499M 0% /dev/shm /dev/vdb1 20G 173M 19G 1% /mnt
```

#### 6.4.2 Format a data disk on a Windows ECS instance

**instance**

Before you can store, read, and write data on a new data disk that is attached to a Windows Elastic Compute Service (ECS) instance, you must initialize the data disk. The initialization operations include partitioning the disk, formatting the disk, and bringing the disk online. This topic describes how to initialize a data disk on a Window instance.

**Prerequisites**

The data disk is attached to a Window instance. For more information, see Attach a data disk.

**Background information**

The example in this topic uses an ECS instance and a data disk that have the configurations described in the following table. Operations may vary based on actual conditions.

| Operating system | Resource | Description |
|---|---|---|
|   | Image used by the instance | Windows Server 2012 R2 64-bit |
| 47 | > Document Version: 2024052 |   |

| lastic Compute Serv | ice User Guide·Disk |   |
|---|---|---|
| Windows operating system |   |   |
|   | Data disk | Disk name: Disk 1 Disk capacity: 40 GiB |

1. Connect to the instance.
For more information, see Overview.
2. On the Windows Server desktop, right-click the
icon and select **Disk Management**.
3. Find the data disk that you want to initialize and is in the **Offline** state. In this example,
**Disk 1** is used.
4. Right-click the blank space around **Disk 1** and select **Online**.
When the disk goes online, **Disk 1** enters the **Not Initialized** state.
5. Right-click the blank space around **Disk 1** and select **Initialize Disk**.
6. In the **Initialize Disk** dialog box, select the disk, select a disk partition format, and then
click **OK**. The following figure shows how to initialize a disk to a GUID partition table (GPT) partition.

> **Important:** A Master Boot Record (MBR) partition can be up to 2 TiB in size. If the disk for which a partition is created is larger than 2 TiB or if the disk may be resized to larger than 2 TiB, use the GPT partition format.

7. Right-click the **Unallocated** section of **Disk 1** and select **New Simple Volume**.
8. In the **New Simple Volume Wizard** window, click **Next** and follow the wizard to perform
initialization operations. i. In the **Specify Volume Size** step, set **Simple volume size in MB** and click **Next**. If you want to create only a single primary partition on the disk, use the default value. You can also specify a simple volume size based on your needs to divide **Disk 1** into multiple partitions. ii. In the **Assign Drive Letter or Path** step, select **Assign the following drive letter**, select a drive letter, and then click **Next**. In this example, **D** is selected for the drive letter. iii. In the **Format Partition** step, select **Format this volume with the following**
**settings**, configure formatting settings, and then click **Next**.
iv. View the information of the new simple volume and then click **Finish** to close the **New**
**Simple Volume Wizard** window.

### 6.5 View disk details

You can view the list of created disks and the details, snapshots, and operation records of a disk. The details of a disk include the basic information and attachment information of the disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Disks page, you can view information about existing disks.
You can view disk information in the disk list, which may include the following columns:
**Disk ID/Name**, **Status**, **Organization/Resource Set**, **Region**, **Disk Category/Size**,
**Multi-attach**, **Instance ID/Name**, **Disk Type**, and **Encrypted**.

> **Note:** If you created a disk together with the instance to which the disk is attached and do not specify a name for the disk, a name is assigned to the disk based on the following naming conventions:
> If the disk is the system disk of the ECS instance, a name in the format of <Instance name>_SystemDisk is assigned to the disk. Example: ecstest_SystemDisk.
> If the disk is a data disk of the ECS instance, a name in the format of <Instance name>_dataDisk_*** is assigned to the disk. Example: ecstest_dataDisk_001 or ecstest_dataDisk_002.

You can perform the following steps to customize the instance list to include specific columns: i. In the upper-right corner of the disk list, click the icon. ii. In the drop-down list, select the columns that you want to include. The selected columns are immediately included in the disk list.
5. Use one of the following methods to find a disk whose details you want to view:

> **Note:** You can select a filter option, such as **Disk Name**, **Disk ID**, **Encryption Key ID**, **Storage Set**, **Partitions**, **Zone**, or **Instance ID**, and enter relevant information to search for disks.
> Fuzzy search is supported only if you select **Disk Name** or **Disk ID** as the filter option.

Select a filter option and enter relevant information to search for disks. Click **Advanced Filter**, specify multiple filter options, and then click **Search** to search for disks.

> **Note:** The Advance Filter feature allows you to specify multiple filter options to narrow down search results.

6. Click the ID of a disk in the **Disk ID/Name** column.
The **Disk Details** tab is displayed. The following table describes the disk information that is displayed on the **Instance Details** tab.

| Section | Description |
|---|---|
| Basic Information | The basic information about the disk, including the disk name, disk ID, disk status, organization and resource set to which the disk belongs, region where the disk resides, disk category, disk size, multi-attach settings, IDs and names of the instances to which the disk is attached, and encryption settings of the disk. You can click Modify Disk Description in the upper-right corner of the Basic Information section to change the name and description of the disk. For more information, see Change the name and description of a disk. |

| Attachment Information | The attachment information about the disk, including the Release Disk with Instance settings, Release Automatic Snapshots with Disk settings, and information about instances to which the disk is attached. You can also click Modify Disk Properties in the upper-right corner of the Attachment Information section to modify the release mode settings of the disk. For more information, see Modify the properties of a disk. |
|---|---|

7. View the snapshots and operation records of the disk.
Snapshots of the disk: Click the **Disk Snapshots** tab to view information about snapshots that are created for the disk. The information about a snapshot includes the snapshot ID, snapshot encryption settings, tags that are added to the disk, snapshot type, snapshot creation progress, and snapshot creation time. Operation records of the disk: Click the **Operation Records** tab to view the operation logs of the disk. The operation logs include the operation names, operators, execution status, operation sources (Valid values: Console Call and API call), operation types, operation source IP addresses, and operation time.

> **Note:** Operation logs can be retained for seven days. To change the retention period of operation logs, contact the administrator to go to the Log Storage Settings page by choosing **Configurations > Log Storage Settings** in the top navigation bar.
> If the retention period of operation logs on the Log Storage Settings page is increased, historical operation logs that are not retained before the retention period is increased are not backfilled.

### 6.6 Roll back a disk by using a snapshot

**snapshot**

If you have created a snapshot of a disk, you can use the snapshot to roll back the disk to the point in time when the snapshot was created. The disk rollback operation is irreversible. After the disk is rolled back, the data that was stored on the disk before the rollback operation is performed is lost and cannot be recovered. Exercise caution when you perform this operation.

**Prerequisites**

Before you roll back a disk by using a snapshot, make sure that the following requirements are met: Snapshots have been created for the disk, and no snapshots are currently being created for the disk. For more information, see Create snapshots. The disk is not released. The disk is attached to an instance that is in the **Stopped** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find a snapshot of the disk that you want to roll back and click **Roll Back Disk** in the
**Actions** column.

> **Note:** You can roll back only one disk on an instance at a time. Other disks that are attached to the instance are not affected. After the rollback operation is complete, the entire disk (not a partition or a directory) is restored to the state that the disk was in when the snapshot was created.

6. In the message that appears, click **Roll Back Disk**.
7. Starts an ECS instance.
For more information, see Start an instance.

**What to do next**

After the disk is rolled back, the hosts configuration file and the configurations such as the hostname, SSH key pair, passwords, network settings, operating system repository settings, and clock source are initialized. You must reconfigure the file and configurations If you have resized the disk after you created the snapshot for the disk, you must log on to the instance to resize the file systems on the disk again after the disk is rolled back. For more information, see Resize a disk.

### 6.7 Change the category of a disk

Apsara Stack offers different categories of disks to meet storage performance and cost requirements for a variety of scenarios. You can change the categories of disks based on your needs without stopping the instances to which the disks are attached. For example, assume that you have created a standard SSD. If you want the standard SSD to deliver a higher IOPS, you can change this standard SSD into an enhanced SSD (ESSD).

**Prerequisites**

Snapshots of the disk whose category you want to change are created. For information about how to create snapshots for disks, see Create snapshots.

**Background information**

For information about the performance of different disk categories, see Categories of disks.

**Precautions**

When you change disk configurations, take note of the following items: When you change the category of a disk, the performance of the disk may also change. We recommend that you change the categories of your disks during off-peak hours. It may take hours to change the category of a disk. The actual amount of time required is determined based on the storage capacity, original category, and throughput of the disk. After you change the configurations of a disk, we recommend that you call the
**DescribeTaskAttribute** operation in **ECS Developer Guide** to view the task progress.
The change may fail due to resource insufficiency in rare cases. If a failure occurs, try again later.

**Usage notes**

Only disks that are based on Apsara Distributed File System 2.0 support configuration changes. The following table lists disk categories that can be changed online.

| Original disk category | New disk category to which a disk can be changed online |
|---|---|
| Standard SSD | Ultra disk Premium performance disk Standard performance disk |
| Ultra disk | Standard SSD Premium performance disk Standard performance disk |
| Premium performance disk | Standard performance disk |
| Standard performance disk | Premium performance disk |

The following table describes limits that apply to each phase of a disk configuration change.

| Phase | Limitation |
|---|---|
| Before the change | Up to five disk change tasks can be concurrently performed per region in an account. |
| During the change | The following limits apply while a disk is being changed: You cannot cancel the disk change task. You cannot create snapshots for the disk. You cannot resize the disk. You cannot partition or format the disk. You cannot re-initialize the disk. You cannot roll back the disk by using a snapshot. You cannot attach or detach the disk. If the disk is a system disk, you cannot replace the operating system of the instance. |
| After the change | A disk can have its category changed only once within seven days. |

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk that you want to resize, click the
icon in the **Actions** column, and then select **Change Disk Category**.
5. In the **Change Disk Category** dialog box, set **New Disk Category**.
6. Then, click **OK**.

**Results**

On the **Disks** page, find the disk whose category you want to change and view its **category**. The new category is displayed.

### 6.8 Modify the properties of a disk

You can modify the properties of a created disk, such as the configurations of the Release Disk with Instance and Release Automatic Snapshots with Disk options.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk whose information you want to modify, click the
icon in the **Actions** column, and then select **Modify Disk Properties**.
5. In the **Modify Disk Properties** dialog box, modify the Release Mode settings. You can
specify one of the following release modes:
**Release Disk with Instance**: If this option is selected, the disk is released when the
instance to which the disk is attached is deleted. If this option is not selected, the disk is retained and enters the **Pending** state when the instance to which the disk is attached is deleted.
**Release Automatic Snapshots with Disk**: If this option is selected, the automatic
snapshots created for the disk are released when the disk is deleted. If this option is not selected, the automatic snapshots are retained when the disk is deleted.
6. Click **OK**.

### 6.9 Change the name and description of a disk

**description of a disk**

You can change the name and description of a created disk to facilitate disk management and improve disk readability.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk whose name and description you want to change. In the **Actions** column,
choose
**> Modify Disk Description**.

> **Note:** Alternatively, click the ID of the disk whose name and description you want to change in the **Disk ID/Name** column, find the **Basic Information** section on the **Disk Details** tab, and then click **Modify Disk Description**.

5. Change the name and description of the disk.
The disk name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://` . The name can contain letters, digits, periods (.), underscores (_), hyphens (-), colons (:), and commas (,). The disk description must be 2 to 256 characters in length and cannot start with `http://` or `https://` .
6. Click **OK**.

### 6.10 Resize a disk

You can resize your disks to store a larger volume of data as your storage requirements increase. You can resize the system disk or data disks of an instance online or offline. After you resize a disk of an instance offline, you must restart the instance for the resize operation to take effect.

**Prerequisites**

To prevent data loss, we recommend that you create a snapshot to back up disk data before you resize a disk. For more information, see Create snapshots. No snapshot is being created for the disk that you want to resize. The following requirements are met: If the disk is a system disk, the associated instance is in the **Running** state. If the disk is a data disk, one of the following requirements is met: The disk is in the **Pending** state. If the disk is attached to an instance, the instance is in the **Running** state. If the disk is a Shared Block Storage device, the disk is in the **Pending** state.

**Background information**

You can use one of the following methods to increase the storage capacity of a single instance:

> **Note:** When you resize a disk, only the storage capacity of the disk is increased. The sizes of partitions and file systems do not change.

Resize an existing disk. You can resize the existing partitions of the disk or create more partitions on the disk. The following table describes the methods that can be used to resize an existing disk.

| Method | Usage notes |
|---|---|
| Resize a disk online | The instance is in the Running state. After you resize the disk, the new size automatically takes effect without the need to restart the associated instance. |
| Resize a disk offline | The instance is in the Running or Stopped state. After you resize the disk, you must restart the associated instance in the Elastic Compute Service (ECS) console or by calling the RebootInstance operation for the new size to take effect. |

Create a disk, attach the disk to an ECS instance as a data disk, and then partition and format the disk. Replace the system disk of an instance and specify a larger size for the new system disk.

**Limits**

Before you resize disks, take note of the following items.

| Item | Limits |
|---|---|
| Disk category | Different CDS-EBS clusters support different disk categories. New CDS-EBS clusters support the following disk categories: Premium performance disk Standard performance disk CDS-EBS clusters that were created in Apsara Stack V3.15.0 and earlier support the following disk categories: Ultra disk Standard SSD Premium performance disk Standard performance disk Existing Elastic Block Storage (EBS) clusters continue to provide shared ultra disks and shared standard SSDs. Important If you have used shared ultra disks and shared standard SSDs, you can continue to use them. If you have never used shared ultra disks and shared standard SSDs, you cannot use disks of these categories. |
| Operating system | The system disks of Windows Server 2003 instances cannot be resized. |
| Partitioning mode | If a data disk uses the MBR partition format, the data disk cannot be resized to more than 2 TiB. If you want to resize a data disk to more than 2 TiB and the data disk uses the MBR partition format, we recommend that you create and attach another data disk. Then, format a GPT partition and copy the data in the MBR partition to the GPT partition. |
| File system | For Windows instances, only disks that use NTFS file systems can be resized. |
| Capacity | System disk: The new capacity must be greater than the current capacity. The new capacity must be smaller than or equal to 2,048 GiB. For example, the system disk of a CentOS instance is 35 GiB in size. When you resize this system disk, the specified new size must be larger than 35 GiB but cannot exceed 2,048 GiB. Data disk: The new capacity must be greater than the current capacity. The new capacity must be smaller than or equal to 32,768 GiB. For example, a data disk of a CentOS instance is 35 GiB in size. When you resize this data disk, the specified new size must be larger than 35 GiB but cannot exceed 32,768 GiB. |
| Operation | When you resize a disk, only the storage capacity of the disk is increased. The sizes of partitions and file systems do not change. After the disk is resized, you must manually re-allocate the storage space on the disk. You cannot roll back a resize operation on a disk to decrease the storage capacity of the disk. |

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk that you want to resize, click the
icon in the **Actions** column, and then select **Resize Disk**.
5. In the **Resize Disk** dialog box, select a resizing method and specify the new capacity.
Resizing methods: Online resizing: After you resize the disk, the new size automatically takes effect without the need to restart the associated instance. Offline resizing: After you resize the disk, you must restart the associated instance in the ECS console or by calling the `RebootInstance` operation for the new size to take effect. For more information, see Restart an instance or the `RebootInstance` topic in **ECS**
**Developer Guide**.
Maximum new capacity: System disk: 2,048 GiB Data disk: 32,768 GiB
6. Click **OK**.

**What to do next**

After a disk is resized, you must manually re-allocate the storage space on the disk.

### 6.11 Support the NVMe protocol and multi-attach feature

**and multi-attach feature**

#### 6.11.1 Overview of disks that support NVMe

Non-Volatile Memory Express (NVMe) is a host controller interface protocol used to accelerate the transfer of data from non-volatile memory. Alibaba Cloud premium performance disks support NVMe. Each premium performance disk can be simultaneously attached to multiple Elastic Compute Service (ECS) instances that support NVMe for data sharing. This topic describes premium performance disks that support NVMe, limits on attaching this type of disks, and operations related to this type of disks.

**Premium performance disks that support NVMe**

Premium performance disks can be attached to multiple ECS instances. After premium performance disks are attached to multiple instances, the disks support concurrent read and write access from these ECS instances and provide high reliability, high concurrency, and high performance. Premium performance disks provide the multi-attach and I/O blocking features. After the multi-attach feature is enabled for a premium performance disk, the disk can be attached to up to 16 ECS instances at a time. You can run NVMe commands to manage the permissions of ECS instances on premium performance disks. For more information about NVMe commands, see NVM Express Base Specification. The preceding features improve service availability without compromising data reliability. If a single point of failure (SPOF) occurs, you can use a premium performance disk to quickly schedule and restore data. Data sharing among multiple ECS instances greatly reduces storage costs and improves service flexibility. Premium performance disks are suitable for high-availability databases and distributed database clusters that each consist of one write node and multiple read-only nodes. Premium performance disks can be attached to ECS instances that support NVMe. For example, after premium performance disks are attached to Linux instances based on NVMe, you can run the **lsblk** command to check the device names and partition names of the disks, as shown in the following figure. Description of the command output: The device names of the premium performance disks are displayed in the `/dev/nvmeXn1` format. Examples: /dev/nvme0n1, /dev/nvme1n1, and /dev/nvme2n1. The partition names of the premium performance disks are displayed in the `<Device name` `of the disk>p<Partition number>` format. Examples: /dev/nvme0n1p1, /dev/nvme1n1p1, and /dev/nvme1n1p2. Premium performance disks provide the multi-attach feature and are used by enterprises to migrate high-availability services to the cloud. For more information, see Enable the multiattach feature.

**Limits**

Before you attach premium performance disks to an ECS instance based on NVMe, the resources of the instance must meet the limits described in the following table.

| Item | Limits |
|---|---|
| Instance family | By default, the instance family must support NVMe. The following instance families support NVMe: ecs.ebmg7s-se-x25-c1m8 ecs.ebmg7m-se-x25-c1m8 ecs.ebmg7x-se-x25-c1m8 ecs.ebmg7s-se-numaoff-x25-c1m8 ecs.ebmg7m-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.g7x-se-x25 Note You can call the DescribeInstanceTypes operation to query instance families and check whether the instance family supports NVMe based on the NvmeSupport parameter in the response. For more information, see the DescribeInstanceTypes topic in ECS Developer Guide. |
| Image | The image must contain the NVMe driver. The NVMe driver is installed in the following public images. Note Only some public Linux images support the NVMe driver. CentOS 7: CentOS 7.6 and later CentOS 8: CentOS 8.0 and later |

| Disk | Disk category: premium performance disk Creation method: Create premium performance disks when you create instances that support NVMe. When you create disks, select premium performance disks as the disk category and enable the multi-attach feature. |
|---|---|

**Related operations**

You can perform the following operations on premium performance disks that support NVMe: Create premium performance disks when you create ECS instances that support NVMe. In this case, the created premium performance disks support NVMe. For more information, see Create an instance by using the wizard. Enable the multi-attach feature when you separately create premium performance disks. For more information, see Enable the multi-attach feature. Format premium performance disks and create file systems. For more information, see Format a data disk for a Linux instance.

> **Important:** The preceding operations are applicable only to premium performance disks that are created together with instances but not to premium performance disks for which the multi-attach feature is enabled.

#### 6.11.2 Enable the multi-attach feature

When you create a premium performance disk, you can enable the multi-attach feature for the disk. After multi-attach is enabled for a premium performance disk, the disk can be attached to up to 16 Elastic Compute Service (ECS) instances that support the Non-Volatile Memory Express (NVMe) protocol within the same zone to allow concurrent read and write access from the instances.

**Benefits**

This feature is suitable for high-availability databases and distributed database clusters that each consists of one write node and multiple read-only nodes. This feature provides the following benefits: Usage of NVMe commands: NVMe commands can be used to manage permissions of ECS instances on premium performance disks. This helps improve service availability without compromising data durability. For more information about NVMe commands, see NVM Express Base Specification. Cross-instance data sharing: This feature enables data sharing across multiple ECS instances to reduce storage costs and improve service flexibility. Disaster recovery: This feature allows quick scheduling of services to normal ECS instances to ensure service continuity in single-point-of-failure (SPOF) scenarios.

**Limits**

The following limits apply to the multi-attach feature: The following instance families support the feature. ecs.ebmg7s-se-x25-c1m8 ecs.ebmg7m-se-x25-c1m8 ecs.ebmg7x-se-x25-c1m8 ecs.ebmg7s-se-numaoff-x25-c1m8 ecs.ebmg7m-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.g7x-se-x25 Data disks are supported but system disks are not supported. The multi-attach feature can be enabled only when you create premium performance disks. This feature cannot be enabled or disabled after premium performance disks are created. After the multi-attach feature is enabled for a premium performance disk, we recommend that you use cluster file systems such as Oracle Cluster File System version 2 (OCFS2), Global File System 2 (GFS2), Veritas Cluster File System (Veritas CFS), Oracle Automatic Storage Management Cluster File System (Oracle ACFS), and Databricks File System (DBFS) on the disk.

> **Warning:** When a premium performance disk for which the multi-attach feature is enabled is attached to multiple ECS instances, data cannot be synchronized among the instances and data inconsistency may occur if file systems such as EXT2, EXT3, EXT4, XFS, and New Technology File System (NTFS) are used.

The performance of premium performance disks is limited. When a premium performance disk is attached to multiple ECS instances, the total performance of the disk on all instances cannot exceed the maximum performance that can be provided by the disk. The following table describes the limits that apply to the features provided by premium performance disks for which the multi-attach feature is enabled.

| Feature | Limits |
|---|---|
| Disk attachment | A single premium performance disk can be attached to up to 16 instances that support the NVMe protocol. |
| Release of disks with instances | Not supported. |
| Disk re-initialization | Not supported. |
| Disk category change | Not supported. |
| Disk resizing | Only offline resizing is supported for disks. For information about how to resize disks online, see Resize cloud disks online. |
| Snapshot-consistent group | Not supported. |

**Use multi-attach**

Perform the following steps to use the multi-attach feature:
1. Step 1: Create a premium performance disk for which the multi-attach feature is enabled
2. Step 2: Attach the premium performance disk to multiple instances that support the NVMe
protocol

**Step 1: Create a premium performance disk for which the**

**multi-attach feature is enabled**

To use the multi-attach feature, enable the feature when you create a premium performance disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Disk**.
5. Configure the parameters that are described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization | Yes | Select the organization for which to create the disk. |
|   | Resource Set | Yes | Select the resource set in which to create the disk. |
|   | Region | Yes | Select the region in which to create the disk. |
|   | Zone | Yes | Select the zone in which to create the disk. |
|   | Creation Method | Yes | Select the method that you want to use to create the disk. Valid values: Disk Creation and Storage Set Creation. Note Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to its resources. Storage sets can be used to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see the "Create a storage set" topic in the CDS User Guide. |

|   | Storage Set | Yes | Select the storage set that you want to use to create the disk. Note This parameter is required if you set Creation Method to Storage Set Creation. |
|---|---|---|---|
|   | Partition | Yes | Select the number of partitions in a storage set. The value of this parameter must be greater than or equal to 2. Note This parameter is required if you set Creation Method to Storage Set Creation. |
| Basic Configurations |   |   |   |
|   | Name | Yes | Enter a name for the disk that you want to create. If you create only one disk, the disk name must be 2 to 128 characters in length. If you create multiple disks at a time, the disk name must be 2 to 125 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
|   | Quantity | Yes | Enter the number of disks that you want to create. Valid values: 1 to 100. |
|   | Specifications | Yes | Select Premium Performance Disk. |
|   | Disk Size | Yes | Specify a disk size in the range of 20 GiB to 32,768 GiB. |
|   | Multi-attach | Yes | Select Yes to enable the multi-attach feature for the disk. |
|   | Encryption | No | Select whether to encrypt created disks. |

|   | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required if you set Encryption to Yes. Valid values: AES256 SM4 |
|---|---|---|---|
|   | Encryption Key | No | Select the key that you want to use to encrypt the disk. This parameter is required if you set Encryption to Yes. Note If no keys are available, create a key in Key Management Service (KMS). |
|   | Use Snapshot | No | Select whether to create the disk from a snapshot. If you select Yes, you must select a snapshot. In this case, the size of the created disk may be affected by the snapshot size. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is smaller than the snapshot size, the disk is created with the snapshot size. |

> **Note:** For more information about how to create disks, see Create a disk.

6. Confirm the configurations and click **Submit**.
7. In the message that appears, click **OK**.
After the disk is created, go back to the **Disks** page. On the page, you can view the created disk that is in the **Available** state and has the multi-attach feature **enabled**.

**Step 2: Attach the premium performance disk to multiple**

**instances that support the NVMe protocol**

Before you attach the premium performance disk to instances, make sure that the following requirements are met: The premium performance disk and the instances reside in the same zone. The instance families and images of the instances comply with the NVMe protocol. For more information, see Overview of disks that support NVMe.
1. Obtain the IDs of the instances to which you want to attach the disk.
In the left-side navigation pane, choose **Instances & Images > ECS Instances**. On the
**Instances** page, view and copy the instance ID in the instance list.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. Use the instance ID to search for the premium performance disk that you want to attach to
the instance. Then, click the icon in the **Actions** column corresponding to the disk, and select **Attach**.
4. In the **Attach** dialog box, select an instance ID from the **Instance** drop-down list and click
**OK**.
You must select the instance ID that you obtained in Step 1 from the **Instance** drop-down list.

> **Note:** You can attach the premium performance disk to only a single instance each time you perform the preceding steps. To attach the premium performance disk to multiple instances, repeat the preceding steps.

You can go to the **Disks** page to view the state of the premium performance disk. The state of the disk is displayed as **Running** on this page. You can click the name of the premium performance disk to go to the **disk details** panel. In the **Attachment Information** section of this panel, you can view information about the premium performance disk that is attached to a single instance or multiple instances.

**What to do next**

After the premium performance disk is attached to multiple instances, we recommend that you create cluster file systems based on your business requirements. Common cluster file systems include OCFS2, GFS2, Veritas CFS, Oracle ACFS, and DBFS.

> **Warning:** When a premium performance disk for which the multi-attach feature is enabled is attached to multiple ECS instances, data cannot be synchronized among the instances and data inconsistency may occur if file systems such as EXT2, EXT3, EXT4, XFS, and New Technology File System (NTFS) are used.

### 6.12 Encrypt a disk

#### 6.12.1 Overview

Disk encryption is a simple and secure method provided by Elastic Compute Service (ECS) to encrypt new disks. Disk encryption eliminates the need to create or maintain your own key management infrastructure, to modify existing applications and maintenance procedures, and to perform additional encryption operations. Disk encryption does not have negative impacts on your business. The following types of data can be encrypted in disk encryption operations: Data stored on disks. Data transmitted between disks and instances. Data within instance operating systems is not encrypted. All snapshots created from encrypted disks. These snapshots are encrypted snapshots. Data transmitted from instances to disks is encrypted on the hosts where the instances reside. Ultra disks, standard SSDs, premium performance disks, and standard performance disks can be encrypted by using disk encryption.

> **Note:** By default, shared SSDs and shared ultra disks cannot be encrypted by using disk encryption. To create and encrypt shared SSDs or shared ultra disks, submit a ticket.

#### 6.12.2 Encrypt a system disk

In the scenarios that require data security and regulatory compliance, you can encrypt disks to secure your data that is stored in Elastic Compute Service (ECS). To encrypt system disks, you can encrypt custom images and then use the encrypted custom images to create instances. The system disks of the created instances are automatically encrypted.

**Limits**

You can encrypt system disks only by encrypting custom images. To encrypt a system disk, perform the following steps:
1. (Optional) Step 1: Create a custom image from an instance
2. (Optional) Step 2: Encrypt the custom image
3. Step 3: Use the encrypted custom image to create an instance
If you have created a custom image and encrypted the image, skip Step 1 and Step 2 and proceed to use the encrypted image to create an instance.

**Step 1: Create a custom image from an instance**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance from which you want to create a custom image. In the **Actions** column,
click the icon and then choose **Disk and Image > Create Custom Image**.
5. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
| Sharing Scope | Select the scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Description | Enter a description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

6. Click **OK**.

**Step 2: Encrypt the custom image**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Find the image that you want to manage. In the **Actions** column, click the
icon and then select **Encrypt Image**.
6. In the **Encrypt Image** dialog box, configure the parameters that are described in the
following table.

| Parameter | Description |
|---|---|
| Image ID | The system automatically obtains the ID of the image. You do not need to configure this parameter. |
| Name | Enter a name for the new encrypted custom image. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with acs: or aliyun . The name cannot contain http:// or https:// and can contain letters, digits, periods (.), colons (:), underscores ( ), and _ hyphens (-). |
| Description | Enter a description for the new encrypted custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

7. Click **OK**.

**Step 3: Use the encrypted custom image to create an instance**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance**.
5. On the Create Instance page, configure the parameters.
For more information about how to configure the parameters to create an instance, see Create an instance by using the wizard. In the **Image ID** section, click **Custom Image** and select the custom image that you encrypted in Step 2: Encrypt the custom image from the **Custom Image** drop-down list.
6. Click **Submit**.

**Result**

After the instance is created, you can click its ID to go to the **Instance Details** page. Then, you can click the **Disks** tab and check the value in the **Encrypted** column corresponding to the system disk. If the value is **Yes**, the system disk is encrypted.

#### 6.12.3 Encrypt a data disk

In scenarios that require data security and regulatory compliance, you can encrypt disks to secure your data stored on the disks. After a data disk is created, its encryption state cannot be changed. If you want to encrypt a data disk, encrypt the disk when you create it.

**Background information**

**g**

We recommend that you determine the number and sizes of data disks before you create them. Take note of the following limits:

> **Note:** System disks cannot be created separately.

The maximum number of data disks that can be attached to a single Elastic Compute Service (ECS) instance varies based on the instance type. A single premium performance disk for which the multi-attach feature is enabled can be attached to up to 16 ECS instances at the same time. Each ultra disk, shared ultra disk, standard SSD, shared standard SSD, premium performance disk, or standard performance disk can be up to 32,768 GB in size. Disks cannot be combined in ECS and are independent of each other. You cannot format multiple disks to combine the disks into a single disk. A snapshot can back up data only of a single disk. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across disks. If you use LVM to create a logical volume across multiple existing disks, data discrepancy may occur when you restore disks from snapshots.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Disk**.
5. On the Create Disk page, configure parameters to create a data disk.
If you want to encrypt the data disk, take note of the following parameters:
**Encryption**: Select **Yes**.
**Encryption Method**: Select an encryption algorithm. Valid values:

**AES256**

**SM4**

**Encryption Key**: Select an encryption key.
For more information about other parameters that you can configure for the data disk, see Create a disk.
6. Click **Submit**.

### 6.13 Re-initialize disks

#### 6.13.1 Re-initialize a system disk

This topic describes how to re-initialize a system disk. After a system disk is re-initialized, it is restored to the state that it was in when it was created.

**Prerequisites**

The system disk that you want to re-initialize is in the **Running** state. The Elastic Compute Service (ECS) instance to which the system disk is attached is in the
**Stopped** state.
After a disk is re-initialized, the data stored on the disk is lost and cannot be recovered. Exercise caution when you perform this operation. We recommend that you back up disk data or create snapshots before you re-initialize a disk. For more information, see Create snapshots.

**Background information**

The result of disk re-initialization depends on the disk type and how the disk was created. For the system disk that is attached to an instance, you can re-initialize the disk to restore it to the state that it was in when it was created. The following changes take place after the system disk is re-initialized: The system disk is restored to the state that it was in when it was created.

> **Warning:** When the system disk is re-initialized, all data stored in the disk is deleted. We recommend that you create snapshots for the disk to back up data before you re-initialize the disk.

The automatic snapshot policy applied to the system disk before the re-initialization remains valid. The IP addresses and disk IDs of the instance remain unchanged. The automatic and manual snapshots of the system disk remain available. You can use these snapshots to roll back the disk. For more information, see Roll back a disk by using a snapshot.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the system disk that you want to re-initialize and click **Reinitialize Disk** in the
**Actions** column.
5. In the **Reinitialize Disk** dialog box, configure the parameters described in the following
table.

| Parameter | Description |
|---|---|
| Password | Reset the password used to log on to the instance. You can retain the original password or specify a new password. |
| Confirm Password |   |
| Instance Startup Policy | If you select Start Instance After Re-initializing Disk, the instance automatically starts after you re-initialize the system disk. |

6. Click **OK**.

**Result**

While the disk is being re-initialized, the disk is in the **Initializing** state. When the disk is reinitialized, it enters the **Running** state.

**What to do next**

If data disks are attached to a Linux instance before its system disk is re-initialized, you must re-create mount points for the partitions of the data disks and mount file systems to these partitions.

> **Note:** After you re-initialize the system disk of a Linux instance, data stored in the data disks attached to the instance remains unchanged, but the mount information of the data disks is lost. You must re-create mount points for the partitions of the data disks and mount file systems to these partitions.

After the system disk is re-initialized, you must redeploy applications and configurations to restore your business. If you have created a snapshot for the system disk before the system disk is re-initialized, you can use the snapshot to create a data disk and attach the data disk to the instance to obtain data that was originally stored in the system disk. For more information, see Create snapshots.

#### 6.13.2 Re-initialize a data disk

When a data disk is attached to an Elastic Compute Service (ECS) instance, you can reinitialize the disk to restore it to the state when it is created.

**Prerequisites**

Snapshots are created for your data disk. For more information, see Create snapshots. The data disk is attached to an ECS instance. For more information, see Attach a data disk. The ECS instance is in the **Stopped** state. For a Linux instance, if you create an empty data disk and add a command in the /etc/fstab file to mount partitions of the data disk on system startup, the command is not executed and the instance cannot start as expected after you re-initialize the data disk. We recommend that you comment out the command in the /etc/fstab file. Perform the following steps: i. Connect to the instance. For more information, see Overview.

| vim /etc/fstab |   |   |
|---|---|---|
| e | I | key to ente |

iv. Find the command used to mount data disk partitions and comment out the command by `#`), as shown in the following command line. using a number sign (

```bash
# /dev/vdb1 /InitTest ext3 defaults 0 0
```

> **Note:** In this example, /dev/vdb1 is a partition and /InitTest is a mount point. You can modify the command based on your business requirements.

`:wq` to save the file and exit. v. Press the `Esc` key to exit the edit mode, and enter

**Background information**

The state of a data disk after it is re-initialized varies based on its original state when it was created and the operating system that the instance runs: The data disk is restored to the initial state when it was created: The data disk becomes an empty disk if it was originally an empty disk. The data disk stores the data recorded in the source snapshot if the data disk was created from a snapshot. For a Windows instance, after you re-initialize a data disk, the data disk is ready for use without the need for additional operations regardless of its original state. For a Linux instance: If a data disk was created from a snapshot, the data disk stores only the data recorded in the source snapshot after the data disk is re-initialized. You do not need to re-mount the partitions, but all the data generated after the disk was created is lost. If a data disk was created as an empty disk, all the data and file systems on the disk are lost after the data disk is re-initialized. You must reformat and partition the disk, and then re-mount the partitions.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to re-initialize, and click **Re-initialize Disk** in the **Actions**
column.
5. In the **Re-initialize Disk** dialog box, click **OK**.

**What to do next**

For a Linux instance, if the data disk was created as an empty disk, you must format the data disk after you re-initialize it. For more information, see Format a data disk for a Linux instance. After the data disk is re-initialized, you must redeploy the applications and reconfigure the parameters on the disk to restore your business at the earliest opportunity.

### 6.14 Detach a data disk

If a data disk is no longer needed by an Elastic Compute Service (ECS) instance, you can detach the disk from the instance. You can also detach a data disk from an instance and then attach the disk to another instance within the same zone. This topic describes how to detach a data disk.

**Prerequisites**

Before you detach a data disk, make sure that the following conditions are met: The disk is attached to an instance and **Running** is displayed in the **Status** column that corresponds to the disk in the ECS console. To prevent data loss and ensure data integrity, we recommend that you stop read and write operations on the disk before you detach it.

**Background information**

Perform the following steps to detach a data disk.

> **Note:** Local disks that are used as data disks cannot be detached.

1. If file systems are mounted to the partitions of the data disk, unmount the data disk from
within the operating system of the instance to which the data disk is attached. For more information, see the Step 1: Unmount the data disk from within the operating system of the instance to which the disk is attached section in this topic.
2. Detach the data disk on the Disks page.
For more information, see the Step 2: Detach the data disk on the Disks page section in this topic.

**Step 1: Unmount the data disk from within the operating**

**system of the instance to which the disk is attached**

If the data disk is partitioned and has file systems mounted, perform the following operations to unmount the data disk from within the operating system of the instance to which the disk is attached:

**For a Linux instance, perform the following procedure.**

1. Connect to the instance.
For more information, see Overview.
2. Run the following command to view the mount information of the data disk:

```
df -h
```

A command output similar to the following one is displayed. In this example, the /dev/vdb1 partition of the data disk is used. In actual scenarios, look up the command output for the data disk partitions whose mount information you want to view.
3. Run the umount command to unmount the file systems from the data disk partitions.
For example, you can run the following command to unmount the file system from the /dev/vdb1 partition of the data disk:

```
umount /dev/vdb1
```

4. Run the following command to view the UUIDs of the data disk partitions:

```
blkid
```

The following command output shows the UUID of the /dev/vdb1 partition of the data disk.
5. Run the following command to check whether automatic mounting is configured in the
/etc/fstab file for the file systems in the data disk partitions:

```
cat /etc/fstab
```

Find the UUID obtained in the previous step in the command output. The file system mounted to the /dev/vdb1 partition is configured in /etc/fstab, as shown in the following figure.
6. Delete the automatic mounting configurations of the file systems in the data disk partitions
from /etc/fstab.

> **Note:** If you do not delete the automatic mounting configurations of the file systems in the data disk partitions from /etc/fstab, the instance cannot be restarted after you detach the data disk from the instance in the ECS console.

i. Run the following command to edit /etc/fstab:

```
vim /etc/fstab
```

ii. Press the `I` key to enter the edit mode. iii. Delete or comment out the automatic mounting configurations of the file systems in the data disk partitions. For example, you can add the number sign ( `#` ) before the line of the automatic mounting configuration to comment it out, as shown in the following figure. iv. Press the Esc key, enter `:wq` , and then press the Enter key to save your changes and exit the edit mode.

**For a Windows instance, perform the following procedure.**

> **Note:** In this example, Windows Server 2012 R2 is used.

1. Connect to the instance.
For more information, see Overview.
2. On the Windows Server desktop, click the **Server Manager** icon in the lower-left corner.
3. In the upper-right corner of the **Server Manager** window, choose **Tools > Computer**
**Management**.
4. In the left-side navigation pane, choose **Computer Management (Local) > Storage >**
**Disk Management**.
5. Right-click the disk that you want to unmount and select **Offline**.

**Step 2: Detach the data disk on the Disks page**

You can detach disks from instances on the Disks or Instances page in the ECS console. This section describes how to detach a data disk on the Disks page.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to detach, click the
icon in the **Actions** column, and then click **Detach**.
5. In the message that appears, click **Detach**.
Alternatively, you can go to the Instance Details page of the associated instance and detach the data disk from the instance on the **Disks** tab.

**Result**

After you perform the preceding steps to detach the data disk, you can choose **Storage &**
**Snapshots > Disks** to find the disk on the Disks page. If **Available** is displayed in the
**Status** column, the disk is detached.

**What to do next**

You can attach the data disk to another instance within the same zone. For more information, see Attach a data disk. When the data disk is no longer needed, you can back up data stored on the disk and then release the disk. For more information, see Create snapshots and Release a data disk.

### 6.15 Release a data disk

You can manually release disks that are no longer needed. When a disk is released, all data stored on the disk is deleted. This topic describes how to release a data disk on the Disks page.

**Prerequisites**

A snapshot is created for the data disk that you want to release to back up disk data. For more information, see Create snapshots. The data disk is in the **Available** state. If the data disk is attached to an instance, you must detach the disk before you can release it. For more information, see Detach a data disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to release, click the
icon in the **Actions** column, and then click **Release**.
5. In the message that appears, click **Release**.

## 7 Images

### 7.1 Overview

This topic describes the concepts, types, and formats of images and how to view the information of an image.

**Image overview**

An image is a template for running environments within Elastic Compute Service (ECS) instances. An image includes an operating system and pre-installed applications. An image works as a copy that stores data from one or more disks. An ECS image may store data from a system disk or from both system and data disks. You can use an image to create an ECS instance or replace the system disk of an ECS instance.

**Image types**

ECS images are classified into public images, custom images, shared custom images, and globally shared images based on image sources.

> **Note:** Image types and image versions are displayed in the ECS console.

| Image type | Description | References |
|---|---|---|

| Public images | Public images provided by Alibaba Cloud in Apsara Stack support the following Windows Server operating systems and mainstream Linux operating systems. | Overview of public images |
|---|---|---|
| Custom images | Custom images are created from instances or snapshots or are imported from your on-premises device. | Overview of custom images |
| Shared custom images | These images are shared with your organization by other Level-1 organizations. | Overview of shared images |
| Globally shared images | These images are custom images that are globally shared by administrators in the Apsara Uni-manager Operations Console. Globally shared images can be viewed and used by all organizations. | Overview of globally shared images |

**Find an image**

You can find an image based on its type, name, ID, or the ID of the snapshot from which the image was created. Then, you can use the image to create instances or perform other operations. The following table provides links to the relevant references.

| Image type | References |
|---|---|
| Public images | Find a public image |
| Custom images | Find a custom image |
| Shared images | Find a shared custom image |
| Globally shared images | Find a globally shared image |

**Image formats**

ECS supports images in the VHD, RAW, and QCOW2 formats. Images in other formats must be converted to the supported formats before they can be run in ECS. For more information, see Convert the format of an image.

### 7.2 View instances that use a specific image

**specific image**

You can view instances that use a specific image to obtain the usage details of the image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click a tab that corresponds to the type of the image that you want to view.
The following table describes the operations that you can perform to go to each tab on the Images page.

| Image type | Operation |
|---|---|
| Custom Image | Choose ECS Image > Custom Image. Note To quickly find and manage custom images that are shared by the current organization, choose ECS Image > Shared Image > Shared by Me. |
| Public Image | Choose ECS Image > Public Image. |
| Shared Image | i. Choose ECS Image > Shared Image. ii. Click Shared. |
| Shared Globally | i. Choose ECS Image > Shared Image. ii. Click Shared Globally. |

5. Find the image and click **Related Instances** in the **Actions** column.

**Result**

Instances that use the specified image are displayed on the Instances page. You can continue to perform other operations on the instances, such as updating the image.

### 7.3 Public images

#### 7.3.1 Overview

Public images are images that are provided by Alibaba Cloud to create a safe, stable running environment for applications that are deployed on Elastic Compute Service (ECS) instances. This topic describes the types of public images: Alibaba Cloud Linux images, third-party images, and open-source images.

**Type of public images**

Public images provided by Alibaba Cloud in Apsara Stack support almost all Windows Server operating systems and mainstream Linux operating systems. The following table describes two types of public images provided by Alibaba Cloud.

| Type of public image | Description | Technical support |
|---|---|---|
| Alibaba Cloud Linux images | Alibaba Cloud Linux images are custom, proprietary operating system images provided by Alibaba Cloud for ECS instances. Alibaba Cloud Linux images are thoroughly tested to ensure their security, stability, and normal startup and operation. | Alibaba Cloud provides technical support to help resolve the issues that you may encounter when you use Alibaba Cloud Linux images. |
| Third-party images and open- source images | Third-party and open-source images are thoroughly tested and released by Alibaba Cloud to ensure their security, stability, and normal startup and operation. The following third-party public images are available: Windows: Windows Server Linux: Anolis OS CentOS CentOS Stream AlmaLinux Rocky Linux Debian Ubuntu OpenSUSE SUSE Linux Kylin UOS NFS | We recommend that you contact corresponding operating system vendors or open source communities for technical support. Alibaba Cloud also provides technical support to help identify image issues. |

**Alibaba Cloud Linux images**

Alibaba Cloud Linux images are Linux public images developed in-house by Alibaba Cloud. The following Alibaba Cloud Linux images are available in both the x86 and ARM architectures: Alibaba Cloud Linux 3 Alibaba Cloud Linux 2

**Third-party images and open-source images**

Alibaba Cloud provides third-party images and open-source images. The following table describes the operating system and instance family of each image.

> **Note:** You can view or find other public images that are available in the ECS console. For more information, see Find a public image.

x86

| Instance family | Operating system | Version |
|---|---|---|
| Intel | Windows Server | Windows Server 2022 Datacenter 64-bit (Simplified Chinese) Windows Server 2022 Datacenter 64-bit (English) |
|   |   | Windows Server 2019 Datacenter 64-bit (Simplified Chinese) Windows Server 2019 Datacenter 64-bit (English) |
|   |   | Windows Server 2016 Datacenter 64-bit (Simplified Chinese) Windows Server 2016 Datacenter 64-bit (English) |
|   |   | Windows Server 2012 R2 Datacenter 64-bit (Simplified Chinese) Windows Server 2012 R2 Datacenter 64-bit (English) |
|   | CentOS | CentOS 7.2 CentOS 7.3 CentOS 7.4 CentOS 7.5 CentOS 7.5 (SCC) CentOS 7.6 CentOS 7.7 CentOS 7.8 (Trusted) CentOS 7.9 CentOS 7.9 (SCC) CentOS 7.9 (UEFI) |
|   | CentOS Stream | CentOS Stream 8 |
|   | AlmaLinux | AlmaLinux 8.6 AlmaLinux 9.0 |

|   | Rocky Linux | Rocky Linux 8.6 Rocky Linux 9.0 |
|---|---|---|
|   | Debian | Debian 10.12 Debian 11.4 Debian 10.12 (UEFI) |
|   | Ubuntu | Ubuntu 18.04 Ubuntu 22.04 Ubuntu 18.04 (UEFI) Ubuntu 20.04 (UEFI) |
|   | OpenSUSE | OpenSUSE 15.4 |
|   | Anolis OS | Anolis OS 7.9 ANCK Anolis OS 7.9 ANCK (Level 3 of MLPS 2.0) Anolis OS 7.9 ANCK 64-bit (UEFI) Anolis OS 8.6 ANCK Anolis OS 8.6 ANCK (Level 3 of MLPS 2.0) Anolis OS 8.6 ANCK (UEFI) Anolis OS 8.4 ANCK (SCC) Important Only ecs.sccg7x-roce-x25 instances can use Anolis images. |
| Intel hygon |   |   |
|   | SUSE Linux | SUSE Linux Enterprise Server 12 SP5 SUSE Linux Enterprise Server 15 SP3 |
|   | Kylin | Kylin V10 SP1 0518 Kylin V10 0524 SP2 Kylin V10 0524 SP2 (UEFI) |
|   | UOS | UOS Server 20 1002a UOS Server 20 1050a u1 UOS Server 20 1050a u1 (UEFI) |
|   | NFS | NFS V4 |

ARM

| Instance family | Operating system | Version |
|---|---|---|
| Kunpeng Feiteng | Anolis OS | Anolis OS 7.9 ANCK for ARM Anolis OS 7.9 ANCK for ARM (Level 3 of MLPS 2.0) Anolis OS 8.6 ANCK for ARM (Level 3 of MLPS 2.0) Anolis OS 8.6 ANCK for ARM |
|   | Kylin | Kylin V10 SP1 0518 Kylin V10 SP2 0524 |
|   | UOS | UOS Server 20 1002a UOS Server 20 1050a u1 |
|   | CentOS | CentOS 7.9 |

**Related operations**

The following table describes the operations that can be performed on public images.

| Operation | Description | References |
|---|---|---|
| Find an image | You can view public images that are available in the current organization in the ECS console. You can search for a specific public image by image type, name, or ID. | Find a public image |
| View instances that use a specific image | You can view instances that use a specific public image to obtain the usage details of the image. | View instances that use a specific image |

#### 7.3.2 Find a public image

You can view the details of all public images that are available in the current organization, region, and resource set in the Elastic Compute Service (ECS) console. You can find a specific public image by image name or ID. Then, you can create instances from the image or perform other operations on the image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Public Image**.
On the public image list, view the details of the public image that you want to manage, such as the image ID, name, and startup mode in the **Image ID/Name** and **Startup Mode** columns.
5. Click Advanced Filter and specify one or more filter conditions. The image list displays
images that match the specified conditions.

| Filter option | Description |
|---|---|
| Image ID | You must enter an exact image ID. |
| Image Name | You must enter an exact image name. |

### 7.4 Custom images

#### 7.4.1 Overview of custom images

Custom images are created from Elastic Compute Service (ECS) instances or snapshots or imported from your on-premises device. Custom images can contain applications and data. You can use custom images to create instances that have identical configurations. This eliminates the need to make repeated configurations. After you create or import a custom image, the image is in the **Available** state. You can share the image with other organizations, export the image to an Object Storage Service (OSS) bucket, or use the image to create instances. If you no longer need the image, you can delete the image.

> **Note:** Only the creator of a custom image can use, share, copy, and delete the image.

The following figure shows how to use a custom image.

**Related operations**

The following table describes the operations that you can perform on custom images.

| Operation | Description | References |
|---|---|---|
| Create an image | You can create a custom image from an instance or from a snapshot to copy the system environment. This eliminates the need to make repeated configurations. | Create a custom image |
| Modify an image | You can modify the name and description of a custom image. | Modify the attributes of a custom image |
| Find an image | You can view all custom images in the current organization, region, and resource set in the ECS console. You can find a specific image by image name or ID. | Find a custom image |
| View instances related to an image | You can view instances that were created from a specific image to obtain image usage information. | View instances that use a specific image |

| Share an image | After you create a custom image, you can share the image with other organizations. After the image is shared, you can go to the ECS Image tab of the Images page, click the Shared Image tab, and then click Shared by me to view the image. | Share a custom image Modify the sharing scope of a custom image |
|---|---|---|
| Encrypt a custom image | You can encrypt custom images as needed. After a custom image is encrypted, you can use the encrypted custom image to create instances that have encrypted system disks. This helps meet data security and compliance requirements. | Encrypt a custom image |
| Configure the boot mode of an image | You can specify Basic Input Output System (BIOS) or Unified Extensible Firmware Interface (UEFI) as the boot mode of a custom image based on your business requirements. | Configure the boot mode of a custom image |
| Import an image | You can import a custom image from your on-premises device. | Limits on importing images. |
| Export a custom image | You can export a custom image that you created to an OSS bucket and then download the image to your on-premises device. | Export a custom image |
| Delete an image | You can delete a custom image that you no longer need. | Delete custom images |

#### 7.4.2 Create a custom image

You can create a custom image and use it to create identical instances or replace the system disks of existing instances.

**Create a custom image from a snapshot**

You can create a custom image from a system disk snapshot to load the operating system and data environment of the snapshot to the image. Before you perform this operation, make sure that the snapshot to use is a system disk snapshot. Custom images cannot be created from only data disk snapshots.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find a system disk snapshot. If **System Disk** is displayed in the **Disk Type (ALL)** column
corresponding to a snapshot, the snapshot is a system disk snapshot. In the **Actions** column, click **Create Custom Image**.
5. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Sharing Scope | Select the scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
| Image Description | Enter a description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

6. Click **OK**.

**Create a custom image from an instance**

You can create a custom image from an instance to replicate the data of the system disk and data disks on the instance.

> **Note:** To prevent data security risks, we recommend that you delete sensitive data from an instance before you use the instance to create a custom image.

When you create a custom image from an instance, a snapshot is automatically generated for each disk on the instance, and all the snapshots constitute a complete custom image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance from which you want to create a custom image. In the **Actions** column,
click the icon and then choose **Disk and Image > Create Custom Image**.
5. Configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|

| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
|---|---|
| Sharing Scope | Select the scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Description | Enter a description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

6. Click **OK**.

#### 7.4.3 Modify the attributes of a custom image

**image**

To facilitate custom image management, you can modify the attributes of a custom image. The attributes include the image name and description.

**Background information**

You can share a custom image with other organizations. After you share the image, you can modify the name or description of the image in the custom image list or shared image list. For more information, see Share a custom image.

**Limits**

You can modify the attributes of only custom images, including custom images that are shared with other organizations. Public images and images that are shared by others cannot have their attributes modified.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Find the custom image that you want to manage and click **Edit** in the **Actions** column.
6. In the **Edit** dialog box, modify the name and description of the custom image.
**Image Name**: The name must be 2 to 128 characters in length. The name cannot start
with a digit or special character. The name can contain underscores (_), hyphens (-), and colons (:).
**Description**: The description must be 2 to 256 characters in length. The description
cannot start with `http://` or `https://` .
7. Click **OK**.

#### 7.4.4 Find a custom image

You can view the details of all custom images that are available in the current organization, region, and resource set in the Elastic Compute Service (ECS) console. You can find a specific custom image by image name or other information. Then, you can create instances from the image or perform other operations on the image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Click Advanced Filter and specify one or more filter conditions. The image list displays
images that match the specified conditions.

| Filter option | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. Fuzzy search is supported. |
| Image Name | Enter an image name to search for the image. Fuzzy search is supported. |
| Snapshot ID | Enter a snapshot ID to search for the images that are associated with the snapshot. Fuzzy search is supported. |
| Tag | Enter the key or value of a tag to search for the images that use the tag. |

**What to do next**

After you find an image that matches the preceding filter options, you can perform the following operations: Create an instance from the image. For more information, see Create an instance by using the wizard. Share the image. For more information, see Share a custom image. Encrypt the image. For more information, see Encrypt a custom image. Export the image. For more information, see Export a custom image. Delete the image. For more information, see Delete a custom image. Modify the attributes (name and description) of the image. For more information, see Modify the description of a custom image.

#### 7.4.5 Share a custom image

##### 7.4.5.1 Share a custom image

You can share a created custom image with other organizations. Then, the organizations can use the shared image to create instances that have identical environments.

**Background information**

Only custom images can be shared. Shared images do not count against the image quotas of the organizations with which the images are shared. The organizations with which images are shared can use the shared images to create instances or replace the system disks of existing instances. You can delete shared images. After a shared image is deleted, the image is no longer visible to the organizations with which the image was shared and the system disks of the instances that were created from the shared image can no longer be re-initialized. Each custom image can be shared with up to 50 organizations. Each time a custom image can be shared with up to 10 organizations.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **ECS Image** tab and then click the **Custom Image** tab to view the custom image
list.

> **Note:** If you want to quickly find the custom image that is shared by the current organization and reshare the image, choose **Shared Image > Shared by Me**.

5. Find the image that you want to manage, click the
icon in the **Actions** column, and then choose **Configure Sharing Settings > Share Image**.
6. In the **Share Image** dialog box, select the organization with which you want to share the
image from the **Organization** drop-down list.

> **Note:** If no organization list is available due to a lack of permissions, you can enter the name of a level-1 organization in the Organization field.

7. Click **OK**.

**Result**

You can choose **Shared Image > Shared by Me** to view the shared custom image list.

**Related operations**

After the custom image is shared, you can perform the following operations based on your business requirements: Remove an organization from the sharee list of the image: In the **Share Image** dialog box, find the organization with which you want to unshare the image in the **Shared Information** list, click the icon in the **Actions** column, and then click **OK**.

> **Important:** If all organizations with which the custom image is shared are deleted, the custom image is removed from the shared by me image list. You can choose **Shared Image >** **Shared by Me** to view the shared by me image list.

Add an organization to the sharee list of the image: In the **Share Image** dialog box, select the organization that you want to add in the
**Organizations** drop-down list and click **OK**.

##### 7.4.5.2 Modify the sharing scope of a custom image

**image**

You can modify the sharing scope of a custom image.

> **Important:** If a custom image is shared with the current organization (including the subordinate organizations) and the current resource set and you shrink the sharing scope, specific users no longer have permissions to manage the custom image. Proceed with caution.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Perform the following operations to modify the sharing scope of the custom image:
Modify the sharing scope of a single custom image a. In the custom image list, find the custom image and click the icon in the **Actions** column. b. Choose **Configure Sharing Settings > Modify Sharing Scope**. c. In the **Modify Sharing Scope** dialog box, configure Sharing Scope. Valid values of Sharing Scope: **Current Organization and Subordinate**
**Organizations**, **Current Resource Set**, and **Current Organization**.
d. Click **OK**. Modify the sharing scopes of multiple custom images

> **Important:** You can modify the sharing scopes of up to 20 custom images at a time.

a. In the custom image list, select multiple custom images and click **Modify Sharing**
**Scope** in the lower part of the page.
b. In the **Modify Sharing Scope** dialog box, configure Sharing Scope. Valid values of Sharing Scope: **Current Organization and Subordinate**
**Organizations**, **Current Resource Set**, and **Current Organization**.
c. Click **OK**.

#### 7.4.6 Encrypt a custom image

This topic describes how to encrypt a custom image to generate a new encrypted custom image.

**Prerequisites**

The custom image is in the **Available** state.

**Background information**

To meet compliance requirements for data security, you can use encrypted custom images to create instances. The system disks of the created instances are automatically encrypted.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Find the image that you want to manage. In the **Actions** column, click the
icon and then select **Encrypt Image**.
6. In the **Encrypt Image** dialog box, configure the parameters that are described in the
following table.

| Parameter | Description |
|---|---|
| Image ID | The system automatically obtains the ID of the image. You do not need to configure this parameter. |
| Name | Enter a name for the new encrypted custom image. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with acs: or aliyun . The name cannot contain http:// or https:// and can contain letters, digits, periods (.), colons (:), underscores ( ), and _ hyphens (-). |
| Description | Enter a description for the new encrypted custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

7. Click **OK**.

**Result**

When the encrypted custom image is being created, you cannot view the creation status of the image in the custom image list. You can choose **Storage & Snapshots > Snapshots** in the left-side navigation pane to view the creation status of the system disk snapshot and data disk snapshots that are contained in the image on the **Disk Snapshots** tab. The disk snapshots are in the **Creating** state. After encryption is complete, you can find a new encrypted custom image and view the name and description of the encrypted image on the Custom Image tab.

#### 7.4.7 Set the boot mode of a custom image

The boot mode is the mode in which the system disk is booted during instance creation. In Elastic Compute Service (ECS), two boot modes are supported: Unified Extensible Firmware Interface (UEFI) and Basic Input/Output System (BIOS). This topic describes how to set the boot mode for a custom image.

**Precautions**

Before you modify the boot mode of a custom image, take note of the following items: You cannot modify the boot mode of a custom image that is used by existing instances. When specify an instance type during instance creation, you can only select an **image** that is supported by the instance type and has a boot mode configured. After you select a custom image to create an instance, the boot modes that are supported by the image are displayed in the ECS console. After you change the boot mode of a custom image to UEFI, the instances that were created from the image start in UEFI mode. Make sure that configurations of the custom image support the UEFI boot mode. Otherwise, the instances cannot start.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Find the image that you want to manage and choose
> **Startup Mode** in the **Actions**

column.
6. In the **Startup Mode** dialog box, configure Startup Mode.
You can set Startup Mode to **BIOS** or **UEFI**.
7. Click **OK**.

**View the results**

In the custom image list, you can find the custom image and view the boot mode of the custom image in the **Startup Mode** column.

#### 7.4.8 Import custom images

##### 7.4.8.1 Limits on importing images

Before you import images to Elastic Compute Service (ECS), you must be familiar with the limits on importing images to ensure image availability and improve import efficiency. This topic describes the limits on importing images. When you import images, take note of the limits described in the following sections: Import Linux images Import Windows images

**Import Linux images**

When you import Linux images, take note of the following limits: Multiple network interfaces are not supported. IPv6 addresses are not supported. Each password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ` ~ ! @ # $ % ^ & * - _ + = | {

```
} [ ] : ; ' < > , . ? /
```

Firewalls must be disabled. By default, port 22 is enabled. A Linux system disk must be 40 GB to 500 GB in size. Dynamic Host Configuration Protocol (DHCP) must be enabled in the images. SELinux must be disabled. The Kernel-based Virtual Machine (KVM) driver must be installed. We recommend that you install cloud-init to configure hostnames, Network Time Protocol (NTP) repositories, and YUM repositories. Table 1. Limits

| Item | Standard operating system image | Non-standard operating system image |
|---|---|---|
| Definition | The following standard 32-bit and 64-bit operating systems are supported: CentOS Ubuntu SUSE OpenSUSE RedHat Debian CoreOS Aliyun Linux Kylin Note Support for standard operating systems may be subject to version changes. You can log on to the ECS console to view the latest supported operating systems. | The following operating systems are regarded as non-standard operating systems: Operating systems that are not supported by Apsara Stack Standard operating systems that do not meet the requirements on critical system configuration files, basic system environments, or applications To use non-standard operating system images, select Others Linux when you import images. If the images that you import are non-standard operating system images, Apsara Stack does not process the instances that are created from these images. After you create an instance from a non-standard operating system image, you must connect to the instance by using the Virtual Network Computing (VNC) feature in the ECS console and then configure the IP address, route, and password of the instance. |

| Critical system configuration file | Do not modify /etc/issue* . Otherwise, the distribution of the operating system cannot be identified by ECS and instance operating systems cannot be created. Do not modify /boot/grub/menu.lst . Otherwise, instance operating systems cannot be started. Do not modify /etc/fstab . Otherwise, partitions cannot be loaded and instance operating systems cannot be started. Do not change /etc/shadow to read-only. Otherwise, the password file cannot be modified and instance operating systems cannot be created. Do not modify /etc/selinux/config to enable SELinux. Otherwise, instance operating systems cannot be started. | Requirements for standard operating system images are not met. |
|---|---|---|
| Basic system environment | Do not adjust the system disk partitions. Only system disks with a single root partition are supported. Make sure that the system disk has sufficient free space. Do not modify critical system files such as /sbin , /bin , and /lib* . Before you import an image, confirm the integrity of the file system. Only ext3 and ext4 file systems are supported. |   |
| Application | Do not install qemu-ga in a custom image. Otherwise, specific services that are required by Apsara Stack may be unavailable. |   |

| Image file format | Only images in the RAW, VHD, or QCOW2 format can be imported. To import images in other formats, use a tool to convert the images to a supported format. We recommend that you import images in the RAW format. Note If you cannot import an image in a different format, convert the image to the RAW format and then import the image. For information about how to convert the format of an image, see Convert the format of an image. When you import images in the VHD format, we recommend that you select image files that have a small transmission footprint, such as image files that do not include a large number of 2-MB files or files larger than 2 TB in size. |   |
|---|---|---|
| Image file size | We recommend that you configure the system disk size based on the virtual disk size rather than the image size. The configured system disk size must be at least 40 GB. |   |

**Import Windows images**

When you import Windows images, take note of the following limits: Each password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ` ~ ! @ # $ % ^ & * - _ + = | { } [ ] : ; ' < > , . ? / . Each password cannot start with /. Imported Windows images do not provide the Windows Activation Service. Firewalls must be disabled. Otherwise, remote logons are not supported. Port 3389 must be enabled. A Windows system disk must be 40 to 500 GB in size. Table 2. Limits

| Item | Description |
|---|---|

| Operating system version | Apsara Stack allows you to import the following 32-bit and 64-bit versions of Windows operating system images: Windows Server 2022 Windows Server 2019 Windows Server 2016 Microsoft Windows Server 2012: Microsoft Windows Server 2012 R2 (Standard Edition) Microsoft Windows Server 2012 (Standard Edition and Datacenter Edition) Microsoft Windows Server 2008: Microsoft Windows Server 2008 R2 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2008 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2003: Microsoft Windows Server 2003 R2 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2003 (Standard Edition, Datacenter Edition, and Enterprise Edition) or later, including Service Pack 1 (SP1) Microsoft Windows 7: Microsoft Windows 7 (Enterprise Edition) Microsoft Windows 7 (Enterprise Edition) Note Support for operating systems may be subject to version changes. You can log on to the ECS console to view the latest supported operating systems. |
|---|---|
| Basic system environment | Multi-partition system disks are supported. Make sure that the system disk has sufficient free space. Do not modify critical system files. Before you import an image, confirm the integrity of the file system. Disks can be partitioned to the master boot record (MBR) format and formatted with New Technology File System (NTFS) file systems. |
| Application | Do not install qemu-ga in an imported image. Otherwise, specific services that are required by Apsara Stack may be unavailable. |

| Image file format | Only images in the RAW, VHD, or QCOW2 format can be imported. To import images in other formats, use a tool to convert the images to a supported format. We recommend that you import images in the RAW format. Note If you cannot import an image in a different format, convert the image to the RAW format and then import the image. For information about how to convert the format of an image, see Convert the image file format. When you import images in the VHD format, we recommend that you select image files that have a small transmission footprint, such as image files that do not include a large number of 2-MB files or files larger than 2 TB in size. |
|---|---|
| Image file size | When you import an image, specify a disk size for the imported image based on the virtual disk size of the image instead of the size of the image file. The system disk capacity can range from 40 GB to 500 GB. |

##### 7.4.8.2 Convert the format of an image

You can import only images in the RAW, VHD, and qcow2 formats to Elastic Compute Service (ECS). To import images in other formats, you must use a tool to convert the images to a supported format. This topic describes how to convert the format of an image in Windows and Linux.

**Background information**

You can use the qemu-img tool to convert an image from the VMDK, VDI, VHDX, qcow1, or QED format to the RAW, VHD, or qcow2 format. You can also convert the format of an image between the RAW, VHD, and qcow2 formats.

**Convert the format of an image on an on-premises Windows**

**computer**

1. Download QEMU.
Visit QEMU Binaries for Windows (64 bit) to download a QEMU installation package for Windows. Select a QEMU version based on your operating system.
2. Install QEMU.
In this example, the installation path is C:\Program Files\qemu.
3. Configure environment variables.
i. Choose **Start > Computer**, right-click Computer, and then select **Properties**. ii. In the left-side navigation pane, click **Advanced system settings**. iii. In the **System Properties** dialog box, click the **Advanced** tab and then click
**Environment Variables**.
iv. In the **Environment Variables** dialog box, find the **Path** variable in the **System**
**variables** section.
If the **Path** variable exists, click **Edit**. If the **Path** variable does not exist, click **New**. v. Add a value for the Path variable. In the Edit System Variable dialog box, enter C:\Program Files\qemu in the **Variable**
**value** field. Separate multiple variable values with semicolons (;) and then click **OK**.
In the New System Variable dialog box, enter Path in the **Variable name** field and enter C:\Program Files\qemu in the **Variable value** field. Then, click **OK**.
4. Open the Command Prompt in Windows and run the `qemu-img --help` command. If a
success output is displayed, the tool is installed.
5. On the command line, run the `cd [Directory of the source image]` command to switch
to the directory of the source image. Example: cd D:\ConvertImage .
6. On the command line, run the `qemu-img convert -f raw -O qcow2 centos.raw`
`centos.qcow2` command to convert the format of the image. Parameter description: `-f` is followed by the source image format. `-O` is case-sensitive. It is followed by the destination image format, source image name, and destination image name. After the image format is converted, the destination image appears in the directory of the source image.

**Convert the format of an image on an on-premises Linux**

**computer**

1. Install qemu-img.
For Ubuntu, run the `apt install qemu-img` command. For CentOS, run the `yum install qemu-img` command.
2. Run the `qemu-img convert -f raw -O qcow2 centos.raw centos.qcow2` command to convert
the image format. Parameter description: `-f` is followed by the source image format. `-O` is case-sensitive. It is followed by the destination image format, source image name, and destination image name.

##### 7.4.8.3 Import an image

After you upload an image from your computer to an Object Storage Service (OSS) bucket, you can import the image as a custom image to Elastic Compute Service (ECS).

**Prerequisites**

An image is made. The image meets the limits and requirements for image import and can be imported in the RAW, VHD, or QCOW2 format. For more information, see Limits on importing images and Convert the format of an image. You are granted the permissions to import images. For more information, see **Enterprise >**
**Permission management** in the Apsara Uni-manager Management Console User Guide in
the Apsara Stack Documentation Center. An image is uploaded from your computer to an OSS bucket by using the OSS console or by calling an OSS API operation. For more information, see **Quick start > Upload objects** in the OSS User Guide or **API reference > Object-related operations > PutObject** in the OSS Developer Guide.

> **Note:** Make sure that the OSS bucket resides in the region to which you want to import the image as a custom image.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Custom Image** tab, click **Import Image**.
5. In the **Import Image** panel, configure the parameters that are described in the following
table.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | The organization to which to assign the custom image. |
| Resource Set | Yes | The resource set to which to assign the custom image. |
| Region | Yes | The region to which to import the image as a custom image. |
| OSS Bucket Name | Yes | The name of the OSS bucket in which the image that you want to import is stored. |
| OSS Object Name | Yes | The name of the OSS object that contains the image file. |
| Image Name | Yes | The name of the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and _ colons (:). It must start with a letter. |

| Sharing Scope | Yes | The scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
|---|---|---|
| Operating System | Yes | The operating system. Valid values: Linux and Windows. |
| System Disk Size | Yes | The size of the system disk on an Elastic Compute Service (ECS) instance. Unit: GB. |
| Architecture | Yes | The operating system architecture. Valid values: x86 64 _ arm64 i386 sw 64 _ Note The architecture types that are displayed in the ECS console prevail. |

| Platform | Yes | The operating system platform. Linux: CentOS Ubuntu SUSE OpenSUSE Debian CoreOS Aliyun Others Linux Note The Linux distributions that are displayed in the ECS console prevail. Windows: Windows Server 2003 Windows Server 2008 Windows Server 2012 Windows Server 2016 Windows Server 2019 Windows Server 2022 |
|---|---|---|
| Startup mode | Yes | The boot mode of the custom image. Valid values: BIOS and UEFI. |
| Image Description | No | The description of the custom image. |
| Add Data Disk Image | No | Imports other images that contain data from data disks. If you select Add Data Disk Image, you must click Add and specify parameters including OSS Bucket Name, OSS Object Name, Image Format, Device Name, and Disk Capacity to add data disk images. |

6. Click **OK**.

**Result**

You can go to the Images page to view the creation progress of the custom image. For more information, see Find an image. When the custom image is created, 100% is displayed in the Progress column.

#### 7.4.9 Export a custom image

You can export custom images to Object Storage Service (OSS) buckets and download the images to your on-premises device.

**Prerequisites**

OSS is activated and an OSS bucket is created. For more information, see **Quick start >**
**Create buckets** in the OSS User Guide in the Apsara Stack Documentation Center.
Your account has permissions to export images. For more information, see **Enterprise >**
**Access control management** in the Apsara Uni-manager Management Console User Guid
e in Apsara Stack Documentation Center.

**Limits**

You can export custom images that are in the RAW, VHD, or QCOW2 format. Custom images can be exported only to their original formats. For example, you can only export RAWformatted custom images in the RAW format.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Find the custom image that you want to export. In the **Actions** column, click **Export**
**Image**.
6. Configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| OSS Bucket | Yes | Select an OSS bucket that resides in the same region as the custom image. |
| OSS Prefix | Yes | Specify a prefix for the name of the custom image object. The prefix can contain 1 to 30 letters or digits. For example, if you set OSS Prefix to Demo, the exported image is named Demo-[Automatically generated object name]. |

7. Click **OK**.
8. **Optional**: In the OSS console, download the custom image file to an on-premises device.
For more information, see **Quick Start > Obtain object URLs** in the OSS User Guide in the Apsara Stack Documentation Center.

#### 7.4.10 Delete a custom image

You can delete custom images that are no longer needed.

**Precautions**

Before you delete a custom image, take note of the following items: After a custom image is deleted, the image can no longer be used to create instances. After a custom image is deleted, the instances that use this image remain available but cannot have their system disks re-initialized. Before you delete a shared image, you must unshare the image. After a shared image is deleted: The accounts from which the image is unshared can no longer query the image by using the Elastic Compute Service (ECS) console or by calling an API operation. The accounts from which the image is unshared can no longer use the image to create instances or replace system disks. The system disks of the instances that were created from the shared image cannot be reinitialized. If you delete a custom image, snapshots contained in the image are not deleted. If you do not want to keep the snapshots, navigate to the Snapshots page and delete the snapshots.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

> **Note:** To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.

5. Use one of the following methods to delete a custom image:
Delete a single image: Method 1: Find the image that you want to delete and click the More icon and then click
**Delete Image** in the **Actions** column.
Method 2: Select the image that you want to delete and click **Delete** in the lower part of the page. Delete multiple images: Select the images that you want to delete and click **Delete** in the lower part of the page.
6. Click **Delete**.

### 7.5 Shared custom images

#### 7.5.1 Overview

Shared custom images are images that are shared with you by other level-1 organizations. You can use shared custom images to create Elastic Compute Service (ECS) instances.

**Introduction**

Shared custom images are images that are shared with you by other level-1 organizations. Shared custom images provide the following features: Shared custom images do not count against the image quota of the sharee. To modify a shared custom image, you must contact the sharer of the image. You can use a shared custom image to create instances. For more information, see Create an instance by using the wizard.

**Related operations**

The following table describes the operations that can be performed on shared custom images.

| Operation | Description | References |
|---|---|---|
| View images | You can view shared custom images that are available in the current organization in the ECS console. You can find a specific shared custom image by image type, image name, image ID, or snapshot ID. | Find a shared custom image |
| View instances that use a specific image | You can view instances that use a specific shared custom image to obtain the usage details of the image. | View instances that use a specific image |

#### 7.5.2 Find a shared custom image

You can find a specific shared custom image by image name or ID in the Elastic Compute Service (ECS) console. Then, you can create instances from the image or perform other operations on the image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Shared Image**.
5. Click **Shared**.
You can view details of custom images that were shared by others, such as the image ID, image name, and startup mode in the **Image ID/Name** and **Startup Mode** columns.
6. Click Advanced Filter and specify one or more filter conditions. The image list displays
images that match the specified conditions.

| Filter option | Description |
|---|---|
| Image ID | You must enter an exact image ID. |
| Image Name | You must enter an exact image name. |

### 7.6 Globally shared images

#### 7.6.1 Overview

Globally shared images are available to all organizations. You can use globally shared images in your organization to create Elastic Compute Service (ECS) instances.

**Introduction**

Globally shared images are the custom images that are globally shared by administrators in the Apsara Uni-manager Operations Console. Globally shared images provide the following benefits: After a custom image is globally shared, it appears in the list of globally shared images for each organization. Globally shared images can be modified only by the administrators who share the images.

> **Note:** For information about how to modify a globally shared image, see **ECS operations** **and maintenance > ECS > Images > Manage images** in the ECS Operations and M aintenance Guide in the Apsara Stack Documentation Center.

If your custom image is configured as a globally shared image, the image is displayed in both the custom image list and globally shared image list. You can use a globally shared image to create ECS instances. For more information, see Create an instance by using the wizard.

**Related operations**

The following table describes the operations that you can perform on globally shared images.

| Operation | Description | References |
|---|---|---|

| View images | You can view the globally shared images in the current organization in the ECS console. You can search for globally shared images by image type, image name, or image ID. | Find a globally shared image |
|---|---|---|
| View instances that use a specific image | You can view the ECS instances that use a specific globally shared image to obtain the usage information of the image. | View instances that use a specific image |

#### 7.6.2 Find a globally shared image

You can view the information of globally shared images in the Elastic Compute Service (ECS) console. You can also search for globally shared images by image name or ID and then use the images to create instances or perform other operations.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **ECS Image** tab, click the **Shared Image** tab.
5. Click **Shared Globally**.
You can view image information in the global shared image list, such as **Image ID/Name**,
**Image Size**, and **Startup Mode**.
6. Select a filter option from the drop-down list and enter relevant information to search for
images.

| Filter option | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. |
| Image Name | Enter an image name to search for the image. |

## 8 Snapshots

### 8.1 Overview

You can back up data on your disks by taking point-in-time snapshots. Then, you can use the snapshots to restore your disk data to the point in time when the snapshots are taken. This topic describes the scenarios for using snapshots and the mechanisms of creating and deleting snapshots. This topic also describes the operations related to snapshots.

**Scenarios**

You can use snapshots for scenarios such as environment replication and disaster recovery: You may want to use the data of a disk as the source data for write operations or save data to a different disk. In this case, you can create a snapshot for a disk and then create another disk from the snapshot. The new disk contains the data of the original disk. Issues such as application errors or malicious read operations and write operations may occur on disks that store data. As a result, these disks require additional protection mechanisms. You can create snapshots at regular intervals to restore data to a previous point in time when data errors occur.

**How snapshots are created**

**Description**

Snapshots are classified into full snapshots and incremental snapshots. The first snapshot that you create or retain for a disk is a full snapshot. The snapshot contains all data blocks that are written to the disk at the time of snapshot creation except for empty data blocks. Subsequent snapshots that you create from the disk are incremental snapshots that store only data blocks that have changed since the last snapshot. The metadata of both full snapshots and incremental snapshots includes the information of all data blocks. When you roll back a disk by using a snapshot, you can restore all disk data to the point in time at which the snapshot is created.

> **Note:** After a disk is initialized, it is divided into multiple data blocks based on logical block addresses (LBAs). These data blocks are the minimum granularity of data backup for snapshots. When data is written to the data blocks, every changed data block is marked to be copied in the next snapshot. Data written to and modified in the disk do not affect the existing snapshots. Snapshots do not affect the original disk data.

**Example**

Data is written to a disk of an Elastic Compute Service (ECS) instance at 10:00:00 and 11:00:00. The following section describes how snapshots are created for the disk:
1. At 9:00:00, the disk contains data blocks A, B, and C, and the first snapshot (Snapshot 1) is
created for the disk. Data blocks A, B, and C are all backed up in Snapshot 1. Snapshot 1 is a full snapshot that backs up all data on the disk.
2. Data continues to be written to the disk. Data block A is changed to A1, data block B is
changed to B1, and data block D is added. The second snapshot (Snapshot 2) is created at 10:00:00 for the disk. Snapshot 2 is an incremental snapshot that backs up only the changed data blocks A1, B1, and D. The metadata of Snapshot 2 includes the information of all data blocks A1, B1, C, and D of the disk. The entire data block C is contained in Snapshot 1.
3. Data continues to be written to the disk. Data block C is changed to C1 and data block E is
added. The third snapshot (Snapshot 3) is created at 11:00:00. Snapshot 3 is an incremental snapshot that backs up only the changed data blocks C1 and E. The metadata of Snapshot 3 includes the information of all data blocks A1, B1, C1, D, and E of the disk. The entire data blocks A1, B1, and D are contained in Snapshot 2.
4. The preceding processes are repeated.

**How snapshots are deleted**

**Description**

In contrast to creating a snapshot, when you delete a snapshot, space is freed up based on the data blocks contained in the snapshot and the data block mappings. When the first snapshot of a disk is deleted, the first incremental snapshot inherits the attributes of this deleted snapshot to become a full snapshot. If the disk has only the full snapshot that is deleted, the first snapshot to be created for the disk later is a full snapshot that backs up all data blocks written since the disk is created.

**Example**

Snapshot 1, Snapshot 2, and Snapshot 3 are created for a disk of an ECS instance. The following section describes the data blocks contained in each snapshot: Snapshot 1: contains data blocks A, B, and C. Snapshot 2: contains data blocks A1 (changed from data block A), B1 (changed from data block B), C (unchanged), and D (new data block). The entire data block C is contained in Snapshot 1. Snapshot 3: contains data block A1 (unchanged), B1 (unchanged), C1 (changed from data block C), D (unchanged), and E (new data block). The entire data blocks A1, B1, and D are contained in Snapshot 2. The following section describes how the disk snapshots are deleted:
1. Snapshot 1 is deleted at 14:00:00. Data blocks A and B contained in Snapshot 1 are not
referenced and are directly deleted. Data block C is retained because it is referenced by Snapshot 2. Snapshot 2 becomes a full snapshot and contains data blocks A1, B1, C, and D. Snapshot 3 is still an incremental snapshot.
2. Snapshot 2 is deleted at 15:00:00. Data block C contained in Snapshot 2 is not referenced
and is directly deleted. Data blocks A1, B1, and D are referenced by Snapshot 3 and are retained. In this case, Snapshot 3 becomes a full snapshot and contains data blocks A1, B1, C1, D, and E.
3. Snapshot 3 is deleted at 16:00:00. All data blocks in Snapshot 3 are not referenced and are
deleted.

**Operations related to snapshots**

You can use snapshots based on your business requirements. The following table describes operations related to snapshots.

> **Note:** Snapshots are stored in Object Storage Service (OSS), but are hidden. Snapshots do not occupy storage space in OSS buckets. Snapshot operations can be performed only in the ECS console or by calling API operations. This topic describes snapshot operations that can be performed in the ECS console. For information about how to call API operations to manage snapshots, see **ECS Developer Guide**.

| Operation | Description | Procedure |
|---|---|---|

| Create snapshots | You can use the following methods to create snapshots: You can manually create snapshots. Manually created snapshots are called manual snapshots. You can create manual snapshots before you perform high-risk operations to improve fault tolerance. You can create snapshots for a single disk or create snapshots for multiple disks on one or more ECS instances by creating a snapshot-consistent group. You can create automatic snapshot policies to create snapshots. Snapshots created based on these policies are called automatic snapshots. After you create an automatic snapshot policy and apply it to a disk, the system creates snapshots for the disk at the points in time specified in the policy. You can use automatic snapshots to back up data and improve the security of your business data. | Create snapshots Create a snapshot-consistent group Create an automatic snapshot policy |
|---|---|---|
| Delete snapshots | When you want to free up space or when the maximum number of snapshots is reached, you can delete snapshots that are no longer needed. | Delete snapshots |
| Roll back disks by using snapshots | When the system is unresponsive or when accidental changes are made, you can roll back a disk to a previous version by using one of its snapshots. | Roll back a disk by using a snapshot |
| Create an image from a system disk snapshot | You can create a custom image from a snapshot that contains the operating system and data of an ECS instance. Then, you can use the custom image to create multiple instances that have identical application environments. | Create a custom image |
| Create a disk from a snapshot | A single snapshot can be used to create multiple identical disks. | Create a disk |

### 8.2 Disk snapshots

#### 8.2.1 Create snapshots

You can use snapshots to back up data, restore Elastic Compute Service (ECS) instances that are accidentally released, and create custom images. You can create snapshots of disks to improve fault tolerance before you roll back a disk, modify key system files, or change the operating system of an instance.

**Prerequisites**

The associated instance of the disk for which you want to create a snapshot is in the
**Running** or **Stopped** state.
The disk is in the **Running** state.

**Background information**

Up to 64 snapshots can be retained for each disk. Snapshots can be used in the following scenarios: Roll back data on disks For more information, see Roll back a disk by using a snapshot. For more information, see Create a custom image from a snapshot. Data disk snapshots cannot be used to create custom images. Create a data disk from a data disk snapshot To create a data disk from a snapshot, set Use Snapshot to Yes and then specify a snapshot on the Create Disk page. For more information, see Create a disk. The size of the created disk is determined based on the size of the specified snapshot and cannot be changed. When you re-initialize a data disk created from a snapshot, the disk is restored to the state of the snapshot. When you create a snapshot, take note of the following items: For each disk, the first snapshot is a full snapshot and subsequent snapshots are incremental snapshots. A longer period of time is required to create the first snapshot. The period of time that is required to create an incremental snapshot varies based on the volume of data that is modified after the point in time when the previous snapshot is created. If a large volume of data is modified, a long period of time is required to create the snapshot.

> **Note:** If you want to use a snapshot immediately after the snapshot is created, you can enable the instant access feature.

We recommend that you create snapshots during off-peak hours. While a snapshot is being created for an instance, do not perform operations that will change the instance state, such as stopping or restarting the instance.

> **Important:** If the state of the ECS instance changes, the snapshot cannot be created.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk for which you want to create a snapshot and click **Create Snapshot** in the
**Actions** column.
5. In the **Create Snapshot** dialog box, configure the parameters described in the following
table and click **OK**.

| Parameter | Description |
|---|---|
| Snapshot Name | The name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. The name can contain digits, letters, colons (:), underscores ( ), and hyphens (-). _ Note The name cannot start with auto because snapshots whose names start with auto are recognized as automatic snapshots. |
| Instant Access | The instance access feature can accelerate the snapshot creation process. You can use the instant access feature to create snapshots within seconds. Enable Instant Access: You can select this check box to enable the instant access feature. By default, this feature is disabled. Note The instance access feature can be enabled for standard performance disks and premium performance disks. Duration of Instant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. Valid values: 1 to 65535. |
| Snapshot Description | The description of the snapshot. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

You can go to the Snapshots page to check the creation progress of the snapshot. For more information, see View snapshot details. After the snapshot is created, 100% is displayed in the Progress column.

#### 8.2.2 View snapshot details

You view the details of created snapshots, including the snapshot names, snapshot IDs, snapshot status, snapshot creation time, names of the source disks (disks from which the snapshots are created), IDs of the source disks, and types of the source disks. You can also view the details of the custom images and disks that are created from a snapshot.

> **Note:** You can view the details of all snapshots that are created from a disk on the Disk Snapshots tab of the disk. For more information, see View disk details.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
Clickthe **Disk****Snapshots**tab
4. Click the **Disk Snapshots** tab.
5. On the Disk Snapshots tab, you can view the details of existing snapshots.
On the Disk Snapshots tab, you can find a snapshot list that consists of multiple columns, including the following ones: **Snapshot ID/Name**, **Status**, **Organization/Resource Set**,
**Instant Access**, **Disk ID/Name**, **Disk Capacity**, **Disk Type (All)**, and **Snapshot Type**.
You can perform the following steps to customize the snapshot list to include specific columns: i. In the upper-right corner of the snapshot list, click the icon. ii. In the **Custom Columns** dialog box, select the columns that you want to include and click **OK**.
6. Use one of the following methods to find a snapshot whose details you want to view:

> **Note:** Search snapshots by using the **Snapshot Name**, **Snapshot ID**, **Disk ID**, **Creation Time**, or **Filter by Tag** filter option.
> Only the **Snapshot Name** and **Snapshot ID** filter options support fuzzy search.

Select a filter option from the drop-down list and enter relevant information to search for snapshots. Click **Advanced Filter**, specify multiple filter options, and then click **Search**. The snapshots that match the filter conditions are displayed in the snapshot list.

> **Note:** You can use the Advanced Filter feature to specify multiple filter options to narrow down search results.

7. In the **Snapshot ID/Name** column, click the ID of a snapshot to go to the Snapshot Details
page. The following table describes the details of the snapshot that is displayed on the Snapshot Details page.

| Section | Description |
|---|---|
| Basic Information | This section displays basic information about the snapshot, including the snapshot name, snapshot ID, snapshot status, snapshot creation progress, snapshot type, snapshot creation time, and Instance Access setting. |
| Disk Information | This section displays information about the disk from which the snapshot was created, including the disk name, disk ID, disk status, and disk type. |

| Relevant Information | Images created from snapshots This tab displays information about the custom images that are created from the snapshot, including the IDs, names, status, and sharing scopes of the custom images. You can click the ID of a custom image in the custom image list to go to the ECS Image > Custom Image tab and view the details of the custom image. For more information, see Find a custom image. Disks Created from Snapshots This tab displays information about the disks that are created from the snapshot, including the IDs, names, status, categories, types, and encryption settings of the disks. You can click the ID of a disk in the disk list to go to theD isk Details tab and view the details of the disk. For more information, see View disk details. |
|---|---|

#### 8.2.3 Roll back a disk by using a snapshot

If you have created a snapshot of a disk, you can use the snapshot to roll back the disk to the point in time when the snapshot was created. The disk rollback operation is irreversible. After the disk is rolled back, the data that was stored on the disk before the rollback operation is performed is lost and cannot be recovered. Exercise caution when you perform this operation.

**Prerequisites**

Before you roll back a disk by using a snapshot, make sure that the following requirements are met: Snapshots have been created for the disk, and no snapshots are currently being created for the disk. For more information, see Create snapshots. The disk is not released. The disk is attached to an instance that is in the **Stopped** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find a snapshot of the disk that you want to roll back and click **Roll Back Disk** in the
**Actions** column.

> **Note:** You can roll back only one disk on an instance at a time. Other disks that are attached to the instance are not affected. After the rollback operation is complete, the entire disk (not a partition or a directory) is restored to the state that the disk was in when the snapshot was created.

6. In the message that appears, click **Roll Back Disk**.
7. Starts an ECS instance.
For more information, see Start an instance.

**What to do next**

After the disk is rolled back, the hosts configuration file and the configurations such as the hostname, SSH key pair, passwords, network settings, operating system repository settings, and clock source are initialized. You must reconfigure the file and configurations If you have resized the disk after you created the snapshot for the disk, you must log on to the instance to resize the file systems on the disk again after the disk is rolled back. For more information, see Resize a disk.

#### 8.2.4 Create a custom image from a snapshot

**snapshot**

You can create a custom image from a snapshot that contains the operating system and data of an Elastic Compute Service (ECS) instance. Then, you can use the custom image to create multiple identical instances.

**Prerequisites**

A system disk snapshot is created. For more information about how to create a system disk snapshot, see Create snapshots.

**Precautions**

Before you create custom images from snapshots, take note of the following items: Both encrypted and unencrypted snapshots can be used to create custom images. Only system disk snapshots can be used to create custom images. Data disk snapshots cannot be used to create custom images. Custom images that are created from snapshots cannot be used across regions.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find a snapshot whose property is displayed as **System Disk** in the **Disk Type (All)**
column, and then click **Create Custom Image** in the **Actions** column.
6. Configure the parameters described in the following table to create a custom image.

| Parameter | Description |
|---|---|
| Sharing Scope | Select the scope in which you want to share the custom image. Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |

| Image Description | The description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
|---|---|

7. Click **OK**.

#### 8.2.5 Delete snapshots

You can delete a snapshot that is no longer needed. After the snapshot is deleted, it cannot be recovered.

**Precautions**

To delete snapshots that have been used to create custom images, you must first delete the custom images. For more information, see Delete a custom image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Use one of the following methods to delete snapshots:
To delete a single snapshot, find the snapshot and click **Delete** in the **Actions** column. To delete one or more snapshots at a time, select the snapshots and click **Delete** below the snapshot list.
6. In the message that appears, click **Delete**.

### 8.3 Use snapshot-consistent groups

**groups**

#### 8.3.1 Create a snapshot-consistent group

You can create a snapshot-consistent group to simultaneously take snapshots for disks on one or more Elastic Compute Service (ECS) instances. If a business system spans multiple disks, you can create a snapshot-consistent group to ensure a consistent write order and crash consistency of business system data.

**Prerequisites**

The instances for which you want to create a snapshot-consistent group are in the **Running** or **Stopped** state. The disks for which you want to create a snapshot-consistent group are in the **Running** state.

> **Important:** You can create snapshot-consistent groups only for standard performance disks and premium performance disks. If an instance has disks of other categories attached, you can select only standard performance disks and premium performance disks on the instance to create a snapshot-consistent group.

**Precautions**

Before you use the snapshot-consistent group feature, take note of the following items: When you create a snapshot-consistent group based on an instance, take note of the following items: To ensure that services are not affected, we recommend that you create the snapshotconsistent group during off-peak hours. A single snapshot-consistent group can contain snapshots of up to 16 disks including system disks and data disks and cannot exceed 32 TiB in size. Snapshots that you created are retained until they are deleted. We recommend that you delete unnecessary snapshots on a regular basis to prevent the snapshot size from exceeding the limit. For information about how to delete a snapshot, see Delete a snapshot. For the amount of time required to create a snapshot-consistent group, take note of the following items: The amount of time required to create a snapshot-consistent group depends on the sizes of the selected disks for which to create snapshots. The first snapshot of each disk is a full snapshot and takes longer to create than subsequent snapshots. Subsequent snapshots are incremental snapshots and do not take as long to be created as the first snapshot. The amount of time required varies based on the amount of data changed since the previous snapshot. If you want to use a snapshot while it is being created, you can enable the instant access feature.

**Scenarios**

Snapshot-consistent groups are applicable to cluster services. Example scenarios that snapshot-consistent groups support: A business system is deployed on multiple disks attached to an ECS instance, and point-intime consistency and crash consistency are required across databases or enterprise-level applications. For example, a MySQL cluster is built on ECS instances, a logical volume in Logical Volume Manager (LVM) spans multiple volumes, or Oracle or SAP HANA clusters are migrated to the cloud. Snapshots need to be created simultaneously for multiple nodes of a distributed application system, such as a large-scale website or a multi-application collaborative system. Disks on an ECS instance need to be backed up simultaneously with high point-in-time consistency.

**Method 1: Create a snapshot-consistent group based on a**

**single instance**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and choose **Disk and Image > Create Snapshot-consistent Group**.
5. In the **Create Snapshot-consistent Group** dialog box, configure the parameters that are
described in the following table.

| Parameter | Description |
|---|---|

| Disks | Select standard performance disks and premium performance disks for which you want to create a snapshot-consistent group. Up to 16 disks can be selected, including the system disk and data disks. The total size of the selected disks cannot exceed 32 TiB. |
|---|---|
| Group Name | Enter a name for the snapshot-consistent group to facilitate management. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, periods (.), underscores ( ), hyphens (-), and _ colons (:). |
| Description | Enter a description for the snapshot-consistent group to facilitate management. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Instant Access | The instance access feature can accelerate the process of snapshot creation. You can use the instant access feature to create snapshots within seconds. Enable Instant Access: You can select this check box to enable the instant access feature. By default, this check box is not selected. Duration of Instant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. Valid values: 1 to 65535. |

6. Click **OK**.
After the snapshot-consistent group is created, you can choose **Storage & Snapshots >**
**Snapshots** and click the **Snapshot-consistent Groups** tab to view the snapshot-
consistent group.

**Method 2: Create a snapshot-consistent group based on**

**multiple instances**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Snapshot-consistent Groups** tab. Then, click **Create Snapshot-consistent**
**Group**.
5. In the **Create Snapshot-consistent Group** dialog box, configure the parameters that are
described in the following table.

| Parameter | Description |
|---|---|
| Data Source | Select the instances based on which to create the snapshot-consistent group. |

| Disks | Select standard performance disks and premium performance disks for which you want to create a snapshot-consistent group. Up to 16 disks can be selected, including system disks and data disks. The total size of the selected disks cannot exceed 32 TiB. |
|---|---|
| Group Name | Enter a name for the snapshot-consistent group to facilitate management. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, periods (.), underscores ( ), hyphens (-), and _ colons (:). |
| Description | Enter a description for the snapshot-consistent group to facilitate management. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Instant Access | The instance access feature can accelerate the process of snapshot creation. You can use the instant access feature to create snapshots within seconds. Enable Instant Access: You can select this check box to enable the instant access feature. By default, this check box is not selected. Duration of Instant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. Valid values: 1 to 65535. |

6. Click **OK**.
After the snapshot-consistent group is created, you can choose **Storage & Snapshots >**
**Snapshots** and click the **Snapshot-consistent Groups** tab to view the snapshot-
consistent group.

**What to do next**

After a snapshot-consistent group is created, you can perform the following operations: Use the snapshot-consistent group to roll back disks. For more information, see Roll back disks by using a snapshot-consistent group. Access the snapshot-consistent group and create a custom image from a snapshot in the group. For more information, see Create a custom image from a snapshot.

#### 8.3.2 Roll back disks by using a snapshot-consistent group

**consistent group**

After a snapshot-consistent group is created, you can use it to roll back one or more disks in the event of system failures or data errors caused by accidental operations.

**Prerequisites**

Before you use a snapshot-consistent group to roll back disks on an Elastic Compute Service (ECS) instance, make sure that the following requirements are met: A snapshot-consistent group is created based on the disks. For more information, see Create a snapshot-consistent group.

> **Important:** The rollback operation cannot be reversed. If data changes were made to the disk from the time the snapshot-consistent group was created until the disk is rolled back, all these data changes are lost. To prevent data loss caused by accidental operations, we recommend that you create a snapshot-consistent group to back up disk data before you roll back disks.

The instance to which the disks to be rolled back are attached is in the **Stopped** state. For more information, see Stop an instance. The disks that correspond to the snapshots contained in the snapshot-consistent group have not been released or detached or do not have snapshots being created. The operating system of the instance has not been replaced since the snapshot-consistent group was created. The snapshots of the disks have not been deleted from the snapshot-consistent group. If the snapshot of a disk has been deleted from the snapshot-consistent group, the disk cannot be rolled back by using the snapshot-consistent group. The snapshot-consistent group can be used to roll back only other disks whose snapshots are contained in the group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Snapshot-consistent Groups** tab.
5. Find the snapshot-consistent group that you want to use and click **Roll Back** in the **Actions**
column.
6. In the **Roll Back** dialog box, perform the following operations:
i. Read the precautions about the rollback operation. Select **Start Instance Immediately**
**After Rollback** based on your business needs.
ii. In the **Disk Snapshots** section, select the snapshots of the disks that you want to roll back. iii. Click **Roll Back**. After the selected disks are rolled back, the Rolled back. message is displayed.

**Result**

After disks are rolled back, you can log on to their associated instances to check whether the disk data has been reverted to the state it was in when the snapshots were created.

#### 8.3.3 Delete a snapshot-consistent group

You can delete snapshot-consistent groups that are no longer needed.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Snapshot-consistent Groups** tab.
5. Find the snapshot-consistent group that you want to delete and click **Delete** in the **Actions**
column.
6. In the message that appears, click **Delete**.

### 8.4 Use automatic snapshots

#### 8.4.1 Create an automatic snapshot policy

Automatic snapshot policies can be applied to system disks and data disks to create snapshots for the disks on a periodic basis. You can use automatic snapshot policies to improve data security and tolerance against accidental operations.

**Background information**

Automatic snapshot policies can effectively eliminate the following risks associated with manual snapshots: When applications such as personal websites or databases deployed on an Elastic Compute Service (ECS) instance encounter attacks or system vulnerabilities, you may be unable to manually create snapshots. In this case, you can use the latest automatic snapshots to roll back the affected disks to restore your data and reduce loss. You can also specify an automatic snapshot policy to create snapshots before regular system maintenance tasks are performed. This eliminates the need to manually create snapshots and ensures that snapshots are always created before maintenance. You can retain up to 64 snapshots for each disk. If the maximum number of snapshots for a disk has been reached while a new snapshot is being created, the system deletes the oldest automatic snapshot.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Policy**.
5. In the **Create Policy** dialog box, configure the parameters described in the following table.

| Parameter or option | Required | Description |
|---|---|---|
| Organization | Yes | The organization in which to apply the automatic snapshot policy. |
| Resource Set | Yes | The resource set in which to apply the automatic snapshot policy. |
| Region | Yes | The ID of the region in which to apply the automatic snapshot policy. |
| Policy Name | Yes | The name of the automatic snapshot policy. The name must be 2 to 128 characters in length and cannot start with a digit or a special character. It can contain the following special characters: periods (.), underscores ( ), hyphens (-), and _ colons (:). |
| Sharing Scope | Yes | The scope in which the automatic snapshot policy can be shared. Valid values:Current Organization and Subordinate Organizations, Current Resource Set, and Current Organization. |

| Creation Time | Yes | The time of the day at which to create an automatic snapshot. Valid values: 00:00 to 23:00 (the start of each hour). You can select multiple values. Note The default time zone for the snapshot policy is UTC+8. You can change the time zone to suit your business requirements. If the time scheduled for creating an automatic snapshot is due while a previous automatic snapshot is being created, the new snapshot creation task is skipped. This may occur when a disk contains a large volume of data. For example, assume that an automatic snapshot policy is applied to a disk that contains a large volume of data, and the system creates snapshots at 00:00, 01:00, and 02:00 based on the policy. If the system starts to create a snapshot at 00:00 and takes 70 minutes to complete the snapshot creation task, the system skips the automatic snapshot task scheduled for 01:00 and creates the next automatic snapshot at 02:00. |
|---|---|---|
| Frequency | Yes | The day of the week when to create automatic snapshots. The valid values range from Monday to Sunday. You can select multiple values. |
| Retention Period | No | The retention period of the automatic snapshots. By default, automatic snapshot are retained for 30 days. Valid values: Custom Period: You can select this option and then specify the number of days during which to retain the automatic snapshots. Valid values: 1 to 65536. Permanently: You can select this option to retain the automatic snapshots until the maximum number of snapshots is reached. |

6. Click **OK**.

**What to do next**

After the automatic snapshot policy is created, you must apply it to a disk for snapshots to be automatically created. For more information, see Apply or cancel an automatic snapshot policy.

#### 8.4.2 View automatic snapshot policies

You can view created automatic snapshot policies.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. View created automatic snapshot policies.

#### 8.4.3 Modify an automatic snapshot policy

After an automatic snapshot policy is created, you can modify properties of the policy based on your business requirements, such as the policy name, creation time, execution frequency, and retention period.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to modify and click **Modify Policy** in the
**Actions** column.
5. In the **Modify Policy** dialog box, modify the original parameter settings of the policy.
For more information about the parameters that you can configure for a policy, see Create an automatic snapshot policy.

> **Note:** Changes made to the retention period do not affect the existing snapshots and take effect only on subsequent snapshots.

6. Click **OK**.

#### 8.4.4 Apply or cancel an automatic snapshot policy

**policy**

You can apply automatic snapshot policies to disks. After an automatic snapshot policy is applied to a disk, snapshots are automatically created for the disk based on the policy.

**Background information**

We recommend that you apply automatic snapshot policies to create automatic snapshots during off-peak hours. You can manually create snapshots for disks to which automatic snapshot policies are applied. When an automatic snapshot is being created for a disk, you must wait for the creation task to be completed before you can manually create a snapshot for the disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to apply or cancel and click **Apply or**
**Cancel Policy** in the **Actions** column.
5. In the **Apply or Cancel Policy** dialog box, perform the following operations based on your
business requirements: If you want to apply the automatic snapshot policy, click the **Disks Without Policy**
**Applied** tab, select the disks to which you want to apply the policy, and then click **Apply**
**Policy** below the disk list.
If you want to disable the automatic snapshot policy, click the **Disks with Policy**
**Applied** tab, select the disks for which you want to disable the policy, and then click
**Cancel Policy** below the disk list.

#### 8.4.5 Delete an automatic snapshot policy

You can delete automatic snapshot policies that you no longer need. After you delete an automatic snapshot policy, the policy is automatically canceled for the disks to which the policy is applied.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to delete and click **Delete Policy** in the
**Actions** column.
5. In the message that appears, click **Delete**.

## 9 Security groups

### 9.1 Overview

A security group acts as a virtual firewall to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances to improve security. Security groups provide Stateful Packet Inspection (SPI) and packet filtering capabilities. You can use security groups and security group rules to define security domains in the cloud.

**Security groups and security group rules**

A security group acts as a virtual firewall that is used to control access to and from one or more ECS instances. Each instance must belong to at least one security group. The following rules apply when you add instances to security groups: Each instance must belong to one or more security groups. The secondary ENIs that are bound to an instance can be assigned to security groups different from those of the instance. The rules of a security group control the inbound or outbound traffic to or from the instances in the security group. You can add or modify security group rules based on your business needs to implement fine-grained access control. New and modified rules are automatically applied to all instances within the security group. Security group rules can be used to control access to or from specific IP addresses, CIDR blocks, security groups, or prefix lists. If an instance belongs to multiple security groups, the rules of all the security groups are applied to the instance. When an access request destined for the instance is detected, the request is matched against applied security group rules one by one based on the rule attributes such as protocol, port range, and priority. No sessions are established until an Allow rule matches the request.

**Work with security groups**

You can perform the following operations to use security groups to control traffic for instances:
1. Create security groups.
2. Add rules to the security groups.
3. Add instances to the security groups.
4. Manage existing security groups and security group rules based on your needs.

**Operations in the ECS console**

The following table describes the operations that you can perform in the ECS console to manage security groups.

| Operation | Description | References |
|---|---|---|
| Create a security group | You can create a security group. | Create a security group |
| Add a security group rule | After you create a security group, you can add or modify security group rules to control inbound or outbound network access. | Add a security group rule |
| Add an ECS instance to a security group | You can add an instance to a security group to control network access in a centralized manner. | Add ECS instances to a security group |

| Manage security groups | You can query, modify, and delete security groups as well as remove instances from security groups. | View security groups Modify a security group Remove instances from a security group Delete a security group |
|---|---|---|
| Manage security group rules | You can modify, clone, export, import, and delete security group rules. | Modify security group rules Clone a security group rule Export security group rules Import security group rules Delete a security group rule |

### 9.2 Create a security group

Security groups are an important means to implement network security isolation. They control network traffic to or from one or more Elastic Compute Service (ECS) instances.

**Background information**

Security groups determine whether instances in the same VPC, region, and account can communicate with each other. By default, if the instances belong to the same security group, they can communicate with each other over the internal network. If the instances belong to different security groups, you can allow mutual access between the security groups to allow the instances to communicate with each other over the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Security Group**.
5. Configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization | Yes | Select an organization in which to create the security group. Make sure that the security group and the VPC belong to the same organization. |
|   | Resource Set | Yes | Select a resource set in which to create the security group. Make sure that the security group and the VPC belong to the same resource set. |
| Document Versio | n: 20240529 22 |   |   |

|   | Region | Yes | Select a region in which to create the security group. Make sure that the security group and VPC reside within the same region. |
|---|---|---|---|
|   | Zone | Yes | Select a zone in which to create the security group. |
| Basic Configuration s | Sharing Scope | Yes | Select the scope for which to share the security group. Valid values: Current Resource Set, Current Organization and Subordinate Organizations, and Current Organization. |
|   | VPC | Yes | Select an existing VPC or click Create VPC to create a VPC. After you create a VPC, you can go back to the Create Security Group page and click the icon to view the most recent list of VPCs. For information about the parameters that are used to create a VPC, see the Create a VPC topic in VPC User Guide. |
|   | Security group name | Yes | Enter a name for the security group. The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, underscores ( ), hyphens (-), and colons (:). It _ cannot start with http:// or https:// . |
|   | Description | No | Enter a description for the security group for easy management. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ periods (.), commas (,), and colons (:). It must start with a letter and cannot start with http:// or https:// . |

6. Click **Submit**.
After the security group is created, it is displayed on the Security Groups page.

**What to do next**

After the security group is created, it contains no security group rules. You can add security group rules to allow or deny access to or from the Internet or internal network for ECS instances within the security group. For more information, see Add a security group rule. Each ECS instance must belong to at least one security group. You can add an instance to one or more security groups. For more information, see Add ECS instances to a security group.

### 9.3 Add a security group rule

You can use security group rules to manage access to and from the Elastic Compute Service (ECS) instances in a security group over the Internet and the internal network.

**Prerequisites**

The public or internal IP addresses from which you want to manage access to your instances are obtained.

**Background information**

Security groups are used to manage access requests that are sent over the Internet or internal network. This topic is provided for the following scenarios: If an application deployed on your instance initiates a request to connect to a network that is not managed by the security groups to which the instance belongs but the request remains in the waiting state, you must add a security group rule to allow this request. When attacks from some of the request sources are detected on running applications, you can add security group rules to block the malicious requests. Before you add security group rules, take note of the following items:

> **Note:** For security purposes, most security groups use Deny rules for inbound traffic. You can add security group rules based on your business requirements.

Both IPv4 and IPv6 addresses can be used as the authorization objects of security group rules. The total number of inbound and outbound rules within each security group cannot exceed 200. For more information, see Overview.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, find the security group for which you want to configure rules
and click **Manage Rules** in the **Actions** column.
5. Click **Create Rule**.
6. In the **Create Rule** dialog box, configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| NIC Type | Yes | Valid value: Internal NIC. No public NICs are available for ECS instances that are deployed in virtual private clouds (VPCs). You can only add internal security group rules. However, the added security group rules apply to both the Internet and the internal network. |
| Rule Direction | Yes | Outbound: access from the ECS instances in the current security group to other ECS instances on the internal network or to resources on the Internet. Inbound: access from other ECS instances on the internal network or from resources on the Internet to the ECS instances in the current security group. |
| Action | Yes | Allow: allows access requests that are sent to specified ports. Deny: denies access requests and drops data packets without returning a response. If two security group rules use the same settings except for the action, the Deny action takes precedence over the Allow action. |

| Protocol Type | Yes | The protocol type of the security group rule. Valid values: All: This value can be used in scenarios in which requests are sent from trusted sources. TCP: This value can be used to allow or deny traffic on one or more consecutive ports. UDP: This value can be used to allow or deny traffic on one or more consecutive ports. ICMP: This value can be used when the ping command is used to test the status of network connection between instances. ICMPv6: This value can be used when the ping6 command is used to test the status of network connection between instances. GRE: This value can be used for VPN. |
|---|---|---|
| Port Range | Yes | The port range varies based on the protocol type. If you set Protocol Type to All, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set Protocol Type to TCP, you can specify a port range in the <start port>/<end port> format. Valid values: 1 to 65535. For example, 80/80 indicates port 80, and 1/22 indicates ports 1 to 22. If you set Protocol Type to UDP, you can specify a port range in the <start port>/<end port> format. Valid values: 1 to 65535. For example, 80/80 indicates port 80, and 1/22 indicates ports 1 to 22. If you set Protocol Type to ICMP, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set Protocol Type to ICMPv6, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set Protocol Type to GRE, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. |
| Priority | Yes | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Authorization Type | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. Security Group: security groups. This authorization type takes effect only on the internal network. You can select another security group in the current account as the authorization object for the instances in the current security group. This way, you can manage access to or from the ECS instances in that security group over the internal network. |

| Authorization Object | Yes | Authorization objects vary based on the authorization type. If you set Authorization Type to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate multiple objects with commas (,). If you enter 0.0.0.0/0 , all IPv4 addresses are allowed or denied based on the value of the Action parameter. Proceed with caution. If you set Authorization Type to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter up to 10 authorization objects. Separate multiple objects with commas (,). If you enter ::/0 , all IPv6 addresses are allowed or denied based on the value of the Action parameter. Proceed with caution. If you set Authorization Type to Security Group, select a security group ID. The specified security group must be within the same VPC as the current security group. |
|---|---|---|
| Description | No | The description of the security group rule. To simplify future management operations, we recommend that you provide a specific description. The description must be 1 to 512 characters in length and cannot start with http:// or https://. |

7. Click **OK**.

### 9.4 Add ECS instances to a security group

**security group**

You can add existing Elastic Compute Service (ECS) instances to a security group in the same region. After the instances are added to the security group, the rules of the security group automatically apply to the instances.

**Background information**

Security groups are an important means for security isolation. A security group can control access to or from one or more ECS instances in the security group. Each ECS instance must be added to at least one security group and can be added to up to five security groups. For information about how to add an ECS instance to multiple security groups, see Add an instance to a security group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group to which you want to add ECS instances. In the **Actions** column,
choose
**> Manage Instances**.
The **Instances** tab is displayed. On the Instance tab, you can view the information of the ECS instances in the security group. The ECS instance information includes **Instance**
**ID/Name**, **Region**, **IP Address**, and **Network Type**.

> **Note:** Select a filter option from the drop-down list and enter relevant information to search for ECS instances. You can search for ECS instances by using the **Instance ID** or **Instance Name** filter option.

5. Click **Add Instance**.
6. In the Add Instance dialog box, select the ECS instances that you want to add to the
security group from the instance list and click **OK**.

> **Important:** After the ECS instances is added to the security group, the rules of the security group automatically apply to the instances.

Select a filter option from the drop-down list and enter relevant information to search for ECS instances. The ECS instances that match the specified filter conditions are displayed.

> **Note:** You can search for ECS instances by using the **Instance Name**, **Instance ID**, **IP** **Address**, or **Tag** filter option.

### 9.5 Manage security groups

#### 9.5.1 View security groups

This topic describes how to search for security groups within a region by using different methods and view the details of the security groups.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to search for security groups:
Select a filter option such as **Security Group ID** from the drop-down list and enter relevant information in the search box. Then, the system searches for security groups based on your specified filter condition.

> **Note:** Fuzzy search is supported only when you select **Security Group ID** or **Security Group Name** as the filter option.

Click **Advanced Filter**, specify multiple filter options, and then click **Search**. Eligible security groups are displayed in the security group list.

> **Note:** You can use the Advance Filter feature and specify multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Security Group ID | Enter the ID of a security group. |
| Security Group Name | Enter the name of a security group. |
| VPC ID | Enter the ID of a virtual private cloud (VPC) to search for security groups that belong to the VPC. |
| Tag | Enter a tag key or a tag value to search for security groups to which the tag key or value is added. |

#### 9.5.2 Modify a security group

You can modify the names and descriptions of created security groups.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group that you want to modify and click **Modify** in the **Actions** column.
5. In the **Modify Security Group** dialog box, modify the name and description of the security
group. The new name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, underscores (_), hyphens (-), and colons (:). It cannot start with http:// or https://. The new description must be 2 to 256 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores (_), hyphens (-), colons (:), and commas (,). It cannot start with http:// or https://.
6. Click **OK**.

#### 9.5.3 Remove instances from a security group

**group**

You can remove Elastic Compute Service (ECS) instances from a security group based on your business requirements. Before you perform this operation, make sure that the instances belong to at least one security group.

**Prerequisites**

The instances that you want to remove belong to two or more security groups.

**Background information**

After an instance is removed from a security group, the instance is isolated from the other instances in the security group. We recommend that you perform all tests in advance to ensure that services can continue to run as expected after you remove the instance from the security group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group from which you want to remove instances, click the
icon in the
**Actions** column, and then select **Manage Instances**.
5. On the Instances page, select one or more instances that you want to remove and click
**Remove from Security Group** in the lower-left corner.
6. In the message that appears, click **Remove from Security Group**.

#### 9.5.4 Delete a security group

You can delete security groups that are no longer needed. When a security group is deleted, its rules are also deleted.

**Prerequisites**

The security group that you want to delete does not contain Elastic Compute Service (ECS) instances. If the security group contains ECS instances, you must remove the instances from the security group. For more information, see Remove instances from a security group. The security group is not referenced by rules of other security groups. If the security group is referenced by rules of other security groups, you must delete those rules as prompted. For more information, see Delete a security group rule.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete a security group:
To delete a single security group, find the security group and click **Delete** in the **Actions** column. To delete one or more security groups at a time, select the security groups and click
**Delete** in the lower-left corner of the Security Groups page.
5. In the message that appears, click **Delete**.

### 9.6 Manage security group rules

#### 9.6.1 Modify security group rules

This topic describes how to modify security group rules. Improper configurations of security group rules can result in serious security risks. You can modify improper rules in a security group to ensure the network security of Elastic Compute Service (ECS) instances within the security group.

**Prerequisites**

A security group is created and security group rules are added. For more information, see the Create a security group and Add a security group rule.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, find the security group for which you want to modify security
group rules and click **Manage Rules** in the **Actions** column.
5. On the Rules page, click the **Inbound** or **Outbound** tab.
6. Find the security group rule that you want to modify and click **Modify Properties** in the
**Actions** column.
7. In the **Modify Properties** dialog box, modify the rule.
For more information about the properties of security group rules, see Add a security group rule.
8. Click **OK**.

#### 9.6.2 Clone a security group rule

You can clone a security group rule to quickly create a similar rule.

**Background information**

You may need to clone a security group rule in the following scenarios: Assume that you have created Security Group Rule A to control TCP access and that you want to create Security Group Rule B to control UDP access. You can create Rule B by cloning Rule A and changing the protocol type to UDP. Assume that you have created Security Group Rule C to control TCP access over port 22 and that you want to create Security Group Rule D to control TCP access over port 3389. You can create Rule D by cloning Rule C and changing the port range to 3389/3389.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, find the security group in which you want to clone a rule and
click **Manage Rules** in the **Actions** column.
5. On the Rules tab, click the **Inbound** or **Outbound** tab.
6. Find the rule that you want to clone and click **Clone** in the **Actions** column.
7. In the **Clone Rule** dialog box, modify the attributes of the rule.
For more information, see Add a security group rule.
8. Click **OK**.
After the rule is cloned, a new rule is displayed in the rule list.

#### 9.6.3 Export security group rules

You can export security group rules into Excel files to your computer for on-premises backup.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group from which you want to export rules. Click **Manage Rules** in the
**Actions** column.
5. On the Rules tab, click the **Inbound** or **Outbound** tab.
6. Click **Export**.
An Excel file that contains the **inbound** rules or **outbound** rules of the security group are automatically downloaded to your on-premises computer.

#### 9.6.4 Import security group rules

Security group rules can be imported to security groups. You can import a backup file of security group rules from your computer to a security group to create or restore security group rules.

**Background information**

You can download a template file (XLS file), configure security group rules in the file based on the template requirements, and then import the file.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group to which you want to import rules. Click **Manage Rules** in the
**Actions** column.
5. On the **Rules** tab, click **Import**.
6. In the **Import Security Group Rule** dialog box, click **Upload File**.
7. Select a backup file of security group rules from your computer and click **Open** to upload
the file.

#### 9.6.5 Delete a security group rule

If you do not need a security group rule that controls access to Elastic Compute Service (ECS) instances or from ECS instances, you can delete the rule.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group from which you want to delete a rule. Click **Manage Rules** in the
**Actions** column.
5. On the Rules tab, click the **Inbound** or **Outbound** tab.
6. Use one of the following methods to delete a security group rule:
To delete a single rule, find the rule and click **Delete** in the **Actions** column. To delete one or more rules at a time, select the rules and click **Delete** in the lower-left corner of the tab.
7. In the message that appears, click **Delete**.
nt

## 10 RAM role management

### 10.1 Attach an instance RAM role to an ECS instance

**to an ECS instance**

This topic describes how to attach an instance Resource Access Management (RAM) role to an Elastic Compute Service (ECS) instance.

**Prerequisites**

An instance RAM role is created. For more information, see **Create a custom role** in the
**Apsara Uni-manager User Guide**.
The ECS instance to which you want to attach an instance RAM role is located in a virtual private cloud (VPC). The current user role has the permissions to **authorize access to cloud services** and
**attach RAM roles to ECS instances** . For more information, see **View the details of a**
**role** in the **Apsara Uni-manager User Guide**.

**Usage notes**

Before you attach an instance RAM role to an ECS instance, take note of the following items: After a RAM role is attached to an instance, the permissions that the RAM role has are granted to the instance. Proceed with caution. An instance RAM role can be attached to a single instance at a time.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage and choose
> **Instance Settings >**

**Attach/Detach RAM Role** in the **Actions** column.
5. In the dialog box that appears, select an existing RAM role and click **OK** to attach the role
to the instance.

### 10.2 Replace the instance RAM role of an ECS instance

**role of an ECS instance**

After you attach an instance Resource Access Management (RAM) role to an Elastic Compute Service (ECS) instance, you can replace the role at anytime.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
nt
4. Select an instance to which a RAM role is attached and choose
> **Instance Settings >**

**Attach/Detach RAM Role** in the **Actions** column.
5. Set **Operation Type** to **Attach**, select a different instance RAM role from the **RAM Role**
drop-down list, and then click **OK** to replace the RAM role.

### 10.3 Detach an instance RAM role from an ECS instance

**from an ECS instance**

After you attach an instance Resource Access Management (RAM) role to an Elastic Compute Service (ECS) instance, you can detach the role from the instance at anytime.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find an instance to which an instance RAM role is attached and choose
> **Instance**

**Settings > Attach/Detach RAM Role** in the **Actions** column.
5. Set **Operation Type** to **Detach** and click **OK** to detach the role.
aces

## 11 Elastic Network Interfaces

### 11.1 Overview

An elastic network interface (ENI) is a virtual network interface controller (NIC) that can be bound to an Elastic Compute Service (ECS) instance of the Virtual Private Cloud (VPC) type. You can use ENIs to deploy high-availability clusters and perform low-cost failover and finegrained network management.

**Attributes**

An ENI is a virtual network interface that must be bound to an instance of the VPC type before the ENI can be used. The following table describes the attributes of an ENI.

| Attribute | Description |
|---|---|
| ENI type | ENIs are classified into primary and secondary ENIs. Primary ENIs: created together with instances. The lifecycle of a primary ENI is the same as the instance to which the primary ENI is bound. You cannot unbind a primary ENI from the instance to which the primary ENI is bound. Secondary ENIs: can be separately created. You can bind or unbind a secondary ENI to or from an instance. |
| VPC | Only instances of the VPC type support ENIs. An ENI must reside within the same VPC as the instance to which the ENI is bound. |
| Organization | An ENI must belong to the same organization as the instance to which the ENI is bound. |
| Resource set | An ENI must belong to the same resource set as the instance to which the ENI is bound. |
| Region | An ENI must reside within the same region as the instance to which the ENI is bound. |
| Zone | The vSwitch to which the ENI belongs must reside within the same zone as the instance to which the ENI is bound. |
| Security group | An ENI must be added to at least one security group. The security group controls the inbound and outbound traffic of the ENI. |
| EIP | An ENI can be associated with one or more elastic IP addresses (EIPs). |
| Primary private IP address | The primary private IP address is an IP address specified by the user or assigned by the system during ENI creation. The primary private IP address must be an idle IP address within the CIDR block of the vSwitch to which the ENI is connected. |
| Secondary private IPv4 address | A secondary private IPv4 address must be an idle IPv4 address within the CIDR block of the associated vSwitch. You can assign or unassign secondary private IPv4 addresses for an ENI. |
| Secondary private IPv6 address | A secondary private IPv6 address must be an idle IPv6 address within the CIDR block of the associated vSwitch. You can assign or unassign the secondary private IPv6 addresses for an ENI. |
| Media access control (MAC) address | A MAC address is the globally unique identifier of an ENI. |

aces

**Features**

An ENI is an independent virtual NIC that can be migrated between multiple instances to support the flexible scaling and migration of services. When you create an ENI together with an instance, the ENI is automatically bound to the instance. You can also separately create a secondary ENI and bind it to an instance. ENIs have the following features: In addition to the primary ENI that is created together with an instance, you can also bind multiple secondary ENIs to the instance. The ECS instance and the secondary ENIs that you want to bind to the instance must reside within the same zone and VPC, but can be connected to different vSwitches and belong to different security groups. Each ENI can be assigned multiple secondary private IP addresses based on the instance type of the instance to which the ENI is bound. When you unbind a secondary ENI from an instance and bind the ENI to another instance, the attributes of the ENI remain unchanged and the network traffic is redirected to the new instance. ENIs support hot-plug and can be migrated among instances. When you unbind an ENI from an instance and bind the ENI to another instance, services on the instances are not affected, and you do not need to restart the instances.

**Limits**

The following limits apply to ENIs: Each ENI can be assigned only a single primary private IP address. Each ENI can be assigned one or more secondary private IP addresses. The number of secondary private IP addresses is determined based on the instance type of the instance to which the ENI is bound. Each ENI can be assigned one or more EIPs. The number of EIPs is determined based on how the EIPs are associated with the ENI. For more information, see the "Create a VPC" and "Create a vSwitch" topics in **Apsara Stack VPC User Guide**. Each ENI must be added to at least one security group and can be added to up to five security groups. ENIs that can be created per region in an account is limited. The ENI quota is displayed on the **Quota overview** page of the Apsara Uni-manager Management Console. The ENI and the instance to which the ENI is bound must reside within the same zone and VPC, but can belong to different vSwitches and security groups. The number of secondary ENIs that can be bound to an ECS instance is determined based on the instance type. The instance bandwidth is determined based on the instance type. You cannot increase the bandwidth of an ECS instance by binding multiple secondary ENIs to the instance.

**Use scenarios**

ENIs are suitable for the following scenarios: Deployment of high-availability clusters To implement a high-availability architecture, you can bind multiple ENIs to a single ECS instance. Low-cost failover You can unbind an ENI from a failed ECS instance and bind it to another normal instance to redirect traffic destined for the failed instance to the normal instance and immediately recover services. Fine-grained network management aces You can configure multiple ENIs for an instance. For example, you can use some ENIs for internal management and other ENIs for Internet business access to isolate management data from business data. You can also configure specific security group rules for each ENI based on the source IP addresses, protocols, and ports to achieve access control. Configuration of multiple private IP addresses for a single instance You can assign multiple secondary private IP addresses to an ENI. If multiple applications are managed on your instance, you can assign an independent IP address for each application to improve the utilization of your instance. Configuration of multiple public IP addresses for a single instance Only a single public IP address can be assigned to an ECS instance that has no ENIs bound. To assign multiple public IP addresses to an instance, you can associate EIPs with one or more ENIs of the instance. In NAT mode, each private IP address of an ENI can have EIPs associated.

### 11.2 Create an ENI

You can bind elastic network interfaces (ENIs) to instances to create high-availability clusters and implement fine-grained network management. You can also unbind an ENI from an instance and then bind the ENI to another instance to perform low-cost failover.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For more information, see the
**Create a VPC** and **Create a vSwitch** topics in **Apsara Stack VPC User Guide**.
A security group is available in the VPC. If no security group is available in the VPC, create a security group. For more information, see Create a security group.

**Background information**

You can use one of the following methods to create an ENI. This topic describes how to separately create an ENI. Create an ENI when you create an instance. A primary ENI is created by default when an instance is created in a VPC. The lifecycle of the primary ENI is the same as that of the instance and the primary ENI cannot be unbound from the instance. Separately create an ENI. ENIs created separately are secondary ENIs. You can bind secondary ENIs to or unbind them from instances.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create ENI**.
5. Configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Organization | Yes | The organization in which to create the ENI. |
| 1 |   |   |   |

| stic Compute Servic | User Guide·Elastic Network Inter e ace |   |   |
|---|---|---|---|
| Area |   |   |   |
|   | Resource Set | Yes | The resource set in which to create the ENI. |
|   | Region | Yes | The region in which to create the ENI. |
|   | Zone | Yes | The zone in which to create the ENI. |
| Basic Configurations | VPC | Yes | The VPC in which to create the ENI. The secondary ENI can be bound only to an instance in the same VPC. Select the VPC in which the instance resides. Note After an ENI is created, its VPC cannot be changed. |
|   | VSwitch | Yes | The vSwitch to which the ENI is connected. The secondary ENI can be bound to only an instance that is in the same zone as the VPC. Select a vSwitch that is in the same zone as the instance. The instance and the ENI can connect to different vSwitches. Note After an ENI is created, its vSwitch cannot be changed. |
|   | Security Group | Yes | The security group in which to create the ENI within the specified VPC. The rules of the security group automatically apply to the ENI. |
|   | ENI Name | Yes | The name of the ENI. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and hyphens (-). _ |
|   | Description | No | The description of the ENI. We recommend that you provide enough information to facilitate easy management. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . The description can contain letters, digits, colons (:), periods (.), commas (,), underscores ( ), and hyphens (-) _ |

|   | http:// |
|---|---|
| https:// |   |

|   | http:// |
|---|---|
| https:// |   |

aces

|   | Primary Private IP Address | No | The primary private IPv4 address of the ENI. The IPv4 address must be within the CIDR block of the specified vSwitch. If you do not specify a primary private IP address, the system automatically assigns a private IPv4 address to the ENI. |
|---|---|---|---|
|   | Auxiliary private network IPv4 | No | The secondary private IPv4 addresses of the ENI. Valid values: No distribution for the time being: No secondary private IPv4 addresses are assigned to the ENI. Automatic allocation: Enter an integer in the range of 1 to 9 as the number of secondary private IPv4 addresses that you want to assign to the ENI. The system automatically assigns the specified number of idle IPv4 addresses from within the CIDR block of the selected vSwitch to the ENI. Specify address: Manually assign secondary private IPv4 addresses to the ENI. You can specify up to 9 secondary private IPv4 addresses. |
|   | Auxiliary private network IPv6 | No | The secondary private IPv6 addresses of the ENI. Valid values: No distribution for the time being: No secondary private IPv6 addresses are assigned to the ENI. Automatic allocation: Enter an integer in the range of 1 to 10 as the number of secondary private IPv6 addresses that you want to assign to the ENI. The system automatically assigns the corresponding number of idle IPv6 addresses in the vSwitch to the ENI. Specify address: Manually assign secondary private IPv6 addresses to the ENI. You can specify up to 10 secondary private IPv6 addresses. Note To assign IPv6 addresses to the ENI, you must select a vSwitch that supports IPv6 addresses. |

6. Click **Submit**.

**Result**

If the ENI is created, **Available** is displayed in the Status column in the ENI list.

**What to do next**

After you create an ENI separately, you can bind it to an instance. For more information, see Bind a secondary ENI to an instance. aces

### 11.3 Bind a secondary ENI to an instance

**instance**

You can bind a secondary elastic network interface (ENI) to an instance. After the ENI is bound, the traffic on the ENI is directed to the instance.

**Prerequisites**

The secondary ENI that you want to bind is in the **Available** state. The instance to which you want to bind the secondary ENI is in the **Running** or **Stopped** state. The instance and the secondary ENI belong to the same virtual private cloud (VPC). The vSwitch with which the secondary ENI is associated is located within the same zone as the vSwitch to which the instance is connected. An ENI can be bound only to an instance within the same zone. The vSwitches of the ENI and of the instance can be different but must be located within the same zone.

**Background information**

The following limits apply when you bind an ENI to an instance: Only secondary ENIs can be manually bound. Primary ENIs share the same lifecycle as instances and cannot be manually bound. An ENI can be bound only to a single instance at the same time. Each instance can have one or more bound ENIs. The maximum number of ENIs that can be bound to an instance is determined based on the instance type.

**Bind an ENI to an existing instance on the instance details**

**page**

To bind multiple secondary ENIs to an instance, you can go to the details page of the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Instances page, find the instance to which you want to bind a secondary ENI and
click the instance ID.
5. Click the **ENIs** tab.
6. Click **Bind ENI**.
7. In the Bind ENI dialog box, select an ENI from the **ENI** drop-down list.
8. Click **OK**.

**Bind an ENI to an existing instance on the ENI page**

To bind secondary ENIs to multiple instances, you can go to the ENI page.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI that you want to bind and click **Bind to Instance** in the **Actions**
column.
5. In the **Bind to Instance** dialog box, select an instance and click **OK**.
aces If the ENI is bound to the instance, **Bound** is displayed in the **Status** column corresponding to the ENI.

### 11.4 Configure a secondary ENI

After secondary elastic network interfaces (ENIs) are bound to Elastic Compute Service (ECS) instances, some images used by these instances may not recognize the IP addresses of these ENIs or configure routes for the ENIs. If this occurs, the secondary ENIs cannot be used on the instances. This topic describes how to configure secondary ENIs from within instances to have their IP addresses recognizable and how to configure routes for the secondary ENIs.

**Prerequisites**

A secondary ENI is bound to an ECS instance. For information about how to bind a secondary ENI to an ECS instance, see Bind a secondary ENI to an instance. You are connected to the ECS instance. For information about how to connect to an ECS instance, see Overview.

**Background information**

If automatic configuration tools are pre-installed on the images that are used by instances, secondary ENIs that are bound to the instances can be automatically configured by the tools. You can use these secondary ENIs without the need to manually configure them. Skip the topic if your instance uses an image of one of the following versions: Alibaba Cloud Linux 3.2104 64-bit CentOS 8.0 64-bit, CentOS 8.1 64-bit, and CentOS 8.2 64-bit CentOS 7.3 64-bit, CentOS 7.4 64-bit, and CentOS 7.5 64-bit CentOS 6.8 64-bit and CentOS 6.9 64-bit Debian 10.5 64-bit and Debian 10.6 64-bit Windows Server 2008 R2 and later
1. Check whether the IP addresses of a secondary ENI bound to an instance are recognized.
For more information, see Check whether the IP addresses of ENIs are recognized. If yes, skip the following steps. If not, proceed with the following steps to configure the secondary ENI.
2. Obtain the information of the secondary ENI.
When you configure a secondary ENI, you may need to specify its information, such as the primary private IP address and media access control (MAC) address. Obtain the information required for subsequent configurations. For more information, see Obtain the information of an ENI. In the examples provided in this topic, the sample values listed in the following table are used. In actual scenarios, replace them with the attribute values of your secondary ENI.

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| MAC address | 00:16:3e:0f:**:** |
| Primary private IP address | 192.168.**.*2 |
| Subnet mask | 255.255.255.0 |

aces

| Gateway address | 192.168.**.253 |
|---|---|

3. Configure the secondary ENI to have its IP address recognized.
The operations required to configure secondary ENIs vary based on the operating systems of the instances to which the secondary ENIs are bound.

| Operating system | References |
|---|---|
| Alibaba Cloud Linux 2 (Instances that run this operating system use the network-scripts network service) CentOS | Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service |
| Alibaba Cloud Linux 2 (Instances that run this operating system use the systemd-networkd network service) | Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2 operating system and uses the systemd-networkd network service |
| Ubuntu Debian | Configure a secondary ENI for an instance that runs a Ubuntu or Debian operating system |
| SUSE openSUSE | Configure a secondary ENI for an instance that runs a SUSE or openSUSE operating system |

4. Check whether routes are configured for the secondary ENI.
You can run the `route -n` command to check route information. If no routes are configured for the secondary ENI or if the existing routes do not meet your requirements, manually configure routes for the secondary ENI. The following sections provide examples on how to configure routes for a secondary ENI that is bound to an instance that runs one of the following operating systems: Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system Configure routes for a secondary ENI of an instance that runs a CentOS 8 operating system

**Check whether the IP addresses of ENIs are recognized**

Run the following command to check whether the IP addresses of ENIs are recognized:

```
ip address show
```

Sample command outputs: The following command output shows that the IP address of the eth0 primary ENI is recognized but the IP address of the eth1 secondary ENI is not recognized. You can perform operations described in this topic to configure the secondary ENI. aces The following command output shows that the IP addresses of both the eth0 primary ENI and the eth1 secondary ENI are recognized. You do not need to configure the secondary ENI.

> **Note:** In the preceding command outputs, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI.

**Obtain the information of an ENI**

You can obtain the information of an ENI from instance metadata, by using the ECS console, or by calling an API operation. Obtain the information of an ENI from instance metadata. Obtain the MAC addresses of the ENIs that are bound to an instance.

```bash
curl http://100.100.100.200/latest/meta-data/network/interfaces/macs/
```

> **Note:** The MAC addresses of ENIs are required to obtain their primary private IP addresses, subnet masks, and gateway addresses.

Obtain the primary private IP address of the specified ENI.

```bash
curl http://100.100.100.200/latest/metadata/network/interfaces/macs/00:16:3e:19:**:**/primary-ip-address
```

Obtain the subnet mask of the specified ENI.

```bash
curl http://100.100.100.200/latest/metadata/network/interfaces/macs/00:16:3e:19:**:**/netmask
```

Obtain the gateway address of the specified ENI.

```bash
curl http://100.100.100.200/latest/metadata/network/interfaces/macs/00:16:3e:19:**:**/gateway
```

aces The following figure shows sample command outputs. In the command outputs, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI.

> **Note:** After you run the `ip address show` command, you can determine which is the primary ENI and which is the secondary ENI based on the order in which the MAC addresses are displayed in the command output.

Obtain the information of an ENI by using the ECS console. i. Log on to the ECS console. ii. In the left-side navigation pane, choose **Network & Security > ENIs**. iii. On the **ENI** page, find the ENI whose information you want to query and view its primary private IP address and MAC address in the Private IP Address and ENI Type/MAC Address columns. The following figure shows an example of the ENI page in the ECS console. Obtain the information of an ENI by using an Alibaba Cloud SDK to call the DescribeNetworkInterfaces operation.

```
aliyun ecs DescribeNetworkInterfaces \ --output cols=MacAddress,PrivateIpAddress rows=NetworkInterfaceSets.NetworkInterfaceSet[] \ --RegionId 'cn-qingdao-****-d01' \ --InstanceId 'i-bp1a5gj0bzhwz7q****'
```

The following figure shows the sample response. In the response, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI.

> **Note:** After you run the `ip address show` command, you can determine which is the primary ENI and which is the secondary ENI based on the order in which the MAC addresses are displayed in the command output.

aces

**Configure a secondary ENI for an instance that runs an Alibaba**

**Cloud Linux 2, CentOS 6, or CentOS 7 operating system and**

**uses the network-scripts network service**

If your instance runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service, you can use the multi-nic-util tool to have the ENIs of the instance automatically configured or you can manually configure the ENIs by modifying their configuration files. Use the multi-nic-util tool to have a secondary ENI automatically configured.

> **Note:** If you want to use the multi-nic-util tool to have secondary ENIs automatically configured for CentOS instances, note that the multi-nic-util tool is supported only on some versions of CentOS images. If your instance uses a CentOS 6 image, make sure that the image version is CentOS 6.8 or later. If your instance uses a CentOS 7 image, make sure that the image version is CentOS 7.3 or later. If the multi- nic-util tool is not supported on the image version that your instance uses, manually configure secondary ENIs by modifying their configuration files.

i. Download and install the multi-nic-util tool.

```
wget https://image-offline.oss-cn-hangzhou.aliyuncs.com/multi-nic-util/multi-nic-ut il-0.6.tgz && \ tar -zxvf multi-nic-util-0.6.tgz && \ cd multi-nic-util-0.6 && \ bash install.sh
```

ii. Restart the ENI service.

```bash
systemctl restart eni.service
```

Manually configure a secondary ENI by modifying its configuration file. i. Open the configuration file of the secondary ENI.

```
vi /etc/sysconfig/network-scripts/ifcfg-eth1
```

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. The following section provides an example of the ENI information to add to the configuration file:

```
DEVICE=eth1 # Specify the ENI that you want to configure. BOOTPROTO=dhcp ONBOOT=yes TYPE=Ethernet USERCTL=yes PEERDNS=no IPV6INIT=no PERSISTENT_DHCLIENT=yes HWADDR=00:16:3e:0f:**:** # Enter the obtained MAC address of the ENI. DEFROUTE=no # Specify not to use the ENI as the default route. To prevent the defa ult route of the ECS instance from being changed when you run the ifup command to s tart the secondary ENI, do not set eth1 as the default route.
```

iii. Restart the network service. For versions earlier than CentOS 7, such as CentOS 6, run the following command:

```
service network restart
```

aces For CentOS 7 or later and Alibaba Cloud Linux 2, run the following command:

```bash
systemctl restart network
```

After you configure the secondary ENI, you can configure routes for the ENI. For more information, see Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system.

> If you want to create custom images from the instance whose ENIs are configured, you must first run the **/etc/eni_utils/eni-cleanup** command to remove network configurations from /etc/udev/rules.d/70-persistent-net.rules and /etc/sysconfig/network-scripts/.

**Configure a secondary ENI for an instance that runs an Alibaba**

**Cloud Linux 2 operating system and uses the systemd-**

**networkd network service**

If your instance runs an Alibaba Cloud Linux 2 operating system and uses the systemdnetworkd network service, you must manually configure a secondary ENI by modifying the configuration file of the ENI.
1. Open the configuration file of the secondary ENI.

```
vi /etc/systemd/network/60-eth1.network
```

2. Add the information of the secondary ENI to the configuration file. Then, save and close the
configuration file. You can use one of the following methods to assign a dynamic or static IP address to the secondary ENI based on your requirements. The following section provides examples of the ENI information to add to the configuration file when different methods are used: Assign a dynamic IP address to the secondary ENI by using the Dynamic Host Configuration Protocol (DHCP).

```
[Match] Name=eth1 # Specify the ENI that you want to configure. [Network] DHCP=yes [DHCP] UseDNS=yes
```

Assign a static IP address to the secondary ENI.

```
[Match] Name=eth1 # Specify the ENI that you want to configure. [Network] Address=192.168.**.*2/24 # Specify the static IP address and subnet mask to be assi gned.
```

> **Note:** In the preceding example, `192.168.**.*2` is the primary private IP address and the `/24` subnet mask is `255.255.255.0` .

3. Restart the network service.
aces

```bash
systemctl restart systemd-networkd
```

**Configure a secondary ENI for an instance that runs a Ubuntu**

**or Debian operating system**

If your instance runs a Ubuntu or Debian operating system, you must configure a secondary ENI by modifying the network interface controller (NIC) configuration file based on your image version. Perform the following operations on an instance that runs a Ubuntu 14.04, Ubuntu 16.04, or Debian operating system: i. Open the NIC configuration file.

```
vi /etc/network/interfaces
```

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. The following section provides an example of the ENI information to add to the configuration file:

```
auto eth0 iface eth0 inet dhcp auto eth1 # Specify the ENI that you want to configure. iface eth1 inet dhcp
```

> **Note:** The eth0 primary ENI is configured in the same configuration file as the eth1 secondary ENI. You must also add the information of the primary ENI to the configuration file.

iii. Restart the network service. For versions earlier than Ubuntu 16.04, such as Ubuntu 14.04, run the following command:

```
service networking restart
```

For Ubuntu 16.04 and Debian, run the following command:

```bash
systemctl restart networking
```

The configurations of the secondary ENI take effect regardless of whether the following alert notification appears. You can run the `ip address show` command to check whether the IP addresses of the secondary ENI are recognized. Perform the following operations on an instance that runs Ubuntu 18.04: i. Open the configuration file of the secondary ENI.

```
vi /etc/netplan/eth1-netcfg.yaml
```

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. aces

> **Note:** When you modify the configuration file, take note of the following items:
> The configuration file is in the `YAML` format. You must follow the `YAML` syntax rules when you configure the file.
> Tabs cannot be used for indentation in `YAML` files. Use spaces instead.
> We recommend that you copy information from the default /etc/netplan/99- netcfg.yaml configuration file to prevent format issues.

The following section provides an example of the ENI information to add to the configuration file:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    eth1:
      dhcp4: yes
      dhcp6: no
```

iii. Apply the added configurations.

```
netplan apply
```

**Configure a secondary ENI for an instance that runs a SUSE or**

**openSUSE operating system**

If your instance run a SUSE or openSUSE operating system, you must manually configure a secondary ENI by modifying its configuration file.
1. Open the configuration file of the secondary ENI.

```
vi /etc/sysconfig/network/ifcfg-eth1
```

2. Add the information of the secondary ENI to the configuration file. Then, save and close the
configuration file. In the following example, a dynamic IP address is assigned to the secondary ENI by using DHCP.

```
BOOTPROTO='dhcp4' STARTMODE='auto' USERCONTROL='no'
```

3. Restart the network service.
For versions earlier than SUSE Linux Enterprise Server 12, run the following command:

```
service network restart
```

For SUSE Linux Enterprise Server 12 or later, run the following command:

```bash
systemctl restart network
```

**Configure routes for a secondary ENI of an instance that runs**

**an Alibaba Cloud Linux 2 or CentOS 7 operating system**

If you manually configure secondary ENIs but do not configure routes for them or if routes configured by the multi-nic-util tool do not meet your requirements, perform the following steps to configure routes. aces
1. View route information.

```
route -n
```

Sample command outputs: The following command output shows only the route information of the eth0 primary ENI, which indicates that no routes are configured for the eth1 secondary ENI. The following command output shows the route information of both the eth0 primary ENI and the eth1 secondary ENI. If the configured routes do not meet your requirements, you can modify the routes.
2. Plan the default route based on your requirements.
In this example, the sample values listed in the following table are used.

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| Primary private IP address | 192.168.**.*2 |
| Gateway address | 192.168.**.253 |
| metric | 1001 |

3. Configure the default route.
You can run the following commands to add the default route for the eth1 secondary ENI, create a route table, and then attach a routing policy to the table. In this example, a route table named table 1001 is created. We recommend that you keep the route table name the same as the metric value in the default route of the ENI. 192.168.**.253 is the gateway address and 192.168.*.*2 is the primary private IP address of the eth1 secondary ENI.

```
ip -4 route add default via 192.168.**.253 dev eth1 metric 1001 && \ ip -4 route add default via 192.168.**.253 dev eth1 table 1001 && \ ip -4 rule add from 192.168.**.*2 lookup 1001
```

4. View the created route table and routing policy.

```
ip route list table 1001 && \ ip rule list
```

The following figure shows that the route table and routing policy are created. aces
5. Configure routes to automatically update on instance startup.
After you perform the preceding steps to configure routes for the eth1 secondary ENI, you must perform the following steps to configure the routes to automatically update on instance startup. Otherwise, the routes become invalid when the instance is restarted. i. Open the /etc/rc.local file.

```
vim /etc/rc.local
```

ii. Add the configuration information of the routes to the /etc/rc.local file. Then, save and close the file.

```
ip -4 route add default via 192.168.**.253 dev eth1 metric 1001 ip -4 route add default via 192.168.**.253 dev eth1 table 1001 ip -4 rule add from 192.168.**.*2 lookup 1001
```

iii. Grant execution permissions on the /etc/rc.local file.

```
chmod +x /etc/rc.local
```

**Configure routes for a secondary ENI of an instance that runs a**

**CentOS 8 operating system**

If routes configured by the system do not meet your requirements, perform the following steps to configure routes.
1. View route information.

```
route -n
```

The following command output shows the route information of both the eth0 primary ENI and the eth1 secondary ENI. If the configured routes do not meet your requirements, you can modify the routes.
2. Plan the default route based on your requirements.
In this example, the sample values listed in the following table are used.

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| Primary private IP address | 192.168.**.*2 |
| Gateway address | 192.168.**.253 |
| table | 1001 |

aces
3. Create a script for configuring routes.
i. Create and open the /root/route.sh file. ii. Add the configuration information of the routes to the /root/route.sh file. Then, save and close the file. The following section shows how to create a route table and attach a routing policy to the route table for the eth1 secondary ENI. In this example, a route table named table 1001 is created. 192.168.**.253 is the gateway address and 192.168.*.*2 is the primary private IP address of the eth1 secondary ENI.

```
#!/bin/bash
i=0 while true; do
        /usr/sbin/ip -4 route add default via 192.168.**.253 dev eth1 table 1001
        if [ $? -eq 0 ]; then
                break
```

`fi`

```
        sleep 3
        let i++
        if [ $i -gt 10 ]; then
                exit -1
```

`fi`

```
done i=0 while true; do
        /usr/sbin/ip -4 rule add from 192.168.**.*2 lookup 1001
        if [ $? -eq 0 ]; then
                break
```

`fi`

```
        sleep 3
        let i++
        if [ $i -gt 10 ]; then
                exit -1
```

`fi`

```
done
```

4. Configure the default route.

```
sh /root/route.sh
```

5. View the created route table and routing policy.

```
ip route list table 1001 && \ ip rule list
```

The following figure shows that the route table and routing policy are created.
6. Configure routes to automatically update on instance startup.
After you perform the preceding steps to configure routes for the eth1 secondary ENI, you aces must perform the following steps to configure the routes to automatically update on instance startup. Otherwise, the routes become invalid when the instance is restarted. i. Open the /etc/rc.local file.

```
vim /etc/rc.local
```

ii. Add the configuration information of the routes to the /etc/rc.local file. Then, save and close the file.

```
sh /root/route.sh
```

iii. Grant execution permissions on the /etc/rc.local file.

```
chmod +x /etc/rc.local
```

### 11.5 View ENIs

You can view the list of created elastic network interfaces (ENIs).
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to search for ENIs that meet specified conditions:
Select a filter option from the drop-down list and enter relevant information in the search box. Then, the system searches for ENIs based on your specified filter condition. Click **Advanced Filter**, specify multiple filter options, and then click **Search**. Eligible ENIs are displayed in the disk list.

> **Note:** You can use the Advance Filter feature and specify multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| ENI Name | Enter an ENI name to search for the ENI. |
| ENI ID | Enter an ENI ID to search for the ENI. |
| vSwitch ID | Enter a vSwitch ID to search for ENIs that are connected to the vSwitch. |
| Security Group ID | Enter a security group ID to search for ENIs that belong to the security group. |
| Instance ID | Enter an instance ID to search for ENIs that are bound to the instance. |
| Tag | Enter a tag key or a tag value to search for the ENIs to which the tag key or value is added. |

aces

### 11.6 Modify the attributes of a secondary ENI

**secondary ENI**

You can modify the attributes of a secondary elastic network interface (ENI), including its name and security group.

**Prerequisites**

The secondary ENI is in the **Available** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI whose attributes you want to modify and click **Modify** in the
**Actions** column.
5. In the **Modify ENI** dialog box, modify the name and security group of the ENI.
6. Click **OK**.

### 11.7 Unbind a secondary ENI from an ECS instance

**an ECS instance**

You can unbind a secondary elastic network interface (ENI) from an Elastic Compute Service (ECS) instance. After the secondary ENI is unbound from the instance, the instance no longer processes the traffic on the ENI.

**Prerequisites**

Before you unbind a secondary ENI, make sure that the following requirements are met: The secondary ENI is in the **Bound** state. The instance to which the secondary ENI is bound is in the **Running** or **Stopped** state.

**Background information**

Only secondary ENIs can be manually unbound. Primary ENIs share the same lifecycle as the associated instances and cannot be manually unbound.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI that you want to unbind and click **Unbind** in the **Actions** column.
5. In the message that appears, click **Unbind**.

**Result**

If the secondary ENI is unbound from the instance, **Available** is displayed in the **Status** column corresponding to the ENI. aces

### 11.8 Delete a secondary ENI

You can delete elastic network interfaces (ENIs) that are no longer needed. Secondary ENIs can be deleted, whereas primary ENIs cannot.

**Prerequisites**

The secondary ENI is in the **Available** state.

**Background information**

When an ENI is deleted, the following results occur: The primary private IP address (PrimaryIpAddress) of the ENI is automatically released. The ENI is removed from all security groups to which it was added.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI that you want to delete and choose
**> Delete** in the **Actions**
column.
5. In the message that appears, click **Delete**.

**Result**

On the ENI page, refresh the ENI list. If the ENI is deleted, it is no longer displayed.

## 12 Key pairs

### 12.1 Overview

Key pairs are a secure and convenient authentication method provided for Elastic Compute Service (ECS) instance logons. Only Linux instances support key pair-based authentication.

**Introduction**

A key pair is a pair of public and private keys that are generated based on an encryption algorithm. By default, 2048-bit RSA key pairs are used. Before you log on to a Linux instance by using a key pair, you must first create a key pair. You can specify a key pair when you create an instance, or bind a key pair to an instance after the instance is created. Then, you can use the private key to connect to the instance.

**Benefits**

Key pair-based authentication has the following advantages over username and passwordbased authentication: Security: Key pairs provide higher security and reliability for logons. Key pairs are more secure than regular user passwords against brute-force attacks. Private keys cannot be deduced even if the public keys are maliciously acquired. Ease of use: If you configure a public key on a Linux instance, you can run an SSH command or use a connection tool to log on to the instance with the corresponding private key, instead of a password. Each key pair can be bound to up to 50 Linux instances. After you bind a key pair to Linux instances, you can connect to the instances without the need to specify the usernames and passwords for the instances. If you want to batch manage multiple Linux instances, we recommend that you use a key pair to log on to the instances.

**Limits**

Key pairs have the following limits: If you use a key pair to log on to a Linux instance, the password logon method is disabled for higher security. Key pairs apply only to Linux instances. Currently, only RSA 2048-bit key pairs can be created in the ECS console. Each Alibaba Cloud account can have up to 500 key pairs per region. Only a single key pair can be bound to each Linux instance in the ECS console. If you bind a key pair to an instance to which another key pair is already bound, the new key pair replaces the original one. If you want to use multiple key pairs to log on to a Linux instance, you can manually modify the ~/.ssh/authorized_keys file from within the instance to add multiple key pairs. For data security purposes, after you bind a key pair to or unbind a key pair from an instance in the **Running** ( `Running` ) state, restart the instance for the operation to take effect.

**Creation methods**

You can use one of the following methods to create a key pair: Create a key pair in the ECS console. By default, the key pair is generated in the RSA 2048bit format. For more information, see Create a key pair.

> **Important:** If you create a key pair in the ECS console, you must download and securely lock away the private key. After the key pair is bound to an instance, you cannot log on to the instance if you do not have the private key.

Import your own key pair to ECS. For more information, see Import a key pair.

> **Note:** Key pairs that you want to import must support one of the following encryption methods:

rsa dsa ssh-rsa ssh-dss ecdsa ssh-rsa-cert-v00@openssh.com ssh-dss-cert-v00@openssh.com ssh-rsa-cert-v01@openssh.com ssh-dss-cert-v01@openssh.com ecdsa-sha2-nistp256-cert-v01@openssh.com ecdsa-sha2-nistp384-cert-v01@openssh.com ecdsa-sha2-nistp521-cert-v01@openssh.com

### 12.2 Create a key pair

This topic describes how to create a key pair in the Apsara Uni-manager Management Console. After a key pair is created, its private key is automatically downloaded. You must securely store the private key to ensure its confidentiality. To log on to an Elastic Compute Service (ECS) instance to which a key pair is bound, you must provide the private key. This topic describes how to create a key pair in the Apsara Uni-manager Management Console.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Key Pairs**.
3. Click **Create Key Pair**.
4. On the Create Key Pair page, configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | Select an organization in which to create the key pair. Make sure that the key pair and the virtual private cloud (VPC) belong to the same organization. |
|   | Resource Set | Yes | Select a resource set in which to create the key pair. Make sure that the key pair and the VPC belong to the same resource set. |
|   | Region | Yes | Select a region in which to create the key pair. Make sure that the key pair and VPC belong to the same region. |

| Basic Settings | Key Pair Name | Yes | Enter a name for the key pair. The key pair name must be unique. The name must be 2 to 128 characters in length and cannot start with a special character or a digit. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), and colons (:). |
|---|---|---|---|
|   | Creation Mode | Yes | Select a method to creating the key pair. We recommend that you select Auto-create. Then, you must securely store the private key in a timely manner. Auto-create: The system creates a key pair for you. The private key is automatically downloaded after the key pair is created. The private key can be downloaded only once. You must securely store the private key file. Import: You can enter a Base64-encoded public key in the Public Key field. |

5. Click **Create**.

**Result**

After the key pair is created, your browser downloads the private key file to your computer.

> **Important:** Private key files are downloaded to your computer only when Auto- create is selected. Private key files are not saved in the ECS console and cannot be recovered if they are lost. Make sure that you securely store your private key files to ensure their confidentiality.

**What to do next**

Before you can use a created key pair to log on to an instance, you must bind the key pair to the instance. For more information, see Bind a key pair to an instance.

### 12.3 Import a key pair

You can create an SSH key pair in the Elastic Compute Service (ECS) console. You can also use a third-party tool to generate an SSH key pair and import the public key of the SSH key pair to ECS.

**Prerequisites**

The public key information of the SSH key pair that you want to import is obtained. For information about how to obtain the public key information of SSH key pairs, see View public key information.

**Precautions**

Take note of the following items:

> **Important:** Do not import private keys. Keep private keys secure. To log on to an ECS instance to which a key pair is bound, you must provide the private key.

You can import only one public key to an ECS instance. Imported public keys must be encoded in `Base64` and support one of the following encryption methods: rsa rsa dsa ssh-rsa ssh-dss ecdsa ssh-rsa-cert-v00@openssh.com ssh-dss-cert-v00@openssh.com ssh-rsa-cert-v01@openssh.com ssh-dss-cert-v01@openssh.com ecdsa-sha2-nistp256-cert-v01@openssh.com ecdsa-sha2-nistp384-cert-v01@openssh.com ecdsa-sha2-nistp521-cert-v01@openssh.com
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Key Pairs**.
3. Click **Create Key Pair**.
4. Enter a name for the key pair and set **Creation Mode** to **Import**.

> **Note:** The name of the key pair must be unique. Otherwise, a prompt indicating that the key pair already exists appears.

5. In the **Public Key** field, enter the public key that you want to import.
6. Click **Create**.

### 12.4 Bind a key pair to an instance

**instance**

You can specify a key pair when you create an Elastic Compute Service (ECS) instance, or bind a key pair to the instance after the instance is created. This topic describes how to bind a key pair to an instance after the instance is created. If your ECS instance originally uses password-based authentication, password-based authentication is automatically disabled after the key pair is bound.

**Background information**

When you bind a key pair to an instance, take note of the following items: Each ECS instance can be bound with only a single key pair. If you bind a key pair to an instance to which another key pair is already bound, the new key pair replaces the original one. A key pair can be bound to up to 50 instances.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Key Pairs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the key pair that you want bind and click **Bind Key Pair** in the **Actions** column.
5. In the **Select Instances** list, select instances to which you want to bind the key pair to
move the instances to the right-side list. If you want to select or remove all instances, click **Move All** below the instance lists. If instance names in the **Select Instances** section are dimmed, the instances are Windows instances and cannot have key pairs bound.
6. Click **OK**.
7. If the selected instance is in the **Running** (Running) state, perform the following operations
to restart the instance to make the binding operation take effect: i. In the left-side navigation pane, choose **Instances & Images > ECS Instances**. ii. Find the instance that you want to restart and choose **Instance Status > Restart**
**Instance** in the **Actions** column.
iii. In the message that appears, click **Restart Instance**.

### 12.5 Unbind SSH key pairs

This topic describes how to unbind an SSH key pair in the Elastic Compute Service (ECS) console.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Network & Security > Key Pairs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the key pair that you want to unbind and click **Unbind Key Pair** in the **Actions**
column.
5. In the **Select Instances** section of the Unbind dialog box, click the ID or name of the
instance from which you want to unbind the key pair. Then, the instance is moved to the right-hand column.
6. Click **OK**.
7. If the selected instance is in the **Running** (Running) state, perform the following operations
to restart the instance to make the binding operation take effect: i. In the left-side navigation pane, choose **Instances & Images > ECS Instances**. ii. Find the instance that you want to restart and choose **Instance Status > Restart**
**Instance** in the **Actions** column.
iii. In the message that appears, click **Restart Instance**.

**What to do next**

After the SSH key pair is unbound, you must reset the password of the instance before you log on to the instance as the root user. For more information, see Reset the logon password of an instance.

> **Note:** If you have reset the password before you unbind the key pair, you can log on by using the new password after you unbind the key pair.

### 12.6 Add or replace a key pair

You can bind multiple SSH key pairs to a Linux instance to allow access to the instance by using the key pairs. You can also replace the existing key pairs of the instance.

**Prerequisites**

The public keys of the new key pairs are obtained. For more information, see View public key information.

**Background information**

On Linux instances, the public key information of key pairs is stored in the ~/.ssh/authorized_keys file. You can modify the file to add multiple key pairs or replace existing key pairs.

> **Note:** When you bind SSH key pairs to instances in the Elastic Compute Service (ECS) console, you can bind only one key pair to each instance. If you need only one key pair for a Linux instance, we recommend that you bind the key pair to the instance in the ECS console. For more information, see Bind a key pair.

1. Use an existing key pair to log on to the ECS instance.
2. Run the **vim .ssh/authorized_keys** command to open the ~/.ssh/authorized_keys file.
3. Add or replace public key information.
You can add and save new public key information under the existing public key information.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCys3aOkFm1Xh8iN0lijeQF5mz9Iw/FV/bUUduZjauiJa1KQJSF4+czK MAv38QEspiWStkSfpTn1g9qeUhfxxxxxxxxxx+XjPsf22fRem+v7MHMa7KnZWiHJxO62D4Ihvv2hKfskz8K44 xxxxxxxx+u17IaL2l2ri8q9YdvVHt0Mw5TpCkERWGoBPE1Y8vxFb97TaE5+zc+2+eff6xxxxxxxxxx/feMeCx 6Lhc2NEpHIPxMpjOv1IytKiDfWcezA2xxxxxxxxxx/YudCmJ8HTCnLId5LpirbNE4X08Bk7tXZAxxxxxxxxxx KB1Cxw1TbGMTfWxxxxxxxxxx imported-openssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdlrdZwV3+GF9q7rhc6vYrExwT4WU4fsaRcVXGV2Mg9RHex21hl1au7 kmnIgukBZjywlQOT4GDdsJy2nBOdJPrCEBIPxxxxxxxxxxx/fctNuKjcmMMOA8YUT+sJKn3l7rCLkesE+S588 NdRjBiiUy40kyr7Y+fqGVdSOHGMXZQPpkBtojcxxxxxxxxxx/htEqGa/Jq4fH7bR6CYQ2XgH/hCap29Mdi/G5 1nbUKuIHdMWOPvjxxxxxxxxxx+lHtTGiAIRG1riyNRVC47ZEVCg9iTWWGrWFvxxxxxxxxxx/9H9mPCO1Xt2fx xxxxxBtmR imported-openssh-key
```

> **Note:** If the ~/.ssh/authorized_keys file contains information about multiple public keys, you can log on to the instance by using the private keys that correspond to the public keys.

You can replace existing public key information with new public key information.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdlrdZwV3+GF9q7rhc6vYrExwT4WU4fsaRcVXGV2Mg9RHex21hl1au7 kmnIgukBZjywlQOT4GDdsJy2nBOdJPrCEBIP6t0Mk5aPkK/fctNuKjcmMMOA8YUT+sJKn3l7rCLkesE+S5880 dRjBiiUy40kyr7Y+fqGVdSOHGMXZQPpkBtojcV14uAy0yV6/htEqGa/Jq4fH7bR6CYQ2XgH/hCap29Mdi/G5T nbUKuIHdMWOPvjGACGcXclex+lHtTGiAIRG1riyNRVC47ZEVCg9iTWWGrWFvVlnI0E3Deb/9H9mPCO1Xt2fxx xxxxBtmR imported-openssh-key
```

If you can log on to the instance by using the new private keys, the key pairs are added or replaced.

### 12.7 View public key information

If you want to configure the same public key file for a group of Elastic Compute Service (ECS) instances and the public key file is not backed up on your on-premises device, you can view public key information by using the methods that are described in this topic.

**View public key information inside an instance**

Public key information is stored in the ~/.ssh/authorized_keys file. Open the file in an instance to view the public key information.

**On-premises Windows device**

To view public key information, perform the following operations:

> **Note:** In this example, PuTTYgen is used. The operations that you must perform may vary based on the actual key generation tool.

1. Start PuTTYgen.
2. Click **Load**.
3. Select the .ppk or .pem file.
PuTTYgen displays public key information.

**On-premises Linux or macOS device**

Run the **ssh-keygen** command with the path of the .pem file specified.

```
ssh-keygen -y -f /path_to_key_pair/my-key-pair.pem
```

View the public key information in the command output. Example:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABA****+GF9q7rhc6vYrExwT4WU4fsaRcVXGV2Mg9RHex21hl1au77GkmnIgukB ywlQOT4GDdsJy2nBOdJPrCEBIPxxxxxxxxxx/fctNuKjcmMMOA8YUT+sJKn3l7rCLkesE+S5880yNdRjBiiUy40ky Y+fqGVdSOHGMXZQPpkBtojcxxxxxxxxxxx/htEqGa/Jq4fH7bR6CYQ2XgH/hCap29Mdi/G5Tx1nbUKuIHdMWOPvjx xxxxxxx+lHtTGiAIRG1riyNRVC47ZEVCxxxxxx
```

> **Note:** If the command fails, run the `chmod 400 my-key-pair.pem` command to modify the permissions to ensure that you can view the file.

## 13 Deployment sets

### 13.1 Overview

Deployment Set is a service provided by Elastic Compute Service (ECS) that allows you to view the physical topology of hosts, racks, and vSwitches. You can select deployment policies based on your business requirements to improve the reliability and performance of your business.

**Benefits**

When you use multiple ECS instances within the same zone, you may have the following requirements on business reliability or performance:

**High business reliability**

To prevent the impacts caused by the failure of physical hosts, racks, or vSwitches, you want to distribute identical application instances across different physical hosts, racks, or vSwitches.

**High network performance**

In scenarios that involve frequent network interactions between instances, you want to associate the instances with the same vSwitch to achieve low-latency and high-bandwidth communication between the instances.

**Deployment granularities and policies**

**Deployment Granularity**

**Host**: The minimum granularity for scheduling is a physical server.

> **Note:** When you create a deployment set, **Deployment Granularity** is set to **Host** by default.

**Rack**: The minimum granularity for scheduling is a rack.
**Network Switch**: The minimum granularity for scheduling is a vSwitch.

**Deployment policy**

**Loose Aggregation**

**Strict Aggregation**

**Loose Dispersion**

**Strict Dispersion**

**Loose Aggregation** and **Strict Aggregation** are intended for higher performance, while
**Loose Dispersion** and **Strict Dispersion** are intended for higher availability.
The following Granularities and policies table describes the deployment policies and use scenarios corresponding to each deployment granularity. Table 1. Granularities and policies

| Deployment granularity | Deployment policy | Use Scenario |
|---|---|---|
| Host | Strict dispersion | General-purpose business scenarios. |
|   | Loose dispersion |   |
| Rack | Strict dispersion | Big data and databases |

| Rack |   |   |
|---|---|---|
|   | Loose dispersion | Game customers |
| vSwitch | Strict dispersion | VPN |
|   | Loose dispersion | Game customers |
|   | Strict aggregation | Big data and databases |
|   | Loose aggregation | Game customers |

**Example**

The following figure shows a typical scenario where business reliability is improved by using deployment sets. Three ECS instances of a tenant are distributed on three different physical hosts, which are distributed on at least two different racks.

> **Note:** For more information about the deployment set APIs, see **Deployment sets** in **ECS Developer Guide**.

### 13.2 Create a deployment set

You can use deployment sets to distribute or aggregate instances involved in your business. You can select hosts, racks, or vSwitches to improve service availability or network performance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Deployment Sets & Elasticity > Deployment**
**Sets**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Deployment Set**.
5. Configure the parameters described in the following table to create a deployment set.

| Section | Parameter | Required | Description |
|---|---|---|---|

| Area | Organization | Yes | The organization to which the deployment set belongs. |
|---|---|---|---|
|   | Resource Set | Yes | The resource set to which the deployment set belongs. |
|   | Region | Yes | The region in which the deployment set resides. |
| Basic Configurati ons | Deployment Domain | Yes | Specify the range of the deployment granularity. Only Default is supported. |
|   | Deployment Granularity | Yes | The basic unit in which instances can be scheduled when you deploy instances. Valid values: Host: Instances are distributed at the host level. Rack: Instances are distributed at the rack level. Network Switch: Instances are distributed or aggregated at the switch level. |
|   | Deployment Policy | No | The dispersion policies are used to improve service availability to prevent impacts on your business when a host, rack, or switch fails. The aggregation policies are used to improve network performance to minimize the access latency between instances. Valid values: Valid values when the Deployment Granularity parameter is set to Host or Rack: Loose Dispersion Strict Dispersion Valid values when the Deployment Granularity parameter is set to Network Switch: Loose Dispersion Strict Dispersion Loose Aggregation Strict Aggregation |
|   | Deployment Set Name | Yes | The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores ( ), and hyphens (-). It must start with a letter _ and cannot start with http:// or https:// . |

|   | Description | No | The description of the deployment set. To simplify future management, we recommend that you provide a suitable description. The description must be 2 to 256 characters in length and can contain letters, digits, colons (:), periods (.), commas (,), underscores ( ), _ and hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
|---|---|---|---|

6. Click **Submit**.

### 13.3 View deployment sets

You can view the list of deployment sets.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Deployment Sets & Elasticity > Deployment**
**Sets**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list and enter relevant information in the search
box to search for a specific deployment set. For example, you can select **Deployment Set Name** or **Deployment Set ID** from the drop-down list and then enter a deployment set name or ID to search for a specific deployment set.

### 13.4 Change the deployment set of an instance

**of an instance**

This topic describes how to add an Elastic Compute Service (ECS) instance to a deployment set or migrate an instance from one deployment set to another.

**Prerequisites**

The instance is in the **Stopped** or **Running** state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage and choose
> **Instance Settings >**

**Change Deployment Set** in the **Actions** column to change the deployment set of the
instance.
5. In the **Change Deployment Set** dialog box, select the destination deployment set and set
the Force Change parameter. Valid values of Forced Change:
**Yes**: allows the instance to be migrated to another host, which may cause the instance to
restart.
**No**: does not allow the instance to be migrated to another host. The instance must
remain on the current host, which may cause a failure to change the deployment set of the instance.
6. Click **OK**.

### 13.5 Modify a deployment set

After you create a deployment set, you can modify the name and description of the deployment set based on your business needs.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Deployment Sets & Elasticity > Deployment**
**Sets**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the deployment set that you want to modify and click **Modify** in the **Actions** column.
5. Modify the name and description of the deployment set.
6. Click **OK**.

### 13.6 Delete a deployment set

You can delete deployment sets that are no longer needed.

**Prerequisites**

No instances exist in the deployment set.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Deployment Sets & Elasticity > Deployment**
**Sets**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete deployment sets:
To delete a single deployment set at a time, find the deployment set and click **Delete** in the **Actions** column. To delete multiple deployment sets at a time, select the deployment sets and click
**Delete** below the deployment set list.
5. In the message that appears, click **Delete**.
ance

## 14 Monitoring & maintenance

### 14.1 Configure monitoring thresholds for organizations

**thresholds for organizations**

You can specify a monitoring period and configure thresholds for a selection of metrics to monitor resource utilization in your organization. Then, you can improve resource utilization efficiency based on monitoring results and optimization suggestions.

**Limits**

Monitoring thresholds can be configured only for organizations that use an admin account.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Monitoring & Maintenance**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Organization** tab.
5. Select one of the following quota usage types and then click **Set Thresholds**:
**High Quota Usage**: indicates that the metric usage is greater than or equal to the
threshold that you specify.
**Low Quota Usage**: indicates that the metric usage is less than or equal to the threshold
that you specify.
6. In the dialog box that appears, specify the monitoring period and metric thresholds. The
following table describes the monitoring period and metric thresholds that you configure.

| Parameter | Description |
|---|---|
| Monitoring Period | Specify the monitoring period. Valid values: 7 Days, 15 Days, and 30 Days. |
| Average CPU Quota Usage | Specify a threshold for average CPU quota usage. High quota usage: The average CPU quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Low quota usage: The average CPU quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Note The threshold can only be an integer multiple of 5%. |

ance

| Average Memory Quota Usage | Specify a threshold for average memory quota usage. High quota usage: The average memory quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Low quota usage: The average memory quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Note The threshold can only be an integer multiple of 5%. |
|---|---|
| Average Storage Quota Usage | Specify a threshold for average storage quota usage. Important This threshold is applicable only to standard SSDs and ultra disks. High quota usage: The average storage quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Low quota usage: The average storage quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Note The threshold can only be an integer multiple of 5%. |

7. Click **OK**.

**Result**

The specified monitoring period and metric thresholds are displayed above the organization list. The organizations that match the specified monitoring period and metric thresholds are displayed in the **Monitoring & Maintenance** section of the **Overview** page in the console.

### 14.2 View the list of monitored organizations

**organizations**

You can view the organizations that meet the monitoring criteria, specified thresholds, and optimization suggestions within the monitoring period.
1. Log on to the ECS console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Use one of the following methods to go to the **Monitoring & Maintenance** page:
In the **Monitoring & Maintenance** section of the **Overview** page, click **Handle Now**. ance In the left-side navigation pane, click **Monitoring & Maintenance**.
4. Click the **Organization** tab and click one of the following tabs as needed:
**High Quota Usage**: displays organizations whose quota usage reaches or exceeds the
upper thresholds that you specify.
**Low Quota Usage**: displays organizations whose quota usage reaches or falls below the
lower thresholds that you specify.

**Result**

You can view the configured monitoring period and metric thresholds on the top of the organization list. You can view the information of organizations that meet monitoring criteria within the specified monitoring period in the organization list, such as the organization name, CPU quota usage, memory quota usage, storage quota usage, instances, and actions.

**What to do next**

You can adjust the quota for an organization based on your business needs. For more information, see the **Quota management** chapter in **Apsara Uni-manager Management**
**Console User Guide**.

### 14.3 Configure monitoring metric thresholds for instances

**thresholds for instances**

You can configure the monitoring period and multiple monitoring metric thresholds for instances to improve resource utilization based on the monitoring results and optimization suggestions.

**Limits**

You can configure monitoring metric thresholds only as as an operations administrator.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Monitoring & Maintenance**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Monitoring & Maintenance** page, click the **Instances** tab.
5. Click one of the following tabs and then click **Set Thresholds**:
**High Resource Usage**: displays instances whose resource usage reaches or exceeds the
upper thresholds that you specify.
**Low Resource Usage**: displays instances whose resource usage reaches or falls below
the lower thresholds that you specify.
6. In the dialog box that appears, configure the parameters described in the following table to
specify the monitoring period and metric thresholds.

| Parameter | Description |
|---|---|
| Monitoring Period | Specify the monitoring period. By default, the monitoring period is seven days. |

ance

| Average CPU Utilization | Specify the threshold for the average CPU utilization. High resource usage: The resource usage of an instance is considered high if its average CPU utilization is greater than or equal to the upper threshold that you specify. This threshold can range from 60% to 95%. Low resource usage: The resource usage of an instance is considered low if its average CPU utilization is smaller than or equal to the lower threshold that you specify. This threshold can range from 5% to 40%. Note The threshold must be an integral multiple of 5%. |
|---|---|
| Average Memory Usage | Specify the threshold for the average memory usage. High resource usage: The resource usage of an instance is considered high if its average memory usage is greater than or equal to the upper threshold that you specify. This threshold can range from 60% to 95%. Low resource usage: The resource usage of an instance is considered low if its average memory usage is smaller than or equal to the lower threshold that you specify. This threshold can range from 5% to 40%. Note The threshold must be an integral multiple of 5%. |

7. Click **OK**.

**Result**

The specified monitoring period and metric thresholds are displayed on the top of the instance list. In the **Monitoring & Maintenance** section of the **Overview** page in the ECS console, the instances that meet monitoring criteria within the specified monitoring period are displayed.

### 14.4 View the list of monitored instances

## instances

You can view the instances that meet the monitoring criteria, specified thresholds, and optimization suggestions within the monitoring period.
1. Log on to the ECS console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Use one of the following methods to go to the **Monitoring & Maintenance** page:
ance In the **Monitoring & Maintenance** section of the **Overview** page, click **Handle Now**. In the left-side navigation pane, click **Monitoring & Maintenance**.
4. Click the **Instances** tab and click one of the following tabs as needed:
**High Resource Usage**: displays instances whose resource usage reaches or exceeds the
upper thresholds that you specify.
**Low Resource Usage**: displays instances whose resource usage reaches or falls below
the lower thresholds that you specify.

**Result**

You can view the configured monitoring period and metric thresholds on the top of the instance list. You can view the information of instances that meet monitoring criteria within the specified monitoring period in the instance list, such as the instance ID and name and resource set.

### 14.5 Reclaim instance resources

You can optimize your business layout by reclaiming under-used instance resources based on the monitoring results of metrics that you set thresholds for.

**Limits**

Only instance resources with low usage can be reclaimed. After an Elastic Compute Service (ECS) instance is moved to the recycle bin, the storage resources of the instance are retained, but its computing resources such as vCPUs and memory are released. After an ECS instance is moved to the recycle bin, the instance is retained here for a specified period of time. During the retention period, the instance can be recovered. After the retention period, the instance is automatically deleted.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Monitoring & Maintenance**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Instances** tab and click **Low Resource Usage**.
5. Find the instance that you want to reclaim, click **Recycle** in the **Actions** column.
6. In the message that appears, click **OK**.
After the instance is reclaimed, **Stopped - Pending Release** is displayed in the Status column of the instance list. You can view the instance in the recycle bin.

**Related operations**

You can restore instances in the recycle bin based on business needs. For more information, see Restore an instance.

## 15 Cloud Assistant

### 15.1 Overview

Cloud Assistant is a native automated operations and maintenance (O&M) tool developed for Elastic Compute Service (ECS). It allows you to batch maintain ECS instances and batch run commands on and send files to ECS instances in a password-free, logon-free manner without the use of jump servers. These commands can consist of shell, PowerShell, or batch scripts. Typically, you can use Cloud Assistant to install and uninstall software, start and stop services, distribute configuration files, and run commonly used commands (scripts).

**Features**

After ECS instances that have the Cloud Assistant client installed enter the **Running** ( `Running` ) state, you can use Cloud Assistant to perform the following operations on the instances by using the ECS console or by calling API operations: Run batch and PowerShell scripts on Windows instances, or run shell, Python, and Perl scripts on Linux instances. Upload files to the instances. Run the same command on multiple instances. The execution state and results of one instance do not affect other instances. Configure custom parameters in Cloud Assistant commands to adapt to different scenarios.

> **Note:** Cloud Assistant does not proactively initiate any operations. You have full control over all Cloud Assistant operations.

**Use scenarios**

Cloud Assistant can help you perform deployment and O&M tasks on ECS instances. The following list provides some examples: Uploading and running automated O&M scripts Running scripts that are already uploaded to instances Managing software lifecycle Deploying code or applications Polling processes Installing service-related patches or security updates Obtaining files from Object Storage Service (OSS) or YUM repositories to update applications on ECS instances Changing hostnames or user logon passwords

**Limits**

Recurring Cloud Assistant tasks can be configured only by calling API operations. The interval at which a command is run cannot be less than 10 seconds. For files or commands that consist of batch, PowerShell, or shell scripts with custom parameters, the following limits apply to their sizes after Base64 encoding: If a command is created not by using the immediate execution feature, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run simultaneously by using the immediate execution feature and is saved, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run simultaneously by using the immediate execution feature but is not saved, the command cannot exceed 24 KB in size after Base64 encoding. A file that you want to upload cannot exceed 32 KB in size after Base64 encoding. Each command can contain a maximum of 20 custom parameters. Cloud Assistant commands can be run only on instances that use the following operating systems: Alibaba Cloud Linux CentOS 7, CentOS 8, and later

> **Note:** CentOS 8 has reached its end of life (EOL) and is no longer maintained by the Linux community. We recommend that you migrate from CentOS 8 to Anolis or Alibaba Cloud Linux.

Debian 9 openSUSE SUSE Linux Enterprise Server (SLES) 11, SLES 12, SLES 15, and later Ubuntu 14, Ubuntu 16, Ubuntu 18, and later Windows Server 2012, Windows Server 2016, Windows Server 2019, and later

**Terms**

The following table describes relevant terms in Cloud Assistant.

| Term | Description |
|---|---|
| Cloud Assistant | A tool provided by Alibaba Cloud that can help you perform routine maintenance tasks on multiple ECS instances and ECS bare metal instances. Cloud Assistant is available in all Alibaba Cloud regions. |
| Cloud Assistant client | A lightweight plug-in that can be installed on ECS instances to run Cloud Assistant commands. On Windows instances, the process of the client program is named AliyunService. On Linux instances, the process of the client program is named aliyun.service. |
| Cloud Assistant daemon process | A daemon process that is used to monitor the resource consumption of the Cloud Assistant client, report the running state of the client, and restart the client if the client fails. Service name: AssistDaemon Path: /usr/local/share/assist-daemon/assist daemon _ Note The Cloud Assistant daemon process is available only for Linux instances. |
| task execution path | A path in which Cloud Assistant saves your command as a file on an ECS instance and executes the file. The path varies based on the operating system. Linux: /tmp Windows: <Installation path of Cloud Assistant>/work/script |
| command | A specific command such as a shell script or a PowerShell script that can be run on ECS instances. |

| custom parameter | A variable that is configured in the {{key}} format in a command. You can specify a custom parameter and its value in the {{"<key>":"<value>"}} format when you create a task to run the command. |
|---|---|
| one-time execution | An execution ( Invocation ) of a one-time task. A one-time task runs a command only once on one or more instances. |
| recurring execution | An execution of a recurring task. A recurring task runs a command on one or more instances based on your specified schedule. |
| execution status | The relationships among different types of execution states. For more information, see Execution states. |

**Execution states**

The following table describes the instance-level execution state of a command that is run on a single instance. The **InvocationStatus** parameter in API indicates the execution state of a command.

| Execution state in API operations | Execution state in the ECS console | Description |
|---|---|---|
| Running | Running | The command is being run. |
| Stopping | Stopping | The command is being stopped. |
| Stopped | Stopped | The command is stopped. |
| Finished | Completed | The command is run to completion. This does not indicate that the command is successful. You can check whether the command is successful based on the command output ( Output ) and the exit code ( ExitCode ). |
| Failed | Failed | The command cannot be run or the command process did not complete before the timeout period specified by Timeout expires. |

**States of batch executions and scheduled executions**

A batch execution is a one-time execution in which a command is run on multiple instances. To better manage batch executions and recurring executions, you can manage the lifecycles of the executions based on the overall execution states, instance-level execution states, and execution-level states. The **InvokeStatus** parameter in API operations indicates the execution status of a command. The following figure shows the relationships among the three types of execution states. The following table describes the overall execution states of a command that is run on multiple instances at the same time.

|   | Execution state in API operations |   | Execution state in the ECS console | Description | Priority |
|---|---|---|---|---|---|
|   | Running |   | Running | The instance-level execution state is Running on some or all instances. | 1 |
|   | Stopping |   | Stopping | The instance-level execution state is Stopping on some or all instances. | 2 |
|   | Stopped |   | Stopped | The instance-level execution state is Stopped on all instances. | 3 |
|   | Failed |   | Failed | The instance-level execution state is Failed on all instances, or is Failed on some instances and is Stopped on the other instances. | 4 |
|   | Finished |   | Completed | The instance-level execution state is Finished on all instances, or is Finished on some instances and is Stopped on the other instances. | 5 |
|   | PartialFailed |   | Partially Failed | The instance-level execution state is Failed on some instances and is Finished on the other instances. | 6 |
|   |   | PartialFailed |   |   |   |

The following figure shows the relationship between the overall execution states and the instance-level execution states of a one-time execution in which a command is run on three instances at the same time. The following table describes the states of recurring executions of a command.

| State | Description |
|---|---|
| Overall execution state | The overall execution state is always Running ( Running ) unless you stop the command on all the instances. |
| Instance-level execution state | For each instance, the instance-level execution state is alwaysR unning ( Running ) unless you stop the command on the instance. |
| Execution-level state | For more information, see Execution states. |

### 15.2 Configure the Cloud Assistant client

**Assistant client**

#### 15.2.1 Install the Cloud Assistant client

The Cloud Assistant client is used to run Cloud Assistant commands on Elastic Compute Service (ECS) instances. This topic describes how to install the Cloud Assistant client.

**Prerequisites**

An administrator account is used to install and use the Cloud Assistant client. The administrator username is root for Linux instances, and system for Windows instances. Before you install the Cloud Assistant client, make sure that your instance type and operating system support Cloud Assistant. For more information, see Limits.

**Background information**

If ECS instances are created from public images in Apsara Stack V3.16.1, the Cloud Assistant client is pre-installed on the instances. If ECS instances are created in Apsara Stack V3.13.0 to V3.16.0, the Cloud Assistant client is not pre-installed on the instances. You can call API operations to use Cloud Assistant on the instances. If you want to use features related to Cloud Assistant, install the Cloud Assistant client. The following table describes how to install the Cloud Assistant client on different operating systems.

| Operating system | Installation method |
|---|---|
| Windows | Install the Cloud Assistant client on Windows instances |
| Linux operating systems such as Alibaba Cloud Linux, CentOS, openSUSE, and SUSE Linux | Install the client on Linux instances by using the RPM package Install the client on Linux instances by using source code |
| Linux operating systems such as Debian and Ubuntu | Install the client on Linux instances by using the Debian package Install the client on Linux instances by using source code |

**Install the Cloud Assistant client on Windows instances**

1. Connect to an ECS instance as the administrator.
For more information, see Overview.
2. Download the client installation file.
You can download the installation file for a specific version of the Cloud Assistant client from one of the following URLs: Public URL for the latest version: latest version of the Cloud Assistant client Public URL for a specified version:

```
https://aliyun-client-assist.ossaccelerate.aliyuncs.com/windows/aliyun_agent_{version}_setup.exe
```

> **Note:** {version} indicates the version number of the Cloud Assistant client.

3. Double-click the installation file and install the client as instructed.
The default installation path is C:\ProgramData\aliyun\assist\ for Windows instances.

**Install the client on Linux instances by using the RPM package**

This method is applicable to operating systems such as Alibaba Cloud Linux, CentOS, openSUSE, and SUSE Linux.
1. Connect to an ECS instance as the administrator.
For more information, see Overview.
2. Download the RPM package of the Cloud Assistant client.

```
wget "https://aliyun-client-assist.ossaccelerate.aliyuncs.com/linux/aliyun_assist_latest.rpm"
```

> **Note:** {version} indicates the version number of the Cloud Assistant client.

3. Install the Cloud Assistant client.
In this example, the latest version of the Cloud Assistant client is installed.

```
rpm -ivh --force aliyun_assist_latest.rpm
```

> **Note:** The default installation path is /usr/local/share/aliyun-assist/ for Linux instances.

**Install the client on Linux instances by using the Debian**

**package**

This method is applicable to operating systems such as Debian and Ubuntu.
1. Connect to an ECS instance as the administrator.
For more information, see Overview.
2. Download the Debian package for a specific version of the Cloud Assistant client from one
of the following URLs: Public URL for the latest version:

```
wget "https://aliyun-client-assist.ossaccelerate.aliyuncs.com/linux/aliyun_assist_latest.deb"
```

Public URL for a specified version:

```
wget "https://aliyun-client-assist.ossaccelerate.aliyuncs.com/linux/aliyun_assist_{version}.deb"
```

> **Note:** {version} indicates the version number of the Cloud Assistant client.

3. If an earlier version of the Cloud Assistant client is installed on the instance, uninstall the
earlier version.

```
dpkg -r aliyun-assist
```

4. Install the Cloud Assistant client.
In this example, the latest version of the Cloud Assistant client is installed.

```
dpkg -i aliyun_assist_latest.deb
```

> **Note:** The default installation path is /usr/local/share/aliyun-assist/ for Linux instances.

**Install the client on Linux instances by using source code**

1. Connect to an ECS instance as the administrator.
For more information, see Overview.
2. Install necessary software such as Git and Go.
In this example, YUM is used to install Git and Go. If you use other versions of Linux, use the corresponding package manager. Install Git.

```bash
yum install git -y
```

Install Go.

```bash
yum install go -y
```

3. Download the source code of the Cloud Assistant client.

```
git clone https://github.com/aliyun/aliyun_assist_client
```

4. Access the source code directory.

```
cd ./aliyun_assist_client
```

5. Compile the source code.

```
go build
```

If no error message is returned, the client is installed.
6. Run the Cloud Assistant client.

```
aliyun-service -d
```

**View information of the Cloud Assistant client on an ECS**

**instance**

After the Cloud Assistant client is installed on an instance, you can perform the following steps to query the version number and state of the client on the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **ECS Instances** tab to view the information about the Cloud Assistant client on the
ECS instances within the current region.

#### 15.2.2 Configure DNS resolution for Cloud Assistant

**Assistant**

This topic describes how to configure Domain Name System (DNS) resolution for Cloud Assistant. During the configuration procedure, you must obtain the IP addresses that correspond to the Cloud Assistant endpoints and then modify the hosts file.

**Background information**

When you use features such as Cloud Assistant on an Elastic Compute Service (ECS) instance, the instance must have access to the endpoints required to perform actions that you specify, such as running a Cloud Assistant command. The default DNS Nameserver is installed on each ECS instance to resolve domain names. You can run the **cat /etc/resolv.conf** command to view the DNS Nameserver settings. Example command output: If you modify the configuration file to override the default DNS Nameserver settings, domain names may fail to resolve or resolve slowly when you use features such as Cloud Assistant. This may cause the features to be unavailable. For example, Cloud Assistant commands cannot be run. In this case, you can perform the following procedure to configure DNS resolution for Cloud Assistant.
1. Connect to an ECS instance. For more information, see Overview.
2. Obtain the IP addresses that correspond to the Cloud Assistant endpoints.
The following Cloud Assistant endpoints are available: Endpoint used to run Cloud Assistant commands, in the format of `<region-`

```
id>.axt.aliyun.com
```

Endpoint used to obtain the Cloud Assistant plug-in and update packages, in the format

```
of aliyun-client-assist-<region-id>.oss-<region-id>-internal.aliyuncs.com
```

> **Note:** Replace <region-id> with a region ID.

3. Modify the hosts file.

```
echo "100.100.XX.XX <region-id>.axt.aliyun.com" >> /etc/hosts && \ echo "100.118.XX.XX aliyun-client-assist-<region-id>.oss-<region-id>internal.aliyuncs.com" >> /etc/hosts
```

> **Note:** Replace `100.100.XX.XX` and `100.118.XX.XX` with the IP addresses that you obtained in the previous step.

4. Check whether the hosts file is modified.

```
cat /etc/hosts
```

If the hosts file is modified, the command output includes the Cloud Assistant endpoints and their corresponding IP addresses. Example command output: After the hosts file is modified, the ECS instance can automatically obtain IP addresses from the hosts file to resolve the Cloud Assistant endpoints.

#### 15.2.3 Start or stop the Cloud Assistant client

**client**

The Cloud Assistant client is an agent that runs Cloud Assistant commands on Elastic Compute Service (ECS) instances. This topic describes how to start or stop the Cloud Assistant client.

**Start or stop the Cloud Assistant client on a Windows instance**

To start or stop the Cloud Assistant client on a Windows instance, perform the following steps.

> **Warning:** **Aliyun Assist Service** is the process of the Cloud Assistant client. If you stop **Aliyun Assist Service**, the Cloud Assistant client stops. This may cause an exception on the instance, and the instance cannot be stopped by using the ECS console. Proceed with caution when you stop the Cloud Assistant client.

1. Connect to the Windows instance. For more information, see Connect to a Windows
instance from a Windows computer by using Remote Desktop.
2. Click Start and choose **Windows Administrative Tools > Computer Management**.
3. Choose **Computer Management (Local) > Services and Applications > Services**.
4. Find **Aliyun Assist Service** and click **Stop the service** or **Restart the service**.

**Uninstall the Cloud Assistant daemon process from a Linux**

**instance**

The Cloud Assistant daemon process is used to monitor the resource consumption of the Cloud Assistant client, report the running status of the client, and restart the client when the client fails. Before you stop the Cloud Assistant client, you must first uninstall the Cloud Assistant daemon process.

> **Note:** The Cloud Assistant daemon process is available only for Linux instances.

1. Connect to the Linux instance. For more information, see Connect to a Linux instance by
using SSH commands in Linux or Mac OS X or Connect to a Linux instance by using a remote connection tool in Windows.
2. Stop the Cloud Assistant daemon process.

```
/usr/local/share/assist-daemon/assist_daemon --stop
```

> **Note:** In the preceding command, /usr/local/share/assist-daemon/assist_daemon specifies the default path of the Cloud Assistant daemon process.

3. Uninstall the Cloud Assistant daemon process.

```
/usr/local/share/assist-daemon/assist_daemon --delete
```

4. Delete the directory of the Cloud Assistant daemon process.

```
rm -rf /usr/local/share/assist-daemon
```

**Start or stop the Cloud Assistant client on a Linux instance**

> **Note:** Before you stop the Cloud Assistant client, you must first uninstall the Cloud Assistant daemon process. For more information, see the Uninstall the Cloud Assistant daemon process from a Linux instance section.

To start or stop the Cloud Assistant client on a Linux instance, perform the following steps:
1. Connect to the Linux instance. For more information, see Connect to a Linux instance by
using SSH commands in Linux or Mac OS X or Connect to a Linux instance by using a remote connection tool in Windows.
2. Run the following commands based on the initialization process of the Linux instance.
Linux operating systems that are based on new versions of the Linux kernel typically use the **systemd** initialization process. Perform the following steps: Check whether the instance uses the systemd initialization process. If the instance uses systemd, a command output is displayed.

```
strings /sbin/init | grep "/lib/system"
```

Stop the Cloud Assistant client.

```bash
systemctl stop aliyun.service
```

Start the Cloud Assistant client.

```bash
systemctl start aliyun.service
```

Restart the Cloud Assistant client.

```bash
systemctl restart aliyun.service
```

Ubuntu 14 and earlier operating systems typically use the **UpStart** initialization process. Perform the following steps: Check whether the instance uses the UpStart initialization process. If the instance uses UpStart, a command output is displayed.

```
strings /sbin/init | grep "upstart"
```

Stop the Cloud Assistant client.

```
/sbin/initctl stop aliyun-service
```

Start the Cloud Assistant client.

```
/sbin/initctl start aliyun-service
```

Restart the Cloud Assistant client.

```
/sbin/initctl restart aliyun-service
```

Linux operating systems that are based on earlier versions of the Linux kernel typically use the **sysvinit** initialization process. Perform the following steps: Check whether the instance uses the sysvinit initialization process. If the instance uses sysvinit, a command output is displayed.

```
strings /sbin/init | grep "sysvinit"
```

Stop the Cloud Assistant client.

```
/etc/init.d/aliyun-service stop
```

Start the Cloud Assistant client.

```
/etc/init.d/aliyun-service start
```

Restart the Cloud Assistant client.

```
/etc/init.d/aliyun-service restart
```

### 15.3 Use Cloud Assistant

#### 15.3.1 Create a command

You can run Cloud Assistant commands to perform routine tasks on Elastic Compute Service (ECS) instances. The tasks include running automated O&M scripts, polling processes, resetting user passwords, installing or uninstalling software, updating applications, and installing patches. The Cloud Assistant commands can be batch or PowerShell commands for Windows instances and shell commands for Linux instances. You can specify custom parameters as variables in commands.

**Prerequisites**

The ECS instances on which you want to run a command are in the **Running** (Running) state. The Cloud Assistant client is installed on the server. For more information, see Install the Cloud Assistant client.

**Background information**

When you use the immediate execution feature, take note of the following items: Only operations administrators, organization administrators, and resource set administrators can create commands. When you encode commands in Base64, the following size limits apply: If a command is not created by using the immediate execution feature, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run by using the immediate execution feature and is saved, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run by using the immediate execution feature but is not saved, the command cannot exceed 24 KB in size after Base64 encoding. You can specify up to 20 custom parameters in a single Cloud Assistant command. You can call an API operation to run a command on up to 50 instances at the same time. When you create a command, make sure that the syntax, logic, and algorithm of the command are correct. For example, if you created the /backup directory ( `mkdir /backup` ) on an instance, you can run the following shell commands to archive a file in the directory:

```
#!/bin/bash
OF=/backup/my-backup-$(date +%Y%m%d).tgz tar -cf $OF {{file}}
```

> **Note:** In the preceding sample commands, `{{file}}` is a custom parameter. When you run the commands, you can set this custom parameter to the name of the file that you want to archive. Example: /app/usrcredential. Custom parameters can be used in scenarios that require dynamic values and values that are shared across multiple commands. We recommend that you specify custom parameters for sensitive data or data that changes together with the environment, such as AccessKey pairs, instance IDs, authorization codes, time parameters, and critical system files.

**Create a command in the ECS console**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create/Run Command**.
5. On the **Create Command** page, configure the parameters that are described in the
following table.

| Section | Parameter | Description |
|---|---|---|
| Resource Owner | Organization | Select the organization for which to create the command. |
|   | Resource Set | Select the resource set in which to create the command. |
|   | Command Source | Select a command source. Enter Command Content: Create a command. Select Saved Command: Select an existing command. |
|   | Command Name | Enter a name for the command. |
|   | Execution Plan | Select the execution plan based on which to run the command. Run Now: The command is immediately run after you click Run or Run and Save. Run on Next System Startup: The command is run the next time the associated instances are started after you click Run or Run and Save. Run on Each System Startup: The command is run each time the associated instances are started after you click Run or Run and Save. |
|   | Command Type | Select a command type. For Linux instances, select Shell. For Windows instances, select Bat or PowerShell. |
|   | Command Content | Enter or paste the command content. |

| Command Information |   |   |
|---|---|---|
|   | Use Parameters | Specify whether to use custom parameters. If you turn on User Parameters, specify custom parameters in the {{key}} format in the Command Content field. |
|   | Command Parameters | Specify the values of the custom parameters that are in the {{key}} format in the Command Content field. This parameter is available only if you turn on Use Parameters. |
|   | Command Description | Enter a description for the command. We recommend that you enter identifiable information, such as the purpose of the command, to facilitate management and maintenance. The description must be 1 to 512 characters in length. |
|   | User | Specify the username to use to run the command on ECS instances. The specified username must exist on the selected instances. We recommend that you run the command as a regular user to reduce security risks. By default, Cloud Assistant commands are run by the root user on Linux instances and by the system user on Windows instances. |
|   | Execution Path | Specify an execution path for the command. Default execution paths for instances that use different operating systems: For Linux instances, the default execution path is the /home directory of the root user. For Windows instances, the default execution path is the directory in which the Cloud Assistant client process resides, such as C:\Windows\System32\. The execution path must be 1 to 200 characters in length. |
|   | Timeout Period | Specify a timeout period for the command to run on instances. If a task that runs the command times out, Cloud Assistant forcefully terminates the task process. Unit: seconds. The value must be an integer that is greater than 10. Default value: 60. Valid values: 10 to 86400. 86,400 seconds are equivalent to 24 hours. Note If you set Timeout Period to a value that is less than 10, the system changes the value to 10 to ensure that the command can be run. |
| Instances | Instance ID/Name | Select the instances on which to run the command. |

6. Click **Save**, **Run and Save**, or **Run**.

**Create a command by using the CLI**

Sample request: Call the RunCommand operation to create and run a Cloud Assistant command named update to update the operating systems of instances.

```
aliyun ecs RunCommand --RegionId 'cn-qingdao-****-d01' \ --Name 'update' --Username 'root' --Type 'RunShellScript' \ --CommandContent 'eXVtIC15IHVwZGF0ZQ==' \ --Timeout '60' --RepeatMode 'Once' --ContentEncoding 'Base64' \ --InstanceId.1 'i-bp12e0ib2ztibede****'
```

> **Note:** The values that are enclosed in single quotation marks ('') are example values of the parameters. Configure the parameters based on actual scenarios. The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| RegionId | cn-qingdao-****-d01 | The ID of the region in which to create the command. |
| Name | update | The name of the command. |
| Username | root | The username to use to run the command on ECS instances. |
| Type | RunShellScript | The type of the command. For Linux instances, set the value to RunShellScript. For Windows instances, set the value to RunBatScript or RunPowershellScript. |
| CommandContent | eXVtIHVwZGF0ZSAte Q== | The Base64-encoded content of the command. |
| Timeout | 60 | The timeout period. |
| RepeatMode | Once | The execution plan. |
| ContentEncoding | Base64 | The encoding format. |
| InstanceId.1 | i- bp12e0ib2ztibede**** | The ID of ECS instance N on which to run the command. In this example, the value of N is 1. |

For more information, see **CreateCommand** in the **ECS Developer Guide**. Sample success response: `{`

```json
        "CommandId": "c-hz018qlm868****",
        "InvokeId": "t-hz018qlm86d****",
        "RequestId": "1D24FA80-64DB-4842-AB20-2520799****"
```

`}`

#### 15.3.2 Run a command

After you create a Cloud Assistant command, you can run it on one or more Elastic Compute Service (ECS) instances. The execution status and results of the command on multiple instances do not affect each other.

**Prerequisites**

Before you run a Cloud Assistant command on ECS instances, make sure that the instances meet the following requirements: The instances are in the **Running** ( `Running` ) state. The Cloud Assistant client is installed on the instances. For more information, see Install the Cloud Assistant client.

> **Important:** Only operations administrators, organization administrators, and resource set administrators can run Cloud Assistant commands.

**Background information**

If you select more than 50 instances to run a command in the ECS console, the system runs the command on the instances in batches.

**Run Cloud Assistant commands by using the ECS console**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the command that you want to run and click **Run** in the **Actions** column.
5. On the **Run Command** page, configure the parameters to run the command.
i. In the **Command Information** section, check command content and configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Execution Plan | Specify when to run the command. Run Now: The command is run immediately after you click Run or Run and Save. Run on Next System Startup: The command is run the next time the selected instances are started after you click Run or Run and Save. Run on Each System Startup: The command is run each time the selected instances are started after you click Run or Run and Save. |
| Command Content | Confirm the command content in the Command Content field. |
| Command Parameters | In the Command Parameters field, enter the values of the custom parameters specified in the command. No format limits apply to the data types of values for the custom parameters. If the current task does not require values for these custom parameters, you can leave the parameters empty. Note If you did not select Use Parameters when you create the command, Command Parameters is not displayed on the Run Command page. |
| User | Specify the username that you want to use to run the command on ECS instances. The specified username must exist on the selected instances. We recommend that you run the command as a regular user to reduce security risks. By default, Cloud Assistant commands are run by the root user on Linux instances and by the system user on Windows instances. |

ii. In the **Instances** section, select one or more instances on which you want to run the command.
6. Click **Run**.

**Run Cloud Assistant command by using Apsara Stack CLI**

1. **Optional:** Check the state of the instances on which you want to run a command. If the
instances are not in the **Running** ( `Running` ) state, call the StartInstance operation to start the instances.

```
aliyun ecs StartInstance --InstanceId 'i-bp1f4f6o8lv0wqof****'
```

> **Note:** Values enclosed in single quotation marks ('') are example values of the parameters. You must configure the parameters based on actual conditions.

For more information, see the "StartInstance" topic in **ECS Developer Guide**.
2. **Optional:** Call the DescribeCloudAssistantStatus operation to check whether the Cloud
Assistant client is installed on the instances.

```
aliyun ecs DescribeCloudAssistantStatus --RegionId 'cn-qingdao-****-d01' \ --InstanceId.1 'i-bp1f4f6o8lv0wqof****'
```

If the value of `CloudAssistantStatus` is true in the response, the Cloud Assistant client is installed on the instances.
3. Call the InvokeCommand operation to run a created Cloud Assistant command on the
instances and obtain the value of **InvokeId** in the response.

```
aliyun ecs InvokeCommand --RegionId 'cn-qingdao-****-d01' \ --InstanceId.1 'i-bp1f4f6o8lv0wqof****' \ --InstanceId.2 'i-bp137qu6142s3mhm****' \ --CommandId 'c-hz018qp243j****' \ --Timed 'false' \ --output cols=InvokeId
```

| Parameter | Example | Description |
|---|---|---|
| RegionId | cn-qingdao-****-d01 | The ID of the region in which to run the command. |
| InstanceId.1 | i- bp1f4f6o8lv0wqof**** | The ID of the first instance on which to run the command. |
| InstanceId.2 | i- bp137qu6142s3mhm* *** | The ID of the second instance on which to run the command. |
| CommandId | c-hz018qp243j**** | The ID of the command. |
| Timed | false | Specifies whether to periodically run the command. If you want to periodically run a command, set Timed to true. The Frequency parameter specifies the execution cycle. For example, you can set Frequency to 0 */20 * * * * to run the command every 20 minutes. For more information, see Cron expression. |

For more information, see the **"InvokeCommand**"topic in the **ECS Developer Guide**.

#### 15.3.3 Upload files to ECS instances

This topic describes how to use Cloud Assistant Agent to upload files such as configuration files and scripts to Elastic Compute Service (ECS) instances.

**Prerequisites**

The ECS instances are in the **Running** (Running) state. Cloud Assistant Agent is installed on the instance. For more information, see Install the Cloud Assistant client.

**Usage notes**

You can call an API operation to send a file to up to 50 instances at a time. The uploaded file is encoded in Base64. The size of the encoded file cannot exceed 32 KB. If you want to upload files that are larger than 32 KB in size or if you want to download files from ECS instances, we recommend that you use the FileZilla tool over the SSH File Transfer Protocol (SFTP) and port 22.

> **Important:** Only operations administrators, organization administrators, and

> resource set administrators can upload files to ECS instances.

**Procedures**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant page, click **Send File**.
5. In the **Command Information** section, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Destination Operating System | Select the operating system of the ECS instances to which you want to send files. Valid values: Linux Operating System Windows Operating System |
| File Content | Select a method that you want to use to upload the file. Valid values: Upload File: You can click Upload File to select a file or drag a file to the Upload File section. Paste File Content: You can paste the file content to the field. Note The uploaded file is encoded in Base64. The size of the encoded file cannot exceed 32 KB. |
| File Name | Specify a name for the file. Note If you turn off Overwrite, make sure that the file name is unique across the destination path of the ECS instances. |
| Destination Path | Specify the destination path to save the file. The following path is used by default: Default value when Destination Operating System is set to Linux Operating System: /root Default value when Destination Operating System is set to Windows Operating System: C:/Users/Administrator/Documents You can enter only absolute path in the field. |
| File Description | Specify a description for the file. |
| User | Specify the user to which the file belongs. This parameter is required only for Linux instances. |
| User Group | Specify the user group to which the file belongs. This parameter is required only for Linux instances. |

| Permissions | Configure permissions on the file. Default value: 0644 . This value indicates that the file owner has read and write permissions on the file, and that other users in the same user group as the file owner and public users have read permissions on the file. Note You can configure this parameter in the same manner as you configure the chmod command. This parameter is required only for Linux instances. |
|---|---|
| Overwrite | Specify whether to overwrite the file that has the same name as the uploaded file in the destination path. |
| Timeout Period | Set the timeout period for the file sending task. When the file sending task times out, Cloud Assistant forcefully stops the task process. Unit: seconds. Valid values: 10 to 86400. Default value: 60. |

6. In the **Instances** section, select the instances to which you want to send the file and
configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization to which the instance belongs. |
| Resource Set | Yes | Select the resource set to which the instance belongs. |
| Instances | Yes | Select the instances to which you want to send the file. |

7. Click **Run**.

**View the execution results of file sending tasks**

View the execution results of the file sending task.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant page, click the File Sending Results tab.
5. In the task list, view the execution state, execution ID, and destination path of the file
sending task. You can perform the following operations in the Actions column that corresponds to the file sending task: Click **View** to view the execution results of the task on each instance. Click **Export** to export the execution results of the task. Click **Resend** to execute the task again.

#### 15.3.4 Clone a command

You can clone an existing Cloud Assistant command to create a new command. You can retain all the information of the original command (cloned command) or modify information such as the name, description, type, content, execution path, or timeout period in the new command (command clone).

> **Important:** Only operations administrators, organization administrators, and resource set administrators can clone commands.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the Cloud Assistant command that you want to clone and click **Clone** in the **Actions**
column.
5. On the **Clone Command** page, configure the parameters that are described in the
following table

| Section | Parameter | Description |
|---|---|---|
| Resource Owner | Organization | Select an organization for the new command. |
|   | Resource Set | Select a resource set for the new command. |
| Command Information | Command Name | Enter a name for the new command. |
|   | Execution Plan | Select a plan on how to run the new command. Run Now: The command is immediately run after you click Run or Run and Save. Run on Next System Startup: The command is run the next time the associated instances are started after you click Run or Run and Save. Run on Each System Startup: The command is run each time the associated instances are started after you click Run or Run and Save. |
|   | Command Type | Select a command type. For Linux instances, select Shell. For Windows instances, select Bat or PowerShell. |
|   | Command Content | Edit or paste the command content. |
|   | Command Description | Enter a description for the new command. We recommend that you enter identifiable information, such as the purpose of the command, to facilitate management and maintenance. |

|   | Execution Path | Specify an execution path for the new command. Default execution paths for instances that use different operating systems: For Linux instances, the default execution path is the /home directory of the root user. For Windows instances, the default execution path is the directory where the process of the Cloud Assistant client is located. Example: C:\ProgramData\aliyun\assist\$(version). |
|---|---|---|
|   | Timeout Period | Specify a timeout period for the new command to run on instances. If a task that runs the command times out, Cloud Assistant forcefully terminates the task process. Unit: seconds. Default value: 60. Minimum value: 10. If you set Timeout Period to a value of less than 10, the system changes the value to 10 to ensure that the command can be run. |

6. Click **Save**.

#### 15.3.5 Delete a command

The number of Cloud Assistant commands that you can have within each Alibaba Cloud region is limited. To ensure a sufficient command quota, we recommend that you regularly delete commands that are no longer needed.

> **Important:** Only operations administrators, organization administrators, and resource set administrators can delete commands.

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the Cloud Assistant command that you want to delete and click **Delete** in the **Actions**
column.
5. In the message that appears, click **Delete**.

### 15.4 Cron expression

When you run a Cloud Assistant command, you can call an API operation and use the Timed and Frequency parameters to set when to run the Cloud Assistant command. The value of the Frequency parameter is a cron expression. This parameter specifies the frequency of scheduled tasks, frequency of routine maintenance, and the point in time at which to complete a one-time task.

**Introduction**

A cron expression is a string that represents time. The string consists of five spaces and six fields, which is in the `X X X X X X X` format. `X` is a placeholder of a field. If a field contains multiple values, the values are separated with commas (,). Each field can be a specific value or special characters that have logical representations.

**Field values**

The following table describes valid values and supported special characters for each field in cron expressions.

| Field | Required | Valid value range | Special character |
|---|---|---|---|
| Second | Yes | [0, 59] | * , - / |
| Minute | Yes | [0, 59] | * , - / |
| Hour | Yes | [0, 23] | * , - / |
| Day | Yes | [1, 31] | * , - / ? L W |
| Month | Yes | [1, 12] or [JAN, DEC] | * , - / |
| Week | Yes | [1, 7] or [MON, SUN]. If you use the [1, 7] format, 1 indicates Monday and 7 indicates Sunday. | * , - / ? L # |

**Special characters**

Each field in a cron expression can contain a specific number of special characters. Each special character represents a logical argument.

| Special character | Description | Example |
|---|---|---|
| * | Indicates all valid values. | In the Month field, an asterisk ( * ) indicates every month. In the Week field, an asterisk ( * ) indicates every day of the week. |
| , | Lists enumerated values. | In the Minute field, 5,20 indicates that the task is triggered once at both the 5th and 20th minutes. |
| - | Indicates a range. | In the Minute field, 5-20 indicates that the task is triggered once every minute from the 5th to 20th minute. |
| / | Indicates increments. | In the Minute field, 0/15 indicates that the task is triggered once every 15 minutes from the beginning of an hour. In the Minute field, 3/20 indicates that the task is triggered once every 20 minutes from the 3rd minute of an hour. |
| ? | Indicates an unspecified value. Only the Day and Week fields support this character. | If the Day or Week field is specified, the other field must be set to a question mark ( ? ) to prevent conflicts. |

| L | Indicates the last day of a specific period. Only the Day and Week fields support this character. Note To prevent logic errors, do not specify a list or range when you use the L character. | In the Day field, L indicates the last day of a month. In the Day of a week field, L indicates the last day of a week, which is Sunday ( SUN ). L can be preceded by a value. For example, 6L in the Week field indicates the last Saturday of a month. |
|---|---|---|
| W | The weekday that is nearest to the specified day of the month. The weekday that the W character indicates is in the same month as the specified day of the month. LW indicates the last weekday of the specified month. | If 5W is specified in the Day field and the 5th day of the month falls on Saturday, the task is triggered on Friday, which is the 4th day of the month. If the 5th day of the month falls on Sunday, the scheduled task is triggered on Monday, which is the 6th day of the month. If the 5th day of the month falls on a weekday, the scheduled task is triggered on the 5th day of the month. |
| # | A specific day of a specific week in every month. Only the Day of a week field supports this character. | In the Week field, 4#2 indicates the second Thursday of a month. |

**Examples**

The following table describes some example values of cron expressions.

| Example | Limit |
|---|---|
| 0 15 10 ? * * | Executes the task at 10:15 every day. |
| 0 15 10 * * ? | Executes the task at 10:15 every day. |
| 0 0 12 * * ? | Executes the task at 12:00 every day. |
| 0 0 10,14,16 * * ? | Executes the task at 10:00, 14:00, and 16:00 every day. |
| 0 0/30 9-17 * * ? | Executes the task every half an hour between 09:00 and 17:00 every day. |
| 0 * 14 * * ? | Executes the task every minute between 14:00 and 14:59 every day. |
| 0 0-5 14 * * ? | Executes the task every minute between 14:00 and 14:05 every day. |
| 0 0/5 14 * * ? | Executes the task every 5 minutes between 14:00 and 14:55 every day. |
| 0 0/5 14,18 * * ? | Executes the task every 5 minutes between 14:00 and 14:55 and between 18:00 and 18:55 every day. |
| 0 0 12 ? * WED | Executes the task at 12:00 every Wednesday. |
| 0 15 10 15 * ? | Executes the task at 10:15 on the 15th day of every month. |
| 0 15 10 L * ? | Executes the task at 10:15 on the last day of every month. |

| 0 15 10 ? * 6L | Executes the task at 10:15 on the last Saturday of every month. |
|---|---|
| 0 15 10 ? * 6#3 | Executes the task at 10:15 on the third Saturday of every month. |
| 0 10,44 14 ? 3 WED | Executes the task at 14:10 and 14:44 every Wednesday in March every year. |

asks

## 16 View asynchronous tasks

In Elastic Compute Service (ECS), importing custom images, exporting custom images, and changing the categories of disks are asynchronous operations. The success of an asynchronous operation indicates only that the request is sent. You can view the progress of the corresponding asynchronous task to obtain the operation results at the earliest opportunity.

**Prerequisites**

A custom image is imported or exported, or the category of a disk is changed. For more information, see Import custom images, Export a custom image, or Change the category of a disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > Asynchronous**
**Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Asynchronous Tasks** page, you can view the details of asynchronous tasks that
are executed, including **Task ID**, **Task Name**, **Task Status**, **Progress**, **Creation Time**, and **End Time**. If an asynchronous task is completed, **Completed** is displayed in the **Task Status** column and **100%** in the **Progress** column.

## 17 Dedicated hosts

### 17.1 Create a dedicated host

A dedicated host is a cloud host whose physical resources are reserved for the exclusive use of a single tenant. Elastic Compute Service (ECS) instances that are created on a dedicated host are physically isolated from the ECS instances that are created on other dedicated hosts. This topic describes how to create a dedicated host.

**Background information**

To ensure service continuity when physical servers fail, Apsara Stack provides the Automatic Instance Migration upon DDH Failure feature to migrate ECS instances that are deployed on dedicated hosts when the dedicated hosts fail. If you enable **Automatic Instance Migration**
**upon DDH Failure** when you create a dedicated host, the dedicated host and ECS instances
deployed on the dedicated host are automatically migrated to a healthy physical server when the dedicated host fails due to a hardware failure. If you do not enable **Automatic Instance**
**Migration upon DDH Failure** when you create a dedicated host, the dedicated host and
ECS instances deployed on the dedicated host are not automatically migrated to a healthy physical server when the dedicated host fails due to a hardware failure.

> **Note:** If a dedicated host is migrated to a healthy physical server after a hardware failure occurs, the ID of the dedicated host and other information such as the ID of the ECS instances deployed on the dedicated host remain unchanged. However, the machine code of the dedicated host is changed based on the new physical server.

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Hosts** tab, click **Create Host**.
5. On the **Create Host** page, configure the parameters described in the following table.

| Section | Parameter | Description |
|---|---|---|
| Basic Configurations | Organization | The organization in which to create the dedicated host. |
|   | Resource Set | The resource set in which to create the dedicated host. |
|   | Region | The region in which to create the dedicated host. |
|   | Zone | The zone in which to create the dedicated host. |
| Instance | Dedicated Host Type | The type of the dedicated host. The dedicated host type determines the instance family and the maximum number of ECS instances that you can deploy on the dedicated host. |

|   | DDH Name | The name of the dedicated host. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ and colons (:). It must start with a letter and cannot start with http:// or https://. |
|---|---|---|
|   | Quantity | The number of dedicated hosts that you want to create. |
| DDH Settings | Allow Automatic Deployment | Specify whether to add the dedicated host to the resource pool for automatic deployment. Valid values: Allow Forbid |
|   | Automatic Instance Migration upon DDH Failure | Specify whether to fail over the instances that are deployed on the dedicated host when the dedicated host fails. Valid values: Enabled Disable |

6. Click **Submit**.

**Result**

After the dedicated host is created, you can view the dedicated host in the dedicated host list and create instances on the dedicated host. For more information about the parameters used to create an ECS instance, seeCreate an instance by using the wizard.

### 17.2 Share a host

You can share a created dedicated host to other organizations. The organizations can create Elastic Compute Service (ECS) instances on the shared host. This topic describes how to share a host, change the sharing scope of a host, and view the hosts that are shared by other organizations to you.

**Share a host to other organizations**

> **Important:** Before you perform the operation, take note of the following items:

The organizations to which a host is shared can create ECS instances on the host. For information about how to create an ECS instance on a host, see Create an ECS instance on a host.

> Before you can delete a shared host, you must delete all ECS instances that reside on the host. After you delete a host that you shared to other organizations, the organizations can no longer view the host.
> Hosts can be shared only across level-1 organizations. You can share a host to up to 10 level-1 organizations at a time and to up to 50 level-1 organizations in total.

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Hosts** page, choose **Hosts > Dedicated Host** to view the list of hosts.
5. Find the host that you want to share. In the **Actions** column, click **Sharing Settings**.
6. In the **Sharing Settings** dialog box, select the organizations to which you want to share
the host from the **Organization** drop-down list.

> **Note:** If you cannot obtain a list of organizations due to insufficient permissions, enter the names of level-1 organizations in the Organization field to share the host.

7. Click **OK**.
8. (Optional) After you share a host, you can perform the following operations to change the
sharing scope of the host based on your business requirements:

**Unshare the host from an organization**

In the **Sharing Settings** dialog box, find the organization from which you want to unshare the host in the **Shared Information** section. In the **Actions** column, click the icon. Then, click **OK**.

**Add an organization to which to share the host**

In the **Sharing Settings** dialog box, select the organization to which you want to share the host from the **Organization** drop-down list and then click **OK**.

**View the hosts that are shared by other organizations to you**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Hosts** page, choose **Hosts > Shared Host**.
You can view the information of the hosts that are shared by other organizations to you. The host information includes **Host ID/Name**, **Status**, **Type**, and **vCPU Usage/Total**.

### 17.3 Create a host group

You can group dedicated hosts into host groups for easy management. This topic describes how to create a host group.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Host Groups** tab.
5. Click **Create Host Group**.
6. On the **Create Host Group** page, configure the parameters described in the following
table.

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Organization | Yes | The organization in which to create the host group. |
| Document Versio |   |   |   |

| er Guide·Dedicat | ed hosts Elastic Compute Servic |   |   |
|---|---|---|---|
| Basic Settings |   |   |   |
|   | Resource Set | Yes | The resource set in which to create the host group. |
|   | Region | Yes | The region in which to create the host group. |
|   | Zone | Yes | The zone in which to create the host group. |
| Instance | Host Group Name | No | The name of the host group. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, underscores ( ), hyphens (-), _ and colons (:). |

7. Click **Submit**.

**Result**

After the host group is created, you can view it in the host group list.

### 17.4 Create an ECS instance on a host

**host**

You can create an Elastic Compute Service (ECS) instance on a dedicated or shared host. This topic describes how to create an ECS instance on a dedicated host.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Dedicated Host** or **Shared Host** tab.
5. In the host list, find the host on which you want to create an ECS instance. In the **Actions**
column, click **Create an instance**. Configure parameters to create an ECS instance. For information about the parameters, see Create an instance. In the **Dedicated Host** section, the **Host type** and **Associated Host** parameters are automatically configured and cannot be modified.

**Result**

In the host list, find the host on which you created an ECS instance. In the **Actions** column, click **Details** to open the host details panel. On the **Instance list** tab, you can view the information of the ECS instance that you created on the host. The ECS instance information includes **Instance ID/Name**, **Organization/Resource Set**, **Status**, and **IP Address**.

### 17.5 Add dedicated hosts to a host group

**host group**

After you create a host group, you can add dedicated hosts to the host group for easy management. This topic describes how to add dedicated hosts to a host group.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Host Groups** tab.
5. Find the host group to which you want to add dedicated hosts and click **Add Host** in the
**Actions** column.
6. In the **Add Host** panel, select a dedicated host and click **Add Host**.
To add a new dedicated host, you can click **Create Host** in the **Add Host** panel. For information about the parameters used to create a host, see Create a dedicated host. After the host is created, add it to the host group.

**Result**

After the dedicated host is added to the host group, you can click the host group name to view the dedicated host in the **Hosts** list.

## 18 Install FTP software

### 18.1 Overview

File Transfer Protocol (FTP) transfers files between a client and a server by establishing two TCP connections. One is the command link for transferring commands between a client and a server. The other is the data link used to upload or download data. Before uploading files to an instance, you must build an FTP site for the instance.

### 18.2 Install and configure vsftp in CentOS

**CentOS**

This topic describes how to install and configure vsftp in CentOS to transfer files.
1. Install vsftp.

```bash
yum install vsftpd -y
```

2. Add an FTP account and a directory.
i. Check the location of the nologin file, which is usually under the /usr/sbin or /sbin directory. ii. Create an FTP account. Run the following commands to create the /alidata/www/wwwroot directory and specify this directory as the home directory of the account pwftp. You can also customize the account name and directory.

```
mkdir -p /alidata/www/wwwroot useradd -d /alidata/www/wwwroot -s /sbin/nologin pwftp
```

iii. Modify the account password.

```
passwd pwftp
```

iv. Modify the permissions on the specified directory.

```
chown -R pwftp.pwftp /alidata/www/wwwroot
```

3. Configure vsftp.
i. Open the vsftp configuration file.

```
vi /etc/vsftpd/vsftpd.conf
```

ii. Change the value of anonymous_enable from `YES` to `NO` . iii. Delete the comment delimiter ( `#` ) from the following configuration lines:

```
local_enable=YES
        write_enable=YES
        chroot_local_user=YES
```

iv. Press the Esc key to exit the edit mode, and enter `:wq` to save the modifications and exit.
4. Modify the shell configuration.
i. Open the shell configuration file.

```
vi /etc/shells
```

ii. If the file does not contain /usr/sbin/nologin or /sbin/nologin, add it to the file.
5. Start vsftp and perform a logon test.
i. Start vsftp.

```
service vsftpd start
```

ii. Use the account pwftp to perform an FTP logon test. This example uses the directory /alidata/www/wwwroot.

### 18.3 Install vsftp in Ubuntu or Debian

**Debian**

This topic describes how to install and configure vsftp in an instance running Ubuntu or Debian to transfer files.
1. Update the software source.

```
apt-get update
```

2. Install vsftp.

```
apt-get install vsftpd -y
```

3. Add an FTP account and a directory.
i. Check the location of the nologin file, which is typically under the /usr/sbinor /sbin directory. ii. Create an FTP account. Run the following commands to create the /alidata/www/wwwroot directory and specify this directory as the home directory of the account pwftp. You can also customize the account name and directory.

```
mkdir -p /alidata/www/wwwroot useradd -d /alidata/www/wwwroot -s /sbin/nologin pwftp
```

iii. Modify the account password.

```
passwd pwftp
```

iv. Modify the permissions on the specified directory.

```
chown -R pwftp.pwftp /alidata/www/wwwroot
```

4. Configure vsftp.
i. Open the vsftp configuration file.

```
vi /etc/vsftpd.conf
```

ii. Change the value of anonymous_enable from `YES` to `NO` . iii. Delete the comment delimiter ( `#` ) from the following configuration lines:

```
local_enable=YES
        write_enable=YES
        chroot_local_user=YES
        chroot_list_enable=YES
        chroot_list_file=/etc/vsftpd.chroot_list
```

iv. Press the Esc key to exit the edit mode, and enter `:wq` to save the modifications and exit. v. Open the /etc/vsftpd.chroot_list file and add the FTP account name to the file. Save the modifications and exit. You can follow steps a to d to open and save the file.
5. Modify shell configurations.
i. Open the shell configuration file.

```
vi /etc/shells
```

ii. If the file does not contain /usr/sbin/nologin or /sbin/nologin, add it to the file.
6. Start vsftp and perform a logon test.
i. Start vsftp.

```
service vsftpd restart
```

ii. Use the account pwftp to perform an FTP logon test. This example uses the directory /alidata/www/wwwroot.

### 18.4 Build an FTP site in Windows Server 2008

**Server 2008**

This topic describes how to build an FTP site on an Elastic Compute Service (ECS) instance that runs Windows Server 2008.

**Prerequisites**

The Web Server (IIS) role is added and FTP is installed on the ECS instance.
1. Connect to the instance. For more information, see Instance connecting overview.
2. Choose **Start > Administrative Tools > Internet Information Services (IIS)**
**Manager**.
3. Right-click the server name and select **Add FTP Site**.
4. Enter an FTP site name and a physical path, and then click **Next**.
5. Set **IP Address** to **All Unassigned** and **SSL** to **No SSL**, and then click **Next**.
6. Set **Authentication** to **Basic**, **Authorization** to **All Users**, and **Permissions** to **Read** and
**Write**, and click **Finish**.

**Result**

Then you can use the administrator account and its password to upload and download files through FTP. Make sure that the following conditions are met: The FTP port is not in use by other applications, and the Windows firewall is not blocking the port. The security group of the instance contains a security group rule that allows inbound traffic on the FTP port.

### 18.5 Build an FTP site in Windows Server 2012

**Server 2012**

This topic describes how to build an FTP site on an Elastic Compute Service (ECS) instance that runs Windows Server 2012.

**Prerequisites**

The Web Server (IIS) role is added and FTP is installed on the ECS instance.
1. Connect to the instance. For more information, see Instance connecting overview.
2. In the left-side navigation pane, click **IIS**.
3. In the left-side navigation pane, click **IIS**.
4. In the **SERVERS** section, right-click the server name and select **Internet Information**
**Services (IIS) Manager**.
5. Right-click the server name and select **Add FTP Site**
6. Enter an FTP site name and a physical path, and then click **Next**.
7. Set **IP Address** to **All Unassigned** and **SSL** to **No SSL**, and then click **Next**.
8. Set **Authentication** to **Basic**, **Authorization** to **All Users**, and **Permissions** to **Read** and
**Write**, and click **Finish**.

**Result**

Then you can use the administrator account and its password to upload and download files through FTP. Make sure that the following conditions are met: The FTP port is not in use by other applications, and the Windows firewall is not blocking the port. The security group of the instance contains a security group rule that allows inbound traffic on the FTP port.
