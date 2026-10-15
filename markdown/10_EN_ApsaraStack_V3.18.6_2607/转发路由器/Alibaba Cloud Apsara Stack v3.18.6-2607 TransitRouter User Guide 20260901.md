---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 TransitRouter User Guide 20260901"
product_version: "V3.18.6_2607"
doc_version: "20260901"
pdf_pages: 59
source_pdf: "667f647052e3edcd_Alibaba Cloud Apsara Stack v3.18.6-2607 TransitRouter User Guide 20260901.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%BD%AC%E5%8F%91%E8%B7%AF%E7%94%B1%E5%99%A8/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20TransitRouter%20User%20Guide%2020260901.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 TransitRouter User Guide 20260901

## Table of Contents

- 1 Log on to the Transit Router console
- 2 Instance management
  - 2.1 Create and manage a CEN instance
  - 2.2 Manage transit routers
    - 2.2.1 Transit routers
    - 2.2.2 Intra-region connections
      - 2.2.2.1 Create a VPC connection
      - 2.2.2.2 Create a VBR connection
      - 2.2.2.3 Create a Connect attachment
      - 2.2.2.4 View network instance connections
    - 2.2.3 Route management
      - 2.2.3.1 Custom route tables
      - 2.2.3.2 Custom route entries
      - 2.2.3.3 Associated forwarding
      - 2.2.3.4 Route learning
      - 2.2.3.5 Routing policies
        - 2.2.3.5.1 Routing policy overview
        - 2.2.3.5.2 Work with routing policies
    - 2.2.4 Multicast management
      - 2.2.4.1 Multicast overview
      - 2.2.4.2 Create and manage a multicast domain
      - 2.2.4.3 Manage vSwitches
      - 2.2.4.4 Multicast group
  - 2.3 Tag management
- 3 Configure health checks
- 4 View operation logs

Router console

## 1 Log on to the Transit Router console

**Router console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

First logon The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % Forget password If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform operations based
on your logon scenarios: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA verification code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the six-digit MFA verification code and click **Authenticate**.

**Note**

For information about how to bind and enable MFA, see **Manage MFA** in **Apsara**
**Uni-manager Management Console User Guide**.
Inthetopnavigationbarchoose **Products****>****Networking****>****CEN** Router console
5. In the top navigation bar, choose **Products > Networking > CEN**.

## 2 Instance management

### 2.1 Create and manage a CEN instance

**instance**

Cloud Enterprise Network (CEN) instances are basic network resources that are used to manage interconnected networks. A CEN instance can be used to manage a network. Before you can connect networks, you must create a CEN instance.

**Create a CEN instance**

1. Log in to the CEN console.
2. In the top navigation bar, select the region in which the CEN instance resides.
3. In the left-side navigation pane, click **CEN Instance**.
4. On the **Cen instance** page, click **Create a CEN instance**.
5. On the **Create a CEN instance** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization in which you want to create the CEN instance. |
| Resource Set | Select a resource set for the CEN instance. |
| Cloud Enterprise Network Name | Enter a name for the CEN instance. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). It must start with a letter. _ |
| Description | Enter a description for the CEN instance. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://. |

**What to do next**

**View CEN instances**

On the **CEN Instance** page, you can click the ID of a CEN instance to view its information.

**Note**

Up to 100 pages of entries can be displayed in the list, and up to 100 entries can be displayed on each page. If more than 10,000 entries exist, specify filter conditions to filter the entries. Enter a keyword or specify **advanced filter conditions** to search for a specific CEN instance. Click the icon in the upper-right corner of the list to specify the columns that you want to display in the list. You can also drag and drop the items to adjust their order. Click the icon next to the name in the **Cen ID/name** column to modify the name of a CEN instance. Click the icon next to the description in the **Description** column to modify the description of a CEN instance. Click the number in the **Forwarding router** column to manage the transfer routers connected to a CEN instance.

**Manage tags**

On the **CEN Instance** page, you can add tags to CEN instances to mark and group the CEN instances. For more information, see Tag management.

**Delete CEN instances**

**Note**

Before you delete a CEN instance, make sure that the following prerequisites are met: No network instance is attached to the CEN instance. For more information, see Delete a network instance connection. No custom route tables exist on the transit router. For more information, see Delete a custom route table. The transit router is not associated with a multicast domain. For more information, see Delete a multicast domain.
1. On the **CEN Instance** page, find the CEN instance that you want to delete and click **Delete**
in the **Actions** column.
2. In the **Delete a CEN instance** message, check the CEN instance ID and click **OK**.

**Manage CEN instances**

1. On the **Cen instance** page, find the CEN instance that you want to manage and click its ID
in the **Cen ID/name** column.
2. On the **CEN Instance** page, you can manage your CEN instances.
Click the **Basic information** tab to view and manage the basic information about the CEN instance and transit routers. In the **Basic information** section, find the **Instance name** parameter, move the pointer over the parameter value, and then click the icon to modify the name of the CEN instance. In the **Basic information** section, find the **Description** parameter, move the pointer over the parameter value, and then click the icon to modify the description of the CEN instance. In the list below the **Basic information** section, you can manage the transit routers of the CEN instance. For more information, see Manage transit routers. Click the **Resource topology** tab to view the resource topology of the CEN instance.

### 2.2 Manage transit routers

#### 2.2.1 Transit routers

You can create one transit router in each region. A transit router is a key network element that is used to forward data within a region.

**Background information**

Transit routers are deployed on Cloud Enterprise Network (CEN) instances. Before you can create a transit router, you must create a CEN instance. Then, you can create a transit router in the region of the CEN instance. A CEN instance manages a network. To connect networks, you must attach the networks to the transit router of the same CEN instance. You can create multiple CEN instances. By default, the network instances attached to different CEN instances are isolated from each other.

**Create a transit router**

1. Log on to the Transit Router console.
2. On the **CEN Instance** page, click **Create a CEN instance**.
3. On the **Create a CEN instance** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | Select an organization in which you want to create the CEN instance. |
| Resource Set | Select a resource set for the CEN instance. |
| Cloud Enterprise Network Name | Enter a name for the CEN instance. |
| Description | Enter a description for the CEN instance. |

4. After you create the CEN instance, select the organization and resource set of the CEN
instance from the top navigation bar. On the **CEN Instance** page, click the ID of the CEN instance.
5. On the details page of the CEN instance, click the **Basic information** tab and click **Create**
**a transit router**.
6. On the **Create Transit Router** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Parameter | Description |
|---|---|

| Organization | Select the organization in which you want to create the transit router. |
|---|---|
| Resource Set | Select a resource set for the transit router. |
| Region | Select the region in which you want to create the transit router. |
| Edition | The edition of the transit router is displayed. Valid value: Enterprise Edition. |
| Name | Enter a name for the transit router. |
| Description | Enter a description for the transit router. |
| Transit Router CIDR | Click Add to add a CIDR block to the transit router. You can specify a custom CIDR block. The CIDR block works in a similar way as the CIDR block of the loopback interface on a router. IP addresses within the CIDR blocks can be allocated to Connect peers. For more information, see Transit router CIDR blocks. |

**Delete a transit router**

You can delete transit routers that you no longer use. Before you delete a transit router, make sure that the following requirements are met: No network instance connections are created on the transit router. For more information, see Delete a network instance connection. The transit router does not contain custom route tables. For more information, see Delete a custom route table. The default route table of the transit router does not contain custom route entries. For more information, see Delete a custom route from a route table of a transit router. The transit router is not associated with a multicast domain. For more information, see Delete a multicast domain.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab, find the transit
router that you want to delete, and then click **Delete** in the **Actions** column.
5. In the **Delete a forwarding router** message, check the transit router ID and click **OK**.

**Delete a CEN instance**

If you no longer use a transit router, you can delete the CEN instance along with the transit router. Before you delete a CEN instance, make sure that the following requirements are met: No network instance connections are created on the transit router. For more information, see Delete a network instance connection. The transit router does not contain custom route tables. For more information, see Delete a custom route table. The default route table of the transit router does not contain custom route entries. For more information, see Delete a custom route from a route table of a transit router. The transit router is not associated with a multicast domain. For more information, see Delete a multicast domain.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, find the CEN instance that you want to delete and click **Delete**
in the **Actions** column.
4. In the **Delete a CEN instance** message, check the CEN instance ID and click **OK**.

#### 2.2.2 Intra-region connections

##### 2.2.2.1 Create a VPC connection

You can connect virtual private clouds (VPCs) to a transit router. After you connect the VPCs to the same transit router, the VPCs can communicate with each other.

**Prerequisites**

The VPC of the transit router has sufficient vSwitches. Each vSwitch has at least one idle IP address. For more information about how to create vSwitches, see **VPCs and vSwitches >**
**Manage vSwitches > Create a vSwitch** in VPC User Guide.

| If you create a VPC connection on a transit router in a region that supports only one zone, |   |
|---|---|
| make sure that the VPC has at least one vSwitch in the zone. The vSwitch must have at |   |
| least one idle IP address. When you create a VPC connection, the transit router creates an |   |
| elastic network interface (NIC) in the vSwitch of the VPC. The vSwitch occupies one IP |   |
| address in the vSwitch and forwards traffic between the VPC and the transit router. |   |

| If you create a VPC connection on a transit router in a region that supports multiple |   |
|---|---|
| zones, make sure that the VPC has at least two vSwitches that are deployed in different |   |
| zones. Each vSwitch must have at least one idle IP address. When you create a VPC |   |
| connection, the transit router creates an ENI in each vSwitch of the VPC. Each ENI |   |
| occupies one IP address in the vSwitch and forwards traffic between the VPC and the |   |
| transit router. The two vSwitches support zone-disaster recovery to ensure uninterrupted |   |
| data transmission between the VPC and the transit router. |   |

You can connect a transit router to a VPC that belongs to the same or a different organization. Before you can connect a VPC to a transit router that belongs to a different organization, the CEN instance to which the transit router belongs must obtain required permissions from the VPC. For more information, see Grant a transit router permissions on a network instance that belongs to another Alibaba Cloud account.

**Create a VPC connection**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab, find the transit
router that you want to manage, and then click **Create a network instance connection** in the **Actions** column.
5. On the **Create Connection** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | Select the organization of the transit router. |
| Resource Set | Select the resource set of the transit router. |
| Region | Select the region of the transit router. |
| Network type | Select VPC. |
| Transit Router | The transit router in the selected region is automatically displayed. |
| Organization | Select the organization of the network instance. |
| Resource Set | Select the resource set of the network instance. |
| Owner Account | The Apsara Stack tenant account to which the network instance belongs is automatically displayed. |
| Connection Name | Enter a name for the VPC connection. |
| Network Instance | Select the VPC that you want to connect to the transit router. |
| vSwitch | Select a vSwitch. If the region supports only one zone, select a vSwitch in the current zone. If the region supports multiple zones, select a vSwitch in at least two zones. When the VPC and transit router communicate, the vSwitches are used to implement zone- disaster recovery. We recommend that you select a vSwitch in each zone to reduce network latency and improve network performance because data can be transmitted over a shorter distance. |

| Advanced Settings | VPC supports the following advanced features. If you enable the advanced settings, the system automatically configures required routes. Associate with Default Route Table of Transit Router After this feature is enabled, the VPC connection is automatically associated with the default route table of the transit router. The transit router forwards the traffic of the VPC based on the default route table. Propagate System Routes to Default Route Table of Transit Router After this feature is enabled, the system routes of the VPC are advertised to the default route table of the transit router. This way, the VPC can communicate with other network instances that are connected to the transit router. Automatically Creates Route That Points to Transit Router and Adds to All Route Tables of Current VPC After this feature is enabled, the system automatically adds the following routes to all route tables of the VPC: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. The routes point to the VPC connection. You can disable the advanced features by clearing the check boxes. If you want to enable the VPC to communicate with other network instances, you can configure associated forwarding and route learning on the transit router. For more information, see Route management. |
|---|---|

After the VPC connection is created, you can view the details about the connection on the
**Intra-region connection management** tab. For more information, see View network
instance connections.

**Change the vSwitches of the VPC connection**

After you create a VPC connection, you can change the vSwitches of the VPC connection. Before you begin, make sure that no routes of the VPC point to the ENI of a transit router. For more information about how to delete a VPC route, see **Route tables > Delete a custom**
**route entry** in VPC User Guide.

**Warning**

If you change the vSwitch of a VPC connection, the connection may be interrupted for up to 15 seconds. Proceed with caution.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Intra-region connection management**
tab and click the ID of the VPC connection that you want to manage.
6. In the **Connection details** panel, click **Edit zone/Subnet** in the **Associate network**
**instances** section.
7. In the **Edit zone/Subnet** dialog box, select a vSwitch from the **Select zone/Subnet** drop-
down list and click **OK**.

##### 2.2.2.2 Create a VBR connection

This topic describes how to establish communication between virtual border routers (VBRs) by connecting them to the transit router of Cloud Enterprise Network (CEN) in the same region. The transit router allows you to access cloud resources over private connections.

**Procedure**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab, find the transit
router that you want to manage, and then click **Create a network instance connection** in the **Actions** column.
5. On the **Create Connection** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | Select the organization of the transit router. |
| Resource Set | Select the resource set of the transit router. |
| Region | Select the region of the transit router. |
| Instance Type | Select Virtual Border Router (VBR). |
| Transit Router | The transit router in the current region is automatically displayed. |
| Organization | Select the organization of the network instance. |
| Resource Set | Select the resource set of the network instance. |
| Owner Account | The Apsara Stack tenant account to which the network instance belongs is automatically displayed. |
| Connection Name | Enter a name for the VBR connection. |
| VBR | Select the ID of the VBR. |

| Advanced VBR Settings | VBRs support the following advanced features. If you enable the advanced settings, the system automatically configures required routes. Associate with Default Route Table of Transit Router After this feature is enabled, the VBR connection is automatically associated with the default route table of the transit router. The transit router forwards the traffic of the VBR based on the default route table. Propagate System Routes to Default Route Table of Transit Router After this feature is enabled, the system routes of the VBR are automatically advertised to the default route table of the transit router. Propagate Routes to VBR After this feature is enabled, the system automatically advertises the routes in the route table that is associated with the VBR connection to the VBR. You can disable the advanced features by clearing the check boxes. If you want to enable the VBR to communicate with other network instances, you can configure associated forwarding and route learning on the transit router. For more information, see Route management. |
|---|---|

##### 2.2.2.3 Create a Connect attachment

A Connect attachment connects a transit router to a third-party device, such as an SD-WAN device. Connect attachments simplify the process of cloud adoption. You can connect networks to Alibaba Cloud after simple configurations.

**Background information**

**Terms**

The following table describes the terms of Connect attachments.

| Term | Description |
|---|---|
| Connect attachment | A Connect attachment connects a transit router to a third-party device, such as an SD-WAN device. Connect attachments simplify the process of cloud adoption. You can connect networks to Alibaba Cloud after simple configurations. |
| Transport attachment type | The type of transport channel. The system creates a Connect attachment between a transit router and an on-premises network by creating a network tunnel on the transport channel. Connect attachments are a type of network tunnel. Each Connect attachment supports multiple network tunnels. The type of transport channel supported by the system isA llvbr. You can create a Connect attachment between a transit router and an on-premises network by using the virtual border router (VBR) in the region. |

| GRE | Generic routing encapsulation (GRE) is a protocol that encapsulates packets that are transmitted over the tunnel. |
|---|---|
| Connect peer | Connect peers are the entities that are connected to transit routers by Connect attachments. Each Connect peer specifies a network tunnel. Each Connect attachment contains two entities: the transit router and the Connect peer. |
| Peer | A peer is the entity that is connected to a transit router over a network tunnel. Each peer is identified by its IP address. |
| Transit route local address | The local address of a transit router. A transit router uses its local address to create a network tunnel and is also identified by its local address during tunneling. The local address of a transit router is allocated from the CIDR block of the transit router. For more information, see Transit router CIDR blocks. |
| Peer address | A peer uses its address to create a network tunnel and is also identified by its address during tunneling. |

**Network topology**

The system creates a Connect attachment between a transit router and an on-premises network by creating a network tunnel on the transport channel. Connect attachments support only VBR connections between transit routers and on-premises networks. The following figure shows the network topology.

**Routes**

The system creates a Connect attachment between a transit router and an on-premises network based on the VBR connections. Therefore, the system creates a virtual route table that is not displayed in the console. The virtual route table contains the routes that are learned by all the VBRs in the region from the on-premises network. Then, the transit router queries the virtual route table and the network tunnel before the transit router forwards network traffic from Alibaba Cloud to the on-premises network. For network traffic that goes from the on-premises network to Alibaba Cloud, the system queries the route table of the VBR and the route table that is associated with the VBR connection when network traffic reaches the Express Connect circuit. Then, network traffic is forwarded to the destination cloud resource. If the transit router is connected to multiple VBRs and the VBRs learn the same routes from the on-premises network, the virtual route table contains routes that have the same destination CIDR block but different next hops. Equal-cost multi-path (ECMP) routing is automatically enabled based on the routes.

**Important**

In a scenario where the transit router is connected to multiple VBRs (active/standby Express Connect circuits are deployed): If the VBRs and the on-premises network use BGP dynamic routing, and one of the Express Connect circuits fails, network traffic is automatically switched to a healthy Express Connect circuit. If the VBRs and the on-premises network use static routes, health checks are enabled for the VBRs, and one of the Express Connect circuits fails, network traffic is automatically switched to a healthy Express Connect circuit. If the VBRs and the on-premises network use static routes, health checks are disabled for the VBRs, and one of the Express Connect circuits fails, network traffic is still forwarded to the faulty Express Connect circuits because the system cannot detect Express Connect errors. In this case, your services may be interrupted.

**Limits**

Connect attachments can forward only multicast packets. Unicast packets cannot be forwarded by Connect attachments. Each Connect attachment supports at most four Connect peers. Connect attachments do not support associated forwarding or route learning.

**Prerequisites**

A transit router is deployed in the region where you want to create a Connect attachment, multicast is enabled for the transit router, and a CIDR block is assigned to the transit router. For more information, see Create a transit router. The on-premises network is connected to the transit router through a VBR, and can communicate with other networks that are also connected to the transit router. For more information, see Create a VBR connection and Create a VPC connection.

**Step 1: Create a Connect attachment**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab, find the transit
router that you want to manage, and then click **Create a network instance connection** in the **Actions** column.
5. On the **Create Connection** page, configure the parameters and click **Submit**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Organization | Select the organization of the transit router. |
| Resource Set | Select the resource set of the transit router. |
| Region | Select the region of the transit router. |
| Instance Type | Select Connect |
| Transit Router | The transit router in the current region is automatically displayed. |
| Connection Name | Enter a name for the Connect attachment. |
| Protocol Type | Select the protocol that you want the Connect attachment to use to encapsulate packets transmitted over the network tunnels. Valid value: GRE. |
| Transport attachment ID | Select a transport channel type. Valid value: Allvbr. This value specifies that the system creates the Connect attachment between the transit router and on-premises network based on the VBR connections. |

**Step 2: Create a Connect peer**

1. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
2. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
3. On the details page of the transit router, click the **Intra-region connection management**
tab.
4. On the **Intra-region connection management** tab, click the ID of the Connect
attachment that you want to manage.
5. In the **Connection Details** panel, click **Create Peer**.
6. In the **Create Peer** dialog box, configure the parameters and click **OK**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Name | Enter a name for the Connect peer. |
| Network instance | The ID of the Connect attachment is automatically displayed. |
| Transit router local address | Enter the local address of the transit router. The local address of a transit router must be allocated from its CIDR block. You can specify an IP address from the CIDR block as the local address. If you do not specify an IP address, an IP address is automatically allocated from the CIDR block of the transit router. |
| Peer address | Enter the address of the Connect peer. Important Make sure that the transit router can access the peer address. Otherwise, the GRE tunnel cannot be created. |

**What to do next**

1. After you create a Connect attachment in the Transit Router console, you need to add the
configurations of the GRE tunnel to the local network device that functions as the Connect peer. This ensures that the GRE tunnel can be created between the transit router and the on-premises network. For more information about the configuration commands, consult the vendor of your device.
2. Connect attachments can forward only multicast packets. After the GRE tunnel is created,
you can create multicast networks between the on-premises network and virtual private clouds (VPCs). When you create a multicast network, you need to add multicast configurations both at the on-premises network side and VPC side. For more information about how to add multicast configurations to your on-premises network, consult the vendor of the peer device. For more information about how to add multicast configurations in a VPC, see Multicast overview and Create and manage a multicast network.

**Related operations**

**Delete a Connect peer**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Intra-region connection management**
tab.
6. On the **Intra-region connection management** tab, click the ID of the Connect
attachment that you want to manage.
7. In the **Connection Details** panel, find the Connect peer that you want to delete and click
**Delete** in the **Actions** column.
8. In the message that appears, review the information and click **OK**.

##### 2.2.2.4 View network instance connections

This topic describes how to view information about network instance connections.

**Procedure**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Intra-region connection management**
tab.
6. On the **Intra-region connection management** tab, view the information about the
network instance connection.

| Column | Description |
|---|---|
| Instance ID/name | The name and ID of the network instance connection. |
| Include Network instances | The ID and name of the network instance. |
| Instance type | The type of network instance. Valid values: VPC instance Border router instance Connect |

| Account | The ID of the Apsara Stack tenant account to which the network instance belongs. |
|---|---|
| Creation time | The time when the network instance connection was created. |
| Status | The status of the network instance connection. Valid values: Loaded Loading Unmounting |

#### 2.2.3 Route management

##### 2.2.3.1 Custom route tables

Transit routers support custom route tables. After you create a custom route table, you can create associated forwarding correlations, route learning correlations, or custom routes in the route table. This helps you manage traffic in a more flexible manner.

**Background information**

A transit router supports one default route table created by the system and custom route tables. The default route table of a transit router is isolated from the custom route tables. The following content describes the default route table and custom route tables: The default route table is created by the system. When you create a transit router, the system automatically creates a default route table. You can manually create custom route tables. Custom route tables are similar to virtual routing and forwarding (VRF) used by traditional routers. A custom route table is isolated from the default route table and other custom route tables. After you create a network instance connection, you can associate the network instance connection to a custom route table by creating an associated forwarding correlation. After you create an associated forwarding correlation, the transit router forwards the traffic of the network instance connection based on the custom route table.

**Create a custom route table**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click **Create a route table**. On the **Create routing table** page,
configure the parameters and click **Submit**.

| Parameter | Description |
|---|---|

| Organization | Select the organization of the transit router route table. |
|---|---|
| Resource Set | Select the resource set of the transit router route table. |
| Route table name | Enter a name for the route table. |
| Routing table description | Enter a description for the route table. |

**View the route table of a transit router**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click the route table ID.
7. On the route table details page, you can view the following information:
The route entries in the route table. For more information, see View route entries of a transit router route table. The associated forwarding correlations. For more information, see Associated forwarding. The route learning correlations. For more information, see Route learning. The routing policies. For more information, see Routing policy overview.

**Delete a custom route table**

You can delete a custom route table that you no longer use. You cannot delete the default route table. Before you delete a custom route table, make sure that the following requirements are met: The custom route table does not contain associated forwarding correlations. For more information about how to delete associated forwarding correlations, see Delete an associated forwarding correlation. The custom route table does not contain route learning correlations. For more information about how to delete route learning correlations, see Delete a route learning policy. The custom route table does not contain custom routes. For more information about how to delete custom routes, see Delete a custom route from a route table of a transit router.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click the route table ID.
7. In the **Basic routing table information** section, click **Delete**.
8. In the message, review the information and click **Delete**.

##### 2.2.3.2 Custom route entries

Route tables of transit routers support custom route entries. This topic describes how to add static or blackhole routes to the route table of a transit router to facilitate traffic management.

**Add a custom route entry**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click the route table ID. On the **Route entry** tab of the details page,
click **Create a route entry**.
7. In the **Create a route entry** dialog box, configure the parameters and click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Route entry name | Enter a name for the route entry. |
| Destination CIDR | Enter a destination CIDR block for the route. Example: 192.168.1.0/24. |
| Whether it is a black hole route | Specify whether to set the route as a blackhole route. Valid values: Yes (default): specifies the route as a blackhole route. All traffic destined for the route is dropped. No: does not specify the route as a blackhole route. If you select this option, you must specify a next hop. |
| Next Hop Connection | Select a next hop for the route entry. |
| Route entry description | Enter a description for the route entry. |

**View transit router routes**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click the ID of the route table that you want to manage.
7. On the **Route entry** tab of the route table details page, you can view the following
information about routes in the current route table.

| Parameter | Description |
|---|---|
| Target network segment | The destination CIDR block of the route entry. |
| Next hop | The network instance connection that is specified as the next hop of the route entry. |
| Type | The type of next hop. Attachment: The next hop is a network instance connection. BlackHole: The current route is a blackhole route. All traffic destined for the route is dropped. |
| Route type | The route type. Valid values: Automatic learning: The route is learned by the transit router. Static routing: The route is a static route configured by you. |
| Route status | The status of the route entry. Valid values: Available: The route is available. Rejected: The route is rejected by a routing policy associated with the route table. Candidate: The route is a standby route. When the active route is unavailable, traffic can be transmitted through the standby route. |
| Description | The description of the route entry. |

**Delete a custom transit router route**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click the ID of the route table that you want to manage.
7. On the **Route entry** tab of the details page, find the route that you want to delete and click
**Delete** in the **Actions** column.
8. In the **Delete a route entry** message, check the route and click **OK**.

##### 2.2.3.3 Associated forwarding

After you connect a network instance to a transit router, you can create an associated forwarding correlation to associate the network instance connection with a route table. After you configure an associated forwarding correlation, the transit router forwards the traffic of the network instance based on the route table.

**Background information**

The preceding figure shows how transit routers work. In this example, the transit router in the cn-qingdao-env17-d01 region is connected to VPC1 and VPC2. The VPC1 connection is associated with Route Table A, and the VPC2 connection is associated with Route Table B. A client in VPC1 wants to access a server in VPC2. The IP address of the server falls into the CIDR block 10.1.1.0/24. The following table shows the process.

| No. | Description |
|---|---|
| ① | A server in VPC1 initiates a request to a server in VPC2. The IP address of the server in VPC2 falls into the CIDR block 10.1.1.0/24. |
| ② | The VPC1 connection is associated with Route Table A. After the transit router receives the request from VPC1, the transit router queries whether Route Table A contains a route that points to the CIDR block 10.1.1.0/24. If the route exists, the request from VPC1 is forwarded to the next hop of 10.1.1.0/24. If the route does not exist, VPC1 cannot access the server in 10.1.1.0/24. |
| ③ | The transit router queries the information about the route that points to 10.1.1.0/24 in Route Table A and forwards the request to VPC2. |

| ④ | The VPC2 connection receives the request and returns an echo reply packet to VPC1. |
|---|---|
| ⑤ | The VPC2 connection is associated with Route Table B. After the transit router receives the echo reply packet from VPC2, the transit router queries whether Route Table B contains a route that points to 192.168.1.0/24. If the route exists, the echo reply packet is forwarded to the next hop of 192.168.1.0/24. If the route does not exist, VPC2 cannot send the echo reply packet to the client in VPC1. |
| ⑥ | The transit router queries the information about the route that points to 192.168.1.0/24 in Route Table B and forwards the echo reply packet to VPC1. |

**Prerequisites**

Each network instance connection can have an associated forwarding correlation with only one route table of only one transit router.

**Create an associated forwarding correlation**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click ID of the route table that you want to manage. On the details
page of the route table, click the **Associated forwarding** tab.
7. On the **Associated forwarding** tab, click **Create an associated forwarding**
**relationship**. In the **Create an associated forwarding relationship** dialog box,
configure the parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Network instance Connection ID | Select the network instance connection that you want to associate with the route table. |
| Forwarding router route table ID | By default, the current transit router route table is selected. |

**Delete an associated forwarding correlation**

**Warning**

After the associated forwarding correlation between a network instance connection and a transit router route table is deleted, the network instance can no longer use the transit router to communicate with other networks. Proceed with caution.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click ID of the route table that you want to manage. On the details
page of the route table, click the **Associated forwarding** tab.
7. On the **Associated forwarding** tab, find the network instance connection that you want to
manage and click **Disassociate a forwarding relationship** in the **Actions** column.
8. In the **Prompt** message, review the information and click **OK**.

##### 2.2.3.4 Route learning

This topic describes how to create a route learning policy for a network instance connection. After route learning is enabled between a network instance connection and a route table of a transit router, the route table of the transit router can automatically learn routes from the network instance.

**Creates a route learning policy**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click ID of the route table that you want to manage. On the details
page of the route table, click the **Route Propagation** tab.
7. On the **Routing learning** tab, click **Create a route learning relationship** . In the **Create**
**a route learning relationship** dialog box, configure the parameters and click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Network instance Connection ID | Select the network instance connection for which you want to enable route learning. |
| Forwarding router route table ID | By default, the current transit router route table is selected. |

**Delete a route learning policy**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side section, click ID of the route table that you want to manage. On the details
page of the route table, click the **Route Propagation** tab.
7. On the **Routing learning** tan, find the network instance connection that you want to delete
and click **Release route learning relationship** in the **Actions** column.
8. In the **Prompt** message, review the information and click **OK**.

##### 2.2.3.5 Routing policies

###### 2.2.3.5.1 Routing policy overview

Transit routers support routing policies. You can configure routing policies to filter and modify routes. This allows you to manage network communication in the cloud.

**How it works**

A transit router in a region contains route tables and routing policies. After a routing policy is associated with a route table of a transit router, the routing policy controls how routes in the route table are advertised. You can configure routing policies in the Ingress Regional Gateway or Egress Regional Gateway direction. Each routing policy is a collection of conditional statements and execution statements. Routing policies are sorted by priority. A smaller value indicates a higher priority. Routes are matched against match conditions specified in routing policies in descending order of policy priority. Routes that meet all match conditions are allowed or rejected based on the specified policy action. You can modify the priority, autonomous system (AS) path, and community value of an allowed route. Routes that do not match all match conditions are allowed by default.

**Components**

A routing policy consists of the following components: basic information, match conditions, and policy values. The following tables describe the details about each component.

**Note**

You can specify policy values and associated policy priorities only when **Routing Policy**
**Action** is set to **Allow**.
Table 1. Basic information

| Parameter | Description |
|---|---|

| Routing Policy Priority | The priority of the routing policy. Valid values: 1 to 100. A smaller value indicates a higher priority. You cannot specify the same priority for routing policies that apply in the same region and direction. The system matches routes against the match conditions of routing policies in descending order of priority. A smaller value indicates a higher priority. Therefore, specify proper values to sort the routing policies in the desired order. |
|---|---|
| Description | The description of the routing policy. |
| Associated Route Table | The ID of the route table that is associated with the routing policy. |
| Direction | The direction in which the routing policy applies. Ingress Regional Gateway: Routes are advertised to the transit router deployed in the current region. For example, routes are advertised from a network instance in the current region to the transit router in the current region. Egress Regional Gateway: Routes are advertised from the transit router deployed in the current region. For example, routes are advertised from the transit router in the current region to other network instances in the current region. |
| Policy Action | The action that is performed on routes which meet all match conditions. The following actions are supported: Allow: allows routes that match the routing policy. Reject: rejects routes that match the routing policy. |
| Associated Route Policy Priority | The priority of the routing policy that is associated with the current policy. This parameter is supported only if you set Action Policy to Allow. Only allowed routes are matched against the routing policy that has the specified priority. The region and direction of the routing policy to be associated must be the same as those of the current routing policy. The priority of the routing policy to be associated must be lower than the priority of the current routing policy. |

Table 2. Match conditions

| Parameter | Description |
|---|---|
| Source Region | The system checks whether routes are advertised from a specified region. The system only checks whether the source regions of the routes meet the specified condition. The destination regions of the routes are not checked. |

| Source Instance IDs | The system checks whether routes are advertised from specified network instances. The following network instance types are supported: Virtual private cloud (VPC) Virtual border router (VBR) You can select Exclude Specified IDs to specify network instance IDs that you want to exclude. If the routes are not advertised from the specified IDs, the routes match the condition. Otherwise, the routes do not match the condition. |
|---|---|
| Destination Instance IDs | The system checks whether routes are advertised to specified network instances. The following network instance types are supported: VPC VBR You can select Exclude Specified IDs to specify network instance IDs that you want to exclude. If the routes are not advertised to the specified IDs, the routes match the condition. Otherwise, the routes do not match the condition. Note The destination instance IDs take effect only when Direction is set to Egress Regional Gateway and the destination instances are deployed in the current region. |
| Source Route Table | The system checks whether routes are advertised from specified route tables. |
| Destination Route Table | The system checks whether routes are advertised to specified route tables. Note The destination route table IDs take effect only when Direction is set to Egress Regional Gateway and the destination route tables belong to network instances deployed in the current region. |
| Source Instance Type | The system checks whether routes are advertised from specified network instance types. The following network instance types are supported: VPC: VPC VBR: VBR |

| Destination Instance Type | The system checks whether routes are advertised to specified network instance types. The following network instance types are supported: VPC: VPC VBR: VBR Note The destination instance types take effect only if Direction is set to Egress Regional Gateway and the destination instance types are supported in the current region. |
|---|---|
| IP Type | The system checks whether IP addresses in routes are of the specified version. The following IP versions are supported: IPv4 IPv6 |
| Route Type | The system checks whether routes are of specified types. The following route types are supported: System: routes that are automatically created by the system. Custom: routes that are added by you. BGP: routes that are advertised over Border Gateway Protocol (BGP). |
| Route Prefix | The system filters routes based on the specified route prefixes. The following match methods are supported: Fuzzy Match: If the prefix of a route falls within one of the specified prefixes, the route matches the condition. For example, if you set the match condition to 10.10.0.0/16 and fuzzy match is applied, routes whose prefix is 10.10.10.0/24 match the condition. Exact Match: A route matches the condition only when the prefix of the route is the same as one of the specified prefixes. For example, if the match value is set to 10.10.0.0/16 and the match method is set to Exact Match, only routes whose prefix is 10.10.0.0/16 match the condition. |

| AS PATH | The system filters routes based on the specified AS path. The following match methods are supported: Fuzzy Match: A route meets the match condition if the AS path of the route overlaps with that specified in the match condition. For example, if you set the AS path to 65001, 65002 and the match method to Fuzzy Match, routes whose AS path is 65501, 65001 match the condition because both AS paths contain 65001 . Exact Match: A route meets the match condition only if the AS path of the route is the same as that specified in the match condition. For example, if you set the match condition to 65501, 65001, 60011 and the match method to Exact Match, only routes whose AS path is 65501, 65001, 60011 match the condition. Note AS path is a mandatory attribute, which describes the AS numbers that a BGP route passes through when it is advertised. |
|---|---|
| Community | The system filters routes based on the community. The following match methods are supported: Fuzzy Match: A route matches the condition if the community of the route overlaps with that specified in the match condition. For example, if you set the match condition to 65001:1000, 65002:2000 and the match method to Fuzzy Match, routes whose community is 65501:1000, 65001:1000 match the condition because both communities contain 65001:1000 . Exact Match: A route matches the condition only if the community of the route is the same as that specified in the match condition. For example, if you set the match condition to 65001:65001, 65002:65005, 65003:65001 and the match method to Exact Match, only routes whose community is 65001:65001, 65002:65005, 65003:65001 match the condition. Note Community is an optional transitive attribute. You can specify a specific community value for a specific route. Downstream routers can filter routes based on the specified community value when routing policies are applied. |

| 65501, |   |
|---|---|

|   | 65001 |   |
|---|---|---|

| 65501, 65001, |   |
|---|---|

|   | 60011 |
|---|---|

| 65001:1000, |   |
|---|---|

|   | 65002:2000 |
|---|---|

|   | 65002:65005, 65003:65001 |
|---|---|

|   | 65002:65005, 65003:65001 |
|---|---|

Table 3. Policy values

| Parameter | Description |
|---|---|

| Route Priority | The priorities of the routes that are allowed. Valid values: 1 to 100. Default value: 50. A smaller value indicates a higher priority. |
|---|---|
| Community | The community values of the routes. The following methods are supported: Add: adds the specified community value to the routes that match the routing policy. Replace: replaces the community values of the routes that match the routing policy with the specified community value. |
| Append AS Path | The AS path to be appended when the transit router receives or advertises a route. The requirements for AS paths that are appended vary based on the direction in which the routing policy applies: If the direction of a routing policy is set toI ngress Regional Gateway and you want to specify appended AS paths, you must specify source instance IDs and a source region in the match conditions. The source region that you specify must be the same region to which the routing policy applies. If the direction of a routing policy is set toE xport from Regional Gateway and you want to specify appended AS paths, you must specify Destination Instance IDs in the match conditions. |

**Matching process**

Routing policies filter routes in match-action mode. Actions are performed after conditions are matched. The system matches routes against match conditions in descending order of routing policy priority. If a route meets all the match conditions in a routing policy, the specified action is performed on the route. If you set Routing Policy Action to Allow, the route is allowed. By default, the system does not match a matched route against the next routing policy. However, if you specify a priority for the associated routing policy, the system matches the route against the routing policy that has the specified priority. If you do not specify a priority, the matching process ends. If you set Routing Policy Action to Reject, the route is rejected. By default, the system stops matching the route against the next routing policy and the matching process ends. If a route does not meet a match condition specified in a routing policy, the current matching process ends and the system matches the route against the next routing policy. If the route meets all the match conditions specified in the next routing policy, the action specified in the routing policy is performed on the route. If you set Routing Policy Action to Allow, the route is allowed. By default, the system does not match a matched route against the next routing policy. However, if you specify a priority for the associated routing policy, the system matches the route against the routing policy that has the specified priority. If you do not specify a priority, the matching process ends. If you set Routing Policy Action to Reject, the route is rejected. By default, the system stops matching the route against the next routing policy and the matching process ends. If a route does not meet a match condition specified in the next routing policy, the current matching process ends and the system matches the route against the next routing policy. The preceding processes are repeated until the system compares the route with the last routing policy. If the route does not meet a match condition specified in the last routing policy, the route is permitted.

**Default routing policy**

Each transit router contains a default routing policy that applies in the Egress Regional Gateway direction. The priority of the default routing policy is 5000, and the policy action is Reject. The default routing policy disables network communication between VBRs that are connected to the same transit router. The following section describes whether VPCs and VBRs that are connected to the same transit router can communicate with each other by default: A VPC that is connected to a transit router can communicate with VPCs and VBRs that are also connected to the transit router. A VBR that is connected to a transit router cannot communicate with other VBRs that are also connected to the transit router.

###### 2.2.3.5.2 Work with routing policies

You can create routing policies to filter and modify routes. This allows you to manage network communication in the cloud. This topic describes how to create, modify, and delete a routing policy.

**Create a routing policy**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side area of the route table details page, click the ID of the route table that you
want to manage.
7. On the details page of the route table, click the **Routing Policy** tab.
8. On the **Routing Policy** tab, click **Create a routing policy**.
9. On the **Add Routing Policy** page, configure the parameters and click **OK**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Routing Policy Priority | Specify a priority for the routing policy. Valid values: 1 to 100. A smaller value specifies a higher priority. On the same transit router, you cannot specify the same priority for different routing policies that apply in the same region and direction. The system matches routes against the match conditions of routing policies in descending order of priority. A smaller value indicates a higher priority. Set the priorities to proper values. |
| Description | Enter a description for the routing policy. |
| Associated Route Table | Select the route table that you want to associate with the routing policy. When you create a routing policy, you can associate the routing policy with the system route table or a custom route table. The routing policy affects only the advertisement of the routes in the route table. |
| Direction | Select the direction in which the routing policy applies. Ingress Regional Gateway: Routes are advertised to the transit router deployed in the current region. For example, the route is advertised from a network instance in the current region to the transit router in the current region. Egress Regional Gateway: Routes are advertised from the transit router deployed in the current region. For example, the route is advertised from the transit router in the current region to other network instances in the current region. |
| Match Conditions | Specify match conditions for the routing policy. To add multiple match conditions, click Add Match Condition. For more information, see Routing policy overview. |

| Routing Policy Action | Select an action for the routing policy. Allow: Routes that meet all the match conditions are allowed. If you select Allow, you can click Add Action Object and configure the following policy values: Route Priority: Specify a priority for the routes that are allowed. Valid values: 1 to 100. Default value: 50. A smaller value indicates a higher priority. Community: Specify a community value. Add and Replace are supported. Appended AS Path: An autonomous system (AS) path is appended when the transit router receives or advertises a route. The requirements for appended AS paths vary based on the direction in which the routing policy applies: When AS paths are appended in the inbound direction, you must specify the source instance IDs and the source region in the match condition. The source region must be the same as the region in which the routing policy applies. When AS paths are appended in the outbound direction, you must specify the destination instance IDs in the match condition. Reject: Routes that meet all the match conditions are rejected. If you select Reject, you cannot configure policy values. |
|---|---|
| Associated Route Policy Priority | Specify a priority for the routing policy that you want to associate with the current one. You can set the parameter only if Action Policy is set to Allow. Only allowed routes are matched against the routing policy that has the specified priority. The region and direction of the routing policy to be associated must be the same as those of the current routing policy. The priority of the routing policy to be associated must be lower than the priority of the current routing policy. |

**Modify a routing policy**

Before you modify a routing policy, take note of the following limits: You cannot modify the route table that is associated with the routing policy or the direction in which the routing policy applies. The routing policy created by the system cannot be modified. The priority of a routing policy created by the system is higher than 1000. If you do not want the default routing policy to take effect, you must add a custom routing policy that has a higher priority than the default routing policy.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side area on the **Forwarding router routing table** tab, click the ID of the route
table that you want to manage. On the route table details page, click the **Routing Policy** tab, and find the routing policy that you want to modify.
7. In the **Actions** column, click **Edit**.
8. On the **Edit Routing Policy** page, modify the policy priority, description, match conditions,
and action and click **Submit**.

**Delete a routing policy**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, click the ID of the CEN instance that you want to manage.
4. On the details page of the CEN instance, click the **Basic information** tab and click the ID of
the transit router that you want to manage.
5. On the details page of the transit router, click the **Forwarding router routing table** tab.
6. In the left-side area of the **Forwarding router routing table** tab, click the ID of the route
table that you want to manage. On the details page of the route table, click the **Routing**
**Policy** tab and find the routing policy that you want to delete.
7. In the **Actions** column, click **Delete**.
8. In the **Prompt** message, click **OK**.

#### 2.2.4 Multicast management

##### 2.2.4.1 Multicast overview

Multicast is supported by transit routers. After you connect a transit router to network instances, you can use the transit router to enable and manage multicast. The transit router also forwards multicast packets. This topic describes how multicast works, the limits of multicast, and how to use multicast.

**Background information**

**What is multicast?**

Multicast is a type of group communication where the same data packet is transmitted to a group of destination clients. Multicast is commonly used in live streaming, video conferencing, financial transaction data synchronization, online education, and streaming television.

**Benefits**

Compared with unicast and broadcast, multicast can reduce workloads on servers and increase bandwidth utilization in one-to-many network communication scenarios. In the following example, live streaming is used to show the differences between unicast and multicast, and the benefits of multicast.

**Note**

The differences between broadcast and multicast are not discussed in this topic. You can research the differences if needed. How unicast works In unicast scenarios, the live streaming server must transmit two packets: Unicast Packet 1 and Unicast Packet 2. The router then forwards Unicast Packet 1 to Client 3 and Unicast Packet 2 to Client 4, as shown in the following figure. How multicast works In multicast scenarios, you can add the live streaming server and the clients to the same multicast group. When the server transmits a data packet to Client 3 and Client 4, only one data packet (Multicast Packet 1) needs to be transmitted to the multicast group. The packet is forwarded by the multicast routers and replicated on the multicast routers that are nearest to the clients. The number of replicas is determined by the number of clients in the multicast group. After the packet is replicated, the multicast routers forward the replicas to the clients, as shown in the following figure. In unicast scenarios, the live streaming server must transmit a packet to every client. The routers must forward every packet. The workloads on the server and the bandwidth usage greatly increase as the number of clients grows. In multicast scenarios, the live streaming server and the clients can be added to the same multicast group. The server needs to transmit only one packet to the multicast group. The multicast routers need to forward only one packet. The packet is replicated on the multicast routers that are nearest to the clients. Multicast can reduce server workloads and bandwidth usage even if the number of clients is large.

**Features and advantages**

This section describes the use scenarios and terms of multicast.

**Scenarios**

After you enable multicast for a transit router, you can create and manage multicast networks in the following scenarios: Create a multicast network in a virtual private cloud (VPC), as shown in Multicast Network 1 in Figure 1. Create a multicast network among VPCs that are deployed in the same region, as shown in Multicast Network 2 in Figure 1. Create a multicast network between an on-premises network and a VPC, as shown in Figure 2. Figure 1: Figure 1_Create a multicast network on Apsara Stack Figure 2: Figure 2_Create a multicast network between an on-premises network and a VPC

**Terms**

The following table describes the terms of multicast.

| Term | Description |
|---|---|
| Multicast Domain | A multicast domain defines the scope of a multicast network in a region. Only resources in the same multicast domain can transmit or receive multicast packets. You can create multiple multicast domains on a transit router. The multicast domains in the same region are isolated from each other. |

| Multicast group | A multicast group consists of resources that transmit, replicate, and receive packets. A multicast group is identified by its IP address. Each multicast domain supports multiple multicast groups. However, the IP address of each multicast group must be unique. Multicast groups cannot communicate with each other. You can assign the same multicast IP address to multicast groups that are created in different multicast domains. |
|---|---|
| Multicast source | A multicast source in a multicast group transmits multicast packets. |
| Multicast member | A multicast member in a multicast group receives multicast packets. |

**Prerequisites**

Multicast is supported by transit routers by default. The elastic network interfaces (ENIs) created by transit routers in VPCs cannot be added to multicast networks. An ENI can be a multicast source and a multicast member in the same multicast group. Only the primary private IP address of an ENI can be used as a multicast object. Other IP addresses of the ENI do not support multicast.

**Procedure**

For more information, see Create and manage a multicast network.

##### 2.2.4.2 Create and manage a multicast domain

This topic describes how to use a transit router to create and manage a multicast domain.

**Create a multicast domain**

1. Log in to the CEN console.
2. In the top navigation bar, select the region in which the CEN instance resides.
3. In the left-side navigation pane, click **CEN Instance**.
4. On the **Cen instance** page, find the CEN instance that you want to manage and click its ID
in the **Cen ID/name** column.
5. On the **Cen instance details** page, click the **Basic information** tab.
6. In the transit router list below the **Basic information** section, find the transit router that
you want to manage and click its ID in the **Instance ID/name** column.
7. On the **Forwarding router details** page, click the **Multicast** tab
8. In the left-side section, click **Create a multicast domain**.
9. In the **Create a multicast domain** dialog box, configure the parameters and click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|

| Forwarding router | The ID of the transit router in the current region is displayed by default. |
|---|---|
| Multicast Domain name | Enter a name for the multicast domain. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter but cannot start with http:// or https://. |
| Description | Enter a description for the multicast domain. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://. |

**What to do next**

**Manage multicast domains**

1. On the **Multicast** tab, click the ID of the multicast domain that you want to manage in the
left-side multicast domain list. You can perform fuzzy match to search for multicast domains by ID.
2. In the **Basic multicast domain information** section, view the basic information about the
multicast domain and manage the multicast domain. In the **Basic multicast domain information** section, find the **Multicast Domain name** parameter, move the pointer over the parameter value, and then click the icon to modify the name of the multicast domain. In the **Basic multicast domain information** section, find the **Description** parameter, move the pointer over the parameter value, and then click the icon to modify the description of the multicast domain. In the **Basic multicast domain information** section, click **Delete** in the upper-right corner to delete the multicast domain.

**Note**

Before you delete a multicast domain, make sure that the following requirements are met: The multicast domain is disassociated from all vSwitches. For more information about how to disassociate a vSwitch, see the "Disassociate a vSwitch" section in the Manage vSwitches topic. All multicast sources and members are removed from the multicast domain. For more information about how to remove multicast sources and members, see Delete a multicast group. Click the **Switch** tab to manage the multicast domain and its vSwitches. For more information, see Manage vSwitches. Click the **Multicast group** tab to manage multicast sources and members in the multicast domain. For more information, see Crate and manage a multicast group.

##### 2.2.4.3 Manage vSwitches

After you create a multicast domain, you can associate it with one or more vSwitches to specify the scope of the multicast network. If you want to remove a vSwitch from a multicast domain, you can disassociate the vSwitch from the multicast domain.

**Associate with a vSwitch**

You can repeat the following steps to associate the multicast domain with vSwitches of different virtual private clouds (VPCs).
1. Log in to the CEN console.
2. In the top navigation bar, select the region in which the CEN instance resides.
3. In the left-side navigation pane, click **CEN Instance**.
4. On the **Cen instance** page, find the CEN instance that you want to manage and click its ID
in the **Cen ID/name** column.
5. On the **Cen instance details** page, click the **Basic information** tab.
6. In the transit router list below the **Basic information** section, find the transit router that
you want to manage and click its ID in the **Instance ID/name** column.
7. On the **Forwarding router details** page, click the **Multicast** tab
8. In the left-side multicast domain list, click the ID of the multicast domain that you want to
manage.
9. In the **Basic multicast domain information** section, click the **Switch** tab.
0. Click **Bind a switch**.
1. In the **Bind a switch** dialog box, configure the parameters and click **OK**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| VPC | Select the VPC to which the vSwitch belongs. |
| Switch | Select the vSwitch that is used to forward multicast packets. You can select multiple vSwitches in a VPC. |

**What to do next**

**Disassociate from a vSwitch**

**Note**

Before you disassociate a multicast domain from a vSwitch, make sure that the vSwitch does not contain a multicast source or a multicast member. For more information about how to remove multicast sources and members, see Delete a multicast group.
1. On the **Switch** tab, find the vSwitch from which you want to disassociate the multicast
domain and click **Unbind** in the **Actions** column.
2. In the **Unbind Switch** message, click **OK**.

##### 2.2.4.4 Multicast group

This topic describes how to create and manage multicast sources and multicast members.

**Create a multicast source**

1. Log in to the CEN console.
2. In the top navigation bar, select the region in which the CEN instance resides.
3. In the left-side navigation pane, click **CEN Instance**.
4. On the **Cen instance** page, find the CEN instance that you want to manage and click its ID
in the **Cen ID/name** column.
5. On the **Cen instance details** page, click the **Basic information** tab.
6. In the transit router list below the **Basic information** section, find the transit router that
you want to manage and click its ID in the **Instance ID/name** column.
7. On the **Forwarding router details** page, click the **Multicast** tab
8. In the multicast domain list on the left, find the target multicast domain, and click the
multicast domain ID.
9. Click **Create Multicast Source**.
0. In the **Create Multicast Source** dialog box, configure the following parameters and click
**OK**.

| Parameter |   | Description |
|---|---|---|
| Transit router |   | The system automatically displays the ID of the transit router in the current region. |
| Multicast domain |   | The system automatically displays the ID of the selected multicast domain. |
| Multicast group informatio n | Select multicast group | Select the multicast group to which the multicast source belongs. Note After a multicast group is created, you cannot modify the IP address of the multicast group. Create a new multicast group: Select this option if no multicast group exists in the current multicast domain. New multicast group IP address: Enter an IP address to create a new multicast group. Valid values: 224.0.0.1 to 239.255.255.254. Each multicast group is identified by its multicast IP address. Use an existing multicast group: Select this option if a multicast group already exists in the current multicast domain. Existing multicast group IP address: Select an existing multicast group. The new multicast source will be added to this group. |

| Multicast source informatio n | Resource type | Select the resource type of the multicast source. Elastic network interface: You can specify an elastic network interface (ENI) that is attached to an ECS instance as the multicast source. After you select the ENI, the system uses the primary private IP address of the ENI to send multicast traffic to the multicast group. vSwitch: Select the vSwitch where the multicast source is located. Elastic network interface: Select an ENI in the vSwitch. This ENI functions as the multicast source. You can select multiple ENIs in a vSwitch. Secondary ENIs are supported. Note If you select a secondary ENI in an Alibaba Cloud Container Service for Kubernetes (ACK) scenario, the transit router (TR) does not support dynamically adding multicast members. You must statically specify the multicast members. Connect: You can use on-premises resources as the multicast source. These resources send multicast traffic to the multicast group through a specified Connect attachment. Connect attachment ID: Select the Connect attachment for the multicast source. Peer attachment ID: Select the Connect peer for the multicast source. You can select multiple Connect peers under a single Connect attachment. |
|---|---|---|

**Create a multicast member**

1. Log in to the CEN console.
2. In the top navigation bar, select the region in which the CEN instance resides.
3. In the left-side navigation pane, click **CEN Instance**.
4. On the **Cen instance** page, find the CEN instance that you want to manage and click its ID
in the **Cen ID/name** column.
5. On the **Cen instance details** page, click the **Basic information** tab.
6. In the transit router list below the **Basic information** section, find the transit router that
you want to manage and click its ID in the **Instance ID/name** column.
7. On the **Forwarding router details** page, click the **Multicast** tab
8. Find the target multicast domain in the multicast domain list on the left and click the
multicast domain ID.
9. Click **Create Multicast Member**.
0. In the **Create Multicast Member** dialog box, configure the parameters based on the
following information, and click **OK**.

| Parameter | Description |
|---|---|

| Transit router |   | The system automatically displays the ID of the transit router in the current region. |
|---|---|---|
| Multicast domain |   | The system automatically displays the ID of the selected multicast domain. |
| Multicast group informatio n | Select multicast group | Select the multicast group to which the multicast member belongs. Note After a multicast group is created, you cannot modify the IP address of the multicast group. Create a new multicast group: Select this option if no multicast group exists in the current multicast domain. New multicast group IP address: Enter an IP address to create a new multicast group. Valid values: 224.0.0.1 to 239.255.255.254. Each multicast group is identified by its multicast IP address. Use an existing multicast group: Select this option if a multicast group already exists in the current multicast domain. Existing multicast group IP address: Select an existing multicast group. The new multicast member will be added to this group. |
| Multicast member informatio n | Resource type | Select the resource type of the multicast member. Elastic network interface: You can specify an ENI attached to an ECS instance as a multicast member. After you select the ENI, it can receive multicast traffic from the multicast group. vSwitch: Select the vSwitch where the multicast member is located. Elastic network interface: Select an ENI in the vSwitch. This ENI functions as the multicast member. You can select multiple ENIs in a vSwitch. Connect: You can use on-premises resources as multicast members. These resources receive multicast traffic from the multicast group through a specified Connect attachment. Connect attachment ID: Select the Connect attachment for the multicast member. Peer attachment ID: Select the Connect peer for the multicast member. You can select multiple Connect peers under a single Connect attachment. |

**More operations**

**Delete a multicast source or member**

If a multicast source or member no longer needs to send or receive multicast traffic, you can remove it from the multicast group.

| Actions | Steps |
|---|---|
| Delete a multicast source | 1. On the Multicast tab, find the target multicast source and click Delete in the Actions column. Multicast sources are identified by Static in the Multicast source type column. 2. In the Delete multicast source dialog box, click OK. |
| Delete a multicast member | 1. On the Multicast tab, find the target multicast member and click Delete in the Actions column. Multicast members are identified by Static in the Multicast member type column. 2. In the Delete multicast member dialog box, click OK. |

### 2.3 Tag management

When you use transit routers, you can use tags to mark and classify Cloud Enterprise Network (CEN) instances. Tags facilitate resource search and aggregation. This topic describes how to manage and use tags.

**Tag overview**

As the number of CEN instances increases, management of CEN instances becomes more complex. To facilitate instance search and filtering, you can use tags to group CEN instances. Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following items: Each tag key that is added to an instance must be unique. You can modify the key and value of a tag or remove a tag from an instance. If you delete an instance, all tags added to the instance are also deleted. This operation does not affect the tags added to other instances. You can add up to 20 tags to an instance. This quota cannot be increased.

**Add tags to a CEN instance**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. The following steps show how to add tags to CEN instances on the **CEN Instance** page:
Add tags to a single CEN instance. a. On the **CEN Instance** page, find the CEN instance that you want to manage and click the icon in the **Tag** column. b. In the **Edit Tags** dialog box, specify the tag keys and values and click **OK**.

| Parameter | Description |
|---|---|
| Tag Key | The key of a tag. You can select or enter a key. |
| Tag Value | The value of a tag. You can select or enter a value. |

c. In the **Edited** message, check the tag information and click **Close**. Add tags to multiple CEN instances at the same time. a. On the **CEN Instance** page, select the IDs of the CEN instances that you want to manage and click **Batch Add Tags** below the instance list. b. In the **Batch Add Tags** dialog, configure the **Tag Key** and **Tag Value** parameters and click **OK**. c. In the **Edited** message, check the tag information and click **Close**.

**Search for CEN instances by tag**

After you add tags to CEN instances, you can search CEN instances by tag.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, choose **Advanced Filter > Filter by Tag**.
4. In the dialog box that appears, select tag keys and tag values and click **Search**. The CEN
instances that have the specified tag keys and tag values are displayed.

**Modify CEN instance tags**

After you add a tag to a CEN instance, you can add more tags to the CEN instance, modify the tags, or remove the tags from the CEN instance.
1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. On the **CEN Instance** page, perform the following steps to manage CEN instance tags:
Modify the tags of a single CEN instance a. On the **CEN Instance** page, find the CEN instance that you want to manage and click the icon in the **Tag** column. b. In the **Edit Tags** dialog box, perform the following operations and click **OK**: Add tags: You can add more tags to the CEN instance. Modify a tag: You can select a tag and modify the tag key or tag value. Remove a tag: You can click the icon on the right side of a tag to remove the tag from the CEN instance. c. In the **Edited** message, check the tag information and click **Close**. Remove tags from multiple CEN instances a. On the **CEN Instance** page, select the IDs of the CEN instances that you want to manage and click **Batch Remove Tags** below the instance list. b. In the **Batch Remove Tags** dialog box, select the tags that you want to remove from the CEN instances. c. In the **Edited** message, check the tag information and click **Close**. cks

## 3 Configure health checks

You can connect virtual border routers (VBRs) to data centers by using Express Connect circuits. After you connect a VBR to a transit router, you can run health checks to probe the availability of the Express Connect circuit.

**Background information**

**How it works**

After you enable health checks for a VBR, a ping packet is transmitted from the source IP address of health checks to the destination IP address in the data center every 2 seconds. If the ping packets are returned from the **Express Connect circuit**, the Express Connect circuit is declared healthy. If the Express Connect circuit **does not respond to eight**
**consecutive ping packets, or the ping packets are returned from other routes**, the
Express Connect circuit is declared unhealthy.

**Warning**

Make sure that the destination IP address of health checks is reachable and the data center does not throttle or block ping packets. If a throttling mechanism, such as Control Plane Policing (CoPP) or local attack defense, is enabled for the gateway devices in the data center, ping packets may be dropped. As a result, the system may frequently switch between Express Connect circuits. We recommend that you disable throttling for the gateway devices in the data center.

**Usage notes on standby Express Connect circuits**

cks If a data center is connected to Alibaba Cloud through multiple Express Connect circuits, we recommend that you configure health checks for each Express Connect circuit. If one of the Express Connect circuits is declared unhealthy by health checks, the system automatically switches network traffic to a healthy Express Connect circuit. When you configure health checks, you can specify whether to enable **automatic route**
**switchover**.

**Prerequisites**

The VBR that is associated with an Express Connect circuit is connected to a transit router. For more information, see Connect VBRs.

**Step 1: Configure health checks in the Transit Router console**

1. Log on to the Transit Router console.
2. In the top navigation bar, select the organization and resource set to which the CEN
3. In the left-side navigation pane, click **Health Check**.
4. On the **Health Check** page, click **Set health check**.
5. In the **Set health check** dialog box, configure the parameters and click **OK**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Cen instance | Select the Cloud Enterprise Network (CEN) instance to which the transit router of the VBR belongs. |
| Border Router | Select the VBR that you want to monitor. |
| SOURCE IP | Enter the source IP address of health checks. You can specify an available IP address that falls within the 10.0.0.0/8, 192.168.0.0/16, or 172.16.0.0/12 CIDR block. The specified IP address must not conflict with the destination IP address, the IP address of the VBR on the Alibaba Cloud side, or the IP address of the VBR on the customer side. |
| Destination IP | Set the destination IP address to the IP address of the VBR on the customer side. |
| Contract issuing interval (seconds) | Enter a time interval at which probe packets are sent during the health check. Unit: seconds. Valid values: 2 to 3. Default value: 2. |
| Number of probe packets | Enter the number of consecutive probe packets that are sent during the health check. Unit: packets. Valid values: 3 to 8. Default value: 8. |

cks

| Switch route | Specifies whether to allow the health check feature to switch to the redundant route. This feature is enabled by default. If a redundant route is configured on the CEN instance, the health check feature immediately switches to the redundant route if an error is detected on the Express Connect circuit. If you disable this feature, health checks perform only probing. The health check feature does not switch to the redundant route even if an error is detected on the Express Connect circuit. Warning Before you disable this feature, make sure that network traffic can be switched to a standby route by using other mechanisms. Otherwise, network connections are interrupted if the Express Connect circuit fails. |
|---|---|

**Step 2: Configure health checks in the data center**

You also need to configure health checks in the data center to ensure that health checks can run as expected.
1. Add a backhaul route for health check ping packets in the data center.

**Important**

If the VBR uses BGP, Alibaba Cloud automatically advertises the source IP address of the health check as a route whose subnet mask is 32 bits in length to the data center after the health check is configured. In this case, you do not need to add a backhaul route. If the VBR uses static routes, you must manually add a route whose destination CIDR block is the source IP address of the health check, subnet mask is 32 bits in length in the data center, and next hop points to the Express Connect circuit. Otherwise, the ping packets cannot be returned through the Express Connect circuit, which will be declared unhealthy. The following example shows how to add a backhaul route. The example is for reference only. For more information about the configuration commands, consult the vendor of your gateway device.

```
#Configure a backhaul route for probe packets.
ip route <The source IP address of the health check> 255.255.255.255 <The IP address of the VBR on the Alibaba Cloud side>
```

2. Add health check configurations to the data center.
You can use Bidirectional Forwarding Detection (BFD) or a network quality analyzer (NQA) to add health check configurations. This ensures that you can test the network connectivity of the Express Connect circuit from the data center. For more information about the configuration commands, consult the vendor of your gateway device.
3. Enable automatic route switchover in the data center.
If your data center is connected to Alibaba Cloud through multiple Express Connect circuits, you need to enable automatic route switchover during health checks in your data center to ensure that you can test the connectivity of the Express Connect circuits from the data center, and the system can switch between routes based on health check results. For more information about the configuration commands, consult the vendor of your gateway device. cks

**What to do next**

| Operation | Description | Procedure |
|---|---|---|
| Modify health checks | After you add a health check rule, you can modify the source IP address, destination IP address, probe interval, and the number of probe packets. Note The status of the Change Route feature cannot be changed. If you want to turn on or turn off Change Route, delete the health check and create another health check. | 1. Log on to the Transit Router console. 2. In the top navigation bar, select the organization and resource set to which the CEN instance belongs. 3. In the left-side navigation pane, click Health Check. 4. On the Health Check page, find the health check that you want to modify and click Edit in the Actions column. 5. In the Edit health check dialog box, modify the source IP address, destination IP address, probe interval, and number of probe packets and click OK. |
| Delete health checks | If you no longer need to monitor the connectivity of an Express Connect circuit, you can delete the health check. | 1. Log on to the Transit Router console. 2. In the top navigation bar, select the organization and resource set to which the CEN instance belongs. 3. In the left-side navigation pane, click Health Check. 4. On the Health Check page, find the health check that you want to delete and click Delete in the Actions column. 5. In the Delete message, click Delete. |

**FAQ**

**In a scenario where multiple VBRs are connected to a transit**

**router, what granularity is the redundancy between Express**

**Connect circuits?**

The Express Connect circuits perform failover based on routes. For example, VBR1 and VBR2 are connected to a transit router and the routes in the following table are added to the route table of the transit router. In this case, network traffic is switched between VBR1 and VBR2: If VBR1 fails health checks, network traffic that is destined for 192.168.1.0/24 is switched from VBR1 to the Express Connect circuit connected to VBR2. If VBR2 fails health checks, network traffic that is destined for 192.168.1.0/24 is switched from VBR2 to the Express Connect circuit connected to VBR1. However, network traffic that is destined for 192.168.2.0/24 is not switched to VBR1.

| Destination CIDR block | Next hop | Network instance associated with the next hop |
|---|---|---|

cks

| 192.168.1.0/24 | VBR1 connection | VBR1 |
|---|---|---|
| 192.168.1.0/24 | VBR2 connection | VBR2 |
| 192.168.2.0/24 | VBR2 connection | VBR2 |

**In a scenario where multiple VBRs are connected to a transit**

**router and Express Connect circuits are redundant with each**

**other, will traffic be interrupted if all the VBRs fail health**

**checks?**

By default, network traffic destined for Alibaba Cloud is transmitted through the Express Connect circuit connected to the last VBR. If the last VBR fails health checks but the Express Connect circuit works as expected, the bandwidth for network traffic from Alibaba Cloud to the data center is reduced because only one Express Connect circuit remains functional. If the last VBR fails health checks and the Express Connect circuit is also declared unhealthy, network traffic from Alibaba Cloud to the data center is interrupted. The last VBR refers to the last VBR that fails health checks. For example, VBR1, VBR2, and VBR3 are connected to a transit router and the routes in the following table are added to the route table of the transit router. The system first detects that VBR1 and VBR2 failed health checks, and then the system detects that VBR3 failed health checks. In this case, the last VBR refers to VBR3. Network traffic from Alibaba Cloud to the data center is transmitted through the Express Connect circuit connected to VBR3.

| Destination CIDR block | Next hop | Network instance associated with the next hop |
|---|---|---|
| 192.168.1.0/24 | VBR1 connection | VBR1 |
| 192.168.1.0/24 | VBR2 connection | VBR2 |
| 192.168.1.0/24 | VBR3 connection | VBR3 |

How network traffic from the data center to Alibaba Cloud is transmitted is determined by your network configurations.

**In a scenario where multiple VBRs are connected to a transit**

**router and Express Connect circuits are redundant with each**

**other, is a route switchover performed if all the VBRs fail**

**health checks?**

Whether the system switches to another route is determined by the connectivity of the Express Connect circuit. A route switchover is performed only when the health status of the Express Connect circuit is changed. cks

**Does the deletion of health check configurations cause**

**frequent route switchover or traffic interruptions?**

If you delete health check configurations in the Transit Router console, the deletion does not cause frequent route switchover. By default, the system considers the Express Connect circuit healthy and continues forwarding network traffic to the Express Connect circuit based on specified routes. However, network traffic will be interrupted if the Express Connect circuit is faulty. If you delete health check configurations in the data center, whether the traffic will be interrupted is determined by your network configurations.

## 4 View operation logs

Cloud Enterprise Network (CEN) allows you to view the operation logs of a CEN instance, which record the instance status, operation sources, operation time, and API call details. You can analyze and trace historical operations based on the operation logs.

**Procedure**

1. Log in to the CEN console.
2. In the top navigation bar, select the region in which the CEN instance resides.
3. Use one of the following methods to view the operation logs of a CEN instance:
View operation logs through the navigation pane. a. In the left-side navigation pane, click **Operation Log**. b. On the **Operation Log** page, view the operation event list, including **Operation Time**,
**Operator**, **Resource Type**, **IP Address**, **Operation Name**, **Read/Write Type**,
**Operation Result**, **Call Source**, **Organization**, and **Resource Set**.
Click **Advanced Filter** to filter operation logs by specifying filter conditions. The following table describes the filter conditions.

| Filter condition | Description |
|---|---|
| Resource Type | The resource type. Set the value to CEN Instance. |
| Event Type | The event type. You can select an event type based on the setting of Resource Type. Valid values: Delete Events, Create Events, Query Events, and Modify Events. |
| Time Range | The time range that you want to query. By default, the current month is selected. |
| Resource ID | The ID of the resource instance. |
| IP Address | The IP address of the operation. |
| Read/Wri te Type | The type of the operation. Valid values: Read Operation and Write Operation. |
| Operatio n Result | The result of the operation. Valid values: Successful and Failed. |
| Keyword | The keyword. You can enter an event ID, resource ID, source IP address, or operation name. |

Find the operation that you want to manage and click **View** in the **Details** column. In the **View Operation Details** panel, view information in the **Basic Information** and
**Instance Details** sections.
View the operation logs of a single CEN instance on the instance details page. a. In the left-side navigation pane, click **CEN Instance**. b. On the **Cen instance** page, find the CEN instance that you want to manage and click its ID in the **Cen ID/name** column. c. On the details page of a CEN instance, click the **Operation Log** tab to view the operation logs of the instance. The operation event list includes the following information: **Operation Name**,
**Operator**, **Execution Status**, **Operation Source**, **Operation Type**, **Operation**
**Source IP Address**, and **Operation Time**.

**Note**

Operation logs are retained for seven days. To adjust the retention period, modify the logging configurations in Configurations > Log Storage Settings as an administrator. If you extend the retention period by modifying the logging configurations, the log data before the modification is not backfilled. Up to 100 pages of records can be displayed in the list, and up to 100 records can be displayed on each page. If more than 10,000 records are available, specify filter conditions to filter the records. Click **Advanced Filter** to filter operation logs that you want by specifying filter conditions such as **Operation Name** and **Operator**.

| Filter condition | Description |
|---|---|
| Operator | The operator that performed the operation. |
| Operation Name | The name of the operation, which is the API operation name. |
| Execution Status | The status of the operation. Valid values: Success and Failed. |
| Operation Source IP Address | The source IP address of the operation. |
| Operation Time | The time range that you want to query. |

Find the operation event that you want to view and click **Operation Details** in the
**Operation** column to view the operation details.
