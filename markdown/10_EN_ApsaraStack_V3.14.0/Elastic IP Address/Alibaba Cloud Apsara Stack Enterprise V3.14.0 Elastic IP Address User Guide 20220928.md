---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Elastic IP Address User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 20
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Elastic IP Address User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Elastic%20IP%20Address%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Elastic IP Address User Guide 20220928

## Table of Contents

- 1 What is Elastic IP Address?
- 2 Log on to the EIP console
- 3 Quick start
  - 3.1 Tutorial overview
  - 3.2 Apply for EIPs
  - 3.3 Associate an EIP with an ECS instance
  - 3.4 Disassociate an EIP from a cloud resource
  - 3.5 Release an EIP
- 4 Manage EIPs
  - 4.1 Apply for EIPs
  - 4.2 Bind an EIP to a cloud instance
    - 4.2.1 Associate an EIP with an ECS instance
    - 4.2.2 Associate an EIP with an SLB instance
    - 4.2.3 Associate an EIP with a NAT gateway
    - 4.2.4 Bind an EIP to a secondary ENI
      - 4.2.4.1 Overview
      - 4.2.4.2 Associate an EIP with a secondary ENI in NAT mode
  - 4.3 Resize the maximum bandwidth
  - 4.4 Disassociate an EIP from a cloud resource
  - 4.5 Release an EIP

s?

## 1 What is Elastic IP Address?

This topic provides an overview of Elastic IP Address. An elastic IP address (EIP) is a public IP address that you can purchase and use as an independent resource. You can associate an EIP with an Elastic Compute Service (ECS) instance, an internal-facing Server Load Balancer (SLB) instance, or a secondary elastic network interface (ENI) deployed in a virtual private cloud (VPC). You can also associate an EIP with a NAT gateway, or a high-availability virtual IP address (HAVIP). An EIP is a NAT IP address provisioned in the Internet-facing gateway of Alibaba Cloud and is mapped to the associated cloud resource by using NAT. After an EIP is associated with a cloud resource, the cloud resource can use the EIP to communicate with the Internet. Differences between an EIP and the static public IP address of an ECS instance The following table describes the differences between an EIP and the static public IP address of an ECS instance.

| Item | EIP | Static public IP address |
|---|---|---|
| Supported network | VPC | VPC |
| Used as an independent resource | Supported | Not supported |
| Associated with and disassociated from an ECS instance at any time | Supported | Not supported |
| Displayed in the ENI information of the operating system of the associated ECS instance | Not displayed. | Not displayed |

Line types EIPs support BGP (Multi-ISP) lines and BGP (Multi-ISP) Pro lines. The following table describes the differences between BGP (Multi-ISP) and BGP (Multi-ISP) Pro.

| Item | BGP (Multi-ISP) | BGP (Multi-ISP) Pro |
|---|---|---|

s?

| Item | BGP (Multi-ISP) | BGP (Multi-ISP) Pro |
|---|---|---|
| Advantages | BGP (Multi-ISP) provides high-quality and high-bandwidth BGP lines. Up to 89 high-quality BGP lines are available worldwide. Direct connections can be established in all regions of the Chinese mainland through lines of the following Internet Service Providers (ISPs): China Telecom, China Unicom, China Mobile, China Mobile Tietong, China Netcom, China Education and Research Network (CERNET), National Radio and Television Administration, Dr. Peng Telecom & Media Group, and Founder Broadband Network. You can use BGP (Multi-ISP) with EIP bandwidth plans to obtain bandwidth of 100 Gbit/s and higher. | BGP (Multi-ISP) Pro lines optimize data transmission to the Chinese mainland and improve connection quality for international services. Compared with BGP (Multi-ISP) lines, when BGP (Multi-ISP) Pro lines provide services to users in the Chinese mainland (excluding data centers), cross-border connections are established by using Chinese mainland ISP services. This reduces network latency. |
| Region | All regions | China (Hong Kong) and Singapore (Singapore) Not e BGP (Multi-ISP) Pro EIPs in the Singapore (Singapore) region support only the pay-as-you-go billing method. |

Benefits EIPs have the following benefits: Purchase and use as independent resources You can purchase and use an EIP as an independent resource. EIPs are not bundled with other computing or storage resources. Associate with resources at any time You can associate an EIP with a cloud resource as needed. You can also disassociate and release the EIP at any time. Modify bandwidth limits on demand You can modify the bandwidth limit of an EIP at any time to meet your business requirements. The modification immediately takes effect. e

## 2 Log on to the EIP console

This topic describes how to log on to the Apsara Uni-manager Management Console to manage your elastic IP addresses (EIPs). The Google Chrome browser is used as an example. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Login.
4. In the top menu bar, choose Product s > Net working > Elast ic IP Address.

## 3 Quick start

### 3.1 Tutorial overview

This topic provides an overview of the tutorial that guides you in creating an EIP and associating an EIP with an ECS instance to allow the ECS instance to access the Internet. This tutorial walks you through the following tasks:
1. Apply for new EIPs
An EIP is a public IP address that you can purchase and hold as an independent resource. To get started, you must create an EIP. You can associate an EIP with an ECS instance deployed in a VPC to enable the ECS instance to connect to the Internet. You can disassociate an ECS instance from an EIP when the ECS instance no longer requires access to the Internet. You can release an EIP if it is no longer needed.

### 3.2 Apply for EIPs

This topic describes how to apply for elastic IP addresses (EIPs). An EIP is a public IP address that you can purchase and hold as an independent resource. Procedure
1. Log on to the EIP console.
2. On the Elast ic IP Addresses page, click Creat e EIP.
3. On the Creat e Elast ic IP Address page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the EIP belongs. |
| Resource Set | Select the resource set to which the EIP belongs. |
| Region | Select the region where you want to create the EIP. Make sure that the EIP and the cloud resources to be associated with the EIP are deployed in the same region. |
| Quant it y | Enter the number of EIPs that you want to create. |
| EIP Name | Enter the name of the EIP that you want to create. |

| Parameter | Description |
|---|---|
| Connect ion T ype | Select a line type for the EIP. |
| Net work T ype | Select a network type for the EIP. Valid values: Int ernet : The EIP is used for communication over the Internet. Hybrid Cloud: The EIP is used for communication within a hybrid cloud. If you want to allow a data center to access the Internet by using SNAT and DNAT, you must select this type. |
| IP Address | Enter the EIP that you want to request. Make sure that you enter an idle IPv4 address. Otherwise, you cannot request the specified EIP. Not e If you do not specify an EIP, the system automatically assigns one. |
| Maximum Bandwidt h | Specify the maximum bandwidth value for the EIP. Unit: Mbit/s. |

### 3.3 Associate an EIP with an ECS instance

instance This topic describes how to associate an elastic IP address (EIP) with an Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC). ECS instances can communicate with the Internet after they are associated with EIPs. Prerequisites An ECS instance is created. For more information, see the Creat e an inst ance topic in the Quick st art chapter of Elastic Compute Service User Guide. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Bind Resource
in the Act ions column.
4. In the Bind Elast ic IP Address t o Resources dialog box, set the following parameters and click
OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select ECS Inst ance. |

| Guide·Quick start | Elastic IP Addres |
|---|---|

| Parameter | Description |
|---|---|
| Binding mode | Select the mode in which you want to associate the EIP. You can select only Normal. In NAT Mode: The EIP is associated with the ECS instance in NAT mode. Both the private IP address and public IP address of the ECS instance are available. The EIP is not displayed in the operating system. To query the public IP address of the ECS instance, call the DescribeInstances operation. The EIP does not support NAT application layer gateway (ALG) protocols such as H.323, Session Initiation Protocol (SIP), Domain Name System (DNS), Real-Time Streaming Protocol (RTSP), and Trivial File Transfer Protocol (TFTP). |
| Select an inst ance t o bind | Select the ECS instance to be associated with the EIP. Make sure that the following requirements are met: The ECS instance is deployed in a VPC. The ECS instance is in the Running or Stopped state. Each ECS instance can be associated with only one EIP. The ECS instance and the EIP reside in the same region. The ECS instance is not assigned a static public IP address. In addition, the ECS instance is not associated with another EIP. |

### 3.4 Disassociate an EIP from a cloud resource

resource This topic describes how to disassociate an elastic IP address (EIP) from a cloud resource. After an EIP is disassociated from a cloud resource, the cloud resource can no longer communicate with the Internet by using the EIP. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Unbind in the
Act ions column.
4. In the message that appears, click OK.

### 3.5 Release an EIP

This topic describes how to release an elastic IP address (EIP) that you no longer need. Prerequisites The EIP is not associated with a cloud resource. For more information, see Disassociate an EIP from a cloud resource.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and choose
> Release in the Act ions column.
4. In the Release EIP dialog box, click OK.

## 4 Manage EIPs

### 4.1 Apply for EIPs

This topic describes how to apply for elastic IP addresses (EIPs). An EIP is a public IP address that you can purchase and hold as an independent resource. Procedure
1. Log on to the EIP console.
2. On the Elast ic IP Addresses page, click Creat e EIP.
3. On the Creat e Elast ic IP Address page, set the following parameters and click Submit .

| Parameter | Description |
|---|---|
| Organizat ion | Select the organization to which the EIP belongs. |
| Resource Set | Select the resource set to which the EIP belongs. |
| Region | Select the region where you want to create the EIP. Make sure that the EIP and the cloud resources to be associated with the EIP are deployed in the same region. |
| Quant it y | Enter the number of EIPs that you want to create. |
| EIP Name | Enter the name of the EIP that you want to create. |
| Connect ion T ype | Select a line type for the EIP. |
| Net work T ype | Select a network type for the EIP. Valid values: Int ernet : The EIP is used for communication over the Internet. Hybrid Cloud: The EIP is used for communication within a hybrid cloud. If you want to allow a data center to access the Internet by using SNAT and DNAT, you must select this type. |
| IP Address | Enter the EIP that you want to request. Make sure that you enter an idle IPv4 address. Otherwise, you cannot request the specified EIP. Not e If you do not specify an EIP, the system automatically assigns one. |
| Maximum Bandwidt h | Specify the maximum bandwidth value for the EIP. Unit: Mbit/s. |

### 4.2 Bind an EIP to a cloud instance

#### 4.2.1 Associate an EIP with an ECS instance

This topic describes how to associate an elastic IP address (EIP) with an Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC). ECS instances can communicate with the Internet after they are associated with EIPs. Prerequisites An ECS instance is created. For more information, see the Creat e an inst ance topic in the Quick st art chapter of Elastic Compute Service User Guide. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Bind Resource
in the Act ions column.
4. In the Bind Elast ic IP Address t o Resources dialog box, set the following parameters and click
OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select ECS Inst ance. |
| Binding mode | Select the mode in which you want to associate the EIP. You can select only Normal. In NAT Mode: The EIP is associated with the ECS instance in NAT mode. Both the private IP address and public IP address of the ECS instance are available. The EIP is not displayed in the operating system. To query the public IP address of the ECS instance, call the DescribeInstances operation. The EIP does not support NAT application layer gateway (ALG) protocols such as H.323, Session Initiation Protocol (SIP), Domain Name System (DNS), Real-Time Streaming Protocol (RTSP), and Trivial File Transfer Protocol (TFTP). |
| Select an inst ance t o bind | Select the ECS instance to be associated with the EIP. Make sure that the following requirements are met: The ECS instance is deployed in a VPC. The ECS instance is in the Running or Stopped state. Each ECS instance can be associated with only one EIP. The ECS instance and the EIP reside in the same region. The ECS instance is not assigned a static public IP address. In addition, the ECS instance is not associated with another EIP. |

#### 4.2.2 Associate an EIP with an SLB instance

This topic describes how to associate an elastic IP address (EIP) with a Server Load Balancer (SLB) instance. After you associate an EIP with an SLB instance, the SLB instance can forward requests from the Internet. Prerequisites An SLB instance is created. For more information, see the Creat e an SLB inst ance topic in the Quick st art chapter of Server Load Balancer User Guide. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Bind Resource
in the Act ions column.
4. In the Bind Elast ic IP Address t o Resources dialog box, set the following parameters and click
OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select SLB Inst ance. |
| Select an inst ance t o bind | Select the SLB instance to be associated with the EIP. Make sure that the following requirements are met: The SLB instance is deployed in a virtual private cloud (VPC). The SLB instance and the EIP reside in the same region. Each SLB instance can be associated with only one EIP. Not e If you associate the EIP with an internal-facing SLB instance and the SLB instance has traffic of private network workloads, transient connections may occur. We recommend that you perform the association during off-peak hours or switch the workloads to another SLB instance. |

#### 4.2.3 Associate an EIP with a NAT gateway

This topic describes how to associate an elastic IP address (EIP) with a NAT gateway. After you associate an EIP with a NAT gateway, you can create DNAT and SNAT entries for the EIP. Prerequisites A NAT gateway is created. For more information, see the Creat e a NAT gat eway topic in the Quick st art chapter of NAT Gateway User Guide.
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Bind Resource
in the Act ions column.
4. In the Bind Elast ic IP Address t o Resources dialog box, set the following parameters and click
OK.

| Parameter | Description |
|---|---|
| Inst ance T ype | Select NAT Gat eway. |
| Select an inst ance t o bind | Select the NAT gateway to be associated with the EIP. Make sure that the following requirements are met: The NAT gateway and the EIP reside in the same region. Each NAT gateway can be associated with at most 20 EIPs, among which at most 10 pay-by-data-transfer EIPs can be associated. |

#### 4.2.4 Bind an EIP to a secondary ENI

##### 4.2.4.1 Overview

You can associate elastic IP addresses (EIPs) with elastic network interfaces (ENIs). Then, you can associate the ENIs with an Elastic Compute Service (ECS) instance. This way, the ECS instance can use multiple EIPs. You can use EIPs to improve the service availability, flexibility, and scalability. Each ENI is assigned a private IP address. After you associate an EIP with an ENI, both the private IP address and the EIP are available for the ENI. You can change the private IP address and public IP address of an ECS instance by replacing the secondary ENI that is associated with the ECS instance. When you replace the secondary ENI of an ECS instance, the reliability and availability of your service are not affected. You can associate multiple ENIs with an ECS instance. Make sure that an EIP is associated with each ENI. This way, the ECS instance can use multiple EIPs. The ECS instance can use the EIPs to provide Internetfacing services. You can configure security group rules for the ECS instance to control access from the Internet. Association modes NAT mode Cut-through mode Multi-EIP to ENI mode Not e The cut-through mode is supported in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Shenzhen), China (Chengdu), Singapore (Singapore), Indonesia (Jakarta), Germany (Frankfurt), UK (London), and US (Virginia). The multi-EIP to ENI mode is available only to users who have used this mode in public preview. The multi-EIP to ENI mode is supported in the following regions: China (Shenzhen), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Chengdu), Singapore (Singapore), Germany (Frankfurt), India (Mumbai), US (Virginia), and UK (London). You can associate an EIP with an ENI in NAT mode.

| Item | NAT mode | Cut-through mode | Multi-EIP to ENI mode |
|---|---|---|---|
| Whether the EIP is displayed in the ENI information of the operating system | No | Yes Not e You can run the if conf ig or ipconf ig command to query the public IP address of the ENI. | Yes Not e After you configure a static IP address in the operating system, you can run the if conf ig or ipconf ig command to query the public IP address of the ENI. |
| Types of ENIs that can be associated with EIPs | Primary and secondary ENIs | Secondary ENIs | Secondary ENIs |

| lastic IP Address |   |   | User Guide·Manage EIP |
|---|---|---|---|

| Item | NAT mode | Cut-through mode | Multi-EIP to ENI mode |
|---|---|---|---|
| Number of EIPs that can be associated with a primary ENI | 1 | N/A | N/A |
| Number of EIPs that can be associated with a secondary ENI | Depends on the number of private IP addresses of the secondary ENI Not e Each EIP is mapped to a private IP address of a secondary ENI. If a secondary ENI is assigned 10 private IP addresses, at most 10 EIPs can be associated with the secondary ENI. | 1 Not e You can associate an EIP with only the primary private IP address of a secondary ENI in cut-through mode. | 10 Not e To request a quota increase, submit a ticket. |
| Whether the private network features of a secondary ENI are available after an EIP is associated with the secondary ENI | Yes | No | Yes |
| Supported protocols | EIPs deployed as NAT application layer gateways (ALGs) do not support protocols such as H.323, Session Initiation Protocol (SIP), Domain Name System (DNS), and Real-Time Streaming Protocol (RTSP). | EIPs support all IP protocols, including FTP, H.323, SIP, DNS, RTSP, and Trivial File Transfer Protocol (TFTP). | EIPs support all IP protocols, including FTP, H.323, SIP, DNS, RTSP, and TFTP. |

The following table describes the features in NAT mode.

| Item | NAT mode |
|---|---|
| Whether the EIP is displayed in the ENI information of the operating system | No |
| Types of ENIs that can be associated with EIPs | Primary and secondary ENIs |

| Item | NAT mode |
|---|---|
| Number of EIPs that can be associated with a primary ENI | 1 |
| Number of EIPs that can be associated with a secondary ENI | Depends on the number of private IP addresses of the secondary ENI Not e Each EIP is mapped to a private IP address of a secondary ENI. If a secondary ENI is assigned 10 private IP addresses, at most 10 EIPs can be associated with the secondary ENI. |
| Whether the private network features of a secondary ENI are available after an EIP is associated with the secondary ENI | Yes |
| Supported protocols | EIPs deployed as NAT application layer gateways (ALGs) do not support protocols such as H.323, Session Initiation Protocol (SIP), Domain Name System (DNS), and Real-Time Streaming Protocol (RTSP). |

##### 4.2.4.2 Associate an EIP with a secondary ENI in NAT mode

mode This topic describes how to associate an elastic IP address (EIP) with a secondary elastic network interface (ENI) in NAT mode. After you associate an EIP with a secondary ENI, both the private IP address and public IP address that are assigned to the secondary ENI are available. In this case, the EIP is not displayed in the secondary ENI information. Prerequisites Before you associate an EIP with a secondary ENI in NAT mode, make sure that the following requirements are met: A secondary ENI that is deployed in a virtual private cloud (VPC) is created. The secondary ENI and the EIP reside in the same region. For more information, see the Creat e an ENI topic in the Elast ic net work int erf aces chapter of Elastic Compute Service User Guide. The secondary ENI is not associated with an Elastic Compute Service (ECS) instance. If the secondary ENI is associated with an ECS instance, disassociate the secondary ENI from the ECS instance first. Then, associate the EIP with the secondary ENI in NAT mode and associate the secondary ENI with the ECS instance. For more information, see the Unbind a secondary ENI f rom an inst ance topic in the Elast ic net work int erf aces chapter of Elastic Compute Service User Guide. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Bind Resource
4. In the Bind Elast ic IP Address t o Resources dialog box, set the following parameters and click

| Parameter | Description |
|---|---|
| Inst ance T ype | Select Secondary ENI. |
| Binding mode | Select Normal. In NAT Mode: The number of EIPs that can be associated with a secondary ENI is based on the number of private IP addresses that are assigned to the secondary ENI. When an EIP is associated with a secondary ENI in NAT mode, both the private IP address and public IP address that are assigned to the secondary ENI are available. The EIP is not displayed in the operating system. To query the EIP, call the DescribeEipAddresses operation. The EIP does not support NAT application layer gateway (ALG) protocols such as H.323, Session Initiation Protocol (SIP), Domain Name System (DNS), Real-Time Streaming Protocol (RTSP), and Trivial File Transfer Protocol (TFTP). |
| Select an inst ance t o bind | Select the secondary ENI to be associated with the EIP. Make sure that the following requirements are met: The secondary ENI is deployed in a VPC. The secondary ENI and the EIP reside in the same region. |

### 4.3 Resize the maximum bandwidth

This topic describes how to resize the maximum bandwidth for elastic IP addresses (EIPs). After you change the maximum bandwidth value for an EIP, the new value immediately takes effect. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and choose
> Modif y

Conf igurat ion in the Act ions column.
4. On the Change Specif icat ions page, specify a new bandwidth value and click Submit .

### 4.4 Disassociate an EIP from a cloud resource

resource This topic describes how to disassociate an elastic IP address (EIP) from a cloud resource. After an EIP is disassociated from a cloud resource, the cloud resource can no longer communicate with the Internet by using the EIP. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and click Unbind in the
Act ions column.
4. In the message that appears, click OK.

### 4.5 Release an EIP

This topic describes how to release an elastic IP address (EIP) that you no longer need. Prerequisites The EIP is not associated with a cloud resource. For more information, see Disassociate an EIP from a cloud resource. Procedure
1. Log on to the EIP console.
2. In the top navigation bar, select the region where the EIP is deployed.
3. On the Elast ic IP Addresses page, find the EIP that you want to manage and choose
> Release in the Act ions column.
4. In the Release EIP dialog box, click OK.
