---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Virtual Private Cloud User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 63
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Virtual Private Cloud User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Virtual%20Private%20Cloud%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Virtual Private Cloud User Guide 20220928

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
    - 4.2.2 Add a secondary IPv4 CIDR block
    - 4.2.3 Delete a secondary IPv4 CIDR block
    - 4.2.4 Modify the name and description of a VPC
    - 4.2.5 Delete a VPC
  - 4.3 VSwitch management
    - 4.3.1 Create a vSwitch
    - 4.3.2 Create cloud resources in a vSwitch
    - 4.3.3 Modify a vSwitch
    - 4.3.4 Delete a vSwitch
- 5 Route tables
  - 5.1 Overview
  - 5.2 Add a custom route entry
  - 5.3 Export route entries
  - 5.4 Modify a route table
  - 5.5 Delete a custom route entry
- 6 HAVIPs
  - 6.1 Overview
  - 6.2 Create HAVIPs
  - 6.3 Associate HAVIPs with backend cloud resources
    - 6.3.1 Associate an HAVIP with an ECS instance
    - 6.3.2 Associate an HAVIP with an ENI
  - 6.4 Associate HAVIPs with EIPs
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
    - 7.5.3 Change the priority of a network ACL rule
  - 7.6 Disassociate a network ACL from a vSwitch
  - 7.7 Delete a network ACL

## 1 What is a VPC?

A virtual private cloud (VPC) is a private network dedicated for your use. You have full control over your VPC. For example, you can specify the CIDR block and configure route tables and gateways. In a VPC, you can deploy Apsara Stack resources, such as Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, and Server Load Balancer (SLB) instances. Furthermore, you can connect your VPC to other VPCs or on-premises networks to create a custom network environment. This way, you can migrate applications to the cloud and extend data centers. Components Each Virtual Private Cloud consists of at least one private network segment, one router, and at least one switch. Private CIDR blocks When you create a VPC and a vSwitch, you must specify the private IP address range for the VPC in CIDR notation. You can use the standard private CIDR blocks listed in the following table and their subsets as CIDR blocks for your VPCs. For more information, see The network planning section in User Guide.

| CIDR blocks | Number of available private IP addresses (system reserved ones excluded) |
|---|---|
| 192.168.0.0/16 | 65,532 |
| 172.16.0.0/12 | 1,048,572 |
| 10.0.0.0/8 | 16,777,212 |

VRouter A VRouter is a hub that connects all VSwitches in a VPC and serves as a gateway between the VPC and other networks. After a VPC is created, the system creates a VRouter for the VPC. Each vRouter is associated with a route table. For more information, see the Route table overview topic in User Guide. vSwitches A vSwitch is a basic network component that connects different cloud resources in a VPC. After you create a VPC, you can create a vSwitch to divide your VPC into multiple subnets. vSwitches deployed in a VPC can communicate with each other over the private network. You can deploy your applications in vSwitches that belong to different zones to improve service availability. For more information, see the Create a vSwitch topic in User Guide. le

## 2 Log on to the VPC console

This topic describes how to log on to the Virtual Private Cloud (VPC) console of Apsara Uni-manager by using the Google Chrome browser. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.

## 3 Quick start

### 3.1 Plan and design a VPC

Before you create virtual private clouds (VPCs) and VSwitches, you need to plan the quantity and Classless Inter-domain Routing (CIDR) blocks of VPCs and VSwitches. How many VPCs are required? How many VSwitches are required? How do I specify CIDR blocks? How do I specify CIDR blocks if I want to connect a VPC to other VPCs or on-premises data centers? How many VPCs are required? One VPC We recommend that you create one VPC if you do not need to deploy systems in multiple regions or separate VPCs. Multiple VPCs We recommend that you create multiple VPCs if you need to: Deploy application systems across regions. A VPC cannot be deployed across regions. If you want to deploy your application systems in different regions, you must create multiple VPCs. You can use Express Connect and VPN Gateway to connect VPCs. Separate IT systems To separate IT systems, you must create multiple VPCs. The following figure shows an example of isolating a production environment from a test environment by deploying them in separate VPCs. How many VSwitches are required? We recommend that you create at least two VSwitches for each VPC and deploy these VSwitches in different zones to achieve zone-disaster recovery. After you deploy your applications in different zones within a region, you must measure the network latency between these applications. This is because the cross-zone network latency may be higher than expected due to complex data processing or cross-zone calls. An ideal approach is to optimize and adjust your systems to strike a balance between availability and latency. In addition, the sizes and designs of your IT systems must also be taken into consideration when you create VSwitches. If you allow traffic from the Internet to be routed to and from the frontend systems, you can deploy the front-end systems in different VSwitches and the backend systems in other VSwitches to create a robust disaster recovery strategy. How do I specify CIDR blocks? When you create VPCs and VSwitches, you must specify their private IP address ranges in the form of CIDR blocks. VPC CIDR blocks You can use 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or their subsets as the CIDR blocks of your VPCs. To specify CIDR blocks for VPCs, follow these rules: If you have only one VPC and this VPC does not need to communicate with any on-premises data center, you can use one of the preceding CIDR blocks or one of their subsets as the CIDR block of the VPC. If you have multiple VPCs, or you need to build a hybrid cloud to integrate VPCs and on-premises data centers, we recommend that you use the subsets of the preceding CIDR blocks for your VPCs. In this case, the mask cannot be longer than 16 bits. VSwitch CIDR blocks The CIDR block of a VSwitch must be a subset of the CIDR block of the VPC this VSwitch resides in. For example, if the CIDR block of a VPC is 192.168.0.0/16, the CIDR block of a VSwitch in the VPC must be a segment from 192.168.0.0/17 to 192.168.0.0/29. To specify CIDR blocks for VSwitches, follow these rules: The CIDR block size for a VSwitch is between a 16-bit mask and a 29-bit mask. It means that 8 to 65,536 IP addresses can be provided. This range is set because a 16-bit host address space provides addressing for 65,534 ECS instances, which can meet your needs in most cases, while a mask smaller than 29 bits can only allow very few usable host addresses. The first and the last three IP addresses in each VSwitch CIDR block are reserved by the system. For example, if the CIDR block of a VSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. You must check the number of ECS instances in the VSwitch before you specify the CIDR block of a VSwitch. How do I specify CIDR blocks if I want to connect a VPC to other VPCs or on-premises data centers? Before you connect your VPC to another VPC or an on-premises data center, you must make sure that the CIDR block of your VPC does not conflict with that of the peer network. For example, assume you have three VPCs: VPC1 in China (Hangzhou), VPC2 in China (Beijing), and VPC3 in China (Shenzhen), as shown in the following figure. Express Connect circuit is used for VPC1 and VPC2 to communicate with each other. VPC3 does not communicate with other VPCs, but may need to communicate with VPC2 in the future. Additionally, you have an on-premises data center in Shanghai, and you need to connect it to VPC1 by using an Express Connect circuit. In this example, the CIDR block of VPC2 is different from the CIDR block of VPC1, but is the same with the CIDR block of VPC3. However, considering that VPC2 and VPC3 may need to communicate with each other later in the private network, the VSwitches in these VPCs are assigned with different CIDR blocks. This example demonstrates that VPCs communicating with each other can have identical CIDR blocks, but their VSwitches must have different CIDR blocks. When you specify CIDR blocks for multiple VPCs that need to communicate with each other, follow these rules: The preferred practice is to specify different CIDR blocks for different VPCs. You can use the subsets of the standard CIDR blocks to increase the number of available CIDR blocks. If you cannot assign different CIDR blocks for VPCs, try to specify different CIDR blocks for the VSwitches in these VPCs. If you cannot assign different CIDR blocks for all VSwitches in these VPCs, make sure that different CIDR blocks are configured for the VSwitches communicating with each other.

### 3.2 Create an IPv4 VPC

This topic describes how to create a virtual private cloud (VPC) with an IPv4 CIDR block and create an Elastic Compute Service (ECS) instance in the VPC. Prerequisites To deploy cloud resources in a VPC, you must first prepare network subnetting. For more information, see Plan and design a VPC. Step 1: Create a VPC Perform the following steps to create a VPC:
1. Log on to the VPC console.
2. On the VPCs page, click Creat e VPC.
3. On the Creat e VPC page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Sharing Scope | Select the participants that can use the VPC to create resources. Current Resource Set : Only the administrator of the current resource set can create resources for the shared VPC. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organization can create resources for the shared VPC. Current Organizat ion: Only the administrator of the current organization can create resources for the shared VPC. Current Resource Set is selected in this example. |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), _ hyphens (-), periods (.), colons (:), and commas (,). It must start with a letter and cannot start with http:// or https:// . VPCt est is used in this example. |

| Parameter | Description |
|---|---|
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Cust om CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/16. In this example, 192.168.0.0/16 is used as the IPv4 CIDR block of the VPC. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. Do Not Assign is selected in this example. |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with a letter and _ cannot start with http:// or https:// . |

4. Click Back t o Console. On the VPCs page, you can view the VPCs that are created.
Step 2: Create a vSwitch Perform the following steps to create a vSwitch in a VPC:
1. In the left-side navigation pane, click vSwit ches.
2. On the vSwit ches page, click Creat e vSwit ch.
3. On the vSwit ch page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where the vSwitch is deployed. |

| Parameter | Description |
|---|---|
| Zone | Select the zone to which the vSwitch belongs. In a VPC, each vSwitch can be deployed in only one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e An instance can be deployed in only one vSwitch. |
| Sharing Scope | Select the participants that can use the vSwitch to create resources. Current Resource Set : Only the administrator of the current resource set can create resources in the vSwitch. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organizations can create resources in the vSwitch. Current Organizat ion: Only the administrator of the current organization can create resources in the vSwitch. Current Resource Set is selected in this example. |
| VPC | The VPC in which you want to create the vSwitch. VPCtest is selected in this example. |
| Dedicat ed f or Out -of -cloud Physical Machines | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-met al servers in VPCs topic in Bare-metal Server Management Service User Guide. No is selected in this example. |
| vSwit ch Name | Enter a name for the vSwitch. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. The default IPv4 CIDR block is used in this example. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the vSwitch. Do Not Assign is selected in this example. |
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |

Step 3: Create a security group Perform the following steps to create a security group:
1. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
2. Choose Net works and Securit y > Securit y Groups.
3. On the Securit y Groups page, click Creat e Securit y Group.
4. On the Creat e Securit y Group page, set the following parameters and click Submit .

| Parameter | Description |   |   |
|---|---|---|---|
| Organizat ion | Select the organization to which the security group belongs. |   |   |
| Resource Set | Select the resource set to which the security group belongs. |   |   |
| Region | Select the region to which the security group belongs. Make sure that the security group and the VPC belong to the same region. |   |   |
| Zone | Select the zone to which the security group belongs. |   |   |
| Sharing Scope | Select the participants that can use the security group to create resources. Current Resource Set : Only the administrator of the current resource set can create resources for the security group. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organization can create resources for the security group. Current Organizat ion: Only the administrator of the current organization can create resources for the security group. Current Resource Set is selected in this example. |   |   |
| VPC | The VPC to which the security group belongs. |   |   |
| Securit y Group Name | Enter a name for the security group. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter and cannot start with http:// or https: // . |   |   |
| Descript ion | Enter a description for the security group. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas _ (,). It must start with a letter and cannot start with http:// or ht tps:// . |   |   |
|   |   | ht |   |

| https: |   |
|---|---|

|   | // |
|---|---|

|   | tps:// |
|---|---|

Step 4: Create an ECS instance Perform the following steps to create an ECS instance in the VPC:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, click vSwit ches.
3. In the top navigation bar, select the region where the vSwitch is deployed.
4. On the vSwit ches page, find the vSwitch that you want to manage, and choose Creat e > ECS
Inst ance in the Act ions column.
5. On the Creat e ECS Inst ance page, set the parameters and click Submit .
For more information about how to configure ECS instances, see Creat e an inst ance in Quick st art of ECS user guide.

### 3.3 Create an IPv6 VPC

This topic describes how to create a virtual private cloud (VPC) with an IPv6 CIDR block and create an Elastic Compute Service (ECS) instance assigned with an IPv6 address in the VPC. The ECS instance can access IPv6 services. Step 1: Create a VPC and a vSwitch Before you deploy cloud resources in a VPC, you must create a VPC and a vSwitch. Perform the following steps to create a VPC and a vSwitch:
1. Log on to the VPC console.
2. On the VPCs page, click Creat e VPC.
3. On the Creat e VPC page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Sharing Scope | Select the participants that can use the VPC to create resources. Current Resource Set : Only the administrator of the current resource set can use the VPC to create resources. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organization can create resources for the shared VPC. Current Organizat ion: Only the administrator of the current organization can use the VPC to create resources. Current Resource Set is selected in this example. |

| Parameter | Description |
|---|---|
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), _ hyphens (-), periods (.), colons (:), and commas (,). It must start with a letter and cannot start with http:// or https:// . VPCt est is used in this example. |
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Cust om CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of the preceding CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/16. In this example, 192.168.0.0/16 is used as the IPv4 CIDR block of the VPC. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. In this example, Assign is selected. |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with a letter and _ cannot start with http:// or https:// . |

4. Click Back t o Console. In the left navigation pane, click vSwit ches.
5. On the vSwit ches page, click Creat e vSwit ch.
6. On the vSwit ch page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where the vSwitch is deployed. |

| Parameter | Description |
|---|---|
| Zone | Select the zone to which the vSwitch belongs. In a VPC, each vSwitch can be deployed in only one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e An instance can be deployed in only one vSwitch. |
| Sharing Scope | Select the participants that can use the vSwitch to create resources. Current Resource Set : Only the administrator of the current resource set can create resources in the vSwitch. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organizations can create resources in the vSwitch. Current Organizat ion: Only the administrator of the current organization can use the vSwitch to create resources. Current Resource Set is selected in this example. |
| VPC | Select the VPC in which you want to create the vSwitch. VPCtest is selected in this example. |
| Dedicat ed f or bare met al | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-met al servers in VPCs topic in Bare-metal Server Management Service User Guide. No is selected in this example. |
| vSwit ch Name | Enter a name for the vSwitch. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the vSwitch. The default IPv4 CIDR block is used in this example. |
| IPv6 CIDR Block | Enter an IPv6 CIDR block for the vSwitch. In this example, the default IPv6 CIDR block is used. |
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |

Step 2: Create a security group Perform the following steps to create a security group:
1. In the top navigation bar, choose Product s > Elast ic Comput ing > Elast ic Comput e Service.
2. Choose Net works and Securit y > Securit y Groups.
3. On the Securit y Groups page, click Creat e Securit y Group.
4. On the Creat e Securit y Group page, set the following parameters and click Submit .

| Parameter | Description |   |   |
|---|---|---|---|
| Organizat ion | Select the organization to which the security group belongs. |   |   |
| Resource Set | Select the resource set to which the security group belongs. |   |   |
| Region | Select the region to which the security group belongs. Make sure that the security group and the VPC belong to the same region. |   |   |
| Zone | Select the zone to which the security group belongs. |   |   |
| Sharing Scope | Select the participants that can use the security group to create resources. Current Resource Set : Only the administrator of the current resource set can create resources for the security group. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organization can create resources for the security group. Current Organizat ion: Only the administrator of the current organization can create resources for the security group. Current Resource Set is selected in this example. |   |   |
| VPC | Select the VPC to which the security group belongs. |   |   |
| Securit y Group Name | Enter a name for the security group. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter and cannot start with http:// or https: // . |   |   |
| Descript ion | Enter a description for the security group. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas _ (,). It must start with a letter and cannot start with http:// or ht tps:// . |   |   |
|   |   | ht |   |

| https: |   |
|---|---|

|   | // |
|---|---|

|   | tps:// |
|---|---|

Step 3: Create and configure an ECS instance After you create a VPC and a vSwitch, you must create an ECS instance and assign an IPv6 address to the ECS instance. Then, you must associate the specified IPv6 address with the elastic network interface (ENI) of the ECS instance. Perform the following steps to create and configure an ECS instance:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region where the vSwitch is deployed.
4. On the vSwit ches page, find the vSwitch that you want to manage, and choose Creat e > ECS
Inst ance in the Act ions column.
5. On the Creat e ECS Inst ance page, set the parameters and click Submit .
In this example, Assign is selected. Therefore, an IPv6 IP address is assigned to the ECS instance. For more information about other parameters, see Creat e an ECS inst ance in Quick St art of Elastic C ompute Service User Guide.
6. Return to the Inst ances page and click the instance ID to view the IPv6 address that is assigned to
the ECS instance.
7. Configure a static IPv6 address.
If the image of your ECS instance supports DHCPv6, you do not need to manually configure a static IPv6 address. DHCPv6 enables automatic configuration of IPv6 addresses. Therefore, if your ECS instance image supports DHCPv6, the ECS instance can use the assigned IPv6 address to communicate within the private network. The following images support DHCPv6: Linux images: CentOS 7.6 IPV6 64Bit CentOS 6.10 64Bit SUSE Linux Enterprise Server 12 SP4 64Bit Windows Server images If the image of your ECS instance does not support DHCPv6, you must manually configure an IPv6 address for the ECS instance. For more information, see the relevant documents. Step 4: Purchase an IPv6 Internet bandwidth plan By default, IPv6 addresses can be used to communicate within only private networks. If you want to use the IPv6 address to access the Internet or to be accessed by IPv6 clients over the Internet, you must purchase an Internet bandwidth plan for the IPv6 address. To purchase an IPv6 Internet bandwidth plan, perform the following steps:
1. In the top navigation bar, choose Product s > Net working > Virt ual Privat e Cloud.
2. In the left-side navigation pane, choose Int ernet Access > IPv6 Gat eway.
3. Select the region where the IPv6 gateway is deployed.
4. On the IPv6 Gat eway page, find the IPv6 gateway that you want to manage and click Manage in
the Act ions column.
5. In the left-side navigation pane, click IPv6 Int ernet Bandwidt h.
6. On the IPv6 Int ernet Bandwidt h page, find the IPv6 address that you want to manage and click
Enable IPv6 Int ernet Bandwidt h in the Act ions column.
7. Select a bandwidth plan and then click OK.
The maximum IPv6 Internet bandwidth for an IPv6 gateway of Free, Enterprise, or Enhanced Edition is 2 Gbit/s. Step 5: Configure security group rules IPv4 and IPv6 addresses are independent of each other. If the current security group rules do not apply to your IPv6 services, you must configure security group rules for the ECS instances to regulate communication with IPv6 addresses. For more information about how to configure security group rules, see the Add securit y group rules chapter in Securit y Groups of Elastic Compute Service User Guide. Step 6: Test the network connectivity Log on to an ECS instance and ping an IPv6 service to test the network connectivity.

## 4 VPCs and VSwitches

### 4.1 Overview

Before you can use cloud resources in a virtual private cloud (VPC), you must create a VPC and a vSwitch. You can create more than one vSwitch to divide a VPC into multiple subnets. By default, the subnets in a VPC can communicate with each other. VPCs and vSwitches A VPC is a private network dedicated for your use. Not e You cannot directly deploy cloud resources in a VPC. You must deploy cloud resources in vSwitches of a VPC. vSwitches are basic components of VPCs and are used to connect different cloud resources. You can deploy a VPC only in one region and cannot deploy a VPC across regions. However, a VPC contains all zones of the region to which the VPC belongs. You can create one or more vSwitches in a zone to divide a VPC into multiple subnets. CIDR blocks and IP addresses VPCs support both IPv4 and IPv6. By default, VPCs use IPv4. You can enable IPv6 based on your business requirements. VPCs support the dual-stack mode. In dual-stack mode, resources in a VPC can communicate through both IPv4 and IPv6 addresses. IPv4 and IPv6 addresses are independent of each other. Therefore, you must configure routes and security groups for both IPv4 and IPv6 addresses. The following table lists the differences between IPv4 and IPv6 addresses.

| IPv4 VPC | IPv6 VPC |
|---|---|
| An IPv4 address is 32 bits in length and contains four groups. Each group consists of at most three decimal digits. | An IPv6 address is 128 bits in length and contains eight groups. Each group consists of four hexadecimal digits. |
| By default, IPv4 is enabled. | You can enable IPv6. |
| The subnet mask of a VPC CIDR block can range from /8 to /24. | The subnet mask of a VPC CIDR block is /61. |
| The subnet mask of a vSwitch CIDR block can range from /16 to /29. | The subnet mask of a vSwitch CIDR block is /64. |
| You can specify an IPv4 CIDR block. | You cannot specify an IPv6 CIDR block. The system automatically assigns an IPv6 CIDR block to your VPC from the IPv6 address pool. |
| Supported by all instance types. | Not supported by specific instance types. For more information, see Inst ance t ypes under What is ECS? in the Elastic Compute Service User Guide. |
| IPv4 elastic IP addresses (EIPs) are supported. | IPv6 EIPs are not supported. |
| VPN gateways and NAT gateways are supported. | VPN gateways and NAT gateways are not supported. |

By default, IPv4 and IPv6 addresses provided for VPCs support only communication over private networks. Cloud resources deployed in different vSwitches that belong to the same VPC can communicate with each other over private networks. To connect a VPC to another VPC or a data center, you can use Express Connect, or VPN Gateway. To enable cloud resources in a VPC to communicate with the Internet, perform the following operations: Through IPv4 addresses You can configure NAT gateways or associate EIPs with Elastic Compute Service (ECS) instances in a VPC. This way, these ECS instances can communicate with the Internet through IPv4 addresses. Through IPv6 addresses To enable cloud resources in a VPC to communicate with the Internet through IPv6 addresses, you must purchase an IPv6 Internet bandwidth plan. You can configure egress-only rules for IPv6 addresses. This allows cloud resources in the VPC to access the Internet through IPv6 addresses. However IPv6 clients cannot access the cloud resources over the Internet. Routes The system automatically creates a system route table and adds system route entries to control the traffic of the VPC. A VPC has only one system route table. You cannot create or delete a system route table. If multiple route entries match the destination CIDR block, the route entry with the largest prefix prevails and determines the next hop. This ensures that the traffic is routed to the most precise destination. You can also add a custom route entry to route traffic to a specified destination.

### 4.2 VPC management

#### 4.2.1 Create a VPC

A virtual private cloud (VPC) is a private network dedicated for your use. You have full control over your VPC. For example, you can specify CIDR blocks, and configure route tables and gateways for your VPC. You can create a VPC, and then use Alibaba Cloud resources, such as Elastic Compute Service (ECS), ApsaraDB RDS, and Server Load Balancer (SLB) instances in the VPC. This topic describes how to create a VPC. Prerequisites 您必须要先做好网络规划。更多信息，请参见Plan networks。 如果您要创建IPv4/IPv6双栈VPC，请先提交申请。 Not e 目前，仅以下地域支持创建IPv4/IPv6双栈VPC：。
1. Log on to the VPC console.
2. In the top navigation bar, select the region where you want to deploy the VPC.
Not e The VPC must be deployed in the same region as that of the cloud resources that you want to deploy in this VPC.
3. On the VPC page, click Creat e VPC.
4. On the Creat e VPC page, configure the VPC and click OK. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select the region where you want to deploy the VPC. |
| Sharing Scope | Select the participants that can use the VPC to create resources. Current Resource Set : Only the administrator of the current resource set can create resources for the shared VPC. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organization can create resources for the shared VPC. Current Organizat ion: Only the administrator of the current organization can use create resources for the shared VPC. |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), _ hyphens (-), periods (.), colons (:), and commas (,). It must start with a letter and cannot start with http:// or https:// . |
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following settings are supported: Recommended CIDR Block: You can use one of the following standard IPv4 CIDR blocks: 192.168.0.0/16 and 172.16.0.0/16. Cust om CIDR Block: You can use 192.168.0.0/16, 172.16.0.0/16, or a subset of these CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/24. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block. Do Not Assign: The system does not assign an IPv6 CIDR block to the VPC. Assign: The system automatically assigns an IPv6 CIDR block to the VPC. If you set this parameter to Assign, the system automatically creates a free IPv6 gateway for this VPC, and assigns an IPv6 CIDR block with the subnet mask /56, such as 2XX1:db8::/56. By default, IPv6 addresses can be used for communication within only private networks. If you want to use the IPv6 address to access the Internet or to be accessed by IPv6 clients over the Internet, you must purchase an Internet bandwidth plan for the IPv6 address. For more information, see the Act ivat e IPv6 Int ernet bandwidt h section of the Manage IPv6 Int ernet bandwidt h topic of the IPv6 gateway user guide. |

| Parameter | Description |
|---|---|
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with a letter and _ cannot start with http:// or https:// . |

#### 4.2.2 Add a secondary IPv4 CIDR block

This topic describes how to expand a virtual private cloud (VPC) by adding a secondary IPv4 CIDR block to the VPC. Prerequisites A VPC is created. For more information, see Create and manage a VPC. Context When you create a VPC, the IPv4 CIDR block that you specified is the primary CIDR block. After the VPC is created, the primary IPv4 CIDR block of the VPC cannot be modified. However, you can add a secondary IPv4 CIDR block to expand the VPC. After you add the secondary IPv4 CIDR block, both the primary and secondary IPv4 CIDR blocks take effect. You can create a vSwitch with the primary or secondary IPv4 CIDR block. However, each vSwitch belongs to only one VPC CIDR block. The system automatically adds a vSwitch route to the VPC route table when you create a vSwitch with the primary or secondary IPv4 CIDR block. The destination CIDR block of a vSwitch route is the CIDR block with which the vSwitch is created. The CIDR block range cannot be the same as or larger than those of other routes in the route table of the VPC. Not e You can add only one secondary IPv4 CIDR block to a VPC and cannot increase the quota.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the VPC page, find the VPC and click Manage in the Act ions column.
4. On the CIDRs tab, click Add IPv4 CIDR.
5. In the Add Secondary CIDR panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| VPC | The VPC to which you want to add the secondary IPv4 CIDR block. |
| Secondary CIDR | Select a method to configure the secondary IPv4 CIDR block: Def ault CIDR Block: You can specify one of the following standard IPv4 CIDR blocks as the secondary IPv4 CIDR block: 192.168.0.0/16 and 172.16.0.0/12. Cust om CIDR Block: You can specify one of the following standard IPv4 CIDR blocks and their subnets as the secondary IPv4 CIDR block: 192.168.0.0/16 and 172.16.0.0/12. When you add a secondary IPv4 CIDR block, take note of the following limits: The CIDR block cannot start with 0. The subnet mask must be 8 to 24 bits in length. The secondary IPv4 CIDR block cannot overlap with the primary IPv4 CIDR block or an existing secondary IPv4 CIDR block. For example, if the primary IPv4 CIDR block of a VPC is 192.168.0.0/16, you cannot specify one of the following CIDR blocks as the secondary IPv4 CIDR block: A CIDR block that is larger than 192.168.0.0/16, such as 192.168.0.0/8. 192.168.0.0/16. A CIDR block that is smaller than 192.168.0.0/16, such as 192.168.0.0/24. |

What's next Create and manage a vSwitch

#### 4.2.3 Delete a secondary IPv4 CIDR block

This topic describes how to delete a secondary IPv4 CIDR block of a virtual private cloud (VPC). However, you cannot delete the primary IPv4 CIDR block of a VPC. Prerequisites Before you delete a secondary IPv4 CIDR block, make sure that you have deleted the vSwitch that is created within the secondary IPv4 CIDR block. For more information, see Delete a vSwitch.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the VPCs page, find the VPC that you want to manage and click Manage in the Act ions
column.
4. On the CIDRs tab, find the secondary IPv4 CIDR block that you want to delete and click Delet e in
the Act ions column.
5. In the message that appears, click OK.

#### 4.2.4 Modify the name and description of a VPC

This topic describes how to modify the name and description of a virtual private cloud (VPC).
1. Log on to the VPC console.
2. In the top navigation bar, select the region where your VPC is deployed.
3. On the VPCs page, find the target VPC network and click Manage in the Act ions column.
4. In the VPC Det ails section, click Edit next to Name. In the dialog box that appears, enter a new
name for the VPC and click OK. The name must be 2 to 128 characters in length and can contain letters, Chinese characters, digits, underscores (_), and hyphens (-). It must start with a letter or a Chinese character.
5. Click Edit next to Descript ion. In the dialog box that appears, enter a new description, and click
OK. The description must be 2 to 256 characters in length and cannot start with `http://` or `https:` `//` .

#### 4.2.5 Delete a VPC

This topic describes how to delete a virtual private cloud (VPC). After you delete a VPC, the vRouters and route tables associated with the VPC are also deleted. Prerequisites Before you delete a VPC, make sure that the following requirements are met: No vSwitch exists in the VPC. If a vSwitch exists in the VPC, delete the vSwitch first. For more information, see Delete a vSwitch. No IPv6 gateway exists in the VPC. If an IPv6 gateway exists in the VPC, delete the IPv6 gateway first.
1. Log on to the VPC console.
2. In the top navigation bar, select the region where the VPC is deployed.
3. On the VPCs page, find the VPC that you want to delete, and click Delet e in the Act ions column.
4. In the Delet e VPC message, click OK.

### 4.3 VSwitch management

#### 4.3.1 Create a vSwitch

A vSwitch is a basic network component that connects different cloud resources in a virtual private cloud (VPC). Context After you create a VPC, you can create vSwitches to divide the VPC into one or more subnets. vSwitches within the same VPC can communicate with each other. Cloud resources must be deployed in vSwitches. You can deploy applications in vSwitches that belong to different zones to improve service availability. Not e vSwitches do not support multicasting or broadcasting.
1. Log on to the VPC console.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region of the VPC in which you want to create a vSwitch.
4. On the vSwit ches page, click Creat e vSwit ch.
5. On the vSwit ch page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the vSwitch belongs. |
| Resource Set | Select the resource set to which the vSwitch belongs. |
| Region | Select the region where you want to deploy the vSwitch. |
| Zone | Select the zone to which the vSwitch belongs. In a VPC, each vSwitch can be deployed in only one zone. You cannot deploy a vSwitch across zones. However, you can deploy cloud resources in vSwitches that belong to different zones to achieve cross-zone disaster recovery. Not e A cloud instance can be deployed in only one vSwitch. |
| Sharing Scope | Select the participants that can use the vSwitch to create resources. Current Resource Set : Only the administrator of the current resource set can create resources in the vSwitch. Current Organizat ion and Subordinat e Organizat ion: Only the administrators of the current organization and its subordinate organizations can create resources in the vSwitch. Current Organizat ion: Only the administrator of the current organization can create resources in the vSwitch. |
| VPC | Select the VPC for which you want to create the vSwitch. |
| Dedicat ed f or Out -of -cloud Physical Machines | Specify whether the vSwitch is dedicated for bare-metal servers. For more information about bare-metal servers, see the Bare-met al servers in VPCs topic in Bare-metal Server Management Service User Guide. |

| Parameter | Description |
|---|---|
| vSwit ch Name | Enter a name for the vSwitch. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |
| IPv4 CIDR Block | Enter an IPv4 CIDR block for the vSwitch. You must specify the IP address range of the vSwitch in CIDR notation. The subnet mask must be 16 to 29 bits in length. It means that 8 to 65,536 IP addresses can be provided. The CIDR block of a vSwitch must be a proper subset of the CIDR block of the VPC to which the vSwitch belongs. The first IP address and last three IP addresses of a vSwitch are reserved. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The CIDR block of a vSwitch cannot be the same as the destination CIDR block in a route entry of the VPC to which the vSwitch belongs. However, the CIDR block of the vSwitch can be a proper subset of the destination CIDR block of the route entry. After a vSwitch is created, you cannot modify its CIDR block. |
| IPv6 CIDR Block | Enter an IPv6 CIDR block for the vSwitch. You must check whether IPv6 is enabled for the specified VPC. If IPv6 is disabled, you cannot assign an IPv6 CIDR block to the vSwitch. If IPv6 is enabled, you can enter a decimal number ranging from 0 to 255 to define the last 8 bits of the IPv6 CIDR block of the vSwitch. For example, if the IPv6 CIDR block of the VPC is 2xx1:db8::/64, specify 255 to define the last 8 bits of the IPv6 CIDR block. In this case, the IPv6 CIDR block of the vSwitch is 2XX1:db8:ff::/64. ff is the hexadecimal value of 255. |
| Descript ion | Enter a description for the vSwitch. The description must be 2 to 256 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |

#### 4.3.2 Create cloud resources in a vSwitch

You cannot directly deploy cloud resources in a virtual private cloud (VPC). You can deploy cloud resources only in a vSwitch that belongs to a VPC. This topic describes how to create cloud resources in a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region of the VPC to which the vSwitch belongs.
4. On the vSwit ches page, find the vSwitch, click Creat e in the Act ions column, and select the
cloud resource that you want to create. You can create Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, and Server Load Balancer (SLB) instances in a vSwitch.
5. On the page that appears, set the parameters.

#### 4.3.3 Modify a vSwitch

This topic describes how to modify the name and description of a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region of the VPC to which the vSwitch belongs.
4. On the vSwit ches page, find the vSwitch that you want to manage and click Manage in the
Act ions column.
5. In the vSwit ch Basic Inf ormat ion section, click Edit next to Name to modify the name of the
vSwitch. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
6. Click Edit next to Descript ion to modify the description of the vSwitch.
The description must be 2 to 256 characters in length and cannot start with `http://` or `https:` `//` .

#### 4.3.4 Delete a vSwitch

This topic describes how to delete a vSwitch. After you delete a vSwitch, you cannot deploy cloud resources in it. Prerequisites Before you delete a vSwitch, make sure that the following requirements are met: All instances deployed in the vSwitch are deleted, such as Elastic Compute Service (ECS) instances, Server Load Balancer (SLB) instances, and ApsaraDB RDS instances. All resources associated with the vSwitch are deleted, such as high-availability virtual IP addresses (HAVIPs) and Source Network Address Translation (SNAT) entries.
1. Log on to the VPC console.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region of the VPC to which the vSwitch belongs.
4. On the vSwit ch page, find the vSwitch that you want to delete and click Delet e in the Act ions
column.
5. In the Delet e vSwit ch message, click OK.

## 5 Route tables

### 5.1 Overview

After you create a virtual private cloud (VPC), the system creates a system route table for the VPC and adds system routes to the route table. The system routes are used to route traffic within the VPC. You cannot create or delete system routes. However, you can create custom routes to route traffic from specific CIDR blocks to a specified destination. Route tables After you create a VPC, the system creates a system route table to manage routes of the VPC. By default, vSwitches in the VPC use this route table. You cannot create or delete the system route table of a VPC. Each entry in a route table is a route entry. A route entry specifies the destination of traffic and consists of the destination CIDR block, next hop type, and next hop. Route entries include system route entries and custom route entries. Each VPC supports up to 10 route tables, which include the system route table. Each vSwitch can be associated with only one route table. The routing policies of a vSwitch are managed by the route table that is associated with the vSwitch. By default, a vSwitch is associated with the system route table after you create the vSwitch. If you want to associate the system route table with a vSwitch that is associated with a custom route table, you must disassociate the custom route table from the vSwitch. Before you can associate other route tables with the vSwitch, you must disassociate the current route table from the vSwitch. Custom route tables do not support active/standby routes or load-balancing routes. Regions that support custom route tables The following table describes the regions that support custom route tables by default.

| Area | Supported region |
|---|---|
| Asia Pacific | China (Qingdao), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shanghai), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), Japan (Tokyo), Singapore (Singapore), Australia (Sydney), Malaysia (Kuala Lumpur), and Indonesia (Jakarta) |
| Europe & Americas | US (Silicon Valley), US (Virginia), Germany (Frankfurt), and UK (London) |
| Middle East and India | India (Mumbai) and UAE (Dubai) |

The custom route table feature is in public preview in the following regions. You can apply for participating in the public review.

| Area | Supported region |
|---|---|
| Asia Pacific | China (Beijing), China (Shanghai), and China (Shenzhen) |

System routes After you create a VPC, the system automatically adds the following system routes to the route table: A route entry with a destination CIDR block of 100.64.0.0/10. This route is used for communication among cloud resources within the VPC. Route entries whose destination CIDR blocks are the same as the CIDR blocks of the vSwitches in the VPC. These routes are used for communication among cloud resources within the vSwitches. For example, if you create a VPC whose CIDR block is 192.168.0.0/16 and two vSwitches whose CIDR blocks are 192.168.1.0/24 and 192.168.0.0/24, three system routes are automatically added to the route table of the VPC. The following table describes the system routes.

| Destination CIDR block | Next hop | Route entry type |
|---|---|---|
| 100.64.0.0/10 | - | System route |
| 192.168.1.0/24 | - | System route |
| 192.168.0.0/24 | - | System route |

Custom routes You can add custom routes to replace system routes or route traffic to a specified destination. You can specify the following types of next hops when you create a custom route: Elastic Compute Service (ECS) instance: Traffic that is destined for the destination CIDR block is routed to a specified ECS instance in the VPC. You can select this type if you want to access the Internet or other applications through the applications deployed on the ECS instance. VPN gateway: Traffic destined for the destination CIDR block is routed to a specified VPN gateway. You can select this type if you want to connect a VPC to another VPC or an on-premises network through the VPN gateway. NAT gateway: Traffic destined for the destination CIDR block is routed to a specified NAT gateway. You can select this type if you want to connect a VPC to the Internet through the NAT gateway. Router interface (to VPC): Traffic that is destined for the destination CIDR block is routed to a specified VPC. You can select this type if you want to connect two VPCs through Express Connect circuits. Router interface (to VBR): Traffic that is destined for the destination CIDR block is routed to a specified virtual border router (VBR). You can select this type if you want to connect a VPC to an on-premises network through Express Connect circuits. Secondary ENI: Traffic that is destined for the destination CIDR block is routed to a specified secondary elastic network interface (ENI). IPv6 routes If IPv6 is enabled for your VPC, the following route entries are automatically added to the system route table of the VPC: A custom route entry whose destination CIDR block is ::/0 and whose next hop is the IPv6 gateway. Cloud resources deployed in the VPC use this route to access the Internet through IPv6 addresses. A system route entry of which the destination CIDR block is the IPv6 CIDR block of a vSwitch. This route is used for communication within the vSwitch. Routing rules If multiple route entries match the destination CIDR block, the route entry with the largest prefix prevails and determines the next hop. This ensures that the traffic is routed to the most precise destination. For example, the following table describes the route table of a VPC.

| Destination CIDR block | Next hop type | Next hop | Route entry type |
|---|---|---|---|
| 100.64.0.0/10 | - | - | System route |
| 192.168.0.0/24 | - | - | System route |
| 0.0.0.0/0 | Instance | i-12345678 | Custom route |
| 10.0.0.0/24 | Instance | i-87654321 | Custom route |

| destined for 100.64.0.0/10 an hat are destined for 0.0.0.0/0 ined for 0.0.0.0/0 is routed to 10.0.0.0/24 is routed to the E is destined for 10.0.0.1 is rout tined for 10.0.1.1 is routed to | 100.64.0.0/10 |   | an |
|---|---|---|---|
|   |   | 0.0.0.0/0 |   |

|   | i-87654321 |   |
|---|---|---|
| i-12345678 |   | . |

Routing examples You can add custom route entries to a route table to control inbound and outbound traffic that are transmitted over the VPC. Routes within a VPC The following figure shows a NAT gateway that is deployed on an ECS instance (ECS 01) in a VPC. To enable the cloud resources in the VPC to access the Internet through the ECS instance, you must add the following route entry to the route table.

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 0.0.0.0/0 | ECS instance | ECS01 |

Connect two VPCs through Express Connect The following figure shows that VPC 1 (172.16.0.0/12) is connected to VPC 2 (192.168.0.0/16) through Express Connect. After you create router interfaces, you must add the following route entries to the VPCs: Add the following route entry to VPC 1

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Router interface (to VPC) | VPC2 |

Add the following route entry to VPC 2

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | Router interface (to VPC) | VPC1 |

Connect two VPCs through a VPN gateway The following figure shows that VPC 1 (172.16.0.0/12) is connected to VPC 2 (10.0.0.0/8) through a VPN gateway. After you configure the VPN gateway, you must add the following route entries to the VPCs. Add the following route entry to VPC 1

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 10.0.0.0/8 | VPN gateway | VPN gateway 1 |

Add the following route entry to VPC 2

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | VPN gateway | VPN gateway 2 |

Connect a VPC to a data center through Express Connect The following figure shows that a VPC is connected to an on-premises network through Express Connect. After you configure a connection over an Express Connect circuit and a virtual border router (VBR), you must add the following route entries: Add the following route entry to the VPC

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Router interfaces (general routing) | Router interface RI 1 |

Add the following route entry to the VBR

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | Express Connect circuit | Router interface RI 3 |
| 172.16.0.0/12 | VPC | Router interface RI 2 |

Add the following route entry to the on-premises network

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 172.16.0.0/12 | - | On-premises gateway device |

Connect a VPC to a data center through a VPN gateway The following figure shows that a VPC (172.16.0.0/12) is connected to a data center (192.168.0.0/16) through a VPN gateway. After you configure the VPN gateway, you must add the following route entry to the VPC.

| Destination CIDR block | Next hop type | Next hop |
|---|---|---|
| 192.168.0.0/16 | VPN gateway | The VPN gateway that you created |

### 5.2 Add a custom route entry

This topic describes how to add a custom route entry. After you create a virtual private cloud (VPC), the system creates a system route table and adds system route entries to the route table. The system route entries are used to route traffic within the VPC. You cannot create or delete system route entries. However, you can create custom route entries to route traffic from source CIDR blocks to specific destinations. Context Each item in the route table is a route entry. A route entry, which consists of the destination CIDR block, type of next hop, and next hop, specifies the destination for network traffic. Route entries include system route entries and custom route entries.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Rout e T ables.
3. In the top navigation bar, select the region to which the route table belongs.
4. On the Rout e T ables page, find the route table and click Management in the Operat ion column.
5. In the Rout e T able Det ails section, click Add Rout e Ent ry.
6. In the Add Rout e Ent ry panel, set the following parameters and click OK:

| Parameter | Description |
|---|---|
| Dest inat ion CIDR block | Enter a destination CIDR block for the route entry. |

| Parameter | Description |
|---|---|
| Next Hop T ype | Select the type of next hop. Valid values: ECS Inst ance: Traffic destined for the specified CIDR block is routed to the specified Elastic Compute Service (ECS) instance. Select this type if you want to route traffic to an ECS instance for centralized traffic forwarding and management. For example, you can configure an ECS instance as the Internet-facing gateway to route traffic from other ECS instances to the Internet. HaVip Address: Traffic destined for the specified CIDR block is routed to the high-availability virtual IP address (HAVIP) that you select. VPN Gat eway: Traffic destined for the specified CIDR block is routed to the specified VPN gateway. NAT Gat eway: Traffic destined for the specified CIDR block is routed to the specified NAT gateway. Secondary ENI: Traffic destined for the specified CIDR block is routed to the secondary elastic network interface (ENI) that you select. Rout er Int erf ace (T o VPC): Traffic destined for the specified CIDR block is routed to the specified VPC. Select this type if you want to connect VPCs through Express Connect circuits. Rout er Int erf ace (T o VBR): Traffic destined for the specified CIDR block is routed to the router interface that is associated with a virtual border router (VBR). Select this type if you want to connect the VPC to a data center through an Express Connect circuit. If you specify Router Interface (To VBR), you must select a routing mode: General Rout ing: Select an associated router interface. Act ive/St andby Rout ing: Select two instances as the next hop. The active route has a weight of 100 and the standby route has a weight of 0. The standby route takes effect when the active route fails the health check. Load Balancing: Select two to four router interfaces as the next hop. The peer router of each router interface must be a VBR. Valid values of the instance weight: 1 to 255. The value must be an integer and the default value is 100. The weight of each instance must be the same. This way, traffic can be evenly distributed to the next-hop instances. |
| ECS Inst ance/VPN Gat eway/NAT Gat eway/Secondary ENI/HAVIP/VPC | Select an instance as the next hop. |

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

High-availability virtual IP addresses (HAVIPs) are private IP addresses that can be created and released as independent resources. You can use HAVIPs with high-availability (HA) software such as Keepalived to provide active/standby services. This improves the availability of your services. Overview Each Elastic Compute Service (ECS) instance is assigned a private IP address as the primary IP address. You can associate HAVIPs with an ECS instance to increase the number of private IP address available for the ECS instance. Both the primary IP address and HAVIPs of an ECS instance can be used to access networks. In addition, you can use HAVIPs with HA software such as Keepalived to provide active/standby services. This improves the availability of your services. You can associate an HAVIP with ECS instances by using the following methods: Directly associate an HAVIP with ECS instances. Each HAVIP can be associated with two ECS instances. After an HAVIP is associated with ECS instances, the ECS instances can send Address Resolution Protocol (ARP) messages to advertise the HAVIP. After the ECS instances advertise the HAVIP, one of the ECS instances serves as the primary instance, and the other ECS instance serves as the secondary instance. If the primary ECS instance is down, the secondary ECS instance takes over to provide services. Attach secondary elastic network interfaces (ENIs) to ECS instances. Then, associate the HAVIP with the secondary ENIs. Each HAVIP can be associated with ENIs of two ECS instances. After the HAVIP is associated with the ENIs, the ECS instances can send ARP messages to advertise the HAVIP. After the ECS instances advertise the HAVIP, one of the ECS instances serves as the primary instance, and the other ECS instance serves as the secondary instance. If the primary ECS instance is down, the secondary ECS instance takes over to provide services. Not e Before you associate an HAVIP with secondary ENIs, make sure that the secondary ENIs are attached to two ECS instances. HAVIPs have the following features: HAVIPs are floating private IP addresses and are not statically assigned to specified ECS instances. HAVIPs can be associated with or disassociated from ECS instances through ARP announcements. An HAVIP can be associated with only ECS instances or ENIs that belong to the same vSwitch. You can associate each HAVIP with two ECS instances or two secondary ENIs. However, you cannot associate an HAVIP with an ECS instance and a secondary ENI at the same time. Scenarios HAVIPs support flexible configurations in the following scenarios: Scenario 1: Internal-facing HA services In the following figure, two ECS instances are assigned the same HAVIP. Keepalived is configured for the ECS instances to provide an internal-facing HA service. Other instances in the same virtual private cloud (VPC) can access this service. The HAVIP serves as the service address. If the primary ECS instance is down, the secondary ECS instance takes over. This improves the availability of your services. Scenario 2: Internet-facing HA services In the following figure, two ECS instances are assigned the same HAVIP. Keepalived is configured and the HAVIP is associated with an elastic IP address (EIP) for the ECS instances to provide an Internetfacing HA service. The EIP that is associated with the HAVIP serves as the service address. If the primary ECS instance is down, the secondary ECS instance takes over. This improves the availability of your services. Limits Before you use HAVIPs, take note of the following limits.

| Item | Default |
|---|---|
| Number of HAVIPs that can be created in each VPC | 5 |
| Number of HAVIPs that can be associated with each ECS instance | 5 |
| Number of HAVIPs that can be associated with each secondary ENI | 5 |
| Number of ECS instances that can be associated with each HAVIP | 2 |
| Number of secondary ENIs that can be associated with each HAVIP | 2 |
| Number of route entries that point to an HAVIP in each VPC | 5 |

| Item | Default |
|---|---|
| Whether HAVIPs support broadcast or multicast communication | Not supported Not e HAVIPs support only unicasting. To implement high availability through third-party software such as Keepalived, you must modify the configuration file to change the communication method to unicasting. |

### 6.2 Create HAVIPs

High-availability virtual IP addresses (HAVIPs) are private IP addresses that can be created and released as independent resources. This topic describes how to create HAVIPs in the console. Prerequisites The HAVIP feature is in public preview. To use this feature,. A virtual private cloud (VPC) and vSwitches are created. For more information, see Create and manage a VPC and Create and manage a vSwitch. A VPC and vSwitches are created. For more information, see Create a VPC and Create and manage a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top menu bar, select the region where you want to create the HAVIP.
4. On the HaVip page, click Creat e HaVip.
5. On the Creat e a high-availabilit y virt ual IP address page, set the following parameters and
click Submit t ed to create an HAVIP.

| Parameter | Description |
|---|---|
| T issue | Select the organization to which the HAVIP belongs. |
| Resource Set | Select the resource set to which the HAVIP belongs. |
| Region | Select the region where you want to create the HAVIP. |
| Propriet ary Net work vpc | Select the VPC to which the HAVIP that you want to create belongs. |
| vswit ch | Select the vSwitch to which the HAVIP that you want to create belongs. |

| Parameter | Description |
|---|---|
| Privat e IP Address | Specify a private IP address for the HAVIP. Not e You must specify an idle private IP address that falls within the CIDR block of the vSwitch. |

### 6.3 Associate HAVIPs with backend cloud resources

cloud resources

#### 6.3.1 Associate an HAVIP with an ECS instance

This topic describes how to associate a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance that is deployed in a virtual private clouds (VPC). After you associate an HAVIP with an ECS instance, the ECS instance can send Address Resolution Protocol (ARP) messages to advertise the HAVIP. This way, the ECS instance can use more than one private IP address. Each HAVIP can be associated with at most two ECS instances. Prerequisites An ECS instance is created. For more information, see in the Creat e an ECS inst ance topic in Quick St art of Elastic Compute Service User Guide. Context You can associate an HAVIP with two ECS instances or two secondary elastic network interfaces (ENIs). However, you cannot associate an HAVIP with an ECS instance and a secondary ENI at the same time.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip Addresses page, find the HAVIP that you want to manage and click Manage in the
Act ions column.
5. In the Resources section, find ENI (Primary) or ENI (St andby) and click Bind.
6. In the dialog box that appears, set the following parameters to associate the HAVIP with an ECS
instance.

| Parameter | Description |
|---|---|
| Resource T ype | Select the type of resource with which you want to associate the HAVIP. Valid values: ECS Inst ances ENI In this example, ECS Inst ances is selected. |
| Bind Resource | Select the ECS instance with which you want to associate the HAVIP. The ECS instance that you select must meet the following requirements: The ECS instance is deployed in a VPC. The ECS instance and the HAVIP belong to the same vSwitch. |

7. Click OK.

#### 6.3.2 Associate an HAVIP with an ENI

This topic describes how to associate a high-availability virtual IP address (HAVIP) with ENIs that are attached to Elastic Compute Service (ECS) instances. Then, the ECS instances can send Address Resolution Protocol (ARP) messages to advertise the HAVIP. This way, the ECS instances can use more than one private IP address. Prerequisites An ENI is created. For more information, see the Creat e an Elast ic Net work Int erf ace topic in the Elast ic Net work Int erf ace chapter of Elastic Compute Service User Guide. Context You can associate each HAVIP with two ECS instances or two ENIs. However, you cannot associate an HAVIP with an ECS instance and an ENI at the same time.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip Addresses page, find the HAVIP that you want to associate and click its ID.
5. In the Resources section, find ENI (Primary) or ENI (St andby) and click Bind.
6. In the dialog box that appears, set the following parameters and click OK.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Resource T ype | Select the type of resource with which you want to associate the HAVIP. Valid values: ECS Inst ance ENI In this example, ENI is selected. |
| Bind Resource | Select the ENI with which you want to associate the HAVIP. The ENI and the HAVIP must belong to the same vSwitch. |

### 6.4 Associate HAVIPs with EIPs

This topic describes how to associate high-availability virtual IP addresses (HAVIPs) with elastic IP addresses (EIPs). After you associate an HAVIP with an EIP, the HAVIP can use the EIP to provide services over the Internet. Prerequisites An EIP is created. For more information, see Creat e an EIP in Quick St art of the Elastic IP Address User Guide.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top menu bar, select the region where the HAVIP is created.
4. On the HaVip Addresses page, find the HAVIP that you want to manage, and choose More >
Bind EIP Address in the Act ions column.
5. In the dialog box that appears, select the EIP with which you want to associate the HAVIP and click
OK. The EIP with which you want to associate the HAVIP must meet the following requirements: The EIP and HAVIP are created in the same region. The EIP must be in the Available state.

### 6.5 Disassociate HAVIPs from backend cloud resources

backend cloud resources

#### 6.5.1 Disassociate an HAVIP from an ECS instance

instance This topic describes how to disassociate a high-availability virtual private IP address (HAVIP) from an Elastic Compute Service (ECS) instance. After you disassociate an HAVIP from an ECS instance, the ECS instance cannot send Address Resolution Protocol (ARP) messages to advertise the HAVIP.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip page, find the HAVIP that you want to manage and click Manage in the Act ions
column.
5. In the Resources section, find the ECS instance that you want to manage and click Unbind.
6. In the message that appears, click OK.

#### 6.5.2 Disassociate an HAVIP from an ENI

This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic network interface (ENI). After you disassociate an HAVIP from an ENI, the Elastic Compute Service (ECS) instance with which the ENI is associated cannot send Address Resolution Protocol (ARP) messages to advertise the HAVIP.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip page, find the HAVIP that you want to disassociate and click Manage in the Act ions
column.
5. In the Resources section, find the ENI that you want to manage and click Unbind.
6. In the message that appears, click OK.

### 6.6 Disassociate an HAVIP from an EIP

EIP This topic describes how to disassociate a high-availability virtual IP address (HAVIP) from an elastic IP address (EIP).
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip Addresses.
3. Select the region to which the HAVIP belongs.
4. On the HaVip Addresses page, find the HAVIP that you want to manage and choose More >
Unbind wit h EIP in the Act ions column.
5. In the message that appears, click OK.

### 6.7 Delete an HAVIP

This topic describes how to delete a high-availability virtual IP address (HAVIP). Prerequisites The HAVIP that you want to delete is not associated with an elastic IP address (EIP). If the HAVIP is associated with an EIP, disassociate the HAVIP from the EIP first. For more information, see Disassociate HAVIPs from EIPs. The HAVIP is not associated with an Elastic Compute Service (ECS) instance. If the HAVIP is associated with an ECS instance, disassociate the HAVIP from the ECS instance. For more information, see Disassociate an HAVIP from an ECS instance. The HAVIP is not associated with a secondary elastic network interface (ENI). If the HAVIP is associated with a secondary ENI, disassociate the HAVIP from the secondary ENI first. For more information, see Disassociate HAVIPs from secondary ENIs.
1. Log on to the VPC console.
2. In the left-side navigation pane, click HaVip.
3. In the top navigation bar, select the region where the HAVIP is created.
4. On the HaVip page, find the HAVIP that you want to manage and choose More > Delet e in the
Act ions column.
5. In the message that appears, click OK.

## 7 Network ACLs

### 7.1 Overview

Network access control lists (ACLs) allow you to regulate access control for a virtual private cloud (VPC). You can create network ACL rules and associate a network ACL with a vSwitch. This allows you to control inbound and outbound traffic of Elastic Compute Service (ECS) instances that are associated with the vSwitch. Features Network ACLs have the following features: A network ACL is used to filter inbound and outbound network traffic of ECS instances that are associated with a vSwitch in a VPC. The network traffic forwarded to ECS instances by Server Load Balancer (SLB) instances is also filtered. Network ACLs are stateless. You must set both inbound and outbound rules. Otherwise, the system may fail to respond to requests. If you create a network ACL that does not contain a rule, all inbound and outbound access are denied. If a network ACL is associated with a vSwitch, the network ACL does not filter the traffic forwarded between ECS instances that are associated with the vSwitch. Network ACL rules You can add rules to or delete rules from a network ACL. Changes to the rules are automatically synchronized to the associated vSwitch. By default, an inbound and an outbound rule are automatically added to a newly created network ACL. These rules allow all inbound and outbound network traffic transmitted through the associated vSwitch. You can delete the default rules. The following table lists the default inbound and outbound rules. Default inbound rule

| Priority | Protocol | Source CIDR block | Destination port range | Action | Type |
|---|---|---|---|---|---|
| 1 | all | 0.0.0.0/0 | -1/-1 | Allow | Custom |

Default outbound rule

| Priority | Protocol | Destination CIDR block | Destination port range | Action | Type |
|---|---|---|---|---|---|
| 1 | all | 0.0.0.0/0 | -1/-1 | Allow | Custom |

A network ACL contains the following parameters: Priority: A smaller value indicates a higher priority. The system attempts to match traffic requests with rules in descending order of priority that starts from the rule whose priority is 1. If a request matches a rule, the system applies the rule to the request and ignores the other rules. For example, the following rules are added and requests destined for IP address 172.16.0.1 are sent from an ECS instance. In the following table, the requests match Rules 2 and 3. Rule 2 has a higher priority than Rule 3. Therefore, the system applies Rule 2. Based on the action of Rule 2, the requests are denied.

| Priority | Protocol | Destination CIDR block | Destination port range | Action | Type |
|---|---|---|---|---|---|
| 1 | all | 10.0.0.0/8 | -1/-1 | Allow | Custom |
| 2 | all | 172.16.0.0/12 | -1/-1 | Block | Custom |
| 3 | all | 172.16.0.0/12 | -1/-1 | Allow | Custom |

Policy: specifies whether to allow or block specific traffic. Protocol: the protocol type. Available options include All, ICMP, GRE, TCP, and UDP. Source CIDR block: the source CIDR block from which inbound traffic is transmitted. Destination CIDR block: the destination CIDR block to which outbound traffic is transmitted. Destination port range: the range of destination ports to which the inbound rule applies. Destination port range: the range of destination ports to which the outbound rule applies. Comparison between network ACLs and security groups Network ACLs control data transmitted through associated vSwitches while security groups control data transmitted through associated ECS instances. The following table lists the differences between network ACLs and security groups.

| Network ACL | Security group |
|---|---|
| Applied to vSwitches. | Applied to instances. |

| Network ACL | Security group |
|---|---|
| Stateless: Returned traffic must be allowed by inbound rules. | Stateful: Returned traffic is automatically allowed and not affected by rules. |
| The system attempts to match requests with rules in descending order of priority. Not all rules are matched. | The system matches a request against all rules before a rule is applied. |
| Each vSwitch can be associated with only one network ACL. | Each ECS instance can be added to more than one security group. |

The following figure shows how network ACLs and security groups are applied to ensure network security. Limits Before you use network ACLs, take note of the following limits.

| Item | Default |
|---|---|
| Number of network ACLs that can be created in each VPC | 200 |

| Item | Default |
|---|---|
| Number of network ACLs that can be associated with each vSwitch | 1 |
| Number of rules that can be added to a network ACL | Inbound rules: 20 Outbound rules: 20 |

The following flowchart shows how to use a network ACL. Manage intercommunication among ECS instances connected to different vSwitches. Manage communication between a data center and a VPC.

### 7.2 Scenarios

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

| Port | Service | Description |
|---|---|---|
| 443 | HTTPS | The HTTPS port. It is used to access services. The HTTPS protocol can implement encrypted and secure data transmission. |
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

| Effectiv e order | Protocol | Source IP address es | Destinat ion port range | Action | Description |
|---|---|---|---|---|---|
| 2 | TCP | 0.0.0.0/ 0 | 443/443 | Accept | Allows inbound HTTPS traffic from any IPv4 addresses. |
| 3 | TCP | 0.0.0.0/ 0 | 22/22 | Accept | Allows inbound SSH traffic from any IPv4 addresses. |
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

### 7.3 Create a network ACL

A network access control list (ACL) allows you to manage network access in a virtual private cloud (VPC). This topic describes how to create a network ACL in a VPC. Prerequisites A VPC is created. For more information, see Create a VPC.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where you want to create the network ACL.
4. On the Net work ACL page, click Creat e Net work ACL.
5. In the Creat e Net work ACL dialog box, set the following parameters, and click OK.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the network ACL belongs. |
| Resource Set | Select the resource set to which the network ACL belongs. |
| Region | Select the region where you want to deploy the network ACL. |
| Name | Enter a name for the network ACL. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), and hyphens (-). It must start with a letter. _ |
| Descript ion | Enter a description for the network ACL. The description must be 2 to 256 characters in length, and can contain letters, digits, underscores ( ), colons (:), and hyphens (-). It must start with a letter and _ cannot start with http:// or https:// . |
| VPC | Select the VPC for which you want to create the network ACL. Not e The VPC and network ACL must be deployed in the same region. |

What's next

### 7.4 Associate a network ACL with a vSwitch

vSwitch After you create a network access control list (ACL), you can associate the network ACL with a vSwitch. This way, you can use the network ACL to manage the traffic of the Elastic Compute Service (ECS) instances in the vSwitch. Prerequisites Before you associate a network ACL with a vSwitch, make sure that the following requirements are met: A network ACL is created. For more information, see Work with network ACLs. A vSwitch is created. The vSwitch and network ACL belong to the same virtual private cloud (VPC). For more information, see Create and manage a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL that you want to manage and click Manage in
the Act ions column.
5. On the Resources tab, click Bind Resource.
6. In the Associat e vSwit ch panel, select the vSwitch and click OK.
Not e The network ACL and vSwitch must belong to the same VPC. A vSwitch can be associated with only one network ACL. What's next

### 7.5 Add network ACL rules

#### 7.5.1 Add an inbound rule

This topic describes how to add an inbound rule to a network access control list (ACL). You can use inbound rules to control Internet or internal network traffic destined for Elastic Compute Service (ECS) instances connected to a vSwitch. Prerequisites A network ACL is created. For more information, see Work with network ACLs.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL that you want to manage and click Inbound
Rule in the Act ions column.
5. On the Inbound Rule tab, click Creat e Inbound Rule.
6. In the Creat e Inbound Rule panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Name | Enter a name for the inbound rule. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter. It cannot start _ with http:// or https:// . |
| Ef f ect ive order | The order in which the inbound rule takes effect. Valid values: 1 to 20. A smaller number indicates a higher priority. |
| Act ion | Select an action for the inbound rule. Valid values: Accept : accepts network traffic that is destined for the ECS instances connected to the vSwitch. Drop: denies network traffic that is destined for the ECS instances connected to the vSwitch. |
| Prot ocol T ype | Select a transport layer protocol. Valid values: ALL ICMP GRE T CP UDP |
| Source IP Addresses | The source CIDR block from which data is transmitted. Default value: 0.0.0.0/32. |
| Dest inat ion Port Range | Enter the destination port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the highest and lowest values in a port range, for example, 1/200 or 80/80. -1/-1 indicates that all ports are available. You cannot set the value to -1/-1. |

#### 7.5.2 Add an outbound rule

This topic describes how to add an outbound rule to a network access control list (ACL). You can use outbound rules to control how Elastic Compute Service (ECS) instances connected to a vSwitch access the Internet or other internal networks. Prerequisites A network ACL is created. For more information, see Work with network ACLs.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL and click Out bound Rule in the Act ions column.
5. On the Out bound Rule tab, click Creat e Out bound Rule.
6. In the Creat e Out bound Rule panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Name | Enter a name for the outbound rule. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name must start with a letter. It cannot start _ with http:// or https:// . |
| Ef f ect ive order | The order in which the outbound rule takes effect. Valid values: 1 to 20. A smaller number indicates a higher priority. |
| Policy | Select an action for the outbound rule. Valid values: Accept : allows ECS instances connected to the vSwitch to access the Internet or other internal networks. Drop: forbids ECS instances connected to the vSwitch to access the Internet or other internal networks. |
| Prot ocol T ype | Select a transport layer protocol. Valid values: ALL ICMP GRE T CP UDP |
| Dest inat ion IP Addresses | The destination CIDR block to which data is transmitted. Default value: 0.0.0.0/32. |
| Dest inat ion Port Range | Enter the destination port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the highest and lowest values in a port range, for example, 1/200 or 80/80. -1/-1 indicates that all ports are available. You cannot set the value to -1/-1. |

#### 7.5.3 Change the priority of a network ACL rule

Rules added to network access control lists (ACLs) take effect in descending order of priority. A smaller value indicates a higher priority. You can change the priority of a network ACL rule to meet your business requirements. Change the priority of an inbound rule
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL that you want to manage and click Manage in
the Act ions column.
5. Click the Inbound Rule tab and click Sort .
6. In the Sort panel, change the priority of the rule by dragging and dropping the rule. Then, click OK.
Not e Rules are listed in descending order of priority. Change the priority of an outbound rule
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL and click Manage in the Act ions column.
5. Click the Out bound Rule tab and click Sort .
6. In the Sort panel, change the priority of the rule by dragging and dropping the rule. Then, click OK.
Not e Rules are listed in descending order of priority.

### 7.6 Disassociate a network ACL from a vSwitch

a vSwitch This topic describes how to disassociate a network access control list (ACL) from a vSwitch. After you disassociate a network ACL from a vSwitch, the network ACL no longer controls the traffic of Elastic Compute Service (ECS) instances that belong to the vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL and click Manage in the Act ions column.
5. On the Resources tab, find the vSwitch and click Unbind in the Act ions column.
6. In the Unbind Net work ACL message, click OK.

### 7.7 Delete a network ACL

This topic describes how to delete a network access control list (ACL). Prerequisites Make sure that the network ACL is not associated with a vSwitch. If the network ACL is associated with a vSwitch, disassociate the network ACL from the vSwitch first. For more information, see Disassociate a VSwitch from a network ACL.
1. Log on to the VPC console.
2. In the left-side navigation pane, click Net work ACL.
3. In the top navigation bar, select the region where the network ACL is created.
4. On the Net work ACL page, find the network ACL that you want to delete and click Delet e in the
Act ions column.
5. In the Delet e Net work ACL message, click OK.
