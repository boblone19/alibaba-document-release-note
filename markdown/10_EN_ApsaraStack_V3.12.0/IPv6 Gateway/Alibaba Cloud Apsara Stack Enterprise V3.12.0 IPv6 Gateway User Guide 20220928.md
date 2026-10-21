---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 IPv6 Gateway User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 25
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 IPv6 Gateway User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20IPv6%20Gateway%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 IPv6 Gateway User Guide 20220928

## Table of Contents

- 1 What is an IPv6 Gateway?
- 2 Log on to the IPv6 Gateway console
- 3 Quick start
  - 3.1 Create an IPv6 VPC
- 4 Enable IPv6 for VPCs
  - 4.1 Create an IPv4 and IPv6 dual-stack VPC
  - 4.2 Enable an IPv6 CIDR block for a VPC network
- 5 Enable IPv6 for vSwitches
  - 5.1 Create an IPv4 and IPv6 dual-stack VSwitch
  - 5.2 Enable IPv6 for a vSwitch
- 6 Manage IPv6 Gateways
  - 6.1 Editions of IPv6 gateways
  - 6.2 Create an IPv6 gateway
  - 6.3 Modify an IPv6 gateway
  - 6.4 Delete an IPv6 gateway
- 7 Manage IPv6 Internet bandwidth
  - 7.1 Enable Internet connectivity for an IPv6 address
  - 7.2 Modify the maximum bandwidth of an IPv6 address
  - 7.3 Disable Internet connectivity for an IPv6 address
- 8 Manage egress-only rules
  - 8.1 Create an egress-only rule
  - 8.2 Delete an egress-only rule

?

## 1 What is an IPv6 Gateway?

This topic provides an overview of the IPv6 Gateways of Virtual Private Cloud (VPC). An IPv6 Gateway functions as an IPv6 traffic gateway for a VPC. You can configure the IPv6 Internet bandwidth and egress-only rules to manage the inbound and outbound IPv6 traffic. Functions The functions of an IPv6 gateway are as follows: IPv6 int ernal net work communicat ion By default, an IPv6 address in a VPC is allocated with an Internet bandwidth of 0 Mbit/s and only supports communication over the internal network. Specifically, the cloud instances in a VPC can only access other IPv6 addresses in the same VPC through the IPv6 address. The resources cannot access the Internet with these IPv6 addresses or be accessed by IPv6 clients over the Internet. IPv6 public net work communicat ion You can purchase an Internet bandwidth for the IPv6 address for which you have applied. In this way, the resources in the VPC can access the Internet through the IPv6 address and be accessed by IPv6 clients over the Internet. You can set the Internet bandwidth to 0 Mbit/s at any time to deny the IPv6 address Internet access. After this configuration, the IPv6 address can only communicate over the internal network. IPv6 public net work communicat ion wit h an egress-only rule You can set an egress-only rule for an IPv6 Gateway. In this way, the IPv6 address can access the Internet, but IPv6 clients are denied access to your cloud resources in the VPC over the Internet. You can delete the egress-only rule at any time. After the rule is deleted, your resources in the VPC can access the Internet through the IPv6 address for which you have purchased Internet bandwidth, and IPv6 clients can access the resources in the VPC over the Internet. The network access capability of IPv6 addresses is dependent on the settings of the network type, Internet bandwidth, and egress-only rule, as shown in the following table. ?

| IPv6 network type | Enable IPv6 Internet bandwidth? | Set an egress-only rule? | IPv6 network access capability |
|---|---|---|---|
| Internal network | No | No | Internal network communication |
| Public network | Yes | No | Internal network communication Public network communication |
|   |   | Yes | Internal network communication Public network communication when access is initiated by VPCs |

Benefits IPv6 Gateway provides the following benefits: High availabilit y IPv6 Gateways provide cross-zone high availability and stable IPv6 Internet gateway services. High perf ormance A single IPv6 Gateway provides a 10-gigabit level throughput. Flexible management of public net work communicat ion You can manage the Internet communication capability of an IPv6 Gateway by adjusting its Internet bandwidth and setting an egress-only rule. way console

## 2 Log on to the IPv6 Gateway console

console This topic provides an example of how to use Google Chrome to log on to the IPv6 Gateway console in the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Net working > IPv6 Gat eway.

## 3 Quick start

### 3.1 Create an IPv6 VPC

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

|   | ps:// |
|---|---|

| Parameter | Description |   |   |
|---|---|---|---|
| IPv4 CIDR Block | Select an IPv4 CIDR block for the VPC. The following setting methods are supported: Recommended CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8. Cust om CIDR Block: Enter 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or a subset of these CIDR blocks. The subnet mask must be 8 to 28 bits in length. For example, enter 192.168.0.0/16. In this tutorial, select Recommended CIDR Block and then select 192.168.0.0/16. Not e After you create a VPC, you cannot change its IPv4 CIDR block. |   |   |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block to the VPC. Do Not Assign: No IPv6 CIDR block will be assigned to the VPC. Assign: An IPv6 CIDR block will be automatically assigned to the VPC. In this tutorial, select Assign. |   |   |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length and can contain letters, Chinese characters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or a Chinese character and cannot start with http:// or htt ps:// . |   |   |
|   |   | htt |   |

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

| User | Guide·Quick start | IPv6 Gatewa |
|---|---|---|

| Parameter | Description |
|---|---|
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

| IPv6 | Gateway | User Guide·Quick star | t |
|---|---|---|---|

| Parameter | Description |
|---|---|
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

## 4 Enable IPv6 for VPCs

### 4.1 Create an IPv4 and IPv6 dual-stack VPC

stack VPC This topic describes how to configure both IPv4 and IPv6 CIDR blocks for a VPC when you create the VPC. By default, all VPCs are associated with IPv4 CIDR blocks which cannot be deleted. However, you can choose whether to allocate an IPv6 CIDR blocks to a VPC. After you choose to allocate an IPv6 CIDR block to a VPC, the system creates an IPv6 gateway of the Free Edition for the VPC for you to provision IPv6 bandwidth and manage IPv6 traffic.
1. Log on to the VPC console.
2. On the top of the page, select a region to deploy your VPC.
3. On the VPCs page, click Creat e VPC.
4. On the Creat e VPC page, configure the VPC network and click Submit . The following table
describes the configuration parameters.

| Parameter | Description |
|---|---|
| Organiza t ion | Select the organization to which the VPC belongs. |
| Resource Set | Select the resource set to which the VPC belongs. |
| Region | Select a region to deploy the VPC. |
| Share wit h Sub- organiza t ions | Specify whether to share the VPC. If you select Yes, administrators of sub-organizations can create resources in the VPC network. |
| VPC Name | Enter a name for the VPC. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with a _ letter and cannot start with http:// or https:// . |

| Parameter | Description |
|---|---|
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VPC. The following setting methods are supported: Recommended CIDR Block: Use 192.168.0.0/16, 172.16.0.0/12, or 10.0.0.0/8 as the IPv4 CIDR block of the VPC. Cust om CIDR Block: Use 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8, or one of their subnets as the IPv4 CIDR block of the VPC. The subnet mask must be 8 to 24 bits in length. For example, enter 192.168.0.0/16. Not e After you create a VPC, you cannot modify its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify whether to assign an IPv6 CIDR block to the VPC. In this example, select Assign. If you set this parameter to Assign, the system automatically creates an IPv6 gateway of the Free Edition for your VPC and assigns an IPv6 CIDR block with the subnet mask /61, such as 2xx1:db8::/61. By default, IPv6 addresses can only be used for communication within private networks. If you need to enable an IPv6 address to access and be accessed over the Internet, you must purchase IPv6 Internet bandwidth for the IPv6 address. For more information, see Enable Internet connectivity for an IPv6 address. Not e After you create a VPC, you cannot modify its IPv6 CIDR block. |
| Descript i on | Enter a description for the VPC. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start with a _ letter and cannot start with http:// or https:// . |

### 4.2 Enable an IPv6 CIDR block for a VPC network

VPC network This topic describes how to enable an IPv6 CIDR block for a Virtual Private Cloud (VPC) network. After the IPv6 CIDR block is enabled, the system automatically creates an IPv6 gateway free of charge for the VPC network. You can use the IPv6 Gateway to manage the IPv6 Internet bandwidth and set egressonly rules.
1. Log on to the VPC console.
2. Select the region where your VPC network is deployed.
3. On the VPCs page, find the target VPC network and click Enable IPv6 CIDR Block in the IPv6 CIDR
Block column.
4. In the Enable IPv6 CIDR Block dialog box, select Enable IPv6 CIDR Block of all VSwit ches in
VPC, and then click OK. If you do not select Enable IPv6 CIDR Block of all VSwit ches in VPC, you must enable IPv6 CIDR Block for each VSwitch. For more information, see Enable IPv6 for a vSwitch. s

## 5 Enable IPv6 for vSwitches

### 5.1 Create an IPv4 and IPv6 dual-stack VSwitch

stack VSwitch This topic describes how to assign an IPv6 CIDR block to a VSwitch when you create the VSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click VSwit ches.
3. Select the region where you want to deploy the VSwitch.
4. On the VSwit ches page, click Creat e VSwit ch.
5. On the VSwit ch page, configure the VSwitch and click Submit . The following table describes the
configuration parameters.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the VSwitch belongs. |
| Resource Set | Select the resource set to which the VSwitch belongs. |
| Region | Select a region to deploy the VSwitch. |
| Zone | Select a zone to deploy the VSwitch. Each VSwitch must reside entirely within one zone and cannot span multiple zones. However, you can deploy cloud resources in VSwitches of different zones to achieve cross-zone disaster recovery. Not e Each cloud resource can be deployed in only one VSwitch. |
| VPC | Select the VPC for which you want to create the VSwitch. |
| Dedicat ed f or Of f -Cloud Servers | Specify whether the VSwitch is dedicated for off-cloud servers. For more information, see the Feat ures of of f -cloud servers f or VPCtopic in the Apsara Stack Bare Metal Server User Guide. |
| VSwit ch Name | Enter a name for the VSwitch. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must start _ with a letter and cannot start with http:// or https:// . |

s

| Parameter | Description |
|---|---|
| IPv4 CIDR Block | Specify an IPv4 CIDR block for the VSwitch. You must specify the IP address range for the VSwitch in the form of a CIDR block. The IPv4 CIDR block size for a VSwitch is between a 16-bit mask and a 29- bit mask. It means that 8 to 65,536 IP addresses can be provided. The IPv4 CIDR block of a VSwitch must be a subset of the IPv4 CIDR block of the VPC this VSwitch resides in. The first and the last three IP addresses of each VSwitch IPv4 CIDR block are reserved. For example, if the VSwitch IPv4 CIDR block is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The IPv4 CIDR block of a VSwitch must be more specific than the CIDR range of a route in any of the VPC route tables. After you create a VSwitch, you cannot modify its IPv4 CIDR block. |
| IPv6 CIDR Block | Specify an IPv6 CIDR block for the VSwitch. The default subnet mask for the IPv6 CIDR block of a VSwitch is /64. You can enter a decimal number ranging from 0 to 255 to define the last 8 bits of the IPv6 CIDR block. For example, if the IPv6 CIDR block of the VPC that contains the VSwitch is 2xx1:db8::/64, you can enter 255 (FF in hexadecimal notation) in this field to define the IPv6 CIDR block of the VSwitch as 2xx1:db8:ff::/64. |
| Descript ion | Enter a description for the VSwitch. The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must _ start with a letter and cannot start with http:// or https:// . |

### 5.2 Enable IPv6 for a vSwitch

This topic describes how to allocate an IPv6 CIDR block to a vSwitch.
1. Log on to the VPC console.
2. In the left-side navigation pane, click vSwit ches.
3. Select the region where your vSwitch resides.
4. On the vSwit ches page, find the target vSwitch, and click Enable IPv6 CIDR Block in the IPv6
CIDR Block column. s
5. (Optional)In the Enable IPv6 CIDR Block dialog box, click OK.
Not e This operation is required only when IPv6 is not enabled for the VPC to which the vSwitch belongs.
6. Specify an IPv6 CIDR block and click OK.
The default subnet mask for the IPv6 CIDR block of a vSwitch is /64. You can enter a decimal number ranging from 0 to 255 to define the last 8 bits of the IPv6 CIDR block. For example, if the IPv6 CIDR block of the VPC that contains the vSwitch is 2xx1:db8::/64, you can enter 255 (FF in hexadecimal notation) in this field to define the IPv6 CIDR block of the vSwitch as 2xx1:db8::ff/64.

## 6 Manage IPv6 Gateways

### 6.1 Editions of IPv6 gateways

This topic describes the different editions of IPv6 gateways. Different quotas and limits apply to IPv6 gateways of different editions, such as the maximum forwarding bandwidth, maximum IPv6 bandwidth per IPv6 address, and maximum number of egress-only rules.

| IPv6 gateway edition | Maximum forwarding bandwidth | Maximum IPv6 bandwidth per IPv6 address | Maximum number of egress-only rules |
|---|---|---|---|
| Free Edition | 10 Gbit/s | 2 Gbit/s | 0 |
| Enterprise Edition | 20 Gbit/s | 2 Gbit/s | 50 |
| Enhanced Enterprise Edition | 50 Gbit/s | 2 Gbit/s | 200 |

### 6.2 Create an IPv6 gateway

This topic describes how to create an IPv6 gateway for a VPC. After you create an IPv6 gateway, you can purchase IPv6 Internet bandwidth and set egress-only rules for the IPv6 gateway. Prerequisites Make sure that IPv6 is enabled for the VPC before you create an IPv6 gateway for the VPC. For more information, see Allocate an IPv6 CIDR block when you create a VPC and Enable an IPv6 CIDR block for a VPC network.
1. Log on to the IPv6 Gateway console.
2. On the IPv6 Gat eway page, click Creat e IPv6 Gat eway.
3. Configure the IPv6 gateway and click Submit . The following table describes the configuration
parameters.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the IPv6 gateway belongs. |
| Resource Set | Select the resource set to which the IPv6 gateway belongs. |
| Region | Select a region to deploy the IPv6 gateway. The IPv6 gateway must belong to the same region as the VPC for which you want to create the IPv6 gateway. |

| Parameter | Description |
|---|---|
| VPC | Select the VPC for which you want to create an IPv6 gateway. The target VPC may not be available due to the following reasons: Only one IPv6 gateway can be created for each VPC. The VPC already has an IPv6 gateway. The VPC has a custom route with the destination CIDR block set to ::/0. If this happens, you must delete this custom route before you can create an IPv6 gateway for the VPC. Not e After an IPv6 gateway is created, you cannot change the VPC that is associated with the IPv6 gateway. |
| Edit ion | Select the edition of the IPv6 gateway. IPv6 gateways are available in the following editions: Free Edition Enterprise Edition Enhanced Enterprise Edition Different quotas and limits apply to IPv6 gateways of different editions, such as the maximum forwarding bandwidth, maximum IPv6 bandwidth per IPv6 address, and maximum number of egress-only rules. For more information, see Editions of IPv6 gateways. |

### 6.3 Modify an IPv6 gateway

This topic describes how to modify the name and description of an IPv6 gateway.
1. Log on to the IPv6 Gateway console.
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Manage in the Act ions
column.
4. On the IPv6 Gat eway Det ails page, click Edit next to Name. In the dialog box that appears, enter
a new name for the IPv6 gateway, and click OK. The name must be 2 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
5. Click Edit next to Descript ion. In the dialog box that appears, enter a new description for the IPv6
gateway and click OK. The description must be 2 to 256 characters in length and cannot start with `http://` or `https:` `//` .

### 6.4 Delete an IPv6 gateway

This topic describes how to delete an IPv6 gateway. If a VPC no longer needs to access or be accessed by IPv6 clients, you can delete the IPv6 gateway associated with the VPC. Prerequisites Before you delete an IPv6 gateway of the enterprise edition or enhanced enterprise edition, you must delete the egress-only rules of the IPv6 gateway. For more information, see Delete an egress-only rule.
1. Log on to the IPv6 Gateway console.
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Delet e in the Act ions column.
4. In the dialog box that appears, click OK.
ndwidth

## 7 Manage IPv6 Internet bandwidth

bandwidth

### 7.1 Enable Internet connectivity for an IPv6 address

an IPv6 address This topic describes how to enable Internet bandwidth for an IPv6 address. After Internet bandwidth is enabled for an IPv6 address, the IPv6 address can be used to communicate over the Internet. Prerequisites An ECS instance is created in the VPC associated with the corresponding IPv6 gateway and is configured with an IPv6 address.
1. Log on to the IPv6 Gateway console.
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Manage in the Act ions
column.
4. In the left-side navigation pane, click IPv6 Int ernet Bandwidt h.
5. On the IPv6 Int ernet Bandwidt h page, find the target IPv6 address, and click Enable IPv6
Int ernet Bandwidt h in the Act ions column.
6. Specify a bandwidth and click Submit .
An IPv6 gateway of the Free Edition, Enterprise Edition, or Enhanced Enterprise Edition supports a 2 Gbit/s maximum bandwidth per IPv6 address.

### 7.2 Modify the maximum bandwidth of an IPv6 address

of an IPv6 address This topic describes how to modify the maximum bandwidth of an IPv6 address. The modification takes effect immediately.
1. Log on to the IPv6 Gateway console.
ndwidth
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Manage in the Act ions
column.
4. In the left-side navigation pane, click IPv6 Int ernet Bandwidt h.
5. In the IPv6 AddressList section, find the target IPv6 address, and choose More > Modif y IPv6
Int ernet Bandwidt h in the Act ions column.
6. Specify a bandwidth and click Submit .

### 7.3 Disable Internet connectivity for an IPv6 address

an IPv6 address This topic describes how to delete the Internet bandwidth of an IPv6 address that is no longer needed for Internet communication.
1. Log on to the IPv6 Gateway console.
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Manage in the Act ions
column.
4. In the left-side navigation pane, click IPv6 Int ernet Bandwidt h.
5. In the IPv6 AddressList section, find the target IPv6 address, and click Delet e IPv6 Int ernet
Bandwidt h in the Act ions column.
6. In the dialog box that appears, click OK.
s

## 8 Manage egress-only rules

### 8.1 Create an egress-only rule

This topic describes how to create an egress-only rule. If you want an instance in the VPC associated with an IPv6 gateway to be able to access the Internet with an IPv6 address, while resources on the Internet cannot initiate communication with this instance, you can create an egress-only rule for the instance. Prerequisites IPv6 Internet bandwidth is enabled for the IPv6 address configured for the instance. For more information, see Enable and manage IPv6 Internet bandwidth. Context IPv6 gateways of the Free Edition do not support egress-only rules. IPv6 gateways of the enterprise edition and enterprise enhanced edition support a maximum of 50 and 200 egress-only rules respectively.
1. Log on to the IPv6 Gateway console.
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Manage in the Act ions
column.
4. In the left-side navigation pane, click Egress-only Rule.
5. On the Egress-only Rule page, click Creat e Egress-only Rule.
6. In the Creat e Egress-only Rule dialog box, select the ECS instance that uses the IPv6 address to
communicate with the Internet, and click OK.

### 8.2 Delete an egress-only rule

This topic describes how to delete an egress-only rule. After the rule is deleted, the IPv6 address with Internet bandwidth can access the Internet, and the instance associated with the IPv6 address can be accessed over the Internet.
1. Log on to the IPv6 Gateway console.
2. Select the region where the IPv6 gateway resides.
3. On the IPv6 Gat eway page, find the target IPv6 gateway, and click Manage in the Act ions
column.
4. In the left-side navigation pane, click Egress-only Rule.
5. On the Egress-only Rule page, find the egress-only rule that you want to delete, and click
Delet e in the Act ions column.
6. In the dialog box that appears, click OK.
