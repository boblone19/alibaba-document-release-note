---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic IP Address User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 22
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic IP Address User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Elastic%20IP%20Address%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic IP Address User Guide 20220928

## Table of Contents

- 1 What is an EIP?
- 2 Log on to the EIP console
- 3 Quick start
  - 3.1 Tutorial overview
  - 3.2 Create a EIP
  - 3.3 Associate an EIP with an ECS instance
  - 3.4 Disassociate an EIP from a cloud resource
  - 3.5 Release an EIP
- 4 Manage EIPs
  - 4.1 Create a EIP
  - 4.2 Bind an EIP to a cloud instance
    - 4.2.1 Associate an EIP with an ECS instance
    - 4.2.2 Associate an EIP with an SLB instance
    - 4.2.3 Associate an EIP with an HAVIP
    - 4.2.4 Associate an EIP with a NAT gateway
    - 4.2.5 Bind an EIP to a secondary ENI
      - 4.2.5.1 Overview
      - 4.2.5.2 Associate an EIP with an ENI in the NAT mode
      - 4.2.5.3 Associate an EIP with an ENI in the cut-through mode
  - 4.3 Upgrade a subscription EIP
  - 4.4 Disassociate an EIP from a cloud resource
  - 4.5 Release an EIP

## 1 What is an EIP?

This topic provides an overview of Elastic IP Address. An elastic IP address (EIP) is a public IP address that you can purchase and hold as an independent resource. You can associate an EIP with an Elastic Compute Service (ECS) instance deployed in a virtual private cloud (VPC), an internal Server Load Balancer (SLB) instance deployed in a VPC, or a secondary elastic network interface (ENI) attached to a VPC. You can also associate an EIP with a NAT gateway, or a High-Availability Virtual IP Address (HAVIP). An EIP is also a NAT IP address that is provisioned in a public-facing gateway of Alibaba Cloud and is mapped to the associated cloud resource with NAT. After an EIP is associated with a cloud resource, the cloud resource can connect to the Internet by using this EIP. Line types EIPs support BGP (Multi-ISP) lines and BGP (Multi-ISP) Pro lines. The following table describes the differences between BGP (Multi-ISP) and BGP (Multi-ISP) Pro.

| Item | BGP (Multi-ISP) | BGP (Multi-ISP) Pro |
|---|---|---|
| Advantages | BGP (Multi-ISP) provides high-quality and high-bandwidth BGP lines. Up to 89 high-quality BGP lines are available worldwide. Direct connections can be established in all regions of the Chinese mainland through lines of the following Internet Service Providers (ISPs): China Telecom, China Unicom, China Mobile, China Mobile Tietong, China Netcom, China Education and Research Network (CERNET), National Radio and Television Administration, Dr. Peng Telecom & Media Group, and Founder Broadband Network. You can use BGP (Multi-ISP) with EIP bandwidth plans to obtain bandwidth of 100 Gbit/s and higher. | BGP (Multi-ISP) Pro lines optimize data transmission to the Chinese mainland and improve connection quality for international services. Compared with BGP (Multi-ISP) lines, when BGP (Multi-ISP) Pro lines provide services to users in the Chinese mainland (excluding data centers), cross-border connections are established by using Chinese mainland ISP services. This reduces network latency. |
| Region | All regions | China (Hong Kong) and Singapore (Singapore) Not e BGP (Multi-ISP) Pro EIPs in the Singapore (Singapore) region support only the pay-as-you-go billing method. |

Benefits EIPs have the following benefits: Independent purchase and possession You can purchase and hold an EIP as an independent resource. EIPs are not bundled with other computing or storage resources. Flexible association You can dissociate an EIP from a cloud resource and then release the EIP if the EIP is no longer needed. Configurable network capabilities You can adjust the peak bandwidth of an EIP at any time. The bandwidth changes take effect immediately. e

## 2 Log on to the EIP console

This topic provides an example of how to log on to the EIP console by using Google Chrome. Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Net working > Elast ic IP Address.

## 3 Quick start

### 3.1 Tutorial overview

This topic provides an overview of the tutorial that guides you in creating an EIP and associating an EIP with an ECS instance to allow the ECS instance to access the Internet. This tutorial walks you through the following tasks:
1. Apply for new EIPs
An EIP is a public IP address that you can purchase and hold as an independent resource. To get started, you must create an EIP. You can associate an EIP with an ECS instance deployed in a VPC to enable the ECS instance to connect to the Internet. You can disassociate an ECS instance from an EIP when the ECS instance no longer requires access to the Internet. You can release an EIP if it is no longer needed.

### 3.2 Create a EIP

This topic describes how to create a EIP. An EIP is a public IP address that you can purchase and hold as an independent resource.
1. Log on to the EIP console.
2. On the Elast ic IP Addresses page, click Creat e EIP.
3. On the Creat e Elast ic IP Address page, set the parameters and click Submit . The following table
describes the configuration parameters.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the EIP belongs. |
| Resource Set | Select the resource set to which the EIP belongs. |
| Region | Select a region for the EIP. Make sure that the EIP and the cloud resource to be associated with the EIP are located in the same region. |
| Zone | Select the zone to which the EIP belongs. |
| Line T ype | Select the line type of the EIP. |

| c IP Address | User Guide·Quick star |
|---|---|

| Parameter | Description |
|---|---|
| Net work T ype | Select the network type of communication for which the EIP will be used. Public Net work: Use the EIP to enable communication with the Internet. Hybrid Cloud: Use the EIP to enable communication within a hybrid cloud. For example, if you need to establish network connections from an on-premises data center to the Internet by using source network address translation (SNAT) and destination network address translation (DNAT), you must select this type for your EIP. |
| Service IP | Specify a specific EIP. Make sure that the specified IP address is an IPv4 address and is not taken by another account. Otherwise, the EIP cannot be allocated. Not e If you do not specify a service IP, a random EIP will be assigned to you by the system. |
| Peak Bandwidt h | Specify the maximum bandwidth for the EIP. Unit: Mbit/s. |

### 3.3 Associate an EIP with an ECS instance

instance This topic describes how to associate an EIP with an ECS instance deployed in a VPC. ECS instances that are associated with EIPs can communicate with the Internet. You have created an ECS instance. For more information, see the Creat e an inst ance topic of Quick st art in the Apsara Stack Elastic Compute Service User Guide.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the target EIP, and then click Bind in the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select ECS Inst ance. |

| Parameter | Description |
|---|---|
| ECS Inst ance | Select the ECS instance to be associated with the EIP. When you select an ECS instance, note the following points: The ECS instance must be deployed in a VPC. The ECS instance must be running or stopped. An ECS instance can be associated with only one EIP. The ECS instance and the EIP must reside in the same region. The ECS instance is not associated with a public IP address or another EIP. |

### 3.4 Disassociate an EIP from a cloud resource

resource This topic describes how to dissociate an EIP from a cloud resource when this cloud resource no longer needs to communicate with the Internet.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the target EIP, and click Unbind in the Act ions column.
4. In the Unbind Elast ic IP Address dialog box, click OK.

### 3.5 Release an EIP

This topic describes how to release an Elastic IP address (EIP). The EIP is disassociated from all instances. For more information, see Disassociate an EIP from a cloud resource.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the target EIP, move the mouse pointer over More
operat ions in the Act ions column, and then click Release.
4. In the Release an EIP dialog box, click OK.

## 4 Manage EIPs

### 4.1 Create a EIP

This topic describes how to create a EIP. An EIP is a public IP address that you can purchase and hold as an independent resource.
1. Log on to the EIP console.
2. On the Elast ic IP Addresses page, click Creat e EIP.
3. On the Creat e Elast ic IP Address page, set the parameters and click Submit . The following table
describes the configuration parameters.

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the EIP belongs. |
| Resource Set | Select the resource set to which the EIP belongs. |
| Region | Select a region for the EIP. Make sure that the EIP and the cloud resource to be associated with the EIP are located in the same region. |
| Zone | Select the zone to which the EIP belongs. |
| Line T ype | Select the line type of the EIP. |
| Net work T ype | Select the network type of communication for which the EIP will be used. Public Net work: Use the EIP to enable communication with the Internet. Hybrid Cloud: Use the EIP to enable communication within a hybrid cloud. For example, if you need to establish network connections from an on-premises data center to the Internet by using source network address translation (SNAT) and destination network address translation (DNAT), you must select this type for your EIP. |
| Service IP | Specify a specific EIP. Make sure that the specified IP address is an IPv4 address and is not taken by another account. Otherwise, the EIP cannot be allocated. Not e If you do not specify a service IP, a random EIP will be assigned to you by the system. |
| Peak Bandwidt h | Specify the maximum bandwidth for the EIP. Unit: Mbit/s. |

### 4.2 Bind an EIP to a cloud instance

#### 4.2.1 Associate an EIP with an ECS instance

This topic describes how to associate an EIP with an ECS instance deployed in a VPC. ECS instances that are associated with EIPs can communicate with the Internet. You have created an ECS instance. For more information, see the Creat e an inst ance topic of Quick st art in the Apsara Stack Elastic Compute Service User Guide.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the target EIP, and then click Bind in the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select ECS Inst ance. |
| ECS Inst ance | Select the ECS instance to be associated with the EIP. When you select an ECS instance, note the following points: The ECS instance must be deployed in a VPC. The ECS instance must be running or stopped. An ECS instance can be associated with only one EIP. The ECS instance and the EIP must reside in the same region. The ECS instance is not associated with a public IP address or another EIP. |

#### 4.2.2 Associate an EIP with an SLB instance

This topic describes how to associate an EIP with an SLB instance. After the association, the SLB instance can distribute requests from the Internet. You have created an SLB instance. For more information, see the Creat e an SLB inst ance topic of Quick st art in the Apsara Stack Server Load Balancer User Guide. 1.

## 2 Log on to the EIP console.

3. In the top navigation bar, select the region where the EIP is created.
4. On the Elast ic IP Addresses page, find the EIP that you want to manage, and click Bind
Resource in the Act ions column.
5. In the Bind Elast ic IP Address dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select SLB Inst ance. |
| SLB Inst ance | Select the SLB instance to be associated with the EIP. When you select an SLB instance, note the following points: The SLB instance must be deployed in a VPC. The SLB instance and the EIP must reside in the same region. An SLB instance can be associated with only one EIP. |

#### 4.2.3 Associate an EIP with an HAVIP

This topic describes how to associate an EIP with an HAVIP. After the association, the HAVIP can be used to connect to the Internet. You have created an HAVIP. For more information, see the Creat e an HAVIP topic of HAVIPs in the Apsara Stack Virtual Private Cloud User Guide.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage, and click Bind
Resource in the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select HaVip Address. |
| HaVip Address | Select the HAVIP to be associated with the EIP. When you select an HAVIP, note the following points: The HAVIP and the EIP must reside in the same region. The HAVIP must be available or allocated. An HAVIP can be associated with only one EIP. |

#### 4.2.4 Associate an EIP with a NAT gateway

This topic describes how to associate an EIP with a NAT gateway. After the association, you can use the EIP to configure DNAT and SNAT entries. You have created a NAT gateway. For more information, see the Creat e a NAT gat eway topic of Quick st art in the Apsara Stack NAT Gateway User Guide.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage, and click Bind
Resource in the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select NAT Gat eway. |
| NAT Gat eway | Select the NAT gateway to be associated with the EIP. When you select a NAT gateway, note the following points: The NAT gateway and the EIP must reside in the same region. A NAT gateway can be associated with a maximum of 20 EIPs. |

#### 4.2.5 Bind an EIP to a secondary ENI

##### 4.2.5.1 Overview

This topic provides an overview of EIP associations with ENIs. You can associate EIPs with ENIs to build a highly robust, flexible, and scalable IT solution. This also allows a cloud server to use multiple public IP addresses. An ENI is assigned with a private IP address. After you associate an EIP with an ENI, the ENI has both a private IP address and a public IP address. When you migrate an ENI that is associated with an EIP from an ECS instance to another ECS instance, the public and private IP addresses are also migrated. This provides a highly reliable and available IP migration solution for cloud servers that use both public and private IP addresses. To enable an ECS instance to use multiple public IP addresses, you can associate the ECS instance with multiple ENIs, and then associate each ENI with an EIP. You can use these public IP addresses along with security group rules to provide external services. Association modes You can associate an EIP with an ENI in one of the following two modes: NAT mode Cut-through mode

| Feature | NAT mode | Cut-through mode | Multi-EIP to ENI mode |
|---|---|---|---|
| Support for displaying the associated EIPs in the ENI information | No | Yes Not e You can run the if conf ig or ipconf ig command to query the EIP associated with the corresponding ENI. | Yes Not e After a static IP address is assigned to an ECS instance, you can run the if conf ig or ipconf ig command to query the EIP associated with the corresponding ENI. |
| Supported ENIs that can be associated with EIPs | Primary and secondary ENIs | Secondary ENIs | Secondary ENIs |
| The maximum number of EIPs that can be associated with a primary ENI | 1 | EIP associations with primary ENIs are not supported. | EIP associations with primary ENIs are not supported. |

| Feature | NAT mode | Cut-through mode | Multi-EIP to ENI mode |
|---|---|---|---|
| The maximum number of EIPs that can be associated with a secondary ENI | Depends on the number of private IP addresses of the secondary ENI. Not e A one- to-one relationship is implemented between EIPs and the private IP addresses of a secondary ENI. For example, if a secondary ENI has 10 private IP addresses, a maximum of 10 EIPs can be associated with this ENI. | 1 Not e In the cut-through mode, an EIP can only be associated with the primary private IP address of a secondary ENI. | 10 Not e You can submit a ticket to request a quota increase. |
| Support for the secondary ENI to deliver networking connectivity within the private network after the ENI is associated with an EIP | Yes | No | Yes |
| Supported protocols | EIPs that are associated in the NAT mode do not support the protocols that require connection management from NAT application-level gateway (ALG), such as H.323, Session Initiation Protocol (SIP), Domain Network System (DNS), and Real Time Streaming Protocol (RTSP). | All IP protocols, such as H.323, SIP, DNS, RTSP, File Transfer Protocol (FTP), and Trivial File Transfer Protocol (TFTP). | All IP protocols, such as FTP, H.323, SIP, DNS, RTSP, and TFTP. |

The following table lists the distinguishing features of each mode.

| Feature | NAT mode | Cut-through mode |
|---|---|---|

| Feature | NAT mode | Cut-through mode |
|---|---|---|
| Support for displaying the associated EIPs in the ENI information | No | Yes Not e You can run the if conf ig or ipconf ig command to query the EIP associated with the corresponding ENI. |
| Supported ENIs that can be associated with EIPs | Primary and secondary ENIs | Secondary ENIs |
| The maximum number of EIPs that can be associated with a primary ENI | 1 | EIP associations with primary ENIs are not supported. |
| The maximum number of EIPs that can be associated with a secondary ENI | Depends on the number of private IP addresses of the secondary ENI. Not e A one-to-one relationship is implemented between EIPs and the private IP addresses of a secondary ENI. For example, if a secondary ENI has 10 private IP addresses, a maximum of 10 EIPs can be associated with this ENI. | 1 Not e In the cut- through mode, an EIP can only be associated with the primary private IP address of a secondary ENI. |
| Support for the secondary ENI to deliver networking connectivity within the private network after the ENI is associated with an EIP | Yes | No |
| Supported protocols | EIPs that are associated in the NAT mode do not support the protocols that require connection management from NAT application-level gateway (ALG), such as H.323, Session Initiation Protocol (SIP), Domain Network System (DNS), and Real Time Streaming Protocol (RTSP). | All IP protocols, such as H.323, SIP, DNS, RTSP, File Transfer Protocol (FTP), and Trivial File Transfer Protocol (TFTP). |

##### 4.2.5.2 Associate an EIP with an ENI in the NAT mode

This topic describes how to associate an EIP with an ENI in the NAT mode. With this association, both the public and private IP addresses of the ENI can be used to provide networking connectivity. EIPs associated in the NAT mode cannot be displayed in the ENI information. Before you associate an EIP with an ENI in the NAT mode, make sure that the following conditions are met: You have created a secondary ENI that is attached to a VPC. The secondary ENI and the EIP to be associated reside in the same region. For more information, see the Creat e an ENI topic of Elast ic Net work Int erf aces in the Apsara Stack Elastic Compute Service User Guide. The secondary ENI is not associated with an ECS instance. If the secondary ENI is associated with an ECS instance, you must disassociate it from the ECS instance. You can re-associate the ENI with the ECS instance after you have associated the ENI with the intended EIP in the NAT mode. For more information, see the Unbind a secondary ENI f rom an inst ance topic of Elast ic Net work Int erf aces in the Apsara Stack Elastic Compute Service User Gui de. Context The NAT mode has the following characteristics: The number of EIPs with which a secondary ENI can be associated depends on the number of private IP addresses of this secondary ENI. When an EIP is associated with an ENI in the NAT mode, both the private and public IP addresses of this ENI are available. The EIP associated with an ENI cannot be viewed in the operating system. To query the EIP associated with an ENI, call the DescribeEipAddresses operation. EIPs that are associated in the NAT mode do not support the protocols that require connection management from NAT ALG, such as H.323, SIP, DNS, RTSP, and TFTP.
1. Log on to the EIP console.
2. In the top navigation bar, select the region of the EIP.
3. On the Elast ic IP Addresses page, find the target EIP and click Bind in the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters and click OK.

| Parameter | Description |
|---|---|
| IP Address | Displays the target EIP. |
| Inst ance T ype | Select Secondary ENI. |
| Mode | Select NAT Mode. |
| Secondary ENI | Select the secondary ENI to be associated with the EIP. |

##### 4.2.5.3 Associate an EIP with an ENI in the cut-through mode

mode This topic describes how to associate an EIP with an ENI in the cut-through mode. After the association, the EIP replaces the private IP address of the secondary ENI, which changes the secondary ENI to an Internet interface. You can view the EIP in the ENI information. Before you associate an EIP with an ENI in the cut-through mode, make sure that the following conditions are met: The secondary ENI is attached to a VPC. The secondary ENI and the EIP reside in the same region. The secondary ENI is not associated with an ECS instance. If the secondary ENI is associated with an ECS instance, you must disassociate it from the ECS instance. You can re-associate the ENI with the ECS instance after you have associated the ENI with the intended EIP in the cut-through mode. For more information, see the Unbind a secondary ENI f rom an inst ance topic of Elast ic Net work Int erf aces in the Apsara Stack Elastic Compute Service User Guide. A secondary ENI can be associated with only one EIP. Context An EIP is essentially a NAT IP address. After you associate an EIP with an ENI in the NAT mode, the public IP address of the ENI is provisioned in a gateway rather than the ENI of the associated ECS instance. Therefore, the public IP address cannot be displayed in the operating system of the ECS instance, which only shows the private IP address in the ENI information. This complicates operations and maintenance because you must keep track of the mappings between network interfaces or servers and public IP addresses. In addition, EIPs that are associated with ENIs in the NAT mode do not support protocols such as H.323, SIP, DNS, or RTSP. To solve the preceding problems, you can associate an EIP with an ENI in cut -t hrough mode. In the cut-through mode: The EIP replaces the private IP address of the secondary ENI. This changes the secondary ENI to an Internet interface which can no longer deliver networking connectivity within the private network. You can view the EIP in the ENI information. To query the EIP associated with the corresponding ENI, you can call theif conf ig oripconf ig operation. EIPs that are associated in the cut-through mode support all Internet protocols, such as H.323, SIP, DNS, RTSP, FTP, and TFTP.
1. Log on to the EIP console.
2. Select the region of the EIP.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage, and click Bind
Resource in the Act ions column.
4. In the Bind Elast ic IP Address dialog box, set the following parameters and clickOK.

| Parameter | Description |
|---|---|
| Inst ance T ype | SelectSecondary ENI. |

| Guide·Manage EIPs | Elastic IP Addres |
|---|---|

| Parameter | Description |
|---|---|
| Binding mode | SelectCut -T hrough Mode. |
| Secondary ENI | Select the secondary ENI to be associated with the EIP. |

Not ice Make sure that the selected secondary ENI is not associated with an ECS instance.
5. Return to the Elastic IP Addresses page and click the ID of the associated ENI.
6. Find the target ENI from the list of ENIs. In the Act ions column, clickBind to associate the ENI with
an ECS instance. The maximum number of ENIs that can be associated with an ECS instance depends on the specification of the ECS instance. For more Information, see the Inst ance t ypes topic of What is ECS in the Apsara Stack Elastic Compute Service User Guide. After you associate a secondary ENI with an ECS instance, you must enable Dynamic Host Configuration Protocol (DHCP) for the secondary ENI and then restart the ENI. Otherwise, the configuration made for the cut-through mode will not take effect. After the configuration is complete, a route entry is automatically created for the ECS instance with the secondary ENI as the egress interface. The priority of this route entry is lower than that of the route with the primary ENI as the egress interface. Therefore, you can adjust the priority of these entries based on your service requirements.
7. Log on to the ECS instance by using the associated EIP to check the network configuration of the
ECS instance. Make sure that the security group rules of the ECS instance allow remote access. As shown in the following figure, the IPv4 address of the ECS instance is changed to the associated EIP.

### 4.3 Upgrade a subscription EIP

This topic describes how to upgrade the bandwidth of EIP. Bandwidth upgrades take effect immediately.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the target EIP and choose More > Upgrade in the
Act ions column.
4. On the Change Specif icat ions page, set a new peak bandwidth for the EIP, and then click
Submit .

### 4.4 Disassociate an EIP from a cloud resource

resource This topic describes how to dissociate an EIP from a cloud resource when this cloud resource no longer needs to communicate with the Internet.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the target EIP, and click Unbind in the Act ions column.
4. In the Unbind Elast ic IP Address dialog box, click OK.

### 4.5 Release an EIP

This topic describes how to release an Elastic IP address (EIP). The EIP is disassociated from all instances. For more information, see Disassociate an EIP from a cloud resource.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is created.
3. On the Elast ic IP Addresses page, find the target EIP, move the mouse pointer over More
operat ions in the Act ions column, and then click Release.
4. In the Release an EIP dialog box, click OK.
