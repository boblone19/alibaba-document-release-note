---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Elastic Compute Service User Guide 20230302"
product_version: "V3.16.2"
doc_version: "20230302"
pdf_pages: 203
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Elastic Compute Service User Guide 20230302.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230221/1/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Elastic%20Compute%20Service%20User%20Guide%2020230302.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Elastic Compute Service User Guide 20230302

## What is ECS?

### Overview

Elastic Compute Service (ECS) is a type of computing service that features elastic processingcapabilities. Compared with physical servers, ECS can be more efficientlymanaged and is more user-friendly. You can create instances, resize disks, and add or release any number of ECS instances at any time based on your business needs. An ECS instance is a virtual computing environment that contains the most basic components of computers such as the CPU, memory, and storage. Users perform operations on ECS instances. Instances are core components of ECS, and operations can be performed on instances by using the ECS console. Other resources such as block storage, images, and snapshots can only be used after they are integrated into ECS instances. For more information, see ECS components. ECS components

### Instance lifecycle

The lifecycle of an ECS instance begins when the instance is created and ends when the instance is released. This topic describes the instance states in the ECS console as well as state attributes and their corresponding instance states in API responses. The following table describes the instance states in the ECS console and their corresponding instance states in API responses.

| State | State attribute | Description | State in an API response |
|---|---|---|---|
| Instance being created | Intermediate | The instance is being created and waiting to start. If an instance remains in this state for an extended period of time, an exception has occurred. | Pending |
| Starting | Intermediate | When you start or restart an instance by using the ECS console or by calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Starting state for an extended period of time, an exception has occurred. | Starting |
| Running | Stable | While an instance is in the Running state, the instance can function normally and can accommodate your business needs. | Running |
| Stopping | Intermediate | When you stop an instance by using the ECS console or by calling an API operation, the instance enters this state before it enters the Stopped state. If an instance remains in the Stopping state for an extended period of time, an exception has occurred. | Stopping |
| Stopped | Stable | An instance enters this state when it is stopped. Instances in the Stopped state cannot provide external services. | Stopped |
| Reinitializing | Intermediate | When you re-initialize the system disk or a data disk of an instance by using the ECS console or calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Reinitializing state for an extended period of time, an exception has occurred. | Stopped |
| Changing system disk | Intermediate | When you replace the system disk of an instance by using the ECS console or by calling an API operation, the instance enters this state before it enters the Running state. If an instance remains in the Changing system disk state for an extended period of time, an exception has occurred. | Stopped |

The following figure shows the transitions between instance states in API responses.

## Instructions

### Restrictions

Learn about restrictions before performing operations on ECS instances. Do not upgrade the kernel or operating system version of an ECS instance. Do not start SELinux for Linux systems except CentOS and RedHat. Do not detach PVDriver. Do not arbitrarily modify the MAC address of the network interface.

### Suggestions

Consider the following suggestions to make more efficient use of ECS: ECS instances with 4 GiB or higher memory must use a 64-bit operating system. 32-bit operating systems have a maximum of 4 GiB of memory addressing. A 32-bit Windows operating system supports a maximum of 4 CPU cores. To ensure service continuity and avoid failover-induced service unavailability, we recommend that you configure service applications to boot automatically at system startup.

### Limits

Before using ECS instances, you must be familiar with the limits of instance families. General limits Windows operating systems support a maximum of 64 vCPUs in instance specifications. ECS instances do not support the installation of virtualization software and secondary virtualization. Sound card applications are not supported. Only GPU instances support virtual sound cards. External hardware devices, such as hardware dongles, USB flash drives, external hard disks, and bank U keys, cannot be directly connected to ECS instances. ECS does not support multicast protocols. If multicasting services are required, we recommend that you use unicast instead. Instance family ga1 To create a ga1 instance, you must use one of the following images pre-installed with drivers: Ubuntu 16.04 with an AMD GPU driver pre-installed Windows Server 2016 English version with an AMD GPU driver pre-installed Windows Server 2008 R2 English version with an AMD GPU driver pre-installed Note: A ga1 instance uses an optimized driver provided by Alibaba Cloud and AMD. The driver is installed in images provided by Alibaba Cloud and is currently unavailable for download. If the GPU driver malfunctions due to improper removal of related components, you need to replace the system disk to restore GPU related functions. Not e This operation causes data loss. If the driver malfunctions because an improper image is selected, you need to replace the system disk to reselect an image with an AMD GPU driver pre-installed. For Windows Server 2008 or earlier, you cannot connect to the VNC after the GPU driver takes effect. The VNC is irresponsive with a black screen or stuck at the splash screen. You can use other methods such as Remote Desktop Protocol (RDP) to access the system. RDP does not support DirectX, OpenGL, or other related applications. You need to install the VNC and a client, or use other supported protocols such as PCOIP and XenDesktop HDX 3D. Instance families gn4, gn5i, and gn5 Bandwidth: If you use an image of Windows Server 2008 R2 for a gn4 instance, you cannot use the Connect to VNC function in the ECS console to connect to the instance after the installed GPU driver takes effect. You need to set the bandwidth to a non-zero value or attach an Elastic IP address to the created instance. Image: If an NVIDIA GPU driver is not required, you can select any image, and then Install the CUDA and GPU drivers for a Linux instance or Install the CUDA and GPU drivers for a Windows instance.

### Notice for Windows users

Before using Windows-based ECS instances, you must consider the following points: Data loss may occur if a local disk is used as the data disk of an instance. We recommend that you use a cloud disk to create your instance if you are not sure about the reliability of the data architecture. Do not close the built-in shutdownmon.exe process. Otherwise, the server may require a longer time to restart. Do not rename, delete, or disable Administrator accounts or it may affect the use of the server. We do not recommend that you use virtual memory. When you modify your computer name, you must synchronize the following key values in the registry. Otherwise, the computer name cannot be modified, causing failure when installing certain third-party programs. The following key values must be modified in the registry:

```
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ActiveComputerName HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
```

### Notice for Linux users

Before using Linux-based ECS instances, you must consider the following points: Do not modify content of the default /etc/issue files under a Linux instance. Otherwise, the custom image created from the instance cannot be recognized, and instances created based on the image cannot start as expected. Do not arbitrarily modify the permissions of each directory in the partition where the root directory is located, especially permissions of /etc, /sbin, /bin, /boot, /dev, /usr, and /lib directories. Improper modification of permissions can cause errors. Do not rename, delete, or disable Linux root accounts. Do not compile or perform any other operations on the Linux kernel. We do not recommend the use of Swap for partitioning. Do not enable the NetWorkManager service. This service conflicts with the internal network service of the system, causing network errors.

### Notice on defense against DDoS

attacks You need to purchase Anti-DDoS Pro to defend against DDoS attacks. For more information, see Apsara Stack Security Product Introduction.

## Quick start

### Overview

This topic describes how to create and connect to an Elastic Compute Service (ECS) instance. Perform the following operations:
1. Create a security group
A security group acts as a virtual firewall to control the inbound and outbound traffic of ECS instances. Each ECS instance must belong to at least one security group. When you create an instance, you must select a security group to control network access of the instance.
2. Create an instance
An ECS instance is a virtual machine that contains the basic computing components of a server, such as CPU, memory, operating system, network settings, and disks. After a security group is created, you can select an instance type to create instances based on your business needs.
3. Connect to an instance
Select a method to connect to an instance based on the network configurations and operating system of the instance and the operating system of your computer. After you connect to the instance, you can perform operations on it such as installing applications.

### Log on to the ECS console

This topic describes how to log on to the ECS console. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.

### Create a security group

Security groups are an important means for network security isolation. They implement network access control for one or more ECS instances. Prerequisites A virtual compute cloud (VPC) is created. For more information, see VPC User Guide. Context Security groups determine whether the instances in the same account that are deployed within the same VPC and region can communicate with each other. By default, if the instances belong to the same security group, they can communicate with each other over the internal network. If the instances belong to different security groups, you can authorize mutual access between the security groups to allow the instances to communicate with each other over the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Securit y Group.
5. Configure the parameters listed in the following table to create a security group.

| Type | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | Select an organization in which to create the security group. Make sure that the security group and the VPC belong to the same organization. |
|   | Resource Set | Yes | Select a resource set in which to create the security group. Make sure that the security group and the VPC belong to the same resource set. |
|   | Region | Yes | Select a region in which to create the security group. Make sure that the security group and VPC belong to the same region. |
|   | Zone | Yes | Select a zone in which to create the security group. |
|   | VPC | Yes | Select a VPC in which to create the security group. |
|   | Security Group Name | No | Enter a name for the security group. The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), hyphens (-), colons (:), and _ commas (,). It cannot start with http:// or https://. |

| stic Compute Serv |   |   |   |
|---|---|---|---|
| Basic Settings Type | Parameter | Required | Description |
|   | Description | No | Enter a description for the security group. To simplify future management operations, we recommend that you provide an informational description. The description must be 2 to 256 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), and commas (,). It cannot start with http:// or https://. |

6. Click Submit .

### Create an instance

An Elastic Compute Service (ECS) instance is a virtual machine that contains the basic computing components of a server, such as CPU, memory, operating system, network settings, and disks. Prerequisites A virtual private cloud (VPC) and a vSwitch are created. For more information, see the "Create a VPC" and "Create a vSwitch" topics in Apsara Stack VPC User Guide. If you want to assign an IPv6 address to the instance that you want to create, make sure that the VPC and vSwitch are associated with IPv6 CIDR blocks. For more information, see the "Enable an IPv6 CIDR block for a VPC" and "Enable an IPv6 CIDR block for a vSwitch" topics in Apsara Stack VPC User Gui de. One or more security groups are available. If no security groups are available, create one. For more information, see Create a security group. Context Some limits apply when you create GPU-accelerated instances. For more information, see Limits.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Inst ance.
5. Configure the parameters described in the following tables.
i. Configure the basic settings of the instance.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select an organization. |
| Resource Set | Yes | Select a resource set. |

ii. Select a region and zone for the instance.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | Select a region. |
| Zone | Yes | Select a zone. Zones are the physical zones with separate power supplies and networks within the same region. The internal networks of zones are connected, and faults in one zone are isolated from the other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |

iii. Configure network settings for the instance.

| Parameter | Required | Description |
|---|---|---|
| Network Type | Yes | Select a network type. Only VPC is supported. |
| VPC | Yes | Select a VPC. |
| vSwitch | Yes | Select a vSwitch. |
| Private IP Address | No | Specify a private IPv4 address for the instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you do not specify a private IP address, the system allocates one to the instance. |
| IPv6 | No | Specify whether to assign an IPv6 address to the instance. |

iv. Configure instance settings such as security group, instance family, and instance type and specify the number of instances that you want to create.

| Parameter | Required | Description |
|---|---|---|
| Security Group | Yes | Select a security group. |
| Deployment Set | No | Select a deployment set. You can use deployment sets to disperse or aggregate the instances involved in your business. |
| User Data | No | In the User Data field, enter the user data to be automatically run on instance startup. Windows supports batch and PowerShell scripts. Before you perform Base64 encoding of user data, make sure that the data to be encoded includes [bat] or [powershell] as the first line. Linux supports shell scripts. |
| Quantity | Yes | Specify the number of instances that you want to create. The number must be an integer within the range of 1 to 100. |
| Instance Family | Yes | Select an instance family. After you select an instance family, you must select an instance type. |
| Instance Type | Yes | Select an instance type. Information such as CPU, memory, and instance family level are displayed in the Instance Type list. Select an instance type based on your business needs. Instance types that have specific CPU and memory combinations do not support Windows Server images. For more information, see the "Limits" topic in ECS Product Introduction. |

v. Configure the image to be used by the instance.

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image, Cust om Image, and Shared Cust om Image. |

| Parameter | Required | Description |
|---|---|---|
| Public Image | Subject to the image type | Select a public image. Public images provided by Alibaba Cloud are licensed, secure, and stable. Public images include Windows Server images and major Linux images. This parameter is required when you set Image Type to Public Image. When you use an image that supports Dynamic Host Configuration Protocol version 6 (DHCPv6) to create an instance, an IPv6 address is automatically assigned to the instance. The instance can use this IPv6 address to communicate over the internal network. When you use an image that does not support DHCPv6 to create an instance, you must manually assign an IPv6 address to the instance. The following images support DHCPv6: Linux images: CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images Not e To use an IPv6 address to communicate over the Internet, you must enable public bandwidth for the IPv6 address. For more information, see the "Enable Internet bandwidth for an IPv6 address" topic in Apsara Stack VPC User Guid e. |
| Custom Image | Subject to the image type | Select a custom image. Custom images are created from instances or snapshots or are imported from your device. This parameter is required when you set Image Type to Cust om Image. |
| Shared Custom Image | Subject to the image type | Select a custom image that is shared by another Apsara Stack tenant. This parameter is required when you set Image Type to Shared Cust om Image. |

vi. Configure the storage settings for the instance.

| Parameter | Required | Description |
|---|---|---|
| System Disk | Yes | Select a disk category from the drop-down list and specify the system disk capacity. Valid values for the disk category: Ult ra Disk and St andard SSD. The system disk capacity must range from 20 GiB to 500 GiB. |
| Data Disk | No | You can click Data Disk to create and attach data disks. For each data disk, select a disk category from the drop-down list and specify the disk capacity. Valid values for the disk category: Ult ra Disk and St andard SSD. A maximum of 16 data disks can be attached to an instance. The maximum capacity of each data disk is 32 TiB. You can optionally select Release wit h Inst ance and Encrypt ion for each data disk. To encrypt a data disk, configure the following parameters: Encrypt ion Met hod: Select AES256. Encrypt ion Key: You can select a key created in Key Management Service (KMS). You can also add data disks after the instance is created. For more information, see Create a disk. |

vii. Configure the logon password settings for the instance.

| Parameter |   | Required | Description |   |   |
|---|---|---|---|---|---|
| Password Setting |   | Yes | Specify when to set a password. Valid values: Set Now and Set Af t er Purchase. If you select Set After Purchase, you can use the password reset feature to set a password after the instance is created. For more information, see Change the logon password of an instance. Not e The password is used to log on to the instance, not to a VNC management terminal. |   |   |
| Logon Password |   | No | Set the password to be used to log on to the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ` ~ ! @#$%^&*- +=\|{}[]:;'<>,. _ ?/ Not e This parameter is required when you set Password Set t ing to Set Now. |   |   |
|   |   |   |   | ( ) ` ~ ! @#$%^&*- +=\|{}[]:;'<>,. _ |   |
|   |   |   | ?/ |   |   |
| Confirm Password |   | No | Enter the password again. Not e This parameter is required when you set Password Set t ing to Set Now. |   |   |

viii. (Optional) Enter a name for the instance. The name must be 2 to 128 characters in length and can contain `hyphens (-), underscores (_),` `and colons (:)` . It must start with a letter and cannot start with `http://` or `https://` .

| h | http:// | or | https:// |
|---|---|---|---|

If you do not specify a name, the system assigns one at random.
6. Click Submit .
Result The new instance appears in the instance list. When the instance is being created, it is in the Preparing state. When the instance is created, it enters the Running state.

### Connect to an instance

#### Instance connecting overview

After an instance is created, you can connect to the instance to perform operations such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that have public IP addresses. For more information about the procedure, see the following topics: Connect to a Linux-based instance by using SSH commands in Linux or Mac OS X Connect to a Linux-based instance by using remote connection tools in Windows Connect to a Windows-based instance by using RDP Use the VNC feature in the ECS console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator, and that of a Linux instance is root.

#### Connect to a Linux instance by using SSH

commands in Linux or Mac OS X This topic describes how to use SSH commands to connect to a Linux instance. Prerequisites The instance and the security group are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

| Rule direction | Authorizati on policy | Protocol type | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Accept | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

1. Enter the following command and press the Enter key.

```
ssh root@instance IP
```

2. Enter the instance password of the root user and press the Enter key.

#### Connect to a Linux-based instance by using

remote connection tools in Windows This topic describes how to connect to an instance by using the PuTTY tool. Prerequisites Remote connection tools are designed with similar logics. In this example, PuTTY is used to connect to an instance. Download PuTTY at the following URL: .
1. Download and install PuTTY for Windows.
2. Start the PuTTY client and complete the following settings:
Host Name (or IP Address): Enter the EIP of the instance to be connected. Port: Select the default port 22. Connection Type: Select SSH. Saved Session: Enter the name of the session. Click Save. After the settings are saved, PuTTY remembers the name and IP address of the instance. This eliminates the need to enter them every time you connect to the instance.
3. Click Open to connect to the instance.
When you connect to the instance for the first time, PuTTY displays security alerts. Click Yes to proceed.
4. Enter the username root and press Enter.
5. Enter the password for the instance and press Enter.
If a message similar to the following one appears, a connection to the instance is established.

```
Welcome to aliyun Elastic Compute Server!
```

#### Connect to a Windows instance by using

RDC This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC). Prerequisites A security group and a Windows instance are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

| Rule direction | Action | Protocol | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 addresses | 0.0.0.0/0 |

1. Use one of the following methods to enable RDC:
Click St art , enter mstsc in the search box, and click mst sc in the search result. Press the Windows logo key+R. In the Run dialog box that appears, enter mstsc and click OK.
2. In the Remot e Deskt op Connect ion dialog box, enter the Elastic IP address of the instance and
click Show Opt ions.
3. Enter the username.
The default username is administrator.
4. (Optional)If you do not want to enter the password upon subsequent logons, select Allow me t o
save credent ials.
5. Click Connect .
6. In the Windows Securit y dialog box that appears, enter the password corresponding to the
username you entered and click OK. Result If the Windows desktop appears, a connection to the Windows instance is established. If an error message is returned indicating that an authentication error has occurred and the function requested is not supported, install CredSSP updates and try again. Follow these steps to install the updates:
1. Connect to an ECS instance by using the VNC.
2. Choose St art > Cont rol Panel.
3. Click Syst em and Securit y.
4. Click Check f or updat es in the Windows Updat es section.
5. If updates are available, click Inst all updat es.
6. Restart the instance.

#### Connect to an instance by using a VNC

management terminal If other remote connection tools such as PuTTy, Xshell, and SecureCRT are not installed or do not work properly, you can access your instances by using a VNC management terminal in the ECS console. Prerequisites The instance to which you want to connect is in the Running state. The root certificate is imported to your web browser. For more information, see Install the certificate for VNC in Windows. The VNC password is reset if it is your first time to connect to the instance after the instance is created. For more information, see Change the VNC password. Context The VNC password is used to log on to a VNC management terminal in the ECS console, whereas the instance password is used to log on to the instance. You can use a VNC management terminal to connect to an instance to solve specific issues. The following table lists some of the issues.

| Issue | Solution |
|---|---|
| The instance starts slowly due to self-check on startup. | Check the self-check progress. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear and consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to connect and click Remot e Connect ion in the Act ions
column.
5. Enter the VNC password and click OK.
After you are logged on to the VNC management terminal, a logon page similar to the following one appears.
6. Enter your username and password.
Fo a Linux instance, enter the username root and the logon password. Not e Passwords in Linux are not displayed as you type. Press the Enter key after you enter the password. For a Windows instance, to use a key combination such as Ctrl+Alt+Delete, click the List icon in the upper-right corner of the VNC page and select the corresponding key combination from the dropdown list. Enter the username and password as prompted, and click the Log On icon such as .

## Instances

### Overview

An Elastic Compute Service (ECS) instance is a virtual server that includes basic components such as CPUs, memory, an operating system (OS), network configurations, and disks. You can use management tools provided by Alibaba Cloud such as the ECS console and ECS API to create and manage ECS instances. You can manage the status of ECS instances and their deployed applications in the same manner as you would do with local servers. You can also upgrade the capabilities (such as compute and storage capabilities) of your ECS instances as your requirements increase. Basic instance configurations The following basic configurations of ECS instances determine the basic resources that the instances require: Instance types Instance types define the basic attributes of ECS instances, such as compute capacity, storage capacity, and networking capacity. Instance types must be used together with images, Elastic Block Storage (EBS) devices, and network resources to create ECS instances that serve different purposes. ECS provides a variety of instance families for typical use scenarios. Each instance family consists of multiple instance types that have different compute capabilities and are suited to different scenarios and requirements. Images Images contain the information necessary to run ECS instances, such as OSs and initialization data of applications. Alibaba Cloud provides ready-to-use images for Windows Server and several mainstream Linux OSs. You can also create or import your own images to save time in making repeated configurations. Storage ECS instances use their attached system disks and data disks for storage. Each instance must have a system disk attached. The first time the instance starts, the OS is installed and instance configurations are initialized based on the system disk image. Cloud disks can be used as system disks or data disks. Local disks can be used only as data disks and are available only for specific instance types, such as instance types with local HDDs. If you want your instances to have more storage space, you can resize their attached cloud disks or attach more cloud disks after the instances are created. For more information, see Create a disk and Attach a disk. Business data is an important asset. Cloud disks use a triplicate mechanism to ensure the durability of data. To ensure that your data remains available, we recommend that you back up your data on a regular basis. You can create snapshots of cloud disks to back up disk data. If you are using local disks, you must implement data redundancy at the application layer to ensure data availability. In addition to basic configurations, you can also configure network configurations, security groups, and OSs for instances. For more information, see Create an instance. Security suggestions When you use Apsara Stack services, we recommend that you follow security suggestions to improve resource security, such as the following ones: Suggestions for permission control: Use the Enterprise Permissions features to control which users can manage resources such as instances and what permissions to grant to the users. Suggestions for security features: Use security features such as security hardening and cloud disk encryption to ensure the security of data and runtime environments. Suggestions for network security: Use virtual private clouds (VPCs) to isolate services of different security levels. Use security groups to control inbound and outbound traffic for instances and allow instances access to the Internet only when required to minimize the attack surface area of resources.

### Create an instance

An Elastic Compute Service (ECS) instance is a virtual machine that contains the basic computing components of a server, such as CPU, memory, operating system, network settings, and disks. Prerequisites A virtual private cloud (VPC) and a vSwitch are created. For more information, see the "Create a VPC" and "Create a vSwitch" topics in Apsara Stack VPC User Guide. If you want to assign an IPv6 address to the instance that you want to create, make sure that the VPC and vSwitch are associated with IPv6 CIDR blocks. For more information, see the "Enable an IPv6 CIDR block for a VPC" and "Enable an IPv6 CIDR block for a vSwitch" topics in Apsara Stack VPC User Gui de. One or more security groups are available. If no security groups are available, create one. For more information, see Create a security group. Context Some limits apply when you create GPU-accelerated instances. For more information, see Limits.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Inst ance.
5. Configure the parameters described in the following tables.
i. Configure the basic settings of the instance.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select an organization. |
| Resource Set | Yes | Select a resource set. |

ii. Select a region and zone for the instance.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | Select a region. |
| Zone | Yes | Select a zone. Zones are the physical zones with separate power supplies and networks within the same region. The internal networks of zones are connected, and faults in one zone are isolated from the other zones. To increase the availability of your applications, we recommend that you create instances in different zones. |

iii. Configure network settings for the instance.

| Parameter | Required | Description |
|---|---|---|
| Network Type | Yes | Select a network type. Only VPC is supported. |
| VPC | Yes | Select a VPC. |
| vSwitch | Yes | Select a vSwitch. |
| Private IP Address | No | Specify a private IPv4 address for the instance. The private IPv4 address must be within the CIDR block of the selected vSwitch. If you do not specify a private IP address, the system allocates one to the instance. |
| IPv6 | No | Specify whether to assign an IPv6 address to the instance. |

iv. Configure instance settings such as security group, instance family, and instance type and specify the number of instances that you want to create.

| Parameter | Required | Description |
|---|---|---|
| Security Group | Yes | Select a security group. |
| Deployment Set | No | Select a deployment set. You can use deployment sets to disperse or aggregate the instances involved in your business. |
| User Data | No | In the User Data field, enter the user data to be automatically run on instance startup. Windows supports batch and PowerShell scripts. Before you perform Base64 encoding of user data, make sure that the data to be encoded includes [bat] or [powershell] as the first line. Linux supports shell scripts. |
| Quantity | Yes | Specify the number of instances that you want to create. The number must be an integer within the range of 1 to 100. |
| Instance Family | Yes | Select an instance family. After you select an instance family, you must select an instance type. |
| Instance Type | Yes | Select an instance type. Information such as CPU, memory, and instance family level are displayed in the Instance Type list. Select an instance type based on your business needs. Instance types that have specific CPU and memory combinations do not support Windows Server images. For more information, see the "Limits" topic in ECS Product Introduction. |

v. Configure the image to be used by the instance.

| Parameter | Required | Description |
|---|---|---|
| Image Type | Yes | Select an image type. Valid values: Public Image, Cust om Image, and Shared Cust om Image. |

| Parameter | Required | Description |
|---|---|---|
| Public Image | Subject to the image type | Select a public image. Public images provided by Alibaba Cloud are licensed, secure, and stable. Public images include Windows Server images and major Linux images. This parameter is required when you set Image Type to Public Image. When you use an image that supports Dynamic Host Configuration Protocol version 6 (DHCPv6) to create an instance, an IPv6 address is automatically assigned to the instance. The instance can use this IPv6 address to communicate over the internal network. When you use an image that does not support DHCPv6 to create an instance, you must manually assign an IPv6 address to the instance. The following images support DHCPv6: Linux images: CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images Not e To use an IPv6 address to communicate over the Internet, you must enable public bandwidth for the IPv6 address. For more information, see the "Enable Internet bandwidth for an IPv6 address" topic in Apsara Stack VPC User Guid e. |
| Custom Image | Subject to the image type | Select a custom image. Custom images are created from instances or snapshots or are imported from your device. This parameter is required when you set Image Type to Cust om Image. |
| Shared Custom Image | Subject to the image type | Select a custom image that is shared by another Apsara Stack tenant. This parameter is required when you set Image Type to Shared Cust om Image. |

vi. Configure the storage settings for the instance.

| Parameter | Required | Description |
|---|---|---|
| System Disk | Yes | Select a disk category from the drop-down list and specify the system disk capacity. Valid values for the disk category: Ult ra Disk and St andard SSD. The system disk capacity must range from 20 GiB to 500 GiB. |
| Data Disk | No | You can click Data Disk to create and attach data disks. For each data disk, select a disk category from the drop-down list and specify the disk capacity. Valid values for the disk category: Ult ra Disk and St andard SSD. A maximum of 16 data disks can be attached to an instance. The maximum capacity of each data disk is 32 TiB. You can optionally select Release wit h Inst ance and Encrypt ion for each data disk. To encrypt a data disk, configure the following parameters: Encrypt ion Met hod: Select AES256. Encrypt ion Key: You can select a key created in Key Management Service (KMS). You can also add data disks after the instance is created. For more information, see Create a disk. |

vii. Configure the logon password settings for the instance.

| Parameter |   | Required | Description |   |   |
|---|---|---|---|---|---|
| Password Setting |   | Yes | Specify when to set a password. Valid values: Set Now and Set Af t er Purchase. If you select Set After Purchase, you can use the password reset feature to set a password after the instance is created. For more information, see Change the logon password of an instance. Not e The password is used to log on to the instance, not to a VNC management terminal. |   |   |
| Logon Password |   | No | Set the password to be used to log on to the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ` ~ ! @#$%^&*- +=\|{}[]:;'<>,. _ ?/ Not e This parameter is required when you set Password Set t ing to Set Now. |   |   |
|   |   |   |   | ( ) ` ~ ! @#$%^&*- +=\|{}[]:;'<>,. _ |   |
|   |   |   | ?/ |   |   |
| Confirm Password |   | No | Enter the password again. Not e This parameter is required when you set Password Set t ing to Set Now. |   |   |

viii. (Optional) Enter a name for the instance. The name must be 2 to 128 characters in length and can contain `hyphens (-), underscores (_),` `and colons (:)` . It must start with a letter and cannot start with `http://` or `https://` .

| h | http:// | or | https:// |
|---|---|---|---|

If you do not specify a name, the system assigns one at random.
6. Click Submit .
Result The new instance appears in the instance list. When the instance is being created, it is in the Preparing state. When the instance is created, it enters the Running state.

### Connect to an instance

#### Instance connecting overview

After an instance is created, you can connect to the instance to perform operations such as installing applications. You can use one of the following methods to connect to an instance: Use remote connection tools to connect to instances that have public IP addresses. For more information about the procedure, see the following topics: Connect to a Linux-based instance by using SSH commands in Linux or Mac OS X Connect to a Linux-based instance by using remote connection tools in Windows Connect to a Windows-based instance by using RDP Use the VNC feature in the ECS console. For more information, see Connect to an instance by using a VNC management terminal. The username of a Windows instance is Administrator, and that of a Linux instance is root.

#### Connect to a Linux instance by using SSH

commands in Linux or Mac OS X This topic describes how to use SSH commands to connect to a Linux instance. Prerequisites The instance and the security group are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address (EIP) is bound with the instance. An inbound security group rule is added to the security group to allow the SSH port.

| Rule direction | Authorizati on policy | Protocol type | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Accept | TCP | 22/22 | 1 | IPv4 CIDR block | 0.0.0.0/0 |

1. Enter the following command and press the Enter key.

```
ssh root@instance IP
```

2. Enter the instance password of the root user and press the Enter key.

#### Connect to a Linux-based instance by using

remote connection tools in Windows This topic describes how to connect to an instance by using the PuTTY tool. Prerequisites Remote connection tools are designed with similar logics. In this example, PuTTY is used to connect to an instance. Download PuTTY at the following URL: .
1. Download and install PuTTY for Windows.
2. Start the PuTTY client and complete the following settings:
Host Name (or IP Address): Enter the EIP of the instance to be connected. Port: Select the default port 22. Connection Type: Select SSH. Saved Session: Enter the name of the session. Click Save. After the settings are saved, PuTTY remembers the name and IP address of the instance. This eliminates the need to enter them every time you connect to the instance.
3. Click Open to connect to the instance.
When you connect to the instance for the first time, PuTTY displays security alerts. Click Yes to proceed.
4. Enter the username root and press Enter.
5. Enter the password for the instance and press Enter.
If a message similar to the following one appears, a connection to the instance is established.

```
Welcome to aliyun Elastic Compute Server!
```

#### Connect to a Windows instance by using

RDC This topic describes how to connect to a Windows instance by using Remote Desktop Connection (RDC). Prerequisites A security group and a Windows instance are created. The instance is in the Running state. A logon password is set for the instance. An Elastic IP address is associated with the instance. An inbound security group rule is added to the security group to allow traffic on the RDP port.

| Rule direction | Action | Protocol | Port range | Priority | Authorizati on type | Authorizati on object |
|---|---|---|---|---|---|---|
| Inbound | Allow | tcp | 3389/3389 | 1 | IPv4 addresses | 0.0.0.0/0 |

1. Use one of the following methods to enable RDC:
Click St art , enter mstsc in the search box, and click mst sc in the search result. Press the Windows logo key+R. In the Run dialog box that appears, enter mstsc and click OK.
2. In the Remot e Deskt op Connect ion dialog box, enter the Elastic IP address of the instance and
click Show Opt ions.
3. Enter the username.
The default username is administrator.
4. (Optional)If you do not want to enter the password upon subsequent logons, select Allow me t o
save credent ials.
5. Click Connect .
6. In the Windows Securit y dialog box that appears, enter the password corresponding to the
username you entered and click OK. Result If the Windows desktop appears, a connection to the Windows instance is established. If an error message is returned indicating that an authentication error has occurred and the function requested is not supported, install CredSSP updates and try again. Follow these steps to install the updates:
1. Connect to an ECS instance by using the VNC.
2. Choose St art > Cont rol Panel.
3. Click Syst em and Securit y.
4. Click Check f or updat es in the Windows Updat es section.
5. If updates are available, click Inst all updat es.
6. Restart the instance.

#### Install the certificate for VNC in Windows

Before you log on to the VNC management terminal, you must export the relative certificate from the site such as the Apsara Uni-manager Management Console and install the certificate in your local browser. Context The VNC feature is provided by the VNC proxy service. The VNC proxy service uses a certificate different from that of Apsara Infrastructure Management Framework. The certificate of the VNC proxy service must be manually imported.
1. Export the certificate from the Apsara Uni-manager Management Console.
i. Log on to the Apsara Uni-manager Management Console. Press the F12 key or Fn+F12 to view and select the certificate. For example, in the Chrome browser, press the F12 key to open Chrome DevTools. ii. In the Cert if icat e dialog box, click the Cert if icat e Pat h tab, select the root certificate, and then click View Cert if icat e. iii. In the Cert if icat e dialog box, click the Det ails tab and then click Copy t o File. iv. In the Cert if icat e Export Wizard dialog box, click Next . v. Select DER encoded binary X.509 (.CER) as the format and then click Next . vi. Click Browse, choose where to store the certificate, enter a file name, and then click Save. vii. Click Next . viii. Click Finish. ix. Click OK.
2. Install the certificate in your local browser.
i. Double-click the certificate. ii. In the Cert if icat e dialog box, click Inst all Cert if icat e. iii. In the Cert if icat e Import Wizard dialog box, click Next . iv. Select Place all cert if icat es in t he f ollowing st ore and click Browse. v. In the Select Cert if icat e St ore dialog box, select T rust ed Root Cert if icat e Aut horit y and then click OK. vi. In the Cert if icat e Import Wizard dialog box, click Next . vii. Click Finish. viii. If a security warning message is displayed, click Yes.
3. Restart your browser and log on to the Apsara Uni-manager Management Console.
After the certificate is installed, the security warning message is no longer displayed on the left of the URL when you log on to the Apsara Uni-manager Management Console.

#### Connect to an instance by using a VNC

management terminal If other remote connection tools such as PuTTy, Xshell, and SecureCRT are not installed or do not work properly, you can access your instances by using a VNC management terminal in the ECS console. Prerequisites The instance to which you want to connect is in the Running state. The root certificate is imported to your web browser. For more information, see Install the certificate for VNC in Windows. The VNC password is reset if it is your first time to connect to the instance after the instance is created. For more information, see Change the VNC password. Context The VNC password is used to log on to a VNC management terminal in the ECS console, whereas the instance password is used to log on to the instance. You can use a VNC management terminal to connect to an instance to solve specific issues. The following table lists some of the issues.

| Issue | Solution |
|---|---|
| The instance starts slowly due to self-check on startup. | Check the self-check progress. |
| The firewall of the operating system is enabled by mistake. | Disable the firewall. |
| Abnormal processes appear and consume large amounts of CPU or bandwidth resources. | Troubleshoot and terminate the abnormal processes. |

1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to connect and click Remot e Connect ion in the Act ions
column.
5. Enter the VNC password and click OK.
After you are logged on to the VNC management terminal, a logon page similar to the following one appears.
6. Enter your username and password.
Fo a Linux instance, enter the username root and the logon password. Not e Passwords in Linux are not displayed as you type. Press the Enter key after you enter the password. For a Windows instance, to use a key combination such as Ctrl+Alt+Delete, click the List icon in the upper-right corner of the VNC page and select the corresponding key combination from the dropdown list. Enter the username and password as prompted, and click the Log On icon such as .

### Manage instance status

#### Stop an instance

You can stop instances that are not in use. The stop operation interrupts the services that are running on the instances. Exercise caution when you perform this operation. Prerequisites The instance that you want to stop is in the Running state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to stop instances:
To stop a single instance, find the instance and choose More > Inst ance St at us > St op in the Act ions column. To stop one or more instances at a time, select the instances and click St op in the lower-left corner of the Instances page.
5. Click OK.
Result When the instance is being stopped, its status in the St at us column changes from Running to St opping. After the instance is stopped, its status changes to St opped.

#### Start an instance

You can start stopped instances. Prerequisites The instance that you want to start is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to start instances:
To start a single instance, find the instance and choose More > Inst ance St at us > St art in the Act ions column. To start one or more instances at a time, select the instances and click St art in the lower-left corner of the Instances page.
5. Click OK.
Result When the instance is being started, its status in the St at us column changes from St opped to St art ing. After the instance is started, its status changes to Running.

#### Restart an instance

You must restart instances after you change their logon passwords or install system updates for the instances. The restart operation stops the instances for a period of time. This causes the services that are running on the instances to be interrupted. Exercise caution when you perform this operation. Prerequisites The instance that you want to restart is in the Running state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to restart instances:
To restart a single instance, find the instance and choose More > Inst ance St at us > Rest art in the Act ions column. To restart one or more instances at a time, select the instances and click Rest art in the lower-left corner of the Instances page.
5. In the Restart Instance dialog box, select a restart mode.
Rest art : restarts the instances normally. Force Rest art : forcibly restarts the instances. This may result in loss of unsaved data.
6. Click OK.

#### Delete an instance

You can delete instances that are no longer needed to release their resources. Deleted instances cannot be recovered. We recommend that you back up data before you delete instances. If data disks are released along with instances, the data on the disks cannot be recovered. Prerequisites The instance to be deleted is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select the instance that you want to delete and click Delet e in the lower-left corner of the
Instances page.
5. Click OK.

### Manage instance attributes

#### View instances

You can view the list of instances and the details of individual instances. The details of an instance include basic configurations, disks, snapshots, security groups, and elastic network interfaces (ENIs).
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Instance Name | Enter an instance name to search for the instance. |
| Instance ID | Enter an instance ID to search for the instance. |
| IP Address | Enter the IP address of an instance to search for the instance. |
| VPC ID | Enter a VPC ID to search for instances that belong to the VPC. |
| Image ID | Enter an image ID to search for instances that use the image. |
| Status | Select an instance status to search for instances in that status. Valid values: Running St opped St art ing St opped |
| Security Group ID | Enter a security group ID to search for instances that belong to the security group. |
| Operating System | Enter the name of operating system to search for instances that use the operating system. |

5. Use one of the following methods to go to the Instance Details page of an instance:
In the Inst ance ID/Name column, click the instance ID. Click Manage in the Act ions column corresponding to the instance. Choose More > Show Det ails in the Act ions column corresponding to the instance.

#### Modify an instance

You can modify the names, descriptions, and user data of created instances.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to modify and choose More > Modif y in the Act ions column.
5. Modify the name, description, and user data of the instance.
The name must be 2 to 128 characters in length. The description must be 2 to 256 characters in length. The user data must be 2 to 999 characters in length.
6. Click OK.

#### Change the logon password of an instance

If you did not set a logon password when you created an instance or have forgotten the password, you can reset the password.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose logon password you want to change and use one of the following methods
to go to the Instance Details page. In the Inst ance ID/Name column, click the ID of the instance. Click Manage in the Act ions column. In the Act ions column, choose More > Show Det ails.
5. Click Change Password.
6. Enter and confirm the new password, and then click OK.
The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ' ~ ! @ # $ % ^ & * - _ + = | { } [ ] : ; ' < > , . ? /
7. Restart the instance by using the ECS console or by calling an API operation for the new password to
take effect. For more information, see Restart an instance or the "RebootInstance" topic in ECS Developer Guide.

#### Change the VNC password

If you use Virtual Network Console (VNC) to connect to an Elastic Compute Service (ECS) instance for the first time or if you forget the VNC password, you can reset the VNC password.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose VNC password you want to change and use one of the following methods
to go to the Instance Details page: On the Instances page, click the instance ID in the Inst ance ID/Name column. On the Instances page, click Manage in the Act ions column. On the Instances page, choose More > Show Det ails in the Act ions column.
5. Click Change VNC Password.
6. Enter and confirm the new password, and click OK.
The password must be 8 to 14 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ! / | \@~`#$%^*()_-+={[}]:;,.? . Not e If your instance is a non-I/O optimized instance, you must restart the instance in the ECS console for the new password to take effect.

#### Enable and disable release protection for

## instances

You can enable release protection for Elastic Compute Service (ECS) instances to prevent manual release. This topic describes how to enable and disable release protection for ECS instances and how to check whether release protection is enabled. Context The release protection feature cannot prevent the automatic release of an instance in normal scenarios such as the following scenarios: The automatic release time that you set for the instance has arrived. The instance does not comply with the applicable security compliance policies. The instance was automatically created by Auto Scaling and is removed during subsequent scale-in events. Enable release protection when you create an instance This section describes how to configure release protection settings when you create an instance. For more information about how to create an instance, see Create an instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Inst ances page, click Creat e Inst ance.
5. In the Basic Conf igurat ions step, configure parameters and click Next .
6. In the Net working step, configure parameters and click Next .
7. In the Syst em Conf igurat ions step, select Release Prot ect ion, configure other parameters, and
then click Conf irm Inf ormat ion.
8. Configure other parameters based on your business requirements and click Submit .
Change the release protection settings You can also enable or disable release protection for an instance by modifying the attributes of the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance that you want to modify, click the
icon in the Act ions column, and then choose Inst ance Set t ings > Change Release Prot ect ion Set t ings.
5. In the dialog box that appears, select or clear Release Prot ect ion.
6. Click OK.
Check whether release protection is enabled
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Inst ances page, use one of the following methods to view details of an instance:
In the Inst ance ID/Name column, click the ID of the instance. Find the instance and click Manage in the Act ions column.
5. On the Inst ance Det ails tab, check the Release Prot ect ion parameter in the Conf igurat ions
section. If the value is Yes, Release Protection is enabled. If the value is no, Release Protection is disabled.

#### Customize instance data

ECS allows you to run the instance customization script upon startup and import data into instances. Context The instance data customization feature is applicable to both Windows and Linux instances. It allows you to: Run the instance customization script upon startup. Import data into instances. Usage instructions Limit s The instance data customization feature can only be used when an instance meets all the following requirements: Network type: VPC Image: a system image or a custom image that is inherited from the system image Operating system: one type included in Supported operating systems Supported operating systems

| Windows | Linux |
|---|---|
| Windows Server 2016 64-bit Windows Server 2012 64-bit Windows Server 2008 64-bit | CentOS Ubuntu SUSE Linux Enterprise OpenSUSE Debian Aliyun Linux |

When you configure instance data customization scripts, you must enter custom data based on the type of operating system and script. Not e Only English characters are allowed. If your data is Base64 encoded, select Ent er Base64 Encoded Inf ormat ion. Not e The size of the customization script cannot exceed 16 KB before the data is Base64 encoded. For Linux instances, the script format must meet the requirements described in Types of Linux instance customization scripts. For Windows instances, the script can only start with `[bat]` or `[powershell]` . After starting an instance, run a command to view the following information: Execution result of the instance customization script Data imported to instances Console: You can modify the custom instance data in the console. Whether the modified instance customization script needs to be re-executed depends on the script type. For example, if the `bootc` `md` script in Cloud Config is modified for Linux instances, the script is automatically executed each time instances are restarted. OpenAPI: You can also use OpenAPI to customize instance data. For more information, see Creat eInst ance and Modif yInst anceAt t ribut e in ECS Developer Guide . Linux instance data customization scripts Linux instance data customization scripts provided by Alibaba Cloud are designed based on the cloudinit architecture. They are used to automatically configure parameters of Linux instances. Customization script types are compatible with the cloud-init. Description of Linux instance data customization scripts Linux instance customization scripts are executed after instances are started and before `/etc/init` is executed. Linux instance customization scripts can only be executed with root permissions by default. Types of Linux instance customization scripts User-Dat a Script Description: A script, such as shell script, is used to customize data. Format: The first line must include #! , such as #! /bin/sh . Limit: The script size (including the first line) cannot exceed 16 KB before the data is Base64 encoded. Frequency: The script is executed only when instances are started for the first time. Example:

```
#! /bin/sh
echo "Hello World. The time is now $(date -R)!" | tee /root/output10.txt
```

Cloud Conf ig Dat a Description: Predefined data is used to configure services, such as specifying yum sources or importing SSH keys. Format: The first line must be `#cloud-config` . Limit: The script size (including the first line) cannot exceed 16 KB before the data is Base64 encoded. Frequency: The script execution frequency varies with the specific service. Example:

```
#cloud-config
apt: primary:
- arches: [default]
uri: http://us.archive.ubuntu.com/ubuntu/
```

Include Description: The configuration content can be saved in a text file and imported into cloud-init as a URL. Format: The first line must be `#include` . Limit: The script size (including the first line) cannot exceed 16 KB before the data is Base64 encoded. Frequency: The script execution frequency depends on the script type in the text file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/cloudconfig
```

GZIP f ormat Description: Cloud-ini limits the size of customization scripts to 16 KB. You can compress and import the script file into the customization script if the file size exceeds 16 KB. Format: The .gz file is imported into the customization script as a URL in `#include` . Frequency: The script execution frequency depends on the script content contained in the GZIP file. Example:

```
#include
http://ecs-image-test.oss-cn-hangzhou.aliyuncs.com/userdata/config.gz
```

View the custom data of a Linux instance Run the following command in the instance:

```bash
curl http://100.100.100.200/latest/user-data
```

Windows instance customization scripts Windows instance customization scripts independently developed by Alibaba Cloud can be used to initialize Windows instances. There are two types of Windows instance customization scripts: Batch processing program: starts with `[bat]` and serves as the first line. The script size must be smaller than 16 KB before the data is Base64 encoded. PowerShell script: starts with `[powershell]` and serves as the first line. The script size must be smaller than 16 KB before the data is Base64 encoded. View the custom data of a Windows instance Run the following PowerShell command in the instance:

```
Invoke-RestMethod http://100.100.100.200/latest/user-data/
```

### Manage the instance recycle bin

#### Set the retention period

When you put Elastic Compute Service (ECS) instances into the recycle bin, the instances enter a retention period. This topic describes how to set the retention period. Prerequisites Only the admin account can set the retention period. Context When an instance enters a retention period, its computing resources (CPU and memory) are released, its elastic IP address is disassociated, and its storage resources are retained. When the retention period expires, the ECS instance and its storage resources are completely destroyed and cannot be recovered. The default retention period is three days. You can set an appropriate retention period of up to 30 days and 23 hours based on your business needs.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Recycle Bin.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Recycle Bin page, click Set Ret ent ion Period.
5. In the Set Ret ent ion Period dialog box, specify a period of time and click OK.

#### Restore an instance

When you place Elastic Compute Service (ECS) instances into the recycle bin, the instances enter a retention period. During the retention period, you can restore the instance anytime based on your business requirements. Context When instances are restored from the recycle bin, computing resources (vCPUs and memory) are automatically re-assigned to the instances. If these instances require elastic IP addresses (EIPs), you must manually associate EIPs with the instances. For more information, see the "Associate an EIP with an ECS instance" topic in the EIP User Guide. Not e When you delete instances to the recycle bin, their computing resources are automatically reclaimed. Your attempt to restore instances from the recycle bin may fail due to insufficient quotas or computing resources. Before you restore instances, make sure that your quotas and computing resources are sufficient.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Recycle Bin.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Restore an instance from the recycle bin.
Use one of the following methods to restore the instance from the recycle bin: To restore a single instance, find the instance in the recycle bin and click Rest ore in the Actions column. In the message that appears, click OK. To restore one or more instances at a time, select the instances and click Rest ore in the lower-left corner of the page. In the message that appears, click OK.

#### Permanently delete instances

You can permanently delete the instances that you no longer need from the recycle bin. This topic describes how to permanently delete instances. Context The instances that are permanently deleted cannot be restored. Make sure that your business is not interrupted before you permanently delete instances.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Recycle Bin.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Instances page, view information about all ECS instances in the retention period, including the
instance ID, name, instance type, deletion time, and automatic release time of the instances.
5. Permanently delete instances from the recycle bin.
You can use one of the following methods to permanently delete instances: To delete a single instance, click Permanent ly Delet e in the Actions column corresponding to the instance. In the message that appears, click Delet e. To delete one or more instances at a time, select all instances that you want to delete, and then click Permanent ly Delet e in the lower-left corner of the Instances page. In the message that appears, click Delet e.

### Change the instance type

#### Change the instance type of an instance

You can change the instance types of instances to suit your business needs. This eliminates the need to create new instances. Hot configuration change You can perform a hot configuration change on an instance that is not in the Stopped state to change its instance type. Not e Only specific instance types support hot configuration changes. The instance types that support hot configuration changes are displayed in the Elastic Compute Service (ECS) console.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance whose instance type you want to change and click Hot Conf igurat ion
Change in the Act ions column.
5. On the Change Configurations of ECS Instance without Service Interruption page, select a new
instance type and click Submit . The Change Configurations of ECS Instance without Service Interruption page shows the instance types available for selection. Upgrade and downgrade You can upgrade or downgrade the instance type of an instance that is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose instance type you want to change and click Upgrade/Downgrade in the
Act ions column.
5. On the Change Configurations of ECS Instance page, select a new instance type and click Submit .
The Change Configurations of ECS Instance page shows the instance types available for selection.
6. Restart the instance by using the ECS console or by calling an API operation for the new instance
type to take effect. For more information, see Start an instance or the "StartInstance" topic in ECS Developer Guide.

#### Perform a hot configuration change on an

instance to change the instance type If the instance type of your Elastic Compute Service (ECS) instance does not suit application requirements, you can change it (including vCPUs, memory, and internal bandwidth). This topic describes how to perform a hot configuration change on an instance to change its instance type. Prerequisites The instance supports hot configuration changes and Support Hot Conf igurat ion Changes was selected when the instance was created in the ECS console. For more information, see Create an instance. Not e Instance types that support hot configuration changes are displayed in the ECS console. Context Compared with the instance type change feature, the hot configuration change feature can be used to change instance types without stopping the instances. When you perform a hot configuration change on an instance to change the instance type, the following limits apply: Windows instances do not support hot configuration changes. When you specify a new instance type for the instance, the vCPU, memory, and internal bandwidth specifications of the instance are changed together. These specifications cannot be separately changed. You must wait at least 10 minutes between two consecutive hot configuration changes to the instance type of a single instance. You can perform a maximum of five consecutive hot configuration changes to the instance type of an instance. After the instance is restarted, stopped, or started, the change times are cleared and recalculated. If a hot configuration change on the instance fails, hot configuration changes cannot be performed on the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose instance type you want to change, click the
icon in the Act ions column, and then click Hot Conf igurat ion Change.
5. In the Hot Conf igurat ion Change dialog box, select a desired instance type and click OK.

### View the monitoring information

of an instance You can view monitoring charts in the CloudMonitor console to learn about the running conditions of Elastic Compute Service (ECS) instances. This topic describes how to go to the CloudMonitor console to view the monitoring information of an ECS instance. Context CloudMonitor provides real-time monitoring, alerting, and notification services for resources to protect your services and business. For more information, see CloudMonit or overview in Apsara Uni-manager Management Console User Guide.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance whose monitoring information you want to view and click Monit or in the
Monitoring column.
5. On the Monit oring Chart s page, view the monitoring information of the ECS instance.

### Add an instance to a security

group You can add created instanced to security groups and use security group rules to control network access for the instances. Context Security groups act as virtual firewalls to provide security isolation and implement network access control for instances. Security groups determine whether the instances in the same account that are deployed within the same VPC and region can communicate with each other. By default, if the instances belong to the same security group, they can communicate with each other over the internal network. If the instances belong to different security groups, you can authorize mutual access between the security groups to allow the instances to communicate with each other over the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group to which you want to add an instance and click Manage Inst ances in the
Act ions column.
5. Click Add Inst ance.
6. In the Add Instance dialog box, select an instance and click OK.
An instance can belong to up to five security groups. After an instance is added to a security group, the rules of the security group automatically apply to the instance.

### Change the private IP address of

an instance Each instance is assigned a private NIC and associated with a private IP address. You can change the private IP address of an instance. The new private IP address must be within the CIDR block of the vSwitch to which the instance is connected and must not be in use by another instance. Prerequisites The instance whose private IP address you want to change is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance whose private IP address you want to change and choose More > Change Privat e
IP Address in the Act ions column.
5. Enter a new private IP address.
The new private IP address must be within the CIDR block of the vSwitch to which the instance is connected. This IP address must not be in use by another instance or be reserved for a specific purpose. For example, if the CIDR block of the vSwitch is 192.168.1.0/24, you can use an IP address within the range from 192.168.1.1 to 192.168.1.254. The first address 192.168.1.0 is reserved to identify the subnet itself, and the last address 192.168.1.255 is reserved as the broadcast address. Neither address can be used.
6. Click OK.

### Enable IPv6

Compared with IPv4 addresses, IPv6 addresses are more sufficient and allow more types of devices to access the Internet. If your network environment supports IPv6, you can assign IPv6 addresses for exiting Elastic Compute Service (ECS) instances. Prerequisites The virtual private cloud (VPC) of the ECS instance to which you want to assign an IPv6 address is associated with an IPv6 CIDR block. For more information, see the "Enable an IPv6 CIDR block for a VPC" topic in Apsara Stack VPC User Guide. The vSwitch connected to the ECS instance to which you want to assign an IPv6 address is associated with an IPv6 CIDR block. For more information, see the "Enable an IPv6 CIDR block for a vSwitch" topic in Apsara Stack VPC User Guide. The instance family of the ECS instance supports IPv6.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to assign an IPv6 address and choose More > Manage
Secondary Privat e IPv6 Addresses in the Act ions column.
5. In the Manage Secondary Privat e IPv6 Addresses dialog box, click Open Now next to the IPv6
Addresses field. Not e Specific instance families do not support IPv6.
6. On the vSwitch page, check whether IPv6 is enabled for the vSwitch.
If IPv6 is not enabled for the vSwitch, click Enable IPv6 CIDR Block in the IPv6 CIDR Block column corresponding to the vSwitch.
7. In the Manage Secondary Privat e IPv6 Addresses dialogue box, click OK.
Result After the configuration is complete, you can click the instance ID and check whether an IPv6 address is assigned to the instance on the Inst ance Det ails page.

### Install the CUDA and GPU drivers

for a Linux instance You must install a GPU driver on GPU instances to use the GPU. If the image you use does not contain a pre-installed GPU driver, you must manually install the CUDA and GPU drivers for the instance. Prerequisites If your instance cannot connect to the Internet, the installation file cannot be downloaded. You can install an FTP client on the instance to transfer the installation file to the instance. Context When installing NVIDIA drivers, you must install the kernel package that contains the kernel header file before you install the CUDA and GPU drivers on the instance.
1. Install the kernel package.
i. Run the uname -r command to view the current kernel version. A similar output is displayed: CentOS: `3.10.0-862.14.4.el7.x86_64` Ubuntu: `4.4.0-117-generic` ii. Copy the kernel package of the corresponding version to the instance and install the package. CentOS: Copy the RPM package of the `kernel-devel` component and run the rpm -ivh 3.10.0-862.14.4.el7.x86_64.rpm command to install the package. 3.10.0-862.14.4.el7.x86_64. rpm is used as an example. Replace it with the actual package name. Ubuntu: Copy the DEB package of the `linux-headers` component and run the dpkg -i 4.4.0- 117-generic.deb command to install the package. 4.4.0-117-generic.deb is used as an example. Replace it with the actual package name.
2. Download the CUDA Toolkit.
i. Access the official CUDA download page. Choose the version based on the GPU application requirements for CUDA. This example uses CUDA Toolkit 9.2. Download the CUDA Toolkit ii. Choose a platform based on your operating system. Select Inst aller T ype to runf ile (local) and click Download. NVIDIA drivers are already included in the CUDA Toolkit. Download the drivers
3. Copy the downloaded cuda_9.2.148_396.37_linux.run file to the instance. cuda_9.2.148_396.37_linux.
run is used as an example. Replace it with the actual file name.
4. Run the sudo sh ./cuda_9.2.148_396.37_linux.run --silent --verbose --driver --t oolkit --
samples command to install the CUDA driver. cuda_9.2.148_396.37_linux.run is used as an example. Replace it with the actual file name. The installation takes about 10 to 20 minutes. When `Driver: Installed` is displayed, the installation is successful. View the CUDA installation result
5. Run the nvidia-smi command to view the GPU driver status.
If the output displays the details of the GPU driver, the driver is running properly. View the GPU driver status What's next If you want to run the OpenGL program, you must first purchase the licenses and install the GRID drivers. For information about the installation procedure, see the official NVIDIA documentation.

### Install the CUDA and GPU drivers

for a Windows instance You must install a GPU driver on GPU instances to use the GPU. If the image you use does not contain a pre-installed GPU driver, you must manually install the CUDA and GPU drivers for the instance. Prerequisites If your instance cannot connect to the Internet, the installation file cannot be downloaded. You can install an FTP client on the instance to transfer the installation file to the instance. To compile CUDA programs, first install a Windows compiling environment, such as Visual Studio 2015. If you do not need to compile CUDA programs, ignore it.
1. Download the CUDA Toolkit.
i. Access the official CUDA download page. Choose the version based on the GPU application requirements for CUDA. This example uses CUDA Toolkit 9.2. ii. Choose a platform based on your operating system. Set Inst aller T ype to exe (local) and click Download. NVIDIA drivers are already included in the CUDA Toolkit.
2. Copy the downloaded cuda_9.2.148_windows.exe file to the instance. cuda_9.2.148_windows.exe is
used as an example. Replace it with the actual file name.
3. Double-click cuda_9.2.148_windows.exe and follow the installation wizard to install the CUDA driver.
cuda_9.2.148_windows.exe is used as an example. Replace it with the actual file name. The installation takes about 10 to 20 minutes. When `Installed: - Nsight Monitor and HUD Launch` `er` is displayed, the driver is installed.
4. Press Win + R and enter devmgmt .msc.
The NVIDIA device is displayed in Display Adapt er.
5. Press Win + R, enter cmd, and run the "C:\Program Files\NVIDIA Corporat ion\NVSMI\nvidia-smi"
command. If the output displays the details of the GPU driver, the driver is running properly. What's next If you want to run the OpenGL and DirectX programs, you must first purchase the licenses and install the GRID drivers. For information about the installation procedure, see the official NVIDIA documentation.

## Disks

### Overview

This topic describes the categories of disks and operations that can be performed on disks. Categories of disks Disks are block-level storage devices provided by Apsara Stack for Elastic Compute Service (ECS) instances. Disks can be classified based on their performance or purposes. Perf ormance-based classif icat ion Disks can be classified into ultra disks, shared ultra disks, standard SSDs, shared SSDs, standard performance disks, and premium performance disks based on their performance. Ultra disks and shared ultra disks are ideal for medium I/O load scenarios and deliver up to 5,000 random IOPS. Standard SSDs and shared SSDs are ideal for I/O-intensive scenarios and deliver up to 25,000 random IOPS. Standard performance disks and premium performance disks are ideal for online transaction processing (OLTP) databases and NoSQL databases and deliver up to 25,000 random IOPS. Import ant Different Cloud Defined Storage (CDS)-Elastic Block Storage (EBS) clusters support different disk categories. New CDS-EBS clusters support premium performance disks and standard performance disks. CDS-EBS clusters that were created in Apsara Stack V3.15.0 and earlier support ultra disks, standard SSDs, premium performance disks, and standard performance disks. Existing EBS clusters continue to provide shared ultra disks and shared SSDs. The following table compares the performance of different disk categories.

| Category | Standard SSD and shared SSD | Ultra disk and shared ultra disk | Standard performance disk | Premium performance disk |
|---|---|---|---|---|
| Maximum capacity per disk (GiB) | 32,768 GiB | 32,768 GiB | 32,768 GiB | 32,768 GiB |
| Maximum IOPS | 25,000 | 5,000 | 5,000 | 25,000 |
| Maximum throughput (MB/s) | 300 MB/s | 140 MB/s | 140 MB/s | 300 MB/s |
| Formula for calculating the IOPS per disk | min{1,800 + 30 × Capacity, 25,000} | min{1,800 + 8 × Capacity, 5,000} | min{1,800 + 8 × Capacity, 5,000} | min{1,800 + 30 × Capacity, 25,000} |

| Category | Standard SSD and shared SSD | Ultra disk and shared ultra disk | Standard performance disk | Premium performance disk |
|---|---|---|---|---|
| Formula for calculating the throughput per disk (MB/s) | min{120 + 0.5 × Capacity, 300} | min{100 + 0.15 × Capacity, 140} | min{100 + 0.15 × Capacity, 140} | min{120 + 0.5 × Capacity, 300} |
| API parameter value | cloud ssd _ | cloud efficiency _ | cloud sperf _ | cloud pperf _ |
| Use scenario | Small and medium-sized development and testing environments that require high data durability | Development and testing applications System disks | OLTP databases: relational databases such as MySQL, PostgreSQL, Oracle, and SQL Server databases NoSQL databases: non-relational databases such as MongoDB, HBase, and Cassandra databases Elasticsearch distributed logs: Elasticsearch, Logstash, and Kibana (ELK) log analysis |   |

Purpose-based classif icat ion Disks can be classified into system disks and data disks based on their purposes. System disks are created and released along with the ECS instances to which they are attached and have the same lifecycle as the instances. Shared access is not allowed for system disks. Data disks can be created separately or along with ECS instances. Shared access is not allowed for data disks. A data disk created together with an ECS instance has the same lifecycle as the instance, and is released along with the instance. Data disks that are separately created can be released along with or independently of the ECS instance to which they are attached. The maximum capacity that a data disk can have is determined by its category. Related operations You can perform operations on disks based on your business needs. The following table describes the operations that can be performed on disks.

| Operation | Description | References |
|---|---|---|
| Create a disk | You can create an empty disk to use as a data disk. | Create a disk |
| Attach a data disk | Separately created disks can be attached to instances within the same zone only as data disks. | Attach a data disk |
| Partition and format a disk | Before you can use a separately created disk that is attached to a Linux or Windows instance, you must partition and format the disk on the instance. | Format a data disk for a Linux instance Format a data disk of a Windows instance |

| Operation | Description | References |
|---|---|---|
| View disks | You can view the list of created disks and the details of a single disk. | View disks |
| Roll back a disk by using a snapshot | If you have created snapshots of a disk, you can use a snapshot to roll back the disk to the point in time when the snapshot was created. | Roll back a disk by using a snapshot |
| Modify the properties of a disk | You can modify the properties of a created disk, including the Release Disk with Instance and Release Automatic Snapshots with Disk properties. | Modify the properties of a disk |
| Modify the name and description of a disk | You can modify the name and description of a created disk. | Modify the name and description of a disk |
| Resize a disk | You can resize the system disk or data disks of an instance online or offline. After you resize a disk of an instance offline, you must restart the instance for the resize operation to take effect. | Resize disks |
| Enable multi-attach | When you create a premium performance disk, you can enable the multi-attach feature for the disk. | Enable the multi-attach feature |
| Encrypt a disk | You can encrypt a new disk to improve security in a simple and secure manner. | Encrypt a system disk Encrypt a data disk |
| Re-initialize a disk | You can re-initialize a system disk or data disk so that the disk can return to the state it was in when the disk was created. | Re-initialize a system disk Re-initialize a data disk |
| Detach a data disk | You can detach a data disk from an instance when the instance no longer needs the disk. You can also detach a data disk from an instance and then attach the disk to another instance within the same zone. | Detach a data disk |
| Release a data disk | You can manually release disks that are no longer needed. When a disk is released, all data stored on the disk is deleted. | Release a data disk |

### Create a disk

You can create standalone data disks and then attach them to ECS instances to increase the storage space of the instances. This topic describes how to create an empty data disk. You cannot create standalone system disks. Context We recommend that you determine the number and sizes of data disks before you create them. The following limits apply to data disks: A maximum of 16 data disks can be attached to an instance. Disks and Shared Block Storage devices share this quota. Each Shared Block Storage device can be attached to up to four ECS instances at the same time. Each ultra disk, standard SSD, Ultra Shared Block Storage device, or SSD Shared Block Storage device can have a maximum capacity of 32 TiB. Disks cannot be combined in ECS. They are independent of each other. You cannot combine multiple disks into one by formatting them. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across multiple disks, because a snapshot can back up data only of a single disk. If you create a logical volume across several disks, data discrepancies may occur when you restore these disks.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Disk.
5. Configure the parameters listed in the following table to create a disk.

| Type | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | Select an organization in which to create the disk. |
|   | Resource Set | Yes | Select a resource set in which to create the disk. |
|   | Region | Yes | Select a region in which to create the disk. |
|   | Zone | Yes | Select a zone in which to create the disk. |
|   | Name | Yes | Enter a name for the disk. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |

|   | Elastic Compute Servic |   |   |
|---|---|---|---|
| Type | Parameter | Required | Description |
| Basic Settings | Specifications | Yes | Select a disk category and specify the disk size. Valid values for the disk category: St andard SSD: standard SSD Ult ra Disk: ultra disk Shared SSD: SSD Shared Block Storage device Shared Ult ra Disk: Ultra Shared Block Storage device The disk size must range from 20 GiB to 32,768 GiB. |
|   | Encrypted | No | Specify whether to encrypt the disk. |
|   | Encryption Method | No | Select an encryption algorithm. This parameter is required when you set Encrypt ed to Yes. Valid values: AES256 SM4 |
|   | Encryption Key | No | Select a key to be used to encrypt the disk. This parameter is required when you set Encrypt ed to Yes. Not e If no key is available, create a key in KMS. |
|   | Use Snapshot | No | Specify whether to create the disk from a snapshot. If you select Yes, you must specify a snapshot. The size of the created disk depends on the size of the specified snapshot. If the disk size that you specify is greater than the snapshot size, the disk is created with the size you specify. If the disk size that you specify is smaller than the snapshot size, the disk is created with the snapshot size. |

6. Click Submit .
Result The created disk is displayed in the disk list and in the Pending state. What's next After the disk is created, you must attach the disk to an instance and partition and format the disk. For more information, see the following topics: Attach a disk Format a data disk for a Linux instance Format a data disk of a Windows instance

### Attach a disk

You can attach separately created disks as data disks to instances. To attach a disk to an instance, make sure that the disk and the instance are located within the same region and zone. Prerequisites The disk that you want to attach is in the Available state. Context You do not need to attach data disks that are created together with instances. A disk can be attached only to a single instance within the same region and zone. Each disk can be attached only to a single instance at the same time. Each Shared Block Storage device can be attached to up to four instances at the same time. Attach a disk on the instance details page To attach multiple disks to an instance, you can go to the details page of the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to attach a disk and click the instance ID.
5. Click the Disks tab.
6. Click At t ach.
7. In the Attach dialog box, select a disk from the Disk drop-down list.
8. Click OK.
Attach a disk on the Disks page To attach multiple disks to different instances, you can go to the Disks page.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk that you want to attach and choose More > At t ach in the Act ions column.
5. Specify the destination instance and configure the release mode.
If you select Release Disk wit h Inst ance, the disk will be released when its associated instance is deleted. If you do not select Release Disk wit h Inst ance, the disk will be retained and enter the Available state when its associated instance is deleted.
6. Click OK.

### Partition and format disks

#### Format a data disk for a Linux instance

Data disks created separately are not partitioned or formatted. This topic describes how to partition and format a data disk of a Linux instance. Prerequisites The disk has been attached to the instance.
1. Connect to the instance.
2. Run the f disk -l command to view all data disks attached to the ECS instance.
If /dev/vdb is not displayed in the command output, the ECS instance does not have a data disk. Check whether the data disk is attached to the instance.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00000000
```

3. Create partitions for the data disk.
i. Run the f disk /dev/sdb command. ii. Enter n to create a new partition. iii. Enter p to set the partition as the primary partition. iv. Enter a partition number and press the Enter key. In this example, 1 is entered to create Partition 1. v. Enter the number of the first available sector. This example uses the default value. This is done by pressing the Enter key. You can also enter a value from 1 to 41610 and press the Enter key. vi. Enter the number of the last sector. This example uses the default value. This is done by pressing the Enter key. You can also enter a value from 1 to 11748 and press the Enter key. vii. (Optional)Optional. To create multiple partitions, repeat steps b through f until all four primary partitions are created. viii. Run the wq command to start partitioning.

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

4. Run the f disk -l command to view the partitions.
If /dev/vdb1 is displayed in the command output, new partition vdb1 is created.

```
[root@iZ********eZ ~]# fdisk -l Disk /dev/vda: 42.9 GB, 42949672960 bytes 255 heads, 63 sectors/track, 5221 cylinders Units = cylinders of 16065 * 512 = 8225280 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x00078f9c Device Boot Start End Blocks Id System /dev/vda1 * 1 5222 41940992 83 Linux Disk /dev/vdb: 21.5 GB, 21474836480 bytes 16 heads, 63 sectors/track, 41610 cylinders Units = cylinders of 1008 * 512 = 516096 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disk identifier: 0x01ac58fe Device Boot Start End Blocks Id System /dev/vdb1 1 41610 20971408+ 83 Linux
```

5. Format the new partition. In this example, the new partition is formatted as ext3 after you run the
mkf s.ext 3 /dev/vdb1 command. The time required for formatting depends on the disk size. You can also format the new partition to another file system. For example, you can run the mkf s.ext 4 /dev/vdb1 command to format the partition as ext4. Compared with ext2, ext3 only adds the log function. Compared with ext3, ext4 improves on some important data structures. ext4 provides better performance and reliability, and more functions.

```
[root@iZ********leZ ~]# mkfs.ext3 /dev/vdb1 mke2fs 1.41.12 (17-May-2010) Filesystem label= OS type: Linux Block size=4096 (log=2) Fragment size=4096 (log=2) Stride=0 blocks, Stripe width=0 blocks 1310720 inodes, 5242852 blocks 262142 blocks (5.00%) reserved for the super user First data block=0 Maximum filesystem blocks=4294967296 160 block groups 32768 blocks per group, 32768 fragments per group 8192 inodes per group Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
    4096000
Writing inode tables: done Creating journal (32768 blocks): done Writing superblocks and filesystem accounting information: done This filesystem will be automatically checked every 25 mounts or 180 days, whichever comes first. Use tune2fs -c or -i to override.
```

6. Run the `echo '/dev/vdb1 /mnt ext3 defaults 0 0' >> /etc/fstab` command to write the
information of the new partition to the /etc/fstab file. You can run the `cat /etc/fstab` command to view the new partition information. Ubuntu 12.04 does not support barriers. To write the information of the new partition into the /etc/fstab file, you must run the `echo '/dev/vdb1 /mnt ext3 barrier=0 0 0' >> /etc/fstab` command. In this example, the partition information is added to the ext3 file system. You can also modify the ext3 parameter to add the partition information to another type of file system. To attach the data disk to a specific folder, for example, to store web pages, modify the /mnt part of the preceding command.

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

7. Mount the new partitions. Run the mount -a command to mount all the partitions listed in /etc/fsta
b and run the df -h command to view the result. If the following information is displayed, the new partitions are mounted and available for use.

```
[root@iZ********eZ ~]# mount -a [root@iZ********eZ ~]# df -h Filesystem Size Used Avail Use% Mounted on /dev/vda1 40G 5.6G 32G 15% / tmpfs 499M 0 499M 0% /dev/shm /dev/vdb1 20G 173M 19G 1% /mnt
```

#### Format a data disk of a Windows instance

Data disks created separately are not partitioned or formatted. This topic describes how to partition and format a data disk of a Windows instance. This example uses Windows Server 2008. Prerequisites The disk has been attached to an instance.
1. In the lower-left corner of the screen, click the Server Manager icon.
2. In the left-side navigation pane of the Server Manager window, choose St orage > Disk
Management .
3. Right-click an empty partition and select New Simple Volume from the shortcut menu.
If the disk status is Of f line, change it to Online.
4. Click Next .
5. Set the size of the simple volume, which is the partition size. Then click Next .
The default value is the maximum value of the disk space. You can specify the partition size as needed.
6. Specify the drive letter and then click Next .
7. Specify the formatting options and then click Next .
We recommend that you format the partition with the default settings provided by the wizard.
8. When the wizard prompts that the partition has been completed, click Finish to close the wizard.

### View disks

You can view the list of disks and the details of individual disks.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list, enter the relevant information in the search box, and
click search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Disk Name | Enter a disk name to search for the disk. |
| Disk ID | Enter a disk ID to search for the disk. |
| Instance ID | Enter an instance ID to search for disks that are attached to the instance. |
| Disk Status | Select a disk status to search for disks in that status. Valid values: Running Pending At t aching Det aching Creat ing Delet ing Delet ed Not e Deleted disks are no longer displayed in the disk list. Init ializing All St at uses |
| Disk Properties | Select a disk type to search for disks of that type. Valid values: All Syst em Disk Dat a Disk |
| Policy ID | Enter the ID of an automatic snapshot policy to search for disks that use the policy. |
| Encryption Key ID | Enter the ID of an encryption key to search for disks that are encrypted by using the key. |

5. In the Disk ID/Name column, click a disk ID to go to the Disk Details page of the disk.
The properties and mount information of the disk are displayed on the Disk Details page.

### Restore a disk

If you have created snapshots for a disk, you can use one of the snapshots to restore the disk to the state when the snapshot was created. The disk restore operation is irreversible. After the disk is restored, the data stored on the disk before the restore operation is performed cannot be recovered. Exercise caution when you perform this operation. Prerequisites Snapshots are created for the disk that you want to restore. The disk is not released. The instance to which the disk is attached is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filtering option from the drop-down list, enter the relevant information in the search bar,
and click Search. You can select multiple filtering options to narrow down the search results.

| Filt ering opt ion | Descript ion |
|---|---|
| Snapshot Name | Enter a snapshot name to search for the snapshot. |
| Snapshot ID | Enter a snapshot ID to search for the snapshot. |
| Instance ID | Enter an instance ID to search for the snapshots related to the instance. |
| Disk ID | Enter a disk ID to search for the snapshots related to the disk. |
| Snapshot Type | Select a snapshot type to search for the snapshots of that type. Options include: All User Snapshot s: manual snapshots. Aut omat ic snapshot s: automatic snapshots. |
| Creation Time | Enter a creation time to search for the snapshots that were created at that time. |

5. Find the snapshot that you want to use to restore the specified disk and click Rest ore Disk in the
Act ions column.
6. Click OK.

### Modify the attributes of a disk

You can modify the attributes of created disks, such as the settings of the Release Disk with Instance and Release Automatic Snapshots with Disk options.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk whose attributes you want to modify and choose More > Modif y Disk Propert ies in
the Act ions column.
5. Modify the Release Mode settings.
Release Disk wit h Inst ance: If this option is selected, the disk will be released when its associated instance is deleted. If this option is not selected, the disk will be retained and enter the Pending state when its associated instance is deleted. Release Aut omat ic Snapshot s wit h Disk: If this option is selected, the automatic snapshots of the disk will be released when the disk is deleted. If this option is not selected, the automatic snapshots will be retained when the disk is deleted.
6. Click OK.

### Modify the description of a disk

You can modify the names and descriptions of created disks.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk that you want to modify and choose More > Modif y Disk Descript ion in the Act ions
column.
5. Modify the name and description of the disk.
The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores (_), colons (:), and hyphens (-). The description must be 2 to 256 characters in length and cannot start with http:// or https://.
6. Click OK.

### Expand a disk

You can expand system disks or data disks online. After a disk is expanded, you do not need to restart the instance to which the disk is attached for the new disk capacity to take effect. Prerequisites To avoid data loss, we recommend that you create a snapshot to back up disk data before you expand a disk. For more information, see Create a snapshot. No snapshot is being created for the disk to be expanded. The following requirements are met: If the disk is a system disk, the associated instance is in the Running state. If the disk is a data disk, one of the following requirements is met: The disk is in the Pending state. If the disk is attached to an instance, the instance is in the Running state. If the disk is a Shared Block Storage device, it is in the Pending state. Context The following limits apply when you expand a disk.

| Limit | Description |
|---|---|
| Disk category | Ultra disks and standard SSDs can be expanded. SSD Shared Block Storage and Ultra Shared Block Storage devices can be expanded. |
| Operating system | The system disks of Windows Server 2003 instances cannot be expanded. |
| Partitioning mode | Data disks that use the MBR partitioning scheme cannot be expanded to larger than 2 TiB in size. To expand an MBR data disk to larger than 2 TiB in size, we recommend that you create and attach a new data disk larger than 2 TiB in size, use the GPT partitioning scheme to partition this new data disk, and then copy data from the original MBR data disk to the new GPT data disk. |
| File system | For Windows instances, only disks that use NTFS file systems can be expanded. |
| Maximum capacity | Ultra disk and standard SSD: 32,768 GiB SSD Shared Block Storage device and Ultra Shared Block Storage device: 32,768 GiB |
| Related operations | When you expand disks, only the capacity of the disks is expanded. The sizes of partitions and file systems do not change. You must manually re-allocate the storage space on a disk after the disk is expanded. You cannot shrink an expanded disk by any means, such as by rolling it back. |

1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk that you want to expand and choose More > Expand Disk in the Act ions column.
5. In the Expand Disk dialog box, specify a new capacity for the disk.
The new capacity must be greater than the current capacity.
6. Click OK.
Result When you expand disks, only the capacity of the disks is expanded. The sizes of partitions and file systems do not change. You must manually re-allocate the storage space on a disk after the disk is expanded.

### Support the NVMe protocol and

multi-attach feature

#### Overview of disks that support NVMe

Non-Volatile Memory Express (NVMe) is a host controller interface protocol used to accelerate the transfer of data from non-volatile memory. Alibaba Cloud premium performance disks support NVMe. Each premium performance disk can be simultaneously attached to multiple Elastic Compute Service (ECS) instances that support NVMe for data sharing. This topic describes premium performance disks that support NVMe, limits on attaching this type of disks, and operations related to this type of disks. Premium performance disks that support NVMe Premium performance disks can be attached to multiple ECS instances. After premium performance disks are attached to multiple instances, the disks support concurrent read and write access from these ECS instances and provide high reliability, high concurrency, and high performance. Premium performance disks provide the multi-attach and I/O blocking features. After the multi-attach feature is enabled for a premium performance disk, the disk can be attached to up to 16 ECS instances at a time. You can run NVMe commands to manage the permissions of ECS instances on premium performance disks. For more information about NVMe commands, see NVM Express Base Specification. The preceding features improve service availability without compromising data reliability. If a single point of failure (SPOF) occurs, you can use a premium performance disk to quickly schedule and restore data. Data sharing among multiple ECS instances greatly reduces storage costs and improves service flexibility. Premium performance disks are suitable for high-availability databases and distributed database clusters that each consist of one write node and multiple read-only nodes. Premium performance disks can be attached to ECS instances that support NVMe. For example, after premium performance disks are attached to Linux instances based on NVMe, you can run the lsblk command to check the device names and partition names of the disks, as shown in the following figure. Description of the command output: The device names of the premium performance disks are displayed in the `/dev/nvmeXn1` format. Examples: /dev/nvme0n1, /dev/nvme1n1, and /dev/nvme2n1. The partition names of the premium performance disks are displayed in the `<Device name of the di` `sk>p<Partition number>` format. Examples: /dev/nvme0n1p1, /dev/nvme1n1p1, and /dev/nvme1n 1p2. Premium performance disks provide the multi-attach feature and are used by enterprises to migrate high-availability services to the cloud. For more information, see Enable the multi-attach feature. Limits Before you attach premium performance disks to an ECS instance based on NVMe, the resources of the instance must meet the limits described in the following table.

| Item | Limits |
|---|---|

| Item | Limits |
|---|---|
| Instance family | By default, the instance family must support NVMe. The following instance families support NVMe: ecs.ebmg7s-se-x25-c1m8 ecs.ebmg7m-se-x25-c1m8 ecs.ebmg7x-se-x25-c1m8 ecs.ebmg7s-se-numaoff-x25-c1m8 ecs.ebmg7m-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.g7x-se-x25 Not e You can call the DescribeInstanceTypes operation to query instance families and check whether the instance family supports NVMe based on the NvmeSupport parameter in the response. For more information, see the DescribeInstanceTypes topic in ECS Developer Guide. |
| Image | The image must contain the NVMe driver. The NVMe driver is installed in the following public images. Not e Only some public Linux images support the NVMe driver. CentOS 7: CentOS 7.6 and later CentOS 8: CentOS 8.0 and later |
| Disk | Disk category: premium performance disk Creation method: Create premium performance disks when you create instances that support NVMe. When you create disks, select premium performance disks as the disk category and enable the multi-attach feature. |

Related operations You can perform the following operations on premium performance disks that support NVMe: Create premium performance disks when you create ECS instances that support NVMe. In this case, the created premium performance disks support NVMe. For more information, see Create an instance by using the wizard. Enable the multi-attach feature when you separately create premium performance disks. For more information, see Enable the multi-attach feature. Format premium performance disks and create file systems. For more information, see Format a data disk for a Linux instance. Import ant The preceding operations are applicable only to premium performance disks that are created together with instances but not to premium performance disks for which the multi-attach feature is enabled.

#### Enable the multi-attach feature

When you create a premium performance disk, you can enable the multi-attach feature for the disk. After multi-attach is enabled for a premium performance disk, the disk can be attached to up to 16 Elastic Compute Service (ECS) instances that support the Non-Volatile Memory Express (NVMe) protocol within the same zone to allow concurrent read and write access from the instances. Benefits This feature is suitable for high-availability databases and distributed database clusters that each consist of one write node and multiple read-only nodes. This feature provides the following benefits: Usage of NVMe commands: NVMe commands can be used to manage permissions of ECS instances on premium performance disks. This helps improve service availability without compromising data durability. For more information about NVMe commands, see NVM Express Base Specification. Cross-instance data sharing: This feature enables data sharing across multiple ECS instances to reduce storage costs and improve service flexibility. Disaster recovery: This feature allows quick scheduling of services to normal ECS instances to ensure service continuity in single-point-of-failure (SPOF) scenarios. Limits The following limits apply to the multi-attach feature: The following list provides instance families that support this feature. ecs.ebmg7s-se-x25-c1m8 ecs.ebmg7m-se-x25-c1m8 ecs.ebmg7x-se-x25-c1m8 ecs.ebmg7s-se-numaoff-x25-c1m8 ecs.ebmg7m-se-numaoff-x25-c1m8 ecs.ebmg7x-se-numaoff-x25-c1m8 ecs.g7x-se-x25 Data disks are supported but system disks are not supported. The multi-attach feature can be enabled only when you create premium performance disks. This feature cannot be enabled or disabled after premium performance disks are created. After the multi-attach feature is enabled for a premium performance disk, we recommend that you use cluster file systems such as Oracle Cluster File System version 2 (OCFS2), Global File System 2 (GFS2), Veritas Cluster File System (Veritas CFS), Oracle Automatic Storage Management Cluster File System (Oracle ACFS), and Databricks File System (DBFS) on the disk. Warning When a premium performance disk for which the multi-attach feature is enabled is attached to multiple ECS instances, data cannot be synchronized among the instances and data inconsistency may occur if file systems such as EXT2, EXT3, EXT4, XFS, and New Technology File System (NTFS) are used. The performance of premium performance disks is limited. When a premium performance disk is attached to multiple ECS instances, the total performance of the disk on all instances cannot exceed the maximum performance that can be provided by the disk. The following table describes the limits that apply to the features provided by premium performance disks for which the multi-attach feature is enabled.

| Feature | Limits |
|---|---|
| Disk attaching | A single premium performance disk can be attached to up to 16 instances that support the NVMe protocol. |
| Release of disks with instances | Not supported. |
| Disk re-initialization | Not supported. |
| Disk category change | Not supported. |
| Disk resizing | Only offline resizing is supported for disks. For more information, see Resize disks. |
| Snapshot-consistent group | Not supported. |

Perform the following steps to use the multi-attach feature:
1. Create a premium performance disk for which the multi-attach feature is enabled. For more
information, see Step 1: Create a premium performance disk for which the multi-attach feature is enabled.
2. Attach the disk to multiple ECS instances that support the NVMe protocol. For more information, see
Step 2: Attach the premium performance disk to multiple instances that support the NVMe protocol. Step 1: Create a premium performance disk for which the multiattach feature is enabled To use the multi-attach feature, enable the feature when you create a premium performance disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Disk.
5. Configure the parameters described in the following table for the premium performance disk that
you create.

| Type | Parameter | Required | Description |
|---|---|---|---|
| Area | Organization | Yes | Select the organization to which the disk belongs. |
|   | Resource Set | Yes | Select the resource set to which the disk belongs. |
|   | Region | Yes | Select the region in which you want to deploy the disk. |
|   | Zone | Yes | Select the zone in which you want to deploy the disk. |
|   | Creation Method | Yes | Select the method that you want to use to create the disk. Valid values: Disk Creation and Storage Set Creation. Not e Storage Set is a service that provides block storage resources in clusters. Each storage set is physically isolated and allows its owner exclusive access to its resources. Storage sets can be used to improve the security and O&M efficiency of your business data storage. For more information about storage sets, see the Create a storage set topic in Cloud Define d Storage (CDS) User Guide. |
|   | Storage Set | Yes | Select the storage set that you want to use to create the disk. Not e This parameter is required if you set Creat ion Met hod to St orage Set Creat ion. |
|   | Partition | Yes | Select the number of partitions in a storage set. The value of this parameter must be greater than or equal to 2. Not e This parameter is required if you set Creat ion Met hod to St orage Set Creat ion. |

| Type | Parameter | Required | Description |
|---|---|---|---|
| Basic Configurations | Name | Yes | Enter a name for the disk that you want to create. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores ( ), and _ hyphens (-). |
|   | Quantity | Yes | Enter the number of disks that you want to create. |
|   | Specifications | Yes | Select Premium Perf ormance Disk. |
|   | Disk Size | Yes | Specify a disk size in the range of 20 GiB to 32,768 GiB. |
|   | Multi-Attach | Yes | Select whether to enable the multi- attach feature for the disk. |
|   | Encryption | No | Select whether to encrypt created disks. |
|   | Encryption Method | No | Select the encryption algorithm that you want to use to encrypt the disk. This parameter is required if you set Encrypt ion to Yes. Valid values: AES256 SM4 |
|   | Encryption Key | No | Select the key that you want to use to encrypt the disk. This parameter is required if you set Encrypt ion to Yes. Not e If no keys are available, create a key in Key Management Service. |

| Type | Parameter | Required | Description |
|---|---|---|---|
|   | Use Snapshot | No | Select whether to create the disk from a snapshot. If you select Yes, you must specify a snapshot. In this case, the size of the created disk may be affected by the snapshot size. If the disk size that you specify is greater than the snapshot size, the disk is created with the size that you specify. If the disk size that you specify is smaller than the snapshot size, the disk is created with the snapshot size. |

Not e For more information about how to create disks, see Create a disk.
6. Confirm the configurations and click Submit .
7. In the message that appears, click OK.
After the disk is created, you can go to the Disks page to view the created disk. The state of the disk is Available, and Enabled is displayed in the Multi-attach column. Step 2: Attach the premium performance disk to multiple instances that support the NVMe protocol Before you attach the premium performance disk to instances, make sure that the following requirements are met: The premium performance disk and the instances reside in the same zone. The instance families and images of the instances comply with the NVMe protocol. For more information, see Limits.
1. Obtain the ID of the instance to which you want to attach the premium performance disk.
In the left-side navigation pane, choose Inst ances & Images > Inst ances. On the Instances page, view and copy the instance ID in the instance list.
2. In the left-side navigation pane, choose St orage & Snapshot s > Disks.
3. Use the instance ID to search for the premium performance disk that you want to attach to the
instance. Then, click the icon in the Act ions column corresponding to the disk, and select At t ach.
4. In the At t ach dialog box, select an instance ID from the Inst ance drop-down list and click OK.
You must select the instance ID that you obtained in Step 1 from the Inst ance drop-down list. Not e You can attach the premium performance disk to only a single instance each time you perform the preceding steps. To attach the premium performance disk to multiple instances, repeat the preceding steps. You can go to the Disks page to view the state of the premium performance disk. The state of the disk is displayed as Running on this page. You can click the name of the premium performance disk to go to the disk detail panel. In the At t achment Inf ormat ion section of this panel, you can view information about the premium performance disk that is attached to a single instance or multiple instances. What to do next After the premium performance disk is attached to multiple instances, we recommend that you create cluster file systems based on your business requirements. Common cluster file systems include OCFS2, GFS2, Veritas CFS, Oracle ACFS, and DBFS. Warning When a premium performance disk for which the multi-attach feature is enabled is attached to multiple ECS instances, data cannot be synchronized among the instances and data inconsistency may occur if file systems such as EXT2, EXT3, EXT4, XFS, and New Technology File System (NTFS) are used.

### Encrypt a disk

#### Overview

Disk encryption is a simple and secure method provided by Elastic Compute Service (ECS) to encrypt new disks. Disk encryption eliminates the need to create or maintain your own key management infrastructure, to modify existing applications and maintenance procedures, and to perform additional encryption operations. Disk encryption does not have negative impacts on your business. The following types of data can be encrypted in disk encryption operations: Data stored on disks. Data transmitted between disks and instances. Data within instance operating systems is not encrypted. All snapshots created from encrypted disks. These snapshots are encrypted snapshots. Data transmitted from instances to disks is encrypted on the hosts where the instances reside. Ultra disks, standard SSDs, premium performance disks, and standard performance disks can be encrypted by using disk encryption. Not e By default, shared SSDs and shared ultra disks cannot be encrypted by using disk encryption. To create and encrypt shared SSDs or shared ultra disks, submit a ticket.

#### Encrypt a system disk

In the scenarios that require data security and regulatory compliance, you can encrypt disks to secure your data stored on the disks. To encrypt system disks, you can encrypt custom images and then use the encrypted custom images to create instances. The system disks of the created instances are automatically encrypted. Context You can encrypt system disks only by encrypting custom images. Step 1: Create a custom image from an instance
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the snapshot from which you want to create a custom image and click Creat e Cust om Image in
the Act ions column.
5. Configure the parameters listed in the following table to create a custom image.

| Parameter | Description |
|---|---|
| Cust om Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). _ It must start with a letter. |
| Sharing Scope | Select the scope in which to share the custom image. Current Organizat ion and Subordinat e Organizat ions Current Resource Set Current Organizat ion |
| Descript ion | Enter a description for the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

6. Click OK.
Step 2: Encrypt the custom image
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Cust om Images tab.
5. Find the custom image that you want to encrypt and click Encrypt Image in the Act ions column.
6. In the Encrypt Image dialog box, configure the parameters listed in the following table.

| Paramet er | Descript ion |
|---|---|
| Image ID | The system automatically obtains the ID of the image to be encrypted. You do not need to configure this parameter. |
| Cust om Image Name | Enter a name for the new encrypted custom image. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and hyphens (-). It must _ start with a letter. |
| Descript ion | Enter a description for the new encrypted custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

7. Click OK.
Step 3: Use the encrypted custom image to create an instance
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Inst ance.
5. Configure the parameters for the instance.
For more information about how to configure these parameters, see Create an instance In the Image section, set Image Type to Cust om Image. Then, select the image that you encrypted from the Cust om Image drop-down list.
6. Click Submit .
Result After the instance is created, you can click its ID to go to the Inst ance Det ails page. Then, you can click the Disks tab and check the value in the Disk Encrypt ion column corresponding to the system disk. If the value is Yes, the system disk is encrypted.

#### Encrypt a data disk

In scenarios that require data security and regulatory compliance, you can encrypt disks to secure your data stored on the disks. After a data disk is created, its encryption state cannot be changed. If you want to encrypt a data disk, enable encryption for the disk when you create it. Context Determine the number and sizes of data disks that you need before you create them. Take note of the following limits: Not e System disks cannot be created separately. The maximum number of data disks that can be attached to a single instance varies based on the instance type. A single premium performance disk that has the multi-attach feature enabled can be attached to up to 16 ECS instances at the same time. Each ultra disk, shared ultra disk, standard SSD, shared SSD, premium performance disk, or standard performance disk can be up to 32 TiB in size. Disks cannot be combined in ECS. They are independent of each other. You cannot combine multiple disks into one by formatting them. A snapshot can back up data only of a single disk. We recommend that you do not use Logical Volume Manager (LVM) to create logical volumes across disks. If you use LVM to create a logical volume across multiple existing disks, data discrepancy may occur when you restore disks from snapshots.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Disk.
5. On the Create Disk page, configure the parameters.
When you encrypt the disk, take note of the following parameters: Encrypt ion: Select Yes. Encrypt ion Met hod: Select an encryption algorithm. Valid values: AES256 SM4 Encrypt ion Key: Select an encryption key. For more information about parameters that you can configure, see Create a disk.
6. Click Submit .

### Re-initialize disks

#### Re-initialize a disk

You can re-initialize disks to restore them to their initial states. Prerequisites The disk to be re-initialized is in the Running state. The instance to which the disk is attached is in the St opped state. After a disk is re-initialized, the data stored on the disk is lost and cannot be recovered. Exercise caution when you perform this operation. We recommend that you back up disk data or create snapshots before you re-initialize a disk. For more information, see Create a snapshot. Context The result of disk re-initialization depends on the disk type and how the disk was created. System disk: The disk is restored to the initial state of the image from which the disk was created. If the corresponding image has been deleted, the disk cannot be re-initialized. Data disk: If the disk is empty when created, the disk is restored to an empty disk. If the disk was created from a snapshot, the disk is restored to the state of the snapshot. If the snapshot from which a disk was created has been deleted, the disk cannot be re-initialized.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to re-initialize and click Re-init ialize in the Act ions column.
5. In the Re-initialize Disk dialog box, perform operations based on the disk type.
For a system disk, enter and confirm a new instance logon password. Select or clear Instance After Re-initializing Disk, and click OK. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters include ( ) ' ~ ! @#$%^&*-_+=|{}[]:;'<>,.? / For a data disk, click OK. Result When the disk is being re-initialized, the disk is in the Init ializing state. After the disk is re-initialized, it enters the Running state.

#### Re-initialize a data disk

When a data disk is attached to an Elastic Compute Service (ECS) instance, you can re-initialize the disk to restore it to the state when it is created. Prerequisites Snapshots are created for your data disk. For more information, see Create a snapshot. The data disk is attached to an ECS instance. For more information, see Attach a disk. The ECS instance is in the St opped state. For a Linux instance, if you create an empty data disk and add a command in the /etc/fstab file to mount partitions of the data disk on system startup, the command is not executed and the instance cannot start as expected after you re-initialize the data disk. We recommend that you comment out the command in the /etc/fstab file. Perform the following steps: i. Connect to the instance. For more information, see Instance connecting overview. ii. Run the `vim /etc/fstab` command. iii. Press the `I` key to enter the edit mode. iv. Find the command used to mount data disk partitions and comment out the command by using a number sign (#), as shown in the following command line.

```bash
# /dev/vdb1 /InitTest ext3 defaults 0 0
```

Not e In this example, /dev/vdb1 is a partition and /InitTest is a mount point. You can modify the command based on your business requirements. v. Press the `Esc` key to exit the edit mode, and enter :wq to save the file and exit. Context The state of a data disk after it is re-initialized varies based on its original state when it was created and the operating system that the instance runs: The data disk is restored to the initial state when it was created: The data disk becomes an empty disk if it was originally an empty disk. The data disk stores the data recorded in the source snapshot if the data disk was created from a snapshot. For a Windows instance, after you re-initialize a data disk, the data disk is ready for use without the need for additional operations regardless of its original state. For a Linux instance: If a data disk was created from a snapshot, the data disk stores only the data recorded in the source snapshot after the data disk is re-initialized. You do not need to re-mount the partitions, but all the data generated after the disk was created is lost. If a data disk was created as an empty disk, all the data and file systems on the disk are lost after the data disk is re-initialized. You must reformat and partition the disk, and then re-mount the partitions.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to re-initialize, and click Re-init ialize Disk in the Act ions column.
5. In the Re-init ialize Disk dialog box, click OK.
What's next For a Linux instance, if the data disk was created as an empty disk, you must format the data disk after you re-initialize it. For more information, see Format a data disk for a Linux instance. After the data disk is re-initialized, you must redeploy the applications and reconfigure the parameters on the disk to restore your business at the earliest opportunity.

### Detach a data disk

You can detach data disks but cannot detach system disks. Prerequisites Before you can detach a data disk from a Windows instance, you must bring the data disk offline by using Disk Management. Not e To avoid data loss and ensure data integrity, we recommend that you stop read and write operations on the disk before you detach it. Before you can detach a data disk from a Linux instance, you must connect to the instance and unmount all partitions on the disk. Not e If you have added an entry in the /etc/fstab file for the disk partitions to be automatically mounted on instance startup, you must delete the entry from the /etc/fstab file before you detach the disk. Otherwise, you are unable to connect to the instance after the instance is restarted. The data disk that you want to detach is in the Running state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the data disk that you want to detach and choose More > Det ach in the Act ions column.
5. Click OK.

### Release a data disk

You can release data disks that are no longer needed. Released disks cannot be recovered. Exercise caution when you release data disks. Prerequisites The data disk to be released is in the Pending state. If the data disk is attached to an instance, you must detach the disk from the instance before you can release the disk.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the disk that you want to release and choose More > Release from the Act ions column.
5. Click OK.

## Images

### Overview

An image is a template for running environments within Elastic Compute Service (ECS) instances. An image includes an operating system and pre-installed applications. An image works as a copy that stores data from one or more disks. An image may store data from a system disk or from both system and data disks. You can use an image to create an ECS instance or replace the system disk of an ECS instance. Image types ECS images are classified into public images, custom images, and shared custom images based on image sources. Not e Image types and image versions are displayed in the ECS console. Public images Public images provided by Alibaba Cloud in Apsara Stack support the following Windows Server operating systems and mainstream Linux operating systems. The following table describes two types of public images provided by Alibaba Cloud.

| Type | Description | Technical support |
|---|---|---|
| Alibaba Cloud Linux images | Alibaba Cloud Linux images are custom, proprietary operating system images provided by Alibaba Cloud for ECS instances. Alibaba Cloud Linux images are thoroughly tested to ensure their security, stability, and normal startup and operation. | Alibaba Cloud provides technical support to help resolve the issues that you may encounter when you use Alibaba Cloud Linux images. |

| Type | Description | Technical support |
|---|---|---|
| Third-party images and open source images | Third-party and open source images are thoroughly tested and released by Alibaba Cloud to ensure their security, stability, and normal startup and operation. The following third- party public images are available: Windows: Windows Server Linux: Anolis OS CentOS Debian FreeBSD Ubuntu openSUSE SUSE Linux UOS Kylin NFS | We recommend that you contact corresponding operating system vendors or open source communities for technical support. Alibaba Cloud also provides information about image- and system-related issues. |

Types and versions of public images Alibaba Cloud Linux images Alibaba Cloud Linux images are Linux public images developed by Alibaba Cloud in-house. Both the x86 and ARM platforms support Alibaba Cloud Linux 2 operating systems. T hird-part y images and open source images You can view or search for available public images in the ECS console. For more information, see View images. The following tables describe the versions of third-party and open source public images for Windows and Linux provided by Alibaba Cloud. Windows images

| Operating system | Operating system version |
|---|---|
| Windows Server 2019 | Windows Server 2019 Datacenter 64-bit (Simplified Chinese) Windows Server 2019 Datacenter 64-bit (English) |
| Windows Server 2016 | Windows Server 2016 Datacenter 64-bit (Simplified Chinese) Windows Server 2016 Datacenter 64-bit (English) |

| Operating system | Operating system version |
|---|---|
| Windows Server 2012 | Windows Server 2012 R2 Datacenter 64-bit (Simplified Chinese) Windows Server 2012 R2 Datacenter 64-bit (English) |
| Windows Server Version 2004 | Windows Server Version 2004 Datacenter 64-bit (Simplified Chinese) Windows Server Version 2004 Datacenter 64-bit (English) |

Linux images x86

| Operating system | Operating system version |
|---|---|
| Anolis OS | AnolisOS 8.2 RHCK AnolisOS 7.9 RHCK AnolisOS 8.4 RHCK AnolisOS 7.9 RHCK (Level 3 of MLPS 2.0) Anolis OS 7.9 ANCK Anolis OS 8.4 ANCK |
| CentOS (Intel) | CentOS 7.9 CentOS 7.2 CentOS 7.4 CentOS 7.5 CentOS 7.5 (SCC) CentOS 7.6 CentOS 7.6 (IPv6-enabled) CentOS 7.7 CentOS 7.8 (Trusted) CentOS 8.0 CentOS 8.1 CentOS 8.2 CentOS 8.5 |
| Debian (Intel) | Debian 9.6 Debian 9.9 Debian 9.13 |
| Ubuntu (Intel) | Ubuntu 16.04 Ubuntu 18.04 |

| Guide·Images | Elastic Compute Servic |
|---|---|

| Operating system | Operating system version |
|---|---|
| openSUSE (Intel) | openSUSE 15.3 |
| SUSE Linux | SUSE Linux Enterprise Server 11 SP4 SUSE Linux Enterprise Server 12 SP4 SUSE Linux Enterprise Server 12 SP5 SUSE Linux Enterprise Server 15 SP2 |
| Kylin (Hygon) | Kylin V10 0524 SP2 SHENLONG Kylin V10 SP1 Kylin V10 SP1 0518 |
| UOS (Hygon) | UOS Server 20 1021a UOS Server 20 1032d |
| NFS (Hygon) | NFS V4 |

ARM

| Operating system | Operating system version |
|---|---|
| Anolis OS | AnolisOS 7.9 RHCK AnolisOS 8.2 RHCK AnolisOS 8.4 RHCK AnolisOS 7.9 RHCK (Level 3 of MLPS 2.0) Anolis OS 7.9 ANCK Anolis OS 8.4 ANCK |
| CentOS | CentOS 7.6 CentOS 7.7 |
| Kylin | Kylin V10 SP1 0518 NeoKylin 7.0 |
| UOS | UOS Server 20 1040d UOS Server 20 1032d UOS Server 20 1021a |

Custom images Custom images are created from ECS instances or snapshots or imported from your computer. Custom images can contain applications and data. You can use custom images to create instances that have identical configurations. This eliminates the need to make repeated configurations. Shared images Shared images are the custom images that are shared to your organization by other accounts. Shared images do not count against the image quotas of organizations to which the images are shared. For more information, see Share a custom image. Find an image You can find an image based on its type, name, ID, or the ID of the snapshot from which the image was created. Then, you can use the image to create instances or perform other operations. For more information, see View images. Image formats ECS supports images in the VHD, RAW, and QCOW2 formats. Images in other formats must be converted to the supported formats before they can be run in ECS. For more information, see Convert the image file format.

### Create a custom image

You can create a custom image and use it to create identical instances or replace the system disks of existing instances. This way, you can quickly obtain multiple instances with the same operating system and data environment. Create a custom image from a snapshot You can create a custom image from a system disk snapshot to load the operating system and data environment of the snapshot to the image. Before you perform this operation, make sure that a system disk snapshot is used. You cannot create custom images from data disk snapshots.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the snapshot from which you want to create a custom image and click Creat e Cust om Image in
the Act ions column.
5. Configure the parameters listed in the following table to create a custom image.

| Parameter | Description |
|---|---|
| Cust om Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). _ It must start with a letter. |
| Sharing Scope | Select the scope in which to share the custom image. Current Organizat ion and Subordinat e Organizat ions Current Resource Set Current Organizat ion |

| Parameter | Description |
|---|---|
| Descript ion | Enter a description for the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

6. Click OK.
Create a custom image from an instance You can create a custom image from an instance to replicate the data of all disks of the instance, including the system disk and data disks. Not e To avoid data security risks, we recommend that you delete sensitive data from an instance before you use the instance to create a custom image. When you create a custom image from an instance, a snapshot is automatically generated for each disk on the instance, and all the snapshots constitute a complete custom image.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance from which you want to create a custom image and choose More > Creat e
Cust om Image in the Act ions column.
5. Configure the parameters listed in the following table to create a custom image.

| Parameter | Description |
|---|---|
| Cust om Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). _ It must start with a letter. |
| Sharing Scope | Select the scope in which to share the custom image. Current Organizat ion and Subordinat e Organizat ions Current Resource Set Current Organizat ion |
| Descript ion | Enter a description for the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

6. Click OK.

### View images

You can view a list of images.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a tab based on the type of images that you want to view.
You can select the Cust om Images or Public Images tab.
5. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Image Name | Enter an image name to search for the image. |
| Image ID | Enter an image ID to search for the image. |
| Snapshot ID | Enter a snapshot ID to search for images associated with the snapshot. This option is not available for public images. |

### View instances related to an

image You can view the instances that use a specified image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a tab based on the type of the image that you want to view.
You can select the Cust om Images or Public Images tab.
5. Find the image and click Relat ed Inst ances in the Act ions column.
Result The Instances page appears and shows the instances that use the image. You can perform operations on these instances, such as updating the image.

### Modify the description of a

custom image You can modify the descriptions of created custom images.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the custom image that you want to modify and click Modif y Descript ion in the Act ions
column.
5. In the Modify Description dialog box, modify the image description in the Basic Settings field.
The description must be 2 to 256 characters in length and cannot start with http:// or https://.
6. Click OK.

### Share a custom image

You can share a created custom image to the organizations that you manage. Then, the organizations can use the shared image to create multiple instances that have identical environments. Context Only custom images can be shared. Shared images do not count against the image quotas of the organizations to which the images are shared. The organizations to which images are shared can use the shared images to create instances or replace the system disks of existing instances. You can delete shared images. After a shared image is deleted, the image is no longer visible to the organizations to which the image was shared and the system disks of the instances created from this image can no longer be re-initialized.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the image that you want to share and click Share Image in the Act ions column.
5. In the Share Image dialog box, select a department from the Depart ment drop-down list.
Not e If no department list is available due to lack of permissions, you can enter the name of a level-1 organization in the Department field to share the image.
6. Click OK.

### Encrypt a custom image

This topic describes how to encrypt a custom image to generate a new identical encrypted custom image. Prerequisites The custom image that you want to encrypt is in the Available (Available) state. Context To meet the requirements for data security compliance, you can use encrypted custom images to create instances. The system disks of the created instances are automatically encrypted.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Cust om Images tab.
5. Find the custom image that you want to encrypt and click Encrypt Image in the Act ions column.
6. In the Encrypt Image dialog box, configure the parameters listed in the following table.

| Parameter | Description |
|---|---|
| Image ID | The system automatically obtains the ID of the image to be encrypted. You do not need to configure this parameter. |
| Cust om Image Name | Enter a name for the new encrypted custom image. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), periods (.), and hyphens (-). It must _ start with a letter. |
| Descript ion | Enter a description for the new encrypted custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

7. Click OK.
Result After you encrypt the custom image, a new identical encrypted custom image is generated and displayed on the Custom Images tab.

### Import custom images

#### Limits on importing images

This topic describes the limits on importing images. You must understand the limits to ensure that the imported images are available and make the import operation more efficient. When you import images, take note of the limits described in the following sections: Linux images Windows images Linux images When you import Linux images, take note of the following limits: Multiple network interfaces are not supported. IPv6 addresses are not supported. Each password must be 8 to 30 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Firewalls must be disabled. By default, port 22 is enabled. Each Linux system disk must range from 40 GiB to 500 GiB in size. DHCP must be enabled in the images. SELinux must be disabled. The Kernel-based Virtual Machine (KVM) driver must be installed. We recommend that you install cloud-init to configure hostnames, NTP sources, and YUM sources. Limits

| Item | Standard operating system image | Non-standard operating system image |
|---|---|---|
| Definition | The supported standard 32-bit and 64-bit operating systems include: CentOS Ubuntu SUSE openSUSE RedHat Debian CoreOS Aliyun Linux Not e Support for standard operating systems may be subject to version changes. You can log on to the ECS console to view the latest supported operating systems. | Non-standard operating systems include: Operating systems that are not supported by Alibaba Cloud Standard operating systems that do not meet the requirements on critical system configuration files, basic system environments, or applications To use non-standard operating system images, select Others Linux when you import images. If the images that you import are non- standard operating system images, Alibaba Cloud does not process the instances created from these images. After you create an instance from a non- standard operating system image, you must connect to the instance by using the VNC feature in the ECS console, and then configure the IP address, route, and password of the instance. |

| Item | Standard operating system image | Non-standard operating system image |
|---|---|---|
| Critical system configuration file | Do not modify /etc/issue* . Otherwise, the version of the operating system cannot be identified, which leads to a failure to create the system. Do not modify /boot/grub/men u.lst . Otherwise, the system fails to start. Do not modify /etc/fstab . Otherwise, partitions cannot be loaded, which causes the system to fail to start. Do not change /etc/shadow to read-only. Otherwise, the password file cannot be modified, which leads to a failure to create the system. Do not modify /etc/selinux/c onfig to enable SELinux. Otherwise, the system fails to start. | Requirements for standard operating system images are not met. |
| Basic system environment | Do not adjust the system disk partitions. Only disks with a single root partition are supported. Make sure that the system disk has sufficient free space. Do not modify critical system files such as /sbin , /bin , and /lib* . Before you import an image, confirm the integrity of the file system. Only ext3 and ext4 file systems are supported. |   |
| Application | Do not install qemu-ga on a custom image. Otherwise, some of the services that Alibaba Cloud uses may be unavailable. |   |

| /boot/grub/men |   |
|---|---|

|   | u.lst |
|---|---|

| /etc/selinux/c |   |
|---|---|

|   | onfig |
|---|---|

|   | /sbin |
|---|---|
| /lib* |   |

| User Guide·Images |   |   |
|---|---|---|
| Item | Standard operating system image | Non-standard operating system image |
| Image file format | Only images in the RAW, VHD, or QCOW2 format can be imported. To import images in other formats, use a tool to convert the images to a supported format. We recommend that you import images in the VHD format, which has a smaller transmission footprint. |   |
| Image file size | We recommend that you configure the system disk size based on the virtual disk size rather than the image size. The configured system disk size must be at least 40 GiB. |   |

Windows images When you import Windows images, take note of the following limits: Each password must be 8 to 30 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Imported Windows images do not provide the Windows Activation Service. Firewalls must be disabled. Otherwise, remote logon is not supported. Port 3389 must be enabled. Each Windows system disk must range from 40 GiB to 500 GiB in size. Limits

| Item | Description |
|---|---|

| Item | Description |
|---|---|
| Operating system version | Alibaba Cloud allows you to import the following 32-bit and 64- bit versions of Windows operating system images: Microsoft Windows Server 2016 Microsoft Windows Server 2012, including: Microsoft Windows Server 2012 R2 (Standard Edition) Microsoft Windows Server 2012 (Standard Edition and Datacenter Edition) Microsoft Windows Server 2008, including: Microsoft Windows Server 2008 R2 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2008 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2003, including: Microsoft Windows Server 2003 R2 (Standard Edition, Datacenter Edition, and Enterprise Edition) Microsoft Windows Server 2003 (Standard Edition, Datacenter Edition, and Enterprise Edition) or later, including Service Pack 1 (SP1) Microsoft Windows 7, including: Microsoft Windows 7 (Professional Edition) Microsoft Windows 7 (Enterprise Edition) Not e Support for standard operating systems may be subject to version changes. You can log on to the ECS console to view the latest supported operating systems. |
| Basic system environment | Multi-partition system disks are supported. Make sure that the system disk has sufficient free space. Do not modify critical system files. Before you import an image, confirm the integrity of the file system. Disks can be partitioned in the MBR format and formatted to NTFS file systems. |
| Application | Do not install qemu-ga on an imported image. Otherwise, some of the services that Alibaba Cloud uses may be unavailable. |

| Item | Description |
|---|---|
| Supported image file format | RAW VHD QCOW2 We recommend that you configure the system disk size based on the virtual disk size rather than the image size. The configured system disk size must range from 40 GiB to 500 GiB. Not e We recommend that you import images in the VHD format, which has a smaller transmission footprint. |

#### Convert the image file format

You can only import image files in the RAW, VHD, and qcow2 formats to ECS. If you want to import images in other formats, you must convert the image into a supported format. This topic describes how to convert the image format in Windows and Linux. Context You can use the qemu-img tool to convert an image from VMDK, VDI, VHDX, qcow1, or QED to RAW, VHD, or qcow2, or implement conversion between RAW, VHD, and qcow2. Not e We recommend that you use the qcow2 format if your application environment supports this format. Windows
1. Download qemu.
Visit QEMU Binaries for Windows (64 bit) to download the qemu tool. Select a qemu version based on your operating system.
2. Install qemu.
The installation path in this example is C:\Program Files\qemu.
3. Configure the environment variables for qemu.
i. Choose St art > Comput er, right-click Computer, and choose Propert ies from the shortcut menu. ii. In the left-side navigation pane, click Advanced Syst em Set t ings. iii. In the Syst em Propert ies dialog box that appears, click the Advanced tab and then click Environment Variables. iv. In the Environment Variables dialog box that appears, find the Pat h variable from the Syst em variables section. If the Pat h variable exists, click Edit . If the Pat h variable does not exist, click New. v. Add a system variable value. In the Edit System Variable dialog box that appears, add C:\Program Files\qemu to the Variable value field, separate different variable values with semicolons (;), and then click OK. In the New System Variable dialog box that appears, enter Path in the Variable name field, enter C:\Program Files\qemu in the Variable value field, and then click OK.
4. Open Command Prompt in Windows and run the `qemu-img --help` command. If a successful
response is displayed, the tool is installed.
5. In the Command Prompt window, run the `cd [Directory of the source image file]` command to
switch to a new file directory, for example, cd D:\ConvertImage .
6. In the Command Prompt window, run the `qemu-img convert -f raw -O qcow2 centos.raw centos.qc`
`ow2` command to convert the image file format. The parameters are described as follows: The `-f` parameter is followed by the source image format. The `-O` parameter (case-sensitive) is followed by the destination image format, source file name, and destination file name. After the conversion is complete, the destination file appears in the directory of the source image file. Linux
1. Install the qemu-img tool.
For Ubuntu, run the `apt install qemu-img` command. For CentOS, run the `yum install qemu-img` command.
2. Run the `qemu-img convert -f raw -O qcow2 centos.raw centos.qcow2` command to convert the
image file format. The parameters are described as follows: The `-f` parameter is followed by the source image format. The `-O` parameter (case-sensitive) is followed by the destination image format, source file name, and destination file name.

#### Import an image

After you upload a local image to an Object Storage Service (OSS) bucket, you can import the image as a custom image to Elastic Compute Service (ECS). Prerequisites An image is made. It meets the limits and requirements for image import and is in the RAW, VHD, or QCOW2 format. For more information, see Limits on importing custom images and Convert the image file format. You are authorized to import images. For more information, see the "RAM" chapter in Apsara Uni-man ager Management Console User Guide. A local image is uploaded to a bucket by using the OSS console or by calling an OSS API operation. For more information, see the "Upload objects" topic in OSS User Guide or the "PutObject" topic in OS S Developer Guide. Not e Make sure that the bucket resides in the region to which you want to import the image as a custom image.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Import Image.
5. Configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | The region to which to import the image as a custom image. |
| Organization | Yes | The organization in which to use the custom image. |
| Resource Set | Yes | The resource set to which to assign the custom image. |
| OSS Bucket Name | Yes | The name of the OSS bucket where the image to be imported is stored. |
| OSS Object Name | Yes | The URL of the object as which the image to be imported is stored in the OSS bucket. For information about how to obtain the URL of an OSS object, see the "Obtain object URLs" topic in O SS User Guide. |
| Image Name | Yes | The name of the custom image. The name must be 2 to 128 characters in length. It must start with a letter and can contain letters, periods (.), underscores ( ), and hyphens (-). _ |
| Sharing Scope | Yes | The scope in which to share the custom image. Current Organizat ion and Subordinat e Organizat ions Current Resource Set Current Organizat ion |
| Operating system | Yes | Valid values: Linux and Windows. |
| System Disk (GiB) | Yes | The size of the system disk on an instance. Unit: GiB. |
| System Architecture | Yes | Valid values: x86 64 and i386. _ |

| Ela | stic Compute Service |   | User Guide·Image | s |
|---|---|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| Platform | Yes | Linux: Cent OS Ubunt u SUSE OpenSUSE Debian CoreOS Aliyun Ot hers Linux Cust omized Linux Windows: Windows Server 2003 Windows Server 2008 Windows Server 2012 |
| Description | No | The description of the custom image. |
| Add Data Disk Image | No | Imports another image that contains data from data disks. If you select Add Data Disk Image, you must specify parameters including OSS Object Address, Image Format, Device Name, and Disk Capacity. |

6. Click OK.
Result You can go to the Images page to view the creation progress of the custom image. For more information, see View images. When the custom image is created, 100% is displayed in the Progress column.

### Export a custom image

You can export custom images to OSS buckets and then download the images to your local device. Prerequisites OSS is activated and an OSS bucket is created. For more information, see the "Create buckets" topic in OSS User Guide. You are authorized to export images. For more information, see the "RAM" chapter in Apsara Uni-man ager Management Console User Guide. Context You can export custom images to the RAW, VHD, or QCOW2 format. After a custom image is exported to an OSS bucket, you can download the image to your local device. For more information, see the "Obtain object URLs" topic in OSS User Guide.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the custom image that you want to export and click Export Image in the Act ions column.
5. Configure the parameters listed in the following table.

| Parameter | Required | Description |
|---|---|---|
| OssBucket | Yes | The name of the OSS bucket where to store the exported image. |
| Image T ype | No | The format in which to export the image. Valid values: RAW, VHD, and QCOW2. |
| OSS Pref ix | No | The prefix of the OSS object to which to export the image. must be 1 to 30 characters in length and can contain digits and letters. |

6. Click OK.

### Delete a custom image

You can delete custom images that are no longer needed. Custom images can be deleted but public images cannot.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Images.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete custom images:
To delete a single custom image, find the image and click Delet e Image in the Act ions column. To delete one or more custom images at a time, select the images and click Delet e in the lowerleft corner of the image list.
5. Click OK.

## Snapshots

### Overview

A snapshot is a copy of data on a disk at the point in time when the snapshot is created. Scenarios You can use snapshots in scenarios such as environment replication and disaster recovery: You may want to use the data of a disk as the source data for write operations or save data to a different disk. In this case, you can create a snapshot for a disk and then create another disk from the snapshot. The new disk contains the basic data of the original disk. Issues such as application errors or malicious read operations and write operations may occur on disks that store data. As a result, these disks require additional protection mechanisms. You can create snapshots at regular intervals to restore data to a previous point in time when data errors occur. How snapshots work Snapshots are created incrementally. This way, only the changed data between two snapshots is copied, as shown in Snapshots. Snapshots In this example, Snapshot 1, Snapshot 2, and Snapshot 3 are the first, second, and third snapshots of a disk. When a snapshot is created, the file system checks each block of data stored on the disk, and only copies the blocks of data that are different from those on the previous snapshots. The following section describes the changes between snapshots in the preceding figure: All data on the disk is copied to Snapshot 1 because it is the first disk snapshot. The changed blocks B1 and C1 are copied to Snapshot 2. Blocks A and D are referenced from Snapshot 1. The changed block B2 is copied to Snapshot 3. Blocks A and D are referenced from Snapshot 1, and block C1 is referenced from Snapshot 2. When you want to restore the disk to the state of Snapshot 3, blocks A, B2, C1, and D are copied to the disk. This way, the disk is restored to the state of Snapshot 3. If Snapshot 2 is deleted, block B1 in the snapshot is deleted, but block C1 is retained because it is referenced by other snapshots. When you roll back a disk to Snapshot 3, block C1 is restored. Not e Snapshots are stored in Object Storage Service (OSS), but are hidden from users. Snapshots do not occupy storage space in OSS buckets. Snapshots can be managed only in the ECS console or by using API operations.

### Create a snapshot

You can manually create snapshots for disks to back up disk data. Prerequisites The associated instance of the disk for which you want to create a snapshot is in the Running or St opped state. The disk is in the Running state. Context Up to 64 snapshots can be retained for each disk. Snapshots can be used in the following scenarios: Roll back data on disks For more information, see Restore a disk. Create a custom image For more information, see Create a custom image from a snapshot. Data disk snapshots cannot be used to create custom images. Create a data disk from a data disk snapshot To create a data disk from a snapshot, set Use Snapshot to Yes and then specify a snapshot on the Create Disk page. For more information, see Create a disk. The created disk size is determined by the size of the specified snapshot and cannot be changed. When you re-initialize a data disk created from a snapshot, the disk is restored to the state of the snapshot. When you create a snapshot, take note of the following items: For each disk, the first snapshot is a full snapshot and subsequent snapshots are incremental snapshots. It takes longer to create the first snapshot. The amount of time it takes to create an incremental snapshot depends on the volume of data that has been changed since the last snapshot. The more data that has changed, the longer it takes. Not e If you want to use a snapshot immediately after it is created, you can enable the instant access feature. We recommend that you create snapshots during off-peak hours.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Disks page, find the disk for which you want to create a snapshot and click Creat e Snapshot
in the Act ions column.
5. Enter a snapshot name and description and then click OK.

| Parameter | Description |
|---|---|
| Snapshot Name | The name of the snapshot. Not e The name cannot start with auto because snapshots whose names start with auto are recognized as automatic snapshots. |
| Inst ant Access | Specifies whether to enable the instant access feature. After you enable the instance access feature for a snapshot, you can immediately use the snapshot to perform operations such as rolling back the disk. |
| Descript ion | The description of the snapshot. |

You can go to the Snapshots page to check the creation progress of the snapshot. For more information, see View snapshots. When the snapshot is created, 100% is displayed in the Progress column.

### View snapshots

You can view the list of snapshots.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Snapshot Name | Enter a snapshot name to search for the snapshot. |
| Snapshot ID | Enter a snapshot ID to search for the snapshot. |
| Instance ID | Enter an instance ID to search for snapshots related to the instance. |
| Disk ID | Enter a disk ID to search for snapshots related to the disk. |

| Filter option | Description |
|---|---|
| Snapshot Type | Select a snapshot type to search for snapshots of that type. Valid values: All User Snapshot s: manual snapshots Aut omat ic Snapshot s: automatic snapshots |
| Creation Time | Enter a time to search for snapshots that were created at that time. |

### Restore a disk

If you have created snapshots for a disk, you can use one of the snapshots to restore the disk to the state when the snapshot was created. The disk restore operation is irreversible. After the disk is restored, the data stored on the disk before the restore operation is performed cannot be recovered. Exercise caution when you perform this operation. Prerequisites Snapshots are created for the disk that you want to restore. The disk is not released. The instance to which the disk is attached is in the St opped state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filtering option from the drop-down list, enter the relevant information in the search bar,
and click Search. You can select multiple filtering options to narrow down the search results.

| Filt ering opt ion | Descript ion |
|---|---|
| Snapshot Name | Enter a snapshot name to search for the snapshot. |
| Snapshot ID | Enter a snapshot ID to search for the snapshot. |
| Instance ID | Enter an instance ID to search for the snapshots related to the instance. |
| Disk ID | Enter a disk ID to search for the snapshots related to the disk. |

| Snapshot Type | Select a snapshot type to search for the snapshots of that type. Options include: All User Snapshot s: manual snapshots. Aut omat ic snapshot s: automatic snapshots. |
|---|---|
| Creation Time | Enter a creation time to search for the snapshots that were created at that time. |

5. Find the snapshot that you want to use to restore the specified disk and click Rest ore Disk in the
Act ions column.
6. Click OK.

### Create a custom image from a

snapshot You can create a custom image from a snapshot that contains the operating system and data of an Elastic Compute Service (ECS) instance. Then, you can use the custom image to create multiple identical instances. Prerequisites A system disk snapshot is created. For more information about how to create a system disk snapshot, see Create a snapshot. Context Before you create custom images from snapshots, take note of the following items: Notes on snapshots used to create custom images: A custom image can be created from a system disk snapshot and one or more data disk snapshots. You cannot use only data disk snapshots to create custom images. Both encrypted and unencrypted snapshots can be used to create custom images. Custom images cannot be used across regions.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Disk Snapshot s tab.
5. Find a snapshot whose property is displayed as Syst em Disk in the Disk T ype (All) column, and then
click Creat e Cust om Image in the Act ions column.
6. Configure the parameters described in the following table to create a custom image.

| Parameter | Description |
|---|---|
| Sharing Scope | Select the scope in which you want to share the custom image. Current Organizat ion and Subordinat e Organizat ions Current Resource Set Current Organizat ion |
| Image Name | Enter a name for the custom image. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). _ It must start with a letter. |
| Image Descript ion | The description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

7. Click OK.

### Delete a snapshot

You can delete snapshots that are no longer needed. Deleted snapshots cannot be recovered. You cannot delete system disk snapshots that have been used to create custom images.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete snapshots:
To delete a single snapshot, find the snapshot and click Delet e in the Act ions column. To delete one or more snapshots at a time, select the snapshots and click Delet e in the lower-left corner of the Snapshots page.
5. Click OK.
ups

## Snapshot-consistent groups

### Create a snapshot-consistent

group You can create a snapshot-consistent group to simultaneously create snapshots for one or more disks attached to an Elastic Compute Service (ECS) instance. When a business system spans multiple disks, you can create a snapshot-consistent group to ensure a consistent write order and crash consistency of business system data. Context You can create a snapshot-consistent group to simultaneously create snapshots for multiple disks attached to an ECS instance. Snapshot-consistent groups are applicable to cluster services. Example scenarios that snapshot-consistent groups support: A business system is deployed on multiple disks attached to an ECS instance, and point-in-time consistency and crash-consistency are required across databases or enterprise-level applications. For example, a MySQL cluster is built on ECS instances, a single Logical Volume Manager (LVM) logical volume is created across multiple volumes, or Oracle or SAP HANA clusters are migrated to the cloud. Snapshots need to be created simultaneously for multiple nodes of a distributed application system such as a large-scale website or a multi-application collaborative system. Disks on an ECS instance need to be batch backed up with high point-in-time consistency. Precautions Before you use the snapshot-consistent group feature, take note of the following items: When you create a snapshot-consistent group based on an instance, take note of the following items: To ensure that services are not affected, we recommend that you create the snapshot-consistent group during off-peak hours. The instance must be in the Running or St opped state. The disks for which to create a snapshot-consistent group can only be standard performance disks and premium performance disks and must be in the Running state. If the instance has disks of other categories attached, you can select only standard performance disks and premium performance disks on the instance to create a snapshot-consistent group. A single snapshot-consistent group can contain snapshots of up to 16 disks including the system disk and data disks and cannot exceed 32 TiB in size. Snapshots that you created are retained until they are deleted. We recommend that you delete unnecessary snapshots on a regular basis to prevent snapshot capacity from exceeding the limit. For more information, see Delete a snapshot. For the amount of time required to create a snapshot-consistent group, take note of the following items: ups The amount of time required to create a snapshot-consistent group depends on the sizes of the selected disks for which to create snapshots. The first snapshot of each disk is a full snapshot and takes longer to create than subsequent snapshots. Subsequent snapshots are incremental snapshots and do not take as long to be created as the first snapshot. The amount of time required varies based on the amount of data changed since the previous snapshot. If you want to use a snapshot while it is being created, you can enable the instant access feature.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Snapshots page, click the Snapshot -consist ent Groups tab. Then, click Creat e Snapshot -
consist ent Group.
5. In the Creat e Snapshot -consist ent Group dialog box, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Dat a Source | Select the instances based on which to create the snapshot-consistent group. |
| Disks | Select standard performance disks and premium performance disks for which you want to create a snapshot-consistent group. Up to 16 disks can be selected, including the system disk and data disks. The total size of the selected disks cannot exceed 32 TiB. |
| Group Name | Enter a name for the snapshot-consistent group for easy management. The name must be 2 to 128 characters in length and must start with a letter. It can contain letters, digits, periods (.), underscores ( ), hyphens (-), _ and colons (:) and cannot start with http:// or https://. |
| Descript ion | Enter a description for the snapshot-consistent group for easy management. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| Inst ant Access | The instance access feature can accelerate the process of snapshot creation. You can use the instant access feature to create snapshots within seconds. Enable Inst ant Access: You can select this check box to enable the instant access feature. By default, this feature is disabled. Durat ion of Inst ant Access: After you enable the instant access feature, you can specify a validity duration for the feature. The default validity duration is one day. The instant access feature is automatically disabled when the specified duration expires. |

What's next After the snapshot-consistent group is created, you can use it to roll back disks as needed. For more information, see Roll back disks by using a snapshot-consistent group. ups

### Roll back disks by using a

snapshot-consistent group After a snapshot-consistent group is created, you can use it to roll back one or more disks in the event of system failures or data errors caused by accidental operations. Prerequisites Before you use a snapshot-consistent group to roll back disks on an Elastic Compute Service (ECS) instance, make sure that the following requirements are met: A snapshot-consistent group is created based on the disks. For more information, see Create a snapshot-consistent group. Import ant The rollback operation cannot be reversed. If data changes were made to the disk from the time the snapshot-consistent group was created until the disk is rolled back, all these data changes are lost. To prevent data loss caused by accidental operations, we recommend that you create a snapshot-consistent group to back up disk data before you roll back disks. The instance to which the disks to be rolled back are attached is in the St opped state. For more information, see Stop an instance. The disks that correspond to the snapshots contained in the snapshot-consistent group have not been released or detached or do not have snapshots being created. The operating system of the instance has not been replaced since the snapshot-consistent group was created. The snapshots of the disks have not been deleted from the snapshot-consistent group. If the snapshot of a disk has been deleted from the snapshot-consistent group, the disk cannot be rolled back by using the snapshot-consistent group. The snapshot-consistent group can be used to roll back only other disks whose snapshots are contained in the group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Snapshot -consist ent Groups tab.
5. Find the snapshot-consistent group that you want to use and click Roll Back in the Act ions column.
6. In the Roll Back dialog box, perform the following operations:
i. Read the precautions about the rollback operation. Select St art Inst ance Immediat ely Af t er Rollback based on your business needs. ii. In the Disk Snapshot s section, select the snapshots of the disks that you want to roll back. iii. Click Roll Back. After the selected disks are rolled back, the `Rolled back.` message is displayed. Result ups After disks are rolled back, you can log on to their associated instances to check whether the disk data has been reverted to the state it was in when the snapshots were created.

### Delete a snapshot-consistent

group You can delete snapshot-consistent groups that are no longer needed.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage & Snapshot s > Snapshot s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Snapshot -consist ent Groups tab.
5. Find the snapshot-consistent group that you want to delete and click Delet e in the Act ions column.
6. In the message that appears, click Delet e.
cies

## Automatic snapshot policies

### Create an automatic snapshot

policy Automatic snapshot policies can be applied to system disks and data disks to create periodical snapshots of the disks. You can use automatic snapshot policies to improve data security and tolerance against operation faults. Context Automatic snapshot policies can effectively eliminate the following risks associated with manual snapshots: When applications such as personal websites or databases deployed on an ECS instance encounter attacks or system vulnerabilities, you may be unable to manually create snapshots. In this case, you can use the latest automatic snapshots to roll back the affected disks to restore your data and reduce loss. You can also specify an automatic snapshot policy to create snapshots before regular system maintenance tasks are performed. This eliminates the need to manually create snapshots and ensures that snapshots are always created before maintenance. You can retain up to 64 snapshots for each disk. If the maximum number of snapshots for a disk is reached while a new snapshot is being created, the system deletes the oldest automatic snapshot.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Policy.
5. Configure the parameters listed in the following table to create an automatic snapshot policy.

| Parameter | Required | Description |
|---|---|---|
| Region | Yes | The ID of the region in which to apply the automatic snapshot policy. |
| Organization | Yes | The organization in which to apply the automatic snapshot policy. |
| Resource Set | Yes | The resource set in which to apply the automatic snapshot policy. |
| Policy Name | Yes | The name of the automatic snapshot policy. The name must be 2 to 128 characters in length and cannot start with a special character or digit. It can contain periods (.), underscores ( ), hyphens (-), _ and colons (:). |

cies

| Parameter | Required | Description |
|---|---|---|
| Creation Time | Yes | The time of the day at which to create an automatic snapshot. Valid values: 00:00 to 23:00 (the start of each hour). You can select multiple values. Not e The default time zone for the snapshot policy is UTC+8. You can change the time zone to suit your business requirements. If the time scheduled for creating an automatic snapshot is due while a previous automatic snapshot is being created, the new snapshot creation task is skipped. This may occur when a disk contains a large volume of data. For example, assume that an automatic snapshot policy is applied to a disk that contains a large volume of data, and the policy specifies to create snapshots at 00:00, 01:00, and 02:00. If the system starts to create a snapshot at 00:00 and takes 70 minutes to complete the snapshot creation task, the system skips the automatic snapshot task scheduled for 01:00 and creates the next automatic snapshot at 02:00. |
| Frequency | Yes | The day of the week when to create automatic snapshots. The valid values range from Monday to Sunday. You can select multiple values. |
| Retention Policy | No | The retention period of the automatic snapshots. The default value is Keep for 30 Days. You can select one of the following options: Keep f or: You can select this option and then specify the number of days during which to retain the automatic snapshots. Valid values: 1 to 65536. Always Keep t he Snapshot s Unt il t he Number of Snapshot s Reaches t he Upper Limit : You can select this option to retain the automatic snapshots until the maximum number of snapshots is reached. |

6. Click OK.
What's next After the automatic snapshot policy is created, you must apply it to a disk for snapshots to be automatically created. For more information, see Configure an automatic snapshot policy for multiple disks.

### View automatic snapshot policies

cies You can view the list of automatic snapshot policies.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. View the list of automatic snapshot policies.

### Modify an automatic snapshot

policy You can modify the attributes of automatic snapshot policies. The attributes of each automatic snapshot policy that can be modified include the name, creation time, frequency, and retention policy.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to modify and click Modif y Policy in the Act ions
column.
5. Modify the attributes of the policy.
Changes made to the retention policy do not affect existing snapshots but take effect only on subsequent snapshots.
6. Click OK.

### Configure an automatic snapshot

policy After you apply an automatic snapshot policy to a disk, snapshots will be created automatically for the disk based on the policy settings. You can cancel an applied automatic snapshot policy at any time. Context We recommend that you configure the automatic snapshot policy to create automatic snapshots during off-peak hours. You can also manually create a snapshot for the disk that already has an automatic snapshot policy applied. When an automatic snapshot is being created, you must wait until the snapshot is complete before you can create a manual snapshot. The automatic snapshot is named in the following format: auto_yyyyMMdd_1, such as auto_20140418_1.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose St orage > Disks.
3. In the top navigation bar, select an organization, a resource set, and a region.
cies
4. Find the disk and click Conf igure Aut omat ic Snapshot Policy in the Act ions column.
5. Select a procedure based on the operation you want to perform on the policy.
To apply an automatic snapshot policy, turn on Aut omat ic Snapshot Policy, select a policy, and then click OK. To cancel an automatic snapshot policy, turn off Aut omat ic Snapshot Policy and click OK.

### Delete an automatic snapshot

policy You can delete automatic snapshot policies that are no longer needed. After you delete an automatic snapshot policy, the policy is automatically canceled for the disks that have it applied.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Snapshot s and Images > Aut omat ic Snapshot Policies.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the automatic snapshot policy that you want to delete and click Delet e Policy in the Act ions
column.
5. Click OK.

## Security groups

### Overview

A security group acts as a virtual firewall to control the inbound and outbound traffic of Elastic Compute Service (ECS) instances to improve security. Security groups provide Stateful Packet Inspection (SPI) and packet filtering capabilities. You can use security groups and security group rules to define security domains in the cloud. Security groups and security group rules A security group acts as a virtual firewall that is used to control access to and from one or more ECS instances. Each instance must belong to at least one security group. The following rules apply when you add instances to security groups: Each instance must belong to one or more security groups. The secondary ENIs that are bound to an instance can be assigned to security groups different from those of the instance. The rules of a security group control the inbound or outbound traffic to or from the instances in the security group. You can add or modify security group rules based on your business needs to implement fine-grained access control. New and modified rules are automatically applied to all instances within the security group. Security group rules can be used to control access to or from specific IP addresses, CIDR blocks, security groups, or prefix lists. If an instance belongs to multiple security groups, the rules of all the security groups are applied to the instance. When an access request destined for the instance is detected, the request is matched against applied security group rules one by one based on the rule attributes such as protocol, port range, and priority. No sessions are established until an Allow rule matches the request. Work with security groups You can perform the following operations to use security groups to control traffic for instances:
1. Create security groups.
2. Add rules to the security groups.
3. Add instances to the security groups.
4. Manage existing security groups and security group rules based on your needs.
Operations in the ECS console The following table describes the operations that you can perform in the ECS console to manage security groups.

| Operation | Description | References |
|---|---|---|
| Create a security group | You can create a security group. | Create a security group |

| Operation | Description | References |
|---|---|---|
| Add a security group rule | After you create a security group, you can add or modify security group rules to control inbound or outbound network access. | Add a security group rule |
| Add an ECS instance to a security group | You can add an instance to a security group to control network access in a centralized manner. | Add an instance to a security group |
| Manage security groups | You can query, modify, and delete security groups as well as remove instances from security groups. | View security groups Modify a security group Remove instances from a security group Delete a security group |
| Manage security group rules | You can modify, clone, export, import, and delete security group rules. | Modify a security group rule Clone a security group rule Export security group rules Import security group rules Delete a security group rule |

### Create a security group

Security groups are an important means for network security isolation. They implement network access control for one or more ECS instances. Prerequisites A virtual compute cloud (VPC) is created. For more information, see VPC User Guide. Context Security groups determine whether the instances in the same account that are deployed within the same VPC and region can communicate with each other. By default, if the instances belong to the same security group, they can communicate with each other over the internal network. If the instances belong to different security groups, you can authorize mutual access between the security groups to allow the instances to communicate with each other over the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Securit y Group.
5. Configure the parameters listed in the following table to create a security group.

| Type | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | Select an organization in which to create the security group. Make sure that the security group and the VPC belong to the same organization. |
|   | Resource Set | Yes | Select a resource set in which to create the security group. Make sure that the security group and the VPC belong to the same resource set. |
|   | Region | Yes | Select a region in which to create the security group. Make sure that the security group and VPC belong to the same region. |
|   | Zone | Yes | Select a zone in which to create the security group. |
| Basic Settings | VPC | Yes | Select a VPC in which to create the security group. |
|   | Security Group Name | No | Enter a name for the security group. The name must be 2 to 128 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), hyphens (-), colons (:), and _ commas (,). It cannot start with http:// or https://. |
|   | Description | No | Enter a description for the security group. To simplify future management operations, we recommend that you provide an informational description. The description must be 2 to 256 characters in length and start with a letter. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), and commas (,). It cannot start with http:// or https://. |

6. Click Submit .

### Add a security group rule

You can use security group rules to control access to and from the ECS instances in a security group over the Internet and the internal network.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group to which you want to add a rule and click Rules in the Act ions column.
5. Click Creat e Rule.
6. Configure the parameters listed in the following table to create a security group rule.

| Parameter | Required | Description |
|---|---|---|
| ENI Type | Yes | Valid value: Int ernal Net work ENI. In VPCs, you cannot find public NICs in ECS instances and can add only internal security group rules. However, the added security group rules apply to both the Internet and the internal network. |
| Direction | Yes | Out bound: access from the ECS instances in the current security group to other ECS instances on the internal network or to resources on the Internet. Inbound: access from other ECS instances on the internal network or from resources on the Internet to the ECS instances in the current security group. |
| Action | Yes | Allow: allows access requests on specified ports. Deny: discards requests received on specified ports without returning messages. If two security group rules are different only in the Action parameter, the Deny rule takes effect whereas the Allow rule is ignored. |
| Protocol | Yes | All: This value can be used in total trust scenarios. T CP: This value can be used to allow or deny traffic on one or several successive ports. UDP: This can be used to allow or deny traffic on one or several successive ports. ICMP: This value can be used when the ping command is used to test the status of the network connection between instances. ICMPv6: This value can be used when the ping6 command is used to test the status of the network connection between instances. GRE: This value can be used for VPN. |

| Parameter | Required | Description |
|---|---|---|
| Port Range | Yes | The port range depends on the protocol type. When you set Protocol to ALL, the value of -1/-1 is displayed, which indicates all ports. You cannot specify a port range in this case. When you set Protocol to T CP, you can specify a port range in the <start port number>/<end port number> format. Valid port numbers: 1 to 65535. You can set the start port number and end port number to the same value to specify a single port. For example, use 22/22 to specify port 22. When you set Protocol to UDP, you can specify a port range in the <start port number>/<end port number> format. Valid port numbers: 1 to 65535. You can set the start port number and end port number to the same value to specify a single port. For example, use 3389/3389 to specify port 3389. When you set Protocol to ICMP, the value of -1/-1 is displayed, which indicates all ports. You cannot specify a port range in this case. When you set Protocol to ICMPv6, the value of -1/-1 is displayed, which indicates all ports. You cannot specify a port range in this case. When you set Protocol to GRE, the value of -1/-1 is displayed, which indicates all ports. You cannot specify a port range in this case. |
| Priority | Yes | The priority of the rule. Valid values: 1 to 100. The default value is 1, which indicates the highest priority. |
| Authorization Type | Yes | IPv4 Addresses: IPv4 addresses or CIDR blocks. IPv6 Addresses: IPv6 addresses or CIDR blocks. Securit y Groups: security groups. This authorization type takes effect only on the internal network. You can select another security group in the current account as the authorization object for the instances in the current security group. This way, you can control the access to or from the ECS instances in that security group over the internal network. |

| Parameter | Required | Description |
|---|---|---|
| Authorization object | Yes | Authorization objects depend on the authorization type. When you set Authorization Type to IPv4 Addresses: Enter single IPv4 addresses or CIDR blocks. Example: 192.0.2.1 or 19 2.0.2.0/24. You can enter up to 10 authorization objects at a time. Separate multiple objects with commas (,). If you enter 0.0.0.0/0, all IPv4 addresses are allowed or denied based on the Action parameter. Exercise caution when you specify 0.0.0.0/0. When you set Authorization Type to IPv6 Addresses: Enter single IPv6 addresses or CIDR blocks. Example: 2001:db8:1:1: 1:1:1:1 or 2001:db8::/32. You can enter up to 10 authorization objects at a time. Separate multiple objects with commas (,). If you enter ::/0, all IPv6 addresses are allowed or denied based on the Action parameter. Exercise caution when you specify ::/0. When you set Authorization Type to Securit y Groups, select a security group ID. If the current security group is of the VPC type, the selected security group must be in the same VPC as the current security group. |
| Description | No | The description of the security group rule. To simplify future management operations, we recommend that you provide an informational description. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

7. Click OK.

### Add an instance to a security

group You can add an existing instance to a security group in the same region. After the instance is added, the rules of the security group automatically apply to the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group to which you want to add an instance and click Manage Inst ances in the
Act ions column.
5. Click Add Inst ance.
6. Select an instance and click OK.

### Manage security groups

#### View security groups

You can view the list of security groups.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Security Group ID | Enter a security group ID to search for the security group. |
| Security Group Name | Enter a security group name to search for the security group. |
| VPC ID | Enter a VPC ID to search for security groups that belong to the VPC. |

#### Modify a security group

You can modify the names and descriptions of created security groups.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group that you want to modify and click Modif y in the Act ions column.
5. Modify the name and description of the security group.
6. Click OK.

#### Remove instances from a security group

You can remove instances from security groups, but each of the instances must always belong to at least one security group. Prerequisites The instances to be removed belong to two or more security groups. Context After an instance is removed from a security group, the instance is isolated from the other instances in the security group. We recommend that you perform all tests in advance to ensure that services can continue to run properly after you remove the instance from the security group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group from which you want to remove instances and click Manage Inst ances in the
Act ions column.
5. On the Instances page, select one or more instances and click Remove in the lower-left corner.
6. Click OK.

#### Delete a security group

You can delete security groups that are no longer needed. Prerequisites No instances exist in the security group that you want to delete.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Use one of the following methods to delete security groups:
To delete a single security group, find the security group and click Delet e in the Act ions column. To delete one or more security groups at a time, select the security groups and click Delet e in the lower-left corner of the Security Groups page.
5. Click OK.

### Manage security group rules

#### Modify a security group rule

You can modify improper rules in a security group to ensure the security of ECS instances in the security group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Find the target security group rule and click Modif y in the Act ions column.
7. In the Modif y Securit y Group Rule dialog box, modify the attributes of the security group rule.
For more information about the attributes of security group rules, see Add a security group rule.
8. Click OK.

#### Clone a security group rule

You can clone a security group rule to quickly create a similar rule.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Find the target security group rule and click Clone in the Act ions column.
7. In the Clone Securit y Group Rule dialog box, modify the attributes of the security group rule.
For more information about the attributes of security group rules, see Add a security group rule.
8. Click OK.

#### Export security group rules

You can export security group rules of a security group to a local device for backup.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the target security group and click Rules in the Act ions column.
5. On the Rules page that appears, click the Inbound or Out bound tab.
6. Click Export in the upper-right corner to download and save the rules to a local device.

#### Import security group rules

You can import a local backup file of security group rules into a security group to create or restore security group rules. Context You can first download a template file (Excel file), configure security group rules in the template file based on the template requirements, and then import the file.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Security Groups page, find the security group into which you want to import rules and click
Rules in the Act ions column.
5. Click Import in the upper-right corner.
6. In the Import Rule dialog box, click Upload File.
7. Select a local backup file of security group rules and click Open.

#### Delete a security group rule

You can delete security group rules that are no longer needed from a security group.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > Securit y Groups.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the security group from which you want to delete a rule. Click Manage Rules in the Act ions
column.
5. On the Rules tab, click the Inbound or Out bound tab.
6. Use one of the following methods to delete a security group rule:
To delete a single rule, find the rule and click Delet e in the Act ions column. To delete one or more rules at a time, select the rules and click Delet e in the lower-left corner of the tab.
7. In the message that appears, click Delet e.

## RAM role management

### Attach an instance RAM role to

an ECS instance This topic describes how to attach an instance RAM role to an Elastic Compute Service (ECS) instance. Prerequisites An instance RAM role is created. For more information, see Create an instance RAM role in Apsara Unimanager Management Console User Guide. The ECS instance to which you want to attach a RAM role is located in a virtual private cloud (VPC). Not e An instance RAM role can be attached to a single instance at a time.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to attach a RAM role, click the
icon in the Act ions column, and then choose Inst ance Set t ings > At t ach/Det ach RAM Role.
5. In the Attach/Detach RAM Role dialog box, select the RAM role from the RAM Role drop-down list
and click OK.

### Replace the instance RAM role of

an ECS instance After you attach an instance RAM role to an Elastic Compute Service (ECS) instance, you can replace the role at anytime.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the ECS instance that has an instance RAM role attached, click the
icon in the Act ions column, and then choose Inst ance Set t ings > At t ach/Det ach RAM Role.
5. Set Operat ion T ype to At t ach. Select another instance RAM role from the RAM Role drop-down
list and click OK to replace the role.

### Detach an instance RAM role

from an ECS instance After you attach an instance RAM role to an Elastic Compute Service (ECS) instance, you can detach the role from the instance at anytime.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find an ECS instance that has an instance RAM role attached, click the
icon in the Act ions column, and then choose Inst ance Set t ings > At t ach/Det ach RAM Role.
5. Set Operat ion T ype to Det ach and click OK to detach the role.
es

## Elastic Network Interfaces

### Overview

An elastic network interface (ENI) is a virtual network interface controller (NIC) that can be bound to an Elastic Compute Service (ECS) instance of the Virtual Private Cloud (VPC) type. You can use ENIs to deploy high-availability clusters and perform low-cost failover and fine-grained network management. Attributes An ENI is a virtual network interface that must be bound to an instance of the VPC type before the ENI can be used. The following table describes the attributes of an ENI.

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

Features An ENI is an independent virtual NIC that can be migrated between multiple instances to support the flexible scaling and migration of services. When you create an ENI together with an instance, the ENI is automatically bound to the instance. You can also separately create a secondary ENI and bind it to an instance. es ENIs have the following features: In addition to the primary ENI that is created together with an instance, you can also bind multiple secondary ENIs to the instance. The ECS instance and the secondary ENIs that you want to bind to the instance must reside within the same zone and VPC, but can be connected to different vSwitches and belong to different security groups. Each ENI can be assigned multiple secondary private IP addresses based on the instance type of the instance to which the ENI is bound. When you unbind a secondary ENI from an instance and bind the ENI to another instance, the attributes of the ENI remain unchanged and the network traffic is redirected to the new instance. ENIs support hot-plug and can be migrated among instances. When you unbind an ENI from an instance and bind the ENI to another instance, services on the instances are not affected, and you do not need to restart the instances. Limits The following limits apply to ENIs: Each ENI can be assigned only a single primary private IP address. Each ENI can be assigned one or more secondary private IP addresses. The number of secondary private IP addresses is determined based on the instance type of the instance to which the ENI is bound. Each ENI can be assigned one or more EIPs. The number of EIPs is determined based on how the EIPs are associated with the ENI. For more information, see the "Create a VPC" and "Create a vSwitch" topics in Apsara Stack VPC User Guide. Each ENI must be added to at least one security group and can be added to up to five security groups. ENIs that can be created per region in an account is limited. The ENI quota is displayed on the Quot a overview page of the Apsara Uni-manager Management Console. The ENI and the instance to which the ENI is bound must reside within the same zone and VPC, but can belong to different vSwitches and security groups. The number of secondary ENIs that can be bound to an ECS instance is determined based on the instance type. The instance bandwidth is determined based on the instance type. You cannot increase the bandwidth of an ECS instance by binding multiple secondary ENIs to the instance. Use scenarios ENIs are suitable for the following scenarios: Deployment of high-availability clusters To implement a high-availability architecture, you can bind multiple ENIs to a single ECS instance. Low-cost failover You can unbind an ENI from a failed ECS instance and bind it to another normal instance to redirect traffic destined for the failed instance to the normal instance and immediately recover services. Fine-grained network management es You can configure multiple ENIs for an instance. For example, you can use some ENIs for internal management and other ENIs for Internet business access to isolate management data from business data. You can also configure specific security group rules for each ENI based on the source IP addresses, protocols, and ports to achieve access control. Configuration of multiple private IP addresses for a single instance You can assign multiple secondary private IP addresses to an ENI. If multiple applications are managed on your instance, you can assign an independent IP address for each application to improve the utilization of your instance. Configuration of multiple public IP addresses for a single instance Only a single public IP address can be assigned to an ECS instance that has no ENIs bound. To assign multiple public IP addresses to an instance, you can associate EIPs with one or more ENIs of the instance. In NAT mode, each private IP address of an ENI can have EIPs associated.

### Create an ENI

You can bind elastic network interfaces (ENIs) to instances to create high-availability clusters and implement fine-grained network management. You can also unbind an ENI from an instance and then bind the ENI to another instance to implement a low-cost failover solution. Prerequisites A virtual private cloud (VPC) and a VSwitch are created. For more information, see Create a VPC and Create a VSwitch in Apsara Stack VPC User Guide . A security group is available in the VPC. If no security group is available in the VPC, create a security group. For more information, see Create a security group. Context ENIs are classified into primary and secondary ENIs. A primary ENI is created by default when an instance is created in a VPC. This primary ENI has the same lifecycle as the instance and cannot be unbound from the instance. ENIs created separately are secondary ENIs. You can bind secondary ENIs to or unbind them from instances. This topic describes how to create a secondary ENI.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e ENI.
5. Configure parameters listed in the following table to create an ENI.

| Section | Parameter | Required | Description |
|---|---|---|---|
|   | Organization | Yes | The organization in which to create the ENI. |

| r Guide·Elastic Network Int |   |   |   |
|---|---|---|---|
|   | erfac Elastic Compute Servic |   |   |
| Section | Parameter | Required | Description |
| Region | Resource Set | Yes | The resource set in which to create the ENI. |
|   | Region | Yes | The region in which to create the ENI. |
|   | Zone | Yes | The zone in which to create the ENI. |
| i i | VPC | Yes | The VPC in which to create the ENI. The secondary ENI can be bound only to an instance in the same VPC. Not e After the ENI is created, you cannot change its VPC. |
|   | VSwitch | Yes | The VSwitch to be associated with the ENI. The secondary ENI can be bound only to an instance in the same VPC. Select a VSwitch that is in the same zone as the instance to which the ENI will be bound. The VSwitch of the ENI can be different from that of the instance. Not e After an ENI is created, you cannot change its VSwitch. |
|   | Security Group | Yes | The security group in which to create the ENI within the specified VPC. The rules of the security group automatically apply to the ENI. |

es

|   | e |   |   |
|---|---|---|---|
| Basic Settings Section | Parameter | Required | Description |
|   | ENI Name | Yes | The name of the ENI. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |
|   | Description | No | The description of the ENI. We recommend that you provide an informational description to simplify future management operations. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, periods (.), underscores ( ), _ hyphens (-), colons (:), and commas (,). |
|   | Primary Private IP | No | The primary private IPv4 address of the ENI. The IPv4 address must be within the CIDR block of the specified VSwitch. If you do not specify a primary private IP address, the system automatically assigns a private IP address to the ENI. |

6. Click Submit .
Result The created ENI is displayed on the ENIs page and is in the Available state. es

### Bind a secondary ENI to an

instance You can bind a secondary elastic network interface (ENI) to an instance. After the ENI is bound, the instance can process the traffic on the ENI. Prerequisites The secondary ENI that you want to bind is in the Available state. The instance to which you want to bind the secondary ENI is in the Running or St opped state. The instance and the secondary ENI belong to the same virtual private cloud (VPC). The vSwitch with which the secondary ENI is associated is located within the same zone as the vSwitch to which the instance is connected. An ENI can be bound only to an instance within the same zone. The vSwitches of the ENI and of the instance can be different but must be located within the same zone. Context The following limits apply when you bind an ENI to an instance: Only secondary ENIs can be manually bound. Primary ENIs share the same lifecycle as instances and cannot be manually bound. An ENI can be bound only to a single instance at the same time. Each instance can have one or more bound ENIs. The maximum number of ENIs that can be bound to an instance is determined based on the instance type. Bind a secondary ENI on the instance details page To bind multiple secondary ENIs to an instance, you can go to the details page of the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance to which you want to bind a secondary ENI and click the instance ID.
5. Click the ENIs tab.
6. Click Bind NIC.
7. In the Bind NIC dialog box, select an ENI from the ENI drop-down list.
8. Click OK.
Bind a secondary ENI on the ENIs page To bind secondary ENIs to multiple instances, you can go to the ENIs page.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI that you want to bind and click Bind in the Act ions column.
5. In the Bind dialog box, select an instance and click OK.
es In the St at us/Creat ion T ime column, the state of the secondary ENI changes to Bound.

### Configure a secondary ENI

After secondary elastic network interfaces (ENIs) are bound to Elastic Compute Service (ECS) instances, some images used by these instances may not recognize the IP addresses of these ENIs or configure routes for the ENIs. If this occurs, the secondary ENIs cannot be used on the instances. This topic describes how to configure secondary ENIs from within instances to have their IP addresses recognizable and how to configure routes for the secondary ENIs. Prerequisites A secondary ENI is bound to an ECS instance. For information about how to bind a secondary ENI to an ECS instance, see Bind a secondary ENI to an instance. You are connected to the ECS instance. For information about how to connect to an ECS instance, see Instance connecting overview. Context If automatic configuration tools are pre-installed on the images that are used by instances, secondary ENIs that are bound to the instances can be automatically configured by the tools. You can use these secondary ENIs without the need to manually configure them. Skip the topic if your instance uses an image of one of the following versions: Alibaba Cloud Linux 3.2104 64-bit CentOS 8.0 64-bit, CentOS 8.1 64-bit, and CentOS 8.2 64-bit CentOS 7.3 64-bit, CentOS 7.4 64-bit, and CentOS 7.5 64-bit CentOS 6.8 64-bit and CentOS 6.9 64-bit Debian 10.5 64-bit and Debian 10.6 64-bit Windows Server 2008 R2 and later
1. Check whether the IP addresses of a secondary ENI bound to an instance are recognized.
For more information, see Check whether the IP addresses of ENIs are recognized. If yes, skip the following steps. If not, proceed with the following steps to configure the secondary ENI.
2. Obtain the information of the secondary ENI.
When you configure a secondary ENI, you may need to specify its information, such as the primary private IP address and media access control (MAC) address. Obtain the information required for subsequent configurations. For more information, see Obtain the information of an ENI. In the examples provided in this topic, the sample values listed in the following table are used. In actual scenarios, replace them with the attribute values of your secondary ENI.

| Secondary ENI attribute | Sample value |
|---|---|
| ENI name | eth1 |
| MAC address | 00:16:3e:0f:**:** |
| Primary private IP address | 192.168.**.*2 |

|   | Elastic Compute Servic |
|---|---|

es

| Secondary ENI attribute | Sample value |
|---|---|
| Subnet mask | 255.255.255.0 |
| Gateway address | 192.168.**.253 |

3. Configure the secondary ENI to have its IP address recognized.
The operations required to configure secondary ENIs vary based on the operating systems of the instances to which the secondary ENIs are bound.

| Operating system | References |
|---|---|
| Alibaba Cloud Linux 2 (Instances that run this operating system use the network-scripts network service) CentOS | Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service |
| Alibaba Cloud Linux 2 (Instances that run this operating system use the systemd-networkd network service) | Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2 operating system and uses the systemd-networkd network service |
| Ubuntu Debian | Configure a secondary ENI for an instance that runs a Ubuntu or Debian operating system |
| SUSE openSUSE | Configure a secondary ENI for an instance that runs a SUSE or openSUSE operating system |

4. Check whether routes are configured for the secondary ENI.
You can run the `route -n` command to check route information. If no routes are configured for the secondary ENI or if the existing routes do not meet your requirements, manually configure routes for the secondary ENI. The following sections provide examples on how to configure routes for a secondary ENI that is bound to an instance that runs one of the following operating systems: Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system Configure routes for a secondary ENI of an instance that runs a CentOS 8 operating system Check whether the IP addresses of ENIs are recognized Run the following command to check whether the IP addresses of ENIs are recognized:

```
ip address show
```

Sample command outputs: The following command output shows that the IP address of the eth0 primary ENI is recognized but the IP address of the eth1 secondary ENI is not recognized. You can perform operations described in this topic to configure the secondary ENI. es The following command output shows that the IP addresses of both the eth0 primary ENI and the eth1 secondary ENI are recognized. You do not need to configure the secondary ENI. Not e In the preceding command outputs, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI. Obtain the information of an ENI You can obtain the information of an ENI from instance metadata, by using the ECS console, or by calling an API operation. Obtain the information of an ENI from instance metadata. Obtain the MAC addresses of the ENIs that are bound to an instance.

```bash
curl http://100.100.100.200/latest/meta-data/network/interfaces/macs/
```

Not e The MAC addresses of ENIs are required to obtain their primary private IP addresses, subnet masks, and gateway addresses. Obtain the primary private IP address of the specified ENI.

```bash
curl http://100.100.100.200/latest/meta-data/network/interfaces/macs/00:16:3e:19:**:**/ primary-ip-address
```

Obtain the subnet mask of the specified ENI.

```bash
curl http://100.100.100.200/latest/meta-data/network/interfaces/macs/00:16:3e:19:**:**/ netmask
```

es Obtain the gateway address of the specified ENI.

```bash
curl http://100.100.100.200/latest/meta-data/network/interfaces/macs/00:16:3e:19:**:**/ gateway
```

The following figure shows sample command outputs. In the command outputs, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI. Not e After you run the `ip address show` command, you can determine which is the primary ENI and which is the secondary ENI based on the order in which the MAC addresses are displayed in the command output. Obtain the information of an ENI by using the ECS console. i. Log on to the ECS console. ii. In the left-side navigation pane, choose Net work & Securit y > ENIs. iii. On the ENI page, find the ENI whose information you want to query and view its primary private IP address and MAC address in the Private IP Address and ENI Type/MAC Address columns. The following figure shows an example of the ENI page in the ECS console. Obtain the information of an ENI by using an Alibaba Cloud SDK to call the DescribeNetworkInterfaces operation.

```
aliyun ecs DescribeNetworkInterfaces \ --output cols=MacAddress,PrivateIpAddress rows=NetworkInterfaceSets.NetworkInterfaceSet[]
```

\

```
--RegionId 'cn-qingdao-****-d01' \ --InstanceId 'i-bp1a5gj0bzhwz7q****'
```

The following figure shows the sample response. In the response, `00:16:3e:16:**:**` is the MAC address of the primary ENI and `00:16:3e:0f:**:**` is the MAC address of the secondary ENI. Not e After you run the `ip address show` command, you can determine which is the primary ENI and which is the secondary ENI based on the order in which the MAC addresses are displayed in the command output. es Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service If your instance runs an Alibaba Cloud Linux 2, CentOS 6, or CentOS 7 operating system and uses the network-scripts network service, you can use the multi-nic-util tool to have the ENIs of the instance automatically configured or you can manually configure the ENIs by modifying their configuration files. Use the multi-nic-util tool to have a secondary ENI automatically configured. Not e If you want to use the multi-nic-util tool to have secondary ENIs automatically configured for CentOS instances, note that the multi-nic-util tool is supported only on some versions of CentOS images. If your instance uses a CentOS 6 image, make sure that the image version is CentOS 6.8 or later. If your instance uses a CentOS 7 image, make sure that the image version is CentOS 7.3 or later. If the multi-nic-util tool is not supported on the image version that your instance uses, manually configure secondary ENIs by modifying their configuration files. i. Download and install the multi-nic-util tool.

```
wget https://image-offline.oss-cn-hangzhou.aliyuncs.com/multi-nic-util/multi-nic-util-0 .6.tgz && \ tar -zxvf multi-nic-util-0.6.tgz && \ cd multi-nic-util-0.6 && \ bash install.sh
```

ii. Restart the ENI service.

```bash
systemctl restart eni.service
```

Manually configure a secondary ENI by modifying its configuration file. i. Open the configuration file of the secondary ENI.

```
vi /etc/sysconfig/network-scripts/ifcfg-eth1
```

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. The following section provides an example of the ENI information to add to the configuration file: es

```
DEVICE=eth1 # Specify the ENI that you want to configure. BOOTPROTO=dhcp ONBOOT=yes TYPE=Ethernet USERCTL=yes PEERDNS=no IPV6INIT=no PERSISTENT_DHCLIENT=yes HWADDR=00:16:3e:0f:**:** # Enter the obtained MAC address of the ENI. DEFROUTE=no # Specify not to use the ENI as the default route. To prevent the default route of the ECS instance from being changed when you run the ifup command to start the secondary ENI, do not set eth1 as the default route.
```

iii. Restart the network service. For versions earlier than CentOS 7, such as CentOS 6, run the following command:

```
service network restart
```

For CentOS 7 or later and Alibaba Cloud Linux 2, run the following command:

```bash
systemctl restart network
```

Not e After you configure the secondary ENI, you can configure routes for the ENI. For more information, see Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system. If you want to create custom images from the instance whose ENIs are configured, you must first run the /et c/eni_ut ils/eni-cleanup command to remove network configurations from /etc/udev/rules.d/70-persistent-net.rules and /etc/sysconfig/network-scripts/. Configure a secondary ENI for an instance that runs an Alibaba Cloud Linux 2 operating system and uses the systemd-networkd network service If your instance runs an Alibaba Cloud Linux 2 operating system and uses the systemd-networkd network service, you must manually configure a secondary ENI by modifying the configuration file of the ENI.
1. Open the configuration file of the secondary ENI.

```
vi /etc/systemd/network/60-eth1.network
```

2. Add the information of the secondary ENI to the configuration file. Then, save and close the
configuration file. You can use one of the following methods to assign a dynamic or static IP address to the secondary ENI based on your requirements. The following section provides examples of the ENI information to add to the configuration file when different methods are used: Assign a dynamic IP address to the secondary ENI by using the Dynamic Host Configuration Protocol (DHCP). es

```
[Match] Name=eth1 # Specify the ENI that you want to configure. [Network] DHCP=yes [DHCP] UseDNS=yes
```

Assign a static IP address to the secondary ENI.

```
[Match] Name=eth1 # Specify the ENI that you want to configure. [Network] Address=192.168.**.*2/24 # Specify the static IP address and subnet mask to be assigned
```

`.` Not e In the preceding example, `192.168.**.*2` is the primary private IP address and the `/24` subnet mask is `255.255.255.0` .
3. Restart the network service.

```bash
systemctl restart systemd-networkd
```

Configure a secondary ENI for an instance that runs a Ubuntu or Debian operating system If your instance runs a Ubuntu or Debian operating system, you must configure a secondary ENI by modifying the network interface controller (NIC) configuration file based on your image version. Perform the following operations on an instance that runs a Ubuntu 14.04, Ubuntu 16.04, or Debian operating system: i. Open the NIC configuration file.

```
vi /etc/network/interfaces
```

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. The following section provides an example of the ENI information to add to the configuration file:

```
auto eth0 iface eth0 inet dhcp auto eth1 # Specify the ENI that you want to configure. iface eth1 inet dhcp
```

Not e The eth0 primary ENI is configured in the same configuration file as the eth1 secondary ENI. You must also add the information of the primary ENI to the configuration file. iii. Restart the network service. For versions earlier than Ubuntu 16.04, such as Ubuntu 14.04, run the following command:

```
service networking restart
```

es For Ubuntu 16.04 and Debian, run the following command:

```bash
systemctl restart networking
```

The configurations of the secondary ENI take effect regardless of whether the following alert notification appears. You can run the `ip address show` command to check whether the IP addresses of the secondary ENI are recognized. Perform the following operations on an instance that runs Ubuntu 18.04: i. Open the configuration file of the secondary ENI.

```
vi /etc/netplan/eth1-netcfg.yaml
```

ii. Add the information of the secondary ENI to the configuration file. Then, save and close the configuration file. Not e When you modify the configuration file, take note of the following items: The configuration file is in the `YAML` format. You must follow the `YAML` syntax rules when you configure the file. Tabs cannot be used for indentation in `YAML` files. Use spaces instead. We recommend that you copy information from the default /etc/netplan/99-netcfg.ya ml configuration file to prevent format issues. The following section provides an example of the ENI information to add to the configuration file:

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

Configure a secondary ENI for an instance that runs a SUSE or openSUSE operating system If your instance run a SUSE or openSUSE operating system, you must manually configure a secondary ENI by modifying its configuration file.
1. Open the configuration file of the secondary ENI.

```
vi /etc/sysconfig/network/ifcfg-eth1
```

2. Add the information of the secondary ENI to the configuration file. Then, save and close the
configuration file. In the following example, a dynamic IP address is assigned to the secondary ENI by using DHCP. es

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

Configure routes for a secondary ENI of an instance that runs an Alibaba Cloud Linux 2 or CentOS 7 operating system If you manually configure secondary ENIs but do not configure routes for them or if routes configured by the multi-nic-util tool do not meet your requirements, perform the following steps to configure routes.
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

| Use es | r Guide·Elastic Network Interfac | Elastic Compute Servic | e |
|---|---|---|---|

| Secondary ENI attribute | Sample value |
|---|---|
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

The following figure shows that the route table and routing policy are created.
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

Configure routes for a secondary ENI of an instance that runs a CentOS 8 operating system If routes configured by the system do not meet your requirements, perform the following steps to configure routes. es
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

3. Create a script for configuring routes.
i. Create and open the /root/route.sh file. es ii. Add the configuration information of the routes to the /root/route.sh file. Then, save and close the file. The following section shows how to create a route table and attach a routing policy to the route table for the eth1 secondary ENI. In this example, a route table named table 1001 is created. 192.1 68.**.253 is the gateway address and 192.168.*.*2 is the primary private IP address of the eth1 secondary ENI.

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
After you perform the preceding steps to configure routes for the eth1 secondary ENI, you must perform the following steps to configure the routes to automatically update on instance startup. Otherwise, the routes become invalid when the instance is restarted. es i. Open the /etc/rc.local file.

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

You can view the list of ENIs.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| ENI Name | Enter an ENI name to search for the ENI. |
| ENI ID | Enter an ENI ID to search for the ENI. |
| VSwitch ID | Enter a vSwitch ID to search for ENIs that are associated with the vSwitch. |
| Security Group ID | Enter a security group ID to search for ENIs that belong to the security group. |
| Instance ID | Enter an instance ID to search for ENIs that are bound to the instance. |

### Modify a secondary ENI

You can modify the attributes of a secondary elastic network interface (ENI), including the name, security group, and description. Prerequisites The secondary ENI is in the Available state. es
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI and click Modif y in the Act ions column.
5. In the Modify ENI dialog box that appears, modify the name, security group, and description of the
ENI.
6. Click OK.

### Unbind a secondary ENI from an

instance You can unbind a secondary elastic network interface (ENI) from an instance. After the secondary ENI is unbound from the instance, the instance no longer processes the traffic on the ENI. Prerequisites The secondary ENI is in the Bound state. The instance is in the Running or St opped state. Context Only secondary ENIs can be unbound. Primary ENIs share the same lifecycle as instances and cannot be unbound.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI and click Unbind in the Act ions column.
5. Click OK.
Result In the St at us/Creat ion T ime column, the status of the secondary ENI changes to Available.

### Delete a secondary ENI

You can delete a secondary elastic network interface (ENI) that is no longer needed. Prerequisites The secondary ENI is in the Available state. Context You can delete only secondary ENIs. Primary ENIs share the same lifecycle as instances and cannot be deleted. es
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net works and Securit y > ENIs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the secondary ENI and click Delet e in the Act ions column.
5. Click OK.

## Key pairs

### Overview

Key pairs are a secure and convenient authentication method provided by Alibaba Cloud for Elastic Compute Service (ECS) instance logons. A key pair consists of a public key and a private key. Only Linux instances support logon based on key pairs. Introduction A key pair consists of a pair of public and private keys that are generated based on an encryption algorithm. By default, 2048-bit RSA key pairs are used. Before you log on to a Linux instance by using a key pair, you must first create the key pair. You can specify a key pair when you create an instance, or bind a key pair to an instance after the instance is created. Then, you can use the private key to connect to the instance. Benefits Key-based authentication has the following advantages over username and password-based authentication: Security: Key pairs provide higher security and reliability for logons. Key pairs are more secure than general user passwords against brute-force attacks. Private keys cannot be deduced even if the public keys are maliciously acquired. Ease of use: If you configure a public key on a Linux instance, you can use the corresponding private key to run SSH commands or other tools for passwordless logon to the instance. You can log on to a large number of Linux instances at the same time. If you want to manage multiple Linux instances, we recommend that you use this method. Limits Key pairs have the following limits: If you use a key pair to log on to a Linux instance, the password logon method is disabled for higher security. Key pairs apply only to Linux instances. Currently, only RSA 2048-bit key pairs can be created in the ECS console. Only a single key pair can be bound to each Linux instance in the ECS console. If you bind a key pair to an instance to which another key pair is already bound, the new key pair replaces the original one. If you want to use multiple key pairs to log on to a Linux instance, you must manually modify the ~/.ssh /authorized_keys file from within the instance to add multiple key pairs. If you bind a key pair to or unbind a key pair from an instance in the Running ( `Running` ) state, you must restart the instance for the operation to take effect. This enhances data security. Creation methods You can use one of the following methods to create a key pair: Create a key pair in the ECS console. By default, the key pair is generated in the RSA 2048-bit format. For more information, see Create a key pair. Import ant If you create a key pair in the ECS console, you must download and securely lock away the private key. After the key pair is bound to an instance, you cannot log on to the instance if you do not have the private key. Create a key pair by using a key pair generator and then import the key pair to the ECS console. The imported key pair must support one of the following encryption methods: rsa dsa ssh-rsa ssh-dss ecdsa ssh-rsa-cert-v00@openssh.com ssh-dss-cert-v00@openssh.com ssh-rsa-cert-v01@openssh.com ssh-dss-cert-v01@openssh.com ecdsa-sha2-nistp256-cert-v01@openssh.com ecdsa-sha2-nistp384-cert-v01@openssh.com ecdsa-sha2-nistp521-cert-v01@openssh.com

### Create a key pair

This topic describes how to create a key pair in the Apsara Uni-manager Management Console. After a key pair is created, its private key is automatically downloaded. You must securely store the private key and ensure its confidentiality. To log on to an Elastic Compute Service (ECS) instance to which a key pair is bound, you must provide the private key. This topic describes how to create a key pair in the Apsara Uni-manager Management Console.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net work & Securit y > SSH Key Pairs.
3. Click Creat e Key Pair.
4. On the Create Key Pair page, configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | Select an organization in which to create the key pair. Make sure that the key pair and the VPC belong to the same organization. |
|   | Resource Set | Yes | Select a resource set in which to create the key pair. Make sure that the key pair and the VPC belong to the same resource set. |
| ocument Version: | 20230302 15 |   |   |

|   | Elastic Compute Servic |   |   |
|---|---|---|---|
| r Guide·Key pairs |   |   |   |
| Section | Parameter | Required | Description |
|   | Region | Yes | Select a region in which to create the key pair. Make sure that the key pair and VPC belong to the same region. |
| Basic Settings | Key Pair Name | Yes | Enter a name for the key pair. The key pair name must be unique. The name must be 2 to 128 characters in length and can contain special characteristics periods (.), underscores ( ), hyphens _ (-), and colons (:). The name cannot start with a special character or a digit. |
|   | Creation Mode | Yes | Select a method of creating the key pair. We recommend that you select Aut o-creat e. Then, you must securely store the private key in a timely manner and ensure its confidentiality. Aut o-creat e: The system creates a key pair for you. The private key is automatically downloaded after the key pair is created. The private key can be downloaded only once. You must securely store the private key file and ensure its confidentiality. Import : You can enter a Base64-encoded public key in the Public Key field. |

5. Click Creat e.
Result After the key pair is created, your browser downloads the private key file to your computer. Import ant Private key files are downloaded to your computer only when Auto-create is selected. Private key files are not saved in the ECS console and cannot be recovered if they are lost. Make sure that you securely store your private key files to ensure their confidentiality. What's next Before you can use a created key pair to log on to an instance, you must bind the key pair to the instance. For more information, see Bind a key pair to an instance.

### Bind a key pair to an instance

You can specify a key pair when you create an Elastic Compute Service (ECS) instance, or bind a key pair to the instance after the instance is created. This topic describes how to bind a key pair to an instance after the instance is created. If your ECS instance originally uses password-based authentication, the password-based authentication is automatically disabled after the key pair is bound. Context Only a single key pair can be bound to each ECS instance in the ECS console. If you bind a key pair to an instance to which another key pair is already bound, the new key pair replaces the original one.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net work & Securit y > SSH Key Pairs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the key pair that you want bind and click Bind Key Pair in the Act ions column.
5. In the Select Inst ances section of the Bind Key Pair dialog box, click the name of the ECS instance to
which you want to bind the key pair. If instance names in the Select Inst ance section are dimmed, the instances are Windows instances and cannot have key pairs bound.
6. Click OK.
7. If the selected ECS instance is in the Running (Running) state, perform the following operations to
restart the instance to make the binding operation take effect: i. In the left-side navigation pane, choose Inst ances & Images > Inst ances. ii. Find the instance that you want to restart and choose Inst ance St at us > Rest art Inst ance in the Act ions column. iii. In the message that appears, click Rest art Inst ance.

### Unbind SSH key pairs

This topic describes how to unbind an SSH key pair in the Elastic Compute Service (ECS) console.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Net work & Securit y > SSH Key Pairs.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the key pair that you want to unbind and click Unbind Key Pair in the Act ions column.
5. In the Select Inst ances section of the Unbind dialog box, click the ID or name of the instance from
which you want to unbind the key pair. Then, the instance is moved to the right-hand column.
6. Click OK.
7. If the selected ECS instance is in the Running (Running) state, perform the following operations to
restart the instance to make the binding operation take effect: i. In the left-side navigation pane, choose Inst ances & Images > Inst ances. ii. Find the instance that you want to restart and choose Inst ance St at us > Rest art Inst ance in the Act ions column. iii. In the message that appears, click Rest art Inst ance. What's next After the SSH key pair is unbound, you must reset the password of the instance before you log on to the instance as the root user. For more information, see Change the logon password of an instance. Not e If you have reset the password before you unbind the key pair, you can log on by using the new password after you unbind the key pair.

## Deployment sets

### Overview

Deployment Set is a service provided by Elastic Compute Service (ECS) that allows you to view the physical topology of hosts, racks, and vSwitches. You can select deployment policies based on your business requirements to improve the reliability and performance of your business. Benefits When you use multiple ECS instances within the same zone, you may have the following requirements on business reliability or performance: High business reliability To prevent the impacts caused by the failure of physical hosts, racks, or vSwitches, you want to distribute identical application instances across different physical hosts, racks, or vSwitches. High network performance In scenarios that involve frequent network interactions between instances, you want to associate the instances with the same vSwitch to achieve low-latency and high-bandwidth communication between the instances. Deployment granularities and policies Deployment Granularit y Host : The minimum granularity for scheduling is a physical server. Not e When you create a deployment set, Deployment Granularit y is set to Host by default. Rack: The minimum granularity for scheduling is a rack. Net work Swit ch: The minimum granularity for scheduling is a vSwitch. Deployment policy Loose Aggregat ion St rict Aggregat ion Loose Dispersion St rict Dispersion Loose Aggregat ion and St rict Aggregat ion are intended for higher performance, while Loose Dispersion and St rict Dispersion are intended for higher availability. The following Granularities and policies table describes the deployment policies and use scenarios corresponding to each deployment granularity. Granularities and policies

| Deployment granularity | Deployment policy | Use Scenario |
|---|---|---|
|   | Strict dispersion |   |
| 60 |   | > Document Version: 2023030 |

| lastic Compute Service |   | User Guide·Deployment set |
|---|---|---|
| Host Deployment granularity | Deployment policy | General-purpose business scenarios. Use Scenario |
|   | Loose dispersion |   |
| Rack | Strict dispersion | Big data and databases |
|   | Loose dispersion | Game customers |
| vSwitch | Strict dispersion | VPN |
|   | Loose dispersion | Game customers |
|   | Strict aggregation | Big data and databases |
|   | Loose aggregation | Game customers |

Example The following figure shows a typical scenario where business reliability is improved by using deployment sets. Three ECS instances of a tenant are distributed on three different physical hosts, which are distributed on at least two different racks. Not e For more information about the deployment set APIs, see Deployment sets in ECS Developer Guide.

### Create a deployment set

You can use deployment sets to distribute or aggregate instances involved in your business. You can select hosts, racks, or network switches to improve service availability or network performance.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click Creat e Deployment Set .
5. Configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Region | Organization | Yes | The organization in which to create the deployment set. |
|   | Resource Set | Yes | The resource set in which to create the deployment set. |
|   | Region | Yes | The region in which to create the deployment set. |
|   | Zone | Yes | The zone in which to create the deployment set. |
| Basic Settings | Deployment Domain | Yes | This parameter determines the valid values of Deployment Granularity. |
|   | Deployment Granularity | Yes | The basic unit that can be scheduled when you deploy instances. Valid values: Host : Instances are distributed or aggregated at the host level. Rack:Instances are distributed or aggregated at the rack level. Net work Swit ch: Instances are distributed or aggregated at the network switch level. |
|   | Deployment Policy | No | The dispersion policies are used to improve service availability to avoid impacts on your business when a host, rack, or switch fails. The aggregation policies are used to improve network performance to minimize the access latency between instances. Valid values: Loose Dispersion St rict Dispersion Loose Aggregat ion St rict Aggregat ion |
|   | Deployment Set Name | Yes | The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), colons (:), and commas (,). It _ must start with a letter and cannot start with http:// or https://. |

|   | ice User Guide·Deployment set |   |   |
|---|---|---|---|
| Section | Parameter | Required | Description |
|   | Description | No | The description of the deployment set. To simplify future management operations, we recommend that you provide an informational description. The description must be 2 to 256 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), _ colons (:), and commas (,). It must start with a letter and cannot start with http:// or https://. |

6. Click Submit .

### View deployment sets

You can view the list of deployment sets.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Select a filter option from the drop-down list, enter the relevant information in the search bar, and
then click Search. You can select multiple filter options to narrow down search results.

| Filter option | Description |
|---|---|
| Deployment Set Name | Enter a deployment set name to search for the deployment set. |
| Deployment Set ID | Enter a deployment set ID to search for the deployment set. |

### Change the deployment set of

an instance This topic describes how to add an Elastic Compute Service (ECS) instance to a deployment set or migrate an instance from one deployment set to another. Prerequisites The instance is in the St opped or Running state.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the instance for which you want to change the deployment set and click the
icon in the Act ions column and choose Inst ance Set t ings > Change Deployment Set .
5. In the Change Deployment Set dialog box, select the destination deployment set and set the
Force Change parameter. Valid values of Forced Change: Yes: allows the instance to be migrated to another host, which may cause the instance to restart. No: does not allow the instance to be migrated to another host. The instance must remain on the current host, which may cause a failure to change the deployment set of the instance.
6. Click OK.

### Modify a deployment set

You can modify the name and description of a deployment set.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the deployment set and click Modif y in the Act ions column.
5. In the Change Deployment Set dialog box, change the name of the deployment set.
6. Click OK.

### Delete a deployment set

You can delete a deployment set that is no longer needed. Prerequisites No instances exist in the deployment set.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Deployment Set s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the deployment set and click Delet e in the Act ions column.
5. Click OK.
e

## Monitoring & maintenance

### Configure monitoring thresholds

for organizations You can specify a monitoring period and configure thresholds for a selection of metrics to monitor resource utilization in your organization. Then, you can improve resource utilization efficiency based on monitoring results and optimization suggestions. Limits Monitoring thresholds can be configured only for organizations that use an admin account.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Monit oring & Maint enance.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Organizat ion tab.
5. Select one of the following quota usage types and then click Set T hresholds:
High Quot a Usage: indicates that the metric usage is greater than or equal to the threshold that you specify. Low Quot a Usage: indicates that the metric usage is less than or equal to the threshold that you specify.
6. In the dialog box that appears, specify the monitoring period and metric thresholds. The following
table describes the monitoring period and metric thresholds that you configure.

| Parameter | Description |
|---|---|
| Monitoring Period | Specify the monitoring period. Valid values: 7 Days, 15 Days, and 30 Days. |
| Average CPU Quota Usage | Specify a threshold for the average CPU quota usage. Threshold for the high quota usage: The average CPU quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Threshold for the low quota usage: The average CPU quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Not e The threshold can only be an integer multiple of 5%. |

e

| Parameter | Description |
|---|---|
| Average Memory Quota Usage | Specify a threshold for the average memory quota usage. Threshold for the high quota usage: The average memory quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Threshold for the low quota usage: The average memory quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Not e The threshold can only be an integer multiple of 5%. |
| Average Storage Quota Usage | Specify a threshold for the average storage quota usage. Threshold for the high quota usage: The average storage quota usage is greater than or equal to the threshold that you specify. The threshold ranges from 60% to 95%. Threshold for the low quota usage: The average storage quota usage is less than or equal to the threshold that you specify. The threshold ranges from 5% to 40%. Not e The threshold can only be an integer multiple of 5%. |

7. Click OK.
Result The specified monitoring period and metric thresholds are displayed above the organization list. The organizations that match the specified monitoring period and metric thresholds are displayed in the Monit oring & Maint enance section of the Overview page in the console.

### View the list of monitored

organizations You can view the organizations that meet the monitoring criteria, specified thresholds, and optimization suggestions within the monitoring period.
1. Log on to the ECS console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Use one of the following methods to go to the Monit oring & Maint enance page:
In the Monit oring & Maint enance section of the Overview page, click Handle Now. e In the left-side navigation pane, click Monit oring & Maint enance.
4. Click the Organizat ion tab and click one of the following tabs as needed:
High Quot a Usage: displays organizations whose quota usage reaches or exceeds the upper thresholds that you specify. Low Quot a Usage: displays organizations whose quota usage reaches or falls below the lower thresholds that you specify. Result You can view the configured monitoring period and metric thresholds on the top of the organization list. You can view the information of organizations that meet monitoring criteria within the specified monitoring period in the organization list, such as the organization name, CPU quota usage, memory quota usage, storage quota usage, instances, and actions. What's next You can adjust the quota for an organization based on your business needs. For more information, see the Quota management chapter in Apsara Uni-manager Management Console User Guide.

### Configure monitoring metric

thresholds for instances You can configure the monitoring period and multiple monitoring metric thresholds for instances to improve resource utilization based on the monitoring results and optimization suggestions. Limits You can configure monitoring metric thresholds only as as an operations administrator.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Monit oring & Maint enance.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Monit oring & Maint enance page, click the Inst ances tab.
5. Click one of the following tabs and then click Set T hresholds:
High Resource Usage: displays instances whose resource usage reaches or exceeds the upper thresholds that you specify. Low Resource Usage: displays instances whose resource usage reaches or falls below the lower thresholds that you specify.
6. In the dialog box that appears, configure the parameters described in the following table to specify
the monitoring period and metric thresholds.

| Parameter | Description |
|---|---|
| Monitoring Period | Specify the monitoring period. By default, the monitoring period is seven days. |

| Use e | r Guide·Monitoring & maintenanc | Elastic Compute Servic | e |
|---|---|---|---|

| Parameter | Description |
|---|---|
| Average CPU Utilization | Specify the threshold for the average CPU utilization. High resource usage: The resource usage of an instance is considered high if its average CPU utilization is greater than or equal to the upper threshold that you specify. This threshold can range from 60% to 95%. Low resource usage: The resource usage of an instance is considered low if its average CPU utilization is smaller than or equal to the lower threshold that you specify. This threshold can range from 5% to 40%. Not e The threshold must be an integral multiple of 5%. |
| Average Memory Usage | Specify the threshold for the average memory usage. High resource usage: The resource usage of an instance is considered high if its average memory usage is greater than or equal to the upper threshold that you specify. This threshold can range from 60% to 95%. Low resource usage: The resource usage of an instance is considered low if its average memory usage is smaller than or equal to the lower threshold that you specify. This threshold can range from 5% to 40%. Not e The threshold must be an integral multiple of 5%. |

7. Click OK.
Result The specified monitoring period and metric thresholds are displayed on the top of the instance list. In the Monit oring & Maint enance section of the Overview page in the ECS console, the instances that meet monitoring criteria within the specified monitoring period are displayed.

### View the list of monitored

## instances

You can view the instances that meet the monitoring criteria, specified thresholds, and optimization suggestions within the monitoring period.
1. Log on to the ECS console.
2. In the top navigation bar, select an organization, a resource set, and a region.
3. Use one of the following methods to go to the Monit oring & Maint enance page:
e In the Monit oring & Maint enance section of the Overview page, click Handle Now. In the left-side navigation pane, click Monit oring & Maint enance.
4. Click the Inst ances tab and click one of the following tabs as needed:
High Resource Usage: displays instances whose resource usage reaches or exceeds the upper thresholds that you specify. Low Resource Usage: displays instances whose resource usage reaches or falls below the lower thresholds that you specify. Result You can view the configured monitoring period and metric thresholds on the top of the instance list. You can view the information of instances that meet monitoring criteria within the specified monitoring period in the instance list, such as the instance ID and name and resource set.

### Reclaim instance resources

You can optimize your business layout by reclaiming under-used instance resources based on the monitoring results of metrics that you set thresholds for. Limits Only instance resources with low usage can be reclaimed. After an Elastic Compute Service (ECS) instance is moved to the recycle bin, the storage resources of the instance are retained, but its computing resources such as vCPUs and memory are released. After an ECS instance is moved to the recycle bin, the instance is retained here for a specified period of time. During the retention period, the instance can be recovered. After the retention period, the instance is automatically deleted.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Monit oring & Maint enance.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Inst ances tab and click Low Resource Usage.
5. Find the instance that you want to reclaim, click Recycle in the Act ions column.
6. In the message that appears, click OK.
After the instance is reclaimed, St opped - Pending Release is displayed in the Status column of the instance list. You can view the instance in the recycle bin. Related operations You can restore instances in the recycle bin based on business needs. For more information, see Restore an instance.

## Cloud Assistant

### Overview

Cloud Assistant is a native automated operations and maintenance (O&M) tool developed for Elastic Compute Service (ECS). It allows you to batch maintain ECS instances and batch run commands on and send files to ECS instances in a password-free, logon-free manner without the use of jump servers. These commands can consist of shell, PowerShell, or batch scripts. Typically, you can use Cloud Assistant to install and uninstall software, start and stop services, distribute configuration files, and run commonly used commands (scripts). Features After ECS instances that have the Cloud Assistant client installed enter the Running ( `Running` ) state, you can use Cloud Assistant to perform the following operations on the instances by using the ECS console or by calling API operations: Run batch and PowerShell scripts on Windows instances, or run shell, Python, and Perl scripts on Linux instances. Upload files to the instances. Run the same command on multiple instances. The execution state and results of one instance do not affect other instances. Configure custom parameters in Cloud Assistant commands to adapt to different scenarios. Not e Cloud Assistant does not proactively initiate any operations. You have full control over all Cloud Assistant operations. Use scenarios Cloud Assistant can help you perform deployment and O&M tasks on ECS instances. The following list provides some examples: Uploading and running automated O&M scripts Running scripts that are already uploaded to instances Managing software lifecycle Deploying code or applications Polling processes Installing service-related patches or security updates Obtaining files from Object Storage Service (OSS) or YUM repositories to update applications on ECS instances Changing hostnames or user logon passwords Limits Recurring Cloud Assistant tasks can be configured only by calling API operations. The interval at which a command is run cannot be less than 10 seconds. The size of a command cannot exceed 16 KB. This includes the total size of the Base64-encoded batch, PowerShell, or shell scripts together with the Base64-encoded custom parameters. The size of a file to be uploaded cannot exceed 32 KB after Base64 encoding. Each command can contain a maximum of 20 custom parameters. Cloud Assistant commands can be run only on instances that use the following operating systems: Alibaba Cloud Linux CentOS 7, CentOS 8, and later Not e CentOS 8 has reached its end of life (EOL) and is no longer maintained by the Linux community. We recommend that you migrate to Anolis or Alibaba Cloud Linux. Debian 9 OpenSUSE SUSE Linux Enterprise Server (SLES) 11, SLES 12, and SLES 15 and later Ubuntu 14, Ubuntu 16, and Ubuntu 18 and later Windows Server 2012, Windows Server 2016, and Windows Server 2019 and later Terms The following table describes relevant terms in Cloud Assistant.

| Term | Description |
|---|---|
| Cloud Assistant | A tool provided by Alibaba Cloud that can help you perform routine maintenance tasks on multiple ECS instances and ECS bare metal instances. Cloud Assistant is available in all Alibaba Cloud regions. |
| Cloud Assistant client | A lightweight plug-in that can be installed on ECS instances to run Cloud Assistant commands. On Windows instances, the process of the client program is named AliyunService. On Linux instances, the process of the client program is named aliyun.service. |
| Cloud Assistant daemon process | A daemon process that is used to monitor the resource consumption of the Cloud Assistant client, report the running state of the client, and restart the client if the client fails. Service name: AssistDaemon Path: /usr/local/share/assist-daemon/assist daemon _ Not e The Cloud Assistant daemon process is available only for Linux instances. |
| task execution path | A path in which Cloud Assistant saves your command as a file on an ECS instance and executes the file. The path varies based on the operating system. Linux: /tmp Windows: <Installation path of Cloud Assistant>/work/script |
| command | A specific command such as a shell script or a PowerShell script that can be run on ECS instances. |

| Term | Description |
|---|---|
| custom parameter | A variable that is configured in the {{key}} format in a command. You can specify a custom parameter and its value in the {{"<key>":"<value>"}} format when you create a task to run the command. The number of Cloud Assistant commands that you can have within each Alibaba Cloud region is limited. To adapt Cloud Assistant commands to multiple scenarios, we recommend that you configure custom parameters. |
| one-time execution | An execution ( Invocation ) of a one-time task. A one-time task runs a command only once on one or more instances. |
| recurring execution | An execution of a recurring task. A recurring task runs a command on one or more instances based on your specified schedule. |
| execution status | The relationships among different types of execution states. For more information, see Execution states. |

Execution states The following table describes the instance-level execution state of a command that is run on a single instance. The InvocationStatus parameter in API indicates the execution state of a command.

| Execution state in API operations | Execution state in the ECS console | Description |
|---|---|---|
| Running | Running | The command is being run. |
| Stopping | Stopping | The command is being stopped. |
| Stopped | Stopped | The command is stopped. |
| Finished | Completed | The command is run to completion. This does not indicate that the command is successful. You can check whether the command is successful based on the command output ( Output ) and the exit code ( ExitCode ). |
| Failed | Failed | The command cannot be run or the command process did not complete before the timeout period specified by Timeout expires. |

States of batch executions and scheduled executions A batch execution is a one-time execution in which a command is run on multiple instances. To better manage batch executions and recurring executions, you can manage the lifecycles of the executions based on the overall execution states, instance-level execution states, and execution-level states. The InvokeStatus parameter in API operations indicates the execution status of a command. The following figure shows the relationships among the three types of execution states. The following table describes the overall execution states of a command that is run on multiple instances at the same time.

| Execution state in API operations | Execution state in the ECS console | Description | Priority |
|---|---|---|---|
| Running | Running | The instance-level execution state is Running on some or all instances. | 1 |
| Stopping | Stopping | The instance-level execution state is Stopping on some or all instances. | 2 |
| Stopped | Stopped | The instance-level execution state is Stopped on all instances. | 3 |
| Failed | Failed | The instance-level execution state is Failed on all instances, or is Failed on some instances and is Stopped on the other instances. | 4 |
| Finished | Completed | The instance-level execution state is Finished on all instances, or is Finished on some instances and is Stopped on the other instances. | 5 |

|   | Execution state in API operations |   | Execution state in the ECS console | Description | Priority |
|---|---|---|---|---|---|
|   | PartialFailed |   | Partially Failed | The instance-level execution state is Failed on some instances and is Finished on the other instances. | 6 |
|   |   | PartialFailed |   |   |   |

The following figure shows the relationship between the overall execution states and the instancelevel execution states of a one-time execution in which a command is run on three instances at the same time. The following table describes the states of recurring executions of a command.

| State | Description |
|---|---|
| Overall execution state | The overall execution state is always Running ( Running ) unless you stop the command on all the instances. |
| Instance-level execution state | For each instance, the instance-level execution state is always Running ( Run ning ) unless you stop the command on the instance. |
| Execution-level state | For more information, see Execution states. |

| Run |   |
|---|---|

|   | ning |
|---|---|

### Configure the Cloud Assistant

client

#### Install the Cloud Assistant client

The Cloud Assistant client is used to run Cloud Assistant commands on Elastic Compute Service (ECS) instances. This topic describes how to install the Cloud Assistant client. Prerequisites An administrator account is used to install and use the Cloud Assistant client. The administrator username is root for Linux instances, and system for Windows instances. Before you install the Cloud Assistant client, make sure that your instance type and operating system support Cloud Assistant. For more information, see Limits. Context If ECS instances are created from public images in Apsara Stack V3.16.1, the Cloud Assistant client is pre-installed on the instances. If ECS instances are created in Apsara Stack V3.13.0 to V3.16.0, the Cloud Assistant client is not preinstalled on the instances. You can call API operations to use Cloud Assistant on the instances. If you want to use features related to Cloud Assistant, install the Cloud Assistant client. The following table describes how to install the Cloud Assistant client on different operating systems.

| Operating system | Installation method |
|---|---|
| Windows | Install the Cloud Assistant client on Windows instances |
| Linux operating systems such as Alibaba Cloud Linux, CentOS, openSUSE, and SUSE Linux | Install the client on Linux instances by using the RPM package Install the client on Linux instances by using source code |
| Linux operating systems such as Debian and Ubuntu | Install the client on Linux instances by using the Debian package Install the client on Linux instances by using source code |

Install the Cloud Assistant client on Windows instances
1. Connect to an ECS instance as the administrator.
For more information, see Instance connecting overview.
2. Download the client installation file.
You can download the installation file for a specific version of the Cloud Assistant client from one of the following URLs: Public URL for the latest version: latest version of the Cloud Assistant client Public URL for a specified version:

```
https://aliyun-client-assist.oss-accelerate.aliyuncs.com/windows/aliyun_agent_{version} _setup.exe
```

Not e {version} indicates the version number of the Cloud Assistant client.
3. Double-click the installation file and install the client as instructed.
The default installation path is C:\ProgramData\aliyun\assist\ for Windows instances. Install the client on Linux instances by using the RPM package This method is applicable to operating systems such as Alibaba Cloud Linux, CentOS, openSUSE, and SUSE Linux.
1. Connect to an ECS instance as the administrator.
For more information, see Instance connecting overview.
2. Download the RPM package of the Cloud Assistant client.

```
wget "https://aliyun-client-assist.oss-accelerate.aliyuncs.com/linux/aliyun_assist_latest .rpm"
```

Not e {version} indicates the version number of the Cloud Assistant client.
3. Install the Cloud Assistant client.
In this example, the latest version of the Cloud Assistant client is installed.

```
rpm -ivh --force aliyun_assist_latest.rpm
```

Not e The default installation path is /usr/local/share/aliyun-assist/ for Linux instances. Install the client on Linux instances by using the Debian package This method is applicable to operating systems such as Debian and Ubuntu.
1. Connect to an ECS instance as the administrator.
For more information, see Instance connecting overview.
2. Download the Debian package for a specific version of the Cloud Assistant client from one of the
following URLs: Public URL for the latest version:

```
wget "https://aliyun-client-assist.oss-accelerate.aliyuncs.com/linux/aliyun_assist_late st.deb"
```

Public URL for a specified version:

```
wget "https://aliyun-client-assist.oss-accelerate.aliyuncs.com/linux/aliyun_assist_{ver sion}.deb"
```

Not e {version} indicates the version number of the Cloud Assistant client.
3. If an earlier version of the Cloud Assistant client is installed on the instance, uninstall the earlier
version.

```
dpkg -r aliyun-assist
```

4. Install the Cloud Assistant client.
In this example, the latest version of the Cloud Assistant client is installed.

```
dpkg -i aliyun_assist_latest.deb
```

Not e The default installation path is /usr/local/share/aliyun-assist/ for Linux instances. Install the client on Linux instances by using source code
1. Connect to an ECS instance as the administrator.
For more information, see Instance connecting overview.
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

View information of the Cloud Assistant client on an ECS instance After the Cloud Assistant client is installed on an instance, you can perform the following steps to query the version number and state of the client on the instance.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the ECS Inst ances tab to view the information about the Cloud Assistant client on the ECS
instances within the current region.

#### Configure DNS resolution for Cloud

Assistant This topic describes how to configure Domain Name System (DNS) resolution for Cloud Assistant. During the configuration procedure, you must obtain the IP addresses that correspond to the Cloud Assistant endpoints and then modify the hosts file. Context When you use features such as Cloud Assistant on an Elastic Compute Service (ECS) instance, the instance must have access to the endpoints required to perform actions that you specify, such as running a Cloud Assistant command. The default DNS Nameserver is installed on each ECS instance to resolve domain names. You can run the cat /et c/resolv.conf command to view the DNS Nameserver settings. Example command output: If you modify the configuration file to override the default DNS Nameserver settings, domain names may fail to resolve or resolve slowly when you use features such as Cloud Assistant. This may cause the features to be unavailable. For example, Cloud Assistant commands cannot be run. In this case, you can perform the following procedure to configure DNS resolution for Cloud Assistant.
1. Connect to an ECS instance. For more information, see Instance connecting overview.
2. Obtain the IP addresses that correspond to the Cloud Assistant endpoints.
The following Cloud Assistant endpoints are available: Endpoint used to run Cloud Assistant commands, in the format of <region-id>`.axt.aliyun.com` Endpoint used to obtain the Cloud Assistant plug-in and update packages, in the format of `aliy` `un-client-assist-`<region-id>`.oss-`<region-id>`-internal.aliyuncs.com` Not e Replace <region-id> with a region ID.
3. Modify the hosts file.

```
echo "100.100.XX.XX <region-id>.axt.aliyun.com" >> /etc/hosts && \ echo "100.118.XX.XX aliyun-client-assist-<region-id>.oss-<region-id>-internal.aliyuncs.co m" >> /etc/hosts
```

Not e Replace `100.100.XX.XX` and `100.118.XX.XX` with the IP addresses that you obtained in the previous step.
4. Check whether the hosts file is modified.

```
cat /etc/hosts
```

If the hosts file is modified, the command output includes the Cloud Assistant endpoints and their corresponding IP addresses. Example command output: After the hosts file is modified, the ECS instance can automatically obtain IP addresses from the hosts file to resolve the Cloud Assistant endpoints.

#### Start or stop the Cloud Assistant client

The Cloud Assistant client is an agent that runs Cloud Assistant commands on Elastic Compute Service (ECS) instances. This topic describes how to start or stop the Cloud Assistant client. Start or stop the Cloud Assistant client on a Windows instance To start or stop the Cloud Assistant client on a Windows instance, perform the following steps. Warning Aliyun Assist Service is the process of the Cloud Assistant client. If you stop Aliyun Assist Service, the Cloud Assistant client stops. This may cause an exception on the instance, and the instance cannot be stopped by using the ECS console. Proceed with caution when you stop the Cloud Assistant client.
1. Connect to the Windows instance. For more information, see Connect to a Windows instance by using
RDC.
2. Click Start and choose Windows Administ rat ive T ools > Comput er Management .
3. Choose Comput er Management (Local) > Services and Applicat ions > Services.
4. Find Aliyun Assist Service and click St op t he service or Rest art t he service.
Uninstall the Cloud Assistant daemon process from a Linux instance The Cloud Assistant daemon process is used to monitor the resource consumption of the Cloud Assistant client, report the running status of the client, and restart the client when the client fails. Before you stop the Cloud Assistant client, you must first uninstall the Cloud Assistant daemon process. Not e The Cloud Assistant daemon process is available only for Linux instances.
1. Connect to the Linux instance. For more information, see Connect to a Linux instance by using SSH
commands in Linux or Mac OS X or Connect to a Linux-based instance by using remote connection tools in Windows.
2. Stop the Cloud Assistant daemon process.

```
/usr/local/share/assist-daemon/assist_daemon --stop
```

Not e In the preceding command, /usr/local/share/assist-daemon/assist_daemon specifies the default path of the Cloud Assistant daemon process.
3. Uninstall the Cloud Assistant daemon process.

```
/usr/local/share/assist-daemon/assist_daemon --delete
```

4. Delete the directory of the Cloud Assistant daemon process.

```
rm -rf /usr/local/share/assist-daemon
```

Start or stop the Cloud Assistant client on a Linux instance Not e Before you stop the Cloud Assistant client, you must first uninstall the Cloud Assistant daemon process. For more information, see the Uninstall the Cloud Assistant daemon process from a Linux instance section. To start or stop the Cloud Assistant client on a Linux instance, perform the following steps:
1. Connect to the Linux instance. For more information, see Connect to a Linux instance by using SSH
commands in Linux or Mac OS X or Connect to a Linux-based instance by using remote connection tools in Windows.
2. Run the following commands based on the initialization process of the Linux instance.
Linux operating systems that are based on new versions of the Linux kernel typically use the syst emd initialization process. Perform the following steps: Check whether the instance uses the systemd initialization process. If the instance uses systemd, a command output is displayed.

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

Ubuntu 14 and earlier operating systems typically use the UpSt art initialization process. Perform the following steps: Check whether the instance uses the UpStart initialization process. If the instance uses UpStart, a command output is displayed.

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

Linux operating systems that are based on earlier versions of the Linux kernel typically use the sysvinit initialization process. Perform the following steps: Check whether the instance uses the sysvinit initialization process. If the instance uses sysvinit, a command output is displayed.

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

### Use Cloud Assistant

#### Create a command

You can use Cloud Assistant commands to perform routine tasks on Elastic Compute Service (ECS) instances. These tasks include running automated O&M scripts, polling processes, resetting user passwords, installing or uninstalling software, updating applications, and installing patches. The commands can be batch or PowerShell commands for Windows instances, and shell commands for Linux instances. You can specify custom parameters as variables in Cloud Assistant commands. Prerequisites The instances on which to run a command are in the Running (Running) state. You can retain up to 100 Cloud Assistant commands within an Alibaba Cloud region. This quota may increase based on your ECS usage. If you click Run when you create a command in the Create Command page, the command does not count against your command quota. Not e You can also call the DescribeAccountAttributes operation with AttributeName.N set to max-axt-command-count to query the maximum number of Cloud Assistant commands that you can retain within a region. You can run Cloud Assistant commands up to 5,000 times per day within each region. This quota may increase based on your ECS usage. Not e You can also call the DescribeAccountAttributes operation with the AttributeName.N parameter set to max-axt-invocation-daily to query the maximum number of times that you can run Cloud Assistant commands per day within each region. Context When you use the immediate execution feature, take note of the following items: Only operations administrators, organization administrators, and resource set administrators can create commands. The size of the command after Base64 encoding cannot exceed 16 KB. Up to 20 custom parameters can be specified in a single Cloud Assistant command. You can call an API operation to run a command on up to 50 instances each time. When you create a command, make sure that the syntax, logic, or algorithm associated with the command are correct. For example, assume that you have created the /backup directory ( `mkdir /backup` ) on an instance. You can run the following shell commands to archive a file in this directory:

```
#!/bin/bash
OF=/backup/my-backup-$(date +%Y%m%d).tgz tar -cf $OF {{file}}
```

Not e In the preceding example, `{{file}}` is a custom parameter. When you run the commands, you can set this custom parameter to the name of the file to be archived. Example: / app/usrcredential. Custom parameters can be used in scenarios that require dynamic values and values that are shared across multiple commands. We recommend that you specify custom parameters for sensitive data or data that changes with the environment, such as AccessKey pairs, instance IDs, authorization codes, time parameters, and critical system files. Procedure in the ECS console
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant, click Creat e /Run Command.
5. On the Creat e Command page, configure the parameters described in the following table.

| Section | Parameter | Description |
|---|---|---|
| Resource Owner | Organization | Select the organization to which the instances belong. |
|   | Resource Set | Select the resource set to which the instances belong. |
| Command Information | Command Source | Select the command source. Ent er Command Cont ent : creates a command. Select Saved Command: selects an existing command. |
|   | Command Name | Enter a name for the command. |
|   | Execution Plan | Select a plan on how to run the command. Run Now: The command is immediately run after you click Run or Run and Save. Run on Next Syst em St art up: The command is run the next time the selected instances are started after you click Run or Run and Save. Run on Each Syst em St art up: The command is run each time the selected instances are started after you click Run or Run and Save. |
|   | Command Type | Select a command type. For Linux instances, select Shell. For Windows instances, select Bat or PowerShell. |
|   | Command Content | Enter or paste the content of the command. |
|   | Use Parameters | Specifies whether to use parameters. If you turn on Use Paramet ers, specify custom parameters in the {{key}} format in the Command Cont ent field. |
|   | Command Parameters | Specify the values of the custom parameters specified in the {{key}} format in the Command Cont ent field. This parameter is available only when Use Paramet ers is turned on. |
|   | Command Description | Enter a description for the command. We recommend that you set a description with information such as the command purpose that makes the command easy to identify, manage, and maintain. |

|   | nt Elastic Compute Servic |   |
|---|---|---|
| Section | Parameter | Description |
|   | User | Specify the username that is used to run the command on ECS instances. By default, Cloud Assistant commands are run by the root user on Linux instances and by the system user on Windows instances. |
|   | Execution Path | Specify an execution path for the command. Different default execution paths are provided based on the operating system of instances on which the command is run. For Linux instances, the default execution path is the /home directory of the root user. For Windows instances, the default execution path is the directory where the process of the Cloud Assistant client is located. Example: C:\ProgramData\aliyun\assist\$(version). |
|   | Timeout Period | Specify a t imeout period for the command to run on instances. If a task that runs the command times out, Cloud Assistant forcefully terminates the task process. Unit: seconds. Default value: 60. Minimum value: 10. If you set T imeout Period to a value of less than 10, the system changes the value to 10 to ensure that the command can be run. |
| Instances | Instance ID/Name | Select the instances on which you want to run the command. |

6. Click Save, Run and Save, or Run.
Procedure by using the CLI Sample request: Call the RunCommand operation to create and run a Cloud Assistant command named update to update the operating system on instances.

```
aliyun ecs RunCommand --RegionId 'cn-qingdao-****-d01' \ --Name 'update' --Username 'root' --Type 'RunShellScript' \ --CommandContent 'eXVtIC15IHVwZGF0ZQ==' \ --Timeout '60' --RepeatMode 'Once' --ContentEncoding 'Base64' \ --InstanceId.1 'i-bp12e0ib2ztibede****'
```

Not e Values enclosed in single quotation marks ('') are example values of the parameters. Configure the parameters based on actual conditions.

| Parameter | Example | Description |
|---|---|---|
| RegionId | cn-qingdao-****-d01 | The ID of region in which to create the command. |

| stic Compute Service |   | User Guide·Cloud Assistan |
|---|---|---|

| Parameter | Example | Description |
|---|---|---|
| Name | update | The name of the command. |
| Username | root | The username used to run the command on ECS instances. |
| Type | RunShellScript | The type of the command. For Linux instances, set the value to RunShellScript. For Windows instances, set the value to RunBatScript or RunPowershellScript. |
| CommandContent | eXVtIHVwZGF0ZSAteQ= = | The Base64-encoded content of the command. |
| Timeout | 60 | The timeout period. |
| RepeatMode | Once | The execution plan. |
| ContentEncoding | Base64 | The encoding format. |
| InstanceId.1 | i-bp12e0ib2ztibede**** | The ID of ECS instance N on which you want to run the command. In this example, the value of N is 1. |

For more information, see the CreateCommand topic in the ECS Developer Guide. Sample success response: `{`

```json
        "CommandId": "c-hz018qlm868****",
        "InvokeId": "t-hz018qlm86d****",
        "RequestId": "1D24FA80-64DB-4842-AB20-2520799****"
```

`}`

#### Run a command

After you create a Cloud Assistant command, you can run it on one or more Elastic Compute Service (ECS) instances. The execution status and results of the command on multiple instances do not affect each other. Prerequisites Before you run a Cloud Assistant command on ECS instances, make sure that the instances meet the following requirements: The instances are in the Running ( `Running` ) state. The Cloud Assistant client is installed on the instances. For more information, see Install the Cloud Assistant client. Import ant Only operations administrators, organization administrators, and resource set administrators can run Cloud Assistant commands. Context You can call an API operation to run a command on up to 50 instances. If you select more than 50 instances to run a command in the ECS console, the system runs the command on the instances in batches. You can run Cloud Assistant commands up to 5,000 times per day within each region. This quota may increase based on your ECS usage. Not e You can also call the DescribeAccountAttributes operation with the At t ribut eName.N parameter set to max-axt-invocation-daily to query the maximum number of times that you can run Cloud Assistant commands per day within each region. Run Cloud Assistant commands by using the ECS console
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the command that you want to run and click Run in the Act ions column.
5. In the Run Command page, configure parameters.
i. In the Command Inf ormat ion section, check command content and configure the parameters described in the following table.

| Parameter | Description |
|---|---|
|   | Select a plan on how to run the command. Immediat e execut ion: The command is run immediately after you click Run or Execut e and Save. Af t er t he next st art up of t he syst em: The command is run the next time the selected instances are started after you click Run or Execut e and Save. Af t er each syst em st art up: The command is run each time the selected instances are started after you click Run or Execut e and Save. Run on Schedule: The command is run at a specified interval, at a specified time, or on a schedule after you click Run or Execut e and Save. If you set Implementation plan to Run on Schedule, the following options are available: |

| Parameter | Run at Fixed Int erval: Use a rate expression to specify an Description interval at which to run the command. You can specify the |   |   |
|---|---|---|---|
| Execution Plan | interval in seconds, minutes, hours, or days. This option is applicable when tasks need to be executed at a fixed interval. Not e When you specify an interval, take note of the following limits: The specified interval can be anywhere from 60 seconds to 7 days and must be longer than the timeout period of the scheduled task. The interval is the duration between two consecutive executions. The interval is irrelevant to the amount of time required to run the command once. For example, assume that you set the |   |   |
|   | interval to 5 minutes and that it takes 2 minutes to run the command each time. Each time the command is run, the system waits 3 minutes before it runs the command again. A task is not executed immediately after it is created. For example, assume that you set the interval to 5 minutes for a task. The task begins to be executed 5 minutes after it is created. Run Only Once at Specif ied T ime: Specify a point in time and a time zone to run the command only once. For example, if you set Execut ion T ime to 2022-05-17 17:30:50 and T ime Zone to (GMT + 8:00) Asia/Shanghai, the command was run only once at 17:30:50 on May 17, 2022 (UTC+8). Run on Clock-based Schedule: Use a cron expression to specify a schedule on which to run the command. Specify a schedule accurate to the second, minute, hour, day of the month, month, day of the week, or year, and select a time zone from the Time Zone drop-down list. The system calculates the recurrence schedule based on the cron expression and time zone and runs the command as scheduled. This option provides flexibility and is applicable when tasks need to run on a schedule. For more information about cron expressions, see Cron expressions. |   |   |
| Command Content | Confi | Not e The minimum interval must be 10 seconds or rm the command content in the Command Cont ent field. more and cannot be shorter than the timeout period of |   |
|   |   | scheduled executions. |   |

For example, if you set Execut ion Frequency to 0 0 12 ? * WED 2022 and T ime Zone to (GMT + 8:00) Asia/Shanghai, the system runs the command at 12:00 every Wednesday in 2022 (UTC+8).

| Parameter | Description |
|---|---|
| Command Parameters | In the Command Paramet ers field, enter values for the custom parameters that are specified in the command. No format limits apply to the data types of values for the custom parameters. If the current task does not require values for these fields, you can leave the fields empty. Not e If you did not select Use Paramet ers when you create the command, the Command Paramet ers fields are not displayed on the Run Command page. |
| User | Specify the username that is used to run the command on ECS instances. By default, Cloud Assistant commands are run by the root user on Linux instances and by the system user on Windows instances. |

ii. In the Inst ances section, select one or more instances on which you want to run the command.
6. Click Run.
Run Cloud Assistant command by using Alibaba Cloud CLI
1. (Optional)Check the state of the instances on which you want to run a command. If the instances are
not in the Running ( `Running` ) state, call the StartInstance operation to start the instances.

```
aliyun ecs StartInstance --InstanceId 'i-bp1f4f6o8lv0wqof****'
```

Not e Values enclosed in single quotation marks ('') are example values of the parameters. You must configure the parameters based on actual conditions. For more information, see or the "StartInstance" topic in ECS Developer Guide.
2. (Optional)Call the DescribeCloudAssistantStatus operation to check whether the Cloud Assistant
client is installed on the instances.

```
aliyun ecs DescribeCloudAssistantStatus --RegionId 'cn-qingdao-****-d01' \ --InstanceId.1 'i-bp1f4f6o8lv0wqof****'
```

If the value of `CloudAssistantStatus` is true in the response, the Cloud Assistant client is installed on the instances.
3. Call the InvokeCommand operation to run a created Cloud Assistant command on the instances and
obtain the value of InvokeId in the response.

```
aliyun ecs InvokeCommand --RegionId 'cn-qingdao-****-d01' \ --InstanceId.1 'i-bp1f4f6o8lv0wqof****' \ --InstanceId.2 'i-bp137qu6142s3mhm****' \ --CommandId 'c-hz018qp243j****' \ --Timed 'false' \ --output cols=InvokeId
```

| Parameter | Example | Description |
|---|---|---|
| RegionId | cn-qingdao-****-d01 | The ID of the region in which to run the command. |
| InstanceId.1 | i- bp1f4f6o8lv0wqof**** | The ID of the first instance on which to run the command. |
| InstanceId.2 | i- bp137qu6142s3mhm*** * | The ID of the second instance on which to run the command. |
| CommandId | c-hz018qp243j**** | The ID of the command. |
| Timed | false | Specifies whether to periodically run the command. If you want to periodically run a command, set T imed to true. The Frequency parameter specifies the execution cycle. For example, you can set Frequency to 0 */20 * * * * to run the command every 20 minutes. For more information, see Cron expression. |

For more information, see the InvokeCommand topic in the ECS Developer Guide.

#### Upload files to ECS instances

This topic describes how to use the Cloud Assistant client to upload files such as configuration files and scripts to Elastic Compute Service (ECS) instances. Prerequisites The ECS instances to which you want to upload a file are in the Running (Running) state. The Cloud Assistant client is installed on the instance. For more information, see Install the Cloud Assistant client. You can call an API operation to send a file to up to 50 instances at a time. The file that you want to upload cannot exceed 32 KB in size after it is encoded in Base64. Context You can use the Cloud Assistant client to upload files that cannot exceed 32 KB in size. If you want to upload files that are larger than 32 KB in size or if you want to download files from ECS instances, we recommend that you use the FileZilla tool over the SSH File Transfer Protocol (SFTP) and port 22. Import ant Only operations administrators, organization administrators, and resource set administrators can upload files to ECS instances.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the ECS Cloud Assistant page, click Send File.
5. In the Command Inf ormat ion section, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Destination Operating System | Select the operating system of the ECS instances. Valid values: Linux Operation System Windows Operating System |
| File Content | Select a method to use to upload the file. Valid values: Upload File: You can click Upload File to select a file or drag a file to the Upload File section. Paste File Content: You can paste the file content to the field. Not e The file that you want to upload cannot exceed 32 KB in size after it is encoded in Base64. |
| File Name | Specify a name for the file. Not e If you turn off Overwrite, make sure that the file name is unique across the destination path of the ECS instances. |
| Destination Path | Specify the destination path to save the file. Default value when Destination Operating System is set to Linux: /root Default value when Destination Operating System is set to Windows: C:/Users/Administrator/Documents |
| File Description | Specify a description for the file. |
| User | Specify the user to which the file belongs. This parameter is required only for Linux instances. |
| User Group | Specify the user group to which the file belongs. This parameter is required only for Linux instances. |

| Parameter | Description |
|---|---|
| Permissions | Configure permissions on the file. Default value: 0644 . This value indicates that the file owner has read and write permissions on the file, and that other users in the same user group as the file owner and public users have read permissions on the file. This parameter is required only for Linux instances. |
| Overwrite | Specify whether to overwrite the file that has the same name as the uploaded file in the destination path. |
| Timeout Period | Set the timeout period for the file sending task. When the file sending task times out, Cloud Assistant forcibly stops the task process. Unit: seconds. Valid values: 10 to 86400. Default value: 60. |

6. In the Inst ances section, select the instances to which to send the file and configure the parameters
described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Organization | Yes | Select the organization to which the file belongs. |
| Resource Set | Yes | Select the resource set to which the file belongs. |
| Instance | Yes | Select the instances to which you want to send the file. |

7. Click Run.
View the execution results of the file sending task View the execution result of this file sending task.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Cloud Assistant page, click the File Sending Results tab.
5. In the task list, view the execution states, execution IDs, and destination paths of file sending tasks.
You can perform the following operations in the Actions column corresponding to a file sending task: Click View to view the execution results of the task on each instance. Click Export to export the task execution results. Click Resend to execute the task again.

#### Clone a command

You can clone an existing Cloud Assistant command to create another command. You can retain all the information of the original command (cloned command), or you can modify information such as the name, description, type, content, execution path, or timeout period in the new command (command clone). Import ant Only operations administrators, organization administrators, and resource set administrators can clone commands.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the Cloud Assistant command that you want to clone and click Clone in the Act ions column.
5. On the Clone Command page, configure the parameters described in the following table.

| Section | Parameter | Description |
|---|---|---|
| Resource Owner | Organization | Select the organization to which the instances belong. |
|   | Resource Set | Select the resource set to which the instances belong. |
| Command Information | Command Name | Specify a name for the new command. |
|   | Execution Plan | Select a plan on how to run the new command. Run Now: The command is immediately run after you click Run or Run and Save. Run on Next Syst em St art up: The command is run the next time the selected instances are started after you click Run or Run and Save. Run on Each Syst em St art up: The command is run each time the selected instances are started after you click Run or Run and Save. |
|   | Command type | Select a command type. For Linux instances, select Shell. For Windows instances, select Bat or PowerShell. |
|   | Command Content | Enter or paste the content of the command. |
|   | Command Description | Specify a description for the new command. We recommend that you set a description with information such as the command purpose that makes the command easy to identify, manage, and maintain. |

|   | User Guide·Cloud Assistan |   |
|---|---|---|
| Section | Parameter | Description |
|   | Execution Path | Specify an execution path for the new command. Different default execution paths are provided based on the operating system of instances on which the command is run. For Linux instances, the default execution path is the /home directory of the root user. For Windows instances, the default execution path is the directory where the process of the Cloud Assistant client is located. Example: C:\ProgramData\aliyun\assist\$(version). |
|   | Timeout Period | Specify a t imeout period for the new command to run on instances. If a task that runs the command times out, Cloud Assistant forcefully terminates the task process. Unit: seconds. Default value: 60. Minimum value: 10. If you set T imeout Period to a value of less than 10, the system changes the value to 10 to ensure that the command can be run. |

6. Click Save.

#### Delete a command

The number of Cloud Assistant commands that you can have within each Alibaba Cloud region is limited. To ensure a sufficient command quota, we recommend that you regularly delete commands that are no longer needed. Import ant Only operations administrators, organization administrators, and resource set administrators can delete commands.
1. Log on to the ECS console.
2. In the left-side navigation pane, choose Maint enance & Monit oring > Cloud Assist ant .
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Find the Cloud Assistant command that you want to delete and click Delet e in the Act ions column.
5. In the message that appears, click OK.

### Cron expression

When you run a Cloud Assistant command, you can call an API operation and use the Timed and Frequency parameters to set when to run the Cloud Assistant command. The value of the Frequency parameter is a cron expression. This parameter specifies the frequency of scheduled tasks, frequency of routine maintenance, and the point in time at which to complete a one-time task. Introduction A cron expression is a string that represents time. The string consists of five spaces and six fields, which is in the `X X X X X X X` format. `X` is a placeholder of a field. If a field contains multiple values, the values are separated with commas (,). Each field can be a specific value or special characters that have logical representations. Field values The following table describes valid values and supported special characters for each field in cron expressions.

| Field | Required | Valid value range | Special character |
|---|---|---|---|
| Second | Yes | [0, 59] | * , - / |
| Minute | Yes | [0, 59] | * , - / |
| Hour | Yes | [0, 23] | * , - / |
| Day | Yes | [1, 31] | * , - / ? L W |
| Month | Yes | [1, 12] or [JAN, DEC] | * , - / |
| Week | Yes | [1, 7] or [MON, SUN]. If you use the [1, 7] format, 1 indicates Monday and 7 indicates Sunday. | * , - / ? L # |

Special characters Each field in a cron expression can contain a specific number of special characters. Each special character represents a logical argument.

| Special character | Description | Example |
|---|---|---|
| * | Indicates all valid values. | In the Month field, an asterisk ( * ) indicates every month. In the Week field, an asterisk ( * ) indicates every day of the week. |
| , | Lists enumerated values. | In the Minute field, 5,20 indicates that the task is triggered once at both the 5th and 20th minutes. |
| - | Indicates a range. | In the Minute field, 5-20 indicates that the task is triggered once every minute from the 5th to 20th minute. |
| / | Indicates increments. | In the Minute field, 0/15 indicates that the task is triggered once every 15 minutes from the beginning of an hour. In the Minute field, 3/20 indicates that the task is triggered once every 20 minutes from the 3rd minute of an hour. |

| Special character | Description | Example |
|---|---|---|
| ? | Indicates an unspecified value. Only the Day and Week fields support this character. | If the Day or Week field is specified, the other field must be set to a question mark ( ? ) to prevent conflicts. |
| L | Indicates the last day of a specific period. Only the Day and Week fields support this character. Not e To prevent logic errors, do not specify a list or range when you use the L character. | In the Day field, L indicates the last day of a month. In the Day of a week field, L indicates the last day of a week, which is Sunday ( SUN ). L can be preceded by a value. For example, 6L in the Week field indicates the last Saturday of a month. |
| W | The weekday that is nearest to the specified day of the month. The weekday that the W character indicates is in the same month as the specified day of the month. LW indicates the last weekday of the specified month. | If 5W is specified in the Day field and the 5th day of the month falls on Saturday, the task is triggered on Friday, which is the 4th day of the month. If the 5th day of the month falls on Sunday, the scheduled task is triggered on Monday, which is the 6th day of the month. If the 5th day of the month falls on a weekday, the scheduled task is triggered on the 5th day of the month. |
| # | A specific day of a specific week in every month. Only the Day of a week field supports this character. | In the Week field, 4#2 indicates the second Thursday of a month. |

Examples The following table describes some example values of cron expressions.

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

| ser Guide·Cloud Assistant | Elastic Compute Servic |
|---|---|

| Example | Limit |
|---|---|
| 0 0/5 14,18 * * ? | Executes the task every 5 minutes between 14:00 and 14:55 and between 18:00 and 18:55 every day. |
| 0 0 12 ? * WED | Executes the task at 12:00 every Wednesday. |
| 0 15 10 15 * ? | Executes the task at 10:15 on the 15th day of every month. |
| 0 15 10 L * ? | Executes the task at 10:15 on the last day of every month. |
| 0 15 10 ? * 6L | Executes the task at 10:15 on the last Saturday of every month. |
| 0 15 10 ? * 6#3 | Executes the task at 10:15 on the third Saturday of every month. |
| 0 10,44 14 ? 3 WED | Executes the task at 14:10 and 14:44 every Wednesday in March every year. |

## Dedicated hosts

### Create a dedicated host

A dedicated host is a cloud host whose physical resources are reserved for the exclusive use of a single tenant. Elastic Compute Service (ECS) instances created on a dedicated host are physically isolated from those created on other hosts. This topic describes how to create a dedicated host.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Dedicat ed Host s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. On the Host s tab, click Creat e Host .
5. On the Creat e Host page, configure the parameters described in the following table.

| Section | Parameter | Description |
|---|---|---|
| Basic Settings | Organization | The organization in which to create the dedicated host. |
|   | Resource Set | The resource set in which to create the dedicated host. |
| Region and Zone | Region | The region in which to create the dedicated host. |
|   | Zone | The zone in which to create the dedicated host. |
| Instance | Dedicated Host Type | The type of the dedicated host. The dedicated host type determines the instance family and the maximum number of ECS instances that you can deploy on the dedicated host. |
|   | DDH Name | The name of the dedicated host. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens _ (-), colons (:), and commas (,). It must start with a letter and cannot start with http:// or https://. |
|   | Quantity | The number of dedicated hosts that you want to create. |
| DDH Settings | Allow Automatic Deployment | Specify whether to add the dedicated host to the resource pool for automatic deployment. Valid values: Allow Not Allow |

|   | osts Elastic Compute Servic |   |
|---|---|---|
| Section | Parameter | Description |
|   | Automatic Instance Migration upon DDH Failure | Specify whether to fail over the instances deployed on the dedicated host when it fails. Valid values: Enable Disable |

6. Click Submit .
Result After the dedicated host is created, you can view it in the Dedicated Host list and create instances on it. For more information about the parameters used to create an ECS instance, seeCreate an instance.

### Create a host group

You can group dedicated hosts into host groups for easy management. This topic describes how to create a host group.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Dedicat ed Host s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Host Groups tab.
5. Click Creat e Host Group.
6. On the Creat e Host Group page, configure the parameters described in the following table.

| Section | Parameter | Required | Description |
|---|---|---|---|
| Basic Settings | Organization | Yes | The organization in which to create the host group. |
|   | Resource Set | Yes | The resource set in which to create the host group. |
| Region and Zone | Region | Yes | The region in which to create the host group. |
|   | Zone | Yes | The zone in which to create the host group. |
| Instance | Host Group Name | No | The name of the host group. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), colons (:), and _ commas (,). It must start with a letter and cannot start with http:// or https://. |

7. Click Submit .
Result After the host group is created, you can view it in the host group list.

### Add dedicated hosts to a host

group After you create a host group, you can add dedicated hosts to the host group for easy management. This topic describes how to add dedicated hosts to a host group.
1. Log on to the ECS console.
2. In the left-side navigation pane, click Dedicat ed Host s.
3. In the top navigation bar, select an organization, a resource set, and a region.
4. Click the Host Groups tab.
5. Find the host group to which you want to add dedicated hosts and click Add Host in the Act ions
column.
6. In the Add Host panel, select a dedicated host and click Add Host .
To add a new dedicated host, you can click Creat e Host in the Add Host panel. For information about the parameters used to create a host, see Create a dedicated host. After the host is created, add it to the host group. Result After the dedicated host is added to the host group, you can click the host group name to view the dedicated host in the Host s list.

## Install FTP software

### Overview

File Transfer Protocol (FTP) transfers files between a client and a server by establishing two TCP connections. One is the command link for transferring commands between a client and a server. The other is the data link used to upload or download data. Before uploading files to an instance, you must build an FTP site for the instance.

### Install and configure vsftp in

CentOS This topic describes how to install and configure vsftp in CentOS to transfer files.
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

### Install vsftp in Ubuntu or Debian

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

### Build an FTP site in Windows

Server 2008 This topic describes how to build an FTP site on an instance running Windows Server 2008. Prerequisites You have added the Web Server (IIS) role and installed FTP on an instance.
1. Connect to an instance.
2. Choose St art > Adminst rat ive T ools > Int ernet Inf ormat ion Services (IIS) Manager.
3. Right-click the server name and select Add FT P Sit e from the shortcut menu.
4. Enter an FTP site name and a physical path, and then click Next .
5. Set IP Address to All Unassigned and SSL to No SSL, and then click Next .
6. Set Aut hent icat ion to Basic, Aut horizat ion to All Users, and Permissions to Read and Writ e,
and click Finish. Result Then you can use the administrator account and password to upload and download files through FTP. Make sure that the following conditions are met: The port for the FTP site is not in use by other applications, and Windows firewall is not blocking the port. The security group of the instance contains a security group rule that allows inbound access to the FTP port.

### Build an FTP site in Windows

Server 2012 This topic describes how to build an FTP site on an instance running Windows Server 2012. Prerequisites You have added the Web Server (IIS) role and installed FTP on an instance.
1. Connect to an instance.
2. Click the Server Manager icon.
3. In the left-side navigation pane, click IIS.
4. In the Server area, right-click the server name and select Int ernet Inf ormat ion Services (IIS)
Manager from the shortcut menu.
5. Right-click the server name and select Add FT P Sit e from the shortcut menu.
6. Enter an FTP site name and a physical path, and then click Next .
7. Set IP Address to All Unassigned and SSL to No SSL, and then click Next .
8. Set Aut hent icat ion to Basic, Aut horizat ion to All Users, and Permissions to Read and Writ e,
and click Finish. Result Then you can use the administrator account and password to upload and download files through FTP. Make sure that the following conditions are met: The port for the FTP site is not in use by other applications, and Windows firewall is not blocking the port. The security group of the instance contains a security group rule that allows inbound access to the FTP port.
