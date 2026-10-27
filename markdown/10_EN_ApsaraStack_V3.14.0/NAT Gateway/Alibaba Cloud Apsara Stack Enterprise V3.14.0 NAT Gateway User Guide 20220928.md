---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 NAT Gateway User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 28
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 NAT Gateway User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20NAT%20Gateway%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 NAT Gateway User Guide 20220928

## Table of Contents

- 1 What is NAT Gateway?
- 2 Log on to the NAT Gateway console
- 3 Quick Start
  - 3.1 Overview
  - 3.2 Create a NAT gateway
  - 3.3 Associate an EIP with a NAT gateway
  - 3.4 Create a DNAT entry
  - 3.5 Create an SNAT entry
- 4 Manage a NAT gateway
  - 4.1 Overview
  - 4.2 Create a NAT gateway
  - 4.3 Modify a NAT gateway
  - 4.4 Delete a NAT gateway
- 5 Manage EIPs
  - 5.1 Associate an EIP with a NAT gateway
  - 5.2 Disassociate an EIP from a NAT gateway
- 6 Manage a DNAT table
  - 6.1 DNAT overview
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
- 9 Anti-DDoS Origin Basic

## 1 What is NAT Gateway?

NAT gateways are enterprise-class gateways that provide the Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT) features. Each NAT gateway provides a throughput capacity of up to 100 Gbit/s. NAT gateways also support cross-zone disaster recovery. Features You must associate public IP addresses with NAT gateways so that the NAT gateways can function as expected. After you create a NAT gateway, you can associate elastic IP addresses (EIPs) with the NAT gateway. NAT gateways provide the SNAT and DNAT features.

| Feature | Description |
|---|---|
| SNAT | SNAT allows ECS instances that are deployed in a VPC to access the Internet when no public IP address is associated with these ECS instances. |
| DNAT | DNAT maps the EIPs of a NAT gateway to ECS instances. This way, the ECS instances can receive requests from the Internet. |

way console

## 2 Log on to the NAT Gateway console

console This topic describes how to log on to the Apsara Uni-manager Management Console to manage your NAT gateways. The Google Chrome browser is used as an example. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top menu bar, choose Product s > Net working > Virt ual Privat e Cloud.
5. In the left-side navigation pane, choose Int ernet Access > NAT Gat eway.

## 3 Quick Start

### 3.1 Overview

This topic describes how to configure Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT). You can configure SNAT and DNAT to enable ECS instances in a Virtual Private Cloud (VPC) network to communicate with the Internet through a NAT gateway. Prerequisites Before you start, make sure that the following conditions are met: A VPC network is created. For more information, see VPC User Guide Creat e a VPC net work in the Quick St art chapter in the VPC User Guide. An ECS instance is created in the VPC network. For more information, see ECS User Guide Creat e an inst ance in the Quick St art chapter in the ECS User Guide. An elastic IP address (EIP) is created. For more information, see EIP User Guide Creat e an EIP in the Quick St art chapter in the EIP User Guide. Procedure In this topic, an ECS instance that is not associated with any public IP addresses in a VPC network is used as an example. The following flowchart shows how to associate an EIP with a NAT gateway: A NAT gateway is an enterprise-class gateway that provides NAT proxy services. Before you configure SNAT and DNAT entries, you must create a NAT gateway. For more information, see Create a NAT gateway.
2. Associate an EIP to a NAT gateway
A NAT gateway functions as expected only after it is associated with a public IP address. After you create a NAT gateway, you can associate it with an EIP. For more information, see Associate an EIP with a NAT Gateway. This topic describes how to create a Destination Network Address Translation (DNAT) entry. DNAT maps public IP addresses to Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network. This way, the ECS instances can receive requests sent over the Internet. DNAT supports port mapping and IP mapping. For more information, see Create a DNAT entry. This topic describes how to create a Source Network Address Translation (SNAT) entry. SNAT allows Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network to access the Internet without using public IP addresses. For more information, see Create a SNAT entry.

### 3.2 Create a NAT gateway

A NAT gateway is an enterprise-class gateway that provides NAT proxy services. Before you configure SNAT and DNAT entries, you must create a NAT gateway. Prerequisites A VPC network is created. For more information, see VPC User GuideCreat e a VPC net work in the Quick St art chapter in the VPC User Guide. Procedure
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

### 3.3 Associate an EIP with a NAT gateway

gateway A NAT gateway works as expected only after you associate an elastic IP address (EIP) with it. This topic describes how to associate an EIP with a NAT gateway. Procedure
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

### 3.4 Create a DNAT entry

This topic describes how to create a DNAT entry. DNAT can map public IP addresses of NAT gateways to Elastic Compute Service (ECS) instances. This way, ECS instances can provide services over the Internet. DNAT supports port mapping and IP mapping. Procedure
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
| Port Set t ings | Select a DNAT mapping method: All: This method uses IP mapping. All requests destined for the elastic IP address (EIP) are forwarded to the ECS instance. Specif ic Port : This method uses port mapping. The NAT gateway forwards requests that use the specified protocol and port to the specified port of the ECS instance. After you select Specific Port, specify the Public Port (the external port), Privat e Port (the internal port), and IP Prot ocol (the protocol over which data is transferred). |
| Ent ry Name | Enter a name for the DNAT entry. The name must be 2 to 128 characters in length, and can contain digits, underscores ( ), and hyphens (-). It must start with a letter. _ |

### 3.5 Create an SNAT entry

This topic describes how to create an SNAT entry. SNAT can provide the proxy service for Elastic Compute Service (ECS) instances. ECS instances that have no IP address assigned in virtual private clouds (VPCs) can access the Internet by using SNAT. Procedure
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
| Available ECS Inst ances | Select an ECS instance in the VPC. The ECS instance can access the Internet by using the specified EIP. Make sure that the following requirements are met: The ECS instance is in the Running state. The ECS instance is not assigned an EIP or a static public IP address. |

| Parameter | Description |
|---|---|
| ECS CIDR Block | The CIDR block of the ECS instance. |
| Public IP Address | Select the EIP that is used to access the Internet. You can select one or more EIPs. You can use multiple EIPs to create an SNAT IP address pool. Not e An EIP that is already used in a DNAT entry cannot be used in an SNAT entry. |

## 4 Manage a NAT gateway

### 4.1 Overview

NAT gateways are enterprise-class gateways that support SNAT and DNAT features. Each NAT gateway provides a forwarding capacity of 10 Gbit/s. NAT gateways support cross-zone disaster recovery. Sizes of NAT gateways NAT gateways are available in multiple sizes, including small, middle, large, and super large-1. The size of a NAT gateway determines the SNAT performance, which includes the maximum number of connections and the number of new connections per second. However, the size of a NAT gateway does not affect the DNAT performance. The following table describes available sizes of NAT gateways.

| Size | Maximum number of SNAT connections | Number of new SNAT connections per second |
|---|---|---|
| Small | 10,000 | 1,000 |
| Medium | 50,000 | 5,000 |
| Large | 200,000 | 10,000 |
| Super Large-1 | 1,000,000 | 50,000 |

When you specify the size of a NAT gateway, take note of the following limits: CloudMonitor monitors only the maximum number of SNAT connections for NAT gateways. CloudMonitor does not monitor the number of new SNAT connections per second. The timeout period of SNAT connections on NAT gateways is 900 seconds. To avoid timeouts of SNAT connections caused by network congestion or Internet jitter, make sure that your applications support automatic reconnection. NAT gateways do not support packet fragmentation. If you use the same destination public IP address and port, the maximum number of concurrent connections is based on the number of elastic IP addresses (EIPs) that are associated with the NAT gateway. Each EIP that is associated with the NAT gateway supports up to 55,000 concurrent connections. If N EIPs are associated with the NAT gateway, the maximum number of concurrent connections that the NAT gateway supports is N × 55,000.

### 4.2 Create a NAT gateway

A NAT gateway is an enterprise-class gateway that provides NAT proxy services. Before you configure SNAT and DNAT entries, you must create a NAT gateway. Prerequisites A VPC network is created. For more information, see VPC User GuideCreat e a VPC net work in the Quick St art chapter in the VPC User Guide.
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
| Specif icat ion | Select the size of the NAT gateway. Valid values: Small: supports up to 10,000 SNAT connections. Medium: supports up to 50,000 SNAT connections. Large: supports up to 200,000 SNAT connections. Super Large: supports up to 1,000,000 SNAT connections. Not e The size of a NAT gateway determines the maximum number of SNAT connections, but it does not affect the maximum number of DNAT connections. |
| Paramet er | Enter a name for the NAT gateway. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), periods (.), colons (:), and commas (,). It _ must start with a letter or Chinese character but cannot start with http:// or https:// . |

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

You can delete NAT gateways that are billed on a pay-as-you-go basis. You cannot delete subscription NAT gateways. Prerequisites Before you delete a NAT gateway, make sure that the following conditions are met: The NAT gateway is not associated with an EIP. If the NAT gateway is associated with an EIP, disassociate the EIP first. For more information, see Disassociate EIPs from a NAT gateway. The DNAT table is empty. If the DNAT table contains DNAT entries, delete these entries first. For more information, see Delete a DNAT entry. The SNAT table is empty. If the DNAT table contains SNAT entries, delete these entries first. For more information, see Delete a SNAT entry. Procedure
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eways page, find the target NAT gateway, and click
> Delet e in the Act ions

column.
4. In the dialog box that appears, click OK.
Not e If you select Delet e (Delet e NAT gat eway and resources), the DNAT and SNAT entries of the NAT gateway are deleted automatically. The EIP associated with the NAT gateway is also disassociated.

## 5 Manage EIPs

### 5.1 Associate an EIP with a NAT gateway

gateway A NAT gateway works as expected only after it is associated with an elastic IP address (EIP). This topic describes how to associate an EIP with a NAT gateway. Prerequisites Before you associate an EIP with a NAT gateway, make sure that the following requirements are met: A NAT gateway is created. For more information, see Create a NAT gateway. An EIP is purchased. For more information, see the Create an EIP topic in Quick St art of Elast ic IP Address User Guide. Procedure
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway with which you want to associate an EIP, and
choose
> Bind Elast ic IP Address in the Act ions column.

4. In the Associat e EIP dialog box, set the following parameters, and click OK.

| Parameter | Description |
|---|---|
| Usable EIP list | Select the EIP that is used to communicate with the Internet. |
| vSwit ch | Select the vSwitch to which you want to add SNAT entries. After you select a vSwitch, the system automatically adds SNAT entries to the vSwitch. Then, cloud services in the vSwitch can access the Internet. You can skip this step and manually add SNAT entries after you associate an EIP with the NAT gateway. |

### 5.2 Disassociate an EIP from a NAT gateway

gateway This topic describes how to disassociate an elastic IP address (EIP) from a NAT gateway. After an EIP is disassociated from a NAT gateway, the NAT gateway can no longer communicate with the Internet by using the EIP. Prerequisites Make sure that the EIP to be disassociated is not used in an SNAT entry or a DNAT entry. If the EIP is used in an SNAT or a DNAT entry, delete the SNAT or DNAT entry first. For more information, see Delete a SNAT entry and Delete a DNAT entry.
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway, and choose
> Unbind Elast ic IP Address

in the Act ions column.
4. In the Unbind Elast ic IP Address panel, select the EIP that you want to disassociate, and click OK.

## 6 Manage a DNAT table

### 6.1 DNAT overview

NAT Gateway supports the Destination Network Address Translation (DNAT) feature. You can create DNAT entries to map public IP addresses to ECS instances in a Virtual Private Cloud (VPC) network. This way, the ECS instances can receive requests from the Internet. DNAT entries You can configure port mapping when you create a DNAT entry. After the DNAT entry is created, requests destined for the specified public IP address are forwarded to the ECS instances within a VPC network based on the port mapping rule. Each DNAT entry consists of the following elements: Public IP : the Elastic IP Address (EIP) bound to the NAT gateway. Privat e IP : the private IP address of the ECS instance in the Virtual Private Cloud. Public port : the external port for port forwarding. Privat e Net work Port : the internal port for port forwarding. Prot ocol t ype : the protocol type of the forwarding port. Port mapping and IP mapping The DNAT feature supports port mapping and IP mapping: Port Mapping After port mapping is configured, a NAT gateway forwards requests destined for a public IP address to the specified ECS instance based on the specified protocol and ports. The following DNAT entries are used as examples: Entry 1: The NAT gateway forwards requests destined for TCP port 80 of ECS instance 1.1.XX.XX to TCP port 80 of ECS instance 192.168.1.1. Entry 2: The NAT gateway forwards requests destined for UDP port 8080 of ECS instance 2.2.XX.XX to UDP port 8000 of ECS instance 192.168.1.2.

| DNAT entry | Public IP address | External port | Private IP address | Internal port | TLS version |
|---|---|---|---|---|---|
| Entry 1 | 1.1.XX.XX | 80 | 192.168.1.1 | 80 | TCP |
| Entry 2 | 2.2.XX.XX | 8080 | 192.168.1.2 | 8000 | UDP |

IP mapping After IP mapping is configured, a NAT gateway forwards all requests destined for a public IP address to the specified ECS instance. The following entry is used as an example: Entry 3: The NAT gateway forwards requests destined for ECS instance 3.3.XX.XX to ECS instance 192.168.1.3.

| DNAT entry | Public IP address | External port | Private IP address | Internal port | TLS version |
|---|---|---|---|---|---|
| Entry 3 | 3.3.XX.XX | Any | 192.168.1.3 | Any | Any |

### 6.2 Create a DNAT entry

This topic describes how to create a Destination Network Address Translation (DNAT) entry. DNAT maps a public IP address to an Elastic Compute Service (ECS) instance in a Virtual Private Cloud (VPC) network. This allows the ECS instance to receive requests sent over the Internet. DNAT supports port mapping and IP mapping. Prerequisites A NAT gateway is created and associated with an elastic IP address (EIP). For more information, see Create a NAT gateway and Associate an EIP with a NAT Gateway. Procedure
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

This topic describes how to modify the public IP address, private IP address, or port of a DNAT entry. Procedure
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway that you want to manage, and click Conf igure
DNAT in the Act ions column.
4. On the DNAT T able page, find the DNAT entry, and click Edit in the Act ions column.
5. In the Edit DNAT Ent ry panel, modify the public IP address, private IP address, or port, and then
click OK.

### 6.4 Delete a DNAT entry

This topic describes how to delete a Destination Network Address Translation (DNAT) entry. If you no longer need an Elastic Compute Service (ECS) instance to receive requests sent over the Internet, you can delete the DNAT entry of the ECS instance. Procedure
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway that you want to manage, and click Conf igure
DNAT in the Act ions column.
4. On the DNAT t able page, find the target DNAT entry, and click Remove in the Act ions column.
5. In the dialog box that appears, click OK.

## 7 Manage an SNAT table

### 7.1 SNAT table overview

NAT Gateway supports Source Network Address Translation (SNAT). SNAT allows Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network to access the Internet without using public IP addresses. SNAT entries You can create SNAT entries in an SNAT table to allow ECS instances to access the Internet. An SNAT entry consists of the following elements: VSwit ch or ECS inst ance: the VSwitch or ECS instance that requires the SNAT proxy service. Public IP address: the public IP address used to access the Internet. VSwitch granularity and ECS granularity SNAT entries can be created based on the following granularity to enable ECS instances in a VPC network to access the Internet. VSwitch granularity You can select the VSwitch granularity to create an SNAT entry. The NAT gateway provides proxy service for an ECS instance attached to the specified VSwitch by using a specified public IP address when the instance sends requests to the Internet. By default, all ECS instances attached to the VSwitch can use the specified public IP address to access the Internet. Not e SNAT entries do not take effect on ECS instances that are assigned public IP addresses. For example, an ECS instance may be assigned static public IP address, associated with an elastic IP address (EIP) or has a Destination Network Address Translation (DNAT) IP mapping configured. These ECS instances use the public IP addresses instead of the SNAT entries to access the Internet. ECS granularity If you select the ECS granularity to create an SNAT entry, the specified ECS instance uses the specified public IP address to access the Internet. The NAT gateway provides proxy service (SNAT) for a specified ECS instance by using a specified public IP address when the instance sends requests to the Internet.

### 7.2 Create an SNAT entry

This topic describes how to create a Source Network Address Translation (SNAT) entry. SNAT allows Elastic Compute Service (ECS) instances in a Virtual Private Cloud (VPC) network to access the Internet without using public IP addresses. Prerequisites Before you create an SNAT entry, make sure that the following requirements are met: A NAT gateway is created and associated with an elastic IP address (EIP). For more information, see Create a NAT gateway and Associate an EIP with a NAT Gateway. To create an SNAT entry with VSwitch granularity, make sure that the VSwitch is created and associated with the NAT gateway in a VPC network. To create an SNAT entry with ECS granularity, make sure that the ECS instance is created and associated with the NAT gateway in a VPC network. Procedure
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

This topic describes how to modify the public IP address in an SNAT entry. Procedure
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway and click Conf igure SNAT in the Act ions
column.
4. On the SNAT T able page, find the SNAT entry, and click Edit in the Act ions column.
5. In the Edit SNAT Ent ry panel, change the public IP address and click OK.

### 7.4 Delete a SNAT entry

This topic describes how to delete a Source Network Address Translation (SNAT) entry. You can delete the SNAT entry if the Elastic Compute Service (ECS) instances without public IP addresses in a Virtual Private Cloud (VPC) network no longer need the SNAT service to access the Internet. Procedure
1. Log on to the NAT Gateway console.
2. In the top navigation bar, select the region where the NAT gateway is deployed.
3. On the NAT Gat eway page, find the NAT gateway and click Conf igure SNAT in the Act ions
column.
4. On the SNAT t able page, find the target SNAT entry, and click Remove in the Act ions column.
5. In the dialog box that appears, click OK.

## 8 NAT service plan

### 8.1 Create a NAT service plan

You can associate an elastic IP address (EIP) or a NAT service plan to a NAT gateway. However, you can choose only one of them for the NAT gateway. If you want to associate a NAT service plan with the NAT gateway, you must create a NAT service plan first. Then, you can configure SNAT or DNAT for the NAT gateway. A NAT service plan consists of public IP addresses and Internet bandwidth. Procedure
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

This topic describes how to add IP addresses to a NAT service plan. The added IP addresses can be used to create Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT) rules. Procedure
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, click the target NAT service plan, and then choose
Add IP Address.
4. On the Modif y IP Addresses page, enter the number of IP addresses to be added, and then click
Submit .

### 8.4 Release an IP address

This topic describes how to release IP addresses in a NAT service plan. The NAT service plan must contain at least one IP address. Prerequisites Before you release an IP address in the NAT service plan, make sure that the IP address is not used in Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT) entries. If the IP address is used in an SNAT or DNAT entry, delete the SNAT or DNAT entry first. For more information, see Delete a DNAT entry and Delete a SNAT entry. Procedure
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, click the target NAT service plan.
4. In the Public IP List section, find the target IP address, and click Release in the Act ions column.
5. In the Release IP dialog box, click OK.

### 8.5 Delete a NAT service plan

This topic describes how to delete a service plan. Before you start, make sure that the following requirements are met: Delete the IP addresses that are used in Destination Network Address Translation (DNAT) entries. For more information, see Delete a DNAT entry. Delete the IP addresses that are used for Source Network Address Translation (SNAT) entries. For more information, see Delete a SNAT entry. Procedure
1. Log on to the NAT Gateway console.
2. On the NAT Gat eways page, find the target NAT gateway and click the ID of the NAT service plan
in the Int ernet Shared Bandwidt h column.
3. On the Bandwidt h Package Det ails page, find the target NAT service plan and click Delet e.
4. In the Delet e Shared Int ernet Shared Bandwidt h dialog box, click OK.

## 9 Anti-DDoS Origin Basic

A distributed denial-of-service (DDoS) attack is a malicious network attack against one or more systems, which can crash the targeted network. Alibaba Cloud provides up to 5 Gbit/s of basic anti-DDoS protection for a NAT gateway free of charge. Anti-DDoS Origin Basic can effectively prevent DDoS attacks. How Anti-DDoS Origin Basic works After you enable Anti-DDoS Origin Basic, traffic from the Internet must pass through Alibaba Cloud Security before the traffic arrives at the NAT gateway. Anti-DDoS Origin Basic scrubs and filters common DDoS attacks at Alibaba Cloud Security. Anti-DDoS Origin Basic protects your services against attacks such as SYN floods, UDP floods, ACK floods, ICMP floods, and DNS Query floods. Anti-DDoS Origin Basic specifies the traffic scrubbing and blackhole triggering thresholds based on the bandwidth limit of the elastic IP address (EIP) that is associated with the NAT gateway. When the inbound traffic reaches the threshold, traffic scrubbing or blackhole is triggered: Traffic scrubbing: When the attack traffic from the Internet exceeds the scrubbing threshold or matches the attack traffic pattern, Alibaba Cloud Security starts to scrub the attack traffic. Traffic scrubbing includes packet filtering, bandwidth capping, and traffic throttling. Blackhole: When the attack traffic from the Internet exceeds the blackhole triggering threshold, blackhole is triggered and all inbound traffic is dropped. Traffic scrubbing and blackhole triggering thresholds The following table describes the methods that are used to calculate the traffic scrubbing and blackhole triggering thresholds on NAT gateways.

| Bandwidth limit of the EIP | Traffic scrubbing threshold (bit/s) | Traffic scrubbing threshold (pps) | Default blackhole triggering threshold |
|---|---|---|---|
| Lower than or equal to 800 Mbit/s | 800 Mbit/s | 120,000 | 1.5 Gbit/s |
| Higher than 800 Mbit/s | Predefined bandwidth | Predefined bandwidth × 150 | Predefined bandwidth × 2 |

If the bandwidth limit of the EIP is 1,000 Mbit/s, the traffic scrubbing threshold (bit/s) is 1,000 Mbit/s, the traffic scrubbing threshold (pps) is 150,000, and the default blackhole triggering threshold is 2 Gbit/s.
