---
title: "Alibaba Cloud Apsara Stack Enterprise V3.16.2 Virtual Private Cloud User Guide"
product_version: "V3.16.2"
doc_version: "20220719"
pdf_pages: 69
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.16.2 Virtual Private Cloud User Guide 20220719.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.16.2%20Virtual%20Private%20Cloud%20User%20Guide%2020220719.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise V3.16.2 Virtual Private Cloud User Guide

## What is a VPC?

A virtual private cloud (VPC) is a private network in the cloud. You can configure the CIDR block, route tables, and gateways of your VPC. You can use Alibaba Cloud services in a VPC, such as Elastic Compute Service (ECS), Server Load Balancer (SLB), and ApsaraDB RDS. You can connect your VPC to other VPCs or on-premises networks to create a custom network environment. This way, you can migrate applications to the cloud and extend data centers. Components Each VPC consists of one vRouter, at least one private CIDR block, and at least one vSwitch. Private CIDR blocks When you create a VPC and a vSwitch, you must specify the private IP address range for the VPC in CIDR notation. You can use the standard private CIDR blocks listed in the following table and their subsets as CIDR blocks for your VPCs. For more information, see the Plan and design a VPC topic in User Guide.

| CIDR block | Number of available private IP addresses (excluding system reserved IP addresses) |
|---|---|
| 192.168.0.0/16 | 65,532 |
| 172.16.0.0/16 | 65,532 |

vRouters A vRouter is the hub of a VPC. As a core component, it connects the vSwitches in a VPC and serves as a gateway between a VPC and other networks. After you create a VPC, the system automatically creates a vRouter. Each vRouter is associated with a route table. For more information, see the Route table overview topic in User Guide. vSwitches A vSwitch is a basic network component that connects different cloud resources in a VPC. After you create a VPC, you can create vSwitches to create one or more subnets for the VPC. vSwitches in the same VPC can communicate with each other. You can deploy your applications in vSwitches that belong to different zones to improve service availability. For more information, see the Create a vSwitch topic in User Guide. le

## Log on to the VPC console

This topic describes how to log on to the Virtual Private Cloud (VPC) console of Apsara Uni-manager by using the Google Chrome browser. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click Aut hent icat e. Not e For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Operations Console User Guide.
5. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.

## Quick start

### Design networks

Before you create virtual private clouds (VPCs) and vSwitches, you must decide the quantities and CIDR blocks of VPCs and vSwitches. How many VPCs do I use? How many vSwitches do I use? How do I specify CIDR blocks? How do I specify CIDR blocks if I want to connect a VPC to another VPC or a data center? How many VPCs do I use? One VPC If you do not want to deploy your business systems across regions or isolate different business systems, we recommend that you use one VPC. Multiple VPCs In the following scenarios, we recommend that you use multiple VPCs: Cross-region deployment A VPC cannot be deployed across regions. If you want to deploy your business system across regions, you must create VPCs in these regions. Then, you can use services such as Express Connect and VPN Gateway to connect the VPCs. Business system isolation If you want to isolate business systems deployed in the same region, you must create multiple VPCs. The following figure shows how the test environment is isolated from the production environment by using VPCs. How many vSwitches do I use? We recommend that you create at least two vSwitches in different zones for a VPC. This implements cross-zone disaster recovery. The network latency between different zones in a region is low. However. you still need to verify the network latency in your actual business system. This is because the network latency may be higher than expected due to complex data processing or cross-zone data transmission. We recommend that you optimize and adjust your business system to strike a balance between availability and latency. In addition, the size and design of your business system must also be taken into consideration when you create vSwitches. If your frontend systems are publicly accessible and your backend systems require Internet access, you can deploy the frontend systems in different vSwitches for redundancy. Then, deploy your backend systems in the remaining vSwitches. How do I specify CIDR blocks? When you create VPCs and vSwitches, you must specify their private IP addresses in CIDR block notation. Specify VPC CIDR blocks You can specify 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or their subsets as the CIDR blocks of your VPCs. When you specify VPC CIDR blocks, take note of the following rules: If you have only one VPC and the VPC does not need to communicate with a data center, you can specify one of the preceding CIDR blocks or their subsets as the VPC CIDR block. If you have multiple VPCs, or you want to set up a hybrid cloud environment between a VPC and your data center, we recommend that you specify the subsets of the preceding CIDR blocks for your VPCs. In this case, we recommend that you set the subnet mask length to 16 bits or less. Specify vSwitch CIDR blocks The CIDR block of a vSwitch must be a subset of the CIDR block of the VPC to which the vSwitch belongs. For example, if the CIDR block of a VPC is 192.168.0.0/16, the CDIR block of a vSwitch that belongs to the VPC can range from 192.168.0.0/17 to 192.168.0.0/29. When you specify vSwitch CIDR blocks, take note of the following rules: The subnet mask of a vSwitch CIDR block must be 16 to 29 bits in length. This allows the vSwitch to provide 8 to 65,536 IP addresses. A 16-bit subnet mask provides IP addresses for 65,532 Elastic Compute Service (ECS) instances, which can meet your needs in most cases. A subnet mask of more than 29 bits in length provides few IP addresses. The first IP address and the last three IP addresses of each vSwitch CIDR block are reserved for the system. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. When you specify the CIDR block of a vSwitch, you must also take into consideration the number of ECS instances that you want to attach to the vSwitch. How do I specify CIDR blocks if I want to connect a VPC to another VPC or a data center? Before you connect your VPC to another VPC or a data center, you must make sure that the VPC CIDR block does not conflict with that of the peer network. For example, you have three VPCs: VPC1 in the China (Hangzhou) region, VPC2 in the China (Beijing) region, and VPC3 in the China (Shenzhen) region, as shown in the following figure. An Express Connect circuit is used to connect VPC1 and VPC2. VPC3 does not communicate with other VPCs, but may need to communicate with VPC2 in the future. Additionally, you have a data center located in Shanghai, and you need to connect it to VPC1 by using an Express Connect circuit. In this example, the CIDR block of VPC2 is different from the CIDR block of VPC1, but is the same with the CIDR block of VPC3. Take into consideration that VPC2 and VPC3 need to communicate with each other through private connections, the vSwitches in these VPCs are assigned different CIDR blocks. The vSwitch CIDR blocks of VPCs that need to communicate with each other must be different. However, these VPCs can have the same CIDR block. When you specify CIDR blocks for multiple VPCs that need to communicate with each other, take note of the following rules: The preferred practice is to specify different CIDR blocks for different VPCs. You can use the subsets of standard CIDR blocks if the given CIDR blocks are insufficient. If you cannot assign different CIDR blocks to the VPCs, try to specify different CIDR blocks for vSwitches in these VPCs. If you cannot assign different CIDR blocks to all of the vSwitches in these VPCs, make sure that different CIDR blocks are specified for the vSwitches that need to communicate with each other.

### Create a VPC with an IPv4 CIDR

block This topic describes how to create a virtual private cloud (VPC) with an IPv4 CIDR block and how to create an Elastic Compute Service (ECS) instance in the VPC. Prerequisites To deploy cloud resources in a VPC, you must first plan the network. For more information, see Design networks. Step 1: Create a VPC
1. Log on to the VPC console.
2. On the Virt ual Privat e Clouds page, click Creat e a propriet ary net work.
3. On the Creat e VPC page, set the parameters and click Submit .

| Parameter | Description |
|---|---|
| Region |   |
| Organizat ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Basic Conf igurat ions |   |
| Sharing Scope | Select the sharing scope of the VPC. Current Resource Set : Only the administrator of the current resource set can use the VPC to create resources. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can use the VPC to create resources. Current Organizat ion: Only the administrator of the current organization can use the VPC to create resources. Current Resource Set is selected in this example. |

| Parameter | Description |
|---|---|
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter _ and cannot start with http:// or https:// . VPCt est is used in this example. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Cust om CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. Example: 192.168.0.0/16. In this example, 192.168.0.0/16 is used as the IPv4 CIDR block of the VPC. Not e After a VPC is created, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. Do Not Assign is selected in this example. |
| Descript ion | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter and cannot start with http:// or https:// . |

4. Click Back t o Console. On the Virt ual Privat e Clouds page, you can view the VPC that is created.
Step 2: Create a vSwitch
1. In the left-side navigation pane, click VSwit ches.
2. On the VSwit ches page, click Creat e a swit ch.
3. On the Creat e vSwit ch page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Basic Inf ormat ion |   |
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |

| l Private Cloud | User Guide·Quick star |
|---|---|

| Parameter | Description |
|---|---|
| Region |   |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone where you want to deploy the vSwitch. In a VPC, a vSwitch can be deployed only in one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e An instance can be deployed in only one vSwitch. |
| Det ailed Set t ings |   |
| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set : Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organizat ion: Only the administrator of the current organization can use the vSwitch to create resources. Current Resource Set is selected in this example. |
| VPC | Select the VPC in which you want to create the vSwitch. VPCtest is selected in this example. |
| Dedicat ed f or Bare Met al Inst ances | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-met al servers in VPCs topic in Bare-metal Server Management Service User Guide. No is selected in this example. |
| vSwit ch Name | The name of the vSwitch. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter _ and cannot start with http:// or https:// . |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. The default IPv4 CIDR block is used in this example. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. Do Not Assign is selected in this example. |

| User | Guide·Quick start | Virtual Private Clou | d |
|---|---|---|---|

| Parameter | Description |
|---|---|
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter and cannot start with http:// or https:// . |

Step 3: Create a security group
1. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
2. Choose Net work & Securit y > Securit y Groups.
3. On the Securit y Groups page, click Creat e Securit y Group.
4. On the Creat e Securit y Group page, set the parameters and click Submit .

| Parameter | Description |
|---|---|
| Area |   |
| Organizat ion | Select the organization to which the security group belongs. |
| Resource Set | Select the resource set to which the security group belongs. |
| Region | Select the region where you want to deploy the security group. Make sure that the security group and the VPC belong to the same region. |
| Zone | Select the zone where you want to deploy the security group. |
| Basic Conf igurat ions |   |
| Sharing Scope | Select the sharing scope of the security group. Current Resource Set : Only the administrator of the current resource set can create resources for the security group. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can create resources for the security group. Current Organizat ion: Only the administrator of the current organization can create resources for the security group. Current Resource Set is selected in this example. |
| VPC | Select the VPC to which the security group belongs. |
| Securit y Group Name | Enter a name for the security group. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter _ and cannot start with http:// or https:// . |

| Parameter | Description |
|---|---|
| Descript ion | Enter a description for the security group. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter and cannot start with http:// or https:// . |

Step 4: Create an ECS instance
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, click VSwit ches.
3. In the top navigation bar, select the region where the vSwitch is deployed.
4. On the VSwit ches page, find the vSwitch and click Creat e ECS Inst ance in the Operat ion
column.
5. On the Creat e Inst ance page, set the parameters.
For more information about how to configure ECS instances, see the Creat e an ECS inst ance topic in the Quick st art chapter of ECS User Guide.

### Create an IPv6 VPC

This topic describes how to create a virtual private cloud (VPC) with an IPv6 CIDR block and how to create an Elastic Compute Service (ECS) instance that is assigned an IPv6 address in the VPC. This allows the ECS instance to access IPv6 services. Step 1: Create a VPC and a vSwitch Before you deploy cloud resources in a VPC, you must create a VPC and a vSwitch. Perform the following steps to create a VPC and a vSwitch:
1. Log on to the VPC console.
2. On the VPCs page, click Creat e VPC.
3. On the Creat e VPC page, set the parameters as described in the following table and click Submit .

| Parameter | Description |
|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |

| Parameter | Description |
|---|---|
| Sharing Scope | Select the sharing scope of the VPC. Current Resource Set : Only the administrator of the current resource set can use the VPC to create resources. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can use the VPC to create resources. Current Organizat ion: Only the administrator of the current organization can use the VPC to create resources. Current Resource Set is selected in this example. |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter and cannot start with _ http:// or https:// . VPCt est is used in this example. |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Cust om CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. Example: 192.168.0.0/16. In this example, 192.168.0.0/16 is used as the IPv4 CIDR block of the VPC. Not e After a VPC is created, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. In this example, Assign is selected. |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), commas (,), and colons (:). It must start with a _ letter and cannot start with http:// or https:// . |

4. Click Back t o Console. In the left-side navigation pane, click vSwit ch.
5. On the vSwit ch page, click Creat e vSwit ch.
6. On the vSwit ch page, set the parameters as described in the following table and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | The resource set to which the vSwitch belongs. |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone where you want to deploy the vSwitch. In a VPC, a vSwitch can be deployed only in one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e An instance can be attached only to one vSwitch. |
| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set : Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organizat ion: Only the administrator of the current organization can use the vSwitch to create resources. Current Resource Set is selected in this example. |
| VPC | Select the VPC in which you want to create the vSwitch. VPCtest is selected in this example. |
| Dedicat ed f or Out -of -cloud Physical Machines | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-met al servers in VPCs topic in Bare-metal Server Management Service User Guide. No is selected in this example. |
| vSwit ch Name | Enter a name for the vSwitch. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter and cannot _ start with http:// or https:// . |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. The default IPv4 CIDR block is used in this example. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. The default IPv6 CIDR block is used in this example. |

| Parameter | Description |
|---|---|
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must _ start with a letter and cannot start with http:// or https:// . |

Step 2: Create a security group Perform the following steps to create a security group:
1. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
2. Choose Net works and Securit y > Securit y Groups.
3. On the Securit y Groups page, click Creat e Securit y Group.
4. On the Creat e Securit y Group page, set security group parameters as described in the following
table and click Submit .

| Parameter | Description |   |   |
|---|---|---|---|
| Organizat ion | Select the organization to which the security group belongs. |   |   |
| Resource Set | Select the resource set to which the security group belongs. |   |   |
| Region | Select the region where you want to deploy the security group. Make sure that the security group and the VPC belong to the same region. |   |   |
| Zone | Select the zone where you want to deploy the security group. |   |   |
| Sharing Scope | Select the sharing scope of the security group. Current Resource Set : Only the administrator of the current resource set can create resources for the security group. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can create resources for the security group. Current Organizat ion: Only the administrator of the current organization can create resources for the security group. Current Resource Set is selected in this example. |   |   |
| VPC | Select the VPC to which the security group belongs. |   |   |
| Securit y Group Name | Enter a name for the security group. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), and colons (:). The name _ must start with a letter and cannot start with http:// or https: // . |   |   |
|   |   | https: |   |

|   | // |
|---|---|

| Parameter | Description |
|---|---|
| Descript ion | Enter a description for the security group. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and _ commas (,). It must start with a letter and cannot start with http:// or https:// . |

Step 3: Create and configure an ECS instance After the VPC and vSwitch are created, create an ECS instance and assign an IPv6 address to the ECS instance. Then, associate the assigned IPv6 address with the elastic network interface (ENI) of the ECS instance. Perform the following steps to create and configure an ECS instance:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, click vSwit ch.
3. Select the region where the vSwitch is deployed.
4. On the vSwit ch page, find the vSwitch that you have created and choose Creat e > ECS Inst ance
in the Act ions column.
5. On the Creat e ECS Inst ance page, set the parameters and click Submit .
In this example, Assign is selected for IPv6. This assigns an IPv6 IP address to the ECS instance. For more information about other parameters, see Creat e an ECS inst ance in Quick St art of the ECS User Guide.
6. Return to the Inst ances page, find the created instance and click its ID to view the assigned IPv6
address.
7. Configure a static IPv6 address.
If the image of your ECS instance supports DHCPv6, you do not need to manually configure a static IPv6 address. DHCPv6 enables automatic configuration of IPv6 addresses. Therefore, if the image of your ECS instance supports DHCPv6, the ECS instance automatically obtains an IPv6 address for communication within the private network. The following images support DHCPv6: Linux images: CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images If the image of your ECS instance does not support DHCPv6, you must manually configure an IPv6 address for your ECS instance. For more information, see the relevant documentation. Step 4: Purchase an IPv6 public bandwidth plan By default, IPv6 addresses can be used for communication only within private networks. If you want to enable mutual access between an IPv6 address and the Internet, you must purchase a public bandwidth plan for the IPv6 address. To purchase an IPv6 public bandwidth plan, perform the following steps:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, choose Int ernet Access > IPv6 Gat eway.
3. Select the region where the IPv6 gateway that you want to use is deployed.
4. On the IPv6 Gat eway page, find the IPv6 gateway that you want to use and click Manage in the
Act ions column.
5. In the left-side navigation pane, click IPv6 Int ernet Bandwidt h.
6. On the IPv6 Int ernet Bandwidt h page, find the IPv6 address that you want to use and click
Enable IPv6 Int ernet Bandwidt h in the Act ions column.
7. Select a bandwidth plan and click OK.
The bandwidth limit of an IPv6 gateway of Free, Enterprise, or Enhanced Edition is 2 Gbit/s. Step 5: Configure security group rules IPv4 and IPv6 addresses are independent of each other. If the current security group rules do not apply to your IPv6 services, you must configure security group rules for the ECS instances to regulate communication with IPv6 addresses. For more information about how to configure security group rules, see or the Add securit y group rules chapter in Securit y Groups of Elastic Compute Service User Guide. Step 6: Verify the network connectivity Log on to an ECS instance and ping an IPv6 service to verify the network connectivity.

## VPCs and VSwitches

### Overview

Before you can use cloud resources in a virtual private cloud (VPC), you must create a VPC and a vSwitch. You can create multiple vSwitches to divide a VPC into multiple subnets. By default, the subnets in a VPC can communicate with each other. VPCs and vSwitches VPCs are private networks dedicated to tenants. Not e You cannot directly deploy cloud resources in a VPC. You must deploy cloud resources in the vSwitches of a VPC. A vSwitch is a basic network device in a VPC and is used to connect cloud resources. You can deploy a VPC only in one region and cannot deploy a VPC across regions. However, a VPC covers all zones of the region to which the VPC belongs. You can create one or more vSwitches in a zone to divide a VPC into subnets. CIDR blocks and IP addresses VPCs support both IPv4 and IPv6. By default, VPCs use IPv4. You can enable IPv6 based on your business requirements. VPCs support the dual-stack mode. In dual-stack mode, resources in a VPC can communicate through both IPv4 and IPv6 addresses. IPv4 and IPv6 addresses are independent of each other. Therefore, you must configure routes and security groups for both IPv4 and IPv6 addresses. The following table lists the differences between IPv4 and IPv6 addresses.

| IPv4 VPC | IPv6 VPC |
|---|---|
| 32 binary digits. An IPv4 address appears as four decimal numbers separated by periods (.).Example: 192.168.1.11. | 128 binary digits. An IPv6 address appears as eight hexadecimal numbers separated by colons (:). Example: 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff. |
| By default, IPv4 is enabled. | You can enable IPv6 as needed. |
| The subnet mask of a VPC CIDR block can range from /8 to /24. | The subnet mask of a VPC CIDR block is /61. |
| The subnet mask of a vSwitch CIDR block can range from /16 to /29. | The subnet mask of a vSwitch CIDR block is /64. |
| You can specify an IPv4 CIDR block. | You cannot specify an IPv6 CIDR block. The system automatically assigns an IPv6 CIDR block to your VPC from the IPv6 address pool. |
| Supported by all instance types. | Not supported by some instance types. For more information, see Inst ance t ypes under What is ECS? in the Elastic Compute Service User Guide. |
| IPv4 elastic IP addresses (EIPs) are supported. | IPv6 EIPs are not supported. |
| VPN gateways and NAT gateways are supported. | VPN gateways and NAT gateways are not supported. |

By default, IPv4 and IPv6 addresses provided for VPCs support only communication over private networks. Cloud resources deployed in different vSwitches that belong to the same VPC can communicate with each other over private networks. To connect a VPC to another VPC or a data center, you can use Express Connect or VPN Gateway. To enable cloud resources in a VPC to communicate with the Internet, perform the following operations: IPv4 addresses You can configure NAT gateways or associate EIPs with Elastic Compute Service (ECS) instances in a VPC. This way, the ECS instances can communicate with the Internet through IPv4 addresses. IPv6 addresses To enable cloud resources in a VPC to communicate with the Internet through IPv6 addresses, you must purchase an IPv6 public bandwidth plan. You can configure egress-only rules for IPv6 addresses. This allows cloud resources in the VPC to access the Internet through IPv6 addresses. However, IPv6 clients cannot access the cloud resources over the Internet. Routes After you create a VPC, the system creates a system route table for the VPC and adds system routes to the route table. The system routes are used to route traffic within the VPC. A VPC has only one system route table. You cannot create or delete a system route table. You can create and associate custom route tables with vSwitches to facilitate network management. A vSwitch can be associated only with one route table. For more information, see Create a custom route table. If multiple route entries match the destination IP address, the route entry with the longest subnet mask is preferably used to determine the next hop. This ensures that the traffic is routed to the most precise destination. You can also add a custom route entry to route traffic to a specified destination. For more information, see Add a custom route entry.

### VPC management

#### Create a VPC

Virtual private clouds (VPCs) are private networks dedicated to tenants. You have full control over your VPC. For example, you can specify CIDR blocks, and configure route tables and gateways for your VPC. This topic describes how to create a VPC. Prerequisites Before you create a VPC, you must plan your networks. For more information, see Design networks.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where you want to deploy the VPC.
Not e You must deploy the VPC in the same region as the cloud resources that you want to deploy in this VPC.
3. On the VPC page, click Creat e VPC.
4. On the Creat e VPC page, set the parameters as described in the following table and click Submit .

| Parameter | Description |
|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Sharing Scope | Select the sharing scope of the VPC. Current Resource Set : Only the administrator of the current resource set can create resources for the shared VPC. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can use the VPC to create resources. Current Organizat ion: Only the administrator of the current organization can use the VPC to create resources. |

| Parameter | Description |
|---|---|
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter and cannot start with _ http:// or https:// . |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can select the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Cust om CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. Example: 192.168.0.0/24. Not e After a VPC is created, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. Not e If you select Do Not Assign, you can click Enable IPv6 CIDR Block in the IPv6 CIDR Block column on the VPC page after the VPC is created. In the Enable IPv6 CIDR Block dialog box, you can select Enable IPv6 CIDR Block of all VSwit ches in VPC to enable IPv6 for all vSwitches in the VPC. The system automatically creates a free IPv6 gateway for this VPC, and assigns an IPv6 CIDR block with the subnet mask /61, such as 2XX1:db8::/61. By default, IPv6 addresses can be used for communication only within private networks. If you want to enable mutual access between an IPv6 address and the Internet, you must purchase an Internet bandwidth plan for the IPv6 address. For more information, see the Act ivat e IPv6 Int ernet bandwidt h section of the Manage IPv6 Int ernet bandwidt h topic of the IPv6 gateway user guide. |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with a _ letter and cannot start with http:// or https:// . |

#### Add a secondary IPv4 CIDR block

After a virtual private cloud (VPC) is created, you can add a secondary IPv4 CIDR block to expand the VPC. Prerequisites A VPC is created. For more information, see Create a VPC. Context The IPv4 CIDR block that you configure when you create a VPC is the primary IPv4 CIDR block. After a VPC is created, the primary IPv4 CIDR block of the VPC cannot be modified. However, you can add a secondary IPv4 CIDR block to expand the VPC. After you add a secondary IPv4 CIDR block to the VPC, both the primary and secondary IPv4 CIDR blocks are in effect. You can create a vSwitch with the primary IPv4 CIDR block or the secondary IPv4 CIDR block. However, each vSwitch belongs to only one VPC CIDR block. The system automatically adds a vSwitch route to the VPC route table when you create a vSwitch with the primary IPv4 CIDR block or a secondary IPv4 CIDR block. The destination CIDR block of the vSwitch route is the CIDR block with which the vSwitch is created. The CIDR block range cannot be the same as or larger than those of other routes in the route table of the VPC. Not e You can add only one secondary IPv4 CIDR block to a VPC and cannot increase the quota.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the VPC page, find the VPC and click Manage in the Act ions column.
4. On the Net work segment management tab, click Add IPv4 CIDR.
5. In the Add Secondary CIDR dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| VPC | Displays the VPC to which you want to add the secondary IPv4 CIDR block. |

| Parameter | Description |
|---|---|
| Secondary CIDR | Select a method to configure the secondary IPv4 CIDR block: Def ault CIDR Block: You can specify one of the following standard IPv4 CIDR blocks as the secondary IPv4 CIDR block: 192.168.0.0/16 and 172.16.0.0/12. Cust om CIDR Block: You can specify one of the following standard IPv4 CIDR blocks or one of their subnets as the secondary IPv4 CIDR block: 192.168.0.0/16 and 172.16.0.0/12. When you add a secondary IPv4 CIDR block, take note of the following limits: The CIDR block cannot start with 0. The mask must be 8 to 24 bits in length. The secondary IPv4 CIDR block cannot overlap with the primary IPv4 CIDR block or an existing secondary IPv4 CIDR block. For example, if the primary IPv4 CIDR block of a VPC is 192.168.0.0/16, you cannot specify one of the following CIDR blocks as a secondary IPv4 CIDR block: A CIDR block larger than 192.168.0.0/16, for example, 192.168.0.0/8. 192.168.0.0/16. A CIDR block smaller than 192.168.0.0/16, for example, 192.168.0.0/24. |

#### Delete a secondary IPv4 CIDR block

You can delete the secondary IPv4 CIDR block of a virtual private cloud (VPC). However, you cannot delete the primary IPv4 CIDR block of a VPC. Prerequisites Before you delete a secondary IPv4 CIDR block, make sure that the vSwitches created with the secondary IPv4 CIDR block are deleted. For more information, see Delete a vSwitch.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the Virt ual Privat e Clouds page, find the VPC that you want to manage, and click
Management in the Operat ion column.
4. On the Net work segment management tab, find the secondary IPv4 CIDR block and click Delet e
in the Operat ion column.
5. In the message that appears, click OK.

#### Modify the name and description of a VPC

This topic describes how to modify the name and description of a VPC.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the Virt ual Privat e Clouds page, find the VPC that you want to manage, and click
Management in the Operat ion column.
4. In the VPC Basic Inf ormat ion section, click
next to VPC name. In the dialog box that appears, enter a new name and click OK. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
5. In the VPC Basic Inf ormat ion section, click
next to Descript ion. In the dialog box that appears, enter a new description and click OK. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://` .

#### Delete a VPC

This topic describes how to delete a virtual private cloud (VPC). After you delete a VPC, vRouters and route tables that are associated with the VPC are also deleted. Prerequisites Before you delete a VPC, make sure that the following requirements are met: No vSwitch exists in the VPC. If the VPC contains a vSwitch, you must delete the vSwitch before you delete the VPC. For more information, see Delete a vSwitch. No IPv6 gateway exists in the VPC. If an IPv6 gateway exists in the VPC, delete the IPv6 gateway first. For more information, see the Delet e an IPv6 gat eway topic in the Manage IPv6 gat eways chapter of IPv6 Gateway User Guide.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the Virt ual Privat e Clouds page, find the VPC that you want to delete, and click Delet e in the
Operat ion column.
4. In the Delet e a propriet ary net work dialog box, click OK.

### VSwitch management

#### Create a vSwitch

A vSwitch is a basic network component that connects different cloud resources in a virtual private cloud (VPC). Context After you create a VPC, you can create vSwitches to create one or more subnets for the VPC. vSwitches in the same VPC can communicate with each other. Cloud resources must be deployed in vSwitches. You can deploy applications in vSwitches that belong to different zones to improve service availability. Not e vSwitches do not support multicasting or broadcasting.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. In the top navigation bar, select the region of the VPC where you want to create a vSwitch.
4. On the VSwit ches page, click Creat e a swit ch.
5. On the Creat e vSwit ch page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone where you want to deploy the vSwitch. In a VPC, a vSwitch can be deployed only in one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e An instance can be attached only to one vSwitch. |
| Sharing Scope | Select the sharing scope of the vSwitch. Current Resource Set : Only the administrator of the current resource set can create resources in the shared vSwitch. Current Organizat ion and Subordinat e Organizat ions: Only the administrators of the current organization and its subordinate organizations can create resources in the shared vSwitch. Current Organizat ion: Only the administrator of the current organization can use the vSwitch to create resources. |
| VPC | Select the VPC in which you want to create the vSwitch. |
| Dedicat ed f or Bare Met al Inst ances | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-met al servers in VPCs topic in Bare-metal Server Management Service User Guide. |
| vSwit ch Name | Enter a name for the vSwitch. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter and cannot _ start with http:// or https:// . |

| Parameter | Description |
|---|---|
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. You must specify the IP address range of the vSwitch in CIDR notation. The subnet mask must be 16 to 29 bits in length, which specifies that 8 to 65,536 IP addresses are available. The CIDR block of a vSwitch must be a proper subset of the CIDR block of the VPC to which the vSwitch belongs. The first IP address and last three IP addresses of a vSwitch CIDR block are reserved. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The CIDR block of a vSwitch cannot be the same as the destination CIDR block in a route entry of the VPC to which the vSwitch belongs. However, the CIDR block of the vSwitch can be a subset of the destination CIDR block of the route entry. After a vSwitch is created, you cannot modify its CIDR block. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. You must check whether IPv6 is enabled for the specified VPC. If IPv6 is not enabled, you cannot assign an IPv6 CIDR block to the vSwitch. If IPv6 is enabled for the VPC, you can enter a decimal number that ranges from 0 to 7 to define the last 8 bits of the IPv6 CIDR block of the vSwitch. For example, if the IPv6 CIDR block of the VPC is 2XX1:db8::/64, you can enter 255 to define the last 8 bits of the IPv6 CIDR block. In this case, the IPv6 CIDR block of the vSwitch is 2XX1:db8:ff::/64. ff is the hexadecimal value of 255. Not e If IPv6 is not enabled when you create a vSwitch, you can enable IPv6 after the vSwitch is created. To do this, go to the VSwit ches page, click Enable IPv6 CIDR in the IPv6 CIDR Block column. |
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must _ start with a letter and cannot start with http:// or https:// . |

#### Create cloud resources

You cannot directly deploy cloud resources in a virtual private cloud (VPC). You must deploy cloud resources in a vSwitch in a VPC. This topic describes how to create cloud resources in a vSwitch. You can create Elastic Compute Service (ECS), Server Load Balancer (SLB), and ApsaraDB RDS instances in a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. In the top navigation bar, select the region of the VPC to which the vSwitch belongs.
4. On the VSwit ches page, you can create the following cloud resources.
Click Creat e ECS Inst ance in the Operat ion column, and then create an ECS instance on the Creat e Inst ance page. For more information about how to configure ECS instances, see the Creat e an ECS inst ance topic in the Quick st art chapter of ECS User Guide. In the Operat ion column, choose
> Creat e SLB Inst ance, and then create an SLB instance
on the Creat e SLB Inst ance page. For more information about how to configure SLB instances, see the Creat e an SLB inst ance topic in the Quick st art chapter of SLB User Guide. In the Operat ion column, choose
> Creat e ApsaraDB RDS Inst ance, and then create an
ApsaraDB RDS instance on the Creat e Inst ance page. For more information about how to configure ApsaraDB RDS instances, see the Creat e an ApsaraDB RDS inst ance topic in the Quick st art chapter of ApsaraDB RDS User Guide.

#### Modify the information about a vSwitch

This topic describes how to modify the name and description of a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. In the top navigation bar, select the region of the VPC to which the vSwitch belongs.
4. On the VSwit ches page, find the vSwitch that you want to manage and click Management in the
Operat ion column.
5. In the Swit ch Basic inf ormat ion section, click
next to Swit ch name. In the dialog box that appears, enter a new name. The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter.
6. In the Swit ch Basic inf ormat ion section, click
next to Descript ion. In the dialog box that appears, enter a new description. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://` .

#### Delete a vSwitch

This topic describes how to delete a vSwitch. After you delete a vSwitch, you cannot deploy cloud resources in it. Prerequisites Before you delete a vSwitch, make sure that the following requirements are met: Cloud resources created in the vSwitch are deleted, such as Elastic Compute Service (ECS), Server Load Balancer (SLB), and ApsaraDB RDS instances. All resources associated with the vSwitch are deleted, such as high-availability virtual IP addresses (HAVIPs) and SNAT entries.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. Select the virtual private cloud (VPC) to which the vSwitch belongs.
4. On the VSwit ches page, find the vSwitch that you want to delete and click Delet e in the
Operat ion column.
5. In the Delet e vSwit ch message, click OK.

## Route tables

### Overview

After you create a virtual private cloud (VPC), the system automatically creates a system route table for the VPC and adds system routes to the route table. The system routes are used to route traffic within the VPC. You cannot create or delete system routes. However, you can create custom routes to route traffic from a specified CIDR block to a specified destination. Route tables After you create a VPC, the system creates a system route table to manage routes of the VPC. By default, vSwitches in the VPC use this route table. You cannot create or delete the system route table of a VPC. However, you can create a custom route table and associate it with a vSwitch to manage your network in a more flexible way. When you associate a vSwitch with a custom route table, the vSwitch is automatically disassociated from the system route table. For more information, see Add subnet routes to a route table. Each entry in a route table is a route entry. A route entry specifies the destination to which network traffic is routed and consists of the destination CIDR block, next hop type, and next hop. Route entries include system route entries and custom route entries. System routes After you create a VPC, the system automatically adds the following system routes to the route table: A route entry with a destination CIDR block of 100.64.0.0/10. This route is used for communication among cloud resources within the VPC. Route entries whose destination CIDR blocks are the same as the CIDR blocks of the vSwitches in the VPC. These routes are used for communication among cloud resources within the vSwitches. For example, if you create a VPC whose CIDR block is 192.168.0.0/16 and two vSwitches whose CIDR blocks are 192.168.1.0/24 and 192.168.0.0/24, three system routes are automatically added to the route table of the VPC. The following table describes the system routes.

| Destination CIDR block | Next hop | Type |
|---|---|---|
| 100.64.0.0/10 | - | System route |
| 192.168.1.0/24 | - | System route |
| 192.168.0.0/24 | - | System route |

Custom routes You can add custom routes to replace system routes or route traffic to a specified destination. You can specify the following types of next hops when you create a custom route: Elastic Compute Service (ECS) instance: Traffic that is destined for the destination CIDR block is routed to a specified ECS instance in the VPC. You can select this type if the application deployed on the ECS instance needs to access the Internet or other applications. VPN gateway: Traffic destined for the destination CIDR block is routed to a specified VPN gateway. You can select this type if you want to connect a VPC to another VPC or an on-premises network through the VPN gateway. NAT gateway: Traffic destined for the destination CIDR block is routed to a specified NAT gateway. You can select this type if you want to connect a VPC to the Internet through the NAT gateway. Router interface (to VPC): Traffic that is destined for the destination CIDR block is routed to a specified VPC. You can select this type if you want to connect two VPCs through Express Connect circuits. Router interface (to VBR): Traffic that is destined for the destination CIDR block is routed to a specified virtual border router (VBR). You can select this type if you want to connect a VPC to an on-premises network through Express Connect circuits. Secondary ENI: Traffic that is destined for the destination CIDR block is routed to a specified secondary elastic network interface (ENI). IPv6 gateway: Traffic that is destined for the destination CIDR block is routed to a specified IPv6 gateway. You can select this type if you want to implement IPv6 communication through an IPv6 gateway. IPv6 routes If IPv6 is enabled for your VPC, the following route entries are automatically added to the system route table of the VPC: A custom route entry whose destination CIDR block is ::/0 and whose next hop is the IPv6 gateway. Cloud resources deployed in the VPC use this route to access the Internet through IPv6 addresses. A system route entry of which the destination CIDR block is the IPv6 CIDR block of a vSwitch. This route is used for communication within the vSwitch. Not e If you create a custom route table and associate the custom route table with a vSwitch for which IPv6 is enabled, you must add a custom route entry whose destination CIDR block is ::/0 and next hop is the IPv6 gateway instance. For more information, see Add a custom route entry. Routing rules If multiple route entries match the destination IP address, the route entry with the longest subnet mask is preferably used to determine the next hop. This ensures that the traffic is routed to the most precise destination. For example, the following table describes the route table of a VPC.

| Destination CIDR block | Next hop type | Next hop | Route entry type |
|---|---|---|---|
| 100.64.0.0/10 | - | - | System route |
| 192.168.0.0/24 | - | - | System route |
| 0.0.0.0/0 | Instance | i-12345678 | Custom route |

| irtual Private Cloud |   |   | User Guide·Route table |
|---|---|---|---|

| Destination CIDR block | Next hop type | Next hop | Route entry type |
|---|---|---|---|
| 10.0.0.0/24 | Instance | i-87654321 | Custom route |

| at are destined for 100.64.0.0/10 an ntries that are destined for 0.0.0.0/0 is destined for 0.0.0.0/0 is routed to 10.0.0.0/24 is routed to the ECS insta ic destined for 10.0.0.1 is routed to 10.0.1.1 is routed to the ECS instanc | 100.64.0.0/10 |   | an |
|---|---|---|---|
|   |   | 0.0.0.0/0 |   |
| 10.0.1.1 |   |   |   |

| 192.168.0.0/24 |   |   | are system are custom |
|---|---|---|---|
|   | 10.0.0.0/24 |   |   |
|   |   | i-12345678 |   |

|   | 0.0.0.0/0 |
|---|---|
| 10.0.0.0/24 |   |
|   | 10.0.0.1 |

Examples You can add custom route entries to a route table to control inbound and outbound traffic that is transmitted over the VPC. Routing within a VPC The following figure shows a NAT gateway that is deployed on an ECS instance (ECS01) in a VPC. To enable the cloud resources in the VPC to access the Internet through the ECS instance, you must add the following route entry to the route table.

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

### Create a custom route table

This topic describes how to use route tables. A route table consists of route entries. Each route entry specifies the destination to which network traffic is routed. You can create a custom route table to manage the inbound and outbound network traffic of subnets in a virtual private cloud (VPC). Create a custom route table
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region where you want to create the route table.
4. On the Rout e T ables page, click Creat e rout ing t able.
5. On the Creat e Rout e T able page, set the following parameters and click OK.

| Parameter | Description |   |   |
|---|---|---|---|
| VPC | Select the VPC to which the route table belongs. |   |   |
| Name | Enter a name for the route table. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). It must start with a letter. _ |   |   |
| Descript ion | Enter a description for the route table. The description must be 2 to 256 characters in length. It cannot start with http: // or https:// . |   |   |
|   |   | http: |   |

|   | // |
|---|---|

After you create a custom route table, you can go to the Rout e T ables page to view the route table. The type of route table is Cust om, which is displayed in the Rout ing t able t ype column. Disassociate a route table from a vSwitch You can disassociate a custom route table from a vSwitch. After a custom route table is disassociated from a vSwitch, the vSwitch is automatically associated with the system route table.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table that you want to manage
belongs.
4. On the Rout e T ables page, find the route table that you want to manage and click its ID.
5. In the Rout ing t able Basic inf ormat ion section, click the Bound swit ch tab. Find the vSwitch
that you want to manage and click Unbind in the Operat ion column.
6. In the Unbind t he swit ch message, click OK.
Delete a custom route table You can delete custom route tables. However, you cannot delete system route tables. If the custom route table that you want to delete is associated with a vSwitch, you must first disassociate the custom route table from the vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table that you want to manage
belongs.
4. On the Rout e T ables page, find the route table that you want to delete and click Delet e in the
Operat ion column.
5. In the Delet e Rout e T able message, click OK.

### Add a custom route entry

This topic describes how to add a custom route entry. After you create a virtual private cloud (VPC), the system creates a system route table and adds system route entries to the route table. The system route entries are used to route traffic within the VPC. You cannot create or delete system route entries. However, you can create custom route entries to route traffic destined for specified CIDR blocks to specified destinations. Context Each item in a route table is a route entry. A route entry consists of the destination CIDR block, next hop type, and next hop. A route entry specifies the destination of network traffic. Route entries include system route entries and custom route entries. You can add custom route entries to the system route table and custom route tables.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table that you want to manage
belongs.
4. On the Rout e T ables page, find the route table and click Management in the Operat ion column.
5. On the Rout ing ent ry list tab, click Add rout e ent ry.
6. In the Add rout e ent ry dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| T arget net work segment | Enter a destination CIDR block for the route entry. IPv4 CIDR Block: The destination CIDR block is an IPv4 CIDR block. IPv6 CIDR Block: The destination CIDR block is an IPv6 CIDR block. |

| Parameter | Description |
|---|---|
| Next hop t ype | Select the next hop type. Valid values: ECS inst ance: Traffic destined for the specified CIDR block is routed to the specified ECS instance. Select this type if you want to route traffic to a specified ECS instance for centralized traffic forwarding and management. For example, you can configure an ECS instance as the Internet-facing gateway to route traffic from other ECS instances to the Internet. Highly available virt ual IP: Traffic destined for the specified CIDR block is routed to the high-availability virtual IP address (HAVIP) that you select. VPN gat eway: Traffic destined for the specified CIDR block is routed to the specified VPN gateway. NAT Gat eway: Traffic destined for the specified CIDR block is routed to the specified NAT gateway. Auxiliary ENI: Traffic destined for the specified CIDR block is routed to the specified secondary elastic network interface (ENI). Rout er Int erf ace (VPC Direct ion): Traffic destined for the specified CIDR block is routed to the VPC that you select. Select this type if you want to connect VPCs through Express Connect circuits. Rout er Int erf ace (Border Rout er Direct ion): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a virtual border router (VBR). Select this type if you want to connect the VPC to a data center through Express Connect circuits. If you select Router Interface (Border Router Direction), you must also select a routing mode: Common rout e: Select an associated router interface. Primary/st andby Rout e: Select two instances as the next hop. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes over when the active route fails to pass the health check. Load rout ing: Select two to four router interfaces as the next hops. The peer router of each router interface must be a VBR. You can set the weight of each instance to an integer from 1 to 255. The default value is 100. The weights of the instances must be the same. This way, traffic can be evenly distributed to the next-hop instances. IPv6 Gat eway: Traffic destined for the specified CIDR block is routed to the specified IPv6 gateway. Not e If you set T arget net work segment to IPv6 CIDR Block, you can select IPv6 Gat eway and Rout er Int erf ace (Border Rout er Direct ion) for Next hop t ype. |

| Parameter | Description |
|---|---|
| ECS Inst ance, VPN gat eway, NAT Gat eway, Auxiliary ENI, Highly available virt ual IP, Rout er Int erf ace (VPC Direct ion), Rout er Int erf ace (Border Rout er Direct ion), and IPv6 Gat eway | Select an instance as the next hop. |

### Export route entries

This topic describes how to export route entries from a route table. The exported route entries can be stored as backups on your computer.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click Management in the Operat ion column.
5. In the Rout e T able Det ails section, click the Rout e Ent ry List tab, and then click Export .
The route entries are exported to a .csv file on your computer.

### Modify the information about a

route table This topic describes how to modify the name and description of a route table.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click Management in the Operat ion column.
5. In the Rout ing t able Basic inf ormat ion section, click
next to Rout ing t able name. In the dialog box that appears, enter a new name for the route table and click OK. The name must be 2 to 128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter.
6. In the Rout ing t able Basic inf ormat ion section, click
next to Descript ion. In the dialog box that appears, enter a new description for the route table and click OK. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://` .

### Delete a custom route entry

This topic describes how to delete a custom route entry. A route table consists of one or more route entries. Each route entry specifies the destination network to which traffic is routed. You can delete custom route entries. However, you cannot delete system route entries.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. In the Rout e T able Det ails section, click Add Rout e Ent ry.
5. On the Rout e Ent ry List tab, find the custom route that you want to delete and click Delet e in
the Act ions column.
6. In the Delet e Rout e Ent ry message, click OK.

### Subnet routing

You can create a custom route table in a virtual private cloud (VPC) and add custom routes to the custom route table. Then, you can associate the custom route table with a vSwitch to control the traffic of the vSwitch. This facilitates network management. The preceding operations are referred to as subnet routing. Prerequisites A VPC is created. For more information, see Create a VPC. Step 1: Create a custom route table
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region where you want to create the route table.
4. On the Rout e T ables page, click Creat e Rout e T able.
5. In the Creat e Rout e T able panel, configure the route table as described in the following table
and click OK.

| Parameter | Description |
|---|---|
| VPC | Select the VPC to which the route table belongs. |
| Name | Enter a name for the route table. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). The name must start with a letter. _ |

| Parameter | Description |   |   |
|---|---|---|---|
| Descript ion | Enter a description for the route table. The description must be 2 to 256 characters in length, and cannot start with htt p:// or https:// . |   |   |
|   |   | htt |   |

|   | p:// |
|---|---|

After you create a custom route table, you can go to the Rout e T ables page to view the route table. The type of route table is displayed as Cust om in the Rout e T able T ype column.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region where you want to create the route table.
4. On the Rout e T ables page, click Creat e rout ing t able.
5. On the Creat e Rout e T able page, set the following parameters and click OK.

| Parameter | Description |   |   |
|---|---|---|---|
| VPC | Select the VPC to which the route table belongs. |   |   |
| Name | Enter a name for the route table. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). It must start with a letter. _ |   |   |
| Descript ion | Enter a description for the route table. The description must be 2 to 256 characters in length. It cannot start with http: // or https:// . |   |   |
|   |   | http: |   |

|   | // |
|---|---|

After you create a custom route table, you can go to the Rout e T ables page to view the route table. The type of route table is Cust om, which is displayed in the Rout ing t able t ype column. Step 2: Add a custom route to the custom route table
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click Manage in the Act ions column.
5. In the Rout e T able Det ails section, click Add Rout e Ent ry.
6. In the Add Rout e Ent ry panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Dest inat ion CIDR Block | Enter a destination CIDR block for the route entry. IPv4 CIDR Block: The destination CIDR block is an IPv4 CIDR block. IPv6 CIDR Block: The destination CIDR block is an IPv6 CIDR block. |

| Parameter | Description |
|---|---|
| Next Hop T ype | Select the next hop type. Valid values: ECS Inst ance: Traffic destined for the specified CIDR block is routed to the specified Elastic Compute Service (ECS) instance. Select this type if you want to route traffic to an ECS instance for centralized traffic forwarding and management. For example, you can configure an ECS instance as the Internet-facing gateway to route traffic from other ECS instances to the Internet. HaVip: Traffic destined for the specified CIDR block is routed to the high- availability virtual IP address (HAVIP) that you select. VPN Gat eway: Traffic destined for the specified CIDR block is routed to the specified VPN gateway. NAT Gat eway: Traffic destined for the specified CIDR block is routed to the specified NAT gateway. Secondary ENI: Traffic destined for the specified CIDR block is routed to the secondary elastic network interface (ENI) that you select. Rout er Int erf ace (T o VPC): Traffic destined for the specified CIDR block is routed to the VPC that you select. Select this type if you want to connect VPCs through Express Connect circuits. Rout er Int erf ace (T o VBR): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a virtual border router (VBR). Select this type if you want to connect the VPC to a data center through Express Connect circuits. If you select Router Interface (To VBR), you must also select a routing mode: General Rout ing: Select an associated router interface. Act ive/St andby Rout ing: Select two instances as the next hop. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes over when the active route fails to pass the health check. Load Balancing Rout ing: Select two to four router interfaces as the next hop. The peer router of each router interface must be a VBR. You can set the weight of each instance to an integer from 1 to 255. The default value is 100. The weights of the instances must be the same. This way, traffic can be evenly distributed to the next-hop instances. IPv6 Gat eway: Traffic destined for the specified CIDR block is routed to the specified IPv6 gateway. Not e If you set Dest inat ion CIDR Block to IPv6 CIDR Block, you can select IPv6 Gat eway and Rout er Int erf ace (T o VBR) for Next Hop T ype. |

| Parameter | Description |
|---|---|
| ECS Inst ance, VPN Gat eway, NAT Gat eway, Secondary ENI, HaVip, Rout er Int erf ace (T o VPC), Rout er Int erf ace (T o VBR), IPv6 Gat eway | Select an instance as the next hop. |

1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table that you want to manage
belongs.
4. On the Rout e T ables page, find the route table and click Management in the Operat ion column.
5. On the Rout ing ent ry list tab, click Add rout e ent ry.
6. In the Add rout e ent ry dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| T arget net work segment | Enter a destination CIDR block for the route entry. IPv4 CIDR Block: The destination CIDR block is an IPv4 CIDR block. IPv6 CIDR Block: The destination CIDR block is an IPv6 CIDR block. |

| Parameter | Description |
|---|---|
| Next hop t ype | Select the next hop type. Valid values: ECS inst ance: Traffic destined for the specified CIDR block is routed to the specified ECS instance. Select this type if you want to route traffic to a specified ECS instance for centralized traffic forwarding and management. For example, you can configure an ECS instance as the Internet-facing gateway to route traffic from other ECS instances to the Internet. Highly available virt ual IP: Traffic destined for the specified CIDR block is routed to the high-availability virtual IP address (HAVIP) that you select. VPN gat eway: Traffic destined for the specified CIDR block is routed to the specified VPN gateway. NAT Gat eway: Traffic destined for the specified CIDR block is routed to the specified NAT gateway. Auxiliary ENI: Traffic destined for the specified CIDR block is routed to the specified secondary elastic network interface (ENI). Rout er Int erf ace (VPC Direct ion): Traffic destined for the specified CIDR block is routed to the VPC that you select. Select this type if you want to connect VPCs through Express Connect circuits. Rout er Int erf ace (Border Rout er Direct ion): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a virtual border router (VBR). Select this type if you want to connect the VPC to a data center through Express Connect circuits. If you select Router Interface (Border Router Direction), you must also select a routing mode: Common rout e: Select an associated router interface. Primary/st andby Rout e: Select two instances as the next hop. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes over when the active route fails to pass the health check. Load rout ing: Select two to four router interfaces as the next hops. The peer router of each router interface must be a VBR. You can set the weight of each instance to an integer from 1 to 255. The default value is 100. The weights of the instances must be the same. This way, traffic can be evenly distributed to the next-hop instances. IPv6 Gat eway: Traffic destined for the specified CIDR block is routed to the specified IPv6 gateway. Not e If you set T arget net work segment to IPv6 CIDR Block, you can select IPv6 Gat eway and Rout er Int erf ace (Border Rout er Direct ion) for Next hop t ype. |

| Parameter ECS Inst ance, VPN | Description |
|---|---|
| gat eway, NAT Gat eway, Auxiliary ENI, Highly available virt ual IP, Rout er Int erf ace (VPC Direct ion), Rout er Int erf ace (Border Rout er Direct ion), and IPv6 Gat eway | Select an instance as the next hop. |

Step 3: Associate the custom route table with a vSwitch You can associate the custom route table with a vSwitch to manage the routes of the vSwitch. A vSwitch can be associated only with one system route table or one custom route table. Perform the following operations to associate the custom route table with a vSwitch:
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table that you want to manage
belongs.
4. On the Rout e T ables page, find the custom route table that you want to manage and click its ID.
5. In the Rout ing t able Basic inf ormat ion section, click the Bound Swit ch tab and click Bind
swit ch.
6. In the Bind swit ch dialog box, select the vSwitch that you want to associate and click OK.

## HAVIPs

### Overview

High-availability virtual IP addresses (HAVIPs) are private IP addresses that can be created and released as independent resources. You can use HAVIPs with high-availability (HA) software such as Keepalived to provide active/standby services. This improves the availability of your services. Introduction Each Elastic Compute Service (ECS) instance is assigned a private IP address as the primary IP address. You can associate HAVIPs with an ECS instance to increase the number of private IP addresses available for the ECS instance. Both the primary IP address and HAVIPs of an ECS instance can be used to access networks. In addition, you can use HAVIPs with HA software such as Keepalived to provide active/standby services. This improves the availability of your services. You can associate an HAVIP with ECS instances by using the following methods: Directly associate an HAVIP with ECS instances. Each HAVIP can be associated with two ECS instances. After an HAVIP is associated with ECS instances, the ECS instances can send Address Resolution Protocol (ARP) messages to advertise the HAVIP. After the ECS instances advertise the HAVIP, one of the ECS instances serves as the primary instance, and the other ECS instance serves as the secondary instance. If the primary ECS instance is down, the secondary ECS instance takes over to provide services. Attach secondary elastic network interfaces (ENIs) to ECS instances. Then, associate the HAVIP with the secondary ENIs. Each HAVIP can be associated with ENIs of two ECS instances. After the HAVIP is associated with the ENIs, the ECS instances can send ARP messages to advertise the HAVIP. After the ECS instances advertise the HAVIP, one of the ECS instances serves as the primary instance, and the other ECS instance serves as the secondary instance. If the primary ECS instance is down, the secondary ECS instance takes over to provide services. Not e Before you associate an HAVIP with secondary ENIs, make sure that the secondary ENIs are attached to two ECS instances. HAVIPs have the following features: HAVIPs are floating private IP addresses and are not statically assigned to specified ECS instances. HAVIPs can be associated with or disassociated from ECS instances through ARP announcements. An HAVIP can be associated only with ECS instances or ENIs that belong to the same vSwitch. You can associate each HAVIP with two ECS instances or two secondary ENIs. However, you cannot associate an HAVIP with an ECS instance and a secondary ENI at the same time. Scenarios HAVIPs support flexible configurations in the following scenarios: Scenario 1: Internal-facing HA services In the following figure, two ECS instances are assigned the same HAVIP. Keepalived is configured for the ECS instances to provide an internal-facing HA service. Other instances in the same virtual private cloud (VPC) can access this service. The HAVIP serves as the service address. If the primary ECS instance is down, the secondary ECS instance takes over. This improves the availability of your services. Scenario 2: Internet-facing HA services In the following figure, two ECS instances are assigned the same HAVIP. Keepalived is configured and the HAVIP is associated with an elastic IP address (EIP) for the ECS instances to provide an Internetfacing HA service. The EIP that is associated with the HAVIP serves as the service address. If the primary ECS instance is down, the secondary ECS instance takes over. This improves the availability of your services. Limits Before you use HAVIPs, take note of the following limits.

| Item | Limit |
|---|---|
| Number of HAVIPs that can be created in each VPC | 5 |
| Number of HAVIPs that can be associated with each ECS instance | 5 |
| Number of HAVIPs that can be associated with each ENI | 5 |
| Number of ECS instances that can be associated with each HAVIP | 2 |
| Number of ENIs that can be associated with each HAVIP | 2 |
| Number of route entries that point an HAVIP in each VPC | 5 |

| Item | Limit |
|---|---|
| Whether HAVIPs support broadcasting or multicasting | N/A Not e HAVIPs support only unicasting. To implement high availability through third-party software such as keepalived, you must modify the configuration file to change the communication method to unicasting. |

### Create an HAVIP

A high-availability virtual IP address (HAVIP) is a private IP address that can be created and released as an independent resource. This topic describes how to create an HAVIP in the console. Prerequisites A virtual private cloud (VPC) and vSwitches are created. For more information, see Create a VPC and Create a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where you want to create the HAVIP.
4. On the HaVip page, click Creat e HaVip.
5. On the Creat e HAVIP page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the HAVIP belongs. |
| Resource Set | Select the resource set to which the HAVIP belongs. |
| Region | Select the region where you want to create the HAVIP. |
| VPC | Select the VPC to which the HAVIP belongs. |
| vSwit ch | Select the vSwitch to which the HAVIP that you want to create belongs. |
| Privat e IP Address | Specify a private IP address for the HAVIP. Not e You must specify an idle private IP address that falls within the CIDR block of the vSwitch. |

### Associate HAVIPs with backend

cloud resources

#### Associate an HAVIP with an ECS instance

You can associate a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). This way, the ECS instance can advertise the HAVIP and obtain multiple private IP addresses through Address Resolution Protocol (ARP). An HAVIP can be associated with at most two ECS instances. Prerequisites An ECS instance is created. For more information, see the Creat e an inst ance topic in the Quick St art chapter of ECS User Guide. Context An HAVIP can be associated with two ECS instances or two elastic network interfaces (ENIs). However, you cannot associate an HAVIP with an ECS instance and an ENI at the same time.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the High-availabilit y Virt ual IP Address page, find the HAVIP and click Manage in the
Act ions column.
5. In the Binding resource section, find Elast ic net work card (Act ive) or Elast ic net work card
(St andby) and click Bind immediat ely.
6. In the dialog box that appears, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Binding t ype | Select the type of resource with which you want to associate the HAVIP. Supported resource types are: ECS inst ance Elast ic net work card In this example, ECS inst ance is selected. |
| Binding resource | Select the ECS instance with which you want to associate the HAVIP. The ECS instance must meet the following requirements: The ECS instance is deployed in a VPC. The ECS instance and the HAVIP belong to the same vSwitch. |

#### Associate an HAVIP with an ENI

You can associate a high-availability virtual IP address (HAVIP) with an elastic network interface (ENI). This way, an Elastic Compute Service (ECS) instance can advertise the HAVIP and obtain multiple private IP addresses through Address Resolution Protocol (ARP). Prerequisites An ENI is created. For more information, see the Creat e an ENI topic in the Elast ic Net work Int erf ace chapter of ECS User Guide. Context An HAVIP can be associated with two ECS instances or two ENIs. However, you cannot associate an HAVIP with an ECS instance and an ENI at the same time.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the High-availabilit y Virt ual IP Address page, find the HAVIP and click Manage in the
Act ions column.
5. In the Binding resource section, find Elast ic net work card (Act ive) or Elast ic net work card
(St andby) and click Bind immediat ely.
6. In the dialog box that appears, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Binding t ype | Select the type of resource with which you want to associate the HAVIP. Supported resource types are: ECS inst ance Elast ic net work card In this example, Elast ic net work card is selected. |
| Bind resource | Select the ENI with which you want to associate the HAVIP. The ENI and HAVIP must belong to the same vSwitch. |

### Associate an HAVIP with an EIP

You can associate a high-availability virtual IP address (HAVIP) with an elastic IP address (EIP). This way, the HAVIP can provide services over the Internet by using the EIP. Prerequisites An EIP is created. For more information, see the Create an EIP topic in Quick St art of Elast ic IP Address User Guide.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the High-availabilit y Virt ual IP Address page, find the HAVIP and click Bind elast ic public
net work IP in the Act ions column.
5. In the dialog box that appears, select the EIP with which you want to associate the HAVIP and click
OK. The EIP must meet the following requirements: The EIP and the HAVIP must be deployed in the same region. The EIP must be in the Available state.

### Disassociate HAVIPs from

backend cloud resources

#### Disassociate an HAVIP from an ECS

instance This topic describes how to disassociate a high-availability virtual private IP address (HAVIP) from an Elastic Compute Service (ECS) instance. After you disassociate an HAVIP from an ECS instance, the ECS instance cannot send Address Resolution Protocol (ARP) messages to advertise the HAVIP.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip page, find the HAVIP that you want to manage and click Manage in the Act ions
column.
5. In the Resources section, find the ECS instance that you want to manage and click Unbind.
6. In the message that appears, click OK.

#### Disassociate an HAVIP from an ENI

This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic network interface (ENI). After you disassociate an HAVIP from an ENI, the Elastic Compute Service (ECS) instance with which the ENI is associated cannot send Address Resolution Protocol (ARP) messages to advertise the HAVIP.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip page, find the HAVIP that you want to disassociate and click Manage in the Act ions
column.
5. In the Resources section, find the ENI that you want to manage and click Unbind.
6. In the message that appears, click OK.

### Disassociate an HAVIP from an

EIP This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic IP address (EIP). After you disassociate an HAVIP from an EIP, the HAVIP can no longer provide services over the Internet.
1. Log on to the VPC console.
2. In the left-side navigation pane, click High-availabilit y Virt ual IP Address.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the High-availabilit y Virt ual IP Address page, find the HAVIP and click Unbind EIP in the
Operat ion column.
5. In the message that appears, click OK.

### Delete an HAVIP

This topic describes how to delete a high-availability virtual IP address (HAVIP). Prerequisites If an HAVIP is associated with an elastic IP address (EIP), you must disassociate the HAVIP from the EIP before you delete the HAVIP. For more information, see Disassociate an HAVIP from an EIP. The HAVIP is not associated with an Elastic Compute Service (ECS) instance. If the HAVIP is associated with an ECS instance, disassociate the HAVIP from the ECS instance first. For more information, see Disassociate an HAVIP from an ECS instance. The HAVIP is not associated with an elastic network interface (ENI). If the HAVIP is associated with an ENI, disassociate the HAVIP from the ENI first. For more information, see Associate an HAVIP with an ENI.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region to which the HAVIP belongs.
4. On the HaVip page, find the HAVIP that you want to delete and click Delet e in the Act ions
column.
5. In the message that appears, click OK.

## Network ACLs

### Overview

Network access control lists (ACLs) allow you to regulate access control for a virtual private cloud (VPC). You can create network ACL rules and associate a network ACL with a vSwitch. This allows you to control inbound and outbound traffic of Elastic Compute Service (ECS) instances that are associated with the vSwitch. Features Network ACLs have the following features: A network ACL is used to filter inbound and outbound network traffic of ECS instances that are associated with a vSwitch in a VPC. The network traffic forwarded to ECS instances by Server Load Balancer (SLB) instances is also filtered. Network ACLs are stateless. You must set both inbound and outbound rules. Otherwise, the system may fail to respond to requests. If you create a network ACL that does not contain a rule, all inbound and outbound access is denied. If a network ACL is associated with a vSwitch, the network ACL does not filter the traffic forwarded between ECS instances that are associated with the vSwitch. Network ACL rules You can add rules to or delete rules from a network ACL. Changes to the rules are automatically synchronized to the associated vSwitch. By default, an inbound rule and an outbound rule are automatically added to a newly created network ACL. These rules allow all inbound and outbound network traffic transmitted through the associated vSwitch. You can delete the default rules. The following table lists the default inbound and outbound rules. Default inbound rule

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
| 2 | all | 172.16.0.0/12 | -1/-1 | Deny | Custom |
| 3 | all | 172.16.0.0/12 | -1/-1 | Allow | Custom |

Policy: specifies whether to allow or deny specific traffic. Protocol: the protocol type. Available options include All, ICMP, GRE, TCP, and UDP. Source CIDR block: the source CIDR block from which inbound traffic is transmitted. Destination IP address: the destination IP addresses to which outbound traffic is transmitted. Destination port range: the range of destination ports to which the inbound rule applies. Destination port range: the range of destination ports to which the outbound rule applies. Comparison between network ACLs and security groups Network ACLs control data transmitted through associated vSwitches while security groups control data transmitted through associated ECS instances. The following table describes the differences between network ACLs and security groups.

| Network ACL | Security group |
|---|---|
| Applies to vSwitches. | Applied to instances. |
| Stateless: Returned traffic must be allowed by inbound rules. | Stateful: Returned traffic is automatically allowed and not affected by rules. |
| The system attempts to match requests against rules in descending order of priority. Not all rules are matched. | The system matches a request against all rules before a rule is applied. |
| Each vSwitch can be associated only with one network ACL. | Each ECS instance can be added to more than one security group. |

The following figure shows how network ACLs and security groups are applied to ensure network security. Limits The following table describes the limits on network ACLs.

| Item | Limit |
|---|---|
| Maximum number of network ACLs that can be created in each VPC | 200 |

| irtual Private Cloud | User Guide·Network ACL |
|---|---|

| Item | Limit |
|---|---|
| Maximum number of network ACLs that can be associated with a vSwitch | 1 |
| Maximum number of rules that can be added to a network ACL | Inbound rules: 20 Outbound rules: 20 |

The following flowchart shows how to use a network ACL.

### Scenarios

If you are familiar with the ports that are commonly used by ECS instances, you can specify them in access control list (ACL) rules to facilitate precise network traffic filtering. This topic describes the ports that are commonly used by ECS instances and the application scenarios of these ports. Ports The following table lists the ports and the services that use these ports.

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

| User Guide·Network A | CLs | Virtual Private Clou |
|---|---|---|

| Port | Service | Description |
|---|---|---|
| 1433 | SQL Server | The TCP port of SQL Server. It is used for SQL Server to provide external services. |
| 1434 | SQL Server | The UDP port of SQL Server. It is used to return the TCP/IP port occupied by SQL Server. |
| 1521 | Oracle | The Oracle communication port. ECS instances that run Oracle SQL must have this port open. |
| 3306 | MySQL | The MySQL port. It is used for MySQL databases to provide external services. |
| 3389 | Windows Server Remote Desktop Services | The Windows Server Remote Desktop Services port. It is used to log on to a Windows instance. |
| 8080 | Proxy port | An alternative to port 80. It is commonly used for WWW proxy services. |

Custom network ACLs and describe a network ACL example for VPCs that support IPv4 addresses only. The inbound rules in effective order 1, 2, 3, and 4 respectively allow HTTP, HTTPS, SSH, and RDP traffic to the vSwitch. Outbound response rules are those in effective order 3. The outbound rules in effective order 1 and 2 respectively allow HTTP and HTTPS traffic from the vSwitch. Outbound response rules are those in effective order 5. The inbound rule in effective order 6 denies all inbound IPv4 traffic. This rule ensures that packets that do not match any other rules are denied. The outbound rule in effective order 4 denies all outbound IPv4 traffic. This rule ensures that packets that do not match any other rules are denied. Not e An inbound or outbound rule must correspond to an inbound or outbound rule that allows response traffic. Inbound rules

| Effectiv e order | Protocol | Source IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|
| 1 | TCP | 0.0.0.0/ 0 | 80/80 | Accept | Allows inbound HTTP traffic from any IPv4 addresses. |
| 2 | TCP | 0.0.0.0/ 0 | 443/443 | Accept | Allows inbound HTTPS traffic from any IPv4 addresses. |
| 3 | TCP | 0.0.0.0/ 0 | 22/22 | Accept | Allows inbound SSH traffic from any IPv4 addresses. |

| irtual Privat | e Cloud |   |   |   | User Guide·Network ACL |
|---|---|---|---|---|---|

| Effectiv e order | Protocol | Source IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|
| 4 | TCP | 0.0.0.0/ 0 | 3389/33 89 | Accept | Allows inbound RDP traffic from any IPv4 addresses. |
| 5 | TCP | 0.0.0.0/ 0 | 32768/6 5535 | Accept | Allows inbound IPv4 traffic from the Internet. This port range is for reference only. For more information on how to select appropriate ephemeral ports, see Ephemeral ports. |
| 6 | All | 0.0.0.0/ 0 | -1/-1 | Drop | Denies all inbound IPv4 traffic. |

Outbound rules

| Effectiv e order | Protocol | Destinat ion IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|
| 1 | TCP | 0.0.0.0/ 0 | 80/80 | Accept | Allows outbound IPv4 HTTP traffic from the vSwitch to the Internet. |
| 2 | TCP | 0.0.0.0/ 0 | 443/443 | Accept | Allows outbound IPv4 HTTPS traffic from the vSwitch to the Internet. |
| 3 | TCP | 0.0.0.0/ 0 | 32768/6 5535 | Accept | Allows outbound IPv4 traffic from the vSwitch to the Internet. This port range is for reference only. For more information on how to select appropriate ephemeral ports, see Ephemeral ports. |
| 4 | All | 0.0.0.0/ 0 | -1/-1 | Drop | Denies all outbound IPv4 traffic. |

Network ACLs for SLB If the ECS instance in the vSwitch acts as the backend server of an SLB instance, you must add the following network ACL rules. Inbound rules

| Effectiv e order | Protoco l | Source IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|

| Effectiv e order | Protoco l | Source IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|
| 1 | SLB listener protoco l | Client IP address es allowed to access the SLB instance | SLB listener port | Accept | Allows inbound traffic from specified client IP addresses. |
| 2 | Health check protoco l | 100.64. 0.0/10 | Health check port | Accept | Allows inbound traffic from health check IP addresses. |

Outbound rules

| Effectiv e order | Protoco l | Destinat ion IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|
| 1 | All | Client IP address es allowed to access the SLB instance | -1/-1 | Accept | Allows all outbound traffic to specified client IP addresses. |
| 2 | All | 100.64. 0.0/10 | -1/-1 | Accept | Allows outbound traffic to health check IP addresses. |

Ephemeral ports Clients use different ports to initiate requests. You can select different port ranges for network ACL rules based on the client type. The following table lists ephemeral port ranges for common clients.

| Client | Port range |
|---|---|
| Linux | 32768/61000 |
| Windows Server 2003 | 1025/5000 |
| Windows Server 2008 and later | 49152/65535 |
| NAT gateway | 1024/65535 |

### Create a network ACL

A network access control list (ACL) allows you to manage network access in a virtual private cloud (VPC). You can create network ACLs in the VPC console. Prerequisites A VPC is created. For more information about how to create MSE Nacos Professional Edition instances, see Create a VPC.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where you want to create the network ACL.
4. On the Net work ACL page, click Creat e Net work ACL.
5. In the Creat e Net work ACL dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the network ACL belongs. |
| Resource Set | Select the resource set to which the network ACL belongs. |
| Region | Select the region where you want to deploy the network ACL. |
| Name | Enter a name for the network ACL. |
| Descript ion | Enter a description for the network ACL. |
| VPC | Select the VPC for which you want to create the network ACL. Not e The VPC and network ACL must be deployed in the same region. |

### Associate a network ACL with a

vSwitch After you create a network access control list (ACL), you can associate it with a vSwitch. This way, you can use the network ACL to control the traffic that flows through the Elastic Compute Service (ECS) instances that are connected to the vSwitch. Prerequisites Before you associate a network ACL with a vSwitch, make sure that the following requirements are met: A network ACL is created. For more information, see Create a network ACL. A vSwitch is created. The vSwitch and network ACL must belong to the same VPC. For more information, see Create a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACLs.
3. In the top navigation bar, select the region to which the network ACK that you want to manage
belongs.
4. On the Net work ACLs page, find the network ACL that you want to manage and click
Management in the Operat ion column.
5. On the Bound resource tab, click Associat ed resources.
6. In the Associat ed resources dialog box, select a vSwitch and click OK.
Not e The network ACL and vSwitch must belong to the same VPC. A vSwitch can be associated only with one network ACL.

### Add network ACL rules

#### Add an inbound rule

After you create a network access control list (ACL), you can add inbound rules to the network ACL. You can use inbound rules to control whether Elastic Compute Service (ECS) instances in a vSwitch can be accessed over the Internet or private networks. Prerequisites A network ACL is created. For more information, see Create a network ACL.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACLs.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACLs page, find the network ACL that you want to manage and click Inbound
direct ion rule in the Operat ion column.
5. On the Inbound direct ion rule tab, click Creat e inbound rule.
6. In the Creat e inbound rule dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Name | Enter a name for the inbound rule. The name must be 2 to 128 characters in length. It must start with a letter and can contain digits, underscores ( ), and hyphens (-). _ |

| Parameter | Description |
|---|---|
| St rat egy | Select an action for the inbound rule. Valid values: Allow: accepts network traffic that is destined for the ECS instances connected to the vSwitch. Reject ion: drops network traffic that is destined for the ECS instances connected to the vSwitch. |
| Prot ocol t ype | Select a transport layer protocol. Valid values: ALL: all protocols ICMP: Internet Control Message Protocol (ICMP) GRE: GRE T CP: Transmission Control Protocol (TCP) UDP: User Datagram Protocol (UDP) |
| Source address | The source CIDR block from which data is transmitted. Default value: 0.0.0.0/32. |
| Dest inat ion Port Range | Enter the destination port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the highest and lowest values in a port range, for example, 1/200 or 80/80. -1/-1 indicates that all ports are available. You cannot set the value to -1/-1. |

#### Add an outbound rule

This topic describes how to add an outbound rule to a network access control list (ACL). You can use outbound rules to control how Elastic Compute Service (ECS) instances connected to a vSwitch access the Internet or other private networks. Prerequisites A network ACL is created. For more information, see Create a network ACL.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACLs.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACLs page, find the network ACL that you want to manage and click Out
direct ion rule in the Operat ion column.
5. On the Out direct ion rule tab, click Creat e out direct ion rules.
6. In the Creat e out direct ion rules dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Name | Enter a name for the outbound rule. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter. _ |
| St rat egy | Select an action for the outbound rule. Valid values: Allow: allows ECS instances connected to the vSwitch to access the Internet or other private networks. Reject ion: forbids ECS instances connected to the vSwitch to access the Internet or other private networks. |
| Prot ocol t ype | Select a transport layer protocol. Valid values: ALL: all protocols ICMP: Internet Control Message Protocol (ICMP) GRE: Generic Routing Encapsulation (GRE) T CP: Transmission Control Protocol (TCP) UDP: User Datagram Protocol (UDP) |
| Dest inat ion address | The destination CIDR block to which data is transmitted. Default value: 0.0.0.0/32. |
| Dest inat ion port range | Enter the destination port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the highest and lowest values in a port range, for example, 1/200 or 80/80. -1/-1 indicates that all ports are available. Do not set the value to -1/-1. |

#### Change the priorities of network ACL rules

Network ACL rules take effect in descending order of priority. A smaller value indicates a higher priority. You can prioritize network ACL rules based on your business requirements. Change the priority of an inbound rule
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACLs.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACLs page, find the network ACL that you want to manage and click
Management in the Operat ion column.
5. Click the Inbound direct ion rule tab and click Sort .
6. In the Sort dialog box, change the priority of the rule by dragging and dropping the rule. Then,
click OK. Not e Rules are listed in descending order of priority. Change the priority of an outbound rule
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACLs.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACLs page, find the network ACL that you want to manage and click
Management in the Act ions column.
5. Click the Out bound direct ion rule tab and click Sort .
6. In the Sort dialog box, change the priority of the rule by dragging and dropping the rule. Then,
click OK. Not e Rules are listed in descending order of priority.

### Disassociate a network ACL from

a vSwitch This topic describes how to disassociate a network access control list (ACL) from a vSwitch. After you disassociate a network ACL from a vSwitch, the network ACL no longer controls the traffic of Elastic Compute Service (ECS) instances that belong to the vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL and click Manage in the Act ions column.
5. On the Resources tab, find the vSwitch and click Unbind in the Act ions column.
6. In the Unbind Net work ACL message, click OK.

### Delete a network ACL

This topic describes how to delete a network access control list (ACL). Prerequisites Make sure that the network ACL is not associated with a vSwitch. If the network ACL is associated with a vSwitch, disassociate the network ACL from the vSwitch first. For more information, see Disassociate a VSwitch from a network ACL.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL that you want to delete and click Delet e in the
Act ions column.
5. In the Delet e Net work ACL message, click OK.
