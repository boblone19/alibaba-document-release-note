---
title: "Elastic Compute Service User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 511
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Elastic Compute Service User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8ECS%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elastic%20Compute%20Service%20User%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# Elastic Compute Service User Guide 20260629

| State | State attribute | Description | State in an API response |
|---|---|---|---|
| Preparing | Intermediate | The instance is being created and waiting to start. If an instance remains in this state for an extended period of time, an exception has occurred. | Preparing |

Elastic Compute Service

## What is ECS?

### Overview

Elastic Compute Service (ECS) is a computing service that provides scalable processing capacity. It is simpler and more efficient to manage than physical servers. You can create instances, scale out disks, or delete multiple ECS instances in batches at any time as needed. An ECS instance, the core concept of Elastic Compute Service, is a virtual computing environment that includes basic computing components, such as CPUs and memory. You can use the ECS console to perform various operations on your instances. Other resources, such as Elastic Block Storage, images, and snapshots, can be used only when they are attached to an ECS instance. Elastic Block Storage Elastic Compute Service snap bandwidth

### Instance lifecycle

The lifecycle of an Elastic Compute Service (ECS) instance begins when the instance is created and ends when the instance is released. This topic describes the instance states in the ECS console as well as state attributes and their corresponding instance states in API responses. The following table describes the instance states in the ECS console and their corresponding instance states in API responses.

| Starting | Intermediate | When you start or restart an instance in the ECS console or by calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in this state for an extended period of time, an exception has occurred. | Starting |
|---|---|---|---|
| Running | Stable | The instance is in the Running state. Important The Running state indicates that an instance is running. However, this state does not always indicate that the operating system of the instance is running. The instance provides network services as expected only after the operating system of the instance is running. Then, you can connect to the instance by using methods such as SSH or Remote Desktop Protocol (RDP) and associate an elastic network interface (ENI) with or attach a disk to the instance online. | Running |
| Stopping | Intermediate | When you stop an instance in the ECS console or by calling an API operation, the instance enters this state before it enters the Stopped state. If an instance remains in this state for an extended period of time, an exception has occurred. | Stopping |
| Stopped | Stable | An instance enters this state when it is stopped. Instances in the Stopped state cannot provide external services. | Stopped |
| Changing | Intermediate | When you perform an Upgrade or Downgrade or Hot Configuration Change operation on an instance in the ECS console or by calling an API operation, the instance enters this state. If an instance remains in this state for an extended period of time, an exception has occurred. | Changing |
| Stopped - Pending Release | Stable | When you delete an instance in the ECS console or by calling an API operation and select Move to Recycle Bin, the instance enters this state. | Stopped - Pending Release |

Elastic Compute Service The following figure shows the transitions between instance states in API responses.

| Create Ins | tancPe |
|---|---|

Elastic Compute Service Restart Instance Running Starting (Starting) Stop Instance Start Instance Release Instance Stopped Stopping Released Release Instance Stable Intermediat

| Limits | Limit | Increasing quotas |
|---|---|---|
| Maximum number of system disks per instance | 1 | No |

Elastic Compute Service

## Instructions

### Suggestions

Consider the following suggestions to use Elastic Compute Service (ECS) more efficiently: ECS instances with 4 GiB or higher memory must use a 64-bit operating system. A 32-bit operating system can be used for instances with a maximum of 4 GiB of memory. A 32-bit Windows operating system can support up to 4 CPU cores. To ensure service continuity and prevent service unavailability due to failovers, we recommend that you configure service applications to start automatically on system startup.

### Limits

Before you use Elastic Compute Service (ECS) instances, you need to familiarize yourself with their limits. Windows does not support instance types with less than 2 GiB of memory. You cannot install virtualization software such as VMware on instances or use virtualization software to re-virtualize instances. ECS does not support sound card applications. Only GPU-accelerated instances support virtual sound cards. You cannot directly connect external hardware devices, such as hardware dongles, USB flash drives, external hard disks, and bank U keys, to ECS instances. ECS does not support multicast protocols. If you want to use multicast, we recommend that you use unicast point-to-point methods instead.

**Elastic block storage**

| Maximum number of data disks per instance | 64 Note Up to 64 data disks can be attached to an ECS instance. The maximum number of disks that can be attached varies by instance type. To query the maximum number of disks supported by an instance type, call the DescribeInstanceTy pes operation and check the value of the DiskQuantity parameter. You can attach up to 16 data disks to an instance when you create the instance. After the instance is created, you can attach more data disks as needed. | No |
|---|---|---|
| Capacity of a single system disk | Windows Server: 40 GiB to 2,048 GiB Red Hat: 40 GiB to 2,048 GiB CoreOS and FreeBSD: 30 GiB to 2,048 GiB Other Linux distributions: 20 GiB to 2,048 GiB | No |
| Capacity of a single data disk | Depends on the data disk category: SSD disks, ultra disks, and standard performance disks: 20 GiB to 32,768 GiB. Premium performance disks: 20 GiB to 131,072 GiB. | No |
| Mount targets of system disks | /dev/vda | No |
| Mount targets of data disks | /dev/vd[b-z] | No |

Elastic Compute Service

| Encryption of data disks created from a full image | When you use a full image that contains unencrypted data disk snapshots to create an ECS instance, you cannot encrypt ultra disks or standard SSDs created from the data disk snapshots. When you use a full image that contains encrypted data disk snapshots to create an ECS instance, you cannot specify the encryption method for ultra disks or standard SSDs created from the data disk snapshots. | No |
|---|---|---|
| Maximum number of disks that can be attached to the physical server that hosts the ECS instance | 250 | No |

| Limits | Limit | Request a quota increase |
|---|---|---|
| Maximum number of snapshots within an account | 100,000 | No |
| Maximum number of manual snapshots that can be retained for a single disk | 256 | No |
| Maximum number of automatic snapshots that can be retained for a single disk | 1,000 | No |
| Maximum number of automatic snapshot policies that can be retained per region within an account | 100 | No |
| Snapshots for which the instant availability feature is enabled | 10 | No |

| Limits | Limit | Increasing quotas |
|---|---|---|

Elastic Compute Service

| Maximum number of images within an account | 100,000 | No |
|---|---|---|
| Maximum number of users to whom an image can be shared | 50 | No |
| Image and instance type limitations | Instance types with 4 GiB of memory or larger do not support 32-bit images. | No |

| Limitations | Limit | Requesting quota increases |
|---|---|---|
| Maximum number of SSH key pairs per region within an account | 500 | No |
| Instance types that support SSH key pairs | Series I instances that are not I/O optimized are not supported. | No |
| Images that support SSH key pairs | Linux images only. | No |

| Limits | Limit | How to increase the quota |
|---|---|---|
| Number of deployment sets | 5,000 | No |

| Limitations | Basic Security Group Limits | Value for advanced security groups |
|---|---|---|
| Maximum number of security groups per region within an account | 100,000 | The value is the same as that for basic security groups. |
| Maximum number of ECS instances in a security group | This value varies based on the number of private IP addresses that the security group can contain. | Unlimited |

Elastic Compute Service

| Maximum number of security groups to which an ECS instance can be added | 10 | The value is the same as that for basic security groups. |
|---|---|---|
| Maximum number of security groups to which an elastic network interface (ENI) of an ECS instance can be added |  |  |
| Maximum number of inbound and outbound rules in a security group | 1,000. This is a shared limit across all security groups. | The value is the same as that for basic security groups. |
| Maximum number of inbound and outbound rules in all security groups to which an ENI can be added | 1,000. This is a shared limit across all security groups. | The value is the same as that for basic security groups. |
| Maximum number of private IP addresses that can be contained in a security group of the Virtual Private Cloud (VPC) type | 2,000 | 65,536 |

| Limits | Limit | Request a quota increase |
|---|---|---|
| Maximum number of Cloud Assistant commands | Unlimited | No |
| Retention period of a Cloud Assistant command execution record | 28 days | No |
| Maximum number of Cloud Assistant command execution records that can be retained | 100,000 | No |
| Maximum number of activation codes that can be used to register Cloud Assistant managed instances. | 5,000 | No |

| Limits | Limit | How to request a quota increase |
|---|---|---|

Elastic Compute Service

**ENI**

| Maximum number of secondary ENIs that can be created | A limited number of ENIs can be created per region within an account. The ENI quota is displayed in the Quota overview section of the Overview tab on the Home page of the Apsara Uni- manager Management Console. | No |
|---|---|---|

Elastic Compute Service

**ga1 instance family**

To create a ga1 instance, use one of the following images with pre-installed drivers: Ubuntu 16.04 with a pre-installed AMD GPU driver Windows Server 2016 Chinese Edition comes with a pre-installed AMD GPU driver. An AMD GPU driver is pre-installed in the Chinese version of Windows Server 2008 R2. Take note of the following items: A ga1 instance uses an optimized driver from Alibaba Cloud and AMD. The driver is preinstalled in images provided by Alibaba Cloud and cannot be downloaded. If the GPU driver malfunctions due to the removal of related components, replace the system disk to restore GPU-related features.

**Note**

Data loss may occur when the system disk is replaced. If the driver malfunctions because an improper image is selected during instance creation, replace the system disk and select an image with a pre-installed AMD GPU driver. Windows Server 2008 and earlier do not allow you to connect to instances using Virtual Network Computing (VNC) after the GPU driver takes effect. In this case, VNC does not respond and a black screen appears or the system is stuck on the splash screen. You can access the system using other methods such as Remote Desktop Protocol (RDP). RDP does not support related applications such as DirectX and OpenGL. You must install the VNC service and client, or use other supported protocols such as PC over IP (PCoIP) and XenDesktop HDX 3D.

**gn4, gn5i, and gn5 instance families**

Bandwidth: If you use a Windows Server 2008 R2 image for a gn4 instance, you cannot use VNC in the ECS console to connect to the instance after the GPU driver takes effect. You must set the bandwidth to a non-zero value or associate an elastic IP address (EIP) with the created instance. Image: If an NVIDIA GPU driver does not need to be pre-installed, select an image to create an instance and then install the driver on the instance. For more information, see Installation guideline for NVIDIA drivers.

### Usage notes on Linux

**operating systems**

Before you use Linux operating systems, take note of the following items: Elastic Compute Service Do not modify the content of the default /etc/issue files in Linux instances. If you modify the content of the default /etc/issue file on a Linux instance and use the instance to create a custom image, the operating system distribution contained in the image cannot be recognized. As a result, Linux instances that are created from the image cannot start. Do not arbitrarily modify the permissions of each directory on the partition in which the root directory is located, especially the permissions of the /etc, /sbin, /bin, /boot, /dev, /usr, and /lib directories. If you incorrectly modify the permissions, errors may occur. Do not rename, delete, or disable the root account. Do not compile the Linux kernel or perform operations on the kernel. For example, if you upgrade the Linux kernel, the following issues may occur: The core components of the operating system greatly change, which may cause risks and potential issues. You must assess the upgrade operation and resolve the issues. If you upgrade the Linux kernel to a version that is not supported in the Yellowdog Updater Modified (YUM) repository for the operating system, the following common risks and issues may occur: System instability: The new kernel may cause the operating system to be unstable. Before you upgrade the kernel, fully assess and validate the upgrade operation. Software incompatibility: Specific software that runs as expected on the original kernel may not run as expected on the new kernel. Update the software or modify the software configurations. Affected performance and functionality: Default kernel options and features may change during the upgrade, which may affect system performance and functionality. Security vulnerabilities: The new kernel may contain unknown security vulnerabilities. Loss of support: If you use a non-official kernel, you may be unable to obtain some official technical support or relevant kernel security updates. Difficulty in kernel rollback: If issues occur after the upgrade, the kernel may be difficult to roll back to the original version. If your ECS instance is in the production environment, exercise caution when you upgrade the Linux kernel. Do not enable SELinux on Linux operating systems except for CentOS and Red Hat. Do not arbitrarily change the media access control (MAC) addresses of network interface controllers (NICs). We recommend that you do not use swap partitions. Do not enable the NetWorkManager service. The service conflicts with the internal network service of the system and causes network errors.

### Usage notes on Windows

**operating systems**

Before you use Windows operating systems, take note of the following items: If a Windows instance uses local disks as data disks, the instance is at risk of data loss. If you are unsure about the reliability of the data architecture, we recommend that you use cloud disks to create Windows instances. Do not close the built-in shutdownmon.exe process. Otherwise, the server may require an extended period of time to restart. Do not rename, delete, or disable the Administrator account. Otherwise, the server usage may be affected. Elastic Compute Service We recommend that you do not use virtual memory. Do not uninstall PV drivers. Do not arbitrarily change the media access control (MAC) addresses of network interface controllers (NICs). If you change the name of your computer, you must synchronously change the following key values in the registry. If you do not synchronously change the key values in the registry, the change does not take effect, which may cause the installation of specific thirdparty programs to fail.

```
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ActiveComputerName HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
```

### Notice on defense against

**DDoS attacks**

You need to purchase Anti-DDoS Pro to defend against DDoS attacks. For more information, see **Apsara Stack Security Product Introduction** . Elastic Compute Service

## Quick start

### Overview

This topic describes how to create and connect to an Elastic Compute Service (ECS) instance. Perform the following operations: A security group acts as a virtual firewall to control inbound and outbound traffic for ECS instances. Each ECS instance must belong to at least one security group. When you create an instance, you must select a security group for the instance. An ECS instance is a virtual server that contains the basic components of a server, such as CPUs, memory, an operating system, network configurations, and disks. After a security group is created, you can select an instance type based on your business requirements to create instances in the security group. Select a method to connect to an instance based on the network configurations and operating system of the instance and the operating system of your computer. After you connect to the instance, you can perform operations on it such as installing applications.

### Log on to the ECS console

This topic describes how to log on to the Elastic Compute Service (ECS) console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

**Note**

**First login**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forgotten password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

| Section | Parameter | Required | Example |
|---|---|---|---|
|  | Organizatio n | Yes | The organization to which the security group belongs. Make sure that the security group and the specified VPC belong to the same organization. |

Elastic Compute Service
3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your login scenario: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA code and click **Authentication**. You have enabled and bound MFA: Enter the six-digit MFA code and click **Authentication**.

**Note**

For more information about how to bind and enable MFA, see **Security Center** >
**MFA** > **Manage MFA** in Apsara Uni-manager Operations Console User Guide.
5. In the top navigation bar, choose **Products > Computing > Elastic Compute Service**.

### Create a security group

Security groups are an important means to implement network security isolation. Security groups control network traffic to or from one or more Elastic Compute Service (ECS) instances.

**Background information**

Security groups determine whether ECS instances that belong to the same virtual private cloud (VPC), region, and account can communicate with each other. If the ECS instances belong to the same security group, the instances can communicate with each other over the internal network. If the ECS instances belong to different security groups, you can allow mutual access between the security groups to allow the instances to communicate over the internal network.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Security Group**.
5. Configure parameters on the Create Security Group page. The following table describes the
parameters.

| er Guide·Quick s |  |  |  |
|---|---|---|---|
| Area |  |  |  |
|  | Resource Set | Yes | The resource set to which you want to add the security group. Make sure that the security group and the specified VPC belong to the same resource set. |
|  | Region | Yes | The region in which you want to create the security group. Make sure that the security group and the specified VPC reside in the same region. |
| Basic Configurati ons | Sharing Scope | No | The sharing scope of the security group. Valid values: Current Resource Set, Current Organization and Subordinate Organizations, and Current Organization. Note If you want to change the sharing scope of a security group, you can choose > Sharing Settings in the Actions column of the security group. |
|  | Security Group Template | No | The template that you want to apply to the security group you create. Select an existing security group template. For more information, see Create a security group template. |
|  | Security Group Type | Yes | The type of the security group. Valid values: Basic Security Group: ECS instances in a basic security group can communicate with each other. You can add security group rules that reference security groups as authorization objects to basic security groups. A basic security group can contain fewer private IP addresses than an advanced security group. Advanced Security Group: An advanced security group can contain more private IP addresses than a basic security group. ECS instances in an advanced security group cannot communicate with each other. You cannot create security group rules that reference security groups as authorization objects for advanced security groups. |

|  | VPC | Yes | The VPC in which the security group is created. Select an existing VPC or click Create VPC to create a VPC. After you create a VPC, you can go back to the Create Security Group page and click the icon to update the VPC list. For more information about how to create a VPC, see the Create a VPC topic in VPC User Guide. |
|---|---|---|---|
|  | Security Group Name | Yes | The name of the security group. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). The name must start with a letter and cannot start with http:// or https:// . |
|  | Description | No | Enter a description for the security group to facilitate management. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), _ commas (,), colons (:), and forward slashes (/). The description must start with a letter and cannot start with http:// or https:// . |
|  | Synchronize | No | This parameter is displayed only after you select Security Group Template. After the synchronization feature is enabled, template rule changes are synchronized to the associated security groups. You cannot modify the rules in the security groups. For more information, see Add security group rules to a security group template. |

Elastic Compute Service
6. Create the security group.
If you create a service by setting **Cloud products** to Elastic Compute Service and
**Security Groups** on the Service Management page, confirm the security group
parameters and click **Confirm Order**. If you do not create a service by setting **Cloud products** to Elastic Compute Service and
**Security Groups** on the Service Management page, confirm the security group
parameters and click **Submit**. For more information about service catalog management, see the **Manage service**
**catalogs** topic in **Apsara Uni-manager Operations Console User Guide** .

**Verify the result**

After you create a security group, you can view the security group on the **Security Groups** page.

**What to do next**

Elastic Compute Service After a security group is created, the security group does not contain security group rules. You can create security group rules for the security group to allow or deny access to or from the Internet or the internal network for ECS instances that belong to the security group. For more information, see Create a security group rule. Each ECS instance must belong to at least one security group. You can add an ECS instance to one or more security groups. For more information, see Add an ECS instance to a security group.

### Create an instance

An Elastic Compute Service (ECS) instance is a virtual machine that consists of basic components, such as the CPU, memory, operating system, network settings, and disks. This topic describes how to create one or more ECS instances.

**Procedure**

**Important**

For information about the limits that apply when you create ECS instances, see Limits.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the page that appears, click **Create Instance**.
5. (Optional) Select a service catalog and click **OK**.
The service management feature is used to manage and control specific specifications of specific services within an enterprise or an organization. This parameter is displayed only after you create and publish services that grant the current organization or user permissions to access ECS instances. For more information about service catalog management, see the **Manage service catalogs** topic in **Apsara Uni-manager**
**Operations Console User Guide**.
6. Configure the region, type, image, and storage of the instance.
7. Before you click Create Order, check the instance configurations in the **Configuration**
**overview** section and configure parameters such as Duration on the right side of the ECS
instance buy page. Make sure that all configurations meet your business requirements. In the **Configuration overview** section on the right side of the page, click **Save as a**
**configuration template** to save the required configurations, such as instance type,
operating system, network settings, security rules, and storage configurations, as a configuration template. You can use a specific configuration template to quickly create ECS instances later without the need to configure all parameters.
8. Create the ECS instance.
If a service whose **Resources** value is **ECS** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Confirm Order**. If no service whose **Resources** value is **ECS** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Submit**.

**Parameters and descriptions**

| Parameter | Required | Description |
|---|---|---|
| Organization/Reso urce Set | Yes | Select the organization and resource set to which the instance belongs. |
| Geography/Availa bility Zone | Yes | Select the region and zone to which the instance belongs. Zones are physical locations in a region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create ECS instances in different zones. |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service

**Billing Configuration**

**Note**

This parameter is available only if the administrator has configured billing rules in the operations center. For more information about the billing rules, see the **Create a billing**
**configuration** topic in **Apsara Uni-manager Operations Console User Guide** .
The **Pay-as-you-go** and **Subscription** billing methods are supported.
**Pay-as-you-go**: You can use the service first. Fees are charged afterward based on the
actual amount of resources that you used. This method is suitable for scenarios in which business usage frequently fluctuates, which allows users to flexibly utilize resources based on actual needs and avoid waste.
**Subscription**: You can directly subscribe to resources for a fixed period of time, and fees
are charged based on the quantity and duration. No additional fees are incurred during subsequent usage. This method is suitable for scenarios where business usage is relatively stable.

**Regional Information**

Instance types offer varying combinations of compute, memory, and storage capacities to fit different use cases. Instance types must be used together with images, block storage devices, and network resources to create ECS instances that serve different purposes.

**Note**

The Quota allowance section displays the CPU, GPU, and memory quotas for the region, organization, and resource set that you selected. If remaining quotas are insufficient, click the icon to view and configure quotas.

| Open the thermal transformer | No | Specifies whether to enable hot configuration change for the instance. If you set this parameter to Yes, you can change the instance type without the need to stop the instance. For more information, see Perform a hot configuration change on an instance to change the instance type. If instance types that support hot configuration changes are available, this parameter is set to Yes by default. In this case, the instance type list displays only the instance types that support hot configuration changes. Note If you do not want to select an instance type that supports hot configuration changes, set this parameter to No. All available instance types are displayed. If no instance types that support hot configuration changes are available, this parameter is set to No by default. In this case, the instance type list displays all available instance types. |
|---|---|---|
| Filter | No | The condition based on which instance types are filtered. You can select CPU, memory, or GPU as the filter condition, or enter a keyword to search for instance types. |
| CPU Type | Yes | Select a CPU type. Valid values: Intel/X86 Hygon/X86 Kunpeng/ARM Phytium/ARM Yitian/ARM Zhaoxin/X86 Others Note The supported CPU types are displayed on the Create an instance page in the ECS console. |

Elastic Compute Service

| Category | Yes | Select an instance category. Valid values: Dedicated Shared Local SSD Local HDD Super Computing Cluster ECS Bare Metal Instance Others Note The actual instance types that are supported are displayed on the Create an instance page in the ECS console. |
|---|---|---|

Elastic Compute Service

| Specifications | Yes | The instance type. Instance types are displayed in a list that consists of the Instance Family, Instance Type, Instance Family Level, Status, CPU Type, CPU Cores, Memory, GPU Specifications, GPUs, Internal Bandwidth, and Number of Disks columns. Select an instance type based on your business requirements. For information about instance families and instance types, see the Instance types topic in the Apsara Stack documentation. Important Available, Sold Out, or Disabled can be displayed in the Status column of an instance type. You can select only instance types in the Available state. If you select a service catalog when you create an instance, the available instance types are limited by the service catalog. For more information, see the Example: Create an ECS instance service topic in Apsara Uni- manager Management Console User Guide. Instance types that have specific vCPU and memory combinations do not support Windows Server images. For more information, see Limits. Important To create a GPU-accelerated instance, you need to install a GPU driver on the instance based on the operating system of the instance. Except that you must install GPU drivers on GPU- accelerated instances, you can manage GPU- accelerated instances in the same manner as you manage non-GPU-accelerated instances. For information about how to install GPU drivers on NVIDIA GPU-accelerated instances, see Installation guideline for NVIDIA drivers. For information about how to install GPU drivers on instances that are equipped with GPUs from other manufacturers, see the official documents of the manufacturers. To create an ECS instance of a Super Computing Cluster (SCC) instance category, you must set the Super Computing Cluster parameter instead of the Deployment Set parameter. The VPC and Security Group parameters may be affected by the virtual private cloud (VPC) ID and security group ID of the SCC. For more information about SCCs, see Overview of SCCs. |
|---|---|---|

Elastic Compute Service

| Super Computing Cluster | Subject to the Category value and the selected instance type | The ID of the SCC to which the instance belongs. You can select an existing SCC or click Create Cluster to create an SCC. After the SCC is created, go back to the Create an instance page and click the icon to obtain the latest SCC list. For more information about how to create an SCC, see Create an SCC. This parameter is available and can be configured only if you set the Category parameter to Super Computing Cluster and select an SCC instance type. This parameter is required when you create an instance of an SCC instance type. |
|---|---|---|
| Instances | Subject to the Super Computing Cluster value | The number of nodes (ECS instances) in the SCC. This parameter is automatically configured and cannot be modified after you configure the Super Computing Cluster parameter. |
| HT Hyper- Threading Technology | No | Specifies whether to enable hyper-threading for the instance. Only specific instance types support the HT Hyper- Threading Technology parameter. You can configure the HT Hyper-Threading Technology parameter after you click Show Advanced options. For more information about HT Hyper-Threading Technology, see Disable HT. If you turn on HT Hyper-Threading Technology, two logical processing cores are created for each physical core of the ECS instance. If you turn off HT Hyper-Threading Technology, the ECS instance exclusively uses CPU physical cores. |
| CPU Topology | No | You can select HT Continuous CPU Topology or HT Discrete CPU Topology. You can modify the CPU topology only for specific instance types. You can modify the CPU Topology parameter after you click Show Advanced options. For more information about CPU topologies, see View and modify CPU topologies. HT continuous CPU topology: Logical cores are continuously assigned to physical cores, which can help reduce communication and contention between threads. This mode is suitable for computing tasks that require low memory access latency and computing power close to computing power provided by the physical cores, such as scientific computing, data analysis, and high-performance computing, which are sensitive to memory access and core computing. HT discrete CPU topology: Logical cores are discretely distributed to physical cores, which can help reduce resource contention in a multi-threaded environment and provide better performance isolation. This mode is suitable for the tasks that are separately assigned to threads or the tasks that require high single-thread performance. |

Elastic Compute Service

**Image ID**

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image, Custom Image, Shared Image, and Enterprise Public Image. Note For more information, see Overview. |
| Public Image | Subject to the Image Type value | Select a public image. Public images that are provided by Alibaba Cloud without operating system licenses deliver high security and stability. Public images for Windows Server operating systems and mainstream Linux operating systems are provided. This parameter is required if you set the Image Type parameter to Public Image. |
| Support ecs-user user login | Subject to the Public Image value | This parameter is available only if you select a public image that supports logins of the ecs-user user to create a Linux ECS instance. If you turn on Support ecs-user user login, ecs- user is used as the username to log in to the Linux ECS instance. If you turn off Support ecs-user user login, root is used as the username to log in to the Linux ECS instance. Warning If you log in to an ECS instance as the root user, you have the highest permissions on the instance. However, security risks may arise. We recommend that you log in to the ECS instance as the ecs-user user. The following public images support ecs-user: x86: Alibaba Cloud Linux 2: aliyun 2 1903 x86 64 20G alibase 2024 _ _ _ _ _ _ _ 0628.vhd aliyun 2 1903 x86 64 20G dengbao alib _ _ _ _ _ _ _ ase 20240705.vhd _ |

Elastic Compute Service Images contain information required to run instances. Alibaba Cloud provides a variety of image sources for easy access to images. The following table describes the image sources.

|  |  | Alibaba Cloud Linux 3: aliyun 3 x86 64 20G alibase 20241103.v _ _ _ _ _ _ hd aliyun 3 x86 64 20G container optimize _ _ _ _ _ _ d 20241226.vhd _ aliyun 3 x86 64 20G dengbao alibase 2 _ _ _ _ _ _ _ 0241103.vhd aliyun 3 x86 64 20G pro alibase 202412 _ _ _ _ _ _ _ 25.vhd aliyun 3 x86 64 20G pro dengbao alibas _ _ _ _ _ _ _ e 20241030.vhd _ aliyun 4 x86 64 20G alibase 20250728.v _ _ _ _ _ _ hd UOS: uos 20 1070a x86 64 20G alibase 2024 _ _ _ _ _ _ _ 1129.vhd Arm: |
|---|---|---|
|  |  | UOS uos 20 1070a arm64 20G uefi alibase 2 _ _ _ _ _ _ _ 0241119.vhd Alibaba Cloud Linux: aliyun 3 arm64 20G uefi dengbao alibas _ _ _ _ _ _ e 20241103.vhd _ |
| Custom Image | Subject to the Image Type value | Select a custom image. Custom images are created from ECS instances or snapshots or imported from your computer. This parameter is required if you set the Image Type parameter to Custom Image. |
| Shared Image | Subject to the Image Type value | Select a shared image. Shared images are custom images that are shared by other level-1 organizations to your organization. This parameter is required if you set the Image Type parameter to Shared Image. |
| Enterprise Public Image | Subject to the Image Type value | Select an enterprise public image. Enterprise public images are images that are shared by an administrator in the Apsara Uni-manager Operations Console. This parameter is required if you set the Image Type parameter to Enterprise Public Image. |

Elastic Compute Service System disks and data disks are attached to instances to provide storage capacity. System disks are used to install operating systems, while data disks are used to store application data.

| Parameter | Required | Description |
|---|---|---|
| Creation Method | Yes | Select the method that you want to use to create a disk. Valid values: Normal Creation and Storage Set Creation. To create a disk in a partition of a specific storage set, select Storage Set Creation. Important If only Normal Creation is displayed, storage sets are not supported in the current environment. Configure storage sets first. Before you create a disk in a partition of a storage set, make sure that the storage set exists and has partitions configured. For more information, see the Create a storage set topic in CDS User Guide. |
| Storage Set | Subject to the Creation Method value | Select an existing storage set. This parameter is required if you set the Creation Method parameter to Storage Set Creation. |
| Partition | Subject to the Creation Method value | Specify a partition number. This parameter is required if you set the Creation Method parameter to Storage Set Creation. |

Elastic Compute Service

**Note**

The Quota allowance section displays the disk quota and disk category quota for the region, organization, and resource set that you selected. If remaining quotas are insufficient, click the icon to view and configure quotas.

| System disk | Yes | Configure the system disk on which you want to install the operating system of the ECS instance. Different Elastic Block Storage (EBS) clusters support different disk categories. New EBS clusters that are deployed in Cloud Defined Storage (CDS) support Premium Performance Disk and Standard Performance Disk. EBS clusters in CDS that were created in Apsara Stack V3.15.0 and earlier support Ultra Disk, SSD Disk, Premium Performance Disk, and Standard Performance Disk. Existing EBS clusters continue to provide shared ultra disks and shared SSD disks. The system disk capacity ranges from 20 GiB to 2,048 GiB. Note The actual minimum system disk capacity varies based on the image type. The capacity range that is displayed in the ECS console shall prevail. You can specify a name for the system disk based on your business requirements. If you do not specify a name for the system disk, a name in the <Instance name> SystemDisk _ format is automatically assigned to the system disk. Example: ecstest SystemDisk . _ You can configure Encryption for premium performance disks and standard performance disks. Some instance types support only certain disk categories. For more information, see the Constraints between instance types and disk categories table in the Attach a data disk topic. |
|---|---|---|
| Encryption | No | If you set the System disk parameter to Premium Performance Disk or Standard Performance Disk, the system disk can be encrypted. In scenarios that require data security and regulatory compliance, you can encrypt system disks to protect your data stored on ECS instances. For more information, see Encrypt a system disk. |
|  |  | Add data disks to store instance data. Different EBS clusters support different disk categories. |

Elastic Compute Service

|  | User Guide·Quick start |  |  | Elastic Compute Servic |  | e |
|---|---|---|---|---|---|---|
|  | Data disk | No |  | New EBS clusters that are deployed in CDS support Premium Performance Disk and Standard Performance Disk. EBS clusters in CDS that were created in Apsara Stack V3.15.0 and earlier support Ultra Disk, SSD Disk, Premium Performance Disk, and Standard Performance Disk. Existing EBS clusters continue to provide shared ultra disks and shared SSD disks. You can add up to 16 data disks to an ECS instance. The maximum size of a data disk varies based on the disk category. Ultra Disk, SSD Disk, and Standard Performance Disk: 32,768 GiB. Premium Performance Disk: 131,072 GiB. When you select Ultra Disk or SSD Disk for the Data disk parameter and specify a capacity greater than 2 TiB, you should notice the following recommended maximum disk sizes based on the number of hosts in the EBS cluster (number of hosts: maximum disk size): 6: 2 TiB 12: 4 TiB 15: 5 TiB 24: 8 TiB The formula for calculating the recommended maximum disk size is: Maximum disk size S = N/3, where N is the number of hosts in the EBS cluster. The calculating result is rounded down to the nearest integer. For example, if an EBS cluster has six hosts, we recommend that you set the disk size to no more than 2 TiB. You can specify a name for each data disk based on your business requirements. If you do not specify a name for a data disk, a name in the <Instance name> dataDisk *** format is _ _ automatically assigned to each data disk. Examples: ecstest dataDisk 001 and _ _ ecstest DataDisk 002 . _ _ |  |  |
|  |  |  |  |  | <Instance |  |
|  |  |  |  | name> dataDisk *** _ _ |  |  |

|  | ecstest dataDisk 001 _ _ |
|---|---|
| ecstest DataDisk 002 _ _ |  |

|  |  |  |  | If you specify a name for each data disk, the final names of the data disks that are displayed after the ECS instance is created vary based on the number of data disks. If you set the Quantity parameter to 1 and specify a name for the data disk, the specified name is displayed as the final name of the data disk. Example: testDataDisk . If you set the Quantity parameter to an integer that is greater than or equal to 2 to create multiple data disks of the same category and capacity, and specify a name for each data disk, the final names of the data disks are in the <User-specified data disk name> ** format. For example, if you _ set the Quantity parameter to 2 and enter testDataDisk as the data disk name, the final names of the data disks are testDataDisk 01 and _ testDataDisk 02 . _ You can configure the Release with Instance and Encryption parameters for each data disk. To encrypt a data disk, configure the following parameters: Encryption Method: Select AES256 or SM4. Encryption Key: You can select a key that |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | <User-specified data disk |  |
|  |  |  |  | name> ** _ |  |  |
|  | Encryption | No |  | is created in Key Management Service If you( KseMt Sth).e Data disk parameter to Premium Performance Disk or Standard Performance DisSko,m teh ein dsatatan cdeis tky pcaens sbuep epnocrrty opntleyd c.ertain disk categories. For more information, see the In scenarios that require data security and Constraints between instance types and disk regulatory compliance, you can encrypt data categories table in the Attach a data disk topic. disks to protect your data stored on ECS instances. For more information, see Encrypt a data disNk.ote |  |  |
|  | Release with Instance | No |  | You can attach data disks to an ECS instance after you create the ECS instance. For more If you want to release the disk when the ECS information, see Attach data disks. instance is released, select this option. If you want to retain the disk when the ECS instance is released, clear this option. |  |  |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service The network settings and the security group settings allow the ECS instance to communicate over the Internet and with other resources and safeguard the instance on the network.

| VPC/VSwitch | Yes | A VPC is a dedicated and isolated network that you can use for your business. You have full control over your VPC. For example, you can specify a private CIDR block and configure route tables and gateways for the VPC. Select an existing VPC and vSwitch, or click Create a VPC and Create a VSwitch to create a VPC and a vSwitch. After the VPC and the vSwitch are created, go back to the Create an instance page and click the icon to obtain the latest VPC and vSwitch lists. For more information about how to create a VPC, see the Create and manage a VPC and Create and manage a vSwitch topics in VPC User Guide. Important If you select an SCC instance type and specify an SCC that has a VPC ID, the VPC ID of the SCC is automatically populated in the field and cannot be changed. For more information, see Add nodes to an SCC. |
|---|---|---|
| Private IP | No | Specify a private IPv4 address for the ECS instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you select Random assignment for the Private IP parameter, the system automatically allocates a private IP address to the instance. |
| Public IP | No | To allow the instance to access the Internet, you must assign a public IP address to the instance. You can select Assign public IPv4 address when you create an instance to have a public IP address automatically assigned to the instance. Alternatively, you can associate an elastic IP address (EIP) with the ECS instance after you create the instance. For more information, see the Create and manage an EIP topic in VPC User Guide. |
| Bandwidth value (Mbit/s) | No | This parameter is required if you select Assign public IPv4 address. Valid values: 1 to 100. |

Elastic Compute Service

| Security Group | Yes | Select an existing security group or click Create a security group to create a security group. After the security group is created, go back to the Create an instance page and click the icon to obtain the latest security group list. For information about how to create a security group, see Create a security group. You can select multiple security groups for an ECS instance at a time. Important If you select an SCC instance type and specify an SCC that has a security group ID, the security group ID of the SCC is automatically populated in the field and cannot be changed. For more information, see Add nodes to an SCC. |
|---|---|---|
| IPv6 | No | After you enable IPv6, the public IPv4 address depletion issue is resolved and a variety of devices can access the Internet. After you select Allocation for the IPv6 parameter and create the instance, you must log in to the instance and configure an IPv6 address in the operating system to use the IPv6 address. |
| Elastic Network Card | No | Select the elastic network interface (ENI) with which you want to associate the ECS instance. Select an existing ENI or click Create an ENI to create an ENI. After the ENI is created, go back to the Create an instance page and click the icon to obtain the latest ENI list. Note You can bind only one secondary ENI when you create an instance. Alternatively, you can create secondary ENIs and bind them to an instance after the instance is created. |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service

**Manage Configuration**

| Login voucher | Settings after creation | After the ECS instance is created, bind a key pair to the instance or use the Reset Password feature to set a password for the instance. |
|---|---|---|
|  | Key Pair | Select an existing key pair or click Create a key pair to create a key pair. After the key pair is created, go back to the Create an instance page and click the icon to obtain the latest key pairs. For more information, see Create a key pair. Important Key pairs can be used to log in to only Linux ECS instances. Set the Username parameter to root or ecs- user. ecs-user is available for selection only if you select a public image that supports logins of the ecs-user user and turn on Support ecs-user user login. Otherwise, only root is available. Warning If you log in to an ECS instance as the root user, you have the highest permissions on the instance. However, security risks may arise. We recommend that you log in to the ECS instance as the ecs-user user. |
|  |  | Enter and confirm a password. Then, configure the Login Username parameter. For a Linux ECS instance, you can set the Login Username parameter to root or ecs-user. ecs-user is available for selection only if you select a public image that supports logins of the ecs-user user and turn on Support ecs- user user login. Otherwise, only root is available. Warning If you log in to an ECS instance as the root user, you have the highest permissions on the instance. However, security risks may arise. We recommend that you log in to the ECS instance as the ecs-user user. For a Windows ECS instance, the Login Username parameter is automatically set to administrator. |

Elastic Compute Service

|  |  |  | Custom Password |  |  | The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? _ / . For Windows ECS instances, the password cannot start with a forward slash (/). Important If an instance runs the Kylin operating system, the following limits apply to the |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | ( ) ` ~ ! @ # $ % |  |  |
|  |  |  |  | tom Password |  | ^ & * - + = \| { } [ ] : ; ' < > , . ? _ |  |  |  |  |  |
|  |  |  |  |  |  | / |  |  |  |  |  |
|  |  |  |  |  |  |  | Important If an instance runs the Kylin operating system, the following limits apply to the |  |  |  |  |
|  |  |  |  |  |  |  | password: For an instance that is created from a Kylin image, the password must be at least eight characters in length and contain at least three of the following types of characters: uppercase letters, lowercase letters, digits, and special characters. Do not use palindrome passwords, simple or commonly used passwords, or passwords that are too similar to the original password. The password cannot contain the username or any words that are included in the cracklib dictionary. You can run the echo "YOUR PASSWORD" \| cracklib-check _ command to check whether the password meets this requirement. Supported special characters include: ( ) ` ~ ! @ # $ % ^ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | echo |  |
|  |  |  |  |  |  |  | "YOUR PASSWORD" \| cracklib-check _ |  |  |  |  |
|  |  |  |  |  |  |  |  | ( ) ` ~ ! @ # $ % ^ |  |  |  |
|  |  |  |  |  |  |  | & * - + = \| { } [ ] : ; ' < > , . ? _ |  |  |  |  |
|  |  |  |  |  |  |  | / |  |  |  |  |
|  |  |  | Keep the original mirror password |  |  | Retain the login password that is set on the selected image. After the ECS instance is created, you can use the login username and password of the image that is used by the instance to connect to the instance. Important The Keep the original mirror password parameter is available for selection only if you set the Image Type parameter to Custom Image, Shared Image, or Enterprise Public Image and select an image on which a login password is set. |  |  |  |  |  |
|  |  | Number of units created | Yes |  |  | You can create up to 100 instances at a time. The number of ECS instances cannot exceed the quota. The quota is displayed on the homepage of the Apsara Uni-manager Management Console. |  |  |  |  |  |

Elastic Compute Service

| Instance name |  | Yes | Enter a name for the instance. The name must be 2 to 110 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), _ periods (.), and hyphens (-). When you create multiple instances, the instance names are automatically suffixed with incremental three-digit numbers in order. By default, the incremental suffixes range from 001 to 100. Examples: LocalHost001, LocalHost002, MyInstance001, and MyInstance002. When you create multiple instances at a time, you can configure sequential names for the instances. For example, you can specify the names of ECS instances in the name prefix[begin number,bits]name suffix _ _ _ format. For example, you can specify my name[99,3]ecs . If you create two _ instances, the names of the instances are my name099ecs and my name100ecs . The _ _ valid values of begin number are 0 to 999999, _ and the valid values of bits are 1 to 6. Default value: 6. |  |  |
|---|---|---|---|---|---|
|  |  |  |  | name prefix[begin number,bits]name suffix _ _ _ |  |
| Example Description |  | No | Enter a description for the ECS instance. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . The description can contain letters, digits, periods (.), underscores ( ), and hyphens (- _ ). |  |  |

Elastic Compute Service

| Host name |  | No | Enter the hostname that you want to display in the operating system. Take note of the following items about the hostname: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For a Windows ECS instance, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). For a Linux ECS instance, you can specify the hostname based on the following rules: The hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). You can use the ${instance id} _ placeholder to pass instance IDs into the hostname. For example, if you set the Host name parameter to k8s-${instance id} _ and the instance is assigned an ID of i- 123abc**** , the hostname of the instance is k8s-i-123abc**** . When you create multiple instances at a time, you can configure sequential hostnames for the instances. For example, you can specify the hostnames of ECS instances in the name prefix[begin number,bits]name suffix _ _ _ format. For example, you can specify my name[99,3]ecs . If you create two _ instances, the names of the instances are my name099ecs and my name100ecs . The _ _ valid values of begin number are 0 to 999999, _ and the valid values of bits are 1 to 6. Default value: 6. |  |  |
|---|---|---|---|---|---|
|  |  |  |  | name prefix[begin number,bits]name suffix _ _ _ |  |
| Instance Release Protection |  | No | You can enable the instance release protection feature to prevent instances from being manually released, which can effectively minimize loss caused by accidental operations or the lack of timely communication among team members. |  |  |
| Label |  | No | Select an existing tag, or enter a key and a value to create a tag. Each tag consists of a tag key and a tag value. You can add tags to resources that have identical characteristics, such as resources that belong to the same organization and resources that serve the same purpose. You can use tags to search for and manage resources in an efficient manner. You can specify up to 20 tags. |  |  |

Elastic Compute Service

| Deployment Sets Important This parameter is not displayed if you select an SCC instance type to create ECS instances. | No | Select an existing deployment set or click Create a deployment set to create a deployment set. After the deployment set is created, go back to the Create an instance page and click the icon to obtain the latest deployment set list. For more information about how to create a deployment set, see Create a deployment set. A deployment set is a policy that controls the distribution of ECS instances. You can use deployment sets to design disaster recovery and service availability solutions when you create ECS instances. You can use deployment sets to disperse or aggregate ECS instances. |
|---|---|---|
| Custom Data Format | No | Specifies whether to enable custom data format. Custom instance data can be run as scripts when the instance starts to automate instance configurations, or can be passed into instances as common data. For more information, see Instance user data. Enter your user data in the field. If the user data is already encoded in Base64, turn on Input is Base64 encoded. |
| Custom Data | No |  |

Elastic Compute Service

**Verify the result**

The new instance that you create appears on the ECS Instances page. When the instance is being created, it is in the **Preparing** state. After the instance is created, it enters the
**Running** state.

**What to do next**

If you add data disks when you create the ECS instance, you must partition and format the data disks before you can use the disks. For more information, see Format a data disk for a Linux instance and Format a data disk on a Windows ECS instance.

### Connect to an instance

#### Overview

After an instance is created, you can connect to the instance to perform operations, such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that use public IP addresses. For more information, see the following topics:

#### Connect to a Linux instance by using SSH commands in Linux or Mac OS X

#### Connect to a Linux instance by using a remote connection tool in Windows

#### Connect to a Windows instance from a Windows computer by using Remote Desktop

Use the VNC feature in the Elastic Computer Service (ECS) console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator.The username of a Linux instance is root.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

Elastic Compute Service

#### Connect to a Linux instance by using

**SSH commands in Linux or Mac OS X**

This topic describes how to use SSH commands to connect to a Linux instance.

**Prerequisites**

The instance and the security group are created. The instance is in the **Running** state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

**Procedure**

1. Enter the following command and press the Enter key:

```
ssh root@<EIP of the instance>
```

2. Enter the instance password of the root user and press the Enter key.

#### Connect to a Linux instance by using a

**remote connection tool in Windows**

This topic describes how to connect to a Linux instance by using the PuTTY tool.

**Prerequisites**

Connection tools are used in a similar way. In this example, PuTTY is used to connect to a Linux instance. To download PuTTY, go to the Putty official website.

**Procedure**

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

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

Elastic Compute Service
4. Enter **root** as the username and press the
`Enter` key.
5. Enter the password of the instance and press the
`Enter` key. The following message indicates that you are connected to the instance.

```
Welcome to aliyun Elastic Compute Server!
```

#### Connect to a Windows instance from a

**Windows computer by using Remote Desktop**

This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC).

**Prerequisites**

A Windows instance is created and added to a security group. The instance is in the **Running** state. A logon password is set for the instance. An elastic IP address (EIP) is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

**Procedure**

1. Use one of the following methods to enable RDC:

**Note**

In this topic, an on-premises computer that runs Windows 10 is used. Operations may vary based on your operating system. On the taskbar of the Windows desktop, enter `mstsc` in the search box. Then, click
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

If the Windows desktop appears, a connection to the Windows instance is established.

| Issue | Solution |
|---|---|
| The instance starts slowly due to self-check on startup. | Check the self-check progress. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear and consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

Elastic Compute Service If an error message is returned indicating that an authentication error occurs and the function requested is not supported, install CredSSP updates and try again. Follow the following steps to install the updates:
1. Connect to the instance by using Virtual Network Computing (VNC). For more information,
see Connect to an instance by using a VNC management terminal.
2. Choose **Start > Control Panel**.
3. Click **System and Security**.
4. Click **Check for updates** in the **Windows Updates** section.
5. If updates are available, click **Install updates**.
6. Restart the instance.

#### Connect to an instance by using a VNC

**management terminal**

If other remote connection tools such as PuTTy, Xshell, and SecureCRT are not installed or do not work properly, you can access your instances by using a VNC management terminal in the ECS console.

**Prerequisites**

The instance to which you want to connect is in the **Running** state. The root certificate is imported to your web browser. For more information, see Install the certificate for VNC in Windows. The VNC password is reset if it is your first time to connect to the instance after the instance is created. For more information, see Change the VNC password.

**Background information**

The VNC password is used to log on to a VNC management terminal in the ECS console, whereas the instance password is used to log on to the instance. You can use a VNC management terminal to connect to an instance to solve specific issues. The following table lists some of the issues.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to connect and click **Remote Connection** in the
**Actions** column.
5. Enter the VNC password and click **OK**.
After you are logged on to the VNC management terminal, a logon page similar to the Elastic Compute Service following one appears.
6. Enter your username and password.
For a Linux instance, enter the username `root` and the logon password.

**Note**

When you log on to the Linux instance, the password is not displayed when you enter it. Press the Enter key after you enter the password. For a Windows instance, to use a keyboard shortcut such as Ctrl+Alt+Delete, click the List icon in the upper-left corner of the page and select the keyboard shortcut from the drop-down list. Enter the username and password as prompted. Then, click the Log On icon, such as . Elastic Compute Service

## Instances

### Overview

An Elastic Compute Service (ECS) instance is a virtual server that includes basic components such as CPUs, memory, an operating system (OS), network configurations, and disks. You can use management tools provided by Alibaba Cloud such as the ECS console and ECS API to create and manage ECS instances. You can manage the status of ECS instances and their deployed applications in the same manner as you would do with local servers. You can also upgrade the capabilities (such as compute and storage capabilities) of your ECS instances as your requirements increase.

**Basic instance configurations**

The following basic configurations of ECS instances determine the basic resources that the instances require: Instance types Instance types define the basic attributes of ECS instances, such as compute capacity, storage capacity, and networking capacity. Instance types must be used together with images, Elastic Block Storage (EBS) devices, and network resources to create ECS instances that serve different purposes. ECS provides a variety of instance families for typical use scenarios. Each instance family consists of multiple instance types that have different compute capabilities and are suited to different scenarios and requirements. For more information, see **Instance families and**
**instance types** in the ECS documentation.
Images contain the information necessary to run ECS instances, such as OSs and initialization data of applications. Alibaba Cloud provides ready-to-use images for Windows Server and several mainstream Linux OSs. You can also create or import your own images to save time in making repeated configurations. ECS instances use their attached system disks and data disks for storage. Each instance must have a system disk attached. The first time the instance starts, the OS is installed and instance configurations are initialized based on the system disk image. Cloud disks can be used as system disks or data disks. Local disks can be used only as data disks and are available only for specific instance types, such as instance types with local HDDs. If you want your instances to have more storage space, you can resize their attached cloud disks or attach more cloud disks after the instances are created. For more information, see Create a disk and Attach data disks. Business data is an important asset. Cloud disks use a triplicate mechanism to ensure the durability of data. To ensure that your data remains available, we recommend that you back up your data on a regular basis. You can create snapshots of cloud disks to back up disk data. If you are using local disks, you must implement data redundancy at the application layer to ensure data availability. In addition to basic configurations, you can also configure network configurations, security groups, and OSs for instances. For more information, see Create an instance. When you use Apsara Stack services, we recommend that you follow security suggestions to improve resource security, such as the following ones: Suggestions for permission control: Use the Enterprise Permissions features to control which users can manage resources such as instances and what permissions to grant to the Elastic Compute Service users. Suggestions for security features: Use security features such as security hardening and cloud disk encryption to ensure the security of data and runtime environments. Suggestions for network security: Use virtual private clouds (VPCs) to isolate services of different security levels. Use security groups to control inbound and outbound traffic for instances and allow instances access to the Internet only when required to minimize the attack surface area of resources.

### Create an instance

An Elastic Compute Service (ECS) instance is a virtual machine that consists of basic components, such as the CPU, memory, operating system, network settings, and disks. This topic describes how to create one or more ECS instances.

**Procedure**

**Important**

For information about the limits that apply when you create ECS instances, see Limits.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the page that appears, click **Create Instance**.
5. (Optional) Select a service catalog and click **OK**.
The service management feature is used to manage and control specific specifications of specific services within an enterprise or an organization. This parameter is displayed only after you create and publish services that grant the current organization or user permissions to access ECS instances. For more information about service catalog management, see the **Manage service catalogs** topic in **Apsara Uni-manager**
**Operations Console User Guide**.
6. Configure the region, type, image, and storage of the instance.
7. Before you click Create Order, check the instance configurations in the **Configuration**
**overview** section and configure parameters such as Duration on the right side of the ECS
instance buy page. Make sure that all configurations meet your business requirements. In the **Configuration overview** section on the right side of the page, click **Save as a**
**configuration template** to save the required configurations, such as instance type,
operating system, network settings, security rules, and storage configurations, as a configuration template. You can use a specific configuration template to quickly create ECS instances later without the need to configure all parameters.
8. Create the ECS instance.
If a service whose **Resources** value is **ECS** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Confirm Order**. If no service whose **Resources** value is **ECS** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Submit**.

**Parameters and descriptions**

| Parameter | Required | Description |
|---|---|---|
| Organization/Reso urce Set | Yes | Select the organization and resource set to which the instance belongs. |
| Geography/Availa bility Zone | Yes | Select the region and zone to which the instance belongs. Zones are physical locations in a region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create ECS instances in different zones. |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service

**Billing Configuration**

**Note**

This parameter is available only if the administrator has configured billing rules in the operations center. For more information about the billing rules, see the **Create a billing**
**configuration** topic in **Apsara Uni-manager Operations Console User Guide** .
The **Pay-as-you-go** and **Subscription** billing methods are supported.
**Pay-as-you-go**: You can use the service first. Fees are charged afterward based on the
actual amount of resources that you used. This method is suitable for scenarios in which business usage frequently fluctuates, which allows users to flexibly utilize resources based on actual needs and avoid waste.
**Subscription**: You can directly subscribe to resources for a fixed period of time, and fees
are charged based on the quantity and duration. No additional fees are incurred during subsequent usage. This method is suitable for scenarios where business usage is relatively stable.

**Regional Information**

Instance types offer varying combinations of compute, memory, and storage capacities to fit different use cases. Instance types must be used together with images, block storage devices, and network resources to create ECS instances that serve different purposes.

**Note**

The Quota allowance section displays the CPU, GPU, and memory quotas for the region, organization, and resource set that you selected. If remaining quotas are insufficient, click the icon to view and configure quotas.

| Open the thermal transformer | No | Specifies whether to enable hot configuration change for the instance. If you set this parameter to Yes, you can change the instance type without the need to stop the instance. For more information, see Perform a hot configuration change on an instance to change the instance type. If instance types that support hot configuration changes are available, this parameter is set to Yes by default. In this case, the instance type list displays only the instance types that support hot configuration changes. Note If you do not want to select an instance type that supports hot configuration changes, set this parameter to No. All available instance types are displayed. If no instance types that support hot configuration changes are available, this parameter is set to No by default. In this case, the instance type list displays all available instance types. |
|---|---|---|
| Filter | No | The condition based on which instance types are filtered. You can select CPU, memory, or GPU as the filter condition, or enter a keyword to search for instance types. |
| CPU Type | Yes | Select a CPU type. Valid values: Intel/X86 Hygon/X86 Kunpeng/ARM Phytium/ARM Yitian/ARM Zhaoxin/X86 Others Note The supported CPU types are displayed on the Create an instance page in the ECS console. |

Elastic Compute Service

| Category | Yes | Select an instance category. Valid values: Dedicated Shared Local SSD Local HDD Super Computing Cluster ECS Bare Metal Instance Others Note The actual instance types that are supported are displayed on the Create an instance page in the ECS console. |
|---|---|---|

Elastic Compute Service

| Specifications | Yes | The instance type. Instance types are displayed in a list that consists of the Instance Family, Instance Type, Instance Family Level, Status, CPU Type, CPU Cores, Memory, GPU Specifications, GPUs, Internal Bandwidth, and Number of Disks columns. Select an instance type based on your business requirements. For information about instance families and instance types, see the Instance types topic in the Apsara Stack documentation. Important Available, Sold Out, or Disabled can be displayed in the Status column of an instance type. You can select only instance types in the Available state. If you select a service catalog when you create an instance, the available instance types are limited by the service catalog. For more information, see the Example: Create an ECS instance service topic in Apsara Uni- manager Management Console User Guide. Instance types that have specific vCPU and memory combinations do not support Windows Server images. For more information, see Limits. Important To create a GPU-accelerated instance, you need to install a GPU driver on the instance based on the operating system of the instance. Except that you must install GPU drivers on GPU- accelerated instances, you can manage GPU- accelerated instances in the same manner as you manage non-GPU-accelerated instances. For information about how to install GPU drivers on NVIDIA GPU-accelerated instances, see Installation guideline for NVIDIA drivers. For information about how to install GPU drivers on instances that are equipped with GPUs from other manufacturers, see the official documents of the manufacturers. To create an ECS instance of a Super Computing Cluster (SCC) instance category, you must set the Super Computing Cluster parameter instead of the Deployment Set parameter. The VPC and Security Group parameters may be affected by the virtual private cloud (VPC) ID and security group ID of the SCC. For more information about SCCs, see Overview of SCCs. |
|---|---|---|

Elastic Compute Service

| Super Computing Cluster | Subject to the Category value and the selected instance type | The ID of the SCC to which the instance belongs. You can select an existing SCC or click Create Cluster to create an SCC. After the SCC is created, go back to the Create an instance page and click the icon to obtain the latest SCC list. For more information about how to create an SCC, see Create an SCC. This parameter is available and can be configured only if you set the Category parameter to Super Computing Cluster and select an SCC instance type. This parameter is required when you create an instance of an SCC instance type. |
|---|---|---|
| Instances | Subject to the Super Computing Cluster value | The number of nodes (ECS instances) in the SCC. This parameter is automatically configured and cannot be modified after you configure the Super Computing Cluster parameter. |
| HT Hyper- Threading Technology | No | Specifies whether to enable hyper-threading for the instance. Only specific instance types support the HT Hyper- Threading Technology parameter. You can configure the HT Hyper-Threading Technology parameter after you click Show Advanced options. For more information about HT Hyper-Threading Technology, see Disable HT. If you turn on HT Hyper-Threading Technology, two logical processing cores are created for each physical core of the ECS instance. If you turn off HT Hyper-Threading Technology, the ECS instance exclusively uses CPU physical cores. |
| CPU Topology | No | You can select HT Continuous CPU Topology or HT Discrete CPU Topology. You can modify the CPU topology only for specific instance types. You can modify the CPU Topology parameter after you click Show Advanced options. For more information about CPU topologies, see View and modify CPU topologies. HT continuous CPU topology: Logical cores are continuously assigned to physical cores, which can help reduce communication and contention between threads. This mode is suitable for computing tasks that require low memory access latency and computing power close to computing power provided by the physical cores, such as scientific computing, data analysis, and high-performance computing, which are sensitive to memory access and core computing. HT discrete CPU topology: Logical cores are discretely distributed to physical cores, which can help reduce resource contention in a multi-threaded environment and provide better performance isolation. This mode is suitable for the tasks that are separately assigned to threads or the tasks that require high single-thread performance. |

Elastic Compute Service

**Image ID**

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image, Custom Image, Shared Image, and Enterprise Public Image. Note For more information, see Overview. |
| Public Image | Subject to the Image Type value | Select a public image. Public images that are provided by Alibaba Cloud without operating system licenses deliver high security and stability. Public images for Windows Server operating systems and mainstream Linux operating systems are provided. This parameter is required if you set the Image Type parameter to Public Image. |
| Support ecs-user user login | Subject to the Public Image value | This parameter is available only if you select a public image that supports logins of the ecs-user user to create a Linux ECS instance. If you turn on Support ecs-user user login, ecs- user is used as the username to log in to the Linux ECS instance. If you turn off Support ecs-user user login, root is used as the username to log in to the Linux ECS instance. Warning If you log in to an ECS instance as the root user, you have the highest permissions on the instance. However, security risks may arise. We recommend that you log in to the ECS instance as the ecs-user user. The following public images support ecs-user: x86: Alibaba Cloud Linux 2: aliyun 2 1903 x86 64 20G alibase 2024 _ _ _ _ _ _ _ 0628.vhd aliyun 2 1903 x86 64 20G dengbao alib _ _ _ _ _ _ _ ase 20240705.vhd _ |

Elastic Compute Service Images contain information required to run instances. Alibaba Cloud provides a variety of image sources for easy access to images. The following table describes the image sources.

|  |  | Alibaba Cloud Linux 3: aliyun 3 x86 64 20G alibase 20241103.v _ _ _ _ _ _ hd aliyun 3 x86 64 20G container optimize _ _ _ _ _ _ d 20241226.vhd _ aliyun 3 x86 64 20G dengbao alibase 2 _ _ _ _ _ _ _ 0241103.vhd aliyun 3 x86 64 20G pro alibase 202412 _ _ _ _ _ _ _ 25.vhd aliyun 3 x86 64 20G pro dengbao alibas _ _ _ _ _ _ _ e 20241030.vhd _ aliyun 4 x86 64 20G alibase 20250728.v _ _ _ _ _ _ hd UOS: uos 20 1070a x86 64 20G alibase 2024 _ _ _ _ _ _ _ 1129.vhd Arm: |
|---|---|---|
|  |  | UOS uos 20 1070a arm64 20G uefi alibase 2 _ _ _ _ _ _ _ 0241119.vhd Alibaba Cloud Linux: aliyun 3 arm64 20G uefi dengbao alibas _ _ _ _ _ _ e 20241103.vhd _ |
| Custom Image | Subject to the Image Type value | Select a custom image. Custom images are created from ECS instances or snapshots or imported from your computer. This parameter is required if you set the Image Type parameter to Custom Image. |
| Shared Image | Subject to the Image Type value | Select a shared image. Shared images are custom images that are shared by other level-1 organizations to your organization. This parameter is required if you set the Image Type parameter to Shared Image. |
| Enterprise Public Image | Subject to the Image Type value | Select an enterprise public image. Enterprise public images are images that are shared by an administrator in the Apsara Uni-manager Operations Console. This parameter is required if you set the Image Type parameter to Enterprise Public Image. |

Elastic Compute Service System disks and data disks are attached to instances to provide storage capacity. System disks are used to install operating systems, while data disks are used to store application data.

| Parameter | Required | Description |
|---|---|---|
| Creation Method | Yes | Select the method that you want to use to create a disk. Valid values: Normal Creation and Storage Set Creation. To create a disk in a partition of a specific storage set, select Storage Set Creation. Important If only Normal Creation is displayed, storage sets are not supported in the current environment. Configure storage sets first. Before you create a disk in a partition of a storage set, make sure that the storage set exists and has partitions configured. For more information, see the Create a storage set topic in CDS User Guide. |
| Storage Set | Subject to the Creation Method value | Select an existing storage set. This parameter is required if you set the Creation Method parameter to Storage Set Creation. |
| Partition | Subject to the Creation Method value | Specify a partition number. This parameter is required if you set the Creation Method parameter to Storage Set Creation. |

Elastic Compute Service

**Note**

The Quota allowance section displays the disk quota and disk category quota for the region, organization, and resource set that you selected. If remaining quotas are insufficient, click the icon to view and configure quotas.

| System disk | Yes | Configure the system disk on which you want to install the operating system of the ECS instance. Different Elastic Block Storage (EBS) clusters support different disk categories. New EBS clusters that are deployed in Cloud Defined Storage (CDS) support Premium Performance Disk and Standard Performance Disk. EBS clusters in CDS that were created in Apsara Stack V3.15.0 and earlier support Ultra Disk, SSD Disk, Premium Performance Disk, and Standard Performance Disk. Existing EBS clusters continue to provide shared ultra disks and shared SSD disks. The system disk capacity ranges from 20 GiB to 2,048 GiB. Note The actual minimum system disk capacity varies based on the image type. The capacity range that is displayed in the ECS console shall prevail. You can specify a name for the system disk based on your business requirements. If you do not specify a name for the system disk, a name in the <Instance name> SystemDisk _ format is automatically assigned to the system disk. Example: ecstest SystemDisk . _ You can configure Encryption for premium performance disks and standard performance disks. Some instance types support only certain disk categories. For more information, see the Constraints between instance types and disk categories table in the Attach a data disk topic. |
|---|---|---|
| Encryption | No | If you set the System disk parameter to Premium Performance Disk or Standard Performance Disk, the system disk can be encrypted. In scenarios that require data security and regulatory compliance, you can encrypt system disks to protect your data stored on ECS instances. For more information, see Encrypt a system disk. |
|  |  | Add data disks to store instance data. Different EBS clusters support different disk categories. |

Elastic Compute Service

|  | User Guide·Instances |  |  | Elastic Compute Servic |  | e |
|---|---|---|---|---|---|---|
|  | Data disk | No |  | New EBS clusters that are deployed in CDS support Premium Performance Disk and Standard Performance Disk. EBS clusters in CDS that were created in Apsara Stack V3.15.0 and earlier support Ultra Disk, SSD Disk, Premium Performance Disk, and Standard Performance Disk. Existing EBS clusters continue to provide shared ultra disks and shared SSD disks. You can add up to 16 data disks to an ECS instance. The maximum size of a data disk varies based on the disk category. Ultra Disk, SSD Disk, and Standard Performance Disk: 32,768 GiB. Premium Performance Disk: 131,072 GiB. When you select Ultra Disk or SSD Disk for the Data disk parameter and specify a capacity greater than 2 TiB, you should notice the following recommended maximum disk sizes based on the number of hosts in the EBS cluster (number of hosts: maximum disk size): 6: 2 TiB 12: 4 TiB 15: 5 TiB 24: 8 TiB The formula for calculating the recommended maximum disk size is: Maximum disk size S = N/3, where N is the number of hosts in the EBS cluster. The calculating result is rounded down to the nearest integer. For example, if an EBS cluster has six hosts, we recommend that you set the disk size to no more than 2 TiB. You can specify a name for each data disk based on your business requirements. If you do not specify a name for a data disk, a name in the <Instance name> dataDisk *** format is _ _ automatically assigned to each data disk. Examples: ecstest dataDisk 001 and _ _ ecstest DataDisk 002 . _ _ |  |  |
|  |  |  |  |  | <Instance |  |
|  |  |  |  | name> dataDisk *** _ _ |  |  |

|  | ecstest dataDisk 001 _ _ |
|---|---|
| ecstest DataDisk 002 _ _ |  |

|  |  |  |  | If you specify a name for each data disk, the final names of the data disks that are displayed after the ECS instance is created vary based on the number of data disks. If you set the Quantity parameter to 1 and specify a name for the data disk, the specified name is displayed as the final name of the data disk. Example: testDataDisk . If you set the Quantity parameter to an integer that is greater than or equal to 2 to create multiple data disks of the same category and capacity, and specify a name for each data disk, the final names of the data disks are in the <User-specified data disk name> ** format. For example, if you _ set the Quantity parameter to 2 and enter testDataDisk as the data disk name, the final names of the data disks are testDataDisk 01 and _ testDataDisk 02 . _ You can configure the Release with Instance and Encryption parameters for each data disk. To encrypt a data disk, configure the following parameters: Encryption Method: Select AES256 or SM4. Encryption Key: You can select a key that |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | <User-specified data disk |  |
|  |  |  |  | name> ** _ |  |  |
|  | Encryption | No |  | is created in Key Management Service If you( KseMt Sth).e Data disk parameter to Premium Performance Disk or Standard Performance DisSko,m teh ein dsatatan cdeis tky pcaens sbuep epnocrrty opntleyd c.ertain disk categories. For more information, see the In scenarios that require data security and Constraints between instance types and disk regulatory compliance, you can encrypt data categories table in the Attach a data disk topic. disks to protect your data stored on ECS instances. For more information, see Encrypt a data disNk.ote |  |  |
|  | Release with Instance | No |  | You can attach data disks to an ECS instance after you create the ECS instance. For more If you want to release the disk when the ECS information, see Attach data disks. instance is released, select this option. If you want to retain the disk when the ECS instance is released, clear this option. |  |  |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service The network settings and the security group settings allow the ECS instance to communicate over the Internet and with other resources and safeguard the instance on the network.

| VPC/VSwitch | Yes | A VPC is a dedicated and isolated network that you can use for your business. You have full control over your VPC. For example, you can specify a private CIDR block and configure route tables and gateways for the VPC. Select an existing VPC and vSwitch, or click Create a VPC and Create a VSwitch to create a VPC and a vSwitch. After the VPC and the vSwitch are created, go back to the Create an instance page and click the icon to obtain the latest VPC and vSwitch lists. For more information about how to create a VPC, see the Create and manage a VPC and Create and manage a vSwitch topics in VPC User Guide. Important If you select an SCC instance type and specify an SCC that has a VPC ID, the VPC ID of the SCC is automatically populated in the field and cannot be changed. For more information, see Add nodes to an SCC. |
|---|---|---|
| Private IP | No | Specify a private IPv4 address for the ECS instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you select Random assignment for the Private IP parameter, the system automatically allocates a private IP address to the instance. |
| Public IP | No | To allow the instance to access the Internet, you must assign a public IP address to the instance. You can select Assign public IPv4 address when you create an instance to have a public IP address automatically assigned to the instance. Alternatively, you can associate an elastic IP address (EIP) with the ECS instance after you create the instance. For more information, see the Create and manage an EIP topic in VPC User Guide. |
| Bandwidth value (Mbit/s) | No | This parameter is required if you select Assign public IPv4 address. Valid values: 1 to 100. |

Elastic Compute Service

| Security Group | Yes | Select an existing security group or click Create a security group to create a security group. After the security group is created, go back to the Create an instance page and click the icon to obtain the latest security group list. For information about how to create a security group, see Create a security group. You can select multiple security groups for an ECS instance at a time. Important If you select an SCC instance type and specify an SCC that has a security group ID, the security group ID of the SCC is automatically populated in the field and cannot be changed. For more information, see Add nodes to an SCC. |
|---|---|---|
| IPv6 | No | After you enable IPv6, the public IPv4 address depletion issue is resolved and a variety of devices can access the Internet. After you select Allocation for the IPv6 parameter and create the instance, you must log in to the instance and configure an IPv6 address in the operating system to use the IPv6 address. |
| Elastic Network Card | No | Select the elastic network interface (ENI) with which you want to associate the ECS instance. Select an existing ENI or click Create an ENI to create an ENI. After the ENI is created, go back to the Create an instance page and click the icon to obtain the latest ENI list. Note You can bind only one secondary ENI when you create an instance. Alternatively, you can create secondary ENIs and bind them to an instance after the instance is created. |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service

**Manage Configuration**

| Login voucher | Settings after creation | After the ECS instance is created, bind a key pair to the instance or use the Reset Password feature to set a password for the instance. |
|---|---|---|
|  | Key Pair | Select an existing key pair or click Create a key pair to create a key pair. After the key pair is created, go back to the Create an instance page and click the icon to obtain the latest key pairs. For more information, see Create a key pair. Important Key pairs can be used to log in to only Linux ECS instances. Set the Username parameter to root or ecs- user. ecs-user is available for selection only if you select a public image that supports logins of the ecs-user user and turn on Support ecs-user user login. Otherwise, only root is available. Warning If you log in to an ECS instance as the root user, you have the highest permissions on the instance. However, security risks may arise. We recommend that you log in to the ECS instance as the ecs-user user. |
|  |  | Enter and confirm a password. Then, configure the Login Username parameter. For a Linux ECS instance, you can set the Login Username parameter to root or ecs-user. ecs-user is available for selection only if you select a public image that supports logins of the ecs-user user and turn on Support ecs- user user login. Otherwise, only root is available. Warning If you log in to an ECS instance as the root user, you have the highest permissions on the instance. However, security risks may arise. We recommend that you log in to the ECS instance as the ecs-user user. For a Windows ECS instance, the Login Username parameter is automatically set to administrator. |

Elastic Compute Service

|  |  |  | Custom Password |  |  | The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? _ / . For Windows ECS instances, the password cannot start with a forward slash (/). Important If an instance runs the Kylin operating system, the following limits apply to the |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | ( ) ` ~ ! @ # $ % |  |  |
|  |  |  |  | tom Password |  | ^ & * - + = \| { } [ ] : ; ' < > , . ? _ |  |  |  |  |  |
|  |  |  |  |  |  | / |  |  |  |  |  |
|  |  |  |  |  |  |  | Important If an instance runs the Kylin operating system, the following limits apply to the |  |  |  |  |
|  |  |  |  |  |  |  | password: For an instance that is created from a Kylin image, the password must be at least eight characters in length and contain at least three of the following types of characters: uppercase letters, lowercase letters, digits, and special characters. Do not use palindrome passwords, simple or commonly used passwords, or passwords that are too similar to the original password. The password cannot contain the username or any words that are included in the cracklib dictionary. You can run the echo "YOUR PASSWORD" \| cracklib-check _ command to check whether the password meets this requirement. Supported special characters include: ( ) ` ~ ! @ # $ % ^ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | echo |  |
|  |  |  |  |  |  |  | "YOUR PASSWORD" \| cracklib-check _ |  |  |  |  |
|  |  |  |  |  |  |  |  | ( ) ` ~ ! @ # $ % ^ |  |  |  |
|  |  |  |  |  |  |  | & * - + = \| { } [ ] : ; ' < > , . ? _ |  |  |  |  |
|  |  |  |  |  |  |  | / |  |  |  |  |
|  |  |  | Keep the original mirror password |  |  | Retain the login password that is set on the selected image. After the ECS instance is created, you can use the login username and password of the image that is used by the instance to connect to the instance. Important The Keep the original mirror password parameter is available for selection only if you set the Image Type parameter to Custom Image, Shared Image, or Enterprise Public Image and select an image on which a login password is set. |  |  |  |  |  |
|  |  | Number of units created | Yes |  |  | You can create up to 100 instances at a time. The number of ECS instances cannot exceed the quota. The quota is displayed on the homepage of the Apsara Uni-manager Management Console. |  |  |  |  |  |

Elastic Compute Service

| Instance name |  | Yes | Enter a name for the instance. The name must be 2 to 110 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), _ periods (.), and hyphens (-). When you create multiple instances, the instance names are automatically suffixed with incremental three-digit numbers in order. By default, the incremental suffixes range from 001 to 100. Examples: LocalHost001, LocalHost002, MyInstance001, and MyInstance002. When you create multiple instances at a time, you can configure sequential names for the instances. For example, you can specify the names of ECS instances in the name prefix[begin number,bits]name suffix _ _ _ format. For example, you can specify my name[99,3]ecs . If you create two _ instances, the names of the instances are my name099ecs and my name100ecs . The _ _ valid values of begin number are 0 to 999999, _ and the valid values of bits are 1 to 6. Default value: 6. |  |  |
|---|---|---|---|---|---|
|  |  |  |  | name prefix[begin number,bits]name suffix _ _ _ |  |
| Example Description |  | No | Enter a description for the ECS instance. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . The description can contain letters, digits, periods (.), underscores ( ), and hyphens (- _ ). |  |  |

Elastic Compute Service

| Host name |  | No | Enter the hostname that you want to display in the operating system. Take note of the following items about the hostname: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For a Windows ECS instance, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). For a Linux ECS instance, you can specify the hostname based on the following rules: The hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). You can use the ${instance id} _ placeholder to pass instance IDs into the hostname. For example, if you set the Host name parameter to k8s-${instance id} _ and the instance is assigned an ID of i- 123abc**** , the hostname of the instance is k8s-i-123abc**** . When you create multiple instances at a time, you can configure sequential hostnames for the instances. For example, you can specify the hostnames of ECS instances in the name prefix[begin number,bits]name suffix _ _ _ format. For example, you can specify my name[99,3]ecs . If you create two _ instances, the names of the instances are my name099ecs and my name100ecs . The _ _ valid values of begin number are 0 to 999999, _ and the valid values of bits are 1 to 6. Default value: 6. |  |  |
|---|---|---|---|---|---|
|  |  |  |  | name prefix[begin number,bits]name suffix _ _ _ |  |
| Instance Release Protection |  | No | You can enable the instance release protection feature to prevent instances from being manually released, which can effectively minimize loss caused by accidental operations or the lack of timely communication among team members. |  |  |
| Label |  | No | Select an existing tag, or enter a key and a value to create a tag. Each tag consists of a tag key and a tag value. You can add tags to resources that have identical characteristics, such as resources that belong to the same organization and resources that serve the same purpose. You can use tags to search for and manage resources in an efficient manner. You can specify up to 20 tags. |  |  |

Elastic Compute Service

| Deployment Sets Important This parameter is not displayed if you select an SCC instance type to create ECS instances. | No | Select an existing deployment set or click Create a deployment set to create a deployment set. After the deployment set is created, go back to the Create an instance page and click the icon to obtain the latest deployment set list. For more information about how to create a deployment set, see Create a deployment set. A deployment set is a policy that controls the distribution of ECS instances. You can use deployment sets to design disaster recovery and service availability solutions when you create ECS instances. You can use deployment sets to disperse or aggregate ECS instances. |
|---|---|---|
| Custom Data Format | No | Specifies whether to enable custom data format. Custom instance data can be run as scripts when the instance starts to automate instance configurations, or can be passed into instances as common data. For more information, see Instance user data. Enter your user data in the field. If the user data is already encoded in Base64, turn on Input is Base64 encoded. |
| Custom Data | No |  |

Elastic Compute Service

**Verify the result**

The new instance that you create appears on the ECS Instances page. When the instance is being created, it is in the **Preparing** state. After the instance is created, it enters the
**Running** state.

**What to do next**

If you add data disks when you create the ECS instance, you must partition and format the data disks before you can use the disks. For more information, see Format a data disk for a Linux instance and Format a data disk on a Windows ECS instance.

### Create multiple instances at a

**time**

If you need to create multiple Elastic Compute Service (ECS) instances at a time due to your business requirements, you can specify the parameters in the template to create the instances.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Batch Create**.
5. Configure the region information.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization for which you want to create ECS instances. |
| Resource Set | Yes | Select the resource set in which you want to create ECS instances. |
| Region | Yes | Select the region in which you want to create ECS instances. |
| Zone | Yes | Select the zone in which you want to create ECS instances. Zones are physical locations in a region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create ECS instances in different zones. |

|  | Field | Require d | Description |
|---|---|---|---|
|  | Organization ID | Yes | The organization for which you want to create ECS instances. |

Elastic Compute Service
6. Click **Template Download**, and configure and save the required parameters.
For more information, see Fields in the template.

**Note**

You can create up to 100 instances at a time. The system reads only the first 100 data entries from the CSV file.
7. Upload the CSV file and click **OK**.
8. After the CSV file is uploaded, the system verifies the parameters one by one. After the
verification is passed, click **Create**. If a parameter fails the verification, you can modify the parameter based on the diagnostics suggestion and try again.

**Verify the result**

The new instance that you create appears on the ECS Instances page. When the instance is being created, it is in the **Preparing** state. After the instance is created, it enters the
**Running** state.

**Fields in the template**

|  | Resource Set ID | Yes | The resource set in which you want to create ECS instances. |
|---|---|---|---|
|  | Region ID | Yes | The ID of the region in which you want to create ECS instances. |
|  | Zone ID | Yes | The zone in which you want to create ECS instances. Zones are physical locations in a region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create ECS instances in different zones. |
|  | Instance Type | Yes | The instance type of the ECS instances. The instance type must have sufficient inventory and be in the Available state. |
|  | Image ID | Yes | The image must support the current instance type and cannot be a commercial image (Alibaba Cloud Linux 3 Pro). |
|  | System Disk Type | Yes | Some instance types support only certain disk categories. For more information about the constraints between instance types and disk categories, see the table in the Background information section of the Attach data disks topic. |
|  | System Disk Capacity (GiB) | Yes | The system disk capacity ranges from 20 GiB to 2,048 GiB. |
| VPC ID | VPC ID | Yes | The virtual private cloud (VPC) ID of the ECS instances. The VPC must exist and be valid. |
| vSwitch ID | VSwitch ID | Yes | The vSwitch ID of the ECS instances. The vSwitch must exist and belong to the specified VPC. |
|  | Private IP Address | No | The private IPv4 address of the ECS instances. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you do not specify this parameter, the system automatically allocates a private IP address. |
|  | Security Groups | Yes | The security group to which the ECS instances belong. The security group must exist and belong to the specified VPC. |

Elastic Compute Service

|  | Password |  |  |  |  | The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / . For _ Windows ECS instances, the password cannot start with a forward slash (/). Important If an instance runs the Kylin operating system, the following limits apply to the password: For an instance that is created from a Kylin image, the password must be at least eight characters in length and contain at least three of the following types of characters: uppercase letters, lowercase letters, digits, and special characters. Do not use palindrome passwords, simple or commonly used passwords, or passwords that are too similar to the original password. The password cannot contain the username or any words that are included in the cracklib dictionary. You can run the echo "YOUR PASSWORD" \| cracklib-check _ command to check whether the password meets this requirement. Supported special characters include: ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , . ? / _ |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | ( ) ` ~ ! @ # $ % ^ & * - |  |  |  |
|  |  |  |  |  |  | + = \| { } [ ] : ; ' < > , . ? / _ |  |  |  |  |  |
|  |  |  |  | Yes |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | echo |  |
|  |  |  |  |  |  |  | "YOUR PASSWORD" \| cracklib-check _ |  |  |  |  |
|  |  |  |  |  |  |  |  |  | ( ) ` ~ ! @ # $ % ^ & |  |  |
|  |  |  |  |  |  |  | * - + = \| { } [ ] : ; ' < > , . ? / _ |  |  |  |  |
|  | Instance Name |  |  | Yes |  | Enter a name for the instance. The name must be 2 to 110 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), periods (.), and hyphens _ (-). |  |  |  |  |  |
|  | Instance Description |  |  | No |  | Enter a description for the ECS instance. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . The description can contain letters, digits, periods (.), underscores ( ), and hyphens (-). _ |  |  |  |  |  |

Elastic Compute Service

|  | Hostname | No | Enter the hostname that you want to display in the operating system. Take note of the following items about the hostname: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For a Windows ECS instance, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). For a Linux ECS instance, you can specify the hostname based on the following rules: The hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). You can use the ${instance id} _ placeholder to pass instance IDs into the hostname. For example, if you set the Host name parameter to k8s-${instance id} _ and the instance is assigned an ID of i- 123abc**** , the hostname of the instance is k8s-i-123abc**** . |  |
|---|---|---|---|---|
|  | Deployment Set ID | No | A deployment set is a policy that controls the distribution of ECS instances. You can use deployment sets to design disaster recovery and service availability solutions when you create ECS instances. You can use deployment sets to disperse or aggregate ECS instances. |  |
|  | Custom Data | No | Specifies whether to enable custom data format. Custom instance data can be run as scripts when the instance starts to automate instance configurations, or can be passed into instances as common data. For more information, see Instance user data. |  |

Elastic Compute Service

### Clone an instance

You can use the Elastic Compute Service (ECS) instance cloning feature to quickly create instances that are the same as or similar to the source instances. The instance cloning feature can be used in scenarios such as replication and test environments, application extensions, disaster recovery, backup, migration, and upgrade. This feature can improve service reliability, scalability, and efficiency. This topic describes how to clone instances and the billing method and limits of the cloned instances.

**Prerequisites**

| Parameter | Description |
|---|---|
| Zone | The zone in which the cloned instance resides. |
| Destination VPC | The VPC in which the cloned instance resides. |
| Destination vSwitch | The vSwitch of the cloned instance. |

Elastic Compute Service

**q**

CloudOps Orchestration Service (OOS) is deployed in your environment. A virtual private cloud (VPC) and a vSwitch are created in the destination zone. For more information, see **VPCs and vSwitches > VPC management > Create a VPC** and **VPCs**
**and vSwitches > vSwitch management > Create a vSwitch** in VPC User Guide in the
Apsara Stack Documentation Center. A security group is created. For more information, see Create a security group.

**Billing**

The billing method of the cloned instance is the same as that of the source instance.

**Note**

For more information about billing rules, see **Operations > Service operations >**
**Pricing > Manage billing configurations** in Apsara Uni-manager Operations Console
User Guide in the Apsara Stack Documentation Center. You can clone instances only in the same zone or across zones in the same region. You cannot clone instances across regions. You cannot clone ECS instances to be released. You cannot clone ECS instances that use local SSDs. You can use the ECS instance cloning feature only in the ECS console. You cannot call API operations to use this feature.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance that you want to clone, click the
icon in the **Actions** column, and then choose **Instance Settings > Clone Instance**.
5. In the **Clone Instance** dialog box, configure the parameters in the Destination Instance
Settings step and click **Next**. The following table describes the parameters.

| Destination Security Group | The security group to which the cloned instance belongs. |  |  |
|---|---|---|---|
| Destination System Disk | The category of the system disk of the cloned instance. |  |  |
| Destination Data Disk | The category of the data disk of the cloned instance. |  |  |
| Destination Instance Quantity | The number of cloned instances that you require. You can create up to 100 cloned instances at a time. If the specified number of cloned instances that you require exceeds the maximum number of additional instances that you can create, the number of cloned instances created is equal to the maximum number of additional instances that you can create. |  |  |
| New Password and Confirm Password | The password of the cloned instance. Enter and confirm a password. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain any of the following special characters: ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , _ . ? / For Windows instances, the password cannot start with a forward slash (/). We recommend that you do not enter a password that contains your username. |  |  |
|  |  | ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] : ; ' < > , _ |  |
|  | . ? / |  |  |
| Clone Type | Online Cloning: Without affecting the status of the source instance, the data of the destination instance is the same as the data of the source instance only at the point in time when the cloning operation is complete. During the cloning process, a temporary custom image is created based on the source instance, and then a destination instance is created and run based on the image. However, the eventual data consistency between the source and destination instances is not guaranteed. Shutdown-Consistent Cloning: The system first creates a full snapshot and stops the source instance to ensure data consistency. After the source instance is stopped, the system creates an incremental snapshot, creates a destination instance based on the incremental snapshot, and then runs the destination instance. If the cloning task is successful, the source instance remains in the Stopped state. If the cloning task fails, the source instance is restarted. Note The created temporary custom image is deleted after the cloning task is complete. |  |  |

Elastic Compute Service
6. In the **Confirmation Preview** step, confirm the configurations and click **Submit**.
7. In the **Clone Result** step, view the cloning result.
You can also click **view the stack execution progress** to view the progress of the cloning task.

| Connection tool | ECS instance operating system | On- premises installation required | Support for connection by using a private IP address | Support for connection by using a public IP address | Supported logon credential |
|---|---|---|---|---|---|
| Workbench (used in a browser) | Windows and Linux | No | Yes | No | Passwords |
| Virtual Network Computing (VNC) (used in a browser) | Windows and Linux | No | No | No | Passwords |
| SSH client (third-party client) | Linux | Yes | No | Yes | Passwords and key pairs |
| Remote Desktop Protocol (RDP) client (third- party client) | Windows | Yes | No | Yes | Passwords |

Elastic Compute Service

### Connect to an instance

#### Overview

Before you can perform operations, such as deploying websites, on an Elastic Compute Service (ECS) instance that you created, you must connect to the instance from an onpremises device. You can use different tools to connect to an ECS instance. This topic describes how to select an appropriate tool to connect to an ECS instance.

**Connection tools**

**Use connection tools**

Workbench is a remote connection tool provided by Apsara Stack, which can be used in a browser. It supports features such as file management, multi-terminal, and operation auditing. You can use Workbench to connect to Linux or Windows ECS instances.
**Characteristics:** Workbench is an installation-free tool that you can directly use in a
browser. You can use Workbench to connect to only ECS instances in Apsara Stack.
**Network**: You can establish connections by using private IP addresses of ECS instances.
**Authentication methods:** Password-based authentication is supported.

**References**

##### Use Workbench to connect to a Linux instance over SSH

Elastic Compute Service

##### Use Workbench to connect to a Windows instance over RDP

**VNC**

You can use VNC to connect to an ECS instance in the **Running** state, even if the instance operating system is starting, or to an ECS instance in the **Stopping** state.

**Note**

After you use VNC to connect to an ECS instance, you can directly view the real-time interface of the operating system in the instance. By default, Linux may not include a GUI. VNC is not restricted by security group settings or the software that runs on the instance. You can use VNC to troubleshoot the issues that occur when other connection tools are used.
**Characteristics:** You cannot use VNC to connect to ECS instances in the **Stopped** state.
You can use VNC to connect only to ECS instances in Apsara Stack.
**Network:** You do not need to associate elastic IP addresses (EIPs) with ECS instances.
**Authentication methods:** Password-based authentication is supported.

**References**

**Third-party SSH client**

You can use a third-party SSH client to connect to Linux ECS instances based on your business requirements. Common SSH clients include **OpenSSH** and **PuTTY**.
**Characteristics:** You may need to install a third-party SSH client before you can use the
client.
**Network:** You must associate EIPs with ECS instances.
**Authentication methods:** Key pair-based authentication and password-based
authentication are supported.

**References**

#### Connect to a Linux instance by using SSH commands in Linux or Mac OS X

#### Connect to a Linux instance by using a remote connection tool in Windows

**Third-party RDP client**

You can use a third-party RDP client to connect to Windows ECS instances based on your business requirements. Common RDP clients include **Microsoft Remote Desktop** and
**Windows Remote Desktop**.
**Characteristics:** You may need to install a third-party RDP client before you can use the
client.
**Network:** You must associate EIPs with ECS instances.
**Authentication methods:** Password-based authentication is supported.

**References**

Connect to a Windows instance by using RDC

#### Connect to an instance by using

**Workbench**

| Rule direc tion | Actio n | Proto col type | Port or port range | Priori ty | Authorization object |
|---|---|---|---|---|---|
| Inbo und | Allo w | Tran smis sion Contr ol Proto col (TCP) | 22/22, which is the default port on a Linux instance A port range if you have manually enabled other ports on the Linux instance | 1 | IP address related to Workbench Note To obtain specific IP addresses, consult your administrator. |

| Parameter | Description |
|---|---|

Elastic Compute Service

##### Use Workbench to connect to a Linux

**instance over SSH**

Workbench is a connection tool that is more efficient and convenient than Virtual Network Computing (VNC) and allows multiple users to connect to a single Linux Elastic Compute Service (ECS) instance at the same time. Workbench allows you to manage files on ECS instances in a visualized manner. You can use Workbench to upload, download, add, modify, delete, and view files.

**Prerequisites**

A service-linked role for Workbench is created. If you use Workbench to connect to an instance for the first time, you are prompted to create a service-linked role for Workbench. A logon password is specified for the instance. For more information, see Reset the logon password of an instance. The instance to which you want to connect is in the **Running** state. Security group rules that allow the IP addresses related to Workbench to access the Linux instance are created. For more information about how to create a security group rule, see Create a security group rule.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the Linux instance to which you want to connect and click
**Connect** in the **Actions** column.
5. In the **Connect** dialog box, click **Log On** in the **Workbench** section.
6. In the **Instance Login** dialog box, configure the parameters.
Configure the required parameters that are described in the following table.

| Instance | The instance to which you want to connect. The information of the current instance is automatically entered. You can also enter the IP address or name of another instance. |
|---|---|
| Connection | The IP address that is used to connect to the instance. Only private IP addresses are supported. |
| Authenticatio n | The authentication method. Set the value to Password-based. Enter a username, such as root or ecs-user, and enter the password for the username. |

| Parameter | Description |
|---|---|
| Protocol | The protocol over which the instance is connected. By default, Terminal Connection (SSH) is selected. |
| Port | If you set the Protocol parameter to Terminal Connection (SSH), this parameter is automatically set to 22. If you specified a different port as the remote connection port, enter the port number. |
| Language | The language that you prefer. The selected language affects the outputs of the Linux instance. We recommend that you select Default. This way, Workbench detects the language settings of the Linux instance and configures the appropriate settings. |
| Character Set | The character set that you prefer. The selected character set affects command outputs on the instance. We recommend that you select Default for Workbench to detect the character set settings of the instance and to make configurations accordingly. |

Elastic Compute Service In the lower part of the dialog box, click **More Options** to show the optional parameters. The following table describes the parameters.
7. Click **OK**.

##### Use Workbench to connect to a Windows

**instance over RDP**

Workbench is a connection tool that is more efficient and convenient than Virtual Network Computing (VNC) and allows multiple users to connect to a single Windows Elastic Compute Service (ECS) instance at the same time. Workbench supports the following authentication methods for logons to instances: password-based authentication, key-based authentication, and credential-based authentication. You cannot use Workbench to connect to an ARM architecture-based Windows instance.

| Rule direc tion | Actio n | Proto col type | Port or port range | Priori ty | Authorization object |
|---|---|---|---|---|---|
| Inbo und | Allo w | Tran smis sion Contr ol Proto col (TCP) | 3389/3389, which is the default port on a Windows instance A port range if you have manually enabled other ports on the Windows instance | 1 | IP addresses related to Workbench Note To obtain specific IP addresses, consult your administrator. |

| Parameter | Description |
|---|---|
| Instance | The instance to which you want to connect. The information of the current instance is automatically entered. You can also enter the IP address or name of another instance. |
| Connection | The IP address that is used to connect to the instance. Only private IP addresses are supported. |
| Authenticatio n | The authentication method. Set the value to Password-based. Enter a username, such as root or ecs-user, and enter the password for the username. |

Elastic Compute Service

**Prerequisites**

A service-linked role for Workbench is created. If you use Workbench to connect to an instance for the first time, you are prompted to create a service-linked role for Workbench. A logon password is specified for the instance. For more information, see Reset the logon password of an instance. The instance to which you want to connect is in the **Running** state. Security group rules that allow the IP addresses related to Workbench to access the Windows instance are created. For more information about how to create a security group rule, see Create a security group rule.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the Windows instance to which you want to connect and
click **Connect** in the **Actions** column.
5. In the **Connect** dialog box, click **Log On** in the **Workbench** section.
6. In the **Instance Login** dialog box, configure the parameters.
Configure the required parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Protocol | The protocol over which the instance is connected. By default, Terminal Connection (SSH) is selected. |
| Port | If you set the Protocol parameter to Terminal Connection (SSH), this parameter is automatically set to 22. If you specified a different port as the remote connection port, enter the port number. |
| Language | The language that you prefer. The selected language affects the outputs of the Windows instance. We recommend that you select Default. This way, Workbench detects the language settings of the Windows instance and configures the appropriate settings. |
| Character Set | The character set that you prefer. The selected character set affects command outputs on the instance. We recommend that you select Default for Workbench to detect the character set settings of the instance and to make configurations accordingly. |

Elastic Compute Service In the lower part of the dialog box, click **More Options** to show the optional parameters. The following table describes the parameters.
7. Click **OK**.

##### Manage files

Workbench allows you to manage files on Linux Elastic Compute Service (ECS) instances in a visualized manner. For example, you can create, edit, and delete files. This topic describes how to use Workbench to manage files on a Linux ECS instance.

**Prerequisites**

An ECS instance is connected. For more information, see Use Workbench to connect to a Linux instance over SSH. Your account is granted the permissions to create folders in specific directories and the permissions to create, edit, upload, and download files in specific directories.

**View files**

1. In the top navigation bar, choose **File > New Navigator** to open a file navigator.
2. View folders and files.
Elastic Compute Service The following figure shows a file navigator window.

**Create a file**

1. In the top navigation bar, choose **File > New Navigator** to open a file navigator window.
2. In the file tree, right-click the location where you want to create a file and select **New File**.
3. In the **New File** dialog box, enter a name for the file and click **OK**.

**Edit a file**

1. In the upper-left corner of the top navigation bar, choose **File > New Navigator** to open a
file navigator. Elastic Compute Service
2. In the file tree, right-click a file and select **Open**.
3. Enter content in the text editor and click the Save icon in the upper-right corner.
4. In the **Confirm Saving** message, click **OK**.

**Delete a file**

1. In the top navigation bar, choose **File > New Navigator** to open a file navigator.
2. In the file tree, right-click a file and select **Delete**.
3. In the **Confirm Deletion** message, click **OK**.

##### Audit commands

The command audit feature of Workbench allows you to check whether historical commands meet security requirements after you used Workbench to connect to an Elastic Compute Service (ECS) instance and ran commands on the instance. The feature helps you detect abnormal operations and risk events. The command audit feature also records information about commands, such as the command syntax and the execution time of commands, which facilitate the subsequent analysis and auditing. This topic describes how to use the command audit feature of Workbench.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

Elastic Compute Service

**Procedure**

1. Connect to an ECS instance by using Workbench.
For more information, see Use Workbench to connect to a Linux instance over SSH or Use Workbench to connect to a Windows instance over RDP.
2. In the top navigation bar of Workbench, choose **Session > Command Audit**.
3. In the command audit list, find the command audit record that you want to view and click
**View** in the **Actions** column to view the information, including the command, logon user,
and execution path.

#### Connect to an instance by using a

**third-party client tool**

##### Connect to a Linux instance by using SSH

**commands in Linux or Mac OS X**

This topic describes how to use SSH commands to connect to a Linux instance.

**Prerequisites**

The instance and the security group are created. The instance is in the **Running** state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

**Procedure**

1. Enter the following command and press the Enter key:

```
ssh root@<EIP of the instance>
```

2. Enter the instance password of the root user and press the Enter key.

##### Connect to a Linux instance by using a

**remote connection tool in Windows**

This topic describes how to connect to a Linux instance by using the PuTTY tool.

**Prerequisites**

Connection tools are used in a similar way. In this example, PuTTY is used to connect to a Linux instance. To download PuTTY, go to the Putty official website.

| Rule direction | Action | Protocol type | Port range | Priority | Authoriza tion type | Authoriza tion object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

Elastic Compute Service

**Procedure**

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

##### Connect to a Windows instance from a

**Windows computer by using Remote Desktop**

This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC).

**Prerequisites**

A Windows instance is created and added to a security group. The instance is in the **Running** state. A logon password is set for the instance. An elastic IP address (EIP) is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

**Procedure**

1. Use one of the following methods to enable RDC:

**Note**

In this topic, an on-premises computer that runs Windows 10 is used. Operations may vary based on your operating system. On the taskbar of the Windows desktop, enter `mstsc` in the search box. Then, click
**Remote Desktop Connection** in the search results.
Elastic Compute Service Press the Windows logo key+R. In the **Run** dialog box, enter `mstsc` and click **OK**.
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

#### Connect to an instance by using VNC

##### Install the certificate for VNC in Windows

Before you can log on to the Virtual Network Computing (VNC) management terminal, you must export the relative certificate from the site such as the Apsara Uni-manager Management Console and install the certificate in a browser on your computer.

**Background information**

The VNC feature is provided by the VNC proxy service. The VNC proxy service uses a different certificate than that of Apsara Infrastructure Management Framework. The certificate of the VNC proxy service must be imported manually.

**Procedure**

1. Export the certificate from the Apsara Uni-manager Management Console.
Elastic Compute Service i. Log on to the Apsara Uni-manager Management Console. Then, press the **F12** key or
**Fn+F12** to view and select the certificate.
In this example, the Chrome browser is used. Press the **F12** key to open Chrome DevTools and click View certificate on the Security tab, as shown in the following figure. ii. In the **Certificate** window, click the **Certificate Path** tab, select the root certificate, and then click **View Certificate**. iii. In the **Certificate** window, click the **Details** tab and then click **Copy to File**. iv. In the **Certificate Export Wizard**, click **Next**. v. Select **DER encoded binary X.509 (.CER)** as the format and then click **Next**. vi. Click **Browse**, select the location where to store the certificate, enter a file name, and then click **Save**. vii. Click **Next**. viii. Click **Complete**. ix. Then, click **OK**.
2. Install the certificate in a browser on your on-premises computer.
i. Double-click the certificate. ii. In the **Certificate** window, click **Install Certificate**. iii. In the **Certificate Import Wizard**, click **Next**. iv. Select **Place all certificates in the following store** and click **Browse**. v. In the **Select Certificate Store** window, select **Trusted Root Certificate Authority** and then click **OK**. vi. In the **Certificate Import Wizard**, click **Next**. vii. Click **Complete**. viii. If a security warning message is displayed, click **Yes**.
3. Restart your browser and log on to the Apsara Uni-manager Management Console.
After the certificate is installed, the security warning message is no longer displayed on the

| Scenario | Operation that you can perform after you connect to the instance by using VNC |
|---|---|
| The operating system of an instance slowly starts due to specific system checks. | Check the self-check progress. |
| The firewall in the operating system of an instance is accidentally enabled. | Disable the firewall. |

Elastic Compute Service left of the URL when you log on to the Apsara Uni-manager Management Console.

##### Connect to an instance by using VNC

Virtual Network Computing (VNC) is a method used to connect to an Elastic Compute Service (ECS) instance. You can use VNC to connect to an ECS instance in the **Running** state even when the operating system is starting, or to an ECS instance in the **Stopping** state. If you cannot connect to an ECS instance by using other methods, you can connect to the instance by using VNC to perform emergency O&M and troubleshoot issues. This topic describes how to connect to an ECS instance by using VNC in the ECS console.

**Note**

Chinese characters cannot be displayed after you log in to a Linux instance by using VNC. To display Chinese characters on a Linux instance, log in to the instance by using SSH. For more information about login methods to ECS instances, see Overview.

**Prerequisites**

The ECS instance is in the **Running** state. The root certificate is imported to your web browser. For more information, see Install the certificate for VNC in Windows. The VNC password is reset if you connect to the instance for the first time after the instance is created. For more information, see Change the VNC password.

**Background information**

The following passwords are involved when you use VNC to connect to an instance: VNC password: the password of VNC used to connect to an instance. Instance login password: the password used to log in to the instance operating system for management. If you cannot connect to an ECS instance by using Workbench or connection software, you can connect to the instance by using VNC and view the real-time status or issues of the instance operating system. The following table describes the scenarios in which you can connect to an ECS instance by using VNC and the operations that you can perform after you connect to the instance.

| An instance is intruded, which causes a high CPU utilization and high bandwidth usage. | Troubleshoot and terminate abnormal processes. |
|---|---|

Elastic Compute Service

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Instance page, find the instance to which you want to connect and click **Connect** in
the **Actions** column.
5. In the **Connect** dialog box, click **Log On** in the **VNC** section.
6. In the **Please enter your VNC password** dialog box, enter the VNC password and click
**OK**.
After you log in to VNC, a login page similar to the following one appears.
7. Log in to the operating system of the instance.
**Linux instance**:
a. Enter your username, such as root or ecs-user, and press the Enter key. b. Enter the login password of the instance and press the Enter key.

**Note**

The characters of the password are hidden when you enter the login password of the Linux instance. You can switch between up to 10 different VNC management terminals when you connect to the Linux instance. The default terminal is **CTRL+ALT+F1**. For example, you can choose **Send Remote Call > CTRL+ALT+F2** to switch to **CTRL+ALT+F2**. A persistent black screen indicates that the instance is in sleep mode. Press a key to wake up the system.
**Windows instance**:
a. In the upper-left corner of the page that appears, choose **Send Remote Commands**
**> CTRL+ALT+DELETE**.
Elastic Compute Service b. Select an account, enter the login password of the instance, and then press the Enter key.

### Manage instance status

#### Stop an instance

You can stop the instances that you do not use for the moment. The stop operation interrupts services that are running on the instances. Exercise caution when you perform this operation.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Stop one or more ECS instances.
To stop a single instance at a time, find the instance and choose **Instance Status >**
**Stop Instance** in the **Actions** column.
Alternatively, go to the Instance Details page and click **Stop** in the upper-right corner. To stop one or more instances at a time, select the instances and click **Stop** in the lower part of the Instances page.
5. In the message that appears, click **Stop Instance**.

**Results**

When an instance is being stopped, its state in the **Status** column changes from **Running** to
**Stopping**. When the instance is stopped, its state changes to **Stopped**.

**FAQ**

**How do I resolve the issue when an instance remains in the**

**Stopping state?**

When your ECS instance remains in the **Stopping** state for an extended period, the ECS instance may be in a normal or abnormal stop process. You need to check the stop progress of the operating system and select a handling method based on the stop status. Normal stop: The ECS instance is in normal stop status, and the stop process is relatively long because the operating system is installing system patches or the low operating system configurations cause the delayed stop response. Abnormal stop: The ECS instance is in abnormal stop status. For example, the stop process does not start because an error occurs in the operating system when you stop the instance.

**Solutions:**

1. View the screenshots of the ECS instance to obtain the stop progress of the operating
system.
2. If you cannot identify the issue through the screenshot, you can connect to the instance by
using Virtual Network Computing (VNC) to view the stop progress of the operating system.
3. Select a handling method based on the stop status of the operating system.
Normal stop: Wait for the stop process to complete. Elastic Compute Service Abnormal stop: If an abnormality occurs, you can connect to the instance by using VNC and manually handle the stop issue. You can also force stop the instance based on your needs.

**Important**

**Force Stop** is equivalent to a power outage and may cause data loss if the data is not
written to the disk in the operating system of the instance.

#### Start an instance

If an Elastic Compute Service (ECS) instance is in a state (such as Stopped) in which it cannot provide services, you must start the instance before you can use it. This topic describes how to start an instance in the ECS console.

**Prerequisites**

The instance is in the **Stopped** state.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Start one or more ECS instances.
To start a single instance at a time, find the instance and choose **Instance Status >**
**Start Instance** in the **Actions** column.
Alternatively, go to the Instance Details page and click **Start** in the upper-right corner. To start one or more instances at a time, select the instances and click **Start** in the lower part of the Instances page.
5. In the message that appears, click **Start Instance**.

**Result**

When an instance is being started, its state in the **Status** column changes from **Stopped** to
**Starting**. When the instance is started, its state changes to **Running**.

#### Restart an instance

After you change the logon passwords or install system updates for instances, you must restart the instances. The restart operation stops the instances for a short period of time and interrupts services that are running on the instances. Exercise caution when you perform this operation.

**Prerequisites**

The instances that you want to restart are in the **Running** state.

**Warning**

The restart operation stops the instances for a short period of time and interrupts services that are running on the instances. Exercise caution when you perform this operation. Elastic Compute Service

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Restart one or more ECS instances.
To restart a single instance at a time, find the instance and choose **Instance Status >**
**Restart Instance** in the **Actions** column.
Alternatively, go to the Instance Details page and click **Restart** in the upper-right corner. To restart one or more instances at a time, select the instances and click **Restart** in the lower part of the Instances page.
5. In the message that appears, select whether to forcefully restart the instances.
If you select **Force Restart**, the instances are forcefully restarted. This may result in the loss of unsaved data. If you do not select **Force Restart**, the instances are gracefully restarted.
6. Click **Restart Instance**.

**Results**

When an instance is being restarted, its state in the **Status** column changes from **Running** to **Stopping**. When the instance is restarted, its state changes to **Running**.

**Note**

If your ECS instance remains in the **Stopping** state for an extended period during the restart process, the instance may be in an abnormal shutdown process and will not start successfully. You need to manually restart the ECS instance again.

#### Delete an instance

You can delete Elastic Compute Service (ECS) instances that you no longer need to release resources. This topic describes how to delete ECS instances.

**Prerequisites**

The ECS instances that you want to delete are in the **Stopped** state.

**Background information**

Deleted instances cannot be recovered. We recommend that you back up data before you delete instances. If data disks are released along with the ECS instances, the disk data cannot be recovered. For information about how to create snapshots of disks to back up disk data, see Create snapshots.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Delete one or more ECS instances.
To delete a single ECS instance at a time, perform the following operations: Elastic Compute Service a. Find the ECS instance and choose **Instance Status > Delete** in the **Actions** column. You can also go to the Instance Details page and choose **More > Delete** in the upperright corner. b. In the dialog box that appears, select **Move to Recycle Bin** based on your business requirements. Then, click **Release**. To delete one or more ECS instances at a time, perform the following operations: a. Select the ECS instances that you want to delete and click **Delete** in the lower part of the Instances page. b. In the dialog box that appears, select **Move to Recycle Bin** based on your business requirements. Then, click **Release**.

**Important**

If a link value is specified for the **deleted ECS instance** in the **ECS channel list** in the UniConsole, no message appears after you click Delete. For more information about how to modify the channel link, see **Service console**
**configuration management** in **Apsara Uni-manager Operations Console**
**User Guide**.
To prevent business fluctuations caused by accidental deletion, **Move to**
**Recycle Bin** is selected by default when you delete an instance. When deleted
ECS instances are moved to the recycle bin, the instances enter a retention period, which is three days by default. During the retention period, the computing resources (vCPUs and memory) of the ECS instances are released, elastic IP addresses (EIPs) are disassociated from the instances, and the storage resources of the instances are retained. If you do not restore resources from the recycle bin during the retention period, the resources are automatically deleted when the retention period ends, and cannot be restored. You can restore the instances from the recycle bin anytime during the retention period. For more information, see Restore an instance. ECS instances equipped with local disks cannot be moved to the recycle bin.

### Manage instance attributes

#### View the details of an instance

You can view all existing Elastic Compute Service (ECS) instances within your account and the details of each ECS instance. The details of an ECS instance include the basic configurations, disks, snapshots, security groups, elastic network interfaces (ENIs), and operation records of the instance. By default, the **Overview** page is displayed when you log in to the ECS console. You can view the overview of ECS instances within your account on the **Overview** page. The Overview page consists of the following sections: This section displays statistics about ECS instance resources that belong to the selected resource set of the selected organization in your account in the selected region. The statistics include the total number of ECS instances, number of ongoing ECS instances, number of images, number of disks, number of security groups, and number of snapshots. Elastic Compute Service Click the value of each parameter to view a list of resources. For example, you can click the value of the Total ECS Instances parameter to view a list of ECS instances on the ECS Instances page.

**Top 10 in Quota Usage**

This section displays the 10 organizations with the highest quota usage. You can click **By**
**CPU Utilization**, **By Memory Utilization**, or **By Storage Utilization** to list the 10
organizations with the highest CPU, memory, or disk quota usage and view the quota usage rankings and trends of the organizations in the previous 7, 15, or 30 days.

**Quota Statistics**

CPU Quota: includes the CPU quota allocated to the resource sets and subordinate organizations of the current organization, and the CPU quota used by the current organization and its subordinate organizations. GPU Quota: includes the GPU quota allocated to the resource sets and subordinate organizations of the current organization, and the GPU quota used by the current organization and its subordinate organizations. Memory Quota: includes the memory quota allocated to the resource sets and subordinate organizations of the current organization, and the memory quota used by the current organization and its subordinate organizations. Disk Quota: includes the disk quota allocated to the resource sets and subordinate organizations of the current organization, and the disk quota used by the current organization and its subordinate organizations.

**Resource Alarm**

This section displays the alerts generated for all resources in the current organization. You can find an alert and click **To deal** to go to the **Alert History** page of the CloudMonitor to view the alert details.

**Alert Statistics**

This section displays the number of alerts generated for all resources in the current organization and the number of alerts at different levels. You can click **View More** to go to the **Alert History** page of the CloudMonitor to view the details of alerts.

**Alert Trend**

This section displays the alert trend within the last 7, 15, and 30 days in the current organization.

**View the information about a single instance on the Instance**

**Details page**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the ECS Instances page, view the information about existing ECS instances.
You can view the information about ECS instances in the ECS instance list, which consists of multiple columns, such as **Instance ID/Name**, **Status**, **Tag, IPv4 Address,**
**Organization/Resource Set**, **Configuration/Specifications**, **Operating System**,
**Image ID/Name**, **Zone**, and **Creator**.
You can perform the following steps to specify the columns to be displayed in the ECS instance list. i. In the upper-right corner of the ECS instance list, click the icon. Elastic Compute Service ii. In the **Custom Columns** dialog box, select the columns that you want to display in the ECS instance list, such as **Creator**, and then click **Save**.

**Important**

You can display the Creator column in the lists of ECS instances, disks, snapshots, custom images, security groups, ENIs, key pairs, and deployment sets. If Creator appears in the Custom Columns dialog box, you can display the Creator column in the resource list. If you want to change the creator of a resource, you can move the pointer over the value in the **Creator** column that corresponds to the resource and click the icon.
5. Select a filter condition, such as **Instance ID**, from the drop-down list and enter the
relevant information in the search box. The instances that meet the specified filter condition are automatically displayed in the instance list.

**Note**

Except for **Tag**, all filter options support fuzzy search. You can specify multiple filter conditions to narrow down the search results.
6. Find the ECS instance whose details you want to view. Then, use one of the following
methods to go to the Instance Details page of the ECS instance to view the details of the instance: In the **Instance ID/Name** column, click the instance ID. In the **Actions** column, click **Manage**. The following table describes the information that is displayed on the **Instance Details** page.

| Section | Description |
|---|---|
| Basic Information | The basic information about the ECS instance, including the instance name, instance ID, region and zone in which the instance resides, organization and resource set to which the instance belongs, instance status, and instance description. |
| Configurations | The configurations of the ECS instance, including the architecture, number of vCPUs, memory, instance type, operating system, and image name. |
| Network Information | The network information about the ECS instance, including the network type, name and ID of the virtual private cloud (VPC) in which the instance resides, name of the vSwitch to which the instance is connected, and primary private IP address. |
| Other Information | The O&M information about the ECS instance, including the release protection settings, name of the key pair that is bound to the instance, and whether the instance I/O is optimized. |

Elastic Compute Service
7. View the information and operation logs of an instance.
Monitoring information: Click the **Monitoring** tab to view the monitoring information about the ECS instance, including the operating system monitoring information, GPU monitoring information, and basic monitoring information. For more information, see View the monitoring information of an instance. Disk information: Click the **Disks** tab to view the information about each disk that is attached to the instance, including the ID, name, status, category, and size of the disk. For more information about disks, see Disks. Security group information: Click the **Security Groups** tab to view the information about each security group to which the instance belongs, including the ID, name, and type of the security group and the security group rules. For more information about security groups, see Security groups. Snapshot information: Click the **Snapshots** tab to view information about the snapshots that are created for disks attached to the instance and the snapshot-consistent groups that are associated with the disks. For more information about snapshots, see Snapshots. ENI information: Click the **ENIs** tab to view the information about each ENI that is bound to the instance, including the ENI name, ENI ID, and ID of the vSwitch to which the ENI is connected. For more information about ENIs, see Elastic Network Interfaces. Operation logs: Click the **Operation Log** tab to view the operation logs of the instance, including the operation name, operator, operation status, operation source (console call or API call), operation type, source IP address of the operation, and operation time. Elastic Compute Service Select a filter condition from the drop-down list and enter the corresponding information in the search box. The operation logs that meet the specified filter condition are automatically displayed.

**Note**

Operation logs can be retained for seven days. You can contact the administrator to change the retention period of operation logs on the Log Storage Settings page. To go to this page, click **Configurations > Log Storage Settings** in the left-side navigation pane. For more information, see the **Log storage settings** topic in
**Apsara Uni-manager Operations Console User Guide** .
If the retention period of operation logs on the Log Storage Settings page is extended, historical operation logs that are not retained before the retention period is extended are not backfilled. Instance management: In the upper-right corner of the Instance Details page, you can click Start, Restart, or Stop to start, restart, or stop the instance. You can also click **More** to perform other operations on the instance, such as resetting the logon password of the instance, attaching a disk, and logging on to the instance by using Virtual Network Computing (VNC).

#### Modify the properties of an instance

After you create an Elastic Compute Service (ECS) instance, you can modify the name, description, and user data of the instance based on your business requirements. If you want to modify the CPU topology of an instance, stop the instance. For more information, see Stop an instance.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance that you want to modify, click the
icon in the **Actions** column, and then choose **Instance Settings > Modify Instance**
**Properties**.
5. In the **Modify Instance Properties** dialog box, modify the following parameters of the
instance:
**Instance Name**: The name of the instance. The name must be 2 to 128 characters in
length. The name must start with a letter and cannot start with `http://` or `https://` . The name can contain letters, digits, periods (.), underscores (_), hyphens (-), and colons (:).

**Note**

You can also move the pointer over the instance name on the ECS Instances page and click the icon next to the instance name. In the Modify Instance Properties dialog box, modify the instance name.

| How to reset | Restart the instance | Required instance status | Install Cloud Assistant Agent |
|---|---|---|---|
| Reset the password online | No | Running | Yes. Cloud Assistant Agent must be in the Running state. |

Elastic Compute Service
**Hostname**: The hostname that is displayed in the operating system. Take note of the
following items about the hostname: The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). For a Windows instance, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. It can contain letters, digits, and hyphens (-). For a Linux instance, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-).
**CPU Topology**: The type of the CPU topology. Valid values: **HT Continuous Mode** and
**HT Discrete Mode**.
You can modify the CPU topology only for specific instance types. For more information about CPU topologies, see View and modify CPU topologies. HT continuous CPU topology: Logical cores are continuously assigned to physical cores, which can help reduce communication and contention between threads. This mode is suitable for computing tasks that require low memory access latency and computing power close to computing power provided by the physical cores, such as scientific computing, data analysis, and high-performance computing, which are sensitive to memory access and core computing. HT discrete CPU topology: Logical cores are discretely distributed to physical cores, which can help reduce resource contention in a multi-threaded environment and provide better performance isolation. This mode is suitable for the tasks that are separately assigned to threads or the tasks that require high single-thread performance.
**Instance Description**: The description of the instance. The description must be 2 to 256
characters in length and cannot start with `http://` or `https://` . The description can contain letters, digits, periods (.), underscores (_), and hyphens (-).
**User Data**: The user data of the instance. For more information about user data, see
Customize instance data.
6. Click **OK**.

#### Reset the logon password of an

**instance**

If you did not specify a logon password when you created an Elastic Compute Service (ECS) instance or if you have forgotten the password, you can reset the password.

**Comparison between the methods used to reset the logon**

**password of an ECS instance**

| Reset the password offline | Yes | Running or Stopped | No |
|---|---|---|---|

| Parameter | Description |
|---|---|
| Password Reset Method | Reset Online: You do not need to restart the instance. Reset Offline: After you reset the password offline, you must restart or start the instance to make the new password take effect. |

Elastic Compute Service

**Important**

If the online password reset feature is disabled in your environment, contact your administrator to enable the feature. When you use the online password reset feature, the plaintext password may be leaked. We recommend that you reset the password of an instance after you log on to the instance.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance that you want to manage and use one of the
following methods to reset its logon password: Reset the logon password on the Instance Details page. Click the instance ID in the **Instance ID/Name** column. In the upper-right corner of the Instance Details page, choose **More > Reset Instance Password**. Click **Manage** in the **Actions** column. In the upper-right corner of the Instance Details page, choose **More > Reset Instance Password**. In the **Actions** column, click the icon and then choose **Password/Key Pair > Reset**
**Instance Password**.
5. In the **Reset Password** dialog box, select **Reset Online**, configure the parameters, and
then click **OK**. The following table describes the parameters.

| Username | The username that you specified when you created the instance. Linux instance: You can reset only the password of the root or ecs-user user. Windows instance: You can reset only the password of the Administrator user. Note If the administrator of your Windows instance is not the Administrator user, the password reset feature is unavailable. |  |  |  |  |
|---|---|---|---|---|---|
|  | The password must be 8 to 30 characters in length, and contain at least three of the following types of characters: Uppercase letters Lowercase letters Digits Special characters: ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] _ : ; ' < > , . ? / The logon password of a Windows instance cannot start with a forward slash (/). Important If an instance runs the Kylin operating system, the following limits apply to the password: For an instance that is created from a Kylin image, the password must be at least eight characters in length and contain at least three of the following types of characters: uppercase letters, lowercase letters, digits, and special characters. Do not use palindrome passwords, simple or commonly used passwords, or passwords that are too similar to the original password. The password cannot contain the username or any words that are included in the cracklib dictionary. You can run the echo "YOUR PASSWORD" \| cracklib-check command to check _ whether the password meets this requirement. Supported special characters include: ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] _ : ; ' < > , . ? / |  |  |  |  |
|  |  |  |  | ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] _ |  |
|  | : ; ' < > , . ? / |  |  |  |  |
| New Password and Confirm Password |  |  |  |  |  |
|  |  |  | ( ) ` ~ ! @ # $ % ^ & * - + = \| { } [ ] _ |  |  |
|  |  | : ; ' < > , . ? / |  |  |  |

Elastic Compute Service
6. Restart the instance in the ECS console or by calling an API operation to make the new
password take effect if you set the **Password Reset Method** parameter to **Reset Offline**. For more information, see Restart an instance or the **RebootInstance** topic in **ECS**
**Developer Guide**.
Elastic Compute Service

#### Change the VNC password

If you use Virtual Network Computing (VNC) to connect to an Elastic Compute Service (ECS) instance for the first time or if you forget the VNC password, you can change the VNC password.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
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

**Note**

If your instance is a non-I/O optimized instance, you must restart the instance in the ECS console for the new password to take effect.

#### Disable HT

You can disable Hyper-Threading (HT) to allow an Elastic Compute Service (ECS) instance to exclusively use physical CPU cores. This improves performance and reduces costs. For example, in memory-intensive business scenarios, you can disable HT to reduce the number of vCPUs. This can improve the memory-to-CPU ratio and reduce software licensing costs.

**CPU and vCPU**

CPU stands for central processing unit. A single CPU can contain several physical cores. The HT technology can create two logical processing cores for each physical core. vCPUs are the virtual processing cores of ECS instances. Apsara Stack ECS supports multi-threading based on HT of the x86 architecture. HT allows two threads to concurrently run on a single physical core. Each thread can be considered as a vCPU. Elastic Compute Service You can disable HT only for the following Intel processer-powered instance families: ecs.g6s-k10, ecs.g6s-k25, ecs.g6m-k10, and ecs.g6m-k25 ecs.g7s-k10, ecs.g7s-k25, ecs.g7m-k10, ecs.g7m-k25, and ecs.g7x-k10, ecs.g7x-k25 After HT is disabled for an instance, HT cannot be enabled for the instance, and the instance does not support hot or cold configuration changes. After HT is disabled for an instance, the number of CPU cores in the instance is 1/2 of the number of that defined by the original instance type. HT can be enabled or disabled only when you create an instance. After the instance is created, you cannot enable or disable HT. The following section describes only the core parameters for disabling HT. For more information about other parameters, see Create an instance.
**Enable Hot Configuration Change**: Set the parameter to **No**.
**Specification**: Select an instance type that allows you to modify the CPU topology. In this
example, ecs.g7s-k25-c1m2.large is selected.
**HT Hyper-Threading Technology**: Turn off HT Hyper-Threading Technology.
If you turn on HT Hyper-Threading Technology, two logical processing cores are created for each physical core of the ECS instance. If you turn off HT Hyper-Threading Technology, the ECS instance exclusively uses CPU physical cores.

**Check whether HT is disabled for an instance**

1. Specify columns to be displayed in the instance list.
By default, the **Hyper-Threading Disabled** column is not displayed on the ECS Instances page. To display the **Hyper-Threading Disabled** column, click the icon in the upperright corner of the ECS Instances page. In the Custom Columns dialog box, select **Hyper-**
**Threading Disabled** and click **Save**.
Elastic Compute Service
2. On the ECS Instances page, check whether HT is disabled for the instance in the **Hyper-**
**Threading Disabled** column.

#### View and modify CPU topologies

You can view and modify the CPU topologies of Elastic Compute Service (ECS) instances based on your business requirements to improve performance and parallelism and optimize resource allocation in various scenarios such as virtualization environments, multi-threaded programming, and high-performance computing (HPC). This topic describes how to view and modify the CPU topology of an instance.

**Background information**

CPU topology refers to the manner in which physical cores and logical cores are connected in a multi-core processor. In most cases, each physical core contains one or more logical cores. The physical cores are interconnected by buses or an interconnect network. The performance and energy efficiency of multi-core processors vary based on the CPU topology. Only specific Apsara Stack instance families support two types of CPU topologies: `Hyper-` `Threading (HT) continuous` (ContinuousCoreToHTMapping) CPU topology and `HT` `discrete` (DiscreteCoreToHTMapping) CPU topology. Elastic Compute Service HT continuous CPU topology: Logical cores are continuously assigned to physical cores, which can help reduce communication and contention between threads. This mode is suitable for computing tasks that require low memory access latency and computing power close to computing power provided by the physical cores, such as scientific computing, data analysis, and high-performance computing, which are sensitive to memory access and core computing. HT discrete CPU topology: Logical cores are discretely distributed to physical cores, which can help reduce resource contention in a multi-threaded environment and provide better performance isolation. This mode is suitable for the tasks that are separately assigned to threads or the tasks that require high single-thread performance. In this example, an x86 instance that has eight vCPUs is used. The following figures show the two types of CPU topologies.

**HT continuous CPU topology**

Relationships between logical cores and physical cores: `HT 0` and `HT 1` belong to `CORE 0` . `HT 2` and `HT 3` belong to `CORE 1` . `HT 4` and `HT 5` belong to `CORE 2` . `HT 6` and `HT 7` belong to `CORE 3` .

**HT discrete CPU topology**

Elastic Compute Service Relationships between logical cores and physical cores: `HT 0` and `HT 4` belong to `CORE 0` . `HT 1` and `HT 5` belong to `CORE 1` . `HT 2` and `HT 6` belong to `CORE 2` . `HT 3` and `HT 7` belong to `CORE 3` . You can modify the CPU topologies of instances in the following instance families that use exclusive Intel processors: ecs.g6s-k10, ecs.g6s-k25, ecs.g6m-k10, and ecs.g6m-k25 ecs.g7s-k10, ecs.g7s-k25, ecs.g7m-k10, ecs.g7m-k25, ecs.g7x-k10, and ecs.g7x-k25

**Note**

CPU topologies of instances in other instance families belong to the HT continuous CPU topology by default and cannot be modified. After you change the CPU topology of an instance to an HT discrete CPU topology, you can perform only cold configuration change instead of hot configuration change on the instance.

**Configure and modify the CPU topology of an instance**

**Important**

If you want to modify the CPU topology of an instance to meet your business requirements, we recommend that you perform benchmark tests and performance evaluation to determine the most suitable mode before you modify the CPU topology.

**Configure the CPU topology when you create an instance**

In the following section, only the main parameters that are used to configure the CPU topology are described. For more information about other parameters, see Create an instance. Elastic Compute Service
**Specification**: Select an instance type that allows you to modify the CPU topology. In this
example, ecs.g7s-k25-c1m2.large is selected.
**HT Hyper-Threading Technology**: Turn on HT Hyper-Threading Technology.
**CPU Topology**: Select **HT Continuous CPU Topology** or **HT Discrete CPU Topology**
based on your business requirements.

**Note**

The following instance types are only examples. The actual supported instance types are subject to your environment.

**Modify the CPU topology of an existing instance**

After you stop an instance, you can modify its CPU topology when you modify the instance properties. For more information, see Modify the properties of an instance. Elastic Compute Service

**View the CPU topology of an instance**

You can view the information about the CPU topology in the Configurations section of the Instance Details tab. For more information, see View the details of an instance. Elastic Compute Service

#### Enable and disable release protection

**for instances**

You can enable release protection for Elastic Compute Service (ECS) instances on which your core business is run to prevent the instances from being accidentally released. This can prevent irreversible consequences caused by unexpected operations and delayed communication between team members. This topic describes how to enable and disable release protection for ECS instances and how to check whether release protection is enabled.

**Background information**

The release protection feature cannot prevent the automatic release of an instance that is triggered by specific reasons. The reasons include but are not limited to the following ones: The automatic release time that you set for the instance arrives. The instance does not comply with applicable security compliance policies. The instance was automatically created by Auto Scaling and is removed during subsequent scale-in events.

#### Enable and disable release protection for instances

**Scenario 1: Enable or disable release protection when you**

When you create an instance, release protection is disabled for the instance by default. You can manually enable release protection for the instance. This section describes how to enable release protection when you create an instance. For more information about other settings for creating an instance, see Create an instance by using the wizard.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **ECS Instances** page, click **Create Instance**.
5. In the **Basic Settings** step, configure the parameters based on your business
requirements and click **Next**.
6. In the **Network Settings** step, configure the parameters based on your business
requirements and click **Next**.
7. In the **System Configurations** step, turn on **Instance Release Protection**, configure
other parameters based on your business requirements, and then click **Next**. Elastic Compute Service
8. In the **Confirmation** step, confirm the configurations and click **Confirm Order**.

**Scenario 2: Enable or disable release protection for an existing**

You can enable or disable release protection for an instance by modifying the properties of the instance.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance that you want to manage, click the
icon in the **Actions** column, and then choose **Instance Settings > Change Release Protection**
**Settings**.
5. In the dialog box that appears, optionally select **Release Protection**.
6. Click **OK**.

**Scenario 3: Disable the release protection feature for multiple**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, select the instances for which you want to disable the release
protection feature and choose **More > Batch Disable Release Protection** in the lower part of the page.
5. In the **Disable Instance Release Protection dialog** box, confirm the instances and click
**Next**.
Elastic Compute Service The system filters out instances for which release protection is disabled.
6. In the Confirm step, click **Submit**.

**Check whether release protection is enabled for an instance**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **ECS Instances** page, use one of the following methods to view the details of an
instance: Find the instance that you want to view and click its ID in the **Instance ID/Name** column. Find the instance that you want to view and click **Manage** in the **Actions** column.
5. On the **Instance Details** page, view the **Release Protection** parameter in the **Other**
**Information** section.

#### Instance user data

The user data feature provided by Elastic Compute Service (ECS) allows you to customize the startup behaviors of instances and pass data into instances.

**Background information**

This feature is applicable to both Windows and Linux instances. You can use this feature to perform the following operations: Run scripts during instance startup. Pass user data as common data into an ECS instance for future reference. The user data feature can be used only when instances meet the following requirements: Network type: Virtual Private Cloud (VPC) Image: a system image or a custom image that is derived from the system image

| Windows | Linux |
|---|---|
| Windows Server 2016 64-bit Windows Server 2012 R2 64-bit Windows Server 2008 R2 64-bit | CentOS Ubuntu SUSE Linux Enterprise OpenSUSE Debian Alibaba Cloud Linux Alibaba Cloud Linux 3 64bit Note When you create an instance using the Alibaba Cloud Linux 3 64bit image, custom parameters are automatically deployed. You can also append more custom data. |

Elastic Compute Service Operating system: one of the operating systems listed in Supported operating systems Table 1. Supported operating systems
**Console**: You can modify the user data of instances in the console. The type of the
modified user data script determines whether the script needs to be re-executed. For example, if the `bootcmd` script in **Cloud Config** is modified for Linux instances, the script is automatically executed each time the instances are restarted.
**API**: You can also call API operations to work with instance user data. For more information,
see **CreateInstance** and **ModifyInstanceAttribute** in **ECS Developer Guide**. User data scripts for Linux instances are implemented based on the cloud-init architecture. The scripts are used to complete automated configurations of Linux instances. User data scripts are compatible with cloud-init.

**Description of user data scripts for Linux instances**

User data scripts for Linux instances are executed after the instances are started but before `/etc/init` is executed. By default, user data scripts for Linux instances can only be executed with root permissions.

**Note**

Only English characters are supported. If your data is Base64-encoded, select **Enter Base64 Encoded Information** .

**User-Data Script**

Description: the script that is used to customize configurations, such as a shell script. Elastic Compute Service Format: The first line must start with #! . Example: #!/bin/sh . Limit: The script including the first line is limited to 16 KB in raw form before it is Base64encoded. Frequency: The script is executed only when instances are started for the first time. Example:

```
#!/bin/sh
echo "Hello World. The time is now $(date -R)!" | tee /root/output10.txt
```

**Cloud Config Data**

Description: the predefined data that is used to configure services such as specifying yum repositories or importing SSH keys. Format: The first line must be #cloud-config . Limit: The script including the first line is limited to 16 KB in raw form before it is Base64encoded. Frequency: The script execution frequency varies based on the specific service. Example:

```
#cloud-config
apt: primary:
- arches: [default]
uri: http://us.archive.ubuntu.com/ubuntu/
```

**Include**

Description: The configuration content in the script can be saved as a text file and passed into cloud-init as a URL. Format: The first line must be #include . Limit: The script including the first line is limited to 16 KB in raw form before it is Base64encoded. Frequency: The script execution frequency varies based on the script type in the text file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/cloudconfig
```

**GZIP format**

Description: cloud-init limits the size of each user data script to 16 KB. If the size of a file exceeds 16 KB, you can compress the file before you pass it into the user data script. Format: The .gz file is passed into the user data script as a URL in #include . Frequency: The script execution frequency varies based on the script content contained in the GZIP file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/config.gz
```

**View the user data of a Linux instance**

Elastic Compute Service To view the user data of a Linux instance, run the following command in the instance:

```bash
curl http://100.100.100.200/latest/user-data
```

User data scripts for Windows instances are developed by Alibaba Cloud and can be used to initialize Windows instances. The following types of user data scripts for Windows instances are available: Batch processing program: The first line starts with `[bat]` . The script is limited to 16 KB in raw form before it is Base64-encoded. PowerShell script: The first line starts with `[powershell]` . The script is limited to 16 KB in raw form before it is Base64-encoded.

**Note**

Only English characters are supported. If your data is Base64-encoded, select **Enter Base64 Encoded Information** .

**View the user data of a Windows instance**

To view the user data of a Windows instance, run the following PowerShell command in the instance:

```
Invoke-RestMethod http://100.100.100.200/latest/user-data/
```

### Manage the instance recycle

**bin**

#### Set the retention period

When you put Elastic Compute Service (ECS) instances into the recycle bin, the instances enter a retention period. This topic describes how to set the retention period.

**Prerequisites**

Only the admin account can set the retention period.

**Background information**

When an instance enters a retention period, its computing resources (CPU and memory) are released, its elastic IP address is disassociated, but its storage resources are retained. When the retention period expires, the ECS instance and its storage resources are completely destroyed and cannot be recovered. The default retention period is three days. You can set an appropriate retention period of up to 30 days and 23 hours based on your business requirements. The retention period can be configured for the recycle bin instead of a specific instance.

**Important**

After you set the retention period, instances in the recycle bin are completely destroyed and cannot be recovered after the retention period expires. Elastic Compute Service

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, click **Recycle Bin**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Recycle Bin page, click **Set Retention Period**.
5. In the **Set Retention Period** dialog box, specify a period of time and click **OK**.

**Result**

You can view the retention period above the instance list on the Recycle Bin page.

#### Restore an instance

When you place Elastic Compute Service (ECS) instances into the recycle bin, the instances enter a retention period. During the retention period, you can restore the instance anytime based on your business requirements.

**Background information**

When instances are restored from the recycle bin, computing resources (vCPUs and memory) are automatically re-assigned to the instances. If the instances require elastic IP addresses (EIPs), you must manually associate EIPs with the instances. For more information, see the
**Associate an EIP with an ECS instance** topic in the **EIP User Guide**.

**Note**

When you delete instances to the recycle bin, their computing resources are automatically reclaimed. Your attempt to restore instances from the recycle bin may fail due to insufficient quotas or computing resources. Before you restore instances, make sure that your quotas and computing resources are sufficient.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, click **Recycle Bin**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Restore an instance from the recycle bin.
Use one of the following methods to restore the instance from the recycle bin: To restore a single instance, find the instance in the recycle bin and click **Restore** in the Actions column. In the message that appears, click **OK**. To restore one or more instances at a time, select the instances and click **Restore** in the lower-left corner of the page. In the message that appears, click **OK**.

#### Permanently delete instances

You can permanently delete the instances that you no longer need from the recycle bin. This topic describes how to permanently delete instances.

**Background information**

The instances that are permanently deleted cannot be restored. Make sure that your business is not interrupted before you permanently delete instances.

**Procedure**

1. Log on to the ECS console.
Elastic Compute Service
2. In the navigation pane on the left, click **Recycle Bin**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. In the instance list, view information about all instances in the retention period, including
the **instance ID, instance name**, **instance type**, and **automatic release time** of the instances.
5. Permanently delete instances from the recycle bin.
You can use one of the following methods to permanently delete instances: To delete a single instance, click **Permanently Delete** in the Actions column corresponding to the instance. In the message that appears, click **Delete**. To delete one or more instances at a time, select all instances that you want to delete, and then click **Permanently Delete** in the lower-left corner of the Instances page. In the message that appears, click **Delete**.

### Change the instance type

#### Change the instance type of an

**instance**

If the instance type of an Elastic Compute Service (ECS) instance does not meet your application requirements, you can change the instance type. This topic describes how to change the instance type of an instance.

**Prerequisites**

The instance whose instance type you want to change is in the **Stopped** state.

**Note**

Service interruptions may occur when you stop instances. We recommend that you stop instances during off-peak hours. The following limits apply when you change the instance type of an instance: When you change the instance type of an instance, the instance specifications, including the vCPU, memory, and internal bandwidth specifications, are changed together. These specifications cannot be separately changed. The instance types of the following families cannot be changed: Instance families equipped with local HDDs Instance families equipped with local SSDs ECS Bare Metal Instance families Super Computing Cluster (SCC) instance families FPGA

**Warning**

When you change the instance type of an instance, the underlying information such as CPU FLAGS of the instance may change and your application authorization codes may become invalid. Elastic Compute Service

**Billing**

After you change the instance type of an instance, you are charged based on the new instance type.

**Note**

Bills are generated only after the administrator configures billing rules in the operations center. For more information about the billing rules, see the **Create a billing**
**configuration** topic in **Apsara Uni-manager Operations Console User Guide** .

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose instance type you want to upgrade or downgrade, click the
icon in the **Actions** column, and then click **Upgrade/Downgrade**.
5. Optional. Select a service catalog and click **OK**.
The service management feature is used to manage and control specific specifications of specific services within an enterprise or an organization. This parameter is displayed only after you create and publish services that grant the current organization or user permissions to access **ECS instances**. For more information about the service management feature, see **Manage service catalogs** in **Apsara Uni-manager**
**Management Console User Guide**.
6. Change the instance type of the instance.

**Note**

The supported instance types that are displayed in the ECS console prevail. If a service whose **cloud resource** is **ECS instance** is created in service management: On the **Modify ECS Instance** page, select the desired instance type and click **Confirm**
**Order**.
If no service whose **cloud resource** is **ECS instance** is created in service management: On the **Modify ECS Instance** page, select the desired instance type and click **Submit**.
7. Restart the instance in the ECS console or by calling an API operation for the new instance
type to take effect. For more information, see the Start an instance or **StartInstance** topic in **ECS Developer**
**Guide**.

#### Perform a hot configuration change on

**an instance to change the instance type**

You can change the instance type of an Elastic Compute Service (ECS) instance to meet your application requirements for resources, including vCPUs and memory. Compared with the instance type change feature, the hot configuration change feature allows you to change the instance type of an ECS instance without stopping the instance.

**Prerequisites**

Elastic Compute Service The instance supports hot configuration changes and the **Enable Hot Configuration**
**Change** parameter is set to Yes when you create the instance. For more information, see
Create an instance.

**Note**

ECS instance types that support the hot configuration change feature are displayed in the ECS console.

**Billing**

After you perform a hot configuration change to change the instance type of an ECS instance, you are charged for the instance based on the new instance type.

**Note**

Bills are generated only after the administrator configures billing rules in the operations center. For more information about billing rules, see **Manage billing configurations** in
**Apsara Uni-manager Management Console User Guide** .
When you perform a hot configuration change to change the instance type of an ECS instance, the following limits apply: Only specific x86 instance types support the hot configuration change feature. The physical machine on which the instance to be changed is deployed must have sufficient CPU and memory resources to meet the specifications of the instance type to which you want to change. When you change the instance type of an ECS instance, the instance specifications, including the vCPU and memory, are changed together. You cannot change the number of vCPUs or the memory size separately. If the instance is created from a custom image that has been deleted, hot configuration changes are not supported. You can perform up to four consecutive hot configuration changes on an instance to increase its memory size. This limit does not apply to the CPU specifications. If you want to perform the fifth consecutive change, the change fails, and an error is reported. In this case, you must restart the instance to reset the hot configuration change count. If you enabled non-uniform memory access (NUMA) on physical machines in an ECS cluster, you can only perform hot configuration changes on the ECS instances that are created in the cluster in proof of concept (PoC) tests. Before you upgrade an ECS instance, log in to the instance and run the `free -m` command to check the amount of available memory resources. You can upgrade the instance only if the value in the `free` column in the command output is greater than or equal to the value calculated based on the following formula: 80 MB + N × 64 MB. If you perform a hot configuration change to upgrade an ECS instance that has insufficient available memory resources, an out of memory (OOM) error may occur on the instance and affect your business. Take note of the following items: 80 MB: the minimum amount of memory resources required to perform a hot configuration change to upgrade the instance type. N × 64 MB: the ratio of the amount of available memory resources to the amount of hotswap memory resources, which is indicated by the size value, is 1:64. When you upgrade an ECS instance to a different instance type, each additional GB of memory requires an additional 64 MB of available memory.

| Image platform | Image name |
|---|---|
| Aliyun | aliyun 2 1903 x86 64 20G alibase 20240628.vhd _ _ _ _ _ _ _ |
|  | aliyun 2 1903 x86 64 20G dengbao alibase 20240705.vhd _ _ _ _ _ _ _ _ |
|  | aliyun 3 x86 64 20G alibase 20241103.vhd _ _ _ _ _ _ |
|  | aliyun 3 x86 64 20G dengbao alibase 20241103.vhd _ _ _ _ _ _ _ |
|  | aliyun 3 x86 64 20G pro alibase 20241225.vhd _ _ _ _ _ _ _ |
|  | aliyun 3 x86 64 20G pro dengbao alibase 20241030.vhd _ _ _ _ _ _ _ _ |
|  | aliyun 3 x86 64 20G container optimized 20241226.vhd _ _ _ _ _ _ _ |
|  | aliyun 4 x86 64 20G alibase 20250728.vhd _ _ _ _ _ _ |
| Anolis | anolisos 8 8 x86 64 20G anck dengbao alibase 20231219.vhd _ _ _ _ _ _ _ _ _ |
|  | anolisos 8 9 x86 64 20G anck alibase 20240724.vhd _ _ _ _ _ _ _ _ |
| UOS | uos 20 1070a x86 64 20G alibase 20241129.vhd _ _ _ _ _ _ _ |
|  | uos 20 1070a x86 64 20G uefi alibase 20241119.vhd _ _ _ _ _ _ _ _ |
| Kylin | kylin v10 sp3 2403 x86 64 20G alibase 20241129.vhd _ _ _ _ _ _ _ _ |
|  | kylin v10 sp3 2403 x86 64 20G uefi alibase 20241119.vhd _ _ _ _ _ _ _ _ _ |
|  | nfs v4 g195 x86 64 20G alibase 20241119.vhd _ _ _ _ _ _ _ |
|  | kylinsec v3 3 9A x86 64 20G alibase 20250708.vhd _ _ _ _ _ _ _ _ |
| CentOS Stream | centos stream 9 x86 64 20G alibase 20241128.vhd _ _ _ _ _ _ _ |

Elastic Compute Service Only the following images support hot configuration changes:

| Ubuntu | ubuntu 20 04 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
|---|---|
|  | ubuntu 22 04 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
|  | ubuntu 24 04 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
| RockyLinux | rockylinux 8 10 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
|  | rockylinux 9 4 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
| AlmaLinux | almalinux 8 10 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
|  | almalinux 9 4 x86 64 20G alibase 20241115.vhd _ _ _ _ _ _ _ |
| SUSE | sles 15 sp6 x86 64 20G alibase 20240930.vhd _ _ _ _ _ _ _ |
| openSUSE | opensuse 15 6 x86 64 20G alibase 20240731.vhd _ _ _ _ _ _ _ |
| redHat | redhat 9 4 x86 64 20G alibase 20240711.vhd _ _ _ _ _ _ _ |

Elastic Compute Service

**Warning**

When you perform a hot configuration change on an ECS instance, the underlying information, such as CPU FLAGS, of the ECS instance may change, and your application authorization codes may become invalid.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Optional. Select a service catalog and click **OK**.
The service management feature is used to manage and control specific specifications of specific services within an enterprise or an organization. This parameter is displayed only after you create and publish services that grant the current organization or user permissions to access **ECS instances**. For more information about the service management feature, see **Manage service catalogs** in **Apsara Uni-manager**
**Management Console User Guide**.
5. Perform a hot configuration change based on your business requirements.
To perform a hot configuration change on a single instance, find the instance, click the icon in the **Actions** column, and then choose **Change Instance Configurations** >
**Hot Configuration Change**.
Elastic Compute Service To perform a hot configuration change on multiple instances at a time, select the instances and choose **More > Hot Configuration Change in Batches** in the lower part of the ECS Instances page.

**Important**

All instances on which you want to perform a hot configuration change at a time must be of the same instance type.
6. Perform a hot configuration change to change the instance type of the instance.
If a service whose **cloud resource** is **ECS instance** is created in service management: On the **Modify ECS Instance** page, select the desired instance type and click **Confirm**
**Order**.
If no service whose **cloud resource** is **ECS instance** is created in service management: On the **Modify ECS Instance** page, select the desired instance type and click **Submit**.
7. After the hot configuration change succeeds, the new instance type is displayed in the
console.

**Important**

If the hot configuration change fails and is not automatically rolled back, restart the instance by using the console or API to change the instance type. Fully assess the risks before you begin.

### Replace the operating

**system of an instance**

When you use an Elastic Compute Service (ECS) instance, you can replace the operating system based on your business requirements. This topic describes how to replace the operating system of an ECS instance.

**Prerequisites**

After the operating system of an instance is replaced, the original system disk is released, and its data is lost and cannot be restored. We recommend that you back up data before you replace an operating system. For information about how to create snapshots of disks to back up disk data, see Create a snapshot. The ECS instance is in the Stopped state. If the instance is not stopped, stop the instance. For more information, see Stop instances. Risks may arise when you replace the operating system of an instance. Before you perform this operation, take note of the following items: After you replace the operating system of an instance, a new system disk is assigned to the instance. The system disk ID changes, and the original system disk is released. Data stored on the original system disk is lost and cannot be restored. The category of the system disk, the IP addresses of the instance, and the media access control (MAC) addresses of the elastic network interfaces (ENIs) that are bound to the instance remain unchanged. After you replace the operating system of an instance, you must redeploy environments on the new system disk to run services.

| Parameter | Description |
|---|---|
| Image Type | Select an image type for the new operating system. Valid values: Public Image Custom Image Shared Image Enterprise Public Image |
| Image System and Image ID | Select an image and the image ID for the new operating system. |

Elastic Compute Service The snapshots of the original system disk cannot be used to roll back the new system disk, but can be used to create custom images. Take note of the following items about the snapshots based on the snapshot type: The manual snapshots of the original system disk are not automatically released. If **Delete Automatic Snapshots While Releasing Disk** is enabled for the original system disk, the automatic snapshots of the disk are automatically released along with the disk. If **Delete Automatic Snapshots While Releasing Disk** is not enabled for the original system disk, the automatic snapshots of the disk are automatically retained. If you want to replace Windows Server operating systems with Linux operating systems or replace Linux operating systems with Windows Server operating systems, take note of the following items: Make sure that the **hostname** of the instance meets the requirements of the replacement operating system, and delete invalid characters. For information about how to change the hostname, see Modify the attributes of an instance or the **ModifyInstanceAttribute** topic in **ECS Developer Guide**. If you want to replace the operating system of an instance with a Windows Server operating system, take note of the following items: Make sure that the system disk has at least 1 GiB of available space reserved. Otherwise, the instance may not be able to start after the operating system is replaced. If your instance is a non-I/O optimized instance, you cannot replace the operating system of the instance in the ECS console. You can only call the ReplaceSystemDisk operation to replace the operating system by using a specific Windows Server public image. For more information about **ReplaceSystemDisk**, see **ECS Developer Guide**. For more information, see Image overview.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance for which you want to replace the operating system, click the
icon in the **Actions** column, and choose **Disks and Image > Replace Operating System**.
5. In the **Replace Operating System** dialog box, specify the information of the new
operating system.

| System Disk Size | Specify the capacity of the new system disk based on your business requirements and the image limits. The new disk capacity must be greater than or equal to the original disk capacity and cannot exceed 2048 GiB. Linux Capacity limit (GiB): [Max{20, Original disk capacity}, 2048] Windows Capacity limit (GiB): [Max{40, Original disk capacity}, 2048] |
|---|---|

Elastic Compute Service
6. Confirm the operating system replacement operation.
If a service whose **Resources** value is **ECS** exists on the Service Management page, confirm the information about the new operating system and click **Confirm Order**. If no service whose **Resources** value is **ECS** exists on the Service Management page, confirm the information about the new operating system and click **OK**.
7. Restart the instance by using the ECS console or calling an API operation for the new
operating system to take effect. For more information, see Start an instance or the **StartInstance** topic in **ECS Developer**
**Guide**.

**What to do next**

After you replace the operating system of an ECS instance, you need to reset the login password of the instance in the following scenarios. For more information, see Reset the login password of an instance. You have selected **Support ecs-user user login** when you created the original instance, and the replacement operating system does not support ecs-user images. The original instance image has a preset password, and the replacement operating system supports any image.

### View the monitoring

**information of an instance**

You can view monitoring charts in the CloudMonitor console to learn about the running conditions of Elastic Compute Service (ECS) instances. This topic describes how to go to the CloudMonitor console to view the monitoring information of an ECS instance.

**Background information**

CloudMonitor provides real-time monitoring, alerting, and notification services for resources to protect your services and business. For more information, see **CloudMonitor > Overview** in the Apsara Uni-manager Management Console User Guide in the Apsara Stack Documentation Center.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. View the monitoring information of an instance in the **Monitoring** panel or on the
**Monitoring** tab.

| Item | Description |
|---|---|
| Monitoring type | The monitoring information of an ECS instance includes basic monitoring information and monitoring information about the instance operating system, GPUs, processes, disks, and networks. |
| Monitoring period | You can specify a period of time during which monitoring data is collected. Valid values: Hourly monitoring periods: 1 Hour, 3 Hours, 6 Hours, and 12 Hours Daily monitoring periods: 1 Day, 3 Days, 7 Days, and 14 Days Custom: Specify the start time and the end time to define a monitoring period based on your business requirements. You can specify the previous 5, 10, or 15 minutes as the monitoring period. |
| Monitoring metric | For information about monitoring metrics, see Cloud Monitor Service > Cloud service monitoring > Metrics in the Apsara Uni-manager M anagement Console User Guide in the Apsara Stack Documentation Center. Note By default, the average values of each monitoring metric are displayed. You can select Maximum or Minimum Value from the drop-down list of a monitoring metric to view the maximum or minimum values. |

Elastic Compute Service
**Monitoring** panel: In the instance list, find the ECS instance whose monitoring
information you want to view and click the icon in the **Monitoring** column.
**Monitoring** tab:
a. On the Instances page, click the instance ID in the **Instance ID/Name** column. b. On the Instance Details page, click the **Monitoring** tab. You can view the monitoring information that is described in the following table in the
**Monitoring** panel or on the **Monitoring** tab.

**Note**

You can also click **More** to go to the CloudMonitor console and view the details of the monitoring information of the instance. The following table describes the monitoring information.

### Add an instance to a security

**group**

You can add a created Elastic Compute Service (ECS) instance to multiple security groups and configure security group rules in the security groups to control network access for the ECS instance. Elastic Compute Service

**Background information**

Security groups are used as virtual firewalls to provide security isolation and control network access for ECS instances. Security groups determine whether the ECS instances in the same account that are deployed in the same virtual private cloud (VPC) and region can communicate with each other over the internal network. By default, ECS instances in the same security group can communicate with each other over the internal network, and ECS instances from different security groups are isolated from each other. If you want ECS instances from different security groups to communicate with each other over the internal network, authorize mutual access between the security groups. For more information about security groups, see Overview of security groups.

**Note**

For information about how to add multiple ECS instances to a security group, see Add ECS instances to a security group.

**Procedure**

**Important**

The security group to which you want to add an ECS instance must reside in the same VPC as the ECS instance.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance that you want to manage. In the **Actions** column, click **Manage**.

**Note**

Alternatively, click the ID of the ECS instance that you want to manage in the **Instance**
**ID/Name** column.
The **Instance Details** tab is displayed.
5. Choose **Security Groups > Security Groups** to view the list of security groups to which
the ECS instance is added.
6. Click **Add to Security Group**.
7. In the Add to Security Group dialog box, select a security group from the Security Group
drop-down list and click **OK**.

**Important**

Each ECS instance can be added to up to five security groups. After an ECS instance is added to a security group, the rules of the security group automatically apply to the instance.

### Change security groups

Elastic Compute Service If the security groups of an ECS instance do not meet your business requirements, you can change the security groups of the instance.

**Procedure**

1. Log on to the ECS console.
2.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance for which you want to change security groups, click the
icon in the **Actions** column, and then choose **Network and Security Group > Change Security**
**Group**.
You can also click **Change Security Group** on the **Security Groups** tab of the instance details page.
5. In the **Change Security Group** dialog box, select the security groups that you want to
associate with the instance and click **OK**. You can select up to 10 security groups. The selected security groups are of the same type (basic security group or advanced security group).

### Change the VPC of an ECS

**instance**

You may need to migrate an Elastic Compute Service (ECS) instance from one virtual private cloud (VPC) to another to meet changing business needs, organizational changes, or updated security policies. This operation helps you achieve network isolation, redesign your network architecture, or resolve IP address conflicts. You can change the VPC of the ECS instance without the need to change its region or zone.

**Important**

Changing the VPC causes a temporary service interruption. We recommend that you perform this operation during off-peak hours. Before you start, create a snapshot to back up your data. For more information, see Create a snapshot.

|  |  |  | Source VPC 192.168.0.0/16 |  |
|---|---|---|---|---|
| Zone Source vSwitch 172.16.50.0/24 ECS1 172.16.50.49 | Change VPC |  | Destination vSwitch 192.168.20.0/24 ECS1 192.168.20.56 |  |
|  | (Option |  | al) Clone the security group Destination Security Group |  |
|  |  | (Option | al) Clone the |  |

Elastic Compute Service

**Region**

**Impacts and risks**

**Service interruption**: The operation requires the instance to be in the **Stopped** state,
which interrupts services.
**Private IP address change:**:
The primary private IP address of the instance changes to a new IP address within the CIDR block of the destination vSwitch. You can either specify a new IP address or let the system automatically assign one. Applications or services with the original private IP address hard-coded, such as database connection strings, firewall whitelists, or other service configurations, will fail. You must manually update these configurations after changing the VPC. The public IP address of the instance remains unchanged.
**Network connection lost**: The instance will lose private network connectivity to all other
resources in the original VPC, such as ApsaraDB RDS instances, Server Load Balancer (SLB) instances, and other ECS instances.
**OS network configuration**: If the operating system (OS) of the instance is configured with
a static IP address, its network settings, including IP address and gateway, will not match the new network environment after the VPC change. This will prevent the instance from communicating over the network and may block remote access.

**Procedure**

**Step 1: Make preparations**

1. **Create a snapshot backup** To prevent data loss from accidental operations, create a
snapshot of the instance's system and data disks. These snapshots are required for the rollback procedure. For more information, see Create a snapshot.
2. **Stop the instance**
The instance must be in the **Stopped** state. If the instance is in the **Running** state, stop it. For more information, see Stop an instance.
3. **Perform prerequisite checks**
Elastic Compute Service
**Secondary Elastic Network Interfaces (ENIs)**: Detach any secondary ENIs attached
to the instance. For more information, see Unbind a secondary ENI from an instance.
**Additional IP addresses**: If the primary ENI has any secondary private IP addresses or
IPv6 addresses, you must first unassign the secondary private IP addresses or delete the assigned IPv6 address. For more information, see Unassign the secondary private IP address.
**SLB**: Remove the instance from any SLB server groups of which it is a member. For more
information, see the **Remove a backend server** topic in **SLB User Guide**.
**Custom route entries**: If the instance is configured in a custom route table, you must
delete the relevant route entries. For more information, see the **Manage custom route**
**tables and vSwitches** topic in **VPC User Guide**.
**High-availability virtual IP address (HAVIP)**: If the instance has an associated HAVIP,
you must disassociate it. For more information, see **HAVIPs > Disassociate an HAVIP**
**from an ECS instance** in **VPC User Guide**.
4. **Prepare destination network resources**
**VPC and vSwitch**: In the destination VPC, ensure that a VPC and a vSwitch exist in the
same zone as the ECS instance. For more information, see the **Create and manage**
**VPCs** topic in **VPC User Guide**.
**Security group**: In the destination VPC, create or identify the security group that you
want to associate with the instance. You can clone a security group to the destination VPC to copy existing rules. For more information, see Clone a security group.

**Step 2: Change the VPC**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance for which you want to change the VPC, click the
icon in the
**Actions** column, and then choose **Network and Security Group > Change VPC**.
You can also click the Instance Details tab, find the **Network Information** section, and click **Change VPC** on the right side of **VPC ID**.
5. Change the VPC:
i. **Make Preparations**: View the network information and notes before you make the change, and click **Next**. ii. **Select VPC**: Specify the **Destination VPC**, **Destination vSwitch**, and **Destination**
**Security Group** parameters, and click **Next**.
iii. (Optional) **Configure Primary Private IP Address**: You can specify a primary private IP address for the instance. The IP address must be within the CIDR block of the destination vSwitch and must not be in use. If you do not specify an IP address, the system automatically assigns one. Then, click **Submit**.
6. View the change result:
On the **Instance Details** tab, view the new VPC and vSwitch in the **Network Information** section.

**Note**

After the VPC is changed, the instance does not automatically start. You must manually start the instance. For more information, see Start an instance.

|  | R |
|---|---|

| Zone |  |
|---|---|
| VPC 172.16.0.0/12 Source vSwitch Destination vSwitch 172.16.10.0/24 172.16.50.0/24 Change vSwitch ECS1 ECS1 172.16.10.226 172.16.50.49 |  |

Elastic Compute Service

**FAQ**

**Error: A reverse access rule is configured for the instance. You**

**cannot modify the VPC.**

**Cause**: After you log in to an ECS instance by using Workbench, a reverse access rule is
automatically created for the instance.
**Solution**: Release the reverse access rule to prevent the ECS instance from being used in
other Alibaba Cloud services. Then, change the VPC again. If your instance generates a reverse access link by using Workbench, perform the following steps to release the reverse access link:
1. Log in to the Workbench console and check whether a reverse access link of the ECS
instance exists on the **Private Links** page. If a reverse access link exists, click **Release**
**Link** in the Actions column to release the link.
2. In the message that appears, click OK. After the reverse access link is released, change the
VPC of the instance again.

### Change the vSwitch of an

**ECS instance**

Change the vSwitch for an Elastic Compute Service (ECS) instance if the current vSwitch runs out of available IP addresses, or if you need to migrate the instance to a new CIDR block as part of a network architecture upgrade, or if you need to replan the CIDR block. This feature lets you move the primary Elastic Network Interface (ENI) of an ECS instance to another vSwitch within the same virtual private cloud (VPC) and zone.

**Impacts and risks**

**Service interruption**: The operation requires the instance to be in the **Stopped** state,
which interrupts services.
**Private IP address change:**:
Elastic Compute Service The primary private IP address of the instance changes to a new IP address within the CIDR block of the destination vSwitch. You can either specify a new IP address or let the system automatically assign one. Applications or services with the original private IP address hard-coded, such as database connection strings, firewall whitelists, or other service configurations, will fail. You must manually update these configurations after changing the vSwitch. The public IP address of the instance remains unchanged.
**OS network configuration**: If the operating system (OS) of the instance is configured with
a static IP address, its network settings, including IP address and gateway, will not match the new network environment after the vSwitch change. This will prevent the instance from communicating over the network and may block remote access.
**Access control**: If the source and destination vSwitches have different network access
control list (ACL) rules, you need to review and adjust them to ensure your applications function correctly. For more information, see the **Manage network ACL rules** topic in
**VPC User Guide**.
**Route configuration**: If your application relies on specific routing rules, the new vSwitch
may have a different routing configuration. Ensure connectivity by associating a custom route table with a vSwitch or configuring the necessary route entries. For more information, see the **Manage custom route tables and vSwitches** topic in **VPC User Guide**.

**Procedure**

**Step 1: Make preparations**

1. Stop the instance.
The instance must be in the **Stopped** state. If the instance is in the **Running** state, stop it. For more information, see Stop an instance.
2. Perform prerequisite checks.
**Multiple private IP addresses** : Detach any secondary elastic network interfaces (ENIs)
attached to the instance. For more information, see Unbind a secondary ENI from an instance.
3. Prepare the destination vSwitch: In the destination VPC, ensure that a vSwitch exists in the
same zone as the ECS instance. For more information, see the **Create and manage**
**vSwitches** topic in **VPC User Guide**.

**Step 2: Change the vSwitch**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance for which you want to change the vSwitch, click the
icon in the
**Actions** column, and then choose **Network and Security Group > Change vSwitch**.
You can also click the Instance Details tab, find the **Network Information** section, and click **Change vSwitch** on the right side of **vSwitch ID**.
5. Change the vSwitch:
i. Select a destination vSwitch. ii. (Optional) Specify the **Private IP Address** parameter. The private IP address must be within the CIDR block of the destination vSwitch. If you do not specify this parameter, an available primary private IP address is automatically assigned.
6. View the change result:
Elastic Compute Service On the **Instance Details** tab, view the new vSwitch in the **Network Information** section.

**Note**

After the vSwitch is changed, the instance does not automatically start. You must manually start the instance. For more information, see Start an instance.

### Change the private IP

**address of an instance**

Each instance is assigned a private network interface and associated with a private IP address. You can change the private IP address of an instance. The new private IP address must be within the CIDR block of the vSwitch to which the instance is connected and must not be in use by another instance.

**Prerequisites**

The instance is in the **Stopped** state.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage. In the **Actions** column, click the
icon and then choose **Network and Security Group > Change Private IP Address**.
5. Enter a new private IP address.
The new private IP address must be within the CIDR block of the vSwitch to which the instance is connected. The IP address must not be in use by another instance or be reserved for specific purposes. For example, if the CIDR block of the vSwitch is 192.168.1.0/24, you can use an IP address in the range of 192.168.1.1 to 192.168.1.254. The first address 192.168.1.0 is reserved to identify the subnet itself, and the last address 192.168.1.255 is reserved as the broadcast address. You can use neither of the first address and the last address.
6. Click **OK**.

### Assign an IPv6 address to an

**instance**

Compared with IPv4 addresses, IPv6 addresses are more sufficient and allow more types of devices to access the Internet. If your network environment supports IPv6, you can assign IPv6 addresses to exiting Elastic Compute Service (ECS) instances. This topic describes how to assign an IPv6 address to an ECS instance.

**Prerequisites**

The vSwitch and virtual private cloud (VPC) of the ECS instance are associated with an IPv6 CIDR block. For more information, see **Create an IPv6 VPC** in the **Apsara Stack VPC**
**User Guide**.
Elastic Compute Service The instance family of the ECS instance supports IPv6.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance to which you want to assign an IPv6 address.
Click the icon in the **Actions** column and choose **Network and Security Group >**
**Manage Secondary Private IP Addresses**.
5. In the **Manage Secondary Private IP Addresses** dialog box, click **Assign IP Address**
below the **IPv6 Address** parameter.

**Note**

Specific instance families do not support IPv6.
6. Enter an IPv6 address and click **OK**.

**Note**

The fixed part of the IPv6 address is rounded up from the subnet mask of the private IPv6 CIDR block. If you do not specify an IPv6 address, the system automatically allocate one.

**Result**

After the configuration is complete, you can click the ID of the instance to go to the **Instance**
**Details** page and view the **IPV6** parameter to check whether an IPv6 address is assigned to
the instance.

### Export a list of instances

You can export a list of Elastic Compute Service (ECS) instances based on your business requirements in the ECS console and download and save the list only as a `.xlsx` file to your computer.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, resource group, and region.
4. In the ECS instance list, select one or more instances that you want to export, and then
click the icon in the upper-right corner of the instance list.

| Parameter | Description |
|---|---|
| Export Data by Scope | All: export a list of all ECS instances. Selected Data: export a list of specific ECS instances. |
| Columns to Export | Select the columns that you want to export. You must select Instance ID/Name. Note If you select "Network Address", the exported Excel file contains only the primary private IP address of the primary network interface card, but the secondary private IP addresses of the primary network interface card or the IP addresses of secondary network interface cards are not contained. If you select "IPv6 Address", the exported Excel file contains only the IPv6 address of the primary network interface card, but the IPv6 addresses of secondary network interface cards are not contained. |

| Number of ECS instances | Download operation | Exported file |
|---|---|---|

Elastic Compute Service

**Note**

If you want to export all ECS instance information, click the icon in the upper-right corner of the instance list.
5. In the **Export** dialog box, configure the parameters to specify the scope of the instance list
that you want to export.
6. Click **OK**.
To prevent download tasks from timing out due to a large amount of data, if the number of instances is small, the system automatically downloads the file on the current page. If the number of instances is large, you must obtain the file from the download center. Details:

**Important**

The default threshold is 500 instances. You can contact Alibaba Cloud technical support to modify the threshold based on your business requirements.

| ≤ 500 | No operation is required. The system automatically exports instance data and downloads the file to your computer. | The exported file contains the following information: File name: ecs instance XXX _ _ File format: .xlsx File content: instance IDs, instance names, operating systems, instance status, instance descriptions, regions, organizations, resource sets, and zones |
|---|---|---|
| > 500 | i. In the The report export task is created. dialog box, click Go to Download Center. ii. On the Download Report page, find the target report in the task list and click Download Report in the Actions column. The system automatically exports instance data and downloads the file to your computer. |  |

| 36 |  | > | Document Version: 2026062 |
|---|---|---|---|

Elastic Compute Service

### Manage NVIDIA drivers

#### Installation guideline for NVIDIA

**drivers**

If drivers are not configured for your GPU-accelerated instances, you must install NVIDIA drivers on your instances. The driver types that you can install on the instances may vary based on the scenarios and instance types. This topic describes how to select GPUaccelerated instance types during instance creation and install NVIDIA drivers on GPUaccelerated instances in different scenarios.

**GPU-accelerated instance types**

Select suitable GPU-accelerated instance types during instance creation. For information about GPU-accelerated instance types, see the **ECS Instance Families & Instance Types**.

**Note**

You can manage GPU-accelerated instances in the same manner that you manage non-GPU-accelerated instances, except for the drivers that are required by GPUaccelerated instances. You can install the following NVIDIA drivers on GPU-accelerated instances: GPU driver: drives physical GPUs. GRID driver: accelerates graphics processing. vGPU-accelerated instances, such as vgn6i instances, use vGPUs. You can install only GRID drivers on vGPU-accelerated instances. Specific GPU-related features may be unavailable for the vGPU-accelerated instances because NVIDIA GRID licenses are not activated for the GPUs that the instances use. You must install GRID drivers and activate GRID licenses on the instances to use the GPU-related features. The following table describes the driver types that you can install on vGPU-accelerated instances for different scenarios.

| Operating system | Driver type | Recommended scenario | References |
|---|---|---|---|
| Windows Server | GRID drivers | Graphics computing scenarios, such as Open Graphics Library (OpenGL) and Direct3D scenarios | Install a GRID driver on a GPU-accelerated Windows instance |
| Linux, such as Alibaba Cloud Linux, CentOS, Ubuntu, or SUSE Linux | GRID drivers | Common computing scenarios, such as deep learning and AI | Install a GRID driver on a vGPU-accelerated Linux instance |

| Operating system | Driver type | Recommended scenario | References |
|---|---|---|---|
| Linux, such as Alibaba Cloud Linux, CentOS, Ubuntu, or SUSE Linux | GPU drivers | Common computing scenarios, such as deep learning, AI, and scientific computing | Install a GPU driver on a GPU-accelerated compute- optimized Linux instance |
|  | GPU drivers | Graphics computing scenarios, such as OpenGL and Direct3D scenarios | Install a GPU driver on a GPU-accelerated compute- optimized Linux instance |
| Windows Server | GPU drivers | Common computing scenarios, such as deep learning, AI, and scientific computing | Install a GPU driver on a GPU-accelerated compute- optimized Windows instance |
|  | GRID drivers | Graphics computing scenarios, such as OpenGL and Direct3D scenarios | Install a GRID driver on a GPU-accelerated Windows instance |

Elastic Compute Service

**Install drivers on GPU-accelerated compute-optimized**

The following table describes the driver types that you can install on GPU-accelerated compute-optimized instances for different scenarios.

#### Install a GPU driver

##### Install a GPU driver on a GPU-accelerated

**compute-optimized Linux instance**

After you create a GPU-accelerated compute-optimized instance from an image for which a GPU driver is not pre-installed, install a GPU driver to use the instance. This topic describes how to install a GPU driver on a GPU-accelerated compute-optimized Linux instance.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance.

**Background information**

Elastic Compute Service GPU-accelerated instances support only GPU drivers that are suitable for the operating systems of the instances. This topic describes how to install a GPU driver on a GPUaccelerated compute-optimized Linux instance.

**Note**

If your GPU-accelerated compute-optimized instance runs Windows, perform the operations that are described in Install a GPU driver on a GPU-accelerated computeoptimized Windows instance to install a GPU driver on the instance.

**Procedure**

1. Download a GPU driver.
i. Visit the NVIDIA Driver Downloads page on the NVIDIA official website.

**Note**

For information about how to install and configure NVIDIA drivers, see NVIDIA Driver Installation Quickstart Guide.

| Filter | Description | Example |
|---|---|---|
| Product Type Product Series Product | Configure Product Type, Product Series, and Product based on the GPUs with which your GPU-accelerated compute- optimized instance is equipped. For information about how to view instance specifications, see View instance information. For information about the GPUs that are supported by each instance type, see the Heterogeneous computing and heterogeneous ECS Bare Metal Instance families topics in the ECS Instance Families and Instance Types | Data Center / Tesla P-Series Tesla P100 |
| Operating System | Select a Linux operating system version based on the image of the instance. If the Operating System drop-down list does not contain the operating system that your instance runs, click Show All Operating Systems in the lower part of the drop-down list. If you cannot find a Linux version that matches the image of the instance, select Linux 64-bit. | Linux 64-bit |
| CUDA Toolkit | Select a CUDA Toolkit version. | 11.2 |
| Language | Select a language for the driver. | Chinese (Simplified) |
| Recommended/B eta | By default, All is selected. You can use the default setting. | All |

Elastic Compute Service ii. Configure filters and click **SEARCH** to search for a driver that is suitable for your instance. The following table describes the filters. Elastic Compute Service iii. In the search result, find the driver version that you want to download, and then click the driver name. iv. On the details page of the driver, click **Download**. On the **Download** page, right-click
**Download** and select **Copy link address**.
2. Connect to the instance.
For more information, see Instance connecting overview.
3. Run the `wget` command that contains the download link address that you copied in **Step**
1 to download the driver installation package. Sample command:

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

**Important**

Make sure that the version of the kernel-devel package is the same as the version of the kernel. Otherwise, a compilation error occurs when you install RPM Package Manager for your driver. Check the version number of kernel-* in the command output before you download kernel-devel. In the preceding command output, the version number of the kernel is 3.10.0-1062.18.1.el7.x86_64. Elastic Compute Service ii. Grant permissions and install the GPU driver. In this example, a Linux 64-bit driver package in the .run format is downloaded. Example: NVIDIA-Linux-x86_64-xxxx.run. Run the following commands to grant permissions on the GPU driver and install the GPU driver:

```
chmod +x NVIDIA-Linux-x86_64-xxxx.run sh NVIDIA-Linux-x86_64-xxxx.run
```

iii. Run the following command to check whether the driver is installed:

```
nvidia-smi
```

The following command output indicates that the GPU driver is installed. iv. Install NVIDIA Fabric Manager. Make sure that the version of NVIDIA Fabric Manager matches your driver version. You must install an NVIDIA Fabric Manager version that matches your driver version only for ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, and ecs.sccgn7ex instances. Otherwise, you cannot use the instances as expected.

**Important**

If your instance is a GPU-accelerated compute-optimized instance that does not belong to the ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, or ecs.sccgn7ex instance family, skip this step. Elastic Compute Service a. Install NVIDIA Fabric Manager. You can install NVIDIA Fabric Manager by using the source code or an installation package. The commands that are required to install NVIDIA Fabric Manager vary based on the instance operating system. The following example shows how to install driver version 460.91.03 on CentOS 7.x and CentOS 8.x. Set `driver_version` to the driver version that you downloaded in **Step 1**.

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

Elastic Compute Service c. Run the following command to check whether NVIDIA Fabric Manager is installed:

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

**Important**

If your instance is a GPU-accelerated compute-optimized instance that does not belong to the ecs.ebmgn7, ecs.ebmgn7e, ecs.ebmgn7ex, or ecs.sccgn7ex instance family, skip this step. Elastic Compute Service Elastic Compute Service a. Install NVIDIA Fabric Manager. You can install NVIDIA Fabric Manager by using the source code or an installation package. The following example shows how to install driver version 460.91.03 on Ubuntu 16.04, Ubuntu 18.04, or Ubuntu 20.04. Set `driver_version` to the driver version that you downloaded in **Step 1**.

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

Elastic Compute Service b. Run the following commands to start NVIDIA Fabric Manager:

```bash
systemctl enable nvidia-fabricmanager systemctl start nvidia-fabricmanager
```

c. Run the following command to check whether NVIDIA Fabric Manager is installed:

```bash
systemctl status nvidia-fabricmanager
```

The following command output indicates that NVIDIA Fabric Manager is installed.

##### Install a GPU driver on a GPU-accelerated

**compute-optimized Windows instance**

After you create a GPU-accelerated compute-optimized Windows instance, no GPU driver is automatically installed on the instance. Download a GPU driver from the NVIDIA official website and install the driver on the instance to use the instance. This topic describes how to install a GPU driver on a GPU-accelerated compute-optimized Windows instance.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance.

**Background information**

GPU-accelerated instances support only GPU drivers that are suitable for the operating systems of the instances. This topic describes how to install a GPU driver on a GPUaccelerated compute-optimized Windows instance. If your GPU-accelerated computeoptimized instance runs Linux, perform the operations that are described in Install a GPU driver on a GPU-accelerated compute-optimized Linux instance to install a GPU driver on the instance.

**Procedure**

1. Connect to the instance.
For more information, see Instance connecting overview.
2. On the remote desktop, visit the NVIDIA Driver Downloads page on the NVIDIA official
website.
3. Configure filters and click **SEARCH** to search for a driver that is appropriate for your
instance.

| Filter | Description | Example |
|---|---|---|
| Product Type Product Series Product | Configure Product Type, Product Series, and Product based on the GPUs with which your GPU-accelerated compute-optimized instance is equipped. For information about how to view instance specifications, see View instance information. For information about the GPUs that are supported by each instance type, see the ECS Instance Families & Instance Types. | Data Center / Tesla P-Series Tesla P100 |
| Operating System | Select a Windows operating system version based on the image of the instance. | Windows 10 64-bit |
| Windows Driver Type | Select a driver type. | Standard |
| CUDA Toolkit | Select a CUDA Toolkit version. | 11.2 |
| Language | Select a language for the driver. | Chinese (Simplified) |
| Recommended/B eta | By default, All is selected. You can use the default setting. | All |

Elastic Compute Service The following table describes the filters.
4. In the search result, find the driver version that you want to download, and then click the
driver name. Elastic Compute Service
5. On the details page of the driver, click **Download**. On the **Download** page, click
**Download**.
6. After the driver is downloaded, open the folder in which the driver installation package is
stored. Double-click the installation package and install the driver as prompted.

**Note**

Windows Remote Desktop Protocol (RDP) does not support applications, such as DirectX and Open Graphics Library (OpenGL) applications, for Windows instances on which the installed GPU drivers are in effect. In this case, you must install the Virtual Network Console (VNC) service and client or use protocols such as PC over IP (PCoIP) and XenDesktop HDX 3D that support the applications. After you install the driver, you can open Device Manager. In the left-side navigation pane, click Display adapters to check whether the driver is installed. If the driver appears, the driver is installed.

#### Install a GRID driver

##### Install a GRID driver on a vGPU-

**accelerated Linux instance**

If you create vGPU-accelerated instances, you must install GRID drivers on the instances. If NVIDIA GRID licenses are not activated for the GPUs that are used by GPU-accelerated instances, GPU-related features do not take effect on the instances. You must obtain and activate the GRID licenses to use the features. This topic describes how to install a GRID driver on a vGPU-accelerated Linux instance, activate a GRID license, and test the GRID driver. In the examples, an ecs.vgn6i instance that runs Ubuntu 16.04 64-bit is used.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance. A remote connection tool, such as VNC Viewer, is installed on your computer. A GRID license and a GRID driver installation package are obtained. Elastic Compute Service

**Note**

The GRID driver version must be suitable for the instance type and region of your vGPUaccelerated instance.

**Background information**

If you use a GPU-accelerated compute-optimized Linux instance, we recommend that you install a GPU driver on the instance. For more information, see Install a GPU driver on a GPUaccelerated compute-optimized Linux instance.
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

**Note**

If the following code is already added to the file, skip this step.

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

| vGPU software version | GRID driver version | Latest CUDA version supported |
|---|---|---|
| 13.5 | 470.161.03 | 11.4 |
| 13.1 | 470.82.01 | 11.4 |
| 12.3 | 460.91.03 | 11.2 |

Elastic Compute Service

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

**Important**

If a CUDA version is returned after you run the `nvidia-smi` command on a GPUaccelerated instance, the version is the latest CUDA version that is supported by the GRID driver. However, this does not indicate that the CUDA version is installed on the instance. The GRID driver does not include CUDA. You must install the CUDA Toolkit.

| 9.4 | 430.99 | 10.1 |
|---|---|---|

Elastic Compute Service
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

ii. Run the lspci | grep NVIDIA command to query the GPU BusID. In this example, the GPU BusID is `00:07.0` .

|  | "Section Device" |
|---|---|
| BusID "PCI:0:7:0" |  |

Elastic Compute Service iii. Configure the X Server environment and reboot the system. a. Run the `nvidia-xconfig --enable-all-gpus --separate-x-screens` command. c. Run the `reboot` command to restart the system.
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
For more information, see Create a security group rule.
7. On your computer, start the VNC application such as VNC Viewer, enter `public IP address`
`of the instance: 5900` to connect to the instance, and then go to a K Desktop Environment (KDE) desktop.
8. Run the `glxinfo` command to view the configurations that are supported by the current
NVIDIA GRID driver. i. Start another SSH session on a client. ii. Run the `export DISPLAY=:1` command. Elastic Compute Service iii. Run the glxinfo –t command to list the configurations that are supported by the current GRID driver.
9. Run the `glxgears` command to test the GRID driver.
i. On the KDE desktop, right-click anywhere and select **Run Command**. ii. Run the `glxgears` command to start the testing application. If a window that is shown in the following figure appears, the GRID driver works as expected.

##### Install a GRID driver on a GPU-

**accelerated Windows instance**

If you want to run graphics-intensive workloads such as OpenGL and Direct3D on a GPUaccelerated compute-optimized Windows instance or a vGPU-accelerated Windows instance, you must install a GRID driver on the instance. This topic describes how to install a GRID driver and activate a GRID license.

**Prerequisites**

The instance is connected to the Internet. If the instance is not connected to the Internet, you cannot download installation files to the instance. You can install an FTP client on the instance to transfer the required installation file to the instance. A remote connection tool is installed on your computer. A GRID license and a GRID driver installation package are obtained.

**Note**

The GRID driver version must be suitable for the instance type and region of your vGPU-accelerated instance.

**Background information**

Elastic Compute Service The procedure for installing a GRID driver on a GPU-accelerated Windows instance is the same as the procedure for installing a GRID driver on a vGPU-accelerated Windows instance. This topic describes how to install a GRID driver and activate a GRID license on a vGPUaccelerated instance. In this example, a vgn6i instance that runs Windows Server 2019 is used.

**Procedure**

1. Connect to the instance.
For more information, see Connect to a Windows instance from a Windows computer by using Remote Desktop.
2. Install the GRID driver that you obtained.
i. Double-click the installation package. In the dialog box that appears, click **OK**. The package is automatically decompressed. Elastic Compute Service ii. In the **NVIDIA Installer** dialog box, click **AGREE AND CONTINUE**. Elastic Compute Service iii. Accept the default settings and click **NEXT**. Elastic Compute Service iv. After the driver is installed, click **RESTART NOW**.
3. After you restart the instance, connect to the instance and check whether the GRID driver is
installed. i. Connect to the instance. For more information, see Connect to a Windows instance from a Windows computer by using Remote Desktop.

**Important**

Do not use VNC to connect to the GPU-accelerated instance in the Elastic Compute Service (ECS) console. VNC cannot render GPU output, which results in a black screen. ii. On your Windows desktop, move the pointer over the icon, right-click the icon, and then click **Device Manager**. Elastic Compute Service iii. In the **Device Manager** dialog box, click **Display adapters** and check whether the GRID driver appears. In this example, an **NVIDIA GRID T4-8Q** driver appears. The following figure shows that the driver is installed.
4. Add a license server and activate the license.
i. On your Windows desktop, right-click anywhere on the screen and select **NVIDIA**
**Control Panel**.
Elastic Compute Service ii. In the left-side navigation pane of the **NVIDIA Control Panel** dialog box, choose
**Licensing > Manage License**.
Elastic Compute Service iii. On the **Manage License** page, enter the IP address and port number of the license server that you obtained and click **Apply**. Reopen the **NVIDIA Control Panel** dialog box. If the message that is shown in the following figure appears, the license is activated.

#### Uninstall an NVIDIA driver

##### Uninstall a GPU driver

You can uninstall a GPU driver from a GPU-accelerated instance. The commands that you run to uninstall a GPU driver vary based on the installation method of the driver and the operating system of the instance.

**Background information**

You can use GPU-accelerated instances only if the required drivers are installed on the instances. If you uninstall a driver from your instance, install another driver that is suitable for the instance type and operating system to ensure that the instance runs as expected. For more information, see Update an NVIDIA driver. If a GPU driver is automatically installed when you create a GPU-accelerated instance, the operations that you perform to uninstall the driver vary based on the operating system of the instance: Ubuntu: Uninstall a GPU driver by using a .deb package. CentOS or SUSE Linux: Uninstall a GPU driver by using a .run package. For information about how to uninstall GPU drivers from different operating systems, see the following sections in this topic: Elastic Compute Service Windows: Linux:

**Note**

To uninstall a GPU driver from a GPU-accelerated instance that runs Linux, you must log on to the instance as the `root` user. If you are a regular user, run the `sudo` command to obtain the permissions of the `root` user before you proceed. In this example, a GPU-accelerated compute-optimized gn6i instance that runs Windows Server 2019 is used.
1. Connect to the instance.
For more information, see Overview.
2. In the lower-left corner of a Windows desktop, click the
icon and then click **Control**
**Panel**.
Elastic Compute Service
3. In the **Control Panel**, click **Uninstall a program**.
4. Right-click the GPU driver that you want to uninstall and select **Uninstall/Change**.
5. In the **NVIDIA Uninstaller** dialog box, click **UNINSTALL**.
6. After you uninstall the driver, click **RESTART NOW**.
When you restart the instance, the GPU driver is uninstalled. If you used a .deb installation package to install a GPU driver on an instance that runs Ubuntu, we recommend that you perform the following operations to uninstall the GPU driver. In this example, NVIDIA driver 410.104, CUDA 10.0.130, and cuDNN 7.5.0 are used.
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

Elastic Compute Service If you used a .run installation package to install a GPU driver on an instance that runs Ubuntu, we recommend that you perform the following operations to uninstall the GPU driver:
1. Run the following command to uninstall the GPU driver:

```
/usr/bin/nvidia-uninstall
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```
/usr/local/cuda/bin/cuda-uninstaller rm -rf /usr/local/cuda-10.0
```

**Note**

The commands that you run to uninstall a driver may vary based on the CUDA version. If you cannot find the cuda-uninstaller file, check whether a file whose name starts with uninstall_cuda exists in the /usr/local/cuda/bin/ directory. If a file whose name starts with uninstall_cuda exists in the directory, replace cuda-uninstaller in the preceding command with the name of the file.
3. Run the following command to restart the instance:

```
reboot
```

If you used a .run installation package to install a GPU driver on an instance that runs CentOS, we recommend that you perform the following operations to uninstall the GPU driver. In this example, NVIDIA driver 410.104, CUDA 10.0.130, and cuDNN 7.5.0 are used.
1. Run the following command to uninstall the GPU driver:

```
/usr/bin/nvidia-uninstall
```

2. Run the following commands to uninstall the CUDA and cuDNN libraries:

```
/usr/local/cuda/bin/cuda-uninstaller rm -rf /usr/local/cuda-10.0
```

**Note**

The commands that you run to uninstall a driver may vary based on the CUDA version. If you cannot find the cuda-uninstaller file, check whether a file whose name starts with uninstall_cuda exists in the /usr/local/cuda/bin/ directory. If a file whose name starts with uninstall_cuda exists in the file, replace cuda-uninstaller in the preceding command with the name of the file.
3. Run the following command to restart the instance:

```
reboot
```

If you used a .rpm installation package to install a GPU driver on an instance that runs CentOS 7, we recommend that you perform the following operations to uninstall the GPU driver:
1. Run the following commands to uninstall the GPU driver:

```bash
yum remove xorg-x11-drv-nvidia nvidia-kmod cuda-drivers yum remove nvidia-diag-driver-local-repo-rhel7-410.104
```

Elastic Compute Service
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

##### Uninstall a GRID driver

This topic describes how to uninstall a GRID driver from a GPU-accelerated instance. The procedure for uninstalling a GRID driver may vary based on the instance operating system.

**Background information**

You can use GPU-accelerated instances only if required drivers are installed on the instances. If you uninstall a driver from your instance, install another driver that is suitable for the instance type and operating system to ensure that the instance runs as expected. For more information, see Update an NVIDIA driver. The following section describes how to uninstall a GRID driver from a vGPU-accelerated Windows instance. In this example, a vgn6i instance that runs Windows Server 2019 is used. Elastic Compute Service
1. Connect to the instance.
For more information, see Overview.
2. In the lower-left corner of a Windows desktop, click the
icon and then click **Control**
**Panel**.
3. In the **Control Panel**, click **Uninstall a program**.
Elastic Compute Service
4. Right-click the GRID driver that you want to uninstall and select **Uninstall/Change**.
5. In the **NVIDIA Uninstaller** dialog box, click **UNINSTALL**.
Elastic Compute Service
6. After you uninstall the driver, click **RESTART NOW**.
When the instance is restarted, the GRID driver is uninstalled. The following section describes how to uninstall a GRID driver from a vGPU-accelerated Linux instance. In this example, a vgn6i instance that runs Ubuntu 18.04 is used.
1. Connect to the instance by using VNC.
For more information, see Connect to an instance by using a VNC management terminal.
2. Uninstall the GRID driver by following the on-screen instructions.
i. Run the following command to uninstall the driver:

```
nvidia-uninstall
```

ii. If you are asked whether to back up the X configuration file as shown in the following figure, we recommend that you accept the default value `NO` and press the Enter key.

**Note**

The command output may vary based on the operating system. Select a value based on the actual scenario. Elastic Compute Service iii. The following command output indicates that the driver is uninstalled. Click **OK** and press the Enter key.

#### Update an NVIDIA driver

If your NVIDIA driver version is not suitable for your scenario or if your GPU-accelerated instance becomes unavailable after you install an incorrect NVIDIA driver type or version, you can perform an NVIDIA driver update by uninstalling the current driver and then installing the required driver. This topic describes how to uninstall and install NVIDIA drivers on different operating systems.

**Procedure**

1. Uninstall an NVIDIA driver.
To uninstall your NVIDIA driver, perform the operations that are described in the following topics based on the driver type:
2. Install a new NVIDIA driver.
The operations that you must perform to install an NVIDIA driver vary based on the driver type. To install a GPU driver on an instance, perform the operations that are described in the following topics based on the operating system of the instance:

##### Install a GPU driver on a GPU-accelerated compute-optimized Linux instance

##### Install a GPU driver on a GPU-accelerated compute-optimized Windows instance

To install a GRID driver on an instance, perform the operations that are described in the following topics based on the operating system of the instance:

##### Install a GRID driver on a vGPU-accelerated Linux instance

##### Install a GRID driver on a GPU-accelerated Windows instance

**Important**

vGPU-accelerated instances support only GRID driver versions that are compatible with their instance types. If you install a GRID driver version that is incompatible with the instance type of a vGPU-accelerated instance, the instance becomes unavailable. Before you install a GRID driver on a vGPUaccelerated instance, make sure that the driver version is compatible with the instance type.

### Super computer clusters

#### Overview of SCCs

This topic describes the features of Super Computing Cluster (SCC) instance families in Elastic Compute Service (ECS) and the instance types in SCC instance families. This topic also provides a comparison between SCCs, physical machines, and virtual machines.

**Introduction**

| Category | Feature | SCC | Physical machine | Virtual machine |
|---|---|---|---|---|
| Automated O&M | Delivery within minutes | Y | N | Y |
| Calculation | Zero performance loss | Y | Y | N |
|  | Zero feature loss | Y | Y | N |
|  | Zero resource contention | Y | Y | N |
|  | Compatibility with ECS disks | Y | N | Y |
|  | Boot from system disks | Y | N | Y |

Elastic Compute Service SCC is developed based on ECS Bare Metal Instance and uses high-speed Remote Direct Memory Access (RDMA) based interconnections to significantly improve the network performance and acceleration ratio of large-scale clusters. SCC provides all benefits of ECS Bare Metal Instance and high-bandwidth, low-latency networks. SCC is applicable to scenarios such as high-performance computing (HPC), AI, machine learning, scientific and engineering computing, data analytics, and audio and video processing. In SCCs, nodes (ECS instances of SCC instance types) are connected over highbandwidth, low-latency RDMA networks to ensure the high parallelism of applications in areas such as high-performance computing, artificial intelligence, and machine learning. RDMA over Converged Ethernet (RoCE) networks rival InfiniBand networks in terms of connection speed and can support more Ethernet-based applications. SCC can work with ECS to provide ultra-high-performance parallel computing resources for Elastic High Performance Computing (E-HPC) to achieve cloud-based high-performance computing. For information about E-HPC, see **What is E-HPC?** in E-HPC User Guide in the Apsara Stack Documentation Center.

**Note**

SCCs are dedicated to HPC scenarios. To use SCCs, the hyper-threading feature must be disabled. However, the instance type is still calculated based on hyper-threading being enabled. Therefore, the number of CPU cores displayed in the operating system (GuestOS) is half of the defined instance type.

**Comparison of instance types**

The following table compares the features of SCCs, physical machines, and virtual machines. In the table, Y indicates that the feature is supported, N indicates that the feature is not supported, and N/A indicates that the feature is not applicable.

| User Guide·Instances |  |  |  |  |
|---|---|---|---|---|
| Storage |  |  |  |  |
|  | Quick reset of system disks | Y | N | Y |
|  | Use of ECS images | Y | N | Y |
|  | Cold migration between physical and virtual machines | Y | N | Y |
|  | No need to install an operating system | Y | N | Y |
|  | No need for local RAIDs, and better protection of data in disks | Y | N | Y |
| Network: | Compatibility with virtual private clouds (VPCs) | Y | N | Y |
|  | No communication bottlenecks between physical and virtual machine clusters in VPCs | Y | N | Y |
| Management | Compatibility with existing ECS management systems | Y | N | Y |
|  | Consistent user experience on features, such as Virtual Network Computing (VNC), with that on virtual machines | Y | N | Y |
|  | Out-of-band (OOB) network security | Y | N | N/A |

| Parameter | Description |
|---|---|
| Organization | Select the organization for which to create the SCC. |
| Resource Set | Select the resource set in which to create the SCC. |
| Region | Select the region in which to create the SCC. |

Elastic Compute Service

**Instance types**

You can add only ECS instances of SCC instance types as nodes to SCCs. For information about SCC instance types, see **Intel-based instance families > SCC instance families** in ECS Instance Families & Instance Types in the Apsara Stack Documentation Center.

#### Create an SCC

Super Computing Cluster (SCC) provides ultra-high-performance, high-parallelism computing cluster services by using heterogeneous accelerators such as CPUs and GPUs that are connected over high-speed Remote Direct Memory Access (RDMA) networks. SCC is used in scenarios such as high-performance computing, artificial intelligence, machine learning, scientific and engineering computing, data analytics, and audio and video processing. This topic describes how to create an SCC.

**Precautions**

Take note of the following items: When you create an SCC, you cannot specify a security group ID and a virtual private cloud (VPC) ID for the SCC. The first time you add Elastic Compute Service (ECS) instances of SCC instance types to the SCC, a security group ID and a VPC ID are automatically configured for the SCC. For more information, see Add nodes to an SCC. When you create an SCC, a deployment set is automatically created in the ECS console. You can choose **Deployment Sets & Elasticity > Deployment Sets** in the left-side navigation pane to view the deployment set on the Deployment Sets page. The deployment set is named `hpc-null-deploymentset` . The Deployment Granularity parameter of the deployment set is set to **Network Switch** and the Deployment Policy parameter is set to
**Loose Aggregation**. For information about deployment sets, see Overview of deployment
sets.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Click **Create Cluster**.
5. On the **Create Super Computing Cluster** page, configure the parameters that are
described in the following table.

| Cluster Name | Enter a name for the SCC. The name must be 2 to 128 characters in length. The name cannot start with a special character or a digit. The name can contain underscores ( ), hyphens (-), _ and colons (:). |
|---|---|
| Cluster Description | Enter a description for the SCC based on your business requirements. |

| Item | Description |
|---|---|

Elastic Compute Service
6. Click **Submit**.

**Result**

You can view the new SCC on the Supper Computing Clusters page. For more information, see View an SCC.

**What to do next**

You can add ECS instances of SCC instance types to the SCC. For more information, see Add nodes to an SCC.

#### Add nodes to an SCC

After you create a super computing cluster (SCC), you can add nodes to the SCC by scaling up the SCC or by selecting an SCC instance type to create Elastic Compute Service (ECS) instances in the SCC.

**Prerequisites**

An SCC is created. For information about how to create an SCC, see Create an SCC.

**Background information**

After an SCC is created, the SCC is a logical cluster that does not contain nodes (ECS instances of SCC instance types) and does not have a security group ID or virtual private cloud (VPC) ID. The first time you add nodes (ECS instances of SCC instance types) to the SCC, the security group ID and VPC ID of the ECS instances are automatically configured as the security group ID and VPC ID of the SCC and cannot be changed.

**Important**

The security group ID and VPC ID of the SCC are automatically passed to ECS instances that are added to the SCC. All ECS instances of SCC instance types in an SCC have the same security group ID and VPC ID. When you add nodes to an SCC, take note of the limits that are described in the following table.

| ECS instance type | The nodes that you want to add must be ECS instances of SCC instance types. You can select SCC instance types to create ECS instances. For more information, see Intel-based instance families > SCC instance families in the Introduction to Instance Families and Instance Types in the Apsara Stack ECS documentation. |
|---|---|
| Image | Public images for the following operating system versions are supported: Anolis OS 8.4 ANCK (SCC) CentOS 7.5 (SCC) CentOS 7.9 (SCC) For information about images, see Overview. |
| Network | No limits apply to an SCC that does not have a security group ID or VPC ID. The following limits apply to an SCC that has a security group ID and a VPC ID: VPC: You can use only the VPC ID of the SCC to create ECS instances in the SCC. Security group: You can use only the security group ID of the SCC to create ECS instances in the SCC. |

Elastic Compute Service

**Scale up an SCC**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the SCC to which you want to add nodes. In the **Actions** column, click **Scale Up**.
5. On the **Create Instance** page, create ECS instances.
Take note of the parameters that are described in the following table. For information about how to create an ECS instance by using the wizard, see Create an instance.

| Parameter or section | Description |
|---|---|
| Specification | The value of Category is fixed to Super Computing Cluster. |
| Instance Type | Select an instance type. |
| Super Computing Cluster | The ID of the SCC to which you want to add nodes is automatically populated in this field and cannot be changed. |
| Number of Cluster Instances | The number of ECS instances in the SCC, which is automatically specified and cannot be changed. |

| Parameter | Description |
|---|---|
| VPC | The VPC ID of the SCC is automatically populated and cannot be changed. |
| Security Group | The security group ID of the SCC is automatically populated and cannot be changed. |

Elastic Compute Service If the SCC already contains ECS instances, the parameters that are described in the following table are automatically specified.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the **Instances** page, click **Create Instance**.
5. On the **Create Instance** page, create ECS instances.

| Parameter or section | Description |
|---|---|
| Specification | Set Category to Super Computing Cluster. |
| Instance Type | Select an instance type. |
| Super Computing Cluster | Select an existing SCC or click Create Cluster to create an SCC. After the SCC is created, go back to the Create Instance page and click the icon to obtain the most recent SCC list. For more information, see Create an SCC. Important This parameter is available and can be configured only when you set Category to Super Computing Cluster and select an SCC instance type. |
| Number of Cluster Instances | The number of ECS instances in the selected SCC, which is automatically specified and cannot be changed. |

| Parameter | Description |
|---|---|
| VPC | The VPC ID of the SCC is automatically populated and cannot be changed. |

Elastic Compute Service Take note of the parameters that are described in the following table. For information about how to create an ECS instance by using the wizard, see Create an instance. If the SCC already contains ECS instances, the parameters that are described in the following table are automatically specified.

| Security Group | The security group ID of the SCC is automatically populated and cannot be changed. |
|---|---|

| Parameter | Description |  |  |
|---|---|---|---|
| Organization | The organization to which the super computing cluster belongs. |  |  |
| Resource Set | The resource set to which the super computing cluster belongs. |  |  |
| Cluster Name | The name of the super computing cluster. |  |  |
| Cluster Description | The description of the super computing cluster. |  |  |
| Instances | The number of instances in the super computing cluster. You can click the number to go to the Instances page to view the information of all instances in the cluster. |  |  |
| Specifications | The total number of vCPUs and size of memory of all instances in the cluster. If no instances are added to the cluster, the value is vCPU: 0 Cores Memory:0 GiB . |  |  |
|  |  | vCPU: 0 Cores |  |
| Security Group ID | The security group ID of the cluster. If no instances are added to the cluster, this parameter is empty. |  |  |

|  | Memory:0 GiB |
|---|---|

Elastic Compute Service

#### View the details of a super computing

**cluster**

You can view the details of a super computing cluster in the super computing cluster list.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the **Super Computing Clusters** page, find the super computing cluster that you want
to view and view the details of the cluster. The following table describes the cluster parameters.

| VPC ID | The virtual private cloud (VPC) ID of the cluster. If no instances are added to the cluster, this parameter is empty. |
|---|---|
| Actions | Scale Up: Add instances to the cluster. For more information, see Add nodes to an SCC. Edit: Modify the attributes of a super computing cluster. For more information, see Modify the attributes of n SCC. Delete: Delete super computing clusters that are no longer needed. For more information, see Delete an SCC. |

| Parameter | Description |
|---|---|
| Cluster Name | Enter a new name for the SCC. The name must be 2 to 128 characters in length. The name cannot start with a special character or a digit. It can contain underscores ( ), hyphens (-), and _ colons (:). |
| Description | Enter a new description for the SCC based on your business requirements. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

Elastic Compute Service

#### Modify the attributes of an SCC

You can modify the following attributes of a super computing cluster (SCC) based on your business requirements: name and description.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the SCC whose attributes you want to modify. In the **Actions** column, click **Edit**.
5. In the **Edit** dialog box, modify the attributes of the SCC.
6. Click **OK**.

#### Delete an SCC

If you no longer need a super computing cluster (SCC), you can delete it.

**Prerequisites**

All Elastic Compute Service (ECS) instances are deleted from the SCC that you want to delete. For information about how to delete an ECS instance, see Delete an instance.

**Important**

Elastic Compute Service The amount of time that is required to release ECS instances in the background is several minutes. After you delete ECS instances from the SCC, we recommend that you wait 5 minutes to 10 minutes before you delete the SCC.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Super Computing**
**Clusters**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the SCC that you want to delete. In the **Actions** column, click **Delete**.
5. In the message that appears, verify the SCC information and click **Delete**.

### ECS bare metal instances

#### Create an ECS bare metal instance

This topic describes how to create an Elastic Compute Service (ECS) bare metal instance in the ECS console.

**Prerequisites**

The O&M administrator of Bare Metal Service in the Apsara Uni-manager Operations Console has registered ECS bare metal instances in a resource pool.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Bare Metal Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Bare Metal Instances page, click **Create Instance**.
5. On the page that appears, select an option in the Service Catalog section and click **OK**.
The service management feature is used to manage and control specific specifications of specific services within an enterprise or organization. This parameter is displayed only after you create and publish services that grant the current organization or user permissions to access ECS bare metal instances. For more information about the service management feature, see **Operations > Service catalogs > Service management** in the Apsara Unimanager Management Console User Guide in the Apsara Stack Documentation Center.
6. In the **Basic Settings** step, configure the basic attributes and the basic resources that are
required to create an ECS bare metal instance and click **Next**. The basic attributes include the organization, resource set, region, and zone. The basic resources include the instance type, image, and storage. You can click **Configuration Preview** in the lower part of the Create Instance page to view instance information. The information includes the attributes that you configured and the attributes that you need to configure.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | The organization in which you want to create the ECS bare metal instance. |
| Resource Set | Yes | The resource set in which you want to create the ECS bare metal instance. |
| Region | Yes | The region in which you want to create the ECS bare metal instance. |
| Zone | Yes | The zone in which you want to create the ECS bare metal instance. Zones are physical locations in the same region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create ECS instances in different zones. |

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service i. Configure the basic attributes of the instance. The following table describes the parameters. ii. Configure the instance specifications, including the instance family and instance type. The following table describes the parameters.

| Enable Hot Configuration Change | No | Specifies whether to enable hot configuration change for the instance. If you set this parameter to Yes, you can change the instance type without the need to stop the instance. For more information, see Perform a hot configuration change to change the instance type of an instance. If instance types that support hot configuration changes are available for selection, this parameter is set to Yes by default. In this case, the instance type list displays only the instance types that support hot configuration changes. Note If you do not need to select an instance type that supports hot configuration changes, set this parameter to No. All available instance types are displayed. If no instance types that support hot configuration changes are available, this parameter is set to No by default. In this case, the instance type list displays all available instance types. |
|---|---|---|
| Filter | No | The condition based on which instance types are filtered. You can select CPU, memory, or GPU as the filter condition, or enter a keyword to search for instance types. |
| CPU Type | Yes | The type of the CPU used by the ECS bare metal instance. Note The supported CPU types are displayed on the Create Instance page in the ECS console. |
| Category | Yes | The category of the ECS bare metal instance. Note The supported instance categories are displayed on the Create Instance page in the ECS console. |

Elastic Compute Service

| BMS Instances | Yes | The ECS bare metal instances that the O&M administrator of Bare Metal Service has registered in the Apsara Uni- manager Operations Console. |
|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| VPC | Yes | The virtual private cloud (VPC) in which you want to create the ECS bare metal instance. Select an existing VPC or click Create VPC to create a VPC. After the VPC is created, return to the ECS instance creation wizard and click the icon to refresh the VPC list. For more information about how to create a VPC, see VPCs and vSwitches > VPC management > Create a VPC in the VPC User Guide in the Apsara Stack Documentation Center. |
| VSwitch | Yes | The vSwitch to which you want to connect the ECS bare metal instance. Select an existing vSwitch or click Create vSwitch to create a vSwitch. After the vSwitch is created, return to the ECS instance creation wizard and click the icon to refresh the vSwitch list. For more information about how to create a vSwitch, see VPCs and vSwitches > vSwitch management > Create a vSwitch in the VPC User Guide in the Apsara Stack Documentation Center. |

Elastic Compute Service iii. Configure the Bare Metal Server (BMS) image to be used to create the ECS bare metal instance. Select the creation type of the BMS image. Use the default image. Re-install the image. Select an image type. Public image: the public image to be used by the ECS bare metal instance. Public images that are provided by Alibaba Cloud without operating system licenses deliver high security and stability. Custom image: the custom image to be used by the ECS bare metal instance. Custom images are created from ECS instances or snapshots or imported from your computer.
7. In the **Network Settings** step, configure the network settings and click **Next**.
You can click **Configuration Preview** in the lower part of the Create Instance page to view instance information. The information includes the settings that you configured and the settings that you need to configure.

| Private IP Address | No | The private IPv4 address to be assigned to the ECS bare metal instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you do not specify a private IPv4 address, the system automatically assigns a private IPv4 address to the ECS bare metal instance. |
|---|---|---|

| Parameter | Required | Description |
|---|---|---|

Elastic Compute Service
8. In the **System Configurations** step, configure the system settings and click **Next**.
The system configurations include the logon password, instance name, instance description, hostname, and whether to enable sequential suffixes, which are displayed in the ECS console. You can click **Configuration Preview** in the lower part of the Create Instance page to view instance information. The information includes the settings that you configured and the settings that you need to configure. i. Configure the logon password for the instance.

**Note**

The logon password must be 8 to 30 characters in length, and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ( ) ` ~ ! @ # $ % ^ & * - _ + = | { } [ ] : ; < > , . ? /. For Windows instances, the logon password cannot start with a forward slash (/). ii. Configure basic information about the instance.

| Instance Name | Yes | The name of the instance that you want to create. When you purchase multiple instances, the instance names are automatically added with a 3- digit suffix in sequence. By default, the incremental suffixes range from 001 to 100. Examples: LocalHost001, LocalHost002, MyInstance 001, and MyInstance002. Rules for custom instance names: You can specify the names of ECS instances in the name prefix[begin number,bi _ _ ts]name suffix format. For _ example, you can specify my name[99,3]ecs. If you _ create two instances, the names of the instances are my name099ecs and _ my name100ecs. The valid _ values of begin number are 0 _ to 999999, and the valid values of bits are 1 to 6. Default value: 6. |
|---|---|---|
| Instance Description | No | The description of the instance. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), _ and full-width characters. It cannot start with http:// or https://. |

Elastic Compute Service

| Hostname | No | The hostname of the instance. Rules for custom hostnames: You can specify the names of hostnames in the name prefix[begin number,bi _ _ ts]name suffix format. For _ example, you can specify my name[99,3]ecs. If you _ create two instances, the names of the instances are my name099ecs and _ my name100ecs. The valid _ values of begin number are 0 _ to 999999, and the value values of bits are 1 to 6. Default value: 6. |
|---|---|---|
| Enable Sequential Suffixes | Yes | Specifies whether to enable sequential suffixes for instances. When multiple instances are created and sequential suffixes are enabled, sequential suffixes are automatically added to the instance names and hostnames. The sequential suffixes range from 001 to 999. If the name prefix[begin number,bi _ _ ts] format is used, this feature does not take effect. The names are only sorted in the specified order. |

Elastic Compute Service
9. Create the ECS bare metal instance.
If the service whose **Cloud resources** parameter is set to **Bare Metal Instance** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Confirm**
**Order**.
If the service whose **Cloud resources** parameter is set to **Bare Metal Instance** does not exist on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Submit**.

**Result**

The ECS bare metal instance that you created is displayed in the **Completed** state on the Bare Metal Instances page.

#### Create multiple ECS bare metal

**instances at a time**

This topic describes how to create multiple Elastic Compute Service (ECS) bare metal instances at a time by uploading a local file.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | The organization in which you want to create the instances. |
| Resource Set | Yes | The resource set in which you want to create the instances. |
| Region | Yes | The region in which you want to create the instances. |
| Zone | Yes | The zone in which you want to create the instances. Zones are physical locations in the same region. Each zone has its own power grid and network. The internal networks of zones are connected. Faults in one zone are isolated from other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |
| Upload File | Yes | In the Upload File section, click Template to download the file template. Configure the parameters based on the formats specified in the template, and then select and upload the file. |

Elastic Compute Service

**Prerequisites**

The O&M administrator of Bare Metal Service has registered ECS bare metal instances in a resource pool in the Apsara Uni-manager Operations Console. The local file in the CSV, XLS, or XLSX format for creating multiple instances at a time is available.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Bare Metal Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Bare Metal Instances page, click **Batch Create**.
5. In the **Batch Create** dialog box, configure the parameters to create instances.

**File template**

| *Machin eTypeN ame | *CP UAr ch | *Mo del | *S N | *IsUs eOri ginI mag e | *Ima geTy pe | *I m a g e | * V P C I d | * V S w it c h | I P | U s e r n a m e | P a s s w o r d | * H o s t N a m e | *I n s t a n c e N a m e | D e s cr ip ti o n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bms | x86 _ 64 | test- mt | 123 456 | install os _ | publi c | C e n t o s- 7 . 9 - x 8 6 _ 6 4 | te st - v p c- 0 1 | t e st - s u b n e t- 0 1 | X X X . X X X . X X X . X X X | n a m e | p a s s w o r d | t e st - a p p ly - 0 1 | t e st - a p pl y- 0 1 |  |
| no clone _ | x86 _ 64 | test- mt | 654 321 | install os _ | custo mize | A n ol is O S - 8 . 6 | te st - v p c- 0 1 | t e st - s u b n e t- 0 1 | X X X . X X X . X X X . X X X | n a m e | p a s s w o r d | t e st - a p p ly - 0 2 | t e st - a p pl y- 0 2 |  |

Elastic Compute Service Elastic Compute Service

**Note**

The file template includes the following parameters. Values of the parameters are not case-sensitive.
**CPUArch**: required. The CPU architecture. Valid values: x86_64 and aarch64.
**Model**: required. The CPU model.
**SN**: required. The serial number (SN) of an instance.
**IsUseOriginImage**: required. Specifies whether to use the initial image. Valid
values: origin_image and install_os. The value origin_image indicates that the initial image is used. The value install_os indicates a new image is installed.
**ImageType**: required. The image type. Valid values: public and customize.
**VPCId**: required. The ID of the virtual private cloud (VPC).
**VSwitch**: required. The ID of the vSwitch.
**IP**: the IP address to be assigned to an instance. If no IP address is specified, the
system automatically assigns an IP address to the instance.
**LoginName**: required. The username that is used to log on to an instance.
**Password**: required. The password that is used to log on to an instance.
**HostName**: the hostname of an instance.
**InstanceName**: required. The custom name of an instance.
**Description**: the description of an instance.

**Result**

The created bare metal instances are in the **Completed** state on the Bare Metal Instances page.

#### Re-apply for an instance

This topic describes how to re-apply for an Elastic Compute Service (ECS) bare metal instance. You can re-apply for a created instance to re-install the instance.

**Prerequisites**

An ECS bare metal instance is created. For more information, see Create an ECS bare metal instance. The ECS bare metal instance is in a stable state, such as Running, Stopped, Create Failed, or No Heartbeat.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Bare Metal Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Bare Metal Instances page, find the instance for which you want to re-apply and click
**Apply Again** in the **Actions** column.
5. On the **Apply Again** page, configure the parameters as prompted. For more information,
see Create an ECS bare metal instance.
6. Click **Submit** to create the instance again.

| Section | Description |
|---|---|

Elastic Compute Service

**Result**

The re-created ECS bare metal instance is in the **Completed** state and displayed on the Bare Metal Instances page.

#### View the details of an instance

You can view all Elastic Compute Service (ECS) bare metal instances created within your account and the details of each ECS bare metal instance. The details of an ECS bare metal instance include the basic information and configuration information.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Bare Metal Instances**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the Bare Metal Instances page, view the information about the existing ECS bare metal
instances. You can view the instance information in the following columns in the instance list:
**Instance Name/SN**, **Status**, **Operation Status**, **Power Status**, **Cloud Assistant Client**
**Status**, **Organization/Resource Set**, **VPC IP Address**, **Image Name/ID**, **Model**,
**Configuration**, **Operating System**, **Out-of-band IP Address**, **Monitoring**, **Instance**
**Description**, and **Created At**.
You can also perform the following steps to specify the columns to be displayed in the instance list: i. In the upper-right corner of the instance list, click the icon. ii. In the **Custom Columns** dialog box, select the columns that you want to display in the instance list, such as **Creator**, and then click **OK**.
5. Select a filter condition, such as **Instance Name**, from the drop-down list and enter
relevant information in the search box. The instances that meet the specified filter condition are automatically displayed in the instance list.

**Note**

You can select a filter condition, such as **Instance Name**, **SN**, **VPC IP Address**,
**Out-of-band IP Address**, or **Creator**, to filter instances.
You can specify multiple filter conditions to narrow down the search results.
6. Find the ECS bare metal instance whose details you want to view. Then, use one of the
following methods to go to the Instance Details page of the ECS bare metal instance to view the details of the instance. In the **Instance Name/SN** column, click the instance name. Click **Manage** in the **Actions** column. The following table describes the information that is displayed on the **Instance Details** page.

| Basic Information | The basic information about the ECS bare metal instance, including the instance name or SN, organization, resource set, region, zone, hostname, Cloud Assistant ID, online status, operation status, power status, Agent, creation time, and instance description. |
|---|---|
| Configurations | The configurations of the ECS bare metal instance, including CPU architecture, model, number of CPU cores, memory size, operating system, image name, image ID, virtual private cloud (VPC) ID, vSwitch, VPC IP address, and out-of-band IP address. |

Elastic Compute Service
7. Manage the instance status.
In the upper-right corner of the Instance Details page, you can click Start, Restart, or Stop to start, restart, or stop the instance. You can also click **More** to perform other operations on the instance, such as releasing the instance and modifying the hostname.

#### Manage the status of an instance

This topic describes how to manage the status of an instance in the Elastic Compute Service (ECS) console. The instance status includes Starting, Restarting, Stopping, and Releasing.

**Prerequisites**

An ECS bare metal instance is created. For more information about how to create an ECS bare metal instance, see Create an ECS bare metal instance. The ECS bare metal instance is in a stable state, such as Running, Stopped, Create Failed, or No Heartbeat.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Bare Metal Instances**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the Bare Metal Instances page, find the instance that you want to manage, move the
pointer over **Instance Status** in the **Actions** column, and then select an option. Select **Start Instance**. In the message that appears, click **Start Instance**. Select **Restart Instance**. In the dialog box that appears, click **Restart Instance**. Select **Stop Instance**. In the message that appears, click **Stop Instance**. Select **Release Instance**. In the dialog box that appears, click **Release Instance** Elastic Compute Service

**Note**

In the dialog box that appears when you release an instance, you can specify whether to clear the data disks attached to the instance. If you do not select
**Clear Data Disks**, only the system disk is deleted. If you select this option,
both the system disk and the data disks are deleted. To release one or more ECS bare metal instances at a time, you can select one or more ECS bare metal instances and click **Release**. In the dialog box that appears, click **Release Instance**. The released ECS bare metal instances are available in the resource pool and installed again. You can apply for using the instances again.
5. View the status of the ECS bare metal instance in the **Operation Status**.

#### View operation logs

This topic describes how to view the operation logs of an Elastic Compute Service (ECS) bare metal instance.

**Prerequisites**

An ECS bare metal instance is created. For more information, see Create an ECS bare metal instance.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > Bare Metal Instances**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the Bare Metal Instances page, find the bare metal instance whose operation logs you
want to view. Use one of the following methods to open the Operation Log dialog box to view the operation logs of the bare metal instance.

**Note**

In the Operation Log dialog box, you can view the information about operations, such as operation type, operation time, and operation status, and filter operation logs by specifying a time range. Click the instance status in the **Operation Status** column. Click **Operation Log** in the **Actions** column.

| Comparison item | Premium performance disk | Standard performance disk | Standard SSD | Ultra disk |
|---|---|---|---|---|
| Maximum capacity per disk (GiB) | 131,072​ GiB | 32768 GiB | 32768 GiB | 32768 GiB |
| Maximum IOPS | 25000 | 5000 | 25000 | 5000 |
| Maximum throughput (MB/s) | 300 MB/s | 140 MB/s | 300 MB/s | 140 MB/s |

Elastic Compute Service

## Disks

### Disk overview

This topic describes the categories of disks and operations that can be performed on disks.

**Disk categories**

Disks are block-level storage devices provided by Apsara Stack for Elastic Compute Service (ECS) instances. Disks can be classified based on their performance or purpose.

**Performance-based classification**

Disks can be classified into ultra disks, standard SSDs, standard performance disks, and premium performance disks based on their performance. Ultra disks are suitable for medium I/O load scenarios and deliver up to 5,000 random IOPS per disk for ECS instances. Standard SSDs are suitable for I/O-intensive scenarios and deliver up to 25,000 random IOPS for ECS instances. Standard and premium performance disks are suitable for online transaction processing (OLTP) databases and NoSQL databases. Each premium performance disk delivers up to 25,000 random IOPS for ECS instances.

**Important**

Different Cloud Defined Storage (CDS)-Elastic Block Storage (EBS) clusters support different disk categories. New CDS-EBS clusters support standard and premium performance disks. CDS-EBS clusters created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks. Shared ultra disks and shared standard SSDs are retired. The following table compares the performance of different disk categories.

| Formula for calculating the IOPS per disk | min(1,800 + 30 × Capacity, 25,000) | min(1,800 + 8 × Capacity, 5,000) | min(1,800 + 30 × Capacity, 25,000) | min(1,800 + 8 × Capacity, 5,000) |
|---|---|---|---|---|
| Formula for calculating the throughput per disk | min(120 + 0.5 × Capacity, 300) MB/s | min(100 + 0.15 × Capacity, 140) MB/s | min(120 + 0.5 × Capacity, 300) MB/s | min(100 + 0.15 × Capacity, 140) MB/s |
| Type name in API operations | cloud pperf _ | cloud sperf _ | cloud ssd _ | cloud efficiency _ |
| Scenarios | OLTP databases: relational databases, such as MySQL, PostgreSQL, Oracle, and SQL Server databases NoSQL databases: non-relational databases, such as MongoDB, HBase, and Cassandra databases Elasticsearch distributed logs: Elasticsearch, Logstash, and Kibana (ELK) log analysis |  | Small and medium-sized development and test applications that require high data reliability | Development and test applications System disks |

Elastic Compute Service

**Note**

**Purpose-based classification**

Disks can be classified into system disks and data disks based on their purpose. System disks are created and released along with the ECS instances to which they are attached and have the same lifecycle as the instances. Shared access is not allowed for system disks. Data disks can be separately created or created along with ECS instances. Shared access is not allowed for data disks. A data disk created together with an ECS instance has the same lifecycle as the instance and is released along with the instance. A data disk that is separately created can be separately released or released along with the ECS instance to which it is attached. The capacity of a data disk is determined by the disk type.

**Data security**

Data durability during read and write operations Your business data has three copies stored in a block storage cluster within the same zone to ensure 99.9999999% (nine 9's) data durability during read and write operations. Proactive backup You can regularly create disk snapshots to enhance data security. Apsara Stack provides the snapshot service that allows you to back up and query disk data, such as logs and customer transaction data. For more information, see Overview. Data erasure mechanisms If you delete data, the data is completely erased from the distributed block storage system and can no longer be accessed by other users. The following mechanisms ensure complete erasure:

| Operation | Description | References |
|---|---|---|
| Create a disk | You can create an empty disk as a data disk. | Create a disk |
| Attach a data disk | You can attach separately created disks only as data disks to ECS instances within the same zone. | Attach data disks |
| Partition and format a disk | Before you can use a separately created disk attached to a Linux or Windows ECS instance, you must partition and format the disk. | Format a data disk for a Linux instance Format a data disk on a Windows ECS instance |
| View disks | You can view a list of created disks and the details of each disk. | View disk details |
| Roll back a disk by using a snapshot | If you created snapshots of a disk, you can use a snapshot to roll back the disk to the point in time when the snapshot was created for the disk. | Roll back a disk by using a snapshot |

Elastic Compute Service The storage system performs sequential writes to append data to existing files at the underlying layer of disks in a high-bandwidth and low-latency manner. If you delete a logical space from a disk to which data is appended, the delete operation is recorded as metadata. The storage system returns only zeros for all data read requests for the logical space. Similarly, when you overwrite the data in the logical space of a disk, data overwrite of the corresponding physical space is delayed. Instead, the storage system modifies the mapping between the logical and physical spaces. This ensures that the overwritten data cannot be read. Data fragments caused by delete or overwrite operations are forcefully and permanently deleted from the underlying physical disks. When you release an EBS device (disk), the storage system immediately destroys its metadata to ensure that the data is no longer accessible. At the same time, the physical storage space of the disk is recycled. The physical storage space must be cleared before it is re-assigned. Before data is written to a new disk, the system returns only zeros for all read requests. Data encryption If your applications are data-sensitive, we recommend that you encrypt the storage devices that you use. Disks and their snapshots are encrypted by using keys based on the industrystandard AES-256 algorithm. Data is automatically encrypted when it is transmitted from ECS instances to disks and then decrypted when it is read. For more information, see Encrypt a disk.

**Disk operations**

You can perform the following operations on disks.

| Change the disk category | You can change the category of a disk online without the need to stop the service. | Change the category of a disk |
|---|---|---|
| Modify disk properties | You can modify the properties of a created disk, including the Release Disk with Instance and Release Automatic Snapshots with Disk properties. | Modify the properties of a disk |
| Modify the name and description of a disk | You can modify the name and description of a disk. | Change the name and description of a disk |
| Resize a disk | You can resize the system disk or data disks of an ECS instance online or offline. After you resize a disk of an instance offline, restart the instance to make the new capacity of the disk take effect. | Resize a disk |
| Enable multi-attach | When you create a premium performance disk, you can enable the multi-attach feature for the disk. | Enable the multi-attach feature |
| Encrypt a disk | You can encrypt a new disk to improve security in a simple and secure manner. | Encrypt a system disk Encrypt a data disk |
| Re-initialize a disk | You can re-initialize a system or data disk to restore the disk to the state when it was created. | Re-initialize a system disk Re-initialize a data disk |
| Detach a data disk | You can detach a data disk from an ECS instance when the instance no longer uses the disk. You can also detach a data disk from an ECS instance and then attach the disk to another ECS instance within the same zone. | Detach data disks |
| Release a data disk | You can manually release a data disk that is no longer used. When a disk is released, all data stored on the disk is deleted. | Release a data disk |

Elastic Compute Service

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization/R esource Set | Yes | Select the resource set in which you want to create the disk. |
|  | Region/Zone | Yes | Select the zone in which you want to create the disk. |

Elastic Compute Service

### Create a disk

You can create a data disk separately and then attach it to an Elastic Compute Service (ECS) instance to increase the storage space of the instance. This topic describes how to create an empty data disk. Determine the number and sizes of data disks that you need before you create them. Take note of the following limits:

**Note**

System disks cannot be separately created. The maximum number of data disks that can be attached to a single instance varies based on the instance type. A single premium performance disk for which the multi-attach feature is enabled can be attached to up to 16 ECS instances at the same time. The maximum capacity of a disk depends on the disk type. Ultra disk, standard SSD, or standard performance disk: up to 32 TiB. Premium performance disk: up to 128 TiB. Disks cannot be combined in ECS. They are independent of each other. You cannot combine multiple disks into one by formatting them. A snapshot can back up data only of a single disk. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across disks. If you use LVM to create a logical volume across multiple disks, data discrepancy may occur when you restore disks from snapshots.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Disk**.
5. On the Create Disk page, configure the parameters. The following table describes the
parameters.

|  | Creation Method | Yes | Select a method to create the disk. Valid values: Disk Creation Storage Set Creation Note Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to resources in the storage set. You can use storage sets to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see Create a storage set in the CDS User Guide. |
|---|---|---|---|
|  | Storage Set | Yes | Select a storage set to create the disk. Note This parameter is required when you set Creation Method to Storage Set Creation. |
|  | Partitions | Yes | Select the number of partitions in a storage set. The value of this parameter must be greater than or equal to 2. Note This parameter is required when you set Creation Method to Storage Set Creation. |
|  | Name | Yes | Enter a name for the disk. If you create only one disk, the name must be 2 to 128 characters in length. If you create multiple disks at a time, the name must be 2 to 125 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |

Elastic Compute Service

|  | Quantity | Yes | Specify the number of disks that you want to create. Valid values: 1 to 100. |
|---|---|---|---|
|  | Specifications | Yes | The disk category. After you select a disk category, specify the size of the disk. Different CDS-EBS clusters support different disk categories. New CDS-EBS clusters support the following disk categories: Premium performance disk Standard performance disk CDS-EBS clusters that were created in Apsara Stack V3.15.0 and earlier support the following disk categories: Ultra disk Standard SSD Premium performance disk Standard performance disk |
| Basic Configurations |  |  |  |

Elastic Compute Service

|  | Disk Size (GiB) | Yes | The disk size depends on the disk type. Standard SSD, ultra disk, and standard performance disk: 20 GiB to 32,768 GiB. Premium performance disk: 20 GiB to 131,072 GiB. Important When you select Ultra Disk or SSD Disk for the Specifications parameter and specify a capacity greater than 2 TiB, you should notice the following recommended maximum disk sizes based on the number of hosts in the EBS cluster (number of hosts: maximum disk size): 6: 2 TiB 12: 4 TiB 15: 5 TiB 24: 8 TiB The formula for calculating the recommended maximum disk size is: Maximum disk size S = N/3, where N is the number of hosts in the EBS cluster. The calculating result is rounded down to the nearest integer. For example, if an EBS cluster has six hosts, we recommend that you set the disk size to no more than 2 TiB. |
|---|---|---|---|
|  | Multi-Attach | No | Specifies whether to enable multi- attach for the disk. For more information, see Overview of disks that support NVMe. Note This parameter is required when you set Specifications to Premium Performance Disk. |
|  | Encryption | No | Specify whether to encrypt the disk. |

Elastic Compute Service

|  | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required when you set Encryption to Yes. Valid values: AES256 SM4 |
|---|---|---|---|
|  | Encryption Key | No | Select a key to encrypt the disk. This parameter is required when you set Encryption to Yes. Note If no keys are available, create a key in Key Management Service (KMS). |
|  | Use Snapshot | No | Specify whether to create the disk from a snapshot. If you select Yes, you must select a snapshot. If you select a snapshot, the size of the disk is determined based on the size of the selected snapshot. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is less than the snapshot size, the disk is created with the snapshot size. |

Elastic Compute Service
6. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements. The **Quota** section displays the quota of each disk type and total quota in the current region, organization, and resource set. If the quota is insufficient, click **Management** to go to the **Quotas** page and adjust the quota.
7. Create the disk.
If you create a service by setting **Cloud products** to Elastic Compute Service and **ECS**
**Disk** on the Service Management page, confirm disk parameters and click **Confirm**
**Order**.
If you do not create a service by setting **Cloud products** to Elastic Compute Service and
**ECS Disk** on the Service Management page, confirm disk parameters and click **Submit**.
For more information about service catalog management, see the **Manage services** topic in **Apsara Uni-manager Operations Console User Guide** .

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization/R esource Set | Yes | Select the resource set in which you want to create the disk. |
|  | Region/Zone | Yes | Select the zone in which you want to create the disk. |
|  | Creation Method | Yes | Select a method to create the disk. Valid values: Disk Creation Storage Set Creation Note Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to resources in the storage set. You can use storage sets to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see Create a storage set in the CDS User Guide. |
|  | Storage Set | Yes | Select a storage set to create the disk. Note This parameter is required when you set Creation Method to Storage Set Creation. |

Elastic Compute Service
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Instances page, click the instance ID in the **Instance ID/Name** column.
5. On the **Instance Details** page, click the **Disks** tab.
6. Click **Create Disk**.
7. Configure the parameters described in the following table.

|  | Partitions | Yes | Select the number of partitions in a storage set. The value of this parameter must be greater than or equal to 2. Note This parameter is required when you set Creation Method to Storage Set Creation. |
|---|---|---|---|
|  | Name | Yes | Enter a name for the disk. If you create only one disk, the name must be 2 to 128 characters in length. If you create multiple disks at a time, the name must be 2 to 125 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
|  | Quantity | Yes | Specify the number of disks that you want to create. Valid values: 1 to 100. |
|  | Specifications | Yes | The disk category. After you select a disk category, specify the size of the disk. Different CDS-EBS clusters support different disk categories. New CDS-EBS clusters support the following disk categories: Premium performance disk Standard performance disk CDS-EBS clusters that were created in Apsara Stack V3.15.0 and earlier support the following disk categories: Ultra disk Standard SSD Premium performance disk Standard performance disk |

Elastic Compute Service

| Basic Configurations |  |  |  |
|---|---|---|---|
|  | Disk Size (GiB) | Yes | The disk size depends on the disk type. Standard SSD, ultra disk, and standard performance disk: 20 GiB to 32,768 GiB. Premium performance disk: 20 GiB to 131,072 GiB. Important When you select Ultra Disk or SSD Disk for the Specifications parameter and specify a capacity greater than 2 TiB, you should notice the following recommended maximum disk sizes based on the number of hosts in the EBS cluster (number of hosts: maximum disk size): 6: 2 TiB 12: 4 TiB 15: 5 TiB 24: 8 TiB The formula for calculating the recommended maximum disk size is: Maximum disk size S = N/3, where N is the number of hosts in the EBS cluster. The calculating result is rounded down to the nearest integer. For example, if an EBS cluster has six hosts, we recommend that you set the disk size to no more than 2 TiB. |
|  | Multi-Attach | No | Specifies whether to enable multi- attach for the disk. For more information, see Overview of disks that support NVMe. Note This parameter is required when you set Specifications to Premium Performance Disk. |
|  | Encryption | No | Specify whether to encrypt the disk. |

Elastic Compute Service

|  | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required when you set Encryption to Yes. Valid values: AES256 SM4 |
|---|---|---|---|
|  | Encryption Key | No | Select a key to encrypt the disk. This parameter is required when you set Encryption to Yes. Note If no keys are available, create a key in Key Management Service (KMS). |
|  | Use Snapshot | No | Specify whether to create the disk from a snapshot. If you select Yes, you must select a snapshot. If you select a snapshot, the size of the disk is determined based on the size of the selected snapshot. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is less than the snapshot size, the disk is created with the snapshot size. |

Elastic Compute Service
8. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements. The **Quota** section displays the quota of each disk type and total quota in the current region, organization, and resource set. If the quota is insufficient, click **Management** to go to the **Quotas** page and adjust the quota.
9. Create the disk.
If you create a service by setting **Cloud products** to Elastic Compute Service and **ECS**
**Disk** on the Service Management page, confirm disk parameters and click **Confirm**
**Order**.
If you do not create a service by setting **Cloud products** to Elastic Compute Service and
**ECS Disk** on the Service Management page, confirm disk parameters and click **Submit**.
For more information about service catalog management, see the **Manage services** topic in **Apsara Uni-manager Operations Console User Guide** .

**Verify the result**

The disk that you created is displayed in the disk list and is in the **Available** state.

| Instance type | Standard SSD | Ultra disk | Standard performanc e disk | Premium ESSD |
|---|---|---|---|---|
| ecs.ebmg7x-se-numaoff-x25- c1m8 | Not supported | Not supported | Not supported | Supported |
| ecs.ebmg7s-se-numaoff-x25- c1m8 | Not supported | Not supported | Not supported | Supported |
| ecs.ebmg7m-se-numaoff-x25- c1m8 | Not supported | Not supported | Not supported | Supported |
| ecs.ebmg6x-se-numaoff-hg- x25-c1m4 | Not supported | Not supported | Not supported | Supported |

Elastic Compute Service

**What to do next**

After the disk is created, you can attach, partition, and format the disk. For more information, see the following topics:

### Attach data disks

You can attach separately created disks only as data disks to Elastic Compute Service (ECS) instances within the same zone.

**Prerequisites**

The disks reside in the same zone as the instances to which you want to attach. The instances are in the **Running** or **Stopped** state. The disks are in the **Available** state.

**Background information**

Before you attach disks, take note of the following items: Data disks that were created along with instances are already attached to the instances. A disk can be attached only to an instance that resides in the same zone and region as the disk. You can attach disks that do not support the multi-attach feature or disks for which the multi-attach feature is disabled only to a single instance at a time. A disk that supports the multi-attach feature can be attached to multiple instances at a time. For more information, see Overview of disks that support NVMe. Some instance types support only certain disk categories. Instance types that are not listed in the following table do not have such limits.

| ecs.ebmg6x-se-numaoff-hg- x25-c1m8 | Not supported | Not supported | Not supported | Supported |
|---|---|---|---|---|
| ecs.ebmg7x-se-numaoff-hg- x25-c1m4 | Not supported | Not supported | Not supported | Supported |
| ecs.ebmg7x-se-numaoff-hg- x25-c1m8 | Not supported | Not supported | Not supported | Supported |
| ecs.g7x-se-x25 | Not supported | Not supported | Not supported | Supported |
| ecs.g7s-se-x25 | Not supported | Not supported | Not supported | Supported |
| ecs.g7m-se-x25 | Not supported | Not supported | Not supported | Supported |
| ecs.g7x-se-numaon-hg-k25 | Not supported | Not supported | Not supported | Supported |
| ecs.g7x-se-2numa-hg-k25 | Not supported | Not supported | Not supported | Supported |
| ecs.ebmg7x-x25-c1m8 | Not supported | Not supported | Supported | Supported |
| ecs.ebmg6e-x25 | Not supported | Not supported | Supported | Supported |
| ecs.ebmg7m-x25-c1m8 | Not supported | Not supported | Supported | Supported |
| ecs.ebmg7s-x25-c1m8 | Not supported | Not supported | Supported | Supported |
| ecs.ebmgn7i-numaoff-x25- a10x4 | Not supported | Not supported | Supported | Supported |
| ecs.ebmgn7ix-x25-c1m8 | Not supported | Not supported | Supported | Supported |

Elastic Compute Service

| ecs.ebmm6e-numaoff-x25- 1nvme | Not supported | Not supported | Supported | Supported |
|---|---|---|---|---|
| ecs.ebmm6e-numaoff-x25- t4x2-2nvme | Not supported | Not supported | Supported | Supported |
| ecs.ebmr6e-numaoff-x25- 12nvme | Not supported | Not supported | Supported | Supported |
| ecs.ebmr6e-numaoff-x25- 1nvme | Not supported | Not supported | Supported | Supported |
| ecs.g6e-x25 | Not supported | Not supported | Supported | Supported |
| ecs.g7m-x25 | Not supported | Not supported | Supported | Supported |
| ecs.g7s-x25 | Not supported | Not supported | Supported | Supported |
| ecs.g7x-x2 | Not supported | Not supported | Supported | Supported |
| ecs.gn7ix-x2 | Not supported | Not supported | Supported | Supported |
| ecs.sccg7x-roce-hg-x25-c1m4 | Not supported | Not supported | Supported | Supported |
| ecs.sccg7x-roce-x25-c1m2 | Not supported | Not supported | Supported | Supported |
| ecs.sccg7x-roce-x25-c1m4 | Not supported | Not supported | Supported | Supported |
| ecs.sccg7x-roce-x25-c1m8 | Not supported | Not supported | Supported | Supported |
| ecs.vgn7ix-x25 | Not supported | Not supported | Supported | Supported |

Elastic Compute Service If you want to attach multiple disks to an ECS instance, go to the details page of the instance.
1. Log on to the ECS console.

| Parameter | Description |
|---|---|
| Instance | Select the ECS instance to which you want to attach the disk. |

Elastic Compute Service
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance and click the instance ID.
5. On the **Instance Details** page, click the **Disks** tab and click **Attach Disk**.
6. In the **Attach Disk** dialog box, select disks from the **Disk** drop-down list.

**Note**

You can select up to five disks at a time. The number of disks that you can select cannot exceed the maximum number of disks that can be attached to the instance. To attach multiple disks, the system executes the AttachDisk operation in serial mode. If an AttachDisk operation fails, the operation is skipped. You can retry the failed operation after all other AttachDisk operations are complete.
7. Click **OK**.
8. Create partitions and file systems on the disk after the disk is attached to the instance.

**Note**

After the disk is attached to the instance, the disk cannot be used on the instance. For example, you cannot view the mount information of the disk attached to a Linux instance by running the `df -h` command. You must perform operations based on the operating system type of the instance to make the disk usable on the instance. For more information, see the following topics: Format a data disk of a Windows instance If you want to attach multiple disks to different ECS instances, go to the Disks page.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find a disk whose **status** is **Available** and choose
> **Attach** in the **Actions** column.
5. In the dialog box that appears, configure parameters to attach the disk.

| Release Disk with Instance | If you select this option, the disk is automatically released when its associated instance is released. If you do not select this option, the disk is retained when its associated instance is released. Note If the disk that you want to attach is a system disk that was detached from another instance, the instance specified by Release Disk with Instance refers to the instance from which the disk was detached, instead of the current instance. |
|---|---|

Elastic Compute Service
6. Click **OK**.
When the disk is attached, its state changes to **Running**.
7. Create partitions and file systems on the disk after the disk is attached to the instance.

**Note**

After the disk is attached to the instance, the disk cannot be used on the instance. For example, you cannot view the mount information of the disk attached to a Linux instance by running the `df -h` command. You must perform operations based on the operating system type of the instance to make the disk usable on the instance. For more information, see the following topics: Format a data disk of a Windows instance

### Partition and format disks

#### Format a data disk for a Linux instance

Data disks created separately are not partitioned or formatted. This topic describes how to partition and format a data disk of a Linux instance.

**Prerequisites**

The data disk that you want to manage is attached to a Linux instance.

**Procedure**

1. Connect to the Linux instance.
For more information, see Overview.
2. Run the **fdisk -l** command to view all data disks attached to the instance.
If /dev/vdb is not displayed in the command output, no data disk is attached to the ECS instance. Check whether the data disk that you want to manage is attached to the instance. Elastic Compute Service

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00000000
```

3. Partition the data disk.
i. Run the **fdisk /dev/vdb** command. ii. Enter n to create a partition. iii. Enter p to set the partition type to primary partition. iv. Enter the partition sequence number and press the ENTER key. In this example, 1 is entered to create Partition 1. v. Enter a sequence number for the first available sector. You can press the ENTER key to accept the default value, or enter a value ranging from 1 to 41,610 and then press the ENTER key. In this example, the default value is used. vi. Enter the sequence number for the last sector. You can press the ENTER key to accept the default value, or enter a value ranging from 1 to 11,748 and then press the ENTER key. In this example, the default value is used. vii. **Optional:**To create multiple partitions, repeat steps ii to vi until all primary partitions are created. Elastic Compute Service viii. Run the **wq** command to start partitioning the data disk.

```
[root@iZ********eZ ~]# fdisk /dev/vdb Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel Building a new DOS disklabel with disk identifier 0x01ac58fe. Changes will remain in memory only, until you decide to write them. After that, of course, the previous content won't be recoverable. Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite) WARNING: DOS-compatible mode is deprecated. It's strongly recommended to
         switch off the mode (command 'c') and change display units to
         sectors (command 'u').
Command (m for help): n Command action
   e   extended
   p   primary partition (1-4)
```

p

```
Partition number (1-4): 1 First cylinder (1-41610, default 1): Using default value 1 Last cylinder, +cylinders or +size{K,M,G} (1-41610, default 41610): Using default value 41610 Command (m for help): wq The partition table has been altered!
```

4. Run the **fdisk -l** command to view the partitions.
If /dev/vdb1 is displayed in the command output, a partition named vdb1 is created.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x01ac58fe Device Boot Start End Blocks Id System /dev/vdb1 1 41610 20971408+ 83 Linux
```

5. Format the new partition. In this example, the **mkfs.ext3 /dev/vdb1** command is used to
format the new partition as ext3. The amount of time required for formatting depends on the disk size. You can also format the new partition to another file system. For example, run the **mkfs.ext4 /dev/vdb1** command to format the partition as ext4.

| echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab ion of the new partition to the /etc/fstab file. Then, run the | command to write cat /etc/fstab |
|---|---|

Elastic Compute Service ext4 is a deeper improvement over ext3 than ext3 was over ext2. ext3 was mostly about adding journaling to ext2, but ext4 modifies important data structures of the file system. ext4 provides better performance and reliability and more features.

```
[root@iZ********leZ ~]# mkfs.ext3 /dev/vdb1 mke2fs 1.41.12 (17-May-2010) Filesystem label= OS type: Linux Block size=4096 (log=2) Fragment size=4096 (log=2) Stride=0 blocks, Stripe width=0 blocks 1310720 inodes, 5242852 blocks 262142 blocks (5.00%) reserved for the super user First data block=0 Maximum filesystem blocks=4294967296 160 block groups 32768 blocks per group, 32768 fragments per group 8192 inodes per group Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
    4096000
Writing inode tables: done Creating journal (32768 blocks): done Writing superblocks and filesystem accounting information: done This filesystem will be automatically checked every 25 mounts or 180 days, whichever comes first. Use tune2fs -c or -i to override.
```

Ubuntu 12.04 does not support barriers. To write the information of the new partition to the /etc/fstab file, run the `echo '/dev/vdb1 /mnt ext3 barrier=0 0 0' >> /etc/fstab` command. In this example, the partition information is added to the ext3 file system. You can also modify the ext3 parameter to add the partition information to another type of file system. To mount the data disk to a specific folder for specific purposes, such as storing web pages, modify the /mnt part of the preceding command.

| Operating system | Resource | Description |
|---|---|---|
|  | Image used by the instance | Windows Server 2012 R2 64-bit |
| 12 | > Document Version: 2026062 |  |

Elastic Compute Service

```
[root@iZ********eZ ~]# echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab [root@iZbp19cdhgdj0aw5r2izleZ ~]# cat /etc/fstab
```

#

```bash
# /etc/fstab
# Created by anaconda on Thu Aug 14 21:16:42 2014
```

#

```bash
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
```

#

```
UUID=94e4e384-0ace-437f-bc96-057dd64f**** / ext4 defaults,barrier=0 1 1 tmpfs /dev/shm tmpfs defaults 0 0 devpts /dev/pts devpts gid=5,mode=620 0 0 sysfs /sys sysfs defaults 0 0 proc /proc proc defaults 0 0 /dev/vdb1 /mnt ext3 defaults 0 0
```

7. Run the following command to mount the new partition: Run the **mount -a** command to
mount all the partitions listed in the /etc/fstab file and run the **df -h** command to view the result. If the following information is displayed, the new partitions are mounted and ready for use.

```
[root@iZ********eZ ~]# mount -a [root@iZ********eZ ~]# df -h Filesystem Size Used Avail Use% Mounted on /dev/vda1 40G 5.6G 32G 15% / tmpfs 499M 0 499M 0% /dev/shm /dev/vdb1 20G 173M 19G 1% /mnt
```

#### Format a data disk on a Windows ECS

**instance**

Before you can store, read, and write data on a new data disk that is attached to a Windows Elastic Compute Service (ECS) instance, you must initialize the data disk. The initialization operations include partitioning the disk, formatting the disk, and bringing the disk online. This topic describes how to initialize a data disk on a Window instance.

**Prerequisites**

The data disk is attached to a Window instance. For more information, see Attach data disks.

**Background information**

The example in this topic uses an ECS instance and a data disk that have the configurations described in the following table. Operations may vary based on actual conditions.

| lastic Compute Serv | ice User Guide·Disk |  |
|---|---|---|
| Windows operating system |  |  |
|  | Data disk | Disk name: Disk 1 Disk capacity: 40 GiB |

**Procedure**

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

**Important**

A Master Boot Record (MBR) partition can be up to 2 TiB in size. If the disk for which a partition is created is larger than 2 TiB or if the disk may be resized to larger than 2 TiB, use the GPT partition format. Elastic Compute Service
7. Right-click the **Unallocated** section of **Disk 1** and select **New Simple Volume**.
8. In the **New Simple Volume Wizard** window, click **Next** and follow the wizard to perform
initialization operations. i. In the **Specify Volume Size** step, set **Simple volume size in MB** and click **Next**. If you want to create only a single primary partition on the disk, use the default value. You can also specify a simple volume size based on your needs to divide **Disk 1** into multiple partitions. ii. In the **Assign Drive Letter or Path** step, select **Assign the following drive letter**, select a drive letter, and then click **Next**. In this example, D is selected for the drive letter. iii. In the **Format Partition** step, select **Format this volume with the following**
**settings**, configure formatting settings, and then click **Next**.
iv. View the information of the new simple volume and then click **Finish** to close the **New**
**Simple Volume Wizard** window.

### View disk details

You can view the list of existing disks and the details, snapshots, and operation logs of a disk. The details of a disk include the basic information and attachment information of the disk.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Disks page, view information about existing disks.
You can view disk information in the disk list in the columns, such as **Disk ID/Name**,
**Status**, **Organization/Resource Set**, **Region**, **Disk Category/Size**, **Multi-attach**,
**Instance ID/Name**, **Disk Type**, and **Encrypted**.

| Section | Description |
|---|---|
| Basic Information | The basic information about the disk, including the disk name, disk ID, disk status, organization and resource set to which the disk belongs, region where the disk resides, disk category, disk size, multi-attach setting, IDs and names of the instances to which the disk is attached, and encryption settings of the disk. You can click Modify Disk Description in the upper-right corner of the Basic Information section to modify the name and description of the disk. For more information, see Change the name and description of a disk. |

Elastic Compute Service

**Note**

If you created a disk together with the instance to which the disk is attached and do not specify a name for the disk, a name is assigned to the disk based on the following naming conventions: If the disk is the system disk of the ECS instance, a name in the format of <Instance name>_SystemDisk is assigned to the disk. Example: ecstest_SystemDisk. If the disk is a data disk of the ECS instance, a name in the format of <Instance name>_dataDisk_*** is assigned to the disk. Example: ecstest_dataDisk_001 or ecstest_dataDisk_002. You can perform the following steps to specify the columns to be displayed in the disk list: i. In the upper-right corner of the disk list, click the icon. ii. In the Custom Columns dialog box, select the columns to be displayed in the disk list. The selected columns are immediately displyaed in the disk list.
5. Select a filter condition such as **Disk ID** from the drop-down list and enter a disk ID in the
search box to search for the disk. The disk that meets the specified filter condition is displayed.

**Note**

You can select a filter condition, such as **Disk Name**, **Disk ID**, **Encryption Key**
**ID**, **Storage Set**, **Partition ID**, **Zone**, or **Instance ID**, and enter relevant
information to search for disks. Fuzzy query is supported only if you select **Disk Name** or **Disk ID** as the filter condition. You can also specify multiple filter conditions to narrow down the search results.
6. Click the ID of a disk in the **Disk ID/Name** column.
The **Disk Details** tab is displayed by default. The following table describes the disk information that is displayed on the **Disk Details** tab.

| Attachment Information | The attachment information about the disk, including the Release Disk with Instance and Release Automatic Snapshots with Disk parameters, and information about instances to which the disk is attached. You can also click Modify Disk Properties in the upper-right corner of the Attachment Information section to modify the release mode of the disk. For more information, see Modify the properties of a disk. |
|---|---|

Elastic Compute Service
7. View the snapshots and operation logs of the disk.
Snapshots of the disk: Click the **Disk Snapshots** tab to view information about snapshots that are created for the disk. The information about a snapshot includes the snapshot ID, snapshot encryption status, tags that are added to the disk, snapshot type, snapshot creation progress, and snapshot creation time. Click the **Operation Log** tab to view the operation logs of the disk. The operation logs include the operation name, operator, execution status, operation source (console call and API call), operation type, source IP address of the operation, and operation time. Search for operation logs that you require by specifying filter conditions. Select a filter condition from the drop-down list and enter the corresponding information in the search box to search operation logs. The operation logs that meet the specified filter condition are displayed. Click **Advanced Filter**, specify multiple filter conditions, and then click **Search** to search operation logs. Click **Operation Details** in the Actions column of an operation to view the operation details.

**Note**

### Roll back a disk by using a

**snapshot**

If you have created a snapshot of a disk, you can use the snapshot to roll back the disk to the point in time when the snapshot was created. The disk rollback operation is irreversible. After the disk is rolled back, the data that was stored on the disk before the rollback operation is performed is lost and cannot be recovered. Exercise caution when you perform this operation.

**Prerequisites**

Before you roll back a disk by using a snapshot, make sure that the following requirements are met: Snapshots have been created for the disk, and no snapshots are currently being created for the disk. For more information, see Create a snapshot. The disk is not released. The disk is attached to an instance that is in the **Stopped** state.

**Procedure**

1. Log on to the ECS console.
Elastic Compute Service
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find a snapshot of the disk that you want to roll back and click **Roll Back Disk** in the
**Actions** column.

**Note**

You can roll back only one disk on an instance at a time. Other disks that are attached to the instance are not affected. After the rollback operation is complete, the entire disk (not a partition or a directory) is restored to the state that the disk was in when the snapshot was created.
6. In the message that appears, click **Roll Back Disk**.
7. Starts an ECS instance.
For more information, see Start an instance.

**What to do next**

After the disk is rolled back, the hosts configuration file and the configurations such as the hostname, SSH key pair, passwords, network settings, operating system repository settings, and clock source are initialized. You must reconfigure the file and configurations If you have resized the disk after you created the snapshot for the disk, you must log on to the instance to resize the file systems on the disk again after the disk is rolled back. For more information, see Resize a disk.

### Change the category of a disk

Apsara Stack offers different categories of disks to meet the requirements for storage performance and costs in different scenarios. You can change the categories of disks based on your business requirements without stopping the instances to which the disks are attached. If you have created a standard SSD and you want to increase the IOPS of the standard SSD, you can upgrade the standard SSD to an enterprise SSD (ESSD).

**Prerequisites**

Snapshots are created for the disk whose category you want to change. For information about how to create snapshots of disks to back up disk data, see Create a snapshot.

**Background information**

For more information about the performance of different disk categories, see the Categories of disks section of the "Overview" topic.

**Considerations**

When you change the category of a disk, take note of the following items: The performance of the disk may be affected. We recommend that you change the disk category during off-peak hours. It may take hours to change the category of a disk. The actual amount of time required is determined based on the storage capacity, original category, and throughput of the disk. We recommend that you call the **DescribeTaskAttribute** operation to view the task progress after you change the category of a disk. For more information, see the DescribeTaskAttribute topic in **ECS Developer Guide**. Disk categories may fail to be changed due to insufficient resources. If a disk category fails to be changed, retry later.

| Original disk category | New disk category to which disks can be changed online |
|---|---|
| Standard SSD | Ultra disk Premium performance disk Standard performance disk |
| Ultra disk | Standard SSD Premium performance disk Standard performance disk |
| Premium performance disk | Standard performance disk |
| Standard performance disk | Premium performance disk |

| Phase | Limit |
|---|---|
| Before the disk category change | Up to five disk change tasks can be concurrently run in the same region within an account. |
| During the disk category change | The following limits apply while a disk is being changed: You cannot cancel the disk change task. You cannot create snapshots for the disk. You cannot resize the disk. You cannot partition or format the disk. You cannot re-initialize the disk You cannot roll back the disk by using snapshots. You cannot attach or detach the disk. If the disk is a system disk, you cannot change the operating system. |
| After the disk category change | You cannot change the disk category again within seven days. |

Elastic Compute Service Disk category change is supported only when a Cloud Defined Storage-Elastic Block Storage (CDS-EBS) cluster is deployed. The following table describes the disk categories that can be changed online. The following table describes the limits that apply to each phase of a disk category change.

**Billing**

Elastic Compute Service After you change the category of a disk, you are charged based on the new disk category.

**Note**

Bills are generated only after the administrator configures billing rules in the operation center. For more information about the billing rules, see the **Create a billing**
**configuration** topic in **Apsara Uni-manager Operations Console User Guide** .

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Disks page, find the disk that you want to manage, move the pointer over the
icon in the **Actions** column, and then select **Change Disk Category**.
5. In the **Change Disk Category** dialog box, select a disk category from the **New Disk**
**Category** drop-down list.
6. Click OK to submit the disk category change task.

**Verify the result**

On the Disks page, you can view the disk category change progress in the **Status** column. When the status of the disk changes from **Changing** to **Running**, the disk category change task is complete. In this case, the new disk category takes effect.

**Note**

When the disk is in the Changing state, you can click View Task below Changing to view the progress of the task. For more information, see View asynchronous tasks.

### Modify the properties of a disk

You can modify the properties of a created disk, such as the configurations of the Release Disk with Instance and Release Automatic Snapshots with Disk options.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk whose information you want to modify, click the
icon in the **Actions** column, and then select **Modify Disk Properties**.
5. In the **Modify Disk Properties** dialog box, modify the Release Mode settings. You can
specify one of the following release modes:
**Release Disk with Instance**: If this option is selected, the disk is released when the
instance to which the disk is attached is deleted. If this option is not selected, the disk is retained and enters the **Pending** state when the instance to which the disk is attached is deleted.
**Release Automatic Snapshots with Disk**: If this option is selected, the automatic
Elastic Compute Service snapshots created for the disk are released when the disk is deleted. If this option is not selected, the automatic snapshots are retained when the disk is deleted.
6. Click **OK**.

### Change the name and

**description of a disk**

You can change the name and description of a created disk to facilitate disk management and improve disk readability.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk whose name and description you want to change. In the **Actions** column,
choose
**> Modify Disk Description**.

**Note**

Alternatively, click the ID of the disk whose name and description you want to change in the **Disk ID/Name** column, find the **Basic Information** section on the **Disk Details** tab, and then click **Modify Disk Description**.
5. Change the name and description of the disk.
The disk name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://` . The name can contain letters, digits, periods (.), underscores (_), hyphens (-), colons (:), and commas (,). The disk description must be 2 to 256 characters in length and cannot start with `http://` or `https://` .
6. Click **OK**.

### Clone a disk

You can clone a disk to quickly create a replica that is identical to the existing disk. This allows you to back up data, migrate the system environment, or create a test environment with ease to ensure business continuity and data security.

**Prerequisites**

A disk is in the **Running** or **Available** state. The disk in the **Available** state was attached to an Elastic Compute Service (ECS) instance and then detached from the ECS instance. You cannot clone a disk across regions.

**Billing**

The replica uses the pay-as-you-go billing method. Elastic Compute Service

**Note**

Bills are generated only after the administrator configures billing rules in the operation center. For more information about billing rules, see the topics under **Operations >**
**Pricing > Manage billing configurations** in Apsara Uni-manager Management
Console User Guide in Apsara Stack Documentation Center.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Disks page, find the disk that you want to clone, move the pointer over the
icon in the **Actions** column, and then select **Clone Disk**.
5. In the **Clone Disk** dialog box, enter a value in the **Destination Disk Quantity** field in the
Destination Disk Settings step and click **Next**.
6. In the Configuration Preview step, preview the ID and type of the disk to be cloned, as well
as the size, region, and zone of the replicas, and then click **Submit**.
7. View the information about the replicas in the destination region.
This process is implemented by CloudOps Orchestration Service (OOS). You can log on to the OOS console to view the progress of the clone operation. For more information about how to log on to the OOS console, see **Log on to the OOS console** in **OOS User Guide** in the Apsara Stack Documentation Center.

### Resize a disk

You can resize your disks to store a larger volume of data as your business grows and storage requirements increase. You can resize the system disk or data disks of an Elastic Compute Service (ECS) instance online or offline. After you resize a disk of an ECS instance offline, you must restart the ECS instance to make the new capacity take effect.

**Prerequisites**

Snapshots are created for the disk that you want to resize to back up the disk data. For more information, see Create a snapshot. This prevents data loss caused by accidental operations performed when the disk is resized. No snapshot is being created for the disk that you want to resize. The following requirements are met: If the disk is a system disk, the ECS instance to which the system disk belongs is in the
**Running** state.
If the disk is a data disk, one of the following requirements is met: The disk is in the **Available** state. If the disk is attached to an ECS instance, the ECS instance is in the **Running** state. If the disk is a Shared Block Storage device, the disk is in the **Available** state.

**Background information**

You can use one of the following methods to increase the storage capacity of a single ECS instance:

| Method | Usage notes |
|---|---|
| Resize a disk online | The ECS instance to which the disk is attached is in the Running state. After you resize the disk, the new capacity automatically takes effect without the need to restart the ECS instance. |
| Resize a disk offline | The ECS instance to which the disk is attached is in the Running or Stopped state. After you resize the disk, you must restart the ECS instance in the ECS console or by calling the RebootInstance operation for the new capacity to take effect. |

| Item | Limits |
|---|---|

Elastic Compute Service

**Note**

When you resize a disk, only the storage capacity of the disk is increased. The sizes of partitions and file systems are not changed. Resize an existing disk. You can resize the existing partitions of the disk or create more partitions on the disk. The following table describes the two methods for resizing an existing disk. Create a disk, attach the disk to an ECS instance as a data disk, and then partition and format the disk. Replace the system disk of the ECS instance and specify a greater size for the new system disk. Before you resize a disk, take note of the items that are described in the following table.

| Disk category | Different Cloud Defined Storage-Elastic Block Storage (CDS-EBS) clusters support different disk categories. New CDS-EBS clusters support the following disk categories: Premium performance disk Standard performance disk CDS-EBS clusters that were created in Apsara Stack V3.15.0 and earlier support the following disk categories: Ultra disk Standard SSD Premium performance disk Standard performance disk Existing Elastic Block Storage (EBS) clusters continue to provide shared ultra disks and shared standard SSDs. Important If you have used shared ultra disks or shared standard SSDs, you can continue to use them. If you have never used shared ultra disks and shared standard SSDs, you cannot use disks of these categories. |
|---|---|
| Operating system | The system disks of ECS instances that run Windows Server 2003 cannot be resized. |
| Partitioning method | If a data disk is partitioned by using the Master Boot Record (MBR) method, the data disk cannot be resized to more than 2 TiB. If you want to resize a data disk partitioned by the MBR method to more than 2 TiB, we recommend that you create and attach another data disk. Then, partition the new data disk by using the GUID partition table (GPT) method and copy the data in the MBR disk to the GPT disk. |
| File system | For Windows instances, only disks that use New Technology File System (NTFS) file systems can be resized. |

Elastic Compute Service

| Capacity | System disk: The new capacity must be greater than the current capacity. The new capacity must be smaller than or equal to 2,048 GiB. Data disk: The new capacity must be greater than the current capacity. The new capacity must be smaller than or equal to the following values: Standard SSD, ultra disk, or standard performance disk : 32,768 GiB. Premium performance disk: 131,072 GiB. Important When you select Ultra Disk or SSD Disk and specify a capacity greater than 2 TiB, you should notice the following recommended maximum disk sizes based on the number of hosts in the EBS cluster (number of hosts: maximum disk size): 6: 2 TiB 12: 4 TiB 15: 5 TiB 24: 8 TiB The formula for calculating the recommended maximum disk size is: Maximum disk size S = N/3, where N is the number of hosts in the EBS cluster. The calculating result is rounded down to the nearest integer. For example, if an EBS cluster has six hosts, we recommend that you set the disk size to no more than 2 TiB. |
|---|---|
| Operation | When you resize a disk, only the storage capacity of the disk is increased. The sizes of partitions and file systems are not changed. After the disk is resized, you must manually re-allocate the storage space on the disk. You cannot roll back a resize operation on a disk to decrease the storage capacity of the disk. |

Elastic Compute Service

**Billing**

After you resize a disk, you are charged based on the new disk specifications.

**Note**

Bills are generated only after the administrator configures billing rules in the operations center. For more information about billing rules, see the topics under **Operations >**
**Pricing > Manage billing configurations** in Apsara Uni-manager Management
Console User Guide in the Apsara Stack Documentation Center.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
Elastic Compute Service
4. On the Disks page, find the disk that you want to resize, move the pointer over the
icon in the **Actions** column, and then select **Resize Disk**.
5. Optional. Select a service catalog and click **OK**.
The service management feature is used to manage and control specific specifications of specific services within an enterprise or an organization. This parameter is displayed only after you create and publish services that grant the current organization or user permissions to access ECS disks. For more information about service management, see the
**Manage service catalogs** topic in **Apsara Uni-manager Management Console User**
**Guide**.
6. In the **Resize Disk** dialog box, select a resizing method and specify the new capacity.
Resizing methods: Online Resizing: After you resize a disk online, the new capacity automatically takes effect without the need to restart the ECS instance to which the disk is attached. Offline Resizing: After you resize a disk offline, you must restart the ECS instance to which the disk is attached in the ECS console or by calling the `RebootInstance` operation for the new capacity to take effect. For more information, see Restart an instance or `RebootInstance` in **ECS Developer**
**Guide**.
Maximum new capacity: System disk: 2,048 GiB. Data disk:
**Standard SSD, ultra disk, or standard performance disk**: 32,768 GiB.
**Premium performance disk**: 131,072 GiB.
7. Resizes the disk.
If a service whose **Resources** value is **ECS Disk** exists on the Service Management page, confirm disk parameters and click **Confirm Order**. If no service whose **Resources** value is **ECS Disk** exists on the Service Management page, confirm disk parameters and click **OK**.

**What to do next**

After a disk is resized, you must manually re-allocate the storage space on the disk.

### Support the NVMe protocol

**and multi-attach feature**

#### Overview of disks that support NVMe

Non-Volatile Memory Express (NVMe) is a host controller interface protocol used to accelerate the transfer of data from non-volatile memory. Alibaba Cloud premium performance disks support NVMe. Each premium performance disk can be simultaneously attached to multiple Elastic Compute Service (ECS) instances that support NVMe for data sharing. This topic describes premium performance disks that support NVMe, limits on attaching the disks, and related operations.

| Resource | Description |
|---|---|

Elastic Compute Service Premium performance disks can be attached to multiple ECS instances. After premium performance disks are attached to multiple instances, the disks support concurrent read and write access from these ECS instances and provide high reliability, high concurrency, and high performance. Premium performance disks provide the multi-attach and I/O blocking features. After the multi-attach feature is enabled for a premium performance disk, the disk can be attached to up to 16 ECS instances at a time. You can run NVMe commands to manage the permissions of ECS instances on premium performance disks. For more information about NVMe commands, see NVM Express Base Specification. The preceding features improve service availability without compromising data reliability. If a single point of failure (SPOF) occurs, you can use a premium performance disk to quickly schedule and restore data. Data sharing among multiple ECS instances greatly reduces storage costs and improves service flexibility. Premium performance disks are suitable for high-availability databases and distributed database clusters that each consist of one write node and multiple read-only nodes. Premium performance disks can be attached to ECS instances that support NVMe. For example, after premium performance disks are attached to Linux instances based on NVMe, you can run the **lsblk** command to check the device names and partition names of the disks. Take note of the following parameters in the preceding figure: The device names of the premium performance disks are displayed in the `/dev/nvmeXn1` format. Examples: /dev/nvme0n1, /dev/nvme1n1, and /dev/nvme2n1. The partition names of the premium performance disks are displayed in the `<Device` `name>p<Partition number>` format. Examples: /dev/nvme0n1p1, /dev/nvme1n1p1, and /dev/nvme1n1p2. Premium performance disks provide the multi-attach feature and are used by enterprises to migrate high-availability services to the cloud. For more information, see Enable the multiattach feature. Before you attach premium performance disks to an ECS instance based on NVMe, the resources of the instance must meet the limits described in the following table.

| Instance family | By default, the instance family must support NVMe. The following instance families support NVMe: ecs.g7m-se-x25 ecs.g7s-se-x25 ecs.g7x-se-x25 ecs.g7x-se-x25 ecs.g7x-se-2numa-hg-k25 ecs.g7x-se-numaoff-hg-x25 ecs.g7x-se-numaoff-hg-x25 ecs.ebmg7m-se-numaoff-x25-c1m8 ecs.ebmg7s-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.ebmg6x-se-numaoff-hg-x25-c1m4 ecs.ebmg6x-se-numaoff-hg-x25-c1m8 ecs.ebmg7x-se-numaoff-hg-x25-c1m4 ecs.ebmg7x-se-numaoff-hg-x25-c1m8 Note You can call the DescribeInstanceTypes operation to query instance families and check whether the instance family supports NVMe based on the NvmeSupport parameter in the response. For more information, see the DescribeInstanceTypes topic in ECS Developer Guide. |
|---|---|
| Cloud disk | Disk category: premium performance disk. Creation method: Create premium performance disks when you create instances that support NVMe. When you create disks, select premium performance disks as the disk category and enable the multi-attach feature. |

Elastic Compute Service

**Related operations**

You can perform the following operations on premium performance disks that support NVMe: Create premium performance disks when you create ECS instances that support NVMe. In this case, the created premium performance disks support NVMe. For more information, see Create an instance. Enable the multi-attach feature when you separately create premium performance disks. For more information, see Enable the multi-attach feature. Format premium performance disks and create file systems. For more information, see Format a data disk for a Linux instance. Elastic Compute Service

**Important**

The preceding operations are applicable only to premium performance disks that are created together with instances but not to premium performance disks for which the multi-attach feature is enabled.

#### Enable the multi-attach feature

When you create a premium performance disk, you can enable the multi-attach feature for it. After you enable the feature, you can attach the disk to up to 16 Elastic Compute Service (ECS) instances that support the Non-Volatile Memory Express (NVMe) protocol in the same zone to allow concurrent read and write access from them.

**Benefits**

The multi-attach feature is suitable for high-availability databases and distributed database clusters that each consists of one write node and multiple read-only nodes. This feature provides the following benefits: Support for NVMe commands: This feature allows you to run NVMe commands to manage permissions of ECS instances on premium performance disks. This helps improve service availability without compromising data durability. For information about NVMe commands, see NVM Express Base Specification. Cross-instance data sharing: This feature enables data sharing across multiple ECS instances to reduce storage costs and improve service flexibility. Disaster recovery: This feature allows quick scheduling of services to healthy ECS instances for service continuity in single-point-of-failure (SPOF) scenarios. The following limits apply to the multi-attach feature: The following instance families support this feature. ecs.g7m-se-x25 ecs.g7s-se-x25 ecs.g7x-se-x25 ecs.g7x-se-x25 ecs.g7x-se-2numa-hg-k25 ecs.g7x-se-numaoff-hg-x25 ecs.g7x-se-numaoff-hg-x25 ecs.ebmg7m-se-numaoff-x25-c1m8 ecs.ebmg7s-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.ebmg6x-se-numaoff-hg-x25-c1m4 ecs.ebmg6x-se-numaoff-hg-x25-c1m8 ecs.ebmg7x-se-numaoff-hg-x25-c1m4 ecs.ebmg7x-se-numaoff-hg-x25-c1m8 Only data disks support this feature but system disks do not.

| Feature | Description |
|---|---|
| Disk attachment | One premium performance disk can be attached to up to 16 instances that support the NVMe protocol. |
| Release of disks together with instances | Not supported. |
| Disk re-initialization | Not supported. |
| Disk category change | Not supported. |
| Disk resizing | Only offline resizing of disks is supported. For information about how to resize disks offline, see Resize disks. |
| Snapshot-consistent group | Not supported. |

Elastic Compute Service The multi-attach feature can be enabled only when you create premium performance disks, and cannot be enabled or disabled after the disks are created. After the multi-attach feature is enabled for a premium performance disk, we recommend that you use cluster file systems such as Oracle Cluster File System version 2 (OCFS2), Global File System 2 (GFS2), Veritas Cluster File System (Veritas CFS), Oracle Automatic Storage Management Cluster File System (Oracle ACFS), and Databricks File System (DBFS) on the disk.

**Warning**

When a premium performance disk for which the multi-attach feature is enabled is attached to multiple ECS instances, data cannot be synchronized among the instances and data inconsistency may occur if file systems such as EXT2, EXT3, EXT4, XFS, and New Technology File System (NTFS) are used. The performance of premium performance disks is limited. When a premium performance disk is attached to multiple ECS instances, the total performance of the disk on all instances cannot exceed the maximum performance that can be provided by the disk. The following table describes the limits that apply to the features provided by premium performance disks for which the multi-attach feature is enabled.

**Use the multi-attach feature**

Perform the following steps to use the multi-attach feature:
1. Step 1: Create a premium performance disk for which the multi-attach feature is enabled
2. Step 2: Attach the premium performance disk to multiple ECS instances that support the

**Step 1: Create a premium performance disk for which the**

**multi-attach feature is enabled**

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization | Yes | Select an organization for which you want to create the disk. |
|  | Resource Set | Yes | Select a resource set in which you want to create the disk. |
|  | Region | Yes | Select a region in which you want to create the disk. |
|  | Zone | Yes | Select a zone in which you want to create the disk. |
|  | Creation Method | Yes | Select the method that you want to use to create the disk. Valid values: Disk Creation and Storage Set Creation. Note Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to its resources. You can use storage sets to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see the Create a storage set topic in CDS User Guide. |
|  | Storage Set | Yes | Select a storage set that you use to create the disk. Note This parameter is required if you set Creation Method to Storage Set Creation. |

Elastic Compute Service Enable the multi-attach feature when you create a premium performance disk.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Click **Create Disk**.
5. Configure the parameters described in the following table.

|  | Partition | Yes | Specify the number of partitions in the specified storage set that you use to create the disk. A storage set must contain two or more partitions. Note This parameter is required if you set Creation Method to Storage Set Creation. |
|---|---|---|---|
|  | Name | Yes | Enter a name for the disk that you want to create. If you create only one disk, the disk name must be 2 to 128 characters in length. If you create multiple disks at a time, the disk name must be 2 to 125 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
| Basic Configurations |  |  |  |
|  | Quantity | Yes | Enter the number of disks that you want to create. Valid values: 1 to 100. |
|  | Specifications | Yes | Select Premium Performance Disk. |
|  | Disk Size (GiB) | Yes | Specify a disk size in the range of 20 GiB to 32,768 GiB. |
|  | Multi-Attach | Yes | Select Yes to enable the multi-attach feature for the disk. |
|  | Encryption | No | Select whether to encrypt created disks. |
|  | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required if you set Encryption to Yes. Valid values: AES256 SM4 |

Elastic Compute Service

|  | Encryption Key | No | Select an encryption key for the disk. This parameter is required if you set Encryption to Yes. Note If no keys are available, create a key in Key Management Service. |
|---|---|---|---|
|  | Use Snapshot | No | Select whether to create the disk from a snapshot. If you select Yes, you must select a snapshot. In this case, the size of the created disk is determined based on the size of the selected snapshot. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is smaller than the snapshot size, the disk is created with the snapshot size. |

Elastic Compute Service

**Note**

For more information about how to create disks, see Create a disk.
6. Confirm the configurations and click **Confirm Order**.
7. In the message that appears, click **OK**.
After the disk is created, go back to the **Disks** page. The created disk that is in the
**Available** state and has the multi-attach feature **enabled**.

**Step 2: Attach the premium performance disk to multiple ECS**

Before you attach the premium performance disk to ECS instances, make sure that the following requirements are met: The disk and the instances reside in the same zone. The instance families and images of the ECS instances comply with the NVMe protocol. For more information, see the Limits section of the "Overview of disks that support NVMe" topic.
1. Obtain the IDs of the ECS instances to which you want to attach the disk.
In the left-side navigation pane, choose **Instances & Images > ECS Instance**. On the
**ECS Instances** page, view and copy the instance IDs in the instance list.
Elastic Compute Service
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. Find the premium performance disk that you created, click the
icon in the **Actions** column corresponding to the disk, and then select **Attach**.
4. In the **Attach** dialog box, select an instance ID from the **Instance** drop-down list and click
**OK**.
Select an instance ID that you obtained in Step 1 from the **Instance** drop-down list.

**Note**

You can attach the premium performance disk to only one ECS instance at a time. To attach the disk to multiple ECS instances, repeat the preceding steps. You can go to the **Disks** page to view the status of the premium performance disk. The status of the disk changes to **Running**. You can click the name of the premium performance disk to go to the **Disk Details** page. In the **Attachment Information** section on the Disk Details tab, you can view attachment information about the disk.

**What to do next**

After you enable the premium performance disk and attach the disk to multiple ECS instances, we recommend that you create cluster file systems. Common cluster file systems include OCFS2, GFS2, Veritas CFS, Oracle ACFS, and DBFS.

**Warning**

When a premium performance disk for which the multi-attach feature is enabled is attached to multiple ECS instances, data cannot be synchronized among the instances and data inconsistency may occur if file systems such as EXT2, EXT3, EXT4, XFS, and New Technology File System (NTFS) are used.

### Encrypt a disk

#### Overview

Elastic Compute Service Disk encryption is a simple and secure method provided by Elastic Compute Service (ECS) to encrypt new disks. Disk encryption eliminates the need to create or maintain your own key management infrastructure, to modify existing applications and maintenance procedures, and to perform additional encryption operations. Disk encryption does not have negative impacts on your business. The following types of data can be encrypted in disk encryption operations: Data stored on disks. Data transmitted between disks and instances. Data within instance operating systems is not encrypted. All snapshots created from encrypted disks. These snapshots are encrypted snapshots. Data transmitted from instances to disks is encrypted on the hosts where the instances reside. Ultra disks, standard SSDs, premium performance disks, and standard performance disks can be encrypted by using disk encryption.

**Note**

By default, shared SSDs and shared ultra disks cannot be encrypted by using disk encryption. To create and encrypt shared SSDs or shared ultra disks, submit a ticket.

#### Encrypt a system disk

In the scenarios that require data security and regulatory compliance, you can encrypt disks to secure your data that is stored in Elastic Compute Service (ECS).

**Background information**

The following methods are supported to encrypt a system disk: Method 1: Enable system disk encryption when you create an ECS instance. This method is supported only for premium performance disks and standard performance disks. Method 2: Encrypt a custom image and use it to create an ECS instance. The system disk of the created ECS instance is automatically encrypted. This method is supported for all disk categories.

**Method 1: Enable system disk encryption when you create an**

**Note**

This method is supported only for premium performance disks and standard performance disks.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Instances & Images > ECS Instances**.
3. Click **Create Instance**.
4. In the **System Disk** section, select **Encryption** and configure the following parameters:
**Encryption Method**: You can select the **AES256** algorithm.
**Encryption Key**: Select an encryption key from the drop-down list.
For more information about other disk configuration parameters, see Create a disk.
5. Click **Confirm Order**.

| Parameter | Description |
|---|---|
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
| Sharing Scope | Select the scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Description | Enter a description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

Elastic Compute Service

**Method 2: Encrypt a custom image and create an ECS instance**

**from the image to encrypt the system disk**

The following procedure describes how to encrypt a system disk by encrypting a custom image and using the image to create an ECS instance:
1. (Optional) Step 1: Create a custom image from an instance
2. (Optional) Step 2: Encrypt the custom image
3. Step 3: Use the encrypted custom image to create an instance
If you have created a custom image and encrypted the image, skip Step 1 and Step 2 and proceed to use the encrypted image to create an instance.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance from which you want to create a custom image. In the **Actions** column,
click the icon and then choose **Disk and Image > Create Custom Image**.
5. Configure the parameters that are described in the following table.
6. Click **OK**.

**Step 2: Encrypt the custom image**

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.

| Parameter | Description |
|---|---|
| Image ID | The system automatically obtains the ID of the image. You do not need to configure this parameter. |
| Name | Enter a name for the new encrypted custom image. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with acs: or aliyun . The name cannot contain http:// or https:// and can contain letters, digits, periods (.), colons (:), underscores ( ), and _ hyphens (-). |
| Description | Enter a description for the new encrypted custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

Elastic Compute Service
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Find the image that you want to manage. In the **Actions** column, click the
icon and then select **Encrypt Image**.
6. In the **Encrypt Image** dialog box, configure the parameters that are described in the
following table. 7.
8. Click **OK**.

**Step 3: Use the encrypted custom image to create an instance**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance**.
5. On the Create Instance page, configure the parameters.
For more information about how to configure the parameters to create an instance, see Create an instance by using the wizard. In the **Image ID** section, click **Custom Image** and select the custom image that you encrypted in Step 2: Encrypt the custom image from the **Custom Image** drop-down list.
6. Click **Submit**.

**Result**

Elastic Compute Service After the instance is created, you can click its ID to go to the **Instance Details** page. Then, you can click the **Disks** tab and check the value in the **Encrypted** column corresponding to the system disk. If the value is **Yes**, the system disk is encrypted.

#### Encrypt a data disk

In the scenarios that require data security and regulatory compliance, you can encrypt data disks to secure your data stored on Elastic Compute Service (ECS) instances. After a data disk is created, its encryption state cannot be changed. If you want to encrypt a data disk, enable encryption for the disk when you create it.

**Background information**

We recommend that you determine the number and sizes of data disks before you create them. Take note of the following limits:

**Note**

System disks cannot be separately created. The maximum number of data disks that can be attached to a single ECS instance varies based on the instance type. A single premium performance disk for which the multi-attach feature is enabled can be attached to up to 16 ECS instances at the same time. Each ultra disk, shared ultra disk, standard SSD, shared standard SSD, premium performance disk, or standard performance disk can be up to 32,768 GiB in size. Disks cannot be combined in ECS and are independent of each other. You cannot format multiple disks to combine them into a single disk. A snapshot can back up data only of a single disk. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across disks. If you use LVM to create a logical volume across multiple disks, data discrepancy may occur when you restore disks from snapshots.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Disk**.
5. On the Create Disk page, configure the parameters.
If you want to encrypt the data disk, take note of the following parameters:
**Encryption**: Select **Yes**.
**Encryption Method**: Select an encryption algorithm. Valid values:

**AES256**

**SM4**

**Encryption Key**: Select an encryption key from the drop-down list.
For information about other disk parameters, see Create a disk.
6. Click **Submit**.

| Parameter | Description |
|---|---|
| Password | Reset the password used to log on to the instance. You can retain the original password or specify a new password. |
| Confirm Password |  |
| Instance Startup Policy | If you select Start Instance After Re-initializing Disk, the instance automatically starts after you re-initialize the system disk. |

Elastic Compute Service

### Re-initialize disks

#### Re-initialize a system disk

This topic describes how to re-initialize a system disk. After a system disk is re-initialized, it is restored to the state that it was in when it was created.

**Prerequisites**

The system disk that you want to re-initialize is in the **Running** state. The Elastic Compute Service (ECS) instance to which the system disk is attached is in the
**Stopped** state.
After a disk is re-initialized, the data stored on the disk is lost and cannot be recovered. Exercise caution when you perform this operation. We recommend that you back up disk data or create snapshots before you re-initialize a disk. For more information, see Create a snapshot.

**Background information**

The result of disk re-initialization depends on the disk type and how the disk was created. For the system disk that is attached to an instance, you can re-initialize the disk to restore it to the state that it was in when it was created. The following changes take place after the system disk is re-initialized: The system disk is restored to the state that it was in when it was created.

**Warning**

When the system disk is re-initialized, all data stored in the disk is deleted. We recommend that you create snapshots for the disk to back up data before you re-initialize the disk. The automatic snapshot policy applied to the system disk before the re-initialization remains valid. The IP addresses and disk IDs of the instance remain unchanged. The automatic and manual snapshots of the system disk remain available. You can use these snapshots to roll back the disk. For more information, see Roll back a disk by using a snapshot.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the system disk that you want to re-initialize and click **Reinitialize Disk** in the
**Actions** column.
5. In the **Reinitialize Disk** dialog box, configure the parameters described in the following
table.

| vim /etc/fstab |  |  |
|---|---|---|
| e | I | key to ente |

Elastic Compute Service
6. Click **OK**.

**Result**

While the disk is being re-initialized, the disk is in the **Initializing** state. When the disk is reinitialized, it enters the **Running** state.

**What to do next**

If data disks are attached to a Linux instance before its system disk is re-initialized, you must re-create mount points for the partitions of the data disks and mount file systems to these partitions.

**Note**

After you re-initialize the system disk of a Linux instance, data stored in the data disks attached to the instance remains unchanged, but the mount information of the data disks is lost. You must re-create mount points for the partitions of the data disks and mount file systems to these partitions. After the system disk is re-initialized, you must redeploy applications and configurations to restore your business. If you have created a snapshot for the system disk before the system disk is re-initialized, you can use the snapshot to create a data disk and attach the data disk to the instance to obtain data that was originally stored in the system disk. For more information, see Create a snapshot.

#### Re-initialize a data disk

When a data disk is attached to an Elastic Compute Service (ECS) instance, you can reinitialize the disk to restore it to the state when it is created.

**Prerequisites**

Snapshots are created for your data disk. For more information, see Create a snapshot. The data disk is attached to an ECS instance. For more information, see Attach data disks. The ECS instance is in the **Stopped** state. For a Linux instance, if you create an empty data disk and add a command in the /etc/fstab file to mount partitions of the data disk on system startup, the command is not executed and the instance cannot start as expected after you re-initialize the data disk. We recommend that you comment out the command in the /etc/fstab file. Perform the following steps: i. Connect to the instance. For more information, see Overview. iv. Find the command used to mount data disk partitions and comment out the command by using a number sign (
#), as shown in the following command line.

```bash
# /dev/vdb1 /InitTest ext3 defaults 0 0
```

**Note**

In this example, /dev/vdb1 is a partition and /InitTest is a mount point. You can modify the command based on your business requirements. `:wq` to save the file and exit. v. Press the `Esc` key to exit the edit mode, and enter

**Background information**

The state of a data disk after it is re-initialized varies based on its original state when it was Elastic Compute Service created and the operating system that the instance runs: The data disk is restored to the initial state when it was created: The data disk becomes an empty disk if it was originally an empty disk. The data disk stores the data recorded in the source snapshot if the data disk was created from a snapshot. For a Windows instance, after you re-initialize a data disk, the data disk is ready for use without the need for additional operations regardless of its original state. For a Linux instance: If a data disk was created from a snapshot, the data disk stores only the data recorded in the source snapshot after the data disk is re-initialized. You do not need to re-mount the partitions, but all the data generated after the disk was created is lost. If a data disk was created as an empty disk, all the data and file systems on the disk are lost after the data disk is re-initialized. You must reformat and partition the disk, and then re-mount the partitions.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to re-initialize, and click **Re-initialize Disk** in the **Actions**
column.
5. In the **Re-initialize Disk** dialog box, click **OK**.

**What to do next**

For a Linux instance, if the data disk was created as an empty disk, you must format the data disk after you re-initialize it. For more information, see Format a data disk for a Linux instance. After the data disk is re-initialized, you must redeploy the applications and reconfigure the parameters on the disk to restore your business at the earliest opportunity.

### Detach data disks

If a data disk is no longer needed by an Elastic Compute Service (ECS) instance, you can detach the disk from the instance. You can also detach a data disk from an instance and then attach the disk to another instance within the same zone. This topic describes how to detach data disks.

**Prerequisites**

Before you detach a data disk, make sure that the following conditions are met: The disk is attached to an instance and **Running** is displayed in the **Status** column that corresponds to the disk in the ECS console. To prevent data loss and ensure data integrity, we recommend that you stop read and write operations on the data disk before you detach the disk.

**Background information**

To detach a data disk, perform the following steps. Elastic Compute Service

**Note**

Local disks that are used as data disks cannot be detached.
1. If file systems are mounted to the partitions of a data disk, detach the data disk from within
the operating system of the instance to which the data disk is attached. For more information, see the Step 1: Detach data disks from within the operating system of the associated instance section of this topic.
2. On the Disks page, detach the data disk.
For more information, see the Step 2: Detach data disks on the Disks page section of this topic.

**Step 1: Detach data disks from within the operating system of**

**the associated instance**

If a data disk is partitioned and file systems are mounted on the disk, perform the following operations to detach the data disk from within the operating system of the ECS instance to which the disk is attached.
1. Use Workbench to connect to the Linux ECS instance.
2. Run the following command to view the mount information of the data disk:

```
df -h
```

The following sample command output is returned. In this example, the /dev/vdb1 partition of the data disk is used. In actual scenarios, select the data disk partitions whose mounting information you want to view.
3. Run the umount command to unmount the file systems from the data disk partitions.
For example, you can run the following command to unmount the file system of the /dev/vdb1 partition:

```
umount /dev/vdb1
```

4. Run the following command to view the UUIDs of the data disk partitions:

```
blkid
```

The following sample command output indicates the UUID of the /dev/vdb1 partition of the data disk.
5. Run the following command to check whether automatic mounting is configured in the
/etc/fstab file for the file systems in the data disk partitions: Elastic Compute Service

```
cat /etc/fstab
```

Find the UUID that you obtained in the previous step in the command output. The file system of the /dev/vdb1 partition is configured in the /etc/fstab file, as shown in the following figure.
6. Delete the automatic mounting configurations of the file systems in the data disk partitions
from the /etc/fstab file.

**Note**

If you do not delete the automatic mounting configurations of the file systems in the data disk partitions from /etc/fstab, the ECS instance cannot be restarted after you detach the data disk from the instance. i. Run the following command to modify the /etc/fstab file:

```
vim /etc/fstab
```

ii. Press the I key to enter the Insert mode. iii. Delete or comment out the automatic mounting configurations of the file systems in the data disk partitions. For example, you can add a number sign ( # ) before a line that contains automatic mounting configuration to comment out the configuration, as shown in the following figure. iv. Press the Esc key, enter `:wq` , and then press the Enter key to save your changes and exit the Insert mode.
1. Use Workbench to connect to a Windows ECS instance.
2. On the Windows Server desktop, right-click the
icon and select **Disk Management**.
3. In the **Disk Management** window, right-click the disk that you want to detach and select
**Offline**.
Elastic Compute Service You can detach data disks on the Instance or Disks page. Perform the following steps to detach data disks on the Instance page in the ECS console:
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance and click the instance ID.
5. On the **Instance Details** page, click the **Disks** tab.
6. Select the data disks that you want to detach and click **Batch Detach**.

**Note**

You can select up to five disks to be detached at a time. To detach multiple disks, the system executes the DetachDisk operation in serial mode. If a DetachDisk operation fails, the operation is skipped. You can retry the failed operation after all other DetachDisk operations are complete.
7. In the dialog box that appears, confirm the disks that you want to detach and the impact,
and click **Detach**.

**Verify the result**

After you perform the preceding steps to detach disks, you can choose **Storage &**
**Snapshots > Disks** to find the disks on the Disks page. If **Available** is displayed in the
**Status** column, the disks are detached.

**What to do next**

You can attach data disks to another ECS instance within the same zone. For more information, see Attach disks. If you no longer need a data disk that you detached, you can back up the data stored on the disk and then release the disk. For more information, see Create a snapshot and Release a data disk.

### Storage sets

#### Overview

| EBS Business 1 Clusters rtitionsPartition 1 Partition 2 Partition... Cluster 1 Cluster 2 Cluster 3 Cluster 4 Cluster 5 Cluster 6 Cluster 7 Cluster... |  |
|---|---|
| Cluster 5 | Cluster... |

| Business 2 Partition 1 Partition 2 Partition... Cluster 1 Cluster 2 Cluster 3 Cluster 4 Cluster 5 Cluster 6 Cluster 7 Cluster... |  |
|---|---|
| Cluster 5 | Cluster... |

Elastic Compute Service You can classify Elastic Block Storage (EBS) clusters based on dimensions such as business type, and associate EBS clusters with different partitions in a storage set. This allows you to isolate EBS clusters by business type.

**Relationship between storage sets, partitions, and EBS clusters**

A storage set is a logical carrier that controls the distribution of disks. A storage set is divided into 2 to N partitions, and a partition can be associated with 1 to N EBS clusters. This allows you to isolate EBS clusters by business type. EBS Clusters The number of partitions in a storage set must be greater than or equal to 2. A cluster can be associated with the partitions of different storage sets. However, a cluster can be associated with only one partition within a storage set. After you create a storage set, you cannot change the number of partitions within the storage set.

**Procedure**

1. Create a storage set and configure partitions.
For more information, see Create a storage set.
2. Associate clusters with partitions.
For more information, see the **Manage storage sets** topic in **Hybrid Cloud Storage**
**Operations and Maintenance Guide**.
3. Specify a storage set and partitions when you create a disk.
For more information, see Create a disk.

#### Create a storage set

You can classify Elastic Block Storage (EBS) clusters based on dimensions such as business type, and associate EBS clusters with different partitions in a storage set. This allows you to isolate EBS clusters of different business types.

**Background information**

When you create a storage set, take note of the following items: The number of partitions in a storage set must be greater than or equal to 2.

| Parameter | Description |
|---|---|
| Organization | The organization to which the storage set belongs. |
| Resource Set | The resource set to which the storage set belongs. |
| Region | The region in which you want to create the storage set. |
| Zone | The zone in which you want to create the storage set. |
| Sharing Scope | The sharing scope of the storage set. You can select the storage set when you create disks for the organizations or resource sets within the specified sharing scope. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |

Elastic Compute Service If you want to create a disk in an EBS cluster, you must create a storage set and associate the EBS cluster with a partition of the storage set in the CDS Ops console, which is the unified O&M platform of Cloud Defined Storage (CDS). Then, select the storage set and partition with which the EBS cluster is associated when you create a disk by using the storage set in the Elastic Compute Service (ECS) console.

**Procedure**

1. You can create a storage set in the ECS console or the EBS console.
a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Computing > Elastic Compute**
**Service**.
c. In the left-side navigation pane, choose **Storage & Snapshots > Storage Set**. ii. Method 2: Create a storage set in the EBS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Storage > Elastic Block Storage**. c. In the left-side navigation pane, choose **Enterprise-Grade Capabilities > Storage**
**Set**.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. On the **Storage Set** page, click **Create Storage Set**.
4. In the **Create Storage Set** panel, configure the parameters and click **OK**. The following
table describes the parameters.

| Storage Set Name | The name of the storage set. It is the unique identifier of the storage set. The name must meet the following requirements: The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, periods (.), colons (:), underscores ( ), and hyphens (-). _ |
|---|---|
| Partition Settings | The names of the partitions in the storage set. The name must meet the following requirements: The name must be 2 to 64 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, periods (.), colons (:), underscores ( ), and hyphens (-). _ At least two partitions are required. You can click Add Partition to add more partitions. |

Elastic Compute Service

**What to do next**

After you create a storage set, you can click the ID of the storage set and create a disk in the storage set. For more information, see Create a disk.

#### View storage sets

This topic describes how to view the existing storage sets and their details.

**Procedure**

1. You can view storage sets in the Elastic Compute Service (ECS) or Elastic Block Storage
(EBS) console. i. Method 1: View storage sets in the ECS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Computing > Elastic Compute**
**Service**.
c. In the left-side navigation pane, choose **Storage & Snapshots > Storage Set**. ii. Method 2: View storage sets in the EBS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Storage > Elastic Block Storage**. c. In the left-side navigation pane, choose **Enterprise-Grade Capabilities > Storage**
**Set**.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. On the **Storage Set** page, select a filter condition from the drop-down list, enter relevant
information in the search box, and then click the specified filter condition are displayed.

| Filter condition | Description |
|---|---|
| Storage Set ID | Enter the full ID of a storage set to search for the storage set. Only exact match is supported. Fuzzy match is not supported. |
| Storage Set Name | Enter the name of a storage set to search for the storage set. Fuzzy match is supported. |

Elastic Compute Service

#### Modify a storage set

After you create a storage set, you can modify the name or sharing scope of the storage set based on your business requirements.

**Modify the name of a storage set or partition names**

1. Modify the name of a storage set in the Elastic Compute Service (ECS) console or Elastic
Block Storage (EBS) console. i. Method 1: Modify the name of a storage set in the ECS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Computing > Elastic Compute**
**Service**.
c. In the left-side navigation pane, choose **Storage & Snapshots > Storage Set**. ii. Method 2: Modify the name of a storage set in the EBS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Storage > Elastic Block Storage**. c. In the left-side navigation pane, choose **Enterprise-Grade Capabilities > Storage**
**Sets**.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. On the **Storage Set** page, find the storage set that you want to modify and click **Modify** in
the **Actions** column.
4. In the **Modify Storage Set** dialog box, modify the name of the storage set and partition
names and click **OK**.

**Modify the sharing scope of a storage set**

1. Log on to the ECS console.
i. Log on to the Apsara Uni-manager Management Console ii. In the top navigation bar, choose **Products > Computing > Elastic Compute Service**.
2. In the left-side navigation pane, choose **Storage & Snapshots > Storage Set**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Storage Set** page, find the storage set whose sharing scope you want to modify
and click **Configure Sharing Settings** in the **Actions** column.
5. In the dialog box that appears, modify the sharing scope of the storage set and click **OK**.

#### Delete a storage set

Elastic Compute Service This topic describes how to delete a storage set that is no longer needed.

**Background information**

When you delete a storage set, take note of the following items: If a disk exists in the storage set to be deleted, the system reports an error. Before you delete a storage set, you must check whether disks exist in the storage set and release the existing disks. To release the existing disks, perform the following operations: On the **Storage Set** page of the Elastic Block Storage (EBS) console, find the storage set that you want to delete and click its ID. The **Disks** page in the Elastic Compute Service (ECS) console appears. On the Disks page, you can view the disks in the storage set. For more information about how to release a disk, see Release a data disk.

**Procedure**

1. Delete a storage set in the ECS console or the EBS console.
i. Method 1: Delete a storage set in the ECS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Computing > Elastic Compute**
**Service**.
c. In the left-side navigation pane, choose **Storage & Snapshots > Storage Set**. ii. Method 2: Delete a storage set in the EBS console. a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, choose **Products > Storage > Elastic Block Storage**. c. In the left-side navigation pane, choose **Enterprise-Grade Capabilities > Storage**
**Sets**.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. On the **Storage Set** page, find the storage set that you want to delete and click **Delete** in
the **Actions** column.
4. In the message that appears, click **OK**.

### Release a data disk

You can manually release disks that are no longer needed. When a disk is released, all data stored on the disk is deleted. This topic describes how to release a data disk on the Disks page.

**Prerequisites**

A snapshot is created for the data disk that you want to release to back up disk data. For more information, see Create a snapshot. The data disk is in the **Available** state. If the data disk is attached to an instance, you must detach the disk before you can release it. For more information, see Detach data disks.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to release, click the
icon in the **Actions** column, and Elastic Compute Service then click **Release**.
5. In the message that appears, click **Release**.

| Image type | Description | References |
|---|---|---|

Elastic Compute Service

## Images

### Overview

This topic describes the concepts, types, and formats of images and how to view the information of an image. An image is a template for running environments within Elastic Compute Service (ECS) instances. An image includes an operating system and pre-installed applications. An image works as a copy that stores data from one or more disks. An ECS image may store data from a system disk or from both system and data disks. You can use an image to create an ECS instance or replace the system disk of an ECS instance.

**Image types**

ECS images are classified into public images, custom images, shared custom images, and globally shared images based on image sources.

**Note**

Image types and image versions are displayed in the ECS console.

| Public images | Public images provided by Alibaba Cloud in Apsara Stack support the following Windows Server operating systems and mainstream Linux operating systems. | Overview of public images |
|---|---|---|
| Custom images | Custom images are created from instances or snapshots or are imported from your on-premises device. | Overview of custom images |
| Shared custom images | These images are shared with your organization by other Level-1 organizations. | Overview of shared images |
| Globally shared images | These images are custom images that are globally shared by administrators in the Apsara Uni-manager Operations Console. Globally shared images can be viewed and used by all organizations. | Overview of globally shared images |

| Image type | References |
|---|---|
| Public images | Find a public image |
| Custom images | View a custom image |
| Shared images | Find a shared custom image |
| Globally shared images | Find a globally shared image |

Elastic Compute Service

**Find an image**

You can find an image based on its type, name, ID, or the ID of the snapshot from which the image was created. Then, you can use the image to create instances or perform other operations. The following table provides links to the relevant references.

**Image formats**

ECS supports images in the VHD, RAW, and QCOW2 formats. Images in other formats must be converted to the supported formats before they can be run in ECS. For more information, see Convert the format of an image.

### View instances that use a

**specific image**

You can view instances that use a specific image to obtain the usage details of the image.

| Image type | Operation |
|---|---|
| Custom Image | Choose ECS Image > Custom Image. Note To quickly find and manage custom images that are shared by the current organization, choose ECS Image > Shared Image > Shared by Me. |
| Public Image | Choose ECS Image > Public Image. |
| Shared Image | i. Choose ECS Image > Shared Image. ii. Click Shared. |
| Shared Globally | i. Choose ECS Image > Shared Image. ii. Click Shared Globally. |

Elastic Compute Service

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click a tab that corresponds to the type of the image that you want to view.
The following table describes the operations that you can perform to go to each tab on the Images page.
5. Find the image and click **Related Instances** in the **Actions** column.

**Result**

Instances that use the specified image are displayed on the Instances page. You can continue to perform other operations on the instances, such as updating the image.

### Custom images

#### Overview of custom images

Custom images are created from Elastic Compute Service (ECS) instances or snapshots or imported from your on-premises device. Custom images can contain applications and data. You can use custom images to create instances that have identical configurations. This eliminates the need to make repeated configurations.

**Procedure**

After you create or import a custom image, the image is in the **Available** state. You can share the image with other organizations, export the image to an Object Storage Service (OSS) bucket, or use the image to create instances. If you no longer need the image, you can delete the image.

| Operation | Description | References |
|---|---|---|
| Create an image | You can create a custom image from an instance or from a snapshot to copy the system environment. This eliminates the need to make repeated configurations. | Create a custom image |
| Modify an image | You can modify the name and description of a custom image. | Modify the attributes of a custom image |
| Find an image | You can view all custom images in the current organization, region, and resource set in the ECS console. You can find a specific image by image name or ID. | View a custom image |
| View instances related to an image | You can view instances that were created from a specific image to obtain image usage information. | View instances that use a specific image |

Elastic Compute Service

**Note**

Only the creator of a custom image can use, share, copy, and delete the image. The following figure shows how to use a custom image.

**Related operations**

The following table describes the operations that you can perform on custom images.

| Share an image | After you create a custom image, you can share the image with other organizations. After the image is shared, you can go to the ECS Image tab of the Images page, click the Shared Image tab, and then click Shared by me to view the image. | Share a custom image Modify the sharing scope of a custom image |
|---|---|---|
| Encrypt a custom image | You can encrypt custom images as needed. After a custom image is encrypted, you can use the encrypted custom image to create instances that have encrypted system disks. This helps meet data security and compliance requirements. | Encrypt a custom image |
| Configure the boot mode of an image | You can specify Basic Input Output System (BIOS) or Unified Extensible Firmware Interface (UEFI) as the boot mode of a custom image based on your business requirements. | Configure the boot mode of a custom image |
| Import an image | You can import a custom image from your on-premises device. | Alibaba Cloud image specifications for Linux. |
| Export a custom image | You can export a custom image that you created to an OSS bucket and then download the image to your on-premises device. | Export a custom image |
| Delete an image | You can delete a custom image that you no longer need. | Delete custom images |

Elastic Compute Service

#### Create a custom image

You can create a custom image and use it to create identical instances or replace the system disks of existing instances. You can create a custom image from a system disk snapshot to load the operating system and data environment of the snapshot to the image. Before you perform this operation, make sure that the snapshot to use is a system disk snapshot. Custom images cannot be created from only data disk snapshots.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.

| Parameter | Description |
|---|---|
| Sharing Scope | Select the scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
| Image Description | Enter a description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

| Parameter | Description |
|---|---|

Elastic Compute Service
4. Find a system disk snapshot. If **System Disk** is displayed in the **Disk Type (ALL)** column
corresponding to a snapshot, the snapshot is a system disk snapshot. In the **Actions** column, click **Create Custom Image**.
5. Configure the parameters that are described in the following table.
6. Click **OK**.
You can create a custom image from an instance to replicate the data of the system disk and data disks on the instance.

**Note**

To prevent data security risks, we recommend that you delete sensitive data from an instance before you use the instance to create a custom image. When you create a custom image from an instance, a snapshot is automatically generated for each disk on the instance, and all the snapshots constitute a complete custom image.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance from which you want to create a custom image. In the **Actions** column,
click the icon and then choose **Disk and Image > Create Custom Image**.
5. Configure the parameters that are described in the following table.

| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
|---|---|
| Sharing Scope | Select the scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Description | Enter a description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

Elastic Compute Service
6. Click **OK**.

#### Modify the attributes of a custom

**image**

To facilitate custom image management, you can modify the attributes of a custom image. The attributes include the image name and description.

**Background information**

You can share a custom image with other organizations. After you share the image, you can modify the name or description of the image in the custom image list or shared image list. For more information, see Share a custom image. You can modify the attributes of only custom images, including custom images that are shared with other organizations. Public images and images that are shared by others cannot have their attributes modified.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Find the custom image that you want to manage and click **Edit** in the **Actions** column.
6. In the **Edit** dialog box, modify the name and description of the custom image.

| Filter condition | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. Fuzzy search is supported. |
| Image Name | Enter an image name to search for the image. Fuzzy search is supported. |
| Snapshot ID | Enter a snapshot ID to search for the images that are associated with the snapshot. Fuzzy search is supported. |

Elastic Compute Service
**Image Name**: The name must be 2 to 128 characters in length. The name cannot start
with a digit or special character. The name can contain underscores (_), hyphens (-), and colons (:).
**Description**: The description must be 2 to 256 characters in length. The description
cannot start with `http://` or `https://` .
7. Click **OK**.

#### View a custom image

You can view all the custom images that are available in the current organization, region, and resource set and the details of each custom image in the Elastic Compute Service (ECS) console. You can search for a custom image by image-related information such as image name. Then, you can create instances from the image or perform other operations on the image.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Select a filter condition from the drop-down list and enter relevant information in the
search box. The custom images that meet the specified filter condition are automatically displayed.

| Filter by Tag | Select the tag key and tag value to search for the images to which the tag is added. Note On the Images page, select images whose tags you want to manage and click Batch Add Tags or Batch Remove Tags in the lower part of the page to add tags to or remove tags from the selected images at a time. |
|---|---|

Elastic Compute Service
6. Click the image ID in the **Image ID/Name** column to view the basic information and
operation logs of the image. On the **Basic Information** tab, view the information, such as image name, image ID, operating system, platform, and snapshot details. Click the **Operation Log** tab to view the information about the operation logs of the custom image, including the operation name, operator, execution status, operation source (console call or API call), operation type, source IP address of the operation, and operation time. Search for operation logs that you require by specifying filter conditions. Select a filter condition from the drop-down list and enter the corresponding information in the search box to search operation logs. The operation logs that meet the specified filter condition are displayed. Click **Advanced Filter**, specify multiple filter conditions, and then click **Search** to search operation logs. Click **Operation Details** in the Actions column of an operation to view the operation details.

**Note**

**What to do next**

After you find an image that matches the preceding filter condition, you can perform the following operations: Create an instance from the image. For more information, see Create an instance. Share the image. For more information, see Share a custom image. Encrypt the image. For more information, see Encrypt a custom image. Export the image. For more information, see Export a custom image. Delete the image. For more information, see Delete a custom image. Modify the name and description of the custom image. For more information, see Modify the attributes of a custom image.

#### Share a custom image

##### Share a custom image

You can share a created custom image with other organizations. Then, the organizations can use the shared image to create instances that have identical environments. Elastic Compute Service

**Background information**

Only custom images can be shared. Shared images do not count against the image quotas of the organizations with which the images are shared. The organizations with which images are shared can use the shared images to create instances or replace the system disks of existing instances. You can delete shared images. After a shared image is deleted, the image is no longer visible to the organizations with which the image was shared and the system disks of the instances that were created from the shared image can no longer be re-initialized. Each custom image can be shared with up to 50 organizations. Each time a custom image can be shared with up to 10 organizations.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **ECS Image** tab and then click the **Custom Image** tab to view the custom image
list.

**Note**

If you want to quickly find the custom image that is shared by the current organization and reshare the image, choose **Shared Image > Shared by Me**.
5. Find the image that you want to manage, click the
icon in the **Actions** column, and then choose **Configure Sharing Settings > Share Image**.
6. In the **Share Image** dialog box, select the organization with which you want to share the
image from the **Organization** drop-down list.

**Note**

If no organization list is available due to a lack of permissions, you can enter the name of a level-1 organization in the Organization field.
7. Click **OK**.

**Result**

You can choose **Shared Image > Shared by Me** to view the shared custom image list.

**Related operations**

After the custom image is shared, you can perform the following operations based on your business requirements: Remove an organization from the sharee list of the image: In the **Share Image** dialog box, find the organization with which you want to unshare the image in the **Shared Information** list, click the icon in the **Actions** column, and then click **OK**.

**Important**

Elastic Compute Service If all organizations with which the custom image is shared are deleted, the custom image is removed from the shared by me image list. You can choose **Shared Image >**
**Shared by Me** to view the shared by me image list.
Add an organization to the sharee list of the image: In the **Share Image** dialog box, select the organization that you want to add in the
**Organizations** drop-down list and click **OK**.

##### Modify the sharing scope of a custom

**image**

You can modify the sharing scope of a custom image.

**Procedure**

**Important**

If a custom image is shared with the current organization (including the subordinate organizations) and the current resource set and you shrink the sharing scope, specific users no longer have permissions to manage the custom image. Proceed with caution.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Perform the following operations to modify the sharing scope of the custom image:
Modify the sharing scope of a single custom image a. In the custom image list, find the custom image and click the icon in the **Actions** column. b. Choose **Configure Sharing Settings > Modify Sharing Scope**. c. In the **Modify Sharing Scope** dialog box, configure Sharing Scope. Valid values of Sharing Scope: **Current Organization and Subordinate**
**Organizations**, **Current Resource Set**, and **Current Organization**.
d. Click **OK**. Modify the sharing scopes of multiple custom images

**Important**

You can modify the sharing scopes of up to 20 custom images at a time. a. In the custom image list, select multiple custom images and click **Modify Sharing**

| Parameter | Description |
|---|---|
| Image ID | The system automatically obtains the ID of the image. You do not need to configure this parameter. |

Elastic Compute Service
**Scope** in the lower part of the page.
b. In the **Modify Sharing Scope** dialog box, configure Sharing Scope. Valid values of Sharing Scope: **Current Organization and Subordinate**
**Organizations**, **Current Resource Set**, and **Current Organization**.
c. Click **OK**.

#### Encrypt a custom image

This topic describes how to encrypt a custom image to generate a new encrypted custom image.

**Prerequisites**

The custom image is in the **Available** state. Custom images in VHD format cannot be encrypted. Make sure that your image is not in VHD format.

**Background information**

To meet compliance requirements for data security, you can use encrypted custom images to create instances. The system disks of the created instances are automatically encrypted.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Find the image that you want to manage. In the **Actions** column, click the
icon and then select **Encrypt Image**.
6. In the **Encrypt Image** dialog box, configure the parameters that are described in the
following table. 7.

| Name | Enter a name for the new encrypted custom image. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with acs: or aliyun . The name cannot contain http:// or https:// and can contain letters, digits, periods (.), colons (:), underscores ( ), and _ hyphens (-). |
|---|---|
| Description | Enter a description for the new encrypted custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

Elastic Compute Service
8. Click **OK**.

**Results**

When the encrypted custom image is being created, you cannot view the creation status of the image in the custom image list. You can choose **Storage & Snapshots > Snapshots** in the left-side navigation pane to view the creation status of the system disk snapshot and data disk snapshots that are contained in the image on the **Disk Snapshots** tab. The disk snapshots are in the **Creating** state. After encryption is complete, you can find a new encrypted custom image and view the name and description of the encrypted image on the Custom Image tab.

#### Set the boot mode of a custom image

The boot mode is the mode in which the system disk is booted during instance creation. In Elastic Compute Service (ECS), two boot modes are supported: Unified Extensible Firmware Interface (UEFI) and Basic Input/Output System (BIOS). This topic describes how to set the boot mode for a custom image.

**Precautions**

Before you modify the boot mode of a custom image, take note of the following items: You cannot modify the boot mode of a custom image that is used by existing instances. When specify an instance type during instance creation, you can only select an **image** that is supported by the instance type and has a boot mode configured. After you select a custom image to create an instance, the boot modes that are supported by the image are displayed in the ECS console. After you change the boot mode of a custom image to UEFI, the instances that were created from the image start in UEFI mode. Make sure that configurations of the custom image support the UEFI boot mode. Otherwise, the instances cannot start.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

| Understand the Create a virtual requirements for machine and install importing images to an operating system Alibaba Cloud ECS | Install the NVMe driver Install cloud-init Install the virtio driver (Optional) Create a Linux custom image | Obtain the image file Check and Import the Create an repair the custom image ECS instance image Convert the format of the image |
|---|---|---|

Elastic Compute Service

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Find the image that you want to manage and choose
> **Startup Mode** in the **Actions**
column.
6. In the **Startup Mode** dialog box, configure Startup Mode.
You can set Startup Mode to **BIOS** or **UEFI**.
7. Click **OK**.

**View the results**

In the custom image list, you can find the custom image and view the boot mode of the custom image in the **Startup Mode** column.

#### Import custom Linux images

If you want to create and import custom Windows images, contact Alibaba Cloud technical support.

##### Import a Linux image

You can import an on-premises image file to Alibaba Cloud to generate a custom image and use the custom image to create Elastic Compute Service (ECS) instances or replace the operating systems (system disks) of existing ECS instances. This meets various business requirements and caters to different application scenarios. This topic describes how to import a Linux image.

**Procedure**

The following figure shows the procedure on how to import a Linux image.
1. Read Alibaba Cloud Marketplace Linux image requirements to understand the requirements
for importing Linux images.
2. Prepare a valid on-premises image file.
i. Install VirtualBox on the server from which you want to create an image and use VirtualBox to create a virtual machine and install an operating system. For more information, see Create a virtual machine and install an operating system. Elastic Compute Service ii. Install the following required plug-ins on the virtual machine. Install the NVMe driver. NVMe delivers faster response speed and higher bandwidth than traditional driver protocols, such as Small Computer System Interface (SCSI) and virtio-blk. For more information, see Install the NVMe driver. Install cloud-init to allow ECS instances that run the image to complete their initialization configurations. For more information, see Install cloud-init. Install the virtio driver to allow ECS instances created from the image to start as expected. For more information, see Install the virtio driver. iii. Install and use an image compliance tool to check whether the image meets the import requirements and repair issues in the image. For more information, see Check whether an image meets the import requirements. iv. Obtain the Linux image file. a. Obtain the Linux image file. For more information, see Obtain a Linux image file. b. Check whether the image file is in a format supported by ECS. ECS instances support only image files in RAW, Virtual Hard Disk (VHD), QEMU Copy-On-Write version 2 (QCOW2), and Virtual Machine Disk (VMDK) formats. If the image file that you want to import is in another format, you must convert the image file to a supported format first. For information about how to convert the format of an image file, see Convert the format of an image.
3. Upload the image file that you obtained to an Object Storage Service (OSS) bucket and
import the image file to ECS. For more information, see Import an image.
4. Create an ECS instance from the custom image that you imported.

##### Alibaba Cloud image specifications for

**Linux**

Before you import a custom Linux image to Alibaba Cloud, ensure that it meets the specifications described in this topic. The image must also pass compatibility tests for ECS instance types. Adhering to these specifications improves image availability and import efficiency, which helps you create ECS instances that meet your business needs.

**Disk partitions**

When you partition disks during image creation, ensure that you meet the following requirements. Disk expansion Use physical partitions for disk partitioning. The root partition must be the last partition. Otherwise, system disk expansion may fail. For systems that support online disk expansion, use the `growpart` command to expand the disk. You must install the `cloud-utils-growpart` package. Swap partition Do not create a swap partition in the image. LVM management Do not use Logical Volume Management (LVM) to manage disk partitions in the image. Disk mounting Configure the fstab and grub files using universally unique identifiers (UUIDs). Elastic Compute Service

**Important**

If the fstab file is not configured correctly, the ECS instance may not run properly after a restart. The minimum system disk capacity is 20 GiB. Set the image boot mode To ensure compatibility with instance types that use different boot modes, configure your local image for either BIOS or UEFI boot mode. When you import the image, set the boot mode to match the actual boot mode of the image. For more information about how to configure the boot mode when you create a local image, see Create a virtual machine and install an operating system. For more information about how to set the boot mode when you import an image, see Import an image. You can query the boot modes of an instance type by checking the value of the `SupportedBootModes` parameter in the response from the DescribeInstanceTypes operation.

**Note**

If your local image supports both BIOS and UEFI, you can set the boot mode to UEFI- Preferred. The image then automatically adapts to the boot modes of all instance types. This can also reduce the cost of image creation.

**Required software and tools**

Before you publish the image, ensure that the virtio driver is installed and added to the temporary file system. The virtio driver ensures that the image can run properly on Alibaba Cloud instances. Newer ECS instance families, such as ecs.g8i and ecs.g7se, attach disks using the NVMe protocol. This requires the image to have the NVMe driver installed. Otherwise, the instance fails to start. To ensure that your image is available when you create these types of ECS instances, install the NVMe driver on your local image. Install cloud-init when you create the image to ensure that ECS instances that run the image can be initialized correctly. Install cloud-init version 23.2.2. This version supports accessing metadata in enhanced mode to secure instance metadata access.

| Note To change passwords using cloud-init, the operating system kernel must support the CONFIG FW CFG SYSFS feature. This feature is supported by default in Linux community _ _ _ kernel versions 4.6 and later. For CentOS, it is supported by default in kernel versions 3.10.0-826.el7 and later. You can run the grep -nr CONFIG FW CFG SYSFS /boot/config- _ _ _ $(uname -r) command on the server for the image. If the output contains CONFIG FW CFG SYSFS=y , the kernel in the image supports the CONFIG FW CFG SYSFS _ _ _ _ _ _ feature. |  |  |
|---|---|---|
|  | grep -nr CONFIG FW CFG SYSFS /boot/config- _ _ _ |  |

Elastic Compute Service Install Cloud Assistant when you create the image. Cloud Assistant is a native automated O&M tool for ECS that lets you run commands in batches, such as Shell, PowerShell, and Bat commands, without requiring passwords, logons, or jump servers. You can perform tasks such as running automated O&M scripts, polling processes, installing or uninstalling software, starting or stopping services, and installing patches or security updates. Contact technical support to obtain Cloud Assistant. Secure the server During image creation, use Alibaba Cloud Server Guard to protect the server. Contact technical support to obtain Server Guard.

**System configuration**

**Time zone settings**

```
timedatectl set-timezone Asia/Shanghai ##Set the time zone to UTC+8 timedatectl set-local-rtc 0 ##Configure the RTC time zone
```

**Configure the SSHD service**

You can configure the SSHD service during image creation. The SSHD service provides remote logon and management for Linux systems. It uses the Secure Shell (SSH) protocol to encrypt communications. The following example shows how to modify the configuration in `/etc/ssh/sshd_config` :

```
UseDNS no AddressFamily inet SyslogFacility AUTHPRIV PermitRootLogin yes PasswordAuthentication yes
```

**Configure the Chrony service**

Chrony is a tool that synchronizes the computer clock. This ensures clock synchronization and prevents issues caused by time discrepancies. The following is an example command: Elastic Compute Service

```bash
chrony_file=/etc/chrony.conf cat >$chrony_file <<EOF
# Use Alibaba NTP server
# Public NTP
# Alibaba Cloud NTP
# server ntp.tbsite.com minpoll 4 maxpoll 10 iburst
server ntp1.tbsite.com minpoll 4 maxpoll 10 iburst server ntp2.tbsite.com minpoll 4 maxpoll 10 iburst
# Ignore stratum in source selection.
stratumweight 0.05
# Record the rate at which the system clock gains/losses time.
driftfile /var/lib/chrony/drift
# Enable kernel RTC synchronization.
rtcsync
# In the first three updates, step the system clock instead of slewing it
# if the adjustment is larger than 10 seconds.
makestep 10 3
# Allow NTP client access from the local network.
# allow 192.168/16
# Listen for commands only on localhost.
bindcmdaddress 127.0.0.1 bindcmdaddress ::1
# Disable logging of client accesses.
noclientlog
# Send a message to syslog if a clock adjustment is larger than 0.5 seconds.
logchange 0.5 logdir /var/log/chrony
# Log measurements, statistics, and tracking.
EOF
```

**Configure the MOTD service (Optional)**

We recommend configuring the Message of the Day (MOTD) service when you create an image. The MOTD service is a feature in Linux that displays a welcome message or system announcement after a user logs on to the system. The following is an example command:

```
echo -e "\nWelcome to Alibaba Cloud Elastic Compute Service ! \n" > /etc/motd
```

**Disable the Firewalld service**

Elastic Compute Service Firewalld is a service that manages firewall rules in Linux. You can disable the firewall because security groups provide security protection in the cloud. The following are example commands:

```bash
systemctl stop firewalld systemctl disable firewalld
```

**Disable SELinux**

Disable the **SELinux** service because it may prevent some applications or services from starting.

```
vi /etc/selinux/config SELINUX=disabled
```

**Configure DHCP for the network interface card**

1. Add the network interface card in the GRand Unified Bootloader (GRUB).
i. In the `/etc/default/grub` file, add the following information to the `GRUB_CMDLINE_LINUX_DEFAULT` line. x86_64 architecture

```
net.ifnames=0 console=tty0 console=ttyS0,115200n8 nvme_core.io_timeout=4294967295 nvme_core.admin_timeout=4294967295
```

Arm64 architecture

```
net.ifnames=0 console=tty0 console=ttyAMA0,115200n8 nvme_core.io_timeout=4294967295 nvme_core.admin_timeout=4294967295
```

Elastic Compute Service ii. In the `/boot/grub/grub.conf` file, add the following information to the kernel parameters.

```
net.ifnames=0 console=tty0 console=ttyS0,115200n8 nvme_core.io_timeout=4294967295 n vme_core.admin_timeout=4294967295
```

The following is an example of a successful addition:

```
cat /boot/grub/grub.conf
```

#

```bash
# Note that you do not have to rerun grub after making changes to this file
# NOTICE:  You have a /boot partition.  This means that
#          all kernel and initrd paths are relative to /boot/, eg.
#          root (hd0,0)
#          kernel /vmlinuz-version ro root=/dev/vda2
#          initrd /initrd-[generic-]version.img
#boot=/dev/vda
default=0 timeout=5 splashimage=(hd0,0)/grub/splash.xpm.gz hiddenmenu title Red Hat Enterprise Linux 6 (2.6.32-754.el6.x86_64)
        root (hd0,0)
                kernel /vmlinuz-2.6.32-754.el6.x86_64 ro root=UUID=37272173-6edd-48c
d-a912-0868012baffa rd_NO_LUKS rd_NO_LVM LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=auto KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rh gb quiet net.ifnames=0 console=tty0 console=ttyS0,115200n8 nvme_core.io_timeout=4294967295 nvme_core.admin_timeout=4294967295
        initrd /initramfs-2.6.32-754.el6.x86_64.img
```

2. Create and configure the network interface card configuration file.

**RHEL series**

i. Edit the network configuration file.

```
vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

ii. Modify the following network configuration items.

```
BOOTPROTO=dhcp DEVICE=eth0 ONBOOT=yes STARTMODE=auto TYPE=Ethernet USERCTL=no
```

**Debian series**

i. Edit the network configuration file.

```
/etc/network/interfaces
```

Elastic Compute Service ii. Modify the following network configuration items.

```
auto lo iface lo inet loopback auto eth0 iface eth0 inet dhcp
```

3. Apply the GRUB configuration.
x86_64 architecture Legacy

```
grub2-mkconfig -o /boot/grub2/grub.cfg
```

UEFI

```
grub2-mkconfig -o /boot/efi/EFI/xxxxxx/grub.cfg
```

Arm64 architecture

```
grub2-mkconfig -o /boot/efi/EFI/xxxxxx/grub.cfg
```

Older systems

```
grub-mkconfig -o /boot/grub/grub.conf
```

**Clear configuration traces (Optional)**

1. Clear traces and delete unnecessary files from the image.

```
rm -rf /root/.bash_history; rm -rf /root/.viminfo; echo > /etc/resolv.conf; echo > /v ar/log/wtmp; echo > /var/log/btmp; find /var/log -type f -exec truncate --size 0 {} \; ;history -c
```

2. Perform MD5 verification and generate an image signature to confirm file consistency.

```
md5sum kylin_v10_sp3_2303_arm64_20G_uefi_alibase_20250816.vhd 5aed82f462131e523e39ab5750d7a457 kylin_v10_sp3_2303_arm64_20G_uefi_alibase_20250816.vhd
```

**Add an image production identifier (Optional)**

Save the time and information of the current image customization.

```
cat /etc/image-id image_name="CentOS Linux release 7.9.2009 (Core)" image_id="centos_7_6_x86_64_20G_alibase_20211030.vhd" release_date="20211030164502" update="20250801"
```

##### Create a Linux image file

Elastic Compute Service

###### Create a virtual machine and install an

**operating system**

VirtualBox is a free open source cross-platform virtual machine software. You can create a Linux image file in the Virtual Hard Disk (VHD) format by using VirtualBox. This topic describes how to create a virtual machine by using VirtualBox and install a Linux operating system on the virtual machine.

**Prerequisites**

VirtualBox is installed. If VirtualBox is not installed, click here to download VirtualBox. An ISO image file is prepared. Network connectivity is good.

**Procedure**

The procedure to install an operating system on a virtual machine may vary based on the operating system. In this topic, VirtualBox 7.1.10 is used to create a virtual machine and the CentOS 7.9 operating system is installed. Perform the following steps:

**Step 1: Create a virtual machine**

1. Open the Oracle VirtualBox Manager. In the toolbar, go to **File > Tools > Global Tools (or**
**Preferences** depending on OS), select the **Expert** tab, and click **OK**.

**Note**

In VirtualBox 7.1.10, you must enable **Expert** mode to select specific disk file formats (like VHD) during creation. Otherwise, the wizard defaults to the VDl format.
2. Click **New** in the toolbar to launch the creation wizard.
3. Create a virtual machine.
i. Configure the **Name and Operating System** :
**Name**: Enter a descriptive name. Example: centosVM.
**Directory**: Choose the directory where the VM files will be stored.
**ISO Image**: Select the prepared ISO image file.
**Version**, **Type**: VirtualBox will automatically populate these fields based on the ISO
image file.
**Skip Unattended Installation**: Check this box. We recommend manual installation to
ensure custom partition configurations. ii. Configure **Hardware**.
**Base Memory**: Allocate RAM for the VM (e.g., 2048 MB).
**Processors**: Assign the number of virtual CPU cores.
**Enable EFl (special OSes Only)**: Check this only if you intend to use UEFl boot mode.
Leave unchecked for BlOS/Legacy boot. Elastic Compute Service iii. In the **Virtual Hard Disk** section, select **Create A Virtual Hard Disk Now** . Set the Disk Size and Storage Location. Select **Hard Disk File Type** .

**Note**

Only image files in the RAW, VHD, QCOW2, and VMDK formats can be imported to Elastic Compute Service (ECS). If you select a different format here, you must convert the created image to a supported format before you can import the image to ECS. For more information, see Convert the format of an image.
4. Click **Finish** to provision the virtual machine.

**Step 2: Install an operating system**

The boot mode is the mode in which the system disk is booted during ECS instance creation. Two boot modes are available: Basic Input Output System (BIOS) and Unified Extensible Firmware Interface (UEFI). You can use one of the boot modes to install a Linux operating system. After the operating system is installed, the system disk is booted in the boot mode. For more information about boot modes, see ECS instance boot modes.

**BlOS**

1. Select the new VM in the list and click **Start**.
2. The VM will boot from the lSO. Follow the on-screen installation wizard.
i. Select your language and click **Continue**. ii. On the **INSTALLATION SUMMARY** page, click **INSTALLATION DESTINATION**. iii. On the **INSTALLATION DESTINATION** page, select **Local Standard Disks** for **Device**
**Selection**, select **I Will Configure Partitioning** for **Partitioning**, and then click **Done**.
iv. On the **MANUAL PARTITIONING** page, click , set **Mount Point** to /, **Device Type** to
**Standard Partition**, and **File System** to **ext4**, and then click **Done**.
v. On the **INSTALLATION SUMMARY** page, click **NETWORK & HOST NAME**. vi. On the **NETWORK & HOST NAME** page, select **Ethernet**, click the **ON** button on the right side, and then click **Done**. vii. On the **INSTALLATION SUMMARY** page, click **Begin Installation**. viii. Once the installation completes, set a password for the root user, and then click **FINISH**
**CONFIGURATION**.
Remember this password. It is required to log in to the VM.
3. After the operating system is installed, restart the system.
4. Log in to the virtual machine and run the following command to make sure that the root
partition is mounted at last. If the root partition is not mounted at last, the instance cannot start or the disk cannot be resized.

```
lsblk
```

The following figure shows a sample command output. Elastic Compute Service

**UEFI**

1. Select the new VM in the list and click **Start**.
2. Follow the on-screen installation wizard.
i. Select your language and click **Continue**. ii. On the **INSTALLATION SUMMARY** page, click **INSTALLATION DESTINATION**. iii. On the **INSTALLATION DESTINATION** page, select **Local Standard Disks** for **Device**
**Selection**, select **I Will Configure Partitioning** for **Partitioning**, and then click **Done**.
iv. On the **MANUAL PARTITIONING** page, click , set **Mount Point**, **Device Type**, and
**File System**, and then click **Done**.
a. You must first mount the **/boot/efi** partition, select **Standard Partition** for **Device**
**Type**, and then select **EFI System Partition** for **File System**.
b. Mount the / root partition, select **Standard Partition** for **Device Type**, and then select **ext4** for **File System**.

**Important**

The system disk can have only the root partition. If the system disk has other partitions, the instance cannot start or the disk cannot be resized. Therefore, you must mount the root partition at last. v. On the **INSTALLATION SUMMARY** page, click **Begin Installation**. vi. Once the installation completes, set a password for the root user, and then click **FINISH**
**CONFIGURATION**.
Remember this password. It is required to log in to the VM.
3. After the operating system is installed, restart the system.
4. Log in to the virtual machine and run the following command to make sure that the root
partition is mounted at last. If the root partition is not mounted at last, the instance cannot start or the disk cannot be resized.

```
lsblk
```

The following figure shows a sample command output.

###### Install the NVMe driver

If you want to create a custom image on which no Non-Volatile Memory Express (NVMe) driver is installed to create an Elastic Compute Service (ECS) instance and use NVMe to improve storage performance, you can follow the steps described in this topic to install the NVMe driver on the custom image.

**Procedure**

1. Run the following command to check whether the kernel loaded the NVMe driver:
Elastic Compute Service

```
cat /boot/config-`uname -r` | grep -i nvme | grep -v "^#"
```

If the `CONFIG_BLK_DEV_NVME=y` message is returned, the operating system can start on an instance of an instance family that supports NVMe. If the `CONFIG_BLK_DEV_NVME=m` message is returned, perform the following steps in sequence.
2. Run the following command to check whether the initial Resource Access Management
(RAM) file system (initramfs) contains the NVMe driver:

```bash
sudo lsinitrd /boot/initramfs-`uname -r`.img | grep -i nvme | awk '{print $NF}' sudo lsinitramfs /boot/initrd.img-$(uname -r) | grep -i nvme | awk '{print $NF}'
```

If the command output shown in the preceding figure is returned, the operating system can start on an instance of an instance family that supports NVMe. In this case, proceed to Step 4. If the command output shown in the preceding figure is not returned, perform the following steps in sequence.
3. Run the following commands in sequence to configure the initramfs to support the NVMe
driver: x86_64

```bash
mkdir -p /etc/dracut.conf.d echo 'add_drivers+=" nvme nvme-core "' | sudo tee /etc/dracut.conf.d/nvme.conf > /d ev/null sudo dracut -v -f
```

arm64

```
mkdir -p /etc/dracut.conf.d echo 'add_drivers+=" nvme nvme-core nvme-fabrics nvme-fc nvme-rdma nvme-loop nvmet nvmet-fc "' >/etc/dracut.conf.d/nvme.conf dracut -v -f
```

|  |  | Note The io timeout parameter is added to the GRUB file to fix timeout errors related to _ the NVMe devices in the Linux operating system. If you set the io timeout parameter to _ the maximum value, the operating system can continue to process I/O requests from NVMe devices, regardless of whether a timeout occurs. In most Linux distributions, the io timeout parameter defaults to 30. Unit: seconds. _ Before setting the io timeout parameter to a specific value, you need to run the _ echo 4294967295 > /sys/module/nvme core/parameters/io timeout or echo 4294967295 _ _ > /sys/module/nvme/parameters/io timeout command to check whether the _ io timeout parameter can be set to the maximum value of 4,294,967,295. If -bash: _ echo: write error: Invalid argument is returned, it indicates that the current Linux version only supports a value of 255. |  |
|---|---|---|---|
|  |  |  | echo 4294967295 > /sys/module/nvme core/parameters/io timeout _ _ |
|  |  | > /sys/module/nvme/parameters/io timeout _ |  |
|  |  |  | io timeout _ |
|  |  | echo: write error: Invalid argument |  |

|  | io timeout _ |
|---|---|
| io timeout _ |  |

Elastic Compute Service

**Note**

If the dracut tool is not installed in your operating system, run the **sudo yum -y**
**install dracut** command to install the dracut tool first.
4. Add the NVMe-related `io_timeout` parameter to the GRand Unified Bootloader (GRUB)
file. i. Run the following command to open the GRUB file:

```bash
sudo vi /etc/default/grub
```

ii. Press the I key to enter Insert mode. At the end of the `GRUB_CMDLINE_LINUX=` line, add the `nvme_core.io_timeout` and nvme_core.admin_timeout parameters and set them both to 4294967295. The following figure shows an example on how to add the parameters.

**Note**

If the GRUB file already contains the preceding parameter settings, you do not need to add the parameters again. iii. Press the `Esc` key to exit Insert mode. Then, enter `:wq` and press the `Enter` key to save and close the file. Elastic Compute Service iv. Apply the GRUB configurations. Run one of the following commands based on the boot mode of the ECS instance: Legacy BIOS boot mode

```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Unified Extensible Firmware Interface (UEFI) boot mode a. Run the following command to view the GRUB configuration file:

```
cat /boot/efi/EFI/centos/grub.cfg
```

b. Run the one of the following commands based on the command output of the grub configuration file. If a different path is specified for configfile, such as `/boot/grub/grub.cfg` shown in the following figure, run the following command to make the configuration take effect:

```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

If no different path is specified for configfile, run the following command to make the configuration take effect:

```bash
sudo grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg
```

5. Run the following command again to check NVMe-related information:

```bash
sudo lsinitrd /boot/initramfs-`uname -r`.img | grep -i nvme | awk '{print $NF}'
```

If the following command output is returned, the configuration is complete and the operating system can start on an instance of an instance family that supports NVMe.

###### Install cloud-init

Cloud-init is an open source initialization tool that automates initialization operations for Linux operating systems, such as generating an initial password, configuring the hostname, and running user data scripts. If you want to migrate an on-premises custom image on which cloud-init is not installed to Alibaba Cloud, you can manually install cloud-init. If you do not install cloud-init, Elastic Compute Service (ECS) instances created from the custom image cannot automatically perform initialization tasks such as configuring the hostname and network settings. This may affect the efficiency of automated deployment and configuration of the ECS instances. This topic describes how to install cloud-init in Linux operating systems. For more information about cloud-init, see Cloud-init documentation.

**Scenarios**

Elastic Compute Service By default, cloud-init is installed on all Alibaba Cloud public images. To ensure that ECS instances created from on-premises custom images can automatically initialize system configurations, we recommend that you consider the following suggestions and perform relevant operations based on your use scenarios: Cloud-init is not installed on the Linux servers that you want to migrate to Alibaba Cloud. Before you migrate a Linux server on which cloud-init is not installed to Alibaba Cloud, install cloud-init on the server. This way, ECS instances that are created based on the Linux server can be automatically initialized during system boot.

**Note**

If you do not want to migrate a Linux server to Alibaba Cloud, installing cloud-init on the server may cause unnecessary complexity or resource usage. Determine whether to install cloud-init based on your actual environment. Cloud-init 0.7.9 or earlier is installed on Linux servers. In most cases, more recent cloud-init versions include more features and fixes to ensure compatibility with the latest cloud platform features. If cloud-init of an outdated version is installed on your Linux server, we recommend that you upgrade cloud-init to a version later than 0.7.9 to maximize compatibility and security. Cloud-init is not installed on ECS instances. If cloud-init is not installed on an ECS instance, we recommend that you install cloud-init on the instance to ensure that the instance can be automatically initialized.

**Step 1: Check whether cloud-init needs to be installed or**

**upgraded**

1. Log on to the source server.
2. Run the following command to check whether cloud-init is installed:

**CentOS series**

```
rpm -qa | grep -i cloud-init pip list | grep -i cloud-init
```

**Ubuntu series**

```
dpkg -l | grep -i cloud-init pip list | grep -i cloud-init
```

**If no output is found or the cloud-init version is earlier than 0.7.9**, you need to
install or upgrade cloud-init.

**Important**

cloud-init 0.7.9 is an initial version of the native cloud-init, which is not suitable for ECS instances and must be upgraded.
**If the cloud-init version is 18 or later** , you do not need to install cloud-init, and it can
automatically configure the network during instance initialization. If the default configuration does not meet your requirements, you can disable the network initialization feature.

| Operating system type | Operating system version | Binary package | MD5 checksum |
|---|---|---|---|
| Debian | 12 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/de bian12/cloud-init 23.2.2-1 all.deb _ _ | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/debian12/cloud- init 23.2.2- _ 1 all.deb.md5sum _ |
| CentOS Stream | 9 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/ce ntosstream9/cloud-init-23.2.2- 2.el9.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/centosstream9/cloud- init-23.2.2- 2.el9.noarch.rpm.md5sum |
|  | 8 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/ce ntosstream8/cloud-init-23.2.2- 2.el8.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/centosstream8/cloud- init-23.2.2- 2.el8.noarch.rpm.md5sum |

Elastic Compute Service
**If cloud-init 19.1.21 is used**, we recommend that you upgrade to Alibaba Cloud cloud-
init 23.2.2. Compared with Alibaba Cloud cloud-init 19.1.21, Alibaba Cloud cloud-init 23.2.2 provides the following improvements and new features: Cloud-init 23.2.2 allows you to access instance metadata in security hardening mode. Other feature enhancements, performance improvements, error fixes, and community contributions. For more information, see ChangeLog.
**Others**: You do not need to install cloud-init.
3. To prevent data loss caused by misoperations during cloud-init installation, we recommend
that you back up the data of the source server in advance. For example, you can create snapshots to back up the data of the source server. Alibaba Cloud cloud-init is optimized for and can provide better support for Alibaba Cloud services. To ensure compatibility, we recommend that you use Alibaba Cloud cloud-init. Select a cloud-init version to install based on your business requirements.

**(Recommended) Install Alibaba Cloud cloud-init 23.2.2**

The most recent version of Alibaba Cloud cloud-init is 23.2.2. Alibaba Cloud cloud-init 23.2.2 is maintained as a package. You can download a package that is suitable for your operating system version to install Alibaba Cloud cloud-init 23.2.2. The following table lists download links of Alibaba Cloud cloud-init 23.2.2 packages for different operating systems.

| Fedora | 39 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/fe dora39/cloud-init-23.2.2- 2.fc39.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/fedora39/cloud-init- 23.2.2- 2.fc39.noarch.rpm.md5sum |
|---|---|---|---|
|  | 38 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/fe dora38/cloud-init-23.2.2- 1.fc38.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/fedora38/cloud-init- 23.2.2- 1.fc38.noarch.rpm.md5sum |
| AlmaLinux | 9 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/al malinux9/cloud-init-23.2.2- 2.el9.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/almalinux9/cloud-init- 23.2.2- 2.el9.noarch.rpm.md5sum |
|  | 8 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/al malinux8/cloud-init-23.2.2- 2.el8.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/almalinux8/cloud-init- 23.2.2- 2.el8.noarch.rpm.md5sum |
| Rocky Linux | 9 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/ro ckylinux9/cloud-init-23.2.2- 2.el9.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/rockylinux9/cloud-init- 23.2.2- 2.el9.noarch.rpm.md5sum |
|  | 8 | https://ecs-image-tools.oss-cn- hangzhou.aliyuncs.com/cloudinit/ro ckylinux8/cloud-init-23.2.2- 2.el8.noarch.rpm | https://ecs-image-tools.oss- cn- hangzhou.aliyuncs.com/clou dinit/rockylinux8/cloud-init- 23.2.2- 2.el8.noarch.rpm.md5sum |

Elastic Compute Service The following sections describe how to download the binary packages of cloud-init and install cloud-init on Debian 12 and CentOS Stream 9.

**Debian 12**

1. Run the following command to download the Alibaba Cloud cloud-init package:

```
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/debian12/cloud-in it_23.2.2-1_all.deb
```

2. Run the following command to install the Alibaba Cloud cloud-init package:

```bash
sudo apt-get install -y ./cloud-init_23.2.2-1_all.deb
```

Elastic Compute Service
3. (Optional) To prevent the Alibaba Cloud cloud-init package from being automatically
updated or upgraded to a more recent open source version, we recommend that you run the following command to hold the package at the current version:

```bash
sudo apt-mark hold cloud-init
```

4. Run the following command to check whether the cloud-init version is as expected:

```
cloud-init --version
```

**CentOS Stream 9**

1. Run the following command to download the Alibaba Cloud cloud-init package:

```
wget https://ecs-image-tools.oss-cnhangzhou.aliyuncs.com/cloudinit/centosstream9/cloud-init-23.2.2-2.el9.noarch.rpm
```

2. Run the following command to install the Alibaba Cloud cloud-init package:

```bash
sudo yum install -y ./cloud-init-23.2.2-2.el9.noarch.rpm
```

3. (Optional) To prevent the Alibaba Cloud cloud-init package from being automatically
updated or upgraded to a more recent open source version, we recommend that you run the following command to hold the package at the current version:

```bash
sudo sh -c 'echo "exclude=cloud-init" >> /etc/dnf/dnf.conf'
```

4. Run the following command to check whether the cloud-init version is as expected:

```
cloud-init --version
```

**Install Alibaba Cloud cloud-init 19.1.21**

1. Make sure that the python-pip dependency library is installed on the source server.
In the examples, the python3-pip dependency library is used. Run one of the following commands to install the python-pip dependency library based on the operating system of the source server.

**CentOS/Red Hat Enterprise Linux**

```bash
sudo yum -y install python3-pip
```

**Ubuntu/Debian**

```bash
sudo apt-get -y install python3-pip
```

**OpenSUSE/SUSE**

```bash
sudo zypper -n install python3-pip
```

2. Run the following command to download the Alibaba Cloud cloud-init installation package:

```
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.2 1.tgz
```

3. Run the following command to decompress the Alibaba Cloud cloud-init installation package
to the current directory:

| Parameter | Description | Example value |
|---|---|---|
| <issue> | The type of the operating system. Valid values: centos, redhat, rhel, debian, ubuntu, opensuse, and sles. The value of this parameter is case-sensitive. sles specifies SUSE or SLES. Note If the operating system is CentOS Stream, set this parameter to centos. | centos |
| <majorversi _ on> | The major version number of the operating system. Note You cannot install Alibaba Cloud cloud-init 19.1.21 on Ubuntu 14. | The major version number of CentOS 7.6 is 7. |

Elastic Compute Service

```
tar -zxvf cloud-init-19.1.21.tgz
```

4. Run the following commands to go to the cloud-init directory and install the dependency
library:

```
cd ./cloud-init-19.1.21 pip3 install -r ./requirements.txt
```

5. Run the following command to go to the tools subdirectory of the cloud-init directory:

```
cd ./tools
```

6. Run the following command to execute the deploy.sh script to install Alibaba Cloud cloud-
init:

```bash
sudo bash ./deploy.sh <issue> <major_version>
```

The following table describes the parameters and the corresponding values in the deploy.sh script. For example, if the current operating system is CentOS 7, run the `sudo bash ./deploy.sh` `centos 7` command.
7. Check whether Alibaba Cloud cloud-init is installed.
If Alibaba Cloud cloud-init is installed, `"description": "success"` is returned.
8. Run the following command to check whether the cloud-init version is as expected:
Elastic Compute Service

```
cloud-init --version
```

The following section provides sample shell scripts that you can use to install Alibaba Cloud cloud-init on different Linux distributions. Modify the shell script based on the operating system.

**CentOS 7/8**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  yum -y install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.21. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/redhat-release | grep -Eo '[0-9]+\.?[0-9]+' | head -1 | awk -F' .' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh centos "$issue_major"
```

**Red Hat Enterprise Linux 7/8**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  yum -y install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.21. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh rhel "$issue_major"
```

**Ubuntu 16/18/20**

Elastic Compute Service

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  apt-get install python36 python3-pip -y
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.21. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh ubuntu "$issue_major"
```

**Debian 9/10**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  apt-get -y install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.21. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh debian "$issue_major"
```

**SUSE 12/15**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools'>& /dev/null; then
  zypper -n install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud/etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.21. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh sles "$issue_major"
```

**OpenSUSE 15**

Elastic Compute Service

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools'>& /dev/null; then
  zypper -n install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud/etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.21. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh opensuse"$issue_major"
```

**Install Alibaba Cloud cloud-init 19.1.23**

1. Make sure that the python-pip dependency library is installed on the source server.
In the examples, the python3-pip dependency library is used. Run one of the following commands to install the python-pip dependency library based on the operating system of the source server.

**CentOS/Red Hat Enterprise Linux**

```bash
sudo yum -y install python3-pip
```

**Ubuntu/Debian**

```bash
sudo apt-get -y install python3-pip
```

**OpenSUSE/SUSE**

```bash
sudo zypper -n install python3-pip
```

2. Run the following command to download the Alibaba Cloud cloud-init installation package:

```
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.2 3.tgz
```

3. Run the following command to decompress the Alibaba Cloud cloud-init installation package
to the current directory:

```
tar -zxvf cloud-init-19.1.23.tgz
```

4. Run the following commands to go to the cloud-init directory and install the dependency
library:

```
cd ./cloud-init-19.1.23 pip3 install -r ./requirements.txt
```

5. Run the following command to go to the tools subdirectory of the cloud-init directory:

```
cd ./tools
```

| Parameter | Description | Example value |
|---|---|---|
| <issue> | The type of the operating system. Valid values: centos, redhat, rhel, debian, ubuntu, opensuse, and sles. The value of this parameter is case-sensitive. sles specifies SUSE or SLES. Note If the operating system is CentOS Stream, set this parameter to centos. | centos |
| <majorversi _ on> | The major version number of the operating system. Note You cannot install Alibaba Cloud cloud-init 19.1.23 on Ubuntu 14. | The major version number of CentOS 7.6 is 7. |

Elastic Compute Service
6. Run the following command to execute the deploy.sh script to install Alibaba Cloud cloud-
init:

```bash
sudo bash ./deploy.sh <issue> <major_version>
```

The following table describes the parameters and the corresponding values in the deploy.sh script. For example, if the current operating system is CentOS 7, run the `sudo bash ./deploy.sh` `centos 7` command.
7. Check whether Alibaba Cloud cloud-init is installed.
If Alibaba Cloud cloud-init is installed, `"description": "success"` is returned.
8. Run the following command to check whether the cloud-init version is as expected:

```
cloud-init --version
```

The following section provides sample shell scripts that you can use to install Alibaba Cloud cloud-init on different Linux distributions. Modify the shell script based on the operating system.

**CentOS 7/8**

Elastic Compute Service

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  yum -y install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.23. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/redhat-release | grep -Eo '[0-9]+\.?[0-9]+' | head -1 | awk -F' .' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh centos "$issue_major"
```

**Red Hat Enterprise Linux 7/8**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  yum -y install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.23. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh rhel "$issue_major"
```

**Ubuntu 16/18/20**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  apt-get install python36 python3-pip -y
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.23. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh ubuntu "$issue_major"
```

**Debian 9/10**

Elastic Compute Service

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools' >& /dev/null; then
  apt-get -y install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud /etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.23. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh debian "$issue_major"
```

**SUSE 12/15**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools'>& /dev/null; then
  zypper -n install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud/etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.23. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh sles "$issue_major"
```

**OpenSUSE 15**

```bash
# Check whether the python3-pip dependency library is installed. If not, install it.
if ! python3 -c 'import setuptools'>& /dev/null; then
  zypper -n install python3-pip
```

`fi`

```bash
# Back up cloud-init of an earlier version.
test -d /etc/cloud && mv /etc/cloud/etc/cloud-old
# Download and decompress the Alibaba Cloud cloud-init installation package.
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloudinit/cloud-init-19.1.23. tgz tar -zxvf ./cloud-init-19.1.21.tgz
# Install Alibaba Cloud cloud-init.
issue_major=$( cat /etc/os-release | grep VERSION_ID | grep -Eo '[0-9]+\.?[0-9]+' | hea d -1 | awk -F'.' '{printf $1}') bash ./cloud-init-*/tools/deploy.sh opensuse"$issue_major"
```

**(Outdated version, not recommended) Install Alibaba Cloud**

**cloud-init 0.7.6a17**

| Parameter | Description | Example value |
|---|---|---|
| <issue> | The type of the operating system. Valid values: centos, debian, and sles. The value of this parameter is case-sensitive. sles specifies SUSE or SLES. | centos |

Elastic Compute Service

**Note**

By default, `Alibaba Cloud cloud-init 0.7.6a15` is installed on Alibaba Cloud public images for CentOS 6, Debian 9, and SUSE Linux Enterprise Server 12 (SLES 12). If you want to test Alibaba Cloud cloud-init 0.7.6a17, run the `sudo mv /etc/cloud/cloud.cfg` `/etc/cloud/cloud.cfg_bak` command to back up the configuration file first.
1. Run the following command to check whether the operating system version is CentOS 6,
Debian 9, or SLES 12:

```
cat /etc/issue
```

2. Make sure that the python-pip dependency library is installed on the source server.
In this example, the python2-pip dependency library is used. Run the following command to install the python2-pip dependency library:

**CentOS 6/SUSE Linux Enterprise Server 12**

```bash
sudo yum -y install python2-pip
```

**Debian 9**

```bash
sudo apt-get -y install python2-pip
```

3. Run the following commands to download and decompress the Alibaba Cloud cloud-init
0.7.6a15 installation package:

```
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/cloud-init-0.7.6a15.tgz tar -zxvf cloud-init-0.7.6a15.tgz
```

4. Run the following command to go to the tools subdirectory of the cloud-init directory:

```
cd cloud-init-0.7.6a15/tools/
```

5. Run the following command to execute the deploy.sh script to install Alibaba Cloud cloud-
init:

```bash
sudo bash ./deploy.sh <issue> <major_version>
```

For example, if the current operating system is CentOS 6, run the `sudo bash ./deploy.sh` `centos 6` command to install Alibaba Cloud cloud-init. The following table describes the parameters and the corresponding values in the deploy.sh script.

| <majorversi _ on> | The major version number of the operating system. | The major version number of CentOS 6.5 is 6. |
|---|---|---|

Elastic Compute Service
6. Run the following command to check whether the cloud-init version is as expected:

```
cloud-init --version
```

**Install native cloud-init**

1. Make sure that the Git, Python, and python-pip dependency libraries are installed on the
source server. In the examples, Git, Python 3.6, and python3-pip are used. Run the following commands to install Git, Python, and python-pip dependency libraries for specific Linux distributions.

**CentOS/Red Hat Enterprise Linux**

```bash
sudo yum -y install git python36 python3-pip
```

**Ubuntu/Debian**

```bash
sudo apt-get -y install git python36 python3-pip
```

**OpenSUSE/SUSE**

```bash
sudo zypper -n install git python36 python3-pip
```

2. Run the following command to download the cloud-init source code repository from Git:

```
git clone https://git.launchpad.net/cloud-init
```

3. Run the following command to go to the cloud-init directory:

```
cd ./cloud-init
```

4. Run the following command to install all required dependency libraries:

```bash
sudo pip3 install -r ./requirements.txt
```

5. Run the following command to install cloud-init:

```
python3 setup.py install
```

6. Modify the cloud.cfg configuration file.
Elastic Compute Service i. Open the cloud.cfg configuration file.

```bash
sudo vi /etc/cloud/cloud.cfg
```

ii. Replace the content that precedes `cloud_init_modules:` with the following content:

```bash
# Example datasource config
# The top level settings are used as module
# and system configuration.
# A set of users which may be applied and/or used by various modules
# when a 'default' entry is found it will reference the 'default_user'
# from the distro configuration specified below
users:
   - default
user:
    name: root
    lock_passwd: False
# If this is set, 'root' will not be able to ssh in and they
# will get a message to login instead as the above $user
disable_root: false
# This will cause the set+update hostname module to not operate (if true)
preserve_hostname: false syslog_fix_perms: root:root datasource_list: [ AliYun ]
# Example datasource config
datasource:
    AliYun:
        support_xen: false
        timeout: 5 # (defaults to 50 seconds)        max_wait: 60 # (defaults to
120 seconds)
#      metadata_urls: [ 'blah.com' ]
# The modules that run in the 'init' stage
cloud_init_modules:
```

7. Run the following command to check whether the cloud-init version is as expected:

```
cloud-init --version
```

Elastic Compute Service

###### Install the virtio driver

The virtio driver is a high-performance I/O driver that is used for virtualization devices. The virtio driver is a required component of images that are released in Alibaba Cloud. Before you create a Linux image, make sure that the virtio driver is installed in the Linux operating system and added to a temporary file system. Otherwise, Elastic Compute Service (ECS) instances may fail to recognize virtio virtualization devices and the operating system may fail to start. This topic describes how to install the virtio driver on a Linux virtual machine based on which you want to create an image.

**Process**

The following figure shows the process of installing the virtio driver in a Linux operating system. Check whether the operating system kernel supports the

**The values of the**

**CONFIG_VIRTIO_BLK and**

**The values of the**

**CONFIG_VIRTIO_BLK and**

**CONFIG_VIRTIO_NET**

**CONFIG_VIRTIO_NET**

**parameters are m,**

**parameters are y**

**or one is y and**

**the other is m**

Check whether the virtio driver is added to a temporary file system

**Yes**

**No**

Add the virtio to a temporary file system End

**Procedure**

**Check whether the operating system kernel supports the virtio**

1. Run the following command on a Linux virtual machine, based on which you want to create
an image, to check whether the system kernel of your source server supports the virtio driver, and determine whether to install the virtio driver for the custom image or whether to add the driver to a temporary file system.

```
grep -i virtio /boot/config-$(uname -r)
```

Sample command output: Elastic Compute Service
2. Analyze the check result.
Make determinations and perform operations based on the values of the `CONFIG_VIRTIO_BLK` and `CONFIG_VIRTIO_NET` parameters that are contained in the command output. CONFIG_VIRTIO_BLK represents the block device driver of virtio, while CONFIG_VIRTIO_NET represents the network device driver of virtio.
**Both parameter values are**y: The virtio driver has been correctly installed in the
operating system and has been compiled into the system kernel. In this case, the virtio driver is automatically loaded after system startup, and you do not need to install the virtio driver.

**Both parameter values are m, or one parameter value is y and the other**

**parameter value is m**: The virtio driver exists as a kernel module. You only need to add
the virtio driver to a temporary file system. For more information, see the Add the virtio driver to a temporary file system section of this topic.

**Add the virtio driver to a temporary file system**

If `CONFIG_VIRTIO_BLK=m` or `CONFIG_VIRTIO_NET=m` is enabled for the system kernel but the specific module is not added to a temporary file system, the virtio driver may fail to be loaded when the system starts. This causes a failure to recognize the virtual machine. The temporary file system is the initial Resource Access Management (RAM) file system (initramfs).
1. If the values of the `CONFIG_VIRTIO_BLK` and `CONFIG_VIRTIO_NET` **parameters are m or if**
**one parameter value is y and the other parameter value is m**, run one of the
following commands based on your specific operating system to check whether the virtio driver is added to the temporary file system.

**CentOS series**

```
lsinitrd /boot/initramfs-$(uname -r).img | grep virtio
```

**Debian**

```
lsinitramfs /boot/initrd.img-$(uname -r)|grep virtio
```

| ontain | virtio blk.ko _ |  |
|---|---|---|
| virtio net.ko _ |  |  |
|  |  | , you n |

|  | CONFIG VIRTIO NET _ _ |
|---|---|
| add drivers+="virtio net" _ _ |  |

Elastic Compute Service

**SUSE**

```
lsinitrd /boot/initrd-$(uname -r)|grep virtio
```

As shown in the preceding figure, the command output contains both `virtio_blk.ko` and `virtio_net.ko` . This indicates that the virtio driver has been added to the temporary file system, and the virtio driver addition operation is not needed.
2. Add the virtio driver to the temporary file system.

**CentOS series**

If the operating system version is CentOS 6, Anolis OS 7, AlmaLinux 8, Fedora 33, or later and the kernel version is later than 2.6.24, run the following commands to add the virtio driver to the temporary file system. You can run the `uname -r` command to check the kernel version. i. Run the following command to open the dracut.conf file:

```
vim /etc/dracut.conf
```

ii. Press the I key to enter the Insert mode and add the following content to the file:

```
add_drivers+="virtio_blk virtio_net"
```

Press the `Esc` key, enter `:wq`, and then press the Enter key to save and close the file.

**Note**

If one of the values of the `CONFIG_VIRTIO_BLK` and `CONFIG_VIRTIO_NET` parameters Elastic Compute Service iii. Run the following command to regenerate initrd:

```
dracut -f
```

**Note**

After the command is run, you can run the echo $? command to check whether a value of 0 is returned. If the value of 0 is returned, initrd is regenerated as expected. You can also run the

```
 lsinitrd /boot/initramfs-$(uname -r).img | grep virtio
```

command to check whether the virtio driver is added to the temporary file system as expected.

**Debian**

i. Run the following command to open the modules file:

```
vim /etc/initramfs-tools/modules
```

ii. Press the I key to enter the Insert mode and add the following content to the file:

```
virtio_blk virtio_net
```

Press the `Esc` key, enter `:wq`, and then press the Enter key to save and close the file.

**Note**

If one of the values of the `CONFIG_VIRTIO_BLK` and `CONFIG_VIRTIO_NET` parameters is y and the other is m, you need to only add the virtio driver whose value is m to the file. For example, if the value of the `CONFIG_VIRTIO_NET` parameter is m, you only need to add `virtio_net` to the file. iii. Run the following command to regenerate initrd:

```
update-initramfs -u
```

**Note**

After the command is run, you can run the echo $? command to check whether a value of 0 is returned. If the value of 0 is returned, initrd is regenerated as expected. You can also run the

```
 lsinitramfs /boot/initrd.img-$(uname -r)|grep virtio
```

command to check whether the virtio driver is added to the temporary file system as expected.

**SUSE**

Versions earlier than SUSE 12 SP1 or openSUSE 13 a. Run the following command to open the kernel file:

```
vim /etc/sysconfig/kernel
```

|  | CONFIG VIRTIO NET _ _ |
|---|---|
| INITRD MODULES="virtio net" _ _ |  |

Elastic Compute Service b. Press the I key to enter the Insert mode and add the following content to the file:

```
INITRD_MODULES="virtio_blk virtio_net"
```

Press the `Esc` key, enter `:wq`, and then press the Enter key to save and close the file.

**Note**

If one of the values of the `CONFIG_VIRTIO_BLK` and `CONFIG_VIRTIO_NET` c. Run the following command to regenerate initrd:

```
mkinitrd
```

SUSE 12 SP1, openSUSE 13, or later a. Run the following command to open the dracut.conf file:

```
vim /etc/dracut.conf
```

b. Press the I key to enter the Insert mode and add the following content to the file:

```
add_drivers+="virtio_blk virtio_net"
```

Press the `Esc` key, enter `:wq`, and then press the Enter key to save and close the file.

**Note**

c. Run the following command to regenerate initrd:

```
dracut -f
```

**Note**

After the command is run, you can run the echo $? command to check whether a value of 0 is returned. If the value of 0 is returned, initrd is regenerated as expected. You can also run the

```
 lsinitrd /boot/initrd-$(uname -r)| grep virtio
```

command to check whether the virtio driver is added to the temporary file system as expected.

###### Check whether an image meets the

**import requirements**

You can use the image compliance tool to check whether the operating system settings of an image meet the import requirements. For example, check whether the image can be used to create full-featured Elastic Compute Service (ECS) instances. This topic describes how to check whether an image meets the import requirements. In the examples, an image that contains a CentOS 7.9 64-bit operating system is used. Elastic Compute Service

**Procedure**

1. Log in to the source server, virtual machine (VM), or cloud host based on which you want to
create an image file.
2. Run the following commands in sequence to download and decompress the image
compliance tool:

```
wget https://ecs-image-tools.oss-cn-hangzhou.aliyuncs.com/imagecheck/ecsgo-helper.tar .gz tar -xf ecsgo-helper.tar.gz
```

You can download the image compliance tool by using your browser.
3. Run the following command to run the image compliance tool:

```bash
sudo ./ecsgo-helper.sh image-online-diagnostic
```

Wait for the image compliance tool to check the system configurations. The following code provides an example of the check result. Elastic Compute Service

```
------------------------------------------------------------
            OS: CentOS 7.9.2009   Kernel: 3.10.0-1160.76.1.el7.x86_64
            Arch: x86_64       RTC-Mode: utc       Boot-Mode: Legacy
------------------------------------------------------------ Image Check Result
```

`K]`

```
Nvme
```

`K]`

```
Fstab
```

`K]`

```
Grub
```

`K]`

```
Dhcp
```

`K]`

```
Selinux
```

`K]`

```
OnlineResizeFS OK] OK] [OK] SecurityCenterAgent OK] SupportMocInstanceTypes OK] DiskUsage [OK] InodeUsage [OK] SystemFileAttribute OK] CriticalUser OK] QemuGuestAgent OK] SshConfig [OK] Firewall
```

`K]`

```
LibDirectory OK]
         Total case Count                19
            Successes:                   19
            Failures:                    0
            Warnings:                    0
------------------------------------------------------------
```

| Check item (Case Name) | Rectified item | Impact | Description |
|---|---|---|---|
| Virtio | virtio | An ECS instance startup exception occurs. | Check whether the virtio driver is installed in the image. ECS instances are VMs that are built based on the Kernel-based Virtual Machine (KVM) architecture, and require that the virtio driver be installed in the image. |
| Nvme | nvme | Instance types that use Non- Volatile Memory Express (NVMe) disks, such as ecs.g7se, cannot be used. | Check whether the NVMe driver is installed in the image. Specific ECS instance types use NVMe disks and require that the NVMe driver be installed in the image. NVMe delivers faster response speed and higher bandwidth than traditional driver protocols, such as Small Computer System Interface (SCSI) and virtio-blk. We recommend that you install the NVMe driver in the image to support specific instance types. |
| Fstab | fstab | An operating system startup exception occurs. | Check configurations in the /etc/fstab file. Incorrect configurations in the /etc/fstab file, such as configurations of nonexistent devices and incorrect universally unique identifiers (UUIDs), cause system startup exceptions. |
| Grub | grub | An operating system startup exception occurs. | Check the GRand Unified Bootloader (GRUB) configuration file. Configuration errors, such as specifying a boot partition with a device name instead of a UUID, can cause the operating system to be unable to start. |

Elastic Compute Service

**Check items**

The image compliance tool provides a check result of `OK` , `FAILED` , or `WARNING` based on the levels of check items. `OK` : All check items comply with the requirements. `FAILED` : Check items do not comply with the requirements, and the ECS instances that are created from the image cannot start as expected or may encounter network exceptions. We recommend that you rectify the non-compliant items before you import the image. `WARNING` : The check items do not comply with the requirements, and the ECS instances that are created from the image are not protected by Security Center and cannot be automatically operated or maintained by using Cloud Assistant. To improve cloud O&M efficiency, we recommend that you rectify the non-compliant items before you import the image. The image compliance tool checks the configuration items of source servers. The following table describes the check items of the image compliance tool.

|  | Dhcp |  |  | dhcp |  | A network error occurs. | Check whether Dynamic Host Configuration Protocol (DHCP) is configured in the network configuration file of the image. We recommend that you configure DHCP for network devices to assign dynamic IP addresses to instances. If a static IP address is configured in the image, network configuration exceptions may occur and the instances that use the image cannot start. We also recommend that you add the net.ifnames parameter as a kernel startup parameter in the GRUB configuration file and set the parameter to 0 to prevent network interfaces from being renamed in the kernel. This way, the network interface controller (NIC) remains named eth0. |
|---|---|---|---|---|---|---|---|
|  | Selinux |  |  | selinux |  | The ECS instance cannot start as expected. | Check whether Security-enhanced Linux (SELinux) is disabled in the image. We recommend that you disable SELinux. |
|  | Cloudinit |  |  | cloudinit |  | Specific system initialization configuration s are missing. | Check whether cloud-init is installed in the image. cloud-init initializes system configurations on instance startup and executes user data scripts. The system configurations include the Network Time Protocol (NTP) settings, software repositories, hostnames, and SSH key pairs. |
|  |  | Cloudinit |  |  | cloudinit |  |  |
|  | SshConfig |  |  | sshd |  | An SSH connection to an ECS instance that uses the image cannot be established. | Check whether the sshd configuration file contains errors. In most cases, the sshd configuration file is /etc/ssh/sshd config. _ If the sshd configuration file contains errors, the sshd service cannot start, and SSH connections to ECS instances that use the image cannot be established. You must check the correctness and validity of the sshd configuration file. You can run the following commands: Run the sudo sshd -T command to view all sshd configuration options. Run the sudo sshd -t command to verify the validity of the sshd configuration file. If the sshd configuration file is valid, no information is returned. |
|  |  | SshConfig |  |  |  |  |  |
|  | Firewall |  |  | firewall |  | The system firewall service may cause an instance access failure. | Check whether the firewall service is enabled. We recommend that you disable the firewall service in the operating system and use ECS security groups to manage inbound and outbound traffic of instances. |

Elastic Compute Service

|  | CloudAssis tant |  |  |  | assist |  |  | Cloud-based O&M efficiency is adversely affected. | Check whether the Cloud Assistant agent is installed in the image. Cloud Assistant is a native automated O&M tool that is developed for ECS. We recommend that you install the Cloud Assistant agent in the image for efficient O&M of ECS. |
|---|---|---|---|---|---|---|---|---|---|
|  |  | CloudAssis |  |  |  | a | ssist |  |  |
|  | tant |  |  |  |  |  |  |  |  |
|  | SecurityCe nterAgent |  |  |  | aegis |  |  | Vulnerabilitie s in an instance that uses the image cannot be identified, and the instance runs without Server Guard protection. | Check whether the Server Guard agent is installed. After the Server Guard agent is installed, the server can be protected by Server Guard. |
|  |  | SecurityCe |  |  |  | aegis |  |  |  |
|  | nterAgent |  |  |  |  |  |  |  |  |
|  | QemuGuestA |  |  |  |  |  |  | An exception occurs on a specific instance feature. | Check whether the Quick EMUlator (QEMU) guest agent (qemu-guest-agent) is installed in the operating system. The QEMU guest agent runs on VMs to interact with hosts. If the QEMU guest agent is installed, specific ECS services are unavailable, and the instance is not full-featured. |
|  |  | QemuGuestA |  |  |  | q | emuguesta | An |  |
|  | gen |  |  |  |  |  |  |  |  |
|  |  |  | t |  | gent |  |  |  |  |

Elastic Compute Service

###### Obtain a Linux image file

This topic describes how to obtain the image file of a Linux virtual machine (VM). After you properly configure a Linux VM, you can obtain the Linux image file generated for the VM.

**Procedure**

1. Open Oracle VM VirtualBox Manager and select a VM. Example: centos VM.
2. Click **Settings**.
3. Choose **Storage > centos VM.vhd**.
4. In the **Information** section on the right side, find the path of the disk file. Example:
C:\Users\Administrator\VirtualBox VMs\centos VM\centos VM.vhd.
5. Access the path to obtain the generated Linux image file.

##### Convert the format of an image

You can import only images in the RAW, VHD, and qcow2 formats to Elastic Compute Service (ECS). To import images in other formats, you must use a tool to convert the images to a supported format. This topic describes how to convert the format of an image in Windows and Linux.

**Background information**

You can use the qemu-img tool to convert an image from the VMDK, VDI, VHDX, qcow1, or QED format to the RAW, VHD, or qcow2 format. You can also convert the format of an image between the RAW, VHD, and qcow2 formats. Elastic Compute Service

**Convert the format of an image on an on-premises Windows**

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

1. Install qemu-img.
For Ubuntu, run the `apt install qemu-img` command. For CentOS, run the `yum install qemu-img` command.
2. Run the `qemu-img convert -f raw -O qcow2 centos.raw centos.qcow2` command to convert
the image format. Parameter description:

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | The organization in which the custom image is to be used. |
| Resource Set | Yes | The resource set in which the custom image is to be used. |
| Region | Yes | The region in which the custom image is to be used. |

Elastic Compute Service `-f` is followed by the source image format. `-O` is case-sensitive. It is followed by the destination image format, source image name, and destination image name.

##### Import an image

After you upload an image to an Object Storage Service (OSS) bucket, you can import the image to Elastic Compute Service (ECS) and use the image as a custom image.

**Prerequisites**

An image is created. The image meets the limits and requirements for image import and can be imported in the RAW, VHD, or QCOW2 format. For more information, see Limits on importing images and Convert the format of an image. You have permissions to import images. For more information, see **Permission**
**management** in **Apsara Uni-manager Operations Console User Guide** .
An image file is uploaded to a bucket in the OSS console or by calling the OSS API. For more information, see the **Upload objects** topic in **OSS User Guide** or the **PutObject** topic in
**OSS Developer Guide**.

**Note**

Make sure that the OSS bucket resides in the region to which you want to import the image as a custom image. In an environment in which multiple OSS clusters exist, ECS has requirements for the OSS buckets from which you want to import images. We recommend that you specify a bucket whose domain name starts with OSS- to import images.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Custom Image** tab, click **Import Image**.
5. In the **Import Image** panel, configure the parameters. The following table describes the
parameters.

| Image File | Yes | The type of the image file to be uploaded. Valid values: Select an Existing OSS File and Local File. Note If you set the Image File parameter to Local File when you import an image, the image file is first uploaded to the destination OSS bucket. Make sure that the OSS bucket has sufficient capacity. |
|---|---|---|
| Image Name | Yes | The name of the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and _ colons (:). The name must start with a letter. |
| Sharing Scope | Yes | The scope in which to share the custom image. Valid values: Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| License Type | No | The type of the license used to activate the operating system in the image after the image is imported. Default value: BYOL. Valid values: BYOL (default) Aliyun Note The value Aliyun is unavailable and will be available soon. |
| Operating System | Yes | The operating system. Valid values: Linux and Windows. |
| System Disk Size (GiB) | Yes | The size of the system disk on an ECS instance. Unit: GiB. |

Elastic Compute Service

| Architecture | Yes | The architecture of the operating system. Valid values: x86 64 _ arm64 i386 Note The architecture types that are displayed in the ECS console prevail. |
|---|---|---|
| Platform | Yes | The platform supported by the operating system. Linux supports platforms, such as CentOS, Ubuntu, SUSE, openSUSE, Debian, CoreOS, Aliyun, and Others Linux. Note The Linux distributions that are displayed in the ECS console prevail. Windows: Windows Server 2003 Windows Server 2008 Windows Server 2012 Windows Server 2016 Windows Server 2019 Windows Server 2022 |
| Startup Mode | Yes | The boot mode of the custom image. Valid values: BIOS and UEFI. |
| Image Description | No | The description of the custom image. |
| Add Data Disk Image | No | Specifies whether to import other images that contain data from data disks. If you select Add Data Disk Image, you must click Add and specify parameters, including OSS Bucket Name, OSS Object Name, Image Format, Device Name, and Disk Capacity to add data disk images. |

Elastic Compute Service
6. Click **OK**.

**Result**

You can go to the Images page to view the creation progress of the custom image. For more information, see View a custom image. After the custom image is created, 100% is displayed in the Progress column.

| Parameter | Required | Description |
|---|---|---|
| OSS Bucket | Yes | Select an OSS bucket that resides in the same region as the custom image. |
| OSS Prefix | Yes | Specify a prefix for the name of the custom image object. The prefix can be 1 to 30 characters in length. The prefix can contain letters and digits. For example, if you set OSS Prefix to Demo, the exported image is named Demo-[Automatically generated object name]. |

Elastic Compute Service

#### Export a custom image

You can export custom images to Object Storage Service (OSS) buckets and download the images to your on-premises device.

**Prerequisites**

OSS is activated and an OSS bucket is created. For more information, see **Quick start >**
**Create buckets** in the OSS User Guide in the Apsara Stack Documentation Center.
Your account has permissions to export images. For more information, see **Enterprise >**
**Access control management** in the Apsara Uni-manager Management Console User Guid
e in Apsara Stack Documentation Center. Elastic Compute Service does not allow custom images to be exported to arbitrary Object Storage Service (OSS) buckets. If multiple OSS clusters exist in the current environment, we recommend that you export custom images to OSS buckets that are created by using domain names prefixed with OSS-**. You can export custom images that are in the RAW, VHD, or QCOW2 format. Custom images can be exported only to their original formats. For example, you can only export RAWformatted custom images in the RAW format.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Find the custom image that you want to export. In the **Actions** column, click **Export**
**Image**.
6. Configure the parameters described in the following table.
7. Click **OK**.
Elastic Compute Service
8. **Optional**: In the OSS console, download the custom image file to an on-premises device.
For more information, see **Quick Start > Obtain object URLs** in the OSS User Guide in the Apsara Stack Documentation Center.

#### Delete a custom image

You can delete custom images that you no longer use. Before you delete a custom image, take note of the following items: After a custom image is deleted, the image can no longer be used to create instances. After a custom image is deleted, the instances that use this image remain available but do not support hot configuration changes or system disk re-initialization (operating system reset). Before you delete a shared image, you must unshare the image. After a shared image is deleted: The accounts from which the image is unshared can no longer query the image by using the Elastic Compute Service (ECS) console or by calling an API operation. The accounts from which the image is unshared can no longer use the image to create instances or replace system disks. The system disks of the instances that were created from the shared image cannot be reinitialized. If you delete a custom image, snapshots contained in the image are not deleted. If you do not want to retain the snapshots, go to the Snapshots page and delete the snapshots.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Custom Image** to go to the custom image list.

**Note**

To quickly find and manage custom images that are shared by the current organization, choose **Shared Image > Shared by Me**.
5. Use one of the following methods to delete a custom image:
Delete a single image: Method 1: Find the image that you want to delete, click the More icon, and then click
**Delete Image** in the **Actions** column.
Method 2: Select the image that you want to delete and click **Delete** in the lower part of the page. Delete multiple images: Select the images that you want to delete and click **Delete** in the lower part of the page.
6. Click **Delete**.

| Public image type | Description | Technical support |
|---|---|---|
| Alibaba Cloud Linux images | Alibaba Cloud Linux images are custom, proprietary operating system images provided by Alibaba Cloud for ECS instances. Alibaba Cloud Linux images are thoroughly tested to ensure their security, stability, and normal startup and operation. | Alibaba Cloud provides technical support to help resolve the issues that may occur when you use Alibaba Cloud Linux images. |

Elastic Compute Service

### Public images

#### Public image overview

Public images are images that are provided by Alibaba Cloud to create a secure, stable runtime environment for applications that are deployed on Elastic Compute Service (ECS) instances. This topic describes the types of public images: Alibaba Cloud Linux images and third-party and open source images.

**Public image types**

Public images provided by Alibaba Cloud in Apsara Stack support almost all Windows Server operating systems and mainstream Linux operating systems. The following table describes two types of public images provided by Alibaba Cloud.

| Third-party and open source images | Third-party and open source images are thoroughly tested and released by Alibaba Cloud to ensure their security, stability, and normal startup and operation. The following third-party public images are available: Windows: Windows Server Linux: Anolis OS CentOS Stream Red Hat AlmaLinux Rocky Linux Debian Ubuntu OpenSUSE SUSE Linux Kylin UOS openEuler NFS | We recommend that you contact corresponding operating system vendors or open source communities for technical support. Alibaba Cloud also provides technical support to help identify issues. |
|---|---|---|

| Architectur e | Instance family | Operating system version |
|---|---|---|

Elastic Compute Service

**Note**

The boot mode of an instance type includes Unified Extensible Firmware Interface (UEFI), Basic Input/Output System (BIOS), and the system-defined mode that supports both UEFI and BIOS. UEFI-Preferred indicates that the image supports both the UEFI and BIOS modes. In Apsara Stack V3.18.6, the following images support UEFI-Preferred. However, GPU-accelerated instance types do not support UEFI-Preferred. aliyun_3_x86_64_20G_pro_alibase_20241225.vhd anolisos_8_9_x86_64_20G_anck_alibase_20240724.vhd debian_12_9_x86_64_20G_alibase_20250314.vhd ubuntu_22_04_x86_64_20G_alibase_20241115.vhd ubuntu_24_04_x86_64_20G_alibase_20241115.vhd Alibaba Cloud Linux images are Linux public images developed by Alibaba Cloud. The following table describes the Alibaba Cloud Linux images that are available in the x86 and ARM architectures.

| x86 | Intel hygon | Alibaba Cloud Linux 3 |
|---|---|---|
|  |  | Alibaba Cloud Linux 3 Container-optimized Edition |
|  |  | Alibaba Cloud Linux 3 MLPS |
|  |  | Alinux pro XC |
|  |  | Alinux pro XC MLPS |
|  |  | Alibaba Cloud Linux 4 |
|  |  | Alibaba Cloud Linux 4 Container-optimized Edition |
|  |  | Alibaba Cloud Linux 4 Pro XC |
|  |  | Alibaba Cloud Linux 4 Pro XC Container-optimized Edition |
| ARM | Kunpeng Feiteng | Alibaba Cloud Linux 3 |
|  |  | Alibaba Cloud Linux 3 MLPS |
|  |  | Alibaba Cloud Linux 3 Pro XC |
|  |  | Alibaba Cloud Linux 3 Pro XC MLPS |
|  |  | Alibaba Cloud Linux 4 |
|  |  | Alibaba Cloud Linux 4 Container-optimized Edition |
|  |  | Alibaba Cloud Linux 4 Pro XC |
|  |  | Alibaba Cloud Linux 4 Pro XC Container-optimized Edition |

Elastic Compute Service Alibaba Cloud provides third-party and open source images. The following table describes the operating systems supported by different instance families and the available versions of the operating systems.

| Instance family | Operating system type | Operating system version |
|---|---|---|
| Intel | Red Hat | Red Hat 9 |
|  | CentOS Stream | CentOS Stream 9 |
|  | AlmaLinux | AlmaLinux 8.10 AlmaLinux 9 |
|  | Rocky Linux | Rocky Linux 8.10 Rocky Linux 9 |
|  | Debian | Debian 11 Debian 12 |
|  | Ubuntu | Ubuntu 20.04 Ubuntu 22.04 Ubuntu 24.04 |
|  | OpenSUSE | OpenSUSE 15.6 |
|  | SUSE Linux | SUSE Linux Enterprise Server 15 SP6 |
|  | Anolis OS | Anolis OS 8.8 ANCK (MLPS 2.0 Level 3) Anolis OS 8.9 ANCK |

Elastic Compute Service

**Note**

You can view or find other public images that are available in the ECS console. For more information, see Find a public image. As of June 30, 2024, all CentOS versions have entered the end of life (EOL) phase. Alibaba Cloud discontinued support for CentOS, such as updated images, software updates, and security patches. ECS instances that are using CentOS images are not affected and can continue to run as expected.

**x86**

| Intel hygon |  |  |
|---|---|---|
|  | Windows Server | Windows Server 2025 Datacenter Edition 64-bit (Simplified Chinese) Windows Server 2025 Datacenter Edition 64-bit (English) Windows Server 2022 Datacenter Edition 64-bit (Simplified Chinese) Windows Server 2022 Datacenter Edition 64-bit (English) Windows Server 2019 Datacenter Edition 64-bit (Simplified Chinese) Windows Server 2019 Datacenter Edition 64-bit (English) Windows Server 2016 Datacenter Edition 64-bit (Simplified Chinese) Windows Server 2016 Datacenter Edition 64-bit (English) Note Microsoft has discontinued support for Windows Server 2008 and Windows Server 2008 R2 since January 14, 2020 and support for Windows Server 2012 and Windows Server 2012 R2 since October 10, 2023. Alibaba Cloud no longer provides technical support for ECS instances that run these operating systems. If your ECS instances run these operating systems, upgrade the operating systems to Windows Server 2016 or later at the earliest opportunity. |
|  | Kylin | Kylin V10 2403 SP3 Kylin V10 2403 SP3 (UEFI) KylinOS v3 3 9A _ _ Kylin V11 2503 |
|  | UOS | UOS Server V20 1070a UOS Server V20 1070a (UEFI) |
|  | OpenEuler | Openeuler 22 03 |
|  | NFS | NFS-CHINA Highly Trusted Server OS V4 |

| Instance family | Operating system type | Operating system version |
|---|---|---|
|  | Anolis OS | Anolis OS 8.8 ANCK for ARM (MLPS 2.0 Level 3) Anolis OS 8.9 ANCK for ARM |

Elastic Compute Service

**ARM**

| User Guide·Image |  |  |
|---|---|---|
| Kunpeng Feiteng |  |  |
|  | Kylin | Kylin V10 SP3 2403 ARM Kylin V10 2204 National Defense Edition Kylin V11 2503 |
|  | UOS | UOS Server V20 1070a ARM |
|  | OpenEuler | Openeuler 22 03 |
|  | Red Hat | Red Hat 9 |

| Operation | Procedure | References |
|---|---|---|
| View images | You can view public images that are available in the current organization in the ECS console. You can search for a specific public image by image type, name, or ID. | Find a public image |
| View instances that use an image | You can view instances that use a specific public image to obtain the usage details of the image. | View instances that use a specific image |

**Supported operations**

The following table describes the operations that can be performed on public images.

#### Find a public image

You can view the details of all public images that are available in the current organization, region, and resource set in the Elastic Compute Service (ECS) console. You can find a specific public image by image name or ID. Then, you can create instances from the image or perform other operations on the image.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Public Image**.
On the public image list, view the details of the public image that you want to manage, such as the image ID, name, and startup mode in the **Image ID/Name** and **Startup Mode** columns.
5. Click Advanced Filter and specify one or more filter conditions. The image list displays
images that match the specified conditions.

| Filter option | Description |
|---|---|
| Image ID | You must enter an exact image ID. |
| Image Name | You must enter an exact image name. |

| Operation | Description | References |
|---|---|---|

Elastic Compute Service
6. In the **Image ID/Name** column, click the image ID to view the Basic Information and
Operation Log. On the **Basic Information** page, you can view the image name, image ID, operating system, platform, snapshot details, and other information. Click the **Operation Log** to view the operation logs of public images, including operation name, operator, execution status, operation source (console call or API call), operation type, operation source IP, operation time, and other information. Search for operation logs that you require by specifying filter conditions. Select a filter condition from the drop-down list and enter the corresponding information in the search box to search operation logs. The operation logs that meet the specified filter condition are displayed. Click **Advanced Filter**, specify multiple filter conditions, and then click **Search** to search operation logs. Click **Operation Details** in the Actions column of an operation to view the operation details.

**Note**

### Shared custom images

#### Overview

Shared custom images are images that are shared with you by other level-1 organizations. You can use shared custom images to create Elastic Compute Service (ECS) instances.

**Introduction**

Shared custom images are images that are shared with you by other level-1 organizations. Shared custom images provide the following features: Shared custom images do not count against the image quota of the sharee. To modify a shared custom image, you must contact the sharer of the image. You can use a shared custom image to create instances. For more information, see Create an instance by using the wizard.

**Related operations**

The following table describes the operations that can be performed on shared custom images.

| View images | You can view shared custom images that are available in the current organization in the ECS console. You can find a specific shared custom image by image type, image name, image ID, or snapshot ID. | Find a shared custom image |
|---|---|---|
| View instances that use a specific image | You can view instances that use a specific shared custom image to obtain the usage details of the image. | View instances that use a specific image |

| Filter option | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. Fuzzy search is supported. |
| Image Name | Enter an image name to search for the image. Fuzzy search is supported. |
| Tag | Enter the key or value of a tag to search for the images that use the tag. Note On the Images page, select images whose tags you want to manage and click Batch Add Tags or Batch Remove Tags in the lower part of the page to batch add tags to or batch remove tags from the images. |

Elastic Compute Service

#### Find a shared custom image

You can find a specific shared custom image by image name or ID in the Elastic Compute Service (ECS) console. Then, you can create instances from the image or perform other operations on the image.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Choose **ECS Image** > **Shared Image**.
5. Click the **Shared** tab.
You can view details of custom images that were shared by others, such as the image ID, image name, and startup mode in the **Image ID/Name** and **Startup Mode** columns.
6. Click Advanced Filter and specify one or more filter conditions. The image list displays
images that match the specified conditions.

| Operation | Description | References |
|---|---|---|
| View images | You can view the globally shared images in the current organization in the ECS console. You can search for globally shared images by image type, image name, or image ID. | Find a globally shared image |
| View instances that use a specific image | You can view the ECS instances that use a specific globally shared image to obtain the usage information of the image. | View instances that use a specific image |

Elastic Compute Service

### Globally shared images

#### Overview

Globally shared images are available to all organizations. You can use globally shared images in your organization to create Elastic Compute Service (ECS) instances.

**Introduction**

Globally shared images are the custom images that are globally shared by administrators in the Apsara Uni-manager Operations Console. Globally shared images provide the following benefits: After a custom image is globally shared, it appears in the list of globally shared images for each organization. Globally shared images can be modified only by the administrators who share the images.

**Note**

For information about how to modify a globally shared image, see **ECS operations**
**and maintenance > ECS > Images > Manage images** in the ECS Operations and M
aintenance Guide in the Apsara Stack Documentation Center. If your custom image is configured as a globally shared image, the image is displayed in both the custom image list and globally shared image list. You can use a globally shared image to create ECS instances. For more information, see Create an instance by using the wizard.

**Related operations**

The following table describes the operations that you can perform on globally shared images.

#### Find a globally shared image

| Filter option | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. |
| Image Name | Enter an image name to search for the image. |

Elastic Compute Service You can view the information of globally shared images in the Elastic Compute Service (ECS) console. You can also search for globally shared images by image name or ID and then use the images to create instances or perform other operations.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **ECS Image** tab, click the **Shared Image** tab.
5. Click **Shared Globally**.
You can view image information in the global shared image list, such as **Image ID/Name**,
**Image Size**, and **Startup Mode**.
6. Select a filter option from the drop-down list and enter relevant information to search for
images.

### Bare metal instance images

Bare metal instance images are used to maintain the metadata of images that are used to install bare metal instances. You can search for, manage the status of, and delete custom images of bare metal instances. You can search for and manage the status of public images of bare metal instances.

#### Manage custom images for bare metal

## instances

You can view all custom images for bare metal instances in the current organization, region, and resource set in the Elastic Compute Service (ECS) console. You can search for a specific custom image by image ID or name. Then, you can create instances from the custom image or perform other operations on the custom image.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Images page, click the **Bare Metal Instance Image** tab and then click the **Custom**
**Image** tab.
5. Select a filter condition from the drop-down list and enter relevant information in the
search box. The custom images that meet the specified filter condition are automatically displayed.

| Filter condition | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. Fuzzy search is supported. |
| Image Name | Enter an image name to search for the image. Fuzzy search is supported. |

Elastic Compute Service
6. Optional. Find the custom image that you want to manage, move the pointer over **Status**
in the **Actions** column, and then select **Enable Image** or **Disable Image**. You can delete custom images that are no longer needed.

**Note**

When you delete an image, the source image file is deleted at the same time. Proceed with caution.
1. Perform Step 1 to Step 4 in the preceding section to go to the Custom Image tab.
2. Find the custom image that you want to delete and click **Delete Image** in the **Actions**
column.
3. In the message that appears, click **Delete**.

#### Manage public images for bare metal

## instances

Public images are images that are provided by Alibaba Cloud to create a safe, stable runtime environment for applications that are deployed on Elastic Compute Service (ECS) bare metal instances. This topic describes how to manage public images for bare metal instances in the ECS console.

**Background information**

Public images in the TGZ and QCOW2 formats are supported in Apsara Stack. By default, Apsara Stack provides specific public images that have been adapted to ECS. If no public images are available on the Public Image tab or public images are not in the
**Enabled** state, contact technical support for help.
If a public image is in the **Disabled** state, the public image is unavailable when you create ECS bare metal instances. In this case, you need to change the state of the public image to
**Enabled** on the Images page.

**Note**

Public images cannot be deleted.
1. Log on to the ECS console.

| Filter condition | Description |
|---|---|
| Image ID | Enter an image ID to search for the image. Fuzzy search is supported. |
| Image Name | Enter an image name to search for the image. Fuzzy search is supported. |

Elastic Compute Service
2. In the navigation pane on the left, choose **Instances & Images > Images**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Images page, click the **Bare Metal Instance Image** tab and then click the **Public**
**Image** tab.
5. Select a filter condition from the drop-down list and enter relevant information in the
search box. The public images that meet the specified filter condition are automatically displayed.
6. Optional. Find the public image that you want to manage, move the pointer over **Status** in
the **Actions** column, and then select **Enable Image** or **Disable Image**. Elastic Compute Service

## Snapshots

### Overview

You can back up data on your disks by taking point-in-time snapshots. Then, you can use the snapshots to restore your disk data to the point in time when the snapshots are taken. This topic describes the scenarios for using snapshots and the mechanisms of creating and deleting snapshots. This topic also describes the operations related to snapshots.

**Scenarios**

You can use snapshots for scenarios such as environment replication and disaster recovery: You may want to use the data of a disk as the source data for write operations or save data to a different disk. In this case, you can create a snapshot for a disk and then create another disk from the snapshot. The new disk contains the data of the original disk. Issues such as application errors or malicious read operations and write operations may occur on disks that store data. As a result, these disks require additional protection mechanisms. You can create snapshots at regular intervals to restore data to a previous point in time when data errors occur. Snapshots are classified into full snapshots and incremental snapshots. The first snapshot that you create or retain for a disk is a full snapshot. The snapshot contains all data blocks that are written to the disk at the time of snapshot creation except for empty data blocks. Subsequent snapshots that you create from the disk are incremental snapshots that store only data blocks that have changed since the last snapshot. The metadata of both full snapshots and incremental snapshots includes the information of all data blocks. When you roll back a disk by using a snapshot, you can restore all disk data to the point in time at which the snapshot is created.

**Note**

After a disk is initialized, it is divided into multiple data blocks based on logical block addresses (LBAs). These data blocks are the minimum granularity of data backup for snapshots. When data is written to the data blocks, every changed data block is marked to be copied in the next snapshot. Data written to and modified in the disk do not affect the existing snapshots. Snapshots do not affect the original disk data.

**Example**

Data is written to a disk of an Elastic Compute Service (ECS) instance at 10:00:00 and 11:00:00. The following section describes how snapshots are created for the disk:
1. At 9:00:00, the disk contains data blocks A, B, and C, and the first snapshot (Snapshot 1) is
created for the disk. Data blocks A, B, and C are all backed up in Snapshot 1. Snapshot 1 is a full snapshot that backs up all data on the disk.
2. Data continues to be written to the disk. Data block A is changed to A1, data block B is
changed to B1, and data block D is added. The second snapshot (Snapshot 2) is created at 10:00:00 for the disk. Snapshot 2 is an incremental snapshot that backs up only the changed data blocks A1, B1, and D. The metadata of Snapshot 2 includes the information of all data blocks A1, B1, C, and D of the disk. The entire data block C is contained in Snapshot 1.
3. Data continues to be written to the disk. Data block C is changed to C1 and data block E is
added. The third snapshot (Snapshot 3) is created at 11:00:00. Snapshot 3 is an incremental snapshot that backs up only the changed data blocks C1 and E. The metadata Elastic Compute Service of Snapshot 3 includes the information of all data blocks A1, B1, C1, D, and E of the disk. The entire data blocks A1, B1, and D are contained in Snapshot 2.
4. The preceding processes are repeated.
In contrast to creating a snapshot, when you delete a snapshot, space is freed up based on the data blocks contained in the snapshot and the data block mappings. When the first snapshot of a disk is deleted, the first incremental snapshot inherits the attributes of this deleted snapshot to become a full snapshot. If the disk has only the full snapshot that is deleted, the first snapshot to be created for the disk later is a full snapshot that backs up all data blocks written since the disk is created.

**Example**

Snapshot 1, Snapshot 2, and Snapshot 3 are created for a disk of an ECS instance. The following section describes the data blocks contained in each snapshot: Snapshot 1: contains data blocks A, B, and C. Snapshot 2: contains data blocks A1 (changed from data block A), B1 (changed from data block B), C (unchanged), and D (new data block). The entire data block C is contained in Snapshot 1. Snapshot 3: contains data block A1 (unchanged), B1 (unchanged), C1 (changed from data block C), D (unchanged), and E (new data block). The entire data blocks A1, B1, and D are contained in Snapshot 2. The following section describes how the disk snapshots are deleted:
1. Snapshot 1 is deleted at 14:00:00. Data blocks A and B contained in Snapshot 1 are not
referenced and are directly deleted. Data block C is retained because it is referenced by Snapshot 2. Snapshot 2 becomes a full snapshot and contains data blocks A1, B1, C, and D. Snapshot 3 is still an incremental snapshot.
2. Snapshot 2 is deleted at 15:00:00. Data block C contained in Snapshot 2 is not referenced
and is directly deleted. Data blocks A1, B1, and D are referenced by Snapshot 3 and are retained. In this case, Snapshot 3 becomes a full snapshot and contains data blocks A1, B1,

| Operation | Description | Procedure |
|---|---|---|

Elastic Compute Service C1, D, and E.
3. Snapshot 3 is deleted at 16:00:00. All data blocks in Snapshot 3 are not referenced and are
deleted. You can use snapshots based on your business requirements. The following table describes operations related to snapshots.

**Note**

Snapshots are stored in Object Storage Service (OSS), but are hidden. Snapshots do not occupy storage space in OSS buckets. Snapshot operations can be performed only in the ECS console or by calling API operations. This topic describes snapshot operations that can be performed in the ECS console. For information about how to call API operations to manage snapshots, see **ECS Developer Guide**.

| Create snapshots | You can use the following methods to create snapshots: You can manually create snapshots. Manually created snapshots are called manual snapshots. You can create manual snapshots before you perform high-risk operations to improve fault tolerance. You can create snapshots for a single disk or create snapshots for multiple disks on one or more ECS instances by creating a snapshot-consistent group. You can create automatic snapshot policies to create snapshots. Snapshots created based on these policies are called automatic snapshots. After you create an automatic snapshot policy and apply it to a disk, the system creates snapshots for the disk at the points in time specified in the policy. You can use automatic snapshots to back up data and improve the security of your business data. | Create a snapshot Create a snapshot-consistent group Create an automatic snapshot policy |
|---|---|---|
| Delete snapshots | When you want to free up space or when the maximum number of snapshots is reached, you can delete snapshots that are no longer needed. | Delete snapshots |
| Roll back disks by using snapshots | When the system is unresponsive or when accidental changes are made, you can roll back a disk to a previous version by using one of its snapshots. | Roll back a disk by using a snapshot |
| Create an image from a system disk snapshot | You can create a custom image from a snapshot that contains the operating system and data of an ECS instance. Then, you can use the custom image to create multiple instances that have identical application environments. | Create a custom image |
| Create a disk from a snapshot | A single snapshot can be used to create multiple identical disks. | Create a disk |

Elastic Compute Service

### Snapshot chain

Elastic Compute Service A snapshot chain is a chain of all snapshots created for a disk. A disk corresponds to a snapshot chain. You can view the size of all snapshots of a disk based on the snapshot chain of the disk.

**Background information**

The total size of snapshots of a disk is calculated based on the snapshot chain of the disk. A snapshot chain is a chain of all snapshots created for a disk. The total size represents the amount of storage space occupied by the data blocks in all snapshots of the disk. The following section describes snapshot size-related concepts: Full snapshot size: the amount of storage space occupied by all data blocks in a single snapshot. Incremental snapshot size: the amount of storage space occupied by the data blocks that represent the difference between the current snapshot and the previous snapshot in the same snapshot chain. Total snapshot size: the sum of the size of the initial full snapshot and the sizes of all subsequent incremental snapshots.

**Prerequisites**

At least one snapshot is created for a disk. For more information, see Create a snapshot. The calculation of the snapshot chain size takes several minutes, and the size is only for reference.

**Procedure**

1. Log on to the Elastic Compute Service (ECS) console.
i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Computing > Elastic Compute Service**.
2. In the left-side navigation pane, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Snapshot Chain** tab, select a field from the drop-down list, and enter a keyword
in the search box. Then, click the condition are displayed in the list.

**Note**

You can search for snapshot chains by using the **Automatic Identification**,
**Snapshot Chain ID**, **Source Disk ID**, **Instance ID**, or **Filter by Tag** filter
option. Fuzzy search is supported for the **Snapshot Chain ID**, **Source Disk ID**, and
**Instance ID** filter options.
You can specify multiple filter conditions to narrow down search results.
5. In the **Snapshot Chain Size** column of the snapshot chain, view the size of all snapshots of
the disk.

**Related operations**

After you find the snapshot chain of the disk, you can perform the following operations as required.

| Operation | Description |
|---|---|
| View the details of the snapshot chain | Click the ID of the snapshot chain or clickV iew Details in the Actions column. You can view the information about the snapshots of the disk and perform operations on a snapshot such as editing the snapshot, rolling back the disk by using the snapshot, creating a custom image from the snapshot, and deleting the snapshot. |
| View the information about the instance to which the corresponding disk of the snapshot chain belongs | Click the instance ID in the Instance ID/Name column of the snapshot chain to view the information about the instance to which the corresponding disk of the snapshot chain belongs. |
| View the information about the disk to which the snapshot chain corresponds | Click the disk ID in the Source Disk ID/Name column of the snapshot chain to view the information about the disk to which the snapshot chain corresponds. |

Elastic Compute Service

### How snapshots work

Snapshots are point-in-time backups of disks. You can use a snapshot of a disk to restore disk data to the point in time when the snapshot was created. This topic describes how to create and delete snapshots and calculate the snapshot size. This topic also describes the relationship between the snapshot size and the disk size. You can manually or automatically create snapshots for disks based on your business requirements. For more information, see Create a snapshot or Create an automatic snapshot policy. Snapshots are classified into full snapshots and incremental snapshots. The first snapshot that you create for a disk is a full snapshot. The snapshot contains all data blocks that were written to the disk when the snapshot was created, except empty data blocks. Subsequent snapshots that you create for the disk are incremental snapshots and contain only data blocks that changed since the previous snapshot. The metadata of full and incremental snapshots includes information about all data blocks. When you roll back a disk by using a snapshot of the disk, you can restore all data of the disk to the point in time when the snapshot was created.

**Note**

After you initialize a disk, the disk is divided into data blocks based on logical block addresses (LBAs). The data blocks are the minimum granularity for data backup in snapshots. When data is written to the data blocks, every changed data block is labeled for copying to the next snapshot. Data that is written to and modified on the disk does not affect the created snapshots. Snapshots do not affect the original disk data. Created snapshots are stored in Object Storage Service (OSS). By default, snapshot data is stored in zone-redundant storage (ZRS) buckets in regions where OSS supports ZRS to maximize data redundancy.

| 1 |  |
|---|---|

| 2 |  |
|---|---|

Elastic Compute Service In regions where OSS does not support ZRS, snapshot data is stored in locally redundant storage (LRS) buckets. For data security reasons, you cannot select the OSS buckets that you create to store snapshot data. After you use a snapshot to create or roll back a disk, the data blocks that are contained in the snapshot are loaded from OSS to the disk. If you access the snapshot data that has not been loaded, the system immediately loads the snapshot data from OSS to the disk. The time required to complete the loading process varies based on the snapshot size and could be minutes or hours. Before all data blocks in the snapshot are loaded to the disk, the read latency of the disk increases. When all data blocks in the snapshot are loaded to the disk, the read latency of the disk returns to the normal level.

**Example**

Assume that data is written to a disk on an Elastic Compute Service (ECS) instance at 10:00:00 and 11:00:00. The following section describes how snapshots are created for the disk:
1. At 9:00:00, the disk contains data blocks A, B, and C, and the first snapshot (Snapshot 1) is
created for the disk. Data blocks A, B, and C are all backed up in Snapshot 1. Snapshot 1 is a full snapshot that backs up all data on the disk.
2. Data continues to be written to the disk. Data block A is changed to A1, data block B is
changed to B1, and data block D is added. The second snapshot (Snapshot 2) for the disk is created at 10:00:00. Snapshot 2 is an incremental snapshot that backs up only the changed data blocks A1, B1, and D. The metadata of Snapshot 2 includes information about all data blocks (A1, B1, C, and D) of the disk. Data block C is derived from Snapshot 1.
3. Data continues to be written to the disk. Data block C is changed to C1, and data block E is
added. The third snapshot (Snapshot 3) is created at 11:00:00. Snapshot 3 is an incremental snapshot that backs up only the changed data blocks C1 and E. The metadata of Snapshot 3 includes the information of all data blocks A1, B1, C1, D, and E of the disk. Data blocks A1, B1, and D are derived from Snapshot 2.
4. The preceding processes are repeated.
Elastic Compute Service If you want to free up storage space or if the maximum number of snapshots is reached, you can delete snapshots that are no longer needed. For information about how to delete a snapshot, see Delete a snapshot.

**Note**

Each disk can have up to 256 manual snapshots and 1,000 automatic snapshots. Compared with creating a snapshot, you must free up storage space based on the data blocks contained in the snapshot and the relationship between the data blocks when you delete a snapshot. When you delete the first snapshot of a disk, the first incremental snapshot inherits the attributes of the deleted snapshot to become a full snapshot. If the disk has only the full snapshot that is deleted, the next snapshot created for the disk is a full snapshot that backs up all data blocks written since the disk was created.

**Example**

Assume that Snapshot 1, Snapshot 2, and Snapshot 3 are created for a disk on an ECS instance. The following section describes the data blocks that are contained in each snapshot: Snapshot 1: contains data blocks A, B, and C. Snapshot 2: contains data blocks A1 (changed from data block A), B1 (changed from data block B), C (unchanged), and D (new data block). Data block C is derived from Snapshot 1. Snapshot 3: contains data block A1 (unchanged), B1 (unchanged), C1 (changed from data block C), D (unchanged), and E (new data block). Data blocks A1, B1, and D are derived from Snapshot 2. The following section describes how the disk snapshots are deleted:
1. Assume that Snapshot 1 is deleted at 14:00:00. Data blocks A and B contained in Snapshot
1 are unreferenced and directly deleted. Data block C is retained because it is referenced by Snapshot 2. In this case, Snapshot 2 becomes a full snapshot and contains data blocks A1, B1, C, and D. Snapshot 3 remains as an incremental snapshot.
2. Then, Snapshot 2 is deleted at 15:00:00. Data block C contained in Snapshot 2 is
unreferenced and directly deleted. Data blocks A1, B1, and D are referenced by Snapshot 3 and retained. In this case, Snapshot 3 becomes a full snapshot and contains data blocks A1, B1, C1, D, and E.
3. Lastly, Snapshot 3 is deleted at 16:00:00. In this case, all data blocks in Snapshot 3 are
unreferenced and deleted.

|  | ECS Snapshot Snapshot Snapshot 1 2 3 A B AA1 BB1 A1 B1 backup backup backup backup backup backup Delete Snapshot 1<br>at A B 14:00:00 C1 E bac CC kup bacC sbnaaFcpD ukslul hopt In sb c nra e ac m pk se hu n op t tal bb aa cc D kk uu pp kup Full Incremental Incremental snapshot snapshot snapshot Snapshot Snapshot 2 3 A1 B1 backup backup Delete Snapshot 2<br>at C1 E 15:00:00 backup backup C backup Full Incremental snapshot snapshot Snapshot 3 A1 B1 D backup backup backup Delete Snapshot 3<br>at 16:00:00 C1 E backup backup Full snapshot The disk has no<br>snapshots and all<br>data blocks are released. |
|---|---|

|  | A1 |
|---|---|

Elastic Compute Service The total snapshot size of a disk is calculated at the granularity of snapshot chains. A snapshot chain is a chain of all snapshots created for a disk. The amount of storage space occupied by the data blocks of all snapshots of the disk is calculated. The following section describes the concepts involved in the snapshot size: Full snapshot size: the amount of the storage space occupied by all data blocks in a single snapshot. Incremental snapshot size: the amount of storage space occupied by the data blocks in a snapshot that changed since the previous snapshot in the same snapshot chain. Total snapshot size: the sum of the size of the first snapshot (full snapshot) and the size of all subsequent incremental snapshots. You can view the size of snapshots by snapshot chain in the ECS console. For more information, see View the snapshot size.

**Example**

Assume that data is written to a disk on an ECS instance at 10:00:00 and 11:00:00. The following section describes how to calculate the snapshot size of the disk:
1. Assume that the disk contains data blocks A (2 MB), B (2 MB), and C (2 MB). Snapshot 1 is
created at 9:00:00 and backs up data blocks A, B, and C. Snapshot 1 is a full snapshot.

| Write d | ata |
|---|---|

| Write | da | ta |
|---|---|---|

| Create a snapshot at 11:00: | 0 |
|---|---|
|  | e |

Elastic Compute Service Size of Snapshot 1 = Size of data block A + Size of data block B + Size of data block C = 6 MB
2. Data blocks A1 (2 MB), B1 (2 MB), and D (2 MB) are written to the disk. Snapshot 2 is
created at 10:00:00 and backs up only data blocks A1, B1, and D that changed since Snapshot 1. Snapshot 2 is an incremental snapshot. Size of Snapshot 2 = Size of data block A1 + Size of data block B1 + Size of data block D = 6 MB
3. Data blocks C1 (2 MB) and E (2 MB) are written to the disk. Snapshot 3 is created at
11:00:00 and backs up only data blocks C1 and E that changed since Snapshot 2. Snapshot 3 is an incremental snapshot. Size of Snapshot 3 = Size of data block C1 + Size of data block E = 4 MB
4. Total snapshot size = Size of Snapshot 1 + Size of Snapshot 2 + Size of Snapshot 3 = 16 MB
ECS Disk Disk data at 9:00:00 Disk data at 10:00:00 Disk data at 11:00:00 A1 B1 A1 B1 A (2 MB) B (2 MB) (2 MB) (2 MB) (2 MB) (2 MB) C1 (2 MB) (2 MB) D (2 MB) (2 MB) E (2 MB) Disk data at 9:00:00 Disk data at 10:00:00 C1 backup A backup B backup A1 backup B1 backup (2 MB) (2 MB) (2 MB) (2 MB) (2 MB) backup D backup (2 MB) (2 MB) Size of Snapshot 1 = 6 MB<br>(Full snapshot size)Size of Snapshot 2 = 6 MB<br>(Incremental snapshot size)

**Relationship between snapshot size and disk size**

The size of a single snapshot of a disk does not exceed the disk size. As the number of snapshots increases, the disk size may be smaller than the total size of all snapshots. Assume that you create a 40-GiB disk, write 20 GiB of data to the disk, and then create a snapshot for the disk. The size of the snapshot is 20 GiB. Assume that you continue to write 10 GiB of data to the disk and then create another snapshot for the disk. The disk size is still 40 GiB, and the total size of snapshots is 30 GiB. This process is repeated. You can use snapshot chains to view the snapshot size. For more information, see View the snapshot size.

**Differences between snapshot size and system capacity**

The snapshot size is calculated by using fixed-sized data blocks as the minimum granularity for data backup in snapshots. Elastic Compute Service When you delete a file from a disk, the used disk capacity that is displayed in the operating system decreases. When you delete a file from the file systems of the operating system, the file is labeled as Deleted, but the data of the file is not physically deleted. File deletion on disks is a write operation, which does not reduce the actual amount of disk space occupied by data. If a snapshot is created before a file is deleted, the snapshot still contains the data blocks that correspond to the deleted file after the file is deleted. If files are physically deleted from the file systems of the operating system, snapshots do not contain the data blocks of the deleted files. For more information, view the documentation of the TRIM mechanism of file systems. The snapshot size may still increase even if you do not write data to a system disk. When an operating system is running, system files are generated and written to the system disks and backed up in snapshots. The size of a snapshot may be slightly larger than the size of data that is written to the disk because specific metadata of file systems occupies disk space. The data blocks of the snapshot contain metadata and the written data. For example, if you create only 1 MB of text files on a disk, the size of the data backed up by snapshots is slightly larger than the size of the text files due to file system metadata. The snapshot size is greater than 1 MB.

### Disk snapshots

#### Create a snapshot

You can use snapshots to back up data, restore Elastic Compute Service (ECS) instances that were accidentally released, and create custom images. Before you roll back disks, modify critical system files, or change the operating system of an instance, you can create snapshots for disks to improve fault tolerance.

**Prerequisites**

The disk for which you want to create a snapshot must be in the **Running** or **Available** state. If the disk is in the **Running** state, the instance must be in the **Running** or **Stopped** state. If the disk is in the **Available** state, the disk must have been previously attached to an ECS instance. You cannot create snapshots for disks that have never been attached to ECS instances.

**Note**

If a cloud disk has never been attached to ECS instances, the data stored on the disk remains unchanged after the disk is created, and you do not need to create snapshots for the disk.

**Background information**

Up to 64 snapshots can be retained for each disk. Snapshots can be used in the following scenarios: Roll back data on disks. For more information, see Roll back a disk by using a snapshot. Create custom images. For more information, see the Create a custom image section of the "Create a custom image" topic. You cannot create custom images from the snapshots of data disks. Create a data disk from a data disk snapshot.

| Parameter | Description |
|---|---|
| Snapshot Name | The name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. The name can contain digits, letters, colons (:), underscores ( ), and hyphens (-). _ Note The name cannot start with auto because snapshots whose names start with auto are recognized as automatic snapshots. |

Elastic Compute Service To create a data disk from a snapshot, set Use Snapshot to Yes and then specify a snapshot on the Create Disk page. For more information, see Create a disk. The size of the disk to be created is determined by the size of the specified snapshot and cannot be changed. When you re-initialize a data disk created from a snapshot, the data on the disk is restored to that of the snapshot used to create the disk. When you create a snapshot, take note of the following items: For each disk, the first snapshot is a full snapshot and subsequent snapshots are incremental snapshots. A longer period of time is required to create the first snapshot. The period of time that is required to create an incremental snapshot varies based on the volume of data that is modified after the point in time when the previous snapshot was created. If a large volume of data is modified, a long period of time is required to create the snapshot.

**Note**

If you want to use a snapshot immediately after the snapshot is created, you can enable the instant access feature. We recommend that you create snapshots during off-peak hours. While a snapshot is being created for an instance, do not perform operations that will change the instance status, such as stopping or restarting the instance.

**Important**

If the status of the ECS instance changes, the snapshot cannot be created.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Disks page, find the disk for which you want to create a snapshot and click **Create**
**Snapshot** in the **Actions** column.
5. In the **Create Snapshot** dialog box, configure the parameters and click **OK**. The following
table describes the parameters.

| Instant Access | The instant access feature can accelerate the process of snapshot creation. You can use the instant access feature to create snapshots within seconds. Enable Instant Access: You can select this check box to enable the instant access feature. By default, this feature is disabled. Note The instant access feature can be enabled only for premium performance disks. Duration of Instant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. Valid values: 1 to 65535. |
|---|---|
| Snapshot Description | The description of the snapshot. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

Elastic Compute Service You can go to the Snapshots page to check the creation progress of the snapshot. For more information, see View snapshot details. After the snapshot is created, 100% is displayed in the Progress column.

#### View snapshot details

You can view the details of a created snapshot, including the snapshot name, snapshot ID, snapshot status, snapshot creation time, name of the disk for which the snapshot is created, ID of the disk for which the snapshot is created, and disk properties. You can also view the details of a custom image and disks that are created from a snapshot.

**Procedure**

**Note**

You can view the details of all snapshots that are created from a disk on the Disk Snapshots tab of the disk. For more information, see View disk details.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. On the Disk Snapshots tab, view the details of existing snapshots.
You can view snapshot information in the columns, including **Snapshot ID/Name**, **Status**,
**Organization/Resource Set**, **Instant Access**, **Disk ID/Name**, **Disk Capacity**, **Disk**
**Type (All)**, and **Snapshot Type**.
You can perform the following steps to specify the columns to be displayed in the snapshot list: i. In the upper-right corner of the snapshot list, click the icon.

| Section | Description |
|---|---|
| Basic Information | This section displays basic information about the snapshot, including the snapshot name, snapshot ID, snapshot status, snapshot creation progress, snapshot type, snapshot creation time, and Instance Access setting. |
| Disk Information | This section displays information about the disk for which the snapshot was created, including the disk name, disk ID, disk status, and disk type. |
| Relevant Information | Images created from snapshots This tab displays information about the custom images that are created from the snapshot, including the IDs, names, status, and sharing scopes of the custom images. You can click the ID of a custom image in the custom image list to go to the Custom Image tab of the ECS Image page and view the details of the custom image. For more information, see View a custom image. Disks Created from Snapshots This tab displays information about the disks that are created from the snapshot, including the IDs, names, status, categories, types, and encryption settings of the disks. You can click the ID of a disk in the disk list to go to theD isk Details tab and view the details of the disk. For more information, see View disk details. |

Elastic Compute Service ii. In the **Custom Columns** dialog box, select the columns to be displayed in the snapshot list and click **Save**.
6. Select a filter condition, such as **Snapshot ID**, from the drop-down list and enter relevant
information in the search box to search for snapshots. The snapshots that meet the specified filter condition are displayed.

**Note**

You can search for snapshots by snapshot name, snapshot ID, disk ID, creation time, or tag. Fuzzy search is supported only if you select **Snapshot Name**, **Snapshot ID**, or
**Disk ID** as the filter condition.
You can specify multiple filter conditions to narrow down search results.
7. In the **Snapshot ID/Name** column, click the ID of a snapshot to go to the Snapshot Details
page.

**View the snapshot details in the sections or tabs described in the following**

**table.**

**View operation logs of the snapshot.**

Click the **Operation Log** tab to view the operation logs of the snapshot, including the operation name, operator, execution status, operation source (console call or API call), operation type, source IP address of the operation, and operation time. Elastic Compute Service Search for operation logs that you require by specifying filter conditions. Select a filter condition from the drop-down list and enter the corresponding information in the search box to search for operation logs. The operation logs that meet the specified filter condition are displayed. Click **Advanced Filter**, specify multiple filter conditions, and then click **Search** to search for operation logs. Click **Operation Details** in the Actions column of an operation to view the operation details.

**Note**

Operation logs can be retained for seven days. To change the retention period of operation logs, contact the administrator to go to the **Log Storage**
**Settings** page in the **Configurations** module. For more information, see
**Configure log storage settings** in Configurations directory of the Apsara
Uni-manager Operations Console User Guide in the Apsara Stack Documentation Center. If the retention period of operation logs on the Log Storage Settings page is extended, historical operation logs that are not retained before the retention period is extended are not backfilled.

#### View the snapshot size

This topic describes how to view the capacity of all snapshots of a single disk and the total capacity of snapshots in the current region, and how to export snapshot capacity information.

**Prerequisites**

At least one snapshot is created for a disk. For more information, see Create a snapshot.

**View the snapshot size of a disk based on the snapshot chain**

**of the disk**

A snapshot chain is a chain of all snapshots created for a disk. A disk corresponds to a snapshot chain. For more information, see How snapshots work.

**Note**

The calculation of the snapshot chain capacity takes several minutes, and the capacity is only for reference. To view the size of all snapshots of a disk in the Elastic Compute Service (ECS) console, perform the following steps:
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots**>**Snapshots**.
3. In the upper-left corner of the top navigation bar, select the resource group and region in
which the resources reside.
4. On the **Snapshots** page, click the **Disk Snapshots** tab.
5. Find and copy the ID of the disk for which you want to view the snapshot size. Make sure
that at least one snapshot is created for the disk. Elastic Compute Service
6. Click the **Snapshot Chain** tab and click **View Details** in the **Actions** column to view the
snapshot size of the disk.
7. (Optional) Click **Details** in the **Actions** column of the specified snapshot chain.
You can view the snapshot information of the disk or perform the operations described in the following topics on the snapshot: Restore a disk To view the total snapshot size in a region in the ECS console, perform the following steps:
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots**>**Snapshots**.
3. In the upper-left corner of the top navigation bar, select the resource group and region
where the destination resources reside.
4. On the **Snapshots** page, you can view the total snapshot size in the current region.

**Export information about snapshot chains by Report**

To export information such as the snapshot capacity in the ECS console, perform the following steps:
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Storage & Snapshots**>**Snapshots**.
3. In the upper-left corner of the top navigation bar, select the resource group and region
where the destination resources reside.
4. Click the **Snapshot Chain** tab, select one or more snapshot chains, and then click the
icon in the upper-right corner.
5. In the **Export** dialog box, configure the **Export Data by Scope** and **Columns to Export**
parameters.
6. Click **OK**.

#### Roll back a disk by using a snapshot

If you have created a snapshot of a disk, you can use the snapshot to roll back the disk to the point in time when the snapshot was created. The disk rollback operation is irreversible. After the disk is rolled back, the data that was stored on the disk before the rollback operation is performed is lost and cannot be recovered. Exercise caution when you perform this operation.

**Prerequisites**

Before you roll back a disk by using a snapshot, make sure that the following requirements are met: Elastic Compute Service Snapshots have been created for the disk, and no snapshots are currently being created for the disk. For more information, see Create a snapshot. The disk is not released. The disk is attached to an instance that is in the **Stopped** state.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find a snapshot of the disk that you want to roll back and click **Roll Back Disk** in the
**Actions** column.

**Note**

You can roll back only one disk on an instance at a time. Other disks that are attached to the instance are not affected. After the rollback operation is complete, the entire disk (not a partition or a directory) is restored to the state that the disk was in when the snapshot was created.
6. In the message that appears, click **Roll Back Disk**.
7. Starts an ECS instance.
For more information, see Start an instance.

**What to do next**

After the disk is rolled back, the hosts configuration file and the configurations such as the hostname, SSH key pair, passwords, network settings, operating system repository settings, and clock source are initialized. You must reconfigure the file and configurations If you have resized the disk after you created the snapshot for the disk, you must log on to the instance to resize the file systems on the disk again after the disk is rolled back. For more information, see Resize a disk.

#### Share a snapshot

Snapshots created in an organization can be shared with other organizations. Members in the organizations with which the snapshots are shared can create disks based on the shared snapshots.

**Prerequisites**

A snapshot is created for a disk. For more information, see Create a snapshot.

**Background information**

Snapshots can be shared only among level-1 organizations. A single snapshot can be shared with up to 10 organizations at a time. A single snapshot can be shared with up to 64 organizations. Shared snapshots cannot be used to create custom images. Snapshots shared with other organizations cannot be shared again. Take note of the following items when you share encrypted snapshots: Elastic Compute Service To share a snapshot that is encrypted by using the AES-256 algorithm, you must use a Resource Access Management (RAM) role to authorize the organization with which the encrypted snapshot is shared to use Key Management Service (KMS). For more information, see the Use a RAM role for authorization section of this topic. Encrypted snapshots that use the default key cannot be shared. Snapshots that are encrypted by using the SM4 algorithm cannot be shared. When you use a shared encrypted snapshot to create disks, you must specify a different encryption key for the disks instead of using the encryption key of the snapshot. Shared snapshots cannot be deleted. Before you can delete a shared snapshot, you must unshare the snapshot. For more information, see the Unshare a snapshot section of this topic. After a snapshot is unshared or the source snapshot that is shared is deleted, the organization with which the snapshot is shared cannot re-initialize the data disks that are created from the snapshot.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Disk Snapshots** tab, find the snapshot that you want to share and click **Share**
**Snapshot** in the **Actions** column.
5. In the **Share Snapshot** dialog box, select the level-1 organizations with which you want to
share the snapshot from the **Organization** drop-down list.

**Note**

If you cannot obtain the organization list due to insufficient permissions, you can enter the UIDs of level-1 organizations with which you want to share the snapshot in the Organization field to search for the level-1 organizations.
6. Click **OK**.

**View a shared snapshot**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Snapshots page, click the **Share Snapshot** tab to view the information about the
shared snapshots. On the **Shared by Me** tab, you can view the snapshots that are shared by the current level-1 organization with other level-1 organizations. You can view the following information about each shared snapshot: snapshot ID or name, status, tag, snapshot source, disk capacity, disk ID or name, disk property, progress, and organization or resource set. On the **Shared by Others** tab, you can view the snapshots that are shared by other level-1 organizations with the current level-1 organization. You can view the following information about each shared snapshot: snapshot ID or name, instant access, disk ID or name, disk capacity, encryption status, snapshot source, progress, description, update time, and creation time. Elastic Compute Service
5. In the search box in the upper-left corner of the tab, enter a snapshot name, snapshot ID,
disk ID, creation time, or tag to filter snapshots. If you no longer need to share a snapshot with other level-1 organizations, you can unshare the snapshot.

**Important**

After you unshare a snapshot, the organizations with which the snapshot is shared cannot re-initialize the data disks that are created from the shared snapshot.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Disk Snapshots** tab of the Snapshots page, find the snapshot that you want to
unshare and click **Share Snapshot** in the **Actions** column.

**Note**

You can also find the shared snapshot on the **Shared by Me** tab of the **Share**
**Snapshot** tab and click **Share Snapshot** in the **Actions** column.
5. In the **Share Snapshot** dialog box, find the organization with which you want to unshare
the snapshot and click the icon in the **Actions** column.
6. Click **OK**.

**Use a RAM role for authorization**

To share an encrypted snapshot, you must use a RAM role to authorize the organization with which the encrypted snapshot is shared to use KMS.
1. Create a RAM role. Configure a custom policy of the key to be used by the organization that
shares the snapshot with other organizations and a trust policy for the organization with which the snapshot is shared. RAM role: AliyunECSShareEncryptSnapshotDefaultRole.

**Note**

The RAM role must be named AliyunECSShareEncryptSnapshotDefaultRole. Otherwise, the encrypted snapshot fails to be shared. Custom policy: Elastic Compute Service

```json
{
  "Version": "1",
  "Statement": [
    {
      "Action": "kms:List*",
      "Resource": "acs:kms:<ID of the region to which the key belongs>:<ID of the o
rganization to which the key belongs>:key",
      "Effect": "Allow"
    },
    {
      "Action": [
        "kms:DescribeKey",
        "kms:TagResource",
        "kms:UntagResource",
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey"
```

`],`

```json
      "Resource": "acs:kms:<ID of the region to which the key belongs>:<ID of the o
rganization to which the key belongs>:key/<ID of the KMS encrypted key associated w ith the snapshot>",
      "Effect": "Allow"
    }
```

]

```
}
```

Trust policy:

```json
{
  "Version": "1",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "<ID of the organization with which the snapshot is
shared>@ecs.aliyuncs.com"
```

]

```
      }
    }
```

]

```
}
```

2. Create a RAM role for the source organization.
For more information, see the **Create RAM role-based authorization** section of the
**Enterprise > Permission management > Role permissions > Create a role** topic in
**Apsara Uni-manager Management Console User Guide** .

#### Create a custom image from a

**snapshot**

| Parameter | Description |
|---|---|
| Sharing Scope | Select the scope in which you want to share the custom image. Current Organization and Subordinate Organizations Current Resource Set Current Organization |
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons _ (:). It must start with a letter. |
| Image Description | The description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

Elastic Compute Service You can create a custom image from a snapshot that contains the operating system and data of an Elastic Compute Service (ECS) instance. Then, you can use the custom image to create multiple identical instances.

**Prerequisites**

A system disk snapshot is created. For more information about how to create a system disk snapshot, see Create a snapshot.

**Precautions**

Before you create custom images from snapshots, take note of the following items: Both encrypted and unencrypted snapshots can be used to create custom images. Only system disk snapshots can be used to create custom images. Data disk snapshots cannot be used to create custom images. Custom images that are created from snapshots cannot be used across regions.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find a snapshot whose property is displayed as **System Disk** in the **Disk Type (All)**
column, and then click **Create Custom Image** in the **Actions** column.
6. Configure the parameters described in the following table to create a custom image.
7. Click **OK**.

#### Modify a snapshot

To facilitate the management of disk snapshots, you can modify the name and description of each snapshot.

**Procedure**

1. Log on to the ECS console.
Elastic Compute Service
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Find the snapshot that you want to manage and click **Edit** in the **Actions** column.
6. In the **Edit** dialog box, modify the name and description of the snapshot.
The snapshot name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), hyphens (-), and colons (:). The name cannot start with a special character, auto, or a digit. The description must be 2 to 256 characters in length. It cannot start with `http://` or

```
 https:// .
```

7. Click **OK**.

#### Delete snapshots

You can delete a snapshot that is no longer needed. After the snapshot is deleted, it cannot be recovered.

**Precautions**

To delete snapshots that have been used to create custom images, you must first delete the custom images. For more information, see Delete a custom image.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Disk Snapshots** tab.
5. Use one of the following methods to delete snapshots:
To delete a single snapshot, find the snapshot and click **Delete** in the **Actions** column. To delete one or more snapshots at a time, select the snapshots and click **Delete** below the snapshot list.
6. In the message that appears, click **Delete**.

### Use snapshot-consistent

**groups**

#### Create a snapshot-consistent group

You can create a snapshot-consistent group to simultaneously create snapshots for disks on one or more Elastic Compute Service (ECS) instances in the same region. If a business system involves multiple disks, you can create a snapshot-consistent group to ensure a consistent write order and crash consistency of business system data.

**Use scenarios**

Snapshot-consistent groups are applicable to cluster services in the following scenarios: Elastic Compute Service A business system is deployed on multiple disks attached to an ECS instance, and point-intime consistency and crash consistency are required across databases or enterprise-level applications. For example, a MySQL cluster is built on ECS instances, a single Logical Volume Manager (LVM) logical volume is created across multiple volumes, or Oracle or SAP HANA clusters are migrated to the cloud. Snapshots need to be created simultaneously for multiple nodes of a distributed application system, such as a large-scale website or a multi-application collaborative system. Disks on an ECS instance need to be backed up simultaneously with high point-in-time consistency.

**Prerequisites**

The ECS instances for which you want to create a snapshot-consistent group are in the
**Running** or **Stopped** state.
The disks for which you want to create a snapshot-consistent group are in the **Running** state. A Resource Access Management (RAM) role is attached to the ECS instance, and a custom policy that contains the permissions on application-consistent snapshots is attached to the RAM role. For more information, see Attach an instance RAM role to an ECS instance.

**Note**

When you create application-consistent snapshots, you must invoke Cloud Assistant to access the ECS instance and run commands. Before you invoke Cloud Assistant, grant Cloud Assistant the required permissions by using the RAM role. Configure a custom RAM role, such as AppSnapshotRoleName. Attach a custom policy to the RAM role. The following sample code provides a custom policy, which indicates that the RAM role has the permissions to query snapshots, create snapshots, add tags, and query disk information.

```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecs:DescribeSnapshot*",
                "ecs:CreateSnapshot*",
                "ecs:TagResources",
```

`],`

```json
            "Resource": [
                "*"
```

`],`

```json
            "Condition": {}
        }
```

]

```
}
```

Before you use the snapshot-consistent group feature, take note of the following items:

| Item | Description |
|---|---|
| Impacts | To ensure that services are not affected, we recommend that you create the snapshot-consistent group during off-peak hours. |
| Amount of time required to create a snapshot- consistent group | The amount of time required to create a snapshot-consistent group depends on the total size of the selected disks for which you want to create snapshots. The first snapshot of each disk is a full snapshot and takes longer to create than subsequent snapshots. Subsequent snapshots are incremental snapshots and do not take as long to be created as the first snapshot. The amount of time required varies based on the amount of data changed since the previous snapshot. If you want to use a snapshot immediately after it is created, you can enable the instant access feature. |
| Limits | You can create snapshot-consistent groups only for standard performance disks and premium performance disks. If an instance has disks of other categories attached, you can select only standard performance disks and premium performance disks on the instance to create a snapshot-consistent group. The cloud disks for which you want to create a snapshot-consistent group must reside in the same zone. You cannot specify custom retention periods for snapshots created by using a snapshot-consistent group. By default, the snapshots are retained until you manually delete them. You can create a snapshot-consistent group for multiple ECS instances. Each snapshot-consistent group can contain snapshots of up to 16 cloud disks, including system disks and data disks, and the total size of these disks cannot exceed 128 TiB. Snapshots that you created are retained until they are deleted. We recommend that you delete unnecessary snapshots on a regular basis to prevent the snapshot size from exceeding the limit. For more information, see Delete a snapshot. |

| Parameter | Description |
|---|---|

Elastic Compute Service

**Method 1: Create a snapshot-consistent group based on a**

**single ECS instance**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance that you want to manage. In the **Actions**
column, click the icon and choose **Disk and Image > Create Snapshot-consistent**
**Group**.
5. In the **Create Snapshot-consistent Group** dialog box, configure the parameters that are
described in the following table. Use the default settings for other parameters.

| Disks | The standard performance disks and premium performance disks for which you want to create the snapshot-consistent group. You can select a maximum of 16 disks, including the system disk and data disks. The total size of the selected disks cannot exceed 128 TiB. |
|---|---|
| Group Name | The name of the snapshot-consistent group, which facilitates management. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, periods (.), underscores ( ), hyphens (-), and _ colons (:). |
| Description | The description of the snapshot-consistent group, which facilitates management. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Instant Access | The instant access feature can accelerate the process of snapshot creation. You can use the instant access feature to create snapshots within seconds. Enable Instant Access: You can select this check box to enable the instant access feature. By default, this feature is disabled. Duration of Instant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. Valid values: 1 to 65535. |
| Application-consistent Snapshot | The application-consistent snapshot feature is supported only in Windows 2016, Windows 2019, Windows 2022, Windows 2025, Ubuntu 20.04, Ubuntu 22.04, and Ubuntu 24.04 operating systems. When you enable the application-consistent snapshot feature, the Cloud Assistant plug-in is automatically installed. For Linux instances, you must upload a script to the specified path within the guest operating system before you enable the feature. Otherwise, file system-consistent snapshots are created. |

Elastic Compute Service
6. Click **OK**.
After the snapshot-consistent group is created, a message that contains the Cloud Assistant command ID and the execution ID is displayed. You can check whether applicationconsistent snapshots are created based on the execution ID. After the snapshot-consistent group is created, you can choose **Storage & Snapshots > Snapshots** in the left-side navigation pane and then click the **Snapshot-consistent Groups** tab to view the snapshot-consistent group.

**Method 2: Create a snapshot-consistent group based on**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Snapshots page, click the **Snapshot-consistent Groups** tab. Then, click **Create**
**Snapshot-consistent Group**.

| Parameter | Description |
|---|---|
| Organization | The organization to which the disk belongs. |
| Resource Set | The resource set to which the disk belongs. |
| Data Source | The ECS instance based on which you want to create the snapshot- consistent group. |
| Disks | The standard performance disks and premium performance disks for which you want to create the snapshot-consistent group. You can select a maximum of 16 disks, including the system disk and data disks. The total size of the selected disks cannot exceed 128 TiB. |
| Group Name | The name of the snapshot-consistent group, which facilitates management. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, periods (.), underscores ( ), hyphens (-), and _ colons (:). |
| Description | The description of the snapshot-consistent group, which facilitates management. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Instant Access | The instant access feature can accelerate the process of snapshot creation. You can use the instant access feature to create snapshots within seconds. Enable Instant Access: You can select this check box to enable the instant access feature. By default, this feature is disabled. Duration of Instant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. Valid values: 1 to 65535. |
| Application-consistent Snapshot | The application-consistent snapshot feature is supported only in Windows 2016, Windows 2019, Windows 2022, Windows 2025, Ubuntu 20.04, Ubuntu 22.04, and Ubuntu 24.04 operating systems. When you enable the application-consistent snapshot feature, the Cloud Assistant plug-in is automatically installed. For Linux instances, you must upload a script to the specified path within the guest operating system before you enable the feature. Otherwise, file system-consistent snapshots are created. |

Elastic Compute Service
5. In the **Create Snapshot-consistent Group** dialog box, configure the parameters that are
described in the following table.
6. Click **OK**.
Elastic Compute Service After the snapshot-consistent group is created, a message that contains the Cloud Assistant command ID and the execution ID is displayed. You can check whether applicationconsistent snapshots are created based on the execution ID. After the snapshot-consistent group is created, you can choose **Storage & Snapshots > Snapshots** in the left-side navigation pane and then click the **Snapshot-consistent Groups** tab to view the snapshot-consistent group.

**What to do next**

After a snapshot-consistent group is created, you can perform the following operations: Use the snapshot-consistent group to roll back disks. For more information, see Roll back disks by using a snapshot-consistent group. Access the snapshot-consistent group and create a custom image from a snapshot that belongs to the group. For more information, see Create a custom image from a snapshot.

#### View the details of a snapshot-

**consistent group**

You can view information about a snapshot-consistent group, including the name, ID, status, creation time, snapshot type, and the names, IDs, and categories of the disks that belong to the snapshot-consistent group.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Snapshots page, click the **Snapshot-consistent Groups** tab.
In the snapshot-consistent group list, view information about existing snapshot-consistent groups in the columns, such as **Snapshot-consistent Group ID/Name**, **Tag**,
**Organization/Resource Set**, **Status**, **Snapshot Type**, and **Disk ID/Name**.
You can also perform the following operations to specify the columns to be displayed in the snapshot-consistent group list: i. In the upper-right corner of the snapshot-consistent group list, click the icon. ii. In the **Custom Columns** dialog box, select the columns that you want to display in the snapshot-consistent group list and click **Save**.
5. Select a filter condition, such as **Snapshot-consistent Group ID**, from the drop-down list
and enter relevant information in the search box. The snapshot-consistent groups that meet the specified filter condition are automatically displayed in the snapshot-consistent group list.

| Section | Description |
|---|---|
| Basic Information | Displays the basic information about the snapshot-consistent group, including the name, ID, status, snapshot type, creation time, and description of the snapshot-consistent group. |
| Disk Snapshots | Displays the information about snapshots created in the snapshot- consistent group in the columns, including Disk Snapshot ID/Name, Status, Disk Type/Capacity, Encrypted/Unencrypted, Disk ID/Name, and Instance ID/Name. |

Elastic Compute Service

**Note**

You can search for a snapshot-consistent group by snapshot-consistent group ID, snapshot-consistent group name, or tag. Fuzzy search is supported only if you select **Snapshot-consistent Group**
**Name** as the filter condition.
You can also specify multiple filter conditions to search for the snapshotconsistent groups that you require. On the Snapshot-consistent Groups tab, you can select one or more snapshotconsistent groups and click **Batch Add Tags** or **Batch Remove Tags**.
6. Click the ID of a snapshot-consistent group in the **Snapshot-consistent Group ID/Name**
column. View the details of the snapshot-consistent group in the sections that are described in the following table. View operation logs of the snapshot-consistent group. Click the **Operation Log** tab to view the operation logs of the snapshot consistent group, including the operation name, operator, execution status, operation source (console call or API call), operation type, source IP address of the operation, and operation time. Search for operation logs that you require by specifying filter conditions. Select a filter condition from the drop-down list and enter the corresponding information in the search box to search operation logs. The operation logs that meet the specified filter condition are displayed. Click **Advanced Filter**, specify multiple filter conditions, and then click **Search** to search operation logs. Click **Operation Details** in the Actions column of an operation to view the operation details.

**Note**

#### Roll back disks by using a snapshot-

**consistent group**

Elastic Compute Service After a snapshot-consistent group is created, you can use it to roll back one or more disks in the event of system failures or data errors caused by accidental operations.

**Prerequisites**

Before you use a snapshot-consistent group to roll back disks on an Elastic Compute Service (ECS) instance, make sure that the following requirements are met: A snapshot-consistent group is created based on the disks. For more information, see Create a snapshot-consistent group.

**Important**

The rollback operation cannot be reversed. If data changes were made to the disk from the time the snapshot-consistent group was created until the disk is rolled back, all these data changes are lost. To prevent data loss caused by accidental operations, we recommend that you create a snapshot-consistent group to back up disk data before you roll back disks. The instance to which the disks to be rolled back are attached is in the **Stopped** state. For more information, see Stop an instance. The disks that correspond to the snapshots contained in the snapshot-consistent group have not been released or detached or do not have snapshots being created. The operating system of the instance has not been replaced since the snapshot-consistent group was created. The snapshots of the disks have not been deleted from the snapshot-consistent group. If the snapshot of a disk has been deleted from the snapshot-consistent group, the disk cannot be rolled back by using the snapshot-consistent group. The snapshot-consistent group can be used to roll back only other disks whose snapshots are contained in the group.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
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

#### Delete a snapshot-consistent group

You can delete snapshot-consistent groups that are no longer needed.

**Procedure**

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | The organization to which the automatic snapshot policy applies. |
| Resource Set | Yes | The resource set to which the automatic snapshot policy applies. |

Elastic Compute Service
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Snapshots**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Snapshot-consistent Groups** tab.
5. Find the snapshot-consistent group that you want to delete and click **Delete** in the **Actions**
column.
6. In the message that appears, click **Delete**.

### Use automatic snapshots

#### Create an automatic snapshot policy

Automatic snapshot policies can be applied to system disks and data disks to create snapshots for the disks on a periodic basis. You can use automatic snapshot policies to improve data security and tolerance against accidental operations.

**Background information**

Automatic snapshot policies can effectively eliminate the following risks associated with manual snapshots: When applications such as personal websites or databases deployed on an Elastic Compute Service (ECS) instance encounter attacks or system vulnerabilities, you may be unable to manually create snapshots. In this case, you can use the latest automatic snapshots to roll back the affected disks to restore data and reduce loss. You can also specify an automatic snapshot policy to create snapshots before regular system maintenance tasks are performed. This eliminates the need to manually create snapshots and ensures that snapshots are always created before maintenance. You can retain up to 1,000 automatic snapshots for each disk. If the maximum number of snapshots for a disk has been reached while a new snapshot is being created, the system deletes the oldest automatic snapshot.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Policy**.
5. In the **Create Policy** dialog box, configure the parameters described in the following table.

| Region | Yes | The ID of the region to which the automatic snapshot policy applies. |
|---|---|---|
| Policy Name | Yes | The name of the automatic snapshot policy. The name must be 2 to 128 characters in length and cannot start with a digit or a special character. The name can contain periods (.), underscores ( ), hyphens (-), and colons (:). _ |
| Sharing Scope | Yes | The scope in which you want to share the automatic snapshot policy. Valid values: Current Organization and Subordinate Organizations, Current Resource Set, and Current Organization. |
| Creation Time | Yes | The time of the day at which to create an automatic snapshot. Valid values: 00:00 to 23:00 (the start of each hour). You can select multiple values. Note The default time zone for the snapshot policy is UTC+8. You can change the time zone based on your business requirements. If the time scheduled for creating an automatic snapshot is due while a previous automatic snapshot is being created, the new snapshot creation task is skipped. This may occur when a disk contains a large amount of data. For example, an automatic snapshot policy specifies that automatic snapshots are created at 00:00:00, 01:00:00, and 02:00:00. If a snapshot creation task requires 70 minutes to complete, from 00:00:00 to 01:10:00, the system runs the next snapshot creation task at 02:00:00 instead of 01:00:00. |
| Frequency | Yes | The day of the week on which you want to create automatic snapshots. The valid values range from Monday to Sunday. You can select multiple values. |

Elastic Compute Service

| Retention Period | No | The retention period of automatic snapshots. By default, automatic snapshots are retained for 30 days. Valid values: Custom Period: You can select this option and specify the number of days for which you want to retain the automatic snapshots. Valid values: 1 to 65535. Permanently: You can select this option to retain the automatic snapshots until they are deleted when the maximum number of snapshots is reached. |
|---|---|---|

Elastic Compute Service
6. Click **OK**.

**What to do next**

After the automatic snapshot policy is created, you must apply the policy to disks. For more information, see Apply or cancel an automatic snapshot policy.

#### View automatic snapshot policies

You can view created automatic snapshot policies.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Automatic Snapshot Policies page, view the automatic snapshot policies that you
created. You can view the details of each automatic snapshot policy, such as **Automatic Snapshot**
**Policy ID/Name**, **Tag**, **Details**, **Associated Disks**, **Organization/Resource Set**,
**Sharing Scope**, and **Creation Time**.

**Note**

You can click the number in the **Associated Disks** column corresponding to an automatic snapshot policy to view the disks that are associated with the policy. You can perform the following steps to specify the columns to be displayed in the automatic snapshot policy list: i. In the upper-right corner of the automatic snapshot policy list, click the icon. ii. In the drop-down list, select the columns to be displayed in the automatic snapshot policy list.
5. Select a filter condition, such as **Policy ID**, from the drop-down list and enter relevant
information to search for automatic snapshot policies. The automatic snapshot policies that meet the specified filter condition are automatically displayed. Elastic Compute Service

**Note**

You can search automatic snapshot policies by specifying the **Policy Name**,
**Policy ID**, **Filter by Tag**, or **Creator**filter condition.
You can also specify multiple filter conditions to narrow down the search results.

#### Modify an automatic snapshot policy

After an automatic snapshot policy is created, you can modify properties of the policy based on your business requirements, such as the policy name, creation time, execution frequency, and retention period.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to modify and click **Modify Policy** in the
**Actions** column.
5. In the **Modify Policy** dialog box, modify the original parameter settings of the policy.
For more information about the parameters that you can configure for a policy, see Create an automatic snapshot policy.

**Note**

Changes made to the retention period do not affect the existing snapshots and take effect only on subsequent snapshots.
6. Click **OK**.

#### Apply or cancel an automatic snapshot

**policy**

You can apply automatic snapshot policies to cloud disks. After an automatic snapshot policy is applied to a cloud disk, snapshots are automatically created for the cloud disk based on the policy.

**Background information**

We recommend that you apply automatic snapshot policies to create automatic snapshots during off-peak hours. You can manually create snapshots for cloud disks to which automatic snapshot policies are applied. When an automatic snapshot is being created for a cloud disk, you must wait for the creation task to be completed before you can manually create a snapshot for the cloud disk.

**Apply or cancel an automatic snapshot policy on the Automatic**

**Snapshot Policies page**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, resource group, and region.
Elastic Compute Service
4. Find the automatic snapshot policy that you want to apply or cancel and click **Associated**
**Disks** in the **Actions** column.
5. In the **Associated Disks** dialog box, apply or cancel the automatic snapshot policy based
on your business requirements. If you want to apply the automatic snapshot policy, click the **Disks Without Policy**
**Applied** tab, select the cloud disks to which you want to apply the policy, and then click
**Apply Policy** below the disk list.
If you want to cancel the automatic snapshot policy, click the **Disks with Policy Applied** tab, select the cloud disks from which you want to remove the policy, and then click
**Cancel Policy** below the disk list.
You can also click the icon in the **Status** or **Disk Type** column to filter disks.

**Apply an automatic snapshot policy on the Disks page**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Disks**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the cloud disk that you want to manage and click **Configure Automatic Snapshot**
**Policy** in the **Actions** column.
5. In the **Configure Automatic Snapshot Policy** dialog box, turn on Automatic Snapshot
Policy and select an automatic snapshot policy.
6. Click **OK**.

#### Modify the sharing scope of an

**automatic snapshot policy**

You can modify the sharing scope of an existing automatic snapshot policy.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Automatic Snapshot Policies page, find the automatic snapshot policy that you want
to manage and click **Modify Sharing Scope** in the **Actions** column.
5. In the **Modify Sharing Scope** dialog box, configure the Sharing Scope parameter.
6. Click **OK**.

#### Delete an automatic snapshot policy

You can delete automatic snapshot policies that you no longer need. After you delete an automatic snapshot policy, the policy is automatically canceled for the disks to which the policy is applied.

**Procedure**

1. Log on to the ECS console.
Elastic Compute Service
2. In the navigation pane on the left, choose **Storage & Snapshots > Automatic Snapshot**
**Policies**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to delete and click **Delete Policy** in the
**Actions** column.
5. In the message that appears, click **Delete**.

| ECS 1 | and | ECS 2 |
|---|---|---|

| Security Group 1 |  |
|---|---|
| etworks of | ECS 1 |

| nd | ECS 2 |
|---|---|

| rules of | Security Group 1 |  |
|---|---|---|
| Security Group 1 |  |  |
|  |  | . No out |

Elastic Compute Service

## Security groups

### Security group overview

A security group is a virtual firewall that manages the inbound and outbound traffic of Elastic Compute Service (ECS) instances. You can add ECS instances that have the same security requirements and trust each other to the same security group. This allows you to divide instances into security zones and secure cloud resources. This topic describes the features, types, and best practices of security groups. This topic also describes how to manage the security groups.

**Features**

When you create an ECS instance, you must specify one or more security groups to which the instance is added. The rules of multiple security groups to which an ECS instance belongs are sorted in order. The security group rules are used to allow or reject the inbound or outbound network traffic of the ECS instances. You can add, modify, or delete a security group rule of a security group. The configuration automatically takes effect on all ECS instances that belong to the security group. A security group rule consists of an authorization object, a destination port, a protocol, an action (allow or deny), and a priority value. You can configure inbound rules for a security group to control traffic to ECS instances in the security group and outbound rules to control traffic from the instances. The security group rules in the security groups to which ECS instances belong apply to the primary elastic network interfaces (ENIs) of the instances. You can specify different security groups for ENIs other than the primary ENI that is associated with an ECS instance that resides in a virtual private cloud (VPC). When you configure a security group, take note of the following items: A security group takes effect only on the VPC in which the security group resides. If you create an ECS instance in a VPC, you must specify a vSwitch and a security group that reside in the same VPC for the instance. You can add an ECS instance or ENI to at least one or more security groups. For information about the upper limit of security groups to which you can add an ECS instance and an ENI, see the Security group limits section of the "Limits" topic. that you configure. The inbound and outbound traffic of `ECS 1` and `ECS 2` is managed by the custom security group rules of `Security Group 1` . Based on the inbound security group

| Internet Outbound Inbound (All traffic is allowed b(My adtecfhaeuslt )the inbound rule) VPC vSwitch vSwitch Security Group 1 Inbound Security Group Rule in Security ECS 1 Primary ENI ECS 2 Primary ENI Protocol Authorization Port Action Obj ICMP 0.0.0.0 -1/-1 Allow |  |
|---|---|

| Security Group 1 ECS 1 Primary | ENI | ECS 2 Primary E |
|---|---|---|

| ICMP | Obj 0.0.0.0 | -1/-1 | Allow |
|---|---|---|---|

Elastic Compute Service

**Security group types**

Security groups can be classified into basic and advanced security groups, which are suitable for different scenarios based on the feature. You can use both types of security groups free of charge. When you add an ECS instance to multiple security groups, you can add the ENI that is attached to the instance to security groups only of the same type. We recommend that you select a security group type based on your business requirements.
**Basic security group**: ECS instances in a basic security group can communicate with
each other. You can add security group rules that reference security groups as authorization objects to basic security groups. A basic security group can contain fewer private IP addresses than an advanced security group.
**Advanced security group**: An advanced security group can contain more private IP
addresses than a basic security group. ECS instances in an advanced security group cannot communicate with each other. You cannot create security group rules that reference security groups as authorization objects for advanced security groups.

**Custom security groups and managed security groups**

Security groups are classified into custom security groups and managed security groups based on the operation permission. Both custom security groups and managed security groups can be basic security groups or advanced security groups.
**Custom security group**: You can use your Apsara Stack tenant account to create custom
security groups in the ECS console. You have permissions to perform operations on the custom security groups.
**Managed security group**: A managed security group is a security group that is created to
ensure service availability. Operation permissions on this type of security group is limited for some cloud services, such as Application Load Balancer (ALB). Managed security groups are managed by cloud service systems. You can view managed security groups but cannot perform operations on these security groups. A security group is considered a managed security group if one of the following conditions is met: The value of `ServiceManaged` is `True` in the response when you call the DescribeSecurityGroups API operation to query information about the security group, or you can view but cannot manage the security group in the console.

**Best practices**

This section describes the best practices for using security groups.

**Make a plan**

You can configure the name, description, tags, and resource group of a security group based on your business requirements. We recommend that you configure these parameters to help you identify and manage security groups.

| Operation | Description | References |
|---|---|---|
| Create a security group | You can create a security group. | Create a security group |

Elastic Compute Service

**Use a security group as a whitelist**

By default, all access to a security group is denied. You can add a rule to the security group to allow access from specific authorization objects on specific ports.

**Follow the principle of least privilege when you add security group rules**

For example, if you want to allow connections to be established to port 22 on a Linux instance, we recommend that you add a rule to allow access only from specific IP addresses instead of all IP addresses ( `0.0.0.0/0` ).

**Follow the principle of least privilege**

For example, if you do not require intra-group connectivity between the ECS instances in a security group, change the internal access control policy of the security group from intragroup connectivity to internal isolation.

**Keep the rules in each security group concise**

Add rules to security groups based on the purposes of the security groups, and then add ECS instances to the security groups. Adding a large number of rules to a single security group increases management complexity. You can perform a health check on a security group to identify redundant rules in the security group.

**Add instances that serve different purposes to different security groups and**

**separately maintain the rules for each group**

For example, you can add ECS instances that are accessible over the Internet to the same security group and allow access only on specific ports that provide external services, such as ports 80 and 443. By default, access to other ports is denied. To ensure that the ECS instances that are accessible over the Internet do not provide other services, such as MySQL and Redis, we recommend that you deploy internal services on the instances that are inaccessible over the Internet, and then add the instances to another security group.

**Do not modify security groups that are used in the production environment**

You can clone a security group to the test environment and modify the clone security group. If the ECS instances in the clone security group run as expected after the modifications, modify the rules of the original security group in the production environment. You can perform the following operations to use security groups to control the traffic of instances in the security groups:
1. Create a security group.
2. Add rules to the security group.
3. Add instances to the security group.
4. Manage the security group and security group rules based on your business requirements.

**Common operations**

The following table describes the operations that you can perform in the ECS console to manage security groups.

| Add a security group rule | After you create a security group, you can add or modify security group rules to control inbound or outbound network access. | Create a security group rule |
|---|---|---|
| Add an ECS instance to a security group | You can add an instance to a security group to control network access in a centralized manner. | Add ECS instances to a security group |
| Manage security groups | You can query, modify, and delete security groups as well as remove instances from security groups. | View the details of a security group Modify a security group Clone a security group Remove instances from a security group Create a scheduled task for a security group Delete security groups |
| Manage security group rules | You can modify, clone, export, import, and delete security group rules. | Modify security group rules Clone a security group rule Export security group rules Import security group rules Delete a security group rule |

Elastic Compute Service

### Create a security group

Security groups are an important means to implement network security isolation. Security groups control network traffic to or from one or more Elastic Compute Service (ECS) instances.

**Background information**

Security groups determine whether ECS instances that belong to the same virtual private cloud (VPC), region, and account can communicate with each other. If the ECS instances belong to the same security group, the instances can communicate with each other over the internal network. If the ECS instances belong to different security groups, you can allow mutual access between the security groups to allow the instances to communicate over the internal network.

**Procedure**

| Section | Parameter | Required | Example |
|---|---|---|---|
| Area | Organizatio n/Resource Set | Yes | Select the organization and resource set to which you want to add the security group. Make sure that the security group are in the same organization and resource set as the specified VPC. |
|  | Region | Yes | The region in which you want to create the security group. Make sure that the security group and the specified VPC reside in the same region. |
|  | Sharing Scope | No | The sharing scope of the security group. Valid values: Current Resource Set, Current Organization and Subordinate Organizations, and Current Organization. Note If you want to change the sharing scope of a security group, you can choose > Sharing Settings in the Actions column of the security group. |
|  | Security Group Template | No | The template that you want to apply to the security group you create. Select an existing security group template. For more information, see Create a security group template. |

Elastic Compute Service
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Security Group**.
5. Configure the parameters. The following table describes the parameters.

| Basic Configurati ons |  |  |  |
|---|---|---|---|
|  | Security Group Type | Yes | The type of the security group. Valid values: Basic Security Group: ECS instances in a basic security group can communicate with each other. You can add security group rules that reference security groups as authorization objects to basic security groups. A basic security group can contain fewer private IP addresses than an advanced security group. Advanced Security Group: An advanced security group can contain more private IP addresses than a basic security group. ECS instances in an advanced security group cannot communicate with each other. You cannot create security group rules that reference security groups as authorization objects for advanced security groups. |
|  | VPC | Yes | The VPC in which you want to create the security group. Select an existing VPC or click Create VPC to create a VPC. After you create a VPC, go back to the Create Security Group page and click the icon to refresh the VPC list. For more information about how to create a VPC, see the Create a VPC topic in VPC User Guide. |
|  | Security Group Name | Yes | The name of the security group. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). The name must start with a letter and cannot start with http:// or https:// . |
|  | Description | No | Enter a description for the security group to facilitate management. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), _ commas (,), colons (:), and forward slashes (/). The description must start with a letter and cannot start with http:// or https:// . |
|  | Synchronize | No | This parameter is displayed only after you select Security Group Template. After the synchronization feature is enabled, template rule changes are synchronized to the associated security groups. In this case, you cannot modify the rules in the security groups. For more information, see Add security group rules to a security group template. |

Elastic Compute Service

| Use scenario | Support by basic security groups | Support by advanced security group |
|---|---|---|
| Prefix list + custom port |   |   |
| Prefix list + port group |   |   |

Elastic Compute Service
6. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements. The **Quota** section displays the security group quota in the current region, organization, and resource set. If the quota is insufficient, click **Management** to go to the **Quotas** page and adjust the quota.
7. Create the security group.
If you create a service by setting **Cloud products** to Elastic Compute Service and
**Security Groups** on the Service Management page, confirm the security group
parameters and click **Confirm Order**. If you do not create a service by setting **Cloud products** to Elastic Compute Service and
**Security Groups** on the Service Management page, confirm the security group
parameters and click **Submit**. For more information about service catalog management, see the **Manage services** topic in **Apsara Uni-manager Operations Console User Guide** .

**Verify the result**

After you create a security group, you can view the security group on the **Security Groups** page.

**What to do next**

After the security group is created, it does not contain security group rules. You can add security group rules to the security group to allow or forbid the ECS instances in the security group to communicate with the Internet or internal network. For more information, see Add a security group rule. Each ECS instance must be added to at least one security group. You can add an ECS instance to one or more security groups. For more information, see Add ECS instances to a security group.

### Create a security group rule

You can use security group rules to manage access to and from the Elastic Compute Service (ECS) instances in a security group over the Internet and the internal network.

**Prerequisites**

The public or internal IP addresses for which you want to limit access to ECS instances are obtained.

**Background information**

**Comparison between use scenarios for basic and advanced**

| Authorization object + custom port |   |   |
|---|---|---|
| Authorization object + port group |   |   |
| Authorization security group + port |   |   |

| Protocol | Supported authorization object | Supported port range |
|---|---|---|
| TCP and UDP | IPv4 IPv6 Prefix list Security group | Port Port group |
| ICMP | IPv4 Prefix list (IPv4) Security group | -1/-1 |
| ICMPv6 | IPv6 Security group | -1/-1 |
| GRE and ALL | IPv4 IPv6 Prefix list Security group | -1/-1 |

Elastic Compute Service

**Relationship between different protocol types and allowed IP**

**ranges (CIDR format)**

If a security group has been associated with a security group template, the security group rules are associated with the security group template and synchronously updated. You cannot directly modify the rules in the security group. For more information about how to modify rules, see Create security group rules within a security group template.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.

| Parameter | Require d | Description |
|---|---|---|
| NIC Type | Yes | The network interface controller (NIC) type. The value is fixed to Internal NIC. No public NICs are available to ECS instances that are deployed in virtual private clouds (VPCs). You can create only internal security group rules. However, the created security group rules take effect on traffic that is sent over the Internet and the internal network. |
| Rule Direction | Yes | The rule direction has been selected and cannot be changed here. |
| Action | Yes | Allow: allows requests on a specific port. Deny: drops requests on a specific port without returning responses. If an Allow rule and a Deny rule differ only in the action, theD eny rule takes precedence over the Allow rule. |
| Protocol Type | Yes | The protocol type used to match requests. Valid values: All: applies to scenarios in which all requests are sent from trusted sources. TCP: allows or denies traffic on one or more consecutive ports. UDP: allows or denies traffic on one or more consecutive ports. ICMP: uses the ping command to test the network connectivity between instances. ICMPv6: uses the ping6 command to test the network connectivity between instances. GRE: applies to VPN services. |
| Priority | Yes | The priority of the security group rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |

Elastic Compute Service
4. On the Security Group tab, find the security group to which you want to add a rule and click
**Manage Rules** in the **Actions** column.
5. Click the **Inbound** or **Outbound** tab, and then click **Create Rule**.
**Outbound**: controls access from the ECS instances in the current security group to other
ECS instances in the internal network or to resources on the Internet.
**Inbound**: controls access from other ECS instances in the internal network or from
resources on the Internet to ECS instances in the current security group.
6. In the **Create Rule** dialog box, configure the parameters described in the following table.

| Allowed IP range (CIDR format) | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. Prefix List: prefix lists. Security Group: security groups. This authorization object type takes effect only on the internal network. You can select a different security group within your account as the authorization object to allow or deny mutual access over the internal network between ECS instances in the selected security group and ECS instances in the current security group. |
|---|---|---|
| Authorizatio n Object | Yes | Authorization objects vary based on the Allowed IP range (CIDR format) parameter that you set. If you set the Authorization Type parameter to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate the authorization objects with commas (,). The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter 0.0.0.0/0 , access to or from all IPv4 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter up to one authorization object. The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter ::/0 , access to or from all IPv6 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to Security Group, select a security group ID from the drop-down list. The specified security group must reside in the same VPC as the current security group. |
| Prefix List Aggregation Template | Optional | If you set the Allowed IP range (CIDR format) parameter to Prefix List, you can directly select an existing parameter template. For more information, see Create a parameter template. |

Elastic Compute Service

| Port Authorizatio n Type | Yes | The destination port used to match requests. Valid values: Custom Port and Port Group. |
|---|---|---|
| Port Range | Yes | If you select Custom Port for the Port Authorization Type parameter, the Port Range parameter is affected by the Protocol Type parameter. If you set the Protocol Type parameter to All, a value of -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to TCP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to UDP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to ICMP, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to ICMPv6, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to GRE, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. |
| Port Aggregation Template | Optional | If you select Port Group for the Port Authorization Type parameter, you must select a template for the Port Aggregation Template parameter. For more information, see Create a parameter template. |

Elastic Compute Service

| Description | No | The description of the security group rule. We recommend that you provide an informative description to simplify rule management. The description must be 1 to 512 characters in length, and cannot start with http:// or https://. Note The description of the security group rule. You can specify a date in the format of year-month-day, for example, 2025-10-24, at the beginning of the description as the validity period of the security group rule. You cannot specify multiple dates. The Security Compliance Analytics module of the Data Analysis service automatically checks the validity period of a security group rule. If the validity period expires, we recommend that you clear the corresponding security group rule. For more information, see the Security compliance analysis topic in Apsara Uni-manager User Guide. After you create a security group rule, you can find the rule and click Modify Description in the Actions column to change the description of the rule. |
|---|---|---|

Elastic Compute Service
7. Click **OK**.

### Add ECS instances to a

**security group**

You can add existing Elastic Compute Service (ECS) instances to a security group in the same region. After the instances are added to the security group, the rules of the security group automatically apply to the instances.

**Background information**

Security groups are an important means for security isolation. A security group can control network access to or from one or more ECS instances in the security group. Each ECS instance must be added to at least one security group and can be added to up to five security groups. Elastic Compute Service

**Note**

For more information about how to add an ECS instance to multiple security groups, see Add an instance to a security group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Group tab of the Security Groups page, find the security group to which you
want to add ECS instances. In the **Actions** column, choose
**> Manage Instances**.
The **Instances** tab is displayed. On the Instances tab, you can view the information about ECS instances in the security group in the columns, including **Instance ID/Name**, **Region**,
**IP Address**, and **Network Type**.
You can select a filter condition, such as **Instance ID**, from the drop-down list and enter relevant information in the search box. The instances that meet the specified filter condition are displayed in the instance list.

**Note**

You can specify multiple filter conditions to narrow down the search results.
5. Click **Add Instance**.
6. In the Add Instance dialog box, select the ECS instances that you want to add to the
security group from the instance list and click **OK**.

**Important**

After the ECS instances are added to the security group, the rules of the security group automatically apply to the instances. You can select a filter condition, such as **Instance Name**, **Instance ID**, **IP Address**, or
**Filter by Tag**, from the drop-down list and enter relevant information to search for ECS
instances. The ECS instances that meet the specified filter condition are automatically displayed in the instance list.

**Note**

You can also go to the **ECS Instances** page, find the ECS instance that you want to add to a security group, click in the **Actions** column, and then choose **Network and**
**Security Group > Add to Security Group** to add the instance to a security group.

### View ENIs in a security group

This topic describes how to view the elastic network interfaces (ENIs) that belong to a security group.

**Procedure**

Elastic Compute Service
1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Group tab, find the security group that you want to view, move the pointer
over the icon in the **Actions** column, and then select **Manage ENIs**.
5. On the **Security ENIs** tab, you can view information about the ENIs that belong to the
security group in the columns, such as **ENI ID/Name**, **Tag**, **Organization/Resource Set**, and **Zone**. Select a filter condition, such as **ENI ID**, from the drop-down list and enter a valid value in the search box. The ENIs that meet the specified filter condition are displayed in the ENI list.

**Note**

You can select multiple filter conditions to narrow down the search results.

### Manage security groups

#### View the details of a security group

This topic describes how to search for security groups in a region by using different methods and view the details of a security group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Group tab, view information about existing security groups.
You can view the security group information in the security group list, such as **Security**
**Group ID/Name**, **VPC**, **Associated Instance**, **Security Group Type**, and
**Organization/Resource Set**.
You can perform the following steps to specify the columns to be displayed in the security group list: i. In the upper-right corner of the security group list, click the icon. ii. In the **Custom Columns** dialog box, select the columns to be displayed and click **Save**.
5. Select a filter condition, such as **Security Group ID**, from the drop-down list and enter a
valid value in the search box. The security groups that meet the specified filter condition are displayed in the security group list.

| Tab | Operation |
|---|---|
| Instances | Click the Instances tab to view the instances that are added to the security group. On the Instances tab, select one or more instances that you want to remove from the security group and click Remove from Security Group in the lower-left corner. |
| Rules | Click the Rules tab to view the rules that are created for the security group. Note In the search box above the rule list, you can select Authorization Object, Port, or Display Mode to filter rules. If you select Display Mode, you need to select Not Merge, Merge by Authorization Object, or Merge by Port to filter rules. You can create inbound or outbound security group rules and import or export security group rules. You can choose More > Add 5-tuple Rule to add 5-tuple rules to the security group. For more information, see Security group 5-tuple rules. You can choose More > Redundant Rule Check to check whether the security group contains redundant rules. If Rule A has a lower priority than Rule B and Rule B includes all conditions of Rule A, Rule A is considered to be a redundant rule. If a redundant rule exists, delete the rule to prevent the number of rules from reaching the upper limit. |
| Secondary ENIs | Click the Secondary ENIs tab to view the secondary elastic network interfaces (ENIs) that are bound to the security group. You can also click buttons or select options in the Actions column to modify and delete ENIs, manage secondary private IP addresses, and unbind ENIs from the security group. |
| Scheduled Task | Create a scheduled task for a security group to dynamically add Elastic Compute Service (ECS) instances to or remove ECS instances from the security group at the specified effective time or expiration time. For more information, see Create a scheduled task for a security group. |

Elastic Compute Service

**Note**

You can search for a security group by specifying the **Security Group ID**,
**Security Group Name**, **VPC ID**, or **Filter by Tag** filter condition.
Fuzzy search is supported only if you select **Security Group ID** or **Security**
**Group Name** as the filter condition.
You can select multiple filter conditions to narrow down the search results.
6. Click the ID of a security group in the **Security Group ID/Name** column. The Security
Group Details page appears. You can view the information or perform operations on the following tabs.

| Operation Log | Click the Operation Log tab to view the operation logs of the security group, including the operation name, operator, execution status, operation source (console operation or API call), operation type, source IP address of the operation, and operation time. Search for operation logs that you require by specifying filter conditions. Select a filter condition from the drop-down list and enter the corresponding information in the search box to search operation logs. The operation logs that meet the specified filter condition are displayed. Click Advanced Filter, specify multiple filter conditions, and then click Search to search operation logs. Click Operation Details in the Actions column of an operation to view the operation details. Note Operation logs can be retained for seven days. You can contact the administrator to change the retention period of operation logs on the Log Storage Settings page. To go to this page, choose Configurations > Log Storage Settings. For more information, see the Log storage settings topic in Apsara Uni-manager Management Console User Guide. If the retention period of operation logs on the Log Storage Settings page is extended, historical operation logs that are not retained before the retention period is extended are not backfilled. |
|---|---|

Elastic Compute Service

#### Modify a security group

You can modify the name and description of an existing security group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Group tab of the Security Groups page, find the security group that you
want to modify and click **Modify** in the **Actions** column.
5. In the **Modify Security Group** dialog box, modify the name and description of the security
group. The new name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, underscores (_), hyphens (-), and colons (:). It cannot start with http:// or https://. The new description must be 2 to 256 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores (_), hyphens (-), colons (:), commas (,), and forward slashes (/). It cannot start with http:// or https://.
6. Click **OK**.

#### Clone a security group

You can clone security groups to quickly create identical security groups.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Destination Region | Organization | Yes | Select an organization for the clone security group. Make sure that the clone security group and the specified virtual private cloud (VPC) belong to the same organization. |
|  | Resource Set | Yes | Select a resource set for the clone security group. Make sure that the clone security group and the specified VPC belong to the same resource set. |
|  | Region | Yes | Select a region for the clone security group. Make sure that the clone security group and the specified VPC reside in the same region. |
|  | Security Group Name | Yes | The name of the security group. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), hyphens _ (-), and colons (:). The name must start with a letter and cannot start with http:// or https:// . |
|  | Security Group Type | Yes | Select the type of the clone security group. Valid values: Basic Security Group and Advanced Security Group. |
|  | VPC ID | Yes | Select an existing VPC or click Create VPC to create a VPC. After you create a VPC, you can go back to the Create Security Group page and click the icon to update the VPC list. For more information about how to create a VPC, see the Create a VPC topic in VPC User Guide. |

Elastic Compute Service A security group that is associated with a security group template cannot be cloned.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group that you want to clone. In the **Actions** column, choose

**>**

**Clone**.
5. In the **Clone Security Group** dialog box, configure parameters for the clone security
group. The following table describes the parameters.

| Destination Security Group Settings |  |  |  |
|---|---|---|---|
|  | Sharing Scope | No | Select a sharing scope for the clone security group. Valid values: Current Resource Set, Current Organization and Subordinate Organizations, and Current Organization. Note If you want to change the sharing scope of a security group, choose > Sharing Settings in the Actions column. |
|  | Description | No | Enter a description for the security group to facilitate management. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ periods (.), commas (,), and colons (:). The description must start with a letter and cannot start with http:// or https:// . |
| Import All Rules |  | No | Specify whether to import all rules from the original security group to the clone security group. Note Rule priorities that are higher than 100 are changed to 100. |
| Tags |  | No | Select existing tag keys or tag values or create tag keys or tag values. |

Elastic Compute Service
6. Click **OK**.
After a security group is cloned, you can view the clone security group on the **Security**
**Groups** page.

#### Remove instances from a security

**group**

You can remove Elastic Compute Service (ECS) instances from a security group based on your business requirements. Make sure that the instances belong to one or more other security groups after being removed.

**Prerequisites**

The instances that you want to remove belong to two or more security groups.

**Background information**

Elastic Compute Service After an instance is removed from a security group, the instance is isolated from the other instances in the security group. We recommend that you perform all tests in advance to ensure that services can continue to run as expected after you remove the instance from the security group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Group tab of the Security Groups page, find the security group from which
you want to remove instances, move the pointer over the icon in the **Actions** column, and then select **Manage Instances**.
5. On the Instances tab, select one or more instances that you want to remove and click
**Remove from Security Group** in the lower-left corner.
6. In the message that appears, click **Remove from Security Group**.

**Note**

You can also remove an ECS instance from a security group on the **ECS Instances** page by performing the following operations: i. Find the instance that you want to remove and click **Manage** in the **Actions** column. ii. On the Instance Details page, click the **Security Groups** tab. iii. On the Security Groups tab, select the security groups from which you want to remove the instance. In the lower part of the security group list, click **Remove from**
**Security Group**.

#### Create a scheduled task for a security

**group**

You can create a scheduled task for a security group to dynamically add Elastic Compute Service (ECS) instances to the security group at the specified effective time and remove ECS instances from the security group at the specified expiration time. If a scheduled task is created for an instance and a security group, and the scheduled task is in the **Pending**, **Successful**, or **Failed** state, you must delete the scheduled task before you can create another scheduled task for the instance and security group. Each instance must belong to at least one security group. If a security group is the only security group to which an instance belongs, you cannot remove the instance from the security group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.

| Paramete r | Require d | Description |
|---|---|---|
| Task Name | Yes | The name of the scheduled task. |
| Description | No | The description of the scheduled task. |
| Effective Time | Yes | The point in time at which the scheduled task takes effect. The system adds the selected ECS instances to the security group at this point in time. |
| Expiration Time | Yes | The point in time at which the scheduled task expires. The system removes the selected ECS instances from the security group at this point in time. Note The add and remove operations are separately performed on the ECS instances. Even if the add operation fails, the remove operation still proceeds. |
| RAM Role | Yes | The Resource Access Management (RAM) role that CloudOps Orchestration Service (OOS) assumes. The following policy must be attached to the RAM role: { "Statement": [ { "Action": [ "ecs:DescribeInstances", "ecs:JoinSecurityGroup", "ecs:LeaveSecurityGroup", "ecs:DescribeInstances" ], "Effect": "Allow", "Resource": "*" } ], "Version": "1" } |

Elastic Compute Service
4. On the Security Group tab of the Security Groups page, find the security group for which
you want to create a scheduled task, and click its ID in the **Security Group ID/Name** column.
5. On the Security Group Details page, click the **Scheduled Task** tab, and then click **Create**
**Scheduled Task**.
6. In the **Create Scheduled Task** dialog box, configure the parameters that are described in
the following table.

| Select Instances | Yes | The ECS instances involved in the scheduled task. |
|---|---|---|

Elastic Compute Service
7. Click **OK**.

**What to do next**

You can modify or delete the scheduled task based on your business requirements. In the scheduled task list, find the scheduled task and click **Modify** in the Actions column to modify the name, description, effective time, and expiration time of the scheduled task. In the scheduled task list, find the scheduled task and click **Delete** in the Actions column to delete the scheduled task. After the scheduled task is deleted, the scheduled task expires.

#### Delete a security group

You can delete security groups that are no longer needed. When a security group is deleted, its rules are also deleted.

**Prerequisites**

The security group that you want to delete does not contain Elastic Compute Service (ECS) instances. If the security group contains ECS instances, you must remove the instances from the security group. For more information, see Remove instances from a security group. The security group is not referenced by rules of other security groups. If the security group is referenced by rules of other security groups, you must delete those rules as prompted. For more information, see Delete a security group rule.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete a security group:
To delete a single security group, find the security group and click **Delete** in the **Actions** column. To delete one or more security groups at a time, select the security groups and click
**Delete** in the lower-left corner of the Security Groups page.
5. In the message that appears, click **Delete**.

### Manage security group rules

#### Security group 5-tuple rules

This topic describes the definition and applicable scenarios of security group 5-tuple rules, and how to add security group 5-tuple rules.

**Definition**

A 5-tuple rule contains the following elements: source IP address, source port, destination IP address, destination port, and protocol.

| Field in the conso le | Field in the 5- tuple rule | Role in the traffic | Security group rule template | How it works |
|---|---|---|---|---|
| Sourc e | Source IP address | The IP address of the client that initiates the connection. |  Prefix lists supported | Prefix lists manage CIDR sets and specify the allowed CIDR blocks, such as CIDR blocks of office networks and jump servers. |

Elastic Compute Service 5-tuple rules are fully compatible with existing security group rules. 5-tuple rules provide finer-grained control over the preceding five elements. Sample 5-tuple outbound rule:

```
Source IP address: 172.16.1.0/32 Source port: 22 Destination IP address: 10.0.0.1/32 Destination port: not specified Protocol: TCP Action: Drop
```

The sample outbound rule indicates that TCP access requests from `172.16.1.0/32` to `10.0.0.1/32` over port 22 are rejected.

**Scenarios**

Some platforms use solutions from third-party vendors to provide network services. To prevent unauthorized access from these platforms to Elastic Compute Service (ECS) instances, 5-tuple rules are required to implement finer control over inbound and outbound traffic. If ECS instances in a security group are configured to be isolated from each other and you want to allow specific ECS instances to communicate with each other, you must configure 5-tuple rules.
**IP stacks**: In the same 5-tuple rule, the source and destination IP addresses must be of the
same IP stack (IPv4 or IPv6 prefix list).
**The source and destination IP addresses must be different** : The authorization
objects of the source and destination must be different.
**Import**: You cannot import 5-tuple rules.
**Limits on security group templates:** You cannot configure 5-tuple parameters in the
security group rule templates.

**Usage notes on prefix lists and port groups**

**Inbound rules**

Inbound rules control inbound traffic from external devices to ECS instances.

| User Guide |  |  |  |  |
|---|---|---|---|---|
|  | Source port | The port of the client that initiates the connection. |  ️Port groups not supported | Port lists manage ports. The source port is a temporary port, such as 32768 to 65535, that is allocated by the client operating system. The source port is randomly allocated and cannot be limited by the port list. |
| Destin ation | Destinati on IP address | The CIDR block of the destination (instance). |  ️Prefix lists not supported | Security groups are associated with instances or elastic network interfaces (ENIs), but security group rules limit the applied scope. We recommend that you use security groups in cross-instance authorization within the same VPC. |
|  | Destinati on port | The listener port on the instance, such as port 22, 80, or 443. |  Port groups supported | The destination port is the service port (SSH, HTTP, or HTTPS) exposed by the instance. It is predictable and suitable for batch configuration by using a port list. |

| Field in the conso le | Field in the 5- tuple rule | Role in the traffic | Security group parameter template | How it works |
|---|---|---|---|---|
| Source | Source IP address | The private IP address of the instance. |  ️Prefix lists not supported | The outbound source IP address is the IP address of the network interface controller (NIC) used by the instance. The rule applies to a specified scope and does not need to be matched by prefix list. |
|  | Source port | The temporary port that the instance uses to initiate the connection. |  ️Port groups not supported | The source port is dynamically allocated by the instance operating system, such as port 32768 to port 65535. The source ports is randomly allocated for each connection, and cannot be limited by the port list. |
|  | Destinati on IP address | The IP address of the destination server to be accessed by the instance. |  Prefix lists supported | The destination is a fixed service CIDR block, such as a database cluster, an NTP server, an API gateway, or a software source image site, which can be managed in batches by a prefix list. |

**Outbound rules**

Outbound rules control outbound traffic from ECS instances to external devices.

| lastic Com |  |  |  |  |
|---|---|---|---|---|
| Destin ation |  |  |  |  |
|  | Destinati on port | The service port listened on the destination server. |  Port groups supported | The destination port is the standard port used by the destination service, such as port 3306 for MySQL, port 6379 for Redis, and port 443 for HTTPS. The destination port is predictable and rarely changes. It is suitable for batch configurations of port groups. |

| Parameter | Require d | Description |
|---|---|---|
| NIC Type | Yes | The NIC type. The value is fixed to Internal NIC. No public NICs are available to ECS instances that are deployed in virtual private clouds (VPCs). You can create only internal security group rules. However, the created security group rules take effect on traffic that is sent over the Internet and the internal network. |
| Rule Direction | Yes | The rule direction has been selected and cannot be changed. |
| Action | Yes | Allow: allows access requests on a specific port. Deny: drops requests on a specific port without returning responses. If two security group rules use the same settings except for the action, the Deny action prevails over the Allow action. |

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Group tab, find the security group to which you want to add a rule and click
**Manage Rules** in the **Actions** column.
5. Click the **Inbound** or **Outbound** tab, and then choose **More > Add 5-tuple Rule**.
**Outbound**: An outbound rule controls access from the ECS instances in the security
group to other ECS instances in the internal network or to resources on the Internet.
**Inbound**: An inbound rule controls access from other ECS instances in the internal
network or from resources on the Internet to ECS instances in the security group.
6. In the **Create Rule** dialog box, configure the parameters. The following table describes the
parameters.
**Inbound rule**:

| Protocol Type | Yes | The protocol used to match requests. Valid values: All: applies to scenarios in which all requests are sent from trusted sources. TCP: allows or denies traffic on one or several consecutive ports. UDP: allows or denies traffic on one or several successive ports. ICMP: uses the ping command to test the network connectivity between instances. ICMPv6: uses the ping6 command to test the network connectivity between instances. GRE: applies to VPN services. |
|---|---|---|
| Priority | Yes | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Allowed IP range (CIDR format) | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. Prefix List: prefix lists. Security Group: security groups. This authorization object type takes effect only on the internal network. You can select a different security group in your account as the authorization object to allow or deny mutual access over the internal network between ECS instances in the selected security group and ECS instances in the current security group. |

Elastic Compute Service

| Authorizatio n Object | Yes | Authorization objects vary based on the Allowed IP range (CIDR format) parameter that you set. If you set the Allowed IP range (CIDR format) parameter to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate the authorization objects with commas (,). The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter 0.0.0.0/0 , access to or from all IPv4 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter only one authorization object. The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter ::/0 , access to or from all IPv6 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to Security Group, select a security group ID from the drop-down list. The specified security group must reside in the same VPC as the current security group. |
|---|---|---|
| Prefix List Aggregation Template | No | If you set the Allowed IP range (CIDR format) parameter to Prefix List, you can directly select an existing parameter template. For more information, see Create a parameter template. |
| Port Authorizatio n Type | Yes | The destination port used to match requests. Only Custom Port is supported. |

Elastic Compute Service

| Port Range | Yes | The port range varies based on the protocol. If you set the Protocol Type parameter to All, a value of -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to TCP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to UDP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to ICMP, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to ICMPv6, the value -1/- 1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to GRE, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. |
|---|---|---|
| Allowed IP range (CIDR format) | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. |

Elastic Compute Service

| Authorizatio n Object | Yes | Authorization objects vary based on the Allowed IP range (CIDR format) parameter that you set. If you set the Allowed IP range (CIDR format) parameter to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate the authorization objects with commas (,). The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter 0.0.0.0/0 , access to or from all IPv4 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter up to one authorization object. The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter ::/0 , access to or from all IPv6 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. |
|---|---|---|
| Port Authorizatio n Type | Yes | The destination port used to match requests. Valid values: Custom Port and Port Group. |
| Port Range | Yes | If you set Port Authorization Type to Custom Port, you must specify a custom port range. Valid values: 1 to 65535. The port range must be in the <start port>/<end port> format. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. |
| Port Aggregation Template | No | If you select Port Group for the Port Authorization Type parameter, you must select a template for the Port Aggregation Template parameter. For more information, see Create a parameter template. |

Elastic Compute Service

| Description | No | The description of the security group rule. To facilitate future management operations, we recommend that you provide an informative description. The description must be 1 to 512 characters in length and cannot start with http:// or https://. Note You can specify a date in the format of year-month- day, for example, 2025-10-24, at the beginning of the description as the validity period of the security group rule. You cannot specify multiple dates. The Security Compliance Analytics module of the Data Analysis service automatically checks the validity period of a security group rule. If the validity period expires, we recommend that you clear the corresponding security group rule. For more information, see the Security compliance analysis topic in Apsara Uni-manager User Guide. After you create a security group rule, you can find the rule and click Modify Description in the Actions column to change the description of the rule. |
|---|---|---|

| Parameter | Require d | Description |
|---|---|---|
| NIC Type | Yes | The NIC type. The value is fixed to Internal NIC. No public NICs are available to ECS instances that are deployed in VPCs. You can create only internal security group rules. However, the created security group rules take effect on traffic that is sent over the Internet and the internal network. |
| Rule Direction | Yes | The rule direction has been selected and cannot be changed. |
| Action | Yes | Allow: allows access requests on a specific port. Deny: drops requests on a specific port without returning responses. If two security group rules use the same settings except for the action, the Deny action prevails over the Allow action. |

Elastic Compute Service
**Outbound rule**:

| Protocol Type | Yes | The protocol used to match requests. Valid values: All: applies to scenarios in which all requests are sent from trusted sources. TCP: allows or denies traffic on one or several successive ports. UDP: allows or denies traffic on one or several successive ports. ICMP: uses the ping command to test the network connectivity between instances. ICMPv6: uses the ping6 command to test the network connectivity between instances. GRE: applies to VPN services. |
|---|---|---|
| Priority | Yes | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Allowed IP range (CIDR format) | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. |

Elastic Compute Service

| Authorizatio n Object | Yes | Authorization objects vary based on the authorization object type. If you set the Allowed IP range (CIDR format) parameter to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate the authorization objects with commas (,). The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter 0.0.0.0/0 , access to or from all IPv4 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter up to one authorization object. The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter ::/0 , access to or from all IPv6 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. |
|---|---|---|
| Port Authorizatio n Type | Yes | The destination port used to match requests. Only Custom Port is supported. |

Elastic Compute Service

| Port Range | Yes | The port range varies based on the protocol. If you set the Protocol Type parameter to All, a value of -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to TCP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to UDP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to ICMP, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to ICMPv6, the value -1/- 1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to GRE, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. |
|---|---|---|
| Allowed IP range (CIDR format) | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. Prefix List: prefix lists. Security Group: security groups. This authorization object type takes effect only on the internal network. You can select a different security group within your account as the authorization object to allow or deny mutual access over the internal network between ECS instances in the selected security group and ECS instances in the current security group. |

Elastic Compute Service

| Authorizatio n Object | Yes | Authorization objects vary based on the Allowed IP range (CIDR format) parameter that you set. If you set the Allowed IP range (CIDR format) parameter to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate the authorization objects with commas (,). The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter 0.0.0.0/0 , access to or from all IPv4 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter up to one authorization object. The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter ::/0 , access to or from all IPv6 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to Security Group, select a security group ID. The specified security group must reside in the same VPC as the current security group. |
|---|---|---|
| Prefix List Aggregation Template | No | If you set the Prefix List Aggregation Template parameter to Prefix list, you must select a prefix list aggregation template. |
| Port Authorizatio n Type | Yes | The destination port used to match requests. Valid values: Custom Port and Port Group. |
| Port Range | Yes | If you set the Port Authorization Type parameter to Custom Port, you must specify a custom port range. Valid values: 1 to 65535. The port range must be in the <start port>/<end port> format. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. |

Elastic Compute Service

| Description | No | The description of the security group rule. To facilitate future management operations, we recommend that you provide an informative description. The description must be 1 to 512 characters in length and cannot start with http:// or https://. Note You can specify a date in the format of year-month- day, for example, 2025-10-24, at the beginning of the description as the validity period of the security group rule. You cannot specify multiple dates. The Security Compliance Analytics module of the Data Analysis service automatically checks the validity period of a security group rule. If the validity period expires, we recommend that you clear the corresponding security group rule. For more information, see the Security compliance analysis topic in Apsara Uni-manager User Guide. After you create a security group rule, you can find the rule and click Modify Description in the Actions column to change the description of the rule. |
|---|---|---|

Elastic Compute Service
7. Click **OK**.

#### Modify security group rules

This topic describes how to modify security group rules. Improper configurations of security group rules can result in serious security risks. You can modify improper rules in a security group to ensure the network security of Elastic Compute Service (ECS) instances within the security group.

**Prerequisites**

A security group is created and security group rules are added. For more information, see Create a security group and Create a security group rule. For a security group that has been associated with a security group template, security group rules are associated with the security group template and synchronously updated. You cannot directly modify the rules in the security group. For more information about how to modify rules, see Create security group rules within a security group template.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the Security Group tab, find the security group for which you want to modify security
group rules and click **Manage Rules** in the **Actions** column.
5. On the Rules tab, click the **Inbound** or **Outbound** tab.
6. Find the security group rule that you want to modify and click **Modify Properties** in the
**Actions** column.
7. In the **Modify Properties** dialog box, modify the properties of the rule.
Elastic Compute Service For more information about the properties of security group rules, see Create a security group rule.
8. Click **OK**.

#### Clone a security group rule

You can clone a security group rule to quickly create a similar rule.

**Background information**

You may need to clone a security group rule in the following scenarios: Assume that you have created Security Group Rule A to control TCP access and that you want to create Security Group Rule B to control UDP access. You can create Rule B by cloning Rule A and changing the protocol type to UDP. Assume that you have created Security Group Rule C to control TCP access over port 22 and that you want to create Security Group Rule D to control TCP access over port 3389. You can create Rule D by cloning Rule C and changing the port range to 3389/3389. Rules of a security group that is associated with a security group template cannot be cloned.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the Security Group tab, find the security group from which you want to clone a security
group rule and click **Manage Rules** in the **Actions** column.
5. On the Rules tab, click the **Inbound** or **Outbound** tab.
6. Find the rule that you want to clone and click **Clone** in the **Actions** column.
7. In the **Clone Rule** dialog box, modify the properties of the rule.
For more information about the properties of security group rules, see Create a security group rule.
8. Click **OK**.
After the rule is cloned, a new rule is displayed in the rule list.

#### Export security group rules

You can export security group rules as Excel files to your computer for on-premises backup. Rules of a security group that is associated with a security group template cannot be exported.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Export security group rules.

| Allowed IP range (CIDR format) | Port Authorization Type |
|---|---|
| IPv4 CIDR Block | Custom Port |
|  | Port Group |
| IPv6 CIDR Block | Custom Port |
|  | Port Group |
| Prefix List | Custom Port |
|  | Port Group |

Elastic Compute Service

**Export the rules of multiple security groups at a time**

Select the security groups whose rules you want to export and click **Batch Export** below the list. An Excel file that contains all **inbound** and **outbound** rules of the selected security groups is automatically downloaded to your on-premises computer.

**Export the rules of a single security group**

i. Find the security group whose rules you want to export. Click **Manage Rules** in the
**Actions** column.
ii. On the Rules tab, click the **Inbound** or **Outbound** tab. iii. Click **Export**. An Excel file that contains the **inbound** rules or **outbound** rules of the security group is automatically downloaded to your on-premises computer.

#### Import security group rules

Security group rules can be imported to security groups. You can import a backup file of security group rules from your computer to a security group to create or restore security group rules.

**Background information**

You can download a template file (XLS file), configure security group rules in the file based on the template requirements, and then import the file. The rules in the template must contain parameters described in the following table: Security group rules cannot be imported to a security group that has been associated with a security group template.

**Procedure**

1. Log on to the ECS console.
Elastic Compute Service
2. In the navigation pane on the left, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the security group to which you want to import rules. Click **Manage Rules** in the
**Actions** column.
5. On the **Rules** tab, click **Import**.
6. In the **Import Security Group Rule** dialog box, click the
icon.
7. Select a backup file of security group rules from your computer and click **OK** to upload the
file.

**Note**

The Import is a non-overwrite import. The new rules imported will not override the existing rules.

#### Delete a security group rule

If you do not need a security group rule that controls access to Elastic Compute Service (ECS) instances or from ECS instances, you can delete the rule. For a security group that has been associated with a security group template, security group rules are associated with the security group template and synchronously updated. You cannot delete the rules in the security group. For more information about how to delete rules in the security group, see Manage security group templates.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Security Groups**.
3. In the top navigation bar, select an organization, resource group, and region.
4. On the Security Group tab, find the security group from which you want to delete a rule and
click **Manage Rules** in the **Actions** column.
5. On the Rules tab, click the **Inbound** or **Outbound** tab.
6. Use one of the following methods to delete a security group rule:
To delete a single rule, find the rule and click **Delete** in the **Actions** column. To delete one or more rules at a time, select the rules and click **Delete** in the lower-left corner of the tab.
7. In the message that appears, click **Delete**.

### Security group templates

#### Create a security group template

| Section | Parameter | Requir ed | Description |
|---|---|---|---|
| Region | Organization /Resource Set | Yes | The resource set in which you want to add the security group template. |
|  | Region | Yes | The region to which the security group template belongs. |
| Basic Configuratio ns | Sharing Scope | Yes | The sharing scope of the security group template. |
|  | Security Group Template Name | Yes | The name of the security group template. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and colons (:). The name must start with a letter and cannot start with http:// or https:// . |

Elastic Compute Service You can create a security group template without the need to associate it with a virtual private cloud (VPC). You can also configure CIDR blocks and port ranges for the security group template based on your business requirements. The use of a security group template effectively removes the tight coupling between security group rules and CIDR blocks or port ranges. This allows you to flexibly configure security rules and improve O&M efficiency.

**Prerequisites**

The permissions to use security group templates are obtained. By default, the administrator manages security group templates. If other roles want to use a security group template, contact the administrator to grant permissions. For more information, see the **Role**
**permissions** topic in **Apsara Uni-manager User Guide**.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Security Group Template** tab, and then click
**Create Security Group Template** .
5. In the **Create Security Group****Template** dialog box, configure the parameters that are
described in the following table.

|  | Description | No | Enter a description for the security group template to facilitate management. The description must be 2 to 50 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), commas (,), colons (:), _ and forward slashes (/). The description must start with a letter and cannot start with http:// or https:// . |
|---|---|---|---|

| Parameter | Require d | Description |
|---|---|---|
| NIC Type | Yes | The network interface controller (NIC) type. The value is fixed to Internal NIC. No public NICs are available to ECS instances that are deployed in virtual private clouds (VPCs). You can create only internal security group rules. However, the created security group rules take effect on traffic that is sent over the Internet and the internal network. |

Elastic Compute Service
6. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements. Then, click **Submit**. After you create a security group template, you can view the security group template in the security group template list.

**What to do next**

After you create a security group template, you can use the template when you create a security group, and add security group rules to the template based on your business requirements. For more information, see Create a security group and Add security group rules to a security group template.

#### Create security group rules within a

**security group template**

When you use a security group template, you can create security group rules within the template based on your business requirements. However, whether the security group rules you create are synchronized to the security group depends on whether the synchronization feature is enabled when the security group template is applied.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Security Group Template** tab.
5. Find the security group template within which you want to create a rule and click **Details** in
the **Actions** column.
6. On the **Rules** tab, click the **Inbound** or **Outbound** tab, and then click **Create Rule**.
7. In the **Create Rule** dialog box, configure the parameters described in the following table.

| Rule Direction | Yes | The rule direction has been selected and cannot be changed here. |
|---|---|---|
| Action | Yes | Allow: allows requests on a specific port. Deny: drops requests on a specific port without returning responses. If an Allow rule and a Deny rule differ only in the action, theD eny rule takes precedence over the Allow rule. |
| Protocol Type | Yes | The protocol type used to match requests. Valid values: All: applies to scenarios in which all requests are sent from trusted sources. TCP: allows or denies traffic on one or more consecutive ports. UDP: allows or denies traffic on one or more consecutive ports. ICMP: uses the ping command to test the network connectivity between instances. ICMPv6: uses the ping6 command to test the network connectivity between instances. GRE: applies to VPN services. |
| Priority | Yes | The priority of the security group rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Allowed IP range (CIDR format) | Yes | IPv4 CIDR Block: IPv4 addresses or CIDR blocks. IPv6 CIDR Block: IPv6 addresses or CIDR blocks. Prefix List: prefix lists. Security Group: security groups. This authorization object type takes effect only on the internal network. You can select a different security group within your account as the authorization object to allow or deny mutual access over the internal network between ECS instances in the selected security group and ECS instances in the current security group. |

Elastic Compute Service

| Authorizatio n Object | Yes | Authorization objects vary based on the Allowed IP range (CIDR format) parameter that you set. If you set the Authorization Type parameter to IPv4 CIDR Block, the following rules apply: You can enter a single IPv4 address or a CIDR block. Example: 192.0.2.1 or 192.0.2.0/24 . You can enter up to 10 authorization objects. Separate the authorization objects with commas (,). The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter 0.0.0.0/0 , access to or from all IPv4 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to IPv6 CIDR Block, the following rules apply: You can enter a single IPv6 address or a CIDR block. Example: 2001:db8:1:1:1:1:1:1 or 2001:db8::/32 . You can enter up to one authorization object. The specified authorization object may conflict with the IP address of an ECS instance. For centralized management and accurate security group association, we recommend that you add this authorization object to a prefix list within a parameter template. If you enter ::/0 , access to or from all IPv6 addresses is allowed or denied based on the value of the Action parameter. Proceed with caution. If you set the Allowed IP range (CIDR format) parameter to Security Group, select a security group ID from the drop-down list. The specified security group must reside in the same VPC as the current security group. |
|---|---|---|
| Prefix List Aggregation Template | Optional | If you set the Allowed IP range (CIDR format) parameter to Prefix List, you can directly select an existing parameter template. For more information, see Create a parameter template. |
| Port Authorizatio n Type | Yes | The destination port used to match requests. Valid values: Custom Port and Port Group. |

Elastic Compute Service

| Port Range | Yes | If you select Custom Port for the Port Authorization Type parameter, the Port Range parameter is affected by the Protocol Type parameter. If you set the Protocol Type parameter to All, a value of -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to TCP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to UDP, you can specify a port range. The port range must be in the <start port>/<end port> format. Valid values of port numbers: 1 to 65535. For example, 80/80 indicates port 80 and 1/22 indicates ports 1 to 22. If you set the Protocol Type parameter to ICMP, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to ICMPv6, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. If you set the Protocol Type parameter to GRE, the value -1/-1 is displayed, which indicates all ports. In this case, you cannot specify a port range. |
|---|---|---|
| Port Aggregation Template | Optional | If you select Port Group for the Port Authorization Type parameter, you must select a template for the Port Aggregation Template parameter. For more information, see Create a parameter template. |
| Description | No | The description of the security group rule. We recommend that you provide an informative description to simplify rule management. The description must be 1 to 512 characters in length, and cannot start with http:// or https://. Note The description of the security group rule. You can specify a date in the format of year-month-day, for example, 2025-10-24, at the beginning of the description as the validity period of the security group rule. You cannot specify multiple dates. The Security Compliance Analytics module of the Data Analysis service automatically checks the validity period of a security group rule. If the validity period expires, we recommend that you clear the corresponding security group rule. For more information, see the Security compliance analysis topic in Apsara Uni-manager User Guide. After you create a security group rule, you can find the rule and click Modify Description in the Actions column to change the description of the rule. |

Elastic Compute Service

#### Manage security group templates

Elastic Compute Service You can modify security group rules within a security group template, modify the sharing scope of the template, or delete the template based on your business requirements.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Security Group Template** tab. In the search box,
search for a security group template that you want to manage by **ID/Name**, **Tag**, and
**Creator** of the security group template.
5. Manage the security group template.
View details of the security group template. Click **Details** in the **Actions** column. On the page that appears, you can view the security group rules and associated security groups of the security group template. You can also create or delete security group rules within the security group template based on your business requirements. Modifies the name or description of the security group template. Click **Modify** in the **Actions** column. In the dialog box that appears, modify the name or description. Modifies the sharing settings of the security group template. Click **Sharing Settings** in the **Actions** column. In the dialog box that appears, modify the sharing scope. Delete the security group template. Click **Delete** in the **Actions** column. In the message that appears, click **Delete**.

#### Delete a security group template

When a security group template is no longer needed, you can delete it to facilitate O&M. A security group template that is associated with a security group cannot be deleted. Delete the security group before you can delete the security group template. For more information, see Delete a security group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Security Group Template** tab.
5. Find the security group template that you want to delete and click **Delete** in the **Actions**
column.
6. In the message that appears, click **Delete**.

### Manage parameter templates

#### Create a parameter template

| Section | Parameter | Requir ed | Description |
|---|---|---|---|
| Destination Instance Configuratio ns | Organization | Yes | The organization to which the parameter template belongs. |
|  | Resource Set | Yes | The resource set to which the parameter template belongs. |
|  | Region | Yes | The ID of the region to which the parameter template belongs. |
|  | Name | Yes | The name of the parameter template. The name must be 2 to 128 characters in length. The name can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). The _ name must start with a letter and cannot start with http:// or https://. |
|  | Description | No | Enter a description for the parameter template to facilitate management. The description must be 2 to 50 characters in length. It cannot start with http:// or https:// . |

Elastic Compute Service A parameter template is a set of network prefixes (CIDR blocks) or ports. You can reference existing CIDR blocks or ports as a set when you configure a security group rule. This eliminates the duplicate rules that are configured for different CIDR blocks or ports and improves O&M efficiency.

**Prerequisites**

By default, the administrator manages security group parameter templates. If other roles want to use a security group parameter template, contact the administrator to grant permissions. For more information, see the **Role permissions** topic in **Apsara Uni-**
**manager User Guide**.
You can use an Alibaba Cloud account to create a maximum of 1,000 parameter templates that contain prefix lists and 1,000 parameter templates that contain port groups in a region.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Parameter Template** tab, and then click **Create**
**Parameter Template**.
5. In the **Create Parameter Template** dialog box, configure the parameters that are
described in the following table.

| Parameter Configuratio ns | Configuratio n Type | No | The configuration type. Valid values: Prefix List and Port Group. |
|---|---|---|---|
|  | Authorizatio n Object Type | No | The type of the authorization object. This parameter is required only if you set the Configuration Type parameter to Prefix List. IPv4 and IPv6 are supported. |
|  | Max Entries | Yes | The maximum number of entries in the prefix list or port group. After you create a prefix list or port group, you cannot change the maximum number of entries in the prefix list or port group. Valid values: 1 to 200. You can also click Import Configurations to import a prefix list or port group. Note The rule quotas of resources, such as security groups, that are associated with a prefix list are calculated based on the maximum number of entries in the prefix list, instead of the actual number of entries. Set the Max Entries parameter to a proper value. |
|  | Configure IP Address | Yes | The IP addresses to be configured. This parameter is required only if you set the Configuration Type parameter to Prefix List. Add CIDR blocks as entries to the prefix list. You can click Add to add a CIDR block and enter a description for the CIDR block. Repeat this operation to add multiple CIDR blocks. Note You can specify only IPv4 CIDR blocks in the entries of the prefix list. |
|  | Configure Port | Yes | The ports to be configured. This parameter is required only if you set the Configuration Type parameter to Port Group. Add ports as entries in the port group. You can click Add to add a port and enter a description for the port. Repeat this operation to add multiple ports. |

Elastic Compute Service
6. Click **OK**.
After a parameter template is created, you can view the parameter template in the parameter template list.

#### View a parameter template

| Filter condition | Description |
|---|---|
| Template ID | The ID of a parameter template. Fuzzy search is supported. |
| Template name | The name of a parameter template. Fuzzy search is supported. |

Elastic Compute Service The topic describes how to search for a parameter template by specifying different filter conditions and view the details of the parameter template.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Parameter Template** tab.
Select a filter condition from the drop-down list and enter relevant information in the field. The parameter templates that meet the specified filter condition are automatically displayed.
5. In the search results, find the parameter template that you want to view and click **Details**
in the **Actions** column to view the details of the parameter template and the security groups with which the parameter template is associated.

#### Modify a parameter template

This topic describes how to modify the properties of an existing parameter template, including the name, description, and configured IP addresses.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Parameter Template** tab.
5. On the Parameter Template tab, find the parameter template that you want to modify and
click **Edit** in the **Actions** column.
6. In the **Edit Parameter Template** dialog box, modify the following parameters and click
**OK**.
**Name**: the name of the parameter template. The name must be 2 to 128 characters in
length. The name can contain letters, digits, periods (.), underscores (_), hyphens (-), and colons (:). The name must start with a letter and cannot start with http:// or https://.
**Description**: the description of the parameter template, which facilitates the
management of the parameter template. The description must be 2 to 50 characters in length. It cannot start with `http://` or `https://` .
**Configure IP Address**: the IP addresses to be configured. This parameter is required
only if you set the Configuration Type parameter to **Prefix List**. Add CIDR blocks as entries to the prefix list. You can click **Add** to add a CIDR block and enter a description for the CIDR block. Repeat this operation to add multiple CIDR blocks. Elastic Compute Service
**Configure Port**: the ports to be configured. This parameter is required only if you set
the Configuration Type parameter to **Port Group**. Add ports as entries in the port group. You can click **Add** to add a port and enter a description for the port. Repeat this operation to add multiple ports.

**Note**

You can also click Import Configurations below **Max Entries** to import a prefix list or port group. However, the template to be imported must be of the same type as the existing parameter template, and the total number of entries after import cannot be greater than the max entries.

#### Modify the sharing scope of a

**parameter template**

This topic describes how to modify the sharing scope of an existing parameter template. If you narrow down the sharing scope of a parameter template, accounts outside the new scope cannot be used to manage the parameter template. Proceed with caution.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Parameter Template** tab.
5. Find the parameter template that you want to modify and click **Sharing Settings** in the
**Actions** column.
6. In the **Sharing Settings** dialog box, configure the Sharing Scope parameter. Valid values
of the Sharing Scope parameter include Current Organization and Subordinate Organizations, Current Resource Set, and Current Organization.

#### Delete a parameter template

If a parameter template has been idled for a long period of time or the parameter template is replaced with another one, you need to delete the parameter template to facilitate O&M management. A parameter template that is associated with a security group or a security group template cannot be deleted. Remove the association before you delete the parameter template.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > Security Groups**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, click the **Parameter Template** tab.
5. Delete one or more parameter templates.
Elastic Compute Service To delete a single parameter template, find the parameter template that you want to delete and click **Delete** in the **Actions** column. To delete multiple parameter templates at a time, select the parameter templates that you want to delete and click **Delete** in the lower part of the Parameter Template tab.
6. In the message that appears, click **Delete**.

| Attribute | Description |
|---|---|
| ENI type | ENIs are classified into primary and secondary ENIs. Primary ENIs: Primary ENIs are created together with ECS instances. The lifecycle of a primary ENI is the same as the lifecycle of the ECS instance to which the primary ENI is bound. You cannot unbind primary ENIs from ECS instances. Secondary ENIs: Secondary ENIs can be separately created. You can bind a secondary ENI to or unbind a secondary ENI from an ECS instance. |
| VPC | Only ECS instances that reside in VPCs support ENIs. An ENI and the ECS instance to which the ENI is bound must reside in the same VPC. |
| Organization | An ENI and the ECS instance to which the ENI is bound must belong to the same organization. |
| Resource set | An ENI and the ECS instance to which the ENI is bound must belong to the same resource set. |
| Regions | An ENI and the ECS instance to which the ENI is bound must reside in the same region. |
| Zone | The vSwitch to which the ENI is connected and the ECS instance to which the ENI is bound must reside in the same zone. |
| Security group | An ENI must be added to at least one security group. The security group controls the inbound and outbound traffic of the ENI. |
| Elastic IP address (EIP) | An ENI can be associated with one or more EIPs. |

aces Elastic Compute Service

## Elastic Network Interfaces

### Overview

An elastic network interface (ENI) is a virtual network interface controller (NIC) that can be bound to an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). You can bind one or more ENIs to each ECS instance. You can bind secondary ENIs to or unbind secondary ENIs from different ECS instances to allow for more flexibility and scalability in network configurations and meet network requirements in different scenarios. For example, you can use ENIs to create multi-IP address, multi-NIC, or high-availability networks. An ENI is a virtual network interface that must be bound to an ECS instance in a VPC before the ENI can be used. The following table describes the attributes of an ENI.

| Primary private IP address | The primary private IP address of an ENI is an IP address specified by the user or assigned by the system during ENI creation. The primary private IP address must be an idle IP address within the CIDR block of the vSwitch to which the ENI is connected. |
|---|---|
| Secondary private IPv4 address | A secondary private IPv4 address of an ENI must be an idle IPv4 address within the IPv4 CIDR block of the vSwitch to which the ENI is connected. You can assign secondary private IPv4 addresses to or unassign secondary private IPv4 addresses from an ENI. |
| Secondary private IPv6 address | A secondary private IPv6 address of an ENI must be an idle IPv6 address within the IPv6 CIDR block of the vSwitch to which the ENI is connected. You can assign secondary private IPv6 addresses to or unassign secondary private IPv6 addresses from an ENI. |
| MAC address | A MAC address is the globally unique identifier of an ENI. |

Elastic Compute Service aces An ENI is an independent virtual NIC that can be moved between ECS instances to allow flexible business scaling and migration. You can create ENIs together with ECS instances, or separately create secondary ENIs and bind the ENIs to existing ECS instances. You can create ENIs differently based on your business requirements.

**Note**

You can assign multiple secondary private IP addresses to each ENI based on the instance type of the ECS instance to which the ENI is bound to allow flexible business scaling. Configuration of multiple private IP addresses for a single ECS instance You can assign multiple secondary private IP addresses to an ENI that is bound to an ECS instance. If multiple applications are hosted on the ECS instance, you can assign multiple secondary private IP addresses to an ENI on the instance to provide each application with an independent IP address. This way, the utilization of the ECS instance is improved. Configuration of multiple public IP addresses for a single ECS instance You can assign only a single public IP address to an ECS instance that has no ENIs bound. You can associate EIPs with an ENI on an ECS instance to allow the instance to have multiple public IP addresses. In NAT mode, you can associate each private IP address of an ENI with an independent EIP. You can move a secondary ENI from one ECS instance to another ECS instance to redirect network traffic to the other instance. ENIs are hot-swappable and can be freely moved between ECS instances without the need to restart the instances. The movement of ENIs does not affect the business that runs on the ECS instances. When you unbind a secondary ENI from an ECS instance and bind the ENI to another ECS instance, the attributes of the ENI remain unchanged and network traffic is redirected to the other instance.

| Operation | Description |
|---|---|

aces Elastic Compute Service The following limits apply to ENIs: You can assign only a single primary private IP address to each ENI. You can assign one or more secondary private IP addresses to each ENI. The number of secondary private IP addresses varies based on the instance type of the ECS instance to which the ENI is bound. You can associate each ENI with one or more EIPs. The number of EIPs varies based on the manner in which you associate the EIPs with the ENI. For more information, see **VPCs**
**and vSwitches > VPC management > Create a VPC** and **VPCs and vSwitches >**
**vSwitch management > Create a vSwitch** in Apsara Stack VPC User Guide.
Each ENI must be added to at least one security group and can be added to up to five security groups. You can create a limited number of ENIs per region in an account. The quota is displayed in the **Quota Overview** section on the Overview page of the Apsara Uni-manager Management Console. The following limits apply when you bind ENIs to ECS instances:

**Important**

Take note that the network bandwidth capabilities of an ECS instance vary based on the instance type. You cannot increase the network bandwidth of an ECS instance by binding multiple secondary ENIs to the instance. An ENI and the ECS instance to which the ENI is bound must reside in the same zone and VPC, but can be connected to different vSwitches and added to different security groups. The number of secondary ENIs that can be bound to an ECS instance varies based on the instance type.

**Use scenarios**

ENIs are suitable for the following scenarios: Deployment of high-availability clusters To implement a high-availability architecture, you can bind multiple ENIs to a single ECS instance. Low-cost failover You can unbind an ENI from a faulty ECS instance and then bind the ENI to another ECS instance to redirect traffic destined for the faulty ECS instance to the other ECS instance and immediately recover services. Fine-grained network management You can configure multiple ENIs on an ECS instance. For example, you can use specific ENIs for internal management and other ENIs for Internet business access to isolate management data from business data. You can also configure security group rules for each ENI based on different elements, such as source IP addresses, protocols, and ports, to achieve find-grained access control.

**Manage ENIs**

You can perform operations on ENIs based on your business requirements. The following table describes the operations that you can perform on ENIs.

| Create an ENI | You can bind ENIs to ECS instances to create high-availability clusters and implement fine-grained network management. You can also unbind an ENI from an ECS instance and bind the ENI to another ECS instance to perform low-cost failover. |
|---|---|
| Bind a secondary ENI to an ECS instance | You can bind a secondary ENI to an existing ECS instance. After the ENI is bound, the traffic on the ENI is redirected to the instance. |
| Configure a secondary ENI | After you bind secondary ENIs to ECS instances, specific images used by the instances may be unable to recognize the IP addresses of the ENIs or add routes for the ENIs. In this case, the ENIs cannot work as expected. You must configure the secondary ENIs within the ECS instances to allow the images to recognize the IP addresses of the ENIs and add routes for the ENIs. |
| View ENIs | You can view the information of existing ENIs. |
| Modify a secondary ENI | You can modify the attributes of a secondary ENI, including the ENI name and the security groups to which the ENI is added. |
| Unbind a secondary ENI from an instance | You can unbind a secondary ENI from an ECS instance. After the secondary ENI is unbound from the ECS instance, the instance no longer processes the traffic on the ENI. |
| Delete a secondary ENI | If you no longer need a secondary ENI, you can delete the ENI. |

Elastic Compute Service aces

### Create an ENI

You can associate elastic network interfaces (ENIs) with Elastic Compute Service (ECS) instances to create high-availability clusters and implement fine-grained network management. You can also disassociate an ENI from an ECS instance and then associate the ENI with a different ECS instance to perform low-cost failover.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For more information, see **Create a**
**VPC** and **Create a vSwitch** in the **VPC User Guide**.
A security group is available in the VPC. If no security group is available in the VPC, create a security group. For more information, see Create a security group.

**Background information**

You can use one of the following methods to create an ENI. This topic describes how to separately create an ENI. A primary ENI is created by default when an ECS instance is created in a VPC. The lifecycle of the primary ENI is the same as the lifecycle of the ECS instance and the primary ENI cannot be disassociated from the ECS instance.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization/Res ource Set | Yes | The resource set in which you want to create the ENI. |
|  | Region/Zone | Yes | The region and zone in which you want to create the ENI. |
|  | VPC | Yes | The VPC in which you want to create the ENI. You can associate the secondary ENI only with an ECS instance in the same VPC. Select the VPC in which the ECS instance resides. You can also click Create VPC to create a VPC. Note After you create an ENI, you cannot change the VPC in which the ENI resides. |
|  | vSwitch | Yes | The vSwitch with which the ENI is associated. You can associate the secondary ENI only with an ECS instance that resides in the same zone as the VPC. Select a vSwitch that resides in the same zone as the ECS instance. The ECS instance and the ENI can be associated with different vSwitches. You can also click Create vSwitch to create a vSwitch. Note After you create an ENI, you cannot change the vSwitch with which the ENI is associated. |

aces Elastic Compute Service ENIs that are separately created are secondary ENIs. You can associate secondary ENIs with or disassociate them from ECS instances.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Click **Create ENI**.
5. Configure the parameters. The following table describes the parameters.

|  | Security Group | Yes | The security group in which you want to create the ENI in the specified VPC. The rules of the security group automatically apply to the ENI. You can also click Create Security Group to create a security group. |
|---|---|---|---|
|  | ENI Name | Yes | The name of the ENI. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https:// . The name can contain letters, digits, colons (:), underscores ( ), and hyphens (-). _ |
|  | Description | No | The description of the ENI. We recommend that you specify a description that can help you identify the ENI. The description must be 2 to 256 characters in length. The description must start with a letter and cannot start with http:// or https:// . The description can contain letters, digits, colons (:), periods (.), commas (,), underscores ( ), and hyphens (-). _ |
| Basic Configurations |  |  |  |
|  | Primary Internal IP Address | No | The primary private IPv4 address of the ENI. The primary private IPv4 address must be within the CIDR block of the specified vSwitch. If you do not specify a primary private IP address, the system automatically assigns a primary private IPv4 address to the ENI. |
|  | Secondary Private IPv4 Address | No | The secondary private IPv4 addresses of the ENI. Valid values: Do Not Allocate: No secondary private IPv4 addresses are assigned to the ENI. Auto Allocate: Enter an integer in the range of 1 to 9 as the number of secondary private IPv4 addresses that you want to assign to the ENI. The system automatically assigns the specified number of idle IPv4 addresses from within the CIDR block of the selected vSwitch to the ENI. Specify IP Address: Manually assign secondary private IPv4 addresses to the ENI. You can specify up to nine secondary private IPv4 addresses. |

Elastic Compute Service aces

|  | Secondary Private IPv6 Addresses | No | The secondary private IPv6 addresses of the ENI. Valid values: Do Not Allocate: No secondary private IPv6 addresses are assigned to the ENI. Auto Allocate: Enter an integer in the range of 1 to 10 as the number of secondary private IPv6 addresses that you want to assign to the ENI. The system automatically assigns the specified number of idle IPv6 addresses from the CIDR block of the selected vSwitch to the ENI. Specify IP Address: Manually assign secondary private IPv6 addresses to the ENI. You can specify up to 10 secondary private IPv6 addresses. Note To assign IPv6 addresses to the ENI, you must select a vSwitch that supports IPv6 addresses. |
|---|---|---|---|

aces Elastic Compute Service
6. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements. The **Quota** section displays the ENI quota in the current region, organization, and resource set. If the quota is insufficient, click **Management** to go to the **Quotas** page and adjust the quota.
7. Create the ENI.
If the service whose **Cloud resources** value is **Elastic Network Interfaces** exists on the Service Management page, confirm the ENI parameters and click **Confirm Order**. If the service whose **Cloud resources** value is **Elastic Network Interfaces** does not exist on the Service Management page, confirm the ENI parameters and click **Submit**. For more information about service catalog management, see the **Manage service**
**catalogs** topic in **Apsara Uni-manager Operations Console User Guide** .

**Verify the result**

After you create the ENI, **Available** is displayed in the Status column of the ENI in the ENI list.

**What to do next**

After you separately create an ENI, you can associate the ENI with an ECS instance. For more information, see Bind a secondary ENI to an instance.

### Bind a secondary ENI to an

**instance**

Elastic Compute Service aces You can bind a secondary elastic network interface (ENI) to an instance. After the ENI is bound, the traffic on the ENI is directed to the instance.

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
2. In the navigation pane on the left, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the secondary ENI that you want to bind and click **Bind to Instance** in the **Actions**
column.
5. In the **Bind to Instance** dialog box, select an instance and click **OK**.
If the ENI is bound to the instance, **Bound** is displayed in the **Status** column corresponding to the ENI.

### Configure a secondary ENI

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| MAC address | 00:16:3e:0f:**:** |
| Primary private IP address | 192.168.**.*2 |
| Subnet mask | 255.255.255.0 |
| Gateway address | 192.168.**.253 |

aces Elastic Compute Service After secondary elastic network interfaces (ENIs) are bound to Elastic Compute Service (ECS) instances, some images used by these instances may not recognize the IP addresses of these ENIs or configure routes for the ENIs. If this occurs, the secondary ENIs cannot be used on the instances. This topic describes how to configure secondary ENIs from within instances to have their IP addresses recognizable and how to configure routes for the secondary ENIs.

**Prerequisites**

A secondary ENI is bound to an ECS instance. For information about how to bind a secondary ENI to an ECS instance, see Bind a secondary ENI to an instance. You are connected to the ECS instance. For information about how to connect to an ECS instance, see Overview.

**Background information**

If automatic configuration tools are pre-installed on the images that are used by instances, secondary ENIs that are bound to the instances can be automatically configured by the tools. You can use these secondary ENIs without the need to manually configure them. Skip the topic if your instance uses an image of one of the following versions: Alibaba Cloud Linux 3.2104 64-bit CentOS 8.0 64-bit, CentOS 8.1 64-bit, and CentOS 8.2 64-bit CentOS 7.3 64-bit, CentOS 7.4 64-bit, and CentOS 7.5 64-bit CentOS 6.8 64-bit and CentOS 6.9 64-bit Debian 10.5 64-bit and Debian 10.6 64-bit Windows Server 2008 R2 and later

**Procedure**

1. Check whether the IP addresses of a secondary ENI bound to an instance are recognized.
For more information, see Check whether the IP addresses of ENIs are recognized. If yes, skip the following steps. If not, proceed with the following steps to configure the secondary ENI.
2. Obtain the information of the secondary ENI.
When you configure a secondary ENI, you may need to specify its information, such as the primary private IP address and media access control (MAC) address. Obtain the information required for subsequent configurations. For more information, see Obtain the information of an ENI. In the examples provided in this topic, the sample values listed in the following table are used. In actual scenarios, replace them with the attribute values of your secondary ENI.
3. Configure the secondary ENI to have its IP address recognized.
The operations required to configure secondary ENIs vary based on the operating systems of the instances to which the secondary ENIs are bound.

| Operating system | References |
|---|---|
| Alibaba Cloud Linux 2 (Instances that run this operating system use the network-scripts network service) CentOS | Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service |
| Alibaba Cloud Linux 2 (Instances that run this operating system use the systemd-networkd network service) | Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2 operating system and uses the systemd-networkd network service |
| Ubuntu Debian | Configure a secondary ENI for an instance that runs a Ubuntu or Debian operating system |
| SUSE openSUSE | Configure a secondary ENI for an instance that runs a SUSE or openSUSE operating system |

Elastic Compute Service aces
4. Check whether routes are configured for the secondary ENI.
You can run the `route -n` command to check route information. If no routes are configured for the secondary ENI or if the existing routes do not meet your requirements, manually configure routes for the secondary ENI. The following sections provide examples on how to configure routes for a secondary ENI that is bound to an instance that runs one of the following operating systems: Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system Configure routes for a secondary ENI of an instance that runs a CentOS 8 operating

**Check whether the IP addresses of ENIs are recognized**

Run the following command to check whether the IP addresses of ENIs are recognized:

```
ip address show
```

Sample command outputs: The following command output shows that the IP address of the eth0 primary ENI is recognized but the IP address of the eth1 secondary ENI is not recognized. You can perform operations described in this topic to configure the secondary ENI. The following command output shows that the IP addresses of both the eth0 primary ENI and the eth1 secondary ENI are recognized. You do not need to configure the secondary ENI. aces Elastic Compute Service

**Note**

In the preceding command outputs, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI.

**Obtain the information of an ENI**

You can obtain the information of an ENI from instance metadata, by using the ECS console, or by calling an API operation. Obtain the information of an ENI from instance metadata. Obtain the MAC addresses of the ENIs that are bound to an instance.

```bash
curl http://100.100.100.200/latest/meta-data/network/interfaces/macs/
```

**Note**

The MAC addresses of ENIs are required to obtain their primary private IP addresses, subnet masks, and gateway addresses. Obtain the primary private IP address of the specified ENI.

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

The following figure shows sample command outputs. In the command outputs, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI.

**Note**

After you run the `ip address show` command, you can determine which is the primary ENI and which is the secondary ENI based on the order in which the MAC addresses are displayed in the command output. Elastic Compute Service aces Obtain the information of an ENI by using the ECS console. i. Log on to the ECS console. ii. In the left-side navigation pane, choose **Network & Security > ENIs**. iii. On the **ENI** page, find the ENI whose information you want to query and view its primary private IP address and MAC address in the Private IP Address and ENI Type/MAC Address columns. The following figure shows an example of the ENI page in the ECS console. Obtain the information of an ENI by using an Alibaba Cloud SDK to call the DescribeNetworkInterfaces operation.

```
aliyun ecs DescribeNetworkInterfaces \ --output cols=MacAddress,PrivateIpAddress rows=NetworkInterfaceSets.NetworkInterfaceSet[] \ --RegionId 'cn-qingdao-****-d01' \ --InstanceId 'i-bp1a5gj0bzhwz7q****'
```

The following figure shows the sample response. In the response, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI.

**Note**

After you run the `ip address show` command, you can determine which is the primary ENI and which is the secondary ENI based on the order in which the MAC addresses are displayed in the command output.

**Configure a secondary ENI for an instance that runs an Alibaba**

**Cloud Linux 2, CentOS 6, or CentOS 7 operating system and**

**uses the network-scripts network service**

If your instance runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service, you can use the multi-nic-util tool to have the ENIs of the instance automatically configured or you can manually configure the ENIs by modifying their configuration files. Use the multi-nic-util tool to have a secondary ENI automatically configured. aces Elastic Compute Service

**Note**

If you want to use the multi-nic-util tool to have secondary ENIs automatically configured for CentOS instances, note that the multi-nic-util tool is supported only on some versions of CentOS images. If your instance uses a CentOS 6 image, make sure that the image version is CentOS 6.8 or later. If your instance uses a CentOS 7 image, make sure that the image version is CentOS 7.3 or later. If the multinic-util tool is not supported on the image version that your instance uses, manually configure secondary ENIs by modifying their configuration files. i. Download and install the multi-nic-util tool.

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

For CentOS 7 or later and Alibaba Cloud Linux 2, run the following command:

```bash
systemctl restart network
```

Elastic Compute Service aces

**Note**

After you configure the secondary ENI, you can configure routes for the ENI. For more information, see Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system. If you want to create custom images from the instance whose ENIs are configured, you must first run the **/etc/eni_utils/eni-cleanup** command to remove network configurations from /etc/udev/rules.d/70-persistent-net.rules and /etc/sysconfig/network-scripts/.

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

**Note**

In the preceding example, `192.168.**.*2` is the primary private IP address and the `/24` subnet mask is `255.255.255.0` .
3. Restart the network service.

```bash
systemctl restart systemd-networkd
```

aces Elastic Compute Service

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

**Note**

The eth0 primary ENI is configured in the same configuration file as the eth1 secondary ENI. You must also add the information of the primary ENI to the configuration file. iii. Restart the network service. For versions earlier than Ubuntu 16.04, such as Ubuntu 14.04, run the following command:

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

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. Elastic Compute Service aces

**Note**

When you modify the configuration file, take note of the following items: The configuration file is in the `YAML` format. You must follow the `YAML` syntax rules when you configure the file. Tabs cannot be used for indentation in `YAML` files. Use spaces instead. We recommend that you copy information from the default /etc/netplan/99netcfg.yaml configuration file to prevent format issues. The following section provides an example of the ENI information to add to the configuration file:

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

If you manually configure secondary ENIs but do not configure routes for them or if routes configured by the multi-nic-util tool do not meet your requirements, perform the following steps to configure routes.

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| Primary private IP address | 192.168.**.*2 |
| Gateway address | 192.168.**.253 |
| metric | 1001 |

aces Elastic Compute Service
1. View route information.

```
route -n
```

Sample command outputs: The following command output shows only the route information of the eth0 primary ENI, which indicates that no routes are configured for the eth1 secondary ENI. The following command output shows the route information of both the eth0 primary ENI and the eth1 secondary ENI. If the configured routes do not meet your requirements, you can modify the routes.
2. Plan the default route based on your requirements.
In this example, the sample values listed in the following table are used.
3. Configure the default route.
You can run the following commands to add the default route for the eth1 secondary ENI, create a route table, and then attach a routing policy to the table. In this example, a route table named table 1001 is created. We recommend that you keep the route table name the same as the metric value in the default route of the ENI. 192.168.**.253 is the gateway address and 192.168.*.*2 is the primary private IP address of the eth1 secondary ENI.

```
ip -4 route add default via 192.168.**.253 dev eth1 metric 1001 && \ ip -4 route add default via 192.168.**.253 dev eth1 table 1001 && \ ip -4 rule add from 192.168.**.*2 lookup 1001
```

4. View the created route table and routing policy.

```
ip route list table 1001 && \ ip rule list
```

The following figure shows that the route table and routing policy are created.

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| Primary private IP address | 192.168.**.*2 |
| Gateway address | 192.168.**.253 |
| table | 1001 |

Elastic Compute Service aces
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
In this example, the sample values listed in the following table are used. aces Elastic Compute Service
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
After you perform the preceding steps to configure routes for the eth1 secondary ENI, you Elastic Compute Service aces must perform the following steps to configure the routes to automatically update on instance startup. Otherwise, the routes become invalid when the instance is restarted. i. Open the /etc/rc.local file.

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

### View ENIs

You can view the list of created elastic network interfaces (ENIs).

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Networks and Security > ENIs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter condition, such as **ENI ID**, from the drop-down list and enter relevant
information in the search box. The ENIs that meet the specified filter condition are automatically displayed in the ENI list.

**Note**

You can specify multiple filter conditions to narrow down the search results.

### Modify the attributes of a

**secondary ENI**

You can modify the attributes of a secondary elastic network interface (ENI), including its name and security group.

**Prerequisites**

The secondary ENI is in the **Available** state.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the secondary ENI whose attributes you want to modify and click **Modify** in the
**Actions** column.
5. In the **Modify ENI** dialog box, modify the name and security group of the ENI.
6. Click **OK**.
aces Elastic Compute Service

### Unbind a secondary ENI from

**an ECS instance**

You can unbind a secondary elastic network interface (ENI) from an Elastic Compute Service (ECS) instance. After the secondary ENI is unbound from the instance, the instance no longer processes the traffic on the ENI.

**Prerequisites**

Before you unbind a secondary ENI, make sure that the following requirements are met: The secondary ENI is in the **Bound** state. The instance to which the secondary ENI is bound is in the **Running** or **Stopped** state.

**Background information**

Only secondary ENIs can be manually unbound. Primary ENIs share the same lifecycle as the associated instances and cannot be manually unbound.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the secondary ENI that you want to unbind and click **Unbind** in the **Actions** column.
5. In the message that appears, click **Unbind**.

**Result**

If the secondary ENI is unbound from the instance, **Available** is displayed in the **Status** column corresponding to the ENI.

### Delete a secondary ENI

You can delete elastic network interfaces (ENIs) that are no longer needed. Secondary ENIs can be deleted, whereas primary ENIs cannot.

**Prerequisites**

The secondary ENI is in the **Available** state.

**Background information**

When an ENI is deleted, the following results occur: The primary private IP address (PrimaryIpAddress) of the ENI is automatically released. The ENI is removed from all security groups to which it was added.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > ENIs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the secondary ENI that you want to delete and choose
**> Delete** in the **Actions**
column. Elastic Compute Service aces
5. In the message that appears, click **Delete**.

**Result**

On the ENI page, refresh the ENI list. If the ENI is deleted, it is no longer displayed. Elastic Compute Service

## Key pairs

### Overview

Key pairs are a secure and convenient authentication method provided for Elastic Compute Service (ECS) instance logons. Only Linux instances support key pair-based authentication.

**Introduction**

A key pair is a pair of public and private keys that are generated based on an encryption algorithm. By default, 2048-bit RSA key pairs are used. Before you log on to a Linux instance by using a key pair, you must first create a key pair. You can specify a key pair when you create an instance, or bind a key pair to an instance after the instance is created. Then, you can use the private key to connect to the instance.

**Benefits**

Key pair-based authentication has the following advantages over username and passwordbased authentication: Security: Key pairs provide higher security and reliability for logons. Key pairs are more secure than regular user passwords against brute-force attacks. Private keys cannot be deduced even if the public keys are maliciously acquired. Ease of use: If you configure a public key on a Linux instance, you can run an SSH command or use a connection tool to log on to the instance with the corresponding private key, instead of a password. Each key pair can be bound to up to 50 Linux instances. After you bind a key pair to Linux instances, you can connect to the instances without the need to specify the usernames and passwords for the instances. If you want to batch manage multiple Linux instances, we recommend that you use a key pair to log on to the instances. Key pairs have the following limits: Key pairs apply only to Linux instances. If you select a key pair as the logon credential when creating an instance, password-based authentication is disabled by default. This means the instance cannot be accessed via username and password logon methods. If an ECS instance originally uses password authentication, binding a key pair may disable the password-based authentication method. Currently, only RSA 2048-bit key pairs can be created in the ECS console. Each Alibaba Cloud account can have up to 500 key pairs per region. Only a single key pair can be bound to each Linux instance in the ECS console. If you bind a key pair to an instance to which another key pair is already bound, the new key pair replaces the original one. If you want to use multiple key pairs to log on to a Linux instance, you can manually modify the ~/.ssh/authorized_keys file from within the instance to add multiple key pairs. For data security purposes, after you bind a key pair to or unbind a key pair from an instance in the **Running** ( `Running` ) state, restart the instance for the operation to take effect.

| Section | Parameter | Required | Description |
|---|---|---|---|

Elastic Compute Service

**Creation methods**

You can use one of the following methods to create a key pair: Create a key pair in the ECS console. By default, the key pair is generated in the RSA 2048bit format. For more information, see Create a key pair.

**Important**

If you create a key pair in the ECS console, you must download and securely lock away the private key. After the key pair is bound to an instance, you cannot log on to the instance if you do not have the private key. Import your own key pair to ECS. For more information, see Import a key pair.

**Note**

Key pairs that you want to import must support one of the following encryption methods: rsa dsa ssh-rsa ssh-dss ecdsa ssh-rsa-cert-v00@openssh.com ssh-dss-cert-v00@openssh.com ssh-rsa-cert-v01@openssh.com ssh-dss-cert-v01@openssh.com ecdsa-sha2-nistp256-cert-v01@openssh.com ecdsa-sha2-nistp384-cert-v01@openssh.com ecdsa-sha2-nistp521-cert-v01@openssh.com

### Create a key pair

This topic describes how to create a key pair in the Apsara Uni-manager Management Console. After a key pair is created, its private key is automatically downloaded. You must securely store the private key to ensure its confidentiality. To log on to an Elastic Compute Service (ECS) instance to which a key pair is bound, you must provide the private key. This topic describes how to create a key pair in the Apsara Uni-manager Management Console.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Key Pairs**.
3. Click **Create Key Pair**.
4. On the Create Key Pair page, configure the parameters described in the following table.

| Region | Organization | Yes | Select an organization in which to create the key pair. Make sure that the key pair and the virtual private cloud (VPC) belong to the same organization. |
|---|---|---|---|
|  | Resource Set | Yes | Select a resource set in which to create the key pair. Make sure that the key pair and the VPC belong to the same resource set. |
|  | Region | Yes | Select a region in which to create the key pair. Make sure that the key pair and VPC belong to the same region. |
| Basic Settings | Key Pair Name | Yes | Enter a name for the key pair. The key pair name must be unique. The name must be 2 to 128 characters in length and cannot start with a special character or a digit. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), and colons (:). |
|  | Creation Mode | Yes | Select a method to creating the key pair. We recommend that you select Auto-create. Then, you must securely store the private key in a timely manner. Auto-create: The system creates a key pair for you. The private key is automatically downloaded after the key pair is created. The private key can be downloaded only once. You must securely store the private key file. Import: You can enter a Base64-encoded public key in the Public Key field. |

Elastic Compute Service
5. Click **Create**.

**Result**

After the key pair is created, your browser downloads the private key file to your computer.

**Important**

Private key files are downloaded to your computer only when Autocreate is selected. Private key files are not saved in the ECS console and cannot be recovered if they are lost. Make sure that you securely store your private key files to ensure their confidentiality.

**What to do next**

Before you can use a created key pair to log on to an instance, you must bind the key pair to the instance. For more information, see Bind a key pair to an instance.

### Import a key pair

You can create an SSH key pair in the Elastic Compute Service (ECS) console. You can also use a third-party tool to generate an SSH key pair and import the public key of the SSH key pair to ECS.

**Prerequisites**

The public key information of the SSH key pair that you want to import is obtained. For information about how to obtain the public key information of SSH key pairs, see View public key information. Elastic Compute Service

**Precautions**

Take note of the following items:

**Important**

Do not import private keys. Keep private keys secure. To log on to an ECS instance to which a key pair is bound, you must provide the private key. You can import only one public key to an ECS instance. Imported public keys must be encoded in `Base64` and support one of the following encryption methods: rsa dsa ssh-rsa ssh-dss ecdsa ssh-rsa-cert-v00@openssh.com ssh-dss-cert-v00@openssh.com ssh-rsa-cert-v01@openssh.com ssh-dss-cert-v01@openssh.com ecdsa-sha2-nistp256-cert-v01@openssh.com ecdsa-sha2-nistp384-cert-v01@openssh.com ecdsa-sha2-nistp521-cert-v01@openssh.com

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Key Pairs**.
3. Click **Create Key Pair**.
4. Enter a name for the key pair and set **Creation Mode** to **Import**.

**Note**

The name of the key pair must be unique. Otherwise, a prompt indicating that the key pair already exists appears.
5. In the **Public Key** field, enter the public key that you want to import.
6. Click **Create**.

### View key pairs

You can view the details of created key pairs.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Key Pairs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter condition, such as **Key Pair Name**, from the drop-down list and enter
relevant information in the search box. The key pairs that meet the specified filter condition are automatically displayed in the key pair list. Elastic Compute Service

**Note**

You can specify multiple filter conditions to narrow down the search results.

### Bind a key pair to an

**instance**

You can specify a key pair when you create an Elastic Compute Service (ECS) instance, or bind a key pair to the instance after the instance is created. This topic describes how to bind a key pair to an instance after the instance is created. If an ECS instance originally uses password authentication, binding a key pair may disable the password-based authentication method.

**Background information**

When you bind a key pair to an instance, take note of the following items: Each ECS instance can be bound with only a single key pair. If you bind a key pair to an instance to which another key pair is already bound, the new key pair replaces the original one. A key pair can be bound to up to 50 instances.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Key Pairs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the key pair that you want bind and click **Bind Key Pair** in the **Actions** column.
5. In the **Select Instances** list, select instances to which you want to bind the key pair to
move the instances to the right-side list. If you want to select or remove all instances, click **Move All** below the instance lists. If instance names in the **Select Instances** section are dimmed, the instances are Windows instances and cannot have key pairs bound.
6. Click **OK**.
7. If the selected instance is in the **Running** (Running) state, perform the following operations
to restart the instance to make the binding operation take effect: i. In the navigation pane on the left, choose **Instances & Images > ECS Instances**. ii. Find the instance that you want to restart and choose **Instance Status > Restart**
**Instance** in the **Actions** column.
iii. In the message that appears, click **Restart Instance**.

**Note**

After you bind the key pair to ECS instances, find the key pair on the Key Pairs page and click **Related Instances** in the **Actions** column to view all ECS instances to which the key pair is bound.

### Unbind SSH key pairs

Elastic Compute Service This topic describes how to unbind an SSH key pair in the Elastic Compute Service (ECS) console.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Key Pairs**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the key pair that you want to unbind and click **Unbind Key Pair** in the **Actions**
column.
5. In the **Select Instances** section of the Unbind dialog box, click the ID or name of the
instance from which you want to unbind the key pair. Then, the instance is moved to the right-hand column.
6. Click **OK**.
7.

**What to do next**

After the SSH key pair is unbound, you must reset the password of the instance before you log on to the instance as the root user. For more information, see Reset the logon password of an instance.

**Note**

If you have reset the password before you unbind the key pair, you can log on by using the new password after you unbind the key pair.

### Delete a key pair

If you no longer require one or more key pairs, you can delete the key pairs.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Network & Security > Key Pairs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete key pairs:
To delete a single key pair, find the key pair and choose
**> Delete** in the **Actions**
column. To delete one or more key pairs at the same time, select the key pairs and click **Delete** in the lower part of the Key Pairs page.
5. In the message that appears, click **Delete**.

### Add or replace a key pair

You can bind multiple SSH key pairs to a Linux instance to allow access to the instance by using the key pairs. You can also replace the existing key pairs of the instance.

**Prerequisites**

The public keys of the new key pairs are obtained. For more information, see View public key information. Elastic Compute Service

**Background information**

On Linux instances, the public key information of key pairs is stored in the ~/.ssh/authorized_keys file. You can modify the file to add multiple key pairs or replace existing key pairs.

**Note**

When you bind SSH key pairs to instances in the Elastic Compute Service (ECS) console, you can bind only one key pair to each instance. If you need only one key pair for a Linux instance, we recommend that you bind the key pair to the instance in the ECS console. For more information, see Bind a key pair.

**Procedure**

1. Use an existing key pair to log on to the ECS instance.
2. Run the **vim .ssh/authorized_keys** command to open the ~/.ssh/authorized_keys file.
3. Add or replace public key information.
You can add and save new public key information under the existing public key information.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCys3aOkFm1Xh8iN0lijeQF5mz9Iw/FV/bUUduZjauiJa1KQJSF4+czK MAv38QEspiWStkSfpTn1g9qeUhfxxxxxxxxxx+XjPsf22fRem+v7MHMa7KnZWiHJxO62D4Ihvv2hKfskz8K44 xxxxxxxx+u17IaL2l2ri8q9YdvVHt0Mw5TpCkERWGoBPE1Y8vxFb97TaE5+zc+2+eff6xxxxxxxxxx/feMeCx 6Lhc2NEpHIPxMpjOv1IytKiDfWcezA2xxxxxxxxxx/YudCmJ8HTCnLId5LpirbNE4X08Bk7tXZAxxxxxxxxxx KB1Cxw1TbGMTfWxxxxxxxxxx imported-openssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdlrdZwV3+GF9q7rhc6vYrExwT4WU4fsaRcVXGV2Mg9RHex21hl1au7 kmnIgukBZjywlQOT4GDdsJy2nBOdJPrCEBIPxxxxxxxxxxx/fctNuKjcmMMOA8YUT+sJKn3l7rCLkesE+S588 NdRjBiiUy40kyr7Y+fqGVdSOHGMXZQPpkBtojcxxxxxxxxxx/htEqGa/Jq4fH7bR6CYQ2XgH/hCap29Mdi/G5 1nbUKuIHdMWOPvjxxxxxxxxxx+lHtTGiAIRG1riyNRVC47ZEVCg9iTWWGrWFvxxxxxxxxxx/9H9mPCO1Xt2fx xxxxxBtmR imported-openssh-key
```

**Note**

If the ~/.ssh/authorized_keys file contains information about multiple public keys, you can log on to the instance by using the private keys that correspond to the public keys. You can replace existing public key information with new public key information.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdlrdZwV3+GF9q7rhc6vYrExwT4WU4fsaRcVXGV2Mg9RHex21hl1au7 kmnIgukBZjywlQOT4GDdsJy2nBOdJPrCEBIP6t0Mk5aPkK/fctNuKjcmMMOA8YUT+sJKn3l7rCLkesE+S5880 dRjBiiUy40kyr7Y+fqGVdSOHGMXZQPpkBtojcV14uAy0yV6/htEqGa/Jq4fH7bR6CYQ2XgH/hCap29Mdi/G5T nbUKuIHdMWOPvjGACGcXclex+lHtTGiAIRG1riyNRVC47ZEVCg9iTWWGrWFvVlnI0E3Deb/9H9mPCO1Xt2fxx xxxxBtmR imported-openssh-key
```

If you can log on to the instance by using the new private keys, the key pairs are added or replaced.

### View public key information

If you want to configure the same public key file for a group of Elastic Compute Service (ECS) instances and the public key file is not backed up on your on-premises device, you can view public key information by using the methods that are described in this topic. Elastic Compute Service

**p**

**y**

Public key information is stored in the ~/.ssh/authorized_keys file. Open the file in an instance to view the public key information.

**On-premises Windows device**

To view public key information, perform the following operations:

**Note**

In this example, PuTTYgen is used. The operations that you must perform may vary based on the actual key generation tool.
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

**Note**

If the command fails, run the `chmod 400 my-key-pair.pem` command to modify the permissions to ensure that you can view the file.

| Deployment granularity | Deployment policy | Use Scenario |
|---|---|---|
| Host | Strict dispersion | General-purpose business scenarios. |
|  | Loose dispersion |  |
| Rack | Strict dispersion | Big data and databases |

Elastic Compute Service

## Deployment sets

### Overview

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

**Note**

When you create a deployment set, **Deployment Granularity** is set to
**Host** by default.
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

| Rack |  |  |
|---|---|---|
|  | Loose dispersion | Game customers |
| vSwitch | Strict dispersion | VPN |
|  | Loose dispersion | Game customers |
|  | Strict aggregation | Big data and databases |
|  | Loose aggregation | Game customers |

**Example**

The following figure shows a typical scenario where business reliability is improved by using deployment sets. Three ECS instances of a tenant are distributed on three different physical hosts, which are distributed on at least two different racks.

**Note**

For more information about the deployment set APIs, see **Deployment sets** in **ECS Developer Guide**.

### Create a deployment set

You can use deployment sets to distribute or aggregate Elastic Compute Service (ECS) instances involved in your business. You can select host, rack, or vSwitch as the deployment granularity to improve service availability or network performance.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Deployment Sets & Elasticity**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Deployment Set**.
5. Configure the parameters. The following table describes the parameters.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization/ Resource Set | Yes | The resource set in which you want to create the deployment set. |
|  | Region | Yes | The region in which you want to create the deployment set. |
| Basic Configurati ons | Deployment Domain | Yes | The range of the deployment granularity. Only Default is supported. |
|  | Deployment Granularity | Yes | The minimum unit in which instances can be scheduled when you deploy instances. Valid values: Host: Instances are distributed at the host level. Rack: Instances are distributed at the rack level. Network Switch: Instances are distributed or aggregated at the vSwitch level. |
|  | Deployment Policy | No | The dispersion policies are used to improve service availability to prevent impact on your business when a host, rack, or vSwitch fails. The aggregation policies are used to improve network performance and minimize the access latency between instances. Valid values: Valid values when the Deployment Granularity parameter is set to Host or Rack: Maximized Dispersion Strict Dispersion Valid values when the Deployment Granularity parameter is set to Network Switch: Maximized Dispersion Strict Dispersion Loose Aggregation Extremely Low Network Latency |

Elastic Compute Service

|  | Deployment Set Name | Yes | The name of the deployment set. The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores ( ), and hyphens (-). The name _ must start with a letter and cannot start with http:// or https:// . |
|---|---|---|---|
|  | Description | No | The description of the deployment set. We recommend that you specify a description that can help you identify the deployment set. The description must be 2 to 256 characters in length, and can contain letters, digits, and special characters. Supported special characters include underscores ( ), hyphens (- _ ), periods (.), commas (,), and colons (:). The description must start with a letter and cannot start with http:// or https:// . |

Elastic Compute Service
6. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements.
7. Create the deployment set.
If a service whose **Resources** column value is **Deployment Set** exists on the Service Management page, confirm the deployment set parameters and click **Confirm Order**. If no service whose **Resources** column value is **Deployment Set** exists on the Service Management page, confirm the deployment set parameters and click **Submit**. For more information about service catalog management, see the **Manage services** topic in **Apsara Uni-manager Operations Console User Guide** .

### View deployment sets

You can view the existing deployment sets and the details of each deployment set.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Deployment Sets & Elasticity**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Deployment Sets page, select a filter condition, such as **Deployment Set ID**, from
the drop-down list and enter relevant information in the search box. The deployment sets that meet the specified filter condition are displayed in the deployment set list.

**Note**

You can specify multiple filter conditions to narrow down the search results.
5. Find the deployment set that you want to view and click **Details** in the **Actions** column.
6. In the Deployment Set Details panel; view the details of the deployment set.
View the ID, name, deployment policy, and deployment granularity of the deployment set. Elastic Compute Service View the instances that are added to the deployment set. You can restore abnormal instances. For more information, see Restore abnormal instances in a deployment set.

### Change the deployment set

**of an instance**

This topic describes how to add an Elastic Compute Service (ECS) instance to a deployment set or migrate an instance from one deployment set to another.

**Prerequisites**

The instance is in the **Stopped** or **Running** state.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage and choose
**Change Deployment Set** in the **Actions** column to change the deployment set of the
instance.
5. In the **Change Deployment Set** dialog box, select the destination deployment set and set
the Force Change parameter. Valid values of Forced Change:
**Yes**: allows the instance to be migrated to another host, which may cause the instance to
restart.
**No**: does not allow the instance to be migrated to another host. The instance must
remain on the current host, which may cause a failure to change the deployment set of the instance.
6. Click **OK**.

### Restore abnormal instances

**in a deployment set**

In a deployment set whose Deployment Granularity parameter is set to Host and Deployment Policy parameter is set to Strict Dispersion, the system reports an exception message for the abnormal instances that violate the deployment set constraints. You can restore the abnormal instances with a few clicks.
1. When you restore abnormal instances, the system removes the abnormal instances from
the deployment set to ensure that all instances in the deployment set are normal.
2. Add the restored instances to the deployment set.
Elastic Compute Service

**Note**

When you add a restored instance to a deployment set, the instance may be restarted. A restored instance may fail to be added to the deployment set. If you still need to add the instance to the deployment set, manually perform the operation. You can restore abnormal instances only in a deployment set whose **Deployment**
**Granularity** parameter is set to **Host** and **Deployment Policy** parameter is set to **Strict**
**Dispersion**.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Deployment Sets & Elasticity**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Deployment Sets page, move the pointer over the value in the **Instances** column of
a deployment set to view the status of the instances in the deployment set.
5. If an abnormal instance exists in the deployment set, click **Details** in the **Actions** column.
6. In the **Deployment Set Details** panel, find the abnormal instance in the **Instance**
**Information** section and click **Restore** in the **Actions** column.
7. In the message that appears, click **OK**. Wait until the instance is restored.
Elastic Compute Service

### Modify a deployment set

After you create a deployment set, you can modify the name and description of the deployment set based on your business needs.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Deployment Sets & Elasticity**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Find the deployment set that you want to modify and click **Modify** in the **Actions** column.
5. Modify the name and description of the deployment set.
6. Click **OK**.

### Delete a deployment set

You can delete deployment sets that are no longer needed.

**Prerequisites**

No instances exist in the deployment set.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Deployment Sets & Elasticity**.
3. In the top navigation bar, select an organization, resource group, and region.
4. Use one of the following methods to delete deployment sets:
To delete a single deployment set at a time, find the deployment set and click **Delete** in the **Actions** column. To delete multiple deployment sets at a time, select the deployment sets and click
**Delete** below the deployment set list.
5. In the message that appears, click **Delete**.
Elastic Compute Service tes

## Configuration templates

A configuration template is a tool used to quickly create instances. It is used to store the custom configuration information (excluding the instance name and password) of an Elastic Compute Service (ECS) instance, including the instance type, image ID, system disk (size and type), and data disk (size and type). You can use a specific configuration template to quickly create ECS instances.

**Features and benefits**

All configurations in configuration templates are optional, which offers greater elasticity and scalability in ECS instance creation and can better meet individual requirements in various scenarios. Configuration templates provide the following features and benefits:
**Preset parameters**: You can preset ECS instance creation parameters, such as the
instance type, operating system, network settings, security rules, and storage settings, in a template. You can save the following parameters in a template: organization, resource set, region, zone, whether hot configuration changes are supported, specifications, image type, image ID, system disk size, system disk type, data disk size, data disk type, VPC, vSwitch, and security group.
**Standardization and consistency**: You can use a template to create ECS instances that
have identical configurations and host identical environments. This reduces the risk of human error in configuration and facilitates management and maintenance.
**Quick deployment**: You can quickly create ECS instances from a template without the
need to specify instance parameters.
**Quota**: Each account can create up to 50 instance configuration templates in a single
resource set in each region.
**Optional parameters**: When you create a configuration template, all parameters are
optional. However, if a configuration template does not include required parameters, such as the instance type and image, you must specify the parameters when you use the template to create ECS instances.
**Immutability**: Configuration templates are immutable.

**Create a configuration template**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance** and configure the parameters.
You can also click the icon in the Actions column of an instance and choose **Instance**
**Settings > Save as ECS Configuration Template** . You are redirected to the instance
creation page. The parameters for the instance are automatically populated.
5. In the upper-right corner of the **Configuration overview** panel, click **Save as**
**configuration template**.
tes Elastic Compute Service
6. In the **Save as Configuration Template** dialog box, configure the **Template Name**,
**Sharing Scope**, and **Template Version Description** parameters, and then click **OK**.

**Use the configuration template to create an instance**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance**. Then, click the **Create Template** tab.
You can also go to the **Resource Retrieval** page and click **Template creation instance** in the Operation column.
5. In the **Select Template** section, select the configuration template that you want to use.
After the configuration information is loaded, check all the configuration information. You can modify the parameters required to create an instance based on your business needs.
6. Create the ECS instance.
If a service whose **Resources** value is **ECS** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Confirm Order**.

| Operation | Procedure |
|---|---|
| Modify a template | i. Click Edit in the Operation column. ii. Modify the name, description, and sharing scope of the template. iii. Click Save. |
| Use a template | i. Click Use templates in the Operation column. ii. After the configuration information is loaded, check all the configuration information. You can modify the parameters required to create an instance based on your business needs. iii. Create an instance as prompted. |
| Delete a template | i. Click Delete in the Operation column. ii. In the message that appears, click OK. |

Elastic Compute Service tes If no service whose **Resources** value is **ECS** exists on the Service Management page, check the basic configurations, network configurations, and system configurations of the instance in the **Confirmation** step. Make sure that all configurations meet your business requirements. Then, click **Submit**.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click **Create Instance**. Then, click the **Create Template** tab.
5. In the **Select Template** section, click **Manage templates**.
6. In the Manage templates dialog box, perform the following operations on configuration
templates. ool Elastic Compute Service

## Dedicated resource pool

A Dedicated Resource Pool (DRP) is a resource pool dedicated to a tenant. A DRP is visible and available only to the corresponding tenant. Other tenants cannot access the DRP without authorization. DRPs are created by O&M administrators and assigned to tenants. DRPs allow you to allocate resources in a flexible manner, share resources among tenants, and perform O&M operations in a centralized manner. By creating a DRP, Apsara Stack O&M administrators can grant the permissions on a group of physical machines to a single tenant for exclusive use. This eliminates physical resource competition among tenants to implement resource isolation. Tenants can also obtain detailed attribute information about DRPs, including the number of vCPUs, memory size, list of available instance types, number of remaining specifications, and permissions to adjust oversold ratios. This allows tenants to plan resources independently, meet security compliance requirements, and optimize deployment costs. DRPs support the deployment set feature. Deployment sets can be used to constrain the instance affinity within a DRP.

### Dedicated resource pool

### overview

A Dedicated Resource Pool (DRP) is a feature of Alibaba Cloud Apsara Stack designed for government and enterprise customers. It offers flexible resource partitioning, dedicated tenant resources, and centralized operations.

**Primary purpose**

A DRP consists of multiple physical servers with identical specifications. An operations administrator can create a DRP based on business requirements and assign a specific tenant as its administrator. This provides resource isolation by preventing the tenant from competing with others for physical resources.

**Features**

ECS instances created within a DRP inherit all the features and performance metrics of ECS instances from the public resource pool, simplifying their deployment and use. As a DRP administrator, you can:

**Resource exclusivity and isolation**

: Gain exclusive access to all physical servers within the DRP to meet the stringent isolation requirements for mission-critical workloads.

**Comprehensive resource visualization**

: Monitor key metrics such as total vCPUs, vCPU allocation rate, memory capacity, memory allocation rate, instance type availability, and all instances within the DRP.

**DRP configuration**

: Adjust settings such as the CPU oversubscription ratio, the policies for instance scheduling and physical machine replacement during a DRP failure, and basic DRP information.

**Permission management**

: Share the DRP with other tenants and revoke permissions as needed. Elastic Compute Service ool

**Procedure**

1. Create a dedicated resource pool in the Apsara Uni-manager Management Console.
2. Create an instance in the dedicated resource pool.
3. Manage the status of instances in the dedicated resource pool.
4. Modify the dedicated resource pool.
i. Modify the information of the dedicated resource pool: You can modify the name, the instance scheduling policy in case of faults, and the CPU oversold ratio for the dedicated resource pool. ii. Modify the sharing settings of the dedicated resource pool: You can share the dedicated resource pool with other level-1 organizations. The level-1 organization to which the dedicated resource pool belongs and the organizations with which the dedicated resource pool is shared can view the dedicated resource pool and create instances in it.

### View a dedicated resource

**pool**

| Tab | Description |
|---|---|
| Basic Information | Displays the basic information about the dedicated resource pool, including the ID, name, instance family, and instance scheduling policy upon failures. |
| Resource Information | Display the information about resources in the dedicated resource pool, including the number of physical cores, total memory, total number of GPUs, and vCPUs. |

ool Elastic Compute Service This topic describes how to view the information about a dedicated resource pool. The information includes basic information, resource information, and resource usage of the dedicated resource pool. If you select the root organization in the top navigation bar, the entry of dedicated resource pools is not displayed in the left-side navigation pane. Switch to the organization to which a dedicated resource pool belongs or an organization with which the dedicated resource pool is shared. In level-1 organizations to which dedicated resource pools belong and with which dedicated resource pools are shared, you can view the dedicated resource pools and create instances in them. For more information about shared dedicated resource pools, see Share a dedicated resource pool. A dedicated resource pool is created in the Elastic Compute Service (ECS) console.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. View the information about a dedicated resource pool.
On the Dedicated Resource Pool page, you can view the information about a dedicated resource pool, such as the ID, name, status, administrator, and instance family of the dedicated resource pool. You can perform the following steps to specify the columns to be displayed in the dedicated resource pool list. i. In the upper-right corner of the dedicated resource pool list, click the icon. ii. In the drop-down list, select the columns to be displayed in the dedicated resource pool list. The selected columns are displayed in the dedicated resource pool list in real time.
5. Above the dedicated resource pool list, enter the ID of a dedicated resource pool to exactly
search for the dedicated resource pool.
6. Click **Details** in the **Actions** column to view the details of the dedicated resource pool.
The Basic Information tab appears by default. On this tab, you can view the basic information of the dedicated resource pool. The following table describes the information.

| Resource Usage | Displays the information about the organizations of the following two types: Organizations that are using the resources in the dedicated resource pool Organizations that have permissions on the dedicated resource pool Note Only the administrator of a dedicated resource pool can view resource usage of the dedicated resource pool. The list retains the organizations whose permissions on the dedicated resource pool are revoked but still have instances that are not released in the dedicated resource pool. |
|---|---|

Elastic Compute Service ool
7. Click the **Instance Information** tab to view the information about instances in the
dedicated resource pool. You can view the basic information about each instance, such as the ID or name, IP address, and configurations of the instance. You can also click the value in the **Instance**
**ID/Name** column to go to the details page of ECS instance and view the details of the ECS
instance.

### Create an instance in a

## dedicated resource pool

Instances created in dedicated resource pools provide the same computing, storage, and network capabilities as regular instances. The ID of the dedicated resource pool to which an instance belongs is displayed in the instance information to identify the instance ownership. An instance created in a dedicated resource pool can be migrated only within the dedicated resource pool to ensure resource isolation. If you select the root organization in the top navigation bar, the entry of dedicated resource pools is not displayed in the left-side navigation pane. Switch to the organization to which a dedicated resource pool belongs or an organization with which the dedicated resource pool is shared. In level-1 organizations to which dedicated resource pools belong and with which dedicated resource pools are shared, you can view the dedicated resource pools and create instances in them. For more information about shared dedicated resource pools, see Share a dedicated resource pool. A dedicated resource pool is created in the Elastic Compute Service (ECS) console.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Resource Pool page, find the dedicated resource pool in which you want
to create an instance and click **Create Instance** in the Actions column. Configure the parameters to create an ECS instance. For more information about the parameters, see Create an instance. In the **Regions** section, the **Dedicated Resource**
**Pool** parameter is automatically set and cannot be modified.

| Parameter | Description |
|---|---|
| Instance Information | Check the information of the instance for which you want to change the dedicated resource pool. |
| Destination Dedicated Resource Pool | Move to Dedicated Resource Pool: Before you move the instance to another dedicated resource pool, make sure that the dedicated resource pool meets the following requirements: The destination dedicated resource pool supports the current instance type. The destination dedicated resource pool has sufficient inventory. The destination dedicated resource pool is in the Available state. Remove from Dedicated Resource Pool: Only instances in the dedicated resource pool can be removed. |

ool Elastic Compute Service

### Change the resource pool to

**which an instance belongs**

**Prerequisites**

The Elastic Compute Service (ECS) instance is in the **Stopped** or **Stopped - Standard Mode** state.

**Change the dedicated resource pool to which an instance**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Resource Pool page, find the dedicated resource pool that you want to
manage and click **Details** in the **Actions** column.
5. On the details page of the dedicated resource pool, click the **Instance Information** tab to
view the information about the instances in the dedicated resource pool.
6. Find the instance that you want to manage and choose **Modify > Modify Dedicated**
**Resource Pool** in the **Actions** column.
7. In the Modify Dedicated Resource Pool dialog box, configure the parameters described in
the following table and then click **Precheck**.

| Migration Method | The migration method. The system automatically selects Hot Migration or Cold Migration as the migration method based on the instance status. |
|---|---|
| Forcible Change | If you forcibly change the dedicated resource pool for the instance, the instance may restart. Proceed with caution. |

| Parameter | Description |
|---|---|
| Instance Information | Check the information of the instance for which you want to change the dedicated resource pool. |
| Destination Dedicated Resource Pool | Move to Dedicated Resource Pool: Before you move the instance to another dedicated resource pool, make sure that the dedicated resource pool meets the following requirements: The destination dedicated resource pool supports the current instance type. The destination dedicated resource pool has sufficient inventory. The destination dedicated resource pool is in the Available state. Remove from Dedicated Resource Pool: Only instances in the dedicated resource pool can be removed. |
| Migration Method | The migration method. The system automatically selects Hot Migration or Cold Migration as the migration method based on the instance status. |

Elastic Compute Service ool
8. After the precheck is successful, click **Modify**.

**Note**

When you change the dedicated resource pool for an instance, compute resources are migrated. The migration process takes a period of time. Wait until the migration is complete. After you submit a change request, you can view the task progress on the
**Migration Task** tab of the Instance Details page.

**Change the dedicated resource pool to which an instance**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the instance for which you want to change the dedicated
resource pool, click the icon in the **Actions** column, and then choose **Instance**
**Settings > Modify Dedicated Resource Pool**.
5. In the Modify Dedicated Resource Pool dialog box, configure the parameters described in
the following table and then click **Precheck**.

| Forcible Change | If you forcibly change the dedicated resource pool for the instance, the instance may restart. Proceed with caution. |
|---|---|

ool Elastic Compute Service
6. After the precheck is successful, click **Modify**.

**Note**

When you change the dedicated resource pool for an instance, compute resources are migrated. The migration process takes a period of time. Wait until the migration is complete. After you submit a change request, you can view the task progress on the
**Migration Task** tab of the Instance Details page.

### Modify an on-failure instance

**scheduling policy**

You can configure an on-failure instance scheduling policy to specify whether the instances in the dedicated resource pool can be temporarily removed from the dedicated resource pool when a physical machine in the dedicated resource pool becomes abnormal and the resources are insufficient.

**Background information**

The on-failure instance scheduling policy takes precedence over the scheduling policy configured for the dedicated resource pool to which the instance belongs.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Resource Pool page, find the dedicated resource pool that you want to
manage and click **Details** in the **Actions** column.
5. On the details page of the dedicated resource pool, click the **Instance Information** tab to
view the information about the instances in the dedicated resource pool.
6. Find the instance that you want to manage and choose **Modify > Modify On-failure**
**Instance Scheduling Policy** in the **Actions** column.
7. In the dialog box that appears, configure the **On-failure Instance Scheduling Policy**
parameter and click **Submit**.
**Do Not Allow Scheduling to Public Resource Pool** : The instances in the dedicated
resource pool remain stopped and cannot be removed from the dedicated resource pool when a physical machine in the dedicated resource pool becomes abnormal and the resources are insufficient.
**Allow Temporary Scheduling to Public Resource Pool** : The instances can be
temporarily removed from the dedicated resource pool. The removed instances still belong to the dedicated resource pool. When the dedicated resource pool has sufficient resources, you can add the instances to the dedicated resource pool by restarting, starting, or migrating the instances. Elastic Compute Service ool

**Note**

You cannot set this parameter to **Allow Temporary Scheduling to Public**
**Resource Pool** for dedicated resource pools that support local disks.

### Manage the status of

**instances in a dedicated resource**

**pool**

If you select the root organization in the top navigation bar, the entry of dedicated resource pools is not displayed in the left-side navigation pane. Switch to the organization to which a dedicated resource pool belongs or an organization with which the dedicated resource pool is shared. In level-1 organizations to which dedicated resource pools belong and with which dedicated resource pools are shared, you can view the dedicated resource pools and create instances in them. For more information about shared dedicated resource pools, see Share a dedicated resource pool. A dedicated resource pool is created in the Elastic Compute Service (ECS) console.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Resource Pool page, find the dedicated resource pool that you want to
manage and click **Details** in the **Actions** column.
5. On the details page of the dedicated resource pool, click the **Instance Information** tab to
view the information about the instances in the dedicated resource pool.
6. Find the instance that you want to manage and click **Instance Status** in the **Actions**
column to start, restart, stop, or delete the instance.

**Note**

If the **On-failure Instance Scheduling Policy** parameter is set to **Allow Scheduling**
**to Public Resource Pool** for a dedicated resource pool, instances in the dedicated
resource pool may be temporarily scheduled to a public resource pool if physical machines in the dedicated resource pool fail. If the resources in the dedicated resource pool are sufficient, you can schedule the instances back to the dedicated resource pool by restarting or starting the instances.

### Modify a dedicated resource

**pool**

ool Elastic Compute Service This topic describes how to modify a dedicated resource pool. You can modify the name, the instance scheduling policy in case of faults, and the CPU oversell ratio for a dedicated resource pool. If you select the root organization in the top navigation bar, the entry of dedicated resource pools is not displayed in the left-side navigation pane. Switch to the organization to which a dedicated resource pool belongs or an organization with which the dedicated resource pool is shared. Only the operations administrator has the permissions to modify the information about a dedicated resource pool. To modify a dedicated resource pool, you must select the organization to which the dedicated resource pool belongs in the top navigation bar as an operations administrator. Operations that you can perform vary based on the organization that you select: If you select the organization to which the dedicated resource pool administrator belongs, you can modify the dedicated resource pool. If you select the organization with which the dedicated resource pool is shared, the Modify button is dimmed and you cannot click it. If you select an organization that has no permissions on the dedicated resource pool, no dedicated resource pool is available. The following limits apply when you modify the CPU oversold ratio: You can modify the CPU oversold ratio only for dedicated resource pools that use specific shared Elastic Compute Service (ECS) instances of the following instance families: Intel processor-powered instance families: ecs.s5-k, ecs.s6-k, ecs.s7-k, and ecs.s8-k Hygon processor-powered instance families: ecs.s5-hg-k, ecs.s6-hg-k, and ecs.s7-hg-k Yitian processor-powered instance family: ecs.s8-yt-k Kunpeng processor-powered instance family: ecs.s5-kp-k Phytium processor-powered instance families: ecs.s5-ft-k and ecs.s6-ft-k Custom instance family: ecs.anyshare (If only instances of the ecs.anyshare instance family are available for a cluster, the CPU oversold ratio of the cluster cannot be changed.) You cannot change the CPU oversold ratio of a dedicated resource pool that is being scaled.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Resource Pool page, find the dedicated resource pool that you want to
modify and click **Edit** in the Actions column. In the Edit Dedicated Resource Pool dialog box, modify the parameters.

| Parameter | Description |
|---|---|
| Dedicated Resource Pool Name | The name must be 2 to 120 characters in length and can contain letters, digits, periods (.), underscores ( ), colons (:), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |
| Description | The description of the dedicated resource pool. The value must be 2 to 120 characters in length and can contain letters. The value cannot start with http:// or https://. |
| On-failure Instance Scheduling Policy | Specifies whether the instances in the dedicated resource pool can be temporarily removed from the dedicated resource pool when a physical machine in the dedicated resource pool becomes abnormal and the resources are insufficient. Valid values: Do Not Allow Scheduling to Public Resource Pool: The instances in the dedicated resource pool remain stopped and cannot be removed from the dedicated resource pool when a physical machine in the dedicated resource pool becomes abnormal and the resources are insufficient. Allow Temporary Scheduling to Public Resource Pool: The instances can be temporarily removed from the dedicated resource pool. The removed instances still belong to the dedicated resource pool. When the dedicated resource pool has sufficient resources, you can add the instances to the dedicated resource pool by restarting, starting, or migrating the instances. Note You cannot set this parameter to Allow Temporary Scheduling to Public Resource Pool for dedicated resource pools that support local disks. |

Elastic Compute Service ool i. Modify the basic information about the dedicated resource pool. ii. Modify the CPU oversold ratio setting.
5. Click **OK**.

### Share a dedicated resource

**pool**

The operations administrator can share a dedicated resource pool with other level-1 organizations. The level-1 organization to which the dedicated resource pool belongs and the organizations with which the dedicated resource pool is shared can view the dedicated resource pool and create instances in it. ool Elastic Compute Service If you select the root organization in the top navigation bar, the entry of dedicated resource pools is not displayed in the left-side navigation pane. Switch to the organization to which a dedicated resource pool belongs or an organization with which the dedicated resource pool is shared. Only the operations administrator has the permissions to share dedicated resource pools. To share a dedicated resource pool, you must select the organization to which the dedicated resource pool belongs in the top navigation bar as an operations administrator. Operations that you can perform vary based on the organization that you select: If you select the organization to which the administrator of the dedicated resource pool belongs, you can share the dedicated resource pool. If you select the organization with which the dedicated resource pool is shared, the Sharing Settings button is dimmed and you cannot click it. If you select an organization that has no permissions on the dedicated resource pool, no dedicated resource pool is available.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Resource Pool**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Resource Pool page, find the dedicated resource pool that you want to
share and click **Share Settings** in the Actions column.
5. In the **Sharing Settings** panel, select one or more organizations with which you want to
share the dedicated resource pool. In the **Shared Information** section, click the icon in the Actions column of an organization to revoke the permissions on the dedicated resource pool from the organization.

**Note**

After you revoke the permissions on the dedicated resource pool from an organization, the organization cannot create instances in the dedicated resource pool. However, existing instances are not affected. For more information about how to view all organizations that use a dedicated resource pool, see View a dedicated resource pool.

| Parameter | Description |
|---|---|
| Monitoring Period | Specify the monitoring period. Valid values: 7 Days, 15 Days, and 30 Days. |
| Average CPU Quota Usage | Specify a threshold for average CPU quota usage. High quota usage: The average CPU quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Low quota usage: The average CPU quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Note The threshold can only be an integer multiple of 5%. |

Elastic Compute Service ance

## Monitoring & maintenance

### Configure monitoring

**thresholds for organizations**

You can specify a monitoring period and configure thresholds for a selection of metrics to monitor resource utilization in your organization. Then, you can improve resource utilization efficiency based on monitoring results and optimization suggestions. Monitoring thresholds can be configured only for organizations that use an admin account.

**Procedure**

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

| Average Memory Quota Usage | Specify a threshold for average memory quota usage. High quota usage: The average memory quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Low quota usage: The average memory quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Note The threshold can only be an integer multiple of 5%. |
|---|---|
| Average Storage Quota Usage | Specify a threshold for average storage quota usage. Important This threshold is applicable only to standard SSDs and ultra disks. High quota usage: The average storage quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Low quota usage: The average storage quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Note The threshold can only be an integer multiple of 5%. |

ance Elastic Compute Service
7. Click **OK**.

**Result**

The specified monitoring period and metric thresholds are displayed above the organization list. The organizations that match the specified monitoring period and metric thresholds are displayed in the **Monitoring & Maintenance** section of the **Overview** page in the console.

### View the list of monitored

**organizations**

You can view the organizations that meet the monitoring criteria, specified thresholds, and optimization suggestions within the monitoring period.

**Procedure**

1. Log on to the ECS console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Use one of the following methods to go to the **Monitoring & Maintenance** page:
In the **Monitoring & Maintenance** section of the **Overview** page, click **Handle Now**.

| Parameter | Description |
|---|---|
| Monitoring Period | Specify the monitoring period. By default, the monitoring period is seven days. |

Elastic Compute Service ance In the left-side navigation pane, click **Monitoring & Maintenance**.
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

### Configure monitoring metric

**thresholds for instances**

You can configure the monitoring period and multiple monitoring metric thresholds for instances to improve resource utilization based on the monitoring results and optimization suggestions. You can configure monitoring metric thresholds only as as an operations administrator.

**Procedure**

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

| Average CPU Utilization | Specify the threshold for the average CPU utilization. High resource usage: The resource usage of an instance is considered high if its average CPU utilization is greater than or equal to the upper threshold that you specify. This threshold can range from 60% to 95%. Low resource usage: The resource usage of an instance is considered low if its average CPU utilization is smaller than or equal to the lower threshold that you specify. This threshold can range from 5% to 40%. Note The threshold must be an integral multiple of 5%. |
|---|---|
| Average Memory Usage | Specify the threshold for the average memory usage. High resource usage: The resource usage of an instance is considered high if its average memory usage is greater than or equal to the upper threshold that you specify. This threshold can range from 60% to 95%. Low resource usage: The resource usage of an instance is considered low if its average memory usage is smaller than or equal to the lower threshold that you specify. This threshold can range from 5% to 40%. Note The threshold must be an integral multiple of 5%. |

ance Elastic Compute Service
7. Click **OK**.

**Result**

The specified monitoring period and metric thresholds are displayed on the top of the instance list. In the **Monitoring & Maintenance** section of the **Overview** page in the ECS console, the instances that meet monitoring criteria within the specified monitoring period are displayed.

### View the list of monitored

## instances

You can view the instances that meet the monitoring criteria, specified thresholds, and optimization suggestions within the monitoring period.

**Procedure**

1. Log on to the ECS console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Use one of the following methods to go to the **Monitoring & Maintenance** page:
Elastic Compute Service ance In the **Monitoring & Maintenance** section of the **Overview** page, click **Handle Now**. In the left-side navigation pane, click **Monitoring & Maintenance**.
4. Click the **Instances** tab and click one of the following tabs as needed:
**High Resource Usage**: displays instances whose resource usage reaches or exceeds the
upper thresholds that you specify.
**Low Resource Usage**: displays instances whose resource usage reaches or falls below
the lower thresholds that you specify.

**Result**

You can view the configured monitoring period and metric thresholds on the top of the instance list. You can view the information of instances that meet monitoring criteria within the specified monitoring period in the instance list, such as the instance ID and name and resource set.

### Reclaim instance resources

You can optimize your business layout by reclaiming under-used instance resources based on the monitoring results of metrics that you set thresholds for. Only instance resources with low usage can be reclaimed. After an Elastic Compute Service (ECS) instance is moved to the recycle bin, the storage resources of the instance are retained, but its computing resources such as vCPUs and memory are released. After an ECS instance is moved to the recycle bin, the instance is retained here for a specified period of time. During the retention period, the instance can be recovered. After the retention period, the instance is automatically deleted.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Monitoring & Maintenance**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Instances** tab and click **Low Resource Usage**.
5. Find the instance that you want to reclaim, click **Recycle** in the **Actions** column.
6. In the message that appears, click **OK**.
After the instance is reclaimed, **Stopped - Pending Release** is displayed in the Status column of the instance list. You can view the instance in the recycle bin.

**Related operations**

You can restore instances in the recycle bin based on business needs. For more information, see Restore an instance. Elastic Compute Service

## Dedicated hosts

### Overview

**What is DDH?**

Dedicated Host (DDH) is a solution that Apsara Stack designs for enterprise users. DDH offers highly cost-effective features, such as dedicated physical resources, flexible deployment, and various configurations. DDH allows you to exclusively use all resources of a physical host and provides flexible and easy-to-use cloud services. You can create Elastic Compute Service (ECS) instances on a host. Such ECS instances provide the same features and services as standard ECS instances.

**DDH capabilities**

Enhanced isolation and security: DDH provides exclusive physical resources to ensure that users can exclusively use physical resources, such as CPU, memory, and network interface controller (NIC) resources. This improves data security and business isolation and is suitable for enterprises with high security and compliance requirements. Cost optimization: DDH can increase the deployment density in low-CPU utilization scenarios, such as the development and test environment and internal system. This reduces the cost of cloud migration. Flexible deployment: ECS instances can be flexibly migrated between hosts of the same specifications. Service availability: If the physical machine on which a dedicated host resides fails, the system automatically migrates the instances deployed on the dedicated host to a healthy physical machine. After the migration is complete, the dedicated host is released from the failed physical machine.

### Create an ECS instance on a

**host**

You can create an Elastic Compute Service (ECS) instance on a dedicated or shared host. This topic describes how to create an ECS instance on a dedicated host.

**Note**

You can manage the resources of a host by yourself. Before you create an ECS instance on a host, make sure that the host has sufficient available resources.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Host**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Hosts tab of the Hosts page, click the **Dedicated Host** or **Shared Host** tab.
5. In the host list, find the host on which you want to create an ECS instance and click **Create**
**an instance** in the **Actions** column.
Elastic Compute Service On the Create Instance page, configure the parameters to create an ECS instance. For more information about the parameters, see Create an instance. In the **Dedicated Host** section, the **Host Type** and **Associated Host** parameters are automatically configured and cannot be modified.

**Execution results**

In the host list, find the host on which you created the ECS instance and click **Details** in the
**Actions** column to open the host details panel. On the **Instance list** tab, you can view the
information about the ECS instance that you created on the host in the columns, such as
**Instance ID/Name**, **Organization/Resource Set**, **Status**, and **IP Address**.

### Manage hosts

#### Create a dedicated host

A dedicated host is a cloud host whose physical resources are reserved for the exclusive use of a single tenant. Elastic Compute Service (ECS) instances that are created on a dedicated host are physically isolated from those created on other dedicated hosts. This topic describes how to create a dedicated host.

**Background information**

To ensure business continuity when physical servers fail, Apsara Stack provides the Instance Failover upon Host Failure feature for dedicated hosts. If you enable the **Instance Failover**
**upon Host Failure** feature when you create a dedicated host, the dedicated host and the
ECS instances deployed on the dedicated host are failed over to a healthy physical server when the dedicated host fails due to a hardware failure. If you do not enable the **Instance**
**Failover upon Host Failure** feature when you create a dedicated host, the dedicated host
and the ECS instances deployed on the dedicated host are not failed over to a healthy physical server when the dedicated host fails due to a hardware failure.

**Note**

If a dedicated host and the ECS instances deployed on the dedicated host are failed over to a healthy physical server after a hardware failure occurs, the ID of the dedicated host and information about the ECS instances remain unchanged, such as the IDs of the instances. However, the machine code of the dedicated host changes.

**Procedure**

1. Log in to the ECS console.
2. In the left-side navigation pane, click **Dedicated Host**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Dedicated Host tab of the **Hosts** tab, click **Create Host**.
5. On the **Create Host** page, configure the parameters. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| Basic Configurations | Organization/Res ource Set | The resource set in which you want to create the dedicated host. |
|  | Region/Zone | The region and zone in which you want to create the dedicated host. |
| Instance | Type | The type of the dedicated host. The dedicated host type determines the instance type and the maximum number of ECS instances that can be deployed on the dedicated host. Note You must check whether the dedicated host type has available resources. |
|  | Hostname | The name of the dedicated host. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ and colons (:). It must start with a letter and cannot start with http:// or https://. |
|  | Quantity | The number of dedicated hosts that you want to create. |
|  | Sharing Scope | The sharing scope of the dedicated host. Valid values: Current Resource Set, Current Organization and Subordinate Organizations, and Current Organization. |
| Other Settings | Automatic Deployment | Specifies whether to enable automatic deployment for the dedicated host. Valid values: Enable Disable |

Elastic Compute Service

|  | Instance Failover upon Host Failure | Specifies whether to migrate the dedicated host and the ECS instances that are deployed on the dedicated host to a healthy physical server when the physical server on which the dedicated host resides fails. Valid values: Yes No Note To ensure that the dedicated host and ECS instances deployed on the dedicated host can be migrated to a physical server that meets the conditions when a failure occurs, reserve an empty physical server that supports the same dedicated host type. |
|---|---|---|

Elastic Compute Service
6. After you configure the parameters, review the parameter settings in the **Configuration**
**overview** section on the right side of the page to ensure that the settings meet your
business requirements.
7. Create the dedicated host.
If a service whose **Resources** column value is **Dedicated Host** exists on the Service Management page, confirm the dedicated host parameter settings and click **Confirm**
**Order**.
If no service whose **Resources** column value is **Dedicated Host** exists on the Service Management page, confirm the dedicated host parameter settings and click **Submit**. For more information about service management, see **Operations > Service catalog >**
**Service management** in Apsara Uni-manager Management Console User Guide in the
Apsara Stack Documentation Center.

**Verify the result**

After the dedicated host is created, you can view the dedicated host in the dedicated host list and create ECS instances on the dedicated host. For information about the parameters used to create an ECS instance, see Create an instance.

#### Share a host

You can share a created dedicated host to other organizations. The organizations can create Elastic Compute Service (ECS) instances on the shared host. This topic describes how to share a host, change the sharing scope of a host, and view the hosts that are shared by other organizations to you.

**Important**

Before you perform the operation, take note of the following items: The organizations to which a host is shared can create ECS instances on the host. For information about how to create an ECS instance on a host, see Create an ECS instance on a host. Before you can delete a shared host, you must delete all ECS instances that reside on the host. After you delete a host that you shared to other organizations, the organizations can no longer view the host. Elastic Compute Service Hosts can be shared only across level-1 organizations. You can share a host to up to 10 level-1 organizations at a time and to up to 50 level-1 organizations in total.
1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Hosts** page, choose **Hosts > Dedicated Host** to view the list of hosts.
5. Find the host that you want to share. In the **Actions** column, click **Sharing Settings**.
6. In the **Sharing Settings** dialog box, select the organizations to which you want to share
the host from the **Organization** drop-down list.

**Note**

If you cannot obtain a list of organizations due to insufficient permissions, enter the names of level-1 organizations in the Organization field to share the host.
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

#### Delete a dedicated host

If you no longer need a dedicated host on which Elastic Compute Service (ECS) instances reside, you can delete the dedicated host.

**Prerequisites**

Before you delete a dedicated host, remove all ECS instances that reside on it.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Host**.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Basic Configuration s | Organization | Yes | The organization in which to create the host group. |
|  | Resource Set | Yes | The resource set in which to create the host group. |
|  | Region | Yes | The region in which to create the host group. |
| Document Versio | n: 20260629 46 |  |  |

Elastic Compute Service
3. On the Dedicated Host page, choose the **Hosts > Dedicated Host** tab.
4. In the top navigation bar, select an organization, resource group, and region.
5. Use one of the following methods to delete one or more dedicated hosts:
To delete a single dedicated host, find the dedicated host that you want to delete and click **Delete** in the **Actions** column. To delete one or more dedicated hosts at a time, select the dedicated hosts that you want to delete and click **Delete** in the lower part of the **Dedicated Host** tab.
6. Confirm the dedicated host deletion operation.
If a service whose **Resources** value is **DDH** exists on the Service Management page, click **Confirm Order** in the dialog box that appears. If a service whose **Resources** value is **DDH** does not exist on the Service Management page, click **OK** in the dialog box that appears. For more information about service management, see **Operations > Service catalog >**
**Service management** in Apsara Uni-manager Management Console User Guide in the
Apsara Stack Documentation Center.

### Manage dedicated host

**groups**

#### Create a host group

You can group dedicated hosts into host groups for easy management. This topic describes how to create a host group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the **Host Groups** tab.
5. Click **Create Host Group**.
6. On the **Create Host Group** page, configure the parameters described in the following
table.

|  | Zone | Yes | The zone in which to create the host group. |
|---|---|---|---|
| Instance | Host Group Name | No | The name of the host group. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and colons (:). _ The name must start with a letter and cannot start with http:// or https://. |

Elastic Compute Service
7. Create the host group.
If the service whose **Cloud resources** value is **Dedicated Host Clusters** exists on the Service Management page, confirm the host group parameters and click **Confirm Order**. If the service whose **Cloud resources** value is **Dedicated Host Clusters** does not exist on the Service Management page, confirm the host group parameters and click **Submit**. For more information about service management, see **Operations > Service catalogs >**
**Service management** in the Apsara Uni-manager Management Console User Guide in the
Apsara Stack Documentation Center.

**Result**

After the host group is created, you can view the host group in the host group list.

#### View a host group

You can view the details of an existing host group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Host**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter condition, such as **Host Group ID**, from the drop-sown list and enter a valid
value in the search box. The host groups that meet the specified filter condition are automatically displayed in the dedicated host group list.

**Note**

You can search for a host group by host group ID, hostname, or tag. Fuzzy search is supported only if you select **Host Group ID** as the filter condition. You can also specify multiple filter conditions to filter host groups that you require.
5. Click the value in the **Host Group ID/Name** column of a host group to view the details of
the host group.
6. Optional. View the operation logs of the host group.
i. On the **Host Group Details** page, click the **Operation Log** tab. ii. Find the operation that you want to view and click **Operation Details** in the **Actions** column. Elastic Compute Service iii. In the **Operation Details** panel, view detailed operation logs in the **Basic Information** and **API Call Details** sections.

#### Add dedicated hosts to a host group

After you create a host group, you can add dedicated hosts to the host group for easy management. This topic describes how to add dedicated hosts to a host group.

**Procedure**

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

#### Delete a dedicated host group

If you no longer need a dedicated host group, you can delete the dedicated host group.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Hosts**.
3. On the Hosts page, click the **Host Groups** tab.
4. In the top navigation bar, select an organization, resource group, and region.
5. Use one of the following methods to delete one or more dedicated host groups:
To delete a single dedicated host group, find the dedicated host group that you want to delete and click **Delete** in the **Actions** column. To delete one or more dedicated host groups at a time, select the dedicated host groups that you want to delete and click **Delete** in the lower part of the **Host Groups** page.
6. In the message that appears, click **Delete**.

### Migrate an ECS instance

**between different dedicated hosts**

As your business grows and changes, resource allocation on your dedicated hosts may become imbalanced. To address this issue, you can migrate Elastic Compute Service (ECS) instances between dedicated hosts to balance the allocation of resources. This enhances resource utilization and ensures high availability of your services. This topic describes how to migrate an ECS instance between different dedicated hosts.

| Parameter | Description |
|---|---|
| Destination Host | Select the dedicated host to which you want to migrate the ECS instance from the Destination Host drop-down list. Note If no dedicated host is available to host the ECS instance in your Apsara Stack account, the Destination Host drop-down list is empty. |
| New Instance Family | Select the instance family of the instance that you want to create on the dedicated host. Note This parameter is displayed only if the Migration Method parameter is set to Cold Migration. |

Elastic Compute Service

**Prerequisites**

The destination dedicated host must meet the following requirements: You can manage resources on the destination host. Before you migrate an instance from one host to another, make sure that the destination host has sufficient available resources. If the destination host and the ECS instance to be migrated belong to different organizations, make sure that the destination host is shared with the organization to which the instance belongs. For more information, see Share a host.

**Impacts**

After an ECS instance is migrated from a dedicated host to another, the dedicated host IDs and the metadata of the ECS instance, such as the instance ID, private IP address, and public IP address, remain unchanged.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, click **Dedicated Host**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Hosts** page, click the **Dedicated Host** tab of the **Hosts** tab.
5. In the dedicated host list, find the host that you want to manage and click **Details** in the
**Actions** column.
6. In the details panel of the dedicated host, find the instance that you want to migrate and
click **Change Host** in the **Actions** column on the **Instance list** tab.
7. In the **Change Host** dialog box, configure the parameters and click **OK**.

| New Instance Type | You can change the instance type when you migrate the ECS instance. The supported instance types depend on the specifications of the destination dedicated host. Note This parameter is displayed only if the Migration Method parameter is set to Cold Migration. |
|---|---|
| Migration Method | You can set this parameter to Cold Migration or Hot Migration. If you select Cold Migration, the ECS instance to be migrated must be in the Stopped state. |

Elastic Compute Service Elastic Compute Service

## O&M and monitoring

### Cloud Assistant

#### Overview

Cloud Assistant is a native automated operations and maintenance (O&M) tool developed for Elastic Compute Service (ECS). Cloud Assistant allows you to batch maintain ECS instances. Cloud Assistant also allows you to batch run commands, which can be shell, PowerShell, or batch commands, on ECS instances and send files to ECS instances in a password- and logonfree manner without the need to use jump servers. In most cases, you can use Cloud Assistant to install and uninstall software, start and stop services, distribute configuration files, and run common commands (or scripts). This is a test update to verify the adoc push workflow for English documentation.

**Features**

When the instances on which the Cloud Assistant client is installed are in the **Running** ( `Running` ) state, you can use Cloud Assistant to perform the following operations on the instances in the ECS console or by calling API operations: Run batch and PowerShell scripts on Windows instances, or run shell, Python, and Perl scripts on Linux instances. Upload files to the instances. Run the same command on multiple instances. The execution of the command on one instance do not affect the other instances. Specify custom parameters in Cloud Assistant commands to adapt to different scenarios.

**Note**

Cloud Assistant does not proactively initiate any operations. You have full control over all Cloud Assistant operations.

**Scenarios**

Cloud Assistant helps you perform deployment and O&M tasks on instances. The following items are a few examples: Uploading and running automated O&M scripts Running scripts that are already uploaded to instances Managing software lifecycle Deploying code or applications Polling processes Installing service-related patches or security updates Obtaining updates from Object Storage Service (OSS) or YUM repositories Changing hostnames or user logon passwords You can configure recurring Cloud Assistant tasks only by calling API operations. The interval at which a command is run cannot be less than 10 seconds.

| Term | Description |
|---|---|
| Cloud Assistant | A tool that helps you perform routine maintenance tasks on multiple ECS instances and ECS bare metal instances. Cloud Assistant is available in all Alibaba Cloud regions. |
| Cloud Assistant client | A lightweight plug-in that can be installed on ECS instances to run Cloud Assistant commands. On Windows instances, the process of the client program is named AliyunService. On Linux instances, the process of the client program is named aliyun.service. |

Elastic Compute Service For files or commands that consist of batch, PowerShell, or shell scripts with custom parameters, the following limits apply to their sizes after Base64 encoding: If a command is created not by using the immediate execution feature, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run simultaneously by using the immediate execution feature and is saved, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run simultaneously by using the immediate execution feature but is not saved, the command cannot exceed 24 KB in size after Base64 encoding. A file that you want to upload cannot exceed 32 KB in size after Base64 encoding. Each command can contain up to 20 custom parameters. Cloud Assistant commands can be run only on instances that use the following operating systems: Alibaba Cloud Linux CentOS 7, CentOS 8, and later

**Note**

CentOS 8 reached end of life (EOL) and is no longer maintained by the Linux community. We recommend that you migrate from CentOS 8 to Anolis or Alibaba Cloud Linux. Debian 9 OpenSUSE Kylin FreeBSD SUSE Linux Enterprise Server (SLES) 11, SLES 12, SLES 15, and later Ubuntu 14, Ubuntu 16, Ubuntu 18, and later Windows Server 2012, Windows Server 2016, Windows Server 2019, and later

**Terms**

The following table describes the relevant terms in Cloud Assistant.

| Cloud Assistant daemon process | A daemon process that is used to monitor the resource consumption of the Cloud Assistant client, report the running status of the client, and restart the client if the client fails. Service name: AssistDaemon Path: /usr/local/share/assist-daemon/assist daemon _ Note The Cloud Assistant daemon process is available only on Linux instances. |
|---|---|
| task execution path | The path in which Cloud Assistant saves your command as a file on an ECS instance and executes the file. The path varies based on the operating system. Linux: /tmp Windows: <Installation path of Cloud Assistant>/work/script |
| command | A specific command that can be run on instances. Example: a command that consists of a shell or PowerShell script. |
| custom parameter | A variable that you specify in the {{key}} format in a command. You can specify a custom parameter and the value of the parameter in the {{"<key>":"<value>"}} format when you create a task to run the command. |
| one-time execution | The execution ( Invocation ) of a one-time task. A one-time task runs a command only once on one or more instances. |
| recurring execution | An execution of a recurring task. A recurring task runs a command on one or more instances based on a schedule. |
| execution status | The relationships among different types of execution states. For more information, see the Execution states section of this topic. |

| Execution state in API responses | Execution state in the ECS console | Description |
|---|---|---|
| Running | Running | The command is being run. |
| Stopping | Stopping | The command is being stopped. |

Elastic Compute Service

**Execution states**

The following table describes the instance-level execution state of a command that is run on a single instance. The **InvocationStatus** parameter in API responses indicates the execution status of a command.

| Stopped | Stopped | The command is stopped. |
|---|---|---|
| Finished | Completed | The command is run to completion. This does not indicate that the command is successful. You can check whether the command is successful based on the command output ( Output ) and the exit code ( ExitCode ). |
| Failed | Failed | The command cannot be run or the command process did not complete before the timeout period specified by Timeout ends. |

| Execution state in API responses | Execution state in the ECS console | Description | Priority |
|---|---|---|---|

Elastic Compute Service

**States of batch executions and recurring executions**

A batch execution is a one-time execution in which a command is run on multiple instances. To better manage batch executions and recurring executions, you can manage the lifecycles of the executions based on the overall execution states, instance-level execution states, and execution-level states. The **InvokeStatus** parameter in API responses indicates the execution status of a command. The following figure shows the relationships among the three types of execution states. The following table describes the overall execution states of a command that is run on multiple instances at the same time.

|  | Running |  | Running | The instance-level execution state is Running (Running) on specific or all instances. | 1 |
|---|---|---|---|---|---|
|  | Stopping |  | Stopping | The instance-level execution state is Stopping (Stopping) on specific or all instances. | 2 |
|  | Stopped |  | Stopped | The instance-level execution state is Stopped (Stopped) on all instances. | 3 |
|  | Failed |  | Failed | The instance-level execution state is Failed (Failed) on all instances, or is Failed (Failed) on specific instances and is Stopped (Stopped) on other instances. | 4 |
|  | Finished |  | Completed | The instance-level execution state is Completed (Finished) on all instances, or is Completed (Finished) on specific instances and is Stopped (Stopped) on other instances. | 5 |
|  | PartialFailed |  | Partially Failed | The instance-level execution state is Failed (Failed) on some instances and is Completed (Finished) on the other instances. | 6 |
|  |  | PartialFailed |  |  |  |

Elastic Compute Service

| State | Description |
|---|---|
| Overall execution state | The overall execution state is always Running ( Running ) unless you stop the command execution on all instances. |
| Instance-level execution state | For each instance, the instance-level execution state is alwaysR unning ( Running ) unless you stop the command on the instance. |
| Execution-level state | For more information, see the Execution states section of this topic. |

Elastic Compute Service The following figure shows the relationship between the overall execution states and the instance-level execution states of a one-time execution in which a command is run on three instances at the same time. The following table describes the states of recurring executions of a command.

#### Configure the Cloud Assistant client

##### View the status of Cloud Assistant and

**handle anomalies**

This topic describes how to view the status of Cloud Assistant, export the Cloud Assistant status list of Elastic Compute Service (ECS) instances, and handle anomalies.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
Elastic Compute Service
4. On the **ECS Instances** tab, view the status of Cloud Assistant.
**Normal**: Cloud Assistant works as expected.
**Not Installed**: Cloud Assistant Agent is not installed on the instance. Contact technical
support.
**Abnormal**: A status anomaly can occur due to various reasons. Troubleshoot the issue
based on the actual scenario. For more information, see Handle Cloud Assistant status anomalies.
5. Optional. Export the Cloud Assistant status list for ECS instances.
Click the icon in the upper-right corner of the ECS instance list to download the Cloud Assistant status list for ECS instances to your local computer.

**Linux ECS instance**

1. Use Workbench to connect to the Linux ECS instance over SSH.
2. Run the following command to check whether the directory where Cloud Assistant Agent is
installed exists:

```
cd /usr/local/share/
```

`ls` If the `aliyun-assist` folder exists, proceed to Step 3. If the `aliyun-assist` folder does not exist, Cloud Assistant Agent was uninstalled. You must reinstall Cloud Assistant Agent.

```
ls -l /sbin/init
```

If the output shows `systemd` , for example, `/lib/systemd/systemd` , the system uses

```
 systemd .
```

If the output shows `upstart` , for example, `/sbin/upstart` , the system uses

```
 Upstart .
```

If the output shows `init` , for example, `/sbin/init` , the system uses `sysvinit` .

| ssistant is | inactive (dead) | , Clo |
|---|---|---|
| systemctl start aliyun.service |  |  |

| f Cloud Assistant is | Stopped | , Cloud |
|---|---|---|
| /etc/init.d/aliyun-service start |  |  |

Elastic Compute Service Run the following command to view the status of Cloud Assistant:

```bash
systemctl status aliyun.service
```

Assistant Agent. If an error message appears during startup or Cloud Assistant Agent fails to be started, uninstall and reinstall Cloud Assistant Agent. If the status of Cloud Assistant is `active (running)` , Cloud Assistant works as expected. Proceed to Step 4.

**Upstart**

Run the following command to view the status of Cloud Assistant:

```
/sbin/initctl status aliyun-service
```

If the status of Cloud Assistant is `stop/waiting` , Cloud Assistant Agent is stopped, and you must run the `/sbin/initctl start aliyun-service` command to start Cloud Assistant Agent. If an error message appears during startup or Cloud Assistant Agent fails to be started, uninstall and reinstall Cloud Assistant Agent. If the status of Cloud Assistant is `start/running` , Cloud Assistant works as expected. Proceed to Step 4.

**sysvinit**

Run the following command to view the status of Cloud Assistant:

```
/etc/init.d/aliyun-service status
```

Agent. Elastic Compute Service If an error message appears during startup or Cloud Assistant Agent fails to be started, uninstall and reinstall Cloud Assistant Agent. If the status of Cloud Assistant is `Running` , Cloud Assistant runs as expected. Proceed to Step 4.
4. View the status of Cloud Assistant in the Cloud Assistant console.
If the status of Cloud Assistant is normal, the issue is resolved. If the status of Cloud Assistant is abnormal, view Cloud Assistant logs to identify the causes.

```
cd /usr/local/share/aliyun-assist/<version>/log tail -100f aliyun_assist_main.log
```

1. Use Workbench to connect to the Windows ECS instance over RDP.
2. Check whether the C:\ProgramData\aliyun\assist directory where Cloud Assistant Agent
is installed exists. If the assist folder exists, proceed to Step 3. If the assist folder does not exist, Cloud Assistant Agent was uninstalled.You must reinstall Cloud Assistant Agent. i. Click Start and choose **Windows Administrative Tools > Computer Management**. ii. Choose **Computer Management (Local) > Services and Applications > Services**. Elastic Compute Service iii. Find **Aliyun Assist Service** in the Name column and view the status of **Cloud**
**Assistant**.
If **Running** is displayed in the **Status** column, **Cloud Assistant** works as expected. If no value is displayed in the **Status** column, Cloud Assistant Agent is stopped. Click
**Start** to start **Cloud Assistant Agent**.
If an error message appears during startup or Cloud Assistant Agent fails to be started, uninstall and reinstall Cloud Assistant Agent.
4. View the status of Cloud Assistant in the Cloud Assistant console.
If the status of Cloud Assistant is normal, the issue is resolved. If the status of Cloud Assistant is abnormal, view Cloud Assistant logs to identify the causes. The default path of the log file: C:\ProgramData\aliyun\assist\<version>\log . `<version>` indicates the version number of Cloud Assistant Agent.

##### Configure DNS resolution for Cloud

**Assistant**

This topic describes how to configure Domain Name System (DNS) resolution for Cloud Assistant. During the configuration procedure, you must obtain the IP addresses that correspond to the Cloud Assistant endpoints and then modify the hosts file.

**Background information**

Elastic Compute Service When you use features such as Cloud Assistant on an Elastic Compute Service (ECS) instance, the instance must have access to the endpoints required to perform actions that you specify, such as running a Cloud Assistant command. The default DNS Nameserver is installed on each ECS instance to resolve domain names. You can run the **cat /etc/resolv.conf** command to view the DNS Nameserver settings. Example command output: If you modify the configuration file to override the default DNS Nameserver settings, domain names may fail to resolve or resolve slowly when you use features such as Cloud Assistant. This may cause the features to be unavailable. For example, Cloud Assistant commands cannot be run. In this case, you can perform the following procedure to configure DNS resolution for Cloud Assistant.

**Procedure**

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

**Note**

Replace <region-id> with a region ID.
3. Modify the hosts file.

```
echo "100.100.XX.XX <region-id>.axt.aliyun.com" >> /etc/hosts && \ echo "100.118.XX.XX aliyun-client-assist-<region-id>.oss-<region-id>internal.aliyuncs.com" >> /etc/hosts
```

**Note**

Replace `100.100.XX.XX` and `100.118.XX.XX` with the IP addresses that you obtained in the previous step.
4. Check whether the hosts file is modified.

```
cat /etc/hosts
```

Elastic Compute Service If the hosts file is modified, the command output includes the Cloud Assistant endpoints and their corresponding IP addresses. Example command output: After the hosts file is modified, the ECS instance can automatically obtain IP addresses from the hosts file to resolve the Cloud Assistant endpoints.

##### Start or stop the Cloud Assistant client

The Cloud Assistant client is an agent that runs Cloud Assistant commands on Elastic Compute Service (ECS) instances. This topic describes how to start or stop the Cloud Assistant client.

**Start or stop the Cloud Assistant client on a Windows instance**

To start or stop the Cloud Assistant client on a Windows instance, perform the following steps.

**Warning**

**Aliyun Assist Service** is the process of the Cloud Assistant client. If you
stop **Aliyun Assist Service**, the Cloud Assistant client stops. This may cause an exception on the instance, and the instance cannot be stopped by using the ECS console. Proceed with caution when you stop the Cloud Assistant client.
1. Connect to the Windows instance. For more information, see Connect to a Windows
instance from a Windows computer by using Remote Desktop.
2. Click Start and choose **Windows Administrative Tools > Computer Management**.
3. Choose **Computer Management (Local) > Services and Applications > Services**.
4. Find **Aliyun Assist Service** and click **Stop the service** or **Restart the service**.

**Uninstall the Cloud Assistant daemon process from a Linux**

The Cloud Assistant daemon process is used to monitor the resource consumption of the Cloud Assistant client, report the running status of the client, and restart the client when the client fails. Before you stop the Cloud Assistant client, you must first uninstall the Cloud Assistant daemon process.

**Note**

The Cloud Assistant daemon process is available only for Linux instances.
1. Connect to the Linux instance. For more information, see Connect to a Linux instance by
Elastic Compute Service using SSH commands in Linux or Mac OS X or Connect to a Linux instance by using a remote connection tool in Windows.
2. Stop the Cloud Assistant daemon process.

```
/usr/local/share/assist-daemon/assist_daemon --stop
```

**Note**

In the preceding command, /usr/local/share/assist-daemon/assist_daemon specifies the default path of the Cloud Assistant daemon process.
3. Uninstall the Cloud Assistant daemon process.

```
/usr/local/share/assist-daemon/assist_daemon --delete
```

4. Delete the directory of the Cloud Assistant daemon process.

```
rm -rf /usr/local/share/assist-daemon
```

**Start or stop the Cloud Assistant client on a Linux instance**

**Note**

Before you stop the Cloud Assistant client, you must first uninstall the Cloud Assistant daemon process. For more information, see the Uninstall the Cloud Assistant daemon process from a Linux instance section. To start or stop the Cloud Assistant client on a Linux instance, perform the following steps:
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

Elastic Compute Service Stop the Cloud Assistant client.

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

#### Use Cloud Assistant

##### Create and run a command

You can run Cloud Assistant commands to perform routine tasks on Elastic Compute Service (ECS) instances. These tasks include running automated operations and maintenance scripts, polling processes, resetting user passwords, installing or uninstalling software, updating applications, and installing patches. Command types can be batch or PowerShell commands for Windows instances and shell commands for Linux instances. You can specify custom parameters as variables in commands.

**Prerequisites**

The instances on which you want to run a Cloud Assistant command are in the **Running** (Running) state. The Cloud Assistant client is installed on the instances. For more information, see Install the Cloud Assistant client.

**Background information**

When you use the immediate execution feature to create and run a command at the same time, take note of the following items: Only operations administrators, organization administrators, and resource set administrators can create commands. When you encode commands in Base64, the following size limits apply:

| Section | Parameter | Description |
|---|---|---|
| Resource Owner | Organization | Select the organization for which you want to create the command. |
|  | Resource Set | Select the resource set in which you want to create the command. |

Elastic Compute Service If a command is not created by using the immediate execution feature, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run by using the immediate execution feature and is saved, the command cannot exceed 18 KB in size after Base64 encoding. If a command is created and run by using the immediate execution feature but is not saved, the command cannot exceed 24 KB in size after Base64 encoding. You can specify up to 20 custom parameters in a single Cloud Assistant command. You can call an API operation to run a command on up to 50 instances each time. When you create a command, make sure that the syntax, logic, or algorithm that is associated with the command is correct. For example, if you create the /backup directory ( `mkdir /backup` ) on an instance, you can run the following shell command to archive a file in the directory:

```
#!/bin/bash
OF=/backup/my-backup-$(date +%Y%m%d).tgz tar -cf $OF {{file}}
```

**Note**

In the preceding sample command, `{{file}}` is a custom parameter. When you run the command, you can set the custom parameter to the name of the file that you want to archive. Example: /app/usrcredential. You can use custom parameters in scenarios that require dynamic values and values that are shared across multiple commands. We recommend that you specify custom parameters for sensitive data or data that changes together with the environment, such as AccessKey pairs, instance IDs, authorization codes, time parameters, and critical system files.

**Create a command in the ECS console**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant page, click **Create/Run Command**.
Alternatively, click the **ECS Instances** tab, find the ECS instance on which you want to run a command, and click **Run Command** in the Actions column.
5. On the **Create Command** page, configure the parameters. The following table describes
the parameters.

| Command Information | Command Source | Select a command source. Enter Command Content: Create a command. Select Saved Command: Select an existing command. |
|---|---|---|
|  | Command Name | Enter a name for the command. |
|  | Execution Plan | Select a plan on how to run the command. Run Now: The command is immediately run after you click Run or Run and Save. Run on Next System Startup: The command is run the next time the associated instances are started after you click Run or Run and Save. Run on Each System Startup: The command is run each time the associated instances are started after you click Run or Run and Save. |
|  | Command Type | Select a command type. For Linux instances, select Shell. For Windows instances, select Bat or PowerShell. |
|  | Command Content | Enter or paste command content in the field. |
|  | Use Parameters | Specify whether to use custom parameters. If you turn on User Parameters, specify custom parameters in the {{key}} format in the Command Content field. |
|  | Command Parameters | Specify the values of the custom parameters that are in the {{key}} format in the Command Content field. This parameter is available only if you turn on Use Parameters. |
|  | Command Description | Enter a description for the command. We recommend that you enter identifiable information, such as the purpose of the command, to facilitate subsequent management and maintenance. The description must be 1 to 512 characters in length. |

Elastic Compute Service

|  | User | Specify the username that you want to use to run the command on instances. The specified username must exist on the selected instances. We recommend that you run the command as a regular user to reduce security risks. By default, Cloud Assistant commands are run by the root user on Linux instances and by the system user on Windows instances. |
|---|---|---|
|  | Execution Path | Specify an execution path for the command. Different default execution paths are provided based on the operating systems of the instances on which the command is run. For Linux instances, the default execution path is the /home directory of the root user. For Windows instances, the default execution path is the directory in which the Cloud Assistant client process resides, such as C:\Windows\System32\. The execution path must be 1 to 200 characters in length. |
|  | Timeout Period | Specify a timeout period for running the command on instances. If the task that runs the command times out, Cloud Assistant forcefully terminates the task process. Unit: seconds. The value must be an integer that is greater than 10. Default value: 60. Valid values: 10 to 86400. 86,400 seconds is equivalent to 24 hours. Note If you set Timeout Period to a value that is less than 10, the system changes the value to 10 to ensure that the task that runs the command can be completed. |
| Instances | Instance ID/Name | Select the instances on which you want to run the command. |

Elastic Compute Service
6. (Optional) In the **CLI Command** section, you can view the executable CLI commands that
are generated based on the execution parameters and the selected instances. In the lower part of the page, click **Copy CLI Command**. Then, use the Alibaba Cloud command line tool to run the generated commands.
7. Click **Save**, **Run and Save**, or **Run**.
**Save**: Save the command without running the command.
**Run and Save**: Save and run the command.
**Run**: Run the command without saving the command.
8. View the command execution result.
i. Click the **Command Execution Results** tab. ii. Use the search box to search for command execution results that meet the requirements.

| Parameter | Example | Description |
|---|---|---|
| RegionId | cn-qingdao-****-d01 | The ID of the region in which you want to create the command. |
| Name | update | The command name. |
| Username | root | The username that you want to use to run the command on ECS instances. |
| Type | RunShellScript | The type of the command. For Linux instances, set the value to RunShellScript. For Windows instances, set the value to RunBatScript or RunPowershellScript. |
| CommandContent | eXVtIHVwZGF0ZSAte Q== | The Base64-encoded content of the command. |
| Timeout | 60 | The timeout period. |
| RepeatMode | Once | The execution plan. |
| ContentEncoding | Base64 | The encoding format. |

Elastic Compute Service iii. Click **View** in the **Actions** column corresponding to a command task to view the command execution details.

**Create a command by using the CLI**

Sample request: Call the RunCommand operation to create and run a Cloud Assistant command named update to update the operating systems of instances.

```
aliyun ecs RunCommand --RegionId 'cn-qingdao-****-d01' \ --Name 'update' --Username 'root' --Type 'RunShellScript' \ --CommandContent 'eXVtIC15IHVwZGF0ZQ==' \ --Timeout '60' --RepeatMode 'Once' --ContentEncoding 'Base64' \ --InstanceId.1 'i-bp12e0ib2ztibede****'
```

**Note**

The values that are enclosed in single quotation marks ('') are sample values of the parameters. Configure the parameters based on actual scenarios. The following table describes the parameters.

| InstanceId.1 | i- bp12e0ib2ztibede**** | The ID of ECS instance N on which you want to run the command. In this example, the value of N is 1. |
|---|---|---|

Elastic Compute Service For more information, see **CreateCommand** in the **ECS Developer Guide**. Sample success response:

```json
{
        "CommandId": "c-hz018qlm868****",
        "InvokeId": "t-hz018qlm86d****",
        "RequestId": "1D24FA80-64DB-4842-AB20-2520799****"
}
```

##### Run a command

After you create a Cloud Assistant command, you can run it on one or more Elastic Compute Service (ECS) instances. The execution status and results of the command on multiple instances do not affect each other.

**Prerequisites**

Before you run a Cloud Assistant command on ECS instances, make sure that the instances meet the following requirements: The instances are in the **Running** ( `Running` ) state. The Cloud Assistant client is installed on the instances. For more information, see Install the Cloud Assistant client.

**Important**

Only operations administrators, organization administrators, and resource set administrators can run Cloud Assistant commands. If you select more than 50 instances to run a command in the ECS console, the system runs the command on the instances in batches.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Commands tab, find the Cloud Assistant command that you want to run and click
**Run** in the **Actions** column.
Use the search box to search for commands that meet your requirements.
5. On the **Run Command** page, configure the parameters to run the command.

| Parameter | Description |
|---|---|
| Execution Plan | Specify when to run the command. Run Now: The command is run immediately after you click Run or Run and Save. Run on Next System Startup: The command is run the next time the selected instances are started after you click Run or Run and Save. Run on Each System Startup: The command is run each time the selected instances are started after you click Run or Run and Save. |
| Command Content | Confirm the command content in the Command Content field. |
| Command Parameters | In the Command Parameters field, enter the values of the custom parameters specified in the command. No format limits apply to the data types of values for the custom parameters. If the current task does not require values for the custom parameters, you can leave the parameters empty. Note If you did not select Use Parameters when you create the command, Command Parameters is not displayed on the Run Command page. |
| User | Specify the username that you want to use to run the command on ECS instances. The specified username must exist on the selected instances. To reduce security risks, we recommend that you run the command as a regular user. By default, Cloud Assistant commands are run by the root user on Linux instances and by the system user on Windows instances. |

Elastic Compute Service i. In the **Command Information** section, check the command content and configure the parameters. The following table describes the parameters. ii. In the **Instances** section, select one or more instances on which you want to run the command.
6. (Optional) In the **CLI Command** section, you can view the executable CLI commands
generated based on the execution parameters and the selected instances. In the lower part of the page, click **Copy CLI Command**. Then, use Apsara Stack CLI to run the generated commands.
7. Click **Run**.
8. View the command execution result.
i. Click the **Command Execution Results** tab. ii. Use the search box to search for command execution results that meet the requirements. iii. Click **View** in the **Actions** column corresponding to a command task to view the command execution details.

| Parameter | Example | Description |
|---|---|---|
| RegionId | cn-qingdao-****-d01 | The ID of the region in which to run the command. |
| InstanceId.1 | i- bp1f4f6o8lv0wqof**** | The ID of the first instance on which to run the command. |
| InstanceId.2 | i- bp137qu6142s3mhm* *** | The ID of the second instance on which to run the command. |
| CommandId | c-hz018qp243j**** | The command ID. |

Elastic Compute Service

**Run a Cloud Assistant command by using Apsara Stack CLI**

1. **(Optional)** Check the status of the instances on which you want to run a command. If an
instance is not in the **Running** ( `Running` ) state, call the StartInstance operation to start the instance.

```
aliyun ecs StartInstance --InstanceId 'i-bp1f4f6o8lv0wqof****'
```

**Note**

Values enclosed in single quotation marks ('') are example values of the parameters. You must configure the parameters based on actual conditions. For more information, see the **StartInstance** topic in the **ECS Developer Guide**.
2. **(Optional)** Call the DescribeCloudAssistantStatus operation to check whether the Cloud
Assistant client is installed on the instances.

```
aliyun ecs DescribeCloudAssistantStatus --RegionId 'cn-qingdao-****-d01' \ --InstanceId.1 'i-bp1f4f6o8lv0wqof****'
```

If the value of the `CloudAssistantStatus` parameter is true in the response, the Cloud Assistant client is installed on the instances.
3. Call the InvokeCommand operation to run a created Cloud Assistant command on the
instances and obtain the value of the **InvokeId** parameter in the response.

```
aliyun ecs InvokeCommand --RegionId 'cn-qingdao-****-d01' \ --InstanceId.1 'i-bp1f4f6o8lv0wqof****' \ --InstanceId.2 'i-bp137qu6142s3mhm****' \ --CommandId 'c-hz018qp243j****' \ --Timed 'false' \ --output cols=InvokeId
```

| Timed | false | Specify whether to periodically run the command. If you want to periodically run a command, set Timed to true. The Frequency parameter specifies the execution cycle. For example, you can set Frequency to 0 */20 * * * * to run the command every 20 minutes. For more information, see Cron expressions. |
|---|---|---|

| Parameter | Description |
|---|---|
| Destination Operating System | Select the operating system of the ECS instances to which you want to send files. Valid values: Linux Operating System Windows Operating System |

Elastic Compute Service For more information, see the **InvokeCommand** topic in the **ECS Developer Guide**.

##### Upload files to ECS instances

This topic describes how to use Cloud Assistant Agent to upload files such as configuration files and scripts to Elastic Compute Service (ECS) instances.

**Prerequisites**

The ECS instances are in the **Running** (Running) state. Cloud Assistant Agent is installed on the instance. For more information, see Install the Cloud Assistant client. You can call an API operation to send a file to up to 50 instances at a time. The uploaded file is encoded in Base64. The size of the encoded file cannot exceed 32 KB. If you want to upload files that are larger than 32 KB in size or if you want to download files from ECS instances, we recommend that you use the FileZilla tool over the SSH File Transfer Protocol (SFTP) and port 22.

**Important**

Only operations administrators, organization administrators, and resource set administrators can upload files to ECS instances.

**Procedures**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant page, click **Send File**.
5. In the **Command Information** section, configure the parameters described in the
following table.

| File Content | Select a method that you want to use to upload the file. Valid values: Upload File: You can click Upload File to select a file or drag a file to the Upload File section. Paste File Content: You can paste the file content to the field. Note The uploaded file is encoded in Base64. The size of the encoded file cannot exceed 32 KB. |
|---|---|
| File Name | Specify a name for the file. Note If you turn off Overwrite, make sure that the file name is unique across the destination path of the ECS instances. |
| Destination Path | Specify the destination path to save the file. The following path is used by default: Default value when Destination Operating System is set to Linux Operating System: /root Default value when Destination Operating System is set to Windows Operating System: C:/Users/Administrator/Documents You can enter only absolute path in the field. |
| File Description | Specify a description for the file. |
| User | Specify the user to which the file belongs. This parameter is required only for Linux instances. |
| User Group | Specify the user group to which the file belongs. This parameter is required only for Linux instances. |
| Permissions | Configure permissions on the file. Default value: 0644 . This value indicates that the file owner has read and write permissions on the file, and that other users in the same user group as the file owner and public users have read permissions on the file. Note You can configure this parameter in the same manner as you configure the chmod command. This parameter is required only for Linux instances. |
| Overwrite | Specify whether to overwrite the file that has the same name as the uploaded file in the destination path. |
| Timeout Period | Set the timeout period for the file sending task. When the file sending task times out, Cloud Assistant forcefully stops the task process. Unit: seconds. Valid values: 10 to 86400. Default value: 60. |

Elastic Compute Service

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization to which the instance belongs. |
| Resource Set | Yes | Select the resource set to which the instance belongs. |
| Instances | Yes | Select the instances to which you want to send the file. |

Elastic Compute Service
6. In the **Instances** section, select the instances to which you want to send the file and
configure the parameters described in the following table.
7. Click **Run**.

**View the execution results of file sending tasks**

View the execution results of the file sending task.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant page, click the File Sending Results tab.
5. In the task list, view the execution state, execution ID, and destination path of the file
sending task. You can perform the following operations in the Actions column that corresponds to the file sending task: Click **View** to view the execution results of the task on each instance. Click **Export** to export the execution results of the task. Click **Resend** to execute the task again.

##### Clone a command

You can clone an existing Cloud Assistant command to create a new command. You can retain all the information of the original command (cloned command) or modify information such as the name, description, type, content, execution path, or timeout period in the new command (command clone).

**Procedure**

**Important**

Only operations administrators, organization administrators, and resource set administrators can clone commands.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the Cloud Assistant command that you want to clone and click **Clone** in the **Actions**
column.
5. On the **Clone Command** page, configure the parameters that are described in the
following table

| Section | Parameter | Description |
|---|---|---|
| Resource Owner | Organization | Select an organization for the new command. |
|  | Resource Set | Select a resource set for the new command. |
| Command Information | Command Name | Enter a name for the new command. |
|  | Execution Plan | Select a plan on how to run the new command. Run Now: The command is immediately run after you click Run or Run and Save. Run on Next System Startup: The command is run the next time the associated instances are started after you click Run or Run and Save. Run on Each System Startup: The command is run each time the associated instances are started after you click Run or Run and Save. |
|  | Command Type | Select a command type. For Linux instances, select Shell. For Windows instances, select Bat or PowerShell. |
|  | Command Content | Edit or paste the command content. |
|  | Command Description | Enter a description for the new command. We recommend that you enter identifiable information, such as the purpose of the command, to facilitate management and maintenance. |
|  | Execution Path | Specify an execution path for the new command. Default execution paths for instances that use different operating systems: For Linux instances, the default execution path is the /home directory of the root user. For Windows instances, the default execution path is the directory where the process of the Cloud Assistant client is located. Example: C:\ProgramData\aliyun\assist\$(version). |
|  | Timeout Period | Specify a timeout period for the new command to run on instances. If a task that runs the command times out, Cloud Assistant forcefully terminates the task process. Unit: seconds. Default value: 60. Minimum value: 10. If you set Timeout Period to a value of less than 10, the system changes the value to 10 to ensure that the command can be run. |

Elastic Compute Service
6. Click **Save**.

##### Delete a command

The number of Cloud Assistant commands that you can have within each Alibaba Cloud region is limited. To ensure a sufficient command quota, we recommend that you regularly delete commands that are no longer needed.

| Field | Required | Valid value range | Special character |
|---|---|---|---|
| Second | Yes | [0, 59] | * , - / |
| Minute | Yes | [0, 59] | * , - / |
| Hour | Yes | [0, 23] | * , - / |
| Day | Yes | [1, 31] | * , - / ? L W |
| Month | Yes | [1, 12] or [JAN, DEC] | * , - / |
| Week | Yes | [1, 7] or [MON, SUN]. If you use the [1, 7] format, 1 indicates Monday and 7 indicates Sunday. | * , - / ? L # |

Elastic Compute Service

**Procedure**

**Important**

Only operations administrators, organization administrators, and resource set administrators can delete commands.
1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Maintenance & Monitoring > ECS Cloud**
**Assistant**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the Cloud Assistant command that you want to delete and click **Delete** in the **Actions**
column.
5. In the message that appears, click **Delete**.

#### Cron expression

When you run a Cloud Assistant command, you can call an API operation and use the Timed and Frequency parameters to set when to run the Cloud Assistant command. The value of the Frequency parameter is a cron expression. This parameter specifies the frequency of scheduled tasks, frequency of routine maintenance, and the point in time at which to complete a one-time task.

**Introduction**

A cron expression is a string that represents time. The string consists of five spaces and six fields, which is in the `X X X X X X X` format. X is a placeholder of a field. If a field contains multiple values, the values are separated with commas (,). Each field can be a specific value or special characters that have logical representations.

**Field values**

The following table describes valid values and supported special characters for each field in cron expressions.

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
| W | The weekday that is nearest to the specified day of the month. The weekday that the W character indicates is in the same month as the specified day of the month. LW indicates the last weekday of the specified month. | If 5W is specified in the Day field and the 5th day of the month falls on Saturday, the task is triggered on Friday, which is the 4th day of the month. If the 5th day of the month falls on Sunday, the scheduled task is triggered on Monday, which is the 6th day of the month. If the 5th day of the month falls on a weekday, the scheduled task is triggered on the 5th day of the month. |
| # | A specific day of a specific week in every month. Only the Day of a week field supports this character. | In the Week field, 4#2 indicates the second Thursday of a month. |

| Example | Limit |
|---|---|

Elastic Compute Service

**Examples**

The following table describes some example values of cron expressions.

| 0 15 10 ? * * | Executes the task at 10:15 every day. |
|---|---|
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
| 0 15 10 ? * 6#3 | Executes the task at 10:15 on the third Saturday of every month. |
| 0 10,44 14 ? 3 WED | Executes the task at 14:10 and 14:44 every Wednesday in March every year. |

| Resource | Supported operation |
|---|---|
| ECS instances | Start ECS instances, stop ECS instances, restart ECS instances, connect remotely to ECS instances through VNC, connect remotely to ECS instances, and view monitoring data |
| Cloud disks | Modify release behavior, execute automatic snapshot policies, attach disks, and detach disks |

Elastic Compute Service

### ECS quick operations

Elastic Compute Service (ECS) quick operations provide a scenario-based operation experience, allowing you to quickly define and perform operations, directly access corresponding operation entries, and maximize management efficiency. ECS quick operations only support the following operations on the following resources.

| ECS recycle bin | Restore data and permanently delete data |
|---|---|
| Elastic network interfaces (ENIs) | Modify an ENI, bind an ENI to an instance, and unbind an ENI from an instance |
| Security groups | Configure rules and manage ENIs |

Elastic Compute Service
1. Log on to the ECS console.
2. In the lower-right corner of any page in the ECS console, click the following icon to perform
quick operations.

**Scenarios**

**Scenario 1: Search by ECS resource type and then quickly click**

**the operation for O&M management**

This example demonstrates how to perform operations on an ECS instance. You can perform operations on other ECS resources by following a similar procedure.
1. On the entry page for ECS quick operations, search for an ECS instance.
Keyword fuzzy search, Chinese/English abbreviation matching, and error correction matching are supported. Keywords include instance ID, instance name, instance IP address, instance type, and other instance attributes.
2. Select the resource. The View Details and Operation buttons appear in the lower-right
corner of the quick operation panel. Elastic Compute Service
3. Perform operations on the ECS instance.
Click **View Details** to go to the instance details page. Click **Operation** and then select the operation that you want to perform on the ECS instance.

**Scenario 2: Search by ECS operation type, identify available**

**ECS resources based on the operation type, and perform O&M**

**operations on the instance**

Elastic Compute Service This example demonstrates how to execute a snapshot policy for a cloud disk. You can perform operations on other ECS resources by following a similar procedure.
1. On the entry page for ECS quick operations, search for the operation name, such as
Execute Automatic Snapshot Policy. Keyword fuzzy search is supported.
2. Select the operation. The quick operation panel displays all resources that support the
operation.
3. Select the resource on which you want to perform a quick operation. The **View Details** and
**Execution** buttons appear in the lower-right corner.
Elastic Compute Service
4. Execute the operation.
Click **View Details** to go to the details page of the resource (the cloud disk details page in this example). Click **Execution**. In the dialog box that appears, complete the operation as prompted.

### Off-peak migration events

Elastic Compute Service An off-peak migration event refers to an event where an Elastic Compute Service (ECS) instance cannot be immediately migrated due to heavy loads. In this case, you need to migrate the ECS instance during off-peak hours by submitting an off-peak migration task. Before you perform the migration, you need to determine the off-peak hours of your business, inform your users of the migration event, and provide a recommended migration time period in advance. This facilitates instance migration during off-peak hours and reduces service risks.

**Note**

Prediction for off-peak hours is supported only for instance with periodic workloads. For instances with non-periodic workloads, only migration events are pushed. Recommended migration time periods are not provided.

**Background information**

The off-peak hours and migration time of an instance are determined by the following factors: whether **Automatic Migration Upon Deadline** is enabled in the Apsara Uni-manager Operations Console and whether a **migration time** is specified. When **Automatic Migration Upon Deadline** is enabled:
**If you do not specify the migration time** , the ECS instance is migrated in the last off-
peak window within 12 hours before the migration deadline. If no off-peak window is available within the period, migration is performed at the deadline.
**If you specify the migration time** , the ECS instance is migrated at the specified
migration time. When Automatic Migration Upon Deadline is disabled:
**If you do not specify the migration time** , the ECS instance migration plan expires at
the deadline.
**If you specify the migration time** , the ECS instance is migrated at the specified
migration time.

**Prerequisites**

An off-peak migration task is created in the Apsara Uni-manager Operations Console. For more information, see **Off-peak migration tasks** in **ECS O&M Guide**.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > O&M Events**.
3. Find the event whose **Event Status** is **Inquiring** and click **Migrate** in the **Actions** column.
4. In the dialog box that appears, select **Migrate Now** or **Scheduled Migration** and click
**Migrate**.
If you select Scheduled Migration, you must specify a migration time, which cannot be later than the deadline.

### View asynchronous tasks

In Elastic Compute Service (ECS), importing custom images, exporting custom images, and changing the categories of disks are asynchronous operations. The success of an asynchronous operation indicates only that the request is sent. You can view the progress of the corresponding asynchronous task to obtain the operation results at the earliest opportunity. Elastic Compute Service

**Prerequisites**

A custom image is imported or exported, or the category of a disk is changed. For more information, see Import custom images, Export a custom image, or Change the category of a disk.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > Asynchronous**
**Tasks**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the **Asynchronous Tasks** page, you can view the details of asynchronous tasks that
are executed, including **Task ID**, **Task Name**, **Task Status**, **Progress**, **Creation Time**, and **End Time**. If an asynchronous task is completed, **Completed** is displayed in the **Task Status** column and **100%** in the **Progress** column.

### Check security group rules

You can use security group rules to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances in security groups. However, improperly configured security group rules may cause security risks or problems such as being unable to access instances. This topic describes how to use the security group rules check feature to determine whether a security group allows and denies access as expected.

**Background information**

When you use the security group rules check feature, you must configure the check parameters. The system uses a simulated matching method to check whether the security group rules are configured as expected. This feature can be used to check whether a specific type of inbound or outbound traffic is allowed. You must configure check parameters based on the direction of the access traffic. For inbound access, you must configure the Source Address, Destination Port, Rule Direction, and Protocol Type parameters. For outbound access, you must configure the Destination Address, Destination Port, Rule Direction, and Protocol Type parameters.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring >**
**Troubleshooting**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Configure the check parameters based on the direction of the access traffic.
For example, you can configure the check parameters to check whether a Linux instance that uses port 22 can be accessed by using the `192.168.XX.XX` IP address. The following figure shows the configured check parameters. Elastic Compute Service
5. View check results.

**Note**

Network connectivity is affected by various factors such as the port on which traffic is allowed, the status of the Elastic Network Interface (ENI), the network configurations of the instance, and the network environment of the physical server. A value of Allow in the Check Result column indicates only that traffic on this port is allowed for the security group rule. It does not indicate normal network connectivity. For example, if security group rules are created to allow connections to an instance but public bandwidth is not enabled for the instance, the instance still cannot be connected over the Internet. The following figure shows an example of the check result. In this example, the security group allows connections to the Linux instance that uses port 22 by using the `192.168.XX.XX` IP address.

### View operation logs

Elastic Compute Service Operation logs record the time, location, and operator of operations on Elastic Compute Service (ECS) instances and resources associated with the ECS instances. If you encounter technical issues or faults when you manage or use ECS instances, you can check operation logs to quickly identify issues or faults to improve troubleshooting efficiency. Operation logs can also be used to determine the impact scope of faults and the responsible party.

**Note**

The log data displayed on the **Operation Log** page is provided by **Simple Log Service**
**(SLS)**. By default, the log data of the last seven days is retained. If you want to store
operation records for a longer period of time, you can deliver the operation logs to your storage service. For more information, see **Configurations > Configure log storage**
**settings** in Apsara Uni-manager Operations Console User Guide in the Apsara Stack
Documentation Center.

**Procedure**

1. Log on to the ECS console.
2. In the left-side navigation pane, choose **Maintenance & Monitoring > Operation Logs**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. View operation logs. By default, the system displays all operations performed on the ECS
instances and their related resources in the previous seven days. In the **Advanced Filter** section, you can filter operation records by specifying filter conditions such as **Resource Type**, **Event Type**, **Starting and ending time**, **Resource**
**ID**, and **Operation ID**.
5. Find the operation log that you want to view and click **View** in the **Actions** column to view
the details of the operation log.

### View system logs and

**screenshots**

Elastic Compute Service (ECS) is a virtualized cloud-based service. You cannot capture screenshots of ECS resources or connect the resources to display devices. However, ECS caches system logs of the last start, restart, or shutdown operations of each instance, and you can capture screenshots of the instances in real time. You can use these features to analyze and troubleshoot instance issues, such as unresponsive operating systems, abnormal restart, or instance connection failures.

**Prerequisites**

The ECS instance that you want to view is in the **Running** state. When you use the features, take note of the following items: For Windows instances, you can view only instance screenshots, and you cannot view system logs. You cannot view system logs or screenshots of ECS instances created before January 1, 2018.

**Procedure**

1. Log on to the ECS console.
Elastic Compute Service
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Instances page, find the ECS instance that you want to view and click the
icon in the **Actions** column. In the drop-down list, choose **Operations and**
**Troubleshooting** > **Obtain Instance Screenshot** to view the screenshots or choose
**Operations and Troubleshooting** > **Obtain Instance System Logs** to view the system
logs. Sample screenshot of a Windows instance Sample screenshot of a Linux instance Sample system log of a Linux instance Elastic Compute Service

### Work with Apsara Pilot

Apsara Pilot is an intelligent tool provided by Alibaba Cloud to help you manage and maintain Elastic Compute Service (ECS) instances more efficiently. You can use different features of Apsara Pilot to query resource information, trigger operations, diagnose instances, and request technical support. Apsara Pilot helps you improve your O&M efficiency and user experience. This topic describes how to work with Apsara Pilot and provides some sample conversations. We recommend that you refer to the sample conversations based on your actual business scenario.

**Important**

The results generated by Apsara Pilot cannot be used as the basis for final technical support conclusions or business decisions. Alibaba Cloud shall not be liable for any direct or indirect losses caused by taking actions based on the output of Apsara Pilot. The query results returned by Apsara Pilot are automatically generated by AI models. The results are not guaranteed to be completely accurate and are for reference only. We recommend that you verify the accuracy based on the actual situation.

**Prerequisites**

The capabilities of Apsara Pilot rely on the output of the Apsara Copilot module. Apsara Copilot is configured to display in the console by the platform administrator on the
**Configurations > Custom Settings > AI Assistant Settings** page.

**AI-assisted instance creation**

As an AI assistant, Apsara Pilot provides conversational interactions to guide you step by step on how to create an ECS instance based on the preset business scenario. You do not need to understand the underlying technical details or manually perform complex creation steps.

**How to use the AI-assisted instance creation feature**

1. When you create an instance, an Apsara Copilot-assisted instance creation panel is
displayed on the right side of the Create Instance page. Click **Start**.

| Business Scenario | Sub-scenario |
|---|---|
| Web Application | Traditional Office/Enterprise Website |
|  | Build Application |
|  | Development or Test Environment |
|  | Frontend Server |
|  | Backend Server |
| Databases | Small and Medium-sized Databases |
|  | Large Distributed Databases |
| Data Analysis | Batch Computing |
|  | Real-time Data Analysis |
| AI/Machine Learning | AI Inference |
|  | AI Training |

Elastic Compute Service
2. Select a preset **Business Scenario** and a **Sub-Scenario**, and then click **OK**.
3. You can create the instance through conversational interactions as prompted.

**AI-empowered instance diagnosis**

Apsara Pilot supports AI-powered instance diagnostics: Elastic Compute Service Performs intelligent diagnosis on errors during ECS instance running and analyzes the possible causes. Provides troubleshooting steps and suggestions.

**How to perform AI-empowered instance diagnosis**

In the upper-right corner of the Instances page, click **AI Diagnostics**. The AI Diagnostics section in the upper part of the page displays the average CPU usage and average memory usage of all instances in the organization within the last 24 hours, and the performance analysis and stability analysis scores of all instances. In the upper-right corner of the instance details page, click **AI Diagnostics**. The AI Diagnostics section in the upper part of the page displays the average CPU usage, average memory usage, and total usage of all disks that are attached to the instance within the last 24 hours. This section also displays the health rating, idle resources, performance bottleneck analysis, security analysis, and optimization suggestions for the instance.

**Instance type recommendation**

Apsara Pilot provides best practices and recommended ECS instance types for different businesses.

**How to generate instance type recommendation**

When you create an instance or change instance specifications, click **AI specification**
**recommendation** or **Specification recommendation** below the **Specifications**
parameter. Then, Apsara Pilot recommends an appropriate instance type based on your business requirements. You can click **Choose Now** to select the instance type that you want to use. Elastic Compute Service

**Intelligent resource query**

You can enter a resource ID to query the status, information, and related resources of the resource.

**How to perform intelligent resource query**

In the ECS console, select a resource ID to get its definition. For example, select the ID of an instance and click **Consult Apsara Copilot**. Then, Apsara Copilot queries and returns the status, information, and related resource of the instance.

**Select-to-define feature**

The select-to-define feature explains any term, parameter, or option that you select from the interface.

**Prerequisites**

The select-to-define feature is enabled. To enable this feature, click the icon in the upperright corner of the Apsara Copilot pane and turn on Enable Word Selection.

**How to use the select-to-define feature**

1. Select a term or parameter that you want to know, and click the floating **Consult Apsara**
**Copilot** icon.
Elastic Compute Service
2. Apsara Copilot automatically searches for answers.
nt Elastic Compute Service

## RAM role management

### Attach an instance RAM role

**to an ECS instance**

This topic describes how to attach an instance Resource Access Management (RAM) role to an Elastic Compute Service (ECS) instance.

**Prerequisites**

An instance RAM role is created. For more information, see **Create a custom role** in the
**Apsara Uni-manager User Guide**.
The ECS instance to which you want to attach an instance RAM role is located in a virtual private cloud (VPC). The current user role has the permissions to **authorize access to cloud services** and
**attach RAM roles to ECS instances** . For more information, see **View the details of a**
**role** in the **Apsara Uni-manager User Guide**.
Before you attach an instance RAM role to an ECS instance, take note of the following items: After a RAM role is attached to an instance, the permissions that the RAM role has are granted to the instance. Proceed with caution. An instance RAM role can be attached to a single instance at a time.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to manage and choose
**Attach/Detach RAM Role** in the **Actions** column.
5. In the dialog box that appears, select an existing RAM role and click **OK** to attach the role
to the instance.

### Replace the instance RAM

**role of an ECS instance**

After you attach an instance Resource Access Management (RAM) role to an Elastic Compute Service (ECS) instance, you can replace the role at anytime.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
Elastic Compute Service nt
4. Select an instance to which a RAM role is attached and choose
**Attach/Detach RAM Role** in the **Actions** column.
5. Set **Operation Type** to **Attach**, select a different instance RAM role from the **RAM Role**
drop-down list, and then click **OK** to replace the RAM role.

### Detach an instance RAM role

**from an ECS instance**

After you attach an instance Resource Access Management (RAM) role to an Elastic Compute Service (ECS) instance, you can detach the role from the instance at anytime.

**Procedure**

1. Log on to the ECS console.
2. In the navigation pane on the left, choose **Instances & Images > ECS Instances**.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find an instance to which an instance RAM role is attached and choose
> **Instance**
**Settings > Attach/Detach RAM Role** in the **Actions** column.
5. Set **Operation Type** to **Detach** and click **OK** to detach the role.
