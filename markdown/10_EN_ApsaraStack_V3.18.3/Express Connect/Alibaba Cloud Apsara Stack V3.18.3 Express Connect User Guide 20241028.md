---
title: "Alibaba Cloud Apsara Stack V3.18.3 Express Connect User Guide 20241028"
product_version: "V3.18.3"
doc_version: "20241028"
pdf_pages: 37
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Express Connect User Guide 20241028.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E9%AB%98%E9%80%9F%E9%80%9A%E9%81%93/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Express%20Connect%20User%20Guide%2020241028.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Express Connect User Guide 20241028

## Table of Contents

- 1 What is Express Connect?
- 2 Log on to the Express Connect console
- 3 Overview page
- 4 VPC peering connections
  - 4.1 Peering connections
  - 4.2 Create and manage a VPC-to-VPC connection
  - 4.3 Create and manage a VBR-to-VPC connection
- 5 Physical connections
  - 5.1 Connections over Express Connect circuits
  - 5.2 Create a connection over an Express Connect circuit
  - 5.3 Delete a connection over an Express Connect circuit
- 6 VBRs
  - 6.1 VBRs
  - 6.2 Create and manage a VBR
  - 6.3 Configure and manage BGP
  - 6.4 Add and manage routes
  - 6.5 Create a peering connection
- 7 Manage tags
- 8 Manage operation logs

ect?

## 1 What is Express Connect?

Express Connect allows you to establish private connections to enable fast, stable, and secure communication between different network environments. You can use Express Connect to ensure network stability and prevent data breaches during transmission.

**Features**

You can use a leased line provided by an Internet service provider (ISP) to establish a physical connection between your data center and an Apsara Stack access point. After the physical connection is established, you can create a virtual border router (VBR) to connect your data center with Apsara Stack to build a hybrid cloud. An Express Connect circuit connects your data center to Apsara Stack over a private network. Compared with Internet-based connections, connections over Express Connect circuits reduce network latency, enhance security, and improve reliability. Express Connect allows you to create a peering connection between two virtual private clouds (VPCs) as a channel for private communication.

**Benefits**

Express Connect provides the following benefits: High-speed connections Express Connect allows networks to communicate with each other through direct, private, and high-speed connections based on the network virtualization technology of Apsara Stack. Network traffic does not need to traverse the Internet. The impact of distance on network performance is minimized to ensure low-latency and high-bandwidth communication. Stability and reliability Express Connect provides services based on the high-quality infrastructure of Apsara Stack. This ensures stable and reliable communication between networks. Security Express Connect allows you to virtualize your networks and enables communication based on the infrastructure provided by Apsara Stack. Networks owned by different accounts are independent of each other. Data packets are exchanged through private connections to prevent data breaches during transmission. Connect console

## 2 Log on to the Express Connect console

**Connect console**

This topic describes how to log on to the Express Connect console from the Apsara Unimanager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language.

2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must follow the on-screen instructions to change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**. Connect console

> **Note:** For more information about how to enable MFA and bind an MFA device, see **MFA** in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Networking > Express Connect**.

## 3 Overview page

The Overview page in the Express Connect console allows you to gain an insight into the features that are supported by Express Connect, quickly detect the number of created instances and connections, and analyze resource usage trends. This provides an overview of resource usage.

**Procedure**

2. In the left-side navigation pane, click **Overview** to view your resources.
ons

## 4 VPC peering connections

### 4.1 Peering connections

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

ons

| The connection is established. | Activated | Activated |
|---|---|---|

### 4.2 Create and manage a VPC-to-VPC connection

**VPC connection**

A VPC-to-VPC peering connection allows two virtual private clouds (VPCs) to communicate with each other. This topic describes how to create and manage a VPC-to-VPC connection.

**Create a VPC-to-VPC connection**

You can directly create a peering connection between two VPCs. After the peering connection is created, the system automatically initiates the connection.
1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, click **Create Peering Connection**.
4. On the page that appears, configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Local Configuration |   |
| Organization | Select the organization to which the initiator VPC belongs. |
| Resource set | Select the resource group to which the initiator VPC belongs. |
| Region | Select the region in which the initiator VPC resides. |
| Router type | Use the default value VPC router for this parameter. |
| Initiator VPC ID | Select the ID of the initiator VPC. |
| Peer Configuration |   |
| Organization | Select the organization to which the acceptor VPC belongs. Note If the acceptor VPC belongs to another organization, confirm with the organization. |
| Resource set | Select the resource group to which the acceptor VPC belongs. |

ons

| Region | Select the region in which the acceptor VPC resides. |
|---|---|
| Router type | Use the default value VPC router for this parameter. |
| Receiving end VPC ID | Select the ID of the acceptor VPC. |
| Basic configuration |   |
| Bandwidth value | Select a bandwidth for communication between the two VPCs over the private network. |

**Create the initiator or acceptor of a VPC-to-VPC peering**

**connection**

You can create one end of a VPC-to-VPC peering connection, manually add the peer information, and then initiate the connection.
1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, click **Create Requester/Acceptor**.
4. On the **Create Peer Connections** page, configure the following parameters and click
**Submit**.

| Parameter | Description |
|---|---|
| Local Configuration |   |
| Organization | Select the organization to which the local VPC belongs. |
| Resource Group | Select the resource group to which the local VPC belongs. |
| Region | Select the region in which the local VPC resides. |
| Router Type | Use the default value VPC router for this parameter. |
| Role | Select Initiator or Receiving End. |
| VPC ID | Select the ID of the local VPC. |
| Name | Enter a name for the local VPC. |

ons

| Peer Configuration |   |
|---|---|
| Peer region | Select the region in which the peer VPC resides. |
| Peer router type | Use the default value VPC router for this parameter. |
| Specification Configuration |   |
| Bandwidth | Select a bandwidth for communication between the two VPCs over the private network. |

**What to do next**

After you create the initiator or acceptor for a VPC-to-VPC peering connection, you need to perform the following operations:
1. Modify the peer information.
i. On the **VPC-to-VPC** page, find the connection that you want to modify and click **Modify**
**Peer Info** in the **Actions** column.
ii. In the **Modify Peer Info** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Peer Router Interface Organization UID | Enter the UID of the organization to which the peer VPC belongs. |
| Peer Router Interface ID | Enter the ID of the peer router interface. |
| Peer Router ID | Enter the ID of the peer router. |

2. Initiate the connection.
On the **VPC-to-VPC** page, find the connection that you want to manage and click **Initiate**
**Connection** in the **Actions** column.

**Delete a VPC-to-VPC connection**

1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **VPC-to-VPC**.
3. On the **VPC-to-VPC** page, find the VPC-to-VPC connection that you want to delete and click
**Delete** in the **Actions** column.
4. In the **Delete** message, click **OK**.

**Related operations**

| Operation | Description |
|---|---|

ons

| Find the connection that you want to manage | You can use one of the following methods to find the connection: On the VPC-to-VPC page, click Tag Filter and configure the Tag Key and Tag Value parameters to filter the connections by tag. On the VPC-to-VPC page, select Name or ID and enter a connection name or connection ID to perform a fuzzy match. |
|---|---|
| Modify the name of a connection | 1. On the VPC-to-VPC page, find the connection that you want to manage and move the pointer over the icon below the connection ID. 2. In the Rename dialog box, enter a name for the connection and click OK. |
| Freeze a VPC-to-VPC connection | You can freeze one or both ends of a VPC-to-VPC connection. On the VPC-to-VPC page, find the VPC-to-VPC connection that you want to manage and click Disable Initiator in the Actions column. In the message that appears, click OK. On the VPC-to-VPC page, find the VPC-to-VPC connection that you want to manage and click Disable Acceptor in the Actions column. In the message that appears, click OK. |
| Unfreeze a VPC-to-VPC connection | If you want to use a VPC-to-VPC connection that is frozen, perform the following operations to unfreeze it: On the VPC-to-VPC page, find the VPC-to-VPC connection that you want to manage and click Enable Initiator in the Actions column. In the message that appears, click OK. On the VPC-to-VPC page, find the VPC-to-VPC connection that you want to manage and click Enable Acceptor in the Actions column. In the message that appears, click OK. |

### 4.3 Create and manage a VBR-to-VPC connection

**VPC connection**

A VBR-to-VPC peering connection allows a virtual border router (VBR) and a virtual private cloud (VPC) to communicate with each other. This topic describes how to create and manage a VBR-to-VPC connection.

**Create a VBR-to-VPC connection**

1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **VBR-to-VPC**.
3. On the **VBR-to-VPC** page, click **Create Peering Connection**.
4. On the Create a peer connection page, configure the following parameters and click
**Submit**.
ons

| Parameter | Description |
|---|---|
| Configuration on the VBR side |   |
| Organization | Select the organization to which the VBR belongs. |
| Resource Set | Select the resource group to which the VBR belongs. |
| Geography | Select the region in which the VBR resides. |
| Router Type | Use the default value Border Router for this parameter. |
| Access Point | Select an access point. |
| VBR | Select the ID of the VBR. |
| Router interface specifications | Select the interface specifications of the VBR. In this example, 1000 Mbps is selected. |
| Router Interface Name | Enter a name for the VBR interface. |
| Description | Enter a description. |
| VPC-side configuration |   |
| Organization | Select the organization to which the VPC belongs. Note If the VPC belongs to another organization, confirm with the organization. |
| Resource Set | Select the resource group to which the VPC belongs. |
| Geography | Select the region in which the VPC resides. |
| Availability Zone | Select a zone in the region to which the VPC belongs. |
| Router Type | Use the default value VPC router for this parameter. |

ons

| VPC | Select a VPC. |
|---|---|
| Router Interface Name | Enter a name for the VPC router interface. |
| Description | Enter a description. |
| Health check source IP address | Enter the source IP address for health checks. Note The source IP address for health checks must be an idle IP address that belongs to the CIDR block of a vSwitch in the specified VPC. |
| Health check destination IP address | Enter the destination IP address for health checks. Note The destination IP address must be the IP address of the customer- premises device that is connected to the VBR by using an Express Connect circuit. |

**Delete a VBR-to-VPC connection**

1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **VBR-to-VPC**.
3. On the **VBR-to-VPC** page, find the VBR-to-VPC connection that you want to delete and click
**Delete** in the **Actions** column.
4. In the **Delete** message, click **OK**.

**Related operations**

| Operation | Description |
|---|---|
| Find the connection that you want to manage | You can use one of the following methods to find the connection: On the VBR-to-VPC page, click Tag Filter and configure the Tag Key and Tag Value parameters to filter the connections by tag. On the VBR-to-VPC page, select Name or ID and enter a connection name or connection ID to perform a fuzzy match. |

ons

| Modify the name of a connection | 1. On the VBR-to-VPC page, find the connection that you want to manage and move the pointer over the icon below the connection ID. 2. In the Rename dialog box, enter a name for the connection and click OK. |
|---|---|
| Freeze a VBR-to-VPC connection | You can freeze one or both ends of a VBR-to-VPC connection. On the VBR-to-VPC page, find the VBR-to-VPC connection that you want to manage and click Disable Initiator in the Actions column. In the message that appears, click OK. On the VBR-to-VPC page, find the VBR-to-VPC connection that you want to manage and click Disable Acceptor in the Actions column. In the message that appears, click OK. |
| Unfreeze a VBR-to-VPC connection | If you want to use a VBR-to-VPC connection that is frozen, perform the following operations to unfreeze it: On the VBR-to-VPC page, find the VBR-to-VPC connection that you want to manage and click Enable Initiator in the Actions column. In the message that appears, click OK. On the VBR-to-VPC page, find the VBR-to-VPC connection that you want to manage and click Enable Acceptor in the Actions column. In the message that appears, click OK. |

## 5 Physical connections

### 5.1 Connections over Express Connect circuits

**Connect circuits**

Express Connect enables fast and secure data transmission between data centers and Apsara Stack. You can lease an Express Connect circuit from a connectivity provider and use the Express Connect circuit to connect a data center to an Apsara Stack access point. Connections over Express Connect circuits are not exposed to the Internet. Compared with Internet connections, connections over Express Connect circuits are safer, faster, and more reliable with lower network latency.

**Connection methods**

You can apply for an Express Connect circuit to establish a connection. You can lease an Express Connect circuit to connect your data center to an access point of Apsara Stack. The Express Connect circuit is dedicated to you. To perform this operation, log on to the Express Connect console. For more information, see Create a connection over an Express Connect circuit.

### 5.2 Create a connection over an Express Connect circuit

**Express Connect circuit**

Before you create a connection over an Express Connect circuit, you must confirm the location of the access point, apply for an Express Connect circuit in the Express Connect console, and then create a virtual border router (VBR).

**Step 1: Confirm the access point**

An access point is where network services are provided and supports multiple types of connections between a data center and Apsara Stack. When you select an access point, take note of the elements such as the region, service provider, and port type. When you select an access point, you must confirm the Apsara Stack region that you want to access.

**Step 2: Apply for an Express Connect circuit**

1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, click **Apply for Physical Connection**.
4. On the **Create a physical line** page, configure the following parameters and click
**Submit**.

| Parameter | Description |
|---|---|
| Area |   |
| Organization | Select the organization to which the connection over the Express Connect circuit belongs. |

| Resource set | Select the resource group to which the connection over the Express Connect circuit belongs. |
|---|---|
| Region | Select the region in which you want to create a connection over the Express Connect circuit. |
| Basic configuration |   |
| Leased Line Name | Enter a name for the connection over the Express Connect circuit. |
| Description | Enter a description for the connection over the Express Connect circuit. |
| End position | Enter the address of the data center that you want to connect by using the Express Connect circuit. |
| Leased line configuration |   |
| Access point | Select an access point to connect to the data center. Access points are Apsara Stack data centers located in different regions. Each region provides one or more access points. The access points allow you to connect to Apsara Stack from different geographical locations and support different connection types. |
| Access port type | Select a port type. Valid values: 100 megabyte Port Gigabit Port Gigabit single mode optical port 10 Gigabit Port 10 Gigabit single mode optical port 40GE single mode optical port 100GE single mode optical port |
| Access equipment | Select the device to connect to the Express Connect circuit. |
| Physical Port | Enter a name for the port on the access device. |
| Dedicated line bandwidth | Enter a maximum bandwidth for the connection over the Express Connect circuit. Minimum value: 2. Unit: Mbit/s. You cannot enter a value higher than the limit specified by the port type. |

5. Return to the **Physical Connection** page. Verify that the connection is created and is in
the **Allocating Resources** state.

**Step 3: Enable the connection over the Express Connect circuit**

1. After resources are allocated, the connection enters the **Pending** state. Click **Enable**
**Connection** in the **Actions** column.
2. Refresh the **Physical Connection** page. The state of the connection changes to **Enabled**.

**Step 4: Create a VBR**

After the connection is enabled, you must create a VBR to forward network traffic between the data center and Apsara Stack.
1. Click the ID of the connection over the Express Connect circuit in the **Enabled** state.
2. On the details page of the connection over the Express Connect circuit, click the
**Connected VBRs** tab and then click **Create VBR**.
3. In the **Create VBR** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Basic Information |   |
| Account Type | Current Organization: creates a VBR for the current organization. Another Organization: creates a VBR for another organization. In this example, Current Organization is selected. |
| Organization | Select an organization for the VBR. |
| Resource Set | Select a resource set for the VBR. This parameter is required ifC urrent Organization is selected for the Account Type parameter. |
| Name | Enter a name for the VBR. This parameter is required if Current Organization is selected for the Account Type parameter. |
| Physical Connection Configurations |   |
| Physical Connection | Select an Express Connect circuit that is enabled and works as expected. |

| VLAN ID | Enter a VLAN ID for the VBR. Valid values: 0 to 2999. If the VLAN ID is set to 0, the switch port on the VBR is a Layer 3 router interface instead of a VLAN interface. When a Layer 3 router interface is used, each Express Connect circuit corresponds to one VBR. If the VLAN ID is set to a value from 1 to 2999, the switch port on the VBR is a Layer 3 VLAN subinterface. When a Layer 3 VLAN subinterface is used, each VLAN ID is associated with a VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to VPCs that belong to different Apsara Stack accounts. VBRs in different VLANs are isolated from each other at Layer 2. Important The VLAN ID that you specify for the VBR and that of the customer- premises device must be the same. |
|---|---|
| IPv4 Address of Gateway at Alibaba Cloud Side | Enter an IPv4 address for the gateway that is deployed on Apsara Stack. In this example, 192.168.101.5 is used. |
| IPv4 Address of Gateway at Customer Side | Enter an IPv4 address for the gateway that is deployed in the data center. In this example, 192.168.101.6 is used. |
| Subnet Mask (IPv4 Address) | Enter the subnet mask of the specified IPv4 addresses. In this example, 255.255.255.252 is used. You can enter a long subnet mask because only two IP addresses are required. |
| IPv6 Support | Specify whether to enable IPv6. Disable: disables IPv6. Enable: enables IPv6. The VPC can communicate with the data center over IPv6. |
| IPv6 Address of Gateway at Alibaba Cloud Side | Enter an IPv6 address for the gateway that is deployed on Apsara Stack. In this example, 2001:XXXX:3c4d:0015:0000:0000:0000:1a2b is used. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |

| IPv6 Address of Gateway at Customer Side | Enter an IPv6 address for the gateway that is deployed in the data center. In this example, 2001:XXXX:3c4d:0015:0000:0000:0000:2a2b is used. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
|---|---|
| Subnet Mask (IPv6 Address) | Enter the subnet mask of the specified IPv6 addresses. In this example, 2408:4004:cc:400::/56 is used. The two IPv6 addresses must fall within the same subnet. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |

4. When the VBR is in the **Active** state, run the **ping** command to check the connectivity
between the IP addresses of the gateways deployed on Apsara Stack and in the data center. After the VBR is created, you can view its information on the details page of the VBR.

**Step 5: Create a peering connection between the VBR and a**

**VPC**

After a connection over the Express Connect circuit is established between the data center and Apsara Stack, you must create a VBR-to-VPC peering connection between the VBR and a VPC. This way, the VPC can communicate with the data center over the private network.
1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **VBR-to-VPC**.
3. On the **VBR-to-VPC** page, click **Create Peering Connection**.
4. On the **Create a peer connection** page, configure the following parameters and click
**Submit**.

| Parameter | Description |
|---|---|
| Configuration on the VBR side |   |
| Organization | Select the organization to which the VBR belongs. |
| Resource Set | Select the resource group to which the VBR belongs. |
| Geography | Select the region in which the VBR resides. |
| Router Type | Use the default value Border Router for this parameter. |

| Access Point | Select an access point. |
|---|---|
| VBR | Select the ID of the VBR. |
| Router interface specifications | Select the interface specifications of the VBR. In this example, 1000 Mbps is selected. |
| Router Interface Name | Enter a name for the VBR interface. |
| Description | Enter a description. |
| VPC-side configuration |   |
| Organization | Select the organization to which the VPC belongs. Note If the VPC belongs to another organization, confirm with the organization. |
| Resource Set | Select the resource group to which the VPC belongs. |
| Geography | Select the region in which the VPC resides. |
| Availability Zone | Select a zone in the region to which the VPC belongs. |
| Router Type | Use the default value VPC router for this parameter. |
| VPC | Select a VPC. |
| Router Interface Name | Enter a name for the VPC router interface. |
| Description | Enter a description. |

| Health check source IP address | Enter the source IP address for health checks. Note The source IP address for health checks must be an idle IP address that belongs to the CIDR block of a vSwitch in the specified VPC. |
|---|---|
| Health check destination IP address | Enter the destination IP address for health checks. Note The destination IP address must be the IP address of the customer- premises device that is connected to the VBR by using an Express Connect circuit. |

**Related operations**

| Operation | Description |
|---|---|
| Find a connection over an Express Connect circuit | You can use one of the following methods to find the connection: On the Physical Connection page, click Tag Filter and configure the Tag Key and Tag Value parameters to filter the connections by tag. On the Physical Connection page, select Name or ID and enter a connection name or connection ID to perform a fuzzy match. |
| Modify the information of a connection over an Express Connect circuit | 1. On the Physical Connection page, click the ID of the connection that you want to manage to view the specifications, endpoint, and bandwidth of the connection as well as the VBRs connected to it. 2. Click Modify next to Basic Information. 3. In the Modify dialog box, modify the Name, Bandwidth, and Data Center Location parameters and click OK. You can also find the connection that you want to manage on the Physical Connection page, move the pointer over the icon below the connection ID, and then modify the connection name. |
| Add a VBR for a connection over an Express Connect circuit | 1. On the Physical Connection page, click the ID of the connection that you want to manage. 2. On the details page of the connection, click Create VBR. In the Create VBR dialog box, configure the parameters and click OK. |

| Modify the information of a VBR | 1. On the Physical Connection page, click the ID of the connection that you want to manage. 2. On the details page of the connection, click the Connected VBRs tab. 3. Find the VBR that you want to modify and clickM odify in the Actions column. 4. In the Modify VBR dialog box, modify the parameters and click OK. |
|---|---|
| Disable the connection to a VBR | You can disable the connection between a VBR and an Express Connect circuit. 1. On the Physical Connection page, find the connection that you want to manage and click its ID. 2. On the Connected VBRs tab, find the VBR that you want to manage. 3. Click Disable Connection in the Actions column. 4. In the Disable Connection message, click OK. |
| Cancel a connection over an Express Connect circuit | You can cancel a connection over an Express Connect circuit if the connection is not enabled. 1. On the Physical Connection page, find the connection that you want to manage. 2. Click Cancel Connection in the Actions column. 3. In the Cancel Connection message, click OK. |
| Disable a connection over an Express Connect circuit | You can disable a connection over an Express Connect circuit after the connection is enabled. 1. On the Physical Connection page, find the connection that you want to manage. 2. Click Disable Connection in the Actions column. 3. In the Disable Connection message, click OK. |

**References**

For more information about how to delete a connection over an Express Connect circuit, see Delete a connection over an Express Connect circuit.

### 5.3 Delete a connection over an Express Connect circuit

**Express Connect circuit**

This topic describes how to delete a connection over an Express Connect circuit.

**Background information**

To delete a connection over an Express Connect circuit, perform the following operations:
1. Delete the routes on the router of the virtual private cloud (VPC) and routes on the virtual
border router (VBR).
2. If Border Gateway Protocol (BGP) routing is configured, delete the BGP peers and BGP
groups.
3. Delete the peering connections.
4. Delete the associated VBRs.
5. Delete the connection over the Express Connect circuit.

**Step 1: Delete routes**

Delete routes of the VPC and the VBR.
1. To delete custom routes in a route table of a VPC, perform the following operations:
i. Log on to the VPC console. For more information, see **Log on to the VPC console** in
**VPC User Guide**.
ii. In the left-side navigation pane, click **Route Tables**. iii. In the top navigation bar, select the region to which the route table belongs. iv. On the **Route Tables** page, find the route table and click **Management** in the **Actions** column. v. On the **Routing Entry List** tab, find the custom route that you want to delete and click
**Delete** in the **Actions** column.
vi. In the **Delete Routing Entry** message, click **OK**.
2. For more information about how to delete a route of a VBR, see the "Delete a route" section
of the Add and manage routes topic.

**Step 2: Delete BGP peers and BGP groups**

If BGP routing is configured, you must delete the BGP settings. For more information, see the "Delete a BGP peer and a BGP group" section of the Configure and manage BGP topic.

**Step 3: Delete the peering connections**

Delete the peering connection between the VPC and the VBR. For more information, see the "Manage a VBR-to-VPC connection" section of the Create and manage a VBR-to-VPC connection topic.

**Step 4: Delete the associated VBRs**

Delete the associated VBRs. For more information, see the "Delete a VBR" section of the Create and manage VBRs topic.

**Step 5: Delete the connection over the Express Connect circuit**

2. In the left-side navigation pane, click **Physical Connection**.
3. On the **Physical Connection** page, find the connection that you want to disable and click
**Disable Connection** in the **Actions** column.
4. In the **Disable Connection** message, click **OK**.
5. On the **Physical Connection** page, find the connection that you want to delete and click
**Delete** in the **Actions** column.
6. In the **Delete** message, click **OK**.

## 6 VBRs

### 6.1 VBRs

Virtual border routers (VBRs) are an abstraction of Express Connect circuits that are isolated and virtualized by using the Layer 3 overlay and vSwitch technologies in the Software Defined Network (SDN) architecture. A VBR is deployed between the customer-premises equipment (CPE) and a virtual private cloud (VPC) and is used to exchange data between the VPC and data center.

> **Note:** Similar to VPC routers, each VBR manages a route table. You can add routes to the route table of a VBR to control network traffic forwarding.

**Features**

A VBR provides the following features: Exchanges data between a VPC and a data center. Determines the type of virtual interface of an Express Connect circuit: Layer 3 router interface or Layer 3 Virtual Local Area Network (VLAN) subinterface. Adds or identifies VLAN tags if a Layer 3 VLAN subinterface is used. Supports Border Gateway Protocol (BGP) routing. BGP is a dynamic routing protocol based on Transmission Control Protocol (TCP). BGP is used to exchange routing and network accessibility information across autonomous systems. When you create a connection over an Express Connect circuit, you can configure BGP routing between your data center and the associated VBR. This way, the data center and the VBR can communicate with each other through a private connection. This helps you to set up a hybrid cloud with higher efficiency, flexibility, and security. VBRs support BGP dynamic routing in both IPv4 and IPv6 networks.

**Limits**

VBRs do not support source address-specific policy-based routes. Each VBR has one and only one route table. VBRs support only BGP-4. You can create at most eight BGP peers for each VBR. Each BGP peer supports at most 110 dynamic routes. Routes are denied when the upper limit is exceeded. To configure BGP when you connect to a VPC, you must specify an Autonomous System Number (ASN) for the VPC. The ASN that you specify must be different from the ASNs of the vSwitches in the VPC.

### 6.2 Create and manage a VBR

After you enable an Express Connect circuit, you must create a virtual border router (VBR) for the Express Connect circuit. The VBR is used as a bridge to forward data from a virtual private cloud (VPC) to a data center. This topic describes how to create and manage a VBR.

**Background information**

A VBR is a router that is deployed between a VPC and the customer-premises equipment (CPE) in a data center. Each VBR is associated with a route table. To manage traffic forwarding on a VBR, you can add routes to the route table that is associated with the VBR. A VBR provides the following features: Exchanges data between a VPC and a data center. Determines the type of virtual interface of an Express Connect circuit: Layer 3 router interface or Layer 3 Virtual Local Area Network (VLAN) subinterface. Adds or identifies VLAN tags if a Layer 3 VLAN subinterface is used. Supports Border Gateway Protocol (BGP) routing. BGP is a dynamic routing protocol based on Transmission Control Protocol (TCP). BGP is used to exchange routing and network accessibility information across autonomous systems. When you create a connection over an Express Connect circuit, you can configure BGP routing between your data center and the associated VBR. This way, the data center and the VBR can communicate with each other through a private connection. This helps you to set up a hybrid cloud with higher efficiency, flexibility, and security. VBRs support BGP dynamic routing in both IPv4 and IPv6 networks.

**Create a VBR**

1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, click **Create VBR**.
4. In the **Create VBR** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Basic Information |   |
| Account Type | Current Organization: creates a VBR for the current organization. Another Organization: creates a VBR for another organization. In this example, Current Organization is selected. |
| Organization | Select an organization for the VBR. |
| Resource Set | Select a resource set for the VBR. This parameter is required ifC urrent Organization is selected for the Account Type parameter. |
| Name | Enter a name for the VBR. This parameter is required if Current Organization is selected for the Account Type parameter. |
| Physical Connection Configurations |   |
| Physical Connection | Select an Express Connect circuit that is enabled and works as expected. |

| VLAN ID | Enter a VLAN ID for the VBR. Valid values: 0 to 2999. If the VLAN ID is set to 0, the switch port on the VBR is a Layer 3 router interface instead of a VLAN interface. When a Layer 3 router interface is used, each Express Connect circuit corresponds to one VBR. If the VLAN ID is set to a value from 1 to 2999, the switch port on the VBR is a Layer 3 VLAN subinterface. When a Layer 3 VLAN subinterface is used, each VLAN ID is associated with a VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to VPCs that belong to different Apsara Stack accounts. VBRs in different VLANs are isolated from each other at Layer 2. Important The VLAN ID that you specify for the VBR and that of the customer- premises device must be the same. |
|---|---|
| IPv4 Address of Gateway at Alibaba Cloud Side | Enter an IPv4 address for the gateway that is deployed on Apsara Stack. In this example, 192.168.101.5 is used. |
| IPv4 Address of Gateway at Customer Side | Enter an IPv4 address for the gateway that is deployed in the data center. In this example, 192.168.101.6 is used. |
| Subnet Mask (IPv4 Address) | Enter the subnet mask of the specified IPv4 addresses. In this example, 255.255.255.252 is used. You can enter a long subnet mask because only two IP addresses are required. |
| IPv6 Support | Specify whether to enable IPv6. Disable: disables IPv6. Enable: enables IPv6. The VPC can communicate with the data center over IPv6. |
| IPv6 Address of Gateway at Alibaba Cloud Side | Enter an IPv6 address for the gateway that is deployed on Apsara Stack. In this example, 2001:XXXX:3c4d:0015:0000:0000:0000:1a2b is used. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
| IPv6 Address of Gateway at Customer Side | Enter an IPv6 address for the gateway that is deployed in the data center. In this example, 2001:XXXX:3c4d:0015:0000:0000:0000:2a2b is used. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |

| Subnet Mask (IPv6 Address) | Enter the subnet mask of the specified IPv6 addresses. In this example, 2408:4004:cc:400::/56 is used. The two IPv6 addresses must fall within the same subnet. Note This parameter is required if Enable is selected for the IPv6 Support parameter. |
|---|---|

**Delete a VBR**

Before you delete a VBR, you must delete the Border Gateway Protocol (BGP) groups, BGP peers, and BGP routes that are configured on the VBR. For more information, see Delete BGP peers and BGP groups and Delete routes.
1. Log on to the Express Connect console.
2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, find the VBR that you want to delete and click **Delete** in the **Actions**
column.
4. In the **Delete** message, click **OK**.

**Related operations**

| Operation | Description |
|---|---|
| Find the VBR that you want to manage | You can use one of the following methods to find the VBR: On the VBRs page, click Tag Filter and configure the Tag Key and Tag Value parameters to filter the VBRs by tag. On the VBRs page, select Name, ID, or Physical Connection and enter relevant information to perform a fuzzy match. |
| View the details of a VBR | On the VBRs page, find the VBR that you want to view and click its ID to view the endpoint, status, and routes of the VBR. |
| Add an Express Connect circuit | 1. On the VBRs page, find the VBR that you want to manage and click its ID. 2. On the details page of the VBR, click the Physical Connection tab and then click Add Physical Connection. 3. In the Add Physical Connection dialog box, configure the parameters and click OK. |

| Attach a VBR to a CEN instance across accounts | You can attach a VBR to a Cloud Enterprise Network (CEN) instance across accounts. 1. On the VBRs page, find the VBR that you want to manage and click its ID. 2. On the details page of the VBR, click the CEN Cross-Account Authorization tab and then click Authorize Cross Account Attach CEN. 3. In the Authorize Cross Account Attach CEN dialog box, configure the Peer Level-1 Organization UID and Peer CEN Instance ID parameters and click OK. |
|---|---|
| Modify the name of a VBR | 1. On the VBRs page, find the VBR that you want to manage and move the pointer over the icon below the VBR ID. 2. In the Rename dialog box, enter a name for the VBR and click OK. |
| Modify a VBR | 1. On the VBRs page, find the VBR that you want to modify and click Modify in the Actions column. 2. In the Modify VBR dialog box, modify the parameters and click OK. |

**References**

You can configure BGP routes between a data center and a VBR. For more information, see Configure BGP. You can add routes to the route table of a VBR to manage traffic forwarding on the VBR. For more information, see Add routes You can create a VBR-to-VPC peering connection to enable communication between a VBR and a VPC. For more information, see Create and manage a VBR-to-VPC connection.

### 6.3 Configure and manage BGP

You can configure Border Gateway Protocol (BGP) routing to enable communication between a data center and a virtual border router (VBR). You must add the BGP peer that communicates with the VBR to a BGP group, and then advertise the BGP CIDR block on the VBR. This topic describes how to configure and manage BGP.

**Background information**

BGP is a dynamic routing protocol based on TCP. BGP is used to exchange routing information and network accessibility information in different autonomous systems. If you use an Express Connect circuit to connect to Apsara Stack, you can configure BGP routing to enable communication between your data center and the virtual border router (VBR) that is associated with the Express Connect circuit. BGP allows you to build hybrid clouds in a more efficient, flexible, and reliable way. Before you configure BGP routing, you must create a BGP group. BGP groups are used to simplify BGP configurations. You can add BGP peers with the same configurations to one BGP group. You need to only create a BGP group with an autonomous system number (ASN) and add BGP peers that meet your requirements to the BGP group. After you add the BGP peers to the BGP group, the BGP peers share the configurations of the BGP group. You do not need to configure each BGP peer separately.

**Limits**

Before you configure BGP routing, take note of the following limits: You can specify only the data center as the BGP peer of a VBR. The data center is connected to the VBR by using an Express Connect circuit. Static routing is required between a VBR and a virtual private cloud (VPC). VBRs support only BGP-4. You can create up to eight BGP peers for each VBR. Each BGP peer supports up to 110 dynamic routes. Routes are denied when the upper limit is exceeded. To configure BGP routing when you connect to a VPC, you must specify an ASN for the VPC. The ASN that you specify must be different from the ASNs of the vSwitches in the VPC.

**Configure BGP**

**Step 1: Create a BGP group**

Before you configure BGP routing, you must create a BGP group with the requested ASN.
2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, find the VBR that you want to manage and click its ID.
4. On the details page of the VBR, click the **BGP Groups** tab. Then, click **Create BGP Group**.
5. In the **Create BGP Group** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| IPv6 Support | Specify whether to enable IPv6. Yes: enables IPv6. After you enable IPv6, the endpoints of VPC and your data center can be IPv6 addresses. No: disables IPv6. |
| Name | The name of the BGP group. |
| Peer ASN | The ASN of the data center. |
| BGP Key | The key of the BGP group. |
| Description | The description of the BGP group. |
| Local ASN | The local ASN. |

**Step 2: Create a BGP peer**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, find the VBR that you want to manage and click its ID.
4. On the details page of the VBR, click the **BGP Peers** tab. Then, click **Create BGP Peer**.
5. In the **Create BGP Peer** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| BGP Group | The BGP group to which you want to add the BGP peer. |
| BGP Peer IP Address | The IP address of the BGP peer. |

**Step 3: Advertise the BGP CIDR block**

After you create the BGP peer, you must advertise the CIDR block of the VPC. After the BGP session is established, the VBR automatically learns the CIDR block of the data center.
2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, find the VBR that you want to manage and click its ID.
4. On the details page of the VBR, click the **BGP CIDR Blocks** tab. Then, click **Advertise BGP**
**CIDR Block**.
5. In the **Advertise BGP CIDR Block** dialog box, enter the CIDR block that you want to
advertise and click **OK**.

**Delete a BGP peer and a BGP group**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, select the region in which the VBR that you want to manage resides
and click its ID.
4. On the details page of the VBR, click the **BGP Peers** tab, find the BGP peer that you want to
delete, and then click Delete in the Actions column.
5. On the details page of the VBR, click the **BGP Groups** tab, find the BGP group that you
want to delete, and then click Delete in the Actions column.
6. On the details page of the VBR, click the **BGP CIDR Blocks** tab, find the BGP CIDR block
that you want to delete, and then click Delete in the Actions column.

**More operations**

| Operation | Description |
|---|---|
| Modify a BGP peer | 1. On the VBRs page, find the VBR that you want to manage and click its ID. 2. On the details page of the VBR, click the BGP Peers tab, find the BGP peer that you want to modify, and then click Modify in the Actions column. 3. In the Modify BGP Peer dialog box, enter the IP address of the BGP peer and click OK. |

| Modify a BGP group | 1. On the VBRs page, find the VBR that you want to manage and click its ID. 2. On the details page of the VBR, click the BGP Groups tab, find the BGP group that you want to modify, and then click Modify in the Actions column. 3. In the Modify BGP Group dialog box, enter the BGP group information and click OK. |
|---|---|

### 6.4 Add and manage routes

You can add routes to the route table of a virtual border router (VBR) to manage where network traffic is forwarded. This topic describes how to add and manage routes.

**Background information**

You must add a route that points to the associated Express Connect circuit and a route that points to the virtual private cloud (VPC). This way, network traffic can be forwarded between the VPC and the data center. You can also configure Border Gateway Protocol (BGP) routing for a VBR. For more information, see Configure and manage BGP.

**Add a route**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, find the VBR that you want to manage and click its ID.
4. On the details page of the VBR, click the **Route Entries** tab. Then, click **Add Route Entry**.
5. In the **Add Route Entry** dialog box, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Next Hop Type | The type of next hop. Valid values: VPC: The VBR routes network traffic to a VPC. Physical Connection: The VBR routes network traffic to an Express Connect circuit. |
| Destination CIDR Block | The destination CIDR block. |
| Next Hop | The next hop. |

**Delete a route**

2. In the left-side navigation pane, click **Virtual Border Router**.
3. On the **VBRs** page, select the region in which the VBR that you want to manage resides
and click its ID.
4. On the details page of the VBR, click the **Route Entries** tab, find the route that you want to
delete, and then click **Delete** in the **Actions** column.
5. In the **Delete** message, click **OK**.

### 6.5 Create a peering connection

This topic describes how to create a peering connection. After you create a virtual border router (VBR), you must create a peering connection between the VBR and a virtual private cloud (VPC). This way, the VBR can route traffic between the VPC and the data center that is connected to the VBR. For more information about how to create a peering connection, see Create and manage a VBR-to-VPC connection.

## 7 Manage tags

Express Connect allows you to search for and filter resources by tag. You can use tags to mark and classify the following resources: virtual border routers (VBRs), VPC-to-VPC connections, VBR-to-VPC connections, and connections over Express Connect circuits.

**Add a tag**

1. Log on to the Express Connect console.
2. Select the region in which your resources reside.
3. In the left-side navigation pane, click the menu item corresponding to the type of the
resources that you want to manage.
4. On the page of the selected resource type, add a tag to one or more resources.
Add a tag to a single resource a. Find the resource that you want to manage, move the pointer over **-** in the **Tag** column or the right of an existing tag, and then click the icon. b. In the **Edit Tags** dialog box, click **Add**, specify the tag key and tag value, and then click **OK**.

| Parameter | Description |
|---|---|
| Tag Key | Select or enter a tag key. The tag key can be up to 64 characters in length and cannot start with aliyun or acs: . The tag key cannot contain http:// or https:// . |
| Tag Value | Select or enter a tag value. The tag value can be up to 128 characters in length and cannot start with aliyun or acs: . The tag value cannot contain http:// or https:// . |

Add a tag to multiple resources a. Select the resources to which you want to add a tag and click **Batch Add Tags** in the lower-left corner. b. In the **Batch Add Tags** dialog box, configure the **Tag Key** and **Tag Value** parameters and click OK.
5. Return to the page of the selected resource type, and click **Tag Filter**. In the dialog box
that appears, specify the tag key and tag value to filter resources.

**Remove a tag**

1. Log on to the Express Connect console.
2. Select the region in which your resources reside.
3. In the left-side navigation pane, click the menu item corresponding to the type of the
resources that you want to manage.
4. On the page of the selected resource type, remove a tag from one or more resources.
Remove a tag from an single resource a. Find the resource that you want to manage and click the icon in the **Tag** column. b. In the **Edit Tags** dialog box, find the tag-value pair that you want to remove, click the Delete icon on the right, and then click **OK**. Remove a tag from multiple resources a. Select the resources from which you want to remove a tag and click **Batch Remove**
**Tags** in the lower-left corner.
b. In the **Batch Remove Tags** dialog box, find the tag-value pair that you want to remove, click the Delete icon on the right, and then click **OK**. gs

## 8 Manage operation logs

Operation logs record the operations of **users or systems** and the data that is changed. Operation logs allow you to easily and clearly view the operation records of accounts and the data on which the operations are performed. Operation logs can be used to support operational analysis of business and provide the basis to protect data security. You can view operation logs of connections over Express Connect circuits and virtual border routers (VBRs).

**Search for operation logs and view log details**

1. Log on to the Express Connect console.
2. Select the region in which your resources reside.
3. Select the resources that you want to manage.
Connection over an Express Connect circuit a. In the left-side navigation pane, click **Physical Connection**. On the **Physical**
**Connection** page, find the connection over an Express Connect circuit that you want
to manage and click its ID. b. On the details page of the connection, click the **Operation Log** tab. VBR a. In the left-side navigation pane, click **Virtual Border Router**. On the **VBRs** page, find the VBR that you want to manage and click its ID. b. On the details page of the VBR, click the **Operation Log** tab.
4. Click **Advanced Filter**, enter the filter conditions based on your business requirements,
and then click **Search** to search for operation records. Operator: the account for which the operation records are generated. After you specify this parameter, you can query the operation records of the specified account. Operation Time: the time when the operation record is generated. Operation Name: the name of the API operation that is called during the operation. Execution status: the execution result of the operation, which can be success or failure. Operation Source IP: the IP address of the operation source. Operation Source: the source of the operation, which can be operation in the console or API call. Operation Type: the type of the operation, which can be read or write.
5. Click **View Details** in the **Operation** column of an operation record to view the log details.
