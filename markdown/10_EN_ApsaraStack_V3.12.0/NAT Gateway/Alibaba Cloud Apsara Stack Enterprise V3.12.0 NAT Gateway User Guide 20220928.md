---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 NAT Gateway User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 31
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 NAT Gateway User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20NAT%20Gateway%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 NAT Gateway User Guide 20220928

## Table of Contents

- 1 What is NAT Gateway?
- 2 Log on to the NAT Gateway console
- 3 Quick Start
  - 3.1 Overview
  - 3.2 Create a NAT gateway
  - 3.3 Associate an EIP with the a NAT gateway
  - 3.4 Create a DNAT entry
  - 3.5 Create an SNAT entry
- 4 Manage a NAT gateway
  - 4.1 Sizes of NAT gateways
  - 4.2 Create a NAT gateway
  - 4.3 Modify a NAT gateway
  - 4.4 Delete a NAT gateway
- 5 Manage EIPs
  - 5.1 Associate an EIP with a NAT gateway
  - 5.2 Disassociate an EIP from a NAT gateway
- 6 Manage a DNAT table
  - 6.1 DNAT table overview
  - 6.2 Create a DNAT entry
  - 6.3 Modify a DNAT entry
  - 6.4 Delete a DNAT entry
- 7 Manage an SNAT table
  - 7.1 SNAT table overview
  - 7.2 Create an SNAT entry
  - 7.3 Modify an SNAT entry
  - 7.4 Delete a SNAT entry
- 8 NAT service plan
  - 8.1 Create a NAT service plan
  - 8.2 Modify the bandwidth of a NAT service plan
  - 8.3 Add an IP address
  - 8.4 Release an IP address
  - 8.5 Delete a NAT service plan
- 9 Anti-DDoS Basic

## 1 What is NAT Gateway?

A NAT gateway is an enterprise-grade Internet gateway. NAT Gateway provides source network address translation (SNAT) and destination network address translation (DNAT) features, a maximum forwarding capacity of 10 Gbit/s, and support for cross-zone disaster recovery. Features NAT gateways must be associated with public IP addresses. After you create a NAT gateway, you can associate it with one or more elastic IP addresses (EIPs). NAT Gateway supports SNAT and DNAT. SNAT allows Elastic Compute Service (ECS) instances that are deployed in a virtual private cloud (VPC) and not associated with public IP addresses to access the Internet. DNAT maps public IP addresses of a NAT gateway to ECS instances so that the ECS instances can be accessible from the Internet. way console

## 2 Log on to the NAT Gateway console

console This topic describes how to use Google Chrome to log on to the NAT Gateway console in Apsara Stack Cloud Management (ASCM). Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Net work > NAT Gat eway.

## 3 Quick Start

### 3.1 Overview

This topic describes how to configure Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT). You can configure SNAT and DNAT to enable ECS instances in a Virtual Private Cloud (VPC) network to communicate with the Internet through a NAT gateway. Before you start, make sure that the following conditions are met: A VPC network is created. For more information, see VPC User Guide Creat e a VPC net work in the Quick St art chapter in the VPC User Guide. An ECS instance is created in the VPC network. For more information, see ECS User Guide Creat e an inst ance in the Quick St art chapter in the ECS User Guide. An elastic IP address (EIP) is created. For more information, see EIP User Guide Creat e an EIP in the Quick St art chapter in the EIP User Guide. In this topic, an ECS instance that is not associated with any public IP addresses in a VPC network is used as an example. The following flowchart shows how to associate an EIP with a NAT gateway: A NAT gateway is an enterprise-class gateway that provides NAT proxy services. Before you configure SNAT and DNAT entries, you must create a NAT gateway. For more information, see Create a NAT gateway.
2. Associate an EIP to a NAT gateway
A NAT gateway functions as expected only after it is associated with a public IP address. After you create a NAT gateway, you can associate it with an EIP. For more information, see Associate an EIP with a NAT Gateway. This topic describes how to create a Destination Network Address Translation (DNAT) entry. DNAT maps public IP addresses to Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network. This way, the ECS instances can receive requests sent over the Internet. DNAT supports port mapping and IP mapping. For more information, see Create a DNAT entry. This topic describes how to create a Source Network Address Translation (SNAT) entry. SNAT allows Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network to access the Internet without using public IP addresses. For more information, see Create a SNAT entry.

### 3.2 Create a NAT gateway

A NAT gateway is an enterprise-class gateway that provides NAT proxy services. Before you configure SNAT and DNAT entries, you must create a NAT gateway. A VPC network is created. For more information, see VPC User GuideCreat e a VPC net work in the Quick St art chapter in the VPC User Guide.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eway page, click Creat e NAT Gat eway.
3. Set the parameters for the NAT gateway based on the following information, and then click
Submit .

| Parameter | Description |
|---|---|
| Organizat ion | The organization to which the NAT gateway belongs. |
| Resource set | The resource set to which the NAT gateway belongs. |
| Region | The region where the NAT gateway is deployed. |
| VPC | The VPC network to which the NAT gateway belongs. If you cannot find the target VPC network in the list, perform the following operations: Check whether the VPC network is already associated with a NAT gateway. Each VPC network can be associated with only one NAT gateway. Check whether the VPC network has a custom route entry with the destination CIDR block set to 0.0.0.0/0. If such a custom route entry exists, delete it. Check whether the RAM user is authorized to access the VPC network. If the RAM user is not authorized, contact your Alibaba Cloud account owner to grant permissions. |

| Parameter | Description |
|---|---|
| Specif icat ion | Select the size of the NAT gateway. Valid values: Small: supports up to 10,000 SNAT connections. Medium: supports up to 50,000 SNAT connections. Large: supports up to 200,000 SNAT connections. Super Large: supports up to 1,000,000 SNAT connections. Not e The size of a NAT gateway determines the maximum number of SNAT connections, but it does not affect the maximum number of DNAT connections. |
| Paramet er | Enter a name for the NAT gateway. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or Chinese character but cannot start with http:// or https:// . |

### 3.3 Associate an EIP with the a NAT gateway

gateway A NAT gateway functions as expected only after it is associated with a public IP address. After you create a NAT gateway, you can associate it with an elastic IP address (EIP). Context You can associate an EIP or a NAT service plan with a NAT gateway. However, you can choose only one of them for the NAT gateway. If you want to associate a NAT service plan with a NAT gateway, you must purchase a NAT service plan first. Then, you can configure the SNAT or DNAT feature for the NAT gateway. For more information, see Create a NAT service plan.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eways page, find the NAT gateway, and choose
> Bind Elast ic IP Address in

the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters, and then click OK.

| Parameter | Description |
|---|---|
| Usable EIP list | Select the EIP that is used to access the Internet. |

| Parameter | Description |
|---|---|
| VSwit ch | Select the VSwitch for which you want to add SNAT entries. After a VSwitch is selected, the system automatically adds an SNAT entry so that Alibaba cloud services in the VSwitch can access the Internet. You can also skip this step and manually add SNAT entries after you associate an EIP with the NAT gateway. For more information, see Create a SNAT entry. |

### 3.4 Create a DNAT entry

This topic describes how to create a Destination Network Address Translation (DNAT) entry. DNAT maps public IP addresses to Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network. This way, the ECS instances can receive requests sent over the Internet. DNAT supports port mapping and IP mapping.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eways page, find the target NAT gateway, and click Conf igure DNAT in the
Act ions column.
4. On the DNAT T able page, click Creat e DNAT Ent ry.
5. On the Creat e DNAT Ent ry page, set the following parameters, and then click OK.

| Parameter | Description |
|---|---|
| Public IP address | Select an available public IP address. Not e If a public IP address is already used in a SNAT entry, it cannot be used to create a DNAT entry. |
| Privat e IP address | Select the ECS instance that uses the DNAT entry to receive requests from the Internet. You can specify the private IP address of the target ECS instance in the following ways: Aut o Fill: select an ECS instance from the ECS instance or Elastic Network Interface (ENI) list. Manually Input : enter the private IP address of the target ECS instance. Not e The private IP address that you enter must fall in the range of the CIDR block or belong to an in-use ECS instance. |

| Parameter | Description |
|---|---|
| Port Set t ings | Select a DNAT mapping method: All: This method uses IP mapping. All requests destined for the public IP address are forwarded to the target ECS instance. Specif ic Port : This method uses port mapping. The NAT gateway forwards requests from the specified protocol and port to the specified port of the target ECS instance. After you select a specific port, specify Public Port (the external port for port mapping), Privat e Port (the internal port for port mapping), and IP Prot ocol (the protocol of the ports). |
| Ent ry Name | Enter a name for the DNAT entry. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). It must start with a letter or Chinese _ character. |

### 3.5 Create an SNAT entry

This topic describes how to create a Source Network Address Translation (SNAT) entry. You can create SNAT entries on the NAT gateway of a Virtual Private Cloud (VPC) network. Then, the Elastic Compute Service (ECS) instances without public IP addresses assigned in the VPC network can use the SNAT entries to access the Internet.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eways page, find the target NAT gateway and click Conf igure SNAT in the
Act ions column.
4. On the SNAT T able page, click Creat e SNAT Ent ry.
5. In the Creat e SNAT Ent ry dialog box, set the following parameters, and then click OK.

| Parameter | Description |
|---|---|
| VSwit ch Granularit y |   |
| VSwit ch | Select the VSwitch for which you want to create the SNAT entry in the associated VPC network. All ECS instances attached to the specified VSwitch can access the Internet by using the SNAT entry. Not e SNAT entries do not take effect on ECS instances that are assigned public IP addresses. For example, an ECS instance may be assigned static public IP address, associated with an elastic IP address (EIP) or has a Destination Network Address Translation (DNAT) IP mapping configured. These ECS instances use the public IP addresses instead of the SNAT entries to access the Internet. |

| Parameter | Description |
|---|---|
| VSwit ch CIDR block | The CIDR block of the selected VSwitch. |
| Public IP address | Select the public IP address that is used to access the Internet. You can select multiple public IP addresses to create an SNAT IP address pool. If the maximum bandwidth of the EIP bandwidth plan is 1024 Mbit/s, add at least five public IP addresses to the SNAT entry. For each additional 200 Mbit/s of the peak bandwidth to the EIP bandwidth plan, at least one public IP address must be added to the SNAT entry. Not e A public IP address that is already used in a DNAT entry cannot be used to create an SNAT entry. |
| Ent ry name | Enter a name for the SNAT entry. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), and hyphens (-). It must start with a letter or a Chinese _ character. |
| ECS Granularit y |   |
| Available ECS Inst ances | Select the ECS instance for which you want to create the SNAT entry in the associated VPC network. The selected ECS instance can access the Internet by using the specified public IP address. Make sure that the following conditions are met: The ECS instance is in the running state. The ECS instance is not associated with an EIP or assigned a static public IP address. |
| ECS CIDR Block | Displays the CIDR block of the ECS instance. |
| Public IP address | Select the public IP address that is used to access the Internet. You can select multiple public IP addresses to create an SNAT IP address pool. Not e A public IP address that is used in a DNAT entry cannot be used to create an SNAT entry. |

| Parameter | Description |
|---|---|
| Ent ry Name | Enter a name for the SNAT entry. The name must be 2 to 128 characters in length and can contain numbers, underscores ( ), and hyphens (-). The name must start with a letter or _ Chinese character. |

## 4 Manage a NAT gateway

### 4.1 Sizes of NAT gateways

This topic describes the available sizes of Network Address Translation (NAT) gateways.The available sizes are Small, Middle, Large, and Super Large. The maximum number of SNAT connections and the number of SNAT connections per second (CPS) supported by a NAT gateway are determined by the size of NAT gateway. However, the size of a NAT gateway does not affect the performance of Destination Network Address Translation (DNAT). Compare NAT gateway sizes The following table lists different sizes of NAT gateways.

| Size | Maximum number of SNAT connections | Number of SNAT CPS |
|---|---|---|
| Small | 10,000 | 1,000 |
| Middle | 50,000 | 5,000 |
| Large | 200,000 | 10,000 |
| Super Large | 1,000,000 | 30,000 |

Limits When you select a size for a NAT gateway, note the following limits: Cloud Monitor monitors only the maximum number of SNAT connections for NAT gateways. It does not monitor the number of new SNAT connections per second. The timeout of SNAT connections in a NAT gateway is 900 seconds. To avoid the timeout of SNAT connections caused by network congestion and Internet instability, make sure that your applications support automatic reconnection. This ensures higher availability. NAT gateways do not support packet fragmentation. For the same destination public IP address and port, the number of EIPs associated with a NAT gateway determines the maximum number of connections. Each EIP associated with a NAT gateway supports up to 55,000 connections. If N EIPs are associated with the NAT gateway, the maximum number of connections that the NAT gateway supports is N × 55,000.

### 4.2 Create a NAT gateway

A NAT gateway is an enterprise-class gateway that provides NAT proxy services. Before you configure SNAT and DNAT entries, you must create a NAT gateway. A VPC network is created. For more information, see VPC User GuideCreat e a VPC net work in the Quick St art chapter in the VPC User Guide.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eway page, click Creat e NAT Gat eway.
3. If this is the first time you purchase a NAT gateway, you must create a service-linked role for NAT
Gateway.创建NAT 网关面板On the page, click Creat e in the Notes on Creating Service-linked Roles section. After a service-linked role is created, you can purchase NAT gateways.
4. On the 创建NAT 网关面板 page, set the following parameters and click Buy Now:
付费模式： 包年包月：包年包月是一种先付费后使用的付费模式。更多信息，请参见包年包月和Pay-byspecification (Discontinued)。 按量付费：按量付费是一种先使用后付费的付费模式。更多信息，请参见Pay-as-you-go。 Region and Zone: Select the region where you want to deploy the NAT gateway. Zone: Select the zone where you want to deploy the NAT gateway. VPC ID: Select the VPC where you want to deploy the NAT gateway. After the NAT gateway is created, you cannot change the VPC where the NAT gateway is deployed. If you cannot find the VPC that you want to manage in the list, troubleshoot the issue by using the following methods: Check whether a VPC is created in the region and zone that you selected. If your account is a Resource Access Management (RAM) user, check whether the RAM user has read permissions on the VPC. If not, contact the Alibaba Cloud account owner to acquire the permissions. VSwit ch ID: Select the vSwitch to which the NAT gateway is attached. Gat eway T ype: By default, Enhanced is selected. Enhanced NAT gateways are an upgrade from standard NAT gateways and use a more advanced architecture. Compared with standard NAT gateways, enhanced NAT gateways provide higher elasticity and stability. This helps you manage data transfer in a more efficient manner. 名称：设置NAT网关实例的名称。 名称长度为2~128个字符，以英文字母或中文开头，可包含数字、下划线（_）和短划线（-）。 规格：当选择包年包月付费模式时，需要选择NAT网关的规格。 小型中型大型不同规格的NAT网关会影响SNAT最大连接数和SNAT每秒新建连接数，但不会影响DNAT性能。请您根据业务需求灵活选择规格。 购买数量：当选择包年包月付费模式时，请设置要购买NAT网关实例的数量。 计费类型：当选择按量付费付费模式时，默认选择按使用量计费，即按NAT网关实际使用量收费。 更多信息，请参见Pay-by-CU。 Billing Cycle:选择 the billing cycle of the NAT gateway. 5.
6. Set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | The organization to which the NAT gateway belongs. |
| Resource Set | The resource group to which the NAT gateway belongs. |
| Region | Select the region where you want to deploy the NAT gateway. |
| VPC | Select the VPC where you want to deploy the NAT gateway. If you cannot find the VPC in the list, perform the following operations: Check whether the VPC is already associated with a NAT gateway. Each VPC can be associated with only one NAT gateway. Check whether the VPC has a custom route entry whose destination CIDR block is 0.0.0.0/0. If the custom route entry exists, delete the custom route entry. Check whether the Resource Access Management (RAM) user is authorized to access the VPC. If the RAM user is unauthorized, contact the owner of the Alibaba Cloud account that created the RAM user to grant permissions. |
| Specif icat ion | Select the size of the NAT gateway. Valid values: Small: supports up to 10,000 SNAT connections. Medium: supports up to 50,000 SNAT connections. Large: supports up to 200,000 SNAT connections. Not e The maximum number of SNAT connections is limited by the size of a NAT gateway. However, the gateway size does not affect the maximum number of DNAT connections. |
| Name | Enter a name for the NAT gateway. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It must _ start with a letter and cannot start with http:// or https:// . |

### 4.3 Modify a NAT gateway

This topic describes how to modify the name and description of a NAT gateway.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway that you want to manage, and then click
Manage in the Act ions column.
4. On the NAT Gat eway Det ails tab, click Edit next to the name. In the dialog box that appears,
enter a new name for the NAT gateway, and then click OK. The name must be 2 to128 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter or Chinese character.
5. Click Edit next to the description. In the dialog box that appears, enter a new description, and then
click OK. The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://` .

### 4.4 Delete a NAT gateway

You can delete NAT gateways that are billed on a pay-as-you-go basis. You cannot delete subscription NAT gateways. Before you delete a NAT gateway, make sure that the following conditions are met: The NAT gateway is not associated with an EIP. If the NAT gateway is associated with an EIP, disassociate the EIP first. For more information, see Disassociate EIPs from a NAT gateway. The DNAT table is empty. If the DNAT table contains DNAT entries, delete these entries first. For more information, see Delete a DNAT entry. The SNAT table is empty. If the DNAT table contains SNAT entries, delete these entries first. For more information, see Delete a SNAT entry.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eways page, find the target NAT gateway, and click
> Delet e in the Act ions

column.
4. In the dialog box that appears, click OK.
If you select Delet e (Delet e NAT gat eway and resources), the DNAT and SNAT entries of the NAT gateway are deleted automatically. The EIP associated with the NAT gateway is also disassociated.

## 5 Manage EIPs

### 5.1 Associate an EIP with a NAT gateway

gateway This topic describes how to associate an EIP with a NAT gateway. NAT gateways must be associated with EIPs so that they can work as expected. After you create a NAT gateway, you can associate it with an EIP. Before you associate an EIP with a NAT gateway, make sure that the following conditions are met: A NAT gateway is created. For more information, see Create a NAT Gateway. An EIP is purchased. For more information, see the Creat e an Elast ic IP address topic of the Quick st art document in the EIP user guide.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway with which you want to associate an EIP, and
choose
> Bind Elast ic IP Address in the Act ions column.

4. In the Associat e EIP dialog box, set the following parameters, and click OK.

| Parameter | Description |
|---|---|
| Usable EIP List | Select the EIP that is used to communicate with the Internet. |
| vSwit ch | Select the vSwitch to which you want to add SNAT entries. After you select a vSwitch, the system automatically adds SNAT entries to the vSwitch. Then, cloud services in the vSwitch can access the Internet. You can skip this step and manually add SNAT entries after you associate an EIP with the NAT gateway. For more information, see Create a SNAT entry. |

### 5.2 Disassociate an EIP from a NAT gateway

gateway If your NAT gateway does not need to communicate with the Internet, you can disassociate the EIP from the NAT gateway. The EIP that you want to disassociate is not used in any SNAT or DNAT entries.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eways page, find the NAT gateway, and choose
> Unbind Elast ic IP Address

in the Act ions column.
4. In the Unbind Elast ic IP Address dialog box, select the EIP that you want to disassociate, and
click OK.

## 6 Manage a DNAT table

### 6.1 DNAT table overview

NAT Gateway supports the Destination Network Address Translation (DNAT) feature. You can create DNAT entries to map public IP addresses to ECS instances in a Virtual Private Cloud (VPC) network. This way, the ECS instances can receive requests from the Internet. DNAT entries You can configure port mapping when you create a DNAT entry. After the DNAT entry is created, requests destined for the specified public IP address are forwarded to the ECS instances within a VPC network based on the port mapping rule. Each DNAT entry consists of the following elements: Public IP address: the EIP associated with the NAT gateway. Privat e IP address: the private IP address assigned to the ECS instance in the VPC network. Public Port : the external port where requests from the Internet are received. Privat e Port : the internal port to which the requests received on the external port are forwarded. Prot ocol T ype: the protocol used by the ports. Port mapping and IP mapping The DNAT feature supports port mapping and IP mapping: Port mapping After port mapping is configured, a NAT gateway forwards requests destined for a public IP address to the specified ECS instance based on the specified protocol and ports.

| DNAT entry | Public IP address | Public port | Private IP address | Private port | Protocol type |
|---|---|---|---|---|---|
| Entry 1 | 139.224.xx.xx | 80 | 192.168.x.x | 80 | TCP |
| Entry 2 | 139.224.xx.xx | 8080 | 192.168.x.x | 8000 | UDP |

Entry 1: The NAT gateway forwards requests destined for TCP port 80 of ECS instance 139.244.xx.xx to TCP port 80 of ECS instance 192.168.x.x. Entry 2: The NAT gateway forwards requests destined for UDP port 8080 of ECS instance 139.224.xx.xx to UDP port 8000 of ECS instance 192.168.x.x. IP mapping After IP mapping is configured, a NAT gateway forwards all requests destined for a public IP address to the specified ECS instance.

| DNAT entry | Public IP address | Public port | Private IP address | Private port | Protocol type |
|---|---|---|---|---|---|
| Entry 3 | 139.224.xx.xx | Any | 192.168.x.x | Any | Any |

Entry 3: The NAT gateway forwards requests destined for ECS instance 139.224.xx.xx to ECS instance 192.168.x.x.

### 6.2 Create a DNAT entry

This topic describes how to create a Destination Network Address Translation (DNAT) entry. DNAT maps a public IP address to an Elastic Compute Service (ECS) instance in a Virtual Private Cloud (VPC) network. This allows the ECS instance to receive requests sent over the Internet. DNAT supports port mapping and IP mapping. A NAT gateway is created and associated with an elastic IP address (EIP). For more information, see Create a NAT gateway and Associate an EIP with a NAT Gateway.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway that you want to manage, and click Conf igure
DNAT in the Act ions column.
4. On the DNAT T able page, click Creat e DNAT Ent ry.
5. In the Creat e DNAT Ent ry panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Public IP Address | Select an available public IP address. Not e If a public IP address is already used to create an SNAT entry, the public IP address cannot be used to create a DNAT entry. |
| Privat e IP Address | Specify the ECS instance that uses the DNAT entry to communicate with the Internet. You can specify the private IP address of the ECS instance in the following ways: Aut o Fill: Select the ECS instance from the drop-down list. Manually Input : Enter the private IP address of the ECS instance. Not e This private IP address must fall within the CIDR block of the virtual private cloud (VPC). You can also enter the private IP address of an existing ECS instance. |

| Parameter | Description |
|---|---|
| Port Set t ings | Select a DNAT mapping method: All: This method uses IP mapping. All requests destined for the elastic IP address (EIP) are forwarded to the ECS instance. Specif ic Port : This method uses port mapping. The NAT gateway forwards requests that use the specified protocol and port to the specified port of the ECS instance. After you select Specific Port, specify the Public Port (the external port), Privat e Port (the internal port), and IP Prot ocol (the protocol over which data is transferred). |
| Ent ry Name | Enter a name for the DNAT entry. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), and hyphens (-). It must start with a letter. _ |

### 6.3 Modify a DNAT entry

This topic describes how to modify a Destination Network Address Translation (DNAT) entry. After you create a DNAT entry, you can modify the public IP address, private IP address, ports, and name of the DNAT entry.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway that you want to manage, and click Conf igure
DNAT in the Act ions column.
4. On the DNAT t able page, find the target DNAT entry, and click Edit in the Act ions column.
5. In the Edit DNAT Ent ry dialog box, change the public IP address, private IP address, ports, and
name of the DNAT entry, and then click OK.

### 6.4 Delete a DNAT entry

This topic describes how to delete a Destination Network Address Translation (DNAT) entry. If you no longer need an Elastic Compute Service (ECS) instance to receive requests sent over the Internet, you can delete the DNAT entry of the ECS instance.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway that you want to manage, and click Conf igure
DNAT in the Act ions column.
4. On the DNAT t able page, find the target DNAT entry, and click Remove in the Act ions column.
5. In the dialog box that appears, click OK.

## 7 Manage an SNAT table

### 7.1 SNAT table overview

NAT Gateway supports Source Network Address Translation (SNAT). SNAT allows Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network to access the Internet without using public IP addresses. SNAT entries You can create SNAT entries in an SNAT table to allow ECS instances to access the Internet. An SNAT entry consists of the following elements: VSwit ch or ECS inst ance: the VSwitch or ECS instance that requires the SNAT proxy service. Public IP address: the public IP address used to access the Internet. VSwitch granularity and ECS granularity SNAT entries can be created based on the following granularity to enable ECS instances in a VPC network to access the Internet. VSwitch granularity You can select the VSwitch granularity to create an SNAT entry. The NAT gateway provides proxy service for an ECS instance attached to the specified VSwitch by using a specified public IP address when the instance sends requests to the Internet. By default, all ECS instances attached to the VSwitch can use the specified public IP address to access the Internet. SNAT entries do not take effect on ECS instances that are assigned public IP addresses. For example, an ECS instance may be assigned static public IP address, associated with an elastic IP address (EIP) or has a Destination Network Address Translation (DNAT) IP mapping configured. These ECS instances use the public IP addresses instead of the SNAT entries to access the Internet. ECS granularity If you select the ECS granularity to create an SNAT entry, the specified ECS instance uses the specified public IP address to access the Internet. The NAT gateway provides proxy service (SNAT) for a specified ECS instance by using a specified public IP address when the instance sends requests to the Internet.

### 7.2 Create an SNAT entry

This topic describes how to create a Source Network Address Translation (SNAT) entry. SNAT allows Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network to access the Internet without using public IP addresses. Before you create an SNAT entry, make sure that the following requirements are met: A NAT gateway is created and associated with an elastic IP address (EIP). For more information, see Create a NAT gateway and Associate an EIP with a NAT Gateway. To create an SNAT entry with VSwitch granularity, make sure that the VSwitch is created and associated with the NAT gateway in a VPC network. To create an SNAT entry with ECS granularity, make sure that the ECS instance is created and associated with the NAT gateway in a VPC network.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway and click Conf igure SNAT in the Act ions
column.
4. On the SNAT T able page, click Creat e SNAT Ent ry.
5. In the Creat e SNAT Ent ry panel, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| VSwit ch Granularit y |   |
| VSwit ch | Select a vSwitch in the VPC. All ECS instances in the vSwitch can access the Internet by using SNAT. Not e SNAT entries do not take effect on ECS instances that are assigned public IP addresses. For example, an ECS instance may be assigned a static public IP address, associated with an elastic IP address (EIP), or configured with DNAT IP mapping. Such an ECS instance uses the public IP address instead of the SNAT entry to access the Internet. |
| VSwit ch CIDR Block | The CIDR block of the selected vSwitch. |
| Public IP Address | Select the EIP that is used to access the Internet. You can select one or more EIPs. You can use multiple EIPs to create an SNAT IP address pool. If the maximum bandwidth value of the EIP bandwidth plan is 1,024 Mbit/s, specify at least five EIPs in each SNAT entry. If the maximum bandwidth value of the EIP bandwidth plan exceeds 1,024 Mbit/s, specify at least one additional EIP in each SNAT entry for every incremental 200 Mbit/s. Not e An EIP that is already used in a DNAT entry cannot be used in an SNAT entry. |
| ECS Granularit y |   |

| Parameter | Description |
|---|---|
| Available ECS Inst ances | Select an ECS instance in the VPC. The ECS instance can access the Internet by using the specified EIP. Make sure that the following requirements are met: The ECS instance is in the Running state. The ECS instance is not assigned an EIP or a static public IP address. |
| ECS CIDR Block | The CIDR block of the ECS instance. |
| Public IP Address | Select the EIP that is used to access the Internet. You can select one or more EIPs. You can use multiple EIPs to create an SNAT IP address pool. Not e An EIP that is already used in a DNAT entry cannot be used in an SNAT entry. |

### 7.3 Modify an SNAT entry

This topic describes how to modify a Source Network Address Translation (SNAT) entry. After you create an SNAT entry, you can modify the public IP address and name of the SNAT entry.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway and click Conf igure SNAT in the Act ions
column.
4. On the SNAT t able page, find the target SNAT entry, and click Edit in the Act ions column.
5. In the Edit SNAT Ent ry dialog box, change the public IP address and name of the SNAT entry, and
then click OK.

### 7.4 Delete a SNAT entry

This topic describes how to delete a Source Network Address Translation (SNAT) entry. You can delete the SNAT entry if the Elastic Compute Service (ECS) instances without public IP addresses in a Virtual Private Cloud (VPC) network no longer need the SNAT service to access the Internet.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway and click Conf igure SNAT in the Act ions
column.
4. On the SNAT t able page, find the target SNAT entry, and click Remove in the Act ions column.
5. In the dialog box that appears, click OK.

## 8 NAT service plan

### 8.1 Create a NAT service plan

You can associate an elastic IP address (EIP) or a NAT service plan to a NAT gateway. However, you can choose only one of them for the NAT gateway. If you want to associate a NAT service plan with the NAT gateway, you must create a NAT service plan first. Then, you can configure SNAT or DNAT for the NAT gateway. A NAT service plan consists of public IP addresses and Internet bandwidth.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and choose Purchase NAT
Bandwidt h Package in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, click Purchase.
4. On the NAT Bandwidt h Package page, set the following parameters, and click Submit .

| Parameter | Description |   |   |
|---|---|---|---|
| Region | Indicates the region for which the NAT service plan is purchased. |   |   |
| Billing met hods | Select the billing method of the NAT service plan. Only By Bandwidt h is supported. |   |   |
| Bandwidt h (Mbit /s) | Enter a bandwidth value for the NAT service plan that you want to purchase. The maximum value is 5000 Mbit/s. |   |   |
| Name | Enter a name for the NAT service plan. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter or Chinese character. _ |   |   |
| Descript ion | Enter a description for the NAT service plan. The description must be 2 to 256 characters in length and cannot start with htt p:// or https:// . |   |   |
|   |   | htt |   |
| Quant it y | Enter the number of NAT bandwidth plans that you want to purchase. |   |   |

|   | p:// |
|---|---|

### 8.2 Modify the bandwidth of a NAT service plan

service plan This topic describes how to modify the bandwidth of a NAT bandwidth plan. The modification takes effect immediately.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, click the target NAT service plan, and then choose
Modif y Bandwidt h.
4. On the Modif y Bandwidt h page, modify the bandwidth, and then click Submit .
Each NAT bandwidth plan supports a maximum of 5,000 Mbit/s in bandwidth.

### 8.3 Add an IP address

This topic describes how to add IP addresses to a NAT service plan. The added IP addresses can be used to create Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT) rules.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, click the target NAT service plan, and then choose
Add IP Address.
4. On the Modif y IP Addresses page, enter the number of IP addresses to be added, and then click
Submit .

### 8.4 Release an IP address

This topic describes how to release IP addresses in a NAT service plan. The NAT service plan must contain at least one IP address. Before you release an IP address in the NAT service plan, make sure that the IP address is not used in Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT) entries. If the IP address is used in an SNAT or DNAT entry, delete the SNAT or DNAT entry first. For more information, see Delete a DNAT entry and Delete a SNAT entry.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, click the target NAT service plan.
4. In the Public IP List section, find the target IP address, and click Release in the Act ions column.
5. In the Release IP dialog box, click OK.

### 8.5 Delete a NAT service plan

This topic describes how to delete a service plan. Before you start, make sure that the following requirements are met: Delete the IP addresses that are used in Destination Network Address Translation (DNAT) entries. For more information, see Delete a DNAT entry. Delete the IP addresses that are used for Source Network Address Translation (SNAT) entries. For more information, see Delete a SNAT entry.
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, find the target NAT service plan and click Delet e.
4. In the Delet e Shared Int ernet Shared Bandwidt h dialog box, click OK.

## 9 Anti-DDoS Basic

Distributed Denial of Service (DDoS) attack is a malicious network attack against the target system, which can make the attacked network inaccessible. Alibaba Cloud provides up to 5 Gbit/s of basic anti- DDoS protection for NAT Gateway, which can efficiently prevent DDoS attack. How Anti-DDoS Basic works After you enable Anti-DDos Basic, all traffic from the Internet must first pass through Alibaba Cloud Security before arriving at NAT Gateway. Anti-DDoS Basic scrubs and filters common DDoS attacks at Alibaba Cloud Security. Anti-DDos Basic protects your services against attacks such as SYN flood, UDP flood, ACK flood, ICMP flood, and DNS Query flood. Anti-DDoS Basic sets the scrubbing threshold and black hole triggering threshold based on the EIP bandwidth of NAT Gateway. When the inbound traffic reaches the threshold, scrubbing or blackholing is triggered: Scrubbing: When the attack traffic from the Internet exceeds the scrubbing threshold or matches certain attack traffic pattern, Alibaba Cloud Security starts scrubbing the attack traffic. The scrubbing includes packet filtering, bandwidth capping, and traffic throttling. Blackholing: When the attack traffic from the Internet exceeds the black hole triggering threshold, blackholing is triggered and all inbound traffic is dropped. Scrubbing threshold The thresholds for triggering traffic scrubbing and blackholing on NAT Gateway are calculated as described in the following table:

| EIP bandwidth | Traffic scrubbing threshold (bits/s) | Traffic scrubbing threshold (packets/s) | Default black hole triggering threshold |
|---|---|---|---|
| Lower than or equal to 800 Mbit/s | 800Mbps | 120,000 | 1.5 Gbps |
| Higher than 800 Mbit/s | Predefined bandwidth | Predefined bandwidth × 150 | Predefined bandwidth × 2 |

If the EIP bandwidth is 1,000 Mbit/s, the traffic scrubbing threshold (bits/s) is 1,000 Mbit/s, the traffic scrubbing threshold (packets/s) is 150,000 and the default blackholing threshold is 2 Gbit/s.
