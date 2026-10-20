---
title: "Express Connect User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 50
source_pdf: "b377f391fd37824b_Alibaba Cloud Apsara Stack V3.18.6 Express Connect User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%AB%98%E9%80%9F%E9%80%9A%E9%81%93%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Express%20Connect%20User%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Express Connect User Guide 20260629

## Table of Contents

- 1 Log on to the Express Connect console
- 2 Getting started
  - 2.1 What is Express Connect?
  - 2.2 Peering connections
  - 2.3 Overview of Express Connect
  - 2.4 VBRs
  - 2.5 Connect a data center to a VPC by using an Express Connect circuit
- 3 Overview
- 4 VPC peering
  - 4.1 Create and manage VPC peering connections
  - 4.2 Configure routes
- 5 VBR-to-VPC connections
- 6 Physical connections
  - 6.1 Create and manage connections over Express Connect circuits
  - 6.2 Modify an Express Connect circuit
  - 6.3 Delete a connection over an Express Connect circuit
  - 6.4 Manage a VBR
- 7 VBRs
  - 7.1 Create and manage a VBR
  - 7.2 Manage Express Connect circuits
  - 7.3 Add and manage routes
  - 7.4 Configure and manage BGP
  - 7.5 Manage VBR-to-VPC connections
  - 7.6 Configure a failover group
  - 7.7 Attach a VBR to a CEN instance across accounts
- 8 Manage operation logs
- 9 Manage tags

Connect console

## 1 Log on to the Express Connect console

**Connect console**

This topic describes how to log on to the Express Connect console from the Apsara Unimanager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. Enter the correct username and password.
Connect console Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
> **Forgot password**
> If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.

3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see the **Security Center** > **Multi-factor Authentication** > **Manage Multi-factor Authentication** section in the Apsara Uni-manager Management Console User Guide.

5. In the top navigation bar, choose **Products > Networking > Express Connect**.
6. In the top navigation bar, select the region.

## 2 Getting started

### 2.1 What is Express Connect?

This topic provides an overview of Express Connect. Express Connect allows you to establish private connections to enable fast, stable, and secure communication between different networking environments. You can use Express Connect to ensure network stability and prevent data breaches.

**Features**

You can use a leased line provided by an Internet Service Provider (ISP) to establish a physical connection between your data center and an Alibaba Cloud access point. After the physical connection is established, you can create a virtual border router (VBR) to connect your data center with Alibaba Cloud to build a hybrid cloud. The physical connections of Express Connect do not traverse the Internet, and therefore feature faster speeds, lower latency, greater security, and higher reliability compared with Internet connections. Express Connect enables you to create a peering connection between two Virtual Private Clouds (VPCs) as a channel for private communication.

**Benefits**

Express Connect provides the following benefits: High-speed interconnections Powered by the network virtualization technology of Alibaba Cloud, Express Connect allows networks to connect and exchange traffic at high speeds within internal networks without carrying traffic across the Internet. The impact of distance on network performance is minimized to ensure low-latency and high-bandwidth communication. Stability and reliability Built on the state-of-the-art infrastructure of Alibaba Cloud, Express Connect guarantees stable and reliable communication between networks. Security Express Connect implements cross-network communication at the network virtualization layer, where data is transmitted over separate and private channels within the infrastructure of Alibaba Cloud, mitigating the risks of data breaches. Buy-as-you-need service Express Connect delivers connectivity with a wide range of bandwidth options. You can choose based on the needs of your business to get the best value for your purchase.

### 2.2 Peering connections

You can create a peering connection between two virtual private clouds (VPCs) or between a VPC and a virtual border router (VBR).

**Initiator and acceptor**

One end of a peering connection functions as the initiator and the other end functions as the acceptor. Only the initiator can initiate the peering connection. The acceptor must wait for the initiator to initiate the peering connection. The concepts of initiator and acceptor are used only to control how a peering connection is established. Data transmission between the initiator and acceptor is bidirectional. Therefore, after a peering connection is established, both the initiator and acceptor can send and receive data. If you create a peering connection for two VPCs within the same account, the system of Express Connect automatically creates the initiator and acceptor. You do not need to manually initiate the connection. The system automatically sends the connection request and enables the connection. If you create a peering connection for two VPCs that belong to different accounts, you must manually initiate the connection. The following table describes the differences between an initiator and acceptor.

| Item | Initiator | Acceptor |
|---|---|---|
| Whether the configuration of the peer is required before the connection is initiated | Yes | Yes |
| Initiate the connection | Supported | Not supported |
| Send messages to the peer after the connection is established | Supported | Supported |

**Connection process and status**

In the peering connection process, the initiator initiates a connection. The acceptor then receives the connection, after which the connection is established successfully. During different stages of the connection process, the status of a peering connection is also different, as shown in the following table.

> **Note:** If you choose to create both ends at the same time when establishing a peering connection, the system automatically initiates and establishes a connection. In this case, the initiator and the acceptor become activated after being created.

| Connection process | Initiator status | Acceptor status |
|---|---|---|
| The initiator initiates a connection. | Connecting | Accepting |
| The connection is established. | Activated | Activated |
| The connection is suspended. | Suspending | Suspending |
| The connection is broken. | Suspended | Suspended |
| A connection is re-initiated. | Activating | Activating |
| The connection is established. | Activated | Activated |

### 2.3 Overview of Express Connect

Express Connect offers a secure, reliable, and high-performance solution for connecting your data centers to Apsara Stack. You can lease an Express Connect circuit from a connectivity provider and use the Express Connect circuit to connect a data center to an Apsara Stack access point. Connections over Express Connect circuits are not exposed to the Internet. Compared with Internet connections, connections over Express Connect circuits are safer, faster, and more reliable with lower network latency.

**Connection methods**

You can apply for an Express Connect circuit to establish a connection. You can lease an Express Connect circuit to connect your data center to an access point of Apsara Stack. The Express Connect circuit is dedicated to you. You can apply for dedicated connections over Express Connect circuits. For more information, see Apply for an Express Connect circuit.

### 2.4 VBRs

Virtual border routers (VBRs) are an abstraction of Express Connect circuits that are isolated and virtualized by using the Layer 3 overlay and vSwitch technologies in the Software Defined Network (SDN) architecture. A VBR is deployed between the customer-premises equipment (CPE) and a virtual private cloud (VPC) and is used to exchange data between the VPC and data center.

> **Note:** Similar to VPC routers, each VBR manages a route table. You can add routes to the route table of a VBR to control network traffic forwarding.

**Features**

A VBR provides the following features: Exchanges data between a VPC and a data center. Determines the type of virtual interface of an Express Connect circuit: Layer 3 router interface or Layer 3 Virtual Local Area Network (VLAN) subinterface. Adds or identifies VLAN tags if a Layer 3 VLAN subinterface is used. Supports Border Gateway Protocol (BGP) routing. BGP is a dynamic routing protocol based on Transmission Control Protocol (TCP). BGP is used to exchange routing and network accessibility information across autonomous systems. When you create a connection over an Express Connect circuit, you can configure BGP routing between your data center and the associated VBR. This way, the data center and the VBR can communicate with each other through a private connection. This helps you to set up a hybrid cloud with higher efficiency, flexibility, and security. VBRs support BGP dynamic routing in both IPv4 and IPv6 networks.

**Limits**

VBRs do not support source address-specific policy-based routes. Each VBR has one and only one route table. VBRs support only BGP-4. You can create at most eight BGP peers for each VBR. Each BGP peer supports at most 110 dynamic routes. Routes are denied when the upper limit is exceeded. To configure BGP when you connect to a VPC, you must specify an Autonomous System Number (ASN) for the VPC. The ASN that you specify must be different from the ASNs of the vSwitches in the VPC.

### 2.5 Connect a data center to a VPC by using an Express Connect circuit

**VPC by using an Express Connect**

**circuit**

You can connect a data center to a virtual private cloud (VPC) on Alibaba Cloud by using an Express Connect circuit. This way, the data center and the VPC can exchange data by using private connections.

**Step 1: Confirm the access point**

Before you apply for an Express Connect circuit, you must choose an access point, check the inventory, and contact a connectivity provider for a pre-installation site survey. An access point is where network services are provided and supports multiple types of connections between a data center and Apsara Stack. When you choose an access point, take note of factors such as the region, connectivity provider, and port.

**Step 2: Apply for an Express Connect circuit**

> **Note:** To apply for an Express Connect circuit, you need to log on to the Apsara Uni-manager Operations Console.

## 1 Log on to the Express Connect console

2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, click **Apply for Physical Connection**.
4. Go to the Apsara Uni-manager Operations Console to configure an Express Connect circuit
as prompted.

**Step 3: Enable the connection over the Express Connect circuit**

The Express Connect circuit interface requested in Step 2 is in the **Allocating Resources** state. After resources are allocated, refresh the **Physical Connection** page. After the Express Connect circuit enters the **Pending Confirmation** state. Perform the following steps to enable the Express Connect circuit:
1. On the **Physical Connection** page, find the Express Connect circuit in the **Disabled** state
and click **Enable Connection** in the **Actions** column.
2. In the **Enable Connection** message, click **OK**.

**Step 4: Create a virtual border router (VBR)**

After the Express Connect circuit is enabled, the Express Connect circuit enters the **Enabled** state on the **Physical Connection** page. You need to create a VBR to enable communication between the data center and the VPC. After a VBR is created and enters the **Normal** state, run the **ping** command to check the connectivity between the on-premises gateway in the data center and the Alibaba Cloud gateway of the VBR.
1. On the **Physical Connection** page, find the **Enabled** Express Connect circuit and click its
ID in the **ID/Name** column.
2. On the details page of the Express Connect circuit, click **Create VBR** in the **Connected**
**VBRs** section.
3. In the **Create VBR** dialog box, specify the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Basic Information |   |
| Account Type | Current Organization: creates a VBR for the current organization. Another Organization: creates a VBR for another organization. In this example, Current Organization is selected. |
| Organization | Select an organization for the VBR. Note This parameter is required if you set Account Type to Current Organization. |
| Resource Set | Select the resource set to which the VBR belongs. Note This parameter is required if you set Account Type to Current Organization. |
| Name | Enter a name for the VBR. Note This parameter is required if you set Account Type to Current Organization. |
| Organization UID | Enter the UID of another organization. Note This parameter is required if you set Account Type to Another Organization. |
| Physical Connection Configurations |   |
| Physical Connection | Select an Express Connect circuit that is enabled and works as expected. |

| VLAN ID | Enter a VLAN ID for the VBR. Valid values: 0 to 3999. If the VLAN ID is set to 0, VLAN is not enabled and the switch port on the VBR is a Layer 3 router interface instead of a VLAN interface. When a Layer 3 router interface is used, each Express Connect circuit corresponds to one VBR. If the VLAN ID is set to a value from 1 to 3999, the switch port on the VBR is a Layer 3 VLAN subinterface. When a Layer 3 VLAN subinterface is used, each VLAN ID is associated with a VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to VPCs that belong to different Apsara Stack accounts. VBRs in different VLANs are isolated from each other at Layer 2. Important The VLAN ID that you specify for the VBR and that of the customer- premises device must be the same. |
|---|---|
| IPv4 Address of Gateway at Alibaba Cloud Side | Enter an IPv4 address for the VBR to route network traffic between the VPC and the data center. |
| IPv4 Address of Gateway at Customer Side | Enter an IPv4 address for the gateway device in the data center to route network traffic between the data center and the VPC. It cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side. |
| Subnet Mask (IPv4 Address) | Enter the subnet mask of the IPv4 addresses that you specified for the VBR and the gateway device in the data center. |
| IPv6 Support | Specify whether to enable IPv6. Disable: disables IPv6. Enable (You cannot disable this feature after it is enabled.): If IPv6 is enabled, the VPC and data center can use IPv6 addresses. |
| IPv6 Address of Gateway at Alibaba Cloud Side | Enter an IPv6 address for the VBR to route network traffic between the VPC and the data center. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
| IPv6 Address of Gateway at Customer Side | Enter an IPv6 address for the gateway device in the data center to route network traffic between the data center and the VPC. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |

| Subnet Mask (IPv6 Address) | Enter the subnet mask of the IPv6 addresses that you specified for the VBR and the gateway device in the data center. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
|---|---|

> **Note:** Specify the IP addresses based on your network plan. The IP addresses must be in the same CIDR block. We recommend that:

1. The specified IP addresses do not conflict with IP addresses in the cloud or on-
premises IP addresses.
2. Use private IP addresses.

> Example:
> IPv4 address of the gateway at the Alibaba Cloud side: 10.0.0.1
> IPv4 address of the gateway at the customer side: 10.0.0.2
> IPv4 subnet mask: 255.255.255.252
> Set IPv6 Address of Gateway at Alibaba Cloud Side to 2408:4004:cc:400::1 (GUA address).
> Set IPv6 Address of Gateway at Customer Side to 2408:4004:cc:400::2 (GUA address).
> Set Subnet Mask (IPv6 Address) to 2408:4004:cc:400::/56.

**Step 5: Create a peering connection between the VBR and the**

**VPC**

After a connection over the Express Connect circuit is established between the data center and Apsara Stack, you must create a VBR-to-VPC peering connection between the VBR and a VPC. This way, the VPC can communicate with the data center over the private network.
1. In the left-side navigation pane, click **VBR-to-VPC**.
2. On the **VBR-to-VPC** page, click **Create Peering Connection**.
3. On the **Create Peering Connection** page, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| VBR-side Configurations |   |
| Organization/Resou rce Set | Select the organization and resource set to which the VBR belongs. |
| Region | Select the region in which the VBR resides. |

| Router Type | Select the router type on the VBR side. OnlyV BR is supported. |
|---|---|
| Access Point | Select an access point. |
| VBR | Select the ID of the VBR. |
| Router Interface Specifications | Select the router interface specification on the VBR side. 1000 Mbps 2000 Mbps 5000 Mbps 10000 Mbps |
| Router Interface Name | Enter a name for the router interface on the VBR side. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https:// . |
| Description | Enter the description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| VPC-side Configurations |   |
| Organization/Resou rce Set | Select the organization and resource set to which the VPC belongs. Note If the VPC belongs to another organization, confirm with the organization. |
| Region/Zone | Select a region and a zone in the region to which the VPC belongs. |
| Router Type | Select the router type on the VPC side. Onlyv Router is supported. |
| VPC | Select a VPC. |
| Router Interface Name | Enter a name for the router interface on the VPC side. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https:// . |

| Description | Enter the description of the VPC. The description must be 2 to 255 characters in length. It must start with a letter and cannot start with http:// or https:// . |
|---|---|
| Health Check Source IP Address | Enter the source IP address for health checks. Note The source IP address for health checks must be an idle IP address that belongs to the CIDR block of a vSwitch in the specified VPC. |
| Health Check Destination IP Address | Enter the destination IP address for health checks. Note The destination IP address must be the IP address of the customer- premises device that is connected to the VBR by using an Express Connect circuit. |

> **Note:** Before you click submit to create the instance, you can view and check the configurations of the instance in the **Configuration overview** section on the right side.
> You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
> You can click **Quota Management** (the organization/resource set does not have quotas) or click **Quota Management** (the organization/resource set has quotas) in the **Quota** section to manage quotas for the cloud service.
> For more information about quota management, see the **Quota management** topic in **Apsara Uni-manager Management Console User Guide** .

## 3 Overview

The Express Connect console provides an overview of your resources, such as connections and instances.

**Procedure**

2. In the left-side navigation pane, click **Overview**.
3. On the Overview page, you can view the connections and instances. You can analyze the
trends of resource usage to better manage your resources.

## 4 VPC peering

### 4.1 Create and manage VPC peering connections

### peering connections

This topic describes how to create a peering connection between two virtual private clouds (VPCs).

**Create a peering connection**

1. Log in to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, click **Create Peering Connection**.
4. On the **Create Peering Connection** page, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Local Configurations |   |
| Requester Organization/Requester Resource Set | The organization and resource set to which the requester VPC belongs. |
| Requester Region | The region in which the requester VPC resides. |
| Router Type | The requester router type. Only vRouter is supported. |
| Local VPC ID | The ID of the requester VPC. |
| Peer Configurations |   |
| Acceptor Organization/Acceptor Resource Set | The organization and resource set to which the acceptor VPC belongs. Note If the acceptor VPC belongs to another organization, confirm with the organization. |
| Acceptor Region | The region in which the acceptor VPC resides. |
| Router Type | The acceptor router type. Only vRouter is supported. |

| Peer VPC ID | The ID of the acceptor VPC. |
|---|---|
| Basic Configurations |   |
| Bandwidth | The maximum bandwidth for the private connections. Only 10000Mbps is supported. |

> **Note:** Before you click submit to create the instance, you can view and check the configurations of the instance in the **Configuration overview** section on the right side.
> You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
> You can click **Quota Management** (the organization/resource set does not have quotas) or click **Quota Management** (the organization/resource set has quotas) in the **Quota** section to manage quotas for the cloud service.
> For more information about quota management, see the **Quota management** topic in **Apsara Uni-manager Management Console User Guide** .

5. Create the peering connection.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created and **Router Interface (VPC-to-**
**VPC)** is displayed in the **Cloud resources** column of the service.
If the service whose **Cloud resources** value is **Router Interface (VPC-to-VPC)** does not exist on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Management Console User Guide** .

**Create a requester or an acceptor**

The following section describes the procedure to create a requester or an acceptor.
1. Log in to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, click **Create Requester/Acceptor**.
4. On the **Create Requester/Acceptor** page, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Local Settings |   |
| Organization | Select the organization to which the requester VPC belongs. |
| Resource Set | Select the resource set to which the requester VPC belongs. |

| Region | Select the region of the requester VPC. |
|---|---|
| Router Type | Select the requester router type. Only vRouter is supported. |
| Role | Select a role. Valid values: Requester Acceptor |
| VPC ID | Select the ID of the requester VPC. |
| Name | Enter a name for the requester VPC. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The name must start _ with a letter and cannot start with http:// or https:// . |
| Peer Settings |   |
| Peer Region | Select the region of the peer VPC. |
| Peer Router Type | Select the peer router type. Only vRouter is supported. |
| Specifications |   |
| Bandwidth | Specify the maximum bandwidth for the private connections. If you set Role to Requester, you can select only 10000Mbps. If you set Role to Acceptor, you can select only Negative. |

5. Create the requester or acceptor.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created and **Router Interface (VPC-to-**
**VPC)** is displayed in the **Cloud resources** column of the service.
If the service whose **Cloud resources** value is **Router Interface (VPC-to-VPC)** does not exist on the Service Management page, confirm the parameters and click **Submit**. For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Management Console User Guide** .

**What to do next**

**VPC-to-VPC connection list**

On the **VPC-to-VPC** page, you can view the created peering connections.

> **Note:** At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

You can use a keyword or a specific filter condition to filter peering connections. Click the icon in the upper-right corner of the peering connection list to select the columns that you want to show or hide. You can also drag a column name to adjust its order. Click the ID in the **Requester** column to view the details of the requester. Click **Route Settings** in the **Requester** column to manage the route configurations of the requester. Click the ID in the **Acceptor** column to view the details of the acceptor. Click **Route Settings** in the **Acceptor** column to manage the route configurations of the acceptor. Click the icon next to the value in the **Requester** or **Acceptor** column to modify the name of the requester or acceptor.

**Tag management**

You can manage tags of peering connections on the **VPC-to-VPC** page. For more information, see Manage tags.

**Modify peer information**

You can modify the peer information when a peering connection is not active.
1. On the **VPC-to-VPC** page, find the peering connection that you want to modify and click
**Modify Peer Info** in the **Actions** column.
2. In the **Modify Peer Info** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Peer Router Interface Organization UID | Enter the UID of the organization to which the peer router belongs. |
| Peer Router Interface ID | Enter the ID of the peer router interface. |
| Peer Router ID | Enter the ID of the peer router. |

**Initiate a connection**

> **Note:** If you create a peering connection for two VPCs within the same account, the system of Express Connect automatically creates the requester and acceptor. You do not need to manually initiate the connection. The system automatically sends the connection request and establishes the connection.
> If you create a peering connection for two VPCs that belong to different accounts, you must manually initiate the connection. Only the requester can initiate the peering connection. The acceptor must wait for the requester to initiate the peering connection.

1. On the **VPC-to-VPC** page, find the peering connection and click **Initiate Connection** in
the **Actions** column.
2. In the **Initiate Connection** message, click **OK**.

**Disable a peering connection**

You can disable a requester VPC or acceptor VPC of a peering connection. After a peering connection is disabled, data is no longer transmitted between the VPCs.
1. On the **VPC-to-VPC** page, find the peering connection and click **Disable Requester** or
**Disable Acceptor** in the **Actions** column.
2. In the message that appears, click **OK**.

**Enable a peering connection**

You can enable a disabled peering connection. After a peering connection is enabled, data is transmitted between the VPCs.
1. On the **VPC-to-VPC** page, find the peering connection and click **Enable Requester** or
**Enable Acceptor** in the **Actions** column.
2. In the message that appears, click **OK**.

**Delete a peering connection**

1. On the **VPC-to-VPC** page, find the peering connection and click **Delete** in the **Actions**
column.
2. In the **Delete** message, click **OK**.

### 4.2 Configure routes

This topic describes how to configure route tables for a virtual private cloud (VPC) peering connection.

**Add peer routes to the requester**

> **Note:** In this example, you can manage only operating system route tables. To manage custom route tables, go to the Route Tables page in the VPC console.

1. Log in to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, find the peering connection that you want to manage and click
**Route Settings** in the **Requester** column.
4. In the panel that appears, view the basic information about the route table and the list of
added routes. In the **Basic Information**section, the route table ID, router ID, whether IPv6 is supported, and the time when the route table was created are displayed. In the route list, you can search for route entries by destination CIDR block.
5. Click **Add Peer Route**.
6. In the **Add Route** dialog box, configure the parameters described in the following table
and click **OK**.

| Parameter | Description |
|---|---|
| Destination CIDR Block | The type of the destination CIDR block. Valid values: IPv4 CIDR Block IPv6 CIDR Block |
| IPv4 CIDR Block or IPv6 CIDR Block | After you configure the Destination CIDR Block parameter, specify a CIDR block of the selected type. If you set the Destination CIDR Block parameter to IPv4 CIDR Block, you can click Add CIDR Block to enter multiple destination CIDR blocks. |
| Next Hop Type | The type of the next hop. Be default, Router Interface (to VPC) is selected. Router Interface (to VPC): routes the traffic destined for the specified CIDR block to the specified VPC. |
| VPC | The VPC instance used to receive traffic. |
| Description | The description of the route. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

7. In the **Add Peer Route** message that appears, wait until all CIDR blocks are in the
**Successful** state and click **OK**.

**Add peer routes to the acceptor**

> **Note:** In this example, you can manage only operating system route tables. To manage custom routing tables, go to the Route Tables page in the VPC console.

1. Log in to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, find the peering connection that you want to manage and click
**Route Settings** in the **Acceptor** column.
4. In the panel that appears, view the basic information about the route table and the list of
added routes. In the **Basic Information**section, the route table ID, router ID, whether IPv6 is supported, and the time when the route table was created are displayed. In the route list, you can search for route entries by destination CIDR block.
5. Click **Add Peer Route**.
6. In the **Add Route** dialog box, configure the parameters described in the following table
and click **OK**.

| Parameter | Description |
|---|---|
| Destination CIDR Block | The type of the destination CIDR block. Valid values: IPv4 CIDR Block IPv6 CIDR Block |
| IPv4 CIDR Block or IPv6 CIDR Block | After you configure the Destination CIDR Block parameter, specify a CIDR block of the selected type. If you set the Destination CIDR Block parameter to IPv4 CIDR Block, you can click Add CIDR Block to enter multiple destination CIDR blocks. |
| Next Hop Type | The type of the next hop. Be default, Router Interface (to VPC) is selected. Router Interface (to VPC): routes the traffic destined for the specified CIDR block to the specified VPC. |
| VPC | The VPC instance used to receive traffic. |
| Description | The description of the route. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |

7. In the **Add Peer Route** message that appears, wait until all CIDR blocks are in the
**Successful** state and click **OK**.
ns

## 5 VBR-to-VPC connections

This topic describes how to create a peering connection between a virtual private cloud (VPC) and a virtual border router (VBR).

**Prerequisites**

A VPC is created. For more information, see **Create and manage a VPC** in the **Apsara**
**Stack VPC User Guide**.
A VBR to be connected to a VPC is created. For more information, see Create and manage a VBR.

**Create a peering connection**

1. Log in to the Express Connect console.
2. In the left-side navigation pane, click **VBR-to-VPC**.
3. On the **VBR-to-VPC** page, click **Create Peering Connection**.
4. On the **Create Peering Connection** page, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| VBR-side Configurations |   |
| Organization/Resou rce Set | Select the organization and resource set to which the VBR belongs. |
| Region | Select the region in which the VBR resides. |
| Router Type | Select the router type on the VBR side. OnlyV BR is supported. |
| Access Point | Select an access point. |
| VBR | Select the ID of the VBR. |
| Router Interface Specifications | Select the router interface specification on the VBR side. 1000 Mbps 2000 Mbps 5000 Mbps 10000 Mbps |
| Router Interface Name | Enter a name for the router interface on the VBR side. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https:// . |

ns

| Description | Enter the description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
|---|---|
| VPC-side Configurations |   |
| Organization/Resou rce Set | Select the organization and resource set to which the VPC belongs. Note If the VPC belongs to another organization, confirm with the organization. |
| Region/Zone | Select a region and a zone in the region to which the VPC belongs. |
| Router Type | Select the router type on the VPC side. Onlyv Router is supported. |
| VPC | Select a VPC. |
| Router Interface Name | Enter a name for the router interface on the VPC side. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter and _ cannot start with http:// or https:// . |
| Description | Enter the description of the VPC. The description must be 2 to 255 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Health Check Source IP Address | Enter the source IP address for health checks. Note The source IP address for health checks must be an idle IP address that belongs to the CIDR block of a vSwitch in the specified VPC. |
| Health Check Destination IP Address | Enter the destination IP address for health checks. Note The destination IP address must be the IP address of the customer- premises device that is connected to the VBR by using an Express Connect circuit. |

ns

> **Note:** Before you click submit to create the instance, you can view and check the configurations of the instance in the **Configuration overview** section on the right side.
> You can click a field to go to the corresponding parameter and modify the parameter setting based on your business requirements.
> You can click **Quota Management** (the organization/resource set does not have quotas) or click **Quota Management** (the organization/resource set has quotas) in the **Quota** section to manage quotas for the cloud service.
> For more information about quota management, see the **Quota management** topic in **Apsara Uni-manager Management Console User Guide** .

5. You can create a peering connection to connect the VBR to a VPC.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **Router Interface (VBR-to-**
**VPC)** is displayed in the **Cloud resources** column of the service.
Confirm the parameters and click **Confirm Order** if the following requirements are met: On the Service Management page, a service is created, and **Router Interface (VBR-to-**
**VPC)** is displayed in the **Cloud resources** column of the service.
For more information about service management, see the **Manage services** topic in
**Apsara Uni-manager Management Console User Guide** .

**What to do next**

**VBR-to-VPC connection list**

On the **VBR-to-VPC** page, you can view the details about the created peering connection in the list.

> **Note:** At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

You can use a keyword or a specific filter condition to filter peering connections. Click the ID in the **Requester** column to view the details of the requester. Click the ID in the **Acceptor** column to view the details of the acceptor. Click the icon next to the name in the **Requester** column to modify the name of the requester router interface. The name must be 2 to 128 characters in length, and can contain letters, Chinese characters, digits, underscores (_), and hyphens (-). It must start with a letter or Chinese character.

**Tag management**

On the **VBR-to-VPC** page, you can manage the tags of peering connection. For more information, see Manage tags.

**Initiate a connection**

ns
1. On the **VBR-to-VPC** page, find the peering connection and click **Initiate Connection** in
the **Actions** column.
2. In the message that appears, click **OK**.

**Disable a VBR-to-VPC connection**

You can disable the requester or acceptor of an active peering connection. After a peering connection is disabled, data is no longer transmitted between the VPC and the VBR.
1. On the **VBR-to-VPC** page, find the peering connection and click **Disable Requester** or
**Disable Acceptor** in the **Actions** column.
2. In the message that appears, click **OK**.

**Enable a VBR-to-VPC connection**

You can enable a disabled VBR-to-VPC connection. After a peering connection is enabled, data is transmitted between the VPC and the VBR.
1. On the **VBR-to-VPC** page, find the peering connection and click **Enable Requester** or
**Enable Acceptor** in the **Actions** column.
2. In the message that appears, click **OK**.

**Health check**

> **Important:** The probe duration is too short and may cause frequent business traffic switchovers. Proceed with caution.

1. On the **VBR-to-VPC** page, find the peering connection and click **Health Check** in the
**Actions** column.
2. In the **Health Check** dialog box, configure the following parameters, select **I am aware of**
**and confirm the risks**, and then click **OK**.

| Parameter | Description |
|---|---|
| Health Check Source IP Address | Enter the source IP address for health checks. |
| Health Check Destination IP Address | Enter the destination IP address for health checks. |
| Probe Duration | The interval at which probe packets are sent for health checks. Unit: seconds. Default value: 2. Valid values: 1 to 10. |
| Number of Probes | Specify the number of probes for the health check. Unit: times. Default value: 8. Valid values: 3 to 8. |

**Delete a VBR-to-VPC connection**

ns

> **Warning:** Before you delete a VBR-to-VPC connection, you need to check whether bare metal resources exist in the peer VPC after the VBR is connected to the VPC.

1. On the **VBR-to-VPC** page, find the peering connection and click **Delete** in the **Actions**
column.
2. Optional. If bare metal resources exist in the peer VPC, confirm the deletion of the VBR as
prompted in the dialog box that appears, and click **OK**.
3. In the **Delete** message, click **OK**.

## 6 Physical connections

### 6.1 Create and manage connections over Express Connect circuits

**connections over Express Connect**

**circuits**

To create a dedicated connection, you must apply for an Express Connect circuit in the console, complete the installation, and then enable the connection.

**Apply for an Express Connect circuit**

> **Note:** To apply for an Express Connect circuit, you need to log on to the Apsara Uni-manager Operations Console.

2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, click **Apply for Physical Connection**.
4. Go to the Apsara Uni-manager Operations Console to configure an Express Connect circuit
as prompted.

**Related operations**

**The list of Express Connect circuits**

On the **Express Connect circuit** page, you can view the created Express Connect circuit in the list.

> **Note:** At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

You can use a keyword or a specific filter condition to filter Express Connect circuits. Click next to the name of an Express Connect circuit in the **ID/Name** column to modify the name. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://` .

**Tag management**

On the **Physical Connection** page, you can manage tags of Express Connect circuits. For more information, see Manage tags.

**Enable an Express Connect circuit**

1. On the **Physical Connection** page, find the Express Connect circuit in the **Disabled** state
and click **Enable Connection** in the **Actions** column.
2. In the **Enable Connection** message, click **OK**.

**Cancel an Express Connect circuit**

1. On the **Physical Connection** page, find the Express Connect circuit and click **Cancel**
**Connection** in the **Actions** column.
2. In the **Cancel Connection** message, click **OK**.

**Disable an Express Connect circuit**

1. On the **Physical Connection** page, find the Express Connect circuit and click **Disable**
**Connection** in the **Actions** column.
2. In the **Disable Connection** message, click **OK**.

**Delete a connection over an Express Connect circuit**

For more information, see Delete a connection over an Express Connect circuit.

**Manage Express Connect circuits**

1. On the **Physical Connection** page, find the Express Connect circuit and click the ID in the
**ID/Name** column.
2. You can manage an Express Connect circuit on the details page.
You can view the basic information in the **Basic Information** section. Click **Modify** in the upper-right corner to modify the information. For more information, see Modify the information about an Express Connect circuit. Click next to **Description** to modify the description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://` . You can manage VBRs associated with the Express Connect circuit in the **Connected**
**VBRs** section. For more information, see Create and manage a VBR.
In the **Operation Log** section, you can view all operations logs of the Express Connect circuit. For more information, see Manage operation logs.

### 6.2 Modify an Express Connect circuit

**circuit**

You can modify the following information about an Express Connect circuit: the name, bandwidth, and the location of the customer data center.

**Procedure**

2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, find the Express Connect circuit and click the ID in the
**ID/Name** column.
4. In the **Basic Information** section of the Express Connect circuit details page, click **Modify**
in the upper-right corner.
5. In the dialog box that appears, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Name | Enter a name for the Express Connect circuit. |
| Bandwidth | Enter a maximum bandwidth value for the Express Connect circuit. Unit: Mbit/s. |
| Data Center Location | Specify the location of the data center. |

### 6.3 Delete a connection over an Express Connect circuit

**Express Connect circuit**

You can delete a connection over an Express Connect circuit that is in the Disabled state.

**Background information**

To delete a connection over an Express Connect circuit, perform the following operations in order:
1. Delete the routes on the router of the virtual private cloud (VPC) and routes on the virtual
border router (VBR).
2. If Border Gateway Protocol (BGP) routing is configured, delete the BGP peers and BGP
groups.
3. Delete a peering connection.
4. Delete the associated VBRs.
5. If the connection is not disabled, disable the connection.
6. Delete the connection over the Express Connect circuit.

**Step 1: Delete routes**

Delete routes on the VPC and the VBR.
1. Delete the routes in custom route tables in the VPC. For more information, see **Manage**
**custom routes** in **VPC User Guide**.
2. Delete the routes on the VBR. For more information, see Delete routes.

**Step 2: Delete BGP peers and BGP groups**

If BGP is configured, you must delete the BGP settings. For more information, see Delete a BGP group and Delete a BGP peer.

**Step 3: Delete peering connections**

Delete the peering connection between the VPC and the VBR. For more information, see Delete a VBR-to-VPC connection.

**Step 4: Delete the associated VBRs**

Delete the VBRs. For more information, see Delete a VBR.

**Step 5: Disable the connection over the Express Connect circuit**

2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, find the Express Connect circuit and click **Disable**
**Connection** in the **Actions** column.
4. In the **Disable Connection** message, click **OK**.

**Step 6: Delete the connection over the Express Connect circuit**

1. On the **Physical Connection** page, find the **Disabled** connection and click **Delete** in the
**Actions** column.
2. In the **Delete** message, click **OK**.

### 6.4 Manage a VBR

After you enable an Express Connect circuit, you must create a virtual border router (VBR) for the Express Connect circuit. The VBR is used to route traffic between the virtual private cloud (VPC) and your data center.

**Add a VBR for a connection over an Express Connect circuit**

2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, find the Express Connect circuit and click the ID in the
**ID/Name** column.
4. On the details page of the Express Connect circuit, click **Create VBR** in the **Connected**
**VBRs** section. For more information, see Create a VBR.

**What to do next**

**Modify a VBR**

On the details page of the Express Connect circuit, find the VBR in the **Connected VBRs** section and click **Modify** in the **Actions** column. For more information, see Modify a VBR.

**Disable a VBR**

1. On the details page of the Express Connect circuit, find the VBR in the **Connected VBRs**
section and click **Disable Connection** in the **Actions** column.
2. In the **Disable Connection** message, click **OK**.

## 7 VBRs

### 7.1 Create and manage a VBR

A VBR is a router between a customer-premises equipment (CPE) in a data center and a VPC. This topic describes how to create and manage a VBR.

**Create a VBR**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, click **Create VBR**.
4. In the **Create VBR** dialog box, specify the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Basic Information |   |
| Account Type | Current Organization: creates a VBR for the current organization. Another Organization: creates a VBR for another organization. In this example, Current Organization is selected. |
| Organization | Select an organization for the VBR. Note This parameter is required if you set Account Type to Current Organization. |
| Resource Set | Select the resource set to which the VBR belongs. Note This parameter is required if you set Account Type to Current Organization. |
| Name | Enter a name for the VBR. Note This parameter is required if you set Account Type to Current Organization. |

| Organization UID | Enter the UID of another organization. Note This parameter is required if you set Account Type to Another Organization. |
|---|---|
| Physical Connection Configurations |   |
| Physical Connection | Select an Express Connect circuit that is enabled and works as expected. |
| VLAN ID | Enter a VLAN ID for the VBR. Valid values: 0 to 3999. If the VLAN ID is set to 0, VLAN is not enabled and the switch port on the VBR is a Layer 3 router interface instead of a VLAN interface. When a Layer 3 router interface is used, each Express Connect circuit corresponds to one VBR. If the VLAN ID is set to a value from 1 to 3999, the switch port on the VBR is a Layer 3 VLAN subinterface. When a Layer 3 VLAN subinterface is used, each VLAN ID is associated with a VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to VPCs that belong to different Apsara Stack accounts. VBRs in different VLANs are isolated from each other at Layer 2. Important The VLAN ID that you specify for the VBR and that of the customer- premises device must be the same. |
| IPv4 Address of Gateway at Alibaba Cloud Side | Enter an IPv4 address for the VBR to route network traffic between the VPC and the data center. |
| IPv4 Address of Gateway at Customer Side | Enter an IPv4 address for the gateway device in the data center to route network traffic between the data center and the VPC. It cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side. |
| Subnet Mask (IPv4 Address) | Enter the subnet mask of the IPv4 addresses that you specified for the VBR and the gateway device in the data center. |
| IPv6 Support | Specify whether to enable IPv6. Disable: disables IPv6. Enable (You cannot disable this feature after it is enabled.): If IPv6 is enabled, the VPC and data center can use IPv6 addresses. |

| IPv6 Address of Gateway at Alibaba Cloud Side | Enter an IPv6 address for the VBR to route network traffic between the VPC and the data center. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
|---|---|
| IPv6 Address of Gateway at Customer Side | Enter an IPv6 address for the gateway device in the data center to route network traffic between the data center and the VPC. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
| Subnet Mask (IPv6 Address) | Enter the subnet mask of the IPv6 addresses that you specified for the VBR and the gateway device in the data center. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |

> **Note:** Specify the IP addresses based on your network plan. The IP addresses must be in the same CIDR block. We recommend that:

1. The specified IP addresses do not conflict with IP addresses in the cloud or on-
premises IP addresses.
2. Use private IP addresses.

> Example:
> IPv4 address of the gateway at the Alibaba Cloud side: 10.0.0.1
> IPv4 address of the gateway at the customer side: 10.0.0.2
> IPv4 subnet mask: 255.255.255.252
> Set IPv6 Address of Gateway at Alibaba Cloud Side to 2408:4004:cc:400::1 (GUA address).
> Set IPv6 Address of Gateway at Customer Side to 2408:4004:cc:400::2 (GUA address).
> Set Subnet Mask (IPv6 Address) to 2408:4004:cc:400::/56.

**Related operations**

**VBR list**

On the **Virtual Border Router** page, you can view the created VBRs in the list.

> **Note:** At most 100 pages are supported and a total of 10,000 entries can be displayed. To view more than 10,000 entries, use filter conditions to filter specific entries.

You can use a keyword or a specific filter condition to filter VBRs. Click next to the name in the **ID/Name** column to modify the name of the VBR.

**Manage tags**

On the **Virtual Border Router** page, you can use tags to group VBRs. For more information, see Manage tags.

**Modify a VBR**

1. On the **Virtual Border Router** page, find the VBR that you want to modify and click **Edit**
in the **Actions** column.
2. In the **Modify VBR** dialog box, specify the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Physical Connection Configurations |   |
| IPv4 Address of Gateway at Alibaba Cloud Side | Enter an IPv4 address for the VBR to route network traffic between the VPC and the data center. |
| IPv4 Address of Gateway at Customer Side | Enter an IPv4 address for the gateway device in the data center to route network traffic between the data center and the VPC. It cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side. |
| Subnet Mask (IPv4 Address) | Enter the subnet mask of the IPv4 addresses that you specified for the VBR and the gateway device in the data center. |
| IPv6 Support | Specify whether to enable IPv6. Disable: disables IPv6. Enable (You cannot disable this feature after it is enabled.): If IPv6 is enabled, the VPC and data center can use IPv6 addresses. |
| IPv6 Address of Gateway at Alibaba Cloud Side | Enter an IPv6 address for the VBR to route network traffic between the VPC and the data center. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |

| IPv6 Address of Gateway at Customer Side | Enter an IPv6 address for the gateway device in the data center to route network traffic between the data center and the VPC. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
|---|---|
| Subnet Mask (IPv6 Address) | Enter the subnet mask of the IPv6 addresses that you specified for the VBR and the gateway device in the data center. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
| BFD Detection Mode (Applicable to BFD Single-hop Scenarios) |   |
| Sending Interval | Enter the sending interval. Unit: milliseconds. Sending interval range: 200 to 1000 milliseconds. You can only enter an integer. |
| Reception Interval | Enter the reception interval. Unit: milliseconds. Reception interval range: 200 to 1000 milliseconds. You can only enter an integer. |
| Number of Probes | Enter the number of probes. Unit: times. Valid values: 3 to 10. |

**Delete a VBR**

Before you delete a VBR, you must delete the Border Gateway Protocol (BGP) groups, BGP peers, and BGP routes that are configured on the VBR. For more information, see Delete a BGP group, Delete a BGP peer, and Delete routes.
1. On the **Virtual Border Routers** page, find the VBR that you want to delete and click
**Delete** in the **Actions** column.
2. In the **Delete** message, click **OK**.

**Manage a VBR**

1. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
2. On the details page of the VBR, you can manage the VBR.
In the **Basic Information** section, you can view the basic information about the VBR. You can manage routes, configure routes, manage BGP, manage VBR-to-VPC connections, and configure failover groups. Click the **Physical Connection** tab to manage Express Connect circuits connected to the VBR. For more information, see Manage Express Connect circuits. Click the **Route Entries** tab to manage routes on the VBR. For more information, see Add and manage routes. Click the **BGP CIDR Blocks** tab to manage the BGP CIDR blocks. For more information, see Configure and manage BGP. Click the **BGP Groups** tab to manage the BGP groups. For more information, see Configure and manage BGP. Click the **BGP Peers** tab to manage the BGP peers related to the VBR. For more information, see Configure and manage BGP. Click the **VBR-to-VPC** tab to manage VBR-to-VPC connections. For more information, see Manage VBR-to-VPC connections. Click the **Failover Groups** tab to manage failover groups. For more information, see Configure failover groups. Click the **CEN Cross-Account Authorization** tab to manage cross-account authorization. For more information, see CEN cross-account authorization. On the **Operation Log** tab, you can view all operations logs of the VBR. For more information, see Manage operation logs.

### 7.2 Manage Express Connect circuits

**circuits**

After you create a virtual border router, you can associate an Express Connect circuit with the VBR or modify the Express Connect circuits that are already associated with the VBR.

**Add an Express Connect circuit**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **Physical Connection** tab.
5. Click **Add Physical Connection**.
6. In the **Add Physical Connection** dialog box, specify the parameters. For more
information, see Create a peering connection.

**Modify an Express Connect circuit**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **Physical Connection** tab.
5. In the Physical Connection list, find the Express Connect circuit and click **Modify** in the
**Actions** column.
6. In the **Modify Physical Connection** dialog box, specify the parameters. For more
information, see Modify a VBR.

### 7.3 Add and manage routes

You can add routes to the route table of a virtual border router (VBR) to manage where network traffic is forwarded. This topic describes how to add and manage routes.

**Background information**

After you create a VBR, you must add routes that point to the Express Connect circuit and the virtual private cloud (VPC) to route network traffic to the data center and the VPC. You can also configure Border Gateway Protocol (BGP) routing for a VBR. For more information, see Configure and manage BGP.

**Add a route**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **Route Entry** tab.
5. Click **Add Route Entry**.
6. In the **Add Route Entry** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Next Hop Type | Select the type of next hop. Valid values: VPC: The VBR routes network traffic to a VPC. Physical Connection: The VBR routes network traffic to an Express Connect circuit. |
| Destination CIDR Block | Enter the destination CIDR block. |
| Next Hop | The next hop. |

**Delete a route**

> **Important:** Before you delete a route, make sure that the **Status** of the route is **Available**.
> Before you delete a route whose **Next Hop Type** is **VPC**, check whether bare metal resources exist in the peer VPC.

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **Route Entry** tab.
5. In the route list, find the route that you want to delete and click **Delete** in the **Actions**
column.
6. Optional. If **Next Hop Type** of the route is **VPC**, delete the route as prompted in the dialog
box that appears and click **OK**
7. In the **Delete** message, click **OK**.

### 7.4 Configure and manage BGP

You can configure Border Gateway Protocol (BGP) routing to enable communication between a data center and a virtual border router (VBR). You must add the BGP peer that communicates with the VBR to a BGP group, and then advertise the BGP CIDR block on the VBR. This topic describes how to configure and manage BGP.

**Background information**

BGP is a dynamic routing protocol based on TCP. BGP is used to exchange routing information and network accessibility information in different autonomous systems. If you use an Express Connect circuit to connect to Apsara Stack, you can configure BGP routing to enable communication between your data center and the virtual border router (VBR) that is associated with the Express Connect circuit. BGP allows you to build hybrid clouds in a more efficient, flexible, and reliable way. Before you configure BGP routing, you must create a BGP group. BGP groups are used to simplify BGP configurations. You can add BGP peers with the same configurations to one BGP group. You need to only create a BGP group with an autonomous system number (ASN) and add BGP peers that meet your requirements to the BGP group. After you add the BGP peers to the BGP group, the BGP peers share the configurations of the BGP group. You do not need to configure each BGP peer separately.

**Limits**

Before you configure BGP routing, take note of the following limits: You can specify only the data center as the BGP peer of a VBR. The data center is connected to the VBR by using an Express Connect circuit. Static routing is required between a VBR and a virtual private cloud (VPC). VBRs support only BGP-4. You can create up to eight BGP peers for each VBR. Each BGP peer supports up to 110 dynamic routes. Routes are denied when the upper limit is exceeded. To configure BGP routing when you connect to a VPC, you must specify an ASN for the VPC. The ASN that you specify must be different from the ASNs of the vSwitches in the VPC.

**Configure BGP**

**Step 1: Create a BGP group**

Before you configure BGP routing, you must create a BGP group with the requested ASN.
2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **BGP Groups** tab.
5. Click **Create BGP Group**.
6. In the **Create BGP Group** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|

| IPv6 Support | Specify whether to enable IPv6. Yes: enables IPv6. After you enable IPv6, the endpoints of VPC and your data center can be IPv6 addresses. No: disables IPv6. |
|---|---|
| Name | Enter a name for the BGP group. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a _ letter and cannot start with http:// or https:// . |
| Peer ASN | Enter the ASN of the data center. Valid values for ASN: 1 to 65534 and 4200000000 to 4294967294. |
| BGP Key | The key of the BGP group. |
| Description | Enter the description of the BGP group. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Local ASN | The local ASN. Valid values for ASN: 1 to 65534 and 4200000000 to 4294967294. |

**Step 2: Create a BGP peer**

1. On the details page of the VBR, click the **BGP Peers** tab.
2. Click **Create BGP Peer**.
3. In the **Create BGP Peer** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| BGP Group | The BGP group to which you want to add the BGP peer. |
| BGP Peer IP Address | Enter the IP address of the BGP peer. |
| Enable BFD | Specify whether to enable BFD. |
| BFD Hop Count | Enter the number of BFD hops. Note This parameter is required only if you enable BFD. |

**Step 3: Advertise the BGP CIDR block**

After you create the BGP peer, you must advertise the CIDR block of the VPC. After the BGP session is established, the VBR automatically learns the CIDR block of the data center.
1. On the details page of the VBR, click the **Advertise BGP Subnet** tab.
2. Click **Advertise BGP Subnet**.
3. In the **Advertise BGP Subnet** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Advertised Subnet | Enter the BGP CIDR block to be advertised. |

**What to do next**

**Modify a BGP peer**

1. On the details page of the VBR, click the **BGP Peers** tab.
2. Find the BGP peer and click **Edit** in the **Actions** column.
3. In the **Modify BGP Peer** dialog box, modify the **BGP Peer IP**, **Enable BFD**, and **BFD Hop**
**Count** parameters, and click **OK**.

**Delete a BGP peer**

1. On the details page of the VBR, click the **BGP Peers** tab.
2. Find the BGP peer and click **Delete** in the **Actions** column.
3. In the dialog box that appears, click **OK**.

**Modify a BGP group**

1. On the details page of the VBR, click the **BGP Groups** tab.
2. Find the BGP group and click **Edit** in the **Actions** column.
3. In the **Modify BGP Group** dialog box, modify the **Name**, **Peer ASN**, **BFD Hop Count**,
**Description**, and **Local ASN**, and click **OK**.

**Delete a BGP group**

1. On the details page of the VBR, click the **BGP Groups** tab.
2. Find the BGP group and click **Delete** in the **Actions** column.
3. In the dialog box that appears, click **OK**.

**Delete a BGP CIDR block**

1. On the details page of the VBR, click the **Advertise BGP Subnet** tab.
2. Find the BGP CIDR block and click **Delete** in the **Actions** column.
3. In the dialog box that appears, click **OK**.

### 7.5 Manage VBR-to-VPC connections

**connections**

This topic describes how to create a peering connection. After you create a virtual border router (VBR), you must create a peering connection between the VBR and a virtual private cloud (VPC). This way, the VBR can route traffic between the VPC and the data center that is connected to the VBR.

**Create a peering connection**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **VBR-to-VPC** tab.
5. Click **Create Peering Connection**.
6. On the **Create BGP Group** page, create a peering connection. For more information, see
Create a peering connection.

**Manage a peering connection**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **VBR-to-VPC** tab.
5. On the Virtual Border Router page, you can manage peering connections. For more
information, see What to do next.

### 7.6 Configure a failover group

When the system detects a failure in an Express Connect circuit, the system performs a failover within a few seconds. To accelerate failovers, you can add virtual border routers (VBRs) to a failover group. After the system detects failures on a VBR by using Bidirectional Forwarding Detection (BDF), the system can seamlessly switch workloads to the standby VBR in the failover group within one second. This accelerates route convergence.

**Limits**

You can add only VBRs that have BFD enabled to failover groups. Each failover group can contain only two VBRs and each VBR can be added to only one failover group. The two VBRs in the same failover group must belong to the same region. You must configure the VBRs in a failover group as active and standby VBRs and configure load balancing for the VBRs.

**Prerequisites**

Two VBRs are created in the same region and each VBR is connected to your data center over an Express Connect circuit. For more information, see Create a VBR and Add routes. BFD is configured for the VBRs. For more information, see Configure BGP.

**Create a failover group**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **Failover Groups** tab.
5. Click **Configure Backup Next Hop**.
6. In the **Configure Backup Next Hop** dialog box, set the following parameters and click
**OK**.

| Parameter | Description |
|---|---|
| Region | The system automatically displays the region where the VBR is deployed. |
| Failover Group Name | Enter a name for the failover group. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a _ letter and cannot start with http:// or https:// . |
| Description | Enter a description for the failover group. The description must be 2 to 256 characters in length and cannot start with http:// or https:// . |
| Failover Group VBRs | Select a standby VBR from the drop-down list. The system lists all VBRs that are in the same region as the current VBR. |

After you complete the preceding steps, the **status** of the failover group changes to
**Normal**.

> **Note:** You cannot modify the configuration of a failover group after the failover group is created.
> If the configuration does not meet your requirements, you can delete the failover group and create one again. For more information, see Delete a failover group.

**Delete a failover group**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **Failover Groups** tab.
5. In the failover group list, find the failover group that you want to delete and click **Delete** in
the **Actions** column.
6. In the dialog box that appears, click **OK**.

### 7.7 Attach a VBR to a CEN instance across accounts

**instance across accounts**

You can attach a virtual border router (VBR) to a Cloud Enterprise Network (CEN) instance that belongs to another account. You need to log on to the VBR that belongs to Account A and then grant permissions to the CEN instance that belongs to Account B. After the authorization is complete, the VBR can be attached to the CEN instance.

**CEN authorization**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **CEN Cross-Account Authorization** tab.
5. Click **CEN Authorization**.
6. In the **CEN Authorization** dialog box, specify **Peer Level-1 Organization UID** and **Peer**
**CEN Instance ID**, and then click **OK**.

**Revoke CEN authorization**

You can revoke the CEN authorization based on your business requirements. Revoking the CEN authorization does not disconnect the VBR that corresponds to the CEN instance.
2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **Virtual Border Router** page, find the VBR and click its ID in the **ID/Name** column.
4. On the details page of the VBR, click the **CEN Cross-Account Authorization** tab.
5. In the list of authorized CEN instances, find the CEN instance and click **Delete** in the
**Actions** column.
6. In the **Cancel Authorization** dialog box, confirm the account ID and CEN instance ID, and
click **OK**. gs

## 8 Manage operation logs

Express Connect allows you to view the operation logs of related resources. The operation logs record the instance status, operation source, operation time, and API call details. You can analyze and trace historical operations based on the operation logs.

**View operation logs**

1. Log in to the Express Connect console.
2. In the left-side navigation pane, click **Operation Logs**.
3. On the Operation Logs page, view the operation logs.

> **Note:** Operation logs are retained for seven days. To adjust the retention period, modify the log storage settings as an administrator.
> If you extend the retention period by modifying the log storage settings, the log data before the new retention period is not recorded.
> Up to 100 pages of records can be displayed on the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records.

4. Click **Advanced Filter** to search for operation logs by specifying filter conditions. The
following table describes the filter conditions.

| Filter condition | Description |
|---|---|
| Resource Type | The resource type. Valid values: Router Interface, VBR, and Express Connect Circuit. |
| Event Type | The event type. Valid values: Delete Events, Create Events, and Query Events. |
| Starting and ending time | The time range that you want to query. By default, the current month is selected. |
| Resource ID | The ID of the resource. |
| IP Address | The IP address of the operation. |
| Read/Write Type | The type of the operation. Valid values: Read Operation and Write Operation. |
| Operation Result | The result of the operation. Valid values: Success and Failed. |

gs

| Keywords | The keyword. You can enter an event ID, a resource ID, an operation source IP address, or an operation name. |
|---|---|

5. **Optional.** Find the operation that you want to manage and click **View** in the **Details**
column. In the **View Operation Details** panel, view information in the **Basic Information** and **Instance Details** sections.

**View operation logs on the instance details page**

1. Log in to the Express Connect console.
2. View the operation logs of a single instance on the instance details page.
i. In the left-side navigation pane, click **Physical Connection** or **Virtual Border Router**. ii. On the page that appears, find the instance that you want to manage and click its ID. iii. On the instance details page, click the **Operation Logs** tab.

> **Note:** Operation logs are retained for seven days. To adjust the retention period, modify the log storage settings as an administrator.
> If you extend the retention period by modifying the log storage settings, the log data before the new retention period is not recorded.
> Up to 100 pages of records can be displayed on the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records.

3. **Optional.** Search for operation logs by specifying filter conditions, such as **Operation**
**Name** and **Operator**. The following table describes the filter conditions.

| Filter condition | Description |
|---|---|
| Operator | The user who performs the operation. |
| Operation Name | The name of the operation. This is the API operation name. |
| Execution Status | The execution status. Valid values: Success and Failed. |
| Operation Source IP | The source IP address of the operation. |
| Operation Time | The time range that you want to query. |

4. **Optional.** Find the operation that you want to manage and click **Operation Details** in the
**Actions** column. In the **Operation Details** panel, view information in the **Basic**
**Information** and **API Call Details** sections.

## 9 Manage tags

Express Connect allows you to search for and filter resources by tag. You can use tags to mark and classify the following resources: virtual border routers (VBRs), VPC-to-VPC connections, VBR-to-VPC connections, and connections over Express Connect circuits. This topic describes how to manage and use tags.

**Tag overview**

As the number of instances increases, it becomes more difficult to manage instances. You can use tags to group instances to help you search for and filter instances. Tags are used to mark instances. Each tag consists of a key and a value. Before you use tags, take note of the following items: You can manage tags for VPC peering connections, VBR-to-VPC connections, Express Connect circuits, and VBRs. The keys of tags that are added to the same instance must be unique. The keys and values of tags can be modified or deleted at any time. If you delete an instance, all tags added to the instance are deleted. This operation does not affect the tags added to other instances. You can add up to 20 tags to an instance. This quota cannot be increased.

**Add tags**

2. In the left-side navigation pane, click the menu item corresponding to the type of the
resources that you want to manage.
3. Add tags to instances based on the following information.
Add a tag to a single resource a. On the instances page, find the instance, move the pointer over in the **Tag** column, and click **Edit** in the pop-up message. b. In the **Edit Tags** dialog box, set the following parameters, click **Add** to add multiple tags, and then click **OK**.

| Parameter | Description |
|---|---|
| Tag Key | Select or enter a tag key. The tag key can be up to 64 characters in length and cannot start with aliyun or acs: . The tag key cannot contain http:// or https:// . |
| Tag Value | Select or enter a tag value. The tag value can be up to 128 characters in length and cannot start with aliyun or acs: . The tag value cannot contain http:// or https:// . |

c. In the **Edited** message, check the tag information and click **Close**. Add a tag to multiple resources a. On the instances page, select the instances to which you want to add tags and click
**Batch Add Tags** in the lower-left corner.
b. In the **Batch Add Tags** dialog box, configure the **Tag Key** and **Tag Value** parameters and click **OK**. c. In the **Edited** message, check the tag information and click **Close**.

**Remove tags**

2. In the left-side navigation pane, click the menu item corresponding to the type of the
resources that you want to manage.
3. Remove tags based on the following information.
Remove tags from an instance a. On the instances page, find the instance, move the pointer over in the **Tag** column, and click **Edit** in the pop-up message. b. In the **Edit Tags** dialog box, click next to the tags that you want to delete, and then click **OK**. c. In the **Edited** message, check the tag information and click **Close**. Remove tags from multiple instances a. On the instances page, select the instances from which you want to remove tags and click **Batch Remove Tags** in the lower-left corner. b. In the **Batch Remove Tags** dialog box, select the tags that you want to remove under
**Tags to Remove**, and then click **OK**.
c. In the **Edited** message, check the tag information and click **Close**.

**Search for instances by tag**

After you add tags to instances, you can quickly filter the instances by tag.
2. In the left-side navigation pane, click the menu item corresponding to the type of the
resources that you want to manage.
3. On the instances page, choose **Advanced Filter > Filter by Tag**.
4. In the dialog box that appears, specify **Tag Key** and **Tag Value**, and then click **Search**.
The instances that have the specified tag keys and tag values are displayed.
