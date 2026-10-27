---
title: "Alibaba Cloud Apsara Stack V3.18.2 Virtual Private Cloud User Guide 20240425"
product_version: "V3.18.2"
doc_version: "20240425"
pdf_pages: 61
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Virtual Private Cloud User Guide 20240425.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/VPC/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Virtual%20Private%20Cloud%20User%20Guide%2020240425.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.2 Virtual Private Cloud User Guide 20240425

## Table of Contents

- 1 What is a VPC?
- 2 Log on to the VPC console
- 3 Quick start
  - 3.1 Plan networks
  - 3.2 Create a VPC with an IPv4 CIDR block
  - 3.3 Create a VPC with an IPv6 CIDR block
- 4 VPCs and VSwitches
  - 4.1 Overview
  - 4.2 VPC management
    - 4.2.1 Create a VPC
    - 4.2.2 Add a secondary IPv4 CIDR block
    - 4.2.3 Delete a secondary IPv4 CIDR block
    - 4.2.4 Modify the name and description of a VPC
    - 4.2.5 Delete a VPC
    - 4.2.6 Manage tags
  - 4.3 VSwitch management
    - 4.3.1 Create a vSwitch
    - 4.3.2 Create cloud resources
    - 4.3.3 Modify the information about a vSwitch
    - 4.3.4 Delete a vSwitch
    - 4.3.5 Manage tags
- 5 Route tables
  - 5.1 Overview
  - 5.2 Create a custom route table
  - 5.3 Add a custom route
  - 5.4 Export route entries
  - 5.5 Modify the information about a route table
  - 5.6 Delete a custom route
  - 5.7 Add subnet routes to a route table
- 6 HAVIPs
  - 6.1 Overview
  - 6.2 Create an HAVIP
  - 6.3 Associate HAVIPs with backend cloud resources
    - 6.3.1 Associates an HAVIP with an ECS instance
    - 6.3.2 Associate an HAVIP with an ENI
  - 6.4 Associate an HAVIP with an EIP
  - 6.5 Disassociate HAVIPs from backend cloud resources
    - 6.5.1 Disassociate an HAVIP from an ECS instance
    - 6.5.2 Disassociate an HAVIP from an ENI
  - 6.6 Disassociate an HAVIP from an EIP
  - 6.7 Delete an HAVIP
- 7 Network ACLs
  - 7.1 Overview
  - 7.2 Scenarios
  - 7.3 Create a network ACL
  - 7.4 Associate a network ACL with a vSwitch
  - 7.5 Add network ACL rules
    - 7.5.1 Add an inbound rule
    - 7.5.2 Add an outbound rule
    - 7.5.3 Change the priorities of network ACL rules
  - 7.6 Disassociate a network ACL from a vSwitch
  - 7.7 Delete a network ACL

## 1 What is a VPC?

A virtual private cloud (VPC) is a private network in the cloud. You can configure the CIDR block, route tables, and gateways of your VPC. You can use Alibaba Cloud services in a VPC, such as Elastic Compute Service (ECS), Server Load Balancer (SLB), and ApsaraDB RDS. You can connect your VPC to other VPCs or on-premises networks to create a custom network environment. This way, you can migrate applications to the cloud and extend data centers.

**Components**

Each VPC consists of one vRouter, at least one private CIDR block, and at least one vSwitch. Private CIDR blocks When you create a VPC and a vSwitch, you must specify the private IP address range for the VPC in CIDR notation. You can use the standard private CIDR blocks listed in the following table and their subsets as CIDR blocks for your VPCs. For more information, see the **Plan and design a VPC** topic in **User Guide**.

| CIDR block | Number of available private IP addresses (excluding system reserved IP addresses) |
|---|---|
| 192.168.0.0/16 | 65,532 |
| 172.16.0.0/16 | 65,532 |

vRouters A vRouter is the hub of a VPC. As a core component, it connects the vSwitches in a VPC and serves as a gateway between a VPC and other networks. After you create a VPC, the system automatically creates a vRouter. Each vRouter is associated with a route table. For more information, see the **Route table overview** topic in **User Guide**. vSwitches A vSwitch is a basic network component that connects different cloud resources in a VPC. After you create a VPC, you can create vSwitches to create one or more subnets for the VPC. vSwitches in the same VPC can communicate with each other. You can deploy your applications in vSwitches that belong to different zones to improve service availability. For more information, see the **Create a vSwitch** topic in **User Guide**. nsole

## 2 Log on to the VPC console

This topic describes how to log on to the Apsara Uni-manager Management Console to manage virtual private clouds (VPCs) by using the Google Chrome browser.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Login**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Multi-factor authentication** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.

## 3 Quick start

### 3.1 Plan networks

Before you create virtual private clouds (VPCs) and vSwitches, you must decide the quantities and CIDR blocks of VPCs and vSwitches. How many VPCs do I use? How many vSwitches do I use? How do I specify CIDR blocks? How do I specify CIDR blocks if I want to connect a VPC to another VPC or a data center?

**How many VPCs do I use?**

One VPC If you do not want to deploy your business systems across regions or isolate different business systems, we recommend that you use one VPC. Multiple VPCs In the following scenarios, we recommend that you use multiple VPCs: Cross-region deployment A VPC cannot be deployed across regions. If you want to deploy your business system across regions, you must create VPCs in these regions. Then, you can use services such as Express Connect and VPN Gateway to connect the VPCs. Service isolation If you want to isolate business systems deployed in the same region, you must create multiple VPCs. The following figure shows how the test environment is isolated from the production environment by using VPCs.

**How many vSwitches do I use?**

We recommend that you create at least two vSwitches in different zones for a VPC. This implements cross-zone disaster recovery. The network latency between different zones in a region is low. However. you still need to verify the network latency in your actual business system. This is because the network latency may be higher than expected due to complex data processing or cross-zone data transmission. We recommend that you optimize and adjust your business system to strike a balance between availability and latency. In addition, the size and design of your business system must also be taken into consideration when you create vSwitches. If the frontend system can be accessed from the Internet and needs to access the Internet, you can deploy the frontend system in different vSwitches and deploy the backend system in another vSwitch. This implements disaster recovery.

**How do I specify CIDR blocks?**

When you create VPCs and vSwitches, you must specify their private IP addresses in CIDR block notation. Specify VPC CIDR blocks You can specify 172.16.0.0/16, 192.168.0.0/16, or their subnets as the CIDR blocks of your VPCs. When you specify CIDR blocks for VPCs, take note of the following rules: If you have only one VPC and the VPC does not need to communicate with a data center, you can specify one of the preceding CIDR blocks or their subnets as the VPC CIDR block. If you have multiple VPCs, or you want to set up a hybrid cloud environment between a VPC and your data center, we recommend that you specify the subnets of the preceding CIDR blocks for your VPCs. In this case, we recommend that you set the subnet mask length to 16 bits or less. Specify vSwitch CIDR blocks The CIDR block of a vSwitch must be a subset of the CIDR block of the VPC to which the vSwitch belongs. For example, if the CIDR block of a VPC is 192.168.0.0/16, the CIDR block of a vSwitch that belongs to the VPC can range from 192.168.0.0/17 to 192.168.0.0/29. When you specify vSwitch CIDR blocks, take note of the following rules: The subnet mask of a vSwitch CIDR block must be 16 to 29 bits in length, which provides 8 to 65,536 IP addresses. A 16-bit subnet mask provides IP addresses for 65,532 Elastic Compute Service (ECS) instances, which can meet your needs in most cases. A subnet mask of more than 29 bits in length provides few IP addresses. The first IP address and the last three IP addresses of a vSwitch CIDR block are reserved. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. When you specify the CIDR block of a vSwitch, you must also take into consideration the number of ECS instances that you want to attach to the vSwitch.

**How do I specify CIDR blocks if I want to connect a VPC to**

**another VPC or a data center?**

Before you connect your VPC to another VPC or a data center, you must make sure that the VPC CIDR block does not conflict with that of the peer network. When you specify CIDR blocks for multiple VPCs that need to communicate with each other, take note of the following rules: The preferred practice is to specify different CIDR blocks for different VPCs. You can use the subnets of standard CIDR blocks if the given CIDR blocks are insufficient. If you cannot assign different CIDR blocks to the VPCs, try to specify different CIDR blocks for vSwitches in these VPCs. If you cannot assign different CIDR blocks to all of the vSwitches in these VPCs, make sure that different CIDR blocks are specified for the vSwitches that need to communicate with each other.

### 3.2 Create a VPC with an IPv4 CIDR block

**CIDR block**

This topic describes how to create a virtual private cloud (VPC) with an IPv4 CIDR block and create an Elastic Compute Service (ECS) instance in the VPC.

**Prerequisites**

To deploy cloud resources in a VPC, you must first plan the networks. For more information, see Plan networks.

**Step 1: Create a VPC**

1. Log on to the VPC console.
2. On the **Virtual Private Clouds** page, click **Create a proprietary network**.
3. On the **Create VPC** page, set the parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Region |   |
| Organization | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Basic Configurations |   |

| Sharing Scope | Select the sharing scope of the VPC. Current Resource Set: Only the administrator of the current resource set can use the VPC to create resources. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can use the VPC to create resources. Current Organization: Only the administrator of the current organization can use the VPC to create resources. Current Resource Set is selected in this example. |
|---|---|
| VPC Name | Enter a name for the VPC. VPCtest is used in this example. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Custom CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. Example: 192.168.0.0/16. In this example, 192.168.0.0/16 is used as the IPv4 CIDR block of the VPC. Note After a VPC is created, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. Do Not Assign is selected in this example. |
| Description | Enter a description for the VPC. |

4. In the **Created.** message, click **OK**. Return to the **Virtual Private Clouds** page to view the
created VPC.

**Step 2: Create a vSwitch**

1. In the left-side navigation pane, click **VSwitches**.
2. On the **VSwitches** page, click **Create a switch**.
3. On the **Create vSwitch** page, set the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Basic Information |   |
| Organization | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region |   |

| Region | Select the region where you want to deploy the vSwitch. |
|---|---|
| Zone | Select the zone where you want to deploy the vSwitch. In a VPC, a vSwitch can be deployed only in one zone. You cannot deploy a vSwitch across zones. You can deploy cloud resources in vSwitches in different zones to implement cross-zone disaster recovery. Note An instance can be deployed in only one vSwitch. |
| Detailed Settings |   |
| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set: Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organization: Only the administrator of the current organization can use the vSwitch to create resources. Current Resource Set is selected in this example. |
| VPC | Select the VPC in which you want to create the vSwitch. VPCtest is selected in this example. |
| Dedicated for Bare Metal Instances | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-metal servers in VPCs topic in Apsara Intelligent Operations Platform User Guide. No is selected in this example. |
| vSwitch Name | Enter a name for the vSwitch. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. The default IPv4 CIDR block is used in this example. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. If the VPC is not assigned an IPv6 CIDR block, the vSwitch is not assigned an IPv6 CIDR block. In this example, no IPv6 CIDR block is assigned to the vSwitch. |
| Description | Enter a description for the vSwitch. |

**Step 3: Create a security group**

1. In the top navigation bar, choose **Products > Elastic Computing > Elastic Compute**
**Service**.
2. In the left-side navigation pane, choose **Network and Security > Security Groups**.
3. On the **Security Groups** page, click **Create Security Group**.
4. On the **Create Security Group** page, set the parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Area |   |
| Organization | Select the organization to which the security group belongs. |
| Resource Set | Select the resource set to which the security group belongs. |
| Region | Select the region where you want to deploy the security group. Make sure that the security group and the VPC belong to the same region. |
| Zone | Select the zone where you want to deploy the security group. |
| Basic Information |   |
| Sharing Scope | Select the sharing scope of the security group. Current Resource Set: Only the administrator of the current resource set can create resources for the security group. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can create resources for the security group. Current Organization: Only the administrator of the current organization can create resources for the security group. Current Resource Set is selected in this example. |
| VPC | Select the VPC to which the security group belongs. |
| Security Group Name | Enter a name for the security group. |
| Description | Enter a description for the security group. |

**Step 4: Create an ECS instance**

1. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.
2. In the left-side navigation pane, click **VSwitches**.
3. In the top navigation bar, select the region where the vSwitch is deployed.
4. On the **VSwitches** page, find the vSwitch and click **Create ECS Instance** in the
**Operation** column.
5. On the **Create Instance** page, set the parameters.
For more information about how to configure ECS instances, see the **Create an ECS**
**instance** topic in the **Quick start** chapter of **ECS User Guide**.

### 3.3 Create a VPC with an IPv6 CIDR block

**CIDR block**

This topic describes how to create a virtual private cloud (VPC) with an IPv6 CIDR block and create Elastic Compute Service (ECS) instances with IPv6 addresses in the VPC. This way, the ECS instances can access IPv6 services.

**Step 1: Create a VPC and a vSwitch**

Before you deploy cloud resources in a VPC, you must create a VPC and a vSwitch.
1. Log on to the VPC console.
2. On the **Virtual Private Clouds** page, click **Create a proprietary network**.
3. On the **Create VPC** page, set the parameters and click **Submit**.

| Paramet er | Description |
|---|---|
| Organiza tion | Select the organization to which the VPC belongs. |
| Resourc e Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Sharing Scope | Select the sharing scope of the VPC. Current Resource Set: Only the administrator of the current resource set can use the VPC to create resources. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can use the VPC to create resources. Current Organization: Only the administrator of the current organization can use the VPC to create resources. Current Resource Set is selected in this example. |
| VPC Name | Enter a name for the VPC. VPCtest is used in this example. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Custom CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. Example: 192.168.0.0/16. In this example, 192.168.0.0/16 is used as the IPv4 CIDR block of the VPC. Note After a VPC is created, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. Assign is selected in this example. |
| Descripti on | Enter a description for the VPC. |

4. On the **Virtual Private Clouds** page, click **VSwitches** in the left-side navigation pane.
5. On the **VSwitches** page, click **Create a switch**.
6. On the **Create vSwitch** page, set the following parameters and click **Submit**.

| Parameter | Description |
|---|---|

| Organization | Select the organization to which the vSwitch belongs. |
|---|---|
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone where you want to deploy the vSwitch. In a VPC, a vSwitch can be deployed only in one zone. You cannot deploy a vSwitch across zones. You can deploy cloud resources in vSwitches in different zones to implement cross-zone disaster recovery. Note An instance can be attached only to one vSwitch. |
| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set: Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organization: Only the administrator of the current organization can use the vSwitch to create resources. Current Resource Set is selected in this example. |
| VPC | Select the VPC in which you want to create the vSwitch. VPCtest is selected in this example. |
| Dedicated for Bare Metal Instances | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-metal servers in VPCs topic in Apsara Intelligent Operations Platform User Guide. No is selected in this example. |
| vSwitch Name | Enter a name for the vSwitch. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. The default IPv4 CIDR block is used in this example. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. The default IPv6 CIDR block is used in this example. |
| Description | Enter a description for the vSwitch. |

**Step 2: Create a security group**

1. In the top navigation bar, choose **Products > Elastic Computing > Elastic Compute**
**Service**.
2. In the left-side navigation pane, choose **Network and Security > Security Groups**.
3. On the Security Groups page, click **Create Security Group**.
4. On the **Create Security Group** page, set the parameters and click **Submit**.

| Parameter | Description |
|---|---|

| Organization | Select the organization to which the security group belongs. |
|---|---|
| Resource Set | Select the resource set to which the security group belongs. |
| Region | Select the region where you want to deploy the security group. Make sure that the security group and the VPC belong to the same region. |
| Zone | Select the zone where you want to deploy the security group. |
| Sharing Scope | Select the sharing scope of the security group. Current Resource Set: Only the administrator of the current resource set can create resources for the security group. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can create resources for the security group. Current Organization: Only the administrator of the current organization can create resources for the security group. Current Resource Set is selected in this example. |
| VPC | Select the VPC to which the security group belongs. |
| Security Group Name | Enter a name for the security group. |
| Description | Enter a description for the security group. |

**Step 3: Create and configure an ECS instance**

After you create a VPC with an IPv6 CIDR block and a vSwitch, create an ECS instance and assign an IPv6 address to the ECS instance. You must allocate the IPv6 address to the elastic network interface (ENI) of the ECS instance.
1. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.
2. In the left-side navigation pane, click **VSwitches**.
3. In the top navigation bar, select the region where the vSwitch is deployed.
4. On the **VSwitches** page, find the vSwitch and click **Create ECS Instance** in the
**Operation** column.
5. On the **Create Instance** page, set the parameters and click **Submit**.
In this example, **Assign** is selected for IPv6. For more information about other parameters, see **Create an ECS instance by using the wizard** in **Quick start** of **ECS User Guide**.
6. Return to the **Instances** page, find the created ECS instance and click its ID to view the
assigned IPv6 address.
7. Configure the static IPv6 address.
If the image of your ECS instance supports DHCPv6, you do not need to manually configure the static IPv6 address. DHCPv6 enables automatic configuration of IPv6 addresses. Therefore, if the image of your ECS instance supports DHCPv6, the ECS instance uses the assigned IPv6 address for communication within the private network. The following images support DHCPv6: Linux images: CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images If the image of your ECS instance does not support DHCPv6, you must manually configure the IPv6 address for your ECS instance. For more information, see the relevant documentation.

**Step 4: Purchase IPv6 Internet bandwidth**

By default, IPv6 addresses are used only for communication within private networks. If you want to use an IPv6 address to access the Internet or provide services to IPv6 clients over the Internet, you must purchase Internet bandwidth for the IPv6 address.
1. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.
2. In the left-side navigation pane, click **IPv6 Gateways**.
3. In the top navigation bar, select the region where the IPv6 gateway is deployed.
4. On the **IPv6 Gateways** page, find the IPv6 gateway that you want to manage and click
**Management** in the **Operation** column.
5. On the details page of the IPv6 gateway, click the **IPv6 public network bandwidth** tab.
6. On the **IPv6 public network bandwidth** tab, find the IPv6 address that you want to
manage and click **Open public network bandwidth** in the **Operation** column.
7. Select a maximum bandwidth value and click **Submit**.
For IPv6 gateways of Free Edition, Enterprise Edition, and Enhanced Enterprise Edition, the maximum bandwidth value of each IPv6 address cannot exceed 2 Gbit/s.

**Step 5: Configure security group rules**

Services that are assigned IPv4 addresses and services that are assigned IPv6 addresses cannot communicate with each other. If the current security group rules do not support your IPv6 services, you must configure IPv6 security group rules for ECS instances. For more information about how to configure security group rules, see the **Add security**
**group rules** chapter in **Security groups** of **ECS User Guide**.

**Step 6: Verify the network connectivity**

Log on to an ECS instance and **ping** an IPv6 service to verify the network connectivity.

## 4 VPCs and VSwitches

### 4.1 Overview

Before you can use cloud resources in a virtual private cloud (VPC), you must create a VPC and a vSwitch. You can create multiple vSwitches to divide a VPC into multiple subnets. By default, the subnets in a VPC can communicate with each other.

**VPCs and vSwitches**

VPCs are private networks dedicated to tenants.

> **Note:** You cannot directly deploy cloud resources in a VPC. You must deploy cloud resources in the vSwitches of a VPC.

A vSwitch is a basic network device in a VPC and is used to connect cloud resources. You can deploy a VPC only in one region and cannot deploy a VPC across regions. However, a VPC covers all zones of the region to which the VPC belongs. You can create one or more vSwitches in a zone to divide a VPC into subnets.

**CIDR blocks and IP addresses**

VPCs support both IPv4 and IPv6. By default, VPCs use IPv4. You can enable IPv6 based on your business requirements. VPCs support the dual-stack mode. In dual-stack mode, resources in a VPC can communicate through both IPv4 and IPv6 addresses. IPv4 and IPv6 addresses are independent of each other. Therefore, you must configure routes and security groups for both IPv4 and IPv6 addresses. The following table lists the differences between IPv4 and IPv6 addresses.

| IPv4 VPC | IPv6 VPC |
|---|---|
| 32 binary digits. An IPv4 address appears as four decimal numbers separated by periods (.).Example: 192.168.1.11. | 128 binary digits. An IPv6 address appears as eight hexadecimal numbers separated by colons (:). Example: 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff. |
| By default, IPv4 is enabled. | You can enable IPv6 as needed. |
| The subnet mask of a VPC CIDR block can range from /8 to /24. | The subnet mask of a VPC CIDR block is /61. |
| The subnet mask of a vSwitch CIDR block can range from /16 to /29. | The subnet mask of a vSwitch CIDR block is /64. |
| You can specify an IPv4 CIDR block. | You cannot specify an IPv6 CIDR block. The system automatically assigns an IPv6 CIDR block to your VPC from the IPv6 address pool. |
| Supported by all instance types. | Not supported by some instance types. For more information, see Instance types under What is ECS? in the Elastic Compute Service User Guide. |
| IPv4 elastic IP addresses (EIPs) are supported. | IPv6 EIPs are not supported. |
| VPN gateways and NAT gateways are supported. | VPN gateways and NAT gateways are not supported. |

By default, IPv4 and IPv6 addresses provided for VPCs support only communication over private networks. Cloud resources deployed in different vSwitches that belong to the same VPC can communicate with each other over private networks. To connect a VPC to another VPC or a data center, you can use Express Connect or VPN Gateway. To enable cloud resources in a VPC to communicate with the Internet, perform the following operations: IPv4 addresses You can configure NAT gateways or associate EIPs with Elastic Compute Service (ECS) instances in a VPC. This way, the ECS instances can communicate with the Internet through IPv4 addresses. IPv6 addresses To enable cloud resources in a VPC to communicate with the Internet through IPv6 addresses, you must purchase an IPv6 public bandwidth plan. You can configure egressonly rules for IPv6 addresses. This allows cloud resources in the VPC to access the Internet through IPv6 addresses. However, IPv6 clients cannot access the cloud resources over the Internet.

**Routes**

After you create a VPC, the system creates a system route table for the VPC and adds system routes to the route table. The system routes are used to route traffic within the VPC. A VPC has only one system route table. You cannot create or delete a system route table. You can create and associate custom route tables with vSwitches to facilitate network management. A vSwitch can be associated only with one route table. For more information, see Create a custom route table. If multiple route entries match the destination IP address, the route entry with the longest subnet mask is preferably used to determine the next hop. This ensures that the traffic is routed to the most precise destination. You can also add a custom route entry to route traffic to a specified destination. For more information, see Add a custom route.

### 4.2 VPC management

#### 4.2.1 Create a VPC

A virtual private cloud (VPC) is a private network in the cloud. You have full control over your VPC. For example, you can specify CIDR blocks, and configure route tables and gateways for your VPC. This topic describes how to create a VPC.

**Prerequisites**

Before you create a VPC, you must plan your networks. For more information, see Plan networks.

**Procedure**

1. Log on to the VPC console.
2. In the top navigation bar, select the region where you want to deploy the VPC.

> **Note:** The VPC and the cloud resources that you want to deploy in the VPC must belong to the same region.

3. In the left-side navigation pane, select **Virtual Private Clouds**.
4. On the **VPC** page, click **Create VPC**.
5. On the **Create a VPC** page, set the parameters and click **Submit**.

| Paramet er | Description |
|---|---|
| Organiza tion | Select the organization to which the VPC belongs. |
| Resourc e set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Shared Scope | Select the sharing scope of the VPC. This resource set: Only the administrator of the current resource set can use the VPC to create resources. This organization and its subordinate organization: Only the administrators of the current organization and its subordinate organizations can use the VPC to create resources. The organization: Only the administrator of the current organization can use the VPC to create resources. |
| Private Network Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a letter and cannot start _ with a http:// or a https:// . |

| IPv4 network segment | Specify an IPv4 CIDR block for the VPC. The following settings are supported: Recommended network segment: You can select the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Advanced Configuration network segment: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/24. Note After a VPC is created, you cannot change its IPv4 CIDR block. |
|---|---|
| IPv6 network segment | Specify whether to assign an IPv6 CIDR block. Not assigned: The system does not assign an IPv6 CIDR block to the VPC. Allocation: The system automatically assigns an IPv6 CIDR block to the VPC. Note If you select Not assigned, you can click Enable IPv6 in the IPv6 network segment column on the VPC page after the VPC is created. In the Enable IPv6 dialog box, you can select Enable IPv6 for all vSwitches in VPC to enable IPv6 for all vSwitches in the VPC. The system automatically creates a Free Edition IPv6 gateway for this VPC, and assigns an IPv6 CIDR block with the subnet mask /61, such as 2XX1:db8::/61. By default, IPv6 addresses are used only for communication within private networks. If you want to use an IPv6 address to access the Internet or provide services for IPv6 clients over the Internet, you must purchase Internet bandwidth for the IPv6 address. For more information, see the Enable IPv6 Internet bandwidth chapter in Manage IPv6 Internet bandwidth in IPv6 Gateway User Guide. |
| Address Pool | Select an address pool type. You can select only BGP. Note This parameter is required when you allocate an IPv6 CIDR block. |
| Descript ion | Enter a description for the VPC. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

#### 4.2.2 Add a secondary IPv4 CIDR block

After a virtual private cloud (VPC) is created, you can add a secondary IPv4 CIDR block to expand the VPC.

**Prerequisites**

A VPC is created. For more information, see Create a VPC.

**Background information**

The IPv4 CIDR block that you configure when you create a VPC is the primary IPv4 CIDR block. After a VPC is created, the primary IPv4 CIDR block of the VPC cannot be modified. However, you can add a secondary IPv4 CIDR block to expand the VPC. After you add a secondary IPv4 CIDR block to the VPC, both the primary and secondary IPv4 CIDR blocks are in effect. You can create a vSwitch with the primary IPv4 CIDR block or the secondary IPv4 CIDR block. However, each vSwitch belongs to only one VPC CIDR block. The system automatically adds a vSwitch route to the VPC route table when you create a vSwitch with the primary IPv4 CIDR block or a secondary IPv4 CIDR block. The destination CIDR block of the vSwitch route is the CIDR block with which the vSwitch is created. The CIDR block range cannot be the same as or larger than those of other routes in the route table of the VPC.

> **Note:** You can add only one secondary IPv4 CIDR block to a VPC and cannot increase the quota.

**Procedure**

1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the **VPC** page, find the VPC and click **Manage** in the **Actions** column.
4. On the **Network segment management** tab, click **Add Secondary IPv4 CIDR Block**.
5. In the **Add Secondary CIDR Block** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| VPC | Displays the VPC to which you want to add the secondary IPv4 CIDR block. |

| Secondary CIDR Block | Select a method to configure the secondary IPv4 CIDR block: Default CIDR Block: You can specify one of the following standard IPv4 CIDR blocks as the secondary IPv4 CIDR block: 192.168.0.0/16 and 172.16.0.0/12. Custom CIDR Block: You can specify one of the following standard IPv4 CIDR blocks or one of their subnets as the secondary IPv4 CIDR block: 192.168.0.0/16 and 172.16.0.0/12. When you add a secondary IPv4 CIDR block, take note of the following limits: The CIDR block cannot start with 0. The mask must be 8 to 24 bits in length. The secondary IPv4 CIDR block cannot overlap with the primary IPv4 CIDR block or an existing secondary IPv4 CIDR block. For example, if the primary IPv4 CIDR block of a VPC is 192.168.0.0/16, you cannot specify one of the following CIDR blocks as a secondary IPv4 CIDR block: A CIDR block larger than 192.168.0.0/16, for example, 192.168.0.0/8. 192.168.0.0/16. A CIDR block smaller than 192.168.0.0/16, for example, 192.168.0.0/24. |
|---|---|

#### 4.2.3 Delete a secondary IPv4 CIDR block

You can delete the secondary IPv4 CIDR block of a virtual private cloud (VPC). However, you cannot delete the primary IPv4 CIDR block of a VPC.

**Prerequisites**

Before you delete a secondary IPv4 CIDR block, make sure that the vSwitches created with the secondary IPv4 CIDR block are deleted. For more information, see Delete a vSwitch.

**Procedure**

1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the **Virtual Private Clouds** page, find the VPC that you want to manage, and click
**Management** in the **Operation** column.
4. On the **Network segment management** tab, find the secondary IPv4 CIDR block and click
**Delete** in the **Operation** column.
5. In the message that appears, click **OK**.

#### 4.2.4 Modify the name and description of a VPC

**VPC**

This topic describes how to modify the name and description of a VPC.

**Procedure**

1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the **Virtual Private Clouds** page, find the VPC that you want to manage, and click
**Management** in the **Operation** column.
4. In the **VPC Basic Information** section, click
next to **VPC name**. In the dialog box that appears, enter a new name and click **OK**. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
5. In the **VPC Basic Information** section, click
next to **Description**. In the dialog box that appears, enter a new description and click **OK**. The description must be 2 to 256 characters in length. It cannot start with `http://` or

```
 https:// .
```

#### 4.2.5 Delete a VPC

This topic describes how to delete a virtual private cloud (VPC). After you delete a VPC, vRouters and route tables that are associated with the VPC are also deleted.

**Prerequisites**

Before you delete a VPC, make sure that the following requirements are met: No vSwitch exists in the VPC. If the VPC contains a vSwitch, you must delete the vSwitch before you delete the VPC. For more information, see Delete a vSwitch. No IPv6 gateway exists in the VPC. If an IPv6 gateway exists in the VPC, delete the IPv6 gateway first. For more information, see the **Delete an IPv6 gateway** topic in the
**Manage IPv6 gateways** chapter of **IPv6 Gateway User Guide**.

**Procedure**

1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the **Virtual Private Clouds** page, find the VPC that you want to delete, and click
**Delete** in the **Operation** column.
4. In the **Delete a proprietary network** dialog box, click **OK**.

#### 4.2.6 Manage tags

Virtual Private Cloud (VPC) supports the tag feature. You can use tags to mark and classify VPCs. This allows you to search for and filter VPCs in a more efficient manner.

**Procedure**

1. Log on to the VPC console.
2. In the top navigation bar, select the region where you want to deploy the VPC.
3. On the **Virtual Private Clouds** page, find the VPC that you want to manage, move the
pointer over **-** or to the right of an existing tag in the **Tag** column, and then click the icon.
4. In the **Edit Tag** dialog box, click **Add**, set the following parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Tag Key | Specify a tag key. You can select or enter a tag key. The key must be 1 to 64 characters in length, and cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

| Tag Value | Specify a tag value. You can select or enter a tag value. The value cannot exceed 128 characters in length, and cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
|---|---|

5. Return to the **Virtual Private Clouds** page and click **Tag Filter**. In the dialog box that
appears, you can filter VPCs based on tag keys and tag values.

### 4.3 VSwitch management

#### 4.3.1 Create a vSwitch

A vSwitch is a basic network component that connects different cloud resources in a virtual private cloud (VPC).

**Background information**

After you create a VPC, you can create vSwitches to create one or more subnets for the VPC. vSwitches in the same VPC can communicate with each other. Cloud resources must be deployed in vSwitches. You can deploy applications in vSwitches that belong to different zones to ensure service availability.

> **Note:** vSwitches do not support multicasting or broadcasting.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **VSwitches**.
3. In the top navigation bar, select the region of the VPC where you want to create a vSwitch.
4. On the **VSwitches** page, click **Create a switch**.
5. On the **Create vSwitch** page, set the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Organization | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone where you want to deploy the vSwitch. In a VPC, a vSwitch can be deployed only in one zone. You cannot deploy a vSwitch across zones. You can deploy cloud resources in vSwitches in different zones to implement cross-zone disaster recovery. Note An instance can be attached only to one vSwitch. |

| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set: Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organization and Subordinate Organizations: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organization: Only the administrator of the current organization can use the vSwitch to create resources. |
|---|---|
| VPC | Select the VPC in which you want to create the vSwitch. |
| Dedicated for Bare Metal Instances | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-metal servers in VPCs topic in Apsara Intelligent Operations Platform User Guide. |
| vSwitch Name | Enter a name for the vSwitch. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. You must specify the IP address range of the vSwitch in CIDR notation. The subnet mask must be 16 to 29 bits in length, which specifies that 8 to 65,536 IP addresses are available. The CIDR block of a vSwitch must be a proper subset of the CIDR block of the VPC to which the vSwitch belongs. The first IP address and the last three IP addresses of a vSwitch CIDR block are reserved. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The CIDR block of a vSwitch cannot be the same as the destination CIDR block in a route of the VPC to which the vSwitch belongs. However, the CIDR block of the vSwitch can be a subset of the destination CIDR block of a route. After a vSwitch is created, you cannot modify its CIDR block. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. You must check whether IPv6 is enabled for the specified VPC. If IPv6 is not enabled, you cannot assign an IPv6 CIDR block to the vSwitch. If IPv6 is enabled for the VPC, you can enter a decimal number that ranges from 0 to 7 to define the last 8 bits of the IPv6 CIDR block of the vSwitch. For example, if the IPv6 CIDR block of the VPC is 2XX1:db8::/64, you can enter 255 to define the last 8 bits of the IPv6 CIDR block. In this case, the IPv6 CIDR block of the vSwitch is 2XX1:db8:ff::/64. ff is the hexadecimal value of 255. |
| Description | Enter a description for the vSwitch. |

#### 4.3.2 Create cloud resources

You cannot directly deploy cloud resources in a virtual private cloud (VPC). You must deploy cloud resources in a vSwitch in a VPC. This topic describes how to create cloud resources in a vSwitch. You can create Elastic Compute Service (ECS), Server Load Balancer (SLB), and ApsaraDB RDS instances in a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click **VSwitches**.
3. In the top navigation bar, select the region of the VPC to which the vSwitch belongs.
4. On the **VSwitches** page, you can create the following cloud resources.
Click **Create ECS Instance** in the **Operation** column, and then create an ECS instance on the **Create Instance** page. For more information about how to configure ECS instances, see the **Create an ECS**
**instance** topic in the **Quick start** chapter of **ECS User Guide**.
In the **Operation** column, choose
**> Create SLB Instance**, and then create an SLB
instance on the **Create SLB Instance** page. For more information about how to configure SLB instances, see the **Create an SLB**
**instance** topic in the **Quick start** chapter of **SLB User Guide**.
In the **Operation** column, choose
**> Create ApsaraDB RDS Instance**, and then
create an ApsaraDB RDS instance on the **Create Instance** page. For more information about how to configure ApsaraDB RDS instances, see the **Create**
**an ApsaraDB RDS instance** topic in the **Quick start** chapter of **ApsaraDB RDS User**
**Guide**.

#### 4.3.3 Modify the information about a vSwitch

This topic describes how to modify the name and description of a vSwitch.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **VSwitches**.
3. In the top navigation bar, select the region of the VPC to which the vSwitch belongs.
4. On the **VSwitches** page, find the vSwitch that you want to manage and click
**Management** in the **Operation** column.
5. In the **Switch Basic information** section, click
next to **Switch name**. In the dialog box that appears, enter a new name. The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter.
6. In the **Switch Basic information** section, click
next to **Description**. In the dialog box that appears, enter a new description. The description must be 2 to 256 characters in length. It cannot start with `http://` or

```
 https:// .
```

#### 4.3.4 Delete a vSwitch

This topic describes how to delete a vSwitch. After you delete a vSwitch, you cannot deploy cloud resources in it.

**Prerequisites**

Before you delete a vSwitch, make sure that the following requirements are met: Cloud resources created in the vSwitch are deleted, such as Elastic Compute Service (ECS), Server Load Balancer (SLB), and ApsaraDB RDS instances. All resources associated with the vSwitch are deleted, such as high-availability virtual IP addresses (HAVIPs) and SNAT entries.
1. Log on to the VPC console.
2. In the left-side navigation pane, click **VSwitches**.
3. Select the virtual private cloud (VPC) to which the vSwitch belongs.
4. On the **VSwitches** page, find the vSwitch that you want to delete and click **Delete** in the
**Operation** column.
5. In the **Delete vSwitch** message, click **OK**.

#### 4.3.5 Manage tags

vSwitches support tags. You can use tags to mark and classify vSwitches. This allows you to search for and filter vSwitches in a more efficient manner.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **VSwitches**.
3. In the top navigation bar, select the region of the VPC to which the vSwitch belongs.
4. On the **VSwitches** page, find the vSwitch that you want to manage, move the pointer over
the **-** icon or to the right of an existing tag in the **Tag** column, and then click the icon.
5. In the **Edit Tag** dialog box, click **Add**, set the following parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Tag Key | Specify a tag key. You can select or enter a tag key. The key must be 1 to 64 characters in length, and cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| Tag Value | Specify a tag value. You can select or enter a tag value. The value cannot exceed 128 characters in length, and cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

6. Return to the **VSwitches** page and click **Tag Filter**. In the dialog box that appears, filter
vSwitches based on tag keys and tag values.

## 5 Route tables

### 5.1 Overview

After you create a virtual private cloud (VPC), the system automatically creates a system route table for the VPC and adds system routes to the route table. The system routes are used to route traffic within the VPC. You cannot create or delete system routes. However, you can create custom routes to route traffic from a specified CIDR block to a specified destination.

**Route tables**

After you create a VPC, the system creates a system route table to manage routes of the VPC. By default, vSwitches in the VPC use this route table. You cannot create or delete the system route table of a VPC. However, you can create a custom route table and associate it with a vSwitch to manage your network in a more flexible way. When you associate a vSwitch with a custom route table, the vSwitch is automatically disassociated from the system route table. For more information, see Add subnet routes to a route table. Each entry in a route table is a route entry. A route entry specifies the destination to which network traffic is routed and consists of the destination CIDR block, next hop type, and next hop. Route entries include system route entries and custom route entries.

**System routes**

After you create a VPC, the system automatically adds the following system routes to the route table: A route entry with a destination CIDR block of 100.64.0.0/10. This route is used for communication among cloud resources within the VPC. Route entries whose destination CIDR blocks are the same as the CIDR blocks of the vSwitches in the VPC. These routes are used for communication among cloud resources within the vSwitches. For example, if you create a VPC whose CIDR block is 192.168.0.0/16 and two vSwitches whose CIDR blocks are 192.168.1.0/24 and 192.168.0.0/24, three system routes are automatically added to the route table of the VPC. The following table describes the system routes.

| Destination CIDR block | Next hop | Type |
|---|---|---|
| 100.64.0.0/10 | - | System route |
| 192.168.1.0/24 | - | System route |
| 192.168.0.0/24 | - | System route |

**Custom routes**

You can add custom routes to replace system routes or route traffic to a specified destination. You can specify the following types of next hops when you create a custom route: Elastic Compute Service (ECS) instance: Traffic that is destined for the destination CIDR block is routed to a specified ECS instance in the VPC. You can select this type if the application deployed on the ECS instance needs to access the Internet or other applications. VPN gateway: Traffic destined for the destination CIDR block is routed to a specified VPN gateway. You can select this type if you want to connect a VPC to another VPC or an on-premises network through the VPN gateway. NAT gateway: Traffic destined for the destination CIDR block is routed to a specified NAT gateway. You can select this type if you want to connect a VPC to the Internet through the NAT gateway. Router interface (to VPC): Traffic that is destined for the destination CIDR block is routed to a specified VPC. You can select this type if you want to connect two VPCs through Express Connect circuits. Router interface (to VBR): Traffic that is destined for the destination CIDR block is routed to a specified virtual border router (VBR). You can select this type if you want to connect a VPC to an on-premises network through Express Connect circuits. Secondary ENI: Traffic that is destined for the destination CIDR block is routed to a specified secondary elastic network interface (ENI). IPv6 gateway: Traffic that is destined for the destination CIDR block is routed to a specified IPv6 gateway. You can select this type if you want to implement IPv6 communication through an IPv6 gateway.

**IPv6 routes**

If IPv6 is enabled for your VPC, the following route entries are automatically added to the system route table of the VPC: A custom route entry whose destination CIDR block is ::/0 and whose next hop is the IPv6 gateway. Cloud resources deployed in the VPC use this route to access the Internet through IPv6 addresses. A system route entry of which the destination CIDR block is the IPv6 CIDR block of a vSwitch. This route is used for communication within the vSwitch.

> **Note:** If you create a custom route table and associate the custom route table with a vSwitch for which IPv6 is enabled, you must add a custom route entry whose destination CIDR block is ::/0 and next hop is the IPv6 gateway instance. For more information, see Add a custom route.

**Routing rules**

If multiple route entries match the destination IP address, the route entry with the longest subnet mask is preferably used to determine the next hop. This ensures that the traffic is routed to the most precise destination. For example, the following table describes the route table of a VPC.

| Destination CIDR block | Next hop type | Next hop | Route entry type |
|---|---|---|---|
| 100.64.0.0/10 | - | - | System route |
| 192.168.0.0/24 | - | - | System route |
| 0.0.0.0/0 | Instance | i-12345678 | Custom route |
| 10.0.0.0/24 | Instance | i-87654321 | Custom route |

| 100.64.0.0/10 |   | and | 192.168.0.0/24 |   | are sy |
|---|---|---|---|---|---|

route entries. The route entries that are destined for `0.0.0.0/0` and `10.0.0.0/24` are

|   | 0.0.0.0/0 |   |
|---|---|---|
| 10.0.0.0/24 |   |   |

|   | i-12345678 |   |
|---|---|---|
| 87654321 |   |   |

|   | 10.0.0.1 |
|---|---|
| 10.0.1.1 |   |

`87654321` . Based on the preceding rule, traffic destined for `10.0.0.1` is routed to the ECS instance `i-87654321` , whereas traffic destined for `10.0.1.1` is routed to the ECS instance

| i-12345678 |   |   |
|---|---|---|
|   |   | . |

**Examples**

You can add custom route entries to a route table to control inbound and outbound traffic that is transmitted over the VPC. Routing within a VPC The following figure shows a NAT gateway that is deployed on an ECS instance (ECS01) in a VPC. To enable the cloud resources in the VPC to access the Internet through the ECS instance, you must add the following route entry to the route table.

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 0.0.0.0/0 | ECS instance | ECS01 |

Connect two VPCs by using Express Connect The following figure shows that VPC1 (172.16.0.0/12) is connected to VPC2 (192.168.0.0/16) through Express Connect. After you create router interfaces, you must add the following route entries to the VPCs: Add the following route entry to VPC1

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Router interface (to VPC) | VPC2 |

Add the following route entry to VPC2

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | Router interface (to VPC) | VPC1 |

Connect two VPCs through a VPN gateway The following figure shows that VPC1 (172.16.0.0/12) is connected to VPC2 (10.0.0.0/8) through a VPN gateway. After you configure the VPN gateway, you must add the following route entries to the VPCs. Add the following route entry to VPC1

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 10.0.0.0/8 | VPN gateway | VPN gateway1 |

Add the following route entry to VPC2

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | VPN gateway | VPN gateway2 |

Connect a VPC to a data center through Express Connect The following figure shows that a VPC is connected to an on-premises network through Express Connect. After you configure a connection over an Express Connect circuit and a VBR, you must add the following route entries: Add the following route entry to the VPC

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Router interface (general routing) | Router interface RI1 |

Add the following route entries to the VBR

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Express Connect circuit | Router interface RI3 |
| 172.16.0.0/12 | VPC | Router interface RI2 |

Add the following route entry to the on-premises network

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | - | On-premises gateway device |

Connect a VPC to a data center through a VPN gateway The following figure shows that a VPC (172.16.0.0/12) is connected to a data center (192.168.0.0/16) through a VPN gateway. After you configure the VPN gateway, you must add the following route entry to the VPC.

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | VPN gateway | The VPN gateway that you created |

### 5.2 Create a custom route table

This topic describes how to work with custom route tables. A route table consists of route entries. Each route entry specifies the destination to which network traffic is routed. You can create a custom route table to manage the inbound and outbound network traffic of subnets in a virtual private cloud (VPC).

**Create a custom route table**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region where you want to create the route table.
4. On the **Route Tables** page, click **Create Route Table**.
5. In the **Create Route Table** panel, configure the route table as described in the following
table and click **OK**.

| Parameter | Description |
|---|---|
| VPC | Select the VPC to which the route table belongs. |
| Name | Enter a name for the route table. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). The name must start with a letter. _ |
| Description | Enter a description for the route table. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . |

After you create a custom route table, you can go to the **Route Tables** page to view the route table. The type of route table is displayed as **Custom** in the **Route Table Type** column.

**Disassociate a route table from a vSwitch**

You can disassociate a custom route table from a vSwitch. After a custom route table is disassociated from a vSwitch, the vSwitch is automatically associated with the system route table.
1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the **Route Tables** page, find the route table that you want to manage and click its ID.
5. In the **Route Table Details** section, click the **Associated vSwitch** tab. Find the vSwitch
that you want to manage and click **Unbind** in the **Actions** column.
6. In the **Unbind Route Table** message, click **OK**.

**Delete a custom route table**

You can delete custom route tables. However, you cannot delete system route tables. If the custom route table that you want to delete is associated with a vSwitch, you must first disassociate the custom route table from the vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the **Route Tables** page, find the route table that you want to delete and click **Delete** in
the **Actions** column.
5. In the **Delete Route Table** message, click **OK**.

### 5.3 Add a custom route

This topic describes how to add a custom route. After you create a virtual private cloud (VPC), the system creates a system route table and adds system routes to the route table. The system routes are used to route traffic within the VPC. You cannot create or delete system routes. However, you can create custom routes to route traffic destined for specified CIDR blocks to specified destinations.

**Background information**

Each item in a route table is a route. A route consists of the destination CIDR block, next hop type, and next hop. A route specifies the destination of network traffic. Routes include system routes and custom routes. You can add custom routes to the system route table and custom route tables.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region to which the route table that you want to
manage belongs.
4. On the **Route Tables** page, find the route table and click **Management** in the **Operation**
column.
5. On the **Routing entry list** tab, click **Add route entry**.
6. In the **Add route entry** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|

| Target network segment | Enter a destination CIDR block for the route. IPv4 network segment: The destination CIDR block is an IPv4 CIDR block. IPv6 network segment: The destination CIDR block is an IPv6 CIDR block. |
|---|---|
| Next hop type | Select the next hop type. Valid values: ECS instance: Traffic destined for the specified CIDR block is routed to the specified ECS instance. Select this type if you want to route traffic to a specified ECS instance for centralized traffic forwarding and management. For example, you can configure an ECS instance as the Internet-facing gateway to route traffic from other ECS instances to the Internet. Highly available virtual IP: Traffic destined for the specified CIDR block is routed to the high-availability virtual IP address (HAVIP) that you select. VPN gateway: Traffic destined for the specified CIDR block is routed to the specified VPN gateway. NAT Gateway: Traffic destined for the specified CIDR block is routed to the specified NAT gateway. Auxiliary ENI: Traffic destined for the specified CIDR block is routed to the specified secondary elastic network interface (ENI). Router Interface (VPC Direction): Traffic destined for the specified CIDR block is routed to the VPC that you select. Select this type if you want to connect VPCs through Express Connect circuits. Router Interface (Border Router Direction): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a virtual border router (VBR). Select this type if you want to connect the VPC to a data center through Express Connect circuits. If you select Router Interface (Border Router Direction), you must also select a routing mode: Common route: Select an associated router interface. Primary/standby Route: Select two instances as the next hops. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes over when the active route fails to pass the health check. Load routing: Select two to four router interfaces as the next hops. The peer router of each router interface must be a VBR. You can set the weight of each instance to an integer from 1 to 255. The default value is 100. The weights of the instances must be the same. This way, traffic can be evenly distributed to the next-hop instances. Note If you set Target network segment to IPv6 network segment, you can select Router Interface (Border Router Direction) for Next hop type. |

| ECS Instance/VPN gateway/NAT Gateway/Auxiliary ENI/Highly available virtual IP/Router Interface (VPC Direction)/Router Interface (Border Router Direction) | Select an instance as the next hop. |
|---|---|

### 5.4 Export route entries

This topic describes how to export route entries from a route table for backup.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the **Route Tables** page, find the route table and click **Manage** in the **Actions** column.
5. In the **Route Table Details** section, click the **Route Entry List** tab, and then click **Export**.
The route entries are exported to a .csv file in your local computer.

### 5.5 Modify the information about a route table

**a route table**

This topic describes how to modify the name and description of a route table.

**Procedure**

1. Log on to the VPC console.
2. 3. 4.
5. In the **Routing table Basic information** section, click
next to **Routing table name**. In the dialog box that appears, enter a new name for the route table and click **OK**.
6. In the **Routing table Basic information** section, click
next to **Description**. In the dialog box that appears, enter a new description for the route table and click **OK**.

### 5.6 Delete a custom route

A route table consists of routes. Each route specifies the destination to which network traffic is routed. You can delete custom routes. However, you cannot delete system routes.

**Procedure**

1. Log on to the VPC console.
2. 3. 4.
5. On the **Route Entry List** tab, find the custom route that you want to delete and click
**Delete** in the **Actions** column.
6. In the **Delete Route Entry** message, click **OK**.

### 5.7 Add subnet routes to a route table

**table**

You can create a custom route table for a virtual private cloud (VPC) and add subnet routes to the custom route table. Then, you can associate the custom route table with a vSwitch to manage the traffic of the vSwitch. This facilitates network management.

**Prerequisites**

A VPC is created. For more information, see Create a VPC.

**Step 1: Create a custom route table**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region where you want to create the route table.
4. On the **Route Tables** page, click **Create Route Table**.
5. In the **Create Route Table** panel, configure the route table as described in the following
table and click **OK**.

| Parameter | Description |
|---|---|
| VPC | Select the VPC to which the route table belongs. |
| Name | Enter a name for the route table. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). The name must start with a letter. _ |
| Description | Enter a description for the route table. The description must be 2 to 256 characters in length, and cannot start with http:// or https:// . |

After you create a custom route table, you can go to the **Route Tables** page to view the route table. The type of route table is displayed as **Custom** in the **Route Table Type** column.

**Step 2: Add subnet routes**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the **Route Tables** page, find the route table and click **Manage** in the **Actions** column.
5. In the **Route Table Details** section, click **Add Route Entry**.
6. In the **Add Route Entry** panel, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|

| Destination CIDR Block | Enter a destination CIDR block for the route entry. IPv4 CIDR Block: The destination CIDR block is an IPv4 CIDR block. IPv6 CIDR Block: The destination CIDR block is an IPv6 CIDR block. |
|---|---|
| Next Hop Type | Select the next hop type. Valid values: ECS Instance: Traffic destined for the specified CIDR block is routed to the specified Elastic Compute Service (ECS) instance. Select this type if you want to route traffic to an ECS instance for centralized traffic forwarding and management. For example, you can configure an ECS instance as the Internet-facing gateway to route traffic from other ECS instances to the Internet. HaVip: Traffic destined for the specified CIDR block is routed to the high-availability virtual IP address (HAVIP) that you select. VPN Gateway: Traffic destined for the specified CIDR block is routed to the specified VPN gateway. NAT Gateway: Traffic destined for the specified CIDR block is routed to the specified NAT gateway. Secondary ENI: Traffic destined for the specified CIDR block is routed to the secondary elastic network interface (ENI) that you select. Router Interface (To VPC): Traffic destined for the specified CIDR block is routed to the VPC that you select. Select this type if you want to connect VPCs through Express Connect circuits. Router Interface (To VBR): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a virtual border router (VBR). Select this type if you want to connect the VPC to a data center through Express Connect circuits. If you select Router Interface (To VBR), you must also select a routing mode: General Routing: Select an associated router interface. Active/Standby Routing: Select two instances as the next hop. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes over when the active route fails to pass the health check. Load Balancing Routing: Select two to four router interfaces as the next hop. The peer router of each router interface must be a VBR. You can set the weight of each instance to an integer from 1 to 255. The default value is 100. The weights of the instances must be the same. This way, traffic can be evenly distributed to the next-hop instances. IPv6 Gateway: Traffic destined for the specified CIDR block is routed to the specified IPv6 gateway. Note If you set Destination CIDR Block to IPv6 CIDR Block, you can select IPv6 Gateway and Router Interface (To VBR) for Next Hop Type. |

| ECS Instance, VPN Gateway, NAT Gateway, Secondary ENI, HaVip, Router Interface (To VPC), Router Interface (To VBR), IPv6 Gateway | Select an instance as the next hop. |
|---|---|

**Step 3: Associate the custom route table with a vSwitch**

You can associate the custom route table with a vSwitch to manage the routes of the vSwitch. A vSwitch can be associated only with one system route table or one custom route table. Perform the following operations to associate the custom route table with a vSwitch:
1. Log on to the VPC console.
2. In the left-side navigation pane, click **Route Tables**.
3. In the top navigation bar, select the region to which the route table that you want to
manage belongs.
4. On the **Route Tables** page, find the custom route table that you want to manage and click
its ID.
5. In the **Route Table Details** section, click the **Associated vSwitch** tab and click
**Associate vSwitch**.
6. In the **Associate vSwitch** panel, select the vSwitch that you want to associate and click
**OK**.

## 6 HAVIPs

### 6.1 Overview

High-availability virtual IP addresses (HAVIPs) are private IP addresses that can be created and released as independent resources. You can use HAVIPs with high-availability software such as Keepalived to provide active/standby services. This improves the availability of your services.

**Features**

Each Elastic Compute Service (ECS) instance is assigned a private IP address as the primary IP address. You can associate HAVIPs with an ECS instance to increase the number of private IP addresses available for the ECS instance. Both the primary IP address and HAVIPs of an ECS instance can be used to access networks. In addition, you can use HAVIPs with HA software such as Keepalived to provide active/standby services. This improves the availability of your services. You can associate an HAVIP with ECS instances by using the following methods: Directly associate an HAVIP with ECS instances. An HAVIP can be associated with three ECS instances. Then, the three ECS instances can announce the HAVIP by using Address Resolution Protocol (ARP). After the HAVIP is announced, one ECS instance serves as the primary instance and the other two serve as secondary instances. If the primary ECS instance is down, a secondary ECS instance takes over to provide services. Attach secondary elastic network interfaces (ENIs) to ECS instances. Then, associate the HAVIP with the secondary ENIs. An HAVIP can be associated with the secondary ENIs of three ECS instances. Then, the three ECS instances can announce the HAVIP by using ARP. After the HAVIP is announced, one ECS instance serves as the primary instance and the other two serve as secondary instances. If the primary ECS instance is down, a secondary ECS instance takes over to provide services.

> **Note:** Before you associate the HAVIP with secondary ENIs, make sure that each secondary ENI is associated with an ECS instance.

HAVIPs provide the following features: HAVIPs are floating private IP addresses and are not statically assigned to specified ECS instances. HAVIPs can be associated with or disassociated from ECS instances through ARP announcements. An HAVIP can be associated only with ECS instances or ENIs that belong to the same vSwitch. An HAVIP can be associated with three ECS instances or three secondary ENIs. However, an HAVIP cannot be associated with ECS instances and secondary ENIs at the same time.

**Scenarios**

HAVIPs support flexible configurations in the following scenarios: Scenario 1: Internal-facing HA services In the following figure, two ECS instances are associated with the same HAVIP. Keepalived is configured for the ECS instances to provide an internal-facing HA service. Other instances in the same virtual private cloud (VPC) can access the service. The HAVIP serves as the service address. If the primary ECS instance is down, the secondary ECS instance takes over. This improves the availability of the service. Scenario 2: Internet-facing HA services In the following figure, two ECS instances are associated with the same HAVIP. Keepalived is configured and the HAVIP is associated with an elastic IP address (EIP) for the ECS instances to provide an Internet-facing HA service. The EIP that is associated with the HAVIP serves as the service address. If the primary ECS instance is down, the secondary ECS instance takes over. This improves the availability of the service.

**Limits**

Before you use HAVIPs, take note of the following limits.

| Item | Default value |
|---|---|
| Maximum number of HAVIPs that can be created in each VPC | 5 |
| Maximum number of HAVIPs that can be associated with each ECS instance | 5 |
| Maximum number of HAVIPs that can be associated with each ENI | 5 |
| Maximum number of ECS instances that can be associated with each HAVIP | 3 |
| Maximum number of ENIs that can be associated with each HAVIP | 3 |

| Maximum number of route entries that point to an HAVIP in each VPC | 5 |
|---|---|
| Whether HAVIPs support broadcasting or multicasting | Unsupported Note HAVIPs support only unicasting. To implement high availability through third- party software such as keepalived, you must modify the configuration file to change the communication method to unicasting. |

### 6.2 Create an HAVIP

A high-availability virtual IP address (HAVIP) is a private IP address that can be created and released as an independent resource. This topic describes how to create an HAVIP in the console.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created. For more information, see Create and manage a VPC and Create and manage a vSwitch.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region where you want to create the HAVIP.
4. On the **HaVip** page, click **Create HaVip**.
5. On the **Create HaVip** page, set the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Organization | Select the organization to which the HAVIP belongs. |
| Resource Set | Select the resource set to which the HAVIP belongs. |
| Region | Select the region where you want to create the HAVIP. |
| VPC | Select the VPC to which the HAVIP belongs. |
| vSwitch | Select the vSwitch to which the HAVIP belongs. |
| Private IP Address | Specify a private IP address for the HAVIP. Note You must specify an idle private IP address that falls within the CIDR block of the vSwitch. |

### 6.3 Associate HAVIPs with backend cloud resources

**backend cloud resources**

#### 6.3.1 Associates an HAVIP with an ECS instance

**instance**

You can associate a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). This way, the ECS instance can announce the HAVIP and obtain multiple private IP addresses through Address Resolution Protocol (ARP). Each HAVIP can be associated with at most three ECS instances.

**Prerequisites**

An ECS instance is created. For more information, see the **Create an instance** section of
**Quick Start** in **ECS User Guide**.

**Background information**

An HAVIP can be associated with three ECS instances or three elastic network interfaces (ENIs). However, an HAVIP cannot be associated with ECS instances and ENIs at the same time.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region of the HAVIP.
4. On the **High-availability Virtual IP Address** page, find the HAVIP that you want to
manage and click **Manage** in the **Actions** column.
5. In the **Associate with Resource** section, find **ENI (Primary)** or **ENI (Secondary)**, and
then click **Associate Now**.
6. In the dialog box that appears, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Binding type | Select the type of resource with which you want to associate the HAVIP. Supported resource types: ECS Instance ENI In this example, ECS Instance is selected. |
| Associate with Resource | Select the ECS instance with which you want to associate the HAVIP. The ECS instance must meet the following requirements: The ECS instance is deployed in a VPC. The ECS instance and the HAVIP belong to the same vSwitch. |

#### 6.3.2 Associate an HAVIP with an ENI

You can associate a high-availability virtual IP address (HAVIP) with an elastic network interface (ENI). This way, an Elastic Compute Service (ECS) instance can advertise the HAVIP and obtain multiple private IP addresses through Address Resolution Protocol (ARP).

**Prerequisites**

An ENI is created. For more information, see the **Create an ENI** section of **Elastic Network**
**Interface** in **ECS User Guide**.

**Background information**

An HAVIP can be associated with three ECS instances or three ENIs. However, an HAVIP cannot be associated with ECS instances and ENIs at the same time.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region of the HAVIP.
4. On the **High-availability Virtual IP Address** page, find the HAVIP that you want to
manage and click **Manage** in the **Actions** column.
5. In the **Associate with Resource** section, find **ENI (Primary)** or **ENI (Secondary)**, and
then click **Associate Now**.
6. In the dialog box that appears, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Binding type | Select the type of resource with which you want to associate the HAVIP. Supported resource types: ECS Instance ENI In this example, ENI is selected. |
| Associate with Resource | Select the ENI with which you want to associate the HAVIP. The ENI and HAVIP must belong to the same vSwitch. |

### 6.4 Associate an HAVIP with an EIP

**EIP**

You can associate a high-availability virtual IP address (HAVIP) with an elastic IP address (EIP). This way, the HAVIP can provide services over the Internet by using the EIP.

**Prerequisites**

An EIP is created. For more information, see the **Create an EIP** topic in **Quick start** of
**Elastic IP Address User Guide**.
1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the **High-availability Virtual IP Address** page, find the HAVIP and click **Bind elastic**
**public network IP** in the **Actions** column.
5. In the dialog box that appears, select the EIP with which you want to associate the HAVIP
and click **OK**. The EIP must meet the following requirements: The EIP and the HAVIP must be deployed in the same region. The EIP must be in the Available state.

### 6.5 Disassociate HAVIPs from backend cloud resources

**backend cloud resources**

#### 6.5.1 Disassociate an HAVIP from an ECS instance

**instance**

This topic describes how to disassociate a high-availability virtual private IP address (HAVIP) from an Elastic Compute Service (ECS) instance. After you disassociate an HAVIP from an ECS instance, the ECS instance cannot send Address Resolution Protocol (ARP) messages to advertise the HAVIP.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the **HaVip** page, find the HAVIP that you want to manage and click **Manage** in the
**Actions** column.
5. In the **Resources** section, find the ECS instance that you want to manage and click
**Unbind**.
6. In the message that appears, click **OK**.

#### 6.5.2 Disassociate an HAVIP from an ENI

This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic network interface (ENI). After you disassociate an HAVIP from an ENI, the Elastic Compute Service (ECS) instance with which the ENI is associated cannot send Address Resolution Protocol (ARP) messages to advertise the HAVIP.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the **HaVip** page, find the HAVIP that you want to disassociate and click **Manage** in the
**Actions** column.
5. In the **Resources** section, find the ENI that you want to manage and click **Unbind**.
6. In the message that appears, click **OK**.

### 6.6 Disassociate an HAVIP from an EIP

**EIP**

This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic IP address (EIP). After you disassociate an HAVIP from an EIP, the HAVIP can no longer provide services over the Internet.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **High-availability Virtual IP Address**.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the **High-availability Virtual IP Address** page, find the HAVIP and click **Unbind EIP**
in the **Operation** column.
5. In the message that appears, click **OK**.

### 6.7 Delete an HAVIP

This topic describes how to delete a high-availability virtual IP address (HAVIP).

**Prerequisites**

If an HAVIP is associated with an elastic IP address (EIP), you must disassociate the HAVIP from the EIP before you delete the HAVIP. For more information, see Disassociate an HAVIP from an EIP. The HAVIP is not associated with an Elastic Compute Service (ECS) instance. If the HAVIP is associated with an ECS instance, disassociate the HAVIP from the ECS instance first. For more information, see Disassociate an HAVIP from an ECS instance. The HAVIP is not associated with an elastic network interface (ENI). If the HAVIP is associated with an ENI, disassociate the HAVIP from the ENI first. For more information, see Associate an HAVIP with an ENI.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **HaVip**.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the **HaVip** page, find the HAVIP that you want to delete and click **Delete** in the **Actions**
column.
5. In the message that appears, click **OK**.

## 7 Network ACLs

### 7.1 Overview

Network access control lists (ACLs) allow you to regulate access control for a virtual private cloud (VPC). You can create network ACL rules and associate a network ACL with a vSwitch. This allows you to control inbound and outbound traffic of Elastic Compute Service (ECS) instances that are associated with the vSwitch.

**Features**

Network ACLs have the following features: A network ACL is used to filter inbound and outbound network traffic of ECS instances that are associated with a vSwitch in a VPC. The network traffic forwarded to ECS instances by Server Load Balancer (SLB) instances is also filtered. Network ACLs are stateless. You must set both inbound and outbound rules. Otherwise, the system may fail to respond to requests. If you create a network ACL that does not contain a rule, all inbound and outbound access is denied. If a network ACL is associated with a vSwitch, the network ACL does not filter the traffic forwarded between ECS instances that are associated with the vSwitch.

**Network ACL rules**

You can add rules to or delete rules from a network ACL. Changes to the rules are automatically synchronized to the associated vSwitch. By default, an inbound rule and an outbound rule are automatically added to a newly created network ACL. These rules allow all inbound and outbound network traffic transmitted through the associated vSwitch. You can delete the default rules. The following table lists the default inbound and outbound rules. Default inbound rule

| Priority | Protocol type | Source CIDR block | Source port range | Action | Type |
|---|---|---|---|---|---|
| 1 | all | 0.0.0.0/0 | -1/-1 | Allow | Custom |

Default outbound rule

| Priority | Protocol type | Destination CIDR block | Destination port range | Action | Type |
|---|---|---|---|---|---|
| 1 | all | 0.0.0.0/0 | -1/-1 | Allow | Custom |

A network ACL contains the following parameters: Priority: A smaller value indicates a higher priority. The system attempts to match requests against rules in descending order of priority. Rule 1 has the highest priority. If a request matches a rule, the system applies the rule to the request and ignores the other rules. For example, the following rules are added and requests destined for IP address 172.16.0.1 are sent from an ECS instance. In the following table, the requests match Rules 2 and 3. Rule 2 has a higher priority than Rule 3. Therefore, the system applies Rule 2. Based on the action of Rule 2, the requests are denied.

| Priority | Protocol type | Destination CIDR block | Destination port range | Action | Type |
|---|---|---|---|---|---|

| 1 | all | 10.0.0.0/8 | -1/-1 | Allow | Custom |
|---|---|---|---|---|---|
| 2 | all | 172.16.0.0/1 2 | -1/-1 | Deny | Custom |
| 3 | all | 172.16.0.0/1 2 | -1/-1 | Allow | Custom |

Policy: specifies whether to allow or deny specific traffic. Protocol: the protocol type. Available options include All, ICMP, GRE, TCP, and UDP. Source CIDR block: the source CIDR block from which inbound traffic is transmitted. Destination IP address: the destination IP addresses to which outbound traffic is transmitted. Destination port range: the range of destination ports to which the inbound rule applies. Destination port range: the range of destination ports to which the outbound rule applies.

**Comparison between network ACLs and security groups**

Network ACLs control data transmitted through associated vSwitches while security groups control data transmitted through associated ECS instances. The following table describes the differences between network ACLs and security groups.

| Network ACL | Security group |
|---|---|
| Applies to vSwitches. | Applied to instances. |
| Stateless: Returned traffic must be allowed by inbound rules. | Stateful: Returned traffic is automatically allowed and not affected by rules. |
| The system attempts to match requests against rules in descending order of priority. Not all rules are matched. | The system matches a request against all rules before a rule is applied. |
| Each vSwitch can be associated only with one network ACL. | Each ECS instance can be added to more than one security group. |

The following figure shows how network ACLs and security groups are applied to ensure network security.

**Limits**

The following table describes the limits on network ACLs.

| Item | Limit |
|---|---|
| Maximum number of network ACLs that can be created in each VPC | 200 |
| Maximum number of network ACLs that can be associated with a vSwitch | 1 |
| Maximum number of rules that can be added to a network ACL | Inbound rules: 20 Outbound rules: 20 |

The following flowchart shows how to use a network ACL.

### 7.2 Scenarios

If you are familiar with the ports that are commonly used by ECS instances, you can specify them in access control list (ACL) rules to facilitate precise network traffic filtering. This topic describes the ports that are commonly used by ECS instances and the application scenarios of these ports.

**Ports**

The following table lists the ports and the services that use these ports.

| Port | Service | Description |
|---|---|---|
| 21 | FTP | The FTP port. It is used to upload and download files. |
| 22 | SSH | The SSH port. It is used to log on to Linux instances in the command line method by using username and password pairs. |
| 23 | Telnet | The Telnet port. It is used to remotely log on to ECS instances. |
| 25 | SMTP | The SMTP port. It is used to send emails. |
| 80 | HTTP | The HTTP port. It is used to access services such as IIS, Apache, and NGINX. |
| 110 | POP3 | The POP3 port. It is used to send and receive emails. |
| 143 | IMAP | The Internet Message Access Protocol (IMAP) port. It is used to receive emails. |
| 443 | HTTPS | The HTTPS port. It is used to access services. The HTTPS protocol can implement encrypted and secure data transmission. |
| 1433 | SQL Server | The TCP port of SQL Server. It is used for SQL Server to provide external services. |
| 1434 | SQL Server | The UDP port of SQL Server. It is used to return the TCP/IP port occupied by SQL Server. |
| 1521 | Oracle | The Oracle communication port. ECS instances that run Oracle SQL must have this port open. |
| 3306 | MySQL | The MySQL port. It is used for MySQL databases to provide external services. |
| 3389 | Windows Server Remote Desktop Services | The Windows Server Remote Desktop Services port. It is used to log on to a Windows instance. |

| 8080 | Proxy port | An alternative to port 80. It is commonly used for WWW proxy services. |
|---|---|---|

**Custom network ACLs**

Inbound rules and Outbound rules describe a network ACL example for VPCs that support IPv4 addresses only. The inbound rules in effective order 1, 2, 3, and 4 respectively allow HTTP, HTTPS, SSH, and RDP traffic to the vSwitch. Outbound response rules are those in effective order 3. The outbound rules in effective order 1 and 2 respectively allow HTTP and HTTPS traffic from the vSwitch. Outbound response rules are those in effective order 5. The inbound rule in effective order 6 denies all inbound IPv4 traffic. This rule ensures that packets that do not match any other rules are denied. The outbound rule in effective order 4 denies all outbound IPv4 traffic. This rule ensures that packets that do not match any other rules are denied.

> **Note:** An inbound or outbound rule must correspond to an inbound or outbound rule that allows response traffic.

Table 1. Inbound rules

| Effecti ve order | Protoc ol | Source IP addres ses | Destin ation port range | Action | Description |
|---|---|---|---|---|---|
| 1 | TCP | 0.0.0.0/ 0 | 80/80 | Accept | Allows inbound HTTP traffic from any IPv4 addresses. |
| 2 | TCP | 0.0.0.0/ 0 | 443/44 3 | Accept | Allows inbound HTTPS traffic from any IPv4 addresses. |
| 3 | TCP | 0.0.0.0/ 0 | 22/22 | Accept | Allows inbound SSH traffic from any IPv4 addresses. |
| 4 | TCP | 0.0.0.0/ 0 | 3389/3 389 | Accept | Allows inbound RDP traffic from any IPv4 addresses. |
| 5 | TCP | 0.0.0.0/ 0 | 32768/ 65535 | Accept | Allows inbound IPv4 traffic from the Internet. This port range is for reference only. For more information on how to select appropriate ephemeral ports, see Ephemeral ports. |
| 6 | All | 0.0.0.0/ 0 | -1/-1 | Drop | Denies all inbound IPv4 traffic. |

Table 2. Outbound rules

| Effecti ve order | Protoc ol | Destin ation IP addres ses | Destin ation port range | Action | Description |
|---|---|---|---|---|---|

| 1 | TCP | 0.0.0.0/ 0 | 80/80 | Accept | Allows outbound IPv4 HTTP traffic from the vSwitch to the Internet. |
|---|---|---|---|---|---|
| 2 | TCP | 0.0.0.0/ 0 | 443/44 3 | Accept | Allows outbound IPv4 HTTPS traffic from the vSwitch to the Internet. |
| 3 | TCP | 0.0.0.0/ 0 | 32768/ 65535 | Accept | Allows outbound IPv4 traffic from the vSwitch to the Internet. This port range is for reference only. For more information on how to select appropriate ephemeral ports, see Ephemeral ports. |
| 4 | All | 0.0.0.0/ 0 | -1/-1 | Drop | Denies all outbound IPv4 traffic. |

**Network ACLs for SLB**

If the ECS instance in the vSwitch acts as the backend server of an SLB instance, you must add the following network ACL rules. Inbound rules

| Effecti ve order | Protoc ol | Source IP addres ses | Destin ation port range | Action | Description |
|---|---|---|---|---|---|
| 1 | SLB listener protoco l | Client IP address es allowed to access the SLB instanc e | SLB listener port | Accept | Allows inbound traffic from specified client IP addresses. |
| 2 | Health check protoco l | 100.64. 0.0/10 | Health check port | Accept | Allows inbound traffic from health check IP addresses. |

Outbound rules

| Effecti ve order | Protoc ol | Destin ation IP addres ses | Destin ation port range | Action | Description |
|---|---|---|---|---|---|

| 1 | All | Client IP address es allowed to access the SLB instanc e | -1/-1 | Accept | Allows all outbound traffic to specified client IP addresses. |
|---|---|---|---|---|---|
| 2 | All | 100.64. 0.0/10 | -1/-1 | Accept | Allows outbound traffic to health check IP addresses. |

**Ephemeral ports**

Clients use different ports to initiate requests. You can select different port ranges for network ACL rules based on the client type. The following table lists ephemeral port ranges for common clients.

| Client | Port range |
|---|---|
| Linux | 32768/61000 |
| Windows Server 2003 | 1025/5000 |
| Windows Server 2008 and later | 49152/65535 |
| NAT gateway | 1024/65535 |

### 7.3 Create a network ACL

A network access control list (ACL) allows you to manage network access in a virtual private cloud (VPC). You can create network ACLs in the VPC console.

**Prerequisites**

A VPC is created. For more information, see Create a VPC.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACL**.
3. In the top navigation bar, select the region where you want to create the network ACL.
4. On the **Network ACL** page, click **Create Network ACL**.
5. In the **Create Network ACL** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Organization | Select the organization to which the network ACL belongs. |
| Resource Set | Select the resource set to which the network ACL belongs. |
| Region | Select the region where you want to deploy the network ACL. |

| Name | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter. _ |
|---|---|
| Description | Enter a description for the network ACL. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), colons (:), and hyphens (-). The name must start with a letter _ and cannot start with http:// or https:// . |
| VPC | Select the VPC for which you want to create the network ACL. Note The VPC and network ACL must be deployed in the same region. |

**What to do next**

### 7.4 Associate a network ACL with a vSwitch

**a vSwitch**

After you create a network access control list (ACL), you can associate it with a vSwitch. This way, you can use the network ACL to control the traffic that flows through the Elastic Compute Service (ECS) instances that are connected to the vSwitch.

**Prerequisites**

Before you associate a network ACL with a vSwitch, make sure that the following requirements are met: A network ACL is created. For more information, see Create a network ACL. A vSwitch is created. The vSwitch and network ACL must belong to the same VPC. For more information, see Create a VSwitch.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACLs**.
3. In the top navigation bar, select the region to which the network ACK that you want to
manage belongs.
4. On the **Network ACLs** page, find the network ACL that you want to manage and click
**Management** in the **Operation** column.
5. On the **Bound resource** tab, click **Associated resources**.
6. In the **Associated resources** dialog box, select a vSwitch and click **OK**.

> **Note:** The network ACL and vSwitch must belong to the same VPC. A vSwitch can be associated only with one network ACL.

### 7.5 Add network ACL rules

#### 7.5.1 Add an inbound rule

After you create a network access control list (ACL), you can add inbound rules to the network ACL. You can use inbound rules to control whether Elastic Compute Service (ECS) instances in a vSwitch can be accessed over the Internet or private networks.

**Prerequisites**

A network ACL is created. For more information, see Create a network ACL.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACLs**.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the **Network ACLs** page, find the network ACL that you want to manage and click
**Inbound direction rule** in the **Operation** column.
5. On the **Inbound direction rule** tab, click **Create inbound rule**.
6. In the **Create inbound rule** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter a name for the inbound rule. The name must be 2 to 128 characters in length. It must start with a letter and can contain digits, underscores ( ), and hyphens (-). _ |
| Strategy | Select an action for the inbound rule. Valid values: Allow: accepts network traffic that is destined for the ECS instances connected to the vSwitch. Rejection: drops network traffic that is destined for the ECS instances connected to the vSwitch. |
| Protocol type | Select a transport layer protocol. Valid values: ALL: all protocols ICMP: Internet Control Message Protocol (ICMP) GRE: GRE TCP: Transmission Control Protocol (TCP) UDP: User Datagram Protocol (UDP) |
| Source address | The source CIDR block from which data is transmitted. Default value: 0.0.0.0/32. |
| Destination Port Range | Enter the destination port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the highest and lowest values in a port range, for example, 1/200 or 80/80. -1/-1 indicates that all ports are available. You cannot set the value to -1/-1. |

#### 7.5.2 Add an outbound rule

This topic describes how to add an outbound rule to a network access control list (ACL). You can use outbound rules to control how Elastic Compute Service (ECS) instances connected to a vSwitch access the Internet or other private networks.

**Prerequisites**

A network ACL is created. For more information, see Create a network ACL.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACLs**.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the **Network ACLs** page, find the network ACL that you want to manage and click **Out**
**direction rule** in the **Operation** column.
5. On the **Out direction rule** tab, click **Create out direction rules**.
6. In the **Create out direction rules** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter a name for the outbound rule. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter. _ |
| Strategy | Select an action for the outbound rule. Valid values: Allow: allows ECS instances connected to the vSwitch to access the Internet or other private networks. Rejection: forbids ECS instances connected to the vSwitch to access the Internet or other private networks. |
| Protocol type | Select a transport layer protocol. Valid values: ALL: all protocols ICMP: Internet Control Message Protocol (ICMP) GRE: Generic Routing Encapsulation (GRE) TCP: Transmission Control Protocol (TCP) UDP: User Datagram Protocol (UDP) |
| Destination address | The destination CIDR block to which data is transmitted. Default value: 0.0.0.0/32. |
| Destination port range | Enter the destination port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the highest and lowest values in a port range, for example, 1/200 or 80/80. -1/-1 indicates that all ports are available. Do not set the value to -1/-1. |

#### 7.5.3 Change the priorities of network ACL rules

**rules**

Network ACL rules take effect in descending order of priority. A smaller value indicates a higher priority. You can prioritize network ACL rules based on your business requirements.

**Change the priority of an inbound rule**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACLs**.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the **Network ACLs** page, find the network ACL that you want to manage and click
**Management** in the **Operation** column.
5. Click the **Inbound direction rule** tab and click **Sort**.
6. In the **Sort** dialog box, change the priority of the rule by dragging and dropping the rule.
Then, click **OK**.

> **Note:** Rules are listed in descending order of priority.

**Change the priority of an outbound rule**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACLs**.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the **Network ACLs** page, find the network ACL that you want to manage and click
**Management** in the **Actions** column.
5. Click the **Outbound direction rule** tab and click **Sort**.
6. In the **Sort** dialog box, change the priority of the rule by dragging and dropping the rule.
Then, click **OK**.

> **Note:** Rules are listed in descending order of priority.

### 7.6 Disassociate a network ACL from a vSwitch

**from a vSwitch**

You can disassociate a network ACL from a vSwitch. After the network ACL is disassociated from the vSwitch, the network ACL no longer controls traffic that flows through the Elastic Compute Service (ECS) instances connected to the vSwitch.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACLs**.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the **Network ACLs** page, find the network ACL that you want to manage and click
**Management** in the **Operation** column.
5. On the **Bound resource** tab, find the vSwitch and click **Unbind** in the **Operation** column.
6. In the message that appears, click **OK**.

### 7.7 Delete a network ACL

This topic describes how to delete a network access control list (ACL).

**Prerequisites**

Make sure that the network ACL is not associated with a vSwitch. If the network ACL is associated with a vSwitch, disassociate the network ACL from the vSwitch first. For more information, see Disassociate a network ACL from a vSwitch.

**Procedure**

1. Log on to the VPC console.
2. In the left-side navigation pane, click **Network ACL**.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the **Network ACL** page, find the network ACL that you want to delete and click **Delete**
in the **Actions** column.
5. In the **Delete Network ACL** message, click **OK**.
