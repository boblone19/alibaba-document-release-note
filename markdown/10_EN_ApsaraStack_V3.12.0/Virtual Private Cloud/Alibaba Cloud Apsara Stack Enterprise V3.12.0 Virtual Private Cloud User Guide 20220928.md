---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Virtual Private Cloud User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 44
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Virtual Private Cloud User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Virtual%20Private%20Cloud%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Virtual Private Cloud User Guide 20220928

## Table of Contents

- 1 What is a VPC?
- 2 Log on to the VPC console
- 3 Quick start
  - 3.1 Plan and design a VPC
  - 3.2 Create an IPv4 VPC
  - 3.3 Create an IPv6 VPC
- 4 VPCs and VSwitches
  - 4.1 Overview
  - 4.2 VPC management
    - 4.2.1 Create a VPC
    - 4.2.2 Modify the name and description of a VPC
    - 4.2.3 Delete a VPC
  - 4.3 VSwitch management
    - 4.3.1 Create a VSwitch
    - 4.3.2 Create cloud resources in a VSwitch
    - 4.3.3 Modify the name and description of a VSwitch
    - 4.3.4 Delete a VSwitch
- 5 Route tables
  - 5.1 Overview
  - 5.2 Add a custom route entry
  - 5.3 Export route entries
  - 5.4 Modify a route table
  - 5.5 Delete a custom route entry
- 6 HAVIPs
  - 6.1 Overview
  - 6.2 Create an HAVIP
  - 6.3 Associate an HAVIP with an ECS instance
  - 6.4 Associate an HAVIP with an EIP
  - 6.5 Disassociate an HAVIP from an ECS instance
  - 6.6 Disassociate an EIP from an HAVIP
  - 6.7 Delete an HAVIP

## 1 What is a VPC?

A virtual private cloud (VPC) is a private network dedicated for your use. You have full control over your VPC, which you can define and customize by specifying the Classless Inter-domain Routing (CIDR) block, configuring route tables, and creating gateways. You can launch Apsara Stack resources such as Elastic Compute Service (ECS) instances, ApsaraDB for RDS (RDS) instances, and Server Load Balancer (SLB) instances in your VPC. Furthermore, you can connect your VPC to other VPCs or on-premises networks to create a custom network environment. In this way, you can smoothly migrate applications and extend on-premises data centers to the cloud. Components Each VPC consists of one VRouter, at least one private CIDR block, and one or more VSwitches. Private CIDR block When you create a VPC or a VSwitch, you must specify its private IP address range in the form of a CIDR block. You can use the standard private CIDR blocks listed in the following table and their subsets as CIDR blocks for your VPCs. For more information, see the Plan and design a VPC section in this User Guide.

| CIDR block | Number of available private IP addresses (excluding those reserved by the system) |
|---|---|
| 192.168.0.0/16 | 65,532 |
| 172.16.0.0/12 | 1,048,572 |
| 10.0.0.0/8 | 16,777,212 |

VRouter A VRouter is a hub that connects all VSwitches in a VPC and serves as a gateway between the VPC and other networks. After a VPC is created, a VRouter is automatically created for the VPC. Each VRouter is associated with a route table. For more information, see the Route table overview section in this User Guide. VSwitch A VSwitch is a basic network component that connects different cloud resources in a VPC. After you create a VPC, you can create VSwitches to partition your VPC into multiple subnets. VSwitches within a VPC can communicate with each other over the private network. You can deploy your applications in VSwitches that belong to different zones to improve service availability. For more information, see the Create a VSwitch sectionin this User Guide. le

## 2 Log on to the VPC console

This topic provides an example of how to log on to the Virtual Private Cloud console by using Google Chrome. Prerequisites Before logging on to the ASCM console, make sure that you have obtained the IP address or domain name of the ASCM console from the deployment personnel. The URL used to access the ASCM console is in the following format: https://[IP address or domain name of the ASCM console]. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL used to access the ASCM console. Press the Enter key.
2. Enter your username and password.
Obtain the username and password for logging on to the console from the operations administrator. Not e When you log on to the ASCM console for the first time, you must change the password of your username as prompted. Due to security concerns, your password must meet the minimum complexity requirements: The password must be 8 to 20 characters in length and must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).
3. Click Login to go to the ASCM console homepage.
4. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.

## 3 Quick start

### 3.1 Plan and design a VPC

Before you create virtual private clouds (VPCs) and VSwitches, you need to plan the quantity and Classless Inter-domain Routing (CIDR) blocks of VPCs and VSwitches. How many VPCs are required? How many VSwitches are required? How do I specify CIDR blocks? How do I specify CIDR blocks if I want to connect a VPC to other VPCs or on-premises data centers? How many VPCs are required? One VPC We recommend that you create one VPC if you do not need to deploy systems in multiple regions or separate VPCs. Multiple VPCs We recommend that you create multiple VPCs if you need to: Deploy application systems across regions. A VPC cannot be deployed across regions. If you want to deploy your application systems in different regions, you must create multiple VPCs. You can use Express Connect and VPN Gateway to connect VPCs. Separate IT systems To separate IT systems, you must create multiple VPCs. The following figure shows an example of isolating a production environment from a test environment by deploying them in separate VPCs. How many VSwitches are required? We recommend that you create at least two VSwitches for each VPC and deploy these VSwitches in different zones to achieve zone-disaster recovery. After you deploy your applications in different zones within a region, you must measure the network latency between these applications. This is because the cross-zone network latency may be higher than expected due to complex data processing or cross-zone calls. An ideal approach is to optimize and adjust your systems to strike a balance between availability and latency. In addition, the sizes and designs of your IT systems must also be taken into consideration when you create VSwitches. If you allow traffic from the Internet to be routed to and from the frontend systems, you can deploy the front-end systems in different VSwitches and the backend systems in other VSwitches to create a robust disaster recovery strategy. How do I specify CIDR blocks? When you create VPCs and VSwitches, you must specify their private IP address ranges in the form of CIDR blocks. VPC CIDR blocks You can use 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or their subsets as the CIDR blocks of your VPCs. To specify CIDR blocks for VPCs, follow these rules: If you have only one VPC and this VPC does not need to communicate with any on-premises data center, you can use one of the preceding CIDR blocks or one of their subsets as the CIDR block of the VPC. If you have multiple VPCs, or you need to build a hybrid cloud to integrate VPCs and on-premises data centers, we recommend that you use the subsets of the preceding CIDR blocks for your VPCs. In this case, the mask cannot be longer than 16 bits. VSwitch CIDR blocks The CIDR block of a VSwitch must be a subset of the CIDR block of the VPC this VSwitch resides in. For example, if the CIDR block of a VPC is 192.168.0.0/16, the CIDR block of a VSwitch in the VPC must be a segment from 192.168.0.0/17 to 192.168.0.0/29. To specify CIDR blocks for VSwitches, follow these rules: The CIDR block size for a VSwitch is between a 16-bit mask and a 29-bit mask. It means that 8 to 65,536 IP addresses can be provided. This range is set because a 16-bit host address space provides addressing for 65,534 ECS instances, which can meet your needs in most cases, while a mask smaller than 29 bits can only allow very few usable host addresses. The first and the last three IP addresses in each VSwitch CIDR block are reserved by the system. For example, if the CIDR block of a VSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. You must check the number of ECS instances in the VSwitch before you specify the CIDR block of a VSwitch. How do I specify CIDR blocks if I want to connect a VPC to other VPCs or on-premises data centers? Before you connect your VPC to another VPC or an on-premises data center, you must make sure that the CIDR block of your VPC does not conflict with that of the peer network. For example, assume you have three VPCs: VPC1 in China (Hangzhou), VPC2 in China (Beijing), and VPC3 in China (Shenzhen), as shown in the following figure. Express Connect circuit is used for VPC1 and VPC2 to communicate with each other. VPC3 does not communicate with other VPCs, but may need to communicate with VPC2 in the future. Additionally, you have an on-premises data center in Shanghai, and you need to connect it to VPC1 by using an Express Connect circuit. In this example, the CIDR block of VPC2 is different from the CIDR block of VPC1, but is the same with the CIDR block of VPC3. However, considering that VPC2 and VPC3 may need to communicate with each other later in the private network, the VSwitches in these VPCs are assigned with different CIDR blocks. This example demonstrates that VPCs communicating with each other can have identical CIDR blocks, but their VSwitches must have different CIDR blocks. When you specify CIDR blocks for multiple VPCs that need to communicate with each other, follow these rules: The preferred practice is to specify different CIDR blocks for different VPCs. You can use the subsets of the standard CIDR blocks to increase the number of available CIDR blocks. If you cannot assign different CIDR blocks for VPCs, try to specify different CIDR blocks for the VSwitches in these VPCs. If you cannot assign different CIDR blocks for all VSwitches in these VPCs, make sure that different CIDR blocks are configured for the VSwitches communicating with each other.

### 3.2 Create an IPv4 VPC

This topic describes how to build a virtual private cloud (VPC) with an IPv4 Classless Inter-domain Routing (CIDR) block and create an Elastic Compute Service (ECS) instance in the VPC. Prerequisites Before you create a VPC, you must first plan and design the VPC. For more information, see Plan networks. Step 1: Create a VPC Perform the following steps to create a VPC:
1. Log on to the VPC console.
2. On the VPCs page, click Creat e VPC.
3. On the Creat e VPC page, configure the VPC and click Submit . The following table describes the
parameters for creating a VPC.

| Parameter | Description |   |   |
|---|---|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |   |   |
| Resource Set | Select the resource set to which the VPC belongs. |   |   |
| Region | Select a region to deploy the VPC. |   |   |
| Share wit h Sub- organiza t ions | Specify whether to share the VPC. If you select Yes, the administrators of sub-organizations can create resources in the VPC. In this tutorial, select No. |   |   |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . In this tutorial, enter VPCt est . |   |   |
|   |   | htt |   |

|   | ps:// |
|---|---|

| Parameter | Description |   |   |
|---|---|---|---|
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following setting methods are supported: Recommended CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8. Cust om CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or a subset of these CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/16. In this tutorial, select Recommended CIDR Block and then select 192.168.0.0/16. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |   |   |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block to the VPC. Do Not Assign: No IPv6 CIDR block will be assigned to the VPC. Assign: An IPv6 CIDR block will be automatically assigned to the VPC. In this tutorial, select Do Not Assign. |   |   |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . |   |   |
|   |   | htt |   |

|   | ps:// |
|---|---|

Step 2: Create a VSwitch Perform the following steps to create a VSwitch in a VPC:
1. In the left-side navigation pane, click VSwit ches.
2. On the VSwit ches page, click Creat e VSwit ch.
3. On the VSwit ch page, configure the VSwitch and click Submit . The following table describes the
parameters for creating a VSwitch.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the VSwitch belongs. |
| Resource Set | Select the resource set to which the VSwitch belongs. |
| Region | Select a region to deploy the VSwitch. |
| Zone | Select a zone to deploy the VSwitch. Each VSwitch must reside entirely within one zone and cannot span multiple zones. However, you can deploy cloud resources in VSwitches that reside in different zones to achieve zone-disaster recovery. Not e Each cloud resource can be deployed in only one VSwitch. |

| Parameter | Description |
|---|---|
| VPC | Select the VPC for which you want to create the VSwitch. In this tutorial, select VPCtest. |
| Dedicat ed f or Of f -Cloud Servers | Specify whether the VSwitch is dedicated for off-cloud servers. For more Information, see the Feat ures of of f -cloud servers f or VPC section in the ECS Bare Metal Instance User Guide. In this tutorial, select No. |
| VSwit ch Name | Enter a name for the VSwitch. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas _ (,). It must start with a letter or a Chinese character and cannot start with http:/ / or https:// . |
| IPv4 CIDR Block | Enter an IPv4 CIDR block for the VSwitch. This tutorial uses the default IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block to the VSwitch. In this tutorial, select Do Not Assign. |
| Descript ion | Enter a description for the VSwitch. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |

|   | / |
|---|---|

Step 3: Create a security group Perform the following steps to create a security group:
1. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
2. Choose Net works and Securit y > Securit y Groups.
3. On the Securit y Groups page, click Creat e Securit y Group.
4. On the Creat e Securit y Group page, configure the security group and click Submit . The
following table describes the parameters for creating a security group.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the security group belongs. |
| Resource Set | Select the resource set to which the security group belongs. |

| Parameter | Description |
|---|---|
| Region | Select the region that will use the security group. The security group and the VPC must belong to the same region. |
| Zone | Select the zone that will use the security group. |
| VPC | Select the VPC to which the security group belongs. |
| Securit y Group Name | Enter a name for the security group. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods _ (.), colons (:), and commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |
| Descript ion | Enter a description for the security group. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods _ (.), colons (:), and commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |

Step 4: Create an ECS instance Perform the following steps to create an ECS instance in the specified VPC:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, click VSwit ches.
3. In the top navigation bar, select the region of the target VSwitch.
4. On the VSwit ches page, find the target VSwitch and choose Purchase > ECS Inst ance in the
Act ions column.
5. On the Creat e ECS Inst ance page, configure the ECS instance and click Submit .
For more information about how to configure an ECS instance, see Creat e an inst ance under Quick st art in the Apsara Stack Elastic Compute Service User Guide.

### 3.3 Create an IPv6 VPC

This topic describes how to build a virtual private cloud (VPC) with an IPv6 Classless Inter-domain Routing (CIDR) block and create an Elastic Compute Service (ECS) instance assigned with an IPv6 address in the VPC. Step 1: Create a VPC and a VSwitch Before you deploy cloud resources in a VPC, you must create a VPC and a VSwitch. Perform the following steps to create a VPC and a VSwitch:
1. Log on to the VPC console.
2. On the VPCs page, click Creat e VPC.
3. On the Creat e VPC page, configure the VPC and click Submit . The following table describes the
parameters for creating a VPC.

| Parameter | Description |   |   |
|---|---|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |   |   |
| Resource Set | Select the resource set to which the VPC belongs. |   |   |
| Region | Select a region to deploy the VPC. |   |   |
| Share wit h Sub- organiza t ions | Specify whether to share the VPC. If you select Yes, the administrators of sub-organizations can create resources in the VPC. In this tutorial, select No. |   |   |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . In this tutorial, enter VPCt est . |   |   |
|   |   | htt |   |
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following setting methods are supported: Recommended CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8. Cust om CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or a subset of these CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/16. In this tutorial, select Recommended CIDR Block and then select 192.168.0.0/16. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |   |   |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block to the VPC. Do Not Assign: No IPv6 CIDR block will be assigned to the VPC. Assign: An IPv6 CIDR block will be automatically assigned to the VPC. In this tutorial, select Assign. |   |   |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . |   |   |
|   |   | htt |   |

|   | ps:// |
|---|---|

|   | ps:// |
|---|---|

4. Click Back t o Console. In the left navigation pane, click VSwit ches.
5. On the VSwit ches page, click Creat e VSwit ch.
6. On the VSwit ch page, configure the VSwitch and click Submit . The following table describes the
parameters for creating a VSwitch.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the VSwitch belongs. |
| Resource Set | Select the resource set to which the VSwitch belongs. |
| Region | Select a region to deploy the VSwitch. |
| Zone | Select a zone to deploy the VSwitch. Each VSwitch must reside entirely within one zone and cannot span multiple zones. However, you can deploy cloud resources in VSwitches that reside in different zones to achieve zone-disaster recovery. Not e Each cloud resource can be deployed in only one VSwitch. |
| VPC | Select the VPC for which you want to create the VSwitch. In this tutorial, select VPCtest. |
| Dedicat ed f or Of f -Cloud Servers | Specify whether the VSwitch is dedicated for off-cloud servers. For more Information, see the Feat ures of of f -cloud servers f or VPC section in the ECS Bare Metal Instance User Guide. In this tutorial, select No. |
| VSwit ch Name | Enter a name for the VSwitch. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas _ (,). It must start with a letter or a Chinese character and cannot start with http:/ / or https:// . |
| IPv4 CIDR Block | Enter an IPv4 CIDR block for the VSwitch. This tutorial uses the default IPv4 CIDR block. |
| IPv6 CIDR Block | Enter an IPv6 CIDR block for the VSwitch. This tutorial uses the default IPv6 CIDR block. |
| Descript ion | Enter a description for the VSwitch. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |

|   | / |
|---|---|

Step 2: Create a security group Perform the following steps to create a security group:
1. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
2. Choose Net works and Securit y > Securit y Groups.
3. On the Securit y Groups page, click Creat e Securit y Group.
4. On the Creat e Securit y Group page, configure the security group and click Submit . The
following table describes the parameters for creating a security group.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the security group belongs. |
| Resource Set | Select the resource set to which the security group belongs. |
| Region | Select the region that will use the security group. The security group and the VPC must belong to the same region. |
| Zone | Select the zone that will use the security group. |
| VPC | Select the VPC to which the security group belongs. |
| Securit y Group Name | Enter a name for the security group. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods _ (.), colons (:), and commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |
| Descript ion | Enter a description for the security group. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods _ (.), colons (:), and commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |

Step 3: Create and configure an ECS instance After you create a VPC and a VSwitch, you must create an ECS instance and assign an IPv6 address to the ECS instance, and then associate this IPv6 address with the network interface controller (NIC) of the ECS instance. Perform the following steps to create and configure an ECS instance:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, click VSwit ches.
3. Select the region where your VSwitch resides.
4. On the VSwit ches page, find the target VSwitch and choose Purchase > ECS Inst ance in the
Act ions column.
5. On the Creat e ECS Inst ance page, configure the ECS instance and click Submit .
In this tutorial, select Assign to assign an IPv6 address to the ECS instance. For more information about other parameters, see Creat e an inst ance under Quick st art in the Apsara Stack Elastic Co mpute Service User Guide.
6. Return to the Inst ances page, and click the instance ID to view the assigned IPv6 address.
7. Configure a static IPv6 address.
If the image of your ECS instance supports DHCPv6, you do not need to manually configure the static IPv6 address. DHCPv6 enables automatic configuration of IPv6 addresses. Therefore, if your ECS instance image supports DHCPv6, the ECS instance can use the assigned IPv6 address to communicate in the private network directly after being created. The following images support DHCPv6: Linux images: CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images If the image of your ECS instance does not support DHCPv6, you must manually configure an IPv6 address for the ECS instance. We recommend that you refer to the related documentation for each image for configuration guidance. Step 4: Purchase an IPv6 Internet bandwidth plan By default, IPv6 addresses are only used for communication inside private networks. If you want to allow an instance assigned with an IPv6 address to access the Internet or be accessed by IPv6 clients over the Internet, you must purchase an Internet bandwidth plan for the IPv6 address. Perform the following steps to purchase an Internet bandwidth plan for the IPv6 address:
1. In the top navigation bar, choose Product s > Net working > IPv6 Gat eway.
2. Select the region where the IPv6 Gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 Gateway and click Manage in the Act ions
column.
4. In the left-side navigation pane, click IPv6 Int ernet Bandwidt h.
5. On the IPv6 Int ernet Bandwidt h page, find the target IPv6 address and click Enable IPv6
Int ernet Bandwidt h in the Act ions column.
6. Select a bandwidth plan and then click Submit .
The maximum IPv6 Internet bandwidth for an IPv6 Gateway of the Free, Enterprise, or Enhanced Edition is 2 Gbit/s. Step 5: Configure the security group rules IPv4 and IPv6 addresses are independent of each other. If the current security group rules cannot serve your IPv6 services, you must configure security group rules for IPv6 traffic. For more information, see Add securit y group rules under Securit y groups in the Apsara Stack Elastic Compute Service User Guide. Step 6: Test the network connectivity Log on to the ECS instance and run the ping command to test the network connectivity.

## 4 VPCs and VSwitches

### 4.1 Overview

To get started with Virtual Private Cloud, you need to create at least one virtual private cloud (VPC) and one VSwitch. You can create VSwitches in a VPC to partition a VPC into multiple subnets. By default, subnets (VSwitches) within a VPC can communicate with each other over the private network. VPCs and VSwitches A VPC is a virtual network dedicated for your use. You can deploy cloud resources in VPCs that you define. Not e A cloud resource cannot be directly deployed in a VPC, but can be deployed in a VSwitch of the VPC. A VSwitch is a basic network component in a VPC and is used to connect cloud resources. Each VPC must reside entirely within one region and cannot span multiple regions. However, a VPC spans all of the zones in a region, which means you can create one or more VSwitches in each zone to partition a VPC into subnets. CIDR blocks and IP addresses VPCs support both IPv4 and IPv6 addressing protocols. By default, VPCs use the IPv4 addressing protocol. You can enable the IPv6 addressing protocol as needed. VPCs can operate in a dual-stack mode, which allows your resources to communicate over IPv4, or IPv6, or both. IPv4 and IPv6 addresses are independent of each other. Therefore, you must configure routing and security groups in your VPC separately for IPv4 and IPv6. The following table summarizes the differences between IPv4 and IPv6 in Apsara Stack VPC.

| IPv4 VPC | IPv6 VPC |
|---|---|
| The format is 32-bit, 4 groups of up to 3 decimal digits. | The format is 128-bit, 8 groups of 4 hexadecimal digits. |
| The IPv4 addressing protocol is enabled for all VPCs by default. | The IPv6 addressing protocol is optional for a VPC. |
| The VPC Classless Inter-domain Routing (CIDR) block size can be from /8 to /24. | The VPC CIDR block size is fixed at /61. |
| The VSwitch CIDR block size can be from /16 to /29. | The VSwitch CIDR block size is fixed at /64. |
| You can choose the private IPv4 CIDR block for your VPC. | Apsara Stack automatically assigns an IPv6 CIDR block for your VPC from its IPv6 address pool.You cannot select your own range. |
| Supported on all instance types. | Not supported on certain instance types. For more information, see Inst ance t ypes under What is ECS in the Apsara Stack Elastic Compute Service User Guide. |
| Elastic IPv4 addresses are supported. | Elastic IPv6 addresses are not supported. |
| VPN gateways and NAT gateways are supported. | VPN gateways and NAT gateways are supported. |

By default, the IPv4 and IPv6 addresses provided for VPCs can only be used for communication within the private network. Resources in different VSwitches within a VPC communicate with one another over private network connections. To connect a VPC to another VPC or an on-premises data center, you need to configure Express Connect or VPN Gateway. . To enable cloud resources in a VPC to access the Internet, set the following configurations: IPv4 communication You can configure a NAT gateway or associate elastic IP addresses (EIPs) to the Elastic Compute Service (ECS) instances in a VPC to allow these ECS instances to access the Internet by using IPv4 addresses. IPv6 communication To enable cloud resources in a VPC to access the Internet by using an IPv6 address, you must purchase public bandwidth for the IPv6 address. You can also configure an egress-only rule for an IPv6 address to allow outbound communication over IPv6 from instances in your VPC to the Internet, and prevent clients on the Internet from initiating IPv6 connections with your instances. Routing After a VPC is created, the system automatically creates a system route table and adds system routes to the route table for traffic management. Each VPC has only one system route table, which is generated automatically upon the creation of the VPC. You cannot create or delete system route tables. If one destination address matches more than one route entry in a route table, the system selects an entry by implementing the longest prefix match algorithm, whereby the most specific of the matching entries, the one with the longest subnet mask, is used to route traffic. You can add a custom route entry to route traffic destined for a specific destination. For more information, see Add a custom route entry.

### 4.2 VPC management

#### 4.2.1 Create a VPC

A virtual private cloud (VPC) is a private network dedicated for your use. You have full control over your VPC. For example, you can specify Classless Inter-domain Routing (CIDR) blocks, configure route tables, and set network gateways for your VPC. You can deploy Apsara Stack resources in your VPC, such as Elastic Compute Service (ECS) instances, ApsaraDB for RDS (RDS) instances, and Server Load Balancer (SLB) instances.
1. Log on to the VPC console.
2. In the top navigation bar, select a region to deploy your VPC.
Not e The VPC must be in the same region as the cloud resources that you want to deploy in this VPC.
3. On the VPC page, click Creat e VPC.
4. On the Creat e VPC page, configure the VPC and click Submit . The following table describes the
parameters for creating a VPC.

| Parameter | Description |   |   |
|---|---|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |   |   |
| Resource Set | Select the resource set to which the VPC belongs. |   |   |
| Region | Select a region to deploy the VPC. |   |   |
| Share wit h Sub- organiza t ions | Specify whether to share the VPC. If you select Yes, the administrators of sub-organizations can create resources in the VPC. |   |   |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . |   |   |
|   |   | htt |   |
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following setting methods are supported: Recommended CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8. Cust om CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or a subset of these CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/16. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |   |   |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block to the VPC. Do Not Assign: No IPv6 CIDR block will be assigned to the VPC. Assign: An IPv6 CIDR block will be automatically assigned to the VPC. If you set this parameter to Assign, the system automatically creates a free IPv6 gateway for this VPC, and assigns an IPv6 CIDR block with the subnet mask /56, such as 2xx1: db8::/56. By default, IPv6 addresses are only used for communication inside private networks. If you want to allow an instance assigned with an IPv6 address to access the Internet or be accessed by IPv6 clients over the Internet, you must purchase an Internet bandwidth plan for the IPv6 address. For more information, see Enable IPv6 Int ernet bandwidt h under Manage IPv6 Int ernet bandwidt h in the Apsara Stack Elastic Compu te Service User Guide. |   |   |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . |   |   |
|   |   | htt |   |

|   | ps:// |
|---|---|

|   | ps:// |
|---|---|

#### 4.2.2 Modify the name and description of a VPC

This topic describes how to modify the name and description of a virtual private cloud (VPC).
1. Log on to the VPC console.
2. In the top navigation bar, select the region where your VPC is deployed.
3. On the VPCs page, find the target VPC network and click Manage in the Act ions column.
4. In the VPC Det ails section, click Edit next to Name. In the dialog box that appears, enter a new
name for the VPC and click OK. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores (_), and hyphens (-). It must start with a letter or a Chinese character.
5. Click Edit next to Descript ion. In the dialog box that appears, enter a new description, and click
OK. The description must be 2 to 256 characters in length and cannot start with `http://` or `https:` `//` .

#### 4.2.3 Delete a VPC

This topic describes how to delete a virtual private cloud (VPC). After you delete a VPC, the VRouter and route tables associated with this VPC are also deleted. Prerequisites Before you delete a VPC, make sure that the following requirements are met: No VSwitch exists in the VPC. If the VPC has one or more VSwitches, we recommend that you delete the VSwitches first before deleting the VPC. For more information, see Delete a vSwitch. No IPv6 gateway is associated with the VPC. If the VPC is associated with an IPv6 gateway, we recommend that you delete the IPv6 gateway first before deleting the VPC.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where your VPC is deployed.
3. On the VPCs page, find the target VPC and click Delet e in the Act ions column.
4. In the Delet e VPC dialog box, click OK.

### 4.3 VSwitch management

#### 4.3.1 Create a VSwitch

A VSwitch is a basic network component in a virtual private cloud (VPC) and is used to connect cloud resources. Context After you create a VPC, you can create VSwitches to partition your VPC into multiple subnets. VSwitches within a VPC can communicate with each other over the private network. Cloud resources are deployed in VSwitches. You can deploy your applications in VSwitches that belong to different zones to improve service availability. Not e VSwitches do not support multicasting or broadcasting.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. Select the region of the VPC in which you want to create a VSwitch.
4. On the VSwit ches page, click Creat e VSwit ch.
5. On the VSwit ch page, configure the VSwitch and click Submit . The following table describes the
parameters for creating a VSwitch.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the VSwitch belongs. |
| Resource Set | Select the resource set to which the VSwitch belongs. |
| Region | Select a region to deploy the VSwitch. |
| Zone | Select a zone to deploy the VSwitch. Each VSwitch must reside entirely within one zone and cannot span multiple zones. However, you can deploy cloud resources in VSwitches that reside in different zones to achieve zone-disaster recovery. Not e Each cloud resource can be deployed in only one VSwitch. |
| VPC | Select the VPC for which you want to create the VSwitch. |
| Dedicat ed f or Of f -Cloud Servers | Specify whether the VSwitch is dedicated for off-cloud servers. For more Information, see the Feat ures of of f -cloud servers f or VPC section in the ECS Bare Metal Instance User Guide. |
| VSwit ch Name | Enter a name for the VSwitch. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas _ (,). It must start with a letter or a Chinese character and cannot start with http:/ / or https:// . |

|   | / |
|---|---|

| Parameter | Description |
|---|---|
| IPv4 CIDR Block | Enter an IPv4 CIDR block for the VSwitch. You must specify the IP address range for the VSwitch in the form of a CIDR block. The CIDR block size for a VSwitch is between a 16-bit mask and a 29-bit mask. It means that 8 to 65,536 IP addresses can be provided. The CIDR block of a VSwitch must be a subset of the CIDR block of the VPC this VSwitch resides in. The first and the last three IP addresses in each VSwitch CIDR block are reserved by the system. For example, if the CIDR block of a VSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The CIDR block of a VSwitch must be more specific than the CIDR range of a route in any of the VPC route tables. After you create a VSwitch, you cannot modify its CIDR block. |
| IPv6 CIDR Block | Enter an IPv6 CIDR block for the VSwitch. You must check whether IPv6 is enabled for the specified VPC. If not, you cannot assign an IPv6 CIDR block to the VSwitch. If yes, you can enter a decimal number ranging from 0 to 255 to define the last 8 bits of the IPv6 CIDR block of the VSwitch. For example, if the IPv6 CIDR block of the VPC that contains the VSwitch is 2xx1:db8::/64, you can enter 255 (FF in the hexadecimal system) in this field to define the IPv6 CIDR block of the VSwitch as 2xx1:db8:ff::/64. |
| Descript ion | Enter a description for the VSwitch. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter or a Chinese character and cannot start with http:// or https:// . |

#### 4.3.2 Create cloud resources in a VSwitch

This topic describes how to create cloud resources in a VSwitch. Note that cloud resources are not directly deployed in a virtual private cloud (VPC), but are provisioned into VSwitches (subnets) of a VPC. You can create cloud resources in a VSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. Select the region of the VPC to which the VSwitch belongs.
4. On the VSwit ches page, find the target VSwitch, click Purchase in the Act ions column, and
select the cloud resource you want to create. You can create Elastic Compute Service (ECS) instances, ApsaraDB for RDS (RDS) instances, and Server Load Balancer (SLB) instances in a VSwitch.
5. On the page that appears, set the parameters to create a cloud resource.

#### 4.3.3 Modify the name and description of a VSwitch

VSwitch This topic describes how to modify the name and description of a VSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region of the VPC in which you want to create a vSwitch.
4. On the VSwit ches page, find the target VSwitch and click Manage in the Act ions column.
5. In the VSwit ch Basic Inf ormat ion section, click Edit next to Name. In the dialog box that
appears, enter a new name for the VSwitch and click OK. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores (_), and hyphens (-). It must start with a letter or a Chinese character.
6. Click Edit next to Descript ion. In the dialog box that appears, enter a new description for the
VSwitch and click OK. The description must be 2 to 256 characters in length and cannot start with `http://` or `https:` `//` .

#### 4.3.4 Delete a VSwitch

This topic describes how to delete a VSwitch that you no longer need. Cloud resources cannot be deployed in deleted VSwitches. Prerequisites Before you delete a VSwitch, make sure that the following conditions are met: You have deleted all of your cloud resources created under the VSwitch, such as Elastic Compute Service (ECS) instances, Server Load Balancer (SLB) instances, and ApsaraDB for RDS (RDS) instances. You have deleted or disabled all resources and actions associated with this VSwitch, such as highavailability virtual IP addresses (HAVIPs) and source network address translation (SNAT) entries.
1. Log on to the VPC console.
2. 3.
4. On the vSwit ch page, find the target VSwitch and click Delet e in the Act ions column.
5. In the Delet e vSwit ch dialog box that appears, click OK.

## 5 Route tables

### 5.1 Overview

Routes and route tables Each virtual private cloud (VPC) comes with a default route table pre-configured with system route entries that direct traffic flowing in and out of the VPC. You cannot create or delete system route entries. However, you can create custom route entries to route traffic destined for specific Classless Inter-domain Routing (CIDR) blocks to the destinations that you define. Route tables When you create a VPC, it automatically has a system route table that controls the routing for all VSwitches (subnets) within the VPC by default. You cannot create or delete the system route table of a VPC. Each route entry in the route table defines a route that is used to direct traffic, and consists of multiple fields, including the destination CIDR block, the next hop for the traffic, and the type of the next hop. Route entries are classified into system route entries and custom route entries. Each VPC can have a maximum of 10 route tables. The system route table counts toward this quota. A VSwitch can only be associated with one route table at a time. The route table associated with a VSwitch manages the routing policies of the VSwitch. A VSwitch is associated with the system route table by default. After you disassociate a custom route table from a VSwitch, the VSwitch is automatically associated with the system route table. Before you change the custom route table associated with a VSwitch to another custom route table, you must disassociate the current custom route table from the VSwitch, and then associate the VSwitch with another custom route table. All regions support custom route tables, except China (Beijing), China (Shenzhen), and China (Hangzhou). Custom route tables do not support active/standby or load-balancing routes. System routes After you create a VPC, the system automatically adds the following system routes to the route table: A route entry with a destination CIDR block of 100.64.0.0/10. This route is used for communication among cloud resources within the VPC. Route entries with destination CIDR blocks same as the CIDR blocks of the VSwitches in this VPC. Such routes are used for communication among cloud resources within VSwitches. For example, if you create a VPC and specify 192.168.0.0/16 as its CIDR block, and then create two VSwitches whose CIDR blocks are 192.168.1.0/24 and 192.168.0.0/24, three system routes listed in the following table are automatically added to the route table of the VPC.

| Destination CIDR block | Next hop | Route entry type |
|---|---|---|
| 100.64.0.0/10 | - | System route |
| 192.168.1.0/24 | - | System route |

| irtual Private Cloud |   | User Guide·Route table |
|---|---|---|

| Destination CIDR block | Next hop | Route entry type |
|---|---|---|
| 192.168.0.0/24 | - | System route |

Custom routes You can add custom routes to replace system routes or route traffic to specified destinations. You can specify the following next hop types when you create a custom route: ECS instance: Traffic destined for the destination CIDR block is forwarded to a specified Elastic Compute Service (ECS) instance in the VPC. You can select this type if you want to access the Internet or other applications through the applications deployed on an ECS instance. VPN gateway: Traffic destined for the destination CIDR block is forwarded to a specified VPN gateway. You can select this type if you want to connect a VPC to another VPC or a local network through a VPN connection. NAT gateway: Traffic destined for the destination CIDR block is forwarded to a specified NAT gateway. You can select this type if you want to connect a VPC to the Internet by using a NAT gateway. Router interface (to VPC): Traffic destined for the destination CIDR block is forwarded to a specified VPC. You can select this type if you want to connect two VPCs by using Express Connect. Router interface (to VBR): Traffic destined for the destination CIDR block is forwarded to a specified Virtual Border Router (VBR). You can select this type if you want to connect a VPC to an on-premises network by using Express Connect. Secondary ENI: Traffic destined for the destination CIDR block is forwarded to a specified secondary Elastic Network Interface (ENI). IPv6 routes If IPv6 is enabled for your VPC, the following route entries are automatically added to the system route table of the VPC: A custom route entry with a destination CIDR block of ::/0 and whose next hop is the IPv6 gateway. This route is used to direct traffic between the cloud resources deployed in the VPC and the Internet by using IPv6 addresses. System route entries whose destination CIDR blocks are the IPv6 CIDR blocks of the VSwitches in the VPC. Such routes are used for communication within the VSwitches. Routing rules If one destination address matches more than one route entry in a route table, the system selects an entry by implementing the longest prefix match algorithm, whereby the most specific of the matching entries, the one with the longest subnet mask, is used to route traffic. The following table describes a route table of a VPC.

| Destination CIDR block | Next hop type | Next hop | Route entry type |
|---|---|---|---|
| 100.64.0.0/10 | - | - | System route |
| 192.168.0.0/24 | - | - | System route |
| 0.0.0.0/0 | Instance | i-12345678 | Custom route |
| 10.0.0.0/24 | Instance | i-87654321 | Custom route |

As shown in the preceding table, the route entries destined for `100.64.0.0/10` and `192.168.0.0/24` are system route entries, and the two destined for `0.0.0.0/0` and `10.0.0.0/24` are custom route entries. Traffic destined for `0.0.0.0/0` is forwarded to the ECS instance `i-12345678` , and traffic destined for `10.0.0.0/24` is forwarded to the ECS instance `i-` `87654321` . According to the longest prefix match algorithm, traffic destined for `10.0.0.1` is forwarded to the ECS instance `i-87654321` , and traffic destined for `10.0.1.1` is forwarded to the ECS instance `i-12345678` . Routing examples You can add custom route entries to a route table to control inbound and outbound traffic for a VPC. Routing within a VPC As shown in the following figure, a NAT gateway is deployed on an ECS instance (ECS01) in a VPC. To enable the cloud resources in this VPC to access the Internet by this ECS instance, you can add the following route entry to the route table.

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 0.0.0.0/0 | ECS instance | ECS01 |

Connect two VPCs by using Express Connect As shown in the following figure, VPC1 (172.16.0.0/12) needs to be connected to VPC2 (192.168.0.0/16) by using Express Connect. After you create router interfaces for interconnection, you must add the following route entries in the route table of each VPC respectively. VPC1

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Router interface (to VPC) | VPC2 |

VPC2

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | Router interface (to VPC) | VPC1 |

Connect two VPCs by using VPN gateways As shown in the following figure, VPC1 (172.16.0.0/12) needs to be connected to VPC2 (10.0.0.0/8) with VPN gateways. After you configure the VPN gateways, you must add the following route entries in the route table of each VPC respectively. VPC1

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 10.0.0.0/8 | VPN gateway | VPN gateway 1 |

VPC2

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | VPN gateway | VPN gateway 2 |

Connect a VPC to an on-premises data center by using Express Connect As shown in the following figure, a VPC needs to be connected to an on-premises data center by using Express Connect. After you configure an Express Connect circuit and a VBR, you must add the following route entries for related networks and devices: VPC

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Router interface (general routing) | Router interface RI1 |

VBR

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | To the Express Connect circuit | Router interface RI3 |
| 172.16.0.0/12 | To VPC | Router interface RI2 |

On-premises network

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | - | A specified local gateway device |

Connect a VPC to an on-premises data center by using VPN gateways As shown in the following figure, a VPC (172.16.0.0/12) needs to be connected to an on-premises data center (192.168.0.0/16). After you configure the VPN gateway, you must add the following route entry to the route table of the VPC.

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | VPN gateway | A specified VPN gateway |

### 5.2 Add a custom route entry

This topic describes how to add a custom route entry. After you create a Virtual Private Cloud (VPC) network, the system creates a default route table and adds system route entries to the route table for traffic management. You cannot create or delete system route entries. However, you can create custom route entries to route traffic from source CIDR blocks to specific destinations. Context Each entry in the route table is a route entry. A route entry, which specifies the destination for network traffic, consists of the destination CIDR block, next hop type, and next hop. Route entries are classified into system route entries and custom route entries.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route tables belong.
4. On the Rout e T ables page, find the route table and click Manage in the Act ions column.
5. In the Rout e T able Det ails section, click the Rout e Ent ry List tab, and then click Add Rout e
Ent ry.
6. On the Add Rout e Ent ry page, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Name | The name of the route entry. The name must be 2 to 128 characters and can contain digits, underscores ( ), and hyphens (-). The name must start with a letter or a Chinese _ character. |
| Dest inat ion CIDR Block | The destination CIDR block to which you want to route traffic. |

| Parameter | Description |
|---|---|
| Next Hop T ype | The type of the next hop. Valid values: ECS Inst ance: Traffic destined for the specified CIDR block is routed to the Elastic Compute Service (ECS) instance you select. Select this type if you want to route traffic to an ECS instance for centralized traffic forwarding and management. For example, when an ECS instance is configured as the Internet-facing gateway to manage the traffic from other ECS instances to the Internet. VPN Gat eway: Traffic destined for the specified CIDR block is routed to the VPN gateway you select. NAT Gat eway: Traffic destined for the specified CIDR block is routed to the NAT gateway you select. Rout er Int erf ace (T o VPC): Traffic destined for the specified CIDR block is routed to the VPC network you select. Select this type if you want to connect VPC networks through Express Connect. Rout er Int erf ace (T o VBR): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a Virtual Border Router (VBR). Select this type if you want to connect the VPC network to an on-premises data center through Express Connect. If you select Router Interface (To VBR), you must also select a routing mode: General Rout ing: Select an associated router interface. Act ive/St andby Rout ing: Select two instances as the next hop. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes over when the active route fails the health check. Load Balancing: Select two to four router interfaces as the next hop. The peer router of each router interface must be a VBR. Valid values of the instance weight: 1 to 255. The value must be an integer and the default value is 100. The weights of the selected instances must be the same. This way, traffic can be evenly distributed to the next-hop instances. |
| ECS Inst ance/VPN Gat eway/NAT Gat eway | Select the next-hop instance. |

Related information CreateRouteEntry

### 5.3 Export route entries

This topic describes how to export route entries from a route table for backup.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click Manage in the Act ions column.
5. In the Rout e T able Det ails section, click the Rout e Ent ry List tab, and then click Export .
The route entries are exported to a .csv file in your local computer.

### 5.4 Modify a route table

This topic describes how to modify the name and description of a route table.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click its ID.
5. In the Rout e T able Det ails section, click Edit next to Name. In the dialog box that appears, enter
a new name for the route table and click OK. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores (_), and hyphens (-). It must start with a letter or a Chinese character.
6. Click Edit next to Descript ion. In the dialog box that appears, enter a new description of the route
table, and click OK. The description must be 2 to 256 characters in length and cannot start with `http://` or `https:` `//` .

### 5.5 Delete a custom route entry

This topic describes how to delete a custom route entry. A route table consists of one or more route entries that determine which way to forward traffic. Note that system route entries cannot be deleted.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click its ID.
5. On the Rout e Ent ry List tab, find the target route entry and then click Delet e in the Act ions
column.
6. In the Delet e Rout e Ent ry dialog box, click OK.

## 6 HAVIPs

### 6.1 Overview

A high-availability virtual IP address (HAVIP) is a private IP address that can be created and released as an independent resource. After you associate an HAVIP with an Elastic Compute Service (ECS) instance, the ECS instance can advertise this HAVIP by sending Address Resolution Protocol (ARP) messages. Features HAVIPs have the following features: Each HAVIP can be associated with a maximum of two ECS instances. After the association, the ECS instance can advertise the associated HAVIP by sending ARP messages. Each ECS instance can claim more than one private IP address by advertising multiple HAVIPs. By allowing ECS instances to advertise HAVIPs with ARP messages, a Virtual Router Redundancy Protocol (VRRP) configuration is implemented to ensure high availability of your services. Each HAVIP can be associated with an elastic IP address (EIP), which means that after an HAVIP is disassociated from the previous ECS instance and reassociated with a different ECS instance, the traffic sent to the EIP can also be delivered to the current ECS instance. Scenarios HAVIPs support flexible configurations in the following scenarios. Scenario 1: High availability services for private networks High-availability solutions are provided by using open-source programs such as Keepalived and Heartbeat. In the following figure, Keepalived integrates the HAVIP and two ECS instances (ECS 1 and ECS 2) into a highly available solution designed for the private network. The cloud instances in the same virtual private cloud (VPC) can access this service over the private network from the IP address of this HAVIP, which is also the endpoint. The high availability of this solution makes sure that ECS 2 is always ready to serve on the same IP address in case ECS 1 fails. Scenario 2: High availability services on the Internet High-availability solutions are provided by using open-source programs such as Keepalived and Heartbeat. In the following figure, ECS 1 and ECS 2 are associated with an HAVIP, which is configured with an EIP. In this case, the service can be accessed over the Internet from its endpoint, that is, the IP address of the HAVIP. Keepalived is used to implement failover, where ECS 2 takes over to keep the service available on the same IP address in case ECS 1 fails. Limits Before you use HAVIPs, note the following limits: HAVIPs can only be deployed in VPCs. HAVIPs do not support multicasting or broadcasting. Each account can hold a maximum of five HAVIPs. A maximum of five HAVIPs can exist in a VPC. Each ECS instance can be associated with a maximum of five HAVIPS. Each HAVIP can be associated with a maximum of two ECS instances. Each VPC can have a maximum of five route entries destined for HAVIPs.

### 6.2 Create an HAVIP

A high-availability virtual IP address (HAVIP) is a private IP address that can be created and released as an independent resource. This topic describes how to create an HAVIP in the console.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Click Creat e HaVip Address.
4. Configure the HAVIP and then click Submit . The following table describes the parameters for
creating an HAVIP.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the HAVIP belongs. |
| Resource Set | Select the resource set to which the HAVIP belongs. |
| Region | Select a region to deploy the HAVIP. |
| VPC | Select the VPC to which the HAVIP belongs. |
| VSwit ch | Select the VSwitch to which the HAVIP belongs. |
| Privat e IP Address | Specify a private IP address for the HAVIP. Not ice You must select an available private IP address in the CIDR range of the VSwitch. |

### 6.3 Associate an HAVIP with an ECS instance

instance This topic describes how to associate a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance deployed in a virtual private cloud (VPC). After the association, the ECS instance can advertise this HAVIP by sending Address Resolution Protocol (ARP) messages. Each HAVIP can be associated with a maximum of two ECS instances. Prerequisites An ECS instance is created and placed in the same region as the HAVIP to be associated. For more information, see Creat e an inst ance under Quick st art in the Apsara Stack Elastic Compute Service User Guide.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Select the region of the HAVIP.
4. Find the target HAVIP and then click Manage in the Act ions column.
5. In the Resources section, click the
icon.
6. On the page that appears, select the ECS instance to associate and click OK.
7. On the HaVip Det ails page, click Ref resh to check the ECS associations of this HAVIP.
After you associate an HAVIP with an ECS instance, you must configure the HAVIP on the network interface of the ECS instance.

### 6.4 Associate an HAVIP with an EIP

This topic describes how to associate a high-availability virtual IP address (HAVIP) with an elastic IP address (EIP). After the association, you can use the HAVIP to provide your instances with public network access. Prerequisites You have purchased an EIP. For more information, see Creat e an elast ic IP address under Quick st art in the Apsara Stack Elastic Compute Service User Guide.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Select the region of the HAVIP.
4. Find the target HAVIP instance and choose More > Bind EIP Address in the Act ions column.
5. On the page that appears, select the EIP to associate and click OK.

### 6.5 Disassociate an HAVIP from an ECS instance

ECS instance This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an Elastic Compute Service (ECS) instance. After the disassociation, the ECS instance can no longer announce this HAVIP by sending Address Resolution Protocol (ARP) messages.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Select the region of the HAVIP.
4. On the HaVip Addresses page, find the target HAVIP and then click Manage in the Act ions
column.
5. In the Resources section, find the target ECS instance and then click Unbind.
6. In the dialog box that appears, click OK.

### 6.6 Disassociate an EIP from an HAVIP

HAVIP This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic IP address (EIP). After the disassociation, you can no longer use the HAVIP to provide your instances with Internet access.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Select the region of the HAVIP.
4. On the HaVip Addresses page, find the target HAVIP and then choose More > Unbind wit h EIP
in the Act ions column.
5. In the dialog box that appears, click OK.

### 6.7 Delete an HAVIP

This topic describes how to delete a high-availability virtual IP address (HAVIP). Prerequisites The HAVIP is not associated with any elastic IP address (EIP). If the HAVIP is associated with an EIP, before you delete the HAVIP, you must disassociate it from the EIP. For more information, see Disassociate an EIP from an HAVIP. The HAVIP is not associated with any Elastic Compute Service (ECS) instance. If the HAVIP is associated with one or more ECS instances, before you delete the HAVIP, you must disassociate it from the ECS instances. For more information, see Disassociate an HAVIP from an ECS instance.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Select the region of the HAVIP.
4. On the HaVip Addresses page, find the target HAVIP and then choose More > Delet e in the
Act ions column.
5. In the dialog box that appears, click OK.
